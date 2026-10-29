/* =========================================================
   CHEMISTRY PAGE — ĐẠI LÒ GIẢ KIM & THÁNH ĐƯỜNG PHÂN TỬ
   Hóa học → Chọn lớp → chemistry-knowledge.html?grade=...
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
   2. TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON HÓA HỌC 2.5D (assets/chemistry-icons.webp)
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

async function sliceChemistryIcons(src) {
  try {
    const img = await loadImg(src || "assets/chemistry-icons.webp");
    const cellW = img.naturalWidth / 4;
    const cellH = img.naturalHeight / 4;
    const size = 240;
    const c = document.createElement("canvas");
    c.width = size;
    c.height = size;
    const ctx = c.getContext("2d");

    const gridMap = [
      { key: "core",          idx: 0,  selector: '[data-icon="core"]' },
      { key: "g6",            idx: 1,  selector: '[data-icon="g6"] .class-icon' },
      { key: "g7",            idx: 2,  selector: '[data-icon="g7"] .class-icon' },
      { key: "g8",            idx: 3,  selector: '[data-icon="g8"] .class-icon' },
      { key: "g9",            idx: 4,  selector: '[data-icon="g9"] .class-icon' },
      { key: "g10",           idx: 5,  selector: '[data-icon="g10"] .class-icon' },
      { key: "g11",           idx: 6,  selector: '[data-icon="g11"] .class-icon' },
      { key: "g12",           idx: 7,  selector: '[data-icon="g12"] .class-icon' },
      { key: "toolCalc",      idx: 8,  selector: '[data-icon="toolCalc"] .tool-sprite' },
      { key: "toolChallenge", idx: 9,  selector: '[data-icon="toolChallenge"] .tool-sprite' },
      { key: "toolProgress",  idx: 10, selector: '[data-icon="toolProgress"] .tool-sprite' },
      { key: "aiBot",         idx: 11, selector: '[data-icon="aiBot"]' },
      { key: "molecule",      idx: 12, selector: '[data-prop="molecule"]' },
      { key: "burner",        idx: 13, selector: '[data-prop="burner"]' },
      { key: "crystal",       idx: 14, selector: '[data-prop="crystal"]' },
      { key: "coil",          idx: 15, selector: '[data-prop="coil"]' }
    ];

    for (const item of gridMap) {
      const col = item.idx % 4;
      const row = (item.idx / 4) | 0;
      ctx.clearRect(0, 0, size, size);
      ctx.drawImage(img, col * cellW, row * cellH, cellW, cellH, 0, 0, size, size);
      const dataUrl = c.toDataURL("image/png");
      iconSprites[item.key] = dataUrl;
      if (item.selector) {
        document.querySelectorAll(item.selector).forEach(el => {
          el.style.backgroundImage = `url("${dataUrl}")`;
          el.querySelectorAll("span").forEach(sp => { sp.style.display = "none"; });
          if (el.classList.contains("tool-sprite")) el.textContent = "";
        });
      }
    }
  } catch (e) {
    console.info("Đang dùng biểu tượng mặc định:", e);
  }
}

sliceChemistryIcons("assets/chemistry-icons.webp");

/* =========================
   3. CLASS CARDS & POPUP
========================= */
const classCards = document.querySelectorAll(".class-card");
const chemistryPopup = document.getElementById("mathPopup");
const chemistryPopupClose = document.getElementById("mathPopupClose");
const chemistryPopupIcon = document.getElementById("mathPopupIcon");
const chemistryPopupTitle = document.getElementById("mathPopupTitle");
const chemistryPopupText = document.getElementById("mathPopupText");
const chemistryPopupButton = document.getElementById("mathPopupButton");

let selectedGrade = null;
let popupCustomAction = null;

function openChemistryPopup({ iconKey, fallbackEmoji, title, text, buttonLabel, action }) {
  if (chemistryPopupIcon) {
    if (iconSprites[iconKey]) {
      chemistryPopupIcon.style.backgroundImage = `url("${iconSprites[iconKey]}")`;
      chemistryPopupIcon.innerHTML = "";
    } else {
      chemistryPopupIcon.style.backgroundImage = "none";
      chemistryPopupIcon.innerHTML = `<span>${fallbackEmoji || "🧪"}</span>`;
    }
  }
  if (chemistryPopupTitle) chemistryPopupTitle.textContent = title;
  if (chemistryPopupText) chemistryPopupText.textContent = text;
  if (chemistryPopupButton) chemistryPopupButton.textContent = buttonLabel || "Khám phá";

  popupCustomAction = action;
  if (chemistryPopup) {
    chemistryPopup.classList.add("show");
    document.body.classList.add("popup-open");
  }
}

function closeChemistryPopup() {
  if (chemistryPopup) {
    chemistryPopup.classList.remove("show");
    document.body.classList.remove("popup-open");
  }
}

classCards.forEach(function (card) {
  card.addEventListener("click", function () {
    selectedGrade = card.dataset.grade;
    // Prefetch dữ liệu bài học ngay khi bấm chọn lớp để trang sau mở tức thì (0ms)
    try {
      const cacheKey = `hdlg_lessons_chemistry_${selectedGrade}`;
      if (!sessionStorage.getItem(cacheKey)) {
        const apiBase = (["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000") ? "http://127.0.0.1:8000/api" : "/api";
        fetch(`${apiBase}/content/subjects/chemistry/lessons?grade=${encodeURIComponent(selectedGrade)}`)
          .then(r => r.ok ? r.json() : null)
          .then(data => {
            if (Array.isArray(data) && data.length) {
              sessionStorage.setItem(cacheKey, JSON.stringify(data));
              data.forEach(l => {
                if (l && l.id != null) sessionStorage.setItem(`hdlg_lesson_${l.id}`, JSON.stringify(l));
              });
            }
          }).catch(() => {});
      }
    } catch (_) {}
    const iconKey = card.dataset.icon || "core";

    openChemistryPopup({
      iconKey: iconKey,
      fallbackEmoji: "🧪",
      title: "Hóa học lớp " + selectedGrade,
      text:
        "Bạn đã chọn chương trình Hóa học lớp " +
        selectedGrade +
        ". Hãy sẵn sàng khám phá thế giới của nguyên tử, phân tử và các phản ứng hóa học!",
      buttonLabel: "Khám phá",
      action: function () {
        if (selectedGrade !== null) {
          window.location.href = "chemistry-knowledge.html?grade=" + selectedGrade;
        }
      }
    });
  });
});

if (chemistryPopupClose) {
  chemistryPopupClose.addEventListener("click", closeChemistryPopup);
}

if (chemistryPopup) {
  chemistryPopup.addEventListener("click", function (event) {
    if (event.target === chemistryPopup) {
      closeChemistryPopup();
    }
  });
}

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") closeChemistryPopup();
});

if (chemistryPopupButton) {
  chemistryPopupButton.addEventListener("click", function () {
    if (typeof popupCustomAction === "function") {
      const fn = popupCustomAction;
      closeChemistryPopup();
      fn();
    }
  });
}

/* =========================
   4. QUICK TOOLS
========================= */
const calculatorButton = document.getElementById("calculatorButton");
const challengeButton = document.getElementById("challengeButton");
const progressButton = document.getElementById("progressButton");

if (calculatorButton) {
  calculatorButton.addEventListener("click", function () {
    window.location.href = "phong_labhoahoc.html";
  });
}

if (challengeButton) {
  challengeButton.setAttribute("data-hq-badge", "missions");
  challengeButton.style.position = "relative";
  challengeButton.addEventListener("click", function () {
    window.location.href = "challenge.html?subject=chemistry";
  });
}

if (progressButton) {
  progressButton.addEventListener("click", function () {
    if (window.HDLGQ) window.HDLGQ.openProgress("chemistry");
    else window.location.href = "challenge.html?subject=chemistry";
  });
}

/* =========================
   5. HIỆU ỨNG PARALLAX & BỌT KHÍ PHẢN ỨNG + LIÊN KẾT PHÂN TỬ 60FPS
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

const canvas = document.getElementById("chemistryCanvas");
const ctx = canvas ? canvas.getContext("2d") : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

const formulas = ["H₂O", "CO₂", "NaCl", "H₂SO₄", "NH₃", "O₂", "C₆H₆", "Fe"];
const atoms = Array.from({ length: 36 }, (_, idx) => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  vx: (Math.random() - 0.5) * 0.5,
  vy: -(Math.random() * 0.55 + 0.2), // Bọt khí & phân tử bay nhẹ lên trên
  r: Math.random() * 4 + 2,
  formula: idx % 4 === 0 ? formulas[idx % formulas.length] : null,
  color: idx % 3 === 0 ? "#f472b6" : idx % 2 === 0 ? "#34d399" : "#fde047"
}));

function renderAlchemicalReaction() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  for (let i = 0; i < atoms.length; i++) {
    const a = atoms[i];
    a.x += a.vx;
    a.y += a.vy;

    if (a.x < 0 || a.x > cw) a.vx *= -1;
    if (a.y < -30) {
      a.y = ch + 20;
      a.x = Math.random() * cw;
    }

    ctx.save();
    ctx.fillStyle = a.color;
    ctx.strokeStyle = a.color;
    ctx.shadowColor = a.color;
    // shadowBlur removed for smooth 60FPS

    if (a.formula) {
      ctx.font = "bold 13px 'Segoe UI', sans-serif";
      ctx.globalAlpha = 0.72;
      ctx.fillText(a.formula, a.x - 10, a.y + 4);
    } else {
      // Vẽ bọt khí giả kim trong suốt có viền sáng
      ctx.globalAlpha = 0.55;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(a.x, a.y, a.r, 0, Math.PI * 2);
      ctx.stroke();
    }
    ctx.restore();

    // Vẽ liên kết cộng hóa trị giữa các hạt ở gần nhau
    for (let j = i + 1; j < atoms.length; j++) {
      const b = atoms[j];
      const dist = Math.hypot(a.x - b.x, a.y - b.y);
      if (dist < 130) {
        const alpha = (1 - dist / 130) * 0.24;
        ctx.strokeStyle = `rgba(52, 211, 153, ${alpha})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.stroke();
      }
    }

    // Xúc tác phản ứng khi đưa chuột lại gần
    const mDist = Math.hypot(mouseX - a.x, mouseY - a.y);
    if (mDist < 160) {
      ctx.strokeStyle = `rgba(244, 114, 182, ${(1 - mDist / 160) * 0.4})`;
      ctx.lineWidth = 1.3;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(mouseX, mouseY);
      ctx.stroke();
    }
  }

  requestAnimationFrame(renderAlchemicalReaction);
}
renderAlchemicalReaction();

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