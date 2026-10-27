import React from 'react';
import { Wand2, BookOpen } from 'lucide-react';
import { useCulturalTranslation } from '../hooks/useCulturalTranslation';
import DiacritizerCard from './DiacritizerCard';
import CulturalGlossCard from './CulturalGlossCard';

export default function TranslateTab({ apiBaseUrl }) {
  const {
    activeMode,
    setActiveMode,
    asciiInput,
    setAsciiInput,
    diacritizedOutput,
    diacritizing,
    handleDiacritize,
    culturalInput,
    setCulturalInput,
    culturalResult,
    translating,
    handleCulturalTranslate
  } = useCulturalTranslation(apiBaseUrl);

  return (
    <div style={{ maxWidth: '1080px', margin: '0 auto', padding: '0 16px' }}>
      {/* Mode Switcher */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: '12px', marginBottom: '32px' }}>
        <button
          onClick={() => setActiveMode('diacritize')}
          className={activeMode === 'diacritize' ? 'btn-gold' : 'btn-ghost'}
          style={{ padding: '10px 24px', borderRadius: '24px', display: 'flex', alignItems: 'center', gap: '8px' }}
        >
          <Wand2 size={16} />
          Smart ASCII-to-Diacritic Restorer
        </button>

        <button
          onClick={() => setActiveMode('cultural')}
          className={activeMode === 'cultural' ? 'btn-gold' : 'btn-ghost'}
          style={{ padding: '10px 24px', borderRadius: '24px', display: 'flex', alignItems: 'center', gap: '8px' }}
        >
          <BookOpen size={16} />
          Cultural Translation & Deep Glossing
        </button>
      </div>

      {/* VIEW 1: SMART ASCII-TO-DIACRITIC RESTORER */}
      {activeMode === 'diacritize' && (
        <DiacritizerCard
          asciiInput={asciiInput}
          setAsciiInput={setAsciiInput}
          diacritizedOutput={diacritizedOutput}
          diacritizing={diacritizing}
          onDiacritize={handleDiacritize}
        />
      )}

      {/* VIEW 2: CULTURAL TRANSLATION & DEEP GLOSSING */}
      {activeMode === 'cultural' && (
        <CulturalGlossCard
          culturalInput={culturalInput}
          setCulturalInput={setCulturalInput}
          culturalResult={culturalResult}
          translating={translating}
          onCulturalTranslate={handleCulturalTranslate}
        />
      )}
    </div>
  );
}
