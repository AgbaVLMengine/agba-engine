#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: DISAMBIGUATION & LIVING SUB-VARIANTS INGESTION (Gate 2 <500 LOC)
Loads entities from scripts/audit_fixes_data.json and updates master corpora.
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
API_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"
DATA_PATH = REPO_ROOT / "scripts/audit_fixes_data.json"

def update_parent_subvariants(corpus):
    parent_updates = {
        "Ìpínlẹ̀ Kwara": ["Ilọrin", "Ọ̀fà (Historical City & Ancient Kingdom)"],
        "Ìpínlẹ̀ Èkó": ["Èkó (Maritime Capital & Cultural Center)", "Ìsàlẹ̀ Èkó (Ancestral Island & Core Settlement)", "Ìkòyí", "Ìkẹjà", "Bàdágbìrì", "Ẹpẹ"],
        "Ìpínlẹ̀ Kogi": ["Kàbbà (Historic Okun Kingdom & City)", "Ìjùmú (Ancestral Okun Confederacy)", "Lọ́kọ́ja", "Okene"],
        "Ìpínlẹ̀ Èkìtì": ["Adó-Èkìtì (Ancestral Capital & Seat of the Ẹwí)", "Ìkọ̀lé-Èkìtì", "Àramọkọ-Èkìtì"],
        "Ère": ["Ère Ìbejì (Sacred Twin Memorial Effigy)", "Ère Ẹlẹ́gbára (Consecrated Sculptural Icon of Èṣù)", "Ère Ọbàtálá"],
        "Owó Ẹyọ": ["Ẹyọ Owó (Unit Cowrie Shell Currency)", "Ẹgbàá", "Àpò Owó"],
        "Ikin Ifá": ["Ikin Ọlọ́jú Mẹ́rin (Four-Eyed Consecrated Palm Nut)", "Ikin Ọlọ́jú Mẹ́ta (Three-Eyed Sacred Palm Nut)"],
        "Agẹrẹ Ifá": ["Agẹrẹ Ológun (Equestrian Carved Divination Vessel)", "Agẹrẹ Arúgbá (Kneeling Maiden Caryatid Vessel)"],
        "Ọ̀pẹ̀lẹ̀": ["Ọ̀pẹ̀lẹ̀ Agbalagba (Elder Master Divination Chain)", "Ọ̀pẹ̀lẹ̀ Idẹ (Sacred Brass Divining Chain)"],
        "Ọpọ́n Ifá": ["Ọpọ́n Ifá Olórí Èṣù (Divination Tray with Crown of Èṣù)", "Ọpọ́n Ifá Gbẹ́rọ́ (Deep Relief Ceremonial Divination Tray)"],
        "Ògbóni": ["Ẹdan Ògbóni (Sanctified Cast Brass Twin Rods)", "Onílẹ̀"],
        "Ìyàwó": ["Ìyàwó Titun (The Newly Wedded Bride)", "Ẹ̀kún Ìyàwó"],
        "Ọkọ": ["Ọkọ Ìyàwó (The Matrimonial Bridegroom)", "Bàbá Ilé (Patriarch & Head of the Compound)"]
    }

    for entity in corpus:
        title = entity.get("title")
        for p_title, new_subs in parent_updates.items():
            if title == p_title or title.startswith(p_title):
                existing = entity.get("sub_variants") or []
                for s in new_subs:
                    if s not in existing:
                        existing.append(s)
                entity["sub_variants"] = existing

def main():
    print("🏛️ Ingesting Disambiguations and Living Sub-Variants...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        new_entities = json.load(f)

    for path in [API_PATH, WEB_PATH]:
        with open(path, "r", encoding="utf-8") as f:
            corpus = json.load(f)

        existing_titles = {e.get("title"): idx for idx, e in enumerate(corpus)}
        existing_ids = {e.get("id"): idx for idx, e in enumerate(corpus)}

        added = 0
        updated = 0

        for item in new_entities:
            target_idx = None
            if item["title"] in existing_titles:
                target_idx = existing_titles[item["title"]]
            elif item["id"] in existing_ids:
                target_idx = existing_ids[item["id"]]

            if target_idx is not None:
                corpus[target_idx].update(item)
                updated += 1
            else:
                corpus.append(item)
                existing_titles[item["title"]] = len(corpus) - 1
                existing_ids[item["id"]] = len(corpus) - 1
                added += 1

        update_parent_subvariants(corpus)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, ensure_ascii=False, indent=2)

        print(f"✅ {path.name}: {added} added, {updated} updated. Total now: {len(corpus)}")

if __name__ == "__main__":
    main()
