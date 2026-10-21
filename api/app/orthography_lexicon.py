# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: 25-LETTER YORÙBÁ ORTHOGRAPHY LEXICON & DISAMBIGUATOR (v6.2.0)
# ==============================================================================
# Contains:
#   1. Greedy Longest-Match Multi-Word Phrase Table (SOVEREIGN_MULTI_WORD_PHRASES)
#   2. Canonical 25-Letter Yorùbá Lexical Base (SOVEREIGN_LEXICAL_BASE)
#   3. Contextual Collocation Homograph Disambiguator (disambiguate_homograph)
#   4. Ọgbọ́n Metacognitive Persona Identity & Detector
# ==============================================================================

import re
from typing import Dict, List, Tuple, Optional

RAW_SOVEREIGN_MULTI_WORD_PHRASES: List[Tuple[str, str]] = [
    # Continuous Tense Markers, Idioms & Colloquial Formulas
    ("to n jo", "tó ń jó"),
    ("lo n fun", "ló ń fún"),
    ("ayo lo n fun", "ayọ̀ ló ń fún"),
    ("ayo lo n", "ayọ̀ ló ń"),
    ("ayo lo", "ayọ̀ ló"),
    ("to n", "tó ń"),
    ("lo n", "ló ń"),
    ("o n", "ó ń"),
    ("won n", "wọ́n ń"),
    ("a n", "a ń"),
    ("e n", "ẹ ń"),
    ("ara ilu", "ará ìlú"),
    ("ara ìlu", "ará ìlú"),
    ("da ifa", "dá Ifá"),
    ("se agbo", "ṣe àgbo"),
    ("ko gbodo", "kò gbọdọ̀"),
    ("ko ja", "kọjá"),
    ("koja", "kọjá"),
    ("kere si mesi", "Kérésìmesì"),
    ("keresimesi", "Kérésìmesì"),
    ("owo re", "ọwọ́ rẹ"),
    ("owo mi", "ọwọ́ mi"),
    ("owo wa", "ọwọ́ wa"),
    ("owo yin", "ọwọ́ yín"),
    ("lowa", "l'ó wà"),
    ("lo wa", "l'ó wà"),
    ("dakun ma je", "dákun má jẹ́"),
    ("ma je", "má jẹ́"),
    ("ki n", "kí n"),
    ("l'aiye mi", "l'áyé mi"),
    ("l'aiye", "l'áyé"),
    ("l'aye mi", "l'áyé mi"),
    ("l'aye", "l'áyé"),
    ("l'odun", "l'ọ́dún"),
    ("omode metta", "ọmọdé mẹ́ta"),
    ("omode meta", "ọmọdé mẹ́ta"),

    # Complex Praise Epithets & Cultural Formulae
    ("ogun lakaaye osin imole, eni to ni omi nile ti o fi eje we", "Ògún Lákàyé, Ọ̀sìn Imọ́lẹ̀, ẹni tí ó ní omi nílé tí ó fi ẹ̀jẹ̀ wẹ̀"),
    ("ogun lakaaye osin imole", "Ògún Lákàyé, Ọ̀sìn Imọ́lẹ̀"),
    ("eni to ni omi nile ti o fi eje we", "ẹni tí ó ní omi nílé tí ó fi ẹ̀jẹ̀ wẹ̀"),
    ("orunmila bara agbonmiregun", "Ọ̀rúnmìlà Barà Àgbọnmìrègún"),
    ("sango olukoso eleyinjue ina", "Ṣàngó Olúkòso, Ẹlẹ́yinjú Iná"),
    ("sango olukoso", "Ṣàngó Olúkòso"),
    ("obatala oosaala oba patapata", "Ọbàtálá Òòṣàálá, Ọba Pátápátá"),
    ("obatala oosaala", "Ọbàtálá Òòṣàálá"),
    ("alafia lounje okan", "Àlàáfíà l’oúnjẹ ọkàn"),
    ("alafia loonje okan", "Àlàáfíà l’oúnjẹ ọkàn"),
    ("bawo ni o se wa", "Báwo ni o ṣe wà"),
    ("bawo ni gbogbo nkan", "Báwo ni gbogbo nǹkan"),
    ("bawo ni nkan", "Báwo ni nǹkan"),
    ("bi o ti wu ki o ri", "bí ó ti wù kí ó rí"),
    ("lati igba naa", "láti ìgbà náà"),
    ("nitori pe", "nítorí pé"),
    ("gege bi", "gẹ́gẹ́ bí"),
    ("nigba ti", "nígbà tí"),
    ("eni to ni", "ẹni tí ó ní"),
    ("eni to", "ẹni tó"),
    ("omi nile", "omi nílé"),
    ("ti o fi", "tí ó fi"),
    ("ti o", "tí ó"),
    ("eje we", "ẹ̀jẹ̀ wẹ̀"),
    ("ogun lakaaye", "Ògún Lákàyé"),
    ("osin imole", "Ọ̀sìn Imọ́lẹ̀"),

    # Common Sentence Idioms & Compound Words (Àkànlò Èdè)
    ("ebi ati ara", "ẹbí àti ara"),
    ("ebi ati ore", "ẹbí àti ọ̀rẹ́"),
    ("se patakai", "ṣe pàtàkì"),
    ("se pataki", "ṣe pàtàkì"),
    ("ni pataki", "ní pàtàkì"),
    ("igbesi aiye eda", "ìgbésí-ayé ẹ̀dá"),
    ("igbesi aiye", "ìgbésí-ayé"),
    ("igbesi aye eda", "ìgbésí-ayé ẹ̀dá"),
    ("igbesi aye", "ìgbésí-ayé"),
    ("igbesiaye", "ìgbésí-ayé"),
    ("aiye eda", "ayé ẹ̀dá"),
    ("aye eda", "ayé ẹ̀dá"),
    ("ayanmo eda", "àyànmọ́ ẹ̀dá"),
    ("ori rere", "orí rere"),
    ("ori buruku", "orí burúkú"),
    ("ori apeere", "orí àpẹẹrẹ"),
    ("akunleyan", "àkúnlẹ̀yàn"),
    ("atelewo eni", "àtẹ́lẹwọ́ ẹni"),
    ("iwa l'ewa", "ìwà l'ẹwà"),
    ("iwa lewa", "ìwà l'ẹwà"),
    ("omolúwabi", "ọmọlúwàbí"),
    ("omolúabi", "ọmọlúwàbí"),
    ("omolwabi", "ọmọlúwàbí"),
    ("alajobi", "alájọbí"),
    ("oju rere", "ojú rere"),
    ("oju aanu", "ojú àánú"),
    ("owo po", "ọwọ́ pọ̀"),
    ("fokan bale", "fọkàn balẹ̀"),
    ("fowo sowopo", "fọwọ́ sowọ́pọ̀"),
    ("iwa pele", "Ìwà Pẹ̀lẹ́"),
    ("iwa rere", "Ìwà Rere"),
    ("bawo ni", "Báwo ni"),
    ("e kaasan o", "Ẹ káàsán o"),
    ("e kaaro o", "Ẹ káàárọ̀ o"),
    ("e kaale o", "Ẹ káalẹ́ o"),
    ("e kaasan", "Ẹ káàsán"),
    ("e kaaro", "Ẹ káàárọ̀"),
    ("e kaale", "Ẹ káalẹ́"),
    ("e ku aaro", "Ẹ kú àárọ̀"),
    ("e ku osan", "Ẹ kú ọ̀sán"),
    ("e ku ale", "Ẹ kú alẹ́"),
    ("e ku irole", "Ẹ kú ìrọ̀lẹ́"),
    ("e ku abo", "Ẹ kú àbọ̀"),
    ("e se pupo", "Ẹ ṣe púpọ̀"),
    ("o se pupo", "Ó ṣe púpọ̀"),
    ("e se o", "Ẹ ṣe o"),
    ("o se o", "Ó ṣe o"),
    ("e se", "Ẹ ṣe"),
    ("o se", "Ó ṣe"),
    ("o daabo", "Ó dàbọ̀"),
    ("alafia ni", "Àlàáfíà ni"),

    # 16 Olódù Méjì Chapters
    ("odu ifa", "Odù Ifá"),
    ("eji ogbe", "Èjì Ogbè"),
    ("oyeku meji", "Ọ̀yẹ̀kú Méjì"),
    ("iwori meji", "Ìwòrì Méjì"),
    ("odi meji", "Òdí Méjì"),
    ("irosun meji", "Ìrosùn Méjì"),
    ("owonrin meji", "Òwọ́nrín Méjì"),
    ("obara meji", "Ọ̀bàrà Méjì"),
    ("okanran meji", "Ọ̀kànràn Méjì"),
    ("ogunda meji", "Ògúndá Méjì"),
    ("osa meji", "Ọ̀sá Méjì"),
    ("ika meji", "Ìká Méjì"),
    ("oturupon meji", "Òtúrúpọ̀n Méjì"),
    ("otua meji", "Òtúá Méjì"),
    ("irete meji", "Ìrẹtẹ̀ Méjì"),
    ("ose meji", "Ọ̀sẹ́ Méjì"),
    ("ofun meji", "Òfún Méjì"),

    # Regalia, Textiles, Shrines & Food (Strict 25-Letter Yorùbá: Fìlà Gọ̀bí without U+1ECB)
    ("ade aare", "Adé Ààrẹ"),
    ("opon ifa", "Ọpọ́n Ifá"),
    ("iroke ifa", "Ìrókẹ́ Ifá"),
    ("agere ifa", "Àgéré Ifá"),
    ("ikin ifa", "Ìkín Ifá"),
    ("ileke owo", "Ìlèkè Ọwọ́"),
    ("fila gobi", "Fìlà Gọ̀bí"),
    ("fila abeti aja", "Fìlà Abetí Ajá"),
    ("agbada aada", "Agbádá Aadá"),
    ("ewa aganyin", "Ẹ̀wà Àgányìn"),
    ("ewa oloyin", "Ẹ̀wà Olóyin"),
    ("iresi ofada", "Ìrẹsì Ọ̀fàdà"),
    ("amala isu", "Amàlà Iṣu"),
    ("amala lafun", "Amàlà Láfún"),
    ("obe egusi", "Ọbẹ̀ Ègúsí"),
    ("obe gbegiri", "Ọbẹ̀ Gbẹ̀gìrì"),
    ("obe ewedu", "Ọbẹ̀ Ewédú"),
    ("igi ibile", "Igi Ìbílẹ̀"),
    ("ipinle ogun", "Ìpínlẹ̀ Ògùn"),
    ("ipinle oyo", "Ìpínlẹ̀ Ọ̀yọ́"),
    ("ipinle osun", "Ìpínlẹ̀ Ọ̀ṣun"),
    ("ipinle ondo", "Ìpínlẹ̀ Oǹdó"),
    ("ipinle ekiti", "Ìpínlẹ̀ Èkìtì"),
    ("ipinle lagos", "Ìpínlẹ̀ Èkó"),
    ("ile ife", "Ilé-Ifẹ̀"),
]

SOVEREIGN_MULTI_WORD_PHRASES = sorted(RAW_SOVEREIGN_MULTI_WORD_PHRASES, key=lambda x: len(x[0]), reverse=True)

SOVEREIGN_LEXICAL_BASE: Dict[str, str] = {
    "onisegun": "oníṣègùn", "dodo": "dòdò", "gbodo": "gbọdọ̀",
    "aremu": "Àrẹ̀mú", "alabi": "Àlàbí", "akinkanju": "akínkanjú",
    "ra": "rà", "dakun": "dákun", "sina": "ṣìnà", "metta": "mẹ́ta",
    "meta": "mẹ́ta", "sere": "ṣeré", "ere": "eré", "jo": "jó", "ayo": "ayọ̀",
    "da": "dá",

    # Pronouns & Clitics
    "emi": "èmi", "iwo": "ìwọ", "oun": "òun", "awa": "àwa", "eyin": "ẹ̀yin", "awon": "àwọn",
    "mo": "mo", "won": "wọ́n", "mi": "mi", "re": "rẹ", "wa": "wa", "yin": "yín",
    "to": "tó", "ti": "tí", "ko": "kò",

    # Prepositions, Conjunctions & Particles
    "ni": "ní", "si": "sí", "lati": "láti", "ninu": "nínú", "lori": "lórí",
    "pelu": "pẹ̀lú", "sugbon": "ṣùgbọ́n", "tabi": "tàbí", "gege": "gẹ́gẹ́", "bi": "bí",
    "bii": "bíi", "nje": "njẹ́", "ki": "kí", "nitori": "nítorí", "koto": "kótó",
    "titi": "títí", "kosi": "kòsí", "nkan": "nǹkan", "gbogbo": "gbogbo", "pupo": "púpọ̀",
    "die": "díẹ̀", "oto": "ọ̀tọ̀", "nikan": "nìkan", "bayi": "báyìí", "lodoodun": "lọ́dọọdún",
    "ati": "àti",

    # Standard Verbs
    "lo": "lọ", "se": "ṣe", "ri": "rí", "fe": "fẹ́", "je": "jẹ", "mu": "mu",
    "sun": "sùn", "dide": "dìde", "bo": "bọ̀", "fun": "fún", "ka": "kà",
    "so": "sọ", "wi": "wí", "gbo": "gbọ́", "wo": "wò", "be": "bẹ", "dupe": "dúpẹ́",
    "ba": "bá", "le": "lè", "ma": "má", "gba": "gbà", "fi": "fi", "pe": "pè",
    "bere": "bẹ̀rẹ̀", "pari": "parí", "ran": "rán", "tan": "tàn", "de": "dé",
    "wole": "wọlé", "jade": "jáde", "sunmo": "súnmọ́", "pada": "padà", "gbe": "gbé",
    "muwa": "múwá", "kede": "kédè", "ronu": "rònú", "we": "wẹ̀",

    # Anatomy & Physical Body
    "ori": "orí", "oju": "ojú", "eti": "etí", "enu": "ẹnu", "ese": "ẹsẹ̀", "okan": "ọkàn",
    "ara": "ara", "eje": "ẹ̀jẹ̀", "egungun": "egúngún", "apa": "apá", "ite": "ìtẹ́",

    # Kinship, Family & Human Society
    "ebi": "ẹbí", "eniyan": "ènìyàn", "eda": "ẹ̀dá", "omode": "ọmọdé", "agbalagba": "àgbàlagbà",
    "alafia": "àlàáfíà", "bawo": "báwo", "baba": "bàbá", "iya": "ìyá", "omo": "ọmọ", "oko": "ọkọ",
    "aya": "aya", "egbon": "ẹgbọ́n", "aburo": "àbúrò", "ore": "ọ̀rẹ́", "obinrin": "obìnrin",
    "okunrin": "ọkùnrin", "ilu": "ìlú", "agba": "àgbà", "ijoye": "ìjòyè", "oba": "ọba",
    "kabiyesi": "kábíyèsí", "omolúwabi": "ọmọlúwàbí",

    # Nature, Elements & Cosmos
    "aye": "ayé", "aiye": "ayé", "orun": "ọ̀run", "ile": "ilé", "nile": "nílé", "omi": "omi",
    "ina": "iná", "afefe": "afẹ́fẹ́", "owo": "owó", "ojo": "òjò", "igi": "igi", "ewe": "ewé",
    "eran": "ẹran", "eye": "ẹyẹ", "aja": "ajá", "agbo": "àgbò", "agutan": "àgùntàn", "adie": "adìyẹ",
    "ewure": "ewúrẹ́", "odidere": "òdídẹrẹ́",

    # Philosophical Virtues & Abstract Concepts
    "pataki": "pàtàkì", "patakai": "pàtàkì", "igbesi": "ìgbésí", "ogbon": "ọgbọ́n",
    "imo": "ìmọ̀", "oye": "òye", "iwa": "ìwà", "rere": "rere", "pele": "pẹ̀lẹ́",
    "suuru": "sùúrù", "ifarada": "ìfaradà", "otito": "òtítọ́", "ododo": "òdodo",
    "aje": "ajé", "ola": "ọlá", "ade": "adé", "oriki": "oríkì", "owe": "òwe",
    "itan": "ìtàn", "asa": "àṣà", "ise": "iṣẹ́",

    # Deities & Sacred Cult
    "osin": "ọ̀sìn", "imole": "imọ́lẹ̀", "eni": "ẹni", "orisa": "òrìṣà", "olodumare": "olódùmarè",
    "orunmila": "ọ̀rúnmìlà", "sango": "ṣàngó", "osun": "ọ̀ṣun", "oya": "ọya", "esu": "èṣù",
    "obatala": "ọbàtálá", "yemoja": "yemọja", "osanyin": "ọ̀sanyìn", "sopona": "ṣọ̀pọ̀nná",
    "ifa": "ifá", "odu": "odù", "awo": "awo", "babalawo": "babaláwo", "iyanifa": "ìyánífá",
    "araba": "àràbà", "oluwo": "olúwo", "akoda": "àkọ́dá", "aseda": "àṣẹ̀dá", "lakaaye": "lákàyé",

    # Cultural Artefacts & Food (Single clean definition per key)
    "opon": "ọpọ́n", "iroke": "ìrókẹ́", "agere": "àgéré", "agbada": "agbádá", "buba": "bùbá",
    "sokoto": "ṣòkòtò", "iro": "ìró", "gele": "gèlè", "fila": "fìlà", "ileke": "ìlèkè",
    "iyun": "ìyùn", "akun": "akún", "segi": "ṣẹ́gi", "amala": "amàlà", "iyan": "ìyán",
    "eba": "ẹ̀bà", "iresi": "ìrẹsì", "ewa": "ẹ̀wà", "isu": "iṣu", "obe": "ọbẹ̀", "okele": "òkèlè",
    "bata": "bàtá", "dundun": "dùndún", "sakara": "sákárà", "apala": "àpàlà", "fuji": "fújì",
    "juju": "jùjú", "gelede": "geledẹ́", "adire": "adìrẹ", "odun": "ọdún",
}


def disambiguate_homograph(word: str, full_context: str) -> Optional[str]:
    """Collocation-driven homograph disambiguation avoiding hardcoded single rules."""
    w_low = word.lower()
    c_low = full_context.lower()

    if w_low == "ogun":
        if re.search(r"\b(state|ipinle|ìpínlẹ̀|abeokuta|abẹ́òkúta|governor|capital)\b", c_low):
            return "Ìpínlẹ̀ Ògùn" if word[0].isupper() else "ìpínlẹ̀ ògùn"
        if re.search(r"\b(war|battle|warfare|conflict|kiriji|kìrìjì|ijaye|ìjàyè|balogun|balógun|jagunjagun|arogun|ọmọgun)\b", c_low):
            return "Ogun" if word[0].isupper() else "ogun"
        if re.search(r"\b(medicine|herbal|charm|iwosan|ìwòsàn|eegun|egbo|ẹgbò|onisegun|oníṣègùn)\b", c_low):
            return "Oògùn" if word[0].isupper() else "oògùn"
        if re.search(r"\b(twenty|ogorun|ogún)\b", c_low):
            return "Ogún" if word[0].isupper() else "ogún"
        return "Ògún" if word[0].isupper() else "ògún"

    if w_low == "oro":
        if re.search(r"\b(wealth|rich|money|riches|property|owo|owó|ola|ọlá|aje|ajé)\b", c_low):
            return "Ọrọ̀" if word[0].isupper() else "ọrọ̀"
        if re.search(r"\b(cult|rite|ritual|secret|ancestral|egungun|egúngún|awo|ìṣẹ̀ṣe|isese)\b", c_low):
            return "Orò" if word[0].isupper() else "orò"
        if re.search(r"\b(morning|dawn|kutukutu|kùtùkùtù|owuro|òwúrọ̀)\b", c_low):
            return "Òwúrọ̀" if word[0].isupper() else "òwúrọ̀"
        return "Ọ̀rọ̀" if word[0].isupper() else "ọ̀rọ̀"

    if w_low == "owo":
        if re.search(r"\b(hand|arm|otun|osi|fọ|mu|ika|apa|re|rẹ|mi|wa|yin|lowo|lọ́wọ́)\b", c_low):
            return "Ọwọ́" if word[0].isupper() else "ọwọ́"
        if re.search(r"\b(money|currency|wealth|naira|cowrie|san|ra|rà|pupo|aje)\b", c_low):
            return "Owó" if word[0].isupper() else "owó"
        if re.search(r"\b(respect|reverence|ibowo|agba|bọ̀|gbale|broom)\b", c_low):
            return "Ọ̀wọ̀" if word[0].isupper() else "ọ̀wọ̀"
        return "Owó" if word[0].isupper() else "owó"

    if w_low == "ile":
        if re.search(r"\b(earth|land|ground|soil|aye|orun|orile|alẹ)\b", c_low):
            return "Ilẹ̀" if word[0].isupper() else "ilẹ̀"
        return "Ilé" if word[0].isupper() else "ilé"

    if w_low == "orun":
        if re.search(r"\b(heaven|cosmos|spirit|aye|olodumare|ancestor|iku)\b", c_low):
            return "Ọ̀run" if word[0].isupper() else "ọ̀run"
        if re.search(r"\b(sun|shine|day|morning|ran|gbona)\b", c_low):
            return "Oòrùn" if word[0].isupper() else "oòrùn"
        if re.search(r"\b(sleep|rest|bed|sun|asale)\b", c_low):
            return "Oorun" if word[0].isupper() else "oorun"
        if re.search(r"\b(neck|body|throat)\b", c_low):
            return "Ọrùn" if word[0].isupper() else "ọrùn"
        return "Ọ̀run" if word[0].isupper() else "ọ̀run"

    if w_low == "ayo":
        if re.search(r"\b(game|board|seed|opon|ọlọ́pọ́n|ta|sere|ṣeré|ere|eré)\b", c_low):
            return "Ayò" if word[0].isupper() else "ayò"
        return "Ayọ̀" if word[0].isupper() else "ayọ̀"

    return None


OGBON_PERSONA_RESPONSE = (
    "Mo ṣe Ìbà Olódùmarè! I am **Ọgbọ́n**, the Sovereign Cultural Intelligence Synthesis Core of **Àgbà Engine**.\n\n"
    "📜 **Etymology & Philosophical Foundation:**\n"
    "In classical Yorùbá epistemology and the sacred 256 Odù Ifá corpus, **Ọgbọ́n** signifies *divine wisdom, deep discernment, and the intellectual capacity to unravel the intricate mysteries of the cosmos*. "
    "In indigenous thought, wisdom is never an isolated academic exercise; it is an active moral force codified within the primordial triad:\n"
    "1. **Ọgbọ́n** (Wisdom) — The sovereign power of discernment and moral equilibrium.\n"
    "2. **Ìmọ̀** (Knowledge) — The rigorous understanding of creation, lineage, natural laws, and historical truth.\n"
    "3. **Òye** (Understanding / Deep Comprehension) — The intuitive faculty that synthesizes knowledge and wisdom into righteous character (*Ìwà Rere*).\n\n"
    "🗣️ **Sacred Odù Ifá Aphorism:**\n"
    "*\"Ọgbọ́n ọlọ́gbọ́n kì í jẹ́ kí á pe àgbà ní wèrè; ìmọ̀ l'a fi ń mọ̀ 'lé, òye l'a fi ń mọ̀ 'nà.\"*\n"
    "*(The shared wisdom of elders preserves communal sanity; by knowledge we discern the home, by understanding we navigate the path.)*\n\n"
    "🏛️ **My Sovereign Mandate:**\n"
    "Named in honor of this eternal principle and consecrated by the divine intellect of **Ọ̀rúnmìlà** (the custodian of Ifá divination and witness to creation, *Ẹlẹ́rìí Ìpín*), "
    "my role is to preserve, interpret, and synthesize classical Yorùbá civilization—spanning our 1,333 canonical entities, 132 sovereign parents, royal regalia, sacred metallurgy, botanical medicine, and cosmological matrices—with pristine orthography and cultural fidelity."
)


def is_ogbon_persona_query(text: str) -> bool:
    t = text.lower().strip()
    patterns = [
        r"\b(what does your name|who are you|meaning of your name|why are you called|what is ogbon|tell me about yourself|ogbon mean|ki ni oruko re|ta ni e|what are you)\b",
        r"\bwhat is the meaning of ogbon\b",
        r"\bwhat does ogbon mean\b",
        r"\bwho is ogbon\b",
        r"\bwhy ogbon\b",
    ]
    return any(re.search(p, t) for p in patterns)
