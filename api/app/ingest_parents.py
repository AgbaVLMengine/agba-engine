#!/usr/bin/env python3
# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: COMPLETE SOVEREIGN ONTOLOGY INGESTION (81 RECORDS)
# ==============================================================================
# Ingests 73 Sovereign Parents + 8 Ìpínlẹ̀ Geopolitical States across:
#   - web/src/data/yoruba_master_corpus.json
#   - agba_web/src/data/yoruba_master_corpus.json
#   - api/data/yoruba_corpus_1007_NORMALIZED.json
#   - agba_enterprise_api/data/yoruba_corpus_1007_NORMALIZED.json
# ==============================================================================

import json
from pathlib import Path
import sys

PARENTS_DATA = [
  {
    "id": "Adé",
    "title": "Adé",
    "category": "Monarchy, Royal Regalia & Governance",
    "aliases": [
      "ade",
      "ade are",
      "ade oba",
      "ade ooni",
      "adenla",
      "beaded crown",
      "coronet",
      "crown",
      "crowns",
      "royal crown"
    ],
    "description": "The sacred beaded crown representing supreme royal authority and divine ancestral lineage of consecrated Yorùbá monarchs (Ọba Aládé). Strictly confined to crowns surmounted by the mystical crane (Okin) and shielded by a beaded fringe veil (Ojuwo).",
    "sub_variants": [
      "Adé Ààrẹ",
      "Adé Ọlọ́kun",
      "Adé Oríṣà",
      "Adé Ìlẹ̀kẹ̀",
      "Adé Aládé",
      "Adé Babaláwo"
    ],
    "historical_timeline": "Dating to classical Ilé-Ifẹ̀ antiquity and Odùduwà's sixteen crowned sons.",
    "etymology_and_philosophy": "Adé originates from 'dé' (to arrive, cover, crown). Consecrates the monarch as Aláṣẹ Èkejì Òrìṣà.",
    "material_and_craftsmanship": "Thousands of microscopic glass seed beads, carnelian beads, stiff palm-rib armature, and ancestral herbal medicine inside the crest.",
    "social_and_ritual_context": "Worn only on state pageantry and sacred festivals; the beaded veil protects mortals from the sacred metaphysical intensity of the king's eyes.",
    "proverbs_and_oral_traditions": [
      "Adé a pẹ́ lórí, bàtà a pẹ́ lẹ́sẹ̀.",
      "Ọba tó jẹ ti ìlú tutù, orúkọ rẹ̀ kò ní parẹ́."
    ],
    "diaspora_connections": "Preserved in Afro-Cuban Santería/Lucumí coronal crowns of Ọbàtálá and Brazilian Candomblé Ketu adés.",
    "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́, Ìjẹ̀bú, Òndó, Òwò.",
    "media_production_notes": "Cinematic visual must show authentic beaded fringe falling below the nose; never expose the king's bare eyes when crowned with Adéńlá."
  },
  {
    "id": "Ọba",
    "title": "Ọba",
    "category": "Monarchy, Royal Regalia & Governance",
    "aliases": [
      "alaafin",
      "alase",
      "awujale",
      "kabiyesi",
      "king",
      "kings",
      "monarch",
      "oba",
      "oba alade",
      "olubadan",
      "ooni"
    ],
    "description": "The divine paramount monarch and institutional cornerstone of Yorùbá civilization, ruling with the title Kábíyèsí (He whose authority cannot be questioned) and Aláṣẹ Èkejì Òrìṣà.",
    "sub_variants": [
      "Ọọ̀ni of Ifẹ̀",
      "Aláàfin of Ọ̀yọ́",
      "Awùjalẹ̀ of Ìjẹ̀bú",
      "Ọwá Obòkun",
      "Olubadan of Ìbàdàn",
      "Aláké of Ẹ̀gbá",
      "Ọba Ẹ̀dẹ"
    ],
    "historical_timeline": "Institutionalized with the founding of classical Ilé-Ifẹ̀ and the expansion of the Old Ọ̀yọ́ Empire.",
    "etymology_and_philosophy": "Embodied as sovereign steward of the realm; balancing physical executive governance with spiritual covenant.",
    "material_and_craftsmanship": "Adorned in embroidered Agbádá, beaded footwear, coral necklaces, and royal flywhisks.",
    "social_and_ritual_context": "Select by the council of kingmakers (Oyomesi, Afọbaaje) following divine consultation through the Ifá oracle.",
    "proverbs_and_oral_traditions": [
      "Kábíyèsí, Aláṣẹ Èkejì Òrìṣà.",
      "Ọba kì í sọ̀rọ̀ lásán."
    ],
    "diaspora_connections": "Survives as sacred royal invocations in Cuban Cabildo de San Agustín and Oyotunji African Village.",
    "geographical_origin": "Pan-Yorùbá royal capitals.",
    "media_production_notes": "Portray with supreme courtly dignity; attendants must prostrate (Dọ̀bálẹ̀) or kneel (Kúnlẹ̀)."
  },
  {
    "id": "Àmì_Ọlá",
    "title": "Àmì Ọlá",
    "category": "Monarchy, Royal Regalia & Governance",
    "aliases": [
      "ami ola",
      "apoti oba",
      "bata ileke",
      "ewu ileke",
      "flywhisk",
      "irukere",
      "kakaki",
      "opa ase",
      "regalia",
      "royal insignia",
      "royal regalia",
      "scepter",
      "throne"
    ],
    "description": "The sovereign non-crown royal regalia, ceremonial staves, beaded apparel, and state insignia carried by Yorùbá monarchs and palace dignitaries.",
    "sub_variants": [
      "Ìrukẹ̀rẹ̀",
      "Ọ̀pá Àṣẹ",
      "Àpótí Ọba",
      "Bàtà Ìlèkè",
      "Èwù Ìlèkè",
      "Kàkàkí",
      "Ọ̀pá Ọ̀rànmíyàn"
    ],
    "historical_timeline": "Formally codified in the classical Ifẹ̀ and Ọ̀yọ́ court protocols over eight centuries.",
    "etymology_and_philosophy": "Àmì (Sign/Emblem) + Ọlá (Honor/Nobility). Physical signs that channel royal prestige and executive command.",
    "material_and_craftsmanship": "Beaded leatherwork, carved elephant ivory, cast brass, horse-tail hair, and hardwood carving.",
    "social_and_ritual_context": "Used in royal processions, state durbars, judicial verdicts, and annual palace festivals.",
    "proverbs_and_oral_traditions": [
      "Ìrukẹ̀rẹ̀ kì í bẹ́nu bẹ́yìn.",
      "Ọ̀pá àṣẹ Ọba ló ń palẹ̀ mọ́."
    ],
    "diaspora_connections": "Widely present in Cuban and Brazilian Orisha altars (Iruke of Ọya and Ọbàtálá).",
    "geographical_origin": "All Yorùbá royal kingdoms.",
    "media_production_notes": "Never conflate with crowns; Ìrukẹ̀rẹ̀ is held in the hand and waved gracefully."
  },
  {
    "id": "Fìlà",
    "title": "Fìlà",
    "category": "Attire, Textiles & Personal Adornment",
    "aliases": [
      "abeti aja",
      "cap",
      "caps",
      "fila",
      "fila gobi",
      "fila orunmila",
      "headwear",
      "traditional cap",
      "yoruba cap"
    ],
    "description": "The quintessential Yorùbá cloth cap worn by men across civic life, ceremonies, and royal courts, folded directionally to communicate political poise, marital status, or social alignment.",
    "sub_variants": [
      "Fìlà Gọ̀bị́",
      "Fìlà Abetí Ajá",
      "Fìlà Ọ̀ránmíyàn",
      "Fìlà Oníderè",
      "Fìlà Kọ̀gbọ́n",
      "Àkẹ̀tẹ̀"
    ],
    "historical_timeline": "Evolved alongside indigenous strip-loom weaving (Aṣọ-Òkè) across pre-colonial Yorùbá city-states.",
    "etymology_and_philosophy": "Fìlà protects the physical head (Orí Òde) and honors the inner metaphysical consciousness (Orí Inú).",
    "material_and_craftsmanship": "Tailored from hand-loomed Aṣọ-Òfì, damask, or brocade, with precise structural stitching and embroidery.",
    "social_and_ritual_context": "Folding left or right signifies societal status and personal disposition; worn with Agbádá or Bùbá.",
    "proverbs_and_oral_traditions": [
      "Fìlà tó wọ̀ lórí kì í jẹ́ kí ẹ̀tẹ́ dé.",
      "Bí orí bá wà, fìlà kò ní wọ́n."
    ],
    "diaspora_connections": "Worn in African diaspora ceremonies across the Americas as a badge of ancestral African identity.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Must be folded neatly (Gọ̀bị́ or Abetí Ajá ears erect or folded down); never worn backwards or flat."
  },
  {
    "id": "Ìlèkè",
    "title": "Ìlèkè",
    "category": "Attire, Textiles & Personal Adornment",
    "aliases": [
      "bead",
      "beaded",
      "beads",
      "beadwork",
      "coral beads",
      "ileke",
      "iyun",
      "necklace",
      "segi",
      "waist beads"
    ],
    "description": "Sacred and ornamental beads strung into royal necklaces, waist beads, wrists, and anklets, serving as supreme indicators of nobility, fertility, wealth, and spiritual devotion.",
    "sub_variants": [
      "Ìyùn",
      "Sẹ̀gí",
      "Ìlèkè Ìbàdí",
      "Èjìgbà Ìlèkè",
      "Ìlèkè Ọrùn",
      "Ìlèkè Ọwọ́",
      "Ìlèkè Ẹsẹ̀",
      "Ìlèkè Ọ̀pẹ̀tẹ̀"
    ],
    "historical_timeline": "Manufactured in ancient Ilé-Ifẹ̀ glass crucible factories since the 10th-12th century CE.",
    "etymology_and_philosophy": "Ìlèkè represents wealth, divine consecration, and spiritual insulation.",
    "material_and_craftsmanship": "Dichroic fused glass, cylindrical Sẹ̀gí jasper, carnelian Ìyùn, and marine coral beads.",
    "social_and_ritual_context": "Given during rites of passage, bridal dowries, chieftaincy installations, and royal coronations.",
    "proverbs_and_oral_traditions": [
      "Ìlèkè Ọba kì í dọ́dàbà.",
      "Ìyùn kì í ṣe ohun àbùkù."
    ],
    "diaspora_connections": "Universal in Santería collares (elekes) and Candomblé contas representing specific Orishas.",
    "geographical_origin": "Ilé-Ifẹ̀, Ìjẹ̀bú, Òwò.",
    "media_production_notes": "Distinguish royal coral from glass seed beads; ensure correct colors for specific deities."
  },
  {
    "id": "Aṣọ",
    "title": "Aṣọ",
    "category": "Attire, Textiles & Personal Adornment",
    "aliases": [
      "agbada",
      "aso",
      "aso oke",
      "attire",
      "buba",
      "cloth",
      "clothing",
      "dandogo",
      "garment",
      "gele",
      "iro",
      "textile",
      "textiles"
    ],
    "description": "Indigenous hand-loomed textiles, tailored ceremonial garments, and multi-piece prestige dress ensembles defining Yorùbá aesthetic grandeur.",
    "sub_variants": [
      "Agbádá",
      "Dàńdógó",
      "Bùbá",
      "Ìró",
      "Gèlè",
      "Aṣọ-Òkè",
      "Gbáríyẹ̀",
      "Kìjìpá",
      "Pà Kaja",
      "Yẹ̀rị̀"
    ],
    "historical_timeline": "Continuously produced on double-heddle narrow treadle looms and vertical broadlooms for centuries.",
    "etymology_and_philosophy": "Aṣọ expresses civilization, dignity (Ọ̀wọ̀), moral modesty, and social prominence.",
    "material_and_craftsmanship": "Locally grown handspun cotton, wild Anaphe silk (Sányán), indigo dye baths, and metallic threads.",
    "social_and_ritual_context": "Central to civic life, weddings, naming ceremonies, funerals, and courtly pageantry (Aṣọ Ẹbí).",
    "proverbs_and_oral_traditions": [
      "Aṣọ ńlá kọ́ ni ènìyàn ńlá.",
      "Aṣọ tó dára kì í pọ́n lójú agbára."
    ],
    "diaspora_connections": "Preserved in ceremonial Afro-Atlantic liturgical garments worn by priestesses and initiates.",
    "geographical_origin": "Ìsẹ́yìn, Ọ̀yọ́, Ìbàdàn, Òkè-Ògùn, Ìjẹ̀bú.",
    "media_production_notes": "Highlight rich textile textures, Sányán silk luster, and stately flowing drapery."
  },
  {
    "id": "Ilà_Kíkọ",
    "title": "Ilà Kíkọ",
    "category": "Attire, Textiles & Personal Adornment",
    "aliases": [
      "abaja",
      "facial marks",
      "gombo",
      "ila",
      "ila kiko",
      "kekeyoruba",
      "lineage marks",
      "pele",
      "scarification",
      "tribal marks",
      "ture"
    ],
    "description": "Traditional facial incisions and lineage scarification marks denoting genealogical clan origins, royal descent, municipal citizenship, and personal beauty.",
    "sub_variants": [
      "Pẹ́lẹ́",
      "Àbàjà",
      "Gọ̀mbọ̀",
      "Túré",
      "Kẹ́kẹ́",
      "Màndà",
      "Pẹ́lẹ́ Ìjẹ̀bú",
      "Pẹ́lẹ́ Ìfẹ̀"
    ],
    "historical_timeline": "Practiced for over a millennium to encode citizenship, lineage identification, and royal patents.",
    "etymology_and_philosophy": "Ilà (Line/Boundary) + Kíkọ (Writing/Inscribing). The human face as an ancestral parchment.",
    "material_and_craftsmanship": "Inscribed in infancy by specialized surgical guilds (Olóòlà) using sterile iron blades and medicinal soot.",
    "social_and_ritual_context": "Immediate identification of lineage during war and peace; honors ancestral lineages and patron deities.",
    "proverbs_and_oral_traditions": [
      "Kò sí ẹni tó ń kọ ilà tó ń kọ ọmọ tirẹ̀ sílẹ̀.",
      "Ilà tó wà lójú kò ṣe é pa rẹ́."
    ],
    "diaspora_connections": "Documented in 18th-19th century transatlantic ship manifests as unmistakable marks of Yorùbá identity.",
    "geographical_origin": "Ọ̀yọ́, Ìbàdàn, Ìjẹ̀bú, Èkìtì, Òndó.",
    "media_production_notes": "Render marks precisely according to historical kingdom (e.g. Ọ̀yọ́ Àbàjà vs Ìjẹ̀bú Pẹ́lẹ́)."
  },
  {
    "id": "Ìrun",
    "title": "Ìrun",
    "category": "Attire, Textiles & Personal Adornment",
    "aliases": [
      "coiffure",
      "hair",
      "hair braiding",
      "hair dressing",
      "hairstyle",
      "hairstyles",
      "irun",
      "korobo",
      "onidiri",
      "suku"
    ],
    "description": "Sacred cranial sculpting, hair braiding, and coiffures created by master hairstyling guilds (Onídìrí) reflecting marital status, royal association, and devotion.",
    "sub_variants": [
      "Ṣùkú",
      "Kọ̀rọ̀bọ́",
      "Òjòńpẹ̀tẹ́",
      "Ìpàkọ́ Ẹlẹ́dẹ̀",
      "Àdàbà",
      "Àfùrù",
      "Ìrun Dídì",
      "Onígbàjámọ̀"
    ],
    "historical_timeline": "Documented in classical terracotta sculptures of ancient Ifẹ̀ depicting elaborate woven coiffures.",
    "etymology_and_philosophy": "The head (Orí) houses destiny; crowning it with beautiful hair honors the inner deity.",
    "material_and_craftsmanship": "Hand-braided black wool, thread (Òwú), palm-leaf ribs, shea butter, and fragrant herbal pomades.",
    "social_and_ritual_context": "Styling varies for queens (Ṣùkú Ọba), brides (Ẹ̀kún Ìyàwó), and deity priestesses.",
    "proverbs_and_oral_traditions": [
      "Ṣùkú lẹlẹ́wà ń dì, ẹlẹ́yinjú ẹgẹ́.",
      "Orí rere ló ń gbádùn ìrun tó dára."
    ],
    "diaspora_connections": "Influenced African-American and Caribbean protective braiding patterns and crown aesthetics.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Depict intricate geometric braiding and elevated crowns with lustrous black finish."
  },
  {
    "id": "Ogun",
    "title": "Ogun",
    "category": "Military Traditions, Weaponry & Defense",
    "aliases": [
      "armed conflict",
      "battle",
      "battles",
      "interstate war",
      "military",
      "military campaign",
      "ogun",
      "war",
      "war expedition",
      "warfare"
    ],
    "description": "The canonical Yorùbá concept and historical institution of armed conflict, interstate warfare, military mobilization, strategic campaigns, and peacetime peace pacts. (Distinct from Ògún the divinity of iron).",
    "sub_variants": [
      "Ogun Ìbílẹ̀",
      "Ogun Kírìjì",
      "Ogun Ọ̀yọ́ àti Ìbàdàn",
      "Ogun Jalumi",
      "Ogun Ọ̀wọ́",
      "Ẹgbẹ́ Ológun",
      "Ààbò-Ogun"
    ],
    "historical_timeline": "Pre-colonial warfare from 16th-century imperial cavalry campaigns to the 19th-century Kírìjì War.",
    "etymology_and_philosophy": "Mid-Mid tone pronunciation (O-gun). Governed by strict codes of martial honor and warrior conventions.",
    "material_and_craftsmanship": "Logistics, iron weaponry, dane guns, cavalry horses, protective war shirts (Ayé / Gbẹ̀bú), and fortifications.",
    "social_and_ritual_context": "Led by the Balógun and regulated by councils of warriors; sealed with ceremonial peace treaties (Àdéhùn).",
    "proverbs_and_oral_traditions": [
      "Ogun kì í jẹ́ kí á mọ ọmọ Ọba.",
      "Bí ogun bá ń bọ̀, ológun ló ń tẹ̀lé."
    ],
    "diaspora_connections": "Narratives of the 19th-century Yorùbá wars directly shaped the demographics and cultural resilience of Cuba and Brazil.",
    "geographical_origin": "Ọ̀yọ́-Ilé, Ìbàdàn, Ìjàyè, Èkìtì-Parapọ̀, Abẹ́òkúta.",
    "media_production_notes": "Portray historic battle maneuvers, disciplined battle formations, and authentic weaponry without anachronisms."
  },
  {
    "id": "Balógun",
    "title": "Balógun",
    "category": "Military Traditions, Weaponry & Defense",
    "aliases": [
      "army general",
      "balogun",
      "commander",
      "field marshal",
      "general",
      "military chief",
      "war general",
      "warlord"
    ],
    "description": "The supreme military general, field marshal, and commander-in-chief of a Yorùbá kingdom's army (Bàbá-ní-Ogun: Father/Leader in War).",
    "sub_variants": [
      "Ààrẹ Ọ̀nà Kakañfò",
      "Ọ̀tún Balógun",
      "Òsì Balógun",
      "Balógun Ìbàdàn",
      "Bàbá Ìkòyí",
      "Seriki"
    ],
    "historical_timeline": "Prominent throughout imperial Ọ̀yọ́ history and reaching zenith in 19th-century warrior city-states like Ìbàdàn.",
    "etymology_and_philosophy": "Contracted from 'Bàbá-ní-ogun' (Father/Lord in warfare). Demands uncompromising courage, strategic genius, and poise.",
    "material_and_craftsmanship": "Rides battle horses, bears ceremonial battle swords (Idà), and wears reinforced war charms (Àkọ́ṣẹ́).",
    "social_and_ritual_context": "Ranks directly beneath or alongside paramount chiefs; holds veto power over military expeditions.",
    "proverbs_and_oral_traditions": [
      "Balógun kì í sá fún ogun.",
      "Ọ̀tún Balógun, Òsì Balógun, kò sí ẹni tó ń gba ojú ogun lọ́wọ́ wọn."
    ],
    "diaspora_connections": "Honored in martial salute chants in Afro-Cuban and Trinidadian Orisha communities.",
    "geographical_origin": "Ìbàdàn, Ọ̀yọ́, Ìjàyè, Abẹ́òkúta.",
    "media_production_notes": "Show commanding military presence, war horse, retinue of drummers, and distinctive battle attire."
  },
  {
    "id": "Idà",
    "title": "Idà",
    "category": "Military Traditions, Weaponry & Defense",
    "aliases": [
      "battle blade",
      "blade",
      "blades",
      "broadsword",
      "ida",
      "iron sword",
      "scimitar",
      "sword",
      "swords"
    ],
    "description": "The forged iron sword, battle blade, and royal state scimitar consecrated under Ògún for martial defense and palace heraldry.",
    "sub_variants": [
      "Idà Agẹmọ",
      "Idà Ọba",
      "Idà Ìṣẹ́gun",
      "Tanmogayi",
      "Idà Ògún",
      "Kùmọ̀",
      "Ọ̀bẹ-Awo"
    ],
    "historical_timeline": "Smelted and forged in Yorùbá smithies since classical antiquity; found in archeological Ifẹ̀ and Ọ̀yọ́ deposits.",
    "etymology_and_philosophy": "Idà embodies the decisive cutting edge of truth, justice, defense, and sovereign authority.",
    "material_and_craftsmanship": "High-carbon forged iron, brass hilt, leather scabbard (Àkò Idà) embossed with geometric motifs.",
    "social_and_ritual_context": "Borne before the king by royal sword-bearers (Àkòdà); consecrated with libations of palm oil and animal offerings.",
    "proverbs_and_oral_traditions": [
      "Idà kì í pa olóri tirẹ̀.",
      "Idà Ògún kì í sùn sínú àkò lásán."
    ],
    "diaspora_connections": "Prominent in Cuban Santería representations of Ògún and Ọya's double-edged sword.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Authentic Yorùbá swords have distinctive hilt designs and leather sheaths; do not use European fencing swords."
  },
  {
    "id": "Ọfà",
    "title": "Ọfà",
    "category": "Military Traditions, Weaponry & Defense",
    "aliases": [
      "archery",
      "arrow",
      "arrows",
      "bow",
      "bow and arrow",
      "bows",
      "ofa",
      "projectile weapon",
      "quiver"
    ],
    "description": "The traditional archery bow, poison-tipped arrows, and handcrafted leather quiver used for military skirmishing, hunting defense, and consecrated to Ọ̀sọ́ọ̀sì.",
    "sub_variants": [
      "Ọfà Ọdẹ",
      "Apó Ọfà",
      "Ọfà Òṣọ́ọ̀sì",
      "Oró Ọfà"
    ],
    "historical_timeline": "Ancient projectile technology used since prehistoric hunter-gatherer eras and formalized in imperial infantry lines.",
    "etymology_and_philosophy": "Represents swift justice, focused intent, and the hunter's single-minded concentration (Àròjinlẹ̀).",
    "material_and_craftsmanship": "Supple hardwood bowstave, sinew or fiber bowstring, reed shafts, iron arrowheads coated in botanical poison (Oró).",
    "social_and_ritual_context": "Carried by guild archers and consecrated to the divine tracker Ọ̀sọ́ọ̀sì.",
    "proverbs_and_oral_traditions": [
      "Ọfà tó já lẹ́nu apó kì í padà síbẹ̀ lásán.",
      "Bí ọfà bá ta kọjá, kì í yípadà."
    ],
    "diaspora_connections": "Universal attribute of Oshosi in Cuban Lucumí and Brazilian Candomblé (Ofá bow emblem).",
    "geographical_origin": "Ọ̀yọ́, Èkìtì, Òkè-Ògùn, Ìbàrìbá borderlands.",
    "media_production_notes": "Include the cylindrical embroidered leather quiver (Apó Ọfà) slung diagonally across the chest."
  },
  {
    "id": "Ọ̀kọ̀",
    "title": "Ọ̀kọ̀",
    "category": "Military Traditions, Weaponry & Defense",
    "aliases": [
      "cavalry lance",
      "javelin",
      "lance",
      "oko",
      "pike",
      "spear",
      "spears",
      "thrusting spear"
    ],
    "description": "The forged iron thrusting spear, throwing javelin, and heavy cavalry lance employed by Yorùbá imperial horsemen and big-game hunters.",
    "sub_variants": [
      "Ọ̀kọ̀ Ẹlẹ́ṣin",
      "Ọ̀kọ̀ Ògún",
      "Ọ̀kọ̀ Ọdẹ",
      "Ọ̀kọ̀ Ìṣẹ́gun"
    ],
    "historical_timeline": "Pivotal weapon of the Ọ̀yọ́ imperial cavalry that controlled the savannah corridors in the 17th-18th centuries.",
    "etymology_and_philosophy": "Emblem of direct, unyielding forward thrust and decisive warrior engagement.",
    "material_and_craftsmanship": "Tempered forged iron spearhead, hardwood shaft, counterbalance iron butt-spike, and grip windings.",
    "social_and_ritual_context": "Carried by horsemen and royal bodyguards; also placed in Ògún shrines as an altar standard.",
    "proverbs_and_oral_traditions": [
      "Ọ̀kọ̀ kì í bá ẹni tí kò jẹ́ ọ̀tá jà.",
      "Ẹni tó fi ọ̀kọ̀ gun erin kò ní pẹ́ jẹ ẹ́."
    ],
    "diaspora_connections": "Found in Candomblé Ketu Ogum ceremonies as sacred metal staves.",
    "geographical_origin": "Ọ̀yọ́-Ilé, Ìlọrin, Kétu, Ẹ̀gbádò.",
    "media_production_notes": "Cavalry lances were long and balanced for horsemen; hunting spears were shorter and sturdier."
  },
  {
    "id": "Àpáta",
    "title": "Àpáta",
    "category": "Military Traditions, Weaponry & Defense",
    "aliases": [
      "apata",
      "armor",
      "buckler",
      "defense shield",
      "shield",
      "shields",
      "war shield"
    ],
    "description": "The defensive war shield and body buckler handcrafted from cured elephant hide, buffalo leather, or carved hardwood to deflect arrows and blade strikes.",
    "sub_variants": [
      "Àpáta Awọ",
      "Àpáta Igi",
      "Àpáta Ológun"
    ],
    "historical_timeline": "Used across classical Yorùbá and Sudanese border warfare prior to firearm proliferation.",
    "etymology_and_philosophy": "Symbol of communal defense, invulnerability, and royal shelter (Ààbò).",
    "material_and_craftsmanship": "Multiple layers of cured elephant or bush-cow hide stretched over an elliptical frame with iron arm-straps.",
    "social_and_ritual_context": "Borne by front-line shield-bearers defending infantry archers and royalty.",
    "proverbs_and_oral_traditions": [
      "Àpáta ńlá tó ń gba ọfà lọ́wọ́ ológun.",
      "Kò sí ohun tí àpáta kì í gbà lójú ogun."
    ],
    "diaspora_connections": "Appears symbolically in Afro-Cuban visual art of warrior orishas.",
    "geographical_origin": "Ọ̀yọ́-Ilé, Ìbàdàn, Ìjẹ̀bú.",
    "media_production_notes": "Textured thick animal hide finish with bold geometric tooling; oval or circular profile."
  },
  {
    "id": "Oko",
    "title": "Oko",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "agbe",
      "agriculture",
      "barn",
      "cultivation",
      "farm",
      "farmer",
      "farming",
      "farmland",
      "field",
      "granary",
      "harvest",
      "oko",
      "plantation"
    ],
    "description": "The sacred farmland, agrarian ecosystems, crop cultivation, farming settlements, elevated yam barns (Àká), and seasonal harvests forming the foundation of Yorùbá economic sustenance.",
    "sub_variants": [
      "Oko Èbá",
      "Oko Egàn",
      "Àbà",
      "Àká",
      "Ebè",
      "Aparò",
      "Ìkórè",
      "Ìfálẹ̀",
      "Ẹgbẹ́ Àgbẹ̀",
      "Kìjìpá"
    ],
    "historical_timeline": "Cultivated continuously for millennia; yam and oil palm civilization documented across West African archeology.",
    "etymology_and_philosophy": "Iṣẹ́ àgbẹ̀ ni iṣẹ́ ilẹ̀ wa (Farming is the foundational vocation of our land). Establishes harmony with Mother Earth (Ilẹ̀).",
    "material_and_craftsmanship": "Farmland plots, raised soil heaps (Ebè), furrowed ridges (Aparò), wooden granaries (Àká), and farm cottages (Àbà).",
    "social_and_ritual_context": "Regulated by agrarian cooperatives (Àárò & Òwe) and celebrated during the New Yam Festival (Ọdún Ìjeṣu).",
    "proverbs_and_oral_traditions": [
      "Iṣẹ́ àgbẹ̀ ni iṣẹ́ ilẹ̀ wa, ẹni kò ṣiṣẹ́ á jalè.",
      "Oko kì í jẹ́ kí àgbẹ̀ kú sínú ebi."
    ],
    "diaspora_connections": "Agricultural knowledge of yams, okra, and plantains was transplanted directly to Caribbean and Brazilian plantations.",
    "geographical_origin": "Pan-Yorùbá fertile farming belts.",
    "media_production_notes": "Distinguish between near-home farms (Oko Èbá) and deep forest farms (Oko Egàn); portray communal farm labor."
  },
  {
    "id": "Ọkọ́",
    "title": "Ọkọ́",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "cultivation tool",
      "farming hoe",
      "hoe",
      "hoe handle",
      "hoes",
      "oko agbe",
      "ridging hoe",
      "tilling hoe",
      "weeding hoe"
    ],
    "description": "The quintessential forged iron tilling implement mounted onto an ergonomically carved curved wooden handle (Ẹkù Ọkọ́), used for mound-shaping, ridging, and weeding.",
    "sub_variants": [
      "Ọkọ́ Ìtulẹ̀",
      "Ọkọ́ Pẹ́pẹ́",
      "Ọkọ́ Ìgbalẹ̀",
      "Ẹkù Ọkọ́"
    ],
    "historical_timeline": "Evolved from stone tilling picks to socketed iron blades forged in Ògún smithies over two millennia.",
    "etymology_and_philosophy": "Ọkọ́ penetrates the crust of the earth to unlock fertility, food, and life.",
    "material_and_craftsmanship": "Smelted high-carbon iron socketed or tanged blade, carved curved hardwood handle (Ẹkù).",
    "social_and_ritual_context": "The farmer's daily companion; honored in seasonal rites and smithy invocations.",
    "proverbs_and_oral_traditions": [
      "Ọkọ́ kì í sin olóko dé ilé.",
      "Ọkọ́ tó mọ ilẹ̀ ń yí i padà sí oúnjẹ."
    ],
    "diaspora_connections": "Replicated across Afro-descendant agricultural communities in the American South and Caribbean.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Handle is curved hardwood fitted snugly into the iron socket; distinct sizes for mound-heaping vs light weeding."
  },
  {
    "id": "Àdá",
    "title": "Àdá",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "ada",
      "bush knife",
      "clearing knife",
      "cutlass",
      "harvesting cutlass",
      "machete",
      "machete blade",
      "machetes",
      "pruning cutlass"
    ],
    "description": "The indispensable forged iron blade used for clearing bush, trail-blazing through virgin forest, pruning cocoa and palm trees, and harvesting staple crops.",
    "sub_variants": [
      "Àdá Ìbílẹ̀",
      "Àdá Ológeṣẹ́",
      "Àdá Pẹ́pẹ́",
      "Àdá Fáàfà",
      "Àgọ́gọ́ Oko",
      "Ìgbà"
    ],
    "historical_timeline": "Primary tool of Yorùbá agrarian expansion and jungle trailblazing throughout history.",
    "etymology_and_philosophy": "Consecrated under Ògún as the instrument that turns impenetrable wilderness into human habitation.",
    "material_and_craftsmanship": "Forged iron blade with balanced weight distribution, curved or hooked tip, and pinned wooden grip.",
    "social_and_ritual_context": "Blessed before clearing the virgin forest; essential tool in every rural and urban household.",
    "proverbs_and_oral_traditions": [
      "Àdá kì í mọ orí olóko.",
      "Àdá tó mú ní ń ṣá igbó dọ̀rọ̀."
    ],
    "diaspora_connections": "The universal machete of Afro-Cuban and Haitian rural laborers, consecrated to Ogou.",
    "geographical_origin": "Pan-Yorùbá agrarian towns.",
    "media_production_notes": "Show authentic curved blade geometry (such as the hooked Ológeṣẹ́) and hand-finished hardwood handle."
  },
  {
    "id": "Ọdẹ",
    "title": "Ọdẹ",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "forest ranger",
      "game tracking",
      "guild hunting",
      "hunter",
      "hunters",
      "hunting",
      "hunting guild",
      "ode",
      "trapping"
    ],
    "description": "The prestigious guild of professional hunters, forest scouts, frontier guards, and wildlife trackers who preserve esoteric knowledge and compose chant poetry (Ìjálá Ọdẹ).",
    "sub_variants": [
      "Ọdẹ Ìbílẹ̀",
      "Ẹgbẹ́ Ọdẹ",
      "Ìpáde Ọdẹ",
      "Ìjálá Ọdẹ",
      "Ìbọn Ọdẹ",
      "Ẹ̀bìtì / Dẹ́kùn",
      "Apó Ọfà"
    ],
    "historical_timeline": "The earliest founders of Yorùbá towns were legendary hunters (Ọdẹ) who located game, water springs, and fertile land.",
    "etymology_and_philosophy": "Patronized by Ògún and Ọ̀sọ́ọ̀sì; requires mastery of nature, animal psychology, and medicinal herbs (Ewé).",
    "material_and_craftsmanship": "Dane guns (Ìbọn Ọdẹ), hunting horns, leather medicine pouches, hunting amulets, and game bags.",
    "social_and_ritual_context": "Hunters guard town gates at night, perform funerary funeral rites for deceased colleagues, and chant Ìjálá.",
    "proverbs_and_oral_traditions": [
      "Ọdẹ tó mọ orí erin kì í sùn.",
      "Ìjálá ń ké, ọdẹ ń gbọ́."
    ],
    "diaspora_connections": "Sacred hunting societies survived in Cuba and Brazil as Cabildos dedicated to Ochosi.",
    "geographical_origin": "Pan-Yorùbá forest kingdoms.",
    "media_production_notes": "Show hunters in deep brown or indigo dyed work clothes hung with horn amulets and flintlock dane guns."
  },
  {
    "id": "Àró",
    "title": "Àró",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "adire",
      "adire cloth",
      "alaro",
      "aro",
      "dye pits",
      "dyeing",
      "dyer",
      "indigo",
      "indigo dyeing",
      "textile dyeing",
      "tie dye"
    ],
    "description": "The venerable women's guild of indigo dye-mistresses (Aláró) operating sunken earthen pits to produce world-renowned indigo-resist textiles (Adirẹ).",
    "sub_variants": [
      "Àró Dídá",
      "Kòtò Àró",
      "Ẹlú",
      "Adirẹ Ẹlẹ́kọ",
      "Adirẹ Alábẹ́rẹ́",
      "Adirẹ Oniko"
    ],
    "historical_timeline": "Practiced for centuries in ancient centers like Ìbàdàn, Abẹ́òkúta, and Òṣogbo.",
    "etymology_and_philosophy": "Àró represents transformation, permanence, and spiritual depth through deep indigo blue.",
    "material_and_craftsmanship": "Fermented wild indigo leaves (Ẹlú), wood-ash lye, monumental sunken clay pits (Kòtò Àró), and cassava starch resist.",
    "social_and_ritual_context": "Controlled exclusively by matriarchal guilds with strict spiritual protocols against pollution of the dye vat.",
    "proverbs_and_oral_traditions": [
      "Kòtò àró kì í gba omi tútù.",
      "Àró dára kò ṣe é pa rẹ́."
    ],
    "diaspora_connections": "Indigo dyeing techniques were brought across the Atlantic, creating indigo industries in the Carolinas and Brazil.",
    "geographical_origin": "Abẹ́òkúta, Ìbàdàn, Òṣogbo.",
    "media_production_notes": "Portray circular sunken clay dye pits with steaming purple-blue indigo foam and cloth hung on drying lines."
  },
  {
    "id": "Ìwunṣọ",
    "title": "Ìwunṣọ",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "aso ofi",
      "horizontal loom",
      "iwunso",
      "loom",
      "strip weaving",
      "vertical loom",
      "weaver",
      "weavers guild",
      "weaving"
    ],
    "description": "The master weavers' guild operating narrow horizontal treadle looms (Ọ̀fì) and upright vertical broadlooms to create prestige hand-woven cloth (Aṣọ-Òkè).",
    "sub_variants": [
      "Ọ̀fì",
      "Ìwunṣọ Obìnrin",
      "Ọkọ̀ Ìwunṣọ",
      "Aṣá Ìwunṣọ",
      "Àkàsọ̀"
    ],
    "historical_timeline": "Centuries of documented production in traditional weaving towns like Ìsẹ́yìn and Ọ̀yọ́.",
    "etymology_and_philosophy": "Ìwun (Weaving) + Aṣọ (Cloth). Weaving symbolizes the cosmic interlacing of destiny and community.",
    "material_and_craftsmanship": "Hardwood loom frames, carved boat shuttles (Ọkọ̀), toothed beater reeds (Aṣá), and foot treadles.",
    "social_and_ritual_context": "Men weave narrow strips on horizontal treadle looms; women weave wide panels on upright stationary looms.",
    "proverbs_and_oral_traditions": [
      "Ọkọ̀ ń lọ, aṣá ń bọ̀, aṣọ ń yọ.",
      "Aláṣọ kì í fẹ́ kí aṣọ rẹ̀ ya."
    ],
    "diaspora_connections": "Strip-loom weaving influenced African-American quilt traditions and Caribbean textiles.",
    "geographical_origin": "Ìsẹ́yìn, Ọ̀yọ́, Ìbàdàn, Òndó.",
    "media_production_notes": "Capture rhythmic mechanical motion of foot treadles, flying shuttle, and rapid clacking of the beater reed."
  },
  {
    "id": "Apẹja",
    "title": "Apẹja",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "apeja",
      "boatman",
      "fish trapping",
      "fisherman",
      "fishermen",
      "fishery",
      "fishing",
      "fishing net",
      "river guild"
    ],
    "description": "The indigenous guild of riverine, lagoon, and coastal fishermen operating carved dugout canoes, woven cast-nets, and conical wicker fish traps.",
    "sub_variants": [
      "Àwọ̀n Apẹja",
      "Ìhà / Àgọ̀ Ẹja",
      "Ọkọ̀ Ojú Omi",
      "Ìwọ̀ Apẹja",
      "Àkérè Apẹja"
    ],
    "historical_timeline": "Thriving riverine commerce along the Niger, Ogun, Osun, and coastal Lagos lagoons for over a thousand years.",
    "etymology_and_philosophy": "Apẹja (He who kills/harvests fish). Consecrated to water divinities (Yemọja, Ọ̀ṣun, Ọlọ́kun).",
    "material_and_craftsmanship": "Hollowed mahogany log canoes, hand-knotted cotton/fiber nets, lead sinkers, and woven cane traps.",
    "social_and_ritual_context": "Fishermen perform river offerings before casting nets and hold night fishing expeditions.",
    "proverbs_and_oral_traditions": [
      "Apẹja kì í bẹ̀rù omi.",
      "Àwọ̀n tó ju sí omi kì í padà bọ̀ lọ́wọ́ òfo."
    ],
    "diaspora_connections": "Yorùbá riverine and coastal traditions influenced Afro-Brazilian fishing guilds in Salvador da Bahia.",
    "geographical_origin": "Èkó (Lagos), Ìjẹ̀bú-Waterside, Badagry, Ọ̀ṣun and Ògùn river valleys.",
    "media_production_notes": "Show dugout wooden canoe gliding on mist-covered river with circular throw-net expanding in mid-air."
  },
  {
    "id": "Ẹ̀mù",
    "title": "Ẹ̀mù",
    "category": "Traditional Trades, Agriculture & Agrarian Guilds",
    "aliases": [
      "brewery",
      "climbing rope",
      "elemu",
      "emu",
      "oguro",
      "palm wine",
      "palm wine tapper",
      "raffia wine",
      "tapping"
    ],
    "description": "The vocation of agile palm wine tappers (Ẹlẹ́mù) harvesting fresh sweet sap from oil palms and raffia palms using reinforced climbing harnesses (Ìgbà).",
    "sub_variants": [
      "Ẹ̀mù Ọ̀pẹ",
      "Oguro",
      "Ìgbà",
      "Àkèrègbè",
      "Ọ̀bẹ Ẹlẹ́mù"
    ],
    "historical_timeline": "Indigenous palm harvesting culture documented since antiquity across the West African rainforest belt.",
    "etymology_and_philosophy": "Palm wine is sacred to Ògún and used in libations; unfermented sweet sap is pure, fermented wine fosters conviviality.",
    "material_and_craftsmanship": "Reinforced palm-fiber climbing harness (Ìgbà), specialized curved tapping knife, and dried calabash bottles.",
    "social_and_ritual_context": "Fresh morning palm wine (Ẹ̀mù Àárọ̀) is consumed at town gatherings and used in ancestral libations.",
    "proverbs_and_oral_traditions": [
      "Ẹ̀mù kì í tan nínú àkèrègbè.",
      "Ẹlẹ́mù kì í dọ́dàbà nígbà tí igi bá ń so omi."
    ],
    "diaspora_connections": "Revered in transatlantic Orisha rites as a prime offering to warriors and ancestors.",
    "geographical_origin": "Èkìtì, Òndó, Ìjẹ̀bú, Ọ̀yọ́ rainforest fringes.",
    "media_production_notes": "Show the tapper suspended high up a palm trunk with the woven Ìgbà belt, checking the tapping gourd."
  },
  {
    "id": "Oníṣègùn",
    "title": "Oníṣègùn",
    "category": "Sacred Botany, Flora & Herbal Medicine",
    "aliases": [
      "adahunse",
      "agbo",
      "healer",
      "herbal doctor",
      "herbalist",
      "onisegun",
      "pharmacopeia",
      "physician",
      "traditional medicine"
    ],
    "description": "The guild of indigenous physicians, medical botanists, and healers operating under Ọ̀sanyìn to diagnose ailments and formulate herbal medicine.",
    "sub_variants": [
      "Egbògi",
      "Àgbo Ìbílẹ̀",
      "Àsèjẹ",
      "Àgbo Tútù",
      "Ọ̀pá Ọ̀sanyìn",
      "Ìkòkò Àgbo"
    ],
    "historical_timeline": "Centuries of empirical botanical observation and pharmacological compounding.",
    "etymology_and_philosophy": "Oní (Owner/Master) + Ṣègùn (Medicine). Illness is seen as physical, psychological, and spiritual disequilibrium.",
    "material_and_craftsmanship": "Decoctions of therapeutic leaves, barks, roots, clay pots (Ìkòkò Àgbo), and carved herbal medicine mortars.",
    "social_and_ritual_context": "Works closely with Ifá diviners; prepares protective and curative tonics for children and mothers.",
    "proverbs_and_oral_traditions": [
      "Kò sí ewé tí kò ní iṣẹ́ tirẹ̀.",
      "Oníṣègùn tó mọ ewé ló ń wo àrùn."
    ],
    "diaspora_connections": "Direct predecessor of Afro-Cuban curanderos, Lucumí herbal doctors, and Brazilian Candomblé folhas masters.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show shelves of medicinal roots, clay pots boiling infusions, and the iconic sixteen-bird iron Ọ̀pá Ọ̀sanyìn staff."
  },
  {
    "id": "Àgbẹ̀dẹ",
    "title": "Àgbẹ̀dẹ",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "agbede",
      "blacksmith",
      "blacksmith guild",
      "forge",
      "iron smith",
      "iron working",
      "metallurgy",
      "smithy"
    ],
    "description": "The sacred blacksmith forge and metallurgical smithy consecrated to Ògún, smelting iron ore and forging tools, weapons, and sacred sculptures.",
    "sub_variants": [
      "Inú Àrọ́",
      "Àwọ̀nwọ́n",
      "Ẹ̀wìrì",
      "Tọ́ǹgù",
      "Àgbẹ̀dẹ-Irin",
      "Alágbede Guild"
    ],
    "historical_timeline": "Iron smelting in Yorùbáland dates back to the 6th century BCE (Nok-related metallurgy and early Ifẹ̀ furnaces).",
    "etymology_and_philosophy": "The forge is a sacred altar of Ògún; oaths sworn on the anvil are inviolable.",
    "material_and_craftsmanship": "Smelted bloomery iron, charcoal furnaces, leather bellows (Ẹ̀wìrì), granite anvils, and forged tongs.",
    "social_and_ritual_context": "Smiths are venerated craftsmen who supply farmers with hoes, hunters with guns, and monarchs with swords.",
    "proverbs_and_oral_traditions": [
      "Àgbẹ̀dẹ kì í rọ irin lásán.",
      "Bí iná bá kú lágbẹ̀dẹ, Ògún á bínú."
    ],
    "diaspora_connections": "Revered in Cuban and Brazilian Ògún rituals where iron anvils and hammers form central altar shrines.",
    "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́, Ìlọrin, Ìjẹ̀bú.",
    "media_production_notes": "Show red-hot glowing iron on the anvil, flying sparks under heavy hammer strikes, and working goatskin bellows."
  },
  {
    "id": "Idẹ",
    "title": "Idẹ",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "brass",
      "brass casting",
      "bronze",
      "bronze casting",
      "cire perdue",
      "ide",
      "ifa metalwork",
      "lost wax"
    ],
    "description": "The sacred metallurgy of brass and bronze casting using the lost-wax technique (Cire Perdue) to produce world-renowned lifelike royal portraits and ritual objects.",
    "sub_variants": [
      "Ẹdan Ògbóni",
      "Orí Idẹ Ifẹ̀",
      "Oṣé Ṣàngó Idẹ",
      "Idẹ Ìlẹ̀kẹ̀",
      "Ère Idẹ"
    ],
    "historical_timeline": "Mastery in 12th-14th century classical Ilé-Ifẹ̀, producing bronzes that astonished international art history.",
    "etymology_and_philosophy": "Brass (Idẹ) never rusts or corrupts; it represents eternity, incorruptibility, and divine kingship.",
    "material_and_craftsmanship": "Beeswax sculpting, fine clay investment molds, alloyed molten copper, tin, and zinc.",
    "social_and_ritual_context": "Commissioned for royal memorials, divine crowns, and the sacred emblems of the Ògbóni society.",
    "proverbs_and_oral_traditions": [
      "Idẹ kì í dẹ́tẹ̀, bàbà kì í pọ́n.",
      "Ẹdan kò ní kùrà."
    ],
    "diaspora_connections": "Influenced sacred brass iconography of Ọ̀ṣun and Ògbóni in Cuba and Brazil.",
    "geographical_origin": "Ilé-Ifẹ̀, Òwò, Ìjẹ̀bú-Òde.",
    "media_production_notes": "Show the lustrous golden patina of classical Ifẹ̀ bronze heads and intricate wax modeling."
  },
  {
    "id": "Amọ̀",
    "title": "Amọ̀",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "amo",
      "ceramic",
      "clay",
      "clay vessel",
      "earthenware",
      "ikoko",
      "pot",
      "pots",
      "potter",
      "pottery"
    ],
    "description": "Women's ceramic guild sculpting sacred earthenware pots, cooking vessels, water storage coolers, and industrial indigo dye vats from natural alluvial clay.",
    "sub_variants": [
      "Ìkòkò",
      "Àgbàbá",
      "Àpè",
      "Kòkò Àró",
      "Aro-Amọ̀",
      "Orù Ẹmu"
    ],
    "historical_timeline": "Continuously practiced since Neolithic times; ceramic pavements and vessels prominent in classical Ifẹ̀ archeology.",
    "etymology_and_philosophy": "Amọ̀ (Alluvial Clay) represents the primal substance from which Ọbàtálá molded human physical bodies.",
    "material_and_craftsmanship": "Sedimentary clay, coil building method, smooth pebble burnishing, and open-pit wood-fire baking.",
    "social_and_ritual_context": "Vessels store water coolly without refrigeration; sacred pots hold consecrated water on Òrìṣà altars.",
    "proverbs_and_oral_traditions": [
      "Amọ̀ tó gbọ́n ló ń di ìkòkò.",
      "Ìkòkò tí kò fọ́ kì í dọ̀wọ́ èrò."
    ],
    "diaspora_connections": "Preserved in Afro-Cuban cazuelas (clay pots) used in Palo and Santería rituals.",
    "geographical_origin": "Ìlorin, Erúwà, Ìbàdàn, Òṣogbo.",
    "media_production_notes": "Show potters coiling clay by hand and burnishing the smooth rounded vessels before bonfire firing."
  },
  {
    "id": "Gbẹ́nàgbẹ́nà",
    "title": "Gbẹ́nàgbẹ́nà",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "carpenter",
      "carved post",
      "carving",
      "gbenagbena",
      "sculptor",
      "wood artisan",
      "woodcarver",
      "woodcarving"
    ],
    "description": "Master sculptors and woodcarvers carving architectural palace veranda posts, masks, divination trays (Ọpọ́n Ifá), stools, and twin figures (Ère Ìbejì).",
    "sub_variants": [
      "Opó Ààfin",
      "Ọpọ́n Ifá",
      "Àpótí Ọba",
      "Ère Ìbejì",
      "Ilẹ̀kùn Ààfin",
      "Ọpọ́n Oúnjẹ"
    ],
    "historical_timeline": "Celebrated across centuries, featuring legendary master artists like Olówè of Iṣẹ̀ and arógunṣebí.",
    "etymology_and_philosophy": "Gbẹ́ (To carve) + Ọ̀nà (Art/Path). Woodcarving releases the spiritual personality latent within sacred hardwoods.",
    "material_and_craftsmanship": "Hardwoods (Irókò, Ọ̀pẹ́pẹ́), curved adzes, gouges, chisels, and natural vegetable dyes.",
    "social_and_ritual_context": "Adorns royal palaces with monumental figurative posts; produces devotional masks and altar sculptures.",
    "proverbs_and_oral_traditions": [
      "Gbẹ́nàgbẹ́nà kì í gbẹ́ igi tí kò dára.",
      "Opó ààfin tó gbẹ́ ń bọ̀wọ̀ fún Ọba."
    ],
    "diaspora_connections": "Directly influenced Yoruba-derived woodcarving styles in Bahia, Cuba, and Surinam.",
    "geographical_origin": "Èkìtì, Òwò, Ọ̀yọ́, Ìjẹ̀bú.",
    "media_production_notes": "Show the rhythmic swinging of the curved hand-adze carving expressive facial features into hardwood."
  },
  {
    "id": "Àwọ̀",
    "title": "Àwọ̀",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "awo",
      "cobbler",
      "hide",
      "hides",
      "leather",
      "leather artisan",
      "leathercraft",
      "leatherwork",
      "tanning"
    ],
    "description": "Traditional tanning, hide treatment, and craftsmanship producing footwear, sword sheaths (Àkò), quivers, horse saddles, and protective bags.",
    "sub_variants": [
      "Bàtà Ìbílẹ̀",
      "Àkò Idà",
      "Apó Ọfà",
      "Àpáta Awọ",
      "Àpò Ọdẹ",
      "Gàárì Ẹṣin"
    ],
    "historical_timeline": "Developed over centuries with livestock tanning centers in Ọ̀yọ́ and trade routes across the savannah.",
    "etymology_and_philosophy": "Hides represent durability, physical defense, and intimate tactile craftsmanship.",
    "material_and_craftsmanship": "Tanned goat, cow, and reptile skins treated with vegetable tannins and stitched with leather thongs.",
    "social_and_ritual_context": "Used in royal court saddles, warrior scabbards, and sacred medicine pouches worn by hunters.",
    "proverbs_and_oral_traditions": [
      "Awọ tó dán ló ń wọ bàtà.",
      "Kò sí ẹran tí kò ní awọ."
    ],
    "diaspora_connections": "Preserved in drumhead tanning (Añá drums in Cuba and Atabaques in Brazil).",
    "geographical_origin": "Ọ̀yọ́, Ìlọrin, Ìṣẹ́yìn.",
    "media_production_notes": "Highlight rich reddish-brown hand-tooled leather with embossed geometric knotwork."
  },
  {
    "id": "Ààfin",
    "title": "Ààfin",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "aafin",
      "court",
      "kings palace",
      "palace",
      "palaces",
      "residence of oba",
      "royal palace"
    ],
    "description": "The expansive residential royal palace of a Yorùbá monarch, encompassing monumental courtyards, sacred impluvia, reception halls (Akódi), and gabled roofs (Kòbì Ààfin).",
    "sub_variants": [
      "Ààfin Ọọ̀ni (Ilé-Ifẹ̀)",
      "Ààfin Aláàfin (Ọ̀yọ́)",
      "Ààfin Awùjalẹ̀ (Ìjẹ̀bú)",
      "Kòbì Ààfin",
      "Akódi",
      "Ọgbà Ààfin"
    ],
    "historical_timeline": "Dating back to classical Ifẹ̀ urbanism, with Ọ̀yọ́-Ilé's ancient palace covering several square miles.",
    "etymology_and_philosophy": "Ààfin represents the civic heart, judicial supreme court, and cosmic sanctuary of the kingdom.",
    "material_and_craftsmanship": "Puddle-mud courtyards, carved Irókò veranda posts (Opó), thatched or zinc roofs, and quartz pebble floors.",
    "social_and_ritual_context": "Houses the monarch, royal wives, palace messengers (Ẹlẹ́kọ̀), and ancestral coronation shrines.",
    "proverbs_and_oral_traditions": [
      "Ààfin Ọba kò ṣe é sun mọ́ lásán.",
      "Bí ààfin Ọba bá jóná, ẹwà ló ń bù sí i."
    ],
    "diaspora_connections": "Concept survives metaphorically in Afro-Cuban Ilé-Osha (House of the Orishas).",
    "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́, Ìjẹ̀bú-Òde, Òwò.",
    "media_production_notes": "Feature vast impluvium courtyards, sweeping gables (Kòbì), and elaborately carved veranda posts."
  },
  {
    "id": "Ilé",
    "title": "Ilé",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "agbo ile",
      "compound",
      "dwelling",
      "home",
      "house",
      "household",
      "ile",
      "living space"
    ],
    "description": "The multi-generational extended family compound (Agbo Ilé) organized around interconnected open-air courtyards housing patrilineal clans.",
    "sub_variants": [
      "Agbo Ilé",
      "Zawo",
      "Òdẹ̀dẹ̀",
      "Ilé Ìtura",
      "Ilé Ìbílẹ̀"
    ],
    "historical_timeline": "Traditional compound architecture evolved over millennia of collective communal living.",
    "etymology_and_philosophy": "Ilé embodies both the physical house and the collective genealogical lineage (Ìdílé).",
    "material_and_craftsmanship": "Laterite clay puddle-mud walls, hardwood roof rafters, palm thatch, and rain-water impluvia.",
    "social_and_ritual_context": "Births, child namings, marriages, and ancestral burials take place within the home compound.",
    "proverbs_and_oral_traditions": [
      "Ilé la ti ń kọ́ ẹ̀ṣọ́ ròde.",
      "Ilé tó gbún, ìdílé ló wà."
    ],
    "diaspora_connections": "Replicated spiritually in the Ilé Asé compound communities of Salvador da Bahia, Brazil.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show continuous rectangular earthen buildings opening into a shared central social courtyard."
  },
  {
    "id": "Ọjà",
    "title": "Ọjà",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "bazaar",
      "market",
      "market square",
      "marketplace",
      "markets",
      "oja",
      "oja oba",
      "trading center"
    ],
    "description": "The central municipal marketplace established directly facing the royal palace (Ọjà Ọba), serving as the economic, social, and communicative heart of Yorùbá towns.",
    "sub_variants": [
      "Ọjà Ọba",
      "Ọjà Alẹ́",
      "Ọjà Ọ̀sán",
      "Ọjà Àkókò",
      "Ọjà Ẹlẹ́kọ̀"
    ],
    "historical_timeline": "Market systems operating on 4-day and 8-day sacred trade cycles date to pre-colonial urban trade networks.",
    "etymology_and_philosophy": "Ayé lọjà, ọ̀run nilé (The world is a marketplace; heaven is our true home).",
    "material_and_craftsmanship": "Open-air thatched stalls, shaded under wide ancestral trees, regulated by trade guild symbols.",
    "social_and_ritual_context": "Administered by the Market Queen (Ìyál'ọ́jà) and trade chiefs (Parakòyí); hub for civic news and festivals.",
    "proverbs_and_oral_traditions": [
      "Ayé lọjà, ọ̀run nilé.",
      "Ọjà kì í kún kí ó má tú."
    ],
    "diaspora_connections": "Yorùbá market women's guild customs laid the foundation for street vendor traditions in Bahia and the Caribbean.",
    "geographical_origin": "Pan-Yorùbá urban centers.",
    "media_production_notes": "Show lively twilight market lanterns (Ọjà Alẹ́), calabashes heaped with food, and colorful textile stalls."
  },
  {
    "id": "Igbó",
    "title": "Igbó",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "forest",
      "forests",
      "grove",
      "igbo",
      "jungle",
      "sacred grove",
      "wilderness",
      "woods"
    ],
    "description": "The natural forest ecosystem, dense tropical wilderness, and sacred groves (Igbó Òrìṣà) set aside for ancestral masquerade secrets and spiritual communion.",
    "sub_variants": [
      "Igbó Òrìṣà",
      "Igbó Igbàlẹ̀",
      "Igbó Olódùmarè",
      "Igbó Egàn",
      "Igbó Ògbóni"
    ],
    "historical_timeline": "Sacred groves like the Òṣun Òṣogbo Sacred Grove are UNESCO World Heritage cultural sanctuaries.",
    "etymology_and_philosophy": "Igbó represents the mysterious realm of nature, spirits, wild flora, and raw metaphysical potency.",
    "material_and_craftsmanship": "Ancient hardwood canopies, meandering river paths, earthen sanctuary clearings, and sacred shrines.",
    "social_and_ritual_context": "Trespassing in sacred groves is strictly forbidden to uninitiated persons; site of annual initiations.",
    "proverbs_and_oral_traditions": [
      "Igbó tó kún kì í ṣe ohun àṣebẹ́lẹ̀.",
      "Ẹni tó mọ igbó ló ń rìn nínú rẹ̀."
    ],
    "diaspora_connections": "Replicated in Cuban Afro-Cuban sacred woods (El Monte) where practitioners gather ritual herbs.",
    "geographical_origin": "Òṣogbo, Ilé-Ifẹ̀, Èkìtì, Òndó rainforests.",
    "media_production_notes": "Dappled sunlight filtering through monumental tree ferns, sacred riverbanks, and secluded carved shrines."
  },
  {
    "id": "Ojúbọ",
    "title": "Ojúbọ",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "altar",
      "altars",
      "ojubo",
      "sacred place",
      "sacred shrine",
      "sanctuary",
      "shrine",
      "shrines"
    ],
    "description": "The consecrated physical shrine, outdoor altar, or temple chamber where offerings, libations, and prayers are presented to divinities and ancestors.",
    "sub_variants": [
      "Ojúbọ Ògún",
      "Ojúbọ Ṣàngó",
      "Ojúbọ Ọ̀ṣun",
      "Ojúbọ Oríṣà-Nlá",
      "Ojúbọ Ẹlẹ́gbára",
      "Ojúbọ Egúngún"
    ],
    "historical_timeline": "Maintained in homes, groves, and town gates since the foundation of Yorùbá religious settlements.",
    "etymology_and_philosophy": "Ojú (Eye/Focal Face) + Ẹbọ (Offering/Sacrifice). The physical portal where humanity covenants with divinity.",
    "material_and_craftsmanship": "Carved stones, terracotta vessels, iron staffs, sacrificial altars anointed with palm oil and camwood.",
    "social_and_ritual_context": "Daily morning prayers (Àkúnlẹ̀kọ̀) and annual festival sacrifices occur at the Ojúbọ.",
    "proverbs_and_oral_traditions": [
      "Ojúbọ kì í gbà omi tútù lásán.",
      "Ẹni tó bọ ojúbọ ló ń rí àṣẹ."
    ],
    "diaspora_connections": "Direct model for the home altars (tronos and panteones) of Cuban Santería and Brazilian Candomblé.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show authentic altar vessels, brass bells, kola nut lobes in water, and consecrated iron implements."
  },
  {
    "id": "Odi",
    "title": "Odi",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "city ramparts",
      "city wall",
      "city walls",
      "defensive walls",
      "fortress",
      "moat",
      "odi",
      "rampart",
      "sungbo eredo"
    ],
    "description": "Monumental defensive earthen ramparts, ditch-and-dyke networks, and perimeter walls built around Yorùbá city-states for military defense.",
    "sub_variants": [
      "Sungbo's Eredo",
      "Odi Ọ̀yọ́-Ilé",
      "Odi Ìbàdàn",
      "Odi Abẹ́òkúta",
      "Odi Ìjẹ̀bú-Òde"
    ],
    "historical_timeline": "Sungbo's Eredo in Ìjẹ̀bú (built c. 1000 CE) is the largest pre-colonial monument in Sub-Saharan Africa.",
    "etymology_and_philosophy": "Odi represents civic sovereignty, community preservation, and strategic territorial integrity.",
    "material_and_craftsmanship": "Massive ditch excavations, stepped earthen embankments up to 20 meters high, and fortified watchtower gates.",
    "social_and_ritual_context": "Guarded by military sentries; gates were locked at sunset and unlocked at dawn.",
    "proverbs_and_oral_traditions": [
      "Odi ńlá kì í sán lábẹ́lẹ̀.",
      "Ìlú tí kò ní odi á di eranko."
    ],
    "diaspora_connections": "Archeological study celebrated globally as evidence of indigenous West African civic engineering.",
    "geographical_origin": "Ìjẹ̀bú, Ọ̀yọ́, Ìbàdàn, Abẹ́òkúta.",
    "media_production_notes": "Show monumental vertical earthen ditch cuts overgrown with moss, towering ramparts, and timber gates."
  },
  {
    "id": "Òkè",
    "title": "Òkè",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "granite inselberg",
      "hill",
      "hills",
      "idanre",
      "monolith",
      "mountain",
      "mountains",
      "oke",
      "olumo rock",
      "rock",
      "rocks"
    ],
    "description": "Sacred granite monoliths, massive inselbergs, and mountainous hill refuges that provided sanctuary during wars and serve as spiritual landmarks.",
    "sub_variants": [
      "Àpáta Olúmo",
      "Àpáta Ìdánre",
      "Òkè Àdó-Awayè",
      "Òkè Ìbàdàn",
      "Òkè Ìgẹ́ti"
    ],
    "historical_timeline": "Olumo Rock protected the Ẹ̀gbá people during the 19th-century wars; Idanre hills inhabited for over 800 years.",
    "etymology_and_philosophy": "Òkè symbolizes permanence, elevation, refuge, and endurance against tribulations.",
    "material_and_craftsmanship": "Natural pre-Cambrian crystalline granite outcrops, natural rock caves, and ancient summit stone steps.",
    "social_and_ritual_context": "Honored during annual festivals (e.g. Ọdún Olúmo, Ọdún Òkè Ìbàdàn) with prayer pilgrimages.",
    "proverbs_and_oral_traditions": [
      "Olúmo gbà wá, ó sì gbà wá títí.",
      "Òkè kì í yí padà."
    ],
    "diaspora_connections": "Revered conceptually in transatlantic orisha cosmology as manifestations of Òkè, deity of heights.",
    "geographical_origin": "Abẹ́òkúta, Idanre, Ìbàdàn, Àdó-Awayè.",
    "media_production_notes": "Dramatic panoramic shots of granite domes rising majestically above tropical forest canopies."
  },
  {
    "id": "Odò",
    "title": "Odò",
    "category": "Architecture, Space & Built Heritage",
    "aliases": [
      "erinjiyan",
      "ikogosi",
      "odo",
      "river",
      "rivers",
      "sacred waters",
      "spring",
      "springs",
      "stream",
      "waterfall",
      "waters"
    ],
    "description": "Sacred river courses, geothermal warm/cold springs, and cascading waterfalls patronized by maternal river divinities (Ọ̀ṣun, Ọ̀yá, Yemọja).",
    "sub_variants": [
      "Odo Ọ̀ṣun",
      "Odo Ògùn",
      "Ikogosi Warm Springs",
      "Erin-Ijesha Waterfalls",
      "Erinle River",
      "Oya River"
    ],
    "historical_timeline": "Sacred geographic sanctuaries revered for over a millennium as healing and life-giving watercourses.",
    "etymology_and_philosophy": "Omi tútù (Cool water) brings peace, healing, fertility, and washes away metaphysical contamination.",
    "material_and_craftsmanship": "Natural therapeutic waters, riparian groves, mineral geothermal confluences, and sacred brass vessels.",
    "social_and_ritual_context": "Sites of annual purification pilgrimages, deity vows, child-dedication rites, and sacred immersion.",
    "proverbs_and_oral_traditions": [
      "Omi tútù kì í ba nǹkan jẹ́.",
      "Odò tó gbàgbé orísun rẹ̀ á gbẹ."
    ],
    "diaspora_connections": "Sacred river rites directly replicated in Cuban river pilgrimages to Oshun and Brazilian sea festivals to Yemoja.",
    "geographical_origin": "Òṣogbo, Ikogosi, Erin-Ijesha, Ọ̀yọ́, Abẹ́òkúta.",
    "media_production_notes": "Capture pristine clear waters, cascading multi-tier falls, and devotees dipping brass vessels at dawn."
  },
  {
    "id": "Ìlú",
    "title": "Ìlú",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "ancient kingdom",
      "cities",
      "city",
      "city state",
      "ilu",
      "kingdom",
      "kingdoms",
      "settlement",
      "town",
      "towns"
    ],
    "description": "The classical autonomous urban city-state, founded under the authority of a crowned monarch (Ọba Aládé) and governed through civil councils and guilds.",
    "sub_variants": [
      "Ilé-Ifẹ̀",
      "Ọ̀yọ́-Ilé",
      "Ìbàdàn",
      "Abẹ́òkúta",
      "Ìjẹ̀bú-Òde",
      "Òndó",
      "Ìlọrin",
      "Ẹdẹ",
      "Òṣogbo",
      "Àkúrẹ́",
      "Òwò"
    ],
    "historical_timeline": "Urban city-state civilization documented in southwest Nigeria from the first millennium CE onward.",
    "etymology_and_philosophy": "Ìlú implies civic order, law, municipal harmony, and collective communal identity.",
    "material_and_craftsmanship": "Radial urban planning featuring central palace, facing market, circumferential city walls, and town gates.",
    "social_and_ritual_context": "Divided into quarters (Àdúgbò) managed by quarter chiefs and age-grade civic societies.",
    "proverbs_and_oral_traditions": [
      "Ìlú kì í wà kí ó má ní Ọba.",
      "Àjòjì kì í mọ ilẹ̀ Ìlú bí ọmọ onílẹ̀."
    ],
    "diaspora_connections": "Town origins (Nago, Oyo, Ijesha, Ketu) became foundational nation groups (Naciones) in Cuba and Brazil.",
    "geographical_origin": "Yorùbá homeland.",
    "media_production_notes": "Present maps and aerial perspectives showing palace-centric radial layout and bustling urban quarters."
  },
  {
    "id": "Ẹranko",
    "title": "Ẹranko",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "animal",
      "animals",
      "beast",
      "elephant",
      "eranko",
      "fauna",
      "game",
      "leopard",
      "lion",
      "mammals",
      "wildlife"
    ],
    "description": "The quadruped animal kingdom, terrestrial wildlife, and game mammals revered across Yorùbá cosmology, royal totems, folklore, and guild hunting.",
    "sub_variants": [
      "Erin",
      "Ẹ̀kùn",
      "Kiníun",
      "Àmọ̀tẹ́kùn",
      "Ẹṣin",
      "Àgùntàn",
      "Ewúrẹ́",
      "Ajá",
      "Ọ̀bọ",
      "Ìgálà",
      "Òkété",
      "Ẹlẹ́dẹ̀"
    ],
    "historical_timeline": "Deep ecological relationship codified in oral hunters' poetry (Ìjálá) and royal emblems over millennia.",
    "etymology_and_philosophy": "Ẹranko (Eran + Oko: Creature of the wild). Animals possess spiritual essence and specific behavioral wisdom.",
    "material_and_craftsmanship": "Hides, horns, tusks, and bone used for royal horns, medicine containers, and leather crafts.",
    "social_and_ritual_context": "The elephant (Erin) symbolizes royal majesty; the leopard (Ẹ̀kùn) embodies fierce executive power.",
    "proverbs_and_oral_traditions": [
      "Àjànàkú kọjá mo rí nǹkan firi, bí a bá rí erin, kí á sọ pé a rí erin.",
      "Ẹ̀kùn kì í ṣe ẹgbẹ́ ajá."
    ],
    "diaspora_connections": "Totemic animals maintain prominent symbolic status in Afro-Atlantic religious sacrifices and iconography.",
    "geographical_origin": "Pan-Yorùbá rainforests and savannah belts.",
    "media_production_notes": "Feature authentic African wildlife species; avoid portraying non-indigenous fauna."
  },
  {
    "id": "Ẹyẹ",
    "title": "Ẹyẹ",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "avian",
      "bird",
      "birds",
      "dove",
      "eagle",
      "eye",
      "fowl",
      "hawk",
      "pigeon",
      "rooster",
      "sacred bird"
    ],
    "description": "Birds, winged creatures, and mystical avian messengers (Ẹlẹ́yẹ) occupying the liminal space between heaven and earth, crowning crowns and sacred staves.",
    "sub_variants": [
      "Àkùkọ",
      "Agbe",
      "Àlùkò",
      "Odídẹrẹ́",
      "Àṣá",
      "Àwòdì",
      "Àdàbà",
      "Ẹyẹlé",
      "Àpárò",
      "Igun",
      "Òwìwí"
    ],
    "historical_timeline": "Avian symbolism present on classical Ifẹ̀ bronzes, crowns, and Ọ̀sanyìn herbal medicine staves.",
    "etymology_and_philosophy": "Birds represent maternal cosmic power (Àwọn Ìyá Mi), spiritual transcendence, and visionary foresight.",
    "material_and_craftsmanship": "Iridescent feathers (Parrot red tail-feather Ẹyin Ìkódẹ, Turaco blue feathers) used in crowns and regalia.",
    "social_and_ritual_context": "The rooster (Àkùkọ) heralds the dawn; the pigeon (Ẹyẹlé) brings peace and prosperity; the vulture (Igun) carries sacrifices.",
    "proverbs_and_oral_traditions": [
      "Agbe kì í dákẹ́ lórí igi.",
      "Ẹyẹlé kì í bínú kúrò nílé."
    ],
    "diaspora_connections": "Avian attributes central to Santería and Candomblé offerings and bird-crowned Osanyin staves.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Focus on the bird crowning the monarch's beaded crown (Okin) and the sixteen birds of Ọ̀sanyìn."
  },
  {
    "id": "Ẹja",
    "title": "Ẹja",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "aquatic",
      "aquatic fauna",
      "catfish",
      "eja",
      "fish",
      "fishes",
      "igbin",
      "marine",
      "mudfish",
      "snail"
    ],
    "description": "Fishes, aquatic fauna, and sacred freshwater mollusks (such as the giant land snail Ìgbín) associated with water deities and peaceful offerings.",
    "sub_variants": [
      "Ẹja Àrọ̀",
      "Àbọ̀rí",
      "Ẹja Kíka",
      "Ìgbín",
      "Alágẹmọ"
    ],
    "historical_timeline": "Mudfish iconography featured prominently in ancient Ifẹ̀, Ọ̀yọ́, and Benin royal arts for centuries.",
    "etymology_and_philosophy": "The mudfish (Ẹja Àrọ̀) survives both in water and dry mud, symbolizing resilience, endurance, and transformation.",
    "material_and_craftsmanship": "Preserved through indigenous wood-smoking methods; snail shells used as liquid medicine bowls.",
    "social_and_ritual_context": "The fluid of the snail (Omi Ìgbín) is the quintessential pacifying offering for the serene deity Ọbàtálá.",
    "proverbs_and_oral_traditions": [
      "Ẹja tútù kì í bọ́ sọ́wọ́ kí ó dákẹ́.",
      "Ìrọ̀rùn igbín ni ìrọ̀rùn igi."
    ],
    "diaspora_connections": "Prominent in Cuban and Brazilian rites for Oshun, Yemoja, and Obatala (sacred offerings of eja and igbin).",
    "geographical_origin": "Lagos lagoons, Osun, Ogun, and Niger river basins.",
    "media_production_notes": "Show fresh African mudfish and the large white-fleshed sacred land snail Ìgbín."
  },
  {
    "id": "Bàbá",
    "title": "Bàbá",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "baba",
      "dad",
      "elder",
      "father",
      "male parent",
      "patriarch",
      "senior patriarch"
    ],
    "description": "The father, paternal elder, and patriarch representing genealogical stewardship, moral authority, family defense, and wisdom.",
    "sub_variants": [
      "Bàbá Ilé",
      "Bàbá Àgbà",
      "Bàbá Ẹgbẹ́",
      "Bàbá Ìdílé"
    ],
    "historical_timeline": "Foundational pillar of Yorùbá patrilineal clan organization across centuries.",
    "etymology_and_philosophy": "Bàbá signifies shelter, lineage foundation, and moral exemplar.",
    "material_and_craftsmanship": "Invested with family ancestral shrines, family lands, and traditional robes.",
    "social_and_ritual_context": "Leads morning prayers for family offspring, arbitrates domestic disputes, and directs marriage negotiations.",
    "proverbs_and_oral_traditions": [
      "Bàbá ni àbà, ọmọ ni ẹ̀ṣọ́.",
      "Bí bàbá bá kú, bàbá ń kù."
    ],
    "diaspora_connections": "Title Bàbá (and Babalorisha / Babalawo) used universally across the Afro-Atlantic world.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Portray senior father seated on veranda chair conferring blessings with quiet moral authority."
  },
  {
    "id": "Ìyá",
    "title": "Ìyá",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "abiyamo",
      "female parent",
      "iya",
      "matriarch",
      "mother",
      "mum",
      "senior matriarch"
    ],
    "description": "The mother, maternal matriarch, and sacred bearer of life (Àbiyamọ) venerated as the compassionate moral center and spiritual guardian of the lineage.",
    "sub_variants": [
      "Àbiyamo",
      "Ìyá Ilé",
      "Ìyá Àgbà",
      "Ìyá Ẹgbẹ́",
      "Ìyál'ọ́jà"
    ],
    "historical_timeline": "Revered across all epochs; female ancestors (Ìyá Mi) possess supreme spiritual oversight.",
    "etymology_and_philosophy": "Ìyá ni wúrà (Mother is pure gold). Motherhood embodies selflessness, spiritual shield, and nurturing.",
    "material_and_craftsmanship": "Adorned with multi-piece woven wrappers (Ìró), headties (Gèlè), and nursing cloths (Ọ̀já).",
    "social_and_ritual_context": "Celebrated at births, weddings, and communal feasts; prayers of a mother are deemed universally efficacious.",
    "proverbs_and_oral_traditions": [
      "Ìyá ni wúrà, bàbá ni dígí.",
      "Àbiyamọ kì í gbọ́ ẹkún ọmọ rẹ̀ kí ó má ta wàrà."
    ],
    "diaspora_connections": "Universal title in Brazilian and Cuban houses (Iyalorisha, Iyami).",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Depict mother wrapping child in traditional Ọ̀já back-cloth with serene protective warmth."
  },
  {
    "id": "Ọmọ",
    "title": "Ọmọ",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "abiku",
      "child",
      "children",
      "daughter",
      "offspring",
      "omo",
      "progeny",
      "son"
    ],
    "description": "The child, offspring, and future continuity of the lineage, treasured above all material wealth in Yorùbá value systems.",
    "sub_variants": [
      "Ọmọ Lúwàbí",
      "Àbíkú",
      "Ìbejì",
      "Ọmọdé",
      "Àrẹ̀mọ"
    ],
    "historical_timeline": "Lineage perpetuity has formed the supreme aspiration of Yorùbá families for centuries.",
    "etymology_and_philosophy": "Ọmọ lérè ayé (Children are the ultimate profit of life). A community responsibility: Ọmọ ẹnìkan kì í ṣe ti ẹnìkan.",
    "material_and_craftsmanship": "Protected by waist beads, infant anklets, and medicinal care.",
    "social_and_ritual_context": "Formally named on the eighth day (Ìsọmọlórúkọ) with honey, salt, water, and dried fish.",
    "proverbs_and_oral_traditions": [
      "Ọmọ kì í burú kí á fi fún ẹkùn pa jẹ.",
      "Ọmọ tí a kò kọ́ ni yóò gbé ilé tí a kọ́ tà."
    ],
    "diaspora_connections": "Ceremonies for divine twins (Ibeji) and children thrive across Cuba, Brazil, and Trinidad.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Capture the eighth-day naming ritual with elder tasting honey and whispering ancestral names."
  },
  {
    "id": "Ẹbí",
    "title": "Ẹbí",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "ancestral lineage",
      "clan",
      "ebi",
      "extended family",
      "family",
      "idile",
      "lineage",
      "relatives"
    ],
    "description": "The extended patrilineal clan, kinship network, and collective ancestral lineage binding living members, unborn descendants, and departed ancestors.",
    "sub_variants": [
      "Ìdílé",
      "Orírun",
      "Àwọn Ẹbí",
      "Ẹgbẹ́ Ẹbí"
    ],
    "historical_timeline": "Organized into royal and civic houses maintaining continuous genealogical trees for generations.",
    "etymology_and_philosophy": "Ẹbí provides identity, moral support, mutual accountability, and shared honor.",
    "material_and_craftsmanship": "Shares collective compound buildings, ancestral burial chambers, and clan praise poetry (Oríkì Ìdílé).",
    "social_and_ritual_context": "Convenes for family meetings, disputes, weddings, funeral pageantry, and communal contributions.",
    "proverbs_and_oral_traditions": [
      "Ẹbí kì í ṣe ohun àkọ́kọ̀ sílẹ̀.",
      "Bí igi bá dá lé igi, ti òkè la kọ́ ń wò."
    ],
    "diaspora_connections": "Transformed into religious family kinship lines (Egbe / Terreiro / Casa) in the diaspora.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Portray vibrant multi-generational family gathering dressed in unified commemorative Aṣọ Ẹbí."
  },
  {
    "id": "Ọkọ",
    "title": "Ọkọ",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "bridegroom",
      "head of household",
      "husband",
      "male partner",
      "oko_husband",
      "spouse"
    ],
    "description": "The husband, matrimonial protector, and household head in Yorùbá marriage traditions.",
    "sub_variants": [
      "Ọkọ Ìyàwó",
      "Bàbá Ilé"
    ],
    "historical_timeline": "Marriage traditions formalized across pre-colonial customary laws.",
    "etymology_and_philosophy": "Demands responsibility, provision, respect for in-laws, and fidelity to marital covenants.",
    "material_and_craftsmanship": "Provides bridal dowry gifts (Ẹrù Ìyàwó), yams, honey, salt, and clothing to the bride's lineage.",
    "social_and_ritual_context": "Prostrates before his prospective in-laws during the traditional engagement (Ìdána).",
    "proverbs_and_oral_traditions": [
      "Ọkọ tó mọ orí aya rẹ̀ kì í fẹ́ kí ó sunkún.",
      "Aya rere ló ń ṣe adé fún ọkọ rẹ̀."
    ],
    "diaspora_connections": "Customary wedding conventions adapted in modern Afro-Atlantic diasporic celebrations.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show groom in rich Agbádá prostrating fully to the ground before his bride's seated family."
  },
  {
    "id": "Ìyàwó",
    "title": "Ìyàwó",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "bride",
      "female partner",
      "iyawo",
      "new bride",
      "nuptials",
      "spouse",
      "wife"
    ],
    "description": "The wife, bride, and nuptial partner welcomed into her new family compound through traditional bridal songs and foot-washing ceremonies.",
    "sub_variants": [
      "Ìyàwó Titun",
      "Ẹ̀kún Ìyàwó",
      "Ayaba (Royal Wife)"
    ],
    "historical_timeline": "Bridal poetry (Ẹ̀kún Ìyàwó) constitutes one of the oldest genres of Yorùbá oral literature.",
    "etymology_and_philosophy": "Derived from the ancient legend of Ìyàwó at Ìwó town; represents resilience, love, and community bridge.",
    "material_and_craftsmanship": "Dressed in hand-loomed Aṣọ-Òkè, intricate coral necklaces, henna body art (Lálì), and elaborate hair braiding.",
    "social_and_ritual_context": "Chants farewell poetry (Ẹ̀kún Ìyàwó) to her birth family; enters the new compound with pure water washed over her feet.",
    "proverbs_and_oral_traditions": [
      "Ìyàwó tó mọ̀wà ló ń gbé ilé ọkọ rẹ̀ pẹ́.",
      "Ẹ̀kún ìyàwó kò kún fún ìbànújẹ́, ayọ̀ ló ń ké."
    ],
    "diaspora_connections": "Bridal chants and respect protocols echo in diaspora marriage and initiation rites.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Depict emotional bride reciting poetic verses before elders, holding embroidered bridal fan."
  },
  {
    "id": "Òrìṣà",
    "title": "Òrìṣà",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "deities",
      "deity",
      "divinities",
      "divinity",
      "eshu",
      "god",
      "gods",
      "obatala",
      "orisa",
      "osun",
      "pantheon",
      "sango",
      "ògún deity"
    ],
    "description": "The divine primordial divinities, deified ancestors, and cosmic emissaries of Olódùmarè governing the elements, morality, human destiny, and nature.",
    "sub_variants": [
      "Ọbàtálá",
      "Ṣàngó",
      "Ọ̀ṣun",
      "Èṣù",
      "Ògún",
      "Ọ̀yá",
      "Yemọja",
      "Ọ̀sọ́ọ̀sì",
      "Ọ̀sanyìn",
      "Erinlẹ̀",
      "Ọbàlúayé"
    ],
    "historical_timeline": "Cosmological matrix developed in classical Ilé-Ifẹ̀ and disseminated globally across the Atlantic.",
    "etymology_and_philosophy": "Òrí-ṣẹ̀ (Consciousness that sprouted at the beginning of time). Forces that intermediate between human and divine.",
    "material_and_craftsmanship": "Sacred emblems: brass for Ọ̀ṣun, iron for Ògún, lead/white cloth for Ọbàtálá, thunderstones (Èdùn Àrá) for Ṣàngó.",
    "social_and_ritual_context": "Venerated through dedicated priesthoods, annual civic festivals, and personalized morning prayers.",
    "proverbs_and_oral_traditions": [
      "Òrìṣà bí o bá gbè mí, fi mí sílẹ̀ bí o ṣe bá mi.",
      "Òrìṣà tó kọ̀ tí kò gba ẹbọ, kò ní rí ìyìn."
    ],
    "diaspora_connections": "Venerated by tens of millions across Cuba (Santería), Brazil (Candomblé), Trinidad, and the United States.",
    "geographical_origin": "Ilé-Ifẹ̀, Ọ̀yọ́, Òṣogbo, Ẹdẹ, Abẹ́òkúta.",
    "media_production_notes": "Present each Òrìṣà with accurate canonical colors, liturgical dance steps, and authentic sacred implements."
  },
  {
    "id": "Odù_Ifá",
    "title": "Odù Ifá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "256 odu",
      "divination chapters",
      "eji ogbe",
      "ifa corpus",
      "odu",
      "odu ifa",
      "oyeku meji",
      "sacred verses"
    ],
    "description": "The monumental 256-chapter corpus of sacred divination verses encoding Yorùbá philosophy, history, medicine, and morality, recognized as a UNESCO Masterpiece of Intangible Heritage.",
    "sub_variants": [
      "Èjì Ogbè",
      "Ọ̀yẹ̀kú Méjì",
      "Ìwòrì Méjì",
      "Òdí Méjì",
      "Ìrosùn Méjì",
      "Ọ̀wọ́nrín Méjì",
      "Ọ̀bàrà Méjì",
      "Ọ̀kànràn Méjì"
    ],
    "historical_timeline": "Oral library compiled and memorized across thousands of years of Babaláwo priesthood lineages.",
    "etymology_and_philosophy": "The immutable word of Olódùmarè communicated through Ọ̀rúnmìlà to reveal destiny and resolve life crises.",
    "material_and_craftsmanship": "Preserved through total oral memorization across 16 major Ojú Odù and 240 paired combinations (Àmúlù).",
    "social_and_ritual_context": "Consulted at every milestone: birth, marriage, coronations, illness, and state policies.",
    "proverbs_and_oral_traditions": [
      "Ifá kì í purọ́, Ọ̀rúnmìlà kì í ṣèké.",
      "Ẹni tó mọ Ifá ló ń mọ ọ̀rọ̀ ayé."
    ],
    "diaspora_connections": "Universal canonical matrix of Ifá divination practiced in Cuba, Venezuela, Brazil, and North America.",
    "geographical_origin": "Ilé-Ifẹ̀, Òkè-Ìgẹ́ti, Ado-Ekiti.",
    "media_production_notes": "Render the sixteen binary marks (I and II) accurately on woodpowder (Ìyẹ̀ròsùn) on the divination tray."
  },
  {
    "id": "Egúngún",
    "title": "Egúngún",
    "category": "Ancestral Masquerades & Funerary Rites",
    "aliases": [
      "alapinni",
      "ancestor",
      "ancestors",
      "ancestral spirit",
      "egungun",
      "egungun masquerade",
      "masquerade",
      "masquerades"
    ],
    "description": "The physical manifestation of ancestral spirits returning from the celestial realm (Ọ̀run) in layered textile masquerades to bless, cleanse, and counsel their living descendants.",
    "sub_variants": [
      "Egúngún Elédà",
      "Egúngún Alágbàá",
      "Egúngún Danafojura",
      "Gèlèdẹ́",
      "Agẹmọ",
      "Eyo Masquerade"
    ],
    "historical_timeline": "Ancestral veneration institutionalized under the sacred lineage of Aláapinni in classical Ọ̀yọ́ and Ifẹ̀.",
    "etymology_and_philosophy": "Egúngún demonstrates that the ancestors are not dead, but living actively among their community.",
    "material_and_craftsmanship": "Multi-layered sumptuous cloth strips, embroidered silk, velvet, cowrie-studded masks, and carved wooden headpieces.",
    "social_and_ritual_context": "Celebrated in annual festivals; wields ceremonial whips (Pàṣán) to dispel metaphysical negativity.",
    "proverbs_and_oral_traditions": [
      "Egúngún tó ń jó, ayọ̀ ló ń fún ará ìlú.",
      "Bí egúngún bá gbè wá, à ń yọ̀."
    ],
    "diaspora_connections": "Preserved in the sacred Egungun societies of Oyotunji Village and Itaparica Island in Bahia, Brazil.",
    "geographical_origin": "Ọ̀yọ́, Ìbàdàn, Òkè-Ògùn, Ìjẹ̀bú, Lagos.",
    "media_production_notes": "Never expose any human skin beneath the masquerade; textiles must whirl dynamically during dance."
  },
  {
    "id": "Ọdún",
    "title": "Ọdún",
    "category": "Festivals, Celebrations & Civic Pageantry",
    "aliases": [
      "annual feast",
      "celebration",
      "celebrations",
      "ceremony",
      "cultural festival",
      "festival",
      "festivals",
      "odun"
    ],
    "description": "The annual cyclic festivals, civic pageantry, and spiritual celebrations marking the turn of the seasons, harvest of crops, and renewal of divine covenants.",
    "sub_variants": [
      "Ọdún Ọlọ́jọ́",
      "Ọdún Òṣun Òṣogbo",
      "Ọdún Ìgogo",
      "Ọdún Agẹmọ",
      "Ọdún Ògún",
      "Ọdún Ìjeṣu"
    ],
    "historical_timeline": "Observed according to the indigenous 13-month lunar calendar for over a thousand years.",
    "etymology_and_philosophy": "Ọdún implies cyclical time, community renewal, collective thanksgiving, and cosmic rejuvenation.",
    "material_and_craftsmanship": "Spectacular dress ensembles, brass trumpets, ceremonial foods, and royal processions.",
    "social_and_ritual_context": "Brings diaspora sons and daughters home; monarch wears the sacred Adé Ààrẹ on Ọlọ́jọ́ Day in Ifẹ̀.",
    "proverbs_and_oral_traditions": [
      "Ọdún a yọ wá, ọdún a gbè wá.",
      "Ẹni tí ọdún bá bá, ayọ̀ ló ń yọ̀."
    ],
    "diaspora_connections": "Influenced Caribbean carnival traditions and Afro-Brazilian festive processions in Bahia.",
    "geographical_origin": "Ilé-Ifẹ̀, Òṣogbo, Ìjẹ̀bú-Òde, Òwò.",
    "media_production_notes": "Portray vibrant community atmosphere, royal retinue, dynamic drumming, and shared feast tables."
  },
  {
    "id": "Ògbóni",
    "title": "Ògbóni",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "earth society",
      "edan",
      "edan ogboni",
      "elders society",
      "indigenous judiciary",
      "judicial council",
      "ogboni",
      "osugbo"
    ],
    "description": "The ancient judicial, political, and spiritual fraternity of senior elders dedicated to venerating Mother Earth (Ilẹ̀), checking royal power, and maintaining justice.",
    "sub_variants": [
      "Ẹdan Ògbóni",
      "Onílẹ̀",
      "Ìwàrẹ̀fà",
      "Ilé-Awo",
      "Òṣùgbó"
    ],
    "historical_timeline": "One of the most ancient indigenous institutions of Yorùbáland, pre-dating modern state structures.",
    "etymology_and_philosophy": "Ògbó-ní (Those possessed of deep wisdom). Dedicated to absolute justice, secrecy, and peace.",
    "material_and_craftsmanship": "Cast brass twin staves linked by a chain (Ẹdan Ògbóni), carved earthen shrines, and ceremonial sashes (Ìtagbè).",
    "social_and_ritual_context": "The supreme judicial appellate court in traditional society; arbitrates capital offenses and kingly succession.",
    "proverbs_and_oral_traditions": [
      "Ògbóni kò ní kùrà.",
      "Ilẹ̀ tó mọ awo kì í da awo."
    ],
    "diaspora_connections": "Revered in Cuban Lucumí and Trinidadian Orisha shrines as the sacred society of elders and brass staves.",
    "geographical_origin": "Ìjẹ̀bú, Ẹ̀gbá, Ọ̀yọ́, Ilé-Ifẹ̀.",
    "media_production_notes": "Show the linked brass Ẹdan staves carried with dignified solemnity; preserve traditional reverence."
  },
  {
    "id": "Ọpọ́n_Ifá",
    "title": "Ọpọ́n Ifá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "carved tray",
      "divination tray",
      "divining board",
      "ifa tray",
      "opon ifa",
      "sacred tray"
    ],
    "description": "The circular or rectangular carved wooden divination tray upon which woodpowder (Ìyẹ̀ròsùn) is dusted and sacred Odù Ifá marks are transcribed.",
    "sub_variants": [
      "Ọpọ́n Ifá Olórí Èṣù",
      "Ọpọ́n Ifá Gbẹ́rọ́",
      "Ọpọ́n Ọlọ́fà"
    ],
    "historical_timeline": "Carved for over a millennium; masterworks collected in international museums like Ulm (collected 1650 CE).",
    "etymology_and_philosophy": "Represents the flat cosmic universe; bordered by the watching face of Èṣù who verifies sacrifices.",
    "material_and_craftsmanship": "Carved from solid hardwood (Irókò) with high-relief borders depicting animals, drums, and deities.",
    "social_and_ritual_context": "Used during formal consultations by Babaláwos to resolve crises and guide monarchs.",
    "proverbs_and_oral_traditions": [
      "Ọpọ́n Ifá kì í fọ́ sọ́wọ́ awo.",
      "Èṣù ló ń wo orí ọpọ́n."
    ],
    "diaspora_connections": "Universal in Cuban and American Ifá divination ceremonies (Tablero de Ifá).",
    "geographical_origin": "Ọ̀yọ́, Èkìtì, Òwò, Ìjẹ̀bú.",
    "media_production_notes": "Show close-up of the carved face of Èṣù looking inward toward the golden-yellow wooddust markings."
  },
  {
    "id": "Ìrókẹ́_Ifá",
    "title": "Ìrókẹ́ Ifá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "divination tapper",
      "ifa tapper",
      "invocation wand",
      "iroke",
      "iroke ifa",
      "ivory tapper",
      "tapper"
    ],
    "description": "The pointed carved elephant ivory, brass, or hardwood tapper used by the diviner to rhythmically tap the center of the tray and invoke the presence of Ọ̀rúnmìlà.",
    "sub_variants": [
      "Ìrókẹ́ Eyin Erin (Ivory)",
      "Ìrókẹ́ Idẹ (Brass)",
      "Ìrókẹ́ Igi (Hardwood)"
    ],
    "historical_timeline": "Ivory tappers feature among the highest achievements of classical Yorùbá court sculpture.",
    "etymology_and_philosophy": "Rhythmic tapping aligns the frequency of the physical chamber with celestial cosmic realms.",
    "material_and_craftsmanship": "Carved elephant ivory or cast brass depicting a kneeling devotee (Arúgbá) or equestrian warrior.",
    "social_and_ritual_context": "Held in the diviner's right hand to summon the spirits before casting divination nuts.",
    "proverbs_and_oral_traditions": [
      "Ìrókẹ́ ń kọ́ ọpọ́n, Ifá ń gbọ́.",
      "À ń kan ìrókẹ́, àwọn awo ń pé."
    ],
    "diaspora_connections": "Universally employed by Babalawo practitioners in Cuba, Brazil, and across the Americas.",
    "geographical_origin": "Òwò, Ilé-Ifẹ̀, Ọ̀yọ́.",
    "media_production_notes": "Show rhythmic clicking sound against the wood of the tray; focus on the carved kneeling figure."
  },
  {
    "id": "Ọ̀pẹ̀lẹ̀",
    "title": "Ọ̀pẹ̀lẹ̀",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "divination chain",
      "divining chain",
      "ifa chain",
      "opele",
      "opele ifa"
    ],
    "description": "The sacred eight-half-pod divination chain cast by Babaláwos for rapid, accurate consultation of the 256 Odù Ifá configurations.",
    "sub_variants": [
      "Ọ̀pẹ̀lẹ̀ Agbalagba",
      "Ọ̀pẹ̀lẹ̀ Idẹ",
      "Ọ̀pẹ̀lẹ̀ Awọ"
    ],
    "historical_timeline": "Employed alongside the slower 16 Ikin palm nut method for centuries.",
    "etymology_and_philosophy": "Falls in two parallel lines of four seeds each, revealing binary concave (open) or convex (closed) faces.",
    "material_and_craftsmanship": "Eight seed pods (Schrebera arbuscula or coconut shells) linked by a cast brass or cotton chain.",
    "social_and_ritual_context": "Held by its central link and thrown gently onto a clean divination mat; interpreted instantly.",
    "proverbs_and_oral_traditions": [
      "Ọ̀pẹ̀lẹ̀ kì í dá èké.",
      "Bí Ọ̀pẹ̀lẹ̀ bá já, awo a tún un so."
    ],
    "diaspora_connections": "Standard daily instrument of Ifá priests across Cuba, Puerto Rico, and the United States.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show fluid casting motion onto the straw mat and the instantaneous reading of the 8 binary pods."
  },
  {
    "id": "Agẹrẹ_Ifá",
    "title": "Agẹrẹ Ifá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "agere",
      "agere ifa",
      "carved container",
      "caryatid",
      "divination cup",
      "ifa cup",
      "sacred bowl"
    ],
    "description": "The elaborately carved wooden caryatid cup or bowl supported by sculpted equestrian warriors or kneeling women, holding the sacred 16 Ikin palm nuts.",
    "sub_variants": [
      "Agẹrẹ Ológun (Equestrian)",
      "Agẹrẹ Arúgbá (Kneeling Maiden)",
      "Agẹrẹ Ẹlẹ́yinjú"
    ],
    "historical_timeline": "Masterwork genre of Yorùbá sculpture celebrated in the British Museum and Metropolitan Museum of Art.",
    "etymology_and_philosophy": "Represents the earth bearing the weight of divine truth with grace, devotion, and elegance.",
    "material_and_craftsmanship": "Monoxylous carving from dense hardwood, embellished with polychrome pigments or beadwork.",
    "social_and_ritual_context": "Rests beside the diviner's consultation mat as a secure sanctuary for the divine seeds.",
    "proverbs_and_oral_traditions": [
      "Agẹrẹ ló ń gbé Ifá ró.",
      "Ẹni tó fi ọwọ́ méjèèjì gbé Agẹrẹ kì í bọ́."
    ],
    "diaspora_connections": "Revered in Cuban and Brazilian Ifá houses as the sacred receptacle of Orula.",
    "geographical_origin": "Èkìtì, Òwò, Ọ̀yọ́, Ìjẹ̀bú.",
    "media_production_notes": "Highlight intricate figurative sculpture underneath supporting the smooth rounded cup above."
  },
  {
    "id": "Ikin_Ifá",
    "title": "Ikin Ifá",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "16 ikin",
      "divination nuts",
      "ikin",
      "ikin ifa",
      "palm nuts",
      "sacred nuts",
      "sacred palm kernels"
    ],
    "description": "The sixteen sacred four-eyed palm nuts (Elaeis guineensis) representing the physical embodiment of Ọ̀rúnmìlà, used in supreme divination consultations.",
    "sub_variants": [
      "Ikin Ọlọ́jú Mẹ́rin (4-eyed)",
      "Ikin Ọlọ́jú Mẹ́ta",
      "Ikin Ọ̀rúnmìlà"
    ],
    "historical_timeline": "Left behind by Ọ̀rúnmìlà as his eternal earthly representatives when he ascended to the celestial realm.",
    "etymology_and_philosophy": "Ikin seeds are ancient, immutable, and hold direct communion with divine destiny.",
    "material_and_craftsmanship": "Specialized palm nuts with four or more germination eyes, polished with palm oil and camwood.",
    "social_and_ritual_context": "Cast between the diviner's hands sixteen times in the most sacred and formal Ifá consultations.",
    "proverbs_and_oral_traditions": [
      "Ikin kì í ṣe ohun àfipamọ́.",
      "Ọ̀rúnmìlà fi ikin sílẹ̀ bí aṣoju."
    ],
    "diaspora_connections": "The foundation of all Ifá shrines (Adele) across Cuba and the transatlantic diaspora.",
    "geographical_origin": "Pan-Yorùbá sacred palm groves.",
    "media_production_notes": "Show the sixteen dark, oily palm nuts cupped in the Babaláwo's palms before pressing against the tray."
  },
  {
    "id": "Ìwà",
    "title": "Ìwà",
    "category": "Oral Literature, Philosophy & Folklore",
    "aliases": [
      "character",
      "ethics",
      "good character",
      "iwa",
      "iwa rere",
      "moral character",
      "morals",
      "omoluwabi"
    ],
    "description": "Character, ethical integrity, and moral poise forming the supreme human virtue in classical Yorùbá philosophy (Ìwà Rere).",
    "sub_variants": [
      "Ìwà Rere",
      "Ọmọlúwàbí",
      "Ìfarabalẹ̀",
      "Sùúrù",
      "Ìtìjú"
    ],
    "historical_timeline": "Central philosophic doctrine enunciated throughout the 256 Odù Ifá corpus.",
    "etymology_and_philosophy": "Ìwà lẹwà (Character is the essence of true beauty). Material wealth without good character is futile.",
    "material_and_craftsmanship": "Expressed through behavioral etiquette: respectful greeting, honest speech, and civic responsibility.",
    "social_and_ritual_context": "Prerequisite for societal leadership, chieftaincy titles, and ancestral veneration.",
    "proverbs_and_oral_traditions": [
      "Ìwà lẹwà ọmọ ènìyàn.",
      "Bí o lówó tí o kò ní ìwà, owó olówó ni."
    ],
    "diaspora_connections": "Fundamental ethical bedrock upheld in transatlantic Orisha temples.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Portray calm, dignified comportment, respectful bowing, and gracious elder mediation."
  },
  {
    "id": "Orí",
    "title": "Orí",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "akunleyan",
      "destiny",
      "inner consciousness",
      "inner head",
      "ori",
      "ori inu",
      "spiritual head"
    ],
    "description": "Destiny, personal divinity, and inner metaphysical consciousness chosen by each soul before incarnation in the realm of Ọbàtálá and Àjàlá Mọ̀pí.",
    "sub_variants": [
      "Orí Inú",
      "Àkúnlẹ̀yàn",
      "Àkúnlẹ̀gbà",
      "Àyànmọ́",
      "Ilé-Orí"
    ],
    "historical_timeline": "The foundational premise of Yorùbá existential theology across millennia.",
    "etymology_and_philosophy": "Orí precedes all other Òrìṣà; no deity can bless a person without the consent of their own inner Orí.",
    "material_and_craftsmanship": "Enshrined physically in a conical beaded leather shrine (Ilé-Orí) studded with thousands of cowries.",
    "social_and_ritual_context": "Venerated through touch to the forehead and prayers for wisdom, longevity, and luck.",
    "proverbs_and_oral_traditions": [
      "Orí la fi ń kọ́ ọlá.",
      "Orí mi, má jẹ́ kí n kùnà lórí ayé."
    ],
    "diaspora_connections": "Universal veneration of Ori and head rogation ceremonies (Kobori / Rogación de Cabeza) in Cuba and Brazil.",
    "geographical_origin": "Ilé-Ifẹ̀, Pan-Yorùbá.",
    "media_production_notes": "Show the magnificent conical cowrie-encrusted shrine (Ilé-Orí) and solemn head prayer rituals."
  },
  {
    "id": "Àṣẹ",
    "title": "Àṣẹ",
    "category": "Spiritual & Cosmological Matrix",
    "aliases": [
      "ase",
      "authority",
      "cosmic force",
      "divine power",
      "power",
      "spiritual authority",
      "vital force"
    ],
    "description": "The divine cosmic life-force, authority, and catalytic vital power bestowed by Olódùmarè that causes speech, prayer, and natural processes to manifest.",
    "sub_variants": [
      "Ọ̀rọ̀ Àṣẹ",
      "Àṣẹ Ọba",
      "Àṣẹ Babaláwo",
      "Ọ̀pá Àṣẹ"
    ],
    "historical_timeline": "The unifying metaphysical principle across all West African and Yorùbá philosophical systems.",
    "etymology_and_philosophy": "So be it; let it manifest. The creative divine spark present in humans, deities, plants, and words.",
    "material_and_craftsmanship": "Embodied in royal scepters, carved gourds of power (Igbá Àṣẹ), and consecrated tongue medicine.",
    "social_and_ritual_context": "Pronounced after blessings, prayers, and judicial decrees to bind the spiritual world to compliance.",
    "proverbs_and_oral_traditions": [
      "Àṣẹ wà lẹ́nu Ọba.",
      "Bí a bá wí, á ṣẹ."
    ],
    "diaspora_connections": "Universal affirmative response and core theological concept across Candomblé (Axé) and Santería (Ashé).",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Evoke moments of solemn collective affirmation where a community resonates with 'Àṣẹ!'."
  },
  {
    "id": "Òwe",
    "title": "Òwe",
    "category": "Oral Literature, Philosophy & Folklore",
    "aliases": [
      "aphorism",
      "idiom",
      "idioms",
      "owe",
      "proverb",
      "proverbs",
      "sayings",
      "traditional sayings"
    ],
    "description": "Axiomatic proverbs, philosophical idioms, and rhetorical vehicles used by elders to resolve disputes, deliver moral truths, and encode ancestral wisdom.",
    "sub_variants": [
      "Òwe Àgbà",
      "Òwe Ìkìlọ̀",
      "Òwe Ìyànjú",
      "Àkójọpọ̀ Òwe"
    ],
    "historical_timeline": "Transmitted continuously through speech, court debate, and oral poetics for millennia.",
    "etymology_and_philosophy": "Òwe lẹṣin ọ̀rọ̀, bí ọ̀rọ̀ bá sọnù, òwe la fi ń wá a (Proverbs are the horses of speech; when speech is lost, proverbs recover it).",
    "material_and_craftsmanship": "Delivered with oratorical finesse, poetic cadence, and measured pacing.",
    "social_and_ritual_context": "Essential in palace debates, marriage negotiations, court judgments, and council deliberations.",
    "proverbs_and_oral_traditions": [
      "Òwe lẹṣin ọ̀rọ̀.",
      "Ẹni tó mọ òwe ló ń tọ́ ọ̀rọ̀ sọ."
    ],
    "diaspora_connections": "Preserved in Lucumí patakís and Afro-Cuban consejo traditions.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Highlight elders speaking with expressive hand gestures and thoughtful pauses before delivering an adage."
  },
  {
    "id": "Oríkì",
    "title": "Oríkì",
    "category": "Auditory Arts, Music, Drums & Chants",
    "aliases": [
      "epithet",
      "eulogy",
      "lineage praise",
      "oriki",
      "panegyric",
      "praise names",
      "praise poetry"
    ],
    "description": "Praise poetry, invocational lineage epithets, and panegyric chants recited to awaken personal pride, honor ancestors, and evoke the spiritual presence of individuals and towns.",
    "sub_variants": [
      "Oríkì Ìdílé",
      "Oríkì Ọba",
      "Oríkì Òrìṣà",
      "Oríkì Ìlú",
      "Oríkì Orúkọ"
    ],
    "historical_timeline": "Ancient performative genre recited by palace chanters (Arokin) and drum ensembles.",
    "etymology_and_philosophy": "Orí (Head/Destiny) + Kì (To salute/praise). Reciting Oríkì expands the inner head with transcendent dignity.",
    "material_and_craftsmanship": "Vocalized in rich melismatic chants or mimicked tonally on the Dùndún talking drum.",
    "social_and_ritual_context": "Chanted at coronations, weddings, funerals, and morning salutations to move listeners to tears and nobility.",
    "proverbs_and_oral_traditions": [
      "Oríkì ni ń mú ọmọ Ọba yangàn.",
      "Bí a bá kì ẹnìkan, orí rẹ̀ a wú."
    ],
    "diaspora_connections": "Liturgical Orisha salutes in Cuba and Brazil are direct retentions of classical Oríkì chants.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Feature solo female chanter with expressive vibrato and rhythmic call-and-response with talking drums."
  },
  {
    "id": "Àrọ̀kọ̀",
    "title": "Àrọ̀kọ̀",
    "category": "Oral Literature, Philosophy & Folklore",
    "aliases": [
      "aroko",
      "coded message",
      "cowrie messaging",
      "cultural semiotics",
      "semiotics",
      "symbolic communication",
      "symbolic messaging"
    ],
    "description": "The sophisticated indigenous semiotic system of coded material communication using shells, feathers, blades, and knotted fibers to send private, diplomatic, judicial, or military messages across distances.",
    "sub_variants": [
      "Àrọ̀kọ̀ Ẹfà (Love)",
      "Àrọ̀kọ̀ Ẹ̀jọ́ (Dispute)",
      "Àrọ̀kọ̀ Ogun (War)",
      "Ẹyin Ìkódẹ (Royal Summons)",
      "Àrọ̀kọ̀ Àlàáfíà (Peace)"
    ],
    "historical_timeline": "Employed throughout pre-colonial diplomacy between sovereign Yorùbá monarchs, generals, and secret societies.",
    "etymology_and_philosophy": "Tangible semiotics: objects embody semantic grammar intelligible to initiated couriers.",
    "material_and_craftsmanship": "Strung cowrie shells (face-to-face or back-to-back), parrot feathers, red cloth, gunpowder, knives, and raffia knots.",
    "social_and_ritual_context": "Carried by royal heralds (Ẹlẹ́kọ̀); 6 cowries facing inward signify mutual love; a powder-filled pod declares war.",
    "proverbs_and_oral_traditions": [
      "Àrọ̀kọ̀ kì í purọ́ lójú awo.",
      "Ẹni tó mọ àrọ̀kọ̀ ló ń gbọ́ ọ̀rọ̀ aṣírí."
    ],
    "diaspora_connections": "Sign systems survived in Abakuá and Palo secret symbol codes in Cuba.",
    "geographical_origin": "Ọ̀yọ́, Ìjẹ̀bú, Èkìtì, Ilé-Ifẹ̀.",
    "media_production_notes": "Show the courier delivering a tied raffia bundle of paired cowrie shells, with elder reading the configuration."
  },
  {
    "id": "Owó_Ẹyọ",
    "title": "Owó Ẹyọ",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "cowrie",
      "cowrie currency",
      "cowrie shell",
      "cowries",
      "money",
      "owo eyo",
      "shell money"
    ],
    "description": "The porcelain-white marine cowrie shell (Cypraea moneta) used for centuries as legal tender currency, royal regalia adornment, divination counter, and symbol of immense wealth.",
    "sub_variants": [
      "Ẹyọ Owó",
      "Ẹ̀gbàá",
      "Ọ̀kẹ́ Owó",
      "Ilé-Orí Ẹyọ"
    ],
    "historical_timeline": "Pre-colonial legal currency standardized into bags (Àpò) and units (Ẹ̀gbàá) before colonial demonetization.",
    "etymology_and_philosophy": "Owó (Money) + Ẹyọ (Single Cowrie). Symbol of wealth, fertility, commercial exchange, and sacred offerings.",
    "material_and_craftsmanship": "Pierced and strung on raffia cords in units of 40, 200, and 2,000 for monetary transactions.",
    "social_and_ritual_context": "Used to pay bridal dowries, market purchases, divination fees, and to adorn royal crowns.",
    "proverbs_and_oral_traditions": [
      "Owó ẹ̀yọ ló ń sọ ọmọdé dọ̀jẹ̀.",
      "Bí kò bá sí owó, kò sí àlàáfíà."
    ],
    "diaspora_connections": "Universal divination instrument (Dillogún / Merindilogún) in Cuban Santería and Candomblé.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show heaps of glistening cowrie shells counted in traditional tallies across wooden counting boards."
  },
  {
    "id": "Ẹgbẹ́",
    "title": "Ẹgbẹ́",
    "category": "Social Structure, Kinship & Lineage",
    "aliases": [
      "aaro",
      "age grade",
      "association",
      "communal labor",
      "egbe",
      "guild",
      "guilds",
      "owe",
      "peer group",
      "society"
    ],
    "description": "Societal age-grade associations, vocational craft guilds, and mutual-aid societies organizing civic labor, mutual defense, and social solidarity.",
    "sub_variants": [
      "Ẹgbẹ́ Àgbẹ̀",
      "Ẹgbẹ́ Ọdẹ",
      "Ẹgbẹ́ Àwọn Ìyá",
      "Àárò (Labor Pooling)",
      "Òwe (Communal Help)"
    ],
    "historical_timeline": "The structural backbone of civic mobilization and economic democracy across Yorùbá municipalities.",
    "etymology_and_philosophy": "Collective synergy; no individual can thrive in isolation from communal fraternity.",
    "material_and_craftsmanship": "Shares uniform festival cloth (Aṣọ Ẹgbẹ́), guild staffs, and communal funds (Ẹ̀súsú).",
    "social_and_ritual_context": "Constructs civic infrastructure, assists members with wedding costs, and provides dignified funeral burial rites.",
    "proverbs_and_oral_traditions": [
      "Ẹgbẹ́ tó wọ̀ kọ̀ kì í fẹ́ kí ọkọ̀ rì.",
      "Ẹyẹ kì í fò kí ó má ní ẹgbẹ́."
    ],
    "diaspora_connections": "Reborn as the mutual-aid Cabildos and Sociedades in Cuba, Brazil, and Trinidad.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show unified dancing troupe of age-grade members dressed in splendid matching silks and commemorative pins."
  },
  {
    "id": "Dùndún",
    "title": "Dùndún",
    "category": "Auditory Arts, Music, Drums & Chants",
    "aliases": [
      "ayan",
      "bata",
      "drum",
      "drum ensemble",
      "drumming",
      "drums",
      "dundun",
      "gangan",
      "talking drum"
    ],
    "description": "The hourglass-shaped pressure talking drum ensemble capable of reproducing the exact pitch contours, glissandos, and speech tones of the Yorùbá language.",
    "sub_variants": [
      "Ìyáàlù Dùndún",
      "Gúdúgúdú",
      "Kẹríkẹrì",
      "Gángan",
      "Bàtá",
      "Ìsájú",
      "Kànàgó"
    ],
    "historical_timeline": "Developed over centuries under the divine patron of drummers, Àyàn Àgalú.",
    "etymology_and_philosophy": "The drum talks directly to human and divine ears; it mimics the 3 phonemic tones (Do, Re, Mi).",
    "material_and_craftsmanship": "Hollowed hardwood shell, twin goatskin membranes, tension cords (Ọsàn), brass rattles (Ṣawọ̀rọ̀), and curved stick (Kọ́ngọ́).",
    "social_and_ritual_context": "Squeeze-and-release technique changes pitch dynamically during royal praise, festivals, and battles.",
    "proverbs_and_oral_traditions": [
      "Dùndún kì í dákẹ́ lẹ́nu awo.",
      "Àyàn kì í gbàgbé ohùn tirẹ̀."
    ],
    "diaspora_connections": "Bàtá drum sacred trios survive with liturgical precision in Cuban Santería ceremonies.",
    "geographical_origin": "Ọ̀yọ́, Ìbàdàn, Ìjẹ̀bú, Òkè-Ògùn.",
    "media_production_notes": "Show the drummer squeezing tension cords beneath the arm while striking the drumhead with curved stick."
  },
  {
    "id": "Orin",
    "title": "Orin",
    "category": "Auditory Arts, Music, Drums & Chants",
    "aliases": [
      "chant",
      "chants",
      "music",
      "orin",
      "singing",
      "song",
      "songs",
      "traditional music"
    ],
    "description": "Indigenous vocal music, call-and-response communal singing, and sacred litanies accompanying ceremonies, work, war, and spiritual festivals.",
    "sub_variants": [
      "Orin Ọba",
      "Orin Òrìṣà",
      "Orin Àárọ̀",
      "Wákà",
      "Sákárà",
      "Àpàlà",
      "Fújì (Roots)"
    ],
    "historical_timeline": "Vocal tradition rooted in antiquity and continuously evolving into world-renowned modern genres.",
    "etymology_and_philosophy": "Song bridges emotion and cosmic order; words sung carry multiplied metaphysical potency.",
    "material_and_craftsmanship": "Performed with polyrhythmic hand-clapping, iron gongs (Agogo), and gourd rattles (Ṣẹ̀kẹ̀rẹ̀).",
    "social_and_ritual_context": "Led by lead vocalists (Alóore) with whole assemblies chiming in on responsive choruses (Ègbè).",
    "proverbs_and_oral_traditions": [
      "Orin tó dára kì í sú eti.",
      "Ẹni tó mọ orin kọ kò ní kùrà."
    ],
    "diaspora_connections": "The foundation of Afro-Cuban rumba, Brazilian samba roots, and afro-spiritual music styles.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Dynamic call-and-response vocal delivery with communal chorus joining in infectious joy."
  },
  {
    "id": "Àlọ́",
    "title": "Àlọ́",
    "category": "Oral Literature, Philosophy & Folklore",
    "aliases": [
      "alo",
      "fables",
      "folktale",
      "folktales",
      "ijapa",
      "moral stories",
      "riddles",
      "storytelling",
      "tales"
    ],
    "description": "Evening fireside oral storytelling, moral fables, and intellectual riddles (Àpamọ̀) teaching youth moral ethics through the adventures of Ìjàpá the tortoise.",
    "sub_variants": [
      "Àlọ́ Àpamọ̀ (Riddles)",
      "Àlọ́ Àpagbè (Fables with Songs)",
      "Ìtàn Ìjàpá"
    ],
    "historical_timeline": "Primary pre-colonial oral pedagogical curriculum for generations of Yorùbá children.",
    "etymology_and_philosophy": "Àlọ́ combines wit, moral correction, humor, and communal bonding under the moonlit sky (Àbẹ́ Òṣùpá).",
    "material_and_craftsmanship": "Delivered through vocal dramatization, character voices, and chorus songs.",
    "social_and_ritual_context": "Told after dinner; riddles test intellectual sharpness before narrative fables begin.",
    "proverbs_and_oral_traditions": [
      "Àlọ́ o! Àlọ̀! Ìjàpá tìrókò ọlọ́gbọ́n ẹ̀wẹ́.",
      "Àlọ́ kì í dákẹ́ tí kò bá kọ́ni lẹ́kọ̀ọ́."
    ],
    "diaspora_connections": "Directly influenced the Uncle Remus / Br'er Rabbit trickster tales in the American South and Caribbean Anansi stories.",
    "geographical_origin": "Pan-Yorùbá rural and urban towns.",
    "media_production_notes": "Children gathered around an elder under a star-filled African night, clapping hands during chorus songs."
  },
  {
    "id": "Ìtàn",
    "title": "Ìtàn",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "chronicles",
      "historical accounts",
      "historical narrative",
      "history",
      "itan",
      "legends",
      "myths",
      "oral history"
    ],
    "description": "The authoritative historical chronicles, dynastic chronicles, and collective memory preserved by royal historians (Arokin) and lineage elders.",
    "sub_variants": [
      "Ìtàn Àdáyébá",
      "Ìtàn Ọ̀yọ́",
      "Ìtàn Ifẹ̀",
      "Ìtàn Ogun",
      "Iwe Itan"
    ],
    "historical_timeline": "Documenting centuries of imperial migrations, founding monarchs, battles, and treaties.",
    "etymology_and_philosophy": "Ìtàn (Story/History) unwinds the thread of time (Tàn: to illuminate or spread out).",
    "material_and_craftsmanship": "Preserved in memorized oral chronicles and later documented in classical literature like Rev. Samuel Johnson's History of the Yorubas.",
    "social_and_ritual_context": "Recited during coronation installation oaths to instruct new kings in constitutional boundaries.",
    "proverbs_and_oral_traditions": [
      "Ìtàn kì í parẹ́ nílé awo.",
      "Ẹni tí kò mọ ìtàn rẹ̀ á dabi ẹni tí kò ní orírun."
    ],
    "diaspora_connections": "Historical narratives kept alive in transatlantic Cabildo archives and elder memories in the Americas.",
    "geographical_origin": "Ọ̀yọ́-Ilé, Ilé-Ifẹ̀, Ìjẹ̀bú, Òwò.",
    "media_production_notes": "Portray the royal palace historian (Arokin) narrating ancient chronicles with rhythmic authority."
  },
  {
    "id": "Ère",
    "title": "Ère",
    "category": "Visual Arts, Sculpture & Guild Metallurgy",
    "aliases": [
      "carving",
      "ere",
      "ere ibeji",
      "figurine",
      "sculpted figure",
      "sculpture",
      "statue",
      "wood sculpture"
    ],
    "description": "Indigenous figurative sculpture, carved wooden memorial statues, twin statuettes (Ère Ìbejì), and shrine figures capturing spiritual essence.",
    "sub_variants": [
      "Ère Ìbejì",
      "Ère Ẹlẹ́gbára",
      "Ère Òrìṣà",
      "Ère Arúgbá",
      "Ère Ṣàngó"
    ],
    "historical_timeline": "Celebrated in the world's premier art museums as archetypes of classical African sculpture.",
    "etymology_and_philosophy": "Sculpture visualizes the unseen spiritual world, presenting balanced proportions (Ìwọ̀ntúnwọ̀nsì).",
    "material_and_craftsmanship": "Dense hardwoods carved with chisels, anointed with camwood paste (Osùn), palm oil, and adorned with beads.",
    "social_and_ritual_context": "Ère Ìbejì are cared for as living twin spirits; washed, fed, and clothed by loving mothers.",
    "proverbs_and_oral_traditions": [
      "Ère tó mọ ojú awo kì í bẹ̀rù.",
      "Ẹni tó ní ère ń bọ̀wọ̀ fún ẹ̀mí."
    ],
    "diaspora_connections": "Twin sculptures and altar figures remain central in Cuban and Brazilian African-heritage shrines.",
    "geographical_origin": "Pan-Yorùbá.",
    "media_production_notes": "Show the rich reddish camwood patina and glowing blue glass bead strands adorning the smooth wood sculpture."
  },
  {
    "id": "Oúnjẹ",
    "title": "Oúnjẹ",
    "category": "Culinary Arts & Indigenous Gastronomy",
    "aliases": [
      "amala",
      "cuisine",
      "dishes",
      "food",
      "gastronomy",
      "iyan",
      "meals",
      "odo",
      "olo",
      "ounje",
      "pounded yam",
      "traditional food"
    ],
    "description": "Traditional culinary arts, indigenous gastronomy, dietary heritage, and food processing implements (Mortar Odó, Grinding Stone Ọlọ́, Calabash Igbá).",
    "sub_variants": [
      "Iyán",
      "Àmàlà",
      "Ẹ̀bà",
      "Àkàrà",
      "Mọ́yìn-mọ́yìn",
      "Gbẹ̀gị̀rị́",
      "Ewedu",
      "Ẹ̀wà",
      "Odó",
      "Ọlọ́",
      "Igbá"
    ],
    "historical_timeline": "Yam and grain gastronomy refined across millennia of agricultural and culinary invention.",
    "etymology_and_philosophy": "Oúnjẹ (Ohun tí a ń jẹ: That which we eat). Nourishes both physical vitality and social camaraderie.",
    "material_and_craftsmanship": "Processed in hardwood mortars (Odó) with heavy pestles (Omoró) or ground on granite stones (Ọlọ́).",
    "social_and_ritual_context": "Shared eating signifies communal solidarity; specific foods consecrated to deities (Iyán to Ọbàtálá, Àmàlà to Ṣàngó).",
    "proverbs_and_oral_traditions": [
      "Iyán lónjẹ, ọkà lòògùn, àìrí rí la ń jẹ̀bà.",
      "Oúnjẹ kì í mọ orí olóko."
    ],
    "diaspora_connections": "Foundation of Afro-Caribbean cuisine (fufu, callaloo, mofongo) and Afro-Brazilian acarajé.",
    "geographical_origin": "Pan-Yorùbá culinary centers.",
    "media_production_notes": "Show the rhythmic pounding of steaming yam in a deep wooden mortar and piping-hot soup steaming in clay bowls."
  },
  {
    "id": "Ewé",
    "title": "Ewé",
    "category": "Sacred Botany, Flora & Herbal Medicine",
    "aliases": [
      "botany",
      "ewe",
      "ewe akoko",
      "flora",
      "herbs",
      "leaves",
      "medicinal leaves",
      "osanyin",
      "plants",
      "sacred herbs"
    ],
    "description": "Sacred botanical flora, medicinal leaves, and spiritual herbs possessing active chemical and metaphysical curative powers under Ọ̀sanyìn.",
    "sub_variants": [
      "Ewé Àkòko",
      "Ewé Ọ̀dúndún",
      "Ewé Tẹ̀tẹ̀",
      "Ewé Èrù",
      "Ewé Ọ̀ṣẹ́tu",
      "Ewé Ìyá",
      "Ewé Ṣawọ̀rọ̀pẹ̀pẹ̀"
    ],
    "historical_timeline": "Herbal pharmacopeia established through thousands of years of empirical botanical practice.",
    "etymology_and_philosophy": "Kò sí ewé tí kò ní iṣẹ́ tirẹ̀ (There is no leaf without its specific mission and medicinal property).",
    "material_and_craftsmanship": "Freshly gathered in rainforest groves at dawn; prepared as teas, powders, poultices, and soaps.",
    "social_and_ritual_context": "Ewé Àkòko placed on the head of newly installed chiefs; cooling leaves (Ọ̀dúndún and Tẹ̀tẹ̀) calm troubled situations.",
    "proverbs_and_oral_traditions": [
      "Kò sí ewé tí kò ní iṣẹ́ tirẹ̀.",
      "Ewé tó mọ orí Ọba kì í ṣubú."
    ],
    "diaspora_connections": "Essential knowledge preserved in Cuban Osainistas and Brazilian Candomblé Babalossanys (Masters of Leaves).",
    "geographical_origin": "Pan-Yorùbá botanical zones.",
    "media_production_notes": "Close-up of fresh green dew-covered leaves plucked in morning light for anointing ceremonies."
  },
  {
    "id": "Obì",
    "title": "Obì",
    "category": "Sacred Botany, Flora & Herbal Medicine",
    "aliases": [
      "covenant",
      "kola",
      "kola nut",
      "kolanut",
      "obi",
      "obi abata",
      "obi gbanja",
      "sacred kolanut"
    ],
    "description": "The sacred kola nut (Cola acuminata), the indispensable seed of hospitality, covenant, prayer, divination, and social reconciliation.",
    "sub_variants": [
      "Obì Àbàtà (4-lobe Sacred)",
      "Obì Gbànja (2-lobe Commercial)",
      "Atare (Alligator Pepper)",
      "Orógbó (Bitter Kola)"
    ],
    "historical_timeline": "Universal covenant token of West Africa traded across ancient trans-Saharan routes.",
    "etymology_and_philosophy": "Obì brings life, wards off harm, and opens communion between mortals and ancestors.",
    "material_and_craftsmanship": "Split into its natural 4 or 5 lobes and cast into water or onto a mat to divine yes/no answers (Aláàfíà, Ẹ̀jẹ́fẹ́).",
    "social_and_ritual_context": "Presented to every visiting guest; split and shared at weddings, naming ceremonies, and deity shrines.",
    "proverbs_and_oral_traditions": [
      "Obì kì í bínú sínú àwo.",
      "Ẹni tó mú obì wá, ó mú ẹ̀mí wá."
    ],
    "diaspora_connections": "Universal divination tool in Cuban Santería (Coco / Obi Abata) and Candomblé ceremonies.",
    "geographical_origin": "Pan-Yorùbá kola belts.",
    "media_production_notes": "Show elder holding fresh deep-red four-lobed kola nut, breaking it cleanly by hand and whispering blessings."
  },
  {
    "id": "Ìpínlẹ̀",
    "title": "Ìpínlẹ̀",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "geopolitical zone",
      "homeland",
      "ipinle",
      "province",
      "provinces",
      "region",
      "state",
      "states",
      "territory"
    ],
    "description": "The sovereign administrative territory, province, or modern geopolitical state encompassing the historical kingdoms, confederacies, and urban polities of Yorùbá civilization.",
    "sub_variants": [
      "Ìpínlẹ̀ Ògùn",
      "Ìpínlẹ̀ Ọ̀yọ́",
      "Ìpínlẹ̀ Ọ̀ṣun",
      "Ìpínlẹ̀ Èkìtì",
      "Ìpínlẹ̀ Òndó",
      "Ìpínlẹ̀ Èkó",
      "Ìpínlẹ̀ Kwara",
      "Ìpínlẹ̀ Kogi"
    ],
    "historical_timeline": "From pre-colonial provincial kingdoms (Ẹ̀gbá, Ìjẹ̀bú, Ọ̀yọ́, Èkìtì-Parapọ̀, Ìjẹ̀ṣà) through Western Region (1951-1967) to modern federal state formations.",
    "etymology_and_philosophy": "Ìpínlẹ̀ originates from 'pín' (to divide/demarcate) and 'ilẹ̀' (land/earth) — literally, a consecrated provincial jurisdiction or territorial demarcated realm.",
    "material_and_craftsmanship": "Cartographic boundaries, state secretariats, monument landmarks, civic capitals, and palace administrative seats.",
    "social_and_ritual_context": "Federated civil governance, state festivals, council of Obas and chiefs, and civic cultural commissions.",
    "proverbs_and_oral_traditions": [
      "Ilẹ̀ la ń bọ̀, a kì í foju di ilẹ̀.",
      "Ilé la ti ń kọ́ ẹ̀ṣọ́ ròde."
    ],
    "diaspora_connections": "Yorùbá state diasporic federations across North America, the UK, Brazil, Cuba, and worldwide socio-cultural associations.",
    "geographical_origin": "Yorùbáland (Southwestern and North-Central Nigeria).",
    "media_production_notes": "Cinematic visual showcases historical provincial landmarks, regional topography, and capital city skylines."
  },
  {
    "id": "Ìpínlẹ̀ Ògùn",
    "title": "Ìpínlẹ̀ Ògùn",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "abeokuta",
      "gateway state",
      "ijebu",
      "ipinle ogun",
      "ogun",
      "ogun state",
      "remo",
      "yewa"
    ],
    "description": "The historic southwestern Yorùbá state named after the sacred Ògùn River, comprising the historical sub-ethnic kingdoms of Ẹ̀gbá, Ìjẹ̀bú, Rẹ́mọ, and Yéwa/Ẹgbádò.",
    "sub_variants": [
      "Abẹ́òkúta",
      "Ìjẹ̀bú-Òde",
      "Ṣagamu",
      "Iláro",
      "Odò Ògùn",
      "Olúmọ Rock",
      "Sungbo Eredo"
    ],
    "historical_timeline": "Created in 1976 from the Western State; birthplace of classical Ẹ̀gbá independence, Ìjẹ̀bú kingdom, and preeminent national pioneers.",
    "etymology_and_philosophy": "Named after Odò Ògùn (the sacred river associated with Ògún). Popularly celebrated as the Gateway State.",
    "material_and_craftsmanship": "Renowned for Adirẹ indigo resist dyeing (Itoku, Abeokuta), Kemta woodcarving, and bronze metallurgy.",
    "social_and_ritual_context": "Center of Olúmọ Rock refuge celebrations, Lisabi festival, Ojúde Ọba pageantry, and Agemo festivals.",
    "proverbs_and_oral_traditions": [
      "Abẹ́òkúta ìlú Ẹ̀gbá, ibi Olúmọ gbé dábòbò wa."
    ],
    "diaspora_connections": "Ancestral homeland of transatlantic returnees (Saros) and Brazilian repatriates who shaped West African renaissance.",
    "geographical_origin": "Southwestern Nigeria (Ogun State).",
    "media_production_notes": "Feature Olúmọ Rock granite crest, Itoku Adirẹ dyers, and the historic Ògùn riverbank."
  },
  {
    "id": "Ìpínlẹ̀ Ọ̀yọ́",
    "title": "Ìpínlẹ̀ Ọ̀yọ́",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "ibadan",
      "ipinle oyo",
      "iseyin",
      "ogbomoso",
      "oyo",
      "oyo state",
      "oyo-ile",
      "pace setter state"
    ],
    "description": "The imperial heartland of the legendary Ọ̀yọ́ Empire and home to Ìbàdàn, the largest pre-colonial indigenous city in tropical Africa.",
    "sub_variants": [
      "Ìbàdàn",
      "Ọ̀yọ́",
      "Ògbómọ̀ṣọ́",
      "Ìṣẹ́yìn",
      "Ṣaki",
      "Ọ̀yọ́-Ilé"
    ],
    "historical_timeline": "Seat of the Alaafin of Oyo and the military titan Ìbàdàn empire of the 19th century; first capital of the Western Region.",
    "etymology_and_philosophy": "Named after the historic Ọ̀yọ́ Empire founded by Ọ̀rànmíyàn. Celebrated as the 'Pace Setter State'.",
    "material_and_craftsmanship": "Master Aṣọ-Òkè handloom weaving (Ìṣẹ́yìn), calabash carving, and wrought iron craftsmanship.",
    "social_and_ritual_context": "Home of the Alaafin of Oyo, the Olubadan of Ibadan, the Soun of Ogbomoso, and Oke-Badan festivals.",
    "proverbs_and_oral_traditions": [
      "Ọ̀yọ́ kì í ṣe ilé ẹnikẹ́ni, Ọ̀yọ́ ilé Aláàfin ni."
    ],
    "diaspora_connections": "Source of foundational Lucumí and Ketu rituals in the Americas; Ọ̀yọ́ language forms the basis of Standard Yorùbá.",
    "geographical_origin": "Southwestern Nigeria (Oyo State).",
    "media_production_notes": "Contrast the monumental Bower Tower / Mapo Hall architecture with ancient Ọ̀yọ́ royal palace courtyards."
  },
  {
    "id": "Ìpínlẹ̀ Ọ̀ṣun",
    "title": "Ìpínlẹ̀ Ọ̀ṣun",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "ede",
      "ile-ife",
      "ilesa",
      "ipinle osun",
      "osogbo",
      "osun",
      "osun state",
      "state of the living spring"
    ],
    "description": "The spiritual cradle of Yorùbá civilization at Ilé-Ifẹ̀ and home of the UNESCO World Heritage Òṣun-Òṣogbo Sacred Grove.",
    "sub_variants": [
      "Ilé-Ifẹ̀",
      "Òṣogbo",
      "Iléṣà",
      "Edẹ",
      "Ìlá-Ọ̀ràngún",
      "Odò Ọ̀ṣun"
    ],
    "historical_timeline": "Homeland of Odùduwà's classical descent at Ilé-Ifẹ̀ (dating to 8th century antiquity) and the heroic Ìjẹ̀ṣà warriors.",
    "etymology_and_philosophy": "Named after the life-giving goddess and river Òṣun. Designated as the 'Land of Virtue' (Ìpínlẹ̀ Ọmọlúàbí).",
    "material_and_craftsmanship": "Classical Ifẹ̀ naturalistic bronze and terracotta casting, Osogbo sacred art movement, and beadwork.",
    "social_and_ritual_context": "World-famous Òṣun-Òṣogbo festival, Olojo festival of the Ọ̀ọ̀ni of Ifẹ̀, and Iwude Ijesa pageantry.",
    "proverbs_and_oral_traditions": [
      "Ilé-Ifẹ̀ orírun ayé, ibi ojúmọ́ ti mọ́ wá."
    ],
    "diaspora_connections": "Universal spiritual motherland for millions of Yorùbá practitioners in Brazil, Cuba, Trinidad, and the United States.",
    "geographical_origin": "Southwestern Nigeria (Osun State).",
    "media_production_notes": "Show the mystical bronze bust of Olókun, Orí Olókun at Ifẹ̀, and the canopy over Òṣun-Òṣogbo Sacred River."
  },
  {
    "id": "Ìpínlẹ̀ Èkìtì",
    "title": "Ìpínlẹ̀ Èkìtì",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "ado-ekiti",
      "ekiti",
      "ekiti state",
      "ijero",
      "ikogosi",
      "ikole",
      "ipinle ekiti",
      "land of honour"
    ],
    "description": "The picturesque highland domain of rolling hills, ancient royal kingdoms, heroic federations (Èkìtì-Parapọ̀), and Ikogosi warm springs.",
    "sub_variants": [
      "Adó-Èkìtì",
      "Ìkọ̀lé-Èkìtì",
      "Ìjẹ̀rò-Èkìtì",
      "Ìkògòsì Warm Springs",
      "Òkè Èkìtì"
    ],
    "historical_timeline": "Formed the historic 19th-century Èkìtì-Parapọ̀ military confederacy led by Balógun Ọgẹdẹ́ngbé to liberate the eastern kingdoms.",
    "etymology_and_philosophy": "Èkìtì derives from 'Okìtì' (rugged hill, mound or mountainous elevation). Known as the 'Land of Honour and Integrity'.",
    "material_and_craftsmanship": "Hardwood architectural palace post carving (Olowe of Ise school), handwoven mats, and pottery.",
    "social_and_ritual_context": "Traditional yam festival (Odun Ijesu), sacred Ogun festivals, and regional council of Pelupelu Obas.",
    "proverbs_and_oral_traditions": [
      "Èkìtì a pọ̀ lórí, a kì í fẹnu bù."
    ],
    "diaspora_connections": "Renowned for producing foundational academic scholars and cultural preservationists throughout the diaspora.",
    "geographical_origin": "Southwestern Nigeria (Ekiti State).",
    "media_production_notes": "Show lush undulating granite hills, carved palace verandas of Ìṣẹ̀-Èkìtì, and the confluent warm/cold waters of Ikogosi."
  },
  {
    "id": "Ìpínlẹ̀ Òndó",
    "title": "Ìpínlẹ̀ Òndó",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "akure",
      "ikare",
      "ilaje",
      "ipinle ondo",
      "ondo",
      "ondo state",
      "owo",
      "sunshine state"
    ],
    "description": "The coastal and rainforest state encompassing the classical artistic kingdom of Òwò, the ancient Ọ̀ṣẹ́màwé dynasty, and the coastal Ìlàjẹ waters.",
    "sub_variants": [
      "Akúrẹ́",
      "Òwò",
      "Òndó Town",
      "Ìkàrẹ́-Àkókó",
      "Ìlàjẹ",
      "Idanre Hills"
    ],
    "historical_timeline": "Dating to medieval Òwò court arts (14th century), the Deji of Akure realm, and the impregnable mountaintop kingdom of Idanre.",
    "etymology_and_philosophy": "Named after ancient Òndó ('Edo ndo' - settlers of the hills). Celebrated as the 'Sunshine State'.",
    "material_and_craftsmanship": "World-renowned Òwò ivory carving and bronze casting, Idanre rock architecture, and timber/cocoa production.",
    "social_and_ritual_context": "Igogo festival of Owo, Odun Oba in Akure, and the marine traditions of the coastal Ilaje and Ikale.",
    "proverbs_and_oral_traditions": [
      "Òndó omo a kéré jẹ, a fẹ́jù fẹ́jù gba oyè."
    ],
    "diaspora_connections": "Preserves deep linguistic and artistic connections with the Benin/Edo realm and international African art collections.",
    "geographical_origin": "Southwestern Nigeria (Ondo State).",
    "media_production_notes": "Show the magnificent rock-hewn steps of Òkè Ìdànrè and the beaded royal regalia of the Ọ̀ṣẹ́màwé and Olowo."
  },
  {
    "id": "Ìpínlẹ̀ Èkó",
    "title": "Ìpínlẹ̀ Èkó",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "badagry",
      "centre of excellence",
      "eko",
      "epe",
      "ikorodu",
      "ipinle eko",
      "isale eko",
      "lagos",
      "lagos state"
    ],
    "description": "The metropolitan coastal powerhouse, historic island monarchy (Ọba of Lagos), center of maritime commerce, and preeminent cultural metropolis.",
    "sub_variants": [
      "Èkó",
      "Ìsàlẹ̀ Èkó",
      "Badagry",
      "Ìkòròdú",
      "Ẹpẹ",
      "Ìkòyí",
      "Victoria Island"
    ],
    "historical_timeline": "From Awori settlement at Ìdúngànran and the Oba of Lagos dynasty, through colonial treaty of 1861, to Africa's largest economic hub.",
    "etymology_and_philosophy": "Èkó originates from the military war camp (Oko/Èkó) of pre-colonial times. Designated the 'Centre of Excellence'.",
    "material_and_craftsmanship": "Maritime shipbuilding, coastal net weaving, Brazilian quarter architecture, and modern creative industry.",
    "social_and_ritual_context": "The sacred Adamu Orisha (Èyọ̀) Play, Gèlèdẹ́ festivals, and the coronation rituals of Ọba Èkó at Iga Idunganran.",
    "proverbs_and_oral_traditions": [
      "Èkó gbóle o gbọ́lẹ, o fi ọmọ lówó o fi ọmọ lẹ́kọ̀ọ́."
    ],
    "diaspora_connections": "Global gateway of return for African-Americans and Afro-Brazilians; world capital of Afrobeats and contemporary Yorùbá cinema.",
    "geographical_origin": "Southwestern Nigeria (Lagos State).",
    "media_production_notes": "Juxtapose the pristine white robes and tall staves of Èyọ̀ masquerades against the Atlantic lagoon shoreline."
  },
  {
    "id": "Ìpínlẹ̀ Kwara",
    "title": "Ìpínlẹ̀ Kwara",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "igbomina",
      "ilorin",
      "ipinle kwara",
      "kwara",
      "kwara state",
      "offa",
      "omu-aran",
      "oro",
      "state of harmony"
    ],
    "description": "The north-central bridgehead of Yorùbá civilization encompassing the ancient frontier kingdoms of Ìgbómìnà, Ọ̀fà, and the historic emirate city of Ìlọrin.",
    "sub_variants": [
      "Ìlọrin",
      "Ọ̀fà",
      "Òmù-Àrán",
      "Orò",
      "Ìgbómìnà",
      "Èsìẹ́"
    ],
    "historical_timeline": "Homeland of Afonja, ancient Ìgbómìnà federations, heroic Ọ̀fà resistance, and the mystical stone figures of Èsìẹ́.",
    "etymology_and_philosophy": "Kwara was derived from the indigenous name for the River Niger. Celebrated as the 'State of Harmony'.",
    "material_and_craftsmanship": "Èsìẹ́ ancient soapstone carvings (the largest collection in Africa), Aṣọ-Òkè weaving, and traditional pottery (Dada, Ilorin).",
    "social_and_ritual_context": "Durbar festival of Ilorin, Ijakadi festival of Offa, and ancient Oro cultural assemblies.",
    "proverbs_and_oral_traditions": [
      "Ìlọrin afọ́njá, ilé kò gbẹkùn, a fẹ́jù fẹ́jù kẹ́gbẹ́."
    ],
    "diaspora_connections": "Cultural nexus connecting northern trans-Saharan trade routes with southern forest Yorùbá civilization.",
    "geographical_origin": "North-Central Nigeria (Kwara State).",
    "media_production_notes": "Capture the enigmatic Èsìẹ́ soapstone figures, handlooms of Omu-Aran, and equestrian pageantry of Ilorin."
  },
  {
    "id": "Ìpínlẹ̀ Kogi",
    "title": "Ìpínlẹ̀ Kogi",
    "category": "Civilization, History & Civic Heritage",
    "aliases": [
      "confluence state",
      "ijumu",
      "ipinle kogi",
      "kabba",
      "kogi state",
      "okun",
      "okun land",
      "yagba"
    ],
    "description": "The eastern confluence territory comprising the Òkun-Yorùbá kingdoms of Kàbbà, Ìjùmú, Yàgbà, Ọwẹ, and Bùnú, preserving archaic linguistic forms.",
    "sub_variants": [
      "Kàbbà",
      "Ìjùmú",
      "Yàgbà",
      "Bùnú",
      "Ọwẹ",
      "Lokoja Confluence"
    ],
    "historical_timeline": "Homeland of Òkun resistance against 19th-century Nupe-Fulani incursions and preservation of classical Yorùbá dialects.",
    "etymology_and_philosophy": "Òkun represents the classical daily greeting of mutual solidarity and wellness among the eastern Yorùbá clans.",
    "material_and_craftsmanship": "Ancient weaving (Aṣọ Ìpàpọ̀), blacksmithing, mountain cave architecture, and coffee/yam agriculture.",
    "social_and_ritual_context": "Obaro of Kabba court ceremonies, ancestral masquerades, and regional harvest festivals.",
    "proverbs_and_oral_traditions": [
      "Òkun kò ṣeé dá mọ́ra, ẹni tí a bá rí la ń kí."
    ],
    "diaspora_connections": "Recognized by global linguists as preserving the oldest tonal phonemes and dialectal root words of proto-Yorùbá.",
    "geographical_origin": "North-Central Nigeria (Kogi State / Okunland).",
    "media_production_notes": "Show the majestic confluence of Rivers Niger and Benue, and highland mountain redoubts of Okun warriors."
  }
]

def ingest_master_parents():
    targets = [
        Path("/home/aruna_olanrewaju/agba-engine/web/src/data/yoruba_master_corpus.json"),
        Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_web/src/data/yoruba_master_corpus.json"),
        Path("/home/aruna_olanrewaju/agba-engine/api/data/yoruba_corpus_1007_NORMALIZED.json"),
        Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine/agba_enterprise_api/data/yoruba_corpus_1007_NORMALIZED.json")
    ]

    print("🚀 [ÀGBÀ INGESTION] Starting Sovereign Parents & Ìpínlẹ̀ Ingestion...", flush=True)
    print(f"📊 Total Sovereign Entries to Ingest: {len(PARENTS_DATA)}", flush=True)

    for target_path in targets:
        if not target_path.exists():
            print(f"⚠️ Target does not exist, skipping: {target_path}", flush=True)
            continue

        print(f"\n📁 Processing Target File: {target_path}", flush=True)
        try:
            with open(target_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Failed to read {target_path}: {e}", flush=True)
            continue

        entities = list(data.values()) if isinstance(data, dict) else list(data)
        entity_map = {e.get("title"): e for e in entities if e.get("title")}
        initial_count = len(entities)

        added = 0
        updated = 0

        for p in PARENTS_DATA:
            title = p["title"]
            record = {
                "id": p["id"],
                "title": p["title"],
                "culture": "Yorùbá",
                "category": p["category"],
                "is_parent": True,
                "aliases": [a.lower().strip() for a in p.get("aliases", [])],
                "description": p.get("description", ""),
                "sub_variants": p.get("sub_variants", []),
                "historical_timeline": p.get("historical_timeline", ""),
                "etymology_and_philosophy": p.get("etymology_and_philosophy", ""),
                "material_and_craftsmanship": p.get("material_and_craftsmanship", ""),
                "social_and_ritual_context": p.get("social_and_ritual_context", ""),
                "proverbs_and_oral_traditions": p.get("proverbs_and_oral_traditions", []),
                "diaspora_connections": p.get("diaspora_connections", ""),
                "geographical_origin": p.get("geographical_origin", ""),
                "media_production_notes": p.get("media_production_notes", ""),
                "details": {
                    "description": p.get("description", ""),
                    "historical_timeline": p.get("historical_timeline", ""),
                    "etymology_and_philosophy": p.get("etymology_and_philosophy", ""),
                    "material_and_craftsmanship": p.get("material_and_craftsmanship", ""),
                    "social_and_ritual_context": p.get("social_and_ritual_context", ""),
                    "proverbs_and_oral_traditions": p.get("proverbs_and_oral_traditions", []),
                    "diaspora_connections": p.get("diaspora_connections", ""),
                    "geographical_origin": p.get("geographical_origin", ""),
                    "media_production_notes": p.get("media_production_notes", "")
                }
            }

            if title in entity_map:
                existing = entity_map[title]
                existing.update(record)
                updated += 1
            else:
                entities.insert(0, record)
                entity_map[title] = record
                added += 1

        # Cleanse Ògún deity aliases to exclude warfare
        if "Ògún" in entity_map:
            ogun_deity = entity_map["Ògún"]
            cleaned = [a for a in ogun_deity.get("aliases", []) if a not in ["war", "warfare", "military", "battle"]]
            if "ògún" not in cleaned:
                cleaned.insert(0, "ògún")
            ogun_deity["aliases"] = cleaned

        # Write to temporary file then atomic rename
        temp_file = target_path.with_name(target_path.stem + "_temp.json")
        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(entities, f, ensure_ascii=False, indent=2)
            temp_file.replace(target_path)
            print(f"✅ Ingestion successful for {target_path.name}:", flush=True)
            print(f"   • Initial count: {initial_count}", flush=True)
            print(f"   • Parents Added: {added}", flush=True)
            print(f"   • Parents Updated: {updated}", flush=True)
            print(f"   • Final Count: {len(entities)}", flush=True)
        except Exception as e:
            print(f"❌ Failed to write {target_path}: {e}", flush=True)

    print("\n🎉 ALL TARGET CORPUS FILES INGESTED AND SAVED TO DISK SUCCESSFULLY!", flush=True)

if __name__ == "__main__":
    ingest_master_parents()
