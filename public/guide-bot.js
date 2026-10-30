/* =========================================================================
   CHÂN TRI — BOT HƯỚNG DẪN "TRI" (tour cho người mới)
   Nhúng:  <script src="/guide-bot.js" defer></script>
   Trang có tour: index.html → physics.html → physics-grade.html?grade=12 → lesson.html
   - Trang chủ: Bot luôn nằm giữa cạnh phải, bấm vào để bắt đầu hướng dẫn.
   - Các trang khác: Bot chỉ hiện khi đang trong tour.
   API: HDLGTour.start() | HDLGTour.stop() | HDLGTour.reset()
   ========================================================================= */
(function () {
  "use strict";
  if (window.HDLGTour) return;

  var LS_STATE = "hdlg_tour", LS_DONE = "hdlg_tour_done", SS_HIDE = "hdlg_tour_hint_hidden";
  var PAGE = (location.pathname.split("/").pop() || "index").replace(/\.html?$/i, "") || "index";
  var QS = new URLSearchParams(location.search);
  var TOTAL = 5;

  var URLS = {
    index: "index.html",
    physics: "physics.html",
    "physics-grade": "physics-grade.html?grade=12",
    lesson: "lesson.html?id=85&subject=physics&grade=12&topic=thuyet-tuong-doi"
  };

  /* ---------- KỊCH BẢN HƯỚNG DẪN ---------- */
  var STEPS = {
    island: {
      page: "index", n: 1, hole: ".hit.physics", click: ".hit.physics", next: "grade", floaty: true,
      title: "Đảo bay Vật lý ⚡",
      text: "Mỗi hòn <b>đảo bay</b> là một <b>môn học</b>. Bấm vào <b>Đảo Vật lý</b> để vào khu học Vật lý — nơi có bài học theo từng lớp, phòng thí nghiệm ảo và thử thách nhanh."
    },
    grade: {
      page: "physics", n: 2, hole: '.class-card[data-grade="12"]', click: '.class-card[data-grade="12"]', next: "gradeGo",
      title: "Chọn lớp học 🎓",
      text: "Bài học được chia theo <b>khối lớp 6 → 12</b>, bám sát chương trình trên lớp. Bấm vào <b>Lớp 12</b> để xem các chủ đề của lớp 12 nhé!"
    },
    gradeGo: {
      page: "physics", n: 2, hole: "#mathPopup .math-popup", click: "#mathPopupButton", next: "topic",
      need: "#mathPopup.show", back: "grade",
      title: "Mở lớp 12 🚪",
      text: "Đây là thông tin của mô-đun lớp 12. Bấm <b>Bắt đầu Khám phá →</b> để mở danh sách bài học."
    },
    topic: {
      page: "physics-grade", n: 3, grade: "12", hole: '.topic-card[data-topic="thuyet-tuong-doi"]', click: '.topic-card[data-topic="thuyet-tuong-doi"]', next: "topicGo",
      title: "Chọn bài học 📚",
      text: "Mỗi thẻ là một <b>bài học</b>, thanh tiến độ cho biết bạn đã học được bao nhiêu. Thử mở bài <b>Thuyết tương đối hẹp của Einstein</b> — bài cực hay về <b>E = mc²</b>!"
    },
    topicGo: {
      page: "physics-grade", n: 3, grade: "12", hole: "#topicPopup .popup", click: "#popupStart", next: "reading",
      need: "#topicPopup.show", back: "topic",
      title: "Vào bài học ▶",
      text: "Mỗi bài học đọc xong sẽ nhận <b>sao ⭐</b> để lên cấp. Bấm <b>Bắt đầu học →</b> để vào bài."
    },
    reading: {
      page: "lesson", n: 4, dim: false, pos: "pos-bottom", ready: "#lessonContent:not(.hidden)", until: "#gameSection", next: "game",
      title: "Phần đọc 📖",
      text: "Đây là <b>phần đọc</b> của bài: định nghĩa, bối cảnh thực tế, kiến thức cốt lõi, công thức, ví dụ và <b>Kiểm tra nhanh</b>. Đọc hết bài được <b>+5 ⭐</b>, trả lời đúng ngay lần đầu thêm <b>+5 ⭐</b>.<br>Đọc xong thì <b>lướt xuống dưới cùng</b> nhé — có bất ngờ đang chờ! 👇",
      action: { label: "⬇ Lướt xuống giúp mình", fn: "scrollGame" }
    },
    game: {
      page: "lesson", n: 5, hole: "#gameSection", click: "#gameButton", intercept: true, next: "bye",
      ready: "#lessonContent:not(.hidden)",
      title: "Trải nghiệm thực tế 2.5D 🎮",
      text: "Đây là phần <b>hay nhất</b> của Chân Tri! Bạn sẽ chơi <b>game mô phỏng 2.5D</b> để vận dụng kiến thức vừa học vào tình huống thật — và <b>ăn thêm thật nhiều sao ⭐</b> để leo bảng xếp hạng.<br>Bấm <b>🚀 Bắt đầu trải nghiệm</b> nào!"
    },
    bye: {
      page: "lesson", n: 5, hole: null, title: "Hoàn thành hướng dẫn 🎉",
      text: "Tuyệt vời! Giờ bạn đã biết cách dùng Chân Tri:<br><b>Chọn đảo môn học → chọn lớp → mở bài → đọc → lướt xuống chơi Trải nghiệm thực tế</b>.<br>Bài nào cũng có phần trải nghiệm này nhé. Chúc bạn học thật vui và sớm lên top bảng xếp hạng! 🏆",
      final: true
    }
  };

  /* ---------- LƯU TRẠNG THÁI ---------- */
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function lsDel(k) { try { localStorage.removeItem(k); } catch (e) {} }
  function getState() {
    try {
      var s = JSON.parse(lsGet(LS_STATE) || "null");
      if (s && STEPS[s.step] && Date.now() - (s.t || 0) < 3 * 3600 * 1000) return s;
    } catch (e) {}
    return null;
  }
  function saveStep(id) { lsSet(LS_STATE, JSON.stringify({ step: id, t: Date.now() })); }

  /* ---------- BOT SVG ---------- */
  var BOT_SVG = '' +
'<svg class="tg-svg" viewBox="0 0 140 160" aria-hidden="true">' +
'<defs>' +
'<linearGradient id="tgShell" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="#e6f3ff"/><stop offset="1" stop-color="#a9d4ff"/></linearGradient>' +
'<linearGradient id="tgShell2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#9fcaf7"/></linearGradient>' +
'<linearGradient id="tgGold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2a8"/><stop offset=".5" stop-color="#fbbf24"/><stop offset="1" stop-color="#b7791f"/></linearGradient>' +
'<linearGradient id="tgScreen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16305e"/><stop offset="1" stop-color="#071433"/></linearGradient>' +
'<radialGradient id="tgEye" cx=".5" cy=".4" r=".6"><stop offset="0" stop-color="#e9ffff"/><stop offset=".45" stop-color="#5eeaff"/><stop offset="1" stop-color="#0ea5e9"/></radialGradient>' +
'<linearGradient id="tgFlame" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e0fbff"/><stop offset=".4" stop-color="#38bdf8"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></linearGradient>' +
'<radialGradient id="tgCore" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fffbe0"/><stop offset=".5" stop-color="#fde047"/><stop offset="1" stop-color="#f59e0b"/></radialGradient>' +
'</defs>' +
'<ellipse class="tg-shadow" cx="70" cy="154" rx="28" ry="4.5" fill="#38bdf8" opacity=".35"/>' +
'<g class="tg-body">' +
  /* lửa phản lực */
'<path class="tg-flame" d="M61 128 Q70 156 79 128 Z" fill="url(#tgFlame)"/>' +
  /* tay trái (vẫy) */
'<g class="tg-arm-l"><path d="M40 104 Q24 98 20 84" stroke="#bcdcff" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M40 104 Q24 98 20 84" stroke="url(#tgShell2)" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="19" cy="81" r="7.5" fill="url(#tgGold)" stroke="#8a5a12" stroke-width="1.2"/></g>' +
  /* tay phải cầm sách */
'<g class="tg-arm-r"><path d="M100 104 Q114 110 116 120" stroke="#bcdcff" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M100 104 Q114 110 116 120" stroke="url(#tgShell2)" stroke-width="6" stroke-linecap="round" fill="none"/>' +
'<g class="tg-book"><path d="M104 118 L117 114 L130 118 L130 132 L117 128 L104 132 Z" fill="#38bdf8" opacity=".25"/><path d="M104 118 L117 114 L117 128 L104 132 Z" fill="#e0f7ff" stroke="#38bdf8" stroke-width="1.4"/><path d="M117 114 L130 118 L130 132 L117 128 Z" fill="#c7efff" stroke="#38bdf8" stroke-width="1.4"/><path d="M108 121 L114 119 M108 125 L114 123 M120 119 L126 121 M120 123 L126 125" stroke="#0ea5e9" stroke-width="1.1" stroke-linecap="round"/></g></g>' +
  /* thân */
'<path d="M44 96 Q44 88 54 88 L86 88 Q96 88 96 96 L94 118 Q92 132 70 132 Q48 132 46 118 Z" fill="url(#tgShell)" stroke="#7fb4ea" stroke-width="1.6"/>' +
'<path d="M48 98 Q70 104 92 98" stroke="url(#tgGold)" stroke-width="3" fill="none" stroke-linecap="round"/>' +
'<circle cx="70" cy="114" r="9.5" fill="#0b1c42" stroke="url(#tgGold)" stroke-width="2.6"/>' +
'<path class="tg-core" d="M70 107.5 L72 112 L76.8 112.4 L73.1 115.4 L74.3 120 L70 117.5 L65.7 120 L66.9 115.4 L63.2 112.4 L68 112 Z" fill="url(#tgCore)"/>' +
  /* cổ */
'<rect x="60" y="82" width="20" height="8" rx="4" fill="#8fbbe8"/>' +
  /* đầu */
'<g class="tg-head">' +
'<line x1="70" y1="20" x2="70" y2="8" stroke="#8fbbe8" stroke-width="3" stroke-linecap="round"/>' +
'<path class="tg-star" d="M70 -3 L72.6 3.2 L79.2 3.6 L74.1 7.8 L75.8 14.2 L70 10.6 L64.2 14.2 L65.9 7.8 L60.8 3.6 L67.4 3.2 Z" fill="url(#tgGold)" stroke="#fff6c2" stroke-width=".8"/>' +
'<circle cx="18" cy="52" r="9" fill="url(#tgGold)" stroke="#8a5a12" stroke-width="1.2"/><circle cx="18" cy="52" r="4" fill="#5eeaff" class="tg-ear"/>' +
'<circle cx="122" cy="52" r="9" fill="url(#tgGold)" stroke="#8a5a12" stroke-width="1.2"/><circle cx="122" cy="52" r="4" fill="#5eeaff" class="tg-ear"/>' +
'<rect x="22" y="18" width="96" height="68" rx="32" fill="url(#tgShell)" stroke="#7fb4ea" stroke-width="1.8"/>' +
'<path d="M36 26 Q52 20 70 20" stroke="#ffffff" stroke-width="4" stroke-linecap="round" fill="none" opacity=".9"/>' +
'<rect x="31" y="30" width="78" height="46" rx="22" fill="url(#tgScreen)" stroke="url(#tgGold)" stroke-width="2.4"/>' +
'<path d="M40 38 Q50 33 62 33" stroke="#5b7fc7" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".6"/>' +
'<g class="tg-eyes"><rect x="47" y="43" width="12" height="16" rx="6" fill="url(#tgEye)"/><rect x="81" y="43" width="12" height="16" rx="6" fill="url(#tgEye)"/>' +
'<circle cx="51" cy="47" r="2.2" fill="#fff"/><circle cx="85" cy="47" r="2.2" fill="#fff"/></g>' +
'<ellipse cx="42" cy="64" rx="5" ry="3" fill="#f472b6" opacity=".55"/><ellipse cx="98" cy="64" rx="5" ry="3" fill="#f472b6" opacity=".55"/>' +
'<path class="tg-mouth" d="M62 63 Q70 70 78 63" stroke="#5eeaff" stroke-width="3" stroke-linecap="round" fill="none"/>' +
'</g></g></svg>';

  /* ---------- CSS ---------- */
  var CSS = "" +
/* Lớp tối = 4 khối màu đặc bao quanh vùng sáng (không dùng clip-path → không nhấp nháy trên điện thoại) */
"#tgMask{position:fixed;inset:0;z-index:99000;pointer-events:none;opacity:0;transition:opacity .3s}" +
"#tgMask.on{opacity:1}#tgMask[hidden]{display:none}" +
"#tgMask i{position:absolute;display:block;background:rgba(3,8,24,.78);pointer-events:auto;left:0;top:0;width:0;height:0}" +
"#tgMask i.full{left:0!important;top:0!important;width:100%!important;height:100%!important}" +
"#tgRing{position:fixed;left:0;top:0;z-index:99001;pointer-events:none;border-radius:16px;border:3px solid #fde047;box-shadow:0 0 20px 4px rgba(56,189,248,.7);display:none;will-change:transform}" +
"#tgRing::after{content:'';position:absolute;inset:-9px;border-radius:22px;border:2px solid rgba(253,224,71,.85);animation:tgRing 1.4s ease-out infinite}" +
"@keyframes tgRing{0%{opacity:.9;transform:scale(.97)}100%{opacity:0;transform:scale(1.06)}}" +
"#tgHand{position:fixed;left:0;top:0;z-index:99002;pointer-events:none;display:none;will-change:transform}" +
"#tgHand span{display:block;font-size:34px;line-height:1;margin-left:-17px;filter:drop-shadow(0 4px 6px rgba(0,0,0,.6));animation:tgHand .9s ease-in-out infinite}" +
"@keyframes tgHand{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}" +
"#tgBox{position:fixed;z-index:99010;will-change:transform;right:12px;top:50%;transform:translateY(-50%);display:flex;align-items:center;gap:6px;font-family:'Segoe UI',Roboto,Arial,sans-serif;pointer-events:none}" +
"#tgBox.pos-top{top:84px;transform:none}#tgBox.pos-bottom{top:auto;bottom:22px;transform:none}" +
"#tgBot{pointer-events:auto;width:96px;height:110px;border:0;padding:0;background:none;cursor:pointer;position:relative;flex:none;-webkit-tap-highlight-color:transparent}" +
"#tgBot:focus-visible{outline:2px solid #fde047;outline-offset:4px;border-radius:20px}" +
"#tgBot .tg-svg{width:100%;height:100%;overflow:visible;filter:drop-shadow(0 10px 16px rgba(2,10,30,.55)) drop-shadow(0 0 14px rgba(56,189,248,.45))}" +
"#tgBot::after{content:'';position:absolute;left:50%;top:46%;width:130%;height:110%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(56,189,248,.28),transparent 65%);z-index:-1;animation:tgAura 3s ease-in-out infinite}" +
"@keyframes tgAura{50%{opacity:.5;transform:translate(-50%,-50%) scale(.9)}}" +
".tg-body{animation:tgFloat 3.2s ease-in-out infinite;transform-origin:70px 90px}" +
"@keyframes tgFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}" +
".tg-shadow{animation:tgShadow 3.2s ease-in-out infinite;transform-origin:70px 154px}" +
"@keyframes tgShadow{50%{transform:scaleX(.8);opacity:.2}}" +
".tg-flame{animation:tgFlameA .18s ease-in-out infinite alternate;transform-origin:70px 128px}" +
"@keyframes tgFlameA{from{transform:scaleY(.8)}to{transform:scaleY(1.15)}}" +
".tg-eyes{animation:tgBlink 4.5s infinite;transform-origin:70px 51px}" +
"@keyframes tgBlink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.1)}}" +
".tg-star{animation:tgStar 2s ease-in-out infinite;transform-origin:70px 6px}" +
"@keyframes tgStar{50%{transform:scale(1.18) rotate(12deg);filter:drop-shadow(0 0 6px #fde047)}}" +
".tg-ear{animation:tgEar 1.6s ease-in-out infinite}@keyframes tgEar{50%{fill:#fde047}}" +
".tg-arm-l{transform-origin:40px 104px;animation:tgWave 2.6s ease-in-out infinite}" +
"@keyframes tgWave{0%,55%,100%{transform:rotate(0)}65%{transform:rotate(16deg)}75%{transform:rotate(-8deg)}85%{transform:rotate(14deg)}}" +
".tg-book{animation:tgBook 3s ease-in-out infinite;transform-origin:117px 124px}@keyframes tgBook{50%{transform:translateY(-3px) rotate(-4deg)}}" +
".tg-core{animation:tgCoreA 2.2s ease-in-out infinite;transform-origin:70px 114px}@keyframes tgCoreA{50%{transform:scale(.82) rotate(36deg)}}" +
"#tgBot.talk .tg-mouth{animation:tgTalk .22s ease-in-out 6 alternate;transform-origin:70px 65px}" +
"@keyframes tgTalk{to{transform:scaleY(1.9)}}" +
"#tgBot:hover .tg-body{animation-duration:1.4s}" +
"#tgBub{pointer-events:auto;position:relative;width:330px;max-width:calc(100vw - 150px);background:linear-gradient(160deg,#17346a,#0b1838);color:#eaf2ff;border:1.5px solid #5b8fe6;border-radius:18px;padding:14px 16px 12px;box-shadow:0 18px 44px rgba(0,0,0,.55),0 0 0 4px rgba(56,189,248,.12);font-size:14px;line-height:1.5;transform-origin:right center;animation:tgPop .28s cubic-bezier(.2,1.4,.4,1)}" +
"#tgBub[hidden]{display:none}" +
"#tgBub::after{content:'';position:absolute;right:-9px;top:50%;width:16px;height:16px;background:#112652;border-right:1.5px solid #5b8fe6;border-top:1.5px solid #5b8fe6;transform:translateY(-50%) rotate(45deg)}" +
"@keyframes tgPop{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:none}}" +
"#tgBub.shake{animation:tgShake .4s}@keyframes tgShake{20%,60%{transform:translateX(-6px)}40%,80%{transform:translateX(6px)}}" +
".tg-head-row{display:flex;align-items:center;gap:8px;margin-bottom:6px}" +
".tg-name{font-size:12px;font-weight:800;color:#7dd3fc;letter-spacing:.4px;text-transform:uppercase}" +
".tg-stepn{margin-left:auto;font-size:11px;font-weight:700;color:#0b1838;background:#fde047;border-radius:999px;padding:2px 8px}" +
".tg-x{background:none;border:0;color:#9fb5df;font-size:18px;line-height:1;cursor:pointer;padding:0 2px;margin-left:4px}" +
".tg-x:hover{color:#fff}" +
".tg-title{margin:0 0 4px;font-size:16px;font-weight:800;color:#fde68a}" +
".tg-text{margin:0}.tg-text b{color:#fff3b0}" +
".tg-dots{display:flex;gap:5px;margin-top:10px}.tg-dots i{flex:1;height:4px;border-radius:4px;background:#ffffff26}.tg-dots i.on{background:linear-gradient(90deg,#38bdf8,#fde047)}" +
".tg-acts{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;align-items:center}" +
".tg-btn{border:0;border-radius:10px;padding:8px 13px;font:700 13.5px 'Segoe UI',Roboto,Arial,sans-serif;cursor:pointer;background:linear-gradient(180deg,#ffe27a,#f5b82e);color:#1b1b1b;box-shadow:0 4px 0 #a86d0d}" +
".tg-btn:active{transform:translateY(2px);box-shadow:0 2px 0 #a86d0d}" +
".tg-btn.ghost{background:#ffffff14;color:#cfe0ff;box-shadow:none;border:1px solid #ffffff2e}" +
".tg-skip{margin-left:auto;background:none;border:0;color:#8ea6d6;font-size:12px;cursor:pointer;text-decoration:underline;padding:4px 0}" +
"body.tg-on .math-ai{display:none!important}" +
/* ---- Điện thoại ---- */
"@media (max-width:700px){" +
"#tgBot{width:58px;height:66px}" +
"#tgBox{right:4px;top:52.5%}" +
"#tgBox.idle #tgBub{width:auto;max-width:calc(100vw - 92px);font-size:13px;padding:10px 12px}" +
"#tgBox.tour{left:8px;right:8px;justify-content:flex-end}" +
"#tgBox.tour.pos-mid,#tgBox.tour.pos-bottom{top:auto;bottom:calc(10px + env(safe-area-inset-bottom));transform:none}" +
"#tgBox.tour.pos-top{top:calc(10px + env(safe-area-inset-top))}" +
"#tgBox.tour #tgBub{flex:1;width:auto;max-width:none;font-size:13.5px;padding:12px 13px 10px}" +
".tg-title{font-size:15px}#tgHand span{font-size:28px;margin-left:-14px}" +
"}" +
"@media (max-width:700px) and (max-height:560px){#tgBox.tour #tgBub{max-height:46vh;overflow:auto}}" +
"@media (prefers-reduced-motion:reduce){#tgBot *,#tgBot::after,#tgRing::after,#tgHand span{animation:none!important}}";

  /* ---------- DOM ---------- */
  var box, bot, bub, dim, dimParts, ring, hand;
  var shown = null;       // vùng sáng đang hiển thị {l,t,r,b}
  var handAt = null;
  var cur = null, curId = null, holeEl = null, clickEl = null, raf = 0, waitTimer = 0, lostSince = 0, lastPlace = 0;
  var passThrough = false;

  function h(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }
  function build() {
    if (box) return;
    document.head.appendChild(h("style", { id: "tgStyle" }, CSS));
    dim = h("div", { id: "tgMask", hidden: "" }, "<i></i><i></i><i></i><i></i>");
    dimParts = dim.querySelectorAll("i");
    ring = h("div", { id: "tgRing" });
    hand = h("div", { id: "tgHand" }, "<span>👆</span>");
    box = h("div", { id: "tgBox", "class": "idle pos-mid" });
    bub = h("div", { id: "tgBub", role: "dialog", "aria-live": "polite", hidden: "" });
    bot = h("button", { id: "tgBot", type: "button", "aria-label": "Trợ lý Tri – phân tích học tập và hướng dẫn dùng web", title: "Trợ lý Tri: phân tích học tập và hướng dẫn" }, BOT_SVG);
    box.appendChild(bub); box.appendChild(bot);
    document.body.appendChild(dim); document.body.appendChild(ring); document.body.appendChild(hand); document.body.appendChild(box);
    bot.addEventListener("click", onBotClick);
    dim.addEventListener("click", function () { nudge(); });
    window.addEventListener("resize", function () { shown = null; stable = null; if (cur && cur.dim !== false && !holeEl) fullDim(); });
    window.addEventListener("click", onCaptureClick, true);
    window.addEventListener("resize", function () { lastPlace = 0; });
  }
  function talk() { bot.classList.remove("talk"); void bot.offsetWidth; bot.classList.add("talk"); }
  function nudge() { bub.classList.remove("shake"); void bub.offsetWidth; bub.classList.add("shake"); talk(); }

  /* ---------- BONG BÓNG THOẠI ---------- */
  function bubble(o) {
    var dots = "";
    if (o.n) { for (var i = 1; i <= TOTAL; i++) dots += '<i class="' + (i <= o.n ? "on" : "") + '"></i>'; dots = '<div class="tg-dots">' + dots + "</div>"; }
    bub.innerHTML =
      '<div class="tg-head-row"><span class="tg-name">🤖 Bot Tri</span>' +
      (o.n ? '<span class="tg-stepn">Bước ' + o.n + "/" + TOTAL + "</span>" : "") +
      (o.close ? '<button class="tg-x" type="button" aria-label="Ẩn">×</button>' : "") + "</div>" +
      (o.title ? '<h3 class="tg-title">' + o.title + "</h3>" : "") +
      '<p class="tg-text">' + o.text + "</p>" + dots +
      ((o.buttons && o.buttons.length) || o.skip ? '<div class="tg-acts"></div>' : "");
    var acts = bub.querySelector(".tg-acts");
    (o.buttons || []).forEach(function (b) {
      var el = h("button", { type: "button", "class": "tg-btn" + (b.ghost ? " ghost" : "") }, b.label);
      el.onclick = function (e) { e.stopPropagation(); b.fn(); };
      acts.appendChild(el);
    });
    if (o.skip) {
      var sk = h("button", { type: "button", "class": "tg-skip" }, "Bỏ qua hướng dẫn");
      sk.onclick = function (e) { e.stopPropagation(); finish(false); };
      acts.appendChild(sk);
    }
    if (o.close) bub.querySelector(".tg-x").onclick = function (e) { e.stopPropagation(); o.close(); };
    bub.hidden = false;
    bub.style.animation = "none"; void bub.offsetWidth; bub.style.animation = "";
    talk();
    lastPlace = 0;
  }
  function hideBubble() { bub.hidden = true; }

  /* ---------- LỚP TỐI + VÙNG SÁNG ---------- */
  function visible(el) {
    if (!el || !el.isConnected) return null;
    var r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return null;
    var cs = getComputedStyle(el);
    if (cs.visibility === "hidden" || cs.display === "none") return null;
    return r;
  }
  function setDim(on) {
    if (on) { dim.hidden = false; requestAnimationFrame(function () { dim.classList.add("on"); }); }
    else { dim.classList.remove("on"); dim.hidden = true; }
    fullDim();
  }
  /* Tối toàn màn hình (chưa có / mất mục tiêu) */
  function fullDim() {
    if (shown === "full") return;
    shown = "full";
    dimParts[0].className = "full";
    for (var i = 1; i < 4; i++) dimParts[i].style.display = "none";
    ring.style.display = "none"; hand.style.display = "none"; handAt = null;
  }
  function setPart(el, l, t, w, h) {
    el.style.left = l + "px"; el.style.top = t + "px"; el.style.width = Math.max(0, w) + "px"; el.style.height = Math.max(0, h) + "px";
  }
  /* Khoét vùng sáng: chỉ cập nhật DOM khi vùng thay đổi thật sự */
  function showHole(l, t, r, b) {
    if (shown && shown !== "full" && Math.abs(shown.l - l) < 1 && Math.abs(shown.t - t) < 1 && Math.abs(shown.r - r) < 1 && Math.abs(shown.b - b) < 1) return false;
    var W = innerWidth, H = innerHeight;
    if (shown === "full" || !shown) { dimParts[0].className = ""; for (var i = 1; i < 4; i++) dimParts[i].style.display = ""; }
    shown = { l: l, t: t, r: r, b: b };
    setPart(dimParts[0], 0, 0, W, t);                 // trên
    setPart(dimParts[1], 0, b, W, H - b);             // dưới
    setPart(dimParts[2], 0, t, l, b - t);             // trái
    setPart(dimParts[3], r, t, W - r, b - t);         // phải
    ring.style.display = "block";
    ring.style.width = (r - l) + "px"; ring.style.height = (b - t) + "px";
    ring.style.transform = "translate3d(" + l + "px," + t + "px,0)";
    return true;
  }
  var stable = null, orphanSince = 0;    // gom biên độ của mục tiêu đang trôi lơ lửng (đảo bay) để vùng sáng đứng yên
  function frame() {
    raf = requestAnimationFrame(frame);
    if (!cur && dim && !dim.hidden) {             // lớp tối "mồ côi" (đã bấm chuyển trang nhưng vẫn ở lại) → tự gỡ
      if (!orphanSince) orphanSince = Date.now();
      else if (Date.now() - orphanSince > 5000) { orphanSince = 0; resync(); }
    } else orphanSince = 0;
    if (!cur || !holeEl) return;               // chưa có mục tiêu (đang chờ trang tải)
    // Trang có thể vẽ lại danh sách (VD: cập nhật tiến độ) → tìm lại phần tử mới
    if (!holeEl.isConnected) { var re = document.querySelector(cur.hole); if (re) holeEl = re; }
    if (cur.click && (!clickEl || !clickEl.isConnected)) clickEl = document.querySelector(cur.click);
    var r = visible(holeEl);
    if (cur.need && !document.querySelector(cur.need)) r = null;

    if (cur.hole && !r) {
      if (cur.dim !== false) fullDim();
      ring.style.display = "none"; hand.style.display = "none"; handAt = null; stable = null;
      if (!lostSince) lostSince = Date.now();
      else if (Date.now() - lostSince > 700 && cur.back) { go(cur.back); }
      else if (Date.now() - lostSince > 1500 && !cur.back) { run(curId); }   // mất dấu mục tiêu → chạy lại bước
      return;
    }
    lostSince = 0;
    if (!r) return;
    var box4 = { l: r.left, t: r.top, r: r.right, b: r.bottom };
    if (cur.floaty) {
      // Đảo bay lên xuống liên tục: lấy khung bao cả biên độ trôi → vùng sáng không phải nhảy theo từng khung hình
      if (stable && Math.abs(stable.l - box4.l) < 60 && Math.abs(stable.t - box4.t) < 60) {
        stable = { l: Math.min(stable.l, box4.l), t: Math.min(stable.t, box4.t), r: Math.max(stable.r, box4.r), b: Math.max(stable.b, box4.b) };
      } else stable = box4;
      box4 = stable;
    }
    var p = 8;
    var l = Math.round(Math.max(0, box4.l - p)), t = Math.round(Math.max(0, box4.t - p)),
        rr = Math.round(Math.min(innerWidth, box4.r + p)), b = Math.round(Math.min(innerHeight, box4.b + p));
    var changed = cur.dim !== false ? showHole(l, t, rr, b) : false;
    var c = clickEl ? visible(clickEl) : null;
    if (c) {
      var hx = Math.round(c.left + c.width / 2), hy = Math.round(c.bottom - 6);
      if (hy > innerHeight - 40) hy = Math.round(c.top - 40);
      if (cur.floaty && handAt) { hx = handAt.x; hy = Math.max(hy, handAt.y); }
      if (!handAt || Math.abs(handAt.x - hx) >= 1 || Math.abs(handAt.y - hy) >= 1) {
        handAt = { x: hx, y: hy };
        hand.style.display = "block";
        hand.style.transform = "translate3d(" + hx + "px," + hy + "px,0)";
      }
    } else if (handAt) { hand.style.display = "none"; handAt = null; }
    if (changed && Date.now() - lastPlace > 350) { place(r); lastPlace = Date.now(); }
  }
  function overlap(a, b) { return !(a.right < b.left || a.left > b.right || a.bottom < b.top || a.top > b.bottom); }
  function place(target) {
    var mobile = innerWidth <= 700;
    var cands = mobile ? (box.classList.contains("tour") ? ["pos-bottom", "pos-top"] : ["pos-mid"]) : ["pos-mid", "pos-bottom", "pos-top"];
    if (!target && cur && cur.pos && !mobile) cands = [cur.pos];
    var pad = { left: target ? target.left - 10 : 0, right: target ? target.right + 10 : 0, top: target ? target.top - 10 : 0, bottom: target ? target.bottom + 10 : 0 };
    var chosen = cands[0], bestArea = Infinity;
    for (var i = 0; i < cands.length; i++) {
      box.classList.remove("pos-mid", "pos-top", "pos-bottom"); box.classList.add(cands[i]);
      if (!target) { chosen = cands[i]; break; }
      var r = box.getBoundingClientRect();
      if (!overlap(r, pad)) { chosen = cands[i]; break; }
      var ix = Math.max(0, Math.min(r.right, pad.right) - Math.max(r.left, pad.left)) * Math.max(0, Math.min(r.bottom, pad.bottom) - Math.max(r.top, pad.top));
      if (ix < bestArea) { bestArea = ix; chosen = cands[i]; }
    }
    box.classList.remove("pos-mid", "pos-top", "pos-bottom"); box.classList.add(chosen);
  }
  function clearSpot() {
    clearInterval(waitTimer); waitTimer = 0;
    holeEl = clickEl = null; stable = null;
    if (dimParts) fullDim();
  }

  /* ---------- CHẠY TỪNG BƯỚC ---------- */
  function waitFor(sel, cb, timeout) {
    var t0 = Date.now();
    clearInterval(waitTimer);
    var tick = function () {
      var el = sel && document.querySelector(sel);
      if (el && visible(el)) { clearInterval(waitTimer); waitTimer = 0; cb(el); return true; }
      if (Date.now() - t0 > (timeout || 12000)) { clearInterval(waitTimer); waitTimer = 0; cb(null); return true; }
      return false;
    };
    if (!tick()) waitTimer = setInterval(tick, 150);
  }
  function inView(el) { var r = el.getBoundingClientRect(); return r.top >= 60 && r.bottom <= innerHeight - 20; }

  function go(id) {
    var s = STEPS[id];
    if (!s) return finish(false);
    saveStep(id);
    if (s.page !== PAGE || (s.grade && QS.get("grade") !== s.grade)) return wrongPage(id);
    run(id);
  }
  function run(id) {
    var s = STEPS[id];
    clearSpot();
    cur = s; curId = id; lostSince = 0;
    document.body.classList.add("tg-on");
    box.classList.remove("idle"); box.classList.add("tour");
    var useDim = s.dim !== false;
    setDim(useDim);

    if (s.final) { showBye(); return; }

    var base = { n: s.n, title: s.title, text: s.text, skip: true, buttons: [] };
    if (s.action && s.action.fn === "scrollGame") base.buttons.push({ label: s.action.label, ghost: true, fn: scrollToGame });

    var start = function () {
      if (!s.hole) { bubble(base); place(null); if (s.until) watchUntil(s); return; }
      bubble({ n: s.n, title: s.title, text: "Đợi mình một chút nhé… ⏳", skip: true });
      waitFor(s.hole, function (el) {
        if (curId !== id) return;
        if (!el) {
          if (s.back) return go(s.back);
          bubble({ n: s.n, title: s.title, text: "Mình chưa tìm thấy mục cần chỉ trên trang này. Thử tải lại trang hoặc bắt đầu lại hướng dẫn nhé.", skip: true,
            buttons: [{ label: "↻ Thử lại", fn: function () { run(id); } }, { label: "Về trang chủ", ghost: true, fn: function () { saveStep("island"); location.href = URLS.index; } }] });
          return;
        }
        holeEl = el; clickEl = s.click ? document.querySelector(s.click) : null;
        if (!inView(el)) el.scrollIntoView({ behavior: "smooth", block: "center" });
        bubble(base); lastPlace = 0;
      }, s.need ? 3000 : 12000);
    };
    if (s.ready) waitFor(s.ready, function () { if (curId === id) start(); }, 15000);
    else start();
  }
  function watchUntil(s) {
    var target = document.querySelector(s.until);
    if (!target) return;
    var id = curId;
    var check = function () {
      if (curId !== id) { window.removeEventListener("scroll", check); return; }
      var r = target.getBoundingClientRect();
      if (r.top < innerHeight * 0.6 && r.bottom > 0) { window.removeEventListener("scroll", check); setTimeout(function () { if (curId === id) go(s.next); }, 250); }
    };
    window.addEventListener("scroll", check, { passive: true });
    check();
  }
  function scrollToGame() {
    var g = document.getElementById("gameSection");
    if (g) g.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  function showBye() {
    clearSpot();
    setDim(true);
    var gb = document.getElementById("gameButton");
    var hasGame = gb && visible(gb);
    var btns = [];
    if (hasGame) btns.push({ label: "🚀 Vào trải nghiệm ngay", fn: function () { finish(true); passThrough = true; gb.click(); passThrough = false; } });
    btns.push({ label: hasGame ? "Ở lại bài học" : "Kết thúc", ghost: !!hasGame, fn: function () { finish(true); } });
    bubble({ n: TOTAL, title: STEPS.bye.title, text: STEPS.bye.text, buttons: btns });
    place(null);
  }

  function wrongPage(id) {
    var s = STEPS[id];
    clearSpot(); cur = null; curId = null;
    setDim(false);
    document.body.classList.add("tg-on");
    box.classList.remove("idle"); box.classList.add("tour");
    var url = URLS[s.page];
    bubble({
      n: s.n, title: "Tiếp tục hướng dẫn?",
      text: "Bạn đang ở trang khác so với hướng dẫn. Bấm <b>Tiếp tục</b> để mình đưa bạn tới đúng chỗ nhé!",
      buttons: [
        { label: "Tiếp tục ▶", fn: function () { location.href = url; } },
        { label: "Thoát hướng dẫn", ghost: true, fn: function () { finish(false); } }
      ]
    });
    place(null);
  }

  function finish(completed) {
    clearSpot(); cur = null; curId = null;
    lsDel(LS_STATE); lsSet(LS_DONE, completed ? "1" : "skip");
    setDim(false);
    document.body.classList.remove("tg-on");
    box.classList.remove("tour"); box.classList.add("idle");
    if (PAGE === "index") {
      bubble({ text: completed ? "Chúc bạn học vui! Bấm vào mình bất cứ lúc nào để xem <b>phân tích học tập</b> hoặc hướng dẫn nhé 😊" : "Đã tắt hướng dẫn. Bấm vào mình để xem <b>phân tích học tập</b> hoặc xem lại hướng dẫn nhé 😊", close: hideBubble });
      place(null);
      setTimeout(hideBubble, 4500);
    } else {
      hideBubble(); box.style.display = "none";
    }
  }

  /* ---------- SỰ KIỆN ---------- */
  function onCaptureClick(e) {
    if (passThrough || !cur || !cur.click) return;
    var t = e.target && e.target.closest ? e.target.closest(cur.click) : null;
    if (!t) return;
    if (cur.intercept) {
      e.preventDefault(); e.stopImmediatePropagation();
      go(cur.next);
      return;
    }
    var next = cur.next, ns = STEPS[next];
    saveStep(next);
    if (ns && ns.page === PAGE) {
      var id = next; cur = null; clearSpot();
      setTimeout(function () { run(id); }, 220);
    } else {
      cur = null; clearSpot(); hideBubble();
    }
  }

  function onBotClick() {
    if (cur) { nudge(); return; }
    var st = getState();
    if (st) return go(st.step);
    hideBubble();
    openAssistant();
  }

  /* ---------- TRỢ LÝ HỌC TẬP (assistant.js, nạp khi cần) ---------- */
  var asstP = null;
  function loadAssistant() {
    if (window.HDLGAssistant) return Promise.resolve(window.HDLGAssistant);
    if (asstP) return asstP;
    asstP = new Promise(function (res, rej) {
      var sc = document.createElement("script"); sc.src = "/assistant.js"; sc.async = true;
      sc.onload = function () { window.HDLGAssistant ? res(window.HDLGAssistant) : rej(); };
      sc.onerror = function () { asstP = null; rej(); };
      document.head.appendChild(sc);
    });
    return asstP;
  }
  function openAssistant(tab) {
    loadAssistant().then(function (A) { A.open(tab); }, function () {
      bubble({ text: "Mình chưa tải được phần phân tích, kiểm tra mạng rồi thử lại nhé!", close: hideBubble,
        buttons: [{ label: "🧭 Xem hướng dẫn", fn: start }] });
      place(null);
    });
  }
  /* Mỗi ngày 1 lần trên trang chủ: nhắc có bao nhiêu gợi ý học tập */
  function dailyHint() {
    var t = new Date(), key = t.getFullYear() + "-" + (t.getMonth() + 1) + "-" + t.getDate();
    if (lsGet("hdlg_tri_hint") === key) return;
    setTimeout(function () {
      if (cur) return;
      loadAssistant().then(function (A) {
        var go = function () {
          A.analyze().then(function (r) {
            var n = A.count(r), top = A.topToday(r)[0];
            if (!n && !top) return;
            var tries = 0, iv = setInterval(function () {
              if (cur || ++tries > 60) { clearInterval(iv); return; }
              if (document.querySelector(".hdlg-ov, .hq-ov, .ta-ov, .dialog.open")) return;
              clearInterval(iv);
              lsSet("hdlg_tri_hint", key);
              bubble({
                text: "📊 Mình vừa xem qua việc học của bạn" + (n ? ": có <b>" + n + " việc nên làm</b> hôm nay." : ".") +
                  (top ? "<br>Gợi ý đầu tiên: <b>" + String(top.t).replace(/[<>&]/g, "") + "</b>" : ""),
                close: hideBubble,
                buttons: [{ label: "📊 Xem phân tích", fn: function () { hideBubble(); openAssistant(); } }]
              });
              place(null);
              setTimeout(function () { if (!cur) hideBubble(); }, 12000);
            }, 700);
          });
        };
        if (window.HDLG && HDLG.ready && HDLG.ready.then) HDLG.ready.then(go, go); else go();
      }, function () {});
    }, 2500);
  }
  function start() {
    lsDel(LS_DONE);
    if (PAGE !== "index") { saveStep("island"); location.href = URLS.index; return; }
    go("island");
  }

  /* Gợi ý lần đầu trên trang chủ: chờ hộp đăng nhập / popup đóng rồi mới hiện */
  function introHint() {
    if (lsGet(LS_DONE)) return;
    try { if (sessionStorage.getItem(SS_HIDE)) return; } catch (e) {}
    var shown = false;
    var t = setInterval(function () {
      if (cur || shown) { clearInterval(t); return; }
      if (document.querySelector(".hdlg-ov, .hq-ov, .dialog.open")) return;
      shown = true; clearInterval(t);
      bubble({
        text: "👋 Xin chào, mình là <b>Tri</b>!<br>Mình có thể <b>hướng dẫn</b> bạn dùng web, hoặc <b>phân tích việc học</b> và gợi ý nên học gì tiếp.",
        close: function () { hideBubble(); try { sessionStorage.setItem(SS_HIDE, "1"); } catch (e) {} },
        buttons: [{ label: "▶ Bắt đầu hướng dẫn", fn: start }, { label: "📊 Phân tích học tập", ghost: true, fn: function () { hideBubble(); openAssistant(); } }]
      });
      place(null);
    }, 600);
  }

  function init() {
    var st = getState();
    if (PAGE !== "index" && !st) return;          // trang khác: chỉ hiện khi đang có tour
    build();
    raf = requestAnimationFrame(frame);
    if (st) {
      var s = STEPS[st.step];
      if (s.page === PAGE && (!s.grade || QS.get("grade") === s.grade)) {
        // tải lại trang khi đang ở bước popup → quay lại bước trước
        run(s.need && s.back ? s.back : st.step);
      } else wrongPage(st.step);
    } else if (lsGet(LS_DONE)) dailyHint();
    else introHint();
  }

  /* Bấm Quay lại (trình duyệt / điện thoại) → trang được khôi phục từ bộ nhớ đệm (bfcache) đúng lúc
     lớp tối đang phủ để chuyển trang. Đồng bộ lại theo trạng thái hướng dẫn hiện tại để không bị kẹt màn tối. */
  function resync() {
    if (!box) { if (getState()) init(); return; }
    var st = getState();
    if (!st) {
      clearSpot(); cur = null; curId = null;
      setDim(false); hideBubble();
      document.body.classList.remove("tg-on");
      box.classList.remove("tour"); box.classList.add("idle");
      if (PAGE !== "index") box.style.display = "none";
      return;
    }
    box.style.display = "";
    var s = STEPS[st.step];
    if (s.page === PAGE && (!s.grade || QS.get("grade") === s.grade)) run(s.need && s.back ? s.back : st.step);
    else wrongPage(st.step);
  }
  window.addEventListener("pageshow", function (e) { if (e.persisted) resync(); });

  window.HDLGTour = {
    start: function () { build(); if (!raf) raf = requestAnimationFrame(frame); start(); },
    stop: function () { if (box) finish(false); },
    assistant: function (tab) { openAssistant(tab); },
    reset: function () { lsDel(LS_STATE); lsDel(LS_DONE); try { sessionStorage.removeItem(SS_HIDE); } catch (e) {} }
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
