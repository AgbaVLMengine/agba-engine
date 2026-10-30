#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: SPRINT 004 RETRIEVAL & ANTI-PARENT-LOOP BENCHMARK
=============================================================================
Automated Regression Test Suite for Lead Architect Àrùnà Ọlànrewájú Kábírù's
14 Friction Queries, Sub-Variant Anti-Loop Invariants, and Category 17 Taxonomy.

Reference Audits:
- .agents/local-seeds/AGY__REPORT_OYE_AUDIT_004.md
- .agents/local-seeds/AGY__REPORT_OYE_TAXONOMY_AUDIT_005.md
- .agents/local-seeds/AGY__REPORT_SUURU_QA_004.md
"""

import sys
import os
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "api"))
sys.path.insert(0, str(REPO_ROOT))

try:
    from app.retrieval import AgbaHybridRetriever
    from app.semantic_bridge import normalize_y, strip_accents
except ImportError as e:
    print(f"Error importing retrieval modules: {e}")
    sys.exit(1)

# Compact, rigorous specification of the 24 test cases
BENCHMARK_TEST_CASES = [
    # 1. Were
    {"id": "Q01_WERE", "query": "Were", "expected_titles": ["Were", "Were / Were Music", "Were Music"], "expected_category": "Auditory Arts, Music, Drums & Chants", "is_parent_expected": True, "must_not_contain": ["Wèrè", "Madness"], "suite": "14_FRICTION_QUERIES"},
    # 2. Were Music
    {"id": "Q02_WERE_MUSIC", "query": "Were Music", "expected_titles": ["Were / Were Music", "Were Music", "Were"], "expected_category": "Auditory Arts, Music, Drums & Chants", "is_parent_expected": True, "must_not_contain": ["Wèrè"], "suite": "14_FRICTION_QUERIES"},
    # 3. Ifa
    {"id": "Q03_IFA", "query": "Ifa", "expected_titles": ["Ifá", "Ifa"], "expected_category": "Spiritual & Cosmological Matrix", "is_parent_expected": True, "must_not_contain": ["Ikin Ifá", "Ọpọ́n Ifá", "Agẹrẹ Ifá"], "suite": "14_FRICTION_QUERIES"},
    # 4A. Àrọ̀kọ̀ (Parent)
    {"id": "Q04A_AROKO_PARENT", "query": "Àrọ̀kọ̀", "expected_titles": ["Àrọ̀kọ̀", "Aroko"], "expected_category": "Oral Literature, Philosophy & Folklore", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 4B. Àrọ̀kọ̀ Ẹfà (Sub-variant Anti-Loop)
    {"id": "Q04B_AROKO_EFA", "query": "Àrọ̀kọ̀ Ẹfà", "expected_titles": ["Àrọ̀kọ̀ Ẹfà", "Aroko Efa"], "expected_sovereign_parent": "Àrọ̀kọ̀", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Àrọ̀kọ̀", "suite": "ANTI_PARENT_LOOP"},
    # 4C. Àrọ̀kọ̀ Ẹ̀jọ́ (Sub-variant Anti-Loop)
    {"id": "Q04C_AROKO_EJO", "query": "Àrọ̀kọ̀ Ẹ̀jọ́", "expected_titles": ["Àrọ̀kọ̀ Ẹ̀jọ́", "Aroko Ejo"], "expected_sovereign_parent": "Àrọ̀kọ̀", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Àrọ̀kọ̀", "suite": "ANTI_PARENT_LOOP"},
    # 5A. Oogun (Property / Inheritance)
    {"id": "Q05A_OOGUN_PROPERTY", "query": "Oogun", "expected_titles": ["Oogun", "Oogun (Property)", "Ogún Ìdílé"], "expected_category": "Social Structure, Kinship & Lineage", "is_parent_expected": True, "must_not_contain": ["Iṣẹ́ L’òògùn Ṣìọ̀rọ̀"], "suite": "14_FRICTION_QUERIES"},
    # 5B. Òògùn (Medicine)
    {"id": "Q05B_OOGUN_MEDICINE", "query": "Òògùn", "expected_titles": ["Òògùn", "Òògùn Ìbílẹ̀", "Oogun (Medicine)"], "expected_category": "Sacred Botany, Flora & Herbal Medicine", "is_parent_expected": True, "must_not_contain": ["Iṣẹ́ L’òògùn Ṣìọ̀rọ̀"], "suite": "14_FRICTION_QUERIES"},
    # 6A. Idà (Parent)
    {"id": "Q06A_IDA_PARENT", "query": "Idà", "expected_titles": ["Idà", "Ida"], "expected_category": "Military Traditions, Weaponry & Defense", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 6B. Idà Agẹmọ (Sub-variant Anti-Loop)
    {"id": "Q06B_IDA_AGEMO", "query": "Idà Agẹmọ", "expected_titles": ["Idà Agẹmọ", "Ida Agemo"], "expected_sovereign_parent": "Idà", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Idà", "suite": "ANTI_PARENT_LOOP"},
    # 7A. Ọ̀kọ̀ (Parent)
    {"id": "Q07A_OKO_SPEAR_PARENT", "query": "Ọ̀kọ̀", "expected_titles": ["Ọ̀kọ̀"], "expected_category": "Military Traditions, Weaponry & Defense", "is_parent_expected": True, "must_not_contain": ["Ọkọ́", "Ọkọ", "Oko"], "suite": "14_FRICTION_QUERIES"},
    # 7B. Ọ̀kọ̀ Ẹlẹ́ṣin (Sub-variant Anti-Loop)
    {"id": "Q07B_OKO_ELESIN", "query": "Ọ̀kọ̀ Ẹlẹ́ṣin", "expected_titles": ["Ọ̀kọ̀ Ẹlẹ́ṣin", "Oko Elesin"], "expected_sovereign_parent": "Ọ̀kọ̀", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Ọ̀kọ̀", "suite": "ANTI_PARENT_LOOP"},
    # 8A. Ọfà (Parent)
    {"id": "Q08A_OFA_PARENT", "query": "Ọfà", "expected_titles": ["Ọfà"], "expected_category": "Military Traditions, Weaponry & Defense", "is_parent_expected": True, "must_not_contain": ["Ofada", "Ìwọ̀fà"], "suite": "14_FRICTION_QUERIES"},
    # 8B. Ọfà Ọdẹ (Sub-variant Anti-Loop)
    {"id": "Q08B_OFA_ODE", "query": "Ọfà Ọdẹ", "expected_titles": ["Ọfà Ọdẹ", "Ofa Ode"], "expected_sovereign_parent": "Ọfà", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Ọfà", "suite": "ANTI_PARENT_LOOP"},
    # 9A. Àdá (Parent)
    {"id": "Q09A_ADA_PARENT", "query": "Àdá", "expected_titles": ["Àdá"], "expected_category": "Traditional Trades, Agriculture & Agrarian Guilds", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 9B. Àdá Ìbílẹ̀ (Sub-variant Anti-Loop)
    {"id": "Q09B_ADA_IBILE", "query": "Àdá Ìbílẹ̀", "expected_titles": ["Àdá Ìbílẹ̀", "Ada Ibile"], "expected_sovereign_parent": "Àdá", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Àdá", "suite": "ANTI_PARENT_LOOP"},
    # 10A. Epa (Masquerade Mask)
    {"id": "Q10A_EPA_MASK", "query": "Epa", "expected_titles": ["Epa"], "expected_category": "Ancestral Masquerades & Funerary Rites", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 10B. Ẹ̀pà (Groundnut)
    {"id": "Q10B_EPA_GROUNDNUT", "query": "Ẹ̀pà", "expected_titles": ["Ẹ̀pà"], "expected_category": "Culinary Arts & Indigenous Gastronomy", "is_parent_expected": True, "must_not_contain": ["Epa Door"], "suite": "14_FRICTION_QUERIES"},
    # 11. Àpáta (Sacred Topography vs Shield)
    {"id": "Q11_APATA_TOPOGRAPHY", "query": "Àpáta", "expected_titles": ["Àpáta"], "expected_category": "Topography, Natural Landscapes & Architecture", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 12A. Ẹja (Category 17 Parent)
    {"id": "Q12A_EJA_PARENT", "query": "Ẹja", "expected_titles": ["Ẹja"], "expected_category": "Indigenous Zoology, Sacred Fauna & Wildlife", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 12B. Ẹja Àrọ̀ (Sub-variant Anti-Loop)
    {"id": "Q12B_EJA_ARO", "query": "Ẹja Àrọ̀", "expected_titles": ["Ẹja Àrọ̀", "Eja Aro"], "expected_sovereign_parent": "Ẹja", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Ẹja", "suite": "ANTI_PARENT_LOOP"},
    # 13A. Ẹyẹ (Category 17 Parent)
    {"id": "Q13A_EYE_PARENT", "query": "Ẹyẹ", "expected_titles": ["Ẹyẹ"], "expected_category": "Indigenous Zoology, Sacred Fauna & Wildlife", "is_parent_expected": True, "suite": "14_FRICTION_QUERIES"},
    # 13B. Odídẹrẹ́ (Sub-variant Anti-Loop)
    {"id": "Q13B_ODIDERE", "query": "Odídẹrẹ́", "expected_titles": ["Odídẹrẹ́", "Odidere"], "expected_sovereign_parent": "Ẹyẹ", "is_parent_expected": False, "anti_loop_parent_to_avoid": "Ẹyẹ", "suite": "ANTI_PARENT_LOOP"},
    # 14. Apẹja (Bilateral Relatives)
    {"id": "Q14_APEJA_RELATIVES", "query": "Apẹja", "expected_titles": ["Apẹja"], "expected_category": "Traditional Trades, Agriculture & Agrarian Guilds", "is_parent_expected": True, "expected_relatives": ["Ẹja", "Ọkọ̀ Ojú Omi", "Odò Ọ̀ṣun", "Olókun"], "suite": "14_FRICTION_QUERIES"},
    # 15. Èkó vs Ẹ̀kọ Disambiguation
    {"id": "Q15_EKO_DISAMBIGUATION", "query": "Èkó", "expected_titles": ["Èkó (Maritime Capital & Cultural Center)", "Ìpínlẹ̀ Èkó"], "expected_category": "Civilization, History & Civic Heritage", "must_not_contain": ["Ẹ̀kọ"], "suite": "DISAMBIGUATION_SUITE"},
    # 16. Ọ̀fà vs Ọfà Disambiguation
    {"id": "Q16_OFA_DISAMBIGUATION", "query": "Ọ̀fà", "expected_titles": ["Ọ̀fà (Historical City & Ancient Kingdom)"], "expected_category": "Civilization, History & Civic Heritage", "must_not_contain": ["Ọfà Ọdẹ"], "suite": "DISAMBIGUATION_SUITE"},
    # 17. Kàbbà Settlement Ingestion
    {"id": "Q17_KABBA_OKUN", "query": "Kàbbà", "expected_titles": ["Kàbbà (Historic Okun Kingdom & City)"], "expected_category": "Civilization, History & Civic Heritage", "suite": "LIVING_VARIANTS_SUITE"},
    # 18. Adó-Èkìtì Settlement Ingestion
    {"id": "Q18_ADO_EKITI", "query": "Adó-Èkìtì", "expected_titles": ["Adó-Èkìtì (Ancestral Capital & Seat of the Ẹwí)", "Ìpínlẹ̀ Èkìtì"], "expected_category": "Civilization, History & Civic Heritage", "suite": "LIVING_VARIANTS_SUITE"},
    # 19. Ojú Odù (Anti-Loop / Dedicated Sovereign Record)
    {"id": "Q19_OJU_ODU", "query": "Oju Odu", "expected_titles": ["Ojú Odù Méjìdínlógún", "Oju Odu", "Ojú Odù"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Ifá", "suite": "ANTI_PARENT_LOOP"},
    # 20. Ojú Odù Méjìdínlógún (Dedicated Sovereign Record)
    {"id": "Q20_OJU_ODU_MEJIDINDLOGUN", "query": "Oju Odu Mejidindlogun", "expected_titles": ["Ojú Odù Méjìdínlógún", "Oju Odu Mejidindlogun"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Ifá", "suite": "ANTI_PARENT_LOOP"},
    # 21. Àmọ̀lù Odù (Dedicated Sovereign Record)
    {"id": "Q21_AMOLU_ODU", "query": "Amolu Odu", "expected_titles": ["Àmọ̀lù Odù", "Amolu Odu"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Ifá", "suite": "ANTI_PARENT_LOOP"},
    # 22. Ọ̀yẹ̀kú Ìwòrì (Batch 6 Composite Sovereign Chapter)
    {"id": "Q22_OYEKU_IWORI", "query": "Oyeku Iwori", "expected_titles": ["Ọ̀yẹ̀kú Ìwòrì", "Oyeku Iwori"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 23. Ọ̀yẹ̀kú Òdí (Batch 6 Composite Sovereign Chapter)
    {"id": "Q23_OYEKU_ODI", "query": "Oyeku Odi", "expected_titles": ["Ọ̀yẹ̀kú Òdí", "Oyeku Odi"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 24. Ìwòrì Ogbè (Batch 6 Composite Sovereign Chapter)
    {"id": "Q24_IWORI_OGBE", "query": "Iwori Ogbe", "expected_titles": ["Ìwòrì Ogbè", "Iwori Ogbe"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 25. Ìwòrì Ọ̀yẹ̀kú (Batch 6 Composite Sovereign Chapter)
    {"id": "Q25_IWORI_OYEKU", "query": "Iwori Oyeku", "expected_titles": ["Ìwòrì Ọ̀yẹ̀kú", "Iwori Oyeku"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 26. Òdí Ogbè (Batch 7 Composite Sovereign Chapter)
    {"id": "Q26_ODI_OGBE", "query": "Odi Ogbe", "expected_titles": ["Òdí Ogbè", "Odi Ogbe"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 27. Òdí Ọ̀yẹ̀kú (Batch 7 Composite Sovereign Chapter)
    {"id": "Q27_ODI_OYEKU", "query": "Odi Oyeku", "expected_titles": ["Òdí Ọ̀yẹ̀kú", "Odi Oyeku"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 28. Ìrosùn Ogbè (Batch 7 Composite Sovereign Chapter)
    {"id": "Q28_IROSUN_OGBE", "query": "Irosun Ogbe", "expected_titles": ["Ìrosùn Ogbè", "Irosun Ogbe"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 29. Ìrosùn Ọ̀yẹ̀kú (Batch 7 Composite Sovereign Chapter)
    {"id": "Q29_IROSUN_OYEKU", "query": "Irosun Oyeku", "expected_titles": ["Ìrosùn Ọ̀yẹ̀kú", "Irosun Oyeku"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 30. Ìwòrì Òtúá (Batch 7 Composite Sovereign Chapter)
    {"id": "Q30_IWORI_OTUA", "query": "Iwori Otua", "expected_titles": ["Ìwòrì Òtúá", "Iwori Otua"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 31. Ìrosùn Ọ̀kànràn (Batch 8 Composite Sovereign Chapter)
    {"id": "Q31_IROSUN_OKANRAN", "query": "Irosun Okanran", "expected_titles": ["Ìrosùn Ọ̀kànràn", "Irosun Okanran"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 32. Ọ̀wọ́nrín Ogbè (Batch 8 Composite Sovereign Chapter)
    {"id": "Q32_OWONRIN_OGBE", "query": "Owónrín Ogbe", "expected_titles": ["Ọ̀wọ́nrín Ogbè", "Owónrín Ogbe", "Owonrin Ogbe"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 33. Ọ̀wọ́nrín Ọ̀yẹ̀kú (Batch 8 Composite Sovereign Chapter)
    {"id": "Q33_OWONRIN_OYEKU", "query": "Owónrín Oyeku", "expected_titles": ["Ọ̀wọ́nrín Ọ̀yẹ̀kú", "Owónrín Oyeku", "Owonrin Oyeku"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # 34. Ọ̀bàrà Ogbè (Batch 8 Composite Sovereign Chapter)
    {"id": "Q34_OBARA_OGBE", "query": "Obàrà Ogbe", "expected_titles": ["Ọ̀bàrà Ogbè", "Obàrà Ogbe", "Obara Ogbe"], "expected_category": "Spiritual & Cosmological Matrix", "anti_loop_parent_to_avoid": "Àmọ̀lù Odù", "suite": "ANTI_PARENT_LOOP"},
    # --- Universal Constellations Suite (HANDOFF-SUURU-005) ---
    # 35. Baṣọ̀run (Governance Parent)
    {"id": "Q35_BASORUN_PARENT", "query": "Baṣọ̀run", "expected_titles": ["Baṣọ̀run (Prime Minister / Supreme Commander of Oyo)", "Baṣọ̀run", "Basorun"], "expected_category": "Monarchy, Royal Regalia & Governance", "suite": "GOVERNANCE_CONSTELLATION"},
    # 36. Basọ̀run Gáà (Child Anti-Loop)
    {"id": "Q36_BASORUN_GAA", "query": "Basorun Gaa", "expected_titles": ["Basọ̀run Gáà", "Basorun Gaa"], "expected_category": "Monarchy, Royal Regalia & Governance", "anti_loop_parent_to_avoid": "Baṣọ̀run", "suite": "ANTI_PARENT_LOOP"},
    # 37. Basọ̀run Olúyọ̀lé (Child Anti-Loop)
    {"id": "Q37_BASORUN_OLUYOLE", "query": "Basorun Oluyole", "expected_titles": ["Basọ̀run Olúyọ̀lé", "Basorun Oluyole"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Baṣọ̀run", "anti_loop_parent_to_avoid": "Baṣọ̀run", "suite": "ANTI_PARENT_LOOP"},
    # 38. Ọ̀yọ́ Mèsì (Governance Constellation / Anti-Loop)
    {"id": "Q38_OYO_MESI", "query": "Oyo Mesi", "expected_titles": ["Ọ̀yọ́ Mèsì", "Oyo Mesi"], "expected_category": "Monarchy, Royal Regalia & Governance", "anti_loop_parent_to_avoid": "Baṣọ̀run", "suite": "ANTI_PARENT_LOOP"},
    # 39. Igbá Ìwà (Child Anti-Loop)
    {"id": "Q39_IGBA_IWA", "query": "Igba Iwa", "expected_titles": ["Igbá Ìwà (The Sacred Calabash of Destiny & Abdication)", "Igbá Ìwà", "Igba Iwa"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Baṣọ̀run", "anti_loop_parent_to_avoid": "Baṣọ̀run", "suite": "ANTI_PARENT_LOOP"},
    # 40. Adé (Regalia Parent)
    {"id": "Q40_ADE_PARENT", "query": "Ade", "expected_titles": ["Adé", "Ade"], "expected_category": "Monarchy, Royal Regalia & Governance", "is_parent_expected": True, "suite": "REGALIA_CONSTELLATION"},
    # 41. Adé Ààrẹ (Child Anti-Loop)
    {"id": "Q41_ADE_AARE", "query": "Ade Aare", "expected_titles": ["Adé Ààrẹ", "Ade Aare"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Adé", "anti_loop_parent_to_avoid": "Adé", "suite": "ANTI_PARENT_LOOP"},
    # 42. Adé Ọ̀kín (Child Anti-Loop)
    {"id": "Q42_ADE_OKIN", "query": "Ade Okin", "expected_titles": ["Adé Ọ̀kín (The Beaded Crown of the Sacred Peacock)", "Adé Ọ̀kín", "Ade Okin"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Adé", "anti_loop_parent_to_avoid": "Adé", "suite": "ANTI_PARENT_LOOP"},
    # 43. Ògún (Weaponry & Cosmic Parent)
    {"id": "Q43_OGUN_PARENT", "query": "Ogun", "expected_titles": ["Ògún", "Ogun"], "expected_category": "Spiritual & Cosmological Matrix", "is_parent_expected": True, "suite": "WEAPONRY_CONSTELLATION"},
    # 44. Dùndún (Auditory Parent)
    {"id": "Q44_DUNDUN_PARENT", "query": "Dundun", "expected_titles": ["Dùndún", "Dundun"], "expected_category": "Auditory Arts, Music, Drums & Chants", "is_parent_expected": True, "suite": "AUDITORY_CONSTELLATION"},
    # 45. Gángan (Auditory Child Anti-Loop)
    {"id": "Q45_GANGAN", "query": "Gangan", "expected_titles": ["Gángan", "Gangan"], "expected_category": "Auditory Arts, Music, Drums & Chants", "expected_sovereign_parent": "Dùndún", "anti_loop_parent_to_avoid": "Dùndún", "suite": "ANTI_PARENT_LOOP"},
    # 46. Ìyáàlù (Auditory Child Anti-Loop)
    {"id": "Q46_IYAALU", "query": "Iyaalu", "expected_titles": ["Ìyáàlù (Lead Mother Drum of the Dùndún Ensemble)", "Ìyáàlù", "Iyaalu", "Ìyáàlù Dùndún"], "expected_category": "Auditory Arts, Music, Drums & Chants", "expected_sovereign_parent": "Dùndún", "anti_loop_parent_to_avoid": "Dùndún", "suite": "ANTI_PARENT_LOOP"},
    # --- Monarchy & Royal Architecture Constellation Suite (HANDOFF-SUURU-007) ---
    # 47. Ọọ̀ni of Ifẹ̀ (Regional Sovereign Monarch Child)
    {"id": "Q47_OONI_OF_IFE", "query": "Ooni of Ife", "expected_titles": ["Ọọ̀ni of Ifẹ̀", "Ooni of Ife"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Ọba", "anti_loop_parent_to_avoid": "Ọba", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 48. Aláàfin of Ọ̀yọ́ (Regional Sovereign Monarch Child)
    {"id": "Q48_ALAAFIN_OF_OYO", "query": "Alaafin of Oyo", "expected_titles": ["Aláàfin of Ọ̀yọ́", "Alaafin of Oyo"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Ọba", "anti_loop_parent_to_avoid": "Ọba", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 49A. Awùjalẹ̀ of Ìjẹ̀bú (Direct Regional Monarch Query)
    {"id": "Q49A_AWUJALE", "query": "Awujale", "expected_titles": ["Awùjalẹ̀ of Ìjẹ̀bú", "Awùjalẹ̀", "Awujale"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Ọba", "anti_loop_parent_to_avoid": "Ọba", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 49B. Awùjalẹ̀ of Ìjẹ̀bú (Full Kingdom Query)
    {"id": "Q49B_AWUJALE_OF_IJEBU", "query": "Awujale of Ijebu", "expected_titles": ["Awùjalẹ̀ of Ìjẹ̀bú", "Awujale of Ijebu"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Ọba", "anti_loop_parent_to_avoid": "Ọba", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 50. Ààfin Ọọ̀ni (Sacred Palace Architecture Child)
    {"id": "Q50_AAFIN_OONI", "query": "Aafin Ooni", "expected_titles": ["Ààfin Ọọ̀ni (Ilé-Ifẹ̀)", "Ààfin Ọọ̀ni", "Aafin Ooni"], "expected_category": "Monarchy, Royal Regalia & Governance", "expected_sovereign_parent": "Ààfin", "anti_loop_parent_to_avoid": "Ààfin", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 51. Kòbì Ààfin (Sacred Royal Gabled Porch Architecture Child)
    {"id": "Q51_KOBI_AAFIN", "query": "Kobi Aafin", "expected_titles": ["Kòbì Ààfin", "Kobi Aafin"], "expected_category": "Topography, Natural Landscapes & Architecture", "expected_sovereign_parent": "Ààfin", "anti_loop_parent_to_avoid": "Ààfin", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 52A. Sányán (Royal Master Weave Child)
    {"id": "Q52A_SANYAN", "query": "Sanyan", "expected_titles": ["Sányán", "Sanyan"], "expected_category": "Attire, Textiles & Personal Adornment", "expected_sovereign_parent": "Aṣọ Òkè", "anti_loop_parent_to_avoid": "Aṣọ Òkè", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 52B. Àlàárì (Royal Master Weave Child)
    {"id": "Q52B_ALAARI", "query": "Alaari", "expected_titles": ["Àlàárì", "Alaari"], "expected_category": "Attire, Textiles & Personal Adornment", "expected_sovereign_parent": "Aṣọ Òkè", "anti_loop_parent_to_avoid": "Aṣọ Òkè", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
    # 53. Ewé Àkòko (Sacred Coronation Leaf Child)
    {"id": "Q53_EWE_AKOKO", "query": "Ewe Akoko", "expected_titles": ["Ewé Àkòko", "Ewe Akoko"], "expected_category": "Sacred Botany, Flora & Herbal Medicine", "is_parent_expected": False, "suite": "ANTI_PARENT_LOOP"},
]

CATEGORY_17_FAUNA_CASES = [
    "Ẹja", "Ẹyẹ", "Ẹranko", "Ìjàpá", "Àkùkọ", "Ẹsin", "Àgbọ̀nrin",
    "Ẹ̀kùn", "Àmọ̀tẹ́kùn", "Aáyá", "Egbin", "Àwòko", "Ẹ̀fọ̀n", "Kiníun",
    "Àdàbà", "Ẹran-Ọ̀sọ́", "Àgbàǹgbá", "Ẹ̀yọ̀-Ẹran"
]


def evaluate_retrieval(retriever: AgbaHybridRetriever, tc: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
    query = tc["query"]
    results = retriever.retrieve(query, top_k=5)
    diag = {"id": tc["id"], "query": query, "suite": tc.get("suite", "GENERAL"), "top_hits": [], "passed": False, "reasons": []}
    if not results:
        diag["reasons"].append(f"No results returned for query '{query}'.")
        return False, diag

    for idx, hit in enumerate(results[:3]):
        diag["top_hits"].append({
            "rank": idx + 1, "title": hit.get("title"), "category": hit.get("category"),
            "fusion_score": hit.get("fusion_score"),
            "is_parent": hit.get("details", {}).get("is_parent", False),
            "sovereign_parent": hit.get("details", {}).get("sovereign_parent", "")
        })

    top1 = results[0]
    top1_title, top1_cat = top1.get("title", ""), top1.get("category", "")
    top1_details = top1.get("details", {})
    top1_is_parent = top1_details.get("is_parent", False)
    top1_sovereign_parent = top1_details.get("sovereign_parent", "")

    expected_titles = [normalize_y(t) for t in tc.get("expected_titles", [])]
    expected_titles_stripped = [strip_accents(t) for t in tc.get("expected_titles", [])]
    norm_top1 = normalize_y(top1_title)
    stripped_top1 = strip_accents(top1_title)

    title_matched = (
        norm_top1 in expected_titles or stripped_top1 in expected_titles_stripped or
        any(et in norm_top1 for et in expected_titles)
    )
    if not title_matched:
        diag["reasons"].append(f"Rank #1 title '{top1_title}' did not match expected: {tc.get('expected_titles')}.")

    anti_loop = tc.get("anti_loop_parent_to_avoid")
    if anti_loop and strip_accents(top1_title) == strip_accents(anti_loop):
        diag["reasons"].append(f"PARENT-LOOP DETECTED: Query for child '{query}' collapsed back to parent '{top1_title}'!")
        title_matched = False

    expected_sov_parent = tc.get("expected_sovereign_parent")
    if expected_sov_parent and strip_accents(top1_sovereign_parent) != strip_accents(expected_sov_parent):
        if strip_accents(expected_sov_parent) not in stripped_top1:
            diag["reasons"].append(f"Child sovereign_parent '{top1_sovereign_parent}' != expected '{expected_sov_parent}'.")

    if tc.get("is_parent_expected") is not None and top1_is_parent != tc.get("is_parent_expected"):
        diag["reasons"].append(f"Entity is_parent flag was {top1_is_parent}, expected {tc.get('is_parent_expected')}.")

    if tc.get("expected_category") and top1_cat != tc.get("expected_category"):
        diag["reasons"].append(f"Rank #1 category '{top1_cat}' != expected '{tc.get('expected_category')}'.")

    for bad_tok in tc.get("must_not_contain", []):
        norm_bad = normalize_y(bad_tok)
        if norm_top1 == norm_bad or norm_bad in norm_top1.split():
            diag["reasons"].append(f"Rank #1 title '{top1_title}' matches forbidden homograph '{bad_tok}'.")
        elif len(bad_tok) > 4 and strip_accents(bad_tok) in stripped_top1:
            diag["reasons"].append(f"Rank #1 title '{top1_title}' contains forbidden substring '{bad_tok}'.")

    if tc.get("expected_relatives"):
        rel_entities = top1_details.get("related_entities", [])
        rel_stripped = [strip_accents(r) for r in rel_entities]
        missing = [er for er in tc["expected_relatives"] if not any(strip_accents(er) in r for r in rel_stripped)]
        if missing:
            diag["reasons"].append(f"Missing expected bilateral relatives: {missing}. Present: {rel_entities}")

    diag["passed"] = (len(diag["reasons"]) == 0)
    return diag["passed"], diag


def evaluate_category_17_taxonomy(retriever: AgbaHybridRetriever) -> Dict[str, Any]:
    CAT_17 = "Indigenous Zoology, Sacred Fauna & Wildlife"
    title_to_cat = {e.get("title"): e.get("category") for e in retriever.corpus_entities}
    results, passed_count, total = {}, 0, len(CATEGORY_17_FAUNA_CASES)

    for fauna in CATEGORY_17_FAUNA_CASES:
        found_cat = next((c for t, c in title_to_cat.items() if strip_accents(t) == strip_accents(fauna)), None)
        is_ok = (found_cat == CAT_17)
        if is_ok:
            passed_count += 1
        results[fauna] = {"found_category": found_cat, "expected_category": CAT_17, "status": "PASS" if is_ok else "FAIL"}

    return {"total": total, "passed": passed_count, "accuracy_pct": round((passed_count / total) * 100, 2), "details": results}


def main():
    parser = argparse.ArgumentParser(description="Àgbà Engine Sprint 004 Retrieval & Anti-Loop Benchmark")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print verbose rank details")
    args = parser.parse_args()

    print("==============================================================================")
    print("🏛️ ÀGBÀ ENGINE: SPRINT 004 RETRIEVAL & ANTI-PARENT-LOOP BENCHMARK")
    print("Specialist: Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("==============================================================================")

    retriever = AgbaHybridRetriever()
    print(f"📂 Loaded Master Corpus with {len(retriever.corpus_entities)} entities.\n")

    test_diags = []
    passed_queries, total_queries = 0, len(BENCHMARK_TEST_CASES)
    friction_passed = anti_loop_passed = 0
    friction_total = sum(1 for tc in BENCHMARK_TEST_CASES if tc.get("suite") == "14_FRICTION_QUERIES")
    anti_loop_total = sum(1 for tc in BENCHMARK_TEST_CASES if tc.get("suite") == "ANTI_PARENT_LOOP")

    for tc in BENCHMARK_TEST_CASES:
        passed, diag = evaluate_retrieval(retriever, tc)
        test_diags.append(diag)
        if passed:
            passed_queries += 1
            if tc.get("suite") == "14_FRICTION_QUERIES":
                friction_passed += 1
            elif tc.get("suite") == "ANTI_PARENT_LOOP":
                anti_loop_passed += 1
        status_str = "✅ PASS" if passed else "❌ FAIL"
        top_title = diag["top_hits"][0]["title"] if diag["top_hits"] else "NO HIT"
        top_cat = diag["top_hits"][0]["category"] if diag["top_hits"] else "N/A"
        print(f"[{status_str}] {tc['id']:<22} | Query: '{tc['query']:<14}' | Top-1: '{top_title}' ({top_cat})")
        if not passed:
            for r in diag["reasons"]:
                print(f"       ⚠️  {r}")

    print("\n------------------------------------------------------------------------------")
    print("🦁 Auditing Category 17 (Indigenous Zoology, Sacred Fauna & Wildlife)...")
    cat17 = evaluate_category_17_taxonomy(retriever)
    print(f"   Category 17 Coverage: {cat17['passed']}/{cat17['total']} ({cat17['accuracy_pct']}%)")
    for fauna, res in cat17["details"].items():
        if res["status"] != "PASS":
            print(f"   [!] Fauna '{fauna}' in '{res['found_category']}', expected '{res['expected_category']}'")

    overall_acc = round((passed_queries / total_queries) * 100, 2)
    friction_acc = round((friction_passed / friction_total) * 100, 2) if friction_total else 0
    anti_loop_acc = round((anti_loop_passed / anti_loop_total) * 100, 2) if anti_loop_total else 0

    print("\n==============================================================================")
    print("📊 BENCHMARK SUMMARY METRICS:")
    print(f"   - Total Queries Tested:       {total_queries}")
    print(f"   - Overall Top-1 Accuracy:     {passed_queries}/{total_queries} ({overall_acc}%)")
    print(f"   - 14 Friction Queries Acc:    {friction_passed}/{friction_total} ({friction_acc}%)")
    print(f"   - Anti-Parent-Loop Acc:       {anti_loop_passed}/{anti_loop_total} ({anti_loop_acc}%)")
    print(f"   - Category 17 Fauna Acc:      {cat17['passed']}/{cat17['total']} ({cat17['accuracy_pct']}%)")
    print("==============================================================================")

    gate_passed = (overall_acc >= 95.0 and anti_loop_acc == 100.0 and cat17["accuracy_pct"] >= 95.0)
    verdict = "PASS" if gate_passed else "FAIL (Pending Remap & Ingestion)"
    print(f"🏛️ SÙÚRÙ QA VERDICT: {verdict}\n")

    if args.json:
        report = {
            "summary": {"total": total_queries, "passed": passed_queries, "overall_acc": overall_acc, "friction_acc": friction_acc, "anti_loop_acc": anti_loop_acc, "cat17_acc": cat17["accuracy_pct"], "gate_passed": gate_passed, "verdict": verdict},
            "category_17_taxonomy": cat17,
            "diagnostics": test_diags
        }
        print(json.dumps(report, indent=2, ensure_ascii=False))

    return 0 if gate_passed else 1


if __name__ == "__main__":
    sys.exit(main())
