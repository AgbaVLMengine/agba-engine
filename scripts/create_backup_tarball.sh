#!/usr/bin/env bash
# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: DETERMINISTIC SPHERE 4 ARCHIVE SNAPSHOT GENERATOR
# ==============================================================================
# Custodian: Àsúnwọ̀n (`asunwon-ledger`) | Supervising Architect: Àgbà
# Standard: Gate 5 Compliant (Excludes node_modules, .git, venv, caches)
# ==============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKUP_DIR="${REPO_ROOT}/backups"
TIMESTAMP="$(date +"%Y%m%d_%H%M%S")"
ARCHIVE_NAME="agba_engine_snapshot_${TIMESTAMP}.tar.gz"
CHECKSUM_NAME="agba_engine_snapshot_${TIMESTAMP}.sha256"

mkdir -p "${BACKUP_DIR}"

echo "=================================================================="
echo "⚖️  ÀSÚNWỌ̀N ARCHIVE SENTINEL: GENERATING SPHERE 4 SNAPSHOT"
echo "📍 Source Repository: ${REPO_ROOT}"
echo "📦 Target Archive:    ${BACKUP_DIR}/${ARCHIVE_NAME}"
echo "=================================================================="

# Create clean tarball excluding node_modules, git objects, and virtualenvs
tar -czf "${BACKUP_DIR}/${ARCHIVE_NAME}" \
  -C "${REPO_ROOT}" \
  --exclude=".git" \
  --exclude="node_modules" \
  --exclude=".venv" \
  --exclude="__pycache__" \
  --exclude="dist" \
  --exclude="build" \
  --exclude="*.pyc" \
  --exclude="backups" \
  .

# Compute cryptographic SHA-256 checksum for immutable ledger balancing
cd "${BACKUP_DIR}"
sha256sum "${ARCHIVE_NAME}" > "${CHECKSUM_NAME}"
CHECKSUM="$(cut -d ' ' -f 1 "${CHECKSUM_NAME}")"

echo "✅ Snapshot Generated Successfully!"
echo "📄 Archive File:   ${BACKUP_DIR}/${ARCHIVE_NAME}"
echo "🔑 SHA-256 Hash:   ${CHECKSUM}"
echo "📁 File Size:      $(du -h "${BACKUP_DIR}/${ARCHIVE_NAME}" | cut -f 1)"
echo ""
echo "☁️  TO SYNC TO GOOGLE DRIVE:"
echo "   1. If Google Drive is shared with Linux, copy to /mnt/chromeos/GoogleDrive/MyDrive/AgbaEngineBackups/"
echo "   2. Or drag '${ARCHIVE_NAME}' into Google Drive in your Chrome browser."
echo "=================================================================="
