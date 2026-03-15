import os
import re

dir_path = r'c:\trialspendly\spendly'
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# We need to overwrite the previous mobile CSS with fixed responsive targets.
# Fix 1: Make .nav-links toggle correctly by removing the `display: none !important` from the media query and instead targeting `.nav-links:not(.open)`
# Fix 2: Add `margin-left: auto;` to .hamburger
# Fix 3: Target `.dashboard-container` instead of `.app-layout` for vertical stacking on mobile
# Fix 4: Force the hero section to have the `hero` class

fixed_mobile_css = """
  /* MOBILE CHECKS - Comprehensive FIXED */
  @media (max-width: 768px) {
    /* Nav — collapse to hamburger */
    .nav-links:not(.open) { display: none !important; }
    .nav-links.open { display: flex !important; flex-direction: column; 
      position: absolute; top: 64px; left: 0; right: 0; 
      background: white; padding: 24px; 
      border-bottom: 1px solid #E5E7EB; z-index: 99; gap: 16px; }
    .hamburger { display: flex !important; cursor: pointer; 
      flex-direction: column; gap: 5px; margin-left: auto; }
    .hamburger span { display: block; width: 22px; height: 2px; 
      background: #0F1117; border-radius: 2px; 
      transition: all 0.2s; }

    /* Hero — stack vertically */
    .hero, #hero .container { flex-direction: column !important; 
      text-align: center !important; padding: 80px 24px 48px !important; display: flex !important; }
    .hero-visual, #hero .dashboard-card { display: none !important; }
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
    .dashboard-container { flex-direction: column !important; display: flex !important; }
    .sidebar { width: 100% !important; height: auto !important; 
      position: relative !important; 
      border-right: none !important; 
      border-bottom: 1px solid #E5E7EB !important; 
      padding: 16px !important; }
    .sidebar-nav { display: flex; flex-wrap: wrap; 
      gap: 8px !important; }
    .main-content { padding: 24px 16px !important; width: 100% !important; box-sizing: border-box; }

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
    .footer-grid, footer .container { grid-template-columns: 1fr !important; gap: 32px !important; }
  }
"""

def apply_fixes():
    for file in files:
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Clean up duplicate hamburgers
        # The previous script might have inserted generic CSS blocks, let's regex out the previous MOBILE CHECKS block
        content = re.sub(r'/\* MOBILE CHECKS - Comprehensive \*/.*?}\s*}', '', content, flags=re.DOTALL)
        content = re.sub(r'/\* MOBILE CHECKS \*/.*?}\s*}', '', content, flags=re.DOTALL)
        content = re.sub(r'nav::after { content: \'☰\'.*?}', '', content, flags=re.DOTALL)
        
        # Inject the new fixed css before </style>
        if '/* MOBILE CHECKS - Comprehensive FIXED */' not in content:
             content = content.replace('</style>', f'{fixed_mobile_css}\n</style>')

        # 2. Add hero class if missing to section id="hero"
        if '<section id="hero"' in content and 'class="hero"' not in content:
             # Make sure it gets class="hero"
             content = re.sub(r'<section id="hero"([^>]*)>', r'<section id="hero"\1 class="hero">', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    apply_fixes()
