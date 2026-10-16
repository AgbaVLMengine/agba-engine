import React from 'react';
import { Cpu, ShieldCheck, CheckCircle2, Database, Globe, Lock, ExternalLink, Code2, BookOpen, Landmark, Sparkles, Layers, FileCode } from 'lucide-react';

export default function ArchitectureTab() {
  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* Overview Banner */}
      <div className="glass-panel-gold" style={{ padding: '32px', marginBottom: '28px', textAlign: 'center' }}>
        <span className="badge-gold" style={{ marginBottom: '8px' }}>ARCHITECTURE & ETHICAL GOVERNANCE</span>
        <h2 className="font-royal text-gold" style={{ fontSize: '2.1rem', marginBottom: '8px', fontWeight: 800 }}>
          Àgbà Engine Operational Matrix
        </h2>
        <p style={{ color: 'var(--text-secondary)', maxWidth: '780px', margin: '0 auto', fontSize: '0.98rem' }}>
          Engineered by <strong>Aruna Olanrewaju Kabiru</strong>. Cross-modal retrieval framework designed to index indigenous knowledge, tonal orthographies, and cultural regalia without sub-token drift or Unicode degradation.
        </p>
      </div>

      {/* Grid of Core Pillars */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: '22px', marginBottom: '32px' }}>
        {/* Pillar 1: Orthography */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid var(--gold-primary)' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Code2 size={20} /> 25-Letter Yorùbá Primacy
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Standard AI LLMs strip under-dots (`ẹ`, `ọ`, `ṣ`) and tonal accents (`á`, `à`), corrupting tonal semantic meaning. Àgbà Engine enforces dual-retrieval parity: exact tonal match (`1.0000`) and ASCII folding fallback (`0.9600`).
          </p>
          <div style={{ background: 'rgba(0,0,0,0.3)', padding: '10px 14px', borderRadius: '6px', fontSize: '0.85rem' }}>
            <code style={{ color: 'var(--gold-light)' }}>Agbádá • Adé Ààrẹ • Ìyùn • Èwù Ìlèkè • Gọ̀mbọ́ • Ọpọ́n Ifá</code>
          </div>
        </div>

        {/* Pillar 2: Architectural Tier Separation */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid #3b82f6' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Lock size={20} /> Tiered Access Separation
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Under sovereign cultural governance, the <strong>Open Source Web Client</strong> is strictly limited to Text & Vision. All <strong>143 Authentic Audio Tokens</strong> (human spoken vocalizations & talking drum glissando) are withheld from client web bundles and reserved exclusively for authorized Enterprise/Institutional API access.
          </p>
          <div style={{ display: 'flex', gap: '8px' }}>
            <span className="badge-emerald">Web: Text & Vision Only</span>
            <span className="badge-gold">API: Tri-Modal Gated</span>
          </div>
        </div>

        {/* Pillar 3: Zero-Cost Cloud Run Infrastructure */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid #10b981' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Globe size={20} /> Zero-Cost Cloud Run & Netlify
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Deployed on Google Cloud Run serverless containers (`min-instances=0`), incurring <strong>$0.00/month</strong> when idle under Google Cloud's Always Free Tier. Frontend served via Netlify Edge CDN with automatic `dev` and `production` branch CI/CD.
          </p>
          <a
            href="https://agba-enterprise-api-dgefvzanqq-uc.a.run.app/health"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-ghost"
            style={{ fontSize: '0.82rem', padding: '6px 12px', textDecoration: 'none' }}
          >
            Inspect Cloud Run Health Probe <ExternalLink size={14} />
          </a>
        </div>
      </div>


      {/* Canonical Sources & Master Bibliography */}
      <div className="glass-panel" style={{ padding: '32px', marginBottom: '36px', borderTop: '3px solid var(--gold-primary)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
          <BookOpen color="var(--gold-primary)" size={26} />
          <div>
            <h3 className="font-royal text-gold" style={{ fontSize: '1.5rem', margin: 0, fontWeight: 700 }}>
              Canonical Sources & Master Bibliography
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', margin: '4px 0 0 0' }}>
              The epistemological, ethnographical, and archival bedrock grounding every entity in the Àgbà Engine master corpus.
            </p>
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px', marginTop: '24px' }}>
          {/* Category 1: Academic Literature */}
          <div style={{ background: 'rgba(0,0,0,0.25)', padding: '20px', borderRadius: '10px', border: '1px solid rgba(212, 175, 55, 0.2)' }}>
            <h4 style={{ color: 'var(--gold-light)', fontSize: '1.05rem', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <BookOpen size={16} /> Classical Scholarly Literature
            </h4>
            <ul style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: '0.86rem', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Rev. Samuel Johnson (1921)</strong><br />
                <em>The History of the Yorubas</em> — Ọ̀yọ́ dynastic lineage, imperial warfare, and administrative statecraft.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Prof. Wande Abimbola (1975, 1976)</strong><br />
                <em>Sixteen Great Poems of Ifá</em> & <em>An Exposition of Ifá Literary Corpus</em> — Sacred Odù Ifá poetic meters and ethical philosophy.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Prof. Rowland Abiodun (2014)</strong><br />
                <em>Yoruba Art and Language</em> — Master aesthetic framework: <em>Ojú-Inú</em>, <em>Àṣẹ</em>, <em>Ìwà</em>, and visual semiotics.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Prof. Babatunde Lawal (1996, 2001)</strong><br />
                <em>The Gẹ̀lẹ̀dẹ́ Spectacle</em> & <em>Awòrán: Representing the Self</em> — Mask symbology, maternal power (*Àwọn Ìyá Wa*), and scarifications.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Prof. William Bascom (1969, 1980)</strong><br />
                <em>Ifa Divination</em> & <em>Sixteen Cowries</em> — Mechanics of Ọ̀pẹ̀lẹ̀, Ikin, and Ẹẹ́rìndínlógún divination.
              </li>
            </ul>
          </div>

          {/* Category 2: Museum Archives */}
          <div style={{ background: 'rgba(0,0,0,0.25)', padding: '20px', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
            <h4 style={{ color: '#60a5fa', fontSize: '1.05rem', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Landmark size={16} /> Museum Collections & Curatorial Vaults
            </h4>
            <ul style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: '0.86rem', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>The Metropolitan Museum of Art (The Met)</strong><br />
                Classical <em>Adé Beaded Crowns</em>, <em>Ọpọ́n Ifá</em>, <em>Ẹrùkẹ̀</em>, and sacred commemorative sculpture.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>The British Museum</strong><br />
                12th–15th century classical <em>Ilé-Ifẹ̀ copper-alloy heads</em>, <em>Obalufon copper mask</em>, and Ọ̀wọ̀ ivories.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Cleveland Museum of Art & Art Institute of Chicago</strong><br />
                Masterpieces carved by <em>Ọlọ́wẹ̀ of Ìsẹ̀</em>, ceremonial beaded royal boots (<em>Bàtà Ìlèkè</em>), and <em>Edan Ògbóni</em> bronzes.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>Smithsonian National Museum of African Art</strong><br />
                Textile archives: wild-silk <em>Sányán</em>, camwood <em>Àlàárì</em>, indigo <em>Ẹtù</em>, and resist-dyed <em>Àdírẹ Ẹlẹ́kọ</em>.
              </li>
              <li>
                <strong style={{ color: 'var(--text-primary)' }}>NCMM National Museum Lagos & Palace Shrines</strong><br />
                Indigenous royal regalia, ancestral thrones, and living ceremonial instruments across Ifẹ̀, Ọ̀yọ́, and Ọ̀wọ̀.
              </li>
            </ul>
          </div>

          </div>
      </div>

{/* Invariants & Ethical Standards */}
      <div className="glass-panel" style={{ padding: '28px', marginBottom: '36px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.4rem', marginBottom: '16px' }}>
          🏛️ Supreme Corpus Invariants & MLOps Governance
        </h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px', fontSize: '0.92rem' }}>
          <div style={{ display: 'flex', gap: '10px' }}>
            <CheckCircle2 color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>Supreme Corpus Primacy:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                All visual and acoustic assets are strictly subordinated to Yorùbá canonical ground truth. Museum descriptions yield to native historical records.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <CheckCircle2 color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>Mandatory Human-in-the-Loop Gate:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                Zero unverified images or logic updates enter the master corpus autonomously. All candidate additions require Lead Architect signoff.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <CheckCircle2 color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>RAIL Cultural Heritage License:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                Protects indigenous intellectual property and sacred regalia against uncredited commercial exploitation or synthetic distillation.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
