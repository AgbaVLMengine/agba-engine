---
name: shared-brain-sync
description: Protocol for reading and updating both the GitHub Shared Brain (.agents/CHECKPOINTS.md) and each agent's Individual Memory (.agents/memory/<agent>.md), then backing them up to GitHub.
---

# Shared Brain & Individual Memory Sync Skill

Every agent in this workspace MUST execute this protocol at the start and end of every task.

## 1. Pre-Task Load
Read:
- `.agents/AGENTS.md`
- `.agents/CHECKPOINTS.md`
- `.agents/HANDOFF.md`
- `.agents/memory/<your-agent-id>.md`

## 2. Post-Task Update
1. Append new architectural discoveries, reusable patterns, or lessons learned to `.agents/memory/<your-agent-id>.md`.
2. Update the status table and append a chronological milestone/task entry in `.agents/CHECKPOINTS.md`.
3. Run `./scripts/sync-brain.sh "<your-agent-id>" "<concise summary>"` to validate Lean Commits compliance and back up the memory state to GitHub.
