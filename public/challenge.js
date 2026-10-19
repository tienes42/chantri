/* =========================================================
   THỬ THÁCH NHANH — Vật lý • Hóa học • Toán
   challenge.html?subject=physics | chemistry | math
   - 10 câu / lượt, có giới hạn thời gian (đổi trong Cài đặt)
   - Đúng: +10 điểm + thưởng tốc độ (tối đa +5)  → tối đa 150 điểm
   - Sao = điểm / 10, mỗi môn tối đa 15 sao/ngày (chỉ cộng phần vượt kỷ lục hôm nay)
   - Kết quả cập nhật Nhiệm vụ hằng ngày (quests.js)
========================================================= */
(function () {
  "use strict";
  var QN = 10;
  var BANK = window.HDLG_QUESTIONS || {};
  var SUB = {
    physics:   { name: "Vật lý",  icon: "⚡", page: "/physics.html",   desc: "Lực, điện, ánh sáng, năng lượng" },
    chemistry: { name: "Hóa học", icon: "🧪", page: "/chemistry.html", desc: "Chất, phản ứng và đời sống" },
    math:      { name: "Toán",    icon: "📐", page: "/math.html",      desc: "Số, hình học và ứng dụng" }
  };
  var RANGES = [
    { id: "all", label: "Tất cả lớp", min: 6, max: 12 },
    { id: "thcs", label: "THCS (lớp 6–9)", min: 6, max: 9 },
    { id: "thpt", label: "THPT (lớp 10–12)", min: 10, max: 12 }
  ];
  var app = document.getElementById("app");
  var params = new URLSearchParams(location.search);
  var subject = SUB[params.get("subject")] ? params.get("subject") : null;
  var range = localStorage.getItem("hdlg_qc_range") || "all";
  var game = null, tick = null;

  function Q() { return window.HDLGQ; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function secs() { return Q() ? Q().settings().time : 15; }
  function sound() { return Q() ? Q().settings().sound : true; }

  /* ---------- âm thanh ---------- */
  var actx = null;
  function beep(type) {
    if (!sound()) return;
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      var notes = type === "ok" ? [660, 880] : type === "bad" ? [220, 160] : type === "end" ? [523, 659, 784, 1046] : [440];
      notes.forEach(function (f, i) {
        var o = actx.createOscillator(), g = actx.createGain(), t = actx.currentTime + i * 0.11;
        o.type = type === "bad" ? "sawtooth" : "sine"; o.frequency.value = f;
        g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.18, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.18);
        o.connect(g); g.connect(actx.destination); o.start(t); o.stop(t + 0.2);
      });
    } catch (e) {}
  }

  /* ---------- header ---------- */
  function setHeader() {
    document.body.className = subject ? "s-" + subject : "";
    document.getElementById("ttlIcon").textContent = subject ? SUB[subject].icon : "🎯";
    document.getElementById("ttlText").textContent = subject ? "THỬ THÁCH NHANH " + SUB[subject].name.toUpperCase() : "ĐẤU TRƯỜNG THỬ THÁCH";
    document.title = (subject ? "Thử thách " + SUB[subject].name : "Thử thách nhanh") + " - HỌC ĐỂ LÀM GÌ";
  }
  function updStars() { document.getElementById("starCount").textContent = window.HDLG ? HDLG.getStars() : 0; }
  window.addEventListener("hdlg:update", updStars);
  document.getElementById("missionBtn").onclick = function () { if (Q()) Q().openMissions(); };
  document.getElementById("backBtn").onclick = function () {
    if (game && !game.over) {
      if (!confirm("Bạn đang làm dở lượt thử thách. Thoát sẽ không được tính kết quả. Vẫn thoát?")) return;
      stopTimer(); game = null;
    }
    if (subject && !params.get("subject")) { subject = null; showPick(); return; }
    location.href = subject ? SUB[subject].page : "/index.html";
  };

  /* ---------- màn chọn môn ---------- */
  function showPick() {
    game = null; setHeader();
    var st = Q() ? Q().state() : null;
    app.innerHTML = '<section class="card center"><h2 class="big">🎯 Chọn môn thử thách</h2><p class="muted">10 câu hỏi thực tế · trả lời càng nhanh càng nhiều điểm · hoàn thành để làm Nhiệm vụ hằng ngày</p><div class="subjects">' +
      Object.keys(SUB).map(function (k) {
        var c = { physics: "#38bdf8", chemistry: "#34d399", math: "#a78bfa" }[k];
        var played = st && st.prog["quick_" + k] ? "✅ Đã chơi hôm nay" : "📜 Nhiệm vụ: chưa hoàn thành";
        return '<button class="sub" data-s="' + k + '" style="--sc:' + c + '"><span class="ic">' + SUB[k].icon + "</span><b>" + SUB[k].name + "</b><small>" + SUB[k].desc + "</small><small>" + played + "</small></button>";
      }).join("") + "</div></section>";
    app.querySelectorAll("[data-s]").forEach(function (b) { b.onclick = function () { subject = b.getAttribute("data-s"); showIntro(); }; });
  }

  /* ---------- màn giới thiệu ---------- */
  function pool() {
    var r = RANGES.filter(function (x) { return x.id === range; })[0] || RANGES[0];
    return (BANK[subject] || []).filter(function (q) { return q.g >= r.min && q.g <= r.max; });
  }
  function showIntro() {
    game = null; setHeader();
    var st = Q() ? Q().state() : { prog: {}, qbest: {}, subj: {}, claimed: [] };
    var sd = st.subj[subject] || { plays: 0, best: 0 };
    var ms = Q() ? Q().MISSIONS.filter(function (m) { return m.key === "quick_" + subject || m.key === "correct" || m.key === "great"; }) : [];
    app.innerHTML = '<section class="card"><div class="center"><h2 class="big">' + SUB[subject].icon + " Thử thách nhanh " + SUB[subject].name + '</h2><p class="muted">Phản xạ nhanh với các câu hỏi gắn với đời sống thực tế</p></div>' +
      '<div class="rules"><div><b>' + QN + "</b>câu hỏi</div><div><b>" + secs() + "s</b>mỗi câu</div><div><b>+10</b>mỗi câu đúng<br>+5 nếu trả lời nhanh</div><div><b>⭐ " + (st.qbest[subject] || 0) + "/15</b>sao hôm nay</div></div>" +
      '<div class="lbl">Phạm vi kiến thức</div><div class="chips">' + RANGES.map(function (r) { return '<button class="chip' + (r.id === range ? " on" : "") + '" data-r="' + r.id + '">' + r.label + "</button>"; }).join("") + "</div>" +
      '<div class="lbl">Nhiệm vụ liên quan hôm nay</div><div class="minis">' + ms.map(function (m) {
        var v = Math.min(m.goal, st.prog[m.key] || 0), ok = v >= m.goal;
        return '<div class="mini' + (ok ? " ok" : "") + '">' + m.icon + " " + esc(m.title) + "<span>" + (ok ? "✓ Xong" : v + "/" + m.goal) + "</span></div>";
      }).join("") + "</div>" +
      '<p class="muted" style="font-size:13px;margin-top:14px">🏆 Kỷ lục của bạn: <b>' + sd.best + "/10</b> câu · Đã chơi " + sd.plays + " lượt. Đổi thời gian mỗi câu trong ⚙️ Cài đặt ở trang chủ.</p>" +
      '<div class="row"><button class="btn" id="startBtn">▶ Bắt đầu thử thách</button>' + (params.get("subject") ? "" : '<button class="btn ghost" id="otherBtn">Đổi môn</button>') + "</div></section>";
    app.querySelectorAll("[data-r]").forEach(function (b) { b.onclick = function () { range = b.getAttribute("data-r"); localStorage.setItem("hdlg_qc_range", range); showIntro(); }; });
    document.getElementById("startBtn").onclick = start;
    var ob = document.getElementById("otherBtn"); if (ob) ob.onclick = showPick;
  }

  /* ---------- chơi ---------- */
  function start() {
    var p = pool();
    if (p.length < 4) p = BANK[subject] || [];
    var qs = shuffle(p).slice(0, QN).map(function (q) {
      var opts = shuffle(q.a.map(function (t, i) { return { t: t, ok: i === 0 }; }));
      return { g: q.g, q: q.q, e: q.e, opts: opts };
    });
    game = { qs: qs, i: 0, score: 0, correct: 0, combo: 0, maxCombo: 0, log: [], over: false, limit: secs() };
    beep("tick"); showQuestion();
  }
  function stopTimer() { if (tick) { clearInterval(tick); tick = null; } }
  function showQuestion() {
    var g = game, q = g.qs[g.i];
    app.innerHTML = '<section class="card"><div class="hud"><span class="tag">Câu ' + (g.i + 1) + "/" + g.qs.length + '</span><span class="tag">⚡ ' + g.score + ' điểm</span><span class="tag combo' + (g.combo >= 2 ? " on" : "") + '">🔥 Combo x' + g.combo +
      '</span><span class="sp"></span><span class="tag" id="tleft">⏱ ' + g.limit + 's</span></div><div class="timer" id="tbar"><i id="tfill"></i></div>' +
      '<span class="qgrade">Lớp ' + q.g + '</span><p class="qtext">' + esc(q.q) + '</p><div class="opts">' +
      q.opts.map(function (o, i) { return '<button class="opt" data-i="' + i + '"><span class="k">' + "ABCD"[i] + "</span><span>" + esc(o.t) + "</span></button>"; }).join("") +
      '</div><div id="fbBox"></div></section>';
    app.querySelectorAll(".opt").forEach(function (b) { b.onclick = function () { answer(+b.getAttribute("data-i")); }; });
    var t0 = Date.now(), lim = g.limit * 1000;
    g.t0 = t0; g.answered = false;
    stopTimer();
    tick = setInterval(function () {
      var left = Math.max(0, lim - (Date.now() - t0));
      var f = document.getElementById("tfill"), l = document.getElementById("tleft"), b = document.getElementById("tbar");
      if (f) f.style.width = (100 * left / lim) + "%";
      if (l) l.textContent = "⏱ " + Math.ceil(left / 1000) + "s";
      if (b) b.classList.toggle("warn", left < lim * 0.3);
      if (left <= 0) answer(-1);
    }, 100);
  }
  function answer(idx) {
    var g = game; if (!g || g.answered) return;
    g.answered = true; stopTimer();
    var q = g.qs[g.i], used = (Date.now() - g.t0) / 1000, ok = idx >= 0 && q.opts[idx].ok, pts = 0;
    if (ok) {
      pts = 10 + Math.max(0, Math.round(5 * (1 - used / g.limit)));
      g.score += pts; g.correct++; g.combo++; g.maxCombo = Math.max(g.maxCombo, g.combo); beep("ok");
    } else { g.combo = 0; beep("bad"); }
    g.log.push({ q: q, pick: idx, ok: ok });
    app.querySelectorAll(".opt").forEach(function (b, i) {
      b.disabled = true;
      if (q.opts[i].ok) b.classList.add("right"); else if (i === idx) b.classList.add("wrong"); else b.classList.add("dim");
    });
    var last = g.i >= g.qs.length - 1;
    var right = q.opts.filter(function (o) { return o.ok; })[0].t;
    document.getElementById("fbBox").innerHTML = '<div class="fb ' + (ok ? "good" : "bad") + '"><p><b>' +
      (ok ? "✅ Chính xác! +" + pts + " điểm" + (g.combo >= 3 ? " · 🔥 Combo x" + g.combo : "") : idx < 0 ? "⏰ Hết giờ! Đáp án: " + esc(right) : "❌ Chưa đúng. Đáp án: " + esc(right)) +
      "</b>💡 " + esc(q.e) + '</p><button class="btn" id="nextBtn">' + (last ? "Xem kết quả" : "Câu tiếp →") + "</button></div>";
    var nb = document.getElementById("nextBtn"); nb.focus();
    nb.onclick = function () { if (last) finish(); else { g.i++; showQuestion(); } };
  }
  document.addEventListener("keydown", function (e) {
    if (!game || game.over) return;
    var map = { "1": 0, "2": 1, "3": 2, "4": 3, a: 0, b: 1, c: 2, d: 3 }, k = e.key.toLowerCase();
    if (!game.answered && k in map) { e.preventDefault(); answer(map[k]); }
  });

  /* ---------- kết thúc ---------- */
  function finish() {
    var g = game; g.over = true; stopTimer(); beep("end");
    var r = Q() ? Q().recordChallenge(subject, g.correct, g.qs.length, g.score) : { gain: 0, earned: Math.floor(g.score / 10), todayBest: 0, newlyDone: [], missions: [] };
    var pct = Math.round(100 * g.correct / g.qs.length);
    var title = pct === 100 ? "🏆 Hoàn hảo!" : pct >= 80 ? "🌟 Xuất sắc!" : pct >= 50 ? "👍 Khá lắm!" : "💪 Cố lên nhé!";
    var starMsg = r.gain > 0 ? "⭐ +" + r.gain + " sao đã cộng vào tài khoản" :
      "Lượt này đạt " + r.earned + " sao – chưa vượt kỷ lục hôm nay (" + r.todayBest + "/15) nên không cộng thêm";
    var rel = r.missions.filter(function (x) { return ["quick_" + subject, "correct", "great"].indexOf(x.m.key) >= 0; });
    app.innerHTML = '<section class="card center"><h2 class="big">' + title + '</h2><div class="ring" style="--p:' + pct + '"><b>' + g.correct + "/" + g.qs.length + "</b><small>câu đúng</small></div>" +
      '<div class="res"><div><b>' + g.score + "</b>Điểm</div><div><b>x" + g.maxCombo + "</b>Combo cao nhất</div><div><b>" + r.earned + "⭐</b>Sao lượt này</div></div>" +
      '<p class="muted">' + starMsg + "</p>" +
      (r.newlyDone.length ? '<div class="news">' + r.newlyDone.map(function (m) { return '<div class="mini ok">🎉 Hoàn thành nhiệm vụ: ' + esc(m.title) + "<span>Vào Nhiệm vụ để nhận ⭐" + m.reward + "</span></div>"; }).join("") + "</div>" : "") +
      '<div class="minis" style="margin-top:10px">' + rel.map(function (x) { return '<div class="mini' + (x.done ? " ok" : "") + '">' + x.m.icon + " " + esc(x.m.title) + "<span>" + (x.claimed ? "✓ Đã nhận" : x.done ? "Chờ nhận" : x.v + "/" + x.m.goal) + "</span></div>"; }).join("") + "</div>" +
      '<div class="row"><button class="btn" id="againBtn">🔄 Chơi lại</button><button class="btn ghost" id="mBtn" data-hq-badge="missions" style="position:relative">📜 Nhận thưởng nhiệm vụ</button><button class="btn ghost" id="homeBtn">🏠 Về trang ' + SUB[subject].name + "</button></div>" +
      '<div class="review"><div class="lbl">Xem lại đáp án</div>' + g.log.map(function (l, i) {
        var right = l.q.opts.filter(function (o) { return o.ok; })[0].t, mine = l.pick >= 0 ? l.q.opts[l.pick].t : "Hết giờ";
        return "<details><summary>" + (l.ok ? "✅" : "❌") + " Câu " + (i + 1) + ": " + esc(l.q.q) + "</summary><p>Bạn chọn: <b>" + esc(mine) + "</b> · Đáp án: <b>" + esc(right) + "</b><br>💡 " + esc(l.q.e) + "</p></details>";
      }).join("") + "</div></section>";
    document.getElementById("againBtn").onclick = start;
    document.getElementById("mBtn").onclick = function () { if (Q()) Q().openMissions(); };
    document.getElementById("homeBtn").onclick = function () { location.href = SUB[subject].page; };
    if (Q()) Q().refresh();
    updStars();
  }

  /* ---------- nền hạt ---------- */
  (function fx() {
    var c = document.getElementById("fx"), x = c.getContext("2d"), w, h, ps = [];
    function rs() { w = c.width = innerWidth; h = c.height = innerHeight; }
    rs(); addEventListener("resize", rs);
    for (var i = 0; i < 40; i++) ps.push({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 2 + 0.6, v: Math.random() * 0.4 + 0.1 });
    (function loop() {
      x.clearRect(0, 0, w, h);
      var col = getComputedStyle(document.body).getPropertyValue("--c") || "#38bdf8";
      ps.forEach(function (p) { p.y -= p.v; if (p.y < -5) { p.y = h + 5; p.x = Math.random() * w; } x.globalAlpha = 0.6; x.fillStyle = col; x.beginPath(); x.arc(p.x, p.y, p.r, 0, 6.29); x.fill(); });
      requestAnimationFrame(loop);
    })();
  })();

  /* ---------- khởi động ---------- */
  setHeader(); updStars();
  if (subject) showIntro(); else showPick();
  if (window.HDLG && HDLG.ready) HDLG.ready.then(function () { updStars(); if (!game) { if (subject) showIntro(); else showPick(); } });
})();
