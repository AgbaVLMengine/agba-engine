# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: ENTERPRISE API GATEWAY - GOOGLE CLOUD RUN DOCKERFILE (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Target Platform: Google Cloud Run (Serverless Container - Always Free Tier)
# Cost Profile: $0.00/month (Scales down to 0 instances when idle)
# Architecture: Tri-Modal Cultural Retrieval + MLOps Telemetry Loop
# ==============================================================================

FROM python:3.11-slim

# Set environment variables for production performance and UTF-8 encoding
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    AGBA_ROOT_DIR=/app \
    PYTHONPATH=/app \
    PYTHONIOENCODING=utf-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

WORKDIR /app

# Install minimal OS dependencies for network and SSL
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU first to minimize container size (saving ~1.5GB of CUDA bloat)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code, bundled cultural data, and local storage
COPY app/ ./app/
COPY data/ ./data/
COPY qdrant_storage/ ./qdrant_storage/
COPY feedback_store.jsonl ./feedback_store.jsonl

# Create directories for runtime logging and telemetry
RUN mkdir -p /app/agba_enterprise_api /app/agba_engine_backups

# Expose port (Cloud Run dynamically sets $PORT, default 8080)
EXPOSE 8080

# Health check endpoint for Cloud Run container liveness probe
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8080}/health || exit 1

# Launch production Uvicorn server with dynamic port resolution
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --workers 1
