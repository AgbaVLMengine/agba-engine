import React, { useState } from 'react';
import Navbar from './components/Navbar';
import SearchTab from './components/SearchTab';
import ChatTab from './components/ChatTab';
import TranslateTab from './components/TranslateTab';
import GalleryTab from './components/GalleryTab';
import AdminTab from './components/AdminTab';
import ArchitectureTab from './components/ArchitectureTab';
import FeedbackModal from './components/FeedbackModal';

export default function App() {
  const [activeTab, setActiveTab] = useState('search');
  const [feedbackOpen, setFeedbackOpen] = useState(false);
  const [feedbackTarget, setFeedbackTarget] = useState({ concept: '', entityId: '' });

  // Dynamically resolve API URL: local Vite dev proxy '/api' or direct Cloud Run
  const apiBaseUrl = import.meta.env.VITE_API_URL || 'https://agba-enterprise-api-dgefvzanqq-uc.a.run.app';

  const handleOpenFeedback = (concept, entityId) => {
    setFeedbackTarget({ concept, entityId });
    setFeedbackOpen(true);
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Sticky Navigation */}
      <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Content Area */}
      <main style={{ flex: 1, paddingBottom: '48px' }}>
        {activeTab === 'search' && (
          <SearchTab apiBaseUrl={apiBaseUrl} onOpenFeedback={handleOpenFeedback} />
        )}
        {activeTab === 'chat' && (
          <ChatTab apiBaseUrl={apiBaseUrl} />
        )}
        {activeTab === 'translate' && (
          <TranslateTab apiBaseUrl={apiBaseUrl} />
        )}
        {activeTab === 'gallery' && (
          <GalleryTab />
        )}
        {activeTab === 'admin' && (
          <AdminTab apiBaseUrl={apiBaseUrl} />
        )}
        {activeTab === 'architecture' && (
          <ArchitectureTab />
        )}
      </main>

      {/* Interactive Feedback / Mismatch Reporting Modal */}
      <FeedbackModal
        isOpen={feedbackOpen}
        onClose={() => setFeedbackOpen(false)}
        defaultConcept={feedbackTarget.concept}
        defaultEntityId={feedbackTarget.entityId}
        apiBaseUrl={apiBaseUrl}
      />

      {/* Luxury Footer */}
      <footer style={{
        borderTop: '1px solid var(--border-subtle)',
        background: 'rgba(6, 9, 14, 0.95)',
        padding: '24px 16px',
        textAlign: 'center',
        fontSize: '0.85rem',
        color: 'var(--text-muted)'
      }}>
        <div style={{ maxWidth: '1280px', margin: '0 auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
          <div>
            <strong className="font-royal text-gold" style={{ fontSize: '0.98rem' }}>ÀGBÀ ENGINE</strong> • Cultural Intelligence Framework
          </div>
          <div>
            Lead Architect: <strong style={{ color: 'var(--gold-light)' }}>Aruna Olanrewaju Kabiru</strong> | License: <code>RAIL-Cultural-Heritage-v1.0</code>
          </div>
          <div>
            Powered by <strong style={{ color: '#10b981' }}>Google Cloud Run</strong> & <strong style={{ color: '#38bdf8' }}>Gemini 2.5 Pro/Flash</strong>
          </div>
        </div>
      </footer>
    </div>
  );
}
