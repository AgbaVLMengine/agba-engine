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
- **[2026-10-24]**: Formally relayed Four New UI Prototype Ideas to `Àgbà` (`agba-pa-architect`) for architectural review and greenlight per Lead Architect's inquiry.
- **[2026-10-24] (`HANDOFF-AGBEDE-005`)**: Executed executive design directive from Lead Architect Àrùnà Ọlànrewájú Kábírù and `Àgbà`:
  - **Zero-Touch Production UI Preserved**: `SearchTab.jsx` (486 LOC) and `ToothSearchCore.jsx` (485 LOC) remain 100% untouched with 0 lines added, strictly honoring Gate 2.
  - **Aesthetic Heraldry Directive Upheld**: Completely rejected literal tooth anatomy in favor of elevated classical brass heraldry and subtle Yorùbá geometric relief (`àkọ̀` / `ìkòkò`).
  - **Prototype 1 (<AkosileProvenanceDrawer />)**: Forged `web/src/components/AkosileProvenanceDrawer.jsx` (120 LOC, < 150 LOC target) displaying academic provenance (Rev. Samuel Johnson 1921, Prof. Wándé Abímbọ́lá, Prof. Rowland Abiodun, Prof. Babatunde Lawal, Pierre Verger), museum accession identifiers, custodial repositories, and RAIL-Cultural-Heritage-v1.0 + Awo sacred boundary protection.
  - **Prototype 2 (<LivingVariantConstellationGrid />)**: Forged `web/src/components/LivingVariantConstellationGrid.jsx` (91 LOC, < 150 LOC target) rendering luminous sub-variant constellation chips with smooth hover glow and 1-click dynamic branching.
  - **Clean Declarative Mounting**: Mounted both components within `EntityBentoDeck.jsx` (395 LOC, < 500 LOC ceiling).
  - **Naming Invariant Upheld (Gate 6)**: Cloud Infrastructure Engineer strictly referenced as `Irin` (`irin-cloud`).
  - **Verification**: `npm run build` compiled in 733ms (1,914 modules transformed, 0 errors); `./scripts/review.sh` passed with 0 hard violations and 0 warnings.
- **[2026-10-27] (`HANDOFF-AGBEDE-006` Completed)**: **Executive Delivery of the Triple Concentric Ọpọ́n Ifá Search Core**:
  - Received unanimous green light from Lead Architect Àrùnà Ọlànrewájú Kábírù and the Sovereign Council (`Ìmọ̀`, `Ẹ̀ṣọ́`, `Òye`, `Àgbà`).
  - Evaluated and mitigated all 5 production trade-offs (mobile real estate, diacritic touch density, low-end GPU performance, Gate 2 LOC ceiling, and downstream vascular vein canvas anchor alignment).
  - Forged `web/src/components/OponSearchCore.jsx` (257 LOC, strictly < 500 lines) fully implementing the Triple Concentric Ọpọ́n Ifá geometry:
    1. Outer Bronze Rim (`Etí Ọpọ́n`): Cosmic perimeter arc with North Sentinel Lozenge, open at southern base.
    2. Mid Celestial Orbit (`Àyíká Ìmọ̀`): Houses the 15 sacred 25-letter Yorùbá diacritics with minimum 32px touch targets.
    3. Inner Golden Dust Hearth (`Àárín Ọpọ́n`): Warm amber *Ìyẹ̀ròsùn* hearth housing search input capsule with zero overlap.
    4. Base Portal & Veins: Channels cascading gold Bézier veins into Sovereign Parent and Living Variants, anchoring `#central-tooth-search-anchor` at the portal.
    5. Gate 4 Awo Sacred Boundary Integrity: Abstract Sentinel Lozenge and dignified *"Ṣàwárí nínú Ìmọ̀"* framing.
  - Wired into `web/src/components/SearchTab.jsx` (486 LOC, 0 net lines added).
  - Verification: `npm run build` compiled in 631ms (1,914 modules transformed, 0 errors); `./scripts/review.sh` passed with 0 hard violations and 0 warnings.
- **[2026-10-27] (`CHECKPOINT-AGBEDE-007`)**: Removed distracting micro-label `"Open Base Gateway • Arterial Veins Flowing"` from `OponSearchCore.jsx` (253 LOC) and prototype lab per Lead Architect directive. Pure visual majesty restored; compiled in 627ms with 0 errors.
- **[2026-10-27] (`CHECKPOINT-AGBEDE-008`)**: **Restored Flowing & Glowing Vein Keyframes in Production**:
  - Root Cause: Keyframe animations (`@keyframes veinCascading`, `@keyframes ringGlow`, `@keyframes goldenDustPulse`) and classes (`.cascading-vein`, `.glowing-ring`, `.dust-heart`) were defined inside the prototype lab's `<style>` block but omitted from `web/src/index.css` and `OponSearchCore.jsx`.
  - Resolution: Injected full keyframe animations and utility classes into `web/src/index.css`. Added `className="cascading-vein"` to left & right SVG arterial paths, `className="glowing-ring"` to Outer Rim, and ambient `dust-heart` golden pulse aura behind the hearth in `web/src/components/OponSearchCore.jsx` (256 LOC < 500 LOC ceiling).
  - Verification: `npm run build` compiled in 910ms (0 errors); `./scripts/review.sh` passed with 0 hard violations and 0 warnings.
- **[2026-10-27] (`CHECKPOINT-AGBEDE-009`)**: **Hearth De-cluttering (Removed Sovereign Hearth Pill Badge)**:
  - Removed badge `ÀÁRÍN ÌMỌ̀ • SOVEREIGN HEARTH` from `OponSearchCore.jsx` (249 LOC) and prototype lab per Lead Architect directive.
  - Re-centered the input capsule vertically inside the golden *Ìyẹ̀ròsùn* hearth (`top: 102px`), giving the search bar and diacritics pristine spatial balance.
  - Feasibility Analysis Conducted: Evaluated lengthening the continuous flowing vein trail across repeated searches via `useExplorationGraph.js` and `VeinRabbitHoleCanvas.jsx`.
- **[2026-10-27] (`CHECKPOINT-AGBEDE-010` / Checkpoint 050)**: **Executive Refactoring of SearchTab.jsx (Gate 2 Headroom Reclaim)**:
  - Objective: Decomposed `web/src/components/SearchTab.jsx` from **486 LOC** down to **227 LOC** (-259 LOC, reclaiming 273 lines of headroom under the 500-LOC ceiling) with zero runtime or UI regressions.
  - Extracted 4 modular files strictly under limits:
    1. `web/src/utils/tonalContour.js`: 34 LOC (< 60 target). `stripAccents`, `normalizeNFC`, `escapeRegExp`, `extractTonalContour`.
    2. `web/src/utils/localRankedSearch.js`: 63 LOC (< 90 target). `searchRankedCorpus(q, masterCorpus)`.
    3. `web/src/utils/bentoHydrator.js`: 67 LOC (< 80 target). `findVisualRegaliaHit`, `hydrateEntityForBento`.
    4. `web/src/hooks/useRootNetworkNodes.js`: 83 LOC (< 110 target). `resolveSubVariantEntities`, `useRootNetworkNodes`.
  - Verification:
    - `npm run build`: compiled in 927ms (1,918 modules, 0 errors).
    - `python3 scripts/benchmark_sprint004.py`: 28/28 Top-1 Accuracy (100.0% PASS).
    - `./scripts/review.sh`: 0 hard violations, 0 warnings across all 8 Production Gates.
- **[2026-10-27] (`CHECKPOINT-AGBEDE-011` / Checkpoint 051)**: **Executive Refactoring of TranslateTab.jsx (Neutralized Hotspot #1)**:
  - Objective: Neutralized our last client-side Gate 2 violation by decomposing `web/src/components/TranslateTab.jsx` from **612 LOC** down to **69 LOC** (-543 LOC, Law 1 Coordinator Invariant satisfied < 90 LOC) using Law 2 (The Three-Drawer Mandate).
  - Extracted 4 modular files strictly under limits:
    1. Pure Logic & Data Drawer: `web/src/utils/yorubaDiacriticsLexicon.js` (**235 LOC**, target < 300 LOC). Pure functions with zero React deps.
    2. State & Lifecycle Drawer: `web/src/hooks/useCulturalTranslation.js` (**92 LOC**, target < 120 LOC). Gate 3 synchronous double-tap lock (`busyRef.current = true`) guarding `/v6/translate/diacritize` and `/v6/translate/cultural`.
    3. Presentation Drawer: `web/src/components/DiacritizerCard.jsx` (**91 LOC**, target < 120 LOC).
    4. Presentation Drawer: `web/src/components/CulturalGlossCard.jsx` (**88 LOC**, target < 150 LOC).
  - Verification:
    - `npm run build`: compiled in 840ms (1,922 modules, 0 errors).
    - `python3 scripts/benchmark_sprint004.py`: 28/28 Top-1 Accuracy (100.0% PASS).
    - `./scripts/review.sh`: 0 hard violations, 0 warnings across all 8 Production Gates.
- **[2026-10-27] (`CHECKPOINT-AGBEDE-012` / Checkpoint 052)**: **Executed The Great Re-Wiring Pass (248 Orphaned Records Resolved)**:
  - Objective: Re-wired orphaned standalone records to Sovereign Parents in lockstep across `api/data/yoruba_corpus_1007_NORMALIZED.json` and `web/src/data/yoruba_master_corpus.json`.
  - Executed `scripts/execute_rewiring_pass.py` (209 LOC < 500 LOC ceiling):
    1. Consolidated Fìlà Family: Deduplicated `Filà Abetíajá` into `Fìlà Abetí Ajá` (citations merged); cleansed Vietnamese `ị` in `Fìlà Gọ̀bị́` -> `Fìlà Gọ̀bí`; wired 8 Fìlà variants under Sovereign Parent `Fìlà`. Total corpus: 1,416 canonical entities.
    2. Wired Paramount Monarchs: `Awùjalẹ̀`, `Déjì`, `Akárìgbò`, `Ọlọ́fà`, `Alárá`, `Arẹ́sà` wired to `Ọba` and linked bidirectionally to their kingdoms.
    3. Wired ancient capitals: `Ilé-Ifẹ̀`, `Òṣogbo` → `Ìpínlẹ̀ Ọ̀ṣun`; `Ìbàdàn`, `Ọ̀yọ́-Ilé` → `Ìpínlẹ̀ Ọ̀yọ́`; `Ilọrin` → `Ìpínlẹ̀ Kwara`; `Ìjẹ̀bú-Òde`, `Abẹ́òkúta` → `Ìpínlẹ̀ Ògùn`.
    4. Auto-wired 223 additional orphaned records declared by Sovereign Parents. Total wired sub-variants elevated to 324.
    5. Resolved 2 Prefix Collisions: Tuned `preprocess_query_tokens` in `api/app/semantic_bridge.py` and `localRankedSearch.js` with negative lookahead protecting `agbadagba` from prefix splitting, and normalized `_` and `-` so `Iwe-Agbadagba` and `baba_ile` achieve clean Top-1 ranking without usurping.
  - Verification:
    - `benchmark_sprint004.py`: 28/28 Top-1 Accuracy (100.0% PASS).
    - `npm run build`: Compiled in 808ms (1,922 modules, 0 errors).
    - `./scripts/review.sh`: 0 hard violations across all 8 Production Gates.












