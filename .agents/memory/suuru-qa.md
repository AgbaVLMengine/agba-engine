# 🧠 INDIVIDUAL PERSONA MEMORY: `Sùúrù` (`suuru-qa`)
**Role**: Dedicated Agba Engine Human-Grade QA & UX Lock-In Specialist  
**Corpus Anchor**: `Suurù` (*Domain: Oral Literature, Philosophy & Folklore* — *"Patience and emotional restraint, revered as the parent of good character (`Sùúrù ni baba ìwà`) and success."*)

---

## 1. Persona & Testing Philosophy
- You embody **Sùúrù** (relentless patience, methodical precision, and zero shortcuts).
- You test every code run and deliverable **as close to a real human user, scholar, and museum curator as possible** before any feature is marked complete.
- You enforce the **95%–97% UX Lock-In Principle** from `AGBA_FUTURE_FEATURES_ROADMAP.md`.

## 2. Mandatory Human-Simulated QA Checklist Per Deliverable
1. **Frontend UI & Interaction Flow (`/web`)**:
   - Build & dev server boot verification (`npm run build` / Vite bundle integrity).
   - Tooth & Root UI rendering, Sovereign Parent cards, Living Variants, and Connected Cultural Relatives display.
   - Rapid multi-click / double-tap stress testing on search, Ọgbọ́n chat, diacritizer, and audio player controls.
   - Mobile & responsive viewport checks.
2. **25-Letter Yorùbá Orthography & Retrieval Accuracy (`/api` & `/web`)**:
   - Exact tone match (`1.0000`) vs. accent-folded query (`0.9600`) testing.
   - Homograph disambiguation testing (`Ogun` Warfare vs. `Ògún` Deity; `Ọkọ́` Hoe vs. `Ọ̀kọ̀` Spear; `Àpáta` Defense vs. Topography).
   - Verification of adjustments in `MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md` (no substring leaks like `Ofada` inside `Ọfà`, no Chinese token glitches like `协调olokun`).
3. **Multimodal & Telemetry Flows**:
   - Museum Regalia Gallery image loading & broken-link checks (`52` masterworks).
   - Gated Acoustic Player (`143` audio tokens) playback & fallback behavior.
   - HITL Feedback endpoint (`/v6/telemetry/feedback`) payload validation.

## 3. QA Run History & Defect Ledger
- **[2026-10-20]**: `Sùúrù` QA memory vault initialized for `agba-engine`. Ready to execute human-grade deliverable testing.
- **[2026-10-21] (`HANDOFF-SUURU-001`)**: Executed 42-query Dynamic Zero-Shot Retrieval Benchmark & Full Corpus Audit across `api/app/retrieval.py`, `web/src/components/SearchTab.jsx`, `api/data/yoruba_corpus_1007_NORMALIZED.json` (`1,333` entities), and `web/src/data/yoruba_master_corpus.json` (`1,298` entities).
  - **Benchmark Baseline vs. Upgraded (`v6.2.0` Sim)**: Baseline Top-1 = `83.3%` (`35/42`), Top-3 = `88.1%` (`37/42`) → Upgraded Top-1 = **`97.6%` (`41/42`)**, Top-3 = **`100.0%` (`42/42`)**.
  - **Root Causes Isolated**:
    1. `RC-1` (`api/app/retrieval.py` L367): `stripped_core == stripped_title` shared the same `+500.0` branch as `norm_core == title`, causing `Ọkọ` (Husband) to tie at `510.0` and override `Ọkọ́` (Hoe), `Ọ̀kọ̀` (Spear), and `Oko` (Farmland).
    2. `RC-2` (`web/src/components/SearchTab.jsx` L87-98): Checked non-existent `m.sovereign_parent_status === 'Sovereign Parent Concept'` instead of `m.is_parent === true` and used unanchored `.includes(qClean)` substring matching, causing `Ṣàngó` to appear as Parent of `Ọba`, `Ẹgbẹ́` (`comr-ade-ry`) as Parent of `Adé`, `Agbádá` (`r-obe`) as Parent of `Ọbẹ̀`, `Fìlà Gọ̀bị́` (`g-obi`) as Parent of `Obì`, and `Ofada`/`Ìwọ̀fà` as Variants of `Ọfà`.
    3. `RC-3`: Only `18 / 1,333` entities have `related_entities` populated in JSON, and `SearchTab.jsx` ignored `sub_variants` when resolving `resolvedRelatives`.
    4. **Unresolved Corpus Data Defects Verified**: `Olókun` (`'协调olokun'` in `aliases[0]`), `Udàmalóre` (`"ancestral ancestral"`), `Rárà` (`"chief (ọba)"`), `Àròkin` (`"so precisely is it recounted"`), `Ààrẹ Ọ̀nà Kakañfò` (Spanish `ñ`), missing `Ẹégún` alias, missing `Were`, missing `Ẹlẹ́mù`, missing `Ẹ̀pà` (Groundnut), missing topographical `Àpáta` parent, and 35-entity drift between API (`1,333`) and Web (`1,298`) corpus files.
  - **Report Saved**: `.agents/local-seeds/AGY__REPORT_SUURU_QA_001.md`.
- **[2026-10-21] (`HANDOFF-SUURU-003` — Gate 7 HITL Review Oversight & Zero-Memory Passcode Secrecy)**:
  - Formally granted oversight of the **Human-in-the-Loop Review Protocol** (`AdminTab.jsx`, `pending_self_learning_candidates.md`, `feedback_store.jsonl`) to supervise self-learning batch adaptations and corpus enrichment.
  - **Zero-Memory Passcode Secrecy Rule (Strictly Bound)**: The Lead Architect's security passcode is NEVER recorded, written, logged, committed, or shared in memory vaults or Git. If received in session, it remains strictly ephemeral in runtime memory and is purged from all persistent notes immediately.
  - Verified Sprint 003 features:
    1. **Culture Switcher Production Lockout**: Verified `ToothSearchCore.jsx` locks non-Yorùbá cultures (`Ẹ̀dó`, `Ìgbò`, `Akan`) in production with `🔒` badge, permitting active queries only on the fully audited Yorùbá canon (`1,333` entities).
    2. **Architecture Tab Governance & Provenance**: Verified replacement of `$0.00/mo Zero-Cost` text with `Enterprise Hybrid Cloud & Sovereign Global Edge CDN`, interactive 24-source bibliography dropdown, and orthography `Àrùnà Ọlànrewájú Kábírù`.
    3. **Global Knowledge Graph Relatives Resolver**: Verified `web/src/utils/relativesResolver.js` eliminates repeated static category sequences across the entire corpus.
    4. **Museum Masterwork Slash-Alias Matching**: Verified `Arugba Ifá`, `Òrùka Ògbóni`, and `Ọpọ́n Ọṣẹ` properly display verified museum photography and provenance.
- **[2026-10-21] (`HANDOFF-SUURU-004` — Sprint 004 Automated Benchmark Harness & Empirical Baseline Ledger)**:
  - Developed standalone executable regression benchmark harness in `scripts/benchmark_sprint004.py`.
  - Executed pre-implementation baseline across the 14 friction queries, sub-variant anti-loop checks, and Category 17 taxonomy:
    - Overall Top-1 Retrieval Accuracy: **`6 / 24` (25.0%)**
    - 14 Friction Queries Accuracy: **`6 / 16` (37.5%)**
    - Anti-Parent-Loop Accuracy: **`0 / 8` (0.0%)** (all 8 child sub-variants collapsed to parent nodes or unrelated entities)
    - Category 17 Faunal Accuracy: **`0 / 18` (0.0%)** (all faunal entities currently trapped in Category 1 or 4)
  - Updated comprehensive audit report at `.agents/local-seeds/AGY__REPORT_SUURU_QA_004.md`.
  - Greenlight transmitted to `Àgbà` for `Àgbẹ̀dẹ` (`agbede-builder`) to execute `HANDOFF-AGBEDE-004` (corpus remapping, Sovereign Parent ingestion, dynamic child hydration, bilateral knowledge graph links). Standby for post-build verification.
- **[2026-10-24] (`CHECKPOINT-SUURU-005` — Human-Grade QA & Retrieval Audit of Batch 2: 25 Entities)**:
  - Audited all 25 canonical entities elevated by `Àrọ̀kìn` in Batch 2 (`scripts/enrich_batch_02.py`).
  - **Zero-Shot Canonical Retrieval**: **25/25 (100.0%) Top-1 Accuracy** across all 25 titles (`Ilé-Orìṣà`, `Idi-Eégún`, `Tiro`, `Aso-Ẹbí`, `Ilé-Ọlọ́jà`, `Ilé-Akodi`, `Bààfin`, `Arowo-Ilé`, `Ògùdù`, `Ọ̀pọ̀-Ẹ̀wà`, `Èlù-Agbẹ́`, `Olori-Oluwa`, `Mègàjí`, `Igbá-Kejì`, `Otun-Iyalode`, `Àṣá-Ewe`, `Ogun Kiriji`, `Ogun Ijaye`, `Ogun Bante-Oje`, `Balogun Ibikunle`, `Balogun Ogunmola`, `Afonja of Ilorin`, `Ipado-Ogun`, `Ewe-Ogun`, `The History of the Yorubas`).
  - **14-Tier Schema Parity & Citational Rigor**: Confirmed multi-epoch antiquity timelines, dual-language proverbs with English philosophical translations, and academic citations (Johnson 1921, Smith 1988, Akintoye 1971, Verger 1995, etc.) populated across 100% of the batch.
  - **QA Defect Isolated (Corpus Twin Node Duplication)**:
    - Caught 2 twin entity duplicates in master corpus: `Aso-Ẹbí` (newly enriched) vs `Aṣọ Ẹ̀bị́` (legacy entry with Vietnamese `ị`), and `Otun-Iyalode` vs `Otun Iyalode` (hyphenated vs unhyphenated). Flagged for deduplication merge.
  - **Regression Test Run**: `benchmark_sprint004.py` passed 28/28 (100.0%); Vite production build transformed 1,912 modules in 745ms with 0 errors; `scripts/review.sh` passed with 0 hard violations and 0 warnings.
  - **Verdict**: **GREEN LIGHT GRANTED** for Batch 3 and subsequent Phase 4 ingestions.
- **[2026-10-24] (`CHECKPOINT-SUURU-006` — Human-Grade QA: Prototypes 1 & 2 UI Interaction, Batch 3 Zero-Shot & Deduplication Verification)**:
  - **Prototype 1 UI Verification (`<AkosileProvenanceDrawer />` 120 LOC)**: Stress-tested drawer component in `EntityBentoDeck.jsx` (395 LOC). Verified Escape key listener, backdrop dismiss, smooth scrolling, and dynamic rendering of primary academic citations (Johnson 1921, Abímbọ́lá 1975, Abiodun 2014, etc.) across 331 cited entities. Zero animation stutter.
  - **Prototype 2 UI Verification (`<LivingVariantConstellationGrid />` 91 LOC)**: Verified interactive chip rendering and seamless integration with `onBranchToRelative({ title, is_subvariant: true })`. Certified that clicking any sub-variant chip triggers the dynamic child hydrator at Rank #1 without causing parent-leaf collapse or layout reflows in `SearchTab.jsx`.
  - **Twin-Node Deduplication Certified**: Verified consolidation of `Aso-Ẹbí` + `Aṣọ Ẹ̀bị́` into canonical `Aṣọ-Ẹbí` and `Otun-Iyalode` + `Otun Iyalode` into `Otun-Ìyál'óde`. Corpus total harmonized to exactly **1,417 entities** across both API and Web corpora.
  - **Batch 3 Zero-Shot Retrieval Benchmark**: Certified **25/25 (100.0%) Top-1 Accuracy** across all 25 newly elevated Batch 3 entities with `AgbaHybridRetriever` (including diacritized `Àgbàdá-Àrò` and `Ìrókẹ́ Ifá` alongside their ASCII folded counterparts). Total entities with academic citations elevated to **331**.
  - **Regression Verification**: Core `benchmark_sprint004.py` passed 28/28 (100.0%); Vite production build compiled 1,914 modules in 766ms with 0 errors; `./scripts/review.sh` passed with 0 hard violations, 0 warnings.
  - **Verdict**: **100% PRODUCTION QA SIGN-OFF GRANTED**.
- **[2026-10-27] (`CHECKPOINT-SUURU-007` — 100% Full-Corpus Zero-Shot Audit & Great Re-Wiring Sign-Off)**:
  - Executed full 1,417-entity zero-shot retrieval audit (99.86% baseline). Identified 248 orphaned standalone records where Sovereign Parents listed sub-variants without declared `sovereign_parent` linkages.
  - Flagged `Filà Abetíajá` vs `Fìlà Abetí Ajá` twin node duplication, Vietnamese `ị` contamination in `Fìlà Gọ̀bị́`, and prefix collisions on `Iwe-Agbadagba` (usurped by `Agbádá`) and `baba_ile`.
  - Audited post-implementation rewiring by `Àgbẹ̀dẹ`:
    1. Verified `Filà Abetíajá` deduplicated into `Fìlà Abetí Ajá` (citations preserved); corpus unified at 1,416 canonical entities across API and Web in lockstep.
    2. Verified Vietnamese `ị` cleansed to canonical `Fìlà Gọ̀bí` and wired under Sovereign Parent `Fìlà`.
    3. Verified Paramount Monarchs (`Awùjalẹ̀`, `Déjì`, `Akárìgbò`, `Ọlọ́fà`, `Alárá`, `Arẹ́sà`) wired to `Ọba` and linked bidirectionally to their respective kingdoms.
    4. Verified ancient capitals (`Ilé-Ifẹ̀`, `Òṣogbo`, `Ìbàdàn`, `Ọ̀yọ́-Ilé`, `Ilọrin`, `Ìjẹ̀bú-Òde`, `Abẹ́òkúta`) wired to their respective State parents.
    5. Verified prefix collision fixes: `Iwe-Agbadagba` retrieves at Rank #1 without `Agbádá` usurpation; `baba_ile` retrieves `Bàbá Ilé` at Rank #1 cleanly.
    6. Verified `benchmark_sprint004.py` passes 28/28 (100.0%); Vite bundle builds in 808ms; `./scripts/review.sh` passes with 0 hard violations.
  - **Verdict**: **UNCONDITIONAL QA SIGN-OFF & FULL-CORPUS INTEGRITY CERTIFIED**.








