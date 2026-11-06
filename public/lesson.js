/* =========================================================
   LESSON.JS — SÁCH HỌC VIỆN NỔI 2.5D & ĐỌC HIỂU CHUYÊN SÂU
   Dùng chung cho: Math, Physics, Chemistry và các môn khác
   Hỗ trợ:
   - KaTeX 0.16.11 + Offline Math/Chem Renderer (window.HDLGMath)
   - Sơ đồ tư duy tổng quan 2.5D tương tác (#mindmapSection)
   - Cấu trúc 3 cấp: Lớp ➔ Chương/Chủ đề ➔ Từng Bài học
     (Breadcrumb Chương, Sidebar Danh sách bài trong Chương, Điều hướng Bài trước / Bài tiếp theo)
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
const topicFromUrl = params.get("topic");
const subIndexFromUrl = params.get("sub") !== null ? parseInt(params.get("sub"), 10) : null;

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
const lessonChapterBadge = document.getElementById("lessonChapterBadge");
const lessonTitle = document.getElementById("lessonTitle");
const lessonDescription = document.getElementById("lessonDescription");

const chapterLessonsCard = document.getElementById("chapterLessonsCard");
const chapterSidebarTitle = document.getElementById("chapterSidebarTitle");
const chapterSidebarProgress = document.getElementById("chapterSidebarProgress");
const chapterLessonsList = document.getElementById("chapterLessonsList");
const chapterNavFooter = document.getElementById("chapterNavFooter");

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

const gameDescription = document.getElementById("gameDescription");
const gameButton = document.getElementById("gameButton");
const noGame = document.getElementById("noGame");

const tocList = document.getElementById("tocList");
const readingProgressFill = document.getElementById("readingProgressFill");
const readingPercentText = document.getElementById("readingPercentText");

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
const mindmapSection = document.getElementById("mindmapSection");

// Chương trình SGK mới: Yêu cầu cần đạt + bộ câu hỏi 3 mức độ
const requirementsSection = document.getElementById("requirementsSection");
const requirementsList = document.getElementById("requirements");
const sgkRef = document.getElementById("sgkRef");
const quizSet = document.getElementById("quizSet");
const singleQuestionBox = document.getElementById("singleQuestionBox");

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

const subjectGradePages = {
  math: "math-grade.html",
  physics: "physics-grade.html",
  chemistry: "chemistry-knowledge.html"
};

document.body.setAttribute("data-subject", subject);
if (subjectPill) {
  subjectPill.textContent = subjectNames[subject] || "Bài học";
}

/* =========================================================
   TỰ ĐỘNG CẮT & TÁCH NỀN ICON 2.5D THEO MÔN HỌC
========================================================= */
function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function initLesson25DSprites() {
  const sheetMap = {
    math: "assets/math-icons.webp",
    physics: "assets/physics-icons.webp",
    chemistry: "assets/chemistry-icons.webp"
  };
  const sheetUrl = sheetMap[subject] || "assets/math-icons.webp";

  try {
    const img = await loadImg(sheetUrl);
    const cellW = img.naturalWidth / 4;
    const cellH = img.naturalHeight / 4;
    const size = 220;
    const c = document.createElement("canvas");
    c.width = size;
    c.height = size;
    const ctx = c.getContext("2d");
    const sprites = [];

    for (let row = 0; row < 4; row++) {
      for (let col = 0; col < 4; col++) {
        ctx.clearRect(0, 0, size, size);
        ctx.drawImage(img, col * cellW, row * cellH, cellW, cellH, 0, 0, size, size);
        sprites.push(c.toDataURL("image/png"));
      }
    }

    const applySprite = (selector, idx) => {
      if (!sprites[idx]) return;
      document.querySelectorAll(selector).forEach((el) => {
        el.style.backgroundImage = `url("${sprites[idx]}")`;
        el.querySelectorAll("span").forEach((s) => { s.style.display = "none"; });
      });
    };

    applySprite('[data-sprite="core"]', 0);
    applySprite('[data-sprite="trophy"]', 7);
    applySprite('[data-prop="p1"]', 12);
    applySprite('[data-prop="p2"]', 13);
    applySprite('[data-prop="p3"]', 14);
    applySprite('[data-prop="p4"]', 15);
  } catch (e) {
    console.info("Sử dụng biểu tượng mặc định:", e);
  }
}
initLesson25DSprites();

// Hiệu ứng Parallax nhẹ cho 4 khí cụ 2.5D ở rìa màn hình
const parallaxBg = document.getElementById("parallaxBg");
const parallaxRelics = document.getElementById("parallaxRelics");
window.addEventListener("mousemove", (e) => {
  const nx = e.clientX / window.innerWidth - 0.5;
  const ny = e.clientY / window.innerHeight - 0.5;
  if (parallaxBg) {
    parallaxBg.style.transform = `translate(${nx * 12}px,${ny * 8}px) scale(1.04)`;
  }
  if (parallaxRelics) {
    parallaxRelics.style.transform = `translate(${nx * -22}px,${ny * -14}px)`;
  }
});

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
   ESCAPE HTML & BỘ DỰNG CÔNG THỨC TOÁN / LÝ / HÓA (KaTeX + OFFLINE)
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

const LATEX_SYMBOLS = {
  "\\alpha": "α", "\\beta": "β", "\\gamma": "γ", "\\delta": "δ", "\\epsilon": "ε", "\\varepsilon": "ε",
  "\\zeta": "ζ", "\\eta": "η", "\\theta": "θ", "\\vartheta": "ϑ", "\\iota": "ι", "\\kappa": "κ",
  "\\lambda": "λ", "\\mu": "μ", "\\nu": "ν", "\\xi": "ξ", "\\pi": "π", "\\rho": "ρ",
  "\\sigma": "σ", "\\tau": "τ", "\\upsilon": "υ", "\\phi": "φ", "\\varphi": "φ", "\\chi": "χ",
  "\\psi": "ψ", "\\omega": "ω",
  "\\Gamma": "Γ", "\\Delta": "Δ", "\\Theta": "Θ", "\\Lambda": "Λ", "\\Xi": "Ξ", "\\Pi": "Π",
  "\\Sigma": "Σ", "\\Phi": "Φ", "\\Psi": "Ψ", "\\Omega": "Ω",
  "\\cdot": "·", "\\times": "×", "\\div": "÷", "\\pm": "±", "\\mp": "∓", "\\ast": "∗",
  "\\le": "≤", "\\leq": "≤", "\\ge": "≥", "\\geq": "≥", "\\ne": "≠", "\\neq": "≠",
  "\\approx": "≈", "\\equiv": "≡", "\\sim": "∼", "\\simeq": "≃", "\\cong": "≅", "\\propto": "∝",
  "\\infty": "∞", "\\partial": "∂", "\\nabla": "∇", "\\forall": "∀", "\\exists": "∃", "\\nexists": "∄",
  "\\in": "∈", "\\notin": "∉", "\\ni": "∋", "\\subset": "⊂", "\\supset": "⊃",
  "\\subseteq": "⊆", "\\supseteq": "⊇", "\\cup": "∪", "\\cap": "∩", "\\setminus": "∖",
  "\\emptyset": "∅", "\\varnothing": "∅",
  "\\to": "→", "\\rightarrow": "→", "\\leftarrow": "←", "\\leftrightarrow": "↔",
  "\\Rightarrow": "⇒", "\\Leftarrow": "⇐", "\\Leftrightarrow": "⇔", "\\iff": "⇔", "\\implies": "⇒",
  "\\mapsto": "↦", "\\uparrow": "↑", "\\downarrow": "↓", "\\upharpoonright": "↑",
  "\\perp": "⊥", "\\parallel": "∥", "\\angle": "∠", "\\widehat": "", "\\triangle": "△",
  "\\circ": "°", "\\degree": "°", "\\prime": "′", "\\dots": "…", "\\ldots": "…", "\\cdots": "⋯",
  "\\quad": " ", "\\qquad": "  ", "\\,": " ", "\\;": " ", "\\:": " ", "\\!": "", "\\ ": " ",
  "\\left": "", "\\right": "", "\\bigl": "", "\\bigr": "", "\\Bigl": "", "\\Bigr": "",
  "\\displaystyle": "", "\\textstyle": "",
  "\\sin": "sin", "\\cos": "cos", "\\tan": "tan", "\\cot": "cot", "\\arcsin": "arcsin", "\\arccos": "arccos", "\\arctan": "arctan",
  "\\ln": "ln", "\\log": "log", "\\lg": "lg", "\\lim": "lim", "\\max": "max", "\\min": "min", "\\gcd": "ƯCLN", "\\lcm": "BCNN",
  "\\int": "∫", "\\oint": "∮", "\\sum": "∑", "\\prod": "∏"
};

const MATHBB_MAP = { N: "ℕ", Z: "ℤ", Q: "ℚ", R: "ℝ", C: "ℂ", P: "ℙ" };

function takeBraced(s, pos) {
  while (pos < s.length && s[pos] === " ") pos++;
  if (s[pos] !== "{") {
    if (s[pos] === "\\" && pos + 1 < s.length) {
      let m = s.slice(pos).match(/^\\[a-zA-Z]+/);
      if (m) return [m[0], pos + m[0].length];
    }
    return [s[pos] || "", pos + 1];
  }
  let depth = 0, i = pos;
  for (; i < s.length; i++) {
    if (s[i] === "\\" && i + 1 < s.length) { i++; continue; }
    if (s[i] === "{") depth++;
    else if (s[i] === "}") {
      depth--;
      if (depth === 0) return [s.slice(pos + 1, i), i + 1];
    }
  }
  return [s.slice(pos + 1), s.length];
}

function normalizeKatexInput(tex) {
  return String(tex || "")
    .replace(/\\[,;:!]\s*\^/g, "^")
    .replace(/\\[,;:!]\s*_/g, "_")
    .replace(/(\s)\^/g, "$1{}^")
    .replace(/^(\s*)\^/, "$1{}^")
    .replace(/([({\[=+\-*/<>|,;:])\s*\^/g, "$1{}^")
    .replace(/([({\[=+\-*/<>|,;:])\s*_/g, "$1{}_")
    .replace(/\\degree\b/g, "^\\circ");
}

function renderLatexOffline(tex) {
  let s = String(tex).trim();
  if (!s) return "";

  s = s.replace(/\\begin\{(cases|aligned|array|matrix|pmatrix|bmatrix|vmatrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
    body = body.replace(/^\s*\{[^}]*\}/, "");
    const rows = body.split(/\\\\/).map((r) => r.trim()).filter(Boolean);
    const renderedRows = rows.map((r) => {
      const cells = r.split("&").map((c) => renderLatexOffline(c.trim()));
      return `<span class="m-row">${cells.map((c) => `<span class="m-cell">${c}</span>`).join("")}</span>`;
    }).join("");
    if (env === "cases") return `<span class="m-cases">{<span class="m-rows">${renderedRows}</span></span>`;
    const lbr = env === "pmatrix" ? "(" : env === "bmatrix" ? "[" : env === "vmatrix" ? "|" : "";
    const rbr = env === "pmatrix" ? ")" : env === "bmatrix" ? "]" : env === "vmatrix" ? "|" : "";
    return `<span class="m-matrix">${lbr}<span class="m-rows">${renderedRows}</span>${rbr}</span>`;
  });

  let out = "", i = 0;
  while (i < s.length) {
    if (s[i] === "\\") {
      const rest = s.slice(i);
      let m = rest.match(/^\\(d?frac|tfrac)\b/);
      if (m) {
        let [num, p1] = takeBraced(s, i + m[0].length);
        let [den, p2] = takeBraced(s, p1);
        out += `<span class="m-frac"><span class="m-num">${renderLatexOffline(num)}</span><span class="m-den">${renderLatexOffline(den)}</span></span>`;
        i = p2; continue;
      }
      m = rest.match(/^\\sqrt\[([^\]]+)\]/);
      if (m) {
        let [rad, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-sqrt"><sup class="m-root">${renderLatexOffline(m[1])}</sup>√<span class="m-rad">${renderLatexOffline(rad)}</span></span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\sqrt\b/);
      if (m) {
        let [rad, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-sqrt">√<span class="m-rad">${renderLatexOffline(rad)}</span></span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\(overrightarrow|vec|overline|bar|widehat|hat|tilde)\b/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        const cls = (m[1] === "overrightarrow" || m[1] === "vec") ? "m-vec" : (m[1] === "widehat" || m[1] === "hat") ? "m-hat" : "m-bar";
        out += `<span class="${cls}">${renderLatexOffline(arg)}</span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\(text|mathrm|textbf|mathbf|mathit|operatorname)\b/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        const tag = (m[1] === "textbf" || m[1] === "mathbf") ? "strong" : "span";
        out += `<${tag} class="m-text">${renderLatexOffline(arg)}</${tag}>`;
        i = p1; continue;
      }
      m = rest.match(/^\\mathbb\b/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-bb">${MATHBB_MAP[arg.trim()] || escapeHTML(arg)}</span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\(overset|stackrel)\b/);
      if (m) {
        let [top, p1] = takeBraced(s, i + m[0].length);
        let [bot, p2] = takeBraced(s, p1);
        out += `<span class="m-over"><span class="m-top">${renderLatexOffline(top)}</span><span class="m-bot">${renderLatexOffline(bot)}</span></span>`;
        i = p2; continue;
      }
      m = rest.match(/^\\(\|[a-zA-Z]+|[^a-zA-Z])/);
      if (m) {
        const tok = m[0];
        if (tok === "\\{" || tok === "\\}") { out += tok.slice(1); i += 2; continue; }
        if (tok === "\\%") { out += "%"; i += 2; continue; }
        if (Object.prototype.hasOwnProperty.call(LATEX_SYMBOLS, tok)) {
          out += LATEX_SYMBOLS[tok];
          i += tok.length;
          if (s[i] === " " && /^\\[a-zA-Z]+$/.test(tok)) i++;
          continue;
        }
        out += escapeHTML(tok.slice(1));
        i += tok.length;
        continue;
      }
    }
    if (s[i] === "^" || s[i] === "_") {
      const tag = s[i] === "^" ? "sup" : "sub";
      let [arg, p1] = takeBraced(s, i + 1);
      out += `<${tag}>${renderLatexOffline(arg)}</${tag}>`;
      i = p1; continue;
    }
    if (s[i] === "{") {
      let [arg, p1] = takeBraced(s, i);
      out += renderLatexOffline(arg);
      i = p1; continue;
    }
    if (s[i] === "}") { i++; continue; }
    if (s[i] === "-" && (i === 0 || /[\s({\[=+,;<>]/.test(s[i - 1]))) {
      out += "−"; i++; continue;
    }
    out += escapeHTML(s[i]);
    i++;
  }
  return out;
}

function renderMathToken(tex, displayMode) {
  const clean = normalizeKatexInput(String(tex).trim());
  if (!clean) return "";
  if (window.katex && typeof window.katex.renderToString === "function") {
    try {
      return window.katex.renderToString(clean, { throwOnError: false, displayMode: !!displayMode, strict: false });
    } catch (_) {}
  }
  const attr = escapeHTML(clean);
  const tag = displayMode ? "div" : "span";
  return `<${tag} class="m-math${displayMode ? " m-block" : ""}" data-latex="${attr}">${renderLatexOffline(clean)}</${tag}>`;
}

function upgradeKatex(root) {
  if (!window.katex || typeof window.katex.renderToString !== "function") return;
  (root || document).querySelectorAll(".m-math[data-latex]").forEach((el) => {
    const tex = normalizeKatexInput(el.getAttribute("data-latex"));
    if (!tex) return;
    try {
      el.innerHTML = window.katex.renderToString(tex, {
        throwOnError: false,
        displayMode: el.classList.contains("m-block"),
        strict: false
      });
      el.removeAttribute("data-latex");
    } catch (_) {}
  });
}
window.addEventListener("load", () => upgradeKatex(document));

function formatInlineStyles(rawStr) {
  if (!rawStr) return "";
  const stash = [];
  const put = (html) => { const id = `\u0000M${stash.length}\u0000`; stash.push(html); return id; };

  let s = String(rawStr)
    .replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => put(renderMathToken(m, true)))
    .replace(/\\\[([\s\S]+?)\\\]/g, (_, m) => put(renderMathToken(m, true)))
    .replace(/\\\(([\s\S]+?)\\\)/g, (_, m) => put(renderMathToken(m, false)))
    .replace(/\$([^$\n]+?)\$/g, (_, m) => put(renderMathToken(m, false)));

  s = s.replace(/`([^`]+)`/g, (_, c) => put(`<code>${escapeHTML(c)}</code>`));

  if (/\\(d?frac|sqrt|overrightarrow|vec|widehat|triangle|angle|cdot|times|div|pm|le|leq|ge|geq|ne|neq|approx|equiv|infty|in|notin|subset|subseteq|cup|cap|emptyset|alpha|beta|gamma|delta|Delta|pi|omega|Omega|sigma|lambda|mu|theta|sin|cos|tan|cot|log|ln|lim|sum|int|mathbb|mathrm|text)\b/.test(s)) {
    s = s.replace(/((?:\\[a-zA-Z]+(?:\{[^}]*\})*|\b[a-zA-Z0-9]+\s*[_^]\s*(?:\{[^}]+\}|[a-zA-Z0-9+-]+))(?:[\s+\-*/=<>≤≥≠≈·×÷,()0-9a-zA-Z\\_{}^]*))/g, (m) => {
      if (m.indexOf("\u0000") !== -1) return m;
      return put(renderMathToken(m, false));
    });
  }

  s = escapeHTML(s)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\b([A-Za-z][a-z]?\d*(?:\([A-Za-z0-9]+\)\d*)*)\^(\d*[+-])/g, "$1<sup>$2</sup>")
    .replace(/(\([A-Za-z]{1,3}\d*\))(\d+)/g, "$1<sub>$2</sub>")
    .replace(/\b((?:[A-Z][a-z]?\d*)+)\b/g, (word) => {
      if (!/\d/.test(word)) return word;
      if (!/^(?:H|He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca|Sc|Ti|V|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Ag|Cd|In|Sn|Sb|Te|I|Xe|Cs|Ba|Au|Hg|Pb|Bi|Cr|Mn|Cu|Zn|Fe|Al|Mg|Ca|Na|K|Ba|Ag|H|C|N|O|S|P|Cl|Br|I|F|\d)+$/.test(word)) return word;
      return word.replace(/([A-Za-z])(\d+)/g, "$1<sub>$2</sub>");
    });

  return s.replace(/\u0000M(\d+)\u0000/g, (_, idx) => stash[Number(idx)] || "");
}

function renderMathText(str, displayMode) {
  if (str === null || str === undefined) return "";
  const raw = String(str).trim();
  if (!raw) return "";
  if (raw.includes("$") || /\\\[|\\\(/.test(raw)) return formatInlineStyles(raw);
  if (/\\[a-zA-Z]+|[_^]\s*\{|[a-zA-Z0-9]\s*\^\s*[0-9a-zA-Z+-]/.test(raw)) {
    return renderMathToken(raw, !!displayMode);
  }
  return formatInlineStyles(raw);
}

window.HDLGMath = {
  inline: formatInlineStyles,
  formula: renderMathText,
  upgrade: upgradeKatex
};

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

    if (/^#{2,4}\s+/.test(line)) {
      closeLists();
      const titleText = formatInlineStyles(line.replace(/^#{2,4}\s+/, ""));
      html += `<h3>${titleText}</h3>`;
      return;
    }

    if (/^[-*•+]\s+/.test(line)) {
      if (inOl) {
        html += "</ol>";
        inOl = false;
      }
      if (!inUl) {
        html += "<ul>";
        inUl = true;
      }
      const itemText = formatInlineStyles(line.replace(/^[-*•+]\s+/, ""));
      html += `<li>${itemText}</li>`;
      return;
    }

    if (/^\d+[.)]\s+/.test(line)) {
      if (inUl) {
        html += "</ul>";
        inUl = false;
      }
      if (!inOl) {
        html += "<ol>";
        inOl = true;
      }
      const itemText = formatInlineStyles(line.replace(/^\d+[.)]\s+/, ""));
      html += `<li>${itemText}</li>`;
      return;
    }

    closeLists();
    html += `<p>${formatInlineStyles(line)}</p>`;
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
    const page = subjectGradePages[subject];
    const g = gradeFromUrl || (currentLessonData && currentLessonData.grade);
    const tp = topicFromUrl || (currentLessonData && currentLessonData.topic);
    if (page && g) {
      window.location.href = `${page}?grade=${encodeURIComponent(g)}${tp ? `&topic=${encodeURIComponent(tp)}` : ""}`;
      return;
    }
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
          <h3 class="formula-category-title">${formatInlineStyles(group.category)}</h3>
          <div class="formula-category-items">
      `;
      group.items.forEach(function (item) {
        if (typeof item === "string") {
          html += `
            <div class="formula-item">
              <div class="formula-expression">${renderMathText(item, true)}</div>
            </div>
          `;
          return;
        }
        html += `
          <div class="formula-item">
            ${item.name ? `<div class="formula-name">${formatInlineStyles(item.name)}</div>` : ""}
            ${item.formula ? `<div class="formula-expression">${renderMathText(item.formula, true)}</div>` : ""}
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
          ${group.name ? `<div class="formula-name">${formatInlineStyles(group.name)}</div>` : ""}
          ${group.formula ? `<div class="formula-expression">${renderMathText(group.formula, true)}</div>` : ""}
          ${group.note ? `<div class="formula-note">${formatRichText(group.note)}</div>` : ""}
        </div>
      `;
      return;
    }

    html += `
      <div class="formula-item">
        <div class="formula-expression">${renderMathText(group, true)}</div>
      </div>
    `;
  });

  formulas.innerHTML = html;
}

/* =========================================================
   RENDER ANSWERS (TRẮC NGHIỆM 2.5D TƯƠNG TÁC)
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
      <span>${formatInlineStyles(answer)}</span>
    `;

    option.addEventListener("click", function () {
      const allOptions = answers.querySelectorAll(".answer-option");
      allOptions.forEach((btn) => btn.classList.remove("correct", "wrong"));

      const isCorrect = Number(index) === Number(correctIndex);
      handleQuizReward(isCorrect);
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
          quizFeedback.textContent = "💡 Chưa chính xác. Hãy xem đáp án đúng được tô xanh để ghi nhớ nhé!";
          quizFeedback.className = "quiz-feedback is-wrong";
        }
      }
    });

    answers.appendChild(option);
  });
}

/* =========================================================
   HỖ TRỢ THÊM MỤC MỚI TỪ BACKEND (extra_sections / sections)
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
    secEl.className = "lesson-section card-25d";
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
   SƠ ĐỒ TƯ DUY TỔNG QUAN 2.5D (TỰ ĐỘNG TỔNG HỢP TỪ BÀI HỌC)
========================================================= */
const mindmapState = {
  zoom: 1,
  panX: 0,
  panY: 0,
  expandedAll: false,
  activeBranchId: null,
  branches: []
};

function stripMarkdownPlain(str) {
  return String(str || "")
    .replace(/\*\*(.+?)\*\*/g, "$1")
    .replace(/^#{1,4}\s+/gm, "")
    .replace(/^[-*•+]\s+/gm, "")
    .trim();
}

function truncateMindmapText(str, maxLen) {
  const s = String(str || "").trim();
  if (s.length <= maxLen) return s;
  const idx = s.indexOf("$");
  if (idx !== -1) {
    const dollarMatches = s.match(/\$/g);
    if (dollarMatches && dollarMatches.length % 2 === 0 && s.length <= maxLen + 35) {
      return s;
    }
  }
  let cut = s.slice(0, maxLen);
  const dCount = (cut.match(/\$/g) || []).length;
  if (dCount % 2 === 1) {
    const nextDollar = s.indexOf("$", maxLen);
    if (nextDollar !== -1 && nextDollar < maxLen + 45) {
      cut = s.slice(0, nextDollar + 1);
    } else {
      cut = cut.slice(0, cut.lastIndexOf("$"));
    }
  }
  return cut.trim() + "…";
}

function extractMindmapBranches(lesson) {
  const branches = [];

  if (Array.isArray(lesson.requirements) && lesson.requirements.length) {
    branches.push({
      id: "mm-req",
      icon: "🎯",
      title: "Mục tiêu cần đạt",
      color: "#6366f1",
      targetId: "requirementsSection",
      items: lesson.requirements.slice(0, 4).map((r) => truncateMindmapText(r, 95)),
      fullItems: lesson.requirements
    });
  }

  if (lesson.definition) {
    const defLines = String(lesson.definition)
      .split(/\n+/)
      .map((l) => l.replace(/^[-*•+]\s+/, "").trim())
      .filter(Boolean);
    const items = defLines.length > 1
      ? defLines.slice(0, 3).map((l) => truncateMindmapText(l, 100))
      : String(lesson.definition).split(/(?<=[.!?;])\s+/).filter(Boolean).slice(0, 3).map((l) => truncateMindmapText(l, 100));
    if (items.length) {
      branches.push({
        id: "mm-def",
        icon: "📖",
        title: "Khái niệm cốt lõi",
        color: "#0284c7",
        targetId: "definitionSection",
        items: items,
        fullItems: defLines.length ? defLines : items
      });
    }
  }

  if (lesson.theory) {
    const rawLines = String(lesson.theory).replace(/\r\n/g, "\n").split("\n");
    const headings = [];
    const bullets = [];
    rawLines.forEach((raw) => {
      const line = raw.trim();
      if (/^#{2,4}\s+/.test(line)) {
        headings.push(line.replace(/^#{2,4}\s+/, "").trim());
      } else if (/^[-*•+]\s+/.test(line)) {
        bullets.push(line.replace(/^[-*•+]\s+/, "").trim());
      } else if (/^\*\*([^*]{3,65})\*\*/.test(line)) {
        const m = line.match(/^\*\*([^*]{3,65})\*\*/);
        if (m) headings.push(m[1].replace(/:$/, "").trim());
      }
    });
    const sourceList = headings.length >= 2 ? headings : bullets.length ? bullets : rawLines.filter(Boolean);
    if (sourceList.length) {
      branches.push({
        id: "mm-theory",
        icon: "🧠",
        title: "Trọng tâm lý thuyết",
        color: "#059669",
        targetId: "theorySection",
        items: sourceList.slice(0, 4).map((t) => truncateMindmapText(t, 92)),
        fullItems: sourceList.slice(0, 8)
      });
    }
  }

  const formulaList = Array.isArray(lesson.formulas) ? lesson.formulas : (lesson.formula ? [lesson.formula] : []);
  if (formulaList.length) {
    const fItems = [];
    const fFull = [];
    formulaList.forEach((group) => {
      if (group && typeof group === "object" && Array.isArray(group.items)) {
        group.items.forEach((it) => {
          if (typeof it === "string") {
            fFull.push(it);
            if (fItems.length < 4) fItems.push(truncateMindmapText(it, 95));
          } else if (it && (it.name || it.formula)) {
            const fStr = it.formula ? (String(it.formula).includes("$") ? it.formula : `$${it.formula}$`) : "";
            const combined = it.name && fStr ? `**${it.name}:** ${fStr}` : (it.name || fStr);
            fFull.push(combined);
            if (fItems.length < 4) fItems.push(combined);
          }
        });
      } else if (group && typeof group === "object" && (group.name || group.formula)) {
        const fStr = group.formula ? (String(group.formula).includes("$") ? group.formula : `$${group.formula}$`) : "";
        const combined = group.name && fStr ? `**${group.name}:** ${fStr}` : (group.name || fStr);
        fFull.push(combined);
        if (fItems.length < 4) fItems.push(combined);
      } else if (typeof group === "string") {
        fFull.push(group);
        if (fItems.length < 4) fItems.push(truncateMindmapText(group, 95));
      }
    });
    if (fItems.length) {
      branches.push({
        id: "mm-formula",
        icon: "📐",
        title: "Công thức & Quy tắc",
        color: "#d97706",
        targetId: "formulaSection",
        items: fItems,
        fullItems: fFull
      });
    }
  }

  if (lesson.example) {
    const exLines = String(lesson.example).split(/\n+/).map((l) => l.replace(/^[-*•+]\s+/, "").trim()).filter(Boolean);
    branches.push({
      id: "mm-example",
      icon: "📝",
      title: "Dạng bài & Ví dụ",
      color: "#db2777",
      targetId: "exampleSection",
      items: exLines.slice(0, 2).map((l) => truncateMindmapText(l, 95)),
      fullItems: exLines
    });
  }

  const appSource = lesson.real_life || lesson.application || lesson.context;
  const appTarget = lesson.real_life ? "realLifeSection" : lesson.application ? "applicationSection" : "contextSection";
  if (appSource) {
    const appLines = String(appSource)
      .split(/\n+/)
      .map((l) => l.replace(/^[-*•+]\s+/, "").trim())
      .filter(Boolean);
    if (appLines.length) {
      branches.push({
        id: "mm-app",
        icon: "🌍",
        title: "Ứng dụng thực tiễn",
        color: "#7c3aed",
        targetId: appTarget,
        items: appLines.slice(0, 3).map((l) => truncateMindmapText(l, 95)),
        fullItems: appLines
      });
    }
  }

  return branches;
}

function drawMindmapConnections() {
  const stage = document.getElementById("mindmapStage");
  const svg = document.getElementById("mindmapSvg");
  const centerNode = document.getElementById("mmCenterNode");
  if (!stage || !svg || !centerNode) return;

  if (window.innerWidth <= 860) {
    svg.innerHTML = "";
    return;
  }

  const stageW = stage.offsetWidth || 920;
  const stageH = stage.offsetHeight || 600;
  svg.setAttribute("viewBox", `0 0 ${stageW} ${stageH}`);

  const cx = centerNode.offsetLeft + centerNode.offsetWidth / 2;
  const cy = centerNode.offsetTop + centerNode.offsetHeight / 2;

  let pathsHtml = "";
  const branchNodes = stage.querySelectorAll(".mm-branch-node");

  branchNodes.forEach((node) => {
    const color = node.getAttribute("data-color") || "#6366f1";
    const isActive = node.classList.contains("is-active");
    const bx = node.offsetLeft + node.offsetWidth / 2;
    const by = node.offsetTop + node.offsetHeight / 2;

    const dx = bx - cx;
    const startX = cx + (dx >= 0 ? Math.min(75, centerNode.offsetWidth * 0.42) : -Math.min(75, centerNode.offsetWidth * 0.42));
    const startY = cy + (by - cy) * 0.22;
    const endX = bx + (dx >= 0 ? -node.offsetWidth * 0.46 : node.offsetWidth * 0.46);
    const endY = by;

    const c1x = startX + (endX - startX) * 0.48;
    const c1y = startY;
    const c2x = startX + (endX - startX) * 0.56;
    const c2y = endY;

    const d = `M ${startX.toFixed(1)} ${startY.toFixed(1)} C ${c1x.toFixed(1)} ${c1y.toFixed(1)}, ${c2x.toFixed(1)} ${c2y.toFixed(1)}, ${endX.toFixed(1)} ${endY.toFixed(1)}`;
    pathsHtml += `<path d="${d}" fill="none" stroke="${color}" stroke-width="${isActive ? 4.2 : 2.8}" stroke-linecap="round" opacity="${isActive ? 0.98 : 0.72}" class="mm-connector-path" />`;
    pathsHtml += `<circle cx="${endX.toFixed(1)}" cy="${endY.toFixed(1)}" r="${isActive ? 5.5 : 4}" fill="${color}" />`;
  });

  svg.innerHTML = pathsHtml;
}

function applyMindmapTransform() {
  const stage = document.getElementById("mindmapStage");
  if (!stage) return;
  if (window.innerWidth <= 860) {
    stage.style.transform = "";
    return;
  }
  stage.style.transform = `translate(${mindmapState.panX}px, ${mindmapState.panY}px) scale(${mindmapState.zoom})`;
}

function showMindmapBranchDetail(branch) {
  const panel = document.getElementById("mindmapDetailPanel");
  if (!panel || !branch) return;

  mindmapState.activeBranchId = branch.id;
  document.querySelectorAll(".mm-branch-node").forEach((el) => {
    el.classList.toggle("is-active", el.getAttribute("data-branch-id") === branch.id);
  });

  const listHtml = (branch.fullItems || branch.items || [])
    .map((item) => `<li>${formatInlineStyles(stripMarkdownPlain(item))}</li>`)
    .join("");

  panel.style.setProperty("--mm-branch-color", branch.color);
  panel.classList.remove("hidden");
  panel.innerHTML = `
    <div class="mm-detail-head">
      <div class="mm-detail-title">
        <span class="mm-detail-icon">${branch.icon}</span>
        <strong>${escapeHTML(branch.title)}</strong>
      </div>
      <div class="mm-detail-actions">
        <a href="#${escapeHTML(branch.targetId)}" class="mm-jump-btn btn-25d">↓ Đi tới mục chi tiết</a>
        <button type="button" class="mm-close-btn" id="mmDetailCloseBtn" aria-label="Đóng bảng chi tiết">✕</button>
      </div>
    </div>
    <ul class="mm-detail-list">${listHtml}</ul>
  `;

  const closeBtn = document.getElementById("mmDetailCloseBtn");
  if (closeBtn) {
    closeBtn.onclick = () => {
      panel.classList.add("hidden");
      mindmapState.activeBranchId = null;
      document.querySelectorAll(".mm-branch-node").forEach((el) => el.classList.remove("is-active"));
      drawMindmapConnections();
    };
  }

  upgradeKatex(panel);
  drawMindmapConnections();
}

function renderMindmap(lesson) {
  if (!mindmapSection) return;
  const nodesContainer = document.getElementById("mindmapNodes");
  const detailPanel = document.getElementById("mindmapDetailPanel");
  if (!nodesContainer) return;

  const branches = extractMindmapBranches(lesson);
  mindmapState.branches = branches;
  mindmapState.zoom = 1;
  mindmapState.panX = 0;
  mindmapState.panY = 0;
  mindmapState.expandedAll = false;
  mindmapState.activeBranchId = null;
  if (detailPanel) detailPanel.classList.add("hidden");

  if (branches.length < 2) {
    setSectionVisible(mindmapSection, false);
    return;
  }

  setSectionVisible(mindmapSection, true);

  const slotLayouts = {
    2: [
      { left: 20, top: 50, side: "left" },
      { left: 80, top: 50, side: "right" }
    ],
    3: [
      { left: 20, top: 32, side: "left" },
      { left: 80, top: 32, side: "right" },
      { left: 50, top: 82, side: "bottom" }
    ],
    4: [
      { left: 20, top: 26, side: "left" },
      { left: 80, top: 26, side: "right" },
      { left: 20, top: 76, side: "left" },
      { left: 80, top: 76, side: "right" }
    ],
    5: [
      { left: 20, top: 22, side: "left" },
      { left: 80, top: 22, side: "right" },
      { left: 19, top: 74, side: "left" },
      { left: 81, top: 74, side: "right" },
      { left: 50, top: 85, side: "bottom" }
    ],
    6: [
      { left: 19, top: 20, side: "left" },
      { left: 81, top: 20, side: "right" },
      { left: 17, top: 52, side: "left" },
      { left: 83, top: 52, side: "right" },
      { left: 20, top: 83, side: "left" },
      { left: 80, top: 83, side: "right" }
    ]
  };
  const slots = slotLayouts[Math.min(6, branches.length)] || slotLayouts[6];

  const shortTitle = String(lesson.title || "Bài học")
    .replace(/^(Chương|Chủ đề)\s+[^:–-]+[:–-]\s*/i, "")
    .trim();
  const gradeLabel = lesson.grade || gradeFromUrl ? `Lớp ${lesson.grade || gradeFromUrl}` : (subjectNames[subject] || "Bài học");

  let html = `
    <div class="mm-center-node" id="mmCenterNode">
      <div class="mm-center-glow"></div>
      <span class="mm-center-badge">${escapeHTML(gradeLabel)} · ${branches.length} nhánh trọng tâm</span>
      <div class="mm-center-icon">${escapeHTML(lesson.icon || "🗺️")}</div>
      <strong class="mm-center-title">${formatInlineStyles(shortTitle)}</strong>
    </div>
  `;

  branches.slice(0, 6).forEach((b, idx) => {
    const slot = slots[idx] || { left: 50, top: 50, side: "right" };
    const previewItems = (mindmapState.expandedAll ? b.fullItems : b.items.slice(0, 2)) || [];
    const bulletsHtml = previewItems
      .map((it) => `<li>${formatInlineStyles(stripMarkdownPlain(it))}</li>`)
      .join("");
    const moreCount = Math.max(0, (b.fullItems ? b.fullItems.length : b.items.length) - previewItems.length);

    html += `
      <div class="mm-branch-node side-${slot.side}"
           data-branch-id="${b.id}"
           data-color="${b.color}"
           style="left:${slot.left}%; top:${slot.top}%; --mm-color:${b.color};"
           role="button"
           tabindex="0"
           aria-label="Nhánh ${escapeHTML(b.title)}">
        <div class="mm-branch-head">
          <span class="mm-branch-icon">${b.icon}</span>
          <strong class="mm-branch-title">${escapeHTML(b.title)}</strong>
          <span class="mm-branch-count">${(b.fullItems || b.items).length} ý</span>
        </div>
        <ul class="mm-branch-list">${bulletsHtml}</ul>
        ${moreCount > 0 ? `<div class="mm-branch-more">+${moreCount} ý chi tiết · Nhấn để xem</div>` : `<div class="mm-branch-more">Nhấn để xem chi tiết →</div>`}
      </div>
    `;
  });

  nodesContainer.innerHTML = html;

  nodesContainer.querySelectorAll(".mm-branch-node").forEach((node) => {
    const branchId = node.getAttribute("data-branch-id");
    const branchObj = branches.find((x) => x.id === branchId);
    if (!branchObj) return;
    node.addEventListener("click", (e) => {
      e.stopPropagation();
      showMindmapBranchDetail(branchObj);
    });
    node.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        showMindmapBranchDetail(branchObj);
      }
    });
  });

  const centerNode = document.getElementById("mmCenterNode");
  if (centerNode) {
    centerNode.addEventListener("click", () => {
      const expandBtn = document.getElementById("mmExpandAllBtn");
      if (expandBtn) expandBtn.click();
    });
  }

  upgradeKatex(nodesContainer);
  requestAnimationFrame(() => {
    drawMindmapConnections();
    setTimeout(drawMindmapConnections, 180);
  });
}

(function initMindmapInteractions() {
  const viewport = document.getElementById("mindmapViewport");
  const expandBtn = document.getElementById("mmExpandAllBtn");
  const zoomInBtn = document.getElementById("mmZoomInBtn");
  const zoomOutBtn = document.getElementById("mmZoomOutBtn");
  const resetBtn = document.getElementById("mmResetBtn");

  if (expandBtn) {
    expandBtn.addEventListener("click", () => {
      mindmapState.expandedAll = !mindmapState.expandedAll;
      expandBtn.textContent = mindmapState.expandedAll ? "🔼 Thu gọn nhánh" : "🔍 Mở rộng chi tiết";
      const stage = document.getElementById("mindmapStage");
      if (stage) stage.classList.toggle("is-expanded-all", mindmapState.expandedAll);

      document.querySelectorAll(".mm-branch-node").forEach((node) => {
        const b = mindmapState.branches.find((x) => x.id === node.getAttribute("data-branch-id"));
        if (!b) return;
        const listEl = node.querySelector(".mm-branch-list");
        const moreEl = node.querySelector(".mm-branch-more");
        const items = mindmapState.expandedAll ? (b.fullItems || b.items) : b.items.slice(0, 2);
        if (listEl) {
          listEl.innerHTML = items.map((it) => `<li>${formatInlineStyles(stripMarkdownPlain(it))}</li>`).join("");
          upgradeKatex(listEl);
        }
        if (moreEl) {
          const leftCount = Math.max(0, (b.fullItems || b.items).length - items.length);
          moreEl.textContent = leftCount > 0 ? `+${leftCount} ý chi tiết · Nhấn để xem` : "Nhấn để mở mục tương ứng →";
        }
      });

      requestAnimationFrame(drawMindmapConnections);
    });
  }

  if (zoomInBtn) {
    zoomInBtn.addEventListener("click", () => {
      mindmapState.zoom = Math.min(1.35, +(mindmapState.zoom + 0.1).toFixed(2));
      applyMindmapTransform();
    });
  }

  if (zoomOutBtn) {
    zoomOutBtn.addEventListener("click", () => {
      mindmapState.zoom = Math.max(0.75, +(mindmapState.zoom - 0.1).toFixed(2));
      applyMindmapTransform();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      mindmapState.zoom = 1;
      mindmapState.panX = 0;
      mindmapState.panY = 0;
      applyMindmapTransform();
      requestAnimationFrame(drawMindmapConnections);
    });
  }

  if (viewport) {
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    viewport.addEventListener("mousedown", (e) => {
      if (window.innerWidth <= 860) return;
      if (e.target.closest(".mm-branch-node") || e.target.closest(".mm-center-node")) return;
      isDragging = true;
      startX = e.clientX - mindmapState.panX;
      startY = e.clientY - mindmapState.panY;
      viewport.classList.add("is-panning");
    });

    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      mindmapState.panX = Math.max(-220, Math.min(220, e.clientX - startX));
      mindmapState.panY = Math.max(-160, Math.min(160, e.clientY - startY));
      applyMindmapTransform();
    });

    window.addEventListener("mouseup", () => {
      if (!isDragging) return;
      isDragging = false;
      viewport.classList.remove("is-panning");
    });
  }

  window.addEventListener("resize", () => {
    requestAnimationFrame(drawMindmapConnections);
  });
})();

/* =========================================================
   TỰ ĐỘNG TẠO MỤC LỤC BÊN TRÁI
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
      const GAME_FILES = { function_challenge: "function-challenge", "store-management": "store_management" };
      const file = GAME_FILES[lesson.game_type] || lesson.game_type;
      window.location.href = `games/${encodeURIComponent(file)}.html?lesson_id=${lesson.id}`;
    };
    noGame.classList.add("hidden");
  } else {
    gameButton.style.display = "none";
    noGame.classList.remove("hidden");
  }
}

/* =========================================================
   YÊU CẦU CẦN ĐẠT & BỘ CÂU HỎI 3 MỨC ĐỘ (CHƯƠNG TRÌNH SGK MỚI)
========================================================= */
function renderRequirements(lesson) {
  if (!requirementsSection || !requirementsList) return;
  const list = Array.isArray(lesson.requirements) ? lesson.requirements.filter(Boolean) : [];
  if (!list.length) {
    setSectionVisible(requirementsSection, false);
    return;
  }
  requirementsList.innerHTML = list
    .map((item) => `<li>${formatInlineStyles(item)}</li>`)
    .join("");
  if (sgkRef) {
    const subjLabel = subjectNames[subject] || "môn học";
    sgkRef.textContent = `Theo Chương trình giáo dục phổ thông môn ${subjLabel} 2018 (Thông tư 32/2018/TT-BGDĐT). Sau bài học này, em cần:`;
  }
  setSectionVisible(requirementsSection, true);
}

function renderQuizSet(lesson) {
  if (!quizSet) return;
  if (singleQuestionBox) singleQuestionBox.style.display = "none";
  const titleEl = questionSection ? questionSection.querySelector(".section-title") : null;
  if (titleEl) titleEl.textContent = `❓ Luyện tập ${lesson.quiz.length} câu: Biết – Hiểu – Vận dụng`;
  if (questionSection) questionSection.setAttribute("data-toc", "Luyện tập 3 mức độ");
  const rewardLabel = document.querySelector("#rewardQuiz .reward-text");
  if (rewardLabel && rewardLabel.firstChild && rewardLabel.firstChild.nodeType === 3) {
    rewardLabel.firstChild.textContent = "Luyện tập " + lesson.quiz.length + " câu";
  }
  setSectionVisible(questionSection, true);

  window.HDLGQuiz.render(quizSet, lesson.quiz, {
    format: formatRichText,
    inline: formatInlineStyles,
    onComplete: function (result) {
      handleQuizSetReward(result);
    }
  });
}

function handleQuizSetReward(result) {
  if (!rewardState.hasQuiz) return;
  rewardState.quizAttempted = true;
  const lid = rewardState.lessonId;
  if (!result.passed) {
    if (result.firstTime && window.HDLG && typeof HDLG.track === "function") {
      whenHdlgReady(function () { if (!getLessonStatus().quiz) HDLG.track("quizWrong", lid); });
    }
    renderRewardCard();
    return;
  }
  if (hdlgReady()) {
    whenHdlgReady(function () {
      if (getLessonStatus().quiz) return renderRewardCard();
      const gained = HDLG.lessonReward(lid, "quiz", rewardState.quizStars, {
        label: `Luyện tập đúng ${result.correct}/${result.total} câu`
      });
      if (gained > 0) popRewardItem("rewardQuiz");
      renderRewardCard();
    });
  }
  renderRewardCard();
}

/* =========================================================
   HỖ TRỢ TÁCH BÀI HỌC TỰ ĐỘNG (NẾU MỞ ?sub=N TRÊN DB CŨ CHƯA IMPORT LẠI)
   & ĐIỀU HƯỚNG CÁC BÀI HỌC TRONG CÙNG CHƯƠNG
========================================================= */
let currentLessonData = null;

function splitCombinedTheorySections(rawTheory) {
  const text = String(rawTheory || "").replace(/\r\n/g, "\n");
  if (!text) return [];
  const regex = /^###\s+((?:Bài|Chủ đề|Phần|Mục)\s+[^\n]+)$/gm;
  const matches = [];
  let m;
  while ((m = regex.exec(text)) !== null) {
    matches.push({ heading: m[1].trim(), startIdx: m.index, bodyStart: m.index + m[0].length });
  }
  if (matches.length < 2) return [];
  return matches.map((item, idx) => {
    const endIdx = idx + 1 < matches.length ? matches[idx + 1].startIdx : text.length;
    const body = text.slice(item.bodyStart, endIdx).trim();
    const firstBullet = body.split("\n").map((l) => l.replace(/^[-*•+]\s+/, "").trim()).find(Boolean) || "";
    return {
      subIndex: idx,
      title: item.heading,
      description: firstBullet.replace(/\*\*/g, "").slice(0, 150),
      theory: `### ${item.heading}\n${body}`
    };
  });
}

function applyVirtualSubLessonIfAny(rawLesson) {
  if (subIndexFromUrl === null || isNaN(subIndexFromUrl)) return rawLesson;
  const subSections = splitCombinedTheorySections(rawLesson.theory);
  if (!subSections.length || !subSections[subIndexFromUrl]) return rawLesson;

  const chosen = subSections[subIndexFromUrl];
  const totalSubs = subSections.length;
  const clone = Object.assign({}, rawLesson);
  clone._virtualSiblings = subSections.map((s) => ({
    id: rawLesson.id,
    subIndex: s.subIndex,
    title: s.title,
    topic: rawLesson.topic,
    grade: rawLesson.grade
  }));
  clone.context_title = rawLesson.context_title && /^(Chương|Chủ đề)/i.test(rawLesson.context_title)
    ? rawLesson.context_title
    : rawLesson.title;
  clone.title = chosen.title;
  if (chosen.description) clone.description = chosen.description;
  clone.theory = chosen.theory;

  if (Array.isArray(rawLesson.quiz) && rawLesson.quiz.length >= totalSubs * 2) {
    const chunkSize = Math.max(3, Math.ceil(rawLesson.quiz.length / totalSubs));
    const startQ = Math.min(subIndexFromUrl * Math.floor(rawLesson.quiz.length / totalSubs), Math.max(0, rawLesson.quiz.length - chunkSize));
    clone.quiz = rawLesson.quiz.slice(startQ, startQ + chunkSize);
  }
  return clone;
}

function resolveChapterTitle(lesson) {
  const ct = String(lesson.context_title || "").trim();
  if (/^(Chương|Chủ đề|Chuyên đề)\b/i.test(ct)) return ct;
  return "";
}

function buildLessonHref(item, fallbackGrade, fallbackTopic) {
  const g = item.grade || fallbackGrade || "";
  const tp = item.topic || fallbackTopic || "";
  const subParam = typeof item.subIndex === "number" ? `&sub=${item.subIndex}` : "";
  return `lesson.html?id=${encodeURIComponent(item.id)}&subject=${encodeURIComponent(subject)}&grade=${encodeURIComponent(g)}&topic=${encodeURIComponent(tp)}${subParam}`;
}

async function loadChapterSiblingLessons(lesson) {
  if (!chapterLessonsCard || !chapterLessonsList) return;
  const g = lesson.grade || gradeFromUrl;
  const tp = lesson.topic || topicFromUrl;
  if (!tp) {
    chapterLessonsCard.classList.add("hidden");
    if (chapterNavFooter) chapterNavFooter.classList.add("hidden");
    return;
  }

  let siblings = [];
  if (Array.isArray(lesson._virtualSiblings) && lesson._virtualSiblings.length > 1) {
    siblings = lesson._virtualSiblings;
  } else {
    let allGradeLessons = null;
    const cacheKey = `hdlg_lessons_${subject}_${g}`;
    try {
      const cached = sessionStorage.getItem(cacheKey);
      if (cached) allGradeLessons = JSON.parse(cached);
    } catch (_) {}

    if (!Array.isArray(allGradeLessons) || !allGradeLessons.length) {
      try {
        const res = await fetch(`${API_BASE}/content/subjects/${encodeURIComponent(subject)}/lessons${g ? `?grade=${encodeURIComponent(g)}` : ""}`);
        if (res.ok) {
          allGradeLessons = await res.json();
          try { sessionStorage.setItem(cacheKey, JSON.stringify(allGradeLessons)); } catch (_) {}
        }
      } catch (_) {}
    }

    if (Array.isArray(allGradeLessons)) {
      siblings = allGradeLessons
        .filter((l) => String(l.topic || "") === String(tp))
        .sort((a, b) => (a.order || a.id || 0) - (b.order || b.id || 0));
    }
  }

  if (!Array.isArray(siblings) || siblings.length <= 1) {
    chapterLessonsCard.classList.add("hidden");
    if (chapterNavFooter) chapterNavFooter.classList.add("hidden");
    return;
  }

  // Render Sidebar Chapter Lessons Card
  chapterLessonsCard.classList.remove("hidden");
  const chapterName = resolveChapterTitle(lesson) || "Các bài trong chương";
  if (chapterSidebarTitle) {
    const shortChap = chapterName.split(":")[0].trim();
    chapterSidebarTitle.textContent = `📚 ${shortChap.toUpperCase()}`;
  }

  let completedCount = 0;
  let currentIdx = -1;

  const listHtml = siblings.map((item, idx) => {
    const isCurrent = typeof item.subIndex === "number"
      ? item.subIndex === subIndexFromUrl
      : String(item.id) === String(lesson.id);
    if (isCurrent) currentIdx = idx;

    const st = window.HDLG && typeof HDLG.lessonStatus === "function"
      ? HDLG.lessonStatus(item.id)
      : { read: false, quiz: false, stars: 0 };
    const isDone = !!(st.read || st.quiz);
    if (isDone) completedCount++;

    const href = buildLessonHref(item, g, tp);
    return `
      <a href="${escapeHTML(href)}" class="ch-lesson-link${isCurrent ? " active" : ""}${isDone ? " is-done" : ""}">
        <span class="ch-lesson-num">${isDone ? "✓" : idx + 1}</span>
        <span class="ch-lesson-name">${escapeHTML(item.title || `Bài ${idx + 1}`)}</span>
      </a>
    `;
  }).join("");

  chapterLessonsList.innerHTML = listHtml;
  if (chapterSidebarProgress) {
    chapterSidebarProgress.textContent = `${ currentIdx >= 0 ? currentIdx + 1 : completedCount }/${siblings.length} bài`;
  }

  // Render Bottom Prev / Next Chapter Navigation Bar
  if (chapterNavFooter && currentIdx !== -1) {
    const prevItem = currentIdx > 0 ? siblings[currentIdx - 1] : null;
    const nextItem = currentIdx + 1 < siblings.length ? siblings[currentIdx + 1] : null;
    const gradePage = subjectGradePages[subject] || "math-grade.html";
    const chapterListUrl = `${gradePage}?grade=${encodeURIComponent(g || "")}&topic=${encodeURIComponent(tp)}`;

    chapterNavFooter.classList.remove("hidden");
    chapterNavFooter.innerHTML = `
      <div class="ch-nav-grid">
        ${prevItem ? `
          <a href="${escapeHTML(buildLessonHref(prevItem, g, tp))}" class="ch-nav-btn ch-nav-prev">
            <span class="ch-nav-dir">← Bài trước</span>
            <strong class="ch-nav-title">${escapeHTML(prevItem.title)}</strong>
          </a>
        ` : `<div class="ch-nav-btn ch-nav-disabled"><span class="ch-nav-dir">Đầu chương</span><strong class="ch-nav-title">${escapeHTML(chapterName)}</strong></div>`}

        <a href="${escapeHTML(chapterListUrl)}" class="ch-nav-btn ch-nav-center">
          <span class="ch-nav-dir">📑 Chương hiện tại</span>
          <strong class="ch-nav-title">Xem tất cả ${siblings.length} bài học</strong>
        </a>

        ${nextItem ? `
          <a href="${escapeHTML(buildLessonHref(nextItem, g, tp))}" class="ch-nav-btn ch-nav-next">
            <span class="ch-nav-dir">Bài tiếp theo →</span>
            <strong class="ch-nav-title">${escapeHTML(nextItem.title)}</strong>
          </a>
        ` : `
          <a href="${escapeHTML(chapterListUrl)}" class="ch-nav-btn ch-nav-next is-finish">
            <span class="ch-nav-dir">🎉 Hoàn thành chương</span>
            <strong class="ch-nav-title">Quay lại chọn Chương tiếp theo →</strong>
          </a>
        `}
      </div>
    `;
  }
}

/* =========================================================
   RENDER LESSON
========================================================= */
function renderLesson(rawLesson) {
  const lesson = applyVirtualSubLessonIfAny(rawLesson);
  currentLessonData = lesson;

  if (lessonIcon) lessonIcon.textContent = lesson.icon || "📚";
  const g = lesson.grade || gradeFromUrl;
  const tp = lesson.topic || topicFromUrl;
  if (lessonGrade) {
    lessonGrade.textContent = g ? `Lớp ${g}` : "Bài học";
  }

  // Hiển thị huy hiệu Chương / Chủ đề trên đầu bài học
  const chapName = resolveChapterTitle(lesson);
  if (lessonChapterBadge) {
    if (chapName) {
      const gradePage = subjectGradePages[subject] || "math-grade.html";
      lessonChapterBadge.textContent = `📂 ${chapName}`;
      lessonChapterBadge.href = `${gradePage}?grade=${encodeURIComponent(g || "")}${tp ? `&topic=${encodeURIComponent(tp)}` : ""}`;
      lessonChapterBadge.classList.remove("hidden");
    } else {
      lessonChapterBadge.classList.add("hidden");
    }
  }

  if (lessonTitle) {
    lessonTitle.textContent = lesson.title || "Bài học";
    document.title = `${lesson.title || "Bài học"} - HỌC ĐỂ LÀM GÌ`;
  }
  if (lessonDescription) {
    lessonDescription.innerHTML = formatInlineStyles(lesson.description || "");
  }

  if (lesson.definition) {
    setText(definition, lesson.definition);
    setSectionVisible(definitionSection, true);
  } else {
    setSectionVisible(definitionSection, false);
  }

  if (lesson.context || lesson.context_title) {
    if (contextTitle) {
      contextTitle.textContent = chapName ? `📖 Tổng quan ${chapName}` : (lesson.context_title || "Bối cảnh thực tế");
    }
    setText(context, lesson.context || "");
    setSectionVisible(contextSection, !!lesson.context);
  } else {
    setSectionVisible(contextSection, false);
  }

  if (lesson.theory) {
    setText(theory, lesson.theory);
    setSectionVisible(theorySection, true);
  } else {
    setSectionVisible(theorySection, false);
  }

  if (lesson.concept) {
    setText(concept, lesson.concept);
    setSectionVisible(conceptSection, true);
  } else {
    setSectionVisible(conceptSection, false);
  }

  renderFormulas(lesson.formulas, lesson.formula);

  if (lesson.example || lesson.example_answer) {
    setText(example, lesson.example || "");
    setText(exampleAnswer, lesson.example_answer || "");
    setSectionVisible(exampleSection, true);
  } else {
    setSectionVisible(exampleSection, false);
  }

  renderRequirements(lesson);
  renderMindmap(lesson);

  if (Array.isArray(lesson.quiz) && lesson.quiz.length && window.HDLGQuiz) {
    renderQuizSet(lesson);
  } else if (lesson.question) {
    setText(question, lesson.question);
    renderAnswers(lesson.answers, lesson.correct);
  } else {
    setSectionVisible(questionSection, false);
  }

  if (lesson.meaning) {
    setText(meaning, lesson.meaning);
    setSectionVisible(meaningSection, true);
  } else {
    setSectionVisible(meaningSection, false);
  }

  if (lesson.application) {
    setText(application, lesson.application);
    setSectionVisible(applicationSection, true);
  } else {
    setSectionVisible(applicationSection, false);
  }

  if (lesson.real_life) {
    setText(realLife, lesson.real_life);
    setSectionVisible(realLifeSection, true);
  } else {
    setSectionVisible(realLifeSection, false);
  }

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

  renderExtraBackendSections(lesson);
  renderGame(lesson);
  initLessonReward(lesson);
  loadChapterSiblingLessons(lesson);
  if (window.HDLG && typeof HDLG.track === "function") whenHdlgReady(function () { HDLG.track("open", lesson.id); });

  finishLoading();
  upgradeKatex(lessonContent);
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
  checkReadReward(percent);

  const links = document.querySelectorAll(".toc-link");
  let activeIndex = 0;
  links.forEach((link, idx) => {
    const targetId = link.getAttribute("href")?.slice(1);
    const targetEl = targetId ? document.getElementById(targetId) : null;
    if (targetEl && targetEl.getBoundingClientRect().top <= 145) {
      activeIndex = idx;
    }
  });
  links.forEach((link, idx) => link.classList.toggle("active", idx === activeIndex));
}

window.addEventListener("scroll", updateReadingProgress, { passive: true });

/* =========================================================
   CỘNG SAO KHI HỌC BÀI
========================================================= */
const READ_DONE_PERCENT = 92;
const MIN_READ_SECONDS = 30;

const rewardState = {
  lessonId: null,
  hasQuiz: false,
  isQuizSet: false,
  quizCount: 0,
  readStars: 5,
  quizStars: 5,
  startedAt: Date.now(),
  reachedEnd: false,
  readTimer: null,
  quizAttempted: false
};

function hdlgReady() {
  return window.HDLG && typeof HDLG.lessonReward === "function";
}

function whenHdlgReady(fn) {
  if (window.HDLG && HDLG.ready && typeof HDLG.ready.then === "function") {
    HDLG.ready.then(fn, fn);
  } else {
    fn();
  }
}

function getLessonStatus() {
  if (!hdlgReady() || rewardState.lessonId == null) {
    return { read: false, quiz: false, stars: 0, done: false };
  }
  return HDLG.lessonStatus(rewardState.lessonId);
}

function setRewardItem(itemId, hintId, ptsId, state, hint, pts) {
  const item = document.getElementById(itemId);
  const hintEl = document.getElementById(hintId);
  const ptsEl = document.getElementById(ptsId);
  if (!item) return;
  item.classList.toggle("is-done", state === "done");
  item.classList.toggle("is-missed", state === "missed");
  if (hintEl && hint != null) hintEl.textContent = hint;
  if (ptsEl && pts != null) ptsEl.textContent = pts;
}

function renderRewardCard() {
  const card = document.getElementById("rewardCard");
  if (!card) return;
  if (!hdlgReady() || rewardState.lessonId == null) {
    card.style.display = "none";
    return;
  }
  card.style.display = "";

  const st = getLessonStatus();
  const max = rewardState.readStars + (rewardState.hasQuiz ? rewardState.quizStars : 0);
  const totalEl = document.getElementById("rewardTotal");
  if (totalEl) totalEl.textContent = `${Math.min(st.stars, max)}/${max} ⭐`;
  card.classList.toggle("is-complete", st.stars >= max);

  // Đọc hết bài
  if (st.read) {
    setRewardItem("rewardRead", "rewardReadHint", "rewardReadPts", "done", "Đã nhận sao", "✓");
  } else {
    const left = Math.max(0, MIN_READ_SECONDS - Math.floor((Date.now() - rewardState.startedAt) / 1000));
    const hint = rewardState.reachedEnd && left > 0
      ? `Đọc kỹ thêm ${left} giây nữa nhé`
      : "Cuộn tới cuối bài học";
    setRewardItem("rewardRead", "rewardReadHint", "rewardReadPts", "", hint, `+${rewardState.readStars}`);
  }

  // Kiểm tra nhanh / Luyện tập
  const quizItem = document.getElementById("rewardQuiz");
  if (quizItem) quizItem.style.display = rewardState.hasQuiz ? "" : "none";
  if (rewardState.hasQuiz) {
    const qTotal = rewardState.quizCount || 10;
    const qNeed = Math.ceil(qTotal * 0.7);
    if (st.quiz) {
      setRewardItem("rewardQuiz", "rewardQuizHint", "rewardQuizPts", "done", "Đã nhận sao", "✓");
    } else if (rewardState.quizAttempted) {
      setRewardItem("rewardQuiz", "rewardQuizHint", "rewardQuizPts", "missed",
        rewardState.isQuizSet
          ? `Chưa đạt ${qNeed}/${qTotal} — xem lời giải rồi bấm “Làm lại”`
          : "Chưa đúng — ôn lại rồi mở lại bài để thử lần nữa", `+${rewardState.quizStars}`);
    } else {
      setRewardItem("rewardQuiz", "rewardQuizHint", "rewardQuizPts", "",
        rewardState.isQuizSet ? `Làm đúng từ ${qNeed}/${qTotal} câu luyện tập` : "Chọn đúng ngay lần đầu", `+${rewardState.quizStars}`);
    }
  }
}

function popRewardItem(itemId) {
  const item = document.getElementById(itemId);
  if (!item) return;
  item.classList.remove("just-earned");
  void item.offsetWidth;
  item.classList.add("just-earned");
}

function tryGiveReadReward() {
  if (!hdlgReady() || rewardState.lessonId == null) return;
  if (getLessonStatus().read || !rewardState.reachedEnd) return;

  const elapsed = (Date.now() - rewardState.startedAt) / 1000;
  if (elapsed < MIN_READ_SECONDS) {
    renderRewardCard();
    if (!rewardState.readTimer) {
      rewardState.readTimer = setInterval(function () {
        if ((Date.now() - rewardState.startedAt) / 1000 >= MIN_READ_SECONDS) {
          clearInterval(rewardState.readTimer);
          rewardState.readTimer = null;
          tryGiveReadReward();
        } else {
          renderRewardCard();
        }
      }, 1000);
    }
    return;
  }

  whenHdlgReady(function () {
    const gained = HDLG.lessonReward(rewardState.lessonId, "read", rewardState.readStars, {
      label: "Đọc hết bài học"
    });
    if (gained > 0) popRewardItem("rewardRead");
    renderRewardCard();
  });
}

function checkReadReward(percent) {
  if (rewardState.lessonId == null || rewardState.reachedEnd) return;
  if (percent >= READ_DONE_PERCENT) {
    rewardState.reachedEnd = true;
    tryGiveReadReward();
  }
}

function handleQuizReward(isCorrect) {
  if (!rewardState.hasQuiz || rewardState.quizAttempted) return;
  rewardState.quizAttempted = true;
  if (!isCorrect && window.HDLG && typeof HDLG.track === "function") {
    const lid = rewardState.lessonId;
    whenHdlgReady(function () { if (!getLessonStatus().quiz) HDLG.track("quizWrong", lid); });
  }

  if (isCorrect && hdlgReady()) {
    whenHdlgReady(function () {
      if (getLessonStatus().quiz) return renderRewardCard();
      const gained = HDLG.lessonReward(rewardState.lessonId, "quiz", rewardState.quizStars, {
        label: "Trả lời đúng Kiểm tra nhanh"
      });
      if (gained > 0) popRewardItem("rewardQuiz");
      renderRewardCard();
    });
  }
  renderRewardCard();
}

function initLessonReward(lesson) {
  rewardState.lessonId = lesson.id;
  rewardState.isQuizSet = !!(Array.isArray(lesson.quiz) && lesson.quiz.length);
  rewardState.quizCount = rewardState.isQuizSet ? lesson.quiz.length : 0;
  rewardState.hasQuiz = rewardState.isQuizSet || !!(lesson.question && Array.isArray(lesson.answers) && lesson.answers.length);
  const total = (window.HDLG && HDLG.LESSON_STARS) || 10;
  if (rewardState.hasQuiz) {
    rewardState.quizStars = Math.floor(total / 2);
    rewardState.readStars = total - rewardState.quizStars;
  } else {
    rewardState.quizStars = 0;
    rewardState.readStars = total;
  }
  rewardState.startedAt = Date.now();
  renderRewardCard();

  if (window.HDLG && HDLG.ready && typeof HDLG.ready.then === "function") {
    HDLG.ready.then(renderRewardCard);
  }
  window.addEventListener("hdlg:update", renderRewardCard);
}

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
    let lesson = null;
    const cached = sessionStorage.getItem(`hdlg_lesson_${lessonId}`);
    if (cached) {
      try { lesson = JSON.parse(cached); } catch (_) {}
    }
    if (!lesson || lesson.id === undefined) {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Không thể tải bài học. HTTP ${response.status}`);
      }
      lesson = await response.json();
      try { sessionStorage.setItem(`hdlg_lesson_${lessonId}`, JSON.stringify(lesson)); } catch (_) {}
    }
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