# 🎯 ZERO-WASTE HANDOFF CARDS (`.agents/HANDOFF.md`)

> **Supervised By**: `Àgbà` (`agba-pa-architect` — Main P.A. & Chief Co-Architect)
> **Lead Architect**: Àrùnà Ọlànrewájú Kábírù
> **Status**: 🟡 **SPRINT 004 (`HANDOFF-004`) — FORENSIC CORPUS AUDIT & ZERO-SHOT ARCHITECTURE**
> **Mandate**: **Audit First Before Ingestion**. Establish exact inventory of missing parents, unindexed sub-variants, dynamic hydration architecture, and knowledge graph linkages before batch ingestion.

---

## Active Audit Sprint (`HANDOFF-004` Series)

### 1. `HANDOFF-OYE-004` — Comprehensive Forensic Corpus Gap & Knowledge Graph Audit
- **Assigned To**: **`Òye`** (`oye-auditor`)
- **Supervising Co-Architect**: `Àgbà` (`agba-pa-architect`)
- **Target Files**:
  - `/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json`
  - `/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json`
  - `/home/aruna_olanrewaju/agba-engine/CORPUS_COMPREHENSIVE_DISCREPANCY_AND_DEPTH_AUDIT.md`
  - `/home/aruna_olanrewaju/agba-engine/web/src/utils/relativesResolver.js`
  - `/home/aruna_olanrewaju/agba-engine/web/src/components/SearchTab.jsx`
- **Audit Mandates**:
  1. **Part I: Missing Parent Entities Audit**:
     - Identify all foundational parent entities that currently do not exist as distinct canonical nodes in the 1,333 corpus (e.g. `Ifá`, `Were / Were Music`, `Oogun` [Property/Estate] vs `Òògùn` [Medicine], `Ẹ̀pà` [Groundnut], `Àpáta` [Rock Formations], and any other missing cosmological/cultural parents).
  2. **Part II: Sub-Variant Inventory Audit**:
     - Extract all sub-variants declared under `Àrọ̀kọ̀`, `Ọ̀kọ̀`, `Ọfà`, `Àdá`, and all other Sovereign Parents across the corpus.
     - Cross-reference against existing corpus entities to catalog exactly which sub-variants currently lack standalone records and cause the "sub-variant resolving parent" loop.
  3. **Part III: Generalized Dynamic Sub-Variant Fallback Hydration Specification**:
     - Design a 100% data-driven, zero-hardcoded algorithmic hydration mechanism for `SearchTab.jsx` and `retrieval.py`.
     - When any sub-variant is queried or clicked that does not have a standalone record, the engine must dynamically synthesize a full 14-tier node inheriting its parent's category, historical origin, and cultural lineage, establishing a true child node without looping back to the parent.
  4. **Part IV: Knowledge Graph Connectivity Audit**:
     - Beyond `Apẹja`, `Ẹja`, `Idà`, audit all entities across the entire 1,333 corpus that currently have empty or weakly linked `related_entities`.
     - Group them by cultural domain and establish the authentic bilateral semantic relationships needed for the Knowledge Graph.
- **Output Artifact**: Save comprehensive audit report to `.agents/local-seeds/AGY__REPORT_OYE_AUDIT_004.md` and update `.agents/memory/oye-auditor.md`.

---

### 2. `HANDOFF-SUURU-004` — Zero-Shot QA Stress-Test & Simulation Benchmark
- **Assigned To**: **`Sùúrù`** (`suuru-qa`)
- **Supervising Co-Architect**: `Àgbà` (`agba-pa-architect`)
- **Target Files**:
  - `/home/aruna_olanrewaju/agba-engine/api/app/retrieval.py`
  - `/home/aruna_olanrewaju/agba-engine/web/src/components/SearchTab.jsx`
- **Audit Mandates**:
  1. Construct a rigorous validation test suite covering the Lead Architect's 14 test queries (`Were`, `Were Music`, `Ifa`, `Àrọ̀kọ̀`, `Oogun`, `Idà`, `Ọ̀kọ̀`, `Ọfà`, `Àdá`, `Epa`, `Àpáta`, `Ẹja`, `Ẹyẹ`, `Apẹja`).
  2. Identify false-positive token collisions (e.g., `Oogun` catching `Iṣẹ́ L’òògùn Ṣìọ̀rọ̀`).
  3. Pre-validate Òye's dynamic hydration architecture against homograph and diacritic edge cases.
- **Output Artifact**: Save report to `.agents/local-seeds/AGY__REPORT_SUURU_QA_004.md` and update `.agents/memory/suuru-qa.md`.

---

### 3. `HANDOFF-AGBEDE-004` (Staged — Pending Audit Review)
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Mandate**: Staged on hold until Lead Architect reviews and approves Òye's audit findings. Implementation of the backfill, ingestion, and dynamic hydration code will commence immediately upon greenlight.
