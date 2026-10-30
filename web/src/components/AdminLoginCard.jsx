import React from 'react';
import { Lock, Unlock } from 'lucide-react';

export default function AdminLoginCard({ passcode, setPasscode, loginError, onLogin }) {
  return (
    <div style={{ maxWidth: '540px', margin: '40px auto', padding: '0 16px' }}>
      <div className="glass-panel-gold" style={{ padding: '36px', textAlign: 'center' }}>
        <div
          style={{
            width: '56px',
            height: '56px',
            borderRadius: '50%',
            background: 'var(--gold-dim)',
            border: '1px solid var(--gold-border)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            margin: '0 auto 16px auto'
          }}
        >
          <Lock size={26} color="#d4af37" />
        </div>

        <h2 className="font-royal text-gold" style={{ fontSize: '1.7rem', marginBottom: '8px' }}>
          Lead Architect Authentication
        </h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '24px' }}>
          Protected Human-in-the-Loop governance portal. Enter your security passcode or master token to inspect failure contexts and authorize batch updates.
        </p>

        <form onSubmit={onLogin} style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
          <input
            type="password"
            placeholder="Enter Architect Passcode..."
            value={passcode}
            onChange={(e) => setPasscode(e.target.value)}
            style={{
              width: '100%',
              padding: '12px 16px',
              borderRadius: '8px',
              background: 'rgba(0,0,0,0.5)',
              border: '1px solid var(--gold-border)',
              color: 'var(--text-primary)',
              fontSize: '1rem',
              outline: 'none',
              textAlign: 'center',
              letterSpacing: '2px'
            }}
          />

          {loginError && (
            <div style={{ color: '#ef4444', fontSize: '0.85rem' }}>
              {loginError}
            </div>
          )}

          <button type="submit" className="btn-gold" style={{ width: '100%', padding: '12px' }}>
            <Unlock size={18} /> Authenticate Access
          </button>
        </form>
      </div>
    </div>
  );
}
