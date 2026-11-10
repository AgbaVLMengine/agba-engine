#!/usr/bin/env python3
"""
Forensic Vector 2: Cross-Category Homograph Collision Sentinel.
Detects entities that share stripped ASCII stems across different categories.
Invariant: Sub-100 LOC, Zero-hardcoding, Standard Library only.
"""
import unicodedata
from collections import defaultdict
from typing import Any, Dict, List


def strip_accents(s: str) -> str:
    """Normalize and strip tonal marks down to baseline ASCII."""
    nfd = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn").lower().strip()


def build_stem_registry(
    all_entities: List[Dict[str, Any]]
) -> Dict[str, List[Dict[str, Any]]]:
    """Index all corpus entities by their stripped title and aliases."""
    stem_map = defaultdict(list)
    for e in all_entities:
        category = e.get("category") or "Uncategorized"
        title = e.get("title") or ""
        eid = e.get("id") or ""
        st = strip_accents(title)
        if st:
            stem_map[st].append({
                "title": title,
                "id": eid,
                "category": category,
                "type": "title",
            })
    return stem_map


def audit_homographs(
    target_entities: List[Dict[str, Any]],
    all_entities: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Scan target entities for tonal collisions with foreign categories."""
    stem_map = build_stem_registry(all_entities)
    findings = []
    seen_pairs = set()

    for e in target_entities:
        title = e.get("title") or ""
        cat = e.get("category") or ""
        eid = e.get("id") or ""
        st = strip_accents(title)
        if not st:
            continue

        matches = stem_map.get(st, [])
        for m in matches:
            if m["category"] != cat and m["id"] != eid:
                pair_key = tuple(sorted([eid, m["id"]]))
                if pair_key in seen_pairs:
                    continue
                seen_pairs.add(pair_key)

                findings.append({
                    "target_title": title,
                    "target_id": eid,
                    "target_category": cat,
                    "colliding_title": m["title"],
                    "colliding_id": m["id"],
                    "colliding_category": m["category"],
                    "stripped_stem": st,
                })
    return findings
