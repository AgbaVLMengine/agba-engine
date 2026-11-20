#!/usr/bin/env python3
"""
Universal Batch Sanitation Runner (Drawer B Execution).
Zero-data-in-code: Operates purely on declarative JSON mutations & invariants.
Replicable across all 17 categories under Gate 2 (<100 LOC).
"""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAYLOAD_PATH = ROOT / "scripts/data/batches/category01_sanitation_payloads.json"
API_PATH = ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = ROOT / "web/src/data/yoruba_master_corpus.json"

def verify_invariants(by_id, invariants):
    """Dynamically validates data integrity locks declared in JSON."""
    for inv in invariants:
        eid = inv["entity_id"]
        field_path = inv["field"].split(".")
        op = inv["operator"]
        expected = inv["expected"]

        val = by_id.get(eid)
        for part in field_path:
            val = val[int(part)] if part.isdigit() else (val.get(part) if isinstance(val, dict) else None)

        if op == "equals":
            assert val == expected, f"Invariant failed on {eid}: {val} != {expected}"
        elif op == "not_contains":
            assert expected not in (val or []), f"Invariant failed: {expected} found in {eid}"

def apply_sanitation(corpus, payload):
    retire_set = set(payload.get("retire_ids", []))
    corpus = [e for e in corpus if e.get("id") not in retire_set]
    by_id = {e.get("id"): e for e in corpus}
    
    # 1. Apply Entity Updates (titles, aliases, clean sub_variants, related_entities)
    for eid, updates in payload.get("entity_updates", {}).items():
        ent = by_id.get(eid)
        if not ent:
            raise KeyError(f"Target entity {eid} missing from corpus!")
        for k, v in updates.items():
            ent[k] = v

    # 2. Apply Facet Updates (deep descriptions, >600c etymology, triads, citations)
    for pid, facets in payload.get("facet_updates", {}).items():
        parent = by_id.get(pid)
        if not parent:
            raise KeyError(f"Facet parent {pid} missing from corpus!")
        parent_facets = parent.setdefault("sub_variant_facets", {})
        for fname, fdata in facets.items():
            parent_facets[fname] = fdata

    # 3. Dynamic Invariant Verification (Zero hardcoded names in code!)
    verify_invariants(by_id, payload.get("expected_invariants", []))
    return corpus

def main():
    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    api_corpus = json.loads(API_PATH.read_text(encoding="utf-8"))
    web_corpus = json.loads(WEB_PATH.read_text(encoding="utf-8"))

    new_api = apply_sanitation(api_corpus, payload)
    new_web = apply_sanitation(web_corpus, payload)

    API_PATH.write_text(json.dumps(new_api, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    WEB_PATH.write_text(json.dumps(new_web, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    api_sha = hashlib.sha256(API_PATH.read_bytes()).hexdigest()
    web_sha = hashlib.sha256(WEB_PATH.read_bytes()).hexdigest()

    if api_sha != web_sha:
        raise ValueError(f"❌ Checksum drift detected: {api_sha} != {web_sha}")

    print(f"✅ Canonical entity count: {len(new_api)} (Web: {len(new_web)})")
    print(f"🔒 Dual-corpora SHA-256 bit-for-bit lockstep parity confirmed (0 bits drift):")
    print(f"   {api_sha}")

if __name__ == "__main__":
    main()
