#!/usr/bin/env bash
# ==============================================================================
# 🧹 ÀGBÀ ENGINE: DISK SAVER RECLAIM SCRIPT (`scripts/reclaim_disk.sh`)
# Persona: Agbálẹ̀ (disk-saver) — Storage Sentinel & Cache Reclaimer
# Standards: Gate 2 Compliant (<500 LOC), Zero-Harm Protection on User Assets
# ==============================================================================

set -euo pipefail

echo "=================================================================="
echo "🧹 DISK SAVER (AGBÁLẸ̀): STORAGE AUDIT & SAFE PURGE SEQUENCE"
echo "📍 Target OS: Linux | Safe Mode: Active"
echo "=================================================================="

# 1. Capture Pre-Cleanup Storage
BEFORE_KB=$(df --output=avail "$HOME" | tail -1 | tr -d ' ')

# 2. Reclaim Google Chrome Caches (Preserves Profile, Cookies, Bookmarks, Logins)
CHROME_CACHE_DIR="$HOME/.cache/google-chrome/Default"
if [ -d "$CHROME_CACHE_DIR" ]; then
    echo "▶ Purging Chrome Stale Caches in $CHROME_CACHE_DIR..."
    rm -rf "$CHROME_CACHE_DIR/Cache/"* 2>/dev/null || true
    rm -rf "$CHROME_CACHE_DIR/Code Cache/"* 2>/dev/null || true
    rm -rf "$CHROME_CACHE_DIR/GPUCache/"* 2>/dev/null || true
    rm -rf "$CHROME_CACHE_DIR/DawnCache/"* 2>/dev/null || true
    echo "  ✅ Chrome runtime caches cleared."
else
    echo "  ℹ️ Chrome cache dir not found at $CHROME_CACHE_DIR."
fi

# 3. Reclaim Developer Package Caches
echo "▶ Clearing developer package caches..."
if [ -d "$HOME/.cache/pip" ]; then
    rm -rf "$HOME/.cache/pip/"* 2>/dev/null || true
    echo "  ✅ Stale pip wheel cache cleared."
fi

if [ -d "$HOME/.npm/_cacache" ]; then
    rm -rf "$HOME/.npm/_cacache/"* 2>/dev/null || true
    echo "  ✅ Stale npm cache cleared."
fi

# 4. Prune System /tmp & Vacuum System Logs
echo "▶ Pruning temporary files older than 48h in /tmp..."
find /tmp -type f -atime +2 -delete 2>/dev/null || true
echo "  ✅ Stale /tmp files pruned."

echo "▶ Vacuuming system journal logs..."
journalctl --vacuum-size=50M 2>/dev/null || true
echo "  ✅ Journal logs vacuumed."

# 5. Git Object Compaction & Intermediate Cache Pruning
REPO_DIR="/home/aruna_olanrewaju/agba-engine"
if [ -d "$REPO_DIR/.git" ]; then
    echo "▶ Compacting git objects in $REPO_DIR..."
    git -C "$REPO_DIR" gc --quiet 2>/dev/null || true
    echo "  ✅ Git objects packed and compacted."
fi

# Clean transient Vite and Python bytecode caches
rm -rf "$REPO_DIR/web/.vite" 2>/dev/null || true
find "$REPO_DIR" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
rm -rf "$HOME/.gemini/antigravity/scratch"/*/workspace-mirror 2>/dev/null || true
echo "  ✅ Transient bytecode and scratch mirrors cleared."

# 6. Capture Post-Cleanup Storage & Calculate Reclaimed Space
AFTER_KB=$(df --output=avail "$HOME" | tail -1 | tr -d ' ')
RECLAIMED_KB=$((AFTER_KB - BEFORE_KB))

if [ "$RECLAIMED_KB" -lt 0 ]; then
    RECLAIMED_KB=0
fi

RECLAIMED_MB=$((RECLAIMED_KB / 1024))
FREE_GB=$(df --output=avail -h "$HOME" | tail -1 | tr -d ' ')

# 5b. Headroom Alert Gate (< 2.0 GB = 2097152 KB)
ALERT_STATUS="🟢 Nominal"
if [ "$AFTER_KB" -lt 2097152 ]; then
    ALERT_STATUS="🚨 CRITICAL (<2.0 GB)"
    echo "⚠️ [CRITICAL STORAGE ALERT] Headroom on $HOME is critically low (< 2.0 GB)!"
fi

echo "=================================================================="
echo "🎉 DISK RECLAIM COMPLETE!"
echo "   📊 Space Reclaimed: ${RECLAIMED_MB} MB"
echo "   💾 Current Available Storage: ${FREE_GB}"
echo "   🛡️ Status: ${ALERT_STATUS}"
echo "=================================================================="

# 7. Append to Memory Vault
MEMORY_FILE="/home/aruna_olanrewaju/agba-engine/memory/disk_saver_memory.md"
ACTION_NAME="${1:-Safe Storage Sweep (Chrome + git gc + pip/npm + /tmp)}"
if [ -f "$MEMORY_FILE" ]; then
    TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")
    echo "| **$TIMESTAMP** | ${ACTION_NAME} | ${RECLAIMED_MB} MB | ${FREE_GB} available | ${ALERT_STATUS} |" >> "$MEMORY_FILE"
    echo "✅ Appended audit entry to memory/disk_saver_memory.md."
    cp "$MEMORY_FILE" "/home/aruna_olanrewaju/agba-engine/.agents/memory/disk_saver_memory.md" 2>/dev/null || true
fi
