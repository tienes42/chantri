/* =========================================================

   MATH / SUBJECT GRADE PAGE (UPGRADED)

   PostgreSQL -> FastAPI -> Frontend

========================================================= */



const API_BASE = "http://127.0.0.1:8000/api";



/* =========================

   GET PARAMS (GRADE & SUBJECT)

========================= */



const params = new URLSearchParams(window.location.search);

const grade = params.get("grade") || "10";

const subjectSlug = params.get("subject") || "math";



const subjectLabels = {

    math: "TOÁN",

    physics: "VẬT LÝ",

    chemistry: "HÓA HỌC"

};



/* =========================

   ELEMENTS

========================= */



const backButton = document.getElementById("backButton");

const gradeTitle = document.getElementById("gradeTitle");

const gradeDescription = document.getElementById("gradeDescription");

const topicsGrid = document.getElementById("topicsGrid");

const topicCount = document.getElementById("topicCount");

const lessonCount = document.getElementById("lessonCount");

const xpCount = document.getElementById("xpCount");

const challengeCount = document.getElementById("challengeCount");

const progressPercent = document.getElementById("progressPercent");

const progressFill = document.getElementById("progressFill");

const progressText = document.getElementById("progressText");

const challengeButton = document.getElementById("challengeButton");

const topicPopup = document.getElementById("topicPopup");

const popupClose = document.getElementById("popupClose");

const popupIcon = document.getElementById("popupIcon");

const popupLabel = document.getElementById("popupLabel");

const popupTitle = document.getElementById("popupTitle");

const popupDescription = document.getElementById("popupDescription");

const popupLessons = document.getElementById("popupLessons");

const popupXP = document.getElementById("popupXP");

const popupStart = document.getElementById("popupStart");



/* =========================

   TOPIC ICONS (FALLBACK DICTIONARY)

========================= */



const topicIcons = {

    // Toán 1-9

    "so-hoc": "🔢",

    "phep-cong": "➕",

    "phep-tru": "➖",

    "phep-nhan": "✖️",

    "phep-chia": "➗",

    "do-luong": "📏",

    "dai-luong": "⚖️",

    "quy-luat-logic": "🧩",

    "phep-chia-hinh-khoi": "➗",

    "so-tu-nhien": "🔢",

    "du-lieu": "📊",

    "lam-quen-phan-so": "🍕",

    "phan-so": "🍰",

    "bieu-do": "📊",

    "trung-binh-cong-tong-hieu": "🧮",

    "so-thap-phan": "🔢",

    "ti-so": "🗺️",

    "ti-so-phan-tram-chuyen-dong": "🚄",

    "toan-thuc-te": "🌍",

    "so-nguyen-chia-het": "🌡️",

    "tu-duy-logic": "🧠",

    "so-huu-ti": "➗",

    "ti-le-thuc-so-thuc": "⚖️",

    "dai-so": "🔤",

    "ung-dung": "🏦",

    "bieu-thuc": "🔤",

    "hang-dang-thuc-phan-thuc": "⚡",

    "phuong-trinh": "⚖️",

    "logic": "🧠",

    "can-thuc": "√",

    "he-thuc-viete-hinh-khong-gian": "🌐",

    // Toán 10-12

    "menh-de": "💡",

    "tap-hop": "⭕",

    "bat-phuong-trinh": "📊",

    "ham-so": "📈",

    "vecto": "➡️",

    "hinh-hoc": "📐",

    "to-hop-xac-suat": "🎲",

    "thong-ke": "📊",

    "day-so-cap-so": "📶",

    "gioi-han": "♾️",

    "mu-logarit": "🚀",

    "dao-ham": "⚡",

    "xac-suat": "🎲",

    "nguyen-ham": "∫",

    "tich-phan": "📐",

    "thong-ke-ghep-nhom": "📊",

    "so-phuc": "🌀",

    "on-tap-thpt": "🏆"

};



/* =========================

   CURRENT DATA

========================= */



let lessons = [];

let selectedTopic = null;



/* =========================

   BACK BUTTON

========================= */



if (backButton) {

    backButton.addEventListener("click", function () {

        window.location.href = `${subjectSlug}.html`;

    });

}



/* =========================

   LOAD LESSONS

========================= */



async function loadLessons() {

    try {

        topicsGrid.innerHTML = `

            <div style="grid-column: 1 / -1; text-align: center; padding: 40px;">

                Đang tải bài học...

            </div>

        `;



        const response = await fetch(

            `${API_BASE}/content/subjects/${subjectSlug}/lessons?grade=${grade}`

        );



        if (!response.ok) {

            throw new Error(`API error: ${response.status}`);

        }



        lessons = await response.json();

        renderPage();

    } catch (error) {

        console.error("Không thể tải dữ liệu:", error);

        topicsGrid.innerHTML = `

            <div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: #d00;">

                Không thể kết nối tới máy chủ.<br><br>

                Hãy kiểm tra FastAPI đang chạy.

            </div>

        `;

    }

}



/* =========================

   GROUP TOPICS

========================= */



function groupTopics() {

    const groups = {};

    lessons.forEach(lesson => {

        if (!groups[lesson.topic]) {

            groups[lesson.topic] = [];

        }

        groups[lesson.topic].push(lesson);

    });

    return groups;

}



/* =========================

   RENDER PAGE

========================= */



function renderPage() {

    const subjectLabel = subjectLabels[subjectSlug] || "MÔN HỌC";

    gradeTitle.textContent = `${subjectLabel} LỚP ${grade}`;

    gradeDescription.textContent =

        `Khám phá hệ thống kiến thức, công thức chuyên sâu ${subjectLabel.toLowerCase()} lớp ${grade} và vận dụng giải quyết các bài toán thực tiễn.`;



    const topics = groupTopics();

    const topicKeys = Object.keys(topics);



    topicCount.textContent = topicKeys.length;

    lessonCount.textContent = lessons.length;

    xpCount.textContent = lessons.length * 10;



    const challenges = lessons.filter(

        lesson => lesson.challenge && lesson.challenge.trim() !== ""

    ).length;

    challengeCount.textContent = challenges;



    progressPercent.textContent = "0%";

    progressFill.style.width = "0%";

    progressText.textContent = `0 / ${lessons.length} bài học hoàn thành`;



    topicsGrid.innerHTML = "";

    topicKeys.forEach((topic, idx) => {

        const topicLessons = topics[topic];

        const firstLesson = topicLessons[0];

        createTopicCard(topic, topicLessons, firstLesson, idx + 1);

    });

}



/* =========================

   CREATE TOPIC CARD

========================= */



function createTopicCard(topic, topicLessons, firstLesson, indexNumber) {

    const card = document.createElement("div");

    card.className = "topic-card";



    const icon = firstLesson.icon || topicIcons[topic] || "📚";

    const title = firstLesson.title || topic;

    const description = firstLesson.description || "Khám phá chủ đề này.";



    card.innerHTML = `

        <div class="topic-icon">${icon}</div>

        <div class="topic-info">

            <span class="topic-number">CHỦ ĐỀ ${indexNumber}</span>

            <h3>${title}</h3>

            <p>${description}</p>

            <div class="topic-meta">

                <span>📚 ${topicLessons.length} bài học</span>

                <span>⭐ ${topicLessons.length * 10} XP</span>

            </div>

        </div>

        <div class="topic-arrow">→</div>

    `;



    card.addEventListener("click", function () {

        openTopic(topic, topicLessons, firstLesson);

    });



    topicsGrid.appendChild(card);

}



/* =========================

   OPEN & CLOSE POPUP

========================= */



function openTopic(topic, topicLessons, firstLesson) {

    selectedTopic = topic;

    popupIcon.textContent = firstLesson.icon || topicIcons[topic] || "📚";

    popupLabel.textContent = `CHỦ ĐỀ · LỚP ${grade}`;

    popupTitle.textContent = firstLesson.title || topic;

    popupDescription.textContent =

        firstLesson.description || "Khám phá kiến thức và luyện tập thông qua các bài học.";

    popupLessons.textContent = topicLessons.length;

    popupXP.textContent = topicLessons.length * 10;

    topicPopup.classList.add("active");

}



if (popupClose) {

    popupClose.addEventListener("click", function () {

        topicPopup.classList.remove("active");

    });

}



if (topicPopup) {

    topicPopup.addEventListener("click", function (event) {

        if (event.target === topicPopup) {

            topicPopup.classList.remove("active");

        }

    });

}



if (popupStart) {

    popupStart.addEventListener("click", function () {

        if (!selectedTopic) return;

        const topicLessons = groupTopics()[selectedTopic];

        if (!topicLessons || topicLessons.length === 0) return;

        window.location.href = `lesson.html?id=${topicLessons[0].id}`;

    });

}



if (challengeButton) {

    challengeButton.addEventListener("click", function () {

        const lessonWithChallenge = lessons.find(

            lesson => lesson.challenge && lesson.challenge.trim() !== ""

        );

        if (!lessonWithChallenge) {

            alert("Chưa có thử thách thực tế.");

            return;

        }

        window.location.href = `lesson.html?id=${lessonWithChallenge.id}`;

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

        window.location.href = "progress.html";

    });

}



loadLessons();

