import os
import re

frontend_dir = r"c:\trialspendly\spendly\frontend"

html_files = [f for f in os.listdir(frontend_dir) if f.endswith(".html")]

pages = ["features", "insights", "pricing", "about", "dashboard", "inventory", "license", "spend", "renewals", "duplicates", "optimization", "cfo", "settings"]
page_pattern = re.compile(r'href="/(' + '|'.join(pages) + r')(?:"|#|\?)')

for file in html_files:
    filepath = os.path.join(frontend_dir, file)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix /assets/ to assets/
    content = content.replace('href="/assets/', 'href="assets/')
    content = content.replace('src="/assets/', 'src="assets/')
    
    # Fix root page links (e.g. href="/features" -> href="features.html")
    for page in pages:
        content = content.replace(f'href="/{page}"', f'href="{page}.html"')
        
    # Fix absolute root link
    content = content.replace('href="/"', 'href="index.html"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Paths fixed successfully.")
