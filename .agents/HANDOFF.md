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
  5. **Mandatory Citational Provenance & Master Bibliography Cross-Referencing**:
     - Every enriched entity MUST explicitly document its exact bibliographic citation / archival origin in `provenance_and_citations`.
     - Explicitly cross-reference against `AGBA_CANONICAL_PROVENANCE_AND_BIBLIOGRAPHY.md` (e.g., Rev. Samuel Johnson 1921, Wándé Abímbọ́lá 1975/1976, Rowland Abiodun 2014, Babatunde Lawal 1996, William Bascom 1969/1980, Pierre Verger 1995, British Museum, The Met, Cleveland Museum of Art).
     - If an entity utilizes a source not currently listed in the Master Bibliography, explicitly tag it as `[NEW CITATIONAL SOURCE: <Author/Archive, Year, Title>]` so Ìmọ̀ and Àgbà can verify and catalog it into `AGBA_CANONICAL_PROVENANCE_AND_BIBLIOGRAPHY.md`.
  6. **QA Watchlist Alert (Sùúrù Forensic Discovery)**:
     - Prior to enriching Batch 3 and subsequent batches, cross-check manifest targets against the normalized corpus to prevent generating split twin records (e.g. `Aso-Ẹbí` vs `Aṣọ Ẹ̀bị́`, `Otun-Iyalode` vs `Otun Iyalode`). Consolidate on exact canonical titles.

---

## 0B. Active Data Quality & QA Handoff (`HANDOFF-DEDUPLICATION-001`)

### `HANDOFF-DEDUPLICATION-001` — Sub-Surface Duplicate Twin Node Consolidation
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`) & **`Àrọ̀kìn`** (`arokin-archivist`)
- **Supervised By**: **`Àgbà`** (`agba-pa-architect`)
- **Reported By**: **`Sùúrù`** (`suuru-qa` — Checkpoint 023)
- **Status**: 🟡 **QUEUED FOR NEXT MAINTENANCE PASS**
- **Target Files**:
  - `/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json`
  - `/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json`
- **Specific Remediation Tasks**:
  1. **Consolidate `Aso-Ẹbí`**:
     - Newly enriched canonical record: `Aso-Ẹbí` (Batch 2).
     - Legacy duplicate record: `Aṣọ Ẹ̀bị́` (carrying Vietnamese underdot `ị` `U+1ECB`).
     - Merge any unique tags/aliases from `Aṣọ Ẹ̀bị́` into `Aso-Ẹbí` and remove the corrupt legacy twin.
  2. **Consolidate `Otun-Iyalode`**:
     - Newly enriched record: `Otun-Iyalode` (hyphenated).
     - Legacy twin record: `Otun Iyalode` (unhyphenated space).
     - Merge `Otun Iyalode` into `Otun-Iyalode`, retaining `"otun iyalode"` as an indexed alias so both hyphenated and space-separated searches resolve to a single canonical entity.

---

## 0. Active Security Handoff (`HANDOFF-ESO-001`) — Staged for Àgbà Review

### `HANDOFF-ESO-001` — Proactive Zero-Trust Perimeter, Query-Key Deprecation & RAG Hardening
- **Assigned To**: **`Ẹ̀ṣọ́`** (`eso-security`) in coordination with **`Àgbà`** (`agba-pa-architect`)
- **Status**: 🟢 **COMPLETED & VERIFIED (Checkpoint 018)**
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

### 3. `HANDOFF-AGBEDE-004` (Completed — Checkpoint 016)
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Status**: 🟢 **COMPLETED** (Category 17 Remapping, 9 Sovereign Parents ingested, Zero-Hardcoded Dynamic Sub-Variant Hydrator active).

---

### 4. `HANDOFF-AGBEDE-005` (Staged — UI Prototype Proposals Awaiting Lead Architect Greenlight)
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Supervised By**: **`Àgbà`** (`agba-pa-architect`)
- **Status**: 🟡 **STAGED FOR REVIEW**
- **Proposal Memo**:
  1. **Prototype A: "Àkọsílẹ̀" Citational Provenance Drawer (`EntityBentoDeck.jsx`)**: Render interactive scholarly citations on each Bento card exposing the 281+ backfilled primary sources (Johnson 1921, Smith 1988, Akintoye 1971, Abiodun 2014, Lawal 1996, Verger 1995).
  2. **Prototype B: Living Sub-Variant "Constellation Grid" (`SearchTab.jsx`)**: Sculptural radial/bento constellation displaying living variants under Sovereign Parents for 1-click sub-vein expansion.
  3. **Prototype C: Visual Tonal Contour & Melodic Pitch Waveform (`ToothSearchCore.jsx` / `TranslateTab.jsx`)**: Dynamic pitch contour curve rendering *Re, Mi, Do* (Mid, High, Low) tones over syllables for homographs and active queries.
  4. **Prototype D: Ancestral Journey Exporter (`VeinRabbitHoleCanvas.jsx` / `SearchTab.jsx`)**: Visual journey trail exporter transforming explored vein paths into study syllabi / shareable heritage maps.
- **Constraints**: Gate 2 (<500 LOC per module), Gate 3 (synchronous `useRef` locks), Gate 4 (100% 25-letter diacritics).
- **Execution**: Standing by for Lead Architect Àrùnà Ọlànrewájú Kábírù's greenlight.
