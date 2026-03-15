import re

filepath = r"c:\trialspendly\spendly\frontend\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# FIX 1
html = re.sub(
    r'body\s*\{[^}]+\}',
    r"""body {
            font-family: var(--sans);
            background: #f0f4ff;
            min-height: 100vh;
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }""",
    html
)
html = re.sub(
    r'\.page-bg\s*\{[^}]+\}',
    r""".page-bg {
            position: fixed;
            inset: 0;
            z-index: -1;
            background: radial-gradient(
                ellipse 140% 70% at 50% -10%,
                #c7d9ff 0%,
                #e8f0ff 35%,
                #f5f0ea 65%,
                #faf6f0 100%
            );
        }""",
    html
)
html = re.sub(
    r'\.page-bg::after\s*\{[^}]+\}',
    r""".page-bg::after {
            content: '';
            position: absolute;
            inset: 0;
            opacity: 0.025;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
            background-size: 128px;
            pointer-events: none;
        }""",
    html
)

if '<div class="page-bg"></div>' not in html:
    html = html.replace('<body>', '<body>\n    <div class="page-bg"></div>', 1)

# FIX 2 & 3
hero_badge = r"""<div class="hero-badge">
            <span class="hero-badge-dot"></span>
            AI-powered SaaS spend intelligence
        </div>"""

html = re.sub(
    r'<h1[^>]*>.*?</h1>',
    r'<h1>Stop wasting money on SaaS<br><em>no one uses.</em></h1>',
    html,
    count=1,
    flags=re.DOTALL
)

# It was previously removed, so let's check if we can insert it before the h1
if "AI-powered SaaS spend intelligence" not in html:
    html = html.replace('<h1>Stop wasting', f'{hero_badge}\n\n        <h1>Stop wasting')

html = re.sub(
    r'\.hero h1\s*\{[^}]+\}',
    r""".hero h1 {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: clamp(44px, 7vw, 88px);
            font-weight: 400;
            line-height: 1.04;
            letter-spacing: -0.03em;
            color: #0C0C0A;
            max-width: 820px;
            margin-bottom: 24px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.1s forwards;
        }
        
        .hero h1 em { font-style: italic; }
        """,
    html
)

html = re.sub(
    r'\.hero-badge\s*\{[^}]+\}',
    r""".hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(255,255,255,0.75);
            border: 1px solid #E8E6E0;
            border-radius: 9999px;
            padding: 6px 16px;
            font-size: 12.5px;
            font-weight: 500;
            color: #6B7280;
            margin-bottom: 28px;
            backdrop-filter: blur(8px);
            opacity: 0;
            animation: fadeUp 0.6s ease forwards;
        }""",
    html
)
html = re.sub(
    r'\.hero-badge-dot\s*\{[^}]+\}',
    r""".hero-badge-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #059669;
            flex-shrink: 0;
        }""",
    html
)

# FIX 4
html = re.sub(
    r'\.hero\s*\{\s*min-height[^}]+\}',
    r""".hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 140px 24px 100px;
        }""",
    html
)

html = re.sub(
    r'\.hero-sub\s*\{[^}]+\}',
    r""".hero-sub, .hero p {
            font-size: clamp(16px, 2vw, 19px);
            color: #44443C;
            max-width: 520px;
            line-height: 1.7;
            margin-bottom: 40px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.2s forwards;
        }""",
    html
)

html = re.sub(
    r'\.hero-trust\s*\{[^}]+\}',
    r""".hero-trust {
            font-size: 13px;
            color: #9A9890;
            margin-bottom: 72px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.35s forwards;
        }""",
    html
)

# FIX 5
html = re.sub(
    r'\.dashboard-wrap\s*\{[^}]+\}',
    r""".dashboard-wrap {
            width: 100%;
            max-width: 880px;
            margin: 0 auto;
            opacity: 0;
            animation: fadeUp 0.8s ease 0.45s forwards;
        }""",
    html
)
html = re.sub(
    r'\.dashboard-card\s*\{[^}]+\}',
    r""".dashboard-card {
            background: #ffffff;
            border-radius: 20px;
            border: 1px solid #E8E6E0;
            box-shadow:
                0 0 0 1px rgba(0,0,0,0.03),
                0 4px 16px rgba(0,0,0,0.06),
                0 24px 64px rgba(0,0,0,0.10),
                0 48px 100px rgba(0,0,0,0.08);
            overflow: hidden;
            animation: float 6s ease-in-out infinite;
            transform-origin: center bottom;
        }""",
    html
)

html = re.sub(
    r'@keyframes float\s*\{[\s\S]*?50%\s*\{[^}]+\}\s*\}',
    r"""@keyframes float {
            0%, 100% { transform: translateY(0px) rotate(-1.5deg); }
            50%       { transform: translateY(-14px) rotate(-1.5deg); }
        }""",
    html
)

# FIX 6
html = re.sub(
    r'section\s*\{\s*padding: 100px 24px;\s*\}',
    r"""section {
            padding: 120px 40px;
        }""",
    html
)


# FIX 7
html = re.sub(
    r'\.feature-strip\s*\{[^}]+\}',
    r""".feature-strip {
            background: #ffffff;
            border-top: 1px solid #E8E6E0;
            border-bottom: 1px solid #E8E6E0;
            padding: 56px 40px;
        }""",
    html
)

html = re.sub(
    r'\.feature-strip \.container\s*\{[^}]+\}',
    r""".feature-strip .container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0;
        }""",
    html
)

html = re.sub(
    r'\.feature-item\s*\{[^}]+\}',
    r""".feature-item {
            padding: 0 36px;
            border-right: 1px solid #E8E6E0;
            transition: all 0.2s ease;
        }
        .feature-item:first-child { padding-left: 0; }
        .feature-item:last-child { border-right: none; }""",
    html,
    count=1
)

html = re.sub(
    r'\.feature-num\s*\{[^}]+\}',
    r""".feature-num {
            font-size: 11px;
            color: #9A9890;
            margin-bottom: 12px;
            letter-spacing: 0.04em;
            font-family: 'DM Sans', sans-serif;
        }""",
    html
)

html = re.sub(
    r'\.feature-verb\s*\{[^}]+\}',
    r""".feature-verb {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: 26px;
            color: #0C0C0A;
            letter-spacing: -0.02em;
            margin-bottom: 8px;
            transition: color 0.2s ease;
            line-height: 1.1;
        }""",
    html
)

html = re.sub(
    r'\.feature-desc\s*\{[^}]+\}',
    r""".feature-desc {
            font-size: 13.5px;
            color: #6B7280;
            line-height: 1.6;
        }""",
    html
)

# FIX 8
html = re.sub(
    r'\.article-img\s*\{[^}]+\}',
    r""".article-img {
            height: 180px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border-radius: 0;
        }""",
    html
)

html = re.sub(
    r'\.article-card\s*\{[^}]+\}',
    r""".article-card {
            background: #ffffff;
            border: 1px solid #E8E6E0;
            border-radius: 16px;
            overflow: hidden;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            text-decoration: none;
            color: inherit;
            display: block;
        }""",
    html
)

html = re.sub(
    r'\.article-card:hover\s*\{[^}]+\}',
    r""".article-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.08),
                        0 20px 48px rgba(0,0,0,0.10);
        }""",
    html
)

html = re.sub(
    r'\.article-body\s*\{[^}]+\}',
    r""".article-body {
            padding: 22px 24px 26px;
        }""",
    html
)

html = re.sub(
    r'\.article-title\s*\{[^}]+\}',
    r""".article-title {
            font-size: 15.5px;
            font-weight: 500;
            color: #0C0C0A;
            line-height: 1.45;
            margin-bottom: 14px;
        }""",
    html
)

# FIX 9
html = re.sub(
    r'\.testimonial\s*\{\s*background:[^}]+}',
    r""".testimonial {
            background: #F7F6F2;
            padding: 120px 40px;
        }""",
    html
)

html = re.sub(
    r'\.testimonial \.container\s*\{[^}]+\}',
    r""".testimonial .container {
            max-width: 720px;
            text-align: center;
            margin: 0 auto;
        }""",
    html
)

html = re.sub(
    r'\.quote-mark\s*\{[^}]+\}',
    r""".quote-mark {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: 140px;
            line-height: 0.5;
            color: #E8E6E0;
            display: block;
            margin-bottom: 36px;
            letter-spacing: -0.05em;
        }""",
    html
)

html = re.sub(
    r'\.testimonial-quote\s*\{[^}]+\}',
    r""".testimonial-quote {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: clamp(20px, 2.5vw, 30px);
            font-style: italic;
            line-height: 1.5;
            color: #0C0C0A;
            letter-spacing: -0.02em;
            margin-bottom: 36px;
        }""",
    html
)

html = re.sub(
    r'\.testimonial-name\s*\{[^}]+\}',
    r""".testimonial-name {
            font-size: 14px;
            font-weight: 500;
            color: #0C0C0A;
        }""",
    html
)

html = re.sub(
    r'\.testimonial-title\s*\{[^}]+\}',
    r""".testimonial-title {
            font-size: 13px;
            color: #9A9890;
        }""",
    html
)

html = html.replace('<span class="quote-mark">\"</span>', '<span class="quote-mark">“</span>')
html = html.replace('<span class="quote-mark">"</span>', '<span class="quote-mark">“</span>')

# FIX 10
html = re.sub(
    r'\.final-cta\s*\{\s*background:[^}]+}',
    r""".final-cta {
            background: #0C0C0A;
            padding: 140px 40px;
            text-align: center;
        }""",
    html
)

html = re.sub(
    r'\.final-cta h2\s*\{[^}]+\}',
    r""".final-cta h2 {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: clamp(36px, 5vw, 64px);
            font-weight: 400;
            color: #F5F4EF;
            letter-spacing: -0.03em;
            line-height: 1.08;
            margin-bottom: 18px;
        }""",
    html
)

html = re.sub(
    r'\.final-cta p\s*\{[^}]+\}',
    r""".final-cta p {
            font-size: 17px;
            color: #6E6E62;
            line-height: 1.65;
            margin-bottom: 44px;
            max-width: 440px;
            margin-left: auto;
            margin-right: auto;
        }""",
    html
)

html = re.sub(
    r'\.btn-light\s*\{[^}]+\}',
    r""".btn-light {
            background: #ffffff;
            color: #0C0C0A;
            font-size: 15px;
            font-weight: 500;
            padding: 14px 34px;
            border-radius: 9999px;
            border: none;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: background 0.2s, transform 0.2s;
        }""",
    html
)

html = re.sub(
    r'\.btn-light:hover\s*\{[^}]+\}',
    r""".btn-light:hover {
            background: #EFF6FF;
            transform: translateY(-2px);
        }""",
    html
)

html = re.sub(
    r'\.final-cta-note\s*\{[^}]+\}',
    r""".final-cta-note {
            margin-top: 18px;
            font-size: 13px;
            color: #4A4A42;
        }""",
    html
)

# FIX 11
html = re.sub(
    r'nav\s*\{[^}]+\}',
    r"""nav, #navbar {
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 200;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 44px;
            transition: background 0.3s ease, box-shadow 0.3s ease;
        }""",
    html
)

html = re.sub(
    r'nav\.scrolled\s*\{[^}]+\}',
    r"""nav.scrolled, #navbar.scrolled {
            background: rgba(240, 244, 255, 0.88);
            backdrop-filter: blur(24px) saturate(180%);
            -webkit-backdrop-filter: blur(24px) saturate(180%);
            box-shadow: 0 1px 0 #E8E6E0, 0 4px 24px rgba(0,0,0,0.04);
        }""",
    html
)

html = re.sub(
    r'\.nav-links a\s*\{[^}]+\}',
    r""".nav-links a {
            font-size: 14px;
            font-weight: 400;
            color: #6B7280;
            text-decoration: none;
            transition: color 0.2s;
            position: relative;
            padding-bottom: 2px;
        }
        
        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -2px; left: 0;
            width: 0; height: 1.5px;
            background: #0C0C0A;
            transition: width 0.25s ease;
        }""",
    html
)

html = re.sub(
    r'\.nav-links a:hover\s*\{[^}]+\}',
    r""".nav-links a:hover {
            color: #0C0C0A;
        }
        
        .nav-links a:hover::after {
            width: 100%;
        }""",
    html
)

# FIX 12
html = re.sub(
    r'\.btn-primary\s*\{[^}]+\}',
    r""".btn-primary {
            background: #0C0C0A;
            color: white;
            font-size: 14.5px;
            font-weight: 500;
            padding: 13px 28px;
            border-radius: 9999px;
            border: none;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: background 0.25s, transform 0.2s, box-shadow 0.2s;
        }""",
    html
)

html = re.sub(
    r'\.btn-primary:hover\s*\{[^}]+\}',
    r""".btn-primary:hover {
            background: #2563EB;
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(37,99,235,0.28);
        }""",
    html
)

html = re.sub(
    r'\.btn-ghost\s*\{[^}]+\}',
    r""".btn-ghost {
            background: transparent;
            color: #0C0C0A;
            font-size: 14.5px;
            font-weight: 500;
            padding: 12px 28px;
            border-radius: 9999px;
            border: 1.5px solid #D0CEC6;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: border-color 0.2s, background 0.2s, transform 0.2s;
        }""",
    html
)

html = re.sub(
    r'\.btn-ghost:hover\s*\{[^}]+\}',
    r""".btn-ghost:hover {
            border-color: #0C0C0A;
            background: rgba(0,0,0,0.03);
            transform: translateY(-1px);
        }""",
    html
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
