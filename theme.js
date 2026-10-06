// Apply the saved choice before rendering, including when opening the HTML directly.
(() => {
  const key = 'aayvu-marketing-theme';
  const root = document.documentElement;
  let saved = 'light';
  try { saved = localStorage.getItem(key) || 'light'; } catch (_) {}

  function syncEmbeddedTheme(theme) {
    document.querySelectorAll('.early-access-frame').forEach(frame => {
      try { frame.contentWindow.postMessage({ type: 'theme', value: theme }, '*'); } catch (_) {}
    });
  }

  function apply(theme) {
    const dark = theme === 'dark';
    root.dataset.theme = dark ? 'dark' : 'light';
    syncEmbeddedTheme(dark ? 'dark' : 'light');
    document.querySelectorAll('.theme-toggle').forEach(button => {
      const label = dark ? 'Switch to light mode' : 'Switch to dark mode';
      button.setAttribute('aria-label', label);
      button.title = label;
    });
  }

  apply(saved);
  document.addEventListener('DOMContentLoaded', () => {
    apply(root.dataset.theme);
    document.querySelectorAll('.theme-toggle').forEach(button => {
      button.addEventListener('click', () => {
        const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
        apply(theme);
        try { localStorage.setItem(key, theme); } catch (_) {}
      });
    });
  });
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) apply(event.newValue);
  });
})();
