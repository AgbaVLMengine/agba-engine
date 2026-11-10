#!/usr/bin/env python3
"""
Forensic Vector 3: Sub-Variant Integrity & Ghost Scanner.
Audits internal duplicates and unindexed ghost sub-variants lacking canonical nodes.
Invariant: Sub-100 LOC, Zero-hardcoding, Standard Library only.
"""
from pathlib import Path
import re
from typing import Any, Dict, List, Set


def load_knowledge_map_keys(knowledge_file: Path) -> Set[str]:
    """Extract curated keys from subVariantKnowledge.js without node execution."""
    if not knowledge_file.exists():
        return set()
    text = knowledge_file.read_text(encoding="utf-8")
    return set(re.findall(r'^\s*"([^"]+)":\s*\{', text, re.MULTILINE))


def audit_subvariants(
    target_entities: List[Dict[str, Any]],
    all_entities: List[Dict[str, Any]],
    knowledge_path: Path,
) -> Dict[str, Any]:
    """Scan sub-variants for internal list duplicates and ghost references."""
    canonical_titles = {e.get("title") for e in all_entities if e.get("title")}
    canonical_ids = {e.get("id") for e in all_entities if e.get("id")}
    canonical_aliases = set()
    for e in all_entities:
        for a in (e.get("aliases") or []):
            if a:
                canonical_aliases.add(str(a).strip())

    knowledge_keys = load_knowledge_map_keys(knowledge_path)
    valid_lookup = canonical_titles | canonical_ids | canonical_aliases | knowledge_keys

    ghosts = []
    internal_duplicates = []
    total_subvariants = 0

    for e in target_entities:
        svs = e.get("sub_variants")
        if not isinstance(svs, list) or not svs:
            continue

        parent_title = e.get("title") or e.get("id")
        seen_variants = set()

        for sv in svs:
            if not isinstance(sv, str):
                continue
            total_subvariants += 1
            sv_clean = sv.strip()
            sv_lower = sv_clean.lower()

            if sv_lower in seen_variants:
                internal_duplicates.append({
                    "parent": parent_title,
                    "parent_id": e.get("id"),
                    "duplicate_variant": sv_clean,
                })
            seen_variants.add(sv_lower)

            if sv_clean not in valid_lookup:
                ghosts.append({
                    "parent": parent_title,
                    "parent_id": e.get("id"),
                    "category": e.get("category"),
                    "ghost_variant": sv_clean,
                })

    svis = 100.0
    if total_subvariants > 0:
        svis = ((total_subvariants - len(ghosts)) / total_subvariants) * 100.0

    return {
        "total_subvariants": total_subvariants,
        "ghost_count": len(ghosts),
        "duplicate_count": len(internal_duplicates),
        "svis_score": round(svis, 2),
        "ghosts": ghosts,
        "internal_duplicates": internal_duplicates,
    }
