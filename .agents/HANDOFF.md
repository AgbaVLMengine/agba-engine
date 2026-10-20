# 🎯 ZERO-WASTE HANDOFF CARDS (`.agents/HANDOFF.md`)

> **Supervised By**: `Àgbà` (`agba-pa-architect` — Main P.A. & Chief Co-Architect)
> **Status**: 🟢 **APPROVED FOR IMMEDIATE EXECUTION BY LEAD ARCHITECT**
> **Execution Rule**: Every agent must read its assigned Handoff Card below, execute the deliverable, update its `.agents/memory/<persona>.md` and `.agents/CHECKPOINTS.md`, and run `./scripts/sync-brain.sh "<persona>" "<summary>"`.

---

## Active Sprint Directives (`HANDOFF-001` Series)

### 1. `HANDOFF-SUURU-001` — Dynamic Query Stress-Testing, Zero-Shot Retrieval QA & Corpus Audit
- **Assigned To**: **`Sùúrù`** (`suuru-qa`)
- **Mode**: Human-Simulated QA & Dynamic Zero-Shot Retrieval Stress Test
- **Exact Files & Targets to Inspect/Test**:
  - `/home/aruna_olanrewaju/agba-engine/api/app/retrieval.py`
  - `/home/aruna_olanrewaju/agba-engine/api/app/main.py`
  - `/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json`
  - `/home/aruna_olanrewaju/agba-engine/MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md`
  - `/home/aruna_olanrewaju/agba-engine/pending_self_learning_candidates.md`
- **Deliverables**:
  1. **Dynamic User Query Anticipation & Zero-Shot Stress Test**:
     - Design and run a comprehensive battery of **dynamic, real-world user queries** against the retrieval logic in `/api/app/retrieval.py` to anticipate what users will search *before* they ask:
       - *Category A — Natural Language & Conversational Questions*: e.g., `"What did Yoruba warriors wear for protection in battle?"`, `"How do elders settle land disputes?"`, `"Who carved the palace doors in Ekiti?"`, `"What herbs or foods are used for postpartum care?"`
       - *Category B — Un-diacritized / Diaspora / Phonetic / Typo Queries*: e.g., `"ogun vs ogun"`, `"oko and oko"`, `"gelede mask meaning"`, `"sango thunder staff"`, `"adire cloth indigo"`, `"ifa divination tray"`.
       - *Category C — Homograph & Substring Collision Traps*: `Ogun` (Warfare) vs `Ògún` (Deity); `Ọkọ́` (Hoe) vs `Ọ̀kọ̀` (Spear); `Ọfà` (Arrow) vs `Ofada` (Rice) vs `Ìwọ̀fà` (Pawnship); `Idà` (Sword) vs `Àpáta Ìdánre`.
       - *Category D — Multi-Concept & Thematic Queries*: Cross-domain queries linking regalia, proverbs (`Òwe`), panegyrics (`Oríkì`), and historical wars (`Ogun Kiriji`, `Ogun Osogbo`).
  2. **Zero-Shot Gap Analysis & Self-Learning Pipeline**:
     - Identify every query where Top-1 / Top-3 zero-shot retrieval fails, returns low-relevance results, or suffers from lexical/semantic blind spots.
     - Propose exact algorithmic improvements to `retrieval.py` (synonym/intent expansion, English-to-Yorùbá semantic bridges, homograph disambiguation scoring) to achieve **95%–97% zero-shot retrieval accuracy**.
  3. **Audit Adjustment Verification**:
     - Verify which items in `MASTER_CONSOLIDATED_AUDIT_ADJUSTMENTS.md` are still unresolved in `yoruba_corpus_1007_NORMALIZED.json`.
  4. **Memory Checkpoint**:
     - Write the full QA & Dynamic Query Benchmark Report to `.agents/local-seeds/AGY__REPORT_SUURU_QA_001.md` and update `.agents/memory/suuru-qa.md` + `.agents/CHECKPOINTS.md`.

---

### 2. `HANDOFF-AGBEDE-001` — Architectural Blueprint: "Tooth & Vein" Rabbit-Hole UI, Equal Multi-Culture Engine & `ágbaengine.com` Domain Acquisition
- **Assigned To**: **`Àgbẹ̀dẹ`** (`agbede-builder`)
- **Mode**: Technical Architecture Blueprint & Modular Component Specification (<500 LOC rule)
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/web/src/App.jsx`
  - `/home/aruna_olanrewaju/agba-engine/web/src/App.css`
  - `/home/aruna_olanrewaju/agba-engine/web/src/index.css`
  - `/home/aruna_olanrewaju/agba-engine/web/src/components/`
  - `/home/aruna_olanrewaju/agba-engine/api/app/retrieval.py`
  - `/home/aruna_olanrewaju/agba-engine/netlify.toml`
- **Deliverables**:
  1. **Pillar 1 — The "Tooth & Vein" Rabbit-Hole Navigation UI Blueprint (`/web/src/components/`)**:
     - Design the modular React + SVG/Canvas architecture (with every component strictly `<500 lines`) for the user's signature UI vision:
       - **Central Tooth Search Anchor (`ToothSearchCore.jsx`)**: A sculpted tooth emblem at the center of the viewport with the interactive search input/button embedded directly inside the crown/core of the tooth.
       - **Living Vein-Thread Graph (`VeinRabbitHoleCanvas.jsx` + `useExplorationGraph.js`)**: Every time a user submits a search and selects an entry, an organic, pulsing **vein-like root thread** (animated SVG Bézier path / Canvas) grows outward from the Central Tooth to that entry card (`Node 1`).
       - **Infinite Rabbit-Hole Breadcrumb Trail**: As the user clicks deeper into Connected Cultural Relatives or Living Variants (`Tooth → Node 1 → Node 2 → Node 3 → ...`), the vein network continuously branches and connects each new node in sequence. Users can zoom/pan or click **any earlier node along the vein** (or the Central Tooth itself) to retrace their exact path back to the beginning of their search no matter how deep into the rabbit hole they go.
  2. **Pillar 2 — Equal Multi-Culture Ingestion & Seamless Culture-Swapping Architecture**:
     - Design the data schema, ingestion pipeline, and runtime switcher to expand Àgbà Engine to other cultures (e.g., Edo/Benin, Igbo, Akan/Ashanti, Nubia, etc.) while **guaranteeing strict structural and epistemological equality across every culture**:
       - **Equal Schema & Depth Standard**: Every culture gets its own peer 14-Tier canonical manifest, Sovereign Parent taxonomy, native orthographic/diacritic restorer (e.g., Yorùbá 25-letter + `Àmì Ohùn`, Igbo sub-dots + tones, Akan symbols, Edo orthography), and museum/oral provenance parity—no culture is hardcoded as "secondary."
       - **Seamless Culture Swapping**: How the UI theme tokens, diacritic keyboard/restorer, and FastAPI/Qdrant `culture_id` routing switch instantaneously (plus a "Pan-Cultural / Comparative Mode" in `Ọgbọ́n`).
  3. **Pillar 3 — Custom Domain Acquisition & Routing Process for `ágbaengine.com`**:
     - Write the complete step-by-step technical guide for acquiring and configuring **`ágbaengine.com`** (and canonical **`àgbàengine.com`** + ASCII **`agbaengine.com`**):
       - **IDN / Punycode Registration**: Explain how Internationalized Domain Names (IDNA2008) convert `ágbaengine.com` (`xn--gbaengine-21a.com`) and `àgbàengine.com` (`xn--gbengine-rza0b.com`), which registrars support `.com` IDNs (Cloudflare Registrar, Namecheap, Porkbun, GoDaddy), and why registering **both** the accented IDN (`ágbaengine.com` / `àgbàengine.com`) and the ASCII fallback (`agbaengine.com`) with 301/alias routing is essential for universal browser/email compatibility.
       - **Netlify + Google Cloud Run DNS & SSL Setup**: Exact DNS records (`APEX ALIAS/ANAME/A` to Netlify load balancer, `www` CNAME, `api.agbaengine.com` mapping to Google Cloud Run `agba-enterprise-api` in `us-central1`, and automated Let's Encrypt TLS certificates for both Punycode and ASCII domains).
  4. **Memory Checkpoint**:
     - Write the complete blueprint to `.agents/local-seeds/AGY__BLUEPRINT_AGBEDE_001.md` and update `.agents/memory/agbede-builder.md` + `.agents/CHECKPOINTS.md`.

---

### 3. `HANDOFF-IMO-001` — Legal Advisory & Lawyer Briefing Document (For Next Tuesday's Counsel Meeting)
- **Assigned To**: **`Ìmọ̀`** (`imo-legal`)
- **Mode**: Comprehensive Legal Audit & Pre-Counsel Advisory Document Generation
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/LICENSE` (if present) & `README.md`
  - `/home/aruna_olanrewaju/agba-engine/AGBA_CANONICAL_PROVENANCE_AND_BIBLIOGRAPHY.md`
  - `/home/aruna_olanrewaju/agba-engine/AGBA_FUTURE_FEATURES_ROADMAP.md`
  - `/home/aruna_olanrewaju/agba-engine/web/src/data/agba_unified_visual_regalia_manifest.json`
  - `/home/aruna_olanrewaju/agba-engine/api/data/agba_audio_manifest.json`
- **Deliverables**:
  1. Author a comprehensive, lawyer-ready **Legal Advisory & Counsel Briefing Document** saved to `/home/aruna_olanrewaju/agba-engine/docs/AGBA_LEGAL_ADVISORY_FOR_COUNSEL.md` (and mirrored in `.agents/local-seeds/AGY__REPORT_IMO_LEGAL_001.md`) structured for the Lead Architect's **meeting with his lawyer next Tuesday**:
     - **Section 1 — Executive Legal Overview of Àgbà Engine**: What the platform is (Tri-Modal Cultural Heritage Retrieval Engine: Text/Diacritics, 52 Museum Visuals, 143 Audio Tokens, Conversational RAG).
     - **Section 2 — What We CAN Legally Do (Green-Light Capabilities)**:
       - Using CC0 / Public Domain museum images (The Met Open Access, Cleveland Museum of Art CC0, Art Institute of Chicago CC0, Smithsonian CC0) for both open-source and commercial/enterprise tiers.
       - Indexing factual historical events, public-domain texts (e.g., Rev. Samuel Johnson 1921), and original synthesized 14-Tier descriptions authored for Àgbà Engine.
       - Licensing our proprietary software, API access, vector weights, and original audio recordings under a dual-tier model (`RAIL-Cultural-Heritage-v1.0` for public client vs. Commercial Enterprise API license for studios/institutions).
     - **Section 3 — What We CANNOT Do / High-Risk Boundaries (Red-Line Guardrails)**:
       - **Museum Non-Commercial / Copyrighted Photography**: British Museum (CC BY-NC-SA 4.0 restricts commercial use without a separate license), Fowler Museum at UCLA, and contemporary photographers—how we must segregate CC0 assets from restricted/editorial assets in the Enterprise Tier.
       - **Academic Bibliography Copyright**: Citing ideas/facts from Wándé Abímbọ́lá (1975/1976), William Bascom (1969/1980), Rowland Abiodun (2014), Babatunde Lawal (1996), and Pierre Verger (1995) is lawful, whereas verbatim reproduction of copyrighted book chapters or translations beyond fair use is prohibited.
       - **Indigenous Cultural IP, Traditional Knowledge (TK) & Sacred *Awo* Boundaries**: WIPO Intergovernmental Committee on IP and Genetic Resources, Traditional Knowledge and Folklore (GRTKF), UNESCO 2003 Intangible Cultural Heritage Convention, Nigerian Copyright Act 2022 (expressions of folklore provisions under Part IV / NCMM custody), and unconditional exclusion of restricted *Awo* initiatory secrets.
       - **Voice & Biometric Data Privacy (v7.0 Roadmap)**: Nigeria Data Protection Act (NDPA 2023), GDPR, and BIPA compliance for the upcoming Sovereign Voice Recorder (16kHz vocal pitch capture) and Museum Photo Scanner.
     - **Section 4 — Missing Legal Artifacts to Draft with Counsel Next Tuesday**:
       - Formal `LICENSE` file in repo root (`RAIL-Cultural-Heritage-v1.0` full legal text).
       - Terms of Service, Privacy Policy, Cultural Takedown / Custodianship Dispute Protocol, and Enterprise API SLA/License Agreement.
       - Specific **10 Questions Checklist for the Lawyer Meeting Next Tuesday**.
  2. **Memory Checkpoint**:
     - Update `.agents/memory/imo-legal.md` and `.agents/CHECKPOINTS.md`.

---

### 4. `HANDOFF-OYE-001` — Codebase Architecture & 500-LOC Industry Standards Audit
- **Assigned To**: **`Òye`** (`oye-auditor`)
- **Mode**: Strictly Read-Only Code & Standards Audit
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/api/app/` (all `.py` files)
  - `/home/aruna_olanrewaju/agba-engine/web/src/` (all `.jsx`, `.js`, `.css` files)
- **Deliverables**:
  1. Run `./scripts/review.sh` and perform a line-by-line audit of `/api/app/` and `/web/src/` against all 6 Production Gates (500-line ceiling, Anti-Bloat/Anti-Patch, synchronous `useRef` UI double-tap locks, UUID idempotency, 25-letter Tonal Invariant & Sacred Cosmology Reverence, OWASP/CORS security).
  2. Write the immutable audit report to `.agents/local-seeds/AGY__REPORT_OYE_AUDIT_001.md` and update `.agents/memory/oye-auditor.md` + `.agents/CHECKPOINTS.md`.

---

### 5. `HANDOFF-IRIN-001` — Google Cloud Run & FastAPI Service Readiness Audit
- **Assigned To**: **`Irin`** (`irin-cloud`)
- **Mode**: Read-Only Cloud, Container & API Diagnostic
- **Exact Files to Inspect**:
  - `/home/aruna_olanrewaju/agba-engine/api/Dockerfile`
  - `/home/aruna_olanrewaju/agba-engine/api/deploy_cloud_run.sh`
  - `/home/aruna_olanrewaju/agba-engine/api/requirements.txt`
  - `/home/aruna_olanrewaju/agba-engine/api/app/main.py`
  - `/home/aruna_olanrewaju/agba-engine/api/app/config.py`
  - `/home/aruna_olanrewaju/agba-engine/netlify.toml`
- **Deliverables**:
  1. Audit Cloud Run Always Free Tier guardrails (`$0.00/mo`, `min-instances=0`, `2GiB` RAM), container cold-start behavior, Qdrant storage persistence vs. ephemeral container filesystem on Cloud Run, and CORS/env alignment with Netlify (including upcoming custom domain `ágbaengine.com` / `api.agbaengine.com`).
  2. Write the diagnostic report to `.agents/local-seeds/AGY__REPORT_IRIN_CLOUD_001.md` and update `.agents/memory/irin-cloud.md` + `.agents/CHECKPOINTS.md`.
