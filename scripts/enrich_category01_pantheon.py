import json
import unicodedata
import hashlib
from pathlib import Path

WORKSPACE = Path("/home/aruna_olanrewaju/agba-engine")
API_CORPUS_PATH = WORKSPACE / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = WORKSPACE / "web/src/data/yoruba_master_corpus.json"
PAYLOADS_PATH = WORKSPACE / "scripts/data/batches/category01_pantheon_payloads.json"

def nfc(val):
    if isinstance(val, str):
        return unicodedata.normalize("NFC", val)
    if isinstance(val, list):
        return [nfc(x) for x in val]
    if isinstance(val, dict):
        return {nfc(k): nfc(v) for k, v in val.items()}
    return val

def run_pantheon_enrichment():
    with open(API_CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    with open(PAYLOADS_PATH, "r", encoding="utf-8") as f:
        payloads = json.load(f)

    print(f"Loaded corpus ({len(corpus)} records) and {len(payloads)} pantheon enrichment payloads.")

    updated_count = 0
    for entity in corpus:
        eid = entity.get("id")
        if eid in payloads:
            p = payloads[eid]
            for k, v in p.items():
                entity[k] = v
                if "details" in entity:
                    entity["details"][k] = v
            updated_count += 1
            print(f"Enriched {eid} ({entity.get('title')}) -> Proverbs: {len(entity.get('proverbs_and_oral_traditions', []))}, Etym len: {len(entity.get('etymology_and_philosophy', ''))}")

    assert updated_count == len(payloads), f"Expected {len(payloads)} updates, got {updated_count}"

    # Normalize NFC
    normalized_corpus = nfc(corpus)
    formatted_json = json.dumps(normalized_corpus, indent=2, ensure_ascii=False) + "\n"

    with open(API_CORPUS_PATH, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    with open(WEB_CORPUS_PATH, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    hash_api = hashlib.sha256(API_CORPUS_PATH.read_bytes()).hexdigest()
    hash_web = hashlib.sha256(WEB_CORPUS_PATH.read_bytes()).hexdigest()

    print(f"\nFinal Corpus Count: {len(normalized_corpus)} entities")
    print(f"API SHA-256: {hash_api}")
    print(f"WEB SHA-256: {hash_web}")
    assert hash_api == hash_web, "FATAL: Checksum drift between master corpora!"
    print(f"✅ DUAL-CORPORA SHA-256 LOCK CONFIRMED WITH 0-BIT DRIFT ({hash_api})")

if __name__ == "__main__":
    run_pantheon_enrichment()
