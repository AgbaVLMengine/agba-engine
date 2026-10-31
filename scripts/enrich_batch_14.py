#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 14 CORPUS ENRICHMENT (THE 256 ODÙ IFÁ GRAND FINALE)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-009
Standards: Gate 2 Compliant (< 250 LOC), 14-Tier Schema + Academic Bibliography

Scope:
1. BATCH 14 ENRICHMENT (FINAL 24 COMPOSITE ODÙ CHAPTERS: ODU_233 TO ODU_256):
   - Remaining 9 Chapters of Ọ̀ṣẹ́: ODU_233_Ọ̀ṣẹ́_Ọ̀bàrà to ODU_241_Ọ̀ṣẹ́_Òfún (completes Ọ̀ṣẹ́ cycle!)
   - Full 15 Chapters of Òfún: ODU_242_Òfún_Ogbè to ODU_256_Òfún_Ọ̀ṣẹ́ (completes Òfún cycle!)
2. SYNCHRONIZATION:
   - Synchronizes api/data/yoruba_corpus_1007_NORMALIZED.json and
     web/src/data/yoruba_master_corpus.json in absolute lockstep.
3. HISTORIC GRAND FINALE:
   - Drops thin Odù chapters from 24 down to exactly ZERO (0)!
   - 100% completion of the entire 256 Odù Ifá corpus with full 14-Tier depth!
=============================================================================
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"
DATA_PATH = REPO_ROOT / "scripts" / "batch_14_data.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Dict[str, Any]]) -> int:
    """Applies authentic 14-Tier depth, timelines, and proverbs to Batch 14 entities."""
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
    """Verifies that all 24 Batch 14 entities have full 14-Tier depth and zero twin duplicates."""
    required_ids = [
        "ODU_233_Ọ̀ṣẹ́_Ọ̀bàrà", "ODU_234_Ọ̀ṣẹ́_Ọ̀kànràn", "ODU_235_Ọ̀ṣẹ́_Ògúndá",
        "ODU_236_Ọ̀ṣẹ́_Ọ̀sá", "ODU_237_Ọ̀ṣẹ́_Ìká", "ODU_238_Ọ̀ṣẹ́_Òtúúrúpọ̀n",
        "ODU_239_Ọ̀ṣẹ́_Òtúá", "ODU_240_Ọ̀ṣẹ́_Ìrẹtẹ̀", "ODU_241_Ọ̀ṣẹ́_Òfún",
        "ODU_242_Òfún_Ogbè", "ODU_243_Òfún_Ọ̀yẹ̀kú", "ODU_244_Òfún_Ìwòrì",
        "ODU_245_Òfún_Òdí", "ODU_246_Òfún_Ìrosùn", "ODU_247_Òfún_Ọ̀wọ́nrín",
        "ODU_248_Òfún_Ọ̀bàrà", "ODU_249_Òfún_Ọ̀kànràn", "ODU_250_Òfún_Ògúndá",
        "ODU_251_Òfún_Ọ̀sá", "ODU_252_Òfún_Ìká", "ODU_253_Òfún_Òtúúrúpọ̀n",
        "ODU_254_Òfún_Òtúá", "ODU_255_Òfún_Ìrẹtẹ̀", "ODU_256_Òfún_Ọ̀ṣẹ́"
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

    print(f"  ✅ Verified 24/24 Batch 14 entities have 100% 14-Tier depth with zero duplicates.")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 14 ENRICHMENT (256 ODÙ GRAND FINALE)")
    print("=" * 80)

    if not DATA_PATH.exists():
        print(f"❌ Error: Data file not found at {DATA_PATH}")
        sys.exit(1)

    enrichments = load_json(DATA_PATH)
    if "batch_14_enrichments" in enrichments:
        enrichments = enrichments["batch_14_enrichments"]
    print(f"📂 Loaded {len(enrichments)} curated 14-Tier Odù chapters from {DATA_PATH.name}")

    api_corpus = load_json(API_CORPUS_PATH)
    web_corpus = load_json(WEB_CORPUS_PATH)

    initial_thin_api = count_thin_entities(api_corpus)
    print(f"📊 Initial Thin ODU Entities: {initial_thin_api}")

    print("\n▶ [STEP 1] Applying Batch 14 Enrichments across Dual Corpora...")
    updated_api = apply_enrichments(api_corpus, enrichments)
    updated_web = apply_enrichments(web_corpus, enrichments)
    print(f"   Updated {updated_api} entities in API corpus.")
    print(f"   Updated {updated_web} entities in Web corpus.")

    print("\n▶ [STEP 2] Verifying Quality & Single-Node Invariants...")
    verify_invariants(api_corpus)
    verify_invariants(web_corpus)

    final_thin_api = count_thin_entities(api_corpus)
    print(f"\n🎉 HISTORIC GRAND FINALE MILESTONE ACHIEVED!")
    print(f"   Remaining Thin ODU Entities: {final_thin_api} (Reduced from {initial_thin_api} down to {final_thin_api})")

    if final_thin_api != 0:
        print(f"⚠️ Warning: Expected exactly 0 remaining thin entities, got {final_thin_api}")
    else:
        print("🏆 100% COMPLETE: ALL 256 ODÙ IFÁ CHAPTERS ARE NOW FULLY ENRICHED!")

    print("\n▶ [STEP 3] Persisting Synchronized Master Corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("✅ Successfully saved both API and Web corpora in absolute lockstep.")
    print("=" * 80)


if __name__ == "__main__":
    main()
