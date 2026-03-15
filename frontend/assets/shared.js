/* ============================================
   SPENDLY — Shared JavaScript Utilities
   Built by Team Bugg Slayers
   ============================================ */

/* --- Mock Data --- */
const mockTools = [
  { name: 'Salesforce', category: 'CRM', cost: 4200, seats: 45, activeSeats: 38, renewal: '2025-03-15', risk: 'low', dept: 'Sales', logo: 'S' },
  { name: 'Slack', category: 'Communication', cost: 1800, seats: 120, activeSeats: 97, renewal: '2025-04-01', risk: 'low', dept: 'All', logo: 'Sl' },
  { name: 'Figma', category: 'Design', cost: 960, seats: 22, activeSeats: 8, renewal: '2025-02-28', risk: 'critical', dept: 'Design', logo: 'F' },
  { name: 'Sketch', category: 'Design', cost: 720, seats: 12, activeSeats: 3, renewal: '2025-03-10', risk: 'high', dept: 'Design', logo: 'Sk' },
  { name: 'Notion', category: 'Productivity', cost: 480, seats: 60, activeSeats: 41, renewal: '2025-05-01', risk: 'medium', dept: 'All', logo: 'N' },
  { name: 'Loom', category: 'Video', cost: 320, seats: 25, activeSeats: 4, renewal: '2025-02-14', risk: 'critical', dept: 'Marketing', logo: 'L' },
  { name: 'Zoom', category: 'Communication', cost: 2100, seats: 100, activeSeats: 88, renewal: '2025-06-15', risk: 'low', dept: 'All', logo: 'Z' },
  { name: 'HubSpot', category: 'Marketing', cost: 3600, seats: 15, activeSeats: 14, renewal: '2025-07-01', risk: 'low', dept: 'Marketing', logo: 'H' },
  { name: 'Jira', category: 'Dev', cost: 1440, seats: 40, activeSeats: 35, renewal: '2025-08-01', risk: 'low', dept: 'Engineering', logo: 'J' },
  { name: 'GitHub', category: 'Dev', cost: 2880, seats: 50, activeSeats: 47, renewal: '2025-09-01', risk: 'low', dept: 'Engineering', logo: 'G' },
  { name: 'Asana', category: 'Productivity', cost: 540, seats: 30, activeSeats: 18, renewal: '2025-04-15', risk: 'medium', dept: 'Operations', logo: 'A' },
  { name: 'Intercom', category: 'Support', cost: 1200, seats: 10, activeSeats: 9, renewal: '2025-05-20', risk: 'low', dept: 'Support', logo: 'I' },
];

const mockAlerts = [
  { type: 'renewal', severity: 'critical', tool: 'Loom', message: 'Renews in 3 days — 21 inactive seats', waste: 268, time: '2 hours ago' },
  { type: 'unused', severity: 'high', tool: 'Figma', message: '14 seats unused for 45+ days', waste: 512, time: '5 hours ago' },
  { type: 'duplicate', severity: 'high', tool: 'Sketch vs Figma', message: '87% feature overlap detected', waste: 720, time: '1 day ago' },
  { type: 'trial', severity: 'medium', tool: 'Notion AI', message: 'Trial converts Friday — $890/mo', waste: 890, time: '1 day ago' },
  { type: 'unused', severity: 'medium', tool: 'Asana', message: '12 seats unused for 30+ days', waste: 216, time: '2 days ago' },
  { type: 'renewal', severity: 'low', tool: 'Zoom', message: 'Renewal in 45 days — review usage', waste: 0, time: '3 days ago' },
  { type: 'unused', severity: 'critical', tool: 'Salesforce', message: '7 premium seats at $93/mo each unused', waste: 651, time: '4 hours ago' },
  { type: 'duplicate', severity: 'medium', tool: 'Asana vs Notion', message: '62% feature overlap in project management', waste: 324, time: '2 days ago' },
];

const mockSpendByMonth = [
  { month: 'Mar', spend: 18200 }, { month: 'Apr', spend: 19400 },
  { month: 'May', spend: 20100 }, { month: 'Jun', spend: 19800 },
  { month: 'Jul', spend: 21300 }, { month: 'Aug', spend: 20650 },
  { month: 'Sep', spend: 21900 }, { month: 'Oct', spend: 22400 },
  { month: 'Nov', spend: 21800 }, { month: 'Dec', spend: 23100 },
  { month: 'Jan', spend: 22700 }, { month: 'Feb', spend: 20652 },
];

const mockSpendByDept = [
  { dept: 'Engineering', spend: 8420 },
  { dept: 'Sales', spend: 6800 },
  { dept: 'Marketing', spend: 5200 },
  { dept: 'Design', spend: 3400 },
  { dept: 'Operations', spend: 2800 },
  { dept: 'Support', spend: 1900 },
  { dept: 'HR', spend: 1200 },
];

const mockOptimizations = [
  { id: 1, action: 'Cancel Sketch', dept: 'Design', desc: '0 logins in 45 days. 8 paid seats. Annual cost: $2,880.', savings: 2880, tags: ['Unused', 'Design', 'High confidence'], confidence: 96 },
  { id: 2, action: 'Downgrade Figma to Free', dept: 'Design', desc: '14 of 22 seats inactive. Move casual users to free viewer plan.', savings: 4200, tags: ['Underused', 'Design', 'Medium confidence'], confidence: 82 },
  { id: 3, action: 'Cancel Loom Premium', dept: 'Marketing', desc: '21 of 25 seats unused for 60+ days. Switch to free tier.', savings: 3840, tags: ['Unused', 'Video', 'High confidence'], confidence: 94 },
  { id: 4, action: 'Consolidate Slack + Teams', dept: 'All', desc: 'Both communication platforms active. 87% feature overlap.', savings: 8640, tags: ['Duplicate', 'Communication', 'Review needed'], confidence: 78 },
  { id: 5, action: 'Renegotiate Salesforce', dept: 'Sales', desc: 'Contract renewal in 90 days. Market rate is 15% lower.', savings: 7560, tags: ['Renewal', 'CRM', 'High impact'], confidence: 88 },
  { id: 6, action: 'Remove Asana inactive seats', dept: 'Operations', desc: '12 of 30 seats inactive for 30+ days.', savings: 2160, tags: ['Underused', 'Productivity'], confidence: 90 },
  { id: 7, action: 'Switch Zoom to annual billing', dept: 'All', desc: 'Currently on monthly. Annual saves 18%.', savings: 4536, tags: ['Billing', 'Quick win'], confidence: 98 },
  { id: 8, action: 'Cancel Monday.com trial', dept: 'Operations', desc: 'Trial ends in 5 days. Only 2 active users. Already have Asana.', savings: 1920, tags: ['Trial', 'Duplicate'], confidence: 95 },
  { id: 9, action: 'Downgrade HubSpot tier', dept: 'Marketing', desc: 'Using only 40% of Enterprise features. Pro tier sufficient.', savings: 5400, tags: ['Overprovisioned', 'Marketing'], confidence: 85 },
  { id: 10, action: 'Remove GitHub inactive seats', dept: 'Engineering', desc: '3 seats assigned to former contractors.', savings: 1080, tags: ['Unused', 'Dev', 'Quick win'], confidence: 99 },
  { id: 11, action: 'Cancel Adobe Stock', dept: 'Design', desc: 'Only 2 downloads in last quarter. Use free alternatives.', savings: 3600, tags: ['Unused', 'Design'], confidence: 91 },
  { id: 12, action: 'Renegotiate Intercom', dept: 'Support', desc: 'Contract renewal in 60 days. Benchmark shows 20% savings possible.', savings: 2880, tags: ['Renewal', 'Support'], confidence: 83 },
  { id: 13, action: 'Consolidate Notion + Confluence', dept: 'All', desc: 'Both knowledge bases active. 70% content overlap detected.', savings: 4320, tags: ['Duplicate', 'Productivity'], confidence: 76 },
  { id: 14, action: 'Cancel Miro extra seats', dept: 'Design', desc: '8 of 15 seats unused. Reduce to 7 seats.', savings: 1184, tags: ['Underused', 'Design'], confidence: 92 },
];

/* --- Spendly Diamond Logo SVG --- */
const LOGO_SVG = `<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 2L28 12L16 30L4 12L16 2Z" fill="url(#logo-grad)" opacity="0.9"/>
  <path d="M16 2L28 12L16 18L4 12L16 2Z" fill="url(#logo-grad2)" opacity="0.6"/>
  <defs>
    <linearGradient id="logo-grad" x1="4" y1="2" x2="28" y2="30" gradientUnits="userSpaceOnUse">
      <stop stop-color="#6366F1"/><stop offset="1" stop-color="#22D3EE"/>
    </linearGradient>
    <linearGradient id="logo-grad2" x1="4" y1="2" x2="28" y2="18" gradientUnits="userSpaceOnUse">
      <stop stop-color="#818CF8"/><stop offset="1" stop-color="#22D3EE"/>
    </linearGradient>
  </defs>
</svg>`;

/* --- Counter Animation --- */
function animateCounter(el, target, duration = 2000, prefix = '', suffix = '') {
  const start = performance.now();
  const update = (time) => {
    const elapsed = time - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 4);
    const current = Math.floor(eased * target);
    el.textContent = prefix + current.toLocaleString() + suffix;
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}

function setupCounters() {
  const counters = document.querySelectorAll('[data-counter]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.counted) {
        entry.target.dataset.counted = 'true';
        const target = parseFloat(entry.target.dataset.counter);
        const prefix = entry.target.dataset.prefix || '';
        const suffix = entry.target.dataset.suffix || '';
        const duration = parseInt(entry.target.dataset.duration) || 2000;
        animateCounter(entry.target, target, duration, prefix, suffix);
      }
    });
  }, { threshold: 0.3 });
  counters.forEach(c => observer.observe(c));
}

/* --- Magnetic Button Effect --- */
function setupMagneticButtons() {
  document.querySelectorAll('.btn-magnetic').forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.transition = 'transform 0.3s ease';
      btn.style.transform = 'translate(0, 0)';
      setTimeout(() => btn.style.transition = '', 300);
    });
  });
}

/* --- Staggered Entrance Animations --- */
function setupEntranceAnimations() {
  const elements = document.querySelectorAll('.animate-in');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
  elements.forEach(el => observer.observe(el));
}

/* --- Navbar Scroll Effect --- */
function setupNavbarScroll() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
}

/* --- Mobile Menu Toggle --- */
function setupMobileMenu() {
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (!hamburger || !mobileMenu) return;
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  });
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
}

/* --- Chart.js Defaults --- */
function setupChartDefaults() {
  if (typeof Chart === 'undefined') return;
  Chart.defaults.color = '#94A3B8';
  Chart.defaults.font.family = "'Outfit', sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.plugins.legend.display = false;
  Chart.defaults.scale.grid = { color: 'rgba(0,0,0,0.05)', drawBorder: false };
  Chart.defaults.scale.border = { display: false };
  Chart.defaults.elements.line.tension = 0.4;
  Chart.defaults.elements.line.borderWidth = 2;
  Chart.defaults.elements.point.radius = 0;
  Chart.defaults.elements.point.hoverRadius = 6;
  Chart.defaults.elements.point.hoverBackgroundColor = '#6366F1';
  Chart.defaults.elements.point.hoverBorderColor = '#fff';
  Chart.defaults.elements.point.hoverBorderWidth = 2;
  Chart.defaults.plugins.tooltip = {
    ...Chart.defaults.plugins.tooltip,
    backgroundColor: 'rgba(255,255,255,0.95)',
    titleColor: '#0F1117',
    bodyColor: '#3D3D3D',
    borderColor: 'rgba(0,0,0,0.08)',
    borderWidth: 1,
    cornerRadius: 8,
    padding: 12,
    titleFont: { family: "'Outfit', sans-serif", size: 13, weight: 600 },
    bodyFont: { family: "'Outfit', sans-serif", size: 12 },
  };
}

/* --- Component HTML Generators Removed --- */
/* (Navbar, Footer, Sidebar are handled natively by trialspendly) */

/* --- Tool Logo Generator (Premium Pastel Colors) --- */
function getToolColor(name) {
  const colors = {
    'Salesforce': { bg: '#E0F2FE', text: '#0284C7' },
    'Slack': { bg: '#FCE7F3', text: '#BE185D' },
    'Figma': { bg: '#FFEDD5', text: '#C2410C' },
    'Sketch': { bg: '#FEF3C7', text: '#B45309' },
    'Notion': { bg: '#F1F5F9', text: '#334155' },
    'Loom': { bg: '#EEF2FF', text: '#4338CA' },
    'Zoom': { bg: '#DBEAFE', text: '#1D4ED8' },
    'HubSpot': { bg: '#FFEDD5', text: '#C2410C' },
    'Jira': { bg: '#E0F2FE', text: '#0369A1' },
    'GitHub': { bg: '#F1F5F9', text: '#0F172A' },
    'Asana': { bg: '#FEE2E2', text: '#B91C1C' },
    'Intercom': { bg: '#E0E7FF', text: '#4338CA' },
    'Microsoft Teams': { bg: '#EDE9FE', text: '#6D28D9' },
    'Monday.com': { bg: '#FCE7F3', text: '#BE185D' },
  };
  return colors[name] || { bg: '#EEF2FF', text: '#3730A3' };
}

function generateToolLogo(tool) {
  const color = getToolColor(tool.name);
  return `<div style="width:40px;height:40px;border-radius:10px;background:${color.bg};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;letter-spacing:0.5px;color:${color.text};flex-shrink:0;">${tool.logo || tool.name.charAt(0)}</div>`;
}

/* --- Sidebar Toggle --- */
function setupSidebarToggle() {
  const toggle = document.getElementById('sidebarToggle');
  const sidebar = document.querySelector('.sidebar');
  if (toggle && sidebar) {
    toggle.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
    });
  }
}

/* --- Risk Badge --- */
function getRiskBadge(risk) {
  const map = {
    'low': '<span class="badge badge--success">Low</span>',
    'medium': '<span class="badge badge--warning">Medium</span>',
    'high': '<span class="badge badge--warning" style="background:rgba(245,158,11,0.25)">High</span>',
    'critical': '<span class="badge badge--danger">Critical</span>',
  };
  return map[risk] || '';
}

/* --- Category Colors --- */
function getCategoryColor(cat) {
  const map = {
    'CRM': '#00A1E0', 'Communication': '#4A154B', 'Design': '#F24E1E',
    'Productivity': '#10B981', 'Video': '#625DF5', 'Marketing': '#FF7A59',
    'Dev': '#0052CC', 'Support': '#1F8DED',
  };
  return map[cat] || '#6366F1';
}

/* --- Init Everything --- */
function initSpendly() {
  setupCounters();
  setupMagneticButtons();
  setupEntranceAnimations();
  setupNavbarScroll();
  setupMobileMenu();
  setupSidebarToggle();
  setupChartDefaults();
  // Init Lucide icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
}

document.addEventListener('DOMContentLoaded', initSpendly);
