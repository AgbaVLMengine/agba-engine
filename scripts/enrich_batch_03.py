#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 3 CORPUS ENRICHMENT & DEDUPLICATION CLEANUP
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema + Mandatory Academic Provenance

Scope:
1. DEDUPLICATION CLEANUP:
   - Consolidate Aso-Ẹbí + Aṣọ Ẹ̀bị́ -> canonical Aṣọ-Ẹbí.
   - Consolidate Otun-Iyalode + Otun Iyalode -> canonical Otun-Ìyál'óde.
2. BATCH 3 ENRICHMENT (25 ENTITIES):
   - Ingest mandatory academic provenance citations across items 300 to 324
     from scripts/thin_entities_manifest.json.
   - Polish proverbs into pristine dual-language format.
3. SYNCHRONIZATION:
   - Synchronize api/data/yoruba_corpus_1007_NORMALIZED.json and
     web/src/data/yoruba_master_corpus.json in lockstep.
=============================================================================
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"
BATCH_DATA_PATH = REPO_ROOT / "scripts/batch_03_data.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_deduplication(corpus: List[Dict[str, Any]], deduplications: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Merges twin duplicate nodes into single canonical records."""
    cleaned_corpus = list(corpus)

    for dedup in deduplications:
        targets = set(dedup["targets_to_replace"])
        canonical_data = dedup["data"]
        canonical_title = dedup["canonical_title"]

        # Find first matching index to insert at, then remove all target matches
        insert_idx = None
        filtered = []
        for idx, entity in enumerate(cleaned_corpus):
            title = entity.get("title")
            if title in targets or entity.get("id") in targets:
                if insert_idx is None:
                    insert_idx = len(filtered)
            else:
                filtered.append(entity)

        if insert_idx is not None:
            filtered.insert(insert_idx, canonical_data)
            print(f"  [DEDUP] Replaced {list(targets)} -> single canonical '{canonical_title}' at index {insert_idx}")
        else:
            # If targets not found, ensure canonical exists
            existing = any(e.get("title") == canonical_title for e in filtered)
            if not existing:
                filtered.append(canonical_data)
                print(f"  [DEDUP] Appended canonical '{canonical_title}'")

        cleaned_corpus = filtered

    return cleaned_corpus


def apply_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Dict[str, Any]]) -> int:
    """Updates Batch 3 entities with academic citations and polished proverbs."""
    updated_count = 0

    for entity in corpus:
        title = entity.get("title")
        if title in enrichments:
            enrich_info = enrichments[title]

            for key, val in enrich_info.items():
                entity[key] = val

            # Keep details dictionary in sync for frontend if present
            if "details" in entity and isinstance(entity["details"], dict):
                for key, val in enrich_info.items():
                    entity["details"][key] = val

            updated_count += 1

    return updated_count


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 3 ENRICHMENT & DEDUPLICATION PASS")
    print("=" * 80)

    if not BATCH_DATA_PATH.exists():
        print(f"❌ Error: Data file not found at {BATCH_DATA_PATH}")
        sys.exit(1)

    batch_data = load_json(BATCH_DATA_PATH)
    deduplications = batch_data.get("deduplications", [])
    enrichments = batch_data.get("batch_3_enrichments", {})

    print(f"📂 Loading API corpus from {API_CORPUS_PATH}...")
    api_corpus = load_json(API_CORPUS_PATH)
    print(f"   Initial API corpus count: {len(api_corpus)}")

    print(f"📂 Loading Web corpus from {WEB_CORPUS_PATH}...")
    web_corpus = load_json(WEB_CORPUS_PATH)
    print(f"   Initial Web corpus count: {len(web_corpus)}")

    # 1. Apply Deduplications
    print("\n▶ [STEP 1] Applying Deduplications...")
    api_corpus = apply_deduplication(api_corpus, deduplications)
    web_corpus = apply_deduplication(web_corpus, deduplications)
    print(f"   Post-dedup API corpus count: {len(api_corpus)}")
    print(f"   Post-dedup Web corpus count: {len(web_corpus)}")

    # 2. Apply Batch 3 Enrichments
    print("\n▶ [STEP 2] Applying Batch 3 Enrichments (25 entities)...")
    updated_api = apply_enrichments(api_corpus, enrichments)
    updated_web = apply_enrichments(web_corpus, enrichments)
    print(f"   Updated {updated_api} / {len(enrichments)} in API corpus.")
    print(f"   Updated {updated_web} / {len(enrichments)} in Web corpus.")

    # 3. Save Synchronized Corpora
    print("\n▶ [STEP 3] Persisting Synchronized Master Corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("✅ Successfully saved both API and Web corpora.")
    print("=" * 80)


if __name__ == "__main__":
    main()
