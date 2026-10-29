#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 8 CORPUS ENRICHMENT
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Execution Directive: HANDOFF-AROKIN-BATCH-008
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema + Mandatory Academic Provenance

Scope:
1. BATCH 8 ENRICHMENT (25 ENTITIES - INDICES 1100 TO 1124):
   - Remaining 9 Chapters of the Ìrosùn Cycle:
     ODU_083_Ìrosùn_Ọ̀kànràn through ODU_091_Ìrosùn_Òfún
   - Full 15 Chapters of the Ọ̀wọ́nrín Cycle:
     ODU_092_Ọ̀wọ́nrín_Ogbè through ODU_106_Ọ̀wọ́nrín_Òfún
   - First Chapter of the Ọ̀bàrà Cycle:
     ODU_107_Ọ̀bàrà_Ogbè
   - Sovereign Parent: 'Àmọ̀lù Odù'
   - Full 14-Tier Depth: Multi-epoch antiquity timelines (Classical Ifẹ̀, Imperial Ọ̀yọ́,
     Transatlantic Lucumí & Candomblé), dialectical philosophy, materiality & craftsmanship,
     therapeutic ethnobotany (Ewé), sacrifice (Ẹbọ), and authentic dual-language liturgical
     proverbs in canonical format: 'Yorùbá (Parenthetical English translation and philosophical commentary).'
   - Foundational peer-reviewed academic citations:
     Wándé Abímbọ́lá (1975, 1976), William Bascom (1969), Pierre Verger (1995),
     Rowland Abiodun (2014), Babatunde Lawal (1996), Sandra Barnes (1997).
2. ZERO TWIN NODES & CANONICAL INVARIANTS:
   - Verifies Ẹpo-Pupa, Ojú Odù Méjìdínlógún, and Àmọ̀lù Odù retain single canonical integrity.
3. SYNCHRONIZATION:
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
BATCH_DATA_PATH = REPO_ROOT / "scripts/batch_08_data.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_batch_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Dict[str, Any]]) -> int:
    """Updates Batch 8 entities with 14-Tier depth, academic citations, proverbs, and multi-epoch timelines."""
    updated_count = 0

    for entity in corpus:
        title = entity.get("title")
        ent_id = entity.get("id")

        matched_key = None
        if ent_id in enrichments:
            matched_key = ent_id
        elif title in enrichments:
            matched_key = title

        if matched_key:
            enrich_info = enrichments[matched_key]

            for key, val in enrich_info.items():
                entity[key] = val

            # Keep details dictionary in sync for frontend if present
            if "details" in entity and isinstance(entity["details"], dict):
                for key, val in enrich_info.items():
                    entity["details"][key] = val

            updated_count += 1

    return updated_count


def verify_canonical_invariants(corpus: List[Dict[str, Any]]) -> None:
    """Verifies that no twin duplicate nodes exist and critical sovereign records are intact."""
    pupa_matches = [e for e in corpus if e.get("title") in ["Ẹpọ Pupa", "Epo-Pupa", "Ẹpo-Pupa"] or e.get("id") in ["Ẹpọ Pupa", "Epo-Pupa", "Ẹpo-Pupa"]]
    if len(pupa_matches) != 1:
        raise ValueError(f"Invariant Violation: Expected exactly 1 Ẹpo-Pupa canonical record, found {len(pupa_matches)}")

    oju_matches = [e for e in corpus if e.get("id") == "Oju_Odu_Mejidinlogun" or e.get("title") == "Ojú Odù Méjìdínlógún"]
    if len(oju_matches) != 1:
        raise ValueError(f"Invariant Violation: Expected exactly 1 Ojú Odù Méjìdínlógún record, found {len(oju_matches)}")

    amolu_matches = [e for e in corpus if e.get("id") == "Amolu_Odu" or e.get("title") == "Àmọ̀lù Odù"]
    if len(amolu_matches) != 1:
        raise ValueError(f"Invariant Violation: Expected exactly 1 Àmọ̀lù Odù record, found {len(amolu_matches)}")

    print("  ✅ Verified canonical invariants: Ẹpo-Pupa (1), Ojú Odù Méjìdínlógún (1), Àmọ̀lù Odù (1).")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 8 ENRICHMENT (INDICES 1100 TO 1124)")
    print("=" * 80)

    if not BATCH_DATA_PATH.exists():
        print(f"❌ Error: Data file not found at {BATCH_DATA_PATH}")
        sys.exit(1)

    batch_data = load_json(BATCH_DATA_PATH)
    enrichments = batch_data.get("batch_8_enrichments", {})

    print(f"📂 Loading API corpus from {API_CORPUS_PATH}...")
    api_corpus = load_json(API_CORPUS_PATH)
    print(f"   Initial API corpus count: {len(api_corpus)}")

    print(f"📂 Loading Web corpus from {WEB_CORPUS_PATH}...")
    web_corpus = load_json(WEB_CORPUS_PATH)
    print(f"   Initial Web corpus count: {len(web_corpus)}")

    # 1. Apply Batch 8 Enrichments
    print(f"\n▶ [STEP 1] Applying Batch 8 Enrichments across {len(enrichments)} entities...")
    updated_api = apply_batch_enrichments(api_corpus, enrichments)
    updated_web = apply_batch_enrichments(web_corpus, enrichments)
    print(f"   Updated {updated_api} entities in API corpus.")
    print(f"   Updated {updated_web} entities in Web corpus.")

    # 2. Verify Invariants
    print("\n▶ [STEP 2] Verifying Zero Twin Nodes Invariants...")
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
