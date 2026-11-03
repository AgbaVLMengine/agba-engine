#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: UNIVERSAL BATCH ENRICHMENT PIPELINE
=============================================================================
Reusable, single-source ingestion engine for Batch 17 through Batch 41.
Eliminates boilerplate script duplication across remaining 641 thin entities.
Gate 2 Compliant: Strictly < 150 LOC.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
API_CORPUS = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"
BATCHES_DIR = REPO_ROOT / "scripts" / "data" / "batches"


def load_corpus(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Corpus file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def save_corpus(path: Path, data: List[Dict[str, Any]]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def enrich_batch(batch_num: int, dry_run: bool = False) -> int:
    batch_file = BATCHES_DIR / f"batch_{batch_num:02d}_data.json"
    if not batch_file.exists():
        # Fallback to scripts/root batch_XX_data.json if present
        fallback = REPO_ROOT / "scripts" / f"batch_{batch_num:02d}_data.json"
        if fallback.exists():
            batch_file = fallback
        else:
            raise FileNotFoundError(f"Batch data payload not found at {batch_file}")

    batch_payload: List[Dict[str, Any]] = json.loads(batch_file.read_text(encoding="utf-8"))
    print(f"📦 Loaded Batch {batch_num} payload: {len(batch_payload)} entities.")

    api_data = load_corpus(API_CORPUS)
    web_data = load_corpus(WEB_CORPUS)

    # Build index map
    api_map = {e.get("id") or e.get("title"): i for i, e in enumerate(api_data)}
    web_map = {e.get("id") or e.get("title"): i for i, e in enumerate(web_data)}

    enriched_count = 0
    for entity in batch_payload:
        key = entity.get("id") or entity.get("title")
        if not key:
            continue

        if key in api_map:
            api_data[api_map[key]].update(entity)
        else:
            api_data.append(entity)

        if key in web_map:
            web_data[web_map[key]].update(entity)
        else:
            web_data.append(entity)

        enriched_count += 1

    if dry_run:
        print(f"🧪 [DRY-RUN] Verified enrichment of {enriched_count} entities. Corpora untouched.")
        return enriched_count

    save_corpus(API_CORPUS, api_data)
    save_corpus(WEB_CORPUS, web_data)
    print(f"✅ Successfully enriched {enriched_count} entities across Dual Corpora (Total: {len(api_data)}).")
    return enriched_count


def main():
    parser = argparse.ArgumentParser(description="Àgbà Universal Batch Enrichment Pipeline")
    parser.add_argument("--batch", type=int, required=True, help="Batch number to ingest (e.g. 17)")
    parser.add_argument("--dry-run", action="store_true", help="Validate payload without writing to disk")
    args = parser.parse_args()

    try:
        enrich_batch(args.batch, dry_run=args.dry_run)
    except Exception as e:
        print(f"❌ Ingestion failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
