#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: ADVERSARIAL HUMAN FUZZING & STRESS HARNESS
=============================================================================
Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù
Executive Authority: Àgbà & Òye Production Gate Scanner

Simulates real-world chaotic human behavior and dialectal variation against
the hybrid retrieval engine:
  Suite 1: Common User Typos & Character Transpositions
  Suite 2: Missing Tone Marks & Underdots (Pure Unaccented ASCII)
  Suite 3: Rapid Double-Clicks & Repeated Token Stutter
  Suite 4: Dialectal Spelling Variations (Èkìtì, Ìjẹ̀bú, Ẹ̀gbá)
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "api"))
sys.path.insert(0, str(REPO_ROOT))

try:
    from app.retrieval import AgbaHybridRetriever
    from app.semantic_bridge import normalize_y, strip_accents
except ImportError as e:
    print(f"❌ Error importing retrieval modules: {e}")
    sys.exit(1)

# Adversarial test matrix covering all four mandated dimensions
ADVERSARIAL_TEST_SUITES = [
    # SUITE 1: Common User Typos & Transpositions
    {
        "suite": "1. USER TYPOS & TRANSPOSITIONS",
        "cases": [
            {"id": "TYPO_01_OGEB", "query": "ogeb oyeku", "expected_one_of": ["Ogbè Ọ̀yẹ̀kú", "Èjì Ogbè", "Ọ̀yẹ̀kú Méjì"], "desc": "Transposed letters in Odù title"},
            {"id": "TYPO_02_ORUNMIAL", "query": "orunmial", "expected_one_of": ["Ọ̀rúnmìlà", "Orunmila"], "desc": "Transposed ending letters in Ọ̀rúnmìlà"},
            {"id": "TYPO_03_SHANGOOO", "query": "shangooo", "expected_one_of": ["Ṣàngó", "Sango"], "desc": "Accidental repeated ending vowel"},
            {"id": "TYPO_04_OBATTALA", "query": "obattala", "expected_one_of": ["Ọbàtálá", "Obatala"], "desc": "Accidental double-consonant typo"},
            {"id": "TYPO_05_YEMOJAA", "query": "yemojaa", "expected_one_of": ["Yemọja", "Yemoja"], "desc": "Duplicate trailing vowel in Yemọja"},
            {"id": "TYPO_06_AGBEDEE", "query": "agbedee", "expected_one_of": ["Àgbẹ̀dẹ", "Agbede"], "desc": "Repeated vowel in blacksmith guild"},
        ],
    },
    # SUITE 2: Missing Tone Marks & Underdots (Pure ASCII)
    {
        "suite": "2. MISSING TONES & ACCENT-FOLDED ASCII",
        "cases": [
            {"id": "ASCII_01_OBATALA", "query": "obatala", "expected_one_of": ["Ọbàtálá", "Obatala"], "desc": "Pure unaccented Ọbàtálá"},
            {"id": "ASCII_02_ESHU", "query": "eshu", "expected_one_of": ["Èṣù", "Eshu", "Èṣù (Primordial Orisha of the Crossroads)"], "desc": "Colloquial 'sh' ASCII spelling of Èṣù"},
            {"id": "ASCII_03_OGBONI", "query": "ogboni", "expected_one_of": ["Ògbóni", "Ogboni"], "desc": "Pure unaccented Ògbóni"},
            {"id": "ASCII_04_GELEDE", "query": "gelede", "expected_one_of": ["Gẹ̀lẹ̀dẹ́", "Gelede"], "desc": "Triple unaccented vowel mask"},
            {"id": "ASCII_05_FILA_ABETI_AJA", "query": "fila abeti aja", "expected_one_of": ["Fìlà Abetí Ajá", "Fìlà Abeti Ajá"], "desc": "Multi-word cap query without underdots"},
            {"id": "ASCII_06_ILE_IFE", "query": "ile ife", "expected_one_of": ["Ilé-Ifẹ̀", "Ile-Ife"], "desc": "Ancient capital unaccented"},
            {"id": "ASCII_07_ARA_ORUN", "query": "ara orun", "expected_one_of": ["Ara Ọ̀run", "Ara Orun"], "desc": "Ancestral masquerade entity in ASCII"},
            {"id": "ASCII_08_ADO_EKITI", "query": "ado ekiti", "expected_one_of": ["Adó-Èkìtì (Ancestral Capital & Seat of the Ẹwí)", "Adó-Èkìtì"], "desc": "Regional capital in ASCII"},
        ],
    },
    # SUITE 3: Rapid Double-Clicks & Repeated Token Stutter
    {
        "suite": "3. RAPID DOUBLE-CLICKS & REPEATED STUTTER",
        "cases": [
            {"id": "STUTTER_01_IFA_IFA", "query": "ifa ifa", "expected_one_of": ["Ifá", "Ifa"], "desc": "Double token repetition for Ifá"},
            {"id": "STUTTER_02_OBA_OBA", "query": "oba oba", "expected_one_of": ["Ọba", "Oba"], "desc": "Double token repetition for Ọba"},
            {"id": "STUTTER_03_SANGO_SANGO", "query": "sango sango", "expected_one_of": ["Ṣàngó", "Sango"], "desc": "Double token repetition for Ṣàngó"},
            {"id": "STUTTER_04_EKO_EKO", "query": "eko eko", "expected_one_of": ["Èkó (Maritime Capital & Cultural Center)", "Èkó"], "desc": "Double token repetition for Èkó"},
            {"id": "STUTTER_05_WERE_WERE", "query": "were were", "expected_one_of": ["Were Music", "Were"], "desc": "Double token repetition for Were music"},
        ],
    },
    # SUITE 4: Dialectal Spelling Variations (Èkìtì, Ìjẹ̀bú, Ẹ̀gbá)
    {
        "suite": "4. DIALECTAL VARIATIONS (ÈKÌTÌ, ÌJẸ̀BÚ, Ẹ̀GBÁ)",
        "cases": [
            {"id": "DIALECT_01_EKITI_UFE", "query": "Ufe", "expected_one_of": ["Ilé-Ifẹ̀", "Ile-Ife"], "desc": "Èkìtì dialectal pronunciation of Ifẹ̀"},
            {"id": "DIALECT_02_EKITI_URUNMILA", "query": "Urunmila", "expected_one_of": ["Ọ̀rúnmìlà", "Orunmila"], "desc": "Èkìtì dialectal pronunciation of Ọ̀rúnmìlà"},
            {"id": "DIALECT_03_EKITI_EWI", "query": "Ewi Ado", "expected_one_of": ["Adó-Èkìtì (Ancestral Capital & Seat of the Ẹwí)", "Adó-Èkìtì"], "desc": "Monarch title query for Èkìtì capital"},
            {"id": "DIALECT_04_IJEBU_WERENSO", "query": "Werenṣo", "expected_one_of": ["Wèrénṣó", "Werenso"], "desc": "Ìjẹ̀bú dialectal vocalization of royal cap"},
            {"id": "DIALECT_05_IJEBU_AWUJALE", "query": "Awujale", "expected_one_of": ["Awùjalẹ̀", "Awujalẹ"], "desc": "Paramount monarch title of Ìjẹ̀búland"},
            {"id": "DIALECT_06_IJEBU_OBANTA", "query": "Obanta", "expected_one_of": ["Ìjẹ̀bú-Òde", "Awùjalẹ̀", "Awujalẹ"], "desc": "Founding dynasty ancestor of Ìjẹ̀bú"},
            {"id": "DIALECT_07_EGBA_LISABI", "query": "Lisabi", "expected_one_of": ["Abeokuta", "Àbẹ́òkúta", "Ìpínlẹ̀ Ògùn"], "desc": "Legendary liberator hero of Ẹ̀gbáland"},
            {"id": "DIALECT_08_EGBA_ALAKE", "query": "Alake", "expected_one_of": ["Abeokuta", "Àbẹ́òkúta", "Ọba"], "desc": "Paramount King of Ẹ̀gbáland"},
            {"id": "DIALECT_09_EGBA_OLUMO", "query": "Olumo", "expected_one_of": ["Àpáta Òlúmọ", "Àpáta", "Olumo Rock", "Abeokuta"], "desc": "Sacred sanctuary rock of Ẹ̀gbáland"},
        ],
    },
]

def run_fuzzing_harness() -> bool:
    print("=" * 78)
    print("🏛️ ÀGBÀ ENGINE: ADVERSARIAL HUMAN FUZZING & CHAOS STRESS HARNESS")
    print("Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("=" * 78)

    retriever = AgbaHybridRetriever()
    total_tested = 0
    total_top1 = 0
    total_top3 = 0

    suite_metrics: List[Dict[str, Any]] = []

    for suite_data in ADVERSARIAL_TEST_SUITES:
        suite_name = suite_data["suite"]
        cases = suite_data["cases"]
        print(f"\n⚡ Auditing Suite: {suite_name} ({len(cases)} cases)...")

        s_top1 = 0
        s_top3 = 0

        for c in cases:
            total_tested += 1
            cid = c["id"]
            query = c["query"]
            expected = c["expected_one_of"]
            desc = c.get("desc", "")

            res = retriever.retrieve(query, top_k=3)
            hit_titles = [r.get("title", "") for r in res]
            top_title = hit_titles[0] if hit_titles else "NONE"

            # Check matches
            clean_expected = [strip_accents(x) for x in expected]
            clean_top = strip_accents(top_title)
            clean_hits = [strip_accents(h) for h in hit_titles]

            top1_hit = any(clean_top == ce or clean_top.startswith(ce) for ce in clean_expected)
            top3_hit = any(any(ch == ce or ch.startswith(ce) for ce in clean_expected) for ch in clean_hits)

            if top1_hit:
                s_top1 += 1
                total_top1 += 1
                s_top3 += 1
                total_top3 += 1
                print(f"   [✅ TOP-1] {cid:<24} | Query: '{query:<14}' -> '{top_title}'")
            elif top3_hit:
                s_top3 += 1
                total_top3 += 1
                print(f"   [🟡 TOP-3] {cid:<24} | Query: '{query:<14}' -> Top-1: '{top_title}', Top-3 has target")
            else:
                print(f"   [❌ MISS ] {cid:<24} | Query: '{query:<14}' -> Top-1: '{top_title}' | Expected: {expected}")

        suite_metrics.append({
            "suite": suite_name,
            "total": len(cases),
            "top1": s_top1,
            "top3": s_top3,
        })

    print("\n" + "=" * 78)
    print("📊 ADVERSARIAL FUZZING BENCHMARK BREAKDOWN:")
    for sm in suite_metrics:
        t1_pct = (sm["top1"] / sm["total"]) * 100
        t3_pct = (sm["top3"] / sm["total"]) * 100
        print(f"   • {sm['suite']:<45} Top-1: {sm['top1']}/{sm['total']} ({t1_pct:5.1f}%) | Top-3: {sm['top3']}/{sm['total']} ({t3_pct:5.1f}%)")

    overall_t1_pct = (total_top1 / total_tested) * 100
    overall_t3_pct = (total_top3 / total_tested) * 100
    print("-" * 78)
    print(f"   🔥 TOTAL OVERALL RESILIENCE: Top-1: {total_top1}/{total_tested} ({overall_t1_pct:.1f}%) | Top-3: {total_top3}/{total_tested} ({overall_t3_pct:.1f}%)")
    print("=" * 78)

    # Sovereign Gate: >= 85% Top-3 resilience on adversarial chaotic input
    passed = overall_t3_pct >= 85.0
    if passed:
        print(f"🏛️ SÙÚRÙ QA VERDICT: PASS (Adversarial resilience {overall_t3_pct:.1f}% exceeds 85.0% Gate)")
    else:
        print(f"🏛️ SÙÚRÙ QA VERDICT: FAIL (Adversarial resilience {overall_t3_pct:.1f}% below 85.0% Gate)")
    print("=" * 78)

    return passed

if __name__ == "__main__":
    ok = run_fuzzing_harness()
    sys.exit(0 if ok else 1)
