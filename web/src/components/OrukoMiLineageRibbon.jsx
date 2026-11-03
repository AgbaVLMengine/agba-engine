import React from 'react';
import { Sparkles, Compass } from 'lucide-react';

/**
 * ÀGBÀ ENGINE: ORÚKỌ MI GOLDEN LINEAGE RIBBON
 * Renders the etymological deconstruction of Yorùbá personal names
 * above the Prime Sovereign Bento Cell.
 * Mobile Invariants: flex-wrap morpheme pills, WCAG AAA contrast, zero text clipping.
 */
export default function OrukoMiLineageRibbon({ card }) {
  if (!card) return null;

  return (
    <div
      className="oruko-mi-lineage-ribbon"
      style={{
        background: 'linear-gradient(135deg, rgba(212, 175, 55, 0.14) 0%, rgba(15, 23, 42, 0.96) 100%)',
        border: '1px solid rgba(212, 175, 55, 0.45)',
        borderRadius: '12px',
        padding: '16px 20px',
        marginBottom: '20px',
        boxShadow: '0 8px 24px -4px rgba(0, 0, 0, 0.45)'
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', marginBottom: '10px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#fef08a', fontSize: '0.96rem', fontWeight: 800 }}>
          <Sparkles size={16} color="#d4af37" />
          <span>Orúkọ Mi: &ldquo;{card.canonical_name}&rdquo;</span>
          <span style={{ fontSize: '0.78rem', color: '#94a3b8', fontWeight: 500 }}>({card.grammatical_class})</span>
        </div>
        {card.lineage_covenant && (
          <span style={{ fontSize: '0.72rem', padding: '3px 10px', borderRadius: '999px', background: 'rgba(16, 185, 129, 0.18)', border: '1px solid rgba(16, 185, 129, 0.45)', color: '#34d399', fontWeight: 700 }}>
            {card.lineage_covenant}
          </span>
        )}
      </div>

      {card.morphemes && card.morphemes.length > 0 && (
        <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '6px', margin: '10px 0' }}>
          {card.morphemes.map((m, idx) => (
            <React.Fragment key={idx}>
              <div style={{ background: 'rgba(0, 0, 0, 0.5)', border: '1px solid rgba(212, 175, 55, 0.25)', borderRadius: '8px', padding: '5px 10px', fontSize: '0.84rem' }}>
                <strong style={{ color: '#fef08a' }}>{m.morpheme}</strong>
                <span style={{ color: '#cbd5e1', marginLeft: '6px', fontSize: '0.8rem' }}>({m.meaning})</span>
              </div>
              {idx < card.morphemes.length - 1 && <span style={{ color: '#d4af37', fontWeight: 800 }}>+</span>}
            </React.Fragment>
          ))}
        </div>
      )}

      <div style={{ fontSize: '0.88rem', color: '#f8fafc', lineHeight: 1.55, marginTop: '8px' }}>
        <strong style={{ color: '#d4af37' }}>Lineage Meaning:</strong> {card.lineage_meaning}
      </div>

      {card.sovereign_parents && card.sovereign_parents.length > 0 && (
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginTop: '10px', fontSize: '0.78rem', color: '#94a3b8' }}>
          <Compass size={13} color="#d4af37" />
          <span>Root Sovereign Hearth:</span>
          <strong style={{ color: '#fef08a' }}>{card.sovereign_parents.join(' • ')}</strong>
        </div>
      )}
    </div>
  );
}
