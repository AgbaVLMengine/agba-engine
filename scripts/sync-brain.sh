#!/usr/bin/env bash
# ==============================================================================
# scripts/sync-brain.sh — Automated GitHub Shared Brain & Individual Memory Sync
# Validates Lean Commits Law, commits .agents/ memory updates, and pushes to GitHub
# ==============================================================================
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

AGENT_NAME="${1:-agba-pa-architect}"
SUMMARY="${2:-Update Shared Brain & Individual Persona Memory}"

echo "🧠 [Shared Brain Sync] Validating .agents/ hygiene via ./scripts/review.sh..."
if [ -x "./scripts/review.sh" ]; then
  ./scripts/review.sh
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "⚠️  Not inside a git repository yet. Run 'git init' and add your GitHub remote first."
  exit 0
fi

git add \
  .agents/AGENTS.md \
  .agents/CHECKPOINTS.md \
  .agents/HANDOFF.md \
  .agents/LEAN_COMMITS_AND_BUNDLES.md \
  .agents/STARTING_PROMPTS.md \
  .agents/local-seeds/ \
  .agents/skills/ \
  .agents/memory/agba-pa-architect.md \
  .agents/memory/suuru-qa.md \
  .agents/memory/oye-auditor.md \
  .agents/memory/imo-legal.md \
  .agents/memory/irin-cloud.md \
  .agents/memory/agbede-builder.md \
  .agents/memory/eso-security.md \
  .agents/memory/arokin-archivist.md \
  .agents/memory/asunwon-ledger.md \
  .agents/memory/akede-herald.md \
  .agents/memory/itoju-welfare.md \
  .agents/memory/disk_saver_memory.md \
  memory/disk_saver_memory.md \
  scripts/reclaim_disk.sh \
  scripts/review.sh \
  scripts/sync-brain.sh

if git diff --cached --quiet; then
  echo "✅ [.agents/] Shared Brain is already clean and up to date."
else
  TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  git commit -m "chore(brain): [$AGENT_NAME] $SUMMARY ($TIMESTAMP)"
  echo "✅ Committed Shared & Individual Persona Memory snapshot."
fi

if git remote get-url origin >/dev/null 2>&1; then
  CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
  echo "🚀 Pushing Shared Brain to GitHub (origin/$CURRENT_BRANCH)..."
  if git push origin "$CURRENT_BRANCH" 2>/dev/null; then
    echo "✅ GitHub Shared Brain backup complete!"
  else
    echo "ℹ️  Local commit saved. GitHub push skipped (offline/sandbox)."
  fi
else
  echo "ℹ️  Local commit complete. Add a 'git remote add origin <github-url>' to enable automatic remote push."
fi
