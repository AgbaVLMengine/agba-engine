# ==============================================================================
# 🎙️ ÀGBÀ ENGINE: OPEN-ACCESS AUDIO STREAMING & B2B ANTI-SCRAPING GATEWAY
# ==============================================================================
# Handoff: HANDOFF-IRIN-003 (Craigslist Open-Access Audio + $0.00/mo Guardrails)
# Persona: Ọlọ́yè Irin (irin-cloud) | Supervised by: Ọlọ́yè Àgbà
# Invariant:
#   - 100% Free, Zero-Key Streaming for Web & Mobile Seekers (Aggressive Edge Cache)
#   - Per-IP Sliding-Window Rate Limiter against Bulk Automated Scraping
#   - Multi-Token Batch Export strictly reserved for Enterprise X-AGBA-API-KEY
# ==============================================================================

import json
import time
import unicodedata
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Deque, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Query, Request, Response, status
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

try:
    from .config import ÀgbàConfig
except (ImportError, ValueError):
    try:
        from app.config import ÀgbàConfig
    except ImportError:
        from config import ÀgbàConfig

audio_router = APIRouter(prefix="/v6/audio", tags=["Acoustic Sovereignty Gateway"])

def _resolve_audio_manifest_path() -> Path:
    candidates = [
        getattr(ÀgbàConfig, "DATA_DIR", Path(__file__).resolve().parent.parent / "data") / "agba_audio_manifest.json",
        Path("/app/data/agba_audio_manifest.json"),
        Path(__file__).resolve().parent.parent / "data" / "agba_audio_manifest.json",
    ]
    for c in candidates:
        if c.exists():
            return c
    return Path(__file__).resolve().parent.parent / "data" / "agba_audio_manifest.json"

AUDIO_MANIFEST_PATH = _resolve_audio_manifest_path()
LOCAL_STEMS_DIR = Path.home() / "YemiVoiceNotes" / "processed_stems"

# Per-IP sliding window rate limiter for unauthenticated public streams (30 req / 60s)
RATE_WINDOW_SEC = 60.0
MAX_UNAUTH_STREAMS_PER_MIN = 30
_IP_STREAM_LOG: Dict[str, Deque[float]] = defaultdict(deque)

EDGE_STREAM_HEADERS = {
    "Cache-Control": "public, max-age=31536000, s-maxage=31536000, immutable",
    "CDN-Cache-Control": "public, max-age=31536000, immutable",
    "Netlify-CDN-Cache-Control": "public, max-age=31536000, durable, immutable",
    "X-Content-Type-Options": "nosniff",
    "X-Agba-Access-Tier": "Public-Sanctuary-Open-Stream",
}

# In-memory manifest cache with mtime invalidation (Irin Edge Optimization)
_MANIFEST_CACHE: List[Dict[str, Any]] = []
_MANIFEST_MTIME: float = 0.0


def _ascii_header(val: str) -> str:
    """Encode unicode strings to ASCII-safe representation for HTTP headers to prevent Latin-1 encoding crash (RFC 7230)."""
    nfd = unicodedata.normalize("NFD", str(val).strip())
    ascii_clean = "".join(c for c in nfd if unicodedata.category(c) != "Mn")
    return ascii_clean.encode("ascii", "ignore").decode("ascii")


def _norm(text: str) -> str:
    nfd = unicodedata.normalize("NFD", str(text).strip().lower())
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn")


def _load_manifest() -> List[Dict[str, Any]]:
    """Cached manifest loader guarded by file modification time."""
    global _MANIFEST_CACHE, _MANIFEST_MTIME
    if not AUDIO_MANIFEST_PATH.exists():
        return []
    try:
        current_mtime = AUDIO_MANIFEST_PATH.stat().st_mtime
        if current_mtime != _MANIFEST_MTIME or not _MANIFEST_CACHE:
            _MANIFEST_CACHE = json.loads(AUDIO_MANIFEST_PATH.read_text(encoding="utf-8"))
            _MANIFEST_MTIME = current_mtime
        return _MANIFEST_CACHE
    except Exception:
        return _MANIFEST_CACHE or []


def _enforce_stream_rate_limit(request: Request) -> None:
    """Protect against automated bulk audio scraping while allowing frictionless human playback."""
    forwarded = request.headers.get("x-forwarded-for")
    client_ip = forwarded.split(",")[0].strip() if forwarded else (request.client.host if request.client else "local")
    now = time.time()
    bucket = _IP_STREAM_LOG[client_ip]
    while bucket and (now - bucket[0]) > RATE_WINDOW_SEC:
        bucket.popleft()
    if len(bucket) >= MAX_UNAUTH_STREAMS_PER_MIN:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded (30 streams/min). Automated bulk scraping of ancestral voice stems is prohibited under RAIL-Cultural-Heritage-v1.0. Authenticate with X-AGBA-API-KEY for enterprise batch access.",
        )
    bucket.append(now)


def _require_enterprise_export_key(request: Request) -> Dict[str, Any]:
    """Verify X-AGBA-API-KEY with 'export_dossier' permission for bulk B2B audio exports."""
    key = (
        request.headers.get("x-agba-api-key")
        or request.headers.get("x-àgbà-api-key")
        or request.headers.get("authorization", "").replace("Bearer ", "")
    )
    client_info = ÀgbàConfig.VALID_API_KEYS.get(key or "")
    if not client_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bulk multi-token audio export requires a valid Enterprise X-AGBA-API-KEY header.",
        )
    if "export_dossier" not in client_info.get("permissions", []):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Key tier '{client_info.get('tier')}' does not hold bulk studio master export privileges. Individual streaming remains free via /v6/audio/stream/{{token_id}}.",
        )
    return client_info


class BatchAudioExportRequest(BaseModel):
    token_ids: List[str] = Field(..., min_length=1, max_length=150, description="List of audio token IDs for enterprise batch export")


@audio_router.get("/stream/{token_id}")
async def stream_audio_token(token_id: str, request: Request):
    """
    Zero-friction, unauthenticated audio token & Auntie Yẹmí voice note stream for Web & Mobile UI.
    Uses 1-year immutable Edge Caching headers so Netlify CDN absorbs repeat plays at $0.00/mo Cloud Run scale.
    """
    _enforce_stream_rate_limit(request)
    target_norm = _norm(token_id)
    manifest = _load_manifest()

    matched = next(
        (
            item for item in manifest
            if _norm(item.get("id", "")) == target_norm
            or _norm(item.get("file_name", "")) == target_norm
            or _norm(item.get("entity_id", "")) == target_norm
        ),
        None,
    )
    if not matched:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Audio token '{token_id}' not found in acoustic manifest.")

    file_name = matched.get("file_name", "")
    custodian = matched.get("category", "Sovereign-Acoustic-Custodian")
    token_str_id = str(matched.get("id", token_id))

    stream_headers = dict(EDGE_STREAM_HEADERS)
    stream_headers["X-Acoustic-Performer"] = _ascii_header(custodian)
    stream_headers["X-Acoustic-Token-Id"] = _ascii_header(token_str_id)

    local_candidate = LOCAL_STEMS_DIR / file_name
    if local_candidate.exists() and local_candidate.is_file():
        media_type = "audio/mpeg" if local_candidate.suffix == ".mp3" else ("audio/ogg" if local_candidate.suffix in (".opus", ".ogg") else "audio/wav")
        return FileResponse(path=str(local_candidate), media_type=media_type, headers=stream_headers)

    return JSONResponse(
        content={
            "status": "stream_ready",
            "access_model": "Craigslist-Open-Sanctuary (No API Key Required)",
            "token": matched,
        },
        headers=stream_headers,
    )


@audio_router.get("/tokens")
async def list_or_lookup_audio_tokens(
    request: Request,
    response: Response,
    entity: Optional[str] = Query(None, max_length=200, description="Entity title or ID to look up audio stems freely"),
):
    """
    Open-access entity audio lookup when `?entity=` is supplied.
    Unfiltered full-catalog dumps require an authenticated Enterprise X-AGBA-API-KEY.
    """
    manifest = _load_manifest()
    if entity:
        _enforce_stream_rate_limit(request)
        q_norm = _norm(entity)
        matches = [
            item for item in manifest
            if q_norm in _norm(item.get("id", ""))
            or q_norm in _norm(item.get("entity_id", ""))
            or q_norm in _norm(item.get("entity_title", ""))
            or q_norm in _norm(item.get("file_name", ""))
        ]
        response.headers.update({
            "Cache-Control": "public, max-age=86400, s-maxage=86400",
            "X-Agba-Access-Tier": "Public-Sanctuary-Entity-Lookup",
            "X-Entity-Query": _ascii_header(entity),
        })
        return {"status": "success", "entity_query": entity, "count": len(matches), "tokens": matches}

    client_info = _require_enterprise_export_key(request)
    return {
        "status": "enterprise_catalog_export",
        "authorized_tier": client_info.get("tier"),
        "total_tokens": len(manifest),
        "tokens": manifest,
    }


@audio_router.post("/batch-export")
async def enterprise_batch_audio_export(payload: BatchAudioExportRequest, request: Request):
    """Strictly authenticated Enterprise B2B multi-token batch export (`X-AGBA-API-KEY` required)."""
    client_info = _require_enterprise_export_key(request)
    manifest = _load_manifest()
    requested_norms = {_norm(tid) for tid in payload.token_ids}
    exported = [item for item in manifest if _norm(item.get("id", "")) in requested_norms]
    return {
        "status": "enterprise_batch_export_ready",
        "authorized_tier": client_info.get("tier"),
        "owner": client_info.get("owner"),
        "license": "RAIL-Cultural-Heritage-v1.0 (Commercial Enterprise B2B)",
        "exported_count": len(exported),
        "tokens": exported,
    }
