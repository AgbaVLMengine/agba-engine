import React, { useState, useMemo, useRef, useCallback } from 'react';
import masterCorpus from '../data/yoruba_master_corpus.json';
import { useExplorationGraph, PEER_CULTURES } from '../hooks/useExplorationGraph';
import { useRootNetworkNodes } from '../hooks/useRootNetworkNodes';
import OponSearchCore from './OponSearchCore';
import VeinRabbitHoleCanvas from './VeinRabbitHoleCanvas';
import EntityBentoDeck from './EntityBentoDeck';
import { resolveKnowledgeGraphRelatives } from '../utils/relativesResolver';
import { hydrateSubVariantFromParent, findSubVariantMatchInCorpus } from '../utils/subVariantHydrator';
import { extractTonalContour } from '../utils/tonalContour';
import { searchRankedCorpus } from '../utils/localRankedSearch';
import { hydrateEntityForBento } from '../utils/bentoHydrator';

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
    startVeinFromHearth,
    startVeinFromOpon,
    startVeinFromTooth,
    branchVeinToRelative,
    retraceToNode,
    resetRabbitHole
  } = useExplorationGraph(activeCulture);

  const rootNetworkNodes = useRootNetworkNodes(query, masterCorpus);

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

        // Dynamic Sub-Variant Fallback Hydrator (Anti-Parent-Loop Guard)
        const svMatch = findSubVariantMatchInCorpus(q, masterCorpus);
        if (svMatch) {
          const synthChild = hydrateSubVariantFromParent(svMatch.variantTitle, svMatch.parent);
          rankedEntities = [hydrateEntityForBento(synthChild, 1.0)];
          setResults({
            status: 'success',
            ranked_entities: rankedEntities
          });
        } else {
          const controller = new AbortController();
          const timeoutId = setTimeout(() => controller.abort(), 1200);
          try {
            const endpoint = apiBaseUrl ? `${apiBaseUrl.replace(/\/$/, '')}/v6/retrieve/deep-context` : '/v6/retrieve/deep-context';
            const res = await fetch(endpoint, {
              method: 'POST',
              signal: controller.signal,
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
            // Air-gap & cold-start timeout fallback to local sovereign ranked search
          } finally {
            clearTimeout(timeoutId);
          }

          if (rankedEntities.length === 0) {
            const localMatches = searchRankedCorpus(q, masterCorpus);
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
        }

        if (rankedEntities.length > 0) {
          const primaryEntity = rankedEntities[0];
          if (options.isBranchHop) {
            branchVeinToRelative(primaryEntity, options.relationLabel || 'Rabbit-Hole Hop');
          } else {
            (startVeinFromHearth || startVeinFromOpon || startVeinFromTooth)(q, primaryEntity);
          }
        }
      } finally {
        setLoading(false);
        busyRef.current = false;
      }
    },
    [apiBaseUrl, branchVeinToRelative, query, startVeinFromHearth, startVeinFromOpon, startVeinFromTooth]
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
    [retraceToNode]
  );

  const handleCuratedDiscovery = () => {
    const anchors = PEER_CULTURES[activeCulture]?.anchors || PEER_CULTURES.yoruba.anchors;
    const randomConcept = anchors[Math.floor(Math.random() * anchors.length)];
    setQuery(randomConcept);
    executeSearch(randomConcept, { isBranchHop: false, relationLabel: 'Curated Anchor' });
  };

  const topMatch = results?.ranked_entities?.[0]
    ? results.ranked_entities[0]
    : (activeNode?.entityData ? hydrateEntityForBento(activeNode.entityData) : null);

  // RC-2 & RC-3 Fix: Global Knowledge Graph Relatives Resolver (Zero Repeated Category Slicing)
  const relatedMatches = useMemo(() => {
    return resolveKnowledgeGraphRelatives(topMatch, masterCorpus, 6);
  }, [topMatch]);

  const tonalContour = topMatch ? extractTonalContour(topMatch.title) : [];

  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* 1. CENTRAL OPON IFA SEARCH CORE & MULTI-CULTURE SWITCHER */}
      <OponSearchCore
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
          busyRef.current = false;
          setLoading(false);
          setQuery(nodeObj.title);
          executeSearch(nodeObj.title, { isBranchHop: true, relationLabel: relType });
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
