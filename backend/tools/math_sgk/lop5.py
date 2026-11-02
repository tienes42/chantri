"""TOÁN 5 — Kết nối tri thức với cuộc sống (tập một, tập hai).

12 chủ đề đánh số trong SGK, đúng thứ tự mục lục.
Mỗi chủ đề: Yêu cầu cần đạt (CT GDPT 2018), kiến thức theo từng bài, công thức/quy tắc,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf

GRADE = 5

LESSONS = [
    # ===================== CHỦ ĐỀ 1 =====================
    {
        "topic": "l5-cd01-on-tap-va-bo-sung",
        "title": "Ôn tập và bổ sung",
        "icon": "🔁",
        "description": "Chủ đề 1 · SGK Toán 5 tập một (tr. 6–31): Bài 1 – Bài 9. Ôn tập số tự nhiên, phân số và các phép tính; phân số thập phân; cộng, trừ hai phân số khác mẫu số; hỗn số; ôn tập hình học và đo lường.",
        "requirements": [
            "Củng cố số tự nhiên, các phép tính với số tự nhiên; phân số, rút gọn, quy đồng, so sánh phân số.",
            "Nhận biết được phân số thập phân.",
            "Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số (quy đồng bằng mẫu số chung).",
            "Nhận biết được hỗn số; chuyển hỗn số thành phân số và ngược lại.",
        ],
        "definition": (
            "- **Phân số thập phân**: phân số có mẫu số là 10, 100, 1000, … (ví dụ 3/10, 47/100). Một số phân số có thể viết thành phân số thập phân: 3/5 = 6/10.\n"
            "- **Cộng, trừ phân số khác mẫu**: quy đồng mẫu số (lấy mẫu số chung, thường là tích hai mẫu hoặc BCNN), rồi cộng/trừ tử số.\n"
            "- **Hỗn số** a b/c gồm phần nguyên a và phần phân số b/c (b/c < 1). Ví dụ 2 3/4 đọc “hai và ba phần tư”; 2 3/4 = (2 × 4 + 3)/4 = 11/4."
        ),
        "theory": (
            "### Bài 1. Ôn tập số tự nhiên\n### Bài 2. Ôn tập các phép tính với số tự nhiên\n### Bài 3. Ôn tập phân số\n"
            "### Bài 4. Phân số thập phân\n- 7/20 = 35/100; 9/25 = 36/100.\n"
            "### Bài 5. Ôn tập các phép tính với phân số\n"
            "### Bài 6. Cộng, trừ hai phân số khác mẫu số\n- 2/3 + 3/4 = 8/12 + 9/12 = 17/12; 3/5 − 1/4 = 12/20 − 5/20 = 7/20.\n"
            "### Bài 7. Hỗn số\n- 13/5 = 2 3/5 (13 : 5 = 2 dư 3).\n"
            "### Bài 8. Ôn tập hình học và đo lường\n### Bài 9. Luyện tập chung"
        ),
        "formulas": [
            G("I. Phân số", F("Phân số thập phân", "Mẫu số 10; 100; 1000; …"), F("Cộng/trừ khác mẫu", "a/b ± c/d = (a × d ± c × b)/(b × d)")),
            G("II. Hỗn số", F("Hỗn số → phân số", "a b/c = (a × c + b)/c", "3 1/2 = 7/2."),
              F("Phân số → hỗn số", "Chia tử cho mẫu: thương là phần nguyên, dư là tử số", "17/4 = 4 1/4.")),
        ],
        "example": "Tính: 1 1/2 + 2 2/3.",
        "example_answer": "1 1/2 = 3/2; 2 2/3 = 8/3. 3/2 + 8/3 = 9/6 + 16/6 = 25/6 = **4 1/6**.",
        "real_life": "- Công thức nấu ăn: 1 1/2 cốc bột; đo chiều dài 2 3/4 m vải.",
        "quiz": [
            mcq("biet", "Phân số nào là phân số thập phân?", ["3/7", "9/100", "5/12", "10/3"], 1, "Mẫu số 100 → **9/100** là phân số thập phân."),
            mcq("biet", "Hỗn số 3 2/5 đọc là:", ["Ba hai phần năm", "Ba và hai phần năm", "Ba phần hai năm", "Ba mươi hai phần năm"], 1, "Đọc “**ba và hai phần năm**”."),
            mcq("biet", "Viết 2 1/3 thành phân số:", ["3/3", "7/3", "5/3", "2/3"], 1, "(2 × 3 + 1)/3 = **7/3**."),
            mcq("biet", "Viết 3/4 thành phân số thập phân:", ["75/100", "34/100", "3/40", "30/40"], 0, "3/4 = (3 × 25)/(4 × 25) = **75/100**."),
            mcq("hieu", "1/2 + 1/3 = ?", ["2/5", "5/6", "1/5", "2/6"], 1, "3/6 + 2/6 = **5/6**.", note="Không cộng tử với tử, mẫu với mẫu."),
            mcq("hieu", "Viết 23/6 thành hỗn số:", ["3 5/6", "3 1/6", "2 5/6", "4 1/6"], 0, "23 : 6 = 3 dư 5 → **3 5/6**."),
            tf("hieu", "Nhận định: “4/5 − 1/3 = 7/15.”", True, "12/15 − 5/15 = 7/15 → **Đúng**."),
            tf("hieu", "Nhận định: “2 3/4 = 6/4.”", False, "2 3/4 = (2 × 4 + 3)/4 = 11/4; 6/4 là kết quả khi nhân nhầm 2 × 3 → **Sai**."),
            mcq("vandung", "Một sợi dây dài 5 m, cắt lần đầu 1 1/2 m, lần sau 2 1/4 m. Còn lại:", ["1 1/4 m", "1 3/4 m", "2 1/4 m", "3 3/4 m"], 0,
                "Đã cắt: 3/2 + 9/4 = 6/4 + 9/4 = 15/4 m. Còn lại: 5 − 15/4 = 20/4 − 15/4 = 5/4 = **1 1/4 m**."),
            short("vandung", "Một bể nước, vòi A chảy 1 giờ được 1/4 bể, vòi B chảy 1 giờ được 1/6 bể. Cả hai vòi cùng chảy 1 giờ được bao nhiêu phần bể? (viết a/b)", ["5/12"],
                  "1/4 + 1/6 = 3/12 + 2/12 = **5/12** (bể)."),
        ],
    },
    # ===================== CHỦ ĐỀ 2 =====================
    {
        "topic": "l5-cd02-so-thap-phan",
        "title": "Số thập phân",
        "icon": "🔟",
        "description": "Chủ đề 2 · SGK Toán 5 tập một (tr. 32–52): Bài 10 – Bài 14. Khái niệm số thập phân; so sánh số thập phân; viết số đo đại lượng dưới dạng số thập phân; làm tròn số thập phân.",
        "requirements": [
            "Đọc, viết được số thập phân; nhận biết được phần nguyên, phần thập phân, hàng của số thập phân.",
            "So sánh được hai số thập phân; sắp xếp được nhóm không quá 4 số thập phân.",
            "Viết được số đo đại lượng (độ dài, khối lượng, diện tích) dưới dạng số thập phân.",
            "Làm tròn được số thập phân đến số tự nhiên gần nhất hoặc đến hàng phần mười, phần trăm.",
        ],
        "definition": (
            "- **Số thập phân** gồm **phần nguyên** (bên trái dấu phẩy) và **phần thập phân** (bên phải dấu phẩy). 0,1 = 1/10; 0,01 = 1/100; 0,001 = 1/1000.\n"
            "- Hàng sau dấu phẩy: **phần mười, phần trăm, phần nghìn**. 25,307: 2 chục, 5 đơn vị, 3 phần mười, 0 phần trăm, 7 phần nghìn.\n"
            "- Thêm (bớt) chữ số 0 ở **tận cùng bên phải phần thập phân** thì số không đổi: 0,5 = 0,50 = 0,500.\n"
            "- **So sánh**: so phần nguyên; nếu bằng thì so lần lượt phần mười, phần trăm, …"
        ),
        "theory": (
            "### Bài 10. Khái niệm số thập phân\n- 3/10 = 0,3; 45/100 = 0,45; 2 7/10 = 2,7.\n"
            "### Bài 11. So sánh các số thập phân\n- 8,45 < 8,5 (cùng phần nguyên 8; phần mười 4 < 5).\n"
            "### Bài 12. Viết số đo đại lượng dưới dạng số thập phân\n- 3 m 25 cm = 3,25 m; 4 kg 50 g = 4,05 kg; 5 m² 7 dm² = 5,07 m².\n"
            "### Bài 13. Làm tròn số thập phân\n- 7,46 làm tròn đến số tự nhiên gần nhất: 7; đến hàng phần mười: 7,5.\n"
            "### Bài 14. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cấu tạo", F("Giá trị hàng", "0,1 = 1/10 · 0,01 = 1/100 · 0,001 = 1/1000"),
              F("Chữ số 0 tận cùng", "a,b = a,b0 = a,b00")),
            G("II. So sánh – làm tròn", F("So sánh", "Phần nguyên → phần mười → phần trăm → …"),
              F("Làm tròn", "Xét chữ số ngay bên phải hàng làm tròn: < 5 giữ; ≥ 5 tăng 1", "12,348 → phần trăm: 12,35.")),
            G("III. Đổi đơn vị", F("Độ dài", "1 cm = 0,01 m · 1 mm = 0,001 m"), F("Khối lượng", "1 g = 0,001 kg · 1 kg = 0,001 tấn")),
        ],
        "example": "Viết số đo sau dưới dạng số thập phân có đơn vị mét: 6 m 8 cm; 45 cm.",
        "example_answer": "6 m 8 cm = 6 8/100 m = **6,08 m**; 45 cm = 45/100 m = **0,45 m**.",
        "real_life": "- Giá tiền, chiều cao (1,45 m), cân nặng (32,5 kg), thành tích chạy (12,8 giây).",
        "quiz": [
            mcq("biet", "Phân số 7/100 viết dưới dạng số thập phân là:", ["0,7", "0,07", "7,00", "0,007"], 1, "7/100 = **0,07**."),
            mcq("biet", "Trong số 32,581, chữ số 8 thuộc hàng:", ["Phần mười", "Phần trăm", "Phần nghìn", "Đơn vị"], 1, "Sau dấu phẩy: 5 (phần mười), **8 (phần trăm)**, 1 (phần nghìn)."),
            mcq("biet", "Số thập phân gồm 5 đơn vị và 3 phần mười viết là:", ["5,03", "5,3", "53", "0,53"], 1, "**5,3**."),
            mcq("biet", "Số 4,50 bằng số nào?", ["4,05", "4,5", "45", "4,005"], 1, "Bỏ chữ số 0 tận cùng phần thập phân: **4,5**."),
            mcq("hieu", "Số lớn nhất trong các số 7,09; 7,9; 7,089; 7,19 là:", ["7,09", "7,9", "7,089", "7,19"], 1, "Cùng phần nguyên 7; phần mười lớn nhất là 9 → **7,9**.", note="Không so sánh theo “số chữ số nhiều hơn”."),
            mcq("hieu", "2 kg 35 g = … kg?", ["2,35", "2,035", "23,5", "2,0035"], 1, "35 g = 35/1000 kg = 0,035 kg → **2,035 kg**."),
            tf("hieu", "Nhận định: “0,8 > 0,75.”", True, "Phần mười 8 > 7 → **Đúng**."),
            tf("hieu", "Nhận định: “Làm tròn 15,46 đến số tự nhiên gần nhất được 16.”", False, "Chữ số phần mười là 4 < 5 → làm tròn xuống 15 → **Sai**."),
            mcq("vandung", "Chiều cao của bốn bạn: An 1,42 m; Bình 1,4 m; Chi 1,38 m; Dũng 1,45 m. Bạn thấp nhất là:", ["An", "Bình", "Chi", "Dũng"], 2,
                "1,38 < 1,40 < 1,42 < 1,45 → **Chi** thấp nhất."),
            short("vandung", "Một con đường dài 3 km 75 m. Viết độ dài con đường dưới dạng số thập phân với đơn vị ki-lô-mét.", ["3,075", "3.075"],
                  "75 m = 75/1000 km = 0,075 km → **3,075 km**.", unit="km", note="Lỗi hay gặp: viết 3,75 km."),
        ],
    },
    # ===================== CHỦ ĐỀ 3 =====================
    {
        "topic": "l5-cd03-don-vi-do-dien-tich",
        "title": "Một số đơn vị đo diện tích",
        "icon": "🗺️",
        "description": "Chủ đề 3 · SGK Toán 5 tập một (tr. 53–64): Bài 15 – Bài 18. Ki-lô-mét vuông, héc-ta; các đơn vị đo diện tích; thực hành trải nghiệm với một số đơn vị đo đại lượng.",
        "requirements": [
            "Nhận biết được các đơn vị đo diện tích km² (ki-lô-mét vuông), ha (héc-ta) và quan hệ với m².",
            "Nắm được bảng đơn vị đo diện tích; chuyển đổi, so sánh, tính toán với các số đo diện tích.",
            "Ước lượng và giải quyết vấn đề thực tế liên quan đến diện tích (đất đai, ruộng vườn, lãnh thổ).",
        ],
        "definition": (
            "- **Ki-lô-mét vuông** (km²): diện tích hình vuông cạnh 1 km; 1 km² = 1 000 000 m².\n"
            "- **Héc-ta** (ha): 1 ha = 1 hm² = 10 000 m²; 1 km² = 100 ha.\n"
            "- **Bảng đơn vị đo diện tích**: km² – hm² (ha) – dam² – m² – dm² – cm² – mm²; hai đơn vị liền kề hơn kém nhau **100 lần**."
        ),
        "theory": (
            "### Bài 15. Ki-lô-mét vuông. Héc-ta\n- Diện tích Hà Nội khoảng 3359 km²; một thửa ruộng 2 ha.\n"
            "### Bài 16. Các đơn vị đo diện tích\n- Mỗi đơn vị ứng với **2 chữ số** khi viết số đo: 3 m² 5 dm² = 3,05 m².\n"
            "### Bài 17. Thực hành và trải nghiệm với một số đơn vị đo đại lượng\n"
            "### Bài 18. Luyện tập chung"
        ),
        "formulas": [
            G("I. Bảng đơn vị", F("Thứ tự", "km² → hm² (ha) → dam² → m² → dm² → cm² → mm²"), F("Liền kề", "Gấp (kém) nhau 100 lần")),
            G("II. Quan hệ cần nhớ", F("Héc-ta", "1 ha = 10 000 m²"), F("Ki-lô-mét vuông", "1 km² = 100 ha = 1 000 000 m²")),
        ],
        "example": "Đổi: 3 ha = … m²; 25 000 m² = … ha; 4 km² = … ha.",
        "example_answer": "3 ha = **30 000 m²**; 25 000 m² = **2,5 ha**; 4 km² = **400 ha**.",
        "real_life": "- Diện tích quốc gia, tỉnh thành (km²); diện tích ruộng, rừng (ha); diện tích căn hộ (m²).",
        "quiz": [
            mcq("biet", "1 ha = … m²?", ["100", "1000", "10 000", "1 000 000"], 2, "1 ha = **10 000 m²**."),
            mcq("biet", "1 km² = … ha?", ["10", "100", "1000", "10 000"], 1, "1 km² = **100 ha**."),
            mcq("biet", "Hai đơn vị đo diện tích liền kề hơn kém nhau:", ["10 lần", "100 lần", "1000 lần", "60 lần"], 1, "Liền kề hơn kém **100 lần**."),
            mcq("biet", "Đơn vị thích hợp để đo diện tích một quốc gia là:", ["m²", "dm²", "km²", "cm²"], 2, "Diện tích rất lớn → **km²**."),
            mcq("hieu", "5 m² 8 dm² = … m²?", ["5,8", "5,08", "58", "5,008"], 1, "8 dm² = 8/100 m² = 0,08 m² → **5,08 m²**.", note="Mỗi đơn vị diện tích ứng với 2 chữ số."),
            mcq("hieu", "45 000 m² = … ha?", ["45", "4,5", "450", "0,45"], 1, "45 000 : 10 000 = **4,5 ha**."),
            tf("hieu", "Nhận định: “2 km² = 2 000 000 m².”", True, "1 km² = 1 000 000 m² → **Đúng**."),
            tf("hieu", "Nhận định: “1 m² = 10 dm².”", False, "1 m² = **100** dm² → **Sai**."),
            mcq("vandung", "Một khu rừng hình chữ nhật dài 2 km, rộng 800 m. Diện tích khu rừng là:", ["160 ha", "1600 ha", "16 ha", "1,6 ha"], 0,
                "Đổi 2 km = 2000 m. S = 2000 × 800 = 1 600 000 m² = **160 ha**."),
            short("vandung", "Một thửa ruộng diện tích 3 ha. Trung bình 100 m² thu được 60 kg thóc. Cả thửa ruộng thu được bao nhiêu tấn thóc?", ["18"],
                  "3 ha = 30 000 m². Số lần 100 m²: 30 000 : 100 = 300. Thóc: 60 × 300 = 18 000 kg = 18 tấn.\nĐáp số: **18 tấn**.", unit="tấn"),
        ],
    },
    # ===================== CHỦ ĐỀ 4 =====================
    {
        "topic": "l5-cd04-phep-tinh-so-thap-phan",
        "title": "Các phép tính với số thập phân",
        "icon": "🧮",
        "description": "Chủ đề 4 · SGK Toán 5 tập một (tr. 65–90): Bài 19 – Bài 24. Phép cộng, trừ, nhân, chia số thập phân; nhân, chia số thập phân với 10; 100; 1000; … hoặc với 0,1; 0,01; 0,001; …",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ, phép nhân, phép chia số thập phân.",
            "Thực hiện được nhân, chia nhẩm số thập phân với 10; 100; 1000; … và với 0,1; 0,01; 0,001; …",
            "Vận dụng tính chất các phép tính để tính hợp lí; giải bài toán thực tế với số thập phân.",
        ],
        "definition": (
            "- **Cộng, trừ**: đặt tính sao cho các **dấu phẩy thẳng cột**; tính như số tự nhiên; đặt dấu phẩy ở kết quả thẳng cột.\n"
            "- **Nhân**: nhân như số tự nhiên; đếm tổng số chữ số ở phần thập phân của hai thừa số rồi tách ở tích bấy nhiêu chữ số từ phải sang trái.\n"
            "- **Chia**: chia số thập phân cho số tự nhiên — khi chia hết phần nguyên thì viết dấu phẩy vào thương; chia cho số thập phân — dời dấu phẩy ở số chia và số bị chia sang phải cùng số chữ số để số chia thành số tự nhiên.\n"
            "- **× 10, 100, 1000**: dời dấu phẩy sang **phải** 1, 2, 3 chữ số; **× 0,1; 0,01; 0,001** (hay : 10, 100, 1000): dời dấu phẩy sang **trái** 1, 2, 3 chữ số."
        ),
        "theory": (
            "### Bài 19. Phép cộng số thập phân\n- 15,6 + 7,48 = 23,08.\n"
            "### Bài 20. Phép trừ số thập phân\n- 25,3 − 8,47 = 16,83 (viết 25,30).\n"
            "### Bài 21. Phép nhân số thập phân\n- 2,4 × 1,5 = 3,60 = 3,6 (tổng 2 chữ số thập phân).\n"
            "### Bài 22. Phép chia số thập phân\n- 8,4 : 4 = 2,1; 9 : 0,6 = 90 : 6 = 15; 12,6 : 0,35 = 1260 : 35 = 36.\n"
            "### Bài 23. Nhân, chia số thập phân với 10; 100; 1 000; … hoặc với 0,1; 0,01; 0,001; …\n- 3,72 × 100 = 372; 45,6 × 0,01 = 0,456; 7,5 : 10 = 0,75.\n"
            "### Bài 24. Luyện tập chung"
        ),
        "formulas": [
            G("I. Cộng, trừ, nhân", F("Cộng/trừ", "Dấu phẩy thẳng cột"), F("Nhân", "Số chữ số thập phân của tích = tổng của hai thừa số", "0,25 × 0,4 = 0,100 = 0,1.")),
            G("II. Chia", F("Chia cho số thập phân", "a : b = (a × 10ⁿ) : (b × 10ⁿ)", "4,5 : 0,15 = 450 : 15 = 30.")),
            G("III. Nhân/chia nhẩm", F("× 10ⁿ hoặc : 0,1…", "Dời dấu phẩy sang phải n chữ số"), F(": 10ⁿ hoặc × 0,1…", "Dời dấu phẩy sang trái n chữ số")),
        ],
        "example": "Một ô tô đi 100 km hết 8,5 l xăng. Hỏi đi 250 km hết bao nhiêu lít xăng?",
        "example_answer": "1 km hết 8,5 : 100 = 0,085 (l). 250 km hết 0,085 × 250 = **21,25 l**.",
        "real_life": "- Tính tiền khi mua 2,5 kg thịt giá 120 000 đồng/kg; chia đều 7,5 m vải.",
        "quiz": [
            mcq("biet", "12,5 + 3,47 = ?", ["15,97", "16,22", "4,72", "15,52"], 0, "Đặt thẳng dấu phẩy: 12,50 + 3,47 = **15,97**.", note="Đặt 3,47 lệch sang trái sẽ ra 4,72."),
            mcq("biet", "4,5 × 10 = ?", ["0,45", "45", "450", "4,50"], 1, "Dời dấu phẩy sang phải 1 chữ số → **45**."),
            mcq("biet", "36,8 : 100 = ?", ["3680", "3,68", "0,368", "0,0368"], 2, "Dời dấu phẩy sang trái 2 chữ số → **0,368**."),
            mcq("biet", "1,2 × 3 = ?", ["3,6", "36", "0,36", "4,2"], 0, "12 × 3 = 36, tách 1 chữ số thập phân → **3,6**."),
            mcq("hieu", "2,5 × 0,4 = ?", ["10", "1", "0,1", "0,01"], 1, "25 × 4 = 100; tổng 2 chữ số thập phân → 1,00 = **1**."),
            mcq("hieu", "7,2 : 0,8 = ?", ["0,9", "9", "90", "5,76"], 1, "Dời dấu phẩy: 72 : 8 = **9**."),
            tf("hieu", "Nhận định: “20 − 7,35 = 12,65.”", True, "20,00 − 7,35 = 12,65 → **Đúng**.", alt="Thử lại: 12,65 + 7,35 = 20."),
            tf("hieu", "Nhận định: “Nhân một số thập phân với 0,1 là dời dấu phẩy sang phải một chữ số.”", False, "× 0,1 tức là chia cho 10 → dời dấu phẩy sang **trái** → **Sai**."),
            mcq("vandung", "Mua 2,5 kg táo, mỗi ki-lô-gam giá 48 000 đồng. Số tiền phải trả là:", ["120 000 đồng", "96 000 đồng", "12 000 đồng", "125 000 đồng"], 0,
                "48 000 × 2,5 = **120 000 đồng**."),
            short("vandung", "Một tấm vải dài 22,5 m được cắt thành các mảnh, mỗi mảnh dài 1,5 m. Cắt được bao nhiêu mảnh?", ["15"],
                  "22,5 : 1,5 = 225 : 15 = 15 (mảnh).\nĐáp số: **15 mảnh**.", unit="mảnh"),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 5 =====================
    {
        "topic": "l5-cd05-hinh-phang-chu-vi-dien-tich",
        "title": "Một số hình phẳng. Chu vi và diện tích",
        "icon": "🔺",
        "description": "Chủ đề 5 · SGK Toán 5 tập một (tr. 91–119): Bài 25 – Bài 29. Hình tam giác, diện tích hình tam giác; hình thang, diện tích hình thang; đường tròn, chu vi và diện tích hình tròn; thực hành đo, vẽ, lắp ghép, tạo hình.",
        "requirements": [
            "Nhận biết được hình tam giác (đáy, đường cao), hình thang (hai đáy, chiều cao), đường tròn, hình tròn.",
            "Tính được diện tích hình tam giác, hình thang; chu vi và diện tích hình tròn.",
            "Vẽ được đường cao của hình tam giác; giải quyết vấn đề thực tế liên quan đến đo, vẽ, lắp ghép, tạo hình.",
        ],
        "definition": (
            "- **Đường cao** của tam giác: đoạn thẳng kẻ từ một đỉnh vuông góc với cạnh đối diện (đáy).\n"
            "- **Hình thang**: tứ giác có **một cặp cạnh đối diện song song** (hai đáy). Hình thang vuông có một cạnh bên vuông góc với hai đáy.\n"
            "- **Đường tròn tâm O bán kính r**; đường kính d = 2 × r. Số π ≈ **3,14**."
        ),
        "theory": (
            "### Bài 25. Hình tam giác. Diện tích hình tam giác\n- Tam giác đáy 8 cm, chiều cao 5 cm: S = 8 × 5 : 2 = 20 cm².\n"
            "### Bài 26. Hình thang. Diện tích hình thang\n- Đáy 6 cm và 4 cm, cao 3 cm: S = (6 + 4) × 3 : 2 = 15 cm².\n"
            "### Bài 27. Đường tròn. Chu vi và diện tích hình tròn\n- r = 2 cm: C = 2 × 2 × 3,14 = 12,56 cm; S = 2 × 2 × 3,14 = 12,56 cm².\n"
            "### Bài 28. Thực hành và trải nghiệm đo, vẽ, lắp ghép, tạo hình\n"
            "### Bài 29. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tam giác", F("Diện tích", "S = a × h : 2", "a: độ dài đáy, h: chiều cao (cùng đơn vị)."),
              F("Tam giác vuông", "S = (cạnh góc vuông × cạnh góc vuông) : 2")),
            G("II. Hình thang", F("Diện tích", "S = (a + b) × h : 2", "a, b: hai đáy; h: chiều cao.")),
            G("III. Hình tròn", F("Chu vi", "C = d × 3,14 = r × 2 × 3,14"), F("Diện tích", "S = r × r × 3,14")),
        ],
        "example": "Một mảnh đất hình thang có đáy lớn 25 m, đáy bé 15 m, chiều cao 12 m. Tính diện tích.",
        "example_answer": "S = (25 + 15) × 12 : 2 = 40 × 12 : 2 = **240 m²**.",
        "real_life": "- Tính diện tích mái nhà hình tam giác, ruộng hình thang; chu vi bánh xe (một vòng lăn được bao xa).",
        "quiz": [
            mcq("biet", "Công thức diện tích hình tam giác là:", ["a × h", "a × h : 2", "(a + b) × h : 2", "r × r × 3,14"], 1, "S = **a × h : 2**."),
            mcq("biet", "Hình thang có:", ["Hai cặp cạnh song song", "Một cặp cạnh đối diện song song", "Bốn cạnh bằng nhau", "Không có cạnh song song"], 1, "Hình thang có **một cặp cạnh đối diện song song**."),
            mcq("biet", "Chu vi hình tròn đường kính d là:", ["d × 3,14", "d × d × 3,14", "d : 3,14", "d × 2"], 0, "C = **d × 3,14**."),
            mcq("biet", "Diện tích hình tròn bán kính r là:", ["r × 2 × 3,14", "r × r × 3,14", "r × 3,14", "d × 3,14"], 1, "S = **r × r × 3,14**."),
            mcq("hieu", "Tam giác có đáy 12 cm, chiều cao 7 cm. Diện tích là:", ["84 cm²", "42 cm²", "19 cm²", "38 cm²"], 1, "12 × 7 : 2 = **42 cm²**."),
            mcq("hieu", "Hình tròn bán kính 5 cm có chu vi là:", ["15,7 cm", "31,4 cm", "78,5 cm", "25 cm"], 1, "C = 5 × 2 × 3,14 = **31,4 cm**."),
            tf("hieu", "Nhận định: “Hình tròn bán kính 10 cm có diện tích 314 cm².”", True, "10 × 10 × 3,14 = 314 → **Đúng**."),
            tf("hieu", "Nhận định: “Hình thang đáy 8 m và 6 m, cao 5 m có diện tích 70 m².”", False, "(8 + 6) × 5 : 2 = 35 m²; quên chia 2 sẽ ra 70 → **Sai**."),
            mcq("vandung", "Bánh xe đạp có đường kính 0,65 m. Bánh xe lăn 100 vòng thì xe đi được:", ["204,1 m", "65 m", "20,41 m", "2041 m"], 0,
                "Một vòng: 0,65 × 3,14 = 2,041 m. 100 vòng: **204,1 m**."),
            short("vandung", "Một tấm biển hình tam giác vuông có hai cạnh góc vuông 60 cm và 45 cm. Tính diện tích tấm biển (cm²).", ["1350"],
                  "S = 60 × 45 : 2 = 1350 (cm²).\nĐáp số: **1350 cm²**.", unit="cm²"),
        ],
    },
    # ===================== CHỦ ĐỀ 6 =====================
    {
        "topic": "l5-cd06-on-tap-hoc-ki-1",
        "title": "Ôn tập học kì 1",
        "icon": "📝",
        "description": "Chủ đề 6 · SGK Toán 5 tập một (tr. 120–138): Bài 30 – Bài 35. Ôn tập số thập phân; các phép tính với số thập phân; một số hình phẳng; diện tích, chu vi; đo lường.",
        "requirements": [
            "Củng cố đọc, viết, so sánh, làm tròn số thập phân; bốn phép tính với số thập phân.",
            "Củng cố diện tích tam giác, hình thang; chu vi, diện tích hình tròn.",
            "Chuyển đổi các đơn vị đo độ dài, khối lượng, diện tích (km², ha) dưới dạng số thập phân.",
        ],
        "definition": (
            "- Số thập phân: phần nguyên, phần thập phân; dời dấu phẩy khi × / : 10, 100, 1000.\n"
            "- Tam giác: S = a × h : 2; hình thang: S = (a + b) × h : 2; hình tròn: C = d × 3,14; S = r × r × 3,14.\n"
            "- Diện tích: 1 ha = 10 000 m²; 1 km² = 100 ha."
        ),
        "theory": (
            "### Bài 30. Ôn tập số thập phân\n### Bài 31. Ôn tập các phép tính với số thập phân\n### Bài 32. Ôn tập một số hình phẳng\n"
            "### Bài 33. Ôn tập diện tích, chu vi một số hình phẳng\n### Bài 34. Ôn tập đo lường\n### Bài 35. Ôn tập chung"
        ),
        "formulas": [
            G("I. Phép tính", F("Nhân", "Tách số chữ số thập phân = tổng của hai thừa số"), F("Chia cho số thập phân", "Dời dấu phẩy để số chia thành số tự nhiên")),
            G("II. Hình phẳng", F("Tam giác", "S = a × h : 2"), F("Hình thang", "S = (a + b) × h : 2"), F("Hình tròn", "C = d × 3,14 · S = r × r × 3,14")),
        ],
        "example": "Tính: (12,5 − 4,7) × 2,4.",
        "example_answer": "12,5 − 4,7 = 7,8; 7,8 × 2,4 = **18,72**.",
        "real_life": "- Tính chi phí sơn một bức tường hình thang; tính tiền điện theo số kWh lẻ.",
        "quiz": [
            mcq("biet", "Số “mười hai phẩy không năm” viết là:", ["12,5", "12,05", "12,005", "1205"], 1, "**12,05**."),
            mcq("biet", "0,75 × 100 = ?", ["7,5", "75", "750", "0,0075"], 1, "Dời dấu phẩy sang phải 2 chữ số → **75**."),
            mcq("biet", "3 m² = … dm²?", ["30", "300", "3000", "0,03"], 1, "1 m² = 100 dm² → **300 dm²**."),
            mcq("biet", "Hình tròn đường kính 8 cm có bán kính:", ["16 cm", "4 cm", "8 cm", "25,12 cm"], 1, "r = 8 : 2 = **4 cm**."),
            mcq("hieu", "Làm tròn 6,358 đến hàng phần mười được:", ["6,3", "6,4", "6,36", "6"], 1, "Chữ số phần trăm 5 ≥ 5 → **6,4**."),
            mcq("hieu", "9,6 : 2,4 = ?", ["4", "0,4", "40", "23,04"], 0, "96 : 24 = **4**."),
            tf("hieu", "Nhận định: “Tam giác đáy 4,5 m, chiều cao 2 m có diện tích 4,5 m².”", True, "4,5 × 2 : 2 = 4,5 m² → **Đúng**."),
            tf("hieu", "Nhận định: “3,5 × 0,2 = 7.”", False, "35 × 2 = 70, tách 2 chữ số thập phân → 0,70 = 0,7 → **Sai**."),
            mcq("vandung", "Một hình tròn có chu vi 18,84 cm. Diện tích hình tròn đó là:", ["28,26 cm²", "113,04 cm²", "9,42 cm²", "56,52 cm²"], 0,
                "d = 18,84 : 3,14 = 6 cm ⇒ r = 3 cm. S = 3 × 3 × 3,14 = **28,26 cm²**."),
            short("vandung", "Một thửa ruộng hình thang có đáy lớn 120 m, đáy bé 80 m, chiều cao 50 m. Diện tích thửa ruộng là bao nhiêu héc-ta?", ["0,5", "0.5"],
                  "S = (120 + 80) × 50 : 2 = 5000 m² = 0,5 ha.\nĐáp số: **0,5 ha**.", unit="ha"),
        ],
    },
    # ===================== CHỦ ĐỀ 7 =====================
    {
        "topic": "l5-cd07-ti-so-va-bai-toan-lien-quan",
        "title": "Tỉ số và các bài toán liên quan",
        "icon": "📈",
        "description": "Chủ đề 7 · SGK Toán 5 tập hai (tr. 4–29): Bài 36 – Bài 44. Tỉ số, tỉ số phần trăm; tỉ lệ bản đồ; tìm hai số khi biết tổng (hiệu) và tỉ số; tìm tỉ số phần trăm của hai số; tìm giá trị phần trăm của một số; máy tính cầm tay.",
        "requirements": [
            "Nhận biết được tỉ số, tỉ số phần trăm của hai đại lượng cùng loại; tỉ lệ bản đồ.",
            "Giải được bài toán tìm hai số khi biết tổng (hoặc hiệu) và tỉ số của hai số đó.",
            "Tìm được tỉ số phần trăm của hai số; tìm được giá trị phần trăm của một số.",
            "Sử dụng được máy tính cầm tay để thực hiện các phép tính và tính tỉ số phần trăm.",
        ],
        "definition": (
            "- **Tỉ số** của a và b (b ≠ 0) là a : b hay a/b.\n"
            "- **Tỉ số phần trăm**: tỉ số viết dưới dạng mẫu 100, kí hiệu %: 25/100 = 25%.\n"
            "- **Tỉ lệ bản đồ** 1 : 1000 nghĩa là 1 cm trên bản đồ ứng với 1000 cm thực tế.\n"
            "- **Tổng – tỉ**: vẽ sơ đồ, tìm tổng số phần bằng nhau; giá trị 1 phần = Tổng : số phần. **Hiệu – tỉ**: giá trị 1 phần = Hiệu : hiệu số phần."
        ),
        "theory": (
            "### Bài 36. Tỉ số. Tỉ số phần trăm\n- 3 : 4 = 0,75 = 75%.\n"
            "### Bài 37. Tỉ lệ bản đồ và ứng dụng\n- Tỉ lệ 1 : 500 000, đoạn 4 cm ⇒ thực tế 2 000 000 cm = 20 km.\n"
            "### Bài 38. Tìm hai số khi biết tổng và tỉ số của hai số đó\n- Tổng 45, tỉ số 2/3: tổng 5 phần; 1 phần = 9; số bé 18, số lớn 27.\n"
            "### Bài 39. Tìm hai số khi biết hiệu và tỉ số của hai số đó\n- Hiệu 12, tỉ số 3/5: hiệu 2 phần; 1 phần = 6; số bé 18, số lớn 30.\n"
            "### Bài 40. Tìm tỉ số phần trăm của hai số\n- 18 và 24: 18 : 24 = 0,75 = 75%.\n"
            "### Bài 41. Tìm giá trị phần trăm của một số\n- 15% của 320 = 320 × 15 : 100 = 48.\n"
            "### Bài 42. Máy tính cầm tay\n### Bài 43. Thực hành và trải nghiệm sử dụng máy tính cầm tay\n### Bài 44. Luyện tập chung"
        ),
        "formulas": [
            G("I. Tỉ số – phần trăm", F("Tỉ số phần trăm của a và b", "a : b × 100 (%)"), F("m% của A", "A × m : 100"),
              F("Tìm số khi biết m% của nó là B", "B : m × 100")),
            G("II. Tổng/Hiệu – tỉ (tỉ số m/n)", F("Tổng – tỉ", "1 phần = Tổng : (m + n)"), F("Hiệu – tỉ", "1 phần = Hiệu : (n − m)")),
            G("III. Tỉ lệ bản đồ 1 : k", F("Độ dài thật", "Độ dài trên bản đồ × k"), F("Độ dài trên bản đồ", "Độ dài thật : k")),
        ],
        "example": "Một lớp có 40 học sinh, trong đó có 18 học sinh nữ. Tính tỉ số phần trăm của số học sinh nữ và số học sinh cả lớp.",
        "example_answer": "18 : 40 = 0,45 = **45%**.",
        "real_life": "- Giảm giá 20%, lãi suất tiết kiệm, tỉ lệ đậu; đọc bản đồ để tính quãng đường thật.",
        "quiz": [
            mcq("biet", "Tỉ số của 3 và 5 là:", ["5/3", "3/5", "8", "15"], 1, "Tỉ số của a và b là a/b → **3/5**."),
            mcq("biet", "0,35 viết dưới dạng tỉ số phần trăm là:", ["3,5%", "35%", "350%", "0,35%"], 1, "0,35 = 35/100 = **35%**."),
            mcq("biet", "Bản đồ tỉ lệ 1 : 1000. Độ dài 1 cm trên bản đồ ứng với độ dài thật:", ["1000 m", "10 m", "100 m", "1 m"], 1, "1 cm × 1000 = 1000 cm = **10 m**."),
            mcq("biet", "Muốn tìm 20% của 150, ta tính:", ["150 : 20", "150 × 20 : 100", "150 × 100 : 20", "150 + 20"], 1, "m% của A = **A × m : 100**."),
            mcq("hieu", "Tổng hai số là 60, tỉ số của chúng là 1/4. Số lớn là:", ["12", "48", "15", "45"], 1, "Tổng 5 phần; 1 phần = 60 : 5 = 12; số lớn = 12 × 4 = **48**."),
            mcq("hieu", "Tỉ số phần trăm của 9 và 12 là:", ["75%", "7,5%", "133%", "0,75%"], 0, "9 : 12 = 0,75 = **75%**."),
            tf("hieu", "Nhận định: “Hiệu hai số là 20, tỉ số là 3/7 thì số bé là 15.”", True, "Hiệu số phần 7 − 3 = 4; 1 phần = 5; số bé = 5 × 3 = 15 → **Đúng**."),
            tf("hieu", "Nhận định: “25% của 80 là 32.”", False, "80 × 25 : 100 = 20 → **Sai**."),
            mcq("vandung", "Một chiếc áo giá 250 000 đồng, được giảm giá 20%. Giá áo sau khi giảm là:", ["200 000 đồng", "50 000 đồng", "230 000 đồng", "300 000 đồng"], 0,
                "Số tiền giảm: 250 000 × 20 : 100 = 50 000. Giá mới: 250 000 − 50 000 = **200 000 đồng**.", alt="Giá mới = 80% giá cũ: 250 000 × 80 : 100 = 200 000."),
            short("vandung", "Trên bản đồ tỉ lệ 1 : 2 000 000, quãng đường từ A đến B dài 5 cm. Quãng đường thật dài bao nhiêu ki-lô-mét?", ["100"],
                  "5 × 2 000 000 = 10 000 000 cm = 100 km.\nĐáp số: **100 km**.", unit="km"),
        ],
    },
    # ===================== CHỦ ĐỀ 8 =====================
    {
        "topic": "l5-cd08-the-tich-don-vi-do-the-tich",
        "title": "Thể tích. Đơn vị đo thể tích",
        "icon": "🧊",
        "description": "Chủ đề 8 · SGK Toán 5 tập hai (tr. 30–39): Bài 45 – Bài 48. Thể tích của một hình; xăng-ti-mét khối, đề-xi-mét khối; mét khối.",
        "requirements": [
            "Nhận biết được “thể tích” thông qua biểu tượng cụ thể.",
            "Nhận biết được các đơn vị đo thể tích cm³, dm³, m³ và quan hệ giữa chúng.",
            "Chuyển đổi, so sánh, tính toán được với các số đo thể tích; liên hệ với dung tích (1 dm³ = 1 l).",
        ],
        "definition": (
            "- **Thể tích** là phần không gian mà một vật chiếm chỗ.\n"
            "- **1 cm³** là thể tích hình lập phương cạnh 1 cm; **1 dm³** là thể tích hình lập phương cạnh 1 dm; **1 m³** là thể tích hình lập phương cạnh 1 m.\n"
            "- 1 dm³ = 1000 cm³; 1 m³ = 1000 dm³ = 1 000 000 cm³. Hai đơn vị thể tích liền kề hơn kém nhau **1000 lần**.\n"
            "- **1 dm³ = 1 l**; 1 cm³ = 1 ml."
        ),
        "theory": (
            "### Bài 45. Thể tích của một hình\n- So sánh thể tích bằng cách đếm số hình lập phương nhỏ xếp thành hình.\n"
            "### Bài 46. Xăng-ti-mét khối. Đề-xi-mét khối\n- 5 dm³ = 5000 cm³.\n"
            "### Bài 47. Mét khối\n- 2,5 m³ = 2500 dm³.\n"
            "### Bài 48. Luyện tập chung"
        ),
        "formulas": [
            G("I. Đơn vị thể tích", F("Quan hệ", "1 m³ = 1000 dm³ · 1 dm³ = 1000 cm³"), F("Liền kề", "Gấp (kém) 1000 lần — mỗi đơn vị ứng với 3 chữ số")),
            G("II. Liên hệ dung tích", F("Lít", "1 dm³ = 1 l · 1 cm³ = 1 ml · 1 m³ = 1000 l")),
        ],
        "example": "Đổi: 3,2 m³ = … dm³; 4500 cm³ = … dm³; 7 dm³ = … l.",
        "example_answer": "3,2 m³ = **3200 dm³**; 4500 cm³ = **4,5 dm³**; 7 dm³ = **7 l**.",
        "real_life": "- Thể tích bể nước (m³), đọc chỉ số đồng hồ nước (m³); dung tích chai nước (l, ml).",
        "quiz": [
            mcq("biet", "1 dm³ = … cm³?", ["10", "100", "1000", "10 000"], 2, "1 dm³ = **1000 cm³**."),
            mcq("biet", "1 m³ = … dm³?", ["100", "1000", "10", "1 000 000"], 1, "1 m³ = **1000 dm³**."),
            mcq("biet", "1 dm³ bằng:", ["1 ml", "1 l", "10 l", "100 ml"], 1, "1 dm³ = **1 l**."),
            mcq("biet", "Thể tích hình lập phương cạnh 1 cm là:", ["1 cm", "1 cm²", "1 cm³", "6 cm²"], 2, "Đó là **1 cm³**."),
            mcq("hieu", "2 m³ 15 dm³ = … m³?", ["2,15", "2,015", "2,0015", "215"], 1, "15 dm³ = 0,015 m³ → **2,015 m³**.", note="Mỗi đơn vị thể tích ứng với 3 chữ số."),
            mcq("hieu", "Một bể chứa 3 m³ nước. Bể chứa bao nhiêu lít nước?", ["300 l", "3000 l", "30 000 l", "30 l"], 1, "3 m³ = 3000 dm³ = **3000 l**."),
            tf("hieu", "Nhận định: “0,5 dm³ = 500 cm³.”", True, "0,5 × 1000 = 500 → **Đúng**."),
            tf("hieu", "Nhận định: “1 m³ = 100 dm³.”", False, "1 m³ = **1000** dm³ → **Sai**."),
            mcq("vandung", "Một hình được xếp từ 4 lớp, mỗi lớp 6 hình lập phương cạnh 1 cm. Thể tích của hình là:", ["10 cm³", "24 cm³", "24 cm²", "64 cm³"], 1,
                "Số hình lập phương: 6 × 4 = 24 → thể tích **24 cm³**."),
            short("vandung", "Gia đình An tháng này dùng hết 18 m³ nước. Hỏi gia đình An đã dùng bao nhiêu lít nước?", ["18000", "18 000"],
                  "1 m³ = 1000 l ⇒ 18 m³ = **18 000 l**.", unit="l"),
        ],
    },
]

LESSONS += [
    # ===================== CHỦ ĐỀ 9 =====================
    {
        "topic": "l5-cd09-dien-tich-the-tich-hinh-khoi",
        "title": "Diện tích và thể tích của một số hình khối",
        "icon": "📦",
        "description": "Chủ đề 9 · SGK Toán 5 tập hai (tr. 40–63): Bài 49 – Bài 55. Hình khai triển của hình lập phương, hình hộp chữ nhật, hình trụ; diện tích xung quanh, diện tích toàn phần của hình hộp chữ nhật, hình lập phương; thể tích hình hộp chữ nhật, hình lập phương.",
        "requirements": [
            "Nhận biết được hình khai triển của hình lập phương, hình hộp chữ nhật, hình trụ.",
            "Tính được diện tích xung quanh, diện tích toàn phần của hình hộp chữ nhật, hình lập phương.",
            "Tính được thể tích hình hộp chữ nhật, hình lập phương.",
            "Ước lượng và giải quyết vấn đề thực tế liên quan đến diện tích, thể tích các hình khối.",
        ],
        "definition": (
            "- **Hình hộp chữ nhật** có 6 mặt là hình chữ nhật; ba kích thước: chiều dài a, chiều rộng b, chiều cao c.\n"
            "- **Hình lập phương** có 6 mặt là hình vuông bằng nhau, cạnh a.\n"
            "- **Diện tích xung quanh** (Sxq): tổng diện tích 4 mặt bên. **Diện tích toàn phần** (Stp): Sxq + diện tích hai đáy.\n"
            "- **Hình khai triển**: “mở” hình khối trải phẳng; hình trụ khai triển gồm 1 hình chữ nhật và 2 hình tròn."
        ),
        "theory": (
            "### Bài 49. Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ\n"
            "### Bài 50. Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật\n- a = 5, b = 4, c = 3 (cm): Sxq = (5 + 4) × 2 × 3 = 54 cm²; Stp = 54 + 2 × 5 × 4 = 94 cm².\n"
            "### Bài 51. Diện tích xung quanh và diện tích toàn phần của hình lập phương\n- a = 4 cm: Sxq = 4 × 4 × 4 = 64 cm²; Stp = 4 × 4 × 6 = 96 cm².\n"
            "### Bài 52. Thể tích của hình hộp chữ nhật\n- V = 5 × 4 × 3 = 60 cm³.\n"
            "### Bài 53. Thể tích của hình lập phương\n- V = 4 × 4 × 4 = 64 cm³.\n"
            "### Bài 54. Thực hành tính toán và ước lượng thể tích một số hình khối\n### Bài 55. Luyện tập chung"
        ),
        "formulas": [
            G("I. Hình hộp chữ nhật (a, b, c)", F("Diện tích xung quanh", "Sxq = (a + b) × 2 × c"),
              F("Diện tích toàn phần", "Stp = Sxq + 2 × a × b"), F("Thể tích", "V = a × b × c")),
            G("II. Hình lập phương (cạnh a)", F("Diện tích xung quanh", "Sxq = a × a × 4"), F("Diện tích toàn phần", "Stp = a × a × 6"), F("Thể tích", "V = a × a × a")),
        ],
        "example": "Một bể nước hình hộp chữ nhật dài 2 m, rộng 1,5 m, cao 1 m. Bể chứa được bao nhiêu lít nước?",
        "example_answer": "V = 2 × 1,5 × 1 = 3 m³ = 3000 dm³ = **3000 l**.",
        "real_life": "- Tính lượng giấy gói hộp quà (diện tích toàn phần); sơn tường phòng (diện tích xung quanh); thể tích bể cá, thùng hàng.",
        "quiz": [
            mcq("biet", "Thể tích hình hộp chữ nhật có ba kích thước a, b, c là:", ["(a + b) × 2 × c", "a × b × c", "a × b", "a + b + c"], 1, "V = **a × b × c**."),
            mcq("biet", "Diện tích toàn phần hình lập phương cạnh a là:", ["a × a × 4", "a × a × 6", "a × a × a", "a × 6"], 1, "6 mặt vuông bằng nhau: Stp = **a × a × 6**."),
            mcq("biet", "Hình lập phương có bao nhiêu mặt?", ["4", "6", "8", "12"], 1, "Hình lập phương có **6** mặt."),
            mcq("biet", "Thể tích hình lập phương cạnh 3 cm là:", ["9 cm³", "27 cm³", "18 cm³", "54 cm³"], 1, "3 × 3 × 3 = **27 cm³**."),
            mcq("hieu", "Hình hộp chữ nhật dài 6 dm, rộng 4 dm, cao 5 dm có diện tích xung quanh là:", ["100 dm²", "120 dm²", "148 dm²", "24 dm²"], 0, "(6 + 4) × 2 × 5 = **100 dm²**."),
            mcq("hieu", "Hình lập phương có diện tích xung quanh 36 cm². Diện tích toàn phần là:", ["54 cm²", "72 cm²", "216 cm²", "48 cm²"], 0, "Một mặt: 36 : 4 = 9 cm²; Stp = 9 × 6 = **54 cm²**."),
            tf("hieu", "Nhận định: “Hình hộp chữ nhật dài 5 cm, rộng 3 cm, cao 2 cm có thể tích 30 cm³.”", True, "5 × 3 × 2 = 30 → **Đúng**."),
            tf("hieu", "Nhận định: “Gấp cạnh hình lập phương lên 2 lần thì thể tích gấp lên 2 lần.”", False, "Thể tích gấp 2 × 2 × 2 = 8 lần → **Sai**."),
            mcq("vandung", "Một thùng không nắp hình hộp chữ nhật dài 8 dm, rộng 5 dm, cao 4 dm. Diện tích tôn cần để làm thùng (không tính mép hàn) là:", ["144 dm²", "184 dm²", "104 dm²", "160 dm²"], 0,
                "Sxq = (8 + 5) × 2 × 4 = 104 dm²; thêm 1 đáy: 8 × 5 = 40 dm² → **144 dm²**.", note="Thùng không nắp chỉ có 1 đáy."),
            short("vandung", "Một bể cá hình hộp chữ nhật dài 80 cm, rộng 50 cm, cao 45 cm. Mực nước cao 30 cm. Trong bể có bao nhiêu lít nước?", ["120"],
                  "Thể tích nước: 80 × 50 × 30 = 120 000 cm³ = 120 dm³ = 120 l.\nĐáp số: **120 l**.", unit="l", note="Dùng chiều cao mực nước, không dùng chiều cao bể."),
        ],
    },
    # ===================== CHỦ ĐỀ 10 =====================
    {
        "topic": "l5-cd10-thoi-gian-van-toc-chuyen-dong-deu",
        "title": "Số đo thời gian, vận tốc. Các bài toán liên quan đến chuyển động đều",
        "icon": "🚗",
        "description": "Chủ đề 10 · SGK Toán 5 tập hai (tr. 64–86): Bài 56 – Bài 62. Các đơn vị đo thời gian; cộng, trừ số đo thời gian; nhân, chia số đo thời gian với một số; vận tốc; quãng đường, thời gian của chuyển động đều; thực hành ước lượng.",
        "requirements": [
            "Nhận biết được quan hệ giữa các đơn vị đo thời gian; thực hiện được cộng, trừ, nhân, chia số đo thời gian.",
            "Nhận biết được vận tốc của chuyển động đều; đơn vị km/giờ, m/phút, m/giây.",
            "Tính được vận tốc, quãng đường, thời gian trong chuyển động đều.",
            "Giải quyết được vấn đề thực tế liên quan đến chuyển động đều.",
        ],
        "definition": (
            "- **Thời gian**: 1 thế kỉ = 100 năm; 1 năm = 12 tháng; 1 năm thường 365 ngày, năm nhuận 366 ngày; 1 ngày = 24 giờ; 1 giờ = 60 phút; 1 phút = 60 giây.\n"
            "- Cộng/trừ số đo thời gian: đặt thẳng cột theo từng đơn vị; nếu số phút ≥ 60 thì đổi sang giờ; trừ không đủ thì mượn 1 giờ = 60 phút.\n"
            "- **Vận tốc** v = quãng đường s : thời gian t. **Quãng đường** s = v × t. **Thời gian** t = s : v (cùng hệ đơn vị)."
        ),
        "theory": (
            "### Bài 56. Các đơn vị đo thời gian\n- 1,5 giờ = 1 giờ 30 phút; 2 giờ 15 phút = 2,25 giờ.\n"
            "### Bài 57. Cộng, trừ số đo thời gian\n- 3 giờ 45 phút + 2 giờ 30 phút = 5 giờ 75 phút = 6 giờ 15 phút.\n"
            "### Bài 58. Nhân, chia số đo thời gian với một số\n- 2 giờ 20 phút × 3 = 6 giờ 60 phút = 7 giờ; 7 giờ 30 phút : 3 = 2 giờ 30 phút.\n"
            "### Bài 59. Vận tốc của một chuyển động đều\n- Ô tô đi 150 km trong 3 giờ: v = 50 km/giờ.\n"
            "### Bài 60. Quãng đường, thời gian của một chuyển động đều\n"
            "### Bài 61. Thực hành tính toán và ước lượng về vận tốc, quãng đường, thời gian trong chuyển động đều\n### Bài 62. Luyện tập chung"
        ),
        "formulas": [
            G("I. Chuyển động đều", F("Vận tốc", "v = s : t"), F("Quãng đường", "s = v × t"), F("Thời gian", "t = s : v"),
              F("Đổi đơn vị vận tốc", "1 km/giờ = 1000 m / 60 phút", "36 km/giờ = 600 m/phút = 10 m/giây.")),
            G("II. Thời gian", F("Quan hệ", "1 giờ = 60 phút · 1 phút = 60 giây · 1 ngày = 24 giờ"),
              F("Đổi phút sang giờ", "m phút = m/60 giờ", "45 phút = 0,75 giờ.")),
        ],
        "example": "Một xe máy khởi hành lúc 7 giờ 15 phút, đi với vận tốc 40 km/giờ trên quãng đường 90 km. Hỏi xe đến nơi lúc mấy giờ?",
        "example_answer": "t = 90 : 40 = 2,25 giờ = 2 giờ 15 phút. Đến nơi: 7 giờ 15 phút + 2 giờ 15 phút = **9 giờ 30 phút**.",
        "real_life": "- Lập kế hoạch đi lại, ước tính giờ đến; đọc biển báo tốc độ; thành tích chạy (m/giây).",
        "quiz": [
            mcq("biet", "Công thức tính vận tốc là:", ["v = s × t", "v = s : t", "v = t : s", "v = s + t"], 1, "**v = s : t**."),
            mcq("biet", "1 giờ 30 phút = … giờ?", ["1,3", "1,5", "1,30", "130"], 1, "30 phút = 0,5 giờ → **1,5 giờ**.", note="Không viết 1,3 giờ."),
            mcq("biet", "Năm nhuận có bao nhiêu ngày?", ["365", "366", "360", "364"], 1, "Năm nhuận có **366** ngày."),
            mcq("biet", "Công thức tính thời gian là:", ["t = s × v", "t = v : s", "t = s : v", "t = s − v"], 2, "**t = s : v**."),
            mcq("hieu", "Một người đi bộ với vận tốc 5 km/giờ trong 2,5 giờ. Quãng đường đi được là:", ["12,5 km", "2 km", "7,5 km", "10 km"], 0, "s = 5 × 2,5 = **12,5 km**."),
            mcq("hieu", "4 giờ 20 phút − 1 giờ 45 phút = ?", ["2 giờ 35 phút", "3 giờ 25 phút", "2 giờ 75 phút", "3 giờ 35 phút"], 0, "Mượn 1 giờ: 3 giờ 80 phút − 1 giờ 45 phút = **2 giờ 35 phút**."),
            tf("hieu", "Nhận định: “54 km/giờ = 15 m/giây.”", True, "54 000 m : 3600 giây = 15 m/giây → **Đúng**."),
            tf("hieu", "Nhận định: “Ô tô đi 120 km trong 1 giờ 30 phút thì vận tốc là 92,3 km/giờ.”", False, "1 giờ 30 phút = 1,5 giờ; v = 120 : 1,5 = 80 km/giờ (lỗi do dùng 1,3 giờ) → **Sai**."),
            mcq("vandung", "Một ca nô đi với vận tốc 24 km/giờ, đi quãng đường 30 km. Thời gian đi là:", ["1 giờ 15 phút", "1 giờ 25 phút", "1,15 giờ", "54 phút"], 0,
                "t = 30 : 24 = 1,25 giờ = **1 giờ 15 phút**."),
            short("vandung", "Hai xe khởi hành cùng lúc từ hai đầu quãng đường dài 180 km, đi ngược chiều nhau với vận tốc 40 km/giờ và 50 km/giờ. Sau bao nhiêu giờ hai xe gặp nhau?", ["2"],
                  "Mỗi giờ hai xe gần nhau thêm 40 + 50 = 90 (km). Thời gian gặp nhau: 180 : 90 = 2 (giờ).\nĐáp số: **2 giờ**.", unit="giờ"),
        ],
    },
    # ===================== CHỦ ĐỀ 11 =====================
    {
        "topic": "l5-cd11-thong-ke-xac-suat",
        "title": "Một số yếu tố thống kê và xác suất",
        "icon": "📊",
        "description": "Chủ đề 11 · SGK Toán 5 tập hai (tr. 87–102): Bài 63 – Bài 67. Thu thập, phân loại, sắp xếp số liệu; biểu đồ hình quạt tròn; tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện; thực hành trải nghiệm.",
        "requirements": [
            "Thu thập, phân loại, sắp xếp được số liệu thống kê theo tiêu chí cho trước.",
            "Đọc, mô tả được số liệu ở dạng biểu đồ hình quạt tròn (có ghi tỉ số phần trăm); nêu nhận xét, giải quyết vấn đề đơn giản.",
            "Sử dụng được tỉ số để mô tả số lần lặp lại của một khả năng xảy ra (nhiều lần) của một sự kiện so với tổng số lần thực hiện.",
        ],
        "definition": (
            "- **Biểu đồ hình quạt tròn**: cả hình tròn biểu diễn **100%**; mỗi hình quạt biểu diễn tỉ số phần trăm của một thành phần.\n"
            "- Đọc biểu đồ: số lượng của thành phần = Tổng × phần trăm : 100.\n"
            "- **Tỉ số lặp lại**: nếu thực hiện n lần, sự kiện A xảy ra k lần thì tỉ số là k/n (có thể viết dạng phần trăm)."
        ),
        "theory": (
            "### Bài 63. Thu thập, phân loại, sắp xếp các số liệu\n"
            "### Bài 64. Biểu đồ hình quạt tròn\n- Lớp 40 bạn, 25% thích bóng đá → 40 × 25 : 100 = 10 bạn.\n"
            "### Bài 65. Tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện\n- Tung đồng xu 50 lần, ngửa 23 lần: tỉ số 23/50 = 46%.\n"
            "### Bài 66. Thực hành và trải nghiệm thu thập, phân tích, biểu diễn các số liệu thống kê\n### Bài 67. Luyện tập chung"
        ),
        "formulas": [
            G("I. Biểu đồ hình quạt", F("Tổng các phần", "= 100%"), F("Giá trị một phần", "Tổng × m : 100")),
            G("II. Tỉ số lặp lại", F("Tỉ số", "k/n = số lần A xảy ra / tổng số lần thực hiện")),
        ],
        "example": "Biểu đồ hình quạt: trong 200 học sinh, 45% thích đọc truyện, 30% thích thể thao, còn lại thích âm nhạc. Có bao nhiêu học sinh thích âm nhạc?",
        "example_answer": "Phần trăm âm nhạc: 100% − 45% − 30% = 25%. Số học sinh: 200 × 25 : 100 = **50** học sinh.",
        "real_life": "- Biểu đồ cơ cấu chi tiêu gia đình; tỉ lệ sút phạt thành công của cầu thủ.",
        "quiz": [
            mcq("biet", "Cả hình tròn trong biểu đồ hình quạt tròn biểu diễn:", ["50%", "100%", "360%", "10%"], 1, "Toàn bộ hình tròn là **100%**."),
            mcq("biet", "Tung đồng xu 20 lần, mặt ngửa xuất hiện 9 lần. Tỉ số số lần xuất hiện mặt ngửa và tổng số lần tung là:", ["9/20", "11/20", "20/9", "9/11"], 0, "k/n = **9/20**."),
            mcq("biet", "Biểu đồ: Táo 40%, Cam 35%, còn lại Xoài. Xoài chiếm:", ["25%", "75%", "35%", "15%"], 0, "100% − 40% − 35% = **25%**."),
            mcq("biet", "Theo biểu đồ trên, loại quả được chọn nhiều nhất là:", ["Táo", "Cam", "Xoài", "Bằng nhau"], 0, "40% lớn nhất → **Táo**."),
            mcq("hieu", "Một lớp có 40 học sinh, biểu đồ cho biết 30% học sinh đi học bằng xe đạp. Số học sinh đi xe đạp là:", ["12", "30", "13", "10"], 0, "40 × 30 : 100 = **12**."),
            mcq("hieu", "Gieo xúc xắc 50 lần, mặt 6 chấm xuất hiện 8 lần. Tỉ số phần trăm là:", ["8%", "16%", "6%", "42%"], 1, "8 : 50 = 0,16 = **16%**."),
            tf("hieu", "Nhận định: “Trong biểu đồ hình quạt, hình quạt chiếm nửa hình tròn biểu diễn 50%.”", True, "Nửa hình tròn = 1/2 × 100% = 50% → **Đúng**."),
            tf("hieu", "Nhận định: “Ném bóng vào rổ 25 lần, trúng 15 lần thì tỉ số trúng là 15/40.”", False, "Tỉ số so với tổng số lần ném: 15/25 = 3/5 = 60% → **Sai**."),
            mcq("vandung", "Gia đình chi tiêu 15 000 000 đồng/tháng: ăn uống 40%, học tập 20%, tiết kiệm 15%, còn lại chi khác. Số tiền chi khác là:", ["3 750 000 đồng", "6 000 000 đồng", "2 250 000 đồng", "3 000 000 đồng"], 0,
                "Chi khác: 100% − 40% − 20% − 15% = 25%. 15 000 000 × 25 : 100 = **3 750 000 đồng**."),
            short("vandung", "Một cầu thủ sút phạt 40 lần, thành công 34 lần. Tỉ số phần trăm số lần thành công là bao nhiêu phần trăm?", ["85", "85%"],
                  "34 : 40 = 0,85 = **85%**.", unit="%"),
        ],
    },
    # ===================== CHỦ ĐỀ 12 =====================
    {
        "topic": "l5-cd12-on-tap-cuoi-nam",
        "title": "Ôn tập cuối năm",
        "icon": "🏁",
        "description": "Chủ đề 12 · SGK Toán 5 tập hai (tr. 103–134): Bài 68 – Bài 75. Ôn tập số tự nhiên, phân số, số thập phân và các phép tính; tỉ số, tỉ số phần trăm; hình học; đo lường; toán chuyển động đều; thống kê và xác suất.",
        "requirements": [
            "Củng cố số tự nhiên, phân số, số thập phân và bốn phép tính; tính giá trị biểu thức.",
            "Giải được các bài toán về tỉ số, tỉ số phần trăm, tổng – tỉ, hiệu – tỉ, chuyển động đều.",
            "Tính được chu vi, diện tích các hình phẳng; diện tích xung quanh, toàn phần, thể tích hình hộp chữ nhật, hình lập phương.",
            "Chuyển đổi các đơn vị đo; đọc biểu đồ hình quạt tròn; tính tỉ số lặp lại của sự kiện.",
        ],
        "definition": (
            "- Phân số ↔ số thập phân ↔ tỉ số phần trăm: 3/4 = 0,75 = 75%.\n"
            "- Hình phẳng: tam giác, hình thang, hình tròn; hình khối: hình hộp chữ nhật, hình lập phương.\n"
            "- Chuyển động đều: s = v × t."
        ),
        "theory": (
            "### Bài 68. Ôn tập số tự nhiên, phân số, số thập phân\n### Bài 69. Ôn tập các phép tính với số tự nhiên, phân số, số thập phân\n"
            "### Bài 70. Ôn tập tỉ số, tỉ số phần trăm\n### Bài 71. Ôn tập hình học\n### Bài 72. Ôn tập đo lường\n"
            "### Bài 73. Ôn tập toán chuyển động đều\n### Bài 74. Ôn tập một số yếu tố thống kê và xác suất\n### Bài 75. Ôn tập chung"
        ),
        "formulas": [
            G("I. Số và tỉ số", F("Phần trăm", "a : b × 100% · m% của A = A × m : 100")),
            G("II. Hình học", F("Tam giác / hình thang", "S = a × h : 2 · S = (a + b) × h : 2"), F("Hình tròn", "C = d × 3,14 · S = r × r × 3,14"),
              F("Hình hộp / lập phương", "V = a × b × c · V = a × a × a")),
            G("III. Chuyển động", F("Quan hệ", "s = v × t · v = s : t · t = s : v")),
        ],
        "example": "Một người gửi tiết kiệm 20 000 000 đồng với lãi suất 0,5% một tháng. Sau một tháng, người đó có cả tiền gửi và tiền lãi là bao nhiêu?",
        "example_answer": "Tiền lãi: 20 000 000 × 0,5 : 100 = 100 000 (đồng). Tổng: **20 100 000 đồng**.",
        "real_life": "- Lập kế hoạch chuyến đi (quãng đường, thời gian, chi phí); tính lượng sơn, lượng nước; đọc số liệu thống kê trên báo.",
        "quiz": [
            mcq("biet", "3/5 viết dưới dạng số thập phân là:", ["0,35", "0,6", "3,5", "0,06"], 1, "3/5 = 6/10 = **0,6**."),
            mcq("biet", "Diện tích hình thang đáy 7 cm và 5 cm, cao 4 cm là:", ["24 cm²", "48 cm²", "140 cm²", "16 cm²"], 0, "(7 + 5) × 4 : 2 = **24 cm²**."),
            mcq("biet", "2,5 giờ = … phút?", ["250", "150", "25", "130"], 1, "2,5 × 60 = **150 phút**."),
            mcq("biet", "1 m³ = … l?", ["100", "1000", "10", "10 000"], 1, "1 m³ = 1000 dm³ = **1000 l**."),
            mcq("hieu", "Tìm x: x × 2,5 = 7,5 + 2,5", ["4", "3", "25", "0,4"], 0, "x × 2,5 = 10 ⇒ x = 10 : 2,5 = **4**."),
            mcq("hieu", "Tỉ số phần trăm của 7 và 28 là:", ["25%", "4%", "400%", "21%"], 0, "7 : 28 = 0,25 = **25%**."),
            tf("hieu", "Nhận định: “Hình lập phương cạnh 0,5 m có thể tích 0,125 m³.”", True, "0,5 × 0,5 × 0,5 = 0,125 → **Đúng**."),
            tf("hieu", "Nhận định: “Ô tô đi với vận tốc 60 km/giờ trong 45 phút được 27 km.”", False, "45 phút = 0,75 giờ; s = 60 × 0,75 = 45 km → **Sai**."),
            mcq("vandung", "Tổng số học sinh hai lớp là 72, số học sinh lớp 5A bằng 4/5 số học sinh lớp 5B. Lớp 5B có:", ["40 học sinh", "32 học sinh", "36 học sinh", "45 học sinh"], 0,
                "Tổng 4 + 5 = 9 phần; 1 phần = 72 : 9 = 8. Lớp 5B: 8 × 5 = **40** học sinh."),
            short("vandung", "Một bể nước hình hộp chữ nhật dài 2 m, rộng 1,2 m, cao 1 m. Hiện bể chứa 75% thể tích. Trong bể có bao nhiêu lít nước?", ["1800"],
                  "Thể tích bể: 2 × 1,2 × 1 = 2,4 m³. Nước: 2,4 × 75 : 100 = 1,8 m³ = 1800 l.\nĐáp số: **1800 l**.", unit="l"),
        ],
    },
]
