"""TOÁN 2 — Kết nối tri thức với cuộc sống (tập một, tập hai).

14 chủ đề đánh số trong SGK, đúng thứ tự mục lục.
Mỗi chủ đề: Yêu cầu cần đạt (CT GDPT 2018), kiến thức theo từng bài, công thức/quy tắc,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf

GRADE = 2

LESSONS = [
    # ===================== CHỦ ĐỀ 1 =====================
    {
        "topic": "l2-cd01-on-tap-va-bo-sung",
        "title": "Ôn tập và bổ sung",
        "icon": "🔁",
        "description": "Chủ đề 1 · SGK Toán 2 tập một (tr. 6–25): Bài 1 – Bài 6. Ôn các số đến 100, tia số, số liền trước – liền sau, thành phần phép cộng, phép trừ, bài toán hơn – kém nhau bao nhiêu.",
        "requirements": [
            "Đếm, đọc, viết, so sánh được các số trong phạm vi 100.",
            "Nhận biết được tia số và viết được số thích hợp trên tia số; nhận biết được số liền trước, số liền sau của một số.",
            "Nhận biết được các thành phần của phép cộng (số hạng, tổng), phép trừ (số bị trừ, số trừ, hiệu).",
            "Thực hiện được phép cộng, phép trừ (không nhớ) trong phạm vi 100.",
            "Giải được bài toán có một bước tính về “hơn, kém nhau bao nhiêu”.",
        ],
        "definition": (
            "- **Số có hai chữ số** gồm chục và đơn vị: 47 gồm 4 chục và 7 đơn vị, viết 47 = 40 + 7.\n"
            "- **Tia số**: các số được ghi lần lượt, cách đều nhau trên một tia, số bên trái bé hơn số bên phải.\n"
            "- **Số liền trước** của một số thì bé hơn số đó 1 đơn vị; **số liền sau** thì lớn hơn số đó 1 đơn vị.\n"
            "- **Phép cộng**: số hạng + số hạng = **tổng**. **Phép trừ**: số bị trừ − số trừ = **hiệu**."
        ),
        "theory": (
            "### Bài 1. Ôn tập các số đến 100\n"
            "- Đọc, viết số theo chục và đơn vị; so sánh hai số: so sánh hàng chục trước, nếu bằng nhau thì so sánh hàng đơn vị.\n"
            "### Bài 2. Tia số. Số liền trước, số liền sau\n"
            "- Điền số còn thiếu trên tia số; số liền trước của 40 là 39, số liền sau của 40 là 41.\n"
            "### Bài 3. Các thành phần của phép cộng, phép trừ\n"
            "- 25 + 13 = 38: 25 và 13 là **số hạng**, 38 là **tổng** (25 + 13 cũng gọi là tổng).\n"
            "- 38 − 13 = 25: 38 là **số bị trừ**, 13 là **số trừ**, 25 là **hiệu**.\n"
            "### Bài 4. Hơn, kém nhau bao nhiêu\n"
            "- Muốn biết số lớn hơn số bé bao nhiêu (hay số bé kém số lớn bao nhiêu) ta lấy **số lớn trừ số bé**.\n"
            "### Bài 5. Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi 100\n"
            "- Đặt tính thẳng cột: đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang trái.\n"
            "### Bài 6. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cấu tạo số", F("Số có hai chữ số", "ab = a chục + b đơn vị", "Ví dụ: 63 = 60 + 3."),
              F("Liền trước – liền sau", "Số liền trước = số đó − 1 · Số liền sau = số đó + 1", "Liền trước 70 là 69; liền sau 70 là 71.")),
            G("II. Thành phần phép tính", F("Phép cộng", "Số hạng + Số hạng = Tổng"),
              F("Phép trừ", "Số bị trừ − Số trừ = Hiệu"),
              F("Hơn, kém nhau bao nhiêu", "Số lớn − Số bé = phần hơn (kém)", "An 12 tuổi, em 7 tuổi: An hơn em 12 − 7 = 5 tuổi.")),
        ],
        "example": "Lớp 2A có 35 bạn, lớp 2B có 32 bạn. Lớp 2A nhiều hơn lớp 2B bao nhiêu bạn?",
        "example_answer": "Muốn biết hơn bao nhiêu, lấy số lớn trừ số bé: 35 − 32 = **3** (bạn).\nĐáp số: 3 bạn.",
        "real_life": "- Đọc số nhà, số trang sách, số ghế trong rạp.\n- So sánh chiều cao, số tuổi: “Em kém anh mấy tuổi?”.",
        "quiz": [
            mcq("biet", "Số gồm 7 chục và 4 đơn vị là:", ["47", "74", "704", "11"], 1,
                "7 chục là 70, thêm 4 đơn vị: 70 + 4 = **74**.", note="Chữ số hàng chục viết trước (bên trái)."),
            mcq("biet", "Số liền sau của 59 là:", ["58", "50", "60", "69"], 2,
                "Số liền sau lớn hơn 1 đơn vị: 59 + 1 = **60**."),
            mcq("biet", "Trong phép cộng 42 + 15 = 57, số 57 được gọi là:", ["Số hạng", "Tổng", "Hiệu", "Số trừ"], 1,
                "Kết quả của phép cộng gọi là **tổng**."),
            mcq("biet", "Trong phép trừ 68 − 23 = 45, số bị trừ là:", ["68", "23", "45", "91"], 0,
                "Số đứng trước dấu “−” là **số bị trừ**: 68.", note="23 là số trừ, 45 là hiệu."),
            mcq("hieu", "Trên tia số, các số 30, 40, ?, 60 cách đều nhau. Số còn thiếu là:", ["45", "50", "55", "41"], 1,
                "Mỗi vạch tăng 10 đơn vị: 30, 40, **50**, 60."),
            mcq("hieu", "Tổng của 34 và 25 là:", ["59", "9", "58", "69"], 0,
                "Tổng là kết quả phép cộng: 34 + 25 = **59** (4 + 5 = 9; 3 + 2 = 5)."),
            tf("hieu", "Nhận định: “86 > 68.”", True,
               "So sánh hàng chục: 8 chục > 6 chục nên 86 > 68 → **Đúng**."),
            tf("hieu", "Nhận định: “Hiệu của 75 và 30 là 105.”", False,
               "Hiệu là kết quả phép trừ: 75 − 30 = 45, không phải 105 (105 là tổng) → **Sai**."),
            mcq("vandung", "Bình cao 98 cm, em Bình cao 86 cm. Bình cao hơn em bao nhiêu xăng-ti-mét?", ["12 cm", "184 cm", "2 cm", "14 cm"], 0,
                "Lấy số lớn trừ số bé: 98 − 86 = **12** (cm).", note="“Cao hơn bao nhiêu” là phép trừ, không phải phép cộng."),
            short("vandung", "Mẹ năm nay 36 tuổi, Lan 9 tuổi... Lan kém mẹ bao nhiêu tuổi?", ["27"],
                  "Số lớn − số bé: 36 − 9 = 27 (tuổi).\nĐáp số: **27 tuổi**.", unit="tuổi",
                  alt="Đếm thêm từ 9 lên 36: 9 → 10 (1), 10 → 36 (26) → 1 + 26 = 27."),
        ],
    },
    # ===================== CHỦ ĐỀ 2 =====================
    {
        "topic": "l2-cd02-cong-tru-pham-vi-20",
        "title": "Phép cộng, phép trừ trong phạm vi 20",
        "icon": "➕",
        "description": "Chủ đề 2 · SGK Toán 2 tập một (tr. 26–56): Bài 7 – Bài 14. Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.",
        "requirements": [
            "Thực hiện được phép cộng (qua 10), phép trừ (qua 10) trong phạm vi 20; cộng, trừ nhẩm trong phạm vi 20.",
            "Thuộc và vận dụng được bảng cộng (qua 10), bảng trừ (qua 10).",
            "Thực hiện được tính toán khi có hai dấu phép tính cộng, trừ (từ trái sang phải).",
            "Giải được bài toán một bước tính về thêm, bớt một số đơn vị; về nhiều hơn, ít hơn một số đơn vị.",
        ],
        "definition": (
            "- **Cộng qua 10**: tổng vượt quá 10, ví dụ 8 + 5 = 13.\n"
            "- **Trừ qua 10**: số bị trừ lớn hơn 10, phải “trừ qua” chục, ví dụ 13 − 5 = 8.\n"
            "- **Thêm / nhiều hơn** → làm phép cộng; **bớt / ít hơn** → làm phép trừ."
        ),
        "theory": (
            "### Bài 7. Phép cộng (qua 10) trong phạm vi 20\n"
            "- **Tách để làm tròn 10**: 8 + 5 → 8 + 2 = 10, 10 + 3 = 13.\n"
            "### Bài 8. Bảng cộng (qua 10)\n"
            "- 9 + 2 … 9 + 9; 8 + 3 … 8 + 9; …; 2 + 9. Đổi chỗ các số hạng tổng không đổi.\n"
            "### Bài 9. Bài toán về thêm, bớt một số đơn vị\n"
            "- Thêm → cộng; bớt → trừ. Trình bày: Bài giải – phép tính – đáp số.\n"
            "### Bài 10. Luyện tập chung\n"
            "### Bài 11. Phép trừ (qua 10) trong phạm vi 20\n"
            "- **Trừ để được 10 rồi trừ tiếp**: 13 − 5 → 13 − 3 = 10, 10 − 2 = 8.\n"
            "- Hoặc dựa vào phép cộng: 8 + 5 = 13 nên 13 − 5 = 8.\n"
            "### Bài 12. Bảng trừ (qua 10)\n"
            "### Bài 13. Bài toán về nhiều hơn, ít hơn một số đơn vị\n"
            "- “Nhiều hơn 3” → cộng 3; “ít hơn 3” → trừ 3.\n"
            "### Bài 14. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cộng qua 10", F("Tách làm tròn 10", "8 + 5 = 8 + 2 + 3 = 10 + 3 = 13"),
              F("Đổi chỗ số hạng", "a + b = b + a", "7 + 6 = 6 + 7 = 13."),
              F("Các tổng bằng 11", "9 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11")),
            G("II. Trừ qua 10", F("Trừ về 10", "14 − 6 = 14 − 4 − 2 = 10 − 2 = 8"),
              F("Dựa vào phép cộng", "Nếu a + b = c thì c − a = b, c − b = a", "9 + 6 = 15 → 15 − 9 = 6; 15 − 6 = 9.")),
            G("III. Giải toán có lời văn", F("Thêm / Nhiều hơn", "Số đã có + số thêm (nhiều hơn)"),
              F("Bớt / Ít hơn", "Số đã có − số bớt (ít hơn)"),
              F("Hai dấu phép tính", "Tính lần lượt từ trái sang phải", "9 + 5 − 6 = 14 − 6 = 8.")),
        ],
        "example": "Tổ Một có 9 bạn, tổ Hai nhiều hơn tổ Một 3 bạn. Hỏi tổ Hai có bao nhiêu bạn?",
        "example_answer": "“Nhiều hơn 3 bạn” → làm phép cộng: 9 + 3 = **12** (bạn).\nĐáp số: 12 bạn.",
        "real_life": "- Tính nhẩm số bút, số kẹo khi được cho thêm hoặc cho bớt.\n- Chia đồ chơi: “Em có ít hơn anh 4 viên bi”.",
        "quiz": [
            mcq("biet", "8 + 6 = ?", ["13", "14", "15", "12"], 1, "Tách 6 = 2 + 4: 8 + 2 = 10, 10 + 4 = **14**."),
            mcq("biet", "15 − 7 = ?", ["8", "9", "7", "22"], 0, "Vì 7 + 8 = 15 nên 15 − 7 = **8**.", note="22 là kết quả của phép cộng 15 + 7."),
            mcq("biet", "Phép tính nào có kết quả bằng 11?", ["9 + 3", "7 + 4", "6 + 6", "8 + 2"], 1,
                "7 + 4 = **11**; 9 + 3 = 12; 6 + 6 = 12; 8 + 2 = 10."),
            mcq("biet", "Bài toán “nhiều hơn một số đơn vị” thường giải bằng phép tính:", ["Phép cộng", "Phép trừ", "Phép nhân", "Phép chia"], 0,
                "“Nhiều hơn” nghĩa là thêm vào → **phép cộng**."),
            mcq("hieu", "Tính: 9 + 4 − 5 = ?", ["8", "18", "0", "10"], 0,
                "Tính từ trái sang phải: 9 + 4 = 13; 13 − 5 = **8**."),
            mcq("hieu", "Biết 7 + 9 = 16. Phép trừ nào đúng?", ["16 − 9 = 6", "16 − 7 = 9", "9 − 7 = 16", "16 − 16 = 7"], 1,
                "Từ 7 + 9 = 16 suy ra 16 − 7 = 9 và 16 − 9 = 7. Phép tính đúng: **16 − 7 = 9**."),
            tf("hieu", "Nhận định: “6 + 8 = 8 + 6.”", True, "Đổi chỗ các số hạng thì tổng không đổi: cả hai bằng 14 → **Đúng**."),
            tf("hieu", "Nhận định: “12 − 4 = 9.”", False, "12 − 2 = 10, 10 − 2 = 8. Vậy 12 − 4 = 8 → **Sai**."),
            mcq("vandung", "Cành trên có 13 con chim, cành dưới ít hơn cành trên 5 con. Cành dưới có bao nhiêu con chim?", ["18", "8", "7", "9"], 1,
                "“Ít hơn 5 con” → phép trừ: 13 − 5 = **8** (con chim).", note="Chọn 18 là nhầm sang phép cộng."),
            short("vandung", "Mai có 8 bông hoa, Mai được bạn tặng thêm 7 bông nữa. Hỏi Mai có tất cả bao nhiêu bông hoa?", ["15"],
                  "Thêm → cộng: 8 + 7 = 15 (bông hoa).\nĐáp số: **15 bông hoa**.", unit="bông hoa",
                  alt="7 + 8: tách 8 = 3 + 5 → 7 + 3 = 10, 10 + 5 = 15."),
        ],
    },
    # ===================== CHỦ ĐỀ 3 =====================
    {
        "topic": "l2-cd03-khoi-luong-dung-tich",
        "title": "Làm quen với khối lượng, dung tích",
        "icon": "⚖️",
        "description": "Chủ đề 3 · SGK Toán 2 tập một (tr. 57–71): Bài 15 – Bài 18. Nặng hơn – nhẹ hơn, ki-lô-gam (kg), lít (l), thực hành cân, đong.",
        "requirements": [
            "Nhận biết được “nặng hơn”, “nhẹ hơn”.",
            "Nhận biết được đơn vị đo khối lượng ki-lô-gam (kg); đọc, viết được số đo khối lượng.",
            "Nhận biết được đơn vị đo dung tích lít (l); đọc, viết được số đo dung tích.",
            "Sử dụng được cân, ca 1 lít để thực hành cân, đong; tính toán với các số đo kg, l.",
            "Giải quyết được vấn đề thực tiễn đơn giản liên quan đến khối lượng, dung tích.",
        ],
        "definition": (
            "- **Ki-lô-gam** là đơn vị đo khối lượng (độ nặng), viết tắt **kg**.\n"
            "- **Lít** là đơn vị đo dung tích (lượng chất lỏng chứa được), viết tắt **l**.\n"
            "- Cân đĩa: đĩa nào thấp hơn thì vật trên đó **nặng hơn**; hai đĩa thăng bằng thì hai vật **nặng bằng nhau**."
        ),
        "theory": (
            "### Bài 15. Ki-lô-gam\n"
            "- So sánh nặng hơn, nhẹ hơn bằng tay hoặc bằng cân đĩa; đọc số đo trên cân: 2 kg, 5 kg.\n"
            "- Cộng, trừ số đo khối lượng: 3 kg + 5 kg = 8 kg (giữ nguyên đơn vị).\n"
            "### Bài 16. Lít\n"
            "- Ca 1 lít, chai 1 lít; đọc, viết: 1 l, 2 l, 10 l. Cộng trừ: 5 l − 2 l = 3 l.\n"
            "### Bài 17. Thực hành và trải nghiệm với các đơn vị ki-lô-gam, lít\n"
            "- Cân đồ vật, đong nước, ước lượng xem đồ vật nặng khoảng bao nhiêu ki-lô-gam.\n"
            "### Bài 18. Luyện tập chung"
        ),
        "formulas": [
            G("I. Đơn vị đo", F("Khối lượng", "ki-lô-gam: kg", "Bao gạo 10 kg."),
              F("Dung tích", "lít: l", "Can nước 5 l.")),
            G("II. Tính với số đo", F("Cộng, trừ cùng đơn vị", "a kg ± b kg = (a ± b) kg", "12 kg − 4 kg = 8 kg."),
              F("Cân đĩa thăng bằng", "Khối lượng đĩa trái = Khối lượng đĩa phải", "Bên trái: quả bí; bên phải: 2 kg + 1 kg → bí nặng 3 kg.")),
        ],
        "example": "Can thứ nhất có 8 l nước, can thứ hai có 5 l nước. Cả hai can có bao nhiêu lít nước?",
        "example_answer": "Gộp lại → cộng: 8 l + 5 l = **13 l**.\nĐáp số: 13 l nước.",
        "real_life": "- Mua 2 kg gạo, 1 l sữa; đọc số ki-lô-gam trên cân ở chợ.\n- Đổ đầy bình nước 5 l, tính xem cần mấy ca 1 l.",
        "quiz": [
            mcq("biet", "Ki-lô-gam viết tắt là:", ["kl", "kg", "l", "g"], 1, "Ki-lô-gam viết tắt là **kg**."),
            mcq("biet", "Đơn vị nào dùng để đo lượng nước trong can?", ["ki-lô-gam", "xăng-ti-mét", "lít", "giờ"], 2,
                "Lượng chất lỏng đo bằng **lít (l)**."),
            mcq("biet", "Cân đĩa: đĩa đựng quả dưa thấp xuống, đĩa đựng quả cam cao lên. Vậy:", ["Quả dưa nhẹ hơn quả cam", "Quả dưa nặng hơn quả cam", "Hai quả nặng bằng nhau", "Không so sánh được"], 1,
                "Đĩa thấp hơn chứa vật **nặng hơn** → quả dưa nặng hơn quả cam."),
            mcq("biet", "Đọc số đo “7 l”:", ["Bảy ki-lô-gam", "Bảy lít", "Bảy mét", "Bảy xăng-ti-mét"], 1, "“l” là lít → đọc là **bảy lít**."),
            mcq("hieu", "15 kg − 6 kg = ?", ["9 kg", "21 kg", "9 l", "11 kg"], 0, "15 − 6 = 9, giữ nguyên đơn vị → **9 kg**."),
            mcq("hieu", "Cân thăng bằng: đĩa trái có túi đường, đĩa phải có quả cân 2 kg và quả cân 1 kg. Túi đường nặng:", ["2 kg", "1 kg", "3 kg", "4 kg"], 2,
                "Cân thăng bằng nên túi đường nặng bằng 2 kg + 1 kg = **3 kg**."),
            tf("hieu", "Nhận định: “4 l + 9 l = 13 l.”", True, "4 + 9 = 13, giữ đơn vị lít → 13 l → **Đúng**."),
            tf("hieu", "Nhận định: “Vật to hơn thì luôn nặng hơn vật nhỏ.”", False,
               "Không đúng: quả bóng bay to nhưng rất nhẹ, hòn bi sắt nhỏ nhưng nặng hơn → **Sai**. Muốn biết nặng hơn phải cân."),
            mcq("vandung", "Thùng có 16 l nước. Mẹ đã dùng 7 l. Thùng còn lại bao nhiêu lít nước?", ["23 l", "9 l", "8 l", "7 l"], 1,
                "Đã dùng → bớt đi: 16 − 7 = **9** (l)."),
            short("vandung", "Bao gạo nặng 25 kg, bao ngô nhẹ hơn bao gạo 4 kg. Bao ngô nặng bao nhiêu ki-lô-gam?", ["21", "21kg"],
                  "“Nhẹ hơn 4 kg” → trừ: 25 − 4 = 21 (kg).\nĐáp số: **21 kg**.", unit="kg"),
        ],
    },
    # ===================== CHỦ ĐỀ 4 =====================
    {
        "topic": "l2-cd04-cong-tru-co-nho-pham-vi-100",
        "title": "Phép cộng, phép trừ (có nhớ) trong phạm vi 100",
        "icon": "🧮",
        "description": "Chủ đề 4 · SGK Toán 2 tập một (tr. 72–97): Bài 19 – Bài 24. Cộng, trừ có nhớ số có hai chữ số với số có một hoặc hai chữ số.",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ (có nhớ không quá một lượt) các số trong phạm vi 100.",
            "Đặt tính đúng: các chữ số cùng hàng thẳng cột; tính từ phải sang trái và nhớ đúng.",
            "Tính toán được trong trường hợp có hai dấu phép tính cộng, trừ.",
            "Giải được bài toán thực tế một bước tính liên quan đến cộng, trừ có nhớ.",
        ],
        "definition": (
            "- **Cộng có nhớ**: hàng đơn vị cộng được từ 10 trở lên, viết chữ số đơn vị và **nhớ 1** sang hàng chục.\n"
            "- **Trừ có nhớ**: chữ số đơn vị ở số bị trừ bé hơn ở số trừ, ta **mượn 1 chục** (lấy thêm 10), rồi **trả 1** ở hàng chục số trừ."
        ),
        "theory": (
            "### Bài 19. Phép cộng (có nhớ) số có hai chữ số với số có một chữ số\n"
            "- 37 + 5: 7 + 5 = 12, viết 2 nhớ 1; 3 thêm 1 bằng 4 → 42.\n"
            "### Bài 20. Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số\n"
            "- 46 + 28: 6 + 8 = 14, viết 4 nhớ 1; 4 + 2 = 6, thêm 1 bằng 7 → 74.\n"
            "### Bài 21. Luyện tập chung\n"
            "### Bài 22. Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số\n"
            "- 42 − 7: 2 không trừ được 7, lấy 12 − 7 = 5, viết 5 nhớ 1; 4 − 1 = 3 → 35.\n"
            "### Bài 23. Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số\n"
            "- 63 − 28: 13 − 8 = 5, viết 5 nhớ 1; 2 thêm 1 bằng 3, 6 − 3 = 3 → 35.\n"
            "### Bài 24. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cộng có nhớ", F("Quy tắc", "Cộng đơn vị ≥ 10 → viết đơn vị, nhớ 1 sang hàng chục", "58 + 7 = 65."),
              F("Ví dụ hai chữ số", "46 + 28 = 74", "6 + 8 = 14 viết 4 nhớ 1; 4 + 2 + 1 = 7.")),
            G("II. Trừ có nhớ", F("Quy tắc", "Đơn vị không trừ được → mượn 10, rồi trả 1 ở hàng chục số trừ", "52 − 8 = 44."),
              F("Ví dụ hai chữ số", "63 − 28 = 35", "13 − 8 = 5; 2 + 1 = 3; 6 − 3 = 3.")),
            G("III. Kiểm tra", F("Thử lại phép trừ", "Hiệu + Số trừ = Số bị trừ", "35 + 28 = 63 ✔"),
              F("Thử lại phép cộng", "Tổng − Số hạng này = Số hạng kia")),
        ],
        "example": "Đặt tính rồi tính: a) 37 + 25;  b) 81 − 46.",
        "example_answer": "a) 7 + 5 = 12, viết 2 nhớ 1; 3 + 2 = 5, thêm 1 bằng 6 → **62**.\nb) 1 không trừ được 6, lấy 11 − 6 = 5, viết 5 nhớ 1; 4 thêm 1 bằng 5, 8 − 5 = 3 → **35**.\nThử lại: 35 + 46 = 81 ✔.",
        "real_life": "- Tính tổng số học sinh hai lớp, số trang sách đã đọc.\n- Tính số tiền còn lại (đơn vị nghìn đồng) khi mua hàng.",
        "quiz": [
            mcq("biet", "36 + 8 = ?", ["44", "34", "116", "43"], 0, "6 + 8 = 14, viết 4 nhớ 1; 3 + 1 = 4 → **44**."),
            mcq("biet", "50 − 6 = ?", ["56", "44", "46", "54"], 1, "0 không trừ được 6: 10 − 6 = 4, viết 4 nhớ 1; 5 − 1 = 4 → **44**."),
            mcq("biet", "Khi đặt tính phép cộng hai số có hai chữ số, ta tính:", ["Từ trái sang phải", "Từ phải sang trái (từ hàng đơn vị)", "Hàng chục trước", "Tuỳ ý"], 1,
                "Luôn tính từ **hàng đơn vị** (bên phải) để biết có nhớ hay không."),
            mcq("biet", "29 + 47 = ?", ["66", "76", "616", "75"], 1, "9 + 7 = 16, viết 6 nhớ 1; 2 + 4 + 1 = 7 → **76**.",
                note="Quên nhớ 1 sẽ ra 66."),
            mcq("hieu", "72 − 35 = ?", ["47", "37", "43", "33"], 1, "12 − 5 = 7, nhớ 1; 3 + 1 = 4, 7 − 4 = 3 → **37**.\nThử lại: 37 + 35 = 72 ✔."),
            mcq("hieu", "Tính: 45 + 18 − 30 = ?", ["33", "63", "93", "23"], 0, "Từ trái sang phải: 45 + 18 = 63; 63 − 30 = **33**."),
            tf("hieu", "Bạn Na tính 64 − 27 = 43. Nhận định: “Bạn Na tính đúng.”", False,
               "Đúng phải là: 14 − 7 = 7, nhớ 1; 6 − 3 = 3 → 37. Na đã lấy 7 − 4 = 3 (trừ ngược) → **Sai**.",
               note="Không được lấy số dưới trừ số trên ở hàng đơn vị."),
            tf("hieu", "Nhận định: “58 + 26 = 84.”", True, "8 + 6 = 14, viết 4 nhớ 1; 5 + 2 + 1 = 8 → 84 → **Đúng**."),
            mcq("vandung", "Thư viện có 63 quyển truyện, đã cho mượn 28 quyển. Thư viện còn lại bao nhiêu quyển truyện?", ["91", "45", "35", "25"], 2,
                "Cho mượn → bớt đi: 63 − 28 = **35** (quyển)."),
            short("vandung", "Khối lớp Hai có 47 bạn nam và 39 bạn nữ. Hỏi khối lớp Hai có tất cả bao nhiêu bạn?", ["86"],
                  "47 + 39: 7 + 9 = 16, viết 6 nhớ 1; 4 + 3 + 1 = 8 → 86.\nĐáp số: **86 bạn**.", unit="bạn"),
        ],
    },
    # ===================== CHỦ ĐỀ 5 =====================
    {
        "topic": "l2-cd05-lam-quen-hinh-phang",
        "title": "Làm quen với hình phẳng",
        "icon": "📐",
        "description": "Chủ đề 5 · SGK Toán 2 tập một (tr. 98–111): Bài 25 – Bài 28. Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, đường gấp khúc, hình tứ giác, gấp – cắt – ghép hình, vẽ đoạn thẳng.",
        "requirements": [
            "Nhận biết được điểm, đoạn thẳng, đường cong, đường thẳng, đường gấp khúc, ba điểm thẳng hàng.",
            "Nhận dạng được hình tứ giác.",
            "Tính được độ dài đường gấp khúc khi biết độ dài các đoạn thẳng.",
            "Vẽ được đoạn thẳng có độ dài cho trước; thực hiện được gấp, cắt, ghép, xếp hình.",
        ],
        "definition": (
            "- **Đoạn thẳng AB** là đường thẳng nối hai điểm A và B (có hai đầu).\n"
            "- **Đường thẳng** kéo dài mãi về hai phía; **đường cong** không thẳng.\n"
            "- **Ba điểm thẳng hàng** là ba điểm cùng nằm trên một đường thẳng.\n"
            "- **Đường gấp khúc** gồm nhiều đoạn thẳng nối tiếp nhau, không cùng nằm trên một đường thẳng.\n"
            "- **Hình tứ giác** có 4 cạnh và 4 đỉnh (hình vuông, hình chữ nhật cũng là tứ giác)."
        ),
        "theory": (
            "### Bài 25. Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng\n"
            "- Dùng thước kiểm tra ba điểm có thẳng hàng không.\n"
            "### Bài 26. Đường gấp khúc. Hình tứ giác\n"
            "- Đường gấp khúc ABCD gồm các đoạn AB, BC, CD. **Độ dài đường gấp khúc = tổng độ dài các đoạn thẳng.**\n"
            "### Bài 27. Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng\n"
            "- Vẽ đoạn thẳng 5 cm: chấm điểm ở vạch 0, chấm điểm ở vạch 5, nối hai điểm, ghi tên.\n"
            "### Bài 28. Luyện tập chung"
        ),
        "formulas": [
            G("I. Đường gấp khúc", F("Độ dài", "Độ dài đường gấp khúc = tổng độ dài các đoạn thẳng", "AB = 3 cm, BC = 4 cm, CD = 2 cm → 3 + 4 + 2 = 9 cm.")),
            G("II. Nhận dạng", F("Tứ giác", "4 cạnh · 4 đỉnh"),
              F("Ba điểm thẳng hàng", "Cùng nằm trên một đường thẳng (đặt thước kiểm tra)")),
        ],
        "example": "Đường gấp khúc MNPQ có MN = 5 cm, NP = 3 cm, PQ = 6 cm. Tính độ dài đường gấp khúc.",
        "example_answer": "Độ dài = MN + NP + PQ = 5 + 3 + 6 = **14 cm**.",
        "real_life": "- Con đường từ nhà đến trường đi qua nhiều khúc rẽ giống đường gấp khúc.\n- Mặt bàn, khung cửa, viên gạch lát nền có dạng tứ giác.",
        "quiz": [
            mcq("biet", "Hình có 4 cạnh và 4 đỉnh gọi là:", ["Hình tam giác", "Hình tứ giác", "Hình tròn", "Đường gấp khúc"], 1, "4 cạnh, 4 đỉnh → **hình tứ giác**."),
            mcq("biet", "Đường gấp khúc ABC gồm mấy đoạn thẳng?", ["1", "2", "3", "4"], 1, "Đường gấp khúc ABC gồm 2 đoạn thẳng: **AB và BC**."),
            mcq("biet", "Ba điểm thẳng hàng là ba điểm:", ["Cùng nằm trên một đường thẳng", "Cùng nằm trên một đường cong", "Tạo thành hình tam giác", "Cách đều nhau"], 0,
                "Định nghĩa: ba điểm **cùng nằm trên một đường thẳng**."),
            mcq("biet", "Khi vẽ đoạn thẳng dài 6 cm bằng thước, em chấm điểm thứ nhất ở vạch số mấy?", ["1", "0", "6", "10"], 1,
                "Chấm điểm đầu ở **vạch 0**, điểm cuối ở vạch 6 rồi nối lại."),
            mcq("hieu", "Đường gấp khúc có các đoạn dài 4 cm, 5 cm, 3 cm. Độ dài đường gấp khúc là:", ["9 cm", "12 cm", "7 cm", "11 cm"], 1,
                "Cộng độ dài các đoạn: 4 + 5 + 3 = **12 cm**."),
            mcq("hieu", "Hình nào dưới đây KHÔNG phải là hình tứ giác?", ["Hình vuông", "Hình chữ nhật", "Hình tam giác", "Hình có 4 cạnh lệch nhau"], 2,
                "Hình tam giác chỉ có 3 cạnh nên **không** là tứ giác."),
            tf("hieu", "Nhận định: “Hình vuông cũng là một hình tứ giác.”", True, "Hình vuông có 4 cạnh, 4 đỉnh → là tứ giác → **Đúng**."),
            tf("hieu", "Nhận định: “Đoạn thẳng kéo dài mãi về hai phía.”", False,
               "Đoạn thẳng có **hai đầu** (giới hạn bởi 2 điểm). Kéo dài mãi về hai phía là **đường thẳng** → **Sai**."),
            mcq("vandung", "Con kiến bò theo đường gấp khúc gồm 3 đoạn, mỗi đoạn dài 5 cm. Con kiến bò được:", ["8 cm", "15 cm", "10 cm", "53 cm"], 1,
                "5 + 5 + 5 = **15 cm**."),
            short("vandung", "Đường gấp khúc ABCD dài 17 cm, trong đó AB = 6 cm, BC = 4 cm. Tính độ dài đoạn CD (cm).", ["7", "7cm"],
                  "AB + BC = 6 + 4 = 10 (cm). CD = 17 − 10 = 7 (cm).\nĐáp số: **7 cm**.", unit="cm"),
        ],
    },
    # ===================== CHỦ ĐỀ 6 =====================
    {
        "topic": "l2-cd06-ngay-gio-thang",
        "title": "Ngày – giờ, giờ – phút, ngày – tháng",
        "icon": "⏰",
        "description": "Chủ đề 6 · SGK Toán 2 tập một (tr. 112–123): Bài 29 – Bài 32. Một ngày có 24 giờ, một giờ có 60 phút, xem đồng hồ (kim phút chỉ số 3, số 6), ngày – tháng, xem lịch.",
        "requirements": [
            "Nhận biết được một ngày có 24 giờ; một giờ có 60 phút.",
            "Đọc được giờ trên đồng hồ khi kim phút chỉ số 12, số 3, số 6.",
            "Nhận biết được số ngày trong tháng, ngày trong tháng; xem được lịch tháng.",
            "Giải quyết được vấn đề thực tiễn đơn giản về thời gian (thời gian biểu, ngày trong tuần).",
        ],
        "definition": (
            "- **1 ngày = 24 giờ**: từ 12 giờ đêm hôm trước đến 12 giờ đêm hôm sau. Buổi chiều 13 giờ còn gọi là 1 giờ chiều.\n"
            "- **1 giờ = 60 phút**. Kim phút chỉ số 3: **15 phút**; chỉ số 6: **30 phút** (rưỡi).\n"
            "- Tháng có 30 hoặc 31 ngày (tháng Hai có 28 hoặc 29 ngày)."
        ),
        "theory": (
            "### Bài 29. Ngày – giờ, giờ – phút\n"
            "- Các buổi: sáng (1 giờ – 10 giờ), trưa (11 – 12 giờ), chiều (13 – 18 giờ), tối (19 – 21 giờ), đêm (22 – 24 giờ).\n"
            "- 8 giờ 30 phút = 8 giờ rưỡi; 15 giờ = 3 giờ chiều; 20 giờ = 8 giờ tối.\n"
            "### Bài 30. Ngày – tháng\n"
            "- Xem tờ lịch tháng: tháng có bao nhiêu ngày, ngày … là thứ mấy, các ngày thứ Hai trong tháng cách nhau 7 ngày.\n"
            "### Bài 31. Thực hành và trải nghiệm xem đồng hồ, xem lịch\n"
            "### Bài 32. Luyện tập chung"
        ),
        "formulas": [
            G("I. Quan hệ thời gian", F("Ngày – giờ", "1 ngày = 24 giờ"), F("Giờ – phút", "1 giờ = 60 phút"),
              F("Tuần lễ", "1 tuần = 7 ngày", "Thứ Hai tuần này là ngày 5 → thứ Hai tuần sau là ngày 12.")),
            G("II. Đọc giờ", F("Kim phút chỉ 12", "giờ đúng"), F("Kim phút chỉ 3", "… giờ 15 phút"),
              F("Kim phút chỉ 6", "… giờ 30 phút (… giờ rưỡi)"),
              F("Giờ buổi chiều, tối", "13 giờ = 1 giờ chiều · 17 giờ = 5 giờ chiều · 21 giờ = 9 giờ tối", "Lấy số giờ trừ 12.")),
        ],
        "example": "Ngày 3 tháng 6 là thứ Hai. Hỏi ngày 10 tháng 6 là thứ mấy? Ngày 17 tháng 6 là thứ mấy?",
        "example_answer": "Mỗi tuần có 7 ngày: 3 + 7 = 10 → ngày 10 cũng là **thứ Hai**; 10 + 7 = 17 → ngày 17 cũng là **thứ Hai**.",
        "real_life": "- Lập thời gian biểu: 6 giờ 30 phút thức dậy, 7 giờ đi học.\n- Xem lịch để biết ngày sinh nhật, ngày 19 tháng 5 sinh nhật Bác Hồ.",
        "quiz": [
            mcq("biet", "Một ngày có bao nhiêu giờ?", ["12 giờ", "24 giờ", "60 giờ", "7 giờ"], 1, "Một ngày có **24 giờ**."),
            mcq("biet", "Một giờ có bao nhiêu phút?", ["30 phút", "100 phút", "60 phút", "24 phút"], 2, "Một giờ có **60 phút**."),
            mcq("biet", "Kim ngắn chỉ số 9, kim dài chỉ số 6. Đồng hồ chỉ:", ["9 giờ", "9 giờ 30 phút", "6 giờ 9 phút", "9 giờ 15 phút"], 1,
                "Kim dài (kim phút) chỉ số 6 là 30 phút → **9 giờ 30 phút** (9 giờ rưỡi)."),
            mcq("biet", "Tháng Ba có bao nhiêu ngày?", ["30 ngày", "28 ngày", "31 ngày", "29 ngày"], 2, "Tháng Ba có **31 ngày**.",
                alt="Đếm trên nắm tay: các tháng ở đốt lồi (1, 3, 5, 7, 8, 10, 12) có 31 ngày."),
            mcq("hieu", "17 giờ còn gọi là:", ["7 giờ chiều", "5 giờ chiều", "5 giờ sáng", "7 giờ tối"], 1, "17 − 12 = 5 → **5 giờ chiều**."),
            mcq("hieu", "Kim ngắn chỉ giữa số 3 và số 4, kim dài chỉ số 3. Đồng hồ chỉ:", ["3 giờ 15 phút", "4 giờ 15 phút", "3 giờ 3 phút", "3 giờ 30 phút"], 0,
                "Kim ngắn đã qua số 3 (chưa đến 4) → 3 giờ; kim dài chỉ số 3 → 15 phút. Vậy **3 giờ 15 phút**."),
            tf("hieu", "Nhận định: “8 giờ tối còn gọi là 20 giờ.”", True, "8 + 12 = 20 → **Đúng**."),
            tf("hieu", "Ngày 5 tháng 9 là thứ Năm. Nhận định: “Ngày 12 tháng 9 là thứ Sáu.”", False,
               "5 + 7 = 12 → ngày 12 cùng thứ với ngày 5, tức là **thứ Năm** → nhận định **Sai**."),
            mcq("vandung", "Lan bắt đầu làm bài lúc 7 giờ tối và làm xong lúc 8 giờ tối. Lan làm bài trong bao lâu?", ["1 giờ", "15 phút", "30 phút", "2 giờ"], 0,
                "Từ 7 giờ đến 8 giờ là **1 giờ** (60 phút)."),
            short("vandung", "Thứ Hai tuần này là ngày 8. Hỏi thứ Hai tuần sau là ngày bao nhiêu?", ["15"],
                  "Một tuần có 7 ngày: 8 + 7 = 15.\nThứ Hai tuần sau là **ngày 15**."),
        ],
    },
    # ===================== CHỦ ĐỀ 7 =====================
    {
        "topic": "l2-cd07-on-tap-hoc-ki-1",
        "title": "Ôn tập học kì 1",
        "icon": "📝",
        "description": "Chủ đề 7 · SGK Toán 2 tập một (tr. 124–137): Bài 33 – Bài 36. Ôn phép cộng, phép trừ trong phạm vi 20, 100; ôn hình phẳng; ôn đo lường (kg, l, giờ, ngày tháng).",
        "requirements": [
            "Củng cố cộng, trừ nhẩm trong phạm vi 20; cộng, trừ (có nhớ) trong phạm vi 100.",
            "Củng cố nhận biết điểm, đoạn thẳng, đường gấp khúc, tứ giác; tính độ dài đường gấp khúc.",
            "Củng cố các đơn vị kg, l; xem giờ, xem lịch.",
            "Vận dụng giải bài toán có lời văn một bước tính.",
        ],
        "definition": (
            "Chủ đề ôn tập tổng hợp học kì 1: **số và phép tính** (cộng, trừ phạm vi 100), **hình phẳng** (đường gấp khúc, tứ giác), "
            "**đo lường** (kg, l, ngày – giờ – phút, ngày – tháng)."
        ),
        "theory": (
            "### Bài 33. Ôn tập phép cộng, phép trừ trong phạm vi 20, 100\n"
            "- Cộng, trừ qua 10; đặt tính có nhớ; tính có hai dấu phép tính.\n"
            "### Bài 34. Ôn tập hình phẳng\n"
            "- Đếm đoạn thẳng, tứ giác; tính độ dài đường gấp khúc.\n"
            "### Bài 35. Ôn tập đo lường\n"
            "- kg, l; đọc giờ; xem lịch.\n"
            "### Bài 36. Ôn tập chung"
        ),
        "formulas": [
            G("I. Số và phép tính", F("Thành phần", "Số hạng + Số hạng = Tổng · Số bị trừ − Số trừ = Hiệu"),
              F("Tìm số hạng", "Số hạng = Tổng − Số hạng kia", "? + 8 = 15 → 15 − 8 = 7."),
              F("Hơn, kém", "Số lớn − Số bé")),
            G("II. Hình và đo lường", F("Đường gấp khúc", "Độ dài = tổng độ dài các đoạn"),
              F("Thời gian", "1 ngày = 24 giờ · 1 giờ = 60 phút · 1 tuần = 7 ngày")),
        ],
        "example": "Tìm số thích hợp: ? + 27 = 54.",
        "example_answer": "Số hạng chưa biết = Tổng − Số hạng đã biết: 54 − 27 = **27**. Thử lại: 27 + 27 = 54 ✔.",
        "real_life": "- Tổng kết điểm thi đua, đếm số sách quyên góp của cả lớp.\n- Đọc giờ vào học, xem lịch nghỉ Tết.",
        "quiz": [
            mcq("biet", "9 + 7 = ?", ["15", "16", "17", "2"], 1, "9 + 1 = 10, 10 + 6 = **16**."),
            mcq("biet", "Trong phép tính 54 − 19 = 35, số 35 là:", ["Số bị trừ", "Số trừ", "Hiệu", "Tổng"], 2, "Kết quả của phép trừ là **hiệu**."),
            mcq("biet", "Đơn vị đo khối lượng đã học là:", ["lít", "ki-lô-gam", "giờ", "xăng-ti-mét"], 1, "Đo khối lượng bằng **ki-lô-gam (kg)**."),
            mcq("biet", "Kim dài chỉ số 12, kim ngắn chỉ số 4. Đồng hồ chỉ:", ["12 giờ 4 phút", "4 giờ", "4 giờ 30 phút", "12 giờ"], 1, "Kim phút chỉ 12 → giờ đúng; kim giờ chỉ 4 → **4 giờ**."),
            mcq("hieu", "Số thích hợp điền vào ô trống: ? + 8 = 15", ["23", "7", "8", "6"], 1, "Số hạng chưa biết = 15 − 8 = **7**."),
            mcq("hieu", "Tính: 63 − 25 + 12 = ?", ["50", "26", "38", "40"], 0, "63 − 25 = 38; 38 + 12 = **50**."),
            tf("hieu", "Nhận định: “Đường gấp khúc gồm 2 đoạn 8 cm và 7 cm thì dài 15 cm.”", True, "8 + 7 = 15 (cm) → **Đúng**."),
            tf("hieu", "Nhận định: “36 kg + 9 kg = 45 l.”", False, "36 + 9 = 45 nhưng đơn vị phải giữ là **kg**: 45 kg, không phải lít → **Sai**."),
            mcq("vandung", "Hùng có 34 viên bi, Hùng có nhiều hơn Dũng 8 viên. Dũng có bao nhiêu viên bi?", ["42", "26", "24", "36"], 1,
                "Hùng nhiều hơn Dũng 8 viên nghĩa là Dũng **ít hơn** Hùng 8 viên: 34 − 8 = **26** (viên).",
                note="Đọc kỹ: “Hùng nhiều hơn Dũng” → tìm số của Dũng phải trừ."),
            short("vandung", "Một cửa hàng buổi sáng bán được 46 l dầu, buổi chiều bán được 38 l dầu. Hỏi cả ngày bán được bao nhiêu lít dầu?", ["84", "84l"],
                  "46 + 38: 6 + 8 = 14, viết 4 nhớ 1; 4 + 3 + 1 = 8 → 84.\nĐáp số: **84 l**.", unit="l"),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 8 =====================
    {
        "topic": "l2-cd08-phep-nhan-phep-chia",
        "title": "Phép nhân, phép chia",
        "icon": "✖️",
        "description": "Chủ đề 8 · SGK Toán 2 tập hai (tr. 4–33): Bài 37 – Bài 45. Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – thương; bảng nhân 2, 5 và bảng chia 2, 5.",
        "requirements": [
            "Nhận biết được ý nghĩa của phép nhân (tổng các số hạng bằng nhau) và phép chia (chia thành các phần bằng nhau, chia theo nhóm).",
            "Nhận biết được thừa số, tích; số bị chia, số chia, thương.",
            "Vận dụng được bảng nhân 2, bảng nhân 5 và bảng chia 2, bảng chia 5 trong thực hành tính.",
            "Giải được bài toán thực tế có một bước tính liên quan đến phép nhân, phép chia.",
        ],
        "definition": (
            "- **Phép nhân**: tổng của các số hạng **bằng nhau** được viết gọn thành phép nhân. 2 + 2 + 2 = 2 × 3 (2 được lấy 3 lần).\n"
            "- Trong 2 × 3 = 6: 2 và 3 là **thừa số**, 6 là **tích** (2 × 3 cũng gọi là tích).\n"
            "- **Phép chia**: chia đều một số lượng thành các phần bằng nhau, hoặc chia theo nhóm. 6 : 2 = 3.\n"
            "- Trong 6 : 2 = 3: 6 là **số bị chia**, 2 là **số chia**, 3 là **thương** (6 : 2 cũng gọi là thương)."
        ),
        "theory": (
            "### Bài 37. Phép nhân\n"
            "- 5 + 5 + 5 + 5 = 20 viết thành 5 × 4 = 20, đọc “năm nhân bốn bằng hai mươi”.\n"
            "### Bài 38. Thừa số, tích\n"
            "- Thừa số × Thừa số = Tích. Đổi chỗ hai thừa số thì tích không đổi: 2 × 5 = 5 × 2 = 10.\n"
            "### Bài 39. Bảng nhân 2\n"
            "- 2 × 1 = 2, 2 × 2 = 4, 2 × 3 = 6, …, 2 × 10 = 20 (mỗi lần thêm 2).\n"
            "### Bài 40. Bảng nhân 5\n"
            "- 5 × 1 = 5, 5 × 2 = 10, 5 × 3 = 15, …, 5 × 10 = 50 (mỗi lần thêm 5).\n"
            "### Bài 41. Phép chia\n"
            "- Có 8 cái kẹo chia đều cho 2 bạn, mỗi bạn 4 cái: 8 : 2 = 4. Có 8 cái kẹo chia mỗi bạn 2 cái thì được 4 bạn: 8 : 2 = 4.\n"
            "- Từ phép nhân suy ra phép chia: 2 × 4 = 8 → 8 : 2 = 4 và 8 : 4 = 2.\n"
            "### Bài 42. Số bị chia, số chia, thương\n"
            "- Số bị chia : Số chia = Thương.\n"
            "### Bài 43. Bảng chia 2\n"
            "- 2 : 2 = 1, 4 : 2 = 2, …, 20 : 2 = 10 (lập từ bảng nhân 2).\n"
            "### Bài 44. Bảng chia 5\n"
            "- 5 : 5 = 1, 10 : 5 = 2, …, 50 : 5 = 10 (lập từ bảng nhân 5).\n"
            "### Bài 45. Luyện tập chung"
        ),
        "formulas": [
            G("I. Phép nhân", F("Ý nghĩa", "a + a + … + a (b số hạng) = a × b", "3 + 3 + 3 + 3 = 3 × 4 = 12."),
              F("Thành phần", "Thừa số × Thừa số = Tích"),
              F("Tính chất giao hoán", "a × b = b × a", "5 × 2 = 2 × 5 = 10.")),
            G("II. Phép chia", F("Thành phần", "Số bị chia : Số chia = Thương"),
              F("Liên hệ nhân – chia", "a × b = c ⇒ c : a = b và c : b = a", "5 × 3 = 15 ⇒ 15 : 5 = 3; 15 : 3 = 5.")),
            G("III. Bảng nhân – chia", F("Bảng nhân 2", "2 × 1 = 2, 2 × 2 = 4, …, 2 × 10 = 20"),
              F("Bảng nhân 5", "5 × 1 = 5, 5 × 2 = 10, …, 5 × 10 = 50"),
              F("Bảng chia 2, chia 5", "20 : 2 = 10, 18 : 2 = 9, … · 50 : 5 = 10, 45 : 5 = 9, …")),
        ],
        "example": "Có 15 quả cam xếp đều vào 5 đĩa. Hỏi mỗi đĩa có mấy quả cam?",
        "example_answer": "Chia đều 15 quả vào 5 đĩa: 15 : 5 = **3** (quả).\nĐáp số: 3 quả cam.",
        "real_life": "- Tính số chân của 6 con gà: 2 × 6 = 12.\n- Chia đều bánh kẹo cho các bạn; xếp học sinh thành hàng 5.",
        "quiz": [
            mcq("biet", "Tổng 4 + 4 + 4 viết thành phép nhân là:", ["4 × 4", "4 × 3", "3 + 4", "4 × 12"], 1,
                "Số 4 được lấy 3 lần → **4 × 3**.", note="Thừa số thứ nhất là số được lấy, thừa số thứ hai là số lần."),
            mcq("biet", "Trong phép nhân 5 × 6 = 30, số 30 gọi là:", ["Thừa số", "Tích", "Thương", "Tổng"], 1, "Kết quả phép nhân là **tích**."),
            mcq("biet", "2 × 8 = ?", ["10", "14", "16", "18"], 2, "Bảng nhân 2: 2 × 8 = **16**."),
            mcq("biet", "Trong phép chia 20 : 5 = 4, số chia là:", ["20", "5", "4", "25"], 1, "Số đứng sau dấu “:” là **số chia**: 5.", note="20 là số bị chia, 4 là thương."),
            mcq("hieu", "35 : 5 = ?", ["5", "6", "7", "8"], 2, "Vì 5 × 7 = 35 nên 35 : 5 = **7**."),
            mcq("hieu", "Từ phép nhân 2 × 9 = 18, ta lập được phép chia nào?", ["18 : 2 = 9", "18 : 3 = 6", "9 : 2 = 18", "18 : 9 = 3"], 0,
                "Tích chia cho thừa số này được thừa số kia: **18 : 2 = 9** (và 18 : 9 = 2)."),
            tf("hieu", "Nhận định: “5 × 4 = 4 × 5.”", True, "Đổi chỗ các thừa số thì tích không đổi: cùng bằng 20 → **Đúng**."),
            tf("hieu", "Nhận định: “Thương của 12 và 2 là 24.”", False, "Thương là kết quả phép chia: 12 : 2 = 6, không phải 24 (24 là tích) → **Sai**."),
            mcq("vandung", "Mỗi bạn có 5 que tính. Hỏi 7 bạn có tất cả bao nhiêu que tính?", ["12", "35", "30", "40"], 1,
                "5 que được lấy 7 lần: 5 × 7 = **35** (que tính).", note="Không cộng 5 + 7 = 12."),
            short("vandung", "Có 18 học sinh chia đều thành các nhóm, mỗi nhóm 2 bạn. Hỏi có bao nhiêu nhóm?", ["9"],
                  "Chia theo nhóm 2: 18 : 2 = 9 (nhóm).\nĐáp số: **9 nhóm**.", unit="nhóm", alt="Đếm thêm 2: 2, 4, 6, …, 18 → đếm được 9 lần."),
        ],
    },
    # ===================== CHỦ ĐỀ 9 =====================
    {
        "topic": "l2-cd09-lam-quen-voi-hinh-khoi",
        "title": "Làm quen với hình khối",
        "icon": "🧊",
        "description": "Chủ đề 9 · SGK Toán 2 tập hai (tr. 34–39): Bài 46 – Bài 47. Nhận dạng khối trụ, khối cầu qua vật thật và mô hình.",
        "requirements": [
            "Nhận dạng được khối trụ, khối cầu thông qua việc sử dụng bộ đồ dùng học tập cá nhân hoặc vật thật.",
            "Nhận biết được các đồ vật trong thực tế có dạng khối trụ, khối cầu.",
            "Đếm được số khối trụ, khối cầu trong một hình ghép.",
        ],
        "definition": (
            "- **Khối cầu**: tròn đều về mọi phía, lăn được theo mọi hướng (quả bóng, viên bi, quả địa cầu).\n"
            "- **Khối trụ**: có hai mặt đáy là hình tròn bằng nhau, thân tròn; đặt nằm thì lăn được, đặt đứng thì đứng vững (lon nước, hộp sữa tròn, khúc gỗ tròn).\n"
            "- Đã biết từ lớp 1: **khối lập phương**, **khối hộp chữ nhật**."
        ),
        "theory": (
            "### Bài 46. Khối trụ, khối cầu\n"
            "- Quan sát, sờ, lăn thử để phân biệt: khối cầu không có mặt phẳng nào; khối trụ có 2 mặt phẳng hình tròn.\n"
            "- Tìm đồ vật quanh em: quả bóng (cầu), cái trống, ống nước, cục pin (trụ).\n"
            "### Bài 47. Luyện tập chung\n"
            "- Phân biệt khối trụ, khối cầu, khối lập phương, khối hộp chữ nhật; đếm số khối trong hình ghép."
        ),
        "formulas": [
            G("I. Đặc điểm nhận dạng", F("Khối cầu", "Tròn đều mọi phía · không có mặt phẳng · lăn mọi hướng"),
              F("Khối trụ", "2 mặt đáy hình tròn bằng nhau + mặt xung quanh cong"),
              F("Khối lập phương / hộp chữ nhật", "Có 6 mặt phẳng, không lăn được")),
        ],
        "example": "Lon nước ngọt, quả bóng đá, viên xúc xắc có dạng khối gì?",
        "example_answer": "Lon nước ngọt: **khối trụ**; quả bóng đá: **khối cầu**; viên xúc xắc: **khối lập phương**.",
        "real_life": "- Ống nước, cột đình, cục pin có dạng khối trụ — dễ lăn khi đặt nằm.\n- Bóng, bi, quả cam có dạng khối cầu.",
        "quiz": [
            mcq("biet", "Quả bóng đá có dạng:", ["Khối trụ", "Khối cầu", "Khối lập phương", "Khối hộp chữ nhật"], 1, "Quả bóng tròn đều mọi phía → **khối cầu**."),
            mcq("biet", "Lon sữa bò hình tròn có dạng:", ["Khối cầu", "Khối lập phương", "Khối trụ", "Khối hộp chữ nhật"], 2, "Có 2 mặt đáy hình tròn → **khối trụ**."),
            mcq("biet", "Đồ vật nào có dạng khối cầu?", ["Viên bi", "Cục pin", "Hộp bút", "Viên gạch"], 0, "**Viên bi** tròn đều → khối cầu."),
            mcq("biet", "Khối trụ có mấy mặt đáy hình tròn?", ["1", "2", "3", "0"], 1, "Khối trụ có **2** mặt đáy hình tròn bằng nhau."),
            mcq("hieu", "Khối nào lăn được theo mọi hướng?", ["Khối trụ", "Khối lập phương", "Khối cầu", "Khối hộp chữ nhật"], 2, "Chỉ **khối cầu** tròn đều mọi phía nên lăn mọi hướng.", note="Khối trụ chỉ lăn theo một hướng khi đặt nằm."),
            mcq("hieu", "Một hình ghép gồm: 3 lon nước, 2 quả bóng và 1 hộp quà vuông. Số khối trụ là:", ["1", "2", "3", "6"], 2, "Lon nước có dạng khối trụ → **3** khối trụ."),
            tf("hieu", "Nhận định: “Cái trống có dạng khối trụ.”", True, "Mặt trống tròn, có 2 mặt đáy tròn → **Đúng**."),
            tf("hieu", "Nhận định: “Khối cầu có thể đặt chồng lên nhau thật vững như khối lập phương.”", False, "Khối cầu không có mặt phẳng nên dễ lăn, khó xếp chồng → **Sai**."),
            mcq("vandung", "Bạn Nam muốn xây tháp cao bằng các khối cho vững. Nên chọn khối nào làm chân tháp?", ["Khối cầu", "Khối lập phương", "Quả bóng", "Viên bi"], 1,
                "**Khối lập phương** có mặt phẳng, đặt vững; khối cầu sẽ lăn."),
            short("vandung", "Trên bàn có 4 quả cam, 2 cục pin, 3 viên bi và 1 hộp phấn hình hộp chữ nhật. Có bao nhiêu đồ vật dạng khối cầu?", ["7"],
                  "Quả cam và viên bi có dạng khối cầu: 4 + 3 = 7.\nĐáp số: **7**.", unit="đồ vật", note="Cục pin là khối trụ, hộp phấn là khối hộp chữ nhật."),
        ],
    },
    # ===================== CHỦ ĐỀ 10 =====================
    {
        "topic": "l2-cd10-cac-so-trong-pham-vi-1000",
        "title": "Các số trong phạm vi 1000",
        "icon": "🔢",
        "description": "Chủ đề 10 · SGK Toán 2 tập hai (tr. 40–64): Bài 48 – Bài 54. Đơn vị, chục, trăm, nghìn; số tròn trăm, tròn chục; số có ba chữ số; viết số thành tổng các trăm, chục, đơn vị; so sánh các số có ba chữ số.",
        "requirements": [
            "Đếm, đọc, viết được các số trong phạm vi 1000; nhận biết được số tròn chục, tròn trăm.",
            "Nhận biết được chữ số hàng trăm, hàng chục, hàng đơn vị; viết được số thành tổng của trăm, chục, đơn vị.",
            "Nhận biết được số liền trước, số liền sau; nhận biết được vị trí các số trên tia số.",
            "So sánh được các số có ba chữ số; sắp xếp được các số theo thứ tự (nhóm không quá 4 số).",
            "Làm quen với việc ước lượng số đồ vật theo các nhóm 1 chục.",
        ],
        "definition": (
            "- 10 đơn vị = 1 **chục**; 10 chục = 1 **trăm**; 10 trăm = 1 **nghìn** (1000).\n"
            "- **Số tròn trăm**: 100, 200, …, 900 (hàng chục và đơn vị đều là 0). **Số tròn chục**: 10, 20, …, 990 (hàng đơn vị là 0).\n"
            "- **Số có ba chữ số** gồm hàng trăm, hàng chục, hàng đơn vị: 375 gồm 3 trăm, 7 chục, 5 đơn vị; 375 = 300 + 70 + 5."
        ),
        "theory": (
            "### Bài 48. Đơn vị, chục, trăm, nghìn\n"
            "- 1 chục = 10 đơn vị; 1 trăm = 10 chục; 1 nghìn = 10 trăm.\n"
            "### Bài 49. Các số tròn trăm, tròn chục\n"
            "- Đọc 400: bốn trăm; 520: năm trăm hai mươi.\n"
            "### Bài 50. So sánh các số tròn trăm, tròn chục\n"
            "- 300 < 500 vì 3 trăm < 5 trăm; 460 > 430 vì cùng 4 trăm, 6 chục > 3 chục.\n"
            "### Bài 51. Số có ba chữ số\n"
            "- Đọc: 205 – hai trăm linh năm (linh = không chục); 714 – bảy trăm mười bốn; 251 – hai trăm năm mươi mốt; 625 – sáu trăm hai mươi lăm.\n"
            "### Bài 52. Viết số thành tổng các trăm, chục, đơn vị\n"
            "- 846 = 800 + 40 + 6; 507 = 500 + 7.\n"
            "### Bài 53. So sánh các số có ba chữ số\n"
            "- So sánh **hàng trăm** trước; nếu bằng thì so sánh **hàng chục**; nếu vẫn bằng thì so sánh **hàng đơn vị**.\n"
            "### Bài 54. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cấu tạo số", F("Quan hệ hàng", "10 đơn vị = 1 chục · 10 chục = 1 trăm · 10 trăm = 1 nghìn"),
              F("Số có ba chữ số", "abc = a trăm + b chục + c đơn vị", "629 = 600 + 20 + 9.")),
            G("II. So sánh", F("Quy tắc", "Trăm → Chục → Đơn vị", "582 < 591 (cùng 5 trăm, 8 chục < 9 chục)."),
              F("Liền trước – liền sau", "n − 1 và n + 1", "Liền trước 400 là 399; liền sau 999 là 1000.")),
        ],
        "example": "Sắp xếp các số 457, 475, 447, 574 theo thứ tự từ bé đến lớn.",
        "example_answer": "So sánh hàng trăm: 574 lớn nhất. Ba số còn lại cùng 4 trăm, so sánh chục: 447 < 457 < 475.\nThứ tự: **447, 457, 475, 574**.",
        "real_life": "- Đọc số trang sách (trang 256), số phòng khách sạn (phòng 305).\n- Ước lượng số hạt, số que tính theo nhóm chục.",
        "quiz": [
            mcq("biet", "Số gồm 6 trăm, 0 chục và 8 đơn vị là:", ["68", "608", "680", "806"], 1, "600 + 0 + 8 = **608**.", note="Hàng chục bằng 0 phải viết chữ số 0."),
            mcq("biet", "10 trăm bằng:", ["100", "1000", "110", "10"], 1, "10 trăm = **1 nghìn = 1000**."),
            mcq("biet", "Số “bảy trăm linh năm” viết là:", ["75", "750", "705", "7005"], 2, "Bảy trăm = 700, linh (0 chục), năm → **705**."),
            mcq("biet", "Số liền sau của 399 là:", ["398", "400", "390", "300"], 1, "399 + 1 = **400**."),
            mcq("hieu", "Số 836 viết thành tổng các trăm, chục, đơn vị là:", ["800 + 30 + 6", "8 + 3 + 6", "800 + 36 + 6", "80 + 30 + 6"], 0, "836 gồm 8 trăm, 3 chục, 6 đơn vị → **800 + 30 + 6**."),
            mcq("hieu", "Số lớn nhất trong các số 519, 591, 195, 559 là:", ["519", "591", "195", "559"], 1, "Ba số có 5 trăm; so sánh chục: 9 > 5 > 1 → **591** lớn nhất."),
            tf("hieu", "Nhận định: “478 > 487.”", False, "Cùng 4 trăm; hàng chục 7 < 8 nên 478 < 487 → **Sai**."),
            tf("hieu", "Nhận định: “Số 900 là số tròn trăm.”", True, "900 có hàng chục và hàng đơn vị đều là 0 → **Đúng**."),
            mcq("vandung", "Từ ba thẻ số 3, 0, 7 lập được số có ba chữ số lớn nhất (mỗi thẻ dùng một lần) là:", ["730", "703", "370", "037"], 0,
                "Muốn lớn nhất: hàng trăm lấy chữ số lớn nhất (7), tiếp theo 3, cuối cùng 0 → **730**.", note="Chữ số 0 không đứng ở hàng trăm."),
            short("vandung", "Số bé nhất có ba chữ số khác nhau là số nào?", ["102"],
                  "Hàng trăm nhỏ nhất khác 0 là 1, hàng chục nhỏ nhất là 0, hàng đơn vị nhỏ nhất khác 1 và 0 là 2 → **102**.",
                  note="Không phải 100 vì 100 có hai chữ số 0 giống nhau."),
        ],
    },
    # ===================== CHỦ ĐỀ 11 =====================
    {
        "topic": "l2-cd11-do-dai-va-tien-viet-nam",
        "title": "Độ dài và đơn vị đo độ dài. Tiền Việt Nam",
        "icon": "📏",
        "description": "Chủ đề 11 · SGK Toán 2 tập hai (tr. 65–78): Bài 55 – Bài 58. Đề-xi-mét, mét, ki-lô-mét; giới thiệu tiền Việt Nam; thực hành trải nghiệm đo độ dài.",
        "requirements": [
            "Nhận biết được các đơn vị đo độ dài dm (đề-xi-mét), m (mét), km (ki-lô-mét) và quan hệ giữa các đơn vị đó.",
            "Thực hiện được việc đo và ước lượng độ dài theo các đơn vị đã học; tính toán với số đo độ dài.",
            "Nhận biết được tiền Việt Nam thông qua hình ảnh một số tờ tiền.",
            "Giải quyết được các vấn đề thực tế đơn giản liên quan đến đo độ dài và tiền.",
        ],
        "definition": (
            "- **Đề-xi-mét** (dm): 1 dm = 10 cm. **Mét** (m): 1 m = 10 dm = 100 cm. **Ki-lô-mét** (km): 1 km = 1000 m.\n"
            "- Dùng **km** đo quãng đường dài (giữa các tỉnh); **m** đo chiều dài lớp học; **dm, cm** đo đồ vật nhỏ.\n"
            "- **Tiền Việt Nam**: đơn vị là **đồng**. Một số tờ tiền: 100 đồng, 200 đồng, 500 đồng, 1000 đồng, 2000 đồng, 5000 đồng, 10 000 đồng…"
        ),
        "theory": (
            "### Bài 55. Đề-xi-mét. Mét. Ki-lô-mét\n"
            "- 1 dm = 10 cm; 1 m = 10 dm; 1 m = 100 cm; 1 km = 1000 m.\n"
            "- Cộng, trừ số đo cùng đơn vị: 25 m + 17 m = 42 m.\n"
            "### Bài 56. Giới thiệu tiền Việt Nam\n"
            "- Nhận biết mệnh giá ghi trên tờ tiền; đổi tiền: 1 tờ 1000 đồng = 2 tờ 500 đồng = 5 tờ 200 đồng = 10 tờ 100 đồng.\n"
            "### Bài 57. Thực hành và trải nghiệm đo độ dài\n"
            "- Đo bằng thước mét, ước lượng: bước chân khoảng 4–5 dm, sải tay khoảng 1 m.\n"
            "### Bài 58. Luyện tập chung"
        ),
        "formulas": [
            G("I. Đơn vị đo độ dài", F("Quan hệ", "1 km = 1000 m · 1 m = 10 dm = 100 cm · 1 dm = 10 cm"),
              F("Tính với số đo", "Chỉ cộng, trừ khi cùng đơn vị; viết đơn vị ở kết quả", "6 dm − 2 dm = 4 dm.")),
            G("II. Tiền Việt Nam", F("Đơn vị", "đồng"),
              F("Đổi tiền", "1000 đồng = 500 đồng + 500 đồng = 5 × 200 đồng")),
        ],
        "example": "Đổi: 3 dm = … cm; 2 m = … dm.",
        "example_answer": "1 dm = 10 cm nên 3 dm = **30 cm**. 1 m = 10 dm nên 2 m = **20 dm**.",
        "real_life": "- Biển báo “Hà Nội 35 km” cho biết quãng đường còn lại.\n- Đi chợ mua đồ, trả tiền và nhận tiền thừa.",
        "quiz": [
            mcq("biet", "1 dm = … cm?", ["1", "10", "100", "1000"], 1, "1 đề-xi-mét = **10** xăng-ti-mét."),
            mcq("biet", "1 km = … m?", ["10", "100", "1000", "10 000"], 2, "1 ki-lô-mét = **1000** mét."),
            mcq("biet", "Đơn vị thích hợp để đo quãng đường từ Hà Nội đến Hải Phòng là:", ["cm", "dm", "m", "km"], 3, "Quãng đường giữa hai thành phố rất dài → dùng **km**."),
            mcq("biet", "Đơn vị tiền Việt Nam là:", ["mét", "đồng", "ki-lô-gam", "lít"], 1, "Tiền Việt Nam tính bằng **đồng**."),
            mcq("hieu", "1 m = … cm?", ["10", "100", "1000", "50"], 1, "1 m = 10 dm = 10 × 10 cm = **100 cm**."),
            mcq("hieu", "35 m + 28 m = ?", ["53 m", "63 m", "63 cm", "7 m"], 1, "35 + 28 = 63 → **63 m** (giữ nguyên đơn vị)."),
            tf("hieu", "Nhận định: “Một chiếc bút chì dài khoảng 2 m.”", False, "Bút chì dài khoảng 15–20 cm (khoảng 2 dm), không phải 2 m → **Sai**.", note="Ước lượng: 1 m bằng khoảng một sải tay."),
            tf("hieu", "Nhận định: “Hai tờ 500 đồng đổi được một tờ 1000 đồng.”", True, "500 + 500 = 1000 (đồng) → **Đúng**."),
            mcq("vandung", "Lan có 1 tờ 2000 đồng, mua một cái tẩy giá 1000 đồng và một cái thước giá 500 đồng. Lan còn lại bao nhiêu tiền?", ["500 đồng", "1000 đồng", "1500 đồng", "3500 đồng"], 0,
                "Tiền mua: 1000 + 500 = 1500 (đồng). Còn lại: 2000 − 1500 = **500 đồng**."),
            short("vandung", "Sợi dây dài 1 m, cắt đi 35 cm. Phần còn lại dài bao nhiêu xăng-ti-mét?", ["65"],
                  "Đổi 1 m = 100 cm. Còn lại: 100 − 35 = 65 (cm).\nĐáp số: **65 cm**.", unit="cm", note="Phải đổi về cùng đơn vị trước khi trừ."),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 12 =====================
    {
        "topic": "l2-cd12-cong-tru-pham-vi-1000",
        "title": "Phép cộng, phép trừ trong phạm vi 1000",
        "icon": "➕",
        "description": "Chủ đề 12 · SGK Toán 2 tập hai (tr. 79–99): Bài 59 – Bài 63. Phép cộng, phép trừ (không nhớ, có nhớ) trong phạm vi 1000; cộng, trừ nhẩm số tròn trăm, tròn chục.",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ (không nhớ, có nhớ không quá một lượt) các số trong phạm vi 1000.",
            "Thực hiện được việc cộng, trừ nhẩm các số tròn chục, tròn trăm trong phạm vi 1000.",
            "Thực hiện được việc tính toán trong trường hợp có hai dấu phép tính cộng, trừ (theo thứ tự từ trái sang phải).",
            "Giải được bài toán thực tế có một bước tính liên quan đến phép cộng, phép trừ.",
        ],
        "definition": (
            "- **Đặt tính**: viết các chữ số cùng hàng thẳng cột (trăm thẳng trăm, chục thẳng chục, đơn vị thẳng đơn vị).\n"
            "- **Tính**: từ phải sang trái — hàng đơn vị → hàng chục → hàng trăm.\n"
            "- **Có nhớ**: khi cộng một hàng được từ 10 trở lên thì viết chữ số đơn vị và **nhớ 1** sang hàng bên trái; khi trừ mà chữ số trên bé hơn chữ số dưới thì **mượn 1** ở hàng bên trái (trừ thêm 1 ở hàng đó)."
        ),
        "theory": (
            "### Bài 59. Phép cộng (không nhớ) trong phạm vi 1000\n"
            "- 342 + 215 = 557. Nhẩm tròn trăm: 300 + 400 = 700 (3 trăm + 4 trăm = 7 trăm).\n"
            "### Bài 60. Phép cộng (có nhớ) trong phạm vi 1000\n"
            "- 265 + 127: 5 + 7 = 12, viết 2 nhớ 1; 6 + 2 + 1 = 9; 2 + 1 = 3 → 392.\n"
            "### Bài 61. Phép trừ (không nhớ) trong phạm vi 1000\n"
            "- 786 − 354 = 432. Nhẩm: 800 − 300 = 500; 650 − 30 = 620.\n"
            "### Bài 62. Phép trừ (có nhớ) trong phạm vi 1000\n"
            "- 452 − 128: 2 không trừ được 8, lấy 12 − 8 = 4, viết 4 nhớ 1; 2 thêm 1 là 3, 5 − 3 = 2; 4 − 1 = 3 → 324.\n"
            "### Bài 63. Luyện tập chung"
        ),
        "formulas": [
            G("I. Quy tắc tính", F("Đặt tính", "Thẳng cột theo hàng; tính từ phải sang trái"),
              F("Cộng có nhớ", "Tổng một hàng ≥ 10 → viết hàng đơn vị, nhớ 1 sang hàng kế tiếp"),
              F("Trừ có nhớ", "Chữ số trên < chữ số dưới → thêm 10 để trừ, nhớ 1 vào số trừ ở hàng kế tiếp")),
            G("II. Thành phần & kiểm tra", F("Thử lại phép trừ", "Hiệu + Số trừ = Số bị trừ", "324 + 128 = 452 ✔"),
              F("Hai dấu phép tính", "Tính lần lượt từ trái sang phải", "500 − 200 + 300 = 300 + 300 = 600.")),
        ],
        "example": "Đặt tính rồi tính: 538 + 245 và 671 − 236.",
        "example_answer": "538 + 245: 8 + 5 = 13, viết 3 nhớ 1; 3 + 4 + 1 = 8; 5 + 2 = 7 → **783**.\n671 − 236: 1 không trừ được 6, 11 − 6 = 5, nhớ 1; 3 + 1 = 4, 7 − 4 = 3; 6 − 2 = 4 → **435**.",
        "real_life": "- Tính tổng số học sinh của hai khối lớp, số trang sách còn phải đọc.\n- Cộng giá tiền các món hàng khi đi mua sắm.",
        "quiz": [
            mcq("biet", "400 + 300 = ?", ["700", "70", "7000", "100"], 0, "4 trăm + 3 trăm = 7 trăm = **700**."),
            mcq("biet", "Khi đặt tính 352 + 41, chữ số 4 của số 41 phải thẳng cột với chữ số nào của 352?", ["3", "5", "2", "Không cần thẳng cột"], 1,
                "4 ở hàng chục, phải thẳng với chữ số hàng chục của 352 là **5**.", note="Lỗi hay gặp: viết lệch sang trái thẳng với hàng trăm."),
            mcq("biet", "235 + 142 = ?", ["377", "367", "387", "93"], 0, "5 + 2 = 7; 3 + 4 = 7; 2 + 1 = 3 → **377**."),
            mcq("biet", "869 − 425 = ?", ["444", "434", "454", "1294"], 0, "9 − 5 = 4; 6 − 2 = 4; 8 − 4 = 4 → **444**."),
            mcq("hieu", "456 + 238 = ?", ["684", "694", "614", "218"], 1, "6 + 8 = 14, viết 4 nhớ 1; 5 + 3 + 1 = 9; 4 + 2 = 6 → **694**.", note="Quên nhớ sẽ ra 684."),
            mcq("hieu", "740 − 50 + 10 = ?", ["700", "680", "800", "690"], 0, "Tính từ trái sang phải: 740 − 50 = 690; 690 + 10 = **700**."),
            tf("hieu", "Nhận định: “523 − 147 = 376.”", True, "13 − 7 = 6, nhớ 1; 2 không trừ được 5, 12 − 5 = 7, nhớ 1; 5 − 2 = 3 → 376 → **Đúng**.", alt="Thử lại: 376 + 147 = 523 ✔."),
            tf("hieu", "Nhận định: “362 + 9 = 452.”", False, "2 + 9 = 11, viết 1 nhớ 1; 6 + 1 = 7; 3 → 371. Đặt 9 thẳng hàng chục sẽ sai ra 452 → **Sai**."),
            mcq("vandung", "Trường có 465 học sinh, trong đó có 238 học sinh nữ. Số học sinh nam là:", ["227", "237", "703", "233"], 0,
                "Số học sinh nam = 465 − 238: 15 − 8 = 7, nhớ 1; 6 − 4 = 2; 4 − 2 = 2 → **227**."),
            short("vandung", "Một con đường dài 900 m. Đội công nhân đã sửa được 350 m. Hỏi còn bao nhiêu mét đường chưa sửa?", ["550"],
                  "900 − 350 = 550 (m).\nĐáp số: **550 m**.", unit="m", alt="Nhẩm: 900 − 300 = 600; 600 − 50 = 550."),
        ],
    },
    # ===================== CHỦ ĐỀ 13 =====================
    {
        "topic": "l2-cd13-thong-ke-xac-suat",
        "title": "Làm quen với yếu tố thống kê, xác suất",
        "icon": "📊",
        "description": "Chủ đề 13 · SGK Toán 2 tập hai (tr. 100–109): Bài 64 – Bài 67. Thu thập, phân loại, kiểm đếm số liệu; biểu đồ tranh; chắc chắn, có thể, không thể; thực hành trải nghiệm.",
        "requirements": [
            "Làm quen với việc thu thập, phân loại, kiểm đếm các đối tượng thống kê (trong một số tình huống đơn giản).",
            "Đọc và mô tả được các số liệu ở dạng biểu đồ tranh; nêu được một số nhận xét đơn giản từ biểu đồ tranh.",
            "Làm quen với việc mô tả những hiện tượng liên quan tới các thuật ngữ: có thể, chắc chắn, không thể, thông qua một vài thí nghiệm, trò chơi.",
        ],
        "definition": (
            "- **Thu thập, phân loại, kiểm đếm**: gom các đối tượng theo từng loại rồi đếm số lượng mỗi loại (có thể đánh dấu |, ||…).\n"
            "- **Biểu đồ tranh**: dùng hình vẽ biểu thị số lượng; mỗi hình có thể ứng với 1 hoặc nhiều đối tượng.\n"
            "- **Chắc chắn**: luôn xảy ra. **Có thể**: có lúc xảy ra, có lúc không. **Không thể**: không bao giờ xảy ra."
        ),
        "theory": (
            "### Bài 64. Thu thập, phân loại, kiểm đếm số liệu\n"
            "- Ví dụ: đếm số bạn thích từng loại quả; ghi kết quả vào bảng.\n"
            "### Bài 65. Biểu đồ tranh\n"
            "- Đọc biểu đồ: đếm số hình ở mỗi hàng; so sánh nhiều nhất, ít nhất, nhiều hơn bao nhiêu.\n"
            "### Bài 66. Chắc chắn, có thể, không thể\n"
            "- Hộp chỉ có bóng đỏ: lấy ra **chắc chắn** là bóng đỏ, **không thể** là bóng xanh.\n"
            "- Hộp có bóng đỏ và xanh: lấy ra **có thể** là bóng đỏ.\n"
            "### Bài 67. Thực hành kiểm đếm số liệu, trải nghiệm"
        ),
        "formulas": [
            G("I. Thống kê", F("Các bước", "Thu thập → Phân loại → Kiểm đếm → Ghi kết quả / Biểu đồ tranh"),
              F("Đọc biểu đồ tranh", "Số lượng = số hình × giá trị mỗi hình")),
            G("II. Khả năng xảy ra", F("Ba mức", "Chắc chắn · Có thể · Không thể")),
        ],
        "example": "Biểu đồ tranh: Táo 🍎🍎🍎🍎🍎, Cam 🍊🍊🍊, Chuối 🍌🍌🍌🍌 (mỗi hình = 1 bạn). Loại quả nào được nhiều bạn thích nhất? Nhiều hơn cam mấy bạn?",
        "example_answer": "Táo có 5 bạn, cam 3 bạn, chuối 4 bạn → **Táo** nhiều nhất; nhiều hơn cam 5 − 3 = **2** bạn.",
        "real_life": "- Điểm danh, kiểm đếm số bạn đi học, số bạn mặc áo đồng phục.\n- Dự đoán: “Ngày mai có thể mưa”, “Mặt Trời chắc chắn mọc ở phía đông”.",
        "quiz": [
            mcq("biet", "Hộp chỉ có 5 viên bi đỏ. Lấy ra 1 viên, viên bi đó … là bi đỏ.", ["chắc chắn", "có thể", "không thể", "không biết"], 0, "Hộp chỉ có bi đỏ nên **chắc chắn** lấy được bi đỏ."),
            mcq("biet", "Hộp chỉ có bóng xanh. Lấy được bóng vàng là sự kiện:", ["chắc chắn", "có thể", "không thể", "luôn xảy ra"], 2, "Hộp không có bóng vàng → **không thể**."),
            mcq("biet", "Kiểm đếm: Tổ 1 có các bạn thích màu: đỏ, xanh, đỏ, vàng, đỏ. Số bạn thích màu đỏ là:", ["1", "2", "3", "5"], 2, "Đếm chữ “đỏ”: **3** bạn."),
            mcq("biet", "Biểu đồ dùng hình vẽ để biểu thị số lượng gọi là:", ["Bảng cửu chương", "Biểu đồ tranh", "Tia số", "Đồng hồ"], 1, "Đó là **biểu đồ tranh**."),
            mcq("hieu", "Biểu đồ tranh: Gà ⭐⭐⭐⭐, Vịt ⭐⭐, Ngan ⭐⭐⭐ (mỗi ⭐ = 1 con). Con vật nào ít nhất?", ["Gà", "Vịt", "Ngan", "Bằng nhau"], 1, "Vịt chỉ có 2 hình → **Vịt** ít nhất."),
            mcq("hieu", "Hộp có 3 bóng đỏ, 2 bóng xanh. Lấy ra 1 quả. Câu nào đúng?", ["Chắc chắn lấy được bóng đỏ", "Không thể lấy được bóng xanh", "Có thể lấy được bóng xanh", "Chắc chắn lấy được bóng vàng"], 2,
                "Hộp có cả đỏ và xanh nên lấy ra **có thể** là bóng xanh (cũng có thể là đỏ)."),
            tf("hieu", "Nhận định: “Ngày mai Mặt Trời mọc ở phía tây là sự kiện không thể.”", True, "Mặt Trời luôn mọc ở phía đông → mọc phía tây là **không thể** → **Đúng**."),
            tf("hieu", "Nhận định: “Gieo một con xúc xắc thì chắc chắn được mặt 6 chấm.”", False, "Xúc xắc có 6 mặt nên chỉ **có thể** ra mặt 6 chấm → **Sai**."),
            mcq("vandung", "Biểu đồ tranh số sách đọc: An 📘📘📘, Bình 📘📘📘📘📘, Chi 📘📘 (mỗi 📘 = 2 quyển). Bình đọc nhiều hơn Chi bao nhiêu quyển?", ["3 quyển", "6 quyển", "10 quyển", "4 quyển"], 1,
                "Bình: 5 × 2 = 10 quyển; Chi: 2 × 2 = 4 quyển. Nhiều hơn: 10 − 4 = **6 quyển**.", note="Mỗi hình ứng với 2 quyển, không phải 1."),
            short("vandung", "Kiểm đếm số xe qua cổng trường: ô tô ||||, xe máy |||| ||||, xe đạp |||. Có tất cả bao nhiêu xe?", ["16"],
                  "Ô tô 4, xe máy 9, xe đạp 3: 4 + 9 + 3 = 16.\nĐáp số: **16 xe**.", unit="xe"),
        ],
    },
    # ===================== CHỦ ĐỀ 14 =====================
    {
        "topic": "l2-cd14-on-tap-cuoi-nam",
        "title": "Ôn tập cuối năm",
        "icon": "🏁",
        "description": "Chủ đề 14 · SGK Toán 2 tập hai (tr. 110–138): Bài 68 – Bài 75. Ôn tập các số trong phạm vi 1000; phép cộng, trừ, nhân, chia; hình học và đo lường; kiểm đếm số liệu và lựa chọn khả năng.",
        "requirements": [
            "Củng cố đọc, viết, so sánh, cấu tạo các số trong phạm vi 1000.",
            "Thực hiện thành thạo cộng, trừ trong phạm vi 1000; bảng nhân 2, 5 và bảng chia 2, 5.",
            "Nhận dạng hình phẳng, hình khối; tính độ dài đường gấp khúc; đổi, tính với đơn vị đo đã học; đọc giờ, xem lịch.",
            "Đọc biểu đồ tranh, mô tả khả năng xảy ra (chắc chắn, có thể, không thể); giải bài toán có lời văn một bước tính.",
        ],
        "definition": (
            "- Số trong phạm vi 1000: trăm – chục – đơn vị; so sánh từ hàng trăm.\n"
            "- Bốn phép tính: cộng, trừ (có nhớ một lượt), nhân, chia với bảng 2 và 5.\n"
            "- Đo lường: cm, dm, m, km; kg; l; giờ – phút; ngày – tháng; tiền Việt Nam (đồng)."
        ),
        "theory": (
            "### Bài 68. Ôn tập các số trong phạm vi 1000\n"
            "### Bài 69. Ôn tập phép cộng, phép trừ trong phạm vi 100\n"
            "### Bài 70. Ôn tập phép cộng, phép trừ trong phạm vi 1000\n"
            "### Bài 71. Ôn tập phép nhân, phép chia\n"
            "- Bảng nhân 2, 5; bảng chia 2, 5; thừa số – tích; số bị chia – số chia – thương.\n"
            "### Bài 72. Ôn tập hình học\n"
            "- Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, đường gấp khúc; hình tứ giác; khối trụ, khối cầu.\n"
            "### Bài 73. Ôn tập đo lường\n"
            "- 1 m = 10 dm = 100 cm; 1 km = 1000 m; kg; l; giờ; tiền.\n"
            "### Bài 74. Ôn tập kiểm đếm số liệu và lựa chọn khả năng\n"
            "### Bài 75. Ôn tập chung"
        ),
        "formulas": [
            G("I. Số và phép tính", F("Cấu tạo số", "abc = a trăm + b chục + c đơn vị"),
              F("Nhân – chia", "Thừa số × Thừa số = Tích · Số bị chia : Số chia = Thương"),
              F("Tìm số hạng", "Số hạng = Tổng − Số hạng kia")),
            G("II. Hình học và đo lường", F("Đường gấp khúc", "Độ dài = tổng độ dài các đoạn thẳng"),
              F("Độ dài", "1 km = 1000 m · 1 m = 10 dm = 100 cm"),
              F("Thời gian", "1 ngày = 24 giờ · 1 giờ = 60 phút")),
        ],
        "example": "Mỗi túi có 5 kg gạo. Hỏi 8 túi như thế có bao nhiêu ki-lô-gam gạo?",
        "example_answer": "5 kg được lấy 8 lần: 5 × 8 = **40** (kg).\nĐáp số: 40 kg gạo.",
        "real_life": "- Tổng kết cuối năm: đếm số sách, số điểm tốt; lập kế hoạch đi chơi hè (thời gian, quãng đường, tiền).",
        "quiz": [
            mcq("biet", "Số “chín trăm mười lăm” viết là:", ["915", "951", "9015", "905"], 0, "900 + 10 + 5 = **915**."),
            mcq("biet", "5 × 9 = ?", ["40", "45", "14", "50"], 1, "Bảng nhân 5: 5 × 9 = **45**."),
            mcq("biet", "16 : 2 = ?", ["8", "7", "14", "32"], 0, "Vì 2 × 8 = 16 nên 16 : 2 = **8**."),
            mcq("biet", "Hình có 4 cạnh là:", ["Hình tam giác", "Hình tứ giác", "Khối cầu", "Hình tròn"], 1, "Hình có 4 cạnh, 4 đỉnh là **hình tứ giác**."),
            mcq("hieu", "Đường gấp khúc gồm 3 đoạn, mỗi đoạn dài 5 cm. Độ dài đường gấp khúc là:", ["8 cm", "15 cm", "10 cm", "53 cm"], 1, "5 + 5 + 5 = 5 × 3 = **15 cm**."),
            mcq("hieu", "So sánh: 607 … 670", ["<", ">", "=", "Không so sánh được"], 0, "Cùng 6 trăm; hàng chục 0 < 7 → 607 **<** 670."),
            tf("hieu", "Nhận định: “2 m = 20 dm.”", True, "1 m = 10 dm nên 2 m = 20 dm → **Đúng**."),
            tf("hieu", "Nhận định: “746 − 382 = 464.”", False, "6 − 2 = 4; 4 không trừ được 8: 14 − 8 = 6, nhớ 1; 7 − 4 = 3 → 364, không phải 464 → **Sai**.", note="Nhớ cộng 1 vào hàng trăm của số trừ."),
            mcq("vandung", "Có 40 quyển vở chia đều cho 5 bạn. Mỗi bạn được mấy quyển?", ["8", "35", "45", "200"], 0,
                "Chia đều: 40 : 5 = **8** (quyển)."),
            short("vandung", "Thùng thứ nhất có 245 l nước, thùng thứ hai có nhiều hơn thùng thứ nhất 136 l. Hỏi thùng thứ hai có bao nhiêu lít nước?", ["381"],
                  "Nhiều hơn → cộng: 245 + 136: 5 + 6 = 11, viết 1 nhớ 1; 4 + 3 + 1 = 8; 2 + 1 = 3 → 381.\nĐáp số: **381 l**.", unit="l"),
        ],
    },
]
