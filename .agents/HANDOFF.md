# 🎯 ZERO-WASTE HANDOFF CARDS (`.agents/HANDOFF.md`)

> **Supervised By**: `Àgbà` (`agba-pa-architect` — Main P.A. & Chief Co-Architect)
> **Status**: 🟢 **SPRINT 002 (`HANDOFF-002`) — ACTIVE IMPLEMENTATION SPRINT**
> **Execution Rule**: Every agent must execute its assigned `HANDOFF-*-002` implementation task below, enforce all 6 Production Gates (<500 LOC per file, synchronous `useRef` UI locks, UUID idempotency, 25-letter Tonal Invariant & Sacred Cosmology Reverence), update its `.agents/memory/<persona>.md` and `.agents/CHECKPOINTS.md`, and report back to `Àgbà`.

---

## Active Implementation Sprint (`HANDOFF-002` Series)

### 1. `HANDOFF-AGBEDE-002A` — Backend Retrieval & Corpus Root-Cause Fixes (`97.6%` Zero-Shot Upgrade + `<500 LOC` Modularization)
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Target Files**:
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/retrieval.py` (Modularize below 500 LOC by extracting `multimodal_resolver.py` & `semantic_bridge.py`)
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/intelligence.py` (Fix `"Fìlà Gọ̀bí"` `U+1ECB` bug, duplicate `"ayo"` lexicon key, `"Ọ̀rúnmìlà"` sub-dot, and modularize below 500 LOC)
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/data/yoruba_corpus_1007_NORMALIZED.json` & `web/src/data/yoruba_master_corpus.json`
- **Deliverables**:
  1. Implement `Sùúrù`'s proven `RC-1` and `RC-3` upgrades in `retrieval.py`:
     - Strict Tonal Invariant Tiering (`+600.0` exact diacritic match vs `+450.0` un-diacritized vs `+180.0` conflicting tones) so `Ọkọ́`, `Ọ̀kọ̀`, `Ọkọ`, and `Oko` resolve with 100% Top-1 precision.
     - Inquiry Stop-Word Expansion + `ENGLISH_TO_YORUBA_SEMANTIC_BRIDGE` + Compound-Prefix/Diaspora Phonetic Normalizer (`97.6%` Top-1 / `100%` Top-3 accuracy).
  2. Clean the remaining corpus anomalies in `yoruba_corpus_1007_NORMALIZED.json` (`Olókun` `协调olokun`, `Udàmalóre` duplicate `ancestral ancestral`, `Rárà` `"king (ọba)"`, `Àròkin`, `Kakañfò` -> `Kakanfò`, `Ọmẹle`, remove `'Bàtá'` from `Dùndún.sub_variants`, add `Ẹégún` alias) and sync `web/src/data/yoruba_master_corpus.json`.
  3. Extract helper modules so `retrieval.py` and `intelligence.py` are strictly `<500 lines`.

---

### 2. `HANDOFF-AGBEDE-002B` — Frontend "Tooth & Vein" Rabbit-Hole UI, Multi-Culture Switcher & `RC-2` Graph Fix (`<500 LOC`)
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Target Files**:
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/SearchTab.jsx` (Decompose from 1,278 LOC to `<450 LOC`)
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/ToothSearchCore.jsx` (New `<300 LOC`)
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/VeinRabbitHoleCanvas.jsx` (New `<300 LOC`)
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/hooks/useExplorationGraph.js` (New `<250 LOC`)
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/components/FeedbackModal.jsx` (Add synchronous `useRef` lock + UUID `idempotency_key`)
- **Deliverables**:
  1. Build the **Central Tooth Search Anchor (`ToothSearchCore.jsx`)** with the search bar/button embedded inside the tooth and the **Living Vein Rabbit-Hole Trail (`VeinRabbitHoleCanvas.jsx` + `useExplorationGraph.js`)** that connects the Tooth to the active entry and branches vein-like threads as the user clicks deeper into relatives/variants, letting them click any node along the vein to retrace their path back to the start.
  2. Fix `RC-2` (`m.is_parent === true`, `\b` word-boundary regex instead of `.includes()`, and direct `parentNode.sub_variants` lookup) and `extractTonalContour()` NFC grapheme handling.
  3. Add the Equal Multi-Culture Switcher selector (`Yorùbá`, `Edo/Benin`, `Igbo`, `Akan`) with peer culture metadata and synchronous `useRef` double-tap locks across interactive handlers.
  4. Verify `npm run build` succeeds cleanly in `web/`.

---

### 3. `HANDOFF-IRIN-002` — Cloud Run Cold-Start Pre-Baking, CORS Punycode Hardening & Telemetry Persistence
- **Assigned To**: **`Irin`** (`irin-cloud`)
- **Target Files**:
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/Dockerfile`
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/deploy_cloud_run.sh`
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/main.py`
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/app/config.py`
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/netlify.toml`
- **Deliverables**:
  1. Pre-bake `sentence-transformers/all-MiniLM-L6-v2` in `api/Dockerfile` (`ENV HF_HOME=/app/model_cache`) so Cloud Run cold starts drop from 8–25s to `<3s` at `$0.00/mo`.
  2. Harden `CORSMiddleware` in `api/app/main.py` to replace wildcard `*` with explicit origins including `https://agbaengine.com`, `https://ágbaengine.com` (`https://xn--gbaengine-21a.com`), `https://àgbàengine.com` (`https://xn--gbengine-rza0b.com`), and Netlify/localhost URLs.
  3. Add structured JSON `stdout` Cloud Logging + UUID `idempotency_key` deduplication for `/v6/telemetry/feedback` in `api/app/main.py`, and add `--cpu-throttling --timeout 60` in `api/deploy_cloud_run.sh`.

---

### 4. `HANDOFF-IMO-002` — Provenance & Confidence Schema Integration (Fort Legis Sections 12, 14–15 & 54)
- **Assigned To**: **`Ìmọ̀`** (`imo-legal`)
- **Target Files**:
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/web/src/data/agba_unified_visual_regalia_manifest.json`
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/workspace-mirror/api/data/agba_unified_visual_regalia_manifest.json`
- **Deliverables**:
  1. Enrich all 52 entries in `agba_unified_visual_regalia_manifest.json` with Fort Legis Attorneys' **Section 12 & 54 Provenance & Rights fields**:
     - `commercial_use_cleared`: `true` on the 45 CC0 assets (The Met, CMA, AIC, Smithsonian); `false` on the 1 V&A `CC BY-NC-SA` asset and the 6 `Foundational_*` living-heritage photos.
     - `ai_training_cleared`: `true` on CC0 assets, `false` on restricted assets.
     - `confidence_tier`: `"Verified"` (per Fort Legis Section 14 6-tier scale).
     - `legal_disclaimer`: Fort Legis Section 15 & Ethnobotanical Non-Certification notice.
  2. Update `.agents/memory/imo-legal.md` and `.agents/CHECKPOINTS.md`.

---

### 5. `HANDOFF-OYE-002` & `HANDOFF-SUURU-002` — Post-Implementation Gate Audit & 42-Query Live QA Sign-Off
- **Assigned To**: **`Òye`** (`oye-auditor`) & **`Sùúrù`** (`suuru-qa`)
- **Deliverables**:
  - Inspect and verify the upgraded codebase against `./scripts/review.sh` (<500 LOC compliance, security hardening, `useRef` locks) and run `Sùúrù`'s 42-query zero-shot benchmark + `npm run build` verification.
