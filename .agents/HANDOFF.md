# 🎯 ZERO-WASTE HANDOFF CARDS (`.agents/HANDOFF.md`)

> **Supervised By**: `Àgbà` (`agba-pa-architect` — Main P.A. & Chief Co-Architect)
> **Execution Rule**: Every agent must read its assigned Handoff Card below, execute the deliverable, update its `.agents/memory/<persona>.md` and `.agents/CHECKPOINTS.md`, and run `./scripts/sync-brain.sh "<persona>" "<summary>"`.

---

## Active Baseline Directives (Awaiting Lead Architect Go-Ahead)

### 1. `HANDOFF-IMO-001` — Legal, Licensing & Provenance Baseline Checkpoint
- **Assigned To**: **`Ìmọ̀`** (`imo-legal`)
- **Mode**: Read-Only Legal & Provenance Audit
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/LICENSE`
  - `/home/aruna_olanrewaju/agba-engine/AGBA_CANONICAL_PROVENANCE_AND_BIBLIOGRAPHY.md`
  - `/home/aruna_olanrewaju/agba-engine/README.md`
  - `/home/aruna_olanrewaju/agba-engine/web/src/data/agba_unified_visual_regalia_manifest.json`
- **Deliverable**:
  1. Audit `RAIL-Cultural-Heritage-v1.0` compliance, Museum Archival image attribution parity (The Met, British Museum, CMA, AIC, Smithsonian, Fowler, NCMM), and Sacred Cosmology / *Awo* exclusion rules.
  2. Identify any legal, IP, privacy (GDPR/NDPA), or licensing gaps before production release.
  3. Record your Legal Checkpoint Report in `.agents/memory/imo-legal.md` and `.agents/CHECKPOINTS.md`.

---

### 2. `HANDOFF-OYE-001` — Codebase Architecture & 500-LOC Industry Standards Audit
- **Assigned To**: **`Òye`** (`oye-auditor`)
- **Mode**: Strictly Read-Only Code & Standards Audit
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/api/app/main.py`
  - `/home/aruna_olanrewaju/agba-engine/api/app/retrieval.py`
  - `/home/aruna_olanrewaju/agba-engine/web/src/App.jsx`
  - `/home/aruna_olanrewaju/agba-engine/web/src/components/`
- **Deliverable**:
  1. Run `./scripts/review.sh` and scan all Python (`/api/app/`) and React (`/web/src/`) files against the 6 Production Gates:
     - Which files currently exceed the **500-Line Modularization Ceiling**?
     - Are there any missing synchronous `useRef` UI double-tap locks, unguarded async mutations, CORS/security risks, or diacritic normalization leaks?
  2. Write an immutable audit report to `.agents/local-seeds/AGY__REPORT_BASELINE_AUDIT.md` and update `.agents/memory/oye-auditor.md` + `.agents/CHECKPOINTS.md`.

---

### 3. `HANDOFF-SUURU-001` — Human-Grade End-to-End QA & Retrieval Verification
- **Assigned To**: **`Sùúrù`** (`suuru-qa`)
- **Mode**: Human-Simulated QA & Retrieval Accuracy Testing
- **Exact Files & Targets to Test**:
  - `/home/aruna_olanrewaju/agba-engine/MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md`
  - `/home/aruna_olanrewaju/agba-engine/api/app/retrieval.py`
  - `/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json`
  - `/home/aruna_olanrewaju/agba-engine/web/` (Frontend build check `npm run build`)
- **Deliverable**:
  1. Run human-simulated QA checks against the retrieval engine and frontend build:
     - Test homograph disambiguation queries (`Ogun` Warfare vs. `Ògún` Deity; `Ọkọ́` Hoe vs. `Ọ̀kọ̀` Spear).
     - Check whether the defects listed in `MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md` (e.g., `Olókun` Chinese token `协调olokun`, `Udàmalóre` duplicate `ancestral ancestral`, Sovereign Parent mismatches like `Ọba`, `Adé`, `Fìlà`) are already resolved in `yoruba_corpus_1007_NORMALIZED.json` or still pending.
  2. Log the exact pass/fail QA matrix in `.agents/memory/suuru-qa.md` and `.agents/CHECKPOINTS.md`.

---

### 4. `HANDOFF-AGBEDE-001` — Builder Readiness & Refactoring Plan Preparation
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Mode**: Pre-Build Inspection (Do NOT modify source code until `Àgbà` and Lead Architect give the green light on `Òye` and `Sùúrù`'s findings)
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md`
  - `/home/aruna_olanrewaju/agba-engine/api/app/retrieval.py`
  - `/home/aruna_olanrewaju/agba-engine/web/src/components/`
- **Deliverable**:
  1. Inspect the codebase and `MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md` to prepare a crisp, modular execution plan (<500 lines per module) for any remaining Corpus/UI/API adjustments.
  2. Record your proposed build sequence in `.agents/memory/agbede-builder.md` and `.agents/CHECKPOINTS.md` and await the Lead Architect's go-ahead.

---

### 5. `HANDOFF-IRIN-001` — Google Cloud Run & FastAPI Service Readiness Check
- **Assigned To**: **`Irin`** (`irin-cloud`)
- **Mode**: Read-Only Cloud & Container Diagnostic
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/api/Dockerfile`
  - `/home/aruna_olanrewaju/agba-engine/api/deploy_cloud_run.sh`
  - `/home/aruna_olanrewaju/agba-engine/api/requirements.txt`
  - `/home/aruna_olanrewaju/agba-engine/netlify.toml`
- **Deliverable**:
  1. Audit `api/Dockerfile`, `api/deploy_cloud_run.sh`, and `netlify.toml` for Cloud Run Always Free Tier compliance (`$0.00/mo`, `min-instances=0`, `2GiB` RAM), cold-start speed, and CORS/env alignment between Netlify and Cloud Run.
  2. Record your Cloud & API readiness report in `.agents/memory/irin-cloud.md` and `.agents/CHECKPOINTS.md`.
