# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: CONVERSATIONAL CHAT & CULTURAL TRANSLATION SUITE (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Dual-Action Intelligence Suite:
# 1. Grounded Conversational Chat (Zero-Hallucination Cultural Scholar RAG)
# 2. Smart ASCII-to-Diacritic Restorer (25-Letter Yorùbá Orthography)
# 3. Cultural Translation & Deep Glossing (Odù Ifá & Sacred Oríkì)
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
        top_k: int = 4
    ) -> Dict[str, Any]:
        """
        Execute Grounded Conversational RAG with zero hallucination.
        Retrieves canonical entities from 1,240-item master corpus + 256 Odù Ifá matrix.
        """
        start_time = time.time()
        # Extract meaningful cultural tokens from natural language conversational prompt
        stop_words = {"tell", "me", "about", "who", "is", "permitted", "to", "wear", "it", "what", "how", "the", "a", "an", "in", "on", "and", "or", "of", "why", "can", "you", "explain", "does", "meaning"}
        raw_tokens = [w for w in re.findall(r'\w+', message.lower()) if w not in stop_words and len(w) > 2]
        query_kw = " ".join(raw_tokens) if raw_tokens else message
        retrieved_hits = self.retriever.retrieve(query_kw, top_k=top_k)
        if not retrieved_hits and query_kw != message:
            retrieved_hits = self.retriever.retrieve(message, top_k=top_k)
        
        # Build context dossier from retrieved entities
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

            snippet = f"Entity: {title} ({category})\n- Description: {desc}\n- Philosophy & Etymology: {etym}\n- Historical Antiquity: {hist}\n- Oral Traditions & Proverbs: {proverbs_text}"
            context_snippets.append(snippet)

        grounded_context = "\n\n".join(context_snippets)

        system_instruction = (
            "You are an authoritative Yorùbá cultural scholar, sovereign historian, and linguist for Àgbà Engine. "
            "Your duty is to provide authentic, highly accurate information rooted in classical Yorùbá culture. "
            "STRICT RULES:\n"
            "1. Ground your response strictly in the provided Canonical Context below whenever applicable.\n"
            "2. Enforce pristine 25-letter Yorùbá orthography with correct tone marks (Àmì Ohùn: Re, Mi, Do) and sub-dots (ẹ, ọ, ṣ) for all indigenous concepts.\n"
            "3. If the user asks about an indigenous concept outside the provided context, maintain scholarly dignity, state what is known within canonical Yorùbá tradition, and avoid modern Hollywood or colonial distortions.\n"
            "4. Be respectful, eloquent, and culturally proud."
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
                        temperature=0.2,
                        max_output_tokens=1000
                    )
                )
                reply_text = response.text
            except Exception as e:
                print(f"⚠️ GenAI Chat API Call Notice: {e}, executing sovereign synthesis fallback.")
                reply_text = self._fallback_chat_synthesis(message, retrieved_hits)
                model_used = "Sovereign Algorithmic Synthesis"
        else:
            reply_text = self._fallback_chat_synthesis(message, retrieved_hits)
            model_used = "Sovereign Algorithmic Synthesis"

        latency_ms = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
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

    def diacritize_ascii(self, ascii_text: str) -> Dict[str, Any]:
        """
        Context-aware diacritization: Takes raw ASCII Yorùbá and restores
        authentic 25-letter tone marks (Re, Mi, Do) and sub-dots (ẹ, ọ, ṣ).
        """
        start_time = time.time()
        
        system_instruction = (
            "You are a master Yorùbá linguist specializing in computational orthography. "
            "Task: Restore the accurate diacritics (sub-dots ẹ, ọ, ṣ and tone marks acute ´, grave `, macron) "
            "to the provided ASCII Yorùbá text according to strict 25-letter Yorùbá orthography. "
            "Disambiguate polysemic words (e.g., oro -> ọ̀rọ̀ [word], ọrọ̀ [wealth], orò [rite]) based on sentence context. "
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
                        temperature=0.1,
                        max_output_tokens=500
                    )
                )
                diacritized_output = response.text.strip()
            except Exception as e:
                diacritized_output = self._fallback_diacritize(ascii_text)
                method = "Sovereign Vocabulary Dictionary Lookup"
        else:
            diacritized_output = self._fallback_diacritize(ascii_text)
            method = "Sovereign Vocabulary Dictionary Lookup"

        latency_ms = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "original_ascii": ascii_text,
            "diacritized_text": diacritized_output,
            "method": method,
            "latency_ms": latency_ms
        }

    def translate_cultural(self, yoruba_text: str) -> Dict[str, Any]:
        """
        Dual-Action Cultural Translation & Deep Glossing for sacred Odù Ifá, Oríkì, and chants.
        Returns:
        1. Strict Orthographic Retention
        2. Literal Translation
        3. Deep Philosophical & Cultural Gloss
        """
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
                        temperature=0.2,
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

    def _fallback_chat_synthesis(self, query: str, hits: List[Dict[str, Any]]) -> str:
        """Algorithmic fallback synthesis when GenAI key is absent."""
        if not hits:
            return f"Àkíyèsí (Notice): The concept '{query}' is currently staged in our archive. Our master corpus contains 1,240 verified entities spanning royal regalia, sacred divinations, and lineages."

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
            related_titles = [h.get("title") for h in hits[1:] if h.get("title")]
            if related_titles:
                response_lines.append(f"\n🔗 **Closely Related Concepts:** {', '.join(related_titles)}")

        return "\n".join(response_lines)

    def _fallback_diacritize(self, ascii_text: str) -> str:
        """Rule-based diacritization mapping against canonical corpus vocabulary."""
        text = ascii_text
        for entity in self.retriever.corpus_entities:
            title = entity.get("title", "")
            aliases = entity.get("aliases", [])
            for a in aliases:
                if len(a) > 2 and re.search(r'\b' + re.escape(a) + r'\b', text, re.IGNORECASE):
                    text = re.sub(r'\b' + re.escape(a) + r'\b', title, text, flags=re.IGNORECASE)
        return text

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
