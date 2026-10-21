import os
import sys
from pathlib import Path

# Tự động xác định thư mục `backend/` và `backend/tools/` dù đặt file ở đâu hay chạy từ đâu
_CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = _CURRENT_DIR.parent if _CURRENT_DIR.name == "tools" else _CURRENT_DIR
TOOLS_DIR = BACKEND_DIR / "tools"

for _p in ( TOOLS_DIR, BACKEND_DIR ):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# Chuyển working directory về `backend/` để đường dẫn SQLite tương đối (sqlite:///./...) luôn khớp với FastAPI
os.chdir(BACKEND_DIR)

try:
    from dotenv import load_dotenv
    _env_path = BACKEND_DIR / ".env"
    if _env_path.exists():
        load_dotenv(dotenv_path=_env_path, override=True)
except ImportError:
    pass

# Tương thích tự động kiểu JSONB của PostgreSQL khi chạy trên SQLite
try:
    from sqlalchemy.dialects.sqlite.base import SQLiteTypeCompiler
    if not hasattr(SQLiteTypeCompiler, "visit_JSONB"):
        SQLiteTypeCompiler.visit_JSONB = SQLiteTypeCompiler.visit_JSON
except Exception:
    pass

"""
Nâng cấp toàn diện nội dung Toán THPT Lớp 10–12 (Chương trình GDPT 2018 + Chuyên đề nâng cao).
Tổng cộng: 24 bài học (3 lớp × 8 chuyên đề/lớp), bao gồm:
- 18 chuyên đề cốt lõi ban đầu (hợp nhất từ upgrade_math_10_12.py và upgrade_lesson_content.py).
- 6 chuyên đề trọng tâm bổ sung mới theo chương trình GDPT 2018:
  + Lớp 10: bat-phuong-trinh (Bất phương trình & Quy hoạch tuyến tính), to-hop-xac-suat (Đại số tổ hợp, Nhị thức Newton & Xác suất cổ điển)
  + Lớp 11: day-so-cap-so (Dãy số, Cấp số cộng & Cấp số nhân), mu-logarit (Hàm số, Phương trình & Bất phương trình Mũ - Lôgarit)
  + Lớp 12: tich-phan (Tích phân & Ứng dụng diện tích, thể tích), thong-ke-ghep-nhom (Các số đặc trưng đo độ phân tán mẫu số liệu ghép nhóm)

Chạy từ thư mục backend:
    python upgrade_math_10_12.py
"""

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject

SUBJECT_SLUG = "math"
SUBJECT_NAME = "Toán"


def format_formulas_text(formulas_structured):
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
        "game_title": game_title or f"Mô phỏng tương tác: {title}",
        "game_description": game_description
        or f"Khám phá và vận dụng {title.lower()} trong bài toán thực tiễn.",
        "game_type": game_type,
    }


LESSONS = [
    # =========================================================
    # TOÁN 10 (8 BÀI)
    # =========================================================
    M(
        10,
        "menh-de",
        "Mệnh đề toán học & Suy luận logic",
        "💡",
        "Nắm vững mệnh đề, mệnh đề chứa biến, phủ định, kéo theo, tương đương và các lượng từ ∀, ∃.",
        "Mệnh đề toán học là một câu khẳng định có tính đúng hoặc sai xác định. Một mệnh đề không thể vừa đúng vừa sai (nguyên lý bài trung).",
        "• Cần phân biệt mệnh đề với câu hỏi, câu cảm thán, câu mệnh lệnh hoặc mệnh đề chứa biến P(x) chưa gán giá trị cụ thể.\n"
        "• Mệnh đề phủ định P̄, mệnh đề kéo theo P ⇒ Q, mệnh đề đảo Q ⇒ P, mệnh đề tương đương P ⇔ Q.\n"
        "• Điều kiện cần và điều kiện đủ; Lượng từ với mọi (∀) và tồn tại (∃) cùng quy tắc phủ định chúng.",
        [
            {
                "category": "I. Phủ định mệnh đề & Phủ định lượng từ",
                "items": [
                    {"name": "Mệnh đề phủ định", "formula": "P̄ đúng khi P sai ; P̄ sai khi P đúng", "note": ""},
                    {"name": "Phủ định mệnh đề chứa ∀", "formula": "Phủ định của '∀x ∈ X, P(x)' là '∃x ∈ X, P̄(x)'", "note": "Đổi ∀ thành ∃ và phủ định tính chất P(x)"},
                    {"name": "Phủ định mệnh đề chứa ∃", "formula": "Phủ định của '∃x ∈ X, P(x)' là '∀x ∈ X, P̄(x)'", "note": "Đổi ∃ thành ∀ và phủ định tính chất P(x)"},
                ],
            },
            {
                "category": "II. Mệnh đề kéo theo & Mệnh đề tương đương",
                "items": [
                    {"name": "Mệnh đề kéo theo", "formula": "P ⇒ Q", "note": "Chỉ SAI khi P đúng mà Q sai; mọi trường hợp khác đều ĐÚNG"},
                    {"name": "Điều kiện cần và đủ", "formula": "Trong P ⇒ Q: P là điều kiện ĐỦ để có Q ; Q là điều kiện CẦN để có P", "note": ""},
                    {"name": "Mệnh đề tương đương", "formula": "P ⇔ Q  (đúng khi cả P ⇒ Q và Q ⇒ P cùng đúng)", "note": "P và Q có cùng chân trị (cùng đúng hoặc cùng sai)"},
                ],
            },
        ],
        "Mệnh đề là nền tảng của tư duy logic toán học, cách phát biểu định lý và cấu trúc điều kiện trong lập trình máy tính.",
        "Biểu thức điều kiện IF - ELSE, toán tử logic AND, OR, NOT trong lập trình, mạch điện tử số và hệ thống truy vấn cơ sở dữ liệu.",
        "Tìm mệnh đề phủ định của mệnh đề P: '∀x ∈ ℝ, x² − 2x + 3 > 0' và xét tính đúng sai của P.",
        "Mệnh đề phủ định là P̄: '∃x ∈ ℝ, x² − 2x + 3 ≤ 0'. Vì x² − 2x + 3 = (x − 1)² + 2 ≥ 2 > 0 với mọi x ∈ ℝ nên P là mệnh đề ĐÚNG và P̄ là mệnh đề SAI.",
        "Mệnh đề kéo theo P ⇒ Q bị SAI trong trường hợp nào dưới đây?",
        [
            "P đúng và Q đúng",
            "P đúng và Q sai",
            "P sai và Q đúng",
            "P sai và Q sai",
        ],
        1,
        "Cho mệnh đề chứa biến P(n): 'n² − 1 chia hết cho 3' với n là số tự nhiên. Hãy xét tính đúng sai của hai mệnh đề P(4) và '∀n ∈ ℕ, P(n)'.",
        "Tại n = 4: 4² − 1 = 15 chia hết cho 3 nên P(4) ĐÚNG. Tuy nhiên tại n = 3: 3² − 1 = 8 không chia hết cho 3 nên mệnh đề '∀n ∈ ℕ, P(n)' là SAI.",
    ),
    M(
        10,
        "tap-hop",
        "Tập hợp & Các phép toán trên tập hợp",
        "⭕",
        "Thực hiện các phép toán Giao (∩), Hợp (∪), Hiệu (\\), Phần bù và biểu diễn các tập con của ℝ trên trục số.",
        "Tập hợp là khái niệm nguyên thủy của toán học dùng để chỉ một nhóm các đối tượng xác định rõ ràng, mỗi đối tượng gọi là một phần tử của tập hợp.",
        "• Cách xác định tập hợp: liệt kê phần tử hoặc chỉ ra tính chất đặc trưng A = {x ∈ X | P(x)}.\n"
        "• Tập rỗng (∅), tập con (A ⊂ B), hai tập hợp bằng nhau (A = B). Tập hợp có n phần tử thì có 2ⁿ tập con.\n"
        "• Các phép toán: Giao (A ∩ B), Hợp (A ∪ B), Hiệu (A \\ B), Phần bù (C_E A khi A ⊂ E).\n"
        "• Các tập con thường dùng của tập số thực ℝ: khoảng (a; b), đoạn [a; b], nửa khoảng [a; b), (a; b].",
        [
            {
                "category": "I. Quan hệ Tập hợp & Số tập con",
                "items": [
                    {"name": "Tập con & Bằng nhau", "formula": "A ⊂ B ⇔ (∀x, x ∈ A ⇒ x ∈ B)  ;  A = B ⇔ (A ⊂ B và B ⊂ A)", "note": "∅ là tập con của mọi tập hợp"},
                    {"name": "Số tập con của tập n phần tử", "formula": "N_tập_con = 2ⁿ", "note": "Số tập con khác rỗng là 2ⁿ − 1"},
                ],
            },
            {
                "category": "II. Các phép toán trên Tập hợp",
                "items": [
                    {"name": "Giao của hai tập hợp", "formula": "A ∩ B = {x | x ∈ A và x ∈ B}", "note": "Lấy phần chung"},
                    {"name": "Hợp của hai tập hợp", "formula": "A ∪ B = {x | x ∈ A hoặc x ∈ B}", "note": "Lấy tất cả phần tử của cả hai"},
                    {"name": "Hiệu và Phần bù", "formula": "A \\ B = {x | x ∈ A và x ∉ B}  ;  C_E A = E \\ A (với A ⊂ E)", "note": ""},
                ],
            },
            {
                "category": "III. Công thức lực lượng (Biểu đồ Venn)",
                "items": [
                    {"name": "Cho 2 tập hợp hữu hạn", "formula": "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)", "note": ""},
                    {"name": "Cho 3 tập hợp hữu hạn", "formula": "n(A∪B∪C) = n(A)+n(B)+n(C) − n(A∩B) − n(B∩C) − n(C∩A) + n(A∩B∩C)", "note": "Nguyên lý bù trừ"},
                ],
            },
        ],
        "Tập hợp giúp phân loại dữ liệu, thực hiện các phép nối (JOIN, UNION, INTERSECT) trong cơ sở dữ liệu SQL và giải hệ điều kiện.",
        "Lọc danh sách khách hàng mua cả hai dòng sản phẩm, thống kê học sinh giỏi nhiều môn bằng biểu đồ Venn.",
        "Cho hai tập hợp A = [−3; 4) và B = (1; 6]. Xác định A ∩ B, A ∪ B, A \\ B và C_ℝ A.",
        "Biểu diễn trên trục số: A ∩ B = (1; 4) ; A ∪ B = [−3; 6] ; A \\ B = [−3; 1] ; C_ℝ A = (−∞; −3) ∪ [4; +∞).",
        "Lớp 10A có 42 học sinh, trong đó có 25 bạn giỏi Toán, 20 bạn giỏi Anh và 10 bạn giỏi cả hai môn Toán và Anh. Hỏi trong lớp có bao nhiêu bạn không giỏi môn nào trong hai môn trên?",
        ["5 bạn", "7 bạn", "10 bạn", "12 bạn"],
        1,
        "Cho hai tập hợp A = [m; m + 3] và B = (−1; 5). Tìm tất cả các giá trị của tham số thực m để A ∩ B ≠ ∅.",
        "Ta tìm m để A ∩ B = ∅ trước: A ∩ B = ∅ ⇔ m + 3 ≤ −1 hoặc m ≥ 5 ⇔ m ≤ −4 hoặc m ≥ 5. Vậy để A ∩ B ≠ ∅ thì −4 < m < 5.",
    ),
    M(
        10,
        "bat-phuong-trinh",
        "Bất phương trình, Hệ bất phương trình bậc nhất hai ẩn & Quy hoạch tuyến tính",
        "📊",
        "Biểu diễn miền nghiệm của bất phương trình, hệ bất phương trình bậc nhất hai ẩn và giải bài toán tối ưu Quy hoạch tuyến tính.",
        "Bất phương trình bậc nhất hai ẩn x, y có dạng ax + by < c (hoặc >, ≤, ≥) với a² + b² > 0; miền nghiệm của hệ bất phương trình là miền đa giác lồi trên mặt phẳng tọa độ Oxy.",
        "• Cách xác định miền nghiệm của bất phương trình ax + by ≤ c: vẽ đường thẳng bờ d: ax + by = c và thử tọa độ một điểm không thuộc d (thường là gốc O(0; 0)).\n"
        "• Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn.\n"
        "• Định lý cơ bản của Quy hoạch tuyến tính: Giá trị lớn nhất và giá trị nhỏ nhất của biểu thức F(x; y) = Ax + By trên miền đa giác lồi luôn đạt được tại một trong các ĐỈNH của đa giác đó.",
        [
            {
                "category": "I. Miền nghiệm của Bất phương trình bậc nhất hai ẩn",
                "items": [
                    {"name": "Đường thẳng bờ d", "formula": "d: ax + by = c chia mặt phẳng Oxy thành 2 nửa mặt phẳng", "note": ""},
                    {"name": "Quy tắc điểm thử M₀(x₀; y₀) ∉ d", "formula": "Thay (x₀; y₀) vào ax + by ≤ c: nếu ĐÚNG thì lấy nửa mặt phẳng chứa M₀, nếu SAI thì lấy nửa kia", "note": "Dấu ≤, ≥ thì lấy cả bờ d; dấu <, > thì bỏ bờ d"},
                ],
            },
            {
                "category": "II. Bài toán tối ưu Quy hoạch tuyến tính",
                "items": [
                    {"name": "Hàm mục tiêu", "formula": "F(x; y) = Ax + By → max / min trên miền đa giác lồi Ω", "note": "x, y thường là số lượng sản phẩm (x ≥ 0, y ≥ 0)"},
                    {"name": "Thuật toán tìm cực trị tại các đỉnh", "formula": "Tính F(xᵢ; yᵢ) tại tất cả các đỉnh A₁, A₂, ..., Aₖ của miền Ω rồi so sánh", "note": "Giá trị lớn nhất/nhỏ nhất tại đỉnh chính là GTLN/GTNN cần tìm"},
                ],
            },
        ],
        "Quy hoạch tuyến tính là công cụ cốt lõi trong quản trị sản xuất, logistics và kinh tế học để tối đa hóa lợi nhuận với nguồn nguyên liệu giới hạn.",
        "Lập kế hoạch sản xuất 2 loại sản phẩm với giới hạn giờ máy và nguyên liệu để thu được lợi nhuận cao nhất.",
        "Tìm giá trị lớn nhất của biểu thức F(x; y) = 3x + 4y trên miền nghiệm của hệ: { x ≥ 0 ; y ≥ 0 ; x + y ≤ 5 ; 2x + y ≤ 8 }.",
        "Miền nghiệm là tứ giác lồi OABC với các đỉnh: O(0; 0), A(4; 0), B(3; 2) (giao của x + y = 5 và 2x + y = 8), C(0; 5). Tính F tại các đỉnh: F(0;0) = 0 ; F(4;0) = 12 ; F(3;2) = 17 ; F(0;5) = 20. Vậy GTLN của F là 20 đạt tại (x; y) = (0; 5).",
        "Cặp số (x; y) nào dưới đây thuộc miền nghiệm của bất phương trình 2x − 3y + 6 > 0?",
        ["(−3; 1)", "(0; 3)", "(1; 2)", "(−4; 0)"],
        2,
        "Một xưởng mộc sản xuất hai loại bàn (x chiếc) và ghế (y chiếc). Mỗi chiếc bàn cần 4 giờ lắp ráp và 2 giờ sơn, lãi 400 nghìn đồng; mỗi chiếc ghế cần 2 giờ lắp ráp và 2 giờ sơn, lãi 250 nghìn đồng. Trong tuần xưởng có tối đa 60 giờ lắp ráp và 40 giờ sơn. Hỏi xưởng nên sản xuất bao nhiêu bàn và ghế để tổng tiền lãi cao nhất?",
        "Hệ ràng buộc: { x ≥ 0, y ≥ 0 ; 4x + 2y ≤ 60 (⇔ 2x + y ≤ 30) ; 2x + 2y ≤ 40 (⇔ x + y ≤ 20) }. Hàm lợi nhuận L(x; y) = 400x + 250y (nghìn đồng). Các đỉnh của miền nghiệm: O(0;0), A(15;0), B(10;10), C(0;20). Tính L: L(0;0) = 0 ; L(15;0) = 6000 ; L(10;10) = 6500 ; L(0;20) = 5000. Vậy lãi cao nhất là 6 500 000 đồng khi sản xuất 10 bàn và 10 ghế.",
    ),
    M(
        10,
        "ham-so",
        "Hàm số, Hàm số bậc hai & Dấu của Tam thức bậc hai",
        "📈",
        "Tìm tập xác định, xét tính biến thiên của hàm số, khảo sát Parabol y = ax² + bx + c và xét dấu tam thức bậc hai.",
        "Hàm số y = f(x) xác định trên tập D gán mỗi x ∈ D với duy nhất một số thực y. Hàm số bậc hai y = ax² + bx + c (a ≠ 0) có đồ thị là Parabol với đỉnh I(−b/(2a); −Δ/(4a)).",
        "• Tập xác định, tập giá trị, tính đồng biến - nghịch biến, tính chẵn - lẻ của hàm số.\n"
        "• Khảo sát sự biến thiên và vẽ đồ thị hàm số bậc hai y = ax² + bx + c (a ≠ 0): tọa độ đỉnh I, trục đối xứng x = −b/(2a), bề lõm.\n"
        "• Định lý về dấu của tam thức bậc hai f(x) = ax² + bx + c (a ≠ 0) và giải bất phương trình bậc hai, phương trình quy về bậc hai.",
        [
            {
                "category": "I. Tập xác định & Tính đơn điệu của Hàm số",
                "items": [
                    {"name": "Điều kiện xác định cơ bản", "formula": "1/A(x) ⇔ A(x) ≠ 0 ; √B(x) ⇔ B(x) ≥ 0 ; 1/√B(x) ⇔ B(x) > 0", "note": ""},
                    {"name": "Đồng biến / Nghịch biến trên K", "formula": "∀x₁, x₂ ∈ K, x₁ < x₂: f(x₁) < f(x₂) (đồng biến) ; f(x₁) > f(x₂) (nghịch biến)", "note": ""},
                ],
            },
            {
                "category": "II. Hàm số bậc hai y = ax² + bx + c (a ≠ 0)",
                "items": [
                    {"name": "Tọa độ đỉnh I & Trục đối xứng", "formula": "I( −b/(2a) ; −Δ/(4a) ) với Δ = b² − 4ac  ;  Trục đối xứng: x = −b/(2a)", "note": ""},
                    {"name": "Cực trị của hàm bậc hai trên ℝ", "formula": "Nếu a > 0: y_min = −Δ/(4a) tại x = −b/(2a) ; Nếu a < 0: y_max = −Δ/(4a) tại x = −b/(2a)", "note": ""},
                ],
            },
            {
                "category": "III. Định lý về dấu của Tam thức bậc hai f(x) = ax² + bx + c",
                "items": [
                    {"name": "Khi Δ < 0", "formula": "f(x) luôn CÙNG DẤU với hệ số a với mọi x ∈ ℝ", "note": "a·f(x) > 0, ∀x ∈ ℝ"},
                    {"name": "Khi Δ = 0", "formula": "f(x) cùng dấu với a với mọi x ≠ −b/(2a) (tại x = −b/(2a) thì f(x) = 0)", "note": ""},
                    {"name": "Khi Δ > 0 (có 2 nghiệm x₁ < x₂)", "formula": "'Trong trái, ngoài cùng': Trên (x₁; x₂) trái dấu với a; trên (−∞; x₁) ∪ (x₂; +∞) cùng dấu với a", "note": ""},
                ],
            },
        ],
        "Mô hình hóa quỹ đạo vật ném, tối ưu hóa doanh thu - chi phí và giải các bài toán điều kiện tham số.",
        "Xác định tầm bay cao nhất và xa nhất của quả bóng đá, tối ưu giá bán sản phẩm để đạt lợi nhuận cực đại.",
        "Xác định parabol (P): y = ax² + bx + 3, biết rằng (P) có đỉnh là I(1; −1). Sau đó giải bất phương trình ax² + bx + 3 ≤ 0.",
        "Vì đỉnh là I(1; −1) nên: { −b/(2a) = 1 ; a(1)² + b(1) + 3 = −1 } ⇔ { b = −2a ; a + b = −4 } ⇔ a = 4, b = −8. Khi đó 4x² − 8x + 3 ≤ 0 ⇔ (2x − 1)(2x − 3) ≤ 0 ⇔ 1/2 ≤ x ≤ 3/2.",
        "Tập nghiệm của bất phương trình −x² + 5x − 6 ≥ 0 là:",
        ["(−∞; 2] ∪ [3; +∞)", "[2; 3]", "(2; 3)", "[−3; −2]"],
        1,
        "Tìm tất cả các giá trị của tham số m để bất phương trình x² − 2(m − 1)x + m + 5 > 0 nghiệm đúng với mọi x ∈ ℝ.",
        "Tam thức bậc hai có hệ số a = 1 > 0, nên để f(x) > 0 với mọi x ∈ ℝ khi và chỉ khi Δ' < 0 ⇔ (m − 1)² − (m + 5) < 0 ⇔ m² − 3m − 4 < 0 ⇔ −1 < m < 4.",
    ),
    M(
        10,
        "vecto",
        "Vectơ, Các phép toán vectơ & Tích vô hướng của hai vectơ",
        "➡️",
        "Nắm vững quy tắc 3 điểm, quy tắc hình bình hành, hệ thức trung điểm - trọng tâm và tích vô hướng của hai vectơ.",
        "Vectơ là một đoạn thẳng có hướng, được xác định bởi điểm đầu và điểm cuối (hoặc bởi phương, hướng và độ dài).",
        "• Hai vectơ cùng phương, cùng hướng, hai vectơ bằng nhau, hai vectơ đối nhau và vectơ-không (0⃗).\n"
        "• Quy tắc ba điểm (cộng và trừ), quy tắc hình bình hành, hệ thức trung điểm đoạn thẳng và trọng tâm tam giác.\n"
        "• Tích của một số k với một vectơ và điều kiện hai vectơ cùng phương.\n"
        "• Tích vô hướng của hai vectơ, góc giữa hai vectơ và điều kiện hai vectơ vuông góc.",
        [
            {
                "category": "I. Quy tắc Cộng, Trừ & Hệ thức Trung điểm - Trọng tâm",
                "items": [
                    {"name": "Quy tắc 3 điểm (Cộng & Hiệu)", "formula": "AB⃗ + BC⃗ = AC⃗  ;  OB⃗ − OA⃗ = AB⃗", "note": "Cộng nối tiếp; trừ chung gốc (ngọn trừ gốc)"},
                    {"name": "Quy tắc hình bình hành ABCD", "formula": "AB⃗ + AD⃗ = AC⃗", "note": "Tổng hai vectơ cạnh chung gốc bằng vectơ đường chéo"},
                    {"name": "Hệ thức Trung điểm I của AB", "formula": "IA⃗ + IB⃗ = 0⃗  ;  MA⃗ + MB⃗ = 2 MI⃗ (với mọi điểm M)", "note": ""},
                    {"name": "Hệ thức Trọng tâm G của ΔABC", "formula": "GA⃗ + GB⃗ + GC⃗ = 0⃗  ;  MA⃗ + MB⃗ + MC⃗ = 3 MG⃗ (với mọi điểm M)", "note": ""},
                ],
            },
            {
                "category": "II. Tọa độ Vectơ & Tích vô hướng trong mặt phẳng Oxy",
                "items": [
                    {"name": "Tọa độ vectơ AB⃗ & Độ dài", "formula": "AB⃗ = (x_B − x_A ; y_B − y_A)  ;  |u⃗| = √(x² + y²)", "note": "Lấy tọa độ điểm cuối trừ điểm đầu"},
                    {"name": "Tích vô hướng theo góc & tọa độ", "formula": "u⃗ · v⃗ = |u⃗| · |v⃗| · cos(u⃗, v⃗) = x₁x₂ + y₁y₂", "note": "Kết quả tích vô hướng là một SỐ THỰC"},
                    {"name": "Góc giữa hai vectơ & Vuông góc", "formula": "cos(u⃗, v⃗) = (x₁x₂ + y₁y₂) / [√(x₁² + y₁²) · √(x₂² + y₂²)]  ;  u⃗ ⊥ v⃗ ⇔ u⃗ · v⃗ = 0", "note": ""},
                ],
            },
        ],
        "Vectơ là ngôn ngữ chuẩn để biểu diễn vận tốc, gia tốc, lực trong vật lý và xử lý đồ họa 2D/3D trong máy tính.",
        "Tổng hợp hai lực kéo một chiếc thuyền trên sông, tính công cơ học A = F⃗ · s⃗ = F · s · cos α.",
        "Trong mặt phẳng Oxy, cho ba điểm A(1; 2), B(3; 5) và C(−2; 4). Tìm tọa độ trọng tâm G của tam giác ABC và tính tích vô hướng AB⃗ · AC⃗.",
        "Trọng tâm G có: x_G = (1 + 3 − 2)/3 = 2/3 ; y_G = (2 + 5 + 4)/3 = 11/3 ⇒ G(2/3; 11/3). Ta có AB⃗ = (2; 3) và AC⃗ = (−3; 2). Tích vô hướng: AB⃗ · AC⃗ = 2·(−3) + 3·2 = 0 (suy ra AB ⊥ AC hay ΔABC vuông tại A).",
        "Cho hình vuông ABCD có cạnh bằng a. Giá trị của tích vô hướng AB⃗ · AC⃗ bằng:",
        ["a²√2", "a²", "a²/2", "0"],
        1,
        "Hai lực F₁⃗ và F₂⃗ cùng tác dụng vào một vật tại điểm O, biết |F₁⃗| = 30 N, |F₂⃗| = 40 N và góc hợp bởi hai lực bằng 60°. Tính độ lớn của hợp lực F⃗ = F₁⃗ + F₂⃗.",
        "Bình phương vô hướng: |F⃗|² = (F₁⃗ + F₂⃗)² = |F₁⃗|² + |F₂⃗|² + 2|F₁⃗||F₂⃗|cos 60° = 30² + 40² + 2·30·40·(1/2) = 900 + 1600 + 1200 = 3700. Vậy độ lớn hợp lực là |F⃗| = √3700 = 10√37 ≈ 60,83 (N).",
    ),
    M(
        10,
        "hinh-hoc",
        "Hệ thức lượng trong tam giác & Phương pháp tọa độ trong mặt phẳng Oxy",
        "📐",
        "Vận dụng định lý Cosin, định lý Sin, các công thức diện tích tam giác và phương trình Đường thẳng, Đường tròn, Ba đường Conic.",
        "Chuyên đề kết hợp Giải tam giác (định lý Cosin, Sin, công thức diện tích Heron) với Hình học giải tích phẳng Oxy (Đường thẳng, Đường tròn, Elip, Hypebol, Parabol).",
        "• Định lý Cosin, Định lý Sin, công thức độ dài đường trung tuyến và 5 công thức tính diện tích tam giác.\n"
        "• Phương trình tham số và phương trình tổng quát của đường thẳng; góc và khoảng cách từ một điểm đến đường thẳng.\n"
        "• Phương trình đường tròn tâm I(a; b) bán kính R và phương trình tiếp tuyến của đường tròn.\n"
        "• Phương trình chính tắc của ba đường Conic: Elip (E), Hypebol (H) và Parabol (P).",
        [
            {
                "category": "I. Hệ thức lượng trong Tam giác thường ABC (cạnh a, b, c; bán kính R, r; nửa chu vi p)",
                "items": [
                    {"name": "Định lý Cosin", "formula": "a² = b² + c² − 2bc · cos A  ⇒  cos A = (b² + c² − a²) / (2bc)", "note": "Tổng quát hóa định lý Pythagore"},
                    {"name": "Định lý Sin", "formula": "a / sin A = b / sin B = c / sin C = 2R", "note": "R là bán kính đường tròn ngoại tiếp"},
                    {"name": "Độ dài đường trung tuyến", "formula": "m_a² = (2b² + 2c² − a²) / 4", "note": ""},
                    {"name": "5 Công thức diện tích S", "formula": "S = (1/2)a·h_a = (1/2)bc·sin A = abc/(4R) = p·r = √[p(p − a)(p − b)(p − c)]", "note": "Công thức cuối là công thức Heron"},
                ],
            },
            {
                "category": "II. Đường thẳng, Đường tròn & Ba đường Conic trong Oxy",
                "items": [
                    {"name": "Đường thẳng Δ: ax + by + c = 0", "formula": "Vectơ pháp tuyến n⃗ = (a; b), VTCP u⃗ = (−b; a) ; d(M₀, Δ) = |ax₀ + by₀ + c| / √(a² + b²)", "note": ""},
                    {"name": "Đường tròn (C) tâm I(a; b), bán kính R", "formula": "(x − a)² + (y − b)² = R²  hoặc  x² + y² − 2ax − 2by + c = 0 (với R = √(a² + b² − c))", "note": "ĐK: a² + b² − c > 0"},
                    {"name": "Elip (E), Hypebol (H) & Parabol (P)", "formula": "(E): x²/a² + y²/b² = 1 (c² = a² − b²) ; (H): x²/a² − y²/b² = 1 (c² = a² + b²) ; (P): y² = 2px", "note": "Tiêu cự 2c"},
                ],
            },
        ],
        "Giải quyết trọn vẹn các bài toán trắc địa, định vị GPS, thiết kế quỹ đạo vệ tinh hình Elip và bản đồ số.",
        "Đo khoảng cách giữa hai địa điểm bị ngăn cách bởi hồ nước (định lý Cosin), xác định vùng phủ sóng trạm thu phát (phương trình đường tròn).",
        "Cho tam giác ABC có a = 7, b = 8, c = 5. Tính góc A, diện tích S, bán kính đường tròn ngoại tiếp R và nội tiếp r của tam giác.",
        "Theo định lý Cosin: cos A = (8² + 5² − 7²)/(2·8·5) = 40/80 = 1/2 ⇒ ∠A = 60°. Nửa chu vi p = (7 + 8 + 5)/2 = 10. Theo Heron: S = √[10(10−7)(10−8)(10−5)] = √300 = 10√3. Khi đó R = abc/(4S) = (7·8·5)/(40√3) = 7√3/3 và r = S/p = √3.",
        "Trong mặt phẳng Oxy, khoảng cách từ điểm M(3; −4) đến đường thẳng Δ: 3x − 4y − 5 = 0 bằng:",
        ["2", "4", "5", "20"],
        1,
        "Trong mặt phẳng Oxy, viết phương trình đường tròn (C) đi qua điểm A(4; 2) và tiếp xúc với đường thẳng d: 3x + 4y − 16 = 0 tại điểm B(4; 1); biết tâm I của (C) có tọa độ nguyên. (Gợi ý: thử hoặc lập hệ từ IA = IB = d(I, d)).",
        "Thực tế: Cho tâm I(1; 2) và đường thẳng d: 3x − 4y + 15 = 0. Bán kính đường tròn tâm I tiếp xúc với d là R = d(I, d) = |3·1 − 4·2 + 15| / √(3² + (−4)²) = 10/5 = 2. Phương trình đường tròn là: (x − 1)² + (y − 2)² = 4.",
    ),
    M(
        10,
        "to-hop-xac-suat",
        "Đại số Tổ hợp (Hoán vị - Chỉnh hợp - Tổ hợp), Nhị thức Newton & Xác suất cổ điển",
        "🎲",
        "Phân biệt quy tắc cộng - quy tắc nhân, hoán vị, chỉnh hợp, tổ hợp, khai triển nhị thức Newton và tính xác suất cổ điển.",
        "Đại số tổ hợp cung cấp các công cụ đếm số phương án của một cấu hình hữu hạn mà không cần liệt kê thủ công, làm cơ sở để tính xác suất cổ điển P(A) = n(A)/n(Ω).",
        "• Quy tắc cộng (công việc chia thành nhiều phương án độc lập) và Quy tắc nhân (công việc gồm nhiều công đoạn liên tiếp).\n"
        "• Hoán vị Pₙ = n! (sắp xếp n phần tử), Chỉnh hợp Aₙᵏ (chọn k từ n phần tử CÓ thứ tự), Tổ hợp Cₙᵏ (chọn k từ n phần tử KHÔNG phân biệt thứ tự).\n"
        "• Công thức khai triển Nhị thức Newton (a + b)ⁿ.\n"
        "• Không gian mẫu Ω, biến cố A, biến cố đối Ā và xác suất cổ điển.",
        [
            {
                "category": "I. Quy tắc đếm & Ba cấu hình Tổ hợp cơ bản (0 ≤ k ≤ n)",
                "items": [
                    {"name": "Quy tắc Cộng & Quy tắc Nhân", "formula": "Phương án độc lập: m + n cách  ;  Công đoạn liên tiếp: m · n cách", "note": ""},
                    {"name": "Hoán vị của n phần tử", "formula": "Pₙ = n! = 1 · 2 · 3 · ... · n (Quy ước: 0! = 1)", "note": "Đổi chỗ toàn bộ n phần tử"},
                    {"name": "Chỉnh hợp chập k của n (CÓ thứ tự)", "formula": "Aₙᵏ = n! / (n − k)! = n(n − 1)...(n − k + 1)", "note": "Chọn k phần tử rồi sắp xếp thứ tự"},
                    {"name": "Tổ hợp chập k của n (KHÔNG thứ tự)", "formula": "Cₙᵏ = n! / [k!(n − k)!] = Aₙᵏ / k!", "note": "Tính chất: Cₙᵏ = Cₙⁿ⁻ᵏ ; Cₙᵏ + Cₙᵏ⁺¹ = Cₙ⁺¹ᵏ⁺¹"},
                ],
            },
            {
                "category": "II. Nhị thức Newton & Xác suất cổ điển",
                "items": [
                    {"name": "Khai triển Nhị thức Newton", "formula": "(a + b)ⁿ = Σ[k=0→n] Cₙᵏ · aⁿ⁻ᵏ · bᵏ", "note": "Số hạng tổng quát thứ k+1: T_{k+1} = Cₙᵏ aⁿ⁻ᵏ bᵏ"},
                    {"name": "Xác suất cổ điển & Biến cố đối", "formula": "P(A) = n(A) / n(Ω)  ;  P(Ā) = 1 − P(A)", "note": "Dùng biến cố đối khi mệnh đề có từ 'ít nhất một'"},
                ],
            },
        ],
        "Ứng dụng trong bảo mật mật khẩu, mã hóa dữ liệu, phân tích rủi ro tài chính, di truyền học và trí tuệ nhân tạo.",
        "Tính số mật khẩu khả dĩ của ngân hàng, số cách lập đội tuyển thi đấu và xác suất kiểm định chất lượng sản phẩm.",
        "Một tổ học sinh có 6 nam và 4 nữ. Chọn ngẫu nhiên 3 học sinh đi trực nhật. Tính xác suất để trong 3 học sinh được chọn có ít nhất 1 học sinh nữ.",
        "Tổng số cách chọn 3 học sinh từ 10 học sinh là n(Ω) = C₁₀³ = 120. Gọi A là biến cố 'có ít nhất 1 nữ', suy ra biến cố đối Ā là 'cả 3 học sinh đều là nam' ⇒ n(Ā) = C₆³ = 20. Vậy P(A) = 1 − P(Ā) = 1 − 20/120 = 5/6.",
        "Hệ số của x³ trong khai triển nhị thức Newton của biểu thức (2x − 1)⁵ là:",
        ["−80", "80", "−40", "40"],
        1,
        "Từ các chữ số {0; 1; 2; 3; 4; 5; 6}, có thể lập được bao nhiêu số tự nhiên chẵn có 4 chữ số đôi một khác nhau?",
        "Gọi số cần lập là abcd (a ≠ 0). TH1: d = 0 ⇒ có 1 cách chọn d; a có 6 cách, b có 5 cách, c có 4 cách ⇒ 1·6·5·4 = 120 (số). TH2: d ∈ {2; 4; 6} (3 cách chọn d); a ≠ 0 và a ≠ d nên a có 5 cách; b có 5 cách; c có 4 cách ⇒ 3·5·5·4 = 300 (số). Tổng cộng có: 120 + 300 = 420 (số).",
    ),
    M(
        10,
        "thong-ke",
        "Số gần đúng - Sai số & Các số đặc trưng của mẫu số liệu không ghép nhóm",
        "📊",
        "Tính sai số tuyệt đối - tương đối, số trung bình, trung vị, tứ phân vị (Q₁, Q₂, Q₃), mốt, phương sai và độ lệch chuẩn.",
        "Thống kê lớp 10 trang bị trọn bộ các số đặc trưng đo xu thế trung tâm (trung bình, trung vị, tứ phân vị, mốt) và đo mức độ phân tán (khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn).",
        "• Số gần đúng, sai số tuyệt đối Δₐ = |ā − a|, độ chính xác d và sai số tương đối δₐ ≤ d/|a|; quy tắc quy tròn số.\n"
        "• Số trung bình (x̄), Trung vị (Mₑ = Q₂), Tứ phân vị (Q₁, Q₂, Q₃) và Mốt (M₀).\n"
        "• Khoảng biến thiên (R), Khoảng tứ phân vị (Δ_Q = Q₃ − Q₁), Phương sai (s²) và Độ lệch chuẩn (s); cách phát hiện giá trị ngoại lệ (outlier).",
        [
            {
                "category": "I. Sai số & Xu thế trung tâm",
                "items": [
                    {"name": "Sai số tuyệt đối & tương đối", "formula": "ā = a ± d  ⇒  Δₐ = |ā − a| ≤ d  ;  δₐ = Δₐ / |a| ≤ d / |a|", "note": ""},
                    {"name": "Số trung bình cộng", "formula": "x̄ = (x₁ + x₂ + ... + xₙ) / n = (n₁x₁ + ... + nₖxₖ) / n", "note": ""},
                    {"name": "Tứ phân vị Q₁, Q₂, Q₃", "formula": "Q₂ = Mₑ (chia mẫu đã sắp xếp thành 2 nửa) ; Q₁ là trung vị nửa dưới ; Q₃ là trung vị nửa trên", "note": ""},
                ],
            },
            {
                "category": "II. Các số đặc trưng đo Độ phân tán & Giá trị ngoại lệ",
                "items": [
                    {"name": "Khoảng biến thiên & Khoảng tứ phân vị", "formula": "R = x_max − x_min  ;  Δ_Q = Q₃ − Q₁", "note": "Δ_Q không bị ảnh hưởng bởi các giá trị bất thường ở hai đầu"},
                    {"name": "Phương sai & Độ lệch chuẩn", "formula": "s² = (1/n) Σ(xᵢ − x̄)² = [(1/n) Σxᵢ²] − x̄²  ;  s = √(s²)", "note": "s càng nhỏ thì dữ liệu càng đồng đều"},
                    {"name": "Điều kiện giá trị ngoại lệ (Outlier)", "formula": "x là giá trị bất thường nếu: x < Q₁ − 1,5·Δ_Q  hoặc  x > Q₃ + 1,5·Δ_Q", "note": ""},
                ],
            },
        ],
        "Giúp kiểm định độ ổn định của dây chuyền sản xuất, phân tích dữ liệu khảo sát và loại bỏ nhiễu (outlier) trong khoa học dữ liệu.",
        "Đánh giá độ đồng đều về phong độ của hai vận động viên bắn súng thông qua độ lệch chuẩn s.",
        "Cho mẫu số liệu điểm kiểm tra của 7 học sinh: 5; 6; 7; 7; 8; 9; 10. Tìm trung vị Q₂, các tứ phân vị Q₁, Q₃ và khoảng tứ phân vị Δ_Q.",
        "Dãy đã sắp xếp tăng dần có n = 7 (lẻ), số chính giữa là x₄ = 7 ⇒ Q₂ = 7. Nửa dưới (không tính x₄) là {5; 6; 7} có trung vị Q₁ = 6. Nửa trên là {8; 9; 10} có trung vị Q₃ = 9. Khoảng tứ phân vị: Δ_Q = Q₃ − Q₁ = 9 − 6 = 3.",
        "Hai xạ thủ A và B cùng bắn 10 phát đạn và có cùng điểm số trung bình x̄ = 8,5 điểm. Biết độ lệch chuẩn điểm của A là s_A = 0,4 và của B là s_B = 1,2. Kết luận nào sau đây là ĐÚNG?",
        [
            "Xạ thủ B có phong độ ổn định hơn xạ thủ A",
            "Xạ thủ A có phong độ ổn định hơn xạ thủ B",
            "Hai xạ thủ có độ ổn định như nhau",
            "Không thể so sánh độ ổn định từ độ lệch chuẩn",
        ],
        1,
        "Một mẫu số liệu có tứ phân vị thứ nhất Q₁ = 40 và tứ phân vị thứ ba Q₃ = 60. Hỏi trong hai giá trị x₁ = 5 và x₂ = 85, giá trị nào là giá trị ngoại lệ (bất thường) của mẫu số liệu?",
        "Ta có khoảng tứ phân vị Δ_Q = Q₃ − Q₁ = 60 − 40 = 20. Ngưỡng dưới là: Q₁ − 1,5·Δ_Q = 40 − 1,5·20 = 10. Ngưỡng trên là: Q₃ + 1,5·Δ_Q = 60 + 1,5·20 = 90. Vì x₁ = 5 < 10 nên x₁ = 5 là giá trị ngoại lệ; còn x₂ = 85 nằm trong đoạn [10; 90] nên không phải ngoại lệ.",
    ),

    # =========================================================
    # TOÁN 11 (8 BÀI)
    # =========================================================
    M(
        11,
        "ham-so",
        "Hàm số lượng giác, Công thức lượng giác & Phương trình lượng giác",
        "🌊",
        "Làm chủ đường tròn lượng giác, trọn bộ công thức biến đổi lượng giác và các phương trình lượng giác cơ bản.",
        "Hàm số lượng giác (y = sin x, y = cos x, y = tan x, y = cot x) là các hàm số tuần hoàn mô tả các dao động, sóng và hiện tượng lặp lại theo chu kỳ.",
        "• Đơn vị đo góc Radian (π rad = 180°), độ dài cung tròn l = R·α và đường tròn lượng giác.\n"
        "• Hệ thức lượng giác cơ bản, các góc có liên quan đặc biệt ('Cos đối, sin bù, phụ chéo, khác π tan cot').\n"
        "• Công thức cộng, công thức nhân đôi, công thức hạ bậc, công thức biến đổi tích thành tổng và tổng thành tích.\n"
        "• Tập xác định, tập giá trị, chu kỳ tuần hoàn của 4 hàm số lượng giác và công thức nghiệm của phương trình lượng giác cơ bản.",
        [
            {
                "category": "I. Hệ thức cơ bản, Công thức Cộng, Nhân đôi & Hạ bậc",
                "items": [
                    {"name": "Hệ thức cơ bản", "formula": "sin²x + cos²x = 1 ; 1 + tan²x = 1/cos²x ; 1 + cot²x = 1/sin²x ; tan x · cot x = 1", "note": ""},
                    {"name": "Công thức cộng", "formula": "sin(a ± b) = sin a cos b ± cos a sin b ; cos(a ± b) = cos a cos b ∓ sin a sin b", "note": "tan(a ± b) = (tan a ± tan b)/(1 ∓ tan a tan b)"},
                    {"name": "Công thức nhân đôi", "formula": "sin 2x = 2 sin x cos x ; cos 2x = cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x", "note": ""},
                    {"name": "Công thức hạ bậc", "formula": "sin²x = (1 − cos 2x)/2 ; cos²x = (1 + cos 2x)/2 ; tan²x = (1 − cos 2x)/(1 + cos 2x)", "note": ""},
                ],
            },
            {
                "category": "II. Chu kỳ hàm số & Phương trình lượng giác cơ bản (k ∈ ℤ)",
                "items": [
                    {"name": "Tập giá trị & Chu kỳ tuần hoàn", "formula": "−1 ≤ sin x, cos x ≤ 1 (Chu kỳ T = 2π) ; tan x, cot x ∈ ℝ (Chu kỳ T = π)", "note": "y = sin(ax+b) có T = 2π/|a|"},
                    {"name": "Phương trình sin u = sin v", "formula": "u = v + k2π  hoặc  u = π − v + k2π", "note": "Đặc biệt: sin x = 0 ⇔ x = kπ ; sin x = 1 ⇔ x = π/2 + k2π"},
                    {"name": "Phương trình cos u = cos v", "formula": "u = v + k2π  hoặc  u = −v + k2π", "note": "Đặc biệt: cos x = 0 ⇔ x = π/2 + kπ ; cos x = 1 ⇔ x = k2π"},
                    {"name": "Phương trình tan u = tan v & cot u = cot v", "formula": "tan u = tan v ⇔ u = v + kπ ; cot u = cot v ⇔ u = v + kπ", "note": ""},
                ],
            },
        ],
        "Mô hình hóa mọi quá trình dao động điều hòa, sóng âm, sóng điện từ, dòng điện xoay chiều và chu kỳ thủy triều.",
        "Tính chiều cao mực nước thủy triều theo giờ trong ngày, mô phỏng sóng âm thanh và điện áp xoay chiều u = U₀cos(ωt + φ).",
        "Giải phương trình lượng giác: 2cos²x − 3cos x + 1 = 0.",
        "Đặt t = cos x (−1 ≤ t ≤ 1). Phương trình trở thành 2t² − 3t + 1 = 0 ⇔ t = 1 hoặc t = 1/2. Với cos x = 1 ⇔ x = k2π. Với cos x = 1/2 = cos(π/3) ⇔ x = ±π/3 + k2π (k ∈ ℤ).",
        "Giá trị lớn nhất M và giá trị nhỏ nhất m của hàm số y = 3sin(2x − π/4) − 2 lần lượt là:",
        ["M = 3, m = −3", "M = 1, m = −5", "M = 5, m = −1", "M = 1, m = −2"],
        1,
        "Chiều cao h (mét) của một cabin trên vòng quay Mặt Trời tại thời điểm t (phút) sau khi bắt đầu chuyển động được cho bởi công thức: h(t) = 30 − 25cos( (π/15)t ). Hỏi cabin đạt độ cao lớn nhất là bao nhiêu mét và sau bao nhiêu phút kể từ lúc khởi hành thì cabin lần đầu tiên đạt độ cao 42,5 m?",
        "Vì cos((π/15)t) ≥ −1 nên h_max = 30 − 25·(−1) = 55 (m). Khi h(t) = 42,5 ⇔ 30 − 25cos((π/15)t) = 42,5 ⇔ cos((π/15)t) = −1/2 = cos(2π/3). Thời điểm dương nhỏ nhất ứng với (π/15)t = 2π/3 ⇒ t = 10 (phút).",
    ),
    M(
        11,
        "day-so-cap-so",
        "Dãy số, Cấp số cộng & Cấp số nhân",
        "📶",
        "Xét tính tăng giảm, bị chặn của dãy số và nắm vững công thức số hạng tổng quát, tổng n số hạng đầu của Cấp số cộng, Cấp số nhân.",
        "Cấp số cộng (CSC) là dãy số mà kể từ số hạng thứ hai, mỗi số hạng bằng số hạng đứng ngay trước nó cộng với một hằng số d (công sai). Cấp số nhân (CSN) là dãy số mà mỗi số hạng kể từ số hạng thứ hai bằng số hạng đứng ngay trước nó nhân với một hằng số q (công bội).",
        "• Dãy số tăng (uₙ₊₁ > uₙ), dãy số giảm (uₙ₊₁ < uₙ) và dãy số bị chặn.\n"
        "• Cấp số cộng (u₁, công sai d): số hạng tổng quát uₙ, tính chất trung bình cộng và tổng n số hạng đầu Sₙ.\n"
        "• Cấp số nhân (u₁, công bội q): số hạng tổng quát uₙ, tính chất trung bình nhân và tổng n số hạng đầu Sₙ (cùng tổng CSN lùi vô hạn khi |q| < 1).",
        [
            {
                "category": "I. Cấp số cộng (Số hạng đầu u₁, công sai d)",
                "items": [
                    {"name": "Định nghĩa & Số hạng tổng quát", "formula": "uₙ₊₁ = uₙ + d  ;  uₙ = u₁ + (n − 1)d (với n ≥ 2)", "note": ""},
                    {"name": "Tính chất đặc trưng CSC", "formula": "uₖ = (uₖ₋₁ + uₖ₊₁) / 2  (2uₖ = uₖ₋₁ + uₖ₊₁)", "note": "Mỗi số hạng là trung bình cộng của 2 số hạng kề nó"},
                    {"name": "Tổng n số hạng đầu Sₙ", "formula": "Sₙ = n(u₁ + uₙ) / 2 = [n · (2u₁ + (n − 1)d)] / 2", "note": ""},
                ],
            },
            {
                "category": "II. Cấp số nhân (Số hạng đầu u₁, công bội q)",
                "items": [
                    {"name": "Định nghĩa & Số hạng tổng quát", "formula": "uₙ₊₁ = uₙ · q  ;  uₙ = u₁ · qⁿ⁻¹ (với n ≥ 2)", "note": ""},
                    {"name": "Tính chất đặc trưng CSN", "formula": "uₖ² = uₖ₋₁ · uₖ₊₁", "note": "Bình phương mỗi số hạng bằng tích 2 số hạng kề nó"},
                    {"name": "Tổng n số hạng đầu Sₙ (với q ≠ 1)", "formula": "Sₙ = u₁ · (1 − qⁿ) / (1 − q) = u₁ · (qⁿ − 1) / (q − 1)", "note": "Nếu q = 1 thì Sₙ = n · u₁"},
                    {"name": "Tổng CSN lùi vô hạn (|q| < 1)", "formula": "S = u₁ + u₂ + ... + uₙ + ... = u₁ / (1 − q)", "note": ""},
                ],
            },
        ],
        "Mô hình hóa bài toán lãi đơn (cấp số cộng), lãi kép ngân hàng, tăng trưởng dân số và phân rã phóng xạ (cấp số nhân).",
        "Tính tổng số ghế trong nhà hát thiết kế theo bậc thang (CSC), tính lãi kép tích lũy hoặc khấu hao tài sản (CSN).",
        "Cho cấp số cộng (uₙ) có u₁ = 3 và u₅ = 19. Tìm công sai d, số hạng u₂₀ và tổng 20 số hạng đầu tiên S₂₀.",
        "Ta có u₅ = u₁ + 4d ⇔ 19 = 3 + 4d ⇒ d = 4. Khi đó u₂₀ = u₁ + 19d = 3 + 19·4 = 79. Tổng 20 số hạng đầu: S₂₀ = 20·(u₁ + u₂₀)/2 = 10·(3 + 79) = 820.",
        "Cho cấp số nhân (uₙ) có u₁ = 2 và công bội q = 3. Tổng của 5 số hạng đầu tiên S₅ của cấp số nhân đó bằng:",
        ["162", "242", "80", "484"],
        1,
        "Một người gửi tiết kiệm ngân hàng theo hình thức lãi kép với số tiền ban đầu là 50 triệu đồng, lãi suất cố định 7%/năm (tiền lãi cuối mỗi năm được cộng gộp vào gốc để tính lãi năm sau). Hỏi sau đúng 10 năm người đó nhận được cả vốn lẫn lãi là bao nhiêu (làm tròn đến hàng phần trăm triệu đồng)?",
        "Số tiền sau mỗi năm lập thành cấp số nhân với u₀ = 50 (triệu đồng) và công bội q = 1 + 0,07 = 1,07. Sau 10 năm, tổng số tiền cả vốn lẫn lãi là: A₁₀ = 50 · (1,07)¹⁰ ≈ 50 · 1,96715 ≈ 98,36 (triệu đồng).",
    ),
    M(
        11,
        "gioi-han",
        "Giới hạn của Dãy số, Giới hạn của Hàm số & Hàm số liên tục",
        "♾️",
        "Tính giới hạn dãy số, giới hạn hàm số (khử dạng vô định 0/0, ∞/∞, ∞ − ∞) và xét tính liên tục của hàm số.",
        "Giới hạn mô tả xu hướng hội tụ của một dãy số khi n → +∞ hoặc của hàm số f(x) khi x tiến dần tới x₀ (hoặc ±∞), là nền tảng trực tiếp để định nghĩa đạo hàm và tích phân.",
        "• Giới hạn cơ bản của dãy số: lim (1/nᵏ) = 0 (k ∈ ℕ*), lim qⁿ = 0 (|q| < 1) và kỹ thuật chia cả tử và mẫu cho lũy thừa bậc cao nhất của n.\n"
        "• Giới hạn hữu hạn, giới hạn một bên (x → x₀⁺, x → x₀⁻) và giới hạn ở vô cực của hàm số; kỹ thuật phân tích nhân tử hoặc nhân lượng liên hợp để khử dạng vô định 0/0.\n"
        "• Hàm số liên tục tại một điểm x₀ (lim[x→x₀] f(x) = f(x₀)), liên tục trên một khoảng/đoạn và định lý giá trị trung gian (chứng minh phương trình có nghiệm).",
        [
            {
                "category": "I. Giới hạn cơ bản của Dãy số (khi n → +∞)",
                "items": [
                    {"name": "Giới hạn bằng 0", "formula": "lim (1 / nᵏ) = 0 (với k > 0)  ;  lim qⁿ = 0 (với |q| < 1)", "note": ""},
                    {"name": "Phân thức đa thức theo n", "formula": "lim (a₀nᵖ + ...) / (b₀nᵍ + ...) = { a₀/b₀ nếu p = q ; 0 nếu p < q ; ±∞ nếu p > q }", "note": "So sánh bậc cao nhất của tử và mẫu"},
                ],
            },
            {
                "category": "II. Giới hạn của Hàm số & Khử dạng vô định",
                "items": [
                    {"name": "Tồn tại giới hạn tại x₀", "formula": "lim[x→x₀] f(x) = L  ⇔  lim[x→x₀⁺] f(x) = lim[x→x₀⁻] f(x) = L", "note": "Giới hạn phải bằng giới hạn trái"},
                    {"name": "Dạng vô định 0/0", "formula": "Phân tích tử & mẫu chứa nhân tử (x − x₀) hoặc nhân lượng liên hợp cho căn thức", "note": "√A − √B = (A − B)/(√A + √B)"},
                    {"name": "Giới hạn lượng giác đặc biệt", "formula": "lim[x→0] (sin x) / x = 1", "note": ""},
                ],
            },
            {
                "category": "III. Hàm số liên tục & Định lý nghiệm trên đoạn [a; b]",
                "items": [
                    {"name": "Điều kiện liên tục tại x₀", "formula": "lim[x→x₀] f(x) = f(x₀)  ⇔  lim[x→x₀⁺] f(x) = lim[x→x₀⁻] f(x) = f(x₀)", "note": ""},
                    {"name": "Sự tồn tại nghiệm", "formula": "Nếu f(x) liên tục trên [a; b] và f(a) · f(b) < 0 ⇒ ∃c ∈ (a; b) sao cho f(c) = 0", "note": "Có ít nhất 1 nghiệm thuộc (a; b)"},
                ],
            },
        ],
        "Cầu nối từ toán học sơ cấp sang giải tích hiện đại, mô tả vận tốc tức thời và trạng thái ổn định lâu dài của các hệ thống tự nhiên.",
        "Tính nồng độ thuốc ổn định trong máu khi dùng định kỳ lâu dài, kiểm tra tính trơn tru không gián đoạn của quỹ đạo robot.",
        "Tính giới hạn: L = lim[x→2] [ √(x + 2) − 2 ] / (x − 2).",
        "Đây là dạng 0/0. Nhân cả tử và mẫu với lượng liên hợp (√(x + 2) + 2): L = lim[x→2] (x + 2 − 4) / [ (x − 2)(√(x + 2) + 2) ] = lim[x→2] 1 / (√(x + 2) + 2) = 1 / (2 + 2) = 1/4.",
        "Giá trị của giới hạn lim[n→+∞] (3n² − 2n + 1) / (n² + 4) bằng:",
        ["0", "1/4", "3", "+∞"],
        2,
        "Tìm giá trị của tham số m để hàm số f(x) = { (x² − 9)/(x − 3) khi x ≠ 3 ; 2m + 1 khi x = 3 } liên tục tại điểm x₀ = 3.",
        "Ta có lim[x→3] f(x) = lim[x→3] (x − 3)(x + 3)/(x − 3) = lim[x→3] (x + 3) = 6, và f(3) = 2m + 1. Để hàm số liên tục tại x = 3 thì lim[x→3] f(x) = f(3) ⇔ 2m + 1 = 6 ⇔ m = 5/2.",
    ),
    M(
        11,
        "mu-logarit",
        "Lũy thừa với số mũ thực, Hàm số Mũ - Lôgarit & Phương trình, Bất phương trình Mũ - Lôgarit",
        "🚀",
        "Làm chủ phép tính lũy thừa số mũ thực, các quy tắc lôgarit, đồ thị hàm số mũ - lôgarit và giải phương trình, bất phương trình.",
        "Lôgarit cơ số a (0 < a ≠ 1) của một số dương b là số mũ α mà ta cần nâng cơ số a lên để được b: α = logₐ b ⇔ a^α = b.",
        "• Lũy thừa với số mũ nguyên âm, số mũ hữu tỉ (a^(m/n) = ⁿ√(aᵐ)) và số mũ thực.\n"
        "• Định nghĩa và trọn bộ quy tắc tính Lôgarit (tích, thương, lũy thừa, công thức đổi cơ số); lôgarit thập phân (log x = log₁₀ x) và lôgarit tự nhiên (ln x = logₑ x, với e ≈ 2,71828).\n"
        "• Tập xác định, sự biến thiên và đồ thị của hàm số mũ y = aˣ và hàm số lôgarit y = logₐ x (chú ý 2 trường hợp: a > 1 đồng biến; 0 < a < 1 nghịch biến).\n"
        "• Giải phương trình và bất phương trình mũ, lôgarit (lưu ý đổi chiều bất phương trình khi cơ số 0 < a < 1).",
        [
            {
                "category": "I. Công thức Lũy thừa với số mũ thực (a, b > 0)",
                "items": [
                    {"name": "Mũ nguyên âm & Mũ phân số", "formula": "a⁻ⁿ = 1 / aⁿ  ;  a^(m/n) = ⁿ√(aᵐ) (với n ∈ ℕ, n ≥ 2)", "note": ""},
                    {"name": "Các quy tắc lũy thừa", "formula": "aˣ · aʸ = aˣ⁺ʸ ; aˣ / aʸ = aˣ⁻ʸ ; (aˣ)ʸ = aˣ·ʸ ; (ab)ˣ = aˣbˣ", "note": ""},
                ],
            },
            {
                "category": "II. Trọn bộ Công thức Lôgarit (0 < a ≠ 1 ; b, c > 0)",
                "items": [
                    {"name": "Định nghĩa & Tính chất cơ bản", "formula": "logₐ b = α ⇔ a^α = b ; logₐ 1 = 0 ; logₐ a = 1 ; a^(logₐ b) = b", "note": ""},
                    {"name": "Lôgarit của tích, thương, lũy thừa", "formula": "logₐ(bc) = logₐ b + logₐ c ; logₐ(b/c) = logₐ b − logₐ c ; logₐ(b^α) = α·logₐ b", "note": "log_(a^β) b = (1/β)·logₐ b"},
                    {"name": "Công thức đổi cơ số (0 < c ≠ 1)", "formula": "logₐ b = (log_c b) / (log_c a)  ⇒  logₐ b · log_b c = logₐ c  ;  logₐ b = 1 / log_b a", "note": ""},
                ],
            },
            {
                "category": "III. Phương trình & Bất phương trình Mũ - Lôgarit cơ bản",
                "items": [
                    {"name": "Phương trình cơ bản", "formula": "a^f(x) = b (b > 0) ⇔ f(x) = logₐ b  ;  logₐ f(x) = b ⇔ f(x) = aᵇ", "note": "ĐK của logₐ f(x) là f(x) > 0"},
                    {"name": "Bất phương trình mũ a^f(x) > a^g(x)", "formula": "Nếu a > 1 ⇔ f(x) > g(x) (cùng chiều)  ;  Nếu 0 < a < 1 ⇔ f(x) < g(x) (ĐỔI CHIỀU)", "note": "Tương tự cho bất phương trình logₐ f(x) > logₐ g(x)"},
                ],
            },
        ],
        "Ứng dụng rộng rãi trong công thức lãi kép liên tục, đo độ pH hóa học, cường độ âm thanh (Decibel), độ mạnh động đất (độ Richter) và chu kỳ bán rã.",
        "Tính thời gian để số tiền gửi ngân hàng tăng gấp đôi, đo mức cường độ âm L = 10·log(I/I₀) (dB).",
        "Cho a > 0, a ≠ 1 và b > 0 thỏa mãn logₐ b = 3. Tính giá trị của biểu thức P = logₐ(a² · b³) − log_(√a)(b).",
        "Ta có: P = logₐ(a²) + logₐ(b³) − 2·logₐ b = 2 + 3·logₐ b − 2·logₐ b = 2 + logₐ b = 2 + 3 = 5.",
        "Tập nghiệm của bất phương trình log_(1/2)(x − 1) ≥ −2 là:",
        ["(1; 5]", "[5; +∞)", "(−∞; 5]", "(1; 3]"],
        0,
        "Dân số của một thành phố được ước tính theo công thức tăng trưởng mũ P(t) = P₀ · (1 + r)ᵗ, trong đó P₀ = 2 triệu người là dân số ban đầu và tốc độ tăng trưởng hàng năm là r = 1,5%/năm. Hỏi sau ít nhất bao nhiêu năm thì dân số thành phố đó vượt mức 2,5 triệu người? (Biết log₁,₀₁₅(1,25) ≈ 14,99).",
        "Ta cần P(t) > 2,5 ⇔ 2 · (1,015)ᵗ > 2,5 ⇔ (1,015)ᵗ > 1,25 ⇔ t > log₁,₀₁₅(1,25) ≈ 14,99. Vậy sau ít nhất 15 năm thì dân số thành phố vượt 2,5 triệu người.",
    ),
    M(
        11,
        "dao-ham",
        "Đạo hàm, Các quy tắc tính Đạo hàm & Ý nghĩa Hình học - Vật lý",
        "⚡",
        "Nắm vững định nghĩa đạo hàm, bảng đạo hàm sơ cấp - hàm hợp, phương trình tiếp tuyến và vận tốc - gia tốc tức thời.",
        "Đạo hàm của hàm số y = f(x) tại điểm x₀ biểu thị tốc độ biến thiên tức thời của hàm số tại điểm đó, được định nghĩa bởi giới hạn f'(x₀) = lim[Δx→0] [f(x₀ + Δx) − f(x₀)] / Δx.",
        "• Ý nghĩa hình học: f'(x₀) là hệ số góc của tiếp tuyến với đồ thị hàm số y = f(x) tại điểm M₀(x₀; f(x₀)).\n"
        "• Ý nghĩa vật lý: Nếu phương trình chuyển động là s = s(t) thì vận tốc tức thời v(t) = s'(t) và gia tốc tức thời a(t) = v'(t) = s''(t).\n"
        "• Quy tắc đạo hàm của tổng, hiệu, tích, thương, đạo hàm của hàm hợp y'_x = y'_u · u'_x và đạo hàm cấp hai f''(x).",
        [
            {
                "category": "I. Quy tắc tính Đạo hàm & Đạo hàm hàm hợp",
                "items": [
                    {"name": "Tổng, Hiệu, Tích với hằng số", "formula": "(u ± v)' = u' ± v'  ;  (k · u)' = k · u'", "note": ""},
                    {"name": "Đạo hàm của Tích & Thương", "formula": "(u · v)' = u'v + uv'  ;  (u / v)' = (u'v − uv') / v² ; (1 / v)' = −v' / v²", "note": "v ≠ 0"},
                    {"name": "Đạo hàm của Hàm hợp y = f(u(x))", "formula": "[f(u(x))]' = f'(u) · u'(x)", "note": "Ví dụ: (√u)' = u' / (2√u)"},
                ],
            },
            {
                "category": "II. Bảng Đạo hàm các hàm số sơ cấp & Hàm hợp u = u(x)",
                "items": [
                    {"name": "Hằng số, Lũy thừa & Căn bậc hai", "formula": "(C)' = 0 ; (xⁿ)' = n·xⁿ⁻¹ ⇒ (uⁿ)' = n·uⁿ⁻¹·u' ; (√x)' = 1/(2√x) ⇒ (√u)' = u'/(2√u)", "note": ""},
                    {"name": "Hàm lượng giác", "formula": "(sin u)' = u'·cos u ; (cos u)' = −u'·sin u ; (tan u)' = u'/cos²u ; (cot u)' = −u'/sin²u", "note": ""},
                    {"name": "Hàm số Mũ & Lôgarit", "formula": "(eᵘ)' = u'·eᵘ ; (aᵘ)' = u'·aᵘ·ln a ; (ln u)' = u'/u ; (logₐ u)' = u'/(u·ln a)", "note": ""},
                ],
            },
            {
                "category": "III. Phương trình Tiếp tuyến & Vận tốc - Gia tốc",
                "items": [
                    {"name": "Phương trình tiếp tuyến tại M₀(x₀; y₀)", "formula": "y = f'(x₀)(x − x₀) + f(x₀)", "note": "Hệ số góc k = f'(x₀)"},
                    {"name": "Vận tốc & Gia tốc tức thời", "formula": "v(t) = s'(t)  ;  a(t) = v'(t) = s''(t)", "note": "Cường độ dòng điện tức thời: i(t) = q'(t)"},
                ],
            },
        ],
        "Công cụ nền tảng nhất của giải tích dùng để khảo sát hàm số, tìm cực trị tối ưu và phân tích động lực học.",
        "Tính vận tốc và gia tốc tức thời của tàu cao tốc, lập phương trình tiếp tuyến và tối ưu hóa chi phí.",
        "Viết phương trình tiếp tuyến của đồ thị hàm số (C): y = x³ − 3x² + 2 tại điểm M có hoành độ x₀ = 3.",
        "Ta có y(3) = 3³ − 3·3² + 2 = 2 ⇒ M(3; 2). Đạo hàm y' = 3x² − 6x ⇒ hệ số góc k = y'(3) = 3·3² − 6·3 = 9. Phương trình tiếp tuyến tại M là: y = 9(x − 3) + 2 ⇔ y = 9x − 25.",
        "Một chất điểm chuyển động thẳng theo phương trình s(t) = −t³ + 6t² + 9t (trong đó t tính bằng giây, s tính bằng mét). Vận tốc lớn nhất mà chất điểm đạt được trong quá trình chuyển động là:",
        ["15 m/s", "21 m/s", "24 m/s", "36 m/s"],
        1,
        "Cho hàm số y = ln(x² + 1). Tính đạo hàm y' và giải phương trình y'(x) = 1.",
        "Áp dụng công thức (ln u)' = u'/u: y' = (x² + 1)' / (x² + 1) = 2x / (x² + 1). Khi đó y'(x) = 1 ⇔ 2x / (x² + 1) = 1 ⇔ x² − 2x + 1 = 0 ⇔ (x − 1)² = 0 ⇔ x = 1.",
        game_title="Điều khiển xe đạt tốc độ tối ưu bằng Đạo hàm",
        game_description="Xây dựng hàm quãng đường s(t), dùng đạo hàm v(t) = s'(t) và a(t) = s''(t) để xác định thời điểm xe đạt vận tốc cực đại.",
        game_type="function_challenge",
    ),
    M(
        11,
        "hinh-hoc",
        "Hình học không gian: Quan hệ Song song, Vuông góc, Góc - Khoảng cách & Thể tích khối đa diện",
        "🧊",
        "Chứng minh đường thẳng song song/vuông góc mặt phẳng, xác định góc - khoảng cách và tính thể tích khối chóp, lăng trụ.",
        "Hình học không gian lớp 11 xây dựng hệ thống định lý về quan hệ song song, quan hệ vuông góc trong không gian 3 chiều, kỹ thuật dựng góc - khoảng cách và công thức thể tích khối đa diện.",
        "• Quan hệ song song: Đường thẳng song song mặt phẳng, hai mặt phẳng song song, phép chiếu song song.\n"
        "• Quan hệ vuông góc: Đường thẳng vuông góc với mặt phẳng (d ⊥ (P) khi d vuông góc với 2 đường thẳng cắt nhau nằm trong (P)), định lý ba đường vuông góc, hai mặt phẳng vuông góc.\n"
        "• Góc giữa đường thẳng và mặt phẳng, góc nhị diện [P, d, Q] và khoảng cách từ điểm đến mặt phẳng, khoảng cách giữa hai đường thẳng chéo nhau.\n"
        "• Công thức thể tích khối chóp, khối lăng trụ và khối chóp cụt đều.",
        [
            {
                "category": "I. Điều kiện Vuông góc & Góc trong không gian",
                "items": [
                    {"name": "Đường thẳng vuông góc mặt phẳng", "formula": "d ⊥ a, d ⊥ b (với a, b ⊂ (P) và a cắt b) ⇒ d ⊥ (P)", "note": "Khi d ⊥ (P) thì d vuông góc với MỌI đường nằm trong (P)"},
                    {"name": "Góc giữa đường thẳng d và mặt phẳng (P)", "formula": "(d, (P)) = (d, d') với d' là hình chiếu vuông góc của d lên (P)", "note": "0° ≤ (d, (P)) ≤ 90°"},
                    {"name": "Hệ thức diện tích hình chiếu đa giác", "formula": "S_chiếu = S_gốc · cos φ", "note": "φ là góc giữa hai mặt phẳng"},
                ],
            },
            {
                "category": "II. Khoảng cách & Thể tích Khối đa diện",
                "items": [
                    {"name": "Tỉ số khoảng cách từ 2 điểm A, B đến (P)", "formula": "Nếu AB cắt (P) tại I ⇒ d(A, (P)) / d(B, (P)) = IA / IB", "note": "Dùng để quy khoảng cách từ điểm khó về chân đường cao H"},
                    {"name": "Thể tích Khối chóp & Khối lăng trụ", "formula": "V_chóp = (1/3) · S_đáy · h  ;  V_lăng_trụ = S_đáy · h", "note": "Hình hộp chữ nhật: V = a·b·c ; Lập phương: V = a³"},
                    {"name": "Thể tích Khối chóp cụt đều (diện tích 2 đáy B, B')", "formula": "V_chóp_cụt = (1/3) · h · (B + B' + √(B · B'))", "note": ""},
                ],
            },
        ],
        "Phát triển tư duy không gian 3D phục vụ kiến trúc, xây dựng cầu đường, cơ khí chế tạo và thiết kế đồ họa 3D.",
        "Tính thể tích kết cấu bê tông móng trụ cầu, độ nghiêng mái dốc và khoảng cách an toàn giữa hai đường ống chéo nhau.",
        "Cho hình chóp S.ABCD có đáy ABCD là hình vuông cạnh a, cạnh bên SA vuông góc với mặt phẳng đáy và SA = a√3. Tính góc giữa đường thẳng SC và mặt phẳng (ABCD) cùng thể tích khối chóp S.ABCD.",
        "Vì SA ⊥ (ABCD) nên AC là hình chiếu vuông góc của SC lên (ABCD) ⇒ góc giữa SC và (ABCD) là ∠SCA. Đáy là hình vuông cạnh a nên AC = a√2. Trong ΔSAC vuông tại A: tan(∠SCA) = SA / AC = (a√3)/(a√2) = √6/2. Thể tích khối chóp: V = (1/3) · S_ABCD · SA = (1/3) · a² · a√3 = (a³√3)/3.",
        "Trong hình chóp S.ABC có SA ⊥ (ABC) và đáy ABC là tam giác vuông tại B. Khẳng định nào dưới đây là ĐÚNG?",
        [
            "BC ⊥ (SAB)",
            "BC ⊥ (SAC)",
            "AC ⊥ (SAB)",
            "AB ⊥ (SBC)",
        ],
        0,
        "Cho hình chóp S.ABCD có đáy ABCD là hình vuông cạnh a, SA ⊥ (ABCD) và SA = a. Tính khoảng cách từ điểm A đến mặt phẳng (SBD).",
        "Gọi O là giao điểm của AC và BD ⇒ AO = a√2 / 2 và BD ⊥ AC, BD ⊥ SA ⇒ BD ⊥ (SAC) ⇒ (SBD) ⊥ (SAC) theo giao tuyến SO. Trong ΔSAO vuông tại A, kẻ AH ⊥ SO tại H thì AH ⊥ (SBD) nên d(A, (SBD)) = AH. Ta có: 1/AH² = 1/SA² + 1/AO² = 1/a² + 2/a² = 3/a² ⇒ AH = a√3 / 3.",
    ),
    M(
        11,
        "xac-suat",
        "Các quy tắc tính Xác suất: Biến cố hợp, Biến cố giao & Biến cố độc lập",
        "🎲",
        "Nắm vững quy tắc cộng xác suất cho hai biến cố xung khắc/bất kỳ và quy tắc nhân xác suất cho hai biến cố độc lập.",
        "Ở lớp 11, lý thuyết xác suất chuyển từ đếm trực tiếp sang vận dụng đại số biến cố (biến cố hợp A ∪ B, biến cố giao A ∩ B = AB, biến cố xung khắc, biến cố độc lập) để giải các bài toán xác suất phức tạp.",
        "• Biến cố hợp A ∪ B (ít nhất một trong hai biến cố xảy ra) và Biến cố giao AB (cả hai biến cố đồng thời xảy ra).\n"
        "• Hai biến cố xung khắc (A ∩ B = ∅: không bao giờ cùng xảy ra) và quy tắc cộng xác suất.\n"
        "• Hai biến cố độc lập (việc xảy ra hay không xảy ra của biến cố này không làm ảnh hưởng tới xác suất xảy ra của biến cố kia) và quy tắc nhân xác suất.",
        [
            {
                "category": "I. Quy tắc Cộng xác suất (Biến cố Hợp A ∪ B)",
                "items": [
                    {"name": "Hai biến cố xung khắc (A ∩ B = ∅)", "formula": "P(A ∪ B) = P(A) + P(B)", "note": ""},
                    {"name": "Hai biến cố bất kỳ", "formula": "P(A ∪ B) = P(A) + P(B) − P(AB)", "note": "Công thức cộng xác suất tổng quát"},
                    {"name": "Biến cố đối Ā", "formula": "P(Ā) = 1 − P(A)", "note": "A và Ā là hai biến cố đối nhau (xung khắc và A ∪ Ā = Ω)"},
                ],
            },
            {
                "category": "II. Biến cố độc lập & Quy tắc Nhân xác suất",
                "items": [
                    {"name": "Quy tắc nhân (A và B độc lập)", "formula": "P(AB) = P(A) · P(B)", "note": "Nếu A, B độc lập thì (A, B̄), (Ā, B), (Ā, B̄) cũng độc lập"},
                    {"name": "Xác suất có ít nhất 1 biến cố xảy ra (khi A, B độc lập)", "formula": "P(A ∪ B) = 1 − P(Ā · B̄) = 1 − P(Ā) · P(B̄)", "note": "Cách tính cực nhanh cho hệ n thành phần độc lập"},
                ],
            },
        ],
        "Đánh giá độ tin cậy của hệ thống kỹ thuật nhiều động cơ/máy chủ dự phòng, phân tích rủi ro y sinh và bảo hiểm.",
        "Tính xác suất hoạt động an toàn của máy bay có 2 động cơ độc lập, hoặc xác suất bắn trúng bia của hai xạ thủ.",
        "Hai xạ thủ độc lập nhau cùng bắn vào một tấm bia (mỗi người bắn 1 viên). Xác suất bắn trúng bia của người thứ nhất là 0,8 và của người thứ hai là 0,7. Tính xác suất để tấm bia bị bắn trúng (có ít nhất 1 người bắn trúng).",
        "Gọi A, B là biến cố người 1, người 2 bắn trúng bia ⇒ P(A) = 0,8 (P(Ā) = 0,2) và P(B) = 0,7 (P(B̄) = 0,3). Vì A, B độc lập nên xác suất cả hai cùng trượt là P(ĀB̄) = 0,2 · 0,3 = 0,06. Vậy xác suất tấm bia bị bắn trúng là: P(A ∪ B) = 1 − 0,06 = 0,94.",
        "Cho hai biến cố A và B có P(A) = 0,5; P(B) = 0,6 và P(AB) = 0,3. Khi đó xác suất của biến cố hợp P(A ∪ B) bằng:",
        ["0,8", "1,1", "0,9", "0,7"],
        0,
        "Một hệ thống máy chủ gồm 3 cụm server hoạt động độc lập với xác suất hoạt động tốt trong ngày của mỗi cụm đều bằng 0,9. Hệ thống vẫn duy trì hoạt động bình thường nếu có ít nhất 1 cụm server hoạt động tốt. Tính xác suất để hệ thống hoạt động bình thường trong ngày.",
        "Xác suất một cụm server bị sự cố là 1 − 0,9 = 0,1. Do 3 cụm độc lập nên xác suất cả 3 cụm đồng thời gặp sự cố là: (0,1)³ = 0,001. Vậy xác suất hệ thống hoạt động bình thường là: 1 − 0,001 = 0,999 (hay 99,9%).",
    ),
    M(
        11,
        "thong-ke",
        "Mẫu số liệu ghép nhóm & Các số đặc trưng đo xu thế trung tâm",
        "📊",
        "Chuyển đổi mẫu số liệu sang dạng ghép nhóm theo các nửa khoảng [aᵢ; aᵢ₊₁) và tính số trung bình, trung vị, tứ phân vị, mốt.",
        "Khi mẫu số liệu có kích thước lớn hoặc biến thiên liên tục (chiều cao, thời gian, thu nhập), ta ghép các số liệu thành các nhóm có dạng [aᵢ; aᵢ₊₁) và sử dụng giá trị đại diện cᵢ = (aᵢ + aᵢ₊₁)/2.",
        "• Bảng tần số ghép nhóm: độ dài nhóm L = aᵢ₊₁ − aᵢ, giá trị đại diện cᵢ = (aᵢ + aᵢ₊₁)/2.\n"
        "• Công thức tính Số trung bình x̄ của mẫu số liệu ghép nhóm.\n"
        "• Công thức nội suy tính Trung vị (Mₑ), Tứ phân vị (Q₁, Q₂, Q₃) và Mốt (M₀) của mẫu số liệu ghép nhóm.",
        [
            {
                "category": "I. Giá trị đại diện & Số trung bình của mẫu ghép nhóm",
                "items": [
                    {"name": "Giá trị đại diện của nhóm [aᵢ; aᵢ₊₁)", "formula": "cᵢ = (aᵢ + aᵢ₊₁) / 2", "note": "Trung điểm của đoạn [aᵢ; aᵢ₊₁]"},
                    {"name": "Số trung bình cộng x̄", "formula": "x̄ = (n₁c₁ + n₂c₂ + ... + nₖcₖ) / n", "note": "n = n₁ + n₂ + ... + nₖ là cỡ mẫu"},
                ],
            },
            {
                "category": "II. Trung vị, Tứ phân vị & Mốt của mẫu số liệu ghép nhóm",
                "items": [
                    {"name": "Trung vị Mₑ = Q₂ (thuộc nhóm [uₘ; uₘ₊₁))", "formula": "Mₑ = uₘ + [ (n/2 − C) / nₘ ] · (uₘ₊₁ − uₘ)", "note": "C: tần số tích lũy trước nhóm m ; nₘ: tần số nhóm m"},
                    {"name": "Tứ phân vị Qₖ (k = 1, 2, 3)", "formula": "Qₖ = uₘ + [ (k·n/4 − C) / nₘ ] · (uₘ₊₁ − uₘ)", "note": "Thay n/2 bằng n/4 (cho Q₁) hoặc 3n/4 (cho Q₃)"},
                    {"name": "Mốt M₀ (nhóm [uₘ; uₘ₊₁) có tần số lớn nhất)", "formula": "M₀ = uₘ + [ (nₘ − nₘ₋₁) / ((nₘ − nₘ₋₁) + (nₘ − nₘ₊₁)) ] · (uₘ₊₁ − uₘ)", "note": ""},
                ],
            },
        ],
        "Xử lý các bộ dữ liệu lớn (Big Data) trong điều tra dân số, thu nhập bình quân, y tế cộng đồng và kiểm định công nghiệp.",
        "Tính thời gian tự học trung bình của học sinh toàn trường, phân tích phổ điểm thi tốt nghiệp THPT.",
        "Khảo sát thời gian tập thể dục mỗi ngày (phút) của 40 người thu được bảng ghép nhóm: [0; 20): 5 người; [20; 40): 15 người; [40; 60): 12 người; [60; 80): 8 người. Tính thời gian tập trung bình x̄ và trung vị Mₑ.",
        "Giá trị đại diện các nhóm: c₁ = 10, c₂ = 30, c₃ = 50, c₄ = 70. Số trung bình: x̄ = (5·10 + 15·30 + 12·50 + 8·70)/40 = 1660/40 = 41,5 (phút). Vì n/2 = 20 và 5 + 15 = 20 nên nhóm chứa trung vị là [40; 60) (hoặc mốc ranh giới 40): Mₑ = 40 + [(20 − 20)/12]·20 = 40 (phút).",
        "Trong mẫu số liệu ghép nhóm, giá trị đại diện của nhóm [150; 160) là:",
        ["150", "160", "155", "10"],
        2,
        "Với bảng số liệu 40 người tập thể dục ở ví dụ trên ([0; 20): 5; [20; 40): 15; [40; 60): 12; [60; 80): 8), hãy tìm nhóm chứa Mốt và tính giá trị Mốt M₀ của mẫu số liệu.",
        "Nhóm có tần số lớn nhất là nhóm 2: [20; 40) với n₂ = 15 (n₁ = 5, n₃ = 12, độ dài nhóm h = 20). Áp dụng công thức: M₀ = 20 + [ (15 − 5) / ((15 − 5) + (15 − 12)) ] · 20 = 20 + (10 / 13) · 20 ≈ 35,38 (phút).",
    ),

    # =========================================================
    # TOÁN 12 (8 BÀI)
    # =========================================================
    M(
        12,
        "ham-so",
        "Ứng dụng Đạo hàm để Khảo sát và Vẽ đồ thị của Hàm số",
        "📈",
        "Xét tính đơn điệu, tìm cực trị, giá trị lớn nhất - nhỏ nhất (GTLN - GTNN), đường tiệm cận (đứng, ngang, xiên) và khảo sát đồ thị.",
        "Khảo sát hàm số sử dụng đạo hàm cấp 1 và cấp 2 để phân tích toàn diện sự biến thiên (đồng biến, nghịch biến), điểm cực đại - cực tiểu, GTLN - GTNN và các đường tiệm cận của đồ thị hàm số.",
        "• Tính đơn điệu: f'(x) ≥ 0 trên K (bằng 0 tại hữu hạn điểm) ⇒ f(x) đồng biến trên K; f'(x) ≤ 0 ⇒ nghịch biến.\n"
        "• Cực trị của hàm số: f'(x) đổi dấu từ '+' sang '−' khi qua x₀ ⇒ x₀ là điểm cực đại; đổi từ '−' sang '+' ⇒ điểm cực tiểu.\n"
        "• Tìm GTLN (max) và GTNN (min) của hàm số trên đoạn [a; b] và trong các bài toán tối ưu hóa thực tế.\n"
        "• Ba loại đường tiệm cận: Tiệm cận đứng (x = x₀), Tiệm cận ngang (y = y₀) và Tiệm cận xiên (y = ax + b).\n"
        "• Khảo sát hàm bậc ba y = ax³ + bx² + cx + d, hàm phân thức bậc nhất/bậc nhất y = (ax+b)/(cx+d) và hàm bậc hai/bậc nhất y = (ax²+bx+c)/(mx+n).",
        [
            {
                "category": "I. Tính đơn điệu, Cực trị & GTLN - GTNN trên đoạn [a; b]",
                "items": [
                    {"name": "Định lý đơn điệu", "formula": "f'(x) > 0, ∀x ∈ K ⇒ f(x) đồng biến trên K  ;  f'(x) < 0, ∀x ∈ K ⇒ f(x) nghịch biến trên K", "note": ""},
                    {"name": "Điều kiện Cực trị", "formula": "Điều kiện cần (hàm khả vi): f'(x₀) = 0 ; Điều kiện đủ: f'(x) đổi dấu khi qua x₀ (hoặc f''(x₀) ≠ 0)", "note": ""},
                    {"name": "Thuật toán tìm Max/Min trên đoạn [a; b]", "formula": "Giải f'(x) = 0 lấy xᵢ ∈ (a; b) ; Tính f(a), f(b), f(xᵢ) rồi so sánh chọn số lớn nhất / nhỏ nhất", "note": ""},
                ],
            },
            {
                "category": "II. Ba loại Đường tiệm cận của đồ thị hàm số y = f(x)",
                "items": [
                    {"name": "Tiệm cận ngang (TCN): y = y₀", "formula": "lim[x→+∞] f(x) = y₀  hoặc  lim[x→−∞] f(x) = y₀", "note": "Hàm y = (ax+b)/(cx+d) có TCN y = a/c"},
                    {"name": "Tiệm cận đứng (TCĐ): x = x₀", "formula": "lim[x→x₀⁺] f(x) = ±∞  hoặc  lim[x→x₀⁻] f(x) = ±∞", "note": "Hàm y = (ax+b)/(cx+d) có TCĐ x = −d/c"},
                    {"name": "Tiệm cận xiên (TCX): y = ax + b (a ≠ 0)", "formula": "a = lim[x→±∞] [f(x)/x]  và  b = lim[x→±∞] [f(x) − ax]  (hoặc chia đa thức tử cho mẫu)", "note": "Hàm y = P₂(x)/Q₁(x) = ax + b + r/(mx+n) có TCX y = ax + b"},
                ],
            },
        ],
        "Công cụ mạnh nhất để giải các bài toán tối ưu hóa chi phí sản xuất, thiết kế bao bì tiết kiệm nguyên liệu nhất và tối đa hóa lợi nhuận kinh tế.",
        "Thiết kế vỏ lon nước ngọt có dung tích cố định V = 330 ml sao cho tốn ít diện tích nhôm nhất, tìm tốc độ tàu chạy tiết kiệm nhiên liệu nhất.",
        "Tìm các đường tiệm cận đứng và tiệm cận xiên của đồ thị hàm số y = (2x² − 3x + 5) / (x − 2).",
        "Tập xác định D = ℝ \\ {2}. Vì lim[x→2⁺] y = +∞ và lim[x→2⁻] y = −∞ nên x = 2 là tiệm cận đứng. Chia đa thức tử cho mẫu: y = 2x + 1 + 7/(x − 2). Vì lim[x→±∞] [y − (2x + 1)] = lim[x→±∞] 7/(x − 2) = 0 nên đường thẳng y = 2x + 1 là tiệm cận xiên.",
        "Giá trị lớn nhất của hàm số f(x) = x³ − 3x² − 9x + 10 trên đoạn [−2; 2] bằng:",
        ["15", "10", "−12", "2"],
        0,
        "Từ một tấm tôn hình vuông có cạnh bằng 12 dm, người ta cắt bỏ ở bốn góc bốn hình vuông nhỏ bằng nhau có cạnh là x (dm), rồi gập các mép lên để hàn thành một chiếc hộp chữ nhật không có nắp. Hỏi phải chọn x bằng bao nhiêu đề-xi-mét để chiếc hộp tạo thành có thể tích lớn nhất?",
        "Điều kiện: 0 < x < 6. Đáy hộp là hình vuông cạnh (12 − 2x) dm và chiều cao hộp là x dm. Thể tích hộp: V(x) = x(12 − 2x)² = 4x³ − 48x² + 144x. Đạo hàm: V'(x) = 12x² − 96x + 144 = 0 ⇔ x² − 8x + 12 = 0 ⇔ x = 2 (nhận) hoặc x = 6 (loại). Tại x = 2 dm, thể tích đạt GTLN là V(2) = 2 · 8² = 128 (dm³).",
    ),
    M(
        12,
        "nguyen-ham",
        "Nguyên hàm & Bảng nguyên hàm của các hàm số sơ cấp",
        "∫",
        "Hiểu định nghĩa nguyên hàm F'(x) = f(x), tính chất tuyến tính và thuộc bảng nguyên hàm cơ bản.",
        "Cho hàm số f(x) xác định trên K. Hàm số F(x) được gọi là một nguyên hàm của f(x) trên K nếu F'(x) = f(x) với mọi x ∈ K. Họ tất cả các nguyên hàm của f(x) được ký hiệu là ∫f(x)dx = F(x) + C (C ∈ ℝ).",
        "• Định nghĩa và sự sai khác nhau một hằng số C giữa các nguyên hàm của cùng một hàm số.\n"
        "• Tính chất tuyến tính của nguyên hàm: nguyên hàm của tổng, hiệu và tích với hằng số khác 0.\n"
        "• Bảng nguyên hàm của các hàm số sơ cấp (lũy thừa, 1/x, hàm mũ, hàm lượng giác) và công thức mở rộng cho biểu thức bậc nhất ax + b.\n"
        "• Bài toán tìm nguyên hàm F(x) thỏa mãn điều kiện ban đầu F(x₀) = y₀ để xác định hằng số C.",
        [
            {
                "category": "I. Định nghĩa & Tính chất của Nguyên hàm",
                "items": [
                    {"name": "Định nghĩa Họ nguyên hàm", "formula": "∫f(x)dx = F(x) + C  ⇔  F'(x) = f(x)", "note": "Mọi nguyên hàm của f(x) đều có dạng F(x) + C"},
                    {"name": "Đạo hàm và Nguyên hàm ngược nhau", "formula": "( ∫f(x)dx )' = f(x)  ;  ∫F'(x)dx = F(x) + C", "note": ""},
                    {"name": "Tính chất tuyến tính", "formula": "∫[f(x) ± g(x)]dx = ∫f(x)dx ± ∫g(x)dx  ;  ∫k·f(x)dx = k·∫f(x)dx (k ≠ 0)", "note": "Lưu ý: KHÔNG có công thức tách tích/thương"},
                ],
            },
            {
                "category": "II. Bảng Nguyên hàm cơ bản & Mở rộng cho (ax + b)",
                "items": [
                    {"name": "Hằng số & Hàm lũy thừa (α ≠ −1)", "formula": "∫k dx = kx + C  ;  ∫x^α dx = x^(α+1)/(α + 1) + C  ;  ∫(ax+b)^α dx = (1/a)·(ax+b)^(α+1)/(α+1) + C", "note": ""},
                    {"name": "Hàm 1/x và 1/x²", "formula": "∫(1/x)dx = ln|x| + C  ;  ∫[1/(ax+b)]dx = (1/a)ln|ax+b| + C  ;  ∫(1/x²)dx = −1/x + C", "note": ""},
                    {"name": "Hàm số Mũ", "formula": "∫eˣ dx = eˣ + C  ;  ∫e^(ax+b) dx = (1/a)e^(ax+b) + C  ;  ∫aˣ dx = aˣ / ln a + C", "note": ""},
                    {"name": "Hàm Lượng giác", "formula": "∫sin x dx = −cos x + C ; ∫cos x dx = sin x + C ; ∫(1/cos²x)dx = tan x + C ; ∫(1/sin²x)dx = −cot x + C", "note": ""},
                ],
            },
        ],
        "Nguyên hàm là phép toán khôi phục lại hàm gốc từ tốc độ thay đổi tức thời (tìm quãng đường s(t) từ vận tốc v(t), tìm tổng chi phí từ chi phí biên).",
        "Khôi phục phương trình chuyển động s(t) = ∫v(t)dt khi biết biểu thức vận tốc và vị trí xuất phát ban đầu.",
        "Tìm nguyên hàm F(x) của hàm số f(x) = 3x² − 2/x + eˣ trên khoảng (0; +∞), biết rằng F(1) = e.",
        "Họ nguyên hàm là F(x) = ∫(3x² − 2/x + eˣ)dx = x³ − 2ln x + eˣ + C (vì x > 0). Thay điều kiện F(1) = e: 1³ − 2ln 1 + e¹ + C = e ⇔ 1 + e + C = e ⇔ C = −1. Vậy F(x) = x³ − 2ln x + eˣ − 1.",
        "Họ tất cả các nguyên hàm của hàm số f(x) = cos(2x) + 4x là:",
        [
            "2sin(2x) + 2x² + C",
            "(1/2)sin(2x) + 2x² + C",
            "−(1/2)sin(2x) + 2x² + C",
            "(1/2)sin(2x) + 4 + C",
        ],
        1,
        "Một ô tô đang chạy với vận tốc 20 m/s thì người lái đạp phanh; từ thời điểm đó ô tô chuyển động chậm dần đều với vận tốc v(t) = −4t + 20 (m/s), trong đó t là khoảng thời gian tính bằng giây kể từ lúc bắt đầu đạp phanh. Hãy lập hàm quãng đường s(t) mà ô tô đi được sau t giây (với s(0) = 0) và tính quãng đường ô tô đi thêm được từ lúc đạp phanh đến khi dừng hẳn.",
        "Ta có s(t) = ∫v(t)dt = ∫(−4t + 20)dt = −2t² + 20t + C. Vì s(0) = 0 nên C = 0 ⇒ s(t) = −2t² + 20t. Khi xe dừng hẳn thì v(t) = 0 ⇔ −4t + 20 = 0 ⇔ t = 5 (giây). Quãng đường đi thêm được là s(5) = −2·(5²) + 20·5 = 50 (m).",
    ),
    M(
        12,
        "tich-phan",
        "Tích phân & Ứng dụng hình học của Tích phân (Diện tích phẳng - Thể tích khối tròn xoay)",
        "📐",
        "Tính tích phân xác định bằng công thức Newton-Leibniz và ứng dụng tính diện tích hình phẳng, thể tích vật thể và khối tròn xoay.",
        "Cho f(x) là hàm số liên tục trên đoạn [a; b] và F(x) là một nguyên hàm bất kỳ của f(x) trên [a; b]. Hiệu số F(b) − F(a) được gọi là tích phân từ a đến b của hàm số f(x), ký hiệu ∫[a→b] f(x)dx.",
        "• Công thức Newton-Leibniz: ∫[a→b] f(x)dx = F(x)|[a→b] = F(b) − F(a).\n"
        "• Các tính chất của tích phân (đổi cận đổi dấu, tính chất chèn cận c: ∫[a→b] = ∫[a→c] + ∫[c→b]).\n"
        "• Ứng dụng 1: Tính diện tích hình phẳng giới hạn bởi các đường cong y = f(x), y = g(x) và hai đường thẳng x = a, x = b.\n"
        "• Ứng dụng 2: Tính thể tích vật thể theo diện tích thiết diện S(x) và thể tích khối tròn xoay khi quay hình phẳng quanh trục Ox.",
        [
            {
                "category": "I. Công thức Newton-Leibniz & Tính chất Tích phân",
                "items": [
                    {"name": "Công thức Newton-Leibniz", "formula": "I = ∫[a→b] f(x)dx = F(b) − F(a)  (với F'(x) = f(x))", "note": "Tích phân chỉ phụ thuộc vào hàm f và hai cận a, b; không phụ thuộc ký hiệu biến"},
                    {"name": "Đổi cận & Chèn cận", "formula": "∫[a→a] f(x)dx = 0 ; ∫[b→a] f(x)dx = −∫[a→b] f(x)dx ; ∫[a→b] f(x)dx = ∫[a→c] f(x)dx + ∫[c→b] f(x)dx", "note": ""},
                    {"name": "Quãng đường đi được từ t = a đến t = b", "formula": "S = ∫[a→b] |v(t)| dt", "note": "Nếu v(t) ≥ 0 trên [a; b] thì độ dịch chuyển bằng quãng đường"},
                ],
            },
            {
                "category": "II. Ứng dụng Tích phân tính Diện tích S & Thể tích V",
                "items": [
                    {"name": "Diện tích giới hạn bởi y = f(x), trục Ox, x = a, x = b", "formula": "S = ∫[a→b] |f(x)| dx", "note": "Xét dấu f(x) trên [a; b] để phá trị tuyệt đối"},
                    {"name": "Diện tích giới hạn bởi 2 đồ thị y = f(x), y = g(x), x = a, x = b", "formula": "S = ∫[a→b] |f(x) − g(x)| dx", "note": "Nếu chưa cho cận a, b thì giải f(x) = g(x) tìm nghiệm nhỏ nhất a, lớn nhất b"},
                    {"name": "Thể tích vật thể có diện tích mặt cắt S(x) (a ≤ x ≤ b)", "formula": "V = ∫[a→b] S(x) dx", "note": "Mặt cắt vuông góc với trục Ox tại hoành độ x"},
                    {"name": "Thể tích khối tròn xoay (quay y = f(x) quanh trục Ox)", "formula": "V = π · ∫[a→b] [f(x)]² dx", "note": "Lưu ý không quên nhân hệ số π ở ngoài"},
                ],
            },
        ],
        "Cho phép tính chính xác diện tích các mảnh đất có biên cong phức tạp, thể tích chi tiết máy tiện tròn xoay, bình gốm và điện lượng tích lũy.",
        "Tính diện tích mặt cắt vòm cổng Parabol, thể tích bình hoa cổ cong hoặc lượng nước chảy qua đập thủy điện.",
        "Tính diện tích hình phẳng giới hạn bởi Parabol (P): y = x² − 2x và đường thẳng (d): y = x.",
        "Phương trình hoành độ giao điểm: x² − 2x = x ⇔ x² − 3x = 0 ⇔ x = 0 hoặc x = 3. Trên đoạn [0; 3], x² − 3x ≤ 0 nên |x² − 3x| = 3x − x². Diện tích cần tìm là: S = ∫[0→3] (3x − x²)dx = (3x²/2 − x³/3)|[0→3] = 27/2 − 9 = 9/2 = 4,5 (đvdt).",
        "Cho hình phẳng (H) giới hạn bởi đồ thị hàm số y = √x, trục hoành Ox và hai đường thẳng x = 0, x = 4. Thể tích khối tròn xoay tạo thành khi quay (H) quanh trục Ox bằng:",
        ["8", "8π", "4π", "16π"],
        1,
        "Cho biết ∫[1→3] f(x)dx = 5 và ∫[1→3] g(x)dx = −2. Hãy tính giá trị của tích phân I = ∫[1→3] [2f(x) − 3g(x) + 4x]dx.",
        "Áp dụng tính chất tuyến tính: I = 2·∫[1→3] f(x)dx − 3·∫[1→3] g(x)dx + ∫[1→3] 4x dx = 2·5 − 3·(−2) + (2x²)|[1→3] = 10 + 6 + (18 − 2) = 32.",
    ),
    M(
        12,
        "hinh-hoc",
        "Vectơ trong không gian & Phương pháp tọa độ trong không gian Oxyz",
        "🌐",
        "Thành thạo hệ tọa độ Oxyz, tích có hướng của hai vectơ và phương trình Mặt phẳng, Đường thẳng, Mặt cầu trong không gian.",
        "Hệ tọa độ Descartes vuông góc Oxyz gắn cho mỗi điểm M trong không gian 3 chiều một bộ ba số thực duy nhất M(x; y; z), biến mọi bài toán hình học không gian thành đại số.",
        "• Tọa độ điểm, tọa độ vectơ, độ dài đoạn thẳng, tọa độ trung điểm và trọng tâm trong không gian Oxyz.\n"
        "• Tích vô hướng u⃗ · v⃗ và Tích có hướng [u⃗, v⃗] của hai vectơ cùng ứng dụng tính diện tích tam giác, thể tích tứ diện/hình hộp.\n"
        "• Phương trình tổng quát của mặt phẳng (P): Ax + By + Cz + D = 0 (vectơ pháp tuyến n⃗ = (A; B; C)) và khoảng cách từ điểm đến mặt phẳng.\n"
        "• Phương trình tham số và phương trình chính tắc của đường thẳng Δ (vectơ chỉ phương u⃗ = (a; b; c)); góc trong không gian.\n"
        "• Phương trình mặt cầu (S) tâm I(a; b; c) bán kính R.",
        [
            {
                "category": "I. Tọa độ Điểm, Vectơ, Tích vô hướng & Tích có hướng trong Oxyz",
                "items": [
                    {"name": "Vectơ AB⃗ & Khoảng cách AB", "formula": "AB⃗ = (x_B − x_A ; y_B − y_A ; z_B − z_A)  ;  AB = √[(x_B − x_A)² + (y_B − y_A)² + (z_B − z_A)²]", "note": ""},
                    {"name": "Trung điểm M & Trọng tâm G", "formula": "M( (x_A+x_B)/2 ; (y_A+y_B)/2 ; (z_A+z_B)/2 )  ;  G( (x_A+x_B+x_C)/3 ; (y_A+y_B+y_C)/3 ; (z_A+z_B+z_C)/3 )", "note": ""},
                    {"name": "Tích vô hướng u⃗ = (x₁;y₁;z₁), v⃗ = (x₂;y₂;z₂)", "formula": "u⃗ · v⃗ = x₁x₂ + y₁y₂ + z₁z₂  ;  cos(u⃗, v⃗) = (u⃗ · v⃗) / (|u⃗| · |v⃗|)", "note": "u⃗ ⊥ v⃗ ⇔ x₁x₂ + y₁y₂ + z₁z₂ = 0"},
                    {"name": "Tích có hướng [u⃗, v⃗]", "formula": "[u⃗, v⃗] = ( y₁z₂ − z₁y₂ ; z₁x₂ − x₁z₂ ; x₁y₂ − y₁x₂ )", "note": "[u⃗, v⃗] vuông góc với cả u⃗ và v⃗ ; S_ΔABC = (1/2)|[AB⃗, AC⃗]|"},
                ],
            },
            {
                "category": "II. Phương trình Mặt phẳng, Đường thẳng & Mặt cầu trong Oxyz",
                "items": [
                    {"name": "Mặt phẳng (P) qua M₀(x₀;y₀;z₀), VTPT n⃗=(A;B;C)", "formula": "A(x − x₀) + B(y − y₀) + C(z − z₀) = 0  ⇔  Ax + By + Cz + D = 0", "note": "Phương trình mặt chắn: x/a + y/b + z/c = 1"},
                    {"name": "Khoảng cách từ M₀ đến mặt phẳng (P)", "formula": "d(M₀, (P)) = |Ax₀ + By₀ + Cz₀ + D| / √(A² + B² + C²)", "note": ""},
                    {"name": "Đường thẳng d qua M₀(x₀;y₀;z₀), VTCP u⃗=(a;b;c)", "formula": "Tham số: {x = x₀ + at ; y = y₀ + bt ; z = z₀ + ct}  ;  Chính tắc: (x−x₀)/a = (y−y₀)/b = (z−z₀)/c", "note": ""},
                    {"name": "Mặt cầu (S) tâm I(a; b; c), bán kính R", "formula": "(x − a)² + (y − b)² + (z − c)² = R²  hoặc  x² + y² + z² − 2ax − 2by − 2cz + d = 0", "note": "Với R = √(a² + b² + c² − d)"},
                ],
            },
            {
                "category": "III. Công thức Góc giữa các đối tượng trong Oxyz",
                "items": [
                    {"name": "Góc giữa 2 đường thẳng & 2 mặt phẳng", "formula": "cos(d₁, d₂) = |u₁⃗ · u₂⃗| / (|u₁⃗||u₂⃗|)  ;  cos((P₁), (P₂)) = |n₁⃗ · n₂⃗| / (|n₁⃗||n₂⃗|)", "note": "Góc luôn thuộc [0°; 90°] nên có dấu trị tuyệt đối"},
                    {"name": "Góc giữa đường thẳng d và mặt phẳng (P)", "formula": "sin(d, (P)) = |u_d⃗ · n_P⃗| / (|u_d⃗| · |n_P⃗|)", "note": "Chú ý dùng SIN cho góc giữa đường và mặt"},
                ],
            },
        ],
        "Cơ sở toán học của định vị vệ tinh GPS, radar hàng không, điều khiển cánh tay robot công nghiệp và engine đồ họa game 3D.",
        "Theo dõi tọa độ máy bay từ trạm radar mặt đất, kiểm tra xem máy bay có nằm trong vùng phủ sóng hình cầu của trạm thu phát hay không.",
        "Trong không gian Oxyz, viết phương trình mặt cầu (S) có tâm I(1; −2; 3) và tiếp xúc với mặt phẳng (P): 2x − 2y + z + 3 = 0.",
        "Vì mặt cầu (S) tiếp xúc với mặt phẳng (P) nên bán kính R của mặt cầu bằng khoảng cách từ tâm I đến (P): R = d(I, (P)) = |2·1 − 2·(−2) + 3 + 3| / √(2² + (−2)² + 1²) = 12 / 3 = 4. Phương trình mặt cầu (S) là: (x − 1)² + (y + 2)² + (z − 3)² = 16.",
        "Trong không gian Oxyz, cho đường thẳng d: (x − 1)/2 = (y + 2)/(−1) = z/3. Một vectơ chỉ phương của đường thẳng d có tọa độ là:",
        ["(1; −2; 0)", "(2; −1; 3)", "(2; 1; 3)", "(−1; 2; 0)"],
        1,
        "Trong không gian Oxyz (đơn vị trên mỗi trục là km), một trạm radar đặt tại gốc tọa độ O(0; 0; 0) có bán kính quét sóng tối đa là R = 500 km. Một máy bay đang bay thẳng đều từ vị trí A(−600; 200; 10) đến vị trí B(600; 200; 10). Hãy viết phương trình tham số quỹ đạo bay AB và xác định độ dài quãng đường mà máy bay nằm trong vùng phủ sóng của trạm radar.",
        "Vectơ AB⃗ = (1200; 0; 0) cùng phương với u⃗ = (1; 0; 0). Phương trình đường bay AB là: { x = t ; y = 200 ; z = 10 } (t ∈ ℝ). Khoảng cách từ gốc O đến đường thẳng AB là h = √(0² + 200² + 10²) = √40100 (km) < R = 500 km. Độ dài dây cung quỹ đạo nằm trong mặt cầu bán kính R = 500 là: L = 2√(R² − h²) = 2√(500² − 40100) = 2√209900 ≈ 916,3 (km).",
    ),
    M(
        12,
        "thong-ke-ghep-nhom",
        "Các số đặc trưng đo mức độ phân tán của Mẫu số liệu ghép nhóm",
        "📊",
        "Tính khoảng biến thiên, khoảng tứ phân vị, phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm để đánh giá độ ổn định và rủi ro.",
        "Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm (R, Δ_Q, s², s) cho biết các số liệu tập trung sát quanh số trung bình hay phân tán rộng.",
        "• Khoảng biến thiên R = aₖ₊₁ − a₁ (hiệu giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên).\n"
        "• Khoảng tứ phân vị Δ_Q = Q₃ − Q₁ của mẫu số liệu ghép nhóm (đo độ phân tán của 50% số liệu ở chính giữa).\n"
        "• Phương sai s² và Độ lệch chuẩn s = √(s²) của mẫu số liệu ghép nhóm dựa trên các giá trị đại diện cᵢ.\n"
        "• Ý nghĩa thực tiễn: So sánh độ đồng đều chất lượng sản phẩm hoặc mức độ rủi ro của hai danh mục đầu tư.",
        [
            {
                "category": "I. Khoảng biến thiên & Khoảng tứ phân vị (Mẫu ghép nhóm)",
                "items": [
                    {"name": "Khoảng biến thiên R", "formula": "R = aₖ₊₁ − a₁", "note": "a₁: đầu mút trái nhóm đầu ; aₖ₊₁: đầu mút phải nhóm cuối"},
                    {"name": "Khoảng tứ phân vị Δ_Q", "formula": "Δ_Q = Q₃ − Q₁", "note": "Ít chịu ảnh hưởng bởi các giá trị ngoại lệ"},
                ],
            },
            {
                "category": "II. Phương sai s² & Độ lệch chuẩn s (Mẫu ghép nhóm)",
                "items": [
                    {"name": "Giá trị đại diện & Số trung bình", "formula": "cᵢ = (aᵢ + aᵢ₊₁)/2  ;  x̄ = (n₁c₁ + ... + nₖcₖ) / n", "note": "n = n₁ + ... + nₖ"},
                    {"name": "Phương sai mẫu ghép nhóm s²", "formula": "s² = (1/n) · [ n₁(c₁ − x̄)² + ... + nₖ(cₖ − x̄)² ] = (1/n)·(n₁c₁² + ... + nₖcₖ²) − x̄²", "note": "Công thức rút gọn thứ hai giúp bấm máy tính rất nhanh"},
                    {"name": "Độ lệch chuẩn s", "formula": "s = √(s²)", "note": "Có cùng đơn vị đo với dữ liệu ban đầu"},
                ],
            },
        ],
        "Đánh giá rủi ro biến động giá cổ phiếu, kiểm soát sai số dây chuyền đóng gói tự động và phân tích khí tượng.",
        "So sánh biên độ dao động nhiệt độ giữa hai vùng du lịch hoặc độ ổn định khối lượng các gói cà phê.",
        "Khảo sát cân nặng (gam) của 20 quả táo thu được bảng ghép nhóm: [180; 200): 4 quả; [200; 220): 12 quả; [220; 240): 4 quả. Tính khoảng biến thiên R, số trung bình x̄, phương sai s² và độ lệch chuẩn s.",
        "Khoảng biến thiên: R = 240 − 180 = 60 (g). Giá trị đại diện: c₁ = 190, c₂ = 210, c₃ = 230. Trung bình: x̄ = (4·190 + 12·210 + 4·230)/20 = 210 (g). Phương sai: s² = [4·(190 − 210)² + 12·(210 − 210)² + 4·(230 − 210)²] / 20 = (1600 + 0 + 1600)/20 = 160. Độ lệch chuẩn: s = √160 = 4√10 ≈ 12,65 (g).",
        "Cho mẫu số liệu ghép nhóm có nhóm đầu tiên là [10; 20) và nhóm cuối cùng là [60; 70). Khoảng biến thiên R của mẫu số liệu ghép nhóm trên là:",
        ["10", "50", "60", "70"],
        2,
        "Lợi nhuận hàng tháng (%) của hai quỹ đầu tư X và Y trong 12 tháng qua có cùng mức trung bình x̄ = 8%, nhưng phương sai của quỹ X là s_X² = 2,25 và phương sai của quỹ Y là s_Y² = 9,0. Hãy tính độ lệch chuẩn của mỗi quỹ và cho biết nhà đầu tư ưa thích sự an toàn, ít biến động nên chọn quỹ nào?",
        "Độ lệch chuẩn của quỹ X là s_X = √2,25 = 1,5 (%) và của quỹ Y là s_Y = √9,0 = 3,0 (%). Vì s_X < s_Y nên lợi nhuận của quỹ X ổn định hơn và ít rủi ro biến động hơn, do đó nhà đầu tư ưa an toàn nên chọn quỹ X.",
    ),
    M(
        12,
        "xac-suat",
        "Xác suất có điều kiện, Công thức Xác suất toàn phần & Công thức Bayes",
        "🎲",
        "Làm chủ xác suất có điều kiện P(A|B), sơ đồ hình cây, công thức xác suất toàn phần và công thức Bayes trong chẩn đoán - AI.",
        "Xác suất có điều kiện P(A|B) là xác suất của biến cố A được tính với giả thiết rằng biến cố B đã xảy ra. Công thức Bayes cho phép cập nhật ngược xác suất nguyên nhân khi đã biết kết quả.",
        "• Định nghĩa xác suất có điều kiện P(A|B) = P(AB) / P(B) (với P(B) > 0) và công thức nhân xác suất tổng quát P(AB) = P(B)·P(A|B).\n"
        "• Phương pháp vẽ Sơ đồ hình cây (Tree Diagram) trực quan hóa các nhánh xác suất.\n"
        "• Công thức xác suất toàn phần: tính xác suất của biến cố A thông qua hai biến cố đối nhau B và B̄.\n"
        "• Công thức Bayes: tính xác suất hậu nghiệm P(B|A) khi biết biến cố kết quả A đã xảy ra.",
        [
            {
                "category": "I. Xác suất có điều kiện & Công thức Nhân tổng quát",
                "items": [
                    {"name": "Xác suất của A với điều kiện B", "formula": "P(A | B) = P(AB) / P(B) = n(AB) / n(B)  (với P(B) > 0)", "note": "P(Ā | B) = 1 − P(A | B)"},
                    {"name": "Công thức nhân xác suất tổng quát", "formula": "P(AB) = P(B) · P(A | B) = P(A) · P(B | A)", "note": "Áp dụng cho mọi cặp biến cố (không cần độc lập)"},
                ],
            },
            {
                "category": "II. Công thức Xác suất toàn phần & Công thức Bayes",
                "items": [
                    {"name": "Công thức Xác suất toàn phần", "formula": "P(A) = P(B) · P(A | B) + P(B̄) · P(A | B̄)", "note": "Cộng xác suất của 2 nhánh dẫn tới kết quả A trên sơ đồ cây"},
                    {"name": "Công thức Bayes (Cập nhật xác suất nguyên nhân)", "formula": "P(B | A) = [ P(B) · P(A | B) ] / P(A) = [ P(B)·P(A|B) ] / [ P(B)·P(A|B) + P(B̄)·P(A|B̄) ]", "note": "Tử số là nhánh thuận lợi đi qua B; mẫu số là xác suất toàn phần P(A)"},
                ],
            },
        ],
        "Nền tảng cốt lõi của Y học chẩn đoán (độ nhạy, độ đặc hiệu của xét nghiệm), bộ lọc thư rác (Naive Bayes Spam Filter) và Học máy (Machine Learning).",
        "Tính xác suất thực sự mắc bệnh của một bệnh nhân khi có kết quả xét nghiệm dương tính, hoặc truy xuất nguồn gốc sản phẩm lỗi từ các dây chuyền nhà máy.",
        "Một nhà máy có hai phân xưởng I và II cùng sản xuất một loại linh kiện. Phân xưởng I sản xuất 60% tổng sản phẩm với tỉ lệ phế phẩm là 2%; phân xưởng II sản xuất 40% tổng sản phẩm với tỉ lệ phế phẩm là 3%. Chọn ngẫu nhiên 1 linh kiện của nhà máy: a) Tính xác suất linh kiện đó là phế phẩm; b) Biết linh kiện lấy ra là phế phẩm, tính xác suất nó do phân xưởng I sản xuất.",
        "Gọi B là biến cố 'linh kiện của phân xưởng I' ⇒ P(B) = 0,6 và P(B̄) = 0,4 (phân xưởng II). Gọi A là biến cố 'linh kiện là phế phẩm' ⇒ P(A|B) = 0,02 và P(A|B̄) = 0,03. a) Theo công thức xác suất toàn phần: P(A) = 0,6·0,02 + 0,4·0,03 = 0,012 + 0,012 = 0,024 (2,4%). b) Theo công thức Bayes: P(B|A) = [P(B)·P(A|B)] / P(A) = 0,012 / 0,024 = 0,5 (50%).",
        "Cho hai biến cố A và B có P(B) = 0,4 và P(AB) = 0,12. Xác suất có điều kiện P(A | B) bằng:",
        ["0,048", "0,3", "0,28", "0,52"],
        1,
        "Tỉ lệ người mắc một căn bệnh hiếm trong cộng đồng là 1% (0,01). Một phương pháp xét nghiệm có độ nhạy là 99% (tức là nếu có bệnh thì xác suất xét nghiệm dương tính là 0,99) và tỉ lệ dương tính giả ở người không mắc bệnh là 2% (tức nếu không bệnh thì xác suất dương tính là 0,02). Một người đi xét nghiệm ngẫu nhiên và nhận kết quả DƯƠNG TÍNH. Hãy dùng công thức Bayes để tính xác suất người đó thực sự mắc bệnh.",
        "Gọi B là biến cố 'Mắc bệnh' ⇒ P(B) = 0,01 ; P(B̄) = 0,99. Gọi A là biến cố 'Xét nghiệm dương tính' ⇒ P(A|B) = 0,99 ; P(A|B̄) = 0,02. Xác suất dương tính toàn phần: P(A) = 0,01·0,99 + 0,99·0,02 = 0,0099 + 0,0198 = 0,0297. Theo công thức Bayes, xác suất người đó thực sự mắc bệnh là: P(B|A) = 0,0099 / 0,0297 = 1/3 ≈ 33,33%.",
    ),
    M(
        12,
        "so-phuc",
        "Số phức, Biểu diễn hình học & Phương trình bậc hai trên tập số phức ℂ",
        "🌀",
        "Thực hiện cộng, trừ, nhân, chia số phức, tìm môđun, số phức liên hợp và giải phương trình bậc hai với hệ số thực trên ℂ.",
        "Số phức có dạng đại số z = a + bi (với a, b ∈ ℝ và đơn vị ảo i thỏa mãn i² = −1), mở rộng tập số thực ℝ thành trường số phức ℂ để mọi phương trình đa thức bậc n ≥ 1 đều có đủ n nghiệm.",
        "• Phần thực a = Re(z), phần ảo b = Im(z), hai số phức bằng nhau.\n"
        "• Biểu diễn hình học của số phức z = a + bi bởi điểm M(a; b) trên mặt phẳng phức Oxy; môđun |z| = OM = √(a² + b²) và số phức liên hợp z̄ = a − bi.\n"
        "• Phép cộng, trừ, nhân, chia hai số phức (nhân cả tử và mẫu với số phức liên hợp của mẫu).\n"
        "• Căn bậc hai của số thực âm và giải phương trình bậc hai ax² + bx + c = 0 (Δ < 0) trên tập số phức ℂ.",
        [
            {
                "category": "I. Cấu trúc Số phức z = a + bi (a, b ∈ ℝ ; i² = −1)",
                "items": [
                    {"name": "Môđun & Số phức liên hợp", "formula": "|z| = √(a² + b²)  ;  z̄ = a − bi  ;  z · z̄ = |z|² = a² + b²", "note": "|z| = |z̄| ; |z₁·z₂| = |z₁|·|z₂| ; |z₁/z₂| = |z₁|/|z₂|"},
                    {"name": "Lũy thừa của đơn vị ảo i (k ∈ ℤ)", "formula": "i⁴ᵏ = 1 ; i⁴ᵏ⁺¹ = i ; i⁴ᵏ⁺² = −1 ; i⁴ᵏ⁺³ = −i", "note": "Chu kỳ lặp lại sau mỗi 4 số mũ"},
                ],
            },
            {
                "category": "II. Bốn phép toán trên Tập số phức ℂ",
                "items": [
                    {"name": "Cộng & Trừ hai số phức", "formula": "(a + bi) ± (c + di) = (a ± c) + (b ± d)i", "note": "Cộng/trừ phần thực với phần thực, phần ảo với phần ảo"},
                    {"name": "Nhân hai số phức", "formula": "(a + bi)(c + di) = (ac − bd) + (ad + bc)i", "note": "Do bd·i² = −bd"},
                    {"name": "Chia hai số phức (c + di ≠ 0)", "formula": "(a + bi) / (c + di) = [(a + bi)(c − di)] / (c² + d²) = (ac + bd)/(c² + d²) + [(bc − ad)/(c² + d²)]i", "note": ""},
                ],
            },
            {
                "category": "III. Phương trình bậc hai ax² + bx + c = 0 (a, b, c ∈ ℝ, a ≠ 0) khi Δ < 0",
                "items": [
                    {"name": "Hai nghiệm phức liên hợp khi Δ < 0", "formula": "z₁ = (−b + i√|Δ|) / (2a)  ;  z₂ = (−b − i√|Δ|) / (2a)", "note": "Định lý Viète vẫn đúng: z₁ + z₂ = −b/a và z₁·z₂ = c/a"},
                ],
            },
        ],
        "Ứng dụng cốt lõi trong biểu diễn dòng điện xoay chiều (tổng trở phức Z = R + (Z_L − Z_C)i), xử lý tín hiệu số (biến đổi Fourier) và cơ học lượng tử.",
        "Tính tổng trở mạch điện xoay chiều RLC bằng số phức và biến đổi phép quay trong đồ họa 2D.",
        "Cho hai số phức z₁ = 3 − 4i và z₂ = 1 + 2i. Tính số phức w = z₁ / z₂ và tìm môđun của w.",
        "Nhân cả tử và mẫu với liên hợp của z₂ là (1 − 2i): w = (3 − 4i)(1 − 2i) / (1² + 2²) = (3 − 6i − 4i + 8i²) / 5 = (−5 − 10i) / 5 = −1 − 2i. Môđun của w là: |w| = √((−1)² + (−2)²) = √5.",
        "Gọi z₁, z₂ là hai nghiệm phức của phương trình z² − 4z + 13 = 0. Giá trị của biểu thức T = |z₁|² + |z₂|² bằng:",
        ["13", "16", "26", "32"],
        2,
        "Trên mặt phẳng tọa độ Oxy, tìm tập hợp các điểm M(x; y) biểu diễn số phức z = x + yi thỏa mãn điều kiện |z − 2 + i| = 3.",
        "Thay z = x + yi vào điều kiện: |(x − 2) + (y + 1)i| = 3 ⇔ √[(x − 2)² + (y + 1)²] = 3 ⇔ (x − 2)² + (y + 1)² = 9. Vậy tập hợp các điểm biểu diễn số phức z là đường tròn có tâm I(2; −1) và bán kính R = 3.",
    ),
    M(
        12,
        "on-tap-thpt",
        "Tổng ôn Toán THPT & Mô hình hóa tối ưu thực tiễn",
        "🏆",
        "Hệ thống hóa toàn bộ kiến thức Giải tích, Hình học không gian - Oxyz và Thống kê - Xác suất cho kỳ thi Tốt nghiệp THPT.",
        "Bài tổng ôn kết nối xuyên suốt các trụ cột Toán học THPT (Hàm số - Đạo hàm, Mũ - Lôgarit, Nguyên hàm - Tích phân, Hình học không gian - Oxyz, Thống kê - Xác suất Bayes) vào các bài toán tổng hợp và thực tiễn.",
        "• Sơ đồ tổng hợp Khảo sát hàm số & Bài toán tối ưu kinh tế - kỹ thuật.\n"
        "• Liên hệ khép kín giữa Quãng đường s(t) ⇄ Vận tốc v(t) ⇄ Gia tốc a(t) qua Đạo hàm và Tích phân.\n"
        "• Kết hợp Hình học không gian cổ điển và phương pháp gắn trục tọa độ Oxyz.\n"
        "• Chiến lược phân tích đề thi Tốt nghiệp THPT (Trắc nghiệm 4 lựa chọn, Trắc nghiệm Đúng/Sai và Trả lời ngắn).",
        [
            {
                "category": "I. Chuỗi liên hệ Giải tích (Đạo hàm ⇄ Nguyên hàm - Tích phân)",
                "items": [
                    {"name": "Bài toán Chuyển động", "formula": "v(t) = s'(t) ; a(t) = v'(t)  ⇄  v(t) = ∫a(t)dt ; s = ∫[t₁→t₂] |v(t)|dt", "note": ""},
                    {"name": "Bài toán Kinh tế (Doanh thu R, Chi phí C, Lợi nhuận P)", "formula": "P(x) = R(x) − C(x)  ⇒  Lợi nhuận cực đại khi P'(x) = 0 ⇔ R'(x) = C'(x) (Doanh thu biên = Chi phí biên)", "note": ""},
                ],
            },
            {
                "category": "II. Tóm tắt Tọa độ hóa Hình học không gian Oxyz",
                "items": [
                    {"name": "Thể tích tứ diện ABCD & Hình hộp", "formula": "V_ABCD = (1/6) · |[AB⃗, AC⃗] · AD⃗|  ;  V_hộp = |[AB⃗, AD⃗] · AA'⃗|", "note": "Tích hỗn tạp của 3 vectơ"},
                    {"name": "Khoảng cách giữa 2 đường thẳng chéo nhau d₁, d₂", "formula": "d(d₁, d₂) = |[u₁⃗, u₂⃗] · M₁M₂⃗| / |[u₁⃗, u₂⃗]|", "note": "M₁ ∈ d₁, M₂ ∈ d₂"},
                ],
            },
        ],
        "Giúp học sinh nhìn thấy bức tranh toàn cảnh của Toán học phổ thông và tự tin chinh phục điểm 9–10 trong kỳ thi Tốt nghiệp THPT.",
        "Tối ưu đường dây cáp điện ngầm nối từ đất liền ra đảo, tính toán thiết kế kiến trúc Oxyz và phân tích dữ liệu.",
        "Một nhà máy sản xuất x (tấn) sản phẩm mỗi tháng (0 < x ≤ 20) có tổng chi phí là C(x) = x³ − 6x² + 15x + 10 (triệu đồng) và giá bán mỗi tấn sản phẩm là 27 triệu đồng. Hỏi nhà máy cần sản xuất bao nhiêu tấn sản phẩm mỗi tháng để đạt lợi nhuận lớn nhất?",
        "Doanh thu khi bán x tấn là R(x) = 27x (triệu đồng). Hàm lợi nhuận là: P(x) = R(x) − C(x) = −x³ + 6x² + 12x − 10. Đạo hàm: P'(x) = −3x² + 12x + 12 = 0 ⇔ x² − 4x − 4 = 0 ⇒ x = 2 + 2√2 ≈ 4,83 (tấn) (vì x > 0). Vậy nhà máy đạt lợi nhuận tối đa khi sản xuất x = 2 + 2√2 tấn/tháng.",
        "Một vật chuyển động với vận tốc v(t) = 3t² + 4t (m/s). Quãng đường vật đi được trong khoảng thời gian từ t = 1 giây đến t = 3 giây là:",
        ["32 m", "42 m", "34 m", "26 m"],
        1,
        "Một hòn đảo ở vị trí A cách bờ biển thẳng một khoảng AH = 3 km (H là hình chiếu vuông góc của A lên bờ biển). Nhà máy điện ở vị trí B trên bờ biển cách H một đoạn BH = 6 km. Chi phí lắp đặt mỗi km dây cáp dưới nước là 500 triệu đồng và mỗi km dây cáp trên bờ là 300 triệu đồng. Hỏi cần chọn điểm nối cáp M trên đoạn bờ biển HB cách H bao nhiêu km (đi cáp ngầm dưới nước từ A đến M rồi đi trên bờ từ M đến B) để tổng chi phí lắp đặt là thấp nhất?",
        "Gọi HM = x (km, 0 ≤ x ≤ 6) ⇒ MB = 6 − x và AM = √(x² + 9). Tổng chi phí (triệu đồng): f(x) = 500√(x² + 9) + 300(6 − x). Đạo hàm: f'(x) = 500x/√(x² + 9) − 300 = 0 ⇔ 5x = 3√(x² + 9) ⇔ 25x² = 9(x² + 9) ⇔ 16x² = 81 ⇒ x = 9/4 = 2,25 (km). Khi đó tổng chi phí nhỏ nhất là f(2,25) = 3 000 triệu đồng (3 tỷ đồng).",
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
        print(f"ĐÃ XỬ LÝ: {len(LESSONS)} BÀI TOÁN LỚP 10–12")
        print(f"TẠO MỚI:  {created}")
        print(f"CẬP NHẬT: {updated}")
        print("=" * 60)

    except Exception as e:
        db.rollback()
        print("\n" + "=" * 60)
        print("LỖI KHI CẬP NHẬT TOÁN 10–12:")
        print(e)
        print("=" * 60)
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()