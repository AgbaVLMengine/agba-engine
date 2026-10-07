import React from 'react';
import { Search, Image, ShieldCheck, Cpu, ExternalLink } from 'lucide-react';

export default function Navbar({ activeTab, setActiveTab, apiStatus }) {
  const tabs = [
    { id: 'search', label: 'Corpus Search & Diacritics', icon: Search },
    { id: 'gallery', label: 'Museum Regalia Gallery', icon: Image },
    { id: 'admin', label: 'HITL Admin Panel', icon: ShieldCheck, badge: 'Protected' },
    { id: 'architecture', label: 'Architecture & Diagnostics', icon: Cpu }
  ];

  return (
    <header className="glass-panel" style={{
      position: 'sticky',
      top: '12px',
      zIndex: 50,
      margin: '12px auto 24px auto',
      maxWidth: '1280px',
      padding: '12px 24px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      border: '1px solid rgba(212, 175, 55, 0.25)',
      boxShadow: '0 8px 32px rgba(0, 0, 0, 0.4)'
    }}>
      {/* Brand Title */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '14px', cursor: 'pointer' }} onClick={() => setActiveTab('search')}>
        <div style={{
          width: '42px',
          height: '42px',
          borderRadius: '10px',
          background: 'linear-gradient(135deg, #d4af37 0%, #8c6710 100%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '22px',
          boxShadow: '0 4px 14px rgba(212, 175, 55, 0.35)'
        }}>
          👑
        </div>
        <div>
          <h1 className="font-royal text-gold" style={{ fontSize: '1.45rem', lineHeight: 1.1, fontWeight: 800 }}>
            ÀGBÀ ENGINE
          </h1>
          <p style={{ fontSize: '0.72rem', color: 'var(--text-muted)', letterSpacing: '0.08em', textTransform: 'uppercase' }}>
            Diacritic Cultural Intelligence Core • v6.1.0
          </p>
        </div>
      </div>

      {/* Navigation Tabs */}
      <nav style={{ display: 'flex', gap: '6px', background: 'rgba(0, 0, 0, 0.25)', padding: '4px', borderRadius: '12px', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '8px 16px',
                borderRadius: '8px',
                border: 'none',
                background: isActive ? 'linear-gradient(135deg, rgba(212, 175, 55, 0.2) 0%, rgba(212, 175, 55, 0.08) 100%)' : 'transparent',
                color: isActive ? 'var(--gold-light)' : 'var(--text-secondary)',
                fontWeight: isActive ? 700 : 500,
                fontSize: '0.88rem',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                borderBottom: isActive ? '2px solid var(--gold-primary)' : '2px solid transparent'
              }}
            >
              <Icon size={16} color={isActive ? '#d4af37' : '#94a3b8'} />
              <span>{tab.label}</span>
              {tab.badge && (
                <span style={{
                  fontSize: '0.65rem',
                  padding: '2px 6px',
                  borderRadius: '10px',
                  background: 'rgba(200, 90, 50, 0.25)',
                  color: '#fb923c',
                  border: '1px solid rgba(200, 90, 50, 0.4)',
                  fontWeight: 700
                }}>
                  {tab.badge}
                </span>
              )}
            </button>
          );
        })}
      </nav>

      {/* Live Cloud Run Status Pill */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        <a
          href="https://agba-enterprise-api-dgefvzanqq-uc.a.run.app/health"
          target="_blank"
          rel="noopener noreferrer"
          style={{ textDecoration: 'none' }}
          title="Verify live Cloud Run endpoint"
        >
          <div className="badge-emerald" style={{ display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', padding: '5px 12px' }}>
            <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: '#10b981', display: 'inline-block', boxShadow: '0 0 8px #10b981' }}></span>
            <span>Cloud Run Live</span>
            <ExternalLink size={12} />
          </div>
        </a>
      </div>
    </header>
  );
}
