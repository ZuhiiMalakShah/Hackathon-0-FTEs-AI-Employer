/**
 * Reusable form field component with label, error display, and required indicator.
 */
import React from 'react';

export default function FormField({
  label,
  name,
  type = 'text',
  value,
  onChange,
  onBlur,
  error,
  required = false,
  placeholder = '',
  options = null,
  rows = null,
}) {
  const inputId = `field-${name}`;
  const hasError = Boolean(error);

  const baseStyle = {
    width: '100%',
    padding: '8px 12px',
    border: `1px solid ${hasError ? '#e53e3e' : '#d1d5db'}`,
    borderRadius: '6px',
    fontSize: '14px',
    outline: 'none',
    boxSizing: 'border-box',
  };

  const renderInput = () => {
    const className = `${rows ? 'textarea' : options ? 'select' : 'input'} ${hasError ? 'error' : ''}`;

    if (options) {
      return (
        <select
          id={inputId}
          name={name}
          value={value}
          onChange={onChange}
          onBlur={onBlur}
          className={className}
          aria-invalid={hasError}
          aria-describedby={hasError ? `${inputId}-error` : undefined}
        >
          <option value="">Select {label.toLowerCase()}...</option>
          {options.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      );
    }

    if (rows) {
      return (
        <textarea
          id={inputId}
          name={name}
          value={value}
          onChange={onChange}
          onBlur={onBlur}
          placeholder={placeholder}
          rows={rows}
          className={className}
          aria-invalid={hasError}
          aria-describedby={hasError ? `${inputId}-error` : undefined}
        />
      );
    }

    return (
      <input
        id={inputId}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        onBlur={onBlur}
        placeholder={placeholder}
        className={className}
        aria-invalid={hasError}
        aria-describedby={hasError ? `${inputId}-error` : undefined}
      />
    );
  };

  return (
    <div className="form-group">
      <label htmlFor={inputId} className="label">
        {label}
        {required && <span style={{ color: 'var(--status-escalated)', marginLeft: '4px' }}>*</span>}
      </label>
      {renderInput()}
      {hasError && (
        <p id={`${inputId}-error`} role="alert" className="error-text">
          {error}
        </p>
      )}
    </div>
  );
}
