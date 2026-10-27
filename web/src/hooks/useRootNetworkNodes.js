import { useMemo, useCallback } from 'react';
import { normalizeNFC, stripAccents, escapeRegExp } from '../utils/tonalContour';
import { hydrateSubVariantFromParent } from '../utils/subVariantHydrator';
import { findVisualRegaliaHit } from '../utils/bentoHydrator';

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
      if (hasDiacritics && tClean === qClean && tNFC !== qNFC) return false;
      return tNFC === qNFC || (!hasDiacritics && tClean === qClean) || wordBoundaryRegex.test(tClean) || aliasesClean.some((a) => a === qClean || wordBoundaryRegex.test(a));
    });

    if (matches.length === 0) return null;

    const exactMatch = matches.find((m) => normalizeNFC(m.title) === qNFC) ||
      matches.find((m) => stripAccents(m.title) === qClean && (m.is_parent === true || m.sovereign_parent_status === 'Sovereign Parent Concept')) ||
      matches.find((m) => stripAccents(m.title) === qClean);

    const matchedNode = exactMatch || matches.find((m) => m.is_parent === true || m.sovereign_parent_status === 'Sovereign Parent Concept') || matches[0];
    let parentNode = matchedNode;
    let childVariants = [];

    // Decouple Sovereign Parent / Living Sub-Variant hierarchy
    if (matchedNode.sovereign_parent && matchedNode.is_parent !== true) {
      const spClean = stripAccents(matchedNode.sovereign_parent);
      const trueParent = masterCorpus.find((m) =>
        normalizeNFC(m.title) === normalizeNFC(matchedNode.sovereign_parent) ||
        (stripAccents(m.title) === spClean && (m.is_parent === true || m.sovereign_parent_status === 'Sovereign Parent Concept')) ||
        stripAccents(m.title) === spClean
      );
      if (trueParent) {
        parentNode = trueParent;
        const siblings = Array.isArray(trueParent.sub_variants) ? resolveEntities(trueParent.sub_variants, trueParent) : [];
        childVariants = [matchedNode, ...siblings.filter((s) => s.title !== matchedNode.title)].slice(0, 4);
      }
    }

    if (childVariants.length === 0) {
      if (Array.isArray(parentNode.sub_variants) && parentNode.sub_variants.length > 0) {
        childVariants = resolveEntities(parentNode.sub_variants, parentNode).slice(0, 4);
      } else {
        childVariants = matches.filter((m) => m.title !== parentNode.title).slice(0, 4);
      }
    }

    const relatedRegalia = findVisualRegaliaHit(parentNode.title) || findVisualRegaliaHit(qTrim);

    return { query: qTrim, parent: parentNode, variants: childVariants, regalia: relatedRegalia, totalCount: matches.length };
  }, [masterCorpus, query, resolveEntities]);
}
