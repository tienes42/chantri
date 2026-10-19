/* =========================================================
   LESSON.JS — HỆ THỐNG BÀI HỌC ĐỌC HIỂU & MỞ RỘNG LINH HOẠT
   Dùng chung cho: Math, Physics, Chemistry và tất cả các môn
   API: GET /api/content/lessons/{id}
========================================================= */

const API_BASE =
  ["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000"
    ? "http://127.0.0.1:8000/api"
    : "/api";

const params = new URLSearchParams(window.location.search);
const lessonId = params.get("id");
const subject = (params.get("subject") || "math").toLowerCase();
const gradeFromUrl = params.get("grade");

/* =========================================================
   DOM ELEMENTS
========================================================= */
const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");
const lessonContent = document.getElementById("lessonContent");
const backButton = document.getElementById("backButton");
const subjectPill = document.getElementById("subjectPill");

const lessonIcon = document.getElementById("lessonIcon");
const lessonGrade = document.getElementById("lessonGrade");
const lessonTitle = document.getElementById("lessonTitle");
const lessonDescription = document.getElementById("lessonDescription");

const definition = document.getElementById("definition");
const concept = document.getElementById("concept");
const formulas = document.getElementById("formulas");
const meaning = document.getElementById("meaning");
const realLife = document.getElementById("realLife");
const contextTitle = document.getElementById("contextTitle");
const context = document.getElementById("context");
const theory = document.getElementById("theory");

const example = document.getElementById("example");
const exampleAnswer = document.getElementById("exampleAnswer");
const exampleAnswerBox = document.getElementById("exampleAnswerBox");
const toggleExampleAnswerBtn = document.getElementById("toggleExampleAnswerBtn");

const question = document.getElementById("question");
const answers = document.getElementById("answers");
const quizFeedback = document.getElementById("quizFeedback");

const application = document.getElementById("application");
const challenge = document.getElementById("challenge");
const challengeAnswer = document.getElementById("challengeAnswer");
const challengeAnswerBox = document.getElementById("challengeAnswerBox");
const challengeSolutionWrapper = document.getElementById("challengeSolutionWrapper");
const toggleChallengeAnswerBtn = document.getElementById("toggleChallengeAnswerBtn");

const extraSectionsContainer = document.getElementById("extraSectionsContainer");

const gameSection = document.getElementById("gameSection");
const gameDescription = document.getElementById("gameDescription");
const gameButton = document.getElementById("gameButton");
const noGame = document.getElementById("noGame");

const tocList = document.getElementById("tocList");
const readingProgressFill = document.getElementById("readingProgressFill");
const readingPercentText = document.getElementById("readingPercentText");

/* =========================================================
   SECTIONS
========================================================= */
const definitionSection = document.getElementById("definitionSection");
const contextSection = document.getElementById("contextSection");
const theorySection = document.getElementById("theorySection");
const conceptSection = document.getElementById("conceptSection");
const formulaSection = document.getElementById("formulaSection");
const exampleSection = document.getElementById("exampleSection");
const questionSection = document.getElementById("questionSection");
const meaningSection = document.getElementById("meaningSection");
const applicationSection = document.getElementById("applicationSection");
const realLifeSection = document.getElementById("realLifeSection");
const challengeSection = document.getElementById("challengeSection");

const subjectNames = {
  math: "Toán học",
  physics: "Vật lý",
  chemistry: "Hóa học",
  biology: "Sinh học",
  informatics: "Tin học",
  computer: "Tin học",
  english: "Tiếng Anh",
  literature: "Ngữ văn",
  history: "Lịch sử",
  geography: "Địa lý"
};

// Gán màu nhấn nhẹ theo môn học
document.body.setAttribute("data-subject", subject);
if (subjectPill) {
  subjectPill.textContent = subjectNames[subject] || "Bài học";
}

/* =========================================================
   TÙY CHỈNH CHẾ ĐỘ ĐỌC (SÁNG / ẤM / TỐI & CỠ CHỮ)
========================================================= */
const savedTheme = localStorage.getItem("hoc-de-lam-gi-reader-theme") || "light";
document.body.setAttribute("data-theme", savedTheme);
document.querySelectorAll(".theme-btn").forEach((btn) => {
  btn.classList.toggle("active", btn.dataset.setTheme === savedTheme);
  btn.addEventListener("click", () => {
    const theme = btn.dataset.setTheme;
    document.body.setAttribute("data-theme", theme);
    localStorage.setItem("hoc-de-lam-gi-reader-theme", theme);
    document.querySelectorAll(".theme-btn").forEach((b) =>
      b.classList.toggle("active", b === btn)
    );
  });
});

let currentFontSize = Number(localStorage.getItem("hoc-de-lam-gi-font-size")) || 16.5;
function applyFontSize(size) {
  currentFontSize = Math.min(21, Math.max(14, size));
  document.documentElement.style.setProperty("--reading-font-size", `${currentFontSize}px`);
  localStorage.setItem("hoc-de-lam-gi-font-size", String(currentFontSize));
}
applyFontSize(currentFontSize);

const fontDecreaseBtn = document.getElementById("fontDecreaseBtn");
const fontIncreaseBtn = document.getElementById("fontIncreaseBtn");
if (fontDecreaseBtn) {
  fontDecreaseBtn.addEventListener("click", () => applyFontSize(currentFontSize - 1));
}
if (fontIncreaseBtn) {
  fontIncreaseBtn.addEventListener("click", () => applyFontSize(currentFontSize + 1));
}

/* =========================================================
   ESCAPE HTML & BỘ ĐỊNH DẠNG VĂN BẢN DÀI TỪ BACKEND
========================================================= */
function escapeHTML(value) {
  if (value === null || value === undefined) return "";
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function formatInlineStyles(escapedStr) {
  return escapedStr
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/`([^`]+)`/g, "<code>$1</code>");
}

/**
 * Tự động trình bày nội dung dài từ Backend:
 * - Hỗ trợ chuỗi văn bản dài nhiều đoạn, gạch đầu dòng (-, *, •), danh sách số (1., 2.), tiêu đề phụ (###)
 * - Hỗ trợ cả trường hợp Backend trả về Mảng (Array) các đoạn văn
 */
function formatRichText(rawValue) {
  if (rawValue === null || rawValue === undefined) return "";

  if (Array.isArray(rawValue)) {
    return rawValue.map((item) => formatRichText(item)).join("");
  }

  const lines = String(rawValue).replace(/\r\n/g, "\n").split("\n");
  let html = "";
  let inUl = false;
  let inOl = false;

  const closeLists = () => {
    if (inUl) {
      html += "</ul>";
      inUl = false;
    }
    if (inOl) {
      html += "</ol>";
      inOl = false;
    }
  };

  lines.forEach((rawLine) => {
    const line = rawLine.trim();
    if (!line) {
      closeLists();
      return;
    }

    // Tiêu đề phụ ### hoặc ##
    if (/^#{2,4}\s+/.test(line)) {
      closeLists();
      const titleText = formatInlineStyles(escapeHTML(line.replace(/^#{2,4}\s+/, "")));
      html += `<h3>${titleText}</h3>`;
      return;
    }

    // Danh sách gạch đầu dòng (- , * , • , + )
    if (/^[-*•+]\s+/.test(line)) {
      if (inOl) {
        html += "</ol>";
        inOl = false;
      }
      if (!inUl) {
        html += "<ul>";
        inUl = true;
      }
      const itemText = formatInlineStyles(escapeHTML(line.replace(/^[-*•+]\s+/, "")));
      html += `<li>${itemText}</li>`;
      return;
    }

    // Danh sách đánh số (1. , 2. , B1: ...)
    if (/^\d+[.)]\s+/.test(line)) {
      if (inUl) {
        html += "</ul>";
        inUl = false;
      }
      if (!inOl) {
        html += "<ol>";
        inOl = true;
      }
      const itemText = formatInlineStyles(escapeHTML(line.replace(/^\d+[.)]\s+/, "")));
      html += `<li>${itemText}</li>`;
      return;
    }

    closeLists();
    html += `<p>${formatInlineStyles(escapeHTML(line))}</p>`;
  });

  closeLists();
  return html;
}

function setText(element, value) {
  if (!element) return;
  element.innerHTML = formatRichText(value);
}

function setSectionVisible(section, visible) {
  if (!section) return;
  section.style.display = visible ? "" : "none";
}

/* =========================================================
   NÚT QUAY LẠI & ẨN/HIỆN LỜI GIẢI
========================================================= */
if (backButton) {
  backButton.addEventListener("click", function () {
    window.history.back();
  });
}

if (toggleExampleAnswerBtn && exampleAnswerBox) {
  toggleExampleAnswerBtn.addEventListener("click", () => {
    const isHidden = exampleAnswerBox.classList.toggle("hidden");
    toggleExampleAnswerBtn.setAttribute("aria-expanded", String(!isHidden));
  });
}

if (toggleChallengeAnswerBtn && challengeAnswerBox) {
  toggleChallengeAnswerBtn.addEventListener("click", () => {
    const isHidden = challengeAnswerBox.classList.toggle("hidden");
    toggleChallengeAnswerBtn.setAttribute("aria-expanded", String(!isHidden));
    toggleChallengeAnswerBtn.textContent = isHidden
      ? "🔍 Xem gợi ý / Đáp án thử thách"
      : "🔼 Thu gọn gợi ý / Đáp án";
  });
}

/* =========================================================
   ERROR & LOADING STATES
========================================================= */
function showError(message) {
  if (loading) loading.style.display = "none";
  if (lessonContent) lessonContent.classList.add("hidden");
  if (errorBox) {
    errorBox.textContent = message;
    errorBox.style.display = "block";
  }
}

function finishLoading() {
  if (loading) loading.style.display = "none";
  if (errorBox) errorBox.style.display = "none";
  if (lessonContent) lessonContent.classList.remove("hidden");
}

/* =========================================================
   RENDER FORMULAS
========================================================= */
function renderFormulas(data, singleFormula) {
  if (!formulas) return;

  let formulaData = data;
  if ((!Array.isArray(formulaData) || formulaData.length === 0) && singleFormula) {
    formulaData = [singleFormula];
  }

  if (!Array.isArray(formulaData) || formulaData.length === 0) {
    formulas.innerHTML = `<p>Chưa có công thức.</p>`;
    setSectionVisible(formulaSection, false);
    return;
  }

  setSectionVisible(formulaSection, true);
  let html = "";

  formulaData.forEach(function (group) {
    if (group && typeof group === "object" && group.category && Array.isArray(group.items)) {
      html += `
        <div class="formula-category">
          <h3 class="formula-category-title">${escapeHTML(group.category)}</h3>
          <div class="formula-category-items">
      `;
      group.items.forEach(function (item) {
        if (typeof item === "string") {
          html += `
            <div class="formula-item">
              <div class="formula-expression">${escapeHTML(item)}</div>
            </div>
          `;
          return;
        }
        html += `
          <div class="formula-item">
            ${item.name ? `<div class="formula-name">${escapeHTML(item.name)}</div>` : ""}
            ${item.formula ? `<div class="formula-expression">${escapeHTML(item.formula)}</div>` : ""}
            ${item.note ? `<div class="formula-note">${formatRichText(item.note)}</div>` : ""}
          </div>
        `;
      });
      html += `</div></div>`;
      return;
    }

    if (group && typeof group === "object") {
      html += `
        <div class="formula-item">
          ${group.name ? `<div class="formula-name">${escapeHTML(group.name)}</div>` : ""}
          ${group.formula ? `<div class="formula-expression">${escapeHTML(group.formula)}</div>` : ""}
          ${group.note ? `<div class="formula-note">${formatRichText(group.note)}</div>` : ""}
        </div>
      `;
      return;
    }

    html += `
      <div class="formula-item">
        <div class="formula-expression">${escapeHTML(group)}</div>
      </div>
    `;
  });

  formulas.innerHTML = html;
}

/* =========================================================
   RENDER ANSWERS (TRẮC NGHIỆM TƯƠNG TÁC)
========================================================= */
function renderAnswers(answerList, correctIndex) {
  if (!answers) return;
  answers.innerHTML = "";
  if (quizFeedback) {
    quizFeedback.className = "quiz-feedback hidden";
    quizFeedback.textContent = "";
  }

  if (!Array.isArray(answerList) || answerList.length === 0) {
    setSectionVisible(questionSection, false);
    return;
  }

  setSectionVisible(questionSection, true);
  const letters = ["A", "B", "C", "D", "E", "F"];

  answerList.forEach(function (answer, index) {
    const option = document.createElement("button");
    option.type = "button";
    option.className = "answer-option";

    const letter = letters[index] || String(index + 1);
    option.innerHTML = `
      <span class="option-letter">${letter}</span>
      <span>${escapeHTML(answer)}</span>
    `;

    option.addEventListener("click", function () {
      const allOptions = answers.querySelectorAll(".answer-option");
      allOptions.forEach((btn) => btn.classList.remove("correct", "wrong"));

      const isCorrect = Number(index) === Number(correctIndex);
      if (isCorrect) {
        option.classList.add("correct");
        if (quizFeedback) {
          quizFeedback.textContent = "✅ Chính xác! Bạn đã nắm vững kiến thức phần này.";
          quizFeedback.className = "quiz-feedback is-correct";
        }
      } else {
        option.classList.add("wrong");
        if (allOptions[Number(correctIndex)]) {
          allOptions[Number(correctIndex)].classList.add("correct");
        }
        if (quizFeedback) {
          quizFeedback.textContent = "💡 Chưa chính xác. Hãy xem đáp án được tô xanh để ghi nhớ nhé!";
          quizFeedback.className = "quiz-feedback is-wrong";
        }
      }
    });

    answers.appendChild(option);
  });
}

/* =========================================================
   HỖ TRỢ THÊM CÁC MỤC MỚI TÙY Ý TỪ BACKEND (extra_sections / sections)
========================================================= */
function renderExtraBackendSections(lesson) {
  if (!extraSectionsContainer) return;
  extraSectionsContainer.innerHTML = "";

  const extraList = Array.isArray(lesson.extra_sections)
    ? lesson.extra_sections
    : Array.isArray(lesson.sections)
      ? lesson.sections
      : [];

  extraList.forEach((sec, idx) => {
    if (!sec || (!sec.content && !sec.body && !sec.text)) return;
    const secEl = document.createElement("section");
    secEl.className = "lesson-section";
    secEl.id = `extraSection_${idx}`;
    const title = sec.title || sec.heading || `Phần mở rộng ${idx + 1}`;
    secEl.setAttribute("data-toc", title);

    secEl.innerHTML = `
      <div class="section-head">
        <span class="section-badge">+${idx + 1}</span>
        <h2 class="section-title">📌 ${escapeHTML(title)}</h2>
      </div>
      <div class="section-content theory-box rich-content">
        ${formatRichText(sec.content || sec.body || sec.text)}
      </div>
    `;
    extraSectionsContainer.appendChild(secEl);
  });
}

/* =========================================================
   TỰ ĐỘNG TẠO MỤC LỤC BÊN TRÁI & ĐÁNH SỐ LẠI CÁC MỤC HIỂN THỊ
========================================================= */
function buildTableOfContents() {
  if (!tocList) return;
  tocList.innerHTML = "";

  const allSections = Array.from(
    document.querySelectorAll(".lesson-article .lesson-section, .lesson-article .game-section")
  ).filter((sec) => sec.style.display !== "none");

  allSections.forEach((sec, idx) => {
    const badge = sec.querySelector(".section-badge");
    if (badge) {
      badge.textContent = String(idx + 1).padStart(2, "0");
    }

    const tocTitle = sec.getAttribute("data-toc") || sec.querySelector(".section-title")?.textContent || `Mục ${idx + 1}`;
    const link = document.createElement("a");
    link.href = `#${sec.id}`;
    link.className = "toc-link";
    link.textContent = `${idx + 1}. ${tocTitle}`;
    tocList.appendChild(link);
  });
}

/* =========================================================
   RENDER GAME
========================================================= */
function renderGame(lesson) {
  if (!gameDescription || !gameButton || !noGame) return;

  if (!lesson.game_title && !lesson.game_description && !lesson.game_type) {
    gameDescription.textContent = "";
    gameButton.style.display = "none";
    noGame.classList.remove("hidden");
    return;
  }

  gameDescription.textContent =
    lesson.game_description ||
    lesson.game_title ||
    "Hãy áp dụng kiến thức vừa học vào thử thách thực tế.";

  if (lesson.game_type) {
    gameButton.style.display = "inline-block";
    gameButton.textContent = "🚀 Bắt đầu trải nghiệm";
    gameButton.onclick = function () {
      window.location.href = `games/${encodeURIComponent(lesson.game_type)}.html?lesson_id=${lesson.id}`;
    };
    noGame.classList.add("hidden");
  } else {
    gameButton.style.display = "none";
    noGame.classList.remove("hidden");
  }
}

/* =========================================================
   RENDER LESSON
========================================================= */
function renderLesson(lesson) {
  if (lessonIcon) lessonIcon.textContent = lesson.icon || "📚";
  if (lessonGrade) {
    const g = lesson.grade || gradeFromUrl;
    lessonGrade.textContent = g ? `Lớp ${g}` : "Bài học";
  }
  if (lessonTitle) {
    lessonTitle.textContent = lesson.title || "Bài học";
    document.title = `${lesson.title || "Bài học"} - HỌC ĐỂ LÀM GÌ`;
  }
  if (lessonDescription) {
    lessonDescription.textContent = lesson.description || "";
  }

  // 1. Definition
  if (lesson.definition) {
    setText(definition, lesson.definition);
    setSectionVisible(definitionSection, true);
  } else {
    setSectionVisible(definitionSection, false);
  }

  // 2. Context
  if (lesson.context || lesson.context_title) {
    if (contextTitle) contextTitle.textContent = lesson.context_title || "Bối cảnh thực tế";
    setText(context, lesson.context || "");
    setSectionVisible(contextSection, true);
  } else {
    setSectionVisible(contextSection, false);
  }

  // 3. Theory
  if (lesson.theory) {
    setText(theory, lesson.theory);
    setSectionVisible(theorySection, true);
  } else {
    setSectionVisible(theorySection, false);
  }

  // 4. Concept
  if (lesson.concept) {
    setText(concept, lesson.concept);
    setSectionVisible(conceptSection, true);
  } else {
    setSectionVisible(conceptSection, false);
  }

  // 5. Formulas
  renderFormulas(lesson.formulas, lesson.formula);

  // 6. Example
  if (lesson.example || lesson.example_answer) {
    setText(example, lesson.example || "");
    setText(exampleAnswer, lesson.example_answer || "");
    setSectionVisible(exampleSection, true);
  } else {
    setSectionVisible(exampleSection, false);
  }

  // 7. Question
  if (lesson.question) {
    setText(question, lesson.question);
    renderAnswers(lesson.answers, lesson.correct);
  } else {
    setSectionVisible(questionSection, false);
  }

  // 8. Meaning
  if (lesson.meaning) {
    setText(meaning, lesson.meaning);
    setSectionVisible(meaningSection, true);
  } else {
    setSectionVisible(meaningSection, false);
  }

  // 9. Application
  if (lesson.application) {
    setText(application, lesson.application);
    setSectionVisible(applicationSection, true);
  } else {
    setSectionVisible(applicationSection, false);
  }

  // 10. Real Life
  if (lesson.real_life) {
    setText(realLife, lesson.real_life);
    setSectionVisible(realLifeSection, true);
  } else {
    setSectionVisible(realLifeSection, false);
  }

  // 11. Challenge
  if (lesson.challenge || lesson.challenge_answer) {
    setText(challenge, lesson.challenge || "");
    setText(challengeAnswer, lesson.challenge_answer || "");
    if (challengeSolutionWrapper) {
      challengeSolutionWrapper.style.display = lesson.challenge_answer ? "" : "none";
    }
    setSectionVisible(challengeSection, true);
  } else {
    setSectionVisible(challengeSection, false);
  }

  // Các mục mở rộng nếu sau này Backend thêm vào
  renderExtraBackendSections(lesson);

  // 12. Game
  renderGame(lesson);

  finishLoading();
  buildTableOfContents();
  updateReadingProgress();
}

/* =========================================================
   THEO DÕI TIẾN ĐỘ ĐỌC BÀI KHI CUỘN TRANG
========================================================= */
function updateReadingProgress() {
  const docEl = document.documentElement;
  const scrollTop = window.scrollY || docEl.scrollTop;
  const scrollHeight = docEl.scrollHeight - docEl.clientHeight;
  const percent = scrollHeight > 0 ? Math.min(100, Math.round((scrollTop / scrollHeight) * 100)) : 100;

  if (readingProgressFill) readingProgressFill.style.width = `${percent}%`;
  if (readingPercentText) readingPercentText.textContent = `${percent}%`;

  // Tô sáng mục đang đọc trên Mục lục bên trái
  const links = document.querySelectorAll(".toc-link");
  let activeIndex = 0;
  links.forEach((link, idx) => {
    const targetId = link.getAttribute("href")?.slice(1);
    const targetEl = targetId ? document.getElementById(targetId) : null;
    if (targetEl && targetEl.getBoundingClientRect().top <= 140) {
      activeIndex = idx;
    }
  });
  links.forEach((link, idx) => link.classList.toggle("active", idx === activeIndex));
}

window.addEventListener("scroll", updateReadingProgress, { passive: true });

/* =========================================================
   LOAD LESSON FROM API
========================================================= */
async function loadLesson() {
  if (!lessonId) {
    showError("Không tìm thấy ID bài học. Hãy mở bài học từ danh sách bài học.");
    return;
  }

  const url = `${API_BASE}/content/lessons/${encodeURIComponent(lessonId)}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Không thể tải bài học. HTTP ${response.status}`);
    }

    const lesson = await response.json();
    if (!lesson || lesson.id === undefined || lesson.id === null) {
      throw new Error("API trả về bài học nhưng không có ID.");
    }

    renderLesson(lesson);
  } catch (error) {
    console.error("LOAD LESSON ERROR:", error);
    showError(error.message || "Không thể tải bài học.");
  }
}

loadLesson();