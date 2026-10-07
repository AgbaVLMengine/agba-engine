# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: AUTOMATED MULTI-MUSEUM DAM VISUAL HARVESTER (v6.1.0-alpha)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Data Sources:
#   1. Cleveland Museum of Art (CMA) Open Access Collection API (CC0)
#   2. Art Institute of Chicago (AIC) IIIF Public Domain Collection API (CC0)
#   3. The Metropolitan Museum of Art (The Met) Open Access API v1.1 (CC0)
#   4. Smithsonian Open Access API (NMAfA & Anthropology Collections) (CC0)
# Mission: Expand VLM visual ground truth with 60+ verified West African museum artifacts
# ==============================================================================

import os
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

try:
    from app.config import AgbaConfig
except ImportError:
    from config import AgbaConfig

IMAGES_DEST_MATRIX = AgbaConfig.get_golden_matrix_dir() / "Images"
IMAGES_DEST_VAULT = AgbaConfig.ROOT_DIR / "Agba_Engine_Foundational_Vault" / "04_Curated_Visual_Regalia"
MANIFEST_PATH = AgbaConfig.get_golden_matrix_dir() / "agba_harvested_museum_visuals.json"


NON_YORUBA_DISQUALIFIERS = [
    'ikenga', 'uhunmwun', 'benin', 'igbo', 'nupe', 'ejagham', 'idoma', 
    'nok', 'agboho mmuo', 'ahianmwen', 'riga', 'hen', 'doll',
    'plaque', 'tusk', 'water transport jar', 'commemorative head'
]

def is_canonical_yoruba(title: str, culture: str = '', desc: str = '') -> bool:
    t_lower = (title or '').lower()
    c_lower = (culture or '').lower()
    d_lower = (desc or '').lower()
    for kw in NON_YORUBA_DISQUALIFIERS:
        if kw in t_lower or kw in d_lower or (kw in c_lower and 'yoruba' not in c_lower):
            return False
    return True

BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://www.artic.edu/"
}

def sanitize_filename(name: str) -> str:
    """Clean filename while preserving diacritics."""
    bad_chars = [":", "/", "\\", "*", "?", '"', "<", ">", "|", "\n", "\r", "\t"]
    for c in bad_chars:
        name = name.replace(c, "-")
    if len(name) > 80:
        name = name[:80]
    return name.strip()

def download_image(url: str, dest_path: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers=BROWSER_HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            if len(data) < 1000:
                return False
            with open(dest_path, "wb") as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"   [!] Failed to download {dest_path.name}: {e}")
        return False

def harvest_cleveland_museum():
    print("\n🏛️ [SOURCE 1] Harvesting Cleveland Museum of Art (CMA)...")
    url = "https://openaccess-api.clevelandart.org/api/artworks/?q=Yoruba&has_image=1&limit=30"
    req = urllib.request.Request(url, headers=BROWSER_HEADERS)
    harvested = []

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            items = data.get("data", [])
            print(f"   Found {len(items)} Yoruba artworks with open images in CMA.")

            for item in items:
                title = item.get("title", "")
                img_url = item.get("images", {}).get("web", {}).get("url")
                if not img_url:
                    continue

                safe_title = sanitize_filename(title)
                filename = f"CMA_{safe_title}.jpg"
                dest_m = IMAGES_DEST_MATRIX / filename
                dest_v = IMAGES_DEST_VAULT / filename

                if not dest_m.exists():
                    print(f"   ⬇️ Downloading CMA: {title}...")
                    if download_image(img_url, dest_m):
                        if IMAGES_DEST_VAULT.exists():
                            with open(dest_m, "rb") as f_in, open(dest_v, "wb") as f_out:
                                f_out.write(f_in.read())
                        time.sleep(0.3)
                else:
                    print(f"   ✨ Cached CMA: {title}")

                harvested.append({
                    "museum": "Cleveland Museum of Art",
                    "title": title,
                    "date": item.get("creation_date"),
                    "culture": item.get("culture", "Yorùbá"),
                    "medium": item.get("technique"),
                    "accession_number": item.get("accession_number"),
                    "filename": filename,
                    "license": "CC0 (Public Domain)",
                    "source_url": img_url
                })

    except Exception as e:
        print(f"   [!] CMA Harvest error: {e}")

    return harvested

def harvest_chicago_art_institute():
    print("\n🏛️ [SOURCE 2] Harvesting Art Institute of Chicago (AIC)...")
    url = "https://api.artic.edu/api/v1/artworks/search?q=Yoruba&query[term][is_public_domain]=true&limit=25&fields=id,title,artist_display,image_id,date_display,medium_display,place_of_origin"
    req = urllib.request.Request(url, headers=BROWSER_HEADERS)
    harvested = []

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            items = data.get("data", [])
            config = data.get("config", {})
            iiif_base = config.get("iiif_url", "https://www.artic.edu/iiif/2")

            for item in items:
                title = item.get("title", "")
                place = str(item.get("place_of_origin", "")).lower()
                img_id = item.get("image_id")
                
                if not img_id or ("nigeria" not in place and "yoruba" not in title.lower()):
                    continue

                img_url = f"{iiif_base}/{img_id}/full/843,/0/default.jpg"
                safe_title = sanitize_filename(title)
                filename = f"AIC_{safe_title}.jpg"
                dest_m = IMAGES_DEST_MATRIX / filename
                dest_v = IMAGES_DEST_VAULT / filename

                if not dest_m.exists():
                    print(f"   ⬇️ Downloading AIC: {title}...")
                    if download_image(img_url, dest_m):
                        if IMAGES_DEST_VAULT.exists():
                            with open(dest_m, "rb") as f_in, open(dest_v, "wb") as f_out:
                                f_out.write(f_in.read())
                        time.sleep(0.3)
                else:
                    print(f"   ✨ Cached AIC: {title}")

                harvested.append({
                    "museum": "Art Institute of Chicago",
                    "title": title,
                    "date": item.get("date_display"),
                    "culture": "Yorùbá",
                    "place_of_origin": item.get("place_of_origin"),
                    "medium": item.get("medium_display"),
                    "filename": filename,
                    "license": "CC0 / Public Domain",
                    "source_url": img_url
                })

    except Exception as e:
        print(f"   [!] AIC Harvest error: {e}")

    return harvested

def harvest_the_met():
    print("\n🏛️ [SOURCE 3] Harvesting The Metropolitan Museum of Art (The Met v1.1)...")
    search_queries = ["Yoruba", "Ife", "Owo Yoruba", "Ibeji", "Gelede"]
    harvested = []
    seen_ids = set()

    for q in search_queries:
        encoded_q = urllib.parse.quote(q)
        search_url = f"https://collectionapi.metmuseum.org/public/collection/v1.1/search?q={encoded_q}&hasImages=true&limit=25"
        try:
            req = urllib.request.Request(search_url, headers=BROWSER_HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                object_ids = data.get("objectIDs", []) or []
                print(f"   Found {len(object_ids)} items for query '{q}' in The Met.")

                for oid in object_ids:
                    if oid in seen_ids:
                        continue
                    seen_ids.add(oid)

                    obj_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}"
                    try:
                        req_obj = urllib.request.Request(obj_url, headers=BROWSER_HEADERS)
                        with urllib.request.urlopen(req_obj, timeout=15) as r_obj:
                            item = json.loads(r_obj.read().decode("utf-8"))
                            
                            if not item.get("isPublicDomain"):
                                continue
                            
                            img_url = item.get("primaryImageSmall") or item.get("primaryImage")
                            if not img_url:
                                continue

                            culture = item.get("culture", "")
                            dept = item.get("department", "")
                            if "yoruba" not in culture.lower() and "africa" not in dept.lower() and "nigeria" not in culture.lower():
                                continue

                            title = item.get("title", f"Met_Object_{oid}")
                            safe_title = sanitize_filename(f"{title}_{oid}")
                            filename = f"MET_{safe_title}.jpg"
                            dest_m = IMAGES_DEST_MATRIX / filename
                            dest_v = IMAGES_DEST_VAULT / filename

                            if not dest_m.exists():
                                print(f"   ⬇️ Downloading The Met: {title} (ID: {oid})...")
                                if download_image(img_url, dest_m):
                                    if IMAGES_DEST_VAULT.exists():
                                        with open(dest_m, "rb") as f_in, open(dest_v, "wb") as f_out:
                                            f_out.write(f_in.read())
                                    time.sleep(0.15)
                            else:
                                print(f"   ✨ Cached The Met: {title}")

                            harvested.append({
                                "museum": "The Metropolitan Museum of Art",
                                "title": title,
                                "date": item.get("objectDate"),
                                "culture": culture or "Yorùbá",
                                "medium": item.get("medium"),
                                "accession_number": item.get("accessionNumber"),
                                "filename": filename,
                                "license": "CC0 (Public Domain)",
                                "source_url": img_url,
                                "object_url": item.get("objectURL")
                            })

                            if len(harvested) >= 35:
                                break
                    except Exception as e_obj:
                        continue
                    time.sleep(0.06)

                    if len(harvested) >= 35:
                        break

        except Exception as e:
            print(f"   [!] The Met search error for '{q}': {e}")

    return harvested

def harvest_smithsonian():
    print("\n🏛️ [SOURCE 4] Harvesting Smithsonian Open Access (NMAfA & Anthropology)...")
    query_str = "Yoruba AND online_media_type:Images"
    encoded_q = urllib.parse.quote(query_str)
    url = f"https://api.si.edu/openaccess/api/v1.0/search?q={encoded_q}&api_key=DEMO_KEY&rows=30"
    harvested = []
    seen_ids = set()

    try:
        req = urllib.request.Request(url, headers=BROWSER_HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            rows = data.get("response", {}).get("rows", [])
            print(f"   Found {len(rows)} verified items in Smithsonian Open Access.")

            for r in rows:
                title = r.get("title", "")
                media_list = r.get("content", {}).get("descriptiveNonRepeating", {}).get("online_media", {}).get("media", [])
                if not media_list:
                    continue

                media_item = media_list[0]
                usage = media_item.get("usage", {}).get("access", "")
                if usage != "CC0":
                    continue

                ids_id = media_item.get("idsId")
                if not ids_id or ids_id in seen_ids:
                    continue
                seen_ids.add(ids_id)

                img_url = f"https://ids.si.edu/ids/download?id={ids_id}_screen"
                safe_title = sanitize_filename(f"{title}_{ids_id}")
                filename = f"SI_{safe_title}.jpg"
                dest_m = IMAGES_DEST_MATRIX / filename
                dest_v = IMAGES_DEST_VAULT / filename

                freetext = r.get("content", {}).get("freetext", {})
                date_val = freetext.get("date", [{}])[0].get("content") if freetext.get("date") else None
                maker_val = freetext.get("name", [{}])[0].get("content") if freetext.get("name") else "Yoruba artist"
                notes_val = freetext.get("notes", [{}])[0].get("content") if freetext.get("notes") else None

                if not dest_m.exists():
                    print(f"   ⬇️ Downloading Smithsonian: {title} ({ids_id})...")
                    if download_image(img_url, dest_m):
                        if IMAGES_DEST_VAULT.exists():
                            with open(dest_m, "rb") as f_in, open(dest_v, "wb") as f_out:
                                f_out.write(f_in.read())
                        time.sleep(0.2)
                else:
                    print(f"   ✨ Cached Smithsonian: {title}")

                harvested.append({
                    "museum": "Smithsonian Institution (NMAfA & Anthropology)",
                    "title": title,
                    "date": date_val,
                    "culture": "Yorùbá",
                    "maker": maker_val,
                    "description": notes_val,
                    "filename": filename,
                    "license": "CC0 (Public Domain)",
                    "source_url": img_url,
                    "ids_id": ids_id
                })

    except Exception as e:
        print(f"   [!] Smithsonian Harvest error: {e}")

    return harvested

def run_harvest():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: MULTI-MUSEUM DAM VISUAL HARVESTER (EXPANDED)")
    print("   - Lead Architect : Aruna Olanrewaju Kabiru")
    print("   - Data Sources   : CMA, AIC, The Met, Smithsonian Open Access (CC0)")
    print("   - Destination    : Agba_Golden_Matrix/Images & Foundational Vault")
    print("=" * 80)

    IMAGES_DEST_MATRIX.mkdir(parents=True, exist_ok=True)
    IMAGES_DEST_VAULT.mkdir(parents=True, exist_ok=True)

    cma_records = harvest_cleveland_museum()
    aic_records = harvest_chicago_art_institute()
    met_records = harvest_the_met()
    si_records = harvest_smithsonian()

    all_records = cma_records + aic_records + met_records + si_records

    # Save unified metadata manifest
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(all_records, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"🎉 MULTI-MUSEUM VISUAL HARVESTING COMPLETE: {len(all_records)} ARTIFACTS INGESTED")
    print(f"   - Cleveland Museum of Art (CMA)          : {len(cma_records)} verified artworks")
    print(f"   - Art Institute of Chicago (AIC)         : {len(aic_records)} verified artworks")
    print(f"   - The Metropolitan Museum of Art (The Met): {len(met_records)} verified artworks")
    print(f"   - Smithsonian Institution Open Access     : {len(si_records)} verified artworks")
    print(f"   - Manifest Catalog                       : {MANIFEST_PATH.name}")
    print("=" * 80)

    return all_records

if __name__ == "__main__":
    run_harvest()
