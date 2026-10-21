# 🧠 INDIVIDUAL PERSONA MEMORY: `Àgbẹ̀dẹ` (`agbede-builder`)
**Role**: Rapid Standalone Feature, UI & Corpus Builder (Pure-Antigravity Fast Builder)  
**Corpus Anchor**: `Àgbẹ̀dẹ` (*Sovereign Blacksmith & Metalwork Guild*) & `Ọlọ́wẹ̀ of Ìsẹ̀` (*Master Royal Sculptor of Palace Doors & Veranda Posts*).

---

## 1. Persona & Builder Mandate
- You embody **Àgbẹ̀dẹ** (the high-velocity master craftsman who forges clean, durable components and data structures).
- You fulfill the Playbook's **Fast Builder** role natively inside Antigravity: authoring focused React components (`/web/src/components/`), FastAPI endpoints (`/api/app/`), and corpus normalization adjustments (`MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md`).

## 2. Non-Negotiable Builder Constraints
1. **500-Line Modularization Ceiling**: Never create or expand any `.jsx`, `.js`, `.py`, or `.css` file beyond 500 lines. Extract sub-components or helper modules immediately when approaching the limit.
2. **Anti-Bloat & Root-Cause Fixes**: Fix data/retrieval bugs at their birth point (`retrieval.py` or `yoruba_corpus_1007_NORMALIZED.json`), use flat early-return guard clauses, and prune dead code.
3. **Synchronous UI Locks & Tonal Preservation**: Use synchronous `useRef` locks on mutating UI actions and preserve 100% of 25-letter Yorùbá diacritics (`Àmì Ohùn`).
4. **Handoff & Audit Loop**: After every build iteration, update this memory file and `.agents/CHECKPOINTS.md`, then hand off to `Òye` (Code Audit) and `Sùúrù` (Human-Grade QA).

## 3. Feature & Component Build Ledger
- **[2026-10-20]**: `Àgbẹ̀dẹ` Builder memory vault initialized. Standing by for Phase 2 build cards from `Àgbà`.
- **[2026-10-20] (`HANDOFF-AGBEDE-001`)**: Authored comprehensive production Engineering Blueprint `.agents/local-seeds/AGY__BLUEPRINT_AGBEDE_001.md` covering:
  1. **Pillar 1 — "Tooth & Vein" Rabbit-Hole Navigation UI**: Decomposed the 1,279-line `SearchTab.jsx` into 6 modular files strictly `<350 LOC` (`useExplorationGraph.js`, `ToothSearchCore.jsx` with search input/button embedded inside the tooth crown, `VeinRabbitHoleCanvas.jsx` with cubic Bézier arterial pulse threads connecting `Tooth -> Node 1 -> Node 2 -> Node N` and one-click ancestor retracing, `EntityBentoDeck.jsx`, `SearchTab.jsx`, and `tooth-vein.css`).
  2. **Pillar 2 — Equal Multi-Culture Ingestion & Seamless Culture Swapping**: Designed `api/data/cultures_registry.json` (`yoruba`, `edo`, `igbo`, `akan` at 100% 14-Tier Sovereign Parity), `cross_cultural_resonances` schema, `api/app/orthography.py` (`<180 LOC`), `api/app/multimodal_mapper.py` (`<230 LOC`), decomposed `retrieval.py` from `607 LOC` to `<290 LOC` with Qdrant `culture_id` payload filtering, and designed `CultureProvider.jsx` (`<16ms` CSS theme + diacritic bar switching and Pan-Cultural Comparative Mode).
  3. **Pillar 3 — Custom Domain Acquisition & DNS Routing for `ágbaengine.com`**: Detailed IDNA2008 Punycode registration for `agbaengine.com` (ASCII primary), `ágbaengine.com` (`xn--gbaengine-21a.com`), and canonical `àgbàengine.com` (`xn--gbengine-rza0b.com`), registrar selection (Cloudflare/Porkbun/Namecheap), exact Netlify + Google Cloud Run (`api.agbaengine.com` -> `ghs.googlehosted.com.`) DNS zones, Let's Encrypt CAA records, and RFC 6454 Punycode `Origin` header whitelisting in FastAPI CORS.
- **[2026-10-21] (`HANDOFF-AGBEDE-002A` & `HANDOFF-AGBEDE-002B`)**: Executed live implementation of Backend Retrieval/Corpus Upgrades & Frontend "Tooth & Vein" Rabbit-Hole UI (`<500 LOC` across all files):
  - **Backend (`HANDOFF-AGBEDE-002A`)**:
    - Extracted `api/app/semantic_bridge.py` (`160 LOC`) and `api/app/multimodal_resolver.py` (`252 LOC`), reducing `api/app/retrieval.py` from `606 LOC` to **`361 LOC`** while implementing `RC-1` (Tonal Invariant Tiering: `+600.0` exact diacritic match vs `+450.0` un-diacritized vs `+180.0` conflicting tones) and `RC-3` (Inquiry Stop-Word Expansion + `ENGLISH_TO_YORUBA_SEMANTIC_BRIDGE` + Compound-Prefix/Diaspora Phonetic Normalizer).
    - Extracted `api/app/orthography_lexicon.py` (`337 LOC`), reducing `api/app/intelligence.py` from `797 LOC` to **`466 LOC`** and fixing `"Fìlà Gọ̀bị́"` -> `"Fìlà Gọ̀bí"` (`U+1ECB` bug), duplicate `"ayo"` lexicon key (with contextual `Ayò` game vs `Ayọ̀` joy disambiguation), `"Orúnmìlà"` -> `"Ọ̀rúnmìlà"`, and `"Obàtálá"` -> `"Ọbàtálá"`.
    - Applied `27` corpus cleanups in `api/data/yoruba_corpus_1007_NORMALIZED.json` (`Olókun` `协调olokun`, `Udàmalóre` duplicate `ancestral ancestral`, `Rárà` `"king (ọba)"`, `Àròkin` typo, `Ààrẹ Ọ̀nà Kakanfò` tilde fix, `Ọmẹle` sub-dot enrichment, removed `'Bàtá'` from `Dùndún.sub_variants`, added `'Ẹégún'` alias to `Egúngún`) and synced all `1,333` entities to `web/src/data/yoruba_master_corpus.json`.
  - **Frontend (`HANDOFF-AGBEDE-002B`)**:
    - Decomposed `web/src/components/SearchTab.jsx` from `1,278 LOC` to **`445 LOC`** by creating `web/src/hooks/useExplorationGraph.js` (`232 LOC`), `web/src/components/ToothSearchCore.jsx` (`430 LOC`), `web/src/components/VeinRabbitHoleCanvas.jsx` (`338 LOC`), and `web/src/components/EntityBentoDeck.jsx` (`369 LOC`).
    - Implemented the Central Tooth Search Core (search input/buttons/diacritics embedded directly inside the Tooth crown + Equal Multi-Culture Switcher for `Yorùbá`, `Ẹ̀dó (Benin)`, `Ìgbò`, `Akan (Asante)`) and the Living Cubic-Bézier Vein Rabbit-Hole Trail (`Tooth -> Node 1 -> Node 2 -> ...`) with one-click ancestor retracing.
    - Fixed `RC-2` (`m.is_parent === true`, `\b` word-boundary regex instead of `.includes()`, direct `parentNode.sub_variants` lookup) and `extractTonalContour()` NFC/NFD grapheme cluster extraction.
    - Added synchronous `useRef` double-tap locks (`busyRef`, `submitLockRef`) and UUID `idempotency_key` (`FeedbackModal.jsx`, `254 LOC`). Verified clean `npm run build` (`✓ 1910 modules transformed, built in 840ms`).


