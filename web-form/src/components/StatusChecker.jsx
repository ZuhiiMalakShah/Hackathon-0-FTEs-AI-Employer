/**
 * Ticket status checker — input ticket ID, fetch and display status.
 */
import React, { useState } from 'react';
import { getTicketStatus } from '../services/api';

export default function StatusChecker() {
  const [ticketId, setTicketId] = useState('');
  const [ticket, setTicket] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleCheck = async (e) => {
    e.preventDefault();
    const trimmed = ticketId.trim();
    if (!trimmed) {
      setError('Please enter a ticket ID');
      return;
    }

    setLoading(true);
    setError('');
    setTicket(null);

    try {
      const data = await getTicketStatus(trimmed);
      setTicket(data);
    } catch (err) {
      setError(err.message || 'Failed to fetch ticket status');
    } finally {
      setLoading(false);
    }
  };

  const statusColors = {
    open: '#3182ce',
    processing: '#d69e2e',
    resolved: '#38a169',
    escalated: '#e53e3e',
    closed: '#718096',
  };

  return (
    <div>
      <h3 style={{ fontSize: '20px', fontWeight: 600, marginBottom: '16px', color: 'var(--text-primary)' }}>
        Track Your Request
      </h3>

      <form onSubmit={handleCheck} className="status-grid">
        <input
          type="text"
          value={ticketId}
          onChange={(e) => { setTicketId(e.target.value); setError(''); }}
          placeholder="Enter Ticket ID (e.g., TKT-0001)"
          className="input"
          style={{ flex: 1 }}
        />
        <button
          type="submit"
          disabled={loading}
          className="btn-primary"
          style={{ padding: '12px 24px', width: 'auto' }}
        >
          {loading ? 'Checking...' : 'Check Status'}
        </button>
      </form>

      {error && (
        <p role="alert" className="error-text" style={{ marginBottom: '16px' }}>{error}</p>
      )}

      {ticket && (
        <div className="response-card" style={{ background: 'rgba(15, 23, 42, 0.4)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
            <span style={{ fontSize: '18px', fontWeight: 700, color: 'var(--accent-primary)' }}>{ticket.ticket_id}</span>
            <span className={`badge status-${ticket.status}`}>
              {ticket.status}
            </span>
          </div>
          <p style={{ fontSize: '15px', color: 'var(--text-primary)', marginBottom: '8px' }}>
            <strong>Subject:</strong> {ticket.subject}
          </p>
          <p style={{ fontSize: '13px', color: 'var(--text-secondary)', marginBottom: '16px' }}>
            Category: {ticket.category} | Priority: {ticket.priority} | Channel: {ticket.source_channel}
          </p>

          {ticket.responses && ticket.responses.length > 0 && (
            <div style={{ marginTop: '20px', borderTop: '1px solid var(--border-light)', paddingTop: '20px' }}>
              <p style={{ fontSize: '14px', fontWeight: 600, marginBottom: '12px', color: 'var(--text-primary)' }}>AI Assistant Responses:</p>
              {ticket.responses.map((r, i) => (
                <div key={i} className="response-card" style={{ marginBottom: '12px', borderLeft: '3px solid var(--accent-primary)' }}>
                  <p style={{ color: 'var(--text-primary)' }}>{r.content}</p>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '11px', marginTop: '8px' }}>
                    {new Date(r.created_at).toLocaleString()} via {r.channel}
                  </p>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
