import { normalizeNFC, stripAccents } from './tonalContour';

/**
 * ⚖️ Detects whether an ASCII query without diacritics maps to multiple
 * distinct canonical entities across different tonal contours (homographs).
 *
 * Examples:
 *   "oko" -> Ọkọ (Husband), Ọkọ́ (Hoe), Oko (Farm), Ọ̀kọ̀ (Spear)
 *   "aja" -> Àjà (Whirlwind Spirit), Ajá (Dog)
 *   "oba" -> Ọba (Monarch), Ọbá (River Divinity)
 *   "ogun" -> Ògún (Divinity of Iron), Ogun (Warfare)
 */
export function detectTonalHomographs(query, masterCorpus = []) {
  if (!query || !Array.isArray(masterCorpus)) return [];
  const qTrim = query.trim();
  if (qTrim.length < 2) return [];

  const qClean = stripAccents(qTrim).toLowerCase();
  const qNFC = normalizeNFC(qTrim).toLowerCase();

  // If user already typed authentic diacritics, honor their explicit intent (bypass fork)
  if (qNFC !== qClean) return [];

  const seenTitles = new Set();
  const candidates = [];

  for (const item of masterCorpus) {
    if (!item?.title) continue;
    const baseTitleClean = stripAccents(item.title.replace(/\s*\([^)]*\)/g, '').trim()).toLowerCase();

    if (baseTitleClean === qClean) {
      const titleKey = normalizeNFC(item.title).toLowerCase();
      if (!seenTitles.has(titleKey)) {
        seenTitles.add(titleKey);
        candidates.push(item);
      }
    }
  }

  // Only fork if 2 or more distinct tonal homographs exist
  return candidates.length > 1 ? candidates : [];
}
