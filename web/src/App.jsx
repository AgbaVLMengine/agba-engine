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

  // Dynamically resolve API URL: local port 8000 or production Cloud Run
  const apiBaseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

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

      {/* Luxury Footer (Clean Single Line) */}
      <footer style={{
        borderTop: '1px solid var(--border-subtle)',
        background: 'rgba(6, 9, 14, 0.95)',
        padding: '24px 16px',
        textAlign: 'center',
        fontSize: '0.92rem'
      }}>
        <div style={{ maxWidth: '1280px', margin: '0 auto' }}>
          <strong className="font-royal text-gold" style={{ fontSize: '1.05rem', letterSpacing: '0.04em' }}>
            ÀGBÀ ENGINE
          </strong>
          {' '}•{' '}
          <span style={{ color: 'var(--text-secondary)' }}>
            Cultural Intelligence Framework
          </span>
        </div>
      </footer>
    </div>
  );
}
