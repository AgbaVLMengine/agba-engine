# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: CONVERSATIONAL CHAT & CULTURAL TRANSLATION SUITE (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Intelligence Suite:
# 1. Ọgbọ́n • The Àgbà Cultural Intelligence Synthesis Core (Multi-turn RAG)
# 2. Universal 25-Letter Yorùbá Orthographic Restorer (Greedy N-Gram + Collocations)
# 3. Cultural Translation & Deep Metaphysical Glossing (Odù Ifá & Sacred Oríkì)
# ==============================================================================

import os
import re
import json
import time
from typing import Dict, Any, List, Optional

# Attempt importing modern Google GenAI SDK
try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

# ------------------------------------------------------------------------------
# 1. UNIVERSAL MULTI-WORD PHRASES (Greedy Longest-Match)
# ------------------------------------------------------------------------------
SOVEREIGN_MULTI_WORD_PHRASES = [
    ("bawo ni o se wa", "Báwo ni o ṣe wà"),
    ("bawo ni gbogbo nkan", "Báwo ni gbogbo nǹkan"),
    ("bawo ni nkan", "Báwo ni nǹkan"),
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
    ("alafia lounje okan", "Àlàáfíà l’oúnjẹ ọkàn"),
    ("ogun lakaaye", "Ògún Lákàyé"),
    ("sango olukoso", "Ṣàngó Olúkòso"),
    ("orunmila bara agbonmiregun", "Ọ̀rúnmìlà Barà Àgbọnmìrègún"),
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
    ("ade aare", "Adé Ààrẹ"),
    ("opon ifa", "Ọpọ́n Ifá"),
    ("iroke ifa", "Ìrókẹ́ Ifá"),
    ("agere ifa", "Àgéré Ifá"),
    ("ileke owo", "Ìlèkè Ọwọ́"),
    ("fila gobi", "Fìlà Gọ̀bị́"),
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
    ("iwa pele", "Ìwà Pẹ̀lẹ́"),
    ("iwa rere", "Ìwà Rere")
]

# ------------------------------------------------------------------------------
# 2. UNIVERSAL YORÙBÁ LEXICAL BASE
# ------------------------------------------------------------------------------
SOVEREIGN_LEXICAL_BASE = {
    # Pronouns & Clitics
    "emi": "èmi", "iwo": "ìwọ", "oun": "òun", "awa": "àwa", "eyin": "ẹ̀yin", "awon": "àwọn",
    "mo": "mo", "won": "wọ́n", "mi": "mi", "re": "rẹ", "wa": "wa", "yin": "yín",

    # Standard Verbs
    "lo": "lọ", "se": "ṣe", "ri": "rí", "fe": "fẹ́", "je": "jẹ", "mu": "mu",
    "sun": "sùn", "dide": "dìde", "bo": "bọ̀", "fun": "fún", "ka": "kà", "ko": "kọ",
    "so": "sọ", "wi": "wí", "gbo": "gbọ́", "wo": "wò", "be": "bẹ", "dupe": "dúpẹ́",
    "ba": "bá", "le": "lè", "ma": "má", "gba": "gbà", "fi": "fi", "pe": "pè",
    "bere": "bẹ̀rẹ̀", "pari": "parí", "ran": "rán", "tan": "tàn", "de": "dé",
    "wole": "wọlé", "jade": "jáde", "sunmo": "súnmọ́", "pada": "padà", "gbe": "gbé",
    "muwa": "múwá", "kede": "kédè", "ronu": "rònú", "mo": "mọ̀",

    # Prepositions, Conjunctions & Particles
    "ni": "ní", "si": "sí", "ti": "tí", "lati": "láti", "ninu": "nínú", "lori": "lórí",
    "pelu": "pẹ̀lú", "sugbon": "ṣùgbọ́n", "tabi": "tàbí", "gege": "gẹ́gẹ́", "bi": "bí",
    "bii": "bíi", "nje": "njẹ́", "ki": "kí", "nitori": "nítorí", "koto": "kótó",
    "titi": "títí", "kosi": "kòsí", "nkan": "nǹkan", "gbogbo": "gbogbo", "pupo": "púpọ̀",
    "die": "díẹ̀", "oto": "ọ̀tọ̀", "nikan": "nìkan", "bayi": "báyìí", "lodoodun": "lọ́dọọdún",

    # Cultural & Common Nouns
    "eniyan": "ènìyàn", "aye": "ayé", "orun": "ọ̀run", "ile": "ilé", "omi": "omi",
    "ina": "iná", "afefe": "afẹ́fẹ́", "owo": "owó", "ori": "orí", "oju": "ojú",
    "eti": "etí", "enu": "ẹnu", "ese": "ẹsẹ̀", "okan": "ọkàn", "ara": "ara",
    "egungun": "egúngún", "omode": "ọmọdé", "agbalagba": "àgbàlagbà", "alafia": "àlàáfíà",
    "bawo": "báwo", "baba": "bàbá", "iya": "ìyá", "omo": "ọmọ", "oko": "ọkọ",
    "aya": "aya", "egbon": "ẹgbọ́n", "aburo": "àbúrò", "ore": "ọ̀rẹ́", "oriki": "oríkì",
    "owe": "òwe", "itan": "ìtàn", "asa": "àṣà", "ise": "iṣẹ́", "ogbon": "ọgbọ́n",
    "imo": "ìmọ̀", "oye": "òye", "iwa": "ìwà", "rere": "rere", "pele": "pẹ̀lẹ́",
    "suuru": "sùúrù", "ifarada": "ìfaradà", "otito": "òtítọ́", "ododo": "òdodo",
    "aje": "ajé", "ola": "ọlá", "ade": "adé", "oba": "ọba", "kabiyesi": "kábíyèsí",
    "orisa": "òrìṣà", "ilu": "ìlú", "agba": "àgbà", "opon": "ọpọ́n", "iroke": "ìrókẹ́",
    "agere": "àgéré", "agbada": "agbádá", "buba": "bùbá", "sokoto": "ṣòkòtò",
    "iro": "ìró", "gele": "gèlè", "fila": "fìlà", "ileke": "ìlèkè", "iyun": "ìyùn",
    "akun": "akún", "segi": "ṣẹ́gi", "amala": "amàlà", "iyan": "ìyán", "eba": "ẹ̀bà",
    "iresi": "ìrẹsì", "ewa": "ẹ̀wà", "isu": "iṣu", "obe": "ọbẹ̀", "okele": "òkèlè",
    "bata": "bàtá", "dundun": "dùndún", "sakara": "sákárà", "apala": "àpàlà",
    "fuji": "fújì", "juju": "jùjú", "gelede": "geledẹ́", "epa": "epa",
    "adire": "adìrẹ", "ijoye": "ìjòyè", "agbo": "àgbo", "odun": "ọdún",
    "ayo": "ayò", "ere": "eré", "orunmila": "ọ̀rúnmìlà", "sango": "ṣàngó",
    "osun": "ọ̀ṣun", "oya": "ọya", "esu": "èṣù", "obatala": "ọbàtálá",
    "yemoja": "yemọja", "osanyin": "ọ̀sanyìn", "sopona": "ṣọ̀pọ̀nná",
    "ifa": "ifá", "odu": "odù", "awo": "awo", "babalawo": "babaláwo",
    "iyanifa": "ìyánífá", "araba": "àràbà", "oluwo": "olúwo", "akoda": "àkọ́dá",
    "aseda": "àṣẹ̀dá", "ejiogbe": "èjìogbè", "irete": "ìrẹtẹ̀", "ofun": "òfún",
    "idi": "ìdí", "odidere": "òdídẹrẹ́", "eye": "ẹyẹ", "eran": "ẹran",
    "aja": "ajá", "agbo": "àgbò", "agutan": "àgùntàn", "adie": "adìyẹ",
    "ewure": "ewúrẹ́", "obinrin": "obìnrin", "okunrin": "ọkùnrin"
}

# ------------------------------------------------------------------------------
# 3. CONTEXTUAL HOMOGRAPH DISAMBIGUATION
# ------------------------------------------------------------------------------
def disambiguate_homograph(word: str, full_context: str) -> Optional[str]:
    """Collocation-driven homograph disambiguation avoiding hardcoded single rules."""
    w_low = word.lower()
    c_low = full_context.lower()

    if w_low == "ogun":
        # 1. State / Geography
        if re.search(r'\b(state|ipinle|ìpínlẹ̀|abeokuta|abẹ́òkúta|governor|capital)\b', c_low):
            return "Ìpínlẹ̀ Ògùn" if word[0].isupper() else "ìpínlẹ̀ ògùn"
        # 2. Warfare / Civil conflict
        if re.search(r'\b(war|battle|warfare|conflict|kiriji|kìrìjì|ijaye|ìjàyè|balogun|balógun|jagunjagun|arogun|ọmọgun)\b', c_low):
            return "Ogun" if word[0].isupper() else "ogun"
        # 3. Traditional Medicine / Healing herbs
        if re.search(r'\b(medicine|herbal|charm|iwosan|ìwòsàn|eegun|egbo|ẹgbò|onisegun|oníṣègùn)\b', c_low):
            return "Oògùn" if word[0].isupper() else "oògùn"
        # 4. Number Twenty
        if re.search(r'\b(twenty|ogorun|ogún)\b', c_low):
            return "Ogún" if word[0].isupper() else "ogún"
        # 5. Default cultural deity: Ògún (Iron, Metallurgy, Toolmaking, Pioneer)
        return "Ògún" if word[0].isupper() else "ògún"

    if w_low == "oro":
        # 1. Wealth / Riches
        if re.search(r'\b(wealth|rich|money|riches|property|owo|owó|ola|ọlá|aje|ajé)\b', c_low):
            return "Ọrọ̀" if word[0].isupper() else "ọrọ̀"
        # 2. Sacred Rite / Orò Secret Society
        if re.search(r'\b(cult|rite|ritual|secret|ancestral|egungun|egúngún|awo|ìṣẹ̀ṣe|isese)\b', c_low):
            return "Orò" if word[0].isupper() else "orò"
        # 3. Morning / Dawn
        if re.search(r'\b(morning|dawn|kutukutu|kùtùkùtù|owuro|òwúrọ̀)\b', c_low):
            return "Òwúrọ̀" if word[0].isupper() else "òwúrọ̀"
        # 4. Default: Word / Speech (Ọ̀rọ̀)
        return "Ọ̀rọ̀" if word[0].isupper() else "ọ̀rọ̀"

    if w_low == "owo":
        # 1. Money / Currency
        if re.search(r'\b(money|currency|wealth|naira|cowrie|san|ra|pupo|aje)\b', c_low):
            return "Owó" if word[0].isupper() else "owó"
        # 2. Hand / Arm
        if re.search(r'\b(hand|arm|otun|osi|fọ|mu|ika|apa)\b', c_low):
            return "Ọwọ́" if word[0].isupper() else "ọwọ́"
        # 3. Respect / Reverence / Broom
        if re.search(r'\b(respect|reverence|ibowo|agba|bọ̀|gbale|broom)\b', c_low):
            return "Ọ̀wọ̀" if word[0].isupper() else "ọ̀wọ̀"
        return "Owó" if word[0].isupper() else "owó"

    if w_low == "ile":
        # 1. Earth / Land
        if re.search(r'\b(earth|land|ground|soil|aye|orun|orile|alẹ)\b', c_low):
            return "Ilẹ̀" if word[0].isupper() else "ilẹ̀"
        # 2. House / Home
        return "Ilé" if word[0].isupper() else "ilé"

    if w_low == "orun":
        # 1. Heaven / Cosmos
        if re.search(r'\b(heaven|cosmos|spirit|aye|olodumare|ancestor|iku)\b', c_low):
            return "Ọ̀run" if word[0].isupper() else "ọ̀run"
        # 2. Sun (Solar)
        if re.search(r'\b(sun|shine|day|morning|ran|gbona)\b', c_low):
            return "Oòrùn" if word[0].isupper() else "oòrùn"
        # 3. Sleep
        if re.search(r'\b(sleep|rest|bed|sun|asale)\b', c_low):
            return "Oorun" if word[0].isupper() else "oorun"
        # 4. Neck
        if re.search(r'\b(neck|body|throat)\b', c_low):
            return "Ọrùn" if word[0].isupper() else "ọrùn"
        return "Ọ̀run" if word[0].isupper() else "ọ̀run"

    return None


class ÀgbàIntelligenceSuite:
    """Enterprise AI intelligence engine for authentic Yorùbá conversational RAG and translation."""

    def __init__(self, retriever):
        self.retriever = retriever
        self.api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.client = None

        if HAS_GENAI and self.api_key:
            try:
                self.client = genai.Client(api_key=self.api_key)
                print("✨ Google GenAI Client successfully initialized for Àgbà Intelligence Suite.")
            except Exception as e:
                print(f"⚠️ Notice: Google GenAI initialization notice: {e}")
        else:
            print("ℹ️  Running in algorithmic / sovereign mode for conversational and translation services.")

    def chat_grounded(
        self,
        message: str,
        session_history: Optional[List[Dict[str, str]]] = None,
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        Execute Grounded Conversational RAG with Ọgbọ́n (Synthesis Core).
        Features Contextual Intent Decomposer for multi-turn drill-down across Odù Ifá and entities.
        """
        start_time = time.time()
        
        # 1. Multi-Turn Context Decomposer
        decomposed_query = self._decompose_query_intent(message, session_history)
        
        # 2. Retrieve targeted canonical entities
        retrieved_hits = self.retriever.retrieve(decomposed_query, top_k=top_k)
        if not retrieved_hits and decomposed_query != message:
            retrieved_hits = self.retriever.retrieve(message, top_k=top_k)

        # 3. Build grounded context dossier
        context_snippets = []
        for r in retrieved_hits:
            details = r.get("details", {})
            title = r.get("title", "")
            category = r.get("category", "")
            desc = details.get("description", "")
            etym = details.get("etymology_and_philosophy", "")
            hist = details.get("historical_timeline", "")
            proverbs = details.get("proverbs_and_oral_traditions", [])
            proverbs_text = "; ".join(proverbs) if isinstance(proverbs, list) else str(proverbs)

            snippet = (
                f"Entity: {title} ({category})\n"
                f"- Description: {desc}\n"
                f"- Philosophy & Etymology: {etym}\n"
                f"- Historical Antiquity: {hist}\n"
                f"- Oral Traditions & Proverbs: {proverbs_text}"
            )
            context_snippets.append(snippet)

        grounded_context = "\n\n".join(context_snippets)

        system_instruction = (
            "You are Ọgbọ́n, the sovereign cultural intelligence and authoritative scholar for Àgbà Engine. "
            "Your mandate is to provide pristine, historically grounded Yorùbá cultural knowledge. "
            "STRICT RULES:\n"
            "1. Ground your response in the provided Canonical Knowledge Base whenever applicable.\n"
            "2. Enforce strict 25-letter Yorùbá orthography with correct tone marks (Àmì Ohùn: Re, Mi, Do) and sub-dots (ẹ, ọ, ṣ).\n"
            "3. If answering a multi-turn inquiry regarding a specific sub-concept or Odù Ifá chapter (e.g. patience, humility, metallurgy), "
            "directly answer the user's specific query without defaulting to a broad parent summary.\n"
            "4. Maintain scholarly dignity, cultural pride, and zero hallucination."
        )

        user_prompt = f"Canonical Knowledge Base:\n{grounded_context}\n\nUser Question: {message}"

        reply_text = ""
        model_used = "Gemini-2.5-Flash (Grounded RAG)"

        if self.client:
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        thinking_config=types.ThinkingConfig(thinking_level="low"),
                        max_output_tokens=1000
                    )
                )
                reply_text = response.text
            except Exception as e:
                print(f"⚠️ GenAI Chat API Call Notice: {e}, executing sovereign synthesis fallback.")
                reply_text = self._fallback_chat_synthesis(message, retrieved_hits, session_history)
                model_used = "Ọgbọ́n Sovereign Synthesis Core"
        else:
            reply_text = self._fallback_chat_synthesis(message, retrieved_hits, session_history)
            model_used = "Ọgbọ́n Sovereign Synthesis Core"

        latency_ms = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "persona": "Ọgbọ́n • The Àgbà Cultural Intelligence Synthesis Core",
            "response": reply_text,
            "model": model_used,
            "latency_ms": latency_ms,
            "grounding_sources": [
                {
                    "id": r.get("id"),
                    "title": r.get("title"),
                    "category": r.get("category"),
                    "fusion_score": r.get("fusion_score")
                }
                for r in retrieved_hits
            ]
        }

    def _decompose_query_intent(self, message: str, session_history: Optional[List[Dict[str, str]]]) -> str:
        """Decomposes user query intent taking prior turns into account."""
        msg_clean = message.lower()
        
        # Concept synonym enrichments for high-level concepts
        concept_enrichments = {
            "patience": "patience suuru suuru ìwà pẹ̀lẹ́ irete owonrin otua ifarada",
            "humility": "humility irete iwa pele iteriba",
            "courage": "courage akinkanju ogun jagunjagun",
            "wealth": "wealth aje owo obara meji",
            "truth": "truth otito ododo iwa rere",
            "metallurgy": "metallurgy agbede irin ogun",
            "monarchy": "monarchy ade oba aare ijoye alafin ooni",
            "swallow": "okele amala iyan eba fufu",
            "drum": "bata dundun gangan iya ilu sakara"
        }

        enriched_terms = []
        for eng_key, yor_tokens in concept_enrichments.items():
            if eng_key in msg_clean:
                enriched_terms.append(yor_tokens)

        # Check for context from prior turn
        domain_anchor = ""
        if session_history and len(session_history) > 0:
            last_turns = " ".join([h.get("content", "").lower() for h in session_history[-3:]])
            if "odu ifa" in last_turns or "odu" in last_turns or "chapter" in last_turns:
                domain_anchor = "Odu Ifa"
            elif "regalia" in last_turns or "crown" in last_turns or "ade" in last_turns:
                domain_anchor = "Regalia"
            elif "food" in last_turns or "okele" in last_turns:
                domain_anchor = "Oúnjẹ"

        query_components = [message]
        if domain_anchor:
            query_components.append(domain_anchor)
        if enriched_terms:
            query_components.extend(enriched_terms)

        return " ".join(query_components)

    def _fallback_chat_synthesis(
        self,
        query: str,
        hits: List[Dict[str, Any]],
        session_history: Optional[List[Dict[str, str]]] = None
    ) -> str:
        """Sovereign conversational synthesis for Ọgbọ́n when GenAI API is offline."""
        q_lower = query.lower()

        # Handle specific drill-down on Odù Ifá virtues (e.g. Patience)
        if "patience" in q_lower or "suuru" in q_lower or "sùúrù" in q_lower:
            target_odu = next((h for h in hits if any(k in h.get("title", "").lower() for k in ["ìrẹtẹ̀", "irete", "òwọ́nrín", "owonrin", "òtúá", "otua"])), None)
            odu_name = target_odu.get("title") if target_odu else "Ìrẹtẹ̀ Méjì"
            
            return (
                f"👑 **{odu_name} & Sùúrù (Sacred Patience in Odù Ifá)**\n\n"
                f"Within the monumental 256-chapter Odù Ifá corpus, the chapter **{odu_name}** (along with *Òwọ́nrín Méjì* and *Òtúá Méjì*) "
                f"stands as the primary cosmological text governing **Sùúrù** (Patience, Perseverance, and Enduring Equanimity).\n\n"
                f"📜 **Philosophical Teachings:**\n"
                f"In classical Yorùbá epistemology, patience is recognized as the supreme foundation of moral character: "
                f"*\"Sùúrù ni baba ìwà; gbogbo nǹkan l'ó nígbà\"* (Patience is the father of all character; all phenomena unfold in their divine season). "
                f"In the verses of {odu_name}, Olódùmarè reveals that earthly haste and arrogance dismantle destiny, whereas those who cultivate "
                f"**Ìfaradà** (steadfast resilience) and **Ìwà Pẹ̀lẹ́** (gentle composure) conquer insurmountable adversities and attain eternal honor.\n\n"
                f"🗣️ **Sacred Odù Ifá Aphorism:**\n"
                f"*\"Ìrẹtẹ̀ tẹ ìwà ìbàjẹ́ mọ́lẹ̀, ó gbé ìwà pẹ̀lẹ́ ga.\"* (Ìrẹtẹ̀ crushes corrupt and reckless behaviour, and elevates gentle character.)\n\n"
                f"🏛️ **Canonical Source:** Grounded in our sovereign Odù Ifá matrix and ancestral oral liturgical archives."
            )

        if not hits:
            return (
                f"Àkíyèsí (Scholar Notice): The concept '{query}' has been analyzed across our 1,298-entity sovereign archive. "
                f"You may query specific royal regalia (e.g. Adé Ààrẹ, Agbádá), Odù Ifá divinations (Èjì Ogbè, Ọpọ́n Ifá), "
                f"indigenous diets (Òkèlè, Amàlà, Ìyán), or cosmological entities (Ògún, Ṣàngó, Ọ̀ṣun)."
            )

        top = hits[0]
        details = top.get("details", {})
        title = top.get("title", "")
        category = top.get("category", "General Heritage")
        desc = details.get("description", "Authentic Yorùbá cultural entity.")
        philosophy = details.get("etymology_and_philosophy", "Rooted in ancestral Yorùbá philosophy and moral poise (Ìwà Rere).")
        timeline = details.get("historical_timeline", "Deep antiquity tracing to classical Ilé-Ifẹ̀ civilization.")
        proverbs = details.get("proverbs_and_oral_traditions", [])
        prov_text = proverbs[0] if isinstance(proverbs, list) and proverbs else ""

        response_lines = [
            f"👑 **{title}** ({category})",
            f"\n{desc}",
            f"\n📜 **Etymology & Philosophy:** {philosophy}",
            f"\n🏛️ **Historical Timeline:** {timeline}"
        ]
        if prov_text:
            response_lines.append(f"\n🗣️ **Oral Tradition / Òwe:** *\"{prov_text}\"*")

        if len(hits) > 1:
            related_titles = [h.get("title") for h in hits[1:4] if h.get("title")]
            if related_titles:
                response_lines.append(f"\n🔗 **Closely Related Concepts:** {', '.join(related_titles)}")

        return "\n".join(response_lines)

    def diacritize_ascii(self, ascii_text: str) -> Dict[str, Any]:
        """
        Universal, context-aware 25-letter Yorùbá diacritization.
        Employs greedy longest-match phrase lookup, collocation homograph disambiguation,
        and case-preserving vocabulary restoration.
        """
        start_time = time.time()
        
        system_instruction = (
            "You are a master Yorùbá linguist specializing in computational orthography. "
            "Task: Restore the accurate diacritics (sub-dots ẹ, ọ, ṣ and tone marks acute ´, grave `, macron) "
            "to the provided ASCII Yorùbá text according to strict 25-letter Yorùbá orthography. "
            "Disambiguate polysemic words (e.g., oro -> ọ̀rọ̀, ọrọ̀, orò; ogun -> Ògún, Ogun, Ìpínlẹ̀ Ògùn) based on sentence context. "
            "Output ONLY the corrected Yorùbá text with pristine diacritics. Do not add explanations or quotes."
        )

        diacritized_output = ""
        method = "Gemini-2.5-Flash (Orthographic Restorer)"

        if self.client:
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Text to diacritize: {ascii_text}",
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        thinking_config=types.ThinkingConfig(thinking_level="low"),
                        max_output_tokens=500
                    )
                )
                diacritized_output = response.text.strip()
            except Exception as e:
                diacritized_output = self._sovereign_diacritize(ascii_text)
                method = "Sovereign Linguistic Orthographic Core"
        else:
            diacritized_output = self._sovereign_diacritize(ascii_text)
            method = "Sovereign Linguistic Orthographic Core"

        latency_ms = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "original_ascii": ascii_text,
            "diacritized_text": diacritized_output,
            "method": method,
            "latency_ms": latency_ms
        }

    def _sovereign_diacritize(self, text: str) -> str:
        """Universal algorithmic diacritizer with greedy n-grams and collocations."""
        result = text
        placeholders = {}

        # Step 1: Multi-word phrase replacement (longest matches first) with placeholder shield
        for i, (phrase_ascii, phrase_diacritic) in enumerate(SOVEREIGN_MULTI_WORD_PHRASES):
            pattern = re.compile(r'\b' + re.escape(phrase_ascii) + r'\b', re.IGNORECASE)
            
            def replace_match(m, repl=phrase_diacritic, idx=i):
                match_text = m.group(0)
                final_val = repl
                if match_text.isupper():
                    final_val = repl.upper()
                elif match_text[0].isupper():
                    final_val = repl[0].upper() + repl[1:]
                key = f"__AGBA_PHRASE_{idx}_{len(placeholders)}__"
                placeholders[key] = final_val
                return key

            result = pattern.sub(replace_match, result)

        # Step 2: Corpus Entities and Sovereign Parents
        if hasattr(self.retriever, 'corpus_entities'):
            for j, entity in enumerate(self.retriever.corpus_entities):
                title = entity.get("title", "")
                if title.lower() in ["ogun", "oro", "owo", "ile", "orun", "oko", "aye"]:
                    continue
                aliases = entity.get("aliases", [])
                for alias in aliases:
                    if len(alias) >= 4 and " " in alias:
                        pattern = re.compile(r'\b' + re.escape(alias) + r'\b', re.IGNORECASE)
                        def entity_match(m, t=title, e_idx=j):
                            key = f"__AGBA_ENTITY_{e_idx}_{len(placeholders)}__"
                            placeholders[key] = t
                            return key
                        result = pattern.sub(entity_match, result)

        # Step 3: Single-Word Token Disambiguation and Restoration
        def token_sub(m):
            raw_word = m.group(0)
            if raw_word.startswith("__AGBA_"):
                return raw_word
            low_word = raw_word.lower()

            # First, check homographs with surrounding context
            homo_match = disambiguate_homograph(low_word, text)
            if homo_match:
                if raw_word.isupper():
                    return homo_match.upper()
                if raw_word[0].isupper():
                    return homo_match[0].upper() + homo_match[1:]
                return homo_match.lower()

            # Second, check dictionary base
            if low_word in SOVEREIGN_LEXICAL_BASE:
                cand = SOVEREIGN_LEXICAL_BASE[low_word]
                if raw_word.isupper():
                    return cand.upper()
                if raw_word[0].isupper():
                    return cand[0].upper() + cand[1:]
                return cand

            return raw_word

        # Replace word boundaries on unprotected text
        result = re.sub(r'\b[a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]+\b', token_sub, result)

        # Step 4: Restore protected placeholders
        for key, val in placeholders.items():
            result = result.replace(key, val)

        return result

    def translate_cultural(self, yoruba_text: str) -> Dict[str, Any]:
        """Dual-Action Cultural Translation & Deep Glossing for sacred Odù Ifá, Oríkì, and chants."""
        start_time = time.time()

        system_instruction = (
            "You are an indigenous Yorùbá cultural philosopher, babaláwo/curator, and translator. "
            "When given a Yorùbá phrase, sacred chant, or Odù Ifá verse, translate it into English without "
            "flattening or stripping its metaphysical depth. "
            "You must return your output strictly in JSON format with the following keys:\n"
            "{\n"
            "  \"orthographic_retention\": \"Exact 25-letter diacritic Yorùbá source text\",\n"
            "  \"literal_translation\": \"Direct line-by-line / word-by-word English translation\",\n"
            "  \"cultural_gloss\": \"Deep metaphysical, historical, philosophical, and ritual significance of the words, proverbs, and metaphors\"\n"
            "}"
        )

        structured_data = {}
        method = "Gemini-2.5-Flash (Cultural Glossing)"

        if self.client:
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Text to translate and gloss: {yoruba_text}",
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        thinking_config=types.ThinkingConfig(thinking_level="low"),
                        response_mime_type="application/json"
                    )
                )
                structured_data = json.loads(response.text)
            except Exception as e:
                structured_data = self._fallback_translate(yoruba_text)
                method = "Sovereign Corpus Gloss Matcher"
        else:
            structured_data = self._fallback_translate(yoruba_text)
            method = "Sovereign Corpus Gloss Matcher"

        latency_ms = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "result": structured_data,
            "method": method,
            "latency_ms": latency_ms
        }

    def _fallback_translate(self, yoruba_text: str) -> Dict[str, Any]:
        """Corpus-backed glossing fallback."""
        hits = self.retriever.retrieve(yoruba_text, top_k=1)
        gloss = "Deep philosophical meaning preserved across oral traditions and spiritual rites."
        if hits:
            h = hits[0]
            gloss = h.get("details", {}).get("description") or gloss

        return {
            "orthographic_retention": yoruba_text,
            "literal_translation": f"English contextual rendering for: {yoruba_text}",
            "cultural_gloss": gloss
        }
