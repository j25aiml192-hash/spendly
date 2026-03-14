import os
import re

dir_path = r'c:\trialspendly\spendly'

# Link target mappings based on inner text
link_mapping = {
    'product': 'features.html',
    'features': 'features.html',
    'pricing': 'pricing.html',
    'about': 'about.html',
    'insights': 'insights.html',
    
    'overview': 'dashboard.html',
    'dashboard': 'dashboard.html',
    'saas inventory': 'inventory.html',
    'inventory': 'inventory.html',
    'license optimizer': 'license.html',
    'license': 'license.html',
    'spend analytics': 'spend.html',
    'spend': 'spend.html',
    'renewal forecast': 'renewals.html',
    'renewals': 'renewals.html',
    'duplicate detector': 'duplicates.html',
    'duplicates': 'duplicates.html',
    'optimization actions': 'optimization.html',
    'optimization': 'optimization.html',
    'alerts': 'dashboard.html',
    'cfo view': 'cfo.html',
    'cfo': 'cfo.html',
    'settings': 'settings.html',
}

cta_mapping = {
    'request a demo': 'dashboard.html',
    'get started': 'dashboard.html',
    'start for free': 'dashboard.html'
}

def clean_class_attribute(a_tag):
    # Remove "active" from class
    # To do this safely, we find class="..."
    def css_repl(m):
        cls_content = m.group(1)
        # remove \bactive\b
        cls_content = re.sub(r'\bactive\b', '', cls_content)
        cls_content = re.sub(r'\s+', ' ', cls_content).strip()
        if cls_content:
            return f'class="{cls_content}"'
        else:
            return ''
    
    return re.sub(r'class\s*=\s*"([^"]*)"', css_repl, a_tag)

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)

    def repl(match):
        a_open = match.group(1)
        inner_html = match.group(2)
        a_close = match.group(3)
        
        inner_text = re.sub(r'<[^>]+>', '', inner_html).strip().lower()
        
        target_href = None
        
        # Mapping logic
        if 'class="logo"' in a_open or 'spendly' in inner_text:
            target_href = 'index.html'
        else:
            for k, v in link_mapping.items():
                if k == inner_text:
                    target_href = v
                    break
                    
        # CTA Check
        if not target_href:
            for k, v in cta_mapping.items():
                if k in inner_text:
                    target_href = v
                    break

        if not target_href:
            # Maybe inside pagination or something else we should not touch
            # But the prompt says "Replace every href="#" in navbars and sidebars with these exact paths"
            # If we don't know the path, leave it.
            pass
            
        if target_href:
            # Identify if it was href="#"
            # Wait, the prompt says "Replace every href="#" ...". 
            # If it already points to something, we might still want to ensure it is correct.
            # Easiest is just to replace whatever href is there with target_href.
            
            # Replace href
            if re.search(r'href\s*=\s*"[^"]*"', a_open):
                a_open = re.sub(r'href\s*=\s*"[^"]*"', f'href="{target_href}"', a_open)
            else:
                a_open = a_open.replace('<a', f'<a href="{target_href}"')
            
            # Identify buttons
            is_button = 'button' in a_open
            
            # Clean active from all matched links first
            a_open = clean_class_attribute(a_open)
            
            # Conditionally add active
            if target_href == filename and not is_button and 'logo' not in a_open:
                if 'class="' in a_open:
                    a_open = re.sub(r'class\s*=\s*"', 'class="active ', a_open)
                else:
                    a_open = a_open.replace('<a', '<a class="active"')

        return a_open + inner_html + a_close

    pattern = r'(<a\s+[^>]*>)(.*?)(</a>)'
    new_content = re.sub(pattern, repl, content, flags=re.DOTALL | re.IGNORECASE)
    
    # cleanup double spaces that might have been introduced
    new_content = new_content.replace('  ', ' ')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

for f in os.listdir(dir_path):
    if f.endswith('.html'):
        process_html_file(os.path.join(dir_path, f))
        print(f"Processed {f}")
