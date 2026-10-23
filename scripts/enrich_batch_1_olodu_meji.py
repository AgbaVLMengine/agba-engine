#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: BATCH 1 CORPUS ENRICHMENT - 16 PRINCIPAL OLÓDÙ IFÁ (OJÚ ODÙ MÉJÌ)
=============================================================================
Author: Àrọ̀kìn (Royal Chronicler & Dedicated Corpus Enrichment Subagent)
Recipient: 4c52730f-614b-45ce-9524-153c7a41e058
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Authentic Yorùbá Schema

Enriches the 16 Principal Olódù Ifá:
1. ODU_001_Ogbè (Èjì Ogbè)
2. ODU_002_Ọ̀yẹ̀kú (Ọ̀yẹ̀kú Méjì)
3. ODU_003_Ìwòrì (Ìwòrì Méjì)
4. ODU_004_Òdí (Òdí Méjì)
5. ODU_005_Ìrosùn (Ìrosùn Méjì)
6. ODU_006_Ọ̀wọ́nrín (Ọ̀wọ́nrín Méjì)
7. ODU_007_Ọ̀bàrà (Ọ̀bàrà Méjì)
8. ODU_008_Ọ̀kànràn (Ọ̀kànràn Méjì)
9. ODU_009_Ògúndá (Ògúndá Méjì)
10. ODU_010_Ọ̀sá (Ọ̀sá Méjì)
11. ODU_011_Ìká (Ìká Méjì)
12. ODU_012_Òtúúrúpọ̀n (Òtúúrúpọ̀n Méjì)
13. ODU_013_Òtúá (Òtúá Méjì)
14. ODU_014_Ìrẹtẹ̀ (Ìrẹtẹ̀ Méjì)
15. ODU_015_Ọ̀ṣẹ́ (Ọ̀ṣẹ́ Méjì)
16. ODU_016_Òfún (Òfún Méjì)

Updates:
- /home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json
- /home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json
=============================================================================
"""

import json
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"
DATA_FILE = REPO_ROOT / "scripts/olodu_meji_batch_1_data.json"

TARGET_ODU_IDS = [
    "ODU_001_Ogbè",
    "ODU_002_Ọ̀yẹ̀kú",
    "ODU_003_Ìwòrì",
    "ODU_004_Òdí",
    "ODU_005_Ìrosùn",
    "ODU_006_Ọ̀wọ́nrín",
    "ODU_007_Ọ̀bàrà",
    "ODU_008_Ọ̀kànràn",
    "ODU_009_Ògúndá",
    "ODU_010_Ọ̀sá",
    "ODU_011_Ìká",
    "ODU_012_Òtúúrúpọ̀n",
    "ODU_013_Òtúá",
    "ODU_014_Ìrẹtẹ̀",
    "ODU_015_Ọ̀ṣẹ́",
    "ODU_016_Òfún"
]


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def validate_olodu_entity(entity: Dict[str, Any], entity_id: str) -> None:
    """Verifies that the entity meets full 14-Tier parity."""
    required_keys = [
        "historical_timeline",
        "etymology_and_philosophy",
        "material_and_craftsmanship",
        "social_and_ritual_context",
        "proverbs_and_oral_traditions",
        "diaspora_connections",
        "media_production_notes",
        "details"
    ]
    for key in required_keys:
        assert key in entity, f"Missing required key '{key}' in {entity_id}"
        assert entity[key], f"Key '{key}' is empty in {entity_id}"

    # Verify historical timeline length and content
    timeline = entity["historical_timeline"]
    assert len(timeline) >= 200, f"Timeline too short in {entity_id}: {len(timeline)} chars"
    assert "Ilé-Ifẹ̀" in timeline, f"Missing Ilé-Ifẹ̀ antiquity in {entity_id}"
    assert "UNESCO" in timeline, f"Missing UNESCO status in {entity_id}"

    # Verify proverbs format
    provs = entity["proverbs_and_oral_traditions"]
    assert isinstance(provs, list), f"Proverbs must be a list in {entity_id}"
    assert 2 <= len(provs) <= 3, f"Expected 2-3 proverbs in {entity_id}, found {len(provs)}"
    for p in provs:
        assert "(" in p and ")" in p, f"Invalid bilingual proverb format in {entity_id}: {p}"

    # Verify details mirrored dictionary
    details = entity["details"]
    assert isinstance(details, dict), f"'details' must be a dict in {entity_id}"
    for k in ["historical_timeline", "etymology_and_philosophy", "material_and_craftsmanship",
              "social_and_ritual_context", "proverbs_and_oral_traditions",
              "diaspora_connections", "media_production_notes"]:
        assert k in details, f"Missing key '{k}' in details for {entity_id}"
        assert details[k] == entity[k], f"Mismatch between top-level and details for '{k}' in {entity_id}"


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 1 OLÓDÙ IFÁ ENRICHMENT (OJÚ ODÙ MÉJÌ)")
    print(f"   Target Entities: {len(TARGET_ODU_IDS)}")
    print("=" * 80)

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Enrichment data file not found at {DATA_FILE}")

    enrichment_data: Dict[str, Dict[str, Any]] = load_json(DATA_FILE)
    print(f"Loaded enrichment data for {len(enrichment_data)} entities.")

    for oid in TARGET_ODU_IDS:
        if oid not in enrichment_data:
            raise KeyError(f"Missing enrichment data for target ID: {oid}")

    api_corpus = load_json(API_CORPUS)
    web_corpus = load_json(WEB_CORPUS)

    api_by_id = {e.get("id"): e for e in api_corpus}
    web_by_id = {e.get("id"): e for e in web_corpus}

    enriched_count = 0
    for entity_id in TARGET_ODU_IDS:
        fields = enrichment_data[entity_id]

        if entity_id not in api_by_id:
            raise KeyError(f"Entity '{entity_id}' not found in API corpus ({API_CORPUS})!")
        if entity_id not in web_by_id:
            raise KeyError(f"Entity '{entity_id}' not found in Web corpus ({WEB_CORPUS})!")

        for target in [api_by_id[entity_id], web_by_id[entity_id]]:
            # Update top-level enriched keys
            for k, v in fields.items():
                target[k] = v

            # Construct / mirror the 'details' dict for frontend compatibility
            details = target.get("details", {})
            if not isinstance(details, dict):
                details = {}
            for k in ["description", "historical_timeline", "etymology_and_philosophy",
                      "material_and_craftsmanship", "social_and_ritual_context",
                      "proverbs_and_oral_traditions", "diaspora_connections",
                      "media_production_notes"]:
                if k in target:
                    details[k] = target[k]
            target["details"] = details

        # Validate parity for both API and Web entities
        validate_olodu_entity(api_by_id[entity_id], f"API:{entity_id}")
        validate_olodu_entity(web_by_id[entity_id], f"Web:{entity_id}")

        print(f"  ✅ [ENRICHED & VALIDATED] '{entity_id}' ({api_by_id[entity_id].get('title', '')}) -> 14-Tier Parity Achieved")
        enriched_count += 1

    save_json(API_CORPUS, api_corpus)
    save_json(WEB_CORPUS, web_corpus)

    print("=" * 80)
    print(f"🎉 SUCCESS: Enriched and verified {enriched_count}/16 Principal Olódù Ifá.")
    print(f"📁 Updated API Corpus: {API_CORPUS}")
    print(f"📁 Updated Web Corpus: {WEB_CORPUS}")
    print("=" * 80)


if __name__ == "__main__":
    main()
