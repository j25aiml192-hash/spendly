import os

dir_path = r'c:\trialspendly\spendly'
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

css_patch = """
    /* Fix dashboard overflow */
    .dashboard-container, .main-content { margin-left: 0 !important; width: 100% !important; box-sizing: border-box !important; overflow-x: hidden !important; }
    
    /* Stack hero buttons */
    #hero .buttons { flex-direction: column !important; width: 100% !important; gap: 12px !important; }
    #hero .buttons a { width: 100% !important; text-align: center !important; box-sizing: border-box !important; }
    
    /* Clean up navbar */
    nav .button { display: none !important; }
    
    /* Fix wrapper sizing */
    html, body { max-width: 100vw !important; overflow-x: hidden !important; }
"""

def patch_mobile_css():
    for file in files:
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if '/* Fix dashboard overflow */' not in content:
            # Inject right before the closing bracket of the @media (max-width: 768px) {} query
            # A simple approach is just appending it right before </style> since the existing block already handles it OR finding the closing bracket
            # Since previously we appended near </style>, we can just append a new @media block
            
            patch_full = f"\n  @media (max-width: 768px) {{{css_patch}}}\n</style>"
            content = content.replace('</style>', patch_full)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    patch_mobile_css()
