---
name: grok-red-team-audit
description: Trigger the mandatory Phase 3 Grok Adversarial Red-Team Audit against current changes using scripts/review.sh and the 8 Ajzenstadt-Supabase Technical Guardrails.
---

# Grok Adversarial Red-Team Audit Skill

Use this skill whenever any code or configuration changes are ready for Phase 3 review before committing or merging.

## Procedure
1. Run `./scripts/review.sh` in the workspace root to execute automated static checks (500-line ceiling, lean commits, floating-point money math, destructive DB commands, and memory presence).
2. Delegate a deep semantic diff review to the `grok-auditor` subagent (or perform the checklist directly if running inside `grok-auditor`):
   - **Gate 1**: Anti-Bloat & Root-Cause Resolution (flat guard clauses, zero defensive symptom patches).
   - **Gate 2**: Financial & Mutating Idempotency (UUID `idempotency_key` + single-tx ledger guard).
   - **Gate 3**: Synchronous Double-Tap UI Locks (`useRef` synchronous lock before `await`).
   - **Gate 4**: Minor-Unit Integer Money Math (cents/kobo integers only).
   - **Gate 5**: Decoupled Access Grants & Webhook Retries (`HTTP 200` access grant vs `HTTP 500` ledger retry).
   - **Gate 6**: 500-Line Component Modularization Rule.
   - **Gate 7**: Zero-Disk / Feather-Light DB & Lean Commits.
   - **Gate 8**: Store Guideline Guards (Apple 3.1.3(a) Reader compliance).
3. Save the audit report to `.agents/local-seeds/AGY__REPORT_<timestamp>.md`, update `.agents/memory/grok-auditor.md` and `.agents/CHECKPOINTS.md`, and report findings to `pa-co-architect`.
