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
Nâng cấp toàn diện nội dung Vật lý Lớp 6–12 (Chương trình GDPT 2018).
Tổng cộng: 50 bài học (Lớp 6–11: 7 bài/lớp; Lớp 12: 8 bài), bao gồm:
- 43 bài học cốt lõi ban đầu (loại bỏ tệp trùng lặp upgrade_physics (1).py).
- 7 chuyên đề bổ sung mới lấp đầy chương trình Vật lý / KHTN GDPT 2018:
  + Lớp 6: trong-luong-va-nang-luong (Trọng lực, Trọng lượng & Bảo toàn năng lượng)
  + Lớp 7: nam-cham-dien-tu-truong-trai-dat (Từ trường Trái Đất, La bàn & Nam châm điện)
  + Lớp 8: moment-luc-don-bay (Tác dụng làm quay của lực, Moment lực & Đòn bẩy)
  + Lớp 9: co-nang-khuc-xa-anh-sang (Động năng, Thế năng, Cơ năng & Khúc xạ - Phản xạ toàn phần)
  + Lớp 10: chuyen-dong-tron-bien-dang-lo-xo (Chuyển động tròn đều, Lực hướng tâm & Định luật Hooke)
  + Lớp 11: song-dien-tu-giao-thoa-tu-dien (Giao thoa sóng, Sóng dừng, Sóng điện từ & Tụ điện)
  + Lớp 12: vat-ly-nhiet-khi-ly-tuong (Vật lý nhiệt, Định luật I NĐLH & Phương trình trạng thái Khí lý tưởng)

Chạy từ thư mục backend:
    python upgrade_physics.py
"""

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject

SUBJECT_SLUG = "physics"
SUBJECT_NAME = "Vật lý"


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


def P(
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
        "context_title": f"Hiện tượng & Ứng dụng: {title}",
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
        "game_title": game_title or f"Thử thách thực tế: {title}",
        "game_description": game_description
        or f"Mô phỏng tương tác và thực hành đo đạc {title.lower()}.",
        "game_type": game_type,
    }


LESSONS = [
    # =========================================================
    # VẬT LÝ LỚP 6 (7 BÀI)
    # =========================================================
    P(
        6,
        "do-dai",
        "Đo chiều dài & Giới hạn đo - Độ chia nhỏ nhất",
        "📏",
        "Xác định kích thước của vật bằng thước đo có GHĐ và ĐCNN phù hợp, thực hiện quy đổi đơn vị độ dài SI.",
        "Đo chiều dài là so sánh chiều dài của vật với một đơn vị độ dài chuẩn thông qua dụng cụ đo thích hợp. Đơn vị đo chiều dài chính thức trong hệ SI là mét (m).",
        "• Giới hạn đo (GHĐ) của thước là chiều dài lớn nhất ghi trên thước; Độ chia nhỏ nhất (ĐCNN) là chiều dài giữa hai vạch chia liên tiếp trên thước.\n"
        "• Quy tắc 5 bước đo chiều dài: Ước lượng chiều dài → Chọn thước có GHĐ và ĐCNN phù hợp → Đặt thước dọc theo vật, vạch số 0 ngang với một đầu vật → Đặt mắt nhìn theo hướng vuông góc với cạnh thước ở đầu kia → Đọc và ghi kết quả theo vạch chia gần nhất.\n"
        "• Các đơn vị lớn và cực nhỏ: km, m, dm, cm, mm, micromét (μm), nanomét (nm).",
        [
            {
                "category": "I. Hệ thống đơn vị đo độ dài (Chuẩn SI: mét - m)",
                "items": [
                    {"name": "Đơn vị thông dụng", "formula": "1 km = 1000 m ; 1 m = 10 dm = 100 cm = 1000 mm", "note": ""},
                    {"name": "Đơn vị vi mô", "formula": "1 mm = 1000 μm (micromét) ; 1 μm = 1000 nm (nanomét)", "note": "Đo kích thước tế bào, vi khuẩn"},
                ],
            },
            {
                "category": "II. Độ chia nhỏ nhất (ĐCNN) & Ghi kết quả đo",
                "items": [
                    {"name": "Tính ĐCNN của thước", "formula": "ĐCNN = (Hiệu hai số ghi liên tiếp) / (Số khoảng chia giữa chúng)", "note": "Kết quả đo phải ghi theo bội số của ĐCNN"},
                    {"name": "Giá trị trung bình qua n lần đo", "formula": "L_tb = (L₁ + L₂ + ... + Lₙ) / n", "note": "Giảm sai số ngẫu nhiên"},
                ],
            },
        ],
        "Đo đạc và đổi đơn vị chuẩn xác giúp đọc bản vẽ kỹ thuật, gia công cơ khí và tránh sai số khi lắp ghép nội thất.",
        "Đo chiều dài bàn học bằng thước cuộn rồi nhập kết quả vào mô phỏng để kiểm tra sai số.",
        "Trên một chiếc thước kẻ, giữa vạch số 2 (cm) và vạch số 3 (cm) được chia làm 10 khoảng bằng nhau. Hãy tính ĐCNN của thước đó.",
        "Hiệu hai số ghi liên tiếp là 3 − 2 = 1 (cm). Số khoảng chia là 10. Vậy ĐCNN = 1 / 10 = 0,1 cm = 1 mm.",
        "Khi dùng một thước có ĐCNN là 0,2 cm để đo chiều dài quyển sách, cách ghi kết quả nào dưới đây là ĐÚNG?",
        ["24,1 cm", "24,2 cm", "24,25 cm", "24,5 cm"],
        1,
        "Muốn đo đường kính ngoài của một chiếc cốc hình trụ bằng thước thẳng và hai miếng gỗ phẳng hình hộp chữ nhật, em hãy trình bày cách làm chính xác nhất.",
        "Kẹp chặt chiếc cốc thẳng đứng vào giữa hai mặt phẳng song song của hai miếng gỗ trên mặt bàn, sau đó dùng thước thẳng đo khoảng cách vuông góc giữa hai mặt trong của hai miếng gỗ.",
        game_title="Thử thách thực tế: Đo độ dài",
        game_description="Đo thật → nhập số đo → so sánh sai số với giá trị chuẩn.",
    ),
    P(
        6,
        "khoi-luong",
        "Đo khối lượng & Sử dụng các loại cân",
        "⚖️",
        "Hiểu bản chất khối lượng là lượng chất chứa trong vật và thực hành đo khối lượng bằng cân.",
        "Mọi vật đều có khối lượng. Khối lượng của một vật chỉ lượng chất tạo nên vật đó và không thay đổi khi vị trí của vật thay đổi. Đơn vị đo khối lượng trong hệ SI là ki-lô-gam (kg).",
        "• Các đơn vị khối lượng: tấn (t), tạ, yến, ki-lô-gam (kg), héc-tô-gam (hg / lạng), gam (g), mi-li-gam (mg).\n"
        "• Các loại cân phổ biến: cân đồng hồ, cân điện tử, cân Роберval (cân đòn), cân y tế.\n"
        "• Lưu ý khi dùng cân đồng hồ: Trước khi cân phải điều chỉnh ốc vặn để kim cân chỉ đúng vạch số 0 (hiệu chỉnh điểm 0).",
        [
            {
                "category": "I. Bảng quy đổi đơn vị Khối lượng (Chuẩn SI: kg)",
                "items": [
                    {"name": "Đơn vị lớn hơn kg", "formula": "1 tấn = 10 tạ = 100 yến = 1000 kg ; 1 tạ = 100 kg ; 1 yến = 10 kg", "note": ""},
                    {"name": "Đơn vị nhỏ hơn kg", "formula": "1 kg = 10 hg (10 lạng) = 1000 g ; 1 g = 1000 mg (mi-li-gam)", "note": "1 lạng = 100 g"},
                ],
            },
            {
                "category": "II. Khối lượng tịnh (Net Weight) trên bao bì",
                "items": [
                    {"name": "Khối lượng hàng thực tế", "formula": "m_hàng (tịnh) = m_tổng_cả_bì − m_vỏ_bao_bì", "note": "Ký hiệu Net Wt trên vỏ hộp"},
                ],
            },
        ],
        "Đo khối lượng giúp định lượng chính xác trong thương mại, pha chế dược phẩm, nấu ăn và kiểm soát tải trọng cầu đường.",
        "Cân các vật trong cửa hàng ảo và chọn phương án đóng gói, vận chuyển phù hợp giới hạn tải trọng.",
        "Trên vỏ một hộp sữa bột có ghi 'Khối lượng tịnh: 850 g'. Nếu đặt cả hộp sữa chưa mở lên cân điện tử thì cân chỉ 980 g. Hãy giải thích và tính khối lượng của vỏ hộp kim loại.",
        "850 g là khối lượng của riêng lượng sữa bột bên trong; 980 g là tổng khối lượng của cả sữa và vỏ hộp. Vậy khối lượng vỏ hộp là: 980 − 850 = 130 (g).",
        "Một người mua 3 lạng thịt bò và 0,5 kg cá. Tổng khối lượng thực phẩm người đó đã mua tính theo gam là:",
        ["350 g", "530 g", "800 g", "3 500 g"],
        2,
        "Làm thế nào để xác định khối lượng của đúng 1 hạt gạo bằng một chiếc cân điện tử nhà bếp có độ chia nhỏ nhất là 1 g?",
        "Đếm lấy 200 hạt gạo (hoặc 500 hạt gạo) cho lên cân để đo tổng khối lượng M (gam), sau đó lấy M chia cho 200 (hoặc 500) sẽ tìm được khối lượng trung bình rất chính xác của 1 hạt gạo.",
        game_title="Thử thách thực tế: Khối lượng và cân",
        game_description="Đặt vật lên cân → đọc khối lượng → quyết định phương án vận chuyển.",
    ),
    P(
        6,
        "luc",
        "Lực, Biểu diễn lực & Hai lực cân bằng - Biến dạng lò xo",
        "🏹",
        "Hiểu tác dụng đẩy/kéo của lực làm biến đổi chuyển động hoặc biến dạng vật, cách vẽ mũi tên lực và độ giãn lò xo.",
        "Tác dụng đẩy hoặc kéo của vật này lên vật khác được gọi là lực (ký hiệu F, đơn vị là Newton - N). Lực là một đại lượng vectơ có điểm đặt, phương, chiều và độ lớn.",
        "• Hai kết quả tác dụng của lực: làm thay đổi tốc độ / hướng chuyển động của vật, hoặc làm vật bị biến dạng (hoặc đồng thời cả hai).\n"
        "• Biểu diễn lực bằng một mũi tên: gốc là điểm đặt lực, phương và chiều là phương và chiều của lực, độ dài biểu thị độ lớn lực theo một tỉ xích cho trước.\n"
        "• Lực tiếp xúc (đẩy xe, đá bóng) và Lực không tiếp xúc (lực hấp dẫn, lực từ nam châm).\n"
        "• Độ giãn của lò xo treo thẳng đứng tỉ lệ thuận với khối lượng (trọng lượng) vật treo; nguyên lý cấu tạo của Lực kế.",
        [
            {
                "category": "I. Các yếu tố của Lực & Hai lực cân bằng",
                "items": [
                    {"name": "4 yếu tố đặc trưng của lực F⃗", "formula": "Điểm đặt ; Phương ; Chiều ; Độ lớn F (đơn vị: Newton - N)", "note": ""},
                    {"name": "Hai lực cân bằng", "formula": "Cùng tác dụng vào 1 vật, cùng phương, ngược chiều và cùng độ lớn (F₁ = F₂)", "note": "Vật đứng yên sẽ tiếp tục đứng yên"},
                ],
            },
            {
                "category": "II. Biến dạng của Lò xo & Lực kế",
                "items": [
                    {"name": "Độ giãn của lò xo Δl", "formula": "Δl = l − l₀", "note": "l₀: chiều dài tự nhiên; l: chiều dài khi treo vật"},
                    {"name": "Tỉ lệ độ giãn theo khối lượng treo", "formula": "Δl₁ / Δl₂ = m₁ / m₂ = P₁ / P₂", "note": "Trong giới hạn đàn hồi của lò xo"},
                ],
            },
        ],
        "Hiểu bản chất lực giúp giải thích mọi tương tác cơ học: đá bóng, giương cung, giảm xóc xe máy và sử dụng lực kế.",
        "Điều khiển hướng và độ lớn lực đẩy một chiếc xe để đưa xe đến đúng vị trí đích.",
        "Một lò xo có chiều dài tự nhiên l₀ = 12 cm. Khi treo quả nặng 100 g thì lò xo dài 14 cm. Hỏi nếu treo quả nặng 250 g thì chiều dài của lò xo là bao nhiêu?",
        "Treo 100 g thì lò xo giãn: Δl₁ = 14 − 12 = 2 (cm). Khi treo 250 g (gấp 2,5 lần 100 g), độ giãn là: Δl₂ = 2 · 2,5 = 5 (cm). Chiều dài lò xo khi đó là: l = 12 + 5 = 17 (cm).",
        "Trường hợp nào dưới đây lực xuất hiện là LỰC KHÔNG TIẾP XÚC?",
        [
            "Thủ môn bắt dính quả bóng đang bay",
            "Gió thổi làm căng buồm",
            "Nam châm hút chiếc đinh sắt đặt cách đó 2 cm",
            "Vận động viên nâng tạ lên cao",
        ],
        2,
        "Treo một vật vào lực kế, kim lực kế chỉ 4,5 N. Nếu dùng tay kéo vật xuống dưới thêm một lực 2 N theo phương thẳng đứng thì số chỉ của lực kế khi ổn định là bao nhiêu?",
        "Lực kế chịu đồng thời trọng lượng vật (4,5 N) và lực kéo của tay cùng hướng thẳng đứng xuống dưới (2 N), nên số chỉ của lực kế là: 4,5 + 2 = 6,5 (N).",
        game_title="Thử thách thực tế: Lực và tác dụng của lực",
        game_description="Chọn hướng và độ lớn lực → quan sát chuyển động → điều chỉnh lực.",
    ),
    P(
        6,
        "trong-luong-va-nang-luong",
        "Trọng lực - Trọng lượng & Sự chuyển hóa, Bảo toàn Năng lượng",
        "🌍",
        "Phân biệt khối lượng (m) với trọng lượng (P = 10m) và nắm vững định luật bảo toàn - chuyển hóa năng lượng.",
        "Trọng lực là lực hút của Trái Đất tác dụng lên vật (có phương thẳng đứng, chiều hướng về phía tâm Trái Đất). Độ lớn của trọng lực tác dụng lên vật gọi là trọng lượng P. Năng lượng đặc trưng cho khả năng sinh công và không tự nhiên sinh ra hay mất đi.",
        "• Lực hấp dẫn: Mọi vật có khối lượng đều hút nhau; trọng lực là trường hợp riêng của lực hấp dẫn do Trái Đất gây ra.\n"
        "• Liên hệ giữa trọng lượng P (đơn vị N) và khối lượng m (đơn vị kg) tại mặt đất: P ≈ 10 · m.\n"
        "• Các dạng năng lượng (động năng, thế năng hấp dẫn, thế năng đàn hồi, quang năng, nhiệt năng, điện năng, hóa năng) và Định luật bảo toàn năng lượng.\n"
        "• Năng lượng tái tạo (Mặt Trời, gió, thủy triều) và năng lượng không tái tạo (than đá, dầu mỏ, khí đốt).",
        [
            {
                "category": "I. Trọng lực & Liên hệ Trọng lượng - Khối lượng",
                "items": [
                    {"name": "Công thức tính Trọng lượng ở mặt đất", "formula": "P = 10 · m  (chính xác hơn: P = g · m với g ≈ 9,8 m/s²)", "note": "m tính bằng kg ; P tính bằng Newton (N)"},
                    {"name": "Trọng lượng 1 quả nặng 100 g", "formula": "m = 100 g = 0,1 kg  ⇒  P = 10 · 0,1 = 1 N", "note": ""},
                ],
            },
            {
                "category": "II. Định luật Bảo toàn Năng lượng & Hiệu suất cơ bản",
                "items": [
                    {"name": "Bảo toàn năng lượng", "formula": "W_toàn_phần = W_có_ích + W_hao_phí = hằng số", "note": "Năng lượng chỉ truyền từ vật này sang vật khác hoặc chuyển hóa giữa các dạng"},
                    {"name": "Hiệu suất sử dụng năng lượng", "formula": "H = (W_có_ích / W_toàn_phần) × 100%", "note": "Hao phí thường thoát ra dưới dạng nhiệt năng"},
                ],
            },
        ],
        "Giúp phân biệt rõ khối lượng (không đổi) với trọng lượng (thay đổi theo thiên thể như Mặt Trăng) và sử dụng năng lượng tiết kiệm, hiệu quả.",
        "So sánh trọng lượng của nhà du hành vũ trụ trên Trái Đất và trên Mặt Trăng, tính năng lượng hao phí của bóng đèn.",
        "Một kiện hàng có khối lượng 45 kg. Tính trọng lượng của kiện hàng đó trên Trái Đất và trên Mặt Trăng (biết trọng lực trên Mặt Trăng bằng 1/6 trên Trái Đất).",
        "Trên Trái Đất: P_TĐ = 10 · 45 = 450 (N). Trên Mặt Trăng: khối lượng vẫn là 45 kg nhưng trọng lượng là P_MT = 450 : 6 = 75 (N).",
        "Khi một bóng đèn LED đang phát sáng, điện năng đã chuyển hóa chủ yếu thành những dạng năng lượng nào?",
        [
            "Quang năng (năng lượng ánh sáng) và Nhiệt năng",
            "Cơ năng và Hóa năng",
            "Thế năng hấp dẫn và Động năng",
            "Năng lượng âm thanh và Từ trường",
        ],
        0,
        "Một bóng đèn sợi đốt tiêu thụ 100 J điện năng trong mỗi giây, nhưng chỉ tạo ra 8 J năng lượng ánh sáng có ích, phần còn lại tỏa nhiệt làm nóng bóng đèn. Tính phần năng lượng nhiệt hao phí mỗi giây và hiệu suất phát sáng của bóng đèn.",
        "Nhiệt năng hao phí mỗi giây là: 100 − 8 = 92 (J). Hiệu suất phát sáng là: H = (8 / 100) × 100% = 8%.",
        game_title="Thử thách thực tế: Trọng lực & Năng lượng",
        game_description="Khảo sát trọng lượng vật trên các hành tinh và tối ưu hiệu suất chuyển hóa năng lượng.",
    ),
    P(
        6,
        "toc-do",
        "Khái niệm Tốc độ & Đơn vị đo tốc độ cơ bản",
        "🏎️",
        "Làm quen với khái niệm tốc độ như thước đo độ nhanh chậm của chuyển động và cách quy đổi m/s ⇄ km/h.",
        "Tốc độ cho biết sự nhanh hay chậm của chuyển động, được xác định bằng quãng đường đi được trong một đơn vị thời gian.",
        "• Hai cách so sánh xem vật nào chuyển động nhanh hơn: cùng quãng đường (ai mất ít thời gian hơn thì nhanh hơn) hoặc cùng thời gian (ai đi được quãng đường dài hơn thì nhanh hơn).\n"
        "• Công thức tính tốc độ v = s / t và hai đơn vị phổ biến nhất là m/s và km/h.\n"
        "• Ý nghĩa của tốc kế trên xe máy, ô tô và biển báo giới hạn tốc độ an toàn.",
        [
            {
                "category": "I. Công thức Tốc độ - Quãng đường - Thời gian",
                "items": [
                    {"name": "Công thức tính tốc độ", "formula": "v = s / t  ⇒  s = v · t  ;  t = s / v", "note": "s: quãng đường ; t: thời gian ; v: tốc độ"},
                ],
            },
            {
                "category": "II. Quy đổi nhanh đơn vị tốc độ",
                "items": [
                    {"name": "Đổi từ m/s sang km/h", "formula": "1 m/s = 3,6 km/h  (nhân với 3,6)", "note": "Ví dụ: 10 m/s = 36 km/h"},
                    {"name": "Đổi từ km/h sang m/s", "formula": "1 km/h = (1 / 3,6) m/s  (chia cho 3,6)", "note": "Ví dụ: 54 km/h = 54 : 3,6 = 15 m/s"},
                ],
            },
        ],
        "Giúp tính thời gian di chuyển, lập lịch trình đi học đúng giờ và tuân thủ tốc độ an toàn giao thông.",
        "Điều khiển xe trong đường đua và chọn thời điểm tăng tốc để về đích nhanh nhất mà không vượt tốc độ giới hạn.",
        "Một vận động viên chạy cự ly 100 m hết 10 giây, trong khi một người đi xe đạp đi được 1,8 km trong 3 phút. Ai chuyển động nhanh hơn?",
        "Tốc độ vận động viên: v₁ = 100 / 10 = 10 (m/s) = 36 (km/h). Đổi 1,8 km = 1800 m và 3 phút = 180 s ⇒ tốc độ người đi xe đạp: v₂ = 1800 / 180 = 10 (m/s). Vậy hai người chuyển động nhanh như nhau.",
        "Tốc độ 72 km/h tương ứng với bao nhiêu mét trên giây (m/s)?",
        ["15 m/s", "20 m/s", "25 m/s", "259,2 m/s"],
        1,
        "Nhà bạn Minh cách trường 4,5 km. Minh đạp xe từ nhà lúc 6 giờ 30 phút với tốc độ không đổi 15 km/h. Hỏi Minh đến trường lúc mấy giờ?",
        "Thời gian Minh đạp xe đến trường là: t = s / v = 4,5 / 15 = 0,3 (giờ) = 18 (phút). Minh đến trường lúc: 6 giờ 30 phút + 18 phút = 6 giờ 48 phút.",
        game_title="Thử thách thực tế: Tốc độ",
        game_description="Tăng/giảm tốc → tránh vật cản → hoàn thành quãng đường.",
    ),
    P(
        6,
        "nhiet-do",
        "Nhiệt độ, Sự nở vì nhiệt & Các thang đo nhiệt độ (°C, °F, K)",
        "🌡️",
        "Hiểu nguyên lý giãn nở vì nhiệt của chất lỏng trong nhiệt kế và công thức chuyển đổi giữa thang Celsius (°C), Fahrenheit (°F) và Kelvin (K).",
        "Nhiệt độ là số đo mức độ nóng, lạnh của một vật. Nhiệt kế hoạt động dựa trên hiện tượng giãn nở vì nhiệt của các chất (thủy ngân, rượu màu, kim loại lưỡng kim).",
        "• Cảm giác của tay về mức độ nóng/lạnh không chính xác, cần dùng nhiệt kế (nhiệt kế y tế có giới hạn đo từ 35°C đến 42°C và có chỗ thắt ngăn thủy ngân tụt xuống).\n"
        "• Ba thang nhiệt độ phổ biến: Thang Celsius (°C: nước đá đang tan là 0°C, nước sôi là 100°C), Thang Fahrenheit (°F: 32°F và 212°F) và Thang nhiệt độ tuyệt đối Kelvin (K: 273,15 K và 373,15 K).",
        [
            {
                "category": "I. Công thức chuyển đổi giữa 3 thang Nhiệt độ",
                "items": [
                    {"name": "Từ độ Celsius (°C) sang Fahrenheit (°F)", "formula": "t(°F) = 1,8 · t(°C) + 32 = (9/5) · t(°C) + 32", "note": "0°C = 32°F ; 100°C = 212°F"},
                    {"name": "Từ độ Fahrenheit (°F) sang Celsius (°C)", "formula": "t(°C) = [ t(°F) − 32 ] / 1,8 = (5/9) · [ t(°F) − 32 ]", "note": ""},
                    {"name": "Từ độ Celsius (°C) sang Kelvin (K - chuẩn SI)", "formula": "T(K) = t(°C) + 273,15  (thường lấy T = t + 273)", "note": "Độ biến thiên: ΔT(K) = Δt(°C)"},
                ],
            },
            {
                "category": "II. Giới hạn đo của Nhiệt kế y tế",
                "items": [
                    {"name": "Thang đo Nhiệt kế y tế", "formula": "Từ 35°C đến 42°C (ĐCNN = 0,1°C)", "note": "Nhiệt độ cơ thể người khỏe mạnh khoảng 37°C (98,6°F)"},
                ],
            },
        ],
        "Theo dõi thân nhiệt y tế, bảo quản kho lạnh thực phẩm và đọc hiểu dự báo thời tiết quốc tế.",
        "Quản lý nhiệt độ của một kho thực phẩm để tránh làm hỏng hàng.",
        "Nhiệt độ cơ thể bình thường của người là 37°C. Hãy đổi nhiệt độ này sang thang độ Fahrenheit (°F) và thang Kelvin (K).",
        "Sang độ F: t(°F) = 1,8 · 37 + 32 = 66,6 + 32 = 98,6 (°F). Sang độ K: T(K) = 37 + 273 = 310 (K).",
        "Tại sao không được dùng nước đang sôi (100°C) để khử trùng nhiệt kế y tế thủy ngân?",
        [
            "Vì nước sôi làm mờ vạch chia trên vỏ thủy tinh",
            "Vì GHĐ của nhiệt kế y tế chỉ đến 42°C, nhúng vào nước 100°C thủy ngân nở mạnh sẽ làm vỡ bầu nhiệt kế",
            "Vì thủy ngân sẽ bị đông đặc ở 100°C",
            "Vì ống quản của nhiệt kế y tế quá rộng",
        ],
        1,
        "Ở nhiệt độ nào thì số chỉ trên thang nhiệt kế Celsius (°C) và số chỉ trên thang nhiệt kế Fahrenheit (°F) có giá trị bằng nhau?",
        "Gọi nhiệt độ đó là x. Ta có phương trình: x = 1,8x + 32 ⇔ −0,8x = 32 ⇔ x = −40. Vậy ở −40°C = −40°F thì hai nhiệt kế chỉ cùng một con số.",
        game_title="Thử thách thực tế: Nhiệt độ",
        game_description="Theo dõi nhiệt kế → bật/tắt thiết bị làm lạnh → giữ nhiệt độ an toàn.",
    ),
    P(
        6,
        "luc-ma-sat",
        "Lực ma sát (Ma sát trượt, Ma sát nghỉ, Ma sát lăn) & Lực cản của môi trường",
        "🛞",
        "Phân biệt 3 loại lực ma sát, hiểu tác dụng có lợi - có hại của ma sát và lực cản của nước, không khí.",
        "Lực ma sát là lực tiếp xúc xuất hiện ở bề mặt tiếp xúc giữa hai vật, cản trở chuyển động tương đối (hoặc xu hướng chuyển động) của vật này trên bề mặt vật kia.",
        "• Lực ma sát nghỉ: giữ cho vật đứng yên khi vật bị một lực tác dụng song song mặt tiếp xúc mà chưa chuyển động (F_msn cân bằng với lực kéo).\n"
        "• Lực ma sát trượt: xuất hiện khi một vật trượt trên bề mặt vật khác, luôn ngược chiều chuyển động.\n"
        "• Lực ma sát lăn: xuất hiện khi vật lăn trên bề mặt vật khác (độ lớn nhỏ hơn nhiều so với ma sát trượt).\n"
        "• Lực cản của nước và không khí phụ thuộc mạnh vào hình dạng vật (hình khí động học / hình con cá giúp giảm lực cản).",
        [
            {
                "category": "I. Ba loại Lực ma sát & Định luật ma sát cơ bản",
                "items": [
                    {"name": "Lực ma sát nghỉ (khi vật chưa trượt)", "formula": "F_msn = F_kéo  (và F_msn ≤ F_msn_cực_đại)", "note": "Giúp ta cầm nắm đồ vật, đi bộ không bị trượt ngã"},
                    {"name": "Lực ma sát trượt", "formula": "F_mst = μ · N", "note": "μ: hệ số ma sát trượt (phụ thuộc bản chất, độ nhám 2 bề mặt) ; N: áp lực vuông góc"},
                    {"name": "So sánh độ lớn (cùng áp lực)", "formula": "F_ma_sát_lăn  ≪  F_ma_sát_trượt", "note": "Lý do ổ bi (bạc đạn) giúp máy móc quay nhẹ nhàng"},
                ],
            },
            {
                "category": "II. Tăng ma sát có lợi & Giảm ma sát có hại",
                "items": [
                    {"name": "Tăng ma sát có lợi", "formula": "Tăng độ nhám bề mặt (khía rãnh lốp xe, đế giày, rắc cát lên đường trơn)", "note": ""},
                    {"name": "Giảm ma sát có hại", "formula": "Mài nhẵn, tra dầu mỡ bôi trơn, thay trượt bằng lăn (dùng ổ bi)", "note": ""},
                ],
            },
        ],
        "Thiết kế lốp xe chống trượt, má phanh an toàn, ổ bi cơ khí và kiểu dáng khí động học cho tàu cao tốc, máy bay.",
        "Chọn loại lốp và bề mặt đường để xe phanh an toàn trong các điều kiện thời tiết khác nhau.",
        "Một thùng hàng đặt trên sàn ngang bị kéo bởi một lực F = 15 N theo phương ngang nhưng thùng vẫn đứng yên. Hỏi lực ma sát nghỉ tác dụng lên thùng khi đó có độ lớn bằng bao nhiêu?",
        "Vì thùng vẫn đứng yên nên lực ma sát nghỉ cân bằng với lực kéo: F_msn = F = 15 N (và ngược chiều với lực kéo).",
        "Tại sao trên mặt lốp ô tô, xe máy và dưới đế giày thể thao người ta thường xẻ nhiều rãnh và gai nổi?",
        [
            "Để tiết kiệm cao su khi sản xuất",
            "Để làm giảm trọng lượng của xe và giày",
            "Để làm tăng lực ma sát bám đường, chống trơn trượt khi di chuyển và phanh",
            "Để tăng lực cản của không khí",
        ],
        2,
        "Tại sao khi đẩy một chiếc tủ nặng trên sàn nhà thì rất vất vả, nhưng nếu kê vài thanh gỗ tròn (hoặc lắp bánh xe) dưới đáy tủ thì lại đẩy đi rất nhẹ nhàng?",
        "Vì khi kê thanh gỗ tròn hoặc lắp bánh xe, ta đã thay thế lực ma sát trượt có độ lớn rất lớn bằng lực ma sát lăn có độ lớn nhỏ hơn rất nhiều lần.",
        game_title="Thử thách thực tế: Lực ma sát",
        game_description="Chọn vật liệu → chạy thử → phanh → đánh giá quãng đường dừng.",
    ),

    # =========================================================
    # VẬT LÝ LỚP 7 (7 BÀI)
    # =========================================================
    P(
        7,
        "toc-do-chuyen-dong",
        "Đồ thị Quãng đường - Thời gian (s - t) & Khoảng cách an toàn giao thông",
        "📈",
        "Vẽ và đọc đồ thị quãng đường - thời gian của chuyển động, tính tốc độ trung bình và khoảng cách dừng xe an toàn.",
        "Đồ thị quãng đường - thời gian (s - t) mô tả trực quan mối liên hệ giữa quãng đường đi được s và thời gian t; độ dốc của đồ thị biểu thị tốc độ của vật.",
        "• Trên đồ thị (s - t) với trục hoành Ot (thời gian) và trục tung Os (quãng đường):\n"
        "  + Đoạn thẳng nằm ngang (song song Ot): vật đang đứng yên (v = 0).\n"
        "  + Đường thẳng đi lên càng dốc thì tốc độ chuyển động của vật càng lớn.\n"
        "• Tốc độ trung bình trên nhiều chặng đường: v_tb = (s₁ + s₂ + ...) / (t₁ + t₂ + ...) (Lưu ý: KHÔNG bằng trung bình cộng các tốc độ!).\n"
        "• Quy tắc '3 giây' tính khoảng cách an toàn tối thiểu giữa hai xe trên đường cao tốc.",
        [
            {
                "category": "I. Tốc độ từ Đồ thị (s - t) & Tốc độ trung bình",
                "items": [
                    {"name": "Tốc độ trên một giai đoạn thẳng", "formula": "v = Δs / Δt = (s₂ − s₁) / (t₂ − t₁)", "note": "Độ dốc (hệ số góc) của đoạn thẳng trên đồ thị s - t"},
                    {"name": "Tốc độ trung bình trên cả lộ trình", "formula": "v_tb = s_tổng / t_tổng = (s₁ + s₂) / (t₁ + t₂)", "note": "Luôn lấy tổng quãng đường chia tổng thời gian"},
                ],
            },
            {
                "category": "II. Khoảng cách an toàn giao thông (Quy tắc 3 giây)",
                "items": [
                    {"name": "Quãng đường dừng xe an toàn", "formula": "s_dừng = s_phản_ứng + s_hãm_phanh", "note": ""},
                    {"name": "Quy tắc 3 giây trên cao tốc", "formula": "d_an_toàn (m) = v (m/s) × 3 (s)", "note": "Ví dụ: xe chạy 25 m/s (90 km/h) cần cách xe trước ít nhất 75 m"},
                ],
            },
        ],
        "Giúp phân tích hành trình qua biểu đồ, điều phối giao thông và giữ khoảng cách an toàn khi lái xe.",
        "Điều phối xe giao hàng dựa trên đồ thị s - t và tính khoảng cách an toàn.",
        "Một người đi xe đạp lên một đoạn dốc dài 120 m hết 40 s, sau đó xuống dốc dài 180 m hết 20 s. Tính tốc độ trung bình của người đó trên từng đoạn đường và trên cả hai đoạn dốc.",
        "Tốc độ lên dốc: v₁ = 120 / 40 = 3 (m/s). Tốc độ xuống dốc: v₂ = 180 / 20 = 9 (m/s). Tốc độ trung bình trên cả hai đoạn: v_tb = (120 + 180) / (40 + 20) = 300 / 60 = 5 (m/s).",
        "Trên đồ thị quãng đường - thời gian (s - t), nếu đường biểu diễn là một đoạn thẳng song song với trục thời gian Ot thì vật đang ở trạng thái nào?",
        [
            "Chuyển động nhanh dần",
            "Chuyển động với tốc độ không đổi khác 0",
            "Đứng yên (tốc độ bằng 0)",
            "Quay ngược chiều chuyển động",
        ],
        2,
        "Một ô tô đi nửa quãng đường đầu với tốc độ v₁ = 40 km/h và nửa quãng đường sau với tốc độ v₂ = 60 km/h. Hãy tính tốc độ trung bình của ô tô trên cả quãng đường.",
        "Gọi cả quãng đường là 2s (km). Thời gian đi nửa đầu là t₁ = s/40; thời gian đi nửa sau là t₂ = s/60. Tốc độ trung bình là: v_tb = 2s / (s/40 + s/60) = 2 / (1/40 + 1/60) = (2 · 40 · 60) / (40 + 60) = 48 (km/h).",
        game_title="Thử thách thực tế: Tốc độ chuyển động",
        game_description="Chọn tốc độ → đọc đồ thị s - t → xử lý khoảng cách an toàn trên đường.",
    ),
    P(
        7,
        "am-thanh",
        "Sóng âm, Độ cao - Độ to của âm & Phản xạ âm (Tiếng vang - Sonar)",
        "🔊",
        "Hiểu sự tạo thành và truyền sóng âm, mối liên hệ giữa tần số - độ cao, biên độ - độ to và ứng dụng phản xạ âm.",
        "Nguồn âm là các vật dao động phát ra âm thanh. Sóng âm truyền được trong các môi trường rắn, lỏng, khí (v_rắn > v_lỏng > v_khí) nhưng KHÔNG truyền được trong chân không.",
        "• Tần số f (đơn vị Hertz - Hz) là số dao động thực hiện trong 1 giây: Tần số càng lớn thì âm nghe càng CAO (bổng); tần số càng nhỏ thì âm càng THẤP (trầm). Tai người nghe được âm từ 20 Hz đến 20 000 Hz (dưới 20 Hz là hạ âm, trên 20 000 Hz là siêu âm).\n"
        "• Biên độ dao động là độ lệch lớn nhất của vật khỏi vị trí cân bằng: Biên độ càng lớn thì âm nghe càng TO (đơn vị đo mức cường độ âm là đề-xi-ben - dB).\n"
        "• Phản xạ âm và Tiếng vang: Ta nghe được tiếng vang khi âm phản xạ truyền đến tai chậm hơn âm trực tiếp ít nhất 1/15 giây.",
        [
            {
                "category": "I. Tần số, Chu kỳ & Tốc độ truyền âm",
                "items": [
                    {"name": "Tần số dao động f (Hz)", "formula": "f = N / t = 1 / T", "note": "N: số dao động trong t giây ; T: chu kỳ (s)"},
                    {"name": "Tốc độ truyền âm trong các môi trường", "formula": "v_rắn > v_lỏng > v_khí  (Trong không khí ở 20°C: v ≈ 340 m/s ; trong nước: v ≈ 1500 m/s ; trong thép: v ≈ 6100 m/s)", "note": "Chân không: v = 0 (không truyền âm)"},
                ],
            },
            {
                "category": "II. Phản xạ âm, Tiếng vang & Đo độ sâu bằng Sonar",
                "items": [
                    {"name": "Khoảng cách từ nguồn âm đến vật cản phản xạ (Sonar)", "formula": "d = (v · t) / 2", "note": "Chia 2 vì sóng âm đi từ nguồn tới vật cản rồi quay ngược lại (quãng đường 2d)"},
                    {"name": "Khoảng cách tối thiểu để nghe thấy Tiếng vang trong không khí", "formula": "d_min = (340 · 1/15) / 2 ≈ 11,33 m", "note": "Do thời gian trễ Δt ≥ 1/15 s"},
                ],
            },
        ],
        "Ứng dụng trong chế tạo nhạc cụ, thiết kế vật liệu cách âm rạp chiếu phim và tàu đo độ sâu đáy biển bằng sóng siêu âm Sonar.",
        "Thiết kế hệ thống cảnh báo âm thanh và dùng sóng siêu âm Sonar đo độ sâu đáy biển.",
        "Một tàu khảo sát phát ra một xung siêu âm thẳng đứng xuống đáy biển và thu được âm phản xạ sau 1,2 giây. Biết tốc độ truyền siêu âm trong nước biển là 1 500 m/s. Tính độ sâu của đáy biển tại vị trí đó.",
        "Trong 1,2 giây sóng siêu âm đi từ tàu xuống đáy biển rồi phản xạ ngược lên tàu (quãng đường 2d). Vậy độ sâu đáy biển là: d = (v · t) / 2 = (1500 · 1,2) / 2 = 900 (m).",
        "Dây đàn bầu thứ nhất thực hiện 880 dao động trong 2 giây; dây đàn thứ hai thực hiện 330 dao động trong 1 giây. Kết luận nào sau đây là ĐÚNG?",
        [
            "Dây thứ nhất phát ra âm cao hơn vì có tần số 440 Hz > 330 Hz",
            "Dây thứ hai phát ra âm cao hơn",
            "Hai dây phát ra âm có cùng độ cao",
            "Dây thứ nhất phát ra âm to hơn dây thứ hai",
        ],
        0,
        "Một người đứng trước một vách núi đá và hét to một tiếng, sau 0,8 giây người đó nghe thấy tiếng vang của chính mình. Biết tốc độ truyền âm trong không khí là 340 m/s. Tính khoảng cách từ người đó đến vách núi.",
        "Khoảng cách từ người đó đến vách núi là: d = (v · t) / 2 = (340 · 0,8) / 2 = 136 (m).",
        game_title="Thử thách thực tế: Âm thanh & Sonar",
        game_description="Tạo tín hiệu âm → điều chỉnh tần số và biên độ → đo khoảng cách bằng phản xạ âm.",
    ),
    P(
        7,
        "anh-sang",
        "Sự truyền thẳng của Ánh sáng, Bóng tối - Nhật thực - Nguyệt thực & Định luật Phản xạ ánh sáng",
        "☀️",
        "Hiểu định luật truyền thẳng ánh sáng, vùng bóng tối - bóng nửa tối và định luật phản xạ ánh sáng (i' = i).",
        "Ánh sáng là một dạng năng lượng phát ra từ các nguồn sáng. Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường thẳng.",
        "• Tia sáng được biểu diễn bằng một đường thẳng có mũi tên chỉ hướng truyền; ba loại chùm sáng: song song, hội tụ, phân kỳ.\n"
        "• Vùng bóng tối (không nhận được ánh sáng từ nguồn) và vùng bóng nửa tối (chỉ nhận được một phần ánh sáng từ nguồn sáng rộng); giải thích hiện tượng Nhật thực (Mặt Trăng che Mặt Trời) và Nguyệt thực (Trái Đất che Mặt Trăng).\n"
        "• Định luật phản xạ ánh sáng và phân biệt phản xạ gương (trên mặt nhẵn bóng) với phản xạ khuếch tán (trên mặt gồ ghề).",
        [
            {
                "category": "I. Tốc độ ánh sáng & Định luật truyền thẳng",
                "items": [
                    {"name": "Tốc độ ánh sáng trong chân không / không khí", "formula": "c ≈ 300 000 km/s = 3 · 10⁸ m/s", "note": "1 năm ánh sáng ≈ 9,46 · 10¹² km"},
                ],
            },
            {
                "category": "II. Định luật Phản xạ ánh sáng",
                "items": [
                    {"name": "Mặt phẳng chứa tia phản xạ", "formula": "Tia phản xạ IR nằm trong mặt phẳng chứa tia tới SI và pháp tuyến IN tại điểm tới I", "note": "IN vuông góc với mặt gương tại I"},
                    {"name": "Quan hệ giữa Góc phản xạ (i') và Góc tới (i)", "formula": "i' = i  (với i = ∠SIN ; i' = ∠NIR)", "note": "Góc hợp bởi tia sáng với mặt gương là α = 90° − i"},
                    {"name": "Góc lệch giữa tia tới và tia phản xạ", "formula": "∠SIR = i + i' = 2i", "note": "Tia tới vuông góc mặt gương (i = 0°) thì tia phản xạ truyền ngược lại (i' = 0°)"},
                ],
            },
        ],
        "Giải thích hiện tượng thiên văn (nhật thực, nguyệt thực), ngắm thẳng hàng trong xây dựng và thiết kế hệ thống gương phản chiếu.",
        "Điều chỉnh góc nghiêng của gương để điều hướng tia laser đến đúng vị trí cảm biến.",
        "Chiếu một tia sáng SI hợp với mặt gương phẳng một góc 35°. Hãy tính góc tới i, góc phản xạ i' và góc hợp bởi tia tới với tia phản xạ.",
        "Pháp tuyến IN vuông góc với mặt gương nên góc tới là: i = 90° − 35° = 55°. Theo định luật phản xạ ánh sáng, góc phản xạ là: i' = i = 55°. Góc hợp bởi tia tới và tia phản xạ là: i + i' = 55° + 55° = 110°.",
        "Hiện tượng Nhật thực toàn phần quan sát được ở những nơi trên Trái Đất nằm trong vùng nào?",
        [
            "Vùng bóng tối của Mặt Trăng in trên Trái Đất (khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất)",
            "Vùng bóng tối của Trái Đất in trên Mặt Trăng",
            "Vùng bóng nửa tối của Mặt Trăng",
            "Bất kỳ nơi nào đang là ban đêm trên Trái Đất",
        ],
        0,
        "Một tia sáng Mặt Trời chiếu nghiêng một góc 30° so với phương nằm ngang. Cần đặt một gương phẳng hợp với phương nằm ngang một góc bao nhiêu độ để tia phản xạ có phương thẳng đứng hướng xuống đáy giếng?",
        "Góc giữa tia tới (nghiêng 30° so với phương ngang) và tia phản xạ (thẳng đứng hướng xuống, vuông góc phương ngang) là: ∠SIR = 30° + 90° = 120°. Suy ra góc tới i = ∠SIR / 2 = 60°. Vì pháp tuyến IN là tia phân giác của ∠SIR nên pháp tuyến hợp với phương thẳng đứng góc 60°, do đó mặt gương hợp với phương nằm ngang một góc 60°.",
        game_title="Thử thách thực tế: Ánh sáng",
        game_description="Xoay gương → quan sát tia phản xạ → tối ưu vị trí cảm biến.",
    ),
    P(
        7,
        "guong-phang",
        "Ảnh của vật tạo bởi Gương phẳng & Kính tiềm vọng",
        "🪞",
        "Nắm vững tính chất ảnh ảo qua gương phẳng và cách dựng ảnh bằng tính chất đối xứng.",
        "Ảnh của một vật tạo bởi gương phẳng là ảnh ảo (không hứng được trên màn chắn), có độ lớn bằng vật và đối xứng với vật qua mặt phẳng gương.",
        "• Ba tính chất của ảnh tạo bởi gương phẳng:\n"
        "  1. Là ảnh ảo, không hứng được trên màn chắn.\n"
        "  2. Độ lớn của ảnh luôn bằng độ lớn của vật.\n"
        "  3. Điểm sáng S và ảnh S' của nó đối xứng nhau qua gương (SS' vuông góc với mặt gương và khoảng cách từ S đến gương bằng khoảng cách từ S' đến gương: d' = d).\n"
        "• Cách dựng ảnh của một vật AB qua gương phẳng và nguyên lý kính tiềm vọng (dùng 2 gương phẳng đặt song song, nghiêng 45°).",
        [
            {
                "category": "I. Công thức vị trí và kích thước Ảnh qua Gương phẳng",
                "items": [
                    {"name": "Khoảng cách từ ảnh đến gương (d') và vật đến gương (d)", "formula": "d' = d  ⇒  Khoảng cách từ vật đến ảnh: L = d + d' = 2d", "note": "Đoạn nối vật và ảnh vuông góc với mặt gương"},
                    {"name": "Chiều cao ảnh (h') và chiều cao vật (h)", "formula": "h' = h", "note": "Dù tiến lại gần hay ra xa gương thì kích thước ảnh vẫn không đổi"},
                    {"name": "Dịch chuyển vật - ảnh", "formula": "Vật tiến lại gần gương đoạn Δd ⇒ khoảng cách vật - ảnh giảm 2·Δd", "note": "Nếu giữ vật cố định, tịnh tiến gương ra xa đoạn a thì ảnh dịch đi đoạn 2a"},
                ],
            },
            {
                "category": "II. Hai gương phẳng ghép & Kính tiềm vọng",
                "items": [
                    {"name": "Kính tiềm vọng", "formula": "2 gương phẳng đặt song song, nghiêng góc 45° so với phương truyền sáng", "note": "Tia sáng phản xạ 2 lần góc 90°, đổi phương song song với tia ban đầu"},
                ],
            },
        ],
        "Ứng dụng trong thiết kế nội thất mở rộng không gian, kính tiềm vọng trên tàu ngầm và gương chiếu hậu.",
        "Đặt biển báo và gương phẳng tại góc khuất cửa hàng để mở rộng vùng quan sát.",
        "Một người cao 1,65 m đứng trước một gương phẳng đặt thẳng đứng và cách gương 1,5 m. Hỏi ảnh của người đó cao bao nhiêu mét và cách người đó bao nhiêu mét? Nếu người đó lùi ra xa gương thêm 0,5 m thì ảnh cách người đó bao nhiêu mét?",
        "Ảnh cao bằng người: h' = 1,65 m và cách người đó một khoảng: L₁ = 2 · 1,5 = 3,0 (m). Khi lùi xa thêm 0,5 m, khoảng cách từ người đến gương là d₂ = 1,5 + 0,5 = 2,0 (m), nên khoảng cách từ người đến ảnh là: L₂ = 2 · 2,0 = 4,0 (m).",
        "Một điểm sáng S đặt cách mặt gương phẳng 20 cm. Nếu cho điểm sáng S dịch chuyển lại gần gương một đoạn 5 cm theo phương vuông góc với mặt gương thì khoảng cách giữa S và ảnh S' của nó khi đó là:",
        ["15 cm", "30 cm", "35 cm", "40 cm"],
        1,
        "Một người cao 1,68 m, mắt cách đỉnh đầu 8 cm, đứng thẳng trước một gương phẳng treo thẳng đứng trên tường. Hỏi chiều cao tối thiểu của chiếc gương phẳng là bao nhiêu để người đó có thể nhìn thấy toàn bộ ảnh của cơ thể mình từ đỉnh đầu đến gót chân?",
        "Theo tính chất đường trung bình trong tam giác đồng dạng tạo bởi mắt và ảnh của cơ thể qua gương, chiều cao tối thiểu của gương phẳng luôn bằng một nửa chiều cao của người: h_gương_min = 1,68 / 2 = 0,84 (m) = 84 (cm) (không phụ thuộc khoảng cách đứng xa hay gần gương!).",
        game_title="Thử thách thực tế: Gương phẳng",
        game_description="Di chuyển gương → kiểm tra vùng nhìn thấy (thị trường của gương) → chọn vị trí tối ưu.",
    ),
    P(
        7,
        "nam-cham",
        "Nam châm vĩnh cửu, Tương tác từ & Đường sức từ",
        "🧲",
        "Khám phá tính chất từ của nam châm, tương tác hút - đẩy giữa hai cực từ và quy ước chiều đường sức từ.",
        "Nam châm là vật có từ tính (có khả năng hút các vật bằng sắt, thép, niken, coban...). Mọi nam châm đều có hai cực: cực Bắc (North - N, thường sơn màu đỏ) và cực Nam (South - S, thường sơn màu xanh).",
        "• Khi để tự do, cực luôn hướng về phía Bắc địa lý gọi là cực Bắc (N), cực hướng về phía Nam địa lý gọi là cực Nam (S).\n"
        "• Tương tác giữa hai nam châm: Các cực cùng tên thì đẩy nhau (N đẩy N, S đẩy S); các cực khác tên thì hút nhau (N hút S).\n"
        "• Từ trường là không gian xung quanh nam châm (hoặc xung quanh dòng điện) có khả năng tác dụng lực từ lên kim nam châm đặt trong nó.\n"
        "• Đường sức từ có chiều quy ước: ở bên ngoài thanh nam châm, đường sức từ đi ra từ cực Bắc (N) và đi vào cực Nam (S).",
        [
            {
                "category": "I. Quy luật Tương tác từ & Từ phổ",
                "items": [
                    {"name": "Tương tác giữa hai cực từ", "formula": "Cùng cực (N–N hoặc S–S): ĐẨY NHAU  ;  Khác cực (N–S): HÚT NHAU", "note": "Vật liệu từ (Fe, Ni, Co) luôn bị cả hai cực của nam châm hút"},
                    {"name": "Độ mạnh yếu của từ trường", "formula": "Chỗ đường sức từ càng DÀY (gần 2 đầu cực từ) ⇒ từ trường càng MẠNH", "note": "Chỗ đường sức từ càng thưa ⇒ từ trường càng yếu"},
                ],
            },
            {
                "category": "II. Quy ước chiều Đường sức từ",
                "items": [
                    {"name": "Bên ngoài nam châm", "formula": "Đi RA từ cực Bắc (N) → đi VÀO cực Nam (S)", "note": "Ghi nhớ: 'Ra Bắc - Vào Nam'"},
                    {"name": "Định hướng kim nam châm thử", "formula": "Tại mỗi điểm, trục kim nam châm nằm dọc theo đường sức từ; cực N hướng theo chiều đường sức", "note": ""},
                ],
            },
        ],
        "Từ trường của nam châm là nền tảng của la bàn định hướng, tàu đệm từ Maglev, loa điện động và ổ cứng từ.",
        "Tạo cơ cấu khóa cửa và phân loại phế liệu sắt tự động dùng nam châm.",
        "Có hai thanh kim loại A và B bề ngoài giống hệt nhau, trong đó một thanh là sắt thường và một thanh là nam châm vĩnh cửu. Không dùng thêm dụng cụ nào khác, làm thế nào để biết thanh nào là nam châm?",
        "Đưa một đầu của thanh A chạm vào chính giữa thanh B (nơi từ tính của nam châm gần như bằng 0): nếu chúng hút nhau mạnh thì A là nam châm, B là sắt; nếu hầu như không hút nhau thì B là nam châm, A là sắt.",
        "Ở bên ngoài một thanh nam châm thẳng, các đường sức từ có chiều như thế nào?",
        [
            "Đi ra từ cực Nam (S) và đi vào cực Bắc (N)",
            "Đi ra từ cực Bắc (N) và đi vào cực Nam (S)",
            "Đi ra từ cả hai cực Bắc và Nam",
            "Đi vào ở cả hai cực Bắc và Nam",
        ],
        1,
        "Nếu một thanh nam châm thẳng không may bị gãy đôi ở chính giữa thành hai nửa, thì mỗi nửa có chỉ còn lại một cực từ duy nhất (một nửa toàn cực N, một nửa toàn cực S) hay không? Vì sao?",
        "Không! Khi thanh nam châm gãy đôi, mỗi nửa lập tức trở thành một nam châm mới hoàn chỉnh có đủ cả hai cực Bắc (N) và Nam (S); không bao giờ tách riêng được một cực từ độc lập.",
        game_title="Thử thách thực tế: Nam châm và từ trường",
        game_description="Đặt nam châm → quan sát từ phổ và đường sức từ → điều chỉnh cơ cấu lực từ.",
    ),
    P(
        7,
        "nam-cham-dien-tu-truong-trai-dat",
        "Từ trường Trái Đất, La bàn & Nam châm điện",
        "🧭",
        "Hiểu cấu tạo từ trường Trái Đất bảo vệ sự sống, nguyên lý hoạt động của la bàn và cách chế tạo, điều khiển nam châm điện.",
        "Trái Đất của chúng ta là một thanh nam châm khổng lồ với cực từ Nam nằm gần cực Bắc địa lý và cực từ Bắc nằm gần cực Nam địa lý. Nam châm điện là dụng cụ tạo ra lực từ nhờ dòng điện chạy qua ống dây dẫn có lõi sắt non.",
        "• Vì cực Bắc (N) của kim la bàn luôn bị hút về phía Bắc địa lý nên ở gần cực Bắc địa lý của Trái Đất thực chất là CỰC TỪ NAM của nam châm Trái Đất (và lệch một góc nhỏ gọi là độ từ thiên).\n"
        "• Cấu tạo nam châm điện: gồm một ống dây dẫn có dòng điện một chiều chạy qua, bên trong có lõi sắt non (dùng sắt non vì khi ngắt điện, sắt non mất hết từ tính ngay; còn lõi thép sẽ bị nhiễm từ vĩnh viễn).\n"
        "• Cách làm tăng lực từ của nam châm điện: Tăng cường độ dòng điện I chạy qua các vòng dây hoặc tăng số vòng dây N của ống dây.",
        [
            {
                "category": "I. Từ trường Trái Đất & La bàn",
                "items": [
                    {"name": "Cực từ Trái Đất và Cực địa lý", "formula": "Cực Bắc địa lý ≈ Cực từ Nam (S) ; Cực Nam địa lý ≈ Cực từ Bắc (N)", "note": "Do cực N của kim la bàn bị hút về cực từ S (ở phương Bắc địa lý)"},
                ],
            },
            {
                "category": "II. Nam châm điện & Điều khiển từ tính",
                "items": [
                    {"name": "Độ mạnh của Nam châm điện", "formula": "Lực từ F_từ tỉ lệ thuận với Cường độ dòng điện (I) và Số vòng dây (N)", "note": "Tăng I hoặc tăng N ⇒ nam châm điện càng mạnh"},
                    {"name": "Đổi cực của Nam châm điện", "formula": "Đổi chiều dòng điện chạy vào ống dây ⇔ Hai cực Bắc (N) - Nam (S) của nam châm điện đổi chỗ cho nhau", "note": ""},
                ],
            },
        ],
        "Ứng dụng trong cần cẩu điện bốc dỡ sắt thép ở cảng, rơ-le điện từ, chuông điện và định hướng hàng hải bằng la bàn.",
        "Điều chỉnh dòng điện và số vòng dây của cần cẩu nam châm điện để nâng và thả các kiện sắt thép đúng vị trí.",
        "Một học sinh chế tạo hai nam châm điện có cùng lõi sắt non: nam châm A có N₁ = 100 vòng dây và dòng điện I₁ = 1 A; nam châm B có N₂ = 250 vòng dây và dòng điện I₂ = 2 A. Nam châm nào hút được nhiều đinh sắt hơn? Khi ngắt công tắc điện thì hiện tượng gì xảy ra?",
        "Nam châm B có cả số vòng dây lớn hơn (250 > 100) và cường độ dòng điện lớn hơn (2 A > 1 A) nên từ trường của B mạnh hơn A rất nhiều, hút được nhiều đinh sắt hơn. Khi ngắt công tắc điện, lõi sắt non mất từ tính ngay nên các đinh sắt rơi xuống.",
        "Vì sao lõi của nam châm điện thường được làm bằng SẮT NON mà không làm bằng THÉP?",
        [
            "Vì sắt non rẻ hơn thép",
            "Vì khi ngắt dòng điện, sắt non mất ngay từ tính giúp nam châm điện nhả vật ra được; còn thép giữ từ tính lâu dài",
            "Vì thép không bị nam châm hút",
            "Vì sắt non không dẫn điện",
        ],
        1,
        "Khi sử dụng la bàn để xác định phương hướng trong rừng, tại sao ta phải để la bàn tránh xa điện thoại di động, loa nghe nhạc hoặc các vật dụng lớn bằng sắt thép?",
        "Vì điện thoại, loa có chứa nam châm/dòng điện tạo ra từ trường riêng và các vật bằng sắt thép làm biến dạng từ trường xung quanh, khiến kim la bàn bị lệch khỏi hướng từ trường Trái Đất và chỉ sai phương hướng.",
        game_title="Thử thách thực tế: Nam châm điện & La bàn",
        game_description="Thay đổi số vòng dây N, dòng điện I và đóng/ngắt mạch để vận hành cần cẩu từ.",
    ),
    P(
        7,
        "anh-sang-mau",
        "Ánh sáng đơn sắc, Ánh sáng trắng & Sự trộn màu - Màu sắc các vật",
        "🌈",
        "Hiểu sự tán sắc ánh sáng trắng thành 7 màu cầu vồng, tổng hợp ba màu cơ bản (Đỏ - Lục - Lam) và sự hấp thụ/tán xạ màu của vật.",
        "Ánh sáng trắng (như ánh sáng Mặt Trời) là tập hợp của vô số ánh sáng đơn sắc có màu biến thiên liên tục từ Đỏ, Da cam, Vàng, Lục, Lam, Chàm đến Tím.",
        "• Khi chiếu chùm sáng trắng hẹp qua lăng kính, chùm sáng bị phân tách thành dải 7 màu cầu vồng (tia đỏ lệch ít nhất, tia tím lệch nhiều nhất).\n"
        "• Trộn 3 chùm ánh sáng màu cơ bản của quang học là Đỏ (Red - R), Lục (Green - G), Lam (Blue - B) với cường độ thích hợp sẽ thu được ánh sáng trắng.\n"
        "• Màu sắc của các vật dưới ánh sáng: Vật màu nào thì phản xạ (hoặc truyền qua) mạnh ánh sáng màu đó và hấp thụ các ánh sáng màu còn lại. Vật màu trắng phản xạ hầu hết mọi ánh sáng màu; vật màu đen hấp thụ hết mọi ánh sáng màu.",
        [
            {
                "category": "I. Tán sắc & Trộn ánh sáng màu (Hệ màu cộng RGB)",
                "items": [
                    {"name": "Dải màu quang phổ ánh sáng trắng", "formula": "Đỏ – Da cam – Vàng – Lục – Lam – Chàm – Tím", "note": "Cầu vồng xuất hiện do ánh sáng Mặt Trời tán sắc qua các giọt nước mưa"},
                    {"name": "Tổng hợp ánh sáng màu cơ bản", "formula": "Đỏ (R) + Lục (G) = Vàng ; Đỏ (R) + Lam (B) = Hồng sẫm (Magenta) ; Lục (G) + Lam (B) = Xanh lơ (Cyan)", "note": "Đỏ + Lục + Lam = Trắng"},
                ],
            },
            {
                "category": "II. Quy tắc nhìn thấy Màu sắc của vật",
                "items": [
                    {"name": "Chiếu sáng trắng vào vật màu X", "formula": "Vật chỉ phản xạ ánh sáng màu X tới mắt ⇒ ta thấy vật có màu X", "note": ""},
                    {"name": "Chiếu ánh sáng đơn sắc màu Y vào vật màu X (Y ≠ X)", "formula": "Vật màu X hấp thụ ánh sáng màu Y ⇒ không có ánh sáng phản xạ tới mắt ⇒ ta thấy vật có MÀU ĐEN", "note": "Trừ khi vật có màu trắng thì chiếu màu gì sẽ thấy màu đó"},
                ],
            },
        ],
        "Nguyên lý tạo màu của màn hình TV, điện thoại (điểm ảnh RGB), hệ thống chiếu sáng sân khấu và nhiếp ảnh.",
        "Pha trộn các chùm sáng màu RGB để tạo tín hiệu và hiệu ứng ánh sáng sân khấu.",
        "Trong phòng tối, một cô ca sĩ mặc chiếc váy màu trắng có thêu bông hoa màu đỏ. Nếu đèn sân khấu chỉ chiếu ánh sáng đơn sắc màu lục (xanh lá cây) vào cô ca sĩ thì khán giả sẽ nhìn thấy chiếc váy và bông hoa có màu gì?",
        "Nền váy màu trắng phản xạ tốt mọi ánh sáng màu nên dưới ánh sáng lục sẽ có MÀU LỤC. Bông hoa màu đỏ hấp thụ ánh sáng màu lục (không phản xạ ánh sáng lục) nên khán giả sẽ thấy bông hoa có MÀU ĐEN.",
        "Vật có màu nào dưới đây hấp thụ mạnh nhất tất cả các ánh sáng màu chiếu tới nó (và nóng lên nhanh nhất dưới nắng)?",
        ["Vật màu trắng", "Vật màu đỏ", "Vật màu vàng", "Vật màu đen"],
        3,
        "Chiếu một chùm ánh sáng trắng đi qua một tấm kính lọc màu đỏ, sau đó cho tia sáng lọt qua đi tiếp qua tấm kính lọc thứ hai màu lam. Hỏi phía sau tấm kính lọc thứ hai ta quan sát thấy ánh sáng màu gì?",
        "Sau tấm kính lọc màu đỏ chỉ còn ánh sáng màu đỏ đi qua. Khi ánh sáng đỏ này gặp tấm kính lọc màu lam, tấm kính màu lam hấp thụ ánh sáng đỏ và không cho truyền qua, nên phía sau tấm kính thứ hai ta thấy TỐI (màu đen, không có ánh sáng lọt qua).",
        game_title="Thử thách thực tế: Ánh sáng màu RGB",
        game_description="Chọn màu đèn chiếu → phối ánh sáng RGB → quan sát sự thay đổi màu sắc vật thể.",
    ),

    # =========================================================
    # VẬT LÝ LỚP 8 (7 BÀI)
    # =========================================================
    P(
        8,
        "khoi-luong-rieng",
        "Khối lượng riêng (D) & Trọng lượng riêng (d)",
        "🧱",
        "Nắm vững công thức khối lượng riêng D = m/V, trọng lượng riêng d = P/V = 10D và phương pháp xác định khối lượng riêng của vật rắn, chất lỏng.",
        "Khối lượng riêng (D hoặc ρ) của một chất được xác định bằng khối lượng của một đơn vị thể tích chất đó: D = m / V. Đây là đại lượng đặc trưng cho từng chất giúp nhận biết vật liệu và dự đoán sự nổi - chìm.",
        "• Đơn vị của khối lượng riêng trong hệ SI là kg/m³ (ngoài ra thường dùng g/cm³ hoặc g/mL).\n"
        "• Quy đổi quan trọng: 1 g/cm³ = 1 g/mL = 1 000 kg/m³ (Ví dụ: nước nguyên chất có D = 1 g/cm³ = 1 000 kg/m³).\n"
        "• Trọng lượng riêng d là trọng lượng của một đơn vị thể tích chất đó: d = P / V = 10 · D (đơn vị N/m³).\n"
        "• Cách đo khối lượng riêng của viên sỏi không thấm nước: dùng cân đo m và dùng bình chia độ chứa nước (phương pháp dâng nước) để đo V = V₂ − V₁.",
        [
            {
                "category": "I. Công thức Khối lượng riêng (D) & Trọng lượng riêng (d)",
                "items": [
                    {"name": "Khối lượng riêng", "formula": "D = m / V  ⇒  m = D · V  ;  V = m / D", "note": "D (kg/m³), m (kg), V (m³)"},
                    {"name": "Trọng lượng riêng", "formula": "d = P / V = 10 · D", "note": "d (N/m³), P (N), V (m³)"},
                ],
            },
            {
                "category": "II. Quy đổi đơn vị & Khối lượng riêng hỗn hợp",
                "items": [
                    {"name": "Hệ số quy đổi chuẩn", "formula": "1 g/cm³ = 1 000 kg/m³  ;  1 kg/m³ = 0,001 g/cm³", "note": "D_nước = 1000 kg/m³ ; D_sắt ≈ 7800 kg/m³ ; D_nhôm ≈ 2700 kg/m³"},
                    {"name": "KLR trung bình của hợp kim / hỗn hợp (không hao hụt thể tích)", "formula": "D_tb = (m₁ + m₂) / (V₁ + V₂)", "note": ""},
                ],
            },
        ],
        "Ứng dụng trong chọn vật liệu hàng không (hợp kim nhôm - titan siêu nhẹ), kiểm tra độ nguyên chất của kim loại và tính tải trọng công trình.",
        "Chọn vật liệu làm cầu mini sao cho đủ bền nhưng tổng khối lượng nhẹ nhất.",
        "Thả chìm hoàn toàn một hòn đá nặng 130 g vào bình chia độ đang chứa 50 cm³ nước thì mực nước trong bình dâng lên đến vạch 100 cm³. Tính khối lượng riêng của hòn đá theo g/cm³ và kg/m³.",
        "Thể tích hòn đá bằng phần nước dâng lên: V = 100 − 50 = 50 (cm³). Khối lượng riêng của hòn đá là: D = m / V = 130 / 50 = 2,6 (g/cm³) = 2 600 (kg/m³).",
        "Biết khối lượng riêng của nhôm là 2 700 kg/m³. Một khối nhôm đặc có thể tích 2 dm³ sẽ có khối lượng là bao nhiêu?",
        ["1,35 kg", "2,7 kg", "5,4 kg", "54 kg"],
        2,
        "Một bức tượng bằng đồng nặng 1,78 kg được nhúng chìm hoàn toàn vào nước thì chiếm thể tích 250 cm³. Biết khối lượng riêng của đồng nguyên chất là 8,9 g/cm³. Hỏi bức tượng đồng đó là đặc hoàn toàn hay bị rỗng bên trong? Nếu rỗng thì thể tích phần rỗng là bao nhiêu?",
        "Đổi m = 1,78 kg = 1 780 g. Thể tích phần đồng thực sự tạo nên tượng là: V_đồng = m / D = 1780 / 8,9 = 200 (cm³). Vì thể tích toàn bộ bức tượng là 250 cm³ > 200 cm³ nên bức tượng bị RỖNG bên trong, với thể tích phần rỗng là: V_rỗng = 250 − 200 = 50 (cm³).",
        game_title="Thử thách thực tế: Khối lượng riêng",
        game_description="Đo m và V → tính khối lượng riêng D → kiểm tra vật đặc hay rỗng.",
    ),
    P(
        8,
        "ap-suat",
        "Áp lực, Áp suất trên một bề mặt, Áp suất chất lỏng & Áp suất khí quyển",
        "🚜",
        "Tính áp suất chất rắn p = F/S, áp suất chất lỏng p = d·h, nguyên lý bình thông nhau - máy nén thủy lực và áp suất khí quyển.",
        "Áp lực là lực ép có phương vuông góc với mặt bị ép. Áp suất (p) được tính bằng độ lớn của áp lực trên một đơn vị diện tích bị ép: p = F / S.",
        "• Đơn vị áp suất trong hệ SI là Pascal (Pa): 1 Pa = 1 N/m² (ngoài ra còn dùng kPa, bar, atm, mmHg).\n"
        "• Cách tăng áp suất (tăng F hoặc giảm diện tích tiếp xúc S như mài sắc lưỡi dao, đầu đinh nhọn) và giảm áp suất (tăng diện tích S như bản xích xe tăng, móng nhà rộng).\n"
        "• Áp suất chất lỏng tác dụng theo mọi phương lên đáy bình, thành bình và các vật trong lòng chất lỏng: p = d · h = D · g · h.\n"
        "• Bình thông nhau và Máy nén thủy lực: F₁ / F₂ = S₁ / S₂; Áp suất khí quyển (ở ngang mực nước biển p₀ ≈ 760 mmHg ≈ 101 325 Pa).",
        [
            {
                "category": "I. Áp suất trên bề mặt rắn (p = F / S)",
                "items": [
                    {"name": "Công thức Áp suất", "formula": "p = F / S  ⇒  F = p · S  ;  S = F / p", "note": "F: áp lực vuông góc (N) ; S: diện tích bị ép (m²) ; p: áp suất (Pa = N/m²)"},
                    {"name": "Đơn vị quy đổi", "formula": "1 kPa = 1 000 Pa ; 1 atm ≈ 101 325 Pa ≈ 760 mmHg", "note": "Chú ý đổi cm² sang m²: 1 cm² = 10⁻⁴ m²"},
                ],
            },
            {
                "category": "II. Áp suất chất lỏng & Máy nén thủy lực (Nguyên lý Pascal)",
                "items": [
                    {"name": "Áp suất cột chất lỏng ở độ sâu h", "formula": "p = d · h = D · g · h", "note": "h tính từ mặt thoáng chất lỏng xuống điểm xét (m)"},
                    {"name": "Áp suất tuyệt đối tại độ sâu h (kể cả khí quyển p₀)", "formula": "p_tổng = p₀ + d · h", "note": ""},
                    {"name": "Công thức Máy nén thủy lực", "formula": "F₂ / F₁ = S₂ / S₁", "note": "Diện tích pít-tông lớn gấp bao nhiêu lần pít-tông nhỏ thì lực nâng lớn gấp bấy nhiêu lần"},
                ],
            },
        ],
        "Giải thích nguyên lý kích thủy lực nâng ô tô, phanh thủy lực, đê đập thủy điện có chân rộng hơn đỉnh và giác mút chân không.",
        "Thiết kế diện tích bàn chân robot tự hành để không bị lún trên nền đất mềm.",
        "Một người nặng 60 kg đứng bằng cả hai bàn chân trên mặt đất phẳng ngang. Biết diện tích tiếp xúc của mỗi bàn chân với mặt đất là 150 cm². Tính áp suất của người đó tác dụng lên mặt đất khi đứng bằng hai chân và khi co một chân.",
        "Áp lực bằng trọng lượng cơ thể: F = P = 10 · 60 = 600 (N). Diện tích 1 bàn chân: S₁ = 150 cm² = 0,015 m²; 2 bàn chân: S₂ = 0,03 m². Khi đứng bằng 2 chân: p₂ = 600 / 0,03 = 20 000 (Pa) = 20 (kPa). Khi đứng 1 chân: p₁ = 600 / 0,015 = 40 000 (Pa) = 40 (kPa).",
        "Một thợ lặn đang ở độ sâu 25 m dưới mặt nước biển. Biết trọng lượng riêng của nước biển là d = 10 300 N/m³. Áp suất do riêng cột nước biển gây ra tại độ sâu đó là:",
        ["25 750 Pa", "257 500 Pa", "103 000 Pa", "412 Pa"],
        1,
        "Một máy nâng thủy lực trong trạm sửa chữa ô tô có diện tích pít-tông nhỏ là s = 15 cm² và diện tích pít-tông lớn là S = 300 cm². Để nâng một chiếc ô tô có khối lượng 1,8 tấn lên cao thì cần tác dụng lên pít-tông nhỏ một lực tối thiểu bằng bao nhiêu Newton?",
        "Trọng lượng của ô tô là: F₂ = P = 10 · 1800 = 18 000 (N). Tỉ số diện tích hai pít-tông là S / s = 300 / 15 = 20. Vậy lực cần tác dụng lên pít-tông nhỏ chỉ là: F₁ = F₂ / 20 = 18 000 / 20 = 900 (N).",
        game_title="Thử thách thực tế: Áp suất & Thủy lực",
        game_description="Chọn diện tích chân đế và pít-tông thủy lực → đặt tải → kiểm tra áp suất.",
    ),
    P(
        8,
        "luc-day-archimedes",
        "Lực đẩy Archimedes & Điều kiện định lượng vật Nổi - Lơ lửng - Chìm",
        "🚢",
        "Tính độ lớn lực đẩy Archimedes F_A = d_lỏng · V_chìm và giải các bài toán cân bằng lực khi vật nổi trên mặt thoáng.",
        "Một vật nhúng vào chất lỏng (hoặc chất khí) bị chất lỏng đẩy thẳng đứng từ dưới lên với một lực có độ lớn bằng trọng lượng của phần chất lỏng mà vật chiếm chỗ. Lực này gọi là lực đẩy Archimedes (F_A).",
        "• Độ lớn lực đẩy Archimedes: F_A = d_lỏng · V_chìm (trong đó V_chìm là thể tích phần vật thực sự chìm dưới mặt thoáng chất lỏng).\n"
        "• Điều kiện định tính và định lượng để vật đặc nhúng trong chất lỏng: Chìm xuống (P > F_A hay d_vật > d_lỏng), Lơ lửng (P = F_A hay d_vật = d_lỏng), Nổi lên (P < F_A hay d_vật < d_lỏng).\n"
        "• Chú ý quan trọng: Khi vật đã nổi và đứng yên cân bằng trên mặt thoáng chất lỏng thì lực đẩy Archimedes cân bằng với trọng lượng của vật: F_A = P_vật ⇔ d_lỏng · V_chìm = d_vật · V_vật.",
        [
            {
                "category": "I. Công thức Lực đẩy Archimedes & Cân bằng dưới nước",
                "items": [
                    {"name": "Độ lớn lực đẩy Archimedes", "formula": "F_A = d_lỏng · V_chìm = D_lỏng · g · V_chìm", "note": "V_chìm (m³): chỉ tính phần thể tích nằm dưới mặt chất lỏng"},
                    {"name": "Đo F_A bằng lực kế", "formula": "F_A = P − F_biểu_kiến", "note": "P: số chỉ lực kế ngoài không khí ; F_biểu_kiến: số chỉ khi nhúng vật trong nước"},
                ],
            },
            {
                "category": "II. Điều kiện Nổi - Chìm & Tỉ lệ thể tích chìm khi vật nổi",
                "items": [
                    {"name": "So sánh theo Trọng lượng riêng / KLR", "formula": "D_vật > D_lỏng: Chìm ; D_vật = D_lỏng: Lơ lửng ; D_vật < D_lỏng: Nổi", "note": ""},
                    {"name": "Khi vật nổi cân bằng trên mặt thoáng", "formula": "F_A = P_vật  ⇔  d_lỏng · V_chìm = d_vật · V_toàn_vật  ⇒  V_chìm / V_toàn_vật = D_vật / D_lỏng", "note": "Ví dụ: Nước đá (D=900) nổi trên nước (D=1000) có 90% thể tích chìm dưới nước"},
                ],
            },
        ],
        "Giải thích vì sao tàu biển bằng thép nặng hàng chục nghìn tấn vẫn nổi trên nước, nguyên lý lặn - nổi của tàu ngầm và khinh khí cầu.",
        "Điều chỉnh tải trọng hàng hóa trên một chiếc tàu để tàu nổi an toàn không vượt vạch mớn nước.",
        "Một vật bằng kim loại khi treo vào lực kế ngoài không khí thì lực kế chỉ 7,8 N. Khi nhúng vật chìm hoàn toàn trong nước (có trọng lượng riêng d₀ = 10 000 N/m³) thì lực kế chỉ 6,8 N. Tính lực đẩy Archimedes tác dụng lên vật, thể tích của vật và trọng lượng riêng của kim loại làm vật.",
        "Lực đẩy Archimedes là: F_A = P − F = 7,8 − 6,8 = 1,0 (N). Thể tích của vật là: V = F_A / d₀ = 1,0 / 10 000 = 10⁻⁴ (m³) = 100 (cm³). Trọng lượng riêng của chất làm vật là: d = P / V = 7,8 / 10⁻⁴ = 78 000 (N/m³) (đây là sắt/thép).",
        "Một khối gỗ hình hộp có khối lượng riêng D_gỗ = 600 kg/m³ được thả nổi tự do trong bể nước có D_nước = 1 000 kg/m³. Khi khối gỗ đứng yên cân bằng trên mặt nước, phần thể tích khối gỗ chìm dưới mặt nước chiếm bao nhiêu phần trăm thể tích cả khối gỗ?",
        ["40%", "50%", "60%", "75%"],
        2,
        "Một tảng băng trôi trên biển có thể tích phần nhô lên khỏi mặt nước biển là 100 m³. Biết khối lượng riêng của băng là D_băng = 920 kg/m³ và của nước biển là D_biển = 1 020 kg/m³. Hãy tính tổng thể tích của cả tảng băng đó.",
        "Gọi tổng thể tích tảng băng là V (m³), suy ra thể tích phần chìm là V_chìm = V − 100 (m³). Khi băng nổi cân bằng: F_A = P ⇔ D_biển · V_chìm = D_băng · V ⇔ 1020 · (V − 100) = 920 · V ⇔ 100 · V = 102 000 ⇔ V = 1 020 (m³).",
        game_title="Thử thách thực tế: Lực đẩy Archimedes",
        game_description="Thêm tải lên thuyền → theo dõi mực nước chiếm chỗ → giữ thuyền nổi an toàn.",
    ),
    P(
        8,
        "moment-luc-don-bay",
        "Tác dụng làm quay của lực, Moment lực & Quy tắc Đòn bẩy",
        "🔧",
        "Hiểu moment lực M = F · d đặc trưng cho tác dụng làm quay quanh trục và ứng dụng quy tắc cân bằng đòn bẩy.",
        "Moment lực (M) đối với một trục quay là đại lượng đặc trưng cho tác dụng làm quay của lực và được đo bằng tích của lực F với cánh tay đòn d của nó: M = F · d.",
        "• Cánh tay đòn (d) là khoảng cách vuông góc từ trục quay O đến giá của lực F (đơn vị mét - m).\n"
        "• Đơn vị của moment lực là Newton nhân mét (N·m).\n"
        "• Đòn bẩy gồm điểm tựa O (trục quay) và hai lực tác dụng F₁, F₂ có cánh tay đòn tương ứng d₁, d₂. Điều kiện cân bằng của đòn bẩy: F₁ · d₁ = F₂ · d₂ (lực tỉ lệ nghịch với cánh tay đòn).\n"
        "• Ba loại đòn bẩy trong kỹ thuật và trên cơ thể người (cánh tay nâng vật, khớp cổ chân, cái kéo, kìm, xe rùa, xà beng).",
        [
            {
                "category": "I. Moment lực & Điều kiện Cân bằng Đòn bẩy",
                "items": [
                    {"name": "Công thức Moment lực M", "formula": "M = F · d", "note": "F: độ lớn lực (N) ; d: cánh tay đòn - khoảng cách từ O đến giá của lực (m) ; M (N·m)"},
                    {"name": "Quy tắc cân bằng Đòn bẩy (Moment)", "formula": "M₁ = M₂  ⇔  F₁ · d₁ = F₂ · d₂  ⇔  F₁ / F₂ = d₂ / d₁", "note": "Muốn dùng lực nhỏ F₂ nâng vật nặng F₁ thì cần d₂ > d₁"},
                ],
            },
            {
                "category": "II. Ba loại Đòn bẩy thực tế",
                "items": [
                    {"name": "Đòn bẩy loại 1 (Điểm tựa O ở giữa)", "formula": "Ví dụ: Bập bênh, cái kéo, kìm cắt dây, xà beng bẩy đá", "note": "Có thể lợi về lực nếu OA < OB"},
                    {"name": "Đòn bẩy loại 2 (Vật chịu lực ở giữa O và lực tác dụng)", "formula": "Ví dụ: Xe rùa đẩy gạch, kẹp tách hạt dẻ, mở nắp chai", "note": "Luôn lợi về lực (d_lực > d_vật)"},
                    {"name": "Đòn bẩy loại 3 (Lực tác dụng ở giữa O và vật)", "formula": "Ví dụ: Đôi đũa, kẹp gắp đá, cơ nhị đầu cánh tay người", "note": "Lợi về đường đi / tốc độ"},
                ],
            },
        ],
        "Giải thích vì sao tay nắm cửa luôn đặt xa bản lề, vì sao cờ-lê cán dài tháo ốc dễ hơn và cách bẩy vật nặng bằng xà beng.",
        "Thiết kế chiều dài cánh tay đòn của cần cẩu tháp và đòn bẩy để nâng khối đá nặng với lực nhỏ nhất.",
        "Một người dùng xà beng dài 1,5 m để bẩy một tảng đá nặng 1 200 N. Biết khoảng cách từ điểm tựa O đến chỗ xà beng tì vào tảng đá là d₁ = 0,25 m; tay người nắm ở đầu kia của xà beng (cách điểm tựa d₂ = 1,5 − 0,25 = 1,25 m). Tính lực tối thiểu tay người cần ấn xuống để nâng được tảng đá.",
        "Áp dụng quy tắc cân bằng moment lực trên đòn bẩy: F₁ · d₁ = F₂ · d₂ ⇔ 1200 · 0,25 = F₂ · 1,25 ⇒ F₂ = 300 / 1,25 = 240 (N) (nhỏ hơn 5 lần so với trọng lượng tảng đá!).",
        "Tại sao tay nắm cửa ra vào luôn được lắp ở gần mép ngoài của cánh cửa (xa bản lề nhất) chứ không lắp ở gần bản lề?",
        [
            "Để trang trí cho cánh cửa cân đối",
            "Để tăng cánh tay đòn d đối với trục bản lề, giúp mở cửa dễ dàng chỉ với một lực nhỏ",
            "Để làm giảm trọng lượng của cánh cửa",
            "Để làm giảm ma sát ở bản lề",
        ],
        1,
        "Hai bạn An (nặng 45 kg) và Bình (nặng 30 kg) cùng ngồi chơi trên một chiếc bập bênh có trục quay ở chính giữa. Nếu bạn An ngồi cách trục quay 1,2 m thì bạn Bình phải ngồi ở phía bên kia cách trục quay bao nhiêu mét để bập bênh nằm ngang cân bằng?",
        "Trọng lượng của An là P₁ = 450 N (d₁ = 1,2 m); của Bình là P₂ = 300 N. Để bập bênh cân bằng: P₁ · d₁ = P₂ · d₂ ⇔ 450 · 1,2 = 300 · d₂ ⇒ d₂ = 540 / 300 = 1,8 (m).",
        game_title="Thử thách thực tế: Moment lực & Đòn bẩy",
        game_description="Thay đổi vị trí điểm tựa và cánh tay đòn → cân bằng bập bênh và nâng vật nặng.",
    ),
    P(
        8,
        "cong-suat",
        "Công cơ học, Công suất & Định luật về Công",
        "⚙️",
        "Tính công cơ học A = F · s, công suất P = A / t = F · v và hiểu định luật về công cho các máy cơ đơn giản.",
        "Công cơ học chỉ xuất hiện khi có lực tác dụng vào vật và làm cho vật dịch chuyển theo phương không vuông góc với phương của lực. Công suất cho biết tốc độ thực hiện công nhanh hay chậm.",
        "• Công cơ học A = F · s (khi vật dịch chuyển theo đúng hướng của lực F), đơn vị là Joule (J): 1 J = 1 N · 1 m; 1 kJ = 1 000 J.\n"
        "• Định luật về công: Không một máy cơ đơn giản nào (mặt phẳng nghiêng, đòn bẩy, ròng rọc động) cho ta lợi về công; được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi và ngược lại.\n"
        "• Công suất P = A / t = F · v, đơn vị là Watt (W): 1 W = 1 J/s; 1 kW = 1 000 W; 1 mã lực (HP) ≈ 736 W (hoặc 746 W).",
        [
            {
                "category": "I. Công cơ học (A) & Công suất (P)",
                "items": [
                    {"name": "Công cơ học (cùng hướng chuyển động)", "formula": "A = F · s  ;  Công nâng vật lên cao h: A = P · h = m · g · h", "note": "A (J), F (N), s (m)"},
                    {"name": "Công suất cơ học", "formula": "P = A / t = (F · s) / t = F · v", "note": "P (W), t (s), v (m/s) ; 1 kW = 1000 W ; 1 MW = 10⁶ W"},
                ],
            },
            {
                "category": "II. Định luật về Công & Hiệu suất Máy cơ đơn giản",
                "items": [
                    {"name": "Máy cơ lý tưởng (bỏ qua ma sát)", "formula": "A_kéo = A_nâng_trực_tiếp  ⇔  F · l = P · h", "note": "Mặt phẳng nghiêng dài l, cao h ; Ròng rọc động lợi 2 lần về lực (F = P/2, s = 2h)"},
                    {"name": "Hiệu suất mặt phẳng nghiêng / ròng rọc thực tế", "formula": "H = (A_có_ích / A_toàn_phần) × 100% = (P · h) / (F · l) × 100%", "note": "A_toàn_phần = A_có_ích + A_ma_sát"},
                ],
            },
        ],
        "Đánh giá sức mạnh của động cơ ô tô, cần cẩu, máy bơm nước và tính toán hiệu suất hệ thống cơ khí.",
        "Chọn động cơ nâng hàng vừa đủ nhanh vừa tối ưu hiệu suất năng lượng.",
        "Một cần cẩu nâng đều một kiện hàng có khối lượng 1,5 tấn lên độ cao 8 m trong thời gian 20 giây. Lấy g = 10 m/s². Tính công và công suất của cần cẩu đã thực hiện.",
        "Trọng lượng kiện hàng: P_trọng = 10 · 1500 = 15 000 (N). Công thực hiện để nâng hàng: A = P_trọng · h = 15 000 · 8 = 120 000 (J) = 120 (kJ). Công suất của cần cẩu: P = A / t = 120 000 / 20 = 6 000 (W) = 6 (kW).",
        "Một người dùng một mặt phẳng nghiêng dài l = 4 m để kéo một thùng hàng nặng P = 600 N lên sàn xe tải cao h = 1 m. Nếu bỏ qua ma sát thì lực kéo F song song với mặt phẳng nghiêng có độ lớn bằng:",
        ["600 N", "300 N", "150 N", "2 400 N"],
        2,
        "Một động cơ ô tô có công suất không đổi P = 45 kW đang kéo xe chạy thẳng đều trên đường ngang với tốc độ 54 km/h. Hãy tính độ lớn của lực kéo do động cơ tạo ra.",
        "Đổi P = 45 kW = 45 000 W và tốc độ v = 54 km/h = 54 : 3,6 = 15 (m/s). Từ công thức P = F · v, suy ra độ lớn lực kéo của động cơ là: F = P / v = 45 000 / 15 = 3 000 (N).",
        game_title="Thử thách thực tế: Công và công suất",
        game_description="Chọn công suất động cơ & hệ ròng rọc → nâng vật → so sánh thời gian và hiệu suất.",
    ),
    P(
        8,
        "nhiet-nang",
        "Năng lượng nhiệt (Nội năng) & Ba hình thức truyền nhiệt (Dẫn nhiệt - Đối lưu - Bức xạ nhiệt)",
        "🔥",
        "Hiểu nội năng - nhiệt năng, ba hình thức truyền nhiệt và công thức tính nhiệt lượng Q = m·c·Δt cùng phương trình cân bằng nhiệt.",
        "Năng lượng nhiệt (nhiệt năng) của vật là tổng động năng của các phân tử cấu tạo nên vật. Phần nhiệt năng mà vật nhận thêm hay mất bớt đi trong quá trình truyền nhiệt gọi là nhiệt lượng (Q, đơn vị Joule - J).",
        "• Hai cách làm biến đổi nhiệt năng (nội năng) của vật: Thực hiện công (cọ xát đồng xu) hoặc Truyền nhiệt (nhúng vào nước nóng).\n"
        "• Ba hình thức truyền nhiệt:\n"
        "  1. Dẫn nhiệt: hình thức truyền nhiệt chủ yếu của CHẤT RẮN (Kim loại dẫn nhiệt rất tốt; len, gỗ, xốp, không khí dẫn nhiệt rất kém).\n"
        "  2. Đối lưu: truyền nhiệt bằng các dòng chất lỏng hoặc chất khí dịch chuyển (chủ yếu ở CHẤT LỎNG và CHẤT KHÍ; không xảy ra trong chất rắn và chân không).\n"
        "  3. Bức xạ nhiệt: truyền nhiệt bằng các tia nhiệt đi thẳng (truyền được cả trong CHÂN KHÔNG; vật có bề mặt sẫm màu và xù xì hấp thụ tia nhiệt tốt hơn vật sáng màu, nhẵn bóng).\n"
        "• Công thức tính nhiệt lượng thu vào/tỏa ra và Phương trình cân bằng nhiệt.",
        [
            {
                "category": "I. Ba hình thức Truyền nhiệt theo môi trường",
                "items": [
                    {"name": "Dẫn nhiệt, Đối lưu & Bức xạ nhiệt", "formula": "Chất rắn: Dẫn nhiệt ; Chất lỏng & khí: Đối lưu ; Chân không: Chỉ có Bức xạ nhiệt", "note": ""},
                ],
            },
            {
                "category": "II. Công thức tính Nhiệt lượng & Phương trình Cân bằng nhiệt",
                "items": [
                    {"name": "Nhiệt lượng thu vào / tỏa ra khi thay đổi nhiệt độ", "formula": "Q = m · c · Δt = m · c · |t₂ − t₁|", "note": "m (kg) ; c: nhiệt dung riêng (J/(kg·K), với nước c ≈ 4200 J/(kg·K)) ; Δt (°C hoặc K)"},
                    {"name": "Phương trình cân bằng nhiệt (Bỏ qua hao phí)", "formula": "Q_tỏa = Q_thu  ⇔  m₁ · c₁ · (t₁ − t) = m₂ · c₂ · (t − t₂)", "note": "t là nhiệt độ cân bằng cuối cùng (t₂ < t < t₁)"},
                ],
            },
        ],
        "Ứng dụng trong thiết kế bình giữ nhiệt chân không (ngăn cả dẫn nhiệt, đối lưu và bức xạ), lắp điều hòa ở trên cao và đun nước từ dưới đáy ấm.",
        "Thiết kế cấu trúc bình giữ nhiệt nhiều lớp để giữ đồ uống nóng lâu nhất.",
        "Tính nhiệt lượng cần truyền cho 2 lít nước (khối lượng m = 2 kg) để đun nóng nước từ 25°C lên đến khi sôi ở 100°C. Biết nhiệt dung riêng của nước là c = 4 200 J/(kg·K).",
        "Độ tăng nhiệt độ là: Δt = 100 − 25 = 75 (°C). Nhiệt lượng cần truyền cho nước là: Q = m · c · Δt = 2 · 4200 · 75 = 630 000 (J) = 630 (kJ).",
        "Vì sao khi lắp đặt máy điều hòa làm lạnh trong phòng người ta thường lắp ở trên cao, còn lò sưởi lại đặt ở dưới thấp?",
        [
            "Để tiết kiệm diện tích tường phòng",
            "Để tạo ra dòng đối lưu tự nhiên: không khí lạnh nặng hơn chìm xuống dưới, không khí nóng nhẹ hơn bốc lên trên giúp làm mát/sưởi ấm đều cả phòng",
            "Vì không khí dẫn nhiệt tốt hơn kim loại",
            "Để tăng bức xạ nhiệt trong chân không",
        ],
        1,
        "Thả một quả cầu bằng đồng có khối lượng m₁ = 0,5 kg đã được nung nóng tới t₁ = 120°C vào một bình chứa m₂ = 0,5 kg nước ở nhiệt độ t₂ = 20°C. Biết nhiệt dung riêng của đồng là c₁ = 380 J/(kg·K) và của nước là c₂ = 4 200 J/(kg·K). Bỏ qua sự trao đổi nhiệt với bình và môi trường. Tính nhiệt độ cân bằng t của hệ.",
        "Áp dụng phương trình cân bằng nhiệt Q_tỏa = Q_thu: m₁c₁(t₁ − t) = m₂c₂(t − t₂) ⇔ 0,5 · 380 · (120 − t) = 0,5 · 4200 · (t − 20) ⇔ 38(120 − t) = 420(t − 20) ⇔ 4560 − 38t = 420t − 8400 ⇔ 458t = 12 960 ⇒ t ≈ 28,3°C.",
        game_title="Thử thách thực tế: Nhiệt năng và truyền nhiệt",
        game_description="Chọn vật liệu cách nhiệt → mô phỏng truyền nhiệt → so sánh nhiệt độ theo thời gian.",
    ),
    P(
        8,
        "dien",
        "Sự nhiễm điện do cọ xát, Dòng điện - Mạch điện & Các tác dụng của Dòng điện",
        "⚡",
        "Hiểu tương tác giữa hai loại điện tích (+/−), chiều dòng điện quy ước, cách mắc Ampe kế - Vôn kế và 5 tác dụng của dòng điện.",
        "Có hai loại điện tích là điện tích dương (+) và điện tích âm (−). Dòng điện là dòng chuyển dời có hướng của các hạt mang điện; trong kim loại, dòng điện là dòng các electron tự do dịch chuyển có hướng.",
        "• Tương tác tĩnh điện: Hai vật nhiễm điện cùng loại thì đẩy nhau, khác loại thì hút nhau. Vật nhận thêm electron thì nhiễm điện âm (−), vật mất bớt electron thì nhiễm điện dương (+).\n"
        "• Chiều dòng điện theo quy ước: là chiều từ cực dương (+) qua dây dẫn và các thiết bị điện tới cực âm (−) của nguồn điện (ngược với chiều chuyển động của electron tự do!).\n"
        "• Cường độ dòng điện I (đơn vị Ampe - A, đo bằng Ampe kế mắc NỐI TIẾP) và Hiệu điện thế U (đơn vị Vôn - V, đo bằng Vôn kế mắc SONG SONG).\n"
        "• Năm tác dụng của dòng điện: Tác dụng nhiệt, tác dụng phát sáng, tác dụng từ, tác dụng hóa học (mạ điện) và tác dụng sinh lý.",
        [
            {
                "category": "I. Cường độ dòng điện (I) & Hiệu điện thế (U)",
                "items": [
                    {"name": "Đơn vị Cường độ dòng điện I (Ampe - A)", "formula": "1 A = 1 000 mA (mi-li-ampe)  ;  1 mA = 0,001 A", "note": "Đo bằng Ampe kế mắc NỐI TIẾP với vật cần đo"},
                    {"name": "Đơn vị Hiệu điện thế U (Vôn - V)", "formula": "1 kV = 1 000 V  ;  1 V = 1 000 mV (mi-li-vôn)", "note": "Đo bằng Vôn kế mắc SONG SONG vào hai đầu vật cần đo"},
                ],
            },
            {
                "category": "II. Mạch điện hai bóng đèn & Cầu chì - Rơle bảo vệ",
                "items": [
                    {"name": "Cầu chì / Aptomat bảo vệ", "formula": "Hoạt động dựa trên TÁC DỤNG NHIỆT (hoặc tác dụng từ) để tự ngắt mạch khi đoản mạch / quá tải", "note": ""},
                    {"name": "Mạ điện (vàng, bạc, crom)", "formula": "Ứng dụng TÁC DỤNG HÓA HỌC của dòng điện đi qua dung dịch muối kim loại", "note": "Vật cần mạ nối với cực âm (−)"},
                ],
            },
        ],
        "Giúp đọc và vẽ sơ đồ mạch điện, sử dụng đồng hồ đo điện đúng quy tắc và phòng chống tai nạn điện giật.",
        "Lắp mạch đèn đơn giản trên bảng mạch mô phỏng, dùng Ampe kế - Vôn kế tìm điểm đứt mạch.",
        "Một học sinh muốn đo cường độ dòng điện chạy qua bóng đèn và hiệu điện thế giữa hai đầu bóng đèn đó. Hãy nêu cách mắc Ampe kế, Vôn kế và cách nối chốt (+) của hai dụng cụ này.",
        "Mắc Ampe kế NỐI TIẾP với bóng đèn; mắc Vôn kế SONG SONG với hai đầu bóng đèn. Chốt dương (+) của cả Ampe kế và Vôn kế đều phải được nối về phía cực dương (+) của nguồn điện.",
        "Trong dây dẫn kim loại, hạt mang điện nào dịch chuyển có hướng tạo thành dòng điện và chiều dịch chuyển của chúng như thế nào so với chiều dòng điện quy ước?",
        [
            "Các hạt nhân nguyên tử dịch chuyển cùng chiều dòng điện quy ước",
            "Các electron tự do dịch chuyển NGƯỢC chiều dòng điện quy ước (từ cực âm sang cực dương)",
            "Các electron tự do dịch chuyển CÙNG chiều dòng điện quy ước",
            "Các ion dương dịch chuyển từ cực dương sang cực âm",
        ],
        1,
        "Tại sao vào những ngày mùa đông hanh khô, khi cởi áo len hoặc dùng lược nhựa chải tóc khô, ta thường nghe thấy tiếng nổ lách tách nhỏ và tóc bị lược nhựa hút dựng đứng lên?",
        "Do khi cọ xát với tóc, lược nhựa và áo len bị nhiễm điện (tĩnh điện). Giữa các phần nhiễm điện trái dấu xuất hiện lực hút tĩnh điện làm tóc bị hút về phía lược, đồng thời sự phóng điện nhỏ qua không khí khô gây ra tiếng nổ lách tách.",
        game_title="Thử thách thực tế: Điện và mạch điện",
        game_description="Nối mạch → mắc Ampe kế & Vôn kế → bật nguồn → chẩn đoán và sửa lỗi mạch.",
    ),

    # =========================================================
    # VẬT LÝ LỚP 9 (7 BÀI)
    # =========================================================
    P(
        9,
        "co-nang-khuc-xa-anh-sang",
        "Động năng - Thế năng - Cơ năng & Khúc xạ ánh sáng - Phản xạ toàn phần - Lăng kính",
        "💎",
        "Tính động năng W_đ = ½mv², thế năng W_t = Ph, bảo toàn cơ năng và định luật khúc xạ ánh sáng n₁sin i = n₂sin r, phản xạ toàn phần.",
        "Cơ năng của vật bằng tổng động năng và thế năng của nó: W = W_đ + W_t. Khúc xạ ánh sáng là hiện tượng tia sáng truyền từ môi trường trong suốt này sang môi trường trong suốt khác bị gãy khúc tại mặt phân cách giữa hai môi trường.",
        "• Động năng W_đ = (1/2)mv² (phụ thuộc khối lượng m và tốc độ v) và Thế năng trọng trường W_t = P·h = m·g·h (phụ thuộc khối lượng và độ cao h so với mốc thế năng).\n"
        "• Chiết suất của môi trường n = c / v (với c = 3·10⁸ m/s) và Định luật khúc xạ ánh sáng: n₁ · sin i = n₂ · sin r.\n"
        "• Hiện tượng Phản xạ toàn phần (ứng dụng trong Cáp quang Internet): chỉ xảy ra khi ánh sáng truyền từ môi trường chiết광 hơn sang môi trường chiết quang kém (n₁ > n₂) và góc tới lớn hơn hoặc bằng góc giới hạn (i ≥ i_gh với sin i_gh = n₂ / n₁).",
        [
            {
                "category": "I. Động năng, Thế năng & Bảo toàn Cơ năng",
                "items": [
                    {"name": "Động năng W_đ & Thế năng trọng trường W_t", "formula": "W_đ = (1/2) · m · v²  ;  W_t = P · h = m · g · h", "note": "m (kg), v (m/s), h (m), W (J)"},
                    {"name": "Cơ năng & Định luật bảo toàn cơ năng", "formula": "W = W_đ + W_t = (1/2)mv² + mgh = hằng số (khi bỏ qua ma sát/lực cản)", "note": "Vật rơi từ độ cao H không vận tốc đầu: v_chạm_đất = √(2gH)"},
                ],
            },
            {
                "category": "II. Khúc xạ ánh sáng & Phản xạ toàn phần",
                "items": [
                    {"name": "Chiết suất tuyệt đối n & Định luật Khúc xạ", "formula": "n = c / v (n ≥ 1)  ;  n₁ · sin i = n₂ · sin r  ⇔  sin i / sin r = n₂ / n₁", "note": "Nếu n₂ > n₁ thì r < i ; nếu n₂ < n₁ thì r > i"},
                    {"name": "Điều kiện Phản xạ toàn phần", "formula": "1) n₁ > n₂  và  2) i ≥ i_gh  với  sin i_gh = n₂ / n₁", "note": "Toàn bộ tia sáng bị phản xạ ngược lại môi trường 1"},
                ],
            },
        ],
        "Giải thích chuyển động của tàu lượn siêu tốc, nhà máy thủy điện, ảo ảnh trên mặt đường nhựa nóng và cáp quang truyền dữ liệu tốc độ cao.",
        "Thiết kế đường trượt tàu lượn siêu tốc (Roller Coaster) và dẫn truyền tia sáng trong sợi cáp quang.",
        "Một vật có khối lượng m = 0,5 kg được thả rơi tự do không vận tốc đầu từ độ cao h = 20 m xuống mặt đất (lấy g = 10 m/s², bỏ qua sức cản không khí). Tính cơ năng của vật, tốc độ của vật khi chạm đất và độ cao nơi có động năng bằng 3 lần thế năng.",
        "Chọn gốc thế năng tại mặt đất. Cơ năng ban đầu bằng thế năng cực đại: W = mgh = 0,5 · 10 · 20 = 100 (J). Khi chạm đất (W_t = 0): W_đ = (1/2)mv² = 100 ⇒ v = √(2·100 / 0,5) = 20 (m/s). Tại nơi W_đ = 3W_t ⇒ W = W_đ + W_t = 4W_t = 100 ⇒ W_t = 25 (J) ⇔ mgh' = 25 ⇒ h' = 25 / (0,5 · 10) = 5 (m).",
        "Chiếu một tia sáng từ không khí (n₁ ≈ 1) vào mặt nước (n₂ = 4/3) dưới góc tới i = 60°. Giá trị của sin góc khúc xạ (sin r) bằng:",
        ["(3√3) / 8", "(2√3) / 3", "3 / 8", "√3 / 4"],
        0,
        "Tính góc giới hạn phản xạ toàn phần i_gh khi chiếu tia sáng từ thủy tinh có chiết suất n₁ = 1,5 ra ngoài không khí (n₂ = 1). Nếu chiếu tia sáng từ trong khối thủy tinh tới mặt phân cách với góc tới i = 45° thì có tia khúc xạ ló ra ngoài không khí hay không?",
        "Ta có sin i_gh = n₂ / n₁ = 1 / 1,5 = 2/3 ≈ 0,667 ⇒ i_gh ≈ 41,8°. Vì tia sáng truyền từ thủy tinh (n₁ = 1,5) ra không khí (n₂ = 1) có n₁ > n₂ và góc tới i = 45° > i_gh (41,8°), nên xảy ra hiện tượng PHẢN XẠ TOÀN PHẦN: không có tia khúc xạ nào ló ra ngoài không khí.",
        game_title="Thử thách thực tế: Cơ năng & Khúc xạ cáp quang",
        game_description="Mô phỏng bảo toàn cơ năng con lắc / tàu lượn và điều chỉnh góc tới tia laser trong sợi quang.",
    ),
    P(
        9,
        "dien-tro",
        "Điện trở dây dẫn, Định luật Ohm & Sự phụ thuộc của Điện trở vào kích thước - vật liệu",
        "Ω",
        "Vận dụng định luật Ohm I = U/R và công thức tính điện trở dây dẫn R = ρ·l/S cùng biến trở.",
        "Điện trở (R, đơn vị Ohm - Ω) biểu thị mức độ cản trở dòng điện nhiều hay ít của dây dẫn. Định luật Ohm phát biểu: Cường độ dòng điện chạy qua một dây dẫn tỉ lệ thuận với hiệu điện thế đặt vào hai đầu dây và tỉ lệ nghịch với điện trở của dây dẫn đó.",
        "• Định luật Ohm: I = U / R (Lưu ý: R là thuộc tính của bản thân vật dẫn, R KHÔNG phụ thuộc vào U và I; công thức R = U / I chỉ dùng để tính giá trị của R).\n"
        "• Đồ thị biểu diễn sự phụ thuộc của I vào U (khi nhiệt độ không đổi) là một đường thẳng đi qua gốc tọa độ O(0; 0).\n"
        "• Công thức phụ thuộc của điện trở vào chiều dài l, tiết diện S và điện trở suất ρ của vật liệu: R = ρ · l / S.\n"
        "• Biến trở (con chạy, tay quay, chiết áp): thay đổi chiều dài phần dây dẫn có dòng điện chạy qua để điều chỉnh cường độ dòng điện trong mạch.",
        [
            {
                "category": "I. Định luật Ohm cho đoạn mạch",
                "items": [
                    {"name": "Hệ thức Định luật Ohm", "formula": "I = U / R  ⇒  U = I · R  ;  R = U / I", "note": "I (A), U (V), R (Ω) ; 1 kΩ = 10³ Ω ; 1 MΩ = 10⁶ Ω"},
                ],
            },
            {
                "category": "II. Điện trở phụ thuộc vào Chiều dài l, Tiết diện S và Điện trở suất ρ",
                "items": [
                    {"name": "Công thức tính điện trở dây dẫn", "formula": "R = ρ · (l / S)", "note": "ρ: điện trở suất (Ω·m) ; l: chiều dài (m) ; S: tiết diện ngang (m²)"},
                    {"name": "Tiết diện dây dẫn hình trụ tròn (đường kính d, bán kính r)", "formula": "S = π · r² = (π · d²) / 4  ;  1 mm² = 10⁻⁶ m²", "note": "Đường kính tăng gấp đôi ⇒ tiết diện S tăng gấp 4 ⇒ điện trở R giảm 4 lần"},
                ],
            },
        ],
        "Giúp tính toán chọn tiết diện dây cáp điện trong nhà, chế tạo biến trở điều chỉnh âm lượng/độ sáng đèn và thiết kế dây đốt nóng.",
        "Chọn điện trở hạn dòng phù hợp để bảo vệ bóng đèn LED khỏi bị cháy do quá dòng.",
        "Một cuộn dây đồng có chiều dài l = 100 m và tiết diện S = 2 mm². Biết điện trở suất của đồng là ρ = 1,7 · 10⁻⁸ Ω·m. Tính điện trở của cuộn dây và cường độ dòng điện chạy qua nó khi đặt vào hai đầu cuộn dây hiệu điện thế U = 3,4 V.",
        "Đổi S = 2 mm² = 2 · 10⁻⁶ m². Điện trở cuộn dây là: R = ρ · l / S = (1,7 · 10⁻⁸ · 100) / (2 · 10⁻⁶) = 0,85 (Ω). Cường độ dòng điện qua cuộn dây là: I = U / R = 3,4 / 0,85 = 4 (A).",
        "Hai dây dẫn bằng đồng có cùng chiều dài. Dây thứ nhất có đường kính tiết diện d₁ = 1 mm, dây thứ hai có đường kính tiết diện d₂ = 2 mm. Tỉ số điện trở R₁ / R₂ của hai dây là:",
        ["R₁ / R₂ = 2", "R₁ / R₂ = 4", "R₁ / R₂ = 1/2", "R₁ / R₂ = 1/4"],
        1,
        "Một bóng đèn LED có hiệu điện thế định mức U_Đ = 3 V và dòng điện định mức I_Đ = 0,02 A (20 mA). Muốn mắc bóng đèn LED này vào nguồn điện U = 9 V để đèn sáng bình thường thì phải mắc nối tiếp với đèn một điện trở bảo vệ R có giá trị bằng bao nhiêu Ohm?",
        "Để đèn sáng bình thường thì hiệu điện thế trên điện trở bảo vệ phải là: U_R = U − U_Đ = 9 − 3 = 6 (V), và dòng điện qua R bằng dòng định mức của đèn: I_R = I_Đ = 0,02 (A). Vậy giá trị điện trở cần mắc là: R = U_R / I_R = 6 / 0,02 = 300 (Ω).",
        game_title="Thử thách thực tế: Điện trở và định luật Ohm",
        game_description="Chọn R → cấp U → quan sát I → bảo vệ LED hoạt động đúng định mức.",
    ),
    P(
        9,
        "doan-mach-noi-tiep",
        "Đoạn mạch nối tiếp & Quy tắc Phân áp",
        "🔗",
        "Nắm vững tính chất dòng điện, hiệu điện thế, điện trở tương đương R_tđ = R₁ + R₂ và công thức chia áp trong đoạn mạch nối tiếp.",
        "Đoạn mạch nối tiếp gồm các điện trở (hoặc thiết bị điện) được mắc liên tiếp nhau thành một dãy duy nhất không có điểm rẽ nhánh.",
        "• Cường độ dòng điện có giá trị như nhau tại mọi điểm trên đoạn mạch nối tiếp: I = I₁ = I₂ = ... = Iₙ.\n"
        "• Hiệu điện thế giữa hai đầu đoạn mạch nối tiếp bằng tổng các hiệu điện thế trên mỗi điện trở thành phần: U = U₁ + U₂ + ... + Uₙ.\n"
        "• Điện trở tương đương của đoạn mạch nối tiếp bằng tổng các điện trở thành phần: R_tđ = R₁ + R₂ + ... + Rₙ (luôn lớn hơn mỗi điện trở thành phần).\n"
        "• Quy tắc phân áp: Hiệu điện thế giữa hai đầu mỗi điện trở tỉ lệ thuận với giá trị điện trở đó: U₁ / U₂ = R₁ / R₂.",
        [
            {
                "category": "I. Hệ thức cơ bản của Đoạn mạch nối tiếp",
                "items": [
                    {"name": "Cường độ dòng điện & Hiệu điện thế", "formula": "I = I₁ = I₂ = ... = Iₙ  ;  U = U₁ + U₂ + ... + Uₙ", "note": ""},
                    {"name": "Điện trở tương đương R_tđ", "formula": "R_tđ = R₁ + R₂ + ... + Rₙ", "note": "Nếu mắc n điện trở giống nhau R₀ nối tiếp: R_tđ = n · R₀"},
                ],
            },
            {
                "category": "II. Quy tắc Phân áp (Chia điện áp)",
                "items": [
                    {"name": "Tỉ lệ hiệu điện thế", "formula": "U₁ / U₂ = R₁ / R₂", "note": "Điện trở càng lớn thì chiếm hiệu điện thế càng lớn"},
                    {"name": "Công thức tính nhanh U₁, U₂ theo U toàn mạch", "formula": "U₁ = U · R₁ / (R₁ + R₂)  ;  U₂ = U · R₂ / (R₁ + R₂)", "note": "Cầu phân áp trong mạch cảm biến điện tử"},
                ],
            },
        ],
        "Ứng dụng trong mạch cầu phân áp cho cảm biến nhiệt độ/ánh sáng, điện trở hạn dòng và dây đèn trang trí.",
        "Thiết kế cầu phân áp và chuỗi đèn nối tiếp sao cho các bóng hoạt động an toàn.",
        "Cho hai điện trở R₁ = 15 Ω và R₂ = 25 Ω mắc nối tiếp nhau vào nguồn điện có hiệu điện thế U = 12 V. Tính điện trở tương đương của đoạn mạch, cường độ dòng điện trong mạch và hiệu điện thế giữa hai đầu mỗi điện trở.",
        "Điện trở tương đương: R_tđ = R₁ + R₂ = 15 + 25 = 40 (Ω). Cường độ dòng điện: I = U / R_tđ = 12 / 40 = 0,3 (A). Hiệu điện thế trên mỗi điện trở: U₁ = I · R₁ = 0,3 · 15 = 4,5 (V) và U₂ = I · R₂ = 0,3 · 25 = 7,5 (V).",
        "Hai điện trở R₁ và R₂ = 3R₁ được mắc nối tiếp vào hiệu điện thế U = 20 V. Hiệu điện thế U₂ giữa hai đầu điện trở R₂ là:",
        ["5 V", "10 V", "15 V", "20 V"],
        2,
        "Cho hai điện trở R₁ = 20 Ω (chịu được dòng điện tối đa I₁_max = 1,5 A) và R₂ = 30 Ω (chịu được dòng điện tối đa I₂_max = 0,8 A). Nếu mắc nối tiếp hai điện trở này với nhau thì hiệu điện thế tối đa U_max có thể đặt vào hai đầu đoạn mạch để không điện trở nào bị hỏng là bao nhiêu?",
        "Khi mắc nối tiếp, cả hai điện trở có cùng dòng điện I chạy qua, nên dòng điện tối đa cho phép của cả mạch phải lấy theo giá trị nhỏ hơn: I_max = min(1,5 A ; 0,8 A) = 0,8 (A). Khi đó U_max = I_max · (R₁ + R₂) = 0,8 · (20 + 30) = 40 (V).",
        game_title="Thử thách thực tế: Đoạn mạch nối tiếp",
        game_description="Chọn điện trở → mắc nối tiếp → đo U và I theo quy tắc phân áp.",
    ),
    P(
        9,
        "doan-mach-song-song",
        "Đoạn mạch song song, Quy tắc Phân dòng & Mạch điện hỗn hợp",
        "🔀",
        "Nắm vững tính chất đoạn mạch song song (U = U₁ = U₂, I = I₁ + I₂, 1/R_tđ = 1/R₁ + 1/R₂) và giải bài toán mạch điện hỗn hợp.",
        "Trong đoạn mạch song song, hai đầu của các nhánh điện trở được nối chung vào hai điểm nút; các thiết bị trên mỗi nhánh hoạt động độc lập dưới cùng một hiệu điện thế.",
        "• Hiệu điện thế giữa hai đầu các nhánh mắc song song luôn bằng nhau: U = U₁ = U₂ = ... = Uₙ.\n"
        "• Cường độ dòng điện mạch chính bằng tổng cường độ dòng điện chạy qua các mạch rẽ: I = I₁ + I₂ + ... + Iₙ.\n"
        "• Nghịch đảo điện trở tương đương bằng tổng các nghịch đảo điện trở thành phần: 1/R_tđ = 1/R₁ + 1/R₂ + ... + 1/Rₙ (R_tđ luôn nhỏ hơn điện trở thành phần nhỏ nhất!).\n"
        "• Quy tắc phân dòng: Cường độ dòng điện qua mỗi nhánh tỉ lệ nghịch với điện trở của nhánh đó: I₁ / I₂ = R₂ / R₁.",
        [
            {
                "category": "I. Hệ thức cơ bản của Đoạn mạch song song",
                "items": [
                    {"name": "Hiệu điện thế & Cường độ dòng điện", "formula": "U = U₁ = U₂ = ... = Uₙ  ;  I = I₁ + I₂ + ... + Iₙ", "note": ""},
                    {"name": "Điện trở tương đương (Tổng quát & 2 điện trở)", "formula": "1/R_tđ = 1/R₁ + 1/R₂ + ... + 1/Rₙ  ;  Với 2 điện trở: R_tđ = (R₁ · R₂) / (R₁ + R₂)", "note": "Tích trên tổng ; n điện trở R₀ giống nhau song song: R_tđ = R₀ / n"},
                ],
            },
            {
                "category": "II. Quy tắc Phân dòng (Chia dòng điện)",
                "items": [
                    {"name": "Tỉ lệ cường độ dòng điện hai nhánh", "formula": "I₁ / I₂ = R₂ / R₁", "note": "Nhánh có điện trở càng nhỏ thì dòng điện đi qua càng lớn"},
                    {"name": "Tính dòng nhánh theo dòng chính I", "formula": "I₁ = I · R₂ / (R₁ + R₂)  ;  I₂ = I · R₁ / (R₁ + R₂)", "note": ""},
                ],
            },
        ],
        "Tất cả các thiết bị điện trong gia đình (đèn, quạt, tivi, tủ lạnh) đều được mắc song song vào mạng điện 220 V để có cùng điện áp định mức và bật/tắt độc lập.",
        "Mô phỏng hệ thống điện căn hộ sao cho khi tắt một thiết bị các thiết bị khác vẫn hoạt động bình thường.",
        "Cho mạch điện hỗn hợp gồm R₁ = 8 Ω mắc nối tiếp với cụm (R₂ // R₃), trong đó R₂ = 30 Ω và R₃ = 20 Ω. Đặt vào hai đầu cả đoạn mạch hiệu điện thế U = 40 V. Tính điện trở tương đương của cả mạch, dòng điện chính I và dòng điện qua R₂, R₃.",
        "Điện trở cụm song song: R₂₃ = (R₂ · R₃) / (R₂ + R₃) = (30 · 20) / (30 + 20) = 12 (Ω). Điện trở tương đương toàn mạch: R_tđ = R₁ + R₂₃ = 8 + 12 = 20 (Ω). Dòng điện mạch chính: I = U / R_tđ = 40 / 20 = 2 (A). Hiệu điện thế trên cụm song song: U₂₃ = I · R₂₃ = 2 · 12 = 24 (V). Suy ra: I₂ = U₂₃ / R₂ = 24 / 30 = 0,8 (A) và I₃ = U₂₃ / R₃ = 24 / 20 = 1,2 (A).",
        "Ba điện trở giống hệt nhau có cùng giá trị R = 18 Ω được mắc song song với nhau. Điện trở tương đương của đoạn mạch đó bằng:",
        ["54 Ω", "18 Ω", "9 Ω", "6 Ω"],
        3,
        "Cho hai điện trở R₁ = 10 Ω (chịu được dòng điện tối đa I₁_max = 1,5 A) và R₂ = 20 Ω (chịu được dòng điện tối đa I₂_max = 1,0 A) mắc song song với nhau. Hỏi hiệu điện thế tối đa U_max có thể đặt vào hai đầu đoạn mạch song song này để không điện trở nào bị cháy là bao nhiêu?",
        "Hiệu điện thế tối đa mà R₁ chịu được là: U₁_max = I₁_max · R₁ = 1,5 · 10 = 15 (V). Hiệu điện thế tối đa mà R₂ chịu được là: U₂_max = I₂_max · R₂ = 1,0 · 20 = 20 (V). Vì hai điện trở mắc song song chịu cùng một hiệu điện thế U, nên U_max = min(15 V ; 20 V) = 15 (V).",
        game_title="Thử thách thực tế: Đoạn mạch song song",
        game_description="Mở/tắt từng nhánh → theo dõi phân dòng I → thiết kế mạng điện gia đình an toàn.",
    ),
    P(
        9,
        "cong-va-cong-suat-dien",
        "Công suất điện, Điện năng tiêu thụ & Định luật Joule-Lenz",
        "💡",
        "Tính công suất điện P = U·I = I²R = U²/R, điện năng tiêu thụ A = P·t (số đếm công tơ kWh) và nhiệt lượng tỏa ra Q = I²Rt.",
        "Công suất điện của một đoạn mạch bằng tích của hiệu điện thế giữa hai đầu đoạn mạch và cường độ dòng điện chạy qua nó (P = U·I), cho biết lượng điện năng mà đoạn mạch tiêu thụ trong một đơn vị thời gian.",
        "• Công thức công suất điện: P = U · I = I² · R = U² / R (đơn vị Watt - W). Số ghi trên dụng cụ điện (ví dụ: 220V – 1000W) cho biết hiệu điện thế định mức và công suất định mức.\n"
        "• Công của dòng điện (điện năng tiêu thụ): A = P · t = U · I · t (đơn vị Joule - J hoặc ki-lô-oát giờ - kWh). Trên công tơ điện: 1 số điện = 1 kWh = 3 600 000 J = 3,6 · 10⁶ J.\n"
        "• Định luật Joule-Lenz: Nhiệt lượng tỏa ra ở dây dẫn có điện trở R khi có dòng điện chạy qua là Q = I² · R · t.",
        [
            {
                "category": "I. Công suất điện (P) & Điện trở định mức của thiết bị",
                "items": [
                    {"name": "Ba công thức tính Công suất điện", "formula": "P = U · I = I² · R = U² / R", "note": "P (W), U (V), I (A), R (Ω)"},
                    {"name": "Điện trở & Dòng định mức từ nhãn (U_đm - P_đm)", "formula": "R = U_đm² / P_đm  ;  I_đm = P_đm / U_đm", "note": "Khi dùng ở điện áp U < U_đm thì công suất thực tế là P = (U / U_đm)² · P_đm"},
                ],
            },
            {
                "category": "II. Điện năng tiêu thụ (A), Công tơ điện & Định luật Joule-Lenz",
                "items": [
                    {"name": "Điện năng tiêu thụ & Số đếm công tơ điện", "formula": "A = P · t = U · I · t  ;  1 số điện = 1 kWh = 1 000 W · 3 600 s = 3 600 000 J", "note": "Nếu P tính bằng kW và t tính bằng giờ (h) thì A = P · t (kWh)"},
                    {"name": "Định luật Joule-Lenz (Nhiệt lượng tỏa ra)", "formula": "Q = I² · R · t  (Joule - J)", "note": "Hiệu suất ấm đun nước: H = (Q_thu_của_nước / A_điện) × 100%"},
                ],
            },
        ],
        "Giúp tính hóa đơn tiền điện hàng tháng của gia đình, tính thời gian đun sôi nước của ấm siêu tốc và chọn dây dẫn không bị nóng chảy.",
        "Quản lý các thiết bị điện trong căn hộ thông minh để giảm hóa đơn tiền điện và tránh nhảy Aptomat.",
        "Một ấm đun nước siêu tốc có ghi 220V – 1500W được sử dụng ở hiệu điện thế đúng 220 V để đun sôi 2 lít nước từ 20°C lên 100°C. Biết hiệu suất của ấm là H = 80% và nhiệt dung riêng của nước là c = 4 200 J/(kg·K). Tính thời gian đun sôi nước và điện năng tiêu thụ theo kWh.",
        "Nhiệt lượng có ích để đun sôi 2 kg nước: Q_ích = m · c · Δt = 2 · 4200 · (100 − 20) = 672 000 (J). Điện năng toàn phần ấm tiêu thụ: A = Q_ích / H = 672 000 / 0,8 = 840 000 (J). Thời gian đun sôi nước: t = A / P = 840 000 / 1500 = 560 (giây) = 9 phút 20 giây. Đổi ra số điện: A = 840 000 / 3 600 000 ≈ 0,233 (kWh).",
        "Một gia đình sử dụng một máy điều hòa có công suất tiêu thụ trung bình 1 000 W (1 kW) trong 6 giờ mỗi ngày. Trong 1 tháng (30 ngày), riêng máy điều hòa này tiêu thụ bao nhiêu 'số điện' (kWh)?",
        ["6 kWh", "30 kWh", "180 kWh", "1 800 kWh"],
        2,
        "Hai bóng đèn sợi đốt có ghi Đ₁(220V – 100W) và Đ₂(220V – 40W). Tính điện trở R₁, R₂ của hai đèn (giả sử không đổi). Nếu đem mắc NỐI TIẾP hai bóng đèn này vào mạng điện U = 220 V thì đèn nào sẽ sáng mạnh hơn? Vì sao?",
        "Ta có: R₁ = 220² / 100 = 484 (Ω) và R₂ = 220² / 40 = 1 210 (Ω) (đèn công suất định mức nhỏ hơn lại có điện trở lớn hơn!). Khi mắc NỐI TIẾP hai đèn vào 220 V, chúng có cùng cường độ dòng điện I chạy qua. Vì công suất thực tế là P = I² · R mà R₂ > R₁ (1210 > 484) nên P₂ > P₁: bóng đèn Đ₂ (40W) sẽ sáng mạnh hơn bóng đèn Đ₁ (100W)!",
        game_title="Thử thách thực tế: Công và công suất điện",
        game_description="Bật/tắt thiết bị → theo dõi công suất tổng và công tơ kWh → tối ưu lịch sử dụng điện.",
    ),
    P(
        9,
        "dien-tu",
        "Cảm ứng điện từ, Dòng điện xoay chiều, Máy biến áp & Truyền tải điện năng đi xa",
        "🧲",
        "Hiểu hiện tượng cảm ứng điện từ, điều kiện xuất hiện dòng điện cảm ứng, công thức máy biến áp và hao phí truyền tải điện.",
        "Khi số đường sức từ xuyên qua tiết diện S của một cuộn dây dẫn kín biến thiên (tăng hoặc giảm) thì trong cuộn dây đó xuất hiện dòng điện cảm ứng. Hiện tượng đó gọi là hiện tượng cảm ứng điện từ (do Michael Faraday khám phá năm 1831).",
        "• Điều kiện xuất hiện dòng điện cảm ứng và nguyên tắc tạo ra dòng điện xoay chiều (ở Việt Nam mạng điện dân dụng có U = 220 V và tần số f = 50 Hz).\n"
        "• Tác dụng từ của dòng điện xoay chiều đổi chiều liên tục dẫn đến nguyên lý cấu tạo của Máy biến áp (gồm cuộn sơ cấp N₁ vòng, cuộn thứ cấp N₂ vòng quấn trên lõi thép kỹ thuật điện): U₁ / U₂ = N₁ / N₂.\n"
        "• Công thức tính công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện năng đi xa: P_hp = (P² · R) / U² (Tăng hiệu điện thế truyền tải U lên n lần thì công suất hao phí giảm đi n² lần!).",
        [
            {
                "category": "I. Máy biến áp (Biến thế) lý tưởng",
                "items": [
                    {"name": "Hệ thức Điện áp và Số vòng dây", "formula": "U₁ / U₂ = N₁ / N₂  ;  I₁ / I₂ = U₂ / U₁ = N₂ / N₁", "note": "N₂ > N₁ ⇒ U₂ > U₁ (Máy tăng áp) ; N₂ < N₁ ⇒ U₂ < U₁ (Máy hạ áp)"},
                    {"name": "Lưu ý quan trọng về Máy biến áp", "formula": "Máy biến áp CHỈ hoạt động với dòng điện xoay chiều (AC), KHÔNG hoạt động với dòng một chiều không đổi (DC)", "note": "Vì dòng DC không tạo ra từ trường biến thiên"},
                ],
            },
            {
                "category": "II. Truyền tải điện năng đi xa & Giảm hao phí",
                "items": [
                    {"name": "Công suất hao phí tỏa nhiệt trên đường dây", "formula": "P_hp = I² · R = (P² · R) / U²", "note": "P: công suất truyền đi (W) ; U: điện áp nơi truyền đi (V) ; R: điện trở tổng cộng của 2 dây dẫn (Ω)"},
                    {"name": "Quy luật giảm hao phí khi tăng áp", "formula": "U tăng n lần  ⇒  P_hp giảm n² lần", "note": "Ví dụ: Tăng điện áp từ 22 kV lên 220 kV (gấp 10 lần) thì hao phí giảm 100 lần!"},
                ],
            },
        ],
        "Cơ sở vận hành của toàn bộ lưới điện quốc gia (Đường dây siêu cao áp 500 kV Bắc – Nam), máy phát điện, sạc không dây và bếp từ.",
        "Điều khiển máy phát điện và trạm biến áp tăng/hạ áp để truyền tải điện năng đi xa với hao phí thấp nhất.",
        "Một máy biến áp có cuộn sơ cấp N₁ = 2 200 vòng và cuộn thứ cấp N₂ = 120 vòng. Đặt vào hai đầu cuộn sơ cấp hiệu điện thế xoay chiều U₁ = 220 V. Tính hiệu điện thế U₂ ở hai đầu cuộn thứ cấp để hở và cho biết đây là máy tăng áp hay hạ áp.",
        "Áp dụng công thức máy biến áp: U₁ / U₂ = N₁ / N₂ ⇒ U₂ = U₁ · (N₂ / N₁) = 220 · (120 / 2200) = 12 (V). Vì U₂ < U₁ (12 V < 220 V) nên đây là máy HẠ ÁP.",
        "Trên cùng một đường dây tải điện và cùng một công suất điện P cần truyền đi, nếu dùng máy biến áp để tăng hiệu điện thế ở hai đầu đường dây lên gấp 5 lần thì công suất hao phí vì tỏa nhiệt trên đường dây sẽ:",
        ["Giảm đi 5 lần", "Tăng lên 5 lần", "Giảm đi 25 lần", "Giảm đi 10 lần"],
        2,
        "Một nhà máy điện truyền tải công suất P = 1 000 kW đi xa dưới hiệu điện thế U = 10 kV trên đường dây tải điện gồm 2 dây có tổng điện trở R = 10 Ω. Hãy tính công suất hao phí P_hp do tỏa nhiệt trên đường dây và hiệu suất truyền tải điện H.",
        "Đổi P = 1000 kW = 10⁶ W và U = 10 kV = 10⁴ V. Cường độ dòng điện trên dây là: I = P / U = 10⁶ / 10⁴ = 100 (A). Công suất hao phí trên đường dây: P_hp = I² · R = 100² · 10 = 100 000 (W) = 100 (kW). Hiệu suất truyền tải là: H = [(P − P_hp) / P] × 100% = [(1000 − 100) / 1000] × 100% = 90%.",
        game_title="Thử thách thực tế: Điện từ học & Lưới điện",
        game_description="Vận hành máy phát điện → điều chỉnh tỉ số vòng dây máy biến áp → tối ưu truyền tải điện.",
    ),
    P(
        9,
        "quang-hoc",
        "Thấu kính hội tụ, Thấu kính phân kỳ, Mắt (Cận thị - Viễn thị) & Kính lúp",
        "🔍",
        "Vẽ đường truyền tia sáng đặc biệt, vận dụng công thức thấu kính (1/f = 1/d ± 1/d') và hiểu cách sửa tật cận thị, viễn thị của mắt.",
        "Thấu kính là một khối chất trong suốt (thủy tinh, nhựa quang học) giới hạn bởi hai mặt cong hoặc một mặt cong và một mặt phẳng. Có hai loại: Thấu kính hội tụ (rìa mỏng, tiêu cự f > 0) và Thấu kính phân kỳ (rìa dày, tiêu cự f < 0).",
        "• Ba đường truyền tia sáng đặc biệt qua thấu kính:\n"
        "  1. Tia tới qua quang tâm O thì truyền thẳng.\n"
        "  2. Tia tới song song với trục chính thì tia ló đi qua tiêu điểm F' (TKHT) hoặc có đường kéo dài đi qua tiêu điểm F' (TKPK).\n"
        "  3. Tia tới qua tiêu điểm F (TKHT) thì tia ló song song với trục chính.\n"
        "• Tính chất ảnh qua Thấu kính hội tụ (d > f: ảnh thật, ngược chiều; d < f: ảnh ảo, cùng chiều, lớn hơn vật) và qua Thấu kính phân kỳ (với mọi d > 0: luôn cho ảnh ảo, cùng chiều, nhỏ hơn vật và nằm trong khoảng OF).\n"
        "• Mắt (thể thủy tinh như TKHT, màng lưới như màn ảnh): Mắt cận thị đeo TKPK (với f = −OC_V); mắt viễn thị đeo TKHT; Kính lúp (TKHT có tiêu cự ngắn, số bội giác G = 25/f(cm)).",
        [
            {
                "category": "I. Công thức Thấu kính & Độ phóng đại ảnh k",
                "items": [
                    {"name": "Thấu kính hội tụ — Trường hợp ảnh thật (d > f)", "formula": "1/f = 1/d + 1/d'  ⇒  d' = (d · f) / (d − f)", "note": "f: tiêu cự ; d: khoảng cách vật đến TK ; d': khoảng cách ảnh đến TK"},
                    {"name": "Thấu kính hội tụ — Trường hợp ảnh ảo (d < f)", "formula": "1/f = 1/d − 1/d'  ⇒  d' = (d · f) / (f − d)", "note": "Ảnh ảo cùng chiều và lớn hơn vật (nguyên lý Kính lúp)"},
                    {"name": "Thấu kính phân kỳ (luôn cho ảnh ảo với mọi d > 0)", "formula": "1/f = 1/d' − 1/d  ⇒  d' = (d · f) / (d + f) (với f, d, d' lấy độ lớn dương)", "note": "Hoặc dùng công thức đại số tổng quát: 1/f = 1/d + 1/d' (TKPK có f < 0, ảnh ảo có d' < 0)"},
                    {"name": "Tỉ số chiều cao ảnh và vật (Độ phóng đại)", "formula": "h' / h = d' / d", "note": "Suy ra từ hai tam giác đồng dạng ΔOAB ∽ ΔOA'B'"},
                ],
            },
            {
                "category": "II. Mắt (Cận thị - Viễn thị) & Kính lúp",
                "items": [
                    {"name": "Sửa tật Cận thị & Viễn thị", "formula": "Mắt Cận (nhìn xa kém): đeo TK Phân kỳ (f_kính = −OC_V)  ;  Mắt Viễn (nhìn gần kém): đeo TK Hội tụ", "note": "C_V là điểm cực viễn của mắt"},
                    {"name": "Số bội giác G của Kính lúp", "formula": "G = 25 / f (trong đó tiêu cự f tính bằng cm)  ⇔  f (cm) = 25 / G", "note": "Ví dụ: Kính lúp ghi 5x có tiêu cự f = 25 / 5 = 5 cm"},
                ],
            },
        ],
        "Ứng dụng trong đo cắt kính mắt (cận, viễn, lão), ống kính máy ảnh, máy chiếu, kính lúp và kính hiển vi.",
        "Điều chỉnh tiêu cự và khoảng cách thấu kính camera để lấy nét ảnh rõ nhất trên cảm biến.",
        "Một vật sáng AB cao h = 4 cm đặt vuông góc với trục chính của một thấu kính hội tụ có tiêu cự f = 15 cm, cách thấu kính một khoảng d = 30 cm. Xác định vị trí d', tính chất và chiều cao h' của ảnh A'B'.",
        "Vì d = 30 cm > f = 15 cm nên ảnh A'B' là ảnh thật, ngược chiều với vật. Áp dụng công thức: 1/f = 1/d + 1/d' ⇒ d' = (d · f)/(d − f) = (30 · 15)/(30 − 15) = 30 (cm). Chiều cao của ảnh: h' = h · (d' / d) = 4 · (30 / 30) = 4 (cm) (Khi d = 2f thì ảnh thật cao bằng vật và d' = 2f!).",
        "Trên vành của một chiếc kính lúp có ghi ký hiệu '2,5x'. Tiêu cự f của chiếc kính lúp này là bao nhiêu?",
        ["2,5 cm", "5 cm", "10 cm", "25 cm"],
        2,
        "Một người bị cận thị chỉ có thể nhìn rõ các vật cách mắt xa nhất là 50 cm (điểm cực viễn OC_V = 50 cm). Để người này có thể nhìn rõ các vật ở rất xa (vô cực) như mắt thường mà không cần điều tiết thì phải đeo sát mắt một thấu kính loại gì và có tiêu cự bằng bao nhiêu?",
        "Người bị cận thị phải đeo THẤU KÍNH PHÂN KỲ sao cho vật ở rất xa qua kính cho ảnh ảo hiện lên đúng tại điểm cực viễn C_V của mắt. Do đó kính phân kỳ cần đeo có độ lớn tiêu cự bằng khoảng cực viễn: f = OC_V = 50 cm (hay f = −50 cm, độ tụ D = −1 / 0,5 = −2 đi-ốp).",
        game_title="Thử thách thực tế: Quang học & Thấu kính",
        game_description="Di chuyển vật và thấu kính → quan sát đường đi 3 tia sáng đặc biệt → lấy nét ảnh.",
    ),
    # =========================================================
    # VẬT LÝ LỚP 10 (7 BÀI)
    # =========================================================
    P(
        10,
        "chuyen-dong-thang",
        "Độ dịch chuyển, Vận tốc tổng hợp & Chuyển động thẳng đều",
        "🚀",
        "Phân biệt quãng đường đi được (s) với độ dịch chuyển (d⃗), tốc độ với vận tốc và công thức cộng vận tốc.",
        "Độ dịch chuyển (d⃗ = Δx) là một đại lượng vectơ nối từ vị trí đầu đến vị trí cuối của chuyển động, cho biết cả độ dài và hướng của sự thay đổi vị trí. Chuyển động thẳng đều là chuyển động có quỹ đạo là đường thẳng và có vận tốc không đổi theo thời gian.",
        "• Khi vật chuyển động thẳng và KHÔNG đổi chiều thì độ lớn độ dịch chuyển bằng quãng đường đi được (|d| = s); nếu vật có đổi chiều thì |d| < s.\n"
        "• Phương trình chuyển động thẳng đều: x = x₀ + v · (t − t₀).\n"
        "• Đồ thị độ dịch chuyển – thời gian (d – t): hệ số góc (độ dốc) của đường thẳng chính là vận tốc v = Δd / Δt.\n"
        "• Công thức cộng vận tốc (Tính tương đối của chuyển động): v₁₃⃗ = v₁₂⃗ + v₂₃⃗ (cùng chiều: v₁₃ = v₁₂ + v₂₃; ngược chiều: v₁₃ = |v₁₂ − v₂₃|; vuông góc: v₁₃ = √(v₁₂² + v₂₃²)).",
        [
            {
                "category": "I. Quãng đường (s), Độ dịch chuyển (d⃗) & Phương trình Chuyển động thẳng đều",
                "items": [
                    {"name": "Tốc độ trung bình & Vận tốc trung bình", "formula": "Tốc độ TB: v_tb = s / Δt (vô hướng, ≥ 0)  ;  Vận tốc TB: v⃗ = d⃗ / Δt = (x₂ − x₁) / (t₂ − t₁)", "note": "Vận tốc có thể dương hoặc âm tùy chiều trục Ox"},
                    {"name": "Phương trình tọa độ chuyển động thẳng đều", "formula": "x = x₀ + v · t", "note": "x₀: tọa độ ban đầu lúc t = 0 ; v: vận tốc"},
                ],
            },
            {
                "category": "II. Công thức Cộng vận tốc (1: Vật ; 2: Hệ quy chiếu chuyển động ; 3: Hệ đứng yên)",
                "items": [
                    {"name": "Công thức vectơ tổng quát", "formula": "v₁₃⃗ = v₁₂⃗ + v₂₃⃗", "note": "v₁₃⃗: vận tốc tuyệt đối ; v₁₂⃗: vận tốc tương đối ; v₂₃⃗: vận tốc kéo theo"},
                    {"name": "Xuôi dòng, Ngược dòng & Vuông góc bờ sông", "formula": "Xuôi: v_xuôi = v_thuyền + v_nước ; Ngược: v_ngược = v_thuyền − v_nước ; Vuông góc: v = √(v_thuyền² + v_nước²)", "note": ""},
                ],
            },
        ],
        "Mô tả chính xác vị trí và vận tốc của tàu thuyền trên sông, máy bay trong gió và bài toán hai xe gặp nhau trên trục tọa độ.",
        "Điều khiển robot giao hàng và ca nô qua sông có dòng nước chảy để cập bến đúng điểm đích.",
        "Một người bơi dọc theo chiều dài bể bơi 50 m hết 25 s, rồi quay đầu bơi ngược lại 30 m hết 15 s. Tính quãng đường đi được, độ dịch chuyển, tốc độ trung bình và vận tốc trung bình của người đó trong cả quá trình.",
        "Tổng thời gian: Δt = 25 + 15 = 40 (s). Quãng đường đi được: s = 50 + 30 = 80 (m) ⇒ tốc độ trung bình = 80 / 40 = 2 (m/s). Độ dịch chuyển so với điểm xuất phát: d = 50 − 30 = 20 (m) ⇒ độ lớn vận tốc trung bình = 20 / 40 = 0,5 (m/s).",
        "Một chiếc thuyền chạy ngang vuông góc với bờ sông với vận tốc so với nước là 4 m/s. Nước sông chảy song song với bờ với vận tốc 3 m/s. Độ lớn vận tốc của thuyền so với bờ sông là:",
        ["1 m/s", "3,5 m/s", "5 m/s", "7 m/s"],
        2,
        "Lúc 7 giờ sáng, xe A khởi hành từ vị trí cách gốc O một đoạn 10 km theo chiều dương với vận tốc 40 km/h; cùng lúc đó xe B tại vị trí cách gốc O một đoạn 100 km chuyển động ngược chiều về O với vận tốc 50 km/h. Hãy lập phương trình tọa độ của hai xe và tìm thời điểm, vị trí hai xe gặp nhau.",
        "Chọn trục Ox chiều từ A đến B, gốc O, mốc thời gian lúc 7 giờ. Phương trình hai xe: x_A = 10 + 40t và x_B = 100 − 50t. Khi hai xe gặp nhau: x_A = x_B ⇔ 10 + 40t = 100 − 50t ⇔ 90t = 90 ⇔ t = 1 (giờ) (tức lúc 8 giờ sáng) tại vị trí x = 50 km.",
        game_title="Thử thách thực tế: Chuyển động thẳng & Cộng vận tốc",
        game_description="Đặt vận tốc và hướng → theo dõi độ dịch chuyển d⃗ → dừng đúng tọa độ đích.",
    ),
    P(
        10,
        "gia-toc",
        "Gia tốc, Chuyển động thẳng biến đổi đều, Sự rơi tự do & Chuyển động ném",
        "🏎️",
        "Làm chủ bộ 4 công thức chuyển động thẳng biến đổi đều, sự rơi tự do và chuyển động ném ngang, ném xiên.",
        "Gia tốc (a⃗ = Δv⃗ / Δt, đơn vị m/s²) là đại lượng vectơ đặc trưng cho tốc độ biến thiên của vận tốc (cả về độ lớn lẫn hướng). Trong chuyển động thẳng biến đổi đều, gia tốc a không đổi theo thời gian.",
        "• Phân biệt chuyển động thẳng NHANH DẦN ĐỀU (a và v CÙNG DẤU: a · v > 0) và CHẬM DẦN ĐỀU (a và v TRÁI DẤU: a · v < 0).\n"
        "• Bộ công thức vàng của chuyển động thẳng biến đổi đều và công thức độc lập với thời gian: v² − v₀² = 2as.\n"
        "• Trên đồ thị vận tốc – thời gian (v – t): hệ số góc đường thẳng là gia tốc a; diện tích hình phẳng giới hạn dưới đồ thị là độ dịch chuyển d.\n"
        "• Sự rơi tự do (chỉ chịu tác dụng của trọng lực, v₀ = 0, a = g ≈ 9,8 m/s²) và Chuyển động ném ngang (tầm bay xa L = v₀ · √(2h/g)).",
        [
            {
                "category": "I. Bộ công thức Chuyển động thẳng biến đổi đều",
                "items": [
                    {"name": "Định nghĩa Gia tốc & Vận tốc tức thời", "formula": "a = (v − v₀) / Δt  ⇒  v = v₀ + a · t", "note": "a · v > 0: nhanh dần đều ; a · v < 0: chậm dần đều"},
                    {"name": "Độ dịch chuyển (Quãng đường khi không đổi chiều)", "formula": "d = s = v₀ · t + (1/2) · a · t² = [(v₀ + v) / 2] · t", "note": "Phương trình tọa độ: x = x₀ + v₀t + (1/2)at²"},
                    {"name": "Hệ thức độc lập với thời gian t", "formula": "v² − v₀² = 2 · a · d", "note": "Dùng cực nhanh khi bài toán không cho thời gian t"},
                ],
            },
            {
                "category": "II. Sự rơi tự do (v₀ = 0, a = g) & Chuyển động Ném ngang (từ độ cao h)",
                "items": [
                    {"name": "Công thức Rơi tự do", "formula": "v = g · t  ;  h = s = (1/2) · g · t²  ;  v = √(2gh)  ;  t_rơi = √(2h / g)", "note": "g ≈ 9,8 m/s² hoặc 10 m/s²"},
                    {"name": "Chuyển động Ném ngang (vận tốc đầu v₀)", "formula": "Theo Ox: x = v₀ · t ; Theo Oy: y = (1/2)gt² ; Tầm bay xa: L = v₀ · √(2h / g)", "note": "Vận tốc chạm đất: v = √(v₀² + 2gh)"},
                    {"name": "Chuyển động Ném xiên góc α (từ mặt đất)", "formula": "Độ cao cực đại: H = (v₀² · sin²α) / (2g)  ;  Tầm bay xa: L = (v₀² · sin 2α) / g", "note": "Tầm xa cực đại khi góc ném α = 45°"},
                ],
            },
        ],
        "Ứng dụng tính toán quãng đường phanh khẩn cấp của ô tô, thiết kế đường băng sân bay, thả hàng cứu trợ từ máy bay và góc bắn pháo binh / thể thao.",
        "Chọn gia tốc tăng tốc và thời điểm đạp phanh để xe dừng đúng vạch an toàn.",
        "Một ô tô đang chạy với tốc độ 72 km/h thì người lái hãm phanh, xe chuyển động thẳng chậm dần đều và dừng lại sau khi đi thêm được 50 m. Tính gia tốc của xe và thời gian từ lúc hãm phanh đến khi xe dừng hẳn.",
        "Chọn chiều dương là chiều chuyển động. Đổi v₀ = 72 km/h = 20 m/s; khi dừng hẳn v = 0, s = 50 m. Áp dụng công thức v² − v₀² = 2as: 0² − 20² = 2 · a · 50 ⇒ a = −400 / 100 = −4 (m/s²). Thời gian hãm phanh: t = (v − v₀) / a = (0 − 20) / (−4) = 5 (s).",
        "Một vật được thả rơi tự do từ độ cao h = 45 m xuống đất tại nơi có g = 10 m/s². Thời gian rơi và tốc độ của vật ngay trước khi chạm đất lần lượt là:",
        [
            "t = 3 s ; v = 30 m/s",
            "t = 4,5 s ; v = 45 m/s",
            "t = 9 s ; v = 30 m/s",
            "t = 3 s ; v = 15 m/s",
        ],
        0,
        "Một máy bay cứu trợ bay ngang ở độ cao h = 500 m với tốc độ không đổi v₀ = 50 m/s (180 km/h). Để kiện hàng cứu trợ (bỏ qua sức cản không khí, lấy g = 10 m/s²) rơi trúng đúng địa điểm tiếp nhận trên mặt đất thì phi công phải thả kiện hàng khi máy bay còn cách địa điểm đó theo phương ngang bao nhiêu mét?",
        "Kiện hàng thực hiện chuyển động ném ngang với v₀ = 50 m/s từ độ cao h = 500 m. Thời gian rơi chạm đất là: t = √(2h / g) = √(2 · 500 / 10) = 10 (s). Khoảng cách theo phương ngang (tầm bay xa) là: L = v₀ · t = 50 · 10 = 500 (m).",
        game_title="Thử thách thực tế: Gia tốc & Chuyển động ném",
        game_description="Chọn gia tốc và góc ném → kiểm tra quỹ đạo và quãng đường phanh.",
    ),
]

LESSONS += [
    P(
        10,
        "dinh-luat-newton",
        "Ba định luật Newton về chuyển động & Các lực cơ học trong thực tiễn",
        "🍎",
        "Nắm vững quán tính (Định luật I), phương trình động lực học F⃗_hl = m·a⃗ (Định luật II) và cặp lực - phản lực (Định luật III).",
        "Ba định luật Newton là nền tảng của cơ học cổ điển, giải thích nguyên nhân duy trì chuyển động thẳng đều (quán tính), mối liên hệ giữa hợp lực với gia tốc và tính chất tương tác hai chiều giữa các vật.",
        "• Định luật I Newton (Quán tính): Nếu một vật không chịu tác dụng của lực nào hoặc chịu tác dụng của các lực có hợp lực bằng 0⃗, thì vật đang đứng yên sẽ tiếp tục đứng yên, đang chuyển động sẽ tiếp tục chuyển động thẳng đều. Khối lượng m là số đo mức quán tính của vật.\n"
        "• Định luật II Newton: Gia tốc của một vật cùng hướng với hợp lực tác dụng lên vật; độ lớn của gia tốc tỉ lệ thuận với độ lớn của hợp lực và tỉ lệ nghịch với khối lượng của vật: a⃗ = F⃗_hl / m hay F⃗_hl = m · a⃗.\n"
        "• Định luật III Newton: Trong mọi trường hợp, khi vật A tác dụng lên vật B một lực F⃗_AB thì vật B cũng tác dụng trở lại vật A một lực F⃗_BA: hai lực này cùng giá, cùng độ lớn nhưng ngược chiều (F⃗_AB = −F⃗_BA). Lưu ý: Lực và phản lực đặt vào HAI VẬT KHÁC NHAU nên không bao giờ triệt tiêu nhau!",
        [
            {
                "category": "I. Ba Định luật Newton",
                "items": [
                    {"name": "Định luật I (Cân bằng lực)", "formula": "ΣF⃗ = 0⃗  ⇒  a⃗ = 0⃗  (v⃗ = hằng số)", "note": "Khối lượng m càng lớn ⇒ mức quán tính càng lớn"},
                    {"name": "Định luật II (Phương trình Động lực học)", "formula": "F⃗_hl = F₁⃗ + F₂⃗ + ... = m · a⃗  ⇒  a = F_hl / m", "note": "1 N = 1 kg · 1 m/s²"},
                    {"name": "Định luật III (Lực & Phản lực)", "formula": "F⃗_AB = −F⃗_BA  (và |F_AB| = |F_BA|)", "note": "Xuất hiện/mất đi đồng thời, cùng bản chất, đặt vào 2 vật khác nhau"},
                ],
            },
            {
                "category": "II. Bài toán Vật chuyển động trên mặt phẳng ngang & mặt phẳng nghiêng góc α",
                "items": [
                    {"name": "Kéo vật trên mặt ngang có ma sát μ (lực kéo ngang F_k)", "formula": "N = mg ; F_ms = μmg ⇒ a = (F_k − μmg) / m", "note": ""},
                    {"name": "Vật trượt xuống mặt phẳng nghiêng góc α (hệ số ma sát μ)", "formula": "N = mg·cos α ; a = g · (sin α − μ · cos α)", "note": "Nếu không ma sát (μ = 0) thì a = g · sin α"},
                ],
            },
        ],
        "Giải thích vai trò của dây đai an toàn và túi khí trên ô tô (chống quán tính), tính lực kéo đầu máy xe lửa và nguyên lý đẩy phản lực.",
        "Điều khiển robot kéo kiện hàng trên mặt phẳng ngang và mặt phẳng nghiêng với các lực ma sát khác nhau.",
        "Một ô tô có khối lượng m = 1,2 tấn đang đứng yên thì bắt đầu chuyển động nhanh dần đều trên đường ngang dưới tác dụng của lực kéo động cơ F_k = 3 600 N. Biết hệ số ma sát giữa bánh xe và mặt đường là μ = 0,1 và g = 10 m/s². Tính gia tốc của ô tô và quãng đường xe đi được sau 10 giây đầu.",
        "Đổi m = 1 200 kg. Lực ma sát cản trở chuyển động: F_ms = μ · m · g = 0,1 · 1200 · 10 = 1 200 (N). Theo Định luật II Newton: a = (F_k − F_ms) / m = (3600 − 1200) / 1200 = 2 (m/s²). Quãng đường đi được sau 10 s: s = (1/2) · a · t² = 0,5 · 2 · 10² = 100 (m).",
        "Cặp 'lực và phản lực' trong Định luật III Newton có đặc điểm nào sau đây?",
        [
            "Cùng đặt vào một vật nên cân bằng nhau",
            "Có cùng độ lớn, cùng chiều và đặt vào hai vật khác nhau",
            "Có cùng giá, cùng độ lớn, ngược chiều nhưng đặt vào hai vật khác nhau nên KHÔNG cân bằng nhau",
            "Lực luôn xuất hiện trước, phản lực xuất hiện sau",
        ],
        2,
        "Một người có khối lượng m = 60 kg đứng trên một bàn cân đặt trong buồng thang máy (lấy g = 10 m/s²). Hỏi bàn cân chỉ giá trị tương ứng bao nhiêu Newton trong hai trường hợp: a) Thang máy đi lên nhanh dần đều với gia tốc a = 1,5 m/s²; b) Thang máy đứt cáp rơi tự do với a = g?",
        "Áp lực người nén lên sàn thang máy có độ lớn bằng phản lực N của sàn: N − P = m·a (chiều dương hướng lên). a) Khi đi lên nhanh dần đều (a = +1,5 m/s²): N = m(g + a) = 60 · (10 + 1,5) = 690 (N) (tăng trọng lượng biểu kiến). b) Khi rơi tự do (gia tốc hướng xuống a = −g): N = m(g − g) = 0 (N) (trạng thái không trọng lượng!).",
        game_title="Thử thách thực tế: Ba định luật Newton",
        game_description="Thay đổi lực kéo và hệ số ma sát → quan sát gia tốc → tối ưu chuyển động.",
    ),
    P(
        10,
        "chuyen-dong-tron-bien-dang-lo-xo",
        "Moment lực cân bằng vật rắn, Chuyển động tròn đều (Lực hướng tâm) & Định luật Hooke",
        "🎡",
        "Nắm vững điều kiện cân bằng tổng quát của vật rắn, tốc độ góc ω, gia tốc hướng tâm a_ht = v²/r và Định luật Hooke F_đh = k·|Δl|.",
        "Chuyên đề tích hợp 3 nội dung cơ học quan trọng của Vật lý 10: Cân bằng vật rắn có trục quay (Moment lực, ngẫu lực), Động học - Động lực học chuyển động tròn đều và Biến dạng đàn hồi của vật rắn (Định luật Hooke).",
        "• Điều kiện cân bằng tổng quát của vật rắn: Tổng các lực tác dụng bằng 0⃗ (ΣF⃗ = 0⃗) VÀ Tổng các moment lực đối với một trục quay bất kỳ bằng 0 (ΣM = 0).\n"
        "• Chuyển động tròn đều (bán kính r, chu kỳ T, tần số f): Tốc độ góc ω = Δφ/Δt = 2π/T = 2πf (rad/s); liên hệ tốc độ dài v = ω · r; gia tốc hướng tâm a_ht = v²/r = ω²·r và lực hướng tâm F_ht = m·a_ht = m·v²/r.\n"
        "• Định luật Hooke cho lò xo trong giới hạn đàn hồi: Độ lớn lực đàn hồi tỉ lệ thuận với độ biến dạng |Δl| của lò xo: F_đh = k · |Δl| (k là độ cứng của lò xo, đơn vị N/m).",
        [
            {
                "category": "I. Chuyển động tròn đều & Lực hướng tâm (bán kính r)",
                "items": [
                    {"name": "Tốc độ góc ω & Tốc độ dài v", "formula": "ω = Δφ / Δt = 2π / T = 2πf (rad/s)  ;  v = ω · r (m/s)", "note": "T: chu kỳ (s) ; f: tần số (Hz = vòng/s)"},
                    {"name": "Gia tốc hướng tâm & Lực hướng tâm", "formula": "a_ht = v² / r = ω² · r  ;  F_ht = m · a_ht = (m · v²) / r = m · ω² · r", "note": "Luôn hướng vào tâm quỹ đạo tròn"},
                ],
            },
            {
                "category": "II. Định luật Hooke & Ghép lò xo",
                "items": [
                    {"name": "Định luật Hooke (trong giới hạn đàn hồi)", "formula": "F_đh = k · |Δl| = k · |l − l₀|", "note": "k: độ cứng lò xo (N/m) ; |Δl|: độ biến dạng (m)"},
                    {"name": "Khi treo vật nặng m cân bằng thẳng đứng", "formula": "F_đh = P  ⇔  k · Δl = m · g  ⇒  Δl = (m · g) / k", "note": ""},
                    {"name": "Ghép 2 lò xo (Nối tiếp & Song song)", "formula": "Nối tiếp: 1/k_nt = 1/k₁ + 1/k₂  ;  Song song: k_ss = k₁ + k₂", "note": "Cắt lò xo: k · l = hằng số (cắt ngắn n lần thì độ cứng tăng n lần)"},
                ],
            },
        ],
        "Giải thích vì sao mặt đường ở khúc cua phải làm nghiêng về phía tâm cua, tính quỹ đạo vệ tinh nhân tạo và thiết kế lò xo giảm xóc.",
        "Tính tốc độ tối đa khi xe vào khúc cua để không bị văng ly tâm và chọn độ cứng lò xo giảm xóc.",
        "Một vệ tinh nhân tạo bay tròn đều quanh Trái Đất ở độ cao mà bán kính quỹ đạo tính từ tâm Trái Đất là r = 7 000 km với tốc độ dài v = 7,56 km/s. Tính tốc độ góc ω, chu kỳ quay T và gia tốc hướng tâm a_ht của vệ tinh.",
        "Đổi r = 7 · 10⁶ m và v = 7 560 m/s. Tốc độ góc: ω = v / r = 7560 / (7 · 10⁶) = 1,08 · 10⁻³ (rad/s). Chu kỳ: T = 2π / ω ≈ 5 818 (s) ≈ 97 (phút). Gia tốc hướng tâm: a_ht = v² / r = 7560² / (7 · 10⁶) ≈ 8,165 (m/s²).",
        "Một lò xo có chiều dài tự nhiên l₀ = 20 cm và độ cứng k = 100 N/m. Khi treo thẳng đứng một vật có khối lượng m = 500 g vào đầu dưới của lò xo (lấy g = 10 m/s²) thì chiều dài của lò xo khi cân bằng là:",
        ["20,5 cm", "22 cm", "25 cm", "30 cm"],
        2,
        "Một ô tô có khối lượng m = 1,5 tấn chạy vào một đoạn đường vòng phẳng nằm ngang có bán kính cong r = 50 m. Biết hệ số ma sát nghỉ cực đại giữa lốp xe và mặt đường là μ = 0,45 (lấy g = 10 m/s²). Hỏi ô tô có thể chạy qua khúc cua này với tốc độ tối đa là bao nhiêu km/h để không bị trượt văng ra khỏi đường?",
        "Khi xe vào cua trên đường phẳng ngang, lực ma sát nghỉ đóng vai trò là lực hướng tâm: F_ht ≤ F_msn_max ⇔ (m · v²) / r ≤ μ · m · g ⇔ v ≤ √(μ · g · r) = √(0,45 · 10 · 50) = √225 = 15 (m/s). Đổi sang km/h: v_max = 15 · 3,6 = 54 (km/h).",
        game_title="Thử thách thực tế: Lực hướng tâm & Định luật Hooke",
        game_description="Điều chỉnh tốc độ xe qua khúc cua và thử nghiệm độ cứng k của hệ lò xo.",
    ),
    P(
        10,
        "dong-luong",
        "Động lượng, Xung lượng của lực & Định luật Bảo toàn Động lượng - Va chạm",
        "🎱",
        "Nắm vững động lượng p⃗ = m·v⃗, độ biến thiên động lượng Δp⃗ = F⃗·Δt và định luật bảo toàn động lượng trong va chạm đàn hồi - mềm, chuyển động bằng phản lực.",
        "Động lượng (p⃗ = m · v⃗, đơn vị kg·m/s hoặc N·s) là đại lượng vectơ đặc trưng cho khả năng truyền chuyển động của một vật khi tương tác với vật khác. Động lượng của một hệ cô lập là một đại lượng bảo toàn.",
        "• Xung lượng của lực F⃗ tác dụng trong khoảng thời gian Δt bằng độ biến thiên động lượng của vật: Δp⃗ = p₂⃗ − p₁⃗ = F⃗ · Δt ⇒ F⃗ = Δp⃗ / Δt (Giải thích vì sao kéo dài thời gian va chạm Δt nhờ túi khí, đệm mút, chùng gối khi nhảy xuống đất giúp giảm mạnh lực va đập F!).\n"
        "• Định luật bảo toàn động lượng cho hệ cô lập: p₁⃗ + p₂⃗ = p₁'⃗ + p₂'⃗.\n"
        "• Hai loại va chạm cơ bản: Va chạm mềm (sau va chạm hai vật dính vào nhau cùng chuyển động với vận tốc V⃗ = (m₁v₁⃗ + m₂v₂⃗)/(m₁ + m₂)) và Va chạm hoàn toàn đàn hồi (bảo toàn cả động lượng lẫn động năng) cùng chuyển động bằng phản lực (tên lửa, súng giật lùi).",
        [
            {
                "category": "I. Động lượng & Định lý Xung lượng của lực",
                "items": [
                    {"name": "Động lượng của một vật", "formula": "p⃗ = m · v⃗  (cùng hướng với vận tốc v⃗ ; độ lớn p = m · v)", "note": "Liên hệ với động năng: p = √(2 · m · W_đ)"},
                    {"name": "Độ biến thiên động lượng & Xung lượng", "formula": "Δp⃗ = p₂⃗ − p₁⃗ = F⃗ · Δt  ⇒  F_tb = |Δp⃗| / Δt", "note": "Tăng thời gian tiếp xúc Δt ⇒ giảm lực chấn thương F_tb"},
                    {"name": "Tổng hợp động lượng của hệ 2 vật", "formula": "Cùng hướng: p = p₁ + p₂ ; Ngược hướng: p = |p₁ − p₂| ; Hợp góc α: p = √(p₁² + p₂² + 2p₁p₂cos α)", "note": ""},
                ],
            },
            {
                "category": "II. Định luật Bảo toàn Động lượng & Các bài toán Va chạm",
                "items": [
                    {"name": "Hệ cô lập tổng quát", "formula": "m₁v₁⃗ + m₂v₂⃗ = m₁v₁'⃗ + m₂v₂'⃗", "note": "Khi chiếu lên trục Ox phải chú ý DẤU của các vận tốc"},
                    {"name": "Va chạm mềm (hai vật dính vào nhau sau va chạm)", "formula": "V⃗ = (m₁v₁⃗ + m₂v₂⃗) / (m₁ + m₂)", "note": "Có một phần cơ năng chuyển hóa thành nhiệt năng ΔW"},
                    {"name": "Chuyển động bằng phản lực (Tên lửa / Súng giật lùi)", "formula": "Ban đầu đứng yên (p⃗_đầu = 0⃗): m_khí · v_khí⃗ + M_vỏ · V_vỏ⃗ = 0⃗  ⇒  V_vỏ⃗ = −(m_khí / M_vỏ) · v_khí⃗", "note": "Vỏ tên lửa/súng chuyển động ngược chiều khí phụt/viên đạn"},
                ],
            },
        ],
        "Ứng dụng thiết kế vùng hấp thụ xung lực và túi khí an toàn trên ô tô, phân tích hiện tượng va chạm giao thông và phóng tên lửa vũ trụ.",
        "Điều chỉnh khối lượng và vận tốc hai xe trong mô phỏng va chạm đàn hồi và va chạm mềm.",
        "Một quả bóng đá có khối lượng m = 0,45 kg đang bay ngang với tốc độ v₁ = 10 m/s tới đập vuông góc vào bức tường rồi bật ngược trở lại theo đúng phương cũ với tốc độ v₂ = 8 m/s. Thời gian bóng tiếp xúc với tường là Δt = 0,05 s. Tính độ biến thiên động lượng của bóng và độ lớn lực trung bình do tường tác dụng lên bóng.",
        "Chọn trục Ox trùng phương chuyển động, chiều dương là chiều bóng bật ra (cùng chiều lực của tường): v₁ = −10 m/s và v₂ = +8 m/s. Độ biến thiên động lượng: Δp = m(v₂ − v₁) = 0,45 · [8 − (−10)] = 0,45 · 18 = 8,1 (kg·m/s). Độ lớn lực trung bình của tường: F = Δp / Δt = 8,1 / 0,05 = 162 (N) (Lưu ý: nếu quên đổi dấu v₁ sẽ tính sai thành 0,45·(8−10) = −0,9!).",
        "Một viên bi A có khối lượng m₁ = 200 g chuyển động với tốc độ 5 m/s đến va chạm mềm (dính chặt vào nhau) với viên bi B có khối lượng m₂ = 300 g đang đứng yên trên mặt phẳng ngang nhẵn. Tốc độ của hai viên bi ngay sau va chạm là:",
        ["1 m/s", "2 m/s", "2,5 m/s", "3 m/s"],
        1,
        "Một khẩu pháo có khối lượng M = 1 500 kg (không kể đạn) đặt trên mặt phẳng ngang nhẵn, bắn một viên đạn có khối lượng m = 5 kg bay ra khỏi nòng theo phương hợp với phương ngang một góc α = 60° với vận tốc v = 600 m/s so với mặt đất. Tính tốc độ giật lùi V của khẩu pháo theo phương ngang ngay sau khi bắn.",
        "Áp dụng bảo toàn động lượng theo phương nằm ngang Ox: 0 = m · v · cos α + M · V_x ⇒ độ lớn tốc độ giật lùi của pháo là: V = (m · v · cos 60°) / M = (5 · 600 · 0,5) / 1500 = 1 500 / 1 500 = 1,0 (m/s).",
        game_title="Thử thách thực tế: Động lượng & Va chạm",
        game_description="Chọn m, v → mô phỏng va chạm đàn hồi / va chạm mềm → kiểm nghiệm bảo toàn động lượng.",
    ),
    P(
        10,
        "nang-luong",
        "Công tổng quát A = F·s·cosα, Định lý Động năng & Bảo toàn Cơ năng",
        "⚡",
        "Tính công của lực hợp góc α bất kỳ, vận dụng Định lý biến thiên động năng W_đ2 − W_đ1 = A_ngoại_lực và Định luật bảo toàn cơ năng.",
        "Khi lực không đổi F⃗ tác dụng lên vật và điểm đặt của lực chuyển dời một đoạn s theo hướng hợp với hướng của lực một góc α, thì công thực hiện bởi lực đó là A = F · s · cos α.",
        "• Biện luận dấu của công theo góc α: 0° ≤ α < 90° ⇒ cos α > 0 ⇒ A > 0 (Công phát động); α = 90° ⇒ cos 90° = 0 ⇒ A = 0 (Lực vuông góc với phương dịch chuyển không sinh công!); 90° < α ≤ 180° ⇒ cos α < 0 ⇒ A < 0 (Công cản).\n"
        "• Định lý biến thiên động năng: Độ biến thiên động năng của một vật bằng tổng công của các ngoại lực tác dụng lên vật: W_đ2 − W_đ1 = (1/2)mv₂² − (1/2)mv₁² = ΣA_ngoại_lực.\n"
        "• Khi vật chỉ chịu tác dụng của lực thế (trọng lực, lực đàn hồi) thì cơ năng được bảo toàn: W = W_đ + W_t = hằng số. Nếu có thêm lực ma sát / lực cản F_c thì độ biến thiên cơ năng bằng công của lực cản: W₂ − W₁ = A_cản = −F_c · s.",
        [
            {
                "category": "I. Công tổng quát, Công suất tức thời & Hiệu suất",
                "items": [
                    {"name": "Công tổng quát (góc α = (F⃗, d⃗))", "formula": "A = F · s · cos α = F · d · cos α", "note": "α < 90°: công phát động ; α = 90°: A = 0 ; α > 90°: công cản (ma sát α = 180° ⇒ A_ms = −F_ms·s)"},
                    {"name": "Công suất trung bình & tức thời", "formula": "P = A / t  ;  P_tức_thời = F · v · cos α", "note": ""},
                ],
            },
            {
                "category": "II. Định lý Động năng & Định luật Bảo toàn Cơ năng",
                "items": [
                    {"name": "Định lý biến thiên Động năng", "formula": "ΔW_đ = (1/2)mv₂² − (1/2)mv₁² = A_ngoại_lực", "note": "Áp dụng đúng cho MỌI loại lực (kể cả lực ma sát)"},
                    {"name": "Bảo toàn cơ năng trong trọng trường (không ma sát)", "formula": "W₁ = W₂  ⇔  (1/2)mv₁² + mgh₁ = (1/2)mv₂² + mgh₂", "note": "Con lắc đơn chiều dài l lệch góc α₀: v_max = √[2gl(1 − cos α₀)]"},
                    {"name": "Khi có lực ma sát / lực cản F_ms trên quãng đường s", "formula": "W₂ − W₁ = A_ms = −F_ms · s", "note": "Độ giảm cơ năng chuyển thành nhiệt năng"},
                ],
            },
        ],
        "Giải các bài toán động lực học phức tạp trên đường cong mà không cần dùng gia tốc, tính toán con lắc đơn và năng lượng xe điện.",
        "Quản lý năng lượng thu hồi khi phanh (Regenerative Braking) của xe điện trên cung đường đèo dốc.",
        "Một người kéo một thùng hàng bằng một sợi dây hợp với phương nằm ngang một góc α = 60° với lực kéo F = 100 N làm thùng hàng trượt trên sàn ngang một đoạn s = 10 m. Biết lực ma sát trượt giữa thùng và sàn là F_ms = 20 N. Tính công của lực kéo, công của trọng lực, công của lực ma sát và tổng công của các lực tác dụng lên thùng.",
        "Công của lực kéo: A_F = F · s · cos 60° = 100 · 10 · 0,5 = 500 (J). Trọng lực và phản lực vuông góc phương dịch chuyển ngang (α = 90°) nên A_P = A_N = 0 (J). Công của lực ma sát (α = 180°): A_ms = F_ms · s · cos 180° = −20 · 10 = −200 (J). Tổng công: A_tổng = 500 − 200 = 300 (J).",
        "Một vật có khối lượng m = 1 kg được ném thẳng đứng lên cao với vận tốc ban đầu v₀ = 10 m/s từ mặt đất (lấy g = 10 m/s², bỏ qua sức cản không khí). Độ cao cực đại mà vật đạt được là:",
        ["2,5 m", "5 m", "10 m", "20 m"],
        1,
        "Một viên đạn có khối lượng m = 20 g bay ngang với vận tốc v₁ = 400 m/s xuyên qua một tấm gỗ dày d = 5 cm. Sau khi xuyên qua tấm gỗ, vận tốc của đạn giảm còn v₂ = 100 m/s. Hãy dùng định lý biến thiên động năng để tính độ lớn lực cản trung bình F_c của tấm gỗ tác dụng lên viên đạn.",
        "Đổi m = 0,02 kg và d = 0,05 m. Áp dụng định lý động năng: (1/2)mv₂² − (1/2)mv₁² = A_cản = −F_c · d. Thay số: 0,5 · 0,02 · (100² − 400²) = −F_c · 0,05 ⇔ 0,01 · (−150 000) = −0,05 · F_c ⇔ −1 500 = −0,05 · F_c ⇒ F_c = 30 000 (N).",
        game_title="Thử thách thực tế: Năng lượng và bảo toàn năng lượng",
        game_description="Tăng/giảm tốc trên đường đèo → theo dõi động năng, thế năng và pin xe điện.",
    ),
    P(
        10,
        "dong-luc-hoc-chat-long",
        "Tĩnh học Chất lưu, Phương trình liên tục & Định luật Bernoulli",
        "🌊",
        "Tính áp suất thủy tĩnh p = p₀ + ρgh, phương trình dòng chảy liên tục S₁v₁ = S₂v₂ và nguyên lý khí động học Bernoulli.",
        "Chất lưu (gồm chất lỏng và chất khí) có khả năng chảy. Ở trạng thái tĩnh, độ chênh lệch áp suất giữa hai độ sâu h₁, h₂ là Δp = ρgΔh; khi chất lưu lý tưởng chảy ổn định trong ống, nơi có tiết diện nhỏ hơn sẽ có tốc độ chảy lớn hơn và áp suất tĩnh nhỏ hơn.",
        "• Định luật cơ bản của tĩnh học chất lưu: p = p₀ + ρ · g · h (p₀ là áp suất khí quyển trên mặt thoáng, ρ là khối lượng riêng chất lỏng).\n"
        "• Phương trình liên tục (bảo toàn lưu lượng thể tích Q đối với chất lỏng không nén được): Q = S₁ · v₁ = S₂ · v₂ = hằng số (m³/s) ⇒ v₁ / v₂ = S₂ / S₁ = (d₂ / d₁)².\n"
        "• Định luật Bernoulli cho ống dòng nằm ngang: p + (1/2)ρv² = hằng số (Nơi chất lưu chảy càng nhanh thì áp suất tĩnh p tại đó càng giảm! Giải thích lực nâng cánh máy bay, bình xịt sơn và vì sao hai tàu thủy chạy song song gần nhau dễ bị hút vào nhau).",
        [
            {
                "category": "I. Áp suất Thủy tĩnh & Độ chênh áp suất",
                "items": [
                    {"name": "Áp suất tuyệt đối tại độ sâu h", "formula": "p = p₀ + ρ · g · h", "note": "p₀ ≈ 1,013 · 10⁵ Pa ; ρ_nước = 1000 kg/m³ (cứ sâu thêm 10 m nước thì áp suất tăng thêm ~1 atm)"},
                    {"name": "Độ chênh áp suất giữa 2 điểm", "formula": "p₂ − p₁ = ρ · g · (h₂ − h₁)", "note": ""},
                ],
            },
            {
                "category": "II. Động lực học Chất lưu: Phương trình liên tục & Định luật Bernoulli",
                "items": [
                    {"name": "Phương trình liên tục (Lưu lượng Q = V/t)", "formula": "Q = S₁ · v₁ = S₂ · v₂ = hằng số  ⇒  v₁ / v₂ = S₂ / S₁ = (d₂ / d₁)²", "note": "Bóp nhỏ đầu vòi nước (giảm S) ⇒ tốc độ tia nước v tăng vọt"},
                    {"name": "Phương trình Bernoulli tổng quát", "formula": "p₁ + (1/2)ρv₁² + ρgh₁ = p₂ + (1/2)ρv₂² + ρgh₂ = hằng số", "note": "Với ống nằm ngang (h₁ = h₂): p₁ + (1/2)ρv₁² = p₂ + (1/2)ρv₂²"},
                    {"name": "Công thức Torricelli (Tốc độ nước chảy ra ở lỗ thủng sâu h)", "formula": "v = √(2 · g · h)", "note": ""},
                ],
            },
        ],
        "Giải thích cơ chế tạo lực nâng cánh máy bay, bộ chế hòa khí, ống đo tốc độ máy bay Pitot và thiết kế hệ thống cấp thoát nước.",
        "Điều khiển van và tiết diện đường ống dẫn nước giữa các bể chứa để kiểm soát lưu lượng và áp suất.",
        "Nước chảy ổn định qua một đoạn ống nằm ngang có tiết diện thu hẹp dần từ S₁ = 20 cm² xuống S₂ = 10 cm². Biết tốc độ dòng nước tại tiết diện lớn S₁ là v₁ = 2 m/s và áp suất tĩnh tại đó là p₁ = 1,5 · 10⁵ Pa (KLR của nước ρ = 1 000 kg/m³). Tính tốc độ v₂ và áp suất tĩnh p₂ tại tiết diện nhỏ S₂.",
        "Theo phương trình liên tục: S₁ · v₁ = S₂ · v₂ ⇒ v₂ = v₁ · (S₁ / S₂) = 2 · (20 / 10) = 4 (m/s). Theo phương trình Bernoulli cho ống ngang: p₁ + (1/2)ρv₁² = p₂ + (1/2)ρv₂² ⇒ p₂ = p₁ + (1/2)ρ(v₁² − v₂²) = 1,5·10⁵ + 0,5·1000·(2² − 4²) = 150 000 − 6 000 = 144 000 (Pa) = 1,44 · 10⁵ Pa.",
        "Vì sao ở các nhà ga tàu cao tốc, hành khách luôn được yêu cầu phải đứng sau vạch giới hạn an toàn cách xa mép đường ray khi đoàn tàu chạy vụt qua với tốc độ cao?",
        [
            "Để tránh tiếng ồn của đoàn tàu",
            "Vì đoàn tàu chạy tốc độ lớn làm luồng không khí sát tàu chuyển động rất nhanh, khiến áp suất tĩnh tại đó giảm mạnh so với áp suất khí quyển phía sau lưng, tạo lực đẩy hút người về phía đoàn tàu",
            "Vì đoàn tàu phát ra từ trường hút con người",
            "Vì nhiệt độ không khí cạnh tàu tăng cao",
        ],
        1,
        "Một bồn chứa nước lớn có mặt thoáng mở thông với khí quyển. Ở thành bồn tại vị trí thấp hơn mặt nước một đoạn h = 5 m có một lỗ nhỏ mở thông ra ngoài (lấy g = 10 m/s²). Tính tốc độ tia nước phun ra khỏi lỗ nhỏ đó.",
        "Áp dụng định lý Torricelli (suy ra trực tiếp từ phương trình Bernoulli với p₁ = p₂ = p₀ và v₁ ≈ 0): v = √(2 · g · h) = √(2 · 10 · 5) = 10 (m/s).",
        game_title="Thử thách thực tế: Chất lưu & Định luật Bernoulli",
        game_description="Chọn tiết diện ống và lưu lượng → theo dõi vận tốc và áp suất theo định luật Bernoulli.",
    ),

    # =========================================================
    # VẬT LÝ LỚP 11 (7 BÀI)
    # =========================================================
    P(
        11,
        "dao-dong",
        "Dao động điều hòa, Con lắc lò xo - Con lắc đơn & Năng lượng dao động",
        "⏱️",
        "Làm chủ phương trình li độ - vận tốc - gia tốc của dao động điều hòa, hệ thức độc lập thời gian và chu kỳ con lắc lò xo, con lắc đơn.",
        "Dao động điều hòa là dao động trong đó li độ của vật là một hàm côsin (hay sin) của thời gian: x = A cos(ωt + φ).",
        "• Các đại lượng đặc trưng: Biên độ A (A > 0), tần số góc ω (rad/s), chu kỳ T = 2π/ω (s), tần số f = 1/T = ω/(2π) (Hz), pha dao động (ωt + φ) và pha ban đầu φ.\n"
        "• Phương trình vận tốc v = x' = −ωA sin(ωt + φ) = ωA cos(ωt + φ + π/2) (sớm pha π/2 so với x) và gia tốc a = v' = −ω²x = ω²A cos(ωt + φ + π) (ngược pha với x, luôn hướng về vị trí cân bằng O).\n"
        "• Hệ thức độc lập với thời gian và Năng lượng dao động điều hòa W = W_đ + W_t = (1/2)kA² = (1/2)mω²A².\n"
        "• Dao động tắt dần, dao động cưỡng bức và hiện tượng Cộng hưởng (f_ngoại_lực = f₀).",
        [
            {
                "category": "I. Phương trình & Hệ thức độc lập thời gian của Dao động điều hòa",
                "items": [
                    {"name": "Li độ, Vận tốc & Gia tốc", "formula": "x = A cos(ωt + φ) ; v = −ωA sin(ωt + φ) ; a = −ω²x", "note": "v_max = ωA (tại VTCB x = 0) ; a_max = ω²A (tại biên x = ±A)"},
                    {"name": "Hệ thức độc lập thời gian", "formula": "A² = x² + (v / ω)²  ;  (x / A)² + (v / v_max)² = 1  ;  (a / a_max)² + (v / v_max)² = 1", "note": "Tại x = ±A/2 thì |v| = v_max·√3/2 ; tại x = ±A√2/2 thì W_đ = W_t"},
                ],
            },
            {
                "category": "II. Con lắc lò xo, Con lắc đơn & Năng lượng Dao động",
                "items": [
                    {"name": "Con lắc lò xo (độ cứng k, vật nặng m)", "formula": "ω = √(k / m) = √(g / Δl₀)  ;  T = 2π√(m / k) = 2π√(Δl₀ / g)", "note": "Δl₀ = mg/k là độ giãn tại VTCB khi treo thẳng đứng"},
                    {"name": "Con lắc đơn (chiều dài dây l, gia tốc trọng trường g)", "formula": "ω = √(g / l)  ;  T = 2π√(l / g)  ;  f = (1 / 2π)√(g / l)", "note": "Chu kỳ T của con lắc đơn KHÔNG phụ thuộc khối lượng m của quả nặng"},
                    {"name": "Cơ năng bảo toàn của dao động điều hòa", "formula": "W = W_đ + W_t = (1/2)mv² + (1/2)kx² = (1/2)kA² = (1/2)mω²A² = hằng số", "note": "W_đ và W_t biến thiên tuần hoàn với tần số f' = 2f, ω' = 2ω, T' = T/2"},
                ],
            },
        ],
        "Ứng dụng trong chế tạo đồng hồ quả lắc, thiết kế hệ thống giảm xóc ô tô (dao động tắt dần) và chống cộng hưởng phá hủy cầu đường, tòa nhà cao tầng khi động đất.",
        "Điều chỉnh độ cứng k và hệ số cản giảm xóc để xe ô tô dập tắt dao động êm ái nhất.",
        "Một vật nhỏ có khối lượng m = 200 g dao động điều hòa dọc theo trục Ox với phương trình x = 6 cos(10t − π/3) (trong đó x tính bằng cm, t tính bằng s). Tính biên độ A, tần số góc ω, tốc độ cực đại v_max, tốc độ của vật khi đi qua vị trí có li độ x = 3√3 cm và cơ năng W của vật.",
        "Từ phương trình: A = 6 cm = 0,06 m ; ω = 10 rad/s. Tốc độ cực đại: v_max = ωA = 10 · 6 = 60 (cm/s) = 0,6 (m/s). Tại x = 3√3 cm: |v| = ω√(A² − x²) = 10√(6² − 27) = 10 · 3 = 30 (cm/s). Đổi m = 0,2 kg, cơ năng của vật là: W = (1/2)mω²A² = 0,5 · 0,2 · 10² · (0,06)² = 0,036 (J) = 36 (mJ).",
        "Tại một nơi trên Trái Đất, một con lắc đơn có chiều dài l = 1 m dao động điều hòa với chu kỳ T₁ = 2 s. Nếu tại nơi đó treo một con lắc đơn khác có chiều dài l₂ = 4 m thì chu kỳ dao động điều hòa T₂ của nó là:",
        ["1 s", "2 s", "4 s", "8 s"],
        2,
        "Một đoàn tàu hỏa chạy trên đường ray gồm các thanh ray dài L = 12,5 m nối tiếp nhau. Biết hệ lò xo giảm xóc của toa tàu có chu kỳ dao động riêng là T₀ = 1,25 s. Hỏi đoàn tàu chạy với tốc độ bằng bao nhiêu km/h thì toa tàu bị rung lắc mạnh nhất (xảy ra cộng hưởng cơ)?",
        "Toa tàu bị rung lắc mạnh nhất khi xảy ra hiện tượng cộng hưởng cơ: thời gian tàu đi hết một thanh ray đúng bằng chu kỳ dao động riêng T₀ = 1,25 s của toa tàu. Khi đó tốc độ của tàu là: v = L / T₀ = 12,5 / 1,25 = 10 (m/s) = 36 (km/h).",
        game_title="Thử thách thực tế: Dao động điều hòa",
        game_description="Thay đổi k, m và biên độ A → quan sát đồ thị x, v, a và năng lượng theo thời gian.",
    ),
    P(
        11,
        "song-co",
        "Sóng cơ học, Bước sóng λ = v·T = v/f & Sự truyền sóng",
        "🌊",
        "Phân biệt sóng ngang và sóng dọc, nắm vững bước sóng λ, phương trình truyền sóng và độ lệch pha giữa hai điểm trên phương truyền sóng.",
        "Sóng cơ là dao động cơ lan truyền trong một môi trường vật chất đàn hồi (rắn, lỏng, khí) theo thời gian. Khi sóng cơ truyền đi, chỉ có pha dao động và năng lượng được truyền đi, còn các phần tử vật chất chỉ dao động quanh vị trí cân bằng cố định của chúng.",
        "• Sóng ngang: phương dao động của các phần tử vuông góc với phương truyền sóng (truyền trên mặt nước và trong chất rắn).\n"
        "• Sóng dọc: phương dao động của các phần tử trùng với phương truyền sóng (truyền được trong cả rắn, lỏng và khí — như sóng âm).\n"
        "• Bước sóng (λ, đơn vị m): là quãng đường mà sóng truyền được trong một chu kỳ T (hoặc khoảng cách gần nhất giữa hai điểm trên cùng phương truyền sóng dao động cùng pha): λ = v · T = v / f.\n"
        "• Khi sóng truyền từ môi trường này sang môi trường khác thì tần số f (và chu kỳ T) KHÔNG ĐỔI, còn tốc độ v và bước sóng λ thay đổi tỉ lệ thuận với nhau.",
        [
            {
                "category": "I. Bước sóng (λ), Tốc độ truyền sóng (v) & Chu kỳ - Tần số",
                "items": [
                    {"name": "Công thức Bước sóng", "formula": "λ = v · T = v / f  ⇒  v = λ · f", "note": "Khoảng cách giữa n ngọn sóng liên tiếp là (n − 1)·λ"},
                    {"name": "Khoảng cách ngắn nhất giữa 2 điểm trên phương truyền sóng", "formula": "Cùng pha: d_min = λ ; Ngược pha: d_min = λ / 2 ; Vuông pha: d_min = λ / 4", "note": ""},
                ],
            },
            {
                "category": "II. Phương trình truyền sóng & Độ lệch pha Δφ",
                "items": [
                    {"name": "Phương trình sóng tại điểm M cách nguồn O đoạn x", "formula": "Tại O: u_O = A cos(ωt)  ⇒  Tại M: u_M = A cos(ωt − 2πx / λ)", "note": "M trễ pha hơn nguồn O một góc Δφ = 2πx / λ"},
                    {"name": "Độ lệch pha giữa hai điểm cách nhau đoạn d", "formula": "Δφ = (2π · d) / λ = (ω · d) / v", "note": "Cùng pha: d = kλ ; Ngược pha: d = (k + 0,5)λ"},
                ],
            },
        ],
        "Ứng dụng trong thăm dò địa chấn, cảnh báo sóng thần (Tsunami), siêu âm y học và kỹ thuật âm học.",
        "Điều khiển tần số nguồn sóng để truyền tín hiệu qua môi trường và đo bước sóng λ.",
        "Một người quan sát một chiếc phao nhỏ trên mặt biển thấy nó nhô cao lên 6 lần trong khoảng thời gian 15 giây, và khoảng cách giữa hai đỉnh sóng liên tiếp là 6 m. Tính chu kỳ dao động T của sóng, bước sóng λ và tốc độ truyền sóng v trên mặt biển.",
        "Phao nhô cao 6 lần tương ứng với (6 − 1) = 5 chu kỳ sóng: 5T = 15 s ⇒ T = 3 (s). Khoảng cách giữa 2 đỉnh sóng liên tiếp là bước sóng: λ = 6 (m). Tốc độ truyền sóng: v = λ / T = 6 / 3 = 2 (m/s).",
        "Một sóng cơ có tần số f = 50 Hz truyền trên một sợi dây đàn hồi với tốc độ v = 20 m/s. Bước sóng λ của sóng này là:",
        ["0,25 m (25 cm)", "0,4 m (40 cm)", "2,5 m", "1 000 m"],
        1,
        "Một nguồn sóng O dao động với tần số f = 20 Hz, truyền đi trên mặt nước với tốc độ v = 1,6 m/s. Trên cùng một phương truyền sóng xuất phát từ O, hai điểm M và N cách nhau một đoạn d = 10 cm sẽ dao động lệch pha nhau một góc bao nhiêu radian (cùng pha, ngược pha hay vuông pha)?",
        "Đổi v = 1,6 m/s = 160 cm/s. Bước sóng là: λ = v / f = 160 / 20 = 8 (cm). Độ lệch pha giữa M và N là: Δφ = (2π · d) / λ = (2π · 10) / 8 = 2,5π = 2π + π/2 (rad). Vậy hai điểm M và N dao động VUÔNG PHA với nhau.",
        game_title="Thử thách thực tế: Sóng cơ",
        game_description="Thay đổi tần số f → quan sát bước sóng λ và độ lệch pha giữa các phần tử môi trường.",
    ),
    P(
        11,
        "song-dien-tu-giao-thoa-tu-dien",
        "Giao thoa sóng (Khe Young), Sóng dừng, Sóng điện từ & Tụ điện",
        "📡",
        "Làm chủ điều kiện cực đại - cực tiểu giao thoa, khoảng vân giao thoa ánh sáng i = λD/a, điều kiện sóng dừng, thang sóng điện từ và tụ điện.",
        "Giao thoa là hiện tượng hai sóng kết hợp khi gặp nhau thì có những điểm chúng luôn tăng cường lẫn nhau (cực đại) và có những điểm chúng luôn triệt tiêu nhau (cực tiểu). Sóng điện từ là điện từ trường lan truyền trong không gian (và cả trong chân không) với tốc độ ánh sáng c = 3·10⁸ m/s.",
        "• Giao thoa sóng cơ (2 nguồn cùng pha): Cực đại giao thoa có d₂ − d₁ = kλ; Cực tiểu giao thoa có d₂ − d₁ = (k + 0,5)λ.\n"
        "• Giao thoa ánh sáng qua khe Young (khoảng cách 2 khe a, từ 2 khe đến màn D): Khoảng vân i = (λ · D) / a.\n"
        "• Sóng dừng trên dây dài l: Khoảng cách giữa 2 nút (hoặc 2 bụng) liên tiếp là λ/2; Hai đầu cố định: l = k·(λ/2); Một đầu cố định, một đầu tự do: l = (2k + 1)·(λ/4).\n"
        "• Thang sóng điện từ (Sóng vô tuyến → Vi sóng → Hồng ngoại → Ánh sáng nhìn thấy → Tử ngoại → Tia X → Tia Gamma) và Tụ điện (Điện dung C = Q/U, năng lượng điện trường W = ½CU²).",
        [
            {
                "category": "I. Giao thoa Sóng cơ & Giao thoa Ánh sáng (Khe Young)",
                "items": [
                    {"name": "Giao thoa 2 nguồn cùng pha S₁, S₂", "formula": "Cực đại: d₂ − d₁ = k · λ  ;  Cực tiểu: d₂ − d₁ = (k + 0,5) · λ  (k ∈ ℤ)", "note": "Trên đoạn S₁S₂ cách nhau λ/2 giữa hai cực đại liên tiếp"},
                    {"name": "Giao thoa khe Young (Khoảng vân i)", "formula": "i = (λ · D) / a  ;  Vân sáng bậc k: x_s = k · i  ;  Vân tối: x_t = (k + 0,5) · i", "note": "thường đo a (mm), D (m), λ (μm) ⇒ i (mm)"},
                ],
            },
            {
                "category": "II. Sóng dừng trên dây dài l (tốc độ v, tần số f)",
                "items": [
                    {"name": "Hai đầu dây cố định (k bó sóng = k bụng, k+1 nút)", "formula": "l = k · (λ / 2) = k · v / (2f)  ⇒  fₖ = k · f₁  (k ∈ ℕ*)", "note": "Khoảng cách giữa 2 nút liên tiếp bằng λ / 2"},
                    {"name": "Một đầu cố định, một đầu tự do", "formula": "l = (2k + 1) · (λ / 4)  (k = 0, 1, 2, ...)", "note": "Số bụng = số nút = k + 1"},
                ],
            },
            {
                "category": "III. Sóng điện từ & Tụ điện (Điện dung C - đơn vị Farad F)",
                "items": [
                    {"name": "Sóng điện từ trong chân không", "formula": "Là sóng NGANG ; truyền được trong chân không với tốc độ c = 3·10⁸ m/s ; λ = c / f", "note": "Bước sóng giảm dần: Vô tuyến > Hồng ngoại > Ánh sáng > Tử ngoại > Tia X > Gamma"},
                    {"name": "Điện dung, Ghép tụ điện & Năng lượng tụ điện", "formula": "Q = C · U ; Ghép nối tiếp: 1/C_nt = 1/C₁ + 1/C₂ ; Song song: C_ss = C₁ + C₂ ; W = (1/2)CU² = Q²/(2C)", "note": "1 μF = 10⁻⁶ F ; 1 nF = 10⁻⁹ F ; 1 pF = 10⁻¹² F"},
                ],
            },
        ],
        "Ứng dụng đo chính xác bước sóng ánh sáng laser, thiết kế hộp cộng hưởng đàn guitar (sóng dừng), truyền thông 5G/Wi-Fi (sóng điện từ) và lưu trữ năng lượng xung (tụ điện).",
        "Thực hiện thí nghiệm giao thoa khe Young để đo bước sóng tia laser và điều chỉnh tần số tạo sóng dừng trên dây.",
        "Trong thí nghiệm Young về giao thoa ánh sáng đơn sắc, khoảng cách giữa hai khe hẹp là a = 1,2 mm, khoảng cách từ mặt phẳng chứa hai khe đến màn quan sát là D = 2,4 m. Trên màn, người ta đo được khoảng cách giữa 5 vân sáng liên tiếp là 4,8 mm. Tính khoảng vân i và bước sóng λ của ánh sáng dùng trong thí nghiệm.",
        "Khoảng cách giữa 5 vân sáng liên tiếp là 4 khoảng vân: 4i = 4,8 mm ⇒ i = 1,2 (mm). Bước sóng ánh sáng là: λ = (a · i) / D = (1,2 · 1,2) / 2,4 = 0,6 (μm) = 600 (nm) (ánh sáng màu da cam).",
        "Trên một sợi dây đàn hồi dài l = 90 cm có hai đầu cố định đang có sóng dừng với 3 bụng sóng (k = 3). Bước sóng λ của sóng truyền trên dây là:",
        ["30 cm", "45 cm", "60 cm", "90 cm"],
        2,
        "Một tụ điện có điện dung C = 20 μF được tích điện dưới hiệu điện thế U = 100 V. Hãy tính điện tích Q và năng lượng điện trường W dự trữ trong tụ điện đó.",
        "Đổi C = 20 μF = 20 · 10⁻⁶ F = 2 · 10⁻⁵ F. Điện tích của tụ: Q = C · U = 2 · 10⁻⁵ · 100 = 2 · 10⁻³ (C) = 2 (mC). Năng lượng điện trường trong tụ: W = (1/2) · C · U² = 0,5 · 2 · 10⁻⁵ · 100² = 0,1 (J).",
        game_title="Thử thách thực tế: Giao thoa, Sóng dừng & Tụ điện",
        game_description="Khảo sát vân giao thoa khe Young, tạo sóng dừng trên dây đàn và nạp/phóng tụ điện.",
    ),
    P(
        11,
        "dien-truong",
        "Định luật Coulomb, Điện trường & Cường độ điện trường",
        "⚡",
        "Tính lực tương tác tĩnh điện Coulomb F = k|q₁q₂|/(εr²), cường độ điện trường E = F/|q| và nguyên lý chồng chất điện trường.",
        "Định luật Coulomb xác định lực hút/đẩy giữa hai điện tích điểm đứng yên; Điện trường là môi trường vật chất bao quanh điện tích và truyền tương tác điện lên các điện tích khác đặt trong nó.",
        "• Điện tích nguyên tố: e = 1,6 · 10⁻¹⁹ C (điện tích của electron là −e, của proton là +e). Định luật bảo toàn điện tích trong hệ cô lập: q₁' = q₂' = (q₁ + q₂)/2 khi hai quả cầu kim loại giống hệt nhau chạm nhau rồi tách ra.\n"
        "• Định luật Coulomb: F = k · |q₁ · q₂| / (ε · r²) với k = 9 · 10⁹ N·m²/C² và ε là hằng số điện môi (trong chân không ε = 1).\n"
        "• Cường độ điện trường tại một điểm: E⃗ = F⃗ / q (nếu q > 0 thì F⃗ cùng chiều E⃗; nếu q < 0 thì F⃗ ngược chiều E⃗).\n"
        "• Vectơ cường độ điện trường của một điện tích điểm Q: hướng ra xa Q nếu Q > 0, hướng vào gần Q nếu Q < 0, độ lớn E = k|Q|/(εr²); Nguyên lý chồng chất điện trường: E⃗ = E₁⃗ + E₂⃗.",
        [
            {
                "category": "I. Định luật Coulomb & Bảo toàn Điện tích",
                "items": [
                    {"name": "Lực tương tác tĩnh điện Coulomb", "formula": "F = k · |q₁ · q₂| / (ε · r²)  (với k = 9 · 10⁹ N·m²/C² = 1/(4πε₀))", "note": "Cùng dấu (q₁q₂ > 0): đẩy nhau ; Trái dấu (q₁q₂ < 0): hút nhau"},
                    {"name": "Hai quả cầu giống nhau tích điện q₁, q₂ chạm nhau rồi tách ra", "formula": "q₁' = q₂' = (q₁ + q₂) / 2", "note": "Chú ý cộng đại số có kèm dấu của q₁ và q₂"},
                ],
            },
            {
                "category": "II. Cường độ Điện trường (E⃗ - đơn vị V/m) & Nguyên lý Chồng chất",
                "items": [
                    {"name": "Định nghĩa Cường độ điện trường & Lực điện", "formula": "E = F / |q|  ⇔  F⃗ = q · E⃗", "note": "q > 0: F⃗ ↑↑ E⃗  ;  q < 0: F⃗ ↑↓ E⃗ (ví dụ electron có q = −e bị kéo ngược chiều E⃗)"},
                    {"name": "Điện trường gây bởi điện tích điểm Q tại khoảng cách r", "formula": "E = k · |Q| / (ε · r²)", "note": "Q > 0: E⃗ hướng ra xa Q ; Q < 0: E⃗ hướng lại gần Q"},
                    {"name": "Nguyên lý chồng chất điện trường", "formula": "E⃗ = E₁⃗ + E₂⃗  ⇒  E = √(E₁² + E₂² + 2E₁E₂ cos α)", "note": "Triệt tiêu (E⃗ = 0⃗) khi E₁⃗ và E₂⃗ cùng phương, ngược chiều và E₁ = E₂"},
                ],
            },
        ],
        "Ứng dụng trong công nghệ sơn tĩnh điện, hệ thống lọc bụi tĩnh điện nhà máy nhiệt điện, máy photocopy và máy in laser.",
        "Điều khiển vị trí các điện tích để dẫn hướng chùm hạt mang điện vào đúng vùng mục tiêu.",
        "Hai điện tích điểm q₁ = +4 μC và q₂ = −9 μC đặt cố định tại hai điểm A và B cách nhau 30 cm trong chân không (ε = 1). Tính độ lớn lực tương tác Coulomb giữa chúng và cường độ điện trường tổng hợp tại trung điểm M của đoạn AB.",
        "Đổi q₁ = 4·10⁻⁶ C, q₂ = −9·10⁻⁶ C, r = 0,3 m. Lực hút Coulomb giữa chúng: F = 9·10⁹ · |4·10⁻⁶ · (−9·10⁻⁶)| / (0,3)² = 3,6 (N). Tại trung điểm M (r₁ = r₂ = 0,15 m): vì q₁ > 0 nên E₁⃗ hướng từ A về B; vì q₂ < 0 nên E₂⃗ cũng hướng từ M về B (cùng chiều E₁⃗!). Do đó E_M = E₁ + E₂ = 9·10⁹ · (4·10⁻⁶ + 9·10⁻⁶) / (0,15)² = 5,2 · 10⁶ (V/m).",
        "Nếu khoảng cách giữa hai điện tích điểm trong chân không tăng lên gấp 3 lần (giữ nguyên độ lớn hai điện tích) thì độ lớn lực tương tác Coulomb giữa chúng sẽ:",
        ["Giảm đi 3 lần", "Tăng lên 3 lần", "Giảm đi 9 lần", "Tăng lên 9 lần"],
        2,
        "Hai điện tích điểm q₁ = +2 · 10⁻⁸ C và q₂ = +8 · 10⁻⁸ C đặt cố định tại hai điểm A và B cách nhau 12 cm trong không khí. Hãy xác định vị trí điểm C trên đường thẳng AB để tại đó cường độ điện trường tổng hợp bằng 0.",
        "Vì q₁, q₂ cùng dấu (+) nên điểm C có E⃗ = E₁⃗ + E₂⃗ = 0⃗ phải nằm TRONG đoạn thẳng AB (r₁ + r₂ = 12 cm) và thỏa mãn E₁ = E₂ ⇔ |q₁| / r₁² = |q₂| / r₂² ⇔ 2 / r₁² = 8 / r₂² ⇒ r₂ = 2r₁. Kết hợp r₁ + r₂ = 12 cm, suy ra r₁ = CA = 4 cm và r₂ = CB = 8 cm.",
        game_title="Thử thách thực tế: Điện trường & Lực Coulomb",
        game_description="Đặt điện tích → thay đổi cường độ E → quan sát đường sức điện và quỹ đạo hạt.",
    ),
    P(
        11,
        "dong-dien",
        "Dòng điện không đổi, Suất điện động của Nguồn điện & Định luật Ohm cho toàn mạch",
        "🔋",
        "Hiểu bản chất dòng điện I = Δq/Δt, suất điện động E của nguồn điện, điện trở trong r và Định luật Ohm cho toàn mạch I = E/(R_N + r).",
        "Dòng điện không đổi là dòng điện có chiều và cường độ không đổi theo thời gian: I = Δq / Δt. Nguồn điện có suất điện động E (đặc trưng cho khả năng thực hiện công của lực lạ bên trong nguồn) và điện trở trong r.",
        "• Cường độ dòng điện I = q / t (1 A = 1 C/s) và mật độ dòng electron tự do trong kim loại I = n · S · v · e.\n"
        "• Suất điện động của nguồn điện: E = A_nguồn / q (đơn vị Vôn - V). Công của nguồn điện: A_ng = E · q = E · I · t; Công suất của nguồn điện: P_ng = E · I.\n"
        "• Định luật Ohm cho toàn mạch kín gồm nguồn điện (E, r) và mạch ngoài R_N: I = E / (R_N + r) ⇔ E = I · (R_N + r) = U_N + I · r ⇒ Hiệu điện thế mạch ngoài U_N = I · R_N = E − I · r.\n"
        "• Hiện tượng đoản mạch (khi R_N ≈ 0 ⇒ dòng đoản mạch cực lớn I_đm = E / r gây nguy cơ cháy nổ nguồn) và hiệu suất nguồn điện H = U_N / E = R_N / (R_N + r).",
        [
            {
                "category": "I. Cường độ Dòng điện, Suất điện động E & Công của Nguồn điện",
                "items": [
                    {"name": "Cường độ dòng điện không đổi & Số electron chuyển qua", "formula": "I = q / t  ⇒  q = I · t  ;  Số electron: N_e = q / e = (I · t) / (1,6 · 10⁻¹⁹)", "note": "q (Coulomb - C), I (A), t (s)"},
                    {"name": "Suất điện động E, Công & Công suất của Nguồn điện", "formula": "E = A_lạ / q  ;  A_nguồn = E · I · t  ;  P_nguồn = E · I", "note": ""},
                ],
            },
            {
                "category": "II. Định luật Ohm cho toàn mạch & Ghép nguồn điện",
                "items": [
                    {"name": "Định luật Ohm cho toàn mạch kín", "formula": "I = E / (R_N + r)", "note": "E: suất điện động (V) ; r: điện trở trong của nguồn (Ω) ; R_N: điện trở mạch ngoài (Ω)"},
                    {"name": "Hiệu điện thế hai cực nguồn (Mạch ngoài) & Hiệu suất", "formula": "U_N = I · R_N = E − I · r  ;  H = (U_N / E) × 100% = [R_N / (R_N + r)] × 100%", "note": "Khi mạch ngoài để hở (I = 0) thì U_N = E"},
                    {"name": "Ghép n nguồn giống nhau (E₀, r₀) nối tiếp / song song", "formula": "Nối tiếp: E_b = n·E₀ , r_b = n·r₀  ;  Song song: E_b = E₀ , r_b = r₀ / n", "note": ""},
                ],
            },
        ],
        "Giải thích vì sao khi đề nổ ô tô (dòng I rất lớn) thì đèn xe bị tối đi (do sụt áp I·r bên trong ắc-quy làm U_N = E − I·r giảm), và thiết kế bộ pin xe điện.",
        "Thiết kế mạch cấp nguồn pin/ắc-quy có điện trở trong r cho tải tiêu thụ đạt công suất và hiệu suất tối ưu.",
        "Một nguồn điện có suất điện động E = 12 V và điện trở trong r = 1 Ω được nối với mạch ngoài là một điện trở R = 5 Ω thành mạch kín. Tính cường độ dòng điện I trong mạch, hiệu điện thế mạch ngoài U_N, công suất tiêu thụ mạch ngoài P_N và hiệu suất H của nguồn điện.",
        "Theo định luật Ohm cho toàn mạch: I = E / (R + r) = 12 / (5 + 1) = 2 (A). Hiệu điện thế mạch ngoài: U_N = I · R = 2 · 5 = 10 (V) (hoặc U_N = E − Ir = 12 − 2·1 = 10 V). Công suất mạch ngoài: P_N = U_N · I = 10 · 2 = 20 (W). Hiệu suất nguồn: H = (U_N / E) × 100% = (10 / 12) × 100% ≈ 83,33%.",
        "Một pin có suất điện động E = 1,5 V và điện trở trong r = 0,5 Ω. Nếu hai cực của pin bị nối tắt bằng một dây dẫn có điện trở không đáng kể (R_N ≈ 0, hiện tượng đoản mạch) thì cường độ dòng điện đoản mạch chạy qua pin là:",
        ["0,75 A", "1,5 A", "2,0 A", "3,0 A"],
        3,
        "Cho nguồn điện có suất điện động E = 6 V và điện trở trong r = 2 Ω mắc với một biến trở R ở mạch ngoài. Hỏi phải điều chỉnh biến trở R bằng bao nhiêu Ohm để công suất tiêu thụ ở mạch ngoài P_R đạt giá trị cực đại? Tính công suất cực đại P_R_max đó.",
        "Công suất mạch ngoài là: P_R = I² · R = E² · R / (R + r)² = E² / (√R − r/√R + 2√r)... Theo bất đẳng thức Cauchy: (R + r)² ≥ 4Rr, dấu '=' xảy ra khi R = r = 2 (Ω). Khi đó công suất mạch ngoài đạt cực đại là: P_R_max = E² / (4r) = 6² / (4 · 2) = 4,5 (W).",
        game_title="Thử thách thực tế: Dòng điện không đổi & Toàn mạch",
        game_description="Chọn E, r và biến trở R → khảo sát sụt áp mạch ngoài và cực đại công suất.",
    ),
    P(
        11,
        "tu-truong",
        "Cảm ứng từ B, Lực từ (F = BIl·sinα) & Lực Lorentz tác dụng lên hạt mang điện",
        "🧲",
        "Tính cảm ứng từ B của dây dẫn thẳng dài, vòng dây tròn, ống dây Solenoid và xác định lực từ Ampere, lực Lorentz theo quy tắc bàn tay trái.",
        "Từ trường được đặc trưng định lượng tại mỗi điểm bởi vectơ cảm ứng từ B⃗ (đơn vị Tesla - T). Từ trường tác dụng lực từ F = B·I·l·sin α lên đoạn dây dẫn mang dòng điện và tác dụng lực Lorentz f = |q|·v·B·sin α lên hạt mang điện chuyển động trong nó.",
        "• Công thức cảm ứng từ B trong không khí gây bởi: Dây dẫn thẳng rất dài (B = 2·10⁻⁷ · I / r); Tâm khung dây tròn N vòng (B = 2π·10⁻⁷ · N · I / R); Trong lòng ống dây hình trụ dài Solenoid (B = 4π·10⁻⁷ · (N/l) · I) — xác định chiều bằng Quy tắc nắm tay phải.\n"
        "• Lực từ (Lực Ampere) tác dụng lên đoạn dây dẫn dài l mang dòng điện I: F = B · I · l · sin α (xác định chiều bằng Quy tắc bàn tay trái: Đặt bàn tay trái duỗi thẳng để các đường sức từ B⃗ xuyên vào lòng bàn tay, chiều từ cổ tay đến ngón tay giữa chỉ chiều dòng điện I, khi đó ngón cái choãi ra 90° chỉ chiều của lực từ F⃗).\n"
        "• Lực Lorentz tác dụng lên hạt mang điện q chuyển động với vận tốc v⃗: f = |q| · v · B · sin α.",
        [
            {
                "category": "I. Cảm ứng từ B (đơn vị Tesla - T) của các dòng điện đặc biệt",
                "items": [
                    {"name": "Dây dẫn thẳng rất dài (cách dây đoạn r)", "formula": "B = 2 · 10⁻⁷ · (I / r)", "note": "Đường sức từ là các đường tròn đồng tâm nằm trong mặt phẳng vuông góc dây dẫn"},
                    {"name": "Tâm vòng dây / khung dây tròn (N vòng, bán kính R)", "formula": "B = 2π · 10⁻⁷ · (N · I) / R", "note": ""},
                    {"name": "Trong lòng ống dây hình trụ dài Solenoid (chiều dài l, N vòng)", "formula": "B = 4π · 10⁻⁷ · (N / l) · I = 4π · 10⁻⁷ · n · I", "note": "n = N / l là số vòng dây trên 1 mét chiều dài ống ; từ trường trong ống là từ trường đều"},
                ],
            },
            {
                "category": "II. Lực từ Ampere (trên dây dẫn) & Lực Lorentz (trên hạt mang điện)",
                "items": [
                    {"name": "Lực từ tác dụng lên đoạn dây dài l mang dòng điện I", "formula": "F = B · I · l · sin α  (với α = (B⃗, I⃗))", "note": "Chiều xác định bằng Quy tắc bàn tay trái ; Khi B⃗ ∥ I⃗ (α = 0° hoặc 180°) thì F = 0"},
                    {"name": "Lực Lorentz tác dụng lên điện tích q bay với vận tốc v", "formula": "f = |q| · v · B · sin α  (với α = (v⃗, B⃗))", "note": "Nếu q < 0 (như electron) thì chiều ngón cái ngược với chiều quy tắc bàn tay trái"},
                    {"name": "Bán kính quỹ đạo tròn khi hạt bay vuông góc từ trường đều (α = 90°)", "formula": "f_Lorentz = F_hướng_tâm  ⇔  |q|vB = mv² / R  ⇒  R = (m · v) / (|q| · B)", "note": "Ứng dụng trong máy gia tốc hạt Cyclotron và khối phổ kế"},
                ],
            },
        ],
        "Ứng dụng trong động cơ điện một chiều/xoay chiều, loa âm thanh, máy chụp cộng hưởng từ (MRI) và máy gia tốc hạt.",
        "Điều chỉnh cảm ứng từ B và dòng điện I để điều khiển lực từ di chuyển thanh dẫn trên đường ray từ trường.",
        "Một đoạn dây dẫn thẳng dài l = 20 cm có dòng điện I = 5 A chạy qua được đặt trong từ trường đều có độ lớn cảm ứng từ B = 0,4 T. Tính độ lớn lực từ tác dụng lên đoạn dây dẫn khi dây dẫn hợp với vectơ cảm ứng từ B⃗ các góc: a) α = 90°; b) α = 30°; c) α = 0°.",
        "Đổi l = 0,2 m. Áp dụng công thức F = B · I · l · sin α: a) Với α = 90°: F = 0,4 · 5 · 0,2 · sin 90° = 0,4 (N). b) Với α = 30°: F = 0,4 · 5 · 0,2 · sin 30° = 0,2 (N). c) Với α = 0° (dây song song đường sức từ): sin 0° = 0 ⇒ F = 0 (N).",
        "Một ống dây hình trụ dài l = 40 cm gồm N = 800 vòng dây được đặt trong không khí. Khi cho dòng điện có cường độ I = 2 A chạy qua ống dây thì độ lớn cảm ứng từ B trong lòng ống dây là:",
        ["1,6π · 10⁻³ T (≈ 5,03 mT)", "8π · 10⁻⁴ T", "4π · 10⁻³ T", "2 · 10⁻³ T"],
        0,
        "Một hạt electron (có khối lượng m = 9,1 · 10⁻³¹ kg, độ lớn điện tích |q| = e = 1,6 · 10⁻¹⁹ C) bay vào một từ trường đều có B = 1,82 · 10⁻³ T theo phương vuông góc với các đường sức từ (α = 90°) với tốc độ v = 3,2 · 10⁶ m/s. Hãy tính độ lớn lực Lorentz tác dụng lên electron và bán kính quỹ đạo tròn R của nó.",
        "Độ lớn lực Lorentz: f = |q| · v · B · sin 90° = 1,6·10⁻¹⁹ · 3,2·10⁶ · 1,82·10⁻³ ≈ 9,32 · 10⁻¹⁶ (N). Bán kính quỹ đạo tròn: R = (m · v) / (|q| · B) = (9,1·10⁻³¹ · 3,2·10⁶) / (1,6·10⁻¹⁹ · 1,82·10⁻³) = 0,01 (m) = 1 (cm).",
        game_title="Thử thách thực tế: Từ trường & Lực từ",
        game_description="Điều chỉnh B, I và góc α → áp dụng quy tắc bàn tay trái → điều khiển lực từ và quỹ đạo hạt.",
    ),
    P(
        11,
        "cam-ung-dien-tu",
        "Từ thông Φ, Định luật Faraday về Cảm ứng điện từ, Định luật Lenz & Tự cảm",
        "⚡",
        "Tính từ thông Φ = NBS·cosα, suất điện động cảm ứng e_c = −ΔΦ/Δt, suất điện động trên thanh chuyển động e = Blv·sinθ và hiện tượng tự cảm.",
        "Từ thông (Φ, đơn vị Weber - Wb) diễn tả số đường sức từ xuyên qua một diện tích S. Theo Định luật Faraday, khi từ thông qua một mạch kín biến thiên thì trong mạch xuất hiện một suất điện động cảm ứng có độ lớn tỉ lệ với tốc độ biến thiên của từ thông.",
        "• Từ thông qua khung dây có N vòng, diện tích S: Φ = N · B · S · cos α (trong đó α = (n⃗, B⃗) là góc hợp bởi vectơ pháp tuyến n⃗ của mặt phẳng khung dây và vectơ cảm ứng từ B⃗).\n"
        "• Định luật Lenz về chiều dòng điện cảm ứng: Dòng điện cảm ứng xuất hiện trong mạch kín có chiều sao cho từ trường do nó sinh ra có tác dụng CHỐNG LẠI nguyên nhân (sự tăng hoặc giảm từ thông) đã sinh ra nó.\n"
        "• Định luật Faraday: e_c = −ΔΦ / Δt (Độ lớn |e_c| = |ΔΦ / Δt|); dòng điện cảm ứng I_c = |e_c| / R.\n"
        "• Hiện tượng tự cảm (cảm ứng điện từ do chính sự biến thiên cường độ dòng điện trong mạch gây ra): Φ_tc = L · i và e_tc = −L · (Δi / Δt) (L là độ tự cảm của ống dây, đơn vị Henry - H).",
        [
            {
                "category": "I. Từ thông (Φ - Weber Wb) & Định luật Faraday - Lenz",
                "items": [
                    {"name": "Từ thông qua khung dây N vòng, diện tích S", "formula": "Φ = N · B · S · cos α  (với α = (n⃗, B⃗))", "note": "Chú ý: Nếu đề cho góc β giữa B⃗ và mặt phẳng khung thì α = 90° − β (cos α = sin β)!"},
                    {"name": "Suất điện động cảm ứng (Định luật Faraday)", "formula": "e_c = −ΔΦ / Δt = −(Φ₂ − Φ₁) / Δt  ⇒  |e_c| = |ΔΦ| / Δt", "note": "Dấu '−' biểu thị Định luật Lenz ; Cường độ dòng cảm ứng: I_c = |e_c| / R"},
                ],
            },
            {
                "category": "II. Thanh dẫn chuyển động cắt đường sức từ & Hiện tượng Tự cảm",
                "items": [
                    {"name": "SĐĐ cảm ứng trong đoạn dây dài l chuyển động với vận tốc v", "formula": "|e_c| = B · l · v · sin θ  (với θ = (v⃗, B⃗))", "note": "Xác định cực dương/âm bằng Quy tắc bàn tay phải"},
                    {"name": "Độ tự cảm L của ống dây dài & Suất điện động tự cảm", "formula": "L = 4π · 10⁻⁷ · (N² / l) · S (Henry - H)  ;  e_tc = −L · (Δi / Δt)", "note": "Năng lượng từ trường trong cuộn cảm: W_L = (1/2) · L · I²"},
                ],
            },
        ],
        "Nguyên lý của máy phát điện xoay chiều, bếp từ (dòng điện Foucault làm nóng đáy nồi nhiễm từ), phanh điện từ xe tải hạng nặng và đàn guitar điện.",
        "Điều khiển tốc độ quay của khung dây trong từ trường hoặc dịch chuyển nam châm để tối ưu công suất phát điện.",
        "Một khung dây phẳng gồm N = 200 vòng dây, mỗi vòng có diện tích S = 50 cm² được đặt trong từ trường đều có vectơ cảm ứng từ B⃗ vuông góc với mặt phẳng khung dây (α = 0°). Trong khoảng thời gian Δt = 0,05 s, độ lớn cảm ứng từ giảm đều từ B₁ = 0,6 T xuống B₂ = 0,1 T. Tính độ lớn suất điện động cảm ứng |e_c| và cường độ dòng điện cảm ứng I_c trong khung, biết điện trở của khung là R = 5 Ω.",
        "Đổi S = 50 cm² = 5 · 10⁻³ m². Vì B⃗ vuông góc mặt phẳng khung nên B⃗ song song pháp tuyến n⃗ ⇒ α = 0° (cos 0° = 1). Độ biến thiên từ thông: |ΔΦ| = N · S · |B₂ − B₁| · cos 0° = 200 · 5·10⁻³ · |0,1 − 0,6| = 0,5 (Wb). Suất điện động cảm ứng: |e_c| = |ΔΦ| / Δt = 0,5 / 0,05 = 10 (V). Cường độ dòng điện cảm ứng: I_c = |e_c| / R = 10 / 5 = 2 (A).",
        "Một cuộn cảm có độ tự cảm L = 0,2 H. Khi cường độ dòng điện trong cuộn cảm giảm đều từ 5 A về 0 trong khoảng thời gian Δt = 0,1 s thì độ lớn suất điện động tự cảm xuất hiện trong cuộn cảm là:",
        ["1 V", "5 V", "10 V", "20 V"],
        2,
        "Một máy bay có chiều dài sải cánh l = 40 m đang bay ngang với tốc độ v = 900 km/h tại khu vực có thành phần thẳng đứng của cảm ứng từ Trái Đất là B_v = 5 · 10⁻⁵ T. Hãy tính hiệu điện thế cảm ứng xuất hiện giữa hai đầu cánh máy bay.",
        "Đổi v = 900 km/h = 250 m/s. Cánh máy bay chuyển động ngang cắt vuông góc các đường sức từ thẳng đứng (θ = 90°), nên suất điện động cảm ứng (hiệu điện thế) giữa hai đầu cánh là: |e_c| = B_v · l · v · sin 90° = 5·10⁻⁵ · 40 · 250 · 1 = 0,5 (V).",
        game_title="Thử thách thực tế: Cảm ứng điện từ",
        game_description="Tăng tốc độ biến thiên từ thông ΔΦ/Δt → theo dõi suất điện động cảm ứng và định luật Lenz.",
    ),

    # =========================================================
    # VẬT LÝ LỚP 12 (8 BÀI)
    # =========================================================
    P(
        12,
        "vat-ly-nhiet-khi-ly-tuong",
        "Vật lý Nhiệt (Nhiệt nóng chảy - Nhiệt hóa hơi), Định luật I NĐLH & Phương trình trạng thái Khí lý tưởng",
        "🌡️",
        "Làm chủ chuyên đề Vật lý Nhiệt & Khí lý tưởng lớp 12 (GDPT 2018): Q = λm, Q = Lm, ΔU = A + Q và phương trình pV/T = nR.",
        "Chuyên đề trọng tâm của Vật lý 12 (Chương trình GDPT 2018) nghiên cứu sự chuyển thể của các chất (nóng chảy, hóa hơi), Định luật I Nhiệt động lực học và các định luật chất khí (Boyle, Charles, Phương trình trạng thái khí lý tưởng và Động năng phân tử khí).",
        "• Nhiệt nóng chảy riêng λ (J/kg): nhiệt lượng cần cung cấp để 1 kg chất rắn nóng chảy hoàn toàn ở nhiệt độ nóng chảy: Q = λ · m (với nước đá ở 0°C: λ ≈ 3,34 · 10⁵ J/kg).\n"
        "• Nhiệt hóa hơi riêng L (J/kg): nhiệt lượng cần để 1 kg chất lỏng hóa hơi hoàn toàn ở nhiệt độ xác định: Q = L · m (với nước ở 100°C: L ≈ 2,26 · 10⁶ J/kg).\n"
        "• Định luật I Nhiệt động lực học: ΔU = A + Q (Quy ước dấu: Hệ nhận nhiệt Q > 0, truyền nhiệt Q < 0; Hệ nhận công A > 0, thực hiện công A < 0).\n"
        "• Ba thông số trạng thái của một lượng khí (Áp suất p, Thể tích V, Nhiệt độ tuyệt đối T(K) = t(°C) + 273): Định luật Boyle (đẳng nhiệt p₁V₁ = p₂V₂), Định luật Charles (đẳng áp V₁/T₁ = V₂/T₂), Phương trình trạng thái p₁V₁/T₁ = p₂V₂/T₂ và Phương trình Clapeyron: p · V = n · R · T.\n"
        "• Áp suất khí theo mô hình động học phân tử: p = (1/3)μmv̄² = (2/3)μW̄_đ và Động năng tịnh tiến trung bình của phân tử khí: W̄_đ = (3/2) · k · T.",
        [
            {
                "category": "I. Sự chuyển thể (Nhiệt nóng chảy λ, Nhiệt hóa hơi L) & Định luật I NĐLH",
                "items": [
                    {"name": "Nhiệt lượng làm nóng chảy & hóa hơi", "formula": "Nóng chảy: Q_nc = λ · m  ;  Hóa hơi: Q_hh = L · m  ;  Đổi nhiệt độ: Q = m · c · Δt", "note": "Trong suốt quá trình đang nóng chảy / đang sôi thì nhiệt độ KHÔNG ĐỔI"},
                    {"name": "Định luật I Nhiệt động lực học", "formula": "ΔU = A + Q", "note": "Q > 0: hệ nhận nhiệt ; Q < 0: hệ tỏa nhiệt ; A > 0: hệ nhận công (bị nén) ; A < 0: hệ sinh công (giãn nở: |A| = p·ΔV)"},
                ],
            },
            {
                "category": "II. Các Định luật Khí lý tưởng (Luôn đổi sang Nhiệt độ tuyệt đối T(K) = t(°C) + 273!)",
                "items": [
                    {"name": "Đẳng nhiệt (Boyle: T = const) & Đẳng áp (Charles: p = const)", "formula": "Đẳng nhiệt: p₁V₁ = p₂V₂  ;  Đẳng áp: V₁ / T₁ = V₂ / T₂  ;  Đẳng tích (V = const): p₁ / T₁ = p₂ / T₂", "note": ""},
                    {"name": "Phương trình trạng thái Khí lý tưởng & Clapeyron", "formula": "(p₁ · V₁) / T₁ = (p₂ · V₂) / T₂ = hằng số  ;  p · V = n · R · T = (m / M) · R · T", "note": "R ≈ 8,31 J/(mol·K) khi p (Pa), V (m³) ; hoặc R ≈ 0,082 atm·L/(mol·K)"},
                ],
            },
            {
                "category": "III. Động học phân tử khí & Động năng trung bình của phân tử",
                "items": [
                    {"name": "Áp suất khí theo mật độ phân tử μ = N/V", "formula": "p = (1/3) · μ · m₀ · v̄² = (2/3) · μ · W̄_đ", "note": ""},
                    {"name": "Động năng tịnh tiến trung bình của 1 phân tử khí", "formula": "W̄_đ = (1/2)m₀v̄² = (3/2) · k · T  (với hằng số Boltzmann k = R / N_A ≈ 1,38 · 10⁻²³ J/K)", "note": "Căn quân phương tốc độ phân tử: v_rms = √(v̄²) = √(3RT / M)"},
                ],
            },
        ],
        "Giải thích chu trình hoạt động của động cơ nhiệt, máy lạnh, lốp xe ô tô tăng áp suất khi chạy ngoài trời nắng và tính toán bình chứa khí nén y tế.",
        "Mô phỏng quá trình nén/giãn khí trong xi-lanh động cơ theo các quá trình đẳng nhiệt, đẳng áp, đẳng tích.",
        "Một bình kín có dung tích không đổi chứa khí ôxi ở nhiệt độ 27°C và áp suất p₁ = 2,0 atm. Nếu nung nóng bình để nhiệt độ của khí tăng lên tới 87°C thì áp suất p₂ của khí trong bình bằng bao nhiêu? Khi đó động năng tịnh tiến trung bình của các phân tử khí tăng lên bao nhiêu lần?",
        "Đổi sang nhiệt độ tuyệt đối Kelvin: T₁ = 27 + 273 = 300 (K) và T₂ = 87 + 273 = 360 (K). Vì bình kín có thể tích không đổi (quá trình đẳng tích): p₂ / T₂ = p₁ / T₁ ⇒ p₂ = p₁ · (T₂ / T₁) = 2,0 · (360 / 300) = 2,4 (atm). Vì W̄_đ = (3/2)kT tỉ lệ thuận với T nên động năng trung bình của phân tử tăng: T₂ / T₁ = 360 / 300 = 1,2 (lần).",
        "Người ta truyền cho khí trong xi-lanh một nhiệt lượng 150 J. Khí nở ra và thực hiện công 90 J đẩy pít-tông lên. Độ biến thiên nội năng ΔU của khối khí trong quá trình này là:",
        ["ΔU = +240 J", "ΔU = +60 J", "ΔU = −60 J", "ΔU = −240 J"],
        1,
        "Tính tổng nhiệt lượng Q cần cung cấp để biến đổi hoàn toàn m = 0,5 kg nước đá ở nhiệt độ 0°C thành hơi nước ở 100°C. Biết nhiệt nóng chảy riêng của nước đá ở 0°C là λ = 3,34 · 10⁵ J/kg, nhiệt dung riêng của nước là c = 4 200 J/(kg·K) và nhiệt hóa hơi riêng của nước ở 100°C là L = 2,26 · 10⁶ J/kg.",
        "Quá trình gồm 3 giai đoạn liên tiếp: 1) Làm nước đá ở 0°C nóng chảy hoàn toàn thành nước ở 0°C: Q₁ = λ · m = 3,34·10⁵ · 0,5 = 167 000 (J). 2) Đun nước từ 0°C lên 100°C: Q₂ = m · c · Δt = 0,5 · 4200 · 100 = 210 000 (J). 3) Làm nước ở 100°C hóa hơi hoàn toàn: Q₃ = L · m = 2,26·10⁶ · 0,5 = 1 130 000 (J). Tổng nhiệt lượng cần cung cấp là: Q = Q₁ + Q₂ + Q₃ = 1 507 000 (J) = 1 507 (kJ).",
        game_title="Thử thách thực tế: Vật lý nhiệt & Khí lý tưởng",
        game_description="Điều chỉnh p, V, T trong xi-lanh → kiểm nghiệm định luật Boyle, Charles và Định luật I NĐLH.",
    ),
    P(
        12,
        "dien-truong-cuong-do",
        "Điện trường đều, Chuyển động của Hạt mang điện trong Điện trường & Công của Lực điện",
        "⚡",
        "Phân tích chuyển động giống vật ném ngang của hạt mang điện trong điện trường đều giữa hai bản phẳng song song và tính công A = qEd.",
        "Điện trường đều là điện trường mà vectơ cường độ điện trường E⃗ tại mọi điểm đều có cùng phương, cùng chiều và cùng độ lớn; đường sức điện là những đường thẳng song song, cách đều nhau (như giữa hai bản kim loại phẳng đặt song song tích điện trái dấu).",
        "• Cường độ điện trường đều giữa hai bản phẳng song song cách nhau đoạn d, hiệu điện thế U: E = U / d (hướng từ bản dương sang bản âm).\n"
        "• Gia tốc của hạt mang điện tích q, khối lượng m trong điện trường đều: a⃗ = F⃗ / m = (q · E⃗) / m.\n"
        "• Nếu hạt mang điện bay vào điện trường đều theo phương vuông góc với đường sức điện (với vận tốc đầu v₀), hạt sẽ chuyển động theo quỹ đạo Parabol giống hệt chuyển động ném ngang với gia tốc a = |q|E/m.\n"
        "• Công của lực điện trường: A_MN = q · E · d (trong đó d = s · cos α là hình chiếu của đường đi MN lên phương của đường sức điện; công của lực tĩnh điện KHÔNG phụ thuộc hình dạng đường đi mà chỉ phụ thuộc vị trí điểm đầu M và điểm cuối N).",
        [
            {
                "category": "I. Điện trường đều & Công của Lực điện (Trường thế)",
                "items": [
                    {"name": "Liên hệ giữa E và U trong điện trường đều", "formula": "E = U / d  ⇔  U = E · d", "note": "d là khoảng cách giữa hai bản phẳng theo phương đường sức (m)"},
                    {"name": "Công của lực điện khi q di chuyển từ M đến N", "formula": "A_MN = q · E · d_MN = q · E · s · cos α", "note": "d_MN > 0 nếu hình chiếu đi xuôi chiều đường sức ; Trên đường cong kín: A_kín = 0"},
                ],
            },
            {
                "category": "II. Quỹ đạo Hạt mang điện bay vuông góc vào Điện trường đều (giống Ném ngang)",
                "items": [
                    {"name": "Gia tốc của hạt (khối lượng m, điện tích q)", "formula": "a = |q| · E / m = (|q| · U) / (m · d)", "note": "Hạt dương (q > 0) lệch về bản âm ; hạt âm (q < 0) lệch về bản dương"},
                    {"name": "Phương trình quỹ đạo & Độ lệch y khi ra khỏi bản dài L", "formula": "t = L / v₀  ;  y = (1/2) · a · t² = [ |q| · E · L² ] / (2 · m · v₀²)", "note": ""},
                ],
            },
        ],
        "Ứng dụng trong ống phóng điện tử (dao động ký điện tử), máy gia tốc tuyến tính và màn hình hiển thị.",
        "Đặt hiệu điện thế U lên hai bản lái tia để điều khiển quỹ đạo chùm electron bắn trúng điểm đích trên màn huỳnh quang.",
        "Hai bản kim loại phẳng đặt song song nằm ngang cách nhau d = 2 cm, tích điện trái dấu với hiệu điện thế U = 120 V. Một hạt bụi tích điện q = −2 · 10⁻¹⁰ C nằm lơ lửng cân bằng chính giữa hai bản (lấy g = 10 m/s²). Hỏi bản nào tích điện dương và khối lượng m của hạt bụi bằng bao nhiêu?",
        "Đổi d = 0,02 m. Cường độ điện trường giữa hai bản là: E = U / d = 120 / 0,02 = 6 000 (V/m). Để hạt bụi lơ lửng cân bằng thì lực điện F⃗ phải hướng thẳng đứng lên trên (ngược chiều trọng lực P⃗). Vì hạt bụi mang điện âm (q < 0) nên E⃗ phải hướng thẳng đứng từ trên xuống dưới, tức là BẢN TRÊN tích điện dương (+). Khi cân bằng: |q| · E = m · g ⇒ m = (2·10⁻¹⁰ · 6000) / 10 = 1,2 · 10⁻⁷ (kg) = 0,12 (mg).",
        "Một điện tích q = +5 μC di chuyển dọc theo cạnh một tam giác đều ABC cạnh a = 10 cm đặt trong điện trường đều có E⃗ song song với cạnh BC và có độ lớn E = 4 000 V/m. Công của lực điện khi điện tích q di chuyển từ B đến C là:",
        ["0,02 J (20 mJ)", "0,01 J", "−0,02 J", "0 J"],
        0,
        "Một electron (m = 9,1 · 10⁻³¹ kg, q = −1,6 · 10⁻¹⁹ C) bay từ bản dương sang bản âm dọc theo đường sức của một điện trường đều có E = 1 000 V/m với vận tốc ban đầu v₀ = 6 · 10⁶ m/s. Hỏi electron đi được quãng đường tối đa bao nhiêu xăng-ti-mét trước khi dừng lại rồi quay đầu chuyển động ngược lại?",
        "Vì electron mang điện âm (q < 0) bay cùng chiều E⃗ nên lực điện ngược chiều chuyển động, thực hiện công cản làm electron chậm dần. Áp dụng định lý động năng: 0 − (1/2)mv₀² = q · E · s (với q < 0) ⇒ s = (m · v₀²) / (2 · |q| · E) = (9,1·10⁻³¹ · 36·10¹²) / (2 · 1,6·10⁻¹⁹ · 1000) ≈ 0,1024 (m) = 10,24 (cm).",
        game_title="Thử thách thực tế: Chuyển động hạt trong Điện trường",
        game_description="Thay đổi điện áp hai bản phẳng → quan sát quỹ đạo parabol của hạt mang điện.",
    ),
    P(
        12,
        "dien-the",
        "Thế năng điện, Điện thế V, Hiệu điện thế U_MN & Đơn vị Electron-Volt (eV)",
        "🔋",
        "Nắm vững mối liên hệ giữa Thế năng điện W_M = q·V_M, Hiệu điện thế U_MN = V_M − V_N = A_MN / q = E·d và đơn vị năng lượng eV.",
        "Điện thế tại một điểm M trong điện trường (V_M = W_M / q, đơn vị Vôn - V) đặc trưng cho điện trường về phương diện tạo ra thế năng khi đặt tại đó một điện tích q. Hiệu điện thế U_MN = V_M − V_N đo công của lực điện khi dịch chuyển một đơn vị điện tích dương từ M đến N.",
        "• Thế năng của một điện tích q tại điểm M trong điện trường: W_M = A_M∞ = q · V_M.\n"
        "• Hiệu điện thế giữa hai điểm M và N: U_MN = V_M − V_N = A_MN / q ⇒ A_MN = q · U_MN.\n"
        "• Liên hệ giữa cường độ điện trường và hiệu điện thế: E = U_MN / d_MN (dọc theo chiều đường sức điện trường thì điện thế V giảm dần!).\n"
        "• Đơn vị năng lượng trong vật lý nguyên tử & hạt nhân: 1 electron-volt (1 eV) là động năng mà 1 hạt có điện tích nguyên tố e thu được khi được tăng tốc qua hiệu điện thế U = 1 V: 1 eV = 1,6 · 10⁻¹⁹ J.",
        [
            {
                "category": "I. Thế năng điện, Điện thế (V) & Hiệu điện thế (U_MN)",
                "items": [
                    {"name": "Thế năng điện & Điện thế tại điểm M", "formula": "V_M = W_M / q = A_M∞ / q  ⇒  W_M = q · V_M", "note": "Gốc điện thế thường chọn ở mặt đất hoặc ở vô cực (V_∞ = 0)"},
                    {"name": "Hiệu điện thế & Công của lực điện", "formula": "U_MN = V_M − V_N = A_MN / q  ⇔  A_MN = q · U_MN = W_M − W_N", "note": "U_MN = −U_NM ; U_MN = E · d_MN"},
                ],
            },
            {
                "category": "II. Định lý Động năng khi tăng tốc hạt bằng Hiệu điện thế U & Đơn vị eV",
                "items": [
                    {"name": "Tăng tốc hạt mang điện q từ trạng thái nghỉ (v₀ = 0) qua điện áp U", "formula": "W_đ = (1/2) · m · v² = |q| · U  ⇒  v = √(2 · |q| · U / m)", "note": "Nguyên lý súng phóng electron và máy phát tia X"},
                    {"name": "Đơn vị năng lượng Electron-Volt (eV)", "formula": "1 eV = 1,6 · 10⁻¹⁹ J  ;  1 keV = 10³ eV  ;  1 MeV = 10⁶ eV = 1,6 · 10⁻¹³ J", "note": ""},
                ],
            },
        ],
        "Ứng dụng tính vận tốc chùm electron trong ống phát tia X y tế, kính hiển vi điện tử và thiết kế chống sét cao áp.",
        "Chọn hiệu điện thế tăng tốc U cho súng phóng điện tử để hạt đạt đúng động năng yêu cầu.",
        "Trong ống phát tia X, một electron (m = 9,1 · 10⁻³¹ kg, |q| = e = 1,6 · 10⁻¹⁹ C) bứt ra khỏi catốt với vận tốc ban đầu không đáng kể (v₀ ≈ 0) và được tăng tốc bởi hiệu điện thế U_AK = 20 kV giữa anốt và catốt. Tính động năng của electron khi đập vào đối catốt theo đơn vị keV và Joule, đồng thời tính tốc độ v của electron khi đó.",
        "Vì electron có điện tích độ lớn 1e được tăng tốc qua U = 20 kV nên động năng thu được là: W_đ = 20 keV = 20 000 eV. Đổi sang Joule: W_đ = |q| · U = 1,6·10⁻¹⁹ · 20 000 = 3,2 · 10⁻¹⁵ (J). Tốc độ của electron khi đập vào đối catốt: v = √(2W_đ / m) = √(2 · 3,2·10⁻¹⁵ / 9,1·10⁻³¹) ≈ 8,39 · 10⁷ (m/s).",
        "Tại hai điểm M và N trong một điện trường có điện thế lần lượt là V_M = 50 V và V_N = −20 V. Công của lực điện trường khi làm dịch chuyển một điện tích q = −2 μC từ M đến N là:",
        ["+1,4 · 10⁻⁴ J", "−1,4 · 10⁻⁴ J", "+6 · 10⁻⁵ J", "−6 · 10⁻⁵ J"],
        1,
        "Một mặt đẳng thế là mặt gồm các điểm có cùng điện thế V. Hãy chứng minh rằng công của lực điện khi di chuyển một điện tích q bất kỳ từ điểm M đến điểm N nằm trên cùng một mặt đẳng thế luôn bằng 0, và suy ra phương của vectơ cường độ điện trường E⃗ so với mặt đẳng thế.",
        "Vì M và N thuộc cùng một mặt đẳng thế nên V_M = V_N ⇒ U_MN = V_M − V_N = 0. Do đó công của lực điện là: A_MN = q · U_MN = 0. Vì A_MN = q · E · s · cos α = 0 với mọi dịch chuyển s trên mặt đẳng thế nên cos α = 0 ⇒ α = 90°: vectơ cường độ điện trường E⃗ (và đường sức điện) luôn VUÔNG GÓC với mặt đẳng thế tại mọi điểm.",
        game_title="Thử thách thực tế: Điện thế và hiệu điện thế",
        game_description="Thay đổi hiệu điện thế tăng tốc U → theo dõi động năng (eV) và tốc độ chùm hạt.",
    ),
    P(
        12,
        "mach-xoay-chieu",
        "Đại cương Dòng điện xoay chiều (Giá trị hiệu dụng), Công suất & Hệ số công suất cosφ",
        "🔌",
        "Nắm vững phương trình điện áp - dòng điện xoay chiều, giá trị hiệu dụng (I = I₀/√2, U = U₀/√2), độ lệch pha φ = φ_u − φ_i và công suất P = UI·cosφ.",
        "Dòng điện xoay chiều (AC) là dòng điện có cường độ biến thiên điều hòa theo thời gian: i = I₀ cos(ωt + φ_i). Giá trị hiệu dụng của dòng điện xoay chiều được định nghĩa dựa trên tác dụng nhiệt tương đương với dòng điện không đổi và bằng giá trị cực đại chia cho √2.",
        "• Giá trị hiệu dụng của cường độ dòng điện, điện áp và suất điện động: I = I₀ / √2 ; U = U₀ / √2 ; E = E₀ / √2 (Các dụng cụ đo AC như Ampe kế, Vôn kế và số ghi trên thiết bị như 220V đều là GIÁ TRỊ HIỆU DỤNG!).\n"
        "• Độ lệch pha giữa điện áp và dòng điện: φ = φ_u − φ_i.\n"
        "• Công suất tiêu thụ trung bình của mạch điện xoay chiều: P = U · I · cos φ, trong đó cos φ gọi là hệ số công suất (0 ≤ cos φ ≤ 1).\n"
        "• Ý nghĩa của việc nâng cao hệ số công suất cos φ trong công nghiệp (quy định cos φ ≥ 0,85 để giảm cường độ dòng điện I = P/(U·cosφ) và giảm hao phí trên đường dây).",
        [
            {
                "category": "I. Phương trình & Giá trị hiệu dụng của Dòng điện xoay chiều",
                "items": [
                    {"name": "Phương trình điện áp u và dòng điện i", "formula": "u = U₀ cos(ωt + φ_u)  ;  i = I₀ cos(ωt + φ_i)  (với ω = 2πf)", "note": "Mỗi giây dòng điện xoay chiều tần số f đổi chiều 2f lần (nếu i_đầu ≠ 0)"},
                    {"name": "Giá trị hiệu dụng (RMS)", "formula": "I = I₀ / √2  ;  U = U₀ / √2  ;  E = E₀ / √2", "note": "Ví dụ: Mạng điện 220 V có điện áp cực đại U₀ = 220√2 ≈ 311 V"},
                ],
            },
            {
                "category": "II. Độ lệch pha φ, Công suất tiêu thụ P & Hệ số công suất cos φ",
                "items": [
                    {"name": "Độ lệch pha của u so với i", "formula": "φ = φ_u − φ_i", "note": "φ > 0: u sớm pha hơn i ; φ < 0: u trễ pha hơn i ; φ = 0: u và i cùng pha"},
                    {"name": "Công suất tiêu thụ & Điện năng tiêu thụ", "formula": "P = U · I · cos φ = (1/2) · U₀ · I₀ · cos φ = I² · R  ;  A = P · t", "note": "Chỉ có điện trở thuần R mới tiêu thụ điện năng tỏa nhiệt!"},
                ],
            },
        ],
        "Giúp đọc hiểu thông số lưới điện xoay chiều, tính công suất thực tế và bù hệ số công suất cos φ trong nhà máy công nghiệp.",
        "Quản lý phụ tải trong mạng điện xoay chiều và bù hệ số công suất cos φ để giảm hao phí.",
        "Đặt điện áp xoay chiều u = 200√2 cos(100πt + π/6) (V) vào hai đầu một đoạn mạch thì dòng điện trong mạch có biểu thức i = 4√2 cos(100πt − π/6) (A). Tìm tần số f, điện áp hiệu dụng U, cường độ hiệu dụng I, độ lệch pha φ, hệ số công suất cos φ và công suất tiêu thụ P của đoạn mạch.",
        "Từ phương trình: ω = 100π rad/s ⇒ f = ω/(2π) = 50 (Hz); U = 200√2 / √2 = 200 (V); I = 4√2 / √2 = 4 (A). Độ lệch pha: φ = φ_u − φ_i = π/6 − (−π/6) = π/3 (rad) (u sớm pha π/3 so với i). Hệ số công suất: cos φ = cos(π/3) = 0,5. Công suất tiêu thụ: P = U · I · cos φ = 200 · 4 · 0,5 = 400 (W).",
        "Tại Việt Nam, mạng điện xoay chiều dân dụng có điện áp hiệu dụng U = 220 V và tần số f = 50 Hz. Điện áp cực đại U₀ giữa hai cực của ổ cắm điện là:",
        ["220 V", "110√2 V", "220√2 V (≈ 311 V)", "440 V"],
        2,
        "Một động cơ điện xoay chiều một pha khi hoạt động bình thường ở điện áp hiệu dụng U = 220 V thì tiêu thụ công suất điện P = 1,76 kW và có hệ số công suất cos φ = 0,8. Biết điện trở thuần của cuộn dây động cơ là R = 5 Ω. Hãy tính cường độ dòng điện hiệu dụng I chạy qua động cơ và hiệu suất H của động cơ (coi hao phí chỉ do tỏa nhiệt trên R).",
        "Đổi P = 1 760 W. Từ P = U · I · cos φ ⇒ cường độ dòng điện hiệu dụng là: I = P / (U · cos φ) = 1760 / (220 · 0,8) = 10 (A). Công suất tỏa nhiệt hao phí trên cuộn dây: P_hp = I² · R = 10² · 5 = 500 (W). Công suất cơ học có ích: P_ích = P − P_hp = 1760 − 500 = 1 260 (W). Hiệu suất động cơ: H = (P_ích / P) × 100% = (1260 / 1760) × 100% ≈ 71,59%.",
        game_title="Thử thách thực tế: Dòng điện xoay chiều",
        game_description="Bật tải xoay chiều → theo dõi U, I hiệu dụng và cos φ → tối ưu hóa công suất.",
    ),
    P(
        12,
        "mach-rlc",
        "Mạch điện xoay chiều RLC mắc nối tiếp & Hiện tượng Cộng hưởng điện",
        "📻",
        "Làm chủ cảm kháng Z_L = ωL, dung kháng Z_C = 1/(ωC), tổng trở Z = √[R² + (Z_L − Z_C)²] và điều kiện cộng hưởng điện ω₀ = 1/√(LC).",
        "Đoạn mạch xoay chiều gồm điện trở thuần R, cuộn cảm thuần có độ tự cảm L và tụ điện có điện dung C mắc nối tiếp có tổng trở Z phụ thuộc vào tần số góc ω của dòng điện.",
        "• Trên từng phần tử đơn lẻ: Điện áp u_R cùng pha với i; Điện áp u_L sớm pha π/2 so với i (cảm kháng Z_L = ωL); Điện áp u_C trễ pha π/2 so với i (dung kháng Z_C = 1/(ωC)).\n"
        "• Định luật Ohm cho đoạn mạch RLC nối tiếp: I = U / Z = U₀ / Z, với tổng trở Z = √[ R² + (Z_L − Z_C)² ] và điện áp hiệu dụng U = √[ U_R² + (U_L − U_C)² ].\n"
        "• Độ lệch pha φ giữa u và i: tan φ = (Z_L − Z_C) / R = (U_L − U_C) / U_R; hệ số công suất cos φ = R / Z = U_R / U.\n"
        "• Hiện tượng Cộng hưởng điện: Xảy ra khi Z_L = Z_C ⇔ ω = ω₀ = 1 / √(LC). Khi đó: Z_min = R, I_max = U/R, φ = 0 (u và i cùng pha), cos φ = 1, P_max = U²/R và U_R_max = U (trong khi U_L = U_C).",
        [
            {
                "category": "I. Cảm kháng (Z_L), Dung kháng (Z_C), Tổng trở (Z) & Độ lệch pha φ",
                "items": [
                    {"name": "Cảm kháng Z_L & Dung kháng Z_C", "formula": "Z_L = ω · L = 2πf · L (Ω)  ;  Z_C = 1 / (ω · C) = 1 / (2πf · C) (Ω)", "note": ""},
                    {"name": "Tổng trở Z & Điện áp hiệu dụng U", "formula": "Z = √[ R² + (Z_L − Z_C)² ]  ;  U = √[ U_R² + (U_L − U_C)² ]  ;  I = U / Z", "note": "Lưu ý: U KHÔNG bằng U_R + U_L + U_C do lệch pha!"},
                    {"name": "Độ lệch pha φ & Hệ số công suất cos φ", "formula": "tan φ = (Z_L − Z_C) / R = (U_L − U_C) / U_R  ;  cos φ = R / Z = U_R / U", "note": "Z_L > Z_C: tính cảm kháng (φ > 0) ; Z_L < Z_C: tính dung kháng (φ < 0)"},
                ],
            },
            {
                "category": "II. Hiện tượng Cộng hưởng điện trong mạch RLC nối tiếp",
                "items": [
                    {"name": "Điều kiện xảy ra Cộng hưởng điện", "formula": "Z_L = Z_C  ⇔  ω₀ = 1 / √(L · C)  ⇔  f₀ = 1 / [2π√(L · C)]", "note": ""},
                    {"name": "Các hệ quả cực trị khi Cộng hưởng", "formula": "Z_min = R  ;  I_max = U / R  ;  cos φ = 1 (φ = 0)  ;  P_max = U² / R  ;  U_R = U (và U_L = U_C)", "note": ""},
                ],
            },
        ],
        "Ứng dụng trong mạch chọn sóng thu thanh Radio, truyền hình, bộ lọc tần số âm thanh và mạch sạc cảm ứng cộng hưởng.",
        "Quét tần số góc ω hoặc điều chỉnh tụ xoay C để bắt trúng tần số cộng hưởng của đài phát thanh.",
        "Cho đoạn mạch RLC mắc nối tiếp gồm điện trở thuần R = 40 Ω, cuộn cảm thuần có L = 0,8/π (H) và tụ điện có C = 10⁻³ / (5π) (F). Đặt vào hai đầu đoạn mạch điện áp u = 120√2 cos(100πt) (V). Tính Z_L, Z_C, tổng trở Z, cường độ hiệu dụng I, công suất tiêu thụ P và viết biểu thức cường độ dòng điện i.",
        "Với ω = 100π rad/s: Z_L = ωL = 100π · (0,8/π) = 80 (Ω); Z_C = 1/(ωC) = 1 / [100π · 10⁻³/(5π)] = 50 (Ω). Tổng trở: Z = √[40² + (80 − 50)²] = √(40² + 30²) = 50 (Ω). Dòng hiệu dụng: I = U / Z = 120 / 50 = 2,4 (A) (⇒ I₀ = 2,4√2 A). Công suất: P = I² · R = (2,4)² · 40 = 230,4 (W). Độ lệch pha: tan φ = (80 − 50)/40 = 3/4 ⇒ φ ≈ +0,6435 rad (36,87°). Vì φ_u = 0 nên φ_i = −φ ≈ −0,6435 rad ⇒ i = 2,4√2 cos(100πt − 0,6435) (A).",
        "Đặt vào hai đầu đoạn mạch RLC nối tiếp một điện áp xoay chiều có U = 100 V không đổi. Biết R = 50 Ω. Khi thay đổi tần số góc ω để trong mạch xảy ra hiện tượng CỘNG HƯỞNG ĐIỆN thì công suất tiêu thụ P_max của đoạn mạch khi đó là:",
        ["100 W", "200 W", "50 W", "400 W"],
        1,
        "Đặt vào hai đầu đoạn mạch RLC nối tiếp một điện áp xoay chiều thì đo được điện áp hiệu dụng trên các phần tử lần lượt là: U_R = 60 V, U_L = 120 V và U_C = 40 V. Hãy tính điện áp hiệu dụng U ở hai đầu cả đoạn mạch và hệ số công suất cos φ của mạch.",
        "Áp dụng công thức cộng vectơ điện áp: U = √[ U_R² + (U_L − U_C)² ] = √[ 60² + (120 − 40)² ] = √(60² + 80²) = 100 (V). Hệ số công suất của mạch là: cos φ = U_R / U = 60 / 100 = 0,6.",
        game_title="Thử thách thực tế: Mạch RLC & Cộng hưởng",
        game_description="Quét tần số f → theo dõi đồ thị I(f) và P(f) → bắt đỉnh cộng hưởng điện.",
    ),
    P(
        12,
        "quang-dien",
        "Lượng tử Ánh sáng (Photon), Hiện tượng Quang điện & Mẫu nguyên tử Bohr",
        "☀️",
        "Nắm vững thuyết lượng tử Planck E = hf = hc/λ, công thức Einstein về hiện tượng quang điện và tiên đề Bohr về quang phổ nguyên tử hiđrô.",
        "Theo thuyết lượng tử ánh sáng của Planck và Einstein, chùm ánh sáng là một chùm các hạt (lượng tử ánh sáng) gọi là photon. Mỗi photon mang một năng lượng xác định ε = h · f = (h · c) / λ.",
        "• Hằng số Planck: h ≈ 6,625 · 10⁻³⁴ J·s ; tốc độ ánh sáng trong chân không: c = 3 · 10⁸ m/s ⇒ h · c ≈ 1,9875 · 10⁻²⁵ J·m.\n"
        "• Hiện tượng quang điện ngoài: Ánh sáng làm bật các electron ra khỏi bề mặt kim loại. Điều kiện xảy ra hiện tượng quang điện là bước sóng ánh sáng kích thích phải nhỏ hơn hoặc bằng giới hạn quang điện λ₀ của kim loại đó: λ ≤ λ₀ (hay ε ≥ A, trong đó A = hc/λ₀ là công thoát của kim loại).\n"
        "• Công thức Einstein về hiện tượng quang điện: ε = h · f = A + W_đ0max = A + (1/2)m_e·v₀max² = A + |e|·U_h.\n"
        "• Tiên đề Bohr cho nguyên tử Hiđrô: Bán kính quỹ đạo dừng thứ n là rₙ = n² · r₀ (với r₀ = 5,3 · 10⁻¹¹ m: bán kính Bohr) và năng lượng mức dừng Eₙ = −13,6 / n² (eV); khi nguyên tử chuyển từ mức E_cao xuống E_thấp thì phát ra photon có ε = hf = E_cao − E_thấp.",
        [
            {
                "category": "I. Năng lượng Photon (ε) & Giới hạn Quang điện (λ₀)",
                "items": [
                    {"name": "Năng lượng của 1 photon ánh sáng", "formula": "ε = h · f = (h · c) / λ  (với h = 6,625 · 10⁻³⁴ J·s ; c = 3 · 10⁸ m/s)", "note": "Công suất nguồn sáng phát N photon/giây: P = N · ε"},
                    {"name": "Công thoát A & Giới hạn quang điện λ₀", "formula": "A = (h · c) / λ₀  ;  Điều kiện xảy ra quang điện: λ ≤ λ₀ (hoặc f ≥ f₀)", "note": "Đổi 1 eV = 1,6 · 10⁻¹⁹ J"},
                ],
            },
            {
                "category": "II. Công thức Einstein & Tiên đề Bohr (Nguyên tử Hiđrô)",
                "items": [
                    {"name": "Phương trình Einstein về Hiện tượng quang điện", "formula": "(h · c) / λ = A + W_đ0max = (h · c) / λ₀ + (1/2)m_e · v₀max² = A + |e| · U_h", "note": "U_h: hiệu điện thế hãm"},
                    {"name": "Bán kính quỹ đạo dừng & Năng lượng nguyên tử Hiđrô", "formula": "rₙ = n² · r₀ (n = 1,2,3,4,5,6 ứng với K,L,M,N,O,P)  ;  Eₙ = −13,6 / n² (eV)", "note": "r₀ = 5,3 · 10⁻¹¹ m"},
                    {"name": "Tiên đề Bohr về bức xạ & hấp thụ photon", "formula": "ε = h · f_mn = (h · c) / λ_mn = E_m − E_n  (với m > n)", "note": ""},
                ],
            },
        ],
        "Cơ sở vật lý của tấm pin năng lượng Mặt Trời (quang điện trong), cảm biến ánh sáng tự động bật đèn đường, cáp quang và công nghệ Laser.",
        "Chọn bước sóng ánh sáng chiếu vào tấm kim loại để tạo dòng quang điện và khảo sát phổ vạch nguyên tử Hiđrô.",
        "Công thoát electron của kim loại dùng làm catốt của một tế bào quang điện là A = 2,48 eV. a) Tính giới hạn quang điện λ₀ của kim loại này (theo μm). b) Chiếu vào catốt bức xạ tử ngoại có bước sóng λ = 0,36 μm, hãy tính động năng ban đầu cực đại W_đ0max của các quang electron bứt ra (theo eV).",
        "a) Đổi A = 2,48 · 1,6·10⁻¹⁹ = 3,968 · 10⁻¹⁹ (J). Giới hạn quang điện là: λ₀ = (h · c) / A = (6,625·10⁻³⁴ · 3·10⁸) / (3,968·10⁻¹⁹) ≈ 5,0 · 10⁻⁷ (m) = 0,50 (μm). b) Khi chiếu λ = 0,36 μm < λ₀ (0,50 μm), năng lượng mỗi photon là: ε = (h · c) / λ = (1,9875·10⁻²⁵) / (0,36·10⁻⁶) ≈ 5,521 · 10⁻¹⁹ (J) ≈ 3,45 (eV). Theo công thức Einstein: W_đ0max = ε − A = 3,45 − 2,48 = 0,97 (eV).",
        "Trong nguyên tử hiđrô theo mẫu nguyên tử Bohr, bán kính quỹ đạo dừng K là r₀. Khi electron chuyển lên quỹ đạo dừng N (lớp thứ 4: K, L, M, N ứng với n = 4) thì bán kính quỹ đạo của nó là:",
        ["4r₀", "9r₀", "16r₀", "25r₀"],
        2,
        "Một nguồn phát sáng laser công suất P = 10 mW phát ra chùm sáng đơn sắc có bước sóng λ = 0,6625 μm. Hãy tính số photon N mà nguồn laser đó phát ra trong mỗi giây (lấy h = 6,625 · 10⁻³⁴ J·s, c = 3 · 10⁸ m/s).",
        "Năng lượng của 1 photon ánh sáng laser là: ε = (h · c) / λ = (6,625·10⁻³⁴ · 3·10⁸) / (0,6625·10⁻⁶) = 3 · 10⁻¹⁹ (J). Đổi P = 10 mW = 10⁻² W = 10⁻² J/s. Số photon phát ra trong 1 giây là: N = P / ε = 10⁻² / (3 · 10⁻¹⁹) ≈ 3,33 · 10¹⁶ (photon/giây).",
        game_title="Thử thách thực tế: Lượng tử ánh sáng & Quang điện",
        game_description="Thay đổi bước sóng λ → kiểm tra ngưỡng quang điện λ₀ → đo động năng quang electron.",
    ),
    P(
        12,
        "hat-nhan",
        "Cấu tạo Hạt nhân, Độ hụt khối - Năng lượng liên kết, Phản ứng hạt nhân & Định luật Phóng xạ",
        "☢️",
        "Tính độ hụt khối Δm, năng lượng liên kết W_lk = Δm·c², các định luật bảo toàn trong phản ứng hạt nhân và định luật phóng xạ N = N₀·2^(−t/T).",
        "Hạt nhân nguyên tử ᴬ_Z X được cấu tạo từ Z hạt proton (mang điện +e) và N = A − Z hạt neutron (không mang điện), gọi chung là A hạt nucleon. Các nucleon liên kết chặt chẽ với nhau nhờ lực hạt nhân (tương tác mạnh ở khoảng cách ~10⁻¹⁵ m).",
        "• Độ hụt khối: Khối lượng của một hạt nhân luôn nhỏ hơn tổng khối lượng của các nucleon tạo thành nó: Δm = Z · m_p + (A − Z) · m_n − m_X.\n"
        "• Năng lượng liên kết W_lk = Δm · c² (với 1 amu = 1 u ≈ 931,5 MeV/c²) và Năng lượng liên kết riêng ε_lk = W_lk / A (đặc trưng cho mức độ bền vững của hạt nhân; các hạt nhân trung bình cỡ 50 ≤ A ≤ 80 như ⁵⁶Fe có W_lk/A lớn nhất ≈ 8,8 MeV/nucleon nên bền vững nhất!).\n"
        "• Phản ứng hạt nhân (Phân hạch & Nhiệt hạch): Bảo toàn điện tích (Z₁ + Z₂ = Z₃ + Z₄) và Bảo toàn số khối/số nucleon (A₁ + A₂ = A₃ + A₄); Năng lượng tỏa/thu: ΔE = (m_trước − m_sau) · c².\n"
        "• Định luật phóng xạ (α = ⁴₂He, β⁻ = ⁰₋₁e, β⁺ = ⁰₊₁e, γ): N(t) = N₀ · 2^(−t/T) = N₀ · e^(−λt) và độ phóng xạ H(t) = λ · N(t) (đơn vị Becquerel - Bq).",
        [
            {
                "category": "I. Cấu tạo Hạt nhân ᴬ_Z X, Độ hụt khối (Δm) & Năng lượng liên kết (W_lk)",
                "items": [
                    {"name": "Số proton (Z), số neutron (N) & Bán kính hạt nhân", "formula": "N = A − Z  ;  R ≈ 1,2 · 10⁻¹⁵ · A^(1/3) (m)", "note": "1 u = 1 amu ≈ 1,66055 · 10⁻²⁷ kg ≈ 931,5 MeV/c²"},
                    {"name": "Độ hụt khối Δm & Năng lượng liên kết W_lk", "formula": "Δm = [Z·m_p + (A − Z)·m_n] − m_X  ;  W_lk = Δm · c² = Δm(u) × 931,5 (MeV)", "note": ""},
                    {"name": "Năng lượng liên kết riêng (Độ bền vững hạt nhân)", "formula": "w_lkr = W_lk / A  (MeV/nucleon)", "note": "w_lkr càng lớn thì hạt nhân càng bền vững"},
                ],
            },
            {
                "category": "II. Phản ứng hạt nhân (A₁_Z₁ X₁ + A₂_Z₂ X₂ → A₃_Z₃ X₃ + A₄_Z₄ X₄)",
                "items": [
                    {"name": "Bảo toàn Số nucleon (A) & Điện tích (Z)", "formula": "A₁ + A₂ = A₃ + A₄  ;  Z₁ + Z₂ = Z₃ + Z₄", "note": "Lưu ý: KHÔNG có định luật bảo toàn khối lượng nghỉ trong phản ứng hạt nhân!"},
                    {"name": "Năng lượng phản ứng hạt nhân ΔE", "formula": "ΔE = (m_trước − m_sau) · c² = (W_lk_sau − W_lk_trước) = (W_đ_sau − W_đ_trước)", "note": "ΔE > 0 (m_trước > m_sau): Tỏa năng lượng ; ΔE < 0: Thu năng lượng"},
                ],
            },
            {
                "category": "III. Định luật Phóng xạ (Chu kỳ bán rã T, Hằng số phóng xạ λ = ln 2 / T)",
                "items": [
                    {"name": "Số hạt nhân N(t) & Khối lượng m(t) còn lại sau thời gian t", "formula": "N(t) = N₀ · 2^(−t / T) = N₀ · e^(−λt)  ;  m(t) = m₀ · 2^(−t / T)", "note": ""},
                    {"name": "Số hạt nhân đã bị phân rã (biến thành hạt nhân con)", "formula": "ΔN = N_con = N₀ − N(t) = N₀ · [1 − 2^(−t / T)]", "note": "Tỉ số hạt nhân con và mẹ: N_con / N(t) = 2^(t / T) − 1"},
                    {"name": "Độ phóng xạ H(t) (Số phân rã trong 1 giây, đơn vị Bq)", "formula": "H(t) = λ · N(t) = (ln 2 / T) · N(t) = H₀ · 2^(−t / T)", "note": "T phải đổi ra giây (s) khi tính H = λ·N ; ln 2 ≈ 0,693"},
                ],
            },
        ],
        "Ứng dụng trong nhà máy điện hạt nhân (phân hạch ²³⁵U), nghiên cứu lò phản ứng nhiệt hạch (tokamak), xạ trị ung thư (⁶⁰Co, ¹³¹I) và định tuổi cổ vật bằng đồng vị ¹⁴C.",
        "Quản lý nguồn phóng xạ y học hạt nhân và tính toán chu kỳ bán rã, liều lượng an toàn.",
        "Cho hạt nhân Heli ⁴₂He có khối lượng m_He = 4,0015 u. Biết khối lượng proton m_p = 1,0073 u, khối lượng neutron m_n = 1,0087 u và 1 u = 931,5 MeV/c². Tính độ hụt khối Δm, năng lượng liên kết W_lk và năng lượng liên kết riêng của hạt nhân ⁴₂He.",
        "Hạt nhân ⁴₂He có Z = 2 proton và N = 4 − 2 = 2 neutron. Độ hụt khối: Δm = 2·1,0073 + 2·1,0087 − 4,0015 = 0,0305 (u). Năng lượng liên kết: W_lk = 0,0305 × 931,5 ≈ 28,41 (MeV). Năng lượng liên kết riêng: w_lkr = W_lk / A = 28,41 / 4 ≈ 7,10 (MeV/nucleon).",
        "Đồng vị phóng xạ Iốt ¹³¹₅₃I dùng trong y học có chu kỳ bán rã T = 8 ngày. Nếu ban đầu có m₀ = 160 mg chất phóng xạ này thì sau t = 24 ngày, khối lượng ¹³¹I còn lại chưa bị phân rã là:",
        ["80 mg", "40 mg", "20 mg", "10 mg"],
        2,
        "Khảo cổ học dùng đồng vị cacbon phóng xạ ¹⁴₆C (có chu kỳ bán rã T = 5 730 năm) để xác định niên đại cổ vật. Một mẫu gỗ cổ tìm thấy trong hang động có độ phóng xạ H bằng 25% (1/4) độ phóng xạ H₀ của một mẫu gỗ tươi cùng loại, cùng khối lượng vừa mới chặt. Hãy tính tuổi t của mẫu gỗ cổ đó.",
        "Ta có: H / H₀ = 2^(−t / T) = 25% = 1/4 = 2⁻² ⇒ t / T = 2 ⇒ t = 2 · T = 2 · 5 730 = 11 460 (năm). Vậy mẫu gỗ cổ có niên đại khoảng 11 460 năm.",
        game_title="Thử thách thực tế: Vật lý hạt nhân & Phóng xạ",
        game_description="Khảo sát đường cong phân rã phóng xạ N(t), phản ứng phân hạch/nhiệt hạch và nguyên tắc an toàn bức xạ.",
    ),
    P(
        12,
        "thuyet-tuong-doi",
        "Thuyết tương đối hẹp Einstein, Hệ thức E = mc² & Vật lý hiện đại",
        "🌌",
        "Hiểu hai tiên đề Einstein, sự giãn thời gian, co chiều dài, khối lượng tương đối tính và hệ thức năng lượng - khối lượng E = mc².",
        "Thuyết tương đối hẹp của Albert Einstein (1905) mở rộng cơ học cổ điển Newton cho các vật chuyển động với tốc độ v rất lớn (so sánh được với tốc độ ánh sáng trong chân không c = 3 · 10⁸ m/s), khẳng định không gian và thời gian có tính tương đối, còn tốc độ ánh sáng trong chân không c là tuyệt đối trong mọi hệ quy chiếu quán tính.",
        "• Hai tiên đề của Thuyết tương đối hẹp:\n"
        "  1. Nguyên lý tương đối: Mọi định luật vật lý đều có cùng một dạng như nhau trong mọi hệ quy chiếu quán tính.\n"
        "  2. Nguyên lý bất biến của tốc độ ánh sáng: Tốc độ ánh sáng trong chân không c ≈ 3 · 10⁸ m/s là như nhau theo mọi hướng và trong mọi hệ quy chiếu quán tính, không phụ thuộc vào vận tốc của nguồn sáng hay của máy thu.\n"
        "• Các hệ quả tương đối tính (với hệ số Lorentz γ = 1 / √(1 − v²/c²) ≥ 1): Sự co độ dài (l = l₀ / γ), Sự giãn thời gian (Δt = γ · Δt₀), Khối lượng tương đối tính (m = γ · m₀) và Hệ thức Einstein giữa năng lượng và khối lượng: E = m · c².",
        [
            {
                "category": "I. Hệ số Lorentz γ, Sự co chiều dài & Sự giãn thời gian",
                "items": [
                    {"name": "Hệ số tương đối tính Lorentz (γ ≥ 1)", "formula": "γ = 1 / √(1 − v² / c²)  (với v < c = 3 · 10⁸ m/s)", "note": "Khi v ≪ c thì γ ≈ 1 (trở về cơ học cổ điển Newton)"},
                    {"name": "Sự co chiều dài dọc theo phương chuyển động", "formula": "l = l₀ · √(1 − v² / c²) = l₀ / γ", "note": "l₀ là chiều dài riêng khi vật đứng yên"},
                    {"name": "Sự giãn thời gian (Đồng hồ chuyển động chạy chậm hơn)", "formula": "Δt = Δt₀ / √(1 − v² / c²) = γ · Δt₀", "note": "Δt₀ là khoảng thời gian riêng"},
                ],
            },
            {
                "category": "II. Khối lượng tương đối tính & Hệ thức Einstein E = mc²",
                "items": [
                    {"name": "Khối lượng tương đối tính m & Năng lượng nghỉ E₀", "formula": "m = m₀ / √(1 − v² / c²) = γ · m₀  ;  Năng lượng nghỉ: E₀ = m₀ · c²", "note": "m₀ là khối lượng nghỉ"},
                    {"name": "Năng lượng toàn phần E & Động năng tương đối tính W_đ", "formula": "E = m · c² = E₀ / √(1 − v² / c²)  ;  W_đ = E − E₀ = (m − m₀) · c²", "note": "Hệ thức năng lượng - động lượng: E² = (E₀)² + (p · c)²"},
                ],
            },
        ],
        "Ứng dụng bắt buộc trong việc hiệu chỉnh đồng hồ nguyên tử trên các vệ tinh định vị toàn cầu GPS (nếu không hiệu chỉnh thuyết tương đối, GPS sẽ sai lệch ~10 km mỗi ngày!), máy gia tốc hạt LHC và năng lượng hạt nhân.",
        "Khám phá mô phỏng con tàu vũ trụ bay với vận tốc gần bằng vận tốc ánh sáng c và hiệu chỉnh đồng hồ vệ tinh GPS.",
        "Một hạt sơ cấp chuyển động với tốc độ v = 0,6c (trong đó c = 3 · 10⁸ m/s là tốc độ ánh sáng trong chân không). Tính hệ số Lorentz γ và tỉ số giữa động năng tương đối tính W_đ với năng lượng nghỉ E₀ của hạt đó.",
        "Ta có: √(1 − v²/c²) = √(1 − 0,6²) = √(1 − 0,36) = √0,64 = 0,8 ⇒ hệ số Lorentz γ = 1 / 0,8 = 1,25. Năng lượng toàn phần là E = γ · E₀ = 1,25 E₀. Động năng của hạt là: W_đ = E − E₀ = 1,25 E₀ − E₀ = 0,25 E₀. Vậy tỉ số W_đ / E₀ = 0,25 = 1/4.",
        "Theo hệ thức Einstein E = m·c², nếu 1 gam (m = 10⁻³ kg) vật chất được chuyển hóa hoàn toàn thành năng lượng (với c = 3 · 10⁸ m/s) thì năng lượng giải phóng ra bằng:",
        ["3 · 10⁵ J", "9 · 10¹³ J (90 000 tỷ Joule)", "9 · 10¹⁶ J", "3 · 10¹¹ J"],
        1,
        "Mặt Trời phát ra năng lượng bức xạ với công suất trung bình khổng lồ là P = 3,9 · 10²⁶ W (J/s). Áp dụng hệ thức Einstein E = Δm · c² (với c = 3 · 10⁸ m/s), hãy tính xem trong mỗi giây Mặt Trời bị giảm đi bao nhiêu triệu tấn khối lượng do bức xạ năng lượng?",
        "Trong mỗi giây (t = 1 s), năng lượng bức xạ của Mặt Trời là E = P · t = 3,9 · 10²⁶ (J). Độ giảm khối lượng của Mặt Trời trong mỗi giây là: Δm = E / c² = (3,9 · 10²⁶) / (3 · 10⁸)² = (3,9 · 10²⁶) / (9 · 10¹⁶) ≈ 4,33 · 10⁹ (kg) = 4,33 · 10⁶ (tấn) = 4,33 triệu tấn mỗi giây!",
        game_title="Thử thách thực tế: Vật lý hiện đại & Thuyết tương đối",
        game_description="Tăng vận tốc v tiệm cận c → quan sát sự giãn thời gian, co độ dài và năng lượng E = mc².",
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
        print(f"ĐÃ XỬ LÝ: {len(LESSONS)} BÀI VẬT LÝ LỚP 6–12")
        print(f"TẠO MỚI:  {created}")
        print(f"CẬP NHẬT: {updated}")
        print("=" * 60)

    except Exception as e:
        db.rollback()
        print("\n" + "=" * 60)
        print("LỖI KHI CẬP NHẬT VẬT LÝ:")
        print(e)
        print("=" * 60)
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()