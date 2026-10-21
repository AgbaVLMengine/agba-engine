// ==============================================================================
// 🏛️ ÀGBÀ ENGINE: GLOBAL KNOWLEDGE GRAPH RELATIVES RESOLVER (v6.2.0)
// ==============================================================================
// Eliminates static category-array slicing (which previously caused repeated
// 4-item sequences like Àlọ́ ÌJÀPÁ → Oríkì → Ewì → Rárà or Amàlà → Èlùbọ́).
// Evaluates:
//   1. Explicit sub_variants, related_entities, and cultural_relatives (NFC-first)
//   2. Reverse Sovereign Parent & sibling sub_variant lineage
//   3. Bi-directional cross-text mention & semantic/lexical token overlap
// ==============================================================================

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function normalizeNFC(s) {
  return (s || '').trim().toLowerCase().normalize('NFC');
}

const STOP_WORDS = new Set([
  'the', 'and', 'for', 'with', 'from', 'that', 'this', 'are', 'was', 'were',
  'used', 'known', 'also', 'into', 'during', 'across', 'within', 'their',
  'yoruba', 'yorùbá', 'traditional', 'sacred', 'ancient', 'cultural', 'people',
  'indigenous', 'nigeria', 'west', 'africa', 'century', 'system', 'symbol',
  'spiritual', 'ritual', 'social', 'history', 'origin', 'meaning', 'form'
]);

function extractGraphTokens(entity) {
  const d = entity.details || entity;
  const raw = [
    entity.title,
    ...(d.aliases || []),
    d.description,
    d.etymology_and_philosophy,
    d.social_and_ritual_context,
    d.material_and_craftsmanship,
    d.geographical_origin
  ]
    .filter(Boolean)
    .join(' ');

  const cleaned = stripAccents(raw).replace(/[^a-z0-9\s]/g, ' ');
  const tokens = new Set();
  for (const w of cleaned.split(/\s+/)) {
    if (w.length >= 4 && !STOP_WORDS.has(w)) {
      tokens.add(w);
    }
  }
  return tokens;
}

export function resolveKnowledgeGraphRelatives(topMatch, masterCorpus, limit = 6) {
  if (!topMatch || !Array.isArray(masterCorpus)) return [];
  const details = topMatch.details || topMatch;
  const selfTitleNFC = normalizeNFC(topMatch.title || details.title);
  const selfTitleClean = stripAccents(topMatch.title || details.title);
  const seenIds = new Set([topMatch.id, topMatch.title, details.id, details.title].filter(Boolean));
  const resolved = [];

  const pushUnique = (cand) => {
    if (!cand) return;
    if (seenIds.has(cand.id) || seenIds.has(cand.title)) return;
    if (normalizeNFC(cand.title) === selfTitleNFC) return;
    seenIds.add(cand.id);
    seenIds.add(cand.title);
    resolved.push(cand);
  };

  // Tier 1: Explicit sub_variants, related_entities, and cultural_relatives (NFC-first)
  const explicitNames = [
    ...(Array.isArray(details.sub_variants) ? details.sub_variants : []),
    ...(Array.isArray(details.related_entities) ? details.related_entities : []),
    ...(Array.isArray(details.cultural_relatives) ? details.cultural_relatives : [])
  ];

  for (const relName of explicitNames) {
    const relNFC = normalizeNFC(relName);
    const relClean = stripAccents(relName);
    const exactHit = masterCorpus.find(
      (e) => normalizeNFC(e.title) === relNFC || normalizeNFC(e.id) === relNFC
    );
    const fallbackHit =
      exactHit ||
      masterCorpus.find(
        (e) => e.id === relName || stripAccents(e.title) === relClean
      );
    pushUnique(fallbackHit);
  }

  // Tier 2: Reverse Sovereign Parent & Sibling Lineage
  if (resolved.length < limit) {
    for (const parentCand of masterCorpus) {
      if (!Array.isArray(parentCand.sub_variants)) continue;
      const hasSelfInVariants = parentCand.sub_variants.some(
        (sv) => normalizeNFC(sv) === selfTitleNFC || stripAccents(sv) === selfTitleClean
      );
      if (hasSelfInVariants) {
        pushUnique(parentCand);
        for (const siblingName of parentCand.sub_variants) {
          if (resolved.length >= limit) break;
          const sibNFC = normalizeNFC(siblingName);
          const sibHit = masterCorpus.find((e) => normalizeNFC(e.title) === sibNFC);
          pushUnique(sibHit);
        }
      }
    }
  }

  // Tier 3: Global Semantic & Lexical Knowledge Graph Scorer (Zero Static Slicing)
  if (resolved.length < limit) {
    const selfTokens = extractGraphTokens(topMatch);
    const selfFullText = stripAccents(
      [details.description, details.etymology_and_philosophy, details.social_and_ritual_context]
        .filter(Boolean)
        .join(' ')
    );
    const selfCategory = topMatch.category || details.category;
    const scoredCandidates = [];

    for (const cand of masterCorpus) {
      if (seenIds.has(cand.id) || seenIds.has(cand.title)) continue;
      const candTitleClean = stripAccents(cand.title);
      if (!candTitleClean || candTitleClean === selfTitleClean) continue;

      let score = 0;

      // Bi-directional cross-reference in text
      if (candTitleClean.length >= 4 && selfFullText.includes(candTitleClean)) {
        score += 85;
      }
      const candDescClean = stripAccents(
        [cand.description, cand.etymology_and_philosophy, cand.social_and_ritual_context]
          .filter(Boolean)
          .join(' ')
      );
      if (selfTitleClean.length >= 4 && candDescClean.includes(selfTitleClean)) {
        score += 80;
      }

      // Shared lexical/philosophical tokens
      const candTokens = extractGraphTokens(cand);
      let sharedCount = 0;
      for (const tok of selfTokens) {
        if (candTokens.has(tok)) sharedCount += 1;
      }
      score += sharedCount * 18;

      if (selfCategory && cand.category === selfCategory) {
        score += 14;
      }
      if (cand.is_parent === true) {
        score += 6;
      }

      if (score > 14) {
        scoredCandidates.push({ cand, score });
      }
    }

    scoredCandidates.sort((a, b) => b.score - a.score);
    for (const item of scoredCandidates) {
      if (resolved.length >= limit) break;
      pushUnique(item.cand);
    }
  }

  return resolved.slice(0, limit);
}
