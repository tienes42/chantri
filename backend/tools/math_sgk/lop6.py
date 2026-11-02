"""TOÁN 6 — Kết nối tri thức với cuộc sống (tập một, tập hai).

9 chương đánh số (I – IX) đúng thứ tự mục lục SGK.
Mỗi chương: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 6

LESSONS = [
    # ===================== CHƯƠNG I =====================
    {
        "topic": "l6-ch01-tap-hop-cac-so-tu-nhien",
        "title": "Tập hợp các số tự nhiên",
        "icon": "🔢",
        "description": "Chương I · SGK Toán 6 tập một (tr. 5–28): Bài 1 – Bài 7. Tập hợp; cách ghi số tự nhiên; thứ tự trong tập hợp số tự nhiên; phép cộng, trừ, nhân, chia số tự nhiên; luỹ thừa với số mũ tự nhiên; thứ tự thực hiện các phép tính.",
        "requirements": [
            "Sử dụng được thuật ngữ tập hợp, phần tử thuộc (không thuộc) một tập hợp; mô tả tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng.",
            "Nhận biết được tập hợp các số tự nhiên; biểu diễn số tự nhiên trong hệ thập phân; biểu diễn các số tự nhiên từ 1 đến 30 bằng số La Mã.",
            "Thực hiện được các phép tính cộng, trừ, nhân, chia trong tập hợp số tự nhiên; vận dụng tính chất giao hoán, kết hợp, phân phối để tính nhẩm, tính hợp lí.",
            "Thực hiện được phép tính luỹ thừa với số mũ tự nhiên; nhân, chia hai luỹ thừa cùng cơ số.",
            "Nhận biết được thứ tự thực hiện các phép tính; giải quyết vấn đề thực tiễn gắn với các phép tính về số tự nhiên.",
        ],
        "definition": (
            "- **Tập hợp**: nhóm các đối tượng xác định (phần tử). Kí hiệu a ∈ A (a thuộc A), b ∉ A (b không thuộc A).\n"
            "- Hai cách mô tả: **liệt kê** A = {0; 1; 2; 3} hoặc **chỉ ra tính chất đặc trưng** A = {x ∈ ℕ | x < 4}.\n"
            "- ℕ = {0; 1; 2; 3; …}; ℕ* = {1; 2; 3; …} (số tự nhiên khác 0).\n"
            "- **Luỹ thừa**: aⁿ = a · a · … · a (n thừa số a), a là cơ số, n là số mũ; a¹ = a; quy ước a⁰ = 1 (a ≠ 0)."
        ),
        "theory": (
            "### Bài 1. Tập hợp\n- Dùng dấu ngoặc nhọn { }, các phần tử cách nhau bởi dấu “;”. Mỗi phần tử chỉ viết một lần.\n"
            "### Bài 2. Cách ghi số tự nhiên\n- Hệ thập phân dùng 10 chữ số 0–9; giá trị chữ số phụ thuộc vị trí: abc = a · 100 + b · 10 + c.\n"
            "- Số La Mã: I = 1, V = 5, X = 10; XIV = 14, XXIX = 29.\n"
            "### Bài 3. Thứ tự trong tập hợp các số tự nhiên\n- a < b thì trên tia số điểm a nằm bên trái điểm b; tính chất bắc cầu: a < b, b < c ⇒ a < c.\n"
            "### Bài 4. Phép cộng và phép trừ số tự nhiên\n- a − b chỉ thực hiện được trong ℕ khi a ≥ b.\n"
            "### Bài 5. Phép nhân và phép chia số tự nhiên\n- Phép chia có dư: a = b · q + r (0 ≤ r < b); r = 0 là phép chia hết.\n"
            "### Luyện tập chung\n"
            "### Bài 6. Luỹ thừa với số mũ tự nhiên\n- a² đọc “a bình phương”, a³ đọc “a lập phương”.\n"
            "### Bài 7. Thứ tự thực hiện các phép tính\n- Luỹ thừa → nhân, chia → cộng, trừ; có ngoặc: ( ) → [ ] → { }.\n"
            "### Luyện tập chung · Bài tập cuối chương I"
        ),
        "formulas": [
            G("I. Tính chất các phép tính", F("Giao hoán", "a + b = b + a · a · b = b · a"),
              F("Kết hợp", "(a + b) + c = a + (b + c) · (a · b) · c = a · (b · c)"),
              F("Phân phối", "a · (b + c) = a · b + a · c · a · (b − c) = a · b − a · c"),
              F("Chia có dư", "a = b · q + r, 0 ≤ r < b")),
            G("II. Luỹ thừa", F("Định nghĩa", "aⁿ = a · a · … · a (n thừa số)"),
              F("Nhân cùng cơ số", "aᵐ · aⁿ = aᵐ⁺ⁿ", "2³ · 2⁴ = 2⁷ = 128."),
              F("Chia cùng cơ số", "aᵐ : aⁿ = aᵐ⁻ⁿ (a ≠ 0, m ≥ n)", "5⁶ : 5⁴ = 5² = 25."),
              F("Quy ước", "a⁰ = 1 (a ≠ 0) · a¹ = a")),
            G("III. Thứ tự thực hiện", F("Không ngoặc", "Luỹ thừa → × : → + −"), F("Có ngoặc", "( ) → [ ] → { }")),
        ],
        "example": "Tính: 5 · 2³ − 18 : 3².",
        "example_answer": "Luỹ thừa trước: 2³ = 8; 3² = 9.\nNhân, chia: 5 · 8 = 40; 18 : 9 = 2.\nTrừ: 40 − 2 = **38**.",
        "real_life": "- Liệt kê tập hợp học sinh tham gia câu lạc bộ; số La Mã trên đồng hồ, thế kỉ.\n- Luỹ thừa mô tả sự tăng nhanh: vi khuẩn phân đôi sau mỗi giờ → sau 10 giờ gấp 2¹⁰ = 1024 lần.",
        "quiz": [
            mcq("biet", "Cho A = {2; 4; 6; 8}. Khẳng định nào đúng?", ["3 ∈ A", "6 ∈ A", "8 ∉ A", "4 ∉ A"], 1, "6 là một phần tử của A → **6 ∈ A**."),
            mcq("biet", "Số La Mã XXIV có giá trị là:", ["26", "24", "16", "14"], 1, "XX = 20, IV = 4 → **24**."),
            mcq("biet", "2⁵ bằng:", ["10", "25", "32", "7"], 2, "2⁵ = 2 · 2 · 2 · 2 · 2 = **32**.", note="Không lấy 2 · 5 = 10."),
            mcq("biet", "Kết quả của 7⁸ : 7⁶ viết dưới dạng luỹ thừa là:", ["7²", "7¹⁴", "1²", "7⁴⁸"], 0, "aᵐ : aⁿ = aᵐ⁻ⁿ → **7²**."),
            mcq("hieu", "Tập hợp B = {x ∈ ℕ | 3 ≤ x < 7} viết bằng cách liệt kê là:", ["{3; 4; 5; 6; 7}", "{3; 4; 5; 6}", "{4; 5; 6}", "{4; 5; 6; 7}"], 1, "x nhận 3, 4, 5, 6 (không lấy 7) → **{3; 4; 5; 6}**."),
            mcq("hieu", "Giá trị của biểu thức 180 − 4 · 5² là:", ["80", "4400", "155", "3900"], 0,
                "Luỹ thừa trước: 5² = 25; nhân: 4 · 25 = 100; trừ: 180 − 100 = **80**.", note="Tính (180 − 4) · 25 = 4400 là sai thứ tự."),
            tf4("hieu", "Cho các phép tính với số tự nhiên. Mỗi khẳng định sau đúng hay sai?",
                ["a) 3⁴ = 81", "b) 2³ · 2² = 2⁶", "c) 25 · 37 · 4 = 3700", "d) 10⁰ = 0"],
                [True, False, True, False],
                "a) 3⁴ = 3 · 3 · 3 · 3 = 81 → Đúng.\nb) 2³ · 2² = 2³⁺² = 2⁵ (cộng số mũ, không nhân) → Sai.\nc) (25 · 4) · 37 = 100 · 37 = 3700 → Đúng.\nd) Quy ước a⁰ = 1 nên 10⁰ = 1 → Sai."),
            tf4("hieu", "Cho phép chia 47 cho 5. Mỗi khẳng định sau đúng hay sai?",
                ["a) Thương là 9", "b) Số dư là 3", "c) 47 = 5 · 9 + 2", "d) Số dư có thể bằng 5"],
                [True, False, True, False],
                "47 = 5 · 9 + 2 nên thương 9, dư 2.\na) Đúng. b) Sai (dư 2). c) Đúng. d) Sai vì số dư luôn nhỏ hơn số chia (0 ≤ r < 5)."),
            mcq("vandung", "Một trường có 1245 học sinh đi tham quan bằng xe 45 chỗ (mỗi học sinh một chỗ). Cần ít nhất bao nhiêu xe?", ["27", "28", "29", "26"], 1,
                "1245 = 45 · 27 + 30 → 27 xe chở được 1215 em, còn 30 em cần thêm 1 xe ⇒ **28 xe**.", note="Chia có dư trong bài toán “ít nhất” phải lấy thương + 1."),
            short("vandung", "Một loại vi khuẩn cứ sau 1 giờ thì số lượng tăng gấp đôi. Ban đầu có 1 con, sau 8 giờ có bao nhiêu con?", ["256"],
                  "Sau n giờ có 2ⁿ con. Sau 8 giờ: 2⁸ = **256** con.", unit="con"),
        ],
    },
]

LESSONS += [
    # ===================== CHƯƠNG II =====================
    {
        "topic": "l6-ch02-tinh-chia-het",
        "title": "Tính chia hết trong tập hợp các số tự nhiên",
        "icon": "➗",
        "description": "Chương II · SGK Toán 6 tập một (tr. 29–56): Bài 8 – Bài 12. Quan hệ chia hết và tính chất; dấu hiệu chia hết cho 2, 5, 3, 9; số nguyên tố, phân tích ra thừa số nguyên tố; ước chung, ƯCLN; bội chung, BCNN.",
        "requirements": [
            "Nhận biết được quan hệ chia hết, khái niệm ước và bội; tính chất chia hết của một tổng.",
            "Vận dụng được dấu hiệu chia hết cho 2, 5, 9, 3 để xác định một số đã cho có chia hết cho 2, 5, 9, 3 hay không.",
            "Nhận biết được số nguyên tố, hợp số; phân tích được một số tự nhiên lớn hơn 1 thành tích các thừa số nguyên tố.",
            "Xác định được ước chung, ước chung lớn nhất; bội chung, bội chung nhỏ nhất của hai hoặc ba số; nhận biết phân số tối giản; cộng trừ phân số bằng cách sử dụng BCNN.",
            "Vận dụng kiến thức số học vào giải quyết vấn đề thực tiễn (chia đều, xếp hàng, lịch trùng nhau).",
        ],
        "definition": (
            "- a **chia hết** cho b (b ≠ 0), kí hiệu a ⋮ b, nếu có số tự nhiên k sao cho a = b · k. Khi đó a là **bội** của b, b là **ước** của a.\n"
            "- **Số nguyên tố**: số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó (2, 3, 5, 7, 11, …). **Hợp số**: số tự nhiên lớn hơn 1 có nhiều hơn hai ước. Số 0 và 1 không là số nguyên tố, không là hợp số.\n"
            "- **ƯCLN(a, b)**: số lớn nhất trong tập ước chung. **BCNN(a, b)**: số nhỏ nhất khác 0 trong tập bội chung.\n"
            "- a, b **nguyên tố cùng nhau** nếu ƯCLN(a, b) = 1."
        ),
        "theory": (
            "### Bài 8. Quan hệ chia hết và tính chất\n- Nếu a ⋮ m và b ⋮ m thì (a + b) ⋮ m; nếu a ⋮ m và b không chia hết cho m thì (a + b) không chia hết cho m.\n"
            "### Bài 9. Dấu hiệu chia hết\n- Cho 2: tận cùng 0, 2, 4, 6, 8. Cho 5: tận cùng 0, 5. Cho 9 (cho 3): tổng các chữ số chia hết cho 9 (cho 3).\n"
            "### Bài 10. Số nguyên tố\n- Phân tích ra thừa số nguyên tố bằng sơ đồ cây hoặc chia cột: 120 = 2³ · 3 · 5.\n"
            "### Luyện tập chung\n"
            "### Bài 11. Ước chung. Ước chung lớn nhất\n- Tìm ƯCLN: phân tích ra thừa số nguyên tố → chọn thừa số **chung** → lấy số mũ **nhỏ nhất** → nhân.\n- ƯC(a, b) = Ư(ƯCLN(a, b)).\n"
            "### Bài 12. Bội chung. Bội chung nhỏ nhất\n- Tìm BCNN: chọn thừa số **chung và riêng** → lấy số mũ **lớn nhất** → nhân. BC(a, b) = B(BCNN(a, b)).\n"
            "### Luyện tập chung · Bài tập cuối chương II"
        ),
        "formulas": [
            G("I. Dấu hiệu chia hết", F("Cho 2", "Chữ số tận cùng ∈ {0; 2; 4; 6; 8}"), F("Cho 5", "Chữ số tận cùng ∈ {0; 5}"),
              F("Cho 3", "Tổng các chữ số ⋮ 3"), F("Cho 9", "Tổng các chữ số ⋮ 9")),
            G("II. ƯCLN – BCNN", F("ƯCLN", "Thừa số chung, số mũ nhỏ nhất", "24 = 2³·3; 36 = 2²·3² ⇒ ƯCLN = 2²·3 = 12."),
              F("BCNN", "Thừa số chung và riêng, số mũ lớn nhất", "BCNN(24, 36) = 2³·3² = 72."),
              F("Liên hệ", "ƯCLN(a, b) · BCNN(a, b) = a · b", "12 · 72 = 864 = 24 · 36.")),
            G("III. Ứng dụng phân số", F("Rút gọn tối giản", "Chia tử và mẫu cho ƯCLN"), F("Mẫu chung nhỏ nhất", "BCNN của các mẫu")),
        ],
        "example": "Tìm ƯCLN(48, 60) và BCNN(48, 60).",
        "example_answer": "48 = 2⁴ · 3; 60 = 2² · 3 · 5.\nƯCLN = 2² · 3 = **12**; BCNN = 2⁴ · 3 · 5 = **240**. Kiểm tra: 12 · 240 = 2880 = 48 · 60 ✔.",
        "real_life": "- Chia đều phần thưởng (ƯCLN); tính thời điểm hai sự kiện lặp lại trùng nhau, xếp hàng vừa đủ (BCNN).",
        "quiz": [
            mcq("biet", "Số nào chia hết cho cả 2 và 5?", ["125", "250", "252", "205"], 1, "Chia hết cho cả 2 và 5 ⇔ tận cùng là 0 → **250**."),
            mcq("biet", "Số nào là số nguyên tố?", ["1", "9", "17", "21"], 2, "**17** chỉ có hai ước 1 và 17.", note="1 không phải số nguyên tố; 9 = 3·3; 21 = 3·7."),
            mcq("biet", "Phân tích 36 ra thừa số nguyên tố được:", ["4 · 9", "2² · 3²", "6²", "2 · 18"], 1, "36 = 2 · 2 · 3 · 3 = **2² · 3²** (các thừa số đều nguyên tố)."),
            mcq("biet", "Số nào chia hết cho 9?", ["4518", "3125", "2024", "1001"], 0, "4 + 5 + 1 + 8 = 18 ⋮ 9 → **4518**."),
            mcq("hieu", "ƯCLN(24, 36) bằng:", ["6", "12", "72", "4"], 1, "24 = 2³·3; 36 = 2²·3² ⇒ ƯCLN = 2²·3 = **12**."),
            mcq("hieu", "BCNN(12, 18) bằng:", ["6", "36", "216", "72"], 1, "12 = 2²·3; 18 = 2·3² ⇒ BCNN = 2²·3² = **36**."),
            tf4("hieu", "Cho số n = 2345. Mỗi khẳng định sau đúng hay sai?",
                ["a) n chia hết cho 2", "b) n chia hết cho 5", "c) n chia hết cho 3", "d) n là hợp số"],
                [False, True, False, True],
                "a) Tận cùng 5 (lẻ) → không chia hết cho 2 → Sai.\nb) Tận cùng 5 → chia hết cho 5 → Đúng.\nc) Tổng chữ số 2 + 3 + 4 + 5 = 14 không chia hết cho 3 → Sai.\nd) n có ước 5 (khác 1 và n) → hợp số → Đúng."),
            tf4("hieu", "Xét hai số 18 và 30. Mỗi khẳng định sau đúng hay sai?",
                ["a) ƯCLN(18, 30) = 6", "b) BCNN(18, 30) = 90", "c) 18 và 30 là hai số nguyên tố cùng nhau", "d) ƯC(18, 30) có đúng 4 phần tử"],
                [True, True, False, True],
                "18 = 2·3², 30 = 2·3·5.\na) ƯCLN = 2·3 = 6 → Đúng. b) BCNN = 2·3²·5 = 90 → Đúng.\nc) ƯCLN = 6 ≠ 1 → Sai. d) ƯC = Ư(6) = {1; 2; 3; 6} → 4 phần tử → Đúng."),
            mcq("vandung", "Cô giáo có 48 quyển vở và 60 bút bi, muốn chia đều thành các phần thưởng như nhau (mỗi phần có cả vở và bút). Số phần thưởng nhiều nhất là:", ["6", "12", "24", "240"], 1,
                "Số phần thưởng là ước chung lớn nhất: ƯCLN(48, 60) = **12** (mỗi phần 4 vở, 5 bút)."),
            short("vandung", "Hai xe buýt cùng xuất phát lúc 6 giờ sáng. Xe thứ nhất cứ 10 phút chạy một chuyến, xe thứ hai cứ 15 phút một chuyến. Sau ít nhất bao nhiêu phút hai xe lại cùng xuất phát?", ["30"],
                  "Thời gian cần tìm là BCNN(10, 15) = 2 · 3 · 5 = **30** phút (lúc 6 giờ 30 phút).", unit="phút"),
        ],
    },
    # ===================== CHƯƠNG III =====================
    {
        "topic": "l6-ch03-so-nguyen",
        "title": "Số nguyên",
        "icon": "🌡️",
        "description": "Chương III · SGK Toán 6 tập một (tr. 57–76): Bài 13 – Bài 17. Tập hợp các số nguyên; phép cộng và phép trừ số nguyên; quy tắc dấu ngoặc; phép nhân số nguyên; phép chia hết, ước và bội của một số nguyên.",
        "requirements": [
            "Nhận biết được số nguyên âm, tập hợp các số nguyên; biểu diễn số nguyên trên trục số; nhận biết số đối của một số nguyên.",
            "Nhận biết được thứ tự trong tập hợp các số nguyên; so sánh được hai số nguyên.",
            "Thực hiện được phép cộng, trừ, nhân, chia (chia hết) trong tập hợp số nguyên; vận dụng tính chất phép tính và quy tắc dấu ngoặc để tính hợp lí.",
            "Nhận biết được quan hệ chia hết, ước và bội trong tập hợp số nguyên.",
            "Giải quyết vấn đề thực tiễn gắn với số nguyên (nhiệt độ, độ cao, lãi lỗ, …).",
        ],
        "definition": (
            "- **Tập hợp số nguyên** ℤ = {…; −3; −2; −1; 0; 1; 2; 3; …}, gồm số nguyên âm, số 0 và số nguyên dương. Số 0 không âm, không dương.\n"
            "- **Số đối** của a là −a (a + (−a) = 0); số đối của −5 là 5.\n"
            "- **So sánh**: trên trục số nằm ngang, điểm a nằm bên trái điểm b thì a < b. Mọi số nguyên âm nhỏ hơn 0 và nhỏ hơn mọi số nguyên dương.\n"
            "- a ⋮ b (b ≠ 0) trong ℤ nếu a = b · q với q ∈ ℤ; nếu a là bội của b thì −a cũng là bội của b."
        ),
        "theory": (
            "### Bài 13. Tập hợp các số nguyên\n- −7 < −3 < 0 < 2.\n"
            "### Bài 14. Phép cộng và phép trừ số nguyên\n- Cộng hai số **cùng dấu**: cộng phần số tự nhiên, giữ dấu chung: (−7) + (−5) = −12.\n"
            "- Cộng hai số **khác dấu**: lấy phần số tự nhiên lớn trừ nhỏ, lấy dấu của số có phần số tự nhiên lớn hơn: (−9) + 4 = −5.\n"
            "- **Trừ**: a − b = a + (−b): 5 − 12 = 5 + (−12) = −7.\n"
            "### Bài 15. Quy tắc dấu ngoặc\n- Bỏ ngoặc có dấu “+” đứng trước: giữ nguyên dấu; có dấu “−” đứng trước: đổi dấu tất cả các số hạng trong ngoặc.\n"
            "### Luyện tập chung\n"
            "### Bài 16. Phép nhân số nguyên\n- Cùng dấu → tích dương; khác dấu → tích âm: (−3) · (−4) = 12; (−6) · 5 = −30.\n"
            "### Bài 17. Phép chia hết. Ước và bội của một số nguyên\n- (−20) : 5 = −4; Ư(6) = {±1; ±2; ±3; ±6}.\n"
            "### Luyện tập chung · Bài tập cuối chương III"
        ),
        "formulas": [
            G("I. Cộng – trừ", F("Số đối", "a + (−a) = 0"), F("Phép trừ", "a − b = a + (−b)"),
              F("Quy tắc dấu ngoặc", "−(a − b + c) = −a + b − c · +(a − b) = a − b")),
            G("II. Nhân – chia", F("Quy tắc dấu", "(+)·(+) = (+) · (−)·(−) = (+) · (+)·(−) = (−)"),
              F("Tính chất", "a · (b + c) = a · b + a · c (trong ℤ)"), F("Luỹ thừa số âm", "(−a)ⁿ dương nếu n chẵn, âm nếu n lẻ", "(−2)³ = −8; (−2)⁴ = 16.")),
        ],
        "example": "Tính hợp lí: (−37) + 54 + (−63) + 46.",
        "example_answer": "[(−37) + (−63)] + (54 + 46) = (−100) + 100 = **0**.",
        "real_life": "- Nhiệt độ dưới 0 °C, độ sâu dưới mực nước biển, lãi (+) / lỗ (−), năm trước Công nguyên.",
        "quiz": [
            mcq("biet", "Số đối của −8 là:", ["−8", "8", "0", "1/8"], 1, "Số đối của −8 là **8** vì (−8) + 8 = 0."),
            mcq("biet", "Sắp xếp nào đúng?", ["−5 < −7 < 0", "−7 < −5 < 0", "0 < −5 < −7", "−5 < 0 < −7"], 1, "Trên trục số −7 nằm bên trái −5 → **−7 < −5 < 0**."),
            mcq("biet", "(−12) + (−8) = ?", ["−20", "20", "−4", "4"], 0, "Cùng dấu âm: 12 + 8 = 20, giữ dấu “−” → **−20**."),
            mcq("biet", "(−6) · (−7) = ?", ["−42", "42", "−13", "13"], 1, "Hai số cùng dấu → tích dương: **42**."),
            mcq("hieu", "15 − (−9) = ?", ["6", "24", "−24", "−6"], 1, "15 − (−9) = 15 + 9 = **24**.", note="Trừ số âm là cộng với số đối của nó."),
            mcq("hieu", "Bỏ dấu ngoặc rồi tính: 25 − (15 − 40) = ?", ["−30", "50", "0", "80"], 1, "25 − 15 + 40 = **50**."),
            tf4("hieu", "Mỗi khẳng định sau về số nguyên đúng hay sai?",
                ["a) −5 < −2", "b) (−3) · (−5) = −15", "c) (−8) + 8 = 0", "d) Số 0 là số nguyên dương"],
                [True, False, True, False],
                "a) −5 nằm bên trái −2 → Đúng.\nb) Cùng dấu → tích dương 15 → Sai.\nc) Tổng hai số đối bằng 0 → Đúng.\nd) 0 không âm, không dương → Sai."),
            tf4("hieu", "Mỗi khẳng định sau đúng hay sai?",
                ["a) −(a − b + c) = −a + b − c", "b) (−2)³ = −8", "c) (−2)⁴ = −16", "d) Ước của 6 trong ℤ chỉ gồm 1; 2; 3; 6"],
                [True, True, False, False],
                "a) Dấu “−” trước ngoặc → đổi dấu mọi số hạng → Đúng.\nb) Số mũ lẻ → âm: −8 → Đúng.\nc) Số mũ chẵn → dương: 16 → Sai.\nd) Trong ℤ, Ư(6) = {±1; ±2; ±3; ±6} → Sai."),
            mcq("vandung", "Nhiệt độ buổi sáng ở Sa Pa là −3 °C, đến trưa tăng thêm 8 °C, đến tối giảm 6 °C so với buổi trưa. Nhiệt độ buổi tối là:", ["−1 °C", "1 °C", "−5 °C", "11 °C"], 0,
                "(−3) + 8 − 6 = 5 − 6 = **−1 °C**."),
            short("vandung", "Một tàu ngầm đang ở độ cao −120 m (so với mực nước biển). Tàu nổi lên 45 m rồi lặn xuống thêm 30 m. Độ cao mới của tàu là bao nhiêu mét?", ["-105", "−105"],
                  "(−120) + 45 + (−30) = −75 − 30 = **−105** (m), tức là ở độ sâu 105 m dưới mực nước biển.", unit="m"),
        ],
    },
    # ===================== CHƯƠNG IV =====================
    {
        "topic": "l6-ch04-hinh-phang-trong-thuc-tien",
        "title": "Một số hình phẳng trong thực tiễn",
        "icon": "⬡",
        "description": "Chương IV · SGK Toán 6 tập một (tr. 77–97): Bài 18 – Bài 20. Hình tam giác đều, hình vuông, hình lục giác đều; hình chữ nhật, hình thoi, hình bình hành, hình thang cân; chu vi và diện tích của một số tứ giác đã học.",
        "requirements": [
            "Nhận dạng được tam giác đều, hình vuông, lục giác đều; mô tả được các yếu tố cơ bản (cạnh, góc, đường chéo).",
            "Mô tả được các yếu tố cơ bản của hình chữ nhật, hình thoi, hình bình hành, hình thang cân.",
            "Vẽ được tam giác đều, hình vuông bằng thước và compa (ê-ke); vẽ hình chữ nhật, hình thoi, hình bình hành.",
            "Giải quyết được vấn đề thực tiễn gắn với tính chu vi và diện tích của các hình đặc biệt nói trên.",
        ],
        "definition": (
            "- **Tam giác đều**: ba cạnh bằng nhau, ba góc bằng nhau (bằng 60°).\n"
            "- **Hình vuông**: bốn cạnh bằng nhau, bốn góc vuông, hai đường chéo bằng nhau.\n"
            "- **Lục giác đều**: sáu cạnh bằng nhau, sáu góc bằng nhau; ba đường chéo chính bằng nhau; ghép được từ 6 tam giác đều.\n"
            "- **Hình chữ nhật**: 4 góc vuông, các cạnh đối bằng nhau, hai đường chéo bằng nhau. **Hình thoi**: 4 cạnh bằng nhau, hai đường chéo vuông góc. **Hình bình hành**: các cạnh đối song song và bằng nhau, hai đường chéo cắt nhau tại trung điểm mỗi đường. **Hình thang cân**: hai đáy song song, hai cạnh bên bằng nhau, hai đường chéo bằng nhau, hai góc kề một đáy bằng nhau."
        ),
        "theory": (
            "### Bài 18. Hình tam giác đều. Hình vuông. Hình lục giác đều\n- Vẽ tam giác đều cạnh 3 cm bằng compa; vẽ hình vuông bằng ê-ke.\n"
            "### Bài 19. Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang cân\n"
            "### Bài 20. Chu vi và diện tích của một số tứ giác đã học\n"
            "### Luyện tập chung · Bài tập cuối chương IV"
        ),
        "formulas": [
            G("I. Chu vi", F("Hình vuông cạnh a", "C = 4a"), F("Hình chữ nhật a, b", "C = 2(a + b)"),
              F("Hình thoi cạnh a", "C = 4a"), F("Hình bình hành a, b", "C = 2(a + b)")),
            G("II. Diện tích", F("Hình vuông", "S = a²"), F("Hình chữ nhật", "S = a · b"),
              F("Hình thoi (hai đường chéo m, n)", "S = (m · n) : 2"), F("Hình bình hành (đáy a, chiều cao h)", "S = a · h"),
              F("Hình thang (đáy a, b; cao h)", "S = (a + b) · h : 2")),
        ],
        "example": "Một mảnh đất hình thang cân có hai đáy 30 m và 20 m, chiều cao 12 m. Tính diện tích và chi phí trồng cỏ nếu 1 m² hết 50 000 đồng.",
        "example_answer": "S = (30 + 20) · 12 : 2 = **300 m²**. Chi phí: 300 · 50 000 = **15 000 000 đồng**.",
        "real_life": "- Tổ ong hình lục giác đều; gạch lát hình thoi, hình vuông; mái nhà, chân bàn hình thang cân.",
        "quiz": [
            mcq("biet", "Mỗi góc của tam giác đều bằng:", ["45°", "60°", "90°", "120°"], 1, "Ba góc bằng nhau, tổng 180° → mỗi góc **60°**."),
            mcq("biet", "Hình nào có hai đường chéo vuông góc với nhau?", ["Hình chữ nhật (không vuông)", "Hình thoi", "Hình bình hành bất kì", "Hình thang cân"], 1, "**Hình thoi** có hai đường chéo vuông góc."),
            mcq("biet", "Diện tích hình bình hành có đáy a và chiều cao h là:", ["a · h : 2", "a · h", "2(a + h)", "(a + h) · 2"], 1, "S = **a · h**."),
            mcq("biet", "Lục giác đều có bao nhiêu cạnh bằng nhau?", ["4", "5", "6", "8"], 2, "Lục giác đều có **6** cạnh bằng nhau."),
            mcq("hieu", "Hình thoi có hai đường chéo dài 10 cm và 6 cm. Diện tích là:", ["60 cm²", "30 cm²", "16 cm²", "32 cm²"], 1, "S = 10 · 6 : 2 = **30 cm²**."),
            mcq("hieu", "Hình chữ nhật có chu vi 30 m, chiều dài 9 m. Diện tích là:", ["54 m²", "270 m²", "81 m²", "42 m²"], 0, "Nửa chu vi 15 m ⇒ chiều rộng 6 m; S = 9 · 6 = **54 m²**."),
            tf4("hieu", "Mỗi khẳng định sau về các tứ giác đúng hay sai?",
                ["a) Hình thoi có hai đường chéo vuông góc", "b) Hình bình hành luôn có hai đường chéo bằng nhau", "c) Hình thang cân có hai đường chéo bằng nhau", "d) Hình chữ nhật luôn có bốn cạnh bằng nhau"],
                [True, False, True, False],
                "a) Đúng. b) Sai — chỉ khi là hình chữ nhật. c) Đúng. d) Sai — chỉ khi là hình vuông."),
            tf4("hieu", "Tính diện tích, mỗi khẳng định sau đúng hay sai?",
                ["a) Hình thoi có hai đường chéo 6 cm và 8 cm có diện tích 24 cm²", "b) Hình bình hành đáy 10 cm, chiều cao 4 cm có diện tích 40 cm²",
                 "c) Hình thang có hai đáy 5 cm và 9 cm, chiều cao 4 cm có diện tích 56 cm²", "d) Hình vuông có chu vi 20 cm thì diện tích là 20 cm²"],
                [True, True, False, False],
                "a) 6 · 8 : 2 = 24 → Đúng. b) 10 · 4 = 40 → Đúng.\nc) (5 + 9) · 4 : 2 = 28 cm² (quên chia 2 mới ra 56) → Sai.\nd) Cạnh 5 cm ⇒ S = 25 cm² → Sai."),
            mcq("vandung", "Một khu vườn hình chữ nhật dài 25 m, rộng 16 m. Người ta làm một lối đi hình bình hành có đáy 2 m (đo theo chiều dài) và chiều cao bằng chiều rộng vườn. Diện tích phần còn lại để trồng rau là:", ["368 m²", "400 m²", "32 m²", "350 m²"], 0,
                "S vườn = 25 · 16 = 400 m²; S lối đi = 2 · 16 = 32 m². Phần trồng rau: 400 − 32 = **368 m²**."),
            short("vandung", "Một khung trang trí hình lục giác đều cạnh 15 cm được uốn từ một sợi dây thép. Cần bao nhiêu xăng-ti-mét dây (không tính mối nối)?", ["90"],
                  "Chu vi lục giác đều: 6 · 15 = **90 cm**.", unit="cm"),
        ],
    },
]

LESSONS += [
    # ===================== CHƯƠNG V =====================
    {
        "topic": "l6-ch05-tinh-doi-xung",
        "title": "Tính đối xứng của hình phẳng trong tự nhiên",
        "icon": "🦋",
        "description": "Chương V · SGK Toán 6 tập một (tr. 98–110): Bài 21 – Bài 22. Hình có trục đối xứng; hình có tâm đối xứng.",
        "requirements": [
            "Nhận biết được trục đối xứng của một hình phẳng; nhận biết được những hình phẳng trong tự nhiên có trục đối xứng.",
            "Nhận biết được tâm đối xứng của một hình phẳng; nhận biết được những hình phẳng trong thế giới tự nhiên có tâm đối xứng.",
            "Nhận biết được tính đối xứng trong Toán học, tự nhiên, nghệ thuật, kiến trúc, công nghệ chế tạo, …",
            "Nhận biết được vẻ đẹp của thế giới tự nhiên biểu hiện qua tính đối xứng.",
        ],
        "definition": (
            "- **Hình có trục đối xứng**: có một đường thẳng d chia hình thành hai phần, nếu “gấp” theo d thì hai phần **chồng khít** lên nhau. d là trục đối xứng.\n"
            "- **Hình có tâm đối xứng**: có một điểm O sao cho khi **quay hình nửa vòng (180°)** quanh O thì hình trùng với chính nó. O là tâm đối xứng.\n"
            "- Một hình có thể có nhiều trục đối xứng, có thể vừa có trục vừa có tâm đối xứng, hoặc không có."
        ),
        "theory": (
            "### Bài 21. Hình có trục đối xứng\n- Tam giác đều: 3 trục; hình vuông: 4 trục; hình chữ nhật, hình thoi: 2 trục; hình thang cân: 1 trục (đường thẳng qua trung điểm hai đáy); lục giác đều: 6 trục; hình tròn: vô số trục (mọi đường kính).\n"
            "### Bài 22. Hình có tâm đối xứng\n- Hình chữ nhật, hình vuông, hình thoi, hình bình hành: tâm là giao điểm hai đường chéo; lục giác đều, hình tròn: tâm là tâm của hình.\n- Tam giác đều, hình thang cân **không** có tâm đối xứng.\n"
            "### Luyện tập chung · Bài tập cuối chương V"
        ),
        "formulas": [
            G("I. Số trục đối xứng", F("Tam giác đều", "3"), F("Hình vuông", "4"), F("Hình chữ nhật / hình thoi", "2"),
              F("Hình thang cân", "1"), F("Lục giác đều", "6"), F("Hình tròn", "vô số")),
            G("II. Tâm đối xứng", F("Có tâm", "Hình bình hành, chữ nhật, thoi, vuông (giao hai đường chéo); lục giác đều; hình tròn"),
              F("Không có tâm", "Tam giác đều, hình thang cân")),
        ],
        "example": "Trong các chữ cái in hoa H, A, N, O: chữ nào có trục đối xứng, chữ nào có tâm đối xứng?",
        "example_answer": "Có trục đối xứng: **H, A, O**. Có tâm đối xứng: **H, N, O**. Chữ N có tâm nhưng không có trục; chữ A có trục nhưng không có tâm.",
        "real_life": "- Cánh bướm, lá cây, khuôn mặt (trục đối xứng); bông hoa, bánh xe, hoa văn gạch (tâm đối xứng); kiến trúc đình chùa, logo.",
        "quiz": [
            mcq("biet", "Hình vuông có bao nhiêu trục đối xứng?", ["1", "2", "4", "Vô số"], 2, "Hình vuông có **4** trục: 2 đường chéo và 2 đường nối trung điểm cạnh đối."),
            mcq("biet", "Hình nào sau đây **không** có tâm đối xứng?", ["Hình chữ nhật", "Tam giác đều", "Hình thoi", "Hình tròn"], 1, "**Tam giác đều** chỉ có trục, không có tâm đối xứng."),
            mcq("biet", "Tâm đối xứng của hình bình hành là:", ["Một đỉnh", "Trung điểm một cạnh", "Giao điểm hai đường chéo", "Không có"], 2, "Tâm là **giao điểm hai đường chéo**."),
            mcq("biet", "Hình tròn có bao nhiêu trục đối xứng?", ["1", "2", "4", "Vô số"], 3, "Mọi đường thẳng qua tâm đều là trục → **vô số**."),
            mcq("hieu", "Hình thang cân có mấy trục đối xứng?", ["0", "1", "2", "4"], 1, "**1** trục: đường thẳng đi qua trung điểm hai đáy."),
            mcq("hieu", "Chữ cái nào có tâm đối xứng nhưng không có trục đối xứng?", ["A", "N", "H", "M"], 1, "**N** quay 180° trùng chính nó nhưng không gấp đôi chồng khít được."),
            tf4("hieu", "Mỗi khẳng định sau về tính đối xứng đúng hay sai?",
                ["a) Tam giác đều có 3 trục đối xứng", "b) Hình bình hành (không phải hình chữ nhật, hình thoi) có trục đối xứng", "c) Hình thoi có tâm đối xứng", "d) Hình thang cân có tâm đối xứng"],
                [True, False, True, False],
                "a) Đúng (3 đường cao). b) Sai — hình bình hành thông thường không có trục đối xứng. c) Đúng (giao hai đường chéo). d) Sai — hình thang cân chỉ có trục đối xứng."),
            tf4("hieu", "Xét các chữ cái in hoa H, A, N. Mỗi khẳng định sau đúng hay sai?",
                ["a) Chữ H có cả trục đối xứng và tâm đối xứng", "b) Chữ A có trục đối xứng", "c) Chữ N có trục đối xứng", "d) Chữ N có tâm đối xứng"],
                [True, True, False, True],
                "a) H có 2 trục (dọc, ngang) và có tâm → Đúng. b) A có trục dọc → Đúng. c) N không có trục → Sai. d) N quay 180° trùng chính nó → Đúng."),
            mcq("vandung", "Một tờ giấy hình chữ nhật (không vuông). Có bao nhiêu cách gấp đôi tờ giấy để hai nửa chồng khít lên nhau?", ["1", "2", "4", "0"], 1,
                "Số cách gấp = số trục đối xứng của hình chữ nhật = **2** (gấp theo đường nối trung điểm các cạnh đối).", note="Gấp theo đường chéo hình chữ nhật thì hai nửa không chồng khít."),
            short("vandung", "Trong các chữ cái in hoa H, A, O, M, Z, E, có bao nhiêu chữ cái có tâm đối xứng?", ["3"],
                  "Các chữ có tâm đối xứng: H, O, Z → **3** chữ. (A, M, E chỉ có trục đối xứng.)"),
        ],
    },
    # ===================== CHƯƠNG VI =====================
    {
        "topic": "l6-ch06-phan-so",
        "title": "Phân số",
        "icon": "🍰",
        "description": "Chương VI · SGK Toán 6 tập hai (tr. 4–27): Bài 23 – Bài 27. Mở rộng khái niệm phân số, phân số bằng nhau; so sánh phân số, hỗn số dương; phép cộng, trừ, nhân, chia phân số; hai bài toán về phân số.",
        "requirements": [
            "Nhận biết được phân số với tử số hoặc mẫu số là số nguyên âm; khái niệm hai phân số bằng nhau và quy tắc bằng nhau của hai phân số.",
            "Nêu được hai tính chất cơ bản của phân số; so sánh được hai phân số; nhận biết được số đối của một phân số, hỗn số dương.",
            "Thực hiện được các phép tính cộng, trừ, nhân, chia với phân số; vận dụng tính chất giao hoán, kết hợp, phân phối và quy tắc dấu ngoặc.",
            "Tính được giá trị phân số của một số cho trước và tính được một số biết giá trị phân số của số đó.",
            "Giải quyết được vấn đề thực tiễn gắn với các phép tính về phân số.",
        ],
        "definition": (
            "- **Phân số** a/b với a, b ∈ ℤ, b ≠ 0. Mọi số nguyên n viết được dưới dạng n/1.\n"
            "- **Hai phân số bằng nhau**: a/b = c/d ⇔ a · d = b · c.\n"
            "- **Tính chất cơ bản**: a/b = (a · m)/(b · m) (m ∈ ℤ, m ≠ 0); a/b = (a : n)/(b : n) (n ∈ ƯC(a, b)). Mọi phân số đưa được về mẫu dương.\n"
            "- **Số đối** của a/b là −a/b; **số nghịch đảo** của a/b (a ≠ 0) là b/a.\n"
            "- **Hỗn số dương** a b/c = a + b/c."
        ),
        "theory": (
            "### Bài 23. Mở rộng khái niệm phân số. Phân số bằng nhau\n- −3/4 = 6/(−8) vì (−3) · (−8) = 4 · 6 = 24.\n"
            "### Bài 24. So sánh phân số. Hỗn số dương\n- Đưa về cùng mẫu dương rồi so sánh tử: −2/3 = −8/12 > −9/12 = −3/4.\n- 2 1/3 = 7/3.\n"
            "### Luyện tập chung\n"
            "### Bài 25. Phép cộng và phép trừ phân số\n- −1/2 + 2/3 = −3/6 + 4/6 = 1/6; 1/4 − 5/6 = 3/12 − 10/12 = −7/12.\n"
            "### Bài 26. Phép nhân và phép chia phân số\n- (−2/5) · (15/4) = −30/20 = −3/2; 3/4 : (−9/8) = 3/4 · (−8/9) = −2/3.\n"
            "### Bài 27. Hai bài toán về phân số\n- Giá trị m/n của số a: a · m/n. Tìm một số biết m/n của nó bằng b: b : m/n.\n"
            "### Luyện tập chung · Bài tập cuối chương VI"
        ),
        "formulas": [
            G("I. Phân số bằng nhau – so sánh", F("Bằng nhau", "a/b = c/d ⇔ a·d = b·c"), F("So sánh", "Quy đồng về cùng mẫu dương, so sánh tử"),
              F("Dấu", "a/(−b) = −a/b")),
            G("II. Phép tính", F("Cộng (cùng mẫu)", "a/m + b/m = (a + b)/m"), F("Trừ", "a/b − c/d = a/b + (−c/d)"),
              F("Nhân", "a/b · c/d = (a·c)/(b·d)"), F("Chia", "a/b : c/d = a/b · d/c (c ≠ 0)")),
            G("III. Hai bài toán", F("Giá trị phân số của một số", "m/n của a = a · m/n"), F("Tìm một số biết m/n của nó bằng b", "Số đó = b : m/n")),
        ],
        "example": "Một lớp có 40 học sinh, 3/8 số học sinh đạt loại giỏi. Tính số học sinh giỏi. Nếu số học sinh giỏi của lớp khác là 12 em và bằng 2/5 số học sinh lớp đó thì lớp đó có bao nhiêu em?",
        "example_answer": "Số HS giỏi: 40 · 3/8 = **15** em. Lớp kia: 12 : 2/5 = 12 · 5/2 = **30** em.",
        "real_life": "- Chia phần tài sản, tính phần công việc đã làm, phần trăm giảm giá dưới dạng phân số; công thức nấu ăn.",
        "quiz": [
            mcq("biet", "Phân số nào bằng −2/5?", ["2/(−5)", "2/5", "−5/2", "5/(−2)"], 0, "2/(−5) = −2/5 (đưa dấu “−” lên tử)."),
            mcq("biet", "Số nghịch đảo của −3/7 là:", ["3/7", "−7/3", "7/3", "−3/7"], 1, "Đổi chỗ tử và mẫu, giữ dấu: **−7/3**."),
            mcq("biet", "Hỗn số 3 1/4 viết dưới dạng phân số là:", ["13/4", "7/4", "4/13", "31/4"], 0, "3 1/4 = (3 · 4 + 1)/4 = **13/4**."),
            mcq("biet", "Tìm x biết x/12 = 3/4:", ["9", "16", "4", "36"], 0, "x · 4 = 12 · 3 ⇒ x = 36 : 4 = **9**."),
            mcq("hieu", "−1/2 + 2/3 = ?", ["1/6", "1/5", "−1/6", "3/5"], 0, "−3/6 + 4/6 = **1/6**."),
            mcq("hieu", "3/4 : (−9/8) = ?", ["−2/3", "−27/32", "2/3", "−3/2"], 0, "3/4 · (−8/9) = −24/36 = **−2/3**.", note="Phép chia: nhân với số nghịch đảo của số chia."),
            tf4("hieu", "Mỗi khẳng định sau đúng hay sai?",
                ["a) −3/4 = 6/(−8)", "b) −2/3 < −3/4", "c) 1/4 − 5/6 = −7/12", "d) (−2/5) · (15/4) = −3/2"],
                [True, False, True, True],
                "a) (−3)·(−8) = 24 = 4·6 → Đúng.\nb) −2/3 = −8/12, −3/4 = −9/12; −8 > −9 nên −2/3 > −3/4 → Sai.\nc) 3/12 − 10/12 = −7/12 → Đúng.\nd) −30/20 = −3/2 → Đúng."),
            tf4("hieu", "Lớp 6A có 40 học sinh, trong đó 3/8 số học sinh xếp loại giỏi, 1/2 số học sinh xếp loại khá, còn lại là trung bình. Mỗi khẳng định sau đúng hay sai?",
                ["a) Lớp có 15 học sinh giỏi", "b) Lớp có 20 học sinh khá", "c) Lớp có 4 học sinh trung bình", "d) Số học sinh trung bình chiếm 1/5 số học sinh cả lớp"],
                [True, True, False, False],
                "a) 40 · 3/8 = 15 → Đúng. b) 40 · 1/2 = 20 → Đúng.\nc) 40 − 15 − 20 = 5 học sinh → Sai.\nd) 5/40 = 1/8, không phải 1/5 → Sai."),
            mcq("vandung", "Một người đi hết quãng đường trong 3 ngày: ngày đầu đi 1/3 quãng đường, ngày thứ hai đi 2/5 quãng đường, ngày thứ ba đi 12 km còn lại. Quãng đường dài:", ["45 km", "36 km", "60 km", "30 km"], 0,
                "Phần còn lại: 1 − 1/3 − 2/5 = 15/15 − 5/15 − 6/15 = 4/15 quãng đường ứng với 12 km.\nQuãng đường: 12 : 4/15 = 12 · 15/4 = **45 km**."),
            short("vandung", "Tìm một số, biết 3/5 của số đó bằng 24.", ["40"],
                  "Số đó = 24 : 3/5 = 24 · 5/3 = **40**."),
        ],
    },
    # ===================== CHƯƠNG VII =====================
    {
        "topic": "l6-ch07-so-thap-phan",
        "title": "Số thập phân",
        "icon": "🔟",
        "description": "Chương VII · SGK Toán 6 tập hai (tr. 28–42): Bài 28 – Bài 31. Số thập phân (kể cả số âm); tính toán với số thập phân; làm tròn và ước lượng; một số bài toán về tỉ số và tỉ số phần trăm.",
        "requirements": [
            "Nhận biết được số thập phân âm, số đối của một số thập phân; so sánh được hai số thập phân.",
            "Thực hiện được các phép tính cộng, trừ, nhân, chia với số thập phân; vận dụng tính chất phép tính để tính hợp lí.",
            "Thực hiện được ước lượng và làm tròn số thập phân.",
            "Tính được tỉ số và tỉ số phần trăm của hai đại lượng; tính được giá trị phần trăm của một số cho trước và tìm một số biết giá trị phần trăm của số đó.",
            "Giải quyết được vấn đề thực tiễn gắn với số thập phân, tỉ số và tỉ số phần trăm (lãi suất, giảm giá, …).",
        ],
        "definition": (
            "- Phân số thập phân (mẫu là luỹ thừa của 10) viết được dưới dạng **số thập phân**: −3/10 = −0,3; −125/100 = −1,25.\n"
            "- **Số đối** của 2,7 là −2,7. **So sánh**: số âm < 0 < số dương; với hai số âm, số nào có số đối lớn hơn thì nhỏ hơn (−1,3 < −1,25 vì 1,3 > 1,25).\n"
            "- **Tỉ số** của a và b (b ≠ 0) là a : b; **tỉ số phần trăm** là (a : b) · 100%.\n"
            "- **Làm tròn**: chữ số bỏ đi đầu tiên ≥ 5 thì cộng 1 vào chữ số giữ lại cuối cùng; < 5 thì giữ nguyên."
        ),
        "theory": (
            "### Bài 28. Số thập phân\n- −3/4 = −0,75; −1,3 < −1,25 < 0 < 0,5.\n"
            "### Bài 29. Tính toán với số thập phân\n- Cộng, trừ, nhân, chia số thập phân âm theo quy tắc dấu như số nguyên: (−3,5) + 1,2 = −2,3; (−1,5) · (−0,4) = 0,6; 4,8 : (−1,2) = −4.\n"
            "### Bài 30. Làm tròn và ước lượng\n- 3,14159 làm tròn đến hàng phần trăm: 3,14; ước lượng 19,8 · 5,1 ≈ 20 · 5 = 100.\n"
            "### Bài 31. Một số bài toán về tỉ số và tỉ số phần trăm\n- m% của a = a · m/100; tìm một số biết m% của nó là b: b : (m/100).\n"
            "### Luyện tập chung · Bài tập cuối chương VII"
        ),
        "formulas": [
            G("I. Tỉ số – phần trăm", F("Tỉ số phần trăm của a và b", "(a : b) · 100%"), F("Giá trị m% của a", "a · m/100"),
              F("Tìm số biết m% của nó là b", "b : (m/100) = b · 100/m")),
            G("II. Tính toán", F("Quy tắc dấu", "Như số nguyên: (−)·(−) = (+), (−)·(+) = (−)"),
              F("Giảm giá m%", "Giá mới = Giá cũ · (100 − m)%"), F("Lãi suất r%/năm", "Sau 1 năm: T = A · (100 + r)%")),
        ],
        "example": "Một chiếc áo giá 400 000 đồng được giảm 15%. Tính số tiền được giảm và giá bán mới.",
        "example_answer": "Số tiền giảm: 400 000 · 15/100 = **60 000 đồng**. Giá mới: 400 000 − 60 000 = **340 000 đồng** (bằng 85% giá cũ).",
        "real_life": "- Giá cả, khuyến mãi, lãi suất ngân hàng; nhiệt độ âm có phần thập phân (−2,5 °C); ước lượng chi tiêu.",
        "quiz": [
            mcq("biet", "Phân số −3/4 viết dưới dạng số thập phân là:", ["−0,34", "−0,75", "−7,5", "0,75"], 1, "−3/4 = −75/100 = **−0,75**."),
            mcq("biet", "Số đối của −2,7 là:", ["2,7", "−2,7", "0,27", "−7,2"], 0, "Số đối của −2,7 là **2,7**."),
            mcq("biet", "Làm tròn 12,467 đến hàng phần mười được:", ["12,4", "12,5", "12,47", "13"], 1, "Chữ số bỏ đi đầu tiên là 6 ≥ 5 → **12,5**."),
            mcq("biet", "Tỉ số phần trăm của 3 và 4 là:", ["34%", "75%", "133%", "0,75%"], 1, "3 : 4 = 0,75 = **75%**."),
            mcq("hieu", "(−2,5) · 4 + 1,5 = ?", ["−8,5", "−11,5", "8,5", "−4"], 0, "(−2,5) · 4 = −10; −10 + 1,5 = **−8,5**."),
            mcq("hieu", "Sắp xếp theo thứ tự tăng dần:", ["−1,3; −1,25; 0,5; 1,05", "−1,25; −1,3; 0,5; 1,05", "−1,3; −1,25; 1,05; 0,5", "0,5; 1,05; −1,25; −1,3"], 0,
                "−1,3 < −1,25 (vì 1,3 > 1,25) < 0,5 < 1,05."),
            tf4("hieu", "Mỗi khẳng định sau đúng hay sai?",
                ["a) −1,25 > −1,3", "b) (−1,5) · (−0,4) = −0,6", "c) 4,8 : (−1,2) = −4", "d) Làm tròn 7,449 đến hàng phần mười được 7,5"],
                [True, False, True, False],
                "a) 1,25 < 1,3 nên −1,25 > −1,3 → Đúng.\nb) Cùng dấu → dương: 0,6 → Sai.\nc) Khác dấu → âm: −4 → Đúng.\nd) Chữ số bỏ đi đầu tiên là 4 < 5 → 7,4 → Sai (không làm tròn “dây chuyền”)."),
            tf4("hieu", "Một chiếc áo giá 400 000 đồng được giảm giá 15%. Mỗi khẳng định sau đúng hay sai?",
                ["a) Số tiền được giảm là 60 000 đồng", "b) Giá sau khi giảm là 340 000 đồng", "c) Giá sau khi giảm bằng 85% giá ban đầu", "d) Nếu giảm tiếp 10% trên giá mới thì tổng cộng giá áo đã giảm 25%"],
                [True, True, True, False],
                "a) 400 000 · 15% = 60 000 → Đúng. b) 400 000 − 60 000 = 340 000 → Đúng. c) 100% − 15% = 85% → Đúng.\nd) Giá cuối: 340 000 · 90% = 306 000 = 76,5% giá ban đầu ⇒ giảm 23,5%, không phải 25% → Sai."),
            mcq("vandung", "Bác An gửi tiết kiệm 50 000 000 đồng với lãi suất 6%/năm. Sau 1 năm, bác nhận được cả gốc và lãi là:", ["53 000 000 đồng", "56 000 000 đồng", "3 000 000 đồng", "50 300 000 đồng"], 0,
                "Lãi: 50 000 000 · 6/100 = 3 000 000. Tổng: **53 000 000 đồng**."),
            short("vandung", "Lớp 6B có 45 học sinh, trong đó 40% là học sinh nữ. Lớp có bao nhiêu học sinh nữ?", ["18"],
                  "45 · 40/100 = **18** học sinh nữ.", unit="học sinh"),
        ],
    },
]

LESSONS += [
    # ===================== CHƯƠNG VIII =====================
    {
        "topic": "l6-ch08-hinh-hoc-co-ban",
        "title": "Những hình hình học cơ bản",
        "icon": "📐",
        "description": "Chương VIII · SGK Toán 6 tập hai (tr. 43–67): Bài 32 – Bài 37. Điểm và đường thẳng; điểm nằm giữa hai điểm, tia; đoạn thẳng, độ dài đoạn thẳng; trung điểm của đoạn thẳng; góc; số đo góc.",
        "requirements": [
            "Nhận biết được những quan hệ cơ bản giữa điểm, đường thẳng: điểm thuộc/không thuộc đường thẳng; ba điểm thẳng hàng, không thẳng hàng; tiên đề về đường thẳng đi qua hai điểm phân biệt.",
            "Nhận biết được khái niệm hai đường thẳng cắt nhau, song song; điểm nằm giữa hai điểm; tia, hai tia đối nhau, hai tia trùng nhau.",
            "Nhận biết được khái niệm đoạn thẳng, trung điểm của đoạn thẳng, độ dài đoạn thẳng.",
            "Nhận biết được khái niệm góc, điểm trong của góc; các góc đặc biệt (vuông, nhọn, tù, bẹt); khái niệm số đo góc.",
            "Giải quyết được vấn đề thực tiễn gắn với đo độ dài, trung điểm và số đo góc.",
        ],
        "definition": (
            "- **Điểm** kí hiệu bằng chữ in hoa (A, B, …); **đường thẳng** kí hiệu chữ thường (a, d, …). A ∈ d: điểm A thuộc đường thẳng d.\n"
            "- Có một và chỉ một đường thẳng đi qua hai điểm phân biệt A, B.\n"
            "- Ba điểm cùng thuộc một đường thẳng là **ba điểm thẳng hàng**; trong ba điểm thẳng hàng có **đúng một điểm nằm giữa** hai điểm còn lại.\n"
            "- **Tia** gốc O là hình gồm điểm O và một phần đường thẳng bị chia ra bởi O. Hai tia chung gốc tạo thành đường thẳng là **hai tia đối nhau**.\n"
            "- **Đoạn thẳng** AB gồm A, B và các điểm nằm giữa A, B. **Trung điểm** M của AB: M nằm giữa A, B và MA = MB = AB/2.\n"
            "- **Góc** là hình gồm hai tia chung gốc; số đo góc tính bằng độ (°). Góc vuông = 90°; nhọn: 0° < α < 90°; tù: 90° < α < 180°; bẹt = 180°."
        ),
        "theory": (
            "### Bài 32. Điểm và đường thẳng\n- Điểm thuộc / không thuộc đường thẳng; ba điểm thẳng hàng; hai đường thẳng cắt nhau (có 1 điểm chung), song song (không có điểm chung), trùng nhau.\n"
            "### Bài 33. Điểm nằm giữa hai điểm. Tia\n- Tia Ox; hai tia đối nhau Ox, Oy (tạo thành đường thẳng xy); hai tia trùng nhau.\n"
            "### Bài 34. Đoạn thẳng. Độ dài đoạn thẳng\n- Nếu M nằm giữa A và B thì **AM + MB = AB**. Trên tia Ox, nếu OA < OB thì A nằm giữa O và B.\n"
            "### Bài 35. Trung điểm của đoạn thẳng\n- M là trung điểm AB ⇔ M nằm giữa A, B và MA = MB ⇒ MA = MB = AB : 2.\n"
            "### Luyện tập chung\n"
            "### Bài 36. Góc\n- Góc xOy (đỉnh O, cạnh Ox, Oy), kí hiệu ∠xOy; điểm trong của góc.\n"
            "### Bài 37. Số đo góc\n- Đo góc bằng thước đo góc; so sánh hai góc theo số đo; góc vuông, nhọn, tù, bẹt.\n"
            "### Luyện tập chung · Bài tập cuối chương VIII"
        ),
        "formulas": [
            G("I. Đoạn thẳng", F("Cộng độ dài", "M nằm giữa A và B ⇒ AM + MB = AB"),
              F("Trung điểm", "M là trung điểm AB ⇒ MA = MB = AB/2"),
              F("Trên tia Ox", "OA < OB ⇒ A nằm giữa O, B và AB = OB − OA")),
            G("II. Góc", F("Góc vuông", "90°"), F("Góc nhọn", "0° < α < 90°"), F("Góc tù", "90° < α < 180°"), F("Góc bẹt", "180° (hai cạnh là hai tia đối nhau)"),
              F("Góc giữa hai kim đồng hồ", "Mỗi “số” trên mặt đồng hồ ứng với 360° : 12 = 30°")),
            G("III. Đếm đường thẳng", F("n điểm, không có 3 điểm nào thẳng hàng", "Số đường thẳng = n(n − 1)/2")),
        ],
        "example": "Cho đoạn thẳng AB = 12 cm. Gọi C là trung điểm của AB, D là trung điểm của AC. Tính DB.",
        "example_answer": "AC = CB = 12 : 2 = 6 cm; DC = AC : 2 = 3 cm. D nằm giữa A và C nên D nằm giữa A, B và DB = DC + CB = 3 + 6 = **9 cm**.",
        "real_life": "- Căng dây để trồng cây thẳng hàng; chia đôi thanh gỗ (trung điểm); đọc góc giữa hai kim đồng hồ; góc mở cánh cửa, góc nghiêng mái nhà.",
        "quiz": [
            mcq("biet", "Qua hai điểm phân biệt A và B có bao nhiêu đường thẳng?", ["0", "1", "2", "Vô số"], 1,
                "Có **một và chỉ một** đường thẳng đi qua hai điểm phân biệt."),
            mcq("biet", "Góc bẹt có số đo bằng:", ["90°", "100°", "180°", "360°"], 2, "Góc bẹt có hai cạnh là hai tia đối nhau, số đo **180°**."),
            mcq("biet", "M là trung điểm của đoạn thẳng AB dài 10 cm. Độ dài MA là:", ["10 cm", "20 cm", "5 cm", "2,5 cm"], 2, "MA = AB : 2 = 10 : 2 = **5 cm**."),
            mcq("biet", "Hai tia Ox và Oy chung gốc O tạo thành đường thẳng xy được gọi là:", ["Hai tia trùng nhau", "Hai tia đối nhau", "Hai tia song song", "Hai đoạn thẳng"], 1,
                "Hai tia chung gốc tạo thành một đường thẳng là **hai tia đối nhau**."),
            mcq("hieu", "Điểm M nằm giữa A và B, biết AM = 3 cm, AB = 8 cm. Độ dài MB là:", ["11 cm", "5 cm", "4 cm", "3 cm"], 1,
                "AM + MB = AB ⇒ MB = 8 − 3 = **5 cm**."),
            mcq("hieu", "Cho 4 điểm, không có ba điểm nào thẳng hàng. Kẻ các đường thẳng đi qua từng cặp điểm. Số đường thẳng là:", ["4", "6", "8", "12"], 1,
                "Mỗi điểm nối với 3 điểm còn lại: 4 · 3 = 12, mỗi đường được đếm 2 lần ⇒ 12 : 2 = **6**.", note="Công thức n(n − 1)/2."),
            tf4("hieu", "Mỗi khẳng định sau đúng hay sai?",
                ["a) Góc có hai cạnh là hai tia đối nhau là góc bẹt", "b) Góc có số đo 95° là góc nhọn",
                 "c) Nếu MA = MB thì M là trung điểm của đoạn thẳng AB", "d) Trong ba điểm thẳng hàng có đúng một điểm nằm giữa hai điểm còn lại"],
                [True, False, False, True],
                "a) Đúng theo định nghĩa góc bẹt.\nb) 90° < 95° < 180° ⇒ góc tù → Sai.\nc) Còn cần M nằm giữa A, B (M có thể không thuộc AB) → Sai.\nd) Đúng (tính chất ba điểm thẳng hàng)."),
            tf4("hieu", "Trên tia Ox lấy hai điểm A, B sao cho OA = 3 cm, OB = 7 cm. Gọi M là trung điểm của AB. Mỗi khẳng định sau đúng hay sai?",
                ["a) Điểm A nằm giữa hai điểm O và B", "b) AB = 4 cm", "c) OM = 5 cm", "d) OA > AB"],
                [True, True, True, False],
                "a) A, B cùng thuộc tia Ox và OA < OB ⇒ A nằm giữa O và B → Đúng.\nb) AB = OB − OA = 7 − 3 = 4 cm → Đúng.\nc) AM = 4 : 2 = 2 cm; OM = OA + AM = 3 + 2 = 5 cm → Đúng.\nd) OA = 3 cm < AB = 4 cm → Sai."),
            mcq("vandung", "Cho đoạn thẳng AB = 12 cm. C là trung điểm của AB, D là trung điểm của AC. Độ dài DB là:", ["6 cm", "3 cm", "9 cm", "4,5 cm"], 2,
                "AC = CB = 6 cm; DC = 3 cm; DB = DC + CB = 3 + 6 = **9 cm**."),
            short("vandung", "Lúc 5 giờ đúng, góc tạo bởi kim giờ và kim phút (góc không lớn hơn 180°) có số đo bao nhiêu độ?", ["150", "150°"],
                  "Kim phút chỉ số 12, kim giờ chỉ số 5: cách nhau 5 khoảng, mỗi khoảng 30° ⇒ 5 · 30° = **150°**.", unit="°"),
        ],
    },
    # ===================== CHƯƠNG IX =====================
    {
        "topic": "l6-ch09-du-lieu-xac-suat-thuc-nghiem",
        "title": "Dữ liệu và xác suất thực nghiệm",
        "icon": "📊",
        "description": "Chương IX · SGK Toán 6 tập hai (tr. 68–98): Bài 38 – Bài 43. Dữ liệu và thu thập dữ liệu; bảng thống kê và biểu đồ tranh; biểu đồ cột; biểu đồ cột kép; kết quả có thể và sự kiện trong trò chơi, thí nghiệm; xác suất thực nghiệm.",
        "requirements": [
            "Thực hiện được việc thu thập, phân loại dữ liệu theo các tiêu chí cho trước; nhận biết được tính hợp lí của dữ liệu.",
            "Đọc và mô tả được dữ liệu ở dạng bảng thống kê, biểu đồ tranh, biểu đồ cột, biểu đồ cột kép; lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp.",
            "Phát hiện được vấn đề hoặc quy luật đơn giản dựa trên phân tích số liệu thu được.",
            "Làm quen với mô hình xác suất trong một số trò chơi, thí nghiệm đơn giản (tung đồng xu, gieo xúc xắc, lấy vật từ hộp).",
            "Làm quen với việc mô tả xác suất (thực nghiệm) của khả năng xảy ra nhiều lần của một sự kiện.",
        ],
        "definition": (
            "- **Dữ liệu** gồm dữ liệu là số (số liệu) và dữ liệu không phải là số (màu sắc, tên, …). Thu thập bằng quan sát, lập phiếu hỏi, làm thí nghiệm, tìm trên Internet.\n"
            "- **Bảng thống kê**, **biểu đồ tranh**, **biểu đồ cột**, **biểu đồ cột kép** (so sánh hai bộ dữ liệu cùng loại).\n"
            "- **Kết quả có thể**: tung đồng xu có 2 kết quả {S; N}; gieo xúc xắc có 6 kết quả {1; 2; 3; 4; 5; 6}.\n"
            "- **Sự kiện** có thể xảy ra hoặc không xảy ra tuỳ kết quả của trò chơi/thí nghiệm.\n"
            "- **Xác suất thực nghiệm** của sự kiện A = (Số lần A xảy ra) : (Tổng số lần thực hiện)."
        ),
        "theory": (
            "### Bài 38. Dữ liệu và thu thập dữ liệu\n- Phân loại dữ liệu; kiểm tra tính hợp lí (ví dụ: chiều cao 15 m của học sinh là không hợp lí).\n"
            "### Bài 39. Bảng thống kê và biểu đồ tranh\n- Mỗi biểu tượng ứng với một số lượng nhất định (ví dụ 1 ⭐ = 10 học sinh).\n"
            "### Bài 40. Biểu đồ cột\n- Trục ngang ghi đối tượng, trục đứng ghi số lượng; độ cao cột biểu diễn số liệu.\n"
            "### Bài 41. Biểu đồ cột kép\n- Hai cột đặt cạnh nhau cho mỗi đối tượng, có chú giải màu; dùng để so sánh hai bộ dữ liệu.\n"
            "### Luyện tập chung\n"
            "### Bài 42. Kết quả có thể và sự kiện trong trò chơi, thí nghiệm\n- Liệt kê các kết quả có thể; xác định sự kiện xảy ra hay không.\n"
            "### Bài 43. Xác suất thực nghiệm\n- Tung đồng xu 40 lần, 18 lần ngửa ⇒ xác suất thực nghiệm xuất hiện mặt N là 18/40 = 9/20.\n"
            "### Luyện tập chung · Bài tập cuối chương IX"
        ),
        "formulas": [
            G("I. Xác suất thực nghiệm", F("Xác suất thực nghiệm của sự kiện A", "Số lần A xảy ra : Tổng số lần thực hiện"),
              F("Sự kiện “không A”", "Số lần không xảy ra A = Tổng số lần − Số lần A xảy ra")),
            G("II. Kết quả có thể", F("Tung 1 đồng xu", "{S; N} – 2 kết quả"), F("Gieo 1 xúc xắc", "{1; 2; 3; 4; 5; 6} – 6 kết quả")),
            G("III. Đọc biểu đồ", F("Tỉ lệ của một nhóm", "Số liệu của nhóm : Tổng số liệu"), F("Chênh lệch", "Hiệu hai số liệu tương ứng")),
        ],
        "example": "Bình tung một đồng xu 40 lần, có 18 lần xuất hiện mặt ngửa. Tính xác suất thực nghiệm xuất hiện mặt ngửa và mặt sấp.",
        "example_answer": "Mặt ngửa: 18/40 = **9/20**. Mặt sấp xuất hiện 40 − 18 = 22 lần: 22/40 = **11/20**.",
        "real_life": "- Điều tra món ăn yêu thích của lớp; đọc biểu đồ lượng mưa, dân số; dự đoán khả năng trúng đích, khả năng trời mưa từ dữ liệu đã có.",
        "quiz": [
            mcq("biet", "Dữ liệu nào sau đây **không phải** là số?", ["Chiều cao của các bạn trong lớp", "Màu sắc yêu thích của các bạn", "Số anh chị em của mỗi bạn", "Điểm kiểm tra môn Toán"], 1,
                "Màu sắc là dữ liệu **không phải là số**."),
            mcq("biet", "Tung một đồng xu, tập hợp các kết quả có thể là:", ["{S}", "{N}", "{S; N}", "{1; 2}"], 2, "Đồng xu có hai mặt: sấp (S) và ngửa (N) ⇒ **{S; N}**."),
            mcq("biet", "Gieo một con xúc xắc 6 mặt, số kết quả có thể là:", ["2", "4", "6", "12"], 2, "Các kết quả: 1, 2, 3, 4, 5, 6 ⇒ **6** kết quả."),
            mcq("biet", "Để so sánh số học sinh nam và nữ của từng lớp trong khối 6, nên dùng:", ["Biểu đồ tranh", "Biểu đồ cột kép", "Bảng ghi tên học sinh", "Hình vẽ đoạn thẳng"], 1,
                "So sánh **hai bộ dữ liệu cùng loại** (nam, nữ) ⇒ **biểu đồ cột kép**."),
            mcq("hieu", "Tung một đồng xu 40 lần, có 18 lần xuất hiện mặt ngửa. Xác suất thực nghiệm xuất hiện mặt ngửa là:", ["18/22", "9/20", "11/20", "18"], 1,
                "18/40 = **9/20**."),
            mcq("hieu", "Gieo một con xúc xắc. Sự kiện “Số chấm xuất hiện là số chẵn” xảy ra khi kết quả là:", ["1; 3; 5", "2; 4; 6", "2; 3; 5", "4; 5; 6"], 1,
                "Các số chẵn trong {1;…;6} là **2; 4; 6**."),
            tf4("hieu", "Biểu đồ cột cho biết số học sinh lớp 6A thích các môn: Toán 12, Ngữ văn 8, Tiếng Anh 10, Tin học 15 (mỗi bạn chọn một môn). Mỗi khẳng định sau đúng hay sai?",
                ["a) Môn Tin học được yêu thích nhiều nhất", "b) Lớp 6A có 45 học sinh tham gia khảo sát",
                 "c) Số bạn thích Toán nhiều hơn số bạn thích Ngữ văn là 2 bạn", "d) Số bạn thích Tiếng Anh chiếm 2/9 số học sinh tham gia"],
                [True, True, False, True],
                "a) 15 là số lớn nhất → Đúng.\nb) 12 + 8 + 10 + 15 = 45 → Đúng.\nc) 12 − 8 = 4 bạn → Sai.\nd) 10/45 = 2/9 → Đúng."),
            tf4("hieu", "Gieo một con xúc xắc 50 lần: mặt 6 chấm xuất hiện 9 lần; mặt có số chấm chẵn xuất hiện 26 lần. Mỗi khẳng định sau đúng hay sai?",
                ["a) Xác suất thực nghiệm xuất hiện mặt 6 chấm là 9/50", "b) Xác suất thực nghiệm xuất hiện mặt có số chấm lẻ là 12/25",
                 "c) Sự kiện “Số chấm xuất hiện lớn hơn hoặc bằng 7” có thể xảy ra", "d) Xác suất thực nghiệm xuất hiện mặt chẵn là 26%"],
                [True, True, False, False],
                "a) 9/50 → Đúng.\nb) Mặt lẻ: 50 − 26 = 24 lần ⇒ 24/50 = 12/25 → Đúng.\nc) Xúc xắc chỉ có từ 1 đến 6 chấm ⇒ không thể xảy ra → Sai.\nd) 26/50 = 52% → Sai."),
            mcq("vandung", "Một xạ thủ bắn 60 viên đạn, có 51 viên trúng đích. Xác suất thực nghiệm bắn trúng đích là:", ["51%", "85%", "15%", "9/60"], 1,
                "51/60 = 0,85 = **85%**."),
            short("vandung", "Một hộp có bóng đỏ và bóng xanh. Lấy ngẫu nhiên một quả rồi trả lại, lặp lại 80 lần, thấy 28 lần lấy được bóng đỏ. Xác suất thực nghiệm của sự kiện “Không lấy được bóng đỏ” là bao nhiêu? (viết dạng phân số tối giản)",
                  ["13/20", "0,65"],
                  "Số lần không lấy được bóng đỏ: 80 − 28 = 52. Xác suất thực nghiệm: 52/80 = **13/20** (= 0,65)."),
        ],
    },
]
