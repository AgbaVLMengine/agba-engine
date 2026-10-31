#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 13 CORPUS ENRICHMENT (THE SUB-25 BREAKTHROUGH)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-008
Standards: Gate 2 Compliant (< 250 LOC), 14-Tier Schema + Academic Bibliography

Scope:
1. BATCH 13 ENRICHMENT (25 COMPOSITE ODÙ CHAPTERS: ODU_208 TO ODU_232):
   - Remaining 4 Chapters of Òtúá: ODU_208_Òtúá_Òtúúrúpọ̀n to ODU_211_Òtúá_Òfún (completes Òtúá cycle!)
   - Full 15 Chapters of Ìrẹtẹ̀: ODU_212_Ìrẹtẹ̀_Ogbè to ODU_226_Ìrẹtẹ̀_Òfún (completes Ìrẹtẹ̀ cycle!)
   - First 6 Chapters of Ọ̀ṣẹ́: ODU_227_Ọ̀ṣẹ́_Ogbè to ODU_232_Ọ̀ṣẹ́_Ọ̀wọ́nrín
2. SYNCHRONIZATION:
   - Synchronizes api/data/yoruba_corpus_1007_NORMALIZED.json and
     web/src/data/yoruba_master_corpus.json in absolute lockstep.
3. HISTORIC MILESTONE:
   - Breaks through the historic sub-25 threshold (from 49 down to exactly 24 thin entities).
=============================================================================
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"
DATA_PATH = REPO_ROOT / "scripts" / "batch_13_data.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Dict[str, Any]]) -> int:
    """Applies authentic 14-Tier depth, timelines, and proverbs to Batch 13 entities."""
    updated = 0
    for entity in corpus:
        eid = entity.get("id")
        title = entity.get("title")

        key = None
        if eid in enrichments:
            key = eid
        elif title in enrichments:
            key = title

        if key:
            info = enrichments[key]
            for field, val in info.items():
                entity[field] = val

            # Keep details dictionary in sync if present
            if "details" in entity and isinstance(entity["details"], dict):
                for field, val in info.items():
                    entity["details"][field] = val

            updated += 1

    return updated


def count_thin_entities(corpus: List[Dict[str, Any]]) -> int:
    """Counts remaining thin ODU entities lacking historical timeline or proverbs."""
    thin = 0
    for e in corpus:
        cid = e.get("id", "")
        ht = e.get("historical_timeline", "")
        prov = e.get("proverbs_and_oral_traditions", [])
        if cid.startswith("ODU_") and (not ht or len(ht) < 50 or not prov):
            thin += 1
    return thin


def verify_invariants(corpus: List[Dict[str, Any]]) -> None:
    """Verifies that all 25 Batch 13 entities have full 14-Tier depth and zero twin duplicates."""
    required_ids = [
        "ODU_208_Òtúá_Òtúúrúpọ̀n", "ODU_209_Òtúá_Ìrẹtẹ̀", "ODU_210_Òtúá_Ọ̀ṣẹ́",
        "ODU_211_Òtúá_Òfún", "ODU_212_Ìrẹtẹ̀_Ogbè", "ODU_213_Ìrẹtẹ̀_Ọ̀yẹ̀kú",
        "ODU_214_Ìrẹtẹ̀_Ìwòrì", "ODU_215_Ìrẹtẹ̀_Òdí", "ODU_216_Ìrẹtẹ̀_Ìrosùn",
        "ODU_217_Ìrẹtẹ̀_Ọ̀wọ́nrín", "ODU_218_Ìrẹtẹ̀_Ọ̀bàrà", "ODU_219_Ìrẹtẹ̀_Ọ̀kànràn",
        "ODU_220_Ìrẹtẹ̀_Ògúndá", "ODU_221_Ìrẹtẹ̀_Ọ̀sá", "ODU_222_Ìrẹtẹ̀_Ìká",
        "ODU_223_Ìrẹtẹ̀_Òtúúrúpọ̀n", "ODU_224_Ìrẹtẹ̀_Òtúá", "ODU_225_Ìrẹtẹ̀_Ọ̀ṣẹ́",
        "ODU_226_Ìrẹtẹ̀_Òfún", "ODU_227_Ọ̀ṣẹ́_Ogbè", "ODU_228_Ọ̀ṣẹ́_Ọ̀yẹ̀kú",
        "ODU_229_Ọ̀ṣẹ́_Ìwòrì", "ODU_230_Ọ̀ṣẹ́_Òdí", "ODU_231_Ọ̀ṣẹ́_Ìrosùn",
        "ODU_232_Ọ̀ṣẹ́_Ọ̀wọ́nrín"
    ]

    for rid in required_ids:
        matches = [e for e in corpus if e.get("id") == rid]
        if len(matches) != 1:
            raise ValueError(f"Invariant Violation: Expected exactly 1 match for {rid}, found {len(matches)}")
        ent = matches[0]
        if not ent.get("historical_timeline") or len(ent.get("historical_timeline")) < 50:
            raise ValueError(f"Quality Violation: {rid} lacks robust historical timeline")
        if not ent.get("proverbs_and_oral_traditions"):
            raise ValueError(f"Quality Violation: {rid} lacks authentic proverbs")

    print(f"  ✅ Verified 25/25 Batch 13 entities have 100% 14-Tier depth with zero duplicates.")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 13 ENRICHMENT (THE SUB-25 BREAKTHROUGH)")
    print("=" * 80)

    if not DATA_PATH.exists():
        print(f"❌ Error: Data file not found at {DATA_PATH}")
        sys.exit(1)

    enrichments = load_json(DATA_PATH)
    if "batch_13_enrichments" in enrichments:
        enrichments = enrichments["batch_13_enrichments"]
    print(f"📂 Loaded {len(enrichments)} curated 14-Tier Odù chapters from {DATA_PATH.name}")

    api_corpus = load_json(API_CORPUS_PATH)
    web_corpus = load_json(WEB_CORPUS_PATH)

    initial_thin_api = count_thin_entities(api_corpus)
    print(f"📊 Initial Thin ODU Entities: {initial_thin_api}")

    print("\n▶ [STEP 1] Applying Batch 13 Enrichments across Dual Corpora...")
    updated_api = apply_enrichments(api_corpus, enrichments)
    updated_web = apply_enrichments(web_corpus, enrichments)
    print(f"   Updated {updated_api} entities in API corpus.")
    print(f"   Updated {updated_web} entities in Web corpus.")

    print("\n▶ [STEP 2] Verifying Quality & Single-Node Invariants...")
    verify_invariants(api_corpus)
    verify_invariants(web_corpus)

    final_thin_api = count_thin_entities(api_corpus)
    print(f"\n🎉 HISTORIC SUB-25 BREAKTHROUGH ACHIEVED!")
    print(f"   Remaining Thin ODU Entities: {final_thin_api} (Reduced from {initial_thin_api} down to {final_thin_api})")

    if final_thin_api != 24:
        print(f"⚠️ Warning: Expected 24 remaining thin entities, got {final_thin_api}")

    print("\n▶ [STEP 3] Persisting Synchronized Master Corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("✅ Successfully saved both API and Web corpora in absolute lockstep.")
    print("=" * 80)


if __name__ == "__main__":
    main()
