import React, { useRef, useState } from 'react';
import { Sparkles, GitBranch, Film, Feather, Globe, Lock, X } from 'lucide-react';
import { PEER_CULTURES } from '../hooks/useExplorationGraph';

const DIACRITICS = ['À', 'Á', 'È', 'É', 'Ẹ̀', 'Ẹ́', 'Ì', 'Í', 'Ò', 'Ó', 'Ọ̀', 'Ọ́', 'Ù', 'Ú', 'Ṣ'];

export default function OponSearchCore({
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
  const [showDiacritics, setShowDiacritics] = useState(false);
  const cultureMeta = PEER_CULTURES[activeCulture] || PEER_CULTURES.yoruba;

  const handleCultureClick = (cult) => {
    if (!cult.productionUnlocked) {
      setLockedCultureNotice(`🔒 ${cult.label} Canon is locked in production (Sequential 14-Tier Ingestion Pending).`);
      setTimeout(() => setLockedCultureNotice(''), 4500);
      return;
    }
    setLockedCultureNotice('');
    onSelectCulture(cult.id);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (submitLockRef.current || loading || !query.trim()) return;
    submitLockRef.current = true;
    onExecuteSearch(query);
    setTimeout(() => { submitLockRef.current = false; }, 250);
  };

  const handleInsertDiacritic = (char) => {
    setQuery((prev) => prev + char);
  };

  return (
    <div style={{ textAlign: 'center', padding: hasSearched ? '10px 0 8px 0' : '28px 0 20px 0', transition: 'all 0.35s ease' }}>
      
      {/* 1. SOVEREIGN PEER CULTURE SWITCHER */}
      <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '5px 10px', borderRadius: '999px', background: 'rgba(12, 17, 28, 0.85)', border: '1px solid rgba(212, 175, 55, 0.3)', marginBottom: '14px', flexWrap: 'wrap', justifyContent: 'center' }}>
        <span style={{ fontSize: '0.72rem', color: 'var(--gold-light)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', display: 'inline-flex', alignItems: 'center', gap: '4px', padding: '0 6px' }}>
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
              title={isLocked ? `${cult.label}: Locked` : `${cult.label}: Active`}
              style={{ padding: '4px 12px', borderRadius: '999px', border: isSelected ? `1px solid ${cult.accent}` : '1px solid transparent', background: isSelected ? 'linear-gradient(135deg, rgba(212, 175, 55, 0.25) 0%, rgba(217, 119, 6, 0.12) 100%)' : 'transparent', color: isSelected ? '#f8fafc' : isLocked ? 'rgba(148, 163, 184, 0.6)' : 'var(--text-secondary)', fontSize: '0.74rem', fontWeight: isSelected ? 700 : 500, cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
            >
              <span>{cult.flag} {cult.label}</span>
              {isLocked && <Lock size={10} color="#94a3b8" />}
            </button>
          );
        })}
      </div>

      {lockedCultureNotice && (
        <div style={{ maxWidth: '640px', margin: '0 auto 12px auto', padding: '6px 14px', borderRadius: '999px', background: 'rgba(217, 119, 6, 0.14)', border: '1px solid rgba(212, 175, 55, 0.35)', color: '#fbbf24', fontSize: '0.76rem', fontWeight: 600 }}>
          {lockedCultureNotice}
        </div>
      )}

      {/* 2. CANONICAL BRAND CREST */}
      <div style={{ marginBottom: hasSearched ? '8px' : '16px' }}>
        <h1 className="font-royal text-gold mobile-heading-compact" style={{ fontSize: hasSearched ? '1.65rem' : '2.6rem', fontWeight: 800, letterSpacing: '0.04em', marginBottom: '3px' }}>
          ÀGBÀ ENGINE
        </h1>
        <p className="mobile-subtitle-compact" style={{ color: 'var(--text-secondary)', fontSize: hasSearched ? '0.82rem' : '0.94rem', maxWidth: '680px', margin: '0 auto' }}>
          {cultureMeta.subtitle}
        </p>
      </div>

      {/* =====================================================================
          3. THE TRIPLE CONCENTRIC OPON IFÁ (ÀÁRÍN ÌMỌ̀ — OPEN AT BASE)
         ===================================================================== */}
      <form onSubmit={handleFormSubmit} style={{ maxWidth: '780px', margin: '0 auto', position: 'relative' }}>
        
        {/* DOM ANCHOR FOR CUBIC-BÉZIER VEIN RABBIT-HOLE GRAPH */}
        <div id="central-tooth-search-anchor" style={{ position: 'relative', width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          
          {/* AMBIENT IYERÒSÙN (GOLDEN WOOD DUST) HEARTH GLOW */}
          <div className="dust-heart" style={{ position: 'absolute', width: '380px', height: '380px', background: 'radial-gradient(circle, rgba(212, 175, 55, 0.22) 0%, rgba(251, 191, 36, 0.08) 55%, transparent 75%)', borderRadius: '50%', pointerEvents: 'none', top: '10px' }} />

          <svg viewBox="0 0 640 430" style={{ width: '100%', maxWidth: '620px', height: 'auto', filter: 'drop-shadow(0 20px 45px rgba(0,0,0,0.9))' }} fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="oponBronzeRim" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fef08a" stop-opacity="0.95" />
                <stop offset="30%" stop-color="#d4af37" stop-opacity="0.9" />
                <stop offset="70%" stop-color="#854d0e" stop-opacity="0.65" />
                <stop offset="100%" stop-color="#eab308" stop-opacity="0.9" />
              </linearGradient>
              <radialGradient id="oponHearthGrad" cx="50%" cy="45%" r="55%">
                <stop offset="0%" stop-color="#241b12" stop-opacity="0.96" />
                <stop offset="60%" stop-color="#120e0a" stop-opacity="0.98" />
                <stop offset="100%" stop-color="#060504" stop-opacity="1" />
              </radialGradient>
            </defs>

            {/* RING 1: OUTER BRONZE RIM (ETÍ ỌPỌ́N — OPEN AT SOUTHERN BASE) */}
            <path d="M 175 355 A 250 250 0 1 1 465 355" stroke="url(#oponBronzeRim)" stroke-width="4.5" stroke-linecap="round" className="glowing-ring" />

            {/* NORTH APEX HERALDIC SENTINEL LOZENGE */}
            <polygon points="320, 40 328, 48 320, 56 312, 48" fill="#fbbf24" stroke="#d4af37" stroke-width="1.5" />
            <circle cx="320" cy="48" r="2" fill="#fff" />
            <circle cx="70" cy="200" r="3.5" fill="#d4af37" />
            <circle cx="570" cy="200" r="3.5" fill="#d4af37" />

            {/* RING 2: MID CELESTIAL DIACRITIC ORBIT (OPEN AT BASE) */}
            <path d="M 195 325 A 195 195 0 1 1 445 325" stroke="#d4af37" stroke-width="2" stroke-opacity="0.45" stroke-dasharray="8, 6" stroke-linecap="round" />

            {/* RING 3: INNER GOLDEN DUST HEARTH (ÀÁRÍN ỌPỌ́N — OPEN AT BASE) */}
            <path d="M 220 295 A 145 145 0 1 1 420 295" fill="url(#oponHearthGrad)" stroke="#fbbf24" stroke-width="2.8" stroke-linecap="round" />

            {/* CASCADING VASCULAR VEINS FLOWING DOWN OUT OF OPEN BASE */}
            <path d="M 235 290 C 235 340, 180 370, 140 425" stroke="#fbbf24" stroke-width="2.6" stroke-linecap="round" className="cascading-vein" />
            <path d="M 405 290 C 405 340, 460 370, 500 425" stroke="#fbbf24" stroke-width="2.6" stroke-linecap="round" className="cascading-vein" />
            <circle cx="140" cy="425" r="4.5" fill="#fef08a" />
            <circle cx="500" cy="425" r="4.5" fill="#fef08a" />
          </svg>

          {/* INSET SEARCH CAPSULE & DIACRITIC STRIP (FLUSH INSIDE HEARTH) */}
          <div className="opon-search-wrapper" style={{ position: 'absolute', top: '102px', width: '90%', maxWidth: '380px', display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 20 }}>
            
            {/* Input Capsule */}
            <div style={{ width: '100%', background: 'rgba(5, 7, 13, 0.95)', border: isFocused ? '2px solid #fbbf24' : '2px solid #d4af37', borderRadius: '16px', padding: '6px 10px', display: 'flex', alignItems: 'center', gap: '8px', boxShadow: isFocused ? '0 0 28px rgba(251, 191, 36, 0.4)' : '0 10px 30px rgba(0, 0, 0, 0.8)', transition: 'all 0.25s ease' }}>
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onFocus={() => setIsFocused(true)}
                onBlur={() => setIsFocused(false)}
                placeholder="Ṣàwárí Ìmọ̀: sovereign parents, Odù..."
                style={{ flex: 1, background: 'transparent', border: 'none', color: '#f8fafc', fontSize: '0.92rem', fontWeight: 600, outline: 'none' }}
              />

              {query && (
                <button type="button" onClick={onClearSearch} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '2px' }}>
                  <X size={15} />
                </button>
              )}

              <button
                type="submit"
                disabled={loading}
                className="btn-gold"
                style={{ padding: '6px 14px', borderRadius: '10px', fontSize: '0.82rem', fontWeight: 800, display: 'inline-flex', alignItems: 'center', gap: '4px', cursor: 'pointer' }}
              >
                {loading ? '...' : 'Ṣàwárí'}
              </button>
            </div>

            {/* Collapsible Tone Marks Toggle */}
            <button
              type="button"
              onClick={() => setShowDiacritics(!showDiacritics)}
              style={{
                marginTop: '8px',
                background: showDiacritics ? 'rgba(212, 175, 55, 0.2)' : 'rgba(10, 14, 24, 0.75)',
                border: '1px solid rgba(212, 175, 55, 0.35)',
                borderRadius: '999px',
                padding: '3px 12px',
                color: 'var(--gold-light)',
                fontSize: '0.70rem',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '5px',
                transition: 'all 0.2s'
              }}
            >
              <span>Àmì Ohùn (15 Yorùbá Tone Beads)</span>
              <span style={{ fontSize: '0.62rem' }}>{showDiacritics ? '▲' : '▼'}</span>
            </button>

            {/* 15 Sacred Yorùbá Diacritic Beads Mounted in Hearth */}
            {showDiacritics && (
              <div style={{ width: '100%', marginTop: '6px', padding: '6px 8px', borderRadius: '12px', background: 'rgba(10, 14, 24, 0.95)', border: '1px solid rgba(212, 175, 55, 0.35)', display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '4px', boxShadow: '0 8px 24px rgba(0, 0, 0, 0.85)' }}>
                {DIACRITICS.map((char) => (
                  <button
                    key={char}
                    type="button"
                    onClick={() => handleInsertDiacritic(char)}
                    style={{ width: '26px', height: '26px', display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '6px', background: 'rgba(18, 24, 38, 0.95)', border: '1px solid rgba(148, 163, 184, 0.25)', color: '#f8fafc', fontSize: '0.78rem', fontWeight: 700, cursor: 'pointer', transition: 'all 0.15s' }}
                    onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#fbbf24'; e.currentTarget.style.color = '#fbbf24'; }}
                    onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'rgba(148, 163, 184, 0.25)'; e.currentTarget.style.color = '#f8fafc'; }}
                  >
                    {char}
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* 4. POST-SEARCH LIVING ROOT PODS (IF ACTIVE) */}
        {hasSearched && rootNetworkNodes?.parent && (
          <div style={{ marginTop: '-20px', position: 'relative', zIndex: 25, width: '100%' }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(170px, 1fr))', gap: '10px' }}>
              <button
                type="button"
                className="root-pod"
                style={{ textAlign: 'left', font: 'inherit', width: '100%', cursor: 'pointer' }}
                onClick={(e) => {
                  e.preventDefault();
                  e.stopPropagation();
                  onSelectRootNode(rootNetworkNodes.parent, 'Sovereign Parent');
                }}
              >
                <span className="root-pod-badge"><Sparkles size={11} /> Sovereign Parent</span>
                <div className="root-pod-title">{rootNetworkNodes.parent.title}</div>
                <div className="root-pod-desc">{rootNetworkNodes.parent.category || 'Canonical Matrix'}</div>
              </button>

              {rootNetworkNodes.variants?.slice(0, 2).map((v) => (
                <button
                  key={v.id || v.title}
                  type="button"
                  className="root-pod"
                  style={{ textAlign: 'left', font: 'inherit', width: '100%', cursor: 'pointer' }}
                  onClick={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    onSelectRootNode(v, 'Living Variant');
                  }}
                >
                  <span className="root-pod-badge"><GitBranch size={11} /> Living Variant</span>
                  <div className="root-pod-title">{v.title}</div>
                  <div className="root-pod-desc">{v.description ? v.description.slice(0, 36) + '...' : 'Child Node'}</div>
                </button>
              ))}

              {rootNetworkNodes.regalia && (
                <button
                  type="button"
                  className="root-pod"
                  style={{ textAlign: 'left', font: 'inherit', width: '100%', cursor: 'pointer' }}
                  onClick={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    onSelectRootNode({ title: rootNetworkNodes.regalia.canonical_name, id: rootNetworkNodes.regalia.canonical_name }, 'Museum Regalia');
                  }}
                >
                  <span className="root-pod-badge"><Film size={11} /> Museum Regalia</span>
                  <div className="root-pod-title">{rootNetworkNodes.regalia.canonical_name}</div>
                  <div className="root-pod-desc">{rootNetworkNodes.regalia.current_custodial_repository || 'Museum Vault'}</div>
                </button>
              )}
            </div>
          </div>
        )}
      </form>

      {/* 5. IDLE DISCOVERY BUTTON & CURATED CULTURAL ANCHORS */}
      {!hasSearched && (
        <div style={{ marginTop: '22px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '10px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <button
              type="button"
              onClick={onCuratedDiscovery}
              className="btn-ghost"
              style={{ padding: '6px 14px', borderRadius: '999px', fontSize: '0.76rem', color: '#fbbf24', borderColor: 'rgba(212, 175, 55, 0.4)', display: 'inline-flex', alignItems: 'center', gap: '5px' }}
            >
              <Sparkles size={12} /> Àwárí Àkànṣe (Discover)
            </button>
            <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)' }}>• 🩸 Curated Cultural Anchors:</span>
          </div>

          <div style={{ display: 'flex', justifyContent: 'center', gap: '8px', flexWrap: 'wrap', maxWidth: '640px' }}>
            {cultureMeta.anchors.map((term) => (
              <span
                key={term}
                onClick={() => { setQuery(term); onExecuteSearch(term); }}
                style={{ fontSize: '0.78rem', color: 'var(--gold-light)', cursor: 'pointer', padding: '2px 8px', borderRadius: '6px', background: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(148, 163, 184, 0.2)', transition: 'all 0.15s' }}
                onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#fbbf24'; e.currentTarget.style.color = '#fbbf24'; }}
                onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'rgba(148, 163, 184, 0.2)'; e.currentTarget.style.color = 'var(--gold-light)'; }}
              >
                {term}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
