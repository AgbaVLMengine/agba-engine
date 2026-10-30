#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 9 CORPUS ENRICHMENT
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Execution Directive: HANDOFF-AROKIN-002
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema + Mandatory Academic Provenance

Scope:
1. BATCH 9 ENRICHMENT (25 ENTITIES - INDICES 1125 TO 1149):
   - Remaining 14 Chapters of the Ọ̀bàrà Cycle:
     ODU_108_Ọ̀bàrà_Ọ̀yẹ̀kú through ODU_121_Ọ̀bàrà_Òfún
   - First 11 Chapters of the Ọ̀kànràn Cycle:
     ODU_122_Ọ̀kànràn_Ogbè through ODU_132_Ọ̀kànràn_Òtúúrúpọ̀n
   - Sovereign Parent: 'Àmọ̀lù Odù'
   - Full 14-Tier Depth: Multi-epoch antiquity timelines, dialectical philosophy,
     materiality & craftsmanship, therapeutic ethnobotany (Ewé), sacrifice (Ẹbọ),
     and authentic dual-language liturgical proverbs in canonical format:
     'Yorùbá (Parenthetical English translation and philosophical commentary).'
   - Foundational peer-reviewed academic citations:
     Wándé Abímbọ́lá (1975, 1976), William Bascom (1969), Pierre Verger (1995),
     Rowland Abiodun (2014), Babatunde Lawal (1996), Sandra Barnes (1997).
2. BAṢỌ̀RUN CONSTELLATION WIRING:
   - Enriches Baṣọ̀run as Sovereign Parent (is_parent: True, sub_variants).
   - Reciprocally connects Baṣọ̀run Gáà and Baṣọ̀run Ọlúyọ̀lé as living sub-variants.
   - Enriches Baṣọ̀run Ọlúyọ̀lé with deep historical provenance and citations.
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
BATCH_DATA_PATH = REPO_ROOT / "scripts/batch_09_data.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_batch_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Dict[str, Any]]) -> int:
    """Updates Batch 9 entities with 14-Tier depth, academic citations, proverbs, and multi-epoch timelines."""
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


def update_basorun_constellation(corpus: List[Dict[str, Any]], oluyole_entity: Dict[str, Any]) -> None:
    """Configures Baṣọ̀run as a Sovereign Parent and connects Baṣọ̀run Gáà & Basọ̀run Olúyọ̀lé cleanly without twins."""
    basorun_found = False
    gaa_found = False
    oluyole_node = None

    # Identify and merge any duplicates
    filtered_corpus = []
    for entity in corpus:
        eid = entity.get("id")
        title = entity.get("title")

        if eid == "Baṣọ̀run" or title.startswith("Baṣọ̀run (Prime Minister"):
            entity["is_parent"] = True
            entity["sub_variants"] = ["Baṣọ̀run Gáà", "Basọ̀run Olúyọ̀lé"]
            entity["living_variants"] = ["Baṣọ̀run Gáà", "Basọ̀run Olúyọ̀lé"]
            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["is_parent"] = True
                entity["details"]["sub_variants"] = ["Baṣọ̀run Gáà", "Basọ̀run Olúyọ̀lé"]
                entity["details"]["living_variants"] = ["Baṣọ̀run Gáà", "Basọ̀run Olúyọ̀lé"]
            basorun_found = True
            filtered_corpus.append(entity)

        elif eid in ["Basọ̀run Gáà", "Baṣọ̀run Gáà"] or title in ["Basọ̀run Gáà", "Baṣọ̀run Gáà"]:
            entity["title"] = "Baṣọ̀run Gáà"
            entity["is_parent"] = False
            entity["sovereign_parent"] = "Baṣọ̀run"
            entity["sovereign_parent_status"] = "Living Sub-Variant"
            aliases = set(entity.get("aliases", []))
            aliases.update(["basorun gaa", "basorun-gaa", "basọ̀run gáà", "baṣọ̀run gáà"])
            entity["aliases"] = sorted(list(aliases))
            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["is_parent"] = False
                entity["details"]["sovereign_parent"] = "Baṣọ̀run"
                entity["details"]["sovereign_parent_status"] = "Living Sub-Variant"
            gaa_found = True
            filtered_corpus.append(entity)

        elif eid in ["basorun_oluyole", "Baṣọ̀run Ọlúyọ̀lé"] or title in ["Basọ̀run Olúyọ̀lé", "Baṣọ̀run Ọlúyọ̀lé"]:
            if oluyole_node is None:
                # Merge into canonical basorun_oluyole
                entity["id"] = "basorun_oluyole"
                entity["title"] = "Basọ̀run Olúyọ̀lé"
                entity["provenance_and_citations"] = oluyole_entity.get("provenance_and_citations", "")
                aliases = set(entity.get("aliases", []))
                aliases.update(oluyole_entity.get("aliases", []))
                aliases.update(["basorun oluyole", "baṣọ̀run ọlúyọ̀lé", "oluyole", "iba oluyole"])
                entity["aliases"] = sorted(list(aliases))
                oluyole_node = entity
                filtered_corpus.append(entity)
            else:
                # Discard duplicate twin
                pass
        else:
            filtered_corpus.append(entity)

    corpus.clear()
    corpus.extend(filtered_corpus)
    print(f"  ✅ Baṣọ̀run constellation updated (Parent: {basorun_found}, Gáà: {gaa_found}, Ọlúyọ̀lé consolidated: True)")


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

    oluyole_matches = [e for e in corpus if e.get("id") in ["basorun_oluyole", "Baṣọ̀run Ọlúyọ̀lé"] or e.get("title") in ["Basọ̀run Olúyọ̀lé", "Baṣọ̀run Ọlúyọ̀lé"]]
    if len(oluyole_matches) != 1:
        raise ValueError(f"Invariant Violation: Expected exactly 1 Basọ̀run Olúyọ̀lé record, found {len(oluyole_matches)}")

    print("  ✅ Verified canonical invariants: Ẹpo-Pupa (1), Ojú Odù Méjìdínlógún (1), Àmọ̀lù Odù (1), Basọ̀run Olúyọ̀lé (1).")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING BATCH 9 ENRICHMENT & BAṢỌ̀RUN CONSTELLATION")
    print("=" * 80)

    if not BATCH_DATA_PATH.exists():
        print(f"❌ Error: Data file not found at {BATCH_DATA_PATH}")
        sys.exit(1)

    batch_data = load_json(BATCH_DATA_PATH)
    enrichments = batch_data.get("batch_9_enrichments", {})
    oluyole_entity = batch_data.get("basorun_oluyole_entity", {})

    print(f"📂 Loading API corpus from {API_CORPUS_PATH}...")
    api_corpus = load_json(API_CORPUS_PATH)
    print(f"   Initial API corpus count: {len(api_corpus)}")

    print(f"📂 Loading Web corpus from {WEB_CORPUS_PATH}...")
    web_corpus = load_json(WEB_CORPUS_PATH)
    print(f"   Initial Web corpus count: {len(web_corpus)}")

    # 1. Apply Batch 9 Enrichments
    print(f"\n▶ [STEP 1] Applying Batch 9 Enrichments across {len(enrichments)} entities...")
    updated_api = apply_batch_enrichments(api_corpus, enrichments)
    updated_web = apply_batch_enrichments(web_corpus, enrichments)
    print(f"   Updated {updated_api} entities in API corpus.")
    print(f"   Updated {updated_web} entities in Web corpus.")

    # 2. Update Baṣọ̀run Constellation & Ingest Baṣọ̀run Ọlúyọ̀lé
    print("\n▶ [STEP 2] Wiring Baṣọ̀run Constellation & Ingesting Baṣọ̀run Ọlúyọ̀lé...")
    update_basorun_constellation(api_corpus, oluyole_entity)
    update_basorun_constellation(web_corpus, oluyole_entity)

    # 3. Verify Canonical Invariants
    print("\n▶ [STEP 3] Verifying Zero Twin Nodes Invariants...")
    verify_canonical_invariants(api_corpus)
    verify_canonical_invariants(web_corpus)

    # 4. Save Synchronized Corpora
    print("\n▶ [STEP 4] Persisting Synchronized Master Corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("✅ Successfully saved both API and Web corpora in lockstep.")
    print(f"   Final API corpus count: {len(api_corpus)}")
    print(f"   Final Web corpus count: {len(web_corpus)}")
    print("=" * 80)


if __name__ == "__main__":
    main()
