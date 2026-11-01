/* HỌC ĐỂ LÀM GÌ — math-format.js
   Hiển thị công thức trong game dạng toán học: a/b → phân số dọc, √(…) → căn có gạch trên, x_A → chỉ số dưới, x^2 → mũ.
   Chỉ đổi cách HIỂN THỊ: ký tự gốc ("/", "_", "(", ")") vẫn nằm trong DOM (ẩn đi) nên textContent không đổi —
   hiệu ứng gõ chữ, so sánh chuỗi… của game vẫn chạy bình thường. Tắt: thêm class "no-math" vào phần tử. */
(function () {
  if (window.HDLGMath) return;
  var PUA = 0xE000, OP_CH = "0-9A-Za-z\\u0391-\\u03A9\\u03B1-\\u03C9\\u00B5\\u0394\\u03A3\\u2032'\\u00B2\\u00B3\\u00B9\\u2070-\\u209C\\u02B0-\\u02FF\\u1D00-\\u1DBF\\u20D7\\u0302\\u0305\\u0110\\u0111|\u221A\u221B\\uE000-\\uE8FF";
  var UNITS = /^(?:[kMGmμunp]?(?:m|g|s|N|J|W|Wh|V|A|Ω|C|K|Pa|Hz|L|T|Wb|F|H|eV|mol|rad|atm|bar|cal|lm|lx|dB|h|min|ph|đ)|cm|dm|mm|km|kWh|°C|°|%|u|ns|ms|vòng|phút|giây|bao|lít|ly|tr|ph|Bq|ngày|tháng|năm|người|lần)(?:[²³]|⁻¹|⁻²)?$/;
  var WORD_OK = /^(?:sin|cos|tan|cot|log|lg|ln|exp|max|min|lim|Fms|Fmax|Fmin|Fht|Fđh|Fdh|Fk|Fq|Fc|Fhd|Fmst|Fmsn|vmax|vmin|Imax|Umax|Wđ|Wt|Wd)$/;
  var COUNTER = /(?:chặng|câu|màn|lượt|vòng|bước|đề|ải|level|lv|ngày|tầng|lần|đợt|mục|nhiệm vụ|đơn|khách|trận|round|stage|gợi ý|sao|tim|mạng|đúng|xong|hoàn thành|tiến độ|đã|còn|điểm|phần|trang|bài|chuyến|ca|ván|cấp|thẻ|hộp|kho|mẫu|giờ|phút|giây|[:#№]|\p{Extended_Pictographic}\uFE0F?)\s*$/iu;
  /* Số/số chỉ thành phân số khi đứng trong ngữ cảnh công thức (sau =, ·, ≈, "bằng", "khoảng"…) — tránh bộ đếm "Chặng 1/3" */
  var MATHW = /(?:^|\s)(?:bằng|là|khoảng|mỗi|tốn|chiếm|gấp|có|đến|từ|trong|còn|hay|hoặc|và|chỉ|giảm|tăng|lấy|nhân|chia|cỡ|tầm|gần|hơn|thêm|bớt|được|mất)$/i;
  function mathCtx(b, paren) {
    if (COUNTER.test(b)) return false;
    if (/[=≈≥≤<>×+−*÷^\[;]\s*$/.test(b) || /[·\-]$/.test(b)) return true;
    if (paren && /[0-9A-Za-z\u0391-\u03C9\u0394\u03A3√∛\uE000-\uE8FF]$/.test(b)) return true; // ρ(4/3), arcsin(1/n)
    return MATHW.test(b.replace(/\s+$/, ""));
  }
  var ESC = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" };
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return ESC[c]; }); }
  var H = "<span class=\"mf-h\">";

  function okOperand(s) {
    var core = s.replace(/[\uE000-\uE8FF]/g, "x");
    if (!/[0-9A-Za-z\u0391-\u03C9\u0394\u03A3\uE000-\uE8FF]/.test(s)) return false;
    var runs = core.match(/[A-Za-z]{3,}/g) || [];
    for (var i = 0; i < runs.length; i++) if (!WORD_OK.test(runs[i])) return false;
    return core.length <= 16;
  }
  function isUnit(s) {
    s = s.replace(/^\(|\)$/g, "");
    var p = s.split(/[·.]/);
    for (var i = 0; i < p.length; i++) if (!UNITS.test(p[i])) return false;
    return true;
  }
  /* Bóc ngoặc ngoài cùng (nếu ngoặc bao trọn biểu thức) — vẫn giữ ký tự ngoặc trong DOM nhưng ẩn */
  function strip(s, render) {
    if (s[0] === "(" && s[s.length - 1] === ")") {
      var d = 0, whole = true;
      for (var i = 0; i < s.length; i++) { if (s[i] === "(") d++; else if (s[i] === ")") { d--; if (d === 0 && i < s.length - 1) { whole = false; break; } } }
      if (whole) return H + "(</span>" + render(s.slice(1, -1)) + H + ")</span>";
    }
    return render(s);
  }

  function convert(text) {
    if (!/[\/_√^]/.test(text)) return null;
    var slots = [], changed = false;
    function slot(html) { slots.push(html); return String.fromCharCode(PUA + slots.length - 1); }
    function subsup(s) { // chỉ số dưới / mũ → ô giữ chỗ (để dùng được trong tử/mẫu)
      return s
        .replace(/(^|[^A-Za-z0-9_\u00C0-\u1EF9])([A-Za-z\u0391-\u03C9\u0394\u03A3])_(\{([^{}]{1,8})\}|[A-Za-z0-9\u00C0-\u1EF9\u0391-\u03C9]{1,7})(?![A-Za-z0-9_\u00C0-\u1EF9])/g, function (m, a, b, c, d) {
          changed = true; return a + b + slot(H + "_" + (d != null ? "{" : "") + "</span><sub>" + esc(d != null ? d : c) + "</sub>" + (d != null ? H + "}</span>" : "")); })
        .replace(/([A-Za-z0-9)\u0391-\u03C9\u00B2\u00B3\uE000-\uE8FF])\^(\(([^()]{1,10})\)|-?[0-9]{1,3}|[A-Za-z])/g, function (m, a, b, c) {
          changed = true; return a + slot(H + "^" + (c != null ? "(" : "") + "</span><sup>" + esc(c != null ? c : b) + "</sup>" + (c != null ? H + ")</span>" : "")); });
    }
    function inline(s) { // HTML-escape + thay ô giữ chỗ (lồng nhau) bằng HTML
      var out = esc(s), k = 0;
      while (/[\uE000-\uE8FF]/.test(out) && k++ < 6) out = out.replace(/[\uE000-\uE8FF]/g, function (c) { return slots[c.charCodeAt(0) - PUA]; });
      return out;
    }
    function fracs(s, inMath) {
      // 1) căn: √(…) (ngoặc lồng nhau)
      var i;
      while ((i = s.indexOf("√(")) >= 0) {
        var d = 0, j = i + 1;
        for (; j < s.length; j++) { if (s[j] === "(") d++; else if (s[j] === ")") { d--; if (!d) break; } }
        if (j >= s.length) break;
        var inner = s.slice(i + 2, j);
        changed = true;
        s = s.slice(0, i) + slot("<span class=\"mf-sq\"><span class=\"mf-rs\">√</span>" + H + "(</span><span class=\"mf-rad\">" + fracs(inner, true) + "</span>" + H + ")</span></span>") + s.slice(j + 1);
      }
      // 2) ngoặc chứa phân số bên trong → xử lý trước để có thể làm tử/mẫu
      s = s.replace(/\(([^()]{1,60})\)/g, function (m, inner, off, all) {
        if (inner.indexOf("/") < 0) return m;
        var r = fracs(inner, inMath || mathCtx(all.slice(Math.max(0, off - 30), off), true)); if (r === esc(inner)) return m;
        return slot(H + "(</span>" + r + H + ")</span>");
      });
      // 3) phân số a/b
      var NUM = "(\\([^()]{1,40}\\)|[" + OP_CH + "·.,]{1,18})", DEN = "(\\([^()]{1,40}\\)|[" + OP_CH + ",.]{1,16})";
      var re = new RegExp("(^|[^" + OP_CH + "·.,/\\u00C0-\\u1EF9])" + NUM + "\\/" + DEN + "(?![.,]?[" + OP_CH + "/\\u00C0-\\u1EF9]|-[A-Za-z])", "g");
      s = s.replace(re, function (m, pre, a, b, off, all) {
        a = a.replace(/^[.,·]+/, function (x) { pre += x; return ""; });
        var tail = ""; b = b.replace(/[.,]+$/, function (x) { tail = x; return ""; });
        if (!a || !b || !okOperand(a) || !okOperand(b)) return m;
        if (isUnit(b) && (isUnit(a) || /\d\s*$/.test(pre))) return m;
        if (/^\d+$/.test(a) && /^\d{4}$/.test(b)) return m; // ngày tháng, năm
        if (/^\d+$/.test(a) && /^\d+[A-Za-zΩ°%]+$/.test(b)) return m; // 0/900N (bộ đếm có đơn vị)
        if (/^\d+$/.test(a) && /^\d+$/.test(b) && !inMath && !mathCtx(all.slice(Math.max(0, off - 30), off) + pre)) return m; // Chặng 1/3, Đã nối 2/8… (chỉ đổi khi đứng trong công thức)
        if (/^(?:ph|ly|tr|ngày|tháng|năm|người|lần|bao|lít|hộp|chuyến|kWh|Wh)$/.test(b)) return m; // vòng/ph, 9k/ly, đ/kWh…
        if (/^[A-Z]{2,}$/.test(a) && /^[A-Z]{2,}$/.test(b)) return m; // AC/DC, PET/CT
        changed = true;
        return pre + slot("<span class=\"mf-fr\"><span class=\"mf-n\">" + strip(a, inline) + "</span>" + H + "/</span><span class=\"mf-d\">" + strip(b, inline) + "</span></span>") + tail;
      });
      return inline(s);
    }
    var html = fracs(subsup(text));
    return changed ? html : null;
  }

  var CSS = ".mf-fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;font-size:.9em;line-height:1.12;margin:0 .1em;text-align:center}" +
    ".mf-n{padding:0 .18em}.mf-d{padding:0 .18em;border-top:1.4px solid currentColor;align-self:stretch}" +
    ".mf-h{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;opacity:0;font-size:0}" +
    ".mf-sq{display:inline-flex;align-items:stretch;white-space:nowrap}.mf-rs{font-size:1.1em;line-height:1;align-self:center}" +
    ".mf-rad{border-top:1.4px solid currentColor;padding:0 .12em;display:inline-flex;align-items:center}" +
    ".mf-fr sub,.mf-fr sup,.mf-sq sub,.mf-sq sup{font-size:.72em}";

  var SKIP = /^(SCRIPT|STYLE|TEXTAREA|INPUT|SELECT|OPTION|TITLE|CODE|PRE|CANVAS|NOSCRIPT|svg|text|tspan)$/;
  function skipEl(el) {
    for (var e = el; e && e.nodeType === 1; e = e.parentNode) {
      if (SKIP.test(e.nodeName) || e.isContentEditable) return true;
      var c = e.className; if (typeof c === "string" && (c.indexOf("no-math") >= 0 || c.indexOf("mf-") >= 0)) return true;
    }
    return false;
  }
  var tpl = document.createElement("template");
  function doText(t) {
    var p = t.parentNode; if (!p || skipEl(p)) return;
    var v = t.nodeValue; if (!v || v.length > 4000) return;
    var h = convert(v); if (h == null) return;
    tpl.innerHTML = h; p.replaceChild(tpl.content, t);
  }
  function walk(n) {
    if (n.nodeType === 3) return doText(n);
    if (n.nodeType !== 1 || skipEl(n)) return;
    var w = document.createTreeWalker(n, 4), a = [], t; while ((t = w.nextNode())) a.push(t);
    for (var i = 0; i < a.length; i++) doText(a[i]);
  }
  var queue = [], sched = false, mo;
  function flush() {
    sched = false; var q = queue; queue = [];
    for (var i = 0; i < q.length; i++) if (q[i].isConnected) walk(q[i]);
    if (mo) mo.takeRecords();
  }
  function push(n) { queue.push(n); if (!sched) { sched = true; (window.queueMicrotask || setTimeout)(flush); } }
  function start() {
    var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
    walk(document.body);
    mo = new MutationObserver(function (rs) {
      for (var i = 0; i < rs.length; i++) {
        var r = rs[i];
        if (r.type === "characterData") push(r.target);
        else for (var k = 0; k < r.addedNodes.length; k++) push(r.addedNodes[k]);
      }
    });
    mo.observe(document.body, { childList: true, subtree: true, characterData: true });
  }
  window.HDLGMath = { convert: convert, render: walk };
  if (document.body) start(); else document.addEventListener("DOMContentLoaded", start);
})();
