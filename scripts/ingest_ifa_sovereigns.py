#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: DEDICATED INGESTION OF IFÁ SOVEREIGN RECORDS
=============================================================================
Author: Àrọ̀kìn (arokin-archivist)
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Execution Directive: HANDOFF-AROKIN-BATCH-002

Ingests dedicated, permanent canonical records for:
1. Ojú Odù Méjìdínlógún (The 16 Principal King Odùs)
2. Àmọ̀lù Odù (The 240 Composite / Permutated Chapters of Ifá)
Synchronizes api/data/yoruba_corpus_1007_NORMALIZED.json and web/src/data/yoruba_master_corpus.json.
=============================================================================
"""

import json
from pathlib import Path
from typing import List, Dict, Any

REPO_ROOT = Path(__file__).resolve().parent.parent
API_PATH = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_PATH = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"

OJU_ODU_RECORD: Dict[str, Any] = {
    "id": "Oju_Odu_Mejidinlogun",
    "title": "Ojú Odù Méjìdínlógún",
    "culture": "Yorùbá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
        "16 king odus",
        "16 principal odu",
        "oju odu",
        "oju odu mejidindlogun",
        "oju odu mejidinlogun",
        "oju odu merindinlogun",
        "oju-odu",
        "ojú odù",
        "ojú odù méjìdínlógún",
        "ojú odù mẹ́rìndínlógún",
        "olodu meji",
        "olódù méjì",
        "sixteen king odus",
        "sixteen principal odus",
        "the sixteen major odu"
    ],
    "description": "The Sixteen Primordial King Odùs of the Ifá binary matrix (Èjì Ogbè through Òfún Méjì), representing the foundational cosmological pillars, archetypal forces, and sacred mathematical ontology of Yorùbá epistemology.",
    "historical_timeline": "Classical Ilé-Ifẹ̀ Antiquity (c. 8th–11th Century CE): Codified by Ọ̀rúnmìlà Bara Àgbọnmìrègún at Òkè-Ìgẹ́ti, Ilé-Ifẹ̀, as the sixteen sovereign royal chapters of cosmic law. Each Ojú Odù was recognized as a primordial deity and metaphysical king governing specific natural elements, ethical covenants, and spiritual destinies. Medieval Ọ̀yọ́ Empire (14th–18th Century CE): Structured the constitutional ethics of the Ọ̀yọ́-Mèsì and the statecraft of the Aláàfin, who sat under the divine counsel of Èjì Ogbè and Òfún Méjì. Transatlantic Diaspora Retention: Inscribed into Lucumí Ifá in Cuba and Candomblé Ketu in Brazil, where the sixteen Olódù Méjì remain the unshakeable liturgy of global Yorùbá sacred divination. Contemporary Recognition: Recognized in 2005 under the UNESCO Masterpiece of Oral and Intangible Heritage of Humanity.",
    "etymology_and_philosophy": "Etymologically derived from 'Ojú' (eyes, primordial source, faces, or principal apertures) and 'Odù' (wombs of cosmic power, containers of divine revelation, or sovereign matrices), paired with 'Mẹ́rìndínlógún' (sixteen). Philosophically, they embody the binary dialectic of light and void, expansion and contraction, through which Olódùmarè structured existence. The 16 King Odùs form an exponential mathematical ontology: 16 × 16 = 256, generating the totality of all existential situations.",
    "material_and_craftsmanship": "Cast and marked upon the carved sacred divination tray (Ọpọ́n Ifá) using sacred wood powder (Ìyẹ̀ròsùn), manipulated through sixteen consecrated sacred palm nuts (Ìkín Ifá) gathered from sacred palm trees, or cast rapidly with the eight-half seed divining chain (Ọ̀pẹ̀lẹ̀) crafted of bronze, copper, and Agbalumo/Opele seed halves.",
    "social_and_ritual_context": "The Ojú Odù Méjìdínlógún are invoked at the supreme rites of existence: the coronation of paramount monarchs (Ọba), the formal initiation of Babaláwos (Ìtẹ̀fá), national crises, treaties of peace, and funerals of high priests. They hold absolute constitutional authority over all moral codes and civic taboos (Èèwọ̀).",
    "proverbs_and_oral_traditions": [
        "Ojú Odù mẹ́rìndínlógún ni àpótí ìmọ̀ Ọlọ́run; ẹni tí ó bá tẹ̀ ẹ́ kì í dáràn nílé ayé. (The sixteen primordial Odù are the supreme treasury of divine wisdom; whoever grounds their life upon their ethical foundation shall never walk into destruction: Teaching that cosmic laws and moral alignment preserve human destiny against spiritual chaos.)",
        "Èjì Ogbè l'ó bí wọ́n pátápátá, Òfún Méjì l'ó tún wọn ṣe; àì mọ ojú odù, awo kì í d'awo. (Èjì Ogbè brought forth all the sacred chapters, and Òfún Méjì perfected their cosmic balance; without mastering the sixteen king Odù, an initiate can never truly attain priesthood: Highlighting the rigorous epistemological discipline required of Babaláwos.)",
        "Bí a bá dá Ifá tí a rí Olódù, gbogbo ayé l'ó ń dákẹ́ rọ́rọ́ gbọ́ ọ̀rọ̀ àwọn àgbà. (When the sacred divination reveals an Olódù Méjì, the entire assembly falls silent to hear the sovereign voice of the cosmic elders: Reverencing the supreme judicial and spiritual authority of the principal sixteen chapters.)"
    ],
    "diaspora_connections": "Preserved in intact hierarchical order across Cuban Santería/Ifá, Venezuelan Regla de Ocha, and Brazilian Ilê Axé sanctuaries.",
    "geographical_origin": "Ilé-Ifẹ̀ (Òkè-Ìgẹ́ti), Òkè-Ìtasẹ̀, Ado-Ekiti.",
    "media_production_notes": "Visually depict the sixteen paired binary column marks (from I I / I I / I I / I I down to II II / II II / II II / II II) inscribed in golden Ìyẹ̀ròsùn dust across the polished rim of an antique carved Ọpọ́n Ifá.",
    "is_parent": True,
    "sovereign_parent": "Odù Ifá",
    "sovereign_parent_status": "Sovereign Parent Concept",
    "sub_variants": [
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
        "Òfún Méjì"
    ],
    "details": {
        "description": "The Sixteen Primordial King Odùs of the Ifá binary matrix (Èjì Ogbè through Òfún Méjì), representing the foundational cosmological pillars, archetypal forces, and sacred mathematical ontology of Yorùbá epistemology.",
        "historical_timeline": "Classical Ilé-Ifẹ̀ Antiquity (c. 8th–11th Century CE): Codified by Ọ̀rúnmìlà Bara Àgbọnmìrègún at Òkè-Ìgẹ́ti, Ilé-Ifẹ̀, as the sixteen sovereign royal chapters of cosmic law. Each Ojú Odù was recognized as a primordial deity and metaphysical king governing specific natural elements, ethical covenants, and spiritual destinies. Medieval Ọ̀yọ́ Empire (14th–18th Century CE): Structured the constitutional ethics of the Ọ̀yọ́-Mèsì and the statecraft of the Aláàfin, who sat under the divine counsel of Èjì Ogbè and Òfún Méjì. Transatlantic Diaspora Retention: Inscribed into Lucumí Ifá in Cuba and Candomblé Ketu in Brazil, where the sixteen Olódù Méjì remain the unshakeable liturgy of global Yorùbá sacred divination. Contemporary Recognition: Recognized in 2005 under the UNESCO Masterpiece of Oral and Intangible Heritage of Humanity.",
        "etymology_and_philosophy": "Etymologically derived from 'Ojú' (eyes, primordial source, faces, or principal apertures) and 'Odù' (wombs of cosmic power, containers of divine revelation, or sovereign matrices), paired with 'Mẹ́rìndínlógún' (sixteen). Philosophically, they embody the binary dialectic of light and void, expansion and contraction, through which Olódùmarè structured existence. The 16 King Odùs form an exponential mathematical ontology: 16 × 16 = 256, generating the totality of all existential situations.",
        "material_and_craftsmanship": "Cast and marked upon the carved sacred divination tray (Ọpọ́n Ifá) using sacred wood powder (Ìyẹ̀ròsùn), manipulated through sixteen consecrated sacred palm nuts (Ìkín Ifá) gathered from sacred palm trees, or cast rapidly with the eight-half seed divining chain (Ọ̀pẹ̀lẹ̀) crafted of bronze, copper, and Agbalumo/Opele seed halves.",
        "social_and_ritual_context": "The Ojú Odù Méjìdínlógún are invoked at the supreme rites of existence: the coronation of paramount monarchs (Ọba), the formal initiation of Babaláwos (Ìtẹ̀fá), national crises, treaties of peace, and funerals of high priests. They hold absolute constitutional authority over all moral codes and civic taboos (Èèwọ̀).",
        "proverbs_and_oral_traditions": [
            "Ojú Odù mẹ́rìndínlógún ni àpótí ìmọ̀ Ọlọ́run; ẹni tí ó bá tẹ̀ ẹ́ kì í dáràn nílé ayé. (The sixteen primordial Odù are the supreme treasury of divine wisdom; whoever grounds their life upon their ethical foundation shall never walk into destruction: Teaching that cosmic laws and moral alignment preserve human destiny against spiritual chaos.)",
            "Èjì Ogbè l'ó bí wọ́n pátápátá, Òfún Méjì l'ó tún wọn ṣe; àì mọ ojú odù, awo kì í d'awo. (Èjì Ogbè brought forth all the sacred chapters, and Òfún Méjì perfected their cosmic balance; without mastering the sixteen king Odù, an initiate can never truly attain priesthood: Highlighting the rigorous epistemological discipline required of Babaláwos.)",
            "Bí a bá dá Ifá tí a rí Olódù, gbogbo ayé l'ó ń dákẹ́ rọ́rọ́ gbọ́ ọ̀rọ̀ àwọn àgbà. (When the sacred divination reveals an Olódù Méjì, the entire assembly falls silent to hear the sovereign voice of the cosmic elders: Reverencing the supreme judicial and spiritual authority of the principal sixteen chapters.)"
        ],
        "diaspora_connections": "Preserved in intact hierarchical order across Cuban Santería/Ifá, Venezuelan Regla de Ocha, and Brazilian Ilê Axé sanctuaries.",
        "geographical_origin": "Ilé-Ifẹ̀ (Òkè-Ìgẹ́ti), Òkè-Ìtasẹ̀, Ado-Ekiti.",
        "media_production_notes": "Visually depict the sixteen paired binary column marks (from I I / I I / I I / I I down to II II / II II / II II / II II) inscribed in golden Ìyẹ̀ròsùn dust across the polished rim of an antique carved Ọpọ́n Ifá.",
        "sub_variants": [
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
            "Òfún Méjì"
        ],
        "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa; Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art."
    },
    "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa; Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art."
}

AMOLU_ODU_RECORD: Dict[str, Any] = {
    "id": "Amolu_Odu",
    "title": "Àmọ̀lù Odù",
    "culture": "Yorùbá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
        "240 composite odus",
        "240 minor odus",
        "amolu",
        "amolu ifa",
        "amolu odu",
        "amulu",
        "amulu odu",
        "composite odu",
        "minor odu",
        "omo odu",
        "permutated chapters of ifa",
        "àmọ̀lù odù",
        "àmúlù odù",
        "ọmọ odù"
    ],
    "description": "The 240 Composite and Permutated Chapters of the Ifá divination corpus (Àmọ̀lù or Ọmọ Odù), formed by the cross-pairing of the 16 Principal King Odùs to address nuanced human crises, specific medicinal recipes, and moral jurisprudence.",
    "historical_timeline": "Classical Antiquity (c. 9th–13th Century CE): Developed as the complex diagnostic application of Ifá science at Ilé-Ifẹ̀, expanding the 16 primary archetypes into 240 dynamic hybrid chapters (e.g., Ogbè-Ọ̀yẹ̀kú, Ògúndá-Bèdé, Òtúá-Méjì combinations) capable of diagnosing specific psychological, ecological, and generational ailments. Guild Evolution: Transmitted orally through specialized hereditary Babaláwo academies across Èkìtì, Ìjẹ̀bú, Ọ̀yọ́, and Ẹ̀gbá. Atlantic Survival: Retained with extraordinary fidelity in Cuba as the 'Tratados de los Oddun de Ifá' and Brazil as 'Caminhos de Odú', preserving precise botanical pharmacopeia across centuries of diaspora exile.",
    "etymology_and_philosophy": "Derived from 'À-mọ̀-lù' (that which is crafted through dynamic fusion or mixture; from 'mọ' meaning to mould/fashion and 'lù' meaning to blend or interweave), also traditionally called 'Àmúlù' or 'Ọmọ Odù' (children of the sovereign Odù). Philosophically, it reflects dialectical realism: life situations are rarely pure archetype, but rather complex combinations of competing forces (e.g., life paired with vulnerability, wealth paired with spiritual contest).",
    "material_and_craftsmanship": "Cast through the two symmetrical columns of the Ọ̀pẹ̀lẹ̀ divining chain or inscribed as two distinct vertical four-mark tetragrams upon the Ọpọ́n Ifá tray. Accompanied by specialized botanical preparations (Ètùtutù, Àkọ́ṣẹ́) prepared in apothecary mortars by guild priests.",
    "social_and_ritual_context": "Used in day-to-day diagnostic consultations (Dídá Ifá) for individuals confronting specific illnesses, marital choices, agricultural ventures, or spiritual blockages. Each of the 240 composite chapters governs specific sacrifice formulations (Ẹbọ), protective talismans, and therapeutic herbal infusions.",
    "proverbs_and_oral_traditions": [
        "Àmọ̀lù kò ṣe é fojú tẹ́ńbẹ́lú; ọmọ odù ni ó ń yan ẹbọ fún gbogbo ayé. (The composite chapters must never be scorned or underestimated; it is the child-Odù that diagnoses the precise sacrifice required to heal all worldly afflictions: Teaching that practical everyday healing resides in detailed, specific application rather than broad generalizations.)",
        "Bí Olódù bá jẹ́ ọba, Àmọ̀lù ni balógun tó ń jagun fún àlàáfíà. (If the sixteen principal Odù are the crowned monarchs, the composite chapters are the vanguard marshals who wage the actual battle for earthly peace and wellness: Highlighting their active diagnostic role in resolving acute human suffering.)",
        "Àmúlù l'ó ń tú ọ̀rọ̀ dídíjú; Ifá kì í fọwọ́ rọ́ ẹni tí ó mọ ìpìlẹ̀ wọn dáadáa. (It is the paired combination that unravels the most tangled knots of existence; Ifá never fails an initiate who understands their foundational genealogy: Emphasizing the mastery of cross-permutational wisdom.)"
    ],
    "diaspora_connections": "Form the foundational diagnostic manual of Lucumí Ifá in Cuba, Puerto Rico, Venezuela, and the Afro-Brazilian Terreiros of Salvador da Bahia.",
    "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́-Ilé, Kétu, Ònkò.",
    "media_production_notes": "Depict the asymmetrical two-column tetragram (e.g. Ogbè on the right, Ọ̀yẹ̀kú on the left) drawn on a weathered circular Ọpọ́n Ifá rimmed with bronze cowrie motifs.",
    "is_parent": False,
    "sovereign_parent": "Odù Ifá",
    "sovereign_parent_status": "Living Sovereign Matrix",
    "sub_variants": [],
    "details": {
        "description": "The 240 Composite and Permutated Chapters of the Ifá divination corpus (Àmọ̀lù or Ọmọ Odù), formed by the cross-pairing of the 16 Principal King Odùs to address nuanced human crises, specific medicinal recipes, and moral jurisprudence.",
        "historical_timeline": "Classical Antiquity (c. 9th–13th Century CE): Developed as the complex diagnostic application of Ifá science at Ilé-Ifẹ̀, expanding the 16 primary archetypes into 240 dynamic hybrid chapters (e.g., Ogbè-Ọ̀yẹ̀kú, Ògúndá-Bèdé, Òtúá-Méjì combinations) capable of diagnosing specific psychological, ecological, and generational ailments. Guild Evolution: Transmitted orally through specialized hereditary Babaláwo academies across Èkìtì, Ìjẹ̀bú, Ọ̀yọ́, and Ẹ̀gbá. Atlantic Survival: Retained with extraordinary fidelity in Cuba as the 'Tratados de los Oddun de Ifá' and Brazil as 'Caminhos de Odú', preserving precise botanical pharmacopeia across centuries of diaspora exile.",
        "etymology_and_philosophy": "Derived from 'À-mọ̀-lù' (that which is crafted through dynamic fusion or mixture; from 'mọ' meaning to mould/fashion and 'lù' meaning to blend or interweave), also traditionally called 'Àmúlù' or 'Ọmọ Odù' (children of the sovereign Odù). Philosophically, it reflects dialectical realism: life situations are rarely pure archetype, but rather complex combinations of competing forces (e.g., life paired with vulnerability, wealth paired with spiritual contest).",
        "material_and_craftsmanship": "Cast through the two symmetrical columns of the Ọ̀pẹ̀lẹ̀ divining chain or inscribed as two distinct vertical four-mark tetragrams upon the Ọpọ́n Ifá tray. Accompanied by specialized botanical preparations (Ètùtutù, Àkọ́ṣẹ́) prepared in apothecary mortars by guild priests.",
        "social_and_ritual_context": "Used in day-to-day diagnostic consultations (Dídá Ifá) for individuals confronting specific illnesses, marital choices, agricultural ventures, or spiritual blockages. Each of the 240 composite chapters governs specific sacrifice formulations (Ẹbọ), protective talismans, and therapeutic herbal infusions.",
        "proverbs_and_oral_traditions": [
            "Àmọ̀lù kò ṣe é fojú tẹ́ńbẹ́lú; ọmọ odù ni ó ń yan ẹbọ fún gbogbo ayé. (The composite chapters must never be scorned or underestimated; it is the child-Odù that diagnoses the precise sacrifice required to heal all worldly afflictions: Teaching that practical everyday healing resides in detailed, specific application rather than broad generalizations.)",
            "Bí Olódù bá jẹ́ ọba, Àmọ̀lù ni balógun tó ń jagun fún àlàáfíà. (If the sixteen principal Odù are the crowned monarchs, the composite chapters are the vanguard marshals who wage the actual battle for earthly peace and wellness: Highlighting their active diagnostic role in resolving acute human suffering.)",
            "Àmúlù l'ó ń tú ọ̀rọ̀ dídíjú; Ifá kì í fọwọ́ rọ́ ẹni tí ó mọ ìpìlẹ̀ wọn dáadáa. (It is the paired combination that unravels the most tangled knots of existence; Ifá never fails an initiate who understands their foundational genealogy: Emphasizing the mastery of cross-permutational wisdom.)"
        ],
        "diaspora_connections": "Form the foundational diagnostic manual of Lucumí Ifá in Cuba, Puerto Rico, Venezuela, and the Afro-Brazilian Terreiros of Salvador da Bahia.",
        "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́-Ilé, Kétu, Ònkò.",
        "media_production_notes": "Depict the asymmetrical two-column tetragram (e.g. Ogbè on the right, Ọ̀yẹ̀kú on the left) drawn on a weathered circular Ọpọ́n Ifá rimmed with bronze cowrie motifs.",
        "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa; McClelland, E.M. (1982). The Cult of Ifá Among the Yoruba; Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society."
    },
    "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa; McClelland, E.M. (1982). The Cult of Ifá Among the Yoruba; Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society."
}


def ingest_records():
    for path in [API_PATH, WEB_PATH]:
        with open(path, "r", encoding="utf-8") as f:
            corpus: List[Dict[str, Any]] = json.load(f)

        existing_titles = {e.get("title") for e in corpus}
        existing_ids = {e.get("id") for e in corpus}

        added = 0
        for rec in [OJU_ODU_RECORD, AMOLU_ODU_RECORD]:
            if rec["id"] not in existing_ids and rec["title"] not in existing_titles:
                corpus.append(rec)
                added += 1
            else:
                for idx, e in enumerate(corpus):
                    if e.get("id") == rec["id"] or e.get("title") == rec["title"]:
                        corpus[idx] = rec
                        print(f"   [!] Updated existing record '{rec['title']}' in {path.name}")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, ensure_ascii=False, indent=2)

        print(f"✅ Ingested {added} sovereign records into {path.name} (Total: {len(corpus)})")


if __name__ == "__main__":
    ingest_records()
