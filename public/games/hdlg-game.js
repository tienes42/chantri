/* =========================================================================
   HỌC ĐỂ LÀM GÌ — hdlg-game.js  (CẦU NỐI SAO / KỶ LỤC / NHIỆM VỤ CHO MỌI GAME)
   Nhúng ngay sau mobile-fit.js, đúng thứ tự:
     <script src="/firebase-config.js"></script>
     <script src="/auth.js"></script>
     <script src="/games/hdlg-game.js"></script>
   Game KHÔNG tự cộng sao bằng setXP(getXP() + n) nữa mà gọi:
     HDLGGame.stage(i, score)      // thắng chặng i (0,1,2…), score 0–100 → tối đa 20 ⭐, chỉ cộng phần vượt kỷ lục
     HDLGGame.bonus(20)            // thưởng hoàn thành đề: chỉ 1 lần cho mỗi đề (mỗi bài)
     HDLGGame.finish(total, max)   // khi mở bảng Tổng kết: đánh dấu đã qua bài + tính nhiệm vụ "Nhà thực nghiệm" + lưu kỷ lục điểm
     HDLGGame.result(score, max, maxStars)  // game đơn giản 1 màn: = cộng sao theo kỷ lục + finish()
   Trừ sao khi mua gợi ý vẫn dùng setXP(getXP() - 20) như cũ (auth.js tự đồng bộ).
   Tự đọc GAME_KEY, LESSON_ID (ưu tiên ?lesson_id= trên URL), SETS/SETX nếu game có khai báo.
   Chạy được cả khi auth.js lỗi mạng (ghi thẳng localStorage + cờ hdlg_dirty để lần sau đồng bộ).
   ========================================================================= */
(function () {
  "use strict";
  if (window.HDLGGame) return;

  var STAGE_MAX = 20;                  // sao tối đa / chặng (score/5)
  var cfg = {};

  function jparse(s, d) { try { var v = JSON.parse(s); return v == null ? d : v; } catch (e) { return d; } }
  function num(v) { v = parseInt(v, 10); return isFinite(v) && v > 0 ? v : 0; }
  function clean(s) { return String(s).replace(/[^A-Za-z0-9_\-]/g, "_"); }
  function G(name) {                   // đọc biến toàn cục của game (kể cả const/let) nếu có
    try { return Function("return typeof " + name + " !== 'undefined' ? " + name + " : undefined")(); } catch (e) { return undefined; }
  }

  function gameKey() {
    return cfg.game || G("GAME_KEY") || location.pathname.split("/").pop().replace(/\.html?$/, "") || "game";
  }
  function lessonId() {
    var q = null; try { q = new URLSearchParams(location.search).get("lesson_id"); } catch (e) {}
    var v = cfg.lesson != null ? cfg.lesson : (q || G("LESSON_ID"));
    return v == null || v === "" ? "" : String(v);
  }
  function setCode() {
    if (cfg.set != null) return String(cfg.set);
    var sets = G("SETS"), x = G("SETX");
    return sets && sets.length && typeof x === "number" ? String.fromCharCode(65 + x) : "A";
  }
  function base() { return clean("g_" + gameKey() + "_" + (lessonId() || "0") + "_" + setCode()); }

  /* ---------- dự phòng khi chưa có auth.js ---------- */
  function localAward(key, stars, opts) {
    opts = opts || {};
    var best = jparse(localStorage.getItem("hdlg_best"), {}) || {}, prev = num(best[key]), gain = Math.max(0, stars - prev);
    if (gain > 0) {
      best[key] = stars; localStorage.setItem("hdlg_best", JSON.stringify(best));
      if (!opts.noStars) localStorage.setItem("hdlg_xp", String(num(localStorage.getItem("hdlg_xp")) + gain));
      localStorage.setItem("hdlg_dirty", "1");
    }
    return { gained: opts.noStars ? 0 : gain, improved: gain > 0, prev: prev, best: Math.max(prev, stars) };
  }
  function award(key, stars, opts) {
    key = clean(key); stars = Math.max(0, Math.round(Number(stars) || 0));
    var H = window.HDLG, r;
    try { r = H && H.award ? H.award(key, stars, opts) : localAward(key, stars, opts); }
    catch (e) { r = localAward(key, stars, opts); }
    refreshHUD(); return r;
  }
  function markDone(id) {
    if (id == null || id === "") return;
    var H = window.HDLG;
    if (H && H.markDone) { H.markDone(isNaN(id) ? id : Number(id)); return; }
    var d = jparse(localStorage.getItem("hdlg_completed"), []);
    if (!Array.isArray(d)) d = [];
    if (!d.some(function (v) { return String(v) === String(id); })) d.push(isNaN(id) ? id : Number(id));
    localStorage.setItem("hdlg_completed", JSON.stringify(d)); localStorage.setItem("hdlg_dirty", "1");
  }
  function questGame() {
    var H = window.HDLG;
    if (H && H.questBump) { H.questBump("game", 1); return; }
    var p = function (n) { return (n < 10 ? "0" : "") + n; }, d = new Date();
    var today = d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate());
    var s = jparse(localStorage.getItem("hdlg_quests"), {}); if (!s || typeof s !== "object" || Array.isArray(s)) s = {};
    s.total = s.total || {}; s.subj = s.subj || {}; s.ach = s.ach || []; s.checkin = s.checkin || { last: "", streak: 0 };
    if (s.day !== today) { s.day = today; s.prog = {}; s.claimed = []; s.qbest = {}; s.bonus = false; }
    s.prog = s.prog || {}; s.prog.game = (s.prog.game || 0) + 1; s.total.game = (s.total.game || 0) + 1;
    localStorage.setItem("hdlg_quests", JSON.stringify(s)); localStorage.setItem("hdlg_dirty", "1");
  }
  function refreshHUD() {
    try { var f = G("syncHubHUD"); if (typeof f === "function") f(); } catch (e) {}
  }
  function toast(m) { try { if (window.HDLG && HDLG.toast && m) HDLG.toast(m); } catch (e) {} }

  /* ---------- API cho game ---------- */
  var HDLGGame = {
    configure: function (o) { o = o || {}; for (var k in o) cfg[k] = o[k]; return HDLGGame; },
    context: function () { return { game: gameKey(), lesson: lessonId(), set: setCode(), key: base() }; },

    /* Thắng chặng i với điểm 0–100. Trả về { gained, prev, best } (best/prev tính bằng sao). */
    stage: function (i, score, maxStars) {
      var m = maxStars || STAGE_MAX;
      var stars = Math.min(m, Math.round(Math.max(0, Number(score) || 0) * m / 100));
      return award(base() + "_s" + ((Number(i) || 0) + 1), stars, { silent: true });
    },
    stageBest: function (i) { var H = window.HDLG, k = clean(base() + "_s" + ((Number(i) || 0) + 1));
      return H && H.getBest ? H.getBest(k) : num((jparse(localStorage.getItem("hdlg_best"), {}) || {})[k]); },

    /* Thưởng hoàn thành đề: chỉ nhận 1 lần / đề. Trả về số sao thực nhận (0 nếu đã nhận). */
    bonus: function (n) { return award(base() + "_clear", n == null ? 20 : n, { silent: true }).gained; },

    /* Gọi 1 lần khi mở bảng Tổng kết. */
    finish: function (total, max) {
      markDone(lessonId());
      var L = G("LESSON_ID"); if (L != null && String(L) !== lessonId()) markDone(L);
      questGame();
      var r = award(base() + "_rec", Math.max(0, Math.round(Number(total) || 0)), { noStars: true });
      if (r.improved && r.prev > 0) toast("🏆 Kỷ lục mới: " + r.best + (max ? "/" + max : "") + " điểm!");
      refreshHUD();
      return { record: r.best, newRecord: r.improved, prevRecord: r.prev };
    },

    /* Game 1 màn đơn giản: sao = score/max × maxStars (mặc định 30), chỉ cộng phần vượt kỷ lục. */
    result: function (score, max, maxStars) {
      max = Number(max) || 100; maxStars = maxStars || 30;
      var ratio = Math.min(1, Math.max(0, (Number(score) || 0) / max));
      var r = award(base() + "_total", Math.round(ratio * maxStars), { silent: true });
      var f = HDLGGame.finish(score, max);
      if (r.gained > 0) toast("⭐ +" + r.gained + " sao đã lưu vào tài khoản");
      else toast("Kỷ lục của bạn ở game này: " + r.best + " ⭐ — vượt kỷ lục để nhận thêm sao!");
      return { gained: r.gained, best: r.best, record: f.record, newRecord: f.newRecord };
    }
  };
  window.HDLGGame = HDLGGame;

  /* Khi auth.js tải xong dữ liệu tài khoản từ Firebase → cập nhật lại số sao trên HUD của game */
  window.addEventListener("hdlg:update", refreshHUD);
})();
