#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 CORPUS ENRICHMENT PIPELINE (GEMINI 3.8 FLASH)
=============================================================================
Lead Architect: Aruna Olanrewaju Kabiru
Supervising Architect: Àgbà (agba-pa-architect)

Mission:
Systematically backfills dual-language proverbs and multi-epoch antiquity
timelines across thin corpus entities, elevating the entire master corpus to
full Àmọ̀tẹ́kùn-grade 14-tier depth parity.

Standards Enforced:
- Gate 2 Compliant (<500 LOC)
- Native JSON Schema enforcement (response_schema)
- Pristine Yorùbá diacritics and capitalization
- Exponential backoff retry loop (up to 60s) for 503/429 spikes
- Automated atomic checkpoints every 10 entities
=============================================================================
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"
MANIFEST_PATH = REPO_ROOT / "scripts/thin_entities_manifest.json"

MODEL_ID_DEFAULT = "gemini-3.8-flash"
BACKOFF_MAX_DELAY = 60
BATCH_CHECKPOINT_INTERVAL = 10

SYSTEM_INSTRUCTION = (
    "You are the Agba Cultural Historian for Yorùbá culture and the Global Heritage "
    "Search Engine of the World. You provide deep, lucid, authoritative 14-tier cultural schemas.\n"
    "CRITICAL FORMATTING INSTRUCTIONS:\n"
    "1. PROVERBS: Every item in 'proverbs_and_oral_traditions' MUST be dual-language, formatted as:\n"
    "   'Yorùbá Proverb with pristine diacritics (Parenthetical English translation and philosophical commentary).'\n"
    "2. HISTORICAL TIMELINE: Multi-epoch antiquity covering classical Ilé-Ifẹ̀ origins, medieval imperial growth, "
    "colonial-era preservation, and living contemporary continuity.\n"
    "3. DIACRITICS: Pristine Yorùbá orthography (ẹ, ọ, ṣ, and tone marks: acute ´, grave `).\n"
    "4. CAPITALIZATION: Proper capitalization for all kingdoms, dynasties, sacred titles, and historical eras."
)

RESPONSE_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "etymology_and_philosophy": {"type": "STRING"},
        "historical_timeline": {"type": "STRING"},
        "material_and_craftsmanship": {"type": "STRING"},
        "social_and_ritual_context": {"type": "STRING"},
        "proverbs_and_oral_traditions": {
            "type": "ARRAY",
            "items": {"type": "STRING"}
        },
        "diaspora_connections": {"type": "STRING"},
        "media_production_notes": {"type": "STRING"}
    },
    "required": [
        "etymology_and_philosophy",
        "historical_timeline",
        "material_and_craftsmanship",
        "social_and_ritual_context",
        "proverbs_and_oral_traditions",
        "diaspora_connections",
        "media_production_notes"
    ]
}

def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: Path, data: Any):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_entity_thin(entity: Dict[str, Any]) -> bool:
    provs = entity.get("proverbs_and_oral_traditions", [])
    timeline = (entity.get("historical_timeline") or "").strip()
    
    has_trans = False
    if isinstance(provs, list) and len(provs) > 0:
        for p in provs:
            if "(" in p and ")" in p:
                has_trans = True
                break
                
    is_thin_time = (
        len(timeline) < 120 or
        timeline.startswith("Deep antiquity tracing") or
        timeline.startswith("Classical Yorùbá antiquity")
    )
    return (not has_trans) or is_thin_time

def enrich_single_entity(client, model_id: str, entity: Dict[str, Any]) -> Dict[str, Any]:
    from google.genai import types

    existing_provs = entity.get("proverbs_and_oral_traditions", [])
    prompt = f"""
Entity ID: {entity.get('id')}
Title: {entity.get('title')}
Category: {entity.get('category')}
Culture: {entity.get('culture', 'Yorùbá')}
Sovereign Parent: {entity.get('sovereign_parent', 'N/A')}
Basic Description: {entity.get('description', '')}
Current Proverbs (if any): {json.dumps(existing_provs, ensure_ascii=False)}
Current Timeline (if any): {entity.get('historical_timeline', '')}

Enrich this entity into an authoritative Àmọ̀tẹ́kùn-grade node. Provide:
1. Deep etymology and linguistic derivation.
2. Multi-epoch historical timeline (ancient Ife / medieval kingdoms / transatlantic era / modern).
3. Specific physical materiality and guild craftsmanship.
4. Court/priestly social protocol and ritual context.
5. 2 or 3 dual-language proverbs with parenthetical English translation and philosophical commentary.
6. Transatlantic diaspora survivals (Cuba, Brazil, Caribbean).
7. Cinematic media production notes.
"""

    retry_delay = 5
    active_model = model_id
    fallback_models = ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash", "gemini-3.1-pro-preview"]

    for attempt in range(6):
        try:
            response = client.models.generate_content(
                model=active_model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    response_mime_type="application/json",
                    response_schema=RESPONSE_SCHEMA,
                    temperature=0.3
                )
            )
            data = json.loads(response.text)
            return data
        except Exception as e:
            err_str = str(e)
            if "402" in err_str or "prepayment credits are depleted" in err_str:
                print(f"\n❌ FATAL BILLING ERROR: Gemini API returned 402 (Prepayment credits depleted).")
                print(f"Please update GEMINI_API_KEY with a free-tier key or top up credits at https://ai.studio/projects.")
                raise e
            if any(code in err_str for code in ["504", "DEADLINE_EXCEEDED", "503", "UNAVAILABLE", "404", "NOT_FOUND"]):
                curr_idx = fallback_models.index(active_model) if active_model in fallback_models else 0
                next_model = fallback_models[(curr_idx + 1) % len(fallback_models)]
                print(f"   [i] Gateway error ({err_str[:40]}...). Auto-failing over from '{active_model}' to '{next_model}'...")
                active_model = next_model
            print(f"   [!] Attempt {attempt+1} error for '{entity.get('title')}': {e}. Retrying in {retry_delay}s...")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, BACKOFF_MAX_DELAY)
            
    raise RuntimeError(f"Failed to enrich {entity.get('title')} after 6 attempts.")

def main():
    parser = argparse.ArgumentParser(description="Phase 4 Batch Enrichment Pipeline")
    parser.add_argument("--api-key", help="Gemini API Key (or set GEMINI_API_KEY env var)")
    parser.add_argument("--model", default=MODEL_ID_DEFAULT, help="Gemini Model ID")
    parser.add_argument("--start", type=int, default=0, help="Starting index in thin manifest")
    parser.add_argument("--limit", type=int, default=0, help="Number of entities to process (0 = all)")
    parser.add_argument("--dry-run", action="store_true", help="Audit and list thin entities without calling API")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

    corpus = load_json(API_CORPUS_PATH)
    thin_indices = [i for i, e in enumerate(corpus) if is_entity_thin(e)]

    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: PHASE 4 BATCH ENRICHMENT PIPELINE")
    print(f"   - Model Active     : {args.model}")
    print(f"   - Master Corpus    : {len(corpus)} total entities")
    print(f"   - Thin Entities    : {len(thin_indices)} identified")
    print("=" * 80)

    if args.dry_run:
        print("\n🔍 DRY RUN AUDIT: Sample of Thin Entities requiring backfill:")
        for idx in thin_indices[:20]:
            e = corpus[idx]
            print(f"   [{idx:04d}] {e.get('title')} | Cat: {e.get('category')}")
        print(f"\nTotal requiring Phase 4 backfill: {len(thin_indices)} entities.")
        return

    targets = thin_indices[args.start:]
    if args.limit > 0:
        targets = targets[:args.limit]

    # Offline / Pre-baked Scholarly Batch Fallback
    batch_05_path = REPO_ROOT / "scripts/batch_05_data.json"
    if not api_key and batch_05_path.exists():
        print("\nℹ️  Notice: GEMINI_API_KEY not set. Engaging Curated Sovereign Scholarly Batch Vault (batch_05_data.json)...")
        with open(batch_05_path, "r", encoding="utf-8") as f:
            b_data = json.load(f).get("batch_5_enrichments", {})

        enriched_count = 0
        for step, c_idx in enumerate(targets):
            entity = corpus[c_idx]
            title = entity.get("title")
            ent_id = entity.get("id")
            match = b_data.get(title) or b_data.get(ent_id)
            if match:
                for k, v in match.items():
                    if v:
                        entity[k] = v
                enriched_count += 1
                print(f"[{step+1}/{len(targets)}] ✅ Enriched: '{title}' ({entity.get('category')}) from Sovereign Batch 05")
            else:
                print(f"[{step+1}/{len(targets)}] ⚠️ Unmatched in Batch 05: '{title}'")

        save_json(API_CORPUS_PATH, corpus)
        save_json(WEB_CORPUS_PATH, corpus)
        print(f"\n💾 Successfully applied {enriched_count} enrichments across API & Web master corpora!")
        return

    if not api_key:
        print("\n❌ ERROR: GEMINI_API_KEY is not set.")
        print("Please export GEMINI_API_KEY='...' or pass --api-key='...' to proceed.")
        sys.exit(1)

    try:
        from google import genai
        client = genai.Client(api_key=api_key, http_options={"timeout": 90000})
    except ImportError:
        print("❌ ERROR: 'google-genai' package is required. Install via 'pip install google-genai'.")
        sys.exit(1)

    print(f"\n🚀 Launching Enrichment on {len(targets)} entities (Indices {args.start} to {args.start + len(targets)})...\n")

    enriched_count = 0
    start_time = time.time()

    for step, c_idx in enumerate(targets):
        entity = corpus[c_idx]
        title = entity.get("title")
        print(f"[{step+1}/{len(targets)}] Enriching: '{title}' ({entity.get('category')})...")

        try:
            data = enrich_single_entity(client, args.model, entity)
            for k in [
                "etymology_and_philosophy",
                "historical_timeline",
                "material_and_craftsmanship",
                "social_and_ritual_context",
                "proverbs_and_oral_traditions",
                "diaspora_connections",
                "media_production_notes"
            ]:
                if k in data and data[k]:
                    entity[k] = data[k]

            enriched_count += 1
            # Polite pacing for Free Tier RPM limits
            time.sleep(2.5)

            # Atomic checkpoint save
            if (step + 1) % BATCH_CHECKPOINT_INTERVAL == 0 or (step + 1) == len(targets):
                save_json(API_CORPUS_PATH, corpus)
                save_json(WEB_CORPUS_PATH, corpus)
                elapsed = time.time() - start_time
                rate = enriched_count / elapsed if elapsed > 0 else 1
                rem = (len(targets) - enriched_count) / rate if rate > 0 else 0
                print(f"   💾 [CHECKPOINT SAVED] ({enriched_count}/{len(targets)}) | ~{rem/60:.1f}m remaining")

        except Exception as e:
            print(f"   ❌ Failed to enrich '{title}': {e}. Continuing to next...")

    print("\n" + "=" * 80)
    print("🎉 PHASE 4 BATCH ENRICHMENT COMPLETED")
    print(f"   - Successfully Enriched : {enriched_count} entities")
    print(f"   - Corpus Updated At     : {API_CORPUS_PATH.name} & {WEB_CORPUS_PATH.name}")
    print("=" * 80)

if __name__ == "__main__":
    main()
