/* =========================================================
   MATH GRADE PAGE — THÁNH ĐƯỜNG HÌNH HỌC & TỶ LỆ VÀNG
   HỌC ĐỂ LÀM GÌ (API VERSION + 2.5D SPRITES)
========================================================= */

const urlParams = new URLSearchParams(window.location.search);
const grade = urlParams.get("grade") || "10";

const API_BASE =
  ["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000"
    ? "http://127.0.0.1:8000/api"
    : "/api";

/* =========================================================
   ELEMENTS
========================================================= */
const gradeTitle = document.getElementById("gradeTitle");
const gradeDescription = document.getElementById("gradeDescription");
const topicsGrid = document.getElementById("topicsGrid");
const topicCount = document.getElementById("topicCount");
const lessonCount = document.getElementById("lessonCount");
const challengeCount = document.getElementById("challengeCount");
const progressPercent = document.getElementById("progressPercent");
const progressFill = document.getElementById("progressFill");
const progressText = document.getElementById("progressText");
const xpCount = document.getElementById("xpCount");
const xpProgress = document.getElementById("xpProgress");

const topicPopup = document.getElementById("topicPopup");
const popupClose = document.getElementById("popupClose");
const popupIcon = document.getElementById("popupIcon");
const popupLabel = document.getElementById("popupLabel");
const popupTitle = document.getElementById("popupTitle");
const popupDescription = document.getElementById("popupDescription");
const popupLessons = document.getElementById("popupLessons");
const popupXP = document.getElementById("popupXP");
const popupStart = document.getElementById("popupStart");

/* =========================================================
   GRADE INFORMATION & TOPIC MAPPINGS
========================================================= */
const gradeDescriptions = {
  1: "Làm quen với những con số, phép tính và hình dạng đầu tiên.",
  2: "Phát triển khả năng tính toán và tư duy logic.",
  3: "Mở rộng khả năng tính toán và giải quyết vấn đề.",
  4: "Xây dựng nền tảng vững chắc về số học và hình học.",
  5: "Hoàn thiện nền tảng toán học tiểu học.",
  6: "Bước vào thế giới toán học THCS.",
  7: "Khám phá đại số và hình học thông qua tư duy logic.",
  8: "Phát triển tư duy đại số và khả năng giải quyết vấn đề.",
  9: "Chuẩn bị nền tảng toán học cho bậc THPT.",
  10: "Xây dựng nền tảng tư duy toán học và khám phá cách Toán được sử dụng để giải quyết vấn đề.",
  11: "Tiến sâu vào giải tích, hình học và xác suất.",
  12: "Chinh phục những kiến thức trọng tâm và vận dụng Toán vào giải quyết vấn đề."
};

const topicIcons = {
  "so-hoc": "🔢",
  "so-tu-nhien": "🔢",
  "so-huu-ti": "🔢",
  "so-thap-phan": "🔢",
  "so-phuc": "🔢",
  "phep-cong": "➕",
  "phep-tru": "➖",
  "phep-nhan": "✖️",
  "phep-chia": "➗",
  "phan-so": "➗",
  "dai-luong": "📏",
  "do-luong": "📏",
  "hinh-hoc": "📐",
  "du-lieu": "📊",
  "bieu-do": "📊",
  "thong-ke": "📊",
  "ti-so": "🎯",
  "toan-thuc-te": "🎯",
  "ung-dung": "🎯",
  "tu-duy-logic": "🧠",
  "logic": "🧠",
  "bieu-thuc": "🔣",
  "phuong-trinh": "📈",
  "can-thuc": "√",
  "ham-so": "📈",
  "menh-de": "🔣",
  "tap-hop": "🧩",
  "vecto": "➡️",
  "dai-so": "📈",
  "gioi-han": "∞",
  "dao-ham": "∫",
  "nguyen-ham": "∫",
  "xac-suat": "🎲",
  "on-tap-thpt": "🏆"
};

const topicDescriptions = {
  "menh-de": "Làm quen với ngôn ngữ và tư duy logic của Toán học.",
  "tap-hop": "Khám phá tập hợp, phép toán trên tập hợp và ứng dụng.",
  "ham-so": "Hiểu hàm số và cách mô tả sự thay đổi.",
  "vecto": "Khám phá vectơ và các ứng dụng hình học.",
  "hinh-hoc": "Khám phá các kiến thức hình học và ứng dụng.",
  "thong-ke": "Thu thập, biểu diễn và phân tích dữ liệu.",
  "so-hoc": "Làm việc với các số và phép tính.",
  "phep-cong": "Khám phá phép cộng qua những tình huống gần gũi.",
  "phep-tru": "Hiểu cách lấy bớt và tìm phần còn lại.",
  "phep-nhan": "Khám phá phép nhân và ứng dụng.",
  "phep-chia": "Hiểu và vận dụng phép chia.",
  "phan-so": "Khám phá và thực hiện các phép toán với phân số.",
  "dai-luong": "Làm việc với các đại lượng và đơn vị đo.",
  "do-luong": "Làm quen với độ dài, thời gian và đơn vị.",
  "du-lieu": "Thu thập và biểu diễn dữ liệu.",
  "bieu-do": "Đọc và phân tích dữ liệu bằng biểu đồ.",
  "xac-suat": "Khám phá xác suất và các bài toán thực tế.",
  "toan-thuc-te": "Vận dụng Toán học để giải quyết các vấn đề thực tế."
};

let lessons = [];
let topics = [];
let selectedTopic = null;
const slicedSprites = [];

let progress = 0; // tính lại từ số bài đã học thật (xem updateProgress)

/* =========================================================
   TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON TOÁN 2.5D (assets/math-icons.png)
========================================================= */
function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function initMathGradeSprites() {
  try {
    const img = await loadImg("assets/math-icons.png");
    const cellW = img.naturalWidth / 4;
    const cellH = img.naturalHeight / 4;
    const size = 220;
    const c = document.createElement("canvas");
    c.width = size;
    c.height = size;
    const ctx = c.getContext("2d");

    for (let row = 0; row < 4; row++) {
      for (let col = 0; col < 4; col++) {
        ctx.clearRect(0, 0, size, size);
        ctx.drawImage(img, col * cellW, row * cellH, cellW, cellH, 0, 0, size, size);
        slicedSprites.push(c.toDataURL("image/png"));
      }
    }

    const applySprite = (selector, idx) => {
      const url = slicedSprites[idx];
      if (!url) return;
      document.querySelectorAll(selector).forEach(el => {
        el.style.backgroundImage = `url("${url}")`;
        el.querySelectorAll("span").forEach(s => { s.style.display = "none"; });
        if (el.classList.contains("action-sprite")) el.textContent = "";
      });
    };
    applySprite('[data-sprite="core"]', 0);
    applySprite('[data-sprite="stat1"]', 1);
    applySprite('[data-sprite="stat2"]', 2);
    applySprite('[data-sprite="stat3"]', 7);
    applySprite('[data-sprite="stat4"]', 9);
    applySprite('[data-sprite="calc"]', 8);
    applySprite('[data-sprite="progress"]', 10);
    applySprite('[data-sprite="scenario"]', 3);
    applySprite('[data-prop="p1"]', 12);
    applySprite('[data-prop="p2"]', 13);
    applySprite('[data-prop="p3"]', 14);
    applySprite('[data-prop="p4"]', 15);
    if (topics.length) renderTopics();
  } catch (e) {
    console.info("Dùng icon mặc định:", e);
  }
}

/* =========================================================
   LOAD LESSONS FROM API
========================================================= */
async function loadLessons() {
  try {
    const cacheKey = `hdlg_lessons_math_${grade}`;
    const cached = sessionStorage.getItem(cacheKey);
    if (cached) {
      try { lessons = JSON.parse(cached); } catch (_) {}
    }
    if (!Array.isArray(lessons) || !lessons.length) {
      const url = `${API_BASE}/content/subjects/math/lessons?grade=${encodeURIComponent(grade)}`;
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      lessons = await response.json();
      try {
        sessionStorage.setItem(cacheKey, JSON.stringify(lessons));
        lessons.forEach(l => {
          if (l && l.id != null) sessionStorage.setItem(`hdlg_lesson_${l.id}`, JSON.stringify(l));
        });
      } catch (_) {}
    }

    if (!Array.isArray(lessons)) {
      throw new Error("API không trả về danh sách bài học");
    }

    buildTopics();
    renderPage();
  } catch (error) {
    console.error("LỖI LOAD LESSONS:", error);
    if (topicsGrid) {
      topicsGrid.innerHTML = `
        <div class="error-state">
          <h3>Không thể tải dữ liệu bài học</h3>
          <p>${error.message}</p>
          <button onclick="location.reload()" class="retry-btn">Thử lại</button>
        </div>
      `;
    }
  }
}

/* =========================================================
   BUILD TOPICS & RENDER PAGE
========================================================= */
function buildTopics() {
  const topicMap = new Map();

  lessons.forEach(function (lesson) {
    if (!topicMap.has(lesson.topic)) {
      topicMap.set(lesson.topic, {
        slug: lesson.topic,
        name: lesson.title,
        description:
          lesson.description ||
          topicDescriptions[lesson.topic] ||
          "Khám phá kiến thức Toán học.",
        icon: lesson.icon || topicIcons[lesson.topic] || "📚",
        lessons: 0
      });
    }
    topicMap.get(lesson.topic).lessons++;
  });

  topics = Array.from(topicMap.values());
}

function renderPage() {
  const gradeNumber = Number(grade);

  if (gradeTitle) {
    gradeTitle.textContent = `TOÁN LỚP ${grade}`;
  }
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[gradeNumber] ||
      "Khám phá Toán học qua kiến thức và thực hành.";
  }

  const totalLessons = lessons.length;
  if (topicCount) topicCount.textContent = topics.length;
  if (lessonCount) lessonCount.textContent = totalLessons;
  if (challengeCount) {
    challengeCount.textContent = lessons.filter(l => l && (l.game_type || l.game_title)).length || topics.length; // số game Thử thách thực tế thật
  }

  updateProgress(totalLessons);

  renderTopics();
}

/* Tiến độ THẬT: lấy từ sao đã nhận khi học bài (HDLG.lessonStats trong auth.js) */
function getStats(list) {
  list = list || lessons;
  if (window.HDLG && typeof HDLG.lessonStats === "function") return HDLG.lessonStats(list);
  return { done: 0, total: list.length, stars: 0, maxStars: list.length * 10, percent: 0 };
}

function updateProgress() {
  const stats = getStats(lessons);
  progress = stats.percent;

  if (progressPercent) progressPercent.textContent = progress + "%";
  if (progressFill) progressFill.style.width = progress + "%";
  if (progressText) {
    progressText.textContent =
      stats.done + " / " + stats.total + " bài học hoàn thành";
  }
  if (xpCount) xpCount.textContent = stats.stars;
  if (xpProgress) {
    xpProgress.style.width = (stats.maxStars ? Math.round(100 * stats.stars / stats.maxStars) : 0) + "%";
  }
}

function getTopicProgress(index) {
  const topic = topics[index];
  if (!topic) return 0;
  return getStats(lessons.filter(lesson => lesson.topic === topic.slug)).percent;
}

function renderTopics() {
  if (!topicsGrid) return;

  if (!topics.length) {
    topicsGrid.innerHTML = `
      <div class="loading-state">
        <strong>Chưa có dữ liệu bài học cho lớp ${grade}.</strong>
      </div>
    `;
    return;
  }

  topicsGrid.innerHTML = "";

  topics.forEach(function (topic, index) {
    const topicProgress = getTopicProgress(index);
    const card = document.createElement("button");
    card.type = "button";
    card.className = "topic-card";
    card.dataset.topic = topic.slug;

    const spriteUrl = slicedSprites.length
      ? slicedSprites[(index + 1) % slicedSprites.length]
      : null;
    const iconStyle = spriteUrl
      ? `style="background-image:url('${spriteUrl}')"`
      : "";
    const iconContent = spriteUrl ? "" : topic.icon;

    card.innerHTML = `
      <div class="topic-top">
        <div class="topic-icon" ${iconStyle}>${iconContent}</div>
        <span class="topic-number">CHỦ ĐỀ ${String(index + 1).padStart(2, "0")}</span>
      </div>
      <h3>${topic.name}</h3>
      <p>${topic.description}</p>
      <div class="topic-progress">
        <div class="topic-progress-top">
          <span>${topic.lessons} bài học</span>
          <span>${topicProgress}%</span>
        </div>
        <div class="topic-progress-bar">
          <div class="topic-progress-fill" style="width:${topicProgress}%"></div>
        </div>
      </div>
      <span class="topic-arrow">→</span>
    `;

    card.addEventListener("click", function () {
      openTopic(topic, index);
    });

    topicsGrid.appendChild(card);
  });
}

/* =========================================================
   TOPIC POPUP
========================================================= */
function openTopic(topic, topicIdx = 0) {
  if (!topic) return;
  selectedTopic = topic;

  if (popupIcon) {
    const spriteUrl = slicedSprites.length
      ? slicedSprites[(topicIdx + 1) % slicedSprites.length]
      : null;
    if (spriteUrl) {
      popupIcon.style.backgroundImage = `url("${spriteUrl}")`;
      popupIcon.textContent = "";
    } else {
      popupIcon.style.backgroundImage = "none";
      popupIcon.textContent = topic.icon;
    }
  }

  if (popupLabel) popupLabel.textContent = `TOÁN LỚP ${grade}`;
  if (popupTitle) popupTitle.textContent = topic.name;
  if (popupDescription) popupDescription.textContent = topic.description;
  if (popupLessons) popupLessons.textContent = topic.lessons;
  if (popupXP) popupXP.textContent = topic.lessons * 10;

  const topicIndex = topics.findIndex(item => item.slug === topic.slug);
  const topicProgress = getTopicProgress(topicIndex);

  if (popupStart) {
    if (topicProgress >= 100) {
      popupStart.innerHTML = "Ôn tập lại <span>→</span>";
    } else if (topicProgress > 0) {
      popupStart.innerHTML = "Tiếp tục học <span>→</span>";
    } else {
      popupStart.innerHTML = "Bắt đầu học <span>→</span>";
    }
  }

  if (topicPopup) {
    topicPopup.classList.add("show");
    document.body.classList.add("popup-open");
  }
}

function closeTopicPopup() {
  if (topicPopup) topicPopup.classList.remove("show");
  document.body.classList.remove("popup-open");
  selectedTopic = null;
}

if (popupClose) popupClose.addEventListener("click", closeTopicPopup);
if (topicPopup) {
  topicPopup.addEventListener("click", function (event) {
    if (event.target === topicPopup) closeTopicPopup();
  });
}

document.addEventListener("keydown", function (event) {
  if (
    event.key === "Escape" &&
    topicPopup &&
    topicPopup.classList.contains("show")
  ) {
    closeTopicPopup();
  }
});

if (popupStart) {
  popupStart.addEventListener("click", function () {
    if (!selectedTopic || !selectedTopic.slug) return;

    const topicLessons = lessons.filter(
      lesson => lesson.topic === selectedTopic.slug
    );
    if (topicLessons.length === 0) {
      alert("Không tìm thấy bài học.");
      return;
    }

    const firstLesson = topicLessons[0];
    const lessonURL =
      "lesson.html?id=" +
      encodeURIComponent(firstLesson.id) +
      "&subject=math&grade=" +
      encodeURIComponent(grade) +
      "&topic=" +
      encodeURIComponent(selectedTopic.slug);

    window.location.href = lessonURL;
  });
}

/* =========================================================
   NAVIGATION & TOOLS
========================================================= */
const backButton = document.getElementById("backButton");
if (backButton) {
  backButton.addEventListener("click", function () {
    window.location.href = "math.html";
  });
}

/* =========================================================
   TIẾN TRÌNH & THỬ THÁCH THỰC TẾ (grade-progress.js dùng chung)
========================================================= */
function withGradeProgress(fn) {
  if (window.HDLGProgress) return fn(window.HDLGProgress);
  let s = document.getElementById("gradeProgressScript");
  if (!s) {
    s = document.createElement("script");
    s.id = "gradeProgressScript";
    s.src = "/grade-progress.js?v=1";
    document.head.appendChild(s);
  }
  s.addEventListener("load", () => fn(window.HDLGProgress));
  s.addEventListener("error", () => alert("Không tải được bảng tiến trình. Hãy kiểm tra kết nối mạng."));
}
function openGradeProgress() {
  withGradeProgress(P => P.open({ subject: "math", grade, getLessons: () => lessons, apiBase: API_BASE }));
}
function gradeChallengeURL() {
  return "/challenge.html?subject=" + "math" + "&grade=" + encodeURIComponent(grade) +
    "&from=" + encodeURIComponent(location.pathname + location.search);
}

const challengeButton = document.getElementById("challengeButton");
if (challengeButton) {
  challengeButton.addEventListener("click", function () {
    window.location.href = gradeChallengeURL();
  });
}

const calculatorButton = document.getElementById("calculatorButton");
if (calculatorButton) {
  calculatorButton.addEventListener("click", function () {
    window.location.href = "calculator.html";
  });
}

const progressButton = document.getElementById("progressButton");
if (progressButton) {
  progressButton.addEventListener("click", function () {
    openGradeProgress();
  });
}

/* =========================================================
   PARALLAX & CANVAS HÌNH HỌC 60FPS
========================================================= */
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
    parallaxBg.style.transform = `translate(${nx * 16}px, ${ny * 10}px) scale(1.04)`;
  }
  if (parallaxRelics) {
    parallaxRelics.style.transform = `translate(${nx * -24}px, ${ny * -16}px)`;
  }
});

const canvas = document.getElementById("gradeCanvas");
const ctx = canvas ? canvas.getContext("2d") : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

const symbols = ["π", "∑", "∫", "∞", "√x", "Δ", "φ"];
const pts = Array.from({ length: 28 }, (_, i) => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  vx: (Math.random() - 0.5) * 0.5,
  vy: (Math.random() - 0.5) * 0.5,
  r: Math.random() * 2.2 + 1.2,
  sym: i % 4 === 0 ? symbols[i % symbols.length] : null,
  color: i % 2 === 0 ? "#fde047" : "#2dd4bf"
}));

function animateCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  for (let i = 0; i < pts.length; i++) {
    const p = pts[i];
    p.x += p.vx;
    p.y += p.vy;
    if (p.x < 0 || p.x > cw) p.vx *= -1;
    if (p.y < 0 || p.y > ch) p.vy *= -1;

    ctx.save();
    ctx.fillStyle = p.color;
    ctx.shadowColor = p.color;
    ctx.shadowBlur = 8;
    if (p.sym) {
      ctx.font = "bold 13px 'Segoe UI', sans-serif";
      ctx.globalAlpha = 0.65;
      ctx.fillText(p.sym, p.x - 5, p.y + 4);
    } else {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();

    for (let j = i + 1; j < pts.length; j++) {
      const q = pts[j];
      const dist = Math.hypot(p.x - q.x, p.y - q.y);
      if (dist < 135) {
        ctx.strokeStyle = `rgba(251, 191, 36, ${(1 - dist / 135) * 0.2})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(q.x, q.y);
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(animateCanvas);
}
animateCanvas();

document.addEventListener("DOMContentLoaded", function () {
  initMathGradeSprites();
  loadLessons();
});

// ===== Đồng bộ khung Tài khoản người chơi & Sự kiện Click giống trang Index =====
(function accountHudGrade() {
    const card = document.getElementById('playerCard') || document.querySelector('.player');
    if (card) {
        card.style.cursor = 'pointer';
        card.title = 'Tài khoản của tôi';
        card.addEventListener('click', () => {
            if (window.HDLG && typeof HDLG.showAccount === 'function') {
                HDLG.showAccount();
            }
        });
    }

    function renderPlayer(d) {
        if (!d) return;
        const nameEl = document.getElementById('playerName') || document.querySelector('.player-info strong');
        const lvlEl = document.getElementById('playerLevel') || document.querySelector('.player .level');
        const barEl = document.getElementById('playerXpBar') || document.getElementById('xpProgress');
        const txtEl = document.getElementById('playerXpText');
        const av = document.getElementById('playerAvatar') || document.querySelector('.player-avatar');

        const level = d.level || (Math.floor((d.xp || 0) / 100) + 1);
        const inLevel = d.inLevel !== undefined ? d.inLevel : ((d.xp || 0) % 100);

        if (nameEl) nameEl.textContent = d.name || 'Tên người chơi';
        if (lvlEl) lvlEl.textContent = 'Lv.' + level;
        if (barEl) barEl.style.width = inLevel + '%';
        if (txtEl) txtEl.textContent = inLevel + '/100';

        if (av) {
            if (d.photo) {
                av.innerHTML = '';
                const img = document.createElement('img');
                img.src = d.photo;
                img.referrerPolicy = 'no-referrer';
                img.alt = '';
                img.style.cssText = 'width:100%;height:100%;border-radius:50%;object-fit:cover';
                av.appendChild(img);
            } else if (d.name) {
                av.textContent = d.name.charAt(0).toUpperCase();
            }
        }
    }

    window.addEventListener('hdlg:update', e => renderPlayer(e.detail));
    if (window.HDLG && HDLG.ready) {
        HDLG.ready.then(() => {
            if (typeof HDLG.getState === 'function') renderPlayer(HDLG.getState());
            else if (HDLG.user) renderPlayer(HDLG.user);
        });
    }
})();

/* Cập nhật lại tiến độ khi sao thay đổi / quay lại trang bằng nút Back */
function refreshRealProgress() {
  if (!lessons.length) return;
  updateProgress();
  renderTopics();
}
window.addEventListener("hdlg:update", refreshRealProgress);
window.addEventListener("pageshow", refreshRealProgress);
if (window.HDLG && HDLG.ready && typeof HDLG.ready.then === "function") {
  HDLG.ready.then(refreshRealProgress);
}
