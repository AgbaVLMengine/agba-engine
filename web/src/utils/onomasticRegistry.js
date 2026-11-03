/**
 * ÀGBÀ ENGINE: ONOMASTIC REGISTRY ("ORÚKỌ MI" DRAWER 1B)
 * Curated Canonical Registry, Deverbal Names & Sacred Birth Circumstances (Àmútọ̀runwá)
 * Gate 2 Compliant: Strictly < 200 LOC.
 * Gate 9 Invariant: Zero restricted biographical terminology; ancestral reverence honored.
 */

import { GRAMMATICAL_CLASSES } from './onomasticAffixes.js';

// Sacred Birth Circumstance Names & Oríkì (Orúkọ Àmútọ̀runwá)
export const AMUTORUNWA_NAMES = {
  ajayi: { canonical_name: 'Àjàyí', circumstance: 'Born face downwards, endowed with natural intuitive sight and spiritual shielding', sovereign_parent: 'Ẹbí' },
  adigun: { canonical_name: 'Adígun', circumstance: 'Warrior born girded with spiritual protection, armor, and battle readiness', sovereign_parent: 'Akín' },
  aina: { canonical_name: 'Àìná', circumstance: 'Child born with the umbilical cord wrapped naturally around the neck or body', sovereign_parent: 'Ẹbí' },
  idowu: { canonical_name: 'Ìdòwú', circumstance: 'Born directly after twins, the consecrated harbinger of equilibrium and household peace', sovereign_parent: 'Ibejì' },
  alaba: { canonical_name: 'Àlàbá', circumstance: 'Born immediately following Ìdòwú, keeper of calm and tranquility in the family compound', sovereign_parent: 'Ibejì' },
  taiwo: { canonical_name: 'Táyéwò', circumstance: 'The vanguard twin who stepped forward first to taste the earth and test its flavor', sovereign_parent: 'Ibejì' },
  kehinde: { canonical_name: 'Kẹ́hìndé', circumstance: 'The rightful senior twin who arrived last, commanding the younger from the womb', sovereign_parent: 'Ibejì' },
  amusan: { canonical_name: 'Àmùṣàn', circumstance: 'Born holding a sacred caul or ancestral masquerade branch, consecrated to Egúngún', sovereign_parent: 'Egúngún' },
  alabi: { canonical_name: 'Àlàbí', circumstance: 'Born enveloped in the white cloth of purity, sheltered by the mantle of Ọbàtálá', sovereign_parent: 'Ọlá' },
  akanbi: { canonical_name: 'Àkànbí', circumstance: 'Conceived and brought forth by special ancestral decree and divine favor', sovereign_parent: 'Ọmọ' },
  ayinde: { canonical_name: 'Àyìndé', circumstance: 'Praised, hailed, and saluted from the first breath onto the soil', sovereign_parent: 'Ọ̀rọ̀' },
  ajoke: { canonical_name: 'Àjọkẹ́', circumstance: 'Cherished collectively in deep communal affection by the entire kindred', sovereign_parent: 'Ẹbí' },
  abike: { canonical_name: 'Àbíkẹ́', circumstance: 'Born purposely to receive affectionate care and honor from the household', sovereign_parent: 'Ẹbí' },
  asake: { canonical_name: 'Àṣàkẹ́', circumstance: 'Singled out and distinguished for tender pampering and royal guidance', sovereign_parent: 'Ọlá' },
  adisa: { canonical_name: 'Àdìsá', circumstance: 'One whose character, lineage praise poetry, and deeds are clearly articulated', sovereign_parent: 'Ọ̀rọ̀' },
  malomo: { canonical_name: 'Málọmọ̀', circumstance: 'Abíkú pleading name beseeching the spiritual wanderer to anchor permanently in life', sovereign_parent: 'Ẹbí' },
  kokumo: { canonical_name: 'Kòkúmọ́', circumstance: 'Abíkú triumphant declaration that the bond of mortality is severed; the child lives', sovereign_parent: 'Ẹbí' },
  durosinmi: { canonical_name: 'Dúrósinmi', circumstance: 'Tarry with me to comfort my later years and escort me home in peace', sovereign_parent: 'Ẹbí' }
};

// Curated Canonical Registry Covering all 5 Grammatical Classes
export const CANONICAL_ONOMASTIC_REGISTRY = {
  // CLASS A: Theophoric/Nominal Prefix + Verb
  oyegunle: {
    canonical_name: 'Òyégúnlẹ̀', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Òye', meaning: 'Deep epistemic discernment & philosophical wisdom', sovereign_parent: 'Òye' }, { morpheme: 'Gúnlẹ̀', meaning: 'Firmly rooted, docked safely ashore', sovereign_parent: null }],
    lineage_meaning: 'One whose lineage is firmly anchored in deep ancestral discernment and epistemic wisdom.',
    lineage_covenant: 'Sovereign Sages & Custodians of Epistemic Discernment', sovereign_parents: ['Òye', 'Ọba']
  },
  olanrewaju: {
    canonical_name: 'Ọlànrewájú', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Ọlá', meaning: 'High nobility, aristocratic dignity & prestige', sovereign_parent: 'Ọlá' }, { morpheme: 'Ńrẹ́wájú', meaning: 'Marching forward relentlessly into expansion', sovereign_parent: null }],
    lineage_meaning: 'Nobility and high honor are advancing continuously into the future.',
    lineage_covenant: 'Noble Vanguard & Dynastic Trailblazers', sovereign_parents: ['Ọlá', 'Ọba']
  },
  oyekanmi: {
    canonical_name: 'Oyèkànmí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Oyè', meaning: 'Chieftaincy title, royal office & authority', sovereign_parent: 'Òye' }, { morpheme: 'Kànmí', meaning: 'Has reached my turn, directly elevated my life', sovereign_parent: null }],
    lineage_meaning: 'The ancestral title and mantle of governance have touched my generational turn.',
    lineage_covenant: 'Noble Titleholders & Regal Dignitaries', sovereign_parents: ['Òye', 'Ọba']
  },
  olasunkanmi: {
    canonical_name: 'Ọlásúnkànmí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Ọlá', meaning: 'High nobility & aristocratic prestige', sovereign_parent: 'Ọlá' }, { morpheme: 'Súnkànmí', meaning: 'Moved closer to embrace me with royal favor', sovereign_parent: null }],
    lineage_meaning: 'Nobility and aristocratic honor have drawn near to embrace my life.',
    lineage_covenant: 'Dynastic Heirs of Nobility', sovereign_parents: ['Ọlá', 'Ọba']
  },
  adewale: {
    canonical_name: 'Adéwálé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Adé', meaning: 'Royal crown, beaded regalia & monarchical authority', sovereign_parent: 'Adé' }, { morpheme: 'Wálé', meaning: 'Has arrived home to the ancestral household', sovereign_parent: null }],
    lineage_meaning: 'The royal crown has returned to inhabit the ancestral home.',
    lineage_covenant: 'Crown Bearers & Dynastic Heirs', sovereign_parents: ['Adé', 'Ọba']
  },
  folakemi: {
    canonical_name: 'Fọlákẹ́mi', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Fi-ọlá', meaning: 'With high nobility and regal dignity', sovereign_parent: 'Ọlá' }, { morpheme: 'Kẹ́mi', meaning: 'Pamper, cherish, and nurture me', sovereign_parent: null }],
    lineage_meaning: 'Cherish, protect, and nurture me with sovereign honor and noble prestige.',
    lineage_covenant: 'Dynastic Heirs of Nobility', sovereign_parents: ['Ọlá', 'Ẹbí']
  },
  odegbami: {
    canonical_name: 'Ọdẹgbàmí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Ọdẹ', meaning: 'Sacred hunter guild & forest scout fraternity', sovereign_parent: 'Ọdẹ' }, { morpheme: 'Gbàmí', meaning: 'Rescues, sustains, and vindicates my earthly steps', sovereign_parent: 'Ògún' }],
    lineage_meaning: 'The sacred hunter guild sustains, delivers, and protects my life.',
    lineage_covenant: 'Hunter Guilds & Forest Protectors', sovereign_parents: ['Ọdẹ', 'Ògún']
  },
  kayode: {
    canonical_name: 'Káyọ̀dé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'Kó-ayọ̀', meaning: 'Gathers and brings auspicious joy', sovereign_parent: 'Ayọ̀' }, { morpheme: 'Dé', meaning: 'Arrived home to the family hearth', sovereign_parent: 'Ẹbí' }],
    lineage_meaning: 'Brings celestial joy and auspicious triumph home to the lineage hearth.',
    lineage_covenant: 'Bearers of Joy & Communal Celebration', sovereign_parents: ['Ayọ̀', 'Ẹbí']
  },
  arosanyi: {
    canonical_name: 'Àròsanyìn', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'A-ro', meaning: 'Dedicated to and standing steadfast with', sovereign_parent: null }, { morpheme: 'Ọ̀sanyìn', meaning: 'Sacred deity of herbal healing and forest leaves', sovereign_parent: 'Ọ̀sanyìn' }],
    lineage_meaning: 'Dedicated to the healing ministry and spiritual wisdom of Ọ̀sanyìn, deity of flora.',
    lineage_covenant: 'Herbal Healers & Keepers of Sacred Botany', sovereign_parents: ['Ọ̀sanyìn']
  },
  afolabi: {
    canonical_name: 'Àfọlábí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_A,
    morphemes: [{ morpheme: 'A-fi-ọlá', meaning: 'Brought forth into the world with sovereign honor', sovereign_parent: 'Ọlá' }, { morpheme: 'Bí', meaning: 'Born into generational existence', sovereign_parent: 'Ọmọ' }],
    lineage_meaning: 'Born into sovereign honor, high nobility, and regal dignity.',
    lineage_covenant: 'Dynastic Heirs of Nobility', sovereign_parents: ['Ọlá', 'Ọba']
  },

  // CLASS B: Possessive/Pronominal Prefix + Trailing Noun
  temilade: {
    canonical_name: 'Tèmiládé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_B,
    morphemes: [{ morpheme: 'Tèmi', meaning: 'Belongs to me, is my rightful portion', sovereign_parent: 'Ẹbí' }, { morpheme: 'ni', meaning: 'Is / affirms identity', sovereign_parent: null }, { morpheme: 'Adé', meaning: 'The sacred crown & sovereign destiny', sovereign_parent: 'Adé' }],
    lineage_meaning: 'The sacred royal crown is my rightful inheritance.',
    lineage_covenant: 'Crown Legatees & Dynastic Claimants', sovereign_parents: ['Adé', 'Ọba']
  },
  temilola: {
    canonical_name: 'Tèmilọ́lá', grammatical_class: GRAMMATICAL_CLASSES.CLASS_B,
    morphemes: [{ morpheme: 'Tèmi', meaning: 'Belongs to me, is my portion', sovereign_parent: 'Ẹbí' }, { morpheme: 'ni', meaning: 'Is / affirms possession', sovereign_parent: null }, { morpheme: 'Ọlá', meaning: 'Nobility & transgenerational honor', sovereign_parent: 'Ọlá' }],
    lineage_meaning: 'Nobility and high honor are my rightful portion.',
    lineage_covenant: 'Lineage Custodians of Inherent Dignity', sovereign_parents: ['Ọlá', 'Ẹbí']
  },
  temitope: {
    canonical_name: 'Tèmítọ́pẹ́', grammatical_class: GRAMMATICAL_CLASSES.CLASS_B,
    morphemes: [{ morpheme: 'Tèmi', meaning: 'My earthly portion & life testimony', sovereign_parent: 'Ẹbí' }, { morpheme: 'tọ́', meaning: 'Is worthy, measured to deserve', sovereign_parent: null }, { morpheme: 'Ọpẹ́', meaning: 'Continuous gratitude to Olódùmarè', sovereign_parent: 'Ọ̀rọ̀' }],
    lineage_meaning: 'My life’s portion and experience are worthy of boundless thanksgiving.',
    lineage_covenant: 'Devotional Harvesters of Gratitude', sovereign_parents: ['Ọ̀rọ̀', 'Ẹbí']
  },
  tiwalade: {
    canonical_name: 'Tíwaládé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_B,
    morphemes: [{ morpheme: 'Tíwa', meaning: 'Belongs to all of us collectively in unity', sovereign_parent: 'Ẹbí' }, { morpheme: 'ni', meaning: 'Is / confirms ownership', sovereign_parent: null }, { morpheme: 'Adé', meaning: 'The crown of kingship & sovereign destiny', sovereign_parent: 'Adé' }],
    lineage_meaning: 'The crown of leadership belongs collectively to our entire lineage.',
    lineage_covenant: 'Communal Custodians of the Crown', sovereign_parents: ['Adé', 'Ọba']
  },

  // CLASS C: Deverbal Nominalizations & Sacred Birth Names (Orúkọ Àmútọ̀runwá)
  ibukun: {
    canonical_name: 'Ìbùkún', grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
    morphemes: [{ morpheme: 'Ì- (Nominalizer)', meaning: 'Prefix transforming verb into an abstract virtue', sovereign_parent: 'Òye' }, { morpheme: 'Bùkún', meaning: 'To slice and add upon into overflow', sovereign_parent: 'Ọlá' }],
    lineage_meaning: 'Divine addition, consecrated blessing, and multiplicative overflow.',
    lineage_covenant: 'Sanctuary of Celestial Favor', sovereign_parents: ['Ọlá', 'Òye']
  },
  ajayi: {
    canonical_name: 'Àjàyí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
    morphemes: [{ morpheme: 'Àjàyí', meaning: 'Sacred birth name (Orúkọ Àmútọ̀runwá): born face downwards with intuitive sight', sovereign_parent: 'Ẹbí' }],
    lineage_meaning: 'Primordial child endowed with natural spiritual shielding and intuitive sight.',
    lineage_covenant: 'Sacred Harbingers of Intuitive Sight', sovereign_parents: ['Ẹbí', 'Orí']
  },
  adigun: {
    canonical_name: 'Adígun', grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
    morphemes: [{ morpheme: 'A- (Agentive)', meaning: 'One who embodies a defined heroic action', sovereign_parent: 'Akín' }, { morpheme: 'Dígun', meaning: 'Packs weapons and spiritual defenses for battle', sovereign_parent: 'Ògún' }],
    lineage_meaning: 'One who girds himself with armor and spiritual defense for the defense of the clan.',
    lineage_covenant: 'Martial Champions & Clan Shield-Bearers', sovereign_parents: ['Akín', 'Ògún']
  },
  alabi: {
    canonical_name: 'Àlàbí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
    morphemes: [{ morpheme: 'Àlà', meaning: 'Pure white cloth, unstained integrity of Ọbàtálá', sovereign_parent: 'Ọbàtálá' }, { morpheme: 'Bí', meaning: 'Brought forth into birth and reality', sovereign_parent: 'Ọmọ' }],
    lineage_meaning: 'One born into pure unstained integrity, sheltered by the white mantle of Ọbàtálá.',
    lineage_covenant: 'Keepers of Stainless Purity & Calm', sovereign_parents: ['Ọlá', 'Ọbàtálá']
  },
  arowolo: {
    canonical_name: 'Arówólò', grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
    morphemes: [{ morpheme: 'A-rí-owó', meaning: 'One who finds cowrie prosperity and wealth', sovereign_parent: 'Owó Ẹyọ' }, { morpheme: 'Lò', meaning: 'To expend with honor and enterprise', sovereign_parent: null }],
    lineage_meaning: 'One who finds ample wealth and commercial prosperity to expend with honor.',
    lineage_covenant: 'Merchant Guilds & Commercial Legatees', sovereign_parents: ['Owó Ẹyọ', 'Ọlá']
  },
  alakija: {
    canonical_name: 'Alákìíjà', grammatical_class: GRAMMATICAL_CLASSES.CLASS_C,
    morphemes: [{ morpheme: 'Alákìíjà', meaning: 'Lineage title of heroic warriors and brave covenant keepers', sovereign_parent: 'Akín' }],
    lineage_meaning: 'Lineage of valiant champion warriors and defenders of the throne.',
    lineage_covenant: 'Martial Champions & Heroic Lineages', sovereign_parents: ['Akín', 'Ọba']
  },

  // CLASS D: Contracted Ancestral Return (Àtúnwá)
  yetunde: {
    canonical_name: 'Yétúndé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_D,
    morphemes: [{ morpheme: 'Yèyé (Ìyá)', meaning: 'Revered ancestral mother & matriarchal pillar', sovereign_parent: 'Ìyá' }, { morpheme: 'Túndé', meaning: 'Has returned in ancestral reincarnation', sovereign_parent: 'Ẹbí' }],
    lineage_meaning: 'The revered ancestral mother has returned to bless and protect the family hearth.',
    lineage_covenant: 'Matriarchal Continuity & Ancestral Rebirth', sovereign_parents: ['Ìyá', 'Ẹbí']
  },
  babatunde: {
    canonical_name: 'Bàbátúndé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_D,
    morphemes: [{ morpheme: 'Bàbá', meaning: 'Ancestral patriarch, elder custodian & compound pillar', sovereign_parent: 'Bàbá' }, { morpheme: 'Túndé', meaning: 'Has returned in living ancestral reincarnation', sovereign_parent: 'Ẹbí' }],
    lineage_meaning: 'The revered ancestral patriarch has returned to guide the lineage forward.',
    lineage_covenant: 'Patriarchal Rebirth & Custodial Wisdom', sovereign_parents: ['Bàbá', 'Ẹbí']
  },
  yewande: {
    canonical_name: 'Yéwándé', grammatical_class: GRAMMATICAL_CLASSES.CLASS_D,
    morphemes: [{ morpheme: 'Yèyé', meaning: 'Revered mother & ancestral matriarch', sovereign_parent: 'Ìyá' }, { morpheme: 'Wá-mí-dé', meaning: 'Sought after me diligently and arrived home', sovereign_parent: 'Ẹbí' }],
    lineage_meaning: 'The ancestral mother searched for me across the waters and arrived safely.',
    lineage_covenant: 'Matriarchal Seekers & Hearth Protectors', sovereign_parents: ['Ìyá', 'Ẹbí']
  },

  // CLASS E: Proverbial Clauses & Sentence Names
  kofoworola: {
    canonical_name: 'Kòfowórọ́lá', grammatical_class: GRAMMATICAL_CLASSES.CLASS_E,
    morphemes: [{ morpheme: 'Kò', meaning: 'Negative particle: Did not, does not', sovereign_parent: null }, { morpheme: "Fi-owó", meaning: 'Use commercial currency or wealth', sovereign_parent: 'Owó Ẹyọ' }, { morpheme: "Ra-ọlá", meaning: 'Purchase high nobility', sovereign_parent: 'Ọlá' }],
    lineage_meaning: 'Did not purchase high honor with money; nobility is an innate transgenerational inheritance.',
    lineage_covenant: 'Sovereign Aristocrats of Inherent Worth', sovereign_parents: ['Ọlá', 'Owó Ẹyọ']
  },
  koforowola: {
    canonical_name: 'Kòfowórọ́lá', grammatical_class: GRAMMATICAL_CLASSES.CLASS_E,
    morphemes: [{ morpheme: 'Kò', meaning: 'Negative particle: Did not, does not', sovereign_parent: null }, { morpheme: "Fi-owó", meaning: 'Use commercial currency or wealth', sovereign_parent: 'Owó Ẹyọ' }, { morpheme: "Ra-ọlá", meaning: 'Purchase high nobility', sovereign_parent: 'Ọlá' }],
    lineage_meaning: 'Did not purchase high honor with money; nobility is an innate transgenerational inheritance.',
    lineage_covenant: 'Sovereign Aristocrats of Inherent Worth', sovereign_parents: ['Owó Ẹyọ', 'Ọlá', 'Ọ̀rọ̀']
  },
  abayomi: {
    canonical_name: 'Àbáyọmí', grammatical_class: GRAMMATICAL_CLASSES.CLASS_E,
    morphemes: [{ morpheme: 'Ọ̀tá-ìbá-yọ̀-mí', meaning: 'The adversary would have gloated over me, but divine wisdom prevailed', sovereign_parent: 'Òye' }],
    lineage_meaning: 'The adversaries would have rejoiced over my defeat, but divine wisdom shielded and vindicated me.',
    lineage_covenant: 'Sovereign Sages of Divine Vindication', sovereign_parents: ['Òye', 'Ọ̀rọ̀', 'Ẹbí']
  },
  fowowe: {
    canonical_name: 'Fowowe', grammatical_class: GRAMMATICAL_CLASSES.CLASS_E,
    morphemes: [{ morpheme: 'Fi-owó', meaning: 'With wealth and cowrie prosperity', sovereign_parent: 'Owó Ẹyọ' }, { morpheme: 'Wẹ̀', meaning: 'Bathes, immersed in abundance', sovereign_parent: null }],
    lineage_meaning: 'One who is immersed and bathes in wealth, blessed with commercial abundance.',
    lineage_covenant: 'Merchant Dynasties & Mercantile Prosperers', sovereign_parents: ['Owó Ẹyọ', 'Ọlá']
  },
  morenikeji: {
    canonical_name: 'Mọ́rẹ́nikéjì', grammatical_class: GRAMMATICAL_CLASSES.CLASS_E,
    morphemes: [{ morpheme: 'Mo-rí', meaning: 'I have found and witnessed with my eyes', sovereign_parent: null }, { morpheme: 'Ẹni-ìkejì', meaning: 'A true soul companion and second self', sovereign_parent: 'Ẹbí' }],
    lineage_meaning: 'I have found a true partner and second self to walk through the journey of life.',
    lineage_covenant: 'Keepers of Sacred Companionship & Kinship', sovereign_parents: ['Ẹbí', 'Ọ̀rọ̀']
  }
};
