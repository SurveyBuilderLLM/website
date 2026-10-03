// Hover opens a dropdown; clicking pins it open until dismissed.
(() => {
  const dropdowns = Array.from(document.querySelectorAll('.nav .drop')).map(drop => ({
    drop,
    trigger: drop.querySelector('.drop-trigger'),
    menu: drop.querySelector('.drop-menu'),
    timer: null,
    pinned: false,
  }));

  function close(item) {
    clearTimeout(item.timer);
    item.pinned = false;
    item.menu.hidden = true;
    item.trigger.setAttribute('aria-expanded', 'false');
  }

  function open(item) {
    clearTimeout(item.timer);
    dropdowns.forEach(other => { if (other !== item) close(other); });
    item.menu.hidden = false;
    item.trigger.setAttribute('aria-expanded', 'true');
  }

  dropdowns.forEach(item => {
    item.drop.addEventListener('mouseenter', () => open(item));
    item.drop.addEventListener('mouseleave', () => {
      clearTimeout(item.timer);
      // Allow diagonal movement and brief excursions beyond the menu edge.
      item.timer = setTimeout(() => {
        if (!item.pinned && !item.drop.contains(document.activeElement)) close(item);
      }, 300);
    });
    item.trigger.addEventListener('click', () => {
      if (item.pinned) close(item);
      else {
        open(item);
        item.pinned = true;
      }
    });
    item.trigger.addEventListener('keydown', event => {
      if (event.key === 'ArrowDown') {
        event.preventDefault();
        open(item);
        item.menu.querySelector('a').focus();
      }
    });
    item.drop.addEventListener('focusout', event => {
      if (!item.drop.contains(event.relatedTarget)) close(item);
    });
    item.drop.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        event.preventDefault();
        close(item);
        item.trigger.focus();
      }
    });
  });

  document.addEventListener('click', event => {
    dropdowns.forEach(item => {
      if (!item.drop.contains(event.target)) close(item);
    });
  });
})();

// Mobile menu: full-width panel under the header, body scroll locked while open.
(() => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.getElementById('primary-links');
  const nav = document.querySelector('.nav');
  if (!toggle || !links || !nav) return;

  function set(open) {
    if (open) document.documentElement.style.setProperty('--nav-h', Math.round(nav.getBoundingClientRect().bottom) + 'px');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    links.classList.toggle('mobile-open', open);
    document.body.classList.toggle('nav-open', open);
  }

  toggle.addEventListener('click', () => set(toggle.getAttribute('aria-expanded') !== 'true'));
  links.addEventListener('click', event => { if (event.target.closest('a')) set(false); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && links.classList.contains('mobile-open')) { set(false); toggle.focus(); }
  });
  window.matchMedia('(min-width: 961px)').addEventListener('change', event => { if (event.matches) set(false); });
})();
