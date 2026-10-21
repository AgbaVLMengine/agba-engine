import React, { useState } from 'react';
import {
  ShieldCheck, CheckCircle2, Globe, Lock, ExternalLink, Code2,
  BookOpen, Landmark, ChevronDown, ChevronUp, Volume2, Scale
} from 'lucide-react';

const FULL_24_SOURCES = [
  '1. Rev. Samuel Johnson (1921) — The History of the Yorubas (Ọ̀yọ́ dynastic statecraft, military titles & pre-colonial governance)',
  '2. Prof. Wándé Abímbọ́lá (1975) — Sixteen Great Poems of Ifá (UNESCO-recognized Odù Ifá liturgical corpus)',
  '3. Prof. Wándé Abímbọ́lá (1976) — Ifá: An Exposition of Ifá Literary Corpus (Structural mechanics of 256 Odù)',
  '4. Prof. Rowland Abíọ́dún (2014) — Yoruba Art and Language: Seeking the African in African Art (Àṣẹ, Ìwà, Ojú-Inú)',
  '5. Prof. Babátúndé Lawal (1996) — The Gẹ̀lẹ̀dẹ́ Spectacle: Art, Gender, and Social Harmony in an African Culture',
  '6. Prof. Babátúndé Lawal (2001) — Awòrán: Representing the Self inenga & Yorùbá Classical Statuary',
  '7. Prof. William Bascom (1969) — Ifa Divination: Communication Between Gods and Men in West Africa',
  '8. Prof. William Bascom (1980) — Sixteen Cowries: Yoruba Divination from Africa to the New World (Ẹẹ́rìndínlógún)',
  '9. Prof. Robert Farris Thompson (1983) — Flash of the Spirit: African & Afro-American Art and Philosophy',
  '10. Prof. Henry John Drewal & Margaret Thompson Drewal (1983) — Gẹ̀lẹ̀dẹ́: Art and Female Power Among the Yoruba',
  '11. Henry John Drewal, John Pemberton III & Rowland Abíọ́dún (1989) — Yoruba: Nine Centuries of African Art and Thought',
  '12. Prof. Jacob Kẹ́hìndé Olúpọ̀nà (2011) — City of 201 Gods: Ilé-Ifẹ̀ in Time, Space, and the Imagination',
  '13. Prof. Karin Barber (1991) — I Could Speak Until Tomorrow: Oriki, Women, and the Past in a Yoruba Town',
  '14. Prof. Oyekan Owomoyela (2005) — Yoruba Proverbs (Comprehensive paremiological lexicon & English translations)',
  '15. Pierre Fatumbi Verger (1995) — Ewé: The Use of Plants in Yoruba Society (Ethnobotanical & liturgical taxonomy)',
  '16. Prof. Toyin Falola & Matt D. Childs (2004) — The Yoruba Diaspora in the Atlantic World',
  '17. Prof. Akinwumi Isola & Bade Ajuwon — Classical Yorùbá Oral Poetics (Ìjálá, Rárà, Ewì & Ẹkún Ìyàwó)',
  '18. Prof. Akin Euba (1990) — Yoruba Drumming: The Dùndún Tradition (Acoustic surrogate speech & tonal glissando)',
  '19. The Metropolitan Museum of Art (New York) — Open Access CC0 Collection (Ọ̀wọ̀ Ivories, Àgéré Ifá & Ògbóni Regalia)',
  '20. The Cleveland Museum of Art (CMA) — Open Access CC0 Collection (Adéńlá, Ọpọ́n Ifá, Ẹdan Ògbóni & Oríkògbófo)',
  '21. The Art Institute of Chicago (AIC) — Open Access CC0 Collection (Òpó Ògògá by Ọlọ́wẹ̀ of Ìsẹ̀, Arugba Ifá & Àpótí Ọba)',
  '22. Smithsonian National Museum of African Art (NMAfA) — Open Access Collection (Ìrókẹ́ Ifá & Ẹ̀gbà Ògbóni)',
  '23. The British Museum & Victoria and Albert Museum (V&A) — Classical Ilé-Ifẹ̀ Terracotta & Textile Reference Archives',
  '24. National Commission for Museums and Monuments (NCMM Nigeria) & Royal Palace Archives of Ilé-Ifẹ̀, Ọ̀yọ́ & Ọ̀wọ̀'
];

export default function ArchitectureTab() {
  const [showFullBib, setShowFullBib] = useState(false);

  return (
    <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 16px' }}>
      {/* Overview Banner */}
      <div className="glass-panel-gold" style={{ padding: '32px', marginBottom: '28px', textAlign: 'center' }}>
        <span className="badge-gold" style={{ marginBottom: '8px' }}>ARCHITECTURE & ETHICAL GOVERNANCE</span>
        <h2 className="font-royal text-gold" style={{ fontSize: '2.1rem', marginBottom: '8px', fontWeight: 800 }}>
          Àgbà Engine Operational Matrix
        </h2>
        <p style={{ color: 'var(--text-secondary)', maxWidth: '780px', margin: '0 auto', fontSize: '0.98rem' }}>
          Engineered by <strong>Àrùnà Ọlànrewájú Kábírù</strong>. Cross-modal retrieval framework designed to index indigenous knowledge, tonal orthographies, and cultural regalia without sub-token drift or Unicode degradation.
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

        {/* Pillar 3: Enterprise Hybrid Cloud & Sovereign Global Edge CDN */}
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid #10b981' }}>
          <h3 className="font-royal text-gold" style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Globe size={20} /> Enterprise Hybrid Cloud & Sovereign Global Edge CDN
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '14px' }}>
            Deployed on high-concurrency containerized microservices with sub-10ms response latency, pre-baked neural embedding weights, multi-region failover, and global edge caching for museum-grade reliability.
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

        {/* Collapsible Full 24-Source Master Bibliography Register */}
        <div style={{ marginTop: '24px', borderTop: '1px solid var(--border-subtle)', paddingTop: '18px' }}>
          <button
            type="button"
            onClick={() => setShowFullBib(!showFullBib)}
            className="btn-gold"
            style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '9px 18px', borderRadius: '10px', fontSize: '0.88rem' }}
          >
            <BookOpen size={15} />
            {showFullBib ? 'Hide Full 24-Source Canonical Bibliography' : 'Inspect All 24 Canonical Bibliographic & Archival Sources'}
            {showFullBib ? <ChevronUp size={15} /> : <ChevronDown size={15} />}
          </button>

          {showFullBib && (
            <div
              className="animate-fade-in"
              style={{
                marginTop: '16px',
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))',
                gap: '10px',
                background: 'rgba(0,0,0,0.35)',
                padding: '18px',
                borderRadius: '10px',
                border: '1px solid var(--border-subtle)'
              }}
            >
              {FULL_24_SOURCES.map((src) => (
                <div key={src} style={{ fontSize: '0.83rem', color: 'var(--text-secondary)', lineHeight: 1.45, padding: '6px 8px', borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                  {src}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Invariants & Ethical Standards */}
      <div className="glass-panel" style={{ padding: '28px', marginBottom: '36px' }}>
        <h3 className="font-royal text-gold" style={{ fontSize: '1.4rem', marginBottom: '16px' }}>
          🏛️ Supreme Corpus Invariants & Ethical Governance
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
                Zero unverified images or logic updates enter the master corpus autonomously. All candidate additions require Lead Architect (`Àrùnà Ọlànrewájú Kábírù`) signoff.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <Scale color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>Sacred Cosmology Reverence & Awo Exclusion:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                Strictly excludes restricted initiatory secrets (<em>Ọ̀rọ̀ Awo</em>) from public datasets and upholds sovereign reverence across all Òrìṣà and ancestral lineages.
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <ShieldCheck color="#10b981" size={20} style={{ flexShrink: 0, marginTop: '2px' }} />
            <div>
              <strong style={{ color: 'var(--text-primary)' }}>RAIL-Cultural-Heritage-v1.0 License:</strong>
              <p style={{ color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                Protects indigenous intellectual property and sacred regalia against uncredited commercial exploitation or synthetic model distillation.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
