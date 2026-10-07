import React, { useState } from 'react';
import { Send, Sparkles, BookOpen, User, Bot, AlertCircle } from 'lucide-react';

export default function ChatTab({ apiBaseUrl }) {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'Ẹ kàábọ̀! I am the Àgbà Cultural Scholar. Ask me any question regarding classical Yorùbá history, royal regalia, Odù Ifá divination, philosophy, or indigenous traditions. All responses are strictly grounded in our 1,240-entity sovereign archive.',
      sources: []
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

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
      console.warn('API error during chat:', err);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: `Àkíyèsí (Notice): The chat service is currently connecting to the sovereign backend. Please verify your connection to Google Cloud Run.`,
          sources: []
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '980px', margin: '0 auto', padding: '0 16px' }}>
      <div className="glass-panel" style={{ padding: '24px', borderRadius: '16px', minHeight: '620px', display: 'flex', flexDirection: 'column' }}>
        {/* Header */}
        <div style={{ borderBottom: '1px solid var(--border-subtle)', paddingBottom: '16px', marginBottom: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h2 className="font-royal text-gold" style={{ fontSize: '1.6rem', marginBottom: '4px' }}>
              💬 Grounded Conversational Cultural Scholar
            </h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Zero-hallucination RAG backed by the 1,240-entity master corpus and 256 Odù Ifá matrix.
            </p>
          </div>
          <span className="badge-gold">
            <Sparkles size={14} /> Gemini 2.5 Grounded
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
                <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: 'linear-gradient(135deg, #d4af37, #8c6710)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                  👑
                </div>
              )}
              <div
                style={{
                  background: m.role === 'user' ? 'rgba(212, 175, 55, 0.15)' : 'rgba(15, 23, 42, 0.8)',
                  border: m.role === 'user' ? '1px solid var(--gold-border)' : '1px solid var(--border-subtle)',
                  borderRadius: '14px',
                  padding: '16px 20px',
                  color: '#f8fafc',
                  lineHeight: 1.6
                }}
              >
                <div style={{ whiteSpace: 'pre-wrap', fontSize: '0.96rem' }}>{m.content}</div>

                {m.sources && m.sources.length > 0 && (
                  <div style={{ marginTop: '12px', paddingTop: '10px', borderTop: '1px solid rgba(255, 255, 255, 0.08)', fontSize: '0.78rem', color: 'var(--gold-light)' }}>
                    <strong>Canonical Grounding Sources:</strong> {m.sources.map((s) => s.title).join(', ')}
                  </div>
                )}
              </div>
              {m.role === 'user' && (
                <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: 'rgba(56, 189, 248, 0.2)', border: '1px solid #38bdf8', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                  <User size={18} color="#38bdf8" />
                </div>
              )}
            </div>
          ))}
          {loading && (
            <div style={{ display: 'flex', gap: '12px', alignItems: 'center', color: 'var(--gold-light)', fontSize: '0.9rem' }}>
              <span>👑 Àgbà Scholar is consulting the canonical archives...</span>
            </div>
          )}
        </div>

        {/* Prompt Input Form */}
        <form onSubmit={handleSend} style={{ display: 'flex', gap: '12px' }}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about Ògún, sacred crowns, Odù Ifá, marriage customs, or royal regalia..."
            disabled={loading}
            style={{
              flex: 1,
              background: 'rgba(0,0,0,0.4)',
              border: '1px solid var(--border-subtle)',
              borderRadius: '24px',
              padding: '14px 22px',
              color: '#fff',
              fontSize: '0.98rem',
              outline: 'none'
            }}
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="btn-gold"
            style={{ padding: '0 24px', borderRadius: '24px', display: 'flex', alignItems: 'center', gap: '8px' }}
          >
            <Send size={16} /> Send
          </button>
        </form>
      </div>
    </div>
  );
}
