#!/usr/bin/env python3
"""
Forensic Vector 1: Duplicate & Triplicate Detection Engine.
Evaluates Jaccard similarity and noun head collisions within the same category.
Invariant: Sub-100 LOC, Zero-hardcoding, Standard Library only.
"""
import re
import unicodedata
from typing import Any, Dict, List


def strip_accents(s: str) -> str:
    """Normalize and strip tonal marks down to ASCII."""
    nfd = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn").lower().strip()


def tokenize(s: str) -> set:
    """Extract word tokens from stripped text."""
    return set(re.findall(r"\w+", strip_accents(s)))


def tokenize_ordered(s: str) -> List[str]:
    """Extract ordered sequence of word tokens."""
    return re.findall(r"\w+", strip_accents(s))


def jaccard_similarity(s1: str, s2: str) -> float:
    """Calculate token-level Jaccard similarity."""
    t1, t2 = tokenize(s1), tokenize(s2)
    return len(t1 & t2) / len(t1 | t2) if (t1 and t2) else 0.0


def is_amolu_inverted(e1: Dict[str, Any], e2: Dict[str, Any]) -> bool:
    """Filter out legitimate transposed composite Odù pairs with distinct IDs."""
    id1, id2 = e1.get("id") or "", e2.get("id") or ""
    if id1 != id2 and (id1.startswith("ODU_") or id2.startswith("ODU_")):
        t1, t2 = tokenize_ordered(e1.get("title") or ""), tokenize_ordered(e2.get("title") or "")
        if len(t1) == 2 and len(t2) == 2 and t1 == t2[::-1]:
            return True
    return False


def audit_duplicates(entities: List[Dict[str, Any]], threshold: float = 0.6) -> List[Dict[str, Any]]:
    """Scan entities within a category for lexical duplicates and alias shadows."""
    findings = []
    n = len(entities)
    for i in range(n):
        e1 = entities[i]
        t1, st1 = e1.get("title") or "", strip_accents(e1.get("title") or "")
        a1 = set(strip_accents(str(a)) for a in (e1.get("aliases") or []))

        for j in range(i + 1, n):
            e2 = entities[j]
            t2, st2 = e2.get("title") or "", strip_accents(e2.get("title") or "")
            a2 = set(strip_accents(str(a)) for a in (e2.get("aliases") or []))

            # Filter legitimate inverted composite chapters (Odù Ifá) & parent-child bonds
            if is_amolu_inverted(e1, e2) or e1.get("sovereign_parent") == t2 or e2.get("sovereign_parent") == t1:
                continue

            sim = jaccard_similarity(t1, t2)
            alias_cross = (st1 and st1 in a2) or (st2 and st2 in a1)
            shared_exact_alias = bool(a1 & a2 and len(st1) > 2 and len(st2) > 2)

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
                    "entity_a": t1, "id_a": e1.get("id"),
                    "entity_b": t2, "id_b": e2.get("id"),
                    "similarity": round(sim, 2), "reason": reason,
                })
    return findings
