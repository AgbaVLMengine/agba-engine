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
    _, norm_query, stripped_query, norm_core, stripped_core, _, _ = preprocess_query_tokens(query)
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


def _domain_metadata(variant_title: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """Synthesize domain-aware multi-epoch timelines, dual-language proverbs, and provenance."""
    p_title = parent.get("title", "Sovereign Parent")
    cat = parent.get("category", "Cultural Heritage")
    if "Spiritual" in cat:
        timeline = f"Classical Antiquity (Pre-15th C.): Codified within {p_title} liturgical lineages at Ilé-Ifẹ̀. Imperial Era (16th-19th C.): Institutionalized across royal shrines. Contemporary Era: Preserved in homeland and transatlantic Lucumí/Candomblé traditions."
        craft = f"Consecrated natural fibers, botanical infusions, sacred camwood (osùn), and hand-forged shrine implements associated with {p_title}."
        proverbs = ["Orí ló mọ ẹni tí yóò là; òòṣà kì í dá ẹni tí kò bá ṣiṣẹ́ lọ́rọ̀. (Destiny guides prosperity; the sacred honors diligent devotion and lineage stewardship.)"]
    elif "Monarchy" in cat:
        timeline = f"Classical Era (12th-15th C.): Established under royal court protocol at Ilé-Ifẹ̀ and Ọ̀yọ́-Ilé as a specialized branch of {p_title}. 16th-19th C.: Regulated by palace guilds. 20th-21st C.: Maintained in contemporary coronations and diplomatic statecraft."
        craft = "Hand-strung glass seed beads, precious coral (iyùn), royal brass casting, and consecrated velvet-lined structural frameworks."
        proverbs = ["Ọba kì í pe méjìoko láàfin; àṣẹ kan ṣoṣo ní í darí ilú. (Two sovereigns do not rule one palace; unified authority sustains the realm.)"]
    elif "Martial" in cat or "Military" in cat:
        timeline = f"16th-18th C. Imperial Expansion: Forged within blacksmith and warrior guilds under {p_title} military doctrine. 19th C. Defense Wars: Deployed by Ẹ̀ṣọ́ and Balógun commanders. Modern Era: Preserved as ceremonial heritage emblems."
        craft = "High-carbon bloomery iron (irin), hardwood hilts carved with guild insignias, tempered steel blades, and protective leather sheaths."
        proverbs = ["Ojú ogun kì í ṣe ibi eré; jagunjagun kì íkọ̀yìn sí ọ̀tá. (The battlefield is no place for play; a true guardian stands firm.)"]
    elif "Attire" in cat:
        timeline = f"15th-18th C.: Woven on narrow strip looms within the {p_title} sartorial tradition. 19th C.: Elevated as prestige ceremonial attire. 20th-21st C.: Celebrated globally as an emblem of Yorùbá elegance."
        craft = "Hand-spun indigenous cotton, wild silk (sányàn), indigo-dyed threads (aro), and complex open-work weft patterning."
        proverbs = ["Èèyàn l'aṣọ mí; bí mo bá bojú wẹ̀yìn tí mo rí ènìyàn mí, inú mí á dùn. (People are my true garment; community is the noblest adornment.)"]
    elif "Auditory" in cat or "Music" in cat:
        timeline = f"Classical Era: Engineered by master Àyàn drum-carvers within the {p_title} acoustic family. Imperial Era: Served as palace speech-surrogacy and panegyric telegraphy. Modern Era: Anchors traditional and global Yorùbá percussion."
        craft = "Seasoned Cordia millenii (òmò) hardwood resonators, treated goatskin membranes, and leather tensioning thongs (ọ̀já)."
        proverbs = ["Bí ìlù bá dùn àjùlọ, ó máa ń fàya. (Measure and balance sustain the sacred rhythm of the drum.)"]
    else:
        timeline = f"Classical Foundations: Rooted in the foundational heritage of {p_title}. Historical Continuity (16th-19th C.): Refined across regional Yorùbá city-states. Contemporary Era: Actively transmitted across homeland and diaspora communities."
        craft = f"Traditional artisan craftsmanship, indigenous natural materials, and guild-regulated fabrication methods aligned with {p_title}."
        proverbs = ["Bí a kò bá gbàgbé ọ̀rọ̀ àná, a ó rí ẹni bá ṣeré lónìí. (When we honor ancestral memory, our living heritage endures.)"]
    return {
        "historical_timeline": timeline,
        "material_and_craftsmanship": craft,
        "proverbs_and_oral_traditions": proverbs,
        "provenance_and_citations": parent.get("provenance_and_citations") or "Johnson, Samuel (1921). The History of the Yorubas; Abiodun, Rowland (2014). Yoruba Art and Language.",
    }


def synthesize_sub_variant(variant_title: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """Dynamically synthesize a 14-tier child node inheriting from its Sovereign Parent."""
    variant_clean = strip_accents(variant_title)
    p_id, p_title, p_cat = parent.get("id", "variant"), parent.get("title", "Heritage"), parent.get("category", "Cultural Heritage")
    meta = _domain_metadata(variant_title, parent)
    other_variants = [sv for sv in parent.get("sub_variants", []) if sv != variant_title]
    desc = f"{variant_title} represents a specialized classical expression and canonical sub-variant within the {p_title} lineage of {p_cat}."
    context = f"Operates in direct ceremonial, social, and institutional alignment with {p_title}, carrying distinct regional and functional prestige."

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
        **meta,
        "social_and_ritual_context": context,
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
            "social_and_ritual_context": context,
            **meta,
        },
    }
