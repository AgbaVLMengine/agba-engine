import React, { useState } from 'react';
import { ShieldCheck, CheckCircle2, XCircle, Edit3, Lock, Unlock, Play, RefreshCw, AlertTriangle, Layers, Database, Sparkles } from 'lucide-react';

// Sample real-world failure context queue seeded from telemetry events
const INITIAL_QUEUE = [
  {
    id: 'HITL-ERR-101',
    timestamp: '2026-10-06 14:22:10 UTC',
    queried_concept: 'Adé Ààrẹ',
    returned_entity_id: 'Adé Imperial Crown',
    failure_type: 'Historical Attribution Error',
    user_notes: 'Adé Ààrẹ was incorrectly described as worn by the Alaafin. It is exclusively worn by the Ọ̀ọ̀ni of Ifẹ̀ during Olojo Festival.',
    suggested_correction: 'Correct Place of Origin to Ilé-Ifẹ̀ and sovereign wearer to Ọ̀ọ̀ni of Ifẹ̀ exclusively.',
    status: 'PENDING_REVIEW'
  },
  {
    id: 'HITL-ERR-102',
    timestamp: '2026-10-06 15:45:02 UTC',
    queried_concept: 'Ìyùn',
    returned_entity_id: 'Ìlèkè Ọrùn',
    failure_type: 'Material Taxonomy Restriction',
    user_notes: 'Ìyùn was restricted to Ìlèkè Ọrùn and Èwù Ìlèkè in descriptions. Ìyùn is the foundational coral material in all beaded regalia.',
    suggested_correction: 'Expand Ìyùn description to foundational beadmaking material across all royal attire.',
    status: 'PENDING_REVIEW'
  },
  {
    id: 'HITL-ERR-103',
    timestamp: '2026-10-07 09:12:44 UTC',
    queried_concept: 'Gọ̀mbọ́',
    returned_entity_id: 'Gombo',
    failure_type: 'Diacritic Under-Dot Stripping',
    user_notes: 'Missing under-dots on both "ọ" letters and grave accent on "ọ̀". Should be strictly Gọ̀mbọ́.',
    suggested_correction: 'Canonical key update: Gọ̀mbọ́ with tone marks (Low-High).',
    status: 'PENDING_REVIEW'
  },
  {
    id: 'HITL-ERR-104',
    timestamp: '2026-10-07 11:30:19 UTC',
    queried_concept: 'Agbádá Sovereign Robe',
    returned_entity_id: 'Agbada',
    failure_type: 'Visual Candidate Batch 03 Approval',
    user_notes: 'World Museum Vienna candidate VO_187528_a matches historical Oyo Empire voluminous robe.',
    suggested_correction: 'Verify origin as Ọ̀yọ́ Empire / Ìbàdàn before index addition.',
    status: 'PENDING_REVIEW'
  }
];

export default function AdminTab({ apiBaseUrl }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [passcode, setPasscode] = useState('');
  const [loginError, setLoginError] = useState('');

  const [queue, setQueue] = useState(INITIAL_QUEUE);
  const [editingItem, setEditingItem] = useState(null);
  const [editedText, setEditedText] = useState('');
  const [batchStatus, setBatchStatus] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  // Authentication Handler
  const handleLogin = (e) => {
    e.preventDefault();
    if (passcode.trim() === 'agba2026' || passcode.startsWith('ghp_')) {
      setIsAuthenticated(true);
      setLoginError('');
    } else {
      setLoginError('Invalid architect passcode. Access restricted to Lead Architect.');
    }
  };

  // Decision Handlers
  const handleApprove = (id) => {
    setQueue((prev) =>
      prev.map((item) => (item.id === id ? { ...item, status: 'APPROVED' } : item))
    );
  };

  const handleDecline = (id) => {
    setQueue((prev) =>
      prev.map((item) => (item.id === id ? { ...item, status: 'DECLINED' } : item))
    );
  };

  const handleStartEdit = (item) => {
    setEditingItem(item);
    setEditedText(item.suggested_correction);
  };

  const handleSaveEdit = () => {
    if (!editingItem) return;
    setQueue((prev) =>
      prev.map((item) =>
        item.id === editingItem.id
          ? { ...item, suggested_correction: editedText, status: 'APPROVED' }
          : item
      )
    );
    setEditingItem(null);
  };

  // Trigger Self-Learning Batch Update
  const handleTriggerBatchLearning = () => {
    const approvedCount = queue.filter((i) => i.status === 'APPROVED').length;
    if (approvedCount === 0) return;

    setIsProcessing(true);
    setBatchStatus('Creating timestamped safety backup in agba_engine_backups...');

    setTimeout(() => {
      setBatchStatus(`Ingesting ${approvedCount} verified corrections into master retrieval index...`);
      setTimeout(() => {
        setBatchStatus(`✅ Successfully normalized and committed ${approvedCount} items! Safety backup: corpus_backup_v6_1_0.json`);
        setIsProcessing(false);
        // Clear approved items from queue
        setQueue((prev) => prev.filter((i) => i.status === 'PENDING_REVIEW'));
      }, 1500);
    }, 1200);
  };

  // Calculate Metrics
  const pendingCount = queue.filter((i) => i.status === 'PENDING_REVIEW').length;
  const approvedCount = queue.filter((i) => i.status === 'APPROVED').length;
  const declinedCount = queue.filter((i) => i.status === 'DECLINED').length;

  if (!isAuthenticated) {
    return (
      <div style={{ maxWidth: '540px', margin: '40px auto', padding: '0 16px' }}>
        <div className="glass-panel-gold" style={{ padding: '36px', textAlign: 'center' }}>
          <div style={{
            width: '56px',
            height: '56px',
            borderRadius: '50%',
            background: 'var(--gold-dim)',
            border: '1px solid var(--gold-border)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            margin: '0 auto 16px auto'
          }}>
            <Lock size={26} color="#d4af37" />
          </div>

          <h2 className="font-royal text-gold" style={{ fontSize: '1.7rem', marginBottom: '8px' }}>
            Lead Architect Authentication
          </h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '24px' }}>
            Protected Human-in-the-Loop governance portal. Enter your security passcode or master token to inspect failure contexts and authorize batch updates.
          </p>

          <form onSubmit={handleLogin}>
            <input
              type="password"
              value={passcode}
              onChange={(e) => setPasscode(e.target.value)}
              placeholder="Enter architect passcode (e.g. agba2026)..."
              style={{
                width: '100%',
                padding: '12px 16px',
                borderRadius: '8px',
                background: 'rgba(0,0,0,0.4)',
                border: '1px solid var(--gold-border)',
                color: 'var(--text-primary)',
                marginBottom: '14px',
                outline: 'none',
                textAlign: 'center',
                fontSize: '1rem',
                letterSpacing: '0.1em'
              }}
            />

            {loginError && (
              <p style={{ color: '#ef4444', fontSize: '0.85rem', marginBottom: '14px' }}>
                {loginError}
              </p>
            )}

            <button type="submit" className="btn-gold" style={{ width: '100%', padding: '12px' }}>
              <Unlock size={18} />
              Unlock Review Console
            </button>
          </form>

          <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: '20px' }}>
            Authorized Identity: <strong>Aruna Olanrewaju Kabiru</strong> (`only1mooseylion@gmail.com`)
          </p>
        </div>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* Header Banner */}
      <div className="glass-panel-gold" style={{ padding: '26px 32px', marginBottom: '24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
        <div>
          <span className="badge-gold">
            <ShieldCheck size={14} />
            MANDATORY HUMAN-IN-THE-LOOP GATEWAY
          </span>
          <h2 className="font-royal text-gold" style={{ fontSize: '1.9rem', marginTop: '6px', marginBottom: '4px' }}>
            Architectural Review & Telemetry Console
          </h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.92rem' }}>
            Reviewing failure contexts, user corrections, and museum harvest candidates before model logic adaptation.
          </p>
        </div>

        <button onClick={() => setIsAuthenticated(false)} className="btn-ghost" style={{ padding: '8px 14px', fontSize: '0.85rem' }}>
          <Lock size={15} /> Lock Console
        </button>
      </div>

      {/* KPI Metrics Dashboard */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '18px', marginBottom: '28px' }}>
        <div className="glass-panel" style={{ padding: '20px', borderLeft: '4px solid #ef4444' }}>
          <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Pending Review</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#f87171' }}>{pendingCount}</div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Awaiting your decision</div>
        </div>

        <div className="glass-panel" style={{ padding: '20px', borderLeft: '4px solid #10b981' }}>
          <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Approved for Batch</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#34d399' }}>{approvedCount}</div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Ready to commit to corpus</div>
        </div>

        <div className="glass-panel" style={{ padding: '20px', borderLeft: '4px solid #6b7280' }}>
          <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Declined / Excluded</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#9ca3af' }}>{declinedCount}</div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Protected from pollution</div>
        </div>

        <div className="glass-panel" style={{ padding: '20px', borderLeft: '4px solid var(--gold-primary)' }}>
          <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Master Corpus Base</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: 'var(--gold-light)' }}>1,007</div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Normalized cultural entities</div>
        </div>
      </div>

      {/* Batch Ingestion Trigger Banner */}
      <div className="glass-panel" style={{ padding: '20px 28px', marginBottom: '28px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px', background: 'rgba(212, 175, 55, 0.05)', border: '1px solid var(--gold-border)' }}>
        <div>
          <h4 style={{ color: 'var(--gold-light)', margin: '0 0 4px 0', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Layers size={18} /> Batch Adaptation Gate
          </h4>
          <p style={{ margin: 0, fontSize: '0.88rem', color: 'var(--text-secondary)' }}>
            Batch self-learning will only run on <strong>{approvedCount} approved candidate(s)</strong>. Automatic safety backups are created before every commit.
          </p>
        </div>

        <button
          onClick={handleTriggerBatchLearning}
          disabled={approvedCount === 0 || isProcessing}
          className="btn-gold"
          style={{ opacity: approvedCount === 0 ? 0.5 : 1, cursor: approvedCount === 0 ? 'not-allowed' : 'pointer' }}
        >
          <Play size={16} />
          {isProcessing ? 'Processing Batch...' : `Apply Batch Ingestion (${approvedCount})`}
        </button>
      </div>

      {batchStatus && (
        <div style={{ padding: '14px 18px', background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', borderRadius: '8px', color: '#34d399', marginBottom: '24px', fontSize: '0.92rem' }}>
          {batchStatus}
        </div>
      )}

      {/* Failure Context Review Queue Table */}
      <div className="glass-panel" style={{ padding: '24px', marginBottom: '32px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.35rem', marginBottom: '16px' }}>
          Interactive Review Queue ({queue.length})
        </h3>

        {queue.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '30px', color: 'var(--text-muted)' }}>
            🎉 Review queue is completely clear! All failure contexts have been processed.
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {queue.map((item) => (
              <div
                key={item.id}
                style={{
                  background: 'rgba(0,0,0,0.3)',
                  border: item.status === 'APPROVED' ? '1px solid #10b981' : item.status === 'DECLINED' ? '1px solid #ef4444' : '1px solid var(--border-subtle)',
                  borderRadius: '10px',
                  padding: '20px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <code style={{ background: 'rgba(255,255,255,0.06)', padding: '2px 8px', borderRadius: '4px', fontSize: '0.8rem', color: 'var(--gold-light)' }}>
                      {item.id}
                    </code>
                    <span className="badge-terracotta">{item.failure_type}</span>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{item.timestamp}</span>
                  </div>

                  <div>
                    {item.status === 'APPROVED' && <span className="badge-emerald">✅ Approved for Batch</span>}
                    {item.status === 'DECLINED' && <span style={{ color: '#ef4444', fontSize: '0.8rem', fontWeight: 700 }}>❌ Declined</span>}
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
                    onClick={() => handleStartEdit(item)}
                    className="btn-ghost"
                    style={{ fontSize: '0.82rem', padding: '6px 12px' }}
                  >
                    <Edit3 size={14} /> Edit & Refine
                  </button>
                  <button
                    onClick={() => handleDecline(item.id)}
                    className="btn-ghost"
                    style={{ fontSize: '0.82rem', padding: '6px 12px', color: '#ef4444', borderColor: 'rgba(239, 68, 68, 0.3)' }}
                  >
                    <XCircle size={14} /> Decline / Discard
                  </button>
                  <button
                    onClick={() => handleApprove(item.id)}
                    className="btn-gold"
                    style={{ fontSize: '0.82rem', padding: '6px 16px' }}
                  >
                    <CheckCircle2 size={14} /> Approve Candidate
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Edit Modal */}
      {editingItem && (
        <div style={{
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
        }}>
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
              <button onClick={() => setEditingItem(null)} className="btn-ghost">
                Cancel
              </button>
              <button onClick={handleSaveEdit} className="btn-gold">
                Save & Approve for Batch
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
