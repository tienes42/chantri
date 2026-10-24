/* =========================================================
   HỌC ĐỂ LÀM GÌ — CHEMISTRY GRADE (2.5D ALCHEMICAL SANCTUM)
   Trang chọn chủ đề Hóa học lớp 6 → 12
   API hiện tại:
   GET http://127.0.0.1:8000/api/content/subjects/chemistry/lessons?grade=6
========================================================= */

const API_BASE =
  ["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000"
    ? "http://127.0.0.1:8000/api"
    : "/api";

const params = new URLSearchParams(window.location.search);
const grade = params.get("grade") || "6";

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
  6: "Khám phá chất, vật liệu, hỗn hợp, dung dịch và những biến đổi hóa học quanh ta.",
  7: "Tìm hiểu nguyên tử, nguyên tố, phân tử, đơn chất, hợp chất và phản ứng hóa học.",
  8: "Làm quen với công thức hóa học, phương trình hóa học, mol, dung dịch và acid-base.",
  9: "Khám phá kim loại, phi kim, hydrocarbon và các vật liệu hóa học trong đời sống.",
  10: "Tìm hiểu cấu tạo nguyên tử, electron, bảng tuần hoàn, liên kết và phản ứng oxi hóa-khử.",
  11: "Đi sâu vào tốc độ phản ứng, cân bằng hóa học, sự điện li và hóa học vô cơ quan trọng.",
  12: "Khám phá hóa học hữu cơ, polymer, điện hóa học và vai trò của hóa học với môi trường."
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
   TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON HÓA HỌC 2.5D (assets/chemistry-icons.png)
========================================================= */
function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function initChemistryGradeSprites() {
  try {
    const img = await loadImg("assets/chemistry-icons.png");
    const cellW = img.naturalWidth / 4;
    const cellH = img.naturalHeight / 4;

    for (let row = 0; row < 4; row++) {
      for (let col = 0; col < 4; col++) {
        const padX = cellW * 0.04;
        const padY = cellH * 0.04;
        const size = 220;
        const c = document.createElement("canvas");
        c.width = size;
        c.height = size;
        const ctx = c.getContext("2d");
        ctx.drawImage(
          img,
          col * cellW + padX,
          row * cellH + padY,
          cellW - padX * 2,
          cellH - padY * 2,
          0,
          0,
          size,
          size
        );

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
            const x = p % size, y = (p / size) | 0;
            if (x > 0) stack.push(p - 1);
            if (x < size - 1) stack.push(p + 1);
            if (y > 0) stack.push(p - size);
            if (y < size - 1) stack.push(p + size);
          }
        }

        for (let i = 0; i < size * size; i++) {
          const idx = i * 4;
          if (d[idx + 3] > 0 && d[idx] > 240 && d[idx + 1] > 240 && d[idx + 2] > 240) {
            d[idx + 3] = 0;
          }
        }

        ctx.putImageData(imgData, 0, 0);
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
    applySprite('[data-sprite="stat1"]', 2);
    applySprite('[data-sprite="stat2"]', 6);
    applySprite('[data-sprite="stat3"]', 9);
    applySprite('[data-sprite="stat4"]', 7);
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

function getTopicProgress(index) {
  const topic = topics[index];
  if (!topic) return 0;
  return getStats(lessons.filter(lesson => lessonTopicSlug(lesson) === topic.slug)).percent;
}

function buildTopics() {
  const map = new Map();

  lessons.forEach((lesson) => {
    const slug = lesson.topic || `topic-${lesson.id}`;
    if (!map.has(slug)) {
      map.set(slug, {
        slug,
        name: lesson.title || slug,
        description:
          lesson.description ||
          "Khám phá kiến thức Hóa học và cách vận dụng vào thực tế.",
        icon: lesson.icon || "🧪",
        lessons: 0
      });
    }
    map.get(slug).lessons++;
  });

  topics = [...map.values()];
}

function renderPage() {
  const gradeNumber = Number(grade);

  if (gradeTitle) gradeTitle.textContent = `HÓA HỌC LỚP ${grade}`;
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[gradeNumber] ||
      "Khám phá kiến thức Hóa học và ứng dụng trong đời sống.";
  }

  if (topicCount) topicCount.textContent = topics.length;
  if (lessonCount) lessonCount.textContent = lessons.length;
  if (challengeCount) challengeCount.textContent = Math.max(1, topics.length);

  updateProgress();
  renderTopics();
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

  topics.forEach((topic, index) => {
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

    card.addEventListener("click", () => openTopic(topic, index));
    topicsGrid.appendChild(card);
  });
}

/* =========================================================
   POPUP & LOAD LESSONS
========================================================= */
function openTopic(topic, topicIdx = 0) {
  if (!topic) return;
  selectedTopic = topic;

  const index = topics.findIndex((item) => item.slug === topic.slug);
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

  if (popupLabel) popupLabel.textContent = `HÓA HỌC LỚP ${grade}`;
  if (popupTitle) popupTitle.textContent = topic.name;
  if (popupDescription) popupDescription.textContent = topic.description;
  if (popupLessons) popupLessons.textContent = topic.lessons;
  if (popupXP) popupXP.textContent = topic.lessons * 10;

  if (popupStart) {
    popupStart.innerHTML =
      progress >= 100
        ? "Ôn tập lại <span>→</span>"
        : progress > 0
          ? "Tiếp tục học <span>→</span>"
          : "Bắt đầu học <span>→</span>";
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
    const gradeNumber = Number(grade);
  document.title = `Hóa học lớp ${grade} - HỌC ĐỂ LÀM GÌ`;
  if (gradeTitle) gradeTitle.textContent = `HÓA HỌC LỚP ${grade}`;
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[gradeNumber] ||
      "Khám phá kiến thức Hóa học và ứng dụng trong đời sống.";
  }
  if (topicsGrid) {
    topicsGrid.innerHTML = `
      <div class="loading-state">
        Đang tải bài học Hóa học lớp ${escapeHTML(grade)}...
      </div>
    `;
  }

  const url = `${API_BASE}/content/subjects/chemistry/lessons?grade=${encodeURIComponent(grade)}`;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);

    const data = await response.json();
    if (!Array.isArray(data)) {
      throw new Error("API không trả về danh sách bài học.");
    }

    lessons = data;
    buildTopics();
    renderPage();
  } catch (error) {
    console.error("LỖI LOAD CHEMISTRY LESSONS:", error);
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
  backButton.addEventListener("click", () => {
    window.location.href = "chemistry.html";
  });
}

if (popupClose) popupClose.addEventListener("click", closePopup);
if (topicPopup) {
  topicPopup.addEventListener("click", (event) => {
    if (event.target === topicPopup) closePopup();
  });
}

document.addEventListener("keydown", (event) => {
  if (
    event.key === "Escape" &&
    topicPopup &&
    topicPopup.classList.contains("show")
  ) {
    closePopup();
  }
});

if (popupStart) {
  popupStart.addEventListener("click", () => {
    if (!selectedTopic || !selectedTopic.slug) return;

    const topicLessons = lessons.filter(
      (lesson) => lesson.topic === selectedTopic.slug
    );
    if (!topicLessons.length) {
      alert("Không tìm thấy bài học.");
      return;
    }

    const firstLesson = topicLessons[0];
    const lessonId = firstLesson.id;

    if (lessonId === undefined || lessonId === null || lessonId === "") {
      alert("Bài học này không có ID từ API.");
      return;
    }

    const lessonURL =
      "lesson.html?id=" +
      encodeURIComponent(lessonId) +
      "&subject=chemistry&grade=" +
      encodeURIComponent(firstLesson.grade || grade) +
      "&topic=" +
      encodeURIComponent(firstLesson.topic || "");

    window.location.href = lessonURL;
  });
}

const challengeButton = $("challengeButton");
if (challengeButton) {
  challengeButton.addEventListener("click", () => {
    alert("Phần thử thách thực tế sẽ kết nối với hệ thống nhiệm vụ và game ở bước tiếp theo.");
  });
}

const calculatorButton = $("calculatorButton");
if (calculatorButton) {
  calculatorButton.addEventListener("click", () => {
    window.location.href = "phong_labhoahoc.html";
  });
}

const progressButton = $("progressButton");
if (progressButton) {
  progressButton.addEventListener("click", () => {
    alert("Trang phân tích tiến trình sẽ được kết nối sau khi hoàn thiện hệ thống học và game.");
  });
}

/* =========================================================
   PARALLAX & CANVAS BỌT KHÍ PHÂN TỬ 60FPS
========================================================= */
const parallaxBg = $("parallaxBg");
const parallaxRelics = $("parallaxRelics");

window.addEventListener("mousemove", (e) => {
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

const formulas = ["H₂O", "CO₂", "NaCl", "H₂SO₄", "NH₃", "O₂"];
const bubbles = Array.from({ length: 30 }, (_, i) => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  vx: (Math.random() - 0.5) * 0.45,
  vy: -(Math.random() * 0.5 + 0.2),
  r: Math.random() * 3.8 + 1.8,
  txt: i % 4 === 0 ? formulas[i % formulas.length] : null,
  color: i % 3 === 0 ? "#f472b6" : "#34d399"
}));

function renderAlchemicalCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  for (let i = 0; i < bubbles.length; i++) {
    const b = bubbles[i];
    b.x += b.vx;
    b.y += b.vy;
    if (b.x < 0 || b.x > cw) b.vx *= -1;
    if (b.y < -25) {
      b.y = ch + 20;
      b.x = Math.random() * cw;
    }

    ctx.save();
    ctx.fillStyle = b.color;
    ctx.strokeStyle = b.color;
    ctx.shadowColor = b.color;
    ctx.shadowBlur = 9;
    if (b.txt) {
      ctx.font = "bold 12px 'Segoe UI', sans-serif";
      ctx.globalAlpha = 0.7;
      ctx.fillText(b.txt, b.x - 10, b.y + 4);
    } else {
      ctx.globalAlpha = 0.55;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.stroke();
    }
    ctx.restore();
  }
  requestAnimationFrame(renderAlchemicalCanvas);
}
renderAlchemicalCanvas();

document.addEventListener("DOMContentLoaded", () => {
  initChemistryGradeSprites();
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
