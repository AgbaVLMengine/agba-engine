# 🏛️ ÀGBÀ ENGINE: SÙÚRÙ ZERO-SHOT RETRIEVAL & ANTI-PARENT-LOOP QA BENCHMARK (SPRINT 004)
## Task Reference: `HANDOFF-SUURU-004` (Regression Benchmark Suite & Empirical Baseline Ledger)
**QA Specialist**: Sùúrù (`suuru-qa`) — *Human-Grade QA & UX Lock-In Specialist*  
**Lead Architect & Visionary**: Àrùnà Ọlànrewájú Kábírù  
**Supervising Chief Co-Architect**: Àgbà (`agba-pa-architect`)  
**Lead Auditor**: Òye (`oye-auditor`)  
**Target Fast Builder**: Àgbẹ̀dẹ (`agbede-builder`)  
**Reference Audits**: 
- `CORPUS_COMPREHENSIVE_DISCREPANCY_AND_DEPTH_AUDIT.md`
- `.agents/local-seeds/AGY__REPORT_OYE_AUDIT_004.md`
- `.agents/local-seeds/AGY__REPORT_OYE_TAXONOMY_AUDIT_005.md`
- `api/data/yoruba_corpus_1007_NORMALIZED.json`

---

### 📋 Executive Summary: Sprint 004 Benchmark Harness & Baseline Findings

To fulfill Lead Architect Àrùnà Ọlànrewájú Kábírù's mandate, `Sùúrù` has engineered an automated regression test suite (`scripts/benchmark_sprint004.py`) and executed the pre-implementation baseline benchmark across the **14 Friction Queries**, **Sub-Variant Anti-Loop Invariants**, and **Category 17 Taxonomy**.

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
   - Vein Trail: [Àrọ̀kọ̀] ➔ [Àrọ̀kọ̀ Ẹfà]        - Never collapses back to parent!
```

#### Pre-Implementation Baseline Benchmark Results (Executed 2026-10-21)
- **Overall Top-1 Retrieval Accuracy**: **`6 / 24` (25.0%)** — *FAILED (Pending Ingestion & Remap)*
- **14 Friction Queries Accuracy**: **`6 / 16` (37.5%)** — *FAILED*
- **Anti-Parent-Loop Retrieval Accuracy**: **`0 / 8` (0.0%)** — *CRITICAL FAILURE (100% Parent Collapses)*
- **Category 17 Faunal Classification Accuracy**: **`0 / 18` (0.0%)** — *PENDING REMAP*

---

## 🎯 SECTION 1: DETAILED AUDIT OF THE 14 FRICTION QUERIES

| # | Query String | Expected Canonical Entity | Domain Category | Baseline Rank #1 Result | Baseline Status | Forensic Root Cause |
|---|---|---|---|---|---|---|
| 1 | `"Were"` | `Were / Were Music` | Auditory Arts (Cat 10) | `NO HITS` | ❌ FAIL | Missing root Sovereign Parent in master corpus; token collision with `Wèrè` (psychosis) avoided but no musical entity exists. |
| 2 | `"Were Music"` | `Were / Were Music` | Auditory Arts (Cat 10) | `Àpala Music` | ❌ FAIL | Missing entity; falls back to related Yoruba genre `Àpala Music`. |
| 3 | `"Ifa"` / `"Ifá"` | `Ifá` | Spiritual Matrix (Cat 01) | `Ikin Ifá` | ❌ FAIL | Missing root Sovereign Parent `Ifá`; falls back to divinatory tool `Ikin Ifá`. |
| 4A | `"Àrọ̀kọ̀"` | `Àrọ̀kọ̀` | Oral Literature (Cat 12) | `Àrọ̀kọ̀` | ✅ PASS | Canonical parent correctly matches. |
| 4B | `"Àrọ̀kọ̀ Ẹfà"` | `Àrọ̀kọ̀ Ẹfà` (Child) | Oral Literature (Cat 12) | `Àrọ̀kọ̀` (Parent) | ❌ FAIL | **Parent-Loop Detected**: Unindexed sub-variant string collapses back to parent entity `Àrọ̀kọ̀`. |
| 4C | `"Àrọ̀kọ̀ Ẹ̀jọ́"` | `Àrọ̀kọ̀ Ẹ̀jọ́` (Child) | Oral Literature (Cat 12) | `Àrọ̀kọ̀` (Parent) | ❌ FAIL | **Parent-Loop Detected**: Judicial dispute summons sub-variant collapses to parent `Àrọ̀kọ̀`. |
| 5A | `"Oogun"` | `Oogun` (Inheritance / Property) | Social Structure (Cat 04) | `Iṣẹ́ L’òògùn Ṣìọ̀rọ̀` | ❌ FAIL | **False-Positive Token Collision**: Missing property parent; unaccented query matches proverb containing `òògùn`. |
| 5B | `"Òògùn"` | `Òògùn` (Traditional Pharmacology) | Sacred Botany (Cat 11) | `Iṣẹ́ L’òògùn Ṣìọ̀rọ̀` | ❌ FAIL | Missing pharmacological parent; matches proverb containing `òògùn`. |
| 6A | `"Idà"` | `Idà` (Martial Sword) | Military Traditions (Cat 07) | `Idà` | ✅ PASS | Canonical parent matches. |
| 6B | `"Idà Agẹmọ"` | `Idà Agẹmọ` (Child) | Military Traditions (Cat 07) | `Idà` (Parent) | ❌ FAIL | **Parent-Loop Detected**: Ritual sword sub-variant collapses to parent `Idà`. |
| 7A | `"Ọ̀kọ̀"` | `Ọ̀kọ̀` (Spear / Lance) | Military Traditions (Cat 07) | `Ọ̀kọ̀` | ✅ PASS | Canonical parent matches; diacritic tiering preserves spear over hoe (`Ọkọ́`) and husband (`Ọkọ`). |
| 7B | `"Ọ̀kọ̀ Ẹlẹ́ṣin"` | `Ọ̀kọ̀ Ẹlẹ́ṣin` (Child) | Military Traditions (Cat 07) | `Ọkọ` (Husband) | ❌ FAIL | **False Collision & Parent Loop**: Multi-word query leaks into `Ọkọ` due to unindexed child. |
| 8A | `"Ọfà"` | `Ọfà` (Bow & Arrow) | Military Traditions (Cat 07) | `Ọfà` | ✅ PASS | Word-boundary isolation prevents leakage into `Ofada` or `Ìwọ̀fà`. |
| 8B | `"Ọfà Ọdẹ"` | `Ọfà Ọdẹ` (Child) | Military Traditions (Cat 07) | `Ofà` (Parent) | ❌ FAIL | **Parent-Loop Detected**: Hunting arrow sub-variant collapses to parent `Ofà`. |
| 9A | `"Àdá"` | `Àdá` (Cutlass / Machete) | Traditional Trades (Cat 13) | `Àdá` | ✅ PASS | Canonical parent matches. |
| 9B | `"Àdá Ìbílẹ̀"` | `Àdá Ìbílẹ̀` (Child) | Traditional Trades (Cat 13) | `Àdá` (Parent) | ❌ FAIL | **Parent-Loop Detected**: Blacksmith-forged cutlass collapses to parent `Àdá`. |
| 10A | `"Epa"` | `Epa` (Helmet Masquerade) | Masquerades (Cat 15) | `Epa` | ✅ PASS | Correctly resolves northern Yoruba ancestral masquerade mask. |
| 10B | `"Ẹ̀pà"` | `Ẹ̀pà` (Groundnut / Legume) | Culinary Arts (Cat 05) | `Epa Door` | ❌ FAIL | Missing culinary groundnut parent; falls back to wood sculpture `Epa Door`. |
| 11 | `"Àpáta"` | `Àpáta` (Sacred Topography / Inselberg) | Topography & Architecture (Cat 09) | `Àpáta` (Military Shield) | ❌ FAIL | **Category Conflation**: Existing `Àpáta` entity is filed under Category 7 (Military Shield) instead of Category 9 (Sacred Topography/Inselbergs like Olúmo and Ìdánre). |
| 12A | `"Ẹja"` | `Ẹja` (Aquatic Faunal Parent) | Indigenous Zoology (Cat 17) | `Ẹja` (Spiritual Matrix) | ❌ FAIL | **Category Conflation**: Filed under Category 1 (`Spiritual & Cosmological Matrix`) instead of formulated Category 17. |
| 12B | `"Ẹja Àrọ̀"` | `Ẹja Àrọ̀` (Child) | Indigenous Zoology (Cat 17) | `Ẹja` (Parent) | ❌ FAIL | **Parent-Loop Detected**: Sacred catfish/mudfish collapses to parent `Ẹja`. |
| 13A | `"Ẹyẹ"` | `Ẹyẹ` (Avian Faunal Parent) | Indigenous Zoology (Cat 17) | `Ẹyẹ` (Spiritual Matrix) | ❌ FAIL | **Category Conflation**: Filed under Category 1 (`Spiritual & Cosmological Matrix`) instead of formulated Category 17. |
| 13B | `"Odídẹrẹ́"` | `Odídẹrẹ́` (Child) | Indigenous Zoology (Cat 17) | `Aiye Kooto` | ❌ FAIL | Missing child record; falls back to folklore entity `Aiye Kooto` without linkage to parent `Ẹyẹ`. |
| 14 | `"Apẹja"` | `Apẹja` (Fishermen Guild) | Traditional Trades (Cat 13) | `Apẹja` | ❌ FAIL | Entity retrieved, but `related_entities` is completely empty (`[]`); lacks bilateral knowledge graph edges to `Ẹja`, `Ọkọ̀ Ojú Omi`, `Odò Ọ̀ṣun`, and `Olókun`. |

---

## 🦁 SECTION 2: CATEGORY 17 FAUNA AUDIT BASELINE

The taxonomy audit in `AGY__REPORT_OYE_TAXONOMY_AUDIT_005.md` formulated Category 17: **`Indigenous Zoology, Sacred Fauna & Wildlife`**.
Evaluation of the 18 standalone animal taxa across the master corpus confirmed **0/18 (0.0%)** currently reside in Category 17:

| Faunal Taxon | English / Scientific Gloss | Current Erroneous Category | Target Canonical Category | Status |
|---|---|---|---|---|
| `Ẹja` | Fish / Aquatic Fauna Parent | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹyẹ` | Birds / Avian Fauna Parent | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹranko` | Terrestrial Mammals Parent | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ìjàpá` | Tortoise (Trickster Archetype) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Àkùkọ` | Rooster (Dawn Divination) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹsin` | Horse (Cavalry Equine) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Àgbọ̀nrin` | Bushbuck / Antelope | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹ̀kùn` | Leopard (Royal Totem) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Àmọ̀tẹ́kùn` | Cheetah / Swift Spotted Leopard | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Aáyá` | Colobus Monkey | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Egbin` | Gazelle (Elegance Archetype) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Àwòko` | Mockingbird / Singer of Songs | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹ̀fọ̀n` | African Buffalo (Strength Archetype) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Kiníun` | Lion (Sovereign Carnivore) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Àdàbà` | Dove (Peace & Blessing Carrier) | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹran-Ọ̀sọ́` | Totemic Domestic Fauna | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Àgbàǹgbá` | Bongo / Giant Horned Antelope | Spiritual & Cosmological Matrix | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |
| `Ẹ̀yọ̀-Ẹran` | Compound Livestock (Goats, Sheep) | Social Structure, Kinship & Lineage | Indigenous Zoology, Sacred Fauna & Wildlife | ❌ PENDING REMAP |

---

## 🛠️ SECTION 3: AUTOMATED BENCHMARK SPECIFICATION (`scripts/benchmark_sprint004.py`)

The automated regression script is staged at `scripts/benchmark_sprint004.py`. It executes 24 test cases across two batteries:
1. **Battery 1: 14 Friction Queries (16 test cases)**:
   - Validates Top-1 title match against exact and diacritized variations.
   - Enforces correct 17-category taxonomic classification.
   - Enforces `is_parent: true` for newly ingested Sovereign Parents.
   - Guards against false-positive token collisions (e.g. `Oogun` catching `Iṣẹ́ L’òògùn Ṣìọ̀rọ̀`).
   - Verifies bilateral knowledge graph edges on `Apẹja` (`Ẹja`, `Ọkọ̀ Ojú Omi`, `Odò Ọ̀ṣun`, `Olókun`).
2. **Battery 2: Sub-Variant Anti-Loop Invariants (8 test cases)**:
   - Validates that querying or clicking any sub-variant (`Àrọ̀kọ̀ Ẹfà`, `Àrọ̀kọ̀ Ẹ̀jọ́`, `Idà Agẹmọ`, `Ọ̀kọ̀ Ẹlẹ́ṣin`, `Ọfà Ọdẹ`, `Àdá Ìbílẹ̀`, `Ẹja Àrọ̀`, `Odídẹrẹ́`) returns the dedicated child record or dynamically synthesized child node at Rank #1.
   - **Strict Assertion**: `norm_top1 != norm_parent`. Any result returning the parent entity is instantly flagged with `PARENT-LOOP DETECTED`.
   - Enforces `is_parent: false` and `sovereign_parent: <Parent Title>`.
3. **Battery 3: Category 17 Taxonomy Coverage (18 test cases)**:
   - Scans the master corpus to confirm all 18 faunal entities are mapped to `Indigenous Zoology, Sacred Fauna & Wildlife`.

### Execution Command:
```bash
python3 scripts/benchmark_sprint004.py --json
```

---

## 🏛️ SECTION 4: SÙÚRÙ VERDICT & GREENLIGHT FOR ÀGBẸ̀DẸ (`HANDOFF-AGBEDE-004`)

- **Current Benchmark Verdict**: 🔴 **FAIL (25.0% Top-1 / 0.0% Anti-Loop / 0.0% Category 17)**
- **Baseline Integrity**: The benchmark script correctly reproduces every friction vector reported by the Lead Architect and validates Òye's forensic audits.
- **Immediate Action**: Greenlight granted for **`Àgbẹ̀dẹ` (`agbede-builder`)** to execute `HANDOFF-AGBEDE-004`:
  1. Ingest the missing Sovereign Parents (`Ifá`, `Were / Were Music`, `Oogun`, `Òògùn`, `Ẹ̀pà`, `Àpáta`, `Ẹlẹ́mù`, `Ẹégún`, `Ìwọ̀fà`).
  2. Implement the **Dynamic Sub-Variant Fallback Hydrator** in `retrieval.py` and `SearchTab.jsx`.
  3. Remap the 140 misclassified entities, establishing **Category 17: `Indigenous Zoology, Sacred Fauna & Wildlife`**.
  4. Wire bilateral `related_entities` edges on `Apẹja`, `Ẹja`, `Idà`, and `Ẹyẹ`.
- Upon notification of completion from `Àgbẹ̀dẹ`, `Sùúrù` will immediately rerun `scripts/benchmark_sprint004.py` to certify **>= 95% Top-1 retrieval accuracy** and complete UX Lock-In.
