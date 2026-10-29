/* =========================================================================
   NÚT "VỀ TRANG CHỦ" — tự gắn vào mọi trang (trừ trang chủ), góc trên bên trái
   - Trang có sẵn nút Quay lại (#backButton / #backBtn): đặt nút 🏠 ngay cạnh nút đó, cùng kiểu dáng.
   - Trang không có (game, mô phỏng…): nút 🏠 nổi cố định ở góc trên bên trái.
   Được auth.js tự nạp; trang không dùng auth.js thì nhúng: <script src="/home-button.js" defer></script>
   ========================================================================= */
(function () {
  "use strict";
  if (window.__hdlgHomeBtn) return;
  window.__hdlgHomeBtn = true;
  try { if (window.parent !== window) return; } catch (e) { return; }      // không hiện trong iframe
  var page = (location.pathname.split("/").pop() || "").toLowerCase();
  if (page === "" || page === "index.html" || page === "index") return;    // trang chủ: không cần

  var HOME = "/index.html";
  var CSS =
    ".hdlg-home-wrap{display:inline-flex;align-items:center;gap:8px;flex:none}" +
    ".hdlg-home-wrap>*{margin:0!important}" +
    ".hdlg-home-inline{flex:none!important;min-width:36px;white-space:nowrap;display:inline-flex!important;align-items:center;justify-content:center;gap:6px;text-decoration:none;cursor:pointer}" +
    ".hdlg-home-fixed{position:fixed;z-index:9990;left:calc(10px + env(safe-area-inset-left));top:calc(10px + env(safe-area-inset-top));" +
      "display:inline-flex;align-items:center;gap:6px;height:40px;padding:0 13px 0 11px;border-radius:999px;" +
      "background:rgba(10,24,56,.82);color:#eaf2ff;border:1.5px solid rgba(125,211,252,.7);" +
      "box-shadow:0 6px 18px rgba(0,0,0,.35);font:700 13px 'Segoe UI',Roboto,Arial,sans-serif;text-decoration:none;" +
      "backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);transition:transform .15s,border-color .15s;-webkit-tap-highlight-color:transparent}" +
    ".hdlg-home-fixed:hover{transform:translateY(-1px);border-color:#fde047}" +
    ".hdlg-home-fixed .i{font-size:18px;line-height:1}" +
    "@media (max-width:700px){.hdlg-home-fixed{height:36px;width:36px;padding:0;justify-content:center}.hdlg-home-fixed .t{display:none}}" +
    ".hdlg-home-chip{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 13px 0 11px;border-radius:999px;flex:none;" +
      "background:rgba(10,24,56,.85);color:#eaf2ff;border:1.5px solid rgba(125,211,252,.7);font:700 13px 'Segoe UI',Roboto,Arial,sans-serif;text-decoration:none}" +
    ".hdlg-home-chip:hover{border-color:#fde047}.hdlg-home-chip .i{font-size:17px;line-height:1}" +
    "@media (max-width:700px){.hdlg-home-inline .t,.hdlg-home-chip .t{display:none}.hdlg-home-chip{width:36px;height:36px;padding:0;justify-content:center}}" +
    "body.hdlg-has-home-fixed{scroll-padding-top:56px}";

  var EXITS = ["#backButton", "#backBtn", "#btnExitGame", "#bExit", ".back-btn", "button.back"];
  function findExit() {
    for (var i = 0; i < EXITS.length; i++) {
      var els = document.querySelectorAll(EXITS[i]);
      for (var j = 0; j < els.length; j++) {
        var r = els[j].getBoundingClientRect();
        if (r.width > 0 && r.height > 0 && r.top < Math.max(200, innerHeight * 0.55) && r.left < innerWidth * 0.6) return els[j];
      }
    }
    return null;
  }
  function makeBtn(cls, label) {
    var a = document.createElement("a");
    a.id = "hdlgHomeBtn"; a.href = HOME; a.title = "Về trang chủ"; a.setAttribute("aria-label", "Về trang chủ");
    a.className = cls;
    a.innerHTML = '<span class="i">🏠</span>' + (label ? '<span class="t">Trang chủ</span>' : "");
    return a;
  }
  function wrapWith(target, a, before) {
    var wrap = document.createElement("span");
    wrap.className = "hdlg-home-wrap";
    target.parentNode.insertBefore(wrap, target);
    if (before) { wrap.appendChild(a); wrap.appendChild(target); } else { wrap.appendChild(target); wrap.appendChild(a); }
  }

  var styled = false;
  function mount(final) {
    if (document.getElementById("hdlgHomeBtn")) return true;
    if (!styled) { var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st); styled = true; }

    // 1) Có nút Quay lại / Thoát / Về bài học ở phía trên → đặt 🏠 ngay cạnh, cùng kiểu dáng
    var back = findExit();
    if (back) {
      var hasLabel = (back.textContent || "").replace(/\s|←|‹|<|&lt;/g, "").length > 1;
      wrapWith(back, makeBtn((back.className || "") + " hdlg-home-inline", hasLabel));
      return true;
    }
    if (!final) return false;               // chờ trang (game) dựng xong giao diện rồi thử lại

    // 2) Có thanh tiêu đề sát mép trên → gắn 🏠 vào đầu thanh, không che chữ
    var hd = document.querySelector("body > header, .game-header, .topbar");
    var first = hd && hd.firstElementChild;
    if (first && hd.getBoundingClientRect().top < 20 && first.getBoundingClientRect().left < innerWidth * 0.4) {
      wrapWith(first, makeBtn("hdlg-home-chip", true), true);
      return true;
    }

    // 3) Còn lại: nút nổi cố định góc trên bên trái
    var a = makeBtn("hdlg-home-fixed", true);
    document.body.appendChild(a);
    document.body.classList.add("hdlg-has-home-fixed");
    return true;
  }
  function start() {
    if (mount(false)) return;
    var tries = 0, t = setInterval(function () {
      if (mount(++tries >= 6 && document.readyState === "complete")) clearInterval(t);
    }, 250);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
