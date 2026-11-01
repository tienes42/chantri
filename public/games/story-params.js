/* HỌC ĐỂ LÀM GÌ — story-params.js
   Lời kể mỗi chặng tự kèm "📋 Thông số" để người chơi có đủ số liệu tính toán ngay trong lúc nghe kể chuyện:
   - dòng nhiệm vụ của chặng (GM.hud().l1: khối lượng, quãng đường, giới hạn…);
   - các dòng "• …" trên bảng số liệu vẽ trong cảnh (sổ tay, bảng thông số) nếu game có.
   Chỉ thêm khi có số liệu chưa được nhắc trong lời kể. Game không có GM.stageLines / GM.hud thì bỏ qua. */
(function () {
  "use strict";
  if (window.__hdlgStoryParams) return;
  window.__hdlgStoryParams = true;
  function G(n) { try { return Function("return typeof " + n + " !== 'undefined' ? " + n + " : undefined")(); } catch (e) { return undefined; } }
  function nums(s) { return (String(s).match(/\d+(?:[.,  ]\d+)*/g) || []).map(function (x) { return x.replace(/[.,  ]/g, ""); }).filter(function (n) { return n !== "0" && n !== "1"; }); }
  function fresh(s, told) { return nums(s).some(function (n) { return !told[n]; }); }

  /* Ghi lại các dòng "• …" đang được vẽ trên canvas (bảng số liệu của chặng) */
  var bullets = new Map(), boardSeen = false;
  var CP = window.CanvasRenderingContext2D && CanvasRenderingContext2D.prototype;
  if (CP && CP.fillText && !CP.fillText.__sp) {
    var ft = CP.fillText;
    CP.fillText = function (t) {
      if (typeof t === "string" && t.charCodeAt(0) === 0x2022 && /\d/.test(t) && t.length < 220) {
        boardSeen = true; bullets.set(t, Date.now());
        if (bullets.size > 120) bullets.delete(bullets.keys().next().value);
      }
      return ft.apply(this, arguments);
    };
    CP.fillText.__sp = true;
  }
  var HOWTO = /^•\s*(Đã|Bấm|Kéo|Nhấn|Chạm|Chọn|Gạt|Xoay|Thả|Mở|Đóng|Đặt|Click|Hãy)\b/i;
  function boardNow(told) {
    var now = Date.now(), out = [];
    bullets.forEach(function (t, s) { if (now - t < 600 && !HOWTO.test(s) && fresh(s, told)) out.push(s.replace(/^•\s*/, "")); });
    return out.slice(0, 8);
  }

  function patch() {
    var GM = G("GM");
    if (!GM || typeof GM.stageLines !== "function" || typeof GM.hud !== "function" || GM.__params) return !!(GM && GM.__params);
    var orig = GM.stageLines;
    GM.stageLines = function () {
      var L = orig.apply(this, arguments);
      try {
        if (!Array.isArray(L) || !L.length || L.some(function (x) { return x && x.__p; })) return L;
        var h = GM.hud(), l1 = h && typeof h.l1 === "string" ? h.l1.replace(/^[^0-9A-Za-zÀ-ỹ]+/, "").trim() : "";
        var told = {};
        nums(L.map(function (x) { return x && x.text || ""; }).join(" ")).forEach(function (n) { told[n] = 1; });
        var l1New = !!l1 && fresh(l1, told);
        if (!l1New && !boardSeen) return L;
        var who = L.some(function (x) { return x && x.who === "A"; }) ? "A" : (L[L.length - 1] && L[L.length - 1].who) || "A";
        var cache = null;
        var line = { who: who, __p: 1 }, res = L.concat([line]);
        bullets.clear();                                                      // chỉ lấy bảng số liệu vẽ SAU khi vào chặng này
        Object.defineProperty(line, "text", { enumerable: true, get: function () {   // tính lúc dòng hiện ra (bảng số liệu đã vẽ xong)
          if (cache != null) return cache;
          var parts = l1New ? [l1] : [], b = boardNow(told);
          parts = parts.concat(b);
          if (!parts.length) parts = l1 ? [l1] : boardNow({});                     // không có gì mới → nhắc lại tóm tắt
          if (!parts.length) return (cache = "📋 Thông số: xem bảng nhiệm vụ phía trên.");
          // chia thành nhiều câu ngắn cho vừa khung hội thoại (nhất là điện thoại)
          var max = 160, atoms = parts.join(" · ").split(" · "), chunks = [], cur = "";
          atoms.forEach(function (a) { if (cur && (cur + " · " + a).length > max) { chunks.push(cur); cur = a; } else cur = cur ? cur + " · " + a : a; });
          if (cur) chunks.push(cur);
          for (var k = 1; k < chunks.length; k++) res.push({ who: who, __p: 1, text: "📋 " + chunks[k] });
          return (cache = "📋 Thông số: " + chunks[0]);
        } });
        return res;
      } catch (e) { return L; }
    };
    GM.__params = true;
    return true;
  }
  if (!patch()) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", patch);
    addEventListener("load", patch);
  }
})();
