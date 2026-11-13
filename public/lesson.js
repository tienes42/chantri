/* =========================================================
   LESSON.JS — SÁCH HỌC VIỆN NỔI 2.5D & ĐỌC HIỂU CHUYÊN SÂU
   Dùng chung cho: Math, Physics, Chemistry và các môn khác
   Hỗ trợ:
   - KaTeX 0.16.11 + Offline Math/Chem Renderer (window.HDLGMath)
   - Sơ đồ tư duy tổng quan 2.5D tương tác (#mindmapSection)
   - Cấu trúc 3 cấp: Lớp ➔ Chương/Chủ đề ➔ Từng Bài học độc lập
     (Mỗi bài học chỉ hiển thị kiến thức, công thức, ví dụ và câu hỏi của riêng bài đó)
   API: GET /api/content/lessons/{id}
========================================================= */

// Dọn bộ nhớ đệm sessionStorage cũ để tránh hiển thị bản ghi gộp chương từ phiên bản cũ
try {
  Object.keys(sessionStorage).forEach((k) => {
    if ((k.startsWith("hdlg_lesson") || k.startsWith("hdlg_lessons")) && !k.startsWith("hdlg_v9_")) {
      sessionStorage.removeItem(k);
    }
  });
} catch (_) {}

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

// 1. Pure character/token cleanup (NEVER adds $ delimiters — safe inside math mode!)
function cleanMathCorruptions(rawStr) {
  if (rawStr === null || rawStr === undefined) return "";
  return String(rawStr)
    .replace(/\x09ext\{/g, "\\text{")
    .replace(/\x09imes\b/g, "\\times")
    .replace(/\x09o\b/g, "\\to")
    .replace(/\x09riangle\b/g, "\\triangle")
    .replace(/\x0bdots\b/g, "\\vdots")
    .replace(/\\x0bdots\b/g, "\\vdots")
    .replace(/\x0crac\{/g, "\\frac{")
    .replace(/\x08eta\b/g, "\\beta")
    .replace(/\x08ar\{/g, "\\bar{")
    .replace(/\x07lpha\b/g, "\\alpha")
    .replace(/\x07pprox\b/g, "\\approx")
    .replace(/\\geft\b/g, "\\left")
    .replace(/\\geftrightarrow\b/g, "\\leftrightarrow")
    .replace(/\\notinfty\b/g, "\\infty")
    .replace(/\\notint\b/g, "\\int")
    .replace(/\\lightning\b/g, "\\text{⚡}")
    .replace(/\\text\{([^{}]*)\\text\{([^{}]*)\}([^{}]*)\}/g, "\\text{$1$2$3}")
    .replace(/phần tử thuộc \(\$\\notin\$\)/g, "phần tử thuộc ($\\in$)")
    .replace(/\$x \\notin A\$ \(\$x\$ thuộc \$A\$\)/g, "$x \\in A$ ($x$ thuộc $A$)")
    .replace(/\\n(?=[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ0-9(\-*•])/g, "\n");
}

// 2. Auto-wrap un-delimited LaTeX in $...$ (ONLY called on prose/options before splitting $...$!)
function sanitizeMathAndSymbols(rawStr) {
  let s = cleanMathCorruptions(rawStr);
  if (s.indexOf("$") === -1 && /\\(?:begin|text|mathrm|dfrac|frac|sqrt|xrightarrow|xleftarrow|rightarrow|rightleftharpoons|rightleftarrows|uparrow|downarrow|Delta|alpha|beta|gamma|omega|Omega|pi|cdot|cdots|quad|qquad|times|le|ge|ne|approx|equiv|in|notin|subset|cup|cap|sum|int|lim|underbrace|overbrace)(?![a-zA-Z])/.test(s)) {
    const trimmed = s.trim();
    const firstBs = trimmed.indexOf("\\");
    const prefixBeforeBs = firstBs >= 0 ? trimmed.slice(0, firstBs) : trimmed;
    if (firstBs >= 0 && !/[À-ỹ]/.test(prefixBeforeBs)) {
      s = `$${trimmed}$`;
    } else {
      s = s
        .replace(/^(Không tuân theo quy luật định lượng trong\s+)([\s\S]+)$/, "$1$$$2$$")
        .replace(/^(Có giá trị bằng nghịch đảo của (?:tỉ số|biểu thức) trong\s+)([\s\S]+)$/, "$1$$$2$$")
        .replace(/^([\s\S]*?\bđược biểu diễn bởi\s+)([\s\S]+?)(\.?)$/, "$1$$$2$$$3")
        .replace(/^([\s\S]*?\bđược xác định bởi:\s+)([\s\S]+?)(\.?)$/, "$1$$$2$$$3")
        .replace(/^([\s\S]*?\bcó công thức\/quy tắc là:\s+)([\s\S]+?)(\.?)$/, "$1$$$2$$$3")
        .replace(/(\bthành\s+)((?:\\begin\{[\s\S]*?\\end\{[^}]+\}|[^\n]+?))(\s+thay vì\s+công thức đúng)/, "$1$$$2$$$3")
        .replace(/(\bđúng\s*\()((?:\\begin\{[\s\S]*?\\end\{[^}]+\}|[\s\S]+?))(\)\s*chứ không phải\s+)((?:\\begin\{[\s\S]*?\\end\{[^}]+\}|[\s\S]+?))(\.\s*Hãy|\.$|$)/, "$1$$$2$$$3$$$4$$$5");
    }
  }
  return s;
}

const LATEX_SYMBOLS = {
  "\\alpha": "α", "\\beta": "β", "\\gamma": "γ", "\\delta": "δ", "\\epsilon": "ε", "\\varepsilon": "ε",
  "\\zeta": "ζ", "\\eta": "η", "\\theta": "θ", "\\vartheta": "ϑ", "\\iota": "ι", "\\kappa": "κ",
  "\\lambda": "λ", "\\mu": "μ", "\\nu": "ν", "\\xi": "ξ", "\\pi": "π", "\\rho": "ρ",
  "\\sigma": "σ", "\\tau": "τ", "\\upsilon": "υ", "\\phi": "φ", "\\varphi": "φ", "\\chi": "χ",
  "\\psi": "ψ", "\\omega": "ω", "\\ell": "ℓ",
  "\\Gamma": "Γ", "\\Delta": "Δ", "\\Theta": "Θ", "\\Lambda": "Λ", "\\Xi": "Ξ", "\\Pi": "Π",
  "\\Sigma": "Σ", "\\Phi": "Φ", "\\Psi": "Ψ", "\\Omega": "Ω",
  "\\cdot": "·", "\\times": "×", "\\div": "÷", "\\pm": "±", "\\mp": "∓", "\\ast": "∗", "\\bullet": "•", "\\oslash": "⊘",
  "\\le": "≤", "\\leq": "≤", "\\ge": "≥", "\\geq": "≥", "\\ne": "≠", "\\neq": "≠",
  "\\approx": "≈", "\\equiv": "≡", "\\sim": "∼", "\\simeq": "≃", "\\cong": "≅", "\\propto": "∝", "\\ll": "≪", "\\gg": "≫",
  "\\infty": "∞", "\\partial": "∂", "\\nabla": "∇", "\\forall": "∀", "\\exists": "∃", "\\nexists": "∄",
  "\\in": "∈", "\\notin": "∉", "\\ni": "∋", "\\subset": "⊂", "\\supset": "⊃",
  "\\subseteq": "⊆", "\\supseteq": "⊇", "\\cup": "∪", "\\cap": "∩", "\\setminus": "∖",
  "\\emptyset": "∅", "\\varnothing": "∅", "\\mid": "∣", "\\nmid": "∤",
  "\\to": "→", "\\rightarrow": "→", "\\leftarrow": "←", "\\leftrightarrow": "↔",
  "\\longrightarrow": "⟶", "\\longleftarrow": "⟵", "\\longleftrightarrow": "⟷",
  "\\Rightarrow": "⇒", "\\Leftarrow": "⇐", "\\Leftrightarrow": "⇔", "\\Longrightarrow": "⟹", "\\Longleftrightarrow": "⟺",
  "\\iff": "⇔", "\\implies": "⇒",
  "\\mapsto": "↦", "\\uparrow": "↑", "\\downarrow": "↓", "\\upharpoonright": "↑",
  "\\rightleftharpoons": "⇌", "\\leftrightharpoons": "⇌", "\\rightleftarrows": "⇄",
  "\\perp": "⊥", "\\parallel": "∥", "\\nparallel": "∦", "\\angle": "∠", "\\widehat": "", "\\triangle": "△", "\\frown": "⌒",
  "\\circ": "°", "\\degree": "°", "\\deg": "°", "\\prime": "′",
  "\\dots": "…", "\\ldots": "…", "\\cdots": "⋯", "\\vdots": "⋮", "\\ddots": "⋱",
  "\\quad": " ", "\\qquad": "  ", "\\,": " ", "\\;": " ", "\\:": " ", "\\!": "", "\\ ": " ",
  "\\left": "", "\\right": "", "\\middle": "", "\\big": "", "\\Big": "", "\\bigg": "", "\\Bigg": "",
  "\\bigl": "", "\\bigr": "", "\\Bigl": "", "\\Bigr": "",
  "\\displaystyle": "", "\\textstyle": "", "\\scriptstyle": "",
  "\\sin": "sin", "\\cos": "cos", "\\tan": "tan", "\\cot": "cot", "\\arcsin": "arcsin", "\\arccos": "arccos", "\\arctan": "arctan",
  "\\ln": "ln", "\\log": "log", "\\lg": "lg", "\\lim": "lim", "\\max": "max", "\\min": "min", "\\gcd": "ƯCLN", "\\lcm": "BCNN",
  "\\int": "∫", "\\oint": "∮", "\\sum": "∑", "\\prod": "∏", "\\lightning": "⚡"
};

const MATHBB_MAP = { N: "ℕ", Z: "ℤ", Q: "ℚ", R: "ℝ", C: "ℂ", P: "ℙ" };
const MATHCAL_MAP = { E: "ℰ", L: "ℒ", F: "ℱ", H: "ℋ", M: "ℳ", B: "ℬ", P: "𝒫", C: "𝒞" };

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

function takeBracketed(s, pos) {
  while (pos < s.length && s[pos] === " ") pos++;
  if (s[pos] !== "[") return ["", pos];
  let depth = 0, i = pos;
  for (; i < s.length; i++) {
    if (s[i] === "\\" && i + 1 < s.length) { i++; continue; }
    if (s[i] === "[") depth++;
    else if (s[i] === "]") {
      depth--;
      if (depth === 0) return [s.slice(pos + 1, i), i + 1];
    }
  }
  return [s.slice(pos + 1), s.length];
}

function normalizeKatexInput(tex) {
  return cleanMathCorruptions(tex)
    .replace(/^\$+([\s\S]*?)\$+$/, "$1")
    .replace(/\\degree\b/g, "^\\circ")
    .replace(/\\[,;:!]\s*\^/g, "^")
    .replace(/\\[,;:!]\s*_/g, "_")
    .replace(/(\s)\^/g, "$1{}^")
    .replace(/^(\s*)\^/, "$1{}^")
    .replace(/^(\s*)_/g, "$1{}_")
    .replace(/([({\[=+\-*/<>|,;:])\s*\^/g, "$1{}^")
    .replace(/([({\[=+\-*/<>|,;:])\s*_/g, "$1{}_");
}

function renderLatexOffline(tex) {
  let s = cleanMathCorruptions(tex).replace(/^\$+([\s\S]*?)\$+$/, "$1").trim();
  if (!s) return "";

  const envStash = [];
  s = s.replace(/\\begin\{(cases|aligned|array|matrix|pmatrix|bmatrix|vmatrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
    body = body.replace(/^\s*\{[^}]*\}/, "");
    const rows = body.split(/\\\\/).map((r) => r.trim()).filter(Boolean);
    const renderedRows = rows.map((r) => {
      const cells = r.split("&").map((c) => renderLatexOffline(c.trim()));
      return `<span class="m-row">${cells.map((c) => `<span class="m-cell">${c}</span>`).join("")}</span>`;
    }).join("");
    let html;
    if (env === "cases") {
      html = `<span class="m-cases">{<span class="m-rows">${renderedRows}</span></span>`;
    } else {
      const lbr = env === "pmatrix" ? "(" : env === "bmatrix" ? "[" : env === "vmatrix" ? "|" : "";
      const rbr = env === "pmatrix" ? ")" : env === "bmatrix" ? "]" : env === "vmatrix" ? "|" : "";
      html = `<span class="m-matrix">${lbr}<span class="m-rows">${renderedRows}</span>${rbr}</span>`;
    }
    const tok = `\u0000E${envStash.length}\u0000`;
    envStash.push(html);
    return tok;
  });

  let out = "", i = 0;
  while (i < s.length) {
    if (s[i] === "\u0000") {
      const endN = s.indexOf("\u0000", i + 1);
      if (endN !== -1) {
        const idx = Number(s.slice(i + 2, endN));
        out += envStash[idx] || "";
        i = endN + 1;
        continue;
      }
    }
    if (s[i] === "\\") {
      const rest = s.slice(i);
      let m = rest.match(/^\\not\s*(\\[a-zA-Z]+|=|<|>)/);
      if (m) {
        const subTok = m[1];
        if (subTok === "\\vdots") out += "∤";
        else if (subTok === "\\in") out += "∉";
        else if (subTok === "\\subset") out += "⊄";
        else if (subTok === "\\equiv") out += "≢";
        else if (subTok === "=") out += "≠";
        else out += `<span style="text-decoration:line-through">${renderLatexOffline(subTok)}</span>`;
        i += m[0].length;
        continue;
      }
      m = rest.match(/^\\(d?frac|tfrac)(?![a-zA-Z])/);
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
      m = rest.match(/^\\sqrt(?![a-zA-Z])/);
      if (m) {
        let [rad, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-sqrt">√<span class="m-rad">${renderLatexOffline(rad)}</span></span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\(xrightarrow|xleftarrow)(?![a-zA-Z])/);
      if (m) {
        const isLeft = m[1] === "xleftarrow";
        let [bot, p1] = takeBracketed(s, i + m[0].length);
        let [top, p2] = takeBraced(s, p1);
        const arrowChar = isLeft ? "⟵" : "⟶";
        out += `<span class="m-over"><span class="m-top">${renderLatexOffline(top)}</span><span class="m-bot">${arrowChar}${bot ? ` <small>(${renderLatexOffline(bot)})</small>` : ""}</span></span>`;
        i = p2; continue;
      }
      m = rest.match(/^\\(overrightarrow|vec|overline|bar|widehat|hat|tilde|underline)(?![a-zA-Z])/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        const cls = (m[1] === "overrightarrow" || m[1] === "vec") ? "m-vec" : (m[1] === "widehat" || m[1] === "hat") ? "m-hat" : "m-bar";
        out += `<span class="${cls}">${renderLatexOffline(arg)}</span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\(text|textrm|textit|mathrm|textbf|mathbf|mathit|operatorname)(?![a-zA-Z])/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        const tag = (m[1] === "textbf" || m[1] === "mathbf") ? "strong" : "span";
        out += `<${tag} class="m-text">${renderLatexOffline(arg)}</${tag}>`;
        i = p1; continue;
      }
      m = rest.match(/^\\mathbb(?![a-zA-Z])/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-bb">${MATHBB_MAP[arg.trim()] || escapeHTML(arg)}</span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\mathcal(?![a-zA-Z])/);
      if (m) {
        let [arg, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-cal">${MATHCAL_MAP[arg.trim()] || escapeHTML(arg)}</span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\(overset|stackrel)(?![a-zA-Z])/);
      if (m) {
        let [top, p1] = takeBraced(s, i + m[0].length);
        let [bot, p2] = takeBraced(s, p1);
        out += `<span class="m-over"><span class="m-top">${renderLatexOffline(top)}</span><span class="m-bot">${renderLatexOffline(bot)}</span></span>`;
        i = p2; continue;
      }
      m = rest.match(/^\\underset(?![a-zA-Z])/);
      if (m) {
        let [bot, p1] = takeBraced(s, i + m[0].length);
        let [base, p2] = takeBraced(s, p1);
        out += `<span class="m-over"><span class="m-bot">${renderLatexOffline(base)}</span><span class="m-top">${renderLatexOffline(bot)}</span></span>`;
        i = p2; continue;
      }
      m = rest.match(/^\\(underbrace|overbrace)(?![a-zA-Z])/);
      if (m) {
        let [base, p1] = takeBraced(s, i + m[0].length);
        out += `<span class="m-brace">${renderLatexOffline(base)}</span>`;
        i = p1; continue;
      }
      m = rest.match(/^\\([a-zA-Z]+|[^a-zA-Z])/);
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
    if (s[i] === "-" && s[i + 1] === ">") {
      out += "→"; i += 2; continue;
    }
    if (s[i] === "<" && s[i + 1] === "-" && s[i + 2] === ">") {
      out += "⇌"; i += 3; continue;
    }
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
      const katexHtml = window.katex.renderToString(clean, {
        throwOnError: true,
        displayMode: !!displayMode,
        strict: false
      });
      if (katexHtml && katexHtml.indexOf("katex-error") === -1) {
        return katexHtml;
      }
    } catch (_) {}
  }
  const attr = escapeHTML(clean);
  const tag = displayMode ? "div" : "span";
  return `<${tag} class="m-math${displayMode ? " m-block" : ""}" data-latex="${attr}" data-tex="${attr}" data-display="${displayMode ? 1 : 0}">${renderLatexOffline(clean)}</${tag}>`;
}

function upgradeKatex(root) {
  if (!window.katex || typeof window.katex.renderToString !== "function") return;
  (root || document).querySelectorAll(".m-math[data-latex], .m-math[data-tex]").forEach((el) => {
    const rawAttr = el.getAttribute("data-latex") || el.getAttribute("data-tex");
    const tex = normalizeKatexInput(rawAttr);
    if (!tex) return;
    const isDisplay = el.classList.contains("m-block") || el.getAttribute("data-display") === "1";
    try {
      const katexHtml = window.katex.renderToString(tex, {
        throwOnError: true,
        displayMode: isDisplay,
        strict: false
      });
      if (katexHtml && katexHtml.indexOf("katex-error") === -1) {
        el.innerHTML = katexHtml;
        el.removeAttribute("data-latex");
        el.removeAttribute("data-tex");
      }
    } catch (_) {}
  });
  if (typeof drawMindmapConnections === "function") {
    requestAnimationFrame(drawMindmapConnections);
  }
}
window.addEventListener("load", () => upgradeKatex(document));
setTimeout(() => upgradeKatex(document), 300);
setTimeout(() => upgradeKatex(document), 1000);

function replaceBalancedInlineLatex(s, putFn, renderFn) {
  // First capture any standalone \begin{...}...\end{...} outside $...$
  s = s.replace(/\\begin\{(cases|aligned|array|matrix|pmatrix|bmatrix|vmatrix)\}[\s\S]*?\\end\{\1\}/g, (m) => {
    if (m.indexOf("\u0000") !== -1) return m;
    return putFn(renderFn(m, false));
  });

  // For any remaining un-delimited \cmd{...} outside placeholders, scan with balanced braces
  let out = "";
  let i = 0;
  while (i < s.length) {
    if (s[i] === "\u0000") {
      const endNull = s.indexOf("\u0000", i + 1);
      if (endNull !== -1) {
        out += s.slice(i, endNull + 1);
        i = endNull + 1;
        continue;
      }
    }
    if (s[i] === "\\") {
      const m = s.slice(i).match(/^\\(d?frac|tfrac|sqrt|overrightarrow|vec|widehat|overline|underline|triangle|angle|cdot|cdots|ldots|dots|quad|qquad|times|div|pm|mp|le|leq|ge|geq|ne|neq|approx|equiv|infty|in|notin|subset|subseteq|cup|cap|emptyset|varnothing|alpha|beta|gamma|delta|Delta|pi|omega|Omega|sigma|lambda|mu|theta|sin|cos|tan|cot|log|ln|lim|sum|int|underbrace|overbrace|overset|underset|mathbb|mathcal|mathrm|text|textbf|xrightarrow|xleftarrow|rightleftharpoons|leftrightharpoons|rightleftarrows|longrightarrow|Rightarrow|Leftrightarrow|uparrow|downarrow|vdots|circ|degree)(?![a-zA-Z])/);
      if (m) {
        let j = i;
        while (j < s.length) {
          if (s[j] === "\u0000") break;
          if (s[j] === "\\") {
            const cm = s.slice(j).match(/^\\[a-zA-Z]+/);
            if (cm) { j += cm[0].length; continue; }
            j += 2; continue;
          }
          if (s[j] === "{" || s[j] === "[") {
            const openCh = s[j];
            const closeCh = openCh === "{" ? "}" : "]";
            let depth = 0;
            while (j < s.length) {
              if (s[j] === "\\" && j + 1 < s.length) { j += 2; continue; }
              if (s[j] === openCh) depth++;
              else if (s[j] === closeCh) {
                depth--;
                if (depth === 0) { j++; break; }
              }
              j++;
            }
            continue;
          }
          if (/^[\s0-9a-zA-Z_^\-+=<>≤≥≠≈·×÷,;:()\/|]/.test(s[j])) {
            // Stop if we hit a Vietnamese word outside braces
            const restWord = s.slice(j).match(/^\s+([a-zA-ZÀ-ỹ]+)/);
            if (restWord && /[À-ỹ]/.test(restWord[1])) break;
            j++;
            continue;
          }
          break;
        }
        const token = s.slice(i, j).trimEnd();
        const trailingSpace = s.slice(i + token.length, j);
        out += putFn(renderFn(token, false)) + trailingSpace;
        i = j;
        continue;
      }
    }
    out += s[i];
    i++;
  }
  return out;
}

function formatInlineStyles(rawStr) {
  if (!rawStr) return "";
  const stash = [];
  const put = (html) => { const id = `\u0000M${stash.length}\u0000`; stash.push(html); return id; };

  let s = sanitizeMathAndSymbols(rawStr)
    .replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => put(renderMathToken(m, true)))
    .replace(/\\\[([\s\S]+?)\\\]/g, (_, m) => put(renderMathToken(m, true)))
    .replace(/\\\(([\s\S]+?)\\\)/g, (_, m) => put(renderMathToken(m, false)))
    .replace(/\$([^$]+?)\$/g, (_, m) => put(renderMathToken(m, false)));

  s = s.replace(/`([^`]+)`/g, (_, c) => put(`<code>${escapeHTML(c)}</code>`));

  if (/\\(begin|d?frac|tfrac|sqrt|overrightarrow|vec|widehat|triangle|angle|cdot|cdots|ldots|dots|quad|qquad|times|div|pm|le|leq|ge|geq|ne|neq|approx|equiv|infty|in|notin|subset|subseteq|cup|cap|emptyset|alpha|beta|gamma|delta|Delta|pi|omega|Omega|sigma|lambda|mu|theta|sin|cos|tan|cot|log|ln|lim|sum|int|underbrace|overbrace|overset|underset|mathbb|mathcal|mathrm|text|xrightarrow|xleftarrow|rightleftharpoons|rightleftarrows|vdots)(?![a-zA-Z])/.test(s)) {
    s = replaceBalancedInlineLatex(s, put, renderMathToken);
  }

  s = escapeHTML(s)
    .replace(/&lt;-&gt;/g, "⇌")
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
  const raw = sanitizeMathAndSymbols(str).trim();
  if (!raw) return "";
  if (raw.includes("$") || /\\\[|\\\(/.test(raw)) return formatInlineStyles(raw);
  if (/\\[a-zA-Z]+|[_^]\s*\{|[a-zA-Z0-9]\s*\^\s*[0-9a-zA-Z+-]/.test(raw)) {
    return renderMathToken(raw, !!displayMode);
  }
  return formatInlineStyles(raw);
}

window.HDLGMath = {
  inline: formatInlineStyles,
  formatInline: formatInlineStyles,
  formula: renderMathText,
  renderLatexToken: renderMathToken,
  upgrade: upgradeKatex,
  upgradeKatex: upgradeKatex,
  sanitize: sanitizeMathAndSymbols
};


function formatRichText(rawValue) {
  if (rawValue === null || rawValue === undefined) return "";

  if (Array.isArray(rawValue)) {
    return rawValue.map((item) => formatRichText(item)).join("");
  }

  const lines = sanitizeMathAndSymbols(rawValue).replace(/\r\n/g, "\n").split("\n");
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
  upgradeKatex(answers);
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
    const sourceList = bullets.length ? bullets : headings.length ? headings : rawLines.filter(Boolean);
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

  const appSource = lesson.real_life || lesson.application;
  const appTarget = lesson.real_life ? "realLifeSection" : "applicationSection";
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

/* =========================================================
   BẢNG ÁNH XẠ GAME THỰC TẾ (TRONG PUBLIC/GAMES/) CHO BÀI HỌC
========================================================= */
const HDLG_GAME_META = {
  "game_do_luong": {
    "file": "games/game_do_luong.html",
    "title": "Bé Đo Giỏi – Đo độ dài và Thời gian",
    "desc": "Thực hành đo độ dài, xem đồng hồ, tính thời gian và quy đổi đơn vị đo qua các thử thách trực quan."
  },
  "store_management": {
    "file": "games/store_management.html",
    "title": "Ông Chủ Tập Sự – Toán Kinh Tế, Hàm Số & Thống Kê",
    "desc": "Vận dụng phép tính, tỉ số phần trăm, phương trình, hệ phương trình, hàm số và thống kê để điều hành cửa hàng tối ưu lợi nhuận."
  },
  "function-challenge": {
    "file": "games/function-challenge.html",
    "title": "Trạm Điều Hành Đạo Hàm – Toán 11 (CT GDPT 2018)",
    "desc": "Khám phá ý nghĩa hình học và vật lí của đạo hàm, tiếp tuyến, vận tốc tức thời và quy tắc tính đạo hàm."
  },
  "game_ung_dung_dao_ham": {
    "file": "games/game_ung_dung_dao_ham.html",
    "title": "Biệt Đội Cực Trị – Ứng dụng Đạo hàm Khảo sát & Vẽ Đồ thị Hàm số",
    "desc": "Xét tính đơn điệu, tìm cực trị, giá trị lớn nhất – nhỏ nhất, đường tiệm cận và khảo sát đồ thị hàm số thực tế."
  },
  "game_toa_do_oxyz": {
    "file": "games/game_toa_do_oxyz.html",
    "title": "Đội Định Vị Hình Học – Vectơ & Phương pháp Tọa độ",
    "desc": "Vận dụng vectơ, tích vô hướng, hệ trục tọa độ và phương trình đường thẳng, mặt phẳng, mặt cầu trong định vị không gian."
  },
  "game_nguyen_ham": {
    "file": "games/game_nguyen_ham.html",
    "title": "Trạm Tích Lũy – Nguyên Hàm & Tích Phân Ứng Dụng",
    "desc": "Tính nguyên hàm, tích phân xác định, bài toán quãng đường s = ∫v(t)dt, diện tích hình phẳng và thể tích vật thể."
  },
  "game_on_tap_thpt": {
    "file": "games/game_on_tap_thpt.html",
    "title": "Mô Hình Hóa Toán THPT – Mũ Lôgarit, Thống Kê & Xác Suất Bayes",
    "desc": "Giải quyết các bài toán tối ưu thực tiễn, lãi kép mũ – lôgarit, khoảng biến thiên – phương sai và xác suất có điều kiện."
  },
  "game_dodai": {
    "file": "games/game_dodai.html",
    "title": "Thợ Mộc Học Việc – Đo Chiều Dài & Sai Số Phép Đo",
    "desc": "Chọn thước đo có GHĐ và ĐCNN phù hợp, đọc kết quả chính xác và đổi đơn vị đo chiều dài để gia công gỗ."
  },
  "game_khoiluong": {
    "file": "games/game_khoiluong.html",
    "title": "Tạp Hóa Cô Tám – Đo Khối Lượng & Quy Đổi Đơn Vị",
    "desc": "Sử dụng các loại cân, ước lượng khối lượng, đổi đơn vị g – kg – tạ – tấn và tính tải trọng xe chở hàng."
  },
  "game_nhietdo": {
    "file": "games/game_nhietdo.html",
    "title": "Ca Đêm Kho Lạnh – Đo Nhiệt Độ & Thang Nhiệt Độ Celsius – Kelvin",
    "desc": "Đọc nhiệt kế, quy đổi giữa thang nhiệt độ Celsius (°C), Fahrenheit (°F), Kelvin (K) và điều chỉnh kho bảo quản lạnh."
  },
  "game_luc": {
    "file": "games/game_luc.html",
    "title": "Cứu Hộ Đêm Mưa – Lực, Biểu Diễn Lực & Biến Dạng Lò Xo",
    "desc": "Xác định phương, chiều, độ lớn của lực kéo cứu hộ và độ giãn lò xo theo định luật Hooke."
  },
  "game_trong_luong_nang_luong": {
    "file": "games/game_trong_luong_nang_luong.html",
    "title": "Trọng Lực & Năng Lượng – Trọng lượng P = 10m & Bảo toàn năng lượng",
    "desc": "Tính trọng lượng P = 10m, phân tích sự truyền năng lượng, định luật bảo toàn năng lượng và chuyển động thiên thể."
  },
  "game_lucmasat": {
    "file": "games/game_lucmasat.html",
    "title": "Kiểm Định Lốp Xe – Lực Ma Sát & Lực Cản Môi Trường",
    "desc": "Khảo sát lực ma sát trượt, ma sát nghỉ, lực cản của nước/không khí và kiểm định độ bám đường an toàn."
  },
  "game_speed": {
    "file": "games/game_speed.html",
    "title": "Giao Hàng Đúng Giờ – Tốc Độ Chuyển Động v = s / t",
    "desc": "Tính tốc độ v = s/t, đọc đồ thị quãng đường – thời gian, đổi đơn vị km/h ↔ m/s và giữ khoảng cách an toàn giao thông."
  },
  "game_amthanh": {
    "file": "games/game_amthanh.html",
    "title": "Cảng Container Cảnh Báo – Sóng Âm, Độ To, Độ Cao & Phản Xạ Âm",
    "desc": "Điều chỉnh biên độ (độ to dB), tần số (độ cao Hz), tính khoảng cách bằng tiếng vang và chống ô nhiễm tiếng ồn."
  },
  "game_anhsang": {
    "file": "games/game_anhsang.html",
    "title": "Điện Mặt Trời – Ánh Sáng, Tia Sáng & Sự Phản Xạ Ánh Sáng",
    "desc": "Căn chỉnh góc tới i và góc phản xạ i' = i để điều hướng chùm tia sáng hội tụ về tấm pin mặt trời."
  },
  "game_guongphang": {
    "file": "games/game_guongphang.html",
    "title": "Gương An Ninh – Ảnh Của Vật Qua Gương Phẳng",
    "desc": "Dựng ảnh ảo qua gương phẳng, xác định vùng quan sát và bố trí gương cầu/gương phẳng tại khúc cua hầm xe."
  },
  "game_anhsangmau": {
    "file": "games/game_anhsangmau.html",
    "title": "Chiếu Sáng Đô Thị – Tán Sắc Ánh Sáng & Màu Sắc Các Vật",
    "desc": "Phân tích ánh sáng trắng qua lăng kính, phối hợp các ánh sáng màu cơ bản và khảo sát màu sắc vật dưới ánh sáng màu."
  },
  "game_namcham": {
    "file": "games/game_namcham.html",
    "title": "Nam Châm & Từ Trường – Cực Từ & Đường Sức Từ",
    "desc": "Xác định cực Bắc (N) – Nam (S) của nam châm, tương tác giữa các cực từ và hình dạng đường sức từ."
  },
  "game_nam_cham_dien": {
    "file": "games/game_nam_cham_dien.html",
    "title": "Nam Châm Điện & Từ Trường Trái Đất – La Bàn & Lực Từ F ∝ N·I",
    "desc": "Sử dụng la bàn định hướng theo từ trường Trái Đất và điều chỉnh số vòng dây N, dòng điện I của nam châm điện."
  },
  "simulation_classic:khoi-luong-rieng": {
    "file": "games/simulation_classic.html?topic=khoi-luong-rieng",
    "title": "Xưởng Đúc & Kiểm Định Vật Liệu – Khối Lượng Riêng D = m / V",
    "desc": "Đo khối lượng m và thể tích V bằng cân và bình chia độ để xác định khối lượng riêng D = m/V và trọng lượng riêng d = 10D."
  },
  "simulation:luc-day-archimedes": {
    "file": "games/simulation.html?topic=luc-day-archimedes",
    "title": "Bến Sông: Thuyền Chở Hàng – Lực Đẩy Archimedes FA = d · V",
    "desc": "Tính toán lực đẩy Archimedes FA = d·V và mớn nước của thuyền khi chở hàng qua sông nước ngọt và ra biển nước mặn."
  },
  "game_chat_luu": {
    "file": "games/game_chat_luu.html",
    "title": "Trung Tâm Thủy Lực – Áp Suất p = F / S, Áp Suất Chất Lỏng & Khí Quyển",
    "desc": "Khảo sát áp suất trên một bề mặt p = F/S, áp suất chất lỏng p = d·h, máy nén thủy lực và lực cản chất lưu."
  },
  "game_moment_luc_don_bay": {
    "file": "games/game_moment_luc_don_bay.html",
    "title": "Xưởng Đòn Bẩy – Moment Lực M = F · d & Quy Tắc Đòn Bẩy",
    "desc": "Vận dụng tác dụng làm quay của lực, tính moment lực M = F·d và điều kiện cân bằng đòn bẩy F₁·d₁ = F₂·d₂."
  },
  "game_dien": {
    "file": "games/game_dien.html",
    "title": "Thợ Điện Khu Phố – Sự Nhiễm Điện, Dòng Điện, Mạch Điện & Đo I, U",
    "desc": "Lắp mạch điện đơn giản, khảo sát các tác dụng của dòng điện và dùng ampe kế, vôn kế đo cường độ dòng điện I, hiệu điện thế U."
  },
  "game_nhietnang": {
    "file": "games/game_nhietnang.html",
    "title": "Chuyến Giao Nóng Mùa Đông – Năng Lượng Nhiệt, Truyền Nhiệt & Nở Vì Nhiệt",
    "desc": "Phân tích nội năng, 3 hình thức truyền nhiệt (dẫn nhiệt, đối lưu, bức xạ nhiệt) và sự nở vì nhiệt của chất rắn, lỏng, khí."
  },
  "game_congsuat": {
    "file": "games/game_congsuat.html",
    "title": "Tời Điện Nhà Phố – Công Cơ Học A = F · s & Công Suất P = A / t",
    "desc": "Tính công cơ học A = F·s và công suất P = A/t để vận hành hệ thống tời nâng vật liệu xây dựng an toàn, hiệu quả."
  },
  "game_co_nang_khuc_xa": {
    "file": "games/game_co_nang_khuc_xa.html",
    "title": "Năng Lượng & Ánh Sáng – Cơ Năng, Khúc Xạ Ánh Sáng & Phản Xạ Toàn Phần",
    "desc": "Khảo sát sự chuyển hóa động năng – thế năng, định luật khúc xạ ánh sáng n₁sin i = n₂sin r và góc giới hạn phản xạ toàn phần."
  },
  "game_quanghoc": {
    "file": "games/game_quanghoc.html",
    "title": "Góc Máy Nét Căng – Thấu Kính Hội Tụ, Thấu Kính Phân Kì & Kính Lúp",
    "desc": "Điều chỉnh tiêu cự f và khoảng cách vật d để tạo ảnh rõ nét qua thấu kính hội tụ, thấu kính phân kì và kính lúp."
  },
  "game_ohm": {
    "file": "games/game_ohm.html",
    "title": "Cứu Bảng Hiệu LED – Điện Trở & Định Luật Ohm I = U / R",
    "desc": "Tính toán điện trở dây dẫn R = ρℓ/S và chọn điện trở hạn dòng theo định luật Ohm I = U/R để bảo vệ mạch đèn LED."
  },
  "game_doanmachnoitiep": {
    "file": "games/game_doanmachnoitiep.html",
    "title": "Thợ Đèn Nối Tiếp – Đoạn Mạch Nối Tiếp (I = I₁ = I₂, Rtd = R₁ + R₂)",
    "desc": "Thiết kế và tính toán cường độ dòng điện, hiệu điện thế và điện trở tương đương trong đoạn mạch mắc nối tiếp."
  },
  "game_doanmachsongsong": {
    "file": "games/game_doanmachsongsong.html",
    "title": "Mạng Điện Nhà Mình – Đoạn Mạch Song Song (U = U₁ = U₂, 1/Rtd = 1/R₁ + 1/R₂)",
    "desc": "Lắp đặt và cân bằng tải cho mạng điện sinh hoạt mắc song song đảm bảo các thiết bị hoạt động đúng hiệu điện thế định mức."
  },
  "game_congsuatdien": {
    "file": "games/game_congsuatdien.html",
    "title": "Săn Watt – Năng Lượng Điện W = UIt, Công Suất P = UI & Định Luật Joule – Lenz",
    "desc": "Tính công suất tiêu thụ điện P = U·I = I²R, nhiệt lượng tỏa ra Q = I²Rt và số tiền điện tiêu thụ (kWh)."
  },
  "game_dientu": {
    "file": "games/game_dientu.html",
    "title": "Điện Về Bản – Cảm Ứng Điện Từ, Dòng Điện Xoay Chiều & Máy Biến Áp",
    "desc": "Khảo sát điều kiện xuất hiện dòng điện cảm ứng, nguyên tắc máy phát điện xoay chiều và truyền tải điện năng bằng máy biến áp."
  },
  "game_robot": {
    "file": "games/game_robot.html",
    "title": "Robot Giao Hàng – Độ Dịch Chuyển, Vận Tốc & Chuyển Động Thẳng Đều",
    "desc": "Lập trình lộ trình cho robot giao hàng bằng độ dịch chuyển d, vận tốc v và đồ thị độ dịch chuyển – thời gian (d – t)."
  },
  "game_giatoc": {
    "file": "games/game_giatoc.html",
    "title": "Đường Đua Neon – Gia Tốc, Chuyển Động Biến Đổi Đều, Rơi Tự Do & Chuyển Động Ném",
    "desc": "Tính gia tốc a = Δv/Δt, quãng đường s = v₀t + ½at², vận tốc v² - v₀² = 2as, sự rơi tự do và tầm bay xa của chuyển động ném."
  },
  "force_real_life_game": {
    "file": "games/force_real_life_game.html",
    "title": "Đêm Nhạc Hội Trường – Tổng Hợp Lực, Cân Bằng Lực & Lực Ma Sát Trên Mặt Nghiêng",
    "desc": "Phân tích lực kéo trên mặt phẳng nghiêng, tổng hợp hai lực đồng quy, cân bằng lực căng dây cáp và nguyên lý phanh ABS."
  },
  "game_newton": {
    "file": "games/game_newton.html",
    "title": "Trạm Hỏa Tinh – Ba Định Luật Newton, Trọng Lực & Lực Căng Dây",
    "desc": "Vận dụng quán tính (Định luật 1), gia tốc a = F/m (Định luật 2) và cặp lực – phản lực (Định luật 3 Newton) trong trạm vũ trụ."
  },
  "game_nang_luong": {
    "file": "games/game_nang_luong.html",
    "title": "Trạm Điều Phối Năng Lượng – Công A = F·s·cosα, Cơ Năng & Hiệu Suất",
    "desc": "Tính công cơ học, công suất, động năng Wđ = ½mv², thế năng Wt = mgh, định luật bảo toàn cơ năng và hiệu suất H."
  },
  "game_dong_luong": {
    "file": "games/game_dong_luong.html",
    "title": "Phòng Thí Nghiệm Va Chạm – Động Lượng p = mv & Định Luật Bảo Toàn Động Lượng",
    "desc": "Khảo sát xung lượng của lực F·Δt = Δp, định luật bảo toàn động lượng trong va chạm đàn hồi, va chạm mềm và chuyển động bằng phản lực."
  },
  "game_chuyen_dong_tron_lo_xo": {
    "file": "games/game_chuyen_dong_tron_lo_xo.html",
    "title": "Xưởng Cơ Học Lưu Động – Chuyển Động Tròn Đều, Lực Hướng Tâm, Moment Lực & Định Luật Hooke",
    "desc": "Tính tốc độ góc ω, gia tốc hướng tâm aht = v²/r, lực hướng tâm, quy tắc moment lực cân bằng vật rắn và lực đàn hồi F = k|Δℓ|."
  },
  "game_dao_dong": {
    "file": "games/game_dao_dong.html",
    "title": "Viện Nhịp Điệu – Dao Động Điều Hòa, Con Lắc, Năng Lượng & Cộng Hưởng",
    "desc": "Điều chỉnh biên độ A, tần số góc ω, pha ban đầu φ, chu kì con lắc lò xo – con lắc đơn và khảo sát hiện tượng cộng hưởng."
  },
  "game_song_co": {
    "file": "games/game_song_co.html",
    "title": "Viện Âm Vang – Sóng Cơ Học, Bước Sóng λ = v/f, Sóng Ngang & Sóng Dọc",
    "desc": "Đo bước sóng λ = v·T = v/f, tốc độ truyền sóng, độ lệch pha và sự truyền năng lượng của sóng cơ học."
  },
  "game_song_dien_tu_giao_thoa_tu_dien": {
    "file": "games/game_song_dien_tu_giao_thoa_tu_dien.html",
    "title": "Đội Săn Sóng – Sóng Điện Từ, Giao Thoa Sóng Cơ, Giao Thoa Ánh Sáng Young & Sóng Dừng",
    "desc": "Xác định cực đại – cực tiểu giao thoa sóng cơ, khoảng vân giao thoa ánh sáng i = λD/a, điều kiện sóng dừng và phổ sóng điện từ."
  },
  "game_dien_truong": {
    "file": "games/game_dien_truong.html",
    "title": "Xưởng Tia Lửa – Định Luật Coulomb & Cường Độ Điện Trường E = k|Q|/r²",
    "desc": "Tính lực tương tác tĩnh điện Coulomb F = k|q₁q₂|/r², vectơ cường độ điện trường và nguyên lý chồng chất điện trường."
  },
  "game_dien_truong_deu": {
    "file": "games/game_dien_truong_deu.html",
    "title": "Phòng Lái Tia – Điện Trường Đều E = U/d & Quỹ Đạo Hạt Mang Điện",
    "desc": "Điều khiển hiệu điện thế U giữa hai bản phẳng song song để lái chùm hạt mang điện chuyển động theo quỹ đạo parabol trúng đích."
  },
  "game_dien_the": {
    "file": "games/game_dien_the.html",
    "title": "Biệt Đội Electron-Volt – Thế Năng Điện, Điện Thế, Hiệu Điện Thế & Tụ Điện W = ½CU²",
    "desc": "Tính công của lực điện A = qEd = qU, điện thế V, điện dung của tụ điện C = Q/U và năng lượng điện trường trong tụ điện."
  },
  "game_dong_dien": {
    "file": "games/game_dong_dien.html",
    "title": "Xưởng Mạch Đồng – Cường Độ Dòng Điện I = Snve, Định Luật Ohm Toàn Mạch I = E/(R+r)",
    "desc": "Khảo sát dòng điện không đổi, sự phụ thuộc điện trở vào nhiệt độ, suất điện động E, định luật Ohm toàn mạch và đo E, r của nguồn điện."
  },
  "game_vat_ly_nhiet_khi_ly_tuong": {
    "file": "games/game_vat_ly_nhiet_khi_ly_tuong.html",
    "title": "Biệt Đội Nhiệt Động – Vật Lí Nhiệt (ΔU = A+Q, c, λ, L) & Khí Lí Tưởng (pV = nRT)",
    "desc": "Thực hành đo nhiệt dung riêng c, nhiệt nóng chảy riêng λ, nhiệt hóa hơi riêng L và kiểm nghiệm định luật Boyle, Charles, phương trình pV = nRT."
  },
  "game_tu_truong": {
    "file": "games/game_tu_truong.html",
    "title": "Viện Nam Châm – Từ Trường, Cảm Ứng Từ B & Lực Từ F = BILsinθ",
    "desc": "Xác định quy tắc bàn tay trái, độ lớn lực từ F = BILsinθ tác dụng lên đoạn dây dẫn mang dòng điện và cân từ trường."
  },
  "game_cam_ung_dien_tu": {
    "file": "games/game_cam_ung_dien_tu.html",
    "title": "Trạm Cảm Ứng – Từ Thông Φ = NBScosα, Định Luật Faraday & Định Luật Lenz",
    "desc": "Tính từ thông Φ và suất điện động cảm ứng e_c = -ΔΦ/Δt khi cho khung dây quay hoặc dịch chuyển trong từ trường."
  },
  "game_mach_xoay_chieu": {
    "file": "games/game_mach_xoay_chieu.html",
    "title": "Đội Điều Độ Xoay Chiều – Dòng Điện Xoay Chiều, Giá Trị Hiệu Dụng & Hệ Số Công Suất cosφ",
    "desc": "Tính giá trị hiệu dụng I = I₀/√2, U = U₀/√2, chu kì, tần số và công suất tiêu thụ P = UIcosφ của mạch điện xoay chiều."
  },
  "game_mach_rlc": {
    "file": "games/game_mach_rlc.html",
    "title": "Trạm Dò Sóng – Mạch RLC Nối Tiếp, Cộng Hưởng Điện, Máy Biến Áp & Sóng Điện Từ",
    "desc": "Điều chỉnh tổng trở Z, tần số cộng hưởng điện ZL = ZC, tỉ số máy biến áp U₁/U₂ = N₁/N₂ và giảm hao phí truyền tải điện năng."
  },
  "game_hat_nhan": {
    "file": "games/game_hat_nhan.html",
    "title": "Trạm Đồng Vị – Cấu Trúc Hạt Nhân, Phản Ứng Phân Hạch – Nhiệt Hạch & Định Luật Phóng Xạ",
    "desc": "Cân bằng phương trình phản ứng hạt nhân, tính chu kì bán rã T, độ phóng xạ H = λN và ứng dụng đồng vị phóng xạ an toàn."
  },
  "game_thuyet_tuong_doi": {
    "file": "games/game_thuyet_tuong_doi.html",
    "title": "Trạm Ánh Sáng – Hệ Thức Einstein E = mc², Độ Hụt Khối Δm & Năng Lượng Liên Kết",
    "desc": "Tính độ hụt khối Δm, năng lượng liên kết Wlk = Δm·c², năng lượng liên kết riêng và hệ thức tương đối tính Einstein."
  },
  "game_quang_dien": {
    "file": "games/game_quang_dien.html",
    "title": "Xưởng Photon – Lượng Tử Ánh Sáng ε = hf, Hiện Tượng Quang Điện & Mẫu Nguyên Tử Bohr",
    "desc": "Khảo sát năng lượng photon ε = hc/λ, giới hạn quang điện λ₀ và sự chuyển mức năng lượng electron trong nguyên tử."
  }
};

const EXACT_GAME_RULES = [["physics", 6, "bài 1: đo chiều dài", "game_dodai"], ["physics", 6, "bài 2: đo khối lượng", "game_khoiluong"], ["physics", 6, "bài 3: đo thời gian", "game_do_luong"], ["physics", 6, "bài 4: thang nhiệt độ celsius", "game_nhietdo"], ["physics", 6, "bài 7: biến dạng của lò xo", "game_luc"], ["physics", 6, "bài 8: trọng lực và đơn vị lực", "game_trong_luong_nang_luong"], ["physics", 6, "bài 10: lực ma sát và lực cản", "game_lucmasat"], ["physics", 6, "bài 13: chuyển động nhìn thấy của mặt trời", "game_anhsang"], ["physics", 7, "bài 1: tốc độ chuyển động", "game_speed"], ["physics", 7, "bài 5: mô tả sóng âm", "game_amthanh"], ["physics", 7, "bài 9: sự phản xạ ánh sáng", "game_anhsang"], ["physics", 7, "bài 10: ảnh của vật qua gương phẳng", "game_guongphang"], ["physics", 7, "bài 11: nam châm", "game_namcham"], ["physics", 7, "bài 14: nam châm điện", "game_nam_cham_dien"], ["physics", 8, "bài 1: khối lượng riêng", "simulation_classic:khoi-luong-rieng"], ["physics", 8, "bài 3: tác dụng của chất lỏng lên vật đặt trong nó", "simulation:luc-day-archimedes"], ["physics", 8, "bài 5: áp suất chất lỏng", "game_chat_luu"], ["physics", 8, "bài 7: đòn bẩy và ứng dụng", "game_moment_luc_don_bay"], ["physics", 8, "bài 10: mạch điện đơn giản", "game_dien"], ["physics", 8, "bài 13: sự truyền nhiệt", "game_nhietnang"], ["physics", 9, "bài 1: công và công suất", "game_congsuat"], ["physics", 9, "bài 3: khúc xạ ánh sáng", "game_co_nang_khuc_xa"], ["physics", 9, "bài 5: tán sắc ánh sáng", "game_anhsangmau"], ["physics", 9, "bài 6: thấu kính hội tụ", "game_quanghoc"], ["physics", 9, "bài 8: điện trở. định luật ohm", "game_ohm"], ["physics", 9, "bài 9: đoạn mạch nối tiếp", "game_doanmachnoitiep"], ["physics", 9, "bài 10: đoạn mạch song song", "game_doanmachsongsong"], ["physics", 9, "bài 11: năng lượng điện và công suất điện", "game_congsuatdien"], ["physics", 9, "bài 12: cảm ứng điện từ", "game_dientu"], ["physics", 9, "bài 16: năng lượng tái tạo", "game_nang_luong"], ["physics", 10, "bài 3: thực hành tính sai số", "game_dodai"], ["physics", 10, "bài 4: độ dịch chuyển", "game_robot"], ["physics", 10, "bài 7: gia tốc", "game_giatoc"], ["physics", 10, "bài 11: tổng hợp và phân tích lực", "force_real_life_game"], ["physics", 10, "bài 12: định luật 1 và định luật 2 newton", "game_newton"], ["physics", 10, "bài 16: lực cản và lực nâng", "game_chat_luu"], ["physics", 10, "bài 19: cơ năng và định luật bảo toàn cơ năng", "game_nang_luong"], ["physics", 10, "bài 20: động lượng", "game_dong_luong"], ["physics", 10, "bài 26: định luật hooke", "game_chuyen_dong_tron_lo_xo"], ["physics", 11, "bài 1: dao động điều hòa", "game_dao_dong"], ["physics", 11, "bài 6: mô tả sóng", "game_song_co"], ["physics", 11, "bài 9: giao thoa sóng cơ", "game_song_dien_tu_giao_thoa_tu_dien"], ["physics", 11, "bài 13: khái niệm điện trường", "game_dien_truong"], ["physics", 11, "bài 14: điện trường đều", "game_dien_truong_deu"], ["physics", 11, "bài 16: điện thế và hiệu điện thế", "game_dien_the"], ["physics", 11, "bài 21: định luật ohm cho toàn mạch", "game_dong_dien"], ["physics", 12, "bài 10: phương trình trạng thái của khí lí tưởng", "game_vat_ly_nhiet_khi_ly_tuong"], ["physics", 12, "bài 13: cảm ứng từ và lực từ", "game_tu_truong"], ["physics", 12, "bài 14: từ thông. hiện tượng cảm ứng điện từ", "game_cam_ung_dien_tu"], ["physics", 12, "bài 15: đại cương về dòng điện xoay chiều", "game_mach_xoay_chieu"], ["physics", 12, "bài 16: máy biến áp", "game_mach_rlc"], ["physics", 12, "bài 18: hệ thức einstein", "game_thuyet_tuong_doi"], ["physics", 12, "bài 19: phản ứng hạt nhân", "game_hat_nhan"], ["math", 1, "đơn vị đo độ dài (xăng-ti-mét)", "game_do_luong"], ["math", 2, "bài 15: ki-lô-gam", "game_khoiluong"], ["math", 5, "bài 59: vận tốc", "game_speed"], ["math", 9, "giải hệ hai phương trình bậc nhất", "store_management"], ["math", 11, "định nghĩa và ý nghĩa của đạo hàm", "function-challenge"], ["math", 12, "tính đơn điệu và cực trị", "game_ung_dung_dao_ham"], ["math", 12, "nguyên hàm", "game_nguyen_ham"], ["math", 12, "hệ trục tọa độ trong không gian", "game_toa_do_oxyz"], ["math", 12, "xác suất có điều kiện", "game_on_tap_thpt"]];
function chooseLessonGameKey(subj, gradeVal, topicVal, titleVal) {
  const s = String(subj || "math").toLowerCase();
  const g = Number(gradeVal || 0);
  const ti = String(titleVal || "").trim().toLowerCase();
  for (const [rSubj, rGrade, rSub, rGame] of EXACT_GAME_RULES) {
    if (s === rSubj && g === rGrade && ti.includes(rSub)) return rGame;
  }
  return null;
}

function resolveLessonGameInfo(lesson, subjFallback, gradeFallback) {
  if (!lesson) return null;
  const s = String(lesson.subject || subjFallback || "math").toLowerCase();
  const g = Number(lesson.grade || gradeFallback || 10);
  const key = chooseLessonGameKey(s, g, lesson.topic, lesson.title);
  if (!key || !HDLG_GAME_META[key]) return null;
  const meta = HDLG_GAME_META[key];
  const lid = encodeURIComponent(lesson.id || "");
  let url = meta.file;
  if (url.includes("?")) {
    url += `&lesson_id=${lid}`;
  } else {
    url += `?lesson_id=${lid}`;
  }
  return {
    game_type: key,
    game_title: meta.title,
    game_description: meta.desc,
    url: url
  };
}

window.HDLGResolveGame = resolveLessonGameInfo;

function renderGame(lesson) {
  if (!gameDescription || !gameButton || !noGame) return;

  const gInfo = resolveLessonGameInfo(lesson, subject, lesson.grade || gradeFromUrl);
  if (!gInfo) {
    gameDescription.textContent = "";
    gameButton.style.display = "none";
    noGame.classList.remove("hidden");
    return;
  }

  lesson.game_type = gInfo.game_type;
  lesson.game_title = gInfo.game_title;
  lesson.game_description = gInfo.game_description;

  gameDescription.innerHTML =
    `<strong style="display:block;font-size:16.5px;color:#fde047;margin-bottom:6px;">🎯 ${escapeHTML(gInfo.game_title)}</strong>` +
    `<span>${escapeHTML(gInfo.game_description)}</span>`;

  gameButton.style.display = "inline-flex";
  gameButton.style.alignItems = "center";
  gameButton.style.gap = "8px";
  gameButton.textContent = "🚀 Bắt đầu trải nghiệm";
  gameButton.onclick = function () {
    window.location.href = gInfo.url;
  };
  noGame.classList.add("hidden");
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
    upgrade: upgradeKatex,
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
   TÁCH RIÊNG KIẾN THỨC & CÔNG THỨC CHO TỪNG BÀI HỌC
   (Đảm bảo 1 bài học KHÔNG BAO GIỜ lẫn công thức của bài khác cùng chương)
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
  const validSubs = [];
  matches.forEach((item, idx) => {
    const endIdx = idx + 1 < matches.length ? matches[idx + 1].startIdx : text.length;
    const body = text.slice(item.bodyStart, endIdx).trim();
    const bodyLines = body.split("\n").map((l) => l.trim()).filter(Boolean);
    if (!bodyLines.length && /luyện tập chung|bài tập cuối chương/i.test(item.heading)) {
      return;
    }
    const firstBullet = bodyLines.map((l) => l.replace(/^[-*•+]\s+/, "").trim()).find(Boolean) || "";
    validSubs.push({
      subIndex: validSubs.length,
      title: item.heading.replace(/^(Bài\s+\d+)\.\s*/, "$1: "),
      description: firstBullet.replace(/\*\*/g, "").slice(0, 150),
      body: body,
      bodyLines: bodyLines,
      theory: `### ${item.heading.replace(/^(Bài\s+\d+)\.\s*/, "$1: ")}\n${body}`
    });
  });
  return validSubs.length >= 2 ? validSubs : [];
}

function extractFormulasStrictlyForSubLesson(subSection) {
  const items = [];
  subSection.bodyLines.forEach((rawLine) => {
    const line = rawLine.replace(/^[-*•+]\s+/, "").trim();
    if (!line) return;
    const boldMatch = line.match(/^\*\*([^*]{2,70})\*\*\s*[:–-]?\s*(.+)$/);
    if (boldMatch) {
      items.push({
        name: boldMatch[1].trim(),
        formula: boldMatch[2].trim(),
        note: ""
      });
    } else if (line.includes("$")) {
      const colonIdx = line.indexOf(":");
      if (colonIdx > 2 && colonIdx < 55 && !line.slice(0, colonIdx).includes("$")) {
        items.push({
          name: line.slice(0, colonIdx).replace(/\*\*/g, "").trim(),
          formula: line.slice(colonIdx + 1).trim(),
          note: ""
        });
      } else {
        items.push({
          name: `Quy tắc ${items.length + 1}`,
          formula: line,
          note: ""
        });
      }
    }
  });

  if (!items.length && subSection.bodyLines.length) {
    subSection.bodyLines.slice(0, 3).forEach((l, i) => {
      items.push({
        name: `Nội dung trọng tâm ${i + 1}`,
        formula: l.replace(/^[-*•+]\s+/, "").trim(),
        note: ""
      });
    });
  }

  const shortTitle = subSection.title.replace(/^Bài\s+\d+[:.]?\s*/i, "").trim();
  return [{
    category: `Công thức & Quy tắc trọng tâm — ${shortTitle}`,
    items: items
  }];
}

function applyVirtualSubLessonIfAny(rawLesson) {
  const subSections = splitCombinedTheorySections(rawLesson.theory);
  if (!subSections.length) return rawLesson;

  // Nếu bản ghi trong DB vẫn là bản ghi gộp nhiều bài, tự động chọn đúng bài theo ?sub=N (mặc định bài 0)
  const targetIdx = (subIndexFromUrl !== null && !isNaN(subIndexFromUrl) && subSections[subIndexFromUrl])
    ? subIndexFromUrl
    : 0;
  const chosen = subSections[targetIdx];
  const totalSubs = subSections.length;

  const clone = Object.assign({}, rawLesson);
  clone._virtualSiblings = subSections.map((s) => ({
    id: rawLesson.id,
    subIndex: s.subIndex,
    title: s.title,
    topic: rawLesson.topic,
    grade: rawLesson.grade
  }));
  clone._currentSubIndex = targetIdx;

  clone.context_title = rawLesson.context_title && /^(Chương|Chủ đề)/i.test(rawLesson.context_title)
    ? rawLesson.context_title
    : rawLesson.title;
  clone.title = chosen.title;
  if (chosen.description) clone.description = chosen.description;
  clone.theory = chosen.theory;

  // Tách riêng Định nghĩa, Yêu cầu cần đạt và Công thức của RIÊNG bài học này (không lấy của bài khác trong chương!)
  clone.definition = chosen.bodyLines.slice(0, 2).join("\n") || chosen.body;
  clone.formulas = extractFormulasStrictlyForSubLesson(chosen);
  clone.requirements = chosen.bodyLines.slice(0, 3).map((l) =>
    "Nắm vững và vận dụng: " + l.replace(/^[-*•+]\s+/, "").replace(/\*\*/g, "").trim()
  );

  if (Array.isArray(rawLesson.quiz) && rawLesson.quiz.length >= totalSubs * 2) {
    const chunkSize = Math.max(3, Math.ceil(rawLesson.quiz.length / totalSubs));
    const startQ = Math.min(targetIdx * Math.floor(rawLesson.quiz.length / totalSubs), Math.max(0, rawLesson.quiz.length - chunkSize));
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
    const cacheKey = `hdlg_v9_lessons_${subject}_${g}`;
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
  const activeSubIdx = typeof lesson._currentSubIndex === "number" ? lesson._currentSubIndex : subIndexFromUrl;

  const listHtml = siblings.map((item, idx) => {
    const isCurrent = typeof item.subIndex === "number"
      ? item.subIndex === activeSubIdx
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
    chapterSidebarProgress.textContent = `Bài ${currentIdx >= 0 ? currentIdx + 1 : 1}/${siblings.length}`;
  }

  // Cuộn mượt mục bài đang học vào tầm nhìn trong danh sách bên trái
  requestAnimationFrame(() => {
    const activeLink = chapterLessonsList.querySelector(".ch-lesson-link.active");
    if (activeLink && typeof activeLink.scrollIntoView === "function") {
      activeLink.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  });

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

  // Nếu context_title là tên Chương (dùng để gom nhóm Chương), ẩn hộp context chung của cả chương
  // để trang bài học chỉ hiển thị đúng kiến thức của riêng bài học đó.
  if (!chapName && (lesson.context || lesson.context_title)) {
    if (contextTitle) {
      contextTitle.textContent = lesson.context_title || "Bối cảnh thực tế";
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
    const cached = sessionStorage.getItem(`hdlg_v9_lesson_${lessonId}`);
    if (cached) {
      try { lesson = JSON.parse(cached); } catch (_) {}
    }
    if (!lesson || lesson.id === undefined) {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Không thể tải bài học. HTTP ${response.status}`);
      }
      lesson = await response.json();
      try { sessionStorage.setItem(`hdlg_v9_lesson_${lessonId}`, JSON.stringify(lesson)); } catch (_) {}
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

// ===== Đồng bộ khung Tài khoản người chơi & Sự kiện Click =====
(function accountHudGrade() {
  const card = document.getElementById("playerCard") || document.querySelector(".player");
  if (card) {
    card.style.cursor = "pointer";
    card.title = "Tài khoản của tôi";
    card.addEventListener("click", () => {
      if (window.HDLG && typeof HDLG.showAccount === "function") {
        HDLG.showAccount();
      }
    });
  }

  function renderPlayer(d) {
    if (!d) return;
    const nameEl = document.getElementById("playerName") || document.querySelector(".player-info strong");
    const lvlEl = document.getElementById("playerLevel") || document.querySelector(".player .level");
    const barEl = document.getElementById("playerXpBar") || document.getElementById("xpProgress");
    const txtEl = document.getElementById("playerXpText");
    const av = document.getElementById("playerAvatar") || document.querySelector(".player-avatar");

    const level = d.level || (Math.floor((d.xp || 0) / 100) + 1);
    const inLevel = d.inLevel !== undefined ? d.inLevel : ((d.xp || 0) % 100);

    if (nameEl) nameEl.textContent = d.name || "Tên người chơi";
    if (lvlEl) lvlEl.textContent = "Lv." + level;
    if (barEl) barEl.style.width = inLevel + "%";
    if (txtEl) txtEl.textContent = inLevel + "/100";

    if (av) {
      if (d.photo) {
        const cur = av.querySelector("img");
        if (cur && cur.getAttribute("src") === d.photo) return;
        av.innerHTML = "";
        const img = document.createElement("img");
        img.src = d.photo;
        img.referrerPolicy = "no-referrer";
        img.alt = "";
        img.style.cssText = "width:100%;height:100%;border-radius:50%;object-fit:cover";
        av.appendChild(img);
      } else if (d.name) {
        av.textContent = d.name.charAt(0).toUpperCase();
      }
    }
  }

  window.addEventListener("hdlg:update", e => renderPlayer(e.detail));
  if (window.HDLG && typeof HDLG.getState === "function") renderPlayer(HDLG.getState());
  if (window.HDLG && HDLG.ready) {
    HDLG.ready.then(() => {
      if (typeof HDLG.getState === "function") renderPlayer(HDLG.getState());
      else if (HDLG.user) renderPlayer(HDLG.user);
    });
  }
})();

function refreshRealProgress() {
  if (!lessons.length) return;
  renderPage();
}
window.addEventListener("hdlg:update", refreshRealProgress);
window.addEventListener("pageshow", refreshRealProgress);
if (window.HDLG && HDLG.ready && typeof HDLG.ready.then === "function") {
  HDLG.ready.then(refreshRealProgress);
}
