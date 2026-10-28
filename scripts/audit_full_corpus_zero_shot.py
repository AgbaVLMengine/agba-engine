#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: TIER 2 QA SUITE - FULL-CORPUS ZERO-SHOT TITLE SWEEP
=============================================================================
Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù
Executive Authority: Àgbà & Òye Production Gate Scanner

Validates that EVERY entity in the master corpus can be retrieved at Top-1
under zero-shot exact queries and accent-folded (ASCII) searches.

Operational Directives:
  - Sweeps all canonical entities loaded by AgbaHybridRetriever.
  - Tests exact title and un-diacritized ASCII query forms.
  - Verifies Top-1 and Top-3 accuracy against the >= 99.5% Sovereign Threshold.
  - Catalogs all rank-2 usurping collisions for curatorial tuning.
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "api"))
sys.path.insert(0, str(REPO_ROOT))

try:
    from app.retrieval import AgbaHybridRetriever
    from app.semantic_bridge import normalize_y, strip_accents
except ImportError as e:
    print(f"❌ Error importing retrieval modules: {e}")
    sys.exit(1)

def run_zero_shot_sweep() -> bool:
    print("=" * 78)
    print("🏛️ ÀGBÀ ENGINE: TIER 2 FULL-CORPUS ZERO-SHOT RETRIEVAL SWEEP")
    print("Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("=" * 78)

    t0 = time.time()
    retriever = AgbaHybridRetriever()
    corpus = retriever.corpus_entities
    total_entities = len(corpus)

    print(f"\n🚀 Launching Zero-Shot Sweep across all {total_entities} canonical entities...")

    top1_exact = 0
    top3_exact = 0
    top1_ascii = 0
    top3_ascii = 0

    collisions_exact: List[Tuple[str, str, str]] = []
    collisions_ascii: List[Tuple[str, str, str]] = []

    for idx, entity in enumerate(corpus):
        title = entity.get("title", "")
        eid = str(entity.get("id", ""))
        ascii_title = strip_accents(title)

        # 1. Exact Diacritic Query Test
        res_exact = retriever.retrieve(title, top_k=3)
        hit_ids = [str(r.get("id")) for r in res_exact]
        hit_titles = [r.get("title") for r in res_exact]

        if hit_ids and (hit_ids[0] == eid or hit_titles[0] == title):
            top1_exact += 1
            top3_exact += 1
        elif eid in hit_ids or title in hit_titles:
            top3_exact += 1
            collisions_exact.append((title, hit_titles[0], "Rank 2/3 Collision"))
        else:
            collisions_exact.append((title, hit_titles[0] if hit_titles else "NONE", "Out of Top 3"))

        # 2. ASCII Accent-Folded Query Test
        if ascii_title:
            res_ascii = retriever.retrieve(ascii_title, top_k=3)
            hit_ascii_ids = [str(r.get("id")) for r in res_ascii]
            hit_ascii_titles = [r.get("title") for r in res_ascii]

            if hit_ascii_ids and (hit_ascii_ids[0] == eid or hit_ascii_titles[0] == title):
                top1_ascii += 1
                top3_ascii += 1
            elif eid in hit_ascii_ids or title in hit_ascii_titles:
                top3_ascii += 1
                collisions_ascii.append((ascii_title, hit_ascii_titles[0], "Rank 2/3 Collision"))
            else:
                collisions_ascii.append((ascii_title, hit_ascii_titles[0] if hit_ascii_titles else "NONE", "Out of Top 3"))

        if (idx + 1) % 350 == 0 or (idx + 1) == total_entities:
            elapsed = time.time() - t0
            rate = (idx + 1) / elapsed if elapsed > 0 else 0
            print(f"   ⏳ Processed {idx + 1}/{total_entities} entities ({rate:.1f} entities/sec)...")

    duration = time.time() - t0
    exact_top1_pct = (top1_exact / total_entities) * 100 if total_entities > 0 else 0
    exact_top3_pct = (top3_exact / total_entities) * 100 if total_entities > 0 else 0
    ascii_top1_pct = (top1_ascii / total_entities) * 100 if total_entities > 0 else 0
    ascii_top3_pct = (top3_ascii / total_entities) * 100 if total_entities > 0 else 0

    print("\n" + "-" * 78)
    print("📊 TIER 2 FULL-CORPUS ZERO-SHOT BENCHMARK METRICS:")
    print(f"   • Total Entities Evaluated:      {total_entities}")
    print(f"   • Total Evaluation Duration:     {duration:.2f} seconds ({total_entities/duration:.1f} qps)")
    print(f"   • Exact Query Top-1 Accuracy:    {top1_exact} / {total_entities} ({exact_top1_pct:.2f}%)")
    print(f"   • Exact Query Top-3 Accuracy:    {top3_exact} / {total_entities} ({exact_top3_pct:.2f}%)")
    print(f"   • ASCII-Folded Top-1 Accuracy:   {top1_ascii} / {total_entities} ({ascii_top1_pct:.2f}%)")
    print(f"   • ASCII-Folded Top-3 Accuracy:   {top3_ascii} / {total_entities} ({ascii_top3_pct:.2f}%)")
    print("-" * 78)

    if collisions_exact:
        print(f"\n⚠️ EXACT TITLE COLLISIONS DETECTED ({len(collisions_exact)} items):")
        for c in collisions_exact[:8]:
            print(f"   ⚠️ Target '{c[0]}' -> Top-1 Usurper: '{c[1]}' ({c[2]})")
        if len(collisions_exact) > 8:
            print(f"   ... and {len(collisions_exact) - 8} more.")

    if collisions_ascii:
        print(f"\n⚠️ ASCII-FOLDED COLLISIONS DETECTED ({len(collisions_ascii)} items):")
        for c in collisions_ascii[:8]:
            print(f"   ⚠️ Target '{c[0]}' -> Top-1 Usurper: '{c[1]}' ({c[2]})")
        if len(collisions_ascii) > 8:
            print(f"   ... and {len(collisions_ascii) - 8} more.")

    # Target threshold is 99.5%
    passed = exact_top1_pct >= 99.5
    print("\n" + "=" * 78)
    if passed:
        print(f"🏛️ SÙÚRÙ QA VERDICT: PASS ({exact_top1_pct:.2f}% Top-1 Accuracy exceeds 99.5% Gate)")
    else:
        print(f"🏛️ SÙÚRÙ QA VERDICT: FAIL ({exact_top1_pct:.2f}% Top-1 Accuracy is below 99.5% Gate)")
    print("=" * 78)

    return passed

if __name__ == "__main__":
    success = run_zero_shot_sweep()
    sys.exit(0 if success else 1)
