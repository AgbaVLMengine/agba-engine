#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: CONSOLIDATE MONARCHY & BOTANICAL TWIN NODES
=============================================================================
Author: Sùúrù (suuru-qa) & Àrọ̀kìn (arokin-archivist)
Consolidates legacy twin nodes into their 14-Tier canonical records:
  1. Awujalẹ -> awujale_of_ijebu (Awùjalẹ̀ of Ìjẹ̀bú)
  2. Ewe Akọko -> ewe_akoko (Ewé Àkòko)
Purges monarch title aliases (ooni, alaafin, awujale) from parent Ọba to
guarantee zero parent-loop collapse when querying regional monarchs directly.
=============================================================================
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
API_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"

TWIN_MERGES = [
    ("Awujalẹ", "awujale_of_ijebu"),
    ("Ewe Akọko", "ewe_akoko")
]


def consolidate(corpus_path: Path):
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    initial_count = len(corpus)
    print(f"Loaded {corpus_path.name}: {initial_count} entities")

    by_id = {e.get("id"): e for e in corpus}

    for legacy_id, canonical_id in TWIN_MERGES:
        if legacy_id in by_id and canonical_id in by_id:
            legacy = by_id[legacy_id]
            canonical = by_id[canonical_id]

            # Merge aliases
            merged_aliases = set(canonical.get("aliases", []))
            merged_aliases.update(legacy.get("aliases", []))
            canonical["aliases"] = sorted(list(merged_aliases))

            # Remove legacy node
            corpus = [e for e in corpus if e.get("id") != legacy_id]
            print(f"  ✅ Merged legacy '{legacy_id}' into canonical '{canonical_id}' ('{canonical.get('title')}')")

    # Purge child monarch title collisions from parent Ọba so children always rank #1
    for e in corpus:
        if e.get("id") == "Ọba" or (e.get("title") == "Ọba" and e.get("category") == "Monarchy, Royal Regalia & Governance"):
            aliases = set(e.get("aliases", []))
            # Remove specific sovereign monarch titles that belong to child nodes
            for specific_title in ["ooni", "alaafin", "awujale", "ọọ̀ni", "aláàfin", "awùjalẹ̀"]:
                aliases.discard(specific_title)
            e["aliases"] = sorted(list(aliases))
            print(f"  ✅ Purged child title collisions from parent Ọba")

    with open(corpus_path, "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)

    print(f"Saved {corpus_path.name}: {len(corpus)} entities (reduced from {initial_count})\n")


def main():
    print("=" * 80)
    print("🏛️ CONSOLIDATING MONARCHY & BOTANICAL TWIN NODES")
    print("=" * 80)
    consolidate(API_PATH)
    consolidate(WEB_PATH)
    print("✅ Twin consolidation complete across dual corpora.")


if __name__ == "__main__":
    main()
