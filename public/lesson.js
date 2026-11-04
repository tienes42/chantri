function normalizeKatexInput(tex) {
  let s = unescapeHTML(String(tex || "").trim());
  if (/&(?:amp|lt|gt|quot|#039|#39|apos);/.test(s)) s = unescapeHTML(s);
  s = s.replace(/\\[,;:!]\s*([\^_])/g, "$1");
  s = s.replace(/(^|[+\-=(,;:\[]|\\(?:rightarrow|to|Rightarrow|Leftrightarrow|longrightarrow|mapsto|times|cdot|pm|quad|qquad))\s*([\^_])/g, "$1{}$2");
  return s;
}

function unescapeHTML(str) {
  if (str === null || str === undefined) return "";
  return String(str)
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#039;/g, "'")
    .replace(/&#39;/g, "'")
    .replace(/&apos;/g, "'");
}

/* =========================================================
   LESSON.JS — SÁCH HỌC VIỆN NỔI 2.5D & ĐỌC HIỂU CHUYÊN SÂU
   Dùng chung cho: Math, Physics, Chemistry và các môn khác
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

// Chương trình SGK mới: Yêu cầu cần đạt + bộ 10 câu hỏi 3 mức độ
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
   ESCAPE HTML & BỘ DỰNG CÔNG THỨC TOÁN - LÝ - HÓA (KaTeX + Offline)
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

const SUP_CHAR_MAP = {
  "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
  "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
  "ⁿ": "n", "ᵐ": "m", "⁺": "+", "⁻": "−"
};
const SUB_CHAR_MAP = {
  "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
  "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
  "₊": "+", "₋": "−"
};

const LATEX_SYMBOLS = {
  "\\cdot": "·", "\\times": "×", "\\div": ":", "\\pm": "±", "\\mp": "∓",
  "\\le": "≤", "\\leq": "≤", "\\ge": "≥", "\\geq": "≥",
  "\\ne": "≠", "\\neq": "≠", "\\approx": "≈", "\\equiv": "≡",
  "\\sim": "∼", "\\simeq": "≃", "\\cong": "≅",
  "\\in": "∈", "\\notin": "∉", "\\subset": "⊂", "\\subseteq": "⊆", "\\supset": "⊃", "\\supseteq": "⊇", "\\setminus": "\\", "\\int": "∫", "\\sum": "∑", "\\prod": "∏",
  "\\cup": "∪", "\\cap": "∩", "\\emptyset": "∅", "\\varnothing": "∅",
  "\\Rightarrow": "⇒", "\\Leftarrow": "⇐", "\\Leftrightarrow": "⇔",
  "\\rightarrow": "→", "\\to": "→", "\\leftarrow": "←", "\\mapsto": "↦",
  "\\forall": "∀", "\\exists": "∃",
  "\\perp": "⊥", "\\parallel": "∥", "\\triangle": "△", "\\angle": "∠",
  "\\pi": "π", "\\alpha": "α", "\\beta": "β", "\\gamma": "γ", "\\delta": "δ",
  "\\Delta": "Δ", "\\epsilon": "ε", "\\varepsilon": "ε", "\\theta": "θ",
  "\\lambda": "λ", "\\mu": "μ", "\\rho": "ρ", "\\sigma": "σ", "\\tau": "τ",
  "\\varphi": "φ", "\\phi": "ϕ", "\\omega": "ω", "\\Omega": "Ω",
  "\\infty": "∞", "\\dots": "…", "\\ldots": "…", "\\cdots": "⋯",
  "\\circ": "°", "\\%": "%", "\\{": "{", "\\}": "}", "\\,": " ", "\\;": " ", "\\:": " ", "\\!": ""
};

function takeBraced(s, pos) {
  while (pos < s.length && s[pos] === " ") pos++;
  if (pos >= s.length || s[pos] !== "{") return null;
  let depth = 0;
  let start = pos + 1;
  for (let i = pos; i < s.length; i++) {
    if (s[i] === "\\") { i++; continue; }
    if (s[i] === "{") depth++;
    else if (s[i] === "}") {
      depth--;
      if (depth === 0) return { content: s.slice(start, i), next: i + 1 };
    }
  }
  return { content: s.slice(start), next: s.length };
}

function takeBracketed(s, pos) {
  while (pos < s.length && s[pos] === " ") pos++;
  if (pos >= s.length || s[pos] !== "[") return null;
  let depth = 0;
  let start = pos + 1;
  for (let i = pos; i < s.length; i++) {
    if (s[i] === "[") depth++;
    else if (s[i] === "]") {
      depth--;
      if (depth === 0) return { content: s.slice(start, i), next: i + 1 };
    }
  }
  return null;
}

function renderLatexOffline(tex) {
  if (!tex) return "";
  let s = String(tex).trim()
    .replace(/\\left\s*([(\[\{|])/g, "$1")
    .replace(/\\right\s*([)\]\}|])/g, "$1")
    .replace(/\\left\s*\\\{/g, "{")
    .replace(/\\right\s*\\\}/g, "}")
    .replace(/\\mathbb\{N\}\^\*/g, "ℕ*")
    .replace(/\\mathbb\{N\}/g, "ℕ")
    .replace(/\\mathbb\{Z\}/g, "ℤ")
    .replace(/\\mathbb\{Q\}/g, "ℚ")
    .replace(/\\mathbb\{R\}/g, "ℝ").replace(/\\mathbb\{C\}/g, "ℂ").replace(/\\not\\subset/g, "⊄").replace(/\\not\\in/g, "∉");

  s = s.replace(/\\begin\{cases\}([\s\S]*?)\\end\{cases\}/g, (_, body) => {
    const rows = body.split(/\\\\/).map(r => r.trim()).filter(Boolean);
    const rowsHtml = rows.map(r => {
      const cols = r.split("&").map(c => renderLatexOffline(c.trim()));
      return `<span class="m-cases-row">${cols.join(" &nbsp; ")}</span>`;
    }).join("");
    return `\x00CASES_START\x00${rowsHtml}\x00CASES_END\x00`;
  });
  let out = "";
  let i = 0;
  while (i < s.length) {
    const ch = s[i];
    if (ch === "\\") {
      const mCmd = s.slice(i).match(/^\\([a-zA-Z]+|[{},;:%!])/);
      if (mCmd) {
        const fullCmd = "\\" + mCmd[1];
        const nextPos = i + fullCmd.length;
        if (fullCmd === "\\frac" || fullCmd === "\\dfrac" || fullCmd === "\\tfrac") {
          const num = takeBraced(s, nextPos);
          if (num) {
            const den = takeBraced(s, num.next);
            if (den) {
              out += `<span class="m-frac"><span class="m-num">${renderLatexOffline(num.content)}</span><span class="m-den">${renderLatexOffline(den.content)}</span></span>`;
              i = den.next;
              continue;
            }
          }
        } else if (fullCmd === "\\sqrt") {
          const opt = takeBracketed(s, nextPos);
          const radPos = opt ? opt.next : nextPos;
          const rad = takeBraced(s, radPos);
          if (rad) {
            const rootHtml = opt ? `<sup class="m-root">${renderLatexOffline(opt.content)}</sup>` : "";
            out += `<span class="m-sqrt">${rootHtml}<span class="m-rad">√</span><span class="m-radicand">${renderLatexOffline(rad.content)}</span></span>`;
            i = rad.next;
            continue;
          }
        } else if (fullCmd === "\\widehat" || fullCmd === "\\hat") {
          const arg = takeBraced(s, nextPos);
          if (arg) {
            out += `<span class="m-hat">${renderLatexOffline(arg.content)}</span>`;
            i = arg.next;
            continue;
          }
        } else if (fullCmd === "\\overline" || fullCmd === "\\bar") {
          const arg = takeBraced(s, nextPos);
          if (arg) {
            out += `<span class="m-overline">${renderLatexOffline(arg.content)}</span>`;
            i = arg.next;
            continue;
          }
        } else if (fullCmd === "\\overrightarrow" || fullCmd === "\\vec") {
          const arg = takeBraced(s, nextPos);
          if (arg) {
            out += `<span class="m-vec">${renderLatexOffline(arg.content)}</span>`;
            i = arg.next;
            continue;
          }
        } else if (fullCmd === "\\mathbf" || fullCmd === "\\boldsymbol") {
          const arg = takeBraced(s, nextPos);
          if (arg) {
            out += `<strong>${renderLatexOffline(arg.content)}</strong>`;
            i = arg.next;
            continue;
          }
        } else if (fullCmd === "\\text" || fullCmd === "\\mathrm" || fullCmd === "\\textbf") {
          const arg = takeBraced(s, nextPos);
          if (arg) {
            const inner = (fullCmd === "\\textbf")
              ? `<strong>${escapeHTML(arg.content)}</strong>`
              : escapeHTML(arg.content);
            out += `<span class="m-text">${inner}</span>`;
            i = arg.next;
            continue;
          }
        } else if (fullCmd === "\\sin" || fullCmd === "\\cos" || fullCmd === "\\tan" || fullCmd === "\\cot" || fullCmd === "\\log" || fullCmd === "\\ln" || fullCmd === "\\lim") {
          out += `<span class="m-text">${mCmd[1]}</span>`;
          i = nextPos;
          continue;
        } else if (Object.prototype.hasOwnProperty.call(LATEX_SYMBOLS, fullCmd)) {
          out += LATEX_SYMBOLS[fullCmd];
          i = nextPos;
          continue;
        }
        out += escapeHTML(mCmd[1]);
        i = nextPos;
        continue;
      }
    }

    if (ch === "^" || ch === "_") {
      const tag = ch === "^" ? "sup" : "sub";
      const cls = ch === "^" ? "m-sup" : "m-sub";
      const braced = takeBraced(s, i + 1);
      if (braced) {
        if (ch === "^" && braced.content.trim() === "\\circ") {
          out += "°";
        } else {
          out += `<${tag} class="${cls}">${renderLatexOffline(braced.content)}</${tag}>`;
        }
        i = braced.next;
        continue;
      }
      if (s.slice(i + 1).startsWith("\\circ")) {
        out += "°";
        i += 6;
        continue;
      }
      if (i + 1 < s.length) {
        out += `<${tag} class="${cls}">${escapeHTML(s[i + 1])}</${tag}>`;
        i += 2;
        continue;
      }
    }

    if (ch === "{") {
      const braced = takeBraced(s, i);
      if (braced) {
        out += renderLatexOffline(braced.content);
        i = braced.next;
        continue;
      }
    }

    if (ch === "-") {
      out += "−";
    } else if (ch === "'") {
      out += "′";
    } else {
      out += escapeHTML(ch);
    }
    i++;
  }
  return out.replace(/\x00CASES_START\x00([\s\S]*?)\x00CASES_END\x00/g, '<span class="m-cases"><span class="m-brace">{</span><span class="m-cases-rows">$1</span></span>');
}

function renderLatexToken(tex, isDisplay) {
  const cleanTex = normalizeKatexInput(tex);
  const attrTex = escapeHTML(cleanTex);
  if (window.katex && typeof window.katex.renderToString === "function") {
    try {
      return window.katex.renderToString(cleanTex, {
        throwOnError: true,
        strict: false,
        displayMode: !!isDisplay
      });
    } catch (_) {}
  }
  const cls = isDisplay ? "m-math m-math-block" : "m-math";
  return `<span class="${cls}" data-tex="${attrTex}" data-display="${isDisplay ? 1 : 0}">${renderLatexOffline(cleanTex)}</span>`;
}

function upgradeKatex() {
  if (!window.katex || typeof window.katex.renderToString !== "function") return;
  document.querySelectorAll(".m-math[data-tex]").forEach((el) => {
    let tex = el.getAttribute("data-tex");
    const isDisplay = el.getAttribute("data-display") === "1";
    if (!tex) return;
    tex = normalizeKatexInput(tex);
    try {
      el.outerHTML = window.katex.renderToString(tex, {
        throwOnError: true,
        strict: false,
        displayMode: isDisplay
      });
    } catch (_) {}
  });
}

function formatPlainMathAndChem(escapedStr) {
  if (!escapedStr) return "";
  let s = escapedStr;
  // Convert Unicode superscripts (e.g., cm², m³, 2³) -> <sup class="m-sup">...</sup>
  s = s.replace(/([⁰¹²³⁴⁵⁶⁷⁸⁹ⁿᵐ⁺⁻]+)/g, (m) => {
    const mapped = Array.from(m).map((c) => SUP_CHAR_MAP[c] || c).join("");
    return `<sup class="m-sup">${mapped}</sup>`;
  });
  // Convert Unicode subscripts (e.g., H₂O, CO₂, x₁) -> <sub class="m-sub">...</sub>
  s = s.replace(/([₀₁₂₃₄₅₆₇₈₉₊₋]+)/g, (m) => {
    const mapped = Array.from(m).map((c) => SUB_CHAR_MAP[c] || c).join("");
    return `<sub class="m-sub">${mapped}</sub>`;
  });
  // Convert common ASCII chemical formulas (e.g., H2O, CO2, H2SO4, Ca(OH)2, Fe2O3, CH3COOH)
  s = s.replace(/\b((?:[A-Z][a-z]?\d*|\([A-Za-z0-9]+\)\d+){2,})\b/g, (word) => {
    if (!/\d/.test(word)) return word;
    if (/^(?:M\d+|L\d+|B\d+|C\d+|A\d+|Q\d+|TC\d+|2D|3D|4G|5G|MP3|MP4|H1|H2|H3|H4|H5|H6)$/.test(word)) return word;
    return word.replace(/([A-Za-z\)])(\d+)/g, '$1<sub class="m-sub">$2</sub>');
  });
  return s;
}

function formatInlineStyles(rawOrEscapedStr, alreadyEscaped = false) {
  if (rawOrEscapedStr === null || rawOrEscapedStr === undefined) return "";
  const raw = alreadyEscaped
    ? String(rawOrEscapedStr)
        .replace(/&amp;/g, "&")
        .replace(/&lt;/g, "<")
        .replace(/&gt;/g, ">")
        .replace(/&quot;/g, '"')
        .replace(/&#039;/g, "'")
    : String(rawOrEscapedStr);

  // Split by $$...$$ and $...$ so math tokens are rendered cleanly while text outside is escaped & styled
  const tokenRe = /(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g;
  const parts = raw.split(tokenRe);
  return parts.map((part) => {
    if (part.startsWith("$$") && part.endsWith("$$") && part.length > 4) {
      return renderLatexToken(part.slice(2, -2), true);
    }
    if (part.startsWith("$") && part.endsWith("$") && part.length > 2) {
      return renderLatexToken(part.slice(1, -1), false);
    }
    let esc = escapeHTML(part);
    esc = esc
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
    return formatPlainMathAndChem(esc);
  }).join("");
}

window.HDLGMath = {
  formatInline: function (rawStr) { return formatInlineStyles(rawStr, false); },
  renderLatexToken: renderLatexToken,
  upgradeKatex: upgradeKatex
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
              <div class="formula-expression">${formatInlineStyles(item)}</div>
            </div>
          `;
          return;
        }
        html += `
          <div class="formula-item">
            ${item.name ? `<div class="formula-name">${formatInlineStyles(item.name)}</div>` : ""}
            ${item.formula ? `<div class="formula-expression">${formatInlineStyles(item.formula)}</div>` : ""}
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
          ${group.formula ? `<div class="formula-expression">${formatInlineStyles(group.formula)}</div>` : ""}
          ${group.note ? `<div class="formula-note">${formatRichText(group.note)}</div>` : ""}
        </div>
      `;
      return;
    }

    html += `
      <div class="formula-item">
        <div class="formula-expression">${formatInlineStyles(group)}</div>
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
   YÊU CẦU CẦN ĐẠT & BỘ 10 CÂU HỎI (CHƯƠNG TRÌNH SGK MỚI)
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
    sgkRef.textContent = "Theo Chương trình giáo dục phổ thông môn Toán 2018 (Thông tư 32/2018/TT-BGDĐT). Sau chủ đề này, em cần:";
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

  if (lesson.definition) {
    setText(definition, lesson.definition);
    setSectionVisible(definitionSection, true);
  } else {
    setSectionVisible(definitionSection, false);
  }

  if (lesson.context || lesson.context_title) {
    if (contextTitle) contextTitle.textContent = lesson.context_title || "Bối cảnh thực tế";
    setText(context, lesson.context || "");
    setSectionVisible(contextSection, true);
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
  if (window.HDLG && typeof HDLG.track === "function") whenHdlgReady(function () { HDLG.track("open", lesson.id); });

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
   - 📖 Đọc hết bài (cuộn tới cuối + ở lại đủ thời gian tối thiểu): +5 sao
   - ❓ Trả lời đúng "Kiểm tra nhanh" ngay lần chọn đầu tiên: +5 sao
   - Bài không có câu Kiểm tra nhanh: đọc hết bài nhận trọn 10 sao
   Mỗi phần chỉ nhận 1 lần / bài (lưu qua HDLG.lessonReward → đồng bộ Firebase).
========================================================= */
const READ_DONE_PERCENT = 92;      // cuộn tới >= 92% trang là "đã tới cuối bài"
const MIN_READ_SECONDS = 30;       // phải ở lại bài ít nhất ngần này giây

const rewardState = {
  lessonId: null,
  hasQuiz: false,
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

// Chờ Firebase đăng nhập & đồng bộ xong rồi mới cộng sao (tránh bị dữ liệu cũ ghi đè)
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

  // Kiểm tra nhanh
  const quizItem = document.getElementById("rewardQuiz");
  if (quizItem) quizItem.style.display = rewardState.hasQuiz ? "" : "none";
  if (rewardState.hasQuiz) {
    if (st.quiz) {
      setRewardItem("rewardQuiz", "rewardQuizHint", "rewardQuizPts", "done", "Đã nhận sao", "✓");
    } else if (rewardState.quizAttempted) {
      setRewardItem("rewardQuiz", "rewardQuizHint", "rewardQuizPts", "missed",
        rewardState.isQuizSet
          ? "Chưa đạt 7/10 — xem lời giải rồi bấm “Làm lại”"
          : "Chưa đúng — ôn lại rồi mở lại bài để thử lần nữa", `+${rewardState.quizStars}`);
    } else {
      setRewardItem("rewardQuiz", "rewardQuizHint", "rewardQuizPts", "",
        rewardState.isQuizSet ? "Làm đúng từ 7/10 câu luyện tập" : "Chọn đúng ngay lần đầu", `+${rewardState.quizStars}`);
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
  rewardState.quizAttempted = true;          // chỉ tính lần chọn ĐẦU TIÊN
  // Ghi lại câu trả lời sai để Trợ lý Tri gợi ý ôn lại bài này
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

  // Chờ đăng nhập/đồng bộ xong rồi vẽ lại (tránh hiển thị sai trạng thái cũ)
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