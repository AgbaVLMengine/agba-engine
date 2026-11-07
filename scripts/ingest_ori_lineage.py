import json
import unicodedata
import hashlib
from pathlib import Path

WORKSPACE = Path("/home/aruna_olanrewaju/agba-engine")
API_CORPUS_PATH = WORKSPACE / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = WORKSPACE / "web/src/data/yoruba_master_corpus.json"
PAYLOADS_PATH = WORKSPACE / "scripts/data/batches/ori_lineage_payloads.json"

def nfc(val):
    if isinstance(val, str):
        return unicodedata.normalize("NFC", val)
    if isinstance(val, list):
        return [nfc(x) for x in val]
    if isinstance(val, dict):
        return {nfc(k): nfc(v) for k, v in val.items()}
    return val

def run_ingestion():
    with open(API_CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    with open(PAYLOADS_PATH, "r", encoding="utf-8") as f:
        payloads = json.load(f)

    initial_count = len(corpus)
    print(f"Initial corpus count: {initial_count}")

    # 1. Ingest Àkúnlẹ̀yàn as standalone 14-tier node
    akunleyan = payloads["akunleyan_payload"]
    existing_akunleyan = next((i for i, e in enumerate(corpus) if e.get("id") == "Àkúnlẹ̀yàn" or e.get("title") == "Àkúnlẹ̀yàn"), None)
    if existing_akunleyan is not None:
        corpus[existing_akunleyan] = akunleyan
        print("Updated Àkúnlẹ̀yàn in-place.")
    else:
        corpus.append(akunleyan)
        print("Appended Àkúnlẹ̀yàn to corpus.")

    # 2. Ingest Àkúnlẹ̀gbà as standalone 14-tier node
    akunlegba = payloads["akunlegba_payload"]
    existing_akunlegba = next((i for i, e in enumerate(corpus) if e.get("id") == "Àkúnlẹ̀gbà" or e.get("title") == "Àkúnlẹ̀gbà"), None)
    if existing_akunlegba is not None:
        corpus[existing_akunlegba] = akunlegba
        print("Updated Àkúnlẹ̀gbà in-place.")
    else:
        corpus.append(akunlegba)
        print("Appended Àkúnlẹ̀gbà to corpus.")

    # 3. Promote Àyànmọ́ to primary canonical title, designating Kadara as alias
    kadara_idx = next((i for i, e in enumerate(corpus) if e.get("id") == "Kadara" or e.get("title") == "Kadara"), None)
    if kadara_idx is not None:
        k = corpus[kadara_idx]
        k["id"] = "Àyànmọ́"
        k["title"] = "Àyànmọ́"
        k["sovereign_parent"] = "Orí"
        k["sovereign_parent_status"] = "sub_variant"
        k["is_parent"] = False

        # Ensure Kadara is in aliases alongside existing aliases
        aliases = k.get("aliases") or []
        for alias_item in ["kadara", "kàdárà", "ayanmo", "àyànmọ́", "affixed destiny", "destiny lot"]:
            if alias_item not in aliases:
                aliases.append(alias_item)
        k["aliases"] = sorted(list(set(aliases)))

        if "details" in k:
            k["details"]["id"] = "Àyànmọ́"
            k["details"]["title"] = "Àyànmọ́"
            k["details"]["sovereign_parent"] = "Orí"
            k["details"]["sovereign_parent_status"] = "sub_variant"
            k["details"]["aliases"] = k["aliases"]

        print(f"Promoted Kadara at index {kadara_idx} to canonical Àyànmọ́ with Kadara as alias.")

    # 4. Wire Orí's sub_variants and knowledge_graph_relations bilaterally
    ori_node = next((e for e in corpus if e.get("id") == "Orí" or e.get("title") == "Orí"), None)
    if ori_node:
        current_subs = ori_node.get("sub_variants") or []
        target_subs = ["Orí Inú", "Àkúnlẹ̀yàn", "Àkúnlẹ̀gbà", "Àyànmọ́", "Ilé-Orí", "Orírun"]
        for sub in target_subs:
            if sub not in current_subs:
                current_subs.append(sub)
        ori_node["sub_variants"] = current_subs

        # Also purge 'akunleyan' alias from Orí to prevent alias collision now that Àkúnlẹ̀yàn is standalone!
        ori_aliases = ori_node.get("aliases") or []
        ori_aliases = [a for a in ori_aliases if a.lower() not in ["akunleyan", "àkúnlẹ̀yàn"]]
        ori_node["aliases"] = ori_aliases

        # Set up knowledge graph relations
        ori_node["knowledge_graph_relations"] = {
            "sovereign_complex": "Trinitarian Destiny Architecture",
            "metaphysical_aspects": ["Orírun", "Orí Inú", "Àkúnlẹ̀yàn", "Àkúnlẹ̀gbà", "Àyànmọ́"],
            "witness_deity": "Ọ̀rúnmìlà",
            "sacred_reliquary": "Ilé-Orí"
        }

        if "details" in ori_node:
            ori_node["details"]["sub_variants"] = current_subs
            ori_node["details"]["aliases"] = ori_aliases
            ori_node["details"]["knowledge_graph_relations"] = ori_node["knowledge_graph_relations"]

        print("Bilateral wiring of Orí sovereign parent node completed.")

    # 5. NFC Normalization & Write to Both Master Corpora
    normalized_corpus = nfc(corpus)
    final_count = len(normalized_corpus)
    print(f"Final corpus count: {final_count}")

    formatted_json = json.dumps(normalized_corpus, indent=2, ensure_ascii=False) + "\n"

    with open(API_CORPUS_PATH, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    with open(WEB_CORPUS_PATH, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    hash_api = hashlib.sha256(API_CORPUS_PATH.read_bytes()).hexdigest()
    hash_web = hashlib.sha256(WEB_CORPUS_PATH.read_bytes()).hexdigest()

    print(f"API SHA-256: {hash_api}")
    print(f"WEB SHA-256: {hash_web}")
    assert hash_api == hash_web, "FATAL: Checksum drift detected between corpora!"
    print(f"✅ DUAL-CORPORA SHA-256 LOCK ACHIEVED WITH 0-BIT DRIFT ({hash_api})")

if __name__ == "__main__":
    run_ingestion()
