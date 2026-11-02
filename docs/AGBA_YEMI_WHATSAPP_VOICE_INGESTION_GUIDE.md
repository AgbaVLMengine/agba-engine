# 🎙️ Auntie Yẹmí WhatsApp Voice Stem Ingestion Guide (`HANDOFF-IRIN-002`)

**Custodian**: `Ọlọ́yè Irin` (`irin-cloud`)  
**Supervising Architect**: `Ọlọ́yè Àgbà` (`agba-pa-architect`)  
**Plenary Authority**: Decree 4 of the First Council Plenary (`CHECKPOINT-PLENARY-001`)  
**Infrastructure Invariant**: `\$0.00/mo` Idle Cost — Zero Background Cloud Daemons, Pure Local CLI Execution

---

## 1. Purpose & Sacred Covenant

Auntie Yẹmí carries the living tonal cadence (*Àmì Ohùn*), nursery rhymes, proverbs, and classical pronunciation of the Yorùbá language. Because *"a word without Àmì Ohùn is a corpse"*, [`scripts/ingest_voice_stem.py`](file:///home/aruna_olanrewaju/agba-engine/scripts/ingest_voice_stem.py) connects WhatsApp `.opus` voice notes exported onto the Genesis Workstation directly to the Àgbà Engine Acoustic Sovereignty manifest with zero cloud roundtrips.

In accordance with our **Moral Dual-Tier Architecture (`CHECKPOINT-AGBA-028`)** and **Gate 5 Lean Commits Law**:
- **64kbps 16kHz Mono `.mp3` Web Streams**: Optimized for instant, free public playback in the people's sanctuary.
- **16-bit 16kHz Mono `.wav` Studio Stems**: Preserved locally in `~/YemiVoiceNotes/processed_stems/` (and backed up to Sphere 4 Google Drive) for acoustic feature extraction and B2B enterprise licensing—never committed as binary bloat to Git.
- **Dual Acoustic Manifests**: Metadata entries are appended in lockstep to both [`api/data/agba_audio_manifest.json`](file:///home/aruna_olanrewaju/agba-engine/api/data/agba_audio_manifest.json) and [`web/src/data/agba_audio_manifest.json`](file:///home/aruna_olanrewaju/agba-engine/web/src/data/agba_audio_manifest.json).

---

## 2. Default Monitored Directories

By default, [`scripts/ingest_voice_stem.py`](file:///home/aruna_olanrewaju/agba-engine/scripts/ingest_voice_stem.py) checks:
1. `~/YemiVoiceNotes/` (Linux Crostini home directory)
2. `/mnt/shared/MyFiles/YemiVoiceNotes/` (Chromebook shared folder for direct WhatsApp Web / Android drop)

---

## 3. Filename Conventions (Zero-Prompt Auto-Tagging)

If you rename a WhatsApp `.opus` note before dropping it into `~/YemiVoiceNotes/`, the script automatically extracts the target entity and category:
- `Oye__proverb.opus` $\rightarrow$ Entity: **`Òye`**, Category: `proverb`
- `Aroko__vocab.opus` $\rightarrow$ Entity: **`Àrọ̀kọ̀`**, Category: `vocab`
- `Ewe_Akoko__nursery_rhyme.opus` $\rightarrow$ Entity: **`Ewé Àkòko`**, Category: `nursery_rhyme`

Supported categories: `vocab`, `proverb`, `nursery_rhyme`, `solfege`, `oriki`.

If a raw WhatsApp filename is kept (e.g., `PTT-20261102-WA0001.opus`), running the script in an interactive terminal will prompt you for the target entity slug and category.

---

## 4. CLI Usage Examples

### A. One-Shot Scan (Recommended — Zero Battery/CPU Drain)
Scans `~/YemiVoiceNotes/` and `/mnt/shared/MyFiles/YemiVoiceNotes/` once, transcodes any new `.opus` notes to `16kHz` mono `.wav` + `.mp3`, updates the dual manifests, and exits immediately:
```bash
python3 scripts/ingest_voice_stem.py
```

### B. Ingest a Single Voice Note with Explicit Entity Slug
```bash
python3 scripts/ingest_voice_stem.py \
  --file ~/YemiVoiceNotes/PTT-20261102-WA0004.opus \
  --slug "Òye" \
  --category proverb
```

### C. Dry-Run Preview (Zero File Writes)
Verify entity matching against the 1,411 master corpus and preview the JSON manifest entry without writing to disk:
```bash
python3 scripts/ingest_voice_stem.py \
  --file ~/YemiVoiceNotes/Oye__proverb.opus \
  --dry-run
```

### D. Active Session Folder Watcher (Foreground Only)
During a live WhatsApp voice-note harvesting session, poll the folder every 5 seconds (`Ctrl+C` to stop when done—leaves zero background daemons running):
```bash
python3 scripts/ingest_voice_stem.py --watch --interval 5
```
