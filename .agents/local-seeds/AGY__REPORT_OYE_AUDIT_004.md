# 🏛️ ÀGBÀ ENGINE: ADVERSARIAL CORPUS AUDIT & ZERO-SHOT ARCHITECTURE REPORT
## Task Reference: `HANDOFF-OYE-004` (Sprint 004 Forensic Audit)
**Lead Auditor**: Òye (`oye-auditor`)  
**QA Validation Partner**: Sùúrù (`suuru-qa`)  
**Supervising Chief Co-Architect**: Àgbà (`agba-pa-architect`)  
**Lead Architect & Reviewer**: Àrùnà Ọlànrewájú Kábírù  
**Status**: 🟢 **AUDIT COMPLETE — READY FOR ARCHITECT REVIEW BEFORE INGESTION**  

---

### 📋 Executive Summary of Audit Findings

| Audit Mandate | Forensic Finding | Root Cause & Systemic Impact | Recommended Architectural Resolution |
| :--- | :--- | :--- | :--- |
| **1. Missing Parent Entities** | **9 Critical Parents Missing** (`Ifá`, `Were`, `Oogun`, `Ẹ̀pà`, `Àpáta`, `Ẹlẹ́mù`) | Exact-match misses root concepts; token search falls back to proverbs or related genres. | Synthesize & ingest canonical 14-tier Sovereign Parent records into normalized master corpus. |
| **2. Sub-Variant Parent Loops** | **100 Sub-Variants Unindexed** across 34 Sovereign Parents | Sub-variant strings in parent arrays have no standalone records; clicking them collapses to parent. | Implement **Dynamic Sub-Variant Fallback Hydration** + backfill standalone records for top martial/semiotic entries. |
| **3. Sub-Variant Hydration** | **Missing in Runtime Logic** | `SearchTab.jsx` previously queried `searchRankedCorpus` on clicked variants, re-ranking parent as #1. | Deploy **100% data-driven, zero-hardcoded dynamic child-node hydrator** in `SearchTab.jsx` and `retrieval.py`. |
| **4. Knowledge Graph Links** | **1,315 / 1,333 Entities (98.6%) lack `related_entities`** | Corpus relied exclusively on category arrays; nodes lacked curated bilateral semantic edges. | Populate explicit bilateral domain knowledge graphs for all audited Sovereign Parents and guilds. |

---

## 🏛️ PART I: PARENT ENTITIES REQUIRING IMMEDIATE CANONICAL INGESTION

The following foundational parent concepts do not exist as distinct records in the 1,333 JSON index:

| # | Canonical Title | Primary Category | Diagnostic Cause of Retrieval Friction | Curated Ingestion Specification |
|---|---|---|---|---|
| 1 | **`Ifá`** | Spiritual & Cosmological Matrix | Supreme Epistemological System, 256 Odù Divinatory Matrix & Wisdom Corpus of Ọ̀rúnmìlà | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 2 | **`Were / Were Music`** | Auditory Arts, Music, Drums & Chants | Ajísààrì Islamic morning awakening music, precursor to modern Fújì | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 3 | **`Oogun (Inherited Estate / Property)`** | Social Structure, Kinship & Lineage | Family property, ancestral inheritance, and lineage estate (Ogún Ìdílé / Inú-Ilé) | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 4 | **`Òògùn (Traditional Pharmacology & Medicine)`** | Sacred Botany, Flora & Herbal Medicine | Pharmacological infusions, protective talismans, and natural herbal remedies | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 5 | **`Ẹ̀pà (Groundnut & Agronomy)`** | Culinary Arts & Indigenous Gastronomy | Groundnut / peanut legume cultivated across Yorùbá farmlands (distinct from Epa masquerade) | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 6 | **`Àpáta (Sacred Topography & Granite Formations)`** | Topography, Natural Landscapes & Architecture | Inselbergs, granite hills, sacred caverns, and rocky ancestral sanctuaries (Olúmo, Ìdánre) | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 7 | **`Ẹlẹ́mù (Palm Wine Tapper Guild)`** | Traditional Trades, Agriculture & Agrarian Guilds | Indigenous guild of palm wine tappers and custodians of Ẹ̀mù Ọ̀pẹ and Ògùrọ̀ | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 8 | **`Ẹégún`** | Ancestral Masquerades & Funerary Rites | Colloquial and lineage manifestation of Egúngún | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |
| 9 | **`Ìwọ̀fà (Pawnship & Traditional Labor Contract)`** | Civilization, History & Civic Heritage | Traditional pre-colonial labor covenant system (distinct from Ọfà arrow) | Ingest as Sovereign Parent with full 14-tier schema, oral proverbs, and living variants. |

---

## 🏛️ PART II: SUB-VARIANT INVENTORY (UNINDEXED CHILD RECORDS CAUSING PARENT LOOPS)

Scanning 34 core Sovereign Parents identified **100 sub-variant strings** that exist only as text in parent arrays without independent child records:

| # | Sovereign Parent | Category | Unindexed Sub-Variant (Currently Collapsing to Parent) | Required Resolution |
|---|---|---|---|---|
| 1 | **Àrọ̀kọ̀** | Oral Literature, Philosophy & Folklore | `Àrọ̀kọ̀ Ẹfà (Love)` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 2 | **Àrọ̀kọ̀** | Oral Literature, Philosophy & Folklore | `Àrọ̀kọ̀ Ẹ̀jọ́ (Dispute)` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 3 | **Àrọ̀kọ̀** | Oral Literature, Philosophy & Folklore | `Àrọ̀kọ̀ Ogun (War)` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 4 | **Àrọ̀kọ̀** | Oral Literature, Philosophy & Folklore | `Ẹyin Ìkódẹ (Royal Summons)` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 5 | **Àrọ̀kọ̀** | Oral Literature, Philosophy & Folklore | `Àrọ̀kọ̀ Àlàáfíà (Peace)` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 6 | **Ọ̀kọ̀** | Military Traditions, Weaponry & Defense | `Ọ̀kọ̀ Ẹlẹ́ṣin` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 7 | **Ọ̀kọ̀** | Military Traditions, Weaponry & Defense | `Ọ̀kọ̀ Ògún` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 8 | **Ọ̀kọ̀** | Military Traditions, Weaponry & Defense | `Ọ̀kọ̀ Ọdẹ` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 9 | **Ọ̀kọ̀** | Military Traditions, Weaponry & Defense | `Ọ̀kọ̀ Ìṣẹ́gun` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 10 | **Ọfà** | Military Traditions, Weaponry & Defense | `Ọfà Ọdẹ` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 11 | **Ọfà** | Military Traditions, Weaponry & Defense | `Apó Ọfà` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 12 | **Ọfà** | Military Traditions, Weaponry & Defense | `Ọfà Òṣọ́ọ̀sì` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 13 | **Ọfà** | Military Traditions, Weaponry & Defense | `Oró Ọfà` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 14 | **Àdá** | Traditional Trades, Agriculture & Agrarian Guilds | `Àdá Ìbílẹ̀` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 15 | **Àdá** | Traditional Trades, Agriculture & Agrarian Guilds | `Àdá Pẹ́pẹ́` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 16 | **Àdá** | Traditional Trades, Agriculture & Agrarian Guilds | `Àdá Fáàfà` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 17 | **Àdá** | Traditional Trades, Agriculture & Agrarian Guilds | `Àgọ́gọ́ Oko` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 18 | **Idà** | Military Traditions, Weaponry & Defense | `Idà Agẹmọ` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 19 | **Idà** | Military Traditions, Weaponry & Defense | `Idà Ọba` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 20 | **Idà** | Military Traditions, Weaponry & Defense | `Idà Ìṣẹ́gun` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 21 | **Idà** | Military Traditions, Weaponry & Defense | `Tanmogayi` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 22 | **Idà** | Military Traditions, Weaponry & Defense | `Idà Ògún` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 23 | **Idà** | Military Traditions, Weaponry & Defense | `Kùmọ̀` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 24 | **Apẹja** | Traditional Trades, Agriculture & Agrarian Guilds | `Àwọ̀n Apẹja` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 25 | **Apẹja** | Traditional Trades, Agriculture & Agrarian Guilds | `Ìhà / Àgọ̀ Ẹja` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 26 | **Apẹja** | Traditional Trades, Agriculture & Agrarian Guilds | `Ọkọ̀ Ojú Omi` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 27 | **Apẹja** | Traditional Trades, Agriculture & Agrarian Guilds | `Ìwọ̀ Apẹja` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 28 | **Apẹja** | Traditional Trades, Agriculture & Agrarian Guilds | `Àkérè Apẹja` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 29 | **Ẹja** | Spiritual & Cosmological Matrix | `Ẹja Àrọ̀` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 30 | **Ẹja** | Spiritual & Cosmological Matrix | `Àbọ̀rí` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 31 | **Ẹja** | Spiritual & Cosmological Matrix | `Ẹja Kíka` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 32 | **Ẹja** | Spiritual & Cosmological Matrix | `Alágẹmọ` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 33 | **Ẹyẹ** | Spiritual & Cosmological Matrix | `Àlùkò` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 34 | **Ẹyẹ** | Spiritual & Cosmological Matrix | `Odídẹrẹ́` | Dynamic Fallback Hydration & Standalone Record Backfill |
| 35 | **Ẹyẹ** | Spiritual & Cosmological Matrix | `Àṣá` | Dynamic Fallback Hydration & Standalone Record Backfill |

*(Truncated: 65 additional sub-variants cataloged)*


---

## 🏛️ PART III: ZERO-HARDCODED DYNAMIC SUB-VARIANT FALLBACK HYDRATION SPECIFICATION

To solve the sub-variant parent loop permanently without hardcoding a single title or ID, the engine must deploy a dynamic child hydrator in `SearchTab.jsx` and `retrieval.py`:

```javascript
function hydrateSubVariantFromParent(variantTitle, parentEntity) {
  const variantClean = stripAccents(variantTitle);
  return {
    id: `${parentEntity.id}_${variantClean.replace(/\s+/g, '_')}`,
    title: variantTitle,
    category: parentEntity.category,
    is_parent: false,
    sovereign_parent: parentEntity.title,
    sovereign_parent_status: 'Living Sub-Variant',
    description: `A specialized living variant within the ${parentEntity.title} tradition, embodying ${variantTitle} in classical ${parentEntity.category}.`,
    historical_timeline: parentEntity.historical_timeline || `Preserved through the generational lineage of ${parentEntity.title}.`,
    material_and_craftsmanship: parentEntity.material_and_craftsmanship,
    social_and_ritual_context: `Operates in direct ritual, ceremonial, and practical alignment with ${parentEntity.title}.`,
    proverbs_and_oral_traditions: parentEntity.proverbs_and_oral_traditions,
    sub_variants: [],
    related_entities: [
      parentEntity.title,
      ...(parentEntity.sub_variants || []).filter(sv => sv !== variantTitle)
    ],
    details: {
      culture: parentEntity.culture || 'Yorùbá Classical',
      category: parentEntity.category,
      sovereign_parent: parentEntity.title
    }
  };
}
```

**Operational Invariant**: When a user clicks or queries a string recognized in any Sovereign Parent's `sub_variants` list that lacks a dedicated index record, the dynamic hydrator synthesizes the node at Rank #1 (`fusion_score: 1.0000`) and branches the vein rabbit hole directly from the parent to the variant!

---

## 🏛️ PART IV: KNOWLEDGE GRAPH CONNECTIVITY AUDIT ACROSS ALL 16 CATEGORIES

Audit revealed that **1,315 / 1,333 entities (98.6%)** currently lack explicit `related_entities` arrays in the JSON file:

| Category | Total Entities | With Curated Links | Unpopulated Orphans | Sample Entities Requiring Graph Links |
| :--- | :--- | :--- | :--- | :--- |
| **Spiritual & Cosmological Matrix** | 434 | 14 | 420 | Ikin Ifá, Agẹrẹ Ifá, Ọ̀pẹ̀lẹ̀, Ọpọ́n Ifá |
| **Attire, Textiles & Personal Adornment** | 104 | 0 | 104 | Agbádá, Ìlèkè, Ìlèkè Ẹsẹ̀, Ìlèkè Ọrùn |
| **Monarchy, Royal Regalia & Governance** | 100 | 1 | 99 | Àmì Ọlá, Ọba, Kábíyèsí, Adé |
| **Social Structure, Kinship & Lineage** | 91 | 0 | 91 | Ẹgbẹ́, Ògbóni, Ìyàwó, Ọkọ |
| **Culinary Arts & Indigenous Gastronomy** | 83 | 0 | 83 | Amàlà, Èlùbọ́, Gbẹ̀gị̀rị́, Ewedu |
| **Civilization, History & Civic Heritage** | 79 | 0 | 79 | Ìpínlẹ̀ Kogi, Ìpínlẹ̀ Kwara, Ìpínlẹ̀ Èkó, Ìpínlẹ̀ Òndó |
| **Military Traditions, Weaponry & Defense** | 72 | 0 | 72 | Àpáta, Ọfà, Idà, Ogun (Warfare & Military Tradition) |
| **Visual Arts, Sculpture & Guild Metallurgy** | 58 | 0 | 58 | Ère, Owó Ẹyọ, Àwọ̀, Gbẹ́nàgbẹ́nà |
| **Topography, Natural Landscapes & Architecture** | 58 | 0 | 58 | Odò, Òkè, Odi, Ojúbọ |
| **Auditory Arts, Music, Drums & Chants** | 58 | 0 | 58 | Àlọ́ ÌJÀPÁ, Oríkì, Ewì, Rárà |
| **Sacred Botany, Flora & Herbal Medicine** | 56 | 0 | 56 | Oníṣègùn, Irókò, Oníṣẹ̀gùn, Ọ̀pẹ |
| **Oral Literature, Philosophy & Folklore** | 51 | 0 | 51 | Àrọ̀kọ̀, Òwe, Àlọ́ Àmoṣùn, Àrokò |
| **Traditional Trades, Agriculture & Agrarian Guilds** | 40 | 1 | 39 | Apẹja, Ìwunṣọ, Ọdẹ, Ọkọ́ |
| **Royal Regalia, Sacred Art & Architecture** | 20 | 2 | 18 | Orufanran, Òpó Ògògá, Ọpọ́n Ọṣẹ, Arugba Ifá |
| **Ancestral Masquerades & Funerary Rites** | 16 | 0 | 16 | Ẹ̀ṣà Ẹégún, Èfé, Egúngún, Geledẹ́ |
| **Festivals, Celebrations & Civic Pageantry** | 13 | 0 | 13 | Ìsọmọlórúkọ, Ìgbéyàwó, Ọdún Ọlọ́jọ́, Ọdún Ọ̀pẹ |

---

### 🎯 Recommended Sequence of Execution for Sprint 004
1. **Audit Signoff**: Lead Architect reviews this audit ledger (`AGY__REPORT_OYE_AUDIT_004.md`).
2. **Dynamic Hydration Implementation (`Àgbẹ̀dẹ`)**: Deploy the Zero-Hardcoding Sub-Variant Hydrator in `SearchTab.jsx` and `relativesResolver.js`.
3. **Missing Parents Ingestion (`Àgbẹ̀dẹ`)**: Ingest the 9 canonical missing parents with complete 14-tier schemas into `yoruba_corpus_1007_NORMALIZED.json` and `yoruba_master_corpus.json`.
4. **Stand-Alone Sub-Variant Backfill (`Àgbẹ̀dẹ`)**: Ingest dedicated records for the critical martial/semiotic sub-variants (`Àrọ̀kọ̀ Ẹfà`, `Àrọ̀kọ̀ Ẹ̀jọ́`, `Ọ̀kọ̀ Ẹlẹ́ṣin`, `Ọfà Ọdẹ`, `Àdá Ìbílẹ̀`).
5. **Bilateral Knowledge Graph Linking (`Àgbẹ̀dẹ`)**: Explicitly wire the bilateral knowledge graphs for `Apẹja`, `Ẹja`, `Idà`, and `Ẹyẹ`.
6. **QA Zero-Shot Benchmark Signoff (`Sùúrù`)**: Test all 14 queries to confirm 100% Top-1 zero-shot retrieval.