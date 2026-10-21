#!/usr/bin/env python3
# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: HANDOFF-AGBEDE-004 CORPUS TRANSFORMATION SCRIPT
# ==============================================================================
# 1. Category 17 Remapping (140 entities to achieve canonical 17-category balance)
# 2. Ingest 9 Missing Sovereign Parents & 6 Critical Martial/Semiotic Sub-Variants
# 3. Wire Bilateral Knowledge Graph Links
# 4. Sync api/data/yoruba_corpus_1007_NORMALIZED.json -> web/src/data/yoruba_master_corpus.json
# ==============================================================================

import json
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = BASE_DIR / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = BASE_DIR / "web" / "src" / "data" / "yoruba_master_corpus.json"
DATA_PATH = BASE_DIR / "scripts" / "handoff_004_data.json"


def execute_transformation():
    print("🏛️ Loading transformation data from:", DATA_PATH)
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    remap_140 = manifest["remap_140"]
    new_sovereign_parents = manifest["new_sovereign_parents"]
    new_sub_variants = manifest["new_sub_variants"]

    print("🏛️ Loading corpus from:", API_CORPUS_PATH)
    with open(API_CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    print(f"   Initial corpus count: {len(corpus)}")

    # 1. Apply 140 Remappings
    remapped_count = 0
    for entity in corpus:
        t = entity.get("title")
        i = entity.get("id")
        new_cat = remap_140.get(t) or remap_140.get(i)
        if new_cat:
            entity["category"] = new_cat
            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["category"] = new_cat
            remapped_count += 1

    print(f"   ✅ Remapped {remapped_count} entities")

    # 2. Update existing Àpáta war shield to disambiguate from Topography
    for entity in corpus:
        if entity.get("id") == "Àpáta" and entity.get("category") == "Military Traditions, Weaponry & Defense":
            entity["id"] = "Àpáta_Shield"
            entity["title"] = "Àpáta (Shield)"
            entity["is_parent"] = False
            entity["sovereign_parent"] = "Àpáta"
            entity["aliases"] = [
                "apata shield", "defense shield", "war shield", "asa", "body buckler", "apata"
            ]
            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["title"] = "Àpáta (Shield)"
                entity["details"]["id"] = "Àpáta_Shield"
            print("   🛡️ Disambiguated Àpáta (Shield) from Topography parent")
            break

    # 3. Update existing Ìwọ̀fà to Sovereign Parent in Civilization
    for entity in corpus:
        if entity.get("id") == "Ìwọ̀fà" or entity.get("title") == "Ìwọ̀fà":
            entity["category"] = "Civilization, History & Civic Heritage"
            entity["is_parent"] = True
            entity["aliases"] = [
                "ìwọ̀fà", "iwofa", "traditional labor covenant", "pawnship",
                "pre-colonial labor contract", "credit labor covenant"
            ]
            entity["sub_variants"] = [
                "Ìwọ̀fà Ọmọdé", "Ìwọ̀fà Àgbà", "Ìwọ̀fà Oko", "Ìwọ̀fà Iṣẹ́-Ọwọ́"
            ]
            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["category"] = "Civilization, History & Civic Heritage"
                entity["details"]["is_parent"] = True
                entity["details"]["sub_variants"] = entity["sub_variants"]
            print("   🏛️ Updated Ìwọ̀fà to Sovereign Parent in Civilization")
            break

    # 4. Remove 'Ẹégún' from Egúngún aliases to avoid collision
    for entity in corpus:
        if entity.get("id") == "Egúngún" or entity.get("title") == "Egúngún":
            entity["aliases"] = [
                a for a in entity.get("aliases", [])
                if a.lower() not in ["ẹégún", "eegun"]
            ]
            print("   🎭 Cleared Ẹégún alias collision from Egúngún")
            break

    # 5. Ingest New Sovereign Parents
    existing_ids = {e.get("id") for e in corpus}
    existing_titles = {e.get("title") for e in corpus}

    for parent in new_sovereign_parents:
        if parent["id"] not in existing_ids and parent["title"] not in existing_titles:
            p_copy = dict(parent)
            p_copy["details"] = dict(parent)
            corpus.append(p_copy)
            existing_ids.add(parent["id"])
            existing_titles.add(parent["title"])
            print(f"   ⭐ Ingested Sovereign Parent: {parent['title']} ({parent['category']})")

    # 6. Ingest 6 Critical Sub-Variants
    for variant in new_sub_variants:
        if variant["id"] not in existing_ids and variant["title"] not in existing_titles:
            v_copy = dict(variant)
            v_copy["details"] = dict(variant)
            corpus.append(v_copy)
            existing_ids.add(variant["id"])
            existing_titles.add(variant["title"])
            print(f"   🌿 Ingested Sub-Variant: {variant['title']} (Parent: {variant['sovereign_parent']})")

    # 7. Wire Bilateral Knowledge Graph Links
    cluster_1 = ["Apẹja", "Ẹja", "Ọkọ̀ Ojú Omi", "Odò Ọ̀ṣun", "Odo Ọ̀ṣun", "Olókun"]
    cluster_2 = ["Idà", "Àdá", "Ọ̀kọ̀", "Ọfà", "Ògún"]
    cluster_3 = ["Ẹyẹ", "Àwọn Ìyá Mi", "Ìyámi (Our Mothers / Primordial Female Energy)", "Odídẹrẹ́", "Adé"]

    def wire_cluster(names):
        found_entities = []
        for e in corpus:
            t = e.get("title", "")
            i = e.get("id", "")
            if t in names or i in names:
                found_entities.append(e)

        for e in found_entities:
            existing_rel = set(e.get("related_entities", []))
            for other in found_entities:
                if other["title"] != e["title"]:
                    existing_rel.add(other["title"])
            e["related_entities"] = sorted(list(existing_rel))
            if "details" in e and isinstance(e["details"], dict):
                e["details"]["related_entities"] = e["related_entities"]

    wire_cluster(cluster_1)
    wire_cluster(cluster_2)
    wire_cluster(cluster_3)
    print("   🕸️ Bilateral Knowledge Graph Links Wired for Clusters 1, 2, and 3")

    # 8. Category Verification Check
    counts = Counter(e.get("category") for e in corpus)
    print("\n🏛️ Final Category Breakdown (Total Entities: %d):" % len(corpus))
    for cat, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"   - {cat}: {cnt}")

    # 9. Write to disk
    with open(API_CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Saved normalized corpus to {API_CORPUS_PATH}")

    with open(WEB_CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    print(f"💾 Synced master corpus to {WEB_CORPUS_PATH}")


if __name__ == "__main__":
    execute_transformation()
