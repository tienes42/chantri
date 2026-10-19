/* HỌC ĐỂ LÀM GÌ — mobile-fit.js
   Sửa giao diện game trên điện thoại (dùng chung cho mọi game).
   data-mode="virtual": game kiểu Tailwind (toàn màn hình) -> khi xoay ngang trên điện thoại,
                        hiển thị như màn hình máy tính rồi thu nhỏ cho vừa.
   data-mode="stage"  : game khung 960x540 tự co giãn -> nhắc xoay ngang khi cầm dọc. */
(function () {
  var me = document.currentScript;
  var mode = (me && me.getAttribute("data-mode")) || "";
  var touch = (window.matchMedia && matchMedia("(pointer: coarse)").matches) || ("ontouchstart" in window);

  /* 1) CSS: dùng chiều cao THẬT của màn hình (100dvh) thay vì 100vh bị thanh trình duyệt che */
  var css =
    "body.h-screen{height:100vh;height:100dvh!important}" +
    ".scroll-y{max-height:88vh;max-height:calc(100dvh - 28px)!important;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;touch-action:pan-y}" +
    /* nút bắt đầu luôn dính ở đáy hộp giới thiệu, không phải cuộn tìm */
    ".scroll-y div:has(> #btnStartGame){position:sticky;bottom:-20px;z-index:3;margin-bottom:-20px;padding:12px 0 20px;background:linear-gradient(rgba(7,14,28,0),rgba(7,14,28,.97) 40%)}" +
    ".hdlg-box{max-height:92vh;max-height:calc(100dvh - 24px)!important;touch-action:pan-y}" +
    "@media (max-height:480px){.hdlg-ov{padding:6px!important}.hdlg-box{max-width:520px!important;padding:12px 18px!important;border-radius:14px!important}.hdlg-box h2{font-size:18px!important}.hdlg-sub{margin-bottom:6px!important;font-size:12px!important}.hdlg-box input{padding:7px 10px!important;margin-bottom:6px!important;font-size:14px!important}.hdlg-btn{padding:8px!important;font-size:14px!important}.hdlg-btn.g{margin-top:6px!important}.hdlg-or{margin-top:6px!important}.hdlg-tg{margin-top:8px!important}}" +
    "#hdlgRotate{position:fixed;left:50%;top:10px;transform:translateX(-50%);z-index:99990;display:none;align-items:center;gap:8px;" +
    "background:rgba(8,20,42,.94);color:#ffe9a3;border:2px solid #ffd166;border-radius:999px;padding:7px 8px 7px 14px;" +
    "font:700 13px 'Segoe UI',Arial,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.5);white-space:nowrap}" +
    "#hdlgRotate button{border:0;background:#ffd166;color:#4a2c00;border-radius:50%;width:24px;height:24px;font-weight:900;font-size:18px;line-height:1;cursor:pointer}";
  var st = document.createElement("style");
  st.id = "hdlgMobileFit";
  st.textContent = css;
  (document.head || document.documentElement).appendChild(st);

  if (!touch) return;

  function isLand() {
    if (screen.orientation && screen.orientation.type) return screen.orientation.type.indexOf("landscape") === 0;
    if (typeof window.orientation === "number") return Math.abs(window.orientation) === 90;
    return innerWidth > innerHeight;
  }

  /* 2) Xoay ngang: giả lập màn hình cao ~600px để giao diện máy tính hiển thị đầy đủ */
  if (mode === "virtual") {
    var meta = document.querySelector('meta[name="viewport"]');
    if (!meta) { meta = document.createElement("meta"); meta.name = "viewport"; document.head.appendChild(meta); }
    var BASE = "width=device-width, initial-scale=1";
    var TARGET = 600, cur = 0, timer = 0;
    var fit = function () {
      var land = isLand();
      var dw = land ? Math.max(screen.width, screen.height) : Math.min(screen.width, screen.height);
      var realH = innerHeight * (dw / innerWidth);          // chiều cao nhìn thấy (px thật)
      if (land && realH > 0 && realH < TARGET - 20) {
        var w = Math.round(dw * TARGET / realH);
        if (Math.abs(w - cur) > 12) { cur = w; meta.setAttribute("content", "width=" + w + ", user-scalable=no"); }
      } else if (cur || !land) {
        if (cur) { cur = 0; meta.setAttribute("content", BASE); }
      }
    };
    var later = function () { clearTimeout(timer); timer = setTimeout(fit, 250); };
    fit();
    addEventListener("resize", later);
    addEventListener("orientationchange", function () { cur = 0; meta.setAttribute("content", BASE); later(); });
    if (screen.orientation && screen.orientation.addEventListener) screen.orientation.addEventListener("change", later);
  }

  /* 3) Game khung cố định: nhắc xoay ngang khi cầm dọc */
  if (mode === "stage") {
    var closed = false;
    var tip = function () {
      var el = document.getElementById("hdlgRotate");
      if (!el) {
        if (!document.body) return;
        el = document.createElement("div");
        el.id = "hdlgRotate";
        el.innerHTML = "<span>🔄 Xoay ngang điện thoại để chơi rõ hơn</span><button type='button' aria-label='Đóng'>×</button>";
        el.querySelector("button").onclick = function () { closed = true; el.style.display = "none"; };
        document.body.appendChild(el);
      }
      el.style.display = (!closed && !isLand()) ? "flex" : "none";
    };
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", tip); else tip();
    addEventListener("resize", tip);
    addEventListener("orientationchange", function () { setTimeout(tip, 300); });
  }
})();
