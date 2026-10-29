/* =========================================================
   PHYSICS PAGE — ĐÀI THIÊN VĂN LƯỢNG TỬ & THỰC NGHIỆM
   Vật lý → Chọn lớp → Danh sách bài học
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
   2. TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON VẬT LÝ 2.5D (assets/physics-icons.webp)
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

async function slicePhysicsIcons(src) {
  try {
    const img = await loadImg(src || "assets/physics-icons.webp");
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
      { key: "gyro",          idx: 12, selector: '[data-prop="gyro"]' },
      { key: "prism",         idx: 13, selector: '[data-prop="prism"]' },
      { key: "magnet",        idx: 14, selector: '[data-prop="magnet"]' },
      { key: "gear",          idx: 15, selector: '[data-prop="gear"]' }
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

slicePhysicsIcons("assets/physics-icons.webp");

/* =========================
   3. CLASS CARDS & POPUP MODAL
========================= */
const classCards = document.querySelectorAll(".class-card");
const physicsPopup = document.getElementById("mathPopup");
const physicsPopupClose = document.getElementById("mathPopupClose");
const physicsPopupIcon = document.getElementById("mathPopupIcon");
const physicsPopupTitle = document.getElementById("mathPopupTitle");
const physicsPopupText = document.getElementById("mathPopupText");
const physicsPopupButton = document.getElementById("mathPopupButton");

let selectedGrade = null;
let popupCustomAction = null;

function openPhysicsPopup({ iconKey, fallbackEmoji, title, text, buttonLabel, action }) {
  if (physicsPopupIcon) {
    if (iconSprites[iconKey]) {
      physicsPopupIcon.style.backgroundImage = `url("${iconSprites[iconKey]}")`;
      physicsPopupIcon.innerHTML = "";
    } else {
      physicsPopupIcon.style.backgroundImage = "none";
      physicsPopupIcon.innerHTML = `<span>${fallbackEmoji || "⚡"}</span>`;
    }
  }
  if (physicsPopupTitle) physicsPopupTitle.textContent = title;
  if (physicsPopupText) physicsPopupText.textContent = text;
  if (physicsPopupButton) physicsPopupButton.textContent = buttonLabel || "Khám phá";

  popupCustomAction = action;
  if (physicsPopup) {
    physicsPopup.classList.add("show");
    document.body.classList.add("popup-open");
  }
}

function closePhysicsPopup() {
  if (physicsPopup) {
    physicsPopup.classList.remove("show");
    document.body.classList.remove("popup-open");
  }
}

classCards.forEach(function (card) {
  card.addEventListener("click", function () {
    selectedGrade = card.dataset.grade;
    // Prefetch dữ liệu bài học ngay khi bấm chọn lớp để trang sau mở tức thì (0ms)
    try {
      const cacheKey = `hdlg_lessons_physics_${selectedGrade}`;
      if (!sessionStorage.getItem(cacheKey)) {
        const apiBase = (["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000") ? "http://127.0.0.1:8000/api" : "/api";
        fetch(`${apiBase}/content/subjects/physics/lessons?grade=${encodeURIComponent(selectedGrade)}`)
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

    openPhysicsPopup({
      iconKey: iconKey,
      fallbackEmoji: "⚡",
      title: "Phòng Thí Nghiệm Vật Lý Lớp " + selectedGrade,
      text:
        "Bạn đã kích hoạt mô-đun Vật lý lớp " +
        selectedGrade +
        ". Hãy bắt đầu hành trình giải mã các định luật tự nhiên và thử sức qua các tình huống thực tế!",
      buttonLabel: "Bắt đầu Khám phá →",
      action: function () {
        window.location.href =
          "physics-grade.html?grade=" + encodeURIComponent(selectedGrade);
      }
    });
  });
});

if (physicsPopupClose) {
  physicsPopupClose.addEventListener("click", closePhysicsPopup);
}

if (physicsPopup) {
  physicsPopup.addEventListener("click", function (event) {
    if (event.target === physicsPopup) {
      closePhysicsPopup();
    }
  });
}

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") closePhysicsPopup();
});

if (physicsPopupButton) {
  physicsPopupButton.addEventListener("click", function () {
    if (typeof popupCustomAction === "function") {
      const fn = popupCustomAction;
      closePhysicsPopup();
      fn();
    }
  });
}

/* =========================
   4. QUICK TOOLS
========================= */
const challengeButton = document.getElementById("challengeButton");
const progressButton = document.getElementById("progressButton");

if (challengeButton) {
  challengeButton.setAttribute("data-hq-badge", "missions");
  challengeButton.style.position = "relative";
  challengeButton.addEventListener("click", function () {
    window.location.href = "challenge.html?subject=physics";
  });
}

if (progressButton) {
  progressButton.addEventListener("click", function () {
    if (window.HDLGQ) window.HDLGQ.openProgress("physics");
    else window.location.href = "challenge.html?subject=physics";
  });
}

/* =========================
   5. HIỆU ỨNG PARALLAX & MẠNG LƯỚI LƯỢNG TỬ 60FPS TRÊN CANVAS
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

const canvas = document.getElementById("physicsCanvas");
const ctx = canvas ? canvas.getContext("2d") : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

// Tạo các hạt lượng tử liên kết với nhau như mạng lưới điện từ
const particles = Array.from({ length: 38 }, () => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  vx: (Math.random() - 0.5) * 0.65,
  vy: (Math.random() - 0.5) * 0.65,
  r: Math.random() * 2.5 + 1.2,
  color: Math.random() > 0.4 ? "#38bdf8" : "#fde047"
}));

function renderQuantumField() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  for (let i = 0; i < particles.length; i++) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;

    if (p.x < 0 || p.x > cw) p.vx *= -1;
    if (p.y < 0 || p.y > ch) p.vy *= -1;

    // Vẽ hạt phát sáng
    ctx.save();
    ctx.fillStyle = p.color;
    ctx.shadowColor = p.color;
    // shadowBlur removed for smooth 60FPS
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // Vẽ đường sức điện từ nối giữa các hạt gần nhau
    for (let j = i + 1; j < particles.length; j++) {
      const q = particles[j];
      const dx = p.x - q.x;
      const dy = p.y - q.y;
      const dist = Math.hypot(dx, dy);
      if (dist < 135) {
        const alpha = (1 - dist / 135) * 0.25;
        ctx.strokeStyle = `rgba(56, 189, 248, ${alpha})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(q.x, q.y);
        ctx.stroke();
      }
    }

    // Tương tác lực hút nhẹ với con trỏ chuột
    const mdx = mouseX - p.x;
    const mdy = mouseY - p.y;
    const mDist = Math.hypot(mdx, mdy);
    if (mDist < 160) {
      ctx.strokeStyle = `rgba(253, 224, 71, ${(1 - mDist / 160) * 0.35})`;
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(p.x, p.y);
      ctx.lineTo(mouseX, mouseY);
      ctx.stroke();
    }
  }

  requestAnimationFrame(renderQuantumField);
}
renderQuantumField();

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