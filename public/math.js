/* =========================================================
   MATH PAGE — THÁNH ĐƯỜNG HÌNH HỌC & CUNG ĐIỆN TỶ LỆ VÀNG
========================================================= */

/* =========================
   1. BACK TO INDEX
========================= */
const backButton = document.getElementById("backButton");

if (backButton) {
  backButton.addEventListener("click", function () {
    window.location.href = "index.html";
  });
}

/* =========================
   2. TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON TOÁN HỌC 2.5D (assets/math-icons.png)
   Phân bổ riêng cho cả 12 lớp (Lớp 1 -> Lớp 12) và 4 công cụ
========================= */
const iconSprites = {};

function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function sliceMathIcons(src) {
  try {
    const img = await loadImg(src);
    const W = img.naturalWidth;
    const H = img.naturalHeight;
    const cellW = W / 4;
    const cellH = H / 4;

    // 16 ô trong lưới 4x4 của assets/math-icons.png được gán cho 12 lớp + 4 công cụ + 4 khối đa diện bay
    const gridMap = [
      // Hàng 1
      { keys: ["core"],             col: 0, row: 0, selector: '[data-icon="core"]' },
      { keys: ["g1"],               col: 1, row: 0, selector: '[data-icon="g1"] .class-icon' },
      { keys: ["g4", "toolGeo"],    col: 2, row: 0, selector: '[data-icon="g4"] .class-icon, [data-icon="toolGeo"] .tool-sprite' },
      { keys: ["g3"],               col: 3, row: 0, selector: '[data-icon="g3"] .class-icon' },
      // Hàng 2
      { keys: ["g9"],               col: 0, row: 1, selector: '[data-icon="g9"] .class-icon' },
      { keys: ["g10"],              col: 1, row: 1, selector: '[data-icon="g10"] .class-icon' },
      { keys: ["g11"],              col: 2, row: 1, selector: '[data-icon="g11"] .class-icon' },
      { keys: ["g12"],              col: 3, row: 1, selector: '[data-icon="g12"] .class-icon' },
      // Hàng 3
      { keys: ["toolCalc"],         col: 0, row: 2, selector: '[data-icon="toolCalc"] .tool-sprite' },
      { keys: ["toolChallenge"],    col: 1, row: 2, selector: '[data-icon="toolChallenge"] .tool-sprite' },
      { keys: ["g5", "toolProgress"], col: 2, row: 2, selector: '[data-icon="g5"] .class-icon, [data-icon="toolProgress"] .tool-sprite' },
      { keys: ["aiBot"],            col: 3, row: 2, selector: '[data-icon="aiBot"]' },
      // Hàng 4
      { keys: ["g6", "fibonacci"],  col: 0, row: 3, selector: '[data-icon="g6"] .class-icon, [data-prop="fibonacci"]' },
      { keys: ["g7", "icosa"],      col: 1, row: 3, selector: '[data-icon="g7"] .class-icon, [data-prop="icosa"]' },
      { keys: ["g8", "mobius"],     col: 2, row: 3, selector: '[data-icon="g8"] .class-icon, [data-prop="mobius"]' },
      { keys: ["g2", "cube"],       col: 3, row: 3, selector: '[data-icon="g2"] .class-icon, [data-prop="cube"]' }
    ];

    for (const item of gridMap) {
      const padX = cellW * 0.04;
      const padY = cellH * 0.04;
      const sx = item.col * cellW + padX;
      const sy = item.row * cellH + padY;
      const sw = cellW - padX * 2;
      const sh = cellH - padY * 2;

      const size = 240;
      const c = document.createElement("canvas");
      c.width = size;
      c.height = size;
      const ctx = c.getContext("2d");
      ctx.drawImage(img, sx, sy, sw, sh, 0, 0, size, size);

      const imgData = ctx.getImageData(0, 0, size, size);
      const d = imgData.data;
      const visited = new Uint8Array(size * size);

      const isBg = idx => {
        const r = d[idx], g = d[idx + 1], b = d[idx + 2];
        const max = Math.max(r, g, b), min = Math.min(r, g, b);
        return (r > 224 && g > 224 && b > 224) || (max - min < 18 && min > 175);
      };

      const stack = [];
      for (let x = 0; x < size; x++) stack.push(x, (size - 1) * size + x);
      for (let y = 0; y < size; y++) stack.push(y * size, y * size + (size - 1));

      while (stack.length > 0) {
        const p = stack.pop();
        if (p < 0 || p >= size * size || visited[p]) continue;
        visited[p] = 1;

        const idx = p * 4;
        if (isBg(idx)) {
          d[idx + 3] = 0;
          const x = p % size;
          const y = (p / size) | 0;
          if (x > 0) stack.push(p - 1);
          if (x < size - 1) stack.push(p + 1);
          if (y > 0) stack.push(p - size);
          if (y < size - 1) stack.push(p + size);
        } else {
          const r = d[idx], g = d[idx + 1], b = d[idx + 2];
          if (r > 205 && g > 205 && b > 205) {
            d[idx + 3] = Math.max(0, 255 - ((r + g + b) / 3 - 205) * 5);
          }
        }
      }

      // Xóa khoảng trắng thuần túy bị kẹt bên trong thước tam giác, bàn tính, vòng vô cực
      for (let i = 0; i < size * size; i++) {
        const idx = i * 4;
        if (d[idx + 3] > 0 && d[idx] > 240 && d[idx + 1] > 240 && d[idx + 2] > 240) {
          d[idx + 3] = 0;
        }
      }

      ctx.putImageData(imgData, 0, 0);
      const dataUrl = c.toDataURL("image/png");
      item.keys.forEach(k => { iconSprites[k] = dataUrl; });

      if (item.selector) {
        document.querySelectorAll(item.selector).forEach(el => {
          el.style.backgroundImage = `url("${dataUrl}")`;
          el.querySelectorAll("span").forEach(sp => { sp.style.display = "none"; });
          if (el.classList.contains("tool-sprite")) {
            el.textContent = "";
          }
        });
      }
    }
  } catch (e) {
    console.info("Đang dùng biểu tượng mặc định:", e);
  }
}

sliceMathIcons("assets/math-icons.png");

/* =========================
   3. CLASS CARDS & POPUP
========================= */
const classCards = document.querySelectorAll(".class-card");
const mathPopup = document.getElementById("mathPopup");
const mathPopupClose = document.getElementById("mathPopupClose");
const mathPopupIcon = document.getElementById("mathPopupIcon");
const mathPopupTitle = document.getElementById("mathPopupTitle");
const mathPopupText = document.getElementById("mathPopupText");
const mathPopupButton = document.getElementById("mathPopupButton");

let selectedGrade = null;
let popupCustomAction = null;

function openMathPopup({ iconKey, fallbackEmoji, title, text, buttonLabel, action }) {
  if (mathPopupIcon) {
    if (iconSprites[iconKey]) {
      mathPopupIcon.style.backgroundImage = `url("${iconSprites[iconKey]}")`;
      mathPopupIcon.innerHTML = "";
    } else {
      mathPopupIcon.style.backgroundImage = "none";
      mathPopupIcon.innerHTML = `<span>${fallbackEmoji || "📚"}</span>`;
    }
  }
  if (mathPopupTitle) mathPopupTitle.textContent = title;
  if (mathPopupText) mathPopupText.textContent = text;
  if (mathPopupButton) mathPopupButton.textContent = buttonLabel || "Khám phá";

  popupCustomAction = action;
  if (mathPopup) {
    mathPopup.classList.add("show");
    document.body.classList.add("popup-open");
  }
}

function closeMathPopup() {
  if (mathPopup) {
    mathPopup.classList.remove("show");
    document.body.classList.remove("popup-open");
  }
}

classCards.forEach(function (card) {
  card.addEventListener("click", function () {
    selectedGrade = card.dataset.grade;
    const iconKey = card.dataset.icon || "core";

    openMathPopup({
      iconKey: iconKey,
      fallbackEmoji: "📚",
      title: "Toán lớp " + selectedGrade,
      text:
        "Bạn đã chọn chương trình Toán lớp " +
        selectedGrade +
        ". Hãy sẵn sàng khám phá kiến thức!",
      buttonLabel: "Khám phá",
      action: function () {
        if (selectedGrade !== null) {
          window.location.href = "math-grade.html?grade=" + selectedGrade;
        }
      }
    });
  });
});

if (mathPopupClose) {
  mathPopupClose.addEventListener("click", closeMathPopup);
}

if (mathPopup) {
  mathPopup.addEventListener("click", function (event) {
    if (event.target === mathPopup) {
      closeMathPopup();
    }
  });
}

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") closeMathPopup();
});

if (mathPopupButton) {
  mathPopupButton.addEventListener("click", function () {
    if (typeof popupCustomAction === "function") {
      const fn = popupCustomAction;
      closeMathPopup();
      fn();
    }
  });
}

/* =========================
   4. QUICK TOOLS (MÁY TÍNH -> calculator.html, THỬ THÁCH, TIẾN TRÌNH)
========================= */
const calculatorButton = document.getElementById("calculatorButton");
const challengeButton = document.getElementById("challengeButton");
const progressButton = document.getElementById("progressButton");

if (calculatorButton) {
  calculatorButton.addEventListener("click", function () {
    window.location.href = "calculator.html";
  });
}

if (challengeButton) {
  challengeButton.setAttribute("data-hq-badge", "missions");
  challengeButton.style.position = "relative";
  challengeButton.addEventListener("click", function () {
    window.location.href = "challenge.html?subject=math";
  });
}

if (progressButton) {
  progressButton.addEventListener("click", function () {
    if (window.HDLGQ) window.HDLGQ.openProgress("math");
    else window.location.href = "challenge.html?subject=math";
  });
}

/* =========================
   5. HIỆU ỨNG PARALLAX & LƯỚI HÌNH HỌC + KÝ HIỆU TOÁN 60FPS
========================= */
const parallaxBg = document.getElementById("parallaxBg");
const parallaxRelics = document.getElementById("parallaxRelics");
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;

window.addEventListener("mousemove", function (e) {
  mouseX = e.clientX;
  mouseY = e.clientY;
  const nx = e.clientX / window.innerWidth - 0.5;
  const ny = e.clientY / window.innerHeight - 0.5;

  if (parallaxBg) {
    parallaxBg.style.transform = `translate(${nx * 18}px, ${ny * 12}px) scale(1.04)`;
  }
  if (parallaxRelics) {
    parallaxRelics.style.transform = `translate(${nx * -28}px, ${ny * -20}px)`;
  }
});

const canvas = document.getElementById("mathCanvas");
const ctx = canvas ? canvas.getContext("2d") : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

const mathSymbols = ["π", "∑", "∫", "∞", "√x", "Δ", "φ", "±"];
const nodes = Array.from({ length: 34 }, (_, idx) => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  vx: (Math.random() - 0.5) * 0.55,
  vy: (Math.random() - 0.5) * 0.55,
  r: Math.random() * 2.4 + 1.4,
  symbol: idx % 3 === 0 ? mathSymbols[idx % mathSymbols.length] : null,
  color: Math.random() > 0.45 ? "#fde047" : "#2dd4bf"
}));

function renderSacredGeometry() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  for (let i = 0; i < nodes.length; i++) {
    const p = nodes[i];
    p.x += p.vx;
    p.y += p.vy;

    if (p.x < 0 || p.x > cw) p.vx *= -1;
    if (p.y < 0 || p.y > ch) p.vy *= -1;

    ctx.save();
    ctx.fillStyle = p.color;
    ctx.shadowColor = p.color;
    ctx.shadowBlur = 10;

    if (p.symbol) {
      ctx.font = "bold 14px 'Segoe UI', sans-serif";
      ctx.globalAlpha = 0.7;
      ctx.fillText(p.symbol, p.x - 6, p.y + 5);
    } else {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();

    for (let j = i + 1; j < nodes.length; j++) {
      const q = nodes[j];
      const dist = Math.hypot(p.x - q.x, p.y - q.y);
      if (dist < 140) {
        const alpha = (1 - dist / 140) * 0.24;
        ctx.strokeStyle = `rgba(251, 191, 36, ${alpha})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(q.x, q.y);
        ctx.stroke();
      }
    }

    const mDist = Math.hypot(mouseX - p.x, mouseY - p.y);
    if (mDist < 165) {
      ctx.strokeStyle = `rgba(45, 212, 191, ${(1 - mDist / 165) * 0.38})`;
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(p.x, p.y);
      ctx.lineTo(mouseX, mouseY);
      ctx.stroke();
    }
  }

  requestAnimationFrame(renderSacredGeometry);
}
renderSacredGeometry();

// ===== Tài khoản Firebase + HUD (Đồng bộ với Index) =====
(function accountHud() {
    const card = document.getElementById('playerCard');
    if (card) {
        card.addEventListener('click', () => { if (window.HDLG) HDLG.showAccount(); });
    }

    function renderPlayer(d) {
        const nameEl = document.getElementById('playerName');
        const lvlEl = document.getElementById('playerLevel');
        const barEl = document.getElementById('playerXpBar');
        const av = document.getElementById('playerAvatar');

        if (nameEl) nameEl.textContent = d.name || 'Tên người chơi';
        if (lvlEl) lvlEl.textContent = 'Lv.' + (d.level || 1);
        if (barEl) barEl.style.width = (d.inLevel || 0) + '%';
        
        if (av) {
            if (d.photo) {
                av.innerHTML = '';
                const img = document.createElement('img');
                img.src = d.photo; img.referrerPolicy = 'no-referrer'; img.alt = '';
                img.style.cssText = 'width:100%;height:100%;border-radius:50%;object-fit:cover';
                av.appendChild(img);
            } else if (d.name) {
                av.textContent = d.name.charAt(0).toUpperCase();
            }
        }
    }

    window.addEventListener('hdlg:update', e => { renderPlayer(e.detail); });
    if (window.HDLG) HDLG.ready.then(() => { if (HDLG.user) renderPlayer(HDLG.user); });
})();