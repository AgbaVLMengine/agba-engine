import React from 'react';
import { ShieldCheck, Lock, Play, RefreshCw, Layers } from 'lucide-react';
import { useHitlQueue } from '../hooks/useHitlQueue';
import AdminLoginCard from './AdminLoginCard';
import HitlReviewCard from './HitlReviewCard';
import HitlEditModal from './HitlEditModal';

export default function AdminTab() {
  const hitl = useHitlQueue();

  if (!hitl.isAuthenticated) {
    return (
      <AdminLoginCard
        passcode={hitl.passcode}
        setPasscode={hitl.setPasscode}
        loginError={hitl.loginError}
        onLogin={hitl.handleLogin}
      />
    );
  }

  const metricCards = [
    { title: 'Pending Review', value: hitl.pendingCount, desc: 'Awaiting your decision', color: '#fbbf24', border: '#f59e0b' },
    { title: 'Approved for Batch', value: hitl.approvedCount, desc: 'Ready to commit to corpus', color: '#34d399', border: '#10b981' },
    { title: 'Declined / Excluded', value: hitl.declinedCount, desc: 'Protected from pollution', color: '#9ca3af', border: '#6b7280' },
    { title: 'Master Corpus Base', value: hitl.totalMasterEntities.toLocaleString(), desc: `${hitl.totalParents} Parents · ${hitl.totalSubVariants} Sub-Variants`, color: 'var(--gold-light)', border: 'var(--gold-primary)' }
  ];

  return (
    <div className="tab-pane animate-fade-in" style={{ maxWidth: '1100px', margin: '0 auto', paddingBottom: '60px' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '28px', flexWrap: 'wrap', gap: '16px' }}>
        <div>
          <h2 className="font-royal text-gold" style={{ fontSize: '1.8rem', display: 'flex', alignItems: 'center', gap: '10px', margin: '0 0 6px 0' }}>
            <ShieldCheck size={28} color="#d4af37" />
            Lead Architect HITL Console
          </h2>
          <p style={{ color: 'var(--text-secondary)', margin: 0, fontSize: '0.92rem' }}>
            Autonomous Failure Review & Sovereign Index Adaptation Hub
          </p>
        </div>

        <button onClick={hitl.handleLogout} className="btn-ghost" style={{ fontSize: '0.85rem', display: 'flex', alignItems: 'center', gap: '6px' }}>
          <Lock size={14} /> Authenticated as Lead Architect
        </button>
      </div>

      {/* Status & Corpus Sizing Metrics */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px', marginBottom: '28px' }}>
        {metricCards.map((c, i) => (
          <div key={i} className="glass-panel" style={{ padding: '20px', borderLeft: `4px solid ${c.border}` }}>
            <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>{c.title}</div>
            <div style={{ fontSize: '2.2rem', fontWeight: 800, color: c.color }}>{c.value}</div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>{c.desc}</div>
          </div>
        ))}
      </div>

      {/* Batch Ingestion Trigger Banner */}
      <div className="glass-panel" style={{ padding: '20px 28px', marginBottom: '28px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px', background: 'rgba(212, 175, 55, 0.05)', border: '1px solid var(--gold-border)' }}>
        <div>
          <h4 style={{ color: 'var(--gold-light)', margin: '0 0 4px 0', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Layers size={18} /> Batch Adaptation Gate
          </h4>
          <p style={{ margin: 0, fontSize: '0.88rem', color: 'var(--text-secondary)' }}>
            Batch self-learning will only run on <strong>{hitl.approvedCount} approved candidate(s)</strong>. Automatic safety backups are created before every commit.
          </p>
        </div>

        <button
          onClick={hitl.handleTriggerBatchLearning}
          disabled={hitl.approvedCount === 0 || hitl.isProcessing}
          className="btn-gold"
          style={{ opacity: hitl.approvedCount === 0 ? 0.5 : 1, cursor: hitl.approvedCount === 0 ? 'not-allowed' : 'pointer' }}
        >
          <Play size={16} />
          {hitl.isProcessing ? 'Processing Batch...' : `Apply Batch Ingestion (${hitl.approvedCount})`}
        </button>
      </div>

      {hitl.batchStatus && (
        <div className="glass-panel animate-fade-in" style={{ padding: '16px 20px', marginBottom: '28px', borderLeft: '4px solid #10b981', display: 'flex', alignItems: 'center', gap: '12px' }}>
          <RefreshCw size={18} color="#34d399" className={hitl.isProcessing ? 'animate-spin' : ''} />
          <span style={{ fontSize: '0.92rem', color: '#e2e8f0' }}>{hitl.batchStatus}</span>
        </div>
      )}

      {/* Review Queue Items */}
      <div style={{ marginBottom: '40px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.3rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
          Telemetry Failure Review Contexts ({hitl.queue.length})
        </h3>

        {hitl.queue.length === 0 ? (
          <div className="glass-panel" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-secondary)' }}>
            All telemetry review candidates processed. Sovereign corpus index is pristine.
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
            {hitl.queue.map((item) => (
              <HitlReviewCard
                key={item.id}
                item={item}
                onStartEdit={hitl.handleStartEdit}
                onDecline={hitl.handleDecline}
                onApprove={hitl.handleApprove}
              />
            ))}
          </div>
        )}
      </div>

      <HitlEditModal
        editingItem={hitl.editingItem}
        editedText={hitl.editedText}
        setEditedText={hitl.setEditedText}
        onCancel={() => hitl.setEditingItem(null)}
        onSave={hitl.handleSaveEdit}
      />
    </div>
  );
}
