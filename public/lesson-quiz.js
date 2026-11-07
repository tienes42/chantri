/* =========================================================
   LESSON-QUIZ.JS — BỘ 10 CÂU HỎI THEO 3 MỨC ĐỘ (BIẾT – HIỂU – VẬN DỤNG)
   Hỗ trợ đầy đủ hiển thị ký hiệu Toán / Lý / Hóa (KaTeX + Offline Renderer)
   trong câu hỏi, 4 đáp án trắc nghiệm (A, B, C, D), 4 mệnh đề Đúng/Sai (a, b, c, d),
   đơn vị trả lời ngắn và lời giải chi tiết.
========================================================= */
(function () {
  "use strict";

  var LEVELS = {
    biet:    { label: "Biết",      icon: "🟢", cls: "lv-biet" },
    hieu:    { label: "Hiểu",      icon: "🔵", cls: "lv-hieu" },
    vandung: { label: "Vận dụng",  icon: "🟠", cls: "lv-vandung" }
  };
  var TYPE_LABEL = { mcq: "Trắc nghiệm", tf: "Đúng / Sai", tf4: "Đúng / Sai", short: "Trả lời ngắn" };
  var LETTERS = ["A", "B", "C", "D", "E", "F"];

  function esc(v) {
    if (v === null || v === undefined) return "";
    return String(v).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#039;");
  }

  function stripLatexForCompare(v) {
    return String(v == null ? "" : v)
      .replace(/\$/g, "")
      .replace(/\{,\}/g, ".")
      .replace(/\\(?:text|mathrm|textbf|mathbf)\{([^}]*)\}/g, "$1")
      .replace(/\\(?:left|right|quad|qquad|,|;|:|!)/g, "")
      .replace(/[{}]/g, "");
  }

  function normalizeAnswer(v) {
    return stripLatexForCompare(v)
      .toLowerCase()
      .normalize("NFC")
      .replace(/[−–—]/g, "-")
      .replace(/\s+/g, "")
      .replace(/,/g, ".")
      .replace(/\.$/, "");
  }

  function toNumber(v) {
    var s = normalizeAnswer(v).replace(/[^0-9.\-\/]/g, "");
    if (!s) return null;
    if (/^-?\d+\/\d+$/.test(s)) { var p = s.split("/"); return Number(p[0]) / Number(p[1]); }
    var n = Number(s);
    return isFinite(n) ? n : null;
  }

  function shortIsCorrect(input, accepted) {
    var list = Array.isArray(accepted) ? accepted : [accepted];
    var a = normalizeAnswer(input);
    if (!a) return false;
    for (var i = 0; i < list.length; i++) {
      var b = normalizeAnswer(list[i]);
      if (a === b) return true;
      if (/^-?[\d.\/]+$/.test(a) && /^-?[\d.\/]+$/.test(b)) {
        var x = toNumber(a), y = toNumber(b);
        if (x !== null && y !== null && Math.abs(x - y) < 1e-9) return true;
      }
    }
    return false;
  }

  function render(container, quiz, opts) {
    opts = opts || {};
    var inline = typeof opts.inline === "function"
      ? opts.inline
      : (window.HDLGMath && typeof window.HDLGMath.inline === "function" ? window.HDLGMath.inline : esc);
    var fmt = typeof opts.format === "function"
      ? opts.format
      : function (t) { return "<p>" + inline(t) + "</p>"; };
    var upgrade = typeof opts.upgrade === "function"
      ? opts.upgrade
      : (window.HDLGMath && typeof window.HDLGMath.upgrade === "function" ? window.HDLGMath.upgrade : function () {});

    if (!container || !Array.isArray(quiz) || !quiz.length) return null;

    var passMark = opts.passMark || Math.ceil(quiz.length * 0.7);
    var state = { answered: 0, correct: 0, results: [], finishedOnce: false };

    container.innerHTML = "";
    container.style.display = "";

    /* ---------- thanh tiến độ ---------- */
    var bar = document.createElement("div");
    bar.className = "qz-status";
    bar.innerHTML =
      '<div class="qz-status-text"><b>Bài luyện tập ' + quiz.length + ' câu</b> · ' +
      '<span class="qz-legend"><i class="lv-biet">Biết</i><i class="lv-hieu">Hiểu</i><i class="lv-vandung">Vận dụng</i></span></div>' +
      '<div class="qz-status-score"><span data-qz="done">0</span>/' + quiz.length + ' đã làm · ' +
      '<span data-qz="ok">0</span> câu đúng</div>' +
      '<div class="qz-progress"><div class="qz-progress-fill" data-qz="fill"></div></div>';
    container.appendChild(bar);

    var currentLevel = null;
    var cards = [];

    quiz.forEach(function (item, idx) {
      var lv = LEVELS[item.level] || LEVELS.biet;
      if (item.level !== currentLevel) {
        currentLevel = item.level;
        var count = quiz.filter(function (x) { return x.level === item.level; }).length;
        var h = document.createElement("h3");
        h.className = "qz-level-title " + lv.cls;
        h.textContent = lv.icon + " Mức " + lv.label.toUpperCase() + " (" + count + " câu)";
        container.appendChild(h);
      }
      var card = buildCard(item, idx, lv);
      cards.push(card);
      container.appendChild(card);
    });

    var summary = document.createElement("div");
    summary.className = "qz-summary";
    summary.style.display = "none";
    container.appendChild(summary);

    function updateStatus() {
      bar.querySelector('[data-qz="done"]').textContent = state.answered;
      bar.querySelector('[data-qz="ok"]').textContent = state.correct;
      bar.querySelector('[data-qz="fill"]').style.width = Math.round(100 * state.answered / quiz.length) + "%";
    }

    function onAnswered(idx, ok) {
      if (state.results[idx] !== undefined) return;
      state.results[idx] = ok;
      state.answered++;
      if (ok) state.correct++;
      updateStatus();
      if (typeof opts.onAnswer === "function") opts.onAnswer(idx, ok);
      if (state.answered === quiz.length) finish();
    }

    function finish() {
      var byLevel = {};
      quiz.forEach(function (q, i) {
        var k = q.level || "biet";
        byLevel[k] = byLevel[k] || { ok: 0, total: 0 };
        byLevel[k].total++;
        if (state.results[i]) byLevel[k].ok++;
      });
      var passed = state.correct >= passMark;
      var rows = Object.keys(LEVELS).filter(function (k) { return byLevel[k]; }).map(function (k) {
        return '<li class="' + LEVELS[k].cls + '">' + LEVELS[k].icon + " " + LEVELS[k].label + ": <b>" +
          byLevel[k].ok + "/" + byLevel[k].total + "</b></li>";
      }).join("");
      summary.className = "qz-summary " + (passed ? "is-pass" : "is-retry");
      summary.innerHTML =
        "<h3>" + (passed ? "🎉 Hoàn thành! " : "💪 Cố lên! ") + "Em làm đúng " + state.correct + "/" + quiz.length + " câu</h3>" +
        "<ul>" + rows + "</ul>" +
        "<p>" + (passed
          ? "Em đã đạt yêu cầu của bài học. Hãy xem lại lời giải các câu sai (nếu có) và thử “cách khác” để hiểu sâu hơn nhé!"
          : "Cần đúng từ " + passMark + "/" + quiz.length + " câu để đạt. Em đọc kỹ lời giải các câu sai rồi bấm “Làm lại” nhé!") + "</p>" +
        '<button type="button" class="qz-btn qz-retry">🔄 Làm lại từ đầu</button>';
      summary.style.display = "";
      summary.querySelector(".qz-retry").addEventListener("click", function () {
        render(container, quiz, opts);
        container.scrollIntoView({ behavior: "smooth", block: "start" });
      });
      if (typeof opts.onComplete === "function") {
        opts.onComplete({ correct: state.correct, total: quiz.length, passed: passed, firstTime: !state.finishedOnce });
      }
      state.finishedOnce = true;
    }

    /* ---------- dựng thẻ câu hỏi ---------- */
    function buildCard(item, idx, lv) {
      var type = item.type || "mcq";
      var card = document.createElement("div");
      card.className = "qz-card " + lv.cls;
      card.innerHTML =
        '<div class="qz-card-head"><span class="qz-no">Câu ' + (idx + 1) + "</span>" +
        '<span class="qz-tag ' + lv.cls + '">' + lv.label + "</span>" +
        '<span class="qz-type">' + (TYPE_LABEL[type] || "") + "</span></div>" +
        '<div class="qz-question rich-content">' + fmt(item.q || "") + "</div>" +
        '<div class="qz-body"></div>' +
        '<div class="qz-feedback" hidden></div>' +
        '<div class="qz-solution" hidden></div>';
      var body = card.querySelector(".qz-body");

      if (type === "mcq") buildMcq(body, item, idx, card);
      else if (type === "tf") buildTf(body, item, idx, card);
      else if (type === "tf4") buildTf4(body, item, idx, card);
      else if (type === "short") buildShort(body, item, idx, card);
      return card;
    }

    function showSolution(card, item, ok, correctText, extraHtml) {
      var fb = card.querySelector(".qz-feedback");
      fb.hidden = false;
      fb.className = "qz-feedback " + (ok ? "is-correct" : "is-wrong");
      fb.innerHTML = ok
        ? "✅ <b>Chính xác!</b> Em hãy so sánh cách làm của mình với lời giải bên dưới nhé."
        : "❌ <b>Chưa đúng.</b> " + (correctText ? "Đáp án đúng: <b class=\"qz-correct-ans\">" + inline(correctText) + "</b>. " : "") +
          "Đọc lời giải để biết mình sai ở đâu nhé.";
      if (extraHtml) fb.innerHTML += extraHtml;

      var sol = card.querySelector(".qz-solution");
      var html = '<div class="qz-sol-title">📘 Lời giải chi tiết</div><div class="rich-content">' + fmt(item.solution || "") + "</div>";
      if (item.note) html += '<div class="qz-sol-note"><b>⚠️ Lưu ý / Lỗi hay gặp:</b><div class="rich-content">' + fmt(item.note) + "</div></div>";
      if (item.alt) html += '<div class="qz-sol-alt"><b>💡 Cách khác:</b><div class="rich-content">' + fmt(item.alt) + "</div></div>";
      sol.innerHTML = html;
      sol.hidden = false;
      card.classList.add(ok ? "is-correct" : "is-wrong");
      upgrade(card);
    }

    function buildMcq(body, item, idx, card) {
      var wrap = document.createElement("div");
      wrap.className = "qz-options";
      (item.options || []).forEach(function (opt, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "answer-option qz-option";
        b.innerHTML = '<span class="option-letter">' + LETTERS[i] + '</span><span class="option-text rich-inline">' + inline(opt) + "</span>";
        b.addEventListener("click", function () {
          if (state.results[idx] !== undefined) return;
          var ok = i === Number(item.answer);
          var all = wrap.querySelectorAll(".qz-option");
          all.forEach(function (x) { x.disabled = true; });
          b.classList.add(ok ? "correct" : "wrong");
          if (all[Number(item.answer)]) all[Number(item.answer)].classList.add("correct");
          var correctText = LETTERS[Number(item.answer)] + ". " + ((item.options || [])[Number(item.answer)] || "");
          showSolution(card, item, ok, ok ? "" : correctText);
          onAnswered(idx, ok);
        });
        wrap.appendChild(b);
      });
      body.appendChild(wrap);
    }

    function buildTf(body, item, idx, card) {
      var wrap = document.createElement("div");
      wrap.className = "qz-tf-buttons";
      [true, false].forEach(function (val) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "qz-tf-btn";
        b.textContent = val ? "Đúng" : "Sai";
        b.addEventListener("click", function () {
          if (state.results[idx] !== undefined) return;
          var ok = val === Boolean(item.answer);
          wrap.querySelectorAll("button").forEach(function (x) { x.disabled = true; });
          b.classList.add(ok ? "correct" : "wrong");
          if (!ok) wrap.querySelectorAll("button")[item.answer ? 0 : 1].classList.add("correct");
          showSolution(card, item, ok, ok ? "" : (item.answer ? "Đúng" : "Sai"));
          onAnswered(idx, ok);
        });
        wrap.appendChild(b);
      });
      body.appendChild(wrap);
    }

    function buildTf4(body, item, idx, card) {
      var statements = item.statements || [];
      var answers = Array.isArray(item.answer) ? item.answer : [];
      var choice = new Array(statements.length);
      var table = document.createElement("div");
      table.className = "qz-tf4";
      statements.forEach(function (st, i) {
        var row = document.createElement("div");
        row.className = "qz-tf4-row";
        row.innerHTML = '<div class="qz-tf4-text rich-inline"><b>' + esc(String.fromCharCode(97 + i)) + ")</b> " + inline(st) + "</div>" +
          '<div class="qz-tf4-ctrl"><button type="button" class="qz-tf-btn sm" data-v="1">Đ</button>' +
          '<button type="button" class="qz-tf-btn sm" data-v="0">S</button></div>';
        row.querySelectorAll("button").forEach(function (b) {
          b.addEventListener("click", function () {
            if (state.results[idx] !== undefined) return;
            choice[i] = b.getAttribute("data-v") === "1";
            row.querySelectorAll("button").forEach(function (x) { x.classList.remove("chosen"); });
            b.classList.add("chosen");
            check.disabled = choice.filter(function (c) { return c !== undefined; }).length < statements.length;
          });
        });
        table.appendChild(row);
      });
      var check = document.createElement("button");
      check.type = "button";
      check.className = "qz-btn qz-check";
      check.textContent = "Kiểm tra";
      check.disabled = true;
      check.addEventListener("click", function () {
        if (state.results[idx] !== undefined) return;
        var right = 0;
        table.querySelectorAll(".qz-tf4-row").forEach(function (row, i) {
          var ok = choice[i] === Boolean(answers[i]);
          if (ok) right++;
          row.classList.add(ok ? "correct" : "wrong");
          row.querySelectorAll("button").forEach(function (x) { x.disabled = true; });
          var mark = document.createElement("span");
          mark.className = "qz-tf4-key";
          mark.textContent = answers[i] ? "→ Đúng" : "→ Sai";
          row.appendChild(mark);
        });
        check.disabled = true;
        var ok = right === statements.length;
        showSolution(card, item, ok, "", ok ? "" : " <span class='qz-partial'>(Em đúng " + right + "/" + statements.length + " ý)</span>");
        onAnswered(idx, ok);
      });
      body.appendChild(table);
      body.appendChild(check);
    }

    function buildShort(body, item, idx, card) {
      var wrap = document.createElement("div");
      wrap.className = "qz-short";
      wrap.innerHTML = '<input type="text" class="qz-input" inputmode="text" autocomplete="off" placeholder="Nhập đáp án của em">' +
        (item.unit ? '<span class="qz-unit rich-inline">' + inline(item.unit) + "</span>" : "") +
        '<button type="button" class="qz-btn qz-check">Kiểm tra</button>';
      var input = wrap.querySelector("input");
      var btn = wrap.querySelector("button");
      function submit() {
        if (state.results[idx] !== undefined) return;
        if (!input.value.trim()) { input.focus(); input.classList.add("shake"); setTimeout(function () { input.classList.remove("shake"); }, 400); return; }
        var accepted = Array.isArray(item.answer) ? item.answer : [item.answer];
        var ok = shortIsCorrect(input.value, accepted);
        input.disabled = true; btn.disabled = true;
        input.classList.add(ok ? "correct" : "wrong");
        showSolution(card, item, ok, ok ? "" : String(accepted[0]) + (item.unit ? " " + item.unit : ""));
        onAnswered(idx, ok);
      }
      btn.addEventListener("click", submit);
      input.addEventListener("keydown", function (e) { if (e.key === "Enter") submit(); });
      body.appendChild(wrap);
    }

    updateStatus();
    upgrade(container);
    return { state: state };
  }

  window.HDLGQuiz = { render: render, _shortIsCorrect: shortIsCorrect };
})();
