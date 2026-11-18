import { stripAccents } from './tonalContour';

export const ONTOLOGICAL_TIER = {
  SOVEREIGN_PARENT: 'SOVEREIGN_PARENT',
  LIVING_VARIANT: 'LIVING_VARIANT',
  AUTONOMOUS_CANON: 'AUTONOMOUS_CANON'
};

export function getOntologicalClassification(entity, masterCorpus = []) {
  if (!entity) return null;

  const entityTitleClean = stripAccents(entity.title || entity.details?.title || '');
  const entityId = entity.id || entity.details?.id;

  // 1. Immutable Sovereign Parent Rule
  const rawSubVariants = entity.sub_variants || entity.details?.sub_variants;
  const hasSubVariants = Array.isArray(rawSubVariants) && rawSubVariants.length > 0;
  const isExplicitParent = entity.is_parent === true || entity.details?.is_parent === true ||
    entity.sovereign_parent_status === 'Sovereign Parent Concept' || entity.details?.sovereign_parent_status === 'Sovereign Parent Concept';

  if (isExplicitParent || hasSubVariants) {
    return {
      tier: ONTOLOGICAL_TIER.SOVEREIGN_PARENT,
      parentTitle: null,
      subVariants: rawSubVariants || []
    };
  }

  // 2. Explicit Living Variant Rule
  const declaredParent = entity.sovereign_parent || entity.details?.sovereign_parent;
  if (declaredParent && entity.is_parent !== true && entity.details?.is_parent !== true) {
    return {
      tier: ONTOLOGICAL_TIER.LIVING_VARIANT,
      parentTitle: declaredParent,
      subVariants: []
    };
  }

  // 3. Reverse-Index Graph Verification across Master Corpus
  if (Array.isArray(masterCorpus) && masterCorpus.length > 0 && entityTitleClean) {
    const parentInCorpus = masterCorpus.find((p) => {
      if (!p || p.id === entityId || stripAccents(p.title) === entityTitleClean) return false;
      const pSVs = p.sub_variants || p.details?.sub_variants;
      if (!Array.isArray(pSVs) || pSVs.length === 0) return false;
      return pSVs.some((sv) => {
        const svTitle = typeof sv === 'string' ? sv : sv.title;
        return stripAccents(svTitle) === entityTitleClean;
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
