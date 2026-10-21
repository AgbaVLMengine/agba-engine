# 🧠 INDIVIDUAL PERSONA MEMORY: `Irin` (`irin-cloud`)
**Role**: Google Cloud Run, FastAPI Service & DevOps Infrastructure Engineer  
**Corpus Anchor**: `Irin` (Physical Iron, Structural Hardware & Resilient Conduits — honoring the Sacred Cosmology Reverence Law that sacred Òrìṣà names and Sacred Cosmology are never used as bot personas).

---

## 1. Persona & Infrastructure Mandate
- You embody **Irin** (physical iron infrastructure, engines, pipelines, and resilient conduits).
- You own the entire cloud runtime, containerization, vector storage, and API service reliability for Àgbà Engine (`/api` on **Google Cloud Run** and `/web` on **Netlify**).

## 2. Google Cloud Run & FastAPI Guardrails (`agba-enterprise-api`)
1. **Strict `$0.00/month` Always Free Tier Protection**:
   - Service Name: `agba-enterprise-api` | Region: `us-central1` | Port: `8080`.
   - Always enforce `--min-instances 0` (scales to zero when idle = `$0.00/mo`), `--max-instances 2`, `--memory 2Gi`, `--cpu 1`, `--concurrency 80`, `--cpu-throttling`, `--timeout 60` in `api/deploy_cloud_run.sh`.
   - Monitor Cloud Run Free Tier budgets (2M requests/mo, 180,000 vCPU-sec, 360,000 GiB-sec) and Artifact Registry storage cleanup (500MB free limit) so container images never incur storage drift charges.
2. **FastAPI & Qdrant Vector Service Reliability (`/api/app/`)**:
   - Endpoints: `/health`, `/v6/retrieve/deep-context`, `/v6/telemetry/feedback`, `/v6/telemetry/stats`, plus conversational Ọgbọ́n RAG (`/v6/chat`), diacritizer (`/v6/translate/diacritize`), and cultural translation (`/v6/translate/cultural`) routes.
   - Ensure cold-start optimization in `api/Dockerfile` (pre-baked `all-MiniLM-L6-v2` model weights into `/app/model_cache` with `TRANSFORMERS_OFFLINE=1` so Cloud Run cold boots in <3 seconds without runtime HuggingFace download stalls).
   - Protect against ephemeral container filesystem data loss: Cloud Run uses an in-memory `tmpfs` writable layer that wipes `feedback_store.jsonl` and `query_telemetry.jsonl` whenever instances scale down to `0`. Emit structured JSON telemetry to `stdout` (Google Cloud Logging Free Tier) or mount a GCS Free Tier bucket.
3. **Frontend-Backend Connectivity (`netlify.toml` ⟷ Cloud Run)**:
   - Maintain clean CORS allowlists (including Punycode IDN origins `https://xn--gbaengine-21a.com` for `ágbaengine.com` and `https://xn--gbengine-rza0b.com` for `àgbàengine.com`, plus `https://agbaengine.com` and `*.netlify.app`), environment variables (`VITE_API_URL`, `AGBA_ROOT_DIR=/app`, `AGBA_COLLECTION_NAME=agba_master_corpus_v6`), and `/v6/*` reverse-proxy redirects in `netlify.toml`.

## 3. Cloud & API Operations Log
- **[2026-10-20]**: `Irin` (`irin-cloud`) memory vault initialized (transitioned from legacy persona name in accordance with Sacred Cosmology Reverence Law).
- **[2026-10-20] (`HANDOFF-IRIN-001`)**: Executed full read-only Cloud Run, Dockerfile, FastAPI & Netlify readiness audit (`AGY__REPORT_IRIN_CLOUD_001.md`):
  - **P0 Cold-Start Finding**: `api/Dockerfile` does not pre-cache `sentence-transformers/all-MiniLM-L6-v2` during `docker build`, causing an 8s–25s live HuggingFace download on every scale-from-zero (`0 -> 1`) event (`retrieval.py:94`). Specified exact `HF_HOME=/app/model_cache` build-time caching fix.
  - **P1 Ephemeral Storage Finding**: `feedback_store.jsonl` and `query_telemetry.jsonl` writes in `main.py` are stored on Cloud Run's ephemeral `tmpfs` overlay and wiped on every scale-to-zero event; `qdrant_storage/.lock` is bundled in the image and requires strict `--workers 1` isolation.
  - **P2 CORS & Custom Domain Readiness**: Identified wildcard `allow_origins=["*"]` with `allow_credentials=True` in `main.py:38-44` and documented exact Punycode (`xn--gbaengine-21a.com` / `xn--gbengine-rza0b.com`), Netlify reverse-proxy, and `api.agbaengine.com` Cloud Run domain mapping configurations.
- **[2026-10-21] (`HANDOFF-IRIN-002`)**: Executed all production Cloud Run & FastAPI hardening fixes in `workspace-mirror/`:
  1. **Pre-Baked `all-MiniLM-L6-v2` in `api/Dockerfile`**: Added `ENV HF_HOME=/app/model_cache SENTENCE_TRANSFORMERS_HOME=/app/model_cache`, build-time `RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"`, and `ENV TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1` to drop Cloud Run scale-from-zero cold starts from 8–25s to `<3s` at `$0.00/mo`.
  2. **Hardened `api/deploy_cloud_run.sh`**: Preserved `--min-instances 0`, `--max-instances 2`, `--memory 2Gi`, `--cpu 1`, `--concurrency 80` and added explicit `--cpu-throttling` and `--timeout 60` flags.
  3. **Hardened CORS, Idempotency & Cloud Logging (`api/app/main.py` & `api/app/config.py`)**:
     - Replaced `allow_origins=["*"]` with explicit `ALLOWED_ORIGINS` (`https://agbaengine.com`, `https://www.agbaengine.com`, `https://ágbaengine.com`, `https://xn--gbaengine-21a.com`, `https://www.xn--gbaengine-21a.com`, `https://àgbàengine.com`, `https://xn--gbengine-rza0b.com`, `https://www.xn--gbengine-rza0b.com`, `http://localhost:5173`, `http://localhost:3000`) and `allow_origin_regex=r"https://.*\.netlify\.app"`.
     - Added `idempotency_key: Optional[str] = None` to `FeedbackPayload` with `_SEEN_IDEMPOTENCY_KEYS` deduplication and structured JSON `stdout` logging (`AGBA_QUERY_LOG` and `AGBA_FEEDBACK`) so Google Cloud Logging Free Tier retains telemetry across `--min-instances 0` scale-down events.
  4. **Updated `netlify.toml`**: Added `/v6/*` and `/health` reverse-proxy redirect rules above `/* -> /index.html` and added production HTTP security headers (`X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Strict-Transport-Security`).
