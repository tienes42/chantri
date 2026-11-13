/* =========================================================
   MATH-GRADE.JS — GIAO DIỆN 3 CẤP: LỚP ➔ CHƯƠNG/CHỦ ĐỀ ➔ BÀI HỌC
   Hỗ trợ Toán Lớp 1 – 12 (SGK Kết nối tri thức với cuộc sống)
   Đồng bộ 100% với Physics & Chemistry + Hỗ trợ Mobile Cuộn Mượt
========================================================= */

// Dọn bộ nhớ đệm sessionStorage cũ để tránh lưu bài gộp cả chương từ phiên bản trước
try {
  Object.keys(sessionStorage).forEach((k) => {
    if ((k.startsWith("hdlg_lesson") || k.startsWith("hdlg_lessons")) && !k.startsWith("hdlg_v9_")) {
      sessionStorage.removeItem(k);
    }
  });
} catch (_) {}

// Mở khóa cuộn trang trên thiết bị di động nếu quay lại từ bfcache
document.body.classList.remove("popup-open");
window.addEventListener("pageshow", () => {
  document.body.classList.remove("popup-open");
});

const API_BASE =
  ["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000"
    ? "http://127.0.0.1:8000/api"
    : "/api";

const params = new URLSearchParams(window.location.search);
let grade = params.get("grade") || localStorage.getItem("selectedMathGrade") || "10";
if (!["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"].includes(String(grade))) {
  grade = "10";
}
try {
  localStorage.setItem("selectedMathGrade", String(grade));
} catch (_) {}
const initialTopicSlug = params.get("topic") || "";

const $ = (id) => document.getElementById(id);

const gradeTitle = $("gradeTitle");
const gradeDescription = $("gradeDescription") || $("gradeSubtitle");
const gradeBadge = $("gradeBadge");
const gradeTabs = $("gradeTabs");
const headerGradeSelect = $("headerGradeSelect");
const topicsGrid = $("topicsGrid");
const topicCount = $("topicCount");
const topicStatLabel = $("topicStatLabel");
const lessonCount = $("lessonCount");
const challengeCount = $("challengeCount") || $("doneCount");
const xpCount = $("xpCount");
const progressPercent = $("progressPercent");
const progressFill = $("progressFill");
const progressText = $("progressText");

const stepHeadingBadge = $("stepHeadingBadge");
const stepHeadingTitle = $("stepHeadingTitle");
const stepHeadingDesc = $("stepHeadingDesc");

const orbFormula1 = $("orbFormula1") || document.querySelector(".floating-number.number-1");
const orbFormula2 = $("orbFormula2") || document.querySelector(".floating-number.number-2");
const orbFormula3 = $("orbFormula3") || document.querySelector(".floating-number.number-3");

const scenarioTitle = $("scenarioTitle");
const scenarioText = $("scenarioText");
const scenarioEquation = $("scenarioEquation");

const topicPopup = $("topicPopup");
const popupClose = $("popupClose");
const popupIcon = $("popupIcon");
const popupLabel = $("popupLabel");
const popupTitle = $("popupTitle");
const popupDescription = $("popupDescription");
const popupLessons = $("popupLessons");
const popupDoneCount = $("popupDoneCount");
const popupXP = $("popupXP");
const popupStart = $("popupStart");
const popupLessonsList = $("popupLessonsList");

const gradeDescriptions = {
  1: "Làm quen với các số từ 0 đến 100, phép cộng – trừ không nhớ, hình phẳng và đo độ dài, thời gian (Toán 1 – Kết nối tri thức).",
  2: "Phép cộng, phép trừ có nhớ trong phạm vi 100 và 1 000, làm quen phép nhân – chia 2, 5, hình khối và thống kê (Toán 2 – Kết nối tri thức).",
  3: "Bảng nhân – chia từ 2 đến 9, các số đến 100 000, chu vi – diện tích hình chữ nhật, hình vuông và xác suất (Toán 3 – Kết nối tri thức).",
  4: "Số tự nhiên đến lớp triệu, bốn phép tính, phân số, góc, hai đường thẳng vuông góc – song song, hình bình hành – hình thoi (Toán 4 – Kết nối tri thức).",
  5: "Số thập phân, tỉ số phần trăm, diện tích hình tam giác – hình thang – hình tròn, thể tích hình hộp và toán chuyển động đều (Toán 5 – Kết nối tri thức).",
  6: "Tập hợp số tự nhiên, số nguyên, phân số, số thập phân, các hình phẳng trong thực tiễn, tính đối xứng và xác suất thực nghiệm (Toán 6 – Kết nối tri thức).",
  7: "Số hữu tỉ, số thực, góc và đường thẳng song song, tam giác bằng nhau, tỉ lệ thức, biểu thức đại số và hình lăng trụ đứng (Toán 7 – Kết nối tri thức).",
  8: "Đa thức nhiều biến, hằng đẳng thức đáng nhớ, phân thức đại số, hàm số bậc nhất, tứ giác, định lí Thalès và tam giác đồng dạng (Toán 8 – Kết nối tri thức).",
  9: "Hệ phương trình bậc nhất hai ẩn, căn bậc hai – căn bậc ba, hệ thức lượng trong tam giác vuông, đường tròn và phương trình bậc hai (Toán 9 – Kết nối tri thức).",
  10: "Mệnh đề – tập hợp, hệ bất phương trình bậc nhất hai ẩn, hệ thức lượng trong tam giác, vectơ, hàm số bậc hai, tọa độ Oxy và đại số tổ hợp (Toán 10 – Kết nối tri thức).",
  11: "Hàm số lượng giác, dãy số – cấp số cộng – cấp số nhân, giới hạn, hàm số mũ – lôgarit, đạo hàm và quan hệ song song – vuông góc trong không gian (Toán 11 – Kết nối tri thức).",
  12: "Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số, nguyên hàm – tích phân, vectơ và phương pháp tọa độ trong không gian Oxyz, xác suất có điều kiện (Toán 12 – Kết nối tri thức)."
};

const gradeHeroFormulas = {
  1: ["5 + 4 = 9", "10 − 3 = 7", "100"],
  2: ["36 + 27", "5 × 4 = 20", "1 km = 1000 m"],
  3: ["S = a × b", "P = (a+b)×2", "8 × 7 = 56"],
  4: ["a/b + c/b", "Góc 90°", "TBC = Tổng : n"],
  5: ["S = π × r²", "v = s : t", "V = a × b × c"],
  6: ["ƯCLN · BCNN", "a + (−b)", "P = k / n"],
  7: ["a/b = c/d", "∑ góc = 180°", "P(x) + Q(x)"],
  8: ["(a+b)²", "a² + b² = c²", "y = ax + b"],
  9: ["Δ = b² − 4ac", "sin α = đối/huyền", "V = πr²h"],
  10: ["a/sin A = 2R", "y = ax² + bx + c", "Cₙᵏ = n!/k!(n−k)!"],
  11: ["sin²x + cos²x = 1", "f'(x₀)", "logₐ(xy)"],
  12: ["∫ f(x)dx", "Oxyz", "P(A|B)"]
};

const gradeScenarios = {
  1: { title: "Đếm và tính tiền mua đồ dùng", text: "Tính tổng số bút chì màu và số tờ tiền khi đi nhà sách.", eq: "Tổng cộng = Số bút hiện có + Số bút mua thêm" },
  2: { title: "Xem đồng hồ & đo chiều cao", text: "Xác định giờ vào lớp và đo chiều dài bàn học bằng dm, cm.", eq: "1 m = 10 dm = 100 cm" },
  3: { title: "Lát gạch nền phòng học", text: "Tính chu vi và diện tích sàn căn phòng hình chữ nhật.", eq: "S = Chiều dài × Chiều rộng" },
  4: { title: "Chia phần bánh & tính trung bình", text: "So sánh các phần phân số và tính số điểm trung bình cộng.", eq: "TBC = (a₁ + a₂ + ... + aₙ) : n" },
  5: { title: "Tính giảm giá & vận tốc", text: "Tính giá sản phẩm sau khi giảm 20% và thời gian di chuyển.", eq: "Giá sau giảm = Giá gốc × (100% − % giảm)" },
  6: { title: "Chia phần thưởng đồng đều", text: "Áp dụng ƯCLN và BCNN để chia đều số quyển vở và bút.", eq: "Số phần nhiều nhất = ƯCLN(a, b)" },
  7: { title: "Pha chế theo tỉ lệ chuẩn", text: "Ứng dụng tỉ lệ thức và tính chất dãy tỉ số bằng nhau.", eq: "x/a = y/b = (x + y)/(a + b)" },
  8: { title: "Đo chiều cao cây bằng bóng nắng", text: "Vận dụng định lí Thalès và tam giác đồng dạng trong thực địa.", eq: "h_cây / h_cọc = d_bóng_cây / d_bóng_cọc" },
  9: { title: "Thiết kế cầu trượt & định vị", text: "Dùng hệ thức lượng trong tam giác vuông để tính độ dốc an toàn.", eq: "h = L · sin α" },
  10: { title: "Tối ưu hóa lợi nhuận sản xuất", text: "Dùng hệ bất phương trình bậc nhất hai ẩn và đỉnh parabol.", eq: "I = −b / (2a) · Lợi nhuận cực đại" },
  11: { title: "Lãi suất kép & tăng trưởng", text: "Ứng dụng cấp số nhân và hàm số mũ – lôgarit trong tài chính.", eq: "A = P · (1 + r)ⁿ" },
  12: { title: "Tối ưu chi phí & xác suất y khoa", text: "Dùng đạo hàm tìm cực trị chi phí và công thức Bayes trong chẩn đoán.", eq: "f'(x) = 0 · P(A|B) = P(AB)/P(B)" }
};

const topicDefaultIcons = [
  "🔢", "📐", "➕", "✖️", "📏", "📊", "🧮", "🧭", "🎲", "📈", "🧊", "🎯", "⏳", "🏆", "🧠", "🔬"
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
  return Number(grade) <= 5 ? "CHỦ ĐỀ" : "CHƯƠNG";
}

function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function initMath25DSprites() {
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
        icon: chapterLesson.icon || "📐",
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
    icon: chapterLesson.icon || "📐",
    parentLesson: chapterLesson
  }];
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
   RENDER GRADE TABS (1..12), HEADER SELECT & PAGE
========================================================= */
function renderGradeTabs() {
  if (headerGradeSelect) {
    headerGradeSelect.value = String(grade);
  }
  if (!gradeTabs) return;
  let html = "";
  for (let g = 1; g <= 12; g++) {
    const active = String(g) === String(grade) ? " active" : "";
    html += `<a href="math-grade.html?grade=${g}" class="grade-tab${active}" data-g="${g}">Lớp ${g}</a>`;
  }
  gradeTabs.innerHTML = html;

  // Tự động cuộn tab đang chọn vào giữa thanh ngang trên điện thoại
  requestAnimationFrame(() => {
    const activeEl = gradeTabs.querySelector(".grade-tab.active");
    if (activeEl && typeof activeEl.scrollIntoView === "function" && window.innerWidth <= 860) {
      activeEl.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    }
  });
}

if (headerGradeSelect) {
  headerGradeSelect.value = String(grade);
  headerGradeSelect.addEventListener("change", function () {
    if (this.value) {
      document.body.classList.remove("popup-open");
      window.location.href = `math-grade.html?grade=${encodeURIComponent(this.value)}`;
    }
  });
}

function renderPage() {
  document.title = `Toán Lớp ${grade} - HỌC ĐỂ LÀM GÌ`;
  renderGradeTabs();

  const isPrimary = Number(grade) <= 5;
  if (gradeTitle) gradeTitle.textContent = `TOÁN LỚP ${grade}`;
  if (gradeDescription) {
    gradeDescription.textContent =
      gradeDescriptions[Number(grade)] ||
      "Khám phá kiến thức Toán học qua từng chương, từng bài học và ứng dụng thực tế.";
  }
  if (gradeBadge) {
    gradeBadge.textContent = `📐 SGK KẾT NỐI TRI THỨC • TOÁN LỚP ${grade}`;
  }

  if (topicStatLabel) {
    topicStatLabel.textContent = isPrimary ? "chủ đề" : "chương học";
  }
  if (stepHeadingBadge) {
    stepHeadingBadge.textContent = isPrimary
      ? "BƯỚC 02 • CHỌN CHỦ ĐỀ ➔ CHỌN BÀI HỌC"
      : "BƯỚC 02 • CHỌN CHƯƠNG ➔ CHỌN BÀI HỌC";
  }
  if (stepHeadingTitle) {
    stepHeadingTitle.textContent = isPrimary ? "Danh sách chủ đề học tập" : "Danh sách chương & chủ đề";
  }
  if (stepHeadingDesc) {
    stepHeadingDesc.textContent = isPrimary
      ? "Bấm vào một chủ đề để mở danh sách từng bài học cụ thể trong chủ đề đó."
      : "Bấm vào một chương để mở danh sách từng bài học cụ thể trong chương đó.";
  }

  const formulas = gradeHeroFormulas[Number(grade)] || ["2x + 3", "πr²", "√x"];
  if (orbFormula1) orbFormula1.textContent = formulas[0];
  if (orbFormula2) orbFormula2.textContent = formulas[1];
  if (orbFormula3) orbFormula3.textContent = formulas[2];

  const sc = gradeScenarios[Number(grade)];
  if (sc) {
    if (scenarioTitle) scenarioTitle.textContent = sc.title;
    if (scenarioText) scenarioText.textContent = sc.text;
    if (scenarioEquation) scenarioEquation.textContent = sc.eq;
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
        <h3>Chưa có chương học cho Lớp ${escapeHTML(grade)}</h3>
        <p>Hãy chạy script <code>python tools/import_math_sgk.py --grades ${escapeHTML(grade)}</code> để nạp dữ liệu.</p>
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
    "&subject=math&grade=" +
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
    popupLabel.textContent = `TOÁN LỚP ${grade} • ${unitLabel} ${String(topicIdx + 1).padStart(2, "0")}`;
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
        document.body.classList.remove("popup-open");
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
      document.body.classList.remove("popup-open");
      window.location.href = buildLessonUrl(nextUnfinished, topic.slug);
    };
  }

  if (topicPopup) {
    topicPopup.classList.add("show");
    topicPopup.setAttribute("aria-hidden", "false");
    document.body.classList.add("popup-open");
  }
}

function closeTopicPopup() {
  if (topicPopup) {
    topicPopup.classList.remove("show");
    topicPopup.setAttribute("aria-hidden", "true");
  }
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
   LOAD LESSONS FROM API
========================================================= */
async function loadLessons() {
  renderGradeTabs();
  if (topicsGrid) {
    topicsGrid.innerHTML = `
      <div class="loading-state">
        Đang tải chương học Toán Lớp ${escapeHTML(grade)}...
      </div>
    `;
  }

  const url = `${API_BASE}/content/subjects/math/lessons?grade=${encodeURIComponent(grade)}`;

  try {
    const cacheKey = `hdlg_v9_lessons_math_${grade}`;
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
        throw new Error("API không trả về danh sách bài học");
      }
      try {
        sessionStorage.setItem(cacheKey, JSON.stringify(data));
      } catch (_) {}
    }
    lessons = data;
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
    console.error("LỖI LOAD MATH LESSONS:", error);
    if (topicsGrid) {
      topicsGrid.innerHTML = `
        <div class="error-state">
          <h3>Không thể tải dữ liệu chương học Toán Lớp ${escapeHTML(grade)}</h3>
          <p>${escapeHTML(error.message)}</p>
          <button type="button" id="retryLessons" class="retry-btn">Thử lại</button>
        </div>
      `;
      const retryBtn = $("retryLessons");
      if (retryBtn) retryBtn.addEventListener("click", loadLessons);
    }
  }
}

/* =========================================================
   NAVIGATION & TOOLS (Đồng bộ với Physics & Chemistry)
========================================================= */
const backButton = $("backButton");
if (backButton) {
  backButton.addEventListener("click", function () {
    document.body.classList.remove("popup-open");
    window.location.href = "math.html";
  });
}

function withGradeProgress(fn) {
  if (window.HDLGProgress) return fn(window.HDLGProgress);
  let s = document.getElementById("gradeProgressScript");
  if (!s) {
    s = document.createElement("script");
    s.id = "gradeProgressScript";
    s.src = "grade-progress.js?v=20261109";
    document.head.appendChild(s);
  }
  s.addEventListener("load", function () {
    if (window.HDLGProgress) fn(window.HDLGProgress);
  });
}

function openGradeProgress() {
  withGradeProgress(function (P) {
    P.open({ subject: "math", grade: grade, getLessons: function () { return lessons; }, apiBase: API_BASE });
  });
}

const progressButton = $("progressButton") || $("progressCard");
if (progressButton) {
  progressButton.addEventListener("click", openGradeProgress);
}

const challengeButton = $("challengeButton") || $("scenarioCard");
if (challengeButton) {
  challengeButton.addEventListener("click", function () {
    document.body.classList.remove("popup-open");
    window.location.href =
      "challenge.html?subject=math&grade=" +
      encodeURIComponent(grade) +
      "&from=" +
      encodeURIComponent(location.pathname + location.search);
  });
}

const calculatorButton = $("calculatorButton") || $("calcCard");
if (calculatorButton) {
  calculatorButton.addEventListener("click", function () {
    document.body.classList.remove("popup-open");
    window.location.href = "calculator.html";
  });
}

/* =========================================================
   PARALLAX & CANVAS THÁNH ĐƯỜNG HÌNH HỌC 60FPS
========================================================= */
const parallaxBg = $("parallaxBg");
const parallaxRelics = $("parallaxRelics");
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

const canvas = $("gradeCanvas");
if (canvas) {
  const ctx = canvas.getContext("2d");
  const mathSyms = ["π", "∑", "√x", "∞", "Δ", "φ"];
  let pts = [];
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  function createParticles() {
    pts = Array.from({ length: 30 }, (_, i) => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 2.2 + 1,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      sym: i % 4 === 0 ? mathSyms[i % mathSyms.length] : null,
      color: i % 2 === 0 ? "#fbbf24" : "#2dd4bf"
    }));
  }
  function animateCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
      ctx.save();
      ctx.fillStyle = p.color;
      if (p.sym) {
        ctx.font = "bold 12px 'Segoe UI', sans-serif";
        ctx.globalAlpha = 0.65;
        ctx.fillText(p.sym, p.x - 5, p.y + 4);
      } else {
        ctx.globalAlpha = 0.55;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }
    requestAnimationFrame(animateCanvas);
  }
  resizeCanvas();
  createParticles();
  animateCanvas();
  window.addEventListener("resize", () => {
    resizeCanvas();
    createParticles();
  });
}

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

initMath25DSprites();
loadLessons();
