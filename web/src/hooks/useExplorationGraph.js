import { useState, useRef, useCallback, useEffect, useMemo } from 'react';

const STORAGE_KEY = 'agba_vein_rabbit_hole_v1';

export const PEER_CULTURES = {
  yoruba: {
    id: 'yoruba',
    label: 'Yorùbá',
    subtitle: 'Ìmọ̀ Yorùbá • 1,411 Canonical Nodes & 256 Odù Ifá',
    diacriticLabel: 'Àmì Ohùn',
    diacritics: ['À', 'Á', 'È', 'É', 'Ẹ̀', 'Ẹ́', 'Ì', 'Í', 'Ò', 'Ó', 'Ọ̀', 'Ọ́', 'Ù', 'Ú', 'Ṣ'],
    anchors: ['Òkèlè', 'Amàlà', 'Ìyán', 'Agbádá', 'Odù Ifá', 'Ògún', 'Bàtá', 'Adé', 'Ọfà', 'Ọbẹ̀'],
    accent: '#d4af37',
    traditionLabel: 'Yorùbá Classical (25-Letter Orthography)',
    productionUnlocked: true,
    statusBadge: 'ACTIVE CANON'
  },
  edo: {
    id: 'edo',
    label: 'Ẹ̀dó (Benin)',
    subtitle: 'Ìmọ̀ Ẹ̀dó • Royal Guilds & Sacred Bronzes',
    diacriticLabel: 'Àmì Ohùn Ẹ̀dó',
    diacritics: ['À', 'Á', 'È', 'É', 'Ẹ', 'Ẹ̀', 'Ẹ́', 'Ì', 'Í', 'Ò', 'Ó', 'Ọ', 'Ọ̀', 'Ọ́', 'Ù', 'Ú', 'Vb', 'Kh', 'Gh', 'Rh'],
    anchors: ['Ọba', 'Adé', 'Idà', 'Igun Eronmwon', 'Ilé-Ifẹ̀', 'Olókun', 'Ààfin'],
    accent: '#e05a2b',
    traditionLabel: 'Ẹ̀dó / Kingdom of Benin Peer Canon',
    productionUnlocked: false,
    statusBadge: 'LOCKED • SEQUENTIAL INGESTION'
  },
  igbo: {
    id: 'igbo',
    label: 'Ìgbò',
    subtitle: 'Àmàmìhè Ìgbò • Afa, Nsibidi & Ụzụ Guilds',
    diacriticLabel: 'Akara Udaolu',
    diacritics: ['Ị', 'Ị̀', 'Ị́', 'Ọ', 'Ọ̀', 'Ọ́', 'Ụ', 'Ụ̀', 'Ụ́', 'Ṅ', 'À', 'Á', 'È', 'É', 'Ò', 'Ó', 'Gb', 'Kp', 'Nw'],
    anchors: ['Obì', 'Iṣu', 'Ọfọ', 'Ikenga', 'Nsibidi', 'Ọbẹ̀', 'Ìyán'],
    accent: '#10b981',
    traditionLabel: 'Ásụ̀sụ̀ Ìgbò (Ọnwụ Orthography Parity)',
    productionUnlocked: false,
    statusBadge: 'LOCKED • SEQUENTIAL INGESTION'
  },
  akan: {
    id: 'akan',
    label: 'Akan (Asante)',
    subtitle: 'Nyansa Akan • Adinkra, Kente & Atumpan',
    diacriticLabel: 'Akan Orthography',
    diacritics: ['Ɛ', 'ɛ', 'Ɔ', 'ɔ', 'À', 'Á', 'È', 'É', 'Ì', 'Í', 'Ò', 'Ó', 'Ù', 'Ú', 'Dw', 'Gy', 'Ky', 'Tw'],
    anchors: ['Adinkra', 'Sika Dwa', 'Atumpan', 'Aṣọ Òkè', 'Ọba', 'Òwe'],
    accent: '#f59e0b',
    traditionLabel: 'Akan / Ashanti Peer Sovereign Canon',
    productionUnlocked: false,
    statusBadge: 'LOCKED • SEQUENTIAL INGESTION'
  }
};

export function useExplorationGraph(activeCulture = 'yoruba') {
  const navLockRef = useRef(false);

  const [graph, setGraph] = useState(() => {
    try {
      const saved = sessionStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed && Array.isArray(parsed.nodes) && Array.isArray(parsed.edges)) {
          return parsed;
        }
      }
    } catch (_) {
      // ignore sessionStorage read issues
    }
    return {
      rootQuery: '',
      cultureId: activeCulture,
      nodes: [],
      edges: [],
      activeNodeId: null
    };
  });

  useEffect(() => {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(graph));
    } catch (_) {
      // ignore quota limits
    }
  }, [graph]);

  // Seed the primary arterial vein from the Central Tooth to Node 1
  const startVeinFromTooth = useCallback((queryText, firstEntity) => {
    if (navLockRef.current || !firstEntity) return;
    navLockRef.current = true;

    const entityId = firstEntity.id || firstEntity.entity_id || firstEntity.title;
    const firstNodeId = `node_1_0_${entityId}`;
    const firstNode = {
      nodeId: firstNodeId,
      entityId,
      title: firstEntity.title,
      category: firstEntity.category || 'Sovereign Concept',
      depth: 1,
      parentNodeId: 'AARIN_ROOT',
      branchIndex: 0,
      relationLabel: 'Root Search Anchor',
      queryContext: queryText,
      entityData: firstEntity
    };

    setGraph({
      rootQuery: queryText,
      cultureId: activeCulture,
      nodes: [firstNode],
      edges: [
        {
          edgeId: `edge_TOOTH_ROOT_to_${firstNodeId}`,
          fromId: 'TOOTH_ROOT',
          toId: firstNodeId,
          relationType: 'PRIMARY_SEARCH_VEIN'
        }
      ],
      activeNodeId: firstNodeId
    });

    setTimeout(() => {
      navLockRef.current = false;
    }, 120);
  }, [activeCulture]);

  // Grow/branch a new vein thread when clicking deeper into related entries or variants
  const branchVeinToRelative = useCallback((targetEntity, relationLabel = 'Cultural Relative') => {
    if (navLockRef.current || !targetEntity) return;
    navLockRef.current = true;

    setGraph((prev) => {
      const targetEntityId = targetEntity.id || targetEntity.entity_id || targetEntity.title;
      const existingNode = prev.nodes.find(
        (n) => n.entityId === targetEntityId || n.title === targetEntity.title
      );
      if (existingNode) {
        return {
          ...prev,
          activeNodeId: existingNode.nodeId,
          nodes: prev.nodes.map((n) =>
            n.nodeId === existingNode.nodeId ? { ...n, entityData: targetEntity } : n
          )
        };
      }

      const sourceId = prev.activeNodeId || prev.nodes[prev.nodes.length - 1]?.nodeId || 'TOOTH_ROOT';
      const sourceNode = prev.nodes.find((n) => n.nodeId === sourceId);
      const nextDepth = sourceNode ? sourceNode.depth + 1 : 1;
      const siblingsAtDepth = prev.nodes.filter((n) => n.depth === nextDepth).length;
      const newNodeId = `node_${nextDepth}_${siblingsAtDepth}_${targetEntityId}`;

      const newNode = {
        nodeId: newNodeId,
        entityId: targetEntityId,
        title: targetEntity.title,
        category: targetEntity.category || 'Connected Relative',
        depth: nextDepth,
        parentNodeId: sourceId,
        branchIndex: siblingsAtDepth,
        relationLabel,
        queryContext: targetEntity.title,
        entityData: targetEntity
      };

      const newEdge = {
        edgeId: `edge_${sourceId}_to_${newNodeId}`,
        fromId: sourceId,
        toId: newNodeId,
        relationType: relationLabel
      };

      return {
        ...prev,
        nodes: [...prev.nodes, newNode],
        edges: [...prev.edges, newEdge],
        activeNodeId: newNodeId
      };
    });

    setTimeout(() => {
      navLockRef.current = false;
    }, 120);
  }, []);

  // Retrace to any ancestor node along the vein (or back to the Sovereign Hearth)
  const retraceToNode = useCallback((targetNodeId) => {
    if (navLockRef.current) return null;
    if (targetNodeId === 'AARIN_ROOT' || targetNodeId === 'OPON_ROOT' || targetNodeId === 'TOOTH_ROOT') {
      const rootNode = graph.nodes[0] || null;
      setGraph((prev) => ({
        ...prev,
        activeNodeId: prev.nodes[0]?.nodeId || null
      }));
      return rootNode;
    }
    const found = graph.nodes.find((n) => n.nodeId === targetNodeId) || null;
    if (found) {
      setGraph((prev) => ({ ...prev, activeNodeId: targetNodeId }));
    }
    return found;
  }, [graph.nodes]);

  const resetRabbitHole = useCallback(() => {
    setGraph({
      rootQuery: '',
      cultureId: activeCulture,
      nodes: [],
      edges: [],
      activeNodeId: null
    });
  }, [activeCulture]);

  const activeNode = useMemo(
    () => graph.nodes.find((n) => n.nodeId === graph.activeNodeId) || null,
    [graph.nodes, graph.activeNodeId]
  );

  // Active arterial lineage from AARIN_ROOT down to activeNodeId
  const activeLineageIds = useMemo(() => {
    const lineage = new Set(['AARIN_ROOT', 'OPON_ROOT', 'TOOTH_ROOT']);
    let curr = activeNode;
    while (curr) {
      lineage.add(curr.nodeId);
      curr = graph.nodes.find((n) => n.nodeId === curr.parentNodeId);
    }
    return lineage;
  }, [graph.nodes, activeNode]);

  return {
    graph,
    activeNode,
    activeLineageIds,
    startVeinFromHearth: startVeinFromTooth,
    startVeinFromOpon: startVeinFromTooth,
    startVeinFromTooth,
    branchVeinToRelative,
    retraceToNode,
    resetRabbitHole
  };
}
