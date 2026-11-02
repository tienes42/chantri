"""TOÁN 1 — Kết nối tri thức với cuộc sống (tập một, tập hai).

10 chủ đề đánh số trong SGK, đúng thứ tự mục lục.
Mỗi chủ đề có: Yêu cầu cần đạt (CT GDPT 2018), kiến thức theo từng bài,
công thức/quy tắc cần nhớ, ví dụ, ứng dụng và 10 câu hỏi 3 mức độ:
  Biết: 4 trắc nghiệm | Hiểu: 2 trắc nghiệm + 2 Đúng/Sai | Vận dụng: 1 trắc nghiệm + 1 trả lời ngắn
"""

GRADE = 1


def mcq(level, q, options, answer, solution, alt=None, note=None):
    return {"level": level, "type": "mcq", "q": q, "options": options, "answer": answer,
            "solution": solution, "alt": alt, "note": note}


def tf(level, q, answer, solution, alt=None, note=None):
    return {"level": level, "type": "tf", "q": q, "answer": answer,
            "solution": solution, "alt": alt, "note": note}


def short(level, q, answer, solution, unit=None, alt=None, note=None):
    return {"level": level, "type": "short", "q": q, "answer": answer, "unit": unit,
            "solution": solution, "alt": alt, "note": note}


LESSONS = [
    # =====================================================================
    # CHỦ ĐỀ 1. CÁC SỐ TỪ 0 ĐẾN 10
    # =====================================================================
    {
        "topic": "l1-cd01-cac-so-tu-0-den-10",
        "title": "Các số từ 0 đến 10",
        "icon": "🔢",
        "description": "Chủ đề 1 · SGK Toán 1 tập một (tr. 6–45): Tiết học đầu tiên, Bài 1 – Bài 6. Đếm, đọc, viết, so sánh và tách – gộp các số từ 0 đến 10.",
        "requirements": [
            "Đếm, đọc, viết được các số trong phạm vi 10.",
            "Nhận biết được số 0 (dùng để chỉ “không có” đồ vật nào).",
            "Nhận biết được “nhiều hơn”, “ít hơn”, “bằng nhau” khi so sánh hai nhóm đồ vật.",
            "Nhận biết được cách so sánh, xếp thứ tự các số trong phạm vi 10 (ở các nhóm có không quá 4 số); sử dụng đúng các dấu >, <, =.",
            "Nhận biết được cấu tạo số (“mấy và mấy”): tách một số thành hai số và gộp hai số thành một số trong phạm vi 10.",
            "Vận dụng đếm, so sánh số để giải quyết tình huống đơn giản trong cuộc sống.",
        ],
        "definition": (
            "**Số** dùng để chỉ số lượng đồ vật. Mỗi nhóm đồ vật có bao nhiêu cái thì ta dùng số đó để ghi lại.\n"
            "- **Số 0** chỉ “không có” đồ vật nào (ví dụ: đĩa không có quả cam nào → 0 quả cam).\n"
            "- **Dãy số từ 0 đến 10:** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Số đứng sau hơn số đứng ngay trước nó 1 đơn vị.\n"
            "- **Dấu so sánh:** > (lớn hơn), < (bé hơn), = (bằng).\n"
            "- **Mấy và mấy:** một số có thể tách thành hai số; hai số đó gộp lại được số ban đầu (8 gồm 5 và 3)."
        ),
        "theory": (
            "### Tiết học đầu tiên\n"
            "- Làm quen với sách Toán 1, bộ đồ dùng học Toán (que tính, chấm tròn, các hình, thẻ số) và các hoạt động: Khám phá, Hoạt động, Trò chơi, Luyện tập.\n"
            "### Bài 1. Các số 0, 1, 2, 3, 4, 5\n"
            "- Đếm số lượng đồ vật (mỗi đồ vật đếm một lần, không bỏ sót), đọc và viết các số 0, 1, 2, 3, 4, 5.\n"
            "- Số 0 dùng khi không có đồ vật nào.\n"
            "### Bài 2. Các số 6, 7, 8, 9, 10\n"
            "- Đếm, đọc, viết các số 6, 7, 8, 9, 10; số 10 được viết bằng hai chữ số: 1 và 0.\n"
            "- Đếm xuôi 0 → 10 và đếm ngược 10 → 0.\n"
            "### Bài 3. Nhiều hơn, ít hơn, bằng nhau\n"
            "- So sánh hai nhóm đồ vật bằng cách **ghép đôi (nối 1 – 1)**: nhóm nào còn thừa thì nhiều hơn; nhóm kia ít hơn; vừa đủ thì bằng nhau.\n"
            "### Bài 4. So sánh số\n"
            "- Dùng dấu >, <, = để so sánh hai số: 5 > 3; 3 < 5; 4 = 4.\n"
            "- Trong dãy số từ 0 đến 10, số đứng trước bé hơn số đứng sau. Xếp thứ tự các số từ bé đến lớn hoặc từ lớn đến bé; tìm số lớn nhất, bé nhất.\n"
            "### Bài 5. Mấy và mấy\n"
            "- Tách một nhóm đồ vật thành hai phần: 5 gồm 2 và 3; 5 gồm 4 và 1…\n"
            "- Gộp hai phần lại được cả nhóm.\n"
            "### Bài 6. Luyện tập chung\n"
            "- Ôn đếm, đọc, viết, so sánh, sắp xếp và tách – gộp các số trong phạm vi 10."
        ),
        "formulas": [
            {"category": "I. Dãy số từ 0 đến 10", "items": [
                {"name": "Đếm xuôi", "formula": "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", "note": "Số liền sau = số đó thêm 1 (sau 6 là 7)."},
                {"name": "Đếm ngược", "formula": "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0", "note": "Số liền trước = số đó bớt 1 (trước 6 là 5)."},
                {"name": "Số 0", "formula": "Không có đồ vật nào → 0", "note": "0 là số bé nhất trong các số đã học."},
            ]},
            {"category": "II. So sánh số", "items": [
                {"name": "Lớn hơn", "formula": "7 > 4  (đọc: bảy lớn hơn bốn)"},
                {"name": "Bé hơn", "formula": "4 < 7  (đọc: bốn bé hơn bảy)"},
                {"name": "Bằng nhau", "formula": "6 = 6  (đọc: sáu bằng sáu)"},
                {"name": "Mẹo nhớ dấu", "formula": "Đầu nhọn của dấu > hoặc < luôn chỉ về số bé hơn", "note": "Trong dãy 0 → 10: số đứng sau lớn hơn số đứng trước."},
            ]},
            {"category": "III. Mấy và mấy (cấu tạo số)", "items": [
                {"name": "Số 5", "formula": "5 gồm 1 và 4 · 2 và 3"},
                {"name": "Số 6", "formula": "6 gồm 1 và 5 · 2 và 4 · 3 và 3"},
                {"name": "Số 7", "formula": "7 gồm 1 và 6 · 2 và 5 · 3 và 4"},
                {"name": "Số 8", "formula": "8 gồm 1 và 7 · 2 và 6 · 3 và 5 · 4 và 4"},
                {"name": "Số 9", "formula": "9 gồm 1 và 8 · 2 và 7 · 3 và 6 · 4 và 5"},
                {"name": "Số 10", "formula": "10 gồm 1 và 9 · 2 và 8 · 3 và 7 · 4 và 6 · 5 và 5"},
            ]},
        ],
        "example": (
            "a) Điền dấu >, <, = vào chỗ chấm: 7 … 9.\n"
            "b) Xếp các số 6, 2, 9, 4 theo thứ tự từ bé đến lớn.\n"
            "c) Số 9 gồm 4 và mấy?"
        ),
        "example_answer": (
            "a) Trong dãy số, 7 đứng trước 9 nên 7 bé hơn 9: **7 < 9**.\n"
            "b) Số bé nhất là 2, rồi đến 4, 6, lớn nhất là 9: **2, 4, 6, 9**.\n"
            "c) Từ 4 đếm thêm: 5, 6, 7, 8, 9 (đếm thêm 5 lần) → **9 gồm 4 và 5**."
        ),
        "real_life": (
            "- Đếm số bạn trong tổ, số bút trong hộp, số bậc cầu thang.\n"
            "- So sánh xem ai có nhiều viên bi hơn, nhóm nào có ít quả hơn.\n"
            "- Chia kẹo, chia bánh thành hai phần (mấy và mấy) cho hai bạn."
        ),
        "quiz": [
            mcq("biet", "Đếm số quả táo: 🍎🍎🍎🍎🍎🍎🍎\nCó bao nhiêu quả táo?",
                ["6", "7", "8", "5"], 1,
                "Chỉ tay vào từng quả và đếm: 1, 2, 3, 4, 5, 6, 7. Quả cuối cùng ứng với số 7.\nVậy có **7 quả táo**.",
                note="Mỗi quả chỉ đếm một lần, không bỏ sót và không đếm lặp lại."),
            mcq("biet", "Số “chín” được viết là:",
                ["6", "9", "7", "10"], 1,
                "Số chín viết là **9**.",
                note="Dễ nhầm 6 với 9: số 6 có vòng tròn ở dưới, số 9 có vòng tròn ở trên."),
            mcq("biet", "Trong dãy số 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, số đứng liền sau số 6 là:",
                ["5", "8", "7", "6"], 2,
                "Số liền sau là số đếm tiếp theo (thêm 1): đếm 6 rồi đến **7**.",
                note="Số liền **trước** 6 là 5, số liền **sau** 6 là 7 — đừng nhầm hai từ này."),
            mcq("biet", "Chiếc đĩa không có quả cam nào. Số chỉ số quả cam trên đĩa là:",
                ["1", "0", "10", "Không viết được số"], 1,
                "Không có quả nào thì ta dùng **số 0**."),
            mcq("hieu", "Dấu thích hợp điền vào chỗ chấm: 8 … 5",
                ["<", ">", "=", "+"], 1,
                "Trong dãy số, 8 đứng sau 5 nên 8 lớn hơn 5. Ta viết **8 > 5**.",
                alt="Lấy 8 chấm tròn và 5 chấm tròn rồi nối mỗi chấm của nhóm 5 với một chấm của nhóm 8: nhóm 8 còn thừa 3 chấm, nên 8 nhiều hơn 5.",
                note="Đầu nhọn của dấu luôn chỉ về số bé hơn (ở đây là số 5)."),
            mcq("hieu", "Số 8 gồm 3 và mấy?",
                ["4", "6", "5", "3"], 2,
                "Từ 3 đếm thêm đến 8: 4, 5, 6, 7, 8 — đếm thêm 5 lần.\nVậy **8 gồm 3 và 5**.",
                alt="Lấy 8 que tính, tách ra 3 que; đếm số que còn lại được 5 que."),
            tf("hieu", "Có 4 con thỏ 🐰🐰🐰🐰 và 3 củ cà rốt 🥕🥕🥕.\nNhận định: “Số thỏ ít hơn số cà rốt.”", False,
               "Nối mỗi con thỏ với một củ cà rốt: còn thừa 1 con thỏ chưa có cà rốt.\nVậy số thỏ **nhiều hơn** số cà rốt (4 > 3). Nhận định đã cho là **Sai**."),
            tf("hieu", "Nhận định: “Các số 7, 2, 10, 5 xếp theo thứ tự từ bé đến lớn là 2, 5, 7, 10.”", True,
               "Tìm số bé nhất: 2; tiếp theo: 5; rồi 7; lớn nhất: 10.\nThứ tự từ bé đến lớn là 2, 5, 7, 10 → nhận định **Đúng**."),
            mcq("vandung", "Mai có 6 bông hoa, Lan có 9 bông hoa, Hà có 4 bông hoa. Bạn nào có nhiều bông hoa nhất?",
                ["Mai", "Lan", "Hà", "Ba bạn bằng nhau"], 1,
                "So sánh ba số 6, 9, 4: số lớn nhất là 9.\nVậy **Lan** có nhiều bông hoa nhất.",
                alt="Xếp các số từ bé đến lớn: 4, 6, 9 → số đứng cuối (9) là lớn nhất."),
            short("vandung", "Em hãy tìm số lớn hơn 7 nhưng bé hơn 9.", ["8"],
                  "Các số lớn hơn 7 là 8, 9, 10. Trong đó chỉ có **8** bé hơn 9.\nVậy số cần tìm là **8**.",
                  alt="Trên dãy số: 7, **8**, 9 — số nằm giữa 7 và 9 là 8."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 2. LÀM QUEN VỚI MỘT SỐ HÌNH PHẲNG
    # =====================================================================
    {
        "topic": "l1-cd02-hinh-phang",
        "title": "Làm quen với một số hình phẳng",
        "icon": "🔷",
        "description": "Chủ đề 2 · SGK Toán 1 tập một (tr. 46–55): Bài 7 – Bài 9. Nhận dạng hình vuông, hình tròn, hình tam giác, hình chữ nhật; lắp ghép, xếp hình.",
        "requirements": [
            "Nhận dạng được hình vuông, hình tròn, hình tam giác, hình chữ nhật thông qua việc sử dụng bộ đồ dùng học tập cá nhân hoặc vật thật.",
            "Nhận biết và thực hiện được việc lắp ghép, xếp hình gắn với sử dụng bộ đồ dùng học tập cá nhân hoặc vật thật.",
            "Đếm được số hình mỗi loại có trong một hình ghép hoặc một bức tranh.",
        ],
        "definition": (
            "- **Hình vuông:** có 4 cạnh, các cạnh dài bằng nhau.\n"
            "- **Hình chữ nhật:** có 4 cạnh, gồm 2 cạnh dài bằng nhau và 2 cạnh ngắn bằng nhau.\n"
            "- **Hình tam giác:** có 3 cạnh.\n"
            "- **Hình tròn:** là một đường cong khép kín, không có cạnh thẳng.\n"
            "Một hình dù đặt xoay, đặt nghiêng hay có màu sắc, kích thước khác nhau thì vẫn là hình đó."
        ),
        "theory": (
            "### Bài 7. Hình vuông, hình tròn, hình tam giác, hình chữ nhật\n"
            "- Quan sát đồ vật thật để nhận ra hình: mặt khăn tay (hình vuông), mặt đồng hồ (hình tròn), biển báo (hình tam giác), mặt bảng lớp (hình chữ nhật).\n"
            "- Phân biệt các hình theo số cạnh và hình dạng các cạnh.\n"
            "### Bài 8. Thực hành lắp ghép, xếp hình\n"
            "- Dùng que tính xếp hình: hình tam giác cần 3 que, hình vuông cần 4 que.\n"
            "- Ghép các hình đã học thành hình mới: 2 hình tam giác có thể ghép thành hình vuông hoặc hình chữ nhật; ghép hình ngôi nhà, con cá, cái thuyền…\n"
            "### Bài 9. Luyện tập chung\n"
            "- Nhận dạng, đếm số hình mỗi loại trong tranh; tìm quy luật dãy hình; lắp ghép hình theo mẫu."
        ),
        "formulas": [
            {"category": "I. Đặc điểm nhận dạng hình phẳng", "items": [
                {"name": "Hình vuông", "formula": "4 cạnh · các cạnh dài bằng nhau", "note": "Ví dụ: mặt viên gạch hoa, khăn tay, ô cửa sổ vuông."},
                {"name": "Hình chữ nhật", "formula": "4 cạnh · 2 cạnh dài bằng nhau, 2 cạnh ngắn bằng nhau", "note": "Ví dụ: mặt bảng lớp, quyển vở, cánh cửa."},
                {"name": "Hình tam giác", "formula": "3 cạnh", "note": "Ví dụ: biển báo nguy hiểm, miếng bánh cắt chéo, mái nhà."},
                {"name": "Hình tròn", "formula": "Đường cong khép kín · không có cạnh thẳng", "note": "Ví dụ: mặt đồng hồ, đĩa, bánh xe."},
            ]},
            {"category": "II. Xếp hình bằng que tính", "items": [
                {"name": "Hình tam giác", "formula": "Cần 3 que tính"},
                {"name": "Hình vuông", "formula": "Cần 4 que tính (dài bằng nhau)"},
                {"name": "Ghép hình", "formula": "2 hình tam giác → 1 hình vuông (hoặc 1 hình chữ nhật)", "note": "2 hình vuông bằng nhau đặt cạnh nhau → 1 hình chữ nhật."},
            ]},
        ],
        "example": "Một bức tranh ngôi nhà gồm: mái nhà là 1 hình tam giác, thân nhà là 1 hình vuông, 1 cửa ra vào hình chữ nhật và 1 ông mặt trời hình tròn. Bức tranh có mấy loại hình? Đó là những hình nào?",
        "example_answer": "Bức tranh có **4 loại hình**: hình tam giác (mái nhà), hình vuông (thân nhà), hình chữ nhật (cửa ra vào), hình tròn (mặt trời).",
        "real_life": (
            "- Nhận ra hình dạng đồ vật quanh em: bàn, bảng, cửa, đồng hồ, biển báo giao thông.\n"
            "- Xếp, ghép hình để làm đồ chơi, trang trí lớp học, vẽ tranh."
        ),
        "quiz": [
            mcq("biet", "Hình nào có 3 cạnh?",
                ["Hình vuông", "Hình tròn", "Hình tam giác", "Hình chữ nhật"], 2,
                "**Hình tam giác** có 3 cạnh. Hình vuông và hình chữ nhật có 4 cạnh; hình tròn không có cạnh thẳng."),
            mcq("biet", "Mặt chiếc đồng hồ treo tường (loại tròn) có dạng hình gì?",
                ["Hình tròn", "Hình vuông", "Hình tam giác", "Hình chữ nhật"], 0,
                "Mặt đồng hồ là một đường cong khép kín, không có cạnh thẳng → **hình tròn**."),
            mcq("biet", "Mặt bảng lớp em thường có dạng hình gì?",
                ["Hình tròn", "Hình tam giác", "Hình chữ nhật", "Hình vuông"], 2,
                "Mặt bảng có 4 cạnh: 2 cạnh dài bằng nhau và 2 cạnh ngắn bằng nhau → **hình chữ nhật**.",
                note="Hình vuông cũng có 4 cạnh nhưng các cạnh dài bằng nhau; mặt bảng dài hơn hẳn chiều cao nên không phải hình vuông."),
            mcq("biet", "Hình vuông có mấy cạnh?",
                ["3", "4", "5", "Không có cạnh"], 1,
                "Hình vuông có **4 cạnh** và các cạnh dài bằng nhau."),
            mcq("hieu", "Cắt một tờ giấy hình vuông theo đường thẳng nối hai góc đối diện, em được hai hình gì?",
                ["2 hình tròn", "2 hình tam giác", "2 hình chữ nhật", "2 hình vuông"], 1,
                "Mỗi phần sau khi cắt có 3 cạnh (2 cạnh của hình vuông và đường cắt) → mỗi phần là một **hình tam giác**.",
                alt="Làm ngược lại: ghép 2 hình tam giác bằng nhau theo cạnh dài nhất sẽ được lại hình vuông ban đầu."),
            mcq("hieu", "Dùng các que tính dài bằng nhau, cần ít nhất bao nhiêu que tính để xếp được 1 hình vuông?",
                ["3", "4", "5", "6"], 1,
                "Hình vuông có 4 cạnh dài bằng nhau, mỗi cạnh là 1 que tính → cần **4 que tính**.",
                note="3 que tính chỉ xếp được hình tam giác."),
            tf("hieu", "Nhận định: “Hình chữ nhật và hình vuông đều có 4 cạnh.”", True,
               "Hình chữ nhật có 4 cạnh, hình vuông cũng có 4 cạnh → nhận định **Đúng**.\nĐiểm khác: hình vuông có 4 cạnh dài bằng nhau."),
            tf("hieu", "Nhận định: “Nếu xoay nghiêng một hình tam giác thì nó không còn là hình tam giác nữa.”", False,
               "Xoay, đặt nghiêng hay đổi màu thì hình vẫn có 3 cạnh, nên vẫn là **hình tam giác**. Nhận định **Sai**."),
            mcq("vandung", "Bạn Nam xếp hình ngôi nhà gồm: mái nhà là 1 hình tam giác, thân nhà là 1 hình vuông, 2 cửa sổ là 2 hình vuông nhỏ và 1 cửa ra vào là hình chữ nhật. Hình ngôi nhà có tất cả bao nhiêu hình vuông?",
                ["1", "2", "3", "4"], 2,
                "Đếm các hình vuông: thân nhà (1), cửa sổ thứ nhất (2), cửa sổ thứ hai (3).\nVậy có **3 hình vuông**.",
                note="Cửa ra vào là hình chữ nhật, mái nhà là hình tam giác — không đếm vào."),
            short("vandung", "Bạn Hà dùng que tính xếp 2 hình tam giác rời nhau (hai hình không dùng chung que nào). Hỏi Hà cần tất cả bao nhiêu que tính?", ["6"],
                  "Mỗi hình tam giác có 3 cạnh nên cần 3 que tính.\nHình thứ nhất: đếm 1, 2, 3; hình thứ hai đếm tiếp: 4, 5, 6.\nVậy Hà cần **6 que tính**.",
                  unit="que tính"),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 3. PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10
    # =====================================================================
    {
        "topic": "l1-cd03-cong-tru-pham-vi-10",
        "title": "Phép cộng, phép trừ trong phạm vi 10",
        "icon": "➕",
        "description": "Chủ đề 3 · SGK Toán 1 tập một (tr. 56–91): Bài 10 – Bài 13. Ý nghĩa, cách tính và bảng cộng, bảng trừ trong phạm vi 10.",
        "requirements": [
            "Nhận biết được ý nghĩa của phép cộng (gộp lại, thêm vào) và phép trừ (bớt đi, tách ra).",
            "Thực hiện được phép cộng, phép trừ các số trong phạm vi 10.",
            "Thực hiện được việc cộng, trừ nhẩm trong phạm vi 10; thuộc bảng cộng, bảng trừ trong phạm vi 10.",
            "Nhận biết được ý nghĩa thực tiễn của phép tính (cộng, trừ) thông qua tranh ảnh, hình vẽ hoặc tình huống thực tiễn; viết được phép tính thích hợp.",
            "Làm quen với tính chất đổi chỗ của phép cộng, số 0 trong phép cộng, phép trừ và mối liên hệ giữa phép cộng với phép trừ.",
        ],
        "definition": (
            "- **Phép cộng** (dấu +) dùng khi **gộp lại** hai nhóm hoặc **thêm vào**: 3 + 2 = 5 (đọc: ba cộng hai bằng năm).\n"
            "- **Phép trừ** (dấu −) dùng khi **bớt đi** hoặc **tách ra** để tìm phần còn lại: 6 − 1 = 5 (đọc: sáu trừ một bằng năm).\n"
            "- **Số 0:** cộng hay trừ với 0 thì số đó không đổi; một số trừ chính nó bằng 0."
        ),
        "theory": (
            "### Bài 10. Phép cộng trong phạm vi 10\n"
            "- Gộp lại thì bằng mấy? (gộp 3 quả bóng và 2 quả bóng được 5 quả: 3 + 2 = 5).\n"
            "- Thêm vào thì bằng mấy? Tính bằng cách **đếm thêm**: 5 + 2 → đếm tiếp 6, 7 → 5 + 2 = 7.\n"
            "- Số 0 trong phép cộng: 4 + 0 = 4; 0 + 2 = 2.\n"
            "- Đổi chỗ các số trong phép cộng thì kết quả không thay đổi: 3 + 4 = 4 + 3.\n"
            "### Bài 11. Phép trừ trong phạm vi 10\n"
            "- Bớt đi còn lại mấy? (có 6 quả, bớt 1 quả còn 5 quả: 6 − 1 = 5).\n"
            "- Tách ra: 7 bông hoa gồm 5 bông đỏ và 2 bông vàng → 7 − 2 = 5. Tính bằng cách **đếm bớt** (đếm lùi).\n"
            "- Số 0 trong phép trừ: 3 − 0 = 3; 3 − 3 = 0.\n"
            "### Bài 12. Bảng cộng, bảng trừ trong phạm vi 10\n"
            "- Lập và ghi nhớ bảng cộng, bảng trừ; dùng bảng để tính nhẩm nhanh.\n"
            "- Từ một phép cộng viết được hai phép trừ: 3 + 5 = 8 → 8 − 3 = 5 và 8 − 5 = 3.\n"
            "### Bài 13. Luyện tập chung\n"
            "- Tính nhẩm, so sánh kết quả phép tính, viết phép tính thích hợp với tranh vẽ/tình huống."
        ),
        "formulas": [
            {"category": "I. Ý nghĩa phép tính", "items": [
                {"name": "Phép cộng", "formula": "Gộp lại / Thêm vào → dùng dấu +", "note": "3 + 2 = 5: 3 và 2 là hai số được cộng, 5 là kết quả."},
                {"name": "Phép trừ", "formula": "Bớt đi / Tách ra (còn lại) → dùng dấu −", "note": "6 − 1 = 5: có 6, bớt 1, còn 5."},
            ]},
            {"category": "II. Tính chất & số 0", "items": [
                {"name": "Đổi chỗ trong phép cộng", "formula": "a + b = b + a   (vd: 2 + 7 = 7 + 2 = 9)"},
                {"name": "Cộng với 0", "formula": "a + 0 = 0 + a = a   (vd: 5 + 0 = 5)"},
                {"name": "Trừ đi 0", "formula": "a − 0 = a   (vd: 8 − 0 = 8)"},
                {"name": "Trừ chính nó", "formula": "a − a = 0   (vd: 8 − 8 = 0)"},
                {"name": "Cộng ↔ Trừ", "formula": "Nếu a + b = c thì c − a = b và c − b = a", "note": "6 + 3 = 9 → 9 − 6 = 3; 9 − 3 = 6."},
            ]},
            {"category": "III. Các phép cộng bằng 10 (cần thuộc)", "items": [
                {"name": "Bảng “tròn 10”", "formula": "1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10"},
                {"name": "Bảng trừ từ 10", "formula": "10 − 1 = 9 · 10 − 2 = 8 · 10 − 3 = 7 · 10 − 4 = 6 · 10 − 5 = 5"},
                {"name": "Cách tính nhẩm", "formula": "Cộng: đếm thêm từ số lớn hơn · Trừ: đếm bớt (đếm lùi)", "note": "2 + 6: đếm từ 6 thêm 2 → 7, 8 → 2 + 6 = 8."},
            ]},
        ],
        "example": "Trong bến có 8 chiếc ô tô, 3 chiếc rời bến. Hỏi trong bến còn lại mấy chiếc ô tô? Viết phép tính thích hợp.",
        "example_answer": "“Rời bến” là bớt đi nên dùng phép trừ: **8 − 3 = 5**.\nTrong bến còn lại **5 chiếc ô tô**.\nKiểm tra lại: 5 + 3 = 8 ✔.",
        "real_life": (
            "- Tính số bạn trong nhóm khi có thêm bạn đến chơi, số kẹo còn lại sau khi ăn bớt.\n"
            "- Đếm tiền lẻ, chia đồ dùng cho bạn, kiểm tra đồ vật còn thiếu."
        ),
        "quiz": [
            mcq("biet", "3 + 4 = ?", ["6", "7", "8", "5"], 1,
                "Đếm thêm từ 4: 5, 6, 7 (thêm 3 lần) → **3 + 4 = 7**.",
                alt="Dùng bảng cộng: 3 + 4 = 4 + 3 = 7."),
            mcq("biet", "9 − 5 = ?", ["4", "5", "3", "14"], 0,
                "Đếm lùi 5 lần từ 9: 8, 7, 6, 5, 4 → **9 − 5 = 4**.",
                alt="Vì 4 + 5 = 9 nên 9 − 5 = 4.",
                note="14 là kết quả của phép cộng 9 + 5 — hãy nhìn kỹ dấu “−”."),
            mcq("biet", "5 + 0 = ?", ["0", "1", "5", "50"], 2,
                "Một số cộng với 0 thì bằng chính số đó: **5 + 0 = 5**."),
            mcq("biet", "Có 4 quả bóng, gộp thêm 2 quả bóng nữa. Phép tính thích hợp là:",
                ["4 − 2 = 2", "4 + 2 = 6", "2 + 2 = 4", "6 − 2 = 4"], 1,
                "“Gộp thêm” là thêm vào nên dùng phép cộng: **4 + 2 = 6**."),
            mcq("hieu", "Biết 6 + 3 = 9. Phép trừ nào dưới đây đúng?",
                ["9 − 6 = 3", "9 − 3 = 5", "6 − 3 = 9", "9 − 9 = 3"], 0,
                "Từ 6 + 3 = 9 ta có hai phép trừ: 9 − 6 = 3 và 9 − 3 = 6.\nVậy phép tính đúng là **9 − 6 = 3**.",
                note="9 − 3 bằng 6 chứ không bằng 5; 9 − 9 = 0."),
            mcq("hieu", "Phép tính nào có kết quả bằng 10?",
                ["4 + 5", "7 + 2", "6 + 4", "10 − 1"], 2,
                "Tính từng phép: 4 + 5 = 9; 7 + 2 = 9; **6 + 4 = 10**; 10 − 1 = 9.\nVậy đáp án là 6 + 4.",
                alt="Nhớ các cặp “tròn 10”: 1 và 9, 2 và 8, 3 và 7, 4 và 6, 5 và 5 → 6 + 4 = 10."),
            tf("hieu", "Nhận định: “2 + 7 = 7 + 2.”", True,
               "2 + 7 = 9 và 7 + 2 = 9. Khi đổi chỗ các số trong phép cộng, kết quả không thay đổi → **Đúng**."),
            tf("hieu", "Nhận định: “8 − 8 = 8.”", False,
               "Có 8, bớt đi cả 8 thì không còn gì: 8 − 8 = **0**. Nhận định **Sai**.",
               note="Phân biệt: 8 − 0 = 8 (không bớt gì) nhưng 8 − 8 = 0 (bớt hết)."),
            mcq("vandung", "Trên cành có 7 con chim, sau đó 3 con bay đi. Hỏi trên cành còn lại mấy con chim?",
                ["10", "4", "3", "5"], 1,
                "“Bay đi” là bớt đi nên dùng phép trừ: 7 − 3 = 4.\nTrên cành còn lại **4 con chim**.",
                note="Nếu chọn 10 là em đã cộng 7 + 3 — đọc kỹ đề: chim bay đi thì số chim ít đi."),
            short("vandung", "Lan có 2 cái kẹo. Mẹ cho Lan thêm một số kẹo nữa thì Lan có tất cả 9 cái kẹo. Hỏi mẹ đã cho Lan mấy cái kẹo?", ["7"],
                  "Ta cần tìm số: 2 + ? = 9. Đếm thêm từ 2 đến 9: 3, 4, 5, 6, 7, 8, 9 → đếm thêm 7 lần.\nVậy mẹ đã cho Lan **7 cái kẹo**.",
                  unit="cái kẹo",
                  alt="Lấy tổng số kẹo trừ đi số kẹo Lan có lúc đầu: 9 − 2 = 7."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 4. LÀM QUEN VỚI MỘT SỐ HÌNH KHỐI
    # =====================================================================
    {
        "topic": "l1-cd04-hinh-khoi-vi-tri",
        "title": "Làm quen với một số hình khối",
        "icon": "🧊",
        "description": "Chủ đề 4 · SGK Toán 1 tập một (tr. 92–101): Bài 14 – Bài 16. Khối lập phương, khối hộp chữ nhật; vị trí và định hướng trong không gian.",
        "requirements": [
            "Nhận dạng được khối lập phương, khối hộp chữ nhật thông qua việc sử dụng bộ đồ dùng học tập cá nhân hoặc vật thật.",
            "Nhận biết được vị trí, định hướng trong không gian: trên – dưới, phải – trái, trước – sau, ở giữa.",
            "Nhận biết và thực hiện được việc lắp ghép, xếp hình gắn với các hình khối đơn giản.",
        ],
        "definition": (
            "- **Khối lập phương:** hình khối có các mặt đều là **hình vuông** (ví dụ: con xúc xắc, khối rubik).\n"
            "- **Khối hộp chữ nhật:** hình khối có các mặt là **hình chữ nhật** (ví dụ: hộp sữa giấy, viên gạch, bao diêm).\n"
            "- **Vị trí trong không gian:** trên – dưới, trước – sau, bên phải – bên trái, ở giữa.\n"
            "Hình vuông, hình chữ nhật là **hình phẳng** (vẽ trên giấy); khối lập phương, khối hộp chữ nhật là **hình khối** (cầm được, xếp chồng được)."
        ),
        "theory": (
            "### Bài 14. Khối lập phương, khối hộp chữ nhật\n"
            "- Nhận dạng khối lập phương, khối hộp chữ nhật qua đồ vật thật và bộ đồ dùng học Toán.\n"
            "- Đếm số khối lập phương/khối hộp chữ nhật trong hình xếp; xếp các khối thành hình theo mẫu.\n"
            "### Bài 15. Vị trí, định hướng trong không gian\n"
            "- Mô tả vị trí đồ vật: ở trên, ở dưới, ở trước, ở sau, ở giữa, bên phải, bên trái.\n"
            "- Tay cầm bút viết thường là tay phải; khi đứng đối diện nhau thì bên phải của em là bên trái của bạn.\n"
            "### Bài 16. Luyện tập chung\n"
            "- Nhận dạng hình khối, mô tả vị trí đồ vật trong tranh, xếp hình khối theo yêu cầu."
        ),
        "formulas": [
            {"category": "I. Nhận dạng hình khối", "items": [
                {"name": "Khối lập phương", "formula": "Các mặt đều là hình vuông", "note": "Con xúc xắc, khối rubik, hộp quà vuông."},
                {"name": "Khối hộp chữ nhật", "formula": "Các mặt là hình chữ nhật (có thể có 2 mặt hình vuông)", "note": "Hộp sữa, viên gạch, hộp bút, tủ lạnh."},
                {"name": "Phân biệt", "formula": "Hình phẳng (vẽ trên giấy) ≠ Hình khối (cầm được)", "note": "Mặt của khối lập phương là hình vuông."},
            ]},
            {"category": "II. Vị trí – định hướng", "items": [
                {"name": "Trên – dưới", "formula": "Quyển sách ở trên bàn · Con mèo ở dưới gầm bàn"},
                {"name": "Trước – sau", "formula": "Bạn đứng trước em · Em đứng sau bạn"},
                {"name": "Phải – trái", "formula": "Xác định theo tay phải, tay trái của chính mình (hoặc của nhân vật trong tranh)"},
                {"name": "Ở giữa", "formula": "Vật nằm giữa hai vật khác (A – B – C: B ở giữa)"},
            ]},
        ],
        "example": "Trên kệ, từ trái sang phải có: con gấu, hộp bút (khối hộp chữ nhật), con xúc xắc (khối lập phương). Đồ vật nào ở giữa? Đồ vật nào có dạng khối lập phương?",
        "example_answer": "- Ba đồ vật: con gấu – hộp bút – con xúc xắc → **hộp bút ở giữa**.\n- **Con xúc xắc** có dạng khối lập phương (các mặt đều là hình vuông).",
        "real_life": (
            "- Xếp đồ chơi, xếp sách vở gọn gàng; nhận ra hình dạng các hộp, thùng đựng đồ.\n"
            "- Chỉ đường, mô tả vị trí đồ vật cho người khác: “quyển truyện ở ngăn trên, bên trái”."
        ),
        "quiz": [
            mcq("biet", "Con xúc xắc có dạng khối gì?",
                ["Khối lập phương", "Khối hộp chữ nhật", "Hình tròn", "Hình tam giác"], 0,
                "Các mặt của con xúc xắc đều là hình vuông → **khối lập phương**."),
            mcq("biet", "Viên gạch (hoặc hộp sữa giấy) thường có dạng hình gì?",
                ["Khối lập phương", "Khối hộp chữ nhật", "Hình vuông", "Hình chữ nhật"], 1,
                "Viên gạch có các mặt là hình chữ nhật và cầm được → **khối hộp chữ nhật**.",
                note="“Hình chữ nhật” là hình phẳng vẽ trên giấy; viên gạch là đồ vật cầm được nên là hình khối."),
            mcq("biet", "Các mặt của khối lập phương đều là hình gì?",
                ["Hình tròn", "Hình tam giác", "Hình vuông", "Hình chữ nhật dài"], 2,
                "Mỗi mặt của khối lập phương là một **hình vuông**."),
            mcq("biet", "Quyển sách đặt trên mặt bàn. Vậy mặt bàn ở … quyển sách.",
                ["trên", "dưới", "trước", "bên trái"], 1,
                "Quyển sách ở trên mặt bàn thì mặt bàn ở **dưới** quyển sách."),
            mcq("hieu", "Ba bạn xếp hàng dọc: An đứng đầu, Bình đứng sau An, Chi đứng sau Bình. Bạn nào đứng ở giữa?",
                ["An", "Bình", "Chi", "Không có ai"], 1,
                "Thứ tự hàng: An – Bình – Chi. Bạn có một bạn đứng trước và một bạn đứng sau là **Bình** → Bình đứng ở giữa."),
            mcq("hieu", "Trên kệ, từ trái sang phải có: quả bóng, con gấu, ô tô. Đồ vật ở bên phải con gấu là:",
                ["quả bóng", "ô tô", "con gấu", "không có đồ vật nào"], 1,
                "Theo thứ tự từ trái sang phải: quả bóng – con gấu – ô tô.\nĐồ vật đứng sau con gấu theo chiều sang phải là **ô tô**.",
                note="Quả bóng ở bên trái con gấu."),
            tf("hieu", "Nhận định: “Khối lập phương có các mặt là hình vuông nên khối lập phương chính là hình vuông.”", False,
               "Hình vuông là hình phẳng; khối lập phương là hình khối có **các mặt** là hình vuông. Hai hình này khác nhau → nhận định **Sai**."),
            tf("hieu", "Con mèo nằm dưới gầm bàn, quả bóng ở trên mặt bàn.\nNhận định: “Quả bóng ở dưới con mèo.”", False,
               "Quả bóng ở trên mặt bàn, con mèo ở dưới gầm bàn → quả bóng ở **trên** con mèo. Nhận định **Sai**."),
            mcq("vandung", "Bạn Việt xếp các khối lập phương thành một cái tháp: tầng dưới cùng có 3 khối, tầng giữa có 2 khối, tầng trên cùng có 1 khối. Cái tháp có tất cả bao nhiêu khối lập phương?",
                ["5", "6", "3", "7"], 1,
                "Đếm từng tầng: tầng dưới 3 khối, tầng giữa 2 khối, tầng trên 1 khối.\n3 + 2 = 5; 5 + 1 = 6. Cái tháp có **6 khối lập phương**.",
                alt="Đếm lần lượt: 1, 2, 3 (tầng dưới), 4, 5 (tầng giữa), 6 (tầng trên)."),
            short("vandung", "Giá sách có 3 ngăn: ngăn trên cùng có 4 quyển truyện, ngăn ở giữa có 3 quyển, ngăn dưới cùng có 2 quyển. Hỏi ngăn ở giữa và ngăn dưới cùng có tất cả bao nhiêu quyển truyện?", ["5"],
                  "Ngăn ở giữa có 3 quyển, ngăn dưới cùng có 2 quyển.\nGộp lại: 3 + 2 = 5. Có tất cả **5 quyển truyện**.",
                  unit="quyển",
                  note="Không cộng ngăn trên cùng (4 quyển) vì đề chỉ hỏi ngăn ở giữa và ngăn dưới cùng."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 5. ÔN TẬP HỌC KÌ 1
    # =====================================================================
    {
        "topic": "l1-cd05-on-tap-hoc-ki-1",
        "title": "Ôn tập học kì 1",
        "icon": "📝",
        "description": "Chủ đề 5 · SGK Toán 1 tập một (tr. 102–113): Bài 17 – Bài 20. Ôn tập các số, phép cộng, phép trừ trong phạm vi 10 và hình học.",
        "requirements": [
            "Củng cố việc đếm, đọc, viết, so sánh, xếp thứ tự các số trong phạm vi 10.",
            "Thực hiện thành thạo phép cộng, phép trừ (tính nhẩm) trong phạm vi 10.",
            "Làm quen với việc thực hiện tính toán trong trường hợp có hai dấu phép tính cộng, trừ (theo thứ tự từ trái sang phải).",
            "Nhận dạng được các hình phẳng (hình vuông, hình tròn, hình tam giác, hình chữ nhật) và các hình khối (khối lập phương, khối hộp chữ nhật).",
            "Vận dụng phép cộng, phép trừ để giải quyết tình huống thực tế đơn giản.",
        ],
        "definition": (
            "Chủ đề ôn tập giúp em hệ thống lại toàn bộ kiến thức học kì 1:\n"
            "- Các số từ 0 đến 10 (đếm, so sánh, mấy và mấy).\n"
            "- Phép cộng, phép trừ trong phạm vi 10.\n"
            "- Hình phẳng, hình khối và vị trí trong không gian.\n"
            "- **Tính có hai dấu phép tính:** thực hiện lần lượt **từ trái sang phải**."
        ),
        "theory": (
            "### Bài 17. Ôn tập các số trong phạm vi 10\n"
            "- Đếm, đọc, viết số; so sánh và sắp xếp; tìm số lớn nhất, bé nhất; mấy và mấy.\n"
            "### Bài 18. Ôn tập phép cộng, phép trừ trong phạm vi 10\n"
            "- Tính nhẩm theo bảng cộng, bảng trừ; viết phép tính thích hợp với tranh; tính có hai dấu phép tính (từ trái sang phải).\n"
            "### Bài 19. Ôn tập hình học\n"
            "- Nhận dạng hình vuông, hình tròn, hình tam giác, hình chữ nhật, khối lập phương, khối hộp chữ nhật; đếm hình; vị trí trên – dưới, trái – phải, trước – sau.\n"
            "### Bài 20. Ôn tập chung\n"
            "- Tổng hợp các dạng bài: số, phép tính, hình học và bài toán thực tế."
        ),
        "formulas": [
            {"category": "I. Số trong phạm vi 10", "items": [
                {"name": "Thứ tự", "formula": "0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10"},
                {"name": "Mấy và mấy", "formula": "Nếu a gồm b và c thì b + c = a", "note": "7 gồm 3 và 4 → 3 + 4 = 7."},
            ]},
            {"category": "II. Phép cộng, phép trừ", "items": [
                {"name": "Đổi chỗ", "formula": "a + b = b + a"},
                {"name": "Số 0", "formula": "a + 0 = a · a − 0 = a · a − a = 0"},
                {"name": "Cộng ↔ Trừ", "formula": "a + b = c ⇒ c − a = b; c − b = a"},
                {"name": "Hai dấu phép tính", "formula": "Tính lần lượt từ trái sang phải", "note": "5 − 2 + 3: 5 − 2 = 3, rồi 3 + 3 = 6."},
            ]},
            {"category": "III. Hình học", "items": [
                {"name": "Hình phẳng", "formula": "Vuông (4 cạnh bằng nhau) · Chữ nhật (4 cạnh) · Tam giác (3 cạnh) · Tròn (không có cạnh)"},
                {"name": "Hình khối", "formula": "Khối lập phương (mặt hình vuông) · Khối hộp chữ nhật (mặt hình chữ nhật)"},
            ]},
        ],
        "example": "Tính: 4 + 3 − 2 = ?",
        "example_answer": "Tính lần lượt từ trái sang phải:\n- 4 + 3 = 7\n- 7 − 2 = 5\nVậy **4 + 3 − 2 = 5**.",
        "real_life": (
            "- Kiểm tra lại đồ dùng học tập (đủ hay thiếu, nhiều hay ít).\n"
            "- Tính nhẩm nhanh khi chơi trò chơi, đi chợ cùng bố mẹ."
        ),
        "quiz": [
            mcq("biet", "Số lớn nhất trong các số 3, 8, 6, 5 là:", ["3", "8", "6", "5"], 1,
                "So sánh: 3 < 5 < 6 < 8. Số lớn nhất là **8**."),
            mcq("biet", "10 − 4 = ?", ["5", "6", "7", "14"], 1,
                "Đếm lùi 4 lần từ 10: 9, 8, 7, 6 → **10 − 4 = 6**.",
                alt="Vì 4 + 6 = 10 nên 10 − 4 = 6."),
            mcq("biet", "Hình có 4 cạnh dài bằng nhau là:",
                ["Hình tròn", "Hình tam giác", "Hình vuông", "Khối hộp chữ nhật"], 2,
                "**Hình vuông** có 4 cạnh dài bằng nhau."),
            mcq("biet", "Số 7 gồm 4 và mấy?", ["2", "3", "4", "11"], 1,
                "Từ 4 đếm thêm: 5, 6, 7 (3 lần) → **7 gồm 4 và 3**."),
            mcq("hieu", "Phép tính nào có kết quả bé nhất?",
                ["2 + 5", "9 − 1", "4 + 4", "10 − 6"], 3,
                "Tính: 2 + 5 = 7; 9 − 1 = 8; 4 + 4 = 8; 10 − 6 = 4.\nSố bé nhất là 4 → phép tính **10 − 6**."),
            mcq("hieu", "Dấu thích hợp điền vào chỗ chấm: 4 + 3 … 9 − 2",
                [">", "<", "=", "+"], 2,
                "Tính từng vế: 4 + 3 = 7; 9 − 2 = 7. Hai kết quả bằng nhau → **4 + 3 = 9 − 2**.",
                note="Phải tính kết quả hai bên trước rồi mới so sánh."),
            tf("hieu", "Nhận định: “Số 0 bé hơn tất cả các số 1, 2, 3, …, 10.”", True,
               "Trong dãy số, 0 đứng đầu tiên nên 0 bé hơn mọi số đứng sau nó → **Đúng**."),
            tf("hieu", "Nhận định: “Kết quả của phép tính 5 + 4 lớn hơn 10.”", False,
               "5 + 4 = 9 và 9 < 10. Vậy kết quả **không** lớn hơn 10 → nhận định **Sai**."),
            mcq("vandung", "Hà có 5 bút chì. Hà cho em 2 bút chì, sau đó mẹ mua thêm cho Hà 3 bút chì. Hỏi lúc này Hà có mấy bút chì?",
                ["6", "10", "4", "0"], 0,
                "Cho em 2 bút: 5 − 2 = 3 (bút). Mẹ mua thêm 3 bút: 3 + 3 = 6 (bút).\nViết gọn: 5 − 2 + 3 = **6**. Hà có **6 bút chì**.",
                note="Tính lần lượt từ trái sang phải. Nếu chọn 10 là em đã cộng cả 2 bút cho em — “cho em” là bớt đi."),
            short("vandung", "Trong vườn có 10 cây, trong đó có 6 cây cam, còn lại là cây bưởi. Hỏi trong vườn có mấy cây bưởi?", ["4"],
                  "Tách 10 cây thành cây cam và cây bưởi: 10 − 6 = 4.\nTrong vườn có **4 cây bưởi**.",
                  unit="cây",
                  alt="10 gồm 6 và 4 → số cây bưởi là 4."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 6. CÁC SỐ ĐẾN 100
    # =====================================================================
    {
        "topic": "l1-cd06-cac-so-den-100",
        "title": "Các số đến 100",
        "icon": "💯",
        "description": "Chủ đề 6 · SGK Toán 1 tập hai (tr. 4–27): Bài 21 – Bài 24. Số có hai chữ số, chục và đơn vị, so sánh số, bảng các số từ 1 đến 100.",
        "requirements": [
            "Đếm, đọc, viết được các số trong phạm vi 20; trong phạm vi 100.",
            "Nhận biết được chục và đơn vị, số tròn chục.",
            "Nhận biết được cách so sánh, xếp thứ tự các số trong phạm vi 100 (ở các nhóm có không quá 4 số).",
            "Sử dụng được bảng các số từ 1 đến 100 để tìm số liền trước, số liền sau và quy luật của dãy số.",
        ],
        "definition": (
            "- **10 đơn vị = 1 chục.** Số 10 còn gọi là “một chục”.\n"
            "- **Số có hai chữ số** gồm chữ số hàng chục (bên trái) và chữ số hàng đơn vị (bên phải): 45 gồm 4 chục và 5 đơn vị.\n"
            "- **Số tròn chục:** 10, 20, 30, 40, 50, 60, 70, 80, 90 (chữ số hàng đơn vị là 0).\n"
            "- **Số 100** (một trăm) là số liền sau của 99; 100 = 10 chục."
        ),
        "theory": (
            "### Bài 21. Số có hai chữ số\n"
            "- Các số từ 11 đến 20: 11 (mười một), 12 (mười hai)… 15 (mười lăm)… 20 (hai mươi).\n"
            "- Các số có hai chữ số đến 99: đọc theo chục và đơn vị: 21 (hai mươi mốt), 34 (ba mươi tư), 55 (năm mươi lăm), 70 (bảy mươi).\n"
            "- Viết số theo cấu tạo: 3 chục và 6 đơn vị viết là 36.\n"
            "### Bài 22. So sánh số có hai chữ số\n"
            "- So sánh chữ số hàng chục trước: số nào có hàng chục lớn hơn thì lớn hơn (58 < 85).\n"
            "- Nếu hàng chục bằng nhau thì so sánh hàng đơn vị (47 > 43).\n"
            "### Bài 23. Bảng các số từ 1 đến 100\n"
            "- Bảng có 10 hàng, mỗi hàng 10 số. Đi sang phải 1 ô: thêm 1; đi xuống 1 ô: thêm 10.\n"
            "- Tìm số liền trước, liền sau; nhận ra các số tròn chục ở cột cuối.\n"
            "### Bài 24. Luyện tập chung\n"
            "- Đọc, viết, phân tích số; so sánh, sắp xếp; số tròn chục; bài toán thực tế về chục và đơn vị."
        ),
        "formulas": [
            {"category": "I. Chục và đơn vị", "items": [
                {"name": "Quy đổi", "formula": "10 đơn vị = 1 chục · 10 chục = 100"},
                {"name": "Cấu tạo số", "formula": "Số ab gồm a chục và b đơn vị", "note": "45 gồm 4 chục và 5 đơn vị; 70 gồm 7 chục và 0 đơn vị."},
                {"name": "Số tròn chục", "formula": "10, 20, 30, 40, 50, 60, 70, 80, 90"},
            ]},
            {"category": "II. Cách đọc số", "items": [
                {"name": "Từ 11 đến 19", "formula": "mười một, mười hai, …, mười lăm, …, mười chín", "note": "15 đọc là “mười lăm” (không đọc “mười năm”)."},
                {"name": "Hàng đơn vị là 1", "formula": "21: hai mươi mốt · 41: bốn mươi mốt"},
                {"name": "Hàng đơn vị là 4", "formula": "24: hai mươi tư (hoặc hai mươi bốn)"},
                {"name": "Hàng đơn vị là 5", "formula": "25: hai mươi lăm"},
            ]},
            {"category": "III. So sánh số có hai chữ số", "items": [
                {"name": "Bước 1", "formula": "So sánh chữ số hàng chục: hàng chục lớn hơn thì số lớn hơn", "note": "58 < 85 vì 5 < 8."},
                {"name": "Bước 2", "formula": "Hàng chục bằng nhau thì so sánh hàng đơn vị", "note": "47 > 43 vì 7 > 3."},
                {"name": "Bảng 1 – 100", "formula": "Sang phải 1 ô: +1 · Xuống dưới 1 ô: +10"},
            ]},
        ],
        "example": "a) Viết số gồm 6 chục và 2 đơn vị, rồi đọc số đó.\nb) So sánh: 39 … 41.",
        "example_answer": "a) 6 chục và 2 đơn vị viết là **62**, đọc là **sáu mươi hai**.\nb) Hàng chục: 3 < 4 nên **39 < 41**.",
        "real_life": (
            "- Đọc số nhà, số trang sách, số ghế trong rạp, số áo cầu thủ.\n"
            "- Đếm đồ vật theo chục (bó que tính, vỉ trứng 10 quả) để đếm nhanh."
        ),
        "quiz": [
            mcq("biet", "Số gồm 3 chục và 6 đơn vị là:", ["63", "36", "306", "9"], 1,
                "Chữ số hàng chục là 3 (viết bên trái), chữ số hàng đơn vị là 6 (viết bên phải) → **36**.",
                note="63 là số gồm 6 chục và 3 đơn vị — đừng viết ngược thứ tự."),
            mcq("biet", "Số “bảy mươi lăm” viết là:", ["705", "57", "75", "7"], 2,
                "Bảy mươi → 7 chục; lăm → 5 đơn vị. Viết là **75**."),
            mcq("biet", "Trong các số dưới đây, số nào là số tròn chục?", ["45", "60", "61", "9"], 1,
                "Số tròn chục có chữ số hàng đơn vị là 0 → **60** (6 chục)."),
            mcq("biet", "Số liền sau của 39 là:", ["38", "40", "49", "30"], 1,
                "Số liền sau là số đó thêm 1: 39 thêm 1 là **40** (3 chục 9 đơn vị thêm 1 đơn vị thành 4 chục).",
                note="38 là số liền trước của 39."),
            mcq("hieu", "Dấu thích hợp điền vào chỗ chấm: 58 … 85", [">", "<", "=", "+"], 1,
                "So sánh chữ số hàng chục: 5 < 8 nên **58 < 85**.",
                note="Hai số có cùng các chữ số 5 và 8 nhưng giá trị khác nhau: phải xem chữ số nào ở hàng chục."),
            mcq("hieu", "Các số 47, 74, 40, 70 xếp theo thứ tự từ bé đến lớn là:",
                ["40, 47, 70, 74", "47, 40, 70, 74", "40, 70, 47, 74", "74, 70, 47, 40"], 0,
                "Nhóm hàng chục 4: 40 < 47; nhóm hàng chục 7: 70 < 74; mà 4 chục < 7 chục.\nThứ tự từ bé đến lớn: **40, 47, 70, 74**.",
                note="Đáp án 74, 70, 47, 40 là thứ tự từ lớn đến bé."),
            tf("hieu", "Nhận định: “Số 16 đọc là ‘mười sáu’ và gồm 1 chục và 6 đơn vị.”", True,
               "16 có chữ số hàng chục là 1, hàng đơn vị là 6; đọc là “mười sáu” → **Đúng**."),
            tf("hieu", "Nhận định: “Trong bảng các số từ 1 đến 100, số ở ngay bên dưới số 34 (cùng cột) là 35.”", False,
               "Đi xuống 1 ô thì số tăng thêm 10 (1 chục): ô dưới số 34 là **44**. Số 35 nằm ở ngay bên phải số 34. Nhận định **Sai**."),
            mcq("vandung", "Mẹ mua 5 bó đũa, mỗi bó có 1 chục chiếc đũa. Hỏi mẹ mua tất cả bao nhiêu chiếc đũa?",
                ["5", "15", "50", "10"], 2,
                "Mỗi bó có 1 chục chiếc, 5 bó có 5 chục chiếc. 5 chục = **50** chiếc đũa.",
                alt="Đếm theo chục: 10, 20, 30, 40, 50."),
            short("vandung", "Tìm số có hai chữ số, biết chữ số hàng chục là 6 và chữ số hàng đơn vị bé hơn chữ số hàng chục 2 đơn vị.", ["64"],
                  "Chữ số hàng đơn vị: 6 − 2 = 4.\nSố cần tìm có 6 chục và 4 đơn vị: **64**.",
                  note="Viết chữ số hàng chục ở bên trái, chữ số hàng đơn vị ở bên phải (không viết 46)."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 7. ĐỘ DÀI VÀ ĐO ĐỘ DÀI
    # =====================================================================
    {
        "topic": "l1-cd07-do-dai",
        "title": "Độ dài và đo độ dài",
        "icon": "📏",
        "description": "Chủ đề 7 · SGK Toán 1 tập hai (tr. 28–43): Bài 25 – Bài 28. Dài hơn – ngắn hơn, đơn vị xăng-ti-mét, thực hành ước lượng và đo độ dài.",
        "requirements": [
            "Nhận biết được về “dài hơn”, “ngắn hơn” (“cao hơn”, “thấp hơn”).",
            "Nhận biết được đơn vị đo độ dài: cm (xăng-ti-mét); đọc và viết được số đo độ dài trong phạm vi 100 cm.",
            "Thực hiện được việc đo và ước lượng độ dài theo đơn vị đo tự quy ước (gang tay, bước chân, que tính…).",
            "Thực hiện được việc đo độ dài bằng thước thẳng với đơn vị đo là cm.",
            "Giải quyết được một số vấn đề thực tiễn đơn giản liên quan đến đo độ dài.",
        ],
        "definition": (
            "- **Dài hơn – ngắn hơn:** đặt hai vật thẳng hàng, một đầu bằng nhau; vật nào thò ra xa hơn thì dài hơn.\n"
            "- **Xăng-ti-mét** là đơn vị đo độ dài, viết tắt là **cm**. Trên thước kẻ, khoảng cách giữa hai vạch số liền nhau là 1 cm.\n"
            "- **Đơn vị tự quy ước:** gang tay, sải tay, bước chân, que tính… (mỗi người có thể đo ra kết quả khác nhau)."
        ),
        "theory": (
            "### Bài 25. Dài hơn, ngắn hơn\n"
            "- So sánh trực tiếp độ dài hai vật (đặt cạnh nhau, một đầu bằng nhau); so sánh cao hơn – thấp hơn; tìm vật dài nhất, ngắn nhất.\n"
            "- Đo độ dài bằng đơn vị tự quy ước: bàn dài 5 gang tay, bảng dài 8 sải tay…\n"
            "### Bài 26. Đơn vị đo độ dài\n"
            "- Làm quen đơn vị **xăng-ti-mét (cm)**; đo bằng thước có vạch chia cm.\n"
            "- Cách đo: đặt **vạch 0** của thước trùng với một đầu của vật, đọc số ở vạch trùng với đầu kia.\n"
            "### Bài 27. Thực hành ước lượng và đo độ dài\n"
            "- Ước lượng độ dài đồ vật (bút chì khoảng 15 cm…) rồi đo lại bằng thước để kiểm tra.\n"
            "- Thực hành đo bằng gang tay, bước chân, que tính.\n"
            "### Bài 28. Luyện tập chung\n"
            "- So sánh, đo độ dài; cộng, trừ số đo độ dài có đơn vị cm; giải bài toán thực tế."
        ),
        "formulas": [
            {"category": "I. Đơn vị đo độ dài", "items": [
                {"name": "Xăng-ti-mét", "formula": "Viết tắt: cm · đọc: xăng-ti-mét", "note": "15 cm đọc là “mười lăm xăng-ti-mét”."},
                {"name": "Thước kẻ", "formula": "Hai vạch số liền nhau cách nhau 1 cm"},
            ]},
            {"category": "II. Cách đo độ dài bằng thước", "items": [
                {"name": "Bước 1", "formula": "Đặt vạch 0 của thước trùng với một đầu của vật"},
                {"name": "Bước 2", "formula": "Đặt thước dọc theo vật (thẳng, sát vật)"},
                {"name": "Bước 3", "formula": "Đọc số ở vạch trùng với đầu còn lại → độ dài vật", "note": "Đầu kia ở vạch 7 → vật dài 7 cm."},
            ]},
            {"category": "III. Tính với số đo độ dài", "items": [
                {"name": "Cộng", "formula": "6 cm + 3 cm = 9 cm", "note": "Cộng các số rồi viết đơn vị cm."},
                {"name": "Trừ (dài hơn bao nhiêu)", "formula": "9 cm − 6 cm = 3 cm", "note": "Vật 9 cm dài hơn vật 6 cm là 3 cm."},
            ]},
        ],
        "example": "Bút chì xanh dài 8 cm, bút chì đỏ dài 5 cm. Bút chì nào dài hơn và dài hơn bao nhiêu xăng-ti-mét?",
        "example_answer": "So sánh 8 > 5 nên **bút chì xanh dài hơn**.\nDài hơn: 8 cm − 5 cm = **3 cm**.",
        "real_life": (
            "- Đo chiều dài bàn học, quyển vở, chiều cao của em để theo dõi lớn lên.\n"
            "- Ước lượng chiều dài đồ vật khi không có thước (dùng gang tay, bước chân)."
        ),
        "quiz": [
            mcq("biet", "Xăng-ti-mét viết tắt là:", ["m", "cm", "kg", "xm"], 1,
                "Xăng-ti-mét viết tắt là **cm**."),
            mcq("biet", "Bút chì đỏ dài hơn bút chì xanh. Vậy bút chì xanh … bút chì đỏ.",
                ["dài hơn", "ngắn hơn", "cao hơn", "dài bằng"], 1,
                "Bút đỏ dài hơn bút xanh thì ngược lại, bút xanh **ngắn hơn** bút đỏ."),
            mcq("biet", "Khi đo độ dài bằng thước, em đặt vạch nào của thước trùng với một đầu của vật?",
                ["Vạch 0", "Vạch 1", "Vạch 10", "Vạch bất kì"], 0,
                "Phải đặt **vạch 0** trùng với một đầu của vật thì số đọc được ở đầu kia mới đúng là độ dài của vật.",
                note="Nếu đặt vạch 1 ở đầu vật, kết quả đọc được sẽ bị thừa 1 cm."),
            mcq("biet", "Số đo “15 cm” được đọc là:",
                ["Mười lăm xăng-ti-mét", "Một năm xăng-ti-mét", "Năm mươi một xăng-ti-mét", "Mười năm mét"], 0,
                "15 đọc là “mười lăm”, cm đọc là “xăng-ti-mét” → **Mười lăm xăng-ti-mét**."),
            mcq("hieu", "Một đầu chiếc tẩy đặt ở vạch 0, đầu kia ở vạch 4 của thước. Chiếc tẩy dài:",
                ["0 cm", "3 cm", "4 cm", "5 cm"], 2,
                "Vạch 0 trùng một đầu tẩy, đầu kia ở vạch 4 → chiếc tẩy dài **4 cm**."),
            mcq("hieu", "Em có thể đo độ dài đồ vật nào dưới đây bằng thước kẻ có vạch chia xăng-ti-mét của mình?",
                ["Chiều dài sân trường", "Chiều dài cái bút chì", "Quãng đường từ nhà đến trường", "Chiều dài một con sông"], 1,
                "Thước kẻ của em chỉ dài khoảng 20 – 30 cm, phù hợp để đo đồ vật nhỏ như **cái bút chì**.\nSân trường, quãng đường, con sông dài hơn rất nhiều."),
            tf("hieu", "Nhận định: “6 cm + 3 cm = 9 cm.”", True,
               "Cộng các số: 6 + 3 = 9, rồi viết đơn vị: **9 cm** → **Đúng**."),
            tf("hieu", "Mai và bố cùng đo chiều dài một cái bàn bằng gang tay. Mai đo được 6 gang tay, bố đo được 4 gang tay.\nNhận định: “Gang tay của Mai dài hơn gang tay của bố.”", False,
               "Cùng một cái bàn: gang tay càng **ngắn** thì phải đo càng **nhiều** lần. Mai đo nhiều lần hơn (6 > 4) nên gang tay của Mai **ngắn hơn** gang tay của bố → **Sai**.",
               note="Đây là lí do người ta dùng đơn vị đo chung là xăng-ti-mét: ai đo cũng ra cùng kết quả."),
            mcq("vandung", "Sợi dây xanh dài 9 cm, sợi dây đỏ dài 6 cm. Sợi dây xanh dài hơn sợi dây đỏ bao nhiêu xăng-ti-mét?",
                ["15 cm", "3 cm", "2 cm", "6 cm"], 1,
                "Dài hơn bao nhiêu → lấy số lớn trừ số bé: 9 cm − 6 cm = **3 cm**.",
                note="15 cm là tổng độ dài hai sợi dây (9 + 6), không phải phần dài hơn."),
            short("vandung", "Bạn Nam nối một đoạn dây dài 5 cm với một đoạn dây dài 4 cm (nối sát nhau, không chồng lên nhau). Hỏi đoạn dây sau khi nối dài bao nhiêu xăng-ti-mét?", ["9", "9cm"],
                  "Nối hai đoạn là gộp lại độ dài: 5 cm + 4 cm = **9 cm**.",
                  unit="cm"),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 8. PHÉP CỘNG, PHÉP TRỪ (KHÔNG NHỚ) TRONG PHẠM VI 100
    # =====================================================================
    {
        "topic": "l1-cd08-cong-tru-pham-vi-100",
        "title": "Phép cộng, phép trừ (không nhớ) trong phạm vi 100",
        "icon": "🧮",
        "description": "Chủ đề 8 · SGK Toán 1 tập hai (tr. 44–71): Bài 29 – Bài 33. Cộng, trừ số có hai chữ số với số có một, hai chữ số (không nhớ); tính nhẩm số tròn chục; bài toán có lời văn.",
        "requirements": [
            "Thực hiện được phép cộng, phép trừ (không nhớ) các số trong phạm vi 100 (đặt tính rồi tính và tính nhẩm).",
            "Thực hiện được việc cộng, trừ nhẩm các số tròn chục.",
            "Làm quen với việc thực hiện tính toán trong trường hợp có hai dấu phép tính cộng, trừ (theo thứ tự từ trái sang phải).",
            "Nhận biết và viết được phép tính (cộng, trừ) phù hợp với câu trả lời của bài toán có lời văn và tính được kết quả đúng.",
        ],
        "definition": (
            "- **Đặt tính:** viết các số thẳng cột: đơn vị thẳng đơn vị, chục thẳng chục; viết dấu + hoặc − ở giữa, kẻ vạch ngang.\n"
            "- **Tính:** thực hiện **từ phải sang trái**: tính hàng đơn vị trước, hàng chục sau.\n"
            "- **Không nhớ:** cộng/trừ ở mỗi hàng đều không vượt quá 9 và không phải “mượn”.\n"
            "- **Bài toán có lời văn:** đọc kĩ đề, tìm cái đã cho, cái cần tìm; viết phép tính và câu trả lời."
        ),
        "theory": (
            "### Bài 29. Phép cộng số có hai chữ số với số có một chữ số\n"
            "- Ví dụ 42 + 4: 2 + 4 = 6, viết 6; hạ 4 → 46.\n"
            "### Bài 30. Phép cộng số có hai chữ số với số có hai chữ số\n"
            "- Ví dụ 42 + 35: 2 + 5 = 7, viết 7; 4 + 3 = 7, viết 7 → 77. Cộng nhẩm số tròn chục: 30 + 20 = 50 (3 chục + 2 chục = 5 chục).\n"
            "### Bài 31. Phép trừ số có hai chữ số cho số có một chữ số\n"
            "- Ví dụ 76 − 5: 6 − 5 = 1, viết 1; hạ 7 → 71. Đếm lùi để trừ nhẩm: 18 − 3 → 17, 16, 15.\n"
            "### Bài 32. Phép trừ số có hai chữ số cho số có hai chữ số\n"
            "- Ví dụ 86 − 64: 6 − 4 = 2; 8 − 6 = 2 → 22. Trừ nhẩm số tròn chục: 60 − 20 = 40.\n"
            "### Bài 33. Luyện tập chung\n"
            "- Tính có hai dấu phép tính từ trái sang phải: 37 + 12 − 23 = 49 − 23 = 26.\n"
            "- Giải bài toán có lời văn: “Trên cây có 74 quả thị, gió làm rụng 21 quả. Hỏi trên cây còn lại bao nhiêu quả?” → 74 − 21 = 53."
        ),
        "formulas": [
            {"category": "I. Đặt tính và tính", "items": [
                {"name": "Đặt tính", "formula": "Đơn vị thẳng cột đơn vị · Chục thẳng cột chục", "note": "Số có một chữ số viết thẳng cột hàng đơn vị."},
                {"name": "Thứ tự tính", "formula": "Từ phải sang trái: hàng đơn vị → hàng chục"},
                {"name": "Ví dụ cộng", "formula": "42 + 35 = 77   (2 + 5 = 7; 4 + 3 = 7)"},
                {"name": "Ví dụ trừ", "formula": "76 − 5 = 71   (6 − 5 = 1; hạ 7)"},
            ]},
            {"category": "II. Tính nhẩm số tròn chục", "items": [
                {"name": "Cộng", "formula": "30 + 20 = 50  (3 chục + 2 chục = 5 chục)"},
                {"name": "Trừ", "formula": "60 − 20 = 40  (6 chục − 2 chục = 4 chục)"},
            ]},
            {"category": "III. Hai dấu phép tính & bài toán có lời văn", "items": [
                {"name": "Hai dấu phép tính", "formula": "Tính lần lượt từ trái sang phải", "note": "37 + 12 − 23 = 49 − 23 = 26."},
                {"name": "Chọn phép tính", "formula": "Thêm, gộp, tất cả → phép cộng · Bớt, cho đi, bay đi, còn lại → phép trừ"},
                {"name": "Trình bày", "formula": "Phép tính: 74 − 21 = 53 · Trả lời: Trên cây còn lại 53 quả thị."},
            ]},
        ],
        "example": "Đặt tính rồi tính: 53 + 24 và 68 − 35.",
        "example_answer": (
            "- 53 + 24: 3 + 4 = 7, viết 7; 5 + 2 = 7, viết 7 → **77**.\n"
            "- 68 − 35: 8 − 5 = 3, viết 3; 6 − 3 = 3, viết 3 → **33**.\n"
            "Kiểm tra: 33 + 35 = 68 ✔."
        ),
        "real_life": (
            "- Tính số học sinh cả lớp (bạn nam + bạn nữ), số trang sách còn phải đọc.\n"
            "- Tính tiền khi mua bán đơn giản, đếm số đồ vật còn lại sau khi dùng."
        ),
        "quiz": [
            mcq("biet", "34 + 5 = ?", ["39", "84", "38", "29"], 0,
                "Cộng hàng đơn vị: 4 + 5 = 9; hàng chục giữ nguyên 3 → **39**.",
                note="84 là do cộng nhầm 5 vào hàng chục (3 + 5). Số 5 là 5 đơn vị nên phải cộng với hàng đơn vị."),
            mcq("biet", "76 − 5 = ?", ["26", "71", "81", "70"], 1,
                "Trừ hàng đơn vị: 6 − 5 = 1; hàng chục giữ nguyên 7 → **71**.",
                note="26 là do trừ nhầm vào hàng chục (7 − 5)."),
            mcq("biet", "40 + 30 = ?", ["7", "70", "43", "700"], 1,
                "4 chục + 3 chục = 7 chục = **70**."),
            mcq("biet", "Khi tính 52 + 36 (đặt tính), ta thực hiện theo thứ tự nào?",
                ["Cộng hàng chục trước, rồi cộng hàng đơn vị", "Cộng hàng đơn vị trước, rồi cộng hàng chục",
                 "Cộng chữ số nào trước cũng được", "Chỉ cộng hàng chục"], 1,
                "Đặt tính xong, ta tính **từ phải sang trái**: cộng hàng đơn vị trước (2 + 6 = 8), rồi hàng chục (5 + 3 = 8) → 88."),
            mcq("hieu", "Kết quả của 37 + 12 − 23 là:", ["26", "72", "49", "36"], 0,
                "Tính từ trái sang phải: 37 + 12 = 49; 49 − 23 = **26**.",
                note="49 mới chỉ là kết quả bước 1 — còn phải trừ tiếp 23."),
            mcq("hieu", "Phép tính nào có kết quả bằng 50?",
                ["20 + 20", "90 − 40", "70 − 30", "10 + 30"], 1,
                "Tính nhẩm số tròn chục: 20 + 20 = 40; **90 − 40 = 50**; 70 − 30 = 40; 10 + 30 = 40."),
            tf("hieu", "Bạn Bi đặt tính 45 − 3 bằng cách viết số 3 thẳng cột với chữ số 4 (hàng chục) và được kết quả 15.\nNhận định: “Bạn Bi làm đúng.”", False,
               "Số 3 là 3 đơn vị nên phải viết thẳng cột với chữ số 5 (hàng đơn vị).\nTính đúng: 5 − 3 = 2, hạ 4 → 45 − 3 = **42**. Bạn Bi làm **Sai**."),
            tf("hieu", "Nhận định: “65 − 25 = 40.”", True,
               "Hàng đơn vị: 5 − 5 = 0; hàng chục: 6 − 2 = 4 → 65 − 25 = **40** → **Đúng**.",
               alt="Kiểm tra bằng phép cộng: 40 + 25 = 65 ✔."),
            mcq("vandung", "Trên cây có 74 quả thị. Gió lay làm rụng 21 quả. Hỏi trên cây còn lại bao nhiêu quả thị?",
                ["95", "53", "43", "54"], 1,
                "“Rụng” là bớt đi nên dùng phép trừ: 74 − 21.\nHàng đơn vị: 4 − 1 = 3; hàng chục: 7 − 2 = 5 → 53.\nTrả lời: Trên cây còn lại **53 quả thị**.",
                note="95 là kết quả của phép cộng 74 + 21 — số quả trên cây phải ít đi chứ không nhiều lên."),
            short("vandung", "Lớp 1A có 23 bạn nữ và 15 bạn nam. Hỏi lớp 1A có tất cả bao nhiêu bạn?", ["38"],
                  "“Tất cả” là gộp lại nên dùng phép cộng: 23 + 15.\nHàng đơn vị: 3 + 5 = 8; hàng chục: 2 + 1 = 3 → 38.\nTrả lời: Lớp 1A có tất cả **38 bạn**.",
                  unit="bạn",
                  alt="Cộng chục với chục, đơn vị với đơn vị: 20 + 10 = 30; 3 + 5 = 8; 30 + 8 = 38."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 9. THỜI GIAN. GIỜ VÀ LỊCH
    # =====================================================================
    {
        "topic": "l1-cd09-thoi-gian-gio-lich",
        "title": "Thời gian. Giờ và lịch",
        "icon": "🕘",
        "description": "Chủ đề 9 · SGK Toán 1 tập hai (tr. 72–87): Bài 34 – Bài 37. Xem giờ đúng trên đồng hồ, các ngày trong tuần, xem lịch tờ hằng ngày.",
        "requirements": [
            "Nhận biết được giờ đúng trên đồng hồ; thực hiện được việc đọc giờ đúng trên đồng hồ.",
            "Nhận biết được mỗi tuần lễ có 7 ngày và tên gọi, thứ tự các ngày trong tuần lễ.",
            "Xác định được thứ, ngày trong tuần khi xem lịch (loại lịch tờ hằng ngày).",
            "Giải quyết được một số vấn đề thực tiễn đơn giản liên quan đến đọc giờ đúng và xem lịch.",
        ],
        "definition": (
            "- **Đồng hồ** có kim ngắn (chỉ **giờ**) và kim dài (chỉ **phút**).\n"
            "- **Giờ đúng:** kim dài chỉ vào số **12**, kim ngắn chỉ vào số nào thì đó là mấy giờ (kim ngắn chỉ 8 → 8 giờ).\n"
            "- **Một tuần lễ có 7 ngày:** Thứ Hai, Thứ Ba, Thứ Tư, Thứ Năm, Thứ Sáu, Thứ Bảy, Chủ nhật.\n"
            "- **Lịch tờ hằng ngày** cho biết: tháng, ngày (số in to) và thứ."
        ),
        "theory": (
            "### Bài 34. Xem giờ đúng trên đồng hồ\n"
            "- Nhận biết mặt đồng hồ (12 số), kim giờ, kim phút; đọc giờ đúng; quay kim đồng hồ chỉ giờ đúng.\n"
            "- Gắn giờ với hoạt động hằng ngày: 6 giờ thức dậy, 7 giờ vào học, 9 giờ đi ngủ…\n"
            "### Bài 35. Các ngày trong tuần\n"
            "- Tên và thứ tự 7 ngày trong tuần; hôm qua – hôm nay – ngày mai; ngày đi học, ngày nghỉ.\n"
            "### Bài 36. Thực hành xem lịch và giờ\n"
            "- Đọc lịch tờ: hôm nay là thứ mấy, ngày bao nhiêu, tháng mấy; tính ngày, thứ của hôm qua, ngày mai.\n"
            "- Đọc thời gian biểu, lịch hoạt động trong tuần.\n"
            "### Bài 37. Luyện tập chung\n"
            "- Xem giờ đúng, xem lịch, giải quyết tình huống thực tế về thời gian."
        ),
        "formulas": [
            {"category": "I. Đồng hồ – Giờ đúng", "items": [
                {"name": "Kim ngắn", "formula": "Chỉ giờ"},
                {"name": "Kim dài", "formula": "Chỉ phút"},
                {"name": "Giờ đúng", "formula": "Kim dài chỉ số 12 · Kim ngắn chỉ số k → k giờ", "note": "Kim dài chỉ 12, kim ngắn chỉ 3 → 3 giờ."},
            ]},
            {"category": "II. Tuần lễ và lịch", "items": [
                {"name": "Tuần lễ", "formula": "1 tuần lễ = 7 ngày"},
                {"name": "Thứ tự các ngày", "formula": "Thứ Hai → Thứ Ba → Thứ Tư → Thứ Năm → Thứ Sáu → Thứ Bảy → Chủ nhật → (Thứ Hai tuần sau)"},
                {"name": "Hôm qua – hôm nay – ngày mai", "formula": "Hôm qua = ngày liền trước hôm nay · Ngày mai = ngày liền sau hôm nay"},
                {"name": "Cùng thứ tuần sau", "formula": "Ngày cùng thứ của tuần sau = ngày hôm nay + 7", "note": "Thứ Hai ngày 10 → Thứ Hai tuần sau là ngày 17."},
            ]},
        ],
        "example": "Tờ lịch hôm nay ghi: Tháng 5 – 19 – Thứ Tư. Hỏi ngày mai là thứ mấy, ngày bao nhiêu?",
        "example_answer": "Ngày liền sau Thứ Tư là **Thứ Năm**; ngày liền sau ngày 19 là ngày **20**.\nVậy ngày mai là Thứ Năm, ngày 20 tháng 5.",
        "real_life": (
            "- Biết giờ để đi học đúng giờ, sắp xếp giờ ăn, giờ học, giờ ngủ.\n"
            "- Xem lịch để nhớ ngày sinh nhật, ngày nghỉ, lịch học trong tuần."
        ),
        "quiz": [
            mcq("biet", "Một tuần lễ có mấy ngày?", ["5", "6", "7", "10"], 2,
                "Một tuần lễ có **7 ngày**: Thứ Hai, Thứ Ba, Thứ Tư, Thứ Năm, Thứ Sáu, Thứ Bảy, Chủ nhật."),
            mcq("biet", "Đồng hồ có kim dài chỉ số 12, kim ngắn chỉ số 8. Đồng hồ chỉ:",
                ["12 giờ", "8 giờ", "2 giờ", "4 giờ"], 1,
                "Kim dài chỉ số 12 → giờ đúng; kim ngắn (kim giờ) chỉ số 8 → **8 giờ**.",
                note="Không đọc theo kim dài: kim dài chỉ 12 không có nghĩa là 12 giờ."),
            mcq("biet", "Ngày liền sau Thứ Bảy là:", ["Thứ Sáu", "Thứ Hai", "Chủ nhật", "Thứ Bảy"], 2,
                "Thứ tự: … Thứ Sáu, Thứ Bảy, **Chủ nhật**, Thứ Hai…"),
            mcq("biet", "Trên đồng hồ, kim nào chỉ giờ?", ["Kim dài", "Kim ngắn", "Cả hai kim", "Không kim nào"], 1,
                "**Kim ngắn** chỉ giờ, kim dài chỉ phút."),
            mcq("hieu", "Hôm nay là Thứ Tư. Hôm qua là:", ["Thứ Ba", "Thứ Năm", "Thứ Hai", "Chủ nhật"], 0,
                "Hôm qua là ngày liền trước hôm nay. Liền trước Thứ Tư là **Thứ Ba**.",
                note="Thứ Năm là ngày mai, không phải hôm qua."),
            mcq("hieu", "Tờ lịch hôm nay ghi: Tháng 5 – 19 – Thứ Năm. Vậy ngày 20 tháng 5 là thứ mấy?",
                ["Thứ Tư", "Thứ Sáu", "Thứ Bảy", "Thứ Năm"], 1,
                "Ngày 20 là ngày liền sau ngày 19 (ngày mai). Liền sau Thứ Năm là **Thứ Sáu**."),
            tf("hieu", "Nhận định: “Lúc 3 giờ đúng, kim dài của đồng hồ chỉ vào số 3.”", False,
               "Lúc 3 giờ đúng: **kim dài chỉ số 12**, kim ngắn chỉ số 3. Nhận định **Sai**."),
            tf("hieu", "Nhận định: “Nếu hôm nay là Chủ nhật thì ngày mai là Thứ Hai.”", True,
               "Sau Chủ nhật là Thứ Hai của tuần mới → **Đúng**."),
            mcq("vandung", "Mai đi ngủ lúc 9 giờ tối và thức dậy lúc 6 giờ sáng. Lúc Mai thức dậy, kim ngắn của đồng hồ chỉ vào số mấy?",
                ["9", "12", "6", "3"], 2,
                "Mai thức dậy lúc 6 giờ: kim dài chỉ số 12, kim ngắn chỉ số **6**.",
                note="9 là giờ đi ngủ; câu hỏi hỏi lúc thức dậy."),
            short("vandung", "Hôm nay là Thứ Hai, ngày 10. Hỏi Thứ Hai tuần sau là ngày bao nhiêu?", ["17"],
                  "Đếm tiếp từng ngày: 11 (Thứ Ba), 12 (Thứ Tư), 13 (Thứ Năm), 14 (Thứ Sáu), 15 (Thứ Bảy), 16 (Chủ nhật), **17 (Thứ Hai)**.\nVậy Thứ Hai tuần sau là ngày **17**.",
                  alt="Một tuần có 7 ngày nên cùng thứ của tuần sau là: 10 + 7 = 17."),
        ],
    },
    # =====================================================================
    # CHỦ ĐỀ 10. ÔN TẬP CUỐI NĂM
    # =====================================================================
    {
        "topic": "l1-cd10-on-tap-cuoi-nam",
        "title": "Ôn tập cuối năm",
        "icon": "🏆",
        "description": "Chủ đề 10 · SGK Toán 1 tập hai (tr. 88–105): Bài 38 – Bài 41. Ôn tập các số và phép tính trong phạm vi 10, 100; ôn tập hình học và đo lường.",
        "requirements": [
            "Đếm, đọc, viết, so sánh, xếp thứ tự các số trong phạm vi 100; nhận biết chục và đơn vị.",
            "Thực hiện được phép cộng, phép trừ (không nhớ) trong phạm vi 100; tính nhẩm trong phạm vi 10 và với số tròn chục; tính có hai dấu phép tính.",
            "Nhận dạng được hình phẳng, hình khối đã học; vị trí, định hướng trong không gian.",
            "Đo độ dài bằng đơn vị cm, đọc giờ đúng, xem lịch tờ hằng ngày.",
            "Giải quyết được vấn đề thực tiễn đơn giản bằng phép cộng, phép trừ (bài toán có lời văn).",
        ],
        "definition": (
            "Ôn tập toàn bộ chương trình Toán 1:\n"
            "- **Số và phép tính:** số đến 100, chục – đơn vị, cộng trừ không nhớ trong phạm vi 100.\n"
            "- **Hình học:** hình vuông, hình tròn, hình tam giác, hình chữ nhật; khối lập phương, khối hộp chữ nhật.\n"
            "- **Đo lường:** xăng-ti-mét (cm), giờ đúng, ngày trong tuần, lịch."
        ),
        "theory": (
            "### Bài 38. Ôn tập các số và phép tính trong phạm vi 10\n"
            "- Đếm, so sánh, mấy và mấy; bảng cộng, bảng trừ trong phạm vi 10.\n"
            "### Bài 39. Ôn tập các số và phép tính trong phạm vi 100\n"
            "- Đọc, viết, phân tích số có hai chữ số; so sánh; cộng, trừ không nhớ; tính hai dấu phép tính; bài toán có lời văn.\n"
            "### Bài 40. Ôn tập hình học và đo lường\n"
            "- Nhận dạng hình; đo độ dài (cm); xem giờ đúng; xem lịch, các ngày trong tuần.\n"
            "### Bài 41. Ôn tập chung\n"
            "- Luyện tập tổng hợp và các bài toán thực tế."
        ),
        "formulas": [
            {"category": "I. Số và phép tính", "items": [
                {"name": "Cấu tạo số", "formula": "Số ab gồm a chục và b đơn vị (64 gồm 6 chục và 4 đơn vị)"},
                {"name": "So sánh", "formula": "So sánh hàng chục trước, hàng chục bằng nhau thì so sánh hàng đơn vị"},
                {"name": "Cộng, trừ không nhớ", "formula": "Đặt tính thẳng cột · Tính từ phải sang trái"},
                {"name": "Hai dấu phép tính", "formula": "Tính từ trái sang phải: 56 − 20 + 3 = 36 + 3 = 39"},
                {"name": "Số 0 & đổi chỗ", "formula": "a + 0 = a · a − 0 = a · a − a = 0 · a + b = b + a"},
            ]},
            {"category": "II. Hình học và đo lường", "items": [
                {"name": "Hình phẳng", "formula": "Vuông · Chữ nhật · Tam giác · Tròn"},
                {"name": "Hình khối", "formula": "Khối lập phương · Khối hộp chữ nhật"},
                {"name": "Độ dài", "formula": "Đơn vị cm · Đặt vạch 0 trùng đầu vật"},
                {"name": "Thời gian", "formula": "Giờ đúng: kim dài chỉ 12 · 1 tuần = 7 ngày"},
            ]},
        ],
        "example": "Cửa hàng có 68 quả bóng, đã bán 25 quả. Hỏi cửa hàng còn lại bao nhiêu quả bóng?",
        "example_answer": "“Đã bán” là bớt đi → phép trừ: 68 − 25.\nHàng đơn vị: 8 − 5 = 3; hàng chục: 6 − 2 = 4 → 43.\nTrả lời: Cửa hàng còn lại **43 quả bóng**.",
        "real_life": (
            "- Vận dụng tổng hợp: đếm tiền, đo đồ vật, xem giờ đi học, xem lịch nghỉ hè.\n"
            "- Chuẩn bị nền tảng vững chắc để học Toán 2."
        ),
        "quiz": [
            mcq("biet", "Số “sáu mươi tư” viết là:", ["604", "46", "64", "6"], 2,
                "Sáu mươi → 6 chục; tư → 4 đơn vị. Viết là **64**."),
            mcq("biet", "Số bé nhất trong các số 52, 25, 50, 20 là:", ["52", "25", "50", "20"], 3,
                "So sánh hàng chục: 25 và 20 có hàng chục là 2 (bé hơn 5). So sánh tiếp hàng đơn vị: 0 < 5 nên 20 < 25.\nSố bé nhất là **20**."),
            mcq("biet", "8 + 2 = ?", ["6", "10", "9", "82"], 1,
                "8 và 2 là cặp “tròn 10”: **8 + 2 = 10**."),
            mcq("biet", "Đồng hồ chỉ 10 giờ đúng khi kim dài chỉ số 12 và kim ngắn chỉ số:",
                ["12", "10", "1", "2"], 1,
                "Giờ đúng: kim ngắn chỉ số nào thì là mấy giờ → kim ngắn chỉ số **10**."),
            mcq("hieu", "56 − 20 + 3 = ?", ["39", "33", "36", "79"], 0,
                "Tính từ trái sang phải: 56 − 20 = 36; 36 + 3 = **39**.",
                note="Nếu tính 20 + 3 = 23 trước rồi lấy 56 − 23 = 33 là sai thứ tự tính."),
            mcq("hieu", "Số nào lớn hơn 68 và bé hơn 71?", ["67", "69", "72", "61"], 1,
                "Các số lớn hơn 68 và bé hơn 71 là 69 và 70. Trong các đáp án chỉ có **69**.",
                alt="Trên bảng số: 68, **69**, 70, 71 — số 69 nằm giữa 68 và 71."),
            tf("hieu", "Nhận định: “45 + 32 = 77.”", True,
               "Hàng đơn vị: 5 + 2 = 7; hàng chục: 4 + 3 = 7 → 45 + 32 = **77** → **Đúng**."),
            tf("hieu", "Nhận định: “Khối hộp chữ nhật có các mặt đều là hình tròn.”", False,
               "Các mặt của khối hộp chữ nhật là **hình chữ nhật** (có thể có mặt hình vuông), không có mặt hình tròn → **Sai**."),
            mcq("vandung", "Cửa hàng có 68 quả bóng, đã bán 25 quả. Hỏi cửa hàng còn lại bao nhiêu quả bóng?",
                ["43", "93", "33", "42"], 0,
                "“Đã bán” là bớt đi → 68 − 25: 8 − 5 = 3; 6 − 2 = 4 → **43**.\nTrả lời: Cửa hàng còn lại 43 quả bóng.",
                alt="Trừ chục trước: 68 − 20 = 48; rồi trừ đơn vị: 48 − 5 = 43.",
                note="93 là kết quả phép cộng 68 + 25 (có nhớ) — sai vì bán đi thì số bóng phải ít đi."),
            short("vandung", "Một sợi dây dài 86 cm. Bạn Hà cắt đi một đoạn dài 40 cm. Hỏi đoạn dây còn lại dài bao nhiêu xăng-ti-mét?", ["46", "46cm"],
                  "“Cắt đi” là bớt đi → 86 cm − 40 cm.\nHàng đơn vị: 6 − 0 = 6; hàng chục: 8 − 4 = 4 → **46 cm**.\nTrả lời: Đoạn dây còn lại dài 46 cm.",
                  unit="cm",
                  alt="Trừ nhẩm số tròn chục: 8 chục − 4 chục = 4 chục, giữ nguyên 6 đơn vị → 46."),
        ],
    },
]
