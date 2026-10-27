import React from 'react';
import { Wand2, Copy } from 'lucide-react';

export default function DiacritizerCard({
  asciiInput,
  setAsciiInput,
  diacritizedOutput,
  diacritizing,
  onDiacritize
}) {
  return (
    <div className="glass-panel" style={{ padding: '32px', borderRadius: '18px' }}>
      <div style={{ marginBottom: '24px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.6rem', marginBottom: '6px' }}>
          Universal 25-Letter Yorùbá Orthographic Restorer
        </h3>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
          Restores authentic sub-dots (ẹ, ọ, ṣ) and tonal contours (Àmì Ohùn: Re, Mi, Do) from ASCII input.
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', marginBottom: '24px' }}>
        <div>
          <label style={{ display: 'block', fontSize: '0.85rem', color: 'var(--gold-light)', marginBottom: '8px', fontWeight: 600 }}>
            Raw ASCII Yorùbá Input:
          </label>
          <textarea
            value={asciiInput}
            onChange={(e) => setAsciiInput(e.target.value)}
            rows={6}
            style={{
              width: '100%',
              background: 'rgba(15, 23, 42, 0.85)',
              border: '1px solid var(--border-subtle)',
              borderRadius: '12px',
              padding: '14px',
              color: '#f8fafc',
              fontSize: '1rem',
              fontFamily: 'monospace',
              outline: 'none',
              resize: 'vertical'
            }}
          />
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '0.85rem', color: 'var(--gold-light)', marginBottom: '8px', fontWeight: 600 }}>
            Pristine 25-Letter Restored Output:
          </label>
          <div
            style={{
              width: '100%',
              minHeight: '160px',
              background: 'rgba(12, 17, 26, 0.95)',
              border: '1px solid var(--gold-border)',
              borderRadius: '12px',
              padding: '14px',
              color: diacritizedOutput ? '#f8fafc' : 'var(--text-muted)',
              fontSize: '1.05rem',
              fontWeight: diacritizedOutput ? 600 : 400,
              whiteSpace: 'pre-wrap'
            }}
          >
            {diacritizedOutput || 'Restored text with accurate tone marks will appear here...'}
          </div>
        </div>
      </div>

      <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px' }}>
        {diacritizedOutput && (
          <button
            onClick={() => navigator.clipboard.writeText(diacritizedOutput)}
            className="btn-ghost"
            style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <Copy size={16} /> Copy Output
          </button>
        )}
        <button
          onClick={onDiacritize}
          disabled={diacritizing || !asciiInput.trim()}
          className="btn-gold"
          style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 24px' }}
        >
          <Wand2 size={16} />
          {diacritizing ? 'Restoring Tonal Contours...' : 'Restore Orthography'}
        </button>
      </div>
    </div>
  );
}
