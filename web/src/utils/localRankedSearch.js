import { stripAccents, normalizeNFC, escapeRegExp } from './tonalContour';

// RC-1 & RC-3 Local Ranked Search Fallback (Tonal Invariant Tiering)
export function searchRankedCorpus(q, masterCorpus = []) {
  const qClean = (q || '').replace(/[?!.,;:'"_\-()[\]]/g, ' ').replace(/\s+/g, ' ').trim();
  const coreSubject = qClean
    .replace(/^(who is|what is|tell me about|explain|who was|what was|meaning of|history of|where is|why is)\s+/i, '')
    .trim();

  const normQ = normalizeNFC(qClean);
  const normCore = normalizeNFC(coreSubject);
  const qStripped = stripAccents(qClean);
  const coreStripped = stripAccents(coreSubject);
  const hasQueryDiacritics = normQ !== qStripped;

  const stopWords = new Set([
    'who', 'what', 'where', 'why', 'how', 'tell', 'about', 'and', 'the',
    'for', 'with', 'is', 'are', 'was', 'were', 'yoruba', 'tradition', 'meaning'
  ]);
  const qTokens = qStripped.split(/\s+/).filter((w) => w.length > 1 && !stopWords.has(w));
  const scored = [];

  for (const entity of masterCorpus) {
    const title = entity.title || '';
    const normTitle = normalizeNFC(title);
    const titleStripped = stripAccents(title);
    const eid = entity.id || '';
    const normEid = normalizeNFC(eid);
    const eidStripped = stripAccents(eid).replace(/_/g, ' ');
    const aliases = entity.aliases || [];
    const normAliases = aliases.map(normalizeNFC);
    const aliasesStripped = aliases.map(stripAccents);
    const descStripped = stripAccents(entity.description || '');

    let score = 0;

    // 1A. Supreme Exact Tonal/Diacritic Match (+600)
    if (normCore && (normTitle === normCore || normEid === normCore)) score += 600;
    else if (normCore && normAliases.includes(normCore)) score += 540;
    else if (normQ && (normTitle === normQ || normEid === normQ)) score += 520;
    else if (normQ && normAliases.includes(normQ)) score += 480;

    // 1B. Accent-Folded Match (+450 if un-diacritized, +180 if conflicting tones)
    if (coreStripped && (titleStripped === coreStripped || eidStripped === coreStripped)) {
      score += hasQueryDiacritics && normTitle !== normCore ? 180 : 450;
    } else if (coreStripped && aliasesStripped.includes(coreStripped)) {
      score += hasQueryDiacritics && !normAliases.includes(normCore) ? 150 : 400;
    } else if (qStripped && (titleStripped === qStripped || eidStripped === qStripped)) {
      score += hasQueryDiacritics && normTitle !== normQ ? 160 : 380;
    } else if (qStripped && aliasesStripped.includes(qStripped)) {
      score += hasQueryDiacritics && !normAliases.includes(normQ) ? 140 : 340;
    }

    // 2. Word-boundary phrase match
    if (coreStripped && new RegExp(`\\b${escapeRegExp(coreStripped)}\\b`, 'i').test(titleStripped)) {
      score += 220;
    }

    // 3. Sovereign Parent root priority
    if (entity.is_parent === true || entity.sovereign_parent_status === 'Sovereign Parent Concept') {
      score += 25;
    }

    for (const tok of qTokens) {
      const wordRegex = new RegExp(`\\b${escapeRegExp(tok)}\\b`, 'i');
      if (wordRegex.test(titleStripped)) score += 50;
      if (aliasesStripped.some((a) => wordRegex.test(a))) score += 40;
      if (wordRegex.test(descStripped)) score += 8;
    }

    if (score > 0) scored.push({ entity, score });
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.map((s) => s.entity);
}
