// Apply the saved choice before rendering, including when opening the HTML directly.
(() => {
  const key = 'aayvu-marketing-theme';
  const root = document.documentElement;
  let saved = 'light';
  try { saved = localStorage.getItem(key) || 'light'; } catch (_) {}

  function syncEmbeddedTheme(theme) {
    document.querySelectorAll('.early-access-frame').forEach(frame => {
      try { frame.contentWindow.postMessage({ type: 'aayvu:embed-theme', value: theme }, window.location.origin); } catch (_) {}
    });
  }

  function setupEmbeddedFrames() {
    const surveyOrigin = window.location.origin;
    const frames = Array.from(document.querySelectorAll('.early-access-frame'));
    if (!frames.length) return;

    window.addEventListener('message', event => {
      if (event.origin !== surveyOrigin) return;
      const frame = frames.find(candidate => candidate.contentWindow === event.source);
      if (event.data?.type === 'aayvu:embed-ready') {
        syncEmbeddedTheme(root.dataset.theme);
        return;
      }
      if (event.data?.type !== 'aayvu:embed-resize') return;
      const height = Number(event.data.height);
      if (!frame || !Number.isFinite(height) || height < 320) return;
      frame.style.height = `${Math.ceil(height)}px`;
    });

    frames.forEach(frame => {
      frame.addEventListener('load', () => {
        try {
          frame.contentWindow.postMessage({ type: 'aayvu:embed-measure' }, surveyOrigin);
          frame.contentWindow.postMessage({ type: 'aayvu:embed-theme', value: root.dataset.theme }, surveyOrigin);
        } catch (_) {}
      });
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
    setupEmbeddedFrames();
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
