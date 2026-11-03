import React, { useRef, useState } from 'react';
import { Search, Sparkles, GitBranch, Film, Feather, Shuffle, Globe, Lock } from 'lucide-react';
import { PEER_CULTURES } from '../hooks/useExplorationGraph';

export default function ToothSearchCore({
  query,
  setQuery,
  loading,
  hasSearched,
  isFocused,
  setIsFocused,
  activeCulture,
  onSelectCulture,
  onExecuteSearch,
  onCuratedDiscovery,
  onClearSearch,
  rootNetworkNodes,
  onSelectRootNode
}) {
  const submitLockRef = useRef(false);
  const [lockedCultureNotice, setLockedCultureNotice] = useState('');
  const cultureMeta = PEER_CULTURES[activeCulture] || PEER_CULTURES.yoruba;

  const handleCultureClick = (cult) => {
    if (!cult.productionUnlocked) {
      setLockedCultureNotice(
        `🔒 ${cult.label} Canon is locked in production until sequential 14-Tier Corpus ingestion & Lead Architect HITL audit complete.`
      );
      setTimeout(() => setLockedCultureNotice(''), 4500);
      return;
    }
    setLockedCultureNotice('');
    onSelectCulture(cult.id);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (submitLockRef.current || loading) return;
    submitLockRef.current = true;
    onExecuteSearch(query);
    setTimeout(() => {
      submitLockRef.current = false;
    }, 250);
  };

  const handleInsertDiacritic = (char) => {
    setQuery((prev) => prev + char);
  };

  return (
    <div
      style={{
        textAlign: 'center',
        padding: hasSearched ? '14px 0 8px 0' : '38px 0 24px 0',
        transition: 'all 0.35s ease'
      }}
    >
      {/* =====================================================================
          EQUAL MULTI-CULTURE SOVEREIGN SWITCHER BAR
         ===================================================================== */}
      <div
        style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: '6px',
          padding: '5px 8px',
          borderRadius: '999px',
          background: 'rgba(12, 17, 28, 0.85)',
          border: '1px solid rgba(212, 175, 55, 0.3)',
          marginBottom: '16px',
          flexWrap: 'wrap',
          justifyContent: 'center'
        }}
      >
        <span
          style={{
            fontSize: '0.72rem',
            color: 'var(--gold-light)',
            fontWeight: 700,
            textTransform: 'uppercase',
            letterSpacing: '0.06em',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '0 8px'
          }}
        >
          <Globe size={13} color={cultureMeta.accent} /> Peer Sovereign Canon:
        </span>
        {Object.values(PEER_CULTURES).map((cult) => {
          const isSelected = cult.id === activeCulture;
          const isLocked = !cult.productionUnlocked;
          return (
            <button
              key={cult.id}
              type="button"
              onClick={() => handleCultureClick(cult)}
              title={
                isLocked
                  ? `${cult.label}: Locked in production (Sequential 14-Tier Ingestion Pending)`
                  : `${cult.label}: Active Sovereign Canon`
              }
              style={{
                padding: '5px 13px',
                borderRadius: '999px',
                border: isSelected ? `1px solid ${cult.accent}` : '1px solid transparent',
                background: isSelected
                  ? 'linear-gradient(135deg, rgba(212, 175, 55, 0.25) 0%, rgba(217, 119, 6, 0.12) 100%)'
                  : 'transparent',
                color: isSelected ? '#f8fafc' : isLocked ? 'rgba(148, 163, 184, 0.65)' : 'var(--text-secondary)',
                fontSize: '0.78rem',
                fontWeight: isSelected ? 700 : 500,
                cursor: isLocked ? 'not-allowed' : 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '5px',
                transition: 'all 0.2s ease'
              }}
            >
              {isLocked && <Lock size={11} color="#fbbf24" />}
              {cult.label}
            </button>
          );
        })}
      </div>

      {lockedCultureNotice && (
        <div
          style={{
            maxWidth: '640px',
            margin: '0 auto 12px auto',
            padding: '6px 14px',
            borderRadius: '999px',
            background: 'rgba(217, 119, 6, 0.14)',
            border: '1px solid rgba(212, 175, 55, 0.35)',
            color: '#fbbf24',
            fontSize: '0.76rem',
            fontWeight: 600
          }}
        >
          {lockedCultureNotice}
        </div>
      )}

      {/* Brand Crest & Sovereign Title */}
      <div style={{ marginBottom: hasSearched ? '10px' : '18px' }}>
        <h1
          className="font-royal text-gold"
          style={{
            fontSize: hasSearched ? '1.65rem' : '2.6rem',
            fontWeight: 800,
            letterSpacing: '0.04em',
            marginBottom: '4px'
          }}
        >
          ÀGBÀ ENGINE
        </h1>
        <p
          style={{
            color: 'var(--text-secondary)',
            fontSize: hasSearched ? '0.84rem' : '0.98rem',
            maxWidth: '680px',
            margin: '0 auto'
          }}
        >
          {cultureMeta.subtitle}
        </p>
      </div>

      {/* =====================================================================
          THE SCULPTED CENTRAL TOOTH EMBLEM (SEARCH EMBEDDED INSIDE CROWN)
         ===================================================================== */}
      <form
        onSubmit={handleFormSubmit}
        style={{ maxWidth: '820px', margin: '0 auto', position: 'relative' }}
      >
        <div
          id="central-tooth-search-anchor"
          className="wisdom-tooth-container"
          style={{
            padding: '22px 26px 26px 26px',
            borderRadius: '54px 54px 36px 36px',
            border: `2px solid ${cultureMeta.accent}`,
            background:
              'radial-gradient(circle at 50% 0%, rgba(217, 119, 6, 0.16) 0%, rgba(15, 23, 42, 0.96) 55%, rgba(9, 13, 22, 0.99) 100%)',
            boxShadow:
              '0 18px 54px rgba(0, 0, 0, 0.75), 0 0 34px rgba(217, 119, 6, 0.25), inset 0 2px 6px rgba(243, 229, 171, 0.25)',
            position: 'relative'
          }}
        >
          {/* Decorative Upper Molar Cusps & Enamel Ridge */}
          <div className="tooth-crown-ridge" style={{ marginBottom: '12px' }} />

          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              fontSize: '0.72rem',
              fontWeight: 700,
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
              color: '#fbbf24',
              marginBottom: '10px'
            }}
          >
            <span>🦷 CENTRAL WISDOM TOOTH CORE</span>
            <span>•</span>
            <span>{cultureMeta.traditionLabel}</span>
          </div>

          {/* Search Input + Embedded Submit Button Inside the Tooth Chamber */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              background: 'rgba(6, 9, 14, 0.85)',
              border: '1.5px solid rgba(212, 175, 55, 0.45)',
              borderRadius: '999px',
              padding: '6px 8px 6px 20px',
              boxShadow: 'inset 0 2px 10px rgba(0, 0, 0, 0.6)'
            }}
          >
            <Search size={20} color="#d97706" style={{ flexShrink: 0 }} />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onFocus={() => setIsFocused(true)}
              placeholder="Search inside the Tooth: sovereign parents, regalia, Odù Ifá, cuisine, drums..."
              style={{
                flex: 1,
                background: 'transparent',
                border: 'none',
                outline: 'none',
                color: '#f8fafc',
                fontSize: '1.05rem',
                padding: '8px 0',
                fontWeight: 500,
                minWidth: '140px'
              }}
            />
            {query && (
              <button
                type="button"
                onClick={onClearSearch}
                title="Reset Tooth & Vein Search"
                style={{
                  background: 'transparent',
                  border: 'none',
                  color: 'var(--text-muted)',
                  cursor: 'pointer',
                  fontSize: '16px',
                  padding: '4px 8px'
                }}
              >
                ✕
              </button>
            )}
            <button
              type="submit"
              disabled={loading}
              className="btn-gold"
              style={{
                padding: '10px 22px',
                borderRadius: '999px',
                fontSize: '0.92rem',
                fontWeight: 700,
                flexShrink: 0
              }}
            >
              <Search size={15} />
              {loading ? 'Tracing Vein...' : 'Ṣàwárí (Search)'}
            </button>
          </div>

          {/* Culture-Specific Diacritic Keyboard Embedded Inside the Tooth */}
          <div
            style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              gap: '5px',
              flexWrap: 'wrap',
              marginTop: '12px'
            }}
          >
            <span
              style={{
                fontSize: '0.72rem',
                color: 'var(--gold-light)',
                textTransform: 'uppercase',
                letterSpacing: '0.05em',
                fontWeight: 700
              }}
            >
              {cultureMeta.diacriticLabel}:
            </span>
            {cultureMeta.diacritics.map((char) => (
              <button
                key={char}
                type="button"
                onClick={() => handleInsertDiacritic(char)}
                className="diacritic-pill"
              >
                {char}
              </button>
            ))}
            <button
              type="button"
              onClick={onCuratedDiscovery}
              className="btn-ghost-gold"
              style={{
                padding: '4px 12px',
                borderRadius: '999px',
                fontSize: '0.76rem',
                marginLeft: '6px',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '5px'
              }}
            >
              <Shuffle size={12} />
              Àwárí Àkànṣe (Discover)
            </button>
          </div>

          {/* Tooth Root Apex Connector Point (Origin of the Vascular Vein Thread) */}
          <div
            style={{
              position: 'absolute',
              bottom: '-14px',
              left: '50%',
              transform: 'translateX(-50%)',
              width: '26px',
              height: '26px',
              borderRadius: '50%',
              background: 'radial-gradient(circle, #fbbf24 0%, #d97706 70%, #78350f 100%)',
              border: '2px solid #f3e5ab',
              boxShadow: '0 0 18px rgba(217, 119, 6, 0.85)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '11px',
              zIndex: 5
            }}
            title="Central Tooth Vascular Root Apex"
          >
            🩸
          </div>
        </div>

        {/* ===================================================================
            IMMEDIATE VASCULAR ROOT PODS (LIVE AUTO-SUGGEST WHILE TYPING)
           =================================================================== */}
        {rootNetworkNodes && isFocused && (
          <div className="root-network-container animate-fade-in" style={{ marginTop: '14px' }}>
            <svg width="100%" height="42" viewBox="0 0 760 42" style={{ overflow: 'visible' }}>
              <defs>
                <linearGradient id="rootAmberGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#fbbf24" />
                  <stop offset="100%" stopColor="#d97706" />
                </linearGradient>
              </defs>
              <path d="M380 0 L380 16" className="root-vessel-line" />
              <path d="M380 16 C280 18, 180 24, 120 40" className="root-vessel-line" />
              <path d="M380 16 C340 20, 310 26, 290 40" className="root-vessel-line" />
              <path d="M380 16 C420 20, 450 26, 470 40" className="root-vessel-line" />
              <path d="M380 16 C480 18, 580 24, 640 40" className="root-vessel-line" />
            </svg>

            <div
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(170px, 1fr))',
                gap: '12px',
                marginTop: '4px'
              }}
            >
              <div
                className="root-pod"
                onClick={() =>
                  onSelectRootNode(
                    rootNetworkNodes.parent,
                    rootNetworkNodes.parent.is_parent === false ? 'Living Variant' : 'Sovereign Parent'
                  )
                }
              >
                <span className="root-pod-badge">
                  {rootNetworkNodes.parent.is_parent === false ||
                  rootNetworkNodes.parent.sovereign_parent_status === 'Living Sub-Variant' ? (
                    <>
                      <GitBranch size={11} /> Living Sub-Variant
                    </>
                  ) : (
                    <>
                      <Sparkles size={11} /> Sovereign Parent
                    </>
                  )}
                </span>
                <div className="root-pod-title">{rootNetworkNodes.parent.title}</div>
                <div className="root-pod-desc">
                  {rootNetworkNodes.parent.category || 'Canonical Matrix'}
                </div>
              </div>

              {rootNetworkNodes.variants.slice(0, 2).map((v) => (
                <div
                  key={v.id || v.title}
                  className="root-pod"
                  onClick={() => onSelectRootNode(v, 'Living Variant')}
                >
                  <span className="root-pod-badge">
                    <GitBranch size={11} /> Living Variant
                  </span>
                  <div className="root-pod-title">{v.title}</div>
                  <div className="root-pod-desc">
                    {v.description ? v.description.slice(0, 36) + '...' : 'Canonical Sub-Variant'}
                  </div>
                </div>
              ))}

              {rootNetworkNodes.regalia ? (
                <div
                  className="root-pod"
                  onClick={() =>
                    onSelectRootNode(
                      { title: rootNetworkNodes.regalia.canonical_name, id: rootNetworkNodes.regalia.canonical_name },
                      'Museum Regalia'
                    )
                  }
                >
                  <span className="root-pod-badge">
                    <Film size={11} /> Museum Regalia
                  </span>
                  <div className="root-pod-title">{rootNetworkNodes.regalia.canonical_name}</div>
                  <div className="root-pod-desc">
                    {rootNetworkNodes.regalia.current_custodial_repository || 'Museum Vault'}
                  </div>
                </div>
              ) : (
                <div
                  className="root-pod"
                  onClick={() => onSelectRootNode(rootNetworkNodes.parent, 'Oral Liturgy')}
                >
                  <span className="root-pod-badge">
                    <Feather size={11} /> Sacred Verse
                  </span>
                  <div className="root-pod-title">Oral Liturgy</div>
                  <div className="root-pod-desc">Proverbs & Oríkì</div>
                </div>
              )}
            </div>
          </div>
        )}
      </form>

      {/* Curated Cultural Anchors when idle */}
      {!hasSearched && (
        <div style={{ marginTop: '24px', display: 'flex', justifyContent: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <span style={{ fontSize: '0.82rem', color: 'var(--text-muted)' }}>Curated Cultural Anchors:</span>
          {cultureMeta.anchors.map((term) => (
            <span
              key={term}
              onClick={() => {
                setQuery(term);
                onExecuteSearch(term);
              }}
              style={{
                fontSize: '0.82rem',
                color: 'var(--gold-light)',
                cursor: 'pointer',
                textDecoration: 'underline',
                textUnderlineOffset: '3px'
              }}
            >
              {term}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}
