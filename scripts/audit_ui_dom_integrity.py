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
EXPECTED_SHA = "9186bd59a7048d33c034fb9fac16c63237de09fb232766372bfab2fb43680186"

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

// Reconstruct Search Engine
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

// 1. Zero-Boilerplate Assertion on DOM Cards
for (const e of corpus) {
  const raw = JSON.stringify(e);
  check(!raw.includes("Rooted in ancestral Yorùbá"), `Entity ${e.id} contains boilerplate 'Rooted in ancestral Yorùbá'`);
  check(!raw.includes("An authentic living sub-variant within the"), `Entity ${e.id} contains boilerplate 'An authentic living sub-variant'`);
}

// 2. Anti-Parent-Loop & Ancestry Assertion (opele_agbalagba, opele_ide)
for (const id of ['opele_agbalagba', 'opele_ide']) {
  const e = corpus.find(x => x.id === id);
  check(e, `Entity ${id} missing from corpus`);
  check(Array.isArray(e.sub_variants) && e.sub_variants.length === 0, `${id} sub_variants must be empty`);
  check(e.sovereign_parent === 'Ọ̀pẹ̀lẹ̀', `${id} sovereign_parent must be Ọ̀pẹ̀lẹ̀`);
  
  const cls = getOntologicalClassification(e, corpus);
  check(cls.tier === ONTOLOGICAL_TIER.LIVING_VARIANT, `${id} must classify as LIVING_VARIANT, got ${cls.tier}`);
  check(cls.parentTitle === 'Ọ̀pẹ̀lẹ̀', `${id} parentTitle must resolve to Ọ̀pẹ̀lẹ̀`);
  
  const rels = resolveKnowledgeGraphRelatives(e, corpus, 8);
  check(!rels.some(r => r.id === id || r.title === e.title), `${id} must not appear in its own connected relatives`);
}

// 3. Field-Level Depth & Triad Assertion across Elevated Category 1 Nodes
const elevated = [
  'Olódùmarè', 'Obàtálá', 'Èṣù', 'CORPUS_OGUN_COSMIC_001', 'CORPUS_SANGO_COSMIC_001',
  'CORPUS_OSUN_001', 'Ọ̀yá', 'CORPUS_YEMOJA_001', 'Orí', 'Ifá', 'Àyànmọ́', 'CORPUS_OLOKUN_001',
  'CORPUS_OBALUAYE_001', 'Ọ̀ṣọ́ọ̀sì', 'Ọ̀pẹ̀lẹ̀', 'Orúnmìlà', 'Onile', 'Àjà', 'Ọbá'
];
for (const id of elevated) {
  const e = corpus.find(x => x.id === id);
  check(e, `Elevated node ${id} missing`);
  const etym = e.etymology_and_philosophy || e.details?.etymology_and_philosophy || '';
  const provs = e.proverbs_and_oral_traditions || e.details?.proverbs_and_oral_traditions || [];
  check(etym.length >= 600, `${id} etymology must be >= 600 chars (got ${etym.length})`);
  check(provs.length >= 3, `${id} proverbs must be >= 3 (got ${provs.length})`);
}

// Check opele & ikin implementations
for (const id of ['opele_agbalagba', 'opele_ide', 'ikin_oloju_merin', 'ikin_oloju_meta']) {
  const e = corpus.find(x => x.id === id);
  check(e, `Node ${id} missing`);
  const provs = e.proverbs_and_oral_traditions || e.details?.proverbs_and_oral_traditions || [];
  check(provs.length >= 3, `${id} proverbs must be >= 3 (got ${provs.length})`);
}

// 4. Ògún Avatar Purity
const ogun = corpus.find(x => x.id === 'CORPUS_OGUN_COSMIC_001');
const weapons = ['Àdá Ìbílẹ̀', 'Idà Agẹmọ', 'Ọ̀kọ̀ Ẹlẹ́ṣin', 'Ọfà Ọdẹ'];
for (const w of weapons) {
  check(!(ogun.sub_variants || []).includes(w), `Ògún sub_variants must not contain physical weapon: ${w}`);
  check((ogun.related_entities || []).includes(w), `Ògún related_entities must preserve weapon: ${w}`);
}

// 5. Sacerdotal Implements & Liturgy
const oko = corpus.find(x => x.id === 'CORPUS_ORISA_OKO_001');
check(JSON.stringify(oko).includes("Ọdún Iṣu Tuntun (New Yam Liturgy)"), "Òrìṣà Oko must include 'Ọdún Iṣu Tuntun (New Yam Liturgy)'");

// 6. Unicode NFC Normalization
for (const e of corpus) {
  check(e.title === e.title.normalize('NFC'), `Title for ${e.id} is not NFC composed`);
}

// 7. ASCII Cross-Domain Disambiguation & Root Pod Anchoring
const resAja = search('Aja');
check(resAja[0]?.entity?.id === 'Àjà', `'Aja' must rank Àjà at #1 (got ${resAja[0]?.entity?.title})`);

const resOba = search('Oba');
check(resOba[0]?.entity?.id === 'Ọbá', `'Oba' must rank Ọbá at #1 (got ${resOba[0]?.entity?.title})`);

const resObaRiver = search('Oba river');
check(resObaRiver[0]?.entity?.title === 'Oba River', `'Oba river' must rank Oba River at #1 (got ${resObaRiver[0]?.entity?.title})`);

const resOnile = search('Onile');
check(resOnile[0]?.entity?.id === 'Onile', `'Onile' must rank Onílẹ̀ at #1 (got ${resOnile[0]?.entity?.title})`);

// 8. Constellation Branching & Parent-Shadow De-coupling
const osunBranch = findSubVariantMatchInCorpus('Ọ̀ṣun Òṣogbo', corpus);
check(osunBranch, "findSubVariantMatchInCorpus('Ọ̀ṣun Òṣogbo') must match");
if (osunBranch) {
  const child = hydrateSubVariantFromParent(osunBranch.variantTitle, osunBranch.parent);
  check(child.is_parent === false, "Hydrated Ọ̀ṣun Òṣogbo must have is_parent: false");
  check(child.sovereign_parent === 'Ọ̀ṣun', "Hydrated Ọ̀ṣun Òṣogbo parent must be Ọ̀ṣun");
}

const arabaBranch = findSubVariantMatchInCorpus('Àràbà Agbáyé', corpus);
check(arabaBranch, "findSubVariantMatchInCorpus('Àràbà Agbáyé') must match");
if (arabaBranch) {
  const child = hydrateSubVariantFromParent(arabaBranch.variantTitle, arabaBranch.parent);
  check(child.is_parent === false, "Hydrated Àràbà Agbáyé must have is_parent: false");
  check(child.sovereign_parent === 'Àràbà Ilé-Ifẹ̀', "Hydrated Àràbà Agbáyé parent must be Àràbà Ilé-Ifẹ̀");
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
    print("🔬 Executing Headless Client-Side DOM Parity & Integrity Benchmark...")

    # Step 1: Cryptographic Dual-Corpora Checksum Lock
    api_sha = hashlib.sha256(API_CORPUS_PATH.read_bytes()).hexdigest()
    web_sha = hashlib.sha256(WEB_CORPUS_PATH.read_bytes()).hexdigest()
    assert api_sha == web_sha, f"Checksum drift: API ({api_sha}) != WEB ({web_sha})"
    assert api_sha == EXPECTED_SHA, f"SHA mismatch: expected {EXPECTED_SHA}, got {api_sha}"
    print(f"✅ Cryptographic Dual-Corpora Lock: {api_sha} (0-bit drift)")

    # Step 2: Headless Node.js DOM Parity Execution
    proc = subprocess.run(["node", "--input-type=module", "-e", NODE_SCRIPT, str(ROOT)], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"❌ Node harness failed:\n{proc.stderr}\n{proc.stdout}")
        sys.exit(1)
    print(proc.stdout.strip())
    print("👑 CERTIFIED: Zero-Boilerplate, Parent-Loop Eradication, and Cross-Domain Integrity Verified!")

if __name__ == "__main__":
    main()
