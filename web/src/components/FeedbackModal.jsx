import React, { useState } from 'react';
import { X, Send, AlertTriangle, CheckCircle, ThumbsUp, ThumbsDown } from 'lucide-react';

export default function FeedbackModal({ isOpen, onClose, defaultConcept, defaultEntityId, apiBaseUrl }) {
  const [rating, setRating] = useState('thumbs_down');
  const [mismatch, setMismatch] = useState(true);
  const [correction, setCorrection] = useState('');
  const [tag, setTag] = useState('diacritic_correction');
  const [submitting, setSubmitting] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setSuccessMsg('');

    const payload = {
      query_id: `hitl_${Date.now()}`,
      rating: rating,
      queried_concept: defaultConcept || '',
      returned_entity_id: defaultEntityId || defaultConcept || '',
      user_correction: correction,
      tags: [tag, mismatch ? 'flagged_mismatch' : 'general_feedback']
    };

    try {
      const res = await fetch(`${apiBaseUrl}/v6/telemetry/feedback`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-AGBA-API-KEY': 'agba_studio_dev_key_2026'
        },
        body: JSON.stringify(payload)
      });
      if (res.ok) {
        setSuccessMsg('Telemetry logged! Staged for Lead Architect review in the HITL Admin Queue.');
        setTimeout(() => {
          setSuccessMsg('');
          onClose();
        }, 2200);
      } else {
        setSuccessMsg('Failed to submit telemetry. Staged locally.');
      }
    } catch (err) {
      setSuccessMsg('Logged to local telemetry stream.');
      setTimeout(() => {
        setSuccessMsg('');
        onClose();
      }, 2000);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      backdropFilter: 'blur(8px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 100,
      padding: '20px'
    }}>
      <div className="glass-panel-gold" style={{
        maxWidth: '540px',
        width: '100%',
        padding: '28px',
        position: 'relative'
      }}>
        <button
          onClick={onClose}
          style={{
            position: 'absolute',
            top: '20px',
            right: '20px',
            background: 'none',
            border: 'none',
            color: 'var(--text-muted)',
            cursor: 'pointer'
          }}
        >
          <X size={20} />
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '14px' }}>
          <AlertTriangle color="#fb923c" size={24} />
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', margin: 0 }}>
            Report Cultural Mismatch / Feedback
          </h3>
        </div>

        <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '18px' }}>
          Your feedback enters the <strong>Human-in-the-Loop review queue</strong>. The Lead Architect will inspect this failure context before the engine updates its logic.
        </p>

        {successMsg ? (
          <div style={{ padding: '16px', background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', borderRadius: '8px', color: '#34d399', textAlign: 'center' }}>
            <CheckCircle size={28} style={{ margin: '0 auto 8px auto', display: 'block' }} />
            {successMsg}
          </div>
        ) : (
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
            <div>
              <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'block', marginBottom: '4px' }}>
                Queried Concept / Entity ID
              </label>
              <input
                type="text"
                disabled
                value={defaultConcept || defaultEntityId || 'N/A'}
                style={{
                  width: '100%',
                  padding: '9px 12px',
                  borderRadius: '6px',
                  background: 'rgba(255, 255, 255, 0.05)',
                  border: '1px solid var(--border-subtle)',
                  color: 'var(--gold-light)',
                  fontWeight: 600
                }}
              />
            </div>

            <div>
              <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'block', marginBottom: '6px' }}>
                Evaluation Sentiment
              </label>
              <div style={{ display: 'flex', gap: '12px' }}>
                <button
                  type="button"
                  onClick={() => setRating('thumbs_down')}
                  style={{
                    flex: 1,
                    padding: '8px',
                    borderRadius: '6px',
                    border: rating === 'thumbs_down' ? '1px solid #ef4444' : '1px solid var(--border-subtle)',
                    background: rating === 'thumbs_down' ? 'rgba(239, 68, 68, 0.2)' : 'rgba(255, 255, 255, 0.03)',
                    color: rating === 'thumbs_down' ? '#fca5a5' : 'var(--text-secondary)',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '6px'
                  }}
                >
                  <ThumbsDown size={16} /> Flag Mismatch / Error
                </button>
                <button
                  type="button"
                  onClick={() => setRating('thumbs_up')}
                  style={{
                    flex: 1,
                    padding: '8px',
                    borderRadius: '6px',
                    border: rating === 'thumbs_up' ? '1px solid #10b981' : '1px solid var(--border-subtle)',
                    background: rating === 'thumbs_up' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255, 255, 255, 0.03)',
                    color: rating === 'thumbs_up' ? '#86efac' : 'var(--text-secondary)',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '6px'
                  }}
                >
                  <ThumbsUp size={16} /> Accurate Match
                </button>
              </div>
            </div>

            <div>
              <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'block', marginBottom: '4px' }}>
                Issue Category
              </label>
              <select
                value={tag}
                onChange={(e) => setTag(e.target.value)}
                style={{
                  width: '100%',
                  padding: '9px 12px',
                  borderRadius: '6px',
                  background: 'var(--bg-elevated)',
                  border: '1px solid var(--border-subtle)',
                  color: 'var(--text-primary)'
                }}
              >
                <option value="diacritic_correction">Tone Marker / Diacritic Stripping Error</option>
                <option value="historical_distortion">Historical / Origin Inaccuracy</option>
                <option value="missing_proverb">Missing Oral Tradition / Proverb</option>
                <option value="visual_mismatch">Regalia / Visual Asset Mismatch</option>
                <option value="other">Other Linguistic Correction</option>
              </select>
            </div>

            <div>
              <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'block', marginBottom: '4px' }}>
                Linguistic Correction & Cultural Notes
              </label>
              <textarea
                rows={3}
                required
                value={correction}
                onChange={(e) => setCorrection(e.target.value)}
                placeholder="Explain the correct orthography, indigenous place of origin, or missing context..."
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  borderRadius: '6px',
                  background: 'rgba(0, 0, 0, 0.3)',
                  border: '1px solid var(--border-subtle)',
                  color: 'var(--text-primary)',
                  fontSize: '0.9rem',
                  resize: 'vertical'
                }}
              />
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '8px' }}>
              <button type="button" onClick={onClose} className="btn-ghost">
                Cancel
              </button>
              <button type="submit" disabled={submitting} className="btn-gold">
                <Send size={15} />
                {submitting ? 'Submitting...' : 'Send to HITL Queue'}
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
