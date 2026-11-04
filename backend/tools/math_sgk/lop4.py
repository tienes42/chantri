"""TOÁN 4 — Kết nối tri thức với cuộc sống (tập một, tập hai).

13 chủ đề đánh số trong SGK, đúng thứ tự mục lục.
Mỗi chủ đề: Yêu cầu cần đạt (CT GDPT 2018), kiến thức theo từng bài, công thức/quy tắc,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf

GRADE = 4

LESSONS = [
    {
        "topic": "l4-cd01-on-tap-va-bo-sung",
        "title": "Ôn tập và bổ sung",
        "icon": "🔁",
        "description": "Chủ đề 1 · SGK Toán 4 tập một (tr. 6–22): Bài 1 – Bài 6. Ôn các số và phép tính trong phạm vi 100 000; số chẵn, số lẻ; biểu thức chứa chữ; giải bài toán có ba bước tính.",
        "requirements": [
            "Củng cố đọc, viết, so sánh, cộng, trừ, nhân, chia các số trong phạm vi 100 000.",
            "Nhận biết được số chẵn, số lẻ.",
            "Làm quen với biểu thức chứa một, hai, ba chữ và tính được giá trị biểu thức khi biết giá trị của chữ.",
            "Giải được bài toán có đến ba bước tính.",
        ],
        "definition": (
            "- **Số chẵn**: có chữ số tận cùng là 0, 2, 4, 6, 8 (chia hết cho 2). **Số lẻ**: tận cùng là 1, 3, 5, 7, 9.\n"
            "- **Biểu thức chứa chữ**: có số, dấu phép tính và chữ, ví dụ a + 5, a × b, a + b + c. Thay chữ bằng số rồi tính được **một giá trị** của biểu thức.\n"
            "- **Bài toán ba bước tính**: tìm lần lượt hai đại lượng trung gian rồi tính kết quả."
        ),
        "theory": (
            "### Bài 1. Ôn tập các số đến 100 000\n"
            "### Bài 2. Ôn tập các phép tính trong phạm vi 100 000\n"
            "### Bài 3. Số chẵn, số lẻ\n"
            "- Hai số chẵn (hoặc lẻ) liên tiếp hơn kém nhau 2 đơn vị.\n"
            "### Bài 4. Biểu thức chứa chữ\n"
            "- Với a = 7: 35 + a × 3 = 35 + 21 = 56. Chu vi hình vuông P = a × 4; hình chữ nhật P = (a + b) × 2.\n"
            "### Bài 5. Giải bài toán có ba bước tính\n"
            "### Bài 6. Luyện tập chung"
        ),
        "formulas": [
            G("I. Số chẵn – lẻ", F("Số chẵn", "Tận cùng 0, 2, 4, 6, 8"), F("Số lẻ", "Tận cùng 1, 3, 5, 7, 9")),
            G("II. Biểu thức chứa chữ", F("Một chữ", "a + 15; 48 : a"), F("Hai chữ", "a + b; a × b"), F("Ba chữ", "a + b + c; (a + b) × c")),
        ],
        "example": "Tính giá trị biểu thức a × b + c với a = 12, b = 5, c = 40.",
        "example_answer": "a × b + c = 12 × 5 + 40 = 60 + 40 = **100**.",
        "real_life": (
            "- Số nhà chẵn ở một bên đường, số lẻ ở bên kia.\n"
            "- Công thức tính tiền: số tiền = giá × số lượng."
        ),
        "quiz": [
            mcq("biet", "Số nào là số chẵn?", ["357", "1209", "4618", "75 391"], 2, "**4618** có tận cùng là 8 → số chẵn."),
            mcq("biet", "Số nào là số lẻ?", ["2470", "3584", "1006", "6723"], 3, "**6723** tận cùng 3 → số lẻ."),
            mcq("biet", "Với a = 9, giá trị của biểu thức 45 : a là:", ["5", "36", "54", "405"], 0, "45 : 9 = **5**."),
            mcq("biet", "Biểu thức nào là biểu thức chứa hai chữ?", ["a + 25", "m × n", "35 × 2", "a + b + c"], 1, "**m × n** chứa hai chữ m và n."),
            mcq("hieu", "Với m = 6, n = 4, giá trị của (m + n) × 2 là:", ["20", "14", "48", "12"], 0, "(6 + 4) × 2 = 10 × 2 = **20**."),
            mcq("hieu", "Số chẵn liền sau số 1998 là:", ["1999", "2000", "2002", "1996"], 1, "Hai số chẵn liên tiếp hơn kém 2: 1998 + 2 = **2000**."),
            tf("hieu", "Nhận định: “Tổng của hai số lẻ là một số chẵn.”", True, "Ví dụ 3 + 5 = 8, 7 + 9 = 16 — luôn là số chẵn → **Đúng**."),
            tf("hieu", "Nhận định: “Với a = 3, biểu thức 20 − a × 4 có giá trị là 68.”", False, "Nhân trước: 20 − 12 = 8; 68 là kết quả khi tính sai thứ tự (20 − 3) × 4 → **Sai**."),
            mcq("vandung", "Mua 3 kg táo giá 45 000 đồng/kg và 2 kg cam giá 30 000 đồng/kg. Đưa 200 000 đồng thì được trả lại:", ["5000 đồng", "25 000 đồng", "15 000 đồng", "65 000 đồng"], 0, "Bước 1 – Tiền táo: 45 000 × 3 = 135 000 (đồng). Bước 2 – Tiền cam: 30 000 × 2 = 60 000 (đồng).\nBước 3 – Trả lại: 200 000 − (135 000 + 60 000) = **5000 đồng**."),
            short("vandung", "Một cửa hàng có 3 thùng dầu, mỗi thùng 125 l. Đã bán 160 l. Số dầu còn lại chia đều vào 5 can. Mỗi can có bao nhiêu lít dầu?", ["43"], "Bước 1: 125 × 3 = 375 (l). Bước 2: 375 − 160 = 215 (l). Bước 3: 215 : 5 = 43 (l).\nĐáp số: **43 l**.", unit="l"),
        ],
    },
    {
        "topic": "l4-cd02-goc-va-don-vi-do-goc",
        "title": "Góc và đơn vị đo góc",
        "icon": "📐",
        "description": "Chủ đề 2 · SGK Toán 4 tập một (tr. 23–32): Bài 7 – Bài 9. Đo góc, đơn vị đo góc (độ); góc nhọn, góc tù, góc bẹt.",
        "requirements": [
            "Nhận biết được đơn vị đo góc: độ (°); sử dụng được thước đo góc để đo các góc 60°, 90°, 120°, 180°.",
            "Nhận biết được góc nhọn, góc vuông, góc tù, góc bẹt.",
            "Giải quyết được vấn đề thực tế đơn giản liên quan đến đo góc.",
        ],
        "definition": (
            "- **Độ** (°) là đơn vị đo góc. Dùng **thước đo góc** (đặt tâm thước trùng đỉnh góc, một cạnh trùng vạch 0°, đọc số đo ở cạnh còn lại).\n"
            "- **Góc vuông** = 90°. **Góc nhọn** bé hơn góc vuông (< 90°). **Góc tù** lớn hơn góc vuông nhưng bé hơn góc bẹt (90° < góc tù < 180°). **Góc bẹt** = 180° (hai cạnh nằm trên một đường thẳng)."
        ),
        "theory": (
            "### Bài 7. Đo góc, đơn vị đo góc\n"
            "- Góc 60° đọc là “sáu mươi độ”.\n"
            "### Bài 8. Góc nhọn, góc tù, góc bẹt\n"
            "- Kim đồng hồ lúc 3 giờ tạo góc vuông; lúc 6 giờ tạo góc bẹt; lúc 2 giờ tạo góc nhọn; lúc 4 giờ tạo góc tù.\n"
            "### Bài 9. Luyện tập chung"
        ),
        "formulas": [
            G("I. Phân loại góc", F("Góc nhọn", "0° < góc < 90°"), F("Góc vuông", "= 90°"), F("Góc tù", "90° < góc < 180°"), F("Góc bẹt", "= 180° = 2 góc vuông")),
            G("II. Đo góc", F("Cách đo", "Tâm thước ≡ đỉnh góc; vạch 0° ≡ một cạnh; đọc số ở cạnh kia")),
        ],
        "example": "Lúc 4 giờ, kim giờ và kim phút tạo thành góc gì? Bao nhiêu độ?",
        "example_answer": "Mỗi khoảng giữa hai số trên mặt đồng hồ ứng với 30°. Lúc 4 giờ hai kim cách 4 khoảng: 4 × 30° = **120°** → **góc tù**.",
        "real_life": "- Độ dốc mái nhà, góc mở của cánh cửa, góc của kéo; góc sút bóng.",
        "quiz": [
            mcq("biet", "Đơn vị đo góc là:", ["mét", "độ", "giây", "ki-lô-gam"], 1, "Góc đo bằng **độ (°)**."),
            mcq("biet", "Góc bẹt có số đo là:", ["90°", "120°", "180°", "360°"], 2, "Góc bẹt = **180°**."),
            mcq("biet", "Góc có số đo 45° là:", ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], 0, "45° < 90° → **góc nhọn**."),
            mcq("biet", "Dụng cụ để đo góc là:", ["Thước đo góc", "Compa", "Cân", "Nhiệt kế"], 0, "Dùng **thước đo góc**."),
            mcq("hieu", "Góc 135° là:", ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], 2, "90° < 135° < 180° → **góc tù**."),
            mcq("hieu", "Lúc 3 giờ đúng, hai kim đồng hồ tạo thành góc:", ["Nhọn", "Vuông", "Tù", "Bẹt"], 1, "Kim phút chỉ 12, kim giờ chỉ 3 → 3 × 30° = 90° → **góc vuông**."),
            tf("hieu", "Nhận định: “Góc bẹt bằng hai lần góc vuông.”", True, "180° = 2 × 90° → **Đúng**."),
            tf("hieu", "Nhận định: “Góc tù luôn lớn hơn 180°.”", False, "Góc tù lớn hơn 90° và **bé hơn** 180° → **Sai**."),
            mcq("vandung", "Lúc 6 giờ đúng, kim giờ và kim phút tạo thành góc bao nhiêu độ?", ["90°", "180°", "60°", "120°"], 1, "Hai kim chỉ 12 và 6, nằm trên một đường thẳng → **180°** (góc bẹt)."),
            short("vandung", "Lúc 2 giờ đúng, góc tạo bởi kim giờ và kim phút bằng bao nhiêu độ?", ["60", "60°"], "Hai kim cách nhau 2 khoảng số, mỗi khoảng 30°: 2 × 30° = **60°** (góc nhọn).", unit="°"),
        ],
    },
    {
        "topic": "l4-cd03-so-co-nhieu-chu-so",
        "title": "Số có nhiều chữ số",
        "icon": "🔢",
        "description": "Chủ đề 3 · SGK Toán 4 tập một (tr. 33–55): Bài 10 – Bài 16. Số có sáu chữ số, số 1 000 000; hàng và lớp; các số trong phạm vi lớp triệu; làm tròn số đến hàng trăm nghìn; so sánh các số có nhiều chữ số; dãy số tự nhiên.",
        "requirements": [
            "Đọc, viết được các số có nhiều chữ số (đến lớp triệu); nhận biết được hàng và lớp; giá trị theo vị trí của từng chữ số.",
            "So sánh, sắp xếp được các số có nhiều chữ số; xác định số lớn nhất, bé nhất trong nhóm 4 số.",
            "Làm tròn được số đến hàng trăm nghìn.",
            "Làm quen với dãy số tự nhiên và đặc điểm của nó.",
        ],
        "definition": (
            "- **Lớp đơn vị** gồm hàng đơn vị, chục, trăm; **lớp nghìn** gồm hàng nghìn, chục nghìn, trăm nghìn; **lớp triệu** gồm hàng triệu, chục triệu, trăm triệu.\n"
            "- Viết số: tách thành từng lớp (3 chữ số) từ phải sang trái: 345 207 816 đọc “ba trăm bốn mươi lăm triệu hai trăm linh bảy nghìn tám trăm mười sáu”.\n"
            "- **Dãy số tự nhiên**: 0, 1, 2, 3, …; không có số tự nhiên lớn nhất; hai số tự nhiên liên tiếp hơn kém nhau 1 đơn vị; số 0 là số tự nhiên bé nhất."
        ),
        "theory": (
            "### Bài 10. Số có sáu chữ số. Số 1 000 000\n"
            "- 10 trăm nghìn = 1 triệu (1 000 000).\n"
            "### Bài 11. Hàng và lớp\n"
            "- Giá trị chữ số phụ thuộc vị trí: trong 352 140, chữ số 5 có giá trị 50 000.\n"
            "### Bài 12. Các số trong phạm vi lớp triệu\n"
            "### Bài 13. Làm tròn số đến hàng trăm nghìn\n"
            "- 3 482 000 → 3 500 000 (xét chữ số hàng chục nghìn 8 ≥ 5).\n"
            "### Bài 14. So sánh các số có nhiều chữ số\n"
            "### Bài 15. Làm quen với dãy số tự nhiên\n"
            "### Bài 16. Luyện tập chung"
        ),
        "formulas": [
            G("I. Hàng và lớp", F("Ba lớp", "Lớp triệu | Lớp nghìn | Lớp đơn vị (mỗi lớp 3 hàng)"), F("Giá trị theo vị trí", "Chữ số × giá trị hàng", "Chữ số 7 ở hàng chục nghìn có giá trị 70 000.")),
            G("II. So sánh – làm tròn", F("So sánh", "Nhiều chữ số hơn thì lớn hơn; cùng số chữ số: so từ trái sang"), F("Làm tròn đến trăm nghìn", "Xét chữ số hàng chục nghìn: < 5 xuống, ≥ 5 lên")),
            G("III. Dãy số tự nhiên", F("Đặc điểm", "0, 1, 2, … · bé nhất là 0 · không có số lớn nhất")),
        ],
        "example": "Đọc số 20 506 070 và nêu giá trị của chữ số 5.",
        "example_answer": "Đọc: hai mươi triệu năm trăm linh sáu nghìn không trăm bảy mươi. Chữ số 5 ở hàng trăm nghìn → giá trị **500 000**.",
        "real_life": "- Dân số Việt Nam khoảng 100 triệu người; khoảng cách Trái Đất – Mặt Trăng khoảng 384 000 km.",
        "quiz": [
            mcq("biet", "Số “một triệu” viết là:", ["100 000", "1 000 000", "10 000 000", "1000"], 1, "1 triệu = **1 000 000** (6 chữ số 0)."),
            mcq("biet", "Lớp nghìn gồm các hàng:", ["Đơn vị, chục, trăm", "Nghìn, chục nghìn, trăm nghìn", "Triệu, chục triệu, trăm triệu", "Trăm, nghìn, triệu"], 1, "Lớp nghìn: **nghìn, chục nghìn, trăm nghìn**."),
            mcq("biet", "Số tự nhiên bé nhất là:", ["1", "0", "10", "Không có"], 1, "Số tự nhiên bé nhất là **0**."),
            mcq("biet", "Trong số 4 382 615, chữ số 3 thuộc hàng:", ["Trăm nghìn", "Chục nghìn", "Triệu", "Nghìn"], 0, "4 | 382 | 615: chữ số 3 đứng đầu lớp nghìn → **hàng trăm nghìn**."),
            mcq("hieu", "Giá trị của chữ số 6 trong số 2 760 345 là:", ["6000", "60 000", "600 000", "6"], 1, "2 | 760 | 345: chữ số 6 ở hàng chục nghìn → **60 000**."),
            mcq("hieu", "Làm tròn số 5 649 000 đến hàng trăm nghìn được:", ["5 600 000", "5 700 000", "6 000 000", "5 650 000"], 0, "Chữ số hàng chục nghìn là 4 < 5 → làm tròn xuống **5 600 000**."),
            tf("hieu", "Nhận định: “999 999 < 1 000 000.”", True, "Số có 6 chữ số bé hơn số có 7 chữ số → **Đúng**."),
            tf("hieu", "Nhận định: “Có số tự nhiên lớn nhất là 999 999 999.”", False, "Thêm 1 vào số nào cũng được số lớn hơn → không có số tự nhiên lớn nhất → **Sai**."),
            mcq("vandung", "Năm 2023, dân số tỉnh A là 1 452 800 người, tỉnh B là 1 425 900 người, tỉnh C là 1 542 000 người, tỉnh D là 1 524 300 người. Tỉnh đông dân nhất là:", ["A", "B", "C", "D"], 2, "Cùng 1 triệu; so hàng trăm nghìn: 5 > 4; trong C và D so chục nghìn: 4 > 2 → **tỉnh C**."),
            short("vandung", "Viết số gồm 3 chục triệu, 4 triệu, 5 chục nghìn và 2 đơn vị.", ["34050002", "34 050 002"], "30 000 000 + 4 000 000 + 50 000 + 2 = **34 050 002**.", note="Các hàng vắng phải viết chữ số 0."),
        ],
    },
    {
        "topic": "l4-cd04-don-vi-do-dai-luong",
        "title": "Một số đơn vị đo đại lượng",
        "icon": "⚖️",
        "description": "Chủ đề 4 · SGK Toán 4 tập một (tr. 56–75): Bài 17 – Bài 21. Yến, tạ, tấn; đề-xi-mét vuông, mét vuông, mi-li-mét vuông; giây, thế kỉ; thực hành sử dụng một số đơn vị đo đại lượng.",
        "requirements": [
            "Nhận biết được các đơn vị đo khối lượng yến, tạ, tấn và quan hệ với kg.",
            "Nhận biết được các đơn vị đo diện tích dm², m², mm² và quan hệ giữa chúng.",
            "Nhận biết được đơn vị đo thời gian giây, thế kỉ và quan hệ với phút, năm.",
            "Thực hiện được chuyển đổi, tính toán với các số đo đã học; ước lượng trong trường hợp đơn giản.",
        ],
        "definition": (
            "- **Khối lượng**: 1 yến = 10 kg; 1 tạ = 10 yến = 100 kg; 1 tấn = 10 tạ = 1000 kg.\n"
            "- **Diện tích**: 1 dm² = 100 cm²; 1 m² = 100 dm² = 10 000 cm²; 1 cm² = 100 mm².\n"
            "- **Thời gian**: 1 phút = 60 giây; 1 thế kỉ = 100 năm. Từ năm 1 đến năm 100 là thế kỉ I; …; năm 2001 đến 2100 là thế kỉ XXI."
        ),
        "theory": (
            "### Bài 17. Yến, tạ, tấn\n"
            "- Con lợn nặng khoảng 1 tạ; xe tải chở 5 tấn hàng.\n"
            "### Bài 18. Đề-xi-mét vuông, mét vuông, mi-li-mét vuông\n"
            "- Hai đơn vị diện tích liền kề hơn kém nhau **100 lần**.\n"
            "### Bài 19. Giây, thế kỉ\n"
            "- Năm 1945 thuộc thế kỉ XX.\n"
            "### Bài 20. Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng\n"
            "### Bài 21. Luyện tập chung"
        ),
        "formulas": [
            G("I. Khối lượng", F("Bảng đơn vị", "tấn – tạ – yến – kg – hg – dag – g (liền kề gấp 10 lần)"), F("Quan hệ với kg", "1 yến = 10 kg · 1 tạ = 100 kg · 1 tấn = 1000 kg")),
            G("II. Diện tích", F("Quan hệ", "1 m² = 100 dm² · 1 dm² = 100 cm² · 1 cm² = 100 mm²")),
            G("III. Thời gian", F("Quan hệ", "1 phút = 60 giây · 1 giờ = 3600 giây · 1 thế kỉ = 100 năm"), F("Xác định thế kỉ", "Năm abcd (không tròn trăm): thế kỉ = ab + 1", "Năm 1789 → thế kỉ 17 + 1 = XVIII.")),
        ],
        "example": "Đổi: 3 tấn 5 tạ = … kg; 2 m² 8 dm² = … dm².",
        "example_answer": (
            "3 tấn 5 tạ = 3000 kg + 500 kg = **3500 kg**.\n"
            "2 m² 8 dm² = 200 dm² + 8 dm² = **208 dm²**."
        ),
        "real_life": "- Diện tích căn phòng (20 m²), khối lượng xe tải; bấm giờ chạy 100 m (giây); lịch sử theo thế kỉ.",
        "quiz": [
            mcq("biet", "1 tấn = … kg?", ["10", "100", "1000", "10 000"], 2, "1 tấn = **1000 kg**."),
            mcq("biet", "1 m² = … dm²?", ["10", "100", "1000", "10 000"], 1, "1 m² = **100 dm²**.", note="Đơn vị diện tích liền kề gấp 100 lần (không phải 10)."),
            mcq("biet", "1 thế kỉ = … năm?", ["10", "100", "1000", "60"], 1, "1 thế kỉ = **100 năm**."),
            mcq("biet", "1 phút = … giây?", ["60", "100", "30", "3600"], 0, "1 phút = **60 giây**."),
            mcq("hieu", "Năm 2024 thuộc thế kỉ:", ["XX", "XXI", "XIX", "XXII"], 1, "Từ 2001 đến 2100 là thế kỉ **XXI**."),
            mcq("hieu", "5 tạ 7 yến = … kg?", ["57", "570", "507", "5070"], 1, "5 tạ = 500 kg; 7 yến = 70 kg → **570 kg**."),
            tf("hieu", "Nhận định: “1 dm² = 100 cm².”", True, "Hình vuông cạnh 1 dm = 10 cm có diện tích 10 × 10 = 100 cm² → **Đúng**."),
            tf("hieu", "Nhận định: “3 phút 20 giây = 320 giây.”", False, "3 phút = 180 giây; 180 + 20 = 200 giây → **Sai**."),
            mcq("vandung", "Một xe tải chở được 4 tấn hàng. Đã chở 25 bao gạo, mỗi bao 1 tạ. Xe còn chở thêm được bao nhiêu ki-lô-gam?", ["1500 kg", "2500 kg", "3975 kg", "1000 kg"], 0, "25 bao × 100 kg = 2500 kg. Đổi 4 tấn = 4000 kg. Còn chở thêm: 4000 − 2500 = **1500 kg**."),
            short("vandung", "Một căn phòng hình chữ nhật dài 6 m, rộng 4 m. Người ta lát nền bằng gạch vuông cạnh 4 dm. Cần bao nhiêu viên gạch?", ["150"], "Diện tích phòng: 6 × 4 = 24 m² = 2400 dm². Diện tích 1 viên: 4 × 4 = 16 dm². Số viên: 2400 : 16 = 150.\nĐáp số: **150 viên**.", unit="viên", alt="Chiều dài xếp 60 : 4 = 15 viên, chiều rộng 40 : 4 = 10 viên → 15 × 10 = 150."),
        ],
    },
    {
        "topic": "l4-cd05-phep-cong-va-phep-tru",
        "title": "Phép cộng và phép trừ",
        "icon": "➕",
        "description": "Chủ đề 5 · SGK Toán 4 tập một (tr. 76–90): Bài 22 – Bài 26. Phép cộng, phép trừ các số có nhiều chữ số; tính chất giao hoán và kết hợp của phép cộng; tìm hai số biết tổng và hiệu của hai số đó.",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ các số tự nhiên có nhiều chữ số (không nhớ và có nhớ không quá ba lượt, không liên tiếp).",
            "Vận dụng được tính chất giao hoán, kết hợp của phép cộng để tính nhẩm, tính hợp lí.",
            "Giải được bài toán tìm hai số khi biết tổng và hiệu của hai số đó.",
        ],
        "definition": (
            "- **Giao hoán**: a + b = b + a. **Kết hợp**: (a + b) + c = a + (b + c).\n"
            "- **Tổng – hiệu**: Biết tổng S và hiệu H của hai số:\n"
            "  - Số lớn = (S + H) : 2; Số bé = (S − H) : 2."
        ),
        "theory": (
            "### Bài 22. Phép cộng các số có nhiều chữ số\n"
            "- 367 528 + 241 736 = 609 264.\n"
            "### Bài 23. Phép trừ các số có nhiều chữ số\n"
            "- 865 279 − 450 237 = 415 042.\n"
            "### Bài 24. Tính chất giao hoán và kết hợp của phép cộng\n"
            "- 25 + 89 + 75 = (25 + 75) + 89 = 189.\n"
            "### Bài 25. Tìm hai số biết tổng và hiệu của hai số đó\n"
            "- Tổng 70, hiệu 10: số lớn (70 + 10) : 2 = 40; số bé 70 − 40 = 30.\n"
            "### Bài 26. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tính chất phép cộng", F("Giao hoán", "a + b = b + a"), F("Kết hợp", "(a + b) + c = a + (b + c)"), F("Cộng với 0", "a + 0 = a")),
            G("II. Tổng – hiệu", F("Số lớn", "(Tổng + Hiệu) : 2"), F("Số bé", "(Tổng − Hiệu) : 2 = Tổng − Số lớn")),
        ],
        "example": "Hai lớp trồng được 150 cây, lớp 4A trồng nhiều hơn lớp 4B 12 cây. Mỗi lớp trồng bao nhiêu cây?",
        "example_answer": "Lớp 4A (số lớn): (150 + 12) : 2 = **81** cây. Lớp 4B: 150 − 81 = **69** cây.",
        "real_life": "- Chia tiền tiết kiệm của hai anh em khi biết tổng và chênh lệch; cộng sản lượng nhiều tháng.",
        "quiz": [
            mcq("biet", "Tính chất (a + b) + c = a + (b + c) gọi là:", ["Giao hoán", "Kết hợp", "Phân phối", "Nhân với 1"], 1, "Đó là tính chất **kết hợp** của phép cộng."),
            mcq("biet", "Muốn tìm số lớn khi biết tổng và hiệu, ta lấy:", ["(Tổng − Hiệu) : 2", "(Tổng + Hiệu) : 2", "Tổng × Hiệu", "Tổng : Hiệu"], 1, "Số lớn = **(Tổng + Hiệu) : 2**."),
            mcq("biet", "425 316 + 172 483 = ?", ["597 799", "597 899", "587 799", "252 833"], 0, "Cộng từng hàng không nhớ → **597 799**."),
            mcq("biet", "Số bé = ?", ["(Tổng + Hiệu) : 2", "(Tổng − Hiệu) : 2", "Tổng − Hiệu", "Hiệu : 2"], 1, "Số bé = **(Tổng − Hiệu) : 2**."),
            mcq("hieu", "Tính nhanh: 168 + 279 + 32 = ?", ["479", "469", "489", "579"], 0, "(168 + 32) + 279 = 200 + 279 = **479**."),
            mcq("hieu", "720 405 − 318 627 = ?", ["401 778", "402 778", "401 878", "1 039 032"], 0, "Thử lại: 401 778 + 318 627 = 720 405 → **401 778**."),
            tf("hieu", "Nhận định: “Tổng hai số là 90, hiệu là 20 thì số bé là 35.”", True, "(90 − 20) : 2 = 35 → **Đúng**."),
            tf("hieu", "Nhận định: “Tổng hai số là 100, hiệu là 30 thì số lớn là 70.”", False, "(100 + 30) : 2 = 65, không phải 70 → **Sai**.", note="Hay nhầm: lấy tổng trừ hiệu rồi không chia 2."),
            mcq("vandung", "Hai thùng có 250 l dầu. Thùng thứ nhất ít hơn thùng thứ hai 30 l. Thùng thứ nhất có:", ["110 l", "140 l", "220 l", "125 l"], 0, "Thùng thứ nhất là số bé: (250 − 30) : 2 = **110 l**."),
            short("vandung", "Tuổi bố và tuổi con cộng lại là 58 tuổi. Bố hơn con 28 tuổi. Hỏi con bao nhiêu tuổi?", ["15"], "Tuổi con (số bé) = (58 − 28) : 2 = 15 (tuổi).\nĐáp số: **15 tuổi**.", unit="tuổi", alt="Tuổi bố: (58 + 28) : 2 = 43; tuổi con: 58 − 43 = 15."),
        ],
    },
    {
        "topic": "l4-cd06-vuong-goc-song-song",
        "title": "Đường thẳng vuông góc. Đường thẳng song song",
        "icon": "📏",
        "description": "Chủ đề 6 · SGK Toán 4 tập một (tr. 91–113): Bài 27 – Bài 32. Hai đường thẳng vuông góc; hai đường thẳng song song; thực hành vẽ; hình bình hành, hình thoi.",
        "requirements": [
            "Nhận biết được hai đường thẳng vuông góc, hai đường thẳng song song.",
            "Vẽ được đường thẳng đi qua một điểm và vuông góc (song song) với một đường thẳng cho trước bằng thước thẳng và ê-ke.",
            "Nhận biết được hình bình hành, hình thoi và đặc điểm về cạnh của chúng.",
            "Giải quyết được vấn đề liên quan đến đo, vẽ, lắp ghép, tạo hình gắn với các hình đã học.",
        ],
        "definition": (
            "- **Hai đường thẳng vuông góc**: cắt nhau tạo thành 4 góc vuông. Kí hiệu AB ⊥ CD.\n"
            "- **Hai đường thẳng song song**: không bao giờ cắt nhau (cùng vuông góc với một đường thẳng thứ ba). Kí hiệu AB ∥ CD.\n"
            "- **Hình bình hành**: có hai cặp cạnh đối diện **song song và bằng nhau**.\n"
            "- **Hình thoi**: có hai cặp cạnh đối diện song song và **bốn cạnh bằng nhau**."
        ),
        "theory": (
            "### Bài 27. Hai đường thẳng vuông góc\n"
            "- Hai cạnh kề của hình chữ nhật vuông góc với nhau.\n"
            "### Bài 28. Thực hành và trải nghiệm vẽ hai đường thẳng vuông góc\n"
            "- Đặt một cạnh góc vuông ê-ke trùng đường thẳng, cạnh kia đi qua điểm cho trước.\n"
            "### Bài 29. Hai đường thẳng song song\n"
            "- Hai cạnh đối diện của hình chữ nhật song song với nhau.\n"
            "### Bài 30. Thực hành và trải nghiệm vẽ hai đường thẳng song song\n"
            "- Vẽ đường vuông góc hai lần: d ⊥ a, b ⊥ d ⇒ b ∥ a.\n"
            "### Bài 31. Hình bình hành, hình thoi\n"
            "### Bài 32. Luyện tập chung"
        ),
        "formulas": [
            G("I. Quan hệ hai đường thẳng", F("Vuông góc", "a ⊥ b: tạo 4 góc vuông"), F("Song song", "a ∥ b: không cắt nhau"), F("Tính chất", "a ⊥ c và b ⊥ c ⇒ a ∥ b")),
            G("II. Tứ giác đặc biệt", F("Hình bình hành", "AB ∥ CD, AD ∥ BC; AB = CD, AD = BC"), F("Hình thoi", "Hai cặp cạnh song song; 4 cạnh bằng nhau"), F("Chu vi hình thoi", "P = a × 4")),
        ],
        "example": "Hình chữ nhật ABCD có những cặp cạnh nào song song, cặp cạnh nào vuông góc?",
        "example_answer": "Song song: **AB ∥ DC**, **AD ∥ BC**. Vuông góc: **AB ⊥ AD, AB ⊥ BC, CD ⊥ AD, CD ⊥ BC**.",
        "real_life": (
            "- Đường ray tàu hỏa song song; mép tường và sàn nhà vuông góc.\n"
            "- Hoa văn hình thoi trên gạch lát, diều; mắt lưới B40 hình thoi."
        ),
        "quiz": [
            mcq("biet", "Hai đường thẳng vuông góc tạo thành mấy góc vuông?", ["1", "2", "3", "4"], 3, "Hai đường thẳng vuông góc tạo thành **4** góc vuông."),
            mcq("biet", "Hai đường thẳng không bao giờ cắt nhau gọi là:", ["Vuông góc", "Song song", "Cắt nhau", "Trùng nhau"], 1, "Đó là hai đường thẳng **song song**."),
            mcq("biet", "Hình có bốn cạnh bằng nhau và hai cặp cạnh đối diện song song là:", ["Hình chữ nhật", "Hình thoi", "Hình thang", "Hình tam giác"], 1, "Đó là **hình thoi** (hình vuông cũng là trường hợp đặc biệt)."),
            mcq("biet", "Dụng cụ dùng để vẽ hai đường thẳng vuông góc là:", ["Compa", "Ê-ke", "Thước đo góc", "Cân"], 1, "Dùng **ê-ke** và thước thẳng."),
            mcq("hieu", "Hình bình hành ABCD có AB = 8 cm, BC = 5 cm. Độ dài CD là:", ["5 cm", "8 cm", "13 cm", "3 cm"], 1, "Cạnh đối diện bằng nhau: CD = AB = **8 cm**."),
            mcq("hieu", "Hình thoi cạnh 7 cm có chu vi là:", ["14 cm", "28 cm", "49 cm", "21 cm"], 1, "P = 7 × 4 = **28 cm**."),
            tf("hieu", "Nhận định: “Hai cạnh đối diện của hình chữ nhật song song với nhau.”", True, "Đúng tính chất hình chữ nhật → **Đúng**."),
            tf("hieu", "Nhận định: “Hình bình hành nào cũng có 4 cạnh bằng nhau.”", False, "Hình bình hành chỉ có các cạnh **đối diện** bằng nhau; 4 cạnh bằng nhau là hình thoi → **Sai**."),
            mcq("vandung", "Hình bình hành có chu vi 36 cm, một cạnh dài 11 cm. Cạnh kề với nó dài:", ["7 cm", "14 cm", "25 cm", "9 cm"], 0, "Nửa chu vi = 36 : 2 = 18 cm = tổng hai cạnh kề. Cạnh kề = 18 − 11 = **7 cm**."),
            short("vandung", "Bác An làm khung diều hình thoi, mỗi cạnh dài 35 cm. Bác cần bao nhiêu xăng-ti-mét nan tre để làm bốn cạnh?", ["140"], "Chu vi hình thoi: 35 × 4 = 140 (cm).\nĐáp số: **140 cm**.", unit="cm"),
        ],
    },
    {
        "topic": "l4-cd07-on-tap-hoc-ki-1",
        "title": "Ôn tập học kì 1",
        "icon": "📝",
        "description": "Chủ đề 7 · SGK Toán 4 tập một (tr. 114–130): Bài 33 – Bài 37. Ôn tập các số đến lớp triệu; phép cộng, phép trừ; hình học; đo lường.",
        "requirements": [
            "Củng cố đọc, viết, so sánh, làm tròn số đến lớp triệu; số chẵn, số lẻ; dãy số tự nhiên.",
            "Thực hiện thành thạo cộng, trừ số có nhiều chữ số; vận dụng tính chất để tính hợp lí; bài toán tổng – hiệu; biểu thức chứa chữ.",
            "Củng cố góc nhọn, vuông, tù, bẹt; vuông góc, song song; hình bình hành, hình thoi.",
            "Chuyển đổi được các đơn vị yến, tạ, tấn; dm², m², mm²; giây, thế kỉ.",
        ],
        "definition": (
            "- Số: hàng – lớp; làm tròn theo chữ số ngay bên phải hàng cần làm tròn.\n"
            "- Tổng – hiệu: Số lớn = (S + H) : 2; Số bé = (S − H) : 2.\n"
            "- Góc: nhọn < 90° = vuông < tù < 180° = bẹt."
        ),
        "theory": (
            "### Bài 33. Ôn tập các số đến lớp triệu\n"
            "### Bài 34. Ôn tập phép cộng, phép trừ\n"
            "### Bài 35. Ôn tập hình học\n"
            "### Bài 36. Ôn tập đo lường\n"
            "### Bài 37. Ôn tập chung"
        ),
        "formulas": [
            G("I. Số và phép tính", F("Tổng – hiệu", "Lớn = (S + H) : 2 · Bé = (S − H) : 2"), F("Tính chất cộng", "a + b = b + a · (a + b) + c = a + (b + c)")),
            G("II. Đo lường", F("Khối lượng", "1 tấn = 10 tạ = 100 yến = 1000 kg"), F("Diện tích", "1 m² = 100 dm² = 10 000 cm²"), F("Thời gian", "1 thế kỉ = 100 năm · 1 phút = 60 giây")),
        ],
        "example": "Tính bằng cách thuận tiện: 2 475 + 3 618 + 525 + 382.",
        "example_answer": "(2475 + 525) + (3618 + 382) = 3000 + 4000 = **7000**.",
        "real_life": "- Tổng kết: so sánh dân số các tỉnh, tính diện tích sân trường, đọc thế kỉ của sự kiện lịch sử.",
        "quiz": [
            mcq("biet", "Số 7 030 405 đọc là:", ["Bảy triệu ba mươi nghìn bốn trăm linh năm", "Bảy triệu ba trăm nghìn bốn trăm linh năm", "Bảy mươi triệu ba nghìn bốn trăm linh năm", "Bảy triệu ba mươi nghìn bốn mươi lăm"], 0, "7 | 030 | 405 → **bảy triệu ba mươi nghìn bốn trăm linh năm**."),
            mcq("biet", "Góc 90° là:", ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], 1, "**Góc vuông** = 90°."),
            mcq("biet", "2 tạ = … kg?", ["20", "200", "2000", "2"], 1, "1 tạ = 100 kg → **200 kg**."),
            mcq("biet", "Hình thoi có:", ["4 góc vuông", "4 cạnh bằng nhau", "Chỉ 1 cặp cạnh song song", "3 cạnh"], 1, "Hình thoi có **4 cạnh bằng nhau**."),
            mcq("hieu", "Làm tròn 2 750 000 đến hàng triệu được:", ["2 000 000", "3 000 000", "2 800 000", "2 700 000"], 1, "Chữ số hàng trăm nghìn là 7 ≥ 5 → **3 000 000**."),
            mcq("hieu", "Năm 1010 (dời đô về Thăng Long) thuộc thế kỉ:", ["X", "XI", "IX", "XII"], 1, "Từ 1001 đến 1100 là thế kỉ **XI**."),
            tf("hieu", "Nhận định: “500 dm² = 5 m².”", True, "1 m² = 100 dm² ⇒ 500 dm² = 5 m² → **Đúng**."),
            tf("hieu", "Nhận định: “Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì vuông góc với nhau.”", False, "Chúng **song song** với nhau → **Sai**."),
            mcq("vandung", "Hai kho có 6500 tấn thóc. Kho A nhiều hơn kho B 900 tấn. Kho A có:", ["3700 tấn", "2800 tấn", "3250 tấn", "7400 tấn"], 0, "(6500 + 900) : 2 = **3700 tấn**."),
            short("vandung", "Một thửa ruộng hình chữ nhật có nửa chu vi 150 m, chiều dài hơn chiều rộng 30 m. Tính diện tích thửa ruộng (m²).", ["5400"], "Chiều dài: (150 + 30) : 2 = 90 (m); chiều rộng: 150 − 90 = 60 (m). Diện tích: 90 × 60 = 5400 (m²).\nĐáp số: **5400 m²**.", unit="m²"),
        ],
    },
    {
        "topic": "l4-cd08-phep-nhan-va-phep-chia",
        "title": "Phép nhân và phép chia",
        "icon": "✖️",
        "description": "Chủ đề 8 · SGK Toán 4 tập hai (tr. 4–35): Bài 38 – Bài 48. Nhân, chia với số có một chữ số, hai chữ số; tính chất giao hoán, kết hợp, phân phối; nhân chia với 10, 100, 1000; ước lượng; số trung bình cộng; bài toán rút về đơn vị.",
        "requirements": [
            "Thực hiện được phép nhân với số có một, hai chữ số; phép chia cho số có một, hai chữ số.",
            "Vận dụng được tính chất giao hoán, kết hợp của phép nhân và tính chất phân phối của phép nhân đối với phép cộng để tính hợp lí.",
            "Thực hiện được nhân, chia nhẩm với 10, 100, 1000…; ước lượng được kết quả tính trong trường hợp đơn giản.",
            "Tìm được số trung bình cộng; giải được bài toán liên quan đến rút về đơn vị.",
        ],
        "definition": (
            "- **Phân phối**: a × (b + c) = a × b + a × c.\n"
            "- **Nhân với 10, 100, 1000**: viết thêm 1, 2, 3 chữ số 0 vào bên phải. **Chia** số tròn chục, tròn trăm… cho 10, 100, 1000: bỏ bớt 1, 2, 3 chữ số 0.\n"
            "- **Số trung bình cộng** của nhiều số = Tổng các số : Số các số hạng.\n"
            "- **Rút về đơn vị**: tìm giá trị một phần (phép chia) rồi tìm giá trị nhiều phần (phép nhân)."
        ),
        "theory": (
            "### Bài 38. Nhân với số có một chữ số\n"
            "- 24 135 × 4 = 96 540.\n"
            "### Bài 39. Chia cho số có một chữ số\n"
            "- 128 472 : 6 = 21 412.\n"
            "### Bài 40. Tính chất giao hoán và kết hợp của phép nhân\n"
            "- 25 × 7 × 4 = (25 × 4) × 7 = 700.\n"
            "### Bài 41. Nhân, chia với 10, 100, 1 000, …\n"
            "- 35 × 100 = 3500; 7000 : 1000 = 7.\n"
            "### Bài 42. Tính chất phân phối của phép nhân đối với phép cộng\n"
            "- 36 × 7 + 36 × 3 = 36 × (7 + 3) = 360.\n"
            "### Bài 43. Nhân với số có hai chữ số\n"
            "- 36 × 23: 36 × 3 = 108 (tích riêng thứ nhất); 36 × 2 = 72 (tích riêng thứ hai, viết lùi sang trái một cột) → 828.\n"
            "### Bài 44. Chia cho số có hai chữ số\n"
            "- 672 : 21 = 32; ước lượng thương: 67 : 21 ≈ 6 : 2 = 3.\n"
            "### Bài 45. Thực hành và trải nghiệm ước lượng trong tính toán\n"
            "### Bài 46. Tìm số trung bình cộng\n"
            "- Trung bình cộng của 36, 42, 57 là (36 + 42 + 57) : 3 = 45.\n"
            "### Bài 47. Bài toán liên quan đến rút về đơn vị\n"
            "- 5 hộp có 40 bút → 1 hộp 8 bút → 7 hộp 56 bút.\n"
            "### Bài 48. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tính chất phép nhân", F("Giao hoán", "a × b = b × a"), F("Kết hợp", "(a × b) × c = a × (b × c)"), F("Phân phối", "a × (b + c) = a × b + a × c"), F("Nhân với 1, với 0", "a × 1 = a · a × 0 = 0")),
            G("II. Nhân – chia nhẩm", F("× 10, 100, 1000", "Thêm 1, 2, 3 chữ số 0"), F(": 10, 100, 1000", "Bớt 1, 2, 3 chữ số 0 (số tròn chục, trăm, nghìn)")),
            G("III. Giải toán", F("Trung bình cộng", "TBC = Tổng : Số số hạng"), F("Rút về đơn vị", "Một phần = Tổng : số phần → Nhiều phần = Một phần × số phần")),
        ],
        "example": "Một ô tô 3 giờ đầu đi được 135 km, 2 giờ sau đi được 95 km. Hỏi trung bình mỗi giờ ô tô đi được bao nhiêu ki-lô-mét?",
        "example_answer": "Tổng quãng đường: 135 + 95 = 230 (km). Tổng thời gian: 3 + 2 = 5 (giờ). Trung bình: 230 : 5 = **46 km** mỗi giờ.",
        "real_life": (
            "- Tính điểm trung bình môn; tính giá tiền 1 sản phẩm rồi suy ra nhiều sản phẩm.\n"
            "- Ước lượng nhanh khi đi siêu thị."
        ),
        "quiz": [
            mcq("biet", "456 × 100 = ?", ["4560", "45 600", "456 000", "4 560 000"], 1, "Nhân với 100: thêm 2 chữ số 0 → **45 600**."),
            mcq("biet", "Tính chất a × (b + c) = a × b + a × c gọi là:", ["Giao hoán", "Kết hợp", "Phân phối", "Nhân với 1"], 2, "Đó là tính chất **phân phối** của phép nhân đối với phép cộng."),
            mcq("biet", "Số trung bình cộng của 12, 18 và 21 là:", ["17", "51", "16", "18"], 0, "(12 + 18 + 21) : 3 = 51 : 3 = **17**."),
            mcq("biet", "9000 : 100 = ?", ["9", "90", "900", "9000"], 1, "Bớt 2 chữ số 0 → **90**."),
            mcq("hieu", "47 × 25 = ?", ["1175", "1075", "329", "1185"], 0, "47 × 5 = 235; 47 × 2 = 94 (lùi một cột) → 235 + 940 = **1175**.", note="Lỗi hay gặp: không viết lùi tích riêng thứ hai."),
            mcq("hieu", "Tính nhanh: 125 × 8 × 7 = ?", ["7000", "1000", "8750", "875"], 0, "(125 × 8) × 7 = 1000 × 7 = **7000**."),
            tf("hieu", "Nhận định: “864 : 24 = 36.”", True, "24 × 36 = 864 → **Đúng**."),
            tf("hieu", "Nhận định: “23 × 99 + 23 = 2300.”", True, "23 × 99 + 23 × 1 = 23 × (99 + 1) = 23 × 100 = 2300 → **Đúng**."),
            mcq("vandung", "Mua 6 quyển vở hết 42 000 đồng. Hỏi mua 9 quyển vở như thế hết bao nhiêu tiền?", ["63 000 đồng", "54 000 đồng", "72 000 đồng", "378 000 đồng"], 0, "Rút về đơn vị: 1 quyển giá 42 000 : 6 = 7000 (đồng). 9 quyển: 7000 × 9 = **63 000 đồng**."),
            short("vandung", "Một trường có 4 lớp, các lớp lần lượt có 32, 35, 30 và 31 học sinh. Hỏi trung bình mỗi lớp có bao nhiêu học sinh?", ["32"], "Tổng: 32 + 35 + 30 + 31 = 128. Trung bình: 128 : 4 = 32 (học sinh).\nĐáp số: **32 học sinh**.", unit="học sinh"),
        ],
    },
    {
        "topic": "l4-cd09-thong-ke-xac-suat",
        "title": "Làm quen với yếu tố thống kê, xác suất",
        "icon": "📊",
        "description": "Chủ đề 9 · SGK Toán 4 tập hai (tr. 36–48): Bài 49 – Bài 52. Dãy số liệu thống kê; biểu đồ cột; số lần xuất hiện của một sự kiện.",
        "requirements": [
            "Nhận biết được về dãy số liệu thống kê; sắp xếp số liệu vào dãy theo các tiêu chí cho trước.",
            "Đọc, mô tả được số liệu ở dạng biểu đồ cột; nêu nhận xét đơn giản; tính toán từ số liệu.",
            "Kiểm đếm được số lần lặp lại của một khả năng xảy ra (nhiều lần) của một sự kiện khi thực hiện thí nghiệm, trò chơi đơn giản.",
        ],
        "definition": (
            "- **Dãy số liệu**: các số liệu được ghi lại theo thứ tự (ví dụ chiều cao của 5 bạn: 132, 128, 140, 135, 130 cm). Số liệu thứ nhất, thứ hai… ; có thể tìm lớn nhất, bé nhất, tổng, trung bình.\n"
            "- **Biểu đồ cột**: mỗi cột biểu diễn số liệu của một đối tượng; cột càng cao số liệu càng lớn.\n"
            "- **Số lần xuất hiện** của một sự kiện: đếm số lần sự kiện đó xảy ra sau nhiều lần thử (ví dụ tung đồng xu 20 lần, mặt ngửa xuất hiện 11 lần)."
        ),
        "theory": (
            "### Bài 49. Dãy số liệu thống kê\n"
            "### Bài 50. Biểu đồ cột\n"
            "- Đọc tên các cột (trục ngang), giá trị (trục đứng); so sánh, tính tổng, hiệu.\n"
            "### Bài 51. Số lần xuất hiện của một sự kiện\n"
            "### Bài 52. Luyện tập chung"
        ),
        "formulas": [
            G("I. Dãy số liệu", F("Các thao tác", "Đọc số liệu thứ n · Lớn nhất/bé nhất · Tổng · Trung bình = Tổng : số số liệu")),
            G("II. Biểu đồ cột", F("Đọc", "Chiều cao cột ↔ giá trị trên trục đứng")),
            G("III. Số lần xuất hiện", F("Kiểm đếm", "Tổng số lần thử = tổng số lần xuất hiện của các khả năng")),
        ],
        "example": "Dãy số liệu số cây trồng của 4 tổ: 15, 18, 12, 19. Tổ nào trồng nhiều nhất? Trung bình mỗi tổ trồng bao nhiêu cây?",
        "example_answer": "Tổ 4 trồng nhiều nhất (19 cây). Trung bình: (15 + 18 + 12 + 19) : 4 = 64 : 4 = **16 cây**.",
        "real_life": "- Biểu đồ cột lượng mưa các tháng; thống kê số sách thư viện cho mượn; trò chơi tung đồng xu, gieo xúc xắc.",
        "quiz": [
            mcq("biet", "Dãy số liệu chiều cao (cm): 135, 128, 142, 130. Số liệu thứ ba là:", ["135", "128", "142", "130"], 2, "Số liệu thứ ba là **142**."),
            mcq("biet", "Trong biểu đồ cột, cột cao nhất biểu diễn:", ["Số liệu bé nhất", "Số liệu lớn nhất", "Tổng số liệu", "Không có ý nghĩa"], 1, "Cột cao nhất ứng với **số liệu lớn nhất**."),
            mcq("biet", "Dãy số liệu trên (135, 128, 142, 130) có mấy số liệu?", ["3", "4", "5", "135"], 1, "Có **4** số liệu."),
            mcq("biet", "Tung đồng xu 10 lần, mặt sấp xuất hiện 4 lần. Mặt ngửa xuất hiện:", ["4 lần", "6 lần", "10 lần", "14 lần"], 1, "10 − 4 = **6** lần."),
            mcq("hieu", "Biểu đồ cột số học sinh đạt giải: 4A: 8, 4B: 12, 4C: 10, 4D: 6. Tổng số học sinh đạt giải là:", ["36", "32", "34", "40"], 0, "8 + 12 + 10 + 6 = **36**."),
            mcq("hieu", "Theo biểu đồ trên, lớp 4B có nhiều hơn lớp 4D bao nhiêu học sinh đạt giải?", ["4", "6", "2", "18"], 1, "12 − 6 = **6**."),
            tf("hieu", "Nhận định: “Theo biểu đồ trên (8, 12, 10, 6), trung bình mỗi lớp có 9 học sinh đạt giải.”", True, "36 : 4 = 9 → **Đúng**."),
            tf("hieu", "Nhận định: “Gieo xúc xắc 12 lần thì mặt 6 chấm chắc chắn xuất hiện đúng 2 lần.”", False, "Số lần xuất hiện là ngẫu nhiên, không chắc chắn bằng 2 → **Sai**."),
            mcq("vandung", "Gieo xúc xắc 30 lần: mặt 1: 4 lần; 2: 6 lần; 3: 5 lần; 4: 3 lần; 5: 7 lần; còn lại mặt 6. Mặt 6 xuất hiện:", ["5 lần", "4 lần", "6 lần", "25 lần"], 0, "4 + 6 + 5 + 3 + 7 = 25; mặt 6: 30 − 25 = **5** lần."),
            short("vandung", "Dãy số liệu số km bác Ba chạy trong 5 ngày: 4, 6, 5, 7, 8. Trung bình mỗi ngày bác chạy bao nhiêu ki-lô-mét?", ["6"], "(4 + 6 + 5 + 7 + 8) : 5 = 30 : 5 = 6 (km).\nĐáp số: **6 km**.", unit="km"),
        ],
    },
    {
        "topic": "l4-cd10-phan-so",
        "title": "Phân số",
        "icon": "🍰",
        "description": "Chủ đề 10 · SGK Toán 4 tập hai (tr. 49–73): Bài 53 – Bài 59. Khái niệm phân số; phân số và phép chia số tự nhiên; tính chất cơ bản của phân số; rút gọn phân số; quy đồng mẫu số; so sánh phân số.",
        "requirements": [
            "Nhận biết được khái niệm ban đầu về phân số, tử số, mẫu số; đọc, viết được phân số.",
            "Nhận biết được thương của phép chia số tự nhiên cho số tự nhiên (khác 0) có thể viết dưới dạng phân số.",
            "Nhận biết được tính chất cơ bản của phân số; rút gọn được phân số; quy đồng được mẫu số hai phân số (một mẫu chia hết cho mẫu kia).",
            "So sánh được hai phân số; sắp xếp được các phân số theo thứ tự; xác định phân số lớn nhất, bé nhất trong nhóm 4 phân số.",
        ],
        "definition": (
            "- **Phân số** $\\frac{a}{b}$ (b ≠ 0): **mẫu số** b cho biết đơn vị được chia thành b phần bằng nhau; **tử số** a cho biết lấy a phần.\n"
            "- **Phân số và phép chia**: a : b = $\\frac{a}{b}$ (b ≠ 0). Ví dụ 3 : 4 = $\\frac{3}{4}$; 8 : 1 = $\\frac{8}{1}$ = 8.\n"
            "- **Tính chất cơ bản**: nhân (hoặc chia) cả tử và mẫu với cùng một số tự nhiên khác 0 thì được phân số bằng phân số đã cho.\n"
            "- **Rút gọn**: chia cả tử và mẫu cho cùng một số > 1 đến khi được **phân số tối giản**.\n"
            "- **So sánh**: cùng mẫu → tử lớn hơn thì lớn hơn; cùng tử → mẫu bé hơn thì lớn hơn; khác mẫu → quy đồng rồi so sánh. Phân số < 1 khi tử < mẫu, = 1 khi tử = mẫu, > 1 khi tử > mẫu."
        ),
        "theory": (
            "### Bài 53. Khái niệm phân số\n"
            "- $\\frac{3}{5}$ đọc “ba phần năm”.\n"
            "### Bài 54. Phân số và phép chia số tự nhiên\n"
            "- 7 : 3 = $\\frac{7}{3}$ > 1.\n"
            "### Bài 55. Tính chất cơ bản của phân số\n"
            "- $\\frac{2}{3}$ = $\\frac{2 × 4}{3 × 4}$ = $\\frac{8}{12}$.\n"
            "### Bài 56. Rút gọn phân số\n"
            "- $\\frac{18}{24}$ = $\\frac{18 : 6}{24 : 6}$ = $\\frac{3}{4}$.\n"
            "### Bài 57. Quy đồng mẫu số các phân số\n"
            "- $\\frac{1}{3}$ và $\\frac{5}{6}$: 6 chia hết cho 3 → $\\frac{1}{3}$ = $\\frac{2}{6}$; giữ $\\frac{5}{6}$.\n"
            "### Bài 58. So sánh phân số\n"
            "- $\\frac{3}{7}$ < $\\frac{5}{7}$; $\\frac{2}{5}$ > $\\frac{2}{9}$; $\\frac{3}{4}$ và $\\frac{5}{8}$: $\\frac{3}{4}$ = $\\frac{6}{8}$ > $\\frac{5}{8}$.\n"
            "### Bài 59. Luyện tập chung"
        ),
        "formulas": [
            G("I. Khái niệm", F("Phân số", "$\\frac{a}{b}$ (b ≠ 0): a là tử số, b là mẫu số"), F("Phép chia", "a : b = $\\frac{a}{b}$"), F("So với 1", "$\\frac{a}{b}$ < 1 ⇔ a < b · $\\frac{a}{b}$ = 1 ⇔ a = b · $\\frac{a}{b}$ > 1 ⇔ a > b")),
            G("II. Tính chất cơ bản", F("Nhân", "$\\frac{a}{b}$ = $\\frac{a × m}{b × m}$, m ≠ 0"), F("Chia", "$\\frac{a}{b}$ = $\\frac{a : n}{b : n}$, n là ước chung"), F("Rút gọn", "Chia tử và mẫu cho cùng số đến khi tối giản", "$\\frac{24}{36}$ = $\\frac{2}{3}$.")),
            G("III. So sánh", F("Cùng mẫu", "Tử lớn hơn → lớn hơn"), F("Cùng tử", "Mẫu bé hơn → lớn hơn"), F("Khác mẫu", "Quy đồng mẫu rồi so sánh")),
        ],
        "example": "Rút gọn phân số $\\frac{36}{48}$ và so sánh với $\\frac{5}{8}$.",
        "example_answer": "$\\frac{36}{48}$ = $\\frac{36 : 12}{48 : 12}$ = **3/4**. Quy đồng: $\\frac{3}{4}$ = $\\frac{6}{8}$ > $\\frac{5}{8}$ ⇒ **36/48 > 5/8**.",
        "real_life": (
            "- Chia bánh pizza thành 8 phần, ăn 3 phần là ăn $\\frac{3}{8}$ cái bánh.\n"
            "- Công thức nấu ăn: $\\frac{1}{2}$ thìa muối, $\\frac{3}{4}$ cốc nước."
        ),
        "quiz": [
            mcq("biet", "Phân số “năm phần chín” viết là:", ["$\\frac{9}{5}$", "$\\frac{5}{9}$", "5,9", "59"], 1, "Tử số 5, mẫu số 9 → **5/9**."),
            mcq("biet", "Thương của phép chia 4 : 7 viết dưới dạng phân số là:", ["$\\frac{7}{4}$", "$\\frac{4}{7}$", "47", "$\\frac{3}{7}$"], 1, "a : b = $\\frac{a}{b}$ → **4/7**."),
            mcq("biet", "Phân số nào bằng 1?", ["$\\frac{5}{6}$", "$\\frac{7}{7}$", "$\\frac{8}{5}$", "$\\frac{0}{3}$"], 1, "Tử bằng mẫu → **7/7 = 1**."),
            mcq("biet", "Trong phân số $\\frac{3}{8}$, mẫu số là:", ["3", "8", "11", "5"], 1, "Số viết dưới gạch ngang là **mẫu số**: 8."),
            mcq("hieu", "Rút gọn phân số $\\frac{15}{25}$ được phân số tối giản:", ["$\\frac{3}{5}$", "$\\frac{5}{3}$", "$\\frac{15}{25}$", "$\\frac{1}{5}$"], 0, "Chia cả tử và mẫu cho 5: **3/5**."),
            mcq("hieu", "Quy đồng mẫu số hai phân số $\\frac{3}{4}$ và $\\frac{5}{12}$ được:", ["$\\frac{9}{12}$ và $\\frac{5}{12}$", "$\\frac{3}{12}$ và $\\frac{5}{12}$", "$\\frac{12}{16}$ và $\\frac{5}{12}$", "$\\frac{9}{12}$ và $\\frac{15}{36}$"], 0, "12 : 4 = 3 → $\\frac{3}{4}$ = $\\frac{9}{12}$; giữ nguyên $\\frac{5}{12}$."),
            tf("hieu", "Nhận định: “$\\frac{2}{5}$ > $\\frac{2}{7}$.”", True, "Cùng tử số, mẫu 5 < 7 nên $\\frac{2}{5}$ > $\\frac{2}{7}$ → **Đúng**."),
            tf("hieu", "Nhận định: “$\\frac{4}{6}$ = $\\frac{6}{9}$.”", True, "$\\frac{4}{6}$ = $\\frac{2}{3}$ và $\\frac{6}{9}$ = $\\frac{2}{3}$ → bằng nhau → **Đúng**."),
            mcq("vandung", "Sắp xếp $\\frac{5}{6}$, $\\frac{2}{3}$, $\\frac{3}{4}$ theo thứ tự từ bé đến lớn (quy đồng mẫu 12):", ["$\\frac{2}{3}$, $\\frac{3}{4}$, $\\frac{5}{6}$", "$\\frac{5}{6}$, $\\frac{3}{4}$, $\\frac{2}{3}$", "$\\frac{3}{4}$, $\\frac{2}{3}$, $\\frac{5}{6}$", "$\\frac{2}{3}$, $\\frac{5}{6}$, $\\frac{3}{4}$"], 0, "$\\frac{5}{6}$ = $\\frac{10}{12}$; $\\frac{2}{3}$ = $\\frac{8}{12}$; $\\frac{3}{4}$ = $\\frac{9}{12}$ → 8 < 9 < 10: **2/3, $\\frac{3}{4}$, 5/6**."),
            short("vandung", "Một lớp có 32 học sinh, trong đó có 12 học sinh nam. Phân số chỉ số học sinh nam so với cả lớp (đã rút gọn) là bao nhiêu? (viết dạng $\\frac{a}{b}$)", ["3/8"], "Phân số: $\\frac{12}{32}$ = $\\frac{12 : 4}{32 : 4}$ = **3/8**."),
        ],
    },
    {
        "topic": "l4-cd11-cong-tru-phan-so",
        "title": "Phép cộng, phép trừ phân số",
        "icon": "➕",
        "description": "Chủ đề 11 · SGK Toán 4 tập hai (tr. 74–85): Bài 60 – Bài 62. Phép cộng phân số; phép trừ phân số (cùng mẫu số và khác mẫu số).",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ hai phân số cùng mẫu số; hai phân số khác mẫu số trong trường hợp có một mẫu số chia hết cho mẫu số còn lại.",
            "Vận dụng tính chất giao hoán, kết hợp của phép cộng phân số để tính hợp lí.",
            "Giải quyết được vấn đề thực tế liên quan đến cộng, trừ phân số.",
        ],
        "definition": (
            "- **Cùng mẫu**: $\\frac{a}{m}$ + $\\frac{b}{m}$ = $\\frac{a + b}{m}$; $\\frac{a}{m}$ − $\\frac{b}{m}$ = $\\frac{a − b}{m}$ (giữ nguyên mẫu số).\n"
            "- **Khác mẫu**: quy đồng mẫu số rồi cộng (trừ) như cùng mẫu.\n"
            "- Cộng (trừ) số tự nhiên với phân số: viết số tự nhiên dưới dạng phân số có cùng mẫu (2 = $\\frac{8}{4}$).\n"
            "- Kết quả nên **rút gọn** về phân số tối giản."
        ),
        "theory": (
            "### Bài 60. Phép cộng phân số\n"
            "- $\\frac{2}{7}$ + $\\frac{3}{7}$ = $\\frac{5}{7}$. $\\frac{1}{4}$ + $\\frac{3}{8}$ = $\\frac{2}{8}$ + $\\frac{3}{8}$ = $\\frac{5}{8}$.\n"
            "### Bài 61. Phép trừ phân số\n"
            "- $\\frac{5}{6}$ − $\\frac{1}{6}$ = $\\frac{4}{6}$ = $\\frac{2}{3}$. $\\frac{3}{4}$ − $\\frac{1}{2}$ = $\\frac{3}{4}$ − $\\frac{2}{4}$ = $\\frac{1}{4}$.\n"
            "### Bài 62. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cùng mẫu", F("Cộng", "$\\frac{a}{m}$ + $\\frac{b}{m}$ = $\\frac{a + b}{m}$"), F("Trừ", "$\\frac{a}{m}$ − $\\frac{b}{m}$ = $\\frac{a − b}{m}$")),
            G("II. Khác mẫu", F("Quy tắc", "Quy đồng mẫu số → cộng/trừ tử số → rút gọn"), F("Với số tự nhiên", "n + $\\frac{a}{b}$ = $\\frac{n × b + a}{b}$", "2 + $\\frac{1}{3}$ = $\\frac{6}{3}$ + $\\frac{1}{3}$ = $\\frac{7}{3}$.")),
            G("III. Tính chất", F("Giao hoán, kết hợp", "$\\frac{a}{b}$ + $\\frac{c}{d}$ = $\\frac{c}{d}$ + $\\frac{a}{b}$ · (x + y) + z = x + (y + z)")),
        ],
        "example": "Một vòi nước giờ thứ nhất chảy được $\\frac{2}{9}$ bể, giờ thứ hai chảy được $\\frac{1}{3}$ bể. Hỏi sau hai giờ vòi chảy được bao nhiêu phần của bể?",
        "example_answer": "$\\frac{2}{9}$ + $\\frac{1}{3}$ = $\\frac{2}{9}$ + $\\frac{3}{9}$ = **5/9** (bể).",
        "real_life": "- Cộng các phần bánh đã ăn; tính phần quãng đường còn lại; pha chế theo tỉ lệ.",
        "quiz": [
            mcq("biet", "$\\frac{3}{8}$ + $\\frac{4}{8}$ = ?", ["$\\frac{7}{16}$", "$\\frac{7}{8}$", "$\\frac{1}{8}$", "$\\frac{12}{8}$"], 1, "Cùng mẫu: $\\frac{3 + 4}{8}$ = **7/8**.", note="Không cộng mẫu số với nhau."),
            mcq("biet", "$\\frac{7}{9}$ − $\\frac{2}{9}$ = ?", ["$\\frac{5}{9}$", "$\\frac{5}{0}$", "$\\frac{9}{9}$", "$\\frac{5}{18}$"], 0, "$\\frac{7 − 2}{9}$ = **5/9**."),
            mcq("biet", "Muốn cộng hai phân số khác mẫu số, trước hết ta:", ["Cộng tử với tử, mẫu với mẫu", "Quy đồng mẫu số", "Rút gọn tử số", "Nhân chéo"], 1, "Trước hết phải **quy đồng mẫu số**."),
            mcq("biet", "$\\frac{1}{5}$ + $\\frac{2}{5}$ = ?", ["$\\frac{3}{10}$", "$\\frac{3}{5}$", "$\\frac{2}{25}$", "$\\frac{1}{5}$"], 1, "$\\frac{1 + 2}{5}$ = **3/5**."),
            mcq("hieu", "$\\frac{1}{2}$ + $\\frac{1}{4}$ = ?", ["$\\frac{2}{6}$", "$\\frac{3}{4}$", "$\\frac{1}{6}$", "$\\frac{2}{4}$"], 1, "$\\frac{1}{2}$ = $\\frac{2}{4}$ → $\\frac{2}{4}$ + $\\frac{1}{4}$ = **3/4**."),
            mcq("hieu", "$\\frac{5}{6}$ − $\\frac{1}{3}$ = ?", ["$\\frac{4}{3}$", "$\\frac{1}{2}$", "$\\frac{4}{6}$", "$\\frac{1}{3}$"], 1, "$\\frac{1}{3}$ = $\\frac{2}{6}$ → $\\frac{5}{6}$ − $\\frac{2}{6}$ = $\\frac{3}{6}$ = **1/2**."),
            tf("hieu", "Nhận định: “2 − $\\frac{3}{4}$ = $\\frac{5}{4}$.”", True, "2 = $\\frac{8}{4}$ → $\\frac{8}{4}$ − $\\frac{3}{4}$ = $\\frac{5}{4}$ → **Đúng**."),
            tf("hieu", "Nhận định: “$\\frac{2}{3}$ + $\\frac{1}{6}$ = $\\frac{3}{9}$.”", False, "Quy đồng: $\\frac{4}{6}$ + $\\frac{1}{6}$ = $\\frac{5}{6}$; cộng cả tử lẫn mẫu ra $\\frac{3}{9}$ là sai quy tắc → **Sai**."),
            mcq("vandung", "Một tấm vải, ngày đầu bán $\\frac{2}{5}$ tấm, ngày sau bán $\\frac{3}{10}$ tấm. Còn lại bao nhiêu phần tấm vải?", ["$\\frac{3}{10}$", "$\\frac{7}{10}$", "$\\frac{1}{2}$", "$\\frac{1}{10}$"], 0, "Đã bán: $\\frac{2}{5}$ + $\\frac{3}{10}$ = $\\frac{4}{10}$ + $\\frac{3}{10}$ = $\\frac{7}{10}$. Còn lại: 1 − $\\frac{7}{10}$ = **3/10** tấm."),
            short("vandung", "Tính bằng cách thuận tiện: $\\frac{3}{7}$ + $\\frac{5}{9}$ + $\\frac{4}{7}$ + $\\frac{4}{9}$ = ? (viết số tự nhiên)", ["2"], "($\\frac{3}{7}$ + $\\frac{4}{7}$) + ($\\frac{5}{9}$ + $\\frac{4}{9}$) = $\\frac{7}{7}$ + $\\frac{9}{9}$ = 1 + 1 = **2**."),
        ],
    },
    {
        "topic": "l4-cd12-nhan-chia-phan-so",
        "title": "Phép nhân, phép chia phân số",
        "icon": "✖️",
        "description": "Chủ đề 12 · SGK Toán 4 tập hai (tr. 86–101): Bài 63 – Bài 66. Phép nhân phân số; phép chia phân số; tìm phân số của một số.",
        "requirements": [
            "Thực hiện được phép nhân, phép chia hai phân số; nhân, chia phân số với số tự nhiên.",
            "Tìm được phân số của một số.",
            "Giải quyết được vấn đề thực tế liên quan đến bốn phép tính với phân số.",
        ],
        "definition": (
            "- **Nhân**: $\\frac{a}{b}$ × $\\frac{c}{d}$ = $\\frac{a × c}{b × d}$ (tử nhân tử, mẫu nhân mẫu).\n"
            "- **Phân số đảo ngược** của $\\frac{c}{d}$ là $\\frac{d}{c}$. **Chia**: $\\frac{a}{b}$ : $\\frac{c}{d}$ = $\\frac{a}{b}$ × $\\frac{d}{c}$ (nhân với phân số đảo ngược).\n"
            "- **Tìm $\\frac{m}{n}$ của một số a**: lấy a × $\\frac{m}{n}$ (hoặc a : n × m)."
        ),
        "theory": (
            "### Bài 63. Phép nhân phân số\n"
            "- $\\frac{2}{3}$ × $\\frac{4}{5}$ = $\\frac{8}{15}$; $\\frac{3}{4}$ × 2 = $\\frac{6}{4}$ = $\\frac{3}{2}$. Diện tích hình chữ nhật $\\frac{3}{4}$ m × $\\frac{2}{5}$ m = $\\frac{6}{20}$ = $\\frac{3}{10}$ m².\n"
            "### Bài 64. Phép chia phân số\n"
            "- $\\frac{3}{5}$ : $\\frac{2}{7}$ = $\\frac{3}{5}$ × $\\frac{7}{2}$ = $\\frac{21}{10}$; $\\frac{4}{5}$ : 2 = $\\frac{4}{5}$ × $\\frac{1}{2}$ = $\\frac{2}{5}$.\n"
            "### Bài 65. Tìm phân số của một số\n"
            "- $\\frac{2}{3}$ của 18 là 18 × $\\frac{2}{3}$ = 12.\n"
            "### Bài 66. Luyện tập chung"
        ),
        "formulas": [
            G("I. Nhân – chia", F("Nhân", "$\\frac{a}{b}$ × $\\frac{c}{d}$ = $\\frac{a × c}{b × d}$"), F("Chia", "$\\frac{a}{b}$ : $\\frac{c}{d}$ = $\\frac{a}{b}$ × $\\frac{d}{c}$"), F("Với số tự nhiên", "$\\frac{a}{b}$ × n = $\\frac{a × n}{b}$ · $\\frac{a}{b}$ : n = $\\frac{a}{b × n}$")),
            G("II. Phân số của một số", F("Quy tắc", "$\\frac{m}{n}$ của a = a × $\\frac{m}{n}$", "$\\frac{3}{4}$ của 20 kg = 20 × $\\frac{3}{4}$ = 15 kg.")),
            G("III. Thứ tự", F("Biểu thức", "Nhân, chia trước; cộng, trừ sau (như số tự nhiên)")),
        ],
        "example": "Một hình chữ nhật có chiều dài $\\frac{4}{5}$ m, chiều rộng $\\frac{2}{3}$ m. Tính diện tích hình chữ nhật.",
        "example_answer": "S = $\\frac{4}{5}$ × $\\frac{2}{3}$ = **8/15 m²**.",
        "real_life": "- Tính $\\frac{3}{4}$ số tiền tiết kiệm; chia $\\frac{3}{4}$ l nước vào các cốc $\\frac{1}{8}$ l.",
        "quiz": [
            mcq("biet", "$\\frac{2}{3}$ × $\\frac{1}{5}$ = ?", ["$\\frac{3}{8}$", "$\\frac{2}{15}$", "$\\frac{2}{8}$", "$\\frac{10}{3}$"], 1, "$\\frac{2 × 1}{3 × 5}$ = **2/15**."),
            mcq("biet", "Phân số đảo ngược của $\\frac{4}{9}$ là:", ["$\\frac{9}{4}$", "$\\frac{4}{9}$", "$\\frac{1}{4}$", "$-\\frac{4}{9}$"], 0, "Đổi chỗ tử và mẫu → **9/4**."),
            mcq("biet", "Muốn chia hai phân số, ta lấy phân số thứ nhất:", ["Chia tử cho tử, mẫu cho mẫu", "Nhân với phân số thứ hai đảo ngược", "Cộng với phân số thứ hai", "Nhân với phân số thứ hai"], 1, "$\\frac{a}{b}$ : $\\frac{c}{d}$ = $\\frac{a}{b}$ × **d/c**."),
            mcq("biet", "$\\frac{1}{2}$ của 30 là:", ["15", "60", "2", "32"], 0, "30 × $\\frac{1}{2}$ = **15**."),
            mcq("hieu", "$\\frac{3}{4}$ : $\\frac{1}{2}$ = ?", ["$\\frac{3}{8}$", "$\\frac{3}{2}$", "$\\frac{2}{3}$", "$\\frac{4}{6}$"], 1, "$\\frac{3}{4}$ × $\\frac{2}{1}$ = $\\frac{6}{4}$ = **3/2**."),
            mcq("hieu", "$\\frac{2}{5}$ của 45 kg là:", ["18 kg", "9 kg", "90 kg", "112 kg"], 0, "45 × $\\frac{2}{5}$ = $\\frac{90}{5}$ = **18 kg**."),
            tf("hieu", "Nhận định: “$\\frac{5}{6}$ × 3 = $\\frac{15}{18}$.”", False, "$\\frac{5}{6}$ × 3 = $\\frac{15}{6}$ = $\\frac{5}{2}$; chỉ nhân tử số với 3, không nhân mẫu → **Sai**."),
            tf("hieu", "Nhận định: “$\\frac{4}{7}$ : 2 = $\\frac{2}{7}$.”", True, "$\\frac{4}{7}$ : 2 = $\\frac{4}{7 × 2}$ = $\\frac{4}{14}$ = $\\frac{2}{7}$ → **Đúng**."),
            mcq("vandung", "Một thửa ruộng thu được 1200 kg thóc. Người ta bán $\\frac{3}{4}$ số thóc. Số thóc còn lại là:", ["300 kg", "900 kg", "400 kg", "1600 kg"], 0, "Đã bán: 1200 × $\\frac{3}{4}$ = 900 (kg). Còn lại: 1200 − 900 = **300 kg**.", alt="Còn lại 1 − $\\frac{3}{4}$ = $\\frac{1}{4}$ số thóc: 1200 × $\\frac{1}{4}$ = 300 kg."),
            short("vandung", "Có $\\frac{3}{4}$ l nước cam rót đều vào các cốc, mỗi cốc $\\frac{1}{8}$ l. Rót được bao nhiêu cốc?", ["6"], "$\\frac{3}{4}$ : $\\frac{1}{8}$ = $\\frac{3}{4}$ × $\\frac{8}{1}$ = $\\frac{24}{4}$ = 6 (cốc).\nĐáp số: **6 cốc**.", unit="cốc"),
        ],
    },
    {
        "topic": "l4-cd13-on-tap-cuoi-nam",
        "title": "Ôn tập cuối năm",
        "icon": "🏁",
        "description": "Chủ đề 13 · SGK Toán 4 tập hai (tr. 102–118): Bài 67 – Bài 73. Ôn tập số tự nhiên và phép tính với số tự nhiên; phân số và phép tính với phân số; hình học và đo lường; thống kê và xác suất.",
        "requirements": [
            "Củng cố số tự nhiên đến lớp triệu; bốn phép tính và các tính chất; trung bình cộng; tổng – hiệu; rút về đơn vị.",
            "Củng cố khái niệm, rút gọn, quy đồng, so sánh phân số; bốn phép tính với phân số; tìm phân số của một số.",
            "Củng cố góc, vuông góc, song song, hình bình hành, hình thoi; đơn vị đo khối lượng, diện tích, thời gian.",
            "Đọc dãy số liệu, biểu đồ cột; kiểm đếm số lần xuất hiện của sự kiện.",
        ],
        "definition": (
            "- Số tự nhiên: hàng – lớp; tính chất giao hoán, kết hợp, phân phối.\n"
            "- Phân số: $\\frac{a}{b}$; nhân chia: tử × tử, mẫu × mẫu; chia = nhân đảo ngược; cộng trừ: quy đồng.\n"
            "- Đo lường: 1 tấn = 1000 kg; 1 m² = 100 dm²; 1 thế kỉ = 100 năm."
        ),
        "theory": (
            "### Bài 67. Ôn tập số tự nhiên\n"
            "### Bài 68. Ôn tập phép tính với số tự nhiên\n"
            "### Bài 69. Ôn tập phân số\n"
            "### Bài 70. Ôn tập phép tính với phân số\n"
            "### Bài 71. Ôn tập hình học và đo lường\n"
            "### Bài 72. Ôn tập một số yếu tố thống kê và xác suất\n"
            "### Bài 73. Ôn tập chung"
        ),
        "formulas": [
            G("I. Giải toán", F("Trung bình cộng", "Tổng : số số hạng"), F("Tổng – hiệu", "Lớn = (S + H) : 2"), F("Phân số của một số", "a × $\\frac{m}{n}$")),
            G("II. Phân số", F("Cộng/trừ", "Quy đồng → cộng/trừ tử"), F("Nhân/chia", "$\\frac{a}{b}$ × $\\frac{c}{d}$ = ac/bd · $\\frac{a}{b}$ : $\\frac{c}{d}$ = $\\frac{a}{b}$ × $\\frac{d}{c}$")),
            G("III. Hình học", F("Hình chữ nhật", "P = (a + b) × 2 · S = a × b"), F("Hình thoi / hình vuông", "P = a × 4")),
        ],
        "example": "Tính: $\\frac{2}{3}$ + $\\frac{1}{2}$ × $\\frac{4}{9}$.",
        "example_answer": "Nhân trước: $\\frac{1}{2}$ × $\\frac{4}{9}$ = $\\frac{4}{18}$ = $\\frac{2}{9}$. Rồi cộng: $\\frac{2}{3}$ + $\\frac{2}{9}$ = $\\frac{6}{9}$ + $\\frac{2}{9}$ = **8/9**.",
        "real_life": "- Lập kế hoạch chi tiêu hè; tính diện tích vườn và số cây cần trồng; đọc biểu đồ kết quả học tập.",
        "quiz": [
            mcq("biet", "Giá trị của chữ số 8 trong số 3 845 120 là:", ["8000", "80 000", "800 000", "8 000 000"], 2, "3 | 845 | 120 → chữ số 8 ở hàng trăm nghìn: **800 000**."),
            mcq("biet", "Phân số tối giản của $\\frac{12}{18}$ là:", ["$\\frac{6}{9}$", "$\\frac{2}{3}$", "$\\frac{4}{6}$", "$\\frac{3}{2}$"], 1, "Chia cho 6: **2/3**."),
            mcq("biet", "2 tấn 30 kg = … kg?", ["230", "2030", "2300", "20 030"], 1, "2000 + 30 = **2030 kg**."),
            mcq("biet", "Góc lớn hơn góc vuông nhưng bé hơn góc bẹt là:", ["Góc nhọn", "Góc tù", "Góc vuông", "Góc bẹt"], 1, "Đó là **góc tù**."),
            mcq("hieu", "$\\frac{3}{5}$ + $\\frac{2}{5}$ × $\\frac{1}{2}$ = ?", ["$\\frac{1}{2}$", "$\\frac{4}{5}$", "$\\frac{5}{10}$", "$\\frac{7}{10}$"], 1, "Nhân trước: $\\frac{2}{5}$ × $\\frac{1}{2}$ = $\\frac{1}{5}$; $\\frac{3}{5}$ + $\\frac{1}{5}$ = **4/5**."),
            mcq("hieu", "Trung bình cộng của hai số là 45, một số là 38. Số còn lại là:", ["52", "7", "83", "41"], 0, "Tổng hai số: 45 × 2 = 90; số còn lại: 90 − 38 = **52**."),
            tf("hieu", "Nhận định: “$\\frac{7}{8}$ > $\\frac{8}{9}$.”", False, "$\\frac{7}{8}$ = 1 − $\\frac{1}{8}$; $\\frac{8}{9}$ = 1 − $\\frac{1}{9}$; vì $\\frac{1}{8}$ > $\\frac{1}{9}$ nên $\\frac{7}{8}$ < $\\frac{8}{9}$ → **Sai**.", alt="Quy đồng mẫu 72: $\\frac{63}{72}$ < $\\frac{64}{72}$."),
            tf("hieu", "Nhận định: “58 × 101 = 5858.”", True, "58 × 101 = 58 × 100 + 58 × 1 = 5800 + 58 = 5858 → **Đúng**."),
            mcq("vandung", "Một mảnh vườn hình chữ nhật dài 60 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Diện tích mảnh vườn là:", ["2400 m²", "200 m²", "3600 m²", "4000 m²"], 0, "Chiều rộng: 60 × $\\frac{2}{3}$ = 40 (m). S = 60 × 40 = **2400 m²**."),
            short("vandung", "Tổng số tuổi của hai mẹ con là 48 tuổi; tuổi con bằng $\\frac{1}{3}$ tuổi mẹ. Hỏi con bao nhiêu tuổi?", ["12"], "Coi tuổi con là 1 phần, tuổi mẹ là 3 phần → tổng 4 phần = 48 tuổi. Tuổi con: 48 : 4 = 12 (tuổi).\nĐáp số: **12 tuổi**.", unit="tuổi"),
        ],
    },
]
