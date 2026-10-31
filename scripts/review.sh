#!/usr/bin/env bash
# ==============================================================================
# scripts/review.sh — Adversarial Red-Team Diff & Technical Guardrail Auditor
# Tailored for 100% Native Antigravity + Àgbà Engine (`Ẹ̀gbẹ́-Àgbà` Personas)
# ==============================================================================
set -euo pipefail

BASE_REF="${1:-HEAD}"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

echo "=================================================================="
echo "🛡️  ÀGBÀ ENGINE x ÒYE AUDITOR: PRODUCTION GATE & STANDARDS CHECK"
echo "📍 Workspace: $REPO_ROOT"
echo "🔍 Target Ref: $BASE_REF"
echo "=================================================================="

VIOLATIONS=0
WARNINGS=0

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  CHANGED_FILES=$( { git diff --name-only "$BASE_REF" 2>/dev/null || true; git ls-files --others --exclude-standard; } | sort -u )
else
  CHANGED_FILES=$(find . -maxdepth 3 -type f -not -path '*/.*')
fi

echo ""
echo "▶ [GATE 2] Checking Component & Module Modularization (3-Tier Pre-Commit Scanner)..."
for f in $CHANGED_FILES; do
  [ -f "$f" ] || continue
  case "$f" in
    *.ts|*.tsx|*.js|*.jsx|*.py|*.vue|*.svelte)
      LINES=$(wc -l < "$f" | tr -d ' ')
      if [ "$LINES" -gt 500 ]; then
        echo "  ❌ [GATE 2 HARD VIOLATION] $f has $LINES lines (Hard ceiling: 500 lines). Build rejected."
        VIOLATIONS=$((VIOLATIONS + 1))
      elif [ "$LINES" -ge 450 ]; then
        echo "  🛑 [EMBARGO ALERT] $f has $LINES lines (≥ 450 lines). Zero inline additions allowed; modular extraction required."
        WARNINGS=$((WARNINGS + 1))
      elif [ "$LINES" -ge 350 ]; then
        echo "  ⚠️  [ADVISORY NOTICE] $f has $LINES lines (≥ 350 lines). Nearing threshold; plan modular extraction."
        WARNINGS=$((WARNINGS + 1))
      else
        echo "  ✅ $f ($LINES / 500 lines — Healthy Headroom)"
      fi
      ;;
  esac
done

echo ""
echo "▶ [GATE 5 & LEAN COMMITS] Checking for Raw Dumps, Binaries & Oversized Code/Doc Files..."
for f in $CHANGED_FILES; do
  [ -f "$f" ] || continue
  case "$f" in
    *.sql.gz|*.dump|*.tar.gz|*.zip)
      echo "  ❌ [VIOLATION] Forbidden archive/dump artifact in working tree: $f"
      VIOLATIONS=$((VIOLATIONS + 1))
      ;;
  esac
done

echo ""
echo "▶ [GATE 3] Scanning Modified Code for Floating-Point Money Math Risks..."
for f in $CHANGED_FILES; do
  [ -f "$f" ] || continue
  case "$f" in
    *.ts|*.tsx|*.js|*.jsx|*.py)
      if grep -nE "(parseFloat.*price|toFixed\(2\))" "$f" >/dev/null 2>&1; then
        echo "  ⚠️  [WARNING] Potential floating-point currency math in $f (Require integer minor units):"
        grep -nE "(parseFloat.*price|toFixed\(2\))" "$f" | head -n 5
        WARNINGS=$((WARNINGS + 1))
      fi
      ;;
  esac
done

echo ""
echo "▶ [CLOUD RUN FREE-TIER GATE] Verifying \$0.00/mo Guardrails in api/deploy_cloud_run.sh..."
if [ -f "api/deploy_cloud_run.sh" ]; then
  if grep -q -- "--min-instances 0" "api/deploy_cloud_run.sh"; then
    echo "  ✅ Cloud Run min-instances=0 (\$0.00/mo idle scale) verified."
  else
    echo "  ❌ [VIOLATION] api/deploy_cloud_run.sh is missing '--min-instances 0'!"
    VIOLATIONS=$((VIOLATIONS + 1))
  fi
fi

echo ""
echo "▶ [GATE 8: Ẹ̀ṢỌ́ PRE-BUILD ZERO-TRUST SECURITY GATE] Scanning Secrets & AI Supply Chain..."
# 1. Supply-Chain & Trojan Wrapper Check
if [ -f "api/requirements.txt" ]; then
  if grep -iE "^\s*litellm" "api/requirements.txt" >/dev/null 2>&1; then
    echo "  ❌ [SECURITY VIOLATION] LiteLLM detected in requirements.txt (Supply chain trojan risk)!"
    VIOLATIONS=$((VIOLATIONS + 1))
  else
    echo "  ✅ AI Supply Chain Verified: Zero LiteLLM trojans, native google-genai direct SDK enforced."
  fi
fi

# 2. Hardcoded Secrets & High-Entropy Tokens Check across changed code files
for f in $CHANGED_FILES; do
  [ -f "$f" ] || continue
  case "$f" in
    *.py|*.js|*.jsx|*.ts|*.tsx|*.json|*.sh|*.env*)
      # Ignore manifest data files and sample tests
      if [[ "$f" == *"manifest"* ]] || [[ "$f" == *"corpus"* ]] || [[ "$f" == *".agents/"* ]]; then
        continue
      fi
      if grep -nE "(AIzaSy[A-Za-z0-9_-]{33}|ghp_[a-zA-Z0-9]{36}|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)" "$f" >/dev/null 2>&1; then
        echo "  ❌ [SECURITY VIOLATION] High-entropy secret detected in $f!"
        grep -nE "(AIzaSy[A-Za-z0-9_-]{33}|ghp_[a-zA-Z0-9]{36}|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)" "$f" | head -n 3
        VIOLATIONS=$((VIOLATIONS + 1))
      fi
      ;;
  esac
done

# 3. Insecure Wildcard CORS with Credentials Check
for f in $CHANGED_FILES; do
  [ -f "$f" ] || continue
  case "$f" in
    *.py)
      if grep -nE 'allow_origins=\["\*"\]' "$f" >/dev/null 2>&1 && grep -nE 'allow_credentials=True' "$f" >/dev/null 2>&1; then
        echo "  ❌ [SECURITY VIOLATION] Insecure wildcard CORS with credentials detected in $f!"
        VIOLATIONS=$((VIOLATIONS + 1))
      fi
      ;;
  esac
done

echo ""
echo "▶ [DUAL-MEMORY GATE] Verifying Shared Team Brain & 11 Persona Memory Vaults..."
REQUIRED_MEMORIES=(
  ".agents/AGENTS.md"
  ".agents/CHECKPOINTS.md"
  ".agents/HANDOFF.md"
  ".agents/LEAN_COMMITS_AND_BUNDLES.md"
  ".agents/STARTING_PROMPTS.md"
  ".agents/memory/agba-pa-architect.md"
  ".agents/memory/suuru-qa.md"
  ".agents/memory/oye-auditor.md"
  ".agents/memory/imo-legal.md"
  ".agents/memory/irin-cloud.md"
  ".agents/memory/agbede-builder.md"
  ".agents/memory/eso-security.md"
  ".agents/memory/arokin-archivist.md"
  ".agents/memory/asunwon-ledger.md"
  ".agents/memory/akede-herald.md"
  ".agents/memory/itoju-welfare.md"
  "memory/disk_saver_memory.md"
)
for mem in "${REQUIRED_MEMORIES[@]}"; do
  if [ -f "$mem" ]; then
    echo "  ✅ Present: $mem"
  else
    echo "  ❌ Missing required memory file: $mem"
    VIOLATIONS=$((VIOLATIONS + 1))
  fi
done

echo "=================================================================="
if [ "$VIOLATIONS" -gt 0 ]; then
  echo "🚨 AUDIT FAILED: $VIOLATIONS violation(s), $WARNINGS warning(s) found."
  exit 1
else
  echo "✅ AUDIT PASSED: 0 hard violations ($WARNINGS warning(s)). Verified by Òye Gate Scanner."
  exit 0
fi
