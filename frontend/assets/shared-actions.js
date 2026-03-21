// ── TOAST NOTIFICATION ──
function showToast(msg, type) {
  const existing = document.getElementById('toast-msg');
  if (existing) existing.remove();
  const t = document.createElement('div');
  t.id = 'toast-msg';
  t.textContent = msg;
  t.style.cssText = `
    position:fixed;bottom:28px;right:28px;z-index:9999;
    padding:12px 20px;border-radius:10px;font-size:14px;
    font-weight:500;font-family:'DM Sans',sans-serif;
    box-shadow:0 4px 24px rgba(0,0,0,0.12);
    background:${type==='error'?'#FEF2F2':type==='warn'?'#FFFBEB':'#ECFDF5'};
    color:${type==='error'?'#991B1B':type==='warn'?'#92400E':'#065F46'};
    border:1px solid ${type==='error'?'#FECACA':type==='warn'?'#FDE68A':'#A7F3D0'};
    animation:slideUp .25s ease;
  `;
  document.body.appendChild(t);
  setTimeout(() => t.style.opacity='0', 2500);
  setTimeout(() => t.remove(), 2800);
}

// ── CONFIRM MODAL ──
function showConfirm(title, message, onConfirm) {
  const existing = document.getElementById('confirm-modal');
  if (existing) existing.remove();
  const overlay = document.createElement('div');
  overlay.id = 'confirm-modal';
  overlay.style.cssText = `
    position:fixed;inset:0;background:rgba(0,0,0,0.45);
    z-index:10000;display:flex;align-items:center;
    justify-content:center;`;
  overlay.innerHTML = `
    <div style="background:#fff;border-radius:16px;padding:32px;
         max-width:420px;width:90%;box-shadow:0 24px 64px rgba(0,0,0,0.15)">
      <h3 style="font-family:'DM Serif Display',serif;font-size:22px;
           color:#0A0A0A;margin-bottom:10px">${title}</h3>
      <p style="font-size:14px;color:#6B7280;margin-bottom:24px;
           line-height:1.6">${message}</p>
      <div style="display:flex;gap:10px;justify-content:flex-end">
        <button onclick="document.getElementById('confirm-modal').remove()"
          style="padding:9px 20px;border-radius:99px;border:1.5px solid #E8E6E0;
          background:transparent;font-size:14px;font-weight:500;cursor:pointer;
          color:#6B7280">Cancel</button>
        <button id="confirm-ok"
          style="padding:9px 20px;border-radius:99px;border:none;
          background:#0A0A0A;color:#fff;font-size:14px;font-weight:500;
          cursor:pointer">Confirm</button>
      </div>
    </div>`;
  document.body.appendChild(overlay);
  document.getElementById('confirm-ok').onclick = () => {
    overlay.remove();
    onConfirm();
  };
  overlay.onclick = (e) => { if(e.target===overlay) overlay.remove(); };
}

// ── ADD TOOL MODAL ──
function showAddToolModal(onSave) {
  const existing = document.getElementById('add-tool-modal');
  if (existing) existing.remove();
  const overlay = document.createElement('div');
  overlay.id = 'add-tool-modal';
  overlay.style.cssText = `
    position:fixed;inset:0;background:rgba(0,0,0,0.45);
    z-index:10000;display:flex;align-items:center;justify-content:center;`;
  overlay.innerHTML = `
    <div style="background:#fff;border-radius:16px;padding:32px;
         max-width:480px;width:90%;box-shadow:0 24px 64px rgba(0,0,0,0.15)">
      <h3 style="font-family:'DM Serif Display',serif;font-size:22px;
           color:#0A0A0A;margin-bottom:24px">Add new tool</h3>
      <div style="display:flex;flex-direction:column;gap:14px">
        <div>
          <label style="font-size:12px;font-weight:500;color:#6B7280;
              text-transform:uppercase;letter-spacing:.07em;
              display:block;margin-bottom:6px">Tool name *</label>
          <input id="tool-name" placeholder="e.g. Salesforce"
            style="width:100%;padding:10px 14px;border:1px solid #E8E6E0;
            border-radius:8px;font-size:14px;outline:none;
            font-family:'DM Sans',sans-serif;box-sizing:border-box">
        </div>
        <div>
          <label style="font-size:12px;font-weight:500;color:#6B7280;
              text-transform:uppercase;letter-spacing:.07em;
              display:block;margin-bottom:6px">Category</label>
          <select id="tool-category"
            style="width:100%;padding:10px 14px;border:1px solid #E8E6E0;
            border-radius:8px;font-size:14px;font-family:'DM Sans',sans-serif;box-sizing:border-box">
            <option>CRM</option><option>Communication</option>
            <option>Design</option><option>Dev</option>
            <option>Productivity</option><option>Marketing</option>
            <option>HR</option><option>Finance</option>
            <option>Security</option><option>Video</option>
            <option>Other</option>
          </select>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <div>
            <label style="font-size:12px;font-weight:500;color:#6B7280;
                text-transform:uppercase;letter-spacing:.07em;
                display:block;margin-bottom:6px">Monthly cost ($)</label>
            <input id="tool-cost" type="number" placeholder="0"
              style="width:100%;padding:10px 14px;border:1px solid #E8E6E0;
              border-radius:8px;font-size:14px;font-family:'DM Sans',sans-serif;box-sizing:border-box">
          </div>
          <div>
            <label style="font-size:12px;font-weight:500;color:#6B7280;
                text-transform:uppercase;letter-spacing:.07em;
                display:block;margin-bottom:6px">Seat count</label>
            <input id="tool-seats" type="number" placeholder="0"
              style="width:100%;padding:10px 14px;border:1px solid #E8E6E0;
              border-radius:8px;font-size:14px;font-family:'DM Sans',sans-serif;box-sizing:border-box">
          </div>
        </div>
        <div>
          <label style="font-size:12px;font-weight:500;color:#6B7280;
              text-transform:uppercase;letter-spacing:.07em;
              display:block;margin-bottom:6px">Renewal date</label>
          <input id="tool-renewal" type="date"
            style="width:100%;padding:10px 14px;border:1px solid #E8E6E0;
            border-radius:8px;font-size:14px;font-family:'DM Sans',sans-serif;box-sizing:border-box">
        </div>
      </div>
      <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:24px">
        <button onclick="document.getElementById('add-tool-modal').remove()"
          style="padding:9px 20px;border-radius:99px;border:1.5px solid #E8E6E0;
          background:transparent;font-size:14px;font-weight:500;cursor:pointer;
          color:#6B7280">Cancel</button>
        <button id="save-tool-btn"
          style="padding:9px 20px;border-radius:99px;border:none;
          background:#0A0A0A;color:#fff;font-size:14px;font-weight:500;
          cursor:pointer">Add tool</button>
      </div>
    </div>`;
  document.body.appendChild(overlay);
  overlay.onclick = (e) => { if(e.target===overlay) overlay.remove(); };
  document.getElementById('save-tool-btn').onclick = async () => {
    const name = document.getElementById('tool-name').value.trim();
    if (!name) { showToast('Tool name is required','error'); return; }
    const btn = document.getElementById('save-tool-btn');
    btn.textContent = 'Saving...';
    btn.disabled = true;
    await onSave({
      name,
      category: document.getElementById('tool-category').value,
      monthly_cost: parseFloat(document.getElementById('tool-cost').value)||0,
      seat_count:   parseInt(document.getElementById('tool-seats').value)||0,
      renewal_date: document.getElementById('tool-renewal').value||null,
    });
    overlay.remove();
  };
}

// ── EXPORT CSV ──
function exportCSV(data, filename) {
  if (!data || !data.length) {
    showToast('No data to export','warn'); return;
  }
  const headers = Object.keys(data[0]);
  const rows    = data.map(r =>
    headers.map(h => JSON.stringify(r[h]??'')).join(',')
  );
  const csv  = [headers.join(','), ...rows].join('\n');
  const blob = new Blob([csv], { type:'text/csv' });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href     = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
  showToast('CSV downloaded ✓','success');
}

// Toast animation
const style = document.createElement('style');
style.textContent = `
  @keyframes slideUp {
    from { opacity:0; transform:translateY(12px); }
    to   { opacity:1; transform:translateY(0); }
  }
`;
document.head.appendChild(style);
