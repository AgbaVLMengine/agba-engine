/**
 * ÀGBÀ ENGINE: ONOMASTIC ZERO-SHOT RETRIEVAL BRIDGE
 * Connects personal Yorùbá names (e.g. Yetunde, Ibukun, Temilade, Morenikeji)
 * directly to their canonical Sovereign Parents at Rank #1.
 *
 * Enforces:
 *   - Sùúrù's Canonical Sovereign Alias Map
 *   - Òye's Anti-Shadowing Rule (Canonical corpus entities take precedence)
 *   - Àgbẹ̀dẹ's Weak Noise Preemption (Onomastic names preempt weak fuzzy hits)
 *   - Òye's Gate 9 Invariant Sanitizer (Biographical & Metaphysical safety)
 */

import { decomposeYorubaName } from './onomasticDecomposer.js';
import { stripAccents, normalizeNFC } from './tonalContour.js';

export const SOVEREIGN_ALIAS_MAP = {
  'Owó Ẹyọ': 'eyo_owo',
  'Ẹyọ Owó': 'eyo_owo',
  'Akín': 'Ògún',
  'Ayọ̀': 'Ẹbí',
  'Ọ̀rọ̀': 'Òye'
};

export function resolveOnomasticZeroShot(query, masterCorpus = [], existingResults = []) {
  if (!query || typeof query !== 'string' || !masterCorpus.length) return null;
  const qClean = query.trim();
  const qNorm = normalizeNFC(stripAccents(qClean).toLowerCase());

  // 1. Òye's Anti-Shadowing Rule: If an exact canonical corpus entity matches, do not synthesize
  const exactMatch = masterCorpus.find((e) => {
    const tNorm = normalizeNFC(stripAccents(e.title || '').toLowerCase());
    const idNorm = normalizeNFC(stripAccents(e.id || '').toLowerCase());
    return tNorm === qNorm || idNorm === qNorm;
  });
  if (exactMatch) return null;

  // 2. Perform 5-Class Onomastic Decomposition
  const decomposition = decomposeYorubaName(qClean);
  if (!decomposition || !decomposition.sovereign_parents || !decomposition.sovereign_parents.length) {
    return null;
  }

  // 3. Locate Primary Sovereign Parent in master corpus (resolving canonical aliases)
  const primaryParentName = decomposition.sovereign_parents[0];
  const mappedTarget = SOVEREIGN_ALIAS_MAP[primaryParentName] || primaryParentName;
  const targetNorm = normalizeNFC(stripAccents(mappedTarget).toLowerCase());

  const parentEntity = masterCorpus.find((e) => {
    const eid = normalizeNFC(stripAccents(e.id || '').toLowerCase());
    const etitle = normalizeNFC(stripAccents(e.title || '').toLowerCase());
    return eid === targetNorm || etitle === targetNorm;
  }) || masterCorpus.find((e) => {
    const etitle = normalizeNFC(stripAccents(e.title || '').toLowerCase());
    return etitle.startsWith(targetNorm);
  });

  if (!parentEntity) return null;

  // 4. Òye's Gate 9 Invariant Sanitizer & Metadata Synthesis
  let sanitizedDesc = parentEntity.description || '';
  if (parentEntity.title === 'Bàbá' || primaryParentName === 'Bàbá') {
    sanitizedDesc = 'Ancestral patriarch, elder custodian & compound pillar. ' + sanitizedDesc;
  }

  const cleanParentTitle = parentEntity.title.replace(/\s*\(.*?\)/g, '').trim();

  return {
    ...parentEntity,
    id: `onomastic_${decomposition.canonical_name.toLowerCase().replace(/[^a-z0-9]/g, '_')}`,
    title: `${cleanParentTitle} (${decomposition.canonical_name})`,
    canonical_name: decomposition.canonical_name,
    is_synthesized: true,
    is_parent: true,
    sovereign_parent_status: 'Onomastic Lineage Anchor',
    category: parentEntity.category || 'Social Structure, Kinship & Lineage',
    score: 0.99,
    description: sanitizedDesc,
    onomastic_card: {
      ribbon: `🏷️ Orúkọ Mi: "${decomposition.canonical_name}" • Ancestral Lineage of ${parentEntity.title}`,
      canonical_name: decomposition.canonical_name,
      grammatical_class: decomposition.grammatical_class,
      lineage_meaning: decomposition.lineage_meaning,
      lineage_covenant: decomposition.lineage_covenant,
      morphemes: decomposition.morphemes,
      sovereign_parents: decomposition.sovereign_parents
    }
  };
}
