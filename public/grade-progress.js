/* =========================================================================
   HỌC ĐỂ LÀM GÌ — BẢNG TIẾN TRÌNH HỌC TẬP CỦA TỪNG LỚP
   Dùng chung cho math-grade.html · physics-grade.html · chemistry-knowledge.html
   HDLGProgress.open({ subject, grade, lessons, apiBase })
   Dữ liệu lấy từ tài khoản (auth.js):
     - hdlg_best  : lesson_<id>_read / lesson_<id>_quiz  (sao học bài)
                    lab_*                                 (thí nghiệm ở Phòng Lab)
     - hdlg_completed : id bài đã vượt qua game “Thử thách thực tế”
     - hdlg_quests    : thống kê Thử thách nhanh theo môn
   ========================================================================= */
(function () {
  "use strict";
  if (window.HDLGProgress) return;

  var SUBJ = {
    math:      { name: "Toán học", short: "Toán",    icon: "📐", color: "#a78bfa", page: "math-grade.html",          lab: null },
    physics:   { name: "Vật lý",   short: "Vật lý",  icon: "⚡", color: "#38bdf8", page: "physics-grade.html",       lab: { name: "Phòng Lab Vật lý", url: "physics-lab.html", test: function (k) { return k.indexOf("chem_") !== 0; }, total: 0 } },
    chemistry: { name: "Hóa học",  short: "Hóa học", icon: "🧪", color: "#34d399", page: "chemistry-knowledge.html", lab: { name: "Phòng Lab Hóa học", url: "phong_labhoahoc.html", test: function (k) { return k.indexOf("chem_") === 0 && k.indexOf("chem_found_") !== 0; }, total: 46 } }
  };

  function jparse(s, d) { try { var v = JSON.parse(s); return v == null ? d : v; } catch (e) { return d; } }
  function ls(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function pct(a, b) { return b ? Math.round(100 * a / b) : 0; }
  function num(v) { v = parseInt(v, 10); return isFinite(v) && v > 0 ? v : 0; }

  /* ---------- đọc dữ liệu ---------- */
  function completedSet() {
    var d = jparse(ls("hdlg_completed"), []), set = {};
    if (Array.isArray(d)) d.forEach(function (x) { set[String(x)] = 1; });
    else if (d && typeof d === "object") Object.keys(d).forEach(function (k) { if (d[k]) set[k] = 1; });
    return set;
  }
  function lessonState(l, done) {
    var st = window.HDLG && HDLG.lessonStatus ? HDLG.lessonStatus(l.id) : { read: false, quiz: false, stars: 0 };
    var hasGame = !!(l.game_type || l.game_title);
    var game = hasGame && !!done[String(l.id)];
    var parts = 2 + (hasGame ? 1 : 0), got = (st.read ? 1 : 0) + (st.quiz ? 1 : 0) + (game ? 1 : 0);
    return { l: l, read: !!st.read, quiz: !!st.quiz, stars: st.stars || 0, hasGame: hasGame, game: game, score: got / parts, got: got, parts: parts };
  }
  function analyse(lessons) {
    var done = completedSet(), rows = lessons.map(function (l) { return lessonState(l, done); });
    var topics = [], map = {};
    rows.forEach(function (r) {
      var key = r.l.topic || "khac";
      if (!map[key]) { map[key] = { slug: key, name: r.l.title, icon: r.l.icon || "📚", rows: [] }; topics.push(map[key]); }
      map[key].rows.push(r);
    });
    topics.forEach(function (t) {
      var s = 0; t.rows.forEach(function (r) { s += r.score; });
      t.mastery = t.rows.length ? Math.round(100 * s / t.rows.length) : 0;
    });
    var tot = { n: rows.length, read: 0, quiz: 0, games: 0, gameDone: 0, stars: 0, got: 0, parts: 0 };
    rows.forEach(function (r) {
      if (r.read) tot.read++; if (r.quiz) tot.quiz++; if (r.hasGame) tot.games++; if (r.game) tot.gameDone++;
      tot.stars += r.stars; tot.got += r.got; tot.parts += r.parts;
    });
    tot.mastery = pct(tot.got, tot.parts);
    tot.maxStars = rows.length * ((window.HDLG && HDLG.LESSON_STARS) || 10);
    return { rows: rows, topics: topics, tot: tot };
  }
  function labStats(subject) {
    var info = SUBJ[subject].lab; if (!info) return null;
    var best = jparse(ls("hdlg_best"), {}) || {}, local = jparse(ls("hdlg_lab_done"), {}) || {}, seen = {}, stars = 0;
    Object.keys(best).forEach(function (k) { if (k.indexOf("lab_") === 0) { var id = k.slice(4); if (info.test(id)) { seen[id] = 1; stars += num(best[k]); } } });
    Object.keys(local).forEach(function (id) { if (info.test(id) && !seen[id]) { seen[id] = 1; stars += num(local[id]); } });
    var found = 0;
    if (subject === "chemistry") { var f = jparse(ls("chemlab_found"), null); found = Array.isArray(f) ? f.length : (f && typeof f === "object" ? Object.keys(f).length : 0); }
    return { name: info.name, url: info.url, done: Object.keys(seen).length, total: info.total, stars: stars, found: found };
  }
  function quickStats(subject) {
    var s = window.HDLGQ && HDLGQ.state ? HDLGQ.state() : jparse(ls("hdlg_quests"), {}) || {};
    var d = (s.subj && s.subj[subject]) || {};
    return { plays: num(d.plays), best: num(d.best), correct: num(d.correct), answered: num(d.answered), today: num(s.qbest && s.qbest[subject]) };
  }

  /* ---------- đường dẫn ---------- */
  function lessonURL(subject, grade, l, hash) {
    return "lesson.html?id=" + encodeURIComponent(l.id) + "&subject=" + subject + "&grade=" + encodeURIComponent(l.grade || grade) + "&topic=" + encodeURIComponent(l.topic || "") + (hash || "");
  }
  var GAME_FILES = { function_challenge: "function-challenge" };   // game_type khác tên file
  function gameURL(l) { var t = l.game_type || "simulation"; return "games/" + encodeURIComponent(GAME_FILES[t] || t) + ".html?lesson_id=" + encodeURIComponent(l.id); }
  function challengeURL(subject, grade) {
    return "/challenge.html?subject=" + subject + "&grade=" + encodeURIComponent(grade) + "&from=" + encodeURIComponent(location.pathname + location.search);
  }
  function nextStep(subject, grade, a) {
    var r, i;
    for (i = 0; i < a.rows.length; i++) { r = a.rows[i]; if (!r.read) return { icon: "📖", title: "Học bài tiếp theo", text: r.l.title, btn: "Vào học", url: lessonURL(subject, grade, r.l) }; }
    for (i = 0; i < a.rows.length; i++) { r = a.rows[i]; if (!r.quiz) return { icon: "🧠", title: "Ôn lại Kiểm tra nhanh", text: r.l.title, btn: "Ôn tập", url: lessonURL(subject, grade, r.l, "#questionSection") }; }
    for (i = 0; i < a.rows.length; i++) { r = a.rows[i]; if (r.hasGame && !r.game) return { icon: "🎮", title: "Vượt qua Thử thách thực tế", text: r.l.title, btn: "Chơi ngay", url: gameURL(r.l) }; }
    return { icon: "🏆", title: "Bạn đã hoàn thành toàn bộ lớp " + grade + "!", text: "Giữ phong độ bằng Thử thách nhanh của lớp này.", btn: "Thử thách", url: challengeURL(subject, grade) };
  }
  function rank(m) {
    if (m >= 100) return { t: "Bậc thầy", c: "#ffd65d" };
    if (m >= 75) return { t: "Thành thạo", c: "#4ade80" };
    if (m >= 40) return { t: "Đang tiến bộ", c: "#38bdf8" };
    if (m > 0) return { t: "Khởi đầu", c: "#a9bde6" };
    return { t: "Chưa bắt đầu", c: "#7c8db5" };
  }

  /* ---------- giao diện ---------- */
  var CSS = "\
.gp-ov{position:fixed;inset:0;z-index:99990;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(4,10,26,.74);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);font-family:'Segoe UI',Roboto,Arial,sans-serif;animation:gpF .2s ease}\
@keyframes gpF{from{opacity:0}to{opacity:1}}\
@keyframes gpU{from{transform:translateY(18px);opacity:0}to{transform:none;opacity:1}}\
.gp-box{--c:#38bdf8;width:100%;max-width:760px;max-height:92vh;display:flex;flex-direction:column;background:linear-gradient(165deg,#15305c,#0b1834 70%);color:#eaf2ff;border:1px solid color-mix(in srgb,var(--c) 55%,#2b4a86);border-radius:20px;box-shadow:0 24px 70px rgba(0,0,0,.55);overflow:hidden;animation:gpU .25s ease}\
.gp-head{display:flex;align-items:center;gap:12px;padding:16px 18px 12px;border-bottom:1px solid #ffffff14}\
.gp-head .ic{width:44px;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:24px;background:color-mix(in srgb,var(--c) 22%,transparent);border:1px solid color-mix(in srgb,var(--c) 50%,transparent);flex:none}\
.gp-head h2{margin:0;font-size:19px;letter-spacing:.2px}\
.gp-head p{margin:2px 0 0;color:#a9bde6;font-size:13px}\
.gp-x{margin-left:auto;background:#ffffff10;border:1px solid #ffffff22;color:#cfe0ff;width:36px;height:36px;border-radius:50%;font-size:20px;cursor:pointer;flex:none}\
.gp-x:hover{background:#ffffff22}\
.gp-tabs{display:flex;gap:6px;padding:10px 18px 0;overflow-x:auto;scrollbar-width:none}\
.gp-tabs button{flex:none;padding:8px 14px;border-radius:999px;border:1px solid #ffffff22;background:#ffffff0c;color:#cfe0ff;font-weight:700;font-size:13px;cursor:pointer}\
.gp-tabs button.on{background:var(--c);border-color:var(--c);color:#06142e}\
.gp-body{flex:1;padding:14px 18px 18px;overflow:auto;-webkit-overflow-scrolling:touch}\
.gp-hero{display:flex;gap:16px;align-items:center;flex-wrap:wrap}\
.gp-ring{position:relative;width:120px;height:120px;flex:none}\
.gp-ring svg{width:100%;height:100%;transform:rotate(-90deg)}\
.gp-ring .v{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}\
.gp-ring b{font-size:28px;line-height:1}\
.gp-ring small{font-size:11px;color:#a9bde6;margin-top:3px}\
.gp-rank{display:inline-block;margin-top:4px;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;background:#ffffff14}\
.gp-tiles{flex:1;min-width:240px;display:grid;grid-template-columns:repeat(2,1fr);gap:8px}\
.gp-tile{background:#ffffff0e;border:1px solid #ffffff14;border-radius:14px;padding:9px 11px}\
.gp-tile span{font-size:12px;color:#a9bde6;display:block}\
.gp-tile b{font-size:19px}\
.gp-tile em{font-style:normal;font-size:12px;color:#8aa0cc;margin-left:3px}\
.gp-bar{height:7px;border-radius:99px;background:#ffffff14;overflow:hidden;margin-top:6px}\
.gp-bar i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--c),#ffd65d);transition:width .6s}\
.gp-next{display:flex;align-items:center;gap:12px;margin:14px 0 4px;padding:12px 14px;border-radius:16px;background:linear-gradient(90deg,color-mix(in srgb,var(--c) 26%,transparent),#ffffff08);border:1px solid color-mix(in srgb,var(--c) 45%,transparent)}\
.gp-next .ni{font-size:26px;flex:none}\
.gp-next div{flex:1;min-width:0}\
.gp-next strong{display:block;font-size:14px}\
.gp-next small{display:block;color:#cfe0ff;font-size:12.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}\
.gp-btn{flex:none;padding:9px 14px;border-radius:12px;border:0;background:#ffd65d;color:#1b1b1b;font-weight:800;font-size:13px;cursor:pointer;text-decoration:none;white-space:nowrap}\
.gp-btn.g{background:#ffffff14;color:#eaf2ff;border:1px solid #ffffff26}\
.gp-h{margin:16px 0 8px;font-size:13px;font-weight:800;letter-spacing:.6px;color:#a9bde6;text-transform:uppercase}\
.gp-topic{border:1px solid #ffffff14;background:#ffffff08;border-radius:14px;margin-bottom:8px;overflow:hidden}\
.gp-topic>summary{list-style:none;display:flex;align-items:center;gap:10px;padding:10px 12px;cursor:pointer}\
.gp-topic>summary::-webkit-details-marker{display:none}\
.gp-topic .ti{font-size:20px;flex:none;width:26px;text-align:center}\
.gp-topic .tn{flex:1;min-width:0}\
.gp-topic .tn b{display:block;font-size:14px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}\
.gp-topic .tp{font-weight:800;font-size:14px;flex:none}\
.gp-topic .ch{flex:none;color:#8aa0cc;transition:transform .2s}\
.gp-topic[open] .ch{transform:rotate(90deg)}\
.gp-les{display:flex;align-items:center;gap:8px;padding:9px 12px;border-top:1px dashed #ffffff14;flex-wrap:wrap}\
.gp-les .lt{flex:1 1 200px;min-width:0;font-size:13px;color:#dbe7ff}\
.gp-chips{display:flex;gap:5px;flex:none}\
.gp-chip{font-size:11.5px;padding:3px 8px;border-radius:99px;background:#ffffff0d;border:1px solid #ffffff1a;color:#8aa0cc;white-space:nowrap}\
.gp-chip.ok{background:#22c55e26;border-color:#4ade8077;color:#bbf7d0}\
.gp-acts{display:flex;gap:5px;flex:none}\
.gp-acts a{font-size:12px;padding:5px 10px;border-radius:9px;background:#ffffff12;border:1px solid #ffffff22;color:#eaf2ff;text-decoration:none;font-weight:700}\
.gp-acts a:hover{background:#ffffff22}\
.gp-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px}\
.gp-card{background:#ffffff0c;border:1px solid #ffffff17;border-radius:16px;padding:12px 14px}\
.gp-card h4{margin:0 0 8px;font-size:14px}\
.gp-kv{display:grid;grid-template-columns:repeat(2,1fr);gap:6px;margin-bottom:8px}\
.gp-kv div{background:#ffffff0b;border-radius:10px;padding:6px 8px;font-size:11.5px;color:#a9bde6}\
.gp-kv b{display:block;font-size:16px;color:#ffd65d}\
.gp-grades{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}\
.gp-grade{display:block;text-decoration:none;color:#eaf2ff;background:#ffffff0c;border:1px solid #ffffff17;border-radius:14px;padding:10px 12px}\
.gp-grade.cur{border-color:var(--c);background:color-mix(in srgb,var(--c) 18%,transparent)}\
.gp-grade b{font-size:15px}\
.gp-grade small{display:block;color:#a9bde6;font-size:12px;margin-top:2px}\
.gp-note{color:#8aa0cc;font-size:12px;margin:12px 0 0;line-height:1.5}\
.gp-empty{text-align:center;padding:26px 10px;color:#a9bde6}\
.gp-foot{display:flex;gap:8px;flex-wrap:wrap;padding:12px 18px;border-top:1px solid #ffffff14;background:#0000001f}\
.gp-foot .gp-btn{flex:1 1 150px;text-align:center;padding:11px 12px}\
@media (max-width:600px){\
.gp-ov{padding:0;align-items:flex-end}\
.gp-box{max-height:94vh;min-height:72vh;border-radius:20px 20px 0 0;border-bottom:0}\
.gp-ring{width:100px;height:100px}.gp-ring b{font-size:24px}\
.gp-hero{justify-content:center}.gp-tiles{min-width:100%}\
.gp-les .lt{flex-basis:100%}\
.gp-foot{padding-bottom:max(12px,env(safe-area-inset-bottom))}\
}";

  var ov = null, opts = null, tab = "overview", allLessons = null, allLoading = false;
  function onKey(e) { if (e.key === "Escape") close(); }
  function close() {
    if (!ov) return; ov.remove(); ov = null;
    document.removeEventListener("keydown", onKey);
    document.body.style.overflow = "";
  }
  function ring(m, color) {
    var r = 52, c = 2 * Math.PI * r, off = c * (1 - m / 100);
    return '<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="' + r + '" fill="none" stroke="#ffffff17" stroke-width="11"/>' +
      '<circle cx="60" cy="60" r="' + r + '" fill="none" stroke="' + color + '" stroke-width="11" stroke-linecap="round" stroke-dasharray="' + c.toFixed(1) + '" stroke-dashoffset="' + off.toFixed(1) + '"/></svg>';
  }
  function bar(v) { return '<div class="gp-bar"><i style="width:' + Math.max(0, Math.min(100, v)) + '%"></i></div>'; }
  function tile(label, a, b, extra) { return '<div class="gp-tile"><span>' + label + "</span><b>" + a + "</b><em>/ " + b + (extra || "") + "</em>" + bar(pct(a, b)) + "</div>"; }

  function viewOverview(a) {
    var S = SUBJ[opts.subject], t = a.tot, rk = rank(t.mastery), nx = nextStep(opts.subject, opts.grade, a);
    var h = '<div class="gp-hero"><div class="gp-ring">' + ring(t.mastery, S.color) + '<div class="v"><b>' + t.mastery + '%</b><small>Mức thành thạo</small><span class="gp-rank" style="color:' + rk.c + '">' + rk.t + "</span></div></div>" +
      '<div class="gp-tiles">' +
      tile("📖 Bài đã học xong", t.read, t.n) +
      tile("🧠 Kiểm tra nhanh đúng", t.quiz, t.n) +
      tile("🎮 Thử thách thực tế (game)", t.gameDone, t.games || 0) +
      tile("⭐ Sao từ bài học", t.stars, t.maxStars) +
      "</div></div>";
    h += '<div class="gp-next"><span class="ni">' + nx.icon + "</span><div><strong>" + esc(nx.title) + "</strong><small>" + esc(nx.text) + '</small></div><a class="gp-btn" href="' + esc(nx.url) + '">' + nx.btn + " →</a></div>";

    // chủ đề mạnh / cần cố gắng
    var started = a.topics.filter(function (x) { return x.mastery > 0; }).slice().sort(function (x, y) { return y.mastery - x.mastery; });
    var weak = a.topics.filter(function (x) { return x.mastery < 100; }).slice().sort(function (x, y) { return x.mastery - y.mastery; });
    h += '<div class="gp-h">Theo chủ đề</div>';
    a.topics.forEach(function (tp) {
      h += '<div class="gp-topic" style="padding:9px 12px;display:flex;align-items:center;gap:10px"><span class="ti">' + esc(tp.icon) + '</span><div class="tn" style="flex:1;min-width:0"><b style="font-size:13.5px;display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + esc(tp.name) + "</b>" + bar(tp.mastery) + '</div><span class="tp" style="color:' + rank(tp.mastery).c + '">' + tp.mastery + "%</span></div>";
    });
    if (started.length || weak.length) {
      h += '<div class="gp-cards" style="margin-top:10px">';
      if (started.length) h += '<div class="gp-card"><h4>💪 Mạnh nhất</h4><div style="font-size:13px;color:#dbe7ff">' + esc(started[0].name) + " · <b>" + started[0].mastery + "%</b></div></div>";
      if (weak.length) h += '<div class="gp-card"><h4>🎯 Nên ôn thêm</h4><div style="font-size:13px;color:#dbe7ff">' + esc(weak[0].name) + " · <b>" + weak[0].mastery + "%</b></div></div>";
      h += "</div>";
    }
    h += "<p class='gp-note'>Mức thành thạo mỗi bài gồm 3 phần: 📖 đọc hết bài · 🧠 trả lời đúng Kiểm tra nhanh ngay lần đầu · 🎮 vượt qua game Thử thách thực tế (đạt từ 50% điểm). Tiến trình được lưu vào tài khoản và đồng bộ trên mọi thiết bị khi đăng nhập.</p>";
    return h;
  }

  function viewLessons(a) {
    var h = "";
    a.topics.forEach(function (tp, i) {
      h += '<details class="gp-topic"' + (tp.mastery < 100 && h.indexOf(" open") < 0 ? " open" : "") + '><summary><span class="ti">' + esc(tp.icon) + '</span><div class="tn"><b>' + esc(tp.name) + "</b>" + bar(tp.mastery) + '</div><span class="tp" style="color:' + rank(tp.mastery).c + '">' + tp.mastery + '%</span><span class="ch">›</span></summary>';
      tp.rows.forEach(function (r) {
        h += '<div class="gp-les"><div class="lt">' + esc(r.l.title) + '</div><div class="gp-chips">' +
          '<span class="gp-chip' + (r.read ? " ok" : "") + '" title="Đọc hết bài">📖 ' + (r.read ? "Đã học" : "Chưa học") + "</span>" +
          '<span class="gp-chip' + (r.quiz ? " ok" : "") + '" title="Đúng Kiểm tra nhanh ngay lần đầu">🧠 ' + (r.quiz ? "Đúng" : "Chưa") + "</span>" +
          (r.hasGame ? '<span class="gp-chip' + (r.game ? " ok" : "") + '" title="Vượt qua game Thử thách thực tế">🎮 ' + (r.game ? "Qua" : "Chưa") + "</span>" : "") +
          '<span class="gp-chip" title="Sao đã nhận">⭐ ' + r.stars + "</span>" +
          '</div><div class="gp-acts"><a href="' + esc(lessonURL(opts.subject, opts.grade, r.l)) + '">' + (r.read ? "Ôn bài" : "Học") + "</a>" +
          (r.hasGame ? '<a href="' + esc(gameURL(r.l)) + '">Game</a>' : "") + "</div></div>";
      });
      h += "</details>";
    });
    return h || '<div class="gp-empty">Chưa có bài học.</div>';
  }

  function viewPractice() {
    var S = SUBJ[opts.subject], q = quickStats(opts.subject), lab = labStats(opts.subject), acc = q.answered ? pct(q.correct, q.answered) : 0;
    var h = '<div class="gp-cards">';
    h += '<div class="gp-card"><h4>🎯 Thử thách nhanh ' + S.short + '</h4><div class="gp-kv"><div><b>' + q.plays + "</b>Lượt chơi</div><div><b>" + q.best + "/10</b>Kỷ lục</div><div><b>" + (q.answered ? acc + "%" : "—") + "</b>Độ chính xác</div><div><b>" + q.today + "/15</b>Sao hôm nay</div></div>" +
      bar(acc) + '<div style="margin-top:10px"><a class="gp-btn" style="display:block;text-align:center" href="' + esc(challengeURL(opts.subject, opts.grade)) + '">Thử thách lớp ' + esc(opts.grade) + " →</a></div></div>";
    if (lab) {
      h += '<div class="gp-card"><h4>🔬 ' + esc(lab.name) + '</h4><div class="gp-kv"><div><b>' + lab.done + (lab.total ? "/" + lab.total : "") + "</b>" + (opts.subject === "chemistry" ? "Bài thí nghiệm" : "Nhiệm vụ") + "</div><div><b>" + lab.stars + "</b>Sao từ Lab</div>" +
        (opts.subject === "chemistry" ? "<div><b>" + lab.found + "</b>Phản ứng đã khám phá</div>" : "") + "</div>" +
        (lab.total ? bar(pct(lab.done, lab.total)) : "") + '<div style="margin-top:10px"><a class="gp-btn g" style="display:block;text-align:center" href="' + esc(lab.url) + '">Vào ' + esc(lab.name) + " →</a></div></div>";
    }
    var x = window.HDLG && HDLG.getStars ? HDLG.getStars() : num(ls("hdlg_xp"));
    h += '<div class="gp-card"><h4>👤 Tài khoản</h4><div class="gp-kv"><div><b>Lv.' + (Math.floor(x / 100) + 1) + "</b>Cấp độ</div><div><b>" + x + "</b>Tổng sao</div></div>" + bar(x % 100) +
      '<div style="font-size:12px;color:#a9bde6;margin-top:6px">Còn ' + (100 - x % 100) + " sao để lên cấp tiếp theo</div></div>";
    h += "</div>";
    return h;
  }

  function viewGrades() {
    var S = SUBJ[opts.subject];
    if (!allLessons) {
      if (!allLoading) loadAll();
      return '<div class="gp-empty">⏳ Đang tải dữ liệu các lớp…</div>';
    }
    if (!allLessons.length) return '<div class="gp-empty">Không tải được dữ liệu các lớp. Kiểm tra kết nối mạng rồi thử lại.</div>';
    var by = {};
    allLessons.forEach(function (l) { var g = String(l.grade); (by[g] = by[g] || []).push(l); });
    var gs = Object.keys(by).sort(function (x, y) { return x - y; }), sumGot = 0, sumParts = 0;
    var h = '<div class="gp-grades">';
    gs.forEach(function (g) {
      var a = analyse(by[g]); sumGot += a.tot.got; sumParts += a.tot.parts;
      h += '<a class="gp-grade' + (String(g) === String(opts.grade) ? " cur" : "") + '" href="' + S.page + "?grade=" + encodeURIComponent(g) + '"><b>' + S.icon + " Lớp " + esc(g) + "</b><small>" + a.tot.read + "/" + a.tot.n + " bài · " + a.tot.mastery + "%</small>" + bar(a.tot.mastery) + "</a>";
    });
    h += "</div><p class='gp-note'>Toàn môn " + S.name + ": thành thạo <b>" + pct(sumGot, sumParts) + "%</b> · chạm vào một lớp để chuyển sang lớp đó.</p>";
    return h;
  }
  function loadAll() {
    allLoading = true;
    var key = "hdlg_lessons_" + opts.subject + "_all";
    try { var c = jparse(sessionStorage.getItem(key), null); if (Array.isArray(c) && c.length) { allLessons = c; allLoading = false; return; } } catch (e) {}
    fetch((opts.apiBase || "/api") + "/content/subjects/" + opts.subject + "/lessons")
      .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
      .then(function (d) { allLessons = Array.isArray(d) ? d : []; try { sessionStorage.setItem(key, JSON.stringify(allLessons.map(function (l) { return { id: l.id, grade: l.grade, topic: l.topic, title: l.title, icon: l.icon, game_type: l.game_type, game_title: l.game_title }; }))); } catch (e) {} })
      .catch(function () { allLessons = []; })
      .then(function () { allLoading = false; if (ov && tab === "grades") render(); });
  }

  /* xuất báo cáo CSV (mở được bằng Excel) */
  function exportCSV(a) {
    var S = SUBJ[opts.subject], rows = [["Môn", "Lớp", "Chủ đề", "Bài học", "Đã học", "Kiểm tra nhanh", "Game thực tế", "Sao", "Thành thạo (%)"]];
    a.rows.forEach(function (r) {
      rows.push([S.name, opts.grade, r.l.topic || "", r.l.title, r.read ? "Có" : "Chưa", r.quiz ? "Đúng" : "Chưa", r.hasGame ? (r.game ? "Qua" : "Chưa") : "Không có", r.stars, Math.round(100 * r.score)]);
    });
    rows.push([]); rows.push(["Tổng", opts.grade, "", a.tot.n + " bài", a.tot.read, a.tot.quiz, a.tot.gameDone + "/" + a.tot.games, a.tot.stars, a.tot.mastery]);
    var csv = "\ufeff" + rows.map(function (r) { return r.map(function (v) { v = String(v == null ? "" : v); return /[",\n;]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }).join(","); }).join("\r\n");
    var blob = new Blob([csv], { type: "text/csv;charset=utf-8" }), u = URL.createObjectURL(blob), el = document.createElement("a");
    el.href = u; el.download = "tien-trinh-" + opts.subject + "-lop-" + opts.grade + ".csv"; document.body.appendChild(el); el.click();
    setTimeout(function () { URL.revokeObjectURL(u); el.remove(); }, 500);
    if (window.HDLG && HDLG.toast) HDLG.toast("📄 Đã tải báo cáo tiến trình (CSV)");
  }

  function render() {
    if (!ov) return;
    var S = SUBJ[opts.subject], lessons = opts.getLessons ? opts.getLessons() : opts.lessons || [], a = analyse(lessons);
    var body;
    if (!lessons.length && tab !== "grades") body = '<div class="gp-empty">⏳ Dữ liệu bài học của lớp ' + esc(opts.grade) + " đang được tải hoặc chưa có. Hãy thử lại sau giây lát.</div>";
    else body = tab === "lessons" ? viewLessons(a) : tab === "practice" ? viewPractice() : tab === "grades" ? viewGrades() : viewOverview(a);
    var u = window.HDLG ? HDLG.user : null, user = u ? { name: u.displayName || (u.email ? u.email.split("@")[0] : "") } : null;
    var tabs = [["overview", "Tổng quan"], ["lessons", "Từng bài"], ["practice", "Luyện tập"], ["grades", "Các lớp"]];
    ov.innerHTML = '<div class="gp-box" role="dialog" aria-modal="true" aria-label="Tiến trình học tập" style="--c:' + S.color + '">' +
      '<div class="gp-head"><span class="ic">📊</span><div><h2>Tiến trình học tập</h2><p>' + S.icon + " " + S.name + " · Lớp " + esc(opts.grade) + (user && user.name ? " · " + esc(user.name) : "") + "</p></div>" +
      '<button class="gp-x" type="button" aria-label="Đóng">×</button></div>' +
      '<div class="gp-tabs">' + tabs.map(function (t) { return '<button type="button" data-tab="' + t[0] + '" class="' + (tab === t[0] ? "on" : "") + '">' + t[1] + "</button>"; }).join("") + "</div>" +
      '<div class="gp-body">' + body + "</div>" +
      '<div class="gp-foot"><a class="gp-btn" href="' + esc(challengeURL(opts.subject, opts.grade)) + '">🎯 Thử thách lớp ' + esc(opts.grade) + '</a><button class="gp-btn g" type="button" data-act="csv">📄 Xuất báo cáo</button>' +
      (window.HDLG && HDLG.showAccount ? '<button class="gp-btn g" type="button" data-act="acc">👤 Tài khoản</button>' : "") + "</div></div>";
    ov.querySelector(".gp-x").onclick = close;
    ov.querySelectorAll("[data-tab]").forEach(function (b) { b.onclick = function () { tab = b.getAttribute("data-tab"); render(); }; });
    var csv = ov.querySelector('[data-act="csv"]'); if (csv) csv.onclick = function () { if (a.rows.length) exportCSV(a); };
    var acc = ov.querySelector('[data-act="acc"]'); if (acc) acc.onclick = function () { close(); HDLG.showAccount(); };
  }

  function open(o) {
    opts = o || {}; if (!SUBJ[opts.subject]) opts.subject = "physics";
    opts.grade = String(opts.grade || "");
    if (!document.getElementById("gpCss")) { var st = document.createElement("style"); st.id = "gpCss"; st.textContent = CSS; document.head.appendChild(st); }
    close(); tab = "overview";
    ov = document.createElement("div"); ov.className = "gp-ov";
    ov.addEventListener("mousedown", function (e) { if (e.target === ov) close(); });
    document.body.appendChild(ov); document.body.style.overflow = "hidden";
    document.addEventListener("keydown", onKey);
    render();
  }
  function refresh() { if (ov) render(); }
  window.addEventListener("hdlg:update", refresh);
  window.addEventListener("hdlg:lesson", refresh);

  window.HDLGProgress = { open: open, close: close, refresh: refresh, analyse: analyse, challengeURL: challengeURL };
})();
