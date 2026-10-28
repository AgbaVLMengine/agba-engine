# 🏛️ ÀGBÀ ENGINE: CONVERSATIONAL CHAT & CULTURAL TRANSLATION SUITE (v6.2.0)
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Coordinator Refactored: HANDOFF-AGBEDE-006 (Law 1: Coordinator < 210 LOC)

import os
import re
import json
import time
from typing import Dict, Any, List, Optional

try:
    from app.orthography_lexicon import (SOVEREIGN_MULTI_WORD_PHRASES, SOVEREIGN_LEXICAL_BASE, disambiguate_homograph, OGBON_PERSONA_RESPONSE, is_ogbon_persona_query)
    from app.prompt_governor import (OGBON_SYSTEM_INSTRUCTION, DIACRITIZER_SYSTEM_INSTRUCTION, CULTURAL_TRANSLATION_SYSTEM_INSTRUCTION, build_grounded_rag_prompt, decompose_query_intent, validate_grounding_citations, fallback_chat_synthesis, sanitize_xml_user_input)
except Exception:
    from orthography_lexicon import (SOVEREIGN_MULTI_WORD_PHRASES, SOVEREIGN_LEXICAL_BASE, disambiguate_homograph, OGBON_PERSONA_RESPONSE, is_ogbon_persona_query)
    from prompt_governor import (OGBON_SYSTEM_INSTRUCTION, DIACRITIZER_SYSTEM_INSTRUCTION, CULTURAL_TRANSLATION_SYSTEM_INSTRUCTION, build_grounded_rag_prompt, decompose_query_intent, validate_grounding_citations, fallback_chat_synthesis, sanitize_xml_user_input)

try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False


class ÀgbàIntelligenceSuite:
    """Enterprise AI intelligence coordinator for Yorùbá conversational RAG and translation."""

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
        top_k: int = 5,
    ) -> Dict[str, Any]:
        """Execute Grounded Conversational RAG with Ọgbọ́n (Synthesis Core)."""
        start_time = time.time()
        if is_ogbon_persona_query(message):
            return {
                "status": "success", "persona": "Ọgbọ́n • The Àgbà Cultural Intelligence Synthesis Core",
                "response": OGBON_PERSONA_RESPONSE, "model": "Ọgbọ́n Sovereign Metacognitive Core",
                "latency_ms": round((time.time() - start_time) * 1000, 2),
                "grounding_sources": [
                    {"id": "ORUNMILA-001", "title": "Ọ̀rúnmìlà", "category": "Spiritual & Cosmological Matrix", "fusion_score": 1.0},
                    {"id": "OGBON-TRIAD-001", "title": "Ọgbọ́n, Ìmọ̀ àti Òye", "category": "Indigenous Epistemology", "fusion_score": 0.95},
                ],
            }

        decomposed = decompose_query_intent(message, session_history)
        hits = self.retriever.retrieve(decomposed, top_k=top_k) or (self.retriever.retrieve(message, top_k=top_k) if decomposed != message else [])
        user_prompt = build_grounded_rag_prompt(hits, message)
        reply_text, model_used = "", "Gemini-2.5-Flash (Grounded RAG)"

        if self.client:
            try:
                cfg = types.GenerateContentConfig(system_instruction=OGBON_SYSTEM_INSTRUCTION, thinking_config=types.ThinkingConfig(thinking_level="low"), max_output_tokens=1000)
                resp = self.client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt, config=cfg)
                reply_text = resp.text
                validate_grounding_citations(reply_text, hits)
            except Exception as e:
                print(f"⚠️ GenAI Chat API Call Notice: {e}, executing sovereign synthesis fallback.")
                reply_text, model_used = fallback_chat_synthesis(message, hits, session_history), "Ọgbọ́n Sovereign Synthesis Core"
        else:
            reply_text, model_used = fallback_chat_synthesis(message, hits, session_history), "Ọgbọ́n Sovereign Synthesis Core"

        return {
            "status": "success", "persona": "Ọgbọ́n • The Àgbà Cultural Intelligence Synthesis Core",
            "response": reply_text, "model": model_used, "latency_ms": round((time.time() - start_time) * 1000, 2),
            "grounding_sources": [
                {"id": r.get("id") or r.get("entity_id"), "title": r.get("title"), "category": r.get("category"), "fusion_score": r.get("fusion_score")}
                for r in hits
            ],
        }

    def diacritize_ascii(self, ascii_text: str) -> Dict[str, Any]:
        """Universal, context-aware 25-letter Yorùbá diacritization."""
        start_time = time.time()
        safe_ascii = sanitize_xml_user_input(ascii_text, max_chars=1000, tag="text_to_diacritize")
        diacritized_output, method = "", "Gemini-2.5-Flash (Orthographic Restorer)"

        if self.client:
            try:
                cfg = types.GenerateContentConfig(system_instruction=DIACRITIZER_SYSTEM_INSTRUCTION, thinking_config=types.ThinkingConfig(thinking_level="low"), max_output_tokens=500)
                resp = self.client.models.generate_content(model="gemini-2.5-flash", contents=f"<text_to_diacritize>\n{safe_ascii}\n</text_to_diacritize>", config=cfg)
                diacritized_output = resp.text.strip()
            except Exception:
                diacritized_output, method = self._sovereign_diacritize(ascii_text), "Sovereign Linguistic Orthographic Core"
        else:
            diacritized_output, method = self._sovereign_diacritize(ascii_text), "Sovereign Linguistic Orthographic Core"

        return {"status": "success", "original_ascii": ascii_text, "diacritized_text": diacritized_output, "method": method, "latency_ms": round((time.time() - start_time) * 1000, 2)}

    diacritize = diacritize_ascii

    def _sovereign_diacritize(self, text: str) -> str:
        """Universal algorithmic diacritizer with greedy n-grams and collocations."""
        result, placeholders = text, {}
        for i, (p_asc, p_diac) in enumerate(SOVEREIGN_MULTI_WORD_PHRASES):
            pat = re.compile(r"\b" + re.escape(p_asc) + r"\b", re.IGNORECASE)
            def rep(m, repl=p_diac, idx=i):
                mt = m.group(0)
                fv = repl.upper() if mt.isupper() else ((repl[0].upper() + repl[1:]) if mt[0].isupper() else repl)
                k = f"__AGBA_PHRASE_{idx}_{len(placeholders)}__"
                placeholders[k] = fv
                return k
            result = pat.sub(rep, result)

        if hasattr(self.retriever, "corpus_entities"):
            for j, ent in enumerate(self.retriever.corpus_entities):
                t = ent.get("title", "")
                if t.lower() in ("ogun", "oro", "owo", "ile", "orun", "oko", "aye"):
                    continue
                for alias in ent.get("aliases", []):
                    if len(alias) >= 4 and " " in alias:
                        pat = re.compile(r"\b" + re.escape(alias) + r"\b", re.IGNORECASE)
                        def ent_rep(m, title=t, e_idx=j):
                            k = f"__AGBA_ENTITY_{e_idx}_{len(placeholders)}__"
                            placeholders[k] = title
                            return k
                        result = pat.sub(ent_rep, result)

        def token_sub(m):
            raw = m.group(0)
            if raw.startswith("__AGBA_"):
                return raw
            low = raw.lower()
            homo = disambiguate_homograph(low, text)
            if homo:
                return homo.upper() if raw.isupper() else ((homo[0].upper() + homo[1:]) if raw[0].isupper() else homo.lower())
            if low in SOVEREIGN_LEXICAL_BASE:
                cand = SOVEREIGN_LEXICAL_BASE[low]
                return cand.upper() if raw.isupper() else ((cand[0].upper() + cand[1:]) if raw[0].isupper() else cand)
            return raw

        result = re.sub(r"\b[a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]+\b", token_sub, result)
        for k, v in placeholders.items():
            result = result.replace(k, v)
        return result

    def translate_cultural(self, yoruba_text: str) -> Dict[str, Any]:
        """Dual-Action Cultural Translation & Deep Glossing."""
        start_time = time.time()
        safe_yoruba = sanitize_xml_user_input(yoruba_text, max_chars=1000, tag="text_to_translate_and_gloss")
        structured_data, method = {}, "Gemini-2.5-Flash (Cultural Glossing)"

        if self.client:
            try:
                cfg = types.GenerateContentConfig(system_instruction=CULTURAL_TRANSLATION_SYSTEM_INSTRUCTION, thinking_config=types.ThinkingConfig(thinking_level="low"), response_mime_type="application/json")
                resp = self.client.models.generate_content(model="gemini-2.5-flash", contents=f"<text_to_translate_and_gloss>\n{safe_yoruba}\n</text_to_translate_and_gloss>", config=cfg)
                structured_data = json.loads(resp.text)
            except Exception:
                structured_data, method = self._fallback_translate(yoruba_text), "Sovereign Corpus Gloss Matcher"
        else:
            structured_data, method = self._fallback_translate(yoruba_text), "Sovereign Corpus Gloss Matcher"

        return {"status": "success", "result": structured_data, "method": method, "latency_ms": round((time.time() - start_time) * 1000, 2)}

    cultural_translation = translate_cultural

    def _fallback_translate(self, yoruba_text: str) -> Dict[str, Any]:
        hits = self.retriever.retrieve(yoruba_text, top_k=1)
        gloss = (hits[0].get("details", {}).get("description") if hits else None) or "Deep philosophical meaning preserved across oral traditions and spiritual rites."
        return {"orthographic_retention": yoruba_text, "literal_translation": f"English contextual rendering for: {yoruba_text}", "cultural_gloss": gloss}

    def _decompose_query_intent(self, message: str, session_history: Optional[List[Dict[str, str]]]) -> str:
        return decompose_query_intent(message, session_history)

    def _fallback_chat_synthesis(self, query: str, hits: List[Dict[str, Any]], session_history: Optional[List[Dict[str, str]]] = None) -> str:
        return fallback_chat_synthesis(query, hits, session_history)


AgbaIntelligenceSuite = ÀgbàIntelligenceSuite
_intelligence_suite = None


def get_intelligence_suite(retriever=None):
    global _intelligence_suite
    if _intelligence_suite is None and retriever is not None:
        _intelligence_suite = ÀgbàIntelligenceSuite(retriever)
    return _intelligence_suite
