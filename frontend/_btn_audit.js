const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = [
  'dashboard.html', 'inventory.html', 'license.html',
  'spend.html', 'renewals.html', 'duplicates.html',
  'optimization.html', 'cfo.html', 'settings.html'
];

function extractAttr(tag, attr) {
  // Match attr="value" or attr='value'
  const re = new RegExp(`${attr}\\s*=\\s*(?:"([^"]*)"|'([^']*)')`, 'i');
  const m = tag.match(re);
  return m ? (m[1] || m[2] || '') : null;
}

function extractText(tag, afterContent) {
  // Get inner text between > and </ or next <
  // afterContent is the content after the opening tag
  if (!afterContent) return '';
  // Remove nested tags to get text
  const text = afterContent.replace(/<[^>]*>/g, '').trim();
  // Truncate
  return text.substring(0, 120);
}

for (const file of files) {
  const filePath = path.join(dir, file);
  if (!fs.existsSync(filePath)) {
    console.log(`\n=== ${file} === (FILE NOT FOUND)`);
    continue;
  }
  
  const content = fs.readFileSync(filePath, 'utf-8');
  console.log(`\n=== ${file} ===`);
  
  // Find all <button ...>...</button> and <a ...>...</a> with class="button" or btn or href
  // Also find elements with onclick
  
  // Strategy: find all <button and <a tags
  const tagRegex = /<(button|a)\b([^>]*)>([\s\S]*?)(?:<\/\1>)/gi;
  
  let match;
  let count = 0;
  const seen = new Set();
  
  while ((match = tagRegex.exec(content)) !== null) {
    const tagName = match[1].toLowerCase();
    const attrs = match[2];
    const innerRaw = match[3];
    
    const id = extractAttr('<x ' + attrs + '>', 'id');
    const cls = extractAttr('<x ' + attrs + '>', 'class');
    const onclick = extractAttr('<x ' + attrs + '>', 'onclick');
    const href = extractAttr('<x ' + attrs + '>', 'href');
    const datLucide = extractAttr('<x ' + attrs + '>', 'data-lucide');
    
    // Get visible text
    let text = innerRaw.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
    if (text.length > 100) text = text.substring(0, 100) + '...';
    
    // Skip nav links that are just page navigation (sidebar items etc)
    // but keep buttons and action links
    
    // For <a> tags - only include if they have a class with button/btn, or onclick, or are in sidebar
    if (tagName === 'a') {
      const isButton = cls && (cls.includes('button') || cls.includes('btn'));
      const hasOnclick = !!onclick;
      const isSidebar = cls && cls.includes('active');
      const isLogo = cls && cls.includes('logo');
      // Skip plain nav links, sidebar links, logo
      if (!isButton && !hasOnclick && !isSidebar && !isLogo) continue;
      if (isLogo) continue; // skip logo
      // Skip sidebar nav links
      if (href && !isButton && !hasOnclick) {
        // It's a navigation link, check if sidebar
        const isSidebarLink = cls && cls.includes('active');
        if (!isSidebarLink) continue;
      }
    }
    
    // Create unique key to avoid dups
    const key = `${tagName}|${text}|${id}|${onclick}|${href}`;
    if (seen.has(key)) continue;
    seen.add(key);
    
    count++;
    console.log(`\nButton #${count}: "${text || '(no text)'}"`);
    console.log(`  tag: <${tagName}>`);
    if (id) console.log(`  id: ${id}`);
    if (cls) console.log(`  class: ${cls}`);
    if (onclick) console.log(`  onclick: ${onclick}`);
    if (href) console.log(`  href: ${href}`);
    
    // Determine what it currently does
    let currently = '';
    if (onclick) {
      currently = `calls ${onclick}`;
    } else if (href && href !== '#' && href !== 'javascript:void(0)') {
      currently = `navigates to ${href}`;
    } else if (href === '#') {
      currently = 'href="#" (nothing)';
    } else {
      currently = 'nothing (no handler)';
    }
    console.log(`  currently: ${currently}`);
  }
  
  // Also find inline onclick on non-button/a elements like divs, trs, etc
  const onclickRegex = /<(?!button|a\b|\/)([\w-]+)\b([^>]*onclick\s*=\s*"([^"]*)"[^>]*)>/gi;
  let ocMatch;
  while ((ocMatch = onclickRegex.exec(content)) !== null) {
    const tagName = ocMatch[1];
    const attrs = ocMatch[0];
    const onclickVal = ocMatch[3];
    
    const id = extractAttr(attrs, 'id');
    const cls = extractAttr(attrs, 'class');
    
    // Get surrounding text - look up to 200 chars ahead for inner text
    const afterPos = onclickRegex.lastIndex;
    const snippet = content.substring(afterPos, afterPos + 200);
    let text = snippet.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
    if (text.length > 80) text = text.substring(0, 80) + '...';
    
    const key = `${tagName}|${onclickVal}|${id}`;
    if (seen.has(key)) continue;
    seen.add(key);
    
    count++;
    console.log(`\nButton #${count}: "${text || '(no text)'}"`);
    console.log(`  tag: <${tagName}> (with onclick)`);
    if (id) console.log(`  id: ${id}`);
    if (cls) console.log(`  class: ${cls}`);
    console.log(`  onclick: ${onclickVal}`);
    console.log(`  currently: calls ${onclickVal}`);
  }
  
  if (count === 0) {
    console.log('  (no buttons or clickable elements found)');
  }
  console.log(`\nTotal clickable elements: ${count}`);
}
