#!/usr/bin/env python3
"""
Forensic Vector 4: Textual Richness, Scantiness & Boilerplate Auditor.
Audits depth invariants and flags leaked prompt metadata prefixes.
Invariant: Sub-100 LOC, Zero-hardcoding, Standard Library only.
"""
import re
from typing import Any, Dict, List

PROMPT_PREFIX_PATTERN = re.compile(
    r"\b(Parenthetical English translation|Philosophical commentary|"
    r"A specialized living variant within|Preserved through the generational lineage of|"
    r"Verbal predicate signifying):?",
    re.IGNORECASE,
)


def audit_richness(
    target_entities: List[Dict[str, Any]], min_depth: int = 600, min_prov: int = 3
) -> Dict[str, Any]:
    """Scan entities for thinness (<600 chars etym/desc), scanty proverbs (<3), and boilerplate."""
    thin_entities = []
    scanty_proverbs = []
    leaked_prompts = []

    for e in target_entities:
        title = e.get("title") or ""
        eid = e.get("id") or ""
        cat = e.get("category") or ""
        etym = e.get("etymology_and_philosophy") or ""
        desc = e.get("description") or ""
        provs = e.get("proverbs_and_oral_traditions") or []

        # Effective character depth check
        depth = max(len(etym), len(desc))
        if depth < min_depth:
            thin_entities.append({
                "title": title,
                "id": eid,
                "category": cat,
                "depth": depth,
                "min_required": min_depth,
            })

        # Proverb triad count check
        if len(provs) < min_prov:
            scanty_proverbs.append({
                "title": title,
                "id": eid,
                "category": cat,
                "count": len(provs),
                "min_required": min_prov,
            })

        # Scan text fields for leaked prompt prefixes
        fields_to_scan = [etym, desc] + [str(p) for p in provs]
        for fld in fields_to_scan:
            match = PROMPT_PREFIX_PATTERN.search(fld)
            if match:
                leaked_prompts.append({
                    "title": title,
                    "id": eid,
                    "category": cat,
                    "matched_pattern": match.group(0),
                    "snippet": fld[:100] + "...",
                })
                break

    return {
        "thin_count": len(thin_entities),
        "scanty_proverb_count": len(scanty_proverbs),
        "leaked_prompt_count": len(leaked_prompts),
        "thin_entities": thin_entities,
        "scanty_proverbs": scanty_proverbs,
        "leaked_prompts": leaked_prompts,
    }
