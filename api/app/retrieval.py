# 🏛️ ÀGBÀ ENGINE: TRI-MODAL HYBRID RETRIEVAL CORE (v6.2.0)
# Lead Architect: Aruna Olanrewaju Kabiru | Coordinator: HANDOFF-AGBEDE-005

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    from app.config import ÀgbàConfig, AgbaConfig
    from app.multimodal_resolver import map_call_and_response_audio, map_image_assets, resolve_entity_multimodal_links
    from app.lexical_ranker import score_lexical_entities, prepare_corpus_index
    from app.sub_variant_hydrator import find_sub_variant_match, synthesize_sub_variant
except Exception:
    from config import ÀgbàConfig, AgbaConfig
    from multimodal_resolver import map_call_and_response_audio, map_image_assets, resolve_entity_multimodal_links
    from lexical_ranker import score_lexical_entities, prepare_corpus_index
    from sub_variant_hydrator import find_sub_variant_match, synthesize_sub_variant

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
    """Production-grade hybrid cultural retrieval coordinator for Àgbà Engine."""
    _instance = None

    def __init__(self):
        self.config = AgbaConfig
        self.corpus_path = self.config.get_normalized_corpus_path()
        self.qdrant_path = self.config.get_qdrant_storage_path()
        self.golden_matrix_dir = self.config.get_golden_matrix_dir()
        self.collection_name = self.config.COLLECTION_NAME

        print("🏛️ Initializing AgbaHybridRetriever (v6.2.0)...")
        self.corpus_entities = self._load_corpus()
        print(f"   📂 Master Corpus Loaded: {len(self.corpus_entities)} entities")

        self.qdrant, self.encoder = None, None
        if HAS_QDRANT:
            try:
                self.qdrant = QdrantClient(path=str(self.qdrant_path))
                print(f"   🗄️  Qdrant Connected: Collection '{self.collection_name}'")
            except Exception as e:
                print(f"   [!] Qdrant notice: {e}. Dense disabled.")
        if HAS_SENTENCE_TRANSFORMERS:
            try:
                self.encoder = SentenceTransformer(self.config.EMBEDDING_MODEL_NAME)
                print("   ✅ Embeddings Ready")
            except Exception as e:
                print(f"   [!] Embedding notice: {e}.")

        audio = map_call_and_response_audio(self.golden_matrix_dir, self.config.ROOT_DIR)
        self.acoustic_calls, self.acoustic_responses, self.acoustic_takes, self.master_opus_suites, self.oriki_assets = audio
        self.audio_tokens, (self.image_assets, self.visual_metadata) = self.acoustic_calls, map_image_assets(self.golden_matrix_dir)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ÀgbàHybridRetriever()
        return cls._instance

    def _load_corpus(self) -> List[Dict[str, Any]]:
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        entities = list(data.values()) if isinstance(data, dict) else data
        odu = self.corpus_path.parent / "agba_odu_ifa_256_canonical.json"
        if odu.exists():
            try:
                with open(odu, "r", encoding="utf-8") as f:
                    e_ids = {e.get("id") for e in entities}
                    entities.extend(item for item in json.load(f) if item.get("id") not in e_ids)
            except Exception as ex:
                print(f"   [!] Notice: Odù Ifá ingestion notice: {ex}")
        return prepare_corpus_index(entities)

    def search_dense(self, query: str, top_k: int = 15) -> List[Dict[str, Any]]:
        """Perform dense vector retrieval against Qdrant collection."""
        if not self.qdrant or not self.encoder:
            return []
        try:
            vec = self.encoder.encode(query).tolist()
            qp = getattr(self.qdrant, "query_points", None)
            hits = qp(collection_name=self.collection_name, query=vec, limit=top_k).points if qp else self.qdrant.search(collection_name=self.collection_name, query_vector=vec, limit=top_k)
            return [{"id": (h.payload or {}).get("id") or str(h.id), "title": (h.payload or {}).get("title", ""), "score": float(h.score), "payload": h.payload or {}, "retrieval_method": "dense_vector"} for h in hits]
        except Exception:
            return []

    def search_lexical(self, query: str, top_k: int = 15) -> List[Dict[str, Any]]:
        """Diacritic-aware lexical, strict word-boundary, and tier-weighted matcher."""
        return score_lexical_entities(self.corpus_entities, query, top_k=top_k)

    def _resolve_multimodal_links(self, eid: str, title: str) -> Dict[str, Any]:
        return resolve_entity_multimodal_links(eid, title, self.acoustic_calls, self.acoustic_responses, self.image_assets, self.visual_metadata)

    def _find_sub_variant_match(self, query: str) -> Optional[tuple]:
        return find_sub_variant_match(self.corpus_entities, query)

    def _synthesize_sub_variant(self, variant_title: str, parent: Dict[str, Any]) -> Dict[str, Any]:
        return synthesize_sub_variant(variant_title, parent)

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
        rrf_scores, entity_map = {}, {}

        eff_lex = lexical_weight if dense_hits else 1.0
        for hits, w in ((dense_hits, dense_weight), (lexical_hits, eff_lex)):
            for rank, hit in enumerate(hits):
                eid = str(hit["id"])
                rrf_scores[eid] = rrf_scores.get(eid, 0.0) + (w / (rrf_k + rank + 1))
                entity_map.setdefault(eid, hit["payload"])

        sorted_eids = sorted(rrf_scores, key=rrf_scores.get, reverse=True)
        final_results = []
        for eid in sorted_eids:
            payload = entity_map.get(eid, {})
            title, category = payload.get("title", eid), payload.get("category", "General Heritage")

            if culture_id and culture_id.lower() not in ("all", "pan_african", "yoruba") and (payload.get("culture_id") or "yoruba").lower() != culture_id.lower():
                continue
            if cultural_domain and "comprehensive" not in cultural_domain.lower():
                full_text = f"{title} {category} {payload.get('description', '')}".lower()
                if not any(kw in full_text for kw in cultural_domain.lower().split()):
                    continue

            final_results.append({
                "entity_id": eid, "title": title, "category": category,
                "fusion_score": round(rrf_scores[eid], 5),
                "multimodal_assets": self._resolve_multimodal_links(eid, title),
                "details": payload,
            })
            if len(final_results) >= top_k:
                break

        sv_match = self._find_sub_variant_match(query)
        if sv_match:
            v_title, p_entity = sv_match
            synth = self._synthesize_sub_variant(v_title, p_entity)
            v_id = synth["id"]
            final_results = [r for r in final_results if r.get("title") != v_title and r.get("entity_id") != v_id]
            final_results.insert(0, {
                "entity_id": v_id, "title": v_title, "category": synth["category"], "fusion_score": 1.0,
                "is_parent": False, "sovereign_parent": p_entity.get("title", ""), "sovereign_parent_status": "Living Sub-Variant",
                "multimodal_assets": self._resolve_multimodal_links(v_id, v_title), "details": synth,
            })

        return final_results[:top_k]


AgbaHybridRetriever = ÀgbàHybridRetriever
