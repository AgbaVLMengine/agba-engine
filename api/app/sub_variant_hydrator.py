# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: SUB-VARIANT HYDRATOR (v6.2.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Modular Extraction: HANDOFF-AGBEDE-005 (Pillar 1: Law 2 - Three-Drawer Mandate)
# Encapsulates:
#   - Dynamic Sub-Variant Fallback Matching (Anti-Parent-Loop Guard)
#   - 14-Tier Child Node Synthesis inheriting from Sovereign Parent
# ==============================================================================

from typing import List, Dict, Any, Optional, Tuple

try:
    from app.semantic_bridge import normalize_y, strip_accents, preprocess_query_tokens
except (ImportError, ValueError):
    try:
        from .semantic_bridge import normalize_y, strip_accents, preprocess_query_tokens
    except (ImportError, ValueError):
        from semantic_bridge import normalize_y, strip_accents, preprocess_query_tokens


def find_sub_variant_match(corpus_entities: List[Dict[str, Any]], query: str) -> Optional[Tuple[str, Dict[str, Any]]]:
    """Check if query matches an unindexed sub-variant string in any Sovereign Parent."""
    (
        _q_cleaned,
        norm_query,
        stripped_query,
        norm_core,
        stripped_core,
        _q_words,
        _bridge_targets,
    ) = preprocess_query_tokens(query)

    for entity in corpus_entities:
        title = normalize_y(entity.get("title", ""))
        stripped_title = strip_accents(entity.get("title", ""))
        aliases = [normalize_y(a) for a in entity.get("aliases", [])]
        stripped_aliases = [strip_accents(a) for a in entity.get("aliases", [])]

        if (norm_core and (norm_core == title or norm_core in aliases)) or \
           (stripped_core and (stripped_core == stripped_title or stripped_core in stripped_aliases)) or \
           (norm_query and (norm_query == title or norm_query in aliases)) or \
           (stripped_query and (stripped_query == stripped_title or stripped_query in stripped_aliases)):
            return None

    for parent in corpus_entities:
        sub_variants = parent.get("sub_variants")
        if not isinstance(sub_variants, list) or not sub_variants:
            continue
        for sv in sub_variants:
            sv_norm = normalize_y(sv)
            sv_stripped = strip_accents(sv)
            if (norm_core and sv_norm == norm_core) or \
               (stripped_core and sv_stripped == stripped_core) or \
               (norm_query and sv_norm == norm_query) or \
               (stripped_query and sv_stripped == stripped_query):
                return (sv, parent)
    return None


def synthesize_sub_variant(variant_title: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """Dynamically synthesize a 14-tier child node inheriting from its Sovereign Parent."""
    variant_clean = strip_accents(variant_title)
    p_id = parent.get("id", "variant")
    p_title = parent.get("title", "Heritage")
    p_cat = parent.get("category", "Cultural Heritage")
    p_timeline = parent.get("historical_timeline") or f"Preserved through the generational lineage of {p_title}."
    p_craft = parent.get("material_and_craftsmanship", "Traditional luxury handcraft and guild metallurgy.")
    p_proverbs = parent.get("proverbs_and_oral_traditions", [])

    other_variants = [sv for sv in parent.get("sub_variants", []) if sv != variant_title]
    desc = f"A specialized living variant within the {p_title} tradition, embodying {variant_title} in classical {p_cat}."
    context = f"Operates in direct ritual, ceremonial, and practical alignment with {p_title}."

    return {
        "id": f"{p_id}_{variant_clean.replace(' ', '_')}",
        "title": variant_title,
        "culture": parent.get("culture", "Yorùbá"),
        "category": p_cat,
        "is_parent": False,
        "sovereign_parent": p_title,
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [variant_title, variant_clean],
        "description": desc,
        "historical_timeline": p_timeline,
        "material_and_craftsmanship": p_craft,
        "social_and_ritual_context": context,
        "proverbs_and_oral_traditions": p_proverbs,
        "diaspora_connections": parent.get("diaspora_connections", ""),
        "geographical_origin": parent.get("geographical_origin", "Yorùbáland"),
        "media_production_notes": parent.get("media_production_notes", ""),
        "sub_variants": [],
        "related_entities": [p_title] + other_variants,
        "details": {
            "culture": parent.get("culture", "Yorùbá"),
            "category": p_cat,
            "is_parent": False,
            "sovereign_parent": p_title,
            "sovereign_parent_status": "Living Sub-Variant",
            "description": desc,
            "historical_timeline": p_timeline,
            "material_and_craftsmanship": p_craft,
            "social_and_ritual_context": context,
            "proverbs_and_oral_traditions": p_proverbs,
        },
    }
