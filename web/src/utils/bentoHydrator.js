import visualManifest from '../data/agba_unified_visual_regalia_manifest.json';
import { normalizeNFC, stripAccents } from './tonalContour';

export function findVisualRegaliaHit(rawTitle, entity = null) {
  if (!rawTitle && !entity) return null;
  const title = rawTitle || entity?.title || entity?.details?.title || '';
  const tNFC = normalizeNFC(title);
  const tClean = stripAccents(title);
  const parent = entity?.sovereign_parent || entity?.details?.sovereign_parent || '';
  const pNFC = normalizeNFC(parent);
  const pClean = stripAccents(parent);

  // 1. Direct canonical name or slash-variant match
  const directHit = visualManifest.find((v) => {
    const vNFC = normalizeNFC(v.canonical_name || '');
    const vClean = stripAccents(v.canonical_name || '');
    if (vNFC === tNFC || vClean === tClean) return true;
    const slashParts = (v.canonical_name || '').split('/');
    if (slashParts.some((p) => normalizeNFC(p) === tNFC || stripAccents(p.trim()) === tClean)) return true;
    // Corpus concept ID match
    if (v.corpus_concept_id) {
      const cNFC = normalizeNFC(v.corpus_concept_id);
      const cClean = stripAccents(v.corpus_concept_id);
      if (cNFC === tNFC || cClean === tClean) return true;
    }
    return false;
  });
  if (directHit) return directHit;

  // 2. Sovereign Parent match (Specialized child variants inherit base regalia photo)
  if (parent) {
    const parentHit = visualManifest.find((v) => {
      const vNFC = normalizeNFC(v.canonical_name || '');
      const vClean = stripAccents(v.canonical_name || '');
      if (vNFC === pNFC || vClean === pClean) return true;
      if (v.corpus_concept_id && (normalizeNFC(v.corpus_concept_id) === pNFC || stripAccents(v.corpus_concept_id) === pClean)) return true;
      return false;
    });
    if (parentHit) return parentHit;
  }

  // 3. Base root token match (e.g. 'Ìrókẹ́ Eyin Erin' matches 'Ìrókẹ́ Ifá', 'Ọpọ́n Ifá Gbẹ́rọ́' matches 'Ọpọ́n Ifá')
  return visualManifest.find((v) => {
    const vClean = stripAccents(v.canonical_name || '');
    const vParts = vClean.split(/\s+/).filter((w) => w.length > 3);
    const tParts = tClean.split(/\s+/).filter((w) => w.length > 3);
    return vParts.length > 0 && tParts.length > 0 && vParts[0] === tParts[0];
  }) || null;
}

export function hydrateEntityForBento(m, score = 0.992) {
  if (!m) return null;
  const visualHit = findVisualRegaliaHit(m.title || m.details?.title, m);
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
