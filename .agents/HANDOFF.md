# 🎯 ZERO-WASTE HANDOFF CARDS (`.agents/HANDOFF.md`)

> **Supervised By**: `Àgbà` (`agba-pa-architect` — Main P.A. & Chief Co-Architect)  
> **Lead Architect**: Àrùnà Ọlànrewájú Kábírù  
> **Active Focus**: 📜 **HANDOFF-AROKIN-001 (CORPUS MASTERY, ENRICHMENT & CROSS-CULTURAL SCOUTING)** + 🛡️ **HANDOFF-ESO-001 (ZERO-TRUST PERIMETER)**

---

## 0. Active Archivist Handoff (`HANDOFF-AROKIN-001`)

### `HANDOFF-AROKIN-001` — Corpus Structure Mastery, Phase 4 Batch Enrichment & Cross-Cultural Scouting Protocol
- **Assigned To**: **`Àrọ̀kìn`** (`arokin-archivist`)
- **Council Partners**: `Ìmọ̀` (Legal/Provenance), `Ẹ̀ṣọ́` (Security Sentinel), `Àgbẹ̀dẹ` (Builder/Hydrator), `Sùúrù` (QA Specialist)
- **Supervising Co-Architect**: `Àgbà` (`agba-pa-architect`)
- **Target Files**:
  - `/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json`
  - `/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json`
  - `/home/aruna_olanrewaju/agba-engine/scripts/thin_entities_manifest.json`
  - `/home/aruna_olanrewaju/agba-engine/scripts/batch_enrich_subagent.py`
  - `/home/aruna_olanrewaju/agba-engine/.agents/memory/arokin-archivist.md`
- **Execution Mandates**:
  1. **Corpus Structure Deep Study**:
     - Systematically analyze the 1,419 canonical records to master data extraction, normalization, and formatting standards.
     - Enforce the 14-Tier Schema: Multi-epoch timelines, dual-language proverbs with philosophical commentary, physical craftsmanship, court protocol, diaspora survivals, sensory aesthetics, living variants, and zero *Awo* disclosure.
  2. **Phase 4 Batch Enrichment**:
     - Backfill remaining 427 thin entities to elevate the entire 1,419 master corpus to 100% Àmọ̀tẹ́kùn-grade parity without external API keys.
  3. **Autonomous Cross-Cultural Scouting (Idle Protocol)**:
     - When not actively enriching, scout and structure candidate corpora for sister African civilizations (Benin/Edo, Igbo, Hausa/Fulani, Akan/Ashanti, Swahili).
  4. **Strict 5-Agent Interlocking Pipeline**:
     - Never ingest newly scouted cultural corpora directly into production without Ìmọ̀ (legal/CC0 clearance), Ẹ̀ṣọ́ (zero-trust security), Àgbẹ̀dẹ (data hydration), Sùúrù (QA retrieval benchmarks), and Àgbà (Co-Architect review for Lead Architect approval).

---

## 0. Active Security Handoff (`HANDOFF-ESO-001`) — Staged for Àgbà Review

### `HANDOFF-ESO-001` — Proactive Zero-Trust Perimeter, Query-Key Deprecation & RAG Hardening
- **Assigned To**: **`Ẹ̀ṣọ́`** (`eso-security`) in coordination with **`Àgbà`** (`agba-pa-architect`)
- **Status**: 🟡 **Awaiting Chief Co-Architect (`Àgbà`) Architectural Review & Concurrence**
- **Target Files**:
  - `/home/aruna_olanrewaju/agba-engine/api/app/intelligence.py` (Current: 466 LOC; Target: <475 LOC)
  - `/home/aruna_olanrewaju/agba-engine/api/app/main.py` (Current: 346 LOC; Target: <355 LOC)
- **Security Specifications & Blast-Radius Mitigation**:
  1. **Item 1: RAG Prompt Injection & System Exfiltration Hardening (`intelligence.py`)**:
     - Wrap external input and canonical context in semantic XML delimiters: `<canonical_knowledge_base>` and `<user_query>`.
     - Inscribe Rule 5 in `system_instruction`: Strict prohibition against revealing system prompts, internal variables, or role inversion under adversarial phrasing ("ignore previous instructions", "DAN", etc.).
     - Truncate input message to max 1,500 characters prior to LLM synthesis.
  2. **Item 2: URL Query-Parameter Credential Deprecation (`main.py` L72)**:
     - Neutralize OWASP API3 risk (API keys leaked in Netlify/Cloud Run access logs and Referer headers).
     - Restrict primary authentication to `X-AGBA-API-KEY` and `Authorization: Bearer` headers; emit a telemetry security warning if legacy query-param `api_key` is detected.
  3. **Item 3: DoS & Context-Stuffing Payload Bounding (`main.py`)**:
     - Enforce `max_length=1000` on `QueryRequest.query`, `DiacritizeRequest.text`, and `CulturalTranslateRequest.text`.
     - Enforce `max_length=2000` on `ChatRequest.message` and `max_length=20` on `ChatRequest.session_history` to prevent Cloud Run 2GiB memory spikes on free tier.
- **Verification Gates Required**:
  - Gate 2: Both files must remain strictly `<500 LOC` (`intelligence.py` < 475, `main.py` < 355).
  - Gate 8: Clean pass in `./scripts/review.sh`.

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
