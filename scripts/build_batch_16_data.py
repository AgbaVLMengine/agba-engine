#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: BATCH 16 DATA GENERATOR (INDICES 25-49)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Corpus Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-003 (Batch 16 Non-Odù Hardening: Entities 25–49)
Standards: Gate 2 Compliant (< 500 LOC), 14-Tier Schema Parity
Scope:
  - 25 foundational civic, ecological, guild, and military entities:
    Ẹyẹ, Ẹranko, Ìlú, Odò, Òkè, Odi, Ojúbọ, Igbó, Ọjà, Àwọ̀, Gbẹ́nàgbẹ́nà,
    Amọ̀, Idẹ, Àgbẹ̀dẹ, Oníṣègùn, Apẹja, Ìwunṣọ, Ọdẹ, Ọkọ́, Oko,
    Àpáta_Shield, Ọfà, Idà, Ogun (Warfare & Military Tradition), Àmì_Ọlá.
=============================================================================
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "scripts" / "batch_16_data.json"

BATCH_16_DATA = {
    "Ẹyẹ": {
        "provenance_and_citations": (
            "Lawal, Babatunde (1996). The Gẹ̀lẹ̀dẹ́ Spectacle: Art, Gender, and Social Harmony in an African Culture. "
            "Seattle: University of Washington Press; Abiodun, Rowland (2014). Yoruba Art and Language: Seeking the "
            "African in African Art. Cambridge: Cambridge University Press; Verger, Pierre Fatumbi (1995). Ewé: "
            "The Use of Plants in Yoruba Society. São Paulo: Odebrecht & Paris: Editions M.H."
        )
    },
    "Ẹranko": {
        "provenance_and_citations": (
            "Drewal, Henry John, & Pemberton, John III (1989). Yoruba: Nine Centuries of African Art and Thought. "
            "New York: Center for African Art & Harry N. Abrams; Bascom, William (1969). Ifa Divination: "
            "Communication Between Gods and Men in West Africa. Bloomington: Indiana University Press; "
            "Abiodun, Rowland (2014). Yoruba Art and Language. Cambridge: Cambridge University Press."
        )
    },
    "Ìlú": {
        "provenance_and_citations": (
            "Smith, Robert S. (1988). Kingdoms of the Yoruba. 3rd ed. Madison: University of Wisconsin Press; "
            "Johnson, Samuel (1921). The History of the Yorubas from the Earliest Times to the Beginning of the "
            "British Protectorate. London: Routledge; Fadipe, N. A. (1970). The Sociology of the Yoruba. "
            "Ibadan: Ibadan University Press; Mabogunje, Akin L. (1962). Yoruba Towns. Ibadan: Ibadan University Press."
        )
    },
    "Odò": {
        "provenance_and_citations": (
            "Ìdòwú, E. Bọ́lájì (1962). Olódùmarè: God in Yoruba Belief. London: Longmans; Verger, Pierre Fatumbi "
            "(1995). Ewé: The Use of Plants in Yoruba Society. São Paulo: Odebrecht; Abímbọ́lá, Wándé (1976). "
            "Ifá: An Exposition of Ifá Literary Corpus. Ibadan: Oxford University Press Nigeria."
        )
    },
    "Òkè": {
        "provenance_and_citations": (
            "Johnson, Samuel (1921). The History of the Yorubas. London: Routledge; Smith, Robert S. (1988). "
            "Kingdoms of the Yoruba. Madison: University of Wisconsin Press; Ojo, G. J. Afolabi (1966). "
            "Yoruba Culture: A Geographical Analysis. London: University of London Press."
        )
    },
    "Odi": {
        "provenance_and_citations": (
            "Smith, Robert S. (1988). Kingdoms of the Yoruba. Madison: University of Wisconsin Press; "
            "Ajayi, J. F. A., & Smith, Robert S. (1964). Yoruba Warfare in the Nineteenth Century. "
            "Cambridge: Cambridge University Press; Johnson, Samuel (1921). The History of the Yorubas. London: Routledge."
        )
    },
    "Ojúbọ": {
        "provenance_and_citations": (
            "Ìdòwú, E. Bọ́lájì (1962). Olódùmarè: God in Yoruba Belief. London: Longmans; Drewal, Henry John, "
            "& Pemberton, John III (1989). Yoruba: Nine Centuries of African Art and Thought. New York: Center "
            "for African Art; Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá. Paris: UNESCO."
        )
    },
    "Igbó": {
        "provenance_and_citations": (
            "Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society. São Paulo: Odebrecht; "
            "Babayemi, S. O. (1980). Egungun among the Oyo Yoruba. Ibadan: Board Publications; Fadipe, N. A. (1970). "
            "The Sociology of the Yoruba. Ibadan: Ibadan University Press."
        )
    },
    "Ọjà": {
        "provenance_and_citations": (
            "Fadipe, N. A. (1970). The Sociology of the Yoruba. Ibadan: Ibadan University Press; Awe, Bolanle (1992). "
            "Nigerian Women in Historical Perspective. Lagos: Sankore / Bookcraft; Falola, Toyin (1984). "
            "The Political Economy of a Pre-colonial African State: Ibadan, 1830–1900. Ile-Ife: University of Ife Press."
        )
    },
    "Àwọ̀": {
        "provenance_and_citations": (
            "Drewal, Henry John, & Pemberton, John III (1989). Yoruba: Nine Centuries of African Art and Thought. "
            "New York: Center for African Art; Johnson, Samuel (1921). The History of the Yorubas. London: Routledge; "
            "Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa. Bloomington: Indiana University Press."
        )
    },
    "Gbẹ́nàgbẹ́nà": {
        "provenance_and_citations": (
            "Abiodun, Rowland (2014). Yoruba Art and Language: Seeking the African in African Art. Cambridge: "
            "Cambridge University Press; Lawal, Babatunde (2001). Awòrán: Representing the Self and Its Metaphysical "
            "Other in Yoruba Art. The Art Bulletin 83(3): 498–526; Drewal, Henry John, & Pemberton, John III (1989). "
            "Yoruba: Nine Centuries of African Art and Thought. New York: Center for African Art."
        )
    },
    "Amọ̀": {
        "provenance_and_citations": (
            "Lawal, Babatunde (1996). The Gẹ̀lẹ̀dẹ́ Spectacle: Art, Gender, and Social Harmony in an African Culture. "
            "Seattle: University of Washington Press; Fadipe, N. A. (1970). The Sociology of the Yoruba. "
            "Ibadan: Ibadan University Press; Willett, Frank (1967). Ife in the History of West African Sculpture. "
            "London: Thames and Hudson."
        )
    },
    "Idẹ": {
        "provenance_and_citations": (
            "Willett, Frank (1967). Ife in the History of West African Sculpture. London: Thames and Hudson; "
            "Williams, Denis (1974). Icon and Image: A Study of Sacred and Secular Forms of African Classical Art. "
            "London: Allen Lane; Drewal, Henry John, & Pemberton, John III (1989). Yoruba: Nine Centuries of "
            "African Art and Thought. New York: Center for African Art."
        )
    },
    "Àgbẹ̀dẹ": {
        "provenance_and_citations": (
            "Barnes, Sandra T. (1997). Africa's Ogun: Old World and New. Bloomington: Indiana University Press; "
            "Johnson, Samuel (1921). The History of the Yorubas. London: Routledge; Williams, Denis (1974). "
            "Icon and Image: A Study of Sacred and Secular Forms of African Classical Art. London: Allen Lane."
        )
    },
    "Oníṣègùn": {
        "proverbs_and_oral_traditions": [
            (
                "Kò sí ewé tí kò ní iṣẹ́ tirẹ̀ nínú igbó; olúwarẹ̀ kò tíì mọ ìwúlò rẹ̀ ni (There is no leaf "
                "in the wild forest without its destined medicinal virtue; it is only human intellect that has "
                "yet to comprehend its healing power. Philosophical commentary: This oral tradition anchors the "
                "metaphysical foundation of traditional African medicine, asserting that every botanical specimen "
                "embodies therapeutic or protective Àṣẹ.)"
            ),
            (
                "Oníṣègùn tó mọ ewé ló ń wo àrùn, àmọ́ Ọlọ́run ló ń wo ọmọ ènìyàn sàn (The herbal physician "
                "diagnoses and prescribes the sacred herbs, but it is Olódùmarè who ultimately enacts the complete "
                "restoration of human life. Philosophical commentary: Enforces professional humility and spiritual "
                "attunement among indigenous practitioners, teaching that clinical mastery must remain deferential "
                "to divine providence.)"
            ),
            (
                "Ewé ńlá kì í sùn nínú igbó kí ebi pa oníṣègùn; ọgbọ́n ewé ni adé àlàáfíà. (The great healing herb "
                "never slumbers in the forest while the herbal physician languishes; botanical mastery is the true crown "
                "of holistic wellbeing. Philosophical commentary: Underscores that deep ecological knowledge, medicinal "
                "discernment, and covenantal attunement with nature grant life, health, and societal sustenance.)"
            )
        ],
        "provenance_and_citations": (
            "Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society. São Paulo: Odebrecht & "
            "Paris: Editions M.H.; Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus. "
            "Ibadan: Oxford University Press Nigeria; Fadipe, N. A. (1970). The Sociology of the Yoruba. "
            "Ibadan: Ibadan University Press."
        )
    },
    "Apẹja": {
        "provenance_and_citations": (
            "Smith, Robert S. (1988). Kingdoms of the Yoruba. Madison: University of Wisconsin Press; "
            "Fadipe, N. A. (1970). The Sociology of the Yoruba. Ibadan: Ibadan University Press; "
            "Bascom, William (1951). Yoruba Food & Cooking. Africa 21(1): 41–53."
        )
    },
    "Ìwunṣọ": {
        "provenance_and_citations": (
            "Eicher, Joanne Bubolz (1976). Nigerian Handcrafted Textiles. Ile-Ife: University of Ife Press; "
            "Nwafor, Okechukwu (2021). Aso Ebi: Cloth and Sociability in Urban Nigeria. Ann Arbor: University "
            "of Michigan Press; Abiodun, Rowland (2014). Yoruba Art and Language: Seeking the African in African Art. "
            "Cambridge: Cambridge University Press."
        )
    },
    "Ọdẹ": {
        "provenance_and_citations": (
            "Barnes, Sandra T. (1997). Africa's Ogun: Old World and New. Bloomington: Indiana University Press; "
            "Babayemi, S. O. (1980). Egungun among the Oyo Yoruba. Ibadan: Board Publications; "
            "Johnson, Samuel (1921). The History of the Yorubas. London: Routledge."
        )
    },
    "Ọkọ́": {
        "provenance_and_citations": (
            "Fadipe, N. A. (1970). The Sociology of the Yoruba. Ibadan: Ibadan University Press; "
            "Barnes, Sandra T. (1997). Africa's Ogun: Old World and New. Bloomington: Indiana University Press; "
            "Bascom, William (1951). Yoruba Food & Cooking. Africa 21(1): 41–53."
        )
    },
    "Oko": {
        "provenance_and_citations": (
            "Fadipe, N. A. (1970). The Sociology of the Yoruba. Ibadan: Ibadan University Press; "
            "Lloyd, P. C. (1962). Yoruba Land Law. London: Oxford University Press; Falola, Toyin (1984). "
            "The Political Economy of a Pre-colonial African State: Ibadan, 1830–1900. Ile-Ife: University of Ife Press."
        )
    },
    "Àpáta_Shield": {
        "provenance_and_citations": (
            "Ajayi, J. F. A., & Smith, Robert S. (1964). Yoruba Warfare in the Nineteenth Century. "
            "Cambridge: Cambridge University Press; Smith, Robert S. (1988). Kingdoms of the Yoruba. "
            "Madison: University of Wisconsin Press; Johnson, Samuel (1921). The History of the Yorubas. London: Routledge."
        )
    },
    "Ọfà": {
        "provenance_and_citations": (
            "Smith, Robert S. (1988). Kingdoms of the Yoruba. Madison: University of Wisconsin Press; "
            "Ajayi, J. F. A., & Smith, Robert S. (1964). Yoruba Warfare in the Nineteenth Century. "
            "Cambridge: Cambridge University Press; Johnson, Samuel (1921). The History of the Yorubas. London: Routledge."
        )
    },
    "Idà": {
        "provenance_and_citations": (
            "Barnes, Sandra T. (1997). Africa's Ogun: Old World and New. Bloomington: Indiana University Press; "
            "Johnson, Samuel (1921). The History of the Yorubas. London: Routledge; "
            "Smith, Robert S. (1988). Kingdoms of the Yoruba. Madison: University of Wisconsin Press."
        )
    },
    "Ogun (Warfare & Military Tradition)": {
        "provenance_and_citations": (
            "Ajayi, J. F. A., & Smith, Robert S. (1964). Yoruba Warfare in the Nineteenth Century. "
            "Cambridge: Cambridge University Press; Akíntóyè, S. A. (1971). Revolution and Power Politics "
            "in Yorubaland 1840–1893. London: Longman; Smith, Robert S. (1988). Kingdoms of the Yoruba. "
            "Madison: University of Wisconsin Press; Johnson, Samuel (1921). The History of the Yorubas. London: Routledge."
        )
    },
    "Àmì_Ọlá": {
        "provenance_and_citations": (
            "Abiodun, Rowland (2014). Yoruba Art and Language: Seeking the African in African Art. "
            "Cambridge: Cambridge University Press; Drewal, Henry John, & Pemberton, John III (1989). "
            "Yoruba: Nine Centuries of African Art and Thought. New York: Center for African Art; "
            "Johnson, Samuel (1921). The History of the Yorubas. London: Routledge."
        )
    }
}


def build_data():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(BATCH_16_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated {len(BATCH_16_DATA)} Batch 16 records in {OUTPUT_FILE}")


if __name__ == "__main__":
    build_data()
