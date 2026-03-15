"""
Premium Landing Page Upgrade Script
Injects 7 new sections, CSS styles, and JS into frontend/index.html
"""

filepath = r"c:\trialspendly\spendly\frontend\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# ── NEW CSS TO ADD ──
NEW_CSS = r"""
        /* ── SCROLL REVEAL ── */
        .reveal {
          opacity: 0;
          transform: translateY(24px);
          transition: opacity 0.65s ease, transform 0.65s ease;
        }
        .reveal.visible {
          opacity: 1;
          transform: translateY(0);
        }

        .stagger > * {
          opacity: 0;
          transform: translateY(18px);
          transition: opacity 0.55s ease, transform 0.55s ease;
        }
        .stagger.visible > *:nth-child(1) { opacity:1; transform:none; transition-delay:0.05s; }
        .stagger.visible > *:nth-child(2) { opacity:1; transform:none; transition-delay:0.13s; }
        .stagger.visible > *:nth-child(3) { opacity:1; transform:none; transition-delay:0.21s; }
        .stagger.visible > *:nth-child(4) { opacity:1; transform:none; transition-delay:0.29s; }
        .stagger.visible > *:nth-child(5) { opacity:1; transform:none; transition-delay:0.37s; }
        .stagger.visible > *:nth-child(6) { opacity:1; transform:none; transition-delay:0.45s; }
        .stagger.visible > *:nth-child(7) { opacity:1; transform:none; transition-delay:0.53s; }
        .stagger.visible > *:nth-child(8) { opacity:1; transform:none; transition-delay:0.61s; }
        .stagger.visible > *:nth-child(9) { opacity:1; transform:none; transition-delay:0.69s; }
        .stagger.visible > *:nth-child(10){ opacity:1; transform:none; transition-delay:0.77s; }
        .stagger.visible > *:nth-child(11){ opacity:1; transform:none; transition-delay:0.85s; }
        .stagger.visible > *:nth-child(12){ opacity:1; transform:none; transition-delay:0.93s; }

        /* ── PAGE LOAD STAGGER ── */
        .anim-1 { opacity:0; animation: fadeUp 0.65s ease 0.00s forwards; }
        .anim-2 { opacity:0; animation: fadeUp 0.65s ease 0.12s forwards; }
        .anim-3 { opacity:0; animation: fadeUp 0.65s ease 0.22s forwards; }
        .anim-4 { opacity:0; animation: fadeUp 0.65s ease 0.32s forwards; }
        .anim-5 { opacity:0; animation: fadeUp 0.65s ease 0.42s forwards; }
        .anim-6 { opacity:0; animation: fadeUp 0.80s ease 0.54s forwards; }

        /* ── LOGO SCROLL STRIP ── */
        .logo-strip {
          background: #ffffff;
          border-top: 1px solid #E8E6E0;
          border-bottom: 1px solid #E8E6E0;
          padding: 32px 40px;
          overflow: hidden;
        }
        .logo-strip-label {
          font-size: 11px;
          font-weight: 500;
          text-transform: uppercase;
          letter-spacing: 0.1em;
          color: #9A9890;
          text-align: center;
          margin-bottom: 22px;
          font-family: 'DM Sans', sans-serif;
        }
        .logo-track-wrap { overflow: hidden; }
        .logo-track {
          display: flex;
          align-items: center;
          gap: 64px;
          width: max-content;
          animation: scrollLogos 30s linear infinite;
        }
        .logo-track:hover { animation-play-state: paused; }
        @keyframes scrollLogos {
          from { transform: translateX(0); }
          to   { transform: translateX(-50%); }
        }
        .logo-item {
          font-family: 'DM Serif Display', Georgia, serif;
          font-size: 17px;
          color: #C8C6C0;
          white-space: nowrap;
          letter-spacing: -0.02em;
          transition: color 0.25s ease;
          cursor: default;
          user-select: none;
        }
        .logo-item:hover { color: #6B7280; }

        /* ── PROBLEM SECTION ── */
        .problem-section {
          background: #ffffff;
          padding: 120px 40px;
        }
        .problem-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 1px;
          background: #E8E6E0;
          border-radius: 20px;
          overflow: hidden;
          margin-top: 56px;
          border: 1px solid #E8E6E0;
        }
        .problem-card {
          background: #ffffff;
          padding: 44px 40px;
          transition: background 0.25s ease;
        }
        .problem-card:hover { background: #FAFAF8; }
        .problem-number {
          font-family: 'DM Serif Display', Georgia, serif;
          font-size: 56px;
          font-weight: 400;
          line-height: 1;
          color: #E0DED8;
          margin-bottom: 20px;
          letter-spacing: -0.03em;
        }
        .problem-title {
          font-family: 'DM Serif Display', Georgia, serif;
          font-size: 22px;
          color: #0C0C0A;
          margin-bottom: 12px;
          letter-spacing: -0.02em;
          line-height: 1.2;
        }
        .problem-desc {
          font-size: 14px;
          color: #6B7280;
          line-height: 1.7;
        }
        .problem-accent-line {
          width: 32px;
          height: 2px;
          border-radius: 2px;
          margin-bottom: 28px;
        }

        /* ── HOW IT WORKS ── */
        .how-section {
          background: #F7F6F2;
          padding: 120px 40px;
        }
        .how-steps {
          display: grid;
          grid-template-columns: repeat(4, 1fr);
          gap: 0;
          margin-top: 72px;
          position: relative;
        }
        .how-connector {
          position: absolute;
          top: 27px;
          left: calc(12.5% + 16px);
          width: calc(75% - 32px);
          height: 1px;
          background: #E8E6E0;
        }
        .how-step {
          padding: 0 28px;
          text-align: center;
          position: relative;
        }
        .how-step-num {
          width: 54px;
          height: 54px;
          border-radius: 50%;
          background: #ffffff;
          border: 1px solid #E8E6E0;
          display: flex;
          align-items: center;
          justify-content: center;
          margin: 0 auto 28px;
          font-family: 'JetBrains Mono', monospace;
          font-size: 13px;
          font-weight: 500;
          color: #9A9890;
          position: relative;
          z-index: 1;
          transition:
            background 0.25s ease,
            border-color 0.25s ease,
            color 0.25s ease,
            box-shadow 0.25s ease;
        }
        .how-step:hover .how-step-num {
          background: #0C0C0A;
          border-color: #0C0C0A;
          color: #ffffff;
          box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .how-step-title {
          font-family: 'DM Serif Display', Georgia, serif;
          font-size: 20px;
          color: #0C0C0A;
          margin-bottom: 12px;
          letter-spacing: -0.02em;
          line-height: 1.2;
        }
        .how-step-desc {
          font-size: 13.5px;
          color: #6B7280;
          line-height: 1.65;
        }

        /* ── BEFORE / AFTER ── */
        .comparison-section {
          background: #ffffff;
          padding: 120px 40px;
        }
        .comparison-wrap {
          display: grid;
          grid-template-columns: 1fr 64px 1fr;
          gap: 0;
          margin-top: 64px;
          align-items: start;
        }
        .comparison-col {
          border: 1px solid #E8E6E0;
          border-radius: 16px;
          overflow: hidden;
        }
        .comparison-col.col-after {
          border-color: #0C0C0A;
          box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        }
        .col-header {
          padding: 18px 26px;
          border-bottom: 1px solid #E8E6E0;
          display: flex;
          align-items: center;
          justify-content: space-between;
          background: #F9F9F7;
        }
        .col-after .col-header {
          background: #0C0C0A;
          border-bottom-color: rgba(255,255,255,0.08);
        }
        .col-header-left {
          display: flex;
          align-items: center;
          gap: 9px;
        }
        .col-dot {
          width: 7px;
          height: 7px;
          border-radius: 50%;
          flex-shrink: 0;
        }
        .col-title {
          font-size: 13px;
          font-weight: 500;
          color: #0C0C0A;
          font-family: 'DM Sans', sans-serif;
        }
        .col-after .col-title { color: #F5F4EF; }
        .col-sub {
          font-size: 11px;
          color: #9A9890;
          font-family: 'DM Sans', sans-serif;
        }
        .col-after .col-sub { color: #4A4A42; }
        .col-items { padding: 8px 0; }
        .col-item {
          display: flex;
          align-items: flex-start;
          gap: 12px;
          padding: 12px 26px;
          transition: background 0.18s ease;
        }
        .col-item:hover { background: #F7F6F2; }
        .col-after .col-item:hover { background: #F5F4EF; }
        .ci-marker {
          width: 18px;
          height: 18px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-shrink: 0;
          margin-top: 2px;
          font-size: 10px;
          font-weight: 700;
        }
        .ci-marker.bad  { background: #FEF2F2; color: #DC2626; }
        .ci-marker.good { background: #ECFDF5; color: #059669; }
        .ci-text {
          font-size: 13.5px;
          color: #44443C;
          line-height: 1.55;
          font-family: 'DM Sans', sans-serif;
        }
        .ci-text strong {
          color: #0C0C0A;
          font-weight: 500;
        }
        .vs-col {
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .vs-badge {
          font-family: 'DM Sans', sans-serif;
          font-size: 11px;
          font-weight: 500;
          color: #9A9890;
          background: #F7F6F2;
          border: 1px solid #E8E6E0;
          border-radius: 9999px;
          padding: 6px 12px;
          letter-spacing: 0.04em;
        }

        /* ── METRICS BAND ── */
        .metrics-band {
          background: #0C0C0A;
          padding: 80px 40px;
        }
        .metrics-grid {
          display: grid;
          grid-template-columns: repeat(4, 1fr);
          max-width: 1000px;
          margin: 0 auto;
        }
        .metric-divider {
          width: 1px;
          background: rgba(255,255,255,0.06);
          margin: 20px 0;
        }
        .metric-item {
          padding: 40px 36px;
          text-align: center;
          position: relative;
        }
        .metric-item + .metric-item {
          border-left: 1px solid rgba(255,255,255,0.06);
        }
        .metric-num {
          font-family: 'JetBrains Mono', monospace;
          font-size: 42px;
          font-weight: 500;
          color: #F5F4EF;
          line-height: 1;
          margin-bottom: 12px;
          letter-spacing: -0.03em;
          font-feature-settings: 'tnum';
        }
        .metric-label {
          font-size: 13px;
          color: #4A4A42;
          line-height: 1.6;
          font-family: 'DM Sans', sans-serif;
        }

        /* ── INTEGRATIONS ── */
        .integrations-section {
          background: #F7F6F2;
          padding: 120px 40px;
        }
        .integrations-header {
          text-align: center;
          max-width: 480px;
          margin: 0 auto 56px;
        }
        .integrations-grid {
          display: grid;
          grid-template-columns: repeat(6, 1fr);
          gap: 10px;
          max-width: 880px;
          margin: 0 auto;
        }
        .integration-card {
          background: #ffffff;
          border: 1px solid #E8E6E0;
          border-radius: 14px;
          padding: 20px 14px 18px;
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 8px;
          transition:
            transform 0.22s ease,
            box-shadow 0.22s ease,
            border-color 0.22s ease;
          cursor: default;
        }
        .integration-card:hover {
          transform: translateY(-3px);
          box-shadow: 0 6px 20px rgba(0,0,0,0.07);
          border-color: #C8C6C0;
        }
        .int-logo {
          width: 36px;
          height: 36px;
          border-radius: 8px;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 12px;
          font-weight: 600;
          font-family: 'DM Sans', sans-serif;
        }
        .int-name {
          font-size: 11px;
          color: #6B7280;
          font-weight: 500;
          text-align: center;
          font-family: 'DM Sans', sans-serif;
          line-height: 1.3;
        }
        .int-status {
          font-size: 9px;
          font-weight: 500;
          padding: 2px 7px;
          border-radius: 20px;
          text-transform: uppercase;
          letter-spacing: 0.05em;
          font-family: 'DM Sans', sans-serif;
        }
        .s-live { background: #ECFDF5; color: #065F46; }
        .s-soon { background: #F7F6F2; color: #9A9890; }

        /* ── FAQ ── */
        .faq-section {
          background: #ffffff;
          padding: 120px 40px;
        }
        .faq-inner {
          max-width: 660px;
          margin: 0 auto;
        }
        .faq-list { margin-top: 56px; }
        .faq-item {
          border-bottom: 1px solid #E8E6E0;
        }
        .faq-item:first-child { border-top: 1px solid #E8E6E0; }
        .faq-btn {
          width: 100%;
          background: none;
          border: none;
          padding: 22px 0;
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: 20px;
          font-family: 'DM Sans', sans-serif;
          font-size: 15.5px;
          font-weight: 500;
          color: #0C0C0A;
          cursor: pointer;
          text-align: left;
          transition: color 0.2s;
        }
        .faq-btn:hover { color: #2563EB; }
        .faq-icon {
          width: 24px;
          height: 24px;
          border-radius: 50%;
          border: 1.5px solid #E8E6E0;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-shrink: 0;
          font-size: 16px;
          color: #9A9890;
          line-height: 1;
          transition:
            background 0.25s ease,
            border-color 0.25s ease,
            color 0.25s ease,
            transform 0.25s ease;
        }
        .faq-item.open .faq-icon {
          background: #0C0C0A;
          border-color: #0C0C0A;
          color: #ffffff;
          transform: rotate(45deg);
        }
        .faq-body {
          font-size: 14.5px;
          color: #6B7280;
          line-height: 1.75;
          max-height: 0;
          overflow: hidden;
          transition: max-height 0.35s ease, padding-bottom 0.35s ease;
          padding-bottom: 0;
          font-family: 'DM Sans', sans-serif;
        }
        .faq-item.open .faq-body {
          max-height: 200px;
          padding-bottom: 22px;
        }

        /* ── NEW RESPONSIVE ── */
        @media (max-width: 1024px) {
          .integrations-grid { grid-template-columns: repeat(4, 1fr); }
        }
        @media (max-width: 768px) {
          .problem-grid       { grid-template-columns: 1fr; }
          .how-steps          { grid-template-columns: 1fr 1fr; }
          .how-connector      { display: none; }
          .comparison-wrap    { grid-template-columns: 1fr; }
          .vs-col             { display: none; }
          .metrics-grid       { grid-template-columns: 1fr 1fr; }
          .integrations-grid  { grid-template-columns: repeat(3, 1fr); }
          .logo-strip         { padding: 24px 20px; }
        }
        @media (max-width: 480px) {
          .integrations-grid  { grid-template-columns: repeat(2, 1fr); }
          .how-steps          { grid-template-columns: 1fr; }
          .metrics-grid       { grid-template-columns: 1fr 1fr; }
          .metric-num         { font-size: 32px; }
        }
"""

# ── LOGO STRIP HTML ──
LOGO_STRIP = """
    <div class="logo-strip">
      <div class="logo-strip-label">Trusted by finance teams at</div>
      <div class="logo-track-wrap">
        <div class="logo-track">
          <span class="logo-item">Meridian Labs</span>
          <span class="logo-item">Acme Corp</span>
          <span class="logo-item">Flux Materials</span>
          <span class="logo-item">Orbit Systems</span>
          <span class="logo-item">Cascade Group</span>
          <span class="logo-item">Nova Ventures</span>
          <span class="logo-item">Apex Digital</span>
          <span class="logo-item">Summit Tech</span>
          <span class="logo-item">Meridian Labs</span>
          <span class="logo-item">Acme Corp</span>
          <span class="logo-item">Flux Materials</span>
          <span class="logo-item">Orbit Systems</span>
          <span class="logo-item">Cascade Group</span>
          <span class="logo-item">Nova Ventures</span>
          <span class="logo-item">Apex Digital</span>
          <span class="logo-item">Summit Tech</span>
        </div>
      </div>
    </div>
"""

# ── PROBLEM SECTION HTML ──
PROBLEM_SECTION = """
    <section class="problem-section">
      <div class="container">
        <div class="reveal">
          <span class="section-label">The problem</span>
          <h2 style="font-family:'DM Serif Display',Georgia,serif;font-size:clamp(32px,4vw,52px);letter-spacing:-0.025em;line-height:1.1;color:#0C0C0A;max-width:580px;margin-top:12px;margin-bottom:0">
            Companies are bleeding money.<br><em>Nobody notices.</em>
          </h2>
        </div>
        <div class="problem-grid stagger">
          <div class="problem-card">
            <div class="problem-accent-line" style="background:#DC2626"></div>
            <div class="problem-number">$247k</div>
            <div class="problem-title">Average annual SaaS spend</div>
            <div class="problem-desc">The typical mid-size company spends a quarter million dollars a year on software \u2014 and has no idea where it all goes.</div>
          </div>
          <div class="problem-card">
            <div class="problem-accent-line" style="background:#D97706"></div>
            <div class="problem-number">30%</div>
            <div class="problem-title">Goes completely wasted</div>
            <div class="problem-desc">Unused licenses, forgotten trials, duplicate tools across departments. Industry data puts waste at 20\u201330% of total SaaS spend.</div>
          </div>
          <div class="problem-card">
            <div class="problem-accent-line" style="background:#2563EB"></div>
            <div class="problem-number">3\u00d7</div>
            <div class="problem-title">More tools than they track</div>
            <div class="problem-desc">IT knows about some tools. Finance sees payments for others. HR tracks headcount. Nobody has the full picture \u2014 until Spendly.</div>
          </div>
        </div>
      </div>
    </section>
"""

# ── HOW IT WORKS HTML ──
HOW_SECTION = """
    <section class="how-section">
      <div class="container">
        <div class="reveal" style="text-align:center;max-width:540px;margin:0 auto">
          <span class="section-label">How it works</span>
          <h2 style="font-family:'DM Serif Display',Georgia,serif;font-size:clamp(32px,4vw,52px);letter-spacing:-0.025em;line-height:1.1;color:#0C0C0A;margin-top:12px">
            From connection to <em>savings in 90 minutes</em>
          </h2>
        </div>
        <div class="how-steps stagger" style="position:relative">
          <div class="how-connector"></div>
          <div class="how-step">
            <div class="how-step-num">01</div>
            <div class="how-step-title">Connect your data</div>
            <div class="how-step-desc">Link your bank feed, SSO provider, or accounting tool. Takes under 12 minutes. No engineering required.</div>
          </div>
          <div class="how-step">
            <div class="how-step-num">02</div>
            <div class="how-step-title">Spendly scans everything</div>
            <div class="how-step-desc">AI automatically discovers every SaaS subscription, maps it to employees, and cross-references usage data.</div>
          </div>
          <div class="how-step">
            <div class="how-step-num">03</div>
            <div class="how-step-title">Waste gets flagged</div>
            <div class="how-step-desc">Unused seats, duplicate tools, expiring trials, and risky renewals surface as ranked actionable alerts.</div>
          </div>
          <div class="how-step">
            <div class="how-step-num">04</div>
            <div class="how-step-title">You approve. Money saved.</div>
            <div class="how-step-desc">One click to approve a recommendation. Spendly tracks every dollar recovered and projects your 90-day savings.</div>
          </div>
        </div>
      </div>
    </section>
"""

# ── COMPARISON SECTION HTML ──
COMPARISON_SECTION = """
    <section class="comparison-section">
      <div class="container">
        <div class="reveal">
          <span class="section-label">The difference</span>
          <h2 style="font-family:'DM Serif Display',Georgia,serif;font-size:clamp(32px,4vw,52px);letter-spacing:-0.025em;line-height:1.1;color:#0C0C0A;max-width:540px;margin-top:12px">
            Life before and <em>after Spendly</em>
          </h2>
        </div>
        <div class="comparison-wrap">
          <div class="comparison-col col-before">
            <div class="col-header">
              <div class="col-header-left">
                <div class="col-dot" style="background:#DC2626"></div>
                <span class="col-title">Without Spendly</span>
              </div>
              <span class="col-sub">Current state</span>
            </div>
            <div class="col-items">
              <div class="col-item">
                <div class="ci-marker bad">\u2715</div>
                <div class="ci-text">Spreadsheets tracking <strong>some</strong> subscriptions \u2014 manually updated, always out of date</div>
              </div>
              <div class="col-item">
                <div class="ci-marker bad">\u2715</div>
                <div class="ci-text">Offboarded employees still have <strong>active paid licenses</strong> weeks later</div>
              </div>
              <div class="col-item">
                <div class="ci-marker bad">\u2715</div>
                <div class="ci-text">Marketing uses Notion. Engineering uses Confluence. <strong>Nobody knows both exist.</strong></div>
              </div>
              <div class="col-item">
                <div class="ci-marker bad">\u2715</div>
                <div class="ci-text">$48,000 Salesforce renewal <strong>auto-renews</strong> because nobody set a reminder</div>
              </div>
              <div class="col-item">
                <div class="ci-marker bad">\u2715</div>
                <div class="ci-text">Finance asks IT for a tool list. IT asks Finance. <strong>Nobody has it.</strong></div>
              </div>
              <div class="col-item">
                <div class="ci-marker bad">\u2715</div>
                <div class="ci-text">Free trial converts to paid at 2am. <strong>$890/mo charged.</strong> Nobody notices for 3 months.</div>
              </div>
            </div>
          </div>

          <div class="vs-col">
            <div class="vs-badge">VS</div>
          </div>

          <div class="comparison-col col-after">
            <div class="col-header">
              <div class="col-header-left">
                <div class="col-dot" style="background:#059669"></div>
                <span class="col-title">With Spendly</span>
              </div>
              <span class="col-sub">Your new reality</span>
            </div>
            <div class="col-items">
              <div class="col-item">
                <div class="ci-marker good">\u2713</div>
                <div class="ci-text"><strong>Every SaaS tool</strong> automatically discovered \u2014 bank feed, SSO, and accounting connected</div>
              </div>
              <div class="col-item">
                <div class="ci-marker good">\u2713</div>
                <div class="ci-text">Offboarded employees flagged <strong>instantly</strong> \u2014 idle seats reclaimed before next billing cycle</div>
              </div>
              <div class="col-item">
                <div class="ci-marker good">\u2713</div>
                <div class="ci-text">AI detects the overlap, <strong>recommends consolidation</strong>, calculates exact annual savings</div>
              </div>
              <div class="col-item">
                <div class="ci-marker good">\u2713</div>
                <div class="ci-text"><strong>90-day renewal calendar</strong> with risk scores \u2014 catch every contract before it auto-renews</div>
              </div>
              <div class="col-item">
                <div class="ci-marker good">\u2713</div>
                <div class="ci-text">One dashboard for Finance, IT, and HR \u2014 <strong>same data, every team aligned</strong></div>
              </div>
              <div class="col-item">
                <div class="ci-marker good">\u2713</div>
                <div class="ci-text">Trial conversion alerts fire <strong>14 days early</strong> \u2014 cancel or upgrade entirely on your terms</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# ── METRICS BAND HTML ──
METRICS_BAND = """
    <div class="metrics-band reveal">
      <div class="metrics-grid">
        <div class="metric-item">
          <div class="metric-num" data-counter data-target="247830" data-prefix="$">$247,830</div>
          <div class="metric-label">Average SaaS spend<br>detected per company</div>
        </div>
        <div class="metric-item">
          <div class="metric-num" data-counter data-target="61" data-prefix="$" data-suffix="k+">$61k+</div>
          <div class="metric-label">Average annual waste<br>recovered in year one</div>
        </div>
        <div class="metric-item">
          <div class="metric-num" data-counter data-target="47" data-suffix=" min">47 min</div>
          <div class="metric-label">Time from signup<br>to first insight</div>
        </div>
        <div class="metric-item">
          <div class="metric-num" data-counter data-target="94" data-suffix="%">94%</div>
          <div class="metric-label">Of AI-flagged waste<br>confirmed accurate</div>
        </div>
      </div>
    </div>
"""

# ── INTEGRATIONS HTML ──
INTEGRATIONS = """
    <section class="integrations-section">
      <div class="container">
        <div class="integrations-header reveal">
          <span class="section-label">Integrations</span>
          <h2 style="font-family:'DM Serif Display',Georgia,serif;font-size:clamp(28px,3.5vw,44px);letter-spacing:-0.025em;line-height:1.1;color:#0C0C0A;margin-top:12px">
            Connects to tools<br><em>you already use</em>
          </h2>
        </div>
        <div class="integrations-grid stagger">
          <div class="integration-card">
            <div class="int-logo" style="background:#EFF6FF;color:#1D4ED8">Pl</div>
            <div class="int-name">Plaid</div>
            <span class="int-status s-live">Live</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#F0FDF4;color:#166534">Ok</div>
            <div class="int-name">Okta</div>
            <span class="int-status s-live">Live</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#FFF7ED;color:#C2410C">Qb</div>
            <div class="int-name">QuickBooks</div>
            <span class="int-status s-live">Live</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#F5F3FF;color:#6D28D9">Gg</div>
            <div class="int-name">Google SSO</div>
            <span class="int-status s-live">Live</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#EFF6FF;color:#1D4ED8">Xe</div>
            <div class="int-name">Xero</div>
            <span class="int-status s-live">Live</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#ECFDF5;color:#065F46">Bb</div>
            <div class="int-name">BambooHR</div>
            <span class="int-status s-soon">Soon</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#FEF2F2;color:#991B1B">Sf</div>
            <div class="int-name">Salesforce</div>
            <span class="int-status s-soon">Soon</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#FFFBEB;color:#92400E">Sl</div>
            <div class="int-name">Slack</div>
            <span class="int-status s-soon">Soon</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#F7F6F2;color:#6B7280">Az</div>
            <div class="int-name">Azure AD</div>
            <span class="int-status s-soon">Soon</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#EFF6FF;color:#1D4ED8">Ne</div>
            <div class="int-name">NetSuite</div>
            <span class="int-status s-soon">Soon</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#F0FDF4;color:#166534">Wr</div>
            <div class="int-name">Workday</div>
            <span class="int-status s-soon">Soon</span>
          </div>
          <div class="integration-card">
            <div class="int-logo" style="background:#F7F6F2;color:#9A9890">+8</div>
            <div class="int-name">More coming</div>
            <span class="int-status s-soon">2025</span>
          </div>
        </div>
      </div>
    </section>
"""

# ── FAQ HTML ──
FAQ_SECTION = """
    <section class="faq-section reveal">
      <div class="container">
        <div class="faq-inner">
          <div style="text-align:center">
            <span class="section-label">FAQ</span>
            <h2 style="font-family:'DM Serif Display',Georgia,serif;font-size:clamp(32px,4vw,48px);letter-spacing:-0.025em;line-height:1.1;color:#0C0C0A;margin-top:12px">
              Questions we <em>always get asked</em>
            </h2>
          </div>
          <div class="faq-list">
            <div class="faq-item">
              <button class="faq-btn" onclick="toggleFaq(this)">
                How long does it take to set up?
                <span class="faq-icon">+</span>
              </button>
              <div class="faq-body">
                Most teams are fully connected in under 12 minutes. Connect your bank feed or accounting tool, link your SSO provider, and Spendly starts scanning immediately. Your first insights appear within the hour \u2014 no engineering resources required.
              </div>
            </div>
            <div class="faq-item">
              <button class="faq-btn" onclick="toggleFaq(this)">
                Does Spendly actually save money or just show data?
                <span class="faq-icon">+</span>
              </button>
              <div class="faq-body">
                Both. Spendly surfaces the waste and gives you one-click actions to eliminate it. You approve a recommendation and it tracks the savings in real time. Average first-year recovery is $61,000 \u2014 with 94% of flagged items confirmed as genuine waste.
              </div>
            </div>
            <div class="faq-item">
              <button class="faq-btn" onclick="toggleFaq(this)">
                Is our financial data safe?
                <span class="faq-icon">+</span>
              </button>
              <div class="faq-body">
                Yes. Spendly is SOC 2 compliant, uses bank-grade encryption, and never stores raw credentials. We connect via OAuth and read-only API access \u2014 we can see your spend data but never move money or make changes on your behalf.
              </div>
            </div>
            <div class="faq-item">
              <button class="faq-btn" onclick="toggleFaq(this)">
                What if we only have a few SaaS tools?
                <span class="faq-icon">+</span>
              </button>
              <div class="faq-body">
                Spendly works for teams with as few as 10 tools. Most customers discover 20\u201330% more tools than they thought they had. Our Starter plan is built for smaller stacks and pays for itself after a single cancelled subscription.
              </div>
            </div>
            <div class="faq-item">
              <button class="faq-btn" onclick="toggleFaq(this)">
                How is this different from checking our credit card statement?
                <span class="faq-icon">+</span>
              </button>
              <div class="faq-body">
                Credit card statements show payments but not usage. Spendly connects payment data with employee login data and HR records \u2014 so you see not just what you're paying, but who's actually using it, which seats are idle, and which tools are duplicated.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# ── NEW SCRIPT ──
NEW_SCRIPT = """
    <script>
    // Navbar scroll state
    const nb = document.querySelector('nav') || document.getElementById('navbar');
    if (nb) {
      window.addEventListener('scroll', () => {
        nb.classList.toggle('scrolled', window.scrollY > 20);
      }, { passive: true });
    }

    // Hamburger
    const hb = document.getElementById('hamburger');
    const nl = document.getElementById('navLinks');
    if (hb && nl) {
      hb.addEventListener('click', () => {
        const open = nl.classList.toggle('open');
        const spans = hb.querySelectorAll('span');
        spans[0].style.transform = open ? 'rotate(45deg) translate(5px,5px)' : '';
        spans[1].style.opacity   = open ? '0' : '1';
        spans[2].style.transform = open ? 'rotate(-45deg) translate(5px,-5px)' : '';
      });
    }

    // Scroll reveal
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -32px 0px' });
    document.querySelectorAll('.reveal, .stagger, .fade-in').forEach(el => obs.observe(el));

    // Counter animation
    function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }
    function runCounter(el) {
      const target   = parseFloat(el.dataset.target) || 0;
      const prefix   = el.dataset.prefix  || '';
      const suffix   = el.dataset.suffix  || '';
      const duration = 1800;
      const start    = performance.now();
      const tick = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const v = Math.floor(easeOutQuart(p) * target);
        el.textContent = prefix + v.toLocaleString() + suffix;
        if (p < 1) requestAnimationFrame(tick);
        else el.textContent = prefix + target.toLocaleString() + suffix;
      };
      requestAnimationFrame(tick);
    }
    const cObs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { runCounter(e.target); cObs.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    document.querySelectorAll('[data-counter]').forEach(el => cObs.observe(el));

    // FAQ
    function toggleFaq(btn) {
      const item   = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    }

    // Magnetic buttons
    document.querySelectorAll('.btn-primary, .btn-ghost, .btn-light').forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
        const r = btn.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width  / 2) * 0.1;
        const y = (e.clientY - r.top  - r.height / 2) * 0.1;
        btn.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
      });
      btn.addEventListener('mouseleave', () => {
        btn.style.transform = '';
      });
    });

    // Page fade in on load
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.4s ease';
    window.addEventListener('load', () => {
      requestAnimationFrame(() => { document.body.style.opacity = '1'; });
    });

    // Smooth page exit
    document.querySelectorAll('a[href]').forEach(link => {
      const href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto')) return;
      link.addEventListener('click', (e) => {
        e.preventDefault();
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.18s ease';
        setTimeout(() => window.location.href = href, 180);
      });
    });
    </script>
"""

# ── PERFORM INSERTIONS (bottom-up to preserve line numbers) ──

content = "".join(lines)

# 1. Find and replace the old <script> block with the new one
# The old script block starts at "    <script>" and ends at "    </script>"
old_script_start = content.find("    <script>\n    // Navbar scroll")
if old_script_start == -1:
    old_script_start = content.find("    <script>\r\n    // Navbar scroll")
old_script_end = content.find("    </script>", old_script_start)
if old_script_end != -1:
    # Include the closing tag
    old_script_end = content.find("\n", old_script_end) + 1
    content = content[:old_script_start] + NEW_SCRIPT + "\n" + content[old_script_end:]

# 2. Insert FAQ section before <!-- FINAL CTA -->
final_cta_marker = "    <!-- FINAL CTA -->"
content = content.replace(final_cta_marker, FAQ_SECTION + "\n" + final_cta_marker)

# 3. Insert Integrations + Metrics before FAQ (which is now before FINAL CTA)
# Insert after insights </section> — find "<!-- INSIGHTS -->" section end
# The insights section ends, then we want to add after it
insights_end = content.find("    <!-- FINAL CTA -->")
# Actually insert before final CTA (which now has FAQ before it)
# Let's insert before the FAQ section
faq_marker = '    <section class="faq-section reveal">'
content = content.replace(faq_marker, INTEGRATIONS + "\n" + faq_marker)

# 4. Insert Metrics Band before Integrations
integrations_marker = '    <section class="integrations-section">'
content = content.replace(integrations_marker, METRICS_BAND + "\n" + integrations_marker)

# 5. Insert Comparison before Metrics Band
metrics_marker = '    <div class="metrics-band reveal">'
content = content.replace(metrics_marker, COMPARISON_SECTION + "\n" + metrics_marker)

# 6. Insert How It Works after Editorial section end (after <!-- VALUES PILLARS -->)
pillars_marker = "    <!-- VALUES PILLARS -->"
content = content.replace(pillars_marker, HOW_SECTION + "\n" + pillars_marker)

# 7. Insert Problem Section after Feature Strip
# Feature strip ends with "</div>" on its own line after feature items
feature_strip_marker = "    <!-- EDITORIAL SPLIT -->"
content = content.replace(feature_strip_marker, PROBLEM_SECTION + "\n" + feature_strip_marker)

# 8. Insert Logo Strip after hero </section>
# Hero section closes, then Feature Strip starts
feature_strip_start = "    <!-- FEATURE STRIP -->"
content = content.replace(feature_strip_start, LOGO_STRIP + "\n" + feature_strip_start)

# 9. Insert CSS before the closing </style> — find the last </style>
# We need to find the main </style> tag
style_close = "    </style>"
content = content.replace(style_close, NEW_CSS + "\n" + style_close, 1)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: All 7 sections, CSS, and JS injected into index.html")
