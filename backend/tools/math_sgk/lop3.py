"""TOÁN 3 — Kết nối tri thức với cuộc sống (tập một, tập hai).

16 chủ đề đánh số trong SGK, đúng thứ tự mục lục.
Mỗi chủ đề: Yêu cầu cần đạt (CT GDPT 2018), kiến thức theo từng bài, công thức/quy tắc,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf

GRADE = 3

LESSONS = [
    # ===================== CHỦ ĐỀ 1 =====================
    {
        "topic": "l3-cd01-on-tap-va-bo-sung",
        "title": "Ôn tập và bổ sung",
        "icon": "🔁",
        "description": "Chủ đề 1 · SGK Toán 3 tập một (tr. 6–27): Bài 1 – Bài 8. Ôn các số đến 1000, cộng trừ trong phạm vi 1000, tìm thành phần phép cộng – trừ, bảng nhân chia 2, 3, 4, 5, ôn hình học và đo lường.",
        "requirements": [
            "Đọc, viết, so sánh, cấu tạo các số trong phạm vi 1000.",
            "Thực hiện được phép cộng, phép trừ trong phạm vi 1000; tìm được thành phần chưa biết của phép cộng, phép trừ.",
            "Vận dụng được bảng nhân 2, 3, 4, 5 và bảng chia 2, 3, 4, 5 trong thực hành tính.",
            "Ôn tập đường gấp khúc, hình tứ giác, khối hình; các đơn vị đo đã học (cm, dm, m, km, kg, l).",
        ],
        "definition": (
            "- **Tìm số hạng**: Số hạng = Tổng − Số hạng kia.\n"
            "- **Tìm số bị trừ**: Số bị trừ = Hiệu + Số trừ. **Tìm số trừ**: Số trừ = Số bị trừ − Hiệu.\n"
            "- **Bảng nhân 3**: 3 × 1 = 3, …, 3 × 10 = 30; **bảng nhân 4**: 4 × 1 = 4, …, 4 × 10 = 40. Bảng chia lập từ bảng nhân tương ứng."
        ),
        "theory": (
            "### Bài 1. Ôn tập các số đến 1 000\n"
            "- 685 = 600 + 80 + 5; so sánh từ hàng trăm.\n"
            "### Bài 2. Ôn tập phép cộng, phép trừ trong phạm vi 1 000\n"
            "- Đặt tính thẳng cột, tính từ phải sang trái, nhớ khi cần.\n"
            "### Bài 3. Tìm thành phần trong phép cộng, phép trừ\n"
            "- ? + 35 = 82 → 82 − 35 = 47; ? − 26 = 54 → 54 + 26 = 80; 90 − ? = 37 → 90 − 37 = 53.\n"
            "### Bài 4. Ôn tập bảng nhân 2; 5, bảng chia 2; 5\n"
            "### Bài 5. Bảng nhân 3, bảng chia 3\n"
            "- 3 × 7 = 21 → 21 : 3 = 7.\n"
            "### Bài 6. Bảng nhân 4, bảng chia 4\n"
            "- 4 × 6 = 24 → 24 : 4 = 6.\n"
            "### Bài 7. Ôn tập hình học và đo lường\n"
            "- Đường gấp khúc, hình tứ giác; 1 m = 100 cm; 1 km = 1000 m.\n"
            "### Bài 8. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tìm thành phần phép cộng, trừ", F("Số hạng", "Số hạng = Tổng − Số hạng kia"),
              F("Số bị trừ", "Số bị trừ = Hiệu + Số trừ"),
              F("Số trừ", "Số trừ = Số bị trừ − Hiệu")),
            G("II. Bảng nhân – chia", F("Bảng 3", "3 × 1 = 3 … 3 × 10 = 30 · 30 : 3 = 10"),
              F("Bảng 4", "4 × 1 = 4 … 4 × 10 = 40 · 40 : 4 = 10")),
        ],
        "example": "Tìm số trừ: 85 − ? = 39.",
        "example_answer": "Số trừ = Số bị trừ − Hiệu = 85 − 39 = **46**. Thử lại: 85 − 46 = 39 ✔.",
        "real_life": "- Biết tổng số bạn và số bạn nam, tìm số bạn nữ.\n- Chia đều 24 cái bánh vào 4 hộp.",
        "quiz": [
            mcq("biet", "3 × 8 = ?", ["24", "21", "27", "11"], 0, "Bảng nhân 3: 3 × 8 = **24**."),
            mcq("biet", "28 : 4 = ?", ["6", "7", "8", "24"], 1, "Vì 4 × 7 = 28 nên 28 : 4 = **7**."),
            mcq("biet", "Muốn tìm số bị trừ, ta lấy:", ["Hiệu cộng số trừ", "Hiệu trừ số trừ", "Số trừ trừ hiệu", "Tổng trừ số hạng"], 0, "Số bị trừ = **Hiệu + Số trừ**."),
            mcq("biet", "Số 708 gồm:", ["7 trăm, 8 chục", "7 trăm, 0 chục, 8 đơn vị", "70 chục, 8 trăm", "7 chục, 8 đơn vị"], 1, "708 = 700 + 0 + 8 → **7 trăm, 0 chục, 8 đơn vị**."),
            mcq("hieu", "Tìm x biết: x + 47 = 92", ["45", "139", "55", "35"], 0, "Số hạng = 92 − 47 = **45**.", note="Không lấy 92 + 47."),
            mcq("hieu", "Một phép trừ có hiệu là 125, số trừ là 238. Số bị trừ là:", ["113", "363", "353", "263"], 1, "Số bị trừ = 125 + 238 = **363**."),
            tf("hieu", "Nhận định: “4 × 9 = 36.”", True, "Bảng nhân 4: 4 × 9 = 36 → **Đúng**."),
            tf("hieu", "Nhận định: “Trong phép tính 70 − ? = 25, số cần tìm là 95.”", False, "Số trừ = 70 − 25 = 45, không phải 95 → **Sai**.", note="Tìm số trừ phải lấy số bị trừ trừ đi hiệu."),
            mcq("vandung", "Có 27 học sinh xếp đều thành 3 hàng. Mỗi hàng có bao nhiêu học sinh?", ["9", "8", "24", "30"], 0, "27 : 3 = **9** (học sinh)."),
            short("vandung", "Một cửa hàng có 450 kg gạo, sau khi bán còn lại 175 kg. Hỏi cửa hàng đã bán bao nhiêu ki-lô-gam gạo?", ["275"],
                  "Số đã bán = Số ban đầu − Số còn lại = 450 − 175 = 275 (kg).\nĐáp số: **275 kg**.", unit="kg"),
        ],
    },
    # ===================== CHỦ ĐỀ 2 =====================
    {
        "topic": "l3-cd02-bang-nhan-bang-chia",
        "title": "Bảng nhân, bảng chia",
        "icon": "✖️",
        "description": "Chủ đề 2 · SGK Toán 3 tập một (tr. 28–48): Bài 9 – Bài 15. Bảng nhân, bảng chia 6, 7, 8, 9; tìm thành phần trong phép nhân, phép chia; một phần mấy.",
        "requirements": [
            "Vận dụng được các bảng nhân, bảng chia 6, 7, 8, 9 trong thực hành tính.",
            "Xác định được thành phần chưa biết của phép nhân, phép chia (thừa số, số bị chia, số chia).",
            "Nhận biết được 1/2, 1/3, …, 1/9 thông qua hình ảnh trực quan; xác định được một phần mấy của một nhóm đồ vật.",
            "Giải được bài toán thực tế liên quan đến phép nhân, phép chia.",
        ],
        "definition": (
            "- **Tìm thừa số**: Thừa số = Tích : Thừa số kia.\n"
            "- **Tìm số bị chia**: Số bị chia = Thương × Số chia. **Tìm số chia**: Số chia = Số bị chia : Thương.\n"
            "- **Một phần mấy**: chia hình (nhóm đồ vật) thành n phần **bằng nhau**, lấy 1 phần được 1/n. Muốn tìm 1/n của một số, lấy số đó **chia cho n**."
        ),
        "theory": (
            "### Bài 9. Bảng nhân 6, bảng chia 6\n- 6 × 7 = 42 → 42 : 6 = 7.\n"
            "### Bài 10. Bảng nhân 7, bảng chia 7\n- 7 × 8 = 56 → 56 : 7 = 8.\n"
            "### Bài 11. Bảng nhân 8, bảng chia 8\n- 8 × 6 = 48 → 48 : 8 = 6.\n"
            "### Bài 12. Bảng nhân 9, bảng chia 9\n- 9 × 7 = 63 → 63 : 9 = 7.\n"
            "### Bài 13. Tìm thành phần trong phép nhân, phép chia\n"
            "- ? × 6 = 54 → 54 : 6 = 9; ? : 7 = 5 → 5 × 7 = 35; 48 : ? = 8 → 48 : 8 = 6.\n"
            "### Bài 14. Một phần mấy\n- 1/4 của 20 cái kẹo là 20 : 4 = 5 cái.\n"
            "### Bài 15. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tìm thành phần phép nhân, chia", F("Thừa số", "Thừa số = Tích : Thừa số kia"),
              F("Số bị chia", "Số bị chia = Thương × Số chia"),
              F("Số chia", "Số chia = Số bị chia : Thương")),
            G("II. Một phần mấy", F("1/n của một số", "1/n của a = a : n", "1/3 của 18 = 18 : 3 = 6.")),
            G("III. Bảng nhân 6–9 (mẹo)", F("Bảng 9", "9 × n = 10 × n − n", "9 × 7 = 70 − 7 = 63.")),
        ],
        "example": "Tìm số bị chia: ? : 8 = 7.",
        "example_answer": "Số bị chia = Thương × Số chia = 7 × 8 = **56**. Thử lại: 56 : 8 = 7 ✔.",
        "real_life": "- Một tuần có 7 ngày: 4 tuần = 7 × 4 = 28 ngày.\n- Chia đôi (1/2) cái bánh, lấy 1/4 số kẹo.",
        "quiz": [
            mcq("biet", "6 × 7 = ?", ["42", "36", "48", "13"], 0, "Bảng nhân 6: 6 × 7 = **42**."),
            mcq("biet", "56 : 8 = ?", ["6", "7", "8", "9"], 1, "8 × 7 = 56 nên 56 : 8 = **7**."),
            mcq("biet", "9 × 9 = ?", ["18", "72", "81", "99"], 2, "Bảng nhân 9: 9 × 9 = **81**."),
            mcq("biet", "Muốn tìm thừa số chưa biết, ta lấy:", ["Tích nhân thừa số kia", "Tích chia cho thừa số kia", "Tích trừ thừa số kia", "Thừa số kia chia cho tích"], 1, "Thừa số = **Tích : Thừa số kia**."),
            mcq("hieu", "1/6 của 42 l nước là:", ["6 l", "7 l", "36 l", "48 l"], 1, "42 : 6 = **7** (l)."),
            mcq("hieu", "Tìm số chia: 63 : ? = 9", ["7", "8", "54", "72"], 0, "Số chia = 63 : 9 = **7**."),
            tf("hieu", "Nhận định: “8 × 7 = 54.”", False, "8 × 7 = 56 → **Sai**.", note="Nhớ: 7 × 8 = 56, 6 × 9 = 54."),
            tf("hieu", "Nhận định: “Hình được chia thành 5 phần bằng nhau, tô màu 1 phần thì đã tô màu 1/5 hình.”", True, "Chia 5 phần bằng nhau, lấy 1 phần → 1/5 → **Đúng**."),
            mcq("vandung", "Mỗi hộp có 8 cái bánh. Hỏi 6 hộp như thế có bao nhiêu cái bánh?", ["14", "42", "48", "56"], 2, "8 × 6 = **48** (cái bánh)."),
            short("vandung", "Lớp 3A có 35 học sinh, trong đó 1/7 số học sinh là học sinh giỏi Toán. Hỏi lớp có bao nhiêu học sinh giỏi Toán?", ["5"],
                  "1/7 của 35 là 35 : 7 = 5 (học sinh).\nĐáp số: **5 học sinh**.", unit="học sinh"),
        ],
    },
    # ===================== CHỦ ĐỀ 3 =====================
    {
        "topic": "l3-cd03-hinh-phang-hinh-khoi",
        "title": "Làm quen với hình phẳng, hình khối",
        "icon": "📐",
        "description": "Chủ đề 3 · SGK Toán 3 tập một (tr. 49–66): Bài 16 – Bài 22. Điểm ở giữa, trung điểm; hình tròn (tâm, bán kính, đường kính); góc vuông, góc không vuông; tam giác, tứ giác, hình chữ nhật, hình vuông; khối lập phương, khối hộp chữ nhật.",
        "requirements": [
            "Nhận biết được điểm ở giữa, trung điểm của đoạn thẳng.",
            "Nhận biết được tâm, bán kính, đường kính của hình tròn; sử dụng được compa để vẽ đường tròn.",
            "Nhận biết được góc, góc vuông, góc không vuông; dùng ê-ke kiểm tra, vẽ góc vuông.",
            "Nhận biết được tam giác, tứ giác; đỉnh, cạnh, góc của hình chữ nhật, hình vuông; vẽ được hình chữ nhật, hình vuông trên lưới ô vuông.",
            "Nhận biết được đỉnh, cạnh, mặt của khối lập phương, khối hộp chữ nhật.",
        ],
        "definition": (
            "- **Trung điểm** M của đoạn thẳng AB: M nằm giữa A và B và **MA = MB**.\n"
            "- **Hình tròn tâm O**: bán kính OA nối tâm với một điểm trên đường tròn; đường kính đi qua tâm, **đường kính = 2 × bán kính**.\n"
            "- **Góc vuông**: kiểm tra bằng ê-ke. **Hình chữ nhật**: 4 góc vuông, 2 cạnh dài bằng nhau, 2 cạnh ngắn bằng nhau. **Hình vuông**: 4 góc vuông, 4 cạnh bằng nhau.\n"
            "- **Khối lập phương, khối hộp chữ nhật**: đều có **8 đỉnh, 12 cạnh, 6 mặt**; khối lập phương có 6 mặt là hình vuông bằng nhau."
        ),
        "theory": (
            "### Bài 16. Điểm ở giữa, trung điểm của đoạn thẳng\n- Trung điểm chia đoạn thẳng thành hai phần dài bằng nhau.\n"
            "### Bài 17. Hình tròn. Tâm, bán kính, đường kính của hình tròn\n- Mọi bán kính bằng nhau; đường kính gấp đôi bán kính.\n"
            "### Bài 18. Góc, góc vuông, góc không vuông\n- Góc gồm đỉnh và hai cạnh; góc vuông khớp với góc ê-ke.\n"
            "### Bài 19. Hình tam giác, hình tứ giác. Hình chữ nhật, hình vuông\n- Tam giác: 3 đỉnh, 3 cạnh, 3 góc; tứ giác: 4 đỉnh, 4 cạnh, 4 góc.\n"
            "### Bài 20. Thực hành vẽ góc vuông, vẽ đường tròn, hình vuông, hình chữ nhật và vẽ trang trí\n"
            "### Bài 21. Khối lập phương, khối hộp chữ nhật\n"
            "### Bài 22. Luyện tập chung"
        ),
        "formulas": [
            G("I. Đoạn thẳng & hình tròn", F("Trung điểm M của AB", "MA = MB = AB : 2"),
              F("Đường kính", "d = 2 × r", "r = 3 cm ⇒ d = 6 cm.")),
            G("II. Hình phẳng", F("Hình chữ nhật", "4 góc vuông · 2 chiều dài bằng nhau · 2 chiều rộng bằng nhau"),
              F("Hình vuông", "4 góc vuông · 4 cạnh bằng nhau")),
            G("III. Hình khối", F("Khối lập phương / hộp chữ nhật", "8 đỉnh · 12 cạnh · 6 mặt")),
        ],
        "example": "Đoạn thẳng AB dài 10 cm, M là trung điểm của AB. Tính độ dài AM.",
        "example_answer": "M là trung điểm nên AM = MB = 10 : 2 = **5 cm**.",
        "real_life": "- Dùng compa vẽ hình tròn trang trí; dùng ê-ke kiểm tra góc tường, góc bàn.\n- Hộp quà, viên xúc xắc là khối lập phương; bao diêm là khối hộp chữ nhật.",
        "quiz": [
            mcq("biet", "Hình tròn có bán kính 4 cm thì đường kính là:", ["2 cm", "4 cm", "8 cm", "16 cm"], 2, "d = 2 × 4 = **8 cm**."),
            mcq("biet", "Dụng cụ dùng để kiểm tra góc vuông là:", ["Compa", "Ê-ke", "Thước dây", "Cân"], 1, "Dùng **ê-ke** để kiểm tra, vẽ góc vuông."),
            mcq("biet", "Hình vuông có mấy cạnh bằng nhau?", ["2", "3", "4", "6"], 2, "Hình vuông có **4** cạnh bằng nhau."),
            mcq("biet", "Khối lập phương có bao nhiêu mặt?", ["4", "6", "8", "12"], 1, "Khối lập phương có **6** mặt (đều là hình vuông)."),
            mcq("hieu", "M là trung điểm của đoạn thẳng CD dài 14 cm. Độ dài MD là:", ["7 cm", "14 cm", "28 cm", "12 cm"], 0, "MD = 14 : 2 = **7 cm**."),
            mcq("hieu", "Khối hộp chữ nhật có bao nhiêu cạnh?", ["6", "8", "12", "4"], 2, "Khối hộp chữ nhật có **12** cạnh (và 8 đỉnh, 6 mặt).", note="Hay nhầm số cạnh với số đỉnh."),
            tf("hieu", "Nhận định: “Hình chữ nhật có 4 góc vuông.”", True, "Đúng theo đặc điểm hình chữ nhật → **Đúng**."),
            tf("hieu", "Nhận định: “Điểm O nằm giữa hai điểm A, B thì O chắc chắn là trung điểm của AB.”", False, "Trung điểm còn cần OA = OB; điểm ở giữa chưa chắc chia đôi đoạn thẳng → **Sai**."),
            mcq("vandung", "Một chiếc đĩa tròn có đường kính 20 cm. Bán kính của đĩa là:", ["40 cm", "10 cm", "20 cm", "5 cm"], 1, "r = d : 2 = 20 : 2 = **10 cm**."),
            short("vandung", "Bạn Mai dán một viền giấy màu dọc theo tất cả các cạnh của một hộp quà hình lập phương. Hỏi Mai cần dán bao nhiêu đoạn viền (mỗi cạnh một đoạn)?", ["12"],
                  "Khối lập phương có 12 cạnh nên cần **12** đoạn viền.", unit="đoạn"),
        ],
    },
    # ===================== CHỦ ĐỀ 4 =====================
    {
        "topic": "l3-cd04-nhan-chia-pham-vi-100",
        "title": "Phép nhân, phép chia trong phạm vi 100",
        "icon": "➗",
        "description": "Chủ đề 4 · SGK Toán 3 tập một (tr. 67–84): Bài 23 – Bài 29. Nhân số có hai chữ số với số có một chữ số; gấp một số lên một số lần; phép chia hết, phép chia có dư; chia số có hai chữ số cho số có một chữ số; giảm một số đi một số lần; bài toán giải bằng hai bước tính.",
        "requirements": [
            "Thực hiện được phép nhân số có hai chữ số với số có một chữ số (có nhớ không quá hai lượt và không liên tiếp).",
            "Thực hiện được phép chia số có hai chữ số cho số có một chữ số; nhận biết phép chia hết, phép chia có dư.",
            "Giải được bài toán về gấp một số lên một số lần, giảm một số đi một số lần.",
            "Giải được bài toán có đến hai bước tính.",
        ],
        "definition": (
            "- **Gấp một số lên n lần**: lấy số đó **nhân** với n. **Giảm một số đi n lần**: lấy số đó **chia** cho n.\n"
            "- **Phép chia có dư**: Số bị chia = Thương × Số chia + Số dư; **số dư luôn bé hơn số chia**. Nếu số dư bằng 0 là phép chia hết.\n"
            "- **Bài toán hai bước tính**: tìm một đại lượng trung gian trước, rồi dùng nó tính kết quả."
        ),
        "theory": (
            "### Bài 23. Nhân số có hai chữ số với số có một chữ số\n- 26 × 3: 6 × 3 = 18, viết 8 nhớ 1; 2 × 3 = 6, thêm 1 là 7 → 78.\n"
            "### Bài 24. Gấp một số lên một số lần\n- 5 gấp lên 4 lần: 5 × 4 = 20.\n"
            "### Bài 25. Phép chia hết, phép chia có dư\n- 17 : 5 = 3 (dư 2) vì 3 × 5 + 2 = 17.\n"
            "### Bài 26. Chia số có hai chữ số cho số có một chữ số\n- 84 : 4: 8 : 4 = 2; 4 : 4 = 1 → 21. 75 : 3: 7 : 3 = 2 dư 1, hạ 5 được 15; 15 : 3 = 5 → 25.\n"
            "### Bài 27. Giảm một số đi một số lần\n- 36 giảm đi 4 lần: 36 : 4 = 9.\n"
            "### Bài 28. Bài toán giải bằng hai bước tính\n"
            "### Bài 29. Luyện tập chung"
        ),
        "formulas": [
            G("I. Gấp – giảm", F("Gấp lên n lần", "a × n"), F("Giảm đi n lần", "a : n"),
              F("Phân biệt", "“thêm n đơn vị” → a + n · “gấp n lần” → a × n")),
            G("II. Phép chia có dư", F("Quan hệ", "Số bị chia = Thương × Số chia + Số dư"),
              F("Điều kiện", "Số dư < Số chia", "Chia cho 4 thì số dư chỉ có thể là 0, 1, 2, 3.")),
        ],
        "example": "Thùng thứ nhất có 15 l dầu, thùng thứ hai có số dầu gấp 3 lần thùng thứ nhất. Hỏi cả hai thùng có bao nhiêu lít dầu?",
        "example_answer": "Bước 1 – Thùng thứ hai: 15 × 3 = 45 (l).\nBước 2 – Cả hai thùng: 15 + 45 = **60** (l).\nĐáp số: 60 l dầu.",
        "real_life": "- Mua 4 quyển vở, mỗi quyển 12 nghìn đồng.\n- Xếp 50 quả trứng vào khay 6 quả: được 8 khay và thừa 2 quả.",
        "quiz": [
            mcq("biet", "23 × 3 = ?", ["66", "69", "26", "96"], 1, "3 × 3 = 9; 2 × 3 = 6 → **69**."),
            mcq("biet", "Gấp 7 lên 5 lần được:", ["12", "35", "2", "75"], 1, "7 × 5 = **35**.", note="Không lấy 7 + 5."),
            mcq("biet", "Giảm 48 đi 6 lần được:", ["42", "54", "8", "288"], 2, "48 : 6 = **8**."),
            mcq("biet", "Trong phép chia cho 5, số dư lớn nhất có thể là:", ["5", "4", "6", "0"], 1, "Số dư bé hơn số chia nên lớn nhất là **4**."),
            mcq("hieu", "29 : 4 = ?", ["7", "7 (dư 1)", "6 (dư 5)", "8 (dư 3)"], 1, "4 × 7 = 28; 29 − 28 = 1 → **7 (dư 1)**.", note="6 dư 5 sai vì số dư phải bé hơn 4."),
            mcq("hieu", "18 × 4 = ?", ["42", "72", "62", "48"], 1, "8 × 4 = 32, viết 2 nhớ 3; 1 × 4 = 4, thêm 3 là 7 → **72**."),
            tf("hieu", "Nhận định: “96 : 3 = 32.”", True, "9 : 3 = 3; 6 : 3 = 2 → 32 → **Đúng**."),
            tf("hieu", "Nhận định: “Gấp 6 lên 3 lần được 9.”", False, "Gấp 3 lần: 6 × 3 = 18; 9 là kết quả của “thêm 3” → **Sai**."),
            mcq("vandung", "Có 34 học sinh, mỗi bàn ngồi 4 bạn. Cần ít nhất bao nhiêu bàn để ai cũng có chỗ?", ["8", "9", "7", "10"], 1,
                "34 : 4 = 8 (dư 2). 8 bàn còn 2 bạn chưa có chỗ nên cần thêm 1 bàn: 8 + 1 = **9** bàn.", note="Bài toán “ít nhất” khi có dư phải cộng thêm 1."),
            short("vandung", "Lan có 12 nhãn vở, Hoa có số nhãn vở gấp 4 lần Lan. Hỏi Hoa có nhiều hơn Lan bao nhiêu nhãn vở?", ["36"],
                  "Hoa có: 12 × 4 = 48 (nhãn vở). Hoa nhiều hơn Lan: 48 − 12 = 36 (nhãn vở).\nĐáp số: **36**.", unit="nhãn vở"),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 5 =====================
    {
        "topic": "l3-cd05-don-vi-do-do-dai-khoi-luong-dung-tich-nhiet-do",
        "title": "Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ",
        "icon": "🌡️",
        "description": "Chủ đề 5 · SGK Toán 3 tập một (tr. 85–96): Bài 30 – Bài 35. Mi-li-mét; gam; mi-li-lít; nhiệt độ, đơn vị đo nhiệt độ; thực hành trải nghiệm với mm, g, ml, °C.",
        "requirements": [
            "Nhận biết được đơn vị đo độ dài mm (mi-li-mét); quan hệ giữa các đơn vị m, dm, cm và mm.",
            "Nhận biết được đơn vị đo khối lượng g (gam); quan hệ giữa g và kg.",
            "Nhận biết được đơn vị đo dung tích ml (mi-li-lít); quan hệ giữa l và ml.",
            "Nhận biết được đơn vị đo nhiệt độ (°C); sử dụng được thước, cân, nhiệt kế để thực hành đo; ước lượng số đo trong trường hợp đơn giản.",
        ],
        "definition": (
            "- **Mi-li-mét** (mm): 1 cm = 10 mm; 1 m = 1000 mm.\n"
            "- **Gam** (g): 1 kg = 1000 g.\n"
            "- **Mi-li-lít** (ml): 1 l = 1000 ml.\n"
            "- **Độ C** (°C): đơn vị đo nhiệt độ; đo bằng **nhiệt kế**. Nước đá tan ở 0 °C, nước sôi ở 100 °C; thân nhiệt người khoảng 37 °C."
        ),
        "theory": (
            "### Bài 30. Mi-li-mét\n- Thước kẻ chia vạch nhỏ nhất là 1 mm; 1 cm = 10 mm.\n"
            "### Bài 31. Gam\n- Gói muối 500 g; quả trứng khoảng 50 g; 1 kg = 1000 g.\n"
            "### Bài 32. Mi-li-lít\n- Thìa thuốc 5 ml; chai nước 500 ml; 1 l = 1000 ml.\n"
            "### Bài 33. Nhiệt độ. Đơn vị đo nhiệt độ\n- Đọc nhiệt kế: 25 °C đọc là “hai mươi lăm độ C”.\n"
            "### Bài 34. Thực hành và trải nghiệm với các đơn vị mi-li-mét, gam, mi-li-lít, độ C\n"
            "### Bài 35. Luyện tập chung"
        ),
        "formulas": [
            G("I. Độ dài", F("Quan hệ", "1 m = 10 dm = 100 cm = 1000 mm · 1 cm = 10 mm")),
            G("II. Khối lượng – dung tích", F("Khối lượng", "1 kg = 1000 g"), F("Dung tích", "1 l = 1000 ml")),
            G("III. Nhiệt độ", F("Mốc nhớ", "Nước đá tan 0 °C · Thân nhiệt ≈ 37 °C · Nước sôi 100 °C")),
        ],
        "example": "Đổi: 4 cm = … mm; 2 kg = … g; 3 l = … ml.",
        "example_answer": "4 cm = **40 mm**; 2 kg = **2000 g**; 3 l = **3000 ml**.",
        "real_life": "- Đọc khối lượng trên bao bì (gói mì 75 g), dung tích hộp sữa (180 ml).\n- Đo nhiệt độ khi bị sốt; xem dự báo thời tiết.",
        "quiz": [
            mcq("biet", "1 cm = … mm?", ["10", "100", "1000", "1"], 0, "1 cm = **10 mm**."),
            mcq("biet", "1 kg = … g?", ["10", "100", "1000", "500"], 2, "1 kg = **1000 g**."),
            mcq("biet", "Dụng cụ đo nhiệt độ là:", ["Cân", "Nhiệt kế", "Thước", "Ca đong"], 1, "Đo nhiệt độ bằng **nhiệt kế**."),
            mcq("biet", "1 l = … ml?", ["100", "10", "1000", "10 000"], 2, "1 l = **1000 ml**."),
            mcq("hieu", "Nhiệt độ cơ thể người khỏe mạnh khoảng:", ["37 °C", "100 °C", "0 °C", "73 °C"], 0, "Thân nhiệt bình thường khoảng **37 °C**."),
            mcq("hieu", "500 g + 300 g = ?", ["800 g", "8 kg", "200 g", "800 kg"], 0, "500 + 300 = 800 → **800 g**."),
            tf("hieu", "Nhận định: “Một quả trứng gà nặng khoảng 50 kg.”", False, "Quả trứng gà nặng khoảng 50 **g**, không phải 50 kg → **Sai**."),
            tf("hieu", "Nhận định: “1 m = 1000 mm.”", True, "1 m = 100 cm = 100 × 10 mm = 1000 mm → **Đúng**."),
            mcq("vandung", "Mẹ có 1 l sữa, rót ra 3 cốc, mỗi cốc 200 ml. Còn lại bao nhiêu mi-li-lít sữa?", ["400 ml", "600 ml", "800 ml", "700 ml"], 0,
                "Đã rót: 200 × 3 = 600 (ml). Đổi 1 l = 1000 ml. Còn lại: 1000 − 600 = **400 ml**."),
            short("vandung", "Quả dưa nặng 2 kg, quả bí nặng 750 g. Quả dưa nặng hơn quả bí bao nhiêu gam?", ["1250"],
                  "Đổi 2 kg = 2000 g. Hơn: 2000 − 750 = 1250 (g).\nĐáp số: **1250 g**.", unit="g", note="Phải đổi cùng đơn vị trước khi trừ."),
        ],
    },
    # ===================== CHỦ ĐỀ 6 =====================
    {
        "topic": "l3-cd06-nhan-chia-pham-vi-1000",
        "title": "Phép nhân, phép chia trong phạm vi 1 000",
        "icon": "🧮",
        "description": "Chủ đề 6 · SGK Toán 3 tập một (tr. 97–112): Bài 36 – Bài 40. Nhân số có ba chữ số với số có một chữ số; chia số có ba chữ số cho số có một chữ số; biểu thức số, tính giá trị biểu thức; so sánh số lớn gấp mấy lần số bé.",
        "requirements": [
            "Thực hiện được phép nhân số có ba chữ số với số có một chữ số; phép chia số có ba chữ số cho số có một chữ số.",
            "Làm quen với biểu thức số; tính được giá trị biểu thức có đến hai dấu phép tính, có hoặc không có dấu ngoặc.",
            "Giải được bài toán so sánh số lớn gấp mấy lần số bé.",
        ],
        "definition": (
            "- **Biểu thức số**: dãy các số nối với nhau bởi dấu phép tính, ví dụ 25 + 3 × 4.\n"
            "- **Thứ tự thực hiện**: có ngoặc → tính trong ngoặc trước; không ngoặc: chỉ có +, − (hoặc chỉ ×, :) → tính từ trái sang phải; có cả +, − và ×, : → **nhân, chia trước, cộng, trừ sau**.\n"
            "- **Số lớn gấp mấy lần số bé**: lấy số lớn **chia** cho số bé."
        ),
        "theory": (
            "### Bài 36. Nhân số có ba chữ số với số có một chữ số\n- 216 × 3 = 648; 134 × 4: 4 × 4 = 16, viết 6 nhớ 1; 3 × 4 = 12, thêm 1 = 13, viết 3 nhớ 1; 1 × 4 = 4, thêm 1 = 5 → 536.\n"
            "### Bài 37. Chia số có ba chữ số cho số có một chữ số\n- 648 : 3 = 216; 236 : 4 = 59 (23 : 4 = 5 dư 3, hạ 6 → 36 : 4 = 9).\n"
            "### Bài 38. Biểu thức số. Tính giá trị của biểu thức số\n- 60 + 20 × 3 = 60 + 60 = 120; (60 + 20) × 3 = 80 × 3 = 240.\n"
            "### Bài 39. So sánh số lớn gấp mấy lần số bé\n- 18 gấp 6 số lần: 18 : 6 = 3 lần.\n"
            "### Bài 40. Luyện tập chung"
        ),
        "formulas": [
            G("I. Thứ tự thực hiện", F("Có ngoặc", "( ) trước"), F("Không ngoặc", "× , : trước; + , − sau"),
              F("Cùng loại", "Từ trái sang phải", "48 : 4 × 2 = 12 × 2 = 24.")),
            G("II. So sánh gấp", F("Số lớn gấp mấy lần số bé", "Số lớn : Số bé", "Mẹ 30 tuổi, con 6 tuổi: 30 : 6 = 5 lần.")),
        ],
        "example": "Tính giá trị biểu thức: 120 − 40 : 5 và (120 − 40) : 5.",
        "example_answer": "120 − 40 : 5 = 120 − 8 = **112** (chia trước).\n(120 − 40) : 5 = 80 : 5 = **16** (trong ngoặc trước).",
        "real_life": "- Tính tiền: mua 3 hộp bút giá 125 nghìn đồng một hộp.\n- So sánh chiều cao: cây cao 12 m gấp mấy lần cột cờ 4 m.",
        "quiz": [
            mcq("biet", "213 × 3 = ?", ["639", "636", "216", "693"], 0, "3 × 3 = 9; 1 × 3 = 3; 2 × 3 = 6 → **639**."),
            mcq("biet", "Trong biểu thức 45 + 15 : 3, ta thực hiện phép tính nào trước?", ["Phép cộng", "Phép chia", "Tùy ý", "Từ trái sang phải"], 1, "Không có ngoặc: **chia trước**, cộng sau."),
            mcq("biet", "Muốn biết số lớn gấp mấy lần số bé, ta lấy:", ["Số lớn trừ số bé", "Số lớn cộng số bé", "Số lớn chia số bé", "Số lớn nhân số bé"], 2, "Lấy **số lớn chia cho số bé**."),
            mcq("biet", "848 : 4 = ?", ["212", "202", "221", "2012"], 0, "8 : 4 = 2; 4 : 4 = 1; 8 : 4 = 2 → **212**."),
            mcq("hieu", "Giá trị của biểu thức 50 + 10 × 4 là:", ["240", "90", "64", "200"], 1, "Nhân trước: 10 × 4 = 40; 50 + 40 = **90**.", note="Tính từ trái sang phải ra 240 là sai."),
            mcq("hieu", "125 × 4 = ?", ["500", "480", "520", "800"], 0, "5 × 4 = 20, viết 0 nhớ 2; 2 × 4 + 2 = 10, viết 0 nhớ 1; 1 × 4 + 1 = 5 → **500**."),
            tf("hieu", "Nhận định: “(30 + 6) : 6 = 31.”", False, "Trong ngoặc trước: 36 : 6 = 6, không phải 31 → **Sai**."),
            tf("hieu", "Nhận định: “Số 42 gấp 7 lần số 6.”", True, "42 : 6 = 7 → **Đúng**."),
            mcq("vandung", "Một cuộn dây dài 156 m, cắt thành 4 đoạn bằng nhau. Mỗi đoạn dài:", ["39 m", "38 m", "624 m", "152 m"], 0,
                "156 : 4: 15 : 4 = 3 dư 3, hạ 6 → 36 : 4 = 9 → **39 m**."),
            short("vandung", "Trong vườn có 8 cây cam và 48 cây chanh. Hỏi số cây chanh gấp mấy lần số cây cam?", ["6"],
                  "48 : 8 = 6 (lần).\nĐáp số: **6 lần**.", unit="lần"),
        ],
    },
    # ===================== CHỦ ĐỀ 7 =====================
    {
        "topic": "l3-cd07-on-tap-hoc-ki-1",
        "title": "Ôn tập học kì 1",
        "icon": "📝",
        "description": "Chủ đề 7 · SGK Toán 3 tập một (tr. 113–121): Bài 41 – Bài 44. Ôn tập phép nhân, phép chia trong phạm vi 100, 1000; ôn tập biểu thức số; ôn tập hình học và đo lường.",
        "requirements": [
            "Củng cố bảng nhân, bảng chia 2–9; nhân, chia số có hai, ba chữ số với (cho) số có một chữ số.",
            "Tính được giá trị biểu thức số có đến hai dấu phép tính; tìm thành phần chưa biết.",
            "Củng cố trung điểm, hình tròn, góc vuông, hình chữ nhật, hình vuông, khối hình; đơn vị mm, g, ml, °C.",
            "Giải được bài toán có đến hai bước tính (gấp, giảm, so sánh số lần).",
        ],
        "definition": (
            "- Nhân/chia viết thẳng cột; chia từ hàng cao nhất; số dư < số chia.\n"
            "- Biểu thức: ngoặc trước → nhân, chia → cộng, trừ.\n"
            "- Gấp n lần: × n; giảm n lần: : n; số lớn gấp mấy lần số bé: số lớn : số bé."
        ),
        "theory": (
            "### Bài 41. Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000\n"
            "### Bài 42. Ôn tập biểu thức số\n"
            "### Bài 43. Ôn tập hình học và đo lường\n"
            "- d = 2 × r; trung điểm chia đôi đoạn thẳng; 1 cm = 10 mm, 1 kg = 1000 g, 1 l = 1000 ml.\n"
            "### Bài 44. Ôn tập chung"
        ),
        "formulas": [
            G("I. Phép tính", F("Chia có dư", "Số bị chia = Thương × Số chia + Số dư (dư < số chia)"),
              F("Thứ tự", "( ) → × : → + −")),
            G("II. Đo lường", F("Đổi đơn vị", "1 cm = 10 mm · 1 kg = 1000 g · 1 l = 1000 ml")),
        ],
        "example": "Tính: 7 × 8 − 26 và 7 × (8 − 2).",
        "example_answer": "7 × 8 − 26 = 56 − 26 = **30**. 7 × (8 − 2) = 7 × 6 = **42**.",
        "real_life": "- Tính tiền mua đồ dùng học tập cho cả tổ; chia đều quà cho các nhóm.",
        "quiz": [
            mcq("biet", "7 × 6 = ?", ["42", "48", "36", "13"], 0, "Bảng nhân 7: 7 × 6 = **42**."),
            mcq("biet", "81 : 9 = ?", ["8", "9", "7", "72"], 1, "9 × 9 = 81 → **9**."),
            mcq("biet", "Hình tròn có đường kính 12 cm thì bán kính là:", ["24 cm", "6 cm", "12 cm", "3 cm"], 1, "r = 12 : 2 = **6 cm**."),
            mcq("biet", "3 kg = … g?", ["30", "300", "3000", "3"], 2, "1 kg = 1000 g → 3 kg = **3000 g**."),
            mcq("hieu", "Giá trị của 100 − 4 × 9 là:", ["864", "64", "36", "96"], 1, "Nhân trước: 4 × 9 = 36; 100 − 36 = **64**."),
            mcq("hieu", "Tìm số bị chia: ? : 6 = 15", ["90", "21", "9", "80"], 0, "Số bị chia = 15 × 6 = **90**."),
            tf("hieu", "Nhận định: “427 : 7 = 61.”", True, "42 : 7 = 6; 7 : 7 = 1 → 61 → **Đúng**.", alt="Thử lại: 61 × 7 = 427 ✔."),
            tf("hieu", "Nhận định: “Giảm 56 đi 8 lần được 48.”", False, "Giảm 8 lần: 56 : 8 = 7; 48 là kết quả của “bớt 8” → **Sai**."),
            mcq("vandung", "Mỗi xe chở 9 bao xi măng. Có 5 xe như vậy đã chở được tất cả 45 bao, sau đó chở thêm 18 bao nữa. Tổng số bao đã chở là:", ["63", "53", "72", "27"], 0,
                "5 × 9 = 45 (bao); 45 + 18 = **63** (bao)."),
            short("vandung", "Một trang trại có 135 con gà, số vịt bằng số gà giảm đi 3 lần. Hỏi trang trại có tất cả bao nhiêu con gà và vịt?", ["180"],
                  "Số vịt: 135 : 3 = 45 (con). Cả gà và vịt: 135 + 45 = 180 (con).\nĐáp số: **180 con**.", unit="con"),
        ],
    },
    # ===================== CHỦ ĐỀ 8 =====================
    {
        "topic": "l3-cd08-cac-so-den-10000",
        "title": "Các số đến 10 000",
        "icon": "🔢",
        "description": "Chủ đề 8 · SGK Toán 3 tập hai (tr. 4–20): Bài 45 – Bài 49. Các số có bốn chữ số, số 10 000; so sánh các số trong phạm vi 10 000; làm quen với chữ số La Mã; làm tròn số đến hàng chục, hàng trăm.",
        "requirements": [
            "Đọc, viết được các số trong phạm vi 10 000; nhận biết số tròn nghìn; cấu tạo thập phân của số.",
            "So sánh được hai số; xác định số lớn nhất, bé nhất và sắp xếp nhóm không quá 4 số trong phạm vi 10 000.",
            "Nhận biết được chữ số La Mã và viết được các số trong phạm vi 20 bằng chữ số La Mã.",
            "Làm quen với việc làm tròn số đến hàng chục, hàng trăm.",
        ],
        "definition": (
            "- **Số có bốn chữ số**: hàng nghìn, trăm, chục, đơn vị. 3725 = 3000 + 700 + 20 + 5. 10 nghìn = **10 000** (mười nghìn).\n"
            "- **So sánh**: số nào nhiều chữ số hơn thì lớn hơn; cùng số chữ số thì so sánh từng hàng từ trái sang phải.\n"
            "- **Chữ số La Mã**: I = 1, V = 5, X = 10. Ghép: II = 2, IV = 4, VI = 6, IX = 9, XI = 11, XIV = 14, XIX = 19, XX = 20.\n"
            "- **Làm tròn đến hàng chục**: chữ số hàng đơn vị < 5 thì làm tròn xuống, ≥ 5 thì làm tròn lên (tương tự cho hàng trăm, xét chữ số hàng chục)."
        ),
        "theory": (
            "### Bài 45. Các số có bốn chữ số. Số 10 000\n- 4058: bốn nghìn không trăm năm mươi tám.\n"
            "### Bài 46. So sánh các số trong phạm vi 10 000\n- 5891 < 6012 (5 nghìn < 6 nghìn); 9999 < 10 000.\n"
            "### Bài 47. Làm quen với chữ số La Mã\n- Chữ số đứng sau lớn hơn → trừ (IV = 5 − 1); đứng sau nhỏ hơn → cộng (VI = 5 + 1). Một chữ số không lặp quá 3 lần.\n"
            "### Bài 48. Làm tròn số đến hàng chục, hàng trăm\n- 1234 làm tròn đến hàng chục được 1230; 3478 làm tròn đến hàng trăm được 3500.\n"
            "### Bài 49. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cấu tạo số", F("Số bốn chữ số", "abcd = a nghìn + b trăm + c chục + d đơn vị", "6204 = 6000 + 200 + 4.")),
            G("II. Chữ số La Mã", F("Ký hiệu", "I = 1 · V = 5 · X = 10"),
              F("Quy tắc", "Nhỏ đứng trước lớn → trừ; nhỏ đứng sau lớn → cộng", "IX = 9, XI = 11, XIV = 14.")),
            G("III. Làm tròn", F("Quy tắc 5", "Chữ số bên phải hàng làm tròn: < 5 → xuống; ≥ 5 → lên", "2650 → tròn trăm: 2700.")),
        ],
        "example": "Làm tròn số 4762 đến hàng chục và hàng trăm.",
        "example_answer": "Đến hàng chục: hàng đơn vị là 2 < 5 → **4760**.\nĐến hàng trăm: hàng chục là 6 ≥ 5 → **4800**.",
        "real_life": "- Mặt đồng hồ dùng số La Mã; tên thế kỉ (thế kỉ XX, XXI).\n- Làm tròn giá tiền, số dân để ước lượng nhanh.",
        "quiz": [
            mcq("biet", "Số “năm nghìn không trăm linh bảy” viết là:", ["5007", "5070", "507", "50 007"], 0, "5000 + 0 + 0 + 7 = **5007**."),
            mcq("biet", "Chữ số La Mã X có giá trị là:", ["5", "10", "1", "50"], 1, "X = **10**."),
            mcq("biet", "Số liền sau của 9999 là:", ["9998", "10 000", "1000", "99 990"], 1, "9999 + 1 = **10 000**."),
            mcq("biet", "Số 3082 gồm:", ["3 nghìn, 8 chục, 2 đơn vị", "3 nghìn, 8 trăm, 2 đơn vị", "30 trăm, 82 nghìn", "3 trăm, 8 chục, 2 đơn vị"], 0, "3082 = 3000 + 0 + 80 + 2."),
            mcq("hieu", "Số IX viết bằng chữ số thường là:", ["11", "9", "4", "6"], 1, "I đứng trước X → 10 − 1 = **9**.", note="XI mới là 11."),
            mcq("hieu", "Làm tròn số 2385 đến hàng trăm được:", ["2300", "2400", "2390", "2380"], 1, "Hàng chục là 8 ≥ 5 → làm tròn lên: **2400**."),
            tf("hieu", "Nhận định: “7099 > 7100.”", False, "Cùng 7 nghìn; hàng trăm 0 < 1 → 7099 < 7100 → **Sai**."),
            tf("hieu", "Nhận định: “Số 14 viết bằng chữ số La Mã là XIV.”", True, "XIV = X + IV = 10 + 4 = 14 → **Đúng**."),
            mcq("vandung", "Sắp xếp các số 4320, 4302, 4230, 4203 theo thứ tự từ lớn đến bé:", ["4320, 4302, 4230, 4203", "4203, 4230, 4302, 4320", "4302, 4320, 4230, 4203", "4320, 4230, 4302, 4203"], 0,
                "So sánh hàng trăm: 3 > 2; trong nhóm 43..: 4320 > 4302; nhóm 42..: 4230 > 4203 → **4320, 4302, 4230, 4203**."),
            short("vandung", "Một trường có 1347 học sinh. Làm tròn số học sinh đến hàng chục thì được bao nhiêu?", ["1350"],
                  "Hàng đơn vị là 7 ≥ 5 → làm tròn lên: 1347 → **1350**."),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 9 =====================
    {
        "topic": "l3-cd09-chu-vi-dien-tich",
        "title": "Chu vi, diện tích một số hình phẳng",
        "icon": "⬛",
        "description": "Chủ đề 9 · SGK Toán 3 tập hai (tr. 21–37): Bài 50 – Bài 53. Chu vi hình tam giác, tứ giác, hình chữ nhật, hình vuông; diện tích của một hình, xăng-ti-mét vuông; diện tích hình chữ nhật, hình vuông.",
        "requirements": [
            "Tính được chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông khi biết độ dài các cạnh.",
            "Nhận biết được “diện tích” thông qua biểu tượng cụ thể; nhận biết đơn vị đo diện tích cm² (xăng-ti-mét vuông).",
            "Tính được diện tích hình chữ nhật, hình vuông.",
            "Giải quyết được một số vấn đề thực tiễn liên quan đến chu vi, diện tích.",
        ],
        "definition": (
            "- **Chu vi** của một hình là **tổng độ dài các cạnh** của hình đó (độ dài đường bao quanh).\n"
            "- **Diện tích** là phần mặt phẳng mà hình chiếm. **1 cm²** là diện tích hình vuông cạnh 1 cm.\n"
            "- Chu vi đo bằng đơn vị độ dài (cm, m); diện tích đo bằng đơn vị diện tích (cm²)."
        ),
        "theory": (
            "### Bài 50. Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông\n"
            "- Tam giác cạnh 3, 4, 5 cm: chu vi = 3 + 4 + 5 = 12 cm.\n"
            "- Hình chữ nhật dài 6 cm, rộng 4 cm: chu vi = (6 + 4) × 2 = 20 cm. Hình vuông cạnh 5 cm: chu vi = 5 × 4 = 20 cm.\n"
            "### Bài 51. Diện tích của một hình. Xăng-ti-mét vuông\n- Đếm số ô vuông 1 cm² phủ kín hình.\n"
            "### Bài 52. Diện tích hình chữ nhật, diện tích hình vuông\n- Hình chữ nhật 6 cm × 4 cm: S = 24 cm²; hình vuông cạnh 5 cm: S = 25 cm².\n"
            "### Bài 53. Luyện tập chung"
        ),
        "formulas": [
            G("I. Chu vi", F("Tam giác, tứ giác", "P = tổng độ dài các cạnh"),
              F("Hình chữ nhật", "P = (a + b) × 2", "a: chiều dài, b: chiều rộng (cùng đơn vị)."),
              F("Hình vuông", "P = a × 4")),
            G("II. Diện tích", F("Hình chữ nhật", "S = a × b"), F("Hình vuông", "S = a × a"),
              F("Đơn vị", "cm² — đọc “xăng-ti-mét vuông”")),
        ],
        "example": "Một hình chữ nhật có chiều dài 9 cm, chiều rộng 5 cm. Tính chu vi và diện tích.",
        "example_answer": "Chu vi: (9 + 5) × 2 = **28 cm**.\nDiện tích: 9 × 5 = **45 cm²**.",
        "real_life": "- Tính chiều dài hàng rào quanh vườn (chu vi); tính số viên gạch lát nền (diện tích).\n- Bọc bìa quyển sách, dán giấy trang trí.",
        "quiz": [
            mcq("biet", "Chu vi hình vuông cạnh 6 cm là:", ["12 cm", "24 cm", "36 cm", "36 cm²"], 1, "P = 6 × 4 = **24 cm**."),
            mcq("biet", "Diện tích hình vuông cạnh 6 cm là:", ["24 cm²", "36 cm²", "12 cm²", "36 cm"], 1, "S = 6 × 6 = **36 cm²**.", note="Diện tích dùng đơn vị cm², không phải cm."),
            mcq("biet", "Công thức tính chu vi hình chữ nhật là:", ["(a + b) × 2", "a × b", "a × 4", "a + b"], 0, "P = **(a + b) × 2**."),
            mcq("biet", "Tam giác có ba cạnh 5 cm, 7 cm, 8 cm. Chu vi tam giác là:", ["20 cm", "15 cm", "280 cm", "13 cm"], 0, "5 + 7 + 8 = **20 cm**."),
            mcq("hieu", "Hình chữ nhật dài 8 cm, rộng 3 cm có diện tích là:", ["22 cm²", "24 cm²", "11 cm²", "24 cm"], 1, "S = 8 × 3 = **24 cm²**."),
            mcq("hieu", "Hình chữ nhật dài 2 dm, rộng 8 cm có chu vi là:", ["20 cm", "56 cm", "160 cm", "28 cm"], 1, "Đổi 2 dm = 20 cm. P = (20 + 8) × 2 = **56 cm**.", note="Hai cạnh phải cùng đơn vị."),
            tf("hieu", "Nhận định: “Hình chữ nhật dài 5 cm, rộng 3 cm có diện tích 16 cm².”", False,
               "S = 5 × 3 = 15 cm²; 16 cm là chu vi (5 + 3) × 2 → **Sai**.", note="Đừng nhầm công thức chu vi với diện tích."),
            tf("hieu", "Nhận định: “Chu vi hình chữ nhật dài 7 cm, rộng 5 cm là 24 cm.”", True, "(7 + 5) × 2 = 24 cm → **Đúng**."),
            mcq("vandung", "Một mảnh vườn hình vuông có chu vi 36 m. Cạnh của mảnh vườn dài:", ["9 m", "18 m", "6 m", "144 m"], 0, "Cạnh = chu vi : 4 = 36 : 4 = **9 m**."),
            short("vandung", "Một tấm bìa hình chữ nhật có chiều rộng 6 cm, chiều dài gấp 2 lần chiều rộng. Tính diện tích tấm bìa (cm²).", ["72"],
                  "Chiều dài: 6 × 2 = 12 (cm). Diện tích: 12 × 6 = 72 (cm²).\nĐáp số: **72 cm²**.", unit="cm²"),
        ],
    },
    # ===================== CHỦ ĐỀ 10 =====================
    {
        "topic": "l3-cd10-cong-tru-nhan-chia-pham-vi-10000",
        "title": "Cộng, trừ, nhân, chia trong phạm vi 10 000",
        "icon": "➕",
        "description": "Chủ đề 10 · SGK Toán 3 tập hai (tr. 38–55): Bài 54 – Bài 58. Phép cộng, phép trừ trong phạm vi 10 000; nhân số có bốn chữ số với số có một chữ số; chia số có bốn chữ số cho số có một chữ số.",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ các số có bốn chữ số (có nhớ không quá hai lượt và không liên tiếp).",
            "Thực hiện được phép nhân số có bốn chữ số với số có một chữ số; phép chia số có bốn chữ số cho số có một chữ số.",
            "Thực hiện được tính nhẩm với số tròn nghìn, tròn trăm; giải bài toán có đến hai bước tính.",
        ],
        "definition": (
            "- **Cộng, trừ**: đặt tính thẳng cột theo hàng, tính từ phải sang trái (đơn vị → chục → trăm → nghìn).\n"
            "- **Nhân**: nhân lần lượt từ hàng đơn vị, nhớ sang hàng tiếp theo.\n"
            "- **Chia**: chia lần lượt từ hàng **cao nhất**; mỗi lượt: chia – nhân – trừ – hạ.\n"
            "- Nhẩm: 3000 + 4000 = 7000 (3 nghìn + 4 nghìn); 2000 × 3 = 6000; 8000 : 4 = 2000."
        ),
        "theory": (
            "### Bài 54. Phép cộng trong phạm vi 10 000\n- 3526 + 2748 = 6274.\n"
            "### Bài 55. Phép trừ trong phạm vi 10 000\n- 7452 − 3218 = 4234.\n"
            "### Bài 56. Nhân số có bốn chữ số với số có một chữ số\n- 1218 × 4 = 4872.\n"
            "### Bài 57. Chia số có bốn chữ số cho số có một chữ số\n- 6369 : 3 = 2123; 4218 : 6 = 703 (42 : 6 = 7; hạ 1, 1 : 6 = 0; hạ 8, 18 : 6 = 3).\n"
            "### Bài 58. Luyện tập chung"
        ),
        "formulas": [
            G("I. Quy tắc tính viết", F("Cộng, trừ, nhân", "Tính từ phải sang trái, nhớ sang hàng kế tiếp"),
              F("Chia", "Từ trái sang phải: chia → nhân → trừ → hạ", "Lượt nào số bị chia nhỏ hơn số chia thì viết 0 ở thương.")),
            G("II. Thử lại", F("Phép trừ", "Hiệu + Số trừ = Số bị trừ"), F("Phép chia", "Thương × Số chia (+ Số dư) = Số bị chia")),
        ],
        "example": "Đặt tính rồi tính: 2615 × 3 và 3640 : 5.",
        "example_answer": "2615 × 3: 5 × 3 = 15 viết 5 nhớ 1; 1 × 3 + 1 = 4; 6 × 3 = 18 viết 8 nhớ 1; 2 × 3 + 1 = 7 → **7845**.\n3640 : 5: 36 : 5 = 7 dư 1; hạ 4 → 14 : 5 = 2 dư 4; hạ 0 → 40 : 5 = 8 → **728**.",
        "real_life": "- Tính tổng tiền mua sắm (đơn vị nghìn đồng); chia đều số sách cho các lớp.",
        "quiz": [
            mcq("biet", "4000 + 3000 = ?", ["7000", "700", "70 000", "1000"], 0, "4 nghìn + 3 nghìn = **7000**."),
            mcq("biet", "Khi chia số có bốn chữ số cho số có một chữ số, ta bắt đầu chia từ:", ["Hàng đơn vị", "Hàng chục", "Hàng cao nhất (bên trái)", "Hàng nào cũng được"], 2, "Phép chia thực hiện từ **hàng cao nhất**."),
            mcq("biet", "2143 × 2 = ?", ["4286", "4386", "2145", "4246"], 0, "3 × 2 = 6; 4 × 2 = 8; 1 × 2 = 2; 2 × 2 = 4 → **4286**."),
            mcq("biet", "9000 − 5000 = ?", ["4000", "14 000", "400", "5000"], 0, "9 nghìn − 5 nghìn = **4000**."),
            mcq("hieu", "4527 + 3685 = ?", ["8212", "8112", "7212", "8202"], 0, "7 + 5 = 12 (nhớ 1); 2 + 8 + 1 = 11 (nhớ 1); 5 + 6 + 1 = 12 (nhớ 1); 4 + 3 + 1 = 8 → **8212**."),
            mcq("hieu", "2436 : 4 = ?", ["609", "690", "69", "6009"], 0, "24 : 4 = 6; hạ 3, 3 : 4 = 0 (viết 0); hạ 6 → 36 : 4 = 9 → **609**.", note="Quên viết chữ số 0 ở thương sẽ ra 69."),
            tf("hieu", "Nhận định: “6000 − 2785 = 3215.”", True, "Thử lại: 3215 + 2785 = 6000 → **Đúng**."),
            tf("hieu", "Nhận định: “1625 × 4 = 6400.”", False, "1625 × 4 = 6500 (5 × 4 = 20; 2 × 4 + 2 = 10; 6 × 4 + 1 = 25; 1 × 4 + 2 = 6) → **Sai**."),
            mcq("vandung", "Một nhà máy ngày đầu sản xuất 1250 sản phẩm, ngày thứ hai sản xuất gấp đôi ngày đầu. Cả hai ngày sản xuất được:", ["2500", "3750", "3500", "1252"], 1,
                "Ngày thứ hai: 1250 × 2 = 2500. Cả hai ngày: 1250 + 2500 = **3750** sản phẩm."),
            short("vandung", "Có 2835 quyển sách xếp đều vào 5 tủ. Mỗi tủ có bao nhiêu quyển sách?", ["567"],
                  "2835 : 5: 28 : 5 = 5 dư 3; hạ 3 → 33 : 5 = 6 dư 3; hạ 5 → 35 : 5 = 7 → 567.\nĐáp số: **567 quyển**.", unit="quyển"),
        ],
    },
    # ===================== CHỦ ĐỀ 11 =====================
    {
        "topic": "l3-cd11-cac-so-den-100000",
        "title": "Các số đến 100 000",
        "icon": "💯",
        "description": "Chủ đề 11 · SGK Toán 3 tập hai (tr. 56–69): Bài 59 – Bài 62. Các số có năm chữ số, số 100 000; so sánh các số trong phạm vi 100 000; làm tròn số đến hàng nghìn, hàng chục nghìn.",
        "requirements": [
            "Đọc, viết được các số trong phạm vi 100 000; nhận biết số tròn nghìn, tròn mười nghìn; cấu tạo thập phân của số.",
            "So sánh hai số; xác định số lớn nhất, bé nhất; sắp xếp nhóm không quá 4 số trong phạm vi 100 000.",
            "Làm quen với việc làm tròn số đến hàng nghìn, hàng chục nghìn.",
        ],
        "definition": (
            "- **Số có năm chữ số**: hàng chục nghìn, nghìn, trăm, chục, đơn vị. 45 813 = 40 000 + 5000 + 800 + 10 + 3.\n"
            "- 10 chục nghìn = **100 000** (một trăm nghìn).\n"
            "- **Làm tròn đến hàng nghìn**: xét chữ số hàng trăm; **đến hàng chục nghìn**: xét chữ số hàng nghìn (< 5 xuống, ≥ 5 lên)."
        ),
        "theory": (
            "### Bài 59. Các số có năm chữ số. Số 100 000\n- 70 506: bảy mươi nghìn năm trăm linh sáu.\n"
            "### Bài 60. So sánh các số trong phạm vi 100 000\n- 48 920 < 51 003 (4 chục nghìn < 5 chục nghìn).\n"
            "### Bài 61. Làm tròn số đến hàng nghìn, hàng chục nghìn\n- 36 452 → tròn nghìn: 36 000; tròn chục nghìn: 40 000.\n"
            "### Bài 62. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cấu tạo số", F("Số năm chữ số", "abcde = a chục nghìn + b nghìn + c trăm + d chục + e đơn vị")),
            G("II. So sánh – làm tròn", F("So sánh", "Nhiều chữ số hơn thì lớn hơn; cùng số chữ số: so từ trái sang phải"),
              F("Làm tròn", "Nhìn chữ số ngay bên phải hàng cần làm tròn: < 5 → giữ; ≥ 5 → tăng 1", "72 680 → tròn nghìn: 73 000.")),
        ],
        "example": "Viết số gồm 6 chục nghìn, 0 nghìn, 4 trăm, 0 chục, 9 đơn vị; đọc số đó.",
        "example_answer": "**60 409** — đọc: sáu mươi nghìn bốn trăm linh chín.",
        "real_life": "- Đọc số dân của một xã (12 450 người), giá tiền (85 000 đồng).\n- Làm tròn để ước lượng: khoảng 12 000 người.",
        "quiz": [
            mcq("biet", "Số “ba mươi hai nghìn không trăm mười lăm” viết là:", ["32 015", "32 150", "3215", "320 015"], 0, "30 000 + 2000 + 0 + 10 + 5 = **32 015**."),
            mcq("biet", "Trong số 58 247, chữ số 8 thuộc hàng:", ["Chục nghìn", "Nghìn", "Trăm", "Chục"], 1, "5 chục nghìn, **8 nghìn**, 2 trăm, 4 chục, 7 đơn vị."),
            mcq("biet", "Số liền trước của 100 000 là:", ["99 999", "100 001", "99 000", "10 000"], 0, "100 000 − 1 = **99 999**."),
            mcq("biet", "Số tròn chục nghìn là:", ["45 000", "70 000", "70 500", "7000"], 1, "**70 000** có các hàng nghìn, trăm, chục, đơn vị đều là 0."),
            mcq("hieu", "Làm tròn số 64 718 đến hàng nghìn được:", ["64 000", "65 000", "64 700", "60 000"], 1, "Hàng trăm là 7 ≥ 5 → làm tròn lên **65 000**."),
            mcq("hieu", "Số lớn nhất trong các số 89 012; 89 120; 81 920; 89 102 là:", ["89 012", "89 120", "81 920", "89 102"], 1, "Ba số có 89 nghìn; so hàng trăm: 1 = 1 > 0; so chục 2 > 0 → **89 120**."),
            tf("hieu", "Nhận định: “40 000 + 5000 + 30 + 8 = 45 038.”", True, "4 chục nghìn, 5 nghìn, 0 trăm, 3 chục, 8 đơn vị → 45 038 → **Đúng**."),
            tf("hieu", "Nhận định: “Làm tròn 25 300 đến hàng chục nghìn được 20 000.”", False, "Chữ số hàng nghìn là 5 ≥ 5 → làm tròn lên 30 000 → **Sai**."),
            mcq("vandung", "Dân số xã A là 12 876 người, xã B là 12 867 người, xã C là 13 002 người. Xã nào đông dân nhất?", ["Xã A", "Xã B", "Xã C", "Bằng nhau"], 2, "13 002 có 3 nghìn > 2 nghìn → **xã C**."),
            short("vandung", "Viết số lớn nhất có năm chữ số khác nhau.", ["98765", "98 765"],
                  "Chọn chữ số lớn nhất lần lượt cho các hàng: 9, 8, 7, 6, 5 → **98 765**.", note="Không phải 99 999 vì các chữ số phải khác nhau."),
        ],
    },
    # ===================== CHỦ ĐỀ 12 =====================
    {
        "topic": "l3-cd12-cong-tru-pham-vi-100000",
        "title": "Cộng, trừ trong phạm vi 100 000",
        "icon": "➖",
        "description": "Chủ đề 12 · SGK Toán 3 tập hai (tr. 70–76): Bài 63 – Bài 65. Phép cộng, phép trừ trong phạm vi 100 000; tính chất giao hoán, kết hợp của phép cộng.",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ các số có đến năm chữ số (có nhớ không quá hai lượt và không liên tiếp).",
            "Nhận biết được tính chất giao hoán, tính chất kết hợp của phép cộng và mối quan hệ giữa phép cộng với phép trừ trong thực hành tính.",
            "Cộng, trừ nhẩm các số tròn nghìn, tròn chục nghìn; giải bài toán có đến hai bước tính.",
        ],
        "definition": (
            "- **Giao hoán**: a + b = b + a. **Kết hợp**: (a + b) + c = a + (b + c) — giúp tính nhanh bằng cách nhóm các số tròn.\n"
            "- **Quan hệ cộng – trừ**: a + b = c ⇒ c − a = b và c − b = a (dùng để thử lại, tìm thành phần chưa biết)."
        ),
        "theory": (
            "### Bài 63. Phép cộng trong phạm vi 100 000\n- 35 248 + 41 637 = 76 885. Tính nhanh: 2500 + 1300 + 7500 = (2500 + 7500) + 1300 = 11 300.\n"
            "### Bài 64. Phép trừ trong phạm vi 100 000\n- 85 372 − 26 145 = 59 227.\n"
            "### Bài 65. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tính chất phép cộng", F("Giao hoán", "a + b = b + a"), F("Kết hợp", "(a + b) + c = a + (b + c)")),
            G("II. Liên hệ", F("Cộng ↔ trừ", "a + b = c ⇒ c − b = a"), F("Nhẩm", "50 000 − 20 000 = 30 000 (5 chục nghìn − 2 chục nghìn)")),
        ],
        "example": "Tính bằng cách thuận tiện: 4600 + 2700 + 5400.",
        "example_answer": "(4600 + 5400) + 2700 = 10 000 + 2700 = **12 700**.",
        "real_life": "- Tính tổng tiền điện, nước trong tháng; số tiền còn lại sau khi mua sắm.",
        "quiz": [
            mcq("biet", "60 000 + 30 000 = ?", ["90 000", "9000", "900 000", "30 000"], 0, "6 chục nghìn + 3 chục nghìn = **90 000**."),
            mcq("biet", "Tính chất a + b = b + a gọi là:", ["Tính chất kết hợp", "Tính chất giao hoán", "Tính chất phân phối", "Quy tắc nhân"], 1, "Đổi chỗ các số hạng → **giao hoán**."),
            mcq("biet", "23 415 + 51 302 = ?", ["74 717", "74 727", "72 717", "28 113"], 0, "5 + 2 = 7; 1 + 0 = 1; 4 + 3 = 7; 3 + 1 = 4; 2 + 5 = 7 → **74 717**."),
            mcq("biet", "80 000 − 50 000 = ?", ["30 000", "3000", "130 000", "35 000"], 0, "8 − 5 = 3 chục nghìn → **30 000**."),
            mcq("hieu", "62 548 − 27 316 = ?", ["35 232", "35 332", "45 232", "35 222"], 0, "8 − 6 = 2; 4 − 1 = 3; 5 − 3 = 2; 12 − 7 = 5 (nhớ 1); 6 − 3 = 3 → **35 232**."),
            mcq("hieu", "Tìm x biết: x + 25 600 = 70 000", ["44 400", "95 600", "45 400", "54 400"], 0, "x = 70 000 − 25 600 = **44 400**."),
            tf("hieu", "Nhận định: “1800 + 3500 + 200 = 5500.”", True, "(1800 + 200) + 3500 = 2000 + 3500 = 5500 → **Đúng**."),
            tf("hieu", "Nhận định: “47 280 + 36 450 = 73 730.”", False, "47 280 + 36 450 = 83 730 (cộng hàng chục nghìn: 4 + 3 + 1 nhớ = 8) → **Sai**.", note="Lỗi quên nhớ khi cộng hàng nghìn (7 + 6 = 13)."),
            mcq("vandung", "Mẹ mang 100 000 đồng đi chợ, mua thịt hết 45 000 đồng và rau hết 12 000 đồng. Mẹ còn lại:", ["43 000 đồng", "57 000 đồng", "33 000 đồng", "53 000 đồng"], 0,
                "Đã mua: 45 000 + 12 000 = 57 000. Còn: 100 000 − 57 000 = **43 000 đồng**."),
            short("vandung", "Một kho có 35 750 kg thóc. Lần đầu xuất 12 500 kg, lần sau xuất 8 250 kg. Hỏi kho còn lại bao nhiêu ki-lô-gam thóc?", ["15000", "15 000"],
                  "Đã xuất: 12 500 + 8 250 = 20 750 (kg). Còn lại: 35 750 − 20 750 = 15 000 (kg).\nĐáp số: **15 000 kg**.", unit="kg",
                  alt="35 750 − 12 500 = 23 250; 23 250 − 8 250 = 15 000."),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 13 =====================
    {
        "topic": "l3-cd13-dong-ho-thang-nam-tien",
        "title": "Xem đồng hồ. Tháng – năm. Tiền Việt Nam",
        "icon": "🕰️",
        "description": "Chủ đề 13 · SGK Toán 3 tập hai (tr. 77–93): Bài 66 – Bài 69. Xem đồng hồ (chính xác đến 5 phút, từng phút); tháng – năm; thực hành xem đồng hồ, xem lịch; tiền Việt Nam.",
        "requirements": [
            "Đọc được giờ chính xác đến 5 phút và từng phút trên đồng hồ.",
            "Nhận biết được các tháng trong năm và số ngày của từng tháng; xem được lịch.",
            "Nhận biết được mệnh giá các tờ tiền Việt Nam trong phạm vi 100 000 đồng; nhận biết tờ 200 000 đồng, 500 000 đồng.",
            "Thực hiện được chuyển đổi, tính toán với số đo thời gian (phút, giờ, ngày, tuần lễ, tháng, năm) và tiền Việt Nam.",
        ],
        "definition": (
            "- **Đồng hồ**: kim giờ ngắn, kim phút dài; mỗi số trên mặt đồng hồ ứng với **5 phút** của kim phút; 1 giờ = 60 phút.\n"
            "- Cách đọc: 8 giờ 45 phút = **9 giờ kém 15 phút**.\n"
            "- **Năm** có 12 tháng. Tháng có 31 ngày: 1, 3, 5, 7, 8, 10, 12; tháng có 30 ngày: 4, 6, 9, 11; tháng 2 có 28 hoặc 29 ngày.\n"
            "- **Tiền Việt Nam** (đồng): các tờ 1000, 2000, 5000, 10 000, 20 000, 50 000, 100 000, 200 000, 500 000 đồng."
        ),
        "theory": (
            "### Bài 66. Xem đồng hồ. Tháng – năm\n- Kim phút chỉ số 7 → 35 phút. Kim phút chỉ giữa vạch → đếm từng phút.\n"
            "### Bài 67. Thực hành xem đồng hồ, xem lịch\n- Xem lịch: ngày, thứ trong tuần; 1 tuần = 7 ngày.\n"
            "### Bài 68. Tiền Việt Nam\n- Đổi tiền, cộng trừ tiền khi mua bán.\n"
            "### Bài 69. Luyện tập chung"
        ),
        "formulas": [
            G("I. Thời gian", F("Quan hệ", "1 giờ = 60 phút · 1 ngày = 24 giờ · 1 tuần = 7 ngày · 1 năm = 12 tháng"),
              F("Kim phút", "Mỗi số = 5 phút", "Chỉ số 9 → 45 phút."),
              F("Mẹo nhớ ngày trong tháng", "Đếm trên khớp nắm tay: tháng ở khớp lồi có 31 ngày")),
            G("II. Tiền", F("Đơn vị", "đồng"), F("Tiền thừa", "Tiền đưa − Tiền hàng")),
        ],
        "example": "Một bộ phim bắt đầu lúc 7 giờ 15 phút và kéo dài 50 phút. Phim kết thúc lúc mấy giờ?",
        "example_answer": "7 giờ 15 phút + 50 phút = 7 giờ 65 phút = **8 giờ 5 phút**.",
        "real_life": "- Lên thời gian biểu; tính số ngày đến sinh nhật.\n- Mua đồ ở căng tin, tính tiền thừa.",
        "quiz": [
            mcq("biet", "Một năm có bao nhiêu tháng?", ["10", "12", "7", "30"], 1, "Một năm có **12** tháng."),
            mcq("biet", "Tháng nào có 30 ngày?", ["Tháng 1", "Tháng 4", "Tháng 8", "Tháng 12"], 1, "Các tháng 4, 6, 9, 11 có 30 ngày → **Tháng 4**."),
            mcq("biet", "Kim phút chỉ vào số 6 nghĩa là:", ["6 phút", "30 phút", "60 phút", "15 phút"], 1, "6 × 5 = **30 phút**."),
            mcq("biet", "Tờ tiền có mệnh giá lớn nhất trong các tờ sau là:", ["50 000 đồng", "20 000 đồng", "100 000 đồng", "10 000 đồng"], 2, "**100 000 đồng** lớn nhất."),
            mcq("hieu", "8 giờ 50 phút còn gọi là:", ["8 giờ kém 10 phút", "9 giờ kém 10 phút", "9 giờ 10 phút", "10 giờ kém 50 phút"], 1, "Còn 10 phút nữa đến 9 giờ → **9 giờ kém 10 phút**."),
            mcq("hieu", "Ngày 28 tháng 3 là thứ Hai. Ngày 4 tháng 4 cùng năm là thứ mấy?", ["Chủ nhật", "Thứ Hai", "Thứ Ba", "Thứ Bảy"], 1,
                "Tháng 3 có 31 ngày: từ 28/3 đến 4/4 là 7 ngày = 1 tuần → vẫn là **thứ Hai**."),
            tf("hieu", "Nhận định: “Tháng 2 luôn có 30 ngày.”", False, "Tháng 2 có 28 hoặc 29 ngày → **Sai**."),
            tf("hieu", "Nhận định: “2 tờ 20 000 đồng và 1 tờ 10 000 đồng là 50 000 đồng.”", True, "20 000 × 2 + 10 000 = 50 000 → **Đúng**."),
            mcq("vandung", "Lan đưa cô bán hàng tờ 50 000 đồng để mua quyển truyện giá 35 000 đồng. Cô trả lại Lan:", ["15 000 đồng", "25 000 đồng", "85 000 đồng", "5000 đồng"], 0, "50 000 − 35 000 = **15 000 đồng**."),
            short("vandung", "Bạn Minh bắt đầu làm bài lúc 19 giờ 20 phút và làm xong lúc 20 giờ 5 phút. Minh làm bài trong bao nhiêu phút?", ["45"],
                  "Từ 19 giờ 20 phút đến 20 giờ là 40 phút; thêm 5 phút → 45 phút.\nĐáp số: **45 phút**.", unit="phút"),
        ],
    },
    # ===================== CHỦ ĐỀ 14 =====================
    {
        "topic": "l3-cd14-nhan-chia-pham-vi-100000",
        "title": "Nhân, chia trong phạm vi 100 000",
        "icon": "✖️",
        "description": "Chủ đề 14 · SGK Toán 3 tập hai (tr. 94–102): Bài 70 – Bài 72. Nhân số có năm chữ số với số có một chữ số; chia số có năm chữ số cho số có một chữ số.",
        "requirements": [
            "Thực hiện được phép nhân số có năm chữ số với số có một chữ số (có nhớ không quá hai lượt và không liên tiếp).",
            "Thực hiện được phép chia số có năm chữ số cho số có một chữ số (chia hết và có dư).",
            "Nhận biết tính chất giao hoán, kết hợp của phép nhân; nhân, chia nhẩm số tròn nghìn, tròn chục nghìn; giải bài toán có đến hai bước tính.",
        ],
        "definition": (
            "- **Giao hoán**: a × b = b × a. **Kết hợp**: (a × b) × c = a × (b × c).\n"
            "- Nhân: từ phải sang trái, nhớ sang hàng kế. Chia: từ trái sang phải, lượt nào chưa đủ chia thì viết 0 ở thương.\n"
            "- Nhẩm: 12 000 × 4 = 48 000 (12 nghìn × 4); 60 000 : 3 = 20 000."
        ),
        "theory": (
            "### Bài 70. Nhân số có năm chữ số với số có một chữ số\n- 21 304 × 3 = 63 912; 13 052 × 4 = 52 208.\n"
            "### Bài 71. Chia số có năm chữ số cho số có một chữ số\n- 36 284 : 4 = 9071; 25 609 : 5 = 5121 (dư 4).\n"
            "### Bài 72. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tính chất phép nhân", F("Giao hoán", "a × b = b × a"), F("Kết hợp", "(a × b) × c = a × (b × c)", "5 × 7 × 2 = (5 × 2) × 7 = 70.")),
            G("II. Chia có dư", F("Quan hệ", "Số bị chia = Thương × Số chia + Số dư"), F("Điều kiện", "0 < Số dư < Số chia")),
        ],
        "example": "Đặt tính rồi tính: 14 216 × 5 và 48 567 : 7.",
        "example_answer": "14 216 × 5 = **71 080**.\n48 567 : 7: 48 : 7 = 6 dư 6; hạ 5 → 65 : 7 = 9 dư 2; hạ 6 → 26 : 7 = 3 dư 5; hạ 7 → 57 : 7 = 8 dư 1 → **6938 (dư 1)**.",
        "real_life": "- Tính tiền mua 4 chiếc áo giá 85 000 đồng; chia đều số gạo vào các bao.",
        "quiz": [
            mcq("biet", "20 000 × 3 = ?", ["60 000", "6000", "600 000", "23 000"], 0, "2 chục nghìn × 3 = **60 000**."),
            mcq("biet", "80 000 : 4 = ?", ["2000", "20 000", "200 000", "32 000"], 1, "8 chục nghìn : 4 = 2 chục nghìn = **20 000**."),
            mcq("biet", "12 031 × 3 = ?", ["36 093", "36 033", "36 903", "12 034"], 0, "1×3 = 3; 3×3 = 9; 0×3 = 0; 2×3 = 6; 1×3 = 3 → **36 093**."),
            mcq("biet", "Tính chất (a × b) × c = a × (b × c) gọi là:", ["Giao hoán", "Kết hợp", "Phân phối", "Chia hết"], 1, "Đó là tính chất **kết hợp** của phép nhân."),
            mcq("hieu", "18 245 × 4 = ?", ["72 980", "72 880", "73 980", "62 980"], 0, "5×4 = 20 (viết 0 nhớ 2); 4×4 + 2 = 18 (8 nhớ 1); 2×4 + 1 = 9; 8×4 = 32 (2 nhớ 3); 1×4 + 3 = 7 → **72 980**."),
            mcq("hieu", "24 036 : 6 = ?", ["4006", "406", "4060", "460"], 0, "24 : 6 = 4; hạ 0 → 0; hạ 3 → 0 (3 < 6); hạ 36 → 6 → **4006**.", note="Mỗi lượt chưa đủ chia phải viết 0."),
            tf("hieu", "Nhận định: “15 000 × 6 = 90 000.”", True, "15 nghìn × 6 = 90 nghìn → **Đúng**."),
            tf("hieu", "Nhận định: “Phép chia 32 157 : 4 có số dư là 5.”", False, "Số dư phải bé hơn 4; thực tế 32 157 : 4 = 8039 dư 1 → **Sai**."),
            mcq("vandung", "Một xe chở 4 chuyến, mỗi chuyến 12 500 kg hàng. Xe đã chở tất cả:", ["50 000 kg", "48 000 kg", "16 500 kg", "45 000 kg"], 0, "12 500 × 4 = **50 000 kg**."),
            short("vandung", "Có 45 650 quyển vở chia đều cho 5 trường. Hỏi mỗi trường nhận được bao nhiêu quyển vở?", ["9130", "9 130"],
                  "45 650 : 5: 45 : 5 = 9; 6 : 5 = 1 dư 1; 15 : 5 = 3; 0 : 5 = 0 → 9130.\nĐáp số: **9130 quyển**.", unit="quyển"),
        ],
    },
    # ===================== CHỦ ĐỀ 15 =====================
    {
        "topic": "l3-cd15-thong-ke-xac-suat",
        "title": "Làm quen với yếu tố thống kê, xác suất",
        "icon": "📊",
        "description": "Chủ đề 15 · SGK Toán 3 tập hai (tr. 103–111): Bài 73 – Bài 75. Thu thập, phân loại, ghi chép số liệu; bảng số liệu; khả năng xảy ra của một sự kiện; thực hành trải nghiệm.",
        "requirements": [
            "Nhận biết được cách thu thập, phân loại, ghi chép số liệu thống kê theo các tiêu chí cho trước.",
            "Đọc và mô tả được các số liệu ở dạng bảng; nêu được một số nhận xét đơn giản từ bảng số liệu.",
            "Nhận biết và mô tả được các khả năng xảy ra (có tính ngẫu nhiên) của một sự kiện khi thực hiện 1 lần thí nghiệm đơn giản.",
        ],
        "definition": (
            "- **Bảng số liệu**: trình bày số liệu theo hàng, cột (tên đối tượng – số lượng).\n"
            "- **Khả năng xảy ra**: liệt kê mọi kết quả có thể có. Tung 1 đồng xu: có **2 khả năng** — mặt sấp hoặc mặt ngửa. Lấy 1 bóng từ hộp có bóng xanh và đỏ: 2 khả năng — xanh hoặc đỏ."
        ),
        "theory": (
            "### Bài 73. Thu thập, phân loại, ghi chép số liệu. Bảng số liệu\n- Lập bảng số bạn thích từng môn thể thao; đọc bảng: nhiều nhất, ít nhất, tổng.\n"
            "### Bài 74. Khả năng xảy ra của một sự kiện\n- Gieo xúc xắc: 6 khả năng (1 → 6 chấm).\n"
            "### Bài 75. Thực hành và trải nghiệm thu thập, phân loại, ghi chép số liệu, đọc bảng số liệu"
        ),
        "formulas": [
            G("I. Thống kê", F("Quy trình", "Thu thập → Phân loại → Ghi chép → Lập bảng → Nhận xét")),
            G("II. Khả năng", F("Đồng xu", "2 khả năng: sấp / ngửa"), F("Xúc xắc", "6 khả năng: 1, 2, 3, 4, 5, 6 chấm")),
        ],
        "example": "Bảng số cây trồng: Lớp 3A: 25 cây; 3B: 30 cây; 3C: 28 cây. Lớp nào trồng nhiều nhất? Cả ba lớp trồng bao nhiêu cây?",
        "example_answer": "Lớp **3B** trồng nhiều nhất (30 cây). Tổng: 25 + 30 + 28 = **83** cây.",
        "real_life": "- Thống kê điểm thi đua, số sách thư viện; tung đồng xu chọn đội giao bóng.",
        "quiz": [
            mcq("biet", "Tung một đồng xu, có mấy khả năng xảy ra về mặt xuất hiện?", ["1", "2", "3", "6"], 1, "Mặt sấp hoặc mặt ngửa → **2** khả năng."),
            mcq("biet", "Gieo một con xúc xắc, có mấy khả năng về số chấm xuất hiện?", ["2", "4", "6", "12"], 2, "Từ 1 đến 6 chấm → **6** khả năng."),
            mcq("biet", "Bảng: Táo 12, Cam 9, Xoài 15 (số bạn thích). Loại quả được thích nhiều nhất là:", ["Táo", "Cam", "Xoài", "Bằng nhau"], 2, "15 lớn nhất → **Xoài**."),
            mcq("biet", "Theo bảng trên, số bạn thích Cam là:", ["12", "9", "15", "36"], 1, "Đọc hàng Cam: **9** bạn."),
            mcq("hieu", "Theo bảng trên (Táo 12, Cam 9, Xoài 15), số bạn thích Xoài nhiều hơn số bạn thích Cam là:", ["3", "6", "24", "27"], 1, "15 − 9 = **6** bạn."),
            mcq("hieu", "Hộp có 3 bóng xanh, 2 bóng đỏ. Lấy ra 1 quả, các khả năng xảy ra là:", ["Chỉ bóng xanh", "Chỉ bóng đỏ", "Bóng xanh hoặc bóng đỏ", "Bóng vàng"], 2, "Hộp có hai màu → có thể lấy **xanh hoặc đỏ**."),
            tf("hieu", "Nhận định: “Theo bảng (Táo 12, Cam 9, Xoài 15), có tất cả 36 bạn được hỏi.”", True, "12 + 9 + 15 = 36 → **Đúng**."),
            tf("hieu", "Nhận định: “Tung đồng xu một lần thì chắc chắn được mặt ngửa.”", False, "Có 2 khả năng (sấp hoặc ngửa) nên không chắc chắn → **Sai**."),
            mcq("vandung", "Bảng số học sinh: Khối 3: 124 em; Khối 4: 118 em; Khối 5: 130 em. Khối 5 nhiều hơn khối 4 bao nhiêu em?", ["6", "12", "248", "8"], 1, "130 − 118 = **12** em."),
            short("vandung", "Trong hộp có 4 thẻ ghi số 1, 2, 3, 4. Rút 1 thẻ. Có bao nhiêu khả năng rút được thẻ ghi số chẵn?", ["2"],
                  "Các số chẵn là 2 và 4 → **2** khả năng."),
        ],
    },
    # ===================== CHỦ ĐỀ 16 =====================
    {
        "topic": "l3-cd16-on-tap-cuoi-nam",
        "title": "Ôn tập cuối năm",
        "icon": "🏁",
        "description": "Chủ đề 16 · SGK Toán 3 tập hai (tr. 112–126): Bài 76 – Bài 81. Ôn tập các số trong phạm vi 10 000, 100 000; cộng, trừ, nhân, chia trong phạm vi 100 000; hình học và đo lường; bảng số liệu, khả năng xảy ra.",
        "requirements": [
            "Củng cố đọc, viết, so sánh, làm tròn các số trong phạm vi 100 000; chữ số La Mã đến 20.",
            "Thực hiện thành thạo bốn phép tính trong phạm vi 100 000; tính giá trị biểu thức; tìm thành phần chưa biết.",
            "Tính chu vi, diện tích hình chữ nhật, hình vuông; đổi đơn vị đo độ dài, khối lượng, dung tích, thời gian, tiền.",
            "Đọc bảng số liệu; mô tả khả năng xảy ra; giải bài toán có đến hai bước tính.",
        ],
        "definition": (
            "- Số đến 100 000: so sánh từ hàng cao nhất; làm tròn theo quy tắc 5.\n"
            "- Biểu thức: ( ) → × : → + −.\n"
            "- Chu vi HCN (a + b) × 2; diện tích HCN a × b; hình vuông: 4 × a và a × a."
        ),
        "theory": (
            "### Bài 76. Ôn tập các số trong phạm vi 10 000, 100 000\n"
            "### Bài 77. Ôn tập phép cộng, phép trừ trong phạm vi 100 000\n"
            "### Bài 78. Ôn tập phép nhân, phép chia trong phạm vi 100 000\n"
            "### Bài 79. Ôn tập hình học và đo lường\n"
            "### Bài 80. Ôn tập bảng số liệu, khả năng xảy ra của một sự kiện\n"
            "### Bài 81. Ôn tập chung"
        ),
        "formulas": [
            G("I. Số và phép tính", F("Thứ tự", "( ) → × : → + −"), F("Chia có dư", "SBC = Thương × SC + dư")),
            G("II. Hình học – đo lường", F("Hình chữ nhật", "P = (a + b) × 2 · S = a × b"), F("Hình vuông", "P = a × 4 · S = a × a"),
              F("Đổi đơn vị", "1 m = 1000 mm · 1 kg = 1000 g · 1 l = 1000 ml · 1 giờ = 60 phút")),
        ],
        "example": "Tính giá trị biểu thức: (12 500 + 7500) × 3.",
        "example_answer": "Trong ngoặc trước: 12 500 + 7500 = 20 000; 20 000 × 3 = **60 000**.",
        "real_life": "- Lập dự toán chi phí chuyến dã ngoại của lớp; tính diện tích lớp học để mua thảm.",
        "quiz": [
            mcq("biet", "Số XVII viết bằng chữ số thường là:", ["17", "12", "15", "22"], 0, "X + V + I + I = 10 + 5 + 2 = **17**."),
            mcq("biet", "Làm tròn 47 500 đến hàng chục nghìn được:", ["40 000", "50 000", "47 000", "48 000"], 1, "Hàng nghìn là 7 ≥ 5 → **50 000**."),
            mcq("biet", "Diện tích hình vuông cạnh 9 cm là:", ["36 cm²", "81 cm²", "18 cm²", "81 cm"], 1, "9 × 9 = **81 cm²**."),
            mcq("biet", "5 l = … ml?", ["50", "500", "5000", "50 000"], 2, "1 l = 1000 ml → **5000 ml**."),
            mcq("hieu", "Giá trị của 36 000 : 6 + 4000 là:", ["10 000", "3600", "4600", "40 000"], 0, "Chia trước: 36 000 : 6 = 6000; 6000 + 4000 = **10 000**."),
            mcq("hieu", "Hình chữ nhật có chiều dài 15 m, chiều rộng 8 m có chu vi là:", ["46 m", "120 m", "23 m", "46 m²"], 0, "(15 + 8) × 2 = **46 m**."),
            tf("hieu", "Nhận định: “35 728 < 35 782.”", True, "Cùng 35 7..; hàng chục 2 < 8 → **Đúng**."),
            tf("hieu", "Nhận định: “Tìm x: x : 4 = 2500 thì x = 625.”", False, "Số bị chia = 2500 × 4 = 10 000; 625 là 2500 : 4 → **Sai**."),
            mcq("vandung", "Một mảnh đất hình chữ nhật dài 25 m, rộng 12 m. Người ta rào xung quanh, chừa 2 m làm cổng. Hàng rào dài:", ["74 m", "72 m", "300 m", "37 m"], 1,
                "Chu vi: (25 + 12) × 2 = 74 (m). Trừ cổng: 74 − 2 = **72 m**."),
            short("vandung", "Mua 3 quyển sách, mỗi quyển giá 24 500 đồng. Đưa người bán tờ 100 000 đồng thì được trả lại bao nhiêu đồng?", ["26500", "26 500"],
                  "Tiền sách: 24 500 × 3 = 73 500 (đồng). Tiền trả lại: 100 000 − 73 500 = 26 500 (đồng).\nĐáp số: **26 500 đồng**.", unit="đồng"),
        ],
    },
]
