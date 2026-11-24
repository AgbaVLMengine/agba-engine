#!/usr/bin/env python3
"""
scripts/audit_ui_dom_integrity.py
Headless Client-Side DOM Parity & Cross-Domain Integrity Benchmark.
Gate 2 Compliant: Under 250 LOC. Standard Library + Node.js subprocess.
"""
import hashlib, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = ROOT / "web/src/data/yoruba_master_corpus.json"
EXPECTED_SHA = "046967bb616b5ede65a242290568a4216dc6bb1a3d45ae8365840443edc9d80c"
EXPECTED_COUNT = 1398

NODE_SCRIPT = r"""
import fs from 'fs';
import path from 'path';

const ROOT = process.argv[1];
const corpus = JSON.parse(fs.readFileSync(path.join(ROOT, 'web/src/data/yoruba_master_corpus.json'), 'utf8'));

// Load tonalContour code
const tonalCode = fs.readFileSync(path.join(ROOT, 'web/src/utils/tonalContour.js'), 'utf8');

// Load ontologyClassifier code and bundle with tonalContour inline
const ontologyRaw = fs.readFileSync(path.join(ROOT, 'web/src/utils/ontologyClassifier.js'), 'utf8');
const ontologyMerged = tonalCode + '\n' + ontologyRaw.replace(/import\s+{[^}]+}\s+from\s+'\.\/tonalContour';?/, '');
const ontologyUri = 'data:text/javascript;base64,' + Buffer.from(ontologyMerged).toString('base64');
const { getOntologicalClassification, ONTOLOGICAL_TIER } = await import(ontologyUri);

// Load relativesResolver
const relUri = path.join(ROOT, 'web/src/utils/relativesResolver.js');
const { resolveKnowledgeGraphRelatives } = await import(relUri);

// Load subVariantHydrator bundled with subVariantKnowledge
const hydratorRaw = fs.readFileSync(path.join(ROOT, 'web/src/utils/subVariantHydrator.js'), 'utf8');
const knowledgeRaw = fs.readFileSync(path.join(ROOT, 'web/src/utils/subVariantKnowledge.js'), 'utf8');
const hydratorMerged = knowledgeRaw + '\n' + hydratorRaw.replace(/import\s+{[^}]+}\s+from\s+'\.\/subVariantKnowledge\.js';?/, '');
const hydratorUri = 'data:text/javascript;base64,' + Buffer.from(hydratorMerged).toString('base64');
const { hydrateSubVariantFromParent, findSubVariantMatchInCorpus } = await import(hydratorUri);

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}
function normalizeNFC(s) {
  return (s || '').trim().toLowerCase().normalize('NFC');
}

function search(q) {
  const qClean = (q || '').replace(/[?!.,;:'"_\-()[\]]/g, ' ').replace(/\s+/g, ' ').trim();
  const normQ = normalizeNFC(qClean);
  const qStripped = stripAccents(qClean);
  const hasQueryDiacritics = normQ !== qStripped;
  const scored = [];

  for (const entity of corpus) {
    const title = entity.title || '';
    const normTitle = normalizeNFC(title);
    const titleStripped = stripAccents(title);
    const aliases = entity.aliases || [];
    let score = 0;

    if (normTitle === normQ) score += 600;
    else if (!hasQueryDiacritics && titleStripped === qStripped) score += 540;
    else if (normTitle.startsWith(normQ)) score += 360;
    else if (!hasQueryDiacritics && titleStripped.startsWith(qStripped)) score += 320;

    const aliasExact = aliases.some((a) => normalizeNFC(a) === normQ);
    const aliasStrippedExact = !hasQueryDiacritics && aliases.some((a) => stripAccents(a) === qStripped);
    if (aliasExact) score += 420;
    else if (aliasStrippedExact) score += 380;

    const baseTitle = title.split('(')[0].trim();
    if (baseTitle && baseTitle !== title) {
      if (normalizeNFC(baseTitle) === normQ) score += 560;
      else if (!hasQueryDiacritics && stripAccents(baseTitle) === qStripped) score += 500;
    }

    if (score > 0) scored.push({ entity, score });
  }
  scored.sort((a, b) => b.score - a.score);
  return scored;
}

const errors = [];
function check(cond, msg) {
  if (!cond) errors.push(msg);
}

// 1. Invariant: Corpus Total Entity Count
check(corpus.length === 1398, `Expected 1398 entities, got ${corpus.length}`);

// 2. Vector 1: Mathematical Disjointness Sentinel across Category 1 on disk (Cell 4 ∩ Cell 6 = ∅)
const cat1 = corpus.filter(e => e.category === 'Spiritual & Cosmological Matrix');
for (const e of cat1) {
  const svs = new Set((e.sub_variants || []).map(s => typeof s === 'string' ? s : s.title));
  const rels = new Set(e.related_entities || []);
  const inter = [...svs].filter(x => rels.has(x));
  check(inter.length === 0, `Cell 4 / Cell 6 overlap in ${e.id}: ${inter.join(', ')}`);
}

// 3. Vector 2: Òrìṣà Pantheon Expansion (18 sub-variants + reciprocal sovereign_parent)
const orisa = corpus.find(x => x.id === 'Òrìṣà');
check(orisa, `Òrìṣà sovereign parent missing`);
check((orisa?.sub_variants || []).length === 18, `Òrìṣà expected 18 sub-variants, got ${(orisa?.sub_variants || []).length}`);
for (const child of ['Yewá', 'Aganjù', 'Nàná Burúkú']) {
  check((orisa?.sub_variants || []).includes(child), `${child} missing from Òrìṣà.sub_variants`);
}
for (const cid of ['Yewá', 'CORPUS_AGANJU_001', 'CORPUS_NANA_BURUKU_001']) {
  const c = corpus.find(x => x.id === cid);
  check(c, `Entity ${cid} missing from corpus`);
  check(c?.sovereign_parent === 'Òrìṣà', `${cid} expected sovereign_parent 'Òrìṣà', got '${c?.sovereign_parent}'`);
}

// 4. Vector 3: Orthographic Elevation of 8 Entities & Searchability
const elevatedMap = [
  ['ofo', 'Ofò'], ['aje saluga', 'Ajé Ṣàlúgà'], ['sigidi', 'Sìgìdì'],
  ['alafia', 'Àlàáfíà'], ['osun-oso', 'Ọ̀ṣun-Ọ̀ṣọ́'], ['iyamode', 'Ìyámòdè'],
  ['opa-ogun', 'Ọ̀pá Ògún'], ['orun osoosi', 'Ọrún Ọ̀ṣọ́ọ̀sì']
];
for (const [q, canonical] of elevatedMap) {
  const ent = corpus.find(x => x.title === canonical);
  check(ent, `Elevated canonical entity '${canonical}' missing from corpus`);
  const sRes = search(q);
  check(sRes[0]?.entity?.title === canonical, `Search '${q}' expected Top-1 '${canonical}', got '${sRes[0]?.entity?.title}'`);
}

// 5. Vector 4: Royal Herald Akígun Canonical Ingestion & Depth
const akigun = corpus.find(x => x.id === 'akigun');
check(akigun, `Akígun missing from corpus`);
check(akigun?.title === 'Akígun', `Akígun title mismatch: ${akigun?.title}`);
check(akigun?.sovereign_parent === 'Àṣẹ-Ọ̀rọ̀', `Akígun sovereign_parent expected 'Àṣẹ-Ọ̀rọ̀', got '${akigun?.sovereign_parent}'`);
const akigunDepth = (akigun?.description || '').length + (akigun?.etymology_and_philosophy || '').length;
check(akigunDepth >= 600, `Akígun depth ${akigunDepth} < 600 chars`);
check((akigun?.proverbs_and_oral_traditions || []).length >= 3, `Akígun proverbs < 3`);

// 6. Vector 5: Aliasing for Èṣù & Ìba
const resExu = search('exu');
check(resExu[0]?.entity?.id === 'Èṣù', `Search 'exu' expected 'Èṣù', got '${resExu[0]?.entity?.id}'`);
const resEchu = search('echu');
check(resEchu[0]?.entity?.id === 'Èṣù', `Search 'echu' expected 'Èṣù', got '${resEchu[0]?.entity?.id}'`);
const resLaroye = search('laroye');
check(resLaroye[0]?.entity?.id === 'Èṣù', `Search 'laroye' expected 'Èṣù', got '${resLaroye[0]?.entity?.id}'`);
const resIbaSe = search('iba se');
check(resIbaSe[0]?.entity?.id === 'Ìba', `Search 'iba se' expected 'Ìba', got '${resIbaSe[0]?.entity?.id}'`);

// 7. Vector 6: Headless DOM Relatives Resolver Check (Zero Variants Leak in Cell 6)
const sampleTargets = ['CORPUS_OGUN_COSMIC_001', 'Ìyámi', 'Ọ̀ṣọ́ọ̀sì', 'Àìṣòótọ́', 'Àṣẹ-Ọ̀rọ̀', 'Òrìṣà'];
for (const tid of sampleTargets) {
  const target = corpus.find(x => x.id === tid);
  if (target) {
    const resolved = resolveKnowledgeGraphRelatives(target, corpus, 6);
    const svs = new Set((target.sub_variants || []).map(s => typeof s === 'string' ? s : s.title));
    const leaked = resolved.filter(r => svs.has(r.title) || svs.has(r.id));
    check(leaked.length === 0, `Resolver leaked sub-variants into relatives for ${tid}: ${leaked.map(l => l.title).join(', ')}`);
  }
}

// 8. Vector 7: Symmetrical Mirror of details.related_entities & Absence of cultural_relatives
for (const tid of sampleTargets) {
  const target = corpus.find(x => x.id === tid);
  if (target && target.details) {
    check(JSON.stringify(target.related_entities) === JSON.stringify(target.details.related_entities), `Details related_entities not mirrored for ${tid}`);
    check(!('cultural_relatives' in target) && !('cultural_relatives' in target.details), `cultural_relatives not pruned for ${tid}`);
  }
}

// 9. Unicode NFC Composition
for (const e of corpus) {
  check(e.title === e.title.normalize('NFC'), `Title for ${e.id} is not NFC composed`);
}

if (errors.length > 0) {
  console.error(`FAILED with ${errors.length} error(s):`);
  for (const err of errors) console.error(`  - ${err}`);
  process.exit(1);
} else {
  console.log("All Node.js Headless DOM & Retrieval assertions PASSED (0 errors).");
}
"""

def main():
    print("🔬 Executing Headless Client-Side DOM Parity & Integrity Benchmark (Batch 03 Post-Sync)...")

    # Step 1: Cryptographic Dual-Corpora Checksum Lock
    api_sha = hashlib.sha256(API_CORPUS_PATH.read_bytes()).hexdigest()
    web_sha = hashlib.sha256(WEB_CORPUS_PATH.read_bytes()).hexdigest()
    assert api_sha == web_sha, f"Checksum drift: API ({api_sha}) != WEB ({web_sha})"
    assert api_sha == EXPECTED_SHA, f"SHA mismatch: expected {EXPECTED_SHA}, got {api_sha}"
    print(f"✅ Cryptographic Dual-Corpora Lock: {api_sha} (0-bit drift across {EXPECTED_COUNT} entities)")

    # Step 2: Headless Node.js DOM Parity Execution
    proc = subprocess.run(["node", "--input-type=module", "-e", NODE_SCRIPT, str(ROOT)], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"❌ Node harness failed:\n{proc.stderr}\n{proc.stdout}")
        sys.exit(1)
    print(proc.stdout.strip())
    print("👑 CERTIFIED: Batch 03 Pantheon Expansion, Orthography, Akígun, Sync & DOM Parity Verified!")

if __name__ == "__main__":
    main()
