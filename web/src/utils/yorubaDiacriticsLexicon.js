import masterCorpus from '../data/yoruba_master_corpus.json';

// Multi-Word Phrases for Greedy Match (Àkànlò Èdè & Cosmological Formulae)
export const RAW_MULTI_WORD_PHRASES = [
  ['to n jo', 'tó ń jó'], ['lo n fun', 'ló ń fún'], ['ayo lo n fun', 'ayọ̀ ló ń fún'],
  ['ayo lo n', 'ayọ̀ ló ń'], ['ayo lo', 'ayọ̀ ló'], ['to n', 'tó ń'], ['lo n', 'ló ń'],
  ['o n', 'ó ń'], ['won n', 'wọ́n ń'], ['a n', 'a ń'], ['e n', 'ẹ ń'],
  ['ara ilu', 'ará ìlú'], ['ara ìlu', 'ará ìlú'], ['da ifa', 'dá Ifá'], ['se agbo', 'ṣe àgbo'],
  ['ko gbodo', 'kò gbọdọ̀'], ['ko ja', 'kọjá'], ['koja', 'kọjá'],
  ['kere si mesi', 'Kérésìmesì'], ['keresimesi', 'Kérésìmesì'],
  ['owo re', 'ọwọ́ rẹ'], ['owo mi', 'ọwọ́ mi'], ['owo wa', 'ọwọ́ wa'], ['owo yin', 'ọwọ́ yín'],
  ['lowa', "l'ó wà"], ['lo wa', "l'ó wà"], ['dakun ma je', 'dákun má jẹ́'], ['ma je', 'má jẹ́'],
  ['ki n', 'kí n'], ["l'aiye mi", "l'áyé mi"], ["l'aiye", "l'áyé"], ["l'aye mi", "l'áyé mi"],
  ["l'aye", "l'áyé"], ["l'odun", "l'ọ́dún"], ['omode metta', 'ọmọdé mẹ́ta'], ['omode meta', 'ọmọdé mẹ́ta'],
  ['ogun lakaaye osin imole, eni to ni omi nile ti o fi eje we', 'Ògún Lákàyé, Ọ̀sìn Imọ́lẹ̀, ẹni tí ó ní omi nílé tí ó fi ẹ̀jẹ̀ wẹ̀'],
  ['ogun lakaaye osin imole', 'Ògún Lákàyé, Ọ̀sìn Imọ́lẹ̀'],
  ['eni to ni omi nile ti o fi eje we', 'ẹni tí ó ní omi nílé tí ó fi ẹ̀jẹ̀ wẹ̀'],
  ['orunmila bara agbonmiregun', 'Ọ̀rúnmìlà Barà Àgbọnmìrègún'],
  ['sango olukoso eleyinjue ina', 'Ṣàngó Olúkòso, Ẹlẹ́yinjú Iná'],
  ['sango olukoso', 'Ṣàngó Olúkòso'], ['obatala oosaala oba patapata', 'Ọbàtálá Òòṣàálá, Ọba Pátápátá'],
  ['obatala oosaala', 'Ọbàtálá Òòṣàálá'], ['alafia lounje okan', 'Àlàáfíà l’oúnjẹ ọkàn'],
  ['alafia loonje okan', 'Àlàáfíà l’oúnjẹ ọkàn'], ['bawo ni o se wa', 'Báwo ni o ṣe wà'],
  ['bawo ni gbogbo nkan', 'Báwo ni gbogbo nǹkan'], ['bawo ni nkan', 'Báwo ni nǹkan'],
  ['bi o ti wu ki o ri', 'bí ó ti wù kí ó rí'], ['lati igba naa', 'láti ìgbà náà'],
  ['nitori pe', 'nítorí pé'], ['gege bi', 'gẹ́gẹ́ bí'], ['nigba ti', 'nígbà tí'],
  ['eni to ni', 'ẹni tí ó ní'], ['eni to', 'ẹni tó'], ['omi nile', 'omi nílé'],
  ['ti o fi', 'tí ó fi'], ['ti o', 'tí ó'], ['eje we', 'ẹ̀jẹ̀ wẹ̀'],
  ['ogun lakaaye', 'Ògún Lákàyé'], ['osin imole', 'Ọ̀sìn Imọ́lẹ̀'],
  ['ebi ati ara', 'ẹbí àti ara'], ['ebi ati ore', 'ẹbí àti ọ̀rẹ́'],
  ['se patakai', 'ṣe pàtàkì'], ['se pataki', 'ṣe pàtàkì'], ['ni pataki', 'ní pàtàkì'],
  ['igbesi aiye eda', 'ìgbésí-ayé ẹ̀dá'], ['igbesi aiye', 'ìgbésí-ayé'],
  ['igbesi aye eda', 'ìgbésí-ayé ẹ̀dá'], ['igbesi aye', 'ìgbésí-ayé'], ['igbesiaye', 'ìgbésí-ayé'],
  ['aiye eda', 'ayé ẹ̀dá'], ['aye eda', 'ayé ẹ̀dá'], ['ayanmo eda', 'àyànmọ́ ẹ̀dá'],
  ['ori rere', 'orí rere'], ['ori buruku', 'orí burúkú'], ['ori apeere', 'orí àpẹẹrẹ'],
  ['akunleyan', 'àkúnlẹ̀yàn'], ['atelewo eni', 'àtẹ́lẹwọ́ ẹni'],
  ["iwa l'ewa", "ìwà l'ẹwà"], ['iwa lewa', "ìwà l'ẹwà"],
  ['omolúwabi', 'ọmọlúwàbí'], ['omolúabi', 'ọmọlúwàbí'], ['omolwabi', 'ọmọlúwàbí'],
  ['alajobi', 'alájọbí'], ['oju rere', 'ojú rere'], ['oju aanu', 'ojú àánú'],
  ['owo po', 'ọwọ́ pọ̀'], ['fokan bale', 'fọkàn balẹ̀'], ['fowo sowopo', 'fọwọ́ sowọ́pọ̀'],
  ['iwa pele', 'Ìwà Pẹ̀lẹ́'], ['iwa rere', 'Ìwà Rere'], ['bawo ni', 'Báwo ni'],
  ['e kaasan o', 'Ẹ káàsán o'], ['e kaaro o', 'Ẹ káàárọ̀ o'], ['e kaale o', 'Ẹ káalẹ́ o'],
  ['e kaasan', 'Ẹ káàsán'], ['e kaaro', 'Ẹ káàárọ̀'], ['e kaale', 'Ẹ káalẹ́'],
  ['e ku aaro', 'Ẹ kú àárọ̀'], ['e ku osan', 'Ẹ kú ọ̀sán'], ['e ku ale', 'Ẹ kú alẹ́'],
  ['e ku irole', 'Ẹ kú ìrọ̀lẹ́'], ['e ku abo', 'Ẹ kú àbọ̀'], ['e se pupo', 'Ẹ ṣe púpọ̀'],
  ['o se pupo', 'Ó ṣe púpọ̀'], ['e se o', 'Ẹ ṣe o'], ['o se o', 'Ó ṣe o'],
  ['e se', 'Ẹ ṣe'], ['o se', 'Ó ṣe'], ['o daabo', 'Ó dàbọ̀'], ['alafia ni', 'Àlàáfíà ni'],
  ['odu ifa', 'Odù Ifá'], ['eji ogbe', 'Èjì Ogbè'], ['oyeku meji', 'Ọ̀yẹ̀kú Méjì'],
  ['iwori meji', 'Ìwòrì Méjì'], ['odi meji', 'Òdí Méjì'], ['irosun meji', 'Ìrosùn Méjì'],
  ['owonrin meji', 'Òwọ́nrín Méjì'], ['obara meji', 'Ọ̀bàrà Méjì'], ['okanran meji', 'Ọ̀kànràn Méjì'],
  ['ogunda meji', 'Ògúndá Méjì'], ['osa meji', 'Ọ̀sá Méjì'], ['ika meji', 'Ìká Méjì'],
  ['oturupon meji', 'Òtúrúpọ̀n Méjì'], ['otua meji', 'Òtúá Méjì'], ['irete meji', 'Ìrẹtẹ̀ Méjì'],
  ['ose meji', 'Ọ̀sẹ́ Méjì'], ['ofun meji', 'Òfún Méjì'], ['ade aare', 'Adé Ààrẹ'],
  ['opon ifa', 'Ọpọ́n Ifá'], ['iroke ifa', 'Ìrókẹ́ Ifá'], ['agere ifa', 'Àgéré Ifá'],
  ['ikin ifa', 'Ìkín Ifá'], ['ileke owo', 'Ìlèkè Ọwọ́'], ['fila gobi', 'Fìlà Gọ̀bị́'],
  ['fila abeti aja', 'Fìlà Abetí Ajá'], ['agbada aada', 'Agbádá Aadá'],
  ['ewa aganyin', 'Ẹ̀wà Àgányìn'], ['ewa oloyin', 'Ẹ̀wà Olóyin'], ['iresi ofada', 'Ìrẹsì Ọ̀fàdà'],
  ['amala isu', 'Amàlà Iṣu'], ['amala lafun', 'Amàlà Láfún'], ['obe egusi', 'Ọbẹ̀ Ègúsí'],
  ['obe gbegiri', 'Ọbẹ̀ Gbẹ̀gìrì'], ['obe ewedu', 'Ọbẹ̀ Ewédú'], ['igi ibile', 'Igi Ìbílẹ̀'],
  ['ipinle ogun', 'Ìpínlẹ̀ Ògùn'], ['ipinle oyo', 'Ìpínlẹ̀ Ọ̀yọ́'], ['ipinle osun', 'Ìpínlẹ̀ Ọ̀ṣun'],
  ['ipinle ondo', 'Ìpínlẹ̀ Oǹdó'], ['ipinle ekiti', 'Ìpínlẹ̀ Èkìtì'], ['ipinle lagos', 'Ìpínlẹ̀ Èkó'],
  ['ile ife', 'Ilé-Ifẹ̀']
];

export const MULTI_WORD_PHRASES = [...RAW_MULTI_WORD_PHRASES].sort((a, b) => b[0].length - a[0].length);

// Comprehensive multi-tiered Yorùbá orthographic lexicon
export const DIACRITIC_LEXICON = {
  'onisegun': 'oníṣègùn', 'dodo': 'dòdò', 'gbodo': 'gbọdọ̀',
  'aremu': 'Àrẹ̀mú', 'alabi': 'Àlàbí', 'akinkanju': 'akínkanjú',
  'ra': 'rà', 'dakun': 'dákun', 'sina': 'ṣìnà', 'metta': 'mẹ́ta',
  'meta': 'mẹ́ta', 'sere': 'ṣeré', 'ere': 'eré', 'jo': 'jó', 'ayo': 'ayọ̀',
  'da': 'dá',
  'emi': 'èmi', 'iwo': 'ìwọ', 'oun': 'òun', 'awa': 'àwa', 'eyin': 'ẹ̀yin', 'awon': 'àwọn',
  'mo': 'mo', 'won': 'wọ́n', 'mi': 'mi', 're': 'rẹ', 'wa': 'wa', 'yin': 'yín',
  'to': 'tó', 'ti': 'tí', 'ko': 'kò',
  'ni': 'ní', 'si': 'sí', 'lati': 'láti', 'ninu': 'nínú', 'lori': 'lórí',
  'pelu': 'pẹ̀lú', 'sugbon': 'ṣùgbọ́n', 'tabi': 'tàbí', 'gege': 'gẹ́gẹ́', 'bi': 'bí',
  'bii': 'bíi', 'nje': 'njẹ́', 'ki': 'kí', 'nitori': 'nítorí', 'koto': 'kótó',
  'titi': 'títí', 'kosi': 'kòsí', 'nkan': 'nǹkan', 'gbogbo': 'gbogbo', 'pupo': 'púpọ̀',
  'die': 'díẹ̀', 'oto': 'ọ̀tọ̀', 'nikan': 'nìkan', 'bayi': 'báyìí', 'lodoodun': 'lọ́dọọdún',
  'ati': 'àti',
  'lo': 'lọ', 'se': 'ṣe', 'ri': 'rí', 'fe': 'fẹ́', 'je': 'jẹ', 'mu': 'mu',
  'sun': 'sùn', 'dide': 'dìde', 'bo': 'bọ̀', 'fun': 'fún', 'ka': 'kà',
  'so': 'sọ', 'wi': 'wí', 'gbo': 'gbọ́', 'wo': 'wò', 'be': 'bẹ', 'dupe': 'dúpẹ́',
  'ba': 'bá', 'le': 'lè', 'ma': 'má', 'gba': 'gbà', 'fi': 'fi', 'pe': 'pè',
  'bere': 'bẹ̀rẹ̀', 'pari': 'parí', 'ran': 'rán', 'tan': 'tàn', 'de': 'dé',
  'wole': 'wọlé', 'jade': 'jáde', 'sunmo': 'súnmọ́', 'pada': 'padà', 'gbe': 'gbé',
  'muwa': 'múwá', 'kede': 'kédè', 'ronu': 'rònú', 'we': 'wẹ̀',
  'ori': 'orí', 'oju': 'ojú', 'eti': 'etí', 'enu': 'ẹnu', 'ese': 'ẹsẹ̀', 'okan': 'ọkàn',
  'ara': 'ara', 'eje': 'ẹ̀jẹ̀', 'egungun': 'egúngún', 'apa': 'apá', 'ite': 'ìtẹ́',
  'ebi': 'ẹbí', 'eniyan': 'ènìyàn', 'eda': 'ẹ̀dá', 'omode': 'ọmọdé', 'agbalagba': 'àgbàlagbà',
  'alafia': 'àlàáfíà', 'bawo': 'báwo', 'baba': 'bàbá', 'iya': 'ìyá', 'omo': 'ọmọ', 'oko': 'ọkọ',
  'aya': 'aya', 'egbon': 'ẹgbọ́n', 'aburo': 'àbúrò', 'ore': 'ọ̀rẹ́', 'obinrin': 'obìnrin',
  'okunrin': 'ọkùnrin', 'ilu': 'ìlú', 'agba': 'àgbà', 'ijoye': 'ìjòyè', 'oba': 'ọba',
  'kabiyesi': 'kábíyèsí', 'omolúwabi': 'ọmọlúwàbí',
  'aye': 'ayé', 'aiye': 'ayé', 'orun': 'ọ̀run', 'ile': 'ilé', 'nile': 'nílé', 'omi': 'omi',
  'ina': 'iná', 'afefe': 'afẹ́fẹ́', 'owo': 'owó', 'ojo': 'òjò', 'igi': 'igi', 'ewe': 'ewé',
  'eran': 'ẹran', 'eye': 'ẹyẹ', 'aja': 'ajá', 'agbo': 'àgbò', 'agutan': 'àgùntàn', 'adie': 'adìyẹ',
  'ewure': 'ewúrẹ́', 'odidere': 'òdídẹrẹ́',
  'pataki': 'pàtàkì', 'patakai': 'pàtàkì', 'igbesi': 'ìgbésí', 'ogbon': 'ọgbọ́n',
  'imo': 'ìmọ̀', 'oye': 'òye', 'iwa': 'ìwà', 'rere': 'rere', 'pele': 'pẹ̀lẹ́',
  'suuru': 'sùúrù', 'ifarada': 'ìfaradà', 'otito': 'òtítọ́', 'ododo': 'òdodo',
  'aje': 'ajé', 'ola': 'ọlá', 'ade': 'adé', 'oriki': 'oríkì', 'owe': 'òwe',
  'itan': 'ìtàn', 'asa': 'àṣà', 'ise': 'iṣẹ́',
  'osin': 'ọ̀sìn', 'imole': 'imọ́lẹ̀', 'eni': 'ẹni', 'orisa': 'òrìṣà', 'olodumare': 'olódùmarè',
  'orunmila': 'ọ̀rúnmìlà', 'sango': 'ṣàngó', 'osun': 'ọ̀ṣun', 'oya': 'ọya', 'esu': 'èṣù',
  'obatala': 'ọbàtálá', 'yemoja': 'yemọja', 'osanyin': 'ọ̀sanyìn', 'sopona': 'ṣọ̀pọ̀nná',
  'ifa': 'ifá', 'odu': 'odù', 'awo': 'awo', 'babalawo': 'babaláwo', 'iyanifa': 'ìyánífá',
  'araba': 'àràbà', 'oluwo': 'olúwo', 'akoda': 'àkọ́dá', 'aseda': 'àṣẹ̀dá', 'lakaaye': 'lákàyé',
  'opon': 'ọpọ́n', 'iroke': 'ìrókẹ́', 'agere': 'àgéré', 'agbada': 'agbádá', 'buba': 'bùbá',
  'sokoto': 'ṣòkòtò', 'iro': 'ìró', 'gele': 'gèlè', 'fila': 'fìlà', 'ileke': 'ìlèkè',
  'iyun': 'ìyùn', 'akun': 'akún', 'segi': 'ṣẹ́gi', 'amala': 'amàlà', 'iyan': 'ìyán',
  'eba': 'ẹ̀bà', 'iresi': 'ìrẹsì', 'ewa': 'ẹ̀wà', 'isu': 'iṣu', 'obe': 'ọbẹ̀', 'okele': 'òkèlè',
  'bata': 'bàtá', 'dundun': 'dùndún', 'sakara': 'sákárà', 'apala': 'àpàlà', 'fuji': 'fújì',
  'juju': 'jùjú', 'gelede': 'geledẹ́', 'adire': 'adìrẹ', 'odun': 'ọdún', 'ayo': 'ayò', 'ere': 'eré'
};

export function disambiguateClientHomograph(word, text) {
  const wLow = word.toLowerCase();
  const cLow = text.toLowerCase();

  if (wLow === 'ogun') {
    if (/\b(state|ipinle|ìpínlẹ̀|abeokuta|abẹ́òkúta|governor)\b/.test(cLow)) {
      return word[0] === word[0].toUpperCase() ? 'Ìpínlẹ̀ Ògùn' : 'ìpínlẹ̀ ògùn';
    }
    if (/\b(war|battle|warfare|conflict|kiriji|ijaye|balogun|jagunjagun)\b/.test(cLow)) {
      return word[0] === word[0].toUpperCase() ? 'Ogun' : 'ogun';
    }
    return word[0] === word[0].toUpperCase() ? 'Ògún' : 'ògún';
  }

  if (wLow === 'oro') {
    if (/\b(wealth|rich|money|owo|ola|aje)\b/.test(cLow)) {
      return word[0] === word[0].toUpperCase() ? 'Ọrọ̀' : 'ọrọ̀';
    }
    if (/\b(cult|rite|ritual|secret|egungun|awo)\b/.test(cLow)) {
      return word[0] === word[0].toUpperCase() ? 'Orò' : 'orò';
    }
    return word[0] === word[0].toUpperCase() ? 'Ọ̀rọ̀' : 'ọ̀rọ̀';
  }

  if (wLow === 'owo') {
    if (/\b(hand|arm|otun|osi|mu|re|rẹ|mi|wa|yin|lowo|lọ́wọ́)\b/.test(cLow)) {
      return word[0] === word[0].toUpperCase() ? 'Ọwọ́' : 'ọwọ́';
    }
    if (/\b(respect|reverence|ibowo|agba)\b/.test(cLow)) {
      return word[0] === word[0].toUpperCase() ? 'Ọ̀wọ̀' : 'ọ̀wọ̀';
    }
    return word[0] === word[0].toUpperCase() ? 'Owó' : 'owó';
  }

  return null;
}

// Client-side rule-based diacritization algorithm
export function restoreDiacriticsAlgorithmic(text) {
  let result = text;
  const placeholders = {};

  // 1. Multi-word phrases
  MULTI_WORD_PHRASES.forEach(([phrase, diac], idx) => {
    const reg = new RegExp(`\\b${phrase}\\b`, 'gi');
    result = result.replace(reg, (m) => {
      let finalVal = diac;
      if (m === m.toUpperCase()) finalVal = diac.toUpperCase();
      else if (m[0] === m[0].toUpperCase()) finalVal = diac[0].toUpperCase() + diac.slice(1);
      const key = `__CLIENT_PHRASE_${idx}_${Object.keys(placeholders).length}__`;
      placeholders[key] = finalVal;
      return key;
    });
  });

  // 2. Single token replacements
  result = result.replace(/\b[a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]+\b/g, (match) => {
    if (match.startsWith('__CLIENT_')) return match;
    const lower = match.toLowerCase();

    const homo = disambiguateClientHomograph(match, text);
    if (homo) return homo;

    if (DIACRITIC_LEXICON[lower]) {
      const replacement = DIACRITIC_LEXICON[lower];
      if (match === match.toUpperCase()) return replacement.toUpperCase();
      if (match[0] === match[0].toUpperCase()) return replacement.charAt(0).toUpperCase() + replacement.slice(1);
      return replacement;
    }
    return match;
  });

  // 3. Restore placeholders
  Object.keys(placeholders).forEach((k) => {
    result = result.replace(k, placeholders[k]);
  });

  return result;
}

// Client-side cultural glossing synthesis
export function synthesizeCulturalGloss(text) {
  const textClean = (text || '').toLowerCase();

  if (textClean.includes('eji ogbe') || textClean.includes('èjì ogbè')) {
    return {
      orthographic_retention: 'Èjì Ogbè lórí Ọpọ́n Ifá',
      literal_translation: 'Èjì Ogbè (The Premier Light) inscribed upon the sacred Ifá Divination Tray.',
      cultural_gloss: 'Èjì Ogbè is the supreme primordial chapter (#1) of the 256 Odù Ifá corpus, embodying pure cosmic illumination, divine consciousness, and spiritual alignment. When cast by a Babaláwo upon the circular Ọpọ́n Ifá tray spread with consecrated Ìrosùn camwood powder, it signifies the unclouded victory of light over chaos, auspicious breakthroughs, and direct communion with Olódùmarè.'
    };
  }

  if (textClean.includes('ogun') || textClean.includes('ògún')) {
    return {
      orthographic_retention: 'Ògún Lákàyé, Ọ̀sìn Imọ́lẹ̀',
      literal_translation: 'Ògún, Lord of the entire world, Chief among primordial luminaries.',
      cultural_gloss: 'Ògún is the primordial Yorùbá divinity of metallurgy, iron, agriculture, and martial justice. As the path-clearer who forged the road between heaven and earth through virgin cosmic wilderness, iron is consecrated as his living body. Blacksmiths, drivers, hunters, and surgeons revere him as the guardian of oath-taking, divine integrity, and productive labor.'
    };
  }

  const matched = masterCorpus.find(e =>
    e.title.toLowerCase().includes(textClean) || textClean.includes(e.title.toLowerCase())
  );

  if (matched) {
    return {
      orthographic_retention: matched.title,
      literal_translation: `English contextual rendering for ${matched.title} (${matched.category})`,
      cultural_gloss: `${matched.description} ${matched.etymology_and_philosophy || ''} Proverbial grounding: ${Array.isArray(matched.proverbs_and_oral_traditions) ? matched.proverbs_and_oral_traditions[0] : matched.proverbs_and_oral_traditions || ''}`
    };
  }

  return {
    orthographic_retention: text,
    literal_translation: `Literal translation for: ${text}`,
    cultural_gloss: 'Authentic cultural concept preserved across oral history, metaphysical balance, and lineage tradition in classical Yorùbá philosophy.'
  };
}
