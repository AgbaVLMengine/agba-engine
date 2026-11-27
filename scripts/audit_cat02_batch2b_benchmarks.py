#!/usr/bin/env python3
"""
scripts/audit_cat02_batch2b_benchmarks.py
100% Data-Blind Dynamic QA & Headless DOM Benchmark Engine for Batch 2B.
Complies with Gate 2 (< 250 LOC), Gate 8, and Sùúrù's 7 Vectors.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_PATH = ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = ROOT / "web/src/data/yoruba_master_corpus.json"
PAYLOAD_PATH = ROOT / "scripts/data/batches/cat2_batch2b_maritime_expansion.json"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    print("=" * 70)
    print("🧪 ỌLỌ́YÈ SÙÚRÙ — DATA-BLIND BATCH 2B BENCHMARK ENGINE")
    print("=" * 70)

    # 1. Cryptographic Parity
    api_sha = sha256_file(API_PATH)
    web_sha = sha256_file(WEB_PATH)
    assert api_sha == web_sha, f"Checksum drift: API ({api_sha}) != WEB ({web_sha})"
    print(f"✅ Vector 1 (Dual-Corpora Checksum): Locked at {api_sha} (0-bit drift)")

    # 2. Dynamic Batch Evaluation
    with open(PAYLOAD_PATH, "r", encoding="utf-8") as pf:
        batch = json.load(pf)
    with open(WEB_PATH, "r", encoding="utf-8") as wf:
        corpus = json.load(wf)

    invariants = batch.get("expected_invariants", {})
    delta = invariants.get("expected_corpus_delta", 11)
    new_ents = batch.get("new_entities", [])
    mutations = batch.get("entity_mutations", [])

    # Vector 2: Entity Count
    expected_total = 1398 + delta
    assert len(corpus) == expected_total, f"Corpus length {len(corpus)} != {expected_total}"
    print(f"✅ Vector 2 (Corpus Count): Strictly {len(corpus)} canonical nodes (1,398 + {delta})")

    by_id = {c["id"]: c for c in corpus}
    by_title = {c.get("title"): c for c in corpus}
    all_identifiers = set(by_id.keys()) | set(by_title.keys())

    # Vector 3: Depth & Proverb Triads across New Entities
    min_rels = invariants.get("min_related_entities", 6)
    min_provs = invariants.get("min_proverbs", 3)
    for ne in new_ents:
        eid = ne["id"]
        ent = by_id.get(eid)
        assert ent, f"Missing node: {eid}"

        # Depth
        etym_len = len(ent.get("etymology_and_philosophy", "") or "")
        min_etym = invariants.get("min_etymology_chars_chieftaincy", 600)
        if "chiefs" not in eid and "conclave" not in eid and "akinsiku" not in eid:
            min_etym = invariants.get("min_etymology_chars_monarch", 1000)
        assert etym_len >= min_etym, f"{eid} etymology len {etym_len} < {min_etym}"

        # Proverbs
        provs = ent.get("proverbs_and_oral_traditions", [])
        assert len(provs) >= min_provs, f"{eid} provs len {len(provs)} < {min_provs}"

        # Relatives count
        rels = ent.get("related_entities", [])
        assert len(rels) >= min_rels, f"{eid} rels len {len(rels)} < {min_rels}"

        # Graph Closure
        for r in rels:
            assert r in all_identifiers, f"{eid} dangling relative: {r}"

        # Symmetrical Details
        if invariants.get("require_symmetrical_details"):
            assert ent.get("details", {}).get("related_entities") == rels, f"{eid} details rels mismatch"

        # Disjointness
        if invariants.get("enforce_disjointness_cell4_cell6"):
            svs = set(s if isinstance(s, str) else s.get("title") for s in (ent.get("sub_variants") or []))
            inter = svs.intersection(set(rels))
            assert len(inter) == 0, f"{eid} Cell 4/Cell 6 overlap: {inter}"

    print(f"✅ Vector 3 (Dynamic Depth, Proverb Triads & Schema Mirroring): All {len(new_ents)} nodes verified!")

    # Vector 4: 6-Slot Saturation & Disjointness on Mutated Parents
    for mut in mutations:
        eid = mut["id"]
        ent = by_id.get(eid)
        assert ent, f"Missing mutated entity: {eid}"
        rels = ent.get("related_entities", [])
        assert len(rels) >= min_rels, f"Mutated {eid} has {len(rels)} < {min_rels} relatives"
        for r in rels:
            assert r in all_identifiers, f"Mutated {eid} dangling relative: {r}"
        if invariants.get("enforce_disjointness_cell4_cell6"):
            svs = set(s if isinstance(s, str) else s.get("title") for s in (ent.get("sub_variants") or []))
            inter = svs.intersection(set(rels))
            assert len(inter) == 0, f"Mutated {eid} Cell 4/Cell 6 overlap: {inter}"

    print(f"✅ Vector 4 (6-Slot Saturation & Parent Disjointness): All {len(mutations)} mutated parents verified!")

    # Vector 5: Headless Node.js DOM Resolution
    node_cmd = """
import fs from 'fs';
const corpus = JSON.parse(fs.readFileSync('web/src/data/yoruba_master_corpus.json', 'utf8'));
const batch = JSON.parse(fs.readFileSync('scripts/data/batches/cat2_batch2b_maritime_expansion.json', 'utf8'));
const { resolveKnowledgeGraphRelatives } = await import('./web/src/utils/relativesResolver.js');
const targets = batch.new_entities.concat(batch.entity_mutations);
for (const t of targets) {
  const entity = corpus.find(e => e.id === t.id);
  const resolved = resolveKnowledgeGraphRelatives(entity, corpus, 6);
  if (resolved.length < 6) throw new Error(`${t.id} resolved only ${resolved.length} items`);
  const svs = new Set((entity.sub_variants || []).map(s => typeof s === 'string' ? s : s.title));
  const leaked = resolved.filter(r => svs.has(r.title) || svs.has(r.id));
  if (leaked.length > 0) throw new Error(`${t.id} leaked sub-variants into Cell 6`);
}
console.log('✅ Node DOM Resolver: 0 sub-variant leaks across all 16 target entities.');
"""
    proc = subprocess.run(["node", "--input-type=module", "-e", node_cmd], capture_output=True, text=True, cwd=str(ROOT))
    assert proc.returncode == 0, f"Node DOM Resolver failed: {proc.stderr}"
    print(f"✅ Vector 5 (Headless DOM Relative Resolver): {proc.stdout.strip()}")

    # Vector 6: NFC Unicode Normalization
    for ne in new_ents:
        ent = by_id[ne["id"]]
        t = ent.get("title", "")
        import unicodedata
        assert t == unicodedata.normalize("NFC", t), f"Title for {ne['id']} not in NFC form"
    print("✅ Vector 6 (Unicode NFC Composition): 100% Normalized across all new titles.")

    # Vector 7: Production Build
    print("🚀 Vector 7: Production Vite Client Build Check...")
    b_proc = subprocess.run(["npm", "run", "build"], cwd=str(ROOT / "web"), capture_output=True, text=True)
    assert b_proc.returncode == 0, f"Client build failed: {b_proc.stderr}"
    print("✅ Vector 7 (Client Production Build): Clean Vite compilation successful!")

    print("=" * 70)
    print("👑 CERTIFIED: BATCH 2B 7-VECTOR QA & BENCHMARK SUITE 100% GREEN!")
    print("=" * 70)

if __name__ == "__main__":
    main()
