# 🎯 ZERO-WASTE HANDOFF CARDS (`.agents/HANDOFF.md`)

> **Purpose**: Eliminates token guessing across subagent chats. Every task delegated by the P.A. & Co-Architect to `grok-builder`, `grok-auditor`, or `grok-scout` must specify exact paths, constraints, and expected outputs.

---

## Active Handoff Queue

### `HANDOFF-001`: Subagent Onboarding & Guardrail Self-Check
- **Assigned To**: `grok-builder`, `grok-auditor`, `grok-scout`
- **Supervised By**: `pa-co-architect`
- **Status**: 🟢 In Progress
- **Context Paths**:
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/.agents/AGENTS.md`
  - `/home/aruna_olanrewaju/.gemini/antigravity/scratch/agy-command-center/.agents/CHECKPOINTS.md`
- **Required Deliverables**:
  1. Read `.agents/AGENTS.md` and `.agents/CHECKPOINTS.md`.
  2. Update your individual memory file in `.agents/memory/<your-agent-name>.md` confirming your operational protocol and active guardrails.
  3. Report readiness back to the Main P.A. & Co-Architect.

---

## Handoff Card Template (Copy for New Tasks)

```markdown
### `HANDOFF-XXX`: [Short Task Title]
- **Assigned To**: [grok-builder | grok-auditor | grok-scout]
- **Target Branch / Worktree**: `dev`
- **Exact File Paths to Read/Modify**:
  - `/abs/path/to/file.ts` (Current LOC: XXX / 500 max)
- **Schema / API Contract**:
  - [Exact SQL / TypeScript interface / Idempotency requirements]
- **Applicable Guardrails**:
  - [ ] Gate 1: Flat code, early returns, root-cause fix
  - [ ] Gate 2: UUID `idempotency_key`
  - [ ] Gate 3: Synchronous `useRef` UI lock
  - [ ] Gate 4: Minor-unit integer money math
  - [ ] Gate 6: File remains < 500 lines
- **Verification Command**:
  - `./scripts/review.sh`
```
