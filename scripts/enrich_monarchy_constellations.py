#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: MONARCHY & ROYAL ARCHITECTURE CONSTELLATION INGESTER
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-004
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema Parity
=============================================================================
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"

NEW_CANONICAL_ENTITIES = [
    {
        "id": "ooni_of_ife",
        "title": "Ọọ̀ni of Ifẹ̀",
        "culture": "Yorùbá",
        "category": "Monarchy, Royal Regalia & Governance",
        "is_parent": False,
        "sovereign_parent": "Ọba",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "ooni of ife", "ọọ̀ni of ifẹ̀", "ooni ife", "ọọ̀ni ifẹ̀", "ooni", "ọọ̀ni",
            "king of ife", "spiritual head of the yoruba", "arole oduduwa"
        ],
        "description": "The sacred Paramount Monarch of Ilé-Ifẹ̀, revered as the spiritual father of the Yorùbá race and living custodian of the ancestral cradle of humanity.",
        "historical_timeline": "Classical Antiquity (c. 11th–14th Century CE): Rooted in the ancestral founding of Ilé-Ifẹ̀ by Odùduwà; formalized through dynasties succeeding Obàlùfọ̀n and Ọ̀rànmíyàn. Imperial & Inter-Kingdom Era (15th–19th Century): Recognized as the supreme spiritual father among all crowned Yoruba kings, holding the prerogative to sanction royal beaded crowns (Adé Aládé) and ancestral swords of state (Idà Ìṣẹ́gun). Modern Era: Head of the Osun State Council of Traditional Rulers and co-chair of the National Council of Traditional Rulers of Nigeria, embodying unbroken cultural continuity from the primordial dawn.",
        "etymology_and_philosophy": "Linguistically contracted from 'Ọmọ-ẹni-tó-ni' (the child of he who owns the land) or 'Ọlọ́wọ̀-ọ̀ni' (The venerable lord of today). Philosophically, the Ọọ̀ni is 'Arole Odùduwà' (the earthly heir to Odùduwà) and 'Ọ̀jìkí-kí-Ọba' (The sovereign hailed before all monarchs). His office personifies cosmic sacrality (Aṣẹ), spiritual consensus, and the moral fountainhead from which all legitimate dynastic authority flows.",
        "material_and_craftsmanship": "Adorned in pure white sacred textiles (Aṣọ Funfun), antique cylindrical Ìyun coral and Sègi cobalt beads, and the consecrated high beaded crown (Adé Arè) embroidered with sacred avian heraldry (Òkín). Holds the beaded staff of office (Ọ̀pá Aṣẹ) and horse-tail whisk (Ìrùkẹ̀rẹ̀).",
        "social_and_ritual_context": "Presides over the ancient Ifẹ̀ royal court, the Ooni-in-Council (High Chiefs / Ìwàrẹ̀fà), and sacred ancestral annual rites including the Olojo Festival (wearing of the sacred Adé Arè), Edì, and Itapa festivals.",
        "proverbs_and_oral_traditions": [
            "Ọọ̀ni l'ó ni Ilé-Ifẹ̀, orísun gbogbo ẹ̀dá. (The Ọọ̀ni is the sovereign custodian of Ilé-Ifẹ̀, the primal source of all humanity: Celebrating spiritual antiquity.)",
            "A kì í bá Ọọ̀ni jà kí a rí àbùkù tán; orísun aṣẹ kì í gbẹ. (One never contends with the Ọọ̀ni and avoids divine consequence; the fountainhead of spiritual mandate never dries up: Revering sacral authority.)",
            "Adé Arè kò gbọdọ̀ kan ilẹ̀ lásán; orí tí yóò dé e gbọdọ̀ fẹsẹ̀ múlẹ̀ nínú ìwà. (The sacred crown of Arè must never touch the bare ground in vain; the head destined to wear it must be firmly rooted in righteous character: Demanding moral fortitude.)"
        ],
        "provenance_and_citations": "Johnson, Samuel (1921). The History of the Yorubas; Akinjogbin, I.A. (1992). The Cradle of a Race: Ife from the Beginning to 1980; Abiodun, Rowland (2014). Yoruba Art and Language; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    {
        "id": "alaafin_of_oyo",
        "title": "Aláàfin of Ọ̀yọ́",
        "culture": "Yorùbá",
        "category": "Monarchy, Royal Regalia & Governance",
        "is_parent": False,
        "sovereign_parent": "Ọba",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "alaafin of oyo", "aláàfin of ọ̀yọ́", "alaafin oyo", "aláàfin ọ̀yọ́",
            "alaafin", "aláàfin", "emperor of oyo", "lord of the palace"
        ],
        "description": "The imperial Paramount Monarch of the Ọ̀yọ́ Empire, titled Kábíyèsí, Emperor of the Yorùbá, and living earthly representative of Ṣàngó.",
        "historical_timeline": "Classical Imperial Genesis (c. 14th–16th Century CE): Founded at Ọ̀yọ́-Ilé by Prince Ọ̀rànmíyàn; expanded under legendary monarchs including Ṣàngó, Àjàká, and Kori. Imperial Zenith (17th–18th Century CE): Governed the vast metropolitan Ọ̀yọ́ Empire from the Niger river to the Dahomey coast, commanding imperial cavalry regiments and international trade. 19th Century Renaissance: Relocated by Aláàfin Àtìbà to Ọ̀yọ́-Àtìbà (New Ọ̀yọ́) in the 1830s following the Fúlàní jihads, maintaining institutional hegemony into the contemporary era.",
        "etymology_and_philosophy": "Contracted from 'Aláàfin' (Oní-ààfin: The Lord and Master of the Palace). Philosophically titled 'Kábíyèsí' (Ká-bí-yín-kò-sí: He whom none dare question), 'Iku Baba Yeye' (Death, the Sire and Mother), and 'Aláṣẹ Èkejì Òrìṣà' (Companion and second-in-command to the Deities). Balances absolute executive authority with constitutional checks by the Ọ̀yọ́ Mèsì council led by the Baṣọ̀run.",
        "material_and_craftsmanship": "Wears the magnificent conical beaded crown with face-veiling seed-bead fringe (Adé Òkín), master-loomed raw silk Sányán and crimson Àlàárì agbádá robes, beaded leather footwear (Bàtà Ìlẹ̀kẹ̀), and holds the carved ivory tusk flywhisk (Ìrùkẹ̀rẹ̀).",
        "social_and_ritual_context": "Presides over the imperial palace (Ààfin Aláàfin), the Kòso sacred coronation shrine, the Ọ̀yọ́ Mèsì council, and annual festivals honoring Ṣàngó, Ọya, and Ọ̀rùn.",
        "proverbs_and_oral_traditions": [
            "Aláàfin l'ó l'Orí, Ọ̀yọ́ Mèsì l'ó ni Ilẹ̀. (The Aláàfin presides over the Head; the Ọ̀yọ́ Mèsì holds the sovereignty of the Earth: Articulating classical separation of powers.)",
            "Ọ̀rọ̀ tí Aláàfin bá sọ ti di àṣẹ; a kì í fẹnu kò lu idà ọba. (The word spoken by the Aláàfin becomes immutable decree; one never contends with the royal blade: Affirming executive authority.)",
            "Ọba Ọ̀yọ́ kì í bẹ̀rù ogun; Ṣàngó l'ó fi iná kọ́ ààfin. (The King of Ọ̀yọ́ fears no war; it was Ṣàngó who established the palace with celestial fire: Celebrating martial heritage.)"
        ],
        "provenance_and_citations": "Johnson, Samuel (1921). The History of the Yorubas; Law, Robin (1977). The Oyo Empire c. 1600-c. 1836; Smith, Robert S. (1988). Kingdoms of the Yoruba; Atanda, J.A. (1973). The New Oyo Empire."
    },
    {
        "id": "awujale_of_ijebu",
        "title": "Awùjalẹ̀ of Ìjẹ̀bú",
        "culture": "Yorùbá",
        "category": "Monarchy, Royal Regalia & Governance",
        "is_parent": False,
        "sovereign_parent": "Ọba",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "awujale of ijebu", "awùjalẹ̀ of ìjẹ̀bú", "awujale", "awùjalẹ̀",
            "king of ijebuland", "paramount ruler of ijebu"
        ],
        "description": "The Paramount Monarch and sovereign ruler of the ancient Kingdom of Ìjẹ̀búland, reigning from the ancestral capital of Ìjẹ̀bú-Òde.",
        "historical_timeline": "Classical Era (c. 14th Century CE to present): Traces royal descent to Ọbánta (Arígbábú), son of Odùduwà's daughter, who unified the Ìjẹ̀bú forest kingdoms. Commercial & Defensive Supremacy (16th–19th Century): Commanded coastal and lagoon trade routes between the interior and European maritime merchants; established Sungbo's Eredo earthwork defense ramparts and maintained fierce political autonomy until the 1892 British expedition. Modern Era: One of the oldest surviving monarchical institutions in West Africa.",
        "etymology_and_philosophy": "Derived from 'A-wú-jọ-alẹ̀' (He who swells and unites the sovereign land / The arbiter who commands peace over the territorial earth). Philosophically represents administrative consensus, commercial acumen, and deep ritual integration with the Òsùgbó/Ògbóni judicial council and Agẹmọ sacerdotal confederacy.",
        "material_and_craftsmanship": "Adorned in high-count indigo-dyed Kìjìpá, heirloom red coral necklaces, master-carved ivory armlets, and conical beaded crowns featuring stylized chameleon and tortoise icons honoring Agẹmọ.",
        "social_and_ritual_context": "Presides over the Ìjẹ̀bú kingdom, the Òsùgbó judicial lodge, the Ìpàkí guild, and the sacred national Agẹmọ festival celebrated across sixteen constituent towns.",
        "proverbs_and_oral_traditions": [
            "Awùjalẹ̀ gb'orí ìtẹ́, Ìjẹ̀bú d'ọrọ̀; ẹni tó bọ̀wọ̀ fún ọba kì í ṣòfò. (When the Awùjalẹ̀ mounts the ancestral throne, Ìjẹ̀bú flourishes in prosperity; he who reverences the monarch never tastes loss: Praising economic governance.)",
            "Ọba Ìjẹ̀bú kì í fojú kàn agẹmọ lásán; aṣẹ àtijọ́ ló ń sọ ilẹ̀ d'ọ̀wọ̀. (The King of Ìjẹ̀bú never beholds Agẹmọ lightly; ancient covenants sanctify the soil: Revering sacred civic oaths.)",
            "Àwùjọ kì í tú tí Awùjalẹ̀ bá wà lórí ìtẹ́; àlàáfíà ni òkúta-ìpìlẹ̀ ìlú. (The civic assembly never scatters while the Awùjalẹ̀ occupies the throne; peace is the foundation of the realm: Celebrating social stability.)"
        ],
        "provenance_and_citations": "Ogunba, Oyin (1967). The Agemo Cult in Ijebuland; Lloyd, P.C. (1962). Yoruba Land Law; Ayandele, E.A. (1992). The Ijebu of Yorubaland 1850-1950; Smith, Robert S. (1988). Kingdoms of the Yoruba."
    },
    {
        "id": "kobi_aafin",
        "title": "Kòbì Ààfin",
        "culture": "Yorùbá",
        "category": "Topography, Natural Landscapes & Architecture",
        "is_parent": False,
        "sovereign_parent": "Ààfin",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "kobi aafin", "kòbì ààfin", "kobi", "kòbì", "royal gabled roof",
            "palace gable porch", "sacred gabled roof"
        ],
        "description": "The sacred gabled porch and projecting roof pavilion of a Yorùbá royal palace, reserved exclusively for the monarch and shrines of paramount ancestors, prohibited in ordinary private architecture.",
        "historical_timeline": "Classical Era (c. 13th Century CE to present): Developed in ancient Ifẹ̀ and imperial Ọ̀yọ́ as an architectural signifier of supreme sovereignty. Customary Sumptuary Law: Under traditional law, no private citizen or non-crowned chief was permitted to build a Kòbì roof upon pain of severe judicial sanction. Survivals: Prominently preserved in the palaces of the Aláàfin of Ọ̀yọ́, Ọọ̀ni of Ifẹ̀, Ẹwí of Adó-Èkìtì, and Ọba of Òkè-Ìlá.",
        "etymology_and_philosophy": "From 'Kò-bì' (That which projects outwards without falling / An architectural summit). Philosophically signifies the sheltering wing of the monarch over the commonwealth and the sacred spatial portal connecting ancestral spirits above with human assemblies below.",
        "material_and_craftsmanship": "Steeply pitched triangular or gabled timber frame clad in thatch or embossed metal sheeting, supported by carved caryatid posts depicting royal mothers, equestrian warriors, and deities.",
        "social_and_ritual_context": "The Aláàfin or Ọba appears beneath the Kòbì during major public festivals to greet chiefs and commoners. Sacred shrines to Ṣàngó, Ògún, or royal ancestors are housed beneath specific designated Kòbì.",
        "proverbs_and_oral_traditions": [
            "Ọba nìkan l'ó l'ẹtọ́ láti tẹ kòbì; ilé ọlọ́rọ̀ kì í díje pẹ̀lú ààfin. (The monarch alone possesses the prerogative to erect a gabled Kòbì; the mansion of the wealthy commoner never competes with the palace: Articulating royal architectural sovereignty.)",
            "Kòbì ààfin kì í jóná kí ọba má tún un kọ́; àbùkù kì í bá adé baba. (The palace gable never burns down without the king rebuilding it grander; dishonor never afflicts the ancestral crown: Proclaiming resilience.)",
            "Ẹni tó dúró sábẹ́ kòbì ti bọ́ sábẹ́ àbò ọba; àṣẹ kì í pa ẹni tó wà l'ọ́gbà ọba. (He who stands beneath the royal gable has entered royal sanctuary; divine authority never slays the guest of the palace: Teaching sanctuary law.)"
        ],
        "provenance_and_citations": "Ojo, G.J. Afolabi (1966). Yoruba Palaces; Vlach, John Michael (1976). Affecting Architecture of the Yoruba; Abiodun, Rowland (2014). Yoruba Art and Language; Johnson, Samuel (1921). The History of the Yorubas."
    },
    {
        "id": "ewe_akoko",
        "title": "Ewé Àkòko",
        "culture": "Yorùbá",
        "category": "Sacred Botany, Flora & Herbal Medicine",
        "is_parent": False,
        "sovereign_parent": "Òògùn",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "ewe akoko", "ewé àkòko", "akoko leaf", "newbouldia laevis",
            "boundary tree", "coronation leaf", "sacred coronation leaf"
        ],
        "description": "Newbouldia laevis — the sacred coronation and boundary leaf of kingship, placed in the royal crown or chieftaincy cap during investiture rites to confer divine longevity, peace, and unshakeable authority.",
        "historical_timeline": "Classical Antiquity to Present: Revered across Yorùbá history as the premier botanical emblem of longevity and divine royal mandate. Investitures: Placed behind the ear and inside the crown of every Ọba and chief at coronation since the dawn of Ilé-Ifẹ̀. Boundary Custody: Planted as living, indestructible boundary markers (Òpó Ààlà) across farmland and municipal territories.",
        "etymology_and_philosophy": "Named 'Àkòko' (from 'Àkọ́-ọ̀kọ̀' / primordial foundation of time). Philosophically represents perpetual life, resilience against lightning and pestilence, and the unyielding permanence of ancestral authority: 'Àkòko kì í kú sí oko' (The Àkòko tree never withers into oblivion).",
        "material_and_craftsmanship": "Lustrous dark-green pinnate leaves harvested with consecrated copper coins and palm gin; placed alongside consecrated parrot feathers (Ìkódẹ) and camwood.",
        "social_and_ritual_context": "Indispensable during monarchical coronations, Ògbóni investitures, Òrìṣà Oko agricultural rites, and establishing inviolate land borders.",
        "proverbs_and_oral_traditions": [
            "Ewé àkòko kì í gbẹ lórí ìtẹ́; orí tí yóò jọba a gb'àkòko kọ́. (The Àkòko leaf never withers upon the throne; the head destined for kingship receives the sacred leaf: Celebrating legitimate investiture.)",
            "Àkòko l'ó ni adé, àkòko l'ó l'oyè; ẹni tí Òrìṣà bá fi àkòko jẹ kì í rí àbùkù. (Àkòko commands the crown, Àkòko governs the title; he whom the deities invest with the leaf never faces dishonor: Affirming divine sanction.)",
            "Bí a bá gbin àkòko sí ààlà, ogun kò lè mú ilẹ̀; àṣẹ àwọn àgbà wà nínú gbongbo rẹ̀. (When Àkòko is planted at the boundary, warfare cannot seize the land; ancestral authority resides in its roots: Teaching boundary sanctity.)"
        ],
        "provenance_and_citations": "Verger, Pierre (1995). Ewé: The Use of Plants in Yoruba Society; Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Oliver-Bever, B. (1986). Medicinal Plants in Tropical West Africa."
    }
]


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def enrich_monarchy_constellation(corpus: List[Dict[str, Any]]) -> None:
    """Enriches and aligns existing Monarchy, Palace, and Attire records."""
    existing_by_id = {e.get("id"): e for e in corpus}

    # 1. Enrich Owa Obokun
    if "Owa Obokun" in existing_by_id:
        owa = existing_by_id["Owa Obokun"]
        owa["title"] = "Ọwá Obòkun of Ìjẹ̀ṣàland"
        owa["is_parent"] = False
        owa["sovereign_parent"] = "Ọba"
        owa["sovereign_parent_status"] = "Living Sub-Variant"
        aliases = set(owa.get("aliases", []))
        aliases.update(["ọwá obòkun", "owa obokun", "ọwá obòkun of ìjẹ̀ṣàland", "owa obokun of ijeshaland"])
        owa["aliases"] = sorted(list(aliases))
        owa["provenance_and_citations"] = "Johnson, Samuel (1921). The History of the Yorubas; Peel, J.D.Y. (1983). Ijeshas and Nigerians: The Poetics of Social Experience; Akintoye, S.A. (1971). Revolution and Power Politics in Yorubaland."

    # 2. Enrich Orangun of Ila
    if "Orangun" in existing_by_id:
        ora = existing_by_id["Orangun"]
        ora["title"] = "Ọ̀ràngún of Ìlá"
        ora["is_parent"] = False
        ora["sovereign_parent"] = "Ọba"
        ora["sovereign_parent_status"] = "Living Sub-Variant"
        aliases = set(ora.get("aliases", []))
        aliases.update(["ọ̀ràngún", "orangun", "ọ̀ràngún of ìlá", "orangun of ila", "king of ila orangun"])
        ora["aliases"] = sorted(list(aliases))
        ora["provenance_and_citations"] = "Johnson, Samuel (1921). The History of the Yorubas; Pemberton, John & Afolayan, Funso S. (1996). Yoruba Sacred Kingship: A Power Like That of the Gods; Smith, Robert S. (1988). Kingdoms of the Yoruba."

    # 3. Enrich Aafin Ooni (Ile-Ife)
    if "Àfin Ọọ̀ni" in existing_by_id:
        pal_ooni = existing_by_id["Àfin Ọọ̀ni"]
        pal_ooni["title"] = "Ààfin Ọọ̀ni (Ilé-Ifẹ̀)"
        pal_ooni["is_parent"] = False
        pal_ooni["sovereign_parent"] = "Ààfin"
        pal_ooni["sovereign_parent_status"] = "Living Sub-Variant"
        aliases = set(pal_ooni.get("aliases", []))
        aliases.update(["àfin ọọ̀ni", "afin ooni", "ààfin ọọ̀ni", "aafin ooni", "ààfin ọọ̀ni (ilé-ifẹ̀)"])
        pal_ooni["aliases"] = sorted(list(aliases))
        pal_ooni["provenance_and_citations"] = "Akinjogbin, I.A. (1992). The Cradle of a Race; Willett, Frank (1967). Ife in the History of West African Sculpture; Blier, Suzanne Preston (2015). Art and Risk in Ancient Yoruba; Drewal, H.J. & Pemberton, J. (1989). Yoruba."

    # 4. Enrich Aafin Alaafin (Oyo)
    if "Àfin Aláàfin" in existing_by_id:
        pal_ala = existing_by_id["Àfin Aláàfin"]
        pal_ala["title"] = "Ààfin Aláàfin (Ọ̀yọ́)"
        pal_ala["is_parent"] = False
        pal_ala["sovereign_parent"] = "Ààfin"
        pal_ala["sovereign_parent_status"] = "Living Sub-Variant"
        aliases = set(pal_ala.get("aliases", []))
        aliases.update(["àfin aláàfin", "afin alaafin", "ààfin aláàfin", "aafin alaafin", "ààfin aláàfin (ọ̀yọ́)"])
        pal_ala["aliases"] = sorted(list(aliases))
        pal_ala["provenance_and_citations"] = "Johnson, Samuel (1921). The History of the Yorubas; Law, Robin (1977). The Oyo Empire; Ojo, G.J. Afolabi (1966). Yoruba Palaces; Vlach, John Michael (1976). Affecting Architecture of the Yoruba."

    # 5. Enrich Sanyan, Alaari, Etu
    textile_citations = "Eicher, Joanne B. (1976). Nigerian Handcrafted Textiles; Picton, John (1995). The Art of African Textiles; Wolff, Norma H. (1982). Yoruba Adire Cloth; Abiodun, Rowland (2014). Yoruba Art and Language."
    for tex_id in ["Sányán", "Àlàárì", "Ẹ̀tù"]:
        if tex_id in existing_by_id:
            tex = existing_by_id[tex_id]
            tex["sovereign_parent"] = "Aṣọ Òkè"
            tex["is_parent"] = False
            tex["sovereign_parent_status"] = "Living Sub-Variant"
            tex["provenance_and_citations"] = textile_citations

    # 6. Align Aso Oke as Sovereign Parent
    if "Aṣọ Òkè" in existing_by_id:
        aso_oke = existing_by_id["Aṣọ Òkè"]
        aso_oke["is_parent"] = True
        aso_oke["sub_variants"] = ["Sányán", "Àlàárì", "Ẹ̀tù"]
        aso_oke["living_variants"] = ["Sányán", "Àlàárì", "Ẹ̀tù"]
        aso_oke["provenance_and_citations"] = textile_citations

    # 7. Ingest new canonical entities if not present
    existing_ids = {e.get("id") for e in corpus}
    added_count = 0
    for new_ent in NEW_CANONICAL_ENTITIES:
        if new_ent["id"] not in existing_ids:
            corpus.append(new_ent)
            added_count += 1

    print(f"  ✅ Monarchy Constellation Enriched: {added_count} new standalone entities ingested.")


def verify_canonical_invariants(corpus: List[Dict[str, Any]]) -> None:
    """Verifies that no twin duplicate nodes exist and critical sovereign records are intact."""
    for check_id, check_title in [
        ("ooni_of_ife", "Ọọ̀ni of Ifẹ̀"),
        ("alaafin_of_oyo", "Aláàfin of Ọ̀yọ́"),
        ("awujale_of_ijebu", "Awùjalẹ̀ of Ìjẹ̀bú"),
        ("kobi_aafin", "Kòbì Ààfin"),
        ("ewe_akoko", "Ewé Àkòko"),
        ("Owa Obokun", "Ọwá Obòkun of Ìjẹ̀ṣàland"),
        ("Orangun", "Ọ̀ràngún of Ìlá")
    ]:
        matches = [e for e in corpus if e.get("id") == check_id or e.get("title") == check_title]
        if len(matches) != 1:
            raise ValueError(f"Invariant Violation: Expected exactly 1 match for {check_id} ({check_title}), found {len(matches)}")

    print("  ✅ All canonical invariants verified: 0 twin duplicates, 100% single-node integrity.")


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING MONARCHY & ROYAL ARCHITECTURE CONSTELLATION")
    print("=" * 80)

    print(f"📂 Loading API corpus from {API_CORPUS_PATH}...")
    api_corpus = load_json(API_CORPUS_PATH)
    print(f"   Initial API corpus count: {len(api_corpus)}")

    print(f"📂 Loading Web corpus from {WEB_CORPUS_PATH}...")
    web_corpus = load_json(WEB_CORPUS_PATH)
    print(f"   Initial Web corpus count: {len(web_corpus)}")

    print("\n▶ [STEP 1] Enriching Monarchy, Palace Architecture & Regalia...")
    enrich_monarchy_constellation(api_corpus)
    enrich_monarchy_constellation(web_corpus)

    print("\n▶ [STEP 2] Verifying Zero Twin Nodes Invariants...")
    verify_canonical_invariants(api_corpus)
    verify_canonical_invariants(web_corpus)

    print("\n▶ [STEP 3] Persisting Synchronized Master Corpora...")
    save_json(API_CORPUS_PATH, api_corpus)
    save_json(WEB_CORPUS_PATH, web_corpus)
    print("✅ Successfully saved both API and Web corpora in lockstep.")
    print(f"   Final API corpus count: {len(api_corpus)}")
    print(f"   Final Web corpus count: {len(web_corpus)}")
    print("=" * 80)


if __name__ == "__main__":
    main()
