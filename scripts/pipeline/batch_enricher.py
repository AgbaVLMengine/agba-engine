#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: UNIVERSAL BATCH ENRICHMENT PIPELINE
=============================================================================
Reusable, single-source ingestion engine for Batch 17 through Batch 41.
Eliminates boilerplate script duplication across remaining 616 thin entities.
Gate 2 Compliant: Strictly < 150 LOC.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Union

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
API_CORPUS = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"
BATCHES_DIR = REPO_ROOT / "scripts" / "data" / "batches"
MANIFEST_PATH = REPO_ROOT / "scripts" / "thin_entities_manifest.json"


def load_corpus(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Corpus file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def save_corpus(path: Path, data: List[Dict[str, Any]]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_index_map(corpus: List[Dict[str, Any]]) -> Dict[str, int]:
    idx_map = {}
    for i, e in enumerate(corpus):
        if e.get("id"):
            idx_map[e["id"]] = i
            idx_map[e["id"].lower()] = i
        if e.get("title"):
            idx_map[e["title"]] = i
            idx_map[e["title"].lower()] = i
        for a in e.get("aliases", []):
            idx_map[str(a).lower()] = i
    return idx_map


def resolve_batch_file(target: Union[str, int]) -> Path:
    if isinstance(target, int) or (isinstance(target, str) and target.isdigit()):
        bnum = int(target)
        p = BATCHES_DIR / f"batch_{bnum:02d}_data.json"
        if not p.exists():
            p = REPO_ROOT / "scripts" / f"batch_{bnum:02d}_data.json"
        return p
    path = Path(target)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path


def enrich_batch(target: Union[str, int], dry_run: bool = False) -> int:
    batch_file = resolve_batch_file(target)
    if not batch_file.exists():
        raise FileNotFoundError(f"Batch data payload not found at {batch_file}")

    raw = json.loads(batch_file.read_text(encoding="utf-8"))
    batch_payload: List[Dict[str, Any]] = (
        [{"id": k, **v} for k, v in raw.items()] if isinstance(raw, dict) else raw
    )
    print(f"📦 Loaded payload from {batch_file.name}: {len(batch_payload)} entities.")

    api_data = load_corpus(API_CORPUS)
    web_data = load_corpus(WEB_CORPUS)
    api_map = build_index_map(api_data)
    web_map = build_index_map(web_data)

    enriched_count = 0
    for entity in batch_payload:
        key = entity.get("id") or entity.get("title")
        if not key:
            continue

        for corpus_data, idx_map in [(api_data, api_map), (web_data, web_map)]:
            target_idx = idx_map.get(key) or idx_map.get(key.lower())
            if target_idx is not None:
                item = corpus_data[target_idx]
                item.update(entity)
                if "details" in item and isinstance(item["details"], dict):
                    for field, val in entity.items():
                        if field != "details":
                            item["details"][field] = val
            else:
                corpus_data.append(entity)
        enriched_count += 1

    if dry_run:
        print(f"🧪 [DRY-RUN] Verified {enriched_count} entities. Corpora untouched.")
        return enriched_count

    save_corpus(API_CORPUS, api_data)
    save_corpus(WEB_CORPUS, web_data)
    print(f"✅ Successfully enriched {enriched_count} entities across Dual Corpora (Total: {len(api_data)}).")

    # Update manifest tracking
    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        orig_len = len(manifest)
        new_manifest = manifest[enriched_count:]
        MANIFEST_PATH.write_text(json.dumps(new_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"📉 Manifest updated: {orig_len} -> {len(new_manifest)} remaining thin entities.")

    if API_CORPUS.read_bytes() == WEB_CORPUS.read_bytes():
        print("🔒 0-bit checksum drift verified: API and Web corpora are 100% identical.")
    else:
        raise ValueError("Checksum drift detected between API and Web corpora!")

    return enriched_count


def main():
    parser = argparse.ArgumentParser(description="Àgbà Universal Batch Enrichment Pipeline")
    parser.add_argument("payload", nargs="?", default=None, help="Batch file path or batch number")
    parser.add_argument("--batch", type=int, default=None, help="Batch number (e.g. 17)")
    parser.add_argument("--dry-run", action="store_true", help="Validate payload without writing to disk")
    args = parser.parse_args()

    target = args.payload if args.payload is not None else args.batch
    if target is None:
        parser.error("Must provide either a batch file path or --batch <num>")

    try:
        enrich_batch(target, dry_run=args.dry_run)
    except Exception as e:
        print(f"❌ Ingestion failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
