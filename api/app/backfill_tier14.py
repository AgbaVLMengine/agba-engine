# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: 14-TIER CULTURAL PARITY BACKFILL ENGINE
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Model Engine: Gemini 3.8 Flash (Official REST Client)
# Mission: Elevate the 965 entities to 100% 14-Tier Schema Completeness
# ==============================================================================

import json
import os
import shutil
import time
import urllib.request
import urllib.error
import unicodedata
from pathlib import Path

# 1. Configuration & Paths
API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL_ID = "gemini-3.8-flash"
BASE_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_ID}:generateContent?key={API_KEY}"

CORPUS_PATH = Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_engine_backups/yoruba_corpus_1007_NORMALIZED.json")
BACKUP_PATH = Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_engine_backups/yoruba_corpus_1007_NORMALIZED.json.bak")

BATCH_SIZE = 10  # 10 entities per request for optimal token density & speed
REQUEST_PAUSE = 1.0  # Polite pause between batches

def clean_nfc(text: str) -> str:
    if not text:
        return ""
    return unicodedata.normalize("NFC", str(text).strip())

def make_backup():
    if not BACKUP_PATH.exists() and CORPUS_PATH.exists():
        print(f"📦 Creating initial master safety backup: {BACKUP_PATH.name}")
        shutil.copy2(CORPUS_PATH, BACKUP_PATH)

def call_gemini_batch(batch_items, max_retries=5):
    prompt_items = []
    for item in batch_items:
        prompt_items.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "category": item.get("category"),
            "description": item.get("description", "")[:250],
            "etymology_and_philosophy": item.get("etymology_and_philosophy", "")[:250],
            "material_and_craftsmanship": item.get("material_and_craftsmanship", "")[:200],
            "proverbs_and_oral_traditions": item.get("proverbs_and_oral_traditions", [])[:2],
            "media_production_notes": item.get("media_production_notes", "")[:200]
        })

    system_instruction = (
        "You are the Agba Cultural Historian for Yorùbá culture and the Global Heritage Search Engine of the World.\n"
        "Generate an authoritative, culturally deep, 2-sentence description of the 'social_and_ritual_context' for each entity.\n"
        "Ensure proper capitalization for all proper nouns, kingdoms, royal titles, and spiritual concepts.\n"
        "Ensure pristine Yorùbá diacritics (ẹ, ọ, ṣ, and tone marks: acute, grave).\n"
        "Output strictly valid JSON with the format: {\"results\": [{\"id\": \"...\", \"social_and_ritual_context\": \"...\"}]}"
    )

    prompt = f"{system_instruction}\n\nENTITIES TO ENRICH:\n{json.dumps(prompt_items, ensure_ascii=False, indent=2)}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": 0.25
        }
    }

    req = urllib.request.Request(
        BASE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    delay = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                parsed = json.loads(text)
                return parsed.get("results", [])
        except Exception as e:
            print(f"   [!] Attempt {attempt+1}/{max_retries} error: {e}. Retrying in {delay}s...")
            time.sleep(delay)
            delay = min(delay * 2, 45)
    
    raise RuntimeError(f"Failed batch after {max_retries} attempts.")

def run_tier14_backfill():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: 14-TIER CORPUS BACKFILL (GEMINI 3.8 FLASH)")
    print("   - Lead Architect : Aruna Olanrewaju Kabiru")
    print(f"   - Target File    : {CORPUS_PATH.name}")
    print(f"   - Model Active   : {MODEL_ID}")
    print("=" * 80)

    make_backup()

    with open(CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    # Convert to list if dict
    is_dict = isinstance(corpus, dict)
    items = list(corpus.values()) if is_dict else corpus

    # Find missing items
    missing_indices = [
        i for i, item in enumerate(items)
        if not item.get("social_and_ritual_context") or str(item.get("social_and_ritual_context")).strip() in ["", "None", "null", "N/A"]
    ]

    total_missing = len(missing_indices)
    print(f"📊 Corpus Status: {len(items)} Total Entities | {total_missing} Missing 'social_and_ritual_context'")

    if total_missing == 0:
        print("✨ 100% 14-Tier Completeness already achieved! No backfill needed.")
        return

    # Process in batches
    num_batches = (total_missing + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"🚀 Launching {num_batches} Batches ({BATCH_SIZE} items/batch)...\n")

    enriched_count = 0
    start_time = time.time()

    for batch_num in range(num_batches):
        batch_slice = missing_indices[batch_num * BATCH_SIZE : (batch_num + 1) * BATCH_SIZE]
        batch_items = [items[i] for i in batch_slice]
        batch_ids = [item.get("id") or item.get("title") for item in batch_items]

        print(f"[{batch_num + 1}/{num_batches}] Processing: {', '.join(batch_ids[:3])}{'...' if len(batch_ids)>3 else ''}")

        try:
            results = call_gemini_batch(batch_items)
            res_dict = {res.get("id"): res.get("social_and_ritual_context") for res in results if res.get("id")}

            for i in batch_slice:
                item_id = items[i].get("id")
                if item_id in res_dict:
                    items[i]["social_and_ritual_context"] = clean_nfc(res_dict[item_id])
                    enriched_count += 1
                else:
                    # Fallback match by title if id was modified in response
                    t = items[i].get("title")
                    matched = False
                    for r_id, r_ctx in res_dict.items():
                        if r_id and (r_id.lower() == str(item_id).lower() or r_id.lower() == str(t).lower()):
                            items[i]["social_and_ritual_context"] = clean_nfc(r_ctx)
                            enriched_count += 1
                            matched = True
                            break
                    if not matched and len(results) > 0:
                        # Index positional fallback if count matches
                        pos = batch_slice.index(i)
                        if pos < len(results):
                            items[i]["social_and_ritual_context"] = clean_nfc(results[pos].get("social_and_ritual_context", ""))
                            enriched_count += 1

            # Sync checkpoint directly to disk after each batch
            with open(CORPUS_PATH, "w", encoding="utf-8") as f:
                json.dump(corpus, f, ensure_ascii=False, indent=2)

            elapsed = time.time() - start_time
            rate = enriched_count / elapsed if elapsed > 0 else 1
            remaining = (total_missing - enriched_count) / rate if rate > 0 else 0
            print(f"   💾 Checkpoint Saved ({enriched_count}/{total_missing}) | ~{remaining/60:.1f}m remaining")

            time.sleep(REQUEST_PAUSE)

        except Exception as e:
            print(f"   ❌ Batch failed with error: {e}. Skipping to next, progress saved.")

    print("\n" + "=" * 80)
    print("🎉 14-TIER CULTURAL PARITY BACKFILL COMPLETED SUCCESSFULLY")
    print(f"   - Newly Enriched Entries : {enriched_count}")
    print(f"   - Total Master Entities  : {len(items)}")
    print(f"   - Master Location        : {CORPUS_PATH}")
    print("=" * 80)

if __name__ == "__main__":
    run_tier14_backfill()
