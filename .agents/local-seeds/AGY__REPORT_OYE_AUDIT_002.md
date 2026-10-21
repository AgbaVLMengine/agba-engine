# 🛡️ ADVERSARIAL RED-TEAM AUDIT REPORT 002 (`HANDOFF-OYE-002`)
**Auditor Persona**: `Òye` (`oye-auditor` — Deep Analytical Discernment & Root-Cause Comprehension)  
**Date**: 2026-10-21  
**Target Scope**: Post-Implementation Verification of Sprint 002 Deliverables (`HANDOFF-AGBEDE-002A`, `HANDOFF-AGBEDE-002B`, `HANDOFF-OGUN-002`)  
**Verdict**: ✅ **PASS (`100%` Compliance across all 15 Sprint 002 Created/Modified Modules)**

---

## 1. Gate 2 — 500-Line Modularization Ceiling (`100% PASS` on Sprint 002 Targets)

Every file created or refactored during Sprint 002 by `Àgbẹ̀dẹ` and `Ògún` strictly obeys the `<500 LOC` ceiling:

| File Path | Pre-Sprint 002 LOC | Post-Sprint 002 LOC | Ceiling (`<500`) | Status |
| :--- | :---: | :---: | :---: | :---: |
| `api/app/retrieval.py` | 606 | **361** | `<500` | ✅ **PASS** (`-245 LOC`) |
| `api/app/semantic_bridge.py` *(new)* | — | **160** | `<500` | ✅ **PASS** |
| `api/app/multimodal_resolver.py` *(new)* | — | **252** | `<500` | ✅ **PASS** |
| `api/app/intelligence.py` | 797 | **466** | `<500` | ✅ **PASS** (`-331 LOC`) |
| `api/app/orthography_lexicon.py` *(new)* | — | **337** | `<500` | ✅ **PASS** |
| `api/app/main.py` | 314 | **346** | `<500` | ✅ **PASS** |
| `api/app/config.py` | 228 | **244** | `<500` | ✅ **PASS** |
| `api/Dockerfile` | 35 | **58** | `<500` | ✅ **PASS** |
| `api/deploy_cloud_run.sh` *(new)* | — | **70** | `<500` | ✅ **PASS** |
| `web/src/components/SearchTab.jsx` | 1,278 | **445** | `<500` | ✅ **PASS** (`-833 LOC`) |
| `web/src/components/ToothSearchCore.jsx` *(new)* | — | **430** | `<500` | ✅ **PASS** |
| `web/src/components/VeinRabbitHoleCanvas.jsx` *(new)* | — | **338** | `<500` | ✅ **PASS** |
| `web/src/components/EntityBentoDeck.jsx` *(new)* | — | **369** | `<500` | ✅ **PASS** |
| `web/src/components/FeedbackModal.jsx` | 238 | **254** | `<500` | ✅ **PASS** |
| `web/src/hooks/useExplorationGraph.js` *(new)* | — | **232** | `<500` | ✅ **PASS** |

> **Watch Note on `./scripts/review.sh`**: When running `./scripts/review.sh` across the entire repo, 3 untouched legacy files from outside Sprint 002's scope remain `>500 LOC` (`api/app/ingest_parents.py` [2,990 LOC], `web/src/components/TranslateTab.jsx` [612 LOC], `api/app/telemetry_processor.py` [607 LOC]), plus untracked `web/node_modules/` packages if `node_modules` is present locally. None of the 15 Sprint 002 target files exceed 500 lines.

---

## 2. Gate 3 — Synchronous `useRef` Locks & UUID Idempotency (`100% PASS`)

1. **`web/src/components/SearchTab.jsx`**:
   - Declares `const busyRef = useRef(false);` (line 97).
   - Guards `executeSearch` synchronously at entry (`if (!q || busyRef.current) return; busyRef.current = true;` on lines 148–149) and releases inside `finally { busyRef.current = false; setLoading(false); }` (lines 201–203).
2. **`web/src/components/ToothSearchCore.jsx`**:
   - Declares `const submitLockRef = useRef(false);` (line 45) with synchronous entry/release inside `handleFormSubmit` (lines 75–81).
3. **`web/src/hooks/useExplorationGraph.js`**:
   - Declares `const navLockRef = useRef(false);` (line 137) and guards `startVeinFromTooth` (line 152), `branchVeinToRelative` (line 185), and `retraceToNode` (line 206) against double-click graph branching races.
4. **`web/src/components/FeedbackModal.jsx` & `api/app/main.py`**:
   - `FeedbackModal.jsx` declares `const submitLockRef = useRef(false);` (line 17), guards `handleSubmit` synchronously (`if (submitLockRef.current || submitting) return;` on line 37), and generates a cryptographic UUIDv4 key via `crypto.randomUUID()` (lines 21–29, 39) sent in both the payload (`idempotency_key`) and HTTP header (`X-Idempotency-Key`).
   - `api/app/main.py` (`FeedbackPayload`, line 127; `submit_telemetry_feedback`, lines 281–331) validates `idempotency_key`, checks `_SEEN_IDEMPOTENCY_KEYS` (hydrated on startup from `feedback_store.jsonl`), and short-circuits duplicate submissions with `{"status": "duplicate_ignored"}`.

---

## 3. Gate 4 — 4 Yorùbá Orthography Bugs Resolved (`100% PASS`)

1. **`"Fìlà Gọ̀bí"` (`U+1ECB` Elimination)**:
   - Verified in `api/app/multimodal_resolver.py` (line 127) and `api/app/orthography_lexicon.py` (line 160): non-Yorùbá `ị` (`U+1ECB`) is completely removed in favor of standard Yorùbá `"Fìlà Gọ̀bí"`. *(Residual note for future sprint: legacy `TranslateTab.jsx` line 151 still has a local copy).*
2. **Duplicate `"ayo"` Key in `SOVEREIGN_LEXICAL_BASE`**:
   - Verified in `api/app/orthography_lexicon.py` (line 187): `"ayo": "ayọ̀"` appears exactly once in `SOVEREIGN_LEXICAL_BASE`, and `disambiguate_homograph` (lines 303–306) contextually resolves `"Ayò"` (board game/seeds) vs `"Ayọ̀"` (joy/celebration).
3. **`"Ọ̀rúnmìlà"` Grounding Source Title**:
   - Verified in `api/app/intelligence.py` (line 93 & line 267): `ORUNMILA-001` now renders `"title": "Ọ̀rúnmìlà"` with proper sub-dot and low-tone grave on `Ọ̀`.
4. **`extractTonalContour(word)` NFC/NFD Grapheme Handling**:
   - Verified in `web/src/components/SearchTab.jsx` (lines 22–42): decomposes segments with `.normalize('NFD')`, tests base vowel against `'aeiouẹọ'`, inspects combining acute (`\u0301` → High `Mí ↗`) and grave (`\u0300` → Low `Dò ↘`) or defaults to Mid (`Rè →`), and returns `ch.normalize('NFC')`.

---

## 4. Gate 5 — CORS Allowlist, Telemetry Persistence & Cloud Run Free-Tier Guardrails (`100% PASS`)

1. **CORS Allowlist (`api/app/config.py` & `api/app/main.py`)**:
   - Wildcard `allow_origins=["*"]` eliminated.
   - Explicit origin allowlist configured in `config.py` (lines 166–178) and wired in `main.py` (lines 38–56) for `https://agbaengine.com`, IDN & Punycode domains (`https://ágbaengine.com`, `https://xn--gbaengine-21a.com`, `https://àgbàengine.com`, `https://xn--gbengine-rza0b.com`), `www.` variants, `localhost:5173`/`3000`, and `allow_origin_regex=r"https://.*\.netlify\.app"`.
   - Methods restricted to `["GET", "POST", "OPTIONS"]` and headers restricted to `["Content-Type", "X-API-Key", "Authorization", "Accept", "X-Idempotency-Key"]`.
2. **Cloud Run Free-Tier & `<3s` Cold-Start Guardrails (`api/Dockerfile` & `api/deploy_cloud_run.sh`)**:
   - `api/Dockerfile` pre-bakes `sentence-transformers/all-MiniLM-L6-v2` into `/app/model_cache` at build time and sets `TRANSFORMERS_OFFLINE=1` and `HF_HUB_OFFLINE=1`, guaranteeing zero-network model loading (`<3s` cold start) and single-process memory safety (`--workers 1`).
   - `api/deploy_cloud_run.sh` enforces `--min-instances 0`, `--max-instances 2`, `--memory 2Gi`, `--cpu 1`, `--concurrency 80`, `--cpu-throttling`, and `--timeout 60`.
3. **Structured Cloud Logging Telemetry (`api/app/main.py`)**:
   - Both `/v6/search` (`telemetry_type: "AGBA_QUERY_LOG"`, lines 187–197) and `/v6/telemetry/feedback` (`telemetry_type: "AGBA_FEEDBACK"`, line 319) emit structured single-line JSON with `flush=True` to stdout so Google Cloud Logging captures all telemetry across scale-to-zero lifecycles.
