import React from 'react';
import { Sparkles, Compass } from 'lucide-react';

export default function LivingVariantConstellationGrid({ subVariants, onSelectVariant }) {
  if (!subVariants || !Array.isArray(subVariants) || subVariants.length === 0) {
    return null;
  }

  return (
    <div
      style={{
        marginTop: '20px',
        padding: '16px 18px',
        background: 'linear-gradient(135deg, rgba(20, 24, 35, 0.75) 0%, rgba(13, 17, 26, 0.9) 100%)',
        border: '1px solid rgba(212, 175, 55, 0.25)',
        borderRadius: '14px',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.4)'
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Compass size={16} color="#fbbf24" />
          <span style={{ fontSize: '0.86rem', fontWeight: 700, color: '#fbbf24', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
            Living Sub-Variants Constellation
          </span>
        </div>
        <span
          style={{
            fontSize: '0.72rem',
            background: 'rgba(212, 175, 55, 0.12)',
            color: '#d4af37',
            border: '1px solid rgba(212, 175, 55, 0.3)',
            padding: '2px 8px',
            borderRadius: '12px',
            fontWeight: 600
          }}
        >
          {subVariants.length} Active Nodes
        </span>
      </div>

      <p style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: '14px', lineHeight: 1.45 }}>
        Tap any living variant below to branch directly into its dedicated 14-Tier cultural profile via the dynamic hydrator.
      </p>

      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
        {subVariants.map((variant, idx) => {
          const variantTitle = typeof variant === 'string' ? variant : variant.title || variant.name;
          if (!variantTitle) return null;

          return (
            <button
              key={idx}
              type="button"
              onClick={() => onSelectVariant && onSelectVariant(variantTitle)}
              style={{
                background: 'radial-gradient(circle at 50% 0%, rgba(212, 175, 55, 0.15) 0%, rgba(15, 23, 42, 0.6) 100%)',
                border: '1px solid rgba(212, 175, 55, 0.35)',
                borderRadius: '10px',
                padding: '7px 14px',
                color: '#f8fafc',
                fontSize: '0.84rem',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '6px',
                transition: 'all 0.2s cubic-bezier(0.16, 1, 0.3, 1)',
                boxShadow: '0 2px 8px rgba(0, 0, 0, 0.25)'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.borderColor = '#fbbf24';
                e.currentTarget.style.boxShadow = '0 0 14px rgba(251, 191, 36, 0.35)';
                e.currentTarget.style.transform = 'translateY(-1px)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.borderColor = 'rgba(212, 175, 55, 0.35)';
                e.currentTarget.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.25)';
                e.currentTarget.style.transform = 'translateY(0)';
              }}
            >
              <Sparkles size={12} color="#fbbf24" />
              <span>{variantTitle}</span>
              <span style={{ fontSize: '0.72rem', color: '#fbbf24', opacity: 0.85 }}>→</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
