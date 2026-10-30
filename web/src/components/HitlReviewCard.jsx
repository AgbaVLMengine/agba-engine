import React from 'react';
import { Edit3, XCircle, CheckCircle2 } from 'lucide-react';

export default function HitlReviewCard({ item, onStartEdit, onDecline, onApprove }) {
  const borderLeftColor =
    item.status === 'APPROVED'
      ? '4px solid #10b981'
      : item.status === 'DECLINED'
      ? '4px solid #ef4444'
      : '4px solid #f59e0b';

  return (
    <div
      className="glass-panel"
      style={{
        padding: '24px',
        display: 'flex',
        flexDirection: 'column',
        gap: '16px',
        borderLeft: borderLeftColor
      }}
    >
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span style={{ fontWeight: 700, color: 'var(--gold-light)', fontSize: '0.95rem' }}>{item.id}</span>
          <span style={{ fontSize: '0.75rem', background: 'rgba(255,255,255,0.06)', padding: '2px 8px', borderRadius: '4px', color: 'var(--text-secondary)' }}>
            {item.failure_type}
          </span>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{item.timestamp}</span>
        </div>

        <div>
          {item.status === 'APPROVED' && <span style={{ color: '#34d399', fontSize: '0.8rem', fontWeight: 700 }}>✓ Approved for Ingestion</span>}
          {item.status === 'DECLINED' && <span style={{ color: '#f87171', fontSize: '0.8rem', fontWeight: 700 }}>✕ Declined / Excluded</span>}
          {item.status === 'PENDING_REVIEW' && <span style={{ color: '#fb923c', fontSize: '0.8rem', fontWeight: 700 }}>⏳ Pending Decision</span>}
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '14px', fontSize: '0.9rem' }}>
        <div>
          <strong style={{ color: 'var(--text-muted)', display: 'block', fontSize: '0.78rem' }}>QUERIED CONCEPT:</strong>
          <span style={{ color: 'var(--gold-light)', fontWeight: 600, fontSize: '1.05rem' }}>{item.queried_concept}</span>
        </div>
        <div>
          <strong style={{ color: 'var(--text-muted)', display: 'block', fontSize: '0.78rem' }}>RETURNED ENTITY:</strong>
          <span style={{ color: 'var(--text-primary)' }}>{item.returned_entity_id}</span>
        </div>
      </div>

      <div style={{ background: 'rgba(255,255,255,0.02)', padding: '12px', borderRadius: '6px', borderLeft: '3px solid #fb923c', fontSize: '0.88rem' }}>
        <strong style={{ color: '#fb923c' }}>Failure Description / User Correction:</strong>
        <p style={{ margin: '4px 0 0 0', color: 'var(--text-primary)' }}>{item.user_notes}</p>
      </div>

      <div style={{ background: 'rgba(16, 185, 129, 0.05)', padding: '12px', borderRadius: '6px', borderLeft: '3px solid #10b981', fontSize: '0.88rem' }}>
        <strong style={{ color: '#34d399' }}>Proposed Candidate Ingestion:</strong>
        <p style={{ margin: '4px 0 0 0', color: 'var(--text-primary)' }}>{item.suggested_correction}</p>
      </div>

      {/* Action Buttons */}
      <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end', marginTop: '4px' }}>
        <button
          onClick={() => onStartEdit(item)}
          className="btn-ghost"
          style={{ fontSize: '0.82rem', padding: '6px 12px' }}
        >
          <Edit3 size={14} /> Edit & Refine
        </button>
        <button
          onClick={() => onDecline(item.id)}
          className="btn-ghost"
          style={{ fontSize: '0.82rem', padding: '6px 12px', color: '#ef4444', borderColor: 'rgba(239, 68, 68, 0.3)' }}
        >
          <XCircle size={14} /> Decline / Discard
        </button>
        <button
          onClick={() => onApprove(item.id)}
          className="btn-gold"
          style={{ fontSize: '0.82rem', padding: '6px 16px' }}
        >
          <CheckCircle2 size={14} /> Approve Candidate
        </button>
      </div>
    </div>
  );
}
