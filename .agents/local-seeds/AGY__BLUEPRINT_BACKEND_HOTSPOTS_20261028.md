# 🏛️ ADVERSARIAL RED-TEAM ARCHITECTURAL BLUEPRINT
## Backend Hotspot De-escalation: `retrieval.py` & `telemetry_processor.py`
**Auditor Persona**: `Òye` (`oye-auditor` — Deep Analytical Discernment, Root-Cause Comprehension & Industry Standards Enforcer)  
**Date**: 2026-10-28T12:35:00Z  
**Document ID**: `AGY__BLUEPRINT_BACKEND_HOTSPOTS_20261028`  
**Governance Anchor**: The 4 Anti-Exponential Scaling Laws (`.agents/AGENTS.md`) & The 3-Tier Pre-Commit Scanner (`./scripts/review.sh`)

---

## 1. Executive Summary & Hotspot Forensic Census

Following our historic victory in completely eradicating client-side Gate 2 violations (slicing `SearchTab.jsx` from 486 → 227 LOC and `TranslateTab.jsx` from 612 → 69 LOC), `Òye` has conducted a forensic static analysis across the entire backend (`api/app/`).

Two significant architectural bottlenecks require proactive de-escalation:

| Backend File | Current LOC | Status under 3-Tier Scanner | Threat Assessment |
| :--- | :---: | :---: | :--- |
| [`api/app/retrieval.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/retrieval.py) | **`451`** | 🛑 **Orange Embargo Alert (≥ 450 LOC)** | 49 lines from Gate 2 ceiling. Zero inline feature additions permitted until decomposed. |
| [`api/app/intelligence.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/intelligence.py) | **`477`** | 🛑 **Orange Embargo Alert (≥ 450 LOC)** | 23 lines from Gate 2 ceiling. Zero inline feature additions permitted until decomposed. |
| [`api/app/telemetry_processor.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/telemetry_processor.py) | **`197`** | ✅ **Gate 2 Resolved (Green Zone < 250 LOC)** | Successfully decomposed from 607 LOC into `hitl_diagnostics.py` & `hitl_card_generator.py`. |

By applying **Law 1 (The 250-LOC Coordinator Invariant)** and **Law 2 (The Three-Drawer Mandate)** to `/api`, we can permanently neutralize both backend bottlenecks.

---

## 2. Blueprint A: `api/app/retrieval.py` Modularization

### A. Problem Statement & Functional Entanglement
`api/app/retrieval.py` currently attempts to execute four distinct engineering duties inside a single 446-line file:
1. Retrieval orchestration, config initialization, and singleton lifecycle.
2. Qdrant dense vector search (`search_dense`).
3. Complex diacritic-aware lexical scoring with RC-1 Tonal Invariants (+600 vs +450 vs +180) and 14-tier keyword matching (`search_lexical`).
4. Dynamic Sub-Variant Fallback synthesis (`_find_sub_variant_match` and `_synthesize_sub_variant`).
5. Reciprocal Rank Fusion (`RRF`, k=60) and multimodal resolution mapping.

### B. The 3-Module Decomposition Architecture

```mermaid
flowchart TD
    API["/v6/search & /v6/retrieve/deep-context (main.py)"] --> Retriever["api/app/retrieval.py\n(Lean Hybrid Coordinator ~160 LOC)"]
    Retriever --> Dense["Qdrant Client & MiniLM Embeddings\n(search_dense ~30 LOC inline)"]
    Retriever --> Lexical["api/app/lexical_ranker.py\n(Tonal Invariant & RC-1 Matcher ~130 LOC)"]
    Retriever --> Hydrator["api/app/sub_variant_hydrator.py\n(Dynamic Anti-Loop Fallback ~95 LOC)"]
    Retriever --> RRF["Reciprocal Rank Fusion\n(RRF k=60 & Multimodal Resolver)"]
```

#### Module 1: `api/app/lexical_ranker.py` (Target: ~130 LOC)
- **Extracted Responsibility**:
  - `score_lexical_entities(corpus_entities: List[Dict], query: str, top_k: int = 15) -> List[Dict[str, Any]]`
  - Encapsulates:
    - Tier 1A: Supreme Exact Diacritic/Tonal Match (`+600.0` parity).
    - Tier 1B: Accent-Folded Exact Match (`+450.0` un-diacritized, `+180.0` tone conflict).
    - Tier 2: Strict Word-Boundary Phrase Match (`+250.0`).
    - Tier 3: Category match bonus (`+3.0`).
    - Tier 4: Token matching across 14-Tier schema properties.
    - Tier 5: RC-3 English-to-Yorùbá Semantic Bridge bonus.
- **Dependencies**: `app.semantic_bridge` (`preprocess_query_tokens`, `normalize_y`, `strip_accents`). Zero Qdrant/Embedding dependencies.

#### Module 2: `api/app/sub_variant_hydrator.py` (Target: ~95 LOC)
- **Extracted Responsibility**:
  - `find_sub_variant_match(corpus_entities: List[Dict], query: str) -> Optional[Tuple[str, Dict]]`
  - `synthesize_sub_variant(variant_title: str, parent: Dict[str, Any]) -> Dict[str, Any]`
- **Alignment**: Exactly mirrors the frontend logic in `web/src/utils/subVariantHydrator.js`, guaranteeing 100% parity between Python backend and React client.

#### Module 3: `api/app/retrieval.py` (Lean Coordinator: Target ~160 LOC)
- **Retained Responsibility**:
  - `ÀgbàHybridRetriever` class lifecycle and singleton `get_instance()`.
  - Qdrant collection connection and MiniLM dense vector search (`search_dense`).
  - Calls `score_lexical_entities` from `lexical_ranker.py`.
  - Reciprocal Rank Fusion (`RRF`, k=60) blending dense and lexical rankings.
  - Sub-variant injection via `sub_variant_hydrator.py`.
- **Headroom Reclaimed**: Slashed from **446 LOC down to ~160 LOC** (**>64% operational headroom**).

---

## 3. Blueprint B: `api/app/telemetry_processor.py` Modularization

### A. Problem Statement & Functional Entanglement
`api/app/telemetry_processor.py` (607 LOC) is currently a monolithic MLOps pipeline combining:
1. Telemetry log parsing (`feedback_store.jsonl` and `query_store.jsonl`).
2. Candidate diagnosis, entity diffing, and discrepancy categorization (171 LOC).
3. Human-in-the-Loop (HITL) card rendering into JSON and Markdown (94 LOC).
4. Candidate state machine (Approve / Reject / Disapprove) (71 LOC).
5. Corpus backup snapshotting, atomic JSON updates, and CLI parsing (164 LOC).

### B. The 3-Module Decomposition Architecture

```mermaid
flowchart TD
    CLI["CLI / Automated Telemetry Cron / HITL Admin Endpoint"] --> Processor["api/app/telemetry_processor.py\n(Coordinator & MLOps Ingestion ~150 LOC)"]
    Processor --> Diagnostic["api/app/hitl_diagnostics.py\n(Telemetry Candidate Extractor ~170 LOC)"]
    Processor --> Reporter["api/app/hitl_card_generator.py\n(Markdown & JSON Card Generator ~120 LOC)"]
    Processor --> CorpusVault["Atomic Corpus Snapshotting\n(shutil.copy2 & Backup Ingestion)"]
```

#### Module 1: `api/app/hitl_diagnostics.py` (Target: ~170 LOC)
- **Extracted Responsibility**:
  - `extract_actionable_candidates(feedbacks, queries_by_id, corpus_by_id, corpus_by_folded) -> List[Dict]`
  - `diagnose_candidate(candidate, corpus_by_id, corpus_by_folded) -> Dict`
  - Categorizes discrepancies:
    - Type 1: Diacritic Mismatches (`U+1ECB` anomalies, missing grave/acute tones).
    - Type 2: Alias Expansions (cross-dialect or diaspora variants).
    - Type 3: Missing Sovereign Parent / New Entity Proposals.

#### Module 2: `api/app/hitl_card_generator.py` (Target: ~120 LOC)
- **Extracted Responsibility**:
  - `format_hitl_markdown_card(candidate: Dict) -> str`
  - `generate_hitl_report(candidates: List[Dict], pending_json_path: Path, pending_md_path: Path) -> Tuple[Path, Path]`
  - Formats GitHub-ready Markdown review cards with diff syntax, confidence metrics, and Lead Architect review checkboxes.

#### Module 3: `api/app/telemetry_processor.py` (Lean Coordinator: Target ~150 LOC)
- **Retained Responsibility**:
  - `TelemetryProcessor` class facade and CLI command parser (`--status`, `--generate`, `--approve`, `--apply`).
  - Candidate lifecycle transitions (`approve_candidate`, `reject_candidate`).
  - Automated timestamped backup creation (`shutil.copy2`) before modifying the master corpus.
  - Atomic writing to `yoruba_corpus_1007_NORMALIZED.json`.
- **Status**: ✅ **COMPLETED (Checkpoint 062)**. Decomposed from 607 LOC down to **197 LOC**.

---

## 4. Blueprint C: `api/app/intelligence.py` Modularization & Prompt Governance

### A. Problem Statement & Functional Entanglement
[`api/app/intelligence.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/intelligence.py) currently sits at **477 LOC** (23 lines from the 500-LOC Gate 2 hard ceiling). Under our 3-Tier Pre-Commit Scanner, it is locked in **Orange Embargo Alert**.

It tangles five distinct concerns:
1. LLM Client setup, API key management, and Google GenAI SDK lifecycle (`genai.Client`).
2. Complex multi-line prompt engineering, XML boundary enforcement, and anti-jailbreak directives (Rule 5 Boundary Defense).
3. Conversational intent decomposition and stop-word normalization (`_decompose_query_intent`).
4. Fallback chat synthesis and offline knowledge generation (`_fallback_chat_synthesis`) with deep Odù Ifá liturgical texts.
5. Algorithmic multi-word phrase substitution and regex token diacritization (`_sovereign_diacritize`).

### B. The 2-Module Decomposition Architecture

```mermaid
flowchart TD
    API["/v6/chat/grounded & /v6/translate/cultural (main.py)"] --> Intelligence["api/app/intelligence.py\n(Lean Intelligence Suite ~200 LOC)"]
    Intelligence --> Governor["api/app/prompt_governor.py\n(Prompt Orchestrator & Citation Validator ~220 LOC)"]
    Intelligence --> Retriever["api/app/retrieval.py\n(Hybrid Knowledge Retrieval)"]
    Intelligence --> GenAI["Google GenAI SDK (gemini-2.5-flash)"]
    Governor --> Sanitizer["XML Boundary Sanitizer & Delimiter Defense"]
    Governor --> Intent["Multi-Turn Intent Decomposer"]
    Governor --> Citations["Grounded Citation & Hallucination Validator"]
    Governor --> Fallback["Sovereign Offline Knowledge Synthesizer"]
```

#### Module 1: `api/app/prompt_governor.py` (Target: ~220 LOC)
- **Extracted Responsibility**:
  - **System Instructions**:
    - `OGBON_SYSTEM_INSTRUCTION`: Scholarly mandate, 25-letter tonal invariants, sub-concept direct drill-down, and Rule 5 Boundary Defense.
    - `DIACRITIZER_SYSTEM_INSTRUCTION`: Polysemic word disambiguation and 25-letter orthography preservation.
    - `CULTURAL_TRANSLATION_SYSTEM_INSTRUCTION`: Deep metaphysical glossing and JSON schema constraints (`orthographic_retention`, `literal_translation`, `cultural_gloss`).
  - **Input Sanitization & XML Escaping (Gate 5 & 8 Security)**:
    - `sanitize_xml_user_input(text: str, max_chars: int = 1500, tag: str = "user_query") -> str`: Escapes delimiters (`</user_query>`, `&lt;`, `&gt;`) and trims input length.
  - **Prompt Packaging**:
    - `build_grounded_rag_prompt(retrieved_hits: List[Dict], user_message: str) -> Tuple[str, str]`: Assembles 14-Tier entity dossiers into `<canonical_knowledge_base>` and packs `<user_query>`.
  - **Conversational Intent Decomposition**:
    - `decompose_query_intent(message: str, session_history: Optional[List[Dict[str, str]]] = None) -> str`: Strips colloquial filler and normalizes monarchical / cosmological inquiries.
  - **Scholarly Citation & Grounding Validation**:
    - `validate_grounding_citations(reply_text: str, retrieved_hits: List[Dict[str, Any]]) -> Dict[str, Any]`: Verifies that cited Odù chapters, historical monarchs, or academic sources (Johnson, Abímbọ́lá, Abiodun, Lawal, Verger, Bascom, Fadipe) are present in the grounded context, logging telemetry warnings upon ungrounded drift.
  - **Sovereign Offline Knowledge Generation**:
    - `generate_fallback_chat_synthesis(query: str, hits: List[Dict[str, Any]], session_history: Optional[List[Dict[str, str]]] = None) -> str`: Pristine, zero-hallucination offline responses for Sùúrù in Ìrẹtẹ̀ Méjì, Odùduwà at Ilé-Ifẹ̀, 401 Irúnmọlẹ̀, Ọ̀rúnmìlà, and standard entity dossiers.

#### Module 2: `api/app/intelligence.py` (Lean Execution Core: Target ~200 LOC)
- **Retained Responsibility**:
  - `ÀgbàIntelligenceSuite` class facade, `genai.Client` lifecycle, API key resolution, and model configuration.
  - `chat_grounded`: Orchestrates retriever call, delegates prompt assembly and citation validation to `prompt_governor.py`, invokes GenAI with fallback.
  - `diacritize_ascii`: Orchestrates GenAI diacritization with `_sovereign_diacritize` fallback.
  - `_sovereign_diacritize`: Algorithmic phrase substitution and regex token replacement via `orthography_lexicon.py`.
  - `translate_cultural`: Orchestrates GenAI cultural translation and JSON parsing with `_fallback_translate`.
- **Headroom Reclaimed**: Slashed from **477 LOC down to ~200 LOC** (**>58% reduction; comfortably inside Green Zone < 250 LOC**).

---

## 5. Unified Backend Modularization Matrix

| File Target | Original LOC | Decomposed Modules | Target LOC Each | Total Target LOC | Gate 2 Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [`api/app/retrieval.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/retrieval.py) | **`451`** | `lexical_ranker.py`<br>`sub_variant_hydrator.py`<br>`retrieval.py` (Coordinator) | ~130 LOC<br>~95 LOC<br>~160 LOC | ~385 LOC | 🟢 All modules < 160 LOC |
| [`api/app/intelligence.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/intelligence.py) | **`477`** | `prompt_governor.py`<br>`intelligence.py` (Execution Core) | ~220 LOC<br>~200 LOC | ~420 LOC | 🟢 All modules < 220 LOC |
| [`api/app/telemetry_processor.py`](file:///home/aruna_olanrewaju/agba-engine/api/app/telemetry_processor.py) | **`607`** | `hitl_diagnostics.py`<br>`hitl_card_generator.py`<br>`telemetry_processor.py` | 170 LOC<br>120 LOC<br>197 LOC | 487 LOC | ✅ Completed (All < 200 LOC) |

---

## 6. Execution Plan & Production Safety Protocol

1. **Strictly Read-Only on Business Logic**: Neither extraction alters scoring weights, RRF math ($k=60$), prompt semantics, or citation schemas.
2. **Deterministic Parity Verification**:
   - `python3 scripts/benchmark_sprint004.py` must maintain **28/28 (100.0%) Top-1 Accuracy** across all 1,415 entities.
   - Zero-shot exact match and anti-parent-loop tests must return identical results.
3. **Automated Scanner Enforcement**: Every extracted file must pass `./scripts/review.sh` with 0 hard violations and 0 embargo alerts, bringing the entire backend into the **Green Zone (< 250 LOC)**.
