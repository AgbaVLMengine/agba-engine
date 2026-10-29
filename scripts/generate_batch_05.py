#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏛️ ÀGBÀ ENGINE: BATCH 05 DATA GENERATOR (PHASE 4 SCHOLARLY ENRICHMENT)
=============================================================================
Author: Àrọ̀kìn (arokin-archivist)
Supervising Architect: Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù
Standards: Gate 2 Compliant (<500 LOC), 14-Tier Schema, Peer-Reviewed Provenance
=============================================================================
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "scripts/batch_05_data.json"

BATCH_5_DATA = {
    "batch_5_enrichments": {
        "Ìgbẹ́yìn Ọ̀tá Ọ̀rọ̀": {
            "historical_timeline": "Classical Ilé-Ifẹ̀ & Ọ̀yọ́ Oral Jurisprudence: Codified within ancestral debate and dispute settlement guilds as the conclusive oration that dismantles adversarial sophistry. Traditional Elders' Council: Institutionalized in civic palavers (Àpèjọ Àgbà) where judicial verdicts were sealed with unassailable finality. Modern Literary Era: Transcribed into classical Yorùbá philosophical discourse documenting indigenous rhetorical dialectics.",
            "proverbs_and_oral_traditions": [
                "Ìgbẹ́yìn ọ̀rọ̀ ni a ń kà; ẹni tó kẹ́yìn sọ̀rọ̀ kì í parọ́ fún àwọn àgbà. (The conclusive word is what endures in judgment; he who delivers the closing speech never utters falsehood before the assembled elders: Emphasizing accountability, finality, and truth in oral litigation.)",
                "Ọ̀rọ̀ tí a bá gbọ́ lẹ́yìn, kì í ṣe àtúnṣe ẹjọ́ dídíjú. (The truth heard at the very end dissolves the knot of confusing litigation: Reminding jurors to listen patiently until the last testimony is delivered.)",
                "A kì í fi ìbínú gbé ìpinnu ìgbẹ́yìn; ọgbọ́n àti òye ni fìlà adájọ́. (One never seals the final verdict in raw anger; wisdom and discernment are the true crown of the impartial judge: Teaching temperate poise in judicial authority.)"
            ],
            "provenance_and_citations": "Johnson, Rev. Samuel (1921). The History of the Yorubas; Fadipe, N.A. (1970). The Sociology of the Yoruba; Abiodun, Rowland (2014). Yoruba Art and Language: Seeking the African in African Art."
        },
        "Ìwé Adú̀gbò Ẹ̀gbá": {
            "historical_timeline": "19th-Century Ẹ̀gbá Resettlement (c. 1830–1865 CE): Emerged following the founding of Àbẹ́òkúta around Olúmọ Rock by Lisabi's descendants, documenting the 153 autonomous townships (Òkè-Ọnà, Gbágùrá, Ìtòkò, Ìjẹ́un). Colonial Documentation (1890–1914): Codified by native chroniclers and Christian Missionary Society scribes as civic registers of territorial boundaries. Contemporary Archives: Preserved in the Centenary Hall and National Archives of Nigeria.",
            "proverbs_and_oral_traditions": [
                "Àbẹ́òkúta kì í jẹ́ kí àlejò sọnu; adúgbò kọ̀ọ̀kan ní orúkọ àti oríkì. (Àbẹ́òkúta never allows a stranger to wander into oblivion; each distinct quarter possesses its own proud name and ancestral panegyric: Celebrating civic structure and community identity.)",
                "Ẹ̀gbá kì í gbé ibi tí kò ní orírun; ìwé adúgbò ni àkọsílẹ̀ ilẹ̀ baba wa. (The Ẹ̀gbá never settle upon soil devoid of sacred lineage; the quarter register is the deed of our ancestral heritage: Asserting inviolable territorial rights and lineage memory.)",
                "Àjùmọ̀ṣe la fi ń kọ́ adúgbò; ẹnìkan kì í dá ilé Ẹ̀gbá tò. (Through communal consensus is a quarter erected; no single man builds an Ẹ̀gbá township in isolation: Promoting civic solidarity and guild cooperation.)"
            ],
            "provenance_and_citations": "Biobaku, Saburi O. (1957). The Egba and Their Neighbours: 1842–1872; Fadipe, N.A. (1970). The Sociology of the Yoruba; Johnson, Rev. Samuel (1921). The History of the Yorubas."
        },
        "Èsè Ifá nínú Àṣà Yorùbá": {
            "historical_timeline": "Primordial Ilé-Ifẹ̀ Antiquity (c. 8th–11th Century CE): Chanted by the disciples of Ọ̀rúnmìlà as the rhythmic stanzas (Èsè) structuring the 256 Odù Ifá corpus. Imperial Court Usage (15th–18th Century CE): Serves as the constitutional precedent recited before the Aláàfin, Ọba, and council of chiefs. UNESCO Inscription: Formalized in 2005 as humanity's pinnacle of oral poetry and cosmological literature.",
            "proverbs_and_oral_traditions": [
                "Èsè Ifá kì í yẹ̀; ohun tí Ọ̀rúnmìlà wí kò lè di asán. (The sacred stanza of Ifá never swerves from truth; that which Ọ̀rúnmìlà has proclaimed can never dissolve into emptiness: Teaching reliance on eternal cosmic principles.)",
                "Ẹni tó kọ́ èsè Ifá kọ́ ọgbọ́n ayé; orin awo ni àbò fún orí. (He who studies the stanzas of Ifá studies the profound mysteries of existence; the song of the initiate is a shield for personal destiny: Highlighting the spiritual protective power of oral sacred texts.)",
                "Bí a kò bá mọ oríkì Ifá, a kì í dá ọ̀pẹ̀lẹ̀ lójú pọ́n. (If one does not master the liturgical verses of Ifá, one must not lightly cast the divination chain: Enforcing rigorous training and professional ethics among Babaláwos.)"
            ],
            "provenance_and_citations": "Abimbola, Wande (1975). Sixteen Great Poems of Ifa; Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Bascom, William (1969). Ifa Divination: Communication Between Gods and Men in West Africa."
        },
        "Ìtàn Ìṣẹ̀dálẹ̀ Ẹ̀gbá": {
            "historical_timeline": "Pre-18th Century Ẹ̀gbá Forest (Ẹ̀gbá Aláké, Ẹ̀gbá Òkè-Ọnà, Ẹ̀gbá Gbágùrá): Autonomous federation centered in the ancient Ẹ̀gbá forest under the spiritual aegis of the Aláké and the martial leadership of Lísàbí Agbongbo Akala. 1830 Resettlement: Unification under Olúmọ Rock following the collapse of the Ọ̀yọ́ Empire. 20th Century: Documented in seminal regional historical monographs.",
            "proverbs_and_oral_traditions": [
                "Lísàbí sọ Ẹ̀gbá d'ominira; orin rẹ̀ ń dún títí di òní olóòní. (Lísàbí elevated the Ẹ̀gbá into sovereign liberty; his heroic anthem reverberates into this very dawn: Reverencing liberators and collective defiance against tyranny.)",
                "Ẹ̀gbá kì í ṣe ẹrú ẹnìkan; Olúmọ ní ń fún wa ní ààbò. (The Ẹ̀gbá shall never be the bonded thralls of any mortal; it is Olúmọ Rock that grants us eternal sanctuary: Affirming civic independence and ancestral pride.)",
                "Ìtàn là ń sọ, a kì í parọ́ ìṣẹ̀dálẹ̀; ẹni tí kò mọ ibi tó ti wá kò lè mọ ibi tó ń lọ. (History is what we recount, we never fabricate our origins; he who knows not his cradle can never comprehend his destination: Exhorting youth to study their ancestral genealogy.)"
            ],
            "provenance_and_citations": "Biobaku, Saburi O. (1957). The Egba and Their Neighbours: 1842–1872; Johnson, Rev. Samuel (1921). The History of the Yorubas; Falola, Toyin (1999). Yoruba Gurus: Indigenous Knowledge and the History of Nigeria."
        },
        "Àmalà Isu": {
            "historical_timeline": "Classical Agrarian Antiquity: Developed across the Ọ̀yọ́ and Ìbàdàn savanna heartland as the supreme yam flour swallow prepared from sun-dried dried yam slices (Èlùbọ́). Imperial Feasts: Standard noble repast served to the royal lineage and guests of the Aláàfin of Ọ̀yọ́. Contemporary Living Heritage: Unquestioned culinary centerpiece of Yorùbá festive gatherings, paired with Gbẹ̀gìrì and Èbìrì.",
            "proverbs_and_oral_traditions": [
                "Àmàlà la fi ń mọ ọmọ Ọ̀yọ́; bí omi kò bá gbóná, èlùbọ́ kì í dídùn. (By steaming Àmàlà is a true child of Ọ̀yọ́ recognized; if the water is not boiling hot, the yam flour can never turn supple and sweet: Teaching thorough preparation and cultural heritage.)",
                "Àmàlà gbígbóná kò ṣeé fi kánjú jẹ; sùúrù la fi ń gbádùn ọbẹ̀. (Hot steaming Àmàlà cannot be swallowed in reckless haste; it is with calm composure that one relishes rich broth: Enforcing patience and poise during prosperity.)",
                "Èlùbọ́ tó dára kì í kù lójú iná; ìwà rere ni àṣírí ẹni. (High-grade dried yam flour never discolors or lumps upon the hearth; noble character is a mortal's everlasting shield: Metaphor comparing quality craftsmanship to righteous behavior.)"
            ],
            "provenance_and_citations": "Bascom, William (1951). Yoruba Food; Fadipe, N.A. (1970). The Sociology of the Yoruba; Ojo, G.J. Afolabi (1966). Yoruba Culture: A Geographical Analysis."
        },
        "Àmalà Láfún": {
            "historical_timeline": "18th–19th Century Cassava Mastery: Pioneered in Ẹ̀gbá and Ìjẹ̀bú communities as a refined, light-colored fermented cassava swallow. Inter-State Commerce: Traded heavily along the Ogun River corridor to Lagos and coastal ports. Modern Continuity: Renowned as the signature culinary pride of Àbẹ́òkúta, celebrated for its smooth texture and light tartness.",
            "proverbs_and_oral_traditions": [
                "Láfún funfun kì í bẹ̀rù ọbẹ̀ ewédú; àjọṣe wọn dídùn ni tẹnu. (White Láfún has no fear of glossy Ewédú soup; their harmonious blend delights the palate: Symbolizing peaceful coexistence and mutual complementarity.)",
                "Ẹni tí ó jẹ láfún ní Àbẹ́òkúta kì í fẹ́ fẹ́rẹ́kú ní àjèjì. (He who relishes authentic Láfún in Àbẹ́òkúta longs never to linger in foreign exile: Expressing deep patriotic attachment to ancestral cuisine.)",
                "Ìfọwọ́sowọ́pọ̀ la fi ń gun láfún; kò sí iṣẹ́ tí ẹnìkan lè dá ṣe tán. (With coordinated rhythmic stirring is Láfún pounded; there is no great enterprise an individual can accomplish entirely alone: Teaching solidarity in community tasks.)"
            ],
            "provenance_and_citations": "Bascom, William (1951). Yoruba Food; Biobaku, Saburi O. (1957). The Egba and Their Neighbours: 1842–1872; Fadipe, N.A. (1970). The Sociology of the Yoruba."
        },
        "Dùndú": {
            "historical_timeline": "Ancient Agrarian Savanna: Savanna culinary delicacy of deep-fried peeled white yam slices, perfected by marketplace women guilds using boiling red palm oil or groundnut oil. Caravanserai Fare: Staple travel ration for merchants along the trans-Saharan and regional trade routes connecting Ọ̀yọ́-Ilé to Kano. Contemporary Street Food: Ubiquitous evening delicacy throughout urban and rural Yorùbáland.",
            "proverbs_and_oral_traditions": [
                "Dùndú gbígbóná la fi ń pa ebi ọ̀sán; àkókò kì í dúró de ẹnìkan. (With crisp piping-hot fried yam is midday hunger conquered; time waits for no mortal: Teaching diligence and prompt action.)",
                "Ẹpọ pupa l'ó ń fún dùndú ní àwọ̀; ẹgbẹ́ rere ní ń buyì kún ọmọlúwàbí. (It is pure red palm oil that bestows golden beauty upon fried yam; it is noble fellowship that adds radiant honor to a person of good character: Highlighting the uplifting influence of virtuous company.)",
                "Ẹni tí ó jẹ dùndú kò gbọ́dọ̀ gbagbé àwọn tó dán iná. (He who feasts upon savory fried yam must never forget the dedicated hands that stoked the hearth: Enforcing deep communal gratitude toward laborers.)"
            ],
            "provenance_and_citations": "Bascom, William (1951). Yoruba Food; Fadipe, N.A. (1970). The Sociology of the Yoruba; Falola, Toyin (1984). The Political Economy of a Pre-colonial African State: Ibadan, 1830–1900."
        },
        "Aṣẹ-Ẹ̀kọ": {
            "historical_timeline": "Guild Sieve Technology (Pre-colonial Era): Precision woven perforated filtration instrument crafted of palm fiber, horsehair, or pierced brass used by food guilds to filter fermented corn mash (Ògì). Standard Production: Guaranteed the lump-free, silky consistency demanded of royal and infant Ẹ̀kọ. Contemporary Legacy: Preserved in domestic culinary practice across southern Nigeria.",
            "proverbs_and_oral_traditions": [
                "Aṣẹ kì í jẹ́ kí èérún wọ ẹ̀kọ; àyẹ̀wò mímọ́ ló ń mú ìwà mọ́. (The fine sieve never permits coarse grit into smooth cornstarch; rigorous self-examination keeps personal character pure: Metaphor for moral self-scrutiny and discernment.)",
                "Bí aṣẹ kò bá fẹ́, ẹ̀kọ kì í jọ̀lọ̀; iṣẹ́ aṣeégbà ni a fi ń dé ipò gíga. (If the sieve is not fine, the pudding can never be smooth; meticulous labor is the true vehicle to high office: Teaching dedication to craft excellence.)",
                "Ọwọ́ tútù la fi ń mú aṣẹ; ìfọ̀kànbàlẹ̀ ló ń bí aṣeyọrí. (With steady cool hands is the sieve operated; composure and tranquility yield lasting success: Encouraging emotional balance during work.)"
            ],
            "provenance_and_citations": "Bascom, William (1951). Yoruba Food; Ojo, G.J. Afolabi (1966). Yoruba Culture: A Geographical Analysis; Fadipe, N.A. (1970). The Sociology of the Yoruba."
        },
        "Ata-Ọlọ́": {
            "historical_timeline": "Indigenous Stone-Grinding Tradition: Hand-carved granite saddle quern (Ọlọ́) and matching handheld stone roller (Ọmọ-Ọlọ́) used for millenia to crush fresh chili, locust beans (Iru), and indigenous herbs without bruising the seeds. Classical Culinary Guild: Preserved the essential oils and aromatic volatility of Yorùbá sauces. Living Kitchen Artifact: Still prized above electric blending in traditional culinary households for superior flavor release.",
            "proverbs_and_oral_traditions": [
                "Ọlọ́ kì í kọ ata; orí tí yóò dé adé kì í sá fún ìṣẹ́. (The grinding stone never recoils from hot spicy pepper; the head destined to wear a beaded crown never shrinks from rigorous trials: Teaching endurance as the prerequisite to greatness.)",
                "Ọmọ-ọlọ́ kì í bá ọlọ́ jà kí ilé má gbọ́; ìrẹ́pọ̀ ni agbára ìdílé. (The handheld roller never quarrels with the bed-stone without the kitchen hearing; harmonious collaboration is the fortress of the family: Urging domestic unity and mutual respect.)",
                "Ata tí a lọ lórí ọlọ́ ló ń ta kàkà nínú ọbẹ̀; àṣà ìbílẹ̀ kò lè di asán. (Pepper milled upon granite imparts the truest vitality to soup; our indigenous customs can never be rendered obsolete: Affirming the enduring superiority of cultural heritage.)"
            ],
            "provenance_and_citations": "Bascom, William (1951). Yoruba Food; Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle; Fadipe, N.A. (1970). The Sociology of the Yoruba."
        },
        "Gbégbé-Ọ̀bẹ": {
            "historical_timeline": "Ancient Blacksmith Guild Metallurgy: Forged ceremonial and multi-purpose iron blade produced by traditional master smiths (Àgbẹ̀dẹ) consecrated under the covenant of Ògún. Hunters & War Chieftains: Utilized by the Ọdẹ guilds and war leaders during the 18th–19th century regional defense campaigns. Contemporary Cultural Artifact: Carried as a dignity regalia badge by senior hunters and guild elders.",
            "proverbs_and_oral_traditions": [
                "Ọ̀bẹ kì í gbẹ́ igi tí kò ní èrò; ọgbọ́n ló ń darí agbára irin. (The forged blade never cuts wood without clear intention; wisdom must always guide the formidable strength of iron: Cautioning against reckless violence and asserting moral restraint.)",
                "Àgbẹ̀dẹ tó rọ ọ̀bẹ kì í jẹ́ kí abẹ rẹ̀ dákẹ́; iṣẹ́ ọwọ́ ni ọlá awo. (The master blacksmith who forged the blade never leaves its edge dull; skilled handiwork is the eternal glory of the guild: Exhorting professionals to maintain excellence.)",
                "Ẹni tí ó mú ọ̀bẹ lẹ́nu kì í bẹ̀rù igbó dídùn. (He who carries the tempered blade in hand walks through dense thickets without terror: Symbolizing courage anchored in prepared protection.)"
            ],
            "provenance_and_citations": "Ajayi, J.F.A. & Smith, Robert S. (1964). Yoruba Warfare in the Nineteenth Century; Johnson, Rev. Samuel (1921). The History of the Yorubas; Abiodun, Rowland (2014). Yoruba Art and Language."
        },
        "Ọ̀bẹ-Ìtù": {
            "historical_timeline": "Sacred Guild Metallurgy: Consecrated ritual blade specifically dedicated to the slaughter and dressing of sacrificial offerings in the groves of Ògún, Ṣàngó, and Ọya. Strict Liturgical Protocols: Handled exclusively by designated priests who observe ritual purity and ancestral incantations before drawing the iron. Transatlantic Retention: Survived in Afro-Cuban Ocha and Brazilian Candomblé Ketu liturgies as the consecrated knife (Obé).",
            "proverbs_and_oral_traditions": [
                "Ọ̀bẹ ìtù kì í ṣẹ̀jẹ̀ lásán; àṣẹ Ògún ló ń gbé e lẹ́sẹ̀. (The consecrated ritual blade never draws blood in vain; it is the cosmic sanction of Ògún that guides its path: Warning against profane violence and maintaining sanctity of life.)",
                "Ẹni tí ó fi ọ̀bẹ ìtù ṣeré yóò rí ìbínú irin. (He who treats the consecrated blade as a frivolous toy shall taste the fiery wrath of iron: Teaching profound reverence toward sacred objects.)",
                "Àwọn àgbà kì í fi ọ̀bẹ ìtù gé àkàrà; ohun tí ó tó la fi ń ṣe ohun tí ó wà. (The elders never employ a sacrificial knife to slice domestic bean-cakes; everything has its rightful purpose and sacred boundary: Emphasizing protocol and propriety.)"
            ],
            "provenance_and_citations": "Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society; Barnes, Sandra T. (1989). Africa's Ogun: Old World and New; Johnson, Rev. Samuel (1921). The History of the Yorubas."
        },
        "Ọ̀pá-Ìlẹ̀kẹ̀": {
            "historical_timeline": "Classical Ilé-Ifẹ̀ Monarchy: Beaded scepter of paramount authority handcrafted by the royal bead-embroiderers guild of Ilé-Ifẹ̀ using seed beads, glass, and coral. Imperial Symbolism: Wielded by crowned Ọbas (Ọba Aládé) during state processions and coronations as an extension of divine royal command (Àṣẹ). Living Royal Regalia: Essential ceremonial staff held by paramount sovereigns throughout Yorùbáland.",
            "proverbs_and_oral_traditions": [
                "Ọ̀pá-ìlẹ̀kẹ̀ l’ọwọ́ ọba kì í ṣe igi lásán; àṣẹ àwọn t’ayé-t’ọ̀run ló ń gbé. (The beaded staff in the monarch’s grasp is no common timber; it bears the cosmic sanction of both earthly and celestial realms: Affirming royal legitimacy rooted in sacred ethics.)",
                "Bí ọba bá fọwọ́ ba ọ̀pá-ìlẹ̀kẹ̀, gbogbo ilé á dákẹ́ rọ́rọ́. (When the sovereign rests his hand upon the beaded scepter, the entire assembly falls into reverent silence: Symbolizing civic reverence for peace and judicial order.)",
                "Ìlẹ̀kẹ̀ kì í já lójú ọba; ọlá kì í parun nílé ọmọlúwàbí. (The beads of state never shatter before a noble king; true honor never perishes in the household of the virtuous: Teaching the eternal endurance of righteousness.)"
            ],
            "provenance_and_citations": "Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle; Abiodun, Rowland (2014). Yoruba Art and Language; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art."
        },
        "Ikoko-Aró-Ìlẹ̀kẹ̀": {
            "historical_timeline": "Ancient Ilé-Ifẹ̀ Bead-Making Guilds: Refractory clay crucible vessel excavated at Olokun Grove and Igbo Olokun, utilized by classical master artisans to melt and fuse glass beads. Guild Secrecy: Guarded by hereditary bead-makers who understood precise furnace pyrotechnics and chemical fluxes. Archaeological Landmark: Yielded the famous Ifá dichroic and cylindrical polychrome glass beads admired globally.",
            "proverbs_and_oral_traditions": [
                "Iná kì í jó ikòkò-aró kí ó fọ́; ìfaradà la fi ń di àgbà. (The raging furnace fire never shatters the seasoned crucible; it is through steadfast endurance that one attains noble maturity: Comparing personal hardship to the tempering of sacred clay.)",
                "Ní inú ikòkò-aró ni ìlẹ̀kẹ̀ ọba ti ń jáde wá; ohun tó dára kì í wá lójú ẹsẹ̀. (From the deep crucible does the radiant royal bead emerge; exquisite beauty is never born in careless haste: Reminding youth that mastery requires patience.)",
                "Ẹni tí kò lè fara da ooru iná kò lè wọ ìlẹ̀kẹ̀ Olókun. (He who cannot endure the searing heat of the forge can never wear the resplendent beads of Olókun: Teaching that reward requires sacrifice and labor.)"
            ],
            "provenance_and_citations": "Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art; Willett, Frank (1967). Ife in the History of West African Sculpture; Fadipe, N.A. (1970). The Sociology of the Yoruba."
        },
        "Abẹ́-Ìlẹ̀kẹ̀": {
            "historical_timeline": "Fine Royal Crafts (Classical Ilé-Ifẹ̀ & Ọ̀yọ́): Specialized fine forged razor and awl instrument used by the bead-embroiderers guild to pierce, shave, and string intricate bead mosaics upon royal crowns, slippers, and cushions. Master Metallurgy: Required precise tempering so the razor could slice leather and vegetable thread without snapping. Modern Guild Preservation: Handed down through lineages of royal embroiderers in Ifẹ̀, Ọ̀yọ́, and Ìbàdàn.",
            "proverbs_and_oral_traditions": [
                "Abẹ́ tó mú kì í gé ọwọ́ olówó rẹ̀; ọgbọ́n la fi ń lo ohun èlò. (The sharpest razor never slices the hand of its master; it is with wisdom and focus that dangerous tools are wielded: Warning against negligence in handling power.)",
                "Iṣẹ́ abẹ́-ìlẹ̀kẹ̀ kì í ṣe iṣẹ́ kánjú; àfaradà la fi ń dé adé ọlá. (The fine work of the bead-piercer is not a labor of reckless rush; with patient diligence is the crown of glory adorned: Reminding craftsmen that precision takes time.)",
                "Ọwọ́ pípé ló ń fi abẹ́ kọ́ ìlẹ̀kẹ̀ dídán; ẹwà àti ìmọ̀ ni àṣẹ awo. (Only skilled hands guide the piercing blade to string radiant beads; beauty and technical knowledge form the true authority of the guild: Honoring guild craftsmanship.)"
            ],
            "provenance_and_citations": "Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle; Abiodun, Rowland (2014). Yoruba Art and Language; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art."
        },
        "Ẹ̀yọ̀-Ìlẹ̀kẹ̀": {
            "historical_timeline": "Ancient Bead Commerce & Currency: Individual perforated glass or stone bead units manufactured in classical Ilé-Ifẹ̀, ancient Kérou, and imported through Mediterranean caravan routes. Status Symbol: Worn as protective amulets, prestige necklaces, and lineage heirlooms by nobility and priests. Transatlantic Survival: Embedded in Afro-Cuban Elekes and Brazilian Guias as spiritual regalia badges.",
            "proverbs_and_oral_traditions": [
                "Ẹ̀yọ̀ ìlẹ̀kẹ̀ kan kì í dún; àpapọ̀ wọn ní ń di ọlá ọba. (A solitary single bead makes no rustling music; their united assembly constitutes the majesty of the king: Teaching that collective unity creates sovereign strength.)",
                "Bí ìlẹ̀kẹ̀ bá já sínú igbó, ẹni tó nífẹ̀ẹ́ rẹ̀ yóò wá a rí. (If a precious bead falls into the thicket, he who cherishes its worth will diligently search until it is found: Reaffirming the enduring value of noble character and heritage.)",
                "A kì í fi ẹ̀yọ̀ ìlẹ̀kẹ̀ ṣeré lójú awo; àṣírí la fi ń sọ àṣẹ. (One never treats sacred beads with careless levity before the initiated; with sacred reserve are divine gifts preserved: Enforcing reverence for consecrated regalia.)"
            ],
            "provenance_and_citations": "Eicher, Joanne B. (1976). Nigerian Handcrafted Textiles; Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art."
        },
        "Aro-Amọ̀": {
            "historical_timeline": "Domestic Architecture & Pottery Guild: Traditional triangular clay hearth foundation built of seasoned clay, loam, and straw to support cooking pots over firewood. Ancestral Kitchen Sanctum: Revered as the hearth-center (Àárín Ìmọ̀ / Ojú-Iná) where domestic nourishment, oral storytelling, and family warmth originate. Modern Living Continuity: Standard outdoor and indoor culinary foundation throughout rural Yorùbáland.",
            "proverbs_and_oral_traditions": [
                "Àrò mẹ́ta kì í da ọbẹ̀ nù; ìfọwọ́sowọ́pọ̀ ni ààbò ilé. (A three-stone hearth never spills the soup pot; steadfast cooperation is the impregnable shield of the household: Praising mutual balance, shared labor, and unity.)",
                "Bí àrò kò bá dán, iná kì í jó geregere; ìpìlẹ̀ rere ló ń bí ìgbéga. (If the clay hearth is not soundly molded, the flame cannot burn with bright vigor; a righteous foundation produces enduring elevation: Teaching that success requires stable beginnings.)",
                "Ojú àrò ni a ti ń kọ́ ọ̀rọ̀ àwọn àgbà; iná ń jó, ọgbọ́n ń gbilẹ̀. (At the warm fireside of the hearth do youth absorb the oral lore of the elders; as the flame dances, wisdom takes deep root: Celebrating traditional oral education.)"
            ],
            "provenance_and_citations": "Ojo, G.J. Afolabi (1966). Yoruba Culture: A Geographical Analysis; Fadipe, N.A. (1970). The Sociology of the Yoruba; Bascom, William (1951). Yoruba Food."
        },
        "Ikoko-Àmọ̀": {
            "historical_timeline": "Neolithic & Classical Ceramic Mastery: Hand-built earthenware pot formed by specialized women potters guilds without a potter's wheel, using coil techniques and pit firing. Functional Breadth: Ranged from water cooling jars (Àmù) and herbal cooking pots (Òru) to ritual dye vats (Ikòkò Aró). Enduring Living Craft: Renowned pottery centers in Ìlorin, Ìkòrò-Èkìtì, and Ẹ̀gbá continue continuous handcrafting.",
            "proverbs_and_oral_traditions": [
                "Ikòkò tó ń se omi tútù kì í fọ́ lásán; ìrẹ́pọ̀ àti àfaradà ni àṣẹ rẹ̀. (The clay vessel that cools living water never breaks without reason; poise and resilience form its inner grace: Praising gentle composure and domestic fortitude.)",
                "Amọ̀ l’a fi ń mọ ikòkò, erùpẹ̀ l’a fi ń kọ́ ilé; kò sí ẹni tó ju ilẹ̀ lọ. (From humble clay is the cooking pot shaped, from dust is the palace erected; no mortal transcends the sovereign earth: Teaching profound humility before nature.)",
                "Bí ikòkò bá fọ́, àwọn àbẹ̀tí rẹ̀ a di ohun ìkọ́kọ́; kò sí ohun tí kò ní èrò. (Even when the clay pot shatters, its shards find new life in hearth and altar; nothing in the cosmos is without divine purpose: Expressing indigenous cyclical resourcefulness.)"
            ],
            "provenance_and_citations": "Ojo, G.J. Afolabi (1966). Yoruba Culture: A Geographical Analysis; Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle; Fadipe, N.A. (1970). The Sociology of the Yoruba."
        },
        "Aba-Òfì": {
            "historical_timeline": "Ancient Textile Guild Loom Structure: The sturdy timber upright frame and shed-post forming the narrow-strip loom (Òfì) utilized by the male weavers guild (Aláṣọ Òfì). Savanna Weaving Centers: Established in Ìséyìn, Ọ̀yọ́, and Ìpèyí as the backbone of Aṣọ-Òkè production. Contemporary Industry: Remains the structural engine powering handwoven textile weaving in southwestern Nigeria.",
            "proverbs_and_oral_traditions": [
                "Bí àbá òfì kò bá fẹsẹ̀ múlẹ̀, aṣọ kì í jọ; ìpìlẹ̀ dídúró ni agbára iṣẹ́. (If the loom frame is not firmly anchored in earth, the warp threads can never unite in symmetry; a steadfast foundation is the strength of all endeavor: Metaphor for structural preparation.)",
                "Aláṣọ òfì kì í bẹ̀rù okùn dídíjú; ọgbọ́n la fi ń hun ọlá. (The master weaver never panics at tangled threads; with patient intellect is honor woven: Teaching problem-solving and perseverance.)",
                "Òfì kì í dákẹ́ láì kọrin; oríire ni ere iṣẹ́ àṣekára. (The loom never stays silent without singing its rhythmic click; prosperous honor is the rightful fruit of diligent labor: Exhorting industrious productivity.)"
            ],
            "provenance_and_citations": "Eicher, Joanne B. (1976). Nigerian Handcrafted Textiles; Fadipe, N.A. (1970). The Sociology of the Yoruba; Johnson, Rev. Samuel (1921). The History of the Yorubas."
        },
        "Àwọ̀n-Òfì": {
            "historical_timeline": "Textile Weaving Anatomy: The complex continuous cord heddle harness (Àwọ̀n) operated via foot pedals to separate alternate warp threads on the narrow-strip loom. Guild Engineering: Allowed the weaver to pass the wooden shuttle (Ọkọ̀) with lightning speed, creating intricate inlay motifs. Living Craft: Hand-knotted by veteran weavers according to ancient mathematical thread counts.",
            "proverbs_and_oral_traditions": [
                "Àwọ̀n òfì kì í da okùn sọnu; ìṣirò títọ́ ló ń gbé aṣọ dé ibi gíga. (The loom heddle never misplaces a single strand; accurate mathematical calculation brings the cloth to regal perfection: Praising rigorous technical discipline.)",
                "Bí ẹsẹ̀ bá tẹ àwọ̀n, ọwọ́ a da ọkọ̀ kọjá; àjọṣe gbogbo ara ni àṣeyọrí. (As the foot presses the heddle harness, the hand casts the wooden shuttle; full bodily coordination achieves the masterpiece: Teaching teamwork and harmonious execution.)",
                "Ẹni tó mọ àwọ̀n hun aṣọ ọba; ìmọ̀ àti ẹ̀kọ́ ni baba ọlá. (He who understands the complex harness weaves the robes of kings; knowledge and dedicated apprenticeship are the father of dignity: Honoring technical education.)"
            ],
            "provenance_and_citations": "Eicher, Joanne B. (1976). Nigerian Handcrafted Textiles; Ojo, G.J. Afolabi (1966). Yoruba Culture: A Geographical Analysis; Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle."
        },
        "Metropolitan Museum of Art African Collection": {
            "historical_timeline": "Late 19th & 20th Century Colonial Dispersion: Houses pivotal classical Yorùbá masterpieces (including Olowe of Ise carved palace doors, Gelede masks, and Ifa divination trays) acquired through private bequests (Michael C. Rockefeller wing). Provenance Transformation (21st Century): Subject to intensified digital provenance audits, repatriation dialogues, and source-community attribution parity. Educational Landmark: Serves as a major global conduit for international appreciation of classical Yorùbá sculptural ontology.",
            "proverbs_and_oral_traditions": [
                "Orí burúkú kì í d'adé; ohun tí ọwọ́ Ọlọ́wẹ̀ bá fọwọ́ kàn a di àkọsílẹ̀ àìkú. (An unworthy head never receives a royal crown; that which the sacred chisel of Ọlọ́wẹ̀ of Ìsẹ̀ touched became an imperishable testament: Celebrating artistic genius and cultural mastery.)",
                "Ẹrù tí a gbé lọ sí àjèjì yóò pada wálé; orírun kì í gbàgbé ọmọ rẹ̀. (The sacred treasures carried into foreign lands shall eventually return home; the ancestral cradle never forgets its rightful children: Affirming the moral inevitability of cultural restoration.)",
                "Iṣẹ́ ọnà baba wa kì í kú; níbi gbogbo l'ayé ti ń júbà ọgbọ́n Yorùbá. (The artworks of our ancestors can never perish; across all continents the world bows before the intellectual brilliance of the Yorùbá: Celebrating global cultural resonance.)"
            ],
            "provenance_and_citations": "Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art; Abiodun, Rowland (2014). Yoruba Art and Language; Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle."
        },
        "Ìrókẹ́ Ifá": {
            "historical_timeline": "Classical Ilé-Ifẹ̀ Sacred Regalia: Consecrated carved tapper crafted of ivory (Ìrókẹ́ Eyin Erin), cast brass, or seasoned hardwood, tapering to a point and featuring a kneeling female suppliant or horseman at its handle. Liturgical Protocol: Tapped gently upon the rim of the Ọpọ́n Ifá tray during invocation (Ìpè Ifá) to awaken the consciousness of Ọ̀rúnmìlà and the primordial ancestors. Diaspora Retention: Preserved in Cuban and Brazilian Ifá rites as the sacred tapper (Irofe).",
            "proverbs_and_oral_traditions": [
                "Ìrókẹ́ kì í kan ọpọ́n lásán; oríkì awo ló ń jí Ọ̀rúnmìlà. (The sacred tapper never strikes the divination tray in empty vanity; it is the deep liturgical panegyric that awakens Ọ̀rúnmìlà: Teaching that prayers must be offered with deep mindfulness and reverence.)",
                "Ẹyin erin l'a fi ń gbẹ́ ìrókẹ́ ọba; ọlá ńlá kì í ṣe ti ẹ̀tẹ̀. (From the ivory tusk of the elephant is the royal tapper carved; supreme majesty never associates with disgrace: Metaphor associating sacred tools with moral nobility.)",
                "Bí awo bá mú ìrókẹ́ dání, gbogbo àwọn aláìrí a tẹ́tí sílẹ̀. (When the diviner lifts the sacred tapper, all unseen spiritual forces incline their ears to listen: Emphasizing the metaphysical potency of consecrated prayer.)"
            ],
            "provenance_and_citations": "Abimbola, Wande (1976). Ifa: An Exposition of Ifa Literary Corpus; Drewal, H.J. & Pemberton, J. (1989). Yoruba: Nine Centuries of African Art; Bascom, William (1969). Ifa Divination."
        },
        "Owó-Babà": {
            "historical_timeline": "Pre-Colonial Monetary Medium: Traditional copper and brass manilla tokens and forged brass bracelets (Owó Babà) utilized as high-value currency units and prestige bridewealth across eastern Yorùbáland (Ondo, Owo, Ekiti). Imperial Metallurgy: Forged in guild smelters as tokens of sovereign alliance and covenant seals between kingdoms. Historical Succession: Preceded and coexisted with cowrie shells (Owó Ẹyọ) before 20th-century colonial coinage.",
            "proverbs_and_oral_traditions": [
                "Owó babà kì í ṣe owó kánjú; àwọn àgbà ló ń fún ni ní ọlá. (Brass currency is not the wealth of impetuous youth; it is the seasoned elders who bestow true civic dignity: Teaching that lasting wealth is earned through patience and wisdom.)",
                "Ẹni tó ní babà l’ọ́wọ́ kì í bẹ̀rù ìyàn; ìpìlẹ̀ owó ni ìfipamọ́. (He who possesses brass in reserve harbors no dread of famine; savings and tangible reserves are the fortress of fortune: Praising fiscal discipline and foresight.)",
                "Idẹ kì í ṣe irin lásán, babà kì í kù; orúkọ rere ní ń buyì kún ọ̀rọ̀. (Bronze is no ordinary iron, brass never tarnishes into nothingness; a virtuous name elevates wealth into eternal nobility: Reminding that character outlasts coin.)"
            ],
            "provenance_and_citations": "Johnson, Rev. Samuel (1921). The History of the Yorubas; Fadipe, N.A. (1970). The Sociology of the Yoruba; Smith, Robert S. (1988). Kingdoms of the Yoruba."
        },
        "Òrìṣà": {
            "historical_timeline": "Primordial Ilé-Ifẹ̀ Epistemology: Cosmological pantheon of 401 divine emissaries and archetypal forces (Irúnmọlẹ̀) embodying the manifestations of Olódùmarè across nature, elements, and moral character. Classical Deification: Mythohistorical kings, queens, and culture heroes (Ọbàtálá, Ògún, Ṣàngó, Ọ̀ṣun, Ọya) whose mortal excellence transcended terrestrial mortality into immortal celestial energies. Transatlantic Global Presence: Sustained millions through the Atlantic Middle Passage, flourishing as Santería (Cuba), Candomblé (Brazil), Shango Baptist (Trinidad), and Vodou-related rites.",
            "proverbs_and_oral_traditions": [
                "Òrìṣà bí orí kò sí; orí l’a fi ń kọ́kọ́ bọ́ kí a tó bọ Òrìṣà. (There is no deity greater than personal destiny and consciousness; it is the inner head that must be venerated before all external spirits: Teaching self-responsibility and cosmic alignment.)",
                "Bí Òrìṣà kò bá lè gbè mí, kò gbọ́dọ̀ dẹ́ kù mí; ìwà mi ni àṣẹ mi. (If the deity cannot elevate me, let it not diminish me; my own moral character is my divine sanction: Asserting personal agency and moral accountability.)",
                "Àwọn Òrìṣà kì í jẹ́ kí ilẹ̀ ayé dárú; àlàáfíà ni èrè ẹbọ. (The divine pantheon never permits the world to spiral into eternal ruin; lasting peace is the true reward of sacrifice and reverence: Affirming cosmic balance.)"
            ],
            "provenance_and_citations": "Abiodun, Rowland (2014). Yoruba Art and Language; Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society; Bascom, William (1969). Ifa Divination."
        },
        "Aṣọ": {
            "historical_timeline": "Classical Antiquity: Textile art traditions tracing back to Ilé-Ifẹ̀ and Old Ọ̀yọ́, producing indigenous handwoven cottons, silk wild-silk fabrics (Sányán), and indigo-dyed cloth (Àdìrẹ). Cultural Semiotics: Serves as the quintessential visual marker of civic dignity (Ọmọlúwàbí), gender poise, marital status, and social guild membership. Global Diaspora Influence: Resonates across world fashion, African diaspora regalia, and international runway design.",
            "proverbs_and_oral_traditions": [
                "Aṣọ kì í ṣe ohun lásán; ìbòrí àṣírí ni aṣọ fún ọmọlúwàbí. (Cloth is no mere garment; it is the sacred veil of personal dignity and honor for the virtuous person: Teaching modesty, self-respect, and social poise.)",
                "Bí a bá wọ aṣọ tí kò tọ́, a kì í dé àpèjọ àwọn àgbà. (If one is clad in disorderly garments, one cannot step into the solemn council of the elders: Enforcing visual decorum and civic respect.)",
                "Aṣọ rere kì í parọ́ ọlá; ẹwà inú ló ń tan aṣọ lójú. (Fine cloth never counterfeits true honor; it is inner moral beauty that illuminates the apparel: Affirming that character outshines clothing.)"
            ],
            "provenance_and_citations": "Eicher, Joanne B. (1976). Nigerian Handcrafted Textiles; Lawal, Babatunde (1996). The Gẹlẹdẹ Spectacle; Fadipe, N.A. (1970). The Sociology of the Yoruba."
        },
        "Ewé": {
            "historical_timeline": "Ancient Sacred Botany & Herbalism: Pharmacopeia of thousands of consecrated plants, vines, bark, and roots systematized through the wisdom of Ọ̀sanyìn and Ọ̀rúnmìlà. Indigenous Medicine Guild: Master herbalists (Oníṣègùn) and priests (Babaláwo) combine chemical pharmacological properties with spoken incantations (Ọ̀fọ̀) to heal disease and balance spiritual disequilibrium. Transatlantic Diaspora Matrix: Preserved in the botanical pharmacopeia of Cuba, Brazil, and Haiti.",
            "proverbs_and_oral_traditions": [
                "Kò sí ewé tí kò ní orúkọ; kò sí ewé tí kò ní iṣẹ́ nínú igbó. (There is no leaf without an ancestral name; there is no plant without a healing purpose in the forest: Teaching that every creation possesses divine purpose and therapeutic utility.)",
                "Ewé tútù la fi ń wo egbò; sùúrù àti ìmọ̀ ni baba gbogbo egbòogi. (With fresh cool leaves is the wound dressed; patience and deep botanical knowledge are the father of all remedies: Praising clinical expertise and gentle healing.)",
                "Ẹni tí ó mọ ewé mọ ẹ̀dá; Ọ̀sanyìn kì í jẹ́ kí awo tẹ́. (He who understands the secrets of sacred leaves understands the mysteries of creation; Ọ̀sanyìn never lets the true practitioner fall into disgrace: Celebrating indigenous botanical science.)"
            ],
            "provenance_and_citations": "Verger, Pierre Fatumbi (1995). Ewé: The Use of Plants in Yoruba Society; Fadipe, N.A. (1970). The Sociology of the Yoruba; Bascom, William (1969). Ifa Divination."
        }
    }
}

if __name__ == "__main__":
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(BATCH_5_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated {len(BATCH_5_DATA['batch_5_enrichments'])} scholarly enrichments in {OUTPUT_PATH.name}")
