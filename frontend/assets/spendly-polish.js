/**
 * spendly-polish.js
 * Drop in /assets/spendly-polish.js
 * Add to every HTML file before </body>:
 * <script src="/assets/spendly-polish.js"></script>
 *
 * Handles:
 * — Navbar scroll state
 * — Hamburger menu
 * — Scroll reveal animations
 * — Counter animations
 * — Active nav link
 * — Page transition
 * — Sidebar active state (app pages)
 */

(function () {
  'use strict';

  /* ─────────────────────────────────────────
     1. NAVBAR — scroll state + hamburger
  ───────────────────────────────────────── */
  const navbar = document.querySelector('nav, #navbar, .navbar');
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');

  if (navbar) {
    // Scroll state
    const updateNav = () => {
      navbar.classList.toggle('scrolled', window.scrollY > 16);
    };
    window.addEventListener('scroll', updateNav, { passive: true });
    updateNav();
  }

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen);

      // Animate hamburger lines → X
      const spans = hamburger.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!navbar.contains(e.target) && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        hamburger.querySelectorAll('span').forEach(s => {
          s.style.transform = '';
          s.style.opacity = '';
        });
      }
    });
  }


  /* ─────────────────────────────────────────
     2. ACTIVE NAV LINK — based on current URL
  ───────────────────────────────────────── */
  const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.nav-links a, .sidebar-link').forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkPath = href.replace(/\.html$/, '').replace(/\/$/, '') || '/';
    if (currentPath === linkPath || (linkPath !== '/' && currentPath.startsWith(linkPath))) {
      link.classList.add('active');
    }
  });


  /* ─────────────────────────────────────────
     3. SCROLL REVEAL — .reveal elements
  ───────────────────────────────────────── */
  const revealEls = document.querySelectorAll('.reveal, .stagger-children');

  if (revealEls.length) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    revealEls.forEach(el => { if (el && el instanceof Element) revealObserver.observe(el); });
  }


  /* ─────────────────────────────────────────
     4. COUNTER ANIMATION
     Usage: <span data-counter data-target="247830" data-prefix="$" data-suffix="+">
  ───────────────────────────────────────── */
  function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
  }

  function animateCounter(el) {
    const target  = parseFloat(el.dataset.target) || 0;
    const prefix  = el.dataset.prefix  || '';
    const suffix  = el.dataset.suffix  || '';
    const decimals = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;
    const duration = parseInt(el.dataset.duration) || 1800;
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed  = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased    = easeOutQuart(progress);
      const value    = eased * target;

      let formatted;
      if (decimals > 0) {
        formatted = value.toFixed(decimals);
      } else {
        formatted = Math.floor(value).toLocaleString();
      }

      el.textContent = prefix + formatted + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        // Final exact value
        el.textContent = prefix + (decimals > 0 ? target.toFixed(decimals) : target.toLocaleString()) + suffix;
      }
    }

    requestAnimationFrame(update);
  }

  const counterEls = document.querySelectorAll('[data-counter]');
  if (counterEls.length) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    counterEls.forEach(el => { if (el && el instanceof Element) counterObserver.observe(el); });
  }


  /* ─────────────────────────────────────────
     5. PAGE TRANSITIONS — smooth exit
  ───────────────────────────────────────── */
  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href');
    // Only internal links, not anchors or external
    if (!href || href.startsWith('#') || href.startsWith('http') ||
        href.startsWith('mailto') || link.target === '_blank') return;

    link.addEventListener('click', (e) => {
      e.preventDefault();
      document.body.style.opacity = '0';
      document.body.style.transition = 'opacity 200ms ease';
      setTimeout(() => { window.location.href = href; }, 200);
    });
  });

  // Fade in on page load
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 300ms ease';
  window.addEventListener('load', () => {
    requestAnimationFrame(() => {
      document.body.style.opacity = '1';
    });
  });


  /* ─────────────────────────────────────────
     6. HOVER LIFT — cards
  ───────────────────────────────────────── */
  document.querySelectorAll('.card, .kpi-card, .article-card').forEach(card => {
    if (!card.style.transition) {
      card.style.transition = 'transform 250ms ease, box-shadow 250ms ease, border-color 250ms ease';
    }
  });


  /* ─────────────────────────────────────────
     7. SPEND BAR CHART — hover highlight
  ───────────────────────────────────────── */
  document.querySelectorAll('.spend-bars').forEach(chart => {
    const bars = chart.querySelectorAll('.spend-bar');
    bars.forEach(bar => {
      bar.addEventListener('mouseenter', () => {
        bars.forEach(b => b.classList.remove('active'));
        bar.classList.add('active');
      });
    });
  });


  /* ─────────────────────────────────────────
     8. SKELETON → REAL CONTENT
     Add class="skeleton-wrap" to any section
     that loads async data — remove class when loaded
  ───────────────────────────────────────── */
  window.spendly = {
    // Call this when async data is ready to remove skeletons
    resolveSkeletons: (container) => {
      if (!container) return;
      container.querySelectorAll('.skeleton').forEach(el => {
        el.style.transition = 'opacity 300ms ease';
        el.style.opacity = '0';
        setTimeout(() => el.remove(), 300);
      });
    }
  };


  /* ─────────────────────────────────────────
     9. TOOLTIP — data-tooltip attribute
     Usage: <button data-tooltip="Coming soon">
  ───────────────────────────────────────── */
  let tooltip = null;

  document.querySelectorAll('[data-tooltip]').forEach(el => {
    el.addEventListener('mouseenter', (e) => {
      tooltip = document.createElement('div');
      tooltip.textContent = el.dataset.tooltip;
      Object.assign(tooltip.style, {
        position: 'fixed',
        background: '#0C0C0A',
        color: '#F5F4EF',
        fontSize: '12px',
        fontFamily: 'var(--font-sans)',
        padding: '5px 10px',
        borderRadius: '6px',
        pointerEvents: 'none',
        zIndex: '9999',
        whiteSpace: 'nowrap',
        opacity: '0',
        transition: 'opacity 150ms ease',
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)'
      });
      document.body.appendChild(tooltip);

      const rect = el.getBoundingClientRect();
      tooltip.style.left = rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + 'px';
      tooltip.style.top  = rect.top - tooltip.offsetHeight - 8 + 'px';

      requestAnimationFrame(() => { tooltip.style.opacity = '1'; });
    });

    el.addEventListener('mouseleave', () => {
      if (tooltip) {
        tooltip.style.opacity = '0';
        setTimeout(() => { tooltip?.remove(); tooltip = null; }, 150);
      }
    });
  });


  /* ─────────────────────────────────────────
     10. KEYBOARD ACCESSIBILITY
  ───────────────────────────────────────── */
  document.addEventListener('keydown', (e) => {
    // Close mobile menu on Escape
    if (e.key === 'Escape' && navLinks?.classList.contains('open')) {
      navLinks.classList.remove('open');
    }
  });

})();
