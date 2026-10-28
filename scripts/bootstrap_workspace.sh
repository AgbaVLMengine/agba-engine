#!/usr/bin/env bash
# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: SOVEREIGN 1-CLICK WORKSPACE BOOTSTRAP SCRIPT
# Role: Disaster Recovery, Zero-Friction Migration & Rapid Environment Restoration
# Ethos: "A kì í fi ọjọ́ ogun dán àdá wò." (One does not test the blade on the day of battle)
# ==============================================================================
set -euo pipefail

echo "=================================================================="
echo "👑 ÀGBÀ ENGINE: SOVEREIGN WORKSPACE BOOTSTRAP & RESTORATION"
echo "📍 Restoring complete development ecosystem on fresh machine..."
echo "=================================================================="

# 1. Environment & Dependency Prerequisites Check
echo "▶ [Step 1/5] Checking System Toolchain..."
command -v git >/dev/null 2>&1 || { echo "❌ Git is required. Install git first."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ Python3 is required. Install python3 first."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "❌ Node/npm is required. Install nodejs & npm first."; exit 1; }

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
NODE_VERSION=$(node --version)
echo "  ✅ Git: $(git --version)"
echo "  ✅ Python: $PYTHON_VERSION"
echo "  ✅ Node: $NODE_VERSION"

# 2. Python Virtual Environment & API Dependencies
echo ""
echo "▶ [Step 2/5] Initializing Python Virtual Environment..."
cd "$(git rev-parse --show-toplevel)"

if [ ! -d "api/.venv" ]; then
  python3 -m venv api/.venv
  echo "  ✅ Created fresh virtual environment at api/.venv"
else
  echo "  ✅ Existing virtual environment detected at api/.venv"
fi

# Source virtual environment and install dependencies
source api/.venv/bin/activate
echo "  📦 Installing / verifying backend dependencies from api/requirements.txt..."
pip install --quiet --upgrade pip
pip install --quiet -r api/requirements.txt
echo "  ✅ Backend dependencies locked."

# 3. Web Client Dependencies (Vite + React)
echo ""
echo "▶ [Step 3/5] Installing Frontend Dependencies..."
cd web
npm install --silent
echo "  ✅ Frontend dependencies installed."
cd ..

# 4. Master Corpus & Knowledge Graph Integrity Check
echo ""
echo "▶ [Step 4/5] Verifying Master Corpus & Knowledge Graph Parity..."
python3 -c "
import json
api_corpus = json.load(open('api/data/yoruba_corpus_1007_NORMALIZED.json'))
web_corpus = json.load(open('web/src/data/yoruba_master_corpus.json'))
assert len(api_corpus) == len(web_corpus), f'Mismatch: {len(api_corpus)} vs {len(web_corpus)}'
print(f'  ✅ Dual-Corpus Parity Verified: {len(api_corpus)} canonical entities loaded.')
"

# 5. Production Gate & Verification Suite
echo ""
echo "▶ [Step 5/5] Running Pre-Flight Production Verification..."
./scripts/review.sh
python3 scripts/benchmark_sprint004.py

echo ""
echo "=================================================================="
echo "🎉 RESTORATION COMPLETE! Àgbà Engine is fully primed and operational."
echo "▶ Run Backend:  cd api && source .venv/bin/activate && uvicorn app.main:app --reload --port 8000"
echo "▶ Run Frontend: cd web && npm run dev"
echo "=================================================================="
