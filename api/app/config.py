# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: ENVIRONMENT PORTABILITY & CONFIGURATION (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Dynamic, portable configuration supporting:
#   - ChromeOS Linux container (/mnt/chromeos/shared/MyFiles/Projects /Agba Engine)
#   - Google Colab & Google Drive (/content/drive/MyDrive/...)
#   - Google Cloud Run (Serverless Always-Free Container /app)
#   - Local Docker Compose simulation environment
#   - Arbitrary Linux/macOS environments via dynamic root discovery or env vars
# ==============================================================================

import os
from pathlib import Path
from typing import Dict, Any, Optional, List

def _resolve_root_dir() -> Path:
    """Dynamically resolve the project root by searching for key anchor directories."""
    candidate_roots = [
        os.environ.get("AGBA_ROOT_DIR"),
        str(Path(__file__).resolve().parent.parent.parent),  # .../agba_enterprise_api/app -> .../Projects /Agba Engine
        str(Path(__file__).resolve().parent.parent),         # In case agba_enterprise_api is root
        "/mnt/chromeos/shared/MyFiles/Projects /Agba Engine",
        "/mnt/chromeos/shared/MyFiles/Projects/Agba Engine",
        "/content/drive/MyDrive/Projects /Agba Engine",
        "/content/drive/MyDrive/agba_enterprise_api",
        "/app",                                              # Docker container root
        os.getcwd()
    ]
    for candidate in candidate_roots:
        if not candidate:
            continue
        path = Path(candidate).resolve()
        # An anchor exists if agba_engine_backups or Agba_Golden_Matrix is present
        if (path / "agba_engine_backups").exists() or (path / "Agba_Golden_Matrix").exists():
            return path
        # Or if this directory is agba_enterprise_api itself containing qdrant_storage or data
        if ((path / "qdrant_storage").exists() or (path / "data").exists()) and (path / "app").exists():
            return path
    
    # Fallback to grandparent of this config file
    return Path(__file__).resolve().parent.parent.parent

class ÀgbàConfig:
    """
    Centralized, portable configuration for Àgbà Engine.
    Discovers asset paths dynamically without hardcoded environment assumptions.
    Maintains strict 25-letter Yorùbá canonical orthography.
    """
    # 1. Dynamically resolved root
    ROOT_DIR: Path = _resolve_root_dir()

    # 2. Database & Corpus Paths
    COLLECTION_NAME: str = os.environ.get("AGBA_COLLECTION_NAME", "agba_master_corpus_v6")
    EMBEDDING_MODEL_NAME: str = os.environ.get("AGBA_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    
    @classmethod
    def get_qdrant_storage_path(cls) -> Path:
        """Resolve persistent Qdrant directory."""
        custom_path = os.environ.get("AGBA_QDRANT_PATH")
        if custom_path and Path(custom_path).exists():
            return Path(custom_path)
            
        candidates = [
            cls.ROOT_DIR / "agba_enterprise_api" / "qdrant_storage",
            cls.ROOT_DIR / "qdrant_storage",
            Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_enterprise_api/qdrant_storage"),
            Path("/content/drive/MyDrive/agba_enterprise_api/qdrant_storage"),
            Path("/app/qdrant_storage")
        ]
        for p in candidates:
            if p.exists():
                return p
        # If not existing yet, create default in agba_enterprise_api
        default_p = cls.ROOT_DIR / "agba_enterprise_api" / "qdrant_storage"
        default_p.mkdir(parents=True, exist_ok=True)
        return default_p

    @classmethod
    def get_normalized_corpus_path(cls) -> Path:
        """Resolve path to the 970/1007 normalized master corpus JSON."""
        custom_path = os.environ.get("AGBA_CORPUS_PATH")
        if custom_path and Path(custom_path).exists():
            return Path(custom_path)
            
        candidates = [
            cls.ROOT_DIR / "Agba_Engine_Foundational_Vault" / "02_Master_Corpus_&_Taxonomy" / "yoruba_corpus_1007_NORMALIZED.json",
            cls.ROOT_DIR / "agba_enterprise_api" / "data" / "yoruba_corpus_1007_NORMALIZED.json",
            cls.ROOT_DIR / "data" / "yoruba_corpus_1007_NORMALIZED.json",
            Path("/app/data/yoruba_corpus_1007_NORMALIZED.json"),
            cls.ROOT_DIR / "agba_engine_backups" / "yoruba_corpus_1007_NORMALIZED.json",
            cls.ROOT_DIR / "agba_engine_backups" / "yoruba_corpus_1007_ENRICHED.json",
            cls.ROOT_DIR / "agba_engine_backups" / "yoruba_corpus_1007_CLEANED.json",
            Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_engine_backups/yoruba_corpus_1007_NORMALIZED.json"),
            Path("/content/drive/MyDrive/agba_engine_backups/yoruba_corpus_1007_NORMALIZED.json")
        ]
        for p in candidates:
            if p.exists():
                return p
        raise FileNotFoundError(f"Normalized corpus not found in any candidate location from root: {cls.ROOT_DIR}")

    @classmethod
    def get_golden_matrix_dir(cls) -> Path:
        """Resolve Agba_Golden_Matrix assets directory."""
        candidates = [
            cls.ROOT_DIR / "Agba_Golden_Matrix",
            cls.ROOT_DIR / "agba_enterprise_api" / "data",
            cls.ROOT_DIR / "data",
            Path("/app/data"),
            Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/Agba_Golden_Matrix"),
            Path("/content/drive/MyDrive/Projects /Agba Engine/Agba_Golden_Matrix")
        ]
        for p in candidates:
            if p.exists():
                return p
        return cls.ROOT_DIR / "Agba_Golden_Matrix"

    @classmethod
    def get_feedback_store_path(cls) -> Path:
        """Resolve persistent telemetry feedback store JSONL."""
        candidates = [
            cls.ROOT_DIR / "agba_enterprise_api" / "feedback_store.jsonl",
            cls.ROOT_DIR / "feedback_store.jsonl",
            Path("/app/feedback_store.jsonl"),
            Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_enterprise_api/feedback_store.jsonl")
        ]
        for p in candidates:
            if p.exists():
                return p
        default_p = cls.ROOT_DIR / "agba_enterprise_api" / "feedback_store.jsonl"
        default_p.parent.mkdir(parents=True, exist_ok=True)
        return default_p

    @classmethod
    def get_query_store_path(cls) -> Path:
        """Resolve persistent query telemetry store JSONL."""
        candidates = [
            cls.ROOT_DIR / "agba_enterprise_api" / "query_telemetry.jsonl",
            cls.ROOT_DIR / "query_telemetry.jsonl",
            Path("/app/query_telemetry.jsonl"),
            Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_enterprise_api/query_telemetry.jsonl")
        ]
        for p in candidates:
            if p.exists():
                return p
        default_p = cls.ROOT_DIR / "agba_enterprise_api" / "query_telemetry.jsonl"
        default_p.parent.mkdir(parents=True, exist_ok=True)
        return default_p

    @classmethod
    def get_pending_candidates_path(cls) -> Path:
        """Resolve pending self-learning candidate queue JSON."""
        candidates = [
            cls.ROOT_DIR / "agba_enterprise_api" / "pending_candidates.json",
            cls.ROOT_DIR / "pending_candidates.json",
            Path("/app/pending_candidates.json")
        ]
        for p in candidates:
            if p.exists():
                return p
        return cls.ROOT_DIR / "agba_enterprise_api" / "pending_candidates.json"

    # 3. Security & Telemetry Configurations
    API_KEY_NAMES: List[str] = ["X-AGBA-API-KEY", "X-ÀGBÀ-API-KEY", "x-agba-api-key"]
    API_KEY_NAME: str = "X-AGBA-API-KEY"
    
    # Authorized client registry with tiered access
    VALID_API_KEYS: Dict[str, Dict[str, Any]] = {
        "agba_studio_dev_key_2026": {
            "tier": "Studio",
            "owner": "Aruna Olanrewaju Kabiru",
            "rate_limit_rpm": 300,
            "permissions": ["text", "vision", "audio", "export_dossier"]
        },
        "àgbà_studio_dev_key_2026": {
            "tier": "Studio",
            "owner": "Aruna Olanrewaju Kabiru",
            "rate_limit_rpm": 300,
            "permissions": ["text", "vision", "audio", "export_dossier"]
        },
        "agba_enterprise_demo_key": {
            "tier": "Institutional",
            "owner": "Aruna Olanrewaju Kabiru",
            "rate_limit_rpm": 120,
            "permissions": ["text", "vision", "audio"]
        },
        "àgbà_enterprise_demo_key": {
            "tier": "Institutional",
            "owner": "Aruna Olanrewaju Kabiru",
            "rate_limit_rpm": 120,
            "permissions": ["text", "vision", "audio"]
        },
        "agba_academic_research_key": {
            "tier": "Academic",
            "owner": "Aruna Olanrewaju Kabiru",
            "rate_limit_rpm": 60,
            "permissions": ["text", "vision"]
        },
        "àgbà_academic_research_key": {
            "tier": "Academic",
            "owner": "Aruna Olanrewaju Kabiru",
            "rate_limit_rpm": 60,
            "permissions": ["text", "vision"]
        }
    }

    # 4. Diagnostic & Status Reporting
    @classmethod
    def print_diagnostics(cls) -> None:
        """Print clean initialization diagnostic report."""
        print("=" * 80)
        print("🏛️  ÀGBÀ ENGINE: CONFIGURATION & ENVIRONMENT DIAGNOSTICS")
        print("   - Lead Architect : Aruna Olanrewaju Kabiru")
        print("   - Version        : v6.1.0 (Cloud Run & Container Ready)")
        print("=" * 80)
        print(f"📁 Project Root Dir    : {cls.ROOT_DIR}")
        print(f"📂 Normalized Corpus   : {cls.get_normalized_corpus_path()}")
        print(f"🗄️  Qdrant Storage     : {cls.get_qdrant_storage_path()}")
        print(f"👑 Golden Matrix Dir   : {cls.get_golden_matrix_dir()}")
        print(f"📊 Feedback Store      : {cls.get_feedback_store_path()}")
        print(f"🧠 Embedding Model     : {cls.EMBEDDING_MODEL_NAME}")
        print(f"📦 Vector Collection   : {cls.COLLECTION_NAME}")
        print(f"🔑 Auth Header Name    : {cls.API_KEY_NAME}")
        print(f"🛡️  Registered Keys    : {len(cls.VALID_API_KEYS)} Tiered Keys Active")
        print("=" * 80)

# Backward-compatible ASCII alias
AgbaConfig = ÀgbàConfig

if __name__ == "__main__":
    ÀgbàConfig.print_diagnostics()
