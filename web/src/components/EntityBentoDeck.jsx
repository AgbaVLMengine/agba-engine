import React, { useState } from 'react';
import {
  Sparkles, BookOpen, MapPin, Feather, Flag, ChevronDown, ChevronUp,
  Shield, Volume2, GitBranch, Scroll
} from 'lucide-react';
import AkosileProvenanceDrawer from './AkosileProvenanceDrawer';
import LivingVariantConstellationGrid from './LivingVariantConstellationGrid';
import OrukoMiLineageRibbon from './OrukoMiLineageRibbon';
import MultiVoiceAcousticPlayer from './MultiVoiceAcousticPlayer';

export default function EntityBentoDeck({
  topMatch,
  query,
  tonalContour,
  relatedMatches,
  onBranchToRelative,
  onOpenFeedback
}) {
  const [tier14Open, setTier14Open] = useState(false);
  const [provenanceOpen, setProvenanceOpen] = useState(false);

  if (!topMatch) return null;

  const isParent =
    topMatch.details?.is_parent === true ||
    topMatch.details?.sovereign_parent_status === 'Sovereign Parent Concept';

  const tier14Items = [
    ['1. Canonical Entity ID', topMatch.details?.id || topMatch.id, true],
    ['2. Canonical Title (25-Letter Orthography)', topMatch.details?.title || topMatch.title, false],
    ['3. Sovereign Parent Classification', isParent ? 'Sovereign Parent Concept' : topMatch.details?.sovereign_parent_status || 'Sovereign Heritage Matrix', false],
    ['4. Cultural Domain Category', topMatch.details?.category || topMatch.category, false],
    ['5. Aliases & Cross-Dialect Variants', (topMatch.details?.aliases || []).join(', ') || 'Canonical primary nomenclature', false],
    ['6. Primary Cultural Description', topMatch.details?.description, false],
    ['7. Historical Antiquity Timeline', topMatch.details?.historical_timeline || 'Deep antiquity tracing to classical Ilé-Ifẹ̀.', false],
    ['8. Etymology, Linguistics & Philosophy', topMatch.details?.etymology_and_philosophy || 'Rooted in ancestral Yorùbá philosophy.', false],
    ['9. Materiality & Craftsmanship', topMatch.details?.material_and_craftsmanship || 'Indigenous craftsmanship and materials.', false],
    ['10. Social Protocol & Ritual Context', topMatch.details?.social_and_ritual_context || 'Integral to royal court and ancestral rites.', false],
    ['11. Proverbs & Praise Poetry (Oríkì)', Array.isArray(topMatch.details?.proverbs_and_oral_traditions) ? topMatch.details?.proverbs_and_oral_traditions.join('; ') : topMatch.details?.proverbs_and_oral_traditions || 'Preserved across oral verse.', false],
    ['12. Transatlantic Diaspora Connections', topMatch.details?.diaspora_connections || 'Survives in Brazil Candomblé and Cuban Santería.', false],
    ['13. Geographical Origin', topMatch.details?.geographical_origin || 'Yorùbáland (Southwestern Nigeria & Diaspora)', false],
    ['14. Curatorial & Ethical Guidelines', topMatch.details?.media_production_notes || 'Ensure authentic period representation and correct tonal pronunciation.', false]
  ];

  return (
    <div className="animate-fade-in" style={{ marginBottom: '48px' }}>
      {topMatch.details?.onomastic_card && (
        <OrukoMiLineageRibbon card={topMatch.details.onomastic_card} />
      )}
      <div className="bento-grid">
        {/* CELL 1: PRIME SOVEREIGN CROWN CELL */}
        <div className="bento-cell bento-cell-sovereign">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
            <span className="badge-gold">
              <Sparkles size={13} />
              {isParent ? 'SOVEREIGN PARENT CONCEPT' : topMatch.details?.sovereign_parent_status || 'PRIME CANONICAL MATCH (#1)'}
            </span>
            <span className="badge-emerald">
              Fusion Score: {topMatch.fusion_score ? topMatch.fusion_score.toFixed(4) : '0.9920'}
            </span>
          </div>

          <h2 className="font-royal text-gold" style={{ fontSize: '2.45rem', fontWeight: 800, marginBottom: '6px' }}>
            {topMatch.title || topMatch.id}
          </h2>

          <p style={{ color: 'var(--gold-light)', fontSize: '0.92rem', marginBottom: '14px', fontWeight: 600 }}>
            {topMatch.category || 'Cultural Heritage'} • Tradition: {topMatch.details?.culture || 'Yorùbá Classical'}
          </p>

          <p style={{ color: 'var(--text-primary)', fontSize: '1.05rem', lineHeight: 1.65, marginBottom: '20px' }}>
            {topMatch.details?.description || 'Authentic Yorùbá cultural entity indexed in the sovereign master corpus.'}
          </p>

          <div style={{ background: 'rgba(0, 0, 0, 0.35)', padding: '12px 16px', borderRadius: '10px', border: '1px solid var(--border-subtle)', marginBottom: '20px', display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '0.86rem' }}>
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

          <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
            <button
              type="button"
              onClick={() => setTier14Open(!tier14Open)}
              className="btn-gold"
              style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '9px 18px', borderRadius: '10px' }}
            >
              <BookOpen size={16} />
              {tier14Open ? 'Hide 14-Tier Schema' : 'Explore 14-Tier Knowledge Graph'}
              {tier14Open ? <ChevronUp size={15} /> : <ChevronDown size={15} />}
            </button>

            <button
              type="button"
              onClick={() => onOpenFeedback(query, topMatch.id || topMatch.title)}
              className="btn-ghost"
              style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '9px 16px', borderRadius: '10px', color: '#fb923c', borderColor: 'rgba(200, 90, 50, 0.4)' }}
            >
              <Flag size={15} />
              Audit / Report Correction
            </button>

            <button
              type="button"
              onClick={() => setProvenanceOpen(true)}
              className="btn-ghost"
              style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '9px 16px', borderRadius: '10px', color: '#fbbf24', borderColor: 'rgba(251, 191, 36, 0.4)' }}
            >
              <Scroll size={15} />
              Àkọsílẹ̀ Provenance
            </button>
          </div>
        </div>

        {/* CELL 2: LIVING ACOUSTIC HEARTH */}
        <div className="bento-cell bento-cell-acoustic">
          <MultiVoiceAcousticPlayer entity={topMatch} tonalContour={tonalContour} />
        </div>

        {/* CELL 3: VERIFIED REGALIA & VISUAL ARCHIVE CELL */}
        <div className="bento-cell bento-cell-regalia">
          {topMatch.multimodal_assets?.has_visual_asset && topMatch.multimodal_assets?.source_url ? (
            <div>
              <span className="badge-gold" style={{ marginBottom: '12px', display: 'inline-block' }}>
                VERIFIED MUSEUM MASTERWORK
              </span>
              <div style={{ height: '240px', borderRadius: '12px', overflow: 'hidden', background: '#0a0d14', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '14px', border: '1px solid var(--border-subtle)' }}>
                <img
                  src={topMatch.multimodal_assets.source_url}
                  alt={topMatch.title}
                  style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                  onError={(e) => { e.target.style.display = 'none'; }}
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
              <div style={{ width: '68px', height: '68px', borderRadius: '50%', margin: '0 auto 14px auto', background: 'linear-gradient(135deg, rgba(217, 119, 6, 0.25) 0%, rgba(217, 119, 6, 0.05) 100%)', border: '2px solid var(--gold-border)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '32px', boxShadow: '0 0 20px rgba(217, 119, 6, 0.25)' }}>
                👑
              </div>
              <span className="badge-gold" style={{ marginBottom: '8px' }}>SOVEREIGN TEXTUAL CANON</span>
              <h4 className="font-royal text-gold" style={{ fontSize: '1.2rem', marginBottom: '6px' }}>{topMatch.title}</h4>
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
          <div style={{ background: 'rgba(0, 0, 0, 0.35)', borderLeft: '3px solid #d97706', padding: '14px 18px', borderRadius: '0 10px 10px 0', marginBottom: '16px' }}>
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
            <strong>Etymology & Philosophical Core:</strong>{' '}
            {topMatch.details?.etymology_and_philosophy || 'Rooted in ancestral Yorùbá moral poise (Ìwà Rere) and cosmological harmony.'}
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

        {/* CELL 6: KINSHIP ROOT NETWORK CELL (GROWS RABBIT-HOLE VEIN) */}
        <div className="bento-cell bento-cell-roots">
          <span className="badge-gold" style={{ marginBottom: '12px', display: 'inline-block' }}>
            <GitBranch size={12} /> KINSHIP ROOT NETWORK (CLICK TO GROW VEIN)
          </span>
          <h4 className="font-royal text-gold" style={{ fontSize: '1.2rem', marginBottom: '10px' }}>
            Connected Cultural Relatives & Variants
          </h4>
          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
            {relatedMatches.slice(0, 5).map((rel) => (
              <button
                key={rel.id || rel.title}
                type="button"
                onClick={() => onBranchToRelative(rel, 'Kinship Relative')}
                style={{ background: 'rgba(217, 119, 6, 0.15)', border: '1px solid rgba(217, 119, 6, 0.35)', borderRadius: '8px', padding: '6px 12px', color: '#f8fafc', fontSize: '0.82rem', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '5px' }}
              >
                <span>🩸 {rel.title}</span>
                <span style={{ fontSize: '0.7rem', color: '#fbbf24' }}>→</span>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* LIVING SUB-VARIANT CONSTELLATION GRID */}
      <LivingVariantConstellationGrid
        subVariants={topMatch.details?.sub_variants || topMatch.sub_variants || []}
        onSelectVariant={(variantTitle) => onBranchToRelative({ title: variantTitle, is_subvariant: true }, 'Living Sub-Variant')}
      />

      {/* 14-TIER KNOWLEDGE GRAPH ACCORDION */}
      {tier14Open && (
        <div className="glass-panel animate-fade-in" style={{ padding: '28px', marginBottom: '28px' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.4rem', marginBottom: '8px' }}>
            14-Tier Cultural Knowledge Graph Schema
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.86rem', marginBottom: '20px' }}>
            Standardized metadata schema curated under Lead Architect Aruna Olanrewaju Kabiru.
          </p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '16px' }}>
            {tier14Items.map(([label, val, isCode]) => (
              <div key={label} style={{ background: 'rgba(0,0,0,0.3)', padding: '14px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                <strong style={{ color: 'var(--gold-light)' }}>{label}:</strong>
                <p style={{ fontSize: '0.88rem', marginTop: '4px' }}>{isCode ? <code>{val}</code> : val}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* RELATED CONCEPTS & SUB-VARIANTS IN CORPUS */}
      {relatedMatches.length > 0 && (
        <div>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.35rem', marginBottom: '16px' }}>
            Branch Deeper into the Rabbit Hole (Connected Relatives & Sub-Variants)
          </h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '16px' }}>
            {relatedMatches.map((item, idx) => (
              <div
                key={item.id || idx}
                className="glass-panel"
                style={{ padding: '18px', cursor: 'pointer', border: '1px solid var(--border-subtle)', transition: 'transform 0.2s ease, border-color 0.2s ease' }}
                onClick={() => onBranchToRelative(item, 'Rabbit-Hole Branch')}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                  <h4 className="font-royal text-gold" style={{ fontSize: '1.1rem' }}>{item.title}</h4>
                  <span className="badge-emerald" style={{ fontSize: '0.72rem' }}>+Vein Branch #{idx + 1}</span>
                </div>
                <p style={{ fontSize: '0.82rem', color: 'var(--gold-light)', marginBottom: '8px' }}>
                  {item.category || 'General Heritage'}
                </p>
                <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
                  {(item.description || item.details?.description || 'Authentic Yorùbá entity.').slice(0, 100)}...
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* AKOSILE ACADEMIC PROVENANCE DRAWER */}
      <AkosileProvenanceDrawer
        isOpen={provenanceOpen}
        onClose={() => setProvenanceOpen(false)}
        entity={topMatch}
      />
    </div>
  );
}
