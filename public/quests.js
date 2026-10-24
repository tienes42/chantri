/* =========================================================================
   HỌC ĐỂ LÀM GÌ — NHIỆM VỤ • THƯỞNG • CÀI ĐẶT • THOÁT • TIẾN TRÌNH
   Cần nạp sau auth.js:
     <script src="/firebase-config.js"></script>
     <script src="/auth.js"></script>
     <script src="/quests.js"></script>
   API: HDLGQ.openMissions() | openRewards() | openSettings() | openExit()
        HDLGQ.openProgress("physics"|"chemistry"|"math") | recordChallenge(...)
   Dữ liệu lưu ở localStorage "hdlg_quests" (auth.js tự đồng bộ lên Firebase)
   ========================================================================= */
(function () {
  "use strict";
  if (window.HDLGQ) return;

  var SUBJECTS = {
    physics:   { name: "Vật lý",  icon: "⚡", page: "physics.html",   color: "#38bdf8" },
    chemistry: { name: "Hóa học", icon: "🧪", page: "chemistry.html", color: "#34d399" },
    math:      { name: "Toán học", icon: "📐", page: "math.html",     color: "#a78bfa" }
  };

  /* ----- Nhiệm vụ hằng ngày (key = bộ đếm trong ngày) ----- */
  var MISSIONS = [
    { id: "qp", icon: "⚡", title: "Thử thách nhanh Vật lý", desc: "Hoàn thành 1 lượt Thử thách nhanh Vật lý", key: "quick_physics", goal: 1, reward: 5, go: "/challenge.html?subject=physics" },
    { id: "qc", icon: "🧪", title: "Thử thách nhanh Hóa học", desc: "Hoàn thành 1 lượt Thử thách nhanh Hóa học", key: "quick_chemistry", goal: 1, reward: 5, go: "/challenge.html?subject=chemistry" },
    { id: "qm", icon: "📐", title: "Thử thách nhanh Toán", desc: "Hoàn thành 1 lượt Thử thách nhanh Toán", key: "quick_math", goal: 1, reward: 5, go: "/challenge.html?subject=math" },
    { id: "cr", icon: "🎯", title: "Nhà thông thái", desc: "Trả lời đúng 15 câu trong các Thử thách nhanh", key: "correct", goal: 15, reward: 8, go: "/challenge.html" },
    { id: "hi", icon: "🏅", title: "Phản xạ siêu tốc", desc: "Đạt từ 8/10 câu đúng trong một lượt", key: "great", goal: 1, reward: 10, go: "/challenge.html" },
    { id: "gm", icon: "🎮", title: "Nhà thực nghiệm", desc: "Chơi xong 1 mini game trong bài học", key: "game", goal: 1, reward: 5, go: "/physics.html" }
    ,{ id: "ls", icon: "📖", title: "Chăm học", desc: "Học xong 1 bài học mới (đọc hết bài)", key: "lesson", goal: 1, reward: 5, go: "/physics.html" }
  ];
  var BONUS = 10; // rương khi xong hết nhiệm vụ ngày

  /* ----- Điểm danh 7 ngày ----- */
  var CHECKIN = [2, 3, 4, 5, 6, 8, 15];

  /* ----- Thành tựu (nhận 1 lần) ----- */
  var ACH = [
    { id: "a1", icon: "🚀", title: "Khởi động", desc: "Hoàn thành 1 lượt Thử thách nhanh", reward: 5, ok: function (s) { return (s.total.quick || 0) >= 1; } },
    { id: "a2", icon: "🔥", title: "Chiến binh thử thách", desc: "Hoàn thành 10 lượt Thử thách nhanh", reward: 20, ok: function (s) { return (s.total.quick || 0) >= 10; } },
    { id: "a3", icon: "🧠", title: "Bộ não vàng", desc: "Trả lời đúng tổng cộng 100 câu", reward: 30, ok: function (s) { return (s.total.correct || 0) >= 100; } },
    { id: "a4", icon: "💯", title: "Hoàn hảo", desc: "Đạt 10/10 câu đúng trong một lượt", reward: 15, ok: function (s) { return (s.total.perfect || 0) >= 1; } },
    { id: "a5", icon: "🌈", title: "Đa năng", desc: "Chơi Thử thách nhanh cả 3 môn Lý – Hóa – Toán", reward: 10, ok: function (s) { return ["physics", "chemistry", "math"].every(function (k) { return s.subj[k] && s.subj[k].plays > 0; }); } },
    { id: "a6", icon: "📅", title: "Chuyên cần", desc: "Điểm danh 7 ngày liên tiếp", reward: 25, ok: function (s) { return (s.checkin.best || 0) >= 7; } },
    { id: "a7", icon: "⭐", title: "Ngôi sao đang lên", desc: "Đạt cấp độ Lv.5", reward: 20, ok: function () { return level() >= 5; } }
    ,{ id: "a8", icon: "📚", title: "Mọt sách", desc: "Học xong 10 bài học", reward: 20, ok: function (s) { return (s.total.lesson || 0) >= 10; } }
  ];

  /* ---------- tiện ích ---------- */
  function H() { return window.HDLG; }
  function jparse(s, d) { try { var v = JSON.parse(s); return v == null ? d : v; } catch (e) { return d; } }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function stars() { return H() ? H().getStars() : (parseInt(localStorage.getItem("hdlg_xp"), 10) || 0); }
  function level() { return Math.floor(stars() / 100) + 1; }
  function toast(m) { if (H() && H().toast) H().toast(m); }
  function getState() {
    if (H() && H().questGet) return H().questGet();
    return { day: "", prog: {}, claimed: [], qbest: {}, total: {}, subj: {}, ach: [], checkin: { last: "", streak: 0 } };
  }
  function save(s) { if (H() && H().questSave) H().questSave(s); refreshBadges(); }
  function give(n, label) { if (n > 0 && H()) H().addStars(n, label); }
  function dayStr(d) { function p(n) { return (n < 10 ? "0" : "") + n; } return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate()); }
  function yesterday() { var d = new Date(); d.setDate(d.getDate() - 1); return dayStr(d); }
  function todayStr() { return dayStr(new Date()); }

  /* ---------- cài đặt (chỉ lưu trên máy) ---------- */
  var SKEY = "hdlg_settings";
  function settings() {
    var s = jparse(localStorage.getItem(SKEY), {});
    return { sound: s.sound !== false, calm: !!s.calm, time: [10, 15, 20, 30].indexOf(s.time) >= 0 ? s.time : 15 };
  }
  function setSettings(p) {
    var s = settings(); for (var k in p) s[k] = p[k];
    localStorage.setItem(SKEY, JSON.stringify(s)); applySettings(); return s;
  }
  function applySettings() { document.documentElement.classList.toggle("hq-calm", settings().calm); }

  /* ---------- trạng thái nhiệm vụ ---------- */
  function missionInfo(s) {
    return MISSIONS.map(function (m) {
      var v = Math.min(m.goal, s.prog[m.key] || 0);
      return { m: m, v: v, done: v >= m.goal, claimed: s.claimed.indexOf(m.id) >= 0 };
    });
  }
  function counts() {
    var s = getState(), mi = missionInfo(s);
    var mClaim = mi.filter(function (x) { return x.done && !x.claimed; }).length;
    if (!s.bonus && mi.every(function (x) { return x.claimed; })) mClaim++;
    var rClaim = (s.checkin.last !== todayStr() ? 1 : 0) +
      ACH.filter(function (a) { return s.ach.indexOf(a.id) < 0 && a.ok(s); }).length;
    return { missions: mClaim, rewards: rClaim };
  }
  function refreshBadges() {
    var c = counts();
    document.querySelectorAll("[data-hq-badge]").forEach(function (el) {
      var n = c[el.getAttribute("data-hq-badge")] || 0;
      if (n > 0) el.setAttribute("data-hq-n", n); else el.removeAttribute("data-hq-n");
    });
  }

  /* ---------- ghi nhận một lượt Thử thách nhanh ---------- */
  function recordChallenge(subject, correct, total, score) {
    var s = getState(), before = missionInfo(s);
    s.prog["quick_" + subject] = (s.prog["quick_" + subject] || 0) + 1;
    s.prog.correct = (s.prog.correct || 0) + correct;
    if (correct >= 8) s.prog.great = (s.prog.great || 0) + 1;
    s.total.quick = (s.total.quick || 0) + 1;
    s.total.correct = (s.total.correct || 0) + correct;
    s.total.answered = (s.total.answered || 0) + total;
    if (correct === total) s.total.perfect = (s.total.perfect || 0) + 1;
    var st = s.subj[subject] || { plays: 0, best: 0, correct: 0, answered: 0, bestScore: 0 };
    st.plays++; st.correct += correct; st.answered += total;
    st.best = Math.max(st.best, correct); st.bestScore = Math.max(st.bestScore, score); st.last = todayStr();
    s.subj[subject] = st;
    var earned = Math.floor(score / 10), prev = s.qbest[subject] || 0, gain = Math.max(0, earned - prev);
    if (gain > 0) s.qbest[subject] = earned;
    save(s);
    if (gain > 0) give(gain, "Thử thách nhanh");
    var after = missionInfo(s), newly = [];
    after.forEach(function (x, i) { if (x.done && !before[i].done) newly.push(x.m); });
    return { gain: gain, earned: earned, todayBest: Math.max(prev, earned), newlyDone: newly, missions: after };
  }

  /* ---------- giao diện chung ---------- */
  var CSS = "\
html.hq-calm .island-float,html.hq-calm .island-float-center,html.hq-calm .cloud,html.hq-calm .actor,html.hq-calm .center-aura-ring,html.hq-calm .rune-btn,html.hq-calm .ai-hint,html.hq-calm .relic,html.hq-calm .poly-relic,html.hq-calm .chem-relic,html.hq-calm .m-relic,html.hq-calm .astrolabe-ring,html.hq-calm .sacred-geometry-wheel,html.hq-calm .molecular-wheel,html.hq-calm .celestial-wheel,html.hq-calm .sacred-wheel,html.hq-calm .orbit,html.hq-calm .geo-ring,html.hq-calm .chem-ring,html.hq-calm .orbit-ring{animation:none!important}\
html.hq-calm #cinematicCanvas,html.hq-calm #physicsCanvas,html.hq-calm #mathCanvas,html.hq-calm #chemistryCanvas,html.hq-calm #gradeCanvas,html.hq-calm .flying-bird-group,html.hq-calm .god-rays,html.hq-calm .quantum-rays,html.hq-calm .golden-rays,html.hq-calm .elixir-rays,html.hq-calm .ambient-rays,html.hq-calm .chem-boom,html.hq-calm .chem-smoke,html.hq-calm .spark,html.hq-calm .lava,html.hq-calm .rainbow,html.hq-calm .bird-paper,html.hq-calm .butterfly,html.hq-calm .hammer,html.hq-calm .music-fx,html.hq-calm .crown,html.hq-calm .fx-math{display:none!important}\
[data-hq-n]::after{content:attr(data-hq-n);position:absolute;top:4px;right:6px;min-width:20px;height:20px;padding:0 5px;box-sizing:border-box;border-radius:10px;background:#ff4757;color:#fff;font:700 12px/20px 'Segoe UI',Arial,sans-serif;text-align:center;box-shadow:0 0 0 2px #0c1a38,0 0 12px #ff4757;z-index:5;pointer-events:none}\
.hq-ov{position:fixed;inset:0;z-index:99990;display:flex;align-items:center;justify-content:center;padding:14px;background:rgba(5,12,30,.74);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);font-family:'Segoe UI',Roboto,Arial,sans-serif}\
.hq-box{position:relative;width:100%;max-width:520px;max-height:90vh;overflow:auto;background:linear-gradient(160deg,#16325f,#0b1733);color:#eaf2ff;border:1px solid #4a74c9;border-radius:20px;padding:22px 20px 20px;box-shadow:0 24px 70px rgba(0,0,0,.6);animation:hqBoxIn .18s ease-out}\
@keyframes hqBoxIn{from{transform:translateY(10px) scale(.97)}to{transform:translateY(0) scale(1)}}\
.hq-box h2{margin:0 0 4px;text-align:center;font-size:23px;color:#ffe27a}\
.hq-sub{margin:0 0 14px;text-align:center;color:#a9bde6;font-size:13px}\
.hq-x{position:absolute;top:10px;right:14px;background:none;border:0;color:#a9bde6;font-size:26px;cursor:pointer;line-height:1}\
.hq-x:hover{color:#fff}\
.hq-item{display:flex;align-items:center;gap:12px;padding:11px 12px;border-radius:14px;background:#ffffff0f;border:1px solid #ffffff14;margin-bottom:8px}\
.hq-item.ok{border-color:#ffd65d88;background:#ffd65d14}\
.hq-item.got{opacity:.6}\
.hq-ic{width:42px;height:42px;flex:none;border-radius:12px;background:#ffffff14;display:flex;align-items:center;justify-content:center;font-size:22px}\
.hq-mid{flex:1;min-width:0}\
.hq-mid b{display:block;font-size:15px}\
.hq-mid small{display:block;color:#a9bde6;font-size:12px;margin:2px 0 6px}\
.hq-bar{height:7px;border-radius:5px;background:#ffffff1c;overflow:hidden}\
.hq-bar i{display:block;height:100%;border-radius:5px;background:linear-gradient(90deg,#62d7ff,#ffd65d)}\
.hq-pv{font-size:11px;color:#a9bde6;margin-top:3px}\
.hq-btn{flex:none;border:0;border-radius:10px;padding:8px 12px;font:700 13px 'Segoe UI',Arial,sans-serif;cursor:pointer;background:#2b5bb5;color:#fff;white-space:nowrap}\
.hq-btn:hover{filter:brightness(1.15)}\
.hq-btn.y{background:linear-gradient(135deg,#ffe27a,#ffb703);color:#3a2500;box-shadow:0 0 14px #ffb70377}\
.hq-btn.ghost{background:transparent;border:1px solid #6d8fd8;color:#cfe0ff}\
.hq-btn.red{background:#e5484d}\
.hq-btn[disabled]{opacity:.55;cursor:default;filter:none}\
.hq-wide{display:block;width:100%;padding:12px;margin-top:10px;font-size:15px}\
.hq-chest{display:flex;align-items:center;gap:12px;padding:12px;border-radius:14px;margin-top:6px;background:linear-gradient(135deg,#3b2a07,#1d2a52);border:1px dashed #ffd65d99}\
.hq-tabs{display:flex;gap:6px;margin:6px 0 14px;background:#ffffff0d;padding:4px;border-radius:12px}\
.hq-tabs button{flex:1;border:0;border-radius:9px;padding:9px;background:none;color:#a9bde6;font:700 14px 'Segoe UI',Arial,sans-serif;cursor:pointer;position:relative}\
.hq-tabs button.on{background:#2b5bb5;color:#fff}\
.hq-days{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:12px}\
.hq-day{border-radius:12px;padding:8px 2px;text-align:center;background:#ffffff0f;border:1px solid #ffffff14;font-size:11px;color:#a9bde6}\
.hq-day b{display:block;font-size:18px;margin:2px 0}\
.hq-day.got{background:#22c55e22;border-color:#22c55e88;color:#bbf7d0}\
.hq-day.now{background:#ffd65d22;border-color:#ffd65d;color:#ffe9a3;box-shadow:0 0 14px #ffd65d55}\
.hq-row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px;border-radius:12px;background:#ffffff0f;margin-bottom:8px}\
.hq-row span{font-size:14px}\
.hq-row small{display:block;color:#a9bde6;font-size:12px}\
.hq-sw{position:relative;width:48px;height:26px;flex:none;border-radius:13px;background:#ffffff26;border:0;cursor:pointer;transition:background .2s}\
.hq-sw::after{content:'';position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;transition:left .2s}\
.hq-sw.on{background:#22c55e}.hq-sw.on::after{left:25px}\
.hq-seg{display:flex;gap:4px}\
.hq-seg button{border:1px solid #4a74c9;background:none;color:#cfe0ff;border-radius:8px;padding:6px 9px;cursor:pointer;font:600 13px 'Segoe UI',Arial,sans-serif}\
.hq-seg button.on{background:#2b5bb5;color:#fff;border-color:#62d7ff}\
.hq-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:8px 0 14px}\
.hq-stats div{text-align:center;background:#ffffff10;border-radius:12px;padding:10px 4px}\
.hq-stats b{display:block;font-size:21px;color:#ffd65d}\
.hq-stats small{color:#a9bde6;font-size:11px}\
.hq-subj{border-radius:14px;padding:12px;margin-bottom:8px;background:#ffffff0c;border:1px solid #ffffff14}\
.hq-subj.hl{border-color:var(--c);box-shadow:0 0 16px color-mix(in srgb,var(--c) 40%,transparent)}\
.hq-subj h4{margin:0 0 8px;display:flex;align-items:center;gap:8px;font-size:15px}\
.hq-subj h4 em{margin-left:auto;font-style:normal}\
.hq-kv{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;text-align:center;font-size:11px;color:#a9bde6}\
.hq-kv b{display:block;color:#fff;font-size:16px}\
.hq-note{font-size:12px;color:#8ea6d6;text-align:center;margin-top:10px}\
@media(max-width:520px){.hq-stats,.hq-kv{grid-template-columns:repeat(2,1fr)}.hq-day b{font-size:15px}}";

  var ov = null;
  function close() { if (ov) { ov.remove(); ov = null; } document.removeEventListener("keydown", onKey); }
  function onKey(e) { if (e.key === "Escape") close(); }
  function open(html, maxW) {
    close();
    ov = document.createElement("div"); ov.className = "hq-ov";
    ov.innerHTML = '<div class="hq-box"' + (maxW ? ' style="max-width:' + maxW + 'px"' : "") + '><button class="hq-x" aria-label="Đóng">×</button>' + html + "</div>";
    ov.addEventListener("mousedown", function (e) { if (e.target === ov) close(); });
    ov.querySelector(".hq-x").onclick = close;
    document.body.appendChild(ov); document.addEventListener("keydown", onKey);
    return ov;
  }
  function bar(v, g) { return '<div class="hq-bar"><i style="width:' + Math.round(100 * v / g) + '%"></i></div>'; }
  function resetIn() {
    var n = new Date(), m = new Date(n); m.setHours(24, 0, 0, 0);
    var t = Math.max(0, m - n), h = Math.floor(t / 3600000), mi = Math.floor(t % 3600000 / 60000);
    return h + " giờ " + mi + " phút";
  }

  /* ---------- NHIỆM VỤ ---------- */
  function openMissions() {
    var s = getState(), mi = missionInfo(s), all = mi.every(function (x) { return x.claimed; });
    var html = "<h2>📜 Nhiệm vụ hằng ngày</h2><p class='hq-sub'>Làm mới sau " + resetIn() + " · Thử thách nhanh sẽ tự cập nhật tiến độ</p>";
    mi.forEach(function (x, i) {
      var btn = x.claimed ? '<button class="hq-btn" disabled>✓ Đã nhận</button>'
        : x.done ? '<button class="hq-btn y" data-claim="' + i + '">Nhận ⭐' + x.m.reward + "</button>"
        : '<button class="hq-btn ghost" data-go="' + x.m.go + '">Làm ngay</button>';
      html += '<div class="hq-item' + (x.claimed ? " got" : x.done ? " ok" : "") + '"><div class="hq-ic">' + x.m.icon + '</div><div class="hq-mid"><b>' + esc(x.m.title) +
        "</b><small>" + esc(x.m.desc) + " · ⭐ " + x.m.reward + "</small>" + bar(x.v, x.m.goal) + '<div class="hq-pv">' + x.v + "/" + x.m.goal + "</div></div>" + btn + "</div>";
    });
    html += '<div class="hq-chest"><div class="hq-ic">🎁</div><div class="hq-mid"><b>Rương hoàn thành</b><small>Nhận hết 6 nhiệm vụ để mở rương ⭐ ' + BONUS + "</small></div>" +
      (s.bonus ? '<button class="hq-btn" disabled>✓ Đã mở</button>' : '<button class="hq-btn y" id="hqBonus"' + (all ? "" : " disabled") + ">Mở rương</button>") + "</div>";
    html += '<button class="hq-btn hq-wide" data-go="/challenge.html">🎯 Vào Thử thách nhanh</button>';
    var o = open(html);
    o.querySelectorAll("[data-go]").forEach(function (b) { b.onclick = function () { location.href = b.getAttribute("data-go"); }; });
    o.querySelectorAll("[data-claim]").forEach(function (b) {
      b.onclick = function () {
        var st = getState(), x = missionInfo(st)[+b.getAttribute("data-claim")];
        if (!x || !x.done || x.claimed) return;
        st.claimed.push(x.m.id); save(st); give(x.m.reward, "Nhiệm vụ: " + x.m.title); openMissions();
      };
    });
    var bo = o.querySelector("#hqBonus");
    if (bo) bo.onclick = function () {
      var st = getState(); if (st.bonus || !missionInfo(st).every(function (x) { return x.claimed; })) return;
      st.bonus = true; save(st); give(BONUS, "Rương nhiệm vụ"); openMissions();
    };
  }

  /* ---------- THƯỞNG ---------- */
  function checkinInfo(s) {
    var t = todayStr(), c = s.checkin, done = c.last === t;
    var streak = done ? c.streak : (c.last === yesterday() ? c.streak : 0);
    var cycle = done ? ((streak - 1) % 7) : (streak % 7);
    return { done: done, streak: streak, idx: cycle };
  }
  function openRewards(tab) {
    tab = tab || "daily";
    var s = getState(), ci = checkinInfo(s), c = counts();
    var html = "<h2>🎁 Phần thưởng</h2><p class='hq-sub'>Điểm danh mỗi ngày và mở khóa thành tựu để nhận thêm sao</p>" +
      '<div class="hq-tabs"><button data-tab="daily" class="' + (tab === "daily" ? "on" : "") + '">📅 Điểm danh</button><button data-tab="ach" class="' + (tab === "ach" ? "on" : "") + '">🏆 Thành tựu</button></div>';
    if (tab === "daily") {
      html += '<div class="hq-days">';
      CHECKIN.forEach(function (r, i) {
        var cls = i < ci.idx || (ci.done && i === ci.idx) ? "got" : (!ci.done && i === ci.idx ? "now" : "");
        html += '<div class="hq-day ' + cls + '">Ngày ' + (i + 1) + "<b>" + (cls === "got" ? "✅" : i === 6 ? "👑" : "⭐") + "</b>+" + r + "</div>";
      });
      html += "</div><p class='hq-sub'>🔥 Chuỗi điểm danh: <b>" + ci.streak + " ngày</b>" + (s.checkin.best ? " · Kỷ lục: " + s.checkin.best + " ngày" : "") + "<br>Bỏ lỡ 1 ngày chuỗi sẽ bắt đầu lại từ Ngày 1.</p>" +
        (ci.done ? '<button class="hq-btn hq-wide" disabled>✓ Hôm nay đã điểm danh – quay lại vào ngày mai nhé!</button>'
                 : '<button class="hq-btn y hq-wide" id="hqCheck">Điểm danh nhận ⭐ ' + CHECKIN[ci.idx] + "</button>");
    } else {
      ACH.forEach(function (a) {
        var got = s.ach.indexOf(a.id) >= 0, ok = a.ok(s);
        html += '<div class="hq-item' + (got ? " got" : ok ? " ok" : "") + '"><div class="hq-ic">' + a.icon + '</div><div class="hq-mid"><b>' + esc(a.title) + "</b><small>" + esc(a.desc) + " · ⭐ " + a.reward + "</small></div>" +
          (got ? '<button class="hq-btn" disabled>✓ Đã nhận</button>' : ok ? '<button class="hq-btn y" data-ach="' + a.id + '">Nhận</button>' : '<button class="hq-btn ghost" disabled>🔒 Chưa đạt</button>') + "</div>";
      });
    }
    var o = open(html);
    o.querySelectorAll("[data-tab]").forEach(function (b) {
      if (b.getAttribute("data-tab") === "ach" && c.rewards - (ci.done ? 0 : 1) > 0) b.setAttribute("data-hq-n", c.rewards - (ci.done ? 0 : 1));
      if (b.getAttribute("data-tab") === "daily" && !ci.done) b.setAttribute("data-hq-n", 1);
      b.onclick = function () { openRewards(b.getAttribute("data-tab")); };
    });
    var ck = o.querySelector("#hqCheck");
    if (ck) ck.onclick = function () {
      var st = getState(), info = checkinInfo(st); if (info.done) return;
      var r = CHECKIN[info.idx];
      st.checkin.streak = info.streak + 1; st.checkin.last = todayStr();
      st.checkin.best = Math.max(st.checkin.best || 0, st.checkin.streak);
      save(st); give(r, "Điểm danh ngày " + (info.idx + 1)); openRewards("daily");
    };
    o.querySelectorAll("[data-ach]").forEach(function (b) {
      b.onclick = function () {
        var st = getState(), id = b.getAttribute("data-ach"), a = ACH.filter(function (x) { return x.id === id; })[0];
        if (!a || st.ach.indexOf(id) >= 0 || !a.ok(st)) return;
        st.ach.push(id); save(st); give(a.reward, "Thành tựu: " + a.title); openRewards("ach");
      };
    });
  }

  /* ---------- CÀI ĐẶT ---------- */
  function openSettings() {
    var st = settings(), u = H() && H().user;
    var acc = u ? (u.isAnonymous ? "Đang chơi với tư cách khách" : (u.displayName || u.email || "Đã đăng nhập")) : "Chưa đăng nhập";
    var html = "<h2>⚙️ Cài đặt</h2><p class='hq-sub'>Các tùy chọn được lưu trên thiết bị này</p>" +
      '<div class="hq-row"><span>🔊 Âm thanh hiệu ứng<small>Tiếng đúng/sai trong Thử thách nhanh</small></span><button class="hq-sw' + (st.sound ? " on" : "") + '" id="hqSound" aria-label="Âm thanh"></button></div>' +
      '<div class="hq-row"><span>🌙 Giảm hiệu ứng chuyển động<small>Dừng các hoạt ảnh bay lượn – giúp máy yếu chạy mượt hơn</small></span><button class="hq-sw' + (st.calm ? " on" : "") + '" id="hqCalm" aria-label="Giảm hiệu ứng"></button></div>' +
      '<div class="hq-row"><span>⏱️ Thời gian mỗi câu<small>Áp dụng cho Thử thách nhanh</small></span><div class="hq-seg" id="hqTime">' +
      [10, 15, 20, 30].map(function (t) { return '<button data-t="' + t + '" class="' + (st.time === t ? "on" : "") + '">' + t + "s</button>"; }).join("") + "</div></div>" +
      '<div class="hq-row"><span>🖥️ Toàn màn hình<small>Bật/tắt chế độ toàn màn hình</small></span><button class="hq-btn ghost" id="hqFull">' + (document.fullscreenElement ? "Thoát" : "Bật") + "</button></div>" +
      '<div class="hq-row"><span>👤 Tài khoản<small>' + esc(acc) + '</small></span><button class="hq-btn ghost" id="hqAcc">Quản lý</button></div>';
    var o = open(html, 480);
    o.querySelector("#hqSound").onclick = function () { this.classList.toggle("on", setSettings({ sound: !settings().sound }).sound); };
    o.querySelector("#hqCalm").onclick = function () { this.classList.toggle("on", setSettings({ calm: !settings().calm }).calm); };
    o.querySelectorAll("#hqTime button").forEach(function (b) {
      b.onclick = function () { setSettings({ time: +b.getAttribute("data-t") }); o.querySelectorAll("#hqTime button").forEach(function (x) { x.classList.toggle("on", x === b); }); };
    });
    o.querySelector("#hqFull").onclick = function () {
      var b = this;
      if (document.fullscreenElement) document.exitFullscreen().then(function () { b.textContent = "Bật"; });
      else if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().then(function () { b.textContent = "Thoát"; }).catch(function () {});
    };
    o.querySelector("#hqAcc").onclick = function () {
      close();
      if (H() && H().user) H().showAccount(); else if (H() && H().configured) H().showLogin(); else toast("Chưa cấu hình Firebase nên chưa có tài khoản");
    };
  }

  /* ---------- THOÁT ---------- */
  function openExit() {
    var u = H() && H().user;
    var html = "<h2>🚪 Thoát</h2><p class='hq-sub'>Tiến trình và số sao của bạn đã được lưu tự động.</p>" +
      (u ? '<button class="hq-btn red hq-wide" id="hqOut">' + (u.isAnonymous ? "Thoát chế độ khách" : "Đăng xuất tài khoản") + "</button>" : "") +
      '<button class="hq-btn ghost hq-wide" id="hqLeave">Rời khỏi trang web</button>' +
      '<button class="hq-btn y hq-wide" id="hqStay">Ở lại học tiếp</button>';
    var o = open(html, 400);
    o.querySelector("#hqStay").onclick = close;
    o.querySelector("#hqLeave").onclick = function () {
      if (H() && H().flush) H().flush();
      setTimeout(function () { window.close(); location.href = "about:blank"; }, 300);
    };
    var out = o.querySelector("#hqOut");
    if (out) out.onclick = function () {
      if (u.isAnonymous && !confirm("Tài khoản khách sẽ bị mất toàn bộ sao nếu chưa nâng cấp. Vẫn thoát?")) return;
      out.disabled = true; out.textContent = "Đang lưu & đăng xuất…"; H().logout();
    };
  }

  /* ---------- TIẾN TRÌNH / HỒ SƠ ---------- */
  function openProgress(subject) {
    var s = getState(), x = stars(), done = jparse(localStorage.getItem("hdlg_completed"), []);
    var nDone = Array.isArray(done) ? done.length : Object.keys(done || {}).length;
    var mi = missionInfo(s), mDone = mi.filter(function (m) { return m.claimed; }).length;
    var html = "<h2>📊 Hồ sơ tiến trình</h2><p class='hq-sub'>Lv." + level() + " · " + (x % 100) + "/100 sao để lên cấp tiếp theo</p>" + bar(x % 100, 100) +
      '<div class="hq-stats"><div><b>' + x + "</b><small>Tổng sao</small></div><div><b>" + nDone + "</b><small>Bài/màn đã qua</small></div><div><b>" +
      (s.checkin.streak && (s.checkin.last === todayStr() || s.checkin.last === yesterday()) ? s.checkin.streak : 0) + "🔥</b><small>Chuỗi điểm danh</small></div><div><b>" + mDone + "/" + MISSIONS.length + "</b><small>Nhiệm vụ hôm nay</small></div></div>";
    var order = ["physics", "chemistry", "math"];
    if (subject && order.indexOf(subject) > 0) { order.splice(order.indexOf(subject), 1); order.unshift(subject); }
    order.forEach(function (k) {
      var sb = SUBJECTS[k], d = s.subj[k] || { plays: 0, best: 0, correct: 0, answered: 0 };
      var acc = d.answered ? Math.round(100 * d.correct / d.answered) + "%" : "—";
      html += '<div class="hq-subj' + (k === subject ? " hl" : "") + '" style="--c:' + sb.color + '"><h4>' + sb.icon + " Thử thách nhanh " + sb.name +
        "<em>⭐ hôm nay " + (s.qbest[k] || 0) + "/15</em></h4>" +
        '<div class="hq-kv"><div><b>' + d.plays + "</b>Lượt chơi</div><div><b>" + d.best + "/10</b>Kỷ lục</div><div><b>" + acc + "</b>Độ chính xác</div><div><b>" + d.correct + "</b>Câu đúng</div></div>" +
        bar(d.answered ? d.correct : 0, d.answered || 1) + "</div>";
    });
    html += '<div style="display:flex;gap:8px;margin-top:6px"><button class="hq-btn y" style="flex:1;padding:12px" id="hqGoC">🎯 Thử thách nhanh</button><button class="hq-btn" style="flex:1;padding:12px" id="hqGoM">📜 Nhiệm vụ</button></div>' +
      "<p class='hq-note'>Mẹo: mỗi môn nhận tối đa 15 sao/ngày từ Thử thách nhanh – hãy phá kỷ lục của chính mình!</p>";
    var o = open(html, 560);
    o.querySelector("#hqGoC").onclick = function () { location.href = "/challenge.html" + (subject ? "?subject=" + subject : ""); };
    o.querySelector("#hqGoM").onclick = openMissions;
  }

  /* ---------- khởi động ---------- */
  function boot() {
    var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
    applySettings(); refreshBadges();
    window.addEventListener("hdlg:update", refreshBadges);
    window.addEventListener("hdlg:quests", refreshBadges);
    if (H() && H().ready) H().ready.then(refreshBadges);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();

  window.HDLGQ = {
    SUBJECTS: SUBJECTS, MISSIONS: MISSIONS, settings: settings, setSettings: setSettings,
    openMissions: openMissions, openRewards: openRewards, openSettings: openSettings, openExit: openExit,
    openProgress: openProgress, recordChallenge: recordChallenge, state: getState, close: close, refresh: refreshBadges
  };
})();