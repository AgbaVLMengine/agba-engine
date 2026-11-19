import { useMemo, useCallback } from 'react';
import { normalizeNFC, stripAccents, escapeRegExp } from '../utils/tonalContour';
import { hydrateSubVariantFromParent } from '../utils/subVariantHydrator';
import { findVisualRegaliaHit } from '../utils/bentoHydrator';
import { getOntologicalClassification, ONTOLOGICAL_TIER } from '../utils/ontologyClassifier';

export function resolveSubVariantEntities(subVariantNames = [], parentNode = null, masterCorpus = []) {
  const resolved = [];
  for (const svName of subVariantNames) {
    const svNFC = normalizeNFC(svName);
    const svClean = stripAccents(svName);
    const hit = masterCorpus.find((e) => normalizeNFC(e.title) === svNFC || normalizeNFC(e.id) === svNFC) ||
      masterCorpus.find((e) => stripAccents(e.title) === svClean || e.id === svName);
    if (hit) {
      resolved.push(hit);
    } else if (parentNode) {
      resolved.push(hydrateSubVariantFromParent(svName, parentNode));
    } else {
      resolved.push({ id: `variant_${svClean}`, title: svName, category: 'Living Sub-Variant', description: `Canonical living variant within the ${svName} lineage.` });
    }
  }
  return resolved;
}

export function useRootNetworkNodes(query, masterCorpus = []) {
  const resolveEntities = useCallback(
    (subVariantNames = [], parentNode = null) => resolveSubVariantEntities(subVariantNames, parentNode, masterCorpus),
    [masterCorpus]
  );

  return useMemo(() => {
    const qTrim = (query || '').trim();
    if (!qTrim || qTrim.length < 2) return null;
    const qNFC = normalizeNFC(qTrim);
    const qClean = stripAccents(qTrim);
    const hasDiacritics = qNFC !== qClean;
    const wordBoundaryRegex = new RegExp(`\\b${escapeRegExp(qClean)}\\b`, 'i');

    const matches = masterCorpus.filter((item) => {
      const tNFC = normalizeNFC(item.title);
      const tClean = stripAccents(item.title);
      const aliasesClean = (item.aliases || []).map(stripAccents);
      const aliasesNFC = (item.aliases || []).map(normalizeNFC);
      const baseTitleClean = stripAccents(item.title.replace(/\s*\([^)]*\)/g, '').trim());
      const baseTitleNFC = normalizeNFC(item.title.replace(/\s*\([^)]*\)/g, '').trim());

      if (hasDiacritics && tClean === qClean && tNFC !== qNFC) return false;
      return (
        tNFC === qNFC ||
        (!hasDiacritics && tClean === qClean) ||
        baseTitleNFC === qNFC ||
        (!hasDiacritics && baseTitleClean === qClean) ||
        aliasesNFC.some((a) => a === qNFC) ||
        aliasesClean.some((a) => a === qClean) ||
        wordBoundaryRegex.test(tClean) ||
        aliasesClean.some((a) => wordBoundaryRegex.test(a))
      );
    });

    if (matches.length === 0) return null;

    // Strict 3-Tier Match Precedence:
    // 1. Exact full title match (with or without accents)
    // 2. Base title match stripping parenthetical qualifiers (e.g. "Àjà (Forest Whirlwind Spirit)" matches "Àjà")
    // 3. Exact full alias match
    // 4. Fallback to ranked list
    const exactMatch =
      matches.find((m) => normalizeNFC(m.title) === qNFC) ||
      matches.find((m) => stripAccents(m.title) === qClean) ||
      matches.find((m) => normalizeNFC(m.title.replace(/\s*\([^)]*\)/g, '').trim()) === qNFC) ||
      matches.find((m) => stripAccents(m.title.replace(/\s*\([^)]*\)/g, '').trim()) === qClean) ||
      matches.find((m) => (m.aliases || []).some((a) => normalizeNFC(a) === qNFC)) ||
      matches.find((m) => (m.aliases || []).some((a) => stripAccents(a) === qClean));

    // Never greedily elevate unrelated parents: use exact match or primary rank
    const matchedNode = exactMatch || matches[0];
    const classification = getOntologicalClassification(matchedNode, masterCorpus);
    let parentNode = matchedNode;
    let childVariants = [];

    if (classification.tier === ONTOLOGICAL_TIER.LIVING_VARIANT && classification.parentTitle) {
      const spClean = stripAccents(classification.parentTitle);
      const trueParent = masterCorpus.find((m) =>
        normalizeNFC(m.title) === normalizeNFC(classification.parentTitle) ||
        stripAccents(m.title) === spClean
      );
      if (trueParent) {
        parentNode = trueParent;
        const siblings = Array.isArray(trueParent.sub_variants) ? resolveEntities(trueParent.sub_variants, trueParent) : [];
        childVariants = [matchedNode, ...siblings.filter((s) => stripAccents(s.title) !== stripAccents(matchedNode.title))].slice(0, 4);
      }
    } else if (classification.tier === ONTOLOGICAL_TIER.SOVEREIGN_PARENT) {
      parentNode = matchedNode;
      if (Array.isArray(classification.subVariants) && classification.subVariants.length > 0) {
        childVariants = resolveEntities(classification.subVariants, parentNode)
          .filter((s) => stripAccents(s.title) !== stripAccents(matchedNode.title))
          .slice(0, 4);
      }
    } else {
      // Autonomous Canon: self-contained node, siblings from related category/matches
      parentNode = matchedNode;
      childVariants = matches.filter((m) => stripAccents(m.title) !== stripAccents(parentNode.title)).slice(0, 4);
    }

    const relatedRegalia = findVisualRegaliaHit(parentNode.title) || findVisualRegaliaHit(qTrim);

    return { query: qTrim, parent: parentNode, variants: childVariants, regalia: relatedRegalia, totalCount: matches.length };
  }, [masterCorpus, query, resolveEntities]);
}
