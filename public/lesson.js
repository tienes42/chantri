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
  "\\rightarrow": "→", "\\to": "→", "\\leftarrow": "←", "\\mapsto": "↦", "\\longrightarrow": "⟶", "\\longleftarrow": "⟵", "\\leftrightarrow": "↔", "\\rightleftharpoons": "⇌", "\\leftrightharpoons": "⇋", "\\uparrow": "↑", "\\downarrow": "↓",
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
        } else if (fullCmd === "\\xrightarrow" || fullCmd === "\\xleftarrow") {
          const opt = takeBracketed(s, nextPos);
          const bracePos = opt ? opt.next : nextPos;
          const arg = takeBraced(s, bracePos);
          if (arg) {
            const arrowChar = fullCmd === "\\xrightarrow" ? "⟶" : "⟵";
            const topHtml = arg.content ? `<span class="m-num" style="font-size:0.75em;border-bottom:none;padding:0 2px;">${renderLatexOffline(arg.content)}</span>` : "";
            const botHtml = opt && opt.content ? `<span class="m-den" style="font-size:0.75em;padding:0 2px;">${renderLatexOffline(opt.content)}</span>` : "";
            out += `<span class="m-frac" style="vertical-align:middle;margin:0 3px;">${topHtml}<span style="line-height:0.9;">${arrowChar}</span>${botHtml}</span>`;
            i = arg.next;
            continue;
          }
        } else if (fullCmd === "\\overset" || fullCmd === "\\underset") {
          const first = takeBraced(s, nextPos);
          if (first) {
            const second = takeBraced(s, first.next);
            if (second) {
              if (fullCmd === "\\overset") {
                out += `<span class="m-frac" style="vertical-align:middle;"><span class="m-num" style="font-size:0.72em;border-bottom:none;padding:0 1px;">${renderLatexOffline(first.content)}</span><span>${renderLatexOffline(second.content)}</span></span>`;
              } else {
                out += `<span class="m-frac" style="vertical-align:middle;"><span>${renderLatexOffline(second.content)}</span><span class="m-den" style="font-size:0.72em;padding:0 1px;">${renderLatexOffline(first.content)}</span></span>`;
              }
              i = second.next;
              continue;
            }
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
  if (typeof drawMindmapConnections === "function") {
    requestAnimationFrame(drawMindmapConnections);
  }
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
   RENDER GAME (HỖ TRỢ ĐA GAME CHO BÀI GỘP & SỬA LỆCH BÀI HỌC - GAME)
========================================================= */
const GAME_FILES_MAP = {
  function_challenge: "function-challenge",
  "store-management": "store_management"
};

const LESSON_GAMES_BY_TOPIC = {
  /* ---------------- VẬT LÝ 12 ---------------- */
  "quang-dien": [
    {
      badge: "Chuyên đề 1 · Mạch RLC",
      icon: "📻",
      title: "Trạm Dò Sóng: Mạch điện xoay chiều RLC & Cộng hưởng điện",
      desc: "Tính cảm kháng Z_L, dung kháng Z_C, tổng trở Z, hệ số công suất cosφ và điều chỉnh tụ xoay để thu sóng cộng hưởng Z_L = Z_C.",
      file: "game_mach_rlc",
      btn: "🚀 Chơi Game Mạch RLC"
    },
    {
      badge: "Chuyên đề 2 · Lượng tử ánh sáng",
      icon: "🔬",
      title: "Xưởng Photon: Lượng tử ánh sáng, Hiện tượng Quang điện & Mẫu Bohr",
      desc: "Khảo sát năng lượng photon ε = hf = hc/λ, giới hạn quang điện λ₀, công thoát A và quang phổ vạch nguyên tử Hydro.",
      file: "game_quang_dien",
      btn: "🚀 Chơi Game Quang điện"
    },
    {
      badge: "Chuyên đề 3 · Thuyết tương đối",
      icon: "🚀",
      title: "Trạm Ánh Sáng: Thuyết tương đối hẹp Einstein & Hệ thức E = mc²",
      desc: "Tính hệ số Lorentz γ, sự giãn thời gian, co chiều dài tương đối tính, năng lượng nghỉ E₀ = m₀c² và động năng hạt tốc độ cao.",
      file: "game_thuyet_tuong_doi",
      btn: "🚀 Chơi Game Thuyết tương đối"
    }
  ],

  "mach-xoay-chieu": [
    {
      badge: "Phần 1 · Dòng điện xoay chiều",
      icon: "⚡",
      title: "Đội Điều Độ Xoay Chiều: Máy phát điện, Giá trị hiệu dụng & cosφ",
      desc: "Vận hành máy phát xoay chiều, tính giá trị hiệu dụng U, I, công suất P = UIcosφ và giảm hao phí truyền tải điện năng.",
      file: "game_mach_xoay_chieu",
      btn: "🚀 Chơi Game Điện xoay chiều"
    },
    {
      badge: "Phần 2 · Cảm ứng điện từ",
      icon: "🧲",
      title: "Trạm Cảm Ứng: Từ thông Φ, Định luật Faraday & Dòng điện Foucault",
      desc: "Khảo sát từ thông Φ = NBScosα, suất điện động cảm ứng e = −ΔΦ/Δt, định luật Lenz, bếp từ và phanh điện từ.",
      file: "game_cam_ung_dien_tu",
      btn: "🚀 Chơi Game Cảm ứng điện từ"
    },
    {
      badge: "Phần 3 · Mạch RLC nối tiếp",
      icon: "📻",
      title: "Trạm Dò Sóng: Mạch RLC mắc nối tiếp & Cộng hưởng điện",
      desc: "Khảo sát mạch RLC nối tiếp, độ lệch pha u – i và hiện tượng cộng hưởng điện f₀ = 1/(2π√(LC)).",
      file: "game_mach_rlc",
      btn: "🚀 Chơi Game Mạch RLC"
    }
  ],

  "tu-truong": [
    {
      badge: "Phần 1 · Từ trường & Lực từ",
      icon: "🧲",
      title: "Viện Nam Châm: Cảm ứng từ B, Lực từ F = BIl·sinα & Lực Lorentz",
      desc: "Điều khiển lực từ tác dụng lên đoạn dây dẫn mang dòng điện, cân từ và quỹ đạo hạt mang điện trong từ trường đều.",
      file: "game_tu_truong",
      btn: "🚀 Chơi Game Từ trường & Lực từ"
    },
    {
      badge: "Phần 2 · Cảm ứng điện từ",
      icon: "⚡",
      title: "Trạm Cảm Ứng: Từ thông, Định luật Faraday & Định luật Lenz",
      desc: "Thực hành tạo dòng điện cảm ứng khi từ thông biến thiên, tính suất điện động cảm ứng và suất điện động tự cảm.",
      file: "game_cam_ung_dien_tu",
      btn: "🚀 Chơi Game Cảm ứng điện từ"
    }
  ],

  "vat-ly-nhiet": [
    {
      badge: "Đề A · Chuyển thể & Nhiệt lượng",
      icon: "🧊",
      title: "Biệt Đội Nhiệt Động (Đề A): Nhiệt dung riêng, Nhiệt nóng chảy λ & Nhiệt hóa hơi L",
      desc: "Tính lượng nước đá ướp cá Q = λm, chưng tinh dầu tràm Q = mcΔt + Lm và nấu chảy nhôm tại xưởng đúc.",
      file: "game_vat_ly_nhiet_khi_ly_tuong",
      set: 0,
      btn: "🚀 Chơi Đề A: Vật lí nhiệt"
    },
    {
      badge: "Đề B · Định luật 1 NĐLH",
      icon: "🚂",
      title: "Biệt Đội Nhiệt Động (Đề B): Nội năng & Định luật 1 Nhiệt động lực học (ΔU = A + Q)",
      desc: "Vận hành xi-lanh hơi nước, làm mát phanh xe tải đổ đèo và tính công suất máy lạnh kho bảo quản.",
      file: "game_vat_ly_nhiet_khi_ly_tuong",
      set: 1,
      btn: "🚀 Chơi Đề B: Định luật 1 NĐLH"
    }
  ],

  "vat-ly-nhiet-khi-ly-tuong": [
    {
      badge: "Đề C · Trọng tâm Chương II",
      icon: "🎈",
      title: "Biệt Đội Nhiệt Động (Đề C): Định luật Boyle, Charles & Phương trình Khí lí tưởng",
      desc: "Tính số lần bơm lốp xe chở nho (p₁V₁ = p₂V₂, p/T = const), bơm khí heli nâng băng rôn (pV = nRT) và van an toàn nồi hấp.",
      file: "game_vat_ly_nhiet_khi_ly_tuong",
      set: 2,
      btn: "🚀 Chơi Đề C: Khí lí tưởng"
    },
    {
      badge: "Ôn tập kết hợp · Nhiệt & Công",
      icon: "🔥",
      title: "Biệt Đội Nhiệt Động (Đề A & B): Chuyển thể & Định luật 1 Nhiệt động lực học",
      desc: "Ôn tập kết hợp quá trình truyền nhiệt, chuyển thể và công cơ học của khối khí.",
      file: "game_vat_ly_nhiet_khi_ly_tuong",
      set: 0,
      btn: "🚀 Chơi Đề A & B: Nhiệt động học"
    }
  ],

  /* ---------------- VẬT LÝ 11 ---------------- */
  "dien-truong": [
    {
      badge: "Phần 1 · Định luật Coulomb & E",
      icon: "⚡",
      title: "Xưởng Tia Lửa: Lực tĩnh điện Coulomb & Cường độ điện trường",
      desc: "Khảo sát lực tương tác F = k|q₁q₂|/r², cân bằng giọt dầu Millikan và tổng hợp cường độ điện trường.",
      file: "game_dien_truong",
      btn: "🚀 Chơi Game Điện trường"
    },
    {
      badge: "Phần 2 · Điện trường đều",
      icon: "🎯",
      title: "Phòng Lái Tia: Điện trường đều E = U/d & Quỹ đạo hạt mang điện",
      desc: "Điều khiển điện áp bản phẳng để lái chùm hạt mang điện bay theo quỹ đạo parabol trúng bia đích.",
      file: "game_dien_truong_deu",
      btn: "🚀 Chơi Game Điện trường đều"
    }
  ],

  "dien-the": [
    {
      badge: "Phần 1 · Thế năng điện & Tụ điện",
      icon: "🔋",
      title: "Biệt Đội Electron-Volt: Công lực điện A = qEd, Điện thế & Tụ điện",
      desc: "Tính công của lực điện, hiệu điện thế U_MN, đơn vị eV và năng lượng tích trữ trong bộ tụ điện.",
      file: "game_dien_the",
      btn: "🚀 Chơi Game Điện thế & Tụ điện"
    },
    {
      badge: "Phần 2 · Lái hạt mang điện",
      icon: "🎯",
      title: "Phòng Lái Tia: Chuyển động hạt mang điện trong Điện trường đều",
      desc: "Vận dụng định lý động năng W_đ2 − W_đ1 = qU để tăng tốc và lái chùm tia điện tử.",
      file: "game_dien_truong_deu",
      btn: "🚀 Chơi Game Phòng Lái Tia"
    }
  ],

  "song-dien-tu-giao-thoa-tu-dien": [
    {
      badge: "Đề A · Giao thoa sóng",
      icon: "🌊",
      title: "Đội Săn Sóng (Đề A): Giao thoa sóng cơ & Khe Young ánh sáng (i = λD/a)",
      desc: "Tính khoảng vân giao thoa i = λD/a, bước sóng ánh sáng và vị trí cực đại – cực tiểu giao thoa.",
      file: "game_song_dien_tu_giao_thoa_tu_dien",
      set: 0,
      btn: "🚀 Chơi Đề A: Giao thoa sóng"
    },
    {
      badge: "Đề B · Sóng dừng",
      icon: "🎸",
      title: "Đội Săn Sóng (Đề B): Sóng dừng trên dây đàn hồi & trong cột khí",
      desc: "Điều chỉnh chiều dài dây l = k·λ/2, tần số họa âm và cộng hưởng ống sáo.",
      file: "game_song_dien_tu_giao_thoa_tu_dien",
      set: 1,
      btn: "🚀 Chơi Đề B: Sóng dừng"
    },
    {
      badge: "Đề C · Sóng điện từ",
      icon: "📡",
      title: "Đội Săn Sóng (Đề C): Thang sóng điện từ, Radar & Thu phát sóng (λ = c/f)",
      desc: "Chọn tần số sóng điện từ, bước sóng λ = c/f và công suất phát radar.",
      file: "game_song_dien_tu_giao_thoa_tu_dien",
      set: 2,
      btn: "🚀 Chơi Đề C: Sóng điện từ"
    }
  ],

  /* ---------------- VẬT LÝ 10 ---------------- */
  "do-luong": [
    {
      badge: "Chương I · Vật lí 10",
      icon: "📏",
      title: "Thực Hành Đo Lường: Chọn dụng cụ theo GHĐ – ĐCNN, Ngắm đúng vạch & Đổi đơn vị",
      desc: "Thực hành chọn thước kẹp (ĐCNN 0,1 mm), thước cuộn, đặt mắt vuông góc tránh sai số thị sai và quy đổi đơn vị chuẩn.",
      file: "game_dodai",
      btn: "🚀 Bắt đầu Thực hành Đo lường"
    }
  ],

  "dinh-luat-newton": [
    {
      badge: "Game 1 · Trạm Hỏa Tinh (10 chặng)",
      icon: "🚀",
      title: "Trạm Hỏa Tinh: Tổng hợp lực, Ba định luật Newton & Các lực cơ học",
      desc: "Vận dụng F = ma, lực ma sát F_ms = μN, lực căng dây và phản lực đẩy trong không gian qua 3 đề thực chiến.",
      file: "game_newton",
      btn: "🚀 Chơi Game Trạm Hỏa Tinh"
    },
    {
      badge: "Game 2 · Đêm Nhạc Hội Trường",
      icon: "🎸",
      title: "Đêm Nhạc Hội Trường: Bài Toán Của Lực (Ma sát dốc · Cân bằng giàn đèn · Phanh ABS)",
      desc: "Trải nghiệm 3 màn cốt truyện liên hoàn: Kéo loa qua dốc ma sát 14°, Cân bằng moment lực giàn đèn và Lái xe kéo phanh ABS đêm mưa.",
      file: "force_real_life_game",
      btn: "🚀 Chơi Đêm Nhạc Hội Trường"
    }
  ],

  "chuyen-dong-tron-bien-dang-lo-xo": [
    {
      badge: "Đề A · Moment lực & Cân bằng",
      icon: "⚖️",
      title: "Xưởng Cơ Học (Đề A): Moment lực M = F·d & Điều kiện cân bằng vật rắn",
      desc: "Cân bằng cần cẩu tháp, cầu nâng và dầm chịu lực bằng quy tắc moment lực.",
      file: "game_chuyen_dong_tron_lo_xo",
      set: 0,
      btn: "🚀 Chơi Đề A: Cân bằng vật rắn"
    },
    {
      badge: "Đề B · Chuyển động tròn đều",
      icon: "🎡",
      title: "Xưởng Cơ Học (Đề B): Chuyển động tròn đều, Tốc độ góc ω & Lực hướng tâm F_ht = mv²/r",
      desc: "Tính tốc độ an toàn qua khúc cua nghiêng, lực hướng tâm và chu kì quay.",
      file: "game_chuyen_dong_tron_lo_xo",
      set: 1,
      btn: "🚀 Chơi Đề B: Chuyển động tròn đều"
    },
    {
      badge: "Đề C · Định luật Hooke",
      icon: "🔩",
      title: "Xưởng Cơ Học (Đề C): Biến dạng đàn hồi & Định luật Hooke F_đh = k·|Δl|",
      desc: "Chọn độ cứng lò xo k, giới hạn đàn hồi và thiết kế hệ giảm xóc chịu tải.",
      file: "game_chuyen_dong_tron_lo_xo",
      set: 2,
      btn: "🚀 Chơi Đề C: Định luật Hooke"
    }
  ],

  /* ---------------- KHTN 9 (VẬT LÝ) ---------------- */
  "co-nang-khuc-xa-anh-sang": [
    {
      badge: "Đề A · Cơ năng (Bài 2–4)",
      icon: "🎢",
      title: "Năng Lượng & Ánh Sáng (Đề A): Động năng W_đ = ½mv², Thế năng W_t = P·h & Cơ năng",
      desc: "Thiết kế đường ray tàu lượn, búa máy đóng cọc và trạm thủy điện bằng định luật bảo toàn cơ năng.",
      file: "game_co_nang_khuc_xa",
      set: 0,
      btn: "🚀 Chơi Đề A: Động năng & Thế năng"
    },
    {
      badge: "Đề B · Khúc xạ ánh sáng (Bài 5)",
      icon: "🔦",
      title: "Năng Lượng & Ánh Sáng (Đề B): Định luật Khúc xạ n₁·sin i = n₂·sin r & Chiết suất",
      desc: "Chiếu đèn laser ngắm mục tiêu dưới nước và đo chiết suất môi trường trong suốt.",
      file: "game_co_nang_khuc_xa",
      set: 1,
      btn: "🚀 Chơi Đề B: Khúc xạ ánh sáng"
    },
    {
      badge: "Đề C · Phản xạ toàn phần & Lăng kính (Bài 6–7)",
      icon: "💎",
      title: "Năng Lượng & Ánh Sáng (Đề C): Phản xạ toàn phần (sin i_gh = n₂/n₁), Cáp quang & Lăng kính",
      desc: "Chọn góc chiếu vào lõi cáp quang, góc mài kim cương và góc lệch tia sáng qua lăng kính.",
      file: "game_co_nang_khuc_xa",
      set: 2,
      btn: "🚀 Chơi Đề C: Cáp quang & Lăng kính"
    }
  ],

  /* ---------------- KHTN 8 (VẬT LÝ) ---------------- */
  "khoi-luong-rieng": [
    {
      badge: "Game 1 · Xưởng Đúc & Kiểm Định",
      icon: "🧱",
      title: "Xưởng Đúc Vật Liệu: Tính Khối lượng riêng D = m / V & Trọng lượng riêng d = 10D",
      desc: "Chọn khối lượng phôi m và thể tích khuôn V để đúc hợp kim nhôm (D = 2,7 g/cm³), phao nổi và quả đối trọng thép.",
      file: "simulation_classic",
      query: "topic=khoi-luong-rieng",
      btn: "🚀 Chơi Game Khối lượng riêng"
    },
    {
      badge: "Game 2 · Trung Tâm Thủy Lực",
      icon: "🚢",
      title: "Trung Tâm Thủy Lực: Ứng dụng Khối lượng riêng chất lỏng & Áp suất",
      desc: "Vận dụng khối lượng riêng ρ của nước ngọt, nước biển và dầu trong bình thông nhau và bể chứa.",
      file: "game_chat_luu",
      set: 0,
      btn: "🚀 Chơi Trung Tâm Thủy Lực"
    }
  ],

  "ap-suat": [
    {
      badge: "Game 1 · Trung Tâm Thủy Lực (9 chặng)",
      icon: "🚰",
      title: "Trung Tâm Thủy Lực: Áp suất bề mặt p = F/S, Áp suất chất lỏng p = d·h & Máy nén thủy lực",
      desc: "Thực hành thiết kế móng trụ, đập nước, bình thông nhau và kích thủy lực Pascal F₂/F₁ = S₂/S₁.",
      file: "game_chat_luu",
      set: 0,
      btn: "🚀 Chơi Trung Tâm Thủy Lực (9 chặng)"
    },
    {
      badge: "Game 2 · Thử thách Nền Móng",
      icon: "🚜",
      title: "Kỹ Sư Nền Móng: Tính nhanh Áp suất xe tải p = F / S qua nền đất yếu",
      desc: "Chọn tải trọng xe m và diện tích tấm ván lót S để áp suất p = 10m/S không vượt giới hạn lún của nền đất.",
      file: "simulation_classic",
      query: "topic=ap-suat",
      btn: "🚀 Chơi Thử thách Nền Móng"
    }
  ],

  "luc-day-archimedes": [
    {
      badge: "Game 1 · Bến Sông Chở Hàng",
      icon: "⛵",
      title: "Bến Sông Chở Hàng: Lực đẩy Archimedes F_A = d·V & Vạch tải an toàn",
      desc: "Kéo thả các kiện Gạo, Xi măng, Trái cây lên thuyền qua sông nước ngọt và biển nước mặn sao cho mạn khô an toàn.",
      file: "simulation",
      query: "topic=luc-day-archimedes",
      btn: "🚀 Chơi Game Bến Sông"
    },
    {
      badge: "Game 2 · Tàu Ngầm & Cứu Hộ Thủy Lực",
      icon: "🚢",
      title: "Trung Tâm Thủy Lực (Đề B): Lực đẩy Archimedes, Khinh khí cầu & Tàu ngầm",
      desc: "Tính toán thể tích chiếm chỗ V, điều chỉnh két nước dằn tàu ngầm và trục vớt vật chìm.",
      file: "game_chat_luu",
      set: 1,
      btn: "🚀 Chơi Game Tàu Ngầm & Thủy Lực"
    },
    {
      badge: "Game 3 · Mô phỏng Thanh trượt",
      icon: "📊",
      title: "Mô Phỏng Thiết Kế Thuyền: Chỉnh bề rộng thuyền w & Khối lượng hàng",
      desc: "Khảo sát sự thay đổi của mớn nước và lực đẩy Archimedes khi thay đổi bề rộng thân thuyền.",
      file: "simulation_classic",
      query: "topic=luc-day-archimedes",
      btn: "🚀 Chơi Mô phỏng Thanh trượt"
    }
  ],

  /* ---------------- KHTN 6 (VẬT LÝ) ---------------- */
  "luc": [
    {
      badge: "Game 1 · Cứu hộ đêm mưa",
      icon: "🛟",
      title: "Cứu Hộ Đêm Mưa: Biểu diễn Lực (Gốc, Phương, Chiều, Độ lớn) & Kéo tời",
      desc: "Điều chỉnh hướng và độ lớn mũi tên lực kéo (kN) để giải cứu 3 xe sa lầy sát mép mương an toàn.",
      file: "game_luc",
      btn: "🚀 Chơi Game Cứu hộ đêm mưa"
    },
    {
      badge: "Game 2 · Đêm Nhạc Hội Trường",
      icon: "🎸",
      title: "Đêm Nhạc Hội Trường: Bài Toán Của Lực (Kéo loa · Treo giàn đèn · Xe kéo)",
      desc: "Vận dụng tổng hợp lực, lực căng dây T = P/(2·sinα) và lực ma sát trong đêm nhạc hội trường.",
      file: "force_real_life_game",
      btn: "🚀 Chơi Đêm Nhạc Hội Trường"
    }
  ],

  "luc-ma-sat": [
    {
      badge: "Game 1 · Kiểm định lốp xe",
      icon: "🛞",
      title: "Trung Tâm Kiểm Định: Lực ma sát trượt, Ma sát lăn, Ma sát nghỉ & Quãng đường phanh",
      desc: "Đo quãng đường phanh trên 4 mặt đường, chọn lốp đi đèo mưa và xử lý ma sát có lợi – có hại.",
      file: "game_lucmasat",
      btn: "🚀 Chơi Game Kiểm định lốp xe"
    },
    {
      badge: "Game 2 · Đêm Nhạc Hội Trường",
      icon: "🎸",
      title: "Đêm Nhạc Hội Trường: Kéo kiện âm thanh 900 N qua dốc gỗ bằng con lăn",
      desc: "So sánh ma sát trượt (μ = 0,42) với ma sát lăn (μ = 0,085) và tìm góc kéo dây α tối ưu.",
      file: "force_real_life_game",
      btn: "🚀 Chơi Đêm Nhạc Hội Trường"
    }
  ],

  /* ---------------- TOÁN 1 & TOÁN 12 ---------------- */
  "l1-cd07-do-dai": [
    {
      badge: "Chủ đề 7 · Toán 1",
      icon: "📏",
      title: "Bé Đo Giỏi (Đề A): Đặt thước đúng vạch 0 & Đo độ dài bằng xăng-ti-mét (cm)",
      desc: "Thực hành kéo thước kẻ đặt vạch 0 trùng đầu bút chì, chọn băng giấy đúng số cm và cộng độ dài.",
      file: "game_do_luong",
      set: 0,
      btn: "🚀 Chơi Đề A: Đo độ dài (cm)"
    }
  ],

  "l1-cd09-thoi-gian-gio-lich": [
    {
      badge: "Đề B · Xem đồng hồ",
      icon: "🕘",
      title: "Bé Đo Giỏi (Đề B): Xem giờ đúng trên đồng hồ kim & Cộng thêm giờ",
      desc: "Thực hành xoay kim ngắn, kim dài chỉ giờ đúng (kim dài chỉ số 12) và tính giờ tàu đến ga.",
      file: "game_do_luong",
      set: 1,
      btn: "🚀 Chơi Đề B: Xem giờ đồng hồ"
    },
    {
      badge: "Đề C · Thứ, ngày & Lịch",
      icon: "📅",
      title: "Bé Đo Giỏi (Đề C): Các ngày trong tuần & Xem tờ lịch hằng ngày",
      desc: "Đọc thứ, ngày trên tờ lịch và tính ngày sinh nhật, ngày đi dã ngoại trong tuần lễ 7 ngày.",
      file: "game_do_luong",
      set: 2,
      btn: "🚀 Chơi Đề C: Xem lịch tuần"
    }
  ],

  "l12-ch02-vecto-va-he-truc-toa-do-trong-khong-gian": [
    {
      badge: "Đề A · Vectơ & Tọa độ Oxyz",
      icon: "🧭",
      title: "Đội Định Vị Oxyz (Đề A): Tọa độ điểm, Phép toán Vectơ, Trọng tâm & Tích vô hướng",
      desc: "Xác định tọa độ 3D (x; y; z), tính độ dài đoạn thẳng AB, tọa độ trọng tâm G và góc giữa hai vectơ.",
      file: "game_toa_do_oxyz",
      set: 0,
      btn: "🚀 Chơi Đề A: Vectơ & Tọa độ Oxyz"
    }
  ],

  "l12-ch05-phuong-phap-toa-do-trong-khong-gian": [
    {
      badge: "Đề B · Mặt phẳng & Đường thẳng",
      icon: "📐",
      title: "Đội Định Vị Oxyz (Đề B): Phương trình Mặt phẳng, Đường thẳng & Khoảng cách",
      desc: "Lập phương trình mặt phẳng, tìm vectơ pháp tuyến, vectơ chỉ phương và khoảng cách từ điểm đến mặt phẳng.",
      file: "game_toa_do_oxyz",
      set: 1,
      btn: "🚀 Chơi Đề B: Mặt phẳng & Đường thẳng"
    },
    {
      badge: "Đề C · Mặt cầu & Tối ưu 3D",
      icon: "🌐",
      title: "Đội Định Vị Oxyz (Đề C): Phương trình Mặt cầu, Giao tuyến & Vùng phủ sóng 3D",
      desc: "Xác định tâm I(a; b; c), bán kính R của mặt cầu phát sóng và bài toán vị trí tương đối trong không gian.",
      file: "game_toa_do_oxyz",
      set: 2,
      btn: "🚀 Chơi Đề C: Mặt cầu Oxyz"
    }
  ]
};

function resolveLessonGamesList(lesson) {
  if (!lesson) return null;
  const topicKey = (lesson.topic || params.get("topic") || "").trim();
  if (topicKey && LESSON_GAMES_BY_TOPIC[topicKey]) {
    return LESSON_GAMES_BY_TOPIC[topicKey];
  }
  /* Dự phòng nhận diện theo tiêu đề bài học nếu topic trong CSDL cũ khác tên */
  const t = (lesson.title || "").toLowerCase();
  const g = Number(lesson.grade || gradeFromUrl || 0);
  if (t.includes("thuyết tương đối") || t.includes("lượng tử ánh sáng") || t.includes("chuyên đề vật lí 12")) {
    return LESSON_GAMES_BY_TOPIC["quang-dien"];
  }
  if (g === 12 && (t.includes("máy phát điện xoay chiều") || t.includes("dòng điện xoay chiều"))) {
    return LESSON_GAMES_BY_TOPIC["mach-xoay-chieu"];
  }
  if (g === 12 && t.includes("từ trường")) {
    return LESSON_GAMES_BY_TOPIC["tu-truong"];
  }
  if (g === 12 && t.includes("khí lí tưởng")) {
    return LESSON_GAMES_BY_TOPIC["vat-ly-nhiet-khi-ly-tuong"];
  }
  if (g === 12 && t.includes("vật lí nhiệt")) {
    return LESSON_GAMES_BY_TOPIC["vat-ly-nhiet"];
  }
  if (g === 11 && (t.includes("thế năng điện") || t.includes("tụ điện"))) {
    return LESSON_GAMES_BY_TOPIC["dien-the"];
  }
  if (g === 11 && (t.includes("lực tĩnh điện") || t.includes("cường độ điện trường"))) {
    return LESSON_GAMES_BY_TOPIC["dien-truong"];
  }
  if (g === 10 && (t.includes("làm quen với vật lí") || t.includes("sai số phép đo"))) {
    return LESSON_GAMES_BY_TOPIC["do-luong"];
  }
  if (g === 8 && t.includes("áp suất")) {
    return LESSON_GAMES_BY_TOPIC["ap-suat"];
  }
  if (g === 8 && t.includes("archimedes")) {
    return LESSON_GAMES_BY_TOPIC["luc-day-archimedes"];
  }
  if (g === 8 && t.includes("khối lượng riêng")) {
    return LESSON_GAMES_BY_TOPIC["khoi-luong-rieng"];
  }
  if (g === 1 && t.includes("độ dài")) {
    return LESSON_GAMES_BY_TOPIC["l1-cd07-do-dai"];
  }
  if (g === 1 && (t.includes("thời gian") || t.includes("giờ và lịch"))) {
    return LESSON_GAMES_BY_TOPIC["l1-cd09-thoi-gian-gio-lich"];
  }
  if (g === 12 && t.includes("vectơ và hệ trục")) {
    return LESSON_GAMES_BY_TOPIC["l12-ch02-vecto-va-he-truc-toa-do-trong-khong-gian"];
  }
  return null;
}

function buildGameHref(lessonIdVal, item) {
  const file = GAME_FILES_MAP[item.file] || item.file;
  const q = [];
  if (lessonIdVal != null) q.push("lesson_id=" + encodeURIComponent(lessonIdVal));
  if (item.set != null) q.push("set=" + encodeURIComponent(item.set));
  if (item.query) q.push(item.query);
  return "games/" + encodeURIComponent(file) + ".html" + (q.length ? "?" + q.join("&") : "");
}

function renderGame(lesson) {
  if (!gameDescription || !gameButton || !noGame) return;

  let multiBox = document.getElementById("multiGamesContainer");
  if (multiBox) multiBox.innerHTML = "";

  if (!lesson) {
    gameDescription.textContent = "";
    gameButton.style.display = "none";
    noGame.classList.remove("hidden");
    return;
  }

  const customList = resolveLessonGamesList(lesson);

  if (customList && customList.length > 0) {
    noGame.classList.add("hidden");

    if (customList.length === 1) {
      const g = customList[0];
      gameDescription.innerHTML = `<strong>${escapeHTML(g.icon)} ${escapeHTML(g.title)}:</strong> ${escapeHTML(g.desc)}`;
      gameButton.style.display = "inline-block";
      gameButton.textContent = g.btn || "🚀 Bắt đầu trải nghiệm";
      gameButton.onclick = function () {
        window.location.href = buildGameHref(lesson.id, g);
      };
      return;
    }

    gameDescription.innerHTML =
      `Bài học này tích hợp <strong>${customList.length} chủ đề thực hành</strong>. Bạn có thể chọn chơi từng game tương ứng với từng phần kiến thức bên dưới:`;
    gameButton.style.display = "none";

    if (!multiBox) {
      multiBox = document.createElement("div");
      multiBox.id = "multiGamesContainer";
      multiBox.style.cssText =
        "display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:16px;";
      gameButton.parentNode.insertBefore(multiBox, gameButton.nextSibling);
    }

    multiBox.innerHTML = customList
      .map(
        (g, idx) => `
        <div style="background:rgba(15,23,42,0.88);border:1.5px solid rgba(56,189,248,0.4);border-radius:16px;padding:16px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 8px 20px rgba(0,0,0,0.22);text-align:left;">
          <div>
            <div style="display:inline-block;font-size:11.5px;font-weight:800;color:#fde68a;background:rgba(245,158,11,0.2);border:1px solid rgba(251,191,36,0.5);padding:3px 10px;border-radius:999px;margin-bottom:8px;">
              ${escapeHTML(g.badge || "Phần " + (idx + 1))}
            </div>
            <div style="font-size:16px;font-weight:800;color:#f8fafc;line-height:1.38;margin-bottom:6px;">
              ${escapeHTML(g.icon || "🎮")} ${escapeHTML(g.title)}
            </div>
            <div style="font-size:13.5px;color:#cbd5e1;line-height:1.52;margin-bottom:14px;">
              ${escapeHTML(g.desc)}
            </div>
          </div>
          <button type="button" data-game-idx="${idx}" style="width:100%;padding:10px 14px;border:none;border-radius:12px;background:linear-gradient(180deg,#22c55e,#15803d);color:#fff;font-weight:800;font-size:14px;cursor:pointer;box-shadow:0 4px 0 #14532d;">
            ${escapeHTML(g.btn || "🚀 Bắt đầu trải nghiệm")}
          </button>
        </div>`
      )
      .join("");

    multiBox.querySelectorAll("button[data-game-idx]").forEach((btn) => {
      btn.addEventListener("click", function () {
        const g = customList[Number(this.getAttribute("data-game-idx"))];
        if (g) window.location.href = buildGameHref(lesson.id, g);
      });
    });
    return;
  }

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
      const file = GAME_FILES_MAP[lesson.game_type] || lesson.game_type;
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
    const subjLabel = subject === "physics" ? "môn Vật lý / KHTN" : subject === "chemistry" ? "môn Hóa học / KHTN" : "môn Toán";
    sgkRef.textContent = `Theo Chương trình giáo dục phổ thông ${subjLabel} 2018 (Thông tư 32/2018/TT-BGDĐT). Sau chủ đề này, em cần:`;
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

/* =========================================================
   SƠ ĐỒ TƯ DUY TƯƠNG TÁC 2.5D (AUTO-MINDMAP GENERATOR)
========================================================= */
let mmZoomLevel = 1;
let mmIsFullscreen = false;

function truncateLatexSafe(rawStr, maxChars = 135) {
  if (!rawStr) return "";
  let cleaned = String(rawStr)
    .replace(/^[-*•+]\s+/, "")
    .replace(/^#{1,4}\s+/, "")
    .trim();
  if (cleaned.length <= maxChars) return cleaned;

  const tokenRe = /(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g;
  const parts = cleaned.split(tokenRe);
  let out = "";
  let plainLen = 0;

  for (let i = 0; i < parts.length; i++) {
    const p = parts[i];
    if (!p) continue;
    const isMath = (p.startsWith("$") && p.endsWith("$"));
    if (isMath) {
      if (plainLen > maxChars) break;
      out += p;
      plainLen += Math.min(p.length, 18);
    } else {
      if (plainLen + p.length > maxChars) {
        const remain = Math.max(12, maxChars - plainLen);
        let slice = p.slice(0, remain);
        const lastSpace = slice.lastIndexOf(" ");
        if (lastSpace > 8) slice = slice.slice(0, lastSpace);
        out += slice.replace(/[,;:\s]+$/, "") + "…";
        break;
      }
      out += p;
      plainLen += p.length;
    }
  }
  return out.trim();
}

function splitCleanLines(text, maxItems = 4, maxChars = 135) {
  if (!text) return [];
  const rawLines = String(text)
    .replace(/\r\n/g, "\n")
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l && !/^#{1,4}\s+/.test(l));

  const results = [];
  for (const line of rawLines) {
    const cleaned = truncateLatexSafe(line, maxChars);
    if (cleaned && results.length < maxItems) {
      results.push(cleaned);
    }
  }
  return results;
}

function parseTheorySubBranches(theoryText) {
  if (!theoryText) return [];
  const lines = String(theoryText).replace(/\r\n/g, "\n").split("\n");
  const groups = [];
  let currentGroup = null;

  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line) continue;
    if (/^#{2,4}\s+/.test(line)) {
      const heading = line.replace(/^#{2,4}\s+/, "").trim();
      currentGroup = {
        type: "subbranch",
        title: truncateLatexSafe(heading, 90),
        items: []
      };
      groups.push(currentGroup);
    } else if (currentGroup) {
      if (currentGroup.items.length < 3) {
        currentGroup.items.push(truncateLatexSafe(line, 125));
      }
    }
  }

  if (groups.length > 0) {
    return groups.slice(0, 5);
  }
  return splitCleanLines(theoryText, 4, 130).map((item) => ({
    type: "leaf",
    text: item
  }));
}

function extractFormulaNodes(formulasData, singleFormula) {
  let list = Array.isArray(formulasData) ? formulasData : [];
  if (!list.length && singleFormula) list = [singleFormula];
  const nodes = [];

  for (const group of list) {
    if (group && typeof group === "object" && Array.isArray(group.items)) {
      for (const it of group.items) {
        if (nodes.length >= 5) break;
        if (typeof it === "string") {
          nodes.push({ type: "formula", name: "", formula: it });
        } else if (it && (it.formula || it.name)) {
          nodes.push({
            type: "formula",
            name: truncateLatexSafe(it.name || "", 70),
            formula: it.formula || ""
          });
        }
      }
    } else if (group && typeof group === "object" && (group.formula || group.name)) {
      if (nodes.length < 5) {
        nodes.push({
          type: "formula",
          name: truncateLatexSafe(group.name || "", 70),
          formula: group.formula || ""
        });
      }
    } else if (typeof group === "string" && nodes.length < 5) {
      nodes.push({ type: "formula", name: "", formula: group });
    }
  }
  return nodes;
}

function buildMindmapBranches(lesson) {
  const branches = [];

  // 1. Yêu cầu cần đạt
  const reqs = Array.isArray(lesson.requirements)
    ? lesson.requirements.filter(Boolean).slice(0, 4).map((r) => ({
        type: "leaf",
        text: truncateLatexSafe(r, 130)
      }))
    : [];
  if (reqs.length > 0) {
    branches.push({
      id: "mm-req",
      title: "Mục tiêu cần đạt",
      icon: "🎯",
      color: "indigo",
      stroke: "#4f46e5",
      targetId: "requirementsSection",
      children: reqs
    });
  }

  // 2. Định nghĩa & Khái niệm
  const defItems = splitCleanLines(lesson.definition || lesson.concept, 3, 135).map((t) => ({
    type: "leaf",
    text: t
  }));
  if (defItems.length > 0) {
    branches.push({
      id: "mm-def",
      title: "Khái niệm cốt lõi",
      icon: "💡",
      color: "sky",
      stroke: "#0284c7",
      targetId: "definitionSection",
      children: defItems
    });
  }

  // 3. Hệ thống lý thuyết trọng tâm
  const theoryNodes = parseTheorySubBranches(lesson.theory);
  if (theoryNodes.length > 0) {
    branches.push({
      id: "mm-theory",
      title: "Kiến thức trọng tâm",
      icon: "🧠",
      color: "teal",
      stroke: "#0d9488",
      targetId: "theorySection",
      children: theoryNodes
    });
  }

  // 4. Công thức & Quy tắc
  const formulaNodes = extractFormulaNodes(lesson.formulas, lesson.formula);
  if (formulaNodes.length > 0) {
    branches.push({
      id: "mm-formula",
      title: "Công thức & Quy tắc",
      icon: "📐",
      color: "amber",
      stroke: "#d97706",
      targetId: "formulaSection",
      children: formulaNodes
    });
  }

  // 5. Ứng dụng & Đời sống
  const appSource = lesson.real_life || lesson.application || lesson.context || "";
  const appItems = splitCleanLines(appSource, 3, 130).map((t) => ({
    type: "leaf",
    text: t
  }));
  if (appItems.length > 0) {
    branches.push({
      id: "mm-app",
      title: "Thực tiễn & Ứng dụng",
      icon: "🌍",
      color: "emerald",
      stroke: "#16a34a",
      targetId: lesson.real_life ? "realLifeSection" : "applicationSection",
      children: appItems
    });
  }

  return branches;
}

function drawMindmapConnections() {
  const stage = document.getElementById("mindmapStage");
  const svg = document.getElementById("mindmapSvgLinks");
  const canvas = document.getElementById("mindmapCanvas");
  if (!stage || !svg || !canvas) return;

  if (stage.getAttribute("data-layout") !== "tree") {
    svg.innerHTML = "";
    return;
  }

  const rootCard = canvas.querySelector(".mm-root-card");
  if (!rootCard) return;

  const prevTransform = stage.style.transform;
  stage.style.transform = "none";

  const stageRect = stage.getBoundingClientRect();
  const rootRect = rootCard.getBoundingClientRect();
  const w = Math.max(stage.scrollWidth, stageRect.width);
  const h = Math.max(stage.scrollHeight, stageRect.height);

  svg.setAttribute("width", String(w));
  svg.setAttribute("height", String(h));
  svg.setAttribute("viewBox", `0 0 ${w} ${h}`);

  const rootX = rootRect.right - stageRect.left;
  const rootY = rootRect.top - stageRect.top + rootRect.height / 2;

  let pathsHtml = "";
  const branchRows = canvas.querySelectorAll(".mm-branch-row");

  branchRows.forEach((row) => {
    const stroke = row.getAttribute("data-stroke") || "#0284c7";
    const branchNode = row.querySelector(".mm-branch-node");
    if (!branchNode) return;

    const bRect = branchNode.getBoundingClientRect();
    const bLeftX = bRect.left - stageRect.left;
    const bCenterY = bRect.top - stageRect.top + bRect.height / 2;
    const dx1 = Math.max(24, (bLeftX - rootX) * 0.5);

    pathsHtml += `<path class="mm-link-path" stroke="${stroke}" d="M ${rootX} ${rootY} C ${rootX + dx1} ${rootY}, ${bLeftX - dx1} ${bCenterY}, ${bLeftX} ${bCenterY}" />`;

    if (!row.classList.contains("is-collapsed")) {
      const bRightX = bRect.right - stageRect.left;
      const leaves = row.querySelectorAll(".mm-leaf-card");
      leaves.forEach((leaf) => {
        const lRect = leaf.getBoundingClientRect();
        const lLeftX = lRect.left - stageRect.left;
        const lCenterY = lRect.top - stageRect.top + lRect.height / 2;
        const dx2 = Math.max(18, (lLeftX - bRightX) * 0.5);
        pathsHtml += `<path class="mm-link-path mm-link-sub" stroke="${stroke}" d="M ${bRightX} ${bCenterY} C ${bRightX + dx2} ${bCenterY}, ${lLeftX - dx2} ${lCenterY}, ${lLeftX} ${lCenterY}" />`;
      });
    }
  });

  svg.innerHTML = pathsHtml;
  stage.style.transform = prevTransform;
}

function renderMindmapChildHtml(child) {
  if (child.type === "formula") {
    return `
      <div class="mm-leaf-card mm-formula-pill">
        ${child.name ? `<span class="mm-formula-name">${formatInlineStyles(child.name)}</span>` : ""}
        <span class="mm-formula-eq">${formatInlineStyles(child.formula)}</span>
      </div>
    `;
  }
  if (child.type === "subbranch") {
    const subItemsHtml = (child.items || [])
      .map((it) => `<li>${formatInlineStyles(it)}</li>`)
      .join("");
    return `
      <div class="mm-leaf-card">
        <div class="mm-subbranch-title"><span>▸</span><span>${formatInlineStyles(child.title)}</span></div>
        ${subItemsHtml ? `<ul class="mm-subbranch-list">${subItemsHtml}</ul>` : ""}
      </div>
    `;
  }
  return `
    <div class="mm-leaf-card">
      ${formatInlineStyles(child.text || "")}
    </div>
  `;
}

function renderMindmap(lesson) {
  const section = document.getElementById("mindmapSection");
  const canvas = document.getElementById("mindmapCanvas");
  if (!section || !canvas) return;

  const branches = buildMindmapBranches(lesson);
  if (!branches.length) {
    setSectionVisible(section, false);
    return;
  }
  setSectionVisible(section, true);

  const g = lesson.grade || gradeFromUrl || "";
  const subjName = subject === "physics" ? "Vật lý" : subject === "chemistry" ? "Hóa học" : "Toán học";
  const badgeText = g ? `${subjName} • Lớp ${g}` : subjName;

  const branchesHtml = branches
    .map((b) => {
      const childrenHtml = b.children.map((ch) => renderMindmapChildHtml(ch)).join("");
      return `
        <div class="mm-branch-row" data-color="${b.color}" data-stroke="${b.stroke}" id="${b.id}">
          <div class="mm-branch-node">
            <div class="mm-branch-top">
              <div class="mm-branch-label">
                <span class="mm-branch-ico">${b.icon}</span>
                <span>${escapeHTML(b.title)}</span>
              </div>
              <button type="button" class="mm-toggle-btn" data-mm-toggle="${b.id}" title="Thu gọn / Mở rộng nhánh này">
                − (${b.children.length})
              </button>
            </div>
            <div class="mm-branch-actions">
              <span>${b.children.length} ý chính</span>
              <button type="button" class="mm-jump-link" data-mm-jump="${b.targetId}">
                Xem mục ↗
              </button>
            </div>
          </div>
          <div class="mm-children-col">
            ${childrenHtml}
          </div>
        </div>
      `;
    })
    .join("");

  canvas.innerHTML = `
    <div class="mm-root-col">
      <div class="mm-root-card">
        <div class="mm-root-icon">${escapeHTML(lesson.icon || "📚")}</div>
        <div class="mm-root-badge">${escapeHTML(badgeText)}</div>
        <div class="mm-root-title">${escapeHTML(lesson.title || "Bài học")}</div>
        <div class="mm-root-desc">${escapeHTML(truncateLatexSafe(lesson.description || "", 110))}</div>
      </div>
    </div>
    <div class="mm-branches-col">
      ${branchesHtml}
    </div>
  `;

  upgradeKatex();
  requestAnimationFrame(() => {
    drawMindmapConnections();
    setTimeout(drawMindmapConnections, 160);
  });
}

function initMindmapInteractions() {
  const section = document.getElementById("mindmapSection");
  const viewport = document.getElementById("mindmapViewport");
  const stage = document.getElementById("mindmapStage");
  const canvas = document.getElementById("mindmapCanvas");
  const zoomLabel = document.getElementById("mmZoomLabel");
  const jumpBtn = document.getElementById("jumpMindmapBtn");

  if (!section || !viewport || !stage || !canvas) return;

  if (jumpBtn) {
    jumpBtn.addEventListener("click", () => {
      section.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  // Đóng/mở từng nhánh & Nhảy tới mục chi tiết
  canvas.addEventListener("click", (e) => {
    const toggleBtn = e.target.closest("[data-mm-toggle]");
    if (toggleBtn) {
      const rowId = toggleBtn.getAttribute("data-mm-toggle");
      const row = document.getElementById(rowId);
      if (row) {
        const collapsed = row.classList.toggle("is-collapsed");
        const count = row.querySelectorAll(".mm-leaf-card").length;
        toggleBtn.textContent = `${collapsed ? "+" : "−"} (${count})`;
        requestAnimationFrame(drawMindmapConnections);
      }
      return;
    }

    const jumpLink = e.target.closest("[data-mm-jump]");
    if (jumpLink) {
      const targetId = jumpLink.getAttribute("data-mm-jump");
      const targetEl = targetId ? document.getElementById(targetId) : null;
      if (targetEl) {
        if (mmIsFullscreen) {
          mmIsFullscreen = false;
          section.classList.remove("is-fullscreen");
        }
        targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }
  });

  // Đổi chế độ bố cục: Nhánh ngang (tree) <-> Tỏa tâm (radial)
  section.querySelectorAll("[data-mm-layout]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const layout = btn.getAttribute("data-mm-layout") || "tree";
      stage.setAttribute("data-layout", layout);
      section.querySelectorAll("[data-mm-layout]").forEach((b) => b.classList.toggle("active", b === btn));
      requestAnimationFrame(drawMindmapConnections);
    });
  });

  // Mở hết / Thu gọn hết
  const expandAllBtn = document.getElementById("mmExpandAllBtn");
  const collapseAllBtn = document.getElementById("mmCollapseAllBtn");
  if (expandAllBtn) {
    expandAllBtn.addEventListener("click", () => {
      canvas.querySelectorAll(".mm-branch-row").forEach((row) => {
        row.classList.remove("is-collapsed");
        const count = row.querySelectorAll(".mm-leaf-card").length;
        const btn = row.querySelector(".mm-toggle-btn");
        if (btn) btn.textContent = `− (${count})`;
      });
      requestAnimationFrame(drawMindmapConnections);
    });
  }
  if (collapseAllBtn) {
    collapseAllBtn.addEventListener("click", () => {
      canvas.querySelectorAll(".mm-branch-row").forEach((row) => {
        row.classList.add("is-collapsed");
        const count = row.querySelectorAll(".mm-leaf-card").length;
        const btn = row.querySelector(".mm-toggle-btn");
        if (btn) btn.textContent = `+ (${count})`;
      });
      requestAnimationFrame(drawMindmapConnections);
    });
  }

  // Thu phóng
  const applyZoom = (newZoom) => {
    mmZoomLevel = Math.min(1.3, Math.max(0.75, Math.round(newZoom * 100) / 100));
    stage.style.transform = `scale(${mmZoomLevel})`;
    if (zoomLabel) zoomLabel.textContent = `${Math.round(mmZoomLevel * 100)}%`;
  };
  const zoomInBtn = document.getElementById("mmZoomInBtn");
  const zoomOutBtn = document.getElementById("mmZoomOutBtn");
  if (zoomInBtn) zoomInBtn.addEventListener("click", () => applyZoom(mmZoomLevel + 0.1));
  if (zoomOutBtn) zoomOutBtn.addEventListener("click", () => applyZoom(mmZoomLevel - 0.1));

  // Toàn màn hình
  const fullscreenBtn = document.getElementById("mmFullscreenBtn");
  if (fullscreenBtn) {
    fullscreenBtn.addEventListener("click", () => {
      mmIsFullscreen = !mmIsFullscreen;
      section.classList.toggle("is-fullscreen", mmIsFullscreen);
      fullscreenBtn.textContent = mmIsFullscreen ? "✕ Đóng toàn màn hình" : "⛶ Toàn màn hình";
      requestAnimationFrame(drawMindmapConnections);
    });
  }
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && mmIsFullscreen) {
      mmIsFullscreen = false;
      section.classList.remove("is-fullscreen");
      if (fullscreenBtn) fullscreenBtn.textContent = "⛶ Toàn màn hình";
      requestAnimationFrame(drawMindmapConnections);
    }
  });

  // Kéo chuột để di chuyển vùng nhìn (Drag to pan)
  let isDown = false;
  let startX = 0;
  let startY = 0;
  let scrollL = 0;
  let scrollT = 0;
  viewport.addEventListener("mousedown", (e) => {
    if (e.target.closest("button, a")) return;
    isDown = true;
    viewport.classList.add("is-dragging");
    startX = e.pageX - viewport.offsetLeft;
    startY = e.pageY - viewport.offsetTop;
    scrollL = viewport.scrollLeft;
    scrollT = viewport.scrollTop;
  });
  window.addEventListener("mouseup", () => {
    isDown = false;
    viewport.classList.remove("is-dragging");
  });
  viewport.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - viewport.offsetLeft;
    const y = e.pageY - viewport.offsetTop;
    viewport.scrollLeft = scrollL - (x - startX);
    viewport.scrollTop = scrollT - (y - startY);
  });

  window.addEventListener("resize", () => {
    requestAnimationFrame(drawMindmapConnections);
  });
}

initMindmapInteractions();

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