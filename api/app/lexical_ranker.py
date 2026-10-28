# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: LEXICAL & DIACRITIC RANKER (v6.2.0)
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Modular Extraction: HANDOFF-AGBEDE-005 (Pillar 1: Law 2 - Three-Drawer Mandate)
# ==============================================================================

import re
from typing import List, Dict, Any

try:
    from app.semantic_bridge import normalize_y, strip_accents, preprocess_query_tokens
except (ImportError, ValueError):
    try:
        from .semantic_bridge import normalize_y, strip_accents, preprocess_query_tokens
    except (ImportError, ValueError):
        from semantic_bridge import normalize_y, strip_accents, preprocess_query_tokens

TIER_KEYS = ["description", "etymology_and_philosophy", "historical_timeline", "social_and_ritual_context", "proverbs_and_oral_traditions"]


def prepare_corpus_index(entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Pre-computes normalized and accent-folded representations for fast lexical scoring."""
    for e in entities:
        eid = str(e.get("id", ""))
        e["_norm_title"], e["_stripped_title"] = normalize_y(e.get("title", "")), strip_accents(e.get("title", ""))
        e["_norm_eid"], e["_stripped_eid"] = normalize_y(eid), strip_accents(eid).replace("_", " ")
        e["_norm_aliases"] = [normalize_y(a) for a in e.get("aliases", [])]
        e["_stripped_aliases"] = [strip_accents(a) for a in e.get("aliases", [])]
        e["_stripped_cat"] = strip_accents(e.get("category", ""))
        texts = [strip_accents(" ".join(e[k]) if isinstance(e[k], list) else str(e[k])) for k in TIER_KEYS if e.get(k)]
        e["_tier_text"] = " ".join(texts)
    return entities


def score_lexical_entities(
    corpus_entities: List[Dict[str, Any]],
    query: str,
    top_k: int = 15,
) -> List[Dict[str, Any]]:
    """Diacritic-aware lexical, strict word-boundary, and tier-weighted matcher."""
    _q, norm_query, stripped_query, norm_core, stripped_core, q_words, bridge_targets = preprocess_query_tokens(query)
    has_query_diacritics = norm_query != stripped_query
    scored = []

    for entity in corpus_entities:
        title, stripped_title = entity.get("_norm_title", ""), entity.get("_stripped_title", "")
        norm_eid, stripped_eid = entity.get("_norm_eid", ""), entity.get("_stripped_eid", "")
        aliases, stripped_aliases = entity.get("_norm_aliases", []), entity.get("_stripped_aliases", [])
        category_stripped = entity.get("_stripped_cat", "")
        score = 0.0

        # 1A. RC-1: Supreme Exact Diacritic/Tonal Match (+600.0)
        if norm_core and (norm_core == title or norm_core == norm_eid):
            score += 600.0
        elif norm_core and norm_core in aliases:
            score += 540.0
        elif norm_query == title or norm_query == norm_eid:
            score += 520.0
        elif norm_query in aliases:
            score += 480.0

        # 1B. RC-1: Accent-Folded Exact Match (+450 / +180)
        if stripped_core and (stripped_core == stripped_title or stripped_core == stripped_eid):
            score += 180.0 if (has_query_diacritics and norm_core != title) else 450.0
        elif stripped_core and stripped_core in stripped_aliases:
            score += 150.0 if (has_query_diacritics and norm_core not in aliases) else 400.0
        elif stripped_query == stripped_title or stripped_query == stripped_eid:
            score += 160.0 if (has_query_diacritics and norm_query != title) else 380.0
        elif stripped_query in stripped_aliases:
            score += 140.0 if (has_query_diacritics and norm_query not in aliases) else 340.0

        # 2. Strict Word-Boundary Phrase Match
        elif stripped_core and re.search(r"\b" + re.escape(stripped_core) + r"\b", stripped_title):
            score += 250.0
        elif stripped_core and any(re.search(r"\b" + re.escape(stripped_core) + r"\b", a) for a in stripped_aliases):
            score += 200.0
        elif stripped_query and re.search(r"\b" + re.escape(stripped_query) + r"\b", stripped_title):
            score += 50.0
        elif stripped_query and any(re.search(r"\b" + re.escape(stripped_query) + r"\b", a) for a in stripped_aliases):
            score += 40.0

        # 3. Category match bonus
        if any(re.search(r"\b" + re.escape(w) + r"\b", category_stripped) for w in q_words):
            score += 3.0

        # 4. Strict Word-token matching across 14 tiers
        matched_words, tier_text = 0, entity.get("_tier_text", "")
        for w in q_words:
            pat = r"\b" + re.escape(w) + r"\b"
            if re.search(pat, stripped_title):
                score += 6.0; matched_words += 1
            elif any(re.search(pat, a) for a in stripped_aliases):
                score += 4.5; matched_words += 1
            elif re.search(pat, tier_text):
                score += 0.5; matched_words += 1

        if q_words and matched_words == len(q_words):
            score += 4.0

        # 5. RC-3: English-to-Yorùbá Semantic Bridge Bonus
        if bridge_targets:
            for bt in bridge_targets:
                if stripped_title == bt:
                    score += 10.0
                elif re.search(r"\b" + re.escape(bt) + r"\b", stripped_title):
                    score += 7.0
                elif any(bt == a or re.search(r"\b" + re.escape(bt) + r"\b", a) for a in stripped_aliases):
                    score += 5.0

        if score > 0:
            scored.append({
                "id": entity.get("id"), "title": entity.get("title"),
                "score": round(score, 4), "payload": entity,
                "retrieval_method": "lexical_diacritic_word_boundary",
            })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]
