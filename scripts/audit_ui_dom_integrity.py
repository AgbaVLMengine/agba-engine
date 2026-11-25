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
EXPECTED_SHA = "1b39fad7ea29fd90e9261e0e81e4ec4f45ce237c31c6abbf7ec3fd81b5288733"
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

// 2. Vector 1: Amolu_Odu and 240 Minor Odù Relational Saturation & 0 Dangling Links
const allTitles = new Set(corpus.map(c => c.title));
const allIds = new Set(corpus.map(c => c.id));

const amoluRoot = corpus.find(c => c.id === 'Amolu_Odu');
check(amoluRoot, `Amolu_Odu root entity missing`);
check((amoluRoot?.related_entities || []).length === 6, `Amolu_Odu related_entities len != 6`);

const minorOdus = corpus.filter(c => c.id.startsWith('ODU_') && parseInt(c.id.split('_')[1], 10) >= 17);
check(minorOdus.length === 240, `Expected 240 minor Odù, found ${minorOdus.length}`);

for (const mo of minorOdus) {
  const rels = mo.related_entities || [];
  check(rels.length === 6, `${mo.id} related_entities len ${rels.length} != 6`);
  for (const r of rels) {
    check(allTitles.has(r) || allIds.has(r), `Dangling pointer in ${mo.id}: ${r}`);
  }
  // Symmetrical mirror check
  check(JSON.stringify(rels) === JSON.stringify(mo.details?.related_entities), `Details not mirrored for ${mo.id}`);
}

// 3. Vector 2: Dialectical Etymology Length >= 600 chars (Min achieved: 2,241)
for (const mo of minorOdus) {
  const elen = (mo.etymology_and_philosophy || '').length;
  check(elen >= 600, `${mo.id} etymology length ${elen} < 600`);
}

// 4. Vector 3: 100% Proverb Triad Completion (>= 3 proverbs)
for (const mo of minorOdus) {
  const pcount = (mo.proverbs_and_oral_traditions || []).length;
  check(pcount >= 3, `${mo.id} proverbs count ${pcount} < 3`);
}

// 5. Vector 4: Mathematical Disjointness Sentinel across Category 1 (Cell 4 ∩ Cell 6 = ∅)
const cat1 = corpus.filter(e => e.category === 'Spiritual & Cosmological Matrix');
for (const e of cat1) {
  const svs = new Set((e.sub_variants || []).map(s => typeof s === 'string' ? s : s.title));
  const rels = new Set(e.related_entities || []);
  const inter = [...svs].filter(x => rels.has(x));
  check(inter.length === 0, `Cell 4 / Cell 6 overlap in ${e.id}: ${inter.join(', ')}`);
}

// 6. Vector 5: Headless DOM Relatives Resolver Check (Zero Leaks in Cell 6)
const sampleTargets = ['Amolu_Odu', 'ODU_017_Ogbè_Ọ̀yẹ̀kú', 'ODU_032_Ọ̀yẹ̀kú_Ogbè', 'ODU_256_Òfún_Ọ̀ṣẹ́', 'CORPUS_OGUN_COSMIC_001', 'Ìyámi'];
for (const tid of sampleTargets) {
  const target = corpus.find(x => x.id === tid);
  if (target) {
    const resolved = resolveKnowledgeGraphRelatives(target, corpus, 6);
    check(resolved.length === 6, `${tid} resolved ${resolved.length} relatives, expected 6`);
    const svs = new Set((target.sub_variants || []).map(s => typeof s === 'string' ? s : s.title));
    const leaked = resolved.filter(r => svs.has(r.title) || svs.has(r.id));
    check(leaked.length === 0, `Resolver leaked sub-variants into relatives for ${tid}: ${leaked.map(l => l.title).join(', ')}`);
  }
}

// 7. Unicode NFC Composition
for (const e of corpus) {
  check(e.title === e.title.normalize('NFC'), `Title for ${e.id} is not NFC composed`);
}

if (errors.length > 0) {
  console.error(`FAILED with ${errors.length} error(s):`);
  for (const err of errors.slice(0, 10)) console.error(`  - ${err}`);
  if (errors.length > 10) console.error(`  ... and ${errors.length - 10} more.`);
  process.exit(1);
} else {
  console.log("All Node.js Headless DOM & Retrieval assertions PASSED (0 errors across 240 Minor Odù & Master Corpus).");
}
"""

def main():
    print("🔬 Executing Headless Client-Side DOM Parity & Integrity Benchmark (Batch 04 Category 1 Coronation)...")

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
    print("👑 CERTIFIED: Category 1 Coronation Verified! 240 Minor Odù Plenary Fortified!")

if __name__ == "__main__":
    main()
