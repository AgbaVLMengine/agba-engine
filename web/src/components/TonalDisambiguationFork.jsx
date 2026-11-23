import React from 'react';
import { Scale, ArrowRight, Sparkles } from 'lucide-react';

export default function TonalDisambiguationFork({
  candidates = [],
  query = '',
  onSelectCandidate
}) {
  if (!candidates || candidates.length < 2) return null;

  return (
    <div
      className="animate-fade-in"
      style={{
        maxWidth: '860px',
        margin: '0 auto 24px auto',
        padding: '16px 20px',
        background: 'linear-gradient(135deg, rgba(20, 16, 10, 0.96) 0%, rgba(15, 23, 42, 0.95) 100%)',
        border: '1px solid rgba(212, 175, 55, 0.45)',
        borderRadius: '16px',
        boxShadow: '0 12px 36px rgba(0, 0, 0, 0.65)'
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px', flexWrap: 'wrap' }}>
        <span style={{ fontSize: '0.8rem', color: '#fbbf24', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.06em', display: 'inline-flex', alignItems: 'center', gap: '5px' }}>
          <Scale size={14} color="#fbbf24" /> Àyànfẹ́ Ohùn (Tonal Disambiguation)
        </span>
        <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)' }}>
          • {candidates.length} distinct canonical concepts match &quot;{query}&quot;. Choose your intended path:
        </span>
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
          gap: '10px'
        }}
      >
        {candidates.map((cand) => (
          <button
            key={cand.id || cand.title}
            type="button"
            onClick={() => onSelectCandidate && onSelectCandidate(cand)}
            style={{
              display: 'flex',
              flexDirection: 'column',
              textAlign: 'left',
              padding: '10px 14px',
              borderRadius: '10px',
              background: 'rgba(0, 0, 0, 0.45)',
              border: '1px solid rgba(212, 175, 55, 0.25)',
              color: '#f8fafc',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
              font: 'inherit'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.borderColor = '#fbbf24';
              e.currentTarget.style.transform = 'translateY(-2px)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.borderColor = 'rgba(212, 175, 55, 0.25)';
              e.currentTarget.style.transform = 'none';
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
              <span className="font-royal text-gold" style={{ fontSize: '1.05rem', fontWeight: 700 }}>
                {cand.title}
              </span>
              <span style={{ fontSize: '0.7rem', color: 'var(--gold-light)', display: 'inline-flex', alignItems: 'center', gap: '2px' }}>
                <ArrowRight size={11} /> Select
              </span>
            </div>
            <span style={{ fontSize: '0.72rem', color: '#34d399', fontWeight: 600, marginBottom: '4px' }}>
              {cand.category || 'Canonical Matrix'}
            </span>
            <p style={{ fontSize: '0.76rem', color: 'var(--text-muted)', margin: 0, lineHeight: 1.35, display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
              {cand.description || 'Authentic Yorùbá canonical entity.'}
            </p>
          </button>
        ))}
      </div>
    </div>
  );
}
