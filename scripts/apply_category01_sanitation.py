#!/usr/bin/env python3
"""
Category 1 Plenary Sanitation & Disambiguation Runner (HANDOFF-AROKIN-002).
Applies surgical fixes synchronously to dual corpora under Gate 2 (<100 LOC).
"""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAYLOAD_PATH = ROOT / "scripts/data/batches/category01_sanitation_payloads.json"
API_PATH = ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = ROOT / "web/src/data/yoruba_master_corpus.json"

def apply_sanitation(corpus, payload):
    # 1. Retire deprecated/merged nodes
    retire_set = set(payload.get("retire_ids", []))
    corpus = [e for e in corpus if e.get("id") not in retire_set]
    by_id = {e.get("id"): e for e in corpus}
    
    # 2. Apply entity updates (titles, aliases, sub_variants, related_entities)
    for eid, updates in payload.get("entity_updates", {}).items():
        ent = by_id.get(eid)
        if not ent:
            raise KeyError(f"Target entity {eid} missing from corpus!")
        for k, v in updates.items():
            ent[k] = v

    # 3. Apply facet expansions (>600 chars, full triads, multi-citations)
    for pid, facets in payload.get("facet_updates", {}).items():
        parent = by_id.get(pid)
        if not parent:
            raise KeyError(f"Facet parent {pid} missing from corpus!")
        parent_facets = parent.setdefault("sub_variant_facets", {})
        for fname, fdata in facets.items():
            parent_facets[fname] = fdata
            svs = parent.setdefault("sub_variants", [])
            if fname not in svs and not any(fname in s for s in svs):
                svs.append(fname)

    # 4. Assert referential integrity on critical invariants
    assert by_id["Onile"]["title"] == "Onílẹ̀ (Primordial Earth Divinity)"
    assert by_id["Onile"]["id"] == "Onile"  # Strict immutable ID lock
    assert by_id["Àjà"]["title"] == "Àjà (Forest Whirlwind Spirit)"
    assert by_id["Àjà"]["id"] == "Àjà"      # Strict immutable ID lock
    assert by_id["Ọbá"]["title"] == "Ọbá (River Divinity of Marital Devotion)"
    assert by_id["Ọbá"]["id"] == "Ọbá"      # Strict immutable ID lock
    assert "Àgéré Ifá" not in by_id         # Homograph retired
    assert by_id["opon_ifa_olori_esu"]["sub_variants"] == []
    assert by_id["opon_ifa_gbero"]["sub_variants"] == []
    assert by_id["CORPUS_OLOKUN_001"]["related_entities"][0] == "Yemọja"
    assert "Adé Ìlẹ̀kẹ̀" in by_id["CORPUS_OLOKUN_001"]["related_entities"]
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
