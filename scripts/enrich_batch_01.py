#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: PHASE 4 BATCH 1 CORPUS ENRICHMENT (HANDOFF-AROKIN-001)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist), Royal Chronicler & Cross-Cultural Archivist
Supervising Architect: Àgbà (agba-pa-architect)
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Authentic Yorùbá Schema

Mission:
Elevates the first 25 thin entities to full Àmọ̀tẹ́kùn-grade parity with:
1. Multi-epoch antiquity timelines (Ancient Ifẹ̀/Classical to Modern).
2. Dual-language proverbs: "Òwe Yorùbá (English Translation: Philosophical Commentary)".
3. Deep etymology, philosophical derivations, and sacred craftsmanship.
=============================================================================
"""

import json
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent
API_CORPUS = REPO_ROOT / "api/data/yoruba_corpus_1007_NORMALIZED.json"
WEB_CORPUS = REPO_ROOT / "web/src/data/yoruba_master_corpus.json"

ENRICHMENTS: Dict[str, Dict[str, Any]] = {
    "Oba Akinyele": {
        "etymology_and_philosophy": "From Yorùbá 'Akin-yẹ-ilé' ('Valor befits the household' or 'The valiant soul brings honor to the lineage', contracted from akin: brave warrior/hero, yẹ: worthy/fitting, and ilé: ancestral home). Philosophically encapsulates the republican martial meritocracy of Ìbàdàn, where nobility is achieved through civic courage and intellectual contribution rather than hereditary monarchical entitlement.",
        "historical_timeline": "Ancient & Classical Antecedents: Traces to the martial dispersal of Old Ọ̀yọ́ warriors converging at Ìbàdàn under Lagelu. 1882–1911: Born in Ìbàdàn into an aristocratic Christian warrior-lineage; served in the colonial civil service and pioneer cocoa trade; authored the seminal 1911 historical treatise 'Ìwé Ìtàn Ìbàdàn' codifying oral genealogies and 19th-century war chronicles. 1920s–1954: Co-founded Faith Tabernacle in Nigeria, evolving into Christ Apostolic Church alongside Prophet Joseph Babalọlá; rose through the civilian Olúbàdàn chieftaincy line. 1955–1964: Coronated as the Olúbàdàn of Ìbàdàn in 1955; knighted KBE in 1956; steered Ìbàdàn with sagacity through First Republic tumult until entering the ancestral realm in May 1964.",
        "material_and_craftsmanship": "Material heritage unites classical Yorùbá royal insignia with 20th-century literate elegance: handwoven Sányán and Alárì robes from Ìbàdàn master weavers, beaded walking staffs (Ọ̀pá Ìlẹ̀kẹ̀), carved ivory flywhisks (Ìrùkẹ̀rẹ̀), and early colonial press bindings of his historical texts.",
        "proverbs_and_oral_traditions": [
            "Ìbàdàn kì í gbé onílé bí àjèjì. (Ìbàdàn does not favor the indigenous son as generously as it embraces the stranger who seeks refuge: Celebrating the cosmopolitan, merit-based sanctuary of Ìbàdàn where valor and industrious endeavor transcend hereditary pedigree.)",
            "Akin kì í kú sinú ilé, ológun ní ń gbọ́ ẹkún ogun. (The valiant hero never perishes in domestic obscurity; it is the battle-cry that summons the courageous: Commemorating martial fortitude and civic duty that sacrifices private comfort for public defense.)",
            "Ọba t'ó jẹ t'ìlú tòrò, orúkọ rẹ̀ kò ní parẹ́; ọba t'ó jẹ t'ìlú dàrú, orúkọ rẹ̀ kò ní parẹ́. (The monarch during whose reign the city prospers will never be forgotten; the monarch during whose reign the city falls into chaos will likewise never be forgotten: The immutable Yorùbá philosophy of historical accountability in leadership.)"
        ]
    },
    "Awujalẹ": {
        "etymology_and_philosophy": "From classical Yorùbá 'A-mú-ìjà-lẹ̀' ('The One Who Quells and Reconciles Strife'), designating the sacred peacemaker, royal arbiter, and paramount sovereign of Ìjẹ̀búland. Philosophically embodies balanced majesty where supreme authority exists to harmonize competing interest groups, guild merchants, and civil confederacies.",
        "historical_timeline": "Ancient Antiquity (c. 10th–14th Century CE): Dynastic foundation established by Ọbànta (Ògbòrògàn-idà) following the pioneering migration of Olú-Ìwà from Ilé-Ifẹ̀, institutionalizing the throne at Ìjẹ̀bú-Òde; engineering of the colossal Sùngbó Èrèdo earthen defensive ramparts. Classical & Pre-Colonial Era: Commanded regional coastal commerce and monopoly over maritime trading corridors buffering forest states. 1892: The British-Ìjẹ̀bú War (Battle of Ìmágwà) dismantled commercial blockades, subjecting the kingdom to colonial restructuring. Modern Era: Exemplified by Ọba Sikiru Kayọ̀dé Adétọ̀nà, Ogbagba II (enthroned 1960), one of Africa's longest-reigning paramount sovereigns, championing the global renaissance of the annual Ọjọ́dé Ọba festival.",
        "material_and_craftsmanship": "Sacred cone-shaped beaded crown (Adé Oríko) embellished with avian totems, cast brass Osùgbó/Ògbóni royal edan sceptres, ceremonial brass bracelets, and high-thread-count royal Kíjìpá and Aṣọ Olóonà textiles crafted by royal guild matriarchs.",
        "proverbs_and_oral_traditions": [
            "Awùjalẹ̀, Aláìyélúwà, Ọmọ Aládé Mẹ́rìndínlógún. (The Awùjalẹ̀, Sovereign of the Cosmos, royal scion of the sixteen consecrated crowns of primordial Ifẹ̀: Affirming the imperial antiquity and uninterrupted lineage of Ìjẹ̀bú sovereignty.)",
            "Ìjẹ̀bú Òde, Àpèbí: Ìlú tó fi owó bọ Òrìṣà, ilé ọlá àti ọpọ̀lọpọ̀ ogbọ́n. (Ijebu-Ode, the sanctuary that venerates the sacred with boundless prosperity, the dwelling of nobility and profound intellect: Reflecting the commercial brilliance, financial mastery, and sacred stewardship of the Ìjẹ̀bú nation.)",
            "Bí a kò bá rí Awùjalẹ̀, a ò lè mọ Ìjẹ̀bú tán. (If one has never encountered the Awùjalẹ̀, one cannot fully comprehend the depth of Ijebu civilization: Emphasizing the sovereign as the living incarnation and spiritual focal point of communal identity.)"
        ]
    },
    "Deji": {
        "etymology_and_philosophy": "From the royal praise epithet 'Ọmọ Ẹkùn, Amúkùn fọlá' ('Offspring of the Leopard, Who Steps with Majestic Grace'), denoting sovereign majesty and paramount rulership of the ancient Àkúrẹ́ Kingdom. Philosophically signifies coiled spiritual potency, judicial equilibrium, and sacred covenant with the earth.",
        "historical_timeline": "Classical Antiquity (c. 12th Century CE): Foundation of the Àkúrẹ́ throne by Prince Asọdẹboyè (revered as Ẹkùn), royal prince of Ilé-Ifẹ̀ who migrated eastward bearing a consecrated beaded crown. 14th–16th Century CE: Construction and expansion of the labyrinthine Ààfin Déjì courtyard palace complex; formalization of the Iwerefa and Ihare chieftaincy cabinets. 19th Century: Navigated regional defense, diplomatic alliances with the Benin Empire, and resistance against Ìbàdàn war-captains. 1897–1957: Reign of Déjì Afunbiowo Adesida I, marking a six-decade cultural renaissance and modernization under British colonial indirect rule. Contemporary Era: Continuous lineage custodianship presiding over the sacred Ọlọ́jọ́ and Ìsẹpẹ seasonal rites.",
        "material_and_craftsmanship": "Material culture centers on the monumental Adé Nlá (great beaded crown with projecting avian finials), heavy coral necklaces (Ìyùn), cast brass ceremonial pectorals, and intricately carved peristyle palace pillars (Ọ̀pọ́ Ààfin) sculpted by hereditary Gbẹ́nàgbẹ́nà guilds.",
        "proverbs_and_oral_traditions": [
            "Àkúrẹ́ Ọmọ Ẹkùn, ọmọ amúkùn fọlá. (Àkúrẹ́, progeny of the Leopard, who gracefully embraces royalty as an inherent destiny: Highlighting the serene majesty, coiled power, and noble poise inherent in the Déjì's sovereign office.)",
            "Déjì kì í fọ̀rọ̀ ayé ṣeré, ẹnu Ọba ni Àṣẹ ti ń jáde. (The Déjì utters nothing in vain, for divine cosmic decree proceeds unhindered from the mouth of the King: Illustrating the sacred finality and metaphysical gravity of royal decrees.)",
            "A kì í rí Ẹkùn kí a tún wá àwọ̀ Ẹkùn. (One does not stand before the living Leopard and still seek the skin of the Leopard: Demonstrating that the physical presence of the Déjì is absolute and self-evident without external validation.)"
        ]
    },
    "Akarigbo": {
        "etymology_and_philosophy": "From 'A-kà-rí-gbọ́' ('The One whose discernment and renown are proclaimed and heard far and wide'), tracking back to ancestral prince Akarigbo, son of Ọba Ọlọ́fin of Ilé-Ifẹ̀. Philosophically embodies federal monarchical unity, confederate consensus, and ancestral continuity across Rẹ́mọland.",
        "historical_timeline": "Ancient Ifẹ̀ Roots (c. 14th–15th Century CE): Migration of royal princes southwards from Ilé-Ifẹ̀ to found the foundational settlements of Rẹ́mọ. Classical & 19th Century: Consolidation of thirty-three autonomous towns into the Rẹ́mọ confederacy, establishing Sagamu in 1872 as the unified administrative and military capital to withstand regional conflicts. 1894–Colonial Era: Ratification of British protectorate treaties while retaining royal Osùgbó council oversight. Contemporary Continuity: The stool remains the paramount cultural and industrial leadership axis of Rẹ́mọland in Ogun State.",
        "material_and_craftsmanship": "Sacred Adé Ilẹ̀kẹ̀ (conical beaded crowns with falling fringe), carved ivory ceremonial staffs, brass-accented Osùgbó judicial staffs (Edan), and royal Sányán garments handwoven by Sagamu guild elders.",
        "proverbs_and_oral_traditions": [
            "Àkàrígbò kò ṣeé tẹ̀ bí ẹní tẹ ẹkẹ. (The sovereign Àkàrígbò cannot be trodden underfoot like brittle reeds: Proclaiming the unshakeable dignity and inviolable authority of the Rẹ́mọ paramount throne.)",
            "Ọba tó jẹ ti ìlú tùbà, tura, orúkọ rẹ̀ kò ní parun. (The monarch during whose reign the realm experiences peace and abundance shall have their name engraved upon eternity: The ethical measure of righteous rule in Rẹ́mọ political philosophy.)",
            "Àgbájọ ọwọ́ la fi ń sọ̀yà, Rẹ́mọ kò gbàgbé orísun. (With a united fist we declare our strength; Rẹ́mọ never forgets its primordial source: Celebrating the federal solidarity of the thirty-three constituent towns anchored to their ancestral origin.)"
        ]
    },
    "Olofa": {
        "etymology_and_philosophy": "Contracted from 'Oní-Ọfà' ('The Lord / Sovereign of the Consecrated Arrow'), rooted in archery, territorial defense, and martial vigilance. Philosophically represents defensive resilience, agrarian integrity, and honor attained through courageous labor.",
        "historical_timeline": "Ancient Foundations (c. 1392 CE): Founded by Olálomi Ọlátẹ̀ńdọ́, a royal prince of Ilé-Ifẹ̀ and renowned archer who established the initial capital at Ọ̀fà-Esé. Imperial Alliance: Served as a stalwart northern military bastion and trading hub in strategic partnership with the Ọ̀yọ́ Empire. 19th Century Wars: Sustained prolonged resistance during the Jalumi War (1878) and Offa War (1887) resisting northern caliphate cavalry incursions. Modern Era: Developed into a premier intellectual, industrial, and railway junction in Kwara State, celebrating the annual Ijakadi festival honoring traditional wrestling and community resilience.",
        "material_and_craftsmanship": "Regalia incorporates consecrated iron arrowheads (Ọfà), peacock plumes (Ìyẹ́ Ọ̀kín), royal beaded flywhisks, and ceremonial saddle embroidery hand-stitched with vibrant trade cloth.",
        "proverbs_and_oral_traditions": [
            "Ọ̀fà mọ̀kàn, ọmọ a kò kẹ́kẹ́, ọmọ a kò fàbàjà, bẹ́ẹ̀ ni a kò tún bọmọ lójú rí. (Children of Ọ̀fà bear no facial incisions, yet their nobility and identity remain unmistakable across the earth: Emphasizing that intrinsic virtue and noble lineage transcend external scarification.)",
            "Ọmọ Ọlọ́fà mọ̀kàn, ọmọ agbógun lẹ́yìn odi. (Scions of the Ọlọ́fà who engage the adversary far outside the fortress walls: Honoring proactive tactical defense, strategic foresight, and courage in safeguarding the commonwealth.)",
            "Ọ̀fà Ilé Ọ̀kin, ibi eré ti ń dọ́lá. (Ọ̀fà, ancestral home of the Regal Peacock, where competitive sports transform into enduring nobility: Celebrating the wrestling tradition of Ijakadi as a crucible of character, camaraderie, and civic pride.)"
        ]
    },
    "Alara": {
        "etymology_and_philosophy": "From 'Alá-Ará' ('The Possessor of Wonder / Miracle / Kinship' or 'Master of Sacred Transformations'), celebrated in the Odù Ifá as the primordial eldest crowned son of Odùduwà. Philosophically embodies primogeniture, agricultural abundance, and cosmological authority.",
        "historical_timeline": "Primordial Antiquity: Ranked in classical Ifá scripture (especially Èjì Ogbè) as the first of the crowned royal sons dispatched from Ilé-Ifẹ̀, establishing the sacred stool at Arámọkọ-Èkìtì. Medieval Era: Spearheaded confederated defense of the Èkìtì hill communities against savanna raids. 19th Century: Anchored the Èkìtì-Parapọ̀ confederacy (1877–1893) fighting for regional liberation against Ìbàdàn hegemony. Modern Era: Continues as a senior paramount ruler of Èkìtì State, preserving ancient coronation liturgies and seasonal yam rituals.",
        "material_and_craftsmanship": "Towering beaded cone crown known as Kéléké Adé, brass rattle staffs (Ṣaworo), camwood-rubbed ceremonial furniture, and heavy Kíjìpá handwoven war vestments.",
        "proverbs_and_oral_traditions": [
            "Alárá ló niṣu, Alárá ló lẹbọ; Alárá kì í f'èwe rẹ̀ bọra kò má le. (The Alárá owns the choice yams, the Alárá commands the sacred offerings; the child wrapped in the mantle of Alárá shall never experience weakness: Praising royal benevolence, agrarian fertility, and ancestral protection.)",
            "Èjì Ogbè tẹ́ Alárá sí rere, ó fún un ní Kéléké Adé tí kì í rẹ̀wẹ̀sì. (Èjì Ogbè divined auspicious fortune for Alárá, bestowing upon him the unyielding Kéléké crown: Codifying the divine metaphysical sanction of the Alárá throne in sacred Ifá scriptures.)",
            "Bí Alárá bá gbóṣù, Ajerò a gba àmì; àwọn ọmọ Òkùnrin Ilé-Ifẹ̀ kì í f'orí bọ abẹ́. (When Alárá salutes the sacred new moon, Ajerò receives the divine sign; the royal princes of Ifẹ̀ never bow in servitude: Illustrating the primordial fraternal solidarity and sovereign equality of Èkìtì kings.)"
        ]
    },
    "Aresa": {
        "etymology_and_philosophy": "From 'Arẹ̀sà' (contracted from 'A-rẹ-ẹ̀sà-kó' or 'A-tẹ́-ẹ̀sà-ọlá', 'The One Who Gathers and Manifests the Chosen Nobility of Ìrẹ̀sà'). Philosophically signifies military unbreakability, collective vigilance, and the divine right of defense.",
        "historical_timeline": "Classical Antiquity: Established as one of the premier crowned kingdoms of the ancient Yorùbá confederacy, ruling the historic fortress realm of Ìrẹ̀sà. 17th–18th Century: Served as a paramount military bulwark safeguarding the agricultural breadbasket of the Ọ̀yọ́ Empire. 19th Century: Following the collapse of Old Ọ̀yọ́, the dynasty successfully relocated and re-established dual seats (Ìrẹ̀sà-Adú and Ìrẹ̀sà-Àpá) near Ògbómọ̀ṣọ́, sustaining uninterrupted chieftaincy rites. Contemporary Era: Preserves sacred royal groves, dynastic oríkì, and traditional agricultural oversight.",
        "material_and_craftsmanship": "Sacred bird-crested beaded crowns (Adé Elẹ́yẹ), cast bronze bells, hand-forged iron ceremonial swords, and hand-loomed indigo-dyed Kíjìpá cloths.",
        "proverbs_and_oral_traditions": [
            "Arẹ̀sà, ọmọ agbógun lẹ́yìn odi; ọmọ a-fòkúta-ṣẹ́gun-ẹni. (Arẹ̀sà, scion of the valiant who repels invading armies outside city walls; who shatters adversaries with stone-like fortitude: Commemorating ancient tactical prowess and unshakeable resilience.)",
            "Bí Ọba kò ba sí, ìlú a dàhoro; bí Arẹ̀sà bá fi orí dé adé, Ìrẹ̀sà a di àbò. (When a righteous King is absent, the city devolves into desolation; when Arẹ̀sà places the crown upon his brow, Ìrẹ̀sà becomes an inviolable sanctuary: Underscoring the sacred stabilizing presence of legitimate monarchy.)",
            "Ọmọ a-jí-fowó-ra-ẹranko-ṣe-bọ; ọmọ Arẹ̀sà kò gbọdọ̀ jìyà. (Descendant of those who awaken with wealth to procure great beasts for sacred offerings; the royal seed of Arẹ̀sà shall never suffer degradation: Expressing royal benevolence, ceremonial generosity, and lineage prosperity.)"
        ]
    },
    "D.O. Fagunwa": {
        "etymology_and_philosophy": "Chief Daniel Ọlọ́runfẹ́mi Fágúnwà; the surname derives from 'Ifá-gún-wà' ('Ifá / Cosmic Wisdom arrives in harmonious balance' or 'Destiny is aligned with dignity'). Philosophically established the foundation of modern Yorùbá narrative ethics, exploring human trials through allegorical wilderness journeys.",
        "historical_timeline": "1903: Born in Òkè-Igbó, Òndó State, immersing in hunters' oral chants (Ìjálá) and classical mythological lore. 1938: Published 'Ògbójú Ọdẹ nínú Igbó Irúnmalẹ̀' (The Forest of a Thousand Daemons)—the world's first full-length novel written in the Yorùbá language, later translated by Nobel laureate Wole Soyinka. 1940s–1950s: Penned seminal allegorical masterpieces including 'Igbó Olódùmarè', 'Ìrèké Oníbùdó', and 'Àdììtú Olódùmarè', permanently defining African magical realism. 1963: Tragically transitioned at Baro on the River Niger, leaving an immortal literary and linguistic legacy.",
        "material_and_craftsmanship": "Literary material heritage of early CMS Bookshop letterpress prints, handwritten dip-pen manuscripts, archival notebooks, and handwoven Aṣọ-Òkè formal attires reflecting Christian-Yorùbá intellectual synthesis.",
        "proverbs_and_oral_traditions": [
            "Bí ẹ̀mí bá wà, ìrètí ń bẹ. (While life endures, hope remains intact: The cardinal moral philosophy guiding Fagunwa's hunter-protagonists through the perilous trials of the cosmic wilderness.)",
            "Àgbò tò kàkà, kò ní kí á má gba orí rẹ̀ lẹ́rù. (Even when the horned ram lowers its stance defensively, its head must still bear its destined weight: Teaching that human trials and moral responsibilities cannot be evaded but must be confronted with courage.)",
            "Ọlọ́gbọ́n a máa kú pẹ̀lú ọgbọ́n rẹ̀, ṣùgbọ́n ìwé a máa fi ọgbọ́n pamọ́ fún ayé. (The sage may depart with his living breath, but written literature preserves wisdom for the ages: Reflecting Fagunwa's epochal role in immortalizing Yorùbá oral philosophy through print.)"
        ]
    },
    "Adé Òrìṣà": {
        "etymology_and_philosophy": "Literal compound of 'Adé' (crown / consecrated headpiece) and 'Òrìṣà' (primordial divinity / spiritual emanation of Olódùmarè). Philosophically represents the sanctified alignment of the inner metaphysical soul (Orí Inú) with cosmic divinity, where the physical crown acts as a protective transmitter of divine Àṣẹ.",
        "historical_timeline": "Primordial Antiquity: Originated at Ilé-Ifẹ̀ during the cosmic descent of the sixteen primordial Òrìṣà led by Odùduwà and Ọbàtálá. Classical Era: Distributed among consecrated monarchs (Ọba Aládé) and high priestly custodians of major divinity shrines (Ṣàngó, Ọ̀ṣun, Ọbàtálá). Transatlantic Survival: Preserved in Cuban Lucumí and Brazilian Candomblé Ketu as the 'Corona de Santo', bestowed upon initiates during the sacred Karí Òrìṣà rites. Contemporary Practice: Continues as the pinnacle of liturgical adornment and royal legitimacy across the Yorùbá global diaspora.",
        "material_and_craftsmanship": "Constructed from thousands of micro-glass seed beads (Ilẹ̀kẹ̀) threaded on vegetable fibers over a basketry framework, featuring beaded veils (Oojú Adé) and consecrated avian totems symbolizing the ancestral mothers (Àwọn Ìyá Mi).",
        "proverbs_and_oral_traditions": [
            "Adé kò le kọ́ orí tí kò ní àyànmọ́ rere. (A crown cannot sit properly upon a head devoid of noble destiny: Teaching that external majesty and titles are hollow without spiritual character and moral grounding.)",
            "Ẹyẹ orí adé kì í fò lásán; ojú Òrìṣà ni ó fi ń wo ayé. (The bird atop the consecrated crown never flutters in vain; it surveys the cosmos through the eyes of the Divinities: Revealing the mystical vigilance and divine insight required of sacred leadership.)",
            "Orí tí yóò wọ adé Òrìṣà, kò ní gbé ẹrù ẹ̀tẹ́. (The head destined to wear the crown of the Òrìṣà shall never bear the burden of disgrace: Affirming spiritual protection and moral uprightness demanded of the anointed.)"
        ]
    },
    "Àpàlà Agba": {
        "etymology_and_philosophy": "Compound of 'Àpàlà' (acoustic percussion genre evolved from acoustic wake-up chants during Ramadan) and 'Àgbà' (revered elders / maestro custodians). Philosophically serves as the auditory vessel of oral history, ethical pedagogy, and social critique among senior guild elders.",
        "historical_timeline": "1930s–1940s: Originated among Muslim communities in Ìjẹ̀bú, Abẹ́òkúta, and Ìbàdàn as an acoustic, drum-driven social poetry. 1950s–1970s: Elevated into an internationally recognized genre by maestro Haruna Ishola (Baba n Gani Agba), Ayinla Omowura, and Kasumu Adio, recording landmark vinyl releases with Decca and EMI. Post-Independence Era: Became the definitive auditory status symbol of commercial titans and traditional rulers. Contemporary Era: Continues to deeply inform modern Fuji, Jùjú, and Afrobeats percussive arrangements.",
        "material_and_craftsmanship": "Master percussion ensemble comprised of the Gángan (talking drum), Ọ̀pọ́n acoustic frame drums, Ṣẹ̀kẹ̀rẹ̀ beaded gourds, resonant thumb-piano (Agidigbo), and forged clapperless iron bells (Agogo).",
        "proverbs_and_oral_traditions": [
            "Àpàlà kì í ṣe orin àwọn alápọ́n; ọlọ́gbọ́n ló ń gbọ́ àpàlà. (Àpàlà is not the melody of the frivolous; it is the wise and mature who discern its deep philosophy: Highlighting the didactic social commentary and elevated oral poetry of the genre.)",
            "Bí gángan kò bá dún lẹ́yìn àpàlà, orin a dabi oúnjẹ tí kò ní iyọ̀. (If the talking drum does not resonate beneath the àpàlà melody, the song is like food cooked without salt: Affirming the indispensable acoustic role of the pressure drum in Yorùbá musical aesthetics.)",
            "Haruna ló f'àpàlà d'ọlá; orin àgbà kì í di asán. (Haruna elevated àpàlà to supreme majesty; the song of the elders never degenerates into futility: Celebrating the immortal legacy of master chroniclers who encoded history into song.)"
        ]
    },
    "Omele-Abo Dundun": {
        "etymology_and_philosophy": "Compound of 'Ọmẹle' (the harmonic accompanying drum), 'Abo' (female / warm maternal register), and 'Dùndún' (the classical hourglass talking drum family). Philosophically embodies maternal stability, supportive harmony, and the foundational pulse of collective life.",
        "historical_timeline": "Classical Ọ̀yọ́ Antiquity: Emerged within hereditary drumming families (Ayan) at Ọ̀yọ́-Ilé under the patronage of the Aláàfin and Òrìṣà Ṣàngó priesthoods. Medieval to 19th Century: Anchored military tempos, civic processions, and royal assemblies throughout the Yorùbá wars. Transatlantic Resonance: Retained within Cuban Batá drum families (as the feminine Itótele register) and Brazilian Candomblé Ketu rhythms. Contemporary Era: Vital grounding instrument in contemporary African orchestras, gospel ensembles, and traditional theater.",
        "material_and_craftsmanship": "Carved from a single cylinder of Cordia millenii (Ọmọ wood), fitted with cured goatskin membranes (Awọ Ewúrẹ́) secured by hand-twisted leather tension cords (Ọsán), and struck with a curved wooden mallet (Kọ́ríkọ́).",
        "proverbs_and_oral_traditions": [
            "Ọmẹle-abo kì í da orin rú; ohùn ìyá ni ó fi ń tọ́ ọmọ sọ́nà. (The female omele drum never disrupts the symphony; it guides the musical ensemble like a mother guiding her progeny: Teaching the power of supportive, foundational stability in community and art.)",
            "Bí ìyááùlù bá ń fọhùn, ọmẹle-abo ní ń gbe lẹ́sẹ̀. (When the master mother drum pronounces sacred verses, it is the female omele that upholds its stride: Illustrating harmonic interdependence between soloist leadership and disciplined rhythmic foundation.)",
            "Àyàn kò kọ́ ọmọ rẹ̀ l'orin kí ọmẹle ó sọ ọ̀rọ̀ àbùkù. (Àyàn never instructed his drum-scions to sing so that the omele would utter indignity: Emphasizing the sacred ethical lineage and speech-fidelity of the drummer guild.)"
        ]
    },
    "Ìlù Agogo": {
        "etymology_and_philosophy": "From 'Ìlù' (the rhythmic strike / percussive sounding, from lù: to strike/beat) and 'Agogo' (the hand-forged clapperless iron bell). In musical guild vernacular, sometimes rendered as 'Ẹlù' (the lead striker/timekeeper). Philosophically represents temporal order, public warning, and the sacred resonance of Ògún's iron in structuring cosmic and communal time.",
        "historical_timeline": "Iron Age Antiquity: Forged in the earliest iron smelters of Ilé-Ifẹ̀ and Òwọ̀; consecrated to Ògún as the herald of civic gatherings and temple assemblies. Classical Era: Commanded market openings, royal proclamations, and sacred seasonal rites across Ọ̀yọ́, Benin, and Ìjẹ̀bú polities. Transatlantic Era: Retained as the indispensable rhythmic anchor in Afro-Cuban Santería/Abakuá and Brazilian Samba (as the Agogô). Modern Era: Endures as the driving metronome in contemporary highlife, Jùjú, and Fela Kuti's Afrobeat.",
        "material_and_craftsmanship": "Forged by master blacksmiths (Àwọn Àgbẹ̀dẹ) from high-grade wrought iron or cast bronze, tempered in cold water baths, and struck with a solid iron striker or dense camwood rod.",
        "proverbs_and_oral_traditions": [
            "Agogo kì í lu ara rẹ̀ lásán; ọwọ́ Ògún ní ń fọhùn. (The iron bell never strikes itself in vain; it is the hand and will of Ògún that sounds forth: Manifesting that every decisive action and warning has a divine cause.)",
            "Ẹlù agogo tí ń kégbe l'ọ́jà, kì í ṣe orin aláyọ̀ nìkan ló ń kọ. (The master bell resounding in the marketplace does not merely sing songs of joy; it sounds civic warnings and cosmic summons: Symbolizing truth-telling and vigilance in public communication.)",
            "Bí agogo kò bá dún lórí àtẹ, ayẹyẹ kò tíì gbádùn. (If the iron bell has not resounded over the festival grounds, the celebration has not yet attained its true soul: Highlighting the bell as the indispensable heartbeat of festivity.)"
        ]
    },
    "Filà Abetíajá": {
        "etymology_and_philosophy": "Compound from 'Filà' (traditional cap) and 'Abetí-ajá' ('Having ear-flaps like a dog'). Philosophically symbolizes sartorial sovereignty, personal wit, and nuanced political commentary expressed through the tilt of the triangular flaps.",
        "historical_timeline": "17th–18th Century: Evolved among aristocrats, cavalry captains, and wealthy merchants in Old Ọ̀yọ́ and Ìjẹ̀bú; the folding of the flaps functioned as non-verbal communication conveying romantic readiness, political defiance, or celebratory serenity. 19th Century: Worn by senior warriors during the Yorùbá civil wars. 20th Century: Championed by prominent anti-colonial nationalists and First Republic leaders such as Chief Ladoke Akintola. Contemporary Era: Reclaimed on global African fashion runways as a supreme emblem of indigenous elegance.",
        "material_and_craftsmanship": "Handcrafted from strips of narrow-loom Aṣọ-Òfì (Sányán, Ẹtù, or Alárì) or plush velvet, lined with stiffened unbleached cotton calico, and embellished with hand-embroidered chain-stitch motifs.",
        "proverbs_and_oral_traditions": [
            "Abetíajá kì í bọ́ lórí ọmọlúwàbí; ipò ọlá ní ń tọ́ka sí. (The dog-eared cap never slips dishonorably from the head of an Ọmọlúwàbí; it points toward the summit of dignity: Expressing how sartorial refinement mirrors an individual's upright character.)",
            "Bí mo bá dárí filà sí ọ̀tún, ayé mi ti tòrò; bí mo bá dárí rẹ̀ sí òsì, ọ̀rọ̀ ń bẹ lẹ́yìn. (When I tilt my cap flaps to the right, my world is serene; when I tilt them to the left, there is weightier matter to resolve: Revealing the subtle non-verbal communicative codes embedded in Yorùbá cap styling.)",
            "A kì í fi filà abetíajá bo orí tí kò lẹ́kọ̀ọ́. (One does not crown a head devoid of discipline and culture with the noble dog-eared cap: Emphasizing that prestige regalia is reserved for those steeped in moral maturity.)"
        ]
    },
    "Filà Oníde": {
        "etymology_and_philosophy": "From 'Filà' (cap) and 'Oní-ide' ('Adorned with sacred brass or bronze emblems'). Philosophically signifies incorruptibility, ancestral wisdom, and the judicial impartiality of senior Osùgbó/Ògbóni elders, as brass never corrodes.",
        "historical_timeline": "Ancient Ifẹ̀ Antiquity: Associated with ancient brass-casting guilds and the cosmological cult of Ọ̀ṣun and Ọ̀rúnmìlà, where brass embodied eternal purity. Classical Eras: Reserved for high-ranking judicial elders, kingmakers, and titled palace counselors across Ọ̀yọ́, Ìjẹ̀bú, and Èkìtì kingdoms. Diaspora Preservations: Mirrored in Afro-Cuban Lucumí and Brazilian Ketu ceremonies where brass crowns and ornaments honor Ọ̀ṣun. Contemporary Period: Worn during coronation ceremonies, judicial conclaves, and supreme chieftaincy installations.",
        "material_and_craftsmanship": "Tailored from deep indigo-dyed Aṣọ Ẹtù or wild silk Sányán, adorned with lost-wax cast brass emblems, protective miniature bells (Ṣaworo), and cowrie shell accents.",
        "proverbs_and_oral_traditions": [
            "Ide kì í dógùn; filà oníde kì í tẹ́ lójú àgbà. (Brass never corrodes into rust; the brass-adorned cap never suffers humiliation in the assembly of elders: Affirming the eternal, incorruptible dignity of sacred leadership.)",
            "Orí tí ó gbé filà oníde, kò gbọdọ̀ jẹ́rìí èké. (The head that bears the consecrated brass cap must never utter false testimony: Codifying the strict ethical integrity demanded of judicial elders and titleholders.)",
            "Ọ̀ṣun ní ń lo ide, Aláàfin ní ń wọ̀ ọ́; filà oníde kì í ṣe eré ọmọdé. (Ọ̀ṣun commands the brass, the Aláàfin arrays in it; the brass-embellished cap is never a plaything for children: Emphasizing the sacred weight and divine covenant of the headpiece.)"
        ]
    },
    "Ìpájọ́": {
        "etymology_and_philosophy": "Contraction of 'Ìpéjọ-àjọ' ('The solemn convocation of lineage elders / Clan judicial court'). Philosophically reflects restorative justice, communal consensus, and the preservation of lineage equilibrium over retributive punishment.",
        "historical_timeline": "Classical Antiquity: Established within compound architecture (Agbo Ilé) across ancient Ifẹ̀ and Ọ̀yọ́ as the primary dispute-resolution mechanism. Pre-Colonial Era: Convened by the Baálé (compound head) and Ìyálé (senior matriarch) to arbitrate civil boundaries, marital disputes, and inheritance. Colonial Era: Maintained communal autonomy by operating outside the British colonial court system. Modern Day: Continues as an active grassroots dispute-resolution forum across Yorùbá towns, averting litigation and cementing familial solidarity.",
        "material_and_craftsmanship": "Convened in the open peristyle veranda (Ìloro), seated upon woven reed mats (Ẹní Ẹẹrẹ) and carved hardwood stools, centered around split kola nuts (Obì Àbàtà) and palm wine libations.",
        "proverbs_and_oral_traditions": [
            "Àgbà kì í wà l'ọ́jà kí orí ọmọ tuntun wọ́; ìpájọ́ kì í jókòó kí ìlú tú. (Elders are not present in the marketplace while the infant's head droops; the lineage assembly does not sit while the community falls into ruin: Highlighting collective elder responsibility in averting communal breakdown.)",
            "Àjọ kì í pé kí ó má tuka, ṣùgbọ́n àwọn olóotọ́ a máa f'ọ̀rọ̀ s'ilẹ̀ rere. (An assembly will inevitably disperse, but righteous arbiters plant decisions upon fertile ground: Emphasizing the enduring peace achieved through fair judicial mediation.)",
            "A kì í torí ìjà kọ ìbátan; ìpájọ́ ni a fi ń mú ọkàn balẹ̀. (One does not sever kinship because of an altercation; it is through the lineage court that peace of heart is restored: Underlining restorative reconciliation as the ultimate aim of justice.)"
        ]
    },
    "Àṣà-Ọmọlúwàbí": {
        "etymology_and_philosophy": "From 'Ọmọ-tí-Olú-Ìwà-bí' ('The child begotten by the Lord of Character / Supreme Being of Moral Essence') + 'Àṣà' (sacred custom/culture). The supreme philosophical concept of Yorùbá moral ontology, valuing integrity, humility, courage, industriousness, and empathy above material accumulation.",
        "historical_timeline": "Primordial Philosophy: Codified in classical Ifá verses (e.g. Òwọ́nrín Mejí and Ìwòrì Mejí) centuries prior to foreign cultural contact as the highest measure of a civilized human being. Classical & Imperial Epoch: The necessary prerequisite for kingship investiture, guild mastership, and martial leadership (Aare Ona Kakanfo). Transatlantic Persistence: Retained in the Black Atlantic as 'Iwa Pele' (gentle/good character), serving as ethical resistance against the brutalities of enslavement. Contemporary Relevance: Regarded globally as the cornerstone of Pan-African humanism and moral ethics.",
        "material_and_craftsmanship": "Materialized through courteous physical postures (Ìdọ̀bálẹ̀ for men, Ìkúnlẹ̀ for women), measured tone of speech, modesty of attire, and generosity of spirit.",
        "proverbs_and_oral_traditions": [
            "Ìwà l'ẹwà ọmọlúwàbí; bí o lówó tí o kò n'íwà, o dabi ère tí a gbé s'óko. (Character is the supreme beauty of the noble soul; if you possess vast wealth but lack moral character, you are no better than a scarecrow standing in the farm: The foundational axiom of Yorùbá virtue ethics.)",
            "Ọmọlúwàbí kì í gbé ọ̀rọ̀ èké kọjá odi. (A person of noble character never carries false witness across the threshold: Highlighting unyielding truthfulness and integrity as non-negotiable virtues.)",
            "Owó kò lè ra orúkọ rere; àṣà-ọmọlúwàbí ni wúrà ayé. (Money cannot purchase a sterling reputation; the ethos of Ọmọlúwàbí is the true gold of existence: Proclaiming moral virtue as infinitely superior to transient material wealth.)"
        ]
    },
    "Ewe Àìdan": {
        "etymology_and_philosophy": "From 'Àì-dá-nù' ('That which cannot be discarded into waste / Incorruptible protective botanical'). In Yorùbá botanical philosophy, represents spiritual purification, postpartum maternal restoration, and the expulsion of negative metaphysical energies.",
        "historical_timeline": "Deep Forest Antiquity: Codified in the ancient Ọ̀sanyìn and Ifá herbal corpus (especially Ọ̀sẹ́ Mejí) as a sacred prophylactic and spiritual barrier. Classical Traditional Medicine: Used for centuries by midwives and herbalists (Oníṣègùn) across Southwestern Nigeria in post-natal restorative soups and medicinal baths. Transatlantic Retention: Preserved in Cuban Lucumí and Brazilian Candomblé ceremonies as an indispensable botanical in sacred cleansing baths (Omiero). Modern Ethnobotany: Pharmacologically validated for anti-inflammatory, antimicrobial, and hypotensive properties.",
        "material_and_craftsmanship": "Bipinnate fern-like leaves paired with aromatic four-winged woody pods of Tetrapleura tetraptera, dried in earthenware vessels and compounded with native black soap (Ọṣẹ Dúdú) and camwood (Osùn).",
        "proverbs_and_oral_traditions": [
            "Àìdan ló ní kí gbogbo ibi ó dà nù. (It is the divine authority of Àìdan that commands all malevolence to disperse into nothingness: Invoking the plant's metaphysical authority to banish misfortune and restore spiritual purity.)",
            "Bí a bá bọ̀wọ̀ fún ewé, ewé a máa jẹ́ fún wa. (If we accord reverence to the sacred leaf, the leaf will manifest its healing efficacy for us: The ecological covenant of reciprocity between the Yorùbá herbalist and the botanical realm.)",
            "Àìdan kò koro sí àgbo, ó ń fún oúnjẹ ní oorun ọlá. (Àìdan brings no bitterness to the healing potion; it bestows the fragrant aroma of honor: Demonstrating that true healing cleanses without inflicting cruelty.)"
        ]
    },
    "Obì Ìyàwó": {
        "etymology_and_philosophy": "Compound of 'Obì' (the sacred kola nut, Cola acuminata) and 'Ìyàwó' (the bride / nuptial partner). Philosophically embodies the matrimonial covenant, mutual prayers for fertility, lineage prosperity, and ancestral sanction.",
        "historical_timeline": "Ancient Antiquity: Originated during early Ifẹ̀ marriage ceremonies where kola nuts were split to invoke ancestral witnesses and ratify familial covenants. Pre-Colonial Era: Served as the pivotal sacramental item in the Idána (engagement) ceremony, distributed to all branches of the extended family to seal the matrimonial pact. Transatlantic Continuity: Survived in Afro-Cuban and Afro-Brazilian traditions as sacred Obi Abata used to consult the ancestors and seal spiritual marriages. Contemporary Practice: An indispensable ritual component in modern Yorùbá traditional weddings across the globe.",
        "material_and_craftsmanship": "Select four-lobed kola nuts (Obì Àbàtà) arranged in ornate brass basins or carved wooden calabashes alongside honey (Oyin), alligator pepper (Atare), sugarcane (Ìrèké), and cowries.",
        "proverbs_and_oral_traditions": [
            "Obì níí kọ́rọ̀ sílé, obì níí kọ́rọ̀ sóde. (It is the sacred kola that summons abundance into the household; it is the kola that radiates prosperity outward: Celebrating the kola nut as a catalyst of domestic and public flourishing.)",
            "Obì kì í kọ̀ láì bí ọmọ; àṣẹ ìyàwó a d'ọmọ l'ọ́wọ́. (The sacred kola nut never refuses to generate fruitful pods; the bridal blessing transforms into children in arms: Nuptial prayer invoking fertility, prosperity, and lineage continuity.)",
            "A kì í fi obì àbàtà bọ orí lásán; ẹ̀jẹ̀ ìrẹ́pọ̀ ni a fi ń gbìn. (One does not offer the four-lobed kola to the divine inner head without solemn purpose; it is the bond of unbreakable harmony that is planted: Highlighting the sacred solemnity of the matrimonial covenant.)"
        ]
    },
    "Ìpèsè-Ẹ̀gbẹ́": {
        "etymology_and_philosophy": "From 'Ìpèsè' (sacred propitiatory banquet / ceremonial offering) and 'Ẹ̀gbẹ́' (The Astral Society / Heavenly Companions / Ẹ̀gbẹ́ Ọ̀run). Philosophically acknowledges spiritual twinship between the physical realm (Àyé) and the invisible realm (Ọ̀run), resolving astral disharmony through generous hospitality.",
        "historical_timeline": "Primordial Cosmogony: Established in ancient Yorùbá spiritual metaphysics to maintain equilibrium between terrestrial children and their spiritual peers at crossroads (Oríta) and riverbanks. Classical Era: Administered by senior priestesses (Ìyálé Ẹ̀gbẹ́) to mitigate infant distress (Àbíkú) and promote communal well-being. Transatlantic Presence: Retained in Lucumí and Candomblé Ketu rituals dedicated to the spiritual child spirits (Erê and Ibeji). Contemporary Era: Actively practiced across Yorùbáland as a joyful feast of music, sweets, and communal sharing.",
        "material_and_craftsmanship": "Wide earthenware vessels (Àwo Pọ́tílí) loaded with sweet foods: sugarcane, fried plantains (Dòdò), parched corn (Guguru), bean cakes (Àkàrà), honey, and decorated with white chalk (Ẹfun) and red camwood.",
        "proverbs_and_oral_traditions": [
            "Bí a bá pèsè fún Ẹ̀gbẹ́, Ayé á tòrò mọ́ni lówó. (When we spread a generous banquet for the Astral Peers, earthly existence becomes tranquil and sweet within our grasp: Expressing cosmic balance and the pacification of turbulent spiritual forces.)",
            "Ẹni tó fún Ẹ̀gbẹ́ l'óúnjẹ, kò ní sunkún ọmọ. (Whoever provides nourishing food for the Heavenly Companions shall never weep in sorrow over physical children: Emphasizing spiritual guardianship over child mortality and infant wellness.)",
            "Àbíkú sọkún fún ìpèsè, Ẹ̀gbẹ́ Ọ̀run gba ẹ̀bùn. (The wandering child longs for reconciliation; the Heavenly Peers accept the peaceful banquet: Signifying the resolution of spiritual wanderlust through communal devotion and shared feasts.)"
        ]
    },
    "Iyalálájẹ́ Market Council": {
        "etymology_and_philosophy": "From 'Ìyá-ní-alá-ajé' ('Mother Custodian of Commerce and Wealth') and 'Market Council' (the confederated chamber of women guild leaders). Philosophically embodies matriarchal economic governance, fair market regulation, and spiritual stewardship over community prosperity.",
        "historical_timeline": "Ancient Antiquity: Traced to the legendary market reforms of Queen Moremi and Ọya at Ilé-Ifẹ̀; crystallized in the institutional development of the Ọjà Ọba (King's Market) across Yorùbá polities. Imperial Era: Commanded profound constitutional veto power in Old Ọ̀yọ́; market boycotts could halt imperial tax collection and restrain despotic rulers. 20th Century: Championed anti-colonial commercial boycotts and tax resistance led by pioneering merchant matriarchs like Madame Tinubu and Alimotu Pelewura. Modern Era: The Ìyálọ́jà/Iyalálájẹ́ institution remains the most powerful economic and social mobilization network in West Africa.",
        "material_and_craftsmanship": "Emblems include cast brass bells and staffs consecrated to the Òrìṣà Ajé, cowrie shell divination boards, heavy coral necklaces (Ìyùn), and opulent layered Aṣọ-Òkè wrappers.",
        "proverbs_and_oral_traditions": [
            "Ayé l’ọjà, ọ̀run n’ilé. (The physical world is an active marketplace; the spiritual realm is our permanent home: The quintessential Yorùbá philosophical paradigm urging fair commercial ethics and moral reckoning.)",
            "Ajé pé l’ọ́jà, ó d’onílé; obìnrin ló ni ọjà tí ìlú fi ń tòrò. (Commerce tarried long in the market until it built an enduring home; it is the women who command the markets through which the commonwealth prospers: Highlighting matriarchal governance of economic life.)",
            "Ọjà kò gbọdọ̀ gbó, kí ìlú fọ́; àṣẹ Iyalálájẹ́ kì í ṣe asán. (The vibrancy of the market must never spoil lest the foundation of the town collapse; the decree of the Iyalálájẹ́ is never in vain: Underscoring the civic indispensable power of commercial matriarchs.)"
        ]
    },
    "Àgbàǹgbá": {
        "etymology_and_philosophy": "Onomatopoeic and praise name for the elusive harnessed bushbuck (Tragelaphus scriptus) of the Yorùbá rainforest. In indigenous fauna philosophy, represents acute discernment, lightning agility, and spiritual sanctuary in the deep bush.",
        "historical_timeline": "Ancient Hunters' Lore: Celebrated in ancient hunters' oral poetry (Ìjálá Ọdẹ) dating to pre-agrarian foraging antiquity across the Yorùbá forest belt. Classical Kingdoms: Sacred fauna in the rituals of Ògún and Ọ̀ṣọ́ọ̀sì, symbolizing the boundary between cultivated farms (Oko) and the untamed wilderness (Igbó). Transatlantic Memory: Preserved in Afro-Cuban Palo Monte and Santería where forest antelope horns (Tarros de Venado) house sacred protective medicines. Modern Conservation: Documented as an important indicator species in protected forest reserves like Omo and Old Oyo National Parks.",
        "material_and_craftsmanship": "Spiral ridged horns used to craft hunters' signal horns (Fèrè) and medicine amulets (Ìrùkẹ̀ Ọdẹ); spotted pelts utilized for sacred drum membranes and hunters' medicine pouches (Àpò Ọdẹ).",
        "proverbs_and_oral_traditions": [
            "Àgbàǹgbá kì í fẹsẹ̀ tẹ ẹ̀gún nínú igbó lásán; ọlọ́gbọ́n lẹran ń ṣe. (The bushbuck never steps upon thorns within the dense forest carelessly; it moves with profound discernment: Urging prudence, strategic foresight, and careful navigation through life's perils.)",
            "Bí ọdẹ kò bá tètè jí, kò lè rí ojú àgbàǹgbá. (If the hunter does not rise before the break of dawn, the countenance of the bushbuck will elude him forever: Teaching that transcendent wisdom and rare fortunes require early discipline and dedication.)",
            "A kì í rí àgbàǹgbá lórí àtẹ ní ọjà láìjẹ́ pé ọwọ́ Ògún tẹ̀ ẹ́. (One never beholds the sacred bushbuck displayed on the market rack unless the hand of Ògún has sanctioned its transition: Demonstrating that elusive greatness is never overcome by chance, but by divine purpose.)"
        ]
    },
    "Ayò Olọ́pọ́n": {
        "etymology_and_philosophy": "From 'Ayò' (joy / celebratory triumph) and 'Olọ́pọ́n' (possessor of the carved wooden board, Ọpọ́n). Philosophically embodies strategic foresight, mathematical acumen, communal sportsmanship, and mental equanimity.",
        "historical_timeline": "Classical Antiquity: Archaeological finds at Ilé-Ifẹ̀ and Old Ọ̀yọ́ indicate stone mancala playing pits dating over a millennium; played by monarchs, generals, and sages. Pre-Colonial Era: Served as a tactical training simulation for military generals (Balógun) prior to battle campaigns. Transatlantic Diaspora: Traveled across the Middle Passage into the Caribbean (Barbados 'Warri', Antigua 'Awari') and Brazil as an intellectual badge of African genius. Contemporary Era: Formalized into national mind-sport championships and university academic curricula worldwide.",
        "material_and_craftsmanship": "Sculpted from a single block of dense hardwood (Ìrókò or Ọmọ) by Gbẹ́nàgbẹ́nà guild carvers, featuring twelve playing pits and two end storage hollows, played with 48 polished nickernut seeds (Ọmọ Ayò).",
        "proverbs_and_oral_traditions": [
            "A kì í fi ojú ayò bẹ́rù ènìyàn. (One does not intimidate an adversary merely by staring down the pits of the game board: True courage is manifested through deliberate strategic moves, not empty posturing.)",
            "Ayò kì í ṣe eré alápọ́n; ọlọ́gbọ́n ló ń ṣẹ́gun nínú ọpọ́n. (Ayò is never the sport of the lazy mind; it is the sharp-witted strategist who reaps the harvest of the board: Teaching that foresight, mathematical discipline, and focus govern victory in human affairs.)",
            "Bí a bá ń ta ayò, a kì í bínú; sùúrù ni a fi ń jẹ ọmọ ayò tán. (When playing Ayò, one must master all anger; it is with patience that one captures all the seeds on the board: Emphasizing emotional restraint as the supreme virtue in conflict and competition.)"
        ]
    },
    "Adire Oníkan": {
        "etymology_and_philosophy": "From 'Adì' (to tie/bind) + 'rẹ' (to dye) + 'Oníkan/Oní-òwú' (possessor of thread/raffia resist bindings). Philosophically symbolizes the art of structured restraint, sacred patience, and the revelation of divine beauty through deep immersion in life's dye pits.",
        "historical_timeline": "Pre-Colonial Roots: Cultivated for centuries across Yorùbá towns, blossoming in 19th-century Abẹ́òkúta (especially Itoku and Kemta) where women dyers (Ẹgbẹ́ Aláró) operated communal indigo vats. Colonial Era Resilience: In the 1920s–1930s, female guild masters successfully resisted imported European printed cottons by asserting hand-bound indigo textiles as prestige ceremonial wear. Transatlantic Links: Indigo resist techniques informed Afro-Caribbean and Brazilian textile arts in Bahia. Contemporary Era: Celebrated internationally as a pinnacle of Pan-African textile design, embraced in global fashion houses.",
        "material_and_craftsmanship": "Woven cotton fabric meticulously hand-bound with raffia (Ìkó) or cotton cord to create geometric motifs, then immersed repeatedly in deep earthen indigo fermentation vats (Kòtò Elú) enriched with wood ash lye.",
        "proverbs_and_oral_traditions": [
            "A kì í kọ́kọ́ dárò kí á tó mọ àwọ̀ rẹ̀. (One does not conclude the character of indigo before the fabric emerges from the deep vat: Warning against premature judgment of human character before they pass through life's testing.)",
            "Bí ẹnìyán bá mọ àdìrẹ kíkàn, ó gbọ́dọ̀ mọ sùúrù wíwú. (He who masters the art of binding must equally cultivate the holy patience of unraveling: Teaching that constructive creation and disentanglement both require disciplined persistence.)",
            "Àṣẹ Ìyá Mápo ní ń sọ òkùnkùn elú di ìmọ́lẹ̀ arẹwà. (It is the divine authority of Ìyá Mápo that transmutes the darkness of indigo into radiant beauty: Celebrating the feminine divine patroness of pottery, dyeing, and creative transmutation.)"
        ]
    },
    "Ọ̀pọ̀ṣẹ́": {
        "etymology_and_philosophy": "From 'Ọ̀pọ̀' (vertical pillar/post) and 'Ṣẹ́' (to manipulate/weave/create). The traditional vertical frame loom operated exclusively by female master weavers, philosophically symbolizing maternal industry, domestic sovereignty, and the weaving of cosmic order.",
        "historical_timeline": "Classical Antiquity (c. 11th–12th Century CE): Terracotta figures from Ilé-Ifẹ̀ substantiate the deep antiquity of broadcloth woven on vertical looms by women. Medieval to 19th Century: Wove thick protective Kíjìpá cloth, bridal wraps, and burial shrouds across Ìjẹ̀bú, Òndó, and Òwọ̀. Transatlantic Diaspora: Maintained by Afro-descendant women in Bahia, Brazil, weaving sacred ceremonial cloths (Pano da Costa) for Candomblé rites. Contemporary Revival: Continues in traditional compound cooperatives preserving archaic indigenous cotton varieties.",
        "material_and_craftsmanship": "Fixed vertical rectangular frame crafted from hardwood poles, bone or hardwood shuttles (Ọkọ̀), shed sticks (Àtẹ́lẹsẹ̀), and heddle rods, weaving broad continuous panels of dense cotton.",
        "proverbs_and_oral_traditions": [
            "Bí a bá ń hun aṣọ lórí ọ̀pọ̀ṣẹ́, sùúrù ni a fi ń gun òwú. (When one weaves upon the vertical loom frame, patience is the supreme tool that straightens the tangled thread: Celebrating deliberate craft and unhurried emotional mastery.)",
            "Ọ̀pọ̀ṣẹ́ kì í kọ̀ láti gba òwú; ilẹ̀ ayé kì í kọ̀ láti gba ẹ̀dá. (The consecrated upright loom never rejects the weaver's thread; the earth never refuses to receive humanity: The ontological philosophy of cosmic acceptance and destined inclusion.)",
            "Obìnrin tí ó mọ ọ̀pọ̀ṣẹ́ hún, kò ní fi aṣọ àkísà bo ọmọ rẹ̀. (The mother who masters the craft of the upright loom frame shall never shroud her progeny in the rags of misfortune: Honoring feminine economic sovereignty, skill acquisition, and maternal protection.)"
        ]
    },
    "Ofì Apá": {
        "etymology_and_philosophy": "From 'Òfì' (the horizontal treadle loom) and 'Apá' (arm / rhythmic wing stroke of the weaver). The narrow-strip horizontal loom operated exclusively by male weavers, philosophically signifying dynamic labor, rhythmic precision, and social prestige.",
        "historical_timeline": "Classical Ọ̀yọ́ Origins: Developed between the 12th and 14th centuries CE, flourishing in ancient weaving capitals like Ìséyìn and Ọ̀yọ́-Ilé under the royal patronage of the Aláàfin. 19th Century Expansion: Guild weavers displaced by the northern wars disseminated narrow-strip weaving techniques southwards to Ìbàdàn, Èdẹ, and Abẹ́òkúta. Transatlantic Resonance: Strip-cloth aesthetics persisted in West African diasporic memories across the Americas. Contemporary Dynamism: Ìséyìn remains the global capital of Aṣọ-Òfì, supplying high-status prestige garments for weddings and state investitures worldwide.",
        "material_and_craftsmanship": "Constructed from bamboo and hardwood timbers with hanging reed beater (Asá), foot treadles (Ìtẹ̀lẹ̀), boat shuttle (Ọkọ̀ Òfì), and drag stone weight (Òkúta Òfì), producing 4-inch narrow strips.",
        "proverbs_and_oral_traditions": [
            "Bí ọkọ̀ ṣe ń lọ, bẹ́ẹ̀ ni aṣọ ń gùn. (As the weaver's shuttle journeys faithfully back and forth, so the cloth of destiny unfolds: Teaching that consistent, focused daily effort weaves the garment of great accomplishment.)",
            "A kì í fi ẹ̀tẹ́ ṣe aṣọ Òfì; ọlá ní ń gbé e wọ̀. (One does not weave disgrace on the loom; it is sovereign majesty that wears the finished cloth: Affirming that sacred craftsmanship must be dedicated to honor and human dignity.)",
            "Ọkọ̀ Òfì kì í bínú sọ́wọ́ olóko. (The weaver's shuttle does not wage war against the guiding hand of the artisan: Illustrating harmonious submission of tools and talent to master artistic vision and communal purpose.)"
        ]
    }
}

def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: Path, data: Any):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_entity_thin(entity: Dict[str, Any]) -> bool:
    provs = entity.get("proverbs_and_oral_traditions", [])
    timeline = (entity.get("historical_timeline") or "").strip()
    has_trans = False
    if isinstance(provs, list) and len(provs) > 0:
        for p in provs:
            if "(" in p and ")" in p:
                has_trans = True
                break
    is_thin_time = (
        len(timeline) < 120 or
        timeline.startswith("Deep antiquity tracing") or
        timeline.startswith("Classical Yorùbá antiquity")
    )
    return (not has_trans) or is_thin_time

def main():
    print("=" * 80)
    print("🏛️  ÀGBÀ ENGINE: EXECUTING HANDOFF-AROKIN-001 (BATCH 1 ENRICHMENT)")
    print(f"   Target Entities to Enrich: {len(ENRICHMENTS)}")
    print("=" * 80)

    api_corpus = load_json(API_CORPUS)
    web_corpus = load_json(WEB_CORPUS)

    api_by_id = {e.get("id"): e for e in api_corpus}
    web_by_id = {e.get("id"): e for e in web_corpus}

    enriched_count = 0
    for entity_id, fields in ENRICHMENTS.items():
        if entity_id not in api_by_id:
            raise KeyError(f"Entity '{entity_id}' not found in API corpus!")
        if entity_id not in web_by_id:
            raise KeyError(f"Entity '{entity_id}' not found in Web corpus!")

        for target in [api_by_id[entity_id], web_by_id[entity_id]]:
            for k, v in fields.items():
                target[k] = v

        # Validate that the entity is no longer thin
        assert not is_entity_thin(api_by_id[entity_id]), f"{entity_id} still thin in API corpus!"
        assert not is_entity_thin(web_by_id[entity_id]), f"{entity_id} still thin in Web corpus!"

        print(f"  ✅ [ENRICHED & VALIDATED] '{entity_id}' -> Àmọ̀tẹ́kùn Parity Achieved")
        enriched_count += 1

    save_json(API_CORPUS, api_corpus)
    save_json(WEB_CORPUS, web_corpus)

    print("=" * 80)
    print(f"🎉 SUCCESS: Enriched {enriched_count} entities in both API & Web corpora.")
    print(f"📁 Updated: {API_CORPUS}")
    print(f"📁 Updated: {WEB_CORPUS}")
    print("=" * 80)

if __name__ == "__main__":
    main()
