/* =========================================================
   MATH GRADE PAGE — CẤU TRÚC 3 CẤP: LỚP ➔ CHƯƠNG/CHỦ ĐỀ ➔ TỪNG BÀI HỌC
   HỌC ĐỂ LÀM GÌ (API VERSION + 2.5D SPRITES)
========================================================= */

const urlParams = new URLSearchParams(window.location.search);
const grade = urlParams.get("grade") || "10";
const initialTopicSlug = urlParams.get("topic") || "";

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
const topicStatLabel = document.getElementById("topicStatLabel");
const lessonCount = document.getElementById("lessonCount");
const challengeCount = document.getElementById("challengeCount");
const progressPercent = document.getElementById("progressPercent");
const progressFill = document.getElementById("progressFill");
const progressText = document.getElementById("progressText");
const xpCount = document.getElementById("xpCount");
const xpProgress = document.getElementById("xpProgress");

const stepHeadingBadge = document.getElementById("stepHeadingBadge");
const stepHeadingTitle = document.getElementById("stepHeadingTitle");
const stepHeadingDesc = document.getElementById("stepHeadingDesc");

const topicPopup = document.getElementById("topicPopup");
const popupClose = document.getElementById("popupClose");
const popupIcon = document.getElementById("popupIcon");
const popupLabel = document.getElementById("popupLabel");
const popupTitle = document.getElementById("popupTitle");
const popupDescription = document.getElementById("popupDescription");
const popupLessons = document.getElementById("popupLessons");
const popupDoneCount = document.getElementById("popupDoneCount");
const popupXP = document.getElementById("popupXP");
const popupLessonsList = document.getElementById("popupLessonsList");
const popupStart = document.getElementById("popupStart");

/* =========================================================
   GRADE INFORMATION & TOPIC MAPPINGS
========================================================= */
const gradeDescriptions = {
  1: "Làm quen với những con số, phép tính và hình dạng đầu tiên qua từng chủ đề và bài học cụ thể.",
  2: "Phát triển khả năng tính toán và tư duy logic theo từng chủ đề và từng bài học SGK.",
  3: "Mở rộng khả năng tính toán và giải quyết vấn đề qua từng chủ đề và từng bài học.",
  4: "Xây dựng nền tảng vững chắc về số học và hình học theo từng chủ đề và bài học.",
  5: "Hoàn thiện nền tảng toán học tiểu học qua hệ thống chủ đề và từng bài học chi tiết.",
  6: "Bước vào thế giới toán học THCS: chọn chương học và khám phá từng bài học cụ thể.",
  7: "Khám phá đại số và hình học thông qua hệ thống chương và từng bài học chi tiết.",
  8: "Phát triển tư duy đại số, hình học và thống kê theo từng chương và từng bài học.",
  9: "Chuẩn bị nền tảng toán học vững chắc cho bậc THPT qua từng chương và từng bài học.",
  10: "Xây dựng nền tảng tư duy toán học THPT theo từng chương và từng bài học chuyên sâu.",
  11: "Tiến sâu vào giải tích, hình học không gian và xác suất theo từng chương và bài học.",
  12: "Chinh phục những kiến thức trọng tâm lớp 12 theo từng chương và từng bài học cụ thể."
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

let lessons = [];
let topics = [];
let selectedTopic = null;
const slicedSprites = [];

let progress = 0;

function escapeHTML(str) {
  return String(str == null ? "" : str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function getChapterUnitLabel() {
  return Number(grade) <= 5 ? "CHỦ ĐỀ" : "CHƯƠNG";
}

/* =========================================================
   TỰ ĐỘNG CẮT & TÁCH NỀN 16 ICON TOÁN 2.5D (assets/math-icons.webp)
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
    const img = await loadImg("assets/math-icons.webp");
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
   TÁCH BÀI HỌC TỰ ĐỘNG NẾU DB ĐANG LƯU GỘP 1 CHƯƠNG = 1 BẢN GHI
========================================================= */
function extractSubLessonsFromCombinedChapter(chapterLesson) {
  const theoryText = String(chapterLesson.theory || "");
  const parts = theoryText.split(/(?=^###\s+)/m).map(s => s.trim()).filter(Boolean);
  const subItems = [];

  parts.forEach((block, idx) => {
    const lines = block.split("\n").map(l => l.trim()).filter(Boolean);
    if (!lines.length) return;
    const rawHeading = lines[0].replace(/^###\s+/, "").trim();
    const bodyLines = lines.slice(1);
    // Bỏ qua tiêu đề Luyện tập chung rỗng không có nội dung
    if (!bodyLines.length && /luyện tập chung|bài tập cuối chương/i.test(rawHeading)) {
      return;
    }
    const summary = bodyLines.length
      ? bodyLines[0].replace(/^[-*•+]\s+/, "").replace(/\$/g, "")
      : chapterLesson.description || "";
    subItems.push({
      id: chapterLesson.id,
      subIndex: idx + 1,
      isVirtualSub: true,
      topic: chapterLesson.topic,
      title: rawHeading,
      description: summary,
      icon: chapterLesson.icon || "📐",
      parentLesson: chapterLesson
    });
  });

  if (subItems.length > 1) return subItems;
  return [{
    id: chapterLesson.id,
    subIndex: null,
    isVirtualSub: false,
    topic: chapterLesson.topic,
    title: chapterLesson.title,
    description: chapterLesson.description || "",
    icon: chapterLesson.icon || "📐",
    parentLesson: chapterLesson
  }];
}

/* =========================================================
   LOAD LESSONS FROM API
========================================================= */
async function loadLessons() {
  try {
    const url = `${API_BASE}/content/subjects/math/lessons?grade=${encodeURIComponent(grade)}`;
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    lessons = await response.json();
    try {
      sessionStorage.setItem(`hdlg_lessons_math_${grade}`, JSON.stringify(lessons));
      lessons.forEach(l => {
        if (l && l.id != null) sessionStorage.setItem(`hdlg_lesson_${l.id}`, JSON.stringify(l));
      });
    } catch (_) {}

    if (!Array.isArray(lessons)) {
      throw new Error("API không trả về danh sách bài học");
    }

    buildTopics();
    renderPage();

    if (initialTopicSlug) {
      const foundIdx = topics.findIndex(t => t.slug === initialTopicSlug);
      if (foundIdx >= 0) {
        openTopic(topics[foundIdx], foundIdx);
      }
    }
  } catch (error) {
    console.error("LỖI LOAD LESSONS:", error);
    if (topicsGrid) {
      topicsGrid.innerHTML = `
        <div class="error-state">
          <h3>Không thể tải dữ liệu bài học</h3>
          <p>${escapeHTML(error.message)}</p>
          <button onclick="location.reload()" class="retry-btn">Thử lại</button>
        </div>
      `;
    }
  }
}

/* =========================================================
   BUILD CHAPTERS (TOPICS) & THEIR INDIVIDUAL LESSONS
========================================================= */
function resolveChapterTitle(firstLesson, index) {
  const ctxTitle = String(firstLesson.context_title || "").trim();
  if (ctxTitle && !/^Ứng dụng thực tế:/i.test(ctxTitle) && !/^Thực tiễn & Ứng dụng/i.test(ctxTitle)) {
    return ctxTitle;
  }
  // Nếu bài học có description kiểu "Chương I · ..." hoặc title chính là tên chương
  return firstLesson.title || `${getChapterUnitLabel()} ${index + 1}`;
}

function resolveChapterDescription(firstLesson, lessonItems) {
  const ctxDesc = String(firstLesson.context || "").trim();
  if (ctxDesc && ctxDesc.length <= 240 && ctxDesc !== firstLesson.real_life) {
    return ctxDesc;
  }
  if (lessonItems.length > 1) {
    const previewNames = lessonItems.slice(0, 3).map(it => it.title).join(" · ");
    return `Gồm ${lessonItems.length} bài học: ${previewNames}${lessonItems.length > 3 ? "…" : ""}`;
  }
  return firstLesson.description || "Khám phá kiến thức Toán học theo từng bài học.";
}

function buildTopics() {
  const topicMap = new Map();

  lessons.forEach(function (lesson) {
    if (!topicMap.has(lesson.topic)) {
      topicMap.set(lesson.topic, {
        slug: lesson.topic,
        rawLessons: [],
        icon: lesson.icon || topicIcons[lesson.topic] || "📚"
      });
    }
    topicMap.get(lesson.topic).rawLessons.push(lesson);
  });

  topics = Array.from(topicMap.values()).map((entry, idx) => {
    const first = entry.rawLessons[0];
    let lessonItems = [];

    if (entry.rawLessons.length > 1) {
      // CSDL đã lưu tách riêng từng Bài học trong cùng 1 Chương (cùng topic)
      lessonItems = entry.rawLessons.map((l, lIdx) => ({
        id: l.id,
        subIndex: null,
        isVirtualSub: false,
        orderNum: lIdx + 1,
        topic: l.topic,
        title: l.title,
        description: l.description || "",
        icon: l.icon || entry.icon,
        rawLesson: l
      }));
    } else {
      // Dự phòng: nếu CSDL vẫn đang có 1 bản ghi gộp cả Chương, tự tách các mục ### Bài X...
      const extracted = extractSubLessonsFromCombinedChapter(first);
      lessonItems = extracted.map((sub, lIdx) => ({
        id: sub.id,
        subIndex: sub.subIndex,
        isVirtualSub: sub.isVirtualSub,
        orderNum: lIdx + 1,
        topic: sub.topic,
        title: sub.title,
        description: sub.description || "",
        icon: sub.icon || entry.icon,
        rawLesson: first
      }));
    }

    const chapterName = resolveChapterTitle(first, idx);
    const chapterDesc = resolveChapterDescription(first, lessonItems);

    return {
      slug: entry.slug,
      name: chapterName,
      description: chapterDesc,
      icon: entry.icon,
      rawLessons: entry.rawLessons,
      lessonItems: lessonItems,
      lessons: lessonItems.length
    };
  });
}

function renderPage() {
  const gradeNumber = Number(grade);
  const isPrimary = gradeNumber <= 5;

  if (gradeTitle) {
    gradeTitle.textContent = `TOÁN LỚP ${grade}`;
  }
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[gradeNumber] ||
      "Khám phá Toán học qua từng chương và từng bài học cụ thể.";
  }

  if (topicStatLabel) {
    topicStatLabel.textContent = isPrimary ? "Chủ đề" : "Chương học";
  }
  if (stepHeadingBadge) {
    stepHeadingBadge.textContent = isPrimary
      ? "BƯỚC 02 • CHỌN CHỦ ĐỀ KIẾN THỨC"
      : "BƯỚC 02 • CHỌN CHƯƠNG KIẾN THỨC";
  }
  if (stepHeadingTitle) {
    stepHeadingTitle.textContent = isPrimary ? "Chọn chủ đề học" : "Chọn chương học";
  }
  if (stepHeadingDesc) {
    stepHeadingDesc.textContent = isPrimary
      ? "Bấm vào một chủ đề để mở danh sách từng bài học bên trong."
      : "Bấm vào một chương để mở danh sách từng bài học bên trong.";
  }

  const totalDisplayedLessons = topics.reduce((sum, t) => sum + t.lessonItems.length, 0);
  if (topicCount) topicCount.textContent = topics.length;
  if (lessonCount) lessonCount.textContent = totalDisplayedLessons;
  if (challengeCount) {
    challengeCount.textContent =
      lessons.filter(l => l && (l.game_type || l.game_title)).length || topics.length;
  }

  updateProgress();
  renderTopics();
}

/* Tiến độ THẬT: lấy từ sao đã nhận khi học bài (HDLG.lessonStats trong auth.js) */
function getStats(list) {
  list = list || lessons;
  if (window.HDLG && typeof HDLG.lessonStats === "function") return HDLG.lessonStats(list);
  return { done: 0, total: list.length, stars: 0, maxStars: list.length * 10, percent: 0 };
}

function getSingleLessonStatus(lessonId) {
  if (window.HDLG && typeof HDLG.lessonStatus === "function") {
    return HDLG.lessonStatus(lessonId) || { read: false, quiz: false, stars: 0 };
  }
  return { read: false, quiz: false, stars: 0 };
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

function getTopicStats(index) {
  const topic = topics[index];
  if (!topic) return { done: 0, total: 0, stars: 0, maxStars: 0, percent: 0 };
  return getStats(topic.rawLessons);
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
  const unitLabel = getChapterUnitLabel();

  topics.forEach(function (topic, index) {
    const tStats = getTopicStats(index);
    const topicProgress = tStats.percent;
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

    const previewItems = topic.lessonItems.slice(0, 3);
    const extraCount = Math.max(0, topic.lessonItems.length - previewItems.length);
    const previewHtml = previewItems
      .map(it => `<span class="topic-lesson-chip">${escapeHTML(it.title)}</span>`)
      .join("") + (extraCount > 0 ? `<span class="topic-lesson-chip is-more">+${extraCount} bài nữa</span>` : "");

    card.innerHTML = `
      <div class="topic-top">
        <div class="topic-icon" ${iconStyle}>${iconContent}</div>
        <span class="topic-number">${unitLabel} ${String(index + 1).padStart(2, "0")}</span>
      </div>
      <h3>${escapeHTML(topic.name)}</h3>
      <p>${escapeHTML(topic.description)}</p>
      <div class="topic-lessons-preview">
        ${previewHtml}
      </div>
      <div class="topic-progress">
        <div class="topic-progress-top">
          <span>📑 ${topic.lessons} bài học (${tStats.done}/${tStats.total} hoàn thành)</span>
          <span>${topicProgress}%</span>
        </div>
        <div class="topic-progress-bar">
          <div class="topic-progress-fill" style="width:${topicProgress}%"></div>
        </div>
      </div>
      <span class="topic-arrow" title="Mở danh sách bài học">Chọn bài →</span>
    `;

    card.addEventListener("click", function () {
      openTopic(topic, index);
    });

    topicsGrid.appendChild(card);
  });
}

/* =========================================================
   CHAPTER -> LESSONS SELECTOR MODAL
========================================================= */
function buildLessonUrl(item, topicSlug) {
  let url =
    "lesson.html?id=" +
    encodeURIComponent(item.id) +
    "&subject=math&grade=" +
    encodeURIComponent(grade) +
    "&topic=" +
    encodeURIComponent(topicSlug);
  if (item.isVirtualSub && item.subIndex) {
    url += "&sub=" + encodeURIComponent(item.subIndex);
  }
  return url;
}

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

  const unitLabel = getChapterUnitLabel();
  const tStats = getTopicStats(topicIdx);

  if (popupLabel) {
    popupLabel.textContent = `TOÁN LỚP ${grade} • ${unitLabel} ${String(topicIdx + 1).padStart(2, "0")}`;
  }
  if (popupTitle) popupTitle.textContent = topic.name;
  if (popupDescription) popupDescription.textContent = topic.description;
  if (popupLessons) popupLessons.textContent = topic.lessons;
  if (popupDoneCount) popupDoneCount.textContent = `${tStats.done}/${tStats.total}`;
  if (popupXP) popupXP.textContent = topic.lessons * 10;

  // Render danh sách từng Bài học trong Chương
  if (popupLessonsList) {
    popupLessonsList.innerHTML = "";
    topic.lessonItems.forEach((item, idx) => {
      const st = getSingleLessonStatus(item.id);
      const isDone = !!(st.read && st.quiz) || st.stars >= 10;
      const inProg = !isDone && (st.read || st.quiz || st.stars > 0);

      let badgeHtml = `<span class="cl-status">⭐ 0/10</span>`;
      if (isDone) {
        badgeHtml = `<span class="cl-status is-done">✓ Đã học • ${st.stars || 10}/10 ⭐</span>`;
      } else if (inProg) {
        badgeHtml = `<span class="cl-status is-progress">⏳ Đang học • ${st.stars}/10 ⭐</span>`;
      }

      const rowBtn = document.createElement("button");
      rowBtn.type = "button";
      rowBtn.className = "chapter-lesson-item" + (isDone ? " is-done" : inProg ? " is-progress" : "");
      rowBtn.setAttribute("role", "listitem");
      rowBtn.innerHTML = `
        <div class="cl-num">${String(idx + 1).padStart(2, "0")}</div>
        <div class="cl-body">
          <div class="cl-title-row">
            <strong class="cl-title">${escapeHTML(item.title)}</strong>
            ${badgeHtml}
          </div>
          ${item.description ? `<p class="cl-desc">${escapeHTML(item.description)}</p>` : ""}
        </div>
        <span class="cl-go">Vào học →</span>
      `;

      rowBtn.addEventListener("click", () => {
        window.location.href = buildLessonUrl(item, topic.slug);
      });

      popupLessonsList.appendChild(rowBtn);
    });
  }

  // Nút CTA dưới đáy: tìm bài đầu tiên chưa hoàn thành trong chương
  const nextUnfinished =
    topic.lessonItems.find(it => {
      const st = getSingleLessonStatus(it.id);
      return !((st.read && st.quiz) || st.stars >= 10);
    }) || topic.lessonItems[0];

  if (popupStart && nextUnfinished) {
    if (tStats.percent >= 100) {
      popupStart.innerHTML = `Ôn lại từ đầu: ${escapeHTML(topic.lessonItems[0].title)} <span>→</span>`;
    } else if (tStats.done > 0) {
      popupStart.innerHTML = `Học tiếp: ${escapeHTML(nextUnfinished.title)} <span>→</span>`;
    } else {
      popupStart.innerHTML = `Bắt đầu: ${escapeHTML(nextUnfinished.title)} <span>→</span>`;
    }
    popupStart.onclick = function () {
      window.location.href = buildLessonUrl(nextUnfinished, topic.slug);
    };
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
    s.src = "/grade-progress.js?v=2";
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

/* Cập nhật lại tiến độ khi sao thay đổi / quay lại trang bằng nút Back */
function refreshRealProgress() {
  if (!lessons.length) return;
  updateProgress();
  renderTopics();
  if (selectedTopic && topicPopup && topicPopup.classList.contains("show")) {
    const idx = topics.findIndex(t => t.slug === selectedTopic.slug);
    if (idx >= 0) openTopic(topics[idx], idx);
  }
}
window.addEventListener("hdlg:update", refreshRealProgress);
window.addEventListener("pageshow", refreshRealProgress);
if (window.HDLG && HDLG.ready && typeof HDLG.ready.then === "function") {
  HDLG.ready.then(refreshRealProgress);
}
