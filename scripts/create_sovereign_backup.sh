#!/usr/bin/env bash
# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: SOVEREIGN AIR-GAPPED BACKUP GENERATOR (PILLAR B)
# Role: Creates standalone, compressed, and checksummed archives of the entire
#       knowledge graph, multi-agent brain, legal dossiers, and corpora.
# Ethos: "A kì í fi owó kan gbágun." (One does not wage war with a single hand)
# ==============================================================================
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
TIMESTAMP=$(date -u +"%Y%m%d_%H%M%SZ")
BACKUP_DIR="$REPO_ROOT/backups"
ARCHIVE_BASE="agba_engine_sovereign_vault_$TIMESTAMP"
TAR_FILE="$BACKUP_DIR/${ARCHIVE_BASE}.tar.gz"
ZIP_FILE="$BACKUP_DIR/${ARCHIVE_BASE}.zip"
CHECKSUM_FILE="$BACKUP_DIR/${ARCHIVE_BASE}_SHA256.txt"

echo "=================================================================="
echo "👑 ÀGBÀ ENGINE: AIR-GAPPED SOVEREIGN VAULT GENERATION"
echo "📍 Target Archive: $ARCHIVE_BASE"
echo "=================================================================="

mkdir -p "$BACKUP_DIR"

cd "$REPO_ROOT"

echo "▶ [Step 1/4] Archiving Knowledge Graph, Brain & Legal Vaults..."
# Bundle core intellectual property:
# 1. api/data (Normalized 14-Tier Master Corpora)
# 2. web/src/data (Unified visual manifests & client datasets)
# 3. .agents (Shared Brain, Checkpoints Ledger, Memory Vaults, Local Seeds)
# 4. docs (Legal Briefs, Safe Harbor Protocol, Victory Chronicles)
# 5. Core root files (LEAD_ARCHITECT_AUDIT_LOG.md, LICENSE, README.md)

tar -czf "$TAR_FILE" \
  api/data \
  web/src/data \
  .agents \
  docs \
  LEAD_ARCHITECT_AUDIT_LOG.md \
  LICENSE \
  README.md

echo "  ✅ Tarball generated: $TAR_FILE"

echo ""
echo "▶ [Step 2/4] Generating Universal ZIP Archive (iOS / Windows / Mac)..."
if command -v zip >/dev/null 2>&1; then
  zip -r -q "$ZIP_FILE" \
    api/data \
    web/src/data \
    .agents \
    docs \
    LEAD_ARCHITECT_AUDIT_LOG.md \
    LICENSE \
    README.md
  echo "  ✅ ZIP archive generated: $ZIP_FILE"
else
  echo "  ℹ️ 'zip' command not found; using tarball as primary archive."
fi

echo ""
echo "▶ [Step 3/4] Generating Cryptographic SHA256 Checksums..."
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$TAR_FILE" > "$CHECKSUM_FILE"
  [ -f "$ZIP_FILE" ] && sha256sum "$ZIP_FILE" >> "$CHECKSUM_FILE"
elif command -v shasum >/dev/null 2>&1; then
  shasum -a 256 "$TAR_FILE" > "$CHECKSUM_FILE"
  [ -f "$ZIP_FILE" ] && shasum -a 256 "$ZIP_FILE" >> "$CHECKSUM_FILE"
fi
cat "$CHECKSUM_FILE"

echo ""
echo "▶ [Step 4/4] Archival Health & Size Verification..."
TAR_SIZE=$(du -h "$TAR_FILE" | cut -f1)
echo "  💾 Compressed Vault Size: $TAR_SIZE"
echo ""
echo "=================================================================="
echo "🎉 SOVEREIGN VAULT CREATED SUCCESSFULLY!"
echo "📍 Files located in: $BACKUP_DIR/"
echo "📱 Transfer options to iPhone 15 Pro Max:"
echo "   1. USB-C Cable direct to Files -> On My iPhone"
echo "   2. AirDrop / iCloud Drive / Google Drive"
echo "=================================================================="
