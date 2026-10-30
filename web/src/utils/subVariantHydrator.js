// ==============================================================================
// 🏛️ ÀGBÀ ENGINE: DYNAMIC SUB-VARIANT FALLBACK HYDRATOR (v6.2.0)
// ==============================================================================
// Zero-hardcoded, data-driven synthesis of unindexed sub-variant child nodes.
// Eliminates the "sub-variant resolving to parent" loop permanently.
// Specifications: AGY__REPORT_OYE_AUDIT_004.md (Part III) & HANDOFF-AGBEDE-004.
// ==============================================================================

import { getSubVariantDeepMetadata } from './subVariantKnowledge';

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function normalizeNFC(s) {
  return (s || '').trim().toLowerCase().normalize('NFC');
}

/**
 * Dynamically synthesizes a complete 14-tier child entity from its Sovereign Parent
 * enriched with authentic domain-aware metadata, multi-epoch timelines, and dual-language proverbs.
 * Guarantees is_parent: false, declares sovereign_parent, and prevents parent loop.
 */
export function hydrateSubVariantFromParent(variantTitle, parentEntity) {
  const variantClean = stripAccents(variantTitle);
  const pId = parentEntity.id || 'variant';
  const pTitle = parentEntity.title || 'Heritage';
  const pCat = parentEntity.category || 'Cultural Heritage';

  // Fetch specialized 14-Tier constellation metadata
  const deepMeta = getSubVariantDeepMetadata(variantTitle, parentEntity);

  const pTimeline = deepMeta.historical_timeline || parentEntity.historical_timeline || `Preserved through the generational lineage of ${pTitle}.`;
  const pCraft = deepMeta.material_and_craftsmanship || parentEntity.material_and_craftsmanship || 'Traditional luxury handcraft and guild metallurgy.';
  const pProverbs = deepMeta.proverbs_and_oral_traditions?.length > 0
    ? deepMeta.proverbs_and_oral_traditions
    : (parentEntity.proverbs_and_oral_traditions || []);

  const otherVariants = Array.isArray(parentEntity.sub_variants)
    ? parentEntity.sub_variants.filter((sv) => sv !== variantTitle)
    : [];

  const desc = deepMeta.description || `A specialized living variant within the ${pTitle} tradition, embodying ${variantTitle} in classical ${pCat}.`;
  const ritualContext = deepMeta.social_and_ritual_context || `Operates in direct ritual, ceremonial, and practical alignment with ${pTitle}.`;
  const provenance = deepMeta.provenance_and_citations || parentEntity.provenance_and_citations || '';

  return {
    id: `${pId}_${variantClean.replace(/\s+/g, '_')}`,
    title: variantTitle,
    culture: parentEntity.culture || 'Yorùbá',
    category: deepMeta.category || pCat,
    is_parent: false,
    sovereign_parent: pTitle,
    sovereign_parent_status: 'Living Sub-Variant',
    aliases: [variantTitle, variantClean],
    description: desc,
    historical_timeline: pTimeline,
    material_and_craftsmanship: pCraft,
    social_and_ritual_context: ritualContext,
    proverbs_and_oral_traditions: pProverbs,
    provenance_and_citations: provenance,
    diaspora_connections: deepMeta.diaspora_connections || parentEntity.diaspora_connections || '',
    geographical_origin: parentEntity.geographical_origin || 'Yorùbáland',
    media_production_notes: parentEntity.media_production_notes || '',
    sub_variants: [],
    related_entities: [pTitle, ...otherVariants],
    details: {
      culture: parentEntity.culture || 'Yorùbá',
      category: deepMeta.category || pCat,
      is_parent: false,
      sovereign_parent: pTitle,
      sovereign_parent_status: 'Living Sub-Variant',
      description: desc,
      historical_timeline: pTimeline,
      material_and_craftsmanship: pCraft,
      social_and_ritual_context: ritualContext,
      proverbs_and_oral_traditions: pProverbs,
      provenance_and_citations: provenance
    }
  };
}

/**
 * Data-driven matcher that searches all Sovereign Parents' sub_variants arrays.
 * Returns { variantTitle, parent } if query matches an unindexed child, else null.
 */
export function findSubVariantMatchInCorpus(query, masterCorpus) {
  if (!query || !Array.isArray(masterCorpus)) return null;
  const qTrim = (query || '').replace(/[?!.,;:'"]/g, '').trim();
  const qClean = stripAccents(qTrim);
  const qNFC = normalizeNFC(qTrim);
  if (qClean.length < 2) return null;

  // 1. If an exact standalone title/alias exists in masterCorpus, return null
  const exactStandalone = masterCorpus.find((e) => {
    const tNFC = normalizeNFC(e.title);
    const tClean = stripAccents(e.title);
    if (tNFC === qNFC || tClean === qClean) return true;
    return (e.aliases || []).some((a) => {
      const aClean = stripAccents(a);
      return aClean === qClean || normalizeNFC(a) === qNFC;
    });
  });
  if (exactStandalone) return null;

  // 2. Iterate across all Sovereign Parents to find parent owning this variant string
  for (const parent of masterCorpus) {
    if (!Array.isArray(parent.sub_variants)) continue;
    for (const sv of parent.sub_variants) {
      const svNFC = normalizeNFC(sv);
      const svClean = stripAccents(sv);
      if (svNFC === qNFC || svClean === qClean) {
        return { variantTitle: sv, parent };
      }
    }
  }

  return null;
}
