#!/usr/bin/env python3
"""
Category 1 Declarative Catharsis & Taxonomic Consolidation Runner.
Executes synchronous dual-corpora consolidation under Gate 2 (<100 LOC).
"""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAYLOAD_PATH = ROOT / "scripts/data/batches/category01_catharsis_payloads.json"
API_CORPUS_PATH = ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = ROOT / "web/src/data/yoruba_master_corpus.json"

def clean_proverbs(proverbs, scrubbing_rules):
    cleaned = []
    for p in proverbs:
        p_clean = p
        for rule in scrubbing_rules:
            p_clean = p_clean.replace(rule["pattern"], rule["replacement"])
        cleaned.append(p_clean)
    return cleaned

def apply_catharsis(corpus, payload):
    by_id = {e.get("id"): e for e in corpus}
    retire_set = set(payload.get("retire_ids", []))
    scrubbing_rules = payload.get("prompt_scrubbing", [])

    for merge in payload.get("duplicate_merges", []):
        tgt = by_id.get(merge["target_id"])
        if not tgt:
            continue
        aliases = tgt.get("aliases") or []
        for new_alias in merge.get("new_aliases", []):
            if new_alias not in aliases:
                aliases.append(new_alias)
        tgt["aliases"] = aliases

    for eid, updates in payload.get("entity_updates", {}).items():
        ent = by_id.get(eid)
        if not ent:
            continue
        for k, v in updates.items():
            if v is None and k in ent:
                del ent[k]
            elif v is not None:
                ent[k] = v

    for eid, prune_list in payload.get("alias_pruning", {}).items():
        ent = by_id.get(eid)
        if ent and "aliases" in ent:
            prune_set = set(p.lower().strip() for p in prune_list)
            ent["aliases"] = [a for a in ent["aliases"] if a.lower().strip() not in prune_set]

    for ent in corpus:
        if ent.get("category") == "Spiritual & Cosmological Matrix":
            proverbs = ent.get("proverbs_and_oral_traditions")
            if proverbs and isinstance(proverbs, list):
                ent["proverbs_and_oral_traditions"] = clean_proverbs(proverbs, scrubbing_rules)

    return [e for e in corpus if e.get("id") not in retire_set]

def compute_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    api_corpus = json.loads(API_CORPUS_PATH.read_text(encoding="utf-8"))
    web_corpus = json.loads(WEB_CORPUS_PATH.read_text(encoding="utf-8"))

    new_api = apply_catharsis(api_corpus, payload)
    new_web = apply_catharsis(web_corpus, payload)

    API_CORPUS_PATH.write_text(json.dumps(new_api, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    WEB_CORPUS_PATH.write_text(json.dumps(new_web, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    api_sha = compute_sha256(API_CORPUS_PATH)
    web_sha = compute_sha256(WEB_CORPUS_PATH)

    print(f"✅ Canonical count: {len(new_api)} (Web: {len(new_web)})")
    print(f"✅ API SHA-256: {api_sha}")
    print(f"✅ WEB SHA-256: {web_sha}")
    if api_sha == web_sha:
        print("🔒 Dual-corpora SHA-256 bit-for-bit lockstep parity confirmed (0 bits drift).")
    else:
        raise ValueError("❌ Checksum drift detected!")

if __name__ == "__main__":
    main()
