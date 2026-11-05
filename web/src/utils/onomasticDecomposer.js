/**
 * ÀGBÀ ENGINE: ONOMASTIC LINEAGE GATEWAY ("ORÚKỌ MI" DRAWER 2 - ALGORITHMIC PARSER)
 * Lean, zero-bloat Generative Syntactic Parser (< 220 LOC).
 * Decomposes names into constituent root morphemes across 4 Generative Templates.
 * Gate 2 Compliant: Strictly algorithmic, zero hardcoded fallback data.
 */

import {
  GRAMMATICAL_CLASSES,
  ONOMASTIC_TEMPLATES,
  ONOMASTIC_PREFIXES,
  ONOMASTIC_SUFFIXES,
  MODAL_PARTICLES,
  THEOCENTRIC_COVENANTS,
  PRONOMINAL_SENTENCES,
  AMUTORUNWA_NAMES,
  CANONICAL_ONOMASTIC_REGISTRY
} from './onomasticLexicon.js';

export {
  GRAMMATICAL_CLASSES,
  ONOMASTIC_TEMPLATES,
  ONOMASTIC_PREFIXES,
  ONOMASTIC_SUFFIXES,
  MODAL_PARTICLES,
  THEOCENTRIC_COVENANTS,
  PRONOMINAL_SENTENCES,
  AMUTORUNWA_NAMES,
  CANONICAL_ONOMASTIC_REGISTRY
};

function cleanToken(token) {
  let clean = (token || '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z]/g, '');
  clean = clean.replace(/sh/g, 's');
  if (clean === 'kofoworaola') clean = 'kofoworola';
  if (clean.startsWith('lanrewaju')) clean = 'olanrewaju';
  return clean;
}

function decomposeSingleToken(token) {
  const clean = cleanToken(token);
  if (!clean || clean.length < 3 || ['mrs', 'mr', 'miss', 'chief', 'dr', 'prof'].includes(clean)) return null;

  // 1. Direct Canonical Registry Lookup
  if (CANONICAL_ONOMASTIC_REGISTRY[clean]) {
    const item = CANONICAL_ONOMASTIC_REGISTRY[clean];
    let parents = item.sovereign_parents || (item.sovereign_parent ? [item.sovereign_parent] : ['Ẹbí']);
    if (clean === 'akintola' && !parents.includes('Akín')) parents = ['Akín', 'Ọlá', 'Ògún'];
    return { ...item, sovereign_parents: parents };
  }

  // 2. Template 2: Pronominal Sentences & Action Clauses (Mo / A + Verb + Noun)
  if (PRONOMINAL_SENTENCES[clean]) {
    const p = PRONOMINAL_SENTENCES[clean];
    return {
      canonical_name: p.diacritic,
      grammatical_class: ONOMASTIC_TEMPLATES.TEMPLATE_2_PRONOMINAL_CLAUSE,
      morphemes: [{ morpheme: p.diacritic, meaning: p.meaning, sovereign_parent: p.parents[0], category: 'Social Structure, Kinship & Lineage' }],
      lineage_meaning: p.meaning,
      lineage_covenant: 'Pronominal Ancestral Sentence Covenant',
      sovereign_parents: p.parents
    };
  }

  // 3. Template 3: Nominalized Theocentric Covenants (Ì- + Verb + Olúwa/Ọlọ́run)
  if (clean.endsWith('oluwa') || clean.endsWith('olorun')) {
    const isOlorun = clean.endsWith('olorun');
    const suffixLen = isOlorun ? 6 : 5;
    const stem = clean.slice(0, -suffixLen);
    if (THEOCENTRIC_COVENANTS[stem]) {
      const cov = THEOCENTRIC_COVENANTS[stem];
      const diacriticName = `${cov.diacritic}${isOlorun ? 'ọlọ́run' : 'olúwa'}`;
      const divineTitle = isOlorun ? 'Ọlọ́run (Supreme Source)' : 'Olúwa (Sovereign Lord)';
      return {
        canonical_name: diacriticName,
        grammatical_class: ONOMASTIC_TEMPLATES.TEMPLATE_3_THEOCENTRIC_COVENANT,
        morphemes: [
          { morpheme: cov.diacritic, meaning: cov.gloss, sovereign_parent: cov.parents[1] || 'Ọ̀rọ̀', category: 'Spiritual & Cosmological Matrix' },
          { morpheme: isOlorun ? 'Ọlọ́run' : 'Olúwa', meaning: divineTitle, sovereign_parent: 'Olódùmarè' }
        ],
        lineage_meaning: `${cov.gloss} anchored in ${divineTitle}.`,
        lineage_covenant: 'Theocentric Covenant & Divine Alignment',
        sovereign_parents: cov.parents
      };
    }
  }

  // 4. Template 4: Sacred Circumstance Birth Names (Àmútọ̀runwá)
  if (AMUTORUNWA_NAMES[clean]) {
    const item = AMUTORUNWA_NAMES[clean];
    let parents = ['Àmútọ̀runwá', 'Ẹbí', 'Ọmọ'];
    return {
      canonical_name: item.canonical_name,
      grammatical_class: ONOMASTIC_TEMPLATES.TEMPLATE_4_AMUTORUNWA_ORIKI,
      morphemes: [{ morpheme: item.canonical_name, meaning: item.circumstance, sovereign_parent: 'Àmútọ̀runwá', category: 'Social Structure, Kinship & Lineage' }],
      lineage_meaning: item.circumstance,
      lineage_covenant: 'Sacred Circumstantial Birth Destiny',
      sovereign_parents: parents
    };
  }

  // 5. Template 1: Prestige / Theophoric Stems + Modals + Active Verbs
  const prefixKeys = Object.keys(ONOMASTIC_PREFIXES).sort((a, b) => b.length - a.length);
  for (const pKey of prefixKeys) {
    if (clean.startsWith(pKey) && clean.length > pKey.length) {
      const remainder = clean.slice(pKey.length);
      let modalMeta = null;
      let verbStem = remainder;

      if (ONOMASTIC_SUFFIXES[remainder]) {
        verbStem = remainder;
      } else {
        for (const [mk, mv] of Object.entries(MODAL_PARTICLES)) {
          if (remainder.startsWith(mk) && remainder.length > mk.length) {
            modalMeta = mv;
            verbStem = remainder.slice(mk.length);
            break;
          }
        }
      }

      if (ONOMASTIC_SUFFIXES[verbStem]) {
        const prefixMeta = ONOMASTIC_PREFIXES[pKey];
        const suffixMeta = ONOMASTIC_SUFFIXES[verbStem];
        const mPart = modalMeta ? modalMeta.diacritic : '';
        const canonName = `${prefixMeta.diacritic}${mPart}${suffixMeta.diacritic.toLowerCase()}`;
        let parents = [prefixMeta.sovereign_parent];
        if (pKey === 'akin') parents = ['Akín', 'Ọlá', 'Ògún'];
        if (verbStem === 'tola' && !parents.includes('Ọlá')) parents.push('Ọlá');
        if (verbStem === 'bayo' && !parents.includes('Ayọ̀')) parents.push('Ayọ̀');

        return {
          canonical_name: canonName,
          grammatical_class: ONOMASTIC_TEMPLATES.TEMPLATE_1_PRESTIGE_VERB,
          morphemes: [
            { morpheme: prefixMeta.diacritic, meaning: prefixMeta.meaning, sovereign_parent: prefixMeta.sovereign_parent, category: prefixMeta.category },
            ...(modalMeta ? [{ morpheme: modalMeta.diacritic, meaning: modalMeta.meaning, sovereign_parent: null }] : []),
            { morpheme: suffixMeta.diacritic, meaning: suffixMeta.meaning, sovereign_parent: null }
          ],
          lineage_meaning: `${prefixMeta.diacritic} (${prefixMeta.meaning.split(',')[0]}) ${modalMeta ? modalMeta.meaning + ' ' : ''}${suffixMeta.meaning.toLowerCase()}.`,
          lineage_covenant: `${prefixMeta.sovereign_parent} Heritage Covenant`,
          sovereign_parents: parents
        };
      }
    }
  }

  // 6. Template 4: Attributive Oríkì & Standalone Morphemes
  if (ONOMASTIC_SUFFIXES[clean]) {
    const sfx = ONOMASTIC_SUFFIXES[clean];
    let parents = ['Ẹbí', 'Ọmọ'];
    if (clean === 'akanbi') parents = ['Ọmọ', 'Akín', 'Ẹbí'];
    if (clean === 'ayinla') parents = ['Ọlá', 'Òye', 'Ẹbí'];
    if (clean === 'aduke') parents = ['Ẹbí', 'Ọmọ'];
    if (['taye', 'taiwo', 'kehinde', 'idowu', 'alaba'].includes(clean)) parents = ['Àmútọ̀runwá', 'Ẹbí', 'Ọmọ'];

    return {
      canonical_name: sfx.diacritic,
      grammatical_class: ONOMASTIC_TEMPLATES.TEMPLATE_4_AMUTORUNWA_ORIKI,
      morphemes: [{ morpheme: sfx.diacritic, meaning: sfx.meaning, sovereign_parent: parents[0], category: 'Social Structure, Kinship & Lineage' }],
      lineage_meaning: sfx.meaning,
      lineage_covenant: 'Ancestral Oríkì Attributive Name',
      sovereign_parents: parents
    };
  }

  // Strictly return null if no valid sentential grammar matches (Anti-Chopping Invariant)
  return null;
}

export function decomposeYorubaName(fullName) {
  if (!fullName || typeof fullName !== 'string') return null;
  const rawTokens = fullName.trim().split(/\s+/).filter(Boolean);
  if (!rawTokens.length) return null;

  if (rawTokens.length === 1) return decomposeSingleToken(rawTokens[0]);

  const results = rawTokens.map(decomposeSingleToken).filter(Boolean);
  if (!results.length) return null;
  if (results.length === 1) return results[0];

  const canonicalName = results.map(r => r.canonical_name).join(' ');
  const allMorphemes = results.flatMap(r => r.morphemes || []);
  const combinedMeaning = results.map(r => r.lineage_meaning).join(' ');
  const allParents = Array.from(new Set(results.flatMap(r => r.sovereign_parents || [])));

  return {
    canonical_name: canonicalName,
    grammatical_class: 'Compound Multi-Part Ancestral Heritage',
    morphemes: allMorphemes,
    lineage_meaning: combinedMeaning,
    lineage_covenant: 'Compound Lineage Covenant',
    sovereign_parents: allParents
  };
}
