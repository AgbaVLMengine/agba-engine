#!/usr/bin/env python3
"""
Category 2 Batch 2C Lean Runner: The Dynastic Succession of Lagos & Patriarch Ọlọ́fin.
Complies with Gate 2 (< 120 LOC), Ẹ̀ṣọ́'s Invariants, Sùúrù's 7 Vectors,
and guarantees 100% Dual-Corpora SHA-256 Bit-for-Bit Lockstep (0-bit drift).
"""
import hashlib
import json
import sys

CORPUS_PATHS = [
    "/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json",
    "/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json"
]
PAYLOAD_PATH = "/home/aruna_olanrewaju/agba-engine/scripts/data/batches/cat2_batch2c_dynastic_succession.json"

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    dry_run = "--dry-run" in sys.argv
    print(f"Executing Batch 2C Runner. Dry-run: {dry_run}")
    print(f"Payload SHA-256: {sha256_file(PAYLOAD_PATH)}")

    with open(PAYLOAD_PATH, "r", encoding="utf-8") as pf:
        payload = json.load(pf)

    with open(CORPUS_PATHS[0], "r", encoding="utf-8") as cf:
        corpus = json.load(cf)

    invariants = payload.get("expected_invariants", {})
    delta = invariants.get("expected_corpus_delta", 13)

    # 1. Pre-flight assertions
    initial_count = len(corpus)
    assert initial_count == 1409, f"Pre-flight failed: Expected 1409, got {initial_count}"
    by_id = {e.get("id"): e for e in corpus}

    new_entities = payload.get("new_entities", [])
    assert len(new_entities) == delta, f"Expected {delta} new entities, got {len(new_entities)}"

    # 2. Ingest new entities with symmetrical details mirroring
    for ne in new_entities:
        eid = ne.get("id")
        assert eid not in by_id, f"Collision detected! Entity {eid} already exists"
        ne_copy = dict(ne)
        if "details" not in ne_copy or not isinstance(ne_copy["details"], dict):
            ne_copy["details"] = dict(ne)
        corpus.append(ne_copy)
        by_id[eid] = ne_copy

    # 3. Apply mutations (reciprocal Golden Cord links)
    mutations = payload.get("entity_mutations", [])
    for mut in mutations:
        eid = mut.get("id")
        target = by_id.get(eid)
        assert target, f"Target mutation {eid} not found in corpus!"
        for k, v in mut.items():
            if k == "id":
                continue
            target[k] = list(v) if isinstance(v, list) else v
            if "details" in target and isinstance(target["details"], dict):
                target["details"][k] = list(v) if isinstance(v, list) else v

        # Disjointness Sentinel Assertion (Cell 4 cap Cell 6 = empty)
        svs = set(s if isinstance(s, str) else s.get("title") for s in target.get("sub_variants", []))
        rels = set(target.get("related_entities", []))
        leak = svs.intersection(rels)
        assert len(leak) == 0, f"Disjointness breach on {eid}: leak {leak}"

    # 4. Post-flight Invariant Verification
    post_count = len(corpus)
    expected_count = initial_count + delta
    assert post_count == expected_count, f"Corpus delta mismatch! {post_count} != {expected_count}"
    assert post_count == 1422, f"Expected strictly 1422 entities, got {post_count}"

    corpus_ids = set(by_id.keys())
    batch_scope = new_entities + mutations
    for item in batch_scope:
        eid = item.get("id")
        target = by_id.get(eid)
        for rel in target.get("related_entities") or []:
            assert rel in corpus_ids, f"Dangling pointer in batch scope: {eid} -> {rel}"

    if dry_run:
        print(f"DRY RUN PASSED: {len(new_entities)} new entities validated. ΔN = +{delta}. Zero disk writes.")
        return

    # 5. Dual-Corpora Write & SHA-256 Lockstep
    for path in CORPUS_PATHS:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, indent=2, ensure_ascii=False)

    hashes = [sha256_file(p) for p in CORPUS_PATHS]
    assert hashes[0] == hashes[1], f"Checksum mismatch! {hashes[0]} != {hashes[1]}"
    print(f"SUCCESS: Dual corpora locked at SHA-256 {hashes[0]}")
    print(f"Batch 2C complete: strictly {len(corpus)} canonical entities in master corpus (0-bit drift).")

if __name__ == "__main__":
    main()
