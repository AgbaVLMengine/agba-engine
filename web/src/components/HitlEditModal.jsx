import React from 'react';

export default function HitlEditModal({ editingItem, editedText, setEditedText, onCancel, onSave }) {
  if (!editingItem) return null;

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0,0,0,0.85)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 100,
        padding: '20px'
      }}
    >
      <div className="glass-panel-gold" style={{ maxWidth: '580px', width: '100%', padding: '28px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px' }}>
          Refine Candidate Metadata: {editingItem.queried_concept}
        </h3>
        <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '16px' }}>
          Ensure strict 25-letter Yorùbá diacritics and historical accuracy before approving.
        </p>

        <textarea
          rows={4}
          value={editedText}
          onChange={(e) => setEditedText(e.target.value)}
          style={{
            width: '100%',
            padding: '12px',
            borderRadius: '8px',
            background: 'rgba(0,0,0,0.4)',
            border: '1px solid var(--gold-border)',
            color: 'var(--text-primary)',
            marginBottom: '18px',
            fontSize: '0.92rem'
          }}
        />

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
          <button onClick={onCancel} className="btn-ghost">
            Cancel
          </button>
          <button onClick={onSave} className="btn-gold">
            Save & Approve for Batch
          </button>
        </div>
      </div>
    </div>
  );
}
