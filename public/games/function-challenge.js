const API_BASE = (["127.0.0.1","localhost"].includes(location.hostname)&&location.port!=="8000"?"http://127.0.0.1:8000/api":"/api");

const GAME_ID = 1;
const USER_ID = Number(localStorage.getItem("user_id")) || 1;

let sessionId = null;
let score = 0;
let questionIndex = 0;

/* 5 Chặng thực tế bám sát Chương IX. Đạo hàm – SGK Toán 11 Kết nối tri thức */
const questions = [
    {
        speaker: "👨‍🔬 Kỹ sư trưởng Minh · Chặng 1/5: Vận tốc tức thời của tàu đệm từ",
        story: "Tàu đệm từ thử nghiệm xuất phát trên đường ray thẳng. Cảm biến ghi lại phương trình quãng đường s(t) theo thời gian t (giây).",
        params: "Phương trình quãng đường: s(t) = 3t² + 4t + 1 (m); thời điểm cần đo: t₀ = 2 giây.",
        formula: "Vận tốc tức thời tại thời điểm t₀ là v(t₀) = s'(t₀). Áp dụng (t²)' = 2t, (t)' = 1 ⇒ s'(t) = 6t + 4. Thay t = 2 vào s'(t).",
        action: "Tính v(2) = s'(2) = 6·2 + 4 rồi bấm chọn giá trị vận tốc đúng (m/s) ở 5 nút bên dưới!",
        funcDisplay: "s(t) = 3t² + 4t + 1 (m)",
        targetDisplay: "Tính vận tốc tức thời v(2) = s'(2) tại t₀ = 2 s:",
        unit: "m/s",
        a: 6, b: 4, y: 16,
        options: [12, 14, 16, 17, 20],
        answer: 16,
        explain: "s'(t) = 6t + 4 ⇒ tại t₀ = 2 s, vận tốc tức thời là v(2) = 6·2 + 4 = 16 m/s."
    },
    {
        speaker: "🌉 Kỹ sư Cầu đường Lan · Chặng 2/5: Độ dốc (Hệ số góc tiếp tuyến) nhịp cầu",
        story: "Đội thiết kế đang kiểm tra độ nghiêng của dầm cầu vòm parabol tại điểm nối trụ để lắp gối đỡ an toàn.",
        params: "Biên dạng vòm cầu: f(x) = x² − 2x + 5; hoành độ điểm đặt gối đỡ: x₀ = 3.",
        formula: "Hệ số góc tiếp tuyến của đồ thị y = f(x) tại x₀ là k = f'(x₀). Ta có f'(x) = (x²)' − (2x)' + (5)' = 2x − 2.",
        action: "Thay x₀ = 3 vào f'(x) = 2x − 2 để tìm hệ số góc tiếp tuyến k = f'(3), rồi bấm chọn đáp án!",
        funcDisplay: "y = f(x) = x² − 2x + 5",
        targetDisplay: "Tìm hệ số góc tiếp tuyến k = f'(3) tại x₀ = 3:",
        unit: "",
        a: 2, b: -2, y: 4,
        options: [2, 3, 4, 6, 8],
        answer: 4,
        explain: "f'(x) = 2x − 2 ⇒ hệ số góc tiếp tuyến tại x₀ = 3 là k = f'(3) = 2·3 − 2 = 4."
    },
    {
        speaker: "⚡ Kỹ sư Điện lực Hùng · Chặng 3/5: Tìm thời điểm đạt tốc độ truyền tải",
        story: "Một tụ điện siêu dung đang nạp điện. Điện lượng q(t) tăng theo hàm bậc hai, cần ngắt mạch đúng lúc cường độ dòng điện tức thời i(t) = q'(t) chạm ngưỡng 14 A.",
        params: "Hàm điện lượng: q(t) = 2t² + 2t (C); ngưỡng dòng điện tức thời cần ngắt: i(t) = q'(t) = 14 A.",
        formula: "Cường độ dòng điện tức thời i(t) = q'(t) = 4t + 2. Giải phương trình 4t + 2 = 14 để tìm thời điểm t (giây).",
        action: "Giải 4t + 2 = 14 tìm thời điểm t (giây) rồi bấm chọn nút đáp án tương ứng!",
        funcDisplay: "q(t) = 2t² + 2t (C)  ⇒  i(t) = q'(t) = 4t + 2",
        targetDisplay: "Tìm thời điểm t (giây) khi dòng điện tức thời i(t) = 14 A:",
        unit: "s",
        a: 4, b: 2, y: 14,
        options: [1, 2, 3, 4, 5],
        answer: 3,
        explain: "i(t) = q'(t) = 4t + 2 = 14 ⇔ 4t = 12 ⇔ t = 3 giây."
    },
    {
        speaker: "🛰️ Kỹ sư Vũ trụ Quân · Chặng 4/5: Vận tốc vật rơi gần bề mặt Sao Hỏa",
        story: "Robot tự hành thả thiết bị thăm dò rơi tự do xuống hố địa chất trên Sao Hỏa. Cần tính vận tốc chạm đất tại giây thứ 5.",
        params: "Phương trình quãng đường rơi trên Sao Hỏa: s(t) = 1,85t² (m); thời điểm chạm đất: t₀ = 5 giây.",
        formula: "Vận tốc tức thời v(t) = s'(t) = 1,85 · (2t) = 3,7t (với g_Sao_Hỏa = 3,7 m/s²). Thay t₀ = 5 s vào v(t).",
        action: "Tính v(5) = 3,7 × 5 rồi bấm chọn vận tốc chạm đất đúng bên dưới!",
        funcDisplay: "s(t) = 1,85t² (m)",
        targetDisplay: "Tính vận tốc tức thời v(5) = s'(5) tại t₀ = 5 s:",
        unit: "m/s",
        a: 3.7, b: 0, y: 18.5,
        options: [9.25, 14.8, 18.5, 22.2, 37],
        answer: 18.5,
        explain: "v(t) = s'(t) = 3,7t ⇒ tại t₀ = 5 s, vận tốc chạm đất là v(5) = 3,7 × 5 = 18,5 m/s."
    },
    {
        speaker: "🏭 Quản đốc Nhà máy Mai · Chặng 5/5: Chi phí biên trong sản xuất (Đạo hàm bậc ba)",
        story: "Dây chuyền sản xuất linh kiện bán dẫn có hàm tổng chi phí C(x) là hàm bậc ba theo sản lượng x (nghìn chiếc). Hãy tính tốc độ tăng chi phí C'(x₀) khi x₀ = 2.",
        params: "Hàm chi phí: C(x) = x³ − 3x² + 8x + 10 (triệu đồng); mức sản lượng đang xét: x₀ = 2.",
        formula: "Quy tắc đạo hàm: (x³)' = 3x², (x²)' = 2x, (x)' = 1 ⇒ C'(x) = 3x² − 6x + 8. Thay x₀ = 2 vào C'(x).",
        action: "Tính C'(2) = 3·(2²) − 6·2 + 8 rồi bấm chọn kết quả đúng để hoàn thành ca trực!",
        funcDisplay: "C(x) = x³ − 3x² + 8x + 10",
        targetDisplay: "Tính tốc độ thay đổi chi phí C'(2) tại x₀ = 2:",
        unit: "triệu/đv",
        a: 3, b: -6, y: 8,
        options: [4, 6, 8, 10, 12],
        answer: 8,
        explain: "C'(x) = 3x² − 6x + 8 ⇒ tại x₀ = 2: C'(2) = 3·4 − 6·2 + 8 = 12 − 12 + 8 = 8 (triệu đồng/đơn vị)."
    }
];

let currentQuestion = null;
let questionStartTime = null;

async function createSession() {
    try {
        const response = await fetch(`${API_BASE}/games/sessions`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: USER_ID, game_id: GAME_ID })
        });
        if (response.ok) {
            const data = await response.json();
            sessionId = data.id;
        }
    } catch (error) {
        console.warn("Chạy chế độ offline:", error);
    }
    loadQuestion();
}

async function recordEvent(action, eventData = {}) {
    if (!sessionId) return;
    try {
        await fetch(`${API_BASE}/games/sessions/${sessionId}/events`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ action: action, event_data: JSON.stringify(eventData) })
        });
    } catch (error) {}
}

function loadQuestion() {
    if (questionIndex >= questions.length) {
        finishGame();
        return;
    }

    currentQuestion = questions[questionIndex];
    questionStartTime = Date.now();

    document.getElementById("dlgSpeaker").textContent = currentQuestion.speaker;
    document.getElementById("dlgStory").textContent = currentQuestion.story;
    document.getElementById("dlgParams").textContent = currentQuestion.params;
    document.getElementById("dlgFormula").textContent = currentQuestion.formula;
    document.getElementById("dlgAction").textContent = currentQuestion.action;

    document.getElementById("functionText").textContent = currentQuestion.funcDisplay;
    document.getElementById("targetBox").innerHTML = currentQuestion.targetDisplay;
    document.getElementById("questionNumber").textContent = questionIndex + 1;
    document.getElementById("message").textContent = "";

    const optionsContainer = document.getElementById("options");
    optionsContainer.innerHTML = "";

    currentQuestion.options.forEach(x => {
        const button = document.createElement("button");
        button.className = "option";
        const disp = String(x).replace(".", ",");
        button.textContent = currentQuestion.unit ? `${disp} ${currentQuestion.unit}` : `${disp}`;
        button.onclick = () => chooseAnswer(x, button);
        optionsContainer.appendChild(button);
    });

    recordEvent("change_parameter", {
        question: questionIndex + 1,
        a: currentQuestion.a,
        b: currentQuestion.b,
        target_y: currentQuestion.y
    });
}

function chooseAnswer(x, button) {
    const elapsed = Date.now() - questionStartTime;
    const expected = currentQuestion.answer;
    const buttons = document.querySelectorAll(".option");
    buttons.forEach(btn => { btn.disabled = true; });

    const msgEl = document.getElementById("message");
    if (x === expected) {
        score += 20;
        document.getElementById("score").textContent = score;
        msgEl.style.color = "#4ade80";
        msgEl.textContent = `✅ Chính xác! ${currentQuestion.explain}`;
        recordEvent("success", {
            question: questionIndex + 1,
            selected_x: x,
            correct_x: expected,
            time_ms: elapsed
        });
    } else {
        msgEl.style.color = "#fb7185";
        msgEl.textContent = `❌ Chưa đúng! Gợi ý: ${currentQuestion.formula}`;
        recordEvent("wrong_answer", {
            question: questionIndex + 1,
            selected_x: x,
            correct_x: expected,
            time_ms: elapsed
        });
        setTimeout(() => {
            buttons.forEach(btn => { btn.disabled = false; });
            recordEvent("retry", { question: questionIndex + 1 });
        }, 700);
        return;
    }

    setTimeout(() => {
        questionIndex++;
        loadQuestion();
    }, 1200);
}

async function finishGame() {
    document.getElementById("gameCard").style.display = "none";
    document.getElementById("finishCard").style.display = "block";
    document.getElementById("finalScore").textContent = score;

    let message = "";
    if (score === 100) {
        message = "Xuất sắc! Bạn đã nắm vững quy tắc tính đạo hàm và ứng dụng vật lý – hình học của đạo hàm (Toán 11).";
    } else if (score >= 60) {
        message = "Khá tốt! Bạn đã hiểu cách áp dụng đạo hàm v(t) = s'(t) và k = f'(x₀) vào thực tế.";
    } else {
        message = "Hãy ôn lại công thức (xⁿ)' = n·xⁿ⁻¹ và ý nghĩa của đạo hàm để đạt điểm tối đa nhé!";
    }
    document.getElementById("finishMessage").textContent = message;

    try { if (window.HDLGGame) HDLGGame.result(score, 100, 20); } catch (e) {}
    if (!sessionId) return;
    try {
        await fetch(`${API_BASE}/games/sessions/${sessionId}/finish?score=${score}`, { method: "POST" });
    } catch (error) {}
}

function goBack() {
    if (history.length > 1) {
        history.back();
    } else {
        window.location.href = "../lesson.html?subject=math&grade=11&topic=l11-ch09-dao-ham";
    }
}

createSession();
