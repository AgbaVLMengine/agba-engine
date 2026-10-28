import React, { useState } from 'react';
import { Search, Image, ShieldCheck, Cpu, MessageSquare, Languages, ExternalLink, Menu, X } from 'lucide-react';

export default function Navbar({ activeTab, setActiveTab }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const tabs = [
    { id: 'search', label: 'Sovereign Search', icon: Search },
    { id: 'chat', label: 'Ọgbọ́n (Intelligence)', icon: MessageSquare, badge: 'Synthesis Core' },
    { id: 'translate', label: 'Diacritize & Translate', icon: Languages },
    { id: 'gallery', label: 'Museum Regalia', icon: Image },
    { id: 'admin', label: 'HITL Review', icon: ShieldCheck, badge: 'Protected' },
    { id: 'architecture', label: 'Architecture', icon: Cpu }
  ];

  const handleSelectTab = (tabId) => {
    setActiveTab(tabId);
    setMobileMenuOpen(false);
  };

  return (
    <header className="glass-panel" style={{
      position: 'sticky',
      top: '12px',
      zIndex: 50,
      margin: '8px auto 16px auto',
      maxWidth: '1280px',
      width: 'calc(100% - 24px)',
      padding: '8px 16px',
      display: 'flex',
      flexDirection: 'column',
      border: '1px solid rgba(212, 175, 55, 0.25)',
      boxShadow: '0 8px 32px rgba(0, 0, 0, 0.4)',
      borderRadius: '16px'
    }}>
      {/* Top Single-Line Header Row */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        width: '100%',
        gap: '8px'
      }}>
        {/* Brand Crest */}
        <div
          style={{ display: 'flex', alignItems: 'center', gap: '10px', cursor: 'pointer', flexShrink: 0 }}
          onClick={() => handleSelectTab('search')}
        >
          <div style={{
            width: '34px',
            height: '34px',
            borderRadius: '9px',
            background: 'linear-gradient(135deg, #d4af37 0%, #8c6710 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '18px',
            boxShadow: '0 4px 14px rgba(212, 175, 55, 0.35)'
          }}>
            👑
          </div>
          <div>
            <h1 className="font-royal text-gold" style={{ fontSize: '1.2rem', lineHeight: 1.1, fontWeight: 800 }}>
              ÀGBÀ ENGINE
            </h1>
            <p style={{ fontSize: '0.62rem', color: 'var(--text-muted)', letterSpacing: '0.06em', textTransform: 'uppercase' }}>
              Sovereign Cultural Intelligence • v6.2.0
            </p>
          </div>
        </div>

        {/* Desktop Navigation Bar */}
        <nav className="desktop-nav" style={{ display: 'flex', gap: '4px', background: 'rgba(0, 0, 0, 0.25)', padding: '4px', borderRadius: '12px', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
          {tabs.map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => handleSelectTab(tab.id)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  padding: '6px 12px',
                  borderRadius: '8px',
                  border: 'none',
                  background: isActive ? 'linear-gradient(135deg, rgba(212, 175, 55, 0.2) 0%, rgba(212, 175, 55, 0.08) 100%)' : 'transparent',
                  color: isActive ? 'var(--gold-light)' : 'var(--text-secondary)',
                  fontWeight: isActive ? 700 : 500,
                  fontSize: '0.82rem',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease',
                  borderBottom: isActive ? '2px solid var(--gold-primary)' : '2px solid transparent'
                }}
              >
                <Icon size={14} color={isActive ? '#d4af37' : '#94a3b8'} />
                <span>{tab.label}</span>
                {tab.badge && (
                  <span style={{
                    fontSize: '0.6rem',
                    padding: '2px 5px',
                    borderRadius: '8px',
                    background: 'rgba(212, 175, 55, 0.25)',
                    color: 'var(--gold-light)',
                    border: '1px solid rgba(212, 175, 55, 0.4)',
                    fontWeight: 700
                  }}>
                    {tab.badge}
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        {/* Right Section: Cloud Run Status & Mobile Hamburger */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
          <a
            href="https://agba-enterprise-api-dgefvzanqq-uc.a.run.app/health"
            target="_blank"
            rel="noopener noreferrer"
            style={{ textDecoration: 'none' }}
            title="Verify live Cloud Run endpoint"
            className="cloud-run-badge"
          >
            <div className="badge-emerald" style={{ display: 'flex', alignItems: 'center', gap: '5px', cursor: 'pointer', padding: '4px 8px', fontSize: '0.72rem' }}>
              <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#10b981', display: 'inline-block', boxShadow: '0 0 8px #10b981' }}></span>
              <span className="cloud-run-text">Cloud Run</span>
              <ExternalLink size={10} />
            </div>
          </a>

          {/* Mobile Hamburger Toggle Button */}
          <button
            type="button"
            className="mobile-nav-toggle"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle navigation menu"
            style={{
              background: 'rgba(212, 175, 55, 0.12)',
              border: '1px solid rgba(212, 175, 55, 0.35)',
              borderRadius: '8px',
              padding: '6px 8px',
              color: 'var(--gold-light)',
              cursor: 'pointer',
              display: 'none',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            {mobileMenuOpen ? <X size={18} /> : <Menu size={18} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Dropdown (Visible only on small viewports when opened) */}
      {mobileMenuOpen && (
        <div className="mobile-nav-drawer" style={{
          marginTop: '12px',
          paddingTop: '10px',
          borderTop: '1px solid rgba(212, 175, 55, 0.2)',
          display: 'flex',
          flexDirection: 'column',
          gap: '6px'
        }}>
          {tabs.map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => handleSelectTab(tab.id)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '9px 12px',
                  borderRadius: '8px',
                  border: 'none',
                  background: isActive ? 'linear-gradient(135deg, rgba(212, 175, 55, 0.2) 0%, rgba(212, 175, 55, 0.08) 100%)' : 'rgba(0, 0, 0, 0.3)',
                  color: isActive ? 'var(--gold-light)' : 'var(--text-secondary)',
                  fontWeight: isActive ? 700 : 500,
                  fontSize: '0.86rem',
                  cursor: 'pointer',
                  borderLeft: isActive ? '3px solid var(--gold-primary)' : '3px solid transparent'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <Icon size={16} color={isActive ? '#d4af37' : '#94a3b8'} />
                  <span>{tab.label}</span>
                </div>
                {tab.badge && (
                  <span style={{
                    fontSize: '0.62rem',
                    padding: '2px 6px',
                    borderRadius: '8px',
                    background: 'rgba(212, 175, 55, 0.25)',
                    color: 'var(--gold-light)',
                    border: '1px solid rgba(212, 175, 55, 0.4)',
                    fontWeight: 700
                  }}>
                    {tab.badge}
                  </span>
                )}
              </button>
            );
          })}
        </div>
      )}
    </header>
  );
}
