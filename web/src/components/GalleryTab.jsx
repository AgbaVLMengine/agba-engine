import React, { useState } from 'react';
import { Search, MapPin, Eye, ExternalLink, X, Landmark, Compass, Award } from 'lucide-react';
import visualManifest from '../data/agba_unified_visual_regalia_manifest.json';

export default function GalleryTab() {
  const [selectedMuseum, setSelectedMuseum] = useState('All Repositories');
  const [filterText, setFilterText] = useState('');
  const [activeModalItem, setActiveModalItem] = useState(null);

  // Extract unique museums
  const museums = ['All Repositories', ...new Set(visualManifest.map(i => i.current_custodial_repository).filter(Boolean))];

  // Filter items
  const filteredItems = visualManifest.filter((item) => {
    const matchesMuseum = selectedMuseum === 'All Repositories' || item.current_custodial_repository === selectedMuseum;
    const searchTarget = `${item.canonical_name || ''} ${item.canonical_title_full || ''} ${item.indigenous_place_of_origin || ''} ${item.museum_archival_title || ''}`.toLowerCase();
    const matchesSearch = !filterText || searchTarget.includes(filterText.toLowerCase());
    return matchesMuseum && matchesSearch;
  });

  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* Gallery Header */}
      <div className="glass-panel-gold" style={{ padding: '30px', marginBottom: '28px', textAlign: 'center' }}>
        <span className="badge-gold" style={{ marginBottom: '8px' }}>52 VERIFIED CULTURAL MASTERWORKS</span>
        <h2 className="font-royal text-gold" style={{ fontSize: '2.1rem', marginBottom: '8px', fontWeight: 800 }}>
          Museum Regalia & Provenance Gallery
        </h2>
        <p style={{ color: 'var(--text-secondary)', maxWidth: '750px', margin: '0 auto 20px auto', fontSize: '0.96rem' }}>
          Explore curated sacred Yoruba crowns, divination vessels, and ceremonial apparel preserved across the world’s leading museums and sovereign cultural vaults.
        </p>

        {/* Filter & Search Bar */}
        <div style={{ display: 'flex', gap: '12px', justifyContent: 'center', flexWrap: 'wrap', maxWidth: '780px', margin: '0 auto' }}>
          <div style={{ flex: 1, minWidth: '240px', position: 'relative' }}>
            <input
              type="text"
              value={filterText}
              onChange={(e) => setFilterText(e.target.value)}
              placeholder="Search by artifact name, origin, or materials..."
              style={{
                width: '100%',
                padding: '11px 16px',
                borderRadius: '8px',
                background: 'rgba(0,0,0,0.4)',
                border: '1px solid var(--gold-border)',
                color: 'var(--text-primary)',
                outline: 'none'
              }}
            />
          </div>

          <select
            value={selectedMuseum}
            onChange={(e) => setSelectedMuseum(e.target.value)}
            style={{
              padding: '11px 16px',
              borderRadius: '8px',
              background: 'var(--bg-elevated)',
              border: '1px solid var(--border-subtle)',
              color: 'var(--gold-light)',
              fontWeight: 600,
              cursor: 'pointer'
            }}
          >
            {museums.map(m => (
              <option key={m} value={m}>{m}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Grid of Verified Masterworks */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(290px, 1fr))',
        gap: '22px',
        marginBottom: '40px'
      }}>
        {filteredItems.map((item, idx) => (
          <div
            key={item.filename || idx}
            className="glass-panel"
            style={{
              overflow: 'hidden',
              display: 'flex',
              flexDirection: 'column',
              transition: 'transform 0.25s ease, box-shadow 0.25s ease',
              cursor: 'pointer',
              border: '1px solid var(--border-subtle)'
            }}
            onClick={() => setActiveModalItem(item)}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'translateY(-4px)';
              e.currentTarget.style.boxShadow = '0 12px 28px rgba(212, 175, 55, 0.15)';
              e.currentTarget.style.borderColor = 'var(--gold-border)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'translateY(0)';
              e.currentTarget.style.boxShadow = 'none';
              e.currentTarget.style.borderColor = 'var(--border-subtle)';
            }}
          >
            {/* Image Thumbnail */}
            <div style={{
              height: '210px',
              background: '#0a0d14',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              position: 'relative',
              overflow: 'hidden'
            }}>
              {item.source_url ? (
                <img
                  src={item.source_url}
                  alt={item.canonical_name}
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                  loading="lazy"
                  onError={(e) => {
                    e.target.style.display = 'none';
                    e.target.parentNode.innerHTML = '<div style="color:#d4af37; font-size:42px;">👑</div>';
                  }}
                />
              ) : (
                <div style={{ fontSize: '42px' }}>👑</div>
              )}
              <div style={{
                position: 'absolute',
                bottom: '10px',
                right: '10px',
                background: 'rgba(0,0,0,0.7)',
                padding: '4px 10px',
                borderRadius: '6px',
                fontSize: '0.72rem',
                color: 'var(--gold-light)',
                backdropFilter: 'blur(4px)'
              }}>
                Inspect Provenance
              </div>
            </div>

            {/* Details */}
            <div style={{ padding: '18px', flex: 1, display: 'flex', flexDirection: 'column' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                <h3 className="font-royal text-gold" style={{ fontSize: '1.15rem', lineHeight: 1.25 }}>
                  {item.canonical_name}
                </h3>
              </div>

              <p style={{ fontSize: '0.82rem', color: 'var(--text-muted)', marginBottom: '10px' }}>
                {item.museum_archival_title}
              </p>

              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                <MapPin size={14} color="#d4af37" />
                <span style={{ color: 'var(--gold-light)', fontWeight: 600 }}>{item.indigenous_place_of_origin}</span>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 'auto', paddingTop: '10px', borderTop: '1px solid var(--border-subtle)' }}>
                <Landmark size={13} />
                <span>{item.current_custodial_repository}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Modal Inspector Drawer */}
      {activeModalItem && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.85)',
          backdropFilter: 'blur(10px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 100,
          padding: '24px'
        }}>
          <div className="glass-panel-gold animate-fade-in" style={{
            maxWidth: '860px',
            width: '100%',
            maxHeight: '90vh',
            overflowY: 'auto',
            padding: '32px',
            position: 'relative'
          }}>
            <button
              onClick={() => setActiveModalItem(null)}
              style={{
                position: 'absolute',
                top: '20px',
                right: '20px',
                background: 'none',
                border: 'none',
                color: 'var(--text-muted)',
                cursor: 'pointer'
              }}
            >
              <X size={24} />
            </button>

            <span className="badge-gold" style={{ marginBottom: '10px' }}>VERIFIED MUSEUM MASTERWORK</span>
            <h2 className="font-royal text-gold" style={{ fontSize: '1.8rem', marginBottom: '4px' }}>
              {activeModalItem.canonical_title_full || activeModalItem.canonical_name}
            </h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginBottom: '20px' }}>
              Archival Catalog Title: <strong>{activeModalItem.museum_archival_title}</strong> | Accession: <code>{activeModalItem.accession_number}</code>
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.2fr', gap: '24px', marginBottom: '24px' }}>
              {/* Image Preview */}
              <div style={{
                borderRadius: '10px',
                overflow: 'hidden',
                background: '#07090e',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                maxHeight: '340px',
                border: '1px solid var(--border-subtle)'
              }}>
                {activeModalItem.source_url ? (
                  <img
                    src={activeModalItem.source_url}
                    alt={activeModalItem.canonical_name}
                    style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                  />
                ) : (
                  <div style={{ fontSize: '64px' }}>👑</div>
                )}
              </div>

              {/* Provenance Attributes Table */}
              <div style={{ background: 'rgba(0,0,0,0.3)', padding: '18px', borderRadius: '10px', fontSize: '0.88rem' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                  <tbody>
                    <tr style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                      <td style={{ padding: '8px 0', color: 'var(--text-muted)', width: '40%' }}>Indigenous Origin:</td>
                      <td style={{ padding: '8px 0', color: '#34d399', fontWeight: 600 }}>{activeModalItem.indigenous_place_of_origin}</td>
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                      <td style={{ padding: '8px 0', color: 'var(--text-muted)' }}>Custodial Museum:</td>
                      <td style={{ padding: '8px 0', fontWeight: 600 }}>{activeModalItem.current_custodial_repository}</td>
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                      <td style={{ padding: '8px 0', color: 'var(--text-muted)' }}>Creation Epoch:</td>
                      <td style={{ padding: '8px 0' }}>{activeModalItem.creation_epoch}</td>
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                      <td style={{ padding: '8px 0', color: 'var(--text-muted)' }}>Master Artisan / Guild:</td>
                      <td style={{ padding: '8px 0' }}>{activeModalItem.master_artisan_or_guild}</td>
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                      <td style={{ padding: '8px 0', color: 'var(--text-muted)' }}>Materials:</td>
                      <td style={{ padding: '8px 0' }}>{activeModalItem.medium_materials}</td>
                    </tr>
                    <tr>
                      <td style={{ padding: '8px 0', color: 'var(--text-muted)' }}>Public License:</td>
                      <td style={{ padding: '8px 0' }}>{activeModalItem.license || 'Open Educational Archive'}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* Deep Description */}
            <div style={{ background: 'rgba(212, 175, 55, 0.05)', borderLeft: '4px solid var(--gold-primary)', padding: '16px', borderRadius: '4px', marginBottom: '16px' }}>
              <h4 style={{ color: 'var(--gold-light)', marginBottom: '6px' }}>Corpus Deep Description</h4>
              <p style={{ fontSize: '0.92rem', lineHeight: 1.6, color: 'var(--text-primary)' }}>
                {activeModalItem.corpus_deep_description}
              </p>
            </div>

            {/* Sacred Semiotics */}
            <div style={{ background: 'rgba(16, 185, 129, 0.05)', borderLeft: '4px solid #10b981', padding: '16px', borderRadius: '4px', marginBottom: '20px' }}>
              <h4 style={{ color: '#86efac', marginBottom: '6px' }}>Philosophical Context & Sacred Semiotics</h4>
              <p style={{ fontSize: '0.92rem', lineHeight: 1.6, color: 'var(--text-primary)' }}>
                {activeModalItem.philosophical_context}
              </p>
            </div>

            {activeModalItem.source_url && (
              <a
                href={activeModalItem.source_url}
                target="_blank"
                rel="noopener noreferrer"
                className="btn-gold"
                style={{ textDecoration: 'none' }}
              >
                <span>View on Museum Archival Catalog</span>
                <ExternalLink size={16} />
              </a>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
