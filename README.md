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

## 🛡️ Tiered Access & Governance Policy

* **Open-Source Client Tier (`/web`):** Free, public access to **Text & Diacritic Retrieval** (`1.0000` exact tone match, `0.9600` folded) and the **Verified Museum Regalia Gallery** (52 verified masterworks from The Met, British Museum, CMA, AIC, Vienna).
* **Enterprise & Institutional API Tier (`/api`):** Secure access to the full **Tri-Modal Pipeline** (**Text**, **Neural Vision**, and **143 Authentic Human Audio Tokens** including spoken vocalizations and Dùndún / Gángan talking drum Solfège mimicry), reserved for verified studios, museums, and academic institutions.

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
