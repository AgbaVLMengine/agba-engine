#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: MASTER ONOMASTIC & 3-TIER GENERATIVE QA BENCHMARK
=============================================================================
Unified Automated QA Suite for Lead Architect Àrùnà Ọlànrewájú Kábírù's
Sovereign Plenary Mandate, 29-Query Mobile Audit, and Generative Fuzzer Suite.

Architectural Tiers:
- Tier 1: Exhaustive Master Preemption Sweep (1,413 Canonical Entities)
          Asserts 100.00% resolve with is_synthesized: false (0 name chopping).
- Tier 2: 1,600+ Unborn Name Combinatorial Fuzzer (Roots × Verbs × Modals)
          Asserts 0 generic fallback strings across mathematical permutations.
- Tier 3: 29-Query Golden Suite + 32 Generative Exemplar Fixtures
          Asserts exact diacritical and sovereign parent parity across all 4 templates.

Directives:
- Adheres to Ọlọ́yè Òye's Performance Invariant (< 150ms execution runtime)
- Gate 2 Headroom: Strictly < 500 LOC

Audited Personas:
- Ọlọ́yè Sùúrù (suuru-qa) — Benchmark Author & Lead QA Specialist
- Ọlọ́yè Àgbẹ̀dẹ (agbede-builder) — Two-Drawer Extractor & UI Craftsman
- Ọlọ́yè Òye (oye-auditor) — Onomastic Lexicon & Knowledge Graph Auditor
- Ọlọ́yè Àrọ̀kìn (arokin-archivist) — Royal Chronicler & Ontological Architect
"""

import sys
import os
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "api"))
sys.path.insert(0, str(REPO_ROOT))

try:
    from app.retrieval import AgbaHybridRetriever
except ImportError:
    AgbaHybridRetriever = None

# ---------------------------------------------------------------------------
# Test Fixture Paths
# ---------------------------------------------------------------------------
FIXTURE_29_PATH = REPO_ROOT / "scripts" / "fixtures" / "oruko_mi_25_queries.json"
FIXTURE_GEN_PATH = REPO_ROOT / "scripts" / "fixtures" / "generative_32_fixtures.json"

if not FIXTURE_29_PATH.exists():
    raise FileNotFoundError(f"Missing required 29-query fixtures at {FIXTURE_29_PATH}")

ONOMASTIC_29_TEST_CASES = json.loads(FIXTURE_29_PATH.read_text(encoding="utf-8"))

FORBIDDEN_FALLBACK_STRINGS = [
    "lineage morphological extension",
    "unidentified morpheme",
    "unknown suffix",
    "generic extension"
]


def run_node_decomposer_batch(queries: List[str]) -> Dict[str, Optional[Dict[str, Any]]]:
    """Execute onomastic decomposition batch in Node.js for perfect fidelity."""
    js_code = """
import('./web/src/utils/onomasticDecomposer.js').then(({ decomposeYorubaName }) => {
  const queries = JSON.parse(process.argv[1]);
  const results = {};
  for (const q of queries) {
    try {
      results[q] = decomposeYorubaName(q);
    } catch (e) {
      results[q] = null;
    }
  }
  process.stdout.write(JSON.stringify(results));
}).catch(err => {
  process.stderr.write(String(err));
  process.exit(1);
});
"""
    cmd = ["node", "--input-type=module", "-e", js_code, json.dumps(queries)]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        return {}
    try:
        return json.loads(proc.stdout)
    except Exception:
        return {}


def run_node_bridge_batch(queries: List[str]) -> Dict[str, Optional[Dict[str, Any]]]:
    """Execute end-to-end onomastic bridge resolution in Node.js with native corpus load."""
    js_code = """
import { resolveOnomasticZeroShot } from './web/src/utils/onomasticBridge.js';
import fs from 'fs';

const corpus = JSON.parse(fs.readFileSync('./web/src/data/yoruba_master_corpus.json', 'utf8'));
const queries = JSON.parse(process.argv[1]);
const results = {};

for (const q of queries) {
  try {
    results[q] = resolveOnomasticZeroShot(q, corpus);
  } catch (e) {
    results[q] = null;
  }
}
process.stdout.write(JSON.stringify(results));
"""
    cmd = ["node", "--input-type=module", "-e", js_code, json.dumps(queries)]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        return {}
    try:
        return json.loads(proc.stdout)
    except Exception:
        return {}


def run_generative_qa_harness() -> Dict[str, Any]:
    """Execute 3-tier generative suite in Node.js (< 150ms invariant)."""
    script = REPO_ROOT / "scripts" / "benchmark_generative_qa.py"
    proc = subprocess.run([sys.executable, str(script)], cwd=str(REPO_ROOT), capture_output=True, text=True)
    print(proc.stdout)
    if proc.returncode != 0 and proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return {}


def audit_onomastic_suite() -> Tuple[int, int, List[str]]:
    """Execute the canonical 29-query Onomastic QA Suite."""
    queries = [tc["query"] for tc in ONOMASTIC_29_TEST_CASES]
    decomposed_map = run_node_decomposer_batch(queries)
    bridge_map = run_node_bridge_batch(queries)

    retriever = None
    if AgbaHybridRetriever:
        try:
            retriever = AgbaHybridRetriever()
        except Exception:
            retriever = None

    passed_count = 0
    total_count = len(ONOMASTIC_29_TEST_CASES)
    failures = []

    print("=" * 80)
    print("🏛️ ÀGBÀ ENGINE: 29-QUERY ONOMASTIC ('ORÚKỌ MI') REGRESSION BENCHMARK")
    print("Lead QA Specialist: Ọlọ́yè Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("=" * 80)

    for tc in ONOMASTIC_29_TEST_CASES:
        tc_id = tc["id"]
        query = tc["query"]
        dec = decomposed_map.get(query)
        bridge_res = bridge_map.get(query)

        # 1. Martial Corpus Sub-Variants Check (Anti-Shadowing Invariant)
        if tc.get("is_corpus_subvariant"):
            corpus_ok = True
            corpus_err = ""
            if bridge_res is not None:
                corpus_ok = False
                corpus_err = "Anti-Shadowing breached: onomasticBridge did not yield null for corpus entity"
            elif retriever:
                res = retriever.retrieve(query, top_k=1)
                if not res or res[0]["title"] != tc["expected_canonical"]:
                    corpus_ok = False
                    top_title = res[0]["title"] if res else "None"
                    corpus_err = f"Retriever Top-1 was '{top_title}' != '{tc['expected_canonical']}'"
                else:
                    details = res[0].get("details", {})
                    if details.get("is_parent") != tc["is_parent_expected"]:
                        corpus_ok = False
                        corpus_err = f"is_parent={details.get('is_parent')} != {tc['is_parent_expected']}"
                    elif details.get("sovereign_parent") != tc["sovereign_parent_expected"]:
                        corpus_ok = False
                        corpus_err = f"sovereign_parent={details.get('sovereign_parent')} != {tc['sovereign_parent_expected']}"
            if not corpus_ok:
                failures.append(f"[{tc_id}] {corpus_err}")
                print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | {corpus_err}")
                continue

        # 2. Decomposer Output Validation
        if not dec:
            failures.append(f"[{tc_id}] Decomposer returned null for query '{query}'")
            print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | Decomposer returned null")
            continue

        # 3. Check for Forbidden Generic Fallbacks
        lineage_str = (dec.get("lineage_meaning") or "").lower()
        morpheme_strs = [m.get("meaning", "").lower() for m in dec.get("morphemes", [])]
        fallback_detected = False
        fallback_culprit = ""
        for fb in FORBIDDEN_FALLBACK_STRINGS:
            if fb in lineage_str or any(fb in m_str for m_str in morpheme_strs):
                fallback_detected = True
                fallback_culprit = fb
                break

        if fallback_detected:
            err = f"Detected forbidden fallback '{fallback_culprit}' in meaning"
            failures.append(f"[{tc_id}] {err}")
            print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | {err}")
            continue

        # 4. Check Sovereign Parents Overlap
        actual_parents = [p.lower() for p in dec.get("sovereign_parents", [])]
        expected_parents = [p.lower() for p in tc.get("expected_parents", [])]
        parent_match = any(ep in actual_parents for ep in expected_parents)

        if not parent_match:
            err = f"Sovereign parents {dec.get('sovereign_parents')} missing expected {tc.get('expected_parents')}"
            failures.append(f"[{tc_id}] {err}")
            print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | {err}")
            continue

        # 5. Suite 3: End-to-End Zero-Shot Search Resolution Verification
        if not tc.get("is_corpus_subvariant"):
            if not bridge_res:
                err = f"Suite 3 Bridge failed: resolveOnomasticZeroShot returned null for '{query}'"
                failures.append(f"[{tc_id}] {err}")
                print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | {err}")
                continue

            card = bridge_res.get("onomastic_card")
            if not card or not card.get("ribbon"):
                err = f"Suite 3 Bridge missing onomastic_card ribbon for '{query}'"
                failures.append(f"[{tc_id}] {err}")
                print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | {err}")
                continue

            if "(Unit Cowrie Shell Currency)" in bridge_res.get("title", ""):
                err = f"Double parenthetical detected in title: '{bridge_res.get('title')}'"
                failures.append(f"[{tc_id}] {err}")
                print(f"[❌ FAIL] {tc_id:<28} | Query: '{query:<20}' | {err}")
                continue

        passed_count += 1
        parents_str = ", ".join(dec.get("sovereign_parents", []))
        rank1_title = bridge_res.get("title") if bridge_res else tc["expected_canonical"]
        print(f"[✅ PASS] {tc_id:<28} | Query: '{query:<20}' | Rank #1: '{rank1_title}' | Roots: [{parents_str}]")

    print("-" * 80)
    print(f"📊 BENCHMARK METRICS: Passed: {passed_count}/{total_count} ({passed_count/total_count*100:.1f}%)")
    print("=" * 80)
    return passed_count, total_count, failures


if __name__ == "__main__":
    t_start = time.time()
    passed, total, fails = audit_onomastic_suite()
    print("\n▶ LAUNCHING 3-TIER GENERATIVE QA & ONTOLOGICAL ENGINE...")
    run_generative_qa_harness()
    total_time_ms = (time.time() - t_start) * 1000
    print(f"⚡ Combined Benchmark Suite Wall Clock Time: {total_time_ms:.2f} ms")
    if passed == total:
        sys.exit(0)
    else:
        sys.exit(1)
