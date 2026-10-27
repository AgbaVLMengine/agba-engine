#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: COMPLETE THE ODÙ IFÁ CONSTELLATION & ENRICHMENT
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema + Mandatory Academic Provenance

Scope:
1. Complete the Odù Ifá Constellation:
   - Update 'Odù_Ifá' and root 'Ifá' so their `sub_variants` constellation
     holds all 16 Principal Ojú Odù Méjì:
     ['Èjì Ogbè', 'Ọ̀yẹ̀kú Méjì', 'Ìwòrì Méjì', 'Òdí Méjì', 'Ìrosùn Méjì',
      'Ọ̀wọ́nrín Méjì', 'Ọ̀bàrà Méjì', 'Ọ̀kànràn Méjì', 'Ògúndá Méjì', 'Ọ̀sá Méjì',
      'Ìká Méjì', 'Òtúúrúpọ̀n Méjì', 'Òtúá Méjì', 'Ìrẹtẹ̀ Méjì', 'Ọ̀ṣẹ́ Méjì',
      'Òfún Méjì'].
2. Enrich 'Odù_Ifá' and 'Ifá' with:
   - Full dual-language liturgical proverbs (Yorùbá + English translation & philosophical commentary).
   - Authoritative academic citations (Abímbọ́lá 1975, Bascom 1969, Verger 1995).
3. Synchronize both api/data/yoruba_corpus_1007_NORMALIZED.json and
   web/src/data/yoruba_master_corpus.json in lockstep.
=============================================================================
"""

import json
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"

PRINCIPAL_16_ODU: List[str] = [
    "Èjì Ogbè",
    "Ọ̀yẹ̀kú Méjì",
    "Ìwòrì Méjì",
    "Òdí Méjì",
    "Ìrosùn Méjì",
    "Ọ̀wọ́nrín Méjì",
    "Ọ̀bàrà Méjì",
    "Ọ̀kànràn Méjì",
    "Ògúndá Méjì",
    "Ọ̀sá Méjì",
    "Ìká Méjì",
    "Òtúúrúpọ̀n Méjì",
    "Òtúá Méjì",
    "Ìrẹtẹ̀ Méjì",
    "Ọ̀ṣẹ́ Méjì",
    "Òfún Méjì",
]

ODU_IFA_UPDATE: Dict[str, Any] = {
    "sub_variants": PRINCIPAL_16_ODU,
    "proverbs_and_oral_traditions": [
        "Ifá kì í purọ́, Ọ̀rúnmìlà kì í ṣèké; bí ayé ń yí padà, òtítọ́ inú odù kò ní yẹ̀. (Ifá never lies, nor does Ọ̀rúnmìlà practice deceit; though the earthly world shifts and wavers, the inner truth inscribed within the sacred Odù remains eternal and immutable: Teaching that moral truth and cosmic order are permanent foundations against mortal vicissitudes.)",
        "Ẹni tó mọ Odù Ifá ló mọ ọ̀rọ̀ ayé; àkọsílẹ̀ àìkú ni àwọn awo ń kà nínú ìyẹ̀ròsùn. (He who understands the sacred chapters of Odù understands the deep mysteries of the universe; it is an imperishable metaphysical scripture that the initiates read upon the sacred divination dust: Affirming that the 256 Odù encapsulate total civilizational wisdom, ethical judgment, and cosmic science.)",
        "Ojú Odù mẹ́rìndínlógún ni àpótí ìmọ̀; ẹni tí ó bá tẹ̀ ẹ́ kì í dáràn nílé ayé. (The sixteen primordial principal Odù constitute the sovereign treasury of wisdom; whoever anchors their life to their moral decrees shall never stumble into ruin in this terrestrial realm: Reaffirming that observance of spiritual taboos and ethical character secures divine protection.)",
    ],
    "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art.",
}

IFA_UPDATE: Dict[str, Any] = {
    "proverbs_and_oral_traditions": [
        "Ifá ló loni, Ifá ló l’ọ̀la, Ifá ló l’ọ̀tuntun ọjọ́ mọ́kàndínlógún; Ọ̀rúnmìlà ló ni gbogbo ọjọ́ orí wa. (Ifá owns today, Ifá owns tomorrow, Ifá owns the cyclical dawn of the nineteenth day; Ọ̀rúnmìlà is the master custodian of all our life's span: Acknowledging supreme divine governance over destiny and the flow of cosmic time.)",
        "Bí a bá bọ́jú, Ifá là ń kọ́kọ́ gbé yẹ̀ wò; a kì í fọwọ́ rọ́ ìmọ̀ràn àwọn àgbà. (When we awake to the dawn, it is the wisdom of Ifá we first consult; one does not brush aside the counsel of the sacred elders: Teaching humility and moral discernment before action.)",
        "Ifá kì í puro, òtítọ́ inú ni Ifá ń gbé; awo kì í dalẹ̀, ẹni tó bá dalẹ̀ á bá awo lọ. (Ifá never speaks falsehood, it is pure truth of the heart that Ifá elevates; an initiate never betrays the covenant, for whoever betrays the sacred oath shall meet spiritual reckoning: Enforcing the inviolable ethics of character and truth.)",
    ],
    "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa; Johnson, Rev. Samuel (1921). The History of the Yorubas; Verger, Pierre (1995). Dieux d'Afrique / Òrìṣà: Les Dieux Yorouba en Afrique et au Nouveau Monde.",
}


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_constellation(corpus: List[Dict[str, Any]]) -> None:
    for entity in corpus:
        title = entity.get("title")
        ent_id = entity.get("id")

        if title == "Odù Ifá" or ent_id == "Odù_Ifá":
            entity["sub_variants"] = list(ODU_IFA_UPDATE["sub_variants"])
            entity["proverbs_and_oral_traditions"] = list(ODU_IFA_UPDATE["proverbs_and_oral_traditions"])
            entity["provenance_and_citations"] = ODU_IFA_UPDATE["provenance_and_citations"]

            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["sub_variants"] = list(ODU_IFA_UPDATE["sub_variants"])
                entity["details"]["proverbs_and_oral_traditions"] = list(ODU_IFA_UPDATE["proverbs_and_oral_traditions"])
                entity["details"]["provenance_and_citations"] = ODU_IFA_UPDATE["provenance_and_citations"]

            print(f"  ✅ Updated '{title}' ({ent_id}) sub_variants: {len(entity['sub_variants'])} Odù")

        elif title == "Ifá" or ent_id == "Ifá":
            # Retain non-odu sub-variants, ensure all 16 principal Odù are present
            existing_subs = entity.get("sub_variants", [])
            merged_subs: List[str] = []
            for item in existing_subs:
                if item not in merged_subs:
                    merged_subs.append(item)
            for odu in PRINCIPAL_16_ODU:
                if odu not in merged_subs:
                    merged_subs.append(odu)

            entity["sub_variants"] = merged_subs
            entity["proverbs_and_oral_traditions"] = list(IFA_UPDATE["proverbs_and_oral_traditions"])
            entity["provenance_and_citations"] = IFA_UPDATE["provenance_and_citations"]

            if "details" in entity and isinstance(entity["details"], dict):
                entity["details"]["sub_variants"] = merged_subs
                entity["details"]["proverbs_and_oral_traditions"] = list(IFA_UPDATE["proverbs_and_oral_traditions"])
                entity["details"]["provenance_and_citations"] = IFA_UPDATE["provenance_and_citations"]

            print(f"  ✅ Updated '{title}' ({ent_id}) sub_variants: {len(entity['sub_variants'])} items")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: COMPLETING ODÙ IFÁ CONSTELLATION & CITATIONAL ENRICHMENT")
    print("=" * 80)

    print(f"📂 Loading API corpus from {API_CORPUS_PATH}...")
    api_corpus = load_json(API_CORPUS_PATH)
    print(f"📂 Loading Web corpus from {WEB_CORPUS_PATH}...")
    web_corpus = load_json(WEB_CORPUS_PATH)

    print("\n▶ Updating API corpus...")
    update_constellation(api_corpus)

    print("\n▶ Updating Web corpus...")
    update_constellation(web_corpus)

    print("\n💾 Persisting updated corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)

    print("✅ Successfully synchronized API and Web corpora.")
    print("=" * 80)


if __name__ == "__main__":
    main()
