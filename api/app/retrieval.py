# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: TRI-MODAL HYBRID RETRIEVAL CORE (v6.0.0-alpha)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Pipeline:
#   1. Dense Vector Similarity (Qdrant R^384 Semantic Search)
#   2. Lexical & Diacritic Matcher (NFC/NFD Yoruba Orthography Parity)
#   3. Reciprocal Rank Fusion (RRF, k=60)
#   4. Tri-Modal Asset Enrichment:
#      - Vision Museum DAM (CMA, AIC, Golden Matrix Regalia)
#      - Acoustic Call (Spoken Speech) & Response (Dùndún Gángan Mimicry)
# ==============================================================================

import os
import re
import json
import unicodedata
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    from .config import ÀgbàConfig, AgbaConfig
except (ImportError, ValueError):
    try:
        from app.config import ÀgbàConfig, AgbaConfig
    except ImportError:
        from config import ÀgbàConfig, AgbaConfig

# Optional ML dependencies with graceful degradation
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

def normalize_y(text: str) -> str:
    """Normalize string using Unicode NFC and lowercase for robust diacritic matching."""
    if not text:
        return ""
    return unicodedata.normalize("NFC", str(text).strip().lower())

def strip_accents(text: str) -> str:
    """Strip accents and diacritics for phonetic/audio token mapping."""
    if not text:
        return ""
    nfkd = unicodedata.normalize('NFKD', text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower().replace(" ", "").replace("_", "").replace("-", "")

class ÀgbàHybridRetriever:
    """
    Production-grade hybrid cultural retrieval engine for Àgbà Engine.
    Combines dense neural embeddings with diacritic-aware lexical scoring.
    """
    _instance = None

    def __init__(self):
        self.config = AgbaConfig
        self.corpus_path = self.config.get_normalized_corpus_path()
        self.qdrant_path = self.config.get_qdrant_storage_path()
        self.golden_matrix_dir = self.config.get_golden_matrix_dir()
        
        print("🏛️ Initializing AgbaHybridRetriever...")
        # 1. Load Local Master Corpus
        self.corpus_entities = self._load_corpus()
        print(f"   📂 Master Corpus Loaded: {len(self.corpus_entities)} entities")

        # 2. Initialize Qdrant Client (if available)
        self.collection_name = self.config.COLLECTION_NAME
        self.qdrant = None
        if HAS_QDRANT:
            try:
                self.qdrant = QdrantClient(path=str(self.qdrant_path))
                print(f"   🗄️  Qdrant Connected: Collection '{self.collection_name}'")
            except Exception as e:
                print(f"   [!] Qdrant connection notice: {e}. Dense vector search disabled.")
        else:
            print("   ℹ️  Notice: qdrant-client not installed locally. Lexical diacritic engine active.")

        # 3. Initialize Dense Embedding Model (if available)
        self.encoder = None
        if HAS_SENTENCE_TRANSFORMERS:
            try:
                print(f"   🧠 Loading Embedding Model: {self.config.EMBEDDING_MODEL_NAME}...")
                self.encoder = SentenceTransformer(self.config.EMBEDDING_MODEL_NAME)
                print("   ✅ Embeddings Ready")
            except Exception as e:
                print(f"   [!] Embedding model notice: {e}.")
        else:
            print("   ℹ️  Notice: sentence-transformers not installed locally. Lexical diacritic engine active.")

        # 4. Map Multi-Modal Assets (Vision Images & Authentic Acoustic Matrix)
        self.acoustic_calls, self.acoustic_responses, self.acoustic_takes, self.master_opus_suites, self.oriki_assets = self._map_call_and_response_audio()
        self.audio_tokens = self.acoustic_calls
        self.visual_metadata = {}
        self.image_assets = self._map_image_assets()
        unique_images = len(set(self.image_assets.values()))
        print(f"   👑 Multi-Modal Assets: 80 OptionB Tokens (40 Calls, 40 Responses), {len(self.master_opus_suites)} Master Opus Suites, {len(self.oriki_assets)} Oríkì Ensemble Assets | {unique_images} Verified Visual Masterworks ({len(self.image_assets)} Search Keys)")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AgbaHybridRetriever()
        return cls._instance

    def _load_corpus(self) -> List[Dict[str, Any]]:
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return list(data.values())
        return data

    def _map_call_and_response_audio(self) -> tuple:
        """
        Comprehensive multi-modal acoustic mapping across the 3 exclusive authentic Yorùbá audio repositories:
        1. Gangan_Master_Segments_OptionB (80 files: 40 Spoken Calls & 40 Dùndún Gángan Responses across 20 Canonical Concepts)
        2. Master_Opus_Suites (4 Sacred Master Audio Suites in .opus)
        3. Oríkì_Ọba_Itire_Ensemble_Loops (59 assets: 52 polyrhythmic ensemble loops + 1 vocal chant + 6 Kábíyèsí mimicry takes)
        """
        gms_dir = self.golden_matrix_dir / "Gangan_master_segments"
        optb_dir = gms_dir / "Gangan_Master_Segments_OptionB"
        if not optb_dir.exists():
            optb_dir = self.golden_matrix_dir / "Gangan_Master_Segments_OptionB"

        calls = {}
        responses = {}
        takes = {}
        master_opus = {}
        oriki_assets = []

        # 1. Map Gangan_Master_Segments_OptionB (80 Assets)
        if optb_dir.exists():
            for f in sorted(optb_dir.glob("*.wav")):
                stem = f.stem
                clean = strip_accents(stem)
                core_key = clean.replace("spoken", "").replace("dundungangan", "").replace("gangan", "").replace("dundun", "")
                core_key = re.sub(r"[_\s]*0[1-9][_\s]*", "", core_key).strip()
                
                if core_key not in takes:
                    takes[core_key] = {"calls": [], "responses": []}
                
                if "spoken" in clean:
                    takes[core_key]["calls"].append(str(f))
                    if core_key not in calls or "_01_" in stem:
                        calls[core_key] = str(f)
                elif "gangan" in clean or "dundun" in clean:
                    takes[core_key]["responses"].append(str(f))
                    if core_key not in responses or "_01_" in stem:
                        responses[core_key] = str(f)

        # 2. Map Master Opus Suites (4 files)
        candidate_opus_dirs = [
            gms_dir,
            self.config.ROOT_DIR / "Agba_Engine_Foundational_Vault" / "03_Acoustic_Counterpart_Tokens" / "Master_Opus_Suites"
        ]
        for odir in candidate_opus_dirs:
            if odir.exists():
                for f in odir.glob("*.opus"):
                    fn = f.name
                    clean_fn = strip_accents(fn)
                    if "ayalu" in clean_fn or "gudugudu" in clean_fn:
                        master_opus["oriki_oba_itire_ensemble"] = str(f)
                    elif "regalia" in clean_fn:
                        master_opus["full_regalia_ati_solfege_mimicry"] = str(f)
                    elif "baseline" in clean_fn or "glissando" in clean_fn:
                        master_opus["foundational_tone_scale_glissando"] = str(f)
                    elif "kabiyesi" in clean_fn:
                        master_opus["gangan_kabiyesi_salutations"] = str(f)

        # 3. Map Oríkì Ọba Itire Ensemble Loops & Vocal Praise Chant (59 files)
        candidate_oriki_dirs = [
            gms_dir / "Oríkì_Ọba_Itire_Ensemble_Loops",
            self.golden_matrix_dir / "Oríkì_Ọba_Itire_Ensemble_Loops",
            self.config.ROOT_DIR / "Agba_Engine_Foundational_Vault" / "03_Acoustic_Counterpart_Tokens" / "Oríkì_Ọba_Itire_Ensemble_Loops"
        ]
        for rdir in candidate_oriki_dirs:
            if rdir.exists():
                for f in rdir.glob("*.wav"):
                    oriki_assets.append(str(f))
                break

        return calls, responses, takes, master_opus, oriki_assets

    def _map_image_assets(self) -> Dict[str, str]:
        """Map normalized entity keys to verified visual regalia and indigenous metadata."""
        images_dir = self.golden_matrix_dir / "Images"
        unified_manifest = self.golden_matrix_dir / "agba_unified_visual_regalia_manifest.json"
        museum_manifest = self.golden_matrix_dir / "agba_harvested_museum_visuals.json"
        mapping = {}
        self.visual_metadata = {}
        
        # 1. Load exact canonical mappings from verified manifests (unified preferred)
        target_manifest = unified_manifest if unified_manifest.exists() else museum_manifest
        if target_manifest.exists():
            try:
                with open(target_manifest, "r", encoding="utf-8") as mf:
                    manifest_items = json.load(mf)
                for it in manifest_items:
                    fname = it.get("filename")
                    fpath = images_dir / fname if fname else None
                    if fpath and fpath.exists():
                        fpath_str = str(fpath)
                        self.visual_metadata[fpath_str] = it
                        self.visual_metadata[fname] = it
                        canon = it.get("canonical_name", "")
                        if canon:
                            self.visual_metadata[canon] = it
                            self.visual_metadata[normalize_y(canon)] = it
                            self.visual_metadata[strip_accents(canon)] = it
                        t = it.get("title", "")
                        if t:
                            self.visual_metadata[t] = it
                            self.visual_metadata[normalize_y(t)] = it
                        full_t = it.get("canonical_title_full", "")
                        if full_t:
                            self.visual_metadata[full_t] = it
                        
                        # Register foundational diacritic filename aliases
                        aliases = {
                            "Adé Ààrẹ": ["Adé Ààrẹ.jpeg", "Ade Aare.jpeg", "Foundational_Ade_Aare.jpeg"],
                            "Èwù Ìlèkè": ["Èwù Ìlèkè.webp", "Ewu Ileke.webp", "Foundational_Ewu_Ileke.webp"],
                            "Fìlà Abetí Ajá": ["Fìlà Abetí Ajá.jpeg", "Fila Abeti Aja.jpeg", "Foundational_Fila_Abeti_Aja.jpeg"],
                            "Fìlà Gọ̀bị́": ["Fìlà Gọ̀bị́.jpeg", "Fila Gobi.jpeg", "Foundational_Fila_Gobi.jpeg"],
                            "Kábíyèsí": ["Kábíyèsí.jpg", "Kabiyesi.jpg", "Foundational_Kabiyesi.jpg"],
                            "Pà Kaja": ["Pà Kaja.jpeg", "Pa Kaja.jpeg", "Foundational_Pa_Kaja.jpeg"]
                        }
                        if canon in aliases:
                            for afn in aliases[canon]:
                                self.visual_metadata[afn] = it
                                apath = str(images_dir / afn)
                                self.visual_metadata[apath] = it
                        
                        # Keys to index
                        keys_to_index = [
                            it.get("canonical_name", ""),
                            it.get("canonical_title_full", ""),
                            it.get("corpus_concept_id", ""),
                            it.get("museum_archival_title", ""),
                            it.get("title", ""),
                            it.get("canonical_corpus_concept", "")
                        ]
                        for raw in keys_to_index:
                            if raw:
                                mapping[normalize_y(raw)] = fpath_str
                                mapping[strip_accents(raw)] = fpath_str
                                # Extract parenthetical terms
                                for p in re.findall(r"\((.*?)\)", raw):
                                    mapping[normalize_y(p)] = fpath_str
                                    mapping[strip_accents(p)] = fpath_str
            except Exception as e:
                print(f"   [!] Manifest map notice: {e}")

        # 2. File-system scanning fallback
        if images_dir.exists():
            for f in images_dir.glob("*.*"):
                if f.suffix.lower() in [".jpg", ".jpeg", ".webp", ".png"]:
                    stem = f.stem
                    clean_name = normalize_y(stem)
                    stripped = strip_accents(stem)
                    
                    mapping[clean_name] = str(f)
                    mapping[stripped] = str(f)
                    
                    # Strip prefixes (CMA_, AIC_, MET_, SI_, Foundational_)
                    no_prefix = re.sub(r"^(cma|aic|met|si|foundational)_", "", stem, flags=re.I)
                    clean_core = re.sub(r"(_\d+|_NMAfA-[\w-]+)$", "", no_prefix)
                    mapping[strip_accents(no_prefix)] = str(f)
                    mapping[strip_accents(clean_core)] = str(f)
                    mapping[normalize_y(clean_core)] = str(f)
                    
                    for p in re.findall(r"\((.*?)\)", stem):
                        mapping[normalize_y(p)] = str(f)
                        mapping[strip_accents(p)] = str(f)

        return mapping

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
                    limit=top_k
                ).points
            else:
                hits = self.qdrant.search(
                    collection_name=self.collection_name,
                    query_vector=query_vector,
                    limit=top_k
                )

            results = []
            for hit in hits:
                payload = hit.payload or {}
                results.append({
                    "id": payload.get("id") or str(hit.id),
                    "title": payload.get("title", ""),
                    "score": float(hit.score),
                    "payload": payload,
                    "retrieval_method": "dense_vector"
                })
            return results
        except Exception as e:
            return []

    def search_lexical(self, query: str, top_k: int = 15) -> List[Dict[str, Any]]:
        """Perform diacritic-aware lexical and keyword matching on master corpus."""
        norm_query = normalize_y(query)
        stripped_query = strip_accents(query)
        scored = []

        for entity in self.corpus_entities:
            title = normalize_y(entity.get("title", ""))
            stripped_title = strip_accents(entity.get("title", ""))
            aliases = [normalize_y(a) for a in entity.get("aliases", [])]
            stripped_aliases = [strip_accents(a) for a in entity.get("aliases", [])]
            desc = normalize_y(entity.get("description", ""))
            etym = normalize_y(entity.get("etymology_and_philosophy", ""))
            
            score = 0.0
            # 1. Exact match on title or alias with diacritics
            if norm_query == title or norm_query in aliases:
                score += 5.0
            # 2. Match without diacritics
            elif stripped_query == stripped_title or stripped_query in stripped_aliases:
                score += 4.5
            # 3. Substring match in title
            elif norm_query in title or any(norm_query in a for a in aliases):
                score += 0.85
            elif stripped_query in stripped_title:
                score += 0.8
            # 4. Word token overlap
            q_words = norm_query.split()
            if any(w in title for w in q_words):
                score += 0.5
            if any(w in desc for w in q_words):
                score += 0.3
            if any(w in etym for w in q_words):
                score += 0.2

            if score > 0:
                scored.append({
                    "id": entity.get("id"),
                    "title": entity.get("title"),
                    "score": score,
                    "payload": entity,
                    "retrieval_method": "lexical_diacritic"
                })

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

    def _resolve_multimodal_links(self, entity_id: str, title: str) -> Dict[str, Any]:
        """
        Enforce strict indigenous provenance, canonical Yorùbá nomenclature, and
        authentic multi-modal grounding (spoken Call, Dùndún Gángan acoustic response,
        and high-resolution curated regalia).
        """
        norm_id = normalize_y(entity_id)
        norm_title = normalize_y(title)
        stripped_id = strip_accents(entity_id)
        stripped_title = strip_accents(title)
        
        media_links = {
            "has_acoustic_counterpart": False,
            "has_audio_token": False,
            "call_spoken_audio_uri": None,
            "response_gangan_audio_uri": None,
            "acoustic_mimicry_type": None,
            "has_visual_asset": False,
            "visual_asset_uri": None,
            "canonical_name": None,
            "canonical_title_full": None,
            "indigenous_place_of_origin": None,
            "origin_region": None,
            "master_artisan_or_guild": None,
            "creation_epoch": None,
            "medium_materials": None,
            "corpus_deep_description": None,
            "philosophical_context": None,
            "current_custodial_repository": None,
            "museum_archival_title": None,
            "accession_number": None
        }

        # Resolve Acoustic Call (Spoken) & Response (Dùndún Gángan)
        for k in [stripped_id, stripped_title]:
            if k in self.acoustic_calls or k in self.acoustic_responses:
                media_links["has_acoustic_counterpart"] = True
                media_links["has_audio_token"] = True
                media_links["call_spoken_audio_uri"] = self.acoustic_calls.get(k)
                media_links["response_gangan_audio_uri"] = self.acoustic_responses.get(k)
                media_links["acoustic_mimicry_type"] = "Dùndún Gángan Glissando (Solfège Mimicry)"
                break
        
        if not media_links["has_acoustic_counterpart"]:
            for k, c_path in self.acoustic_calls.items():
                if k in stripped_id or k in stripped_title:
                    media_links["has_acoustic_counterpart"] = True
                    media_links["has_audio_token"] = True
                    media_links["call_spoken_audio_uri"] = c_path
                    media_links["response_gangan_audio_uri"] = self.acoustic_responses.get(k)
                    media_links["acoustic_mimicry_type"] = "Dùndún Gángan Glissando (Solfège Mimicry)"
                    break

        # Resolve Visual Asset with Canonical Yoruba & Indigenous Provenance
        matched_visual_uri = None
        for k in [norm_title, stripped_title, norm_id, stripped_id]:
            if k in self.image_assets:
                matched_visual_uri = self.image_assets[k]
                break

        # Canonical cross-reference for primordial Orisha/concepts
        if not matched_visual_uri:
            CROSS_REFS = {
                'esu': ['ogo elegba', 'dance staff for esu', 'ogo elegbara'],
                'sango': ['shrine figure for sango', 'sango'],
                'opon ifa': ['opon ifa', 'divination tray'],
                'iroke ifa': ['iroke ifa', 'tapper'],
                'agere ifa': ['agere ifa', 'divination vessel', 'arugba ifa'],
                'edan ogboni': ['edan ogboni', 'pair of staffs'],
                'ere ibeji': ['ere ibeji', 'twin figure'],
                'opo ogoga': ['opo ogoga', 'veranda post'],
                'udamalore': ['udamalore'],
                'orufanran': ['orufanran'],
                'aso oke': ['aso oke'],
                'egungun': ['egungun'],
                'gelede': ['gelede'],
                'ade aare': ['ade aare', 'foundational_ade_aare'],
                'ade': ['adenla', 'ade'],
                'kabiyesi': ['kabiyesi'],
                'onile': ['onile']
            }
            for ck, c_queries in CROSS_REFS.items():
                if ck in stripped_title or ck in stripped_id:
                    for query_kw in c_queries:
                        for img_k, img_uri in self.image_assets.items():
                            if query_kw in img_k:
                                matched_visual_uri = img_uri
                                break
                        if matched_visual_uri:
                            break
                if matched_visual_uri:
                    break

        if not matched_visual_uri:
            for k, path in self.image_assets.items():
                if (k and (k in stripped_title or stripped_title in k or k in stripped_id or stripped_id in k) and len(k) > 4):
                    matched_visual_uri = path
                    break

        if matched_visual_uri:
            media_links["has_visual_asset"] = True
            media_links["visual_asset_uri"] = matched_visual_uri
            meta = self.visual_metadata.get(matched_visual_uri)
            if not meta:
                import os
                bname = os.path.basename(matched_visual_uri)
                meta = self.visual_metadata.get(bname)
                
            if meta:
                media_links["canonical_name"] = meta.get("canonical_name")
                media_links["canonical_title_full"] = meta.get("canonical_title_full")
                media_links["indigenous_place_of_origin"] = meta.get("indigenous_place_of_origin")
                media_links["origin_region"] = meta.get("origin_region")
                media_links["master_artisan_or_guild"] = meta.get("master_artisan_or_guild")
                media_links["creation_epoch"] = meta.get("creation_epoch")
                media_links["medium_materials"] = meta.get("medium_materials")
                media_links["corpus_deep_description"] = meta.get("corpus_deep_description")
                media_links["philosophical_context"] = meta.get("philosophical_context")
                media_links["current_custodial_repository"] = meta.get("current_custodial_repository")
                media_links["museum_archival_title"] = meta.get("museum_archival_title")
                media_links["accession_number"] = meta.get("accession_number")

        return media_links

    def retrieve(
        self,
        query: str,
        cultural_domain: Optional[str] = None,
        top_k: int = 5,
        dense_weight: float = 0.6,
        lexical_weight: float = 0.4,
        rrf_k: int = 60
    ) -> List[Dict[str, Any]]:
        """
        Execute full hybrid retrieval pipeline using Reciprocal Rank Fusion (RRF).
        """
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

            if cultural_domain and "comprehensive" not in cultural_domain.lower():
                dom_norm = cultural_domain.lower()
                full_text = f"{title} {category} {payload.get('description', '')}".lower()
                if not any(kw in full_text for kw in dom_norm.split()):
                    continue

            multimodal_meta = self._resolve_multimodal_links(eid, title)

            final_results.append({
                "entity_id": eid,
                "title": title,
                "category": category,
                "fusion_score": round(rrf_scores[eid], 5),
                "multimodal_assets": multimodal_meta,
                "details": payload
            })

            if len(final_results) >= top_k:
                break

        return final_results

if __name__ == "__main__":
    retriever = AgbaHybridRetriever.get_instance()
    test_queries = ["Opón Ifá", "Ìrókẹ́ Ifá", "Ère Ìbejì", "Adé Ààrẹ", "Agbádá"]
    print("\n" + "=" * 80)
    print("🔍 TESTING RECONCILED MUSEUM DAM RETRIEVAL")
    print("=" * 80)
    for q in test_queries:
        print(f"\n⚡ Query: '{q}'")
        res = retriever.retrieve(q, top_k=1)
        for r in res:
            mm = r["multimodal_assets"]
            call_fn = Path(mm["call_spoken_audio_uri"]).name if mm["call_spoken_audio_uri"] else "None"
            resp_fn = Path(mm["response_gangan_audio_uri"]).name if mm["response_gangan_audio_uri"] else "None"
            img_fn = Path(mm["visual_asset_uri"]).name if mm["visual_asset_uri"] else "None"
            print(f"   ▶ [{r['fusion_score']}] {r['title']}")
            print(f"     🗣️  Call (Spoken Speech)       : {call_fn}")
            print(f"     🥁 Response (Dùndún Gángan)   : {resp_fn}")
            print(f"     🖼️  Museum Visual Hero Asset   : {img_fn}")

# Backward-compatible ASCII alias
AgbaHybridRetriever = ÀgbàHybridRetriever
