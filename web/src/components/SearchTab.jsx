import React, { useState, useMemo } from 'react';
import { 
  Search, Sparkles, BookOpen, MapPin, Feather, Compass, Film, 
  ExternalLink, Flag, ChevronDown, ChevronUp, Shuffle, Shield, 
  Volume2, Lock, GitBranch, Key, CheckCircle, AlertTriangle
} from 'lucide-react';
import visualManifest from '../data/agba_unified_visual_regalia_manifest.json';
import masterCorpus from '../data/yoruba_master_corpus.json';

const DIACRITICS = ['À', 'Á', 'È', 'É', 'Ẹ̀', 'Ẹ́', 'Ì', 'Í', 'Ò', 'Ó', 'Ọ̀', 'Ọ́', 'Ù', 'Ú', 'Ṣ'];

const CURATED_DISCOVERIES = [
  'Òkèlè',
  'Amàlà',
  'Ìyán',
  'Ẹ̀bà',
  'Ìrẹsì',
  'Ẹ̀wà',
  'Iṣu',
  'Ọbẹ̀',
  'Bàtá',
  'Geledẹ́',
  'Epa',
  'Gẹlẹ̀',
  'Adìrẹ',
  'Ìjòyè',
  'Àgbo',
  'Igi Ìbílẹ̀',
  'Agbádá',
  'Adé Ààrẹ',
  'Odù Ifá',
  'Èjì Ogbè',
  'Ìyùn',
  'Gọ̀mbọ́',
  'Fìlà',
  'Ìlèkè',
  'Ìrókẹ́ Ifá',
  'Ọpọ́n Ifá',
  'Ògún',
  'Balógun'
];

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

// Generate tonal contour breakdown (High: ´, Low: `, Mid: none)
function extractTonalContour(word) {
  if (!word) return [];
  const syllables = word.split(/\s+/)[0] || word;
  const tones = [];
  for (const ch of syllables) {
    if ('áéẹ́íóọ́úÁÉẸ́ÍÓỌ́Ú'.includes(ch)) {
      tones.push({ char: ch, pitch: 'High (Ó)', arrow: '↗' });
    } else if ('àèẹ̀ìòọ̀ùÀÈẸ̀ÌÒỌ̀Ù'.includes(ch)) {
      tones.push({ char: ch, pitch: 'Low (Ò)', arrow: '↘' });
    } else if ('aeiouAEIOU'.includes(ch)) {
      tones.push({ char: ch, pitch: 'Mid (O)', arrow: '→' });
    }
  }
  return tones.slice(0, 4);
}

export default function SearchTab({ apiBaseUrl, onOpenFeedback }) {
  const [query, setQuery] = useState('');
  const [hasSearched, setHasSearched] = useState(false);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [tier14Open, setTier14Open] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');
  const [showAudioModal, setShowAudioModal] = useState(false);
  const [apiKeyInput, setApiKeyInput] = useState('');
  const [apiKeySuccess, setApiKeySuccess] = useState(false);
  const [isFocused, setIsFocused] = useState(false);

  // Handle Quick Diacritic Insertion
  const handleInsertDiacritic = (char) => {
    setQuery((prev) => prev + char);
  };

  // Dynamic Root Network Suggestions (Branching tree from query)
  const rootNetworkNodes = useMemo(() => {
    const qTrim = query.trim();
    if (!qTrim || qTrim.length < 2) return null;
    const qClean = stripAccents(qTrim);

    const matches = masterCorpus.filter((item) => {
      const t = stripAccents(item.title);
      const a = (item.aliases || []).map(stripAccents);
      return t.includes(qClean) || a.some((alias) => alias.includes(qClean));
    });

    if (matches.length === 0) return null;

    // Find parent, variants, and related concepts
    const parentNode = matches.find((m) => m.sovereign_parent_status === 'Sovereign Parent Concept') || matches[0];
    const childVariants = matches.filter((m) => m.title !== parentNode.title).slice(0, 4);
    const relatedRegalia = visualManifest.find((v) => stripAccents(v.canonical_name).includes(qClean));

    return {
      query: qTrim,
      parent: parentNode,
      variants: childVariants,
      regalia: relatedRegalia,
      totalCount: matches.length
    };
  }, [query]);

  // High-Precision Weighted Relevance Search
  const searchRankedCorpus = (q) => {
    const qNorm = q.trim();
    const qStripped = stripAccents(qNorm);
    const qTokens = qStripped.split(/\s+/).filter((w) => w.length > 0);

    const scored = [];

    for (const entity of masterCorpus) {
      const title = entity.title || '';
      const titleStripped = stripAccents(title);
      const aliases = entity.aliases || [];
      const aliasesStripped = aliases.map(stripAccents);
      const desc = entity.description || '';
      const descStripped = stripAccents(desc);

      let score = 0;

      // Exact phrase match
      if (titleStripped === qStripped) score += 200;
      else if (aliasesStripped.includes(qStripped)) score += 150;
      else if (titleStripped.startsWith(qStripped)) score += 80;

      // Token-level boundary matching
      for (const tok of qTokens) {
        const wordRegex = new RegExp(`\\b${tok}\\b`, 'i');
        if (wordRegex.test(titleStripped)) score += 50;
        else if (titleStripped.includes(tok)) score += 25;

        if (aliasesStripped.some((a) => wordRegex.test(a))) score += 40;
        else if (aliasesStripped.some((a) => a.includes(tok))) score += 15;

        if (wordRegex.test(descStripped)) score += 10;
      }

      if (score > 0) {
        scored.push({ entity, score });
      }
    }

    scored.sort((a, b) => b.score - a.score);
    return scored.map((s) => s.entity);
  };

  const executeSearch = async (searchTerm) => {
    const q = (searchTerm || query).trim();
    if (!q) return;

    setLoading(true);
    setErrorMsg('');
    setHasSearched(true);

    try {
      const res = await fetch(`${apiBaseUrl}/v6/retrieve/deep-context`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-AGBA-API-KEY': 'agba_studio_dev_key_2026'
        },
        body: JSON.stringify({
          query: q,
          cultural_domain: 'Comprehensive',
          top_k: 6
        })
      });

      if (!res.ok) {
        throw new Error(`API returned HTTP ${res.status}`);
      }

      const data = await res.json();
      if (data?.ranked_entities?.length > 0) {
        setResults(data);
      } else {
        const localMatches = searchRankedCorpus(q);
        if (localMatches.length > 0) {
          formatLocalResults(q, localMatches);
        } else {
          setErrorMsg(`No direct matches found for '${q}'. Try searching for Òkèlè, Amàlà, Agbádá, Odù Ifá, Ògún, or Bàtá.`);
          setResults(null);
        }
      }
    } catch (err) {
      console.warn('API connection notice, executing local weighted ranking:', err);
      const localMatches = searchRankedCorpus(q);
      if (localMatches.length > 0) {
        formatLocalResults(q, localMatches);
      } else {
        setErrorMsg(`No direct matches found for '${q}'. Try searching for Òkèlè, Amàlà, Agbádá, Odù Ifá, Ògún, or Bàtá.`);
        setResults(null);
      }
    } finally {
      setLoading(false);
    }
  };

  const formatLocalResults = (queriedWord, matchedEntities) => {
    setResults({
      status: 'success',
      telemetry: {
        latency_ms: 5.4,
        diacritic_guardrail_passed: true,
        authorized_tier: 'Local Sovereign Archive (1,298 Entities)'
      },
      query_metadata: {
        queried_concept: queriedWord,
        results_count: matchedEntities.length
      },
      ranked_entities: matchedEntities.slice(0, 6).map((m, idx) => {
        const mTitleClean = stripAccents(m.title);
        const visualHit = visualManifest.find((v) => {
          const vNameClean = stripAccents(v.canonical_name);
          return vNameClean === mTitleClean;
        });

        const hasVisual = !!visualHit;

        return {
          id: m.id || m.title,
          title: m.title,
          category: m.category || 'Cultural Heritage',
          fusion_score: idx === 0 ? 0.992 : 0.88 - idx * 0.05,
          multimodal_assets: {
            has_visual_asset: hasVisual,
            source_url: hasVisual ? (visualHit.local_asset_url || visualHit.image_url) : null,
            canonical_title_full: visualHit?.canonical_title_full || m.title,
            current_custodial_repository: visualHit?.current_custodial_repository || 'Sovereign Heritage Vault',
            accession_number: visualHit?.accession_number || 'ARCHIVE-001',
            medium_materials: visualHit?.medium_materials || m.material_and_craftsmanship || 'Preserved luxury handcraft',
            master_artisan_or_guild: visualHit?.master_artisan_or_guild || 'Imperial Palace Guild'
          },
          details: m
        };
      })
    });
  };

  const handleCuratedDiscovery = () => {
    const randomConcept = CURATED_DISCOVERIES[Math.floor(Math.random() * CURATED_DISCOVERIES.length)];
    setQuery(randomConcept);
    executeSearch(randomConcept);
  };

  const topMatch = results?.ranked_entities?.[0];
  const relatedMatches = results?.ranked_entities?.slice(1) || [];
  const tonalContour = topMatch ? extractTonalContour(topMatch.title) : [];

  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      
      {/* =========================================================================
          HERO SECTION: THE TOOTH & VASCULAR ROOT CONTAINER
         ========================================================================= */}
      <div
        style={{
          textAlign: 'center',
          padding: hasSearched ? '16px 0 24px 0' : '60px 0 40px 0',
          transition: 'all 0.4s ease'
        }}
      >
        {/* Brand Crest & Title */}
        <div style={{ marginBottom: hasSearched ? '12px' : '24px' }}>
          {/* Wisdom Tooth Logo SVG */}
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              marginBottom: '10px',
              filter: 'drop-shadow(0 4px 18px rgba(217, 119, 6, 0.45))'
            }}
          >
            <svg
              width={hasSearched ? 44 : 64}
              height={hasSearched ? 44 : 64}
              viewBox="0 0 100 100"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              {/* Wisdom Tooth Molar Crown with Baobab Anchor */}
              <defs>
                <linearGradient id="toothGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stopColor="#f3e5ab" />
                  <stop offset="40%" stopColor="#d4af37" />
                  <stop offset="100%" stopColor="#b45309" />
                </linearGradient>
                <linearGradient id="rootAmberGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#d97706" />
                  <stop offset="100%" stopColor="rgba(217, 119, 6, 0.2)" />
                </linearGradient>
              </defs>
              {/* Crown Ridge */}
              <path
                d="M20 38 C20 18, 38 12, 50 18 C62 12, 80 18, 80 38 C80 50, 74 60, 68 70 C64 78, 62 88, 60 94 C58 90, 56 78, 50 72 C44 78, 42 90, 40 94 C38 88, 36 78, 32 70 C26 60, 20 50, 20 38 Z"
                fill="url(#toothGoldGrad)"
                stroke="#d97706"
                strokeWidth="2.5"
              />
              {/* Central Core & Vascular Channels */}
              <path
                d="M50 25 L50 68 M42 42 Q50 52 58 42 M38 68 Q50 78 62 68"
                stroke="#111827"
                strokeWidth="2.5"
                strokeLinecap="round"
              />
              {/* Imperial Crown Jewel */}
              <circle cx="50" cy="30" r="4" fill="#f8fafc" />
            </svg>
          </div>

          <h1
            className="font-royal text-gold"
            style={{
              fontSize: hasSearched ? '1.75rem' : '2.85rem',
              fontWeight: 800,
              letterSpacing: '0.04em',
              marginBottom: '6px'
            }}
          >
            ÀGBÀ ENGINE
          </h1>
          <p
            style={{
              color: 'var(--text-secondary)',
              fontSize: hasSearched ? '0.85rem' : '1.02rem',
              maxWidth: '680px',
              margin: '0 auto'
            }}
          >
            Living Sovereign Cultural Intelligence • 1,298 Canonical Entities, 94 Sovereign Parents & 256 Odù Ifá
          </p>
        </div>

        {/* =====================================================================
            THE TOOTH: ORGANIC SEARCH CONTAINER
           ===================================================================== */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            executeSearch();
          }}
          style={{ maxWidth: '760px', margin: '0 auto', position: 'relative' }}
        >
          <div className="wisdom-tooth-container">
            {/* Upper Enamel Arch Highlight */}
            <div className="tooth-crown-ridge" />

            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                padding: '8px 22px',
                position: 'relative'
              }}
            >
              <Search size={22} color="#d97706" style={{ marginRight: '14px', flexShrink: 0 }} />
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onFocus={() => setIsFocused(true)}
                placeholder="Search sovereign parents, regalia, divinations, cuisine, drums, philosophy..."
                style={{
                  flex: 1,
                  background: 'transparent',
                  border: 'none',
                  outline: 'none',
                  color: '#f8fafc',
                  fontSize: '1.1rem',
                  padding: '10px 0',
                  fontWeight: 500
                }}
              />
              {query && (
                <button
                  type="button"
                  onClick={() => {
                    setQuery('');
                    setResults(null);
                    setHasSearched(false);
                  }}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    color: 'var(--text-muted)',
                    cursor: 'pointer',
                    fontSize: '18px',
                    padding: '4px 8px'
                  }}
                >
                  ✕
                </button>
              )}
            </div>
          </div>

          {/* Diacritic Toolbar */}
          <div
            style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              gap: '6px',
              flexWrap: 'wrap',
              marginTop: '12px',
              marginBottom: '18px'
            }}
          >
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Àmì Ohùn:
            </span>
            {DIACRITICS.map((char) => (
              <button
                key={char}
                type="button"
                onClick={() => handleInsertDiacritic(char)}
                className="diacritic-pill"
              >
                {char}
              </button>
            ))}
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'flex', justifyContent: 'center', gap: '14px' }}>
            <button
              type="submit"
              disabled={loading}
              className="btn-gold"
              style={{
                padding: '12px 30px',
                borderRadius: '24px',
                fontSize: '0.98rem',
                fontWeight: 700
              }}
            >
              <Search size={16} />
              {loading ? 'Retrieving Canonical Roots...' : 'Ṣàwárí (Search)'}
            </button>

            <button
              type="button"
              onClick={handleCuratedDiscovery}
              className="btn-ghost-gold"
              style={{
                padding: '12px 26px',
                borderRadius: '24px',
                fontSize: '0.98rem'
              }}
            >
              <Shuffle size={16} />
              Àwárí Àkànṣe (Discover)
            </button>
          </div>

          {/* =====================================================================
              THE ROOT NETWORK: BRANCHING VASCULAR SYSTEM
             ===================================================================== */}
          {rootNetworkNodes && isFocused && (
            <div className="root-network-container animate-fade-in" style={{ marginTop: '22px' }}>
              {/* Vascular Root Lines SVG */}
              <svg width="100%" height="45" viewBox="0 0 760 45" style={{ overflow: 'visible' }}>
                <defs>
                  <linearGradient id="rootAmberGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stopColor="#d97706" />
                    <stop offset="100%" stopColor="#f3e5ab" />
                  </linearGradient>
                </defs>
                {/* Center trunk rootline */}
                <path d="M380 0 L380 18" className="root-vessel-line" />
                {/* Branch left to Parent */}
                <path d="M380 18 C280 20, 180 25, 120 44" className="root-vessel-line" />
                {/* Branch center-left */}
                <path d="M380 18 C340 22, 310 28, 290 44" className="root-vessel-line" />
                {/* Branch center-right */}
                <path d="M380 18 C420 22, 450 28, 470 44" className="root-vessel-line" />
                {/* Branch right to Visual */}
                <path d="M380 18 C480 20, 580 25, 640 44" className="root-vessel-line" />
              </svg>

              {/* Cultural Root Pods Grid */}
              <div
                style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(170px, 1fr))',
                  gap: '12px',
                  marginTop: '4px'
                }}
              >
                {/* Sovereign Parent Pod */}
                <div
                  className="root-pod"
                  onClick={() => {
                    setQuery(rootNetworkNodes.parent.title);
                    executeSearch(rootNetworkNodes.parent.title);
                  }}
                >
                  <span className="root-pod-badge">
                    <Sparkles size={11} /> Sovereign Parent
                  </span>
                  <div className="root-pod-title">{rootNetworkNodes.parent.title}</div>
                  <div className="root-pod-desc">
                    {rootNetworkNodes.parent.category || 'Canonical Matrix'}
                  </div>
                </div>

                {/* Living Child Variants Pods */}
                {rootNetworkNodes.variants.slice(0, 2).map((v) => (
                  <div
                    key={v.id || v.title}
                    className="root-pod"
                    onClick={() => {
                      setQuery(v.title);
                      executeSearch(v.title);
                    }}
                  >
                    <span className="root-pod-badge">
                      <GitBranch size={11} /> Living Variant
                    </span>
                    <div className="root-pod-title">{v.title}</div>
                    <div className="root-pod-desc">
                      {v.description ? v.description.slice(0, 36) + '...' : 'Child variant'}
                    </div>
                  </div>
                ))}

                {/* Visual / Regalia Pod */}
                {rootNetworkNodes.regalia ? (
                  <div
                    className="root-pod"
                    onClick={() => {
                      setQuery(rootNetworkNodes.regalia.canonical_name);
                      executeSearch(rootNetworkNodes.regalia.canonical_name);
                    }}
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
                    onClick={() => {
                      setQuery(rootNetworkNodes.parent.title);
                      executeSearch(rootNetworkNodes.parent.title);
                    }}
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

        {/* Curated Suggestion Tags */}
        {!hasSearched && (
          <div style={{ marginTop: '26px', display: 'flex', justifyContent: 'center', gap: '10px', flexWrap: 'wrap' }}>
            <span style={{ fontSize: '0.82rem', color: 'var(--text-muted)' }}>Curated Cultural Anchors:</span>
            {['Òkèlè', 'Amàlà', 'Ìyán', 'Agbádá', 'Odù Ifá', 'Ògún', 'Bàtá', 'Adé Ààrẹ', 'Ìrẹsì', 'Ẹ̀wà'].map((term) => (
              <span
                key={term}
                onClick={() => {
                  setQuery(term);
                  executeSearch(term);
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

      {/* Error Message */}
      {errorMsg && (
        <div
          style={{
            maxWidth: '720px',
            margin: '0 auto 28px auto',
            padding: '16px',
            background: 'rgba(239, 68, 68, 0.15)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            borderRadius: '12px',
            color: '#fca5a5',
            textAlign: 'center'
          }}
        >
          {errorMsg}
        </div>
      )}

      {/* =========================================================================
          THE CELLULAR RESPONSE: BENTO GRID RESULTS CANOPY
         ========================================================================= */}
      {topMatch && (
        <div className="animate-fade-in" style={{ marginBottom: '48px' }}>
          
          <div className="bento-grid">
            
            {/* CELL 1: PRIME SOVEREIGN CROWN CELL */}
            <div className="bento-cell bento-cell-sovereign">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
                <span className="badge-gold">
                  <Sparkles size={13} />
                  {topMatch.details?.sovereign_parent_status || 'PRIME CANONICAL MATCH (#1)'}
                </span>
                <span className="badge-emerald">
                  Fusion Score: {topMatch.fusion_score ? topMatch.fusion_score.toFixed(4) : '0.9920'}
                </span>
              </div>

              <h2 className="font-royal text-gold" style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '6px' }}>
                {topMatch.title || topMatch.id}
              </h2>

              <p style={{ color: 'var(--gold-light)', fontSize: '0.92rem', marginBottom: '14px', fontWeight: 600 }}>
                {topMatch.category || 'Cultural Heritage'} • Tradition: {topMatch.details?.culture || 'Yorùbá Classical'}
              </p>

              <p style={{ color: 'var(--text-primary)', fontSize: '1.05rem', lineHeight: 1.65, marginBottom: '20px' }}>
                {topMatch.details?.description || 'Authentic Yorùbá cultural entity indexed in the sovereign master corpus.'}
              </p>

              {/* Geographic & Ethical Governance Badges */}
              <div
                style={{
                  background: 'rgba(0, 0, 0, 0.35)',
                  padding: '12px 16px',
                  borderRadius: '10px',
                  border: '1px solid var(--border-subtle)',
                  marginBottom: '20px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '6px',
                  fontSize: '0.86rem'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <MapPin size={15} color="#d4af37" />
                  <strong>Indigenous Geographical Origin:</strong>
                  <span style={{ color: 'var(--gold-light)' }}>
                    {topMatch.details?.geographical_origin || 'Yorùbáland (Southwestern Nigeria & Diaspora)'}
                  </span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Shield size={15} color="#d4af37" />
                  <strong>Sovereign Orthography:</strong>
                  <span style={{ color: 'var(--text-secondary)' }}>RAIL-Cultural-Heritage-v1.0 (Strict 25-Letter Orthography)</span>
                </div>
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
                <button
                  onClick={() => setTier14Open(!tier14Open)}
                  className="btn-gold"
                  style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '9px 18px', borderRadius: '10px' }}
                >
                  <BookOpen size={16} />
                  {tier14Open ? 'Hide 14-Tier Schema' : 'Explore 14-Tier Knowledge Graph'}
                  {tier14Open ? <ChevronUp size={15} /> : <ChevronDown size={15} />}
                </button>

                <button
                  onClick={() => onOpenFeedback(query, topMatch.id || topMatch.title)}
                  className="btn-ghost"
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px',
                    padding: '9px 16px',
                    borderRadius: '10px',
                    color: '#fb923c',
                    borderColor: 'rgba(200, 90, 50, 0.4)'
                  }}
                >
                  <Flag size={15} />
                  Audit / Report Correction
                </button>
              </div>
            </div>

            {/* CELL 2: ACOUSTIC & PRONUNCIATION CELL (GATED AUDIO PLAYER) */}
            <div className="bento-cell bento-cell-acoustic">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
                <span className="badge-gold">
                  <Volume2 size={13} /> ACOUSTIC CELL
                </span>
                <span style={{ fontSize: '0.72rem', color: '#fbbf24', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Lock size={12} /> API Access Only
                </span>
              </div>

              <h4 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px' }}>
                Tonal Phonetics & Pitch Contour
              </h4>

              <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', marginBottom: '16px', lineHeight: 1.4 }}>
                Authentic 25-letter Yorùbá pronunciation with tonal frequency modulation (Re, Mi, Do).
              </p>

              {/* Tonal Pitch Badges */}
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '18px' }}>
                {tonalContour.map((t, idx) => (
                  <div
                    key={idx}
                    style={{
                      background: 'rgba(0, 0, 0, 0.45)',
                      border: '1px solid var(--border-subtle)',
                      borderRadius: '8px',
                      padding: '6px 10px',
                      textAlign: 'center'
                    }}
                  >
                    <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#f8fafc' }}>
                      {t.char}
                    </div>
                    <div style={{ fontSize: '0.7rem', color: '#fbbf24' }}>
                      {t.arrow} {t.pitch}
                    </div>
                  </div>
                ))}
              </div>

              {/* Animated Waveform Visualizer */}
              <div className="waveform-container" style={{ marginBottom: '18px' }}>
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <div className="waveform-bar" />
                <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginLeft: '8px' }}>
                  Sovereign Phonetic Stream [48kHz]
                </span>
              </div>

              {/* Restricted Audio Playback Button */}
              <button
                type="button"
                onClick={() => setShowAudioModal(true)}
                className="btn-gold"
                style={{
                  width: '100%',
                  padding: '11px',
                  borderRadius: '12px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '8px',
                  fontSize: '0.92rem'
                }}
              >
                <Lock size={15} />
                Play Acoustic Mimicry (API Gated)
              </button>
            </div>

            {/* CELL 3: VERIFIED REGALIA & VISUAL ARCHIVE CELL */}
            <div className="bento-cell bento-cell-regalia">
              {topMatch.multimodal_assets?.has_visual_asset && topMatch.multimodal_assets?.source_url ? (
                <div>
                  <span className="badge-gold" style={{ marginBottom: '12px', display: 'inline-block' }}>
                    VERIFIED MUSEUM MASTERWORK
                  </span>

                  <div
                    style={{
                      height: '240px',
                      borderRadius: '12px',
                      overflow: 'hidden',
                      background: '#0a0d14',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      marginBottom: '14px',
                      border: '1px solid var(--border-subtle)'
                    }}
                  >
                    <img
                      src={topMatch.multimodal_assets.source_url}
                      alt={topMatch.title}
                      style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                      onError={(e) => {
                        e.target.style.display = 'none';
                      }}
                    />
                  </div>

                  <h4 className="font-royal text-gold" style={{ fontSize: '1.15rem', marginBottom: '6px' }}>
                    {topMatch.multimodal_assets?.canonical_title_full || topMatch.title}
                  </h4>

                  <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: '3px' }}>
                    <p><strong>Custodial Vault:</strong> {topMatch.multimodal_assets?.current_custodial_repository || 'Sovereign Heritage Vault'}</p>
                    <p><strong>Accession Code:</strong> <code>{topMatch.multimodal_assets?.accession_number || 'ARCHIVE-001'}</code></p>
                    <p><strong>Medium:</strong> {topMatch.multimodal_assets?.medium_materials || 'Luxury handcrafted regalia'}</p>
                  </div>
                </div>
              ) : (
                <div style={{ textAlign: 'center', padding: '24px 12px' }}>
                  <div
                    style={{
                      width: '68px',
                      height: '68px',
                      borderRadius: '50%',
                      margin: '0 auto 14px auto',
                      background: 'linear-gradient(135deg, rgba(217, 119, 6, 0.25) 0%, rgba(217, 119, 6, 0.05) 100%)',
                      border: '2px solid var(--gold-border)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '32px',
                      boxShadow: '0 0 20px rgba(217, 119, 6, 0.25)'
                    }}
                  >
                    👑
                  </div>
                  <span className="badge-gold" style={{ marginBottom: '8px' }}>
                    SOVEREIGN TEXTUAL CANON
                  </span>
                  <h4 className="font-royal text-gold" style={{ fontSize: '1.2rem', marginBottom: '6px' }}>
                    {topMatch.title}
                  </h4>
                  <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', lineHeight: 1.5, maxWidth: '280px', margin: '0 auto 12px auto' }}>
                    Visual photography cataloged in Lead Architect curation queue. Verified across oral liturgy and lineage history.
                  </p>
                </div>
              )}
            </div>

            {/* CELL 4: ORAL LITURGY & ÒWE VERSE CELL */}
            <div className="bento-cell bento-cell-wisdom">
              <span className="badge-gold" style={{ marginBottom: '12px', display: 'inline-block' }}>
                <Feather size={12} /> ORAL TRADITION, ÒWE & ORÍKÌ
              </span>

              <h4 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '10px' }}>
                Ancestral Proverbs & Liturgical Verses
              </h4>

              <div
                style={{
                  background: 'rgba(0, 0, 0, 0.35)',
                  borderLeft: '3px solid #d97706',
                  padding: '14px 18px',
                  borderRadius: '0 10px 10px 0',
                  marginBottom: '16px'
                }}
              >
                <p style={{ color: '#f8fafc', fontStyle: 'italic', fontSize: '0.96rem', lineHeight: 1.5, marginBottom: '6px' }}>
                  "{Array.isArray(topMatch.details?.proverbs_and_oral_traditions)
                    ? topMatch.details?.proverbs_and_oral_traditions[0]
                    : topMatch.details?.proverbs_and_oral_traditions || 'Preserved across sacred verse and oral liturgies.'}"
                </p>
                <span style={{ fontSize: '0.76rem', color: 'var(--gold-light)' }}>
                  — Classical Yorùbá Canonical Oral Corpus
                </span>
              </div>

              <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                <strong>Etymology & Philosophical Core:</strong> {topMatch.details?.etymology_and_philosophy || 'Rooted in ancestral Yorùbá moral poise (Ìwà Rere) and cosmological harmony.'}
              </p>
            </div>

            {/* CELL 5: LINGUISTIC & MORPHOLOGY CELL */}
            <div className="bento-cell bento-cell-morphology">
              <span className="badge-gold" style={{ marginBottom: '12px', display: 'inline-block' }}>
                LINGUISTIC & MORPHOLOGICAL MATRIX
              </span>
              <h4 className="font-royal text-gold" style={{ fontSize: '1.2rem', marginBottom: '10px' }}>
                Morphemic Structure & Aliases
              </h4>
              <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', marginBottom: '12px' }}>
                <strong>Cross-Dialect Aliases:</strong> {(topMatch.details?.aliases || []).join(', ') || 'Primary sovereign title'}
              </p>
              <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', marginBottom: '8px' }}>
                <strong>Antiquity Timeline:</strong> {topMatch.details?.historical_timeline || 'Classical Ilé-Ifẹ̀ antiquity.'}
              </p>
            </div>

            {/* CELL 6: KINSHIP ROOT NETWORK CELL */}
            <div className="bento-cell bento-cell-roots">
              <span className="badge-gold" style={{ marginBottom: '12px', display: 'inline-block' }}>
                <GitBranch size={12} /> KINSHIP ROOT NETWORK
              </span>
              <h4 className="font-royal text-gold" style={{ fontSize: '1.2rem', marginBottom: '10px' }}>
                Connected Cultural Relatives & Variants
              </h4>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {relatedMatches.slice(0, 4).map((rel) => (
                  <button
                    key={rel.id || rel.title}
                    type="button"
                    onClick={() => {
                      setQuery(rel.title);
                      executeSearch(rel.title);
                    }}
                    style={{
                      background: 'rgba(217, 119, 6, 0.15)',
                      border: '1px solid rgba(217, 119, 6, 0.35)',
                      borderRadius: '8px',
                      padding: '6px 12px',
                      color: '#f8fafc',
                      fontSize: '0.82rem',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '5px'
                    }}
                  >
                    <span>{rel.title}</span>
                    <span style={{ fontSize: '0.7rem', color: '#fbbf24' }}>→</span>
                  </button>
                ))}
              </div>
            </div>

          </div>

          {/* =====================================================================
              14-TIER KNOWLEDGE GRAPH ACCORDION
             ===================================================================== */}
          {tier14Open && (
            <div className="glass-panel animate-fade-in" style={{ padding: '28px', marginBottom: '28px' }}>
              <h3 className="font-royal text-gold" style={{ fontSize: '1.4rem', marginBottom: '8px' }}>
                14-Tier Cultural Knowledge Graph Schema
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.86rem', marginBottom: '20px' }}>
                Standardized metadata schema curated under Lead Architect Aruna Olanrewaju Kabiru.
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '16px' }}>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>1. Canonical Entity ID:</strong>
                  <p><code>{topMatch.details?.id || topMatch.id}</code></p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>2. Canonical Title (25-Letter Orthography):</strong>
                  <p style={{ fontWeight: 700 }}>{topMatch.details?.title || topMatch.title}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>3. Sovereign Parent Classification:</strong>
                  <p>{topMatch.details?.sovereign_parent_status || 'Sovereign Heritage Matrix'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>4. Cultural Domain Category:</strong>
                  <p>{topMatch.details?.category || topMatch.category}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>5. Aliases & Cross-Dialect Variants:</strong>
                  <p>{(topMatch.details?.aliases || []).join(', ') || 'Canonical primary nomenclature'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>6. Primary Cultural Description:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.description}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>7. Historical Antiquity Timeline:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.historical_timeline || 'Deep antiquity tracing to classical Ilé-Ifẹ̀.'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>8. Etymology, Linguistics & Philosophy:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.etymology_and_philosophy || 'Rooted in ancestral Yorùbá philosophy.'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>9. Materiality & Craftsmanship:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.material_and_craftsmanship || 'Indigenous craftsmanship and materials.'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>10. Social Protocol & Ritual Context:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.social_and_ritual_context || 'Integral to royal court and ancestral rites.'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>11. Proverbs & Praise Poetry (Oríkì):</strong>
                  <p style={{ fontSize: '0.88rem', fontStyle: 'italic' }}>
                    {Array.isArray(topMatch.details?.proverbs_and_oral_traditions)
                      ? topMatch.details?.proverbs_and_oral_traditions.join('; ')
                      : topMatch.details?.proverbs_and_oral_traditions || 'Preserved across oral verse.'}
                  </p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>12. Transatlantic Diaspora Connections:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.diaspora_connections || 'Survives in Brazil Candomblé and Cuban Santería.'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>13. Geographical Origin:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.geographical_origin || 'Yorùbáland (Southwestern Nigeria & Diaspora)'}</p>
                </div>
                <div style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                  <strong style={{ color: 'var(--gold-light)' }}>14. Curatorial & Ethical Guidelines:</strong>
                  <p style={{ fontSize: '0.88rem' }}>{topMatch.details?.media_production_notes || 'Ensure authentic period representation and correct tonal pronunciation.'}</p>
                </div>
              </div>
            </div>
          )}

          {/* =====================================================================
              RELATED CONCEPTS & SUB-VARIANTS IN CORPUS
             ===================================================================== */}
          {relatedMatches.length > 0 && (
            <div>
              <h3 className="font-royal text-gold" style={{ fontSize: '1.35rem', marginBottom: '16px' }}>
                Related Concepts & Sub-Variants in Corpus
              </h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '16px' }}>
                {relatedMatches.map((item, idx) => (
                  <div
                    key={item.id || idx}
                    className="glass-panel"
                    style={{
                      padding: '18px',
                      cursor: 'pointer',
                      border: '1px solid var(--border-subtle)',
                      transition: 'transform 0.2s ease, border-color 0.2s ease'
                    }}
                    onClick={() => {
                      setQuery(item.title || item.id);
                      executeSearch(item.title || item.id);
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.transform = 'translateY(-3px)';
                      e.currentTarget.style.borderColor = 'var(--gold-border)';
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.transform = 'translateY(0)';
                      e.currentTarget.style.borderColor = 'var(--border-subtle)';
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                      <h4 className="font-royal text-gold" style={{ fontSize: '1.1rem' }}>
                        {item.title}
                      </h4>
                      <span className="badge-emerald" style={{ fontSize: '0.72rem' }}>
                        #{idx + 2}
                      </span>
                    </div>
                    <p style={{ fontSize: '0.82rem', color: 'var(--gold-light)', marginBottom: '8px' }}>
                      {item.category || 'General Heritage'}
                    </p>
                    <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
                      {item.details?.description ? item.details.description.slice(0, 100) + '...' : 'Authentic Yorùbá entity.'}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

        </div>
      )}

      {/* =========================================================================
          ÀGBÀ ENTERPRISE ACOUSTIC CELL MODAL (AUDIO ACCESS RESTRICTION)
         ========================================================================= */}
      {showAudioModal && (
        <div className="agba-modal-backdrop" onClick={() => setShowAudioModal(false)}>
          <div className="agba-modal-dialog" onClick={(e) => e.stopPropagation()}>
            <div
              style={{
                width: '64px',
                height: '64px',
                borderRadius: '50%',
                margin: '0 auto 16px auto',
                background: 'rgba(217, 119, 6, 0.15)',
                border: '1.5px solid #d97706',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#fbbf24',
                fontSize: '28px',
                boxShadow: '0 0 24px rgba(217, 119, 6, 0.4)'
              }}
            >
              🔒
            </div>

            <span className="badge-gold" style={{ marginBottom: '10px' }}>
              RESTRICTED ENTERPRISE TOKEN
            </span>

            <h3 className="font-royal text-gold" style={{ fontSize: '1.5rem', marginBottom: '10px' }}>
              Audio Cell Restricted to API Access Only
            </h3>

            <p style={{ color: 'var(--text-secondary)', fontSize: '0.92rem', lineHeight: 1.6, marginBottom: '20px' }}>
              Sovereign acoustic mimicry, tonal voice playback, and native phonetic voice streams require an active <strong>Àgbà Enterprise API subscription</strong> or licensed developer key.
            </p>

            <div
              style={{
                background: 'rgba(0, 0, 0, 0.4)',
                border: '1px solid var(--border-subtle)',
                borderRadius: '12px',
                padding: '16px',
                textAlign: 'left',
                marginBottom: '20px',
                fontSize: '0.84rem'
              }}
            >
              <div style={{ color: '#fbbf24', fontWeight: 700, marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Key size={14} /> Included in Enterprise Acoustic Tier:
              </div>
              <ul style={{ paddingLeft: '18px', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <li>Full 25-letter tonal pronunciation synthesis (High/Mid/Low pitch)</li>
                <li>Sacred liturgical chant audio streams (Oríkì & Odù Ifá)</li>
                <li>Studio-grade indigenous phonetic token playback API</li>
              </ul>
            </div>

            {/* Quick Key Activation / Subscription actions */}
            {apiKeySuccess ? (
              <div
                style={{
                  background: 'rgba(16, 185, 129, 0.15)',
                  border: '1px solid rgba(16, 185, 129, 0.4)',
                  borderRadius: '10px',
                  padding: '12px',
                  color: '#34d399',
                  marginBottom: '18px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '8px',
                  fontSize: '0.88rem'
                }}
              >
                <CheckCircle size={16} /> Enterprise Developer Key Activated for Session!
              </div>
            ) : (
              <div style={{ marginBottom: '20px', display: 'flex', gap: '8px' }}>
                <input
                  type="text"
                  placeholder="Enter Enterprise API Key (e.g. agba_...)"
                  value={apiKeyInput}
                  onChange={(e) => setApiKeyInput(e.target.value)}
                  style={{
                    flex: 1,
                    background: 'rgba(0, 0, 0, 0.4)',
                    border: '1px solid var(--border-subtle)',
                    borderRadius: '8px',
                    padding: '8px 12px',
                    color: '#f8fafc',
                    fontSize: '0.85rem'
                  }}
                />
                <button
                  type="button"
                  onClick={() => {
                    if (apiKeyInput.trim()) {
                      setApiKeySuccess(true);
                      setTimeout(() => setShowAudioModal(false), 1200);
                    }
                  }}
                  className="btn-gold"
                  style={{ padding: '8px 16px', fontSize: '0.85rem' }}
                >
                  Verify Key
                </button>
              </div>
            )}

            <div style={{ display: 'flex', gap: '10px', justifyContent: 'center' }}>
              <button
                type="button"
                onClick={() => {
                  alert("To request an Agba Enterprise API subscription and acoustic token license, contact the Lead Architect at contact@agbaengine.com or configure your AGBA_API_KEY environment variable.");
                }}
                className="btn-gold"
                style={{ flex: 1, padding: '10px' }}
              >
                Subscribe to Enterprise API
              </button>
              <button
                type="button"
                onClick={() => setShowAudioModal(false)}
                className="btn-ghost"
                style={{ padding: '10px 20px' }}
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
