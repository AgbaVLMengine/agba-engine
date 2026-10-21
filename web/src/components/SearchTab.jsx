import React, { useState, useMemo, useRef, useCallback } from 'react';
import visualManifest from '../data/agba_unified_visual_regalia_manifest.json';
import masterCorpus from '../data/yoruba_master_corpus.json';
import { useExplorationGraph, PEER_CULTURES } from '../hooks/useExplorationGraph';
import ToothSearchCore from './ToothSearchCore';
import VeinRabbitHoleCanvas from './VeinRabbitHoleCanvas';
import EntityBentoDeck from './EntityBentoDeck';
import { resolveKnowledgeGraphRelatives } from '../utils/relativesResolver';

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function normalizeNFC(s) {
  return (s || '').trim().toLowerCase().normalize('NFC');
}

function escapeRegExp(s) {
  return (s || '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Generate tonal contour breakdown using NFC/NFD grapheme clusters (High: ´, Low: `, Mid: none)
function extractTonalContour(word) {
  if (!word) return [];
  const firstWord = word.normalize('NFC').split(/\s+/)[0] || word;
  const tones = [];
  const segments = Array.from(firstWord);

  for (const ch of segments) {
    const nfd = ch.normalize('NFD');
    const base = nfd[0]?.toLowerCase() || '';
    if (!'aeiouẹọ'.includes(base) && !'aeiou'.includes(nfd[0]?.toLowerCase())) continue;

    if (nfd.includes('\u0301')) {
      tones.push({ char: ch.normalize('NFC'), pitch: 'High (Mí)', arrow: '↗' });
    } else if (nfd.includes('\u0300')) {
      tones.push({ char: ch.normalize('NFC'), pitch: 'Low (Dò)', arrow: '↘' });
    } else {
      tones.push({ char: ch.normalize('NFC'), pitch: 'Mid (Rè)', arrow: '→' });
    }
  }
  return tones.slice(0, 5);
}

export default function SearchTab({ apiBaseUrl, onOpenFeedback }) {
  const [query, setQuery] = useState('');
  const [activeCulture, setActiveCulture] = useState('yoruba');
  const [hasSearched, setHasSearched] = useState(false);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [errorMsg, setErrorMsg] = useState('');
  const [isFocused, setIsFocused] = useState(false);

  // Synchronous double-tap lock for search and branch mutations
  const busyRef = useRef(false);

  const {
    graph,
    activeNode,
    activeLineageIds,
    startVeinFromTooth,
    branchVeinToRelative,
    retraceToNode,
    resetRabbitHole
  } = useExplorationGraph(activeCulture);

  const findVisualRegaliaHit = useCallback((rawTitle) => {
    if (!rawTitle) return null;
    const tNFC = normalizeNFC(rawTitle);
    const tClean = stripAccents(rawTitle);
    return (
      visualManifest.find((v) => normalizeNFC(v.canonical_name) === tNFC) ||
      visualManifest.find((v) =>
        (v.canonical_name || '')
          .split('/')
          .map((p) => normalizeNFC(p))
          .includes(tNFC)
      ) ||
      visualManifest.find((v) => stripAccents(v.canonical_name) === tClean) ||
      visualManifest.find((v) =>
        (v.canonical_name || '')
          .split('/')
          .map((p) => stripAccents(p.trim()))
          .includes(tClean)
      )
    );
  }, []);

  const resolveSubVariantEntities = useCallback((subVariantNames = []) => {
    const resolved = [];
    for (const svName of subVariantNames) {
      const svNFC = normalizeNFC(svName);
      const svClean = stripAccents(svName);
      const hit =
        masterCorpus.find((e) => normalizeNFC(e.title) === svNFC || normalizeNFC(e.id) === svNFC) ||
        masterCorpus.find((e) => stripAccents(e.title) === svClean || e.id === svName);
      if (hit) {
        resolved.push(hit);
      } else {
        resolved.push({
          id: `variant_${svClean}`,
          title: svName,
          category: 'Living Sub-Variant',
          description: `Canonical living variant within the ${svName} lineage.`
        });
      }
    }
    return resolved;
  }, []);

  // RC-2 Fix: Strict Word-Boundary & is_parent Root Network Resolver (Zero Substring Leakage)
  const rootNetworkNodes = useMemo(() => {
    const qTrim = query.trim();
    if (!qTrim || qTrim.length < 2) return null;
    const qNFC = normalizeNFC(qTrim);
    const qClean = stripAccents(qTrim);
    const hasDiacritics = qNFC !== qClean;
    const wordBoundaryRegex = new RegExp(`\\b${escapeRegExp(qClean)}\\b`, 'i');

    const matches = masterCorpus.filter((item) => {
      const tNFC = normalizeNFC(item.title);
      const tClean = stripAccents(item.title);
      const aliasesClean = (item.aliases || []).map(stripAccents);
      if (hasDiacritics && tClean === qClean && tNFC !== qNFC) return false;
      return (
        tNFC === qNFC ||
        (!hasDiacritics && tClean === qClean) ||
        wordBoundaryRegex.test(tClean) ||
        aliasesClean.some((a) => a === qClean || wordBoundaryRegex.test(a))
      );
    });

    if (matches.length === 0) return null;

    // Prioritize exact title match or verified Sovereign Parent (is_parent === true)
    const exactMatch =
      matches.find((m) => normalizeNFC(m.title) === qNFC) ||
      matches.find((m) => stripAccents(m.title) === qClean && (m.is_parent === true || m.sovereign_parent_status === 'Sovereign Parent Concept')) ||
      matches.find((m) => stripAccents(m.title) === qClean);

    const parentNode =
      exactMatch ||
      matches.find((m) => m.is_parent === true || m.sovereign_parent_status === 'Sovereign Parent Concept') ||
      matches[0];

    let childVariants = [];
    if (Array.isArray(parentNode.sub_variants) && parentNode.sub_variants.length > 0) {
      childVariants = resolveSubVariantEntities(parentNode.sub_variants).slice(0, 4);
    } else {
      childVariants = matches.filter((m) => m.title !== parentNode.title).slice(0, 4);
    }

    const relatedRegalia = findVisualRegaliaHit(parentNode.title) || findVisualRegaliaHit(qTrim);

    return {
      query: qTrim,
      parent: parentNode,
      variants: childVariants,
      regalia: relatedRegalia,
      totalCount: matches.length
    };
  }, [findVisualRegaliaHit, query, resolveSubVariantEntities]);

  // RC-1 & RC-3 Local Ranked Search Fallback (Tonal Invariant Tiering)
  const searchRankedCorpus = useCallback((q) => {
    const qClean = (q || '').replace(/[?!.,;:'"]/g, '').trim();
    const coreSubject = qClean
      .replace(/^(who is|what is|tell me about|explain|who was|what was|meaning of|history of|where is|why is)\s+/i, '')
      .trim();

    const normQ = normalizeNFC(qClean);
    const normCore = normalizeNFC(coreSubject);
    const qStripped = stripAccents(qClean);
    const coreStripped = stripAccents(coreSubject);
    const hasQueryDiacritics = normQ !== qStripped;

    const stopWords = new Set([
      'who', 'what', 'where', 'why', 'how', 'tell', 'about', 'and', 'the',
      'for', 'with', 'is', 'are', 'was', 'were', 'yoruba', 'tradition', 'meaning'
    ]);
    const qTokens = qStripped.split(/\s+/).filter((w) => w.length > 1 && !stopWords.has(w));
    const scored = [];

    for (const entity of masterCorpus) {
      const title = entity.title || '';
      const normTitle = normalizeNFC(title);
      const titleStripped = stripAccents(title);
      const aliases = entity.aliases || [];
      const normAliases = aliases.map(normalizeNFC);
      const aliasesStripped = aliases.map(stripAccents);
      const descStripped = stripAccents(entity.description || '');

      let score = 0;

      // 1A. Supreme Exact Tonal/Diacritic Match (+600)
      if (normCore && (normTitle === normCore || normalizeNFC(entity.id) === normCore)) score += 600;
      else if (normCore && normAliases.includes(normCore)) score += 540;
      else if (normQ && normTitle === normQ) score += 520;

      // 1B. Accent-Folded Match (+450 if un-diacritized, +180 if conflicting tones)
      if (coreStripped && titleStripped === coreStripped) {
        score += hasQueryDiacritics && normTitle !== normCore ? 180 : 450;
      } else if (coreStripped && aliasesStripped.includes(coreStripped)) {
        score += hasQueryDiacritics && !normAliases.includes(normCore) ? 150 : 400;
      }

      // 2. Word-boundary phrase match
      if (coreStripped && new RegExp(`\\b${escapeRegExp(coreStripped)}\\b`, 'i').test(titleStripped)) {
        score += 220;
      }

      for (const tok of qTokens) {
        const wordRegex = new RegExp(`\\b${escapeRegExp(tok)}\\b`, 'i');
        if (wordRegex.test(titleStripped)) score += 50;
        if (aliasesStripped.some((a) => wordRegex.test(a))) score += 40;
        if (wordRegex.test(descStripped)) score += 8;
      }

      if (score > 0) scored.push({ entity, score });
    }

    scored.sort((a, b) => b.score - a.score);
    return scored.map((s) => s.entity);
  }, []);

  const hydrateEntityForBento = useCallback((m, score = 0.992) => {
    const visualHit = findVisualRegaliaHit(m.title || m.details?.title);
    const hasVisual = !!(visualHit || m.multimodal_assets?.has_visual_asset);
    const resolvedSourceUrl =
      visualHit?.local_asset_url ||
      visualHit?.image_url ||
      m.multimodal_assets?.source_url ||
      null;

    if (m.details && m.multimodal_assets) {
      return {
        ...m,
        multimodal_assets: {
          ...m.multimodal_assets,
          has_visual_asset: !!(hasVisual && resolvedSourceUrl),
          source_url: resolvedSourceUrl,
          canonical_title_full: visualHit?.canonical_title_full || m.multimodal_assets.canonical_title_full || m.title,
          current_custodial_repository: visualHit?.current_custodial_repository || m.multimodal_assets.current_custodial_repository || 'Sovereign Heritage Vault',
          accession_number: visualHit?.accession_number || m.multimodal_assets.accession_number || 'ARCHIVE-001',
          medium_materials: visualHit?.medium_materials || m.multimodal_assets.medium_materials || m.details?.material_and_craftsmanship
        }
      };
    }

    return {
      id: m.id || m.title,
      title: m.title,
      category: m.category || 'Cultural Heritage',
      fusion_score: score,
      multimodal_assets: {
        has_visual_asset: !!(hasVisual && resolvedSourceUrl),
        source_url: resolvedSourceUrl,
        canonical_title_full: visualHit?.canonical_title_full || m.title,
        current_custodial_repository: visualHit?.current_custodial_repository || 'Sovereign Heritage Vault',
        accession_number: visualHit?.accession_number || 'ARCHIVE-001',
        medium_materials: visualHit?.medium_materials || m.material_and_craftsmanship || 'Preserved luxury handcraft',
        master_artisan_or_guild: visualHit?.master_artisan_or_guild || 'Imperial Palace Guild'
      },
      details: m
    };
  }, [findVisualRegaliaHit]);

  const executeSearch = useCallback(
    async (searchTerm, options = { isBranchHop: false, relationLabel: 'Root Search' }) => {
      const q = (searchTerm ?? query).trim();
      if (!q || busyRef.current) return;
      busyRef.current = true;

      setLoading(true);
      setErrorMsg('');
      setHasSearched(true);
      setIsFocused(false);

      try {
        let rankedEntities = [];
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
          if (res.ok) {
            const data = await res.json();
            if (data?.ranked_entities?.length > 0) {
              rankedEntities = data.ranked_entities;
              setResults(data);
            }
          }
        } catch (_) {
          // Fallback to local sovereign ranked search
        }

        if (rankedEntities.length === 0) {
          const localMatches = searchRankedCorpus(q);
          if (localMatches.length > 0) {
            rankedEntities = localMatches.slice(0, 6).map((m, idx) => hydrateEntityForBento(m, idx === 0 ? 0.992 : 0.88 - idx * 0.05));
            setResults({
              status: 'success',
              ranked_entities: rankedEntities
            });
          } else {
            setErrorMsg(`No direct matches found for '${q}'. Try searching for Òkèlè, Amàlà, Agbádá, Odù Ifá, Ògún, or Bàtá.`);
            setResults(null);
          }
        }

        if (rankedEntities.length > 0) {
          const primaryEntity = rankedEntities[0];
          if (options.isBranchHop) {
            branchVeinToRelative(primaryEntity, options.relationLabel || 'Rabbit-Hole Hop');
          } else {
            startVeinFromTooth(q, primaryEntity);
          }
        }
      } finally {
        setLoading(false);
        busyRef.current = false;
      }
    },
    [apiBaseUrl, branchVeinToRelative, hydrateEntityForBento, query, searchRankedCorpus, startVeinFromTooth]
  );

  const handleBranchToRelative = useCallback(
    (relEntity, relationLabel = 'Cultural Relative') => {
      const targetTitle = relEntity.title || relEntity.id;
      setQuery(targetTitle);
      executeSearch(targetTitle, { isBranchHop: true, relationLabel });
    },
    [executeSearch]
  );

  const handleRetraceVeinNode = useCallback(
    (nodeId) => {
      const retraced = retraceToNode(nodeId);
      if (retraced?.entityData) {
        setQuery(retraced.title);
        setResults({
          status: 'success',
          ranked_entities: [hydrateEntityForBento(retraced.entityData, 0.995)]
        });
      }
    },
    [hydrateEntityForBento, retraceToNode]
  );

  const handleCuratedDiscovery = () => {
    const anchors = PEER_CULTURES[activeCulture]?.anchors || PEER_CULTURES.yoruba.anchors;
    const randomConcept = anchors[Math.floor(Math.random() * anchors.length)];
    setQuery(randomConcept);
    executeSearch(randomConcept, { isBranchHop: false, relationLabel: 'Curated Anchor' });
  };

  const topMatch = activeNode?.entityData
    ? hydrateEntityForBento(activeNode.entityData)
    : results?.ranked_entities?.[0];

  // RC-2 & RC-3 Fix: Global Knowledge Graph Relatives Resolver (Zero Repeated Category Slicing)
  const relatedMatches = useMemo(() => {
    return resolveKnowledgeGraphRelatives(topMatch, masterCorpus, 6);
  }, [topMatch]);

  const tonalContour = topMatch ? extractTonalContour(topMatch.title) : [];

  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* 1. CENTRAL TOOTH SEARCH CORE & MULTI-CULTURE SWITCHER */}
      <ToothSearchCore
        query={query}
        setQuery={setQuery}
        loading={loading}
        hasSearched={hasSearched}
        isFocused={isFocused}
        setIsFocused={setIsFocused}
        activeCulture={activeCulture}
        onSelectCulture={(cultId) => setActiveCulture(cultId)}
        onExecuteSearch={(qText) => executeSearch(qText, { isBranchHop: false })}
        onCuratedDiscovery={handleCuratedDiscovery}
        onClearSearch={() => {
          setQuery('');
          setResults(null);
          setHasSearched(false);
          resetRabbitHole();
        }}
        rootNetworkNodes={rootNetworkNodes}
        onSelectRootNode={(nodeObj, relType) => {
          setQuery(nodeObj.title);
          executeSearch(nodeObj.title, { isBranchHop: hasSearched, relationLabel: relType });
        }}
      />

      {/* 2. LIVING VASCULAR VEIN RABBIT-HOLE TRAIL (TOOTH -> NODE 1 -> NODE 2 -> ...) */}
      <VeinRabbitHoleCanvas
        graph={graph}
        activeNode={activeNode}
        activeLineageIds={activeLineageIds}
        onRetraceToNode={handleRetraceVeinNode}
        onResetRabbitHole={() => {
          resetRabbitHole();
          setResults(null);
          setHasSearched(false);
        }}
      />

      {/* Error Notice */}
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

      {/* 3. 12-COLUMN CELLULAR BENTO DECK & 14-TIER GRAPH */}
      <EntityBentoDeck
        topMatch={topMatch}
        query={query}
        tonalContour={tonalContour}
        relatedMatches={relatedMatches}
        onBranchToRelative={handleBranchToRelative}
        onOpenFeedback={onOpenFeedback}
      />
    </div>
  );
}
