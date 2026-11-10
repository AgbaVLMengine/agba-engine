#!/usr/bin/env python3
"""
Forensic Vector 1: Duplicate & Triplicate Detection Engine.
Evaluates Jaccard similarity and noun head collisions within the same category.
Invariant: Sub-100 LOC, Zero-hardcoding, Standard Library only.
"""
import re
import unicodedata
from typing import Any, Dict, List, Tuple


def strip_accents(s: str) -> str:
    """Normalize and strip tonal marks down to ASCII."""
    nfd = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn").lower().strip()


def tokenize(s: str) -> set:
    """Extract word tokens from stripped text."""
    return set(re.findall(r"\w+", strip_accents(s)))


def jaccard_similarity(s1: str, s2: str) -> float:
    """Calculate token-level Jaccard similarity."""
    t1, t2 = tokenize(s1), tokenize(s2)
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)


def audit_duplicates(
    entities: List[Dict[str, Any]], threshold: float = 0.6
) -> List[Dict[str, Any]]:
    """Scan entities within a category for lexical duplicates and alias shadows."""
    findings = []
    n = len(entities)
    for i in range(n):
        e1 = entities[i]
        t1 = e1.get("title") or ""
        st1 = strip_accents(t1)
        a1 = set(strip_accents(str(a)) for a in (e1.get("aliases") or []))

        for j in range(i + 1, n):
            e2 = entities[j]
            t2 = e2.get("title") or ""
            st2 = strip_accents(t2)
            a2 = set(strip_accents(str(a)) for a in (e2.get("aliases") or []))

            sim = jaccard_similarity(t1, t2)
            alias_cross = (st1 and st1 in a2) or (st2 and st2 in a1)
            shared_exact_alias = bool(a1 & a2 and len(st1) > 2 and len(st2) > 2)

            # Ignore generic parent-child relations if declared
            is_parent_child = (
                e1.get("sovereign_parent") == t2 or e2.get("sovereign_parent") == t1
            )
            if is_parent_child:
                continue

            reason = None
            if st1 == st2 and st1:
                reason = "Exact stem twin"
            elif sim >= threshold:
                reason = f"High Jaccard overlap ({sim:.2f})"
            elif alias_cross:
                reason = "Cross-alias title collision"
            elif shared_exact_alias:
                reason = f"Shared alias collision ({list(a1 & a2)[0]})"

            if reason:
                findings.append({
                    "entity_a": t1,
                    "id_a": e1.get("id"),
                    "entity_b": t2,
                    "id_b": e2.get("id"),
                    "similarity": round(sim, 2),
                    "reason": reason,
                })
    return findings
