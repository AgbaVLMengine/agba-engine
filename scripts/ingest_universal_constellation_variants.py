#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: UNIVERSAL CONSTELLATION SUB-VARIANT INGESTER
=============================================================================
Ingests 4 canonical living sub-variant entities to fulfill HANDOFF-SUURU-005:
  1. Basọ̀run Olúyọ̀lé (Child of Baṣọ̀run)
  2. Igbá Ìwà (Child of Baṣọ̀run / Ọ̀yọ́ Mèsì)
  3. Adé Ọ̀kín (Child of Adé)
  4. Ìyáàlù Dùndún (Child of Dùndún)

Strict Gate 2 (<500 LOC), Gate 4 (Awo exclusion & authentic diacritics),
and Dual-Corpus synchronization.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS_PATH = REPO_ROOT / "api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"

NEW_ENTITIES = [
    {
        "id": "basorun_oluyole",
        "title": "Basọ̀run Olúyọ̀lé",
        "culture": "Yorùbá",
        "category": "Monarchy, Royal Regalia & Governance",
        "is_parent": False,
        "sovereign_parent": "Baṣọ̀run",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "basorun oluyole",
            "basorun olúyọ̀lé",
            "oluyole",
            "olúyọ̀lé",
            "iba oluyole",
            "oluyole of ibadan",
            "baṣọrun oluyole",
            "basorun oluyole of ibadan"
        ],
        "description": "The formidable 19th-century Baṣọ̀run, warrior-statesman, and paramount ruler of Ìbàdànland (Iba Olúyọ̀lé). Grandson of the historic Baṣọ̀run Gáà through his mother Agbọ́nrin, Olúyọ̀lé was invested with the supreme military and civic title of Baṣọ̀run by Aláàfin Àtìbà of Ọ̀yọ́, transforming Ibadan from a wartime military confederacy into an invincible imperial powerhouse across Yorùbáland.",
        "historical_timeline": "19th Century (c. 1830s–1850 CE): Following the collapse of Ọ̀yọ́-Ilé, Olúyọ̀lé established absolute paramount authority over Ibadan, orchestrating the victory at the Battle of Òṣogbo (1840) which decisively halted Fulani cavalry expansion into the southern rainforests. Invested by Aláàfin Àtìbà as Baṣọ̀run of the resurrected Ọ̀yọ́ Empire, establishing the dual-command hegemony between Ọ̀yọ́ and Ibadan. Modern Continuity: Immortalized as the foundational civic ancestor of Ibadan ('Ọmọ Ìbàdàn kò mọ̀kọ̀, Olúyọ̀lé lo mọ'), his ancestral palace at Oja'ba remains a sacred historical monument.",
        "etymology_and_philosophy": "From 'Olú' (lord/supreme head) and 'Yọ̀lé' (rejoices in the lineage). Philosophically embodies republican martial meritocracy, decisive strategic intelligence, and the preservation of Yorùbá civilization during geopolitical crisis.",
        "material_and_craftsmanship": "Distinguished by heavy martial regalia, master-forged iron cavalry stirrups, broadswords (Idà), ceremonial dane guns (Ìbọn Ọdẹ), and the sovereign Baṣọ̀run embroidered velvet robes and Akòkò chieftaincy wreaths.",
        "social_and_ritual_context": "Presided over the Ibadan military state council, arbitrated lineage disputes, and conducted state libations to Ògún and the ancestral spirits of Ibadan heroes.",
        "proverbs_and_oral_traditions": [
            "Ìbàdàn kì í gbé oníwà-kíwà, ilé Olúyọ̀lé ni gbogbo wa ń gbé. (Ibadan never tolerates the dishonorable; it is in the house of Olúyọ̀lé that we all dwell. This underscores that civic integrity and collective valor are the indispensable foundations of citizenship.)",
            "Olúyọ̀lé kì í dárò ogun kí ó má bọ́ sí i. (Olúyọ̀lé never reflects upon war without entering it triumphantly. This celebrates resolute action, unwavering courage, and martial mastery in defending ancestral sovereignty.)"
        ],
        "diaspora_connections": "His martial legacy and defense of Yoruba autonomy are celebrated in Afro-Cuban and Brazilian historical memory through songs commemorating the 19th-century warrior-kings.",
        "geographical_origin": "Ìbàdàn, Ọ̀yọ́-Ilé.",
        "curatorial_guidelines": "Display 19th-century forged cavalry implements, traditional warrior tunics, and historical portraiture of the Ibadan martial aristocracy.",
        "related_entities": [
            "Baṣọ̀run (Prime Minister / Supreme Commander of Oyo)",
            "Basọ̀run Gáà",
            "Ọ̀yọ́ Mèsì",
            "Aláàfin Àtìbà",
            "Ìbàdàn",
            "Kúrunmí",
            "Balogun Ibikunle"
        ],
        "sub_variants": []
    },
    {
        "id": "igba_iwa",
        "title": "Igbá Ìwà (The Sacred Calabash of Destiny & Abdication)",
        "culture": "Yorùbá",
        "category": "Monarchy, Royal Regalia & Governance",
        "is_parent": False,
        "sovereign_parent": "Baṣọ̀run",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "igba iwa",
            "igba-iwa",
            "igbá ìwà",
            "calabash of destiny",
            "calabash of existence",
            "calabash of abdication",
            "igba awo",
            "sacred calabash of oyo"
        ],
        "description": "The sacred constitutional calabash within the Ọ̀yọ́ Empire's system of institutional checks and balances. When an Aláàfin ruled tyrannically, breached sacred constitutional covenants, or alienated the ancestral forces, the Ọ̀yọ́ Mèsì, convened under the supreme leadership of the Baṣọ̀run, presented the monarch with Igbá Ìwà containing parrot eggs or empty, solemnly declaring: 'Àwọn Òrìṣà kọ̀ ọ́, Ilẹ̀ kọ̀ ọ́, Àwa náà kọ̀ ọ́' (The gods reject you, the earth rejects you, we also reject you), mandating honourable abdication and ritual suicide.",
        "historical_timeline": "Classical Antiquity (c. 14th–18th Century CE): Codified as the supreme constitutional mechanism preventing tyrannical despotism in the Ọ̀yọ́ Empire. Recorded extensively by Reverend Samuel Johnson (1921) in 'The History of the Yorubas'. Post-Colonial Continuity: Stands globally as one of the world's earliest constitutional instruments of democratic accountability and monarchical limitation.",
        "etymology_and_philosophy": "From 'Igbá' (gourd/calabash) and 'Ìwà' (character, destiny, existence). Philosophically signifies that royal power (*Àṣẹ*) is contingent upon moral righteousness (*Ìwà Rere*), and that cosmic harmony supercedes imperial autocracy.",
        "material_and_craftsmanship": "A pair of pristine hemispheres carved from the sacred calabash (Lagenaria siceraria), polished with camwood and chalk, inlaid with geometric ancestral incisions, and lined with white homespun cloth.",
        "social_and_ritual_context": "Solemnly dispatched by royal emissaries of the Ọ̀yọ́ Mèsì to the Aláàfin's inner chambers under strict esoteric protocols.",
        "proverbs_and_oral_traditions": [
            "Àwọn Òrìṣà kọ̀ ọ́, Ilẹ̀ kọ̀ ọ́, Àwa náà kọ̀ ọ́; Igbá Ìwà ti dé. (The gods reject you, the earth rejects you, we also reject you; the Calabash of Destiny has arrived. This ancient constitutional pronouncement affirms that sovereign legitimacy is revocable when moral virtue is abandoned.)",
            "Ọba tó fọ́ Igbá Ìwà, kò lè jẹ oyè bọ̀ sáyé mọ́. (The monarch who has broken the Calabash of Destiny can never return to the throne; moral degradation is permanent in the eyes of the ancestors.)"
        ],
        "diaspora_connections": "Preserved metaphorically in Afro-Cuban Lucumí and Brazilian Candomblé cosmology as 'Igbá Odù' / 'Igbá Ìwà', the cosmic vessel containing the secrets of life, balance, and divine judgment.",
        "geographical_origin": "Ọ̀yọ́-Ilé, Ilé-Ifẹ̀.",
        "curatorial_guidelines": "Present alongside classical carved calabash vessels, Ọ̀yọ́ royal insignia, and constitutional history archives.",
        "related_entities": [
            "Baṣọ̀run (Prime Minister / Supreme Commander of Oyo)",
            "Ọ̀yọ́ Mèsì",
            "Ọba",
            "Aláàfin Àtìbà",
            "Ìwà Lẹ̀ṣọ́",
            "Ògbóni"
        ],
        "sub_variants": []
    },
    {
        "id": "ade_okin",
        "title": "Adé Ọ̀kín (The Beaded Crown of the Sacred Peacock)",
        "culture": "Yorùbá",
        "category": "Monarchy, Royal Regalia & Governance",
        "is_parent": False,
        "sovereign_parent": "Adé",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "ade okin",
            "adé ọ̀kín",
            "ade-okin",
            "crown of okin",
            "peacock beaded crown",
            "royal okin crown",
            "ade alade okin"
        ],
        "description": "The paramount royal beaded crown embellished with the sacred plumage and sculptural effigy of the Ọ̀kín (the mythical royal peacock / king of birds). Symbolizing cosmic majesty, impeccable aesthetic grace, and ancestral distinction, Adé Ọ̀kín is donned by paramount Yorùbá monarchs during transcendental state ceremonies and sovereign festivals.",
        "historical_timeline": "Classical Ilé-Ifẹ̀ Antiquity (c. 11th–14th Century CE): Created by master bead-embroiderers (Onísọ̀nà) for paramount lineage rulers. Celebrated in royal court poetry across Ọ̀yọ́, Ìjẹ̀bú, Òwò, and Ẹ̀gbá. Modern Era: Remains an iconic symbol of Yorùbá artistic excellence in global museum collections (Metropolitan Museum, British Museum).",
        "etymology_and_philosophy": "From 'Adé' (crown) and 'Ọ̀kín' (the sacred peacock, celebrated as 'Ọba Ẹyẹ', the monarch of birds). Philosophically conveys that true kingship possesses natural, unblemished splendor and radiant moral light.",
        "material_and_craftsmanship": "Conical basketry foundation woven from stiff palm ribs, covered with starched fabric and embroidered with tens of thousands of miniature polychrome glass seed beads; crowned by sculpted beaded birds (Ẹyẹ) symbolizing female spiritual power (Ìyámi) and ancestral vigilance.",
        "social_and_ritual_context": "Consecrated with sacred herbal infusions (*Òògùn*) inside the crown's apex. The veil of beads (*Oju-Adé*) conceals the monarch's human gaze, transmuting the king into the living embodiment of divine authority.",
        "proverbs_and_oral_traditions": [
            "Ọ̀kín l’ọba ẹyẹ, Adé Ọ̀kín l’olórí adé. (The peacock is the monarch of birds, and the Crown of Ọ̀kín is the sovereign of all crowns. This reflects how unsurpassed beauty and royal grace converge in paramount regalia.)",
            "Bí ọba bá dádé Ọ̀kín, gbogbo ayé a dákẹ́ rọ́rọ́. (When the sovereign dons the Crown of Ọ̀kín, the entire universe falls into reverent silence, acknowledging the sublime manifestation of ancestral splendor.)"
        ],
        "diaspora_connections": "Beaded crown traditions for consecrated divinities (Ọbalúayé, Ọbàtálá, Ọ̀ṣun) flourish in Afro-Cuban Lucumí beadwork and Brazilian Candomblé 'coroas de orixá'.",
        "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́, Òwò.",
        "curatorial_guidelines": "Showcase with archival glass beadwork, ancestral royal textiles, and photographic documentation of beaded veil crowns.",
        "related_entities": [
            "Adé",
            "Adé Ààrẹ",
            "Ọba",
            "Ẹyẹ",
            "Ìyámi (Our Mothers / Primordial Female Energy)"
        ],
        "sub_variants": []
    },
    {
        "id": "iyaalu_dundun",
        "title": "Ìyáàlù (Lead Mother Drum of the Dùndún Ensemble)",
        "culture": "Yorùbá",
        "category": "Auditory Arts, Music, Drums & Chants",
        "is_parent": False,
        "sovereign_parent": "Dùndún",
        "sovereign_parent_status": "Living Sub-Variant",
        "aliases": [
            "iyaalu",
            "ìyáàlù",
            "iyaalu dundun",
            "ìyáàlù dùndún",
            "mother drum",
            "lead talking drum",
            "iya ilu",
            "iya-ilu"
        ],
        "description": "The master talking drum and commanding matriarchal voice of the Dùndún orchestra. Adorned with brass jingles (Ṣaworo) along both rims and played with a curved indigenous mallet (Kọ́nkọ́lọ́) while squeezing longitudinal leather tension cords (Ọsán) under the arm, the Ìyáàlù accurately reproduces the pitch glides, tonal inflections, and rhythmic morphology of spoken Yorùbá, reciting praise poetry (Oríkì), proverbial philosophy, and royal court proclamations.",
        "historical_timeline": "Antiquity (c. 12th Century CE): Consecrated under the hereditary guild of Àyàn master drummers (Àyàn Àgalú). Served as sonic communications network across ancient city-states. Transatlantic Survival: Preserved in Afro-Cuban Batá traditions and Brazilian Candomblé 'Ilú' drumming suites.",
        "etymology_and_philosophy": "From 'Ìyá' (mother) and 'Ìlù' (drum). Philosophically articulates the matriarchal foundation of Yorùbá sonic ontology, where the 'mother' instrument guides, disciplines, and harmonizes all auxiliary drums in the ensemble.",
        "material_and_craftsmanship": "Carved from a single resonant block of sacred softwood (Omo, Cordia millenii), fitted with cured goat skin or antelope hide membranes, bound with braided leather tuning thongs, and encircled with cast brass bells (Ṣaworo).",
        "social_and_ritual_context": "Lead instrument at coronation pageantry, funeral rituals of notables, ancestral masquerade festivals, and daily palace dawn greetings for the Ọba.",
        "proverbs_and_oral_traditions": [
            "Bí Ìyáàlù bá dún, àwọn ọmọ rẹ̀ a gbè é. (When the Mother Drum sounds, all her children drums harmonize in assent. This illustrates the harmonious order where matriarchal wisdom directs communal collective action.)",
            "Ẹnu Ìyáàlù kì í parọ́, ohun tí Àyàn bá kọ́ ọ ló ń sọ. (The mouth of the Mother Drum never utters falsehood; it speaks only what the ancestral deity Àyàn has taught it. This attests to the sacred truth-bearing nature of the talking drum.)"
        ],
        "diaspora_connections": "Crucial to Afro-Cuban Lucumí and Santería drumming rituals, where the Iya (lead batá) commands liturgical shifts and trance induction.",
        "geographical_origin": "Pan-Yorùbáland (Ọ̀yọ́, Èkìtì, Ìjẹ̀bú, Òṣun).",
        "curatorial_guidelines": "Display alongside carved wooden mallets, brass Ṣaworo bells, and acoustic soundboards demonstrating linguistic pitch mimicry.",
        "related_entities": [
            "Dùndún",
            "Gángan",
            "Gúdúgúdú",
            "Kẹríkẹrì",
            "Àyàn"
        ],
        "sub_variants": []
    }
]


def ingest():
    print("Ingesting 4 universal constellation sub-variants...")
    for path in [API_CORPUS_PATH, WEB_CORPUS_PATH]:
        with open(path, "r", encoding="utf-8") as f:
            corpus = json.load(f)

        existing_ids = {e["id"] for e in corpus}
        added_count = 0

        # Update parent sub_variants and related_entities
        for e in corpus:
            eid = e.get("id")
            if eid in ["Baṣọ̀run", "Baṣọ̀run (Prime Minister / Supreme Commander of Oyo)"]:
                sv = e.setdefault("sub_variants", [])
                for sub in ["Basọ̀run Gáà", "Basọ̀run Olúyọ̀lé", "Igbá Ìwà"]:
                    if sub not in sv:
                        sv.append(sub)
                re = e.setdefault("related_entities", [])
                for rel in ["Basọ̀run Olúyọ̀lé", "Igbá Ìwà"]:
                    if rel not in re:
                        re.append(rel)
            elif eid == "Adé":
                sv = e.setdefault("sub_variants", [])
                if "Adé Ọ̀kín" not in sv:
                    sv.append("Adé Ọ̀kín")
                re = e.setdefault("related_entities", [])
                if "Adé Ọ̀kín" not in re:
                    re.append("Adé Ọ̀kín")
            elif eid == "Dùndún":
                sv = e.setdefault("sub_variants", [])
                if "Ìyáàlù Dùndún" not in sv and "Ìyáàlù" not in sv:
                    sv.append("Ìyáàlù")
                re = e.setdefault("related_entities", [])
                if "Ìyáàlù" not in re and "Ìyáàlù Dùndún" not in re:
                    re.append("Ìyáàlù")

        for ent in NEW_ENTITIES:
            if ent["id"] not in existing_ids:
                # Add full record structure
                record = dict(ent)
                record["details"] = dict(ent)
                corpus.append(record)
                existing_ids.add(ent["id"])
                added_count += 1

        with open(path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, indent=2, ensure_ascii=False)

        print(f"Updated {path.name}: added {added_count} entities (Total now: {len(corpus)})")


if __name__ == "__main__":
    ingest()
