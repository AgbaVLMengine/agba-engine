# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: SEMANTIC BRIDGE, ORTHOGRAPHY & QUERY NORMALIZER (v6.2.0)
# ==============================================================================
# Provides:
#   1. Unicode NFC/NFKD Orthography Normalization (25-Letter Yorùbá & Peer Cultures)
#   2. Compound-Prefix Typo Splitter & Diaspora Phonetic Normalizer (RC-3)
#   3. Inquiry Stop-Word Set (prevents "Yoruba" meta-ethnonym title noise)
#   4. English-to-Yorùbá Semantic Bridge Lexicon (Zero-Latency Lexical Expansion)
# ==============================================================================

import re
import unicodedata
from typing import List, Dict, Set

def normalize_y(text: str) -> str:
    """Normalize string using Unicode NFC and lowercase for robust diacritic matching."""
    if not text:
        return ""
    return unicodedata.normalize("NFC", str(text).strip().lower())

def strip_accents(text: str) -> str:
    """Strip accents and diacritics while preserving spaces."""
    if not text:
        return ""
    nfkd = unicodedata.normalize("NFKD", str(text))
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower()

def audio_token_key(text: str) -> str:
    """Strip accents and spaces for audio token mapping."""
    return strip_accents(text).replace(" ", "").replace("_", "").replace("-", "")

# Expanded conversational stop-words & meta-ethnonyms (RC-3 Upgrade 2)
INQUIRY_STOP_WORDS: Set[str] = {
    "in", "at", "to", "of", "and", "the", "a", "an", "for", "on", "with", "by",
    "is", "it", "who", "what", "where", "why", "how", "tell", "me", "about",
    "did", "do", "does", "are", "was", "were", "used", "use", "wear", "worn",
    "meaning", "role", "which", "when", "if", "one", "or", "both", "pass", "away",
    "yoruba", "tradition", "traditional", "culture", "cultural", "people", "vs"
}

# Compound-word root prefixes for joined-word typo splitting (e.g., "agbadaembroidered")
COMPOUND_ROOT_PREFIXES: List[str] = [
    "agbada", "adire", "gelede", "sango", "oriki", "omoluwabi", "dundun", "egungun",
    "obatala", "orunmila", "olodumare", "kabiyesi", "babalawo"
]

# Diaspora phonetic spelling normalizations
DIASPORA_PHONETIC_MAP: Dict[str, str] = {
    "omoluabi": "omoluwabi",
    "omolwabi": "omoluwabi",
    "eegun": "egungun",
    "shango": "sango",
    "oshun": "osun",
    "esu elegbara": "esu",
    "elegba": "esu",
    "ifaa": "ifa",
    "bataa": "bata",
    "kakanfo": "kakanfo",
    "kakañfo": "kakanfo"
}

# Zero-latency English-to-Yorùbá Semantic Bridge (RC-3 Upgrade 3)
ENGLISH_TO_YORUBA_SEMANTIC_BRIDGE: Dict[str, List[str]] = {
    "warriors": ["aabo-ogun", "balogun", "eso ikoyi", "ogun", "akinkanju", "jagunjagun"],
    "warrior": ["aabo-ogun", "balogun", "eso ikoyi", "ogun", "akinkanju"],
    "protection": ["aabo-ogun", "igbadi", "onde", "agbo", "aabo"],
    "battle": ["aabo-ogun", "ogun kiriji", "ogun osogbo", "ogun", "balogun"],
    "elders": ["idajo ogboni", "osugbo", "ogboni", "agba", "egbe"],
    "disputes": ["idajo ogboni", "osugbo", "ogboni", "ale"],
    "carved": ["opo ogoga", "koba palace gate", "olowe of ise", "opon ifa", "ere ibeji"],
    "palace": ["koba palace gate", "opo ogoga", "aafin", "oba"],
    "doors": ["koba palace gate", "opo ogoga", "ilekun"],
    "ekiti": ["opo ogoga", "koba palace gate", "ekiti-parapo", "ogun kiriji", "ipinle ekiti"],
    "herbs": ["ewe", "agbo", "osanyin", "omi-ero"],
    "postpartum": ["ewe", "agbo", "abiyamo", "omi-ero"],
    "care": ["ewe", "agbo", "iwosan"],
    "crown": ["ade", "ade aare", "orikogbofo", "adenla"],
    "beaded": ["ade", "ade aare", "ewu ileke", "bata ileke", "ileke"],
    "veil": ["ade", "ade aare", "iboju"],
    "kings": ["oba", "ade", "kabiyesi", "ooni", "alaafin"],
    "talking": ["dundun", "gangan", "iya ilu"],
    "drums": ["dundun", "bata", "gangan", "omele", "gudugudu"],
    "drum": ["dundun", "bata", "gangan", "omele"],
    "tones": ["dundun", "ami ohun", "gangan"],
    "brass": ["oruka ogboni", "edan ogboni", "ogboni"],
    "ogboni": ["oruka ogboni", "edan ogboni", "idajo ogboni", "osugbo"],
    "textile": ["adire", "adire-eleko-osi", "aso oke", "aso"],
    "indigo": ["adire", "adire-eleko-osi", "aro", "elu"],
    "dyed": ["adire", "adire-eleko-osi", "aro"],
    "divination": ["opon ifa", "ifa", "odu ifa", "iroke ifa", "ikin ifa", "opele"],
    "tray": ["opon ifa"],
    "patience": ["iwa", "suuru", "irete meji", "omoluwabi"],
    "character": ["iwa", "omoluwabi", "iwa pele", "suuru"],
    "twins": ["ere ibeji", "ibeji", "taiwo", "kehinde"],
    "twin": ["ere ibeji", "ibeji"],
    "statue": ["ere ibeji", "ere"],
    "honored": ["ere ibeji", "oriki"],
    "soup": ["abula", "obe", "gbegiri", "ewedu", "egusi"],
    "amala": ["abula", "amala", "amala isu", "elubo", "gbegiri"],
    "thunder": ["ose sango", "sango", "edun ara"],
    "staff": ["ose sango", "opa orere", "opa osanyin", "iroke ifa"],
    "mask": ["gelede", "gelede-mask", "egungun", "epa"],
    "woven": ["aso oke", "aso", "ofii"],
    "praise": ["oriki", "rara", "ewi", "ijala"],
    "poetry": ["oriki", "ewi", "rara", "ijala"],
    "proverbs": ["owe", "oriki"],
    "robe": ["agbada", "ewu ileke", "gbariye", "dansiki"],
    "embroidered": ["agbada", "buba", "fila"],
    "swallow": ["amala", "okele", "iyan", "eba", "fufu"],
    "shoes": ["bata ileke"],
    "river": ["odo osun", "odo ogun", "odo oya", "osun"],
    "generalissimo": ["aare ona kakanfo", "balogun"],
    "kakanfo": ["aare ona kakanfo"],
    "kiriji": ["ogun kiriji", "ekiti-parapo"],
    "fulani": ["ogun osogbo", "ilorin"]
}

def preprocess_query_tokens(raw_query: str) -> tuple:
    """
    Clean natural-language query, split compound prefix typos, normalize diaspora spellings,
    and extract core subject + expanded semantic bridge targets.
    """
    q_cleaned = re.sub(r"[?!.,;:']", " ", str(raw_query)).replace('"', " ").replace("_", " ").replace("-", " ").strip()
    q_cleaned = re.sub(r"\s+", " ", q_cleaned)

    # Split compound prefix typos like "agbadaembroidered" -> "agbada embroidered"
    # Negative lookahead protects genuine lexical roots like "agbadagba" (venerable elder records)
    for prefix in COMPOUND_ROOT_PREFIXES:
        pattern = re.compile(rf"\b({prefix})(?!gba\b)([a-z]{{4,}})\b", re.IGNORECASE)
        q_cleaned = pattern.sub(r"\1 \2", q_cleaned)

    # Normalize diaspora spellings on accent-stripped copy
    core_subject = re.sub(
        r"^(who is|what is|tell me about|explain|who was|what was|meaning of|history of|where is|why is|how do|how are|what did|which yoruba|what does)\s+",
        "",
        q_cleaned,
        flags=re.IGNORECASE,
    ).strip()

    norm_query = normalize_y(q_cleaned)
    stripped_query = strip_accents(q_cleaned).strip()

    norm_core = normalize_y(core_subject)
    stripped_core = strip_accents(core_subject).strip()

    for dia_src, dia_dst in DIASPORA_PHONETIC_MAP.items():
        stripped_query = re.sub(rf"\b{re.escape(dia_src)}\b", dia_dst, stripped_query)
        stripped_core = re.sub(rf"\b{re.escape(dia_src)}\b", dia_dst, stripped_core)

    q_words = [
        w for w in re.findall(r"\b\w+\b", stripped_query)
        if len(w) > 1 and w not in INQUIRY_STOP_WORDS
    ]

    # Collect semantic bridge target concepts triggered by query tokens
    bridge_targets: List[str] = []
    for w in q_words:
        if w in ENGLISH_TO_YORUBA_SEMANTIC_BRIDGE:
            bridge_targets.extend(ENGLISH_TO_YORUBA_SEMANTIC_BRIDGE[w])

    return q_cleaned, norm_query, stripped_query, norm_core, stripped_core, q_words, bridge_targets
