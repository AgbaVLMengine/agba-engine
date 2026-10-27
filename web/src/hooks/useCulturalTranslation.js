import { useState, useRef, useCallback } from 'react';
import { restoreDiacriticsAlgorithmic, synthesizeCulturalGloss } from '../utils/yorubaDiacriticsLexicon';

export function useCulturalTranslation(apiBaseUrl) {
  const [activeMode, setActiveMode] = useState('diacritize');

  // Diacritize States
  const [asciiInput, setAsciiInput] = useState('Ogun lakaaye osin imole, eni to ni omi nile ti o fi eje we');
  const [diacritizedOutput, setDiacritizedOutput] = useState('');
  const [diacritizing, setDiacritizing] = useState(false);

  // Cultural Translation States
  const [culturalInput, setCulturalInput] = useState('Èjì Ogbè lori Ọpọ́n Ifá');
  const [culturalResult, setCulturalResult] = useState(null);
  const [translating, setTranslating] = useState(false);

  // Synchronous double-tap lock (Gate 3)
  const busyRef = useRef(false);

  const handleDiacritize = useCallback(async () => {
    const text = asciiInput.trim();
    if (!text || busyRef.current) return;
    busyRef.current = true;
    setDiacritizing(true);
    setDiacritizedOutput('');

    try {
      const res = await fetch(`${apiBaseUrl}/v6/translate/diacritize`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-AGBA-API-KEY': 'agba_studio_dev_key_2026'
        },
        body: JSON.stringify({ text })
      });

      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setDiacritizedOutput(data.diacritized_text || restoreDiacriticsAlgorithmic(asciiInput));
    } catch (err) {
      console.warn('API connection notice, executing local diacritization lexicon:', err);
      setDiacritizedOutput(restoreDiacriticsAlgorithmic(asciiInput));
    } finally {
      setDiacritizing(false);
      busyRef.current = false;
    }
  }, [apiBaseUrl, asciiInput]);

  const handleCulturalTranslate = useCallback(async () => {
    const text = culturalInput.trim();
    if (!text || busyRef.current) return;
    busyRef.current = true;
    setTranslating(true);
    setCulturalResult(null);

    try {
      const res = await fetch(`${apiBaseUrl}/v6/translate/cultural`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-AGBA-API-KEY': 'agba_studio_dev_key_2026'
        },
        body: JSON.stringify({ text })
      });

      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setCulturalResult(data.result || synthesizeCulturalGloss(culturalInput));
    } catch (err) {
      console.warn('API connection notice, executing local cultural gloss synthesis:', err);
      setCulturalResult(synthesizeCulturalGloss(culturalInput));
    } finally {
      setTranslating(false);
      busyRef.current = false;
    }
  }, [apiBaseUrl, culturalInput]);

  return {
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
  };
}
