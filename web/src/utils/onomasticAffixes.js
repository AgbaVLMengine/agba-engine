/**
 * ÀGBÀ ENGINE: ONOMASTIC AFFIXES ("ORÚKỌ MI" DRAWER 1A)
 * Curated Theophoric Prefixes, Verbal Predicates & Suffix Dictionaries
 * Gate 2 Compliant: Strictly < 250 LOC.
 * Gate 9 Invariant: Zero restricted biographical terminology; ancestral reverence honored.
 */

export const GRAMMATICAL_CLASSES = {
  CLASS_A: 'Class A (Theophoric/Nominal Prefix + Verb)',
  CLASS_B: 'Class B (Possessive/Pronominal + Trailing Noun)',
  CLASS_C: 'Class C (Deverbal Nominalization & Sacred Birth Name)',
  CLASS_D: 'Class D (Contracted Ancestral Return)',
  CLASS_E: 'Class E (Proverbial Clause & Sentence Name)'
};

export const ONOMASTIC_TEMPLATES = {
  TEMPLATE_1_PRESTIGE_VERB: 'Template 1 (Prestige / Theophoric + Verb)',
  TEMPLATE_2_PRONOMINAL_CLAUSE: 'Template 2 (Pronominal Sentence Clause)',
  TEMPLATE_3_THEOCENTRIC_COVENANT: 'Template 3 (Nominalized Theocentric Covenant)',
  TEMPLATE_4_AMUTORUNWA_ORIKI: 'Template 4 (Sacred Circumstance & Attributive Oríkì)'
};

export const ONOMASTIC_PREFIXES = {
  oye: { diacritic: 'Òye', meaning: 'Deep discernment, philosophical wisdom & epistemic clarity', sovereign_parent: 'Òye', category: 'Oral Literature, Philosophy & Folklore' },
  ade: { diacritic: 'Adé', meaning: 'Royal crown, monarchical authority & sovereign destiny', sovereign_parent: 'Adé', category: 'Attire, Textiles & Personal Adornment' },
  ola: { diacritic: 'Ọlá', meaning: 'High nobility, aristocratic dignity & transgenerational prestige', sovereign_parent: 'Ọlá', category: 'Social Structure, Kinship & Lineage' },
  ogun: { diacritic: 'Ògún', meaning: 'Iron metallurgy, pioneering paths, blacksmithing & martial justice', sovereign_parent: 'Ògún', category: 'Spiritual & Cosmological Matrix' },
  osun: { diacritic: 'Ọ̀ṣun', meaning: 'Sacred waters, maternal fertility, prosperity & divine sweetness', sovereign_parent: 'Ọ̀ṣun', category: 'Spiritual & Cosmological Matrix' },
  sango: { diacritic: 'Ṣàngó', meaning: 'Solar thunder, cosmic justice & royal Aláàfin authority', sovereign_parent: 'Ṣàngó', category: 'Spiritual & Cosmological Matrix' },
  ifa: { diacritic: 'Ifá', meaning: 'Sacred matrix of divination, 256 Odù & cosmic destiny', sovereign_parent: 'Ifá', category: 'Spiritual & Cosmological Matrix' },
  fa: { diacritic: 'Ifá', meaning: 'Sacred oracle & wisdom matrix', sovereign_parent: 'Ifá', category: 'Spiritual & Cosmological Matrix' },
  akin: { diacritic: 'Akín', meaning: 'Heroic valor, military courage & champion warrior spirit', sovereign_parent: 'Akín', category: 'Military Traditions, Weaponry & Defense' },
  ayo: { diacritic: 'Ayọ̀', meaning: 'Auspicious joy, celestial celebration & communal triumph', sovereign_parent: 'Ayọ̀', category: 'Oral Literature, Philosophy & Folklore' },
  omo: { diacritic: 'Ọmọ', meaning: 'Sacred child, generational continuation & ancestral lineage vessel', sovereign_parent: 'Ọmọ', category: 'Social Structure, Kinship & Lineage' },
  baba: { diacritic: 'Bàbá', meaning: 'Ancestral patriarch, elder custodian & compound pillar', sovereign_parent: 'Bàbá', category: 'Social Structure, Kinship & Lineage' },
  iya: { diacritic: 'Ìyá', meaning: 'Sacred matriarch, mother & primordial wellspring of life', sovereign_parent: 'Ìyá', category: 'Social Structure, Kinship & Lineage' },
  olu: { diacritic: 'Olú', meaning: 'Paramount lord, sovereign chief & head of the assembly', sovereign_parent: 'Olú', category: 'Monarchy, Royal Regalia & Governance' },
  oro: { diacritic: 'Orò', meaning: 'Ancestral mysteries & the sacred bullroarer fraternity', sovereign_parent: 'Orò', category: 'Ancestral Masquerades & Funerary Rites' },
  odu: { diacritic: 'Odù', meaning: 'Primordial womb of divination & cosmic sign of destiny', sovereign_parent: 'Odù Ifá', category: 'Spiritual & Cosmological Matrix' },
  ebi: { diacritic: 'Ẹbí', meaning: 'Kinship network, bloodline hearth & communal family bond', sovereign_parent: 'Ẹbí', category: 'Social Structure, Kinship & Lineage' },
  ori: { diacritic: 'Orí', meaning: 'Inner spiritual head, personal destiny & divine consciousness', sovereign_parent: 'Orí', category: 'Spiritual & Cosmological Matrix' },
  owo: { diacritic: 'Owó', meaning: 'Honorable enterprise, trade prosperity & cowrie currency', sovereign_parent: 'Owó Ẹyọ', category: 'Economy, Trade & Cowrie Systems' },
  oba: { diacritic: 'Ọba', meaning: 'Sovereign monarch, kingly throne & divine ruler', sovereign_parent: 'Ọba', category: 'Monarchy, Royal Regalia & Governance' },
  ara: { diacritic: 'Ará', meaning: 'Kinship relation, citizen & kinsman', sovereign_parent: 'Ẹbí', category: 'Social Structure, Kinship & Lineage' },
  ilu: { diacritic: 'Ìlú', meaning: 'Ancient township, kingdom capital & civic community', sovereign_parent: 'Ìpínlẹ̀ Ọ̀yọ́', category: 'Civilization, History & Civic Heritage' },
  alade: { diacritic: 'Aládé', meaning: 'Bearer of the sacred royal crown', sovereign_parent: 'Adé', category: 'Attire, Textiles & Personal Adornment' },
  ibilade: { diacritic: 'Ìbílade', meaning: 'Lineage birthright into royal crown nobility', sovereign_parent: 'Adé', category: 'Attire, Textiles & Personal Adornment' },
  orisa: { diacritic: 'Òrìṣà', meaning: 'Consecrated celestial divinity & primordial avatar', sovereign_parent: 'Òrìṣà', category: 'Spiritual & Cosmological Matrix' }
};

export const MODAL_PARTICLES = {
  tun: { diacritic: 'tún', meaning: 'again, once more into renewed elevation' },
  ti: { diacritic: 'ti', meaning: 'already established in grace' },
  fi: { diacritic: 'fi', meaning: 'by means of, endowed with' }
};

export const THEOCENTRIC_COVENANTS = {
  ileri: { diacritic: 'Ìlérí', root_verb: 'lérí (promise)', gloss: 'Sacred divine covenant and solemn promise', parents: ['Olódùmarè', 'Ọ̀rọ̀', 'Òye'] },
  imisi: { diacritic: 'Ìmísí', root_verb: 'mí sí (breathe upon)', gloss: 'Divine breath, cosmic inspiration and sacred spirit', parents: ['Olódùmarè', 'Ẹ̀mí', 'Òye'] },
  ife: { diacritic: 'Ìfẹ́', root_verb: 'fẹ́ (love/will)', gloss: 'Supreme unconditional love and divine goodwill', parents: ['Olódùmarè', 'Ìfẹ́', 'Òye'] },
  ibukun: { diacritic: 'Ìbùkún', root_verb: 'bù kún (pour blessings on)', gloss: 'Measured blessings and abundance poured forth', parents: ['Olódùmarè', 'Ọlá', 'Òye'] },
  ireti: { diacritic: 'Ìrètí', root_verb: 'retí (await/expect)', gloss: 'Steadfast hope, enduring expectation and moral patience', parents: ['Olódùmarè', 'Òye'] }
};

export const PRONOMINAL_SENTENCES = {
  motunrayo: { diacritic: 'Mótúnrayọ̀', parents: ['Ayọ̀', 'Ẹbí'], meaning: 'I have beheld joy once again after an era of patience' },
  afolabi: { diacritic: 'Afọlábí', parents: ['Ọlá'], meaning: 'Born into and endowed with sovereign nobility' },
  morohunmbo: { diacritic: 'Moróhúnm̀bọ́', parents: ['Ẹbí', 'Ọ̀rọ̀', 'Òye'], meaning: 'I have found a precious ancestral treasure to bring home' },
  ayodele: { diacritic: 'Ayọ̀délé', parents: ['Ayọ̀', 'Ẹbí'], meaning: 'Joy has arrived home to complete the dynasty' },
  adebayo: { diacritic: 'Adébáyọ̀', parents: ['Adé', 'Ayọ̀', 'Ẹbí'], meaning: 'The crown meets with boundless celestial joy' },
  mosunmola: { diacritic: 'Mósúnmọ́lá', parents: ['Ọlá'], meaning: 'I move closer to embrace high aristocratic honor' }
};

export const ONOMASTIC_SUFFIXES = {
  yeku: { diacritic: 'Yẹ̀kú', meaning: 'Spared from death, transcending mortality through ancestral grace' },
  fua: { diacritic: 'Fúà', meaning: 'Radiates with serene, luminous, and stainless purity' },
  bunmi: { diacritic: 'Bùnmi', meaning: 'Bestowed upon me as a consecrated divine blessing' },
  kemi: { diacritic: 'Kẹ́mi', meaning: 'Pampers, nurtures, and wraps me in affectionate protection' },
  wumi: { diacritic: 'Wùmí', meaning: 'Deeply delights my inner spirit, endears itself to my heart' },
  bisi: { diacritic: 'Bísí', meaning: 'Has multiplied and brought transgenerational increase' },
  bimpe: { diacritic: 'Bím̀pé', meaning: 'Birthed me complete, flawless and unblemished' },
  nike: { diacritic: 'Níkẹ́', meaning: 'Possesses tender cherishing, maternal pampering and honor' },
  niyi: { diacritic: 'Níyì', meaning: 'Possesses enduring prestige, reverence and majesty' },
  laja: { diacritic: 'Lajà', meaning: 'Reconciles disputes, dispels discord and establishes peace' },
  lakun: { diacritic: 'Lakùn', meaning: 'Opens wide the ocean of endless royal abundance' },
  ribigbe: { diacritic: 'Ribigbé', meaning: 'Has found an exalted and worthy throne to inhabit' },
  kunle: { diacritic: 'Kúnlé', meaning: 'Fills the ancestral household with radiance, honor, and children' },
  wale: { diacritic: 'Wálé', meaning: 'Returned home to the lineage sanctuary and household hearth' },
  dele: { diacritic: 'Délé', meaning: 'Arrived home to bring peaceful completion to the dynasty' },
  yeju: { diacritic: 'Yẹjú', meaning: 'Befits the countenance, adorns the face with dignity' },
  tola: { diacritic: 'Tọ́lá', meaning: 'Worthy of royal honor, measured to match high aristocratic dignity' },
  koya: { diacritic: 'Kọ̀yà', meaning: 'Repudiates oppression, suffering, poverty, and societal injustice' },
  dapo: { diacritic: 'Dàpọ̀', meaning: 'Blended together in harmonious generational unity' },
  gbemi: { diacritic: 'Gbèmí', meaning: 'Favors, supports, vindicates, and sustains my earthly steps' },
  seun: { diacritic: 'Ṣeun', meaning: 'Rendered benevolent favor and divine lovingkindness' },
  dupe: { diacritic: 'Dúpẹ́', meaning: 'Renders unceasing grateful thanksgiving unto Olódùmarè' },
  tayo: { diacritic: 'Táyọ̀', meaning: 'Surpasses ordinary happiness into boundless spiritual jubilation' },
  bayo: { diacritic: 'Báyọ̀', meaning: 'Meets and blends seamlessly with celestial joy and jubilation' },
  femi: { diacritic: 'Fẹ́mi', meaning: 'Loves and cherishes me with steady, unconditional affection' },
  korede: { diacritic: 'Kórédé', meaning: 'Harvested and ushered in abundance, blessings, and good fortune' },
  segun: { diacritic: 'Ṣẹ́gun', meaning: 'Emerged victorious over life struggles and spiritual battles' },
  sola: { diacritic: 'Ṣọlá', meaning: 'Acts with aristocratic grace and bestows nobility upon the hearth' },
  bode: { diacritic: 'Bọ̀dé', meaning: 'Arrived through the sacred city gateway in majestic triumph' },
  kanmi: { diacritic: 'Kànmí', meaning: 'Has reached my turn, directly touched and elevated my soul' },
  sunkanmi: { diacritic: 'Súnkànmí', meaning: 'Moved closer to embrace me with favor and royal abundance' },
  jide: { diacritic: 'Jídé', meaning: 'Awakened from the spiritual realm to walk among the living' },
  wande: { diacritic: 'Wándé', meaning: 'Sought me out diligently across spiritual waters and found me' },
  folabi: { diacritic: 'Fọ́lábí', meaning: 'Birthed through the instrument of sovereign ancestral nobility' },
  tunji: { diacritic: 'Túnjí', meaning: 'Resurrected, reawakened into vibrant generational life' },
  rewaju: { diacritic: 'Rẹ́wájú', meaning: 'Advancing toward future breakthroughs and generational elevation' },
  nrewaju: { diacritic: 'Ńrẹ́wájú', meaning: 'Marching forward relentlessly into greater expansion and victory' },
  gunle: { diacritic: 'Gúnlẹ̀', meaning: 'Firmly rooted, docked safely ashore, permanently anchored in destiny' },
  diran: { diacritic: 'Dìran', meaning: 'Transformed into an unbroken hereditary transgenerational legacy' },
  dimeji: { diacritic: 'Dìméjì', meaning: 'Multiplied twofold in grace, abundance, and doubled blessings' },
  bose: { diacritic: 'Bọ́ṣẹ̀', meaning: 'Born on the consecrated day of worship and communal devotion' },
  bolaji: { diacritic: 'Bọ́lájí', meaning: 'Awakened side-by-side with ancestral honor and nobility' },
  bolanle: { diacritic: 'Bọ́lánlé', meaning: 'Met nobility waiting comfortably within the homestead' },
  lana: { diacritic: 'Lànà', meaning: 'Clears and pioneers a righteous path of destiny and elevation' },
  sanya: { diacritic: 'Ṣànyá', meaning: 'Compensates and vindicates the lineage for past tribulations' },
  yele: { diacritic: 'Yẹlé', meaning: 'Befits the royal homestead and confers honor upon the compound' },
  biyi: { diacritic: 'Bíyìí', meaning: 'Birthed this noble one into generational prestige and favor' },
  poju: { diacritic: 'Pọ̀jù', meaning: 'Abounds in great dignity and overflows with transgenerational blessing' },
  boyejo: { diacritic: 'Bọ́yèjọ', meaning: 'Harmonizes with chieftaincy dignity and adorns the family title' },
  odunayo: { diacritic: 'Ọdúnayọ̀', meaning: 'A festive year of joy, marking a season of generational triumph' },
  alabi: { diacritic: 'Àlàbí', meaning: 'Born into pure white cloth, enveloped in unstained honor' },
  adigun: { diacritic: 'Adígun', meaning: 'Warrior fully armed with ancestral protection and charms' },
  ajayi: { diacritic: 'Àjàyí', meaning: 'Born facing the earth, endowed with spiritual sight' },
  yetunde: { diacritic: 'Yétúndé', meaning: 'The revered ancestral mother has returned to the hearth' },
  babatunde: { diacritic: 'Bàbátúndé', meaning: 'The revered ancestral patriarch has reincarnated to guide the house' },
  yewande: { diacritic: 'Yéwándé', meaning: 'Mother sought and found me across the sacred rivers' },
  babajide: { diacritic: 'Bàbájídé', meaning: 'Ancestral patriarch has awakened from the spiritual realm' },
  iyabo: { diacritic: 'Ìyábọ̀', meaning: 'Mother has returned home in joyful reincarnation' },
  iyabode: { diacritic: 'Ìyábọ̀dé', meaning: 'Mother has arrived at the gateway of the living' },
  kofoworola: { diacritic: 'Kòfowórọlá', meaning: 'Did not purchase honor with money, nobility is innate' },
  morenikeji: { diacritic: 'Mọ́rẹ́nikéjì', meaning: 'I have found a true soul companion and complementary partner' },
  modupe: { diacritic: 'Mọdúpẹ́', meaning: 'I render grateful praise to Olódùmarè and the ancestors' },
  kosoko: { diacritic: 'Kòsọ́kọ́', meaning: 'There is no hoe remaining to dig a grave; this child lives' },
  akanke: { diacritic: 'Àkànkẹ́', meaning: 'Specially chosen from birth to be showered with tender care' },
  asake: { diacritic: 'Àṣàkẹ́', meaning: 'Selected for affectionate pampering and royal guidance' },
  ajoke: { diacritic: 'Àjọkẹ́', meaning: 'Cherished collectively in unity by the whole kindred' },
  abike: { diacritic: 'Àbíkẹ́', meaning: 'Born purposely to receive the honor and care of the family' },
  adisa: { diacritic: 'Àdìsá', meaning: 'One whose character, deeds, and oríkì are clearly articulated' },
  akanbi: { diacritic: 'Àkànbí', meaning: 'One specially conceived and brought forth by divine favor' },
  ayinla: { diacritic: 'Àyìnlá', meaning: 'One praised and celebrated from the moment of stepping forth' },
  aduke: { diacritic: 'Àdùkẹ́', meaning: 'One whom the entire lineage strives to pamper and cherish' },
  idowu: { diacritic: 'Ìdòwú', meaning: 'Child born directly after twins, carrier of calming equilibrium' },
  alaba: { diacritic: 'Àlàbá', meaning: 'Child born following Ìdòwú, the keeper of homestead peace' },
  taye: { diacritic: 'Táyéwò', meaning: 'First of the twin pair to taste the earth and test its sweetness' },
  taiwo: { diacritic: 'Táyéwò', meaning: 'First of the twin pair to taste the earth and test its sweetness' },
  kehinde: { diacritic: 'Kẹ́hìndé', meaning: 'The senior twin who sent the younger ahead, arriving with authority' },
  malomo: { diacritic: 'Málọmọ̀', meaning: 'Pleading with the sacred spirit child to abide permanently' },
  kokumo: { diacritic: 'Kòkúmọ́', meaning: 'Has conquered mortality, will never return to the grave' },
  durosinmi: { diacritic: 'Dúrósinmi', meaning: 'Tarry with me to comfort my later years and bury me in peace' }
};
