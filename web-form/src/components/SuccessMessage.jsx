/**
 * Post-submission success confirmation — displays ticket ID and next steps.
 */
import React from 'react';

export default function SuccessMessage({ ticketId, onSubmitAnother }) {
  return (
    <div className="success-container">
      <span className="success-icon">&#10003;</span>
      <h2 style={{ fontSize: '28px', fontWeight: 700, marginBottom: '16px', color: 'var(--text-primary)' }}>
        Request Received
      </h2>
      <p style={{ fontSize: '16px', color: 'var(--text-secondary)', marginBottom: '32px' }}>
        Your support ticket has been created successfully. Our autonomous AI agent is processing your request.
      </p>

      <div className="ticket-badge">
        <p style={{ fontSize: '12px', color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '8px' }}>
          Ticket Reference
        </p>
        <p className="ticket-id">
          {ticketId}
        </p>
      </div>

      <div style={{ marginTop: '32px' }}>
        <button
          onClick={onSubmitAnother}
          className="btn-primary"
          style={{ width: 'auto', padding: '12px 32px', background: 'transparent', border: '1px solid var(--border-light)' }}
        >
          Submit Another Request
        </button>
      </div>
    </div>
  );
}
