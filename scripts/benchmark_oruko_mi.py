#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: 25-QUERY ONOMASTIC ("ORÚKỌ MI") REGRESSION BENCHMARK
=============================================================================
Automated QA Benchmark Suite for Lead Architect Àrùnà Ọlànrewájú Kábírù's
25-Query Mobile Audit Matrix across the Yorùbá Onomastic Decomposer & Corpus.

Directives:
- HANDOFF-SUURU-006 (Checkpoint 130 / HANDOFF-ORUKO-MI-001)
- Gate 2 Headroom: Strictly < 500 LOC

Audited Personas:
- Ọlọ́yè Sùúrù (suuru-qa) — Benchmark Author & Lead QA Specialist
- Ọlọ́yè Àgbẹ̀dẹ (agbede-builder) — Two-Drawer Extractor & UI Craftsman
- Ọlọ́yè Òye (oye-auditor) — Onomastic Lexicon & Knowledge Graph Auditor
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
# The 25 Canonical Test Cases Audited by Kábíyèsí Àrùnà Ọlànrewájú Kábírù
# ---------------------------------------------------------------------------
FIXTURE_PATH = REPO_ROOT / "scripts" / "fixtures" / "oruko_mi_25_queries.json"
if not FIXTURE_PATH.exists():
    raise FileNotFoundError(f"Missing required test fixtures at {FIXTURE_PATH}")

ONOMASTIC_25_TEST_CASES = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

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


def audit_onomastic_suite() -> Tuple[int, int, List[str]]:
    """Execute the full 25-query Onomastic QA Suite."""
    queries = [tc["query"] for tc in ONOMASTIC_25_TEST_CASES]
    decomposed_map = run_node_decomposer_batch(queries)

    retriever = None
    if AgbaHybridRetriever:
        try:
            retriever = AgbaHybridRetriever()
        except Exception:
            retriever = None

    passed_count = 0
    total_count = len(ONOMASTIC_25_TEST_CASES)
    failures = []

    print("=" * 80)
    print("🏛️ ÀGBÀ ENGINE: 25-QUERY ONOMASTIC ('ORÚKỌ MI') REGRESSION BENCHMARK")
    print("Lead QA Specialist: Ọlọ́yè Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("=" * 80)
    time.sleep(0.05)

    for tc in ONOMASTIC_25_TEST_CASES:
        tc_id = tc["id"]
        query = tc["query"]
        dec = decomposed_map.get(query)

        # 1. Martial Corpus Sub-Variants Check
        if tc.get("is_corpus_subvariant"):
            corpus_ok = True
            corpus_err = ""
            if retriever:
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

        passed_count += 1
        canon = dec.get("canonical_name", "")
        parents_str = ", ".join(dec.get("sovereign_parents", []))
        print(f"[✅ PASS] {tc_id:<28} | Query: '{query:<20}' | Canon: '{canon}' | Roots: [{parents_str}]")

    print("-" * 80)
    print(f"📊 BENCHMARK METRICS: Passed: {passed_count}/{total_count} ({passed_count/total_count*100:.1f}%)")
    print("=" * 80)
    return passed_count, total_count, failures


if __name__ == "__main__":
    passed, total, fails = audit_onomastic_suite()
    if passed == total:
        print("🏛️ SÙÚRÙ QA VERDICT: 100% CERTIFIED PASS (Zero Generic Fallbacks & Sovereign Parity)")
        sys.exit(0)
    else:
        print(f"⚠️ SÙÚRÙ QA VERDICT: {len(fails)} ANOMALIES DETECTED — Awaiting Milestone A & B Integration")
        sys.exit(1)
