/* =========================================================================
   TRỢ LÝ TRI — phân tích tiến độ học & gợi ý cá nhân (chạy hoàn toàn trên máy người dùng)
   Dữ liệu dùng: sao/kỷ lục (hdlg_best), nhiệm vụ & nhật ký học (hdlg_quests: lv = bài đã mở,
   qw = câu Kiểm tra nhanh trả lời sai, days = ngày có học, subj = Thử thách nhanh), danh mục bài học.
   Không gửi dữ liệu đi đâu. API: HDLGAssistant.open(tab) | close() | analyze() → Promise<report>
   ========================================================================= */
(function () {
  "use strict";
  if (window.HDLGAssistant) return;

  var SUBJ = {
    physics:   { name: "Vật lý",  icon: "⚡", page: "/physics.html",   color: "#38bdf8" },
    chemistry: { name: "Hóa học", icon: "🧪", page: "/chemistry.html", color: "#34d399" },
    math:      { name: "Toán học", icon: "📐", page: "/math.html",     color: "#a78bfa" }
  };
  var ORDER = ["physics", "chemistry", "math"];
  var GAME_FILES = { function_challenge: "function-challenge", "store-management": "store_management" };
  var CHECKIN = [2, 3, 4, 5, 6, 8, 15];

  function H() { return window.HDLG || null; }
  function jparse(s, d) { try { var v = JSON.parse(s); return v == null ? d : v; } catch (e) { return d; } }
  function num(v) { v = parseInt(v, 10); return isFinite(v) && v > 0 ? v : 0; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function dayStr(d) { return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }
  function daysAgo(n) { var d = new Date(); d.setDate(d.getDate() - n); return dayStr(d); }
  function ddmm(s) { var p = String(s || "").split("-"); return p.length === 3 ? p[2] + "/" + p[1] : ""; }
  function pct(a, b) { return b > 0 ? Math.round(a * 100 / b) : null; }

  /* ---------- danh mục bài học ---------- */
  var catalogP = null;
  function loadCatalog() {
    if (catalogP) return catalogP;
    try { var c = jparse(sessionStorage.getItem("hdlg_catalog"), null); if (Array.isArray(c) && c.length) return (catalogP = Promise.resolve(c)); } catch (e) {}
    var base = window.HOC_API_BASE || ((["127.0.0.1", "localhost"].indexOf(location.hostname) >= 0 && location.port !== "8000") ? "http://127.0.0.1:8000/api" : "/api");
    function get(u) { return fetch(u).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (d) { if (!Array.isArray(d) || !d.length) throw new Error("empty"); return d; }); }
    catalogP = get(base + "/content/catalog").catch(function () { return get("/lesson-catalog.json"); })
      .then(function (d) { try { sessionStorage.setItem("hdlg_catalog", JSON.stringify(d)); } catch (e) {} return d; })
      .catch(function () { catalogP = null; return []; });
    return catalogP;
  }

  function lessonUrl(l) {
    return "/lesson.html?id=" + encodeURIComponent(l.id) + "&subject=" + encodeURIComponent(l.subject) + "&grade=" + encodeURIComponent(l.grade || "") + "&topic=" + encodeURIComponent(l.topic || "");
  }
  function gameUrl(l) {
    if (!l.game_type) return lessonUrl(l);
    return "/games/" + encodeURIComponent(GAME_FILES[l.game_type] || l.game_type) + ".html?lesson_id=" + encodeURIComponent(l.id);
  }

  /* ---------- PHÂN TÍCH ---------- */
  function analyze() {
    return loadCatalog().then(function (cat) {
      var best = jparse(localStorage.getItem("hdlg_best"), {}) || {};
      var q = (H() && H().questGet) ? H().questGet() : (jparse(localStorage.getItem("hdlg_quests"), {}) || {});
      q.checkin = q.checkin || {}; q.total = q.total || {}; q.subj = q.subj || {}; q.prog = q.prog || {}; q.claimed = q.claimed || [];
      var lv = q.lv || {}, qw = q.qw || {}, days = Array.isArray(q.days) ? q.days : [];
      var xp = H() ? H().getStars() : num(localStorage.getItem("hdlg_xp"));
      var byId = {}; cat.forEach(function (l) { byId[String(l.id)] = l; });

      /* game: g_<game>_<lesson>_<đề>_<s1|clear|rec|total> */
      var games = {};
      Object.keys(best).forEach(function (k) {
        var m = /^g_(.+?)_(\d+)_([A-Z])_(s(\d+)|clear|rec|total)$/.exec(k);
        if (!m || m[2] === "0") return;
        var g = games[m[2]] || (games[m[2]] = { stages: [], clear: false, total: null });
        var v = num(best[k]);
        if (m[5]) g.stages.push({ set: m[3], n: num(m[5]), pct: Math.min(100, v * 5) });
        else if (m[4] === "clear") g.clear = true;
        else if (m[4] === "total") g.total = Math.min(100, Math.round(v * 100 / 30));
      });
      Object.keys(games).forEach(function (id) {
        var g = games[id], arr = g.stages.map(function (s) { return s.pct; });
        if (g.total != null) arr.push(g.total);
        g.avg = arr.length ? Math.round(arr.reduce(function (a, b) { return a + b; }, 0) / arr.length) : null;
        g.weak = g.stages.slice().sort(function (a, b) { return a.pct - b.pct; })[0] || null;
      });

      function st(l) {
        var id = String(l.id);
        return {
          read: num(best["lesson_" + id + "_read"]) > 0,
          quiz: num(best["lesson_" + id + "_quiz"]) > 0,
          wrong: !!qw[id] && !(num(best["lesson_" + id + "_quiz"]) > 0),
          opened: lv[id] || "",
          game: games[id] || null
        };
      }

      var subj = {}, review = [], unfinished = [], noGame = [], weakGames = [], next = [];
      ORDER.forEach(function (k) { subj[k] = { key: k, total: 0, read: 0, quizOk: 0, quizWrong: 0, gamesPlayed: 0, gameSum: 0, lastOpen: "", grades: {}, recentGrade: null }; });

      cat.forEach(function (l) {
        var S = subj[l.subject]; if (!S) return;
        var s = st(l); l._st = s;
        S.total++;
        if (s.read) S.read++;
        if (s.quiz) S.quizOk++;
        if (s.wrong) { S.quizWrong++; review.push({ l: l, when: qw[String(l.id)] }); }
        if (s.game && s.game.avg != null) {
          S.gamesPlayed++; S.gameSum += s.game.avg;
          if (s.game.avg < 60) weakGames.push({ l: l, g: s.game });
        }
        if (s.opened && !s.read) unfinished.push({ l: l, when: s.opened });
        if (s.read && l.has_game && !s.game) noGame.push({ l: l });
        if (s.read || s.opened) {
          var g = l.grade || 0; S.grades[g] = (S.grades[g] || 0) + 1;
          if (s.opened && s.opened > S.lastOpen) { S.lastOpen = s.opened; S.recentGrade = g; }
        }
      });
      review.sort(function (a, b) { return a.when < b.when ? 1 : -1; });
      unfinished.sort(function (a, b) { return a.when < b.when ? 1 : -1; });
      weakGames.sort(function (a, b) { return a.g.avg - b.g.avg; });

      /* Học tiếp: theo lớp đang học của từng môn */
      ORDER.forEach(function (k) {
        var S = subj[k], grade = S.recentGrade;
        if (grade == null) {
          var gs = Object.keys(S.grades); if (!gs.length) return;
          grade = Number(gs.sort(function (a, b) { return S.grades[b] - S.grades[a]; })[0]);
        }
        S.grade = grade;
        var list = cat.filter(function (l) { return l.subject === k && (l.grade || 0) === grade; });
        S.gradeTotal = list.length; S.gradeRead = list.filter(function (l) { return l._st.read; }).length;
        var nx = list.filter(function (l) { return !l._st.read && !l._st.opened; })[0];
        if (!nx) {   // học hết lớp này → gợi ý lớp kế tiếp
          var up = cat.filter(function (l) { return l.subject === k && (l.grade || 0) > grade && !l._st.read; })
                      .sort(function (a, b) { return (a.grade - b.grade) || (a.id - b.id); })[0];
          if (up) next.push({ l: up, why: "Bạn đã học hết " + SUBJ[k].name + " lớp " + grade + " 🎉 — sang lớp " + up.grade + " nhé!" });
        } else next.push({ l: nx, why: "Bài tiếp theo của " + SUBJ[k].name + " lớp " + grade + " (" + S.gradeRead + "/" + S.gradeTotal + " bài đã học)" });
      });

      /* Thử thách nhanh */
      ORDER.forEach(function (k) {
        var c = q.subj[k] || {}, S = subj[k];
        S.quickPlays = num(c.plays); S.quickAcc = pct(num(c.correct), num(c.answered));
        S.quizRate = pct(S.quizOk, S.quizOk + S.quizWrong);
        S.gameAvg = S.gamesPlayed ? Math.round(S.gameSum / S.gamesPlayed) : null;
        var parts = [S.quizRate, S.gameAvg, S.quickAcc].filter(function (v) { return v != null; });
        S.score = parts.length ? Math.round(parts.reduce(function (a, b) { return a + b; }, 0) / parts.length) : null;
        S.active = S.read > 0 || S.gamesPlayed > 0 || S.quickPlays > 0 || !!S.lastOpen;
      });

      /* Chỉ số chung */
      var last7 = days.filter(function (d) { return d >= daysAgo(6); }).length;
      var tot = { read: 0, quizOk: 0, quizWrong: 0, gamesPlayed: 0, gameSum: 0 };
      ORDER.forEach(function (k) { var S = subj[k]; tot.read += S.read; tot.quizOk += S.quizOk; tot.quizWrong += S.quizWrong; tot.gamesPlayed += S.gamesPlayed; tot.gameSum += S.gameSum; });
      var metrics = {
        diligence: Math.round(last7 * 100 / 7),
        understand: pct(tot.quizOk, tot.quizOk + tot.quizWrong),
        practice: tot.gamesPlayed ? Math.round(tot.gameSum / tot.gamesPlayed) : null,
        reflex: pct(num(q.total.correct), num(q.total.answered))
      };

      /* Điểm danh & nhiệm vụ hôm nay */
      var t = dayStr(new Date()), c = q.checkin, ciDone = c.last === t;
      var streak = ciDone ? num(c.streak) : (c.last === daysAgo(1) ? num(c.streak) : 0);
      var ciIdx = ciDone ? ((streak - 1) % 7) : (streak % 7);
      var M = (window.HDLGQ && HDLGQ.MISSIONS) || [];
      var mLeft = M.filter(function (m) { return (q.prog[m.key] || 0) < m.goal; });
      var mClaim = M.filter(function (m) { return (q.prog[m.key] || 0) >= m.goal && q.claimed.indexOf(m.id) < 0; });

      /* Mạnh / yếu */
      var scored = ORDER.map(function (k) { return subj[k]; }).filter(function (S) { return S.score != null; });
      scored.sort(function (a, b) { return b.score - a.score; });
      var strong = scored.length ? scored[0] : null, weak = scored.length > 1 ? scored[scored.length - 1] : null;
      if (strong && weak && strong.score - weak.score < 8) weak = null;

      var rep = {
        name: H() && H().user ? (H().user.displayName || (H().user.email || "").split("@")[0] || "") : "",
        xp: xp, level: Math.floor(xp / 100) + 1, toNext: 100 - (xp % 100),
        subj: subj, metrics: metrics, last7: last7, activeDays: days.length, streak: streak, ciDone: ciDone, ciReward: CHECKIN[ciIdx] || 2,
        missionsLeft: mLeft, missionsClaim: mClaim, review: review, unfinished: unfinished, noGame: noGame, weakGames: weakGames, next: next,
        strong: strong, weak: weak, totals: tot, catalogOk: cat.length > 0,
        quickTotal: num(q.total.quick), lessonsTotal: cat.length
      };
      rep.todo = buildTodo(rep);
      rep.tips = buildTips(rep);
      return rep;
    });
  }

  /* ---------- việc nên làm (ưu tiên) ---------- */
  function item(o) { return o; }
  function buildTodo(r) {
    var out = [];
    if (!r.ciDone) out.push(item({ ic: "📅", t: "Điểm danh hôm nay", why: r.streak ? "Giữ chuỗi " + r.streak + " ngày 🔥 — nhận ⭐ " + r.ciReward : "Nhận ⭐ " + r.ciReward + " và bắt đầu chuỗi mới", act: "Điểm danh", fn: "rewards", kind: "daily" }));
    r.review.slice(0, 3).forEach(function (x) { out.push(item({ ic: "🔁", t: "Xem lại: " + x.l.title, why: "Câu Kiểm tra nhanh lần đầu chưa đúng (" + ddmm(x.when) + ") — đọc lại phần công thức & ví dụ rồi thử lại", act: "Ôn lại", href: lessonUrl(x.l), kind: "review", s: x.l.subject })); });
    r.weakGames.slice(0, 2).forEach(function (x) { out.push(item({ ic: "🎮", t: "Chơi lại game: " + x.l.title, why: "Điểm trung bình mới " + x.g.avg + "/100" + (x.g.weak ? " · yếu nhất chặng " + x.g.weak.n + " (" + x.g.weak.pct + ")" : ""), act: "Chơi lại", href: gameUrl(x.l), kind: "review", s: x.l.subject })); });
    r.unfinished.slice(0, 3).forEach(function (x) { out.push(item({ ic: "⏳", t: "Học nốt: " + x.l.title, why: "Mở bài ngày " + ddmm(x.when) + " nhưng chưa đọc hết", act: "Học tiếp", href: lessonUrl(x.l), kind: "unfinished", s: x.l.subject })); });
    r.noGame.slice(0, 2).forEach(function (x) { out.push(item({ ic: "🚀", t: "Trải nghiệm game: " + x.l.title, why: "Đã đọc xong bài nhưng chưa chơi — game giúp nhớ lâu hơn", act: "Chơi ngay", href: gameUrl(x.l), kind: "game", s: x.l.subject })); });
    r.next.forEach(function (x) { out.push(item({ ic: "➡️", t: "Học tiếp: " + x.l.title, why: x.why, act: "Bắt đầu", href: lessonUrl(x.l), kind: "next", s: x.l.subject })); });
    ORDER.forEach(function (k) {
      var S = r.subj[k];
      if (S.quickAcc != null && S.quickPlays >= 1 && S.quickAcc < 60) out.push(item({ ic: "⚡", t: "Luyện Thử thách nhanh " + SUBJ[k].name, why: "Tỉ lệ đúng mới " + S.quickAcc + "% — luyện thêm để tăng phản xạ", act: "Luyện", href: "/challenge.html?subject=" + k, kind: "quick", s: k }));
    });
    if (r.missionsClaim.length) out.push(item({ ic: "🎁", t: "Nhận thưởng " + r.missionsClaim.length + " nhiệm vụ đã xong", why: "Bạn đã hoàn thành nhưng chưa bấm nhận sao", act: "Nhận", fn: "missions", kind: "daily" }));
    else if (r.missionsLeft.length) out.push(item({ ic: "📜", t: "Còn " + r.missionsLeft.length + " nhiệm vụ hôm nay", why: r.missionsLeft.slice(0, 2).map(function (m) { return m.title; }).join(" · "), act: "Xem", fn: "missions", kind: "daily" }));
    if (!r.next.length && !r.totals.read && !r.unfinished.length) {
      ORDER.forEach(function (k) { out.push(item({ ic: SUBJ[k].icon, t: "Bắt đầu học " + SUBJ[k].name, why: "Chọn lớp của bạn rồi mở bài đầu tiên", act: "Vào học", href: SUBJ[k].page, kind: "next", s: k })); });
    }
    return out;
  }
  /* Gợi ý nổi bật hôm nay: tối đa 3 việc, ưu tiên đa dạng */
  function topToday(r) {
    var pick = [], kinds = {};
    var pref = ["daily", "review", "unfinished", "next", "game", "quick"];
    pref.forEach(function (k) { var x = r.todo.filter(function (i) { return i.kind === k; })[0]; if (x && pick.length < 3 && !kinds[k]) { pick.push(x); kinds[k] = 1; } });
    return pick;
  }

  /* ---------- lời khuyên ---------- */
  function buildTips(r) {
    var tips = [], m = r.metrics, T = r.totals, hr = new Date().getHours();
    var active = ORDER.filter(function (k) { return r.subj[k].active; });
    if (!T.read && !T.gamesPlayed && !r.quickTotal) {
      tips.push("Mới bắt đầu thì cứ <b>1 bài mỗi ngày</b>: đọc bài → làm Kiểm tra nhanh → chơi game. Đều đặn quan trọng hơn học nhiều một lúc.");
      tips.push("Chưa biết bắt đầu từ đâu? Bấm <b>🧭 Xem hướng dẫn</b> bên dưới, mình dẫn bạn đi một vòng.");
      return tips;
    }
    if (r.last7 <= 2) tips.push("Tuần này bạn mới học <b>" + r.last7 + "/7 ngày</b>. Học đều 15–20 phút mỗi ngày giúp nhớ lâu hơn hẳn so với học dồn một buổi.");
    else if (r.last7 >= 5) tips.push("Bạn học <b>" + r.last7 + "/7 ngày</b> tuần này — rất chăm! Giữ nhịp này nhé 💪");
    if (m.understand != null && T.quizOk + T.quizWrong >= 3 && m.understand < 60)
      tips.push("Kiểm tra nhanh mới đúng <b>" + m.understand + "%</b> ngay lần đầu. Trước khi chọn đáp án, đọc lại phần <b>Công thức</b> và <b>Ví dụ minh họa</b>, tự giải thử ra nháp.");
    else if (m.understand != null && T.quizOk >= 3 && m.understand >= 85)
      tips.push("Bạn trả lời Kiểm tra nhanh đúng <b>" + m.understand + "%</b> — hiểu bài rất chắc. Thử <b>Thử thách nhanh</b> để luyện phản xạ thêm nhé!");
    if (T.read >= 2 && T.gamesPlayed < T.read / 2)
      tips.push("Bạn đọc " + T.read + " bài nhưng mới chơi " + T.gamesPlayed + " game. Phần <b>Trải nghiệm thực tế</b> giúp vận dụng kiến thức vào tình huống thật — và còn được nhiều ⭐ hơn!");
    if (m.practice != null && m.practice < 60)
      tips.push("Điểm game trung bình " + m.practice + "/100. Đọc kỹ đề mỗi chặng, mở <b>📔 Sổ tay</b> trong game để xem lại công thức trước khi làm.");
    if (T.gamesPlayed >= 2 && T.read < T.gamesPlayed)
      tips.push("Bạn hay vào thẳng game — đọc bài trước 5 phút sẽ giúp đạt điểm cao hơn ở các chặng khó.");
    if (r.weak) tips.push("Môn <b>" + SUBJ[r.weak.key].name + "</b> đang yếu hơn các môn khác (" + r.weak.score + "/100). Ưu tiên ôn môn này 2–3 buổi trong tuần.");
    if (active.length === 1) {
      var other = ORDER.filter(function (k) { return k !== active[0]; })[0];
      tips.push("Bạn đang tập trung vào " + SUBJ[active[0]].name + ". Thử thêm <b>" + SUBJ[other].name + "</b> — nhiều kiến thức liên quan nhau đấy!");
    }
    if (!r.quickTotal) tips.push("Bạn chưa thử <b>Thử thách nhanh</b> — 10 câu, mỗi câu 15 giây, rất hợp để ôn bài trong 3 phút.");
    if (r.toNext <= 25) tips.push("Chỉ còn <b>" + r.toNext + " ⭐</b> nữa là lên <b>Lv." + (r.level + 1) + "</b>!");
    if (hr >= 23 || hr < 5) tips.push("Khuya rồi 🌙 Ngủ đủ giấc giúp não ghi nhớ bài vừa học tốt hơn — mai học tiếp nhé!");
    return tips.slice(0, 5);
  }

  /* ---------- GIAO DIỆN ---------- */
  var CSS =
".ta-ov{position:fixed;inset:0;z-index:99995;display:flex;align-items:center;justify-content:center;padding:14px;background:rgba(3,10,26,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);font-family:'Segoe UI',Roboto,Arial,sans-serif;animation:taFade .2s ease-out}" +
"@keyframes taFade{from{opacity:0}to{opacity:1}}@keyframes taUp{from{transform:translateY(14px);opacity:.4}to{transform:none;opacity:1}}" +
".ta-box{position:relative;width:100%;max-width:600px;height:680px;max-height:90vh;max-height:calc(100dvh - 28px);display:flex;flex-direction:column;background:linear-gradient(165deg,#13305c,#0a1630 70%);color:#eaf2ff;border:1.5px solid rgba(125,211,252,.55);border-radius:22px;box-shadow:0 24px 70px rgba(0,0,0,.6),0 0 30px rgba(56,189,248,.15);animation:taUp .25s ease-out;overflow:hidden}" +
".ta-hd{display:flex;align-items:center;gap:12px;padding:16px 18px 10px}" +
".ta-av{width:52px;height:52px;flex:none;border-radius:16px;background:radial-gradient(circle at 50% 40%,#1e4b8f,#0b1a3a);border:1.5px solid rgba(125,211,252,.6);display:flex;align-items:center;justify-content:center}" +
".ta-av svg{width:44px;height:44px}" +
".ta-hd h2{margin:0;font-size:19px;color:#fde68a}.ta-hd p{margin:2px 0 0;font-size:13px;color:#a9c2ea;line-height:1.4}" +
".ta-x{position:absolute;top:10px;right:12px;width:34px;height:34px;border-radius:50%;border:0;background:rgba(255,255,255,.08);color:#cfe0ff;font-size:22px;line-height:1;cursor:pointer}.ta-x:hover{background:rgba(255,255,255,.16)}" +
".ta-tabs{display:flex;gap:6px;padding:0 18px 10px;border-bottom:1px solid rgba(125,211,252,.15)}" +
".ta-tabs button{flex:1;white-space:nowrap;border:1px solid rgba(125,211,252,.25);background:rgba(255,255,255,.04);color:#cfe0ff;border-radius:12px;padding:8px 6px;font-weight:700;font-size:13px;font-family:inherit;cursor:pointer;position:relative}" +
".ta-tabs button.on{background:linear-gradient(135deg,#0ea5e9,#2563eb);border-color:transparent;color:#fff}" +
".ta-tabs b{display:inline-block;min-width:18px;height:18px;line-height:18px;border-radius:9px;background:#f43f5e;color:#fff;font-size:11px;margin-left:4px;padding:0 4px}" +
".ta-bd{overflow:auto;padding:14px 18px 6px;-webkit-overflow-scrolling:touch;overscroll-behavior:contain}" +
".ta-sec{margin:0 0 16px}.ta-sec h3{margin:0 0 8px;font-size:14px;color:#7dd3fc;letter-spacing:.3px}" +
".ta-met{display:grid;grid-template-columns:1fr 1fr;gap:8px}" +
".ta-m{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:10px 12px}" +
".ta-m small{display:block;color:#a9c2ea;font-size:12px}.ta-m b{font-size:20px}.ta-m i{font-style:normal;font-size:12px;color:#8fb0de;margin-left:4px}" +
".ta-bar{height:7px;border-radius:4px;background:rgba(255,255,255,.1);margin-top:6px;overflow:hidden}.ta-bar span{display:block;height:100%;border-radius:4px}" +
".ta-it{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:14px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);margin-bottom:8px}" +
".ta-it .ic{width:36px;height:36px;flex:none;border-radius:11px;background:rgba(56,189,248,.14);display:flex;align-items:center;justify-content:center;font-size:18px}" +
".ta-it .mid{flex:1;min-width:0}.ta-it .mid b{display:block;font-size:14px;line-height:1.3}.ta-it .mid small{display:block;color:#a9c2ea;font-size:12px;line-height:1.35;margin-top:2px}" +
".ta-go{flex:none;border:0;border-radius:11px;padding:8px 12px;background:linear-gradient(135deg,#fde047,#f59e0b);color:#3b2300;font-weight:800;font-size:12.5px;font-family:inherit;cursor:pointer;text-decoration:none;white-space:nowrap}" +
".ta-go:hover{filter:brightness(1.08)}" +
".ta-tip{display:flex;gap:8px;padding:9px 12px;border-radius:12px;background:rgba(253,224,71,.07);border:1px solid rgba(253,224,71,.18);margin-bottom:7px;font-size:13.5px;line-height:1.45;color:#e7efff}" +
".ta-tip b{color:#fde68a}" +
".ta-sw{display:grid;grid-template-columns:1fr 1fr;gap:8px}.ta-sw div{border-radius:14px;padding:10px 12px;font-size:13px;line-height:1.4}" +
".ta-sw .s{background:rgba(52,211,153,.1);border:1px solid rgba(52,211,153,.3)}.ta-sw .w{background:rgba(251,113,133,.1);border:1px solid rgba(251,113,133,.3)}" +
".ta-sb{border-radius:16px;padding:12px 14px;margin-bottom:10px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09)}" +
".ta-sb h4{margin:0 0 6px;font-size:15px;display:flex;align-items:center;gap:8px}.ta-sb h4 em{margin-left:auto;font-style:normal;font-size:12px;color:#a9c2ea;font-weight:600}" +
".ta-row{display:flex;justify-content:space-between;font-size:12.5px;color:#c9d9f5;margin-top:6px}" +
".ta-empty{color:#a9c2ea;font-size:13px;padding:6px 2px}" +
".ta-ft{display:flex;gap:8px;padding:10px 18px 14px;border-top:1px solid rgba(125,211,252,.15)}" +
".ta-ft button{flex:1;border-radius:12px;padding:10px;font-weight:700;font-size:13.5px;font-family:inherit;cursor:pointer;border:1px solid rgba(125,211,252,.35);background:rgba(255,255,255,.05);color:#e6f0ff}" +
".ta-ft button.y{background:linear-gradient(135deg,#0ea5e9,#2563eb);border-color:transparent;color:#fff}" +
".ta-load{padding:40px 10px;text-align:center;color:#a9c2ea}" +
"@media (max-width:600px){.ta-ov{padding:0;align-items:flex-end}.ta-box{max-width:none;height:auto;border-radius:20px 20px 0 0;max-height:92vh;max-height:calc(100dvh - 10px)}.ta-hd{padding:14px 14px 8px}.ta-tabs,.ta-ft{padding-left:14px;padding-right:14px}.ta-bd{padding:12px 14px 4px}.ta-met{gap:6px}.ta-m b{font-size:18px}.ta-sw{grid-template-columns:1fr}.ta-go{padding:8px 10px}.ta-tabs{gap:5px}.ta-tabs button{font-size:12px;padding:8px 3px}.ta-tabs b{min-width:16px;height:16px;line-height:16px;font-size:10px;margin-left:3px}}";

  var BOT_SVG = '<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="12" y="16" width="40" height="30" rx="13" fill="#e8f3ff" stroke="#38bdf8" stroke-width="2.5"/><rect x="18" y="22" width="28" height="17" rx="8" fill="#0b2a55"/><circle cx="26" cy="30.5" r="3.4" fill="#67e8f9"/><circle cx="38" cy="30.5" r="3.4" fill="#67e8f9"/><path d="M27 35.5q5 3 10 0" stroke="#67e8f9" stroke-width="2" fill="none" stroke-linecap="round"/><line x1="32" y1="16" x2="32" y2="9" stroke="#38bdf8" stroke-width="2.5"/><circle cx="32" cy="7.5" r="3.2" fill="#fde047"/><rect x="20" y="46" width="24" height="10" rx="5" fill="#e8f3ff" stroke="#38bdf8" stroke-width="2"/></svg>';

  var ov = null, curTab = "overview", lastRep = null;
  function close() { if (ov) { ov.remove(); ov = null; document.removeEventListener("keydown", onKey); } }
  function onKey(e) { if (e.key === "Escape") close(); }
  function color(v) { return v == null ? "#64748b" : v >= 75 ? "#34d399" : v >= 50 ? "#fbbf24" : "#fb7185"; }
  function metric(label, v, note) {
    return '<div class="ta-m"><small>' + label + "</small><b>" + (v == null ? "—" : v + "%") + "</b>" + (note ? "<i>" + note + "</i>" : "") +
      '<div class="ta-bar"><span style="width:' + (v || 0) + "%;background:" + color(v) + '"></span></div></div>';
  }
  function itemHtml(x) {
    var btn = x.href ? '<a class="ta-go" href="' + esc(x.href) + '">' + esc(x.act) + " →</a>"
                     : '<button class="ta-go" data-fn="' + esc(x.fn) + '">' + esc(x.act) + "</button>";
    return '<div class="ta-it"><div class="ic">' + x.ic + '</div><div class="mid"><b>' + esc(x.t) + "</b><small>" + esc(x.why) + "</small></div>" + btn + "</div>";
  }
  function greet(r) {
    var h = new Date().getHours(), g = h < 11 ? "Chào buổi sáng" : h < 14 ? "Chào buổi trưa" : h < 18 ? "Chào buổi chiều" : "Chào buổi tối";
    return g + (r.name ? ", " + esc(r.name) : "") + "! 👋";
  }
  function summaryLine(r) {
    var T = r.totals;
    if (!T.read && !T.gamesPlayed && !r.quickTotal) return "Mình chưa có nhiều dữ liệu về bạn. Học vài bài là mình phân tích được ngay!";
    return "Lv." + r.level + " · " + r.xp + " ⭐ · đã học " + T.read + "/" + r.lessonsTotal + " bài · " + T.gamesPlayed + " game · học " + r.last7 + "/7 ngày gần đây" + (r.streak ? " · chuỗi " + r.streak + "🔥" : "");
  }

  function renderOverview(r) {
    var m = r.metrics, h = "";
    h += '<div class="ta-sec"><h3>📊 CHỈ SỐ HỌC TẬP</h3><div class="ta-met">' +
      metric("📅 Chuyên cần (7 ngày)", m.diligence, r.last7 + "/7 ngày") +
      metric("🧠 Hiểu bài (Kiểm tra nhanh)", m.understand, r.totals.quizOk + r.totals.quizWrong ? r.totals.quizOk + "/" + (r.totals.quizOk + r.totals.quizWrong) + " đúng" : "chưa có") +
      metric("🎮 Vận dụng (điểm game)", m.practice, r.totals.gamesPlayed ? r.totals.gamesPlayed + " game" : "chưa chơi") +
      metric("⚡ Phản xạ (Thử thách nhanh)", m.reflex, r.quickTotal ? r.quickTotal + " lượt" : "chưa thử") + "</div></div>";
    var top = topToday(r);
    h += '<div class="ta-sec"><h3>📌 TRI GỢI Ý HÔM NAY</h3>' + (top.length ? top.map(itemHtml).join("") : '<div class="ta-empty">Bạn đã làm hết việc cần làm hôm nay 🎉</div>') + "</div>";
    if (r.strong || r.weak) {
      h += '<div class="ta-sec"><h3>⚖️ ĐIỂM MẠNH & CẦN CẢI THIỆN</h3><div class="ta-sw">';
      h += r.strong ? '<div class="s">💪 <b>Mạnh nhất: ' + SUBJ[r.strong.key].name + "</b><br>" + r.strong.score + "/100 điểm tổng hợp</div>" : "";
      h += r.weak ? '<div class="w">⚠️ <b>Cần cải thiện: ' + SUBJ[r.weak.key].name + "</b><br>" + r.weak.score + "/100 — ưu tiên ôn môn này</div>"
                  : '<div class="s">✨ Các môn khá đều nhau — tiếp tục giữ phong độ!</div>';
      h += "</div></div>";
    }
    h += '<div class="ta-sec"><h3>💡 LỜI KHUYÊN CỦA TRI</h3>' + r.tips.map(function (t) { return '<div class="ta-tip"><span>💬</span><span>' + t + "</span></div>"; }).join("") + "</div>";
    return h;
  }
  function list(title, arr, empty) {
    return '<div class="ta-sec"><h3>' + title + "</h3>" + (arr.length ? arr.map(itemHtml).join("") : '<div class="ta-empty">' + empty + "</div>") + "</div>";
  }
  function renderTodo(r) {
    var by = function (k) { return r.todo.filter(function (x) { return x.kind === k; }); };
    return list("📅 HÔM NAY", by("daily"), "Đã điểm danh và xong nhiệm vụ hôm nay ✅") +
      list("🔁 NÊN XEM LẠI", by("review"), "Chưa có bài nào cần ôn lại — tốt lắm!") +
      list("⏳ ĐANG HỌC DỞ", by("unfinished"), "Không có bài nào bỏ dở.") +
      list("🚀 CHƯA TRẢI NGHIỆM GAME", by("game"), "Bài nào đọc xong bạn cũng đã chơi game rồi 👍") +
      list("➡️ NÊN HỌC TIẾP", by("next"), "Mở một môn và chọn lớp để mình gợi ý bài tiếp theo.") +
      (by("quick").length ? list("⚡ LUYỆN PHẢN XẠ", by("quick"), "") : "");
  }
  function renderSubjects(r) {
    return '<div class="ta-sec"><h3>📚 TIẾN ĐỘ THEO MÔN</h3>' + ORDER.map(function (k) {
      var S = r.subj[k], P = SUBJ[k], prog = pct(S.read, S.total) || 0;
      return '<div class="ta-sb"><h4>' + P.icon + " " + P.name + (S.score != null ? "<em>Tổng hợp " + S.score + "/100</em>" : "<em>chưa có dữ liệu</em>") + "</h4>" +
        '<div class="ta-row"><span>Đã học ' + S.read + "/" + S.total + " bài" + (S.grade != null ? " · Lớp " + S.grade + ": " + S.gradeRead + "/" + S.gradeTotal : "") + "</span><span>" + prog + "%</span></div>" +
        '<div class="ta-bar"><span style="width:' + prog + "%;background:" + P.color + '"></span></div>' +
        '<div class="ta-row"><span>🧠 Kiểm tra nhanh</span><span>' + (S.quizRate == null ? "—" : S.quizRate + "% đúng (" + S.quizOk + "/" + (S.quizOk + S.quizWrong) + ")") + "</span></div>" +
        '<div class="ta-row"><span>🎮 Game</span><span>' + (S.gameAvg == null ? "—" : S.gamesPlayed + " game · TB " + S.gameAvg + "/100") + "</span></div>" +
        '<div class="ta-row"><span>⚡ Thử thách nhanh</span><span>' + (S.quickAcc == null ? "—" : S.quickPlays + " lượt · " + S.quickAcc + "% đúng") + "</span></div>" +
        "</div>";
    }).join("") + "</div>";
  }

  function render() {
    if (!ov) return;
    var r = lastRep, bd = ov.querySelector(".ta-bd");
    ov.querySelector(".ta-hd p").innerHTML = r ? summaryLine(r) : "Đang xem lại quá trình học của bạn…";
    ov.querySelector(".ta-hd h2").innerHTML = r ? greet(r) : "Trợ lý Tri";
    ov.querySelectorAll(".ta-tabs button").forEach(function (b) {
      b.classList.toggle("on", b.getAttribute("data-tab") === curTab);
      if (b.getAttribute("data-tab") === "todo" && r) {
        var n = r.todo.filter(function (x) { return x.kind === "review" || x.kind === "unfinished"; }).length;
        b.innerHTML = "📌 Việc nên làm" + (n ? "<b>" + n + "</b>" : "");
      }
    });
    if (!r) { bd.innerHTML = '<div class="ta-load">⏳ Tri đang phân tích dữ liệu học tập…</div>'; return; }
    bd.innerHTML = curTab === "todo" ? renderTodo(r) : curTab === "subjects" ? renderSubjects(r) : renderOverview(r);
    bd.scrollTop = 0;
    bd.querySelectorAll("[data-fn]").forEach(function (b) {
      b.onclick = function () {
        var fn = b.getAttribute("data-fn"); close();
        if (window.HDLGQ) { if (fn === "rewards") HDLGQ.openRewards("daily"); else if (fn === "missions") HDLGQ.openMissions(); }
      };
    });
  }

  function open(tab) {
    curTab = tab || "overview";
    if (!ov) {
      var st = document.getElementById("taCss");
      if (!st) { st = document.createElement("style"); st.id = "taCss"; st.textContent = CSS; document.head.appendChild(st); }
      ov = document.createElement("div");
      ov.className = "ta-ov"; ov.setAttribute("role", "dialog"); ov.setAttribute("aria-label", "Trợ lý Tri");
      ov.innerHTML = '<div class="ta-box"><button class="ta-x" aria-label="Đóng">×</button>' +
        '<div class="ta-hd"><div class="ta-av">' + BOT_SVG + "</div><div><h2>Trợ lý Tri</h2><p></p></div></div>" +
        '<div class="ta-tabs"><button data-tab="overview">📊 Tổng quan</button><button data-tab="todo">📌 Việc nên làm</button><button data-tab="subjects">📚 Theo môn</button></div>' +
        '<div class="ta-bd"></div>' +
        '<div class="ta-ft"><button data-act="tour">🧭 Xem hướng dẫn</button><button class="y" data-act="close">Đã hiểu!</button></div></div>';
      document.body.appendChild(ov);
      ov.addEventListener("click", function (e) { if (e.target === ov) close(); });
      ov.querySelector(".ta-x").onclick = close;
      ov.querySelector('[data-act="close"]').onclick = close;
      ov.querySelector('[data-act="tour"]').onclick = function () { close(); if (window.HDLGTour) HDLGTour.start(); };
      ov.querySelectorAll(".ta-tabs button").forEach(function (b) { b.onclick = function () { curTab = b.getAttribute("data-tab"); render(); }; });
      document.addEventListener("keydown", onKey);
    }
    lastRep = null; render();
    var go = function () { analyze().then(function (r) { lastRep = r; render(); }); };
    if (H() && H().ready && typeof H().ready.then === "function") H().ready.then(go, go); else go();
  }

  window.HDLGAssistant = {
    open: open, close: close, analyze: analyze,
    /* số gợi ý quan trọng (ôn lại + học dở + điểm danh) — dùng cho bong bóng nhắc trên trang chủ */
    count: function (r) { return r ? r.review.length + r.unfinished.length + (r.ciDone ? 0 : 1) + r.weakGames.length : 0; },
    topToday: topToday
  };
})();
