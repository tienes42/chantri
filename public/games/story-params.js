/* HỌC ĐỂ LÀM GÌ — story-params.js (Nâng cấp theo CT GDPT 2018)
   1. Bổ sung vào cốt truyện mở đầu (#introStory):
      - 📘 Lý thuyết & Công thức trọng tâm (theo bài học mới)
      - 🎯 Chốt nhiệm vụ (Đọc xong cốt truyện cần làm gì?)
   2. Bổ sung vào hội thoại mỗi chặng (GM.stageLines / stageLines):
      - 📊 Thông số để tính toán: toàn bộ số liệu, hằng số (r, T, m, U, I, R, f…), giới hạn an toàn của chặng.
      - 📐 Công thức & cách tính (theo bài học mới): công thức áp dụng và hướng thay số cụ thể của chặng.
      - 🎯 Chốt lại nhiệm vụ (Cần làm gì): chỉ rõ cần chỉnh thanh trượt / núm xoay / linh kiện nào và bấm nút nào để chạy.
   3. Mở khóa miễn phí Gợi ý 1 (Cách lập luận & công thức) và hiển thị nút "📋 Thông số & Nhiệm vụ" ngay trong màn chơi. */
(function () {
  "use strict";
  if (window.__hdlgStoryParams) return;
  window.__hdlgStoryParams = true;

  function G(n) {
    try { return Function("return typeof " + n + " !== 'undefined' ? " + n + " : undefined")(); }
    catch (e) { return undefined; }
  }
  function $(id) { return document.getElementById(id); }

  function cleanHtml(s) {
    if (!s) return "";
    return String(s)
      .replace(/<br\s*\/?>/gi, " · ")
      .replace(/<sub>([^<]+)<\/sub>/gi, "_$1")
      .replace(/<sup>([^<]+)<\/sup>/gi, "^($1)")
      .replace(/<\/?b[^>]*>/gi, "")
      .replace(/<\/?[a-z][^>]*>/gi, "")
      .replace(/&nbsp;/g, " ")
      .replace(/&amp;/g, "&")
      .replace(/&lt;/g, "<")
      .replace(/&gt;/g, ">")
      .replace(/\s+/g, " ")
      .trim();
  }

  /* Ghi lại các dòng "• …" đang được vẽ trên canvas (bảng số liệu của chặng) */
  var bullets = new Map();
  var CP = window.CanvasRenderingContext2D && CanvasRenderingContext2D.prototype;
  if (CP && CP.fillText && !CP.fillText.__sp) {
    var ft = CP.fillText;
    CP.fillText = function (t) {
      if (typeof t === "string" && t.charCodeAt(0) === 0x2022 && /\d/.test(t) && t.length < 220) {
        bullets.set(t, Date.now());
        if (bullets.size > 120) bullets.delete(bullets.keys().next().value);
      }
      return ft.apply(this, arguments);
    };
    CP.fillText.__sp = true;
  }
  var HOWTO = /^•\s*(Đã|Bấm|Kéo|Nhấn|Chạm|Chọn|Gạt|Xoay|Thả|Mở|Đóng|Đặt|Click|Hãy)\b/i;
  function boardNow() {
    var now = Date.now(), out = [];
    bullets.forEach(function (t, s) {
      if (now - t < 1500 && !HOWTO.test(s)) out.push(s.replace(/^•\s*/, "").trim());
    });
    return out.slice(0, 8);
  }

  /* Trích xuất thông tin đầy đủ của chặng hiện tại */
  function extractStageGuide() {
    var GM = G("GM"), S = G("S"), KDc = G("KDc"), KD = G("KD");
    var updateAux = G("updateAux"), updateHUD = G("updateHUD");
    if (typeof updateAux === "function") { try { updateAux(); } catch (e) {} }
    if (typeof updateHUD === "function") { try { updateHUD(); } catch (e) {} }

    var c = (S && S.cfg) || {};
    var kd = null;
    try {
      if (typeof KDc === "function") kd = KDc();
      else if (Array.isArray(KD) && c && typeof c.i === "number") kd = KD[c.i];
    } catch (e) { kd = null; }

    /* 1. Thông số để tính toán */
    var paramParts = [];
    var l1 = "";
    try {
      var h = GM && typeof GM.hud === "function" ? GM.hud() : null;
      if (h && typeof h.l1 === "string") l1 = h.l1;
      else if (kd && typeof kd.h1 === "function") l1 = kd.h1(c);
      else if ($("telemetryLine1")) l1 = $("telemetryLine1").textContent || "";
    } catch (e) {}
    l1 = cleanHtml(l1).replace(/^[^0-9A-Za-zÀ-ỹΔλμρπΩ]+/, "").trim();
    if (l1) paramParts.push(l1);

    try {
      if (kd && typeof kd.info === "function") {
        var inf = kd.info(c) || [];
        inf.forEach(function (item) {
          var s = cleanHtml(item).replace(/^•\s*/, "").trim();
          if (s && paramParts.join(" ").indexOf(s) < 0) paramParts.push(s);
        });
      }
    } catch (e) {}

    var bNow = boardNow();
    bNow.forEach(function (b) {
      if (b && paramParts.join(" ").indexOf(b) < 0) paramParts.push(b);
    });

    var paramsText = paramParts.join(" · ");
    if (!paramsText) paramsText = "Xem các số liệu hiển thị trên thanh trạng thái phía trên màn hình.";

    /* 2. Công thức & cách tính (từ Gợi ý 1 + điều kiện vùng xanh) */
    var greenText = "";
    try {
      if (GM && typeof GM.greenTag === "function") greenText = cleanHtml(GM.greenTag());
      else if (kd && kd.green) greenText = cleanHtml(kd.green);
    } catch (e) {}
    greenText = greenText.replace(/^🟢\s*/, "").trim();

    var hint1Text = "";
    try {
      var hts = null;
      if (GM && typeof GM.hintTexts === "function") hts = GM.hintTexts();
      else {
        var htFn = G("hintTexts");
        if (typeof htFn === "function") hts = htFn();
      }
      if (Array.isArray(hts) && hts[0]) hint1Text = cleanHtml(hts[0]);
      else if (kd && typeof kd.hint1 === "function") hint1Text = cleanHtml(kd.hint1(c));
      else if (kd && typeof kd.hints === "function") {
        var kh = kd.hints(c);
        if (Array.isArray(kh) && kh[0]) hint1Text = cleanHtml(kh[0]);
      }
    } catch (e) {}

    var formulaParts = [];
    if (greenText) formulaParts.push("Điều kiện đạt chuẩn: " + greenText);
    if (hint1Text && formulaParts.join(" ").indexOf(hint1Text) < 0) formulaParts.push("Hướng tính: " + hint1Text);
    var formulaText = formulaParts.join(" · ");
    if (!formulaText) formulaText = "Áp dụng công thức trọng tâm của bài học để tính giá trị phù hợp với thông số trên.";

    /* 3. Chốt lại nhiệm vụ (Cần chỉnh thông số gì, thao tác thế nào, bấm nút nào) */
    var pDesc = [];
    try {
      var P = (kd && Array.isArray(kd.P)) ? kd.P : null;
      if (P && P.length) {
        P.forEach(function (p) {
          if (!p || !p.lab) return;
          if (Array.isArray(p.opts) && p.opts.length) {
            var sample = p.opts.slice(0, 5).join(", ") + (p.opts.length > 5 ? "…" : "");
            pDesc.push(p.lab + " (" + sample + ")");
          } else if (p.min != null && p.max != null) {
            pDesc.push(p.lab + " (từ " + p.min + " đến " + p.max + (p.unit ? " " + p.unit : "") + ")");
          } else {
            pDesc.push(p.lab);
          }
        });
      }
    } catch (e) {}

    var chint = "";
    try {
      if (GM && typeof GM.controlHint === "function") chint = cleanHtml(GM.controlHint());
      else if (kd && kd.hint) chint = cleanHtml(kd.hint);
      else if ($("controlHint")) chint = cleanHtml($("controlHint").textContent);
    } catch (e) {}
    chint = chint.replace(/^[^\wÀ-ỹ]+/, "").trim();

    var execLabel = "Chạy thử ▶";
    try {
      if ($("executeBtnText") && $("executeBtnText").textContent.trim()) {
        execLabel = $("executeBtnText").textContent.trim();
      } else if (kd && kd.execLabel) {
        execLabel = kd.execLabel;
      } else if ($("btnExecuteStage") && $("btnExecuteStage").textContent.trim()) {
        execLabel = $("btnExecuteStage").textContent.trim();
      }
    } catch (e) {}

    var actionText = "Dựa vào thông số và công thức trên, bạn hãy tính giá trị cần thiết";
    if (pDesc.length) actionText += " rồi chỉnh [" + pDesc.join(" · ") + "]";
    if (chint) actionText += " (" + chint + ")";
    actionText += ". Sau khi chỉnh xong, bấm nút «" + execLabel + "» ở góc dưới để kiểm tra kết quả!";

    return {
      paramsText: paramsText,
      formulaText: formulaText,
      actionText: actionText,
      execLabel: execLabel
    };
  }

  window.__hdlgExtractStageGuide = extractStageGuide;

  /* Làm giàu mảng lời thoại của mỗi chặng */
  function enrichStageLines(L) {
    try {
      if (!Array.isArray(L) || !L.length) return L;
      if (L.some(function (x) { return x && x.__p; })) return L;

      /* Mở khóa miễn phí Gợi ý 1 (Cách lập luận & thông số) cho người chơi */
      var S = G("S");
      if (S && Array.isArray(S.hints) && typeof S.stage === "number") {
        if (!S.hints[S.stage] || S.hints[S.stage] < 1) S.hints[S.stage] = 1;
      }

      var who = L.some(function (x) { return x && x.who === "A"; }) ? "A"
              : L.some(function (x) { return x && x.who === "F"; }) ? "F"
              : (L[L.length - 1] && L[L.length - 1].who) || "A";

      var lParams = { who: who, __p: 1 };
      var lFormula = { who: who, __p: 1 };
      var lAction = { who: who, __p: 1 };
      var cached = null;
      function getG() {
        if (!cached) cached = extractStageGuide();
        return cached;
      }
      bullets.clear();

      Object.defineProperty(lParams, "text", {
        enumerable: true,
        get: function () { return "📊 Thông số để tính toán: " + getG().paramsText; }
      });
      Object.defineProperty(lFormula, "text", {
        enumerable: true,
        get: function () { return "📐 Công thức & cách tính: " + getG().formulaText; }
      });
      Object.defineProperty(lAction, "text", {
        enumerable: true,
        get: function () { return "🎯 Chốt lại nhiệm vụ (Cần làm gì): " + getG().actionText; }
      });

      setTimeout(updateQuickGuidePanel, 60);
      return L.concat([lParams, lFormula, lAction]);
    } catch (e) {
      return L;
    }
  }

  window.__hdlgEnrichStageLines = enrichStageLines;

  /* Làm giàu cốt truyện mở đầu (#introStory) để chốt rõ lý thuyết bài học mới & việc cần làm */
  function enrichIntroStoryHtml(rawHtml) {
    try {
      var html = String(rawHtml || "");
      if (!html || html.indexOf("hdlg-intro-summary") >= 0) return html;

      var GM = G("GM"), LESSON = G("LESSON") || G("FALLBACK_LESSON") || {};
      var lessons = [];
      try {
        if (GM && typeof GM.summaryLessons === "function") {
          lessons = GM.summaryLessons() || [];
        }
      } catch (e) {}

      var formulaItems = [];
      if (Array.isArray(lessons) && lessons.length) {
        lessons.slice(0, 4).forEach(function (it) {
          if (Array.isArray(it) && it.length >= 2) {
            formulaItems.push("<li><b class='text-amber-200'>" + it[0] + ":</b> " + it[1] + "</li>");
          }
        });
      } else if (Array.isArray(LESSON.formulas) && LESSON.formulas.length) {
        LESSON.formulas.slice(0, 4).forEach(function (f) {
          if (typeof f === "string") formulaItems.push("<li>• " + f + "</li>");
          else if (f && f.name && f.formula) formulaItems.push("<li><b class='text-amber-200'>" + f.name + ":</b> " + f.formula + "</li>");
        });
      }

      var theoryBlock = formulaItems.length
        ? "<div class='mt-2.5 p-2.5 rounded-xl bg-slate-900/80 border border-amber-400/40 text-[11.5px] leading-relaxed'>" +
            "<div class='font-extrabold text-amber-300 mb-1'>📘 Kiến thức & Công thức trọng tâm (theo bài học mới):</div>" +
            "<ul class='space-y-1 text-slate-200'>" + formulaItems.join("") + "</ul>" +
          "</div>"
        : "";

      var missionBlock =
        "<div class='hdlg-intro-summary mt-2 p-2.5 rounded-xl bg-emerald-950/75 border border-emerald-400/50 text-[11.5px] leading-relaxed text-emerald-100'>" +
          "<div class='font-extrabold text-emerald-300 mb-0.5'>🎯 Chốt lại: Vào màn chơi bạn cần làm gì?</div>" +
          "<div><b>Bước 1:</b> Đọc kỹ dòng <b>📊 Thông số để tính toán</b> và <b>📐 Công thức & cách tính</b> xuất hiện ngay trong lời thoại của nhân vật ở mỗi chặng (hoặc bấm nút <b>📋 Tóm tắt</b> ở góc trên).<br>" +
          "<b>Bước 2:</b> Thay các thông số đã cho vào công thức để tính ra giá trị cần tìm, rồi <b>kéo thanh trượt / xoay núm / chọn linh kiện</b> trên màn hình.<br>" +
          "<b>Bước 3:</b> Bấm nút hành động màu xanh lá (<b>▶</b>) ở góc dưới để chạy kiểm chứng và hoàn thành cả 3 chặng!</div>" +
        "</div>";

      return html + theoryBlock + missionBlock;
    } catch (e) {
      return rawHtml;
    }
  }

  window.__hdlgEnrichIntroStory = enrichIntroStoryHtml;

  /* Bảng nổi "📋 Thông số & Nhiệm vụ" trong lúc thiết lập (setup) để người chơi vừa nhìn số liệu vừa chỉnh thanh trượt */
  var panelOpen = false;
  function ensureQuickGuideUI() {
    if ($("hdlgQuickGuideWrap")) return;
    if (!document.body) return;

    var st = document.createElement("style");
    st.textContent =
      "#hdlgQuickGuideWrap{position:fixed;left:12px;bottom:14px;z-index:28;max-width:min(92vw,440px);font-family:'Be Vietnam Pro','Segoe UI',system-ui,sans-serif;pointer-events:auto}" +
      "#hdlgQuickGuideBtn{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(180deg,#0f172a,#1e293b);color:#fde68a;border:2px solid #f59e0b;border-radius:999px;padding:6px 13px;font-size:12px;font-weight:800;box-shadow:0 6px 18px rgba(0,0,0,.55);cursor:pointer}" +
      "#hdlgQuickGuideBtn:hover{filter:brightness(1.12)}" +
      "#hdlgQuickGuideCard{display:none;margin-bottom:8px;background:rgba(9,18,36,.96);color:#f1f5f9;border:2px solid #38bdf8;border-radius:16px;padding:11px 13px;font-size:12px;line-height:1.48;box-shadow:0 12px 30px rgba(0,0,0,.7);backdrop-filter:blur(8px);max-height:52vh;overflow-y:auto}" +
      "#hdlgQuickGuideCard.open{display:block}" +
      ".hdlg-qg-sec{margin-bottom:7px}.hdlg-qg-sec:last-child{margin-bottom:0}" +
      ".hdlg-qg-lbl{font-weight:800;display:block;margin-bottom:2px}";
    document.head.appendChild(st);

    var wrap = document.createElement("div");
    wrap.id = "hdlgQuickGuideWrap";
    wrap.innerHTML =
      "<div id='hdlgQuickGuideCard'>" +
        "<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;border-bottom:1px solid rgba(148,163,184,.25);padding-bottom:4px'>" +
          "<strong style='color:#38bdf8;font-size:12.5px'>📋 Tóm tắt Thông số · Công thức · Nhiệm vụ</strong>" +
          "<button type='button' id='hdlgQuickGuideClose' style='background:none;border:0;color:#94a3b8;font-weight:900;font-size:14px;cursor:pointer'>✕</button>" +
        "</div>" +
        "<div class='hdlg-qg-sec'><span class='hdlg-qg-lbl' style='color:#fcd34d'>📊 Thông số để tính toán:</span><div id='hdlgQGParams'></div></div>" +
        "<div class='hdlg-qg-sec'><span class='hdlg-qg-lbl' style='color:#c084fc'>📐 Công thức & cách tính:</span><div id='hdlgQGFormula'></div></div>" +
        "<div class='hdlg-qg-sec'><span class='hdlg-qg-lbl' style='color:#4ade80'>🎯 Chốt nhiệm vụ (Cần làm gì):</span><div id='hdlgQGAction'></div></div>" +
      "</div>" +
      "<button type='button' id='hdlgQuickGuideBtn'>📋 Thông số & Nhiệm vụ</button>";
    document.body.appendChild(wrap);

    $("hdlgQuickGuideBtn").addEventListener("click", function () {
      panelOpen = !panelOpen;
      updateQuickGuidePanel();
    });
    $("hdlgQuickGuideClose").addEventListener("click", function () {
      panelOpen = false;
      var card = $("hdlgQuickGuideCard");
      if (card) card.classList.remove("open");
    });
  }

  function updateQuickGuidePanel() {
    try {
      var GM = G("GM"), stFn = G("stageLines");
      if (!GM && typeof stFn !== "function") return;
      ensureQuickGuideUI();
      var g = extractStageGuide();
      if ($("hdlgQGParams")) $("hdlgQGParams").textContent = g.paramsText;
      if ($("hdlgQGFormula")) $("hdlgQGFormula").textContent = g.formulaText;
      if ($("hdlgQGAction")) $("hdlgQGAction").textContent = g.actionText;
      var card = $("hdlgQuickGuideCard");
      if (card) card.classList.toggle("open", !!panelOpen);
      if (window.HDLGMath && typeof window.HDLGMath.render === "function" && card) {
        window.HDLGMath.render(card);
      }
    } catch (e) {}
  }

  function patch() {
    var GM = G("GM");
    var patched = false;

    if (GM && typeof GM.stageLines === "function" && !GM.__params) {
      var origSL = GM.stageLines;
      GM.stageLines = function () {
        var L = origSL.apply(this, arguments);
        return enrichStageLines(L);
      };
      if (typeof GM.introStory === "function") {
        var origIS = GM.introStory;
        GM.introStory = function () {
          return enrichIntroStoryHtml(origIS.apply(this, arguments));
        };
      }
      GM.__params = true;
      patched = true;
    }

    /* Hỗ trợ game_congsuat.html (dùng hàm stageLines toàn cục thay vì GM.stageLines) */
    var globalSL = G("stageLines");
    if (!GM && typeof globalSL === "function" && !globalSL.__params) {
      try {
        window.stageLines = function () {
          var L = globalSL.apply(this, arguments);
          return enrichStageLines(L);
        };
        window.stageLines.__params = true;
        patched = true;
      } catch (e) {}
    }

    if (patched) {
      var introEl = $("introStory");
      if (introEl && introEl.innerHTML && introEl.innerHTML.indexOf("hdlg-intro-summary") < 0) {
        introEl.innerHTML = enrichIntroStoryHtml(introEl.innerHTML);
      }
      setTimeout(updateQuickGuidePanel, 200);
    }
    return patched;
  }

  if (!patch()) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", patch);
    addEventListener("load", patch);
  }
})();
