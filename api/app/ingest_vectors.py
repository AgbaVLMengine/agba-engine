# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: QDRANT EMBEDDING & VECTOR UPSERT PIPELINE (v6.0.0-alpha)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Dynamic vector ingestion pipeline powered by AgbaConfig.
# ==============================================================================

import os
import json
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer

# Import centralized dynamic configuration
try:
    from app.config import AgbaConfig
except ImportError:
    from config import AgbaConfig

def load_normalized_corpus():
    corpus_path = AgbaConfig.get_normalized_corpus_path()
    print(f"📂 Loading normalized corpus from: {corpus_path}")
    with open(corpus_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def run_vector_ingestion():
    print("=" * 75)
    print("🚀 INITIALIZING ÀGBÀ ENGINE EMBEDDING & UPSERT PIPELINE")
    print("   - Architect : Aruna Olanrewaju Kabiru")
    print("=" * 75)
    
    # 1. Initialize Qdrant Client (Persistent Storage resolved by AgbaConfig)
    db_path = str(AgbaConfig.get_qdrant_storage_path())
    os.makedirs(db_path, exist_ok=True)
    client = QdrantClient(path=db_path)
    collection_name = AgbaConfig.COLLECTION_NAME
    
    # 2. Load Local Embedding Model (384 dim, fast semantic matching)
    print(f"🧠 Loading dense embedding model ({AgbaConfig.EMBEDDING_MODEL_NAME})...")
    model = SentenceTransformer(AgbaConfig.EMBEDDING_MODEL_NAME)
    
    # 3. Load Master Corpus
    corpus_data = load_normalized_corpus()
    
    # Ensure corpus data is a list of entity dictionaries
    if isinstance(corpus_data, dict):
        corpus_items = list(corpus_data.values())
    else:
        corpus_items = corpus_data
        
    print(f"📊 Preparing {len(corpus_items)} normalized entities for vectorization...")
    
    points_to_upsert = []
    
    for idx, item in enumerate(corpus_items):
        if isinstance(item, dict):
            name = item.get("name", item.get("title", f"Entity_{idx}"))
            description = item.get("description", item.get("content", str(item)))
            category = item.get("category", "")
            # Include rich cultural context if present
            social_ctx = item.get("social_and_ritual_context", "")
            text_to_embed = f"{name} ({category}): {description}. {social_ctx}".strip()
            payload = item
        else:
            text_to_embed = str(item)
            payload = {"raw_text": text_to_embed}
            
        vector = model.encode(text_to_embed).tolist()
        
        points_to_upsert.append(
            models.PointStruct(
                id=idx + 1,
                vector=vector,
                payload=payload
            )
        )
    
    print(f"🔄 Upserting {len(points_to_upsert)} vectors into Qdrant collection '{collection_name}'...")
    client.upsert(
        collection_name=collection_name,
        points=points_to_upsert
    )
    
    collection_info = client.get_collection(collection_name=collection_name)
    print("=" * 75)
    print("✨ VECTOR INGESTION & UPSERT COMPLETED SUCCESSFULLY")
    print(f"   - Total Indexed Vectors : {collection_info.points_count}")
    print(f"   - Database Storage Path : {db_path}")
    print("=" * 75)

if __name__ == "__main__":
    AgbaConfig.print_diagnostics()
    # Note: run_vector_ingestion() can be triggered after Step 2 backfill is complete
