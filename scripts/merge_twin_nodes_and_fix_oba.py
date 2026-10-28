#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: TWIN NODES MERGE & ỌBA/ỌBÁ ALIAS PURIFICATION
Author: Àrọ̀kìn (arokin-archivist) & Àgbẹ̀dẹ (agbede-builder)
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
API_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"

TWIN_PAIRS = [
    ("Iyá Oba", "Ìyá-Ọba"),
    ("Ìlèkè Ọrùn", "Ìlẹ̀kẹ̀-Ọ̀rùn"),
    ("Ìlèkè Ọwọ́", "Ìlẹ̀kẹ̀-Ọwọ́"),
    ("Ẹgbẹ́ Àgbẹ̀", "Ẹgbẹ́-Àgbẹ̀"),
    ("Agbájọ Ogun", "Agbájó-Ogun"),
    ("Obe Ata", "Obẹ-Ata"),
    ("Ọmọ Odo", "Ọmọ-Odo"),
    ("Owó Ẹyọ", "Owó-Ẹ̀yọ̀"),
    ("Otun Balogun", "Otun-Balogun"),
    ("Ẹgbẹ́ Ọ̀dẹ", "Egbe-Ode"),
    ("Opa Ogun", "Opa-Ogun"),
    ("Oríki Idile", "Oriki-Idile"),
    ("Ilé Awo", "Ilé-Awo")
]


def process_corpus(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    initial_count = len(corpus)
    print(f"Loaded {path.name}: {initial_count} entities")

    # 1. Clean up Ọbá (River Orisha) vs Ọba (Monarch)
    for e in corpus:
        if e.get("id") == "Ọbá" or (e.get("title") == "Ọbá" and "river" in e.get("description", "").lower()):
            e["aliases"] = [
                "Orisha Oba",
                "Orisa Oba",
                "Oba River Deity",
                "Oba Nani",
                "Ayaba Sango",
                "Orisa of Oba River"
            ]
            print(f"  ✅ Purged polluted monarch aliases from Ọbá (River Orisha)")

        if e.get("id") == "Ọba" or (e.get("title") == "Ọba" and "monarch" in e.get("description", "").lower()):
            monarch_aliases = set(e.get("aliases", []))
            monarch_aliases.update([
                "alaafin", "alase", "awujale", "kabiyesi", "king", "kings",
                "monarch", "oba", "oba alade", "olubadan", "ooni",
                "paramount monarch", "paramount ruler"
            ])
            e["aliases"] = sorted(list(monarch_aliases))
            e["is_parent"] = True
            print(f"  ✅ Reinforced Ọba (Monarch) with complete sovereign parent metadata")

    # 2. Merge 13 twin pairs
    removed_ids = set()
    for legacy_title, canonical_title in TWIN_PAIRS:
        legacy_node = next((e for e in corpus if e.get("title") == legacy_title or e.get("id") == legacy_title), None)
        canonical_node = next((e for e in corpus if e.get("title") == canonical_title or e.get("id") == canonical_title), None)

        if legacy_node and canonical_node and legacy_node != canonical_node:
            # Transfer aliases
            c_aliases = set(canonical_node.get("aliases", []))
            c_aliases.add(legacy_title)
            c_aliases.update(legacy_node.get("aliases", []))
            canonical_node["aliases"] = sorted(list(c_aliases))

            removed_ids.add(legacy_node.get("id") or legacy_title)
            print(f"  🔀 Merged twin '{legacy_title}' ➔ canonical '{canonical_title}'")

    # Filter out removed legacy twins
    new_corpus = [e for e in corpus if (e.get("id") or e.get("title")) not in removed_ids]
    print(f"  Deduplicated: {initial_count} ➔ {len(new_corpus)} entities (-{len(removed_ids)})")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(new_corpus, f, ensure_ascii=False, indent=2)
    print(f"Saved {path.name} successfully.")
    return len(new_corpus)


if __name__ == "__main__":
    c1 = process_corpus(API_PATH)
    c2 = process_corpus(WEB_PATH)
    assert c1 == c2, f"Corpus mismatch: {c1} vs {c2}"
    print(f"\n✨ Corpus synchronization verified in lockstep at {c1} canonical entities.")
