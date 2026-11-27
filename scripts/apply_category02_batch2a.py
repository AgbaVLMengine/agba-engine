#!/usr/bin/env python3
"""
Category 2 Batch 2A Lean Runner: Orthographic Elevation, Deduplication & Audio Binding.
Complies with Gate 2 (< 120 LOC), Ẹ̀ṣọ́'s Invariant Assertions, Sùúrù's 7 Vectors,
and guarantees 100% Dual-Corpora SHA-256 Bit-for-Bit Lockstep (0-bit drift).
"""
import hashlib
import json
import sys

CORPUS_PATHS = [
    "/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json",
    "/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json"
]
PAYLOAD_PATH = "/home/aruna_olanrewaju/agba-engine/scripts/data/batches/cat2_batch2a_foundation_payload.json"

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    dry_run = "--dry-run" in sys.argv
    print(f"Executing Batch 2A Runner. Dry-run: {dry_run}")
    print(f"Payload SHA-256: {sha256_file(PAYLOAD_PATH)}")

    with open(PAYLOAD_PATH, "r", encoding="utf-8") as pf:
        payload = json.load(pf)

    with open(CORPUS_PATHS[0], "r", encoding="utf-8") as cf:
        corpus = json.load(cf)

    # 1. Pre-flight assertions
    assert len(corpus) == 1398, f"Pre-flight assertion failed: Expected 1398 entities, got {len(corpus)}"
    by_id = {e.get("id"): e for e in corpus}
    assert "Ìrùke" in by_id, "Expected 'Ìrùke' stub to be present for retirement"
    assert "Ìrukẹ̀rẹ̀" in by_id, "Expected canonical 'Ìrukẹ̀rẹ̀' to be present"

    # 2. Retire redundant stub 'Ìrùke' and enshrine 'oba_onitire_of_itire' in its exact slot
    rep_info = payload["retire_and_replace"]
    retire_id = rep_info["retire_id"]
    replacement = rep_info["replacement_entity"]

    # Ensure symmetrical details on replacement entity
    rep_details = dict(replacement)
    replacement["details"] = rep_details

    # Merge aliases into target entity ('Ìrukẹ̀rẹ̀')
    merge_target = by_id[rep_info["merge_into_id"]]
    existing_aliases = set(merge_target.get("aliases", []))
    for alias in rep_info.get("merge_aliases", []):
        existing_aliases.add(alias)
    merge_target["aliases"] = sorted(list(existing_aliases))
    if isinstance(merge_target.get("details"), dict):
        merge_target["details"]["aliases"] = list(merge_target["aliases"])

    # In-place slot replacement (preserves order and strictly preserves total count)
    for idx, e in enumerate(corpus):
        if e.get("id") == retire_id:
            corpus[idx] = replacement
            break

    # Rebuild dictionary lookup
    by_id = {e.get("id"): e for e in corpus}
    assert "oba_onitire_of_itire" in by_id, "oba_onitire_of_itire enshrinement failed!"
    assert "Ìrùke" not in by_id, "Retirement of 'Ìrùke' failed!"

    # 3. Apply mutations to entities_to_update
    updates = payload.get("entities_to_update", {})
    for eid, mut in updates.items():
        target = by_id.get(eid)
        assert target, f"Target entity {eid} not found in corpus!"
        for k, v in mut.items():
            target[k] = v

        # Symmetrical Mirror Law to nested details
        if "details" not in target or not isinstance(target["details"], dict):
            target["details"] = {}
        for k, v in mut.items():
            target["details"][k] = list(v) if isinstance(v, list) else v

        # Disjointness Sentinel Assertion (Cell 4 cap Cell 6 = empty)
        svs = set(s if isinstance(s, str) else s.get("title") for s in target.get("sub_variants", []))
        rels = set(target.get("related_entities", []))
        leak = svs.intersection(rels)
        assert len(leak) == 0, f"Disjointness breach on {eid}: leak {leak}"

    # 4. Post-flight invariants
    assert len(corpus) == 1398, f"Post-flight count drift! Expected 1398, got {len(corpus)}"
    corpus_ids = set(by_id.keys())
    for eid, mut in updates.items():
        for rel in mut.get("related_entities", []):
            assert rel in corpus_ids, f"Dangling pointer: {eid} -> {rel}"

    if dry_run:
        print(f"DRY RUN PASSED: 1398 entities certified. oba_onitire_of_itire enshrined. Zero disk writes.")
        return

    # 5. Dual-Corpora Write & SHA-256 Lockstep
    for path in CORPUS_PATHS:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, indent=2, ensure_ascii=False)

    hashes = [sha256_file(p) for p in CORPUS_PATHS]
    assert hashes[0] == hashes[1], f"Checksum mismatch! {hashes[0]} != {hashes[1]}"
    print(f"SUCCESS: Dual corpora locked at SHA-256 {hashes[0]}")
    print(f"Batch 2A complete: exactly {len(corpus)} entities in master corpus (0-bit drift).")

if __name__ == "__main__":
    main()
