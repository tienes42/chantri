import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
"""
Nâng cấp toàn diện nội dung Toán lớp 1–9 (Chương trình GDPT 2018).
Tổng cộng: 54 bài học (9 lớp × 6 chuyên đề/lớp), bao gồm:
- 45 chuyên đề cốt lõi ban đầu (được làm giàu lý thuyết, công thức phân nhóm, ví dụ, câu hỏi trắc nghiệm, thử thách thực tế).
- 9 chuyên đề bổ sung mới giúp lấp đầy các mảng kiến thức quan trọng ở từng khối lớp:
  + Lớp 1: quy-luat-logic (Quy luật và Tư duy sắp xếp)
  + Lớp 2: phep-chia-hinh-khoi (Phép chia và Khối hình học)
  + Lớp 3: lam-quen-phan-so (Làm quen với Phân số & Diện tích)
  + Lớp 4: trung-binh-cong-tong-hieu (Trung bình cộng & Bài toán Tổng - Hiệu)
  + Lớp 5: ti-so-phan-tram-chuyen-dong (Tỉ số phần trăm & Toán chuyển động đều)
  + Lớp 6: so-nguyen-chia-het (Số nguyên, ƯCLN và BCNN)
  + Lớp 7: ti-le-thuc-so-thuc (Số thực, Căn bậc hai & Đại lượng tỉ lệ)
  + Lớp 8: hang-dang-thuc-phan-thuc (Hằng đẳng thức đáng nhớ, Phân thức & Định lý Thalès)
  + Lớp 9: he-thuc-viete-hinh-khong-gian (Hệ thức Viète, Bất phương trình & Hình học không gian)

Chạy từ thư mục backend:
    python upgrade_math_1_9.py
"""

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject

SUBJECT_SLUG = "math"
SUBJECT_NAME = "Toán"


def format_formulas_text(formulas_structured):
    """Tạo chuỗi tóm tắt công thức từ cấu trúc danh mục để tương thích ngược với trường `formula`."""
    if not formulas_structured:
        return ""
    lines = []
    for group in formulas_structured:
        if isinstance(group, str):
            lines.append(group)
            continue
        cat = group.get("category")
        if cat:
            lines.append(f"• {cat}:")
        for item in group.get("items", []):
            name = item.get("name", "")
            f_str = item.get("formula", "")
            note = item.get("note", "")
            line = f"  - {name}: {f_str}" if name else f"  - {f_str}"
            if note:
                line += f" ({note})"
            lines.append(line)
    return "\n".join(lines)


def M(
    grade,
    topic,
    title,
    icon,
    description,
    definition,
    concept,
    formulas,
    meaning,
    real_life,
    example,
    example_answer,
    question,
    answers,
    correct,
    challenge,
    challenge_answer,
    game_title=None,
    game_description=None,
    game_type="simulation",
):
    return {
        "grade": grade,
        "topic": topic,
        "title": title,
        "icon": icon,
        "description": description,
        "definition": definition.strip(),
        "concept": concept.strip(),
        "formulas": formulas,
        "meaning": meaning.strip(),
        "real_life": real_life.strip(),
        "context_title": f"Ứng dụng thực tế: {title}",
        "context": real_life.strip(),
        "theory": f"{definition.strip()}\n\n{concept.strip()}",
        "formula": format_formulas_text(formulas),
        "example": example.strip(),
        "example_answer": example_answer.strip(),
        "question": question.strip(),
        "answers": answers,
        "correct": correct,
        "application": meaning.strip(),
        "challenge": challenge.strip(),
        "challenge_answer": challenge_answer.strip(),
        "game_title": game_title or f"Thử thách tương tác: {title}",
        "game_description": game_description
        or f"Vận dụng kiến thức {title.lower()} để giải quyết tình huống thực tế.",
        "game_type": game_type,
    }


LESSONS = [
    # =========================================================
    # LỚP 1 (6 BÀI)
    # =========================================================
    M(
        1,
        "so-hoc",
        "Số tự nhiên trong phạm vi 100",
        "🔢",
        "Nhận biết, đọc, viết, so sánh và tách - gộp các số tự nhiên từ 0 đến 100.",
        "Số tự nhiên dùng để đếm số lượng đồ vật và biểu thị thứ tự. Ở lớp 1, học sinh làm quen với các số từ 0 đến 100, hiểu cấu tạo số gồm hàng chục và hàng đơn vị.",
        "• Đếm, đọc và viết các số từ 0 đến 100.\n"
        "• Phân tích cấu tạo số có hai chữ số: chục và đơn vị (ví dụ: 35 gồm 3 chục và 5 đơn vị).\n"
        "• Nhận biết số liền trước, số liền sau và tia số.\n"
        "• So sánh hai số bằng các dấu >, <, = và sắp xếp dãy số theo thứ tự tăng/giảm dần.",
        [
            {
                "category": "I. Cấu tạo số & Thứ tự trên tia số",
                "items": [
                    {"name": "Số liền trước của n", "formula": "n - 1 (với n ≥ 1)", "note": "Đứng ngay bên trái n trên tia số"},
                    {"name": "Số liền sau của n", "formula": "n + 1", "note": "Đứng ngay bên phải n trên tia số"},
                    {"name": "Cấu tạo số có 2 chữ số", "formula": "ab = a chục + b đơn vị = 10 × a + b", "note": "1 ≤ a ≤ 9; 0 ≤ b ≤ 9"},
                ],
            },
            {
                "category": "II. Quy tắc so sánh hai số",
                "items": [
                    {"name": "Khác số chữ số", "formula": "Số có nhiều chữ số hơn thì lớn hơn", "note": "Ví dụ: 10 > 9, 100 > 99"},
                    {"name": "Cùng có hai chữ số", "formula": "So sánh chữ số hàng chục trước, nếu bằng nhau thì so sánh hàng đơn vị", "note": "Ví dụ: 47 > 39; 45 < 48"},
                ],
            },
        ],
        "Giúp học sinh hình thành cảm nhận về số lượng, cấu trúc hệ thập phân và thứ tự trong cuộc sống.",
        "Đếm số bút màu trong hộp, đọc số nhà, số trang sách, xem số thứ tự khi xếp hàng hoặc đếm tiền mệnh giá nhỏ.",
        "Số gồm 4 chục và 6 đơn vị được viết là số nào? Tìm số liền trước và số liền sau của số đó.",
        "Số đó là 46. Số liền trước của 46 là 45; số liền sau của 46 là 47.",
        "Trong các số 29, 51, 18, 45, số lớn nhất là số nào?",
        ["29", "51", "18", "45"],
        1,
        "Trên kệ có 3 hộp bánh, mỗi hộp 10 chiếc và thêm 7 chiếc bánh lẻ bên ngoài. Hỏi có tất cả bao nhiêu chiếc bánh?",
        "3 hộp là 3 chục (30 chiếc), thêm 7 chiếc lẻ là 37 chiếc bánh.",
    ),
    M(
        1,
        "phep-cong",
        "Phép cộng trong phạm vi 100 (không nhớ)",
        "➕",
        "Hiểu ý nghĩa gộp lại của phép cộng và thực hiện cộng không nhớ trong phạm vi 100.",
        "Phép cộng là phép toán dùng để gộp hai hay nhiều nhóm đồ vật lại với nhau nhằm tìm tổng số lượng.",
        "• Nhận biết dấu cộng (+), các số hạng và tổng.\n"
        "• Thuộc bảng cộng trong phạm vi 10.\n"
        "• Đặt tính và tính phép cộng số có hai chữ số với số có một hoặc hai chữ số (không nhớ): viết thẳng cột hàng đơn vị với hàng đơn vị, hàng chục với hàng chục, cộng từ phải sang trái.",
        [
            {
                "category": "I. Cấu trúc & Tính chất phép cộng",
                "items": [
                    {"name": "Thành phần phép cộng", "formula": "Số hạng + Số hạng = Tổng (a + b = c)", "note": "Kết quả gọi là Tổng"},
                    {"name": "Tính chất giao hoán", "formula": "a + b = b + a", "note": "Đổi chỗ hai số hạng thì tổng không đổi"},
                    {"name": "Cộng với số 0", "formula": "a + 0 = 0 + a = a", "note": "Số nào cộng với 0 cũng bằng chính nó"},
                ],
            },
            {
                "category": "II. Quy tắc cộng số có hai chữ số (không nhớ)",
                "items": [
                    {"name": "Cộng theo cột dọc", "formula": "(a chục + b đơn vị) + (c chục + d đơn vị) = (a + c) chục + (b + d) đơn vị", "note": "Với b + d < 10 và a + c < 10"},
                ],
            },
        ],
        "Phép cộng mô tả sự thêm vào, gộp chung và tích lũy số lượng.",
        "Tính tổng số kẹo của hai bạn, tổng số học sinh nam và nữ trong tổ, hoặc tổng giá tiền khi mua hai món đồ.",
        "Đặt tính rồi tính: 34 + 25.",
        "Cộng hàng đơn vị: 4 + 5 = 9. Cộng hàng chục: 3 + 2 = 5. Kết quả: 34 + 25 = 59.",
        "Kết quả của phép tính 42 + 36 là bao nhiêu?",
        ["68", "76", "78", "88"],
        2,
        "Lan có 23 nhãn vở, mẹ cho Lan thêm 15 nhãn vở nữa. Hỏi Lan có tất cả bao nhiêu nhãn vở?",
        "Lan có tất cả: 23 + 15 = 38 (nhãn vở).",
    ),
    M(
        1,
        "phep-tru",
        "Phép trừ trong phạm vi 100 (không nhớ)",
        "➖",
        "Hiểu ý nghĩa bớt đi của phép trừ và thực hiện trừ không nhớ trong phạm vi 100.",
        "Phép trừ là phép toán dùng để lấy bớt một phần khỏi nhóm ban đầu nhằm tìm số lượng còn lại hoặc phần chênh lệch.",
        "• Nhận biết dấu trừ (−), số bị trừ, số trừ và hiệu.\n"
        "• Thuộc bảng trừ trong phạm vi 10.\n"
        "• Đặt tính và tính phép trừ trong phạm vi 100 (không nhớ) theo cột dọc từ hàng đơn vị sang hàng chục.\n"
        "• Hiểu mối quan hệ ngược nhau giữa phép cộng và phép trừ.",
        [
            {
                "category": "I. Cấu trúc & Tính chất phép trừ",
                "items": [
                    {"name": "Thành phần phép trừ", "formula": "Số bị trừ − Số trừ = Hiệu (a − b = c)", "note": "Với a ≥ b"},
                    {"name": "Trừ đi 0 và trừ chính nó", "formula": "a − 0 = a ; a − a = 0", "note": "Tính chất cơ bản"},
                    {"name": "Quan hệ với phép cộng", "formula": "Nếu a + b = c thì c − a = b và c − b = a", "note": "Dùng để thử lại kết quả"},
                ],
            },
            {
                "category": "II. Quy tắc trừ không nhớ",
                "items": [
                    {"name": "Trừ theo hàng", "formula": "Trừ hàng đơn vị trước, trừ hàng chục sau", "note": "Viết các chữ số cùng hàng thẳng cột"},
                ],
            },
        ],
        "Phép trừ giúp xác định phần còn lại sau khi đã dùng, đã cho hoặc tìm phần chênh lệch giữa hai nhóm.",
        "Tính số tiền còn lại sau khi mua bánh, số quả bóng còn lại trên sân hoặc số trang sách chưa đọc.",
        "Tính: 68 − 23.",
        "Hàng đơn vị: 8 − 3 = 5. Hàng chục: 6 − 2 = 4. Vậy 68 − 23 = 45.",
        "Phép tính 89 − 34 có kết quả bằng bao nhiêu?",
        ["45", "55", "53", "65"],
        1,
        "Một đàn gà có 47 con, trong đó có 22 con gà trống. Hỏi đàn gà có bao nhiêu con gà mái?",
        "Số gà mái là: 47 − 22 = 25 (con).",
    ),
    M(
        1,
        "do-luong",
        "Đo độ dài và Thời gian",
        "📏",
        "Làm quen với đơn vị đo độ dài xăng-ti-mét (cm), cách dùng thước kẻ và xem đồng hồ giờ đúng.",
        "Đo lường là sử dụng dụng cụ và đơn vị chuẩn để xác định độ dài của vật hoặc thời điểm, khoảng thời gian trong ngày.",
        "• Nhận biết đơn vị đo độ dài xăng-ti-mét (viết tắt là cm).\n"
        "• Cách đo độ dài đoạn thẳng bằng thước thẳng: đặt vạch số 0 trùng với một đầu đoạn thẳng, mép thước sát đoạn thẳng, đọc số ở đầu kia.\n"
        "• Xem đồng hồ khi kim dài chỉ số 12 (giờ đúng) và đọc lịch các ngày trong tuần.",
        [
            {
                "category": "I. Đo độ dài",
                "items": [
                    {"name": "Đơn vị xăng-ti-mét", "formula": "Ký hiệu: cm", "note": "Dùng đo các vật nhỏ như bút chì, quyển vở"},
                    {"name": "Cộng/trừ số đo độ dài", "formula": "a cm + b cm = (a + b) cm", "note": "Giữ nguyên tên đơn vị ở kết quả"},
                ],
            },
            {
                "category": "II. Thời gian & Lịch",
                "items": [
                    {"name": "Đồng hồ giờ đúng", "formula": "Kim phút (dài) chỉ số 12, kim giờ (ngắn) chỉ số k ⇒ k giờ", "note": "Ví dụ: kim ngắn chỉ số 8, kim dài chỉ số 12 là 8 giờ"},
                    {"name": "Số ngày trong tuần", "formula": "1 tuần lễ = 7 ngày", "note": "Từ Thứ Hai đến Chủ Nhật"},
                ],
            },
        ],
        "Giúp học sinh mô tả chính xác kích thước đồ vật và rèn thói quen sinh hoạt đúng giờ.",
        "Đo chiều dài chiếc bút chì, đo gang tay, xem giờ đi học buổi sáng và xem lịch học hàng tuần.",
        "Một băng giấy màu xanh dài 12 cm, băng giấy màu đỏ dài 7 cm. Nếu nối hai băng giấy sát nhau (không chồng lên nhau) thì dài bao nhiêu xăng-ti-mét?",
        "Tổng chiều dài là: 12 cm + 7 cm = 19 cm.",
        "Khi đồng hồ chỉ 9 giờ đúng, kim dài và kim ngắn chỉ vào những số nào?",
        ["Kim ngắn chỉ 12, kim dài chỉ 9", "Kim ngắn chỉ 9, kim dài chỉ 12", "Cả hai kim chỉ số 9", "Kim ngắn chỉ 9, kim dài chỉ 6"],
        1,
        "Hôm nay là Thứ Năm ngày 10. Hỏi 3 ngày nữa là Thứ Mấy, ngày bao nhiêu?",
        "Ngày 10 + 3 = ngày 13; Thứ Năm đếm thêm 3 ngày là Chủ Nhật (ngày 13).",
    ),
    M(
        1,
        "hinh-hoc",
        "Hình phẳng và Khối hình cơ bản",
        "🔺",
        "Nhận dạng hình vuông, hình tròn, hình tam giác, hình chữ nhật và khối lập phương, khối hộp chữ nhật.",
        "Hình học lớp 1 giúp học sinh nhận biết các hình phẳng và khối hình học trong không gian cùng các quan hệ vị trí.",
        "• Hình phẳng: Hình vuông, hình chữ nhật, hình tam giác, hình tròn.\n"
        "• Hình khối: Khối lập phương (giống rubik, xúc xắc) và khối hộp chữ nhật (giống hộp sữa, viên gạch).\n"
        "• Xác định vị trí định hướng trong không gian: trên - dưới, phải - trái, trước - sau, ở giữa.",
        [
            {
                "category": "I. Đặc điểm nhận dạng hình phẳng",
                "items": [
                    {"name": "Hình tam giác", "formula": "Có 3 cạnh thẳng và 3 đỉnh (3 góc)", "note": "Ví dụ: biển báo giao thông hình tam giác"},
                    {"name": "Hình vuông", "formula": "Có 4 cạnh thẳng bằng nhau và 4 góc vuông", "note": "Ví dụ: viên gạch lát nền"},
                    {"name": "Hình chữ nhật", "formula": "Có 4 góc vuông, 2 cạnh dài bằng nhau và 2 cạnh ngắn bằng nhau", "note": "Ví dụ: mặt bàn, quyển sách"},
                    {"name": "Hình tròn", "formula": "Đường cong khép kín, không có góc và cạnh thẳng", "note": "Ví dụ: mặt đồng hồ tròn, đĩa CD"},
                ],
            },
            {
                "category": "II. Đặc điểm hình khối",
                "items": [
                    {"name": "Khối lập phương", "formula": "Có 6 mặt đều là hình vuông bằng nhau", "note": "8 đỉnh, 12 cạnh bằng nhau"},
                    {"name": "Khối hộp chữ nhật", "formula": "Có 6 mặt đều là hình chữ nhật", "note": "8 đỉnh, 12 cạnh"},
                ],
            },
        ],
        "Phát triển trí tưởng tượng không gian và khả năng quan sát thế giới xung quanh.",
        "Nhận biết biển báo giao thông, lắp ghép mô hình từ các khối gỗ hoặc xếp hình Tangram.",
        "Dùng 2 hình tam giác vuông cân bằng nhau ghép sát cạnh dài nhất lại với nhau, ta được hình gì?",
        "Ta ghép được một hình vuông.",
        "Đồ vật nào dưới đây có dạng khối lập phương?",
        ["Quả bóng đá", "Viên xúc xắc (con súc sắc)", "Lon nước ngọt", "Chiếc đĩa tròn"],
        1,
        "Một hình vuông lớn được ghép bởi 4 hình vuông nhỏ bằng nhau (xếp thành 2 hàng, mỗi hàng 2 hình). Hỏi trên hình vẽ có tất cả bao nhiêu hình vuông?",
        "Có 4 hình vuông nhỏ và 1 hình vuông lớn bao ngoài, tổng cộng là 5 hình vuông.",
    ),
    M(
        1,
        "quy-luat-logic",
        "Quy luật, Dãy hình và Toán thực tế",
        "🧩",
        "Khám phá quy luật lặp lại của hình ảnh, màu sắc, dãy số và giải bài toán có lời văn đơn giản.",
        "Quy luật là trật tự lặp đi lặp lại hoặc tăng/giảm cố định của một dãy số, dãy hình hoặc sự vật.",
        "• Nhận biết quy luật xen kẽ hoặc lặp lại theo chu kỳ của dãy hình, màu sắc.\n"
        "• Tìm số còn thiếu trong dãy số đếm thêm 1, đếm thêm 2, đếm thêm 5, đếm thêm 10.\n"
        "• Phân tích bài toán có lời văn: xác định 'Bài toán cho biết gì?', 'Bài toán hỏi gì?', chọn phép tính '+' hoặc '−' và viết câu trả lời.",
        [
            {
                "category": "I. Quy luật dãy số cơ bản",
                "items": [
                    {"name": "Dãy số cách đều d đơn vị", "formula": "Số sau = Số trước + d (hoặc Số trước − d)", "note": "Ví dụ: 2, 4, 6, 8, 10 (cộng thêm 2)"},
                    {"name": "Dãy lặp theo chu kỳ", "formula": "(A - B - C) - (A - B - C) - ...", "note": "Xác định cụm lặp lại để đoán phần tử tiếp theo"},
                ],
            },
            {
                "category": "II. Từ khóa giải toán có lời văn",
                "items": [
                    {"name": "Bài toán gộp / thêm", "formula": "Từ khóa: 'thêm', 'tất cả', 'cả hai', 'gộp lại' ⇒ Dùng phép cộng (+)", "note": "Kiểm tra đơn vị bài toán"},
                    {"name": "Bài toán bớt / còn lại", "formula": "Từ khóa: 'bớt đi', 'bay đi', 'cho đi', 'còn lại' ⇒ Dùng phép trừ (−)", "note": "Số bị trừ luôn lớn hơn hoặc bằng số trừ"},
                ],
            },
        ],
        "Rèn luyện tư duy phát hiện quy luật (pattern recognition) và kỹ năng đọc hiểu, giải quyết vấn đề.",
        "Xếp hàng trang trí cờ màu xen kẽ, đếm bước nhảy cách đều và tính toán khi đi siêu thị cùng bố mẹ.",
        "Tìm số tiếp theo trong dãy số: 10, 20, 30, 40, ...",
        "Dãy số tăng thêm 10 đơn vị ở mỗi bước (đếm theo chục). Số tiếp theo là 50.",
        "Quan sát dãy hình: 🔺 🔵 🟢 🔺 🔵 🟢 🔺 ... Hình tiếp theo là hình gì?",
        ["🔺", "🔵", "🟢", "⬜"],
        1,
        "Trong hàng xếp tập thể dục, An đứng thứ 4 tính từ đầu hàng và đứng thứ 3 tính từ cuối hàng. Hỏi hàng của An có tất cả bao nhiêu bạn?",
        "Trước An có 3 bạn, sau An có 2 bạn, cộng thêm chính An là: 3 + 2 + 1 = 6 (bạn).",
    ),

    # =========================================================
    # LỚP 2 (6 BÀI)
    # =========================================================
    M(
        2,
        "so-hoc",
        "Số tự nhiên đến 1000 & Cấu tạo thập phân",
        "🔢",
        "Đọc, viết, so sánh và phân tích các số có ba chữ số theo hàng trăm, chục, đơn vị.",
        "Ở lớp 2, tập hợp số tự nhiên mở rộng đến 1000, giúp biểu diễn các số lượng lớn hơn thông qua ba hàng: trăm, chục, đơn vị.",
        "• Đếm theo trăm, chục, đơn vị; đọc và viết các số trong phạm vi 1000.\n"
        "• Phân tích số có ba chữ số thành tổng các trăm, chục, đơn vị.\n"
        "• Nhận biết số tròn chục, số tròn trăm, số chẵn và số lẻ.\n"
        "• So sánh các số có ba chữ số.",
        [
            {
                "category": "I. Cấu tạo thập phân của số có 3 chữ số",
                "items": [
                    {"name": "Quan hệ giữa các hàng", "formula": "1 nghìn = 10 trăm ; 1 trăm = 10 chục ; 1 chục = 10 đơn vị", "note": "Mỗi hàng gấp 10 lần hàng liền kề bên phải"},
                    {"name": "Khai triển số abc", "formula": "abc = a × 100 + b × 10 + c", "note": "a là chữ số hàng trăm (a ≠ 0), b hàng chục, c hàng đơn vị"},
                ],
            },
            {
                "category": "II. Số chẵn, số lẻ & Số đặc biệt",
                "items": [
                    {"name": "Số chẵn", "formula": "Tận cùng là 0, 2, 4, 6, 8", "note": "Chia thành 2 phần bằng nhau không dư"},
                    {"name": "Số lẻ", "formula": "Tận cùng là 1, 3, 5, 7, 9", "note": "Không chia đôi chẵn được"},
                    {"name": "Số lớn nhất / nhỏ nhất", "formula": "Số có 3 chữ số nhỏ nhất: 100 ; lớn nhất: 999", "note": "Nếu 3 chữ số khác nhau: nhỏ nhất 102, lớn nhất 987"},
                ],
            },
        ],
        "Giúp học sinh hiểu sâu quy tắc hệ thập phân và tự tin xử lý các con số đến hàng nghìn.",
        "Đọc giá tiền, số kilomet trên cột mốc đường bộ, số báo danh hoặc số lượng sách trong thư viện.",
        "Viết số gồm 5 trăm, 0 chục và 8 đơn vị, sau đó viết số đó thành tổng các trăm, chục, đơn vị.",
        "Số đó là 508. Viết thành tổng: 508 = 500 + 8.",
        "Số lớn nhất có ba chữ số khác nhau là số nào?",
        ["999", "987", "998", "900"],
        1,
        "Từ ba thẻ số 2, 0, 7, em có thể ghép được bao nhiêu số có ba chữ số khác nhau? Hãy liệt kê các số đó.",
        "Chữ số hàng trăm không thể bằng 0, nên lập được 4 số: 207, 270, 702, 720.",
    ),
    M(
        2,
        "phep-cong",
        "Phép cộng có nhớ trong phạm vi 100 & 1000",
        "➕",
        "Thực hiện thành thạo phép cộng qua 10 và phép cộng có nhớ trong phạm vi 100, 1000.",
        "Phép cộng có nhớ xảy ra khi tổng các chữ số ở một hàng bằng hoặc vượt quá 10, ta phải gộp 10 đơn vị ở hàng đó thành 1 đơn vị ở hàng liền kề bên trái.",
        "• Bảng cộng qua 10 (trong phạm vi 20) bằng phương pháp 'gộp cho đủ chục rồi cộng với số còn lại'.\n"
        "• Đặt tính và tính cộng có nhớ trong phạm vi 100 và 1000.\n"
        "• Giải bài toán về 'nhiều hơn' một số đơn vị.",
        [
            {
                "category": "I. Phương pháp cộng qua 10",
                "items": [
                    {"name": "Tách số để凑 (gộp) tròn chục", "formula": "9 + a = 9 + (1 + (a − 1)) = 10 + (a − 1)", "note": "Ví dụ: 8 + 5 = 8 + 2 + 3 = 10 + 3 = 13"},
                ],
            },
            {
                "category": "II. Quy tắc cộng có nhớ & Bài toán 'Nhiều hơn'",
                "items": [
                    {"name": "Quy tắc nhớ sang hàng kế tiếp", "formula": "Nếu tổng hàng đơn vị = 10 + r ⇒ viết r, nhớ 1 sang hàng chục", "note": "Luôn cộng thêm 1 đã nhớ vào hàng tiếp theo"},
                    {"name": "Bài toán 'Nhiều hơn'", "formula": "Số lớn = Số bé + Phần nhiều hơn", "note": "Ví dụ: Có 15 bông hoa, thêm/nhiều hơn 7 bông ⇒ 15 + 7"},
                ],
            },
        ],
        "Giúp tính tổng nhanh, chính xác khi các đại lượng vượt qua mốc tròn chục, tròn trăm.",
        "Tính tổng số điểm qua các vòng thi, tổng số cây trồng của hai lớp hoặc tổng số tiền tiết kiệm.",
        "Tính 47 + 38 và giải thích cách nhớ.",
        "Hàng đơn vị: 7 + 8 = 15, viết 5 nhớ 1. Hàng chục: 4 + 3 = 7, thêm 1 bằng 8, viết 8. Vậy 47 + 38 = 85.",
        "Kết quả của phép tính 265 + 128 là bao nhiêu?",
        ["383", "393", "395", "493"],
        1,
        "Tổ Một trồng được 36 cây hoa, Tổ Hai trồng được nhiều hơn Tổ Một 17 cây hoa. Hỏi Tổ Hai trồng được bao nhiêu cây hoa?",
        "Số cây hoa Tổ Hai trồng được là: 36 + 17 = 53 (cây).",
    ),
    M(
        2,
        "phep-tru",
        "Phép trừ có nhớ & Tìm thành phần chưa biết",
        "➖",
        "Thực hiện phép trừ qua 10, trừ có nhớ và giải bài toán 'ít hơn'.",
        "Phép trừ có nhớ xảy ra khi chữ số ở một hàng của số bị trừ nhỏ hơn chữ số cùng hàng của số trừ, ta phải mượn 1 chục (10 đơn vị) từ hàng liền kề bên trái.",
        "• Bảng trừ qua 10 (trong phạm vi 20) bằng cách 'trừ để về 10 rồi trừ tiếp'.\n"
        "• Đặt tính và tính trừ có nhớ trong phạm vi 100 và 1000.\n"
        "• Giải bài toán về 'ít hơn' và tìm số hạng, số bị trừ, số trừ chưa biết.",
        [
            {
                "category": "I. Quy tắc trừ có nhớ",
                "items": [
                    {"name": "Trừ qua 10", "formula": "13 − 5 = (13 − 3) − 2 = 10 − 2 = 8", "note": "Tách số trừ để đưa về số tròn chục 10"},
                    {"name": "Quy tắc mượn 1 chục", "formula": "Khi chữ số hàng đơn vị a < b: lấy (10 + a) − b, rồi nhớ trả 1 vào hàng chục", "note": "Không quên trừ đi 1 ở hàng chục của số bị trừ"},
                ],
            },
            {
                "category": "II. Tìm thành phần chưa biết & Bài toán 'Ít hơn'",
                "items": [
                    {"name": "Tìm số hạng chưa biết", "formula": "Số hạng = Tổng − Số hạng kia (x + b = c ⇒ x = c − b)", "note": ""},
                    {"name": "Tìm số bị trừ / số trừ", "formula": "Số bị trừ = Hiệu + Số trừ ; Số trừ = Số bị trừ − Hiệu", "note": ""},
                    {"name": "Bài toán 'Ít hơn'", "formula": "Số bé = Số lớn − Phần ít hơn", "note": ""},
                ],
            },
        ],
        "Giúp tính toán chính xác phần chênh lệch, tiền thừa và tìm lại số lượng ban đầu.",
        "Tính tiền trả lại khi mua hàng bằng tờ tiền mệnh giá lớn, so sánh chiều cao hoặc cân nặng giữa hai bạn.",
        "Đặt tính rồi tính: 72 − 28.",
        "2 không trừ được 8, lấy 12 − 8 = 4, viết 4 nhớ 1. Hàng chục: 2 thêm 1 bằng 3, 7 − 3 = 4, viết 4. Vậy 72 − 28 = 44.",
        "Tìm x, biết: x − 27 = 45.",
        ["x = 18", "x = 62", "x = 72", "x = 74"],
        2,
        "Bao gạo tẻ nặng 50 kg, bao gạo nếp nhẹ hơn bao gạo tẻ 14 kg. Hỏi cả hai bao gạo nặng bao nhiêu ki-lô-gam?",
        "Bao gạo nếp nặng: 50 − 14 = 36 (kg). Cả hai bao nặng: 50 + 36 = 86 (kg).",
    ),
    M(
        2,
        "phep-nhan",
        "Phép nhân – Bảng nhân 2 và 5",
        "✖️",
        "Hiểu phép nhân là tổng của các số hạng bằng nhau; thuộc và vận dụng bảng nhân 2, bảng nhân 5.",
        "Phép nhân là phép toán viết gọn của phép cộng nhiều số hạng bằng nhau.",
        "• Nhận biết các thành phần của phép nhân: Thừa số × Thừa số = Tích.\n"
        "• Chuyển đổi giữa tổng các số hạng bằng nhau và phép nhân.\n"
        "• Lập và học thuộc lòng bảng nhân 2, bảng nhân 5 để giải bài toán thực tế.",
        [
            {
                "category": "I. Bản chất và Thành phần phép nhân",
                "items": [
                    {"name": "Định nghĩa qua phép cộng", "formula": "a × n = a + a + ... + a (có n số hạng a)", "note": "Đọc là: a được lấy n lần"},
                    {"name": "Thành phần phép nhân", "formula": "Thừa số × Thừa số = Tích", "note": ""},
                    {"name": "Tính chất cơ bản", "formula": "a × b = b × a ; a × 1 = 1 × a = a ; a × 0 = 0 × a = 0", "note": "Mọi số nhân với 0 đều bằng 0"},
                ],
            },
            {
                "category": "II. Bảng nhân 2 và Bảng nhân 5",
                "items": [
                    {"name": "Bảng nhân 2", "formula": "2 × 1 = 2, 2 × 2 = 4, ..., 2 × 10 = 20", "note": "Các tích là dãy số chẵn tăng thêm 2"},
                    {"name": "Bảng nhân 5", "formula": "5 × 1 = 5, 5 × 2 = 10, ..., 5 × 10 = 50", "note": "Các tích luôn tận cùng bằng 0 hoặc 5"},
                ],
            },
        ],
        "Giúp tính nhanh tổng số lượng khi các nhóm đều có số phần tử bằng nhau mà không cần cộng lặp lại nhiều lần.",
        "Đếm số chiếc đũa theo đôi (nhân 2), đếm số ngón tay trên các bàn tay (nhân 5), tính tổng số ghế trong các hàng.",
        "Viết tổng 5 + 5 + 5 + 5 + 5 + 5 thành phép nhân và tính kết quả.",
        "Số 5 được lấy 6 lần nên ta viết: 5 × 6 = 30.",
        "Mỗi bàn học có 2 học sinh ngồi. Hỏi 8 bàn học như thế có tất cả bao nhiêu học sinh?",
        ["10 học sinh", "14 học sinh", "16 học sinh", "18 học sinh"],
        2,
        "Mỗi tuần lễ em đi học 5 ngày (từ Thứ Hai đến Thứ Sáu). Hỏi trong 4 tuần lễ liên tiếp, em đi học tất cả bao nhiêu ngày?",
        "Số ngày đi học trong 4 tuần là: 5 × 4 = 20 (ngày).",
    ),
    M(
        2,
        "dai-luong",
        "Đơn vị đo Độ dài, Khối lượng, Dung tích & Thời gian",
        "⚖️",
        "Sử dụng các đơn vị dm, m, km, kg, lít (l) và xem đồng hồ đến 15 phút, 30 phút.",
        "Đại lượng đo lường lớp 2 mở rộng sang đo độ dài lớn (dm, m, km), khối lượng (kg), dung tích chất lỏng (lít) và thời gian chi tiết hơn.",
        "• Độ dài: Đề-xi-mét (dm), mét (m), ki-lô-mét (km) và quy tắc quy đổi.\n"
        "• Khối lượng: Ki-lô-gam (kg) – dùng cân đĩa, cân đồng hồ.\n"
        "• Dung tích: Lít (l) – đo lượng nước, sữa, dầu ăn.\n"
        "• Thời gian: Ngày - giờ, giờ - phút (xem đồng hồ khi kim phút chỉ số 3 là 15 phút, chỉ số 6 là 30 phút hay rưỡi).",
        [
            {
                "category": "I. Quy đổi đơn vị độ dài",
                "items": [
                    {"name": "Đề-xi-mét và Mét", "formula": "1 dm = 10 cm ; 1 m = 10 dm = 100 cm", "note": ""},
                    {"name": "Ki-lô-mét", "formula": "1 km = 1000 m", "note": "Dùng đo quãng đường dài giữa các địa điểm"},
                ],
            },
            {
                "category": "II. Khối lượng, Dung tích & Thời gian",
                "items": [
                    {"name": "Khối lượng & Dung tích", "formula": "Đơn vị khối lượng: kg ; Đơn vị dung tích: lít (l)", "note": "Cộng/trừ cùng đơn vị đo"},
                    {"name": "Thời gian", "formula": "1 ngày = 24 giờ ; 1 giờ = 60 phút", "note": "Kim phút chỉ số 3: 15 phút; chỉ số 6: 30 phút (rưỡi)"},
                ],
            },
        ],
        "Giúp học sinh định lượng chính xác độ dài, sức nặng, thể tích chất lỏng và quản lý thời gian hàng ngày.",
        "Đo chiều cao cơ thể, cân hoa quả ở chợ, đong nước vào bình và xem lịch trình tàu xe.",
        "Điền số thích hợp: 3 m = ... dm = ... cm.",
        "3 m = 30 dm = 300 cm.",
        "Khi kim ngắn nằm giữa số 7 và số 8, kim dài chỉ đúng số 6 thì đồng hồ chỉ mấy giờ?",
        ["7 giờ 6 phút", "7 giờ 15 phút", "7 giờ 30 phút (7 giờ rưỡi)", "8 giờ 30 phút"],
        2,
        "Một can dầu chứa 20 lít dầu. Người ta rót đầy vào 3 chai nhỏ, mỗi chai 5 lít. Hỏi trong can còn lại bao nhiêu lít dầu?",
        "Số dầu đã rót ra 3 chai là: 5 × 3 = 15 (lít). Số dầu còn lại trong can là: 20 − 15 = 5 (lít).",
    ),
    M(
        2,
        "phep-chia-hinh-khoi",
        "Phép chia (Bảng chia 2, 5) & Hình học (Đường gấp khúc, Khối trụ - cầu)",
        "➗",
        "Hiểu ý nghĩa phép chia đều, thuộc bảng chia 2, 5; tính độ dài đường gấp khúc và nhận biết khối trụ, khối cầu.",
        "Phép chia là phép toán ngược của phép nhân, dùng để chia một nhóm thành các phần bằng nhau hoặc chia theo từng nhóm có số lượng bằng nhau.",
        "• Thành phần phép chia: Số bị chia : Số chia = Thương.\n"
        "• Lập và thuộc bảng chia 2, bảng chia 5 từ bảng nhân tương ứng.\n"
        "• Nhận biết đường thẳng, đường cong, ba điểm thẳng hàng, đường gấp khúc, hình tứ giác.\n"
        "• Nhận dạng khối trụ (lon sữa, khúc gỗ tròn) và khối cầu (quả bóng, viên bi).",
        [
            {
                "category": "I. Phép chia và Quan hệ Nhân - Chia",
                "items": [
                    {"name": "Thành phần phép chia", "formula": "Số bị chia : Số chia = Thương (a : b = c)", "note": "Số chia b ≠ 0"},
                    {"name": "Quan hệ với phép nhân", "formula": "Từ a × b = c ⇒ c : a = b và c : b = a", "note": "Một phép nhân cho hai phép chia tương ứng"},
                ],
            },
            {
                "category": "II. Đường gấp khúc & Hình khối",
                "items": [
                    {"name": "Độ dài đường gấp khúc", "formula": "L = a + b + c + ... (Tổng độ dài các đoạn thẳng thành phần)", "note": "Các đoạn thẳng phải cùng đơn vị đo"},
                    {"name": "Khối trụ & Khối cầu", "formula": "Khối trụ có 2 đáy hình tròn bằng nhau; Khối cầu lăn được về mọi phía", "note": ""},
                ],
            },
        ],
        "Giúp chia đều phần thưởng, tính tổng quãng đường gồm nhiều chặng gấp khúc và phân biệt các vật thể 3D.",
        "Chia đều bánh cho các bạn, đo quãng đường đi qua nhiều ngã rẽ và nhận diện đồ vật hình trụ, hình cầu.",
        "Một đường gấp khúc ABCD gồm ba đoạn thẳng có độ dài lần lượt là AB = 12 cm, BC = 15 cm, CD = 23 cm. Tính độ dài đường gấp khúc đó.",
        "Độ dài đường gấp khúc ABCD là: 12 + 15 + 23 = 50 (cm).",
        "Có 35 quyển vở chia đều cho 5 bạn học sinh giỏi. Hỏi mỗi bạn nhận được bao nhiêu quyển vở?",
        ["5 quyển", "6 quyển", "7 quyển", "8 quyển"],
        2,
        "Một sợi dây dài 40 dm được cắt thành các đoạn bằng nhau, mỗi đoạn dài 5 dm. Hỏi cắt được mấy đoạn dây và phải dùng kéo cắt mấy lần?",
        "Số đoạn dây cắt được là: 40 : 5 = 8 (đoạn). Để cắt thành 8 đoạn thì chỉ cần cắt: 8 − 1 = 7 (lần).",
    ),

    # =========================================================
    # LỚP 3 (6 BÀI)
    # =========================================================
    M(
        3,
        "so-tu-nhien",
        "Số tự nhiên đến 100 000 & Làm tròn số",
        "🔢",
        "Đọc, viết, so sánh số trong phạm vi 100 000, làm quen chữ số La Mã và quy tắc làm tròn số.",
        "Ở lớp 3, học sinh mở rộng phạm vi số tự nhiên lên đến hàng chục nghìn (100 000), nắm vững cấu tạo thập phân, chữ số La Mã từ I đến XX và cách làm tròn số.",
        "• Các hàng: đơn vị, chục, trăm, nghìn, chục nghìn, trăm nghìn.\n"
        "• Nhận biết và đọc viết các chữ số La Mã phổ biến (I, V, X, XI, XII, ..., XX) trên mặt đồng hồ.\n"
        "• Quy tắc làm tròn số đến hàng chục, hàng trăm, hàng nghìn, hàng chục nghìn để ước lượng nhanh.",
        [
            {
                "category": "I. Cấu tạo số & Chữ số La Mã",
                "items": [
                    {"name": "Khai triển số 5 chữ số", "formula": "abcde = a×10000 + b×1000 + c×100 + d×10 + e", "note": "a ≠ 0"},
                    {"name": "Ký hiệu La Mã cơ bản", "formula": "I = 1, V = 5, X = 10 ; IV = 4, VI = 6, IX = 9, XI = 11", "note": "Viết trái là trừ, viết phải là cộng"},
                ],
            },
            {
                "category": "II. Quy tắc làm tròn số",
                "items": [
                    {"name": "Làm tròn xuống", "formula": "Nếu chữ số ngay sau hàng làm tròn là 0, 1, 2, 3, 4 ⇒ giữ nguyên chữ số hàng làm tròn", "note": "Các chữ số bên phải thay bằng 0"},
                    {"name": "Làm tròn lên", "formula": "Nếu chữ số ngay sau hàng làm tròn là 5, 6, 7, 8, 9 ⇒ cộng thêm 1 vào hàng làm tròn", "note": "Các chữ số bên phải thay bằng 0"},
                ],
            },
        ],
        "Giúp đọc hiểu các số liệu dân số, giá tiền hàng chục nghìn đồng và ước lượng nhanh kết quả tính toán.",
        "Ước lượng số tiền cần mang khi đi mua sắm, đọc năm xây dựng công trình hoặc số trên mặt đồng hồ La Mã.",
        "Làm tròn số 34 628 đến hàng nghìn và đến hàng trăm.",
        "Làm tròn đến hàng nghìn (xét chữ số hàng trăm là 6 ≥ 5): được 35 000. Làm tròn đến hàng trăm (xét chữ số hàng chục là 2 < 5): được 34 600.",
        "Số 48 350 làm tròn đến hàng nghìn thì được số nào?",
        ["48 000", "48 300", "48 400", "49 000"],
        0,
        "Một chiếc áo có giá 86 000 đồng, một chiếc quần có giá 93 000 đồng. Hãy làm tròn giá tiền mỗi món đến hàng chục nghìn để ước lượng xem mang theo 200 000 đồng có đủ mua cả hai món không?",
        "86 000 làm tròn thành 90 000; 93 000 làm tròn thành 90 000. Tổng ước lượng khoảng 180 000 đồng < 200 000 đồng nên chắc chắn đủ tiền mua.",
    ),
    M(
        3,
        "phep-nhan",
        "Bảng nhân 2–9 & Nhân số có nhiều chữ số với số có một chữ số",
        "✖️",
        "Thuộc hoàn chỉnh bảng nhân từ 2 đến 9, nhân số có nhiều chữ số và tính giá trị biểu thức.",
        "Phép nhân lớp 3 hoàn thiện toàn bộ bảng nhân từ 2 đến 9 và mở rộng sang nhân đặt tính cột dọc với các số có đến 4–5 chữ số.",
        "• Hoàn thiện bảng nhân 2, 3, 4, 5, 6, 7, 8, 9.\n"
        "• Nhân số có 2, 3, 4, 5 chữ số với số có 1 chữ số (không nhớ và có nhớ).\n"
        "• Bài toán 'Gấp một số lên một số lần'.\n"
        "• Tính chất giao hoán, kết hợp của phép nhân và nhân một số với một tổng.",
        [
            {
                "category": "I. Tính chất của phép nhân",
                "items": [
                    {"name": "Giao hoán & Kết hợp", "formula": "a × b = b × a ; (a × b) × c = a × (b × c)", "note": "Dùng để nhóm các số có tích tròn chục, tròn trăm"},
                    {"name": "Phân phối đối với phép cộng", "formula": "a × (b + c) = a × b + a × c", "note": "Cơ sở của phép nhân đặt tính theo hàng"},
                ],
            },
            {
                "category": "II. Bài toán gấp một số lên nhiều lần",
                "items": [
                    {"name": "Gấp số a lên k lần", "formula": "Giá trị mới = a × k", "note": "Phân biệt với 'thêm k đơn vị' là a + k"},
                ],
            },
        ],
        "Giúp tính toán nhanh sản lượng, tiền hàng số lượng lớn và giải bài toán có nhiều bước tính.",
        "Tính tổng tiền mua nhiều quyển sách cùng giá, tổng trọng lượng các thùng hàng trên xe tải.",
        "Đặt tính rồi tính: 1 218 × 4.",
        "4 × 8 = 32 viết 2 nhớ 3; 4 × 1 = 4 thêm 3 là 7; 4 × 2 = 8; 4 × 1 = 4. Kết quả: 1 218 × 4 = 4 872.",
        "Kết quả của biểu thức 150 + 25 × 4 là bao nhiêu?",
        ["700", "250", "200", "625"],
        1,
        "Một nông trại thu hoạch được 1 350 kg cam. Số ki-lô-gam quýt thu hoạch được gấp 3 lần số cam. Hỏi nông trại thu hoạch được tất cả bao nhiêu ki-lô-gam cả cam và quýt?",
        "Số quýt là: 1 350 × 3 = 4 050 (kg). Tổng số cam và quýt là: 1 350 + 4 050 = 5 400 (kg).",
    ),
    M(
        3,
        "phep-chia",
        "Bảng chia 2–9, Phép chia có dư & Thứ tự thực hiện phép tính",
        "➗",
        "Thực hiện phép chia hết, phép chia có dư và nắm vững quy tắc tính giá trị biểu thức.",
        "Phép chia số tự nhiên a cho b (b ≠ 0) luôn tìm được thương q và số dư r sao cho a = b × q + r với 0 ≤ r < b.",
        "• Thuộc bảng chia từ 2 đến 9.\n"
        "• Chia số có nhiều chữ số cho số có một chữ số (chia từ trái sang phải).\n"
        "• Hiểu điều kiện bắt buộc của phép chia có dư: Số dư luôn nhỏ hơn số chia.\n"
        "• Bài toán 'Giảm một số đi một số lần' và quy tắc thứ tự thực hiện phép tính.",
        [
            {
                "category": "I. Phép chia hết và Phép chia có dư",
                "items": [
                    {"name": "Công thức tổng quát", "formula": "a = b × q + r (với 0 ≤ r < b)", "note": "a: số bị chia, b: số chia, q: thương, r: số dư"},
                    {"name": "Số dư lớn nhất có thể", "formula": "r_max = b − 1", "note": "Nếu r = 0 thì đó là phép chia hết"},
                    {"name": "Giảm số a đi k lần", "formula": "Giá trị mới = a : k", "note": "Phân biệt với 'giảm đi k đơn vị' là a − k"},
                ],
            },
            {
                "category": "II. Thứ tự thực hiện phép tính trong biểu thức",
                "items": [
                    {"name": "Chỉ có (+, −) hoặc chỉ có (×, :)", "formula": "Thực hiện lần lượt từ trái sang phải", "note": ""},
                    {"name": "Có cả (+, −, ×, :)", "formula": "Thực hiện Nhân, Chia trước; Cộng, Trừ sau", "note": ""},
                    {"name": "Có dấu ngoặc ( )", "formula": "Thực hiện trong ngoặc ( ) trước, ngoài ngoặc sau", "note": ""},
                ],
            },
        ],
        "Giúp giải quyết các bài toán đóng gói hàng hóa, phân bổ phương tiện khi có phần lẻ còn dư.",
        "Tính số chuyến đò cần chở hết đoàn khách, đóng gói bánh vào hộp và chia phần thưởng.",
        "Thực hiện phép chia 47 : 5 và kiểm tra lại kết quả.",
        "47 : 5 = 9 (dư 2). Kiểm tra: 5 × 9 + 2 = 45 + 2 = 47 (và số dư 2 < 5).",
        "Trong một phép chia có số chia là 7, thương là 12 và số dư là số dư lớn nhất có thể. Số bị chia là bao nhiêu?",
        ["84", "85", "90", "91"],
        2,
        "Một đoàn khách du lịch có 38 người muốn qua sông. Mỗi chiếc thuyền chỉ chở được tối đa 6 khách (không kể người lái thuyền). Hỏi cần ít nhất bao nhiêu chiếc thuyền để chở hết đoàn khách cùng một lúc?",
        "Ta có 38 : 6 = 6 (dư 2 người). 2 người còn dư vẫn cần thêm 1 chiếc thuyền nữa. Vậy cần ít nhất: 6 + 1 = 7 (chiếc thuyền).",
    ),
    M(
        3,
        "hinh-hoc",
        "Hình học phẳng: Trung điểm, Hình tròn, Chu vi & Diện tích",
        "📐",
        "Nhận biết góc vuông, trung điểm đoạn thẳng, tâm - bán kính - đường kính hình tròn và tính chu vi, diện tích hình chữ nhật, hình vuông.",
        "Hình học lớp 3 cung cấp các khái niệm đo lường không gian cốt lõi: trung điểm, tâm và bán kính đường tròn, cùng công thức tính chu vi và diện tích.",
        "• Điểm ở giữa và Trung điểm của đoạn thẳng.\n"
        "• Góc vuông, góc không vuông (kiểm tra bằng ê-ke).\n"
        "• Hình tròn: Tâm O, bán kính R, đường kính d = 2R (dùng com-pa để vẽ).\n"
        "• Công thức tính Chu vi và Diện tích của hình chữ nhật, hình vuông.",
        [
            {
                "category": "I. Trung điểm & Hình tròn",
                "items": [
                    {"name": "Trung điểm M của đoạn AB", "formula": "M nằm giữa A, B và MA = MB = AB : 2", "note": "M chia đoạn AB thành 2 phần bằng nhau"},
                    {"name": "Đường kính & Bán kính", "formula": "d = 2 × R  ⇔  R = d : 2", "note": "Tâm O là trung điểm của mọi đường kính"},
                ],
            },
            {
                "category": "II. Chu vi và Diện tích (Cùng đơn vị đo)",
                "items": [
                    {"name": "Hình chữ nhật (dài a, rộng b)", "formula": "Chu vi: P = (a + b) × 2  ;  Diện tích: S = a × b", "note": "Nửa chu vi: a + b = P : 2"},
                    {"name": "Hình vuông (cạnh a)", "formula": "Chu vi: P = a × 4  ;  Diện tích: S = a × a", "note": "Cạnh hình vuông: a = P : 4"},
                ],
            },
        ],
        "Giúp tính toán kích thước hàng rào, khung tranh, diện tích lát gạch nền nhà hoặc diện tích mảnh vườn.",
        "Tính số viên gạch cần lát phòng học, độ dài ruy-băng viền quanh thiệp hoặc bán kính bồn hoa tròn.",
        "Một mảnh vườn hình chữ nhật có chiều dài 15 m, chiều rộng 8 m. Tính chu vi và diện tích mảnh vườn đó.",
        "Chu vi mảnh vườn: (15 + 8) × 2 = 46 (m). Diện tích mảnh vườn: 15 × 8 = 120 (m²).",
        "Một hình vuông có chu vi bằng 36 cm. Diện tích của hình vuông đó là bao nhiêu?",
        ["36 cm²", "64 cm²", "81 cm²", "144 cm²"],
        2,
        "Một sân bóng mini hình chữ nhật có chiều rộng 12 m, chiều dài gấp đôi chiều rộng. Người ta làm hàng rào bao quanh sân, chừa ra lối cửa đi rộng 3 m. Tính chiều dài hàng rào cần làm.",
        "Chiều dài sân: 12 × 2 = 24 (m). Chu vi sân: (24 + 12) × 2 = 72 (m). Chiều dài hàng rào trừ cửa: 72 − 3 = 69 (m).",
    ),
    M(
        3,
        "du-lieu",
        "Thống kê số liệu & Khả năng xảy ra của sự kiện",
        "📊",
        "Thu thập, phân loại, đọc bảng thống kê số liệu, biểu đồ tranh và nhận biết khả năng xảy ra của một sự kiện.",
        "Thống kê và xác suất sơ cấp giúp học sinh biết cách đọc thông tin từ bảng biểu và đánh giá xem một sự kiện 'chắc chắn', 'có thể' hay 'không thể' xảy ra.",
        "• Kiểm đếm và ghi chép số liệu bằng vạch kiểm đếm.\n"
        "• Đọc và phân tích bảng số liệu thống kê, biểu đồ tranh.\n"
        "• Đánh giá khả năng xảy ra của một sự kiện: 'Chắc chắn xảy ra', 'Có thể xảy ra', 'Không thể xảy ra'.",
        [
            {
                "category": "I. Xử lý bảng số liệu & Biểu đồ tranh",
                "items": [
                    {"name": "Tổng số liệu", "formula": "Tổng = x₁ + x₂ + ... + xₙ", "note": "Cộng tất cả các nhóm đối tượng"},
                    {"name": "Độ chênh lệch", "formula": "Hiệu = Giá trị lớn nhất − Giá trị nhỏ nhất", "note": "So sánh nhiều hơn / ít hơn"},
                    {"name": "Giá trị biểu đồ tranh", "formula": "Số lượng = Số biểu tượng × Giá trị 1 biểu tượng", "note": "Chú ý đọc kỹ phần chú giải"},
                ],
            },
            {
                "category": "II. Nhận biết khả năng xảy ra",
                "items": [
                    {"name": "Chắc chắn / Có thể / Không thể", "formula": "Chắc chắn (luôn đúng) ; Có thể (đôi khi xảy ra) ; Không thể (không bao giờ xảy ra)", "note": ""},
                ],
            },
        ],
        "Giúp rèn kỹ năng đọc bảng biểu thông tin và dự đoán hợp lý các tình huống trong đời sống.",
        "Đọc bảng điểm thi đua của lớp, thống kê số sách quyên góp và dự đoán kết quả trò chơi rút thăm.",
        "Trong hộp kín có 4 quả bóng màu đỏ và 1 quả bóng màu xanh. Không nhìn vào hộp, lấy ngẫu nhiên 1 quả bóng. Khả năng lấy được bóng màu vàng là gì?",
        "Vì trong hộp không có quả bóng màu vàng nào nên sự kiện 'lấy được bóng màu vàng' là KHÔNG THỂ xảy ra.",
        "Trên biểu đồ tranh, mỗi hình 🍎 biểu thị 5 quả táo. Nếu giỏ của Mai có 6 hình 🍎 thì giỏ của Mai có thật sự bao nhiêu quả táo?",
        ["6 quả", "11 quả", "25 quả", "30 quả"],
        3,
        "Lớp 3A khảo sát môn thể thao yêu thích: Bóng đá có 16 bạn, Cầu lông có 12 bạn, Bơi lội có 9 bạn (mỗi bạn chỉ chọn 1 môn). Hỏi lớp 3A có tất cả bao nhiêu học sinh tham gia khảo sát và môn nhiều nhất hơn môn ít nhất bao nhiêu bạn?",
        "Tổng số học sinh: 16 + 12 + 9 = 37 (bạn). Môn nhiều nhất (Bóng đá) hơn môn ít nhất (Bơi lội): 16 − 9 = 7 (bạn).",
    ),
    M(
        3,
        "lam-quen-phan-so",
        "Làm quen với Phân số (Một phần mấy) & Đơn vị đo lường mở rộng",
        "🍕",
        "Nhận biết một phần hai đến một phần chín (1/2 đến 1/9) và sử dụng các đơn vị mm, g, ml, nhiệt độ (°C).",
        "Khi chia một hình hay một nhóm đồ vật thành n phần bằng nhau (n từ 2 đến 9), mỗi phần được gọi là 'một phần n', viết là 1/n.",
        "• Nhận biết và đọc viết các phân số dạng 1/2, 1/3, 1/4, ..., 1/9.\n"
        "• Tìm một trong các phần bằng nhau của một số (lấy số đó chia cho số phần).\n"
        "• Các đơn vị đo lường chi tiết: mi-li-mét (mm), gam (g), mi-li-lít (ml) và độ C (°C).",
        [
            {
                "category": "I. Tìm một trong các phần bằng nhau của một số",
                "items": [
                    {"name": "Giá trị của 1/n của số A", "formula": "Giá trị 1 phần = A : n", "note": "Ví dụ: 1/4 của 20 chiếc bánh là 20 : 4 = 5 chiếc"},
                ],
            },
            {
                "category": "II. Hệ thống đơn vị đo mở rộng lớp 3",
                "items": [
                    {"name": "Độ dài (mm)", "formula": "1 cm = 10 mm ; 1 dm = 100 mm ; 1 m = 1000 mm", "note": "Đo bề dày đồng xu, quyển sách"},
                    {"name": "Khối lượng (g) & Dung tích (ml)", "formula": "1 kg = 1000 g ; 1 lít (l) = 1000 ml", "note": "Đo gia vị, thuốc uống, sữa hộp"},
                    {"name": "Diện tích (cm²)", "formula": "Xăng-ti-mét vuông (cm²) là diện tích hình vuông cạnh 1 cm", "note": ""},
                ],
            },
        ],
        "Giúp học sinh biết chia phần công bằng và đo đạc chính xác đến từng mi-li-mét, gam, mi-li-lít.",
        "Chia bánh sinh nhật, đong si-rô thuốc bằng cốc chia vạch ml, cân bột làm bánh bằng gam.",
        "Mẹ mua 24 quả trứng, mẹ dùng 1/3 số trứng để làm bánh. Hỏi mẹ đã dùng bao nhiêu quả trứng và còn lại bao nhiêu quả?",
        "Mẹ đã dùng: 24 : 3 = 8 (quả trứng). Số trứng còn lại là: 24 − 8 = 16 (quả trứng).",
        "Một chai sữa tươi có dung tích 1 lít. Sau khi rót ra cốc 350 ml, trong chai còn lại bao nhiêu mi-li-lít sữa?",
        ["550 ml", "650 ml", "750 ml", "349 ml"],
        1,
        "Một sợi dây ruy-băng dài 3 m 6 dm. Bạn Hà cắt lấy 1/4 sợi dây để gói quà. Hỏi đoạn dây bạn Hà cắt ra dài bao nhiêu đề-xi-mét?",
        "Đổi 3 m 6 dm = 36 dm. Độ dài đoạn dây cắt ra là: 36 : 4 = 9 (dm).",
    ),

    # =========================================================
    # LỚP 4 (6 BÀI)
    # =========================================================
    M(
        4,
        "so-tu-nhien",
        "Số tự nhiên đến lớp triệu & Bốn phép tính với số lớn",
        "🔢",
        "Đọc, viết số đến hàng trăm triệu, nắm vững cấu trúc lớp - hàng và thực hiện cộng, trừ, nhân, chia với số có nhiều chữ số.",
        "Ở lớp 4, hệ thống số tự nhiên mở rộng đến lớp triệu (và lớp tỉ), các hàng được nhóm thành từng lớp 3 chữ số từ phải sang trái.",
        "• Lớp đơn vị (đơn vị, chục, trăm), Lớp nghìn (nghìn, chục nghìn, trăm nghìn), Lớp triệu (triệu, chục triệu, trăm triệu).\n"
        "• Cộng, trừ các số có nhiều chữ số; tính chất giao hoán và kết hợp.\n"
        "• Nhân và chia với số có hai, ba chữ số; nhân/chia nhẩm với 10, 100, 1000.\n"
        "• Dấu hiệu chia hết cho 2, 5, 9, 3.",
        [
            {
                "category": "I. Cấu trúc Lớp & Dấu hiệu chia hết",
                "items": [
                    {"name": "Chia hết cho 2 ; cho 5", "formula": "Chia hết cho 2: tận cùng 0,2,4,6,8 ; Chia hết cho 5: tận cùng 0 hoặc 5", "note": "Chia hết cho cả 2 và 5: tận cùng là 0"},
                    {"name": "Chia hết cho 9 ; cho 3", "formula": "Tổng các chữ số chia hết cho 9 (hoặc cho 3) thì số đó chia hết cho 9 (hoặc cho 3)", "note": "Ví dụ: 459 có 4+5+9=18 chia hết cho 9"},
                ],
            },
            {
                "category": "II. Tính chất Đại số của Phép cộng & Phép nhân",
                "items": [
                    {"name": "Nhân một số với một tổng / hiệu", "formula": "a × (b ± c) = a × b ± a × c", "note": "Áp dụng tính nhanh cực hiệu quả"},
                    {"name": "Nhân/chia nhẩm với 10, 100, 1000", "formula": "Nhân với 10ⁿ: thêm n chữ số 0 vào bên phải", "note": "Chia số tròn chục/trăm cho 10ⁿ: bớt n chữ số 0"},
                ],
            },
        ],
        "Tạo nền tảng tính toán vững chắc với các con số quy mô lớn trong kinh tế, địa lý và dân số.",
        "Đọc ngân sách dự án, dân số các tỉnh thành, diện tích quốc gia và tính toán hóa đơn lớn.",
        "Tính bằng cách thuận tiện nhất: 248 × 64 + 248 × 36.",
        "Áp dụng tính chất phân phối: 248 × 64 + 248 × 36 = 248 × (64 + 36) = 248 × 100 = 24 800.",
        "Số nào dưới đây chia hết cho cả 2, 3, 5 và 9?",
        ["1 350", "2 345", "4 052", "1 230"],
        0,
        "Tìm chữ số x và y để số 25xy chia hết cho cả 2, 5 và 9.",
        "Để 25xy chia hết cho cả 2 và 5 thì chữ số tận cùng y = 0. Khi đó tổng các chữ số là 2 + 5 + x + 0 = 7 + x. Để chia hết cho 9 thì 7 + x = 9 ⇒ x = 2. Số cần tìm là 2520.",
    ),
    M(
        4,
        "phan-so",
        "Phân số và Các phép tính với phân số",
        "🍰",
        "Hiểu bản chất phân số là thương của phép chia, rút gọn, quy đồng và thực hiện cộng, trừ, nhân, chia phân số.",
        "Phân số a/b (với a, b là số tự nhiên, b ≠ 0) gồm tử số a và mẫu số b, biểu thị thương của phép chia a : b.",
        "• Tính chất cơ bản của phân số, rút gọn phân số về phân số tối giản và quy đồng mẫu số.\n"
        "• So sánh hai phân số cùng mẫu, khác mẫu hoặc cùng tử số.\n"
        "• Thực hiện 4 phép tính cộng, trừ, nhân, chia phân số.\n"
        "• Bài toán: Tìm phân số của một số.",
        [
            {
                "category": "I. Tính chất cơ bản & So sánh phân số",
                "items": [
                    {"name": "Phân số bằng nhau", "formula": "a/b = (a × m)/(b × m) = (a : n)/(b : n)", "note": "m, n là số tự nhiên khác 0"},
                    {"name": "So sánh với 1", "formula": "a < b ⇔ a/b < 1 ; a = b ⇔ a/b = 1 ; a > b ⇔ a/b > 1", "note": ""},
                ],
            },
            {
                "category": "II. Bốn phép tính với phân số & Ứng dụng",
                "items": [
                    {"name": "Cộng, trừ phân số", "formula": "Cùng mẫu: a/m ± b/m = (a ± b)/m ; Khác mẫu: quy đồng rồi cộng/trừ tử số", "note": "Giữ nguyên mẫu số chung"},
                    {"name": "Nhân, chia phân số", "formula": "a/b × c/d = (a × c)/(b × d) ; a/b : c/d = a/b × d/c", "note": "Chia là nhân với phân số đảo ngược (c ≠ 0)"},
                    {"name": "Tìm phân số a/b của số M", "formula": "Giá trị = M × (a/b) = (M : b) × a", "note": ""},
                ],
            },
        ],
        "Giúp biểu diễn và tính toán chính xác mọi phần lẻ của đại lượng mà số tự nhiên không biểu diễn được.",
        "Chia phần diện tích đất canh tác, pha chế công thức nấu ăn, tính thời gian làm việc theo phần giờ.",
        "Tính: 3/4 + 5/6 và rút gọn kết quả.",
        "Mẫu số chung là 12: 3/4 + 5/6 = 9/12 + 10/12 = 19/12.",
        "Một lớp học có 35 học sinh, trong đó số học sinh nữ chiếm 3/5 số học sinh cả lớp. Hỏi lớp đó có bao nhiêu học sinh nam?",
        ["14 học sinh", "21 học sinh", "15 học sinh", "20 học sinh"],
        0,
        "Một tấm vải dài 45 m. Lần thứ nhất người ta cắt lấy 1/3 tấm vải, lần thứ hai cắt lấy 2/5 phần vải còn lại. Hỏi sau hai lần cắt, tấm vải còn lại bao nhiêu mét?",
        "Lần 1 cắt: 45 × 1/3 = 15 (m), còn lại 45 − 15 = 30 (m). Lần 2 cắt: 30 × 2/5 = 12 (m). Sau 2 lần cắt còn lại: 30 − 12 = 18 (m).",
    ),
    M(
        4,
        "hinh-hoc",
        "Góc, Hai đường thẳng vuông góc - song song, Hình bình hành & Hình thoi",
        "📐",
        "Nhận biết góc nhọn, góc tù, góc bẹt, đo góc bằng thước đo góc và tính chất hình bình hành, hình thoi.",
        "Hình học lớp 4 mở rộng sang số đo góc (đơn vị độ °), quan hệ vuông góc - song song và hai tứ giác đặc biệt là hình bình hành, hình thoi.",
        "• Góc nhọn (< 90°), góc vuông (= 90°), góc tù (> 90° và < 180°), góc bẹt (= 180°).\n"
        "• Hai đường thẳng vuông góc và hai đường thẳng song song.\n"
        "• Hình bình hành: có hai cặp cạnh đối diện song song và bằng nhau.\n"
        "• Hình thoi: có hai cặp cạnh đối diện song song và bốn cạnh bằng nhau.",
        [
            {
                "category": "I. Phân loại Góc theo số đo",
                "items": [
                    {"name": "Góc nhọn, vuông, tù, bẹt", "formula": "Góc nhọn < 90° ; Góc vuông = 90° ; 90° < Góc tù < 180° ; Góc bẹt = 180°", "note": "Góc bẹt bằng 2 góc vuông"},
                ],
            },
            {
                "category": "II. Hình bình hành & Hình thoi",
                "items": [
                    {"name": "Hình bình hành (đáy a, cạnh bên b, cao h)", "formula": "Chu vi: P = (a + b) × 2  ;  Diện tích: S = a × h", "note": "a và h cùng đơn vị đo"},
                    {"name": "Hình thoi (cạnh a, hai đường chéo m, n)", "formula": "Chu vi: P = a × 4  ;  Diện tích: S = (m × n) : 2", "note": "Hai đường chéo hình thoi vuông góc với nhau"},
                ],
            },
        ],
        "Giúp đo đạc góc nghiêng, thiết kế hoa văn trang trí, khung cửa và tính diện tích các mảnh đất hình bình hành, hình thoi.",
        "Thiết kế họa tiết gạch bông hình thoi, bậc cầu thang song song, đo góc nghiêng mái nhà.",
        "Một bồn hoa hình thoi có độ dài hai đường chéo lần lượt là 6 m và 4 m. Tính diện tích bồn hoa đó.",
        "Diện tích bồn hoa hình thoi là: (6 × 4) : 2 = 12 (m²).",
        "Khẳng định nào dưới đây là ĐÚNG về hình thoi?",
        [
            "Hình thoi có 4 góc đều là góc vuông",
            "Hình thoi có hai cặp cạnh đối diện song song và 4 cạnh bằng nhau",
            "Hình thoi chỉ có một cặp cạnh song song",
            "Hai đường chéo của hình thoi luôn bằng nhau",
        ],
        1,
        "Một mảnh đất hình bình hành có độ dài đáy là 28 m, chiều cao bằng 3/4 độ dài đáy. Trên mảnh đất đó người ta trồng rau, cứ mỗi mét vuông thu hoạch được 3 kg rau. Tính tổng khối lượng rau thu hoạch được.",
        "Chiều cao mảnh đất: 28 × 3/4 = 21 (m). Diện tích mảnh đất: 28 × 21 = 588 (m²). Số rau thu hoạch được: 588 × 3 = 1 764 (kg).",
    ),
    M(
        4,
        "dai-luong",
        "Đơn vị Khối lượng (Yến, Tạ, Tấn), Diện tích (dm², m², mm²) & Thời gian (Giây, Thế kỷ)",
        "⚖️",
        "Chuyển đổi thành thạo các bảng đơn vị đo khối lượng, diện tích và thời gian lớn.",
        "Các đại lượng đo lường ở lớp 4 hoàn thiện hệ thống đơn vị khối lượng lớn (yến, tạ, tấn), diện tích (mm², cm², dm², m²) và thời gian (giây, thế kỷ).",
        "• Khối lượng: Tấn, tạ, yến, kg, g.\n"
        "• Diện tích: m², dm², cm², mm² (hai đơn vị diện tích liền kề hơn kém nhau 100 lần).\n"
        "• Thời gian: Giây, phút, giờ, ngày, năm, thế kỷ (1 thế kỷ = 100 năm) và cách xác định một năm thuộc thế kỷ thứ mấy.",
        [
            {
                "category": "I. Bảng quy đổi Khối lượng & Diện tích",
                "items": [
                    {"name": "Khối lượng lớn", "formula": "1 tấn = 10 tạ = 100 yến = 1000 kg ; 1 tạ = 10 yến = 100 kg ; 1 yến = 10 kg", "note": "Mỗi đơn vị liền kề gấp/kém 10 lần"},
                    {"name": "Đơn vị diện tích", "formula": "1 m² = 100 dm² = 10 000 cm² ; 1 dm² = 100 cm² ; 1 cm² = 100 mm²", "note": "Mỗi đơn vị diện tích liền kề gấp/kém 100 lần"},
                ],
            },
            {
                "category": "II. Đơn vị Thời gian & Quy tắc tính Thế kỷ",
                "items": [
                    {"name": "Giây và Thế kỷ", "formula": "1 phút = 60 giây ; 1 giờ = 3600 giây ; 1 thế kỷ = 100 năm", "note": "Năm nhuận có 366 ngày (tháng 2 có 29 ngày)"},
                    {"name": "Cách xác định thế kỷ", "formula": "Năm tròn trăm (ab00) thuộc thế kỷ ab ; Năm abcd (cd ≠ 00) thuộc thế kỷ (ab + 1)", "note": "Ví dụ: năm 1945 thuộc thế kỷ 20 (XX); năm 2000 thuộc thế kỷ 20; năm 2026 thuộc thế kỷ 21 (XXI)"},
                ],
            },
        ],
        "Giúp quy đổi chính xác tải trọng hàng hóa, diện tích căn hộ và các mốc lịch sử theo thế kỷ.",
        "Tính tải trọng xe tải chở nông sản (tấn, tạ), diện tích căn phòng (m²) và xác định thế kỷ của các sự kiện lịch sử.",
        "Điền số thích hợp: a) 4 tấn 5 tạ = ... kg ; b) 7 m² 8 dm² = ... dm².",
        "a) 4 tấn 5 tạ = 4000 kg + 500 kg = 4500 kg. b) 7 m² 8 dm² = 700 dm² + 8 dm² = 708 dm².",
        "Bác Hồ đọc Bản Tuyên ngôn Độc lập khai sinh nước Việt Nam Dân chủ Cộng hòa vào ngày 2 tháng 9 năm 1945. Năm đó thuộc thế kỷ thứ mấy?",
        ["Thế kỷ XVIII (18)", "Thế kỷ XIX (19)", "Thế kỷ XX (20)", "Thế kỷ XXI (21)"],
        2,
        "Một căn phòng hình chữ nhật có chiều dài 8 m, chiều rộng 5 m. Người ta dùng các viên gạch hình vuông cạnh 4 dm để lát kín nền phòng (không tính mạch vữa). Hỏi cần bao nhiêu viên gạch?",
        "Diện tích nền phòng: 8 × 5 = 40 (m²) = 4000 (dm²). Diện tích 1 viên gạch: 4 × 4 = 16 (dm²). Số viên gạch cần dùng: 4000 : 16 = 250 (viên).",
    ),
    M(
        4,
        "bieu-do",
        "Biểu đồ cột & Kiểm đếm xác suất thực nghiệm",
        "📊",
        "Đọc, phân tích dữ liệu trên biểu đồ cột và thực hành kiểm đếm số lần lặp lại của một sự kiện.",
        "Biểu đồ cột sử dụng chiều cao của các cột chữ nhật để biểu diễn trực quan độ lớn của các số liệu thống kê.",
        "• Cấu tạo biểu đồ cột: Tên biểu đồ, trục ngang (tên các đối tượng), trục đứng (số liệu) và độ cao các cột.\n"
        "• So sánh xu hướng tăng/giảm, tìm giá trị lớn nhất, nhỏ nhất, tổng và trung bình cộng từ biểu đồ.\n"
        "• Ghi lại kết quả nhiều lần thực nghiệm (tung đồng xu, xúc xắc) để đếm số lần xuất hiện của một sự kiện.",
        [
            {
                "category": "I. Khai thác thông tin từ Biểu đồ cột",
                "items": [
                    {"name": "Tổng giá trị các cột", "formula": "S = h₁ + h₂ + ... + hₙ", "note": "Cộng số liệu ghi trên đỉnh các cột"},
                    {"name": "Trung bình cộng các cột", "formula": "TB = (h₁ + h₂ + ... + hₙ) : n", "note": "n là số cột được xét"},
                ],
            },
            {
                "category": "II. Kiểm đếm số lần xuất hiện của sự kiện",
                "items": [
                    {"name": "Tỉ số lần xuất hiện", "formula": "Số lần sự kiện A xảy ra / Tổng số lần thực hiện phép thử", "note": "Làm quen với thống kê thực nghiệm"},
                ],
            },
        ],
        "Giúp đọc hiểu nhanh các báo cáo số liệu về lượng mưa, sản lượng, doanh thu trên báo chí và thực tế.",
        "Phân tích biểu đồ lượng mưa các tháng, biểu đồ số sách mượn tại thư viện trường.",
        "Biểu đồ số cây trồng của 4 khối lớp cho biết: Khối 1 trồng 30 cây, Khối 2 trồng 40 cây, Khối 3 trồng 45 cây, Khối 4 trồng 65 cây. Hỏi trung bình mỗi khối trồng được bao nhiêu cây?",
        "Trung bình mỗi khối trồng được: (30 + 40 + 45 + 65) : 4 = 180 : 4 = 45 (cây).",
        "Nam tung một đồng xu 20 lần liên tiếp, trong đó có 11 lần xuất hiện mặt Sấp (S). Hỏi có bao nhiêu lần xuất hiện mặt Ngửa (N)?",
        ["8 lần", "9 lần", "10 lần", "11 lần"],
        1,
        "Số lượng học sinh giỏi của 3 lớp 4A, 4B, 4C trên biểu đồ cột lần lượt là 18 bạn, 22 bạn và một cột bị mờ số của lớp 4C. Biết trung bình mỗi lớp có 21 học sinh giỏi. Hãy tìm số học sinh giỏi của lớp 4C.",
        "Tổng số học sinh giỏi của 3 lớp là: 21 × 3 = 63 (bạn). Số học sinh giỏi của lớp 4C là: 63 − (18 + 22) = 23 (bạn).",
    ),
    M(
        4,
        "trung-binh-cong-tong-hieu",
        "Số trung bình cộng & Bài toán Tìm hai số khi biết Tổng và Hiệu",
        "🧮",
        "Nắm vững công thức tìm số trung bình cộng, bài toán rút về đơn vị và bài toán tìm hai số khi biết tổng và hiệu.",
        "Đây là các dạng toán có lời văn trọng tâm bậc tiểu học, giúp học sinh tìm giá trị đại diện và giải hệ hai đại lượng qua sơ đồ đoạn thẳng.",
        "• Số trung bình cộng của nhiều số bằng tổng các số đó chia cho số các số hạng.\n"
        "• Bài toán tìm hai số khi biết Tổng và Hiệu của hai số đó.\n"
        "• Bài toán liên quan đến rút về đơn vị.",
        [
            {
                "category": "I. Số trung bình cộng",
                "items": [
                    {"name": "Công thức trung bình cộng", "formula": "TBC = (a₁ + a₂ + ... + aₙ) : n", "note": "n là số các số hạng"},
                    {"name": "Tìm tổng khi biết TBC", "formula": "Tổng = TBC × n", "note": "Dùng khi tìm một số hạng còn thiếu"},
                ],
            },
            {
                "category": "II. Tìm hai số khi biết Tổng (S) và Hiệu (D)",
                "items": [
                    {"name": "Cách 1: Tìm Số bé trước", "formula": "Số bé = (Tổng − Hiệu) : 2  ;  Số lớn = Số bé + Hiệu", "note": "Tổng và Hiệu phải cùng chẵn hoặc cùng lẻ (với số tự nhiên)"},
                    {"name": "Cách 2: Tìm Số lớn trước", "formula": "Số lớn = (Tổng + Hiệu) : 2  ;  Số bé = Tổng − Số lớn", "note": ""},
                ],
            },
        ],
        "Giúp tính mức tiêu thụ trung bình hàng tháng và phân chia số lượng khi biết tổng và độ chênh lệch.",
        "Tính điểm trung bình, chiều cao trung bình của đội bóng, tính tuổi của bố và con, hoặc chiều dài và chiều rộng mảnh đất khi biết chu vi.",
        "Hai lớp 4A và 4B có tất cả 72 học sinh. Lớp 4A có nhiều hơn lớp 4B là 4 học sinh. Tính số học sinh của mỗi lớp.",
        "Số học sinh lớp 4A (số lớn): (72 + 4) : 2 = 38 (học sinh). Số học sinh lớp 4B (số bé): 72 − 38 = 34 (học sinh).",
        "Trung bình cộng của ba số là 40. Biết hai trong ba số đó là 32 và 45. Số thứ ba là bao nhiêu?",
        ["38", "43", "45", "53"],
        1,
        "Một mảnh vườn hình chữ nhật có chu vi là 120 m, chiều dài hơn chiều rộng 16 m. Tính diện tích mảnh vườn đó.",
        "Nửa chu vi (tổng chiều dài và chiều rộng) là: 120 : 2 = 60 (m). Chiều dài: (60 + 16) : 2 = 38 (m). Chiều rộng: 60 − 38 = 22 (m). Diện tích: 38 × 22 = 836 (m²).",
    ),

    # =========================================================
    # LỚP 5 (6 BÀI)
    # =========================================================
    M(
        5,
        "so-thap-phan",
        "Số thập phân & Bốn phép tính với số thập phân",
        "🔢",
        "Hiểu cấu tạo số thập phân, so sánh, làm tròn và thực hiện thành thạo cộng, trừ, nhân, chia số thập phân.",
        "Số thập phân gồm hai phần ngăn cách nhau bởi dấu phẩy (,): bên trái là phần nguyên, bên phải là phần thập phân (hàng phần mười, phần trăm, phần nghìn...).",
        "• Chuyển đổi phân số thập phân (mẫu là 10, 100, 1000...) thành số thập phân và ngược lại.\n"
        "• Tính chất bằng nhau khi viết thêm hoặc xóa chữ số 0 ở tận cùng bên phải phần thập phân.\n"
        "• Cộng, trừ, nhân, chia số thập phân; nhân và chia nhẩm với 10, 100, 1000 hoặc với 0,1; 0,01; 0,001.",
        [
            {
                "category": "I. Cấu tạo & Chuyển đổi số thập phân",
                "items": [
                    {"name": "Hàng của phần thập phân", "formula": "a,bcd = a + b/10 + c/100 + d/1000", "note": "b: phần mười, c: phần trăm, d: phần nghìn"},
                    {"name": "Số thập phân bằng nhau", "formula": "a,b = a,b0 = a,b00", "note": "Thêm/bớt số 0 tận cùng bên phải không đổi giá trị"},
                ],
            },
            {
                "category": "II. Quy tắc dịch dấu phẩy khi Nhân & Chia nhẩm",
                "items": [
                    {"name": "Nhân với 10, 100, 1000 (hoặc chia cho 0,1; 0,01; 0,001)", "formula": "Dịch dấu phẩy sang BÊN PHẢI 1, 2, 3,... chữ số", "note": "Ví dụ: 3,45 × 10 = 34,5"},
                    {"name": "Chia cho 10, 100, 1000 (hoặc nhân với 0,1; 0,01; 0,001)", "formula": "Dịch dấu phẩy sang BÊN TRÁI 1, 2, 3,... chữ số", "note": "Ví dụ: 25,6 : 10 = 2,56"},
                ],
            },
        ],
        "Giúp biểu diễn và tính toán chính xác các số đo độ dài, khối lượng, diện tích và tiền tệ trong thực tế.",
        "Đọc chỉ số công tơ điện, cân nặng 42,5 kg, chiều cao 1,58 m, điểm trung bình môn học 8,75.",
        "Tính: a) 12,45 + 7,8 ; b) 15,6 : 1,2.",
        "a) Đặt dấu phẩy thẳng cột: 12,45 + 7,80 = 20,25. b) Bỏ dấu phẩy ở số chia (nhân cả hai với 10): 156 : 12 = 13.",
        "Kết quả của phép tính 4,75 × 0,1 + 4,75 × 0,9 là bao nhiêu?",
        ["0,475", "4,75", "47,5", "9,5"],
        1,
        "Một can nhựa rỗng nặng 0,45 kg. Khi đổ đầy 15 lít dầu hỏa vào can thì cân nặng tất cả là 12,45 kg. Hỏi mỗi lít dầu hỏa nặng bao nhiêu ki-lô-gam?",
        "Khối lượng của 15 lít dầu hỏa là: 12,45 − 0,45 = 12 (kg). Mỗi lít dầu hỏa nặng: 12 : 15 = 0,8 (kg).",
    ),
    M(
        5,
        "phan-so",
        "Hỗn số, Phân số thập phân & Ôn tập nâng cao về Phân số",
        "🍰",
        "Chuyển đổi giữa hỗn số và phân số, viết số đo đại lượng dưới dạng số thập phân thông qua phân số thập phân.",
        "Hỗn số gồm phần nguyên kết hợp với phần phân số (phần phân số luôn nhỏ hơn 1), giúp biểu diễn gọn các lượng lớn hơn 1 đơn vị.",
        "• Đọc, viết hỗn số và cách đổi hỗn số ra phân số, đổi phân số lớn hơn 1 ra hỗn số.\n"
        "• Phân số thập phân là phân số có mẫu số là 10, 100, 1000,...\n"
        "• Đổi các đơn vị đo độ dài, khối lượng, diện tích (km², ha) sang phân số thập phân và số thập phân.",
        [
            {
                "category": "I. Hỗn số & Chuyển đổi",
                "items": [
                    {"name": "Cấu tạo hỗn số", "formula": "A và b/c = A + b/c (với b < c)", "note": "A là phần nguyên, b/c là phần phân số"},
                    {"name": "Đổi hỗn số ra phân số", "formula": "A (b/c) = (A × c + b) / c", "note": "Ví dụ: 2 (3/5) = (2×5 + 3)/5 = 13/5"},
                ],
            },
            {
                "category": "II. Đơn vị diện tích lớn (Héc-ta & Ki-lô-mét vuông)",
                "items": [
                    {"name": "Héc-ta (ha)", "formula": "1 ha = 1 hm² = 10 000 m²", "note": "Dùng đo diện tích ruộng đất, nông trường, rừng"},
                    {"name": "Ki-lô-mét vuông (km²)", "formula": "1 km² = 100 ha = 1 000 000 m²", "note": "1 ha = 1/100 km² = 0,01 km²"},
                ],
            },
        ],
        "Giúp chuyển đổi linh hoạt giữa phân số, hỗn số và số thập phân khi đo đạc ruộng đất và giải toán.",
        "Đo diện tích rừng quốc gia bằng héc-ta (ha), diện tích cánh đồng lúa hoặc thời gian 2 và 1/2 giờ.",
        "Chuyển hỗn số 3 và 3/4 thành phân số, sau đó viết dưới dạng phân số thập phân và số thập phân.",
        "3 và 3/4 = (3 × 4 + 3)/4 = 15/4 = (15 × 25)/(4 × 25) = 375/100 = 3,75.",
        "Một khu rừng sinh thái có diện tích 4 km² 25 ha. Diện tích khu rừng đó tính theo đơn vị ki-lô-mét vuông là:",
        ["4,025 km²", "4,25 km²", "42,5 km²", "425 km²"],
        1,
        "Một cánh đồng hình chữ nhật có chiều dài 800 m, chiều rộng 500 m. Hỏi diện tích cánh đồng đó bằng bao nhiêu héc-ta (ha)?",
        "Diện tích cánh đồng là: 800 × 500 = 400 000 (m²). Đổi: 400 000 m² = 40 ha.",
    ),
    M(
        5,
        "hinh-hoc",
        "Diện tích Tam giác, Hình thang, Hình tròn & Thể tích Hình hộp, Hình lập phương",
        "📦",
        "Nắm trọn bộ công thức diện tích hình phẳng và diện tích xung quanh, toàn phần, thể tích các hình khối.",
        "Hình học lớp 5 tổng hợp toàn bộ công thức tính diện tích tam giác, hình thang, hình tròn và mở rộng sang không gian 3 chiều (cm³, dm³, m³).",
        "• Diện tích hình tam giác, hình thang; chu vi và diện tích hình tròn (số π ≈ 3,14).\n"
        "• Đơn vị đo thể tích: m³, dm³ (1 dm³ = 1 lít), cm³ (hai đơn vị liền kề gấp/kém nhau 1000 lần).\n"
        "• Diện tích xung quanh (Sxq), diện tích toàn phần (Stp) và thể tích (V) của hình hộp chữ nhật, hình lập phương, làm quen hình trụ - hình cầu.",
        [
            {
                "category": "I. Hình phẳng: Tam giác, Hình thang, Hình tròn",
                "items": [
                    {"name": "Hình tam giác (đáy a, cao h)", "formula": "S = (a × h) : 2  ⇒  a = (S × 2) : h ; h = (S × 2) : a", "note": ""},
                    {"name": "Hình thang (đáy lớn a, đáy bé b, cao h)", "formula": "S = (a + b) × h : 2", "note": "Muốn tính diện tích hình thang, đáy lớn đáy nhỏ ta mang cộng vào..."},
                    {"name": "Hình tròn (bán kính r, đường kính d)", "formula": "Chu vi: C = d × 3,14 = r × 2 × 3,14 ; Diện tích: S = r × r × 3,14", "note": "π ≈ 3,14"},
                ],
            },
            {
                "category": "II. Hình khối 3D & Đơn vị đo Thể tích",
                "items": [
                    {"name": "Quy đổi thể tích", "formula": "1 m³ = 1000 dm³ = 1 000 000 cm³ ; 1 dm³ = 1000 cm³ = 1 lít", "note": "Hai đơn vị liền kề hơn kém nhau 1000 lần"},
                    {"name": "Hình hộp chữ nhật (dài a, rộng b, cao c)", "formula": "Sxq = (a + b) × 2 × c ; Stp = Sxq + 2 × a × b ; V = a × b × c", "note": ""},
                    {"name": "Hình lập phương (cạnh a)", "formula": "Sxq = (a × a) × 4 ; Stp = (a × a) × 6 ; V = a × a × a", "note": ""},
                ],
            },
        ],
        "Giúp tính toán diện tích sơn tường, thể tích bể chứa nước, diện tích bồn hoa tròn và thiết kế bao bì.",
        "Tính số lít nước trong bể cá cảnh, diện tích sơn căn phòng và diện tích mặt bàn tròn.",
        "Một bể cá dạng hình hộp chữ nhật (không có nắp) có chiều dài 8 dm, chiều rộng 5 dm, chiều cao 6 dm. Tính thể tích bể cá theo đơn vị lít.",
        "Thể tích bể cá là: V = 8 × 5 × 6 = 240 (dm³). Vì 1 dm³ = 1 lít nên bể chứa được tối đa 240 lít nước.",
        "Một bồn hoa hình tròn có đường kính d = 6 m. Diện tích của bồn hoa đó là bao nhiêu?",
        ["18,84 m²", "28,26 m²", "37,68 m²", "113,04 m²"],
        1,
        "Một thửa ruộng hình thang có đáy lớn 42 m, đáy bé bằng 2/3 đáy lớn, chiều cao bằng trung bình cộng hai đáy. Tính diện tích thửa ruộng đó.",
        "Đáy bé là: 42 × 2/3 = 28 (m). Chiều cao là: (42 + 28) : 2 = 35 (m). Diện tích thửa ruộng: (42 + 28) × 35 : 2 = 1 225 (m²).",
    ),
    M(
        5,
        "ti-so",
        "Tỉ số, Tỉ lệ bản đồ & Bài toán Tìm hai số khi biết Tổng (hoặc Hiệu) và Tỉ số",
        "🗺️",
        "Giải quyết bài toán Tổng - Tỉ, Hiệu - Tỉ và tính khoảng cách thực tế thông qua tỉ lệ bản đồ.",
        "Tỉ số a : b (hoặc a/b với b ≠ 0) cho biết đại lượng này bằng bao nhiêu phần của đại lượng kia.",
        "• Giải bài toán 'Tìm hai số khi biết Tổng và Tỉ số' (Tổng - Tỉ).\n"
        "• Giải bài toán 'Tìm hai số khi biết Hiệu và Tỉ số' (Hiệu - Tỉ).\n"
        "• Bài toán hai đại lượng tỉ lệ thuận, tỉ lệ nghịch (bằng phương pháp rút về đơn vị hoặc tìm tỉ số).\n"
        "• Tỉ lệ bản đồ (ví dụ 1 : 1 000 000): tính độ dài thực tế và độ dài thu nhỏ trên bản đồ.",
        [
            {
                "category": "I. Bài toán Tổng - Tỉ và Hiệu - Tỉ (tỉ số m/n)",
                "items": [
                    {"name": "Bài toán Tổng - Tỉ", "formula": "Tổng số phần = m + n ; Giá trị 1 phần = Tổng : (m + n)", "note": "Số bé = Giá trị 1 phần × m ; Số lớn = Giá trị 1 phần × n"},
                    {"name": "Bài toán Hiệu - Tỉ", "formula": "Hiệu số phần = n − m ; Giá trị 1 phần = Hiệu : (n − m)", "note": "Số bé = Giá trị 1 phần × m ; Số lớn = Giá trị 1 phần × n"},
                ],
            },
            {
                "category": "II. Tỉ lệ bản đồ (1 : k)",
                "items": [
                    {"name": "Độ dài thực tế", "formula": "D_thực = d_bản_đồ × k", "note": "Sau khi nhân xong thường đổi ra m hoặc km"},
                    {"name": "Độ dài trên bản đồ", "formula": "d_bản_đồ = D_thực : k", "note": "Đổi D_thực ra cùng đơn vị nhỏ (cm, mm) trước khi chia"},
                ],
            },
        ],
        "Giúp đọc bản đồ địa lý, bản vẽ thiết kế kiến trúc và phân chia nguồn lực theo tỉ lệ cho trước.",
        "Đo khoảng cách giữa hai thành phố trên bản đồ, pha chế bê tông hoặc chia lợi nhuận theo tỉ lệ góp vốn.",
        "Hiệu của hai số là 45, tỉ số của hai số đó là 2/5. Tìm hai số đó.",
        "Hiệu số phần bằng nhau: 5 − 2 = 3 (phần). Giá trị 1 phần: 45 : 3 = 15. Số bé: 15 × 2 = 30. Số lớn: 15 × 5 = 75.",
        "Trên bản đồ tỉ lệ 1 : 500 000, khoảng cách giữa hai địa điểm đo được là 4 cm. Khoảng cách thực tế giữa hai địa điểm đó là bao nhiêu ki-lô-mét?",
        ["2 km", "20 km", "200 km", "50 km"],
        1,
        "Một nông trại nuôi 240 con cả gà và vịt, biết số vịt bằng 3/5 số gà. Hỏi nông trại đó nuôi bao nhiêu con gà, bao nhiêu con vịt?",
        "Tổng số phần bằng nhau: 3 + 5 = 8 (phần). Số vịt là: (240 : 8) × 3 = 90 (con). Số gà là: 240 − 90 = 150 (con).",
    ),
    M(
        5,
        "ti-so-phan-tram-chuyen-dong",
        "Tỉ số phần trăm, Biểu đồ hình quạt tròn & Toán chuyển động đều",
        "🚄",
        "Nắm vững 3 dạng bài toán tỉ số phần trăm, đọc biểu đồ quạt tròn và công thức Vận tốc - Quãng đường - Thời gian.",
        "Tỉ số phần trăm (ký hiệu %) là phân số có mẫu số là 100; Toán chuyển động đều mô tả mối liên hệ giữa vận tốc (v), quãng đường (s) và thời gian (t).",
        "• Ba bài toán cơ bản về tỉ số phần trăm: Tìm tỉ số % của hai số; Tìm giá trị % của một số; Tìm một số khi biết giá trị % của nó.\n"
        "• Đọc và xử lý số liệu trên biểu đồ hình quạt tròn (tổng cả hình tròn là 100%).\n"
        "• Công thức chuyển động đều: v = s : t ; s = v × t ; t = s : v và bài toán hai xe chuyển động ngược chiều / cùng chiều.",
        [
            {
                "category": "I. Ba bài toán Tỉ số phần trăm",
                "items": [
                    {"name": "Dạng 1: Tỉ số % của a và b", "formula": "(a : b) × 100%", "note": "Tìm thương của a : b rồi nhân nhẩm với 100 và viết ký hiệu %"},
                    {"name": "Dạng 2: Tìm p% của số A", "formula": "Giá trị = A × p : 100", "note": "Ứng dụng tính tiền giảm giá, tiền lãi ngân hàng"},
                    {"name": "Dạng 3: Tìm số A khi biết p% của A là B", "formula": "A = B : p × 100", "note": "Bài toán ngược"},
                ],
            },
            {
                "category": "II. Toán chuyển động đều",
                "items": [
                    {"name": "Vận tốc, Quãng đường, Thời gian", "formula": "v = s : t  ;  s = v × t  ;  t = s : v", "note": "Đơn vị tương ứng: (km/h, km, giờ) hoặc (m/s, m, giây)"},
                    {"name": "Hai xe đi ngược chiều (cùng lúc)", "formula": "t_gặp = S_ban_đầu : (v₁ + v₂)", "note": "Tổng vận tốc: v₁ + v₂"},
                    {"name": "Hai xe đi cùng chiều (đuổi nhau)", "formula": "t_đuổi_kịp = S_cách_nhau : (v₁ − v₂) (với v₁ > v₂)", "note": "Hiệu vận tốc: v₁ − v₂"},
                ],
            },
        ],
        "Ứng dụng trực tiếp nhất vào tính lãi suất tiết kiệm, giảm giá khuyến mãi và tính thời gian di chuyển tàu xe.",
        "Tính giá sản phẩm sau khi giảm giá 20% (Sale off), tính lãi suất ngân hàng và tính giờ ô tô đến nơi.",
        "Một ô tô đi quãng đường dài 135 km hết 2 giờ 15 phút. Tính vận tốc của ô tô theo km/h.",
        "Đổi 2 giờ 15 phút = 2,25 giờ. Vận tốc của ô tô là: v = 135 : 2,25 = 60 (km/h).",
        "Một chiếc balo có giá niêm yết 350 000 đồng. Nhân dịp khai giảng, cửa hàng giảm giá 20%. Hỏi giá chiếc balo sau khi giảm là bao nhiêu?",
        ["70 000 đồng", "280 000 đồng", "300 000 đồng", "330 000 đồng"],
        1,
        "Lúc 7 giờ sáng, một người đi xe máy từ A với vận tốc 40 km/h và một người đi ô tô từ B với vận tốc 55 km/h đi ngược chiều nhau. Biết quãng đường AB dài 190 km. Hỏi hai xe gặp nhau lúc mấy giờ?",
        "Tổng vận tốc hai xe: 40 + 55 = 95 (km/h). Thời gian đi để gặp nhau: 190 : 95 = 2 (giờ). Hai xe gặp nhau lúc: 7 giờ + 2 giờ = 9 giờ sáng.",
    ),
    M(
        5,
        "toan-thuc-te",
        "Giải toán thực tế tổng hợp cấp Tiểu học",
        "🌍",
        "Vận dụng tổng hợp số thập phân, phần trăm, hình học và chuyển động để giải quyết bài toán thực tiễn.",
        "Toán thực tế kết nối các công cụ số học, đại lượng và hình học để giải quyết các bài toán tài chính gia đình, thiết kế và sản xuất.",
        "• Phân tích đề bài nhiều bước tính, lập kế hoạch giải quyết vấn đề.\n"
        "• Bài toán mua bán: Giá vốn, giá bán, tiền lãi/lỗ.\n"
        "• Bài toán năng suất công việc và bài toán hình học gắn với chi phí thực tế.",
        [
            {
                "category": "I. Bài toán Tài chính - Mua bán",
                "items": [
                    {"name": "Tiền lãi & Tỉ suất lãi", "formula": "Tiền lãi = Giá bán − Giá vốn ; % Lãi (so với vốn) = (Tiền lãi : Giá vốn) × 100%", "note": ""},
                    {"name": "Giá sau thuế / chiết khấu", "formula": "Giá thanh toán = Giá gốc × (100% − % Giảm giá)", "note": ""},
                ],
            },
            {
                "category": "II. Bài toán Chi phí Xây dựng & Sản xuất",
                "items": [
                    {"name": "Tổng chi phí theo diện tích", "formula": "Tổng tiền = Diện tích cần thi công (m²) × Đơn giá 1 m²", "note": "Trừ đi diện tích cửa khi sơn tường"},
                ],
            },
        ],
        "Giúp học sinh tổng hợp toàn bộ kiến thức Tiểu học để sẵn sàng bước vào cấp THCS.",
        "Lập dự toán sơn phòng học, tính lợi nhuận bán hàng hội chợ trường hoặc tính thời gian hành trình du lịch.",
        "Một cửa hàng nhập một chiếc quạt điện với giá vốn 400 000 đồng. Để bán được lãi 15% so với giá vốn thì cửa hàng cần định giá bán là bao nhiêu?",
        "Tiền lãi cần đạt là: 400 000 × 15 : 100 = 60 000 (đồng). Giá bán là: 400 000 + 60 000 = 460 000 (đồng).",
        "Một vòi nước chảy vào bể mỗi phút được 25 lít nước. Biết bể có thể tích 1,5 m³. Hỏi nếu bể đang cạn thì sau bao nhiêu phút vòi chảy đầy bể?",
        ["40 phút", "50 phút", "60 phút", "6 phút"],
        2,
        "Một phòng học hình hộp chữ nhật dài 8 m, rộng 6 m, cao 3,5 m. Nhà trường quét sơn bốn bức tường xung quanh và trần nhà bên trong phòng, biết diện tích các cửa là 12 m². Tính số tiền sơn phải trả, biết mỗi mét vuông sơn hết 45 000 đồng.",
        "Diện tích xung quanh: (8 + 6) × 2 × 3,5 = 98 (m²). Diện tích trần nhà: 8 × 6 = 48 (m²). Diện tích cần sơn: 98 + 48 − 12 = 134 (m²). Số tiền phải trả: 134 × 45 000 = 6 030 000 (đồng).",
    ),

    # =========================================================
    # LỚP 6 (6 BÀI)
    # =========================================================
    M(
        6,
        "so-tu-nhien",
        "Tập hợp Số tự nhiên, Lũy thừa với số mũ tự nhiên & Thứ tự thực hiện phép tính",
        "🔢",
        "Nắm vững ký hiệu tập hợp ℕ, ℕ*, phép nâng lên lũy thừa và thứ tự thực hiện phép tính có dấu ngoặc.",
        "Tập hợp các số tự nhiên được ký hiệu là ℕ = {0; 1; 2; 3; ...} và tập các số tự nhiên khác 0 là ℕ* = {1; 2; 3; ...}. Lũy thừa bậc n của a là tích của n thừa số bằng nhau, mỗi thừa số bằng a.",
        "• Cách viết tập hợp (liệt kê phần tử hoặc chỉ ra tính chất đặc trưng) và ký hiệu ∈, ∉.\n"
        "• Lũy thừa với số mũ tự nhiên: nhân, chia hai lũy thừa cùng cơ số.\n"
        "• Thứ tự ưu tiên thực hiện phép tính: Lũy thừa → Nhân và Chia → Cộng và Trừ; Ngoặc tròn ( ) → Ngoặc vuông [ ] → Ngoặc nhọn { }.",
        [
            {
                "category": "I. Phép tính Lũy thừa với số mũ tự nhiên",
                "items": [
                    {"name": "Định nghĩa lũy thừa", "formula": "aⁿ = a · a · ... · a (n thừa số a, với n ∈ ℕ*)", "note": "a là cơ số, n là số mũ"},
                    {"name": "Quy ước mũ 0 và mũ 1", "formula": "a¹ = a  ;  a⁰ = 1 (với a ≠ 0)", "note": ""},
                    {"name": "Nhân hai lũy thừa cùng cơ số", "formula": "aᵐ · aⁿ = aᵐ⁺ⁿ", "note": "Giữ nguyên cơ số, cộng hai số mũ"},
                    {"name": "Chia hai lũy thừa cùng cơ số", "formula": "aᵐ : aⁿ = aᵐ⁻ⁿ (với a ≠ 0, m ≥ n)", "note": "Giữ nguyên cơ số, trừ hai số mũ"},
                ],
            },
            {
                "category": "II. Thứ tự thực hiện các phép tính",
                "items": [
                    {"name": "Không có ngoặc", "formula": "Lũy thừa → Nhân và Chia → Cộng và Trừ", "note": ""},
                    {"name": "Có dấu ngoặc", "formula": "( ) → [ ] → { }", "note": "Tính từ ngoặc trong ra ngoặc ngoài"},
                ],
            },
        ],
        "Lũy thừa giúp biểu diễn cực gọn những con số khổng lồ trong tin học (2¹⁰ = 1024 byte), sinh học và thiên văn học.",
        "Tính dung lượng bộ nhớ máy tính (KB, MB, GB), sự nhân đôi của tế bào vi khuẩn theo thời gian.",
        "Tính giá trị của biểu thức: A = 3 · 2³ + 18 : 3² − 5⁰.",
        "A = 3 · 8 + 18 : 9 − 1 = 24 + 2 − 1 = 25.",
        "Kết quả viết dưới dạng một lũy thừa của phép tính 5⁷ · 5³ : 5⁴ là:",
        ["5⁶", "5¹⁴", "5⁵", "5²¹"],
        0,
        "Một loài vi khuẩn cứ sau mỗi 20 phút lại phân đôi một lần (từ 1 tế bào thành 2 tế bào). Ban đầu có 1 tế bào vi khuẩn. Hỏi sau 2 giờ sẽ có bao nhiêu tế bào vi khuẩn?",
        "Đổi 2 giờ = 120 phút. Số lần phân đôi là: 120 : 20 = 6 (lần). Số tế bào vi khuẩn sau 2 giờ là: 2⁶ = 64 (tế bào).",
    ),
    M(
        6,
        "so-nguyen-chia-het",
        "Tính chia hết, Số nguyên tố, ƯCLN - BCNN & Tập hợp Số nguyên ℤ",
        "🌡️",
        "Thành thạo phân tích thừa số nguyên tố để tìm ƯCLN, BCNN và thực hiện các phép toán trên tập số nguyên ℤ.",
        "Tập hợp số nguyên ℤ = {..., −3, −2, −1, 0, 1, 2, 3, ...} mở rộng tập số tự nhiên bằng cách bổ sung các số nguyên âm để biểu diễn các đại lượng có hai chiều ngược nhau.",
        "• Số nguyên tố, hợp số và phân tích một số ra thừa số nguyên tố.\n"
        "• Quy tắc tìm Ước chung lớn nhất (ƯCLN) và Bội chung nhỏ nhất (BCNN).\n"
        "• Số đối, thứ tự trên trục số nguyên.\n"
        "• Quy tắc cộng, trừ, nhân, chia hai số nguyên và quy tắc dấu ngoặc.",
        [
            {
                "category": "I. Ước chung lớn nhất (ƯCLN) & Bội chung nhỏ nhất (BCNN)",
                "items": [
                    {"name": "Tìm ƯCLN bằng phân tích TSNT", "formula": "Tích các thừa số nguyên tố CHUNG với số mũ NHỎ NHẤT", "note": "ƯC(a, b) là ước của ƯCLN(a, b)"},
                    {"name": "Tìm BCNN bằng phân tích TSNT", "formula": "Tích các thừa số nguyên tố CHUNG và RIÊNG với số mũ LỚN NHẤT", "note": "BC(a, b) là bội của BCNN(a, b)"},
                    {"name": "Hệ thức liên hệ", "formula": "a · b = ƯCLN(a, b) · BCNN(a, b)", "note": "Với hai số nguyên dương a, b"},
                ],
            },
            {
                "category": "II. Phép toán trên Tập hợp Số nguyên ℤ",
                "items": [
                    {"name": "Cộng hai số nguyên", "formula": "Cùng dấu: (−a) + (−b) = −(a + b) ; Khác dấu: lấy số lớn trừ số bé, mang dấu của số có phần tự nhiên lớn hơn", "note": "a + (−a) = 0"},
                    {"name": "Trừ hai số nguyên & Quy tắc dấu ngoặc", "formula": "a − b = a + (−b)  ;  −(a − b + c) = −a + b − c", "note": "Trước ngoặc có dấu '−' thì đổi dấu mọi số hạng trong ngoặc"},
                    {"name": "Quy tắc dấu trong Nhân & Chia", "formula": "(+) · (+) = (+) ; (−) · (−) = (+) ; (+) · (−) = (−)", "note": "Cùng dấu ra Dương, trái dấu ra Âm"},
                ],
            },
        ],
        "Giúp giải các bài toán chia nhóm đều nhất (ƯCLN), tìm chu kỳ lặp lại trùng nhau (BCNN) và tính toán nhiệt độ âm, độ sâu dưới mực nước biển, tài chính thu - chi.",
        "Chia quà từ thiện thành nhiều phần giống nhau nhất (ƯCLN), tính lịch trực nhật trùng nhau (BCNN), theo dõi nhiệt độ mùa đông.",
        "Tìm ƯCLN(24, 36) và BCNN(24, 36).",
        "Ta có 24 = 2³ · 3 và 36 = 2² · 3². Vậy ƯCLN(24, 36) = 2² · 3 = 12 ; BCNN(24, 36) = 2³ · 3² = 72.",
        "Kết quả của phép tính (−15) + (−25) − (−10) · (−3) là:",
        ["−70", "−10", "20", "−40"],
        0,
        "Đội văn nghệ của trường có 48 nam và 72 nữ. Cô phụ trách muốn chia đội thành các tổ sao cho số nam và số nữ được chia đều vào các tổ. Hỏi có thể chia được nhiều nhất thành bao nhiêu tổ? Khi đó mỗi tổ có bao nhiêu nam, bao nhiêu nữ?",
        "Số tổ nhiều nhất là ƯCLN(48, 72) = 24 (tổ). Khi đó mỗi tổ có: 48 : 24 = 2 (nam) và 72 : 24 = 3 (nữ).",
    ),
    M(
        6,
        "phan-so",
        "Phân số với tử và mẫu là số nguyên & Hai bài toán về phân số",
        "➗",
        "Mở rộng phân số sang tử và mẫu nguyên, thực hiện các phép tính và giải hai bài toán cơ bản về phân số.",
        "Phân số ở lớp 6 có dạng a/b với a, b ∈ ℤ và b ≠ 0. Hai phân số a/b và c/d bằng nhau nếu a · d = b · c.",
        "• Rút gọn, quy đồng mẫu nhiều phân số (đưa về mẫu dương rồi lấy BCNN của các mẫu).\n"
        "• Cộng, trừ, nhân, chia phân số âm và dương; tính chất phân phối của phép nhân.\n"
        "• Bài toán 1: Tìm giá trị phân số m/n của một số a cho trước (tính a · m/n).\n"
        "• Bài toán 2: Tìm một số biết giá trị phân số m/n của nó bằng b (tính b : m/n).",
        [
            {
                "category": "I. Định nghĩa & Phép toán phân số (a, b, c, d ∈ ℤ)",
                "items": [
                    {"name": "Hai phân số bằng nhau", "formula": "a/b = c/d ⇔ a · d = b · c (b, d ≠ 0)", "note": "Quy tắc nhân chéo"},
                    {"name": "Đổi dấu phân số", "formula": "a/(−b) = (−a)/b = −(a/b)  ;  (−a)/(−b) = a/b", "note": "Luôn đưa phân số về mẫu số dương trước khi quy đồng"},
                    {"name": "Số nghịch đảo", "formula": "Nghịch đảo của a/b (a, b ≠ 0) là b/a (vì a/b · b/a = 1)", "note": ""},
                ],
            },
            {
                "category": "II. Hai bài toán cơ bản về Phân số",
                "items": [
                    {"name": "Bài toán 1 (Tìm m/n của số A)", "formula": "Giá trị = A · (m/n)", "note": "Biết tổng thể, tìm phần nhỏ"},
                    {"name": "Bài toán 2 (Biết m/n của X bằng B)", "formula": "X = B : (m/n) = B · (n/m)", "note": "Biết một phần, tìm tổng thể ban đầu"},
                ],
            },
        ],
        "Giúp giải quyết các bài toán tỉ lệ, phần trăm giảm giá, khối lượng nguyên liệu và tài chính.",
        "Tính giá gốc của mặt hàng khi biết giá đã giảm, tính dung lượng pin còn lại và chia phần công việc.",
        "Tìm x, biết: (3/5) · x − 1/2 = 7/10.",
        "(3/5) · x = 7/10 + 1/2 = 7/10 + 5/10 = 12/10 = 6/5 ⇒ x = (6/5) : (3/5) = 2.",
        "Một quyển sách sau khi giảm giá 1/5 giá bìa thì bán với giá 64 000 đồng. Giá bìa ban đầu của quyển sách đó là bao nhiêu?",
        ["76 800 đồng", "80 000 đồng", "75 000 đồng", "90 000 đồng"],
        1,
        "Bạn An đọc một cuốn truyện trong 3 ngày. Ngày thứ nhất đọc được 1/3 số trang. Ngày thứ hai đọc được 5/8 số trang còn lại. Ngày thứ ba đọc nốt 36 trang cuối cùng. Hỏi cuốn truyện có tất cả bao nhiêu trang?",
        "Sau ngày 1 còn lại 1 − 1/3 = 2/3 (cuốn). Ngày 2 đọc 5/8 phần còn lại, nên 36 trang ngày 3 ứng với: 1 − 5/8 = 3/8 (phần còn lại). Số trang còn lại sau ngày 1 là: 36 : (3/8) = 96 (trang). Tổng số trang cuốn truyện là: 96 : (2/3) = 144 (trang).",
    ),
    M(
        6,
        "hinh-hoc",
        "Hình học trực quan (Tính đối xứng) & Hình học phẳng cơ bản (Điểm, Đường thẳng, Góc)",
        "📐",
        "Nhận biết hình có trục đối xứng, tâm đối xứng, tính chu vi - diện tích các tứ giác và nắm vững tia, đoạn thẳng, góc.",
        "Hình học lớp 6 gồm hai mảng: Hình học trực quan (các tứ giác đặc biệt, tính đối xứng trong tự nhiên) và Hình học phẳng cơ bản (điểm, đường thẳng, tia, đoạn thẳng, trung điểm, góc).",
        "• Ôn tập và tổng hợp công thức chu vi, diện tích: Hình vuông, chữ nhật, tam giác, hình thang, hình bình hành, hình thoi.\n"
        "• Hình có trục đối xứng (cánh bướm, chữ A, hình thang cân, hình thoi) và hình có tâm đối xứng (chữ S, hình bình hành, hình tròn).\n"
        "• Điểm thuộc/không thuộc đường thẳng, ba điểm thẳng hàng, hai đường thẳng cắt nhau/song song, tia, đoạn thẳng, trung điểm của đoạn thẳng và số đo góc.",
        [
            {
                "category": "I. Chu vi & Diện tích các hình tứ giác đặc biệt",
                "items": [
                    {"name": "Hình bình hành & Hình thoi", "formula": "S_bình_hành = a · h  ;  S_thoi = (d₁ · d₂) / 2", "note": "d₁, d₂ là độ dài hai đường chéo hình thoi"},
                    {"name": "Hình thang (đáy a, b; cao h)", "formula": "S_thang = (a + b) · h / 2", "note": ""},
                ],
            },
            {
                "category": "II. Đoạn thẳng, Trung điểm & Số đo Góc",
                "items": [
                    {"name": "Điểm nằm giữa", "formula": "Nếu M nằm giữa A và B thì AM + MB = AB", "note": ""},
                    {"name": "Trung điểm M của AB", "formula": "MA = MB = AB / 2", "note": "M vừa nằm giữa A, B vừa cách đều A, B"},
                    {"name": "Số đoạn thẳng tạo từ n điểm", "formula": "Số đoạn thẳng = n · (n − 1) / 2", "note": "Cứ 2 điểm nối được 1 đoạn thẳng"},
                ],
            },
        ],
        "Giúp ứng dụng tính đối xứng trong kiến trúc, thiết kế logo và tính toán khoảng cách trên bản vẽ kỹ thuật.",
        "Nhận diện trục đối xứng, tâm đối xứng của biển báo giao thông, hoa văn kiến trúc và đo khoảng cách giữa các trạm trên một tuyến đường thẳng.",
        "Trên tia Ox lấy hai điểm A và B sao cho OA = 4 cm, OB = 10 cm. Gọi M là trung điểm của đoạn thẳng AB. Tính độ dài đoạn thẳng AB và OM.",
        "Vì OA < OB (4 < 10) nên A nằm giữa O và B ⇒ AB = OB − OA = 10 − 4 = 6 (cm). Vì M là trung điểm của AB nên AM = AB / 2 = 3 (cm). Vậy OM = OA + AM = 4 + 3 = 7 (cm).",
        "Cho 10 điểm phân biệt, cứ qua 2 điểm ta vẽ được một đoạn thẳng. Hỏi vẽ được tất cả bao nhiêu đoạn thẳng?",
        ["20 đoạn thẳng", "45 đoạn thẳng", "50 đoạn thẳng", "90 đoạn thẳng"],
        1,
        "Một sân vườn hình chữ nhật có chiều dài 20 m, chiều rộng 12 m. Chính giữa sân người ta xây một bồn hoa hình thoi có độ dài hai đường chéo là 8 m và 5 m, phần còn lại lát cỏ. Tính diện tích phần sân lát cỏ.",
        "Diện tích sân vườn: 20 · 12 = 240 (m²). Diện tích bồn hoa hình thoi: (8 · 5) : 2 = 20 (m²). Diện tích phần lát cỏ: 240 − 20 = 220 (m²).",
    ),
    M(
        6,
        "du-lieu",
        "Thu thập, Tổ chức dữ liệu, Biểu đồ cột kép & Xác suất thực nghiệm",
        "📊",
        "Phân loại dữ liệu định tính - định lượng, đọc biểu đồ cột kép và tính xác suất thực nghiệm của một sự kiện.",
        "Thống kê lớp 6 giúp học sinh phân biệt dữ liệu là số (số liệu) và dữ liệu không phải là số, so sánh hai bộ dữ liệu qua biểu đồ cột kép và tính xác suất thực nghiệm.",
        "• Thu thập, phân loại và kiểm tra tính hợp lý của dữ liệu trong bảng thống kê.\n"
        "• Biểu đồ tranh, biểu đồ cột và biểu đồ cột kép (so sánh hai nhóm đối tượng theo cùng tiêu chí).\n"
        "• Phép thử nghiệm, sự kiện và công thức tính Xác suất thực nghiệm.",
        [
            {
                "category": "I. Thống kê & Biểu đồ cột kép",
                "items": [
                    {"name": "Độ chênh lệch trên cột kép", "formula": "Δ = |Cột_nhóm_1 − Cột_nhóm_2|", "note": "So sánh hai đối tượng tại cùng một mốc thời gian/địa điểm"},
                ],
            },
            {
                "category": "II. Xác suất thực nghiệm",
                "items": [
                    {"name": "Xác suất thực nghiệm của sự kiện A", "formula": "P_tn(A) = n(A) / N", "note": "n(A): số lần sự kiện A xảy ra ; N: tổng số lần thực hiện phép thử"},
                ],
            },
        ],
        "Giúp đánh giá khả năng xảy ra của sự kiện dựa trên số liệu thực tế và phân tích báo cáo so sánh.",
        "So sánh doanh số hai chi nhánh qua biểu đồ cột kép, tính tỉ lệ nảy mầm của hạt giống hoặc tỉ lệ sút bóng trúng đích.",
        "Một cầu thủ thực hiện 40 quả sút phạt đền trong buổi tập và ghi bàn được 32 quả. Tính xác suất thực nghiệm của sự kiện 'Cầu thủ sút phạt đền ghi bàn'.",
        "Xác suất thực nghiệm là: 32 / 40 = 4/5 = 0,8 (hay 80%).",
        "Gieo một con xúc xắc 6 mặt 50 lần, thấy mặt 6 chấm xuất hiện 8 lần, mặt 1 chấm xuất hiện 10 lần. Xác suất thực nghiệm của sự kiện 'Số chấm xuất hiện là 1 hoặc 6' là:",
        ["4/25", "1/5", "9/25", "8/50"],
        2,
        "Một hộp có các quả bóng màu xanh, đỏ, vàng. Nam lấy ngẫu nhiên 1 quả bóng, ghi lại màu rồi trả lại vào hộp. Lặp lại 60 lần, Nam thấy có 24 lần lấy được bóng xanh và 15 lần lấy được bóng đỏ. Tính xác suất thực nghiệm của sự kiện lấy được bóng màu vàng.",
        "Số lần lấy được bóng màu vàng là: 60 − (24 + 15) = 21 (lần). Xác suất thực nghiệm lấy được bóng vàng là: 21 / 60 = 7/20 = 0,35 (hay 35%).",
    ),
    M(
        6,
        "tu-duy-logic",
        "Tư duy Logic, Quy luật dãy số & Nguyên lý Dirichlet cơ bản",
        "🧠",
        "Phát triển tư duy suy luận logic, tính tổng dãy số cách đều (công thức Gauss) và giải toán suy luận.",
        "Tư duy logic sử dụng các quy tắc suy luận chặt chẽ, tìm quy luật tổng quát và loại trừ để giải các bài toán tổ hợp - số học thú vị.",
        "• Công thức tính số số hạng và tổng của dãy số tự nhiên cách đều.\n"
        "• Dãy phân số có quy luật (khử liên tiếp / phương pháp sai phân: 1/[n(n+1)] = 1/n − 1/(n+1)).\n"
        "• Suy luận logic loại trừ và Nguyên lý chuồng thỏ (Dirichlet) cơ bản.",
        [
            {
                "category": "I. Dãy số cách đều (khoảng cách d)",
                "items": [
                    {"name": "Số các số hạng", "formula": "Số số hạng = (Số cuối − Số đầu) : d + 1", "note": ""},
                    {"name": "Tổng của dãy số cách đều", "formula": "Tổng S = (Số đầu + Số cuối) · Số số hạng : 2", "note": "Công thức Gauss"},
                    {"name": "Tìm số hạng thứ n", "formula": "Số thứ n = Số đầu + (n − 1) · d", "note": ""},
                ],
            },
            {
                "category": "II. Dãy phân số quy luật & Nguyên lý Dirichlet",
                "items": [
                    {"name": "Công thức tách phân số", "formula": "1 / [n · (n + 1)] = 1/n − 1/(n + 1)  ;  k / [n · (n + k)] = 1/n − 1/(n + k)", "note": "Triệt tiêu các số hạng ở giữa"},
                    {"name": "Nguyên lý Dirichlet", "formula": "Nhốt N vật vào k chuồng (N > k) ⇒ có ít nhất 1 chuồng chứa từ ⌈N/k⌉ vật trở lên", "note": ""},
                ],
            },
        ],
        "Rèn luyện trí thông minh toán học, khả năng khái quát hóa thuật toán và tư duy lập trình.",
        "Tính tổng số ghế trong khán đài hình quạt, lập lịch thi đấu vòng tròn và giải các bài toán logic thực tế.",
        "Tính nhanh tổng: S = 1/(1·2) + 1/(2·3) + 1/(3·4) + ... + 1/(99·100).",
        "Ta có: S = (1 − 1/2) + (1/2 − 1/3) + (1/3 − 1/4) + ... + (1/99 − 1/100) = 1 − 1/100 = 99/100.",
        "Tổng của dãy số tự nhiên lẻ: 1 + 3 + 5 + 7 + ... + 99 bằng bao nhiêu?",
        ["2 450", "2 500", "4 950", "5 000"],
        1,
        "Một lớp học có 40 học sinh. Chứng minh rằng có ít nhất 4 học sinh có cùng tháng sinh trong năm.",
        "Một năm có 12 tháng. Ta có 40 = 12 · 3 + 4. Theo nguyên lý Dirichlet, nếu mỗi tháng có tối đa 3 học sinh sinh nhật thì 12 tháng chỉ có tối đa 36 học sinh. Do còn dư 4 học sinh nên chắc chắn có ít nhất 1 tháng có từ 3 + 1 = 4 học sinh cùng tháng sinh.",
    ),

    # =========================================================
    # LỚP 7 (6 BÀI)
    # =========================================================
    M(
        7,
        "so-huu-ti",
        "Tập hợp Số hữu tỉ ℚ & Lũy thừa của một số hữu tỉ",
        "➗",
        "Thực hiện thành thạo các phép toán cộng, trừ, nhân, chia và lũy thừa trên tập hợp số hữu tỉ ℚ.",
        "Số hữu tỉ là số viết được dưới dạng phân số a/b với a, b ∈ ℤ, b ≠ 0. Tập hợp các số hữu tỉ được ký hiệu là ℚ (bao gồm cả số nguyên, phân số, số thập phân hữu hạn và số thập phân vô hạn tuần hoàn).",
        "• Biểu diễn số hữu tỉ trên trục số và so sánh hai số hữu tỉ.\n"
        "• Cộng, trừ, nhân, chia số hữu tỉ và quy tắc chuyển vế (khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải đổi dấu số hạng đó).\n"
        "• Các công thức lũy thừa của một số hữu tỉ (lũy thừa của lũy thừa, lũy thừa của một tích, một thương).",
        [
            {
                "category": "I. Quy tắc chuyển vế & Giá trị tuyệt đối",
                "items": [
                    {"name": "Quy tắc chuyển vế", "formula": "x + a = b ⇔ x = b − a  ;  x − a = b ⇔ x = b + a", "note": "Chuyển vế thì đổi dấu"},
                    {"name": "Giá trị tuyệt đối", "formula": "|x| = x nếu x ≥ 0 ; |x| = −x nếu x < 0", "note": "Luôn có |x| ≥ 0 với mọi x ∈ ℚ"},
                ],
            },
            {
                "category": "II. Lũy thừa của một số hữu tỉ (x, y ∈ ℚ; m, n ∈ ℕ)",
                "items": [
                    {"name": "Nhân, chia cùng cơ số", "formula": "xᵐ · xⁿ = xᵐ⁺ⁿ  ;  xᵐ : xⁿ = xᵐ⁻ⁿ (x ≠ 0, m ≥ n)", "note": ""},
                    {"name": "Lũy thừa của lũy thừa", "formula": "(xᵐ)ⁿ = xᵐ·ⁿ", "note": "Nhân hai số mũ"},
                    {"name": "Lũy thừa của một tích / thương", "formula": "(x · y)ⁿ = xⁿ · yⁿ  ;  (x / y)ⁿ = xⁿ / yⁿ (y ≠ 0)", "note": "Cùng số mũ có thể gộp cơ số"},
                ],
            },
        ],
        "Hoàn thiện kỹ năng tính toán phân số, lũy thừa và giải các bài toán tìm x phức tạp.",
        "Tính toán lãi kép, độ cao/độ sâu địa hình và chuyển đổi giữa phân số với số thập phân vô hạn tuần hoàn.",
        "Rút gọn và tính giá trị của biểu thức: A = (8¹⁰ · 15¹⁰) / 120¹⁰ + (−1/2)³.",
        "Ta có (8¹⁰ · 15¹⁰) / 120¹⁰ = (8 · 15)¹⁰ / 120¹⁰ = 120¹⁰ / 120¹⁰ = 1. Mà (−1/2)³ = −1/8. Vậy A = 1 − 1/8 = 7/8.",
        "Tìm tất cả các giá trị của x thỏa mãn: |x − 1/2| = 3/2.",
        ["x = 2", "x = −1", "x = 2 hoặc x = −1", "x = 1 hoặc x = −2"],
        2,
        "So sánh hai lũy thừa lớn mà không dùng máy tính: 2³⁰⁰ và 3²⁰⁰.",
        "Đưa về cùng số mũ 100: 2³⁰⁰ = (2³)¹⁰⁰ = 8¹⁰⁰ ; 3²⁰⁰ = (3²)¹⁰⁰ = 9¹⁰⁰. Vì 8 < 9 nên 8¹⁰⁰ < 9¹⁰⁰, suy ra 2³⁰⁰ < 3²⁰⁰.",
    ),
    M(
        7,
        "ti-le-thuc-so-thuc",
        "Số thực ℝ, Căn bậc hai số học & Tỉ lệ thức - Dãy tỉ số bằng nhau",
        "⚖️",
        "Hiểu số vô tỉ, số thực ℝ, căn bậc hai số học và vận dụng tính chất dãy tỉ số bằng nhau, đại lượng tỉ lệ thuận - nghịch.",
        "Số thực (ℝ) gồm số hữu tỉ (ℚ) và số vô tỉ (𝕀 – các số thập phân vô hạn không tuần hoàn như √2, π). Tỉ lệ thức là đẳng thức của hai tỉ số a/b = c/d.",
        "• Căn bậc hai số học của số a ≥ 0 là số x ≥ 0 sao cho x² = a (ký hiệu √a).\n"
        "• Tỉ lệ thức và tính chất của dãy tỉ số bằng nhau.\n"
        "• Đại lượng tỉ lệ thuận (y = k·x) và đại lượng tỉ lệ nghịch (x·y = a).",
        [
            {
                "category": "I. Căn bậc hai số học & Số thực",
                "items": [
                    {"name": "Căn bậc hai số học", "formula": "x = √a ⇔ {x ≥ 0 và x² = a} (với a ≥ 0)", "note": "Ví dụ: √25 = 5 (không lấy −5)"},
                    {"name": "Liên hệ tập hợp số", "formula": "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ  (ℝ = ℚ ∪ 𝕀)", "note": "Trục số thực lấp đầy hoàn toàn đường thẳng"},
                ],
            },
            {
                "category": "II. Tỉ lệ thức & Dãy tỉ số bằng nhau",
                "items": [
                    {"name": "Tính chất cơ bản của tỉ lệ thức", "formula": "a/b = c/d ⇔ a · d = b · c", "note": "b, d ≠ 0"},
                    {"name": "Tính chất dãy tỉ số bằng nhau", "formula": "a/b = c/d = e/f = (a + c + e)/(b + d + f) = (a − c + e)/(b − d + f)", "note": "Giả thiết các mẫu số đều khác 0"},
                    {"name": "Tỉ lệ thuận & Tỉ lệ nghịch", "formula": "Tỉ lệ thuận: y₁/x₁ = y₂/x₂ = k  ;  Tỉ lệ nghịch: x₁·y₁ = x₂·y₂ = a", "note": ""},
                ],
            },
        ],
        "Công cụ cực mạnh để giải các bài toán chia phần theo tỉ lệ, tính năng suất công nhân và kích thước hình học.",
        "Chia lợi nhuận kinh doanh theo vốn góp của 3 cổ đông, tính thời gian hoàn thành công trình khi tăng số máy móc.",
        "Tìm ba số x, y, z biết x/2 = y/3 = z/5 và x + y + z = 50.",
        "Áp dụng tính chất dãy tỉ số bằng nhau: x/2 = y/3 = z/5 = (x + y + z)/(2 + 3 + 5) = 50/10 = 5. Suy ra: x = 10, y = 15, z = 25.",
        "Cho biết 12 công nhân có năng suất như nhau cùng làm một công việc thì hoàn thành trong 8 ngày. Nếu muốn hoàn thành công việc đó trong 6 ngày thì cần bao nhiêu công nhân?",
        ["9 công nhân", "14 công nhân", "16 công nhân", "18 công nhân"],
        2,
        "Ba lớp 7A, 7B, 7C cùng tham gia trồng cây. Số cây trồng được của ba lớp lần lượt tỉ lệ với 4; 5; 6. Biết hai lần số cây lớp 7A cộng với số cây lớp 7B nhiều hơn số cây lớp 7C là 63 cây. Tính số cây mỗi lớp đã trồng.",
        "Gọi số cây 3 lớp là x, y, z. Ta có x/4 = y/5 = z/6 = 2x/8 và 2x + y − z = 63. Theo tính chất dãy tỉ số bằng nhau: x/4 = y/5 = z/6 = (2x + y − z)/(8 + 5 − 6) = 63/7 = 9. Vậy 7A trồng 36 cây, 7B trồng 45 cây, 7C trồng 54 cây.",
    ),
    M(
        7,
        "dai-so",
        "Biểu thức đại số & Đa thức một biến",
        "🔤",
        "Thu gọn, tìm bậc, hệ số, tính giá trị, tìm nghiệm và thực hiện cộng, trừ, nhân, chia đa thức một biến.",
        "Biểu thức đại số là biểu thức bao gồm các số và các chữ (đại diện cho số) được nối với nhau bởi các phép toán. Đa thức một biến là tổng của những đơn thức của cùng một biến.",
        "• Tính giá trị của biểu thức đại số tại giá trị cho trước của biến.\n"
        "• Thu gọn, sắp xếp đa thức một biến theo lũy thừa giảm (hoặc tăng) của biến.\n"
        "• Xác định bậc, hệ số cao nhất, hệ số tự do của đa thức.\n"
        "• Cộng, trừ, nhân, chia đa thức một biến; tìm nghiệm của đa thức P(x) (giá trị x = a sao cho P(a) = 0).",
        [
            {
                "category": "I. Cấu trúc Đa thức một biến P(x)",
                "items": [
                    {"name": "Dạng thu gọn chuẩn", "formula": "P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ (với aₙ ≠ 0)", "note": "Bậc là n; hệ số cao nhất là aₙ; hệ số tự do là a₀"},
                    {"name": "Nghiệm của đa thức", "formula": "x = x₀ là nghiệm của P(x) ⇔ P(x₀) = 0", "note": "Đa thức bậc n có tối đa n nghiệm"},
                ],
            },
            {
                "category": "II. Phép toán trên Đa thức & Hệ số đặc biệt",
                "items": [
                    {"name": "Nhân đơn thức với đơn thức", "formula": "(a · xᵐ) · (b · xⁿ) = (a · b) · xᵐ⁺ⁿ", "note": "Nhân hệ số với hệ số, cộng số mũ của biến"},
                    {"name": "Tính chất tổng các hệ số", "formula": "Tổng các hệ số của P(x) bằng P(1) ; Hệ số tự do bằng P(0)", "note": "Mẹo kiểm tra nhanh kết quả thu gọn"},
                ],
            },
        ],
        "Chuyển từ tính toán với con số cụ thể sang lập công thức tổng quát dùng cho lập trình, vật lý và kinh tế.",
        "Viết công thức tính tiền cước taxi theo số km, tính diện tích mảnh đất khi thay đổi kích thước biến x.",
        "Cho hai đa thức P(x) = 3x² − 5x + 2 và Q(x) = −3x² + 2x + 7. Tính A(x) = P(x) + Q(x) và tìm nghiệm của A(x).",
        "A(x) = (3x² − 3x²) + (−5x + 2x) + (2 + 7) = −3x + 9. Cho A(x) = 0 ⇔ −3x + 9 = 0 ⇔ x = 3. Vậy x = 3 là nghiệm của A(x).",
        "Cho đa thức M(x) = 4x³ − 2x⁵ + 7x − 1 + 2x⁵. Bậc và hệ số cao nhất của đa thức M(x) sau khi thu gọn lần lượt là:",
        ["Bậc 5, hệ số cao nhất là 2", "Bậc 3, hệ số cao nhất là 4", "Bậc 3, hệ số cao nhất là 7", "Bậc 5, hệ số cao nhất là −2"],
        1,
        "Tìm giá trị của hệ số a để đa thức F(x) = 2x² − ax + 6 có một nghiệm là x = 2. Khi đó hãy tìm nghiệm còn lại của F(x).",
        "Vì x = 2 là nghiệm nên F(2) = 0 ⇔ 2·(2²) − a·2 + 6 = 0 ⇔ 14 − 2a = 0 ⇔ a = 7. Khi đó F(x) = 2x² − 7x + 6 = (x − 2)(2x − 3) = 0 ⇒ nghiệm còn lại là x = 3/2.",
    ),
    M(
        7,
        "hinh-hoc",
        "Góc ở vị trí đặc biệt, Đường thẳng song song, Tam giác bằng nhau & Các đường đồng quy",
        "📐",
        "Nắm vững góc đối đỉnh, góc so le trong - đồng vị, các trường hợp bằng nhau của tam giác và 4 đường đồng quy trong tam giác.",
        "Hình học lớp 7 xây dựng nền tảng suy luận chứng minh hình học qua quan hệ song song, tam giác bằng nhau và bốn tâm đặc biệt của tam giác.",
        "• Hai góc kề bù (tổng 180°), hai góc đối đỉnh (bằng nhau), tia phân giác của một góc.\n"
        "• Dấu hiệu nhận biết và tính chất hai đường thẳng song song (so le trong, đồng vị, trong cùng phía); Tiên đề Euclid.\n"
        "• Tổng ba góc của tam giác (180°), bất đẳng thức tam giác và các trường hợp bằng nhau của tam giác: (c.c.c), (c.g.c), (g.c.g), tam giác vuông (cạnh huyền - góc nhọn, cạnh huyền - cạnh góc vuông).\n"
        "• Bốn đường đồng quy: Trung tuyến (Trọng tâm G), Phân giác (Tâm đường tròn nội tiếp I), Trung trực (Tâm đường tròn ngoại tiếp O), Đường cao (Trực tâm H).",
        [
            {
                "category": "I. Góc, Song song & Bất đẳng thức Tam giác",
                "items": [
                    {"name": "Tổng 3 góc & Góc ngoài tam giác", "formula": "∠A + ∠B + ∠C = 180°  ;  Góc ngoài tại C = ∠A + ∠B", "note": ""},
                    {"name": "Bất đẳng thức tam giác", "formula": "|b − c| < a < b + c", "note": "Độ dài 1 cạnh luôn lớn hơn hiệu và nhỏ hơn tổng 2 cạnh kia"},
                    {"name": "Quan hệ cạnh và góc đối diện", "formula": "BC > AC ⇔ ∠A > ∠B", "note": "Cạnh lớn hơn đối diện với góc lớn hơn"},
                ],
            },
            {
                "category": "II. Bốn đường đồng quy trong Tam giác",
                "items": [
                    {"name": "Ba đường trung tuyến (Trọng tâm G)", "formula": "AG = (2/3) AM ; GM = (1/3) AM ; AG = 2 GM", "note": "M là trung điểm BC; G là tâm khối lượng tam giác"},
                    {"name": "Ba đường phân giác (Điểm I)", "formula": "I cách đều 3 cạnh của tam giác", "note": "I là tâm đường tròn nội tiếp"},
                    {"name": "Ba đường trung trực (Điểm O)", "formula": "OA = OB = OC (O cách đều 3 đỉnh)", "note": "O là tâm đường tròn ngoại tiếp"},
                    {"name": "Ba đường cao (Trực tâm H)", "formula": "Ba đường cao cùng đi qua trực tâm H", "note": "Trong tam giác cân tại A thì A, G, I, O, H thẳng hàng"},
                ],
            },
        ],
        "Giúp chứng minh các tính chất hình học chặt chẽ, xác định vị trí đặt trạm phát sóng cách đều 3 khu dân cư.",
        "Xác định vị trí đặt trạm biến áp cách đều 3 ngôi làng (giao 3 đường trung trực) hoặc đặt đài phun nước cách đều 3 con đường bao quanh công viên (giao 3 đường phân giác).",
        "Cho tam giác ABC có ∠A = 70°, ∠B = 50°. Tia phân giác của góc C cắt AB tại D. Tính số đo góc ∠CDB.",
        "Ta có ∠C = 180° − (70° + 50°) = 60°. Vì CD là phân giác góc C nên ∠ACD = ∠BCD = 60° : 2 = 30°. Trong ΔACD, góc ngoài ∠CDB = ∠A + ∠ACD = 70° + 30° = 100°.",
        "Cho tam giác ABC có đường trung tuyến AM = 12 cm và trọng tâm G. Độ dài đoạn thẳng AG và GM lần lượt là:",
        ["AG = 6 cm, GM = 6 cm", "AG = 8 cm, GM = 4 cm", "AG = 9 cm, GM = 3 cm", "AG = 10 cm, GM = 2 cm"],
        1,
        "Một tam giác cân có độ dài hai cạnh là 4 cm và 9 cm. Hãy tính chu vi của tam giác cân đó và giải thích vì sao chỉ có một trường hợp thỏa mãn.",
        "Nếu cạnh bên là 4 cm thì tổng hai cạnh bên là 4 + 4 = 8 cm < 9 cm (vi phạm bất đẳng thức tam giác). Vậy cạnh bên bắt buộc phải là 9 cm và cạnh đáy là 4 cm. Chu vi tam giác là: 9 + 9 + 4 = 22 (cm).",
    ),
    M(
        7,
        "thong-ke",
        "Biểu đồ đoạn thẳng, Biểu đồ hình quạt tròn & Xác suất của biến cố",
        "📈",
        "Phân tích xu hướng qua biểu đồ đoạn thẳng, tỉ lệ phần trăm trên biểu đồ quạt tròn và tính xác suất cổ điển.",
        "Ở lớp 7, học sinh sử dụng biểu đồ đoạn thẳng để biểu diễn sự thay đổi của một đại lượng theo thời gian, biểu đồ quạt tròn cho cấu trúc tỉ lệ % và tính xác suất của biến cố ngẫu nhiên.",
        "• Đọc và nhận xét xu hướng tăng/giảm trên biểu đồ đoạn thẳng.\n"
        "• Tính số lượng thành phần từ tỉ lệ % trên biểu đồ hình quạt tròn.\n"
        "• Biến cố chắc chắn (P = 1), biến cố không thể (P = 0) và biến cố ngẫu nhiên có đồng khả năng (P = 1/n).",
        [
            {
                "category": "I. Biểu đồ hình quạt tròn & Biểu đồ đoạn thẳng",
                "items": [
                    {"name": "Giá trị của phần quạt chiếm p%", "formula": "Giá trị = Tổng_số × p% = Tổng_số × p / 100", "note": "Tổng các hình quạt luôn bằng 100%"},
                    {"name": "Tốc độ tăng/giảm giữa hai mốc", "formula": "Δy = y₂ − y₁  ;  % Tăng = [(y₂ − y₁) / y₁] × 100%", "note": ""},
                ],
            },
            {
                "category": "II. Xác suất của biến cố",
                "items": [
                    {"name": "Biến cố chắc chắn & Không thể", "formula": "P(Chắc chắn) = 1  ;  P(Không thể) = 0", "note": "0 ≤ P(A) ≤ 1"},
                    {"name": "Xác suất k kết quả thuận lợi trên n kết quả đồng khả năng", "formula": "P(A) = k / n", "note": ""},
                ],
            },
        ],
        "Giúp đọc hiểu biểu đồ nhiệt độ, tăng trưởng kinh tế theo năm và tính xác suất trong các phép thử đồng khả năng.",
        "Theo dõi biến động nhiệt độ trong ngày, cơ cấu chi tiêu gia đình và tính xác suất bốc thăm.",
        "Một hộp có 12 chiếc thẻ cùng loại ghi các số từ 1 đến 12. Rút ngẫu nhiên 1 thẻ. Tính xác suất của biến cố A: 'Số xuất hiện trên thẻ là số nguyên tố'.",
        "Từ 1 đến 12 có 5 số nguyên tố là: {2; 3; 5; 7; 11}. Vậy xác suất của biến cố A là: P(A) = 5/12.",
        "Biểu đồ hình quạt tròn cho biết cơ cấu chi tiêu tháng của một gia đình có tổng thu nhập 25 triệu đồng: Ăn uống 40%, Giáo dục 20%, Sinh hoạt 25%, còn lại là Tiết kiệm. Số tiền gia đình đó tiết kiệm được mỗi tháng là:",
        ["2,5 triệu đồng", "3,75 triệu đồng", "5 triệu đồng", "6,25 triệu đồng"],
        1,
        "Gieo một con xúc xắc cân đối và đồng chất một lần. Tính xác suất của biến cố B: 'Số chấm xuất hiện là ước của 6'.",
        "Các kết quả có thể là {1; 2; 3; 4; 5; 6} (6 kết quả). Các ước của 6 trên mặt xúc xắc là {1; 2; 3; 6} (4 kết quả thuận lợi). Vậy P(B) = 4/6 = 2/3.",
    ),
    M(
        7,
        "ung-dung",
        "Hình lăng trụ đứng & Toán ứng dụng Tài chính - Đời sống",
        "🏦",
        "Tính diện tích xung quanh, thể tích hình lăng trụ đứng và giải bài toán lãi suất, thuế VAT, giá cước bậc thang.",
        "Toán ứng dụng lớp 7 kết hợp hình học không gian (lăng trụ đứng tam giác, lăng trụ đứng tứ giác) với các bài toán tài chính tiêu dùng thực tế.",
        "• Hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng tam giác, lăng trụ đứng tứ giác.\n"
        "• Công thức tính diện tích xung quanh và thể tích hình lăng trụ đứng.\n"
        "• Bài toán thực tế: Tính thuế giá trị gia tăng (VAT), chiết khấu kép, tiền điện theo biểu giá bậc thang và lãi suất ngân hàng.",
        [
            {
                "category": "I. Hình lăng trụ đứng (Tam giác & Tứ giác)",
                "items": [
                    {"name": "Diện tích xung quanh", "formula": "S_xq = C_đáy · h", "note": "C_đáy là chu vi đáy, h là chiều cao lăng trụ"},
                    {"name": "Diện tích toàn phần", "formula": "S_tp = S_xq + 2 · S_đáy", "note": ""},
                    {"name": "Thể tích lăng trụ đứng", "formula": "V = S_đáy · h", "note": "S_đáy là diện tích một mặt đáy"},
                ],
            },
            {
                "category": "II. Công thức Tài chính ứng dụng",
                "items": [
                    {"name": "Lãi đơn sau 1 kỳ hạn", "formula": "Tiền cả gốc lẫn lãi: A = P · (1 + r)", "note": "P: tiền gốc, r: lãi suất (dạng thập phân hoặc %)"},
                    {"name": "Giá sau giảm p% rồi tính thêm thuế VAT q%", "formula": "Giá thanh toán = Giá_niêm_yết · (1 − p%) · (1 + q%)", "note": ""},
                ],
            },
        ],
        "Giúp tính thể tích lều trại, gầu xúc máy đào, bể bơi và tính toán thông minh trong tiêu dùng cá nhân.",
        "Tính diện tích vải bạt may lều cắm trại hình lăng trụ đứng tam giác, tính hóa đơn siêu thị có VAT.",
        "Một chiếc lều cắm trại có dạng hình lăng trụ đứng tam giác với đáy là tam giác cân có cạnh đáy 2 m, chiều cao đáy 1,5 m và chiều dài lều (chiều cao lăng trụ) là 3 m. Tính thể tích không gian bên trong lều.",
        "Diện tích đáy tam giác là: S_đáy = (2 · 1,5) : 2 = 1,5 (m²). Thể tích không gian trong lều là: V = S_đáy · h = 1,5 · 3 = 4,5 (m³).",
        "Bác An gửi tiết kiệm 100 triệu đồng kỳ hạn 1 năm với lãi suất 6,5%/năm. Hết 1 năm, bác An nhận được cả vốn lẫn lãi là bao nhiêu?",
        ["100,65 triệu đồng", "106,5 triệu đồng", "165 triệu đồng", "105,6 triệu đồng"],
        1,
        "Một chiếc laptop có giá niêm yết 20 000 000 đồng (chưa gồm thuế VAT). Cửa hàng đang có chương trình giảm giá 10% trên giá niêm yết, sau đó khách hàng cần đóng thêm 10% thuế VAT tính trên giá đã giảm. Hỏi số tiền thực tế khách phải trả là bao nhiêu?",
        "Giá sau khi giảm 10% là: 20 000 000 · (1 − 0,1) = 18 000 000 (đồng). Tiền sau khi cộng thêm 10% VAT trên giá đã giảm là: 18 000 000 · (1 + 0,1) = 19 800 000 (đồng).",
    ),

    # =========================================================
    # LỚP 8 (6 BÀI)
    # =========================================================
    M(
        8,
        "bieu-thuc",
        "Đa thức nhiều biến & Các phép toán trên Đa thức nhiều biến",
        "🔤",
        "Thu gọn đơn thức, đa thức nhiều biến và thực hiện cộng, trừ, nhân, chia đa thức nhiều biến.",
        "Đơn thức nhiều biến là biểu thức đại số chỉ gồm một số, hoặc một biến, hoặc một tích giữa các số và các biến. Đa thức nhiều biến là một tổng của những đơn thức.",
        "• Đơn thức thu gọn, bậc của đơn thức (tổng số mũ của tất cả các biến) và cộng/trừ các đơn thức đồng dạng.\n"
        "• Thu gọn đa thức nhiều biến, xác định bậc của đa thức (bậc của hạng tử có bậc cao nhất trong dạng thu gọn).\n"
        "• Nhân đơn thức với đa thức, nhân hai đa thức và chia đa thức cho đơn thức.",
        [
            {
                "category": "I. Đơn thức & Đơn thức đồng dạng",
                "items": [
                    {"name": "Bậc của đơn thức A = k · xᵐ · yⁿ · zᵖ (k ≠ 0)", "formula": "Bậc = m + n + p", "note": "Số thực khác 0 là đơn thức bậc 0"},
                    {"name": "Đơn thức đồng dạng", "formula": "k₁ · xᵐyⁿ ± k₂ · xᵐyⁿ = (k₁ ± k₂) · xᵐyⁿ", "note": "Có hệ số khác 0 và có cùng phần biến"},
                ],
            },
            {
                "category": "II. Phép toán trên Đa thức nhiều biến",
                "items": [
                    {"name": "Nhân hai đa thức", "formula": "(A + B)(C + D) = AC + AD + BC + BD", "note": "Nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia"},
                    {"name": "Chia đơn thức cho đơn thức", "formula": "(a · xᵐyⁿ) : (b · xᵖyᵍ) = (a/b) · xᵐ⁻ᵖ · yⁿ⁻ᵍ", "note": "Chia hết khi m ≥ p và n ≥ q (b ≠ 0)"},
                ],
            },
        ],
        "Giúp biểu diễn các đại lượng phụ thuộc đồng thời vào nhiều yếu tố như diện tích, thể tích, doanh thu.",
        "Lập biểu thức tính diện tích bề mặt hộp quà theo chiều dài x, chiều rộng y và chiều cao z.",
        "Thu gọn và tìm bậc của đa thức: P = 3x²y − 5xy² + 2x²y + 5xy² − 7.",
        "P = (3x²y + 2x²y) + (−5xy² + 5xy²) − 7 = 5x²y − 7. Hạng tử 5x²y có bậc là 2 + 1 = 3, nên đa thức P có bậc 3.",
        "Kết quả rút gọn của biểu thức M = x(2x − y) − y(x − 2y) + 2xy là:",
        ["2x² − 2y²", "2x² + 2y²", "2x² + 4xy + 2y²", "2x² − 2xy + 2y²"],
        1,
        "Chứng minh rằng giá trị của biểu thức A = (x − 3)(x + 7) − (x + 5)(x − 1) + 30 không phụ thuộc vào giá trị của biến x.",
        "Khai triển: A = (x² + 4x − 21) − (x² + 4x − 5) + 30 = x² + 4x − 21 − x² − 4x + 5 + 30 = 14 (hằng số không phụ thuộc vào x).",
    ),
    M(
        8,
        "hang-dang-thuc-phan-thuc",
        "7 Hằng đẳng thức đáng nhớ, Phân tích đa thức thành nhân tử & Phân thức đại số",
        "⚡",
        "Làm chủ trọn bộ 7 hằng đẳng thức đáng nhớ, phân tích đa thức thành nhân tử và biến đổi phân thức đại số.",
        "Bảy hằng đẳng thức đáng nhớ là những công cụ biến đổi đại số quan trọng nhất cấp THCS, giúp phân tích đa thức thành nhân tử và rút gọn phân thức đại số A/B (với B ≠ 0).",
        "• Trọn bộ 7 hằng đẳng thức đáng nhớ (bình phương, hiệu hai bình phương, lập phương, tổng/hiệu hai lập phương).\n"
        "• Các phương pháp phân tích đa thức thành nhân tử: Đặt nhân tử chung, dùng hằng đẳng thức, nhóm hạng tử, tách hạng tử.\n"
        "• Phân thức đại số: Điều kiện xác định (mẫu thức khác 0), rút gọn, quy đồng và cộng - trừ - nhân - chia phân thức.",
        [
            {
                "category": "I. Bảy hằng đẳng thức đáng nhớ",
                "items": [
                    {"name": "1. Bình phương của một tổng", "formula": "(A + B)² = A² + 2AB + B²", "note": ""},
                    {"name": "2. Bình phương của một hiệu", "formula": "(A − B)² = A² − 2AB + B²", "note": ""},
                    {"name": "3. Hiệu hai bình phương", "formula": "A² − B² = (A − B)(A + B)", "note": ""},
                    {"name": "4. Lập phương của một tổng", "formula": "(A + B)³ = A³ + 3A²B + 3AB² + B³ = A³ + B³ + 3AB(A + B)", "note": ""},
                    {"name": "5. Lập phương của một hiệu", "formula": "(A − B)³ = A³ − 3A²B + 3AB² − B³ = A³ − B³ − 3AB(A − B)", "note": ""},
                    {"name": "6. Tổng hai lập phương", "formula": "A³ + B³ = (A + B)(A² − AB + B²)", "note": "A² − AB + B² là bình phương thiếu của hiệu"},
                    {"name": "7. Hiệu hai lập phương", "formula": "A³ − B³ = (A − B)(A² + AB + B²)", "note": "A² + AB + B² là bình phương thiếu của tổng"},
                ],
            },
            {
                "category": "II. Phân thức đại số A/B (Điều kiện xác định: B ≠ 0)",
                "items": [
                    {"name": "Tính chất cơ bản & Rút gọn", "formula": "A/B = (A · M)/(B · M) = (A : N)/(B : N)", "note": "Phân tích tử và mẫu thành nhân tử để giản ước"},
                    {"name": "Cộng, trừ, nhân, chia phân thức", "formula": "A/B ± C/B = (A ± C)/B  ;  (A/B) · (C/D) = (AC)/(BD)  ;  (A/B) : (C/D) = (AD)/(BC)", "note": ""},
                ],
            },
        ],
        "Giúp tính nhẩm siêu tốc, tìm giá trị lớn nhất/nhỏ nhất (GTLN/GTNN) của biểu thức và rút gọn các công thức vật lý - kỹ thuật.",
        "Tính nhẩm nhanh 99² hay 52 · 48, tối ưu hóa kích thước vật liệu và tính vận tốc trung bình trên các chặng đường.",
        "Phân tích đa thức P = x² − 2xy + y² − 9 thành nhân tử.",
        "Nhóm 3 hạng tử đầu: P = (x² − 2xy + y²) − 9 = (x − y)² − 3² = (x − y − 3)(x − y + 3).",
        "Với x ≠ ±2, kết quả rút gọn của phân thức Q = (x² − 4x + 4) / (x² − 4) là:",
        ["(x + 2) / (x − 2)", "(x − 2) / (x + 2)", "1", "−2 / (x + 2)"],
        1,
        "Tìm giá trị nhỏ nhất (GTNN) của biểu thức M = x² − 6x + 15.",
        "Biến đổi về bình phương: M = (x² − 6x + 9) + 6 = (x − 3)² + 6. Vì (x − 3)² ≥ 0 với mọi x nên M ≥ 6. Dấu '=' xảy ra khi x = 3. Vậy GTNN của M là 6 tại x = 3.",
    ),
    M(
        8,
        "phuong-trinh",
        "Hàm số bậc nhất y = ax + b & Phương trình bậc nhất một ẩn",
        "📈",
        "Vẽ đồ thị hàm số bậc nhất, xác định hệ số góc và giải bài toán bằng cách lập phương trình bậc nhất một ẩn.",
        "Hàm số bậc nhất có dạng y = ax + b (a ≠ 0) với đồ thị là một đường thẳng có hệ số góc a; phương trình bậc nhất một ẩn có dạng ax + b = 0 (a ≠ 0).",
        "• Mặt phẳng tọa độ Oxy, tọa độ của một điểm M(x₀; y₀).\n"
        "• Đồ thị hàm số y = ax + b (a ≠ 0): nhận biết hai đường thẳng song song, cắt nhau qua hệ số góc.\n"
        "• Giải phương trình bậc nhất một ẩn ax + b = 0, phương trình đưa được về dạng ax + b = 0.\n"
        "• Các bước giải bài toán bằng cách lập phương trình (chuyển động, năng suất, phần trăm).",
        [
            {
                "category": "I. Hàm số bậc nhất y = ax + b (a ≠ 0) & Vị trí hai đường thẳng",
                "items": [
                    {"name": "Giao điểm với hai trục tọa độ", "formula": "Cắt Oy tại A(0; b)  ;  Cắt Ox tại B(−b/a; 0)", "note": "a là hệ số góc, b là tung độ gốc"},
                    {"name": "Quan hệ giữa d: y = ax + b và d': y = a'x + b'", "formula": "Song song: a = a' và b ≠ b' ; Trùng nhau: a = a' và b = b' ; Cắt nhau: a ≠ a'", "note": "Vuông góc: a · a' = −1"},
                ],
            },
            {
                "category": "II. Phương trình bậc nhất một ẩn",
                "items": [
                    {"name": "Phương trình ax + b = 0 (a ≠ 0)", "formula": "ax + b = 0 ⇔ ax = −b ⇔ x = −b/a", "note": "Luôn có nghiệm duy nhất x = −b/a"},
                    {"name": "Phương trình tích", "formula": "A(x) · B(x) = 0 ⇔ A(x) = 0 hoặc B(x) = 0", "note": ""},
                ],
            },
        ],
        "Giúp mô hình hóa các mối quan hệ tuyến tính và tìm đại lượng chưa biết trong bài toán chuyển động, công việc.",
        "Tính cước taxi y = ax + b (b là giá mở cửa, a là giá mỗi km), tìm thời gian dự kiến hoàn thành đơn hàng.",
        "Giải phương trình: (2x − 1)/3 − (x + 2)/4 = 1.",
        "Quy đồng mẫu số chung 12: 4(2x − 1) − 3(x + 2) = 12 ⇔ 8x − 4 − 3x − 6 = 12 ⇔ 5x − 10 = 12 ⇔ 5x = 22 ⇔ x = 22/5.",
        "Đường thẳng d: y = (m − 2)x + 5 song song với đường thẳng d': y = 3x − 1 khi giá trị của m bằng:",
        ["m = 3", "m = 5", "m = 1", "m = −1"],
        1,
        "Một ca nô xuôi dòng từ bến A đến bến B mất 2 giờ và ngược dòng từ B về A mất 3 giờ. Biết vận tốc dòng nước là 3 km/h. Tính vận tốc riêng của ca nô và độ dài quãng sông AB.",
        "Gọi vận tốc riêng của ca nô là x (km/h, x > 3). Vận tốc xuôi dòng là x + 3, ngược dòng là x − 3. Phương trình quãng đường AB: 2(x + 3) = 3(x − 3) ⇔ 2x + 6 = 3x − 9 ⇔ x = 15 (km/h). Quãng sông AB dài: 2 · (15 + 3) = 36 (km).",
    ),
    M(
        8,
        "hinh-hoc",
        "Tứ giác, Định lý Pythagore, Định lý Thalès, Tam giác đồng dạng & Hình chóp đều",
        "📐",
        "Nắm vững hệ thống dấu hiệu nhận biết các tứ giác, định lý Pythagore, định lý Thalès, tam giác đồng dạng và hình chóp đều.",
        "Hình học lớp 8 là trụ cột của hình học phẳng THCS với sơ đồ phả hệ tứ giác, định lý Pythagore, định lý Thalès, tam giác đồng dạng và mở rộng sang hình chóp tam giác đều, tứ giác đều.",
        "• Tứ giác (tổng 4 góc bằng 360°), Hình thang cân, Hình bình hành, Hình chữ nhật, Hình thoi, Hình vuông.\n"
        "• Định lý Pythagore và Pythagore đảo trong tam giác vuông.\n"
        "• Định lý Thalès thuận - đảo, tính chất đường trung bình, tính chất đường phân giác của tam giác.\n"
        "• Ba trường hợp đồng dạng của hai tam giác (c.c.c, c.g.c, g.g) và Hình chóp tam giác đều, hình chóp tứ giác đều.",
        [
            {
                "category": "I. Định lý Pythagore, Định lý Thalès & Đường phân giác",
                "items": [
                    {"name": "Định lý Pythagore (ΔABC vuông tại A)", "formula": "BC² = AB² + AC²", "note": "Ngược lại nếu BC² = AB² + AC² thì ΔABC vuông tại A"},
                    {"name": "Định lý Thalès (DE // BC, D ∈ AB, E ∈ AC)", "formula": "AD/AB = AE/AC = DE/BC  và  AD/DB = AE/EC", "note": "Đường trung bình MN // BC và MN = BC/2"},
                    {"name": "Tính chất đường phân giác AD (D ∈ BC)", "formula": "DB / DC = AB / AC", "note": "Phân giác chia cạnh đối diện tỉ lệ với hai cạnh kề"},
                ],
            },
            {
                "category": "II. Tam giác đồng dạng & Hình chóp đều",
                "items": [
                    {"name": "Tỉ số đồng dạng k (ΔA'B'C' ∽ ΔABC)", "formula": "Tỉ số chu vi/đường cao/trung tuyến = k  ;  Tỉ số diện tích: S' / S = k²", "note": "Diện tích tỉ lệ với bình phương tỉ số đồng dạng"},
                    {"name": "Hình chóp đều (trung đoạn d, chiều cao h)", "formula": "S_xq = p · d (p là nửa chu vi đáy)  ;  V = (1/3) · S_đáy · h", "note": ""},
                ],
            },
        ],
        "Giúp đo chiều cao tòa nhà, cây cối thông qua bóng nắng mà không cần trèo lên, và tính thể tích kim tự tháp, mái nhà.",
        "Đo chiều cao cột cờ bằng bóng nắng (tam giác đồng dạng), kiểm tra góc vuông tường xây bằng bộ số Pythagore (3 - 4 - 5).",
        "Cho tam giác ABC có AB = 6 cm, AC = 9 cm, BC = 10 cm. Đường phân giác góc A cắt BC tại D. Tính độ dài DB và DC.",
        "Theo tính chất đường phân giác: DB/DC = AB/AC = 6/9 = 2/3 ⇒ DB/2 = DC/3 = (DB + DC)/(2 + 3) = 10/5 = 2. Suy ra DB = 4 cm, DC = 6 cm.",
        "Nếu ΔA'B'C' ∽ ΔABC theo tỉ số đồng dạng k = 3 và diện tích ΔABC bằng 10 cm² thì diện tích ΔA'B'C' bằng bao nhiêu?",
        ["30 cm²", "60 cm²", "90 cm²", "100 cm²"],
        2,
        "Một kim tự tháp bằng thủy tinh có dạng hình chóp tứ giác đều với cạnh đáy là 12 cm và chiều cao các mặt bên (trung đoạn) là 10 cm. Hãy tính diện tích xung quanh và thể tích của kim tự tháp đó.",
        "Nửa chu vi đáy: p = (12 · 4) : 2 = 24 (cm) ⇒ S_xq = p · d = 24 · 10 = 240 (cm²). Áp dụng định lý Pythagore cho tam giác vuông tạo bởi đường cao h, trung đoạn d = 10 và nửa cạnh đáy 6 cm: h = √(10² − 6²) = 8 (cm). Diện tích đáy: S_đáy = 12² = 144 (cm²). Thể tích: V = (1/3) · 144 · 8 = 384 (cm³).",
    ),
    M(
        8,
        "thong-ke",
        "Thống kê chọn biểu đồ & Mối liên hệ giữa Xác suất thực nghiệm và Xác suất lý thuyết",
        "📊",
        "Lựa chọn biểu đồ phù hợp với từng loại dữ liệu và kết nối xác suất thực nghiệm với xác suất lý thuyết.",
        "Thống kê lớp 8 hướng dẫn cách chọn đúng loại biểu đồ (cột, cột kép, đoạn thẳng, quạt tròn) để tránh hiểu sai dữ liệu, đồng thời làm rõ quy luật số lớn trong xác suất.",
        "• Khi nào dùng biểu đồ cột, cột kép, đoạn thẳng hay quạt tròn?\n"
        "• Phát hiện những điểm biểu diễn không hợp lý trên biểu đồ.\n"
        "• Khi số lần thực hiện phép thử N càng lớn, xác suất thực nghiệm của biến cố càng tiến gần đến xác suất lý thuyết của biến cố đó.",
        [
            {
                "category": "I. Quy tắc lựa chọn Biểu đồ thống kê",
                "items": [
                    {"name": "Biểu đồ hình quạt tròn", "formula": "Dùng khi muốn biểu diễn TỈ LỆ PHẦN TRĂM các phần trong tổng thể (Tổng = 100%)", "note": ""},
                    {"name": "Biểu đồ đoạn thẳng", "formula": "Dùng khi biểu diễn XU HƯỚNG THAY ĐỔI của một đại lượng theo thời gian", "note": ""},
                    {"name": "Biểu đồ cột / cột kép", "formula": "Dùng khi SO SÁNH độ lớn của nhiều đối tượng hoặc hai nhóm đối tượng", "note": ""},
                ],
            },
            {
                "category": "II. Xác suất lý thuyết & Xác suất thực nghiệm",
                "items": [
                    {"name": "Xác suất lý thuyết (đồng khả năng)", "formula": "P(E) = n(E) / n(Ω)", "note": "n(E): số kết quả thuận lợi; n(Ω): tổng số kết quả có thể"},
                    {"name": "Quy luật số lớn", "formula": "Khi số phép thử N → ∞ thì P_thực_nghiệm(E) ≈ P_lý_thuyết(E)", "note": "Dùng để ước lượng kích thước quần thể"},
                ],
            },
        ],
        "Giúp trình bày báo cáo khoa học chuẩn xác và ứng dụng phương pháp bắt - đánh dấu - thả lại trong sinh thái học.",
        "Ước lượng số lượng cá trong hồ nuôi thông qua xác suất thực nghiệm và thiết kế dashboard báo cáo.",
        "Để ước lượng số cá trong hồ, người ta bắt lên 100 con cá, đánh dấu tất cả rồi thả lại xuống hồ. Hôm sau người ta bắt ngẫu nhiên 80 con cá thì thấy có 8 con có đánh dấu. Hãy ước lượng số cá có trong hồ.",
        "Xác suất thực nghiệm bắt được cá đánh dấu là 8/80 = 1/10. Gọi N là tổng số cá trong hồ, tỉ lệ cá đánh dấu là 100/N ≈ 1/10 ⇒ N ≈ 1000 (con cá).",
        "Muốn biểu diễn cơ cấu diện tích các loại cây trồng (Lúa 55%, Cây ăn quả 30%, Rau màu 15%) của một hợp tác xã, loại biểu đồ nào thích hợp nhất?",
        ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ cột kép", "Biểu đồ tranh"],
        1,
        "Chọn ngẫu nhiên một số tự nhiên có hai chữ số (từ 10 đến 99). Tính xác suất của biến cố A: 'Số được chọn là một số chính phương'.",
        "Từ 10 đến 99 có tất cả (99 − 10) + 1 = 90 số. Các số chính phương có hai chữ số là: {16; 25; 36; 49; 64; 81} (gồm 6 số). Vậy xác suất P(A) = 6/90 = 1/15.",
    ),
    M(
        8,
        "logic",
        "Suy luận Logic, Chứng minh phản chứng & Bất đẳng thức cơ bản",
        "🧠",
        "Rèn luyện kỹ năng lập luận suy diễn, phương pháp phản chứng và đánh giá biểu thức đại số.",
        "Chứng minh toán học đòi hỏi đi từ giả thiết đến kết luận bằng chuỗi suy luận logic hoặc chứng minh giả thiết ngược lại dẫn đến mâu thuẫn (phản chứng).",
        "• Cấu trúc định lý: Giả thiết (GT) ⇒ Kết luận (KL), định lý thuận và định lý đảo.\n"
        "• Phương pháp chứng minh phản chứng.\n"
        "• Kỹ năng biến đổi bình phương không âm A² ≥ 0 để chứng minh bất đẳng thức và tìm cực trị đại số.",
        [
            {
                "category": "I. Suy luận Logic & Phản chứng",
                "items": [
                    {"name": "Suy luận trực tiếp", "formula": "GT ⇒ A₁ ⇒ A₂ ⇒ ... ⇒ KL", "note": ""},
                    {"name": "Chứng minh phản chứng", "formula": "Giả sử trái với KL (¬KL) ⇒ suy ra điều mâu thuẫn với GT hoặc chân lý đã biết ⇒ KL đúng", "note": ""},
                ],
            },
            {
                "category": "II. Đánh giá biểu thức qua Hằng đẳng thức",
                "items": [
                    {"name": "Tính không âm của bình phương", "formula": "A² ≥ 0 với mọi A  ⇒  A² + m ≥ m (GTNN là m)  ;  −A² + M ≤ M (GTLN là M)", "note": "Dấu '=' xảy ra khi A = 0"},
                    {"name": "Bất đẳng thức cơ bản", "formula": "a² + b² ≥ 2ab  ⇔  (a − b)² ≥ 0 (luôn đúng với mọi a, b)", "note": "Dấu '=' xảy ra khi a = b"},
                ],
            },
        ],
        "Phát triển tư duy phản biện, khả năng kiểm chứng thông tin và tìm phương án tối ưu.",
        "Tối ưu hóa lợi nhuận, tìm kích thước chuồng trại có diện tích lớn nhất với chiều dài hàng rào cố định.",
        "Tìm giá trị lớn nhất (GTLN) của biểu thức P = −x² + 4x + 7.",
        "Ta có: P = −(x² − 4x + 4) + 11 = −(x − 2)² + 11. Vì −(x − 2)² ≤ 0 với mọi x nên P ≤ 11. Dấu '=' xảy ra khi x = 2. Vậy GTLN của P là 11 tại x = 2.",
        "Cho hai số thực x, y thỏa mãn (x − 2)² + (y + 3)² = 0. Khi đó giá trị của biểu thức T = x + y bằng:",
        ["5", "−5", "−1", "1"],
        2,
        "Bác nông dân có 40 m lưới thép muốn quây thành một khu vườn hình chữ nhật (quây cả 4 cạnh). Hỏi bác nên chọn chiều dài và chiều rộng bằng bao nhiêu mét để diện tích khu vườn là lớn nhất?",
        "Gọi một kích thước là x (m, 0 < x < 20). Nửa chu vi là 40 : 2 = 20 (m), nên kích thước kia là 20 − x (m). Diện tích: S = x(20 − x) = −x² + 20x = −(x − 10)² + 100 ≤ 100 (m²). Diện tích lớn nhất bằng 100 m² khi x = 10 m (khu vườn là hình vuông cạnh 10 m).",
    ),

    # =========================================================
    # LỚP 9 (6 BÀI)
    # =========================================================
    M(
        9,
        "can-thuc",
        "Căn bậc hai, Căn bậc ba & Các phép biến đổi Căn thức đại số",
        "√",
        "Nắm vững điều kiện xác định của căn thức, trục căn thức ở mẫu và rút gọn biểu thức chứa căn bậc hai, căn bậc ba.",
        "Căn thức bậc hai √A xác định (có nghĩa) khi và chỉ khi A ≥ 0. Hằng đẳng thức nền tảng là √(A²) = |A|. Căn bậc ba ³√A xác định với mọi số thực A.",
        "• Điều kiện xác định của √A là A ≥ 0; của 1/√A là A > 0.\n"
        "• Liên hệ giữa phép nhân, phép chia và phép khai phương.\n"
        "• Đưa thừa số ra ngoài/vào trong dấu căn, khử mẫu của biểu thức lấy căn và trục căn thức ở mẫu (nhân lượng liên hợp).\n"
        "• Căn bậc ba: (³√A)³ = ³√(A³) = A với mọi A ∈ ℝ.",
        [
            {
                "category": "I. Hằng đẳng thức & Phép biến đổi Căn bậc hai",
                "items": [
                    {"name": "Điều kiện xác định & Hằng đẳng thức", "formula": "√A xác định ⇔ A ≥ 0  ;  √(A²) = |A|", "note": "|A| = A nếu A ≥ 0; |A| = −A nếu A < 0"},
                    {"name": "Khai phương một tích & một thương", "formula": "√(A · B) = √A · √B (A, B ≥ 0)  ;  √(A / B) = √A / √B (A ≥ 0, B > 0)", "note": ""},
                    {"name": "Đưa thừa số ra ngoài dấu căn", "formula": "√(A² · B) = |A| · √B (với B ≥ 0)", "note": ""},
                ],
            },
            {
                "category": "II. Trục căn thức ở mẫu (Lượng liên hợp) & Căn bậc ba",
                "items": [
                    {"name": "Trục căn thức dạng đơn", "formula": "A / √B = (A√B) / B (với B > 0)", "note": ""},
                    {"name": "Nhân lượng liên hợp", "formula": "C / (√A ± √B) = C(√A ∓ √B) / (A − B) (với A, B ≥ 0 và A ≠ B)", "note": "Áp dụng (√A − √B)(√A + √B) = A − B"},
                    {"name": "Căn bậc ba", "formula": "x = ³√A ⇔ x³ = A  ;  ³√(A³) = A (với mọi A ∈ ℝ)", "note": "Căn bậc ba giữ nguyên dấu của A"},
                ],
            },
        ],
        "Công cụ thiết yếu trong các bài toán rút gọn biểu thức thi vào lớp 10 và tính toán vật lý, hình học.",
        "Tính chu kỳ con lắc đơn T = 2π√(l/g), tốc độ vũ trụ cấp I v = √(gR) và đường chéo màn hình tivi.",
        "Rút gọn biểu thức: A = √( (2 − √5)² ) + 4 / (√5 − 1).",
        "Vì 2 = √4 < √5 nên |2 − √5| = √5 − 2. Trục căn thức: 4/(√5 − 1) = 4(√5 + 1)/(5 − 1) = √5 + 1. Vậy A = (√5 − 2) + (√5 + 1) = 2√5 − 1.",
        "Với x ≥ 0 và x ≠ 4, kết quả rút gọn của biểu thức P = [ 1/(√x − 2) + 1/(√x + 2) ] · (x − 4)/√x là:",
        ["1", "2", "2√x", "√x / 2"],
        1,
        "Tính giá trị của biểu thức S = 1/(1 + √2) + 1/(√2 + √3) + 1/(√3 + √4) + ... + 1/(√99 + √100).",
        "Trục căn thức từng số hạng: 1/(√k + √(k+1)) = √(k+1) − √k. Do đó S = (√2 − 1) + (√3 − √2) + (√4 − √3) + ... + (√100 − √99) = √100 − 1 = 10 − 1 = 9.",
    ),
    M(
        9,
        "ham-so",
        "Hàm số bậc hai y = ax² (a ≠ 0) & Sự tương giao giữa Parabol và Đường thẳng",
        "📈",
        "Khảo sát tính chất, vẽ đồ thị Parabol y = ax² và giải bài toán giao điểm giữa Parabol (P) với đường thẳng (d).",
        "Hàm số y = ax² (a ≠ 0) có đồ thị là một đường cong Parabol đi qua gốc tọa độ O(0; 0) và nhận trục tung Oy làm trục đối xứng.",
        "• Tính chất biến thiên của hàm số y = ax² theo dấu của hệ số a (a > 0 và a < 0).\n"
        "• Cách lập bảng giá trị (thường lấy 5 điểm đối xứng qua O) và vẽ Parabol (P).\n"
        "• Phương trình hoành độ giao điểm của Parabol (P): y = ax² và đường thẳng (d): y = mx + n là ax² − mx − n = 0.",
        [
            {
                "category": "I. Tính chất và Đồ thị hàm số y = ax² (a ≠ 0)",
                "items": [
                    {"name": "Trường hợp a > 0", "formula": "Đồ thị nằm phía TRÊN trục hoành; O(0;0) là điểm thấp nhất (y_min = 0)", "note": "x < 0: nghịch biến ; x > 0: đồng biến"},
                    {"name": "Trường hợp a < 0", "formula": "Đồ thị nằm phía DƯỚI trục hoành; O(0;0) là điểm cao nhất (y_max = 0)", "note": "x < 0: đồng biến ; x > 0: nghịch biến"},
                ],
            },
            {
                "category": "II. Tương giao giữa (P): y = ax² và (d): y = mx + n",
                "items": [
                    {"name": "Phương trình hoành độ giao điểm", "formula": "ax² = mx + n ⇔ ax² − mx − n = 0 (*)", "note": "Số giao điểm bằng số nghiệm của (*)"},
                    {"name": "Điều kiện cắt nhau / tiếp xúc", "formula": "Δ > 0: cắt tại 2 điểm phân biệt ; Δ = 0: tiếp xúc (1 điểm chung) ; Δ < 0: không giao nhau", "note": ""},
                ],
            },
        ],
        "Mô tả quỹ đạo chuyển động ném xiên, chảo thu sóng vệ tinh Parabol, gương phản xạ đèn pha ô tô và cổng vòm kiến trúc.",
        "Tính quỹ đạo bóng rổ, độ cao vòm cầu Parabol và quãng đường phanh xe tỉ lệ với bình phương vận tốc (s = k·v²).",
        "Cho Parabol (P): y = x² và đường thẳng (d): y = 2x + 3. Tìm tọa độ các giao điểm của (P) và (d).",
        "Phương trình hoành độ giao điểm: x² = 2x + 3 ⇔ x² − 2x − 3 = 0 ⇔ (x + 1)(x − 3) = 0 ⇔ x = −1 (⇒ y = 1) hoặc x = 3 (⇒ y = 9). Vậy hai giao điểm là A(−1; 1) và B(3; 9).",
        "Điểm nào dưới đây thuộc đồ thị hàm số (P): y = −(1/2)x²?",
        ["M(2; 2)", "N(−2; −2)", "P(4; −4)", "Q(−4; 8)"],
        1,
        "Một cổng chào có hình dạng một Parabol y = ax² (với gốc tọa độ O tại đỉnh cao nhất của cổng, trục Oy hướng thẳng đứng xuống đất). Biết cổng cao 8 m và khoảng cách giữa hai chân cổng trên mặt đất là 8 m. Hãy xác định hệ số a và tính chiều cao của cổng tại vị trí cách trục đối xứng 2 m.",
        "Chân cổng cách trục đối xứng 8 : 2 = 4 m và ở độ sâu 8 m so với đỉnh, nên đi qua điểm (4; 8) ⇒ 8 = a · 4² ⇒ a = 1/2. Tại vị trí cách trục đối xứng x = 2 m, khoảng cách từ đỉnh cổng xuống là y = (1/2) · 2² = 2 (m). Vậy chiều cao cổng tại vị trí đó tính từ mặt đất là: 8 − 2 = 6 (m).",
    ),
    M(
        9,
        "phuong-trinh",
        "Phương trình quy về bậc nhất, Hệ hai phương trình bậc nhất hai ẩn & Phương trình bậc hai",
        "⚖️",
        "Giải hệ phương trình bậc nhất hai ẩn bằng phương pháp thế - cộng đại số và giải phương trình bậc hai một ẩn.",
        "Hệ hai phương trình bậc nhất hai ẩn (x, y) cho phép tìm đồng thời hai đại lượng chưa biết; phương trình bậc hai ax² + bx + c = 0 (a ≠ 0) được giải tổng quát nhờ biệt thức Δ (Delta).",
        "• Phương trình tích và phương trình chứa ẩn ở mẫu (chú ý đặt điều kiện xác định).\n"
        "• Giải hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế và phương pháp cộng đại số.\n"
        "• Công thức nghiệm và công thức nghiệm thu gọn (Δ') của phương trình bậc hai ax² + bx + c = 0 (a ≠ 0).",
        [
            {
                "category": "I. Hệ hai phương trình bậc nhất hai ẩn",
                "items": [
                    {"name": "Dạng tổng quát", "formula": "{ a₁x + b₁y = c₁  ;  a₂x + b₂y = c₂ }", "note": "Giải bằng phương pháp thế hoặc cộng đại số"},
                    {"name": "Điều kiện số nghiệm (khi a₂, b₂, c₂ ≠ 0)", "formula": "a₁/a₂ ≠ b₁/b₂: 1 nghiệm duy nhất ; a₁/a₂ = b₁/b₂ ≠ c₁/c₂: vô nghiệm ; a₁/a₂ = b₁/b₂ = c₁/c₂: vô số nghiệm", "note": ""},
                ],
            },
            {
                "category": "II. Công thức nghiệm Phương trình bậc hai ax² + bx + c = 0 (a ≠ 0)",
                "items": [
                    {"name": "Biệt thức Δ (Delta)", "formula": "Δ = b² − 4ac", "note": "Nếu b = 2b' thì dùng Δ' = b'² − ac"},
                    {"name": "Trường hợp Δ > 0 (2 nghiệm phân biệt)", "formula": "x₁ = (−b + √Δ) / (2a)  ;  x₂ = (−b − √Δ) / (2a)", "note": "Với Δ': x₁,₂ = (−b' ± √Δ') / a"},
                    {"name": "Trường hợp Δ = 0 (Nghiệm kép) & Δ < 0", "formula": "Δ = 0 ⇒ x₁ = x₂ = −b / (2a)  ;  Δ < 0 ⇒ Phương trình vô nghiệm thực", "note": ""},
                    {"name": "Nhẩm nghiệm nhanh", "formula": "Nếu a + b + c = 0 ⇒ x₁ = 1, x₂ = c/a ; Nếu a − b + c = 0 ⇒ x₁ = −1, x₂ = −c/a", "note": "Rất hữu ích khi thi cử"},
                ],
            },
        ],
        "Giải quyết hầu hết các bài toán thực tế có hai ẩn số và các bài toán chuyển động, hình học dẫn đến phương trình bậc hai.",
        "Tìm giá hai mặt hàng khi biết hóa đơn của hai người mua, tính kích thước mảnh đất khi biết chu vi và diện tích.",
        "Giải hệ phương trình: { 2x + 3y = 13 ; 3x − y = 3 }.",
        "Từ phương trình (2) suy ra y = 3x − 3. Thế vào (1): 2x + 3(3x − 3) = 13 ⇔ 11x − 9 = 13 ⇔ 11x = 22 ⇔ x = 2. Suy ra y = 3(2) − 3 = 3. Vậy nghiệm của hệ là (x; y) = (2; 3).",
        "Phương trình bậc hai 2x² − 7x + 5 = 0 có hai nghiệm là:",
        ["x₁ = 1 ; x₂ = 5/2", "x₁ = −1 ; x₂ = −5/2", "x₁ = 1 ; x₂ = −5/2", "x₁ = 2 ; x₂ = 5"],
        0,
        "Hai vòi nước cùng chảy vào một bể cạn thì sau 4 giờ 48 phút đầy bể. Nếu mở vòi thứ nhất trong 3 giờ và vòi thứ hai trong 4 giờ thì chảy được 3/4 bể. Hỏi nếu mỗi vòi chảy riêng một mình thì mất bao lâu mới đầy bể?",
        "Đổi 4 giờ 48 phút = 24/5 giờ. Gọi thời gian vòi 1, vòi 2 chảy riêng đầy bể là x, y (giờ, x, y > 24/5). Mỗi giờ hai vòi chảy được 1/x và 1/y bể. Ta có hệ: { 1/x + 1/y = 5/24 ; 3/x + 4/y = 3/4 }. Giải hệ được 1/x = 1/12 và 1/y = 1/8 ⇒ x = 12 (giờ), y = 8 (giờ).",
    ),
    M(
        9,
        "he-thuc-viete-hinh-khong-gian",
        "Bất phương trình, Định lý Viète & Hình học không gian (Trụ - Nón - Cầu)",
        "🌐",
        "Áp dụng Định lý Viète cho phương trình bậc hai, giải bất phương trình bậc nhất và tính diện tích, thể tích Hình trụ, Hình nón, Hình cầu.",
        "Chuyên đề kết hợp ba mảng kiến thức trọng tâm lớp 9: Bất đẳng thức - Bất phương trình bậc nhất một ẩn, Định lý Viète và các khối tròn xoay trong không gian (Trụ, Nón, Cầu).",
        "• Liên hệ giữa thứ tự với phép cộng và phép nhân (nhân/chia hai vế bất đẳng thức với số âm phải đổi chiều).\n"
        "• Định lý Viète (tổng và tích hai nghiệm) và bài toán tìm hai số khi biết tổng S, tích P.\n"
        "• Công thức tính diện tích xung quanh, diện tích toàn phần và thể tích của Hình trụ, Hình nón và Hình cầu.",
        [
            {
                "category": "I. Bất đẳng thức & Bất phương trình bậc nhất",
                "items": [
                    {"name": "Nhân hai vế với số c", "formula": "Nếu a < b và c > 0 ⇒ a·c < b·c  ;  Nếu a < b và c < 0 ⇒ a·c > b·c (ĐỔI CHIỀU)", "note": "Quy tắc quan trọng nhất khi giải bất phương trình"},
                ],
            },
            {
                "category": "II. Định lý Viète (cho ax² + bx + c = 0 có Δ ≥ 0)",
                "items": [
                    {"name": "Tổng và tích hai nghiệm", "formula": "S = x₁ + x₂ = −b / a  ;  P = x₁ · x₂ = c / a", "note": ""},
                    {"name": "Biểu thức đối xứng thường gặp", "formula": "x₁² + x₂² = S² − 2P  ;  (x₁ − x₂)² = S² − 4P  ;  x₁³ + x₂³ = S³ − 3SP", "note": "Biểu diễn qua S và P mà không cần giải nghiệm"},
                ],
            },
            {
                "category": "III. Hình trụ, Hình nón & Hình cầu (bán kính R, cao h, đường sinh l)",
                "items": [
                    {"name": "Hình trụ", "formula": "S_xq = 2πRh  ;  S_tp = 2πRh + 2πR²  ;  V = πR²h", "note": ""},
                    {"name": "Hình nón (l = √(R² + h²))", "formula": "S_xq = πRl  ;  S_tp = πRl + πR²  ;  V = (1/3)πR²h", "note": ""},
                    {"name": "Hình cầu (Mặt cầu)", "formula": "Diện tích mặt cầu: S = 4πR²  ;  Thể tích khối cầu: V = (4/3)πR³", "note": ""},
                ],
            },
        ],
        "Giúp giải các bài toán tham số m trong đề thi tuyển sinh vào lớp 10 và tính toán dung tích bồn chứa, lon nước, quả địa cầu.",
        "Thiết kế vỏ lon nước giải khát hình trụ, nón lá truyền thống và bồn chứa khí gas hình cầu.",
        "Cho phương trình x² − 5x + 3 = 0 có hai nghiệm x₁, x₂. Không giải phương trình, hãy tính giá trị của biểu thức A = x₁² + x₂².",
        "Vì Δ = (−5)² − 4·1·3 = 13 > 0 nên phương trình có 2 nghiệm. Theo định lý Viète: S = x₁ + x₂ = 5 và P = x₁x₂ = 3. Ta có A = x₁² + x₂² = S² − 2P = 5² − 2·3 = 19.",
        "Một quả bóng đá có dạng hình cầu với bán kính R = 10 cm (lấy π ≈ 3,14). Diện tích bề mặt của quả bóng đó là bao nhiêu?",
        ["314 cm²", "628 cm²", "1 256 cm²", "4 186,67 cm²"],
        2,
        "Tìm tất cả các giá trị của tham số m để phương trình x² − 2(m + 1)x + m² + 2 = 0 có hai nghiệm phân biệt x₁, x₂ thỏa mãn x₁² + x₂² = 10.",
        "Ta có Δ' = (m + 1)² − (m² + 2) = 2m − 1. Để có 2 nghiệm phân biệt thì Δ' > 0 ⇔ m > 1/2. Theo Viète: S = 2(m + 1), P = m² + 2. Khi đó x₁² + x₂² = S² − 2P = 4(m + 1)² − 2(m² + 2) = 2m² + 8m = 10 ⇔ m² + 4m − 5 = 0 ⇔ m = 1 (nhận vì 1 > 1/2) hoặc m = −5 (loại). Vậy m = 1.",
    ),
    M(
        9,
        "hinh-hoc",
        "Hệ thức lượng trong tam giác vuông, Tỉ số lượng giác & Đường tròn - Tứ giác nội tiếp",
        "⭕",
        "Làm chủ tỉ số lượng giác (sin, cos, tan, cot), hệ thức lượng trong tam giác vuông và các định lý về Đường tròn, Tứ giác nội tiếp.",
        "Hình học phẳng lớp 9 tập trung vào hai chủ đề lớn: Hệ thức lượng & Tỉ số lượng giác trong tam giác vuông và Hình học Đường tròn (góc ở tâm, góc nội tiếp, tiếp tuyến, tứ giác nội tiếp).",
        "• Tỉ số lượng giác của góc nhọn: sin, cos, tan, cot và hệ thức giữa cạnh và góc trong tam giác vuông.\n"
        "• Hệ thức lượng trong tam giác vuông (với đường cao AH ứng với cạnh huyền BC).\n"
        "• Đường tròn: Liên hệ dây và khoảng cách đến tâm, tính chất hai tiếp tuyến cắt nhau, góc ở tâm, góc nội tiếp, độ dài cung và diện tích hình quạt tròn.\n"
        "• Tứ giác nội tiếp đường tròn và các dấu hiệu nhận biết.",
        [
            {
                "category": "I. Tỉ số lượng giác & Hệ thức lượng trong ΔABC vuông tại A (đường cao AH)",
                "items": [
                    {"name": "Tỉ số lượng giác góc nhọn α", "formula": "sin α = Đối / Huyền ; cos α = Kề / Huyền ; tan α = Đối / Kề ; cot α = Kề / Đối", "note": "sin²α + cos²α = 1 ; tan α · cot α = 1"},
                    {"name": "Hệ thức lượng trong tam giác vuông", "formula": "AB² = BH · BC ; AH² = BH · CH ; AB · AC = BC · AH ; 1/AH² = 1/AB² + 1/AC²", "note": ""},
                ],
            },
            {
                "category": "II. Đường tròn (O; R), Góc nội tiếp & Tứ giác nội tiếp",
                "items": [
                    {"name": "Góc ở tâm & Góc nội tiếp cùng chắn cung n°", "formula": "Góc ở tâm = n°  ;  Góc nội tiếp = n° / 2 = (1/2) Góc ở tâm", "note": "Góc nội tiếp chắn nửa đường tròn bằng 90°"},
                    {"name": "Hai tiếp tuyến cắt nhau tại M (tiếp điểm A, B)", "formula": "MA = MB ; MO là tia phân giác ∠AMB ; OM là trung trực của AB", "note": ""},
                    {"name": "Tứ giác nội tiếp ABCD", "formula": "∠A + ∠C = 180° và ∠B + ∠D = 180° (Tổng hai góc đối bằng 180°)", "note": "Hoặc hai đỉnh kề nhau cùng nhìn 1 cạnh dưới 2 góc bằng nhau"},
                    {"name": "Độ dài cung l & Diện tích quạt tròn S_q (góc n°)", "formula": "l = (πRn) / 180  ;  S_q = (πR²n) / 360 = (l · R) / 2", "note": ""},
                ],
            },
        ],
        "Giúp đo khoảng cách từ tàu biển vào hải đăng, chiều cao tháp truyền hình bằng giác kế và giải câu hình học tổng hợp thi vào lớp 10.",
        "Đo chiều cao tòa tháp từ góc nâng của tia nắng mặt trời, thiết kế cầu vòm và bánh răng cơ khí.",
        "Một chiếc thang dài 5 m đặt dựa vào tường sao cho chân thang cách chân tường 2,5 m. Tính góc tạo bởi chiếc thang và mặt đất.",
        "Gọi góc giữa thang và mặt đất là α. Trong tam giác vuông, ta có cos α = Kề / Huyền = 2,5 / 5 = 1/2 ⇒ α = 60°.",
        "Cho đường tròn (O; 6 cm) và cung AB có số đo bằng 60°. Diện tích hình quạt tròn OAB giới hạn bởi hai bán kính OA, OB và cung AB là:",
        ["2π cm²", "6π cm²", "12π cm²", "36π cm²"],
        1,
        "Từ điểm M nằm ngoài đường tròn (O; R) với OM = 2R, kẻ hai tiếp tuyến MA, MB tới đường tròn (A, B là hai tiếp điểm). Tính độ dài đoạn thẳng AB theo R và số đo góc ∠AMB.",
        "Trong ΔOAM vuông tại A: AM = √(OM² − OA²) = √(4R² − R²) = R√3 ; sin(∠AMO) = OA/OM = R/(2R) = 1/2 ⇒ ∠AMO = 30° ⇒ ∠AMB = 2 · 30° = 60°. Vì MA = MB và ∠AMB = 60° nên ΔMAB là tam giác đều, suy ra AB = MA = R√3.",
    ),
    M(
        9,
        "toan-thuc-te",
        "Mô hình hóa Toán thực tế tổng hợp & Ôn thi vào lớp 10",
        "🚀",
        "Tổng hợp kỹ năng lập phương trình, hệ phương trình, lượng giác, hình không gian và xác suất cho kỳ thi tuyển sinh vào lớp 10.",
        "Toán thực tế lớp 9 tích hợp đại số, hàm số, lượng giác, hình học không gian và thống kê - xác suất để giải quyết các bài toán thực tiễn hoàn chỉnh.",
        "• Bài toán thực tế giải bằng hệ phương trình hoặc phương trình bậc hai (năng suất, vòi nước, chuyển động, lãi suất, khuyến mãi).\n"
        "• Bài toán thực tế ứng dụng tỉ số lượng giác góc nhọn (tính chiều cao, khoảng cách không tới được).\n"
        "• Bài toán tối ưu hóa thực tế và thống kê tần số - tần số tương đối.",
        [
            {
                "category": "I. Mô hình Chuyển động, Năng suất & Dung dịch",
                "items": [
                    {"name": "Bài toán làm chung - làm riêng", "formula": "1/t₁ + 1/t₂ = 1/t_chung", "note": "Coi toàn bộ công việc là 1 đơn vị"},
                    {"name": "Bài toán nồng độ dung dịch", "formula": "C% = (m_chất_tan / m_dung_dịch) × 100%", "note": ""},
                ],
            },
            {
                "category": "II. Đo chiều cao bằng hai góc nhìn α, β (α < β)",
                "items": [
                    {"name": "Chiều cao H khi tiến lại gần đoạn d", "formula": "d = H · cot α − H · cot β  ⇒  H = d / (cot α − cot β)", "note": "Ứng dụng đo đỉnh núi, tháp cao từ hai vị trí"},
                ],
            },
        ],
        "Trang bị tư duy giải quyết vấn đề toàn diện cho kỳ thi tuyển sinh lớp 10 và thực tiễn đời sống.",
        "Tính toán kế hoạch sản xuất của nhà máy, đo độ cao máy bay bằng radar và tối ưu giá vé để đạt doanh thu cực đại.",
        "Một rạp chiếu phim bán vé với giá 80 000 đồng/vé thì trung bình có 200 khách mỗi suất. Cứ giảm giá vé 5 000 đồng thì số khách tăng thêm 20 người. Hỏi rạp nên định giá vé bao nhiêu để doanh thu một suất chiếu là lớn nhất?",
        "Gọi x là số lần giảm 5 000 đồng (x ≥ 0). Giá vé mới là (80 − 5x) nghìn đồng; số khách là (200 + 20x) người. Doanh thu R(x) = (80 − 5x)(200 + 20x) = −100x² + 600x + 16 000 = −100(x − 3)² + 16 900 ≤ 16 900 (nghìn đồng). Doanh thu lớn nhất đạt 16 900 000 đồng khi x = 3, tức giá vé là 80 000 − 15 000 = 65 000 đồng.",
        "Từ đỉnh một ngọn hải đăng cao 45 m so với mực nước biển, người quan sát nhìn thấy một con tàu dưới góc hạ 30° so với phương nằm ngang. Khoảng cách từ con tàu đến chân hải đăng là (làm tròn đến mét):",
        ["26 m", "45 m", "78 m", "90 m"],
        2,
        "Theo kế hoạch, một xưởng may phải may xong 360 bộ quần áo trong một thời gian quy định. Đến khi thực hiện, mỗi ngày xưởng đã may nhiều hơn 4 bộ so với kế hoạch nên đã hoàn thành sớm hơn 1 ngày. Hỏi theo kế hoạch, mỗi ngày xưởng phải may bao nhiêu bộ quần áo?",
        "Gọi số bộ quần áo may mỗi ngày theo kế hoạch là x (bộ, x ∈ ℕ*). Thời gian kế hoạch là 360/x (ngày); thời gian thực tế là 360/(x + 4) (ngày). Ta có phương trình: 360/x − 360/(x + 4) = 1 ⇔ 360(x + 4) − 360x = x(x + 4) ⇔ x² + 4x − 1440 = 0 ⇔ (x − 36)(x + 40) = 0 ⇒ x = 36 (bộ/ngày).",
    ),
]


def main():
    db = SessionLocal()
    try:
        subject = db.scalar(select(Subject).where(Subject.slug == SUBJECT_SLUG))
        if subject is None:
            subject = Subject(slug=SUBJECT_SLUG, name=SUBJECT_NAME)
            db.add(subject)
            db.flush()
            print(f"[CREATE] Tạo subject {SUBJECT_NAME}, ID = {subject.id}")
        else:
            print(f"[OK] Tìm thấy subject {SUBJECT_NAME}, ID = {subject.id}")

        created = 0
        updated = 0

        for item in LESSONS:
            lesson = db.scalar(
                select(Lesson).where(
                    Lesson.subject_id == subject.id,
                    Lesson.grade == item["grade"],
                    Lesson.topic == item["topic"],
                )
            )

            if lesson is None:
                lesson = Lesson(
                    subject_id=subject.id,
                    grade=item["grade"],
                    topic=item["topic"],
                    title=item["title"],
                )
                db.add(lesson)
                created += 1
                status = "CREATE"
            else:
                updated += 1
                status = "UPDATE"

            for key, value in item.items():
                if hasattr(lesson, key):
                    setattr(lesson, key, value)

            print(f"[{status}] Lớp {item['grade']} | {item['topic']} | {item['title']}")

        db.commit()

        print("\n" + "=" * 60)
        print(f"ĐÃ XỬ LÝ: {len(LESSONS)} BÀI TOÁN LỚP 1–9")
        print(f"TẠO MỚI:  {created}")
        print(f"CẬP NHẬT: {updated}")
        print("=" * 60)

    except Exception as e:
        db.rollback()
        print("\n" + "=" * 60)
        print("LỖI KHI CẬP NHẬT TOÁN 1–9:")
        print(e)
        print("=" * 60)
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()