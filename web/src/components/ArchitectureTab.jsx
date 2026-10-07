import React from 'react';
import { Cpu, ShieldCheck, CheckCircle2, Database, Globe, Lock, ExternalLink, Code2 } from 'lucide-react';

export default function ArchitectureTab() {
  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* Overview Banner */}
      <div className="glass-panel-gold" style={{ padding: '32px', marginBottom: '28px', textAlign: 'center' }}>
        <span className="badge-gold" style={{ marginBottom: '8px' }}>ARCHITECTURE & ETHICAL GOVERNANCE</span>
        <h2 className="font-royal text-gold" style={{ fontSize: '2.1rem', marginBottom: '8px', fontWeight: 800 }}>
          Àgbà Engine Operational Matrix
        </h2>
        <p style={{ color: 'var(--text-secondary)', maxWidth: '780px', margin: '0 auto', fontSize: '0.98rem' }}>
          Engineered by <strong>Aruna Olanrewaju Kabiru</strong>. Cross-modal retrieval framework designed to index indigenous knowledge, tonal orthographies, and cultural regalia without sub-token drift or Unicode degradation.
        </p>
      </div>

      {/* Grid of Core Pillars */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: '22px', marginBottom: '32px' }}>
        {/* Pillar 1: Orthography */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid var(--gold-primary)' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Code2 size={20} /> 25-Letter Yorùbá Primacy
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Standard AI LLMs strip under-dots (`ẹ`, `ọ`, `ṣ`) and tonal accents (`á`, `à`), corrupting tonal semantic meaning. Àgbà Engine enforces dual-retrieval parity: exact tonal match (`1.0000`) and ASCII folding fallback (`0.9600`).
          </p>
          <div style={{ background: 'rgba(0,0,0,0.3)', padding: '10px 14px', borderRadius: '6px', fontSize: '0.85rem' }}>
            <code style={{ color: 'var(--gold-light)' }}>Agbádá • Adé Ààrẹ • Ìyùn • Èwù Ìlèkè • Gọ̀mbọ́ • Ọpọ́n Ifá</code>
          </div>
        </div>

        {/* Pillar 2: Architectural Tier Separation */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid #3b82f6' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Lock size={20} /> Tiered Access Separation
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Under sovereign cultural governance, the <strong>Open Source Web Client</strong> is strictly limited to Text & Vision. All <strong>143 Authentic Audio Tokens</strong> (human spoken vocalizations & talking drum glissando) are withheld from client web bundles and reserved exclusively for authorized Enterprise/Institutional API access.
          </p>
          <div style={{ display: 'flex', gap: '8px' }}>
            <span className="badge-emerald">Web: Text & Vision Only</span>
            <span className="badge-gold">API: Tri-Modal Gated</span>
          </div>
        </div>

        {/* Pillar 3: Zero-Cost Cloud Run Infrastructure */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid #10b981' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Globe size={20} /> Zero-Cost Cloud Run & Netlify
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Deployed on Google Cloud Run serverless containers (`min-instances=0`), incurring <strong>$0.00/month</strong> when idle under Google Cloud's Always Free Tier. Frontend served via Netlify Edge CDN with automatic `dev` and `production` branch CI/CD.
          </p>
          <a
            href="https://agba-enterprise-api-dgefvzanqq-uc.a.run.app/health"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-ghost"
            style={{ fontSize: '0.82rem', padding: '6px 12px', textDecoration: 'none' }}
          >
            Inspect Cloud Run Health Probe <ExternalLink size={14} />
          </a>
        </div>
      </div>

      {/* Invariants & Ethical Standards */}
      <div className="glass-panel" style={{ padding: '28px', marginBottom: '36px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.4rem', marginBottom: '16px' }}>
          🏛️ Supreme Corpus Invariants & MLOps Governance
        </h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px', fontSize: '0.92rem' }}>
          <div style={{ display: 'flex', gap: '10px' }}>
            <CheckCircle2 color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>Supreme Corpus Primacy:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                All visual and acoustic assets are strictly subordinated to Yorùbá canonical ground truth. Museum descriptions yield to native historical records.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <CheckCircle2 color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>Mandatory Human-in-the-Loop Gate:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                Zero unverified images or logic updates enter the master corpus autonomously. All candidate additions require Lead Architect signoff.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <CheckCircle2 color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>RAIL Cultural Heritage License:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                Protects indigenous intellectual property and sacred regalia against uncredited commercial exploitation or synthetic distillation.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
