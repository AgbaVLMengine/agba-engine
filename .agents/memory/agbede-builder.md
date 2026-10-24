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
- **[2026-10-21] (`HANDOFF-AGBEDE-004`)**: Executed comprehensive Category 17 Remapping, Sovereign Parents Ingestion & Dynamic Sub-Variant Hydrator:
  - **Category 17 Remapping & 140 Misclassifications**:
    - Created canonical Category 17: `Indigenous Zoology, Sacred Fauna & Wildlife` re-homing 18 standalone animal/avian/aquatic taxa (`Ẹja`, `Ẹyẹ`, `Ẹranko`, `Ìjàpá`, etc.).
    - Executed 140 entry-by-entry remappings across Categories 1–16 with zero data loss, perfectly aligning with `AGY__REPORT_OYE_TAXONOMY_AUDIT_005.md` Table 4.
  - **9 Missing Sovereign Parents & 6 Sub-Variants Ingested**:
    - Ingested 9 canonical Sovereign Parents with rich 14-tier schemas: `Ifá`, `Were Music`, `Oogun` (Property/Inheritance), `Òògùn` (Pharmacology/Medicine), `Ẹ̀pà` (Groundnut/Legume), `Àpáta` (Inselberg Topography), `Ẹlẹ́mù` (Palm Wine Tapper Guild), `Ẹégún` (Ancestral Masquerades), `Ìwọ̀fà` (Pre-colonial Labor Covenant).
    - Disambiguated `Àpáta (Shield)` (`Àpáta_Shield`), cleared `Ẹégún` alias collision from `Egúngún`, and diacritized `Ofada` -> `Ọ̀fàdà`.
    - Ingested 6 dedicated standalone records for critical sub-variants: `Àrọ̀kọ̀ Ẹfà (Love)`, `Àrọ̀kọ̀ Ẹ̀jọ́ (Dispute)`, `Ọ̀kọ̀ Ẹlẹ́ṣin`, `Ọfà Ọdẹ`, `Àdá Ìbílẹ̀`, `Idà Agẹmọ`. Total corpus: 1,347 entries synced across API and Web.
  - **Zero-Hardcoded Dynamic Sub-Variant Fallback Hydrator**:
    - Built `web/src/utils/subVariantHydrator.js` (`107 LOC`) and integrated into `web/src/components/SearchTab.jsx` (`460 LOC`) and `api/app/retrieval.py` (`470 LOC`).
    - When a query or click matches an unindexed string in any Sovereign Parent's `sub_variants` list, dynamically synthesizes the child node inheriting category and craftsmanship, set `is_parent: false`, `sovereign_parent: parent.title`, and injects at Rank #1 (`fusion_score: 1.0`). Parent loop permanently eliminated (`loop: False` across 100% of tested pairs).
  - **Bilateral Knowledge Graph Wiring**:
    - Explicitly wired bilateral relations for `Apẹja` ↔ `Ẹja` ↔ `Ọkọ̀ Ojú Omi` ↔ `Odò Ọ̀ṣun` ↔ `Olókun`; `Idà` ↔ `Àdá` ↔ `Ọ̀kọ̀` ↔ `Ọfà` ↔ `Ògún`; and `Ẹyẹ` ↔ `Àwọn Ìyá Mi` ↔ `Odídẹrẹ́` ↔ `Adé`.
  - **Verification & Industry Standards**:
    - Passed `./scripts/review.sh` (0 hard violations across all Production Gates).
    - Passed `npm run build` (Vite bundle built in 1.09s with zero errors).
    - Validated Batteries X-1 (9/9 Sovereign Parents), X-2 (12/12 Anti-Loop Sub-Variants), and X-3 (10/10 Homograph Guards).
- **[2026-10-24]**: Formally relayed Four New UI Prototype Ideas to `Àgbà` (`agba-pa-architect`) for architectural review and greenlight per Lead Architect's inquiry:
  1. **"Àkọsílẹ̀" Citational Provenance Drawer** in `EntityBentoDeck.jsx` (surfacing the 281+ backfilled primary academic sources: Johnson 1921, Smith 1988, Akintoye 1971, Abiodun 2014, Lawal 1996, Verger 1995).
  2. **Living Sub-Variant "Constellation Grid"** beneath Sovereign Parents in `SearchTab.jsx` (one-click sub-vein visual expansion).
  3. **Visual Tonal Contour & Melodic Pitch Waveform** in `ToothSearchCore.jsx` / `TranslateTab.jsx` (visual High/Mid/Low pitch line over syllables).
  4. **Ancestral Journey Exporter (Study Syllabus)** for vein exploration trails (exportable/shareable cultural journey summary).
  - Confirmed web client builds in 1.21s (`npm run build` — 1,912 modules, 0 errors). Stood by for authorization to begin forging.



