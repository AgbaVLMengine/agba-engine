#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: THE GREAT RE-WIRING PASS (Sprint 004 / Checkpoint 052)
=============================================================================
Wired 248 orphaned standalone records to their Sovereign Parents in lockstep across:
  - api/data/yoruba_corpus_1007_NORMALIZED.json
  - web/src/data/yoruba_master_corpus.json

Execution Directives:
  1. Consolidate Fìlà family & twin nodes (deduplicate Filà Abetíajá, fix Vietnamese 'ị' in Fìlà Gọ̀bị́).
  2. Wire Paramount Monarchs (Awùjalẹ̀, Déjì, Akárìgbò, Ọlọ́fà, Alárá, Arẹ́sà) to 'Ọba' + bilateral kingdom links.
  3. Wire ancient capitals to their State Sovereign Parents.
  4. Wire all orphaned sub-variant entities declared by Sovereign Parents.
"""

import json
import re
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"

def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s.strip()) if s else ""

def strip_accents(s: str) -> str:
    if not s:
        return ""
    return "".join(c for c in unicodedata.normalize("NFD", str(s)) if unicodedata.category(c) != "Mn").lower()

def execute_rewiring():
    print("🚀 Starting the Great Re-Wiring Pass...")
    with open(API_CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    print(f"   Initial Corpus Size: {len(corpus)} entities")

    # 1. Consolidate Fìlà family & twin nodes
    # Merge 'Filà Abetíajá' into 'Fìlà Abetí Ajá'
    abetiaja_legacy = next((e for e in corpus if e.get("title") == "Filà Abetíajá"), None)
    abetiaja_canon = next((e for e in corpus if e.get("title") == "Fìlà Abetí Ajá"), None)
    if abetiaja_legacy and abetiaja_canon:
        if not abetiaja_canon.get("provenance_and_citations"):
            abetiaja_canon["provenance_and_citations"] = abetiaja_legacy.get("provenance_and_citations")
        legacy_aliases = abetiaja_legacy.get("aliases", [])
        canon_aliases = abetiaja_canon.get("aliases", [])
        for a in legacy_aliases:
            if a not in canon_aliases:
                canon_aliases.append(a)
        abetiaja_canon["aliases"] = canon_aliases
        corpus.remove(abetiaja_legacy)
        print("   ✅ Merged twin node 'Filà Abetíajá' -> canonical 'Fìlà Abetí Ajá'")

    # Fix Vietnamese 'ị' in 'Fìlà Gọ̀bị́' -> canonical 'Fìlà Gọ̀bí'
    for e in corpus:
        if "gọ̀bị́" in e.get("title", "").lower() or e.get("id") == "Fìlà Gọ̀bị́":
            e["id"] = "Fìlà Gọ̀bí"
            e["title"] = "Fìlà Gọ̀bí"
            e["aliases"] = [a.replace("gọ̀bị́", "gọ̀bí").replace("Gọ̀bị́", "Gọ̀bí") for a in e.get("aliases", [])]
            if "fìlà gọ̀bí" not in e["aliases"]:
                e["aliases"].append("fìlà gọ̀bí")
            if "description" in e:
                e["description"] = e["description"].replace("Gọ̀bị́", "Gọ̀bí").replace("gọ̀bị́", "gọ̀bí")
            if "etymology_and_philosophy" in e:
                e["etymology_and_philosophy"] = e["etymology_and_philosophy"].replace("Gọ̀bị́", "Gọ̀bí").replace("gọ̀bị́", "gọ̀bí")
            if "details" in e and isinstance(e["details"], dict):
                e["details"]["title"] = "Fìlà Gọ̀bí"
                e["details"]["id"] = "Fìlà Gọ̀bí"
            print("   ✅ Fixed Vietnamese 'ị' in 'Fìlà Gọ̀bị́' -> 'Fìlà Gọ̀bí'")

    # Wire Fìlà sub-variants under Sovereign Parent 'Fìlà'
    fila_parent = next((e for e in corpus if e.get("title") == "Fìlà"), None)
    if fila_parent:
        canonical_fila_variants = [
            "Fìlà Gọ̀bí", "Fìlà Abetí Ajá", "Fìlà Ọ̀ránmíyàn", "Fìlà Oníderè",
            "Fìlà Kọ̀gbọ́n", "Filà Oníde", "Fìlà Labankada", "Filà Kọ̀ṣeébàá", "Àkẹ̀tẹ̀"
        ]
        fila_parent["sub_variants"] = canonical_fila_variants
        for fv in canonical_fila_variants:
            fv_clean = strip_accents(fv)
            match = next((e for e in corpus if strip_accents(e.get("title", "")) == fv_clean or strip_accents(e.get("id", "")) == fv_clean), None)
            if match and not match.get("is_parent"):
                match["sovereign_parent"] = "Fìlà"
                match["sovereign_parent_status"] = "Living Sub-Variant"
                if "details" in match and isinstance(match["details"], dict):
                    match["details"]["sovereign_parent"] = "Fìlà"
                    match["details"]["sovereign_parent_status"] = "Living Sub-Variant"
        print("   ✅ Consolidated Fìlà Family under Sovereign Parent 'Fìlà'")

    # 2. Wire Paramount Monarchs (Awùjalẹ̀, Déjì, Akárìgbò, Ọlọ́fà, Alárá, Arẹ́sà) to 'Ọba'
    monarch_kingdom_map = {
        "Awujalẹ": {"canon_title": "Awùjalẹ̀", "kingdom_id": "Ìjẹ̀bú-Òde", "kingdom_title": "Ìjẹ̀bú-Òde", "state": "Ìpínlẹ̀ Ògùn"},
        "Deji": {"canon_title": "Déjì", "kingdom_id": "Akúrẹ́", "kingdom_title": "Akúrẹ́", "state": "Ìpínlẹ̀ Òndó"},
        "Akarigbo": {"canon_title": "Akárìgbò", "kingdom_id": "Ìpínlẹ̀ Ògùn", "kingdom_title": "Ìpínlẹ̀ Ògùn", "state": "Ìpínlẹ̀ Ògùn"},
        "Olofa": {"canon_title": "Ọlọ́fà", "kingdom_id": "ofa_kwara_city", "kingdom_title": "Ọ̀fà (Historical City & Ancient Kingdom)", "state": "Ìpínlẹ̀ Kwara"},
        "Alara": {"canon_title": "Alárá", "kingdom_id": "Ìpínlẹ̀ Èkìtì", "kingdom_title": "Ìpínlẹ̀ Èkìtì", "state": "Ìpínlẹ̀ Èkìtì"},
        "Aresa": {"canon_title": "Arẹ́sà", "kingdom_id": "Ìpínlẹ̀ Ọ̀yọ́", "kingdom_title": "Ìpínlẹ̀ Ọ̀yọ́", "state": "Ìpínlẹ̀ Ọ̀yọ́"},
    }

    oba_parent = next((e for e in corpus if e.get("title") == "Ọba"), None)
    if oba_parent:
        if not oba_parent.get("sub_variants"):
            oba_parent["sub_variants"] = []
        if not oba_parent.get("related_entities"):
            oba_parent["related_entities"] = []

        for m_id, m_info in monarch_kingdom_map.items():
            monarch_ent = next((e for e in corpus if e.get("id") == m_id or strip_accents(e.get("title", "")) == strip_accents(m_info["canon_title"])), None)
            if monarch_ent:
                monarch_ent["sovereign_parent"] = "Ọba"
                monarch_ent["sovereign_parent_status"] = "Living Sub-Variant"
                if not monarch_ent.get("related_entities"):
                    monarch_ent["related_entities"] = []
                for link in ["Ọba", m_info["kingdom_title"], m_info["state"]]:
                    if link not in monarch_ent["related_entities"]:
                        monarch_ent["related_entities"].append(link)

                if m_info["canon_title"] not in oba_parent["sub_variants"]:
                    oba_parent["sub_variants"].append(m_info["canon_title"])
                if m_info["canon_title"] not in oba_parent["related_entities"]:
                    oba_parent["related_entities"].append(m_info["canon_title"])

            # Link kingdom entity bidirectionally
            kid = m_info["kingdom_id"]
            k_ent = next((e for e in corpus if e.get("id") == kid or e.get("title") == m_info["kingdom_title"]), None)
            if k_ent:
                if not k_ent.get("related_entities"):
                    k_ent["related_entities"] = []
                if m_info["canon_title"] not in k_ent["related_entities"]:
                    k_ent["related_entities"].append(m_info["canon_title"])

        print("   ✅ Wired Paramount Monarchs to 'Ọba' and linked bidirectionally to kingdoms")

    # 3. Wire ancient capitals to their State Sovereign Parents
    capitals_map = {
        "Ilé-Ifẹ̀": "Ìpínlẹ̀ Ọ̀ṣun",
        "Òṣogbo": "Ìpínlẹ̀ Ọ̀ṣun",
        "Ìbàdàn": "Ìpínlẹ̀ Ọ̀yọ́",
        "Ọ̀yọ́-Ilé": "Ìpínlẹ̀ Ọ̀yọ́",
        "Ilọrin": "Ìpínlẹ̀ Kwara",
        "Ìjẹ̀bú-Òde": "Ìpínlẹ̀ Ògùn",
        "Abeokuta": "Ìpínlẹ̀ Ògùn",
    }
    for cap_name, st_name in capitals_map.items():
        cap_clean = strip_accents(cap_name)
        for e in corpus:
            if strip_accents(e.get("title", "")) == cap_clean or strip_accents(e.get("id", "")) == cap_clean:
                if not e.get("is_parent"):
                    e["sovereign_parent"] = st_name
                    e["sovereign_parent_status"] = "Living Sub-Variant"
                    if "details" in e and isinstance(e["details"], dict):
                        e["details"]["sovereign_parent"] = st_name
                        e["details"]["sovereign_parent_status"] = "Living Sub-Variant"
    print("   ✅ Wired ancient capitals to their State Sovereign Parents")

    # 4. Wire all remaining orphaned standalone records matching any parent's sub_variants
    parents = [e for e in corpus if e.get("is_parent") or e.get("sub_variants")]
    wired_count = 0

    for p in parents:
        p_title = p.get("title")
        for sv in p.get("sub_variants", []):
            sv_name = sv if isinstance(sv, str) else sv.get("title")
            clean_sv = strip_accents(sv_name)

            for e in corpus:
                if e.get("is_parent"):
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

                if matched and not e.get("sovereign_parent"):
                    e["sovereign_parent"] = p_title
                    e["sovereign_parent_status"] = "Living Sub-Variant"
                    if "details" in e and isinstance(e["details"], dict):
                        e["details"]["sovereign_parent"] = p_title
                        e["details"]["sovereign_parent_status"] = "Living Sub-Variant"
                    wired_count += 1
                    break

    print(f"   ✅ Auto-wired {wired_count} orphaned records from Sovereign Parent manifests")

    # Verify total entities currently having sovereign_parent populated
    has_sp = len([e for e in corpus if e.get("sovereign_parent")])
    is_p = len([e for e in corpus if e.get("is_parent")])
    print(f"   📊 Final Stats: {len(corpus)} total entities | {is_p} Sovereign Parents | {has_sp} Wired Sub-Variants")

    # Save to both target files in lockstep
    with open(API_CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    print(f"   💾 Saved to {API_CORPUS_PATH}")

    with open(WEB_CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    print(f"   💾 Saved to {WEB_CORPUS_PATH}")

if __name__ == "__main__":
    execute_rewiring()
