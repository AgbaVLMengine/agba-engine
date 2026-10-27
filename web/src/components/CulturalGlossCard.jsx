import React from 'react';
import { BookOpen, Feather } from 'lucide-react';

export default function CulturalGlossCard({
  culturalInput,
  setCulturalInput,
  culturalResult,
  translating,
  onCulturalTranslate
}) {
  return (
    <div className="glass-panel" style={{ padding: '32px', borderRadius: '18px' }}>
      <div style={{ marginBottom: '24px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.6rem', marginBottom: '6px' }}>
          Sacred Translation & Deep Metaphysical Glossing
        </h3>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
          Dual-action translation that preserves indigenous philosophical depth without flat colonial truncation.
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <label style={{ display: 'block', fontSize: '0.85rem', color: 'var(--gold-light)', marginBottom: '8px', fontWeight: 600 }}>
          Yorùbá Phrase or Odù Ifá Verse:
        </label>
        <input
          type="text"
          value={culturalInput}
          onChange={(e) => setCulturalInput(e.target.value)}
          placeholder="e.g. Èjì Ogbè lori Ọpọ́n Ifá"
          style={{
            width: '100%',
            background: 'rgba(15, 23, 42, 0.85)',
            border: '1px solid var(--border-subtle)',
            borderRadius: '12px',
            padding: '12px 18px',
            color: '#f8fafc',
            fontSize: '1rem',
            outline: 'none'
          }}
        />
      </div>

      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '28px' }}>
        <button
          onClick={onCulturalTranslate}
          disabled={translating || !culturalInput.trim()}
          className="btn-gold"
          style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 24px' }}
        >
          <BookOpen size={16} />
          {translating ? 'Synthesizing Metaphysical Gloss...' : 'Translate & Gloss'}
        </button>
      </div>

      {culturalResult && (
        <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
          <div style={{ background: 'rgba(0, 0, 0, 0.4)', padding: '18px', borderRadius: '12px', border: '1px solid var(--border-subtle)' }}>
            <span className="badge-gold" style={{ marginBottom: '8px' }}>
              1. Orthographic Retention
            </span>
            <p style={{ fontSize: '1.2rem', fontWeight: 700, color: '#f8fafc' }}>
              {culturalResult.orthographic_retention}
            </p>
          </div>

          <div style={{ background: 'rgba(0, 0, 0, 0.4)', padding: '18px', borderRadius: '12px', border: '1px solid var(--border-subtle)' }}>
            <span className="badge-emerald" style={{ marginBottom: '8px' }}>
              2. Direct Contextual Translation
            </span>
            <p style={{ fontSize: '1.05rem', color: 'var(--text-primary)' }}>
              {culturalResult.literal_translation}
            </p>
          </div>

          <div style={{ background: 'rgba(217, 119, 6, 0.1)', padding: '22px', borderRadius: '12px', border: '1px solid rgba(217, 119, 6, 0.4)' }}>
            <span className="badge-gold" style={{ marginBottom: '8px' }}>
              <Feather size={12} /> 3. Deep Metaphysical & Philosophical Gloss
            </span>
            <p style={{ fontSize: '0.96rem', color: 'var(--gold-light)', lineHeight: 1.65 }}>
              {culturalResult.cultural_gloss}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
