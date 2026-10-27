export function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

export function normalizeNFC(s) {
  return (s || '').trim().toLowerCase().normalize('NFC');
}

export function escapeRegExp(s) {
  return (s || '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Generate tonal contour breakdown using NFC/NFD grapheme clusters (High: ´, Low: `, Mid: none)
export function extractTonalContour(word) {
  if (!word) return [];
  const firstWord = word.normalize('NFC').split(/\s+/)[0] || word;
  const tones = [];
  const segments = Array.from(firstWord);

  for (const ch of segments) {
    const nfd = ch.normalize('NFD');
    const base = nfd[0]?.toLowerCase() || '';
    if (!'aeiouẹọ'.includes(base) && !'aeiou'.includes(nfd[0]?.toLowerCase())) continue;

    if (nfd.includes('\u0301')) {
      tones.push({ char: ch.normalize('NFC'), pitch: 'High (Mí)', arrow: '↗' });
    } else if (nfd.includes('\u0300')) {
      tones.push({ char: ch.normalize('NFC'), pitch: 'Low (Dò)', arrow: '↘' });
    } else {
      tones.push({ char: ch.normalize('NFC'), pitch: 'Mid (Rè)', arrow: '→' });
    }
  }
  return tones.slice(0, 5);
}
