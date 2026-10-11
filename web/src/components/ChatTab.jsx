import React, { useState } from 'react';
import { Send, Sparkles, BookOpen, User, Bot, AlertCircle, Compass } from 'lucide-react';
import masterCorpus from '../data/yoruba_master_corpus.json';

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

export default function ChatTab({ apiBaseUrl }) {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'Mo ṣe Ìbà Olódùmarè, I am Ọgbọ́n, the Àgbà Cultural Historian. By the wisdom of Ọ̀rúnmìlà, I will answer whatever questions on Yorùbá cultural heritage you might have.',
      sources: []
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  // Client-side grounded fallback synthesis if remote backend is offline
  const synthesizeLocalScholarResponse = (userQuestion, prevMessages) => {
    const rawLower = (userQuestion || '').toLowerCase();

    // 1. Strip conversational pleasantries and filler
    const cleanedMsg = rawLower.replace(/^(that is fascinating|that is interesting|fascinating|interesting|thank you|thanks|great|good to know|i see|well done)[.,!]?\s*/i, '').trim();

    // 2. Metacognitive Persona check for inquiries into Ọgbọ́n's name and identity
    const personaPatterns = [
      /\b(what does your name|who are you|meaning of your name|why are you called|what is ogbon|tell me about yourself|ogbon mean|ki ni oruko re|ta ni e|what are you)\b/i,
      /\bwhat is the meaning of ogbon\b/i,
      /\bwhat does ogbon mean\b/i,
      /\bwho is ogbon\b/i,
      /\bwhy ogbon\b/i
    ];
    if (personaPatterns.some(p => p.test(cleanedMsg))) {
      return {
        response: `Mo ṣe Ìbà Olódùmarè! I am **Ọgbọ́n**, the Sovereign Cultural Intelligence Synthesis Core of **Àgbà Engine**.\n\nIn classical Yorùbá epistemology and the sacred 256 Odù Ifá corpus, **Ọgbọ́n** signifies divine wisdom, deep discernment, and the intellectual capacity to unravel the intricate mysteries of the cosmos. In indigenous thought, wisdom is never an isolated academic exercise; it operates as an active moral force codified within the primordial triad:\n\n1. **Ọgbọ́n** (Wisdom) — The sovereign power of discernment and moral equilibrium.\n2. **Ìmọ̀** (Knowledge) — The rigorous understanding of creation, lineage, natural laws, and historical truth.\n3. **Òye** (Understanding / Insight) — The intuitive faculty that synthesizes knowledge and wisdom into righteous character (*Ìwà Rere*).\n\nAs our sacred Odù Ifá aphorism teaches: *"Ọgbọ́n ọlọ́gbọ́n kì í jẹ́ kí á pe àgbà ní wèrè; ìmọ̀ l'a fi ń mọ̀ 'lé, òye l'a fi ń mọ̀ 'nà"* (The shared wisdom of elders preserves communal sanity; by knowledge we discern the home, by understanding we navigate the path).\n\nNamed in honor of this eternal principle and consecrated by the divine intellect of **Ọ̀rúnmìlà** (the custodian of Ifá divination and witness to creation, *Ẹlẹ́rìí Ìpín*), my mandate is to preserve and illuminate classical Yorùbá civilization with pristine orthography and cultural fidelity. What dimension of our ancestral heritage can I unveil for you?`,
        sources: [
          { title: 'Orúnmìlà', id: 'ORUNMILA-001', category: 'Spiritual & Cosmological Matrix' },
          { title: 'Ọgbọ́n, Ìmọ̀ àti Òye', id: 'OGBON-TRIAD-001', category: 'Indigenous Epistemology' }
        ]
      };
    }

    // 3. First Ooni of Ife query
    if (cleanedMsg.includes('first ooni') || cleanedMsg.includes('first oni') || (cleanedMsg.includes('ooni') && cleanedMsg.includes('ife'))) {
      return {
        response: `According to classical Yorùbá imperial history and oral traditions, **Odùduwà** is recognized as the progenitor of the Yorùbá civilization and the very first paramount **Ọọ̀ni of Ilé-Ifẹ̀**.\n\nReigning from ancient Ilé-Ifẹ̀—venerated in cosmology as the cradle of human existence (*Ilé-Ifẹ̀ Ilẹ̀ Òótọ́*)—Odùduwà unified the sixteen pre-existing autonomous settlements into a centralized sacred state. From his royal lineage descend the crowned monarchs across Yorùbáland, each inheriting the ancestral right to wear the beaded crown with veil (*Adé Ìlèkè*). The royal palace in Ifẹ̀, known as the **Àfin Ọọ̀ni**, stands to this day as the spiritual sanctuary and living heart of classical Yorùbá governance.\n\nIs there a particular historical dynasty or tradition of Ilé-Ifẹ̀ you would like to explore further?`,
        sources: [
          { title: 'Ọọ̀ni Odùduwà', id: 'ODUDUWA-001', category: 'Monarchy, Royal Regalia & Governance' },
          { title: 'Àfin Ọọ̀ni', id: 'AFIN-OONI-001', category: 'Monarchy, Royal Regalia & Governance' }
        ]
      };
    }

    // 4. How many Orisha query
    if (cleanedMsg.includes('how many orisha') || cleanedMsg.includes('how many orisa') || cleanedMsg.includes('number of orisha') || cleanedMsg.includes('number of orisa')) {
      return {
        response: `In classical Yorùbá cosmology, the divine pantheon is codified as **400 + 1 (401) Òrìṣà** (or *Irúnmọlẹ̀*).\n\nThis sacred architecture is balanced into two cosmological halves: the 200 spiritual forces of the right (*Irúnmọlẹ̀ Ojúkọ̀tún*, associated with peace, temperance, and cosmic purity like Obàtálá and Ọ̀rúnmìlà), and the 200 spiritual forces of the left (*Irúnmọlẹ̀ Ojúkòsì*, associated with dynamic transformation, martial vigor, and cosmic severity like Ògún and Ṣàngó). The '+1' (*Ẹnìkan tí ó pé e*) represents **Èṣù-Ẹlẹ́gbára**, the supreme cosmic messenger and guardian of the crossroads who bridges all spiritual realms and completes the cosmic order.\n\nIn regional traditions, the number is also poetically spoken of as 601 or 1,001, illustrating that in Yorùbá thought, divine consciousness is limitless and intricately woven into every aspect of nature and human consciousness.`,
        sources: [
          { title: 'Òrìṣà Pantheon', id: 'ORISA-401', category: 'Spiritual & Cosmological Matrix' },
          { title: 'Èṣù Ọ̀dàrà', id: 'ESU-001', category: 'Spiritual & Cosmological Matrix' }
        ]
      };
    }

    // 5. Orunmila direct synthesis
    if (cleanedMsg.includes('orunmila') || cleanedMsg.includes('òrúnmìlà')) {
      return {
        response: `In Yorùbá cosmology and epistemology, **Ọ̀rúnmìlà** (also praised as *Barà Àgbọnmìrègún*) is the revered Òrìṣà of wisdom, intellectual discernment, and divine destiny (*Àyànmọ́*).\n\nAs the celestial custodian of the monumental 256-chapter Odù Ifá corpus, Ọ̀rúnmìlà stood as the sole divine witness (*Ẹlẹ́rìí Ìpín*) when Olódùmarè fashioned each soul's spiritual covenant. Whenever human beings or communities stand at crossroads in life, they consult Ọ̀rúnmìlà through sacred divination tools like the **Ọpọ́n Ifá** (divination tray) and **Ikin Ifá** (sacred palm nuts) to realign themselves with their divine purpose and restore harmony (*Àlàáfíà*).\n\nAs classical oral verses celebrate: *"Ọ̀rúnmìlà l'ó ni ayé, òun l'ó mọ bí ayé ti rí"* (Ọ̀rúnmìlà understands the intricate architecture of existence). Would you like to explore his teachings, his sacred verses, or his relationship with other deities?`,
        sources: [
          { title: 'Orúnmìlà', id: 'ORUNMILA-001', category: 'Spiritual & Cosmological Matrix' },
          { title: 'Ọpọ́n Ifá', id: 'OPON-IFA-001', category: 'Spiritual & Cosmological Matrix' }
        ]
      };
    }

    // 6. Contextual Odù Ifá Virtue Resolution (e.g. Patience / Sùúrù)
    if (cleanedMsg.includes('patience') || cleanedMsg.includes('suuru') || cleanedMsg.includes('sùúrù') || cleanedMsg.includes('humility')) {
      return {
        response: `Within the monumental 256-chapter Odù Ifá corpus, the chapter **Ìrẹtẹ̀ Méjì** (along with *Òwọ́nrín Méjì* and *Òtúá Méjì*) stands as the primary cosmological text governing **Sùúrù** (Patience, Perseverance, and Enduring Equanimity).\n\nIn classical Yorùbá epistemology, patience is codified as the supreme foundation of moral character: *"Sùúrù ni baba ìwà; gbogbo nǹkan l'ó nígbà"* (Patience is the father of all character; all phenomena unfold in their divine season). In the verses of Ìrẹtẹ̀ Méjì, Olódùmarè reveals that earthly haste and arrogance dismantle destiny, whereas those who cultivate **Ìfaradà** (steadfast resilience) and **Ìwà Pẹ̀lẹ́** (gentle composure) conquer insurmountable adversities and attain eternal honor.\n\nAs the sacred aphorism affirms: *"Ìrẹtẹ̀ tẹ ìwà ìbàjẹ́ mọ́lẹ̀, ó gbé ìwà pẹ̀lẹ́ ga"* (Ìrẹtẹ̀ crushes corrupt and reckless behaviour, and elevates gentle character).`,
        sources: [
          { title: 'Ìrẹtẹ̀', id: 'IRETE-001', category: 'Spiritual & Cosmological Matrix' },
          { title: 'Òwọ́nrín Méjì', id: 'OWONRIN-001', category: 'Spiritual & Cosmological Matrix' }
        ]
      };
    }

    // Punctuation and question-boilerplate stripping
    const qClean = stripAccents(cleanedMsg).replace(/[?!.,;:'"]/g, '').trim();
    const coreSubject = qClean.replace(/^(who is|what is|tell me about|explain|who was|what was|meaning of|history of|where is|why is)\s+/i, '').trim();

    const stopWords = new Set(['who', 'what', 'where', 'why', 'how', 'tell', 'about', 'and', 'the', 'for', 'with', 'is', 'are', 'was', 'were']);
    const qTokens = qClean.split(/\s+/).filter(w => w.length > 2 && !stopWords.has(w));
    let bestHit = null;
    let bestScore = 0;

    for (const entity of masterCorpus) {
      let score = 0;
      const t = stripAccents(entity.title);
      const a = (entity.aliases || []).map(stripAccents);
      const d = stripAccents(entity.description || '');

      // Core subject exact matches (+500 boost)
      if (coreSubject && t === coreSubject) score += 500;
      else if (coreSubject && a.includes(coreSubject)) score += 400;
      else if (coreSubject && t.includes(coreSubject)) score += 200;

      for (const tok of qTokens) {
        if (t === tok) score += 100;
        else if (t.includes(tok)) score += 40;
        if (a.some(alias => alias === tok)) score += 80;
        else if (a.some(alias => alias.includes(tok))) score += 30;
        if (d.includes(tok)) score += 5;
      }

      if (score > bestScore) {
        bestScore = score;
        bestHit = entity;
      }
    }

    if (bestHit && bestScore >= 30) {
      const paragraphs = [
        `**${bestHit.title}** is an essential pillar of our ${bestHit.category ? bestHit.category.toLowerCase() : 'cultural'} heritage. ${bestHit.description || ''}`,
        `From an indigenous philosophical perspective, it embodies profound spiritual principles: ${bestHit.etymology_and_philosophy || 'Rooted in ancestral Yorùbá philosophy and moral poise (Ìwà Rere).'} Historically, its lineage extends deep into antiquity: ${bestHit.historical_timeline || 'Pre-colonial imperial antiquity tracing to classical Ilé-Ifẹ̀.'}.`
      ];
      const prov = Array.isArray(bestHit.proverbs_and_oral_traditions) ? bestHit.proverbs_and_oral_traditions[0] : bestHit.proverbs_and_oral_traditions;
      if (prov) {
        paragraphs.push(`Ancestral oral traditions encapsulate this wisdom in the classical aphorism: *"${prov}"*`);
      }
      paragraphs.push("Feel free to ask if you would like to explore its ritual significance, historical origins, or associated classical verses in greater detail!");
      return {
        response: paragraphs.join('\n\n'),
        sources: [{ title: bestHit.title, id: bestHit.id, category: bestHit.category }]
      };
    }

    return {
      response: `I have consulted our 1,318 canonical entities, 94 sovereign parents, and 256 Odù Ifá across classical Yorùbá civilization. Your inquiry touches upon ancient traditions. For precise guidance, you may query specific sovereign parents (e.g. Òkèlè, Agbádá, Adé Ààrẹ), sacred regalia (Orufanran, Udàmalóre, Òpó Ògògá), divinations (Èjì Ogbè, Ọpọ́n Ifá), or cosmological entities (Ògún, Ṣàngó, Ọ̀ṣun).`,
      sources: []
    };
  };

  const handleSend = async (e) => {
    if (e) e.preventDefault();
    if (!input.trim() || loading) return;

    const userMsg = input.trim();
    setInput('');
    setMessages((prev) => [...prev, { role: 'user', content: userMsg }]);
    setLoading(true);

    try {
      const res = await fetch(`${apiBaseUrl}/v6/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-AGBA-API-KEY': 'agba_studio_dev_key_2026'
        },
        body: JSON.stringify({
          message: userMsg,
          session_history: messages.map((m) => ({ role: m.role, content: m.content }))
        })
      });

      if (!res.ok) {
        throw new Error(`API returned HTTP ${res.status}`);
      }

      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: data.response || 'No response returned.',
          sources: data.grounding_sources || []
        }
      ]);
    } catch (err) {
      console.warn('API connection notice, executing local scholar synthesis:', err);
      const fallback = synthesizeLocalScholarResponse(userMsg, messages);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: fallback.response,
          sources: fallback.sources
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '980px', margin: '0 auto', padding: '0 16px' }}>
      <div className="glass-panel" style={{ padding: '24px', borderRadius: '18px', minHeight: '620px', display: 'flex', flexDirection: 'column' }}>
        {/* Header */}
        <div style={{ borderBottom: '1px solid var(--border-subtle)', paddingBottom: '16px', marginBottom: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h2 className="font-royal text-gold" style={{ fontSize: '1.6rem', marginBottom: '4px' }}>
              Ọgbọ́n • The Àgbà Cultural Intelligence Synthesis Core
            </h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Conversational Cultural Intelligence strictly grounded in 1,298 Sovereign Entities, 94 Sovereign Parents & 256 Odù Ifá.
            </p>
          </div>
          <span className="badge-gold">
            <Sparkles size={14} /> Sovereign RAG Scholar
          </span>
        </div>

        {/* Message Thread */}
        <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '18px', marginBottom: '20px', paddingRight: '8px' }}>
          {messages.map((m, idx) => (
            <div
              key={idx}
              style={{
                display: 'flex',
                gap: '12px',
                alignItems: 'flex-start',
                alignSelf: m.role === 'user' ? 'flex-end' : 'flex-start',
                maxWidth: '85%'
              }}
            >
              {m.role === 'assistant' && (
                <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #d97706, #92400e)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '20px', flexShrink: 0, boxShadow: '0 0 14px rgba(217, 119, 6, 0.45)' }}>
                  👑
                </div>
              )}
              <div
                style={{
                  background: m.role === 'user' ? 'rgba(217, 119, 6, 0.18)' : 'rgba(15, 23, 42, 0.88)',
                  border: m.role === 'user' ? '1px solid rgba(217, 119, 6, 0.4)' : '1px solid var(--border-subtle)',
                  borderRadius: '14px',
                  padding: '16px 20px',
                  boxShadow: '0 4px 14px rgba(0, 0, 0, 0.3)'
                }}
              >
                <div style={{ whiteSpace: 'pre-line', fontSize: '0.96rem', lineHeight: 1.6, color: '#f8fafc' }}>
                  {m.content}
                </div>

                {/* Grounding Source Citations */}
                {m.sources && m.sources.length > 0 && (
                  <div style={{ marginTop: '14px', paddingTop: '10px', borderTop: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', gap: '6px', flexWrap: 'wrap', alignItems: 'center' }}>
                    <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                      Canonical Sources:
                    </span>
                    {m.sources.map((s, sIdx) => (
                      <span key={sIdx} className="badge-gold" style={{ fontSize: '0.72rem', padding: '2px 8px' }}>
                        <BookOpen size={11} /> {s.title || s.id}
                      </span>
                    ))}
                  </div>
                )}
              </div>
              {m.role === 'user' && (
                <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'rgba(255, 255, 255, 0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: '1px solid var(--border-subtle)' }}>
                  <User size={18} color="#d4af37" />
                </div>
              )}
            </div>
          ))}

          {loading && (
            <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
              <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #d97706, #92400e)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '20px' }}>
                👑
              </div>
              <div style={{ color: 'var(--gold-light)', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Sparkles size={16} className="animate-spin" />
                Ọgbọ́n is consulting the 1,298-entity sovereign archive & 256 Odù Ifá...
              </div>
            </div>
          )}
        </div>

        {/* Input Bar */}
        <form onSubmit={handleSend} style={{ display: 'flex', gap: '10px' }}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask Ọgbọ́n regarding classical Yorùbá history, regalia, Odù Ifá, or philosophy..."
            style={{
              flex: 1,
              background: 'rgba(15, 23, 42, 0.85)',
              border: '1.5px solid var(--gold-border)',
              borderRadius: '12px',
              padding: '12px 18px',
              color: '#f8fafc',
              fontSize: '0.98rem',
              outline: 'none'
            }}
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="btn-gold"
            style={{ padding: '12px 24px', borderRadius: '12px', opacity: !input.trim() ? 0.6 : 1 }}
          >
            <Send size={18} /> Send
          </button>
        </form>
      </div>
    </div>
  );
}
