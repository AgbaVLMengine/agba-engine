import json
import unicodedata
import hashlib
from pathlib import Path

WORKSPACE = Path("/home/aruna_olanrewaju/agba-engine")
API_CORPUS_PATH = WORKSPACE / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = WORKSPACE / "web/src/data/yoruba_master_corpus.json"
PAYLOADS_PATH = WORKSPACE / "scripts/data/batches/archival_dedup_payloads.json"

def nfc(val):
    if isinstance(val, str):
        return unicodedata.normalize("NFC", val)
    if isinstance(val, list):
        return [nfc(x) for x in val]
    if isinstance(val, dict):
        return {nfc(k): nfc(v) for k, v in val.items()}
    return val

def execute_ingestion():
    with open(API_CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    with open(PAYLOADS_PATH, "r", encoding="utf-8") as f:
        payloads = json.load(f)

    print(f"Loaded corpus ({len(corpus)} items) and {len(payloads)} payloads.")

    # 1. Deduplicate Èjì Ogbè
    idx_139 = None
    idx_rich = None
    for i, e in enumerate(corpus):
        if e.get("id") == "Èjì Ogbè" or e.get("title") == "Èjì Ogbè":
            if i < 500 and idx_139 is None:
                idx_139 = i
            else:
                idx_rich = i

    if idx_139 is not None and idx_rich is not None:
        stub = corpus[idx_139]
        rich = corpus[idx_rich]
        merged_aliases = set(rich.get("aliases", []) + stub.get("aliases", []))
        cleaned_aliases = sorted([a for a in merged_aliases if a.strip().lower() not in ["ogbè", "ogbe"]])
        rich["aliases"] = cleaned_aliases
        if "details" in rich:
            rich["details"]["aliases"] = cleaned_aliases
        corpus.pop(idx_139)
        print(f"Merged and popped Èjì Ogbè stub at index {idx_139}.")

    # 2. Re-parent Bọ̀lị̀ to Ọ̀gẹ̀dẹ̀
    for e in corpus:
        if e.get("id") == "Bọ̀lị̀" or e.get("title") == "Bọ̀lị̀":
            e["sovereign_parent"] = "Ọ̀gẹ̀dẹ̀"
            e["sovereign_parent_status"] = "sub_variant"
            if "details" in e:
                e["details"]["sovereign_parent"] = "Ọ̀gẹ̀dẹ̀"
                e["details"]["sovereign_parent_status"] = "sub_variant"
            e["knowledge_graph_relations"] = {
                "sovereign_parent": "Ọ̀gẹ̀dẹ̀",
                "culinary_pair": "Ẹ̀pà",
                "elemental_catalysts": ["Iná", "Èédú", "Àdògán"]
            }
            break

    # 3. Add or update new payloads
    existing_ids = {e.get("id"): i for i, e in enumerate(corpus)}
    new_order = [
        "dandogo_payload", "orirun_payload", "balogun_oluyole_payload",
        "balogun_odeluku_payload", "kurunmi_payload", "jimba_payload", "lateju_payload"
    ]

    for key in new_order:
        data = payloads[key]
        pid = data["id"]
        if pid in existing_ids:
            corpus[existing_ids[pid]] = data
            print(f"Updated {pid} in-place.")
        else:
            corpus.append(data)
            existing_ids[pid] = len(corpus) - 1
            print(f"Appended {pid}.")

    # 4. Update Sovereign Parents sub_variants
    for e in corpus:
        if e.get("id") == "Balógun" or e.get("title") == "Balógun":
            subs = e.get("sub_variants") or []
            for item in ["Balógun Olúyòlé", "Balógun Òdélúkù", "Kúrúnmí", "Jím̀bà", "Látẹ́jú"]:
                if item not in subs:
                    subs.append(item)
            e["sub_variants"] = subs
            if "details" in e:
                e["details"]["sub_variants"] = subs

        if e.get("id") == "Aṣọ-Òkè" or e.get("title") == "Aṣọ-Òkè":
            subs = e.get("sub_variants") or []
            if "Dàńdógó" not in subs:
                subs.append("Dàńdógó")
            e["sub_variants"] = subs
            if "details" in e:
                e["details"]["sub_variants"] = subs

        if e.get("id") == "Orí" or e.get("title") == "Orí":
            subs = e.get("sub_variants") or []
            if "Orírun" not in subs:
                subs.append("Orírun")
            e["sub_variants"] = subs
            if "details" in e:
                e["details"]["sub_variants"] = subs

    # 5. Normalize and write to both master corpora
    normalized_corpus = nfc(corpus)
    formatted_json = json.dumps(normalized_corpus, indent=2, ensure_ascii=False) + "\n"

    with open(API_CORPUS_PATH, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    with open(WEB_CORPUS_PATH, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    hash_api = hashlib.sha256(API_CORPUS_PATH.read_bytes()).hexdigest()
    hash_web = hashlib.sha256(WEB_CORPUS_PATH.read_bytes()).hexdigest()
    assert hash_api == hash_web, "Checksum drift detected!"
    print(f"✅ LOCK CONFIRMED: {len(normalized_corpus)} entities, SHA-256: {hash_api}")

if __name__ == "__main__":
    execute_ingestion()
