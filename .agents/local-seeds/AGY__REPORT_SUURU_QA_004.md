# 🏛️ ÀGBÀ ENGINE: SÙÚRÙ ZERO-SHOT RETRIEVAL & ANTI-PARENT-LOOP QA BENCHMARK (SPRINT 004)
## Category X: Sovereign Parents, Missing Root Entities & Dynamic Sub-Variant Hydration Suite
**QA Specialist**: Sùúrù (`suuru-qa`)  
**Lead Architect & Visionary**: Àrùnà Ọlànrewájú Kábírù  
**Supervising Chief Co-Architect**: Àgbà (`agba-pa-architect`)  
**Lead Auditor**: Òye (`oye-auditor`)  
**Target Builder**: Àgbẹ̀dẹ (`agbede-builder`)  
**Reference Documents**: 
- `CORPUS_COMPREHENSIVE_DISCREPANCY_AND_DEPTH_AUDIT.md`
- `.agents/local-seeds/AGY__REPORT_OYE_AUDIT_004.md`
- `api/data/yoruba_corpus_1007_NORMALIZED.json`

---

### 📋 Executive Summary of Test Suite: Category X

**Category X** establishes the dedicated QA validation battery for Sprint 004, specifically formulated to stress-test the ingestion of **9 Missing Sovereign Parents**, eliminate **Sub-Variant Parent Loops** across **34 Sovereign Parents (100 unindexed child entities)**, and verify the **Zero-Hardcoding Dynamic Sub-Variant Fallback Hydrator** in `SearchTab.jsx` and `retrieval.py`.

```
                      [ USER QUERY: "Àrọ̀kọ̀ Ẹfà" ]
                                    │
                                    ▼
                     [ Dynamic Sub-Variant Hydrator ]
                                    │
               ┌────────────────────┴────────────────────┐
               ▼                                         ▼
   [ Node Synthesized at Rank #1 ]            [ Sovereign Parent Node ]
   - Title: "Àrọ̀kọ̀ Ẹfà"                       - Title: "Àrọ̀kọ̀"
   - is_parent: false                         - is_parent: true
   - sovereign_parent: "Àrọ̀kọ̀"                 - sovereign_parent_status: "Parent"
   - Vein Trail: [Àrọ̀kọ̀] ➔ [Àrọ̀kọ̀ Ẹfà]        - Never collapses back to self!
```

---

## 🎯 CATEGORY X TEST SUITE SPECIFICATION

### Battery X-1: Missing Sovereign Parent Canonical Retrieval (9 Test Queries)
*Objective*: Verify that exact-match and semantic token queries for newly ingested canonical parents return the parent at Rank #1 (`fusion_score: 1.0000` or `>0.9600`), establishing an authentic Sovereign Parent card (`is_parent: true`) with complete 14-tier schema.

| Query ID | Test Query String | Canonical Target Entity | Domain Category | Expected Rank & Type | Pass / Fail Invariants |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `X-1.01` | `"Ifá"` / `"Ifa"` | **`Ifá`** | Spiritual & Cosmological Matrix | **Rank #1 (Sovereign Parent)** | `is_parent: true`; must NOT fall back to `Ọ̀rúnmìlà` or `Ọpọ́n Ifá` as primary root; contains 256 Odù matrix reference. |
| `X-1.02` | `"Were"` / `"Were Music"` | **`Were / Were Music`** | Auditory Arts, Music, Drums & Chants | **Rank #1 (Sovereign Parent)** | `is_parent: true`; distinct from `Wèrè` (madness); traces Ajísààrì Islamic dawn awakening precursor to Fújì. |
| `X-1.03` | `"Oogun (Property)"` / `"Oogun"` | **`Oogun`** | Social Structure, Kinship & Lineage | **Rank #1 (Sovereign Parent)** | `is_parent: true`; must NOT collide with `Òògùn` (medicine) or proverb `Iṣẹ́ L’òògùn Ṣìọ̀rọ̀`. |
| `X-1.04` | `"Òògùn"` / `"Oogun traditional medicine"` | **`Òògùn`** | Sacred Botany, Flora & Herbal Medicine | **Rank #1 (Sovereign Parent)** | `is_parent: true`; pharmacological infusions & talismans; homographically separated from `Oogun` property. |
| `X-1.05` | `"Ẹ̀pà (Groundnut)"` / `"Epa"` | **`Ẹ̀pà`** | Culinary Arts & Indigenous Gastronomy | **Rank #1 (Sovereign Parent)** | `is_parent: true`; agrarian legume; disambiguated from `Epa` masquerade helmet mask. |
| `X-1.06` | `"Àpáta (Rock Formation)"` / `"Apata"` | **`Àpáta`** | Topography, Natural Landscapes & Architecture | **Rank #1 (Sovereign Parent)** | `is_parent: true`; inselbergs & granite hills (Olúmo, Ìdánre); disambiguated from military shield. |
| `X-1.07` | `"Ẹlẹ́mù"` / `"Elemu"` | **`Ẹlẹ́mù`** | Traditional Trades, Agriculture & Agrarian Guilds | **Rank #1 (Sovereign Parent)** | `is_parent: true`; palm wine tapper guild; linked to `Ẹ̀mù Ọ̀pẹ` and `Ògùrọ̀`. |
| `X-1.08` | `"Ẹégún"` / `"Eegun"` | **`Ẹégún`** | Ancestral Masquerades & Funerary Rites | **Rank #1 (Sovereign Parent / Sovereign Alias)** | Maps deterministically to ancestral masquerade without dropping into generic `Ẹgbẹ́`. |
| `X-1.09` | `"Ìwọ̀fà"` / `"Iwofa"` | **`Ìwọ̀fà`** | Civilization, History & Civic Heritage | **Rank #1 (Sovereign Parent)** | Traditional pre-colonial pawnship/labor contract; zero substring collision with `Ọfà` (arrow) or `Ofada`. |

---

### Battery X-2: Anti-Parent-Loop Sub-Variant Dynamic Hydration (16 Test Queries)
*Objective*: When querying or clicking unindexed sub-variants that exist in a parent's `sub_variants` array, the system MUST dynamically hydrate a dedicated child node at Rank #1 (`is_parent: false`, `sovereign_parent: parent.title`), branch the Vein Rabbit-Hole (`Parent ➔ Child`), and NEVER display the Parent card in place of the clicked child.

| Query ID | Sub-Variant Query String | Parent Entity | Category | Expected Synthesized Node | Anti-Loop Invariant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `X-2.01` | `"Àrọ̀kọ̀ Ẹfà"` / `"Aroko Efa"` | `Àrọ̀kọ̀` | Oral Literature | `Àrọ̀kọ̀ Ẹfà` (Rank #1 Child) | Must NOT collapse to `Àrọ̀kọ̀`; vein shows `[Àrọ̀kọ̀] ➔ [Àrọ̀kọ̀ Ẹfà]`. |
| `X-2.02` | `"Àrọ̀kọ̀ Ẹ̀jọ́"` / `"Aroko Ejo"` | `Àrọ̀kọ̀` | Oral Literature | `Àrọ̀kọ̀ Ẹ̀jọ́` (Rank #1 Child) | Must NOT collapse to `Àrọ̀kọ̀`; indicates judicial conflict summons. |
| `X-2.03` | `"Àrọ̀kọ̀ Ogun"` / `"Aroko Ogun"` | `Àrọ̀kọ̀` | Oral Literature | `Àrọ̀kọ̀ Ogun` (Rank #1 Child) | Must NOT collapse to `Àrọ̀kọ̀` or deity `Ògún`; represents war declaration. |
| `X-2.04` | `"Ẹyin Ìkódẹ"` / `"Eyin Ikode"` | `Àrọ̀kọ̀` | Oral Literature | `Ẹyin Ìkódẹ` (Rank #1 Child) | Parent is `Àrọ̀kọ̀`; signifies supreme royal summons via parrot feather. |
| `X-2.05` | `"Ọ̀kọ̀ Ẹlẹ́ṣin"` / `"Oko Elesin"` | `Ọ̀kọ̀` | Military Traditions | `Ọ̀kọ̀ Ẹlẹ́ṣin` (Rank #1 Child) | Must NOT collapse to `Ọ̀kọ̀`; identifies cavalry lance. |
| `X-2.06` | `"Ọ̀kọ̀ Ògún"` / `"Oko Ogun"` | `Ọ̀kọ̀` | Military Traditions | `Ọ̀kọ̀ Ògún` (Rank #1 Child) | Must NOT collapse to `Ọ̀kọ̀` or `Ògún`; consecrated metallurgical lance. |
| `X-2.07` | `"Ọfà Ọdẹ"` / `"Ofa Ode"` | `Ọfà` | Military Traditions | `Ọfà Ọdẹ` (Rank #1 Child) | Must NOT collapse to `Ọfà` or `Ọdẹ`; identifies hunting arrow. |
| `X-2.08` | `"Apó Ọfà"` / `"Apo Ofa"` | `Ọfà` | Military Traditions | `Apó Ọfà` (Rank #1 Child) | Must NOT collapse to `Ọfà`; identifies leather quiver. |
| `X-2.09` | `"Àdá Ìbílẹ̀"` / `"Ada Ibile"` | `Àdá` | Traditional Trades | `Àdá Ìbílẹ̀` (Rank #1 Child) | Must NOT collapse to `Àdá`; identifies standard clearing machete. |
| `X-2.10` | `"Àdá Pẹ́pẹ́"` / `"Ada Pepe"` | `Àdá` | Traditional Trades | `Àdá Pẹ́pẹ́` (Rank #1 Child) | Must NOT collapse to `Àdá`; identifies pruning cutlass. |
| `X-2.11` | `"Idà Agẹmọ"` / `"Ida Agemo"` | `Idà` | Military Traditions | `Idà Agẹmọ` (Rank #1 Child) | Must NOT collapse to `Idà`; ceremonial curved broadsword. |
| `X-2.12` | `"Idà Ọba"` / `"Ida Oba"` | `Idà` | Military Traditions | `Idà Ọba` (Rank #1 Child) | Must NOT collapse to `Idà` or `Ọba`; royal state sword of justice. |
| `X-2.13` | `"Tanmogayi"` | `Idà` | Military Traditions | `Tanmogayi` (Rank #1 Child) | Must NOT collapse to `Idà`; cavalry slashing sabre. |
| `X-2.14` | `"Àwọ̀n Apẹja"` / `"Awon Apeja"` | `Apẹja` | Traditional Trades | `Àwọ̀n Apẹja` (Rank #1 Child) | Must NOT collapse to `Apẹja`; artisanal river casting net. |
| `X-2.15` | `"Ẹja Àrọ̀"` / `"Eja Aro"` | `Ẹja` | Spiritual & Cosmological | `Ẹja Àrọ̀` (Rank #1 Child) | Must NOT collapse to `Ẹja` or `Àrọ̀`; sacred catfish/mudfish. |
| `X-2.16` | `"Odídẹrẹ́"` / `"Odidere"` | `Ẹyẹ` | Spiritual & Cosmological | `Odídẹrẹ́` (Rank #1 Child) | Must NOT collapse to `Ẹyẹ`; sacred African grey parrot. |

---

### Battery X-3: Tonal Homograph & Substring Collision Traps (10 Stress Queries)
*Objective*: Prevent false-positive token collisions that historically corrupted retrieval in `SearchTab.jsx` and `retrieval.py`.

| Query ID | Stress Query | False-Positive Trap to Avoid | Deterministic Target Entity | Validation Rule |
| :--- | :--- | :--- | :--- | :--- |
| `X-3.01` | `"Oogun"` | `Iṣẹ́ L’òògùn Ṣìọ̀rọ̀` (Proverb) / `Òògùn` (Medicine) | **`Oogun` (Inheritance / Property)** | Exact tonal invariant; does not match proverbs containing `òògùn`. |
| `X-3.02` | `"Òògùn"` | `Oogun` (Property) | **`Òògùn` (Traditional Pharmacology)** | Exact diacritic match (+600.0) elevates pharmacological node. |
| `X-3.03` | `"Ọkọ́"` | `Ọ̀kọ̀` (Spear) / `Ọkọ` (Husband) / `Oko` (Farm) | **`Ọkọ́` (Agricultural Hoe)** | Exact tone (1060.0) isolates Hoe; zero substring bleed. |
| `X-3.04` | `"Ọ̀kọ̀"` | `Ọkọ́` (Hoe) / `Ọkọ` (Husband) / `Oko` (Farm) | **`Ọ̀kọ̀` (Military Spear)** | Exact tone (1060.0) isolates Spear; zero substring bleed. |
| `X-3.05` | `"Ọfà"` | `Ofada` (Rice) / `Ìwọ̀fà` (Pawnship) | **`Ọfà` (Bow & Arrow)** | Word-boundary regex `\bọfà\b` prevents substring leakage into `Ofada` or `Ìwọ̀fà`. |
| `X-3.06` | `"Ofada"` | `Ọfà` (Bow & Arrow) | **`Ọ̀fàdà` (Indigenous Rice)** | Diacritized canon `Ọ̀fàdà` ranks #1; no association with archery. |
| `X-3.07` | `"Àpáta"` | `Àpáta` (Defense Shield) | **`Àpáta` (Inselberg Topography)** | Disambiguates rock topography from defensive shield standard. |
| `X-3.08` | `"Epa"` | `Ẹ̀pà` (Groundnut) | **`Epa` (Ancestral Helmet Masquerade)** | Disambiguates northern Yorùbá masquerade from edible legume. |
| `X-3.09` | `"Ẹ̀pà"` | `Epa` (Masquerade) | **`Ẹ̀pà` (Groundnut & Agronomy)** | Exact low-tone underdot `Ẹ̀pà` ranks culinary legume #1. |
| `X-3.10` | `"Were"` | `Wèrè` (Madness / Psychosis) | **`Were / Were Music`** | Musical genre node takes priority under auditory art domain. |

---

## 🔬 SÙÚRÙ AUTOMATION HARNESS (READY FOR INGESTION VERIFICATION)

```python
# test_category_x_anti_loop.py
import json
import pytest

def test_missing_parents_exist(corpus_data):
    REQUIRED_PARENTS = [
        "Ifá", "Were / Were Music", "Oogun", "Òògùn", 
        "Ẹ̀pà", "Àpáta", "Ẹlẹ́mù", "Ẹégún", "Ìwọ̀fà"
    ]
    corpus_titles = {e["title"] for e in corpus_data}
    for parent in REQUIRED_PARENTS:
        assert any(parent.lower() in t.lower() for t in corpus_titles), f"Missing Sovereign Parent: {parent}"

def test_sub_variant_hydration_anti_loop(runtime_resolver):
    TEST_PAIRS = [
        ("Àrọ̀kọ̀ Ẹfà", "Àrọ̀kọ̀"),
        ("Ọ̀kọ̀ Ẹlẹ́ṣin", "Ọ̀kọ̀"),
        ("Ọfà Ọdẹ", "Ọfà"),
        ("Àdá Ìbílẹ̀", "Àdá"),
        ("Idà Agẹmọ", "Idà"),
        ("Àwọ̀n Apẹja", "Apẹja"),
        ("Ẹja Àrọ̀", "Ẹja"),
        ("Odídẹrẹ́", "Ẹyẹ")
    ]
    for child_query, expected_parent in TEST_PAIRS:
        node = runtime_resolver.resolve(child_query)
        assert node["title"].lower() != expected_parent.lower(), f"Parent-Loop detected for query {child_query}!"
        assert node["sovereign_parent"].lower() == expected_parent.lower(), f"Child node failed to declare {expected_parent} as parent."
        assert node["is_parent"] is False, f"Sub-variant node {child_query} incorrectly flagged as parent."
```

---

## 🏛️ Sùúrù Human-Simulation Verification Verdict
- **Status**: 🟢 **CATEGORY X TEST BATTERY ARMORED & READY**
- **Action Required by Àgbẹ̀dẹ (`agbede-builder`)**:
  1. Ingest the 9 missing Sovereign Parents with complete 14-tier attributes.
  2. Implement the Zero-Hardcoding Dynamic Child Hydrator in `SearchTab.jsx` and `retrieval.py`.
  3. Wire the bilateral knowledge graph links for `Apẹja`, `Ẹja`, `Idà`, and `Ẹyẹ`.
- Once Àgbẹ̀dẹ signals deployment, Sùúrù will execute this 35-query battery to certify zero-shot retrieval and UX lock-in.
