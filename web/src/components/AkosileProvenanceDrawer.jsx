import React, { useEffect } from 'react';
import { X, BookOpen, Shield, Library, ExternalLink, Scroll, Award } from 'lucide-react';

export default function AkosileProvenanceDrawer({ isOpen, onClose, entity }) {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen || !entity) return null;

  const title = entity.title || entity.id || 'Canonical Entity';
  const category = entity.category || entity.details?.category || 'Yorùbá Classical';
  const provenanceText =
    entity.details?.provenance_and_citations ||
    entity.provenance_and_citations ||
    entity.details?.academic_citations;

  const defaultScholarlyCitations = [
    { author: 'Rev. Samuel Johnson', year: '1921', work: 'The History of the Yorubas: From the Earliest Times to the Beginning of the British Protectorate' },
    { author: 'Prof. Wándé Abímbọ́lá', year: '1975/1976', work: 'Sixteen Great Poems of Ifá / Ifá Divination Poetry' },
    { author: 'Prof. Rowland Abiodun', year: '2014', work: 'Yoruba Art and Language: Seeking the African in African Art' },
    { author: 'Prof. Babatunde Lawal', year: '1996', work: 'The Gẹ̀lẹ̀dẹ́ Spectacle: Art, Gender, and Social Harmony in an African Culture' },
    { author: 'Pierre Fatumbi Verger', year: '1995', work: 'Ewé: The Use of Plants in Yoruba Society' }
  ];

  const accessionNumber = entity.multimodal_assets?.accession_number;
  const custodialVault = entity.multimodal_assets?.current_custodial_repository;

  return (
    <div style={{ position: 'fixed', inset: 0, zIndex: 9999, display: 'flex', justifyContent: 'flex-end', background: 'rgba(5, 7, 12, 0.75)', backdropFilter: 'blur(6px)' }}>
      <div onClick={onClose} style={{ position: 'absolute', inset: 0 }} />
      <div
        className="animate-fade-in"
        style={{
          position: 'relative',
          width: '100%',
          maxWidth: '520px',
          height: '100%',
          background: '#0d111a',
          borderLeft: '1px solid rgba(212, 175, 55, 0.35)',
          boxShadow: '-10px 0 40px rgba(0, 0, 0, 0.85)',
          overflowY: 'auto',
          padding: '28px 24px',
          display: 'flex',
          flexDirection: 'column',
          gap: '22px'
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', borderBottom: '1px solid rgba(212, 175, 55, 0.2)', paddingBottom: '16px' }}>
          <div>
            <span style={{ fontSize: '0.74rem', letterSpacing: '0.08em', color: '#d4af37', textTransform: 'uppercase', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Scroll size={13} /> ÀKỌSÍLẸ̀ PROVENANCE ARCHIVE
            </span>
            <h3 className="font-royal text-gold" style={{ fontSize: '1.6rem', marginTop: '4px', marginBottom: '2px' }}>
              {title}
            </h3>
            <p style={{ fontSize: '0.82rem', color: '#94a3b8' }}>Domain: {category}</p>
          </div>
          <button
            type="button"
            onClick={onClose}
            style={{ background: 'rgba(255, 255, 255, 0.05)', border: '1px solid rgba(255, 255, 255, 0.1)', color: '#f8fafc', borderRadius: '8px', padding: '6px', cursor: 'pointer' }}
          >
            <X size={18} />
          </button>
        </div>

        {/* SECTION 1: SCHOLARLY CITATIONS */}
        <div style={{ background: 'rgba(212, 175, 55, 0.04)', border: '1px solid rgba(212, 175, 55, 0.2)', borderRadius: '12px', padding: '16px' }}>
          <h4 style={{ fontSize: '0.9rem', color: '#fbbf24', display: 'flex', alignItems: 'center', gap: '7px', marginBottom: '10px' }}>
            <BookOpen size={15} /> Academic Citations & Master Bibliography
          </h4>
          {provenanceText ? (
            <p style={{ fontSize: '0.86rem', color: '#e2e8f0', lineHeight: 1.6, fontStyle: 'italic' }}>
              {provenanceText}
            </p>
          ) : (
            <ul style={{ paddingLeft: '18px', margin: 0, fontSize: '0.82rem', color: '#cbd5e1', lineHeight: 1.55 }}>
              {defaultScholarlyCitations.map((c, i) => (
                <li key={i} style={{ marginBottom: '6px' }}>
                  <strong style={{ color: '#fbbf24' }}>{c.author}</strong> ({c.year}). <em>{c.work}</em>.
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* SECTION 2: MUSEUM ACCESSION & CUSTODIAL DATA */}
        {(accessionNumber || custodialVault) && (
          <div style={{ background: 'rgba(30, 41, 59, 0.45)', border: '1px solid rgba(148, 163, 184, 0.2)', borderRadius: '12px', padding: '16px' }}>
            <h4 style={{ fontSize: '0.9rem', color: '#e2e8f0', display: 'flex', alignItems: 'center', gap: '7px', marginBottom: '10px' }}>
              <Library size={15} color="#d4af37" /> Museum Accession & Physical Provenance
            </h4>
            <div style={{ fontSize: '0.84rem', color: '#94a3b8', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {custodialVault && <p><strong>Custodial Repository:</strong> {custodialVault}</p>}
              {accessionNumber && <p><strong>Accession Identifier:</strong> <code style={{ color: '#fbbf24' }}>{accessionNumber}</code></p>}
            </div>
          </div>
        )}

        {/* SECTION 3: LEGAL SOVEREIGNTY & AWO SANCTITY */}
        <div style={{ background: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(212, 175, 55, 0.25)', borderRadius: '12px', padding: '16px' }}>
          <h4 style={{ fontSize: '0.9rem', color: '#d4af37', display: 'flex', alignItems: 'center', gap: '7px', marginBottom: '8px' }}>
            <Shield size={15} /> Cultural Heritage Licensing & Ethics
          </h4>
          <p style={{ fontSize: '0.82rem', color: '#94a3b8', lineHeight: 1.5, marginBottom: '10px' }}>
            Governed under <strong>RAIL-Cultural-Heritage-v1.0</strong> (Responsible AI License). Prohibits cultural distortion, offensive commercialization, and deep-fake degradation.
          </p>
          <div style={{ fontSize: '0.78rem', color: '#f59e0b', background: 'rgba(245, 158, 11, 0.08)', padding: '8px 12px', borderRadius: '8px', borderLeft: '3px solid #f59e0b' }}>
            <strong>Awo Sacred Exclusion:</strong> Preserves sacred boundaries; restricted initiatory rites remain confidential to traditional custodial lineages.
          </div>
        </div>
      </div>
    </div>
  );
}
