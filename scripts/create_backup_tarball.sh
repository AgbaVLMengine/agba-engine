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

# Enforce Strict 3-Snapshot Rolling Retention in Local backups/
for old_tar in $(ls -1t "${BACKUP_DIR}"/agba_engine_snapshot_*.tar.gz 2>/dev/null | tail -n +4); do
  base="${old_tar%.tar.gz}"
  rm -f "${base}.tar.gz" "${base}.sha256"
  echo "🧹 Pruned older local snapshot: $(basename "${base}")"
done

# Auto-Sync to Google Drive & Enforce Strict 3-Snapshot Rolling Retention
GDRIVE_CANDIDATES=(
  "/mnt/chromeos/GoogleDrive/MyDrive/AgbaEngineBackups"
  "/mnt/shared/GoogleDrive/MyDrive/AgbaEngineBackups"
  "/mnt/chromeos/removable/AgbaEngineBackups"
  "/home/aruna_olanrewaju/GoogleDrive/AgbaEngineBackups"
)

GDRIVE_SYNCED=0
for GDRIVE_DIR in "${GDRIVE_CANDIDATES[@]}"; do
  if [ -d "${GDRIVE_DIR}" ]; then
    cp "${BACKUP_DIR}/${ARCHIVE_NAME}" "${BACKUP_DIR}/${CHECKSUM_NAME}" "${GDRIVE_DIR}/"
    for old_gd_tar in $(ls -1t "${GDRIVE_DIR}"/agba_engine_snapshot_*.tar.gz 2>/dev/null | tail -n +4); do
      gd_base="${old_gd_tar%.tar.gz}"
      rm -f "${gd_base}.tar.gz" "${gd_base}.sha256"
      echo "🧹 Rotated out oldest Google Drive snapshot: $(basename "${gd_base}")"
    done
    echo "☁️  Synced to Google Drive (${GDRIVE_DIR}) — Strict 3-Backup Cap Verified."
    GDRIVE_SYNCED=1
    break
  fi
done

if [ "$GDRIVE_SYNCED" -eq 0 ]; then
  echo "⚠️  Google Drive external mount not active. Snapshot securely retained in local backups/."
  echo "    To mirror to Google Drive, right-click 'AgbaEngineBackups' in ChromeOS Files app and select 'Share with Linux'."
fi
echo "=================================================================="
