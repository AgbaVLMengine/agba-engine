/**
 * ÀGBÀ ENGINE: ONOMASTIC LINEAGE GATEWAY ("ORÚKỌ MI")
 * Decomposes Yorùbá names into constituent root morphemes, resolves tonal marks,
 * and links directly to canonical Sovereign Parent nodes in the 1,411 corpus.
 *
 * Implements Kábíyèsí's "Oyegunle" model: Òye (Epistemic Wisdom) + Gunlẹ̀ (Firmly Anchored).
 */

export const ONOMASTIC_PREFIXES = {
  oye: { diacritic: 'Òye', meaning: 'Deep discernment, philosophical wisdom & epistemic clarity', sovereign_parent: 'Òye', category: 'Oral Literature, Philosophy & Folklore' },
  ade: { diacritic: 'Adé', meaning: 'Royal crown, monarchical authority & sovereign destiny', sovereign_parent: 'Adé', category: 'Attire, Textiles & Personal Adornment' },
  ogun: { diacritic: 'Ògún', meaning: 'Iron metallurgy, pioneering paths, blacksmithing & martial justice', sovereign_parent: 'Ògún', category: 'Spiritual & Cosmological Matrix' },
  sango: { diacritic: 'Ṣàngó', meaning: 'Solar thunder, cosmic justice & royal Aláàfin authority', sovereign_parent: 'Ṣàngó', category: 'Spiritual & Cosmological Matrix' },
  osun: { diacritic: 'Ọ̀ṣun', meaning: 'Sacred waters, maternal fertility, prosperity & divine sweetness', sovereign_parent: 'Ọ̀ṣun', category: 'Spiritual & Cosmological Matrix' },
  ifa: { diacritic: 'Ifá', meaning: 'Sacred matrix of divination, 256 Odù & cosmic destiny', sovereign_parent: 'Ifá', category: 'Spiritual & Cosmological Matrix' },
  fa: { diacritic: 'Ifá', meaning: 'Sacred oracle & wisdom matrix', sovereign_parent: 'Ifá', category: 'Spiritual & Cosmological Matrix' },
  ola: { diacritic: 'Ọlá', meaning: 'High nobility, aristocratic dignity & transgenerational prestige', sovereign_parent: 'Ọlá', category: 'Social Structure, Kinship & Lineage' },
  akin: { diacritic: 'Akín', meaning: 'Heroic valor, military courage & champion warrior spirit', sovereign_parent: 'Akín', category: 'Military Traditions, Weaponry & Defense' },
  ayo: { diacritic: 'Ayọ̀', meaning: 'Auspicious joy, celestial celebration & communal triumph', sovereign_parent: 'Ayọ̀', category: 'Oral Literature, Philosophy & Folklore' },
  omo: { diacritic: 'Ọmọ', meaning: 'Sacred child, generational continuation & ancestral lineage vessel', sovereign_parent: 'Ọmọ', category: 'Social Structure, Kinship & Lineage' },
  baba: { diacritic: 'Bàbá', meaning: 'Ancestral patriarch, protective fatherhood & custodial pillar', sovereign_parent: 'Bàbá', category: 'Social Structure, Kinship & Lineage' },
  iya: { diacritic: 'Ìyá', meaning: 'Sacred matriarch, mother & primordial wellspring of life', sovereign_parent: 'Ìyá', category: 'Social Structure, Kinship & Lineage' },
  olu: { diacritic: 'Olú', meaning: 'Paramount lord, sovereign chief & head of the assembly', sovereign_parent: 'Olú', category: 'Monarchy, Royal Regalia & Governance' },
  oro: { diacritic: 'Orò', meaning: 'Ancestral mysteries & the sacred bullroarer fraternity', sovereign_parent: 'Orò', category: 'Ancestral Masquerades & Funerary Rites' },
  odu: { diacritic: 'Odù', meaning: 'Primordial womb of divination & cosmic sign of destiny', sovereign_parent: 'Odù Ifá', category: 'Spiritual & Cosmological Matrix' },
  ebi: { diacritic: 'Ẹbí', meaning: 'Kinship network, bloodline hearth & communal family bond', sovereign_parent: 'Ẹbí', category: 'Social Structure, Kinship & Lineage' }
};

export const ONOMASTIC_SUFFIXES = {
  gunle: { diacritic: 'Gúnlẹ̀', meaning: 'Firmly rooted, docked safely ashore, permanently anchored' },
  nrewaju: { diacritic: 'Ńrẹ́wájú', meaning: 'Marching forward relentlessly into greater nobility and expansion' },
  rewaju: { diacritic: 'Rẹ́wájú', meaning: 'Advancing toward future breakthroughs and generational elevation' },
  wale: { diacritic: 'Wálé', meaning: 'Returned home to ancestral sanctuary and lineage honor' },
  dele: { diacritic: 'Délé', meaning: 'Arrived home to bring completion and peace to the hearth' },
  wumi: { diacritic: 'Wùmí', meaning: 'Deeply delights my soul, endears itself to my inner spirit' },
  gbemi: { diacritic: 'Gbèmí', meaning: 'Favors, vindicates, and sustains my earthly path' },
  korede: { diacritic: 'Kórédé', meaning: 'Harvested and ushered in blessings, fortune, and prosperity' },
  leke: { diacritic: 'Lékè', meaning: 'Triumphs on high, transcending every earthly trial and obstacle' },
  tayo: { diacritic: 'Táyọ̀', meaning: 'Surpasses ordinary joy into boundless spiritual celebration' },
  segun: { diacritic: 'Ṣẹ́gun', meaning: 'Emerged victorious over adversity, conquest of life challenges' },
  koya: { diacritic: 'Kọ̀yà', meaning: 'Repudiates oppression, suffering, and societal injustice' },
  diran: { diacritic: 'Dìran', meaning: 'Transformed into an unbroken hereditary transgenerational legacy' },
  yemi: { diacritic: 'Yẹmí', meaning: 'Befits my destiny, perfectly adorns my character and name' },
  lola: { diacritic: 'Lọ́lá', meaning: 'Endowed with honor, wrapped in royal and familial nobility' },
  dimeji: { diacritic: 'Dìméjì', meaning: 'Multiplied twofold in grace, abundance, and double blessings' },
  bose: { diacritic: 'Bọ́ṣẹ̀', meaning: 'Born on the sacred day of worship and communal dedication' },
  femi: { diacritic: 'Fẹ́mi', meaning: 'Loves and cherishes me with unwavering devotion' }
};

// Curated Canonical Lineages (Instant Exact Synthesis)
export const CANONICAL_ONOMASTIC_REGISTRY = {
  oyegunle: {
    canonical_name: 'Òyégúnlẹ̀',
    morphemes: [
      { morpheme: 'Òye', meaning: 'Deep epistemic discernment, philosophical wisdom & ancestral intellect', sovereign_parent: 'Òye', category: 'Oral Literature, Philosophy & Folklore' },
      { morpheme: 'Gunlẹ̀', meaning: 'Firmly rooted, docked ashore, permanently anchored in destiny', sovereign_parent: null }
    ],
    lineage_meaning: 'One whose lineage is firmly anchored in deep ancestral discernment and epistemic wisdom.',
    lineage_covenant: 'Sovereign Sages & Custodians of Epistemic Discernment',
    sovereign_parents: ['Òye', 'Ọba']
  },
  yetunde: {
    canonical_name: 'Yétúndé',
    morphemes: [
      { morpheme: 'Yèyé (Ìyá)', meaning: 'Revered Mother & Matriarchal Ancestor', sovereign_parent: 'Ìyá', category: 'Social Structure, Kinship & Lineage' },
      { morpheme: 'Túndé', meaning: 'Has returned again in ancestral reincarnation', sovereign_parent: 'Ẹbí' }
    ],
    lineage_meaning: 'The revered ancestral mother has returned to bless the family lineage.',
    lineage_covenant: 'Matriarchal Continuity & Ancestral Return',
    sovereign_parents: ['Ìyá', 'Ẹbí']
  },
  olanrewaju: {
    canonical_name: 'Ọlànrewájú',
    morphemes: [
      { morpheme: 'Ọlá', meaning: 'High nobility, aristocratic dignity & transgenerational prestige', sovereign_parent: 'Ọlá', category: 'Social Structure, Kinship & Lineage' },
      { morpheme: 'Ńrẹ́wájú', meaning: 'Marching forward relentlessly into greater expansion', sovereign_parent: null }
    ],
    lineage_meaning: 'Nobility and high honor are advancing continuously into the future.',
    lineage_covenant: 'Noble Vanguard & Dynastic Trailblazers',
    sovereign_parents: ['Ọlá', 'Ọba']
  },
  kabiru: {
    canonical_name: 'Kábírù',
    morphemes: [
      { morpheme: 'Kábírù', meaning: 'The Great, The Magnified (Naturalized classical designation of sovereign majesty)', sovereign_parent: 'Aláàfin', category: 'Monarchy, Royal Regalia & Governance' }
    ],
    lineage_meaning: 'One endowed with majestic grandeur, enduring strength, and expansive greatness.',
    lineage_covenant: 'Imperial Greatness & Sovereign Authority',
    sovereign_parents: ['Aláàfin', 'Ọba']
  },
  adewale: {
    canonical_name: 'Adéwálé',
    morphemes: [
      { morpheme: 'Adé', meaning: 'Royal crown, beaded regalia & monarchical authority', sovereign_parent: 'Adé', category: 'Attire, Textiles & Personal Adornment' },
      { morpheme: 'Wálé', meaning: 'Has arrived home to the ancestral household', sovereign_parent: null }
    ],
    lineage_meaning: 'The royal crown has returned to inhabit the home.',
    lineage_covenant: 'Crown Bearers & Dynastic Heirs',
    sovereign_parents: ['Adé', 'Ọba']
  },
  ogundele: {
    canonical_name: 'Ògúndélé',
    morphemes: [
      { morpheme: 'Ògún', meaning: 'Primordial divinity of iron, metallurgy, and justice', sovereign_parent: 'Ògún', category: 'Spiritual & Cosmological Matrix' },
      { morpheme: 'Délé', meaning: 'Has arrived at the homestead in victory', sovereign_parent: null }
    ],
    lineage_meaning: 'Ògún (the master of iron and path-clearing) has arrived at the homestead.',
    lineage_covenant: 'Metallurgical Guild, Blacksmith Hearths & Martial Champions',
    sovereign_parents: ['Ògún', 'Àdá']
  },
  akinwumi: {
    canonical_name: 'Akínwùmí',
    morphemes: [
      { morpheme: 'Akín', meaning: 'Heroic valor, champion warrior courage & endurance', sovereign_parent: 'Akín', category: 'Military Traditions, Weaponry & Defense' },
      { morpheme: 'Wùmí', meaning: 'Delights my soul and earns deep reverence', sovereign_parent: null }
    ],
    lineage_meaning: 'Heroic courage and valor delight my spirit.',
    lineage_covenant: 'Valorous Defenders & Strategic Champions',
    sovereign_parents: ['Akín', 'Idà']
  },
  babalola: {
    canonical_name: 'Bàbálọ́lá',
    morphemes: [
      { morpheme: 'Bàbá', meaning: 'Father, protective patriarch & ancestral pillar', sovereign_parent: 'Bàbá', category: 'Social Structure, Kinship & Lineage' },
      { morpheme: 'Lọ́lá', meaning: 'Is the embodiment of nobility and honor', sovereign_parent: 'Ọlá' }
    ],
    lineage_meaning: 'The father is the very foundation of honor and nobility.',
    lineage_covenant: 'Patriarchal Keepers of Lineage Prestige',
    sovereign_parents: ['Bàbá', 'Ọlá']
  },
  adediran: {
    canonical_name: 'Adédìran',
    morphemes: [
      { morpheme: 'Adé', meaning: 'Sacred crown & royal destiny', sovereign_parent: 'Adé', category: 'Attire, Textiles & Personal Adornment' },
      { morpheme: 'Dìran', meaning: 'Has become an unbroken generational heritage', sovereign_parent: null }
    ],
    lineage_meaning: 'The crown has become an unbroken, transgenerational dynasty.',
    lineage_covenant: 'Imperial Hereditary Dynasties',
    sovereign_parents: ['Adé', 'Ọba']
  }
};

function decomposeSingleToken(token) {
  const clean = token
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z]/g, '');
  if (clean.length < 3 || ['mrs', 'mr', 'miss', 'chief', 'dr', 'prof'].includes(clean)) return null;

  // 1. Direct registry lookup
  if (CANONICAL_ONOMASTIC_REGISTRY[clean]) {
    return CANONICAL_ONOMASTIC_REGISTRY[clean];
  }

  // 2. Algorithmic prefix + suffix segmentation
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
            morphemes: [
              { morpheme: prefixMeta.diacritic, meaning: prefixMeta.meaning, sovereign_parent: prefixMeta.sovereign_parent, category: prefixMeta.category },
              { morpheme: suffixMeta.diacritic, meaning: suffixMeta.meaning, sovereign_parent: null }
            ],
            lineage_meaning: `${prefixMeta.diacritic} (${prefixMeta.meaning.split(',')[0]}) combines with ${suffixMeta.diacritic.toLowerCase()} (${suffixMeta.meaning.toLowerCase()}).`,
            lineage_covenant: `${prefixMeta.sovereign_parent} Lineage Covenant`,
            sovereign_parents: [prefixMeta.sovereign_parent].filter(Boolean)
          };
        }
      }

      if (remainder.length > 0) {
        return {
          canonical_name: `${prefixMeta.diacritic}${remainder}`,
          morphemes: [
            { morpheme: prefixMeta.diacritic, meaning: prefixMeta.meaning, sovereign_parent: prefixMeta.sovereign_parent, category: prefixMeta.category },
            { morpheme: remainder, meaning: 'Lineage morphological extension', sovereign_parent: null }
          ],
          lineage_meaning: `Lineage anchored in ${prefixMeta.diacritic} (${prefixMeta.meaning}).`,
          lineage_covenant: `${prefixMeta.sovereign_parent} Heritage`,
          sovereign_parents: [prefixMeta.sovereign_parent].filter(Boolean)
        };
      }
    }
  }

  return null;
}

/**
 * Decomposes any Yorùbá name, surname, or full name phrase into morphemes,
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
    morphemes: resolved.flatMap((r) => r.morphemes),
    lineage_meaning: resolved.map((r) => `${r.canonical_name}: ${r.lineage_meaning}`).join(' • '),
    lineage_covenant: resolved.map((r) => r.lineage_covenant).join(' & '),
    sovereign_parents: Array.from(new Set(resolved.flatMap((r) => r.sovereign_parents)))
  };
}
