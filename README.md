# 🏛️ Àgbà Engine (`agba-engine`)

**Version:** `6.1.0-alpha`  
**Lead Architect & Creator:** Aruna Olanrewaju Kabiru  
**License:** `RAIL-Cultural-Heritage-v1.0`  
**Target Infrastructure:** Google Cloud Run (Backend API) + Netlify (React Frontend)

---

## 🌍 Overview & Cultural Sovereignty

`agba-engine` is an open, diacritic-preserving cultural intelligence platform and multi-modal retrieval engine engineered to index Global Cultural Heritage, Indigenous Knowledge Systems, and Tonal Orthographies without semantic degradation or sub-token drift.

The engine preserves the pristine **25-letter Yorùbá alphabet** and its complete three-tone acoustic register (**Àmì Ohùn: Re, Mi, Do**) across vector embeddings, lexical ranking, and institutional archival catalogs.

---

## 🏗️ Repository Architecture (Monorepo)

```text
agba-engine/
├── api/                           # Enterprise API & Retrieval Engine (FastAPI + Docker)
│   ├── app/                       # Core hybrid retrieval, config, and telemetry router
│   ├── data/                      # 1,007-entity normalized master corpus & manifests
│   ├── qdrant_storage/            # Dense vector index storage
│   ├── Dockerfile                 # Google Cloud Run production container definition
│   ├── deploy_cloud_run.sh        # $0.00/month Always Free Tier deploy automator
│   └── requirements.txt
├── web/                           # Open Source Client Interface (React + Vite)
│   ├── src/                       # Custom Yorùbá design system & components
│   └── netlify.toml               # Netlify branch deployments (dev & production)
├── docs/                          # Architectural roadmaps & specifications
└── LICENSE                        # RAIL Cultural Heritage License
```

---

## 🛡️ The Sovereign Craigslist 99% Free Model & Enterprise Commercial Moat

Àgbà Engine operates on the **Sovereign Craigslist Model**: 99% of its cultural utility is completely open, friction-free, and unpaywalled for everyday humanity, while maintaining an ironclad commercial moat against corporate AI extraction.

* **The People's Sanctuary (99% Free Access):**
  - **100% Free Streaming for All Everyday Seekers:** Curious youth, elders, teachers, researchers, and diaspora seekers enjoy unrestricted in-browser streaming access to all **1,411 Canonical Entities**, all **256 Odù Ifá Chapters**, and all **143 Authentic Audio Tokens** (Auntie Yẹmí's pitch contours, Baba Sẹ́fíù Adégbìlú's Dùndún/Gúdúgúdú talking drum glissando, and Father's royal Oríkì).
  - **Zero Friction:** No paywalls, no mandatory logins, no API keys, and no subscription barriers. *"Words without the Àmì Ohùn is a corpse"*—we never withhold the living spoken voice of our ancestors from our people.
* **The Enterprise Commercial Moat (Monetized B2B):**
  - **Strictly Restricted & Withheld:** Automated bulk dataset scraping, raw lossless 24-bit/96kHz studio WAV downloads, offline database dumps, and commercial AI foundation model training / synthetic TTS voice cloning weights for Big Tech conglomerates.
  - **Enterprise B2B Licensing (`api.agbaengine.com`):** High-throughput authenticated API concordance, cultural training dataset synchronization, and commercial gaming/film IP licensing governed by executed Master Services Agreements (MSA) under `RAIL-Cultural-Heritage-v1.0` and Part III (Performers' Rights) of the Nigerian Copyright Act 2022. All enterprise revenues are reinvested across four sovereign pillars: engine infrastructure preservation, founder & core contributor welfare, living elder honoraria, and zero-cost public hosting.
  - *Full Economic Specification:* See [`docs/AGBA_CRAIGSLIST_SOVEREIGN_ECONOMIC_MODEL.md`](file:///home/aruna_olanrewaju/agba-engine/docs/AGBA_CRAIGSLIST_SOVEREIGN_ECONOMIC_MODEL.md).

---

## 🚀 Quickstart: Google Cloud Run Deployment

Deploy the headless API container to Google Cloud Run in under 3 minutes:

```bash
cd api
bash deploy_cloud_run.sh
```

The container automatically scales to **0 instances when idle**, ensuring **$0.00/month** hosting cost on Google Cloud's Always Free Tier.

---

## 📜 Ethical Licensing

This project is governed by the **RAIL-Cultural-Heritage-v1.0** license, ensuring that digitized indigenous heritage and tonal acoustics cannot be exploited for uncredited commercial distillation or cultural erasure.
