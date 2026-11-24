#!/usr/bin/env python3
"""
Generic, Data-Blind Batch 03 Sanitation Runner for Agba Engine.
Enforces Single-Drawer Discipline, Gate 2 compliance (< 120 LOC),
Dual-Corpora Checksum Lock (0-bit drift), and Declarative Invariants.
"""
import hashlib
import json
import sys

CORPUS_PATHS = [
    "/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json",
    "/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json"
]
PAYLOAD_PATH = "/home/aruna_olanrewaju/agba-engine/scripts/data/batches/category01_sanitation_batch03.json"

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def evaluate_invariants(by_id, initial_count, final_count, invariants):
    for inv in invariants:
        itype = inv.get("type")
        if itype == "entity_count_delta":
            assert final_count - initial_count == inv["delta"], f"Count delta mismatch: {final_count - initial_count} != {inv['delta']}"
        elif itype == "in_sub_variants":
            parent_svs = by_id[inv["parent_id"]].get("sub_variants", [])
            for c in inv["child_titles"]:
                assert c in parent_svs, f"Child {c} missing from {inv['parent_id']} sub_variants"
        elif itype == "in_related_entities":
            rels = by_id[inv["entity_id"]].get("related_entities", [])
            for t in inv["targets"]:
                assert t in rels, f"Target {t} missing from {inv['entity_id']} related_entities"
        elif itype == "field_equals":
            actual = by_id[inv["entity_id"]].get(inv["field"])
            assert actual == inv["expected"], f"{inv['entity_id']}.{inv['field']} = {actual} != {inv['expected']}"
        elif itype == "disjoint_variants_relatives":
            for tid in inv["target_ids"]:
                e = by_id.get(tid, {})
                svs = set(s if isinstance(s, str) else s.get("title") for s in e.get("sub_variants", []))
                rels = set(e.get("related_entities", []))
                leak = svs.intersection(rels)
                assert len(leak) == 0, f"Disjointness breach on {tid}: leak {leak}"

def main():
    dry_run = "--dry-run" in sys.argv
    payload_hash = sha256_file(PAYLOAD_PATH)
    print(f"Payload SHA-256: {payload_hash}")

    with open(PAYLOAD_PATH, "r", encoding="utf-8") as pf:
        payload = json.load(pf)

    with open(CORPUS_PATHS[0], "r", encoding="utf-8") as cf:
        corpus = json.load(cf)

    initial_count = len(corpus)
    by_id = {e.get("id"): e for e in corpus}

    # 1. Add new entities
    for ne in payload.get("new_entities", []):
        assert ne["id"] not in by_id, f"Duplicate entity id: {ne['id']}"
        corpus.append(ne)
        by_id[ne["id"]] = ne

    # 2. Apply mutations
    for mut in payload.get("entity_mutations", []):
        target = by_id.get(mut["id"])
        assert target, f"Mutation target {mut['id']} not found"
        for k, v in mut.items():
            if k == "id":
                continue
            elif k == "aliases_append":
                for a in v:
                    if a not in target.setdefault("aliases", []):
                        target["aliases"].append(a)
            else:
                target[k] = v

    # 3. Dynamic invariant assertions
    evaluate_invariants(by_id, initial_count, len(corpus), payload.get("expected_invariants", []))

    if dry_run:
        print(f"DRY RUN PASSED: {len(payload.get('new_entities', []))} added, {len(payload.get('entity_mutations', []))} mutated.")
        print(f"Final Count would be {len(corpus)} entities.")
        return

    # 4. Dual-Corpora Write & Checksum Parity Lock
    for path in CORPUS_PATHS:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, indent=2, ensure_ascii=False)

    hashes = [sha256_file(p) for p in CORPUS_PATHS]
    assert hashes[0] == hashes[1], f"Checksum drift detected! {hashes[0]} != {hashes[1]}"
    print(f"SUCCESS: Dual-Corpora locked at SHA-256 {hashes[0]}")
    print(f"Total Canonical Corpus Count: {len(corpus)} entities (0-bit drift).")

if __name__ == "__main__":
    main()
