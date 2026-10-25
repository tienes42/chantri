/* =========================================================
   HỌC ĐỂ LÀM GÌ — PHYSICS GRADE (2.5D QUANTUM OBSERVATORY)
   Trang chọn chủ đề Vật lý lớp 6 → 12
========================================================= */

const API_BASE =
  ["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000"
    ? "http://127.0.0.1:8000/api"
    : "/api";

const params = new URLSearchParams(window.location.search);
const grade = params.get("grade") || "10";

const $ = (id) => document.getElementById(id);

const gradeTitle = $("gradeTitle");
const gradeDescription = $("gradeDescription");
const topicsGrid = $("topicsGrid");
const topicCount = $("topicCount");
const lessonCount = $("lessonCount");
const challengeCount = $("challengeCount");
const progressPercent = $("progressPercent");
const progressFill = $("progressFill");
const progressText = $("progressText");
const xpCount = $("xpCount");
const xpProgress = $("xpProgress");

const topicPopup = $("topicPopup");
const popupClose = $("popupClose");
const popupIcon = $("popupIcon");
const popupLabel = $("popupLabel");
const popupTitle = $("popupTitle");
const popupDescription = $("popupDescription");
const popupLessons = $("popupLessons");
const popupXP = $("popupXP");
const popupStart = $("popupStart");

let lessons = [];
let topics = [];
let selectedTopic = null;
const slicedSprites = [];

const gradeDescriptions = {
  6: "Đo lường, khối lượng, lực, chuyển động và nhiệt độ — nền tảng để hiểu thế giới vật chất.",
  7: "Khám phá tốc độ, âm thanh, ánh sáng, nam châm và các hiện tượng quang học.",
  8: "Tìm hiểu khối lượng riêng, áp suất, lực đẩy Archimedes, công, nhiệt và điện.",
  9: "Vận dụng điện học, quang học và điện từ học để giải thích nhiều hiện tượng thực tế.",
  10: "Khám phá chuyển động, gia tốc, các định luật Newton, động lượng và năng lượng.",
  11: "Đi sâu vào dao động, sóng, điện trường, dòng điện, từ trường và cảm ứng điện từ.",
  12: "Tiếp cận điện trường, dòng điện xoay chiều, mạch RLC, lượng tử và vật lý hạt nhân."
};

const topicIcons = {
  "do-dai": "📏",
  "khoi-luong": "⚖️",
  "luc": "💪",
  "toc-do": "🏃",
  "nhiet-do": "🌡️",
  "luc-ma-sat": "🛞",
  "toc-do-chuyen-dong": "🚗",
  "am-thanh": "🔊",
  "anh-sang": "💡",
  "guong-phang": "🪞",
  "nam-cham": "🧲",
  "anh-sang-mau": "🌈",
  "khoi-luong-rieng": "🧊",
  "ap-suat": "🎈",
  "luc-day-archimedes": "🚢",
  "cong-suat": "⚙️",
  "nhiet-nang": "🔥",
  "dien": "🔌",
  "dien-tro": "〽️",
  "doan-mach-noi-tiep": "🔗",
  "doan-mach-song-song": "🔀",
  "cong-va-cong-suat-dien": "⚡",
  "dien-tu": "🧲",
  "quang-hoc": "🔭",
  "chuyen-dong-thang": "🚀",
  "gia-toc": "📈",
  "dinh-luat-newton": "⚖️",
  "dong-luong": "💥",
  "nang-luong": "🔋",
  "dong-luc-hoc-chat-long": "🌊",
  "dao-dong": "〰️",
  "song-co": "🌊",
  "dien-truong": "⚡",
  "dong-dien": "🔌",
  "tu-truong": "🧲",
  "cam-ung-dien-tu": "🌀",
  "dien-truong-cuong-do": "⚡",
  "dien-the": "🔋",
  "mach-xoay-chieu": "〽️",
  "mach-rlc": "🔌",
  "hat-nhan": "☢️",
  "quang-dien": "☀️",
  "thuyet-tuong-doi": "🌌"
};

const topicDescriptions = {
  "do-dai": "Đo độ dài bằng dụng cụ thích hợp và biết cách đọc, ghi kết quả đo.",
  "khoi-luong": "Hiểu khối lượng và cách sử dụng cân để đo khối lượng.",
  "luc": "Nhận biết lực, tác dụng của lực và biểu diễn lực.",
  "toc-do": "Mô tả mức độ nhanh chậm của chuyển động bằng tốc độ.",
  "nhiet-do": "Đo và so sánh nhiệt độ, hiểu sự thay đổi nhiệt độ.",
  "luc-ma-sat": "Hiểu lực ma sát và vai trò của nó trong đời sống.",
  "toc-do-chuyen-dong": "Tính và phân tích tốc độ của các chuyển động.",
  "am-thanh": "Khám phá nguồn âm, độ cao, độ to và sự truyền âm.",
  "anh-sang": "Tìm hiểu sự truyền ánh sáng và các hiện tượng ánh sáng.",
  "guong-phang": "Khám phá ảnh của vật qua gương phẳng.",
  "nam-cham": "Tìm hiểu nam châm và tác dụng của từ trường.",
  "anh-sang-mau": "Giải thích màu sắc và sự phân tách ánh sáng.",
  "khoi-luong-rieng": "Tính khối lượng riêng và ứng dụng để nhận biết vật liệu.",
  "ap-suat": "Hiểu áp suất và cách áp suất thay đổi trong các tình huống thực tế.",
  "luc-day-archimedes": "Khám phá lực đẩy của chất lỏng và điều kiện vật nổi, chìm.",
  "cong-suat": "Tính công và công suất trong các quá trình cơ học.",
  "nhiet-nang": "Hiểu nhiệt năng và các cách truyền nhiệt.",
  "dien": "Làm quen với dòng điện, nguồn điện và mạch điện.",
  "dien-tro": "Tìm hiểu điện trở và định luật Ohm.",
  "doan-mach-noi-tiep": "Phân tích cường độ dòng điện và hiệu điện thế trong mạch nối tiếp.",
  "doan-mach-song-song": "Phân tích mạch điện mắc song song và các đại lượng đặc trưng.",
  "cong-va-cong-suat-dien": "Tính điện năng, công suất điện và ứng dụng trong gia đình.",
  "dien-tu": "Khám phá mối liên hệ giữa dòng điện và từ trường.",
  "quang-hoc": "Vận dụng kiến thức ánh sáng, thấu kính và tạo ảnh.",
  "chuyen-dong-thang": "Mô tả vị trí, quãng đường, vận tốc trong chuyển động thẳng.",
  "gia-toc": "Phân tích sự thay đổi vận tốc theo thời gian.",
  "dinh-luat-newton": "Dùng ba định luật Newton để giải thích và dự đoán chuyển động.",
  "dong-luong": "Hiểu động lượng và định luật bảo toàn động lượng.",
  "nang-luong": "Tìm hiểu công, động năng, thế năng và bảo toàn năng lượng.",
  "dong-luc-hoc-chat-long": "Khám phá áp suất và chuyển động của chất lưu.",
  "dao-dong": "Mô tả dao động điều hòa bằng các đại lượng đặc trưng.",
  "song-co": "Tìm hiểu sự truyền sóng và các hiện tượng giao thoa, phản xạ.",
  "dien-truong": "Khám phá điện trường và lực điện tác dụng lên điện tích.",
  "dong-dien": "Hiểu bản chất dòng điện không đổi và các định luật mạch điện.",
  "tu-truong": "Tìm hiểu từ trường và lực từ tác dụng lên dòng điện.",
  "cam-ung-dien-tu": "Khám phá hiện tượng cảm ứng điện từ và suất điện động cảm ứng.",
  "dien-truong-cuong-do": "Tính cường độ điện trường và phân tích điện trường.",
  "dien-the": "Hiểu điện thế, hiệu điện thế và mối liên hệ với công của lực điện.",
  "mach-xoay-chieu": "Phân tích dòng điện xoay chiều và các đại lượng hiệu dụng.",
  "mach-rlc": "Tìm hiểu mạch RLC và hiện tượng cộng hưởng.",
  "hat-nhan": "Khám phá cấu tạo hạt nhân, phóng xạ và năng lượng hạt nhân.",
  "quang-dien": "Tìm hiểu lượng tử ánh sáng và hiện tượng quang điện.",
  "thuyet-tuong-doi": "Làm quen với một số ý tưởng nền tảng của vật lý hiện đại."
};

function escapeHTML(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

/* =========================================================
   TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON VẬT LÝ 2.5D (assets/physics-icons.png)
========================================================= */
function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function initPhysicsGradeSprites() {
  for (let i = 0; i < 16; i++) {
    slicedSprites.push(`assets/sprites/physics_${i}.webp`);
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
  applySprite('[data-sprite="stat1"]', 14);
  applySprite('[data-sprite="stat2"]', 1);
  applySprite('[data-sprite="stat3"]', 9);
  applySprite('[data-sprite="stat4"]', 7);
  applySprite('[data-sprite="calc"]', 8);
  applySprite('[data-sprite="progress"]', 10);
  applySprite('[data-sprite="scenario"]', 5);
  applySprite('[data-prop="p1"]', 12);
  applySprite('[data-prop="p2"]', 13);
  applySprite('[data-prop="p3"]', 14);
  applySprite('[data-prop="p4"]', 15);
  if (topics.length) renderTopics();
}

/* =========================================================
   PROGRESS & TOPICS
========================================================= */
/* Tiến độ THẬT: lấy từ sao đã nhận khi học bài (HDLG.lessonStats trong auth.js) */
function lessonTopicSlug(lesson) {
  return lesson.topic || `topic-${lesson.id}`;
}

function getStats(list) {
  list = list || lessons;
  if (window.HDLG && typeof HDLG.lessonStats === "function") return HDLG.lessonStats(list);
  return { done: 0, total: list.length, stars: 0, maxStars: list.length * 10, percent: 0 };
}

function getProgress() {
  return getStats(lessons).percent;
}

function updateProgress() {
  const stats = getStats(lessons);
  const progress = stats.percent;

  if (progressPercent) progressPercent.textContent = `${progress}%`;
  if (progressFill) progressFill.style.width = `${progress}%`;
  if (progressText) {
    progressText.textContent = `${stats.done} / ${stats.total} bài học hoàn thành`;
  }
  if (xpCount) xpCount.textContent = String(stats.stars);
  if (xpProgress) xpProgress.style.width = `${stats.maxStars ? Math.round(100 * stats.stars / stats.maxStars) : 0}%`;
}

function buildTopics() {
  const map = new Map();

  lessons.forEach(function (lesson) {
    const slug = lesson.topic || `topic-${lesson.id}`;
    if (!map.has(slug)) {
      map.set(slug, {
        slug: slug,
        name: lesson.title || slug,
        description:
          lesson.description ||
          topicDescriptions[slug] ||
          "Khám phá kiến thức Vật lý và cách vận dụng vào thực tế.",
        icon: lesson.icon || topicIcons[slug] || "⚡",
        lessons: 0
      });
    }
    map.get(slug).lessons++;
  });

  topics = [...map.values()];
}

function renderPage() {
  const gradeNumber = Number(grade);
  if (gradeTitle) gradeTitle.textContent = `VẬT LÝ LỚP ${grade}`;
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[gradeNumber] ||
      "Khám phá các quy luật vật lý và ứng dụng trong đời sống.";
  }

  if (topicCount) topicCount.textContent = topics.length;
  if (lessonCount) lessonCount.textContent = lessons.length;
  if (challengeCount) challengeCount.textContent = Math.max(1, topics.length);

  updateProgress();
  renderTopics();
}

function getTopicProgress(index) {
  const topic = topics[index];
  if (!topic) return 0;
  return getStats(lessons.filter(lesson => lessonTopicSlug(lesson) === topic.slug)).percent;
}

function renderTopics() {
  if (!topicsGrid) return;

  if (!topics.length) {
    topicsGrid.innerHTML = `
      <div class="loading-state">
        <strong>Chưa có dữ liệu bài học cho lớp ${escapeHTML(grade)}.</strong>
      </div>
    `;
    return;
  }

  topicsGrid.innerHTML = "";

  topics.forEach(function (topic, index) {
    const progress = getTopicProgress(index);
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
    const iconContent = spriteUrl ? "" : escapeHTML(topic.icon);

    card.innerHTML = `
      <div class="topic-top">
        <div class="topic-icon" ${iconStyle}>${iconContent}</div>
        <span class="topic-number">CHỦ ĐỀ ${String(index + 1).padStart(2, "0")}</span>
      </div>
      <h3>${escapeHTML(topic.name)}</h3>
      <p>${escapeHTML(topic.description)}</p>
      <div class="topic-progress">
        <div class="topic-progress-top">
          <span>${topic.lessons} bài học</span>
          <span>${progress}%</span>
        </div>
        <div class="topic-progress-bar">
          <div class="topic-progress-fill" style="width:${progress}%"></div>
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
   POPUP & LOAD LESSONS
========================================================= */
function openTopic(topic, topicIdx = 0) {
  if (!topic) return;
  selectedTopic = topic;

  const index = topics.findIndex(item => item.slug === topic.slug);
  const progress = getTopicProgress(index);

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

  if (popupLabel) popupLabel.textContent = `VẬT LÝ LỚP ${grade}`;
  if (popupTitle) popupTitle.textContent = topic.name;
  if (popupDescription) popupDescription.textContent = topic.description;
  if (popupLessons) popupLessons.textContent = topic.lessons;
  if (popupXP) popupXP.textContent = topic.lessons * 10;

  if (popupStart) {
    if (progress >= 100) {
      popupStart.innerHTML = "Ôn tập lại <span>→</span>";
    } else if (progress > 0) {
      popupStart.innerHTML = "Tiếp tục học <span>→</span>";
    } else {
      popupStart.innerHTML = "Bắt đầu học <span>→</span>";
    }
  }

  if (topicPopup) {
    topicPopup.classList.add("show");
    topicPopup.setAttribute("aria-hidden", "false");
    document.body.classList.add("popup-open");
  }
}

function closePopup() {
  if (topicPopup) {
    topicPopup.classList.remove("show");
    topicPopup.setAttribute("aria-hidden", "true");
  }
  document.body.classList.remove("popup-open");
  selectedTopic = null;
}

async function loadLessons() {
  // Cập nhật ngay tiêu đề & mô tả theo lớp trên URL trước khi gọi API
  const gradeNumber = Number(grade);
  document.title = `Vật lý lớp ${grade} - HỌC ĐỂ LÀM GÌ`;
  if (gradeTitle) gradeTitle.textContent = `VẬT LÝ LỚP ${grade}`;
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[gradeNumber] ||
      "Khám phá các quy luật vật lý và ứng dụng trong đời sống.";
  }
  if (topicsGrid) {
    topicsGrid.innerHTML = `
      <div class="loading-state">
        Đang tải bài học Vật lý lớp ${escapeHTML(grade)}...
      </div>
    `;
  }

  const url = `${API_BASE}/content/subjects/physics/lessons?grade=${encodeURIComponent(grade)}`;

  try {
    const cacheKey = `hdlg_lessons_physics_${grade}`;
    let data = null;
    const cached = sessionStorage.getItem(cacheKey);
    if (cached) {
      try { data = JSON.parse(cached); } catch (_) {}
    }
    if (!Array.isArray(data) || !data.length) {
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      data = await response.json();
      if (!Array.isArray(data)) {
        throw new Error("API không trả về danh sách bài học.");
      }
      try {
        sessionStorage.setItem(cacheKey, JSON.stringify(data));
        data.forEach(l => {
          if (l && l.id != null) sessionStorage.setItem(`hdlg_lesson_${l.id}`, JSON.stringify(l));
        });
      } catch (_) {}
    }
    lessons = data;
    buildTopics();
    renderPage();
  } catch (error) {
    console.error("LỖI LOAD LESSONS:", error);
    if (topicsGrid) {
      topicsGrid.innerHTML = `
        <div class="error-state">
          <h3>Không thể tải bài học</h3>
          <p>${escapeHTML(error.message)}</p>
          <button type="button" id="retryLessons" class="retry-btn">Thử lại</button>
        </div>
      `;
      const retryButton = $("retryLessons");
      if (retryButton) retryButton.addEventListener("click", loadLessons);
    }
  }
}

const backButton = $("backButton");
if (backButton) {
  backButton.addEventListener("click", function () {
    window.location.href = "physics.html";
  });
}

if (popupClose) popupClose.addEventListener("click", closePopup);
if (topicPopup) {
  topicPopup.addEventListener("click", function (event) {
    if (event.target === topicPopup) closePopup();
  });
}

document.addEventListener("keydown", function (event) {
  if (
    event.key === "Escape" &&
    topicPopup &&
    topicPopup.classList.contains("show")
  ) {
    closePopup();
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
      "&subject=physics&grade=" +
      encodeURIComponent(grade) +
      "&topic=" +
      encodeURIComponent(selectedTopic.slug);

    window.location.href = lessonURL;
  });
}

const challengeButton = $("challengeButton");
if (challengeButton) {
  challengeButton.addEventListener("click", function () {
    alert("Phần thử thách thực tế sẽ kết nối với hệ thống nhiệm vụ và game ở bước tiếp theo.");
  });
}

const calculatorButton = $("calculatorButton");
if (calculatorButton) {
  calculatorButton.addEventListener("click", function () {
    window.location.href = "physics-lab.html";
  });
}

const progressButton = $("progressButton");
if (progressButton) {
  progressButton.addEventListener("click", function () {
    alert("Trang phân tích tiến trình sẽ được kết nối sau khi hoàn thiện hệ thống học và game.");
  });
}

/* =========================================================
   PARALLAX & CANVAS HẠT LƯỢNG TỬ 60FPS
========================================================= */
const parallaxBg = $("parallaxBg");
const parallaxRelics = $("parallaxRelics");

window.addEventListener("mousemove", function (e) {
  const nx = e.clientX / window.innerWidth - 0.5;
  const ny = e.clientY / window.innerHeight - 0.5;
  if (parallaxBg) {
    parallaxBg.style.transform = `translate(${nx * 16}px, ${ny * 10}px) scale(1.04)`;
  }
  if (parallaxRelics) {
    parallaxRelics.style.transform = `translate(${nx * -24}px, ${ny * -16}px)`;
  }
});

const canvas = $("gradeCanvas");
const ctx = canvas ? canvas.getContext("2d") : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

const particles = Array.from({ length: 30 }, () => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  vx: (Math.random() - 0.5) * 0.6,
  vy: (Math.random() - 0.5) * 0.6,
  r: Math.random() * 2.4 + 1.2,
  color: Math.random() > 0.4 ? "#38bdf8" : "#fde047"
}));

function renderQuantumCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  for (let i = 0; i < particles.length; i++) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    if (p.x < 0 || p.x > cw) p.vx *= -1;
    if (p.y < 0 || p.y > ch) p.vy *= -1;

    ctx.save();
    ctx.fillStyle = p.color;
    ctx.shadowColor = p.color;
    ctx.shadowBlur = 10;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    for (let j = i + 1; j < particles.length; j++) {
      const q = particles[j];
      const dist = Math.hypot(p.x - q.x, p.y - q.y);
      if (dist < 135) {
        ctx.strokeStyle = `rgba(56, 189, 248, ${(1 - dist / 135) * 0.22})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(q.x, q.y);
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(renderQuantumCanvas);
}
renderQuantumCanvas();

document.addEventListener("DOMContentLoaded", function () {
  initPhysicsGradeSprites();
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
