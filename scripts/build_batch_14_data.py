#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: BATCH 14 DATA GENERATOR (INDICES 233-256)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-009 (The 256 Odù Ifá Grand Finale)
Standards: Gate 2 Compliant (< 500 LOC), 14-Tier Schema Parity
Scope:
  - Remaining 9 chapters of Ọ̀ṣẹ́: ODU_233 to ODU_241 (completing Ọ̀ṣẹ́ cycle!)
  - Full 15 chapters of Òfún: ODU_242 to ODU_256 (completing Òfún cycle & the 256 Odù matrix!)
=============================================================================
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "scripts" / "batch_14_data.json"

BATCH_14_DATA = {
    "ODU_233_Ọ̀ṣẹ́_Ọ̀bàrà": {
        "historical_timeline": "Classical Antiquity (c. 11th–14th Century CE): Codified at Ilé-Ifẹ̀ as Ọ̀ṣẹ́-Bàrà, governing artistic prosperity, royal musical patronage, and the moral ethics of wealth. 19th-Century Era: Consulted by trading guilds and court praise-singers in Oyo and Ibadan. Contemporary/Diaspora: Retained in Lucumí Ifá as Ose Bara, celebrated for turning creative talent into sustainable abundance.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (I/II/I/II: victory, sweetness, artistic radiance) on the right and Ọ̀bàrà (I/II/II/II: abundance, sovereignty, modesty) on the left of Ọpọ́n Ifá. Dialectically balances creative brilliance with humble stewardship, teaching that genuine talent endures only when guided by modesty and generosity.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn across Ọpọ́n Ifá as I/II/I/II on the right and I/II/II/II on the left. The Babaláwo taps the northern quadrant with an ivory Ìrọ́kẹ́. Involves Ewé Ajé, Ewé Ọ̀dúndún, pure honey, sixteen cowries, and a white pigeon.",
        "social_and_ritual_context": "Cast for royal performers, sculptors, textile artisans, and entrepreneurs seeking commercial expansion through creative enterprises.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ kọrin ayọ̀, Ọ̀bàrà gbé adé ọrọ̀ dé; ọlọ́gbọ́n kì í fi ọrọ̀ rẹ̀ yangàn. (Ọ̀ṣẹ́ sang joyful melodies, and Ọ̀bàrà brought the crown of wealth; the wise never flaunts their riches: Creative abundance flourishes when rooted in humility.)",
            "Ọwọ́ tí ó mọ ọná ń jẹun nígbà gbogbo; ìwà pẹ̀lẹ́ ni adé oríire. (The hand skilled in art always feasts; a gentle character crowns good fortune: Industry and grace ensure lifelong sustenance.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_234_Ọ̀ṣẹ́_Ọ̀kànràn": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Kànràn, governing passionate judicial poetry, speaking truth to power through musical allegory, and dispelling slander. 19th-Century Era: Consulted by town criers and court poets during political crises. Contemporary/Diaspora: Preserved in Lucumí as Ose Kana, invoking Ṣàngó's protection against artistic envy.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (sweetness, beauty, melody) and Ọ̀kànràn (thunder, stern moral conscience, direct speech). Demonstrates that art is a potent vehicle for moral truth; sweet words devoid of integrity are flattery, whereas truth spoken with artistic grace pierces the conscience.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá with Ìyẹ̀rosùn as I/II/I/II on right and II/II/II/I on left. The Babaláwo strikes Ọpọ́n center with an ivory Ìrọ́kẹ́. Involves Ewé Ọ́kìkà, Ewé Tètè, ram offering, shea butter, and cold spring water.",
        "social_and_ritual_context": "Divined during heated chieftaincy disputes, public scandals, and when artists face censorship or false accusations.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ bu oyin sí ọ̀rọ̀, Ọ̀kànràn sọ òtítọ́; ọ̀rọ̀ dídùn kì í dín agbára òtítọ́ kù. (Ọ̀ṣẹ́ poured honey upon speech, and Ọ̀kànràn declared the truth; sweet expression never diminishes the authority of truth: Eloquent honesty commands universal conviction.)",
            "Iná ìbínú kì í ṣe oògùn ọ̀ràn; ẹnu tí ó mọ̀fẹ́ ló ń parí aṣọ̀. (The fire of wrath is never an antidote for conflict; the diplomatic voice settles discord: Measured speech dispels anger.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Barnes, Sandra T. (1997). Africa's Ogun: Old World and New; Bascom, William (1969). Ifa Divination."
    },
    "ODU_235_Ọ̀ṣẹ́_Ògúndá": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Gúndá, the sovereign chapter of ornamental metallurgy, brass ornamentation, lost-wax casting, and ceremonial weaponry. 19th-Century Era: Consulted by royal guilds casting brass regalia and ceremonial swords (Idà Ọba). Contemporary/Diaspora: Retained in Lucumí as Ose Ogunda, safeguarding artists handling sharp metal tools.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (aesthetic beauty) and Ògúndá (iron, technological force). Represents the transformative reconciliation of brute force with artistic beauty; iron hammered without artistic design remains an instrument of violence, but consecrated by art becomes a symbol of civilization.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as I/II/I/II on right and I/I/I/II on left. The Babaláwo touches a consecrated iron blade to Ọpọ́n center. Involves Ewé Pèrègún, iron filings, roasted yam, palm oil, and a rooster to Ògún.",
        "social_and_ritual_context": "Cast for blacksmiths, brass sculptors, jewelers, and engineers dedicating major artistic or infrastructural monuments.",
        "proverbs_and_oral_traditions": [
            "Ògún gbẹ́ irin, Ọ̀ṣẹ́ fi ẹwà dé e lédè; agbára tí ó wọ aṣọ ọgbọ́n kì í ṣìnà. (Ògún forged the iron, and Ọ̀ṣẹ́ adorned it in beauty; power clothed in wisdom never loses its path: Consecrated technical skill elevates society.)",
            "Irin tí ó bọ̀wọ̀ fún ọnà kì í fọ́; iṣẹ́ ọwọ́ tí ó mọ́ ló ń gbé oríire ga. (Iron that honors artistry never shatters; immaculate craftsmanship elevates human dignity: Disciplined labor bears enduring glory.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Williams, Denis (1974). Icon and Image."
    },
    "ODU_236_Ọ̀ṣẹ́_Ọ̀sá": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Sá, governing aesthetic intuition, appeasing the nocturnal mothers (*Àwọn Ìyámi*) through artistic pageantry (Gẹ̀lẹ̀dẹ́), and musical harmony. 19th-Century Era: Consulted during annual Gẹ̀lẹ̀dẹ́ mask dedications in Ketu and Egbado. Contemporary/Diaspora: Maintained in Lucumí as Ose Sa, invoking maternal spirits for artistic inspiration.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (beauty, celebration) and Ọ̀sá (flight, nocturnal spirits, astral wind). Teaches that maternal and spiritual forces are honored not through fearful groveling, but through transcendent beauty, celebratory masks, and sweet communal harmony.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as I/II/I/II on right and II/I/I/I on left. The Babaláwo circles the northern rim with an ivory Ìrọ́kẹ́. Involves Ewé Ègé, Ewé Ọ̀dúndún, cold maize gruel (Ẹ̀kọ), white pigeon, and cooked rabbit offering.",
        "social_and_ritual_context": "Divined during masquerade mask carvings, feminine ancestral festivals, and appeasing psychic disturbances through artistic offerings.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ jó fún àwọn ìyá, Ọ̀sá gbé orin fò dé ọ̀run; ẹni tí ó ba fi ẹwà bọ̀wọ̀ fún àwọn àgbà kì í rí ìpọ́njú. (Ọ̀ṣẹ́ danced before the mothers, and Ọ̀sá carried the hymn to heaven; he who honors elders with beauty encounters no grief: Aesthetic reverence disarms hostility.)",
            "Afẹ́fẹ́ tútù ló ń gbé adùn wọlé; ìrẹ̀lẹ̀ ọkàn ń pa iná ìbínú. (The cooling breeze ushers sweetness into the home; humility of soul quenches wrath: Gracious conduct fosters peace.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_237_Ọ̀ṣẹ́_Ìká": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Ká, governing the triumph of creative innocence over toxic envy, dissolving artistic plagiarism, and releasing creatives from insidious entrapments. 19th-Century Era: Consulted when guild rivals plotted against celebrated artisans. Contemporary/Diaspora: Retained in Lucumí as Ose Ka, celebrated for releasing initiates from toxic snares.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (radiant beauty, sweetness) and Ìká (restraint, the viper's coil, snare). Demonstrates that brilliant talent naturally attracts envious sabotage; maintaining moral purity and cheerful persistence dissolves the most venomous conspiracies.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as I/II/I/II on right and II/I/II/II on left. The Babaláwo uses an ivory Ìrọ́kẹ́ to cut a raffia strand on Ọpọ́n Ifá. Prepared with Ewé Ègé, Ewé Àlùpàyídà, pure honey, white pigeon, and severed raffia cord.",
        "social_and_ritual_context": "Cast when celebrated creatives or successful entrepreneurs are targeted by competitors with lawsuits, slander, or malicious traps.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ tú àwọ̀n Ìká, ó fi adùn gba oríire là; ẹyẹ tí ó lẹ́wà kì í bọ́ sí àwọ̀n ode. (Ọ̀ṣẹ́ unraveled the net of Ìká and delivered fortune through sweetness; the beautiful bird never perishes in the hunter's snare: Divine grace protects innocent brilliance.)",
            "A kì í fi owó búrúkú dènà ẹni tí Ọlọ́run kọ́ lẹ́kọ̀ọ́; òtítọ́ ló ń bẹ́ agbára ibi lórí. (One cannot block with wicked hands the person taught by the Divine; truth cuts through the power of malice: Spiritual authenticity outlasts intrigue.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Epega, A.A. & Neimark, P. (1995). The Sacred Ifa Oracle."
    },
    "ODU_238_Ọ̀ṣẹ́_Òtúúrúpọ̀n": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Túúrúpọ̀n, governing maternal beauty, postpartum physical recovery, pediatric cosmetic care, and radiant nursery blessings. 19th-Century Era: Consulted by midwives caring for royal nursing mothers in palace compounds. Contemporary/Diaspora: Retained in Lucumí as Ose Trupon, celebrated for infant health and maternal vitality.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (sweetness, beauty) and Òtúúrúpọ̀n (maternal nurture, carrying life). Teaches that the physical restoration of the mother is vital for the wellbeing of the lineage; honoring motherhood with comfort and celebratory beauty sustains human continuity.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as I/II/I/II on right and II/II/I/II on left. The Babaláwo taps the southern edge with an ivory Ìrọ́kẹ́. Involves Ewé Ọ̀já-Ọmọ, Ewé Ọ̀dúndún, pure honey, shea butter, and snail water.",
        "social_and_ritual_context": "Divined for postpartum mothers recovering vitality, naming ceremonies, and blessing childhood sleeping quarters.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ fi oyin tọ́ ọmọ, Òtúúrúpọ̀n pọ̀n ọn mọ́ra; abiyamọ tí ó nífẹ̀ẹ́ kì í jẹ́ kí ọmọ rẹ̀ kégbe. (Ọ̀ṣẹ́ nurtured the infant with honey, and Òtúúrúpọ̀n strapped the child close; the devoted mother never lets her child cry in distress: Loving nurture fosters joyful youth.)",
            "Ẹrù ọmọ kì í pa abiyamọ; ayọ̀ ọmọ bíbí ló ń mú kí ilé gbilẹ̀. (The burden of an infant never breaks the mother; the joy of childbirth is what expands the homestead: Generational care secures the future.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Fadipe, N.A. (1970). The Sociology of the Yoruba."
    },
    "ODU_239_Ọ̀ṣẹ́_Òtúá": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Túá, governing sacred hymns, prayers inspiring melodic eloquence, and divine inspiration for spiritual poets and orators. 19th-Century Era: Consulted during inter-provincial peace convocations to open sessions with sacred song. Contemporary/Diaspora: Maintained in Lucumí as Ose Tura, celebrated for answered prayers crowned with joy.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (melody, sweetness, beauty) and Òtúá (prayer, release, divine light). Teaches that when sincere prayer is expressed through beauty and music, it touches the heart of the universe; melodic devotion elevates the human spirit to communion with the Divine.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as I/II/I/II on right and I/II/I/I on left. The Babaláwo sweeps Ìyẹ̀rosùn with a white horse-tail whisk (Ìrùkẹ̀rẹ̀). Involves Ewé Ẹfun, Ewé Tètè, pure honey, white chalk (Ẹfun), and a white dove.",
        "social_and_ritual_context": "Cast for sacred singers, poets, liturgical leaders, and individuals seeking divine inspiration for creative undertakings.",
        "proverbs_and_oral_traditions": [
            "Òtúá gbàdúrà, Ọ̀ṣẹ́ kọrin ìyìn; àdúrà tí a fi ayọ̀ gbà kì í bọ́ sí asán. (Òtúá prayed, and Ọ̀ṣẹ́ sang praises; the prayer offered with joy never lapses into vanity: Joyful faith commands divine fulfillment.)",
            "Orin mímọ́ ń ṣí ìlẹ̀kùn ọ̀run; ọkàn tí ó kún fún ìdúpẹ́ ń rí àṣẹ gbà. (Sacred hymns unlock the gates of heaven; the heart laden with gratitude receives spiritual authority: Thanksgiving brings blessings.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Law, Robin (1977). The Oyo Empire."
    },
    "ODU_240_Ọ̀ṣẹ́_Ìrẹtẹ̀": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Rẹtẹ̀ or Ọ̀ṣẹ́-Bilé, governing cosmetic herbal formulas, rejuvenating radiant skin after physical illness, and herbal black soap (Ọṣẹ Dúdú) craft. 19th-Century Era: Consulted by master soap-makers and cosmetic herbalists in Ondo and Osogbo. Contemporary/Diaspora: Preserved in Lucumí as Ose Bile, renowned for herbal soap consecration and skin vitality.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (beauty, sweet waters) and Ìrẹtẹ̀ (medicinal action, purification, carving). Emphasizes that true beauty is built upon internal bodily purity; medicinal hygiene cleanses away blemishes to reveal radiant inner health.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as I/II/I/II on right and I/I/II/I on left. The Babaláwo touches the southern perimeter with an ivory Ìrọ́kẹ́. Involves Ewé Ìrẹtẹ̀, Ewé Ṣaworo, traditional black soap, shea butter, and pure honey.",
        "social_and_ritual_context": "Divined when preparing sacred therapeutic soaps, recovering cosmetic vitality after severe skin disease, and blessing public bathhouses.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ wẹ ara mọ́, Ìrẹtẹ̀ bọ́ àbùkù dànù; ìmọ́tótó ara ló ń fi ẹwà hàn. (Ọ̀ṣẹ́ washed the body clean, and Ìrẹtẹ̀ cast off all blemishes; bodily cleanliness reveals true beauty: Wholesome hygiene brings forth radiance.)",
            "Ọṣẹ tí ó mọ́ kì í dọ̀tí; ìwà tútù àti ìlera ni aṣọ olódodo. (The cleansing soap is never soiled; gentle character and radiant health are the vestments of the righteous: Purity preserves honor.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_241_Ọ̀ṣẹ́_Òfún": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀ṣẹ́-Fún, the sacred conclusion of the Ọ̀ṣẹ́ cycle, uniting Ọ̀ṣun's riverine sweetness with Ọbàtálá's pristine white mantle of creation. 19th-Century Era: Consulted during royal festivals celebrating matrimonial reconciliation in Ilé-Ifẹ̀. Contemporary/Diaspora: Maintained in Lucumí as Ose Fun, crowning aesthetic endeavors with supreme sanctity.",
        "etymology_and_philosophy": "Conjunction of Ọ̀ṣẹ́ (sweetness, beauty) and Òfún (primordial white clay, creation, supreme source). Teaches that the highest expression of beauty is pure, untarnished righteousness; art reaches divine status when it directs the human heart toward holiness.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as I/II/I/II on right and II/I/II/I on left. The Babaláwo marks a circle of white chalk (Ẹfun) around Ọpọ́n Ifá. Involves pure white chalk (Ẹfun), Ewé Òdúndún, cold water, sixteen snails, and white linen.",
        "social_and_ritual_context": "Cast for mature artists concluding their life's work, crowning matrimonial celebrations, and purifying community sanctuaries.",
        "proverbs_and_oral_traditions": [
            "Ọ̀ṣẹ́ da oyin sílẹ̀, Òfún fi ẹfun mímọ́ bò ó; ẹwà tí ó ní ìwà mímọ́ kì í parun. (Ọ̀ṣẹ́ poured out honey, and Òfún covered it with sacred white chalk; beauty endowed with holiness never perishes: Consecrated grace endures through eternity.)",
            "Aṣọ funfun kì í gba ẹ̀gbin; ìwà rere ni ohun ọ̀ṣọ́ tí ó dára jùlọ. (White vestments tolerate no stain; virtuous character is the finest adornment: Pure righteousness outshines worldly ornament.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_242_Òfún_Ogbè": {
        "historical_timeline": "Classical Antiquity (c. 11th–14th Century CE): Codified at Ilé-Ifẹ̀ as Òfún-Nàgbè or Òfún-Ogbè, the paramount sovereign chapter of primordial creation, Ọbàtálá's white clay modeling human form, and total cosmic light. 19th-Century Era: Consulted by supreme Ọbàtálá council priests during national renewal ceremonies. Contemporary/Diaspora: Retained in Lucumí as Ofun Nagbe, renowned for miraculous birth and spiritual renewal.",
        "etymology_and_philosophy": "Conjunction of Òfún (II/I/II/I: primordial creation, white clay, gestation) on the right and Ogbè (I/I/I/I: absolute light, life, victory) on the left of Ọpọ́n Ifá. Dialectically represents the cosmic dawn of human existence; creation takes living breath through divine light.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn across Ọpọ́n Ifá as II/I/II/I on the right and I/I/I/I on the left. The Babaláwo strikes the central hearth (`Àárín Ọpọ́n`) with an ivory Ìrọ́kẹ́. Involves pure white chalk (Ẹfun), Ewé Òdúndún, cold spring water, sixteen land snails, and white linen.",
        "social_and_ritual_context": "Cast during national renewal ceremonies, healing congenital reproductive crises, and dedicating paramount shrines of creation.",
        "proverbs_and_oral_traditions": [
            "Òfún mọ amọ̀, Ogbè fún un ní ẹ̀mí; ọwọ́ Ọbàtálá ló ń ṣe ẹ̀dá ní àgbàyanu. (Òfún molded the sacred clay, and Ogbè endowed it with living breath; the hand of Ọbàtálá fashions humanity in wonder: Divine craftsmanship animates all existence.)",
            "Ẹni tí Ọlọ́run dá kì í tẹ́; ìmọ́lẹ̀ òtítọ́ ló ń ṣe amọ̀nà fún oríire. (The being fashioned by the Divine is never disgraced; the light of truth guides righteous destiny: Primordial purpose guarantees ultimate fulfillment.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_243_Òfún_Ọ̀yẹ̀kú": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Yẹ̀kú, governing peaceful longevity, the serene passing of venerable elders, and transforming the terror of death into honorable ancestral rest. 19th-Century Era: Consulted when venerable monarchs reached extreme old age. Contemporary/Diaspora: Preserved in Lucumí as Ofun Yeku, celebrated for longevity covenants and peaceful endings.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, white clay) and Ọ̀yẹ̀kú (twilight, mortality, cooling, ancestral rest). Teaches that death for the virtuous elder is not defeat, but a serene return to the primordial source; pure character robs the grave of its sting.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá with Ìyẹ̀rosùn as II/I/II/I on right and II/II/II/II on left. The Babaláwo uses an ivory Ìrọ́kẹ́ to direct offerings toward the southern realm. Involves Ewé Ìran, Ewé Akòko, white chalk (Ẹfun), pure honey, and a white sheep.",
        "social_and_ritual_context": "Divined for elderly patriarchs and matriarchs seeking peaceful completion of life, ancestral transitions, and averting sudden catastrophes.",
        "proverbs_and_oral_traditions": [
            "Òfún fi aṣọ funfun wọ̀ ọ́, Ọ̀yẹ̀kú paná ìbẹ̀rù ikú; ọjọ́ ogbó tí ó ní àlàáfíà ni ẹ̀bùn tí ó ga jùlọ. (Òfún clothed the soul in white, and Ọ̀yẹ̀kú quenched the fear of death; peaceful old age is the supreme gift of life: Virtuous living leads to tranquil rest.)",
            "Igi tí ó fẹsẹ̀ múlẹ̀ dáradára kì í ṣubú láì gbó; orísun mímọ́ ló ń gbé ẹ̀mí ga. (The tree firmly rooted never falls before its ripe maturity; a pure foundation elevates long life: Righteous living secures longevity.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_244_Òfún_Ìwòrì": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Wòrì or Òfún-Gèmú, governing profound philosophical contemplation, esoteric wisdom of white-haired sages, and discerning the origins of human consciousness. 19th-Century Era: Consulted by high councils of elders arbitrating complex customary laws. Contemporary/Diaspora: Retained in Lucumí as Ofun Gemi / Ofun Iwori, celebrated for deep esoteric vision.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, pristine origin) and Ìwòrì (deep visionary contemplation). Teaches that the deepest knowledge is not clever sophistry, but the quiet contemplation of primordial cosmic principles; wisdom resides with those who contemplate origins.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/I on right and II/I/I/II on left. The Babaláwo taps the northern perimeter with an ivory Ìrọ́kẹ́. Involves Ewé Gbégbé, Ewé Àjídèwe, clear spring water, white chalk, and a white dove.",
        "social_and_ritual_context": "Cast for judicial arbiters, spiritual teachers, philosophers, and counselors evaluating difficult moral crossroads.",
        "proverbs_and_oral_traditions": [
            "Òfún wo orísun ayé, Ìwòrì rí ìmọ́lẹ̀ ọgbọ́n; ọlọ́gbọ́n tòótọ́ kì í sọ̀rọ̀ láì ronú jinlẹ̀. (Òfún contemplated the cosmic source, and Ìwòrì beheld the light of wisdom; the true sage never speaks without deep reflection: Contemplation gives birth to authoritative guidance.)",
            "Ojú tí ó ti rí ọ̀pọ̀ ọdún ń mọ ojú ọ̀nà tọ́; ìmọ̀ràn àgbà ni odi ìlú. (The eyes that have seen many seasons know the righteous pathway; the counsel of elders is the rampart of the commonwealth: Reverence for wisdom sustains society.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_245_Òfún_Òdí": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Dí, governing the fortification of ethical character (*Ìwà Rere*), building impenetrable spiritual barriers against corruption, and preserving virgin purity. 19th-Century Era: Consulted when consecrating sacred city boundary posts. Contemporary/Diaspora: Maintained in Lucumí as Ofun Di, celebrated for creating unbreachable domestic shields.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, purity) and Òdí (rampart, foundation, protective barrier). Demonstrates that spiritual purity must be fortified by rigorous self-discipline; a pristine character without defensive boundaries is easily corrupted by societal vice.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as II/I/II/I on right and I/II/II/I on left. The Babaláwo seals the markings with a consecrated smooth river stone. Involves Ewé Pèrègún, Ewé Tètè, white chalk (Ẹfun), river stone, and a male goat.",
        "social_and_ritual_context": "Divined before dedicating new sanctuaries, protecting youths from negative peer influences, and establishing ethical guidelines for communities.",
        "proverbs_and_oral_traditions": [
            "Òfún fi amọ̀ funfun mọ odi, Òdí ti ẹnu-ọ̀nà rẹ̀; ìwà mímọ́ tí a mọ odi mọ́ kì í wó. (Òfún built the rampart with sacred white clay, and Òdí sealed its gateway; holy character protected by boundaries never crumbles: Disciplined boundaries safeguard moral integrity.)",
            "Odi tí ó lágbára kì í jẹ́ kí olè wọlé; ààbò ọkàn ni ìbẹ̀rù Ọlọ́run. (A sturdy rampart never permits thieves to enter; the spiritual defense of the soul is reverence for the Divine: Moral reverence grants immunity.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_246_Òfún_Ìrosùn": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Rosùn, the sacred union of Ọbàtálá's white chalk (Ẹfun) and the ancestors' red camwood (Osùn), balancing primordial creation with lineage continuity. 19th-Century Era: Consulted during royal investitures uniting priests of Ọbàtálá and ancestral monarchs. Contemporary/Diaspora: Retained in Lucumí as Ofun Koso / Ofun Iroso, celebrated for lineage blessings.",
        "etymology_and_philosophy": "Conjunction of Òfún (white clay, creation, supreme coolness) and Ìrosùn (red camwood, blood memory, lineage fire). Dialectically unites pristine divine origin with human ancestral bloodline; reminds initiates that heaven and ancestral heritage meet in the human vessel.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/I on right and I/I/II/II on left. The Babaláwo strokes Ọpọ́n Ifá blending white chalk and red camwood. Involves Ewé Ọ̀dúndún, Osùn powder, white chalk (Ẹfun), white rooster, and white cloth.",
        "social_and_ritual_context": "Cast during royal crowning ceremonies, ancestral reconciliation rites, and celebrating birth across noble lineages.",
        "proverbs_and_oral_traditions": [
            "Ẹfun funfun pàdé osùn pupa, àlàáfíà wọ ilé dé; àpapọ̀ ọ̀run àti ilẹ̀ ló ń bí oríire. (White chalk met red camwood, and peace entered the home; the convergence of heaven and earth produces good fortune: Harmonizing divine grace with ancestral roots brings prosperity.)",
            "Ọmọ tí ó rántí orírun rẹ̀ kì í ṣìnà; ìmọ́lẹ̀ àwọn baba wa ń tan sí ọ̀nà wa. (The child who remembers their origins never goes astray; the light of our forebears illuminates our path: Heritage anchors true destiny.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art."
    },
    "ODU_247_Òfún_Ọ̀wọ́nrín": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Wọ́nrín, governing the calming of sudden communal panics, overcoming famine through sacred food reserves, and maintaining divine poise in chaos. 19th-Century Era: Consulted by town governors during sudden wartime siege alerts. Contemporary/Diaspora: Maintained in Lucumí as Ofun Juani, celebrated for sudden divine rescues.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, peace, supreme stability) and Ọ̀wọ́nrín (sudden cosmic reversal, turbulence). Teaches that the serenity of Ọbàtálá is an immovable mountain; when volatile winds blow, the sage remains cool, centered, and patient.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as II/I/II/I on right and II/II/I/I on left. The Babaláwo strikes the southwestern quadrant with an ivory Ìrọ́kẹ́. Involves Ewé Òdúndún, Ewé Tètè, cold water, roasted corn, palm oil, and a white hen.",
        "social_and_ritual_context": "Divined during sudden community emergencies, commercial downturns, and sudden family shocks requiring steady leadership.",
        "proverbs_and_oral_traditions": [
            "Ọ̀wọ́nrín mú ìjì wá, Òfún fi sùúrù paná rẹ̀; orí tí ó tútù kì í bọ́ sí kòtò. (Ọ̀wọ́nrín brought the gale, but Òfún cooled it with patience; the calm head never tumbles into the pit: Serene patience weathers sudden crises.)",
            "Bí ayé bá ń mì, olódodo ń dúró gbọnyingbọnyin; ìgbàgbọ́ nínú Ọlọ́run ni odi tí kò lè wó. (Though the earth shakes, the righteous stands firm; faith in the Divine is an unshakable bastion: Inner tranquility overcomes external chaos.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_248_Òfún_Ọ̀bàrà": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Bàrà, governing consecrated royal sovereignty, wealth sanctified to feed the destitute, and moral modesty in high office. 19th-Century Era: Consulted during royal installation rites in Oyo and Ketu. Contemporary/Diaspora: Retained in Lucumí as Ofun Bara, celebrated for turning modest resources into noble abundance.",
        "etymology_and_philosophy": "Conjunction of Òfún (purity, divine origin) and Ọ̀bàrà (abundance, royalty, modesty). Teaches that political sovereignty is a sacred trust from Ọbàtálá; rulers who accumulate riches for selfish vanity violate cosmic law and invite ancestral downfall.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/I on right and I/II/II/II on left. The Babaláwo taps the northern quadrant with an ivory Ìrọ́kẹ́. Involves Ewé Ajé, Ewé Ọ̀dúndún, pure honey, sixteen cowries, white chalk, and a white pigeon.",
        "social_and_ritual_context": "Cast for newly crowned rulers, government ministers, philanthropic leaders, and corporate executives stewarding public resources.",
        "proverbs_and_oral_traditions": [
            "Òfún fi aṣọ funfun wọ̀ ọ́, Ọ̀bàrà dé adé ọrọ̀; adé tí a fi òtítọ́ wọ̀ kì í já bọ́. (Òfún clothed him in white linen, and Ọ̀bàrà placed the crown of wealth upon him; the crown worn with integrity never falls: Consecrated stewardship preserves royal authority.)",
            "Ọrọ̀ tí ó ní ìbẹ̀rù Ọlọ́run ń bọ́ gbogbo ìlú; ìrẹ̀lẹ̀ ọba ló ń mú kí ìjọba rẹ̀ pẹ́. (Riches guided by reverence for the Divine nourish the entire commonwealth; the humility of the monarch secures an enduring reign: Moral leadership inspires loyalty.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_249_Òfún_Ọ̀kànràn": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Kànràn, governing divine justice, judicial decrees delivered under Ọbàtálá's authority, and shattering false testimonies. 19th-Century Era: Consulted by judicial panels before passing sentence on disputed capital offenses. Contemporary/Diaspora: Preserved in Lucumí as Ofun Kana, invoked for divine vindication.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, purity, Ọbàtálá) and Ọ̀kànràn (thunder, stern conscience, direct truth). Teaches that mercy and purity do not imply weakness; when moral law is mocked, the divine white clay speaks with the voice of thunder to uphold cosmic balance.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as II/I/II/I on right and II/II/II/I on left. The Babaláwo strikes Ọpọ́n center with an ivory Ìrọ́kẹ́. Involves Ewé Ọ́kìkà, Ewé Tètè, white chalk (Ẹfun), ram offering, and cold spring water.",
        "social_and_ritual_context": "Divined during judicial arbitrations, confronting institutional corruption, and seeking vindication from malicious frame-ups.",
        "proverbs_and_oral_traditions": [
            "Òfún sọ̀kalẹ̀ láti ọ̀run, Ọ̀kànràn sọ àṣẹ òdodo; ẹni tí ó ba ń dán Ọlọ́run wò yóò tẹ́. (Òfún descended from heaven, and Ọ̀kànràn proclaimed righteous authority; he who mocks divine law shall be humbled: Cosmic justice relentlessly vindicates the innocent.)",
            "Òtítọ́ kì í bẹ̀rù ìdájọ́; ẹni tí ọkàn rẹ̀ bá mọ́ ń rìn láì fòyà. (Truth never fears the judgment seat; he whose conscience is pure walks without fear: Moral innocence grants unflinching courage.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Barnes, Sandra T. (1997). Africa's Ogun: Old World and New; Bascom, William (1969). Ifa Divination."
    },
    "ODU_250_Òfún_Ògúndá": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Gúndá, governing the spiritual ethics of metallurgy, sculpting royal wooden and ivory regalia, and sanctifying ironcraft to constructive ends. 19th-Century Era: Consulted by master carvers sculpting palace posts for the Ọọ̀ni of Ifẹ̀. Contemporary/Diaspora: Retained in Lucumí as Ofun Funda / Ofun Ogunda, celebrated for ethical craftsmanship.",
        "etymology_and_philosophy": "Conjunction of Òfún (purity, creation, Ọbàtálá) and Ògúndá (iron blade, industrial technology). Represents the spiritual sanctification of human industry; technological capability must submit to moral creativity, building up communities rather than tearing them down.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/I on right and I/I/I/II on left. The Babaláwo touches an iron tool to white chalk on Ọpọ́n center. Involves Ewé Pèrègún, white chalk (Ẹfun), iron filings, roasted yam, palm oil, and a white rooster.",
        "social_and_ritual_context": "Cast before inaugurating grand architecture, dedicating master sculpture commissions, and opening industrial guild workshops.",
        "proverbs_and_oral_traditions": [
            "Ọbàtálá fún alágbẹ̀dẹ ní ìmọ̀, Ògún la ojú ọ̀nà; iṣẹ́ ọnà tí a fi ọ̀wọ̀ ṣe kì í parun. (Ọbàtálá endowed the blacksmith with skill, and Ògún opened the road; craftsmanship executed with reverence never perishes: Consecrated labor builds enduring civilization.)",
            "Idà tí ó mọ̀fẹ́ kì í jẹ́ kí ẹ̀jẹ̀ ṣàn lásán; ọgbọ́n ló ń darí agbára irin. (The blade guided by wisdom never sheds blood in vain; wisdom directs the power of iron: Ethical restraint governs power.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Williams, Denis (1974). Icon and Image."
    },
    "ODU_251_Òfún_Ọ̀sá": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Sá, governing reconciliation between supreme celestial light and nocturnal astral entities, bringing spiritual peace across all dimensions of reality. 19th-Century Era: Consulted during peace negotiations between differing spiritual societies. Contemporary/Diaspora: Maintained in Lucumí as Ofun Sa, invoking harmony between Ọbàtálá and Yemọja.",
        "etymology_and_philosophy": "Conjunction of Òfún (primordial light, purity) and Ọ̀sá (flight, nocturnal wind, spiritual mobility). Teaches that the visible and invisible worlds must live in reciprocal peace; spiritual maturity embraces the mystery of the cosmos without fear or arrogance.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as II/I/II/I on right and II/I/I/I on left. The Babaláwo circles the perimeter with an ivory Ìrọ́kẹ́. Involves Ewé Ègé, Ewé Ọ̀dúndún, cold maize gruel (Ẹ̀kọ), white chalk (Ẹfun), and a white dove.",
        "social_and_ritual_context": "Divined when settling inter-guild spiritual disputes, curing sleep disorders, and cultivating serene peace across family lineages.",
        "proverbs_and_oral_traditions": [
            "Òfún tan ìmọ́lẹ̀, Ọ̀sá gbé àlàáfíà fò dé orí ayé; ẹni tí ó ba bá gbogbo ẹ̀dá ré kì í rí ewu. (Òfún shed radiant light, and Ọ̀sá bore peace aloft over the earth; he who walks in harmony with all creation faces no peril: Universal reverence brings universal protection.)",
            "Afẹ́fẹ́ tútù kì í ba aṣọ funfun jẹ́; ìrẹ̀lẹ̀ inú ló ń mú oríire wá. (The cooling breeze never soils the white linen; inner humility attracts enduring blessings: Quiet grace conquers hostility.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_252_Òfún_Ìká": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Ká, governing the complete dissolution of malevolent conspiracies, deliverance from treacherous entrapments, and unraveling venomous schemes through primordial purity. 19th-Century Era: Invoked during military betrayals to reveal traitors in royal courts. Contemporary/Diaspora: Retained in Lucumí as Ofun Ka, celebrated for delivering initiates from insidious snares.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, purity, divine innocence) and Ìká (restraint, the viper's coil, snare). Demonstrates that the white mantle of Ọbàtálá dissolves the most venomous serpent's coil; malevolent schemes devour themselves in the presence of spotless righteousness.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/I on right and II/I/II/II on left. The Babaláwo cuts through a knotted raffia thread on Ọpọ́n Ifá with an ivory Ìrọ́kẹ́. Involves Ewé Ègé, Ewé Àlùpàyídà, white chalk (Ẹfun), white pigeon, and severed raffia cord.",
        "social_and_ritual_context": "Cast when someone is surrounded by envious enemies, ensnared in corrupt contracts, or trapped in destructive conspiracies.",
        "proverbs_and_oral_traditions": [
            "Òfún já àwọ̀n Ìká dànù, ó fi aṣọ funfun gba ẹni rere là; ẹni tí ó gbẹ́ kòtò ibi yóò wọ̀ ọ́ fúnra rẹ̀. (Òfún tore the net of Ìká to shreds and delivered the righteous with white vestments; he who digs the pit of malice shall tumble into it himself: Divine innocence shatters treachery.)",
            "A kì í fi owó búrúkú bẹ Ọlọ́run níṣẹ́; òtítọ́ nìkan ló ń borí gbogbo ìkà. (One cannot bribe the Divine with wicked hands; truth alone conquers all cruelty: Pure righteousness outlasts malice.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Epega, A.A. & Neimark, P. (1995). The Sacred Ifa Oracle."
    },
    "ODU_253_Òfún_Òtúúrúpọ̀n": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Túúrúpọ̀n, governing Ọbàtálá's blessing over the human womb, safeguarding embryological development, pediatric longevity, and pristine maternal care. 19th-Century Era: Consulted by royal midwives during complex imperial pregnancies. Contemporary/Diaspora: Maintained in Lucumí as Ofun Trupon, celebrated for sacred pregnancy rites.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, white clay, divine modeling) and Òtúúrúpọ̀n (maternal care, carrying life). Teaches that the infant is shaped directly by Ọbàtálá's sacred hands; revering motherhood and protecting the unborn preserves the divine thread of human civilization.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as II/I/II/I on right and II/II/I/II on left. The Babaláwo taps the southern edge with an ivory Ìrọ́kẹ́. Involves Ewé Ọ̀já-Ọmọ, Ewé Ọ̀dúndún, pure white chalk (Ẹfun), shea butter, and snail broth.",
        "social_and_ritual_context": "Divined for pregnant women, difficult conceptions, dedicating pediatric nurseries, and consecrating newborn destinies.",
        "proverbs_and_oral_traditions": [
            "Ọbàtálá mọ ọmọ nínú ilé-ọlẹ̀, Òtúúrúpọ̀n pọ̀n ọn mọ́ra; ẹ̀dá tí Ọlọ́run dá kì í tẹ́. (Ọbàtálá molded the child within the sanctuary of the womb, and Òtúúrúpọ̀n strapped the child close; the soul fashioned by the Divine never suffers disgrace: Divine creation safeguards life.)",
            "Ẹrù ọmọ kì í pa abiyamọ; ayọ̀ ìbí ọmọ ló ń sọ ilé di ọgbà àlàáfíà. (The burden of an infant never breaks the mother; the joy of childbirth turns the homestead into a garden of peace: Sacrificial maternal love builds the future.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Fadipe, N.A. (1970). The Sociology of the Yoruba."
    },
    "ODU_254_Òfún_Òtúá": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Túá or Òfún-Tèmọ́lẹ̀, governing pristine spiritual prayers ascending straight to Ọlọ́run, divine covenants blessing nations, and uncorrupted priesthood. 19th-Century Era: Consulted during peace treaties ending major regional conflicts. Contemporary/Diaspora: Preserved in Lucumí as Ofun Tura, celebrated for answered prayers and divine light.",
        "etymology_and_philosophy": "Conjunction of Òfún (primordial white clay, creation, purity) and Òtúá (prayer, illumination, divine release). Demonstrates that when prayer is offered from a heart free of malice and deceit, it ascends directly to the celestial throne without impediment; moral purity is the soul of prayer.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/I on right and I/II/I/I on left. The Babaláwo sweeps Ìyẹ̀rosùn with a white Ìrùkẹ̀rẹ̀ whisk and draws an Ẹfun line. Involves Ewé Ẹfun, Ewé Tètè, white chalk (Ẹfun), pure honey, and a white dove.",
        "social_and_ritual_context": "Cast during national prayer convocations, dedications of major temples, installations of supreme priests, and high covenants.",
        "proverbs_and_oral_traditions": [
            "Òtúá gbàdúrà, Òfún da aṣọ funfun bo ayé; àdúrà tí ó mọ́ kì í já sí asán. (Òtúá prayed, and Òfún draped the world in white vestments; the prayer offered in purity never falls to the earth in vain: Sincere spiritual devotion commands cosmic fulfillment.)",
            "Ọ̀nà tí Ọlọ́run bá ṣí, kò sí ẹni tí ó lè tì í; ìmọ́lẹ̀ òtítọ́ ló ń lé òkùnkùn sá. (The pathway that the Supreme Being opens, none can shut; the light of truth dispels all darkness: Divine providence guarantees ultimate vindication.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Law, Robin (1977). The Oyo Empire."
    },
    "ODU_255_Òfún_Ìrẹtẹ̀": {
        "historical_timeline": "Classical Antiquity: Codified as Òfún-Rẹtẹ̀ or Òfún-Bìrẹtẹ̀, governing complete physical and spiritual regeneration, stamping out deep-seated hereditary infirmities, and surgical purification. 19th-Century Era: Consulted when long-standing plague epidemics finally subsided. Contemporary/Diaspora: Retained in Lucumí as Ofun Rete, invoking Babalú-Ayé and Ọbàtálá for final healing.",
        "etymology_and_philosophy": "Conjunction of Òfún (creation, purity, supreme source) and Ìrẹtẹ̀ (trampling down disease, surgical purification, firm footstep). Teaches that complete healing occurs when medical treatment is crowned with spiritual purification; when corruption is eradicated, the human body reflects pristine divine wholeness.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá as II/I/II/I on right and I/I/II/I on left. The Babaláwo touches the southern edge with an ivory Ìrọ́kẹ́. Involves Ewé Ìrẹtẹ̀, Ewé Ṣaworo, pure white chalk (Ẹfun), shea butter, and consecrated palm oil.",
        "social_and_ritual_context": "Divined when patients recover from life-threatening chronic disease, epidemiological purifications, and concluding medical convalescence.",
        "proverbs_and_oral_traditions": [
            "Òfún wo ara sàn, Ìrẹtẹ̀ tẹ àrùn mọ́lẹ̀; àlàáfíà Ọlọ́run ló ń kọ́ odi ìlera. (Òfún healed the body, and Ìrẹtẹ̀ trampled disease underfoot; the peace of the Divine builds the fortress of health: Complete recovery unites physical and spiritual purity.)",
            "Bí a bá fọ ara dé inú, ìmọ́lẹ̀ ń tàn jáde; ìlera tòótọ́ ni orísun gbogbo ayọ̀. (When one cleanses both outer flesh and inner spirit, radiant light shines forth; genuine health is the spring of all joy: Pristine wholeness endures.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_256_Òfún_Ọ̀ṣẹ́": {
        "historical_timeline": "Classical Antiquity (c. 11th–14th Century CE): Codified at Ilé-Ifẹ̀ as Òfún-Ṣẹ́ or Òfún-Mewó, the sacred 256th and crowning chapter of the entire Ifá binary corpus, representing the ultimate cosmic union of Ọbàtálá's white mantle of creation and Ọ̀ṣun's golden river of sweetness and joy. 19th-Century Era: Consulted at the conclusion of supreme coronation and universal peace assemblies. Contemporary/Diaspora: Preserved in Lucumí as Ofun She, crowning the entire 256 Odù matrix with universal blessing, peace, and eternal beauty.",
        "etymology_and_philosophy": "Conjunction of Òfún (II/I/II/I: primordial creation, white clay, the womb of existence) on the right and Ọ̀ṣẹ́ (I/II/I/II: victory, sweetness, artistic radiance, Ọ̀ṣun's river) on the left of Ọpọ́n Ifá. Dialectically concludes the entire 256 Odù Ifá binary matrix: creation without sweetness is sterile, while sweetness without creation lacks substance; their perfect union completes the cosmos in eternal harmony, peace, and moral beauty (*Àṣẹ Ìwà Pẹ̀lẹ́*).",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn across Ọpọ́n Ifá as II/I/II/I on the right and I/II/I/II on the left. The Babaláwo taps the four quadrants of Ọpọ́n Ifá with an ivory Ìrọ́kẹ́ and sprinkles consecrated river water mixed with white chalk. Involves pure white chalk (Ẹfun), pure honey, Ewé Òdúndún, Ewé Ọ̀ṣun, sixteen land snails, white linen, and sixteen cowries.",
        "social_and_ritual_context": "Cast at the coronation of supreme monarchs, the final sealing of major treaties, dedicating grand temples of creation, and celebrating the complete cycle of human existence.",
        "proverbs_and_oral_traditions": [
            "Òfún mọ ayé ní ẹfun funfun, Ọ̀ṣẹ́ bu oyin adùn sí i; gbogbo ẹ̀dá kún fún ayọ̀ àti àlàáfíà láéláé. (Òfún fashioned the world in pristine white chalk, and Ọ̀ṣẹ́ poured the honey of sweetness upon it; all creation is filled with joy and peace forever: The cosmic marriage of purity and beauty completes the universe.)",
            "Oríire tí ó wọ ilé kì í tún jáde mọ́; ìwà pẹ̀lẹ́ ni adé tí ó ga jùlọ nínú ayé. (The good fortune that enters the righteous dwelling never departs; gentle character is the supreme crown of existence: Moral perfection seals cosmic harmony.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle; Verger, Pierre (1995). Ewé."
    }
}


def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: GENERATING BATCH 14 DATA VAULT (INDICES 233-256)")
    print("================================================================================")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(BATCH_14_DATA, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully wrote {len(BATCH_14_DATA)} records to {OUTPUT_FILE}")
    print("=" * 80)


if __name__ == "__main__":
    main()
