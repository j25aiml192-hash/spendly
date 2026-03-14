import os
import re

dir_path = r'c:\trialspendly\spendly'
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# We'll use regex to target the anchor text exactly in the footer area to avoid touching anything in the nav or body
def update_footer_links():
    for file in files:
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Isolate footer strictly so we only replace links inside
        footer_match = re.search(r'(<footer.*?>)(.*?)(</footer>)', content, re.DOTALL | re.IGNORECASE)
        if not footer_match:
            continue
            
        footer_start = footer_match.group(1)
        footer_body = footer_match.group(2)
        footer_end = footer_match.group(3)
        
        # Link updates
        # Changelog -> /insights
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Changelog</a>', r'href="insights.html"\1>Changelog</a>', footer_body)
        
        # Careers -> /about
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Careers</a>', r'href="about.html"\1>Careers</a>', footer_body)
        
        # Blog -> /insights  
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Blog</a>', r'href="insights.html"\1>Blog</a>', footer_body)
        
        # Contact -> mailto:hello@spendly.io
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Contact</a>', r'href="mailto:hello@spendly.io"\1>Contact</a>', footer_body)
        
        # Legal: Privacy, Terms, Security, SOC 2 -> /about
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Privacy</a>', r'href="about.html"\1>Privacy</a>', footer_body)
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Terms</a>', r'href="about.html"\1>Terms</a>', footer_body)
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>Security</a>', r'href="about.html"\1>Security</a>', footer_body)
        footer_body = re.sub(r'href=["\'](?:#|/?)["\']([^>]*)>SOC 2</a>', r'href="about.html"\1>SOC 2</a>', footer_body)

        # Reconstruct and overwrite
        new_content = content[:footer_match.start()] + footer_start + footer_body + footer_end + content[footer_match.end():]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == '__main__':
    update_footer_links()
