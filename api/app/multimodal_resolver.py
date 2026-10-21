# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: MULTI-MODAL ASSET & PROVENANCE RESOLVER (v6.2.0)
# ==============================================================================
# Maps and resolves:
#   1. Acoustic Call (Spoken Speech) & Response (Dùndún Gángan Mimicry)
#   2. Master Opus Suites & Oríkì Ọba Itire Ensemble Loops
#   3. Verified Museum Visual Masterworks (CMA, AIC, Met, Smithsonian, Golden Matrix)
# ==============================================================================

import os
import re
import json
from pathlib import Path
from typing import Dict, Any, Tuple

try:
    from .semantic_bridge import normalize_y, strip_accents, audio_token_key
except ImportError:
    from semantic_bridge import normalize_y, strip_accents, audio_token_key


def map_call_and_response_audio(golden_matrix_dir: Path, root_dir: Path) -> Tuple[dict, dict, dict, dict, list]:
    """
    Comprehensive multi-modal acoustic mapping across the 3 exclusive authentic Yorùbá audio repositories:
    1. Gangan_Master_Segments_OptionB (80 files: 40 Spoken Calls & 40 Dùndún Gángan Responses)
    2. Master_Opus_Suites (4 Sacred Master Audio Suites in .opus)
    3. Oríkì_Ọba_Itire_Ensemble_Loops (59 assets)
    """
    gms_dir = golden_matrix_dir / "Gangan_master_segments"
    optb_dir = gms_dir / "Gangan_Master_Segments_OptionB"
    if not optb_dir.exists():
        optb_dir = golden_matrix_dir / "Gangan_Master_Segments_OptionB"

    calls: Dict[str, str] = {}
    responses: Dict[str, str] = {}
    takes: Dict[str, Dict[str, list]] = {}
    master_opus: Dict[str, str] = {}
    oriki_assets: list = []

    if optb_dir.exists():
        for f in sorted(optb_dir.glob("*.wav")):
            stem = f.stem
            clean = audio_token_key(stem)
            core_key = clean.replace("spoken", "").replace("dundungangan", "").replace("gangan", "").replace("dundun", "")
            core_key = re.sub(r"[_\s]*0[1-9][_\s]*", "", core_key).strip()

            if core_key not in takes:
                takes[core_key] = {"calls": [], "responses": []}

            if "spoken" in clean:
                takes[core_key]["calls"].append(str(f))
                if core_key not in calls or "_01_" in stem:
                    calls[core_key] = str(f)
            elif "gangan" in clean or "dundun" in clean:
                takes[core_key]["responses"].append(str(f))
                if core_key not in responses or "_01_" in stem:
                    responses[core_key] = str(f)

    candidate_opus_dirs = [
        gms_dir,
        root_dir / "Agba_Engine_Foundational_Vault" / "03_Acoustic_Counterpart_Tokens" / "Master_Opus_Suites",
    ]
    for odir in candidate_opus_dirs:
        if odir.exists():
            for f in odir.glob("*.opus"):
                clean_fn = audio_token_key(f.name)
                if "ayalu" in clean_fn or "gudugudu" in clean_fn:
                    master_opus["oriki_oba_itire_ensemble"] = str(f)
                elif "regalia" in clean_fn:
                    master_opus["full_regalia_ati_solfege_mimicry"] = str(f)
                elif "baseline" in clean_fn or "glissando" in clean_fn:
                    master_opus["foundational_tone_scale_glissando"] = str(f)
                elif "kabiyesi" in clean_fn:
                    master_opus["gangan_kabiyesi_salutations"] = str(f)

    candidate_oriki_dirs = [
        gms_dir / "Oríkì_Ọba_Itire_Ensemble_Loops",
        golden_matrix_dir / "Oríkì_Ọba_Itire_Ensemble_Loops",
        root_dir / "Agba_Engine_Foundational_Vault" / "03_Acoustic_Counterpart_Tokens" / "Oríkì_Ọba_Itire_Ensemble_Loops",
    ]
    for rdir in candidate_oriki_dirs:
        if rdir.exists():
            for f in rdir.glob("*.wav"):
                oriki_assets.append(str(f))
            break

    return calls, responses, takes, master_opus, oriki_assets


def map_image_assets(golden_matrix_dir: Path) -> Tuple[Dict[str, str], Dict[str, Any]]:
    """Map normalized entity keys to verified visual regalia and indigenous metadata."""
    images_dir = golden_matrix_dir / "Images"
    unified_manifest = golden_matrix_dir / "agba_unified_visual_regalia_manifest.json"
    museum_manifest = golden_matrix_dir / "agba_harvested_museum_visuals.json"
    mapping: Dict[str, str] = {}
    visual_metadata: Dict[str, Any] = {}

    target_manifest = unified_manifest if unified_manifest.exists() else museum_manifest
    if target_manifest.exists():
        try:
            with open(target_manifest, "r", encoding="utf-8") as mf:
                manifest_items = json.load(mf)
            for it in manifest_items:
                fname = it.get("filename")
                fpath = images_dir / fname if fname else None
                if fpath and fpath.exists():
                    fpath_str = str(fpath)
                    visual_metadata[fpath_str] = it
                    visual_metadata[fname] = it
                    canon = it.get("canonical_name", "")
                    if canon:
                        visual_metadata[canon] = it
                        visual_metadata[normalize_y(canon)] = it
                        visual_metadata[strip_accents(canon)] = it
                    t = it.get("title", "")
                    if t:
                        visual_metadata[t] = it
                        visual_metadata[normalize_y(t)] = it
                    full_t = it.get("canonical_title_full", "")
                    if full_t:
                        visual_metadata[full_t] = it

                    aliases = {
                        "Adé Ààrẹ": ["Adé Ààrẹ.jpeg", "Ade Aare.jpeg", "Foundational_Ade_Aare.jpeg"],
                        "Èwù Ìlèkè": ["Èwù Ìlèkè.webp", "Ewu Ileke.webp", "Foundational_Ewu_Ileke.webp"],
                        "Fìlà Abetí Ajá": ["Fìlà Abetí Ajá.jpeg", "Fila Abeti Aja.jpeg", "Foundational_Fila_Abeti_Aja.jpeg"],
                        "Fìlà Gọ̀bí": ["Fìlà Gọ̀bí.jpeg", "Fila Gobi.jpeg", "Foundational_Fila_Gobi.jpeg"],
                        "Kábíyèsí": ["Kábíyèsí.jpg", "Kabiyesi.jpg", "Foundational_Kabiyesi.jpg"],
                        "Pà Kaja": ["Pà Kaja.jpeg", "Pa Kaja.jpeg", "Foundational_Pa_Kaja.jpeg"],
                    }
                    if canon in aliases:
                        for afn in aliases[canon]:
                            visual_metadata[afn] = it
                            visual_metadata[str(images_dir / afn)] = it

                    keys_to_index = [
                        it.get("canonical_name", ""),
                        it.get("canonical_title_full", ""),
                        it.get("corpus_concept_id", ""),
                        it.get("museum_archival_title", ""),
                        it.get("title", ""),
                        it.get("canonical_corpus_concept", ""),
                    ]
                    for raw in keys_to_index:
                        if raw:
                            mapping[normalize_y(raw)] = fpath_str
                            mapping[strip_accents(raw)] = fpath_str
                            for part in raw.split("/"):
                                part_clean = part.strip()
                                if part_clean:
                                    mapping[normalize_y(part_clean)] = fpath_str
                                    mapping[strip_accents(part_clean)] = fpath_str
                            for p in re.findall(r"\((.*?)\)", raw):
                                mapping[normalize_y(p)] = fpath_str
                                mapping[strip_accents(p)] = fpath_str
        except Exception as e:
            print(f"   [!] Manifest map notice: {e}")

    if images_dir.exists():
        for f in images_dir.glob("*.*"):
            if f.suffix.lower() in [".jpg", ".jpeg", ".webp", ".png"]:
                stem = f.stem
                mapping[normalize_y(stem)] = str(f)
                mapping[strip_accents(stem)] = str(f)
                no_prefix = re.sub(r"^(cma|aic|met|si|foundational)_", "", stem, flags=re.I)
                clean_core = re.sub(r"(_\d+|_NMAfA-[\w-]+)$", "", no_prefix)
                mapping[strip_accents(no_prefix)] = str(f)
                mapping[strip_accents(clean_core)] = str(f)
                mapping[normalize_y(clean_core)] = str(f)
                for p in re.findall(r"\((.*?)\)", stem):
                    mapping[normalize_y(p)] = str(f)
                    mapping[strip_accents(p)] = str(f)

    return mapping, visual_metadata


def resolve_entity_multimodal_links(
    entity_id: str,
    title: str,
    acoustic_calls: Dict[str, str],
    acoustic_responses: Dict[str, str],
    image_assets: Dict[str, str],
    visual_metadata: Dict[str, Any],
) -> Dict[str, Any]:
    """Enforce strict indigenous provenance and resolve multi-modal audio/visual links."""
    norm_id = normalize_y(entity_id)
    norm_title = normalize_y(title)
    stripped_id = strip_accents(entity_id)
    stripped_title = strip_accents(title)

    media_links: Dict[str, Any] = {
        "has_acoustic_counterpart": False,
        "has_audio_token": False,
        "call_spoken_audio_uri": None,
        "response_gangan_audio_uri": None,
        "acoustic_mimicry_type": None,
        "has_visual_asset": False,
        "visual_asset_uri": None,
        "canonical_name": None,
        "canonical_title_full": None,
        "indigenous_place_of_origin": None,
        "origin_region": None,
        "master_artisan_or_guild": None,
        "creation_epoch": None,
        "medium_materials": None,
        "corpus_deep_description": None,
        "philosophical_context": None,
        "current_custodial_repository": None,
        "museum_archival_title": None,
        "accession_number": None,
    }

    for k in [stripped_id, stripped_title]:
        if k in acoustic_calls or k in acoustic_responses:
            media_links["has_acoustic_counterpart"] = True
            media_links["has_audio_token"] = True
            media_links["call_spoken_audio_uri"] = acoustic_calls.get(k)
            media_links["response_gangan_audio_uri"] = acoustic_responses.get(k)
            media_links["acoustic_mimicry_type"] = "Dùndún Gángan Glissando (Solfège Mimicry)"
            break

    if not media_links["has_acoustic_counterpart"]:
        for k, c_path in acoustic_calls.items():
            if k in stripped_id or k in stripped_title:
                media_links["has_acoustic_counterpart"] = True
                media_links["has_audio_token"] = True
                media_links["call_spoken_audio_uri"] = c_path
                media_links["response_gangan_audio_uri"] = acoustic_responses.get(k)
                media_links["acoustic_mimicry_type"] = "Dùndún Gángan Glissando (Solfège Mimicry)"
                break

    matched_visual_uri = None
    for k in [norm_title, stripped_title, norm_id, stripped_id]:
        if k in image_assets:
            matched_visual_uri = image_assets[k]
            break

    if not matched_visual_uri:
        for img_k, img_uri in image_assets.items():
            if stripped_title == img_k or stripped_id == img_k:
                matched_visual_uri = img_uri
                break

    if matched_visual_uri:
        media_links["has_visual_asset"] = True
        media_links["visual_asset_uri"] = matched_visual_uri
        meta = visual_metadata.get(matched_visual_uri) or visual_metadata.get(os.path.basename(matched_visual_uri))
        if meta:
            for field in [
                "canonical_name", "canonical_title_full", "indigenous_place_of_origin",
                "origin_region", "master_artisan_or_guild", "creation_epoch",
                "medium_materials", "corpus_deep_description", "philosophical_context",
                "current_custodial_repository", "museum_archival_title", "accession_number",
                "local_asset_url", "image_url",
            ]:
                media_links[field] = meta.get(field)
            media_links["source_url"] = meta.get("local_asset_url") or meta.get("image_url") or meta.get("source_url")

    return media_links
