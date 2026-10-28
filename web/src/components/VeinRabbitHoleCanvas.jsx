import React, { useMemo } from 'react';
import { GitBranch, RotateCcw, Sparkles, Compass } from 'lucide-react';

export default function VeinRabbitHoleCanvas({
  graph,
  activeNode,
  activeLineageIds,
  onRetraceToNode,
  onResetRabbitHole
}) {
  const nodes = graph?.nodes || [];
  const edges = graph?.edges || [];

  // Compute 2D layout coordinates (x, y) in a virtual 920px SVG canvas for every node along the rabbit hole
  const layout = useMemo(() => {
    if (nodes.length === 0) return { nodeCoords: {}, svgHeight: 90, depthGroups: [] };

    const maxDepth = Math.max(...nodes.map((n) => n.depth), 1);
    const rowHeight = 82;
    const topY = 18;
    const centerX = 460;

    const nodeCoords = {
      AARIN_ROOT: { x: centerX, y: 0, title: 'Àárín Ìmọ̀ (Hearth Origin)' },
      OPON_ROOT: { x: centerX, y: 0, title: 'Àárín Ìmọ̀ (Hearth Origin)' },
      TOOTH_ROOT: { x: centerX, y: 0, title: 'Àárín Ìmọ̀ (Hearth Origin)' }
    };

    const depthGroups = [];
    for (let d = 1; d <= maxDepth; d++) {
      const atDepth = nodes.filter((n) => n.depth === d);
      depthGroups.push({ depth: d, items: atDepth });

      const count = atDepth.length;
      atDepth.forEach((node, idx) => {
        const spread = Math.min(240, 680 / Math.max(count, 1));
        const xOffset = count === 1 ? 0 : (idx - (count - 1) / 2) * spread;
        nodeCoords[node.nodeId] = {
          x: centerX + xOffset,
          y: topY + d * rowHeight - 28,
          node
        };
      });
    }

    return {
      nodeCoords,
      svgHeight: topY + maxDepth * rowHeight + 24,
      depthGroups,
      maxDepth
    };
  }, [nodes]);

  if (nodes.length === 0) return null;

  return (
    <div
      className="glass-panel animate-fade-in"
      style={{
        maxWidth: '1040px',
        margin: '0 auto 28px auto',
        padding: '18px 22px 22px 22px',
        border: '1px solid rgba(217, 119, 6, 0.4)',
        background: 'linear-gradient(180deg, rgba(15, 23, 42, 0.92) 0%, rgba(9, 13, 22, 0.96) 100%)',
        boxShadow: '0 14px 40px rgba(0, 0, 0, 0.55), inset 0 1px 1px rgba(243, 229, 171, 0.15)',
        position: 'relative'
      }}
    >
      {/* Top Status & Retrace Controls Bar */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '10px',
          marginBottom: '10px',
          borderBottom: '1px solid rgba(255, 255, 255, 0.07)',
          paddingBottom: '10px'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
          <span className="badge-gold">
            <GitBranch size={12} /> VASCULAR RABBIT-HOLE TRAIL
          </span>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
            Depth <strong style={{ color: '#fbbf24' }}>{activeNode?.depth || 1}</strong> •{' '}
            <strong>{nodes.length}</strong> {nodes.length === 1 ? 'Vein Node' : 'Vein Nodes Explored'}
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          {nodes.length > 1 && (
            <button
              type="button"
              onClick={() => onRetraceToNode('TOOTH_ROOT')}
              className="btn-ghost-gold"
              style={{
                padding: '5px 12px',
                fontSize: '0.76rem',
                borderRadius: '999px',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '5px'
              }}
              title="Retrace the vein back to your first search entry"
            >
              <Compass size={13} />
              Retrace to Origin Anchor (#1: {nodes[0]?.title})
            </button>
          )}
          <button
            type="button"
            onClick={onResetRabbitHole}
            className="btn-ghost"
            style={{
              padding: '5px 11px',
              fontSize: '0.75rem',
              borderRadius: '999px',
              display: 'inline-flex',
              alignItems: 'center',
              gap: '5px'
            }}
            title="Clear vascular trail"
          >
            <RotateCcw size={12} />
            Prune Trail
          </button>
        </div>
      </div>

      {/* =====================================================================
          DYNAMIC CUBIC BÉZIER VASCULAR VEIN GRAPH (SVG + INTERACTIVE NODES)
         ===================================================================== */}
      <div style={{ width: '100%', overflowX: 'auto' }}>
        <svg
          width="100%"
          height={layout.svgHeight}
          viewBox={`0 0 920 ${layout.svgHeight}`}
          style={{ overflow: 'visible', display: 'block', minWidth: '580px' }}
        >
          <defs>
            <linearGradient id="veinPrimaryGold" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#fbbf24" />
              <stop offset="50%" stopColor="#d97706" />
              <stop offset="100%" stopColor="#f3e5ab" />
            </linearGradient>
            <linearGradient id="veinDormantAmber" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="rgba(217, 119, 6, 0.45)" />
              <stop offset="100%" stopColor="rgba(148, 163, 184, 0.25)" />
            </linearGradient>
          </defs>

          {/* 1. Render Cubic Bézier Vein Threads Connecting Tooth -> Node 1 -> Node 2 -> ... */}
          {edges.map((edge) => {
            const p1 = layout.nodeCoords[edge.fromId];
            const p2 = layout.nodeCoords[edge.toId];
            if (!p1 || !p2) return null;

            const isActiveLineage =
              activeLineageIds.has(edge.fromId) && activeLineageIds.has(edge.toId);
            const midY = (p1.y + p2.y) / 2;
            const dPath = `M ${p1.x} ${p1.y} C ${p1.x} ${midY}, ${p2.x} ${midY}, ${p2.x} ${p2.y}`;

            return (
              <g key={edge.edgeId}>
                {/* Outer Vascular Glow Wall */}
                <path
                  d={dPath}
                  fill="none"
                  stroke={isActiveLineage ? 'rgba(217, 119, 6, 0.35)' : 'rgba(148, 163, 184, 0.12)'}
                  strokeWidth={isActiveLineage ? 7 : 3}
                  strokeLinecap="round"
                />
                {/* Inner Pulsing Arterial Thread */}
                <path
                  d={dPath}
                  fill="none"
                  stroke={isActiveLineage ? 'url(#veinPrimaryGold)' : 'url(#veinDormantAmber)'}
                  strokeWidth={isActiveLineage ? 2.8 : 1.6}
                  strokeDasharray={isActiveLineage ? 'none' : '5 4'}
                  strokeLinecap="round"
                  className={isActiveLineage ? 'root-vessel-line' : ''}
                />
              </g>
            );
          })}

          {/* 2. Render Origin Hearth Junction at (460, 6) */}
          <g
            style={{ cursor: 'pointer' }}
            onClick={() => onRetraceToNode('AARIN_ROOT')}
          >
            <circle
              cx={460}
              cy={8}
              r={7}
              fill="#fbbf24"
              stroke="#0f172a"
              strokeWidth="2"
            />
            <text
              x={474}
              y={12}
              fill="#fbbf24"
              fontSize="11"
              fontWeight="700"
              style={{ letterSpacing: '0.05em' }}
            >
              👑 ÀÁRÍN ÌMỌ̀ ({graph.rootQuery || nodes[0]?.title})
            </text>
          </g>

          {/* 3. Render Interactive Vascular Node Pills at Every Depth */}
          {nodes.map((node) => {
            const coord = layout.nodeCoords[node.nodeId];
            if (!coord) return null;

            const isCurrent = activeNode?.nodeId === node.nodeId;
            const isInLineage = activeLineageIds.has(node.nodeId);
            const pillW = 196;
            const pillH = 44;

            return (
              <g
                key={node.nodeId}
                transform={`translate(${coord.x - pillW / 2}, ${coord.y - pillH / 2})`}
                style={{ cursor: 'pointer' }}
                onClick={() => onRetraceToNode(node.nodeId)}
              >
                <rect
                  width={pillW}
                  height={pillH}
                  rx={12}
                  ry={12}
                  fill={
                    isCurrent
                      ? 'rgba(217, 119, 6, 0.28)'
                      : isInLineage
                      ? 'rgba(22, 32, 54, 0.96)'
                      : 'rgba(15, 23, 42, 0.78)'
                  }
                  stroke={
                    isCurrent
                      ? '#fbbf24'
                      : isInLineage
                      ? 'rgba(217, 119, 6, 0.65)'
                      : 'rgba(148, 163, 184, 0.25)'
                  }
                  strokeWidth={isCurrent ? 2.2 : 1.3}
                />
                <circle
                  cx={16}
                  cy={pillH / 2}
                  r={5}
                  fill={isCurrent ? '#34d399' : isInLineage ? '#fbbf24' : '#64748b'}
                />
                <text
                  x={28}
                  y={18}
                  fill="#fbbf24"
                  fontSize="9.5"
                  fontWeight="700"
                >
                  {`HOP #${node.depth} • ${(node.relationLabel || 'VEIN NODE').toUpperCase().slice(0, 18)}`}
                </text>
                <text
                  x={28}
                  y={33}
                  fill="#f8fafc"
                  fontSize="12.5"
                  fontWeight="700"
                >
                  {node.title.length > 20 ? node.title.slice(0, 19) + '…' : node.title}
                </text>
              </g>
            );
          })}
        </svg>
      </div>

      {/* Breadcrumb Quick-Jump Strip for Mobile & Rapid Ancestor Retracing */}
      <div
        style={{
          marginTop: '8px',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          flexWrap: 'wrap',
          fontSize: '0.78rem',
          color: 'var(--text-secondary)'
        }}
      >
        <span style={{ color: 'var(--text-muted)', display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
          <Sparkles size={12} color="#d4af37" /> Click any node on the vein to retrace:
        </span>
        <button
          type="button"
          onClick={() => onRetraceToNode('AARIN_ROOT')}
          style={{
            background: 'rgba(212, 175, 55, 0.12)',
            border: '1px solid rgba(212, 175, 55, 0.35)',
            color: 'var(--gold-light)',
            borderRadius: '999px',
            padding: '2px 9px',
            fontSize: '0.74rem',
            cursor: 'pointer',
            fontWeight: 700
          }}
        >
          👑 Àárín Ìmọ̀
        </button>
        {nodes.map((n, idx) => {
          const isCurrent = activeNode?.nodeId === n.nodeId;
          return (
            <React.Fragment key={n.nodeId}>
              <span style={{ color: '#d97706' }}>──►</span>
              <button
                type="button"
                onClick={() => onRetraceToNode(n.nodeId)}
                style={{
                  background: isCurrent ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255, 255, 255, 0.05)',
                  border: isCurrent ? '1px solid #10b981' : '1px solid rgba(255, 255, 255, 0.12)',
                  color: isCurrent ? '#34d399' : '#f8fafc',
                  borderRadius: '999px',
                  padding: '2px 10px',
                  fontSize: '0.75rem',
                  cursor: 'pointer',
                  fontWeight: isCurrent ? 700 : 500
                }}
              >
                {idx + 1}. {n.title}
              </button>
            </React.Fragment>
          );
        })}
      </div>
    </div>
  );
}
