/**
 * ÀGBÀ ENGINE: ONOMASTIC LINEAGE GATEWAY ("ORÚKỌ MI" DRAWER 2 - ALGORITHMIC PARSER)
 * Lean, zero-bloat 5-Class Yorùbá Morphological Engine & Tonal Decomposer (< 200 LOC).
 * Decomposes names into constituent root morphemes and connects them to Sovereign Parents.
 *
 * Imports static linguistic datasets from Drawer 1 (onomasticLexicon.js).
 */

import {
  GRAMMATICAL_CLASSES,
  ONOMASTIC_PREFIXES,
  ONOMASTIC_SUFFIXES,
  AMUTORUNWA_NAMES,
  CANONICAL_ONOMASTIC_REGISTRY
} from './onomasticLexicon.js';

// Re-export lexical structures to preserve backwards-compatibility
export {
  GRAMMATICAL_CLASSES,
  ONOMASTIC_PREFIXES,
  ONOMASTIC_SUFFIXES,
  AMUTORUNWA_NAMES,
  CANONICAL_ONOMASTIC_REGISTRY
};

/**
 * Decomposes a single normalized Yorùbá onomastic token across all 5 classes.
 */
function decomposeSingleToken(token) {
  let clean = token
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z]/g, '');
  if (clean.length < 3 || ['mrs', 'mr', 'miss', 'chief', 'dr', 'prof'].includes(clean)) return null;

  // Epenthetic & phonetic slang-folding (Sùúrù Rule)
  clean = clean.replace(/sh/g, 's');
  if (clean === 'kofoworaola') clean = 'kofoworola';
  if (clean.startsWith('lanrewaju')) clean = 'olanrewaju';

  // 1. Direct registry lookup across 5 Grammatical Classes
  if (CANONICAL_ONOMASTIC_REGISTRY[clean]) {
    return CANONICAL_ONOMASTIC_REGISTRY[clean];
  }

  // 2. Class C: Sacred Birth Circumstance Names (Orúkọ Àmútọ̀runwá)
  if (AMUTORUNWA_NAMES[clean]) {
    const item = AMUTORUNWA_NAMES[clean];
    return {
      canonical_name: item.canonical_name,
      grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
      morphemes: [{ morpheme: item.canonical_name, meaning: item.circumstance, sovereign_parent: item.sovereign_parent, category: 'Social Structure, Kinship & Lineage' }],
      lineage_meaning: item.circumstance,
      lineage_covenant: 'Sacred Birth Circumstance & Consecrated Destined Covenant',
      sovereign_parents: [item.sovereign_parent].filter(Boolean)
    };
  }

  // 3. Class B: Possessive/Pronominal Prefix Decomposition
  if (clean.startsWith('temi') || clean.startsWith('tiwa')) {
    const isTemi = clean.startsWith('temi');
    const pDiacritic = isTemi ? 'Tèmi' : 'Tíwa';
    const remainder = clean.slice(4);
    if (remainder.startsWith('la') || remainder.startsWith('lo') || remainder.startsWith('to')) {
      const traitKey = remainder.slice(1);
      const matchedSuffix = ONOMASTIC_SUFFIXES[traitKey] || ONOMASTIC_SUFFIXES[remainder];
      const traitName = matchedSuffix ? matchedSuffix.diacritic : traitKey.charAt(0).toUpperCase() + traitKey.slice(1);
      return {
        canonical_name: `${pDiacritic}${remainder.charAt(0)}${traitName.toLowerCase()}`,
        grammatical_class: GRAMMATICAL_CLASSES.CLASS_B,
        morphemes: [
          { morpheme: pDiacritic, meaning: isTemi ? 'Belongs to me' : 'Belongs to us collectively', sovereign_parent: 'Ẹbí', category: 'Social Structure, Kinship & Lineage' },
          { morpheme: remainder, meaning: `Affirmation of ${traitName}`, sovereign_parent: 'Ọlá' }
        ],
        lineage_meaning: `${pDiacritic} affirms rightful inheritance and ownership of ${traitName}.`,
        lineage_covenant: 'Possessive Claimants of Honor', sovereign_parents: ['Ọlá', 'Ẹbí']
      };
    }
  }

  // 4. Class D: Contracted Ancestral Return Decomposition (Àtúnwá)
  if (clean.startsWith('ye') || clean.startsWith('iya') || clean.startsWith('baba')) {
    let pDiac = 'Yèyé', pKeyLen = 2, sParent = 'Ìyá';
    if (clean.startsWith('iya')) { pDiac = 'Ìyá'; pKeyLen = 3; sParent = 'Ìyá'; }
    else if (clean.startsWith('baba')) { pDiac = 'Bàbá'; pKeyLen = 4; sParent = 'Bàbá'; }
    const remainder = clean.slice(pKeyLen);
    if (['tunde', 'jide', 'bode', 'wale', 'wande', 'bo'].includes(remainder)) {
      const sfx = ONOMASTIC_SUFFIXES[remainder] || { diacritic: remainder.charAt(0).toUpperCase() + remainder.slice(1), meaning: 'Ancestral rebirth' };
      return {
        canonical_name: `${pDiac}${sfx.diacritic.toLowerCase()}`,
        grammatical_class: GRAMMATICAL_CLASSES.CLASS_D,
        morphemes: [
          { morpheme: pDiac, meaning: `Revered ancestral ${sParent.toLowerCase()}`, sovereign_parent: sParent, category: 'Social Structure, Kinship & Lineage' },
          { morpheme: sfx.diacritic, meaning: sfx.meaning, sovereign_parent: 'Ẹbí' }
        ],
        lineage_meaning: `The revered ancestral ${sParent.toLowerCase()} has returned to the homestead (${sfx.meaning}).`,
        lineage_covenant: 'Ancestral Reincarnation & Lineage Continuity', sovereign_parents: [sParent, 'Ẹbí']
      };
    }
  }

  // 5. Class E: Proverbial Clauses (Sentence Names)
  if (clean.startsWith('kofo') || clean.startsWith('kosi') || clean.startsWith('fowo') || clean.startsWith('moren') || clean.startsWith('modu') || clean.startsWith('koso')) {
    const sfx = ONOMASTIC_SUFFIXES[clean];
    if (sfx) {
      return {
        canonical_name: sfx.diacritic,
        grammatical_class: GRAMMATICAL_CLASSES.CLASS_E,
        morphemes: [{ morpheme: sfx.diacritic, meaning: sfx.meaning, sovereign_parent: 'Ọ̀rọ̀', category: 'Oral Literature, Philosophy & Folklore' }],
        lineage_meaning: sfx.meaning,
        lineage_covenant: 'Philosophical Proverbial Lineage', sovereign_parents: ['Ọ̀rọ̀', 'Ọlá']
      };
    }
  }

  // 6. Class A: Systematic Theophoric/Nominal Prefix + 120+ Verbal Suffixes
  const prefixKeys = Object.keys(ONOMASTIC_PREFIXES).sort((a, b) => b.length - a.length);
  for (const pKey of prefixKeys) {
    if (clean.startsWith(pKey)) {
      const remainder = clean.slice(pKey.length);
      const prefixMeta = ONOMASTIC_PREFIXES[pKey];
      const suffixKeys = Object.keys(ONOMASTIC_SUFFIXES).sort((a, b) => b.length - a.length);
      for (const sKey of suffixKeys) {
        if (remainder === sKey || remainder.startsWith(sKey)) {
          const suffixMeta = ONOMASTIC_SUFFIXES[sKey];
          const fullDiacritic = `${prefixMeta.diacritic}${suffixMeta.diacritic.toLowerCase()}`;
          return {
            canonical_name: fullDiacritic,
            grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
            morphemes: [
              { morpheme: prefixMeta.diacritic, meaning: prefixMeta.meaning, sovereign_parent: prefixMeta.sovereign_parent, category: prefixMeta.category },
              { morpheme: suffixMeta.diacritic, meaning: suffixMeta.meaning, sovereign_parent: null }
            ],
            lineage_meaning: `${prefixMeta.diacritic} (${prefixMeta.meaning.split(',')[0]}) combines with ${suffixMeta.diacritic.toLowerCase()} (${suffixMeta.meaning.toLowerCase()}).`,
            lineage_covenant: `${prefixMeta.sovereign_parent} Lineage Covenant`, sovereign_parents: [prefixMeta.sovereign_parent].filter(Boolean)
          };
        }
      }

      // Contextual verbal predicate fallback (Never "Lineage morphological extension")
      if (remainder.length > 0) {
        const capitalizedRemainder = remainder.charAt(0).toUpperCase() + remainder.slice(1);
        return {
          canonical_name: `${prefixMeta.diacritic}${remainder}`,
          grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
          morphemes: [
            { morpheme: prefixMeta.diacritic, meaning: prefixMeta.meaning, sovereign_parent: prefixMeta.sovereign_parent, category: prefixMeta.category },
            { morpheme: capitalizedRemainder, meaning: `Verbal predicate signifying the manifest action of ${prefixMeta.diacritic}`, sovereign_parent: null }
          ],
          lineage_meaning: `Lineage anchored in ${prefixMeta.diacritic} (${prefixMeta.meaning.split(',')[0]}).`,
          lineage_covenant: `${prefixMeta.sovereign_parent} Heritage`, sovereign_parents: [prefixMeta.sovereign_parent].filter(Boolean)
        };
      }
    }
  }

  // 7. Direct match inside 120+ ONOMASTIC_SUFFIXES (e.g. standalone oríkì / orúkọ àmútọ̀runwá)
  if (ONOMASTIC_SUFFIXES[clean]) {
    const sfx = ONOMASTIC_SUFFIXES[clean];
    return {
      canonical_name: sfx.diacritic,
      grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
      morphemes: [{ morpheme: sfx.diacritic, meaning: sfx.meaning, sovereign_parent: 'Ẹbí', category: 'Social Structure, Kinship & Lineage' }],
      lineage_meaning: sfx.meaning,
      lineage_covenant: 'Ancestral Oríkì & Consecrated Birth Covenant', sovereign_parents: ['Ẹbí']
    };
  }

  return null;
}

/**
 * Decomposes any Yorùbá name, surname, or multi-part name phrase into morphemes,
 * resolves orthography, and extracts matching Sovereign Parents.
 */
export function decomposeYorubaName(rawName) {
  if (!rawName || typeof rawName !== 'string') return null;
  const tokens = rawName.trim().split(/\s+/).filter(Boolean);
  if (tokens.length === 0) return null;

  const resolved = tokens.map(decomposeSingleToken).filter(Boolean);
  if (resolved.length === 0) return null;
  if (resolved.length === 1) return resolved[0];

  return {
    canonical_name: resolved.map((r) => r.canonical_name).join(' '),
    grammatical_class: resolved[0].grammatical_class,
    morphemes: resolved.flatMap((r) => r.morphemes),
    lineage_meaning: resolved.map((r) => `${r.canonical_name}: ${r.lineage_meaning}`).join(' • '),
    lineage_covenant: resolved.map((r) => r.lineage_covenant).join(' & '),
    sovereign_parents: Array.from(new Set(resolved.flatMap((r) => r.sovereign_parents)))
  };
}
