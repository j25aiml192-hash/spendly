import os

filepath = r'c:\trialspendly\spendly\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to remove the broken `<nav>` duplicates and append a working body structure with `#hero` and `footer`.
# Let's find where <body> starts.
body_start = content.find('<body>')
if body_start != -1:
    css_and_head = content[:body_start + 6]
else:
    css_and_head = content

HTML_BODY = """
  <nav>
    <a href="index.html" class="logo active">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2L2 7l10 5 10-5-10-5z m0 15L2 12l10-5 10 5-10 5z m0 8L2 17l10-5 10 5-10 5z" />
      </svg>
      Spendly
    </a>
    <ul>
      <li><a href="features.html">Product</a></li>
      <li><a href="insights.html">Insights</a></li>
      <li><a href="pricing.html">Pricing</a></li>
      <li><a href="about.html">About</a></li>
    </ul>
    <a href="dashboard.html" class="button">Start for free</a>
  </nav>

  <section id="hero" class="active">
    <div class="container">
      <div>
        <h1>AI-powered SaaS<br><em>Spend Intelligence</em></h1>
        <p>Detect wasted licenses, eliminate duplicate tools, and automate your software renewals.</p>
        <div class="buttons">
          <a href="dashboard.html" class="primary-button">Get started</a>
          <a href="features.html" class="ghost-button">View features</a>
        </div>
        <span class="trust-line">Trusted by finance teams worldwide</span>
      </div>
      <div>
        <div class="dashboard-card">
          <div class="dashboard-card-header">
            <div class="fake-window-buttons">
              <span></span><span></span><span></span>
            </div>
            Overview
          </div>
          <h3>Total SaaS Spend</h3>
          <div class="total-spend">$247,830</div>
          <div class="total-spend-delta">+3.2% vs last month</div>
          <div class="dashboard-metrics">
            <div class="dashboard-metric-card">
              <h4>Active</h4>
              <p>47 tools</p>
            </div>
            <div class="dashboard-metric-card">
              <h4>Waste</h4>
              <p>$61,240</p>
            </div>
            <div class="dashboard-metric-card">
              <h4>Renewals</h4>
              <p>6 soon</p>
            </div>
          </div>
          <div class="dashboard-alert">
            14 assigned Figma seats are inactive
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="cta" class="active">
    <div class="container">
      <h4>Ready to see what you're wasting?</h4>
      <a href="dashboard.html" class="button">Request a demo</a>
    </div>
  </section>

  <footer style="background-color: var(--bg-dark); color: var(--text-on-dark-muted); padding: 64px 0; font-size: 14px;">
    <div class="container" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;">
      <div style="font-family: 'DM Serif Display', serif; font-size: 22px; color: var(--text-primary);">
        Spendly
        <p style="font-family: 'DM Sans', sans-serif; color: var(--text-on-dark-muted); margin-top: 8px;">
          AI-powered SaaS spend intelligence<br>Built by Team Bugg Slayers</p>
      </div>
      <div>
        <h5 style="font-family: 'DM Sans', sans-serif; font-size: 16px; font-weight: 500; color: var(--text-on-dark); margin-bottom: 16px;">
          Product</h5>
        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="margin-bottom: 8px;"><a href="dashboard.html" style="color: var(--text-on-dark-muted); text-decoration: none;">Overview</a></li>
          <li style="margin-bottom: 8px;"><a href="features.html" style="color: var(--text-on-dark-muted); text-decoration: none;">Features</a></li>
          <li style="margin-bottom: 8px;"><a href="pricing.html" style="color: var(--text-on-dark-muted); text-decoration: none;">Pricing</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Changelog</a></li>
        </ul>
      </div>
      <div>
        <h5 style="font-family: 'DM Sans', sans-serif; font-size: 16px; font-weight: 500; color: var(--text-on-dark); margin-bottom: 16px;">
          Company</h5>
        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="margin-bottom: 8px;"><a href="about.html" style="color: var(--text-on-dark-muted); text-decoration: none;">About</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Careers</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Blog</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Contact</a></li>
        </ul>
      </div>
      <div>
        <h5 style="font-family: 'DM Sans', sans-serif; font-size: 16px; font-weight: 500; color: var(--text-on-dark); margin-bottom: 16px;">
          Legal</h5>
        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Privacy</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Terms</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Security</a></li>
          <li style="margin-bottom: 8px;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">SOC 2</a></li>
        </ul>
      </div>
    </div>
    <div class="divider" style="border-top: 1px solid rgba(255,255,255,0.1); margin: 32px 0;"></div>
    <div class="bottom" style="display: flex; justify-content: space-between; align-items: center;">
      <p style="color: var(--text-on-dark-muted); font-family: 'DM Sans', sans-serif;">© 2025 Spendly · Built by Team Bugg Slayers</p>
      <p style="color: var(--text-on-dark-muted); font-family: 'DM Sans', sans-serif;"><a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Privacy</a> · <a href="#" style="color: var(--text-on-dark-muted); text-decoration: none;">Terms</a></p>
    </div>
  </footer>
</body>
</html>
"""

new_content = css_and_head + '\n' + HTML_BODY
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
