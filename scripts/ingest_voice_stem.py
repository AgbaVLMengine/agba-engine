#!/usr/bin/env python3
# ==============================================================================
# 🎙️ ÀGBÀ ENGINE: AUNTIE YẸMÍ WHATSAPP VOICE STEM INGESTION PIPELINE
# ==============================================================================
# Handoff: HANDOFF-IRIN-002 (Plenary Decree 4 — Acoustic Sovereignty)
# Persona: Ọlọ́yè Irin (irin-cloud) | Supervised by: Ọlọ́yè Àgbà
# Invariant: $0.00/mo Idle Infrastructure — Zero Cloud Daemons, Pure Local CLI
# ==============================================================================

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
import unicodedata
import wave
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
API_MANIFEST = REPO_ROOT / "api" / "data" / "agba_audio_manifest.json"
WEB_MANIFEST = REPO_ROOT / "web" / "src" / "data" / "agba_audio_manifest.json"
CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"

DEFAULT_WATCH_DIRS = [
    Path.home() / "YemiVoiceNotes",
    Path("/mnt/shared/MyFiles/YemiVoiceNotes"),
]
VALID_CATEGORIES = ("vocab", "proverb", "nursery_rhyme", "solfege", "oriki")


def normalize_slug(text: str) -> str:
    """Normalize Yorùbá text into an ASCII-safe slug while preserving NFC title."""
    nfc = unicodedata.normalize("NFC", text.strip())
    nfd = unicodedata.normalize("NFD", nfc)
    stripped = "".join(c for c in nfd if unicodedata.category(c) != "Mn")
    clean = "".join(c if c.isalnum() else "_" for c in stripped.lower())
    return "_".join(filter(None, clean.split("_")))


def resolve_corpus_entity(slug_or_title: str) -> Tuple[str, Optional[str]]:
    """Match a target slug or title against the 1,411 canonical master corpus."""
    target_norm = normalize_slug(slug_or_title)
    if not CORPUS_PATH.exists():
        return slug_or_title.strip(), None
    try:
        raw = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
        entities = raw.get("entities", raw) if isinstance(raw, dict) else raw
        for ent in entities:
            ent_id = str(ent.get("id", ""))
            ent_title = str(ent.get("title", ""))
            if normalize_slug(ent_id) == target_norm or normalize_slug(ent_title) == target_norm:
                return ent_title, ent_id
    except Exception:
        pass
    return slug_or_title.strip(), None


def parse_filename_hint(file_path: Path) -> Tuple[Optional[str], str]:
    """
    Extract optional entity slug and category from filename conventions:
    e.g. 'Oye__proverb.opus' -> ('Oye', 'proverb')
    WhatsApp default 'PTT-20261102-WA0001.opus' -> (None, 'proverb')
    """
    stem = file_path.stem
    if stem.upper().startswith("PTT-") or stem.upper().startswith("AUD-"):
        return None, "proverb"
    if "__" in stem:
        parts = stem.split("__", 1)
        cat = parts[1].lower() if parts[1].lower() in VALID_CATEGORIES else "proverb"
        return parts[0].replace("_", " "), cat
    return stem.replace("_", " "), "proverb"


def parse_ogg_opus_duration(src_file: Path) -> float:
    """Pure-Python RFC 7845 Ogg Opus granule parser (48kHz PCM granules) when ffmpeg is absent."""
    try:
        data = src_file.read_bytes()
        idx = data.rfind(b"OggS")
        if idx != -1 and idx + 14 <= len(data):
            granule = int.from_bytes(data[idx + 6 : idx + 14], "little", signed=False)
            if 0 < granule < (1 << 60):
                return round(granule / 48000.0, 2)
    except Exception:
        pass
    return 0.0


def transcode_audio_stem(
    src_file: Path,
    out_dir: Path,
    stem_id: str,
    fmt: str = "both",
) -> Tuple[Optional[Path], Optional[Path], float, str]:
    """Convert .opus/.ogg WhatsApp note via ffmpeg, or vault native .opus if ffmpeg is absent."""
    out_dir.mkdir(parents=True, exist_ok=True)
    if not shutil.which("ffmpeg"):
        opus_out = out_dir / f"{stem_id}{src_file.suffix or '.opus'}"
        shutil.copy2(src_file, opus_out)
        duration_s = parse_ogg_opus_duration(src_file)
        return None, opus_out, duration_s, opus_out.name

    wav_path = out_dir / f"{stem_id}.wav"
    mp3_path = out_dir / f"{stem_id}.mp3"

    cmd_wav = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(src_file),
        "-ac", "1", "-ar", "16000", "-sample_fmt", "s16",
        str(wav_path),
    ]
    subprocess.run(cmd_wav, check=True)

    duration_s = 0.0
    if wav_path.exists():
        with wave.open(str(wav_path), "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            duration_s = round(frames / float(rate), 2) if rate else 0.0

    if fmt in ("mp3", "both"):
        cmd_mp3 = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-i", str(wav_path),
            "-ac", "1", "-ar", "16000", "-codec:a", "libmp3lame", "-b:a", "64k",
            str(mp3_path),
        ]
        subprocess.run(cmd_mp3, check=True)

    if fmt == "mp3" and wav_path.exists():
        wav_path.unlink()
        wav_path = None
    elif fmt == "wav":
        mp3_path = None

    stream_name = f"{stem_id}.mp3" if fmt in ("mp3", "both") else f"{stem_id}.wav"
    return wav_path, mp3_path, duration_s, stream_name


def append_to_acoustic_manifests(entry: Dict[str, Any], dry_run: bool = False) -> bool:
    """Atomically append the voice stem metadata to both API and Web acoustic manifests (Craigslist Open-Access Model)."""
    if dry_run:
        print(f"🧪 [DRY-RUN] Manifest entry prepared:\n{json.dumps(entry, indent=2, ensure_ascii=False)}")
        return True

    for manifest_path in (API_MANIFEST, WEB_MANIFEST):
        if not manifest_path.exists():
            continue
        items: List[Dict[str, Any]] = json.loads(manifest_path.read_text(encoding="utf-8"))
        if any(item.get("id") == entry["id"] or item.get("source_sha256") == entry.get("source_sha256") for item in items):
            print(f"⏭️  Stem '{entry['id']}' already indexed in {manifest_path.relative_to(REPO_ROOT)}.")
            continue
        items.append(entry)
        manifest_path.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def process_single_note(
    src_file: Path,
    out_dir: Path,
    slug_override: Optional[str],
    category_override: Optional[str],
    fmt: str,
    non_interactive: bool,
    dry_run: bool,
) -> Optional[Dict[str, Any]]:
    """Process one WhatsApp .opus voice note and register it in the acoustic manifest."""
    file_hash = hashlib.sha256(src_file.read_bytes()).hexdigest()[:16]
    hint_slug, hint_cat = parse_filename_hint(src_file)
    target_slug = slug_override or hint_slug
    category = category_override or hint_cat

    if not target_slug and not non_interactive and sys.stdin.isatty():
        print(f"\n🎙️ Detected WhatsApp Voice Note: {src_file.name}")
        target_slug = input("   Enter target entity slug/title (e.g. Òye, Àrọ̀kọ̀, Ewé Àkòko): ").strip()
        cat_in = input(f"   Enter stem category {VALID_CATEGORIES} [default: {category}]: ").strip().lower()
        if cat_in in VALID_CATEGORIES:
            category = cat_in

    if not target_slug:
        target_slug = src_file.stem

    canonical_title, entity_id = resolve_corpus_entity(target_slug)
    clean_slug = normalize_slug(canonical_title)
    stem_id = f"Yemi_{clean_slug}_{category}_{file_hash[:6]}"

    if dry_run:
        duration_s = parse_ogg_opus_duration(src_file)
        stream_file = f"{stem_id}.mp3"
    else:
        _wav, _mp3, duration_s, stream_file = transcode_audio_stem(src_file, out_dir, stem_id, fmt=fmt)

    entry: Dict[str, Any] = {
        "id": stem_id,
        "file_name": stream_file,
        "category": f"Yemi_{category.capitalize()}",
        "speaker": "Auntie Yẹmí",
        "entity_id": entity_id or clean_slug,
        "entity_title": unicodedata.normalize("NFC", canonical_title),
        "drive_path": f"/audio/yemi_stems/{stream_file}",
        "duration_s": duration_s,
        "source_sha256": file_hash,
        "acoustic_features": {
            "sample_rate_hz": 16000,
            "channels": 1,
            "pipeline": "WhatsApp_Opus_16kHz_Mono",
        },
    }
    append_to_acoustic_manifests(entry, dry_run=dry_run)
    print(f"✅ Ingested Auntie Yẹmí stem: {stem_id} -> '{canonical_title}' ({duration_s}s)")
    return entry


def scan_directories(args: argparse.Namespace) -> int:
    """Scan configured directories or single file for .opus/.ogg WhatsApp voice notes."""
    out_dir = Path(args.out_dir).expanduser()
    if args.file:
        target = Path(args.file).expanduser()
        if not target.exists():
            print(f"❌ File not found: {target}", file=sys.stderr)
            return 1
        process_single_note(target, out_dir, args.slug, args.category, args.format, args.non_interactive, args.dry_run)
        return 0

    watch_dirs = [Path(args.watch_dir).expanduser()] if args.watch_dir else DEFAULT_WATCH_DIRS
    seen_files = set()

    while True:
        found_count = 0
        for d in watch_dirs:
            if not d.exists():
                continue
            for note in sorted(d.glob("*.opus")) + sorted(d.glob("*.ogg")):
                if note.resolve() in seen_files:
                    continue
                seen_files.add(note.resolve())
                found_count += 1
                process_single_note(note, out_dir, args.slug, args.category, args.format, args.non_interactive, args.dry_run)

        if not args.watch:
            if found_count == 0:
                dirs_str = ", ".join(str(d) for d in watch_dirs)
                print(f"ℹ️  No new .opus/.ogg notes found in [{dirs_str}]. Zero-cost scan complete.")
            break
        time.sleep(args.interval)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Auntie Yẹmí WhatsApp Voice Stem Local Ingestion Pipeline ($0.00/mo Zero-Daemon CLI)"
    )
    parser.add_argument("--watch-dir", type=str, default=None, help="Directory to scan for incoming .opus files")
    parser.add_argument("--file", type=str, default=None, help="Process a single .opus/.ogg voice note directly")
    parser.add_argument("--out-dir", type=str, default="~/YemiVoiceNotes/processed_stems", help="Output directory for 16kHz stems")
    parser.add_argument("--slug", type=str, default=None, help="Target corpus entity slug or title (e.g., 'Òye', 'Àrọ̀kọ̀')")
    parser.add_argument("--category", type=str, choices=VALID_CATEGORIES, default=None, help="Acoustic stem category")
    parser.add_argument("--format", type=str, choices=("mp3", "wav", "both"), default="both", help="Output audio stem format")
    parser.add_argument("--watch", action="store_true", help="Poll directory during an active recording session")
    parser.add_argument("--interval", type=int, default=5, help="Poll interval in seconds when --watch is enabled")
    parser.add_argument("--non-interactive", action="store_true", help="Never prompt on stdin; use filename/CLI hints")
    parser.add_argument("--dry-run", action="store_true", help="Preview manifest payload without writing files")
    return parser


if __name__ == "__main__":
    sys.exit(scan_directories(build_parser().parse_args()))
