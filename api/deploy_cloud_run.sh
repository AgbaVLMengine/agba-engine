#!/usr/bin/env bash
# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: GOOGLE CLOUD RUN ZERO-COST DEPLOYMENT AUTOMATOR (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Cost Profile: $0.00 / month (Leveraging Google Cloud Always Free Tier & Free Credits)
# - Cloud Run Free Tier: 2 Million requests/month + 360,000 vCPU-seconds + 180 GiB-seconds
# - Auto-scale: min-instances=0 (Zero charges when no requests are being processed)
# ==============================================================================

set -e

SERVICE_NAME="agba-enterprise-api"
REGION="${GCP_REGION:-us-central1}"

echo "================================================================================"
echo "🏛️  ÀGBÀ ENGINE: GOOGLE CLOUD RUN ZERO-COST PRODUCTION DEPLOYMENT"
echo "   - Service Name : $SERVICE_NAME"
echo "   - Region       : $REGION"
echo "   - Architecture : Tri-Modal Cultural Gateway + MLOps Telemetry Loop"
echo "   - Port         : 8080 (Cloud Run default)"
echo "   - Memory       : 2GiB (Fits in Always Free Tier)"
echo "   - Min Instances: 0 (Scales to ZERO when idle = $0.00)"
echo "================================================================================"

# Check if gcloud CLI is installed
if ! command -v gcloud &> /dev/null; then
    echo "⚠️  gcloud CLI not detected in this environment."
    echo "   To deploy from your terminal, Google Cloud Shell, or local workstation:"
    echo "   1. gcloud auth login"
    echo "   2. gcloud config set project YOUR_PROJECT_ID"
    echo "   3. gcloud services enable run.googleapis.com cloudbuild.googleapis.com"
    echo "   4. cd agba_enterprise_api && bash deploy_cloud_run.sh"
    exit 1
fi

PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    echo "❌ No active GCP project configured. Run 'gcloud config set project YOUR_PROJECT_ID' first."
    exit 1
fi

echo "📦 Active GCP Project ID: $PROJECT_ID"
echo "🚀 Building container image and deploying service to Cloud Run..."

gcloud run deploy "$SERVICE_NAME" \
    --source . \
    --region "$REGION" \
    --platform managed \
    --allow-unauthenticated \
    --memory 2Gi \
    --cpu 1 \
    --min-instances 0 \
    --max-instances 2 \
    --concurrency 80 \
    --set-env-vars AGBA_ROOT_DIR=/app,AGBA_COLLECTION_NAME=agba_master_corpus_v6,AGBA_EMBEDDING_MODEL=all-MiniLM-L6-v2

SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" --region "$REGION" --format="value(status.url)")

echo "================================================================================"
echo "🎉 ÀGBÀ ENGINE DEPLOYED SUCCESSFULLY TO GOOGLE CLOUD RUN!"
echo "   - Live Service URL       : $SERVICE_URL"
echo "   - Health Check           : $SERVICE_URL/health"
echo "   - Deep Context Retrieval : $SERVICE_URL/v6/retrieve/deep-context"
echo "   - Telemetry Ingestion    : $SERVICE_URL/v6/telemetry/feedback"
echo "   - Telemetry Stats        : $SERVICE_URL/v6/telemetry/stats"
echo "   - Cost Status            : $0.00 / month (Scales to zero when idle)"
echo "================================================================================"
