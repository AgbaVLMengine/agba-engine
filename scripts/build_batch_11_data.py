#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: BATCH 11 DATA GENERATOR (INDICES 158-182)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Directive: HANDOFF-AROKIN-006
Standards: Gate 2 Compliant (< 500 LOC), 14-Tier Schema Parity
Scope:
  - 9 remaining chapters of Ọ̀sá: ODU_158 to ODU_166 (completing Ọ̀sá cycle!)
  - Full 15 chapters of Ìká: ODU_167 to ODU_181 (completing Ìká cycle!)
  - Opening chapter of Òtúúrúpọ̀n: ODU_182
=============================================================================
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "scripts" / "batch_11_data.json"

BATCH_11_DATA = {
    "ODU_158_Ọ̀sá_Ọ̀bàrà": {
        "historical_timeline": "Classical Antiquity (c. 11th–14th Century CE): Codified at Ilé-Ifẹ̀ as Ọ̀sá-Bàrà, governing spiritual trade diplomacy, intuitive commercial caravans, and maternal blessings on wealth. 19th-Century Era: Consulted by merchant guild leaders navigating regional tolls and wartime trade routes. Contemporary/Diaspora: Preserved in Lucumí and Candomblé Ketu lineages as Osa Bara, celebrated for turning volatile social conditions into financial abundance.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (II/I/I/I: the mystical wind, intuitive flight) on the right and Ọ̀bàrà (I/II/II/II: royal abundance, nobility, eloquence) on the left of Ọpọ́n Ifá. Dialectically balances unpredictable spiritual tides with sovereign economic rectitude, teaching that enduring prosperity is preserved when commercial ambition is guided by spiritual humility.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn across Ọpọ́n Ifá as II/I/I/I on the right and I/II/II/II on the left. Interaction with Ìrọ́kẹ́ Ifá involves tapping the northern rim to awaken Olókun and Ọ̀bàrà's mercantile aṣẹ. Prepared with Ewé Ajé, Ewé Ọ̀dúndún, pure honey, pigeon, and sixteen consecrated cowries.",
        "social_and_ritual_context": "Cast for caravan leaders, entrepreneurs, and market chiefs seeking expansion amidst unpredictable sociopolitical storms.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá gbé ọrọ̀ wọlé, Ọ̀bàrà fi adé bò ó; ọlọ́gbọ́n kì í jẹ́ kí afẹ́fẹ́ kó ọrọ̀ rẹ̀ lọ. (Ọ̀sá ushered wealth into the dwelling, and Ọ̀bàrà crowned it with majesty; the sage never permits the gale to scatter his harvest: Prudent stewardship preserves sudden fortune.)",
            "Bí a bá ń wá owó, a kì í fẹnu kò lu àwọn àgbà; ìrẹ̀lẹ̀ ní ń fa ọrọ̀ mọ́ra. (When pursuing wealth, one must never quarrel with elders; humility is the magnet that attracts enduring prosperity: Filial reverence secures lasting success.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_159_Ọ̀sá_Ọ̀kànràn": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Kànràn or Ọ̀sá-Lọ́kọ̀, governing judicial clarity, controlling reckless wrath, and dispelling spiritual bewilderment. 19th-Century Era: Consulted during tribunal arbitrations to prevent false testimony during the Yorùbá civil wars. Contemporary/Diaspora: Retained in Afro-Cuban Ocha-Ifá as Osa Kana, invoking Ṣàngó's protection against witchcraft.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (mystical wind, spiritual flight) and Ọ̀kànràn (thunder, moral conscience, direct speech). Teaches that the fury of righteous indignation must be tempered by cool discernment; violent anger unguided by wisdom destroys both the accuser and the sanctuary.",
        "material_and_craftsmanship": "Marked upon Ọpọ́n Ifá with Ìyẹ̀rosùn as II/I/I/I on the right and II/II/II/I on the left. The Babaláwo uses an ivory Ìrọ́kẹ́ to chant pacification verses to Ṣàngó. Involves Ewé Ọ́kìkà, Ewé Tètè, ram offering, and cool spring water.",
        "social_and_ritual_context": "Cast during bitter family inheritance disputes, heated chieftaincy conflicts, and judicial crises requiring impartial verdict.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá kànràn sọ òtítọ́ láì bínú; iná ìbínú kì í ṣe oògùn àrùn. (Ọ̀sá Ọ̀kànràn speaks truth without fury; the fire of wrath is never an antidote for illness: Calm moral conviction carries greater authority than violent rage.)",
            "A kì í fi orí kọ lu idà; ọ̀rọ̀ sùúrù ló ń pa iná ẹ̀sùn. (One does not strike the blade with one's bare forehead; patient speech quenches the flames of accusation: Measured diplomacy neutralizes provocation.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Barnes, Sandra T. (1997). Africa's Ogun: Old World and New; Bascom, William (1969). Ifa Divination."
    },
    "ODU_160_Ọ̀sá_Ògúndá": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Gúndá, governing the safety of ironworkers, safe clearing of sacred forests, and technological reconciliation. 19th-Century Era: Consulted by blacksmith guilds manufacturing defense armaments for frontline garrisons. Contemporary/Diaspora: Preserved in Lucumí as Osa Kuleya / Osa Ogunda, safeguarding against industrial and vehicular accidents.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (spirit, wind) and Ògúndá (iron, technological force). Demonstrates that technological and metallurgical power must always acknowledge ecological and spiritual boundaries; hacking through nature without ritual respect invites self-destruction.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/I/I on the right and I/I/I/II on the left. The Babaláwo strikes the center of Ọpọ́n Ifá with an iron-tipped Ìrọ́kẹ́. Involves Ewé Pèrègún, roasted yam, palm oil, iron filings, and a rooster to Ògún.",
        "social_and_ritual_context": "Divined before clearing dense virgin forests, building industrial factories, undergoing hazardous surgeries, or handling dangerous machinery.",
        "proverbs_and_oral_traditions": [
            "Ògún gbẹ́ idà, Ọ̀sá gbé afẹ́fẹ́ lé e lẹ́yìn; agbára tí ó gbọ́n kì í ṣìnà. (Ògún forged the blade, and Ọ̀sá backed it with the wind; strength guided by wisdom never loses its path: True technical mastery requires spiritual mindfulness.)",
            "Irin kì í ja igbó láì l'ọ́wọ́ alágbẹ̀dẹ; ọ̀wọ̀ la fi ń kọ́ ọ̀làjú. (Iron does not tame the jungle without the blacksmith's craft; reverence is what builds civilization: Constructive labor demands disciplined respect.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Williams, Denis (1974). Icon and Image."
    },
    "ODU_161_Ọ̀sá_Ìká": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Ká, governing the unraveling of malicious conspiracies, overcoming witchcraft traps, and spiritual liberation. 19th-Century Era: Invoked during wartime sieges to escape hostile encirclement. Contemporary/Diaspora: Maintained in Afro-Cuban Ifá as Osa Ka, delivering initiates from malicious legal entrapments.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (flight, astral wind) and Ìká (restraint, the coil of the serpent, snare). Teaches that the insidious traps of the wicked are bypassed not through brute resistance, but through spiritual elevation, vigilance, and superior moral character.",
        "material_and_craftsmanship": "Marked upon Ìyẹ̀rosùn as II/I/I/I on right and II/I/II/II on left. The Ìrọ́kẹ́ taps the eastern quadrant to dissolve bindings. Involves Ewé Ègé, Ewé Arújẹ, white pigeon, and a severed raffia cord symbolizing release.",
        "social_and_ritual_context": "Cast when someone is targeted by conspirators, framed by false witnesses, or trapped in toxic environments.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá fo kọjá àwọ̀n Ìká; ẹyẹ tí ó mọ̀fẹ́ kì í jẹ́ kí okùn mú un. (Ọ̀sá flew over the net of Ìká; the wise bird never allows the snare to entangle it: Spiritual vigilance and swift intuition outmaneuver malice.)",
            "A kì í fi ọwọ́ mú ejò kí a má gba oró; awo tí ó gbọ́n ń sá fún kòtò ibi. (One does not handle a viper with bare hands and avoid its venom; the prudent initiate flees the pit of wickedness: Avoiding dangerous associations preserves life.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Epega, A.A. & Neimark, P. (1995). The Sacred Ifa Oracle."
    },
    "ODU_162_Ọ̀sá_Òtúúrúpọ̀n": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Túúrúpọ̀n, governing pediatric resilience, maternal protection against nocturnal infant fevers, and lineage continuity. 19th-Century Era: Relied upon by midwives protecting displaced families during regional conflicts. Contemporary/Diaspora: Retained in Lucumí Ifá as Osa Trupon, celebrated for infant health rites.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (the mysterious wind) and Òtúúrúpọ̀n (carrying children upon the back, maternal nurture). Teaches that maternal vigilance is the spiritual shield of civilization; protecting the vulnerable from nocturnal terrors guarantees the future of the commonwealth.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/I/I on right and II/II/I/II on left. The Ìrọ́kẹ́ taps the central hearth (`Àárín Ọpọ́n`). Prepared with Ewé Ọ̀já-Ọmọ, Ewé Àbáwẹ̀, cold maize gruel (Ẹ̀kọ), shea butter, and snail broth.",
        "social_and_ritual_context": "Divined for pregnant women, pediatric health recovery, and households protecting children from spiritual disturbances.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá pọ̀n ọmọ mọ́ra, ó ti ẹnu-ọ̀nà àrùn; ọmọ lúwàbí kì í kú ní kékeré. (Ọ̀sá strapped the infant to the back and barred the door against illness; the child of destiny shall not perish in youth: Maternal devotion and ancestral medicine safeguard life.)",
            "Ẹrù ọmọ kì í pa ìyá; ìfẹ́ inú ló ń gbé iran tó ń bọ̀ ga. (The burden of an infant never breaks the mother; deep love is what elevates the rising generation: Sacrificial care builds the future.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Fadipe, N.A. (1970). The Sociology of the Yoruba."
    },
    "ODU_163_Ọ̀sá_Òtúá": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Túá or Ọ̀sá-Wọ̀rìkú, governing international diplomacy, treaties of non-aggression, and religious tolerance. 19th-Century Era: Consulted during peace negotiations between Ekitiparapo and Oyo forces. Contemporary/Diaspora: Preserved in Lucumí Ifá as Osa Tura, celebrated for prayers that disperse spiritual darkness.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (spirit wind) and Òtúá (prayer, release, divine light). Teaches that genuine peace and spiritual freedom arrive when prayers are offered with a clean heart and covenants are honored across borders.",
        "material_and_craftsmanship": "Marked upon Ìyẹ̀rosùn as II/I/I/I on right and I/II/I/I on left. The Babaláwo chants holding a white horse-tail whisk (Ìrùkẹ̀rẹ̀). Involves Ewé Ẹfun, Ewé Tètè-Àgbalagba, honey, white dove, and white chalk (Ẹfun).",
        "social_and_ritual_context": "Cast during peace treaty ratifications, resolving corporate disputes, and dedicating new sanctuaries.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá tú àdúrà sílẹ̀, ìmọ́lẹ̀ gba orí ayé; ẹni tí ó ba fẹ́ àlàáfíà kì í rí ogun. (Ọ̀sá poured forth prayer, and divine light covered the earth; he who genuinely seeks peace never faces war: Sincere spiritual devotion commands universal harmony.)",
            "Àdúrà tí a fi ọkàn mímọ́ gbà kì í ṣubú sílẹ̀; Ọlọ́run ń gbèjà olódodo. (The prayer offered with a pure conscience never falls flat; the Supreme Being defends the righteous: Moral integrity brings divine deliverance.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Law, Robin (1977). The Oyo Empire."
    },
    "ODU_164_Ọ̀sá_Ìrẹtẹ̀": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Rẹtẹ̀ or Ọ̀sá-Ọ̀lọ́mọ, governing bodily cleansing, the excision of spiritual impurities, and victory over infectious skin diseases. 19th-Century Era: Consulted during epidemic quarantines in military encampments. Contemporary/Diaspora: Maintained in Lucumí as Osa Rete, presiding over therapeutic baths.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (clearing wind) and Ìrẹtẹ̀ (trampling down disease, surgical incision). Demonstrates that moral and physical corruption must be confronted directly and excised cleanly without sentimental compromise.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/I/I on right and I/I/II/I on left. The Babaláwo uses an ivory Ìrọ́kẹ́ to demarcate the quadrant of health. Involves Ewé Ìrẹtẹ̀, Ewé Ṣaworo, sulfur-and-chalk bath, and shea butter.",
        "social_and_ritual_context": "Cast for individuals suffering from chronic dermatological or viral conditions, and for community sanitation purifications.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá tẹ àrùn mọ́lẹ̀, ó fi ara dídára wọlé; ìmọ́tótó ni aṣọ àwọn olóye. (Ọ̀sá trampled disease underfoot and entered with radiant health; cleanliness is the vestment of the wise: Physical and spiritual hygiene preserves human vigor.)",
            "Bí a kò bá bẹ́ ibi tí ó wọ́ dànù, a kì í rí ibi tútù simi. (Unless one lops off the crooked branch, the tree finds no refreshing shade: Decisive removal of vice guarantees communal peace.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_165_Ọ̀sá_Ọ̀ṣẹ́": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Ṣẹ́, the conduit of Ọ̀ṣun's sweetness, artistic inspiration, and joyous matrimonial celebration. 19th-Century Era: Consulted during royal weddings and palace arts festivals. Contemporary/Diaspora: Revered in Afro-Cuban Ocha-Ifá as Osa She, commanding victory through sweetness and creative radiance.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (astral wind) and Ọ̀ṣẹ́ (sweetness, beauty, Ọ̀ṣun). Teaches that the turbulence of life is overcome not through stubborn conflict, but through beauty, generosity, honeyed speech, and joyous community celebration.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/I/I on right and I/II/I/II on left. The Ìrọ́kẹ́ touches the southern border invoking Ọ̀ṣun. Prepared with Ewé Ọ̀ṣun, wild honey, cast bronze bell, yellow silk, and river water.",
        "social_and_ritual_context": "Divined for artists, poets, brides, and traders seeking sweet resolution to contentious legal and personal disputes.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá bu oyin sí afẹ́fẹ́, ó sọ ìbànújẹ́ di orin ayọ̀; ọ̀rọ̀ dídùn ni ń yọ ejò nínú ihò. (Ọ̀sá poured honey upon the wind and turned grief into joyful song; pleasant speech is what coaxes the serpent from its hole: Gracious words overcome hostility.)",
            "Omi Ọ̀ṣun kì í gbẹ kí ẹja má rí ibi lúwẹ̀ẹ́; ore-ọ̀fẹ́ Ọlọ́run kì í kùnà. (The river of Ọ̀ṣun never dries up so that the fish lack room to swim; the benevolent grace of the Almighty never falters: Abundance flows to the generous soul.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Badejo, Diedre L. (1996). Ọ̀ṣun Ṣèègèsí; Bascom, William (1969). Ifa Divination."
    },
    "ODU_166_Ọ̀sá_Òfún": {
        "historical_timeline": "Classical Antiquity: Codified as Ọ̀sá-Fún, the triumphant completion of the Ọ̀sá cycle, embodying Obàtálá's white cloth covenant and elder transcendence. 19th-Century Era: Consulted when veteran high priests retired into contemplative seclusion. Contemporary/Diaspora: Preserved in Lucumí Ifá as Osa Fun, commanding absolute moral cleanliness.",
        "etymology_and_philosophy": "Conjunction of Ọ̀sá (spirit wind) and Òfún (white chalk, primal creation, senior authority). Teaches that the culmination of all spiritual trials is the calm, stainless whiteness of elder character (Ìwà-tútù), where wrath dissolves into peace.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/I/I on right and II/I/II/I on left. The Babaláwo marks the center with white chalk (Ẹfun). Involves pure white cloth, shea butter, cold spring water, and a white pigeon to Obàtálá.",
        "social_and_ritual_context": "Cast for paramount elders, high judges, and spiritual leaders assuming custodial governance over sacred institutions.",
        "proverbs_and_oral_traditions": [
            "Ọ̀sá wọ aṣọ funfun, ó fi ìwà tútù tẹ ìjì mọ́lẹ̀; a kì í fi ẹ̀gbin kùn aṣọ Obàtálá. (Ọ̀sá donned the white cloth and calmed the tempest through gentle character; one never defiles the vestment of Obàtálá: Stainless integrity outlives all stormy trials.)",
            "Àgbà tí ó ní sùúrù ló ń jẹ adé ọlá; ìrẹ̀lẹ̀ ni ìyá gbogbo ìwà rere. (The elder who masters patience inherits the crown of majesty; humility is the mother of all virtues: Patient wisdom brings enduring dignity.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_167_Ìká_Ogbè": {
        "historical_timeline": "Classical Antiquity: Codified at Ilé-Ifẹ̀ as Ìká-Gbèmí or Ìká-Ogbè, inaugurating the Ìká cycle by breaking the cords of wickedness through the solar dawn of Ogbè. 19th-Century Era: Consulted before liberating captives during regional skirmishes. Contemporary/Diaspora: Celebrated in Lucumí as Ika Bemi, delivering initiates from witchcraft snares.",
        "etymology_and_philosophy": "Conjunction of Ìká (II/I/II/II: restraint, the coil of the serpent, binding cord) on the right and Ogbè (I/I/I/I: solar light, opening highway) on the left of Ọpọ́n Ifá. Dialectically represents the victory of solar righteousness over covert entrapment, declaring that no knot can withstand the light of truth.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/II on right and I/I/I/I on left. The Ìrọ́kẹ́ Ifá strikes the top of Ọpọ́n Ifá invoking Ogbè's radiant light. Involves Ewé Tètè, Ewé Gbégbé, white rooster, and a cut twine cord.",
        "social_and_ritual_context": "Cast when someone is wrongly indicted, framed in fraudulent legal contracts, or entangled in malicious plots.",
        "proverbs_and_oral_traditions": [
            "Ìká gbè mí, Ogbè la ojú ọ̀nà; okùn tí a fi de olódodo yóò já sí wẹ́wẹ́. (Ìká supported me, and Ogbè opened the highway; the cord used to bind the righteous shall snap into fragments: Divine illumination shatters the snares of the wicked.)",
            "Bí ilẹ̀ bá mọ́, olè a gbọ́n; ìmọ́lẹ̀ òtítọ́ ló ń lé òkùnkùn ẹ̀tàn sá. (When dawn breaks, the thief scatters; the light of truth chases away the darkness of deception: Uncompromising transparency overcomes deceit.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Barnes, Sandra T. (1997). Africa's Ogun."
    },
    "ODU_168_Ìká_Ọ̀yẹ̀kú": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Yẹ̀kú, governing the unbinding of ancestral death curses, neutralising lethal poison, and spiritual containment. 19th-Century Era: Consulted during epidemics to shield families from mortality. Contemporary/Diaspora: Maintained in Lucumí Ifá as Ika Yeku, presiding over rites against untimely demise.",
        "etymology_and_philosophy": "Conjunction of Ìká (binding cord) and Ọ̀yẹ̀kú (darkness, mortality, ancestral veil). Teaches that the knot of death is undone when the living offer reverence and sacrifice to ancestors, transforming impending tragedy into long life.",
        "material_and_craftsmanship": "Inscribed as II/I/II/II on right and II/II/II/II on left on Ọpọ́n Ifá. The Babaláwo marks the board with dark camwood and chalk. Involves Ewé Òdúndún, Ewé Rinrin, black cloth, he-goat, and cold water poured upon ancestral stones.",
        "social_and_ritual_context": "Cast when ominous portents indicate premature death or generational mortality patterns in a lineage.",
        "proverbs_and_oral_traditions": [
            "Ìká yẹ̀ ikú lórí awo; a kì í fi okùn ọ̀rọ̀ de ẹni tí Ọlọ́run ti dá sí. (Ìká deflected death from the initiate; one does not bind the soul that the Almighty has spared: Timely sacrifice and ancestral alignment preserve life.)",
            "Ẹni tí ó ba gbọ́ ikilọ̀ kì í bá ogun kọjú; ìṣọ́ra ni bàbá àlàáfíà. (He who heeds sacred warnings never collides with catastrophe; vigilant foresight is the father of peace: Prudence averts destruction.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_169_Ìká_Ìwòrì": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Wòrì or Ìká-Fẹ́lẹ́jẹ̀, governing clairvoyant detection of covert sabotage, unmasking hypocrites, and forensic investigations. 19th-Century Era: Consulted by military scouts detecting ambushes. Contemporary/Diaspora: Retained in Cuba as Ika Fefe, revealing hidden plots.",
        "etymology_and_philosophy": "Conjunction of Ìká (restraint, concealment) and Ìwòrì (deep spiritual clairvoyance). Teaches that covert treachery cannot survive the piercing scrutiny of spiritual insight; the truth hidden in darkness is laid bare by disciplined inquiry.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/II on right and II/I/I/II on left. The Ìrọ́kẹ́ taps the western edge of Ọpọ́n Ifá. Prepared with Ewé Ìyàyà, Ewé Iná, ram offering, and clear spring water used to wash the initiate's eyes.",
        "social_and_ritual_context": "Divined during forensic trials, detecting theft within royal households, and exposing secret conspiracies.",
        "proverbs_and_oral_traditions": [
            "Ìká wò inú ọ̀rọ̀, ó rí gbongbo ètàn; ojú awo kì í fò lórí òtítọ́. (Ìká gazed into the matter and uncovered the root of deceit; the eye of the initiate never overlooks the truth: Penetrating insight exposes hidden sabotage.)",
            "A kì í fi ojú lásán wo awo; òye inú ló ń tú àwọn ọ̀tá ká. (One does not behold the mysteries with superficial eyes; inner discernment scatters conspirators: Spiritual clarity shatters deceit.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Drewal, H.J. & Pemberton, J. (1989). Yoruba."
    },
    "ODU_170_Ìká_Òdí": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Dí, governing the protective barrier around the hearth, reproductive integrity, and legal defense of estates. 19th-Century Era: Consulted before fortifying township walls against invading cavalry. Contemporary/Diaspora: Preserved in Lucumí Ifá as Ika Di, sealing homes against spiritual intrusion.",
        "etymology_and_philosophy": "Conjunction of Ìká (containment) and Òdí (protective wall, womb). Demonstrates that power without defensive containment leaks away; safeguarding family autonomy requires firm moral and physical boundaries.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/II/II on right and II/I/I/I on left. The Ìrọ́kẹ́ strikes the perimeter rim (`Etí Ọpọ́n`). Prepared with Ewé Gbégbé, fresh palm fronds (Mọ̀rìwò), iron spikes, and rooster offering deposited at compound thresholds.",
        "social_and_ritual_context": "Cast when establishing new homesteads, defending property titles against encroachers, and protecting pregnant women.",
        "proverbs_and_oral_traditions": [
            "Ìká dí ẹnu-ọ̀nà fún ibi; odi tí Ifá mọ kì í wó láé. (Ìká sealed the portal against malevolence; the fortress that Ifá constructs never collapses: Sound boundaries guarantee generational stability.)",
            "Bí ilé bá l'álàáfíà, ìta kò lè mú un; ìfọwọ́sowọ́pọ̀ ni àbò ìdílé. (If the household possesses concord, outside hostility cannot prevail; mutual cooperation is the shield of the lineage: Domestic solidarity resists all assaults.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_171_Ìká_Ìrosùn": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Rosùn or Ìká-Kosùn, governing lineage honor, unbinding generational family curses, and consecrating ancestral blood. 19th-Century Era: Consulted during royal chieftaincy reconciliation councils. Contemporary/Diaspora: Maintained in Cuba as Ika Roso, commanding respect for ancestral heritage.",
        "etymology_and_philosophy": "Conjunction of Ìká (restraint, binding) and Ìrosùn (camwood, ancestral bloodline). Teaches that the ties of blood must not become instruments of oppression; camwood purification restores mutual affection and lineage dignity.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/II on right and I/I/II/II on left. The Ìrọ́kẹ́ Ifá touches scarlet Osùn powder before sounding the wood. Involves Osùn paste, Ewé Àkòko, rooster, and palm oil poured on ancestral stones.",
        "social_and_ritual_context": "Cast during bitter inheritance disputes among siblings, family health reconciliation, and removing ancestral curses.",
        "proverbs_and_oral_traditions": [
            "Ìká wẹ ẹ̀jẹ̀ ìjà nù pẹ̀lú osùn; ará kì í jẹ ará rẹ̀ ní yán-anyàn. (Ìká cleansed the blood of discord with sacred camwood; kin must never devour their own brethren: Family reconciliation preserves the ancestral house.)",
            "Ẹ̀jẹ̀ kì í ṣe nǹkan tí a fi ń ta tẹ́tẹ́; ìṣọ̀kan ilé ni orísun agbára. (Bloodline is not a token to gamble away; domestic unity is the fountain of fortitude: Kinship honor demands loyalty.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Fadipe, N.A. (1970). The Sociology of the Yoruba."
    },
    "ODU_172_Ìká_Ọ̀wọ́nrín": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Wọ́nrín, governing the swift dispersion of legal conspiracies, sudden reversal of slander, and victory over adversaries. 19th-Century Era: Consulted by commanders anticipating unexpected tactical maneuvers. Contemporary/Diaspora: Preserved in Lucumí as Ika Juani.",
        "etymology_and_philosophy": "Conjunction of Ìká (snare) and Ọ̀wọ́nrín (whirlwind, sudden change). Demonstrates that the storm of public opinion can be reversed through swift, decisive action and absolute adherence to truth; the wind scatters the traps of liars.",
        "material_and_craftsmanship": "Inscribed on Ọpọ́n Ifá as II/I/II/II on right and II/II/I/I on left. The Babaláwo waves a broom over Ìyẹ̀rosùn. Involves Ewé Ọlọ́jọ̀bọ́, Ewé Àjídèwe, rooster, and small broom symbolizing sweeping away slander.",
        "social_and_ritual_context": "Cast during severe public defamation, court battles, and sudden financial or social turbulence.",
        "proverbs_and_oral_traditions": [
            "Afẹ́fẹ́ Ìká fẹ́ ẹ̀tàn dànù bí eruku; irọ́ ní ń sáré, òtítọ́ yóò lé e bá. (The gale of Ìká blew deceit away like dust; falsehood may sprint ahead, but truth shall overtake it: Righteous integrity outlasts all rumors.)",
            "Ìjì líle kì í gbé igi tí gbongbo rẹ̀ jinlẹ̀; olódodo dúró ṣinṣin nínú ìdánwò. (A ferocious storm never uproots the deeply anchored tree; the righteous statesman stands firm under trial: Unshakable moral conviction prevails.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Barnes, Sandra T. (1997). Africa's Ogun."
    },
    "ODU_173_Ìká_Ọ̀bàrà": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Bàrà, governing commercial rectitude, honoring contracts, and the coronation of honest wealth. 19th-Century Era: Consulted by treasury guilds auditing tax revenues in imperial Ọ̀yọ́. Contemporary/Diaspora: Maintained in Cuba as Ika Bara, celebrating legitimate trade wealth.",
        "etymology_and_philosophy": "Conjunction of Ìká (restraint, law) and Ọ̀bàrà (wealth, nobility, eloquence). Proves that wealth acquired through fraudulent schemes inevitably entangles the lineage in ruin, while wealth bound by law and honesty endures for generations.",
        "material_and_craftsmanship": "Marked upon Ìyẹ̀rosùn as II/I/II/II on right and I/II/II/II on left. The Ìrọ́kẹ́ strikes the northern quadrant of abundance. Prepared with Ewé Ajé, Ewé Tètè, pigeon, honey, and sixteen consecrated cowries.",
        "social_and_ritual_context": "Divined for merchants, bankers, accountants, and public trustees managing communal resources.",
        "proverbs_and_oral_traditions": [
            "Ìká dábò bo ọrọ̀ pẹ̀lú òtítọ́; èrè tí kò mọ́ kì í gbé awo ga. (Ìká protected wealth with honesty; tainted profit never elevates the initiate: Lawful commerce guarantees enduring honor.)",
            "Ọrọ̀ tí a fi ẹ̀tàn kó jọ kò ní gbongbo; bí afẹ́fẹ́ bá kọjá, a gbálẹ̀ mọ́ ọn. (Wealth amassed through deceit has no roots; when the storm passes, it sweeps the courtyard bare: Fraudulent gains evaporate quickly.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Falola, Toyin (1984). The Political Economy of a Pre-colonial African State."
    },
    "ODU_174_Ìká_Ọ̀kànràn": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Kànràn, governing courageous testimony in judicial assemblies, breaking perjury, and divine retribution against corrupt officials. 19th-Century Era: Consulted during judicial ordeals at royal courts. Contemporary/Diaspora: Preserved in Lucumí as Ika Kana, commanding uncompromising truth.",
        "etymology_and_philosophy": "Conjunction of Ìká (entanglement, binding) and Ọ̀kànràn (voice of conscience, thunder). Teaches that the knot of injustice is severed when an upright witness speaks the unvarnished truth without fear of human retaliation.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/II/II on right and II/II/II/I on left. The Babaláwo strikes the board firmly with an ivory Ìrọ́kẹ́. Involves Ewé Ọ́kìkà, Ewé Aragba, ram offering to Ṣàngó, and kola nuts.",
        "social_and_ritual_context": "Cast during high court arbitrations, exposing institutional corruption, and delivering innocent victims from perjury.",
        "proverbs_and_oral_traditions": [
            "Ìká kànràn sọ òtítọ́ níwájú ọba; ahọ́n tí kì í purọ́ kì í bẹ̀rù idà. (Ìká Ọ̀kànràn spoke the truth before the king; the tongue that never lies harbors no fear of the blade: Fearless honesty commands universal respect.)",
            "Bí a bá ń ja fún ẹ̀tọ́, a kì í fẹsẹ̀ fà sẹ́yìn; Ọlọ́run ló ń gbèjà olódodo. (When fighting for justice, one does not retreat; the Almighty defends the upright: Courageous truth conquers corruption.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Barnes, Sandra T. (1997). Africa's Ogun."
    },
    "ODU_175_Ìká_Ògúndá": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Gúndá, the charter of iron precision, surgical extraction of tumors, and severing treacherous cords. 19th-Century Era: Consulted by warrior armorers forging specialized combat machetes. Contemporary/Diaspora: Retained in Lucumí Ifá as Ika Ogunda.",
        "etymology_and_philosophy": "Conjunction of Ìká (the binding knot) and Ògúndá (Ògún's iron blade, cutting road). Demonstrates that when entanglements become toxic and paralyzing, decisive surgical action is required to sever the knot and restore freedom.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/II on right and I/I/I/II on left. The Babaláwo marks the line with a forged miniature iron blade. Prepared with Ewé Pèrègún, palm oil, roasted yam, iron slag, and a rooster to Ògún.",
        "social_and_ritual_context": "Divined before major surgical operations, severing toxic business partnerships, and defending territories against bandits.",
        "proverbs_and_oral_traditions": [
            "Ògún mú idà gé okùn Ìká; irin kì í bẹ̀rù kókó tí ó le. (Ògún drew the blade and severed the cord of Ìká; forged iron harbors no fear of the stubborn knot: Decisive courage overcomes paralyzing obstacles.)",
            "A kì í fi ọ̀bẹ ṣe eré ọmọdé; agbára tí ó bá tọ́ ló ń là ọ̀nà ọlá. (One does not treat the blade as child's play; righteous power is what opens the highway of majesty: Force must be guided by wisdom.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Williams, Denis (1974). Icon and Image."
    },
    "ODU_176_Ìká_Ọ̀sá": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Sá, governing spiritual liberation from nocturnal envy, escaping hostile sorcery, and pacifying the Mothers. 19th-Century Era: Consulted by diplomats fleeing besieged citadels to establish new settlements. Contemporary/Diaspora: Preserved in Cuba as Ika Sa.",
        "etymology_and_philosophy": "Conjunction of Ìká (restraint, the trap) and Ọ̀sá (flight, astral wind). Teaches that when malicious forces lay in wait, wisdom does not engage in futile confrontation; strategic retreat and spiritual flight preserve destiny for future triumph.",
        "material_and_craftsmanship": "Inscribed on Ọpọ́n Ifá as II/I/II/II on right and II/I/I/I on left. The Ìrọ́kẹ́ sounds the central impluvium. Prepared with Ewé Ọ̀dúndún, Ewé Tètè-tútù, shea butter, white chalk, and cold water.",
        "social_and_ritual_context": "Cast during acute social friction, domestic strife, and escaping toxic partnerships without legal entanglements.",
        "proverbs_and_oral_traditions": [
            "Ìká sá kúrò nínú ewu, ó rí òmìnira gbà; ẹni tó gbọ́n kì í dúró de ọ̀fà ọ̀tá. (Ìká fled from peril and received liberty; the sage does not wait idly for the enemy's arrow: Strategic retreat preserves life.)",
            "A kì í fi orí kọ lu àpáta; sùúrù ló ń mú awo kọjá afẹ́fẹ́ líle. (One does not shatter one's forehead against the boulder; patience guides the initiate past ferocious winds: Prudence outlasts adversity.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Drewal, H.J. (1992). Gelede."
    },
    "ODU_177_Ìká_Òtúúrúpọ̀n": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Túúrúpọ̀n, governing parental vigilance, guarding children against hidden domestic dangers, and pediatric care. 19th-Century Era: Consulted by clan matrons maintaining refuge nurseries during warfare. Contemporary/Diaspora: Retained in Lucumí as Ika Batrupon.",
        "etymology_and_philosophy": "Conjunction of Ìká (vigilant restraint) and Òtúúrúpọ̀n (maternal care, carrying infants). Demonstrates that protective discipline is an act of supreme love; setting boundaries around youth prevents them from stepping into perilous traps.",
        "material_and_craftsmanship": "Inscribed on Ìyẹ̀rosùn as II/I/II/II on right and II/II/I/II on left. The Ìrọ́kẹ́ taps the southern quadrants of lineage health. Prepared with Ewé Ọ̀já-Ọmọ, Ewé Àbáwẹ̀, cold maize gruel, shea butter, and snail broth.",
        "social_and_ritual_context": "Cast for parents raising headstrong youths, midwives protecting newborn deliveries, and pediatric recoveries.",
        "proverbs_and_oral_traditions": [
            "Ìká fi ìfẹ́ di ọmọ mọ́ra; ọ̀pá ìtọ́sọ́nà kì í pa ọmọ lúwàbí. (Ìká bound the child close with love; the guiding rod never slays a noble child: Loving discipline secures righteous character.)",
            "A kì í fi ọmọdé sílẹ̀ nínú ewu; àwọn ọmọ wẹẹrẹ ni ọjọ́ ọ̀la ìlú. (One does not abandon children in peril; the youth are the future of the commonwealth: Parental vigilance builds the nation.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Fadipe, N.A. (1970). The Sociology of the Yoruba."
    },
    "ODU_178_Ìká_Òtúá": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Túá or Ìká-Alákọ̀kọ̀, governing emancipation from debt bondage, divine release from captivity, and sacred covenants. 19th-Century Era: Consulted during ransoming of wartime captives. Contemporary/Diaspora: Preserved in Lucumí Ifá as Ika Tura.",
        "etymology_and_philosophy": "Conjunction of Ìká (restraint, imprisonment) and Òtúá (prayer, light, release). Teaches that the deepest spiritual and physical bonds are unloosened when the individual turns to sincere prayer, covenant fidelity, and truthful restitution.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/II/II on right and I/II/I/I on left. The Babaláwo waves a white horse-tail whisk. Involves Ewé Ẹfun, Ewé Tètè-Àgbalagba, honey, white dove, and white chalk (Ẹfun).",
        "social_and_ritual_context": "Cast when seeking liberation from debt, unbinding wrongful oaths, and prayers for personal freedom.",
        "proverbs_and_oral_traditions": [
            "Ìká tú okùn ìdè, ó fi òmìnira wọlé; àdúrà olódodo kì í kùnà. (Ìká untied the cord of bondage and entered with freedom; the prayer of the righteous never fails: Sincere prayer breaks all shackles.)",
            "A kì í fi ogun wá àlàáfíà; àdéhùn mímọ́ ló ń mú ìlú gbilẹ̀. (One does not seek peace through reckless war; sacred covenants cause the commonwealth to thrive: Covenant fidelity brings liberty.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Bascom, William (1969). Ifa Divination; Law, Robin (1977). The Oyo Empire."
    },
    "ODU_179_Ìká_Ìrẹtẹ̀": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Rẹtẹ̀, governing medical ethics, public health quarantine, and trampling parasitic disease. 19th-Century Era: Consulted by herbalists sanitizing municipal wells. Contemporary/Diaspora: Maintained in Lucumí Ifá as Ika Rete.",
        "etymology_and_philosophy": "Conjunction of Ìká (containment, boundary) and Ìrẹtẹ̀ (trampling down disease, surgical cleansing). Demonstrates that containing outbreaks requires strict quarantine discipline and swift therapeutic action; hygiene is a sacred moral duty.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn as II/I/II/II on right and I/I/II/I on left. The Ìrọ́kẹ́ sounds the eastern quadrant. Prepared with Ewé Ìrẹtẹ̀, Ewé Ṣaworo, sulfur bath, and cold shea butter ointment.",
        "social_and_ritual_context": "Cast during community health emergencies, treating persistent infections, and enforcing quarantine protocols.",
        "proverbs_and_oral_traditions": [
            "Ìká tẹ àrùn mọ́lẹ̀, ó fi ìlera kún ilé; ìmọ́tótó ni aṣọ àwọn olóye. (Ìká trampled disease underfoot and filled the house with health; cleanliness is the vestment of the wise: Public hygiene preserves the community.)",
            "Bí a kò bá dí ẹnu kòtò, àrùn yóò wọlé; ìṣọ́ra ni ààbò ẹ̀mí. (Unless one seals the mouth of the pit, disease enters; cautious sanitation preserves life: Preventive discipline saves lives.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Verger, Pierre (1995). Ewé."
    },
    "ODU_180_Ìká_Ọ̀ṣẹ́": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Ṣẹ́, governing the sweetening of bitter disputes, matrimonial reconciliation, and artistic victory over malice. 19th-Century Era: Consulted by royal envoys resolving border disputes. Contemporary/Diaspora: Celebrated in Cuba as Ika She, unlocking financial joy.",
        "etymology_and_philosophy": "Conjunction of Ìká (bitterness, knot) and Ọ̀ṣẹ́ (victory through sweetness, Ọ̀ṣun). Teaches that the tightest knots of resentment are dissolved not with harsher force, but with the softening sweetness of patience, love, and artistic grace.",
        "material_and_craftsmanship": "Inscribed upon Ọpọ́n Ifá as II/I/II/II on right and I/II/I/II on left. The Ìrọ́kẹ́ strokes Ìyẹ̀rosùn gently while invoking Ọ̀ṣun. Prepared with Ewé Ọ̀ṣun, wild honey, cast bronze bell, and yellow cloth.",
        "social_and_ritual_context": "Cast for couples experiencing marital discord, artists seeking inspiration, and traders resolving commercial disputes.",
        "proverbs_and_oral_traditions": [
            "Ìká bu oyin sí kókó ìjà, ó sọ gbogbo rẹ̀ di adùn; ọ̀rọ̀ dídùn ni ń tú kókó líle. (Ìká poured honey upon the knot of dispute and transformed it into sweetness; pleasant words loosen the tightest knot: Gracious love dissolves all bitterness.)",
            "Odò Ọ̀ṣun kì í gbẹ kí ẹja má rí ibi lúwẹ̀ẹ́; ore-ọ̀fẹ́ Ọlọ́run kì í kùnà. (The river of Ọ̀ṣun never dries up so that the fish lack room to swim; the benevolent grace of the Almighty never fails: Abundance crowns the peacemaker.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1976). Ifá: An Exposition of Ifá Literary Corpus; Badejo, Diedre L. (1996). Ọ̀ṣun Ṣèègèsí; Bascom, William (1969). Ifa Divination."
    },
    "ODU_181_Ìká_Òfún": {
        "historical_timeline": "Classical Antiquity: Codified as Ìká-Fún, concluding the Ìká cycle with Obàtálá's white cloth purity and complete absolution from false guilt. 19th-Century Era: Consulted by senior judges rendering final verdicts. Contemporary/Diaspora: Preserved in Lucumí Ifá as Ika Fun, commanding absolute moral cleanliness.",
        "etymology_and_philosophy": "Conjunction of Ìká (restraint, the trap) and Òfún (white chalk, primal purity, Obàtálá). Proves that all malicious snares collapse before stainless moral character; the white cloth of purity cannot be bound by the ropes of wickedness.",
        "material_and_craftsmanship": "Inscribed on Ọpọ́n Ifá as II/I/II/II on right and II/I/II/I on left. The Babaláwo marks the center with white chalk (Ẹfun). Involves pure white cloth, shea butter, cold spring water, and a white pigeon to Obàtálá.",
        "social_and_ritual_context": "Cast for individuals falsely accused of crimes, elder judges assuming high office, and purifying ancestral shrines.",
        "proverbs_and_oral_traditions": [
            "Ìká wọ aṣọ funfun, ó já gbogbo okùn ẹ̀tàn; a kì í fi ẹ̀gbin kùn aṣọ Obàtálá. (Ìká donned the white garment and severed all cords of deceit; one never soils the vestment of Obàtálá: Stainless integrity shatters all false accusations.)",
            "Àgbà tí ó ní sùúrù ló ń jẹ adé ọlá; ìrẹ̀lẹ̀ ni ìyá gbogbo ìwà rere. (The elder who masters patience inherits the crown of majesty; humility is the mother of all virtues: Purity of conscience is life's ultimate shield.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Lawal, Babatunde (1996). The Gelede Spectacle."
    },
    "ODU_182_Òtúúrúpọ̀n_Ogbè": {
        "historical_timeline": "Classical Antiquity: Codified at Ilé-Ifẹ̀ as Òtúúrúpọ̀n-Bè or Òtúúrúpọ̀n-Ogbè, inaugurating the Òtúúrúpọ̀n cycle with the radiant dawn of generational health and maternal vitality. 19th-Century Era: Consulted during royal birth festivals and crowning ceremonies to divine lineage longevity. Contemporary/Diaspora: Celebrated in Lucumí and Candomblé Ketu as Otrupon Bekonwao, governing pediatric health and maternal blessing.",
        "etymology_and_philosophy": "Conjunction of Òtúúrúpọ̀n (II/II/I/II: maternal care, carrying children upon the back, lineage nurturing) on the right and Ogbè (I/I/I/I: pristine solar light, expanding highway) on the left of Ọpọ́n Ifá. Dialectically represents the dawn of flourishing pediatric life and ancestral blessing, declaring that human civilization reaches its zenith when children are nurtured in light, love, and moral instruction.",
        "material_and_craftsmanship": "Inscribed upon Ìyẹ̀rosùn across Ọpọ́n Ifá as II/II/I/II on the right and I/I/I/I on the left. The Babaláwo strikes the eastern gate of Ogbè using a carved wooden Ìrọ́kẹ́ adorned with the figure of a mother holding an infant. Prepared with Ewé Ọ̀já-Ọmọ, Ewé Àbáwẹ̀, cold maize gruel (Ẹ̀kọ), shea butter, snail broth, and two white doves.",
        "social_and_ritual_context": "Cast during naming ceremonies (Ìsomọ́lórúkọ), pediatric health recoveries, and consecrating matrimonial unions for fruitful progeny.",
        "proverbs_and_oral_traditions": [
            "Òtúúrúpọ̀n gbé ọmọ pọ̀n, Ogbè la ojú ọ̀nà; ọmọ lúwàbí ni adé ilé. (Òtúúrúpọ̀n strapped the child to the back, and Ogbè opened the highway; a virtuous child is the crown of the household: Nurturing youth in light and wisdom elevates the entire lineage.)",
            "Ẹrù ọmọ kì í wu ìyá lórí; pẹ̀lú ìfẹ́ la fi ń kọ́ ọmọdé ní ọ̀nà ìyè. (The burden of an infant never wearies the mother; it is with tender love that we guide the child along the path of life: Sacrificial maternal care secures the commonwealth.)"
        ],
        "provenance_and_citations": "Abímbọ́lá, Wándé (1975). Sixteen Great Poems of Ifá; Bascom, William (1969). Ifa Divination; Fadipe, N.A. (1970). The Sociology of the Yoruba; Lawal, Babatunde (1996). The Gelede Spectacle."
    }
}

def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: GENERATING BATCH 11 DATA VAULT (INDICES 158-182)")
    print("=" * 80)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(BATCH_11_DATA, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully wrote {len(BATCH_11_DATA)} records to {OUTPUT_FILE}")
    print("=" * 80)

if __name__ == "__main__":
    main()
