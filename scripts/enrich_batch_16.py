#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 16 CORPUS ENRICHMENT (ENTITIES 25-49)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Corpus Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-003 (Batch 16 Non-Odù Hardening: Entities 25–49)
Standards: Gate 2 Compliant (< 200 LOC), 14-Tier Schema Parity
Scope:
  - Enriches 25 foundational civic, guild, ecological, and martial entities:
    Ẹyẹ, Ẹranko, Ìlú, Odò, Òkè, Odi, Ojúbọ, Igbó, Ọjà, Àwọ̀, Gbẹ́nàgbẹ́nà,
    Amọ̀, Idẹ, Àgbẹ̀dẹ, Oníṣègùn, Apẹja, Ìwunṣọ, Ọdẹ, Ọkọ́, Oko,
    Àpáta_Shield, Ọfà, Idà, Ogun (Warfare & Military Tradition), Àmì_Ọlá.
  - Synchronizes nested `details` across all updated entities.
  - Updates `scripts/thin_entities_manifest.json` to reflect 616 remaining thin nodes.
=============================================================================
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"
DATA_PATH = REPO_ROOT / "scripts" / "batch_16_data.json"
MANIFEST_PATH = REPO_ROOT / "scripts" / "thin_entities_manifest.json"


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def apply_enrichments(corpus: List[Dict[str, Any]], enrichments: Dict[str, Dict[str, Any]]) -> int:
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

            # Keep nested details dictionary in sync
            if "details" in entity and isinstance(entity["details"], dict):
                for field, val in info.items():
                    entity["details"][field] = val
            elif "details" not in entity:
                entity["details"] = {field: val for field, val in info.items()}

            updated += 1

    return updated


def update_thin_manifest() -> int:
    """Updates thin manifest to reflect remaining 616 entities (indices 50 to 665)."""
    cmd = "git show 7607fc8e47e8c59954446629f2e4b6dbd936520b~1:scripts/thin_entities_manifest.json"
    raw = subprocess.check_output(cmd, shell=True).decode("utf-8")
    original_manifest = json.loads(raw)
    
    # Remaining entities after Batch 15 (0-24) and Batch 16 (25-49)
    remaining_manifest = original_manifest[50:]
    save_json(MANIFEST_PATH, remaining_manifest)
    return len(remaining_manifest)


def main():
    print("🚀 Starting Phase 4 Batch 16 Corpus Ingestion...")

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing Batch 16 data payload at {DATA_PATH}")

    enrichments = load_json(DATA_PATH)
    print(f"📦 Loaded {len(enrichments)} Batch 16 enrichment records.")

    api_corpus = load_json(API_CORPUS_PATH)
    web_corpus = load_json(WEB_CORPUS_PATH)

    print(f"📚 Loaded API Corpus: {len(api_corpus)} entities")
    print(f"🌐 Loaded Web Corpus: {len(web_corpus)} entities")

    updated_api = apply_enrichments(api_corpus, enrichments)
    updated_web = apply_enrichments(web_corpus, enrichments)

    print(f"✅ Updated API entities: {updated_api} / {len(enrichments)}")
    print(f"✅ Updated Web entities: {updated_web} / {len(enrichments)}")

    if updated_api != len(enrichments) or updated_web != len(enrichments):
        raise ValueError(
            f"Parity mismatch! Expected {len(enrichments)}, got API={updated_api}, Web={updated_web}"
        )

    # Save synchronized corpora
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("💾 Saved synchronized master corpora to API and Web paths.")

    # Update manifest tracking
    remaining_thin = update_thin_manifest()
    print(f"📉 Updated thin entities manifest: {remaining_thin} remaining thin nodes (reduced from 641 to {remaining_thin}).")

    # Verify 0-bit drift
    api_bytes = API_CORPUS_PATH.read_bytes()
    web_bytes = WEB_CORPUS_PATH.read_bytes()
    if api_bytes == web_bytes:
        print("🔒 0-bit checksum drift verified: API and Web corpora are 100% identical.")
    else:
        raise ValueError("Checksum drift detected between API and Web corpora!")


if __name__ == "__main__":
    main()
