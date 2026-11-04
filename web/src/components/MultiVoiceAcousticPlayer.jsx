import React, { useState, useRef, useEffect } from 'react';
import { Volume2, Play, Pause, Sparkles, Music, Mic, Crown } from 'lucide-react';

const CUSTODIAL_VOICES = [
  { id: 'yemi', icon: Mic, label: 'Ẹlẹ́rìí Àmì Ohùn', custodian: 'Auntie Yẹmí', role: 'Tone Witness (Spoken)', dur: '1.2s' },
  { id: 'dundun', icon: Volume2, label: 'Ohùn Ayélujára Dùndún', custodian: 'Baba Sẹ́fíù Adégbílù', role: 'Talking Drum Syllables', dur: '1.0s' },
  { id: 'aluko', icon: Sparkles, label: 'Ìdáhùn Ọmọbìnrin', custodian: 'Àlùkọ̀ / Granddaughter', role: 'Harmonic Call & Response', dur: '1.4s' },
  { id: 'oriki', icon: Crown, label: 'Oríkì Ọba Onítìrẹ́', custodian: 'Royal Father', role: 'Imperial Lineage Cadence', dur: '4.8s' },
  { id: 'ensemble', icon: Music, label: 'Àkójọpọ̀ Ilù Àtijọ́', custodian: 'Classical Guild Ensemble', role: 'Dùndún & Gùdùgùdù', dur: '6.2s' },
];

export default function MultiVoiceAcousticPlayer({ entity, tonalContour = [] }) {
  const [activeVoice, setActiveVoice] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef(null);

  // Eradicate ghost audio on unmount or entity change
  useEffect(() => {
    return () => {
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current.src = '';
      }
    };
  }, [entity]);

  const togglePlayback = (voice) => {
    if (activeVoice === voice.id && isPlaying) {
      if (audioRef.current) audioRef.current.pause();
      setIsPlaying(false);
      return;
    }

    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.src = '';
    }

    // Public Sanctuary Stream route (Immutable Edge Cache + No Key Required)
    const streamUrl = `/v6/audio/stream/${encodeURIComponent(entity?.id || entity?.title || 'Ade')}_${voice.id}`;
    const audio = new Audio(streamUrl);
    audioRef.current = audio;

    audio.onended = () => { setIsPlaying(false); setActiveVoice(null); };
    audio.onerror = () => {
      // Graceful fallback for entities without master audio stem
      setIsPlaying(false);
      setActiveVoice(null);
    };

    audio.play().then(() => {
      setActiveVoice(voice.id);
      setIsPlaying(true);
    }).catch(() => {
      setIsPlaying(false);
      setActiveVoice(null);
    });
  };

  return (
    <div className="multi-voice-acoustic-player" style={{ width: '100%' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
        <span className="badge-gold" style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
          <Volume2 size={13} /> LIVING ACOUSTIC HEARTH
        </span>
        <span style={{ fontSize: '0.72rem', color: '#10b981', display: 'flex', alignItems: 'center', gap: '4px', fontWeight: 600 }}>
          ● 100% Free Public Sanctuary
        </span>
      </div>

      <h4 className="font-royal text-gold" style={{ fontSize: '1.2rem', marginBottom: '6px' }}>
        {entity?.title || 'Tonal Phonetics & Drum Mimicry'}
      </h4>
      <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: '14px', lineHeight: 1.4 }}>
        Multi-generational acoustic constellation honoring the spoken tone and sacred talking drum counterpart.
      </p>

      {/* 25-Letter Tonal Pitch Contour Ribbon */}
      {tonalContour.length > 0 && (
        <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', marginBottom: '14px' }}>
          {tonalContour.map((t, idx) => (
            <div key={idx} style={{ background: 'rgba(0, 0, 0, 0.45)', border: '1px solid var(--border-subtle)', borderRadius: '6px', padding: '4px 8px', textAlign: 'center', minWidth: '32px' }}>
              <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc' }}>{t.char}</div>
              <div style={{ fontSize: '0.65rem', color: '#fbbf24' }}>{t.arrow} {t.pitch}</div>
            </div>
          ))}
        </div>
      )}

      {/* 5 Custodial Stems — WCAG Touch Targets >= 44px */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '10px' }}>
        {CUSTODIAL_VOICES.map((v) => {
          const Icon = v.icon;
          const active = activeVoice === v.id && isPlaying;
          return (
            <button
              key={v.id}
              type="button"
              onClick={() => togglePlayback(v)}
              aria-label={`Play ${v.label}`}
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                minHeight: '44px',
                padding: '8px 12px',
                borderRadius: '10px',
                border: active ? '1.5px solid #d97706' : '1px solid var(--border-subtle)',
                background: active ? 'rgba(217, 119, 6, 0.18)' : 'rgba(0, 0, 0, 0.35)',
                color: active ? '#fbbf24' : '#e2e8f0',
                cursor: 'pointer',
                textAlign: 'left',
                transition: 'all 0.15s ease'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{ width: '28px', height: '28px', borderRadius: '50%', background: active ? '#d97706' : 'rgba(255,255,255,0.06)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: active ? '#000' : '#fbbf24' }}>
                  {active ? <Pause size={14} /> : <Icon size={14} />}
                </div>
                <div>
                  <div style={{ fontSize: '0.86rem', fontWeight: 600 }}>{v.label}</div>
                  <div style={{ fontSize: '0.70rem', color: 'var(--text-muted)' }}>{v.custodian} • {v.role}</div>
                </div>
              </div>
              <span style={{ fontSize: '0.72rem', color: '#fbbf24', background: 'rgba(251,191,36,0.1)', padding: '2px 6px', borderRadius: '6px' }}>
                {active ? 'Playing...' : v.dur}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
