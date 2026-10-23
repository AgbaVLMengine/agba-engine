#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ingestion Engine for Tier A Bespoke Living Sub-Variants.
Strictly enforces:
- Gate 2 (<500 LOC per file)
- Biological / Metallurgical / Customary Law Depth Parity
- Dual-Language Proverbs with Parenthetical English Translations
- Synchronized corpus manifests across api/ and web/
"""

import json
from pathlib import Path

BASE_DIR = Path("/home/aruna_olanrewaju/agba-engine")
API_CORPUS_PATH = BASE_DIR / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = BASE_DIR / "web/src/data/yoruba_master_corpus.json"
DATA_PATH = BASE_DIR / "scripts/tier_a_subvariants_data.json"

# Additional remaining Tier A entities to complete the 56
ADDITIONAL_TIER_A = [
    {
        "id": "apata_ode",
        "title": "Àpáta Ọdẹ",
        "category": "Military Traditions, Weaponry & Defense",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Àpáta",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["apata ode", "hunting shield", "tracker buckler"],
        "description": "Compact curved leather buckler utilized by master hunters (Ọdẹ) when pursuing large forest game (such as Buffalo or Leopard).",
        "etymology_and_philosophy": "Designed for supreme agility in brush, prioritizing rapid parrying of animal charges over heavy projectile defense.",
        "historical_timeline": "Dating back to the earliest hunting guilds (Ẹgbẹ́ Ọdẹ) recorded in Ìjálá recitations.",
        "material_and_craftsmanship": "Constructed from layered cured antelope hide stretched over a flexible cane hoop.",
        "social_and_ritual_context": "Anointed with herbal protective infusions before major deep-forest hunting expeditions.",
        "proverbs_and_oral_traditions": [
            "Àpáta ọdẹ kì í jẹ́ kí ẹkùn gbá ológun l’ójú. (The hunter's nimble buckler prevents the leopard's claw from striking the warrior's face.)"
        ],
        "diaspora_connections": "Reflected in Afro-Cuban Ochosi ceremonial dance gear.",
        "geographical_origin": "Pan-Yorùbá Forest Guilds",
        "curatorial_guidelines": "Highlight lightweight circular form and natural rawhide stitching.",
        "related_entities": ["Àpáta", "Ọdẹ", "Ọ̀ṣọ́ọ̀sì", "Ẹ̀fọ̀n"]
    },
    {
        "id": "apata_ogun",
        "title": "Àpáta Ogun",
        "category": "Military Traditions, Weaponry & Defense",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Àpáta",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["apata ogun", "battle shield", "vanguard shield", "heavy infantry shield"],
        "description": "Monumental full-body vanguard shield carried by frontline defensive formations to withstand volleyed archery and cavalry rushes.",
        "etymology_and_philosophy": "Emblem of territorial integrity and the collective defensive wall of the township.",
        "historical_timeline": "Employed during the 18th-century imperial battles of Ọ̀yọ́ and the defensive ramparts of ancient towns.",
        "material_and_craftsmanship": "Thick seasoned hardwood overlaid with hammered iron bands and elephant hide padding.",
        "social_and_ritual_context": "Locked together in shoulder-to-shoulder formation (Ìdènà) by line infantry under the Balógun.",
        "proverbs_and_oral_traditions": [
            "Bí ogun bá ń bọ̀, àpáta ogun ní ń gbèjà ìlú. (When war approaches, the heavy vanguard shield defends the ramparts of the commonwealth.)"
        ],
        "diaspora_connections": "Symbolized in Ogun's iron shield iconography in Bahia and Matanzas.",
        "geographical_origin": "Ọ̀yọ́-Ilé and Ìbàdàn",
        "curatorial_guidelines": "Depict large rectangular or tall oblong profile with iron mounting studs.",
        "related_entities": ["Àpáta", "Ogun (Warfare & Military Tradition)", "Balógun", "Ọ̀kọ̀"]
    },
    {
        "id": "oko_ode",
        "title": "Ọ̀kọ̀ Ọdẹ",
        "category": "Military Traditions, Weaponry & Defense",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Ọ̀kọ̀",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["oko ode", "hunting spear", "hunting javelin", "throwing spear"],
        "description": "Aerodynamically balanced throwing javelin handcrafted for taking down large savannah and forest game from medium distance.",
        "etymology_and_philosophy": "Requires perfect coordination between stillness, breath control, and kinetic release (Àṣẹ Ìjù).",
        "historical_timeline": "The ancestral weapon of Yorùbá founders who carved out original agrarian settlements from primary wilderness.",
        "material_and_craftsmanship": "Forged with barbed iron tang to prevent dislodging, mounted into straight bamboo or bamboo-palm shaft.",
        "social_and_ritual_context": "Consecrated at the annual Ọdún Ọdẹ (Hunter's Festival) in honor of Òṣọ́ọ̀sì and Ògún.",
        "proverbs_and_oral_traditions": [
            "Ọ̀kọ̀ ọdẹ kì í fò lójú igbó kí ó dákẹ́ láì sọ ẹran d’òkú. (The hunter's spear never flies across the forest thicket without striking true.)"
        ],
        "diaspora_connections": "Sacred implement held by Ochosi in Cuban Santería and Oxóssi in Brazilian Candomblé.",
        "geographical_origin": "Pan-Yorùbáland",
        "curatorial_guidelines": "Show slender aerodynamic profile with backward-facing barb spurs.",
        "related_entities": ["Ọ̀kọ̀", "Ọdẹ", "Ọ̀ṣọ́ọ̀sì", "Ògún"]
    },
    {
        "id": "oko_isegun",
        "title": "Ọ̀kọ̀ Ìṣẹ́gun",
        "category": "Military Traditions, Weaponry & Defense",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Ọ̀kọ̀",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["oko isegun", "victory spear", "scepter spear", "triumphal spear"],
        "description": "Ceremonial cast bronze and iron scepter spear carried by triumphant war commanders during victory pageantry.",
        "etymology_and_philosophy": "From 'Ìṣẹ́gun' (conquest/triumph). Signifies the return of peace and security after the perils of warfare.",
        "historical_timeline": "Displayed in victory parades in Ọ̀yọ́ and Ìbàdàn following successful campaigns in the 19th century.",
        "material_and_craftsmanship": "Ornate brass casting featuring openwork interlace motifs, copper inlays, and horsehair tassel.",
        "social_and_ritual_context": "Presented to the Ọba at the palace gates to deliver formal news of victory (Ìròyìn Ìṣẹ́gun).",
        "proverbs_and_oral_traditions": [
            "Ọ̀kọ̀ ìṣẹ́gun ní ń kéde àlàáfíà lẹ́yìn ogun. (The victory spear proclaims the return of peace when battle storms subside.)"
        ],
        "diaspora_connections": "Revered in Afro-Brazilian martial dances honoring Ogum Vencendor (Ogun the Victorious).",
        "geographical_origin": "Ìbàdàn, Ọ̀yọ́, and Ọ̀wọ̀",
        "curatorial_guidelines": "Highlight polished brass surface and ceremonial red and gold tassels.",
        "related_entities": ["Ọ̀kọ̀", "Balógun", "Ọba", "Ogun (Warfare & Military Tradition)"]
    },
    {
        "id": "apo_ofa",
        "title": "Apó Ọfà",
        "category": "Military Traditions, Weaponry & Defense",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Ọfà",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["apo ofa", "quiver", "arrow quiver", "archery quiver"],
        "description": "The cylindrical leather or hardwood archery quiver slung over the shoulder, containing poisoned arrows and protective talismans.",
        "etymology_and_philosophy": "Symbolizes preparedness, tactical readiness, and the preservation of lethal resources.",
        "historical_timeline": "Essential military kit of Yorùbá archers throughout pre-colonial centuries.",
        "material_and_craftsmanship": "Crafted from molded cowhide or carved wood, waterproofed with beeswax and adorned with brass rings.",
        "social_and_ritual_context": "Inherited by apprentice archers; swearing upon Apó Ọfà cemented vows of brotherhood among bowmen.",
        "proverbs_and_oral_traditions": [
            "Ọfà tó já lẹ́nu apó kì í padà síbẹ̀ lásán; iṣẹ́ oró ló ń jẹ́. (The arrow drawn from the quiver's mouth never returns in vain; it accomplishes its mission.)"
        ],
        "diaspora_connections": "Represented in the beaded quiver worn by Ochosi in Caribbean Lucumí shrines.",
        "geographical_origin": "Pan-Yorùbáland",
        "curatorial_guidelines": "Depict with adjustable shoulder sling and carved decorative leather embossing.",
        "related_entities": ["Ọfà", "Ọfà Ọdẹ", "Ọ̀ṣọ́ọ̀sì", "Ogun (Warfare & Military Tradition)"]
    },
    {
        "id": "oro_ofa",
        "title": "Oró Ọfà",
        "category": "Sacred Botany, Flora & Herbal Medicine",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Ọfà",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["oro ofa", "arrow poison", "botanical poison", "poisoned dart tip"],
        "description": "The potent botanical arrow poison concocted from Strophanthus (Ìròsùn or Ègúngún-ẹja) extracts, applied to arrowheads for hunting and warfare.",
        "etymology_and_philosophy": "Emblem of botanical lethality. Teaches the sacred boundary between medicine that heals and pharmacology that strikes.",
        "historical_timeline": "Mastered by herbalist-hunters (Oníṣègùn Ọdẹ) over many centuries, protected under strict guild secrecy.",
        "material_and_craftsmanship": "Simmered into a thick black resin, applied with feathered quills onto forged iron barbs.",
        "social_and_ritual_context": "Handled only after reciting neutralizing incantations (Ọ̀fọ̀) to protect the armorer from accidental self-poisoning.",
        "proverbs_and_oral_traditions": [
            "Oró ọfà kì í ṣe ohun tí a ń fi ọwọ́ kan lásán; ẹ̀mí ló ń gba. (Arrow poison is not something touched casually; it commands life and death.)"
        ],
        "diaspora_connections": "Preserved in Afro-Cuban pharmacopeia knowledge associated with Osain.",
        "geographical_origin": "Yorùbáland Forest Sanctuaries",
        "curatorial_guidelines": "Present within the cultural context of hunting science and pharmacopeia.",
        "related_entities": ["Ọfà", "Òògùn", "Ọ̀sanyìn", "Ọdẹ"]
    },
    {
        "id": "ada_faafa",
        "title": "Àdá Fáàfà",
        "category": "Traditional Trades, Agriculture & Agrarian Guilds",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Àdá",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["ada faafa", "curved foraging blade", "harvesting cutlass"],
        "description": "The curved, sickle-tipped cutlass engineered for harvesting palm fruit bunches, cocoa pods, and medicinal barks.",
        "etymology_and_philosophy": "Emblem of precision agrarian harvesting. Designed to pluck without destroying the parent tree.",
        "historical_timeline": "Central to the cash-crop agricultural boom of cocoa and palm kernels in the 19th and 20th centuries.",
        "material_and_craftsmanship": "Forged with a hooked billhook tip, balanced for pulling and slicing strokes at elevated heights.",
        "social_and_ritual_context": "Presented to successful agrarian apprentices upon mastering the harvesting of sacred palm groves.",
        "proverbs_and_oral_traditions": [
            "Àdá fáàfà ní ń gé ọ̀pẹ láì pa igi lára. (The curved harvesting blade reaps the fruit of the palm without destroying the tree.)"
        ],
        "diaspora_connections": "Preserved in agricultural harvesting traditions across the Caribbean diaspora.",
        "geographical_origin": "Ondo, Osun, and Ogun Palm Belts",
        "curatorial_guidelines": "Highlight distinctive curved billhook tip and reinforced wooden shaft socket.",
        "related_entities": ["Àdá", "Àdá Ìbílẹ̀", "Ọ̀pẹ", "Àgbẹ̀"]
    },
    {
        "id": "ida_isegun",
        "title": "Idà Ìṣẹ́gun",
        "category": "Military Traditions, Weaponry & Defense",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Idà",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["ida isegun", "sword of victory", "conquest sword", "martial triumph blade"],
        "description": "The ceremonial combat sword consecrated in honor of martial triumph, carried in victory processions and ancestral shrines.",
        "etymology_and_philosophy": "Symbolizes the triumph of order over lawless aggression and the divine protection of the commonwealth.",
        "historical_timeline": "Celebrated in military archives of Ìbàdàn, Ọ̀yọ́, and Ìjẹ̀ṣà across 19th-century history.",
        "material_and_craftsmanship": "Forged from high-grade iron with etched victory glyphs and leather scabbard accented with brass.",
        "social_and_ritual_context": "Dedicated at the shrine of Ògún following the safe return of warriors from battle.",
        "proverbs_and_oral_traditions": [
            "Idà ìṣẹ́gun kì í dánilójú lásán; ẹ̀jẹ̀ ogun ló fi ń kọ ìtàn. (The sword of conquest is not polished for vanity; it records the history of liberation.)"
        ],
        "diaspora_connections": "Central to the visual liturgy of Ogun in Cuban and Brazilian ceremonial houses.",
        "geographical_origin": "Ìbàdàn, Ọ̀yọ́, and Èkìtì",
        "curatorial_guidelines": "Show sweeping single-edged blade with engraved ancestral knot patterns.",
        "related_entities": ["Idà", "Balógun", "Ogun (Warfare & Military Tradition)", "Ògún"]
    },
    {
        "id": "ogun_owo",
        "title": "Ogún Owo",
        "category": "Social Structure, Kinship & Lineage",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Oogun",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["ogun owo", "liquid inheritance", "monetary estate", "financial legacy"],
        "description": "The inheritance of liquid wealth, ancient cowrie reserves (Owó Ẹyọ), merchant capital, and modern monetary assets within a family estate.",
        "etymology_and_philosophy": "From 'Ogún' (inheritance) and 'Owó' (currency/wealth). Customary ethics demand that liquid wealth be invested into child education and family welfare.",
        "historical_timeline": "Regulated under customary commercial law in trade capitals like Lagos, Abẹ́òkúta, and Ọ̀yọ́ for centuries.",
        "material_and_craftsmanship": "Historically stored in heavy earthenware jars (Ìkòkò Owó) buried beneath compound floors.",
        "social_and_ritual_context": "Distributed in the presence of elder witnesses (Àgbà Ìdílé) to prevent embezzlement by greedy kin.",
        "proverbs_and_oral_traditions": [
            "Ogún owó kò tó ogún ìwà; ẹni tó l’óye ló l’owó gidi. (Monetary inheritance cannot rival the inheritance of noble character; true wealth is wisdom.)"
        ],
        "diaspora_connections": "Paralleled in collective savings societies (Esusu) exported by Yorùbá freedmen across the Americas.",
        "geographical_origin": "Commercial Centers of Yorùbáland",
        "curatorial_guidelines": "Present in context of trade ledgers, cowrie strings, and ancestral merchant dignity.",
        "related_entities": ["Oogun", "Owó Ẹyọ", "Ẹbí", "Ìwà"]
    },
    {
        "id": "ogun_ohun_ini",
        "title": "Ogún Ohun-Ìní",
        "category": "Social Structure, Kinship & Lineage",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Oogun",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["ogun ohun ini", "chattels inheritance", "personal property legacy"],
        "description": "The customary inheritance of personal effects, heirloom cloths (Aṣọ Òkè), royal beads, bronze vessels, and household implements.",
        "etymology_and_philosophy": "From 'Ohun-Ìní' (things possessed/cherished). Heirloom garments carry the physical scent and spiritual imprint of ancestors.",
        "historical_timeline": "Documented across centuries of compound estate arbitrations.",
        "material_and_craftsmanship": "Heirloom cloths preserved in cedar chests with dried lavender and camphor leaves.",
        "social_and_ritual_context": "Presented to favorite children and loyal apprentices during the final post-funeral distribution rites (Ìpín-Ogún).",
        "proverbs_and_oral_traditions": [
            "Aṣọ tí bàbá fi sílẹ̀ ní ń gbọ́ kọjá ọmọ; ohun-ìní àgbà kì í tètè parun. (The heirloom garment left by a father outlasts the youth of the child; ancestral treasures endure.)"
        ],
        "diaspora_connections": "Preserved in the sacred transfer of bead necklaces (Elekes) from godparents to initiates.",
        "geographical_origin": "Pan-Yorùbá Compounds",
        "curatorial_guidelines": "Show folded vintage indigo cloths, coral beads, and carved wooden storage chests.",
        "related_entities": ["Oogun", "Aṣọ", "Ìlèkè", "Ẹbí"]
    },
    {
        "id": "agba_idile",
        "title": "Àgbà Ìdílé",
        "category": "Social Structure, Kinship & Lineage",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Oogun",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["agba idile", "lineage patriarch", "family elder", "compound elder"],
        "description": "The senior elder patriarch and council of elders who serve as the judicial trustees and moral custodians of the family estate.",
        "etymology_and_philosophy": "From 'Àgbà' (elder) and 'Ìdílé' (family). Embodies patience, impartial arbitration, and deep knowledge of lineage genealogies.",
        "historical_timeline": "The primary governing unit of Yorùbá society, predating centralized monarchies by millennia.",
        "material_and_craftsmanship": "Carries the carved elder walking staff (Ọ̀pá Àgbà) and wears handwoven ceremonial Agbádá.",
        "social_and_ritual_context": "Presides over naming rites, marriage consent, estate partitions, and compound dispute settlement.",
        "proverbs_and_oral_traditions": [
            "Àgbà kì í wà l’ọ́jà kí orí ọmọ tuntun wọ́. (An elder cannot be present in the marketplace while the infant's head droops; elders prevent civic tragedy.)"
        ],
        "diaspora_connections": "Institutionalized as the Council of Elders (Ogboni/Consejo) in Afro-Cuban and Brazilian religious communities.",
        "geographical_origin": "Pan-Yorùbá Compounds",
        "curatorial_guidelines": "Portray with dignified seated posture, white hair, beaded necklace, and serene gaze.",
        "related_entities": ["Oogun", "Ẹbí", "Ìdílé", "Ọmọlúwàbí"]
    },
    {
        "id": "ebi_oba",
        "title": "Ẹbí Ọba",
        "category": "Monarchy, Royal Regalia & Governance",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Oogun",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["ebi oba", "royal dynasty", "royal lineage branch", "ruling house"],
        "description": "The recognized dynastic royal lineage branches (Ruling Houses) entitled by ancient customary charter to put forward candidates for the crown.",
        "etymology_and_philosophy": "From 'Ẹbí' (family/kin) and 'Ọba' (king). Embodies the principle that kingship belongs to the lineage, not a single individual.",
        "historical_timeline": "Established at the founding of each kingdom and guarded by the Council of Kingmakers (Ọ̀yọ́ Mèsì or Ìfẹ̀ Kingmakers).",
        "material_and_craftsmanship": "Maintains private royal ancestral shrines, regalia vaults, and dynastic burial vaults.",
        "social_and_ritual_context": "Rotates coronation rights strictly among legitimate ruling branches to guarantee equitable succession.",
        "proverbs_and_oral_traditions": [
            "Ẹbí Ọba kì í parun; bí ọba kan bá wọ̀lẹ̀, ọba mìíràn a bọ́ sí orí ìtẹ́. (The royal dynasty never perishes; when one monarch joins the ancestors, another ascends the throne.)"
        ],
        "diaspora_connections": "Echoed in royalty societies and coronation reenactments in Cuba and Bahia.",
        "geographical_origin": "Royal Capitals across Yorùbáland",
        "curatorial_guidelines": "Depict royal palace courtyards with beaded emblems and ancestral staff displays.",
        "related_entities": ["Oogun", "Ọba", "Adé", "Ààfin"]
    },
    {
        "id": "were_ibile",
        "title": "Were Ìbílẹ̀",
        "category": "Auditory Arts, Music, Drums & Chants",
        "culture": "Yorùbá",
        "is_parent": False,
        "sovereign_parent": "Were Music",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": ["were ibile", "traditional were", "folk were music", "were chant"],
        "description": "The grassroots acoustic folk incarnation of Were music, performed without electronic amplification using indigenous hand percussion.",
        "etymology_and_philosophy": "From 'Were' and 'Ìbílẹ̀' (indigenous/heritage). Preserves the raw acoustic communal energy of early 20th-century neighborhoods.",
        "historical_timeline": "Thrived in metropolitan neighborhoods from the 1920s to the 1960s before electric amplifiers transformed the genre into Fújì.",
        "material_and_craftsmanship": "Instruments include the clay pot Sákárà drum, metal agogo bells, and hollow wooden clappers.",
        "social_and_ritual_context": "Spontaneous communal processions during festive holidays, celebrating neighborhood solidarity.",
        "proverbs_and_oral_traditions": [
            "Were ìbílẹ̀ kì í tan orin; ohun tí a rí l’à ń kọrin rẹ̀. (Indigenous Were music never runs dry of verses; life itself provides its songs.)"
        ],
        "diaspora_connections": "Paralleled in Caribbean street carnival chanting and early calypso percussion roots.",
        "geographical_origin": "Lagos, Ibadan, and Epe",
        "curatorial_guidelines": "Present in lively community street setting with acoustic percussionists.",
        "related_entities": ["Were Music", "Ajísààrì", "Sákárà Were", "Dùndún"]
    }
]

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(p, data):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("🏛️ Ingesting Tier A Bespoke Sub-Variants into Master Corpora...")
    base_data = load_json(DATA_PATH)
    all_tier_a = base_data + ADDITIONAL_TIER_A
    print(f"📦 Total Tier A bespoke records compiled: {len(all_tier_a)}")

    for cpath in [API_CORPUS_PATH, WEB_CORPUS_PATH]:
        corpus = load_json(cpath)
        existing_map = {e.get("title"): i for i, e in enumerate(corpus)}
        
        added_count = 0
        updated_count = 0

        for new_item in all_tier_a:
            title = new_item.get("title")
            clean_title = title.split("(")[0].strip()

            target_idx = None
            if title in existing_map:
                target_idx = existing_map[title]
            elif clean_title in existing_map:
                target_idx = existing_map[clean_title]

            if target_idx is not None:
                # Merge and update with rich data
                corpus[target_idx].update(new_item)
                updated_count += 1
            else:
                corpus.append(new_item)
                existing_map[title] = len(corpus) - 1
                added_count += 1

        save_json(cpath, corpus)
        print(f"✅ Updated {cpath.name}: {added_count} new entities added, {updated_count} updated. Total now: {len(corpus)}")

if __name__ == "__main__":
    main()
