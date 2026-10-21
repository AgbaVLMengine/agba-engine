# 🛡️ ADVERSARIAL RED-TEAM CODE & STANDARDS AUDIT REPORT (`AGY__REPORT_OYE_AUDIT_001`)

> **Auditor**: **`Òye`** (`oye-auditor` — Adversarial Code Audit & Industry Standards Enforcer)  
> **Corpus Anchor**: `Òye` & `Ojú-Inú` (*Rowland Abiodun 2014* — Deep Analytical Discernment, Inner Vision & Root-Cause Comprehension)  
> **Directive**: `HANDOFF-OYE-001`  
> **Timestamp**: `2026-10-21T00:55:00+01:00`  
> **Audit Mode**: Strictly Read-Only on `/api/app/` and `/web/src/`  
> **Automated Gate Scanner (`./scripts/review.sh`)**: 🚨 **FAILED (`6 Hard Violations` on Gate 2 500-LOC Ceiling; `18` Additional Architectural/Security Findings Across Gates 1, 3, 4, 5)**

---

## Executive Audit Verdict

Under the lens of **Ojú-Inú** (*inner analytical vision that pierces surface appearances to expose structural root causes*), the Àgbà Engine v6.1.0 codebase demonstrates strong cultural reverence and a solid tri-modal hybrid retrieval foundation, **but fails Production Readiness across 5 of the 6 Production Gates**:

| Production Gate | Status | Critical / High Findings | Summary Verdict |
| :--- | :--- | :--- | :--- |
| **Gate 1: Anti-Bloat, Root-Cause & Flat Guard Clauses** | 🔴 **FAIL** | 5 High | Massive DRY duplication between Python (`intelligence.py`) and JS (`TranslateTab.jsx`, `ChatTab.jsx`); dead Vite boilerplate (`App.css`); redundant imports (`os`, `re`) inside methods; hardcoded host paths in CLI scripts. |
| **Gate 2: 500-Line Modularization Ceiling** | 🔴 **FAIL** | 6 Hard Violations | `ingest_parents.py` (**2,990 LOC**), `SearchTab.jsx` (**1,278 LOC**), `intelligence.py` (**797 LOC**), `TranslateTab.jsx` (**612 LOC**), `telemetry_processor.py` (**607 LOC**), `retrieval.py` (**606 LOC**). `index.css` is at **482 LOC** (96.4% of ceiling). |
| **Gate 3: Synchronous `useRef` Locks & UUID Idempotency** | 🔴 **FAIL** | 4 Critical | **Zero (`0`) `useRef` locks** exist anywhere in `/web/src/`. All mutating/async handlers rely on async `useState` booleans (`loading`, `submitting`, `diacritizing`, `translating`, `isProcessing`), exposing 15–50ms double-tap race windows. `FeedbackModal.jsx` uses `hitl_${Date.now()}` instead of a UUIDv4 `idempotency_key`, and `/v6/telemetry/feedback` performs un-deduplicated file appends. |
| **Gate 4: 25-Letter Yorùbá Tonal Invariant & Cosmology** | 🟡 **WARN** | 4 Medium/High | Subtle Unicode bugs: `Fìlà Gọ̀bị́` uses Igbo/Vietnamese `ị` (`U+1ECB`) instead of Yorùbá `í` (`U+00ED`) across 3 files; `SOVEREIGN_LEXICAL_BASE` has duplicate key `"ayo"` overwriting `"ayọ̀"` (joy) with `"ayò"` (game); `extractTonalContour()` in `SearchTab.jsx` fails on precomposed/decomposed `Ẹ́/Ẹ̀/Ọ́/Ọ̀` graphemes; `ORUNMILA-001` missing sub-dot in `"Orúnmìlà"`. |
| **Gate 5: OWASP / API Security, CORS & Secret Hygiene** | 🔴 **FAIL** | 6 Critical/High | Wildcard CORS `allow_origins=["*"]` combined with `allow_credentials=True` in `main.py`; hardcoded API keys in `config.py` and client-side JS bundles; `AdminTab.jsx` client-side auth bypass via any string starting with `'ghp_'`; fake client-side key validation in `SearchTab.jsx`; DOM XSS sink in `GalleryTab.jsx`; unenforced `rate_limit_rpm`. |
| **Gate 6: Lean Commits & Artifact Hygiene** | 🟢 **PASS** | 0 Violations | Zero `.sql.gz`, `.dump`, `.tar.gz`, or `.zip` archive pollution detected by `./scripts/review.sh`. (Note: 2,990-line inline JSON in `ingest_parents.py` should live in `/data/` JSON, not `.py` code). |

---

## Gate 1: Anti-Bloat, Root-Cause Resolution & Flat Guard Clauses

### 1.1 Massive Cross-Stack DRY Violations (Dual-Maintenance Trap)
- **Orthographic Lexicon Duplication**: `RAW_SOVEREIGN_MULTI_WORD_PHRASES` (165 tuples), `SOVEREIGN_LEXICAL_BASE` (~160 words), and `disambiguate_homograph()` in [intelligence.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py#L28-L340) are copy-pasted almost verbatim into [TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L6-L278) (`RAW_MULTI_WORD_PHRASES`, `DIACRITIC_LEXICON`, `disambiguateClientHomograph`). Any linguistic fix in Python silently drifts from the JS client unless manually patched in both places.
- **RAG Fallback Duplication**: The hardcoded scholar answers (`OGBON_PERSONA_RESPONSE`, `first ooni`, `how many orisha`, `orunmila`, `patience / suuru`) in [intelligence.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py#L343-L594) are duplicated verbatim inside [ChatTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L21-L143) (`synthesizeLocalScholarResponse`).
- **Lexical Search Duplication**: [SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx#L110-L163) (`searchRankedCorpus`) re-implements [retrieval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/retrieval.py#L334-L429) (`search_lexical`) with diverging weights (+600/+500/+200 in JS vs +500/+450/+250 in Python).

### 1.2 Dead Files, Unused Imports & Redundant In-Function Imports
- **Dead Vite Boilerplate ([App.css](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/App.css#L1-L185))**: `web/src/App.css` (184 lines) contains default Vite starter styles (`.counter`, `.hero`, `.vite`, `#next-steps`) and is **never imported anywhere** in `web/src/`. Delete it outright (-184 LOC).
- **Redundant In-Method Standard Library Imports**:
  - [retrieval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/retrieval.py#L339) re-imports `import re` inside `search_lexical()` even though `import re` is already at line 15.
  - [retrieval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/retrieval.py#L505) re-imports `import os` inside `_resolve_multimodal_links()` even though `import os` is already at line 14.
- **Unused Imports Across Python & React**:
  - [main.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L11-L13): `Path` and `Header` are imported but never used.
  - [embed_visual_corpus.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/embed_visual_corpus.py#L9-L15): `os`, `sys`, `struct`, `Tuple` are imported but never used. Furthermore, `projection_head = AgbaVisionProjectionHead(VAULT_PROJ_PATH)` is instantiated at [line 157](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/embed_visual_corpus.py#L157) inside `generate_batch_visual_embeddings()`, **but `projection_head.project()` is never called**—it writes raw `extract_lightweight_visual_descriptor()` byte histograms instead!
  - [SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx#L3-L5): `Compass`, `ExternalLink`, and `AlertTriangle` are imported from `lucide-react` but never rendered.
  - [ChatTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L2): `Bot`, `AlertCircle`, and `Compass` are imported from `lucide-react` but never rendered; `prevMessages` parameter in `synthesizeLocalScholarResponse(userQuestion, prevMessages)` ([line 21](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L21)) is unused.
  - [TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L2): `Check` and `Sparkles` are imported but never rendered.
  - [GalleryTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/GalleryTab.jsx#L2): `Search`, `Eye`, `Compass`, `Award` are imported but never rendered.
  - [AdminTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/AdminTab.jsx#L2): `RefreshCw`, `AlertTriangle`, `Database`, `Sparkles`, and prop `apiBaseUrl` ([line 48](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/AdminTab.jsx#L48)) are unused.
  - [ArchitectureTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ArchitectureTab.jsx#L2): `ShieldCheck`, `Database`, `Sparkles`, `Layers`, `FileCode` are imported but never rendered.

### 1.3 Hardcoded Host Paths Bypassing `ÀgbàConfig`
- [apply_hitl_visual_approval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/apply_hitl_visual_approval.py#L15) hardcodes `ROOT_DIR = Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine")` instead of using `ÀgbàConfig.ROOT_DIR`.
- [backfill_tier14.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/backfill_tier14.py#L23-L24) hardcodes `/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/...` and `MODEL_ID = "gemini-3.8-flash"` (non-existent model ID).
- [telemetry_processor.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/telemetry_processor.py#L356-L360) hardcodes `/home/aruna_olanrewaju/.gemini/antigravity-ide/brain/ef901e36-5592-4a8c-8b6d-ba3081572a24/...`.

---

## Gate 2: The 500-Line Component & Module Ceiling

### 2.1 Complete Line-Count Inventory (`wc -l`)

| File Path | Exact Lines (`wc -l`) | Ceiling (`500`) | Status |
| :--- | :---: | :---: | :--- |
| [api/app/ingest_parents.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/ingest_parents.py) | **2,990** | 500 | ❌ **VIOLATION (+2,490 LOC)** |
| [web/src/components/SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx) | **1,278** | 500 | ❌ **VIOLATION (+778 LOC)** |
| [api/app/intelligence.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py) | **797** | 500 | ❌ **VIOLATION (+297 LOC)** |
| [web/src/components/TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx) | **612** | 500 | ❌ **VIOLATION (+112 LOC)** |
| [api/app/telemetry_processor.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/telemetry_processor.py) | **607** | 500 | ❌ **VIOLATION (+107 LOC)** |
| [api/app/retrieval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/retrieval.py) | **606** | 500 | ❌ **VIOLATION (+106 LOC)** |
| [web/src/index.css](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/index.css) | **482** | 500 | ⚠️ **NEAR CEILING (96.4%)** |
| [web/src/components/AdminTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/AdminTab.jsx) | **414** | 500 | ✅ PASS (82.8%) |
| [api/app/ingest_visual_corpus.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/ingest_visual_corpus.py) | **363** | 500 | ✅ PASS |
| [web/src/components/ChatTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx) | **310** | 500 | ✅ PASS |
| [web/src/components/GalleryTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/GalleryTab.jsx) | **305** | 500 | ✅ PASS |
| [api/app/main.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py) | **297** | 500 | ✅ PASS |
| [web/src/components/FeedbackModal.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/FeedbackModal.jsx) | **238** | 500 | ✅ PASS |
| [api/app/config.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/config.py) | **231** | 500 | ✅ PASS |
| [api/app/embed_visual_corpus.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/embed_visual_corpus.py) | **220** | 500 | ✅ PASS |
| [api/app/apply_hitl_visual_approval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/apply_hitl_visual_approval.py) | **194** | 500 | ✅ PASS |
| [api/app/backfill_tier14.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/backfill_tier14.py) | **184** | 500 | ✅ PASS |
| [web/src/App.css](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/App.css) | **184** | 500 | 🗑️ DEAD FILE (Delete) |
| [web/src/components/ArchitectureTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ArchitectureTab.jsx) | **183** | 500 | ✅ PASS |
| [web/src/components/Navbar.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/Navbar.jsx) | **116** | 500 | ✅ PASS |
| [api/app/ingest_vectors.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/ingest_vectors.py) | **95** | 500 | ✅ PASS |
| [web/src/App.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/App.jsx) | **80** | 500 | ✅ PASS |
| [api/app/__init__.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/__init__.py) | **17** | 500 | ✅ PASS |
| [web/src/main.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/main.jsx) | **10** | 500 | ✅ PASS |
| **TOTAL** | **10,813** | — | **6 Violations** |

### 2.2 Mandatory Modular Extraction Plan for `Àgbẹ̀dẹ` (`agbede-builder`)
1. **`api/app/ingest_parents.py` (2,990 → ~75 LOC)**: Extract the 2,900-line `PARENTS_DATA` array into `api/data/sovereign_parents_81.json` and load via `json.load()`.
2. **`web/src/components/SearchTab.jsx` (1,278 → 4 modules <320 LOC each)**:
   - `ToothSearchCore.jsx` (Hero, sculpted tooth search input, `Àmì Ohùn` toolbar, curated anchors)
   - `VeinRabbitHoleCanvas.jsx` + `useExplorationGraph.js` (Branching vascular SVG/Canvas root network & rabbit-hole history)
   - `BentoEntityCanopy.jsx` (6-cell Bento grid + 14-Tier Knowledge Graph accordion + related variants)
   - `EnterpriseAudioModal.jsx` (Gated acoustic cell modal)
3. **`api/app/intelligence.py` (797 → 3 modules <300 LOC each)**:
   - `api/app/orthography.py` (25-letter diacritizer, greedy phrase table, lexical base, homograph disambiguator)
   - `api/app/ogbon_rag.py` (`ÀgbàIntelligenceSuite.chat_grounded`, query intent decomposer, sovereign fallbacks)
   - `api/app/cultural_translator.py` (`translate_cultural` and corpus gloss synthesis)
4. **`web/src/components/TranslateTab.jsx` (612 → 2 modules <280 LOC each)**:
   - Extract `RAW_MULTI_WORD_PHRASES`, `DIACRITIC_LEXICON`, and `restoreDiacriticsAlgorithmic` into `web/src/utils/yorubaOrthography.js` (~290 LOC) and keep `TranslateTab.jsx` pure UI (~310 LOC).
5. **`api/app/telemetry_processor.py` (607 → 2 modules <320 LOC each)**:
   - Split candidate extraction/diagnosis (`telemetry_diagnostics.py`) from HITL Markdown/commit sync (`telemetry_processor.py`).
6. **`api/app/retrieval.py` (606 → 2 modules <320 LOC each)**:
   - Extract `_map_call_and_response_audio`, `_map_image_assets`, and `_resolve_multimodal_links` into `api/app/multimodal_resolver.py` (~260 LOC), keeping `retrieval.py` focused on dense/lexical search + RRF fusion (~340 LOC).

---

## Gate 3: Synchronous `useRef` UI Double-Tap Locks & UUID Idempotency

### 3.1 Complete Absence of `useRef` Synchronous Locks in `/web/src/`
A full AST/grep inspection of `/web/src/` confirms **`useRef` is not imported or used in a single React component**. Every mutating or network-triggering action relies solely on asynchronous React state (`useState`), which does not update until the next render tick—allowing rapid double-clicks or Enter+Click to fire duplicate concurrent requests:
- [FeedbackModal.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/FeedbackModal.jsx#L14-L55) (`handleSubmit`): Checks neither `submitting` nor a `useRef` lock at the top of `handleSubmit`! Even if `disabled={submitting}` is on the button, pressing Enter or double-tapping before React re-renders dispatches duplicate POSTs to `/v6/telemetry/feedback`.
- [SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx#L165-L215) (`executeSearch`): Does not guard `if (isSearchingRef.current) return;` at entry; clicking curated pills, root pods, or "Discover" rapidly fires overlapping fetches that race to call `setResults()`.
- [ChatTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L145-L194) (`handleSend`): Uses `if (!input.trim() || loading) return;` via async `loading` state instead of a synchronous `sendingRef.current` lock.
- [TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L375-L425) (`handleDiacritize`, `handleCulturalTranslate`): Uses async `diacritizing` / `translating` state instead of synchronous `useRef` locks.
- [AdminTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/AdminTab.jsx#L104-L120) (`handleTriggerBatchLearning`): Checks `approvedCount === 0` but does not even check `if (isProcessing) return;` inside the handler body, nor does it use a `useRef` lock.

### 3.2 Missing UUID `idempotency_key` on Telemetry & Feedback Mutations
- **Client-Side Timestamp Collision ([FeedbackModal.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/FeedbackModal.jsx#L19-L26))**:
  - Generates `query_id: \`hitl_${Date.now()}\`` instead of `crypto.randomUUID()`, and includes **no `idempotency_key` field**.
- **Server-Side Un-Deduplicated Append ([main.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L78-L85) & [L179-L206](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L179-L206))**:
  - `FeedbackPayload` lacks an `idempotency_key: str = Field(...)` field.
  - `submit_telemetry_feedback` blindly opens `FEEDBACK_STORE_PATH` in `"a"` mode and writes every retry/double-tap as a new JSONL line without checking whether `idempotency_key` (or `query_id`) has already been recorded.

---

## Gate 4: 25-Letter Yorùbá Tonal Invariant & Sacred Cosmology Reverence

### 4.1 Foreign Unicode Character Contamination (`ị` U+1ECB in `Fìlà Gọ̀bị́`)
- Across **three files**—[retrieval.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/retrieval.py#L246), [intelligence.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py#L174), and [TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L151)—the canonical cap `Fìlà Gọ̀bí` is spelled `"Fìlà Gọ̀bị́"` using **`ị` (`U+1ECB`, Latin Small Letter I with Dot Below)** plus combining acute accent.
- **Root Cause**: The 25-letter Yorùbá alphabet (`A B D E Ẹ F G GB H I J K L M N O Ọ P R S Ṣ T U W Y`) only has sub-dots on **`Ẹ/ẹ`**, **`Ọ/ọ`**, and **`Ṣ/ṣ`**. There is **no sub-dotted `ị`** in Yorùbá orthography (`ị` belongs to Igbo/Vietnamese). It must be normalized to **`Fìlà Gọ̀bí`**.

### 4.2 Duplicate Dictionary Key Overwrite in `SOVEREIGN_LEXICAL_BASE` (`"ayo"`)
- In [intelligence.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py#L204) (`"ayo": "ayọ̀"`, joy) and [line 266](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py#L266) (`"ayo": "ayò"`, traditional board game), `"ayo"` is defined twice in the same dictionary literal!
- Identical bug in [TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L179) and [line 240](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L240).
- **Consequence**: Python and JS silently overwrite `"ayọ̀"` (joy) with `"ayò"` (board game), causing `diacritize_ascii` to corrupt general sentences containing `ayo` unless matched by an earlier multi-word phrase, instead of routing `"ayo"` through `disambiguate_homograph()`.

### 4.3 Broken Decomposed Grapheme Iteration in `extractTonalContour()`
- In [SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx#L48-L62), `extractTonalContour(word)` iterates `for (const ch of syllables)` and checks `'áéẹ́íóọ́úÁÉẸ́ÍÓỌ́Ú'.includes(ch)` and `'aeiouAEIOU'.includes(ch)`.
- **Root Cause**: In Unicode, `ẹ́`, `ẹ̀`, `ọ́`, `ọ̀` do **not** exist as single precomposed code points! Even under `NFC`, `ẹ́` is two code points: `ẹ` (`U+1EB9`) + `\u0301` (Combining Acute Accent). Thus, iterating `for (const ch of syllables)` visits `ẹ` first (which is not in `'aeiouAEIOU'` and has no tone mark attached) and then visits `\u0301` alone (which matches `'áéẹ́...'` because the string literal itself contains `\u0301`!), pushing a disembodied combining mark `{ char: '\u0301', pitch: 'High (Ó)' }` into the UI badge! Furthermore, mid-tone `ẹ` (`U+1EB9`) and `ọ` (`U+1ECD`) are completely omitted from `'aeiouAEIOU'`.

### 4.4 Missing Sub-Dot on `Ọ̀rúnmìlà` in Grounding Citations
- In [intelligence.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py#L410) and [ChatTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L39) & [L72](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L72), the grounding source title is written `"Orúnmìlà"` (missing both the grave accent and the sub-dot on `Ọ̀`) instead of canonical **`"Ọ̀rúnmìlà"`**.

---

## Gate 5: OWASP / API Security, FastAPI CORS Policy, Rate-Limiting & Secret Hygiene

### 5.1 Wildcard CORS with Credentials ([main.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L38-L44)) — **HIGH (OWASP A05:2021 Security Misconfiguration)**
- `app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])` violates the W3C Fetch/CORS specification and OWASP API8. Production origins must be restricted to an explicit allowlist (`https://àgbàengine.com`, `https://agbaengine.com`, Netlify deploy previews, and `http://localhost:5173`).

### 5.2 Hardcoded API Keys in Source & Client Bundle — **CRITICAL (OWASP A07:2021 / A02:2021)**
- [config.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/config.py#L168-L205) hardcodes plaintext API keys (`"agba_studio_dev_key_2026"`, `"agba_enterprise_demo_key"`, `"agba_academic_research_key"`).
- [main.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L63-L64) contains a redundant hardcoded backdoor check `if key == "agba_studio_dev_key_2026": return ...` using non-constant-time `==` comparison (instead of `secrets.compare_digest`).
- [SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx#L178), [ChatTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ChatTab.jsx#L159), [TranslateTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/TranslateTab.jsx#L385), and [FeedbackModal.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/FeedbackModal.jsx#L33) hardcode `'X-AGBA-API-KEY': 'agba_studio_dev_key_2026'` (the highest `Studio` tier key with `export_dossier` permissions!) directly into the public browser bundle.
- [ingest_visual_corpus.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/ingest_visual_corpus.py#L263) hardcodes `api_key=DEMO_KEY` in the Smithsonian API URL.

### 5.3 Client-Side Authentication Bypass in `AdminTab.jsx` & `SearchTab.jsx` — **CRITICAL (OWASP A01:2021 Broken Access Control)**
- In [AdminTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/AdminTab.jsx#L65), `if ((envPasscode && entered === envPasscode) || (entered && entered.startsWith('ghp_')))` grants full HITL Admin Console access in the browser to **any user who types the 4 characters `ghp_`**. Furthermore, `VITE_ARCHITECT_PASSCODE` is bundled into plaintext client JS at build time.
- In [SearchTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx#L1239-L1242), clicking "Verify Key" on the restricted Enterprise Audio Modal runs `if (apiKeyInput.trim()) { setApiKeySuccess(true); }`—accepting literally **any non-empty string** without calling the backend!

### 5.4 Unenforced Rate Limits & Unbounded Input Payloads — **HIGH (OWASP API4:2023 Unrestricted Resource Consumption)**
- While [config.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/config.py#L172) defines `"rate_limit_rpm": 300 / 120 / 60`, **no rate-limiting middleware or token bucket exists in `main.py`**.
- `QueryRequest`, `FeedbackPayload`, `ChatRequest`, `DiacritizeRequest`, and `CulturalTranslateRequest` in [main.py](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L72-L85) & [L257-L266](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py#L257-L266) have **no `max_length` constraints** on `str` or `List` fields, allowing multi-megabyte payloads to exhaust Gemini tokens, regex CPU (`_sovereign_diacritize`), or disk space (`feedback_store.jsonl`).

### 5.5 Direct DOM `innerHTML` Mutation in `GalleryTab.jsx` — **LOW/MEDIUM (DOM XSS Sink)**
- [GalleryTab.jsx](file:///home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/GalleryTab.jsx#L122) mutates `e.target.parentNode.innerHTML = '<div ...>👑</div>'` inside `onError`. In React, mutating `parentNode.innerHTML` corrupts React's virtual DOM fiber reconciliation and introduces an unsafe DOM sink pattern.

---

## Gate 6: Prioritized Remediation Roadmap for `Àgbẹ̀dẹ` & `Irin`

1. **[P0 — Gate 2 Modularization]**: Split the 6 files exceeding 500 LOC (`ingest_parents.py`, `SearchTab.jsx`, `intelligence.py`, `TranslateTab.jsx`, `telemetry_processor.py`, `retrieval.py`) and delete dead `web/src/App.css` so `./scripts/review.sh` exits `0`.
2. **[P0 — Gate 3 Concurrency & Idempotency]**: Add `useRef` synchronous locks (`inFlightRef.current`) to all 5 interactive React components and add `idempotency_key: str = Field(..., min_length=8, max_length=64)` (UUIDv4) to `FeedbackPayload` with server-side deduplication in `main.py`.
3. **[P0 — Gate 4 Orthography Fixes]**: Replace `Fìlà Gọ̀bị́` (`U+1ECB`) with `Fìlà Gọ̀bí`, remove the duplicate `"ayo"` key in `SOVEREIGN_LEXICAL_BASE` (move `ayo` to `disambiguate_homograph`), fix `"Orúnmìlà"` -> `"Ọ̀rúnmìlà"`, and refactor `extractTonalContour()` to normalize to `NFD` and group base Yorùbá vowels (`a e ẹ i o ọ u`) with their combining tone marks (`\u0300`, `\u0301`).
4. **[P1 — Gate 5 Security Hardening]**: Remove the `'ghp_'` bypass in `AdminTab.jsx`, move API key validation and rate-limiting (`rate_limit_rpm`) to FastAPI middleware using `secrets.compare_digest`, add `max_length` bounds to all Pydantic models, and lock down CORS `allow_origins` to canonical domains (`https://àgbàengine.com`, `https://agbaengine.com`, `https://ágbaengine.com`).
