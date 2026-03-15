import os
import re

dir_path = r'c:\trialspendly\spendly'
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

mobile_css = """
@media (max-width: 768px) {

  /* Nav — collapse to hamburger */
  .nav-links { display: none; }
  .nav-links.open { display: flex; flex-direction: column; 
    position: fixed; top: 64px; left: 0; right: 0; 
    background: white; padding: 24px; 
    border-bottom: 1px solid #E5E7EB; z-index: 99; gap: 16px; }
  .hamburger { display: flex !important; cursor: pointer; 
    flex-direction: column; gap: 5px; }
  .hamburger span { display: block; width: 22px; height: 2px; 
    background: #0F1117; border-radius: 2px; 
    transition: all 0.2s; }

  /* Hero — stack vertically */
  .hero { flex-direction: column !important; 
    text-align: center !important; padding: 80px 24px 48px !important; }
  .hero-visual { display: none !important; }
  .hero-content { max-width: 100% !important; }

  /* Typography — scale down */
  h1 { font-size: clamp(32px, 8vw, 52px) !important; }
  h2 { font-size: clamp(24px, 6vw, 36px) !important; }

  /* All grid layouts — single column */
  .cards-grid, 
  .features-grid, 
  .articles-grid,
  .stats-grid,
  .pricing-grid,
  .pillars-grid { grid-template-columns: 1fr !important; }

  /* Dashboard layout — stack sidebar on top */
  .app-layout { flex-direction: column !important; }
  .sidebar { width: 100% !important; height: auto !important; 
    position: relative !important; 
    border-right: none !important; 
    border-bottom: 1px solid #E5E7EB !important; 
    padding: 16px !important; }
  .sidebar-nav { display: flex; flex-wrap: wrap; 
    gap: 8px !important; }
  .main-content { padding: 24px 16px !important; }

  /* KPI cards — 2 columns on mobile */
  .kpi-grid { grid-template-columns: 1fr 1fr !important; }

  /* Numbered feature list — stack vertically */
  .feature-list { flex-direction: column !important; gap: 24px !important; }
  .feature-divider { display: none !important; }

  /* Two-column sections — stack */
  .two-col, 
  .split-section, 
  .case-study-layout { grid-template-columns: 1fr !important; 
    flex-direction: column !important; }

  /* Container padding */
  .container { padding-left: 20px !important; 
    padding-right: 20px !important; }

  /* Footer — single column */
  .footer-grid { grid-template-columns: 1fr !important; gap: 32px !important; }
}
"""

hamburger_html = """
    <div class="hamburger" style="display: none;">
      <span></span>
      <span></span>
      <span></span>
    </div>"""

mobile_js = """<script>
document.querySelector('.hamburger')?.addEventListener('click', () => {
  document.querySelector('.nav-links')?.classList.toggle('open');
});
</script>"""

def apply_mobile_fixes():
    for file in files:
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add CSS
        if '/* Nav — collapse to hamburger */' not in content:
            content = content.replace('</style>', f'{mobile_css}\n</style>')
        
        # Adjust <ul> to have class="nav-links"
        if '<ul class="nav-links"' not in content and '<ul class="nav-links">' not in content:
            # First occurrence of <ul> inside <nav> normally
            nav_match = re.search(r'<nav>.*?<ul>', content, re.DOTALL)
            if nav_match:
                content = content.replace('<ul>', '<ul class="nav-links">', 1)

        # Add Hamburger HTML right after </ul> or before <a class="button"> or before </nav>
        if 'class="hamburger"' not in content:
            if '<a href="dashboard.html" class="button">' in content:
                # Insert before the button to keep it generally right aligned next to it, or after the ul
                content = content.replace('</ul>\n    <a', '</ul>' + hamburger_html + '\n    <a')
            else:
                content = content.replace('</nav>', hamburger_html + '\n  </nav>', 1)
               
        # Add JS
        if "document.querySelector('.hamburger')" not in content:
            if '<script>' in content:
                content = content.replace('<script>', mobile_js + '\n  <script>', 1)
            else:
                content = content.replace('</body>', mobile_js + '\n</body>')

        # Rewrite file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    apply_mobile_fixes()
