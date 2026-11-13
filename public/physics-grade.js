/* =========================================================
   PHYSICS-GRADE.JS — GIAO DIỆN 3 CẤP: LỚP ➔ CHƯƠNG/CHỦ ĐỀ ➔ BÀI HỌC
   Hỗ trợ Vật lý Lớp 6 – 12 (SGK Kết nối tri thức với cuộc sống)
========================================================= */

// Dọn bộ nhớ đệm sessionStorage cũ để tránh lưu bài gộp cả chương từ phiên bản trước
try {
  Object.keys(sessionStorage).forEach((k) => {
    if ((k.startsWith("hdlg_lesson") || k.startsWith("hdlg_lessons")) && !k.startsWith("hdlg_v9_")) {
      sessionStorage.removeItem(k);
    }
  });
} catch (_) {}

const params = new URLSearchParams(window.location.search);
let grade = params.get("grade") || localStorage.getItem("selectedPhysicsGrade") || "6";
if (!["6", "7", "8", "9", "10", "11", "12"].includes(String(grade))) {
  grade = "6";
}
localStorage.setItem("selectedPhysicsGrade", String(grade));
const initialTopicSlug = params.get("topic") || "";

const gradeTitle = document.getElementById("gradeTitle");
const gradeDescription = document.getElementById("gradeDescription");
const gradeBadge = document.getElementById("gradeBadge");
const topicsGrid = document.getElementById("topicsGrid");
const topicCount = document.getElementById("topicCount");
const lessonCount = document.getElementById("lessonCount");
const challengeCount = document.getElementById("challengeCount");
const xpCount = document.getElementById("xpCount");
const progressPercent = document.getElementById("progressPercent");
const progressFill = document.getElementById("progressFill");
const progressText = document.getElementById("progressText");
const gradeTabs = document.getElementById("gradeTabs");
const headerGradeSelect = document.getElementById("headerGradeSelect");
document.body.classList.remove("popup-open");
window.addEventListener("pageshow", () => { document.body.classList.remove("popup-open"); });
if (headerGradeSelect) {
  headerGradeSelect.value = String(grade);
  headerGradeSelect.addEventListener("change", function () {
    if (this.value) {
      document.body.classList.remove("popup-open");
      window.location.href = "physics-grade.html?grade=" + encodeURIComponent(this.value);
    }
  });
}

const topicPopup = document.getElementById("topicPopup");
const popupClose = document.getElementById("popupClose");
const popupIcon = document.getElementById("popupIcon");
const popupLabel = document.getElementById("popupLabel");
const popupTitle = document.getElementById("popupTitle");
const popupDescription = document.getElementById("popupDescription");
const popupLessons = document.getElementById("popupLessons");
const popupDoneCount = document.getElementById("popupDoneCount");
const popupXP = document.getElementById("popupXP");
const popupStart = document.getElementById("popupStart");
const popupLessonsList = document.getElementById("popupLessonsList");

const API_BASE =
  ["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000"
    ? "http://127.0.0.1:8000/api"
    : "/api";

const gradeDescriptions = {
  6: "Đo chiều dài, khối lượng, thời gian, nhiệt độ; lực và tác dụng của lực, trọng lực, ma sát; năng lượng và Trái Đất – Bầu trời (KHTN 6 – Kết nối tri thức).",
  7: "Tốc độ chuyển động, đồ thị quãng đường – thời gian; sóng âm; sự truyền thẳng và phản xạ ánh sáng, gương phẳng; nam châm và từ trường (KHTN 7 – Kết nối tri thức).",
  8: "Khối lượng riêng, áp suất và lực đẩy Archimedes; moment lực và đòn bẩy; điện tích và mạch điện; năng lượng nhiệt và sự truyền nhiệt (KHTN 8 – Kết nối tri thức).",
  9: "Công, công suất, động năng – thế năng; khúc xạ ánh sáng, lăng kính và thấu kính; định luật Ohm, đoạn mạch nối tiếp – song song; cảm ứng điện từ và dòng điện xoay chiều (KHTN 9 – Kết nối tri thức).",
  10: "Sai số phép đo; động học chuyển động biến đổi đều và rơi tự do; ba định luật Newton; công, năng lượng, bảo toàn cơ năng; động lượng, chuyển động tròn và biến dạng vật rắn (Vật lí 10 – Kết nối tri thức).",
  11: "Dao động điều hòa và năng lượng dao động; sóng cơ, sóng điện từ, giao thoa và sóng dừng; định luật Coulomb, điện trường và tụ điện; dòng điện không đổi và định luật Ohm toàn mạch (Vật lí 11 – Kết nối tri thức).",
  12: "Vật lí nhiệt, nội năng và sự chuyển thể; phương trình trạng thái khí lí tưởng; từ trường, cảm ứng điện từ và dòng điện xoay chiều; cấu trúc hạt nhân, phóng xạ và năng lượng hạt nhân (Vật lí 12 – Kết nối tri thức)."
};

const topicDefaultIcons = [
  "⚡", "🧲", "🔭", "🌊", "🔬", "🔋", "🌡️", "🚀", "🌈", "⚛️", "🧭", "📡"
];

let lessons = [];
let topics = [];
let selectedTopic = null;
let slicedSprites = [];

function escapeHTML(value) {
  if (value === null || value === undefined) return "";
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function getChapterUnitLabel() {
  return "CHƯƠNG";
}

function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function initPhysics25DSprites() {
  try {
    const img = await loadImg("assets/physics-icons.webp");
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
    console.info("Dùng icon Vật lý mặc định:", e);
  }
}

/* =========================================================
   TÁCH BÀI HỌC TỰ ĐỘNG NẾU DB ĐANG LƯU GỘP 1 CHƯƠNG = 1 BẢN GHI
   (Đồng bộ chỉ số 0-based `sub=0, 1, 2...` với lesson.js)
========================================================= */
function extractSubLessonsFromCombinedChapter(chapterLesson) {
  const theoryText = String(chapterLesson.theory || "").replace(/\r\n/g, "\n");
  const regex = /^###\s+((?:Bài|Chủ đề|Phần|Mục)\s+[^\n]+)$/gm;
  const matches = [];
  let m;
  while ((m = regex.exec(theoryText)) !== null) {
    matches.push({
      heading: m[1].trim(),
      startIdx: m.index,
      bodyStart: m.index + m[0].length
    });
  }

  const subItems = [];
  if (matches.length >= 2) {
    matches.forEach((item, idx) => {
      const endIdx = idx + 1 < matches.length ? matches[idx + 1].startIdx : theoryText.length;
      const body = theoryText.slice(item.bodyStart, endIdx).trim();
      const bodyLines = body.split("\n").map(l => l.trim()).filter(Boolean);
      if (!bodyLines.length && /luyện tập chung|bài tập cuối chương/i.test(item.heading)) {
        return;
      }
      const firstLine = bodyLines.length
        ? bodyLines[0].replace(/^[-*•+]\s+/, "").replace(/\*\*/g, "").replace(/\$/g, "")
        : (chapterLesson.description || "");
      subItems.push({
        id: chapterLesson.id,
        subIndex: subItems.length,
        isVirtualSub: true,
        topic: chapterLesson.topic,
        title: item.heading.replace(/^(Bài\s+\d+)\.\s*/, "$1: "),
        description: firstLine.slice(0, 145),
        icon: chapterLesson.icon || "⚡",
        parentLesson: chapterLesson
      });
    });
  }

  if (subItems.length > 1) return subItems;
  return [{
    id: chapterLesson.id,
    subIndex: null,
    isVirtualSub: false,
    topic: chapterLesson.topic,
    title: chapterLesson.title,
    description: chapterLesson.description || "",
    icon: chapterLesson.icon || "⚡",
    parentLesson: chapterLesson
  }];
}

/* =========================================================
   LOAD LESSONS FROM API
========================================================= */
async function loadLessons() {
  try {
    const cacheKey = `hdlg_v9_lessons_physics_${grade}`;
    let data = null;
    try {
      const cached = sessionStorage.getItem(cacheKey);
      if (cached) data = JSON.parse(cached);
    } catch (_) {}

    if (!Array.isArray(data) || !data.length) {
      const url = `${API_BASE}/content/subjects/physics/lessons?grade=${encodeURIComponent(grade)}`;
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      data = await response.json();
      try {
        sessionStorage.setItem(cacheKey, JSON.stringify(data));
      } catch (_) {}
    }

    lessons = Array.isArray(data) ? data : [];
    try {
      lessons.forEach(l => {
        if (l && l.id != null) sessionStorage.setItem(`hdlg_v9_lesson_${l.id}`, JSON.stringify(l));
      });
    } catch (_) {}

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
          <h3>Không thể tải dữ liệu bài học Vật lý</h3>
          <p>${escapeHTML(error.message)}</p>
        </div>
      `;
    }
  }
}

/* =========================================================
   GOM CÁC BÀI HỌC THEO CHƯƠNG / CHỦ ĐỀ (CẤU TRÚC 3 CẤP)
========================================================= */
function resolveChapterTitleFromLessons(groupLessons, idx) {
  for (const l of groupLessons) {
    const ct = String(l.context_title || "").trim();
    if (/^(Chương|Chủ đề|Chuyên đề|Phần|Ôn tập)\b/i.test(ct)) {
      return ct;
    }
  }
  if (groupLessons.length === 1) {
    return groupLessons[0].title || `${getChapterUnitLabel()} ${idx + 1}`;
  }
  const firstTitle = String(groupLessons[0].title || "").trim();
  if (/^(Chương|Chủ đề)\b/i.test(firstTitle)) return firstTitle;
  return `${getChapterUnitLabel()} ${idx + 1}: ${firstTitle.replace(/^Bài\s+\d+[:.]\s*/i, "")}`;
}

function resolveChapterDescription(groupLessons, lessonItems) {
  for (const l of groupLessons) {
    const ct = String(l.context_title || "").trim();
    const ctx = String(l.context || "").trim();
    if (/^(Chương|Chủ đề)\b/i.test(ct) && ctx && ctx.length <= 220) {
      return ctx.replace(/\$/g, "");
    }
  }
  if (groupLessons.length === 1 && groupLessons[0].description) {
    return groupLessons[0].description;
  }
  const sampleNames = lessonItems
    .slice(0, 4)
    .map(it => it.title.replace(/^Bài\s+\d+[:.]?\s*/i, ""))
    .join(" · ");
  return `Gồm ${lessonItems.length} bài học: ${sampleNames}${lessonItems.length > 4 ? "..." : ""}`;
}

function buildTopics() {
  const topicMap = new Map();

  lessons.forEach((lesson) => {
    const key = lesson.topic || `topic-${lesson.id}`;
    if (!topicMap.has(key)) {
      topicMap.set(key, []);
    }
    topicMap.get(key).push(lesson);
  });

  topics = [];
  let idx = 0;

  topicMap.forEach((groupLessons, key) => {
    groupLessons.sort((a, b) => (a.order || a.id || 0) - (b.order || b.id || 0));

    let lessonItems = [];
    if (groupLessons.length === 1) {
      lessonItems = extractSubLessonsFromCombinedChapter(groupLessons[0]);
    } else {
      lessonItems = groupLessons.map((l) => ({
        id: l.id,
        subIndex: null,
        isVirtualSub: false,
        topic: key,
        title: l.title || "Bài học",
        description: l.description || "",
        icon: l.icon || topicDefaultIcons[idx % topicDefaultIcons.length],
        parentLesson: l
      }));
    }

    const chapterName = resolveChapterTitleFromLessons(groupLessons, idx);
    const chapterDesc = resolveChapterDescription(groupLessons, lessonItems);

    topics.push({
      slug: key,
      name: chapterName,
      description: chapterDesc,
      icon: groupLessons[0].icon || topicDefaultIcons[idx % topicDefaultIcons.length],
      lessons: lessonItems.length,
      rawLessons: groupLessons,
      lessonItems: lessonItems
    });
    idx++;
  });
}

/* =========================================================
   PROGRESS HELPERS
========================================================= */
function getSingleLessonStatus(lessonId) {
  if (window.HDLG && typeof HDLG.lessonStatus === "function" && lessonId != null) {
    return HDLG.lessonStatus(lessonId);
  }
  return { read: false, quiz: false, stars: 0 };
}

function getTopicStats(index) {
  const tp = topics[index];
  if (!tp || !tp.rawLessons || !tp.rawLessons.length) {
    return { done: 0, total: 0, stars: 0, maxStars: 0, percent: 0 };
  }
  let done = 0;
  let stars = 0;
  const maxStars = tp.rawLessons.length * 10;

  tp.rawLessons.forEach((l) => {
    const st = getSingleLessonStatus(l.id);
    if ((st.read && st.quiz) || st.stars >= 10) done++;
    stars += Math.min(10, st.stars || 0);
  });

  const percent = maxStars > 0 ? Math.round((stars / maxStars) * 100) : 0;
  if (tp.rawLessons.length === 1 && tp.lessonItems.length > 1) {
    const st = getSingleLessonStatus(tp.rawLessons[0].id);
    const virtualDone = st.read && st.quiz ? tp.lessonItems.length : st.read || st.quiz ? Math.ceil(tp.lessonItems.length / 2) : 0;
    return {
      done: virtualDone,
      total: tp.lessonItems.length,
      stars: st.stars || 0,
      maxStars: tp.lessonItems.length * 10,
      percent: percent
    };
  }

  return {
    done: done,
    total: tp.lessonItems.length,
    stars: stars,
    maxStars: maxStars,
    percent: percent
  };
}

function getOverallProgress() {
  if (!topics.length) return { percent: 0, totalDone: 0, totalLessons: 0, totalStars: 0 };
  let totalDone = 0;
  let totalLessons = 0;
  let totalStars = 0;
  let totalMaxStars = 0;

  topics.forEach((_, idx) => {
    const st = getTopicStats(idx);
    totalDone += st.done;
    totalLessons += st.total;
    totalStars += st.stars;
    totalMaxStars += st.maxStars;
  });

  const percent = totalMaxStars > 0 ? Math.round((totalStars / totalMaxStars) * 100) : 0;
  return { percent, totalDone, totalLessons, totalStars };
}

/* =========================================================
   RENDER GRADE TABS (6..12) & PAGE
========================================================= */
function renderGradeTabs() {
  if (headerGradeSelect) headerGradeSelect.value = String(grade);
  if (!gradeTabs) return;
  let html = "";
  for (let g = 6; g <= 12; g++) {
    const active = String(g) === String(grade) ? " active" : "";
    html += `<a href="physics-grade.html?grade=${g}" class="grade-tab${active}" data-g="${g}">Lớp ${g}</a>`;
  }
  gradeTabs.innerHTML = html;
  requestAnimationFrame(() => {
    const activeEl = gradeTabs.querySelector(".grade-tab.active");
    if (activeEl && typeof activeEl.scrollIntoView === "function" && window.innerWidth <= 860) {
      activeEl.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    }
  });
}
renderGradeTabs();

function renderPage() {
  document.title = `Vật lý Lớp ${grade} - HỌC ĐỂ LÀM GÌ`;
  renderGradeTabs();

  if (gradeTitle) gradeTitle.textContent = `VẬT LÝ LỚP ${grade}`;
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[grade] ||
      "Khám phá các quy luật của chuyển động, lực, năng lượng và thế giới tự nhiên qua từng bài học.";
  }
  if (gradeBadge) {
    gradeBadge.textContent = `⚡ SGK KẾT NỐI TRI THỨC • LỚP ${grade}`;
  }

  const ov = getOverallProgress();
  if (topicCount) topicCount.textContent = topics.length;
  if (lessonCount) lessonCount.textContent = ov.totalLessons;
  if (challengeCount) challengeCount.textContent = `${ov.totalDone}/${ov.totalLessons}`;
  if (xpCount) xpCount.textContent = ov.totalLessons * 10;

  if (progressPercent) progressPercent.textContent = `${ov.percent}%`;
  if (progressFill) progressFill.style.width = `${ov.percent}%`;
  if (progressText) {
    progressText.textContent =
      `${ov.totalDone} / ${ov.totalLessons} bài học hoàn thành` +
      (ov.totalStars ? ` · ⭐ ${ov.totalStars}/${ov.totalLessons * 10}` : "");
  }

  renderTopics();
}

function renderTopics() {
  if (!topicsGrid) return;
  topicsGrid.innerHTML = "";

  if (!topics.length) {
    topicsGrid.innerHTML = `
      <div class="empty-state">
        <h3>Chưa có chương học Vật lý cho Lớp ${escapeHTML(grade)}</h3>
        <p>Hãy chạy script <code>python tools/import_physics_sgk.py --grades ${escapeHTML(grade)}</code> để nạp dữ liệu.</p>
      </div>
    `;
    return;
  }

  const unitLabel = getChapterUnitLabel();

  topics.forEach((topic, index) => {
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
    "&subject=physics&grade=" +
    encodeURIComponent(grade) +
    "&topic=" +
    encodeURIComponent(topicSlug);
  if (item.isVirtualSub && typeof item.subIndex === "number") {
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
    popupLabel.textContent = `VẬT LÝ LỚP ${grade} • ${unitLabel} ${String(topicIdx + 1).padStart(2, "0")}`;
  }
  if (popupTitle) popupTitle.textContent = topic.name;
  if (popupDescription) popupDescription.textContent = topic.description;
  if (popupLessons) popupLessons.textContent = topic.lessons;
  if (popupDoneCount) popupDoneCount.textContent = `${tStats.done}/${tStats.total}`;
  if (popupXP) popupXP.textContent = topic.lessons * 10;

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
    window.location.href = "physics.html";
  });
}

const challengeButton = document.getElementById("challengeButton");
if (challengeButton) {
  challengeButton.addEventListener("click", function () {
    window.location.href =
      "challenge.html?subject=physics&grade=" +
      encodeURIComponent(grade) +
      "&from=" +
      encodeURIComponent(location.pathname + location.search);
  });
}

const calculatorButton = document.getElementById("calculatorButton");
if (calculatorButton) {
  calculatorButton.addEventListener("click", function () {
    window.location.href = `physics-tools.html?grade=${encodeURIComponent(grade)}`;
  });
}

function withGradeProgress(fn) {
  if (window.HDLGProgress) return fn(window.HDLGProgress);
  let s = document.getElementById("gradeProgressScript");
  if (!s) {
    s = document.createElement("script");
    s.id = "gradeProgressScript";
    s.src = "grade-progress.js";
    document.head.appendChild(s);
  }
  s.addEventListener("load", function () {
    if (window.HDLGProgress) fn(window.HDLGProgress);
  });
}

const progressButton = document.getElementById("progressButton");
if (progressButton) {
  progressButton.addEventListener("click", function () {
    withGradeProgress(function (P) {
      P.open({ subject: "physics", grade: grade, getLessons: function () { return lessons; }, apiBase: API_BASE });
    });
  });
}

window.addEventListener("hdlg:update", function () {
  if (topics.length) renderPage();
});

/* =========================================================
   2.5D PARALLAX & AMBIENT PARTICLES
========================================================= */
const parallaxBg = document.getElementById("parallaxBg");
const parallaxRelics = document.getElementById("parallaxRelics");
window.addEventListener("mousemove", (e) => {
  const nx = e.clientX / window.innerWidth - 0.5;
  const ny = e.clientY / window.innerHeight - 0.5;
  if (parallaxBg) {
    parallaxBg.style.transform = `translate(${nx * 14}px,${ny * 10}px) scale(1.04)`;
  }
  if (parallaxRelics) {
    parallaxRelics.style.transform = `translate(${nx * -24}px,${ny * -16}px)`;
  }
});

const canvas = document.getElementById("gradeCanvas");
if (canvas) {
  const ctx = canvas.getContext("2d");
  let particles = [];
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  function createParticles() {
    particles = [];
    for (let i = 0; i < 34; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 2 + 0.6,
        vx: (Math.random() - 0.5) * 0.28,
        vy: (Math.random() - 0.5) * 0.28
      });
    }
  }
  function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach((p) => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) p.x = canvas.width;
      if (p.x > canvas.width) p.x = 0;
      if (p.y < 0) p.y = canvas.height;
      if (p.y > canvas.height) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(56, 189, 248, 0.35)";
      ctx.fill();
    });
    requestAnimationFrame(animateParticles);
  }
  resizeCanvas();
  createParticles();
  animateParticles();
  window.addEventListener("resize", () => {
    resizeCanvas();
    createParticles();
  });
}

initPhysics25DSprites();
loadLessons();


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
