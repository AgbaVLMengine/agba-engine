#!/usr/bin/env python3
"""
Modular Forensics Orchestrator & CLI Runner.
Executes the 4 forensic vectors and writes an external Markdown report.
Invariant: Sub-100 LOC, Zero-hardcoding, Standard Library only.
"""
import argparse, json, sys
from pathlib import Path
from vector_duplicates import audit_duplicates
from vector_homographs import audit_homographs
from vector_subvariants import audit_subvariants
from vector_richness import audit_richness

ROOT = Path(__file__).resolve().parent.parent.parent
CORPUS_PATH = ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
KNOWLEDGE_PATH = ROOT / "web/src/utils/subVariantKnowledge.js"
SCRATCH_DIR = ROOT / ".agents/scratch"

CANONICAL_CATS = [
    "Spiritual & Cosmological Matrix", "Attire, Textiles & Personal Adornment",
    "Monarchy, Royal Regalia & Governance", "Social Structure, Kinship & Lineage",
    "Culinary Arts & Indigenous Gastronomy", "Civilization, History & Civic Heritage",
    "Military Traditions, Weaponry & Defense", "Visual Arts, Sculpture & Guild Metallurgy",
    "Topography, Natural Landscapes & Architecture", "Auditory Arts, Music, Drums & Chants",
    "Sacred Botany, Flora & Herbal Medicine", "Oral Literature, Philosophy & Folklore",
    "Traditional Trades, Agriculture & Agrarian Guilds", "Royal Regalia, Sacred Art & Architecture",
    "Ancestral Masquerades & Funerary Rites", "Festivals, Celebrations & Civic Pageantry",
    "Indigenous Zoology, Sacred Fauna & Wildlife"
]

def write_report(cat_name, dups, homos, subs, rich, out_file):
    lines = [
        f"# 🏛️ Àgbà Engine Forensics Pathology Report: {cat_name}\n",
        f"- **Duplicates/Triplicates**: {len(dups)} | **Homographs**: {len(homos)}",
        f"- **Ghost Sub-Variants**: {subs['ghost_count']} (SVIS: {subs['svis_score']}%)",
        f"- **Thin Entities (<600 chars)**: {rich['thin_count']} | **Scanty Proverbs (<3)**: {rich['scanty_proverb_count']}",
        f"- **Leaked Prompt Prefixes**: {rich['leaked_prompt_count']}\n",
        "## 1. Duplicate & Triplicate Pairs",
    ]
    lines += [f"- **{d['entity_a']}** ({d['id_a']}) ↔ **{d['entity_b']}** ({d['id_b']}): {d['reason']}" for d in dups[:20]]
    lines += ["\n## 2. Cross-Category Homograph Collisions"]
    lines += [f"- **{h['target_title']}** ({h['target_category']}) collides with **{h['colliding_title']}** ({h['colliding_category']})" for h in homos]
    lines += ["\n## 3. Ghost Sub-Variants (Sample)"]
    lines += [f"- Parent **{g['parent']}**: `{g['ghost_variant']}`" for g in subs["ghosts"][:20]]
    lines += ["\n## 4. Leaked Metadata Prompt Prefixes"]
    lines += [f"- **{p['title']}**: `{p['matched_pattern']}` in *{p['snippet']}*" for p in rich["leaked_prompts"]]
    out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Àgbà Engine Modular Forensics")
    parser.add_argument("--category", type=str, help="Category number (1-17) or name")
    parser.add_argument("--all", action="store_true", help="Audit all categories")
    args = parser.parse_args()

    with open(CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)
    cat_map = {str(i): cat for i, cat in enumerate(CANONICAL_CATS, 1)}

    target_cats = CANONICAL_CATS if args.all else []
    if args.category:
        val = str(int(args.category)) if args.category.isdigit() else args.category
        target_cats = [cat_map[val]] if val in cat_map else [c for c in CANONICAL_CATS if args.category.lower() in c.lower()]

    if not target_cats:
        print("Please specify a valid --category (1-17) or --all"); sys.exit(1)

    for cat in target_cats:
        print(f"🔬 Auditing Category: {cat}...")
        c_entities = [e for e in corpus if e.get("category") == cat]
        dups = audit_duplicates(c_entities)
        homos = audit_homographs(c_entities, corpus)
        subs = audit_subvariants(c_entities, corpus, KNOWLEDGE_PATH)
        rich = audit_richness(c_entities)

        cat_idx = CANONICAL_CATS.index(cat) + 1
        out_path = SCRATCH_DIR / f"forensics_cat{cat_idx:02d}_report.md"
        write_report(cat, dups, homos, subs, rich, out_path)
        print(f"✅ Report inscribed: {out_path} (Dups: {len(dups)}, Homos: {len(homos)}, Ghosts: {subs['ghost_count']}, Thin: {rich['thin_count']})")

if __name__ == "__main__":
    main()
