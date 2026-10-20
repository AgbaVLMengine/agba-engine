# ⚡ GROK BUILD PROMPT SEED TEMPLATE (`.agents/local-seeds/GROK_BUILD__PROMPT_TEMPLATE.md`)

```markdown
# GROK-BUILDER EXECUTION SEED
- **Handoff ID**: HANDOFF-XXX
- **Target Files**: [Exact absolute paths]
- **Objective**: [Single-responsibility objective]
- **Mandatory Guardrails**:
  1. Max 500 lines per file (modularize if approaching ceiling).
  2. Flat guard clauses only (early returns; no nested pyramids).
  3. Synchronous `useRef` lock (`busyRef.current = true`) on any mutating UI action.
  4. Integer minor-unit currency math only + UUID `idempotency_key` on mutations.
- **Post-Build Memory Requirement**:
  - Update `.agents/memory/grok-builder.md` and `.agents/CHECKPOINTS.md` before reporting back to `pa-co-architect`.
```
