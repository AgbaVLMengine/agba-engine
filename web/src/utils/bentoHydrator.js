import visualManifest from '../data/agba_unified_visual_regalia_manifest.json';
import { normalizeNFC, stripAccents } from './tonalContour';

export function findVisualRegaliaHit(rawTitle) {
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
}

export function hydrateEntityForBento(m, score = 0.992) {
  if (!m) return null;
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
}
