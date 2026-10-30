#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: UNIVERSAL SOVEREIGN CONSTELLATION RE-WIRER (v6.2.0)
=============================================================================
Author: Àgbẹ̀dẹ (agbede-builder) & Lead Architect Àrùnà Ọlànrewájú Kábírù
Modular Task: HANDOFF-AGBEDE-005 (Universal Constellation Hierarchy Pass)
Gate 2 Compliant (< 500 LOC)

Systematic corpus-wide hierarchy pass across all 17 categories:
  1. Monarchy & Governance:
     - Baṣọ̀run: Sovereign Parent Concept with sub-variants Basọ̀run Gáà, Basọ̀run Olúyọ̀lé, Ọ̀yọ́ Mèsì, Igbá Ìwà, Idà Ọrọ̀
     - Wire Basọ̀run Gáà as Living Sub-Variant
     - Wire monarch dynasties (Aláàfin and Ọọ̀ni lineages) to Sovereign Parent Ọba
  2. Metallurgy & Weaponry:
     - Ògún: Cosmic Sovereign Parent with sub-variants Àdá Ìbílẹ̀, Idà Agẹmọ, Ọ̀kọ̀ Ẹlẹ́ṣin, Ọfà Ọdẹ, Ẹwiri Blacksmith Hearth
     - Wire Ẹwiri to trade/blacksmith guild & link to Ògún
  3. Textiles & Regalia:
     - Agbádá: Sovereign Parent Concept with sub-variants Sányán, Ẹ̀tù, Àlàárì
     - Wire Sányán, Àlàárì, and Ẹ̀tù (re-wiring from Òògùn) to Sovereign Parent Agbádá
     - Adé: Sovereign Parent Concept with Adé Ààrẹ, Adé Ọ̀kín, Adé Ilẹ̀kẹ̀
  4. Auditory & Chants:
     - Dùndún: Sovereign Parent Concept with Gángan, Ìyáàlù Dùndún, Goje
     - Wire Goje as Living Sub-Variant under Dùndún
  5. Universal 17-Category Sweep:
     - Audit all Sovereign Parents and auto-link matching unparented child entities
"""

import json
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"


def strip_accents(s: str) -> str:
    if not s:
        return ""
    return "".join(c for c in unicodedata.normalize("NFD", str(s)) if unicodedata.category(c) != "Mn").lower().strip()


def normalize_nfc(s: str) -> str:
    return unicodedata.normalize("NFC", str(s).strip()) if s else ""


def update_entity_details(entity: dict) -> None:
    if "details" in entity and isinstance(entity["details"], dict):
        for k in ["is_parent", "sovereign_parent", "sovereign_parent_status", "category"]:
            if k in entity:
                entity["details"][k] = entity[k]


def rewire_universal_constellations():
    print("🔨 Starting Universal Sovereign Constellation Re-Wiring Pass...")

    with open(API_CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    initial_count = len(corpus)
    print(f"   📊 Initial Master Corpus Size: {initial_count} entities")

    # Fast lookup by ID and Title
    entity_by_id = {e.get("id"): e for e in corpus if e.get("id")}
    entity_by_title = {e.get("title"): e for e in corpus if e.get("title")}

    # --------------------------------------------------------------------------
    # 1. Monarchy & Governance Constellation
    # --------------------------------------------------------------------------
    # A. Baṣọ̀run
    basorun = entity_by_id.get("Baṣọ̀run")
    if basorun:
        basorun["is_parent"] = True
        basorun["sovereign_parent_status"] = "Sovereign Parent Concept"
        basorun["sovereign_parent"] = None
        basorun_variants = ["Basọ̀run Gáà", "Basọ̀run Olúyọ̀lé", "Ọ̀yọ́ Mèsì", "Igbá Ìwà", "Idà Ọrọ̀"]
        current_sub = basorun.get("sub_variants") or []
        for v in basorun_variants:
            if v not in current_sub:
                current_sub.append(v)
        basorun["sub_variants"] = current_sub
        update_entity_details(basorun)
        print("   ✅ Configured 'Baṣọ̀run' as Sovereign Parent Concept with 5 core variants")

    # Wire Basọ̀run Gáà
    basorun_gaa = entity_by_id.get("Basọ̀run Gáà")
    if basorun_gaa:
        basorun_gaa["is_parent"] = False
        basorun_gaa["sovereign_parent"] = "Baṣọ̀run"
        basorun_gaa["sovereign_parent_status"] = "Living Sub-Variant"
        update_entity_details(basorun_gaa)
        print("   ✅ Wired 'Basọ̀run Gáà' -> sovereign_parent: 'Baṣọ̀run'")

    # B. Ọba and Royal Dynasties (Aláàfin & Ọọ̀ni lineages)
    oba = entity_by_id.get("Ọba")
    if oba:
        oba["is_parent"] = True
        oba["sovereign_parent_status"] = "Sovereign Parent Concept"
        update_entity_details(oba)

    monarch_dynasties = [
        "Aláàfin Ọ̀rànmíyàn", "Aláàfin Àtìbà", "Àfin Aláàfin", "Ìtàn Àwọn Aláàfin Ọ̀yọ́",
        "Ọọ̀ni Odùduwà", "Àfin Ọọ̀ni", "Ooni Lúwo Gbàgìdá", "Ọọ̀ni Adérẹ̀mí"
    ]
    for dyn_id in monarch_dynasties:
        ent = entity_by_id.get(dyn_id)
        if ent and not ent.get("sovereign_parent"):
            ent["sovereign_parent"] = "Ọba"
            ent["sovereign_parent_status"] = "Living Sub-Variant"
            ent["is_parent"] = False
            update_entity_details(ent)
            print(f"   ✅ Wired Monarch Dynasty '{dyn_id}' -> sovereign_parent: 'Ọba'")

    # --------------------------------------------------------------------------
    # 2. Metallurgy & Weaponry Constellation (Ògún)
    # --------------------------------------------------------------------------
    ogun = entity_by_id.get("CORPUS_OGUN_COSMIC_001")
    if ogun:
        ogun["is_parent"] = True
        ogun["sovereign_parent_status"] = "Sovereign Parent Concept"
        ogun_variants = [
            "Ògún Lákàyé", "Ògún Alágbede (Blacksmith)", "Ògún Ọdẹ (Hunter)", "Ògún Balógun (Warrior)",
            "Àdá Ìbílẹ̀", "Idà Agẹmọ", "Ọ̀kọ̀ Ẹlẹ́ṣin", "Ọfà Ọdẹ", "Ẹwiri Blacksmith Hearth"
        ]
        curr_ogun_sub = ogun.get("sub_variants") or []
        for v in ogun_variants:
            if v not in curr_ogun_sub:
                curr_ogun_sub.append(v)
        ogun["sub_variants"] = curr_ogun_sub
        update_entity_details(ogun)
        print("   ✅ Configured 'Ògún' with full martial & metallurgy constellation")

    # Wire Ẹwiri
    ewiri = entity_by_id.get("Ẹwiri")
    if ewiri:
        rel = ewiri.get("related_entities") or []
        if "Ògún" not in rel:
            rel.append("Ògún")
        ewiri["related_entities"] = rel
        print("   ✅ Linked 'Ẹwiri' to Ògún metallurgy network")

    # --------------------------------------------------------------------------
    # 3. Textiles & Regalia Constellation (Agbádá & Adé)
    # --------------------------------------------------------------------------
    agbada = entity_by_id.get("Agbádá")
    if agbada:
        agbada["is_parent"] = True
        agbada["sovereign_parent_status"] = "Sovereign Parent Concept"
        agbada["sub_variants"] = ["Sányán", "Ẹ̀tù", "Àlàárì"]
        update_entity_details(agbada)
        print("   ✅ Configured 'Agbádá' as Sovereign Parent with Sányán, Ẹ̀tù, Àlàárì")

    # Wire Sányán and Àlàárì
    for textile_id in ["Sányán", "Àlàárì"]:
        textile = entity_by_id.get(textile_id)
        if textile:
            textile["sovereign_parent"] = "Agbádá"
            textile["sovereign_parent_status"] = "Living Sub-Variant"
            textile["is_parent"] = False
            update_entity_details(textile)
            print(f"   ✅ Wired Textile '{textile_id}' -> sovereign_parent: 'Agbádá'")

    # Re-wire Ẹ̀tù from Òògùn to Agbádá
    etu = entity_by_id.get("Ẹ̀tù")
    if etu:
        etu["sovereign_parent"] = "Agbádá"
        etu["sovereign_parent_status"] = "Living Sub-Variant"
        etu["is_parent"] = False
        update_entity_details(etu)
        print("   ✅ Re-wired Textile 'Ẹ̀tù' from medicine to sovereign_parent: 'Agbádá'")

    # Adé
    ade = entity_by_id.get("Adé")
    if ade:
        ade["is_parent"] = True
        ade["sovereign_parent_status"] = "Sovereign Parent Concept"
        ade_variants = ["Adé Ààrẹ", "Adé Ọ̀kín", "Adé Ìlẹ̀kẹ̀", "Adé Ọlọ́kun", "Adé Oríṣà", "Adé Aládé", "Adé Babaláwo"]
        curr_ade_sub = ade.get("sub_variants") or []
        for v in ade_variants:
            if v not in curr_ade_sub:
                curr_ade_sub.append(v)
        ade["sub_variants"] = curr_ade_sub
        update_entity_details(ade)
        print("   ✅ Configured 'Adé' Sovereign Parent Concept with full royal crown hierarchy")

    # --------------------------------------------------------------------------
    # 4. Auditory & Chants Constellation (Dùndún)
    # --------------------------------------------------------------------------
    dundun = entity_by_id.get("Dùndún")
    if dundun:
        dundun["is_parent"] = True
        dundun["sovereign_parent_status"] = "Sovereign Parent Concept"
        dundun_variants = ["Ìyáàlù Dùndún", "Gángan", "Gúdúgúdú", "Kẹríkẹrì", "Ìsájú", "Kànàgó", "Goje"]
        curr_dundun_sub = dundun.get("sub_variants") or []
        for v in dundun_variants:
            if v not in curr_dundun_sub:
                curr_dundun_sub.append(v)
        dundun["sub_variants"] = curr_dundun_sub
        update_entity_details(dundun)
        print("   ✅ Configured 'Dùndún' Sovereign Parent Concept with complete drum ensemble")

    # Wire Goje
    goje = entity_by_id.get("Goje")
    if goje:
        goje["sovereign_parent"] = "Dùndún"
        goje["sovereign_parent_status"] = "Living Sub-Variant"
        goje["is_parent"] = False
        update_entity_details(goje)
        print("   ✅ Wired 'Goje' -> sovereign_parent: 'Dùndún'")

    # --------------------------------------------------------------------------
    # 5. Universal 17-Category Sweep
    # --------------------------------------------------------------------------
    # Ensure all Sovereign Parents declare "Sovereign Parent Concept"
    parents = [e for e in corpus if e.get("is_parent") or e.get("sub_variants")]
    for p in parents:
        if p.get("is_parent") and not p.get("sovereign_parent"):
            p["sovereign_parent_status"] = "Sovereign Parent Concept"
            update_entity_details(p)

    auto_wired_count = 0
    for p in parents:
        p_title = p.get("title")
        for sv in p.get("sub_variants", []):
            sv_name = sv if isinstance(sv, str) else sv.get("title")
            clean_sv = strip_accents(sv_name)

            for e in corpus:
                if e.get("is_parent"):
                    continue
                # Do not re-wire entities that already declare a sovereign_parent
                if e.get("sovereign_parent"):
                    continue

                e_title_clean = strip_accents(e.get("title", ""))
                e_aliases_clean = [strip_accents(a) for a in e.get("aliases", [])]
                e_id_clean = strip_accents(e.get("id", ""))

                matched = False
                if clean_sv == e_title_clean or clean_sv in e_aliases_clean or clean_sv == e_id_clean:
                    matched = True
                elif e_title_clean.startswith(clean_sv + " ("):
                    matched = True
                elif "(" in clean_sv and clean_sv.split("(")[0].strip() == e_title_clean:
                    matched = True

                if matched:
                    e["sovereign_parent"] = p_title
                    e["sovereign_parent_status"] = "Living Sub-Variant"
                    e["is_parent"] = False
                    update_entity_details(e)
                    auto_wired_count += 1
                    break

    print(f"   ✅ Auto-wired {auto_wired_count} additional orphaned entities across all 17 categories")

    # --------------------------------------------------------------------------
    # 6. Verification and Lockstep Persistence
    # --------------------------------------------------------------------------
    final_count = len(corpus)
    has_sp = len([e for e in corpus if e.get("sovereign_parent")])
    is_p = len([e for e in corpus if e.get("is_parent")])

    print(f"   📊 Final Stats: {final_count} entities | {is_p} Sovereign Parents | {has_sp} Wired Sub-Variants")
    assert final_count == initial_count, f"Corpus size changed! Expected {initial_count}, got {final_count}"

    with open(API_CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    print(f"   💾 Saved in lockstep to {API_CORPUS_PATH}")

    with open(WEB_CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    print(f"   💾 Saved in lockstep to {WEB_CORPUS_PATH}")


if __name__ == "__main__":
    rewire_universal_constellations()
