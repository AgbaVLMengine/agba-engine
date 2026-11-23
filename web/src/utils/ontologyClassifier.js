import { stripAccents, normalizeNFC } from './tonalContour';

export const ONTOLOGICAL_TIER = {
  SOVEREIGN_PARENT: 'SOVEREIGN_PARENT',
  LIVING_VARIANT: 'LIVING_VARIANT',
  AUTONOMOUS_CANON: 'AUTONOMOUS_CANON'
};

export function getOntologicalClassification(entity, masterCorpus = []) {
  if (!entity) return null;

  const entityTitleClean = stripAccents(entity.title || entity.details?.title || '');
  const entityId = entity.id || entity.details?.id;

  // 1. Explicit Living Variant Rule (Precedence over sub_variants when declared parent exists)
  const declaredParent = entity.sovereign_parent || entity.details?.sovereign_parent;
  const isExplicitParent = entity.is_parent === true || entity.details?.is_parent === true ||
    entity.sovereign_parent_status === 'Sovereign Parent Concept' || entity.details?.sovereign_parent_status === 'Sovereign Parent Concept';

  if (declaredParent && !isExplicitParent) {
    const parentClean = stripAccents(declaredParent);
    // Anti-Circularity Guard: an entity cannot claim itself as its Sovereign Parent
    if (parentClean !== entityTitleClean) {
      return {
        tier: ONTOLOGICAL_TIER.LIVING_VARIANT,
        parentTitle: declaredParent,
        subVariants: []
      };
    }
  }

  // 2. Immutable Sovereign Parent Rule
  const rawSubVariants = entity.sub_variants || entity.details?.sub_variants;
  const hasSubVariants = Array.isArray(rawSubVariants) && rawSubVariants.length > 0;

  if (isExplicitParent || hasSubVariants) {
    // Strip self-referential loops from sub_variants list
    const filteredSubVariants = (rawSubVariants || []).filter((sv) => {
      const svTitle = typeof sv === 'string' ? sv : sv?.title;
      return stripAccents(svTitle) !== entityTitleClean;
    });

    return {
      tier: ONTOLOGICAL_TIER.SOVEREIGN_PARENT,
      parentTitle: null,
      subVariants: filteredSubVariants
    };
  }

  // 3. Reverse-Index Graph Verification across Master Corpus (Strict Tone-Aware NFC Matching)
  const entityTitleNFC = normalizeNFC(entity.title || entity.details?.title || '').toLowerCase();
  if (Array.isArray(masterCorpus) && masterCorpus.length > 0 && entityTitleNFC) {
    const parentInCorpus = masterCorpus.find((p) => {
      if (!p || p.id === entityId || normalizeNFC(p.title || '').toLowerCase() === entityTitleNFC) return false;
      const pSVs = p.sub_variants || p.details?.sub_variants;
      if (!Array.isArray(pSVs) || pSVs.length === 0) return false;
      return pSVs.some((sv) => {
        const rawTitle = typeof sv === 'string' ? sv : (sv?.title || sv?.id || '');
        return normalizeNFC(rawTitle).toLowerCase() === entityTitleNFC;
      });
    });

    if (parentInCorpus) {
      return {
        tier: ONTOLOGICAL_TIER.LIVING_VARIANT,
        parentTitle: parentInCorpus.title,
        subVariants: []
      };
    }
  }

  // 4. Autonomous Sovereign Canon
  return {
    tier: ONTOLOGICAL_TIER.AUTONOMOUS_CANON,
    parentTitle: null,
    subVariants: []
  };
}
