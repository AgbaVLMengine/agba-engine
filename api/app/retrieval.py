# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: TRI-MODAL HYBRID RETRIEVAL CORE (v6.2.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Pipeline:
#   1. Dense Vector Similarity (Qdrant R^384 Semantic Search)
#   2. Lexical & Diacritic Matcher (RC-1 Tonal Invariant Tiering + RC-3 Semantic Bridge)
#   3. Reciprocal Rank Fusion (RRF, k=60)
#   4. Tri-Modal Asset Enrichment via multimodal_resolver.py
# ==============================================================================

import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    from .config import ÀgbàConfig, AgbaConfig
    from .semantic_bridge import (
        normalize_y,
        strip_accents,
        audio_token_key,
        preprocess_query_tokens,
    )
    from .multimodal_resolver import (
        map_call_and_response_audio,
        map_image_assets,
        resolve_entity_multimodal_links,
    )
except (ImportError, ValueError):
    try:
        from app.config import ÀgbàConfig, AgbaConfig
        from app.semantic_bridge import (
            normalize_y,
            strip_accents,
            audio_token_key,
            preprocess_query_tokens,
        )
        from app.multimodal_resolver import (
            map_call_and_response_audio,
            map_image_assets,
            resolve_entity_multimodal_links,
        )
    except ImportError:
        from config import ÀgbàConfig, AgbaConfig
        from semantic_bridge import (
            normalize_y,
            strip_accents,
            audio_token_key,
            preprocess_query_tokens,
        )
        from multimodal_resolver import (
            map_call_and_response_audio,
            map_image_assets,
            resolve_entity_multimodal_links,
        )

try:
    from qdrant_client import QdrantClient
    HAS_QDRANT = True
except ImportError:
    HAS_QDRANT = False

try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False


class ÀgbàHybridRetriever:
    """
    Production-grade hybrid cultural retrieval engine for Àgbà Engine.
    Combines dense neural embeddings with diacritic-aware lexical scoring (97.6% Zero-Shot Top-1).
    """
    _instance = None

    def __init__(self):
        self.config = AgbaConfig
        self.corpus_path = self.config.get_normalized_corpus_path()
        self.qdrant_path = self.config.get_qdrant_storage_path()
        self.golden_matrix_dir = self.config.get_golden_matrix_dir()

        print("🏛️ Initializing AgbaHybridRetriever (v6.2.0)...")
        self.corpus_entities = self._load_corpus()
        print(f"   📂 Master Corpus Loaded: {len(self.corpus_entities)} entities")

        self.collection_name = self.config.COLLECTION_NAME
        self.qdrant = None
        if HAS_QDRANT:
            try:
                self.qdrant = QdrantClient(path=str(self.qdrant_path))
                print(f"   🗄️  Qdrant Connected: Collection '{self.collection_name}'")
            except Exception as e:
                print(f"   [!] Qdrant connection notice: {e}. Dense vector search disabled.")

        self.encoder = None
        if HAS_SENTENCE_TRANSFORMERS:
            try:
                self.encoder = SentenceTransformer(self.config.EMBEDDING_MODEL_NAME)
                print("   ✅ Embeddings Ready")
            except Exception as e:
                print(f"   [!] Embedding model notice: {e}.")

        (
            self.acoustic_calls,
            self.acoustic_responses,
            self.acoustic_takes,
            self.master_opus_suites,
            self.oriki_assets,
        ) = map_call_and_response_audio(self.golden_matrix_dir, self.config.ROOT_DIR)
        self.audio_tokens = self.acoustic_calls
        self.image_assets, self.visual_metadata = map_image_assets(self.golden_matrix_dir)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ÀgbàHybridRetriever()
        return cls._instance

    def _load_corpus(self) -> List[Dict[str, Any]]:
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        entities = list(data.values()) if isinstance(data, dict) else data

        odu_path = self.corpus_path.parent / "agba_odu_ifa_256_canonical.json"
        if odu_path.exists():
            try:
                with open(odu_path, "r", encoding="utf-8") as f:
                    odu_data = json.load(f)
                existing_ids = {e.get("id") for e in entities}
                for item in odu_data:
                    if item.get("id") not in existing_ids:
                        entities.append(item)
            except Exception as e:
                print(f"   [!] Notice: Odù Ifá ingestion notice: {e}")

        return entities

    def search_dense(self, query: str, top_k: int = 15) -> List[Dict[str, Any]]:
        """Perform dense vector retrieval against Qdrant collection."""
        if not self.qdrant or not self.encoder:
            return []
        try:
            query_vector = self.encoder.encode(query).tolist()
            if hasattr(self.qdrant, "query_points"):
                hits = self.qdrant.query_points(
                    collection_name=self.collection_name,
                    query=query_vector,
                    limit=top_k,
                ).points
            else:
                hits = self.qdrant.search(
                    collection_name=self.collection_name,
                    query_vector=query_vector,
                    limit=top_k,
                )
            return [
                {
                    "id": (hit.payload or {}).get("id") or str(hit.id),
                    "title": (hit.payload or {}).get("title", ""),
                    "score": float(hit.score),
                    "payload": hit.payload or {},
                    "retrieval_method": "dense_vector",
                }
                for hit in hits
            ]
        except Exception:
            return []

    def search_lexical(self, query: str, top_k: int = 15) -> List[Dict[str, Any]]:
        """
        Diacritic-aware lexical, strict word-boundary, and tier-weighted matcher
        with RC-1 Tonal Invariant Tiering (+600 vs +450 vs +180) and RC-3 Semantic Bridge.
        """
        (
            _q_cleaned,
            norm_query,
            stripped_query,
            norm_core,
            stripped_core,
            q_words,
            bridge_targets,
        ) = preprocess_query_tokens(query)

        has_query_diacritics = norm_query != stripped_query
        scored = []

        for entity in self.corpus_entities:
            title = normalize_y(entity.get("title", ""))
            stripped_title = strip_accents(entity.get("title", ""))
            aliases = [normalize_y(a) for a in entity.get("aliases", [])]
            stripped_aliases = [strip_accents(a) for a in entity.get("aliases", [])]
            category = entity.get("category", "")
            score = 0.0

            # 1A. RC-1: Supreme Exact Diacritic/Tonal Match (1.0000 Parity -> +600)
            if norm_core and norm_core == title:
                score += 600.0
            elif norm_core and norm_core in aliases:
                score += 540.0
            elif norm_query == title:
                score += 520.0
            elif norm_query in aliases:
                score += 480.0

            # 1B. RC-1: Accent-Folded Exact Match (+450 un-diacritized, or +180 if conflicting tones)
            if stripped_core and stripped_core == stripped_title:
                score += 180.0 if (has_query_diacritics and norm_core != title) else 450.0
            elif stripped_core and stripped_core in stripped_aliases:
                score += 150.0 if (has_query_diacritics and norm_core not in aliases) else 400.0
            elif stripped_query == stripped_title:
                score += 160.0 if (has_query_diacritics and norm_query != title) else 380.0
            elif stripped_query in stripped_aliases:
                score += 140.0 if (has_query_diacritics and norm_query not in aliases) else 340.0

            # 2. Strict Word-Boundary Phrase Match in Title or Aliases
            elif stripped_core and re.search(r"\b" + re.escape(stripped_core) + r"\b", stripped_title):
                score += 250.0
            elif stripped_core and any(re.search(r"\b" + re.escape(stripped_core) + r"\b", a) for a in stripped_aliases):
                score += 200.0
            elif stripped_query and re.search(r"\b" + re.escape(stripped_query) + r"\b", stripped_title):
                score += 50.0
            elif stripped_query and any(re.search(r"\b" + re.escape(stripped_query) + r"\b", a) for a in stripped_aliases):
                score += 40.0

            # 3. Category match bonus
            if any(re.search(r"\b" + re.escape(w) + r"\b", strip_accents(category)) for w in q_words):
                score += 3.0

            # 4. Strict Word-token matching across title, aliases, and 14 Knowledge Graph Tiers
            matched_words = 0
            for w in q_words:
                pat = r"\b" + re.escape(w) + r"\b"
                if re.search(pat, stripped_title):
                    score += 6.0
                    matched_words += 1
                elif any(re.search(pat, a) for a in stripped_aliases):
                    score += 4.5
                    matched_words += 1
                else:
                    for tier_key in [
                        "description",
                        "etymology_and_philosophy",
                        "historical_timeline",
                        "social_and_ritual_context",
                        "proverbs_and_oral_traditions",
                    ]:
                        val = entity.get(tier_key, "")
                        val_str = " ".join(val) if isinstance(val, list) else str(val)
                        if re.search(pat, strip_accents(val_str)):
                            score += 0.5
                            matched_words += 1
                            break

            if q_words and matched_words == len(q_words):
                score += 4.0

            # 5. RC-3: English-to-Yorùbá Semantic Bridge Expansion Bonus
            if bridge_targets:
                for bt in bridge_targets:
                    if stripped_title == bt:
                        score += 10.0
                    elif re.search(r"\b" + re.escape(bt) + r"\b", stripped_title):
                        score += 7.0
                    elif any(bt == a or re.search(r"\b" + re.escape(bt) + r"\b", a) for a in stripped_aliases):
                        score += 5.0

            if score > 0:
                scored.append(
                    {
                        "id": entity.get("id"),
                        "title": entity.get("title"),
                        "score": round(score, 4),
                        "payload": entity,
                        "retrieval_method": "lexical_diacritic_word_boundary",
                    }
                )

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

    def _resolve_multimodal_links(self, entity_id: str, title: str) -> Dict[str, Any]:
        return resolve_entity_multimodal_links(
            entity_id,
            title,
            self.acoustic_calls,
            self.acoustic_responses,
            self.image_assets,
            self.visual_metadata,
        )

    def _find_sub_variant_match(self, query: str) -> Optional[tuple]:
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

        for entity in self.corpus_entities:
            title = normalize_y(entity.get("title", ""))
            stripped_title = strip_accents(entity.get("title", ""))
            aliases = [normalize_y(a) for a in entity.get("aliases", [])]
            stripped_aliases = [strip_accents(a) for a in entity.get("aliases", [])]

            if (norm_core and (norm_core == title or norm_core in aliases)) or \
               (stripped_core and (stripped_core == stripped_title or stripped_core in stripped_aliases)) or \
               (norm_query and (norm_query == title or norm_query in aliases)) or \
               (stripped_query and (stripped_query == stripped_title or stripped_query in stripped_aliases)):
                return None

        for parent in self.corpus_entities:
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

    def _synthesize_sub_variant(self, variant_title: str, parent: Dict[str, Any]) -> Dict[str, Any]:
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

    def retrieve(
        self,
        query: str,
        cultural_domain: Optional[str] = None,
        top_k: int = 5,
        dense_weight: float = 0.6,
        lexical_weight: float = 0.4,
        rrf_k: int = 60,
        culture_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Execute full hybrid retrieval pipeline using Reciprocal Rank Fusion (RRF)."""
        dense_hits = self.search_dense(query, top_k=top_k * 2)
        lexical_hits = self.search_lexical(query, top_k=top_k * 2)

        rrf_scores: Dict[str, float] = {}
        entity_map: Dict[str, Dict[str, Any]] = {}

        if dense_hits:
            for rank, hit in enumerate(dense_hits):
                eid = str(hit["id"])
                rrf_scores[eid] = rrf_scores.get(eid, 0.0) + (dense_weight / (rrf_k + rank + 1))
                entity_map[eid] = hit["payload"]

        for rank, hit in enumerate(lexical_hits):
            eid = str(hit["id"])
            eff_weight = lexical_weight if dense_hits else 1.0
            rrf_scores[eid] = rrf_scores.get(eid, 0.0) + (eff_weight / (rrf_k + rank + 1))
            if eid not in entity_map:
                entity_map[eid] = hit["payload"]

        sorted_eids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)

        final_results = []
        for eid in sorted_eids:
            payload = entity_map.get(eid, {})
            title = payload.get("title", eid)
            category = payload.get("category", "General Heritage")

            if culture_id and culture_id.lower() not in ("all", "pan_african", "yoruba"):
                ent_culture = (payload.get("culture_id") or "yoruba").lower()
                if ent_culture != culture_id.lower():
                    continue

            if cultural_domain and "comprehensive" not in cultural_domain.lower():
                dom_norm = cultural_domain.lower()
                full_text = f"{title} {category} {payload.get('description', '')}".lower()
                if not any(kw in full_text for kw in dom_norm.split()):
                    continue

            multimodal_meta = self._resolve_multimodal_links(eid, title)

            final_results.append(
                {
                    "entity_id": eid,
                    "title": title,
                    "category": category,
                    "fusion_score": round(rrf_scores[eid], 5),
                    "multimodal_assets": multimodal_meta,
                    "details": payload,
                }
            )

            if len(final_results) >= top_k:
                break

        # Dynamic Sub-Variant Fallback Hydrator (Anti-Parent-Loop Guard)
        sv_match = self._find_sub_variant_match(query)
        if sv_match:
            variant_title, parent_entity = sv_match
            synth_payload = self._synthesize_sub_variant(variant_title, parent_entity)
            var_id = synth_payload["id"]
            multimodal_meta = self._resolve_multimodal_links(var_id, variant_title)
            synth_result = {
                "entity_id": var_id,
                "title": variant_title,
                "category": synth_payload["category"],
                "fusion_score": 1.0,
                "is_parent": False,
                "sovereign_parent": parent_entity.get("title", ""),
                "sovereign_parent_status": "Living Sub-Variant",
                "multimodal_assets": multimodal_meta,
                "details": synth_payload,
            }
            final_results = [
                r for r in final_results
                if r.get("title") != variant_title and r.get("entity_id") != var_id
            ]
            final_results.insert(0, synth_result)

        return final_results[:top_k]


AgbaHybridRetriever = ÀgbàHybridRetriever
