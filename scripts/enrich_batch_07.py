#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 7 CORPUS ENRICHMENT
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema + Mandatory Academic Provenance

Scope:
1. BATCH 7 ENRICHMENT (25 ENTITIES - ÌWÒRÌ, ÒDÍ & ÌROSÙN CYCLES OF ÀMỌ̀LÙ ODÙ):
   - 4 Composite Chapters of the Ìwòrì cycle (Ìwòrì Òtúá through Ìwòrì Òfún)
   - 15 Composite Chapters of the Òdí cycle (Òdí Ogbè through Òdí Òfún)
   - 6 Composite Chapters of the Ìrosùn cycle (Ìrosùn Ogbè through Ìrosùn Ọ̀bàrà)
   - 100% carrying authentic dual-language liturgical proverbs in the canonical format:
     'Yorùbá (Parenthetical English translation and philosophical commentary).'
   - Full multi-epoch antiquity timelines, materials/craftsmanship, and academic provenance.
2. SYNCHRONIZATION:
   - Synchronizes api/data/yoruba_corpus_1007_NORMALIZED.json and
     web/src/data/yoruba_master_corpus.json in absolute lockstep.
=============================================================================
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"
BATCH_DATA_PATH = REPO_ROOT / "scripts/batch_07_data.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_batch_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Any]) -> int:
    updated_count = 0
    title_to_enrichment = {}
    for key, data in enrichments.items():
        clean_title = key.split("_", 2)[-1].replace("_", " ") if "_" in key else key
        title_to_enrichment[clean_title] = data
        title_to_enrichment[key] = data

    for entity in corpus:
        t = entity.get("title")
        i = entity.get("id")
        enrich_data = title_to_enrichment.get(t) or title_to_enrichment.get(i)

        if enrich_data:
            for field in [
                "historical_timeline",
                "etymology_and_philosophy",
                "material_and_craftsmanship",
                "social_and_ritual_context",
                "proverbs_and_oral_traditions",
                "provenance_and_citations"
            ]:
                if field in enrich_data:
                    entity[field] = enrich_data[field]
                    if "details" in entity and isinstance(entity["details"], dict):
                        entity["details"][field] = enrich_data[field]
            updated_count += 1

    return updated_count


def verify_canonical_invariants(corpus: List[Dict[str, Any]]) -> None:
    """Verifies that no twin duplicate nodes exist and critical sovereign records are intact."""
    oju_matches = [e for e in corpus if e.get("id") == "Oju_Odu_Mejidinlogun" or e.get("title") == "Ojú Odù Méjìdínlógún"]
    if len(oju_matches) != 1:
        raise ValueError(f"Invariant Violation: Expected exactly 1 Ojú Odù Méjìdínlógún record, found {len(oju_matches)}")

    amolu_matches = [e for e in corpus if e.get("id") == "Amolu_Odu" or e.get("title") == "Àmọ̀lù Odù"]
    if len(amolu_matches) != 1:
        raise ValueError(f"Invariant Violation: Expected exactly 1 Àmọ̀lù Odù record, found {len(amolu_matches)}")

    print("  ✅ Verified canonical invariants: Ojú Odù Méjìdínlógún (1), Àmọ̀lù Odù (1).")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 7 ENRICHMENT (ÌWÒRÌ, ÒDÍ & ÌROSÙN CYCLES)")
    print("=" * 80)

    if not BATCH_DATA_PATH.exists():
        print(f"❌ Error: Data file not found at {BATCH_DATA_PATH}")
        sys.exit(1)

    batch_data = load_json(BATCH_DATA_PATH)
    enrichments = batch_data.get("batch_7_enrichments", {})

    print(f"📂 Loading API corpus from {API_CORPUS_PATH}...")
    api_corpus = load_json(API_CORPUS_PATH)
    print(f"   Initial API corpus count: {len(api_corpus)}")

    print(f"📂 Loading Web corpus from {WEB_CORPUS_PATH}...")
    web_corpus = load_json(WEB_CORPUS_PATH)
    print(f"   Initial Web corpus count: {len(web_corpus)}")

    # 1. Apply Batch 7 Enrichments
    print(f"\n▶ [STEP 1] Applying Batch 7 Enrichments across {len(enrichments)} entities...")
    updated_api = apply_batch_enrichments(api_corpus, enrichments)
    updated_web = apply_batch_enrichments(web_corpus, enrichments)
    print(f"   Updated {updated_api} entities in API corpus.")
    print(f"   Updated {updated_web} entities in Web corpus.")

    # 2. Verify Invariants
    print("\n▶ [STEP 2] Verifying Canonical Invariants...")
    verify_canonical_invariants(api_corpus)
    verify_canonical_invariants(web_corpus)

    # 3. Save Synchronized Corpora
    print("\n▶ [STEP 3] Persisting Synchronized Master Corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("✅ Successfully saved both API and Web corpora in lockstep.")
    print("=" * 80)


if __name__ == "__main__":
    main()
