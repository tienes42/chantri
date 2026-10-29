/* =========================================================================
   HỌC ĐỂ LÀM GÌ — Tài khoản Firebase + lưu SAO dùng chung cho toàn web & game
   - Đăng nhập Email/Mật khẩu + Google (mẫu từ index (9).html)
   - Sao = localStorage "hdlg_xp"  (Lv = floor(sao/100)+1)
   - Lưu lên Firestore: collection "leaderboard", document = uid
   Nhúng vào trang:
     <script src="/firebase-config.js"></script>
     <script src="/auth.js"></script>
   API cho game:  HDLG.finishLevel({id, score, max})  |  HDLG.addStars(n)
   ========================================================================= */
(function () {
  "use strict";
  if (window.HDLG) return;

  var SDK = "https://www.gstatic.com/firebasejs/8.10.1/";
  var COLLECTION = "leaderboard";
  var SCORE_PER_STAR = 10;            // điểm game / 10 = số sao (chỉnh ở đây)
  var K = { xp: "hdlg_xp", hints: "hdlg_hints", done: "hdlg_completed", best: "hdlg_best",
            owner: "hdlg_owner_uid", dirty: "hdlg_dirty", q: "hdlg_quests" };
  var WATCH = [K.xp, K.hints, K.done, K.best, K.q];
  var cfg = window.HDLG_FIREBASE_CONFIG || {};
  var configured = !!(cfg.apiKey && cfg.projectId);
  var inFrame = false;
  try { inFrame = window.parent !== window; } catch (e) { inFrame = true; }

  var rawSet = Storage.prototype.setItem, rawRemove = Storage.prototype.removeItem;
  var suppress = false, pushTimer = null, auth = null, db = null, user = null;
  var pendingGuestName = "";          // tên khách nhập ở màn đăng nhập, gán vào tài khoản ngay khi tạo xong
  var listeners = [], readyResolve, state = { ready: false, user: null };
  var ready = new Promise(function (r) { readyResolve = r; });

  /* ---------- localStorage helpers ---------- */
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { suppress = true; try { rawSet.call(localStorage, k, v); } catch (e) {} suppress = false; }
  function lsDel(k) { suppress = true; try { rawRemove.call(localStorage, k); } catch (e) {} suppress = false; }
  function num(v) { v = parseInt(v, 10); return isFinite(v) && v > 0 ? v : 0; }
  function jparse(s, d) { try { var v = JSON.parse(s); return v == null ? d : v; } catch (e) { return d; } }
  function doneList() {
    var d = jparse(lsGet(K.done), []), out = [];
    if (Array.isArray(d)) out = d.map(String);
    else if (d && typeof d === "object") out = Object.keys(d).filter(function (k) { return d[k]; });
    return out;
  }
  function readLocal() {
    return { xp: num(lsGet(K.xp)), hints: num(lsGet(K.hints)), completed: doneList(), best: jparse(lsGet(K.best), {}), q: lsGet(K.q) || "" };
  }
  function writeLocal(s) {
    lsSet(K.xp, String(s.xp)); lsSet(K.hints, String(s.hints));
    lsSet(K.done, JSON.stringify(s.completed)); lsSet(K.best, JSON.stringify(s.best));
    if (s.q) lsSet(K.q, s.q); else lsDel(K.q);
  }
  function merge(a, b) {
    var best = {}, k;
    for (k in a.best) best[k] = Math.max(num(a.best[k]), num(b.best && b.best[k]));
    for (k in (b.best || {})) if (!(k in best)) best[k] = num(b.best[k]);
    var set = {}; a.completed.concat(b.completed || []).forEach(function (x) { set[x] = 1; });
    return { xp: Math.max(a.xp, b.xp), hints: Math.max(a.hints, b.hints), completed: Object.keys(set), best: best, q: mergeQ(a.q, b.q) };
  }
  /* Gộp dữ liệu nhiệm vụ/điểm danh của 2 nơi (máy này + Firebase) mà KHÔNG làm mất chuỗi điểm danh */
  function mergeQ(aStr, bStr) {
    var A = jparse(aStr, null), B = jparse(bStr, null);
    var okA = A && typeof A === "object" && !Array.isArray(A), okB = B && typeof B === "object" && !Array.isArray(B);
    if (!okA) return okB ? bStr : (aStr || bStr || "");
    if (!okB) return aStr;
    function maxMap(x, y) { var r = {}, k; x = x || {}; y = y || {}; for (k in x) r[k] = num(x[k]); for (k in y) r[k] = Math.max(num(r[k]), num(y[k])); return r; }
    function union(x, y) { var r = (x || []).slice(); (y || []).forEach(function (v) { if (r.indexOf(v) < 0) r.push(v); }); return r; }
    var r = {}, k;
    for (k in B) r[k] = B[k];
    for (k in A) r[k] = A[k];
    // Điểm danh: lấy bản có ngày điểm danh gần nhất (cùng ngày → chuỗi dài hơn); kỷ lục lấy lớn nhất
    var ca = A.checkin || {}, cb = B.checkin || {}, la = String(ca.last || ""), lb = String(cb.last || "");
    var c = la > lb ? ca : lb > la ? cb : (num(ca.streak) >= num(cb.streak) ? ca : cb);
    r.checkin = { last: String(c.last || ""), streak: num(c.streak), best: Math.max(num(ca.best), num(cb.best), num(ca.streak), num(cb.streak)) };
    r.ach = union(A.ach, B.ach);
    r.total = maxMap(A.total, B.total);
    r.subj = {}; var sa = A.subj || {}, sb = B.subj || {};
    for (k in sb) r.subj[k] = sb[k];
    for (k in sa) if (!r.subj[k] || num(sa[k].plays) >= num(r.subj[k].plays)) r.subj[k] = sa[k];
    // Nhiệm vụ trong ngày: cùng ngày thì gộp, khác ngày thì lấy ngày mới hơn
    var da = String(A.day || ""), db2 = String(B.day || "");
    if (da === db2) {
      r.prog = maxMap(A.prog, B.prog); r.qbest = maxMap(A.qbest, B.qbest);
      r.claimed = union(A.claimed, B.claimed); r.bonus = !!(A.bonus || B.bonus);
    } else {
      var N = da > db2 ? A : B;
      r.day = N.day; r.prog = N.prog || {}; r.qbest = N.qbest || {}; r.claimed = N.claimed || []; r.bonus = !!N.bonus;
    }
    return JSON.stringify(r);
  }
  function level(xp) { return Math.floor(xp / 100) + 1; }
  /* ---------- tên khách ---------- */
  var GUEST_ANIMALS = ["Cú Mèo", "Gấu Trúc", "Cáo Nhỏ", "Sóc Nâu", "Cá Heo", "Đại Bàng", "Mèo Mun", "Thỏ Ngọc", "Rồng Con", "Hổ Con", "Voi Con", "Chim Sẻ", "Kỳ Lân", "Cánh Cụt"];
  var GUEST_TRAITS = ["Thông Thái", "Tò Mò", "Nhanh Nhẹn", "Dũng Cảm", "Chăm Chỉ", "Vui Vẻ", "Sáng Tạo", "Lanh Lợi", "Kiên Trì", "Tinh Anh"];
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function randomGuestName() { return pick(GUEST_ANIMALS) + " " + pick(GUEST_TRAITS) + " " + (10 + Math.floor(Math.random() * 990)); }
  function cleanName(s) { return String(s || "").replace(/[\u0000-\u001f<>]/g, "").replace(/\s+/g, " ").trim().slice(0, 30); }
  function displayName(u) { if (u && u.isAnonymous) return u.displayName || ("Khách " + u.uid.slice(0, 4)); return (u && (u.displayName || (u.email ? u.email.split("@")[0] : ""))) || "Người chơi"; }

  /* ---------- sự kiện ---------- */
  function emit() {
    var x = num(lsGet(K.xp));
    var detail = { user: user, xp: x, level: level(x), inLevel: x % 100, hints: num(lsGet(K.hints)), name: user ? displayName(user) : "", photo: user ? user.photoURL || "" : "" };
    try { window.dispatchEvent(new CustomEvent("hdlg:update", { detail: detail })); } catch (e) {}
    listeners.forEach(function (f) { try { f(detail); } catch (e) {} });
  }

  /* ---------- đẩy lên Firestore ---------- */
  function schedulePush() {
    if (!user || !db) return;
    lsSet(K.dirty, "1");
    clearTimeout(pushTimer); pushTimer = setTimeout(push, 1200);
  }
  function push() {
    if (!user || !db) return Promise.resolve();
    clearTimeout(pushTimer);
    var s = readLocal();
    var data = { name: displayName(user), avatar: user.photoURL || "", xp: s.xp, hints: s.hints,
                 completed: s.completed, best: safeKeys(s.best), quests: (s.q || "").slice(0, 20000),
                 updatedAt: firebase.firestore.FieldValue.serverTimestamp() };
    return db.collection(COLLECTION).doc(user.uid).set(data, { merge: true })
      .then(function () { lsDel(K.dirty); })
      .catch(function (e) { console.warn("[HDLG] Chưa lưu được lên Firebase:", e && e.code || e); });
  }
  function safeKeys(o) { var r = {}; for (var k in o) r[String(k).replace(/[^A-Za-z0-9_\-]/g, "_")] = num(o[k]); return r; }

  function hook() {
    Storage.prototype.setItem = function (k, v) {
      rawSet.apply(this, arguments);
      if (!suppress && this === window.localStorage && WATCH.indexOf(k) >= 0) { schedulePush(); emit(); }
    };
    Storage.prototype.removeItem = function (k) {
      rawRemove.apply(this, arguments);
      if (!suppress && this === window.localStorage && WATCH.indexOf(k) >= 0) { schedulePush(); emit(); }
    };
    window.addEventListener("storage", function (e) { if (WATCH.indexOf(e.key) >= 0) emit(); });
    window.addEventListener("pagehide", function () { if (lsGet(K.dirty)) push(); });
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden" && lsGet(K.dirty)) push();
      else if (document.visibilityState === "visible" && user) emit();
    });
  }

  /* ---------- đồng bộ khi đăng nhập ---------- */
  function syncOnLogin() {
    var ref = db.collection(COLLECTION).doc(user.uid);
    return ref.get().then(function (snap) {
      var remote = snap.exists ? snap.data() : null;
      var rs = remote ? { xp: num(remote.xp), hints: num(remote.hints), completed: (remote.completed || []).map(String), best: remote.best || {}, q: typeof remote.quests === "string" ? remote.quests : "" }
                      : { xp: 0, hints: 0, completed: [], best: {}, q: "" };
      var local = readLocal(), owner = lsGet(K.owner), result;
      if (owner === user.uid) {
        result = Object.assign({}, lsGet(K.dirty) ? local : (remote ? rs : local));
        result.q = mergeQ(local.q, rs.q);                // điểm danh ở máy khác / chưa kịp lưu vẫn được giữ
      }
      else if (!owner) result = merge(local, rs);        // tiến trình chơi thử trước khi đăng nhập
      else result = rs;                                  // máy đang dùng bởi tài khoản khác
      writeLocal(result); lsSet(K.owner, user.uid);
      var changed = !remote || result.xp !== rs.xp || result.hints !== rs.hints ||
        result.completed.length !== rs.completed.length || result.q !== rs.q || remote.name !== displayName(user) || (remote.avatar || "") !== (user.photoURL || "");
      if (changed || lsGet(K.dirty)) return push();
    }).catch(function (e) { console.warn("[HDLG] Không đọc được Firestore (kiểm tra Rules):", e && e.code || e); })
      .then(emit);
  }

  function saveAccountLocal(u) {
    lsSet("user_id", u.uid); lsSet("hdlg_display_name", displayName(u));
    lsSet("hdlg_email", u.email || ""); lsSet("hdlg_photo_url", u.photoURL || "");
  }
  function clearAccountLocal() {
    ["user_id", "hdlg_display_name", "hdlg_email", "hdlg_photo_url", K.xp, K.hints, K.done, K.best, K.q, K.owner, K.dirty].forEach(lsDel);
  }

  /* ---------- Nhiệm vụ / thử thách (dữ liệu dùng chung, quests.js vẽ giao diện) ---------- */
  function pad2(n) { return (n < 10 ? "0" : "") + n; }
  function today() { var d = new Date(); return d.getFullYear() + "-" + pad2(d.getMonth() + 1) + "-" + pad2(d.getDate()); }
  function questGet() {
    var s = jparse(lsGet(K.q), {});
    if (!s || typeof s !== "object" || Array.isArray(s)) s = {};
    s.total = s.total || {}; s.subj = s.subj || {}; s.ach = s.ach || []; s.checkin = s.checkin || { last: "", streak: 0 };
    if (s.day !== today()) { s.day = today(); s.prog = {}; s.claimed = []; s.qbest = {}; s.bonus = false; }
    s.prog = s.prog || {}; s.claimed = s.claimed || []; s.qbest = s.qbest || {};
    return s;
  }
  function questSave(s) {
    lsSet(K.q, JSON.stringify(s)); schedulePush(); emit();
    try { window.dispatchEvent(new CustomEvent("hdlg:quests", { detail: s })); } catch (e) {}
  }
  function questBump(key, n) {
    var s = questGet(); n = n || 1;
    s.prog[key] = (s.prog[key] || 0) + n; s.total[key] = (s.total[key] || 0) + n;
    questSave(s); return s;
  }

  /* ---------- API cho game ---------- */
  function addStars(n, label) {
    n = Math.round(n); if (!(n > 0)) return 0;
    lsSet(K.xp, String(num(lsGet(K.xp)) + n)); schedulePush(); emit(); toast("⭐ +" + n + " sao" + (label ? " · " + label : ""));
    return n;
  }
  function markDone(id) {
    if (id == null || id === "") return;
    var d = jparse(lsGet(K.done), []);
    if (Array.isArray(d)) { if (d.map(String).indexOf(String(id)) < 0) d.push(isNaN(id) ? id : Number(id)); }
    else if (d && typeof d === "object") d[id] = true; else d = [id];
    lsSet(K.done, JSON.stringify(d));
  }
  function finishLevel(o) {
    o = o || {};
    var score = Math.max(0, Number(o.score) || 0), max = Number(o.max) || 100;
    var gameKey = String(o.game || location.pathname.split("/").pop().replace(/\.html?$/, "") || "game");
    var key = gameKey + (o.id != null && o.id !== "" ? "_" + o.id : "");
    key = key.replace(/[^A-Za-z0-9_\-]/g, "_");
    var stars = Math.round(score / SCORE_PER_STAR);
    var best = jparse(lsGet(K.best), {}), prev = num(best[key]), gain = Math.max(0, stars - prev);
    if (gain > 0) { best[key] = stars; lsSet(K.best, JSON.stringify(best)); }
    if (score >= max * 0.5) markDone(o.id);
    if (gain > 0) lsSet(K.xp, String(num(lsGet(K.xp)) + gain));
    if (o.game !== "quick") questBump("game", 1);
    schedulePush(); emit();
    if (gain > 0) toast("⭐ +" + gain + " sao đã lưu vào tài khoản");
    else toast(user ? "Bạn đã đạt " + prev + " sao ở màn này — hãy phá kỷ lục để nhận thêm!" : "");
    return { gained: gain, stars: stars, best: Math.max(prev, stars), total: num(lsGet(K.xp)) };
  }

  /* Thưởng theo KỶ LỤC cho 1 khóa bất kỳ (dùng bởi /games/hdlg-game.js):
     chỉ cộng phần sao VƯỢT kỷ lục cũ của khóa đó → chơi lại không bị cộng vô hạn. */
  function award(key, stars, opts) {
    opts = opts || {};
    key = String(key || "game").replace(/[^A-Za-z0-9_\-]/g, "_");
    stars = Math.max(0, Math.round(Number(stars) || 0));
    var best = jparse(lsGet(K.best), {}) || {}, prev = num(best[key]), gain = Math.max(0, stars - prev);
    if (gain > 0) {
      best[key] = stars; lsSet(K.best, JSON.stringify(best));
      if (!opts.noStars) lsSet(K.xp, String(num(lsGet(K.xp)) + gain));   // noStars: chỉ ghi kỷ lục điểm
      schedulePush(); emit();
      if (!opts.silent && !opts.noStars) toast("⭐ +" + gain + " sao" + (opts.label ? " · " + opts.label : ""));
    }
    return { gained: opts.noStars ? 0 : gain, improved: gain > 0, prev: prev, best: Math.max(prev, stars), total: num(lsGet(K.xp)) };
  }
  function getBest(key) { return num((jparse(lsGet(K.best), {}) || {})[String(key).replace(/[^A-Za-z0-9_\-]/g, "_")]); }

  /* ---------- Sao khi HỌC BÀI (mỗi phần chỉ nhận 1 lần / bài) ----------
     Lưu trong "hdlg_best" với khóa lesson_<id>_<phần> = số sao đã nhận
     → tự đồng bộ Firebase như sao của game.
     Phần: "read" (đọc hết bài) | "quiz" (đúng Kiểm tra nhanh ngay lần đầu)  */
  var LESSON_STARS = 10;              // tổng sao tối đa của 1 bài học (khớp "10 XP/bài" ở trang lớp)
  function lessonKey(id, part) { return ("lesson_" + id + "_" + part).replace(/[^A-Za-z0-9_\-]/g, "_"); }
  function lessonStatus(id) {
    var best = jparse(lsGet(K.best), {}) || {};
    var read = num(best[lessonKey(id, "read")]), quiz = num(best[lessonKey(id, "quiz")]);
    var stars = read + quiz;
    return { read: read > 0, quiz: quiz > 0, stars: stars, done: read > 0 };
  }
  function lessonReward(id, part, n, opts) {
    opts = opts || {};
    if (id == null || id === "" || !part) return 0;
    n = Math.round(n); if (!(n > 0)) return 0;
    var best = jparse(lsGet(K.best), {}) || {}, key = lessonKey(id, part);
    if (num(best[key]) > 0) return 0;                       // đã nhận phần này rồi
    var wasDone = lessonStatus(id).done;
    best[key] = n; lsSet(K.best, JSON.stringify(best));
    lsSet(K.xp, String(num(lsGet(K.xp)) + n));
    if (!wasDone && lessonStatus(id).done) { markDone("lesson_" + id); questBump("lesson", 1); }
    schedulePush(); emit();
    toast("⭐ +" + n + " sao" + (opts.label ? " · " + opts.label : ""));
    try { window.dispatchEvent(new CustomEvent("hdlg:lesson", { detail: { id: id, part: part, gained: n, status: lessonStatus(id) } })); } catch (e) {}
    return n;
  }
  /* Thống kê 1 danh sách bài học (dùng cho trang lớp / chủ đề) */
  function lessonStats(list) {
    list = Array.isArray(list) ? list : [];
    var done = 0, stars = 0;
    list.forEach(function (l) { var st = lessonStatus(l && l.id != null ? l.id : l); if (st.done) done++; stars += st.stars; });
    var total = list.length;
    return { done: done, total: total, stars: stars, maxStars: total * LESSON_STARS,
             percent: total ? Math.round(100 * done / total) : 0 };
  }
  function getLeaderboard(n) {
    if (!db) return Promise.resolve([]);
    return db.collection(COLLECTION).orderBy("xp", "desc").limit(n || 10).get().then(function (qs) {
      var out = []; qs.forEach(function (d) { var v = d.data(); out.push({ uid: d.id, name: v.name || "Người chơi", avatar: v.avatar || "", xp: num(v.xp) }); });
      return out;
    }).catch(function (e) { console.warn("[HDLG] Không đọc được bảng xếp hạng:", e && e.code || e); return []; });
  }

  /* ---------- giao diện ---------- */
  var CSS = "\
.hdlg-ov{position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(5,12,30,.72);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);font-family:'Segoe UI',Roboto,Arial,sans-serif}\
.hdlg-ov[hidden],.hdlg-box [hidden]{display:none!important}\
.hdlg-box{width:100%;max-width:400px;max-height:92vh;overflow:auto;background:linear-gradient(160deg,#16325f,#0c1a38);color:#eaf2ff;border:1px solid #4a74c9;border-radius:18px;padding:22px;box-shadow:0 20px 60px rgba(0,0,0,.55);position:relative}\
.hdlg-box h2{margin:0 0 4px;font-size:22px;text-align:center}\
.hdlg-sub{margin:0 0 14px;text-align:center;color:#a9bde6;font-size:13px}\
.hdlg-box input{width:100%;box-sizing:border-box;margin-bottom:10px;padding:11px 12px;border-radius:10px;border:1px solid #3a5a9c;background:#0a1630;color:#fff;font-size:15px;outline:none}\
.hdlg-box input:focus{border-color:#62d7ff}\
.hdlg-btn{display:block;width:100%;padding:11px;border:0;border-radius:10px;font-weight:700;font-size:15px;cursor:pointer;background:#ffd65d;color:#1b1b1b}\
.hdlg-btn:disabled{opacity:.6;cursor:wait}\
.hdlg-btn.g{background:#fff;color:#222;margin-top:10px}\
.hdlg-btn.o{background:transparent;color:#ff9b9b;border:1px solid #ff9b9b;margin-top:12px}\
.hdlg-err{background:#ff4d4d26;border:1px solid #ff7b7b88;color:#ffb3b3;padding:8px 10px;border-radius:8px;font-size:13px;margin-bottom:10px}\
.hdlg-or{text-align:center;color:#8aa0cc;font-size:12px;margin:12px 0 0}\
.hdlg-tg{text-align:center;margin-top:14px;font-size:13px;color:#a9bde6}\
.hdlg-tg a{color:#62d7ff;cursor:pointer;font-weight:700;margin-left:4px}\
.hdlg-x{position:absolute;top:10px;right:12px;background:none;border:0;color:#a9bde6;font-size:22px;cursor:pointer}\
.hdlg-row{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:10px;background:#ffffff10;margin-bottom:6px}\
.hdlg-row.me{background:#ffd65d30;border:1px solid #ffd65d88}\
.hdlg-row i{width:26px;text-align:center;font-style:normal;font-weight:700;color:#ffd65d}\
.hdlg-row b{flex:1;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}\
.hdlg-row strong{color:#ffd65d}\
.hdlg-av{width:30px;height:30px;border-radius:50%;background:#2c5aa8;object-fit:cover;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;flex:none}\
.hdlg-big{display:flex;flex-direction:column;align-items:center;gap:6px;margin-bottom:10px}\
.hdlg-big .hdlg-av{width:64px;height:64px;font-size:28px}\
.hdlg-stats{display:flex;gap:8px;margin:10px 0}\
.hdlg-stats div{flex:1;text-align:center;background:#ffffff12;border-radius:10px;padding:8px}\
.hdlg-stats b{display:block;font-size:20px;color:#ffd65d}\
.hdlg-toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:100000;background:#0c1a38ee;color:#ffe9a3;border:1px solid #ffd65d;border-radius:999px;padding:9px 18px;font:600 14px 'Segoe UI',Arial,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.4);transition:opacity .4s;pointer-events:none}\
.hdlg-guest{margin-top:10px;padding:12px;border-radius:12px;background:#ffffff0d;border:1px dashed #4a74c9;animation:hdlgIn .22s ease-out}\
.hdlg-guest label{display:block;font-size:13px;font-weight:600;margin-bottom:6px;color:#cfe0ff}\
.hdlg-guest small{display:block;font-size:12px;color:#8aa0cc;margin:-2px 0 10px}\
.hdlg-gr{display:flex;gap:8px}\
.hdlg-gr input{flex:1;min-width:0}\
.hdlg-dice{flex:none;width:44px;height:42px;border-radius:10px;border:1px solid #3a5a9c;background:#0a1630;font-size:20px;cursor:pointer}\
.hdlg-dice:hover{border-color:#62d7ff}\
@keyframes hdlgIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}\
.hdlg-warn{position:fixed;left:8px;bottom:8px;z-index:99998;background:#ffefc2;color:#5a3b00;border-radius:8px;padding:6px 10px;font:12px Arial,sans-serif;max-width:300px}";

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in (attrs || {})) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function avatarHTML(name, photo) {
    return photo ? '<img class="hdlg-av" referrerpolicy="no-referrer" src="' + esc(photo) + '" alt="">'
                 : '<span class="hdlg-av">' + esc((name || "?").charAt(0).toUpperCase()) + "</span>";
  }
  function toast(msg) {
    if (!msg || !document.body) return;
    var t = el("div", { "class": "hdlg-toast" }, esc(msg)); document.body.appendChild(t);
    setTimeout(function () { t.style.opacity = "0"; }, 2600); setTimeout(function () { t.remove(); }, 3100);
  }

  var overlay = null;
  function openModal(html, closable) {
    closeModal();
    overlay = el("div", { "class": "hdlg-ov" }, '<div class="hdlg-box">' + (closable ? '<button class="hdlg-x" aria-label="Đóng">×</button>' : "") + html + "</div>");
    document.body.appendChild(overlay);
    if (closable) {
      overlay.querySelector(".hdlg-x").onclick = closeModal;
      overlay.addEventListener("mousedown", function (e) { if (e.target === overlay) closeModal(); });
    }
    return overlay;
  }
  function closeModal() { if (overlay) { overlay.remove(); overlay = null; } }

  var ERR = {
    "auth/email-already-in-use": "Email này đã được đăng ký. Hãy thử đăng nhập.",
    "auth/invalid-email": "Email không hợp lệ.",
    "auth/weak-password": "Mật khẩu quá yếu (cần ít nhất 6 ký tự).",
    "auth/user-not-found": "Không tìm thấy tài khoản với email này.",
    "auth/wrong-password": "Sai mật khẩu. Vui lòng thử lại.",
    "auth/invalid-credential": "Email hoặc mật khẩu không đúng.",
    "auth/too-many-requests": "Bạn đã thử quá nhiều lần. Vui lòng chờ một lát.",
    "auth/unauthorized-domain": "Tên miền này chưa được cấp phép trong Firebase (Authentication > Settings > Authorized domains).",
    "auth/popup-blocked": "Trình duyệt đã chặn cửa sổ popup đăng nhập. Hãy cho phép popup rồi thử lại.",
    "auth/popup-closed-by-user": "Cửa sổ đăng nhập Google đã bị đóng trước khi hoàn tất.",
    "auth/cancelled-popup-request": "Yêu cầu đăng nhập trước đó chưa hoàn tất, vui lòng thử lại.",
    "auth/operation-not-allowed": "Phương thức đăng nhập này chưa được bật trong Firebase.",
    "auth/admin-restricted-operation": "Chế độ khách (Anonymous) chưa được bật trong Firebase → Authentication → Sign-in method.",
    "auth/credential-already-in-use": "Tài khoản này đã tồn tại. Hãy đăng nhập bằng nó (sao của khách sẽ không được gộp).",
    "auth/provider-already-linked": "Tài khoản đã được liên kết rồi.",
    "auth/network-request-failed": "Lỗi kết nối mạng. Vui lòng kiểm tra Internet và thử lại.",
    "auth/internal-error": "Lỗi nội bộ từ Firebase — thường do tên miền chưa được cấp phép hoặc cấu hình API Key sai."
  };
  function errText(code) { if (code && !ERR[code]) console.warn("[Firebase Auth]", code); return ERR[code] || "Đã có lỗi xảy ra (mã: " + (code || "không rõ") + "). Vui lòng thử lại."; }

  function showLogin(upgrade) {
    upgrade = upgrade === true;
    var reg = upgrade;
    var guest = !!(user && user.isAnonymous);
    var ov = openModal(
      '<h2 id="hdT">🔐 Đăng nhập</h2><p class="hdlg-sub" id="hdS">Đăng nhập để lưu sao và tiến trình học của bạn</p>' +
      '<div class="hdlg-err" id="hdE" hidden></div>' +
      '<form id="hdF"><input id="hdN" type="text" placeholder="Tên hiển thị" maxlength="30" hidden>' +
      '<input id="hdM" type="email" placeholder="Email" required autocomplete="email">' +
      '<input id="hdP" type="password" placeholder="Mật khẩu (ít nhất 6 ký tự)" required minlength="6" autocomplete="current-password">' +
      '<button class="hdlg-btn" id="hdB" type="submit">Đăng nhập</button></form>' +
      '<p class="hdlg-or">— hoặc —</p><button class="hdlg-btn g" id="hdG" type="button">🔵 Đăng nhập bằng Google</button>' +
      '<button class="hdlg-btn g" id="hdK" type="button" style="background:#2c5aa8;color:#fff">👤 Chơi với tư cách khách</button>' +
      '<div class="hdlg-guest" id="hdGW" hidden><label for="hdGN">Bạn muốn được gọi là gì?</label>' +
      '<div class="hdlg-gr"><input id="hdGN" type="text" placeholder="Nhập tên (có thể bỏ trống)" maxlength="30" autocomplete="nickname" enterkeyhint="go">' +
      '<button class="hdlg-dice" id="hdGD" type="button" title="Gợi ý tên ngẫu nhiên" aria-label="Gợi ý tên ngẫu nhiên">🎲</button></div>' +
      '<small>Bỏ trống sẽ được đặt tên ngẫu nhiên. Có thể đổi tên sau trong mục Tài khoản.</small>' +
      '<button class="hdlg-btn" id="hdGS" type="button">🚀 Vào chơi</button></div>' +
      '<p class="hdlg-tg"><span id="hdL">Chưa có tài khoản?</span><a id="hdA">Đăng ký</a></p>', upgrade);
    var $ = function (id) { return ov.querySelector("#" + id); };
    function err(m) { $("hdE").textContent = m || ""; $("hdE").hidden = !m; }
    function busy(b) { $("hdB").disabled = b; $("hdG").disabled = b; $("hdK").disabled = b; $("hdGS").disabled = b; }
    function linked() { closeModal(); saveAccountLocal(user); push().then(emit); emit(); toast("✅ Đã nâng cấp tài khoản, sao được giữ lại"); }
    if (upgrade) {
      $("hdK").hidden = true; $("hdL").parentNode.hidden = false;
      $("hdT").textContent = "⬆ Nâng cấp tài khoản"; $("hdS").textContent = "Đăng ký để giữ sao của khách và chơi trên nhiều thiết bị";
      $("hdB").textContent = "Tạo tài khoản"; $("hdN").hidden = false; $("hdL").parentNode.hidden = true;
    }
    // Bước 1: bấm "Chơi với tư cách khách" → hiện ô nhập tên ngay bên dưới
    $("hdK").onclick = function () {
      err("");
      var box = $("hdGW"); box.hidden = !box.hidden;
      if (!box.hidden) setTimeout(function () { $("hdGN").focus(); }, 30);
    };
    $("hdGD").onclick = function () { $("hdGN").value = randomGuestName(); $("hdGN").focus(); };
    // Bước 2: bấm "Vào chơi" (hoặc Enter) → tạo tài khoản khách với tên đã nhập / tên ngẫu nhiên
    function startGuest() {
      err(""); busy(true);
      $("hdGS").textContent = "Đang vào…";
      pendingGuestName = cleanName($("hdGN").value) || randomGuestName();
      auth.signInAnonymously().catch(function (x) {
        pendingGuestName = ""; err(errText(x.code)); busy(false); $("hdGS").textContent = "🚀 Vào chơi";
      });
    }
    $("hdGS").onclick = startGuest;
    $("hdGN").addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); startGuest(); } });
    $("hdA").onclick = function () {
      if (upgrade) return;
      reg = !reg; err("");
      $("hdT").textContent = reg ? "📝 Đăng ký" : "🔐 Đăng nhập";
      $("hdB").textContent = reg ? "Tạo tài khoản" : "Đăng nhập";
      $("hdL").textContent = reg ? "Đã có tài khoản?" : "Chưa có tài khoản?";
      $("hdA").textContent = reg ? "Đăng nhập" : "Đăng ký";
      $("hdN").hidden = !reg;
      $("hdP").autocomplete = reg ? "new-password" : "current-password";
    };
    $("hdF").onsubmit = function (e) {
      e.preventDefault(); err(""); busy(true);
      var email = $("hdM").value.trim(), pw = $("hdP").value, nm = $("hdN").value.trim();
      var p;
      if (upgrade && guest) p = user.linkWithCredential(firebase.auth.EmailAuthProvider.credential(email, pw))
        .then(function () { return nm ? user.updateProfile({ displayName: nm }) : null; }).then(linked);
      else p = reg ? auth.createUserWithEmailAndPassword(email, pw).then(function (c) { return nm ? c.user.updateProfile({ displayName: nm }) : null; })
                   : auth.signInWithEmailAndPassword(email, pw);
      p.catch(function (x) { err(errText(x.code)); }).then(function () { busy(false); });
    };
    $("hdG").onclick = function () {
      err(""); busy(true);
      var gp = new firebase.auth.GoogleAuthProvider(), p;
      if (upgrade && guest) p = user.linkWithPopup(gp).then(linked).catch(function (x) {
        if (x.code === "auth/credential-already-in-use" && x.credential) return auth.signInWithCredential(x.credential);
        throw x; });
      else p = auth.signInWithPopup(gp);
      p.catch(function (x) { err(errText(x.code)); }).then(function () { busy(false); });
    };
  }

  function logout() {
    if (user && user.isAnonymous && !confirm("Tài khoản khách sẽ MẤT toàn bộ sao nếu thoát. Bạn vẫn muốn thoát?")) return Promise.resolve();
    return push().then(function () { clearAccountLocal(); return auth.signOut(); }).then(function () { location.reload(); });
  }

  /* Đổi tên hiển thị: cập nhật hồ sơ Firebase + tên trên bảng xếp hạng */
  function rename(nm) {
    nm = cleanName(nm);
    if (!user || !nm) return Promise.reject({ code: "hdlg/empty-name" });
    return user.updateProfile({ displayName: nm }).then(function () { saveAccountLocal(user); emit(); return push(); }).then(emit);
  }

  function showAccount() {
    if (!user) return showLogin();
    var x = num(lsGet(K.xp)), name = displayName(user);
    var ov = openModal('<div class="hdlg-big">' + avatarHTML(name, user.photoURL) + "<h2>" + esc(name) + '</h2><div class="hdlg-sub" style="margin:0">' + esc(user.email || "") + "</div></div>" +
      '<div class="hdlg-stats"><div><b>⭐ ' + x + "</b>Sao</div><div><b>Lv." + level(x) + "</b>Cấp độ</div><div><b>🎫 " + num(lsGet(K.hints)) + "</b>Gợi ý</div></div>" +
      '<button class="hdlg-btn" id="hdR">🏆 Xem bảng xếp hạng</button>' +
      '<button class="hdlg-btn g" id="hdRN" type="button">✏️ Đổi tên hiển thị</button>' +
      '<form class="hdlg-guest" id="hdRW" hidden><div class="hdlg-gr"><input id="hdRI" type="text" maxlength="30" placeholder="Tên mới" autocomplete="nickname">' +
      '<button class="hdlg-dice" id="hdRD" type="button" title="Tên ngẫu nhiên" aria-label="Tên ngẫu nhiên">🎲</button></div>' +
      '<div class="hdlg-err" id="hdRE" hidden></div><button class="hdlg-btn" id="hdRS" type="submit">💾 Lưu tên</button></form>' +
      (user.isAnonymous ? '<button class="hdlg-btn g" id="hdU">⬆ Đăng ký để giữ sao</button><p class="hdlg-sub" style="margin-top:8px">Bạn đang chơi với tư cách khách. Xóa dữ liệu trình duyệt hoặc thoát sẽ mất sao.</p>' : "") +
      '<button class="hdlg-btn o" id="hdO">' + (user.isAnonymous ? "Thoát chế độ khách" : "Đăng xuất") + "</button>", true);
    if (user.isAnonymous) ov.querySelector("#hdU").onclick = function () { showLogin(true); };
    var q = function (id) { return ov.querySelector("#" + id); };
    q("hdRN").onclick = function () {
      var w = q("hdRW"); w.hidden = !w.hidden;
      if (!w.hidden) { q("hdRI").value = name; q("hdRI").focus(); q("hdRI").select(); }
    };
    q("hdRD").onclick = function () { q("hdRI").value = randomGuestName(); q("hdRI").focus(); };
    q("hdRW").onsubmit = function (e) {
      e.preventDefault();
      var nm = cleanName(q("hdRI").value), b = q("hdRS");
      if (!nm) { q("hdRE").textContent = "Tên không được để trống."; q("hdRE").hidden = false; return; }
      b.disabled = true; b.textContent = "Đang lưu…";
      rename(nm).then(function () { toast("✅ Đã đổi tên thành " + nm); showAccount(); })
        .catch(function (x) { q("hdRE").textContent = errText(x && x.code); q("hdRE").hidden = false; b.disabled = false; b.textContent = "💾 Lưu tên"; });
    };
    ov.querySelector("#hdR").onclick = showLeaderboard;
    ov.querySelector("#hdO").onclick = function () { var b = this, t = b.textContent; b.disabled = true; b.textContent = "Đang lưu & đăng xuất…"; logout().then(function () { b.disabled = false; b.textContent = t; }); };
  }

  function showLeaderboard() {
    var ov = openModal('<h2>🏆 Bảng xếp hạng</h2><p class="hdlg-sub">Top 10 người nhiều sao nhất</p><div id="hdLB">Đang tải…</div>', true);
    getLeaderboard(10).then(function (list) {
      var box = ov.querySelector("#hdLB"); if (!box) return;
      if (!list.length) { box.textContent = "Chưa có dữ liệu."; return; }
      box.innerHTML = list.map(function (r, i) {
        return '<div class="hdlg-row' + (user && r.uid === user.uid ? " me" : "") + '"><i>' + (i === 0 ? "👑" : i + 1) + "</i>" + avatarHTML(r.name, r.avatar) + "<b>" + esc(r.name) + "</b><strong>⭐ " + r.xp + "</strong></div>";
      }).join("");
    });
  }

  /* ---------- khởi động ---------- */
  function loadScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement("script"); s.src = src; s.onload = res; s.onerror = function () { rej(new Error("Không tải được " + src)); };
      document.head.appendChild(s);
    });
  }
  function whenBody(fn) { if (document.body) fn(); else document.addEventListener("DOMContentLoaded", fn); }

  function init() {
    hook();
    whenBody(function () { document.head.appendChild(el("style", {}, CSS)); });
    if (!configured) {
      console.warn("[HDLG] Chưa dán cấu hình Firebase vào /firebase-config.js — tạm thời chưa có đăng nhập.");
      state.ready = true; readyResolve(null);
      if (!inFrame) whenBody(function () { document.body.appendChild(el("div", { "class": "hdlg-warn" }, "⚠ Chưa cấu hình Firebase (file firebase-config.js)")); });
      return;
    }
    loadScript(SDK + "firebase-app.js").then(function () {
      return Promise.all([loadScript(SDK + "firebase-auth.js"), loadScript(SDK + "firebase-firestore.js")]);
    }).then(function () {
      if (!firebase.apps.length) firebase.initializeApp(cfg);
      auth = firebase.auth(); db = firebase.firestore();
      auth.onAuthStateChanged(function (u) {
        user = u; state.user = u;
        if (u) {
          if (!inFrame) whenBody(closeModal);
          // Khách vừa nhập tên → ghi tên vào hồ sơ Firebase TRƯỚC khi đồng bộ lên bảng xếp hạng
          var nm = pendingGuestName; pendingGuestName = "";
          var pre = (nm && u.isAnonymous && !u.displayName)
            ? u.updateProfile({ displayName: nm }).catch(function (e) { console.warn("[HDLG] Không lưu được tên khách:", e && e.code || e); })
            : Promise.resolve();
          pre.then(function () {
            saveAccountLocal(u);
            if (nm && u.isAnonymous) toast("👋 Chào " + displayName(u) + "!");
            return syncOnLogin();
          }).then(function () { state.ready = true; readyResolve(u); });
        } else {
          state.ready = true; readyResolve(null); emit();
          if (!inFrame) whenBody(showLogin);
        }
      });
    }).catch(function (e) { console.error("[HDLG] Lỗi khởi tạo Firebase:", e); state.ready = true; readyResolve(null); });
  }

  window.HDLG = {
    ready: ready, configured: configured,
    get user() { return user; },
    getStars: function () { return num(lsGet(K.xp)); },
    getLevel: function () { return level(num(lsGet(K.xp))); },
    addStars: addStars, finishLevel: finishLevel, award: award, getBest: getBest, markDone: function (id) { markDone(id); schedulePush(); emit(); }, getLeaderboard: getLeaderboard,
    lessonReward: lessonReward, lessonStatus: lessonStatus, lessonStats: lessonStats, LESSON_STARS: LESSON_STARS,
    showLogin: showLogin, showAccount: showAccount, rename: rename, randomName: randomGuestName, showLeaderboard: showLeaderboard, logout: logout,
    onChange: function (f) { listeners.push(f); }, flush: push,
    today: today, questGet: questGet, questSave: questSave, questBump: questBump, toast: toast
  };
  init();
})();

/* =========================================================================
   DÒNG CHỮ TÁC GIẢ MỜ NHẸ (WATERMARK) TRÊN TOÀN BỘ CÁC TRANG
   ========================================================================= */
(function injectGlobalAuthorCredit() {
  function mountAuthorBadge() {
    if (!document.body || document.getElementById("hdlgAuthorCredit")) return;

    const style = document.createElement("style");
    style.textContent = `
      #hdlgAuthorCredit {
        position: fixed;
        right: 12px;
        bottom: 5px;
        z-index: 9999;
        font: 400 10px/1.2 "Segoe UI", system-ui, -apple-system, sans-serif;
        color: rgba(255, 255, 255, 0.32);
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.35);
        letter-spacing: 0.3px;
        pointer-events: none;
        user-select: none;
        white-space: nowrap;
      }
      @media (max-width: 650px) {
        #hdlgAuthorCredit {
          right: 8px;
          bottom: 3px;
          font-size: 9px;
        }
      }
    `;

    const badge = document.createElement("div");
    badge.id = "hdlgAuthorCredit";
    badge.textContent = "Web được làm bởi Nguyễn Duy Khang và Cao Nhựt Tiến";

    document.head.appendChild(style);
    document.body.appendChild(badge);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountAuthorBadge);
  } else {
    mountAuthorBadge();
  }
})();

/* Nút 🏠 về trang chủ (góc trên trái, mọi trang trừ trang chủ) — xem /home-button.js */
(function () {
  if (window.__hdlgHomeBtn || document.querySelector('script[src*="home-button.js"]')) return;
  var s = document.createElement("script"); s.src = "/home-button.js"; s.defer = true;
  (document.head || document.documentElement).appendChild(s);
})();
