/**
 * App entry point — renders SupportForm and StatusChecker.
 */
import React from 'react';
import SupportForm from './components/SupportForm';
import StatusChecker from './components/StatusChecker';

export default function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>TechCorp Support</h1>
        <p>24/7 AI-powered customer success assistant</p>
      </header>

      <main className="glass-card">
        <section>
          <SupportForm />
        </section>

        <section className="status-checker">
          <StatusChecker />
        </section>
      </main>

      <footer style={{ textAlign: 'center', marginTop: '40px', color: 'var(--text-secondary)', fontSize: '14px' }}>
        &copy; 2026 TechCorp Digital FTE. All rights reserved.
      </footer>
    </div>
  );
}
