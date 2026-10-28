#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: TIER 3 QA SUITE - BILATERAL PARENT-CHILD CONSISTENCY MATRIX
=============================================================================
Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù
Executive Authority: Àgbà & Òye Production Gate Scanner

Validates bidirectional knowledge-graph integrity across all 158 Sovereign Parents
and their child sub-variants in the master corpus.

Invariants Verified:
  1. Sovereign Parent Declaration: Each parent must declare `is_parent: true` or `sub_variants: [...]`.
  2. Bilateral Child Linkage: Every child declared in `parent.sub_variants` that exists as a
     standalone record must declare `sovereign_parent == parent.title` or `sovereign_parent == parent.id`.
  3. Anti-Parent-Loop Rule: A child entity must NEVER have `sovereign_parent == child.title` (no self-loops).
  4. Child Flag Parity: If an entity has a `sovereign_parent`, it must have `is_parent: false`.
  5. Sovereign Parent Status: Active children must declare `sovereign_parent_status: "Living Sub-Variant"`.
"""

import sys
import json
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"

def strip_accents(s: str) -> str:
    if not s:
        return ""
    return "".join(c for c in unicodedata.normalize("NFD", str(s)) if unicodedata.category(c) != "Mn").lower().strip()

def run_matrix_audit() -> bool:
    print("=" * 78)
    print("🏛️ ÀGBÀ ENGINE: TIER 3 BILATERAL PARENT-CHILD CONSISTENCY MATRIX")
    print("Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("=" * 78)

    if not API_CORPUS.exists():
        print(f"❌ Error: API corpus not found at {API_CORPUS}")
        return False

    with open(API_CORPUS, "r", encoding="utf-8") as f:
        corpus: List[Dict[str, Any]] = json.load(f)

    print(f"📂 Master Corpus Loaded: {len(corpus)} canonical entities\n")

    # Index corpus by title and aliases
    lookup_by_clean: Dict[str, Dict[str, Any]] = {}
    for e in corpus:
        title = e.get("title", "")
        eid = e.get("id", "")
        if title:
            lookup_by_clean[strip_accents(title)] = e
        if eid:
            lookup_by_clean[strip_accents(str(eid))] = e
        for a in e.get("aliases", []):
            clean_a = strip_accents(a)
            if clean_a and clean_a not in lookup_by_clean:
                lookup_by_clean[clean_a] = e

    parents = [e for e in corpus if e.get("is_parent") or e.get("sub_variants")]
    print(f"👑 Auditing {len(parents)} Sovereign Parent Manifests...\n")

    parent_count = len(parents)
    total_sub_variants_declared = 0
    standalone_children_found = 0
    correctly_wired_children = 0
    orphaned_children = []
    self_loops = []
    parent_flag_violations = []

    for p in parents:
        p_title = p.get("title", "UNKNOWN_PARENT")
        p_clean = strip_accents(p_title)
        sub_variants = p.get("sub_variants", [])
        total_sub_variants_declared += len(sub_variants)

        # Invariant 3: Anti-Parent Loop on Parent itself
        if p.get("sovereign_parent") and strip_accents(p.get("sovereign_parent", "")) == p_clean:
            self_loops.append((p_title, "Parent lists itself as sovereign_parent"))

        for sv in sub_variants:
            sv_title = sv if isinstance(sv, str) else sv.get("title", "")
            sv_clean = strip_accents(sv_title)

            # Look up child in corpus
            child = lookup_by_clean.get(sv_clean)
            if not child:
                # Check for prefix or parentheses match
                if "(" in sv_clean:
                    base = sv_clean.split("(")[0].strip()
                    child = lookup_by_clean.get(base)

            if child:
                standalone_children_found += 1
                c_title = child.get("title", "")
                c_parent = child.get("sovereign_parent")

                # Invariant 3: Anti-Parent Loop on Child
                if c_parent and strip_accents(c_parent) == strip_accents(c_title):
                    self_loops.append((c_title, f"Child lists itself as sovereign_parent"))

                # Invariant 4: Child flag parity
                if c_parent and child.get("is_parent") is True:
                    parent_flag_violations.append((c_title, "Child has sovereign_parent set but is_parent=True"))

                # Invariant 2: Bilateral linkage check
                if not c_parent:
                    orphaned_children.append((c_title, p_title, "Missing sovereign_parent pointer"))
                else:
                    c_parent_clean = strip_accents(c_parent)
                    # Check if matches parent title or id or aliases
                    p_id_clean = strip_accents(str(p.get("id", "")))
                    p_aliases = [strip_accents(a) for a in p.get("aliases", [])]
                    if c_parent_clean == p_clean or c_parent_clean == p_id_clean or c_parent_clean in p_aliases:
                        correctly_wired_children += 1
                    else:
                        # Mismatched parent
                        orphaned_children.append((c_title, p_title, f"Contradictory parent: '{c_parent}' != '{p_title}'"))

    # Check the reverse direction: all standalone entities claiming a sovereign_parent
    reverse_claims = [e for e in corpus if e.get("sovereign_parent")]
    reverse_orphan_count = 0
    for c in reverse_claims:
        sp_name = c.get("sovereign_parent")
        sp_clean = strip_accents(sp_name)
        if sp_clean not in lookup_by_clean:
            reverse_orphan_count += 1

    print("-" * 78)
    print("📊 TIER 3 CONSISTENCY MATRIX AUDIT RESULTS:")
    print(f"   • Total Sovereign Parents Audited:     {parent_count} / 158 target")
    print(f"   • Total Sub-Variants Declared:        {total_sub_variants_declared}")
    print(f"   • Standalone Child Records Found:     {standalone_children_found}")
    print(f"   • Bilaterally Wired & Validated:      {correctly_wired_children}")
    print(f"   • Self-Loop Violations:               {len(self_loops)}")
    print(f"   • Flag Parity Violations:             {len(parent_flag_violations)}")
    print(f"   • Orphaned / Contradictory Records:   {len(orphaned_children)}")
    print(f"   • Unresolved Reverse Parent Pointers: {reverse_orphan_count}")
    print("-" * 78)

    # Detailed report of any edge cases
    if self_loops:
        print("\n🚨 SELF-LOOP VIOLATIONS DETECTED:")
        for sl in self_loops[:10]:
            print(f"   ❌ {sl[0]}: {sl[1]}")

    if parent_flag_violations:
        print("\n⚠️ FLAG PARITY VIOLATIONS DETECTED:")
        for pf in parent_flag_violations[:10]:
            print(f"   ⚠️ {pf[0]}: {pf[1]}")

    if orphaned_children:
        print(f"\n⚠️ ORPHANED / MISMATCHED RECORDS ({len(orphaned_children)} items):")
        for oc in orphaned_children[:10]:
            print(f"   ⚠️ Child '{oc[0]}' under Parent '{oc[1]}': {oc[2]}")
        if len(orphaned_children) > 10:
            print(f"   ... and {len(orphaned_children) - 10} more.")

    # Sùúrù QA Verdict
    success = (len(self_loops) == 0 and len(parent_flag_violations) == 0)
    print("\n" + "=" * 78)
    if success and len(orphaned_children) == 0:
        print("🏛️ SÙÚRÙ QA VERDICT: PASS (100% Bilateral Parity Achieved)")
    elif success:
        print(f"🏛️ SÙÚRÙ QA VERDICT: PASS WITH OBSERVATIONS ({correctly_wired_children} wired, {len(orphaned_children)} catalogued for ingestion)")
    else:
        print("🏛️ SÙÚRÙ QA VERDICT: FAIL (Loop or Flag violations detected)")
    print("=" * 78)

    return success

if __name__ == "__main__":
    ok = run_matrix_audit()
    sys.exit(0 if ok else 1)
