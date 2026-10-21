import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
"""
Nâng cấp toàn diện nội dung Hóa học Lớp 6–12 (Chương trình GDPT 2018 - Danh pháp IUPAC).
Tổng cộng: 49 bài học (7 lớp × 7 chuyên đề/lớp), bao gồm:
- 42 bài học cốt lõi ban đầu (được nâng cấp đầy đủ lý thuyết, hệ thống công thức phân nhóm, ví dụ, trắc nghiệm, thử thách và mô phỏng).
- 7 chuyên đề bổ sung mới lấp đầy chương trình Hóa học / KHTN GDPT 2018:
  + Lớp 6: oxygen-khong-khi (Oxygen, Không khí & Sự cháy)
  + Lớp 7: hoa-tri-lien-ket (Hóa trị, Công thức hóa học & Liên kết Ion - Cộng hóa trị)
  + Lớp 8: oxide-phan-bon (Phân loại Oxide & Phân bón hóa học N - P - K)
  + Lớp 9: dan-xuat-hydrocarbon-lop-9 (Ethylic Alcohol, Acetic Acid, Chất béo & Carbohydrate cơ bản)
  + Lớp 10: nhom-halogen (Nguyên tố nhóm Halogen VIIA, Hydrogen Halide & Muối Halide)
  + Lớp 11: dan-xuat-alcohol-carbonyl-acid (Dẫn xuất Halogen, Alcohol - Phenol, Hợp chất Carbonyl & Carboxylic Acid)
  + Lớp 12: dai-cuong-kim-loai-phuc-chat (Đại cương Kim loại, Điện phân Faraday, Ăn mòn điện hóa, Nhóm IA-IIA & Phức chất)

Chạy từ thư mục backend:
    python upgrade_chemistry.py
"""

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject

SUBJECT_SLUG = "chemistry"
SUBJECT_NAME = "Hóa học"


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


def C(
    grade,
    topic,
    title,
    icon,
    description,
    context_title,
    context,
    definition,
    concept,
    formulas,
    example,
    example_answer,
    question,
    answers,
    correct,
    application,
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
        "context_title": context_title.strip(),
        "context": context.strip(),
        "definition": definition.strip(),
        "concept": concept.strip(),
        "formulas": formulas,
        "meaning": application.strip(),
        "real_life": context.strip(),
        "theory": f"{definition.strip()}\n\n{concept.strip()}",
        "formula": format_formulas_text(formulas),
        "example": example.strip(),
        "example_answer": example_answer.strip(),
        "question": question.strip(),
        "answers": answers,
        "correct": correct,
        "application": application.strip(),
        "challenge": challenge.strip(),
        "challenge_answer": challenge_answer.strip(),
        "game_title": game_title or f"Phòng thí nghiệm ảo: {title}",
        "game_description": game_description
        or f"Thực hành thí nghiệm và khám phá {title.lower()} trong thực tế.",
        "game_type": game_type,
    }


LESSONS = [
    # =========================================================
    # HÓA HỌC LỚP 6 (7 BÀI)
    # =========================================================
    C(
        6,
        "chat-va-vat-lieu",
        "Chất, Vật thể & Tính chất của Vật liệu quanh ta",
        "🧪",
        "Phân biệt chất, vật thể tự nhiên - nhân tạo, vật hữu sinh - vô sinh và tính chất vật lý, tính chất hóa học.",
        "Từ chiếc cốc đến chiếc bàn",
        "Mọi vật thể xung quanh chúng ta đều được cấu tạo từ một hay nhiều chất. Một chiếc cốc có thể làm bằng thủy tinh, nhựa hoặc thép không gỉ tùy mục đích sử dụng.",
        "Vật thể là những đối tượng tồn tại xung quanh ta hoặc trong không gian; Chất là thành phần cấu tạo nên vật thể (ở đâu có vật thể là ở đó có chất). Vật liệu là một chất hoặc hỗn hợp một số chất được con người sử dụng làm nguyên liệu đầu vào để sản xuất đồ vật.",
        "• Phân loại vật thể: Vật thể tự nhiên (có sẵn trong tự nhiên như đá, cây, nước sông) và Vật thể nhân tạo (do con người tạo ra như bàn ghế, xe đạp); Vật hữu sinh (có đặc trưng sống) và Vật vô sinh.\n"
        "• Tính chất vật lý: trạng thái (rắn, lỏng, khí), màu sắc, mùi vị, tính tan, nhiệt độ nóng chảy, nhiệt độ sôi, tính dẫn điện, dẫn nhiệt, khối lượng riêng (quan sát/đo được mà KHÔNG có sự tạo thành chất mới).\n"
        "• Tính chất hóa học: khả năng biến đổi thành chất khác (khả năng cháy, bị phân hủy, bị gỉ sét/ăn mòn).\n"
        "• Tính chất và ứng dụng của các vật liệu phổ biến: Kim loại, Nhựa, Gỗ, Thủy tinh, Gốm, Cao su.",
        [
            {
                "category": "I. Mối quan hệ Vật thể – Vật liệu – Chất",
                "items": [
                    {"name": "Sơ đồ cấu tạo", "formula": "Chất (Fe, C, H₂O, cellulose...) → Vật liệu (Thép, Gỗ, Thủy tinh...) → Vật thể (Cây cầu, Cái bàn, Cốc nước...)", "note": ""},
                    {"name": "Khối lượng riêng đặc trưng cho chất", "formula": "ρ = D = m / V  (g/cm³ hoặc kg/m³)", "note": "Nước nguyên chất ở 4°C có ρ = 1 g/cm³"},
                ],
            },
            {
                "category": "II. Phân biệt Tính chất Vật lý & Tính chất Hóa học",
                "items": [
                    {"name": "Tính chất Vật lý", "formula": "Không tạo ra chất mới (Nóng chảy, sôi, dẫn điện, dẫn nhiệt, hòa tan...)", "note": ""},
                    {"name": "Tính chất Hóa học", "formula": "Có sự biến đổi tạo ra CHẤT MỚI (Than cháy tạo CO₂, sắt gỉ tạo iron oxide...)", "note": ""},
                ],
            },
        ],
        "Một khối kim loại có khối lượng 270 g và thể tích 100 cm³. Tính khối lượng riêng của kim loại đó và cho biết đó là kim loại gì (biết D_Al = 2,7 g/cm³; D_Fe = 7,8 g/cm³).",
        "Khối lượng riêng của khối kim loại là: ρ = m / V = 270 / 100 = 2,7 (g/cm³). Vậy kim loại đó là nhôm (Aluminium - Al).",
        "Hiện tượng nào dưới đây thể hiện TÍNH CHẤT HÓA HỌC của chất?",
        [
            "Nước lỏng đông đặc thành nước đá ở 0°C",
            "Đinh sắt để lâu ngoài không khí ẩm bị phủ lớp gỉ màu nâu đỏ",
            "Dây đồng dẫn điện tốt và có màu đỏ",
            "Đường ăn tan hoàn toàn trong nước ấm",
        ],
        1,
        "Lựa chọn đúng vật liệu làm nồi nấu, dây dẫn điện, lốp xe, cửa kính giúp đảm bảo độ bền, an toàn và hướng tới sử dụng vật liệu xanh (3R: Reduce – Reuse – Recycle).",
        "Giải thích vì sao dây dẫn điện gia dụng thường có lõi làm bằng đồng (copper) và vỏ bọc ngoài làm bằng nhựa PVC hoặc cao su?",
        "Vì đồng là kim loại dẫn điện rất tốt giúp truyền tải dòng điện hiệu quả, còn nhựa PVC/cao su là vật liệu cách điện và không thấm nước giúp bảo vệ người sử dụng khỏi bị điện giật.",
    ),
    C(
        6,
        "trang-thai-chat",
        "Ba thể cơ bản của Chất (Rắn - Lỏng - Khí) & Sự chuyển thể",
        "💧",
        "So sánh cấu trúc hạt của thể rắn, lỏng, khí và nắm vững 6 quá trình chuyển thể (nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ).",
        "Vòng tuần hoàn của nước trong tự nhiên",
        "Nước đá trong tủ lạnh, nước uống hàng ngày và hơi nước bốc lên từ nồi canh đều là cùng một chất (H₂O) nhưng tồn tại ở ba thể vật lý khác nhau.",
        "Mọi chất đều được cấu tạo từ những hạt vô cùng nhỏ bé. Tùy thuộc vào khoảng cách và lực liên kết giữa các hạt mà chất tồn tại ở ba thể cơ bản: Rắn (Solid - s), Lỏng (Liquid - l) và Khí/Hơi (Gas/Vapor - g).",
        "• Thể rắn: các hạt liên kết rất chặt chẽ, chỉ dao động quanh vị trí cố định ⇒ Có hình dạng và thể tích xác định, rất khó bị nén.\n"
        "• Thể lỏng: các hạt liên kết kém chặt hơn, trượt lên nhau được ⇒ Không có hình dạng riêng (lấy hình dạng phần bình chứa), nhưng có thể tích xác định, khó bị nén.\n"
        "• Thể khí: các hạt ở rất xa nhau, chuyển động hỗn độn về mọi phía ⇒ Không có hình dạng và thể tích riêng (chiếm toàn bộ thể tích bình chứa), rất dễ bị nén.\n"
        "• Sự chuyển thể: Nóng chảy (rắn → lỏng), Đông đặc (lỏng → rắn), Sự hóa hơi gồm Bay hơi (trên mặt thoáng ở mọi nhiệt độ) và Sôi (cả trên mặt thoáng và trong lòng chất lỏng ở nhiệt độ sôi xác định), Ngưng tụ (khí → lỏng).",
        [
            {
                "category": "I. So sánh đặc điểm 3 thể của chất (Mô hình hạt)",
                "items": [
                    {"name": "Thể rắn (s)", "formula": "Lực liên kết hạt rất mạnh ; Hình dạng xác định ; Thể tích xác định ; Không nén được", "note": ""},
                    {"name": "Thể lỏng (l)", "formula": "Lực liên kết trung bình ; Hình dạng theo bình chứa ; Thể tích xác định ; Khó nén", "note": ""},
                    {"name": "Thể khí / hơi (g)", "formula": "Khoảng cách hạt rất lớn ; Không có hình dạng & thể tích riêng ; Rất dễ bị nén", "note": ""},
                ],
            },
            {
                "category": "II. Các quá trình Chuyển thể & Đặc điểm nhiệt độ",
                "items": [
                    {"name": "Nóng chảy ⇄ Đông đặc", "formula": "Rắn ⇄ Lỏng  (Với chất kết tinh: diễn ra ở nhiệt độ nóng chảy xác định t_nc)", "note": "Nước đá nóng chảy / đông đặc ở 0°C (1 atm)"},
                    {"name": "Hóa hơi (Bay hơi & Sôi) ⇄ Ngưng tụ", "formula": "Lỏng ⇄ Khí (Hơi)  (Sự sôi diễn ra ở nhiệt độ sôi xác định t_s)", "note": "Trong suốt thời gian đang nóng chảy hoặc đang sôi, nhiệt độ của chất KHÔNG ĐỔI"},
                ],
            },
        ],
        "Khi đun sôi nước ở áp suất chuẩn (100°C), nếu ta tiếp tục đun mạnh hơn thì nhiệt độ của nước đang sôi có vượt quá 100°C không? Quá trình chuyển thể nào đang diễn ra?",
        "Nhiệt độ của nước vẫn giữ nguyên ở 100°C trong suốt thời gian nước đang sôi (nhiệt cung cấp dùng để chuyển nước lỏng thành hơi nước). Quá trình đó là sự sôi (hóa hơi).",
        "Hiện tượng nào dưới đây là sự NGƯNG TỤ?",
        [
            "Viên nước đá để ngoài cốc tan dần thành nước lỏng",
            "Quần áo ướt phơi ngoài nắng khô nhanh",
            "Hơi nước trong không khí ban đêm gặp lá cây lạnh tạo thành các giọt sương đọng trên lá",
            "Đun nước trong ấm đến 100°C thấy bọt khí nổi lên từ đáy ấm",
        ],
        2,
        "Ứng dụng trong đúc kim loại (nóng chảy – đông đặc), làm muối từ nước biển (bay hơi), chưng cất tinh dầu (sôi – ngưng tụ) và nén khí LPG vào bình gas.",
        "Tại sao khi mở nắp nồi canh đang nóng, ta thấy có nhiều giọt nước đọng ở mặt dưới của nắp nồi? Còn khi hà hơi vào mặt gương lạnh vào mùa đông thì mặt gương bị mờ đi?",
        "Do hơi nước nóng bốc lên từ nồi canh (hoặc từ hơi thở) khi gặp nắp nồi / mặt gương có nhiệt độ thấp hơn đã bị lạnh đi và NGƯNG TỤ thành các hạt nước nhỏ li ti.",
    ),
    C(
        6,
        "oxygen-khong-khi",
        "Oxygen (O₂) & Thành phần Không khí – Sự cháy và Bảo vệ môi trường không khí",
        "🌬️",
        "Nắm vững tính chất của khí Oxygen (duy trì sự sống và sự cháy), thành phần phần trăm thể tích không khí và cách dập tắt đám cháy.",
        "Hơi thở của sự sống và ngọn lửa",
        "Con người có thể nhịn ăn nhiều ngày nhưng không thể nhịn thở quá vài phút vì tế bào luôn cần khí Oxygen. Không khí bao quanh Trái Đất là một hỗn hợp khí có tỷ lệ xác định.",
        "Oxygen (O₂) là chất khí không màu, không mùi, không vị, nặng hơn không khí một chút và ít tan trong nước; có vai trò quyết định đối với sự hô hấp của sinh vật và sự cháy của nhiên liệu.",
        "• Tính chất vật lý của Oxygen: ở điều kiện thường là chất khí không màu, không mùi, không vị, hóa lỏng ở −183°C (oxygen lỏng có màu xanh nhạt), ít tan trong nước (1 lít nước ở 20°C, 1 atm hòa tan khoảng 31 mL khí O₂).\n"
        "• Thành phần của không khí khô theo thể tích: khoảng 78% khí Nitrogen (N₂), 21% khí Oxygen (O₂), khoảng 1% các khí khác (Carbon dioxide CO₂ ~0,04%, khí hiếm Argon Ar, hơi nước, bụi...).\n"
        "• Điều kiện phát sinh sự cháy (Tam giác lửa: Chất cháy + Oxygen + Nguồn nhiệt đạt tới nhiệt độ bắt cháy) và nguyên tắc dập tắt đám cháy.",
        [
            {
                "category": "I. Thành phần phần trăm thể tích của Không khí",
                "items": [
                    {"name": "Tỉ lệ thể tích các khí trong không khí", "formula": "V_N₂ ≈ 78%  ;  V_O₂ ≈ 21% (≈ 1/5 V_không_khí)  ;  Khí khác (Ar, CO₂, hơi nước...) ≈ 1%", "note": "Tỉ lệ gần đúng: V_không_khí ≈ 5 · V_O₂"},
                ],
            },
            {
                "category": "II. Tam giác cháy & Nguyên tắc dập tắt đám cháy",
                "items": [
                    {"name": "3 điều kiện cần và đủ cho sự cháy", "formula": "1) Có chất cháy (nhiên liệu) + 2) Có đủ khí Oxygen + 3) Nhiệt độ đạt tới nhiệt độ bắt cháy", "note": "Nếu nồng độ O₂ giảm xuống dưới ~14% thì hầu hết sự cháy dừng lại"},
                    {"name": "2 biện pháp dập tắt đám cháy", "formula": "1) Hạ nhiệt độ chất cháy xuống dưới nhiệt độ bắt cháy VÀ/HOẶC 2) Cách ly chất cháy khỏi khí Oxygen", "note": "Lưu ý: Đám cháy xăng dầu hoặc điện KHÔNG được phun nước trực tiếp!"},
                ],
            },
        ],
        "Một căn phòng học có chiều dài 8 m, chiều rộng 6 m và chiều cao 3,5 m. Hãy tính thể tích không khí trong phòng và thể tích khí Oxygen có trong phòng (biết Oxygen chiếm 21% thể tích không khí).",
        "Thể tích không khí trong phòng là: V_kk = 8 · 6 · 3,5 = 168 (m³) = 168 000 (lít). Thể tích khí Oxygen có trong phòng là: V_O2 = 168 · 21% = 35,28 (m³) = 35 280 (lít).",
        "Khí nào chiếm tỉ lệ thể tích lớn nhất (khoảng 78%) trong không khí tự nhiên?",
        [
            "Oxygen (O₂)",
            "Carbon dioxide (CO₂)",
            "Nitrogen (N₂)",
            "Hydrogen (H₂)",
        ],
        2,
        "Cung cấp bình thở oxygen y tế, thợ lặn, phi công; lắp đặt hệ thống sục khí cho đầm nuôi tôm cá và phòng cháy chữa cháy.",
        "Tại sao khi xảy ra đám cháy do xăng, dầu hỏa hoặc cồn bị đổ ra sàn, tuyệt đối KHÔNG ĐƯỢC dùng nước để dập lửa mà phải dùng cát, chăn chiên ướt hoặc bình chữa cháy bột/khí CO₂?",
        "Vì xăng và dầu hỏa không tan trong nước và nhẹ hơn nước (D_xăng ≈ 0,7 g/cm³ < D_nước = 1 g/cm³). Nếu tạt nước vào, xăng dầu sẽ nổi lên trên mặt nước và loang rộng ra xung quanh khiến đám cháy bùng phát dữ dội hơn. Dùng cát hoặc chăn ướt phủ kín sẽ ngăn xăng dầu tiếp xúc với khí Oxygen trong không khí làm lửa tắt ngay.",
    ),
    C(
        6,
        "hon-hop",
        "Chất tinh khiết, Hỗn hợp (Đồng nhất - Không đồng nhất) & Các phương pháp Tách chất",
        "⚗️",
        "Phân biệt chất tinh khiết với hỗn hợp, huyền phù - nhũ tương và lựa chọn phương pháp Lọc, Cô cạn, Chiết, Chưng cất phù hợp.",
        "Từ nước biển đến hạt muối trắng",
        "Nước biển chứa nước và nhiều muối khoáng hòa tan. Làm thế nào để tách riêng được muối ăn tinh khiết hoặc tách dầu ăn bị lẫn vào nước?",
        "Chất tinh khiết (chất nguyên chất) chỉ tạo ra từ một chất duy nhất nên có tính chất vật lý và hóa học hoàn toàn xác định. Hỗn hợp gồm từ hai chất trở lên trộn lẫn vào nhau mà không xảy ra phản ứng hóa học.",
        "• Hỗn hợp đồng nhất (có thành phần giống nhau tại mọi vị trí trong toàn bộ hỗn hợp — gọi là dung dịch, như nước đường, nước muối lọc trong, không khí sạch).\n"
        "• Hỗn hợp không đồng nhất: thành phần không giống nhau trong toàn bộ hỗn hợp, gồm Huyền phù (các hạt chất rắn lơ lửng trong chất lỏng như nước phù sa, nước bột sắn dây sống) và Nhũ tương (các giọt chất lỏng lơ lửng trong chất lỏng khác không tan vào nhau như dầu ăn lắc với nước, sữa tươi, sốt mayonnaise).\n"
        "• Các phương pháp vật lý tách chất ra khỏi hỗn hợp: Lắng – gạn – lọc, Cô cạn (bay hơi), Chiết (dùng phễu chiết) và Chưng cất.",
        [
            {
                "category": "I. Phân loại Chất tinh khiết & Hỗn hợp",
                "items": [
                    {"name": "Chất tinh khiết (1 chất duy nhất)", "formula": "Có t_nóng_chảy, t_sôi và khối lượng riêng ρ XÁC ĐỊNH KHÔNG ĐỔI", "note": "Ví dụ: Nước cất sôi đúng ở 100°C (1 atm)"},
                    {"name": "Hỗn hợp đồng nhất (Dung dịch)", "formula": "Chất tan + Dung môi phân bố đồng đều mọi vị trí", "note": "Ví dụ: Nước đường, nước muối, cồn y tế"},
                    {"name": "Huyền phù & Nhũ tương (Hỗn hợp không đồng nhất)", "formula": "Huyền phù: Rắn lơ lửng trong Lỏng  ;  Nhũ tương: Lỏng lơ lửng trong Lỏng", "note": ""},
                ],
            },
            {
                "category": "II. Nguyên tắc lựa chọn Phương pháp Tách chất",
                "items": [
                    {"name": "1. Phương pháp LỌC (qua phễu và giấy lọc)", "formula": "Tách chất RẮN KHÔNG TAN ra khỏi chất lỏng (hoặc chất khí)", "note": "Ví dụ: Tách cát ra khỏi nước, lọc bụi không khí"},
                    {"name": "2. Phương pháp CÔ CẠN (Bay hơi)", "formula": "Tách chất RẮN TAN (không bay hơi ở nhiệt độ cao) ra khỏi dung dịch", "note": "Ví dụ: Cô cạn nước muối thu muối ăn NaCl"},
                    {"name": "3. Phương pháp CHIẾT (Phễu chiết)", "formula": "Tách hai chất LỎNG KHÔNG TAN VÀO NHAU và có khối lượng riêng khác nhau (tách thành 2 lớp)", "note": "Ví dụ: Tách dầu ăn và nước ; tách tinh dầu sả và nước"},
                    {"name": "4. Phương pháp CHƯNG CẤT / DÙNG NAM CHÂM", "formula": "Chưng cất: Tách các chất lỏng tan vào nhau có nhiệt độ sôi khác nhau ; Nam châm: tách sắt", "note": ""},
                ],
            },
        ],
        "Cho hỗn hợp gồm dầu ăn và nước. Khi để yên trong bình thủy tinh, hiện tượng gì xảy ra? Cần dùng dụng cụ và phương pháp nào để tách riêng dầu ăn và nước?",
        "Vì dầu ăn không tan trong nước và nhẹ hơn nước (D_dầu ≈ 0,8 g/cm³ < D_nước = 1 g/cm³) nên hỗn hợp tách thành 2 lớp: dầu ăn nổi ở lớp trên, nước ở lớp dưới. Ta dùng PHỄU CHIẾT (phương pháp chiết), mở khóa phễu cho lớp nước phía dưới chảy ra hết rồi đóng khóa lại để thu dầu ăn ở trên.",
        "Hỗn hợp nào dưới đây được gọi là một NHŨ TƯƠNG?",
        [
            "Nước muối sinh lý",
            "Nước sông Hồng đục ngầu phù sa",
            "Hỗn hợp dầu ăn và giấm ăn (hoặc nước) được lắc mạnh",
            "Nước đường pha loãng",
        ],
        2,
        "Hệ thống lọc nước sạch sinh hoạt, sản xuất muối biển, chiết xuất tinh dầu thiên nhiên và phân loại rác tái chế.",
        "Trình bày quy trình chi tiết gồm 4 bước để tách riêng từng chất nguyên chất ra khỏi hỗn hợp rắn gồm: mạt sắt (Fe), bột cát (SiO₂), muối ăn (NaCl) và bột lưu huỳnh (Sulfur - S, biết bột lưu huỳnh không tan trong nước và nhẹ nổi trên mặt nước hoặc tách sau cát).",
        "Quy trình chuẩn cho hỗn hợp (mạt sắt, cát, muối ăn): Bước 1: Dùng nam châm đưa lại gần hỗn hợp để hút tách hết mạt sắt. Bước 2: Cho hỗn hợp còn lại (cát và muối ăn) vào cốc nước và khuấy đều, muối ăn tan hết còn cát không tan lắng xuống đáy. Bước 3: Đổ hỗn hợp qua phễu có đặt giấy lọc (phương pháp lọc), phần giữ lại trên giấy lọc đem sấy khô thu được cát sạch. Bước 4: Đem phần nước lọc trong suốt đi đun nóng (phương pháp cô cạn), nước bay hơi hết thu được muối ăn kết tinh ở đáy bát sứ.",
    ),
    C(
        6,
        "dung-dich",
        "Dung dịch, Dung môi, Chất tan, Độ tan (S) & Nồng độ phần trăm cơ bản",
        "🥤",
        "Xác định chất tan - dung môi, phân biệt dung dịch bão hòa và chưa bão hòa, tính độ tan S và các yếu tố làm tăng tốc độ hòa tan.",
        "Bí quyết pha chế đồ uống chuẩn vị",
        "Khi pha một ly nước đường, tại sao dùng đường cát mịn pha với nước ấm và khuấy đều thì đường lại tan nhanh hơn rất nhiều so với để nguyên viên đường phèn trong nước lạnh?",
        "Dung dịch là hỗn hợp đồng nhất của dung môi và chất tan. Ở nhiệt độ và áp suất xác định, dung dịch không thể hòa tan thêm chất tan được nữa gọi là dung dịch bão hòa; dung dịch còn có thể hòa tan thêm chất tan gọi là dung dịch chưa bão hòa.",
        "• Dung môi thường là nước (ngoài ra có dung môi hữu cơ như cồn ethanol, xăng, acetone để hòa tan dầu mỡ, sơn móng tay).\n"
        "• Ba cách làm cho chất rắn tan NHANH HƠN trong nước: 1) Khuấy đều dung dịch; 2) Đun nóng dung dịch; 3) Nghiền nhỏ chất rắn.\n"
        "• Độ tan (S) của một chất trong nước là số gam chất đó hòa tan tối đa trong 100 gam nước để tạo thành dung dịch bão hòa ở một nhiệt độ xác định. Đa số chất rắn có độ tan tăng khi nhiệt độ tăng; còn chất khí (như CO₂ trong nước ngọt có gas, O₂ trong nước) có độ tan GIẢM khi nhiệt độ tăng và khi áp suất giảm.",
        [
            {
                "category": "I. Khối lượng Dung dịch, Độ tan (S) & Nồng độ phần trăm (C%)",
                "items": [
                    {"name": "Bảo toàn khối lượng khi pha dung dịch", "formula": "m_dung_dịch = m_chất_tan + m_dung_môi (m_dd = m_ct + m_H₂O)", "note": "Lưu ý: Thể tích dung dịch có thể hơi hụt so với tổng thể tích, nhưng KHỐI LƯỢNG luôn cộng bảo toàn!"},
                    {"name": "Công thức tính Độ tan S (ở nhiệt độ t°C)", "formula": "S = (m_ct / m_H₂O) × 100  (đơn vị: g chất tan / 100 g H₂O)", "note": "Áp dụng cho dung dịch BÃO HÒA ở t°C"},
                    {"name": "Công thức tính Nồng độ phần trăm C%", "formula": "C% = (m_ct / m_dd) × 100%  ⇒  m_ct = (m_dd · C%) / 100%", "note": "Với dung dịch bão hòa: C%_bh = [S / (100 + S)] × 100%"},
                ],
            },
            {
                "category": "II. Các yếu tố ảnh hưởng đến Tốc độ hòa tan & Độ tan",
                "items": [
                    {"name": "Tăng tốc độ hòa tan chất rắn", "formula": "Nghiền nhỏ (tăng diện tích tiếp xúc) + Khuấy trộn + Đun nóng", "note": ""},
                    {"name": "Độ tan của Chất khí (O₂, CO₂) trong nước", "formula": "Tăng khi Nhiệt độ GIẢM và Áp suất TĂNG", "note": "Lý do lon nước ngọt có gas ướp lạnh và đóng nắp kín giữ được nhiều gas CO₂"},
                ],
            },
        ],
        "Ở 20°C, hòa tan tối đa được 36 gam muối ăn (NaCl) vào 100 gam nước thì thu được dung dịch bão hòa. Tính độ tan S và nồng độ phần trăm C% của dung dịch NaCl bão hòa ở 20°C.",
        "Độ tan của NaCl ở 20°C là S = 36 g/100 g H₂O. Khối lượng dung dịch bão hòa là: m_dd = 36 + 100 = 136 (g). Nồng độ phần trăm của dung dịch bão hòa là: C% = (36 / 136) × 100% ≈ 26,47%.",
        "Muốn pha chế 500 gam dung dịch nước muối sinh lý có nồng độ 0,9% thì cần dùng bao nhiêu gam muối ăn (NaCl) tinh khiết và bao nhiêu gam nước cất?",
        [
            "4,5 g muối NaCl và 495,5 g nước cất",
            "0,9 g muối NaCl và 499,1 g nước cất",
            "9,0 g muối NaCl và 491,0 g nước cất",
            "45 g muối NaCl và 455 g nước cất",
        ],
        0,
        "Pha chế dung dịch y tế (nước muối sinh lý 0,9%, dung dịch Oresol), bảo quản nước giải khát có gas và giải thích vì sao mùa hè cá thường phải ngoi lên mặt nước để đớp không khí.",
        "Tại sao vào những ngày mùa hè nắng nóng oi bức, cá nuôi trong ao hồ thường phải ngoi lên sát mặt nước để thở, và người nuôi cá phải bật máy quạt nước?",
        "Vì vào mùa hè nhiệt độ nước tăng cao làm độ tan của khí Oxygen (O₂) trong nước giảm mạnh, khiến lượng O₂ hòa tan trong nước ao bị thiếu hụt. Cá phải ngoi lên sát mặt nước (nơi tiếp xúc trực tiếp với không khí có nhiều O₂ hơn) để hô hấp; bật máy quạt nước giúp tăng diện tích tiếp xúc giữa nước và không khí để hòa tan thêm O₂.",
    ),
    C(
        6,
        "bien-doi-vat-ly",
        "Sự biến đổi Vật lý và Sự biến đổi Hóa học",
        "🔄",
        "Phân biệt chính xác quá trình biến đổi vật lý (không sinh ra chất mới) và biến đổi hóa học (có sinh ra chất mới) qua các dấu hiệu thực nghiệm.",
        "Đốt giấy và làm tan viên đá",
        "Khi viên nước đá tan chảy thành nước lỏng, bản chất chất vẫn là H₂O; nhưng khi đốt một tờ giấy, tờ giấy biến thành tro đen, khói và khí không thể quay trở lại thành giấy ban đầu.",
        "Sự biến đổi vật lý là hiện tượng chất chỉ biến đổi về trạng thái, hình dạng, kích thước, sự hòa tan... mà vẫn giữ nguyên là chất ban đầu (không tạo thành chất mới). Sự biến đổi hóa học (phản ứng hóa học) là hiện tượng chất biến đổi có tạo ra chất mới.",
        "• Ví dụ về biến đổi vật lý: Hòa tan muối/đường vào nước, dây tóc bóng đèn вольфрам (tungsten) nóng sáng khi có dòng điện, cồn bay hơi, rèn thanh sắt thành lưỡi dao, nghiền nhỏ hạt tiêu.\n"
        "• Ví dụ về biến đổi hóa học: Đốt cháy than/gỗ/khí gas, đinh sắt bị gỉ trong không khí ẩm, cơm bị ôi thiu, lên men sữa tươi thành sữa chua, nung đá vôi thành vôi sống, quang hợp ở cây xanh.\n"
        "• Trong nhiều quá trình thực tế (như đốt một ngọn nến Paraffin), cả biến đổi vật lý và biến đổi hóa học diễn ra nối tiếp nhau.",
        [
            {
                "category": "I. Tiêu chí cốt lõi phân biệt Biến đổi Vật lý & Biến đổi Hóa học",
                "items": [
                    {"name": "Biến đổi Vật lý", "formula": "Chất A (trạng thái/hình dạng 1)  →  Chất A (trạng thái/hình dạng 2)  (KHÔNG có chất mới)", "note": ""},
                    {"name": "Biến đổi Hóa học", "formula": "Chất ban đầu (A, B)  →  Chất mới (C, D)  (CÓ chất mới sinh ra với tính chất khác hẳn)", "note": ""},
                ],
            },
            {
                "category": "II. Năm dấu hiệu nhận biết có Biến đổi Hóa học xảy ra",
                "items": [
                    {"name": "Dấu hiệu quan sát trực tiếp", "formula": "1) Đổi màu sắc ; 2) Sủi bọt khí ; 3) Xuất hiện chất rắn không tan (kết tủa) ; 4) Tỏa nhiệt và phát sáng ; 5) Thay đổi mùi vị", "note": ""},
                ],
            },
        ],
        "Khi thắp sáng một cây nến (làm bằng sáp paraffin), phần sáp quanh bấc nến chảy lỏng ra, thấm vào bấc rồi hóa hơi và cháy tạo thành khí carbon dioxide (CO₂) và hơi nước (H₂O). Hãy chỉ ra giai đoạn nào là biến đổi vật lý, giai đoạn nào là biến đổi hóa học.",
        "Giai đoạn sáp nến rắn nóng chảy thành sáp lỏng rồi bay hơi thành hơi paraffin là BIẾN ĐỔI VẬT LÝ (chưa tạo chất mới). Giai đoạn hơi paraffin cháy trong không khí tạo ra khí CO₂ và hơi nước H₂O là BIẾN ĐỔI HÓA HỌC (có tạo ra chất mới).",
        "Quá trình nào sau đây là SỰ BIẾN ĐỔI VẬT LÝ?",
        [
            "Lên men nước ép nho để sản xuất rượu vang",
            "Đốt khí gas (LPG) trên bếp để đun nấu thức ăn",
            "Dây tóc bóng đèn bằng kim loại Tungsten nóng đỏ và phát sáng khi bật công tắc điện",
            "Sữa tươi để quên ngoài trời nắng bị chua và vón cục",
        ],
        2,
        "Nhận diện các quá trình biến đổi giúp bảo quản thực phẩm chống ôi thiu, sơn phủ chống gỉ sét kim loại và điều khiển quá trình nấu nướng.",
        "Khi đập quả trứng gà sống vào chảo dầu đang nóng để rán (chiên) trứng, lòng trắng trứng trong suốt chuyển thành màu trắng đục và đông cứng lại. Đây là biến đổi vật lý hay biến đổi hóa học? Giải thích.",
        "Đây là sự BIẾN ĐỔI HÓA HỌC (kèm biến tính cấu trúc phân tử protein dưới tác dụng của nhiệt độ cao), tạo ra chất mới có màu sắc, mùi vị và tính chất không thể đảo ngược lại thành lòng trắng trứng sống ban đầu.",
    ),
    C(
        6,
        "an-toan-hoa-hoc",
        "Dụng cụ thí nghiệm, Biển báo nguy hiểm & Quy tắc An toàn Hóa học",
        "🛡️",
        "Nhận diện các dụng cụ thí nghiệm hóa học, biển báo cảnh báo nguy hiểm (GHS) và quy tắc vàng khi tiếp xúc với hóa chất.",
        "Phòng thí nghiệm an toàn",
        "Mỗi lọ hóa chất trong phòng thí nghiệm đều có dán nhãn ghi tên, công thức và các biểu tượng cảnh báo nguy hiểm. Hiểu đúng các ký hiệu này giúp ta thực hiện thí nghiệm an toàn tuyệt đối.",
        "An toàn trong phòng thí nghiệm hóa học là hệ thống các quy tắc bắt buộc về trang bị bảo hộ (kính bảo hộ, găng tay, áo blouse), thao tác lấy hóa chất, đun nóng và xử lý sự cố hóa chất.",
        "• Các dụng cụ thí nghiệm cơ bản: Ống nghiệm (test tube), cốc thủy tinh (beaker), bình tam giác (Erlenmeyer flask), ống đong (measuring cylinder), phễu (funnel), ống hút nhỏ giọt (pipette), đèn cồn.\n"
        "• Hệ thống biển báo an toàn: Hình tam giác đều viền đen/đỏ nền vàng là biển CẢNH BÁO nguy hiểm (Chất dễ cháy, Chất ăn mòn, Chất độc, Chất oxi hóa...); Hình tròn viền đỏ gạch chéo là biển CẤM; Hình vuông/chữ nhật nền xanh là biển CHỈ DẪN bắt buộc.\n"
        "• Quy tắc vàng: Không nếm, không ngửi trực tiếp hóa chất (muốn nhận biết mùi phải dùng bàn tay phẩy nhẹ hơi hóa chất về phía mũi); khi đun nóng ống nghiệm phải kẹp ở vị trí 1/3 từ miệng ống nghiệm xuống và hướng miệng ống nghiệm về phía không có người; tắt đèn cồn bằng cách đậy nắp chụp (tuyệt đối không thổi!).",
        [
            {
                "category": "I. Quy tắc Thao tác an toàn trong Phòng thí nghiệm",
                "items": [
                    {"name": "Lấy hóa chất & Ngửi mùi hóa chất", "formula": "Dùng thìa thủy tinh/nhựa hoặc ống nhỏ giọt ; Phẩy nhẹ tay trên miệng lọ để ngửi gián tiếp", "note": "Không đổ hóa chất thừa ngược trở lại lọ gốc"},
                    {"name": "Đun nóng chất lỏng trong ống nghiệm", "formula": "Lượng chất lỏng ≤ 1/3 ống nghiệm ; Kẹp ở 1/3 phía trên miệng ống ; Nghiêng ~45° hướng về phía không có người", "note": "Hơ nóng đều khắp ống trước khi đun tập trung ở đáy"},
                    {"name": "Nguyên tắc Pha loãng Acid đặc (đặc biệt H₂SO₄ đặc)", "formula": "Rót TỪ TỪ ACID VÀO NƯỚC và khuấy đều (Tuyệt đối KHÔNG đổ nước vào acid đặc!)", "note": "Tránh sôi bắn acid gây bỏng nặng"},
                ],
            },
            {
                "category": "II. Ý nghĩa hình dạng và màu sắc Biển báo an toàn",
                "items": [
                    {"name": "Biển CẤM vs Biển CẢNH BÁO vs Biển CHỈ DẪN", "formula": "Tròn đỏ gạch chéo: CẤM ; Tam giác vàng/thoi đỏ: CẢNH BÁO NGUY HIỂM ; Xanh dương/xanh lá: BẮT BUỘC / CỨU HỘ", "note": ""},
                ],
            },
        ],
        "Khi muốn tắt ngọn lửa đèn cồn sau khi làm thí nghiệm xong, học sinh A định dùng miệng thổi tắt đèn cồn, còn học sinh B dùng nắp nhựa/kim loại của đèn cồn chụp nhẹ lên bấc đèn. Ai làm đúng và vì sao?",
        "Học sinh B làm ĐÚNG. Dùng nắp chụp đậy lên bấc đèn sẽ ngăn ngọn lửa tiếp xúc với khí Oxygen làm lửa tắt an toàn. Tuyệt đối không dùng miệng thổi đèn cồn vì luồng gió thổi có thể đẩy ngọn lửa tạt ngược vào trong bầu chứa cồn gây nổ và bỏng.",
        "Khi muốn nhận biết mùi của một chất khí hoặc hóa chất lỏng trong ống nghiệm, thao tác nào dưới đây là ĐÚNG quy tắc an toàn?",
        [
            "Đưa mũi sát vào miệng ống nghiệm và hít thật sâu",
            "Đổ một ít hóa chất ra lòng bàn tay rồi đưa lên mũi ngửi",
            "Giữ ống nghiệm cách xa mặt khoảng 15–20 cm, dùng bàn tay phẩy nhẹ trên miệng ống nghiệm để làn hơi thoảng về phía mũi",
            "Đun sôi hóa chất lên để mùi bốc ra mạnh hơn rồi ngửi",
        ],
        2,
        "Hình thành kỹ năng sử dụng hóa chất gia dụng (nước tẩy Javel, nước thông cống, cồn sát khuẩn) an toàn trong gia đình.",
        "Tại sao trên nhãn các chai nước tẩy bồn cầu (chứa acid HCl) và nước tẩy trắng Javel (chứa NaClO) luôn có dòng cảnh báo: 'Tuyệt đối không trộn lẫn hai loại chất tẩy rửa này với nhau khi cọ rửa phòng tắm kín'?",
        "Vì khi trộn nước tẩy chứa acid (HCl) với nước Javel (NaClO) sẽ xảy ra phản ứng hóa học giải phóng khí Chlorine (Cl₂) cực độc (NaClO + 2HCl → NaCl + Cl₂↑ + H₂O). Trong phòng tắm kín, hít phải khí Cl₂ sẽ gây tổn thương nghiêm trọng đường hô hấp và nguy hiểm đến tính mạng.",
    ),

    # =========================================================
    # HÓA HỌC LỚP 7 (7 BÀI)
    # =========================================================
    C(
        7,
        "nguyen-tu",
        "Nguyên tử – Hạt nhân (Proton, Neutron) & Vỏ nguyên tử (Electron)",
        "⚛️",
        "Nắm vững cấu tạo nguyên tử theo mô hình Rutherford – Bohr, điện tích - khối lượng các hạt p, n, e và cách tính khối lượng nguyên tử theo amu.",
        "Khám phá thế giới vi mô bên trong nguyên tử",
        "Mọi vật chất đều được cấu tạo từ các hạt nguyên tử cực kỳ nhỏ bé (đường kính khoảng 10⁻¹⁰ m). Dù rất nhỏ nhưng nguyên tử lại có cấu trúc rỗng gồm tâm là hạt nhân và vỏ là các lớp electron.",
        "Nguyên tử là hạt vô cùng nhỏ và trung hòa về điện, gồm hai phần: Hạt nhân nằm ở tâm nguyên tử (chứa hạt proton mang điện tích dương +1 và hạt neutron không mang điện) và Vỏ nguyên tử (tạo bởi một hay nhiều electron mang điện tích âm −1 chuyển động xung quanh hạt nhân).",
        "• Đặc điểm 3 loại hạt cơ bản:\n"
        "  + Proton (p): điện tích quy ước +1, khối lượng xấp xỉ 1 amu.\n"
        "  + Neutron (n): điện tích bằng 0 (không mang điện), khối lượng xấp xỉ 1 amu.\n"
        "  + Electron (e): điện tích quy ước −1, khối lượng cực nhỏ ≈ 0,00055 amu (nhỏ hơn khối lượng p và n khoảng 1840 lần!).\n"
        "• Vì nguyên tử trung hòa về điện nên: Số hạt proton (p) = Số hạt electron (e) = Số đơn vị điện tích hạt nhân (Z).\n"
        "• Vì khối lượng của electron rất nhỏ không đáng kể nên khối lượng của nguyên tử tập trung hầu hết ở hạt nhân: Khối lượng nguyên tử (amu) ≈ p + n.\n"
        "• Theo mô hình Rutherford – Bohr, các electron sắp xếp thành từng lớp từ trong ra ngoài: Lớp thứ nhất (sát hạt nhân nhất) chứa tối đa 2e; Lớp thứ hai chứa tối đa 8e; Lớp thứ ba chứa tối đa 8e (đối với 20 nguyên tố đầu tiên).",
        [
            {
                "category": "I. Các hệ thức cơ bản trong Nguyên tử trung hòa",
                "items": [
                    {"name": "Điều kiện trung hòa về điện", "formula": "Số proton (p) = Số electron (e) = Số đơn vị điện tích hạt nhân (Z)", "note": "Điện tích hạt nhân = +Z"},
                    {"name": "Tổng số hạt cơ bản trong nguyên tử (S)", "formula": "S = p + n + e = 2p + n", "note": "Vì p = e"},
                    {"name": "Khối lượng nguyên tử (theo đơn vị amu)", "formula": "m_nguyên_tử ≈ m_hạt_nhân ≈ p + n (amu)", "note": "Do m_e ≈ 0,00055 amu ≪ 1 amu (1 amu ≈ 1,6605 · 10⁻²⁴ g)"},
                ],
            },
            {
                "category": "II. Sức chứa Electron trên các lớp vỏ (Mô hình Bohr cho Z ≤ 20)",
                "items": [
                    {"name": "Thứ tự điền electron từ trong ra ngoài", "formula": "Lớp 1 (lớp K): tối đa 2e  ;  Lớp 2 (lớp L): tối đa 8e  ;  Lớp 3 (lớp M): tối đa 8e (với Z ≤ 20)", "note": "Ví dụ: Al (Z=13) có 3 lớp e: (2, 8, 3) ⇒ có 3e lớp ngoài cùng"},
                ],
            },
        ],
        "Nguyên tử Aluminium (Nhôm) có điện tích hạt nhân là +13 và có 14 hạt neutron trong hạt nhân. Hãy xác định số hạt proton, số hạt electron, khối lượng nguyên tử (theo amu) và số electron ở lớp ngoài cùng của nguyên tử Aluminium.",
        "Số proton = số electron = Z = 13 (hạt). Khối lượng nguyên tử: m ≈ p + n = 13 + 14 = 27 (amu). Phân bố 13 electron vào các lớp từ trong ra ngoài: Lớp 1 có 2e, Lớp 2 có 8e, còn lại Lớp 3 (lớp ngoài cùng) có 13 − (2 + 8) = 3 electron.",
        "Khẳng định nào dưới đây là ĐÚNG khi nói về cấu tạo nguyên tử?",
        [
            "Hạt nhân nguyên tử được cấu tạo bởi các hạt proton và electron",
            "Trong nguyên tử, số hạt proton luôn bằng số hạt neutron",
            "Khối lượng của nguyên tử tập trung hầu hết ở hạt nhân vì khối lượng electron vô cùng nhỏ",
            "Hạt neutron mang điện tích âm (−1)",
        ],
        2,
        "Mô hình nguyên tử là chìa khóa để giải thích vì sao các nguyên tố khác nhau có tính chất khác nhau và cách chúng liên kết tạo ra mọi vật chất.",
        "Một nguyên tử X có tổng số hạt (proton, neutron, electron) là 40 hạt, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 12 hạt. Hãy tính số hạt p, e, n và khối lượng nguyên tử X theo amu.",
        "Ta có tổng số hạt: p + n + e = 2p + n = 40 (1) (vì p = e). Số hạt mang điện là (p + e = 2p), số hạt không mang điện là n ⇒ 2p − n = 12 (2). Cộng (1) và (2) được: 4p = 52 ⇒ p = e = 13, suy ra n = 40 − 2·13 = 14. Khối lượng nguyên tử X là: p + n = 13 + 14 = 27 (amu) (X là Aluminium - Al).",
    ),
    C(
        7,
        "nguyen-to-hoa-hoc",
        "Nguyên tố hóa học, Ký hiệu hóa học & Bảng tuần hoàn các nguyên tố hóa học",
        "🔬",
        "Hiểu định nghĩa nguyên tố hóa học, thuộc ký hiệu - tên gọi IUPAC và quy tắc sắp xếp Chu kỳ - Nhóm trong Bảng tuần hoàn.",
        "Ngôn ngữ chung của khoa học toàn cầu",
        "Hiện nay khoa học đã biết tới 118 nguyên tố hóa học. Nhờ Bảng tuần hoàn của Mendeleev và hệ thống ký hiệu hóa học quốc tế (IUPAC), các nhà khoa học trên toàn thế giới có thể đọc hiểu thành phần của mọi chất.",
        "Nguyên tố hóa học là tập hợp những nguyên tử cùng loại, có CÙNG SỐ HẠT PROTON trong hạt nhân. Số hạt proton đặc trưng cho một nguyên tố hóa học và được gọi là số hiệu nguyên tử (Z).",
        "• Ký hiệu hóa học gồm 1 hoặc 2 chữ cái (chữ cái đầu luôn viết IN HOA, chữ cái thứ hai nếu có viết thường): H (Hydrogen - 1), He (Helium - 2), C (Carbon - 12), N (Nitrogen - 14), O (Oxygen - 16), Na (Sodium - 23), Mg (Magnesium - 24), Al (Aluminium - 27), Si (Silicon - 28), P (Phosphorus - 31), S (Sulfur - 32), Cl (Chlorine - 35,5), K (Potassium - 39), Ca (Calcium - 40), Fe (Iron - 56), Cu (Copper - 64), Zn (Zinc - 65), Ag (Silver - 108).\n"
        "• Cấu tạo Bảng tuần hoàn (sắp xếp theo chiều tăng dần của điện tích hạt nhân Z):\n"
        "  + Ô nguyên tố: Số thứ tự của ô = Số hiệu nguyên tử (Z) = Số p = Số e.\n"
        "  + Chu kỳ (hàng ngang, gồm 7 chu kỳ): Các nguyên tố trong cùng một chu kỳ có CÙNG SỐ LỚP ELECTRON (Số thứ tự chu kỳ = Số lớp electron).\n"
        "  + Nhóm (cột dọc): Các nguyên tố trong cùng một nhóm A có CÙNG SỐ ELECTRON LỚP NGOÀI CÙNG nên có tính chất hóa học tương tự nhau (Số thứ tự nhóm A = Số electron lớp ngoài cùng, trừ He).",
        [
            {
                "category": "I. Mối liên hệ Vàng giữa Cấu tạo Nguyên tử và Vị trí trong Bảng tuần hoàn (Nhóm A)",
                "items": [
                    {"name": "Số thứ tự Ô nguyên tố", "formula": "Số thứ tự Ô = Z = Số proton (p) = Số electron (e)", "note": ""},
                    {"name": "Số thứ tự Chu kỳ (Hàng ngang)", "formula": "Số thứ tự Chu kỳ = Số lớp electron trong nguyên tử", "note": "Chu kỳ 1, 2, 3 là các chu kỳ nhỏ; 4, 5, 6, 7 là chu kỳ lớn"},
                    {"name": "Số thứ tự Nhóm A (Cột dọc)", "formula": "Số thứ tự Nhóm A (IA → VIIIA) = Số electron ở lớp ngoài cùng", "note": "Riêng Helium (He, Z=2) chỉ có 2e lớp ngoài cùng nhưng xếp vào nhóm VIIIA (khí hiếm)"},
                ],
            },
            {
                "category": "II. Phân loại Kim loại – Phi kim – Khí hiếm theo số e lớp ngoài cùng",
                "items": [
                    {"name": "Kim loại (Nhóm IA, IIA, IIIA...)", "formula": "Thường có 1, 2 hoặc 3 electron ở lớp ngoài cùng (trừ H, He, B)", "note": "Chiếm hơn 80% tổng số nguyên tố trong BTH"},
                    {"name": "Phi kim (Nhóm VA, VIA, VIIA...)", "formula": "Thường có 5, 6 hoặc 7 electron ở lớp ngoài cùng (cùng với H, C, Si)", "note": ""},
                    {"name": "Khí hiếm (Nhóm VIIIA: He, Ne, Ar...)", "formula": "Có 8 electron ở lớp ngoài cùng (riêng He có 2e) ⇒ rất bền vững, hầu như không phản ứng", "note": ""},
                ],
            },
        ],
        "Nguyên tố Magnesium (Mg) nằm ở ô số 12, chu kỳ 3, nhóm IIA trong Bảng tuần hoàn. Hãy cho biết nguyên tử Mg có bao nhiêu proton, bao nhiêu electron, mấy lớp electron, mấy electron lớp ngoài cùng và Mg là kim loại hay phi kim?",
        "Ô số 12 ⇒ có 12 proton và 12 electron. Chu kỳ 3 ⇒ có 3 lớp electron. Nhóm IIA ⇒ có 2 electron ở lớp ngoài cùng (phân bố e trên 3 lớp là 2, 8, 2). Vì có 2e lớp ngoài cùng (thuộc nhóm IIA) nên Mg là nguyên tố KIM LOẠI.",
        "Ký hiệu hóa học và khối lượng nguyên tử (amu) đúng của nguyên tố Potassium (Kali) và Sodium (Natri) lần lượt là:",
        [
            "P (31 amu) và S (32 amu)",
            "K (39 amu) và Na (23 amu)",
            "Ca (40 amu) và Na (23 amu)",
            "K (19 amu) và So (11 amu)",
        ],
        1,
        "Tra cứu nhanh thông tin nguyên tố trên nhãn phân bón, thành phần dinh dưỡng thực phẩm, dược phẩm và vật liệu bán dẫn.",
        "Nguyên tử của nguyên tố X có 3 lớp electron và có 7 electron ở lớp ngoài cùng. Hãy xác định vị trí (ô, chu kỳ, nhóm) của X trong Bảng tuần hoàn, cho biết tên nguyên tố X và giải thích vì sao X là phi kim hoạt động mạnh?",
        "Có 3 lớp electron ⇒ X thuộc Chu kỳ 3. Có 7e lớp ngoài cùng ⇒ X thuộc Nhóm VIIA (nhóm Halogen). Vì lớp 1 có 2e, lớp 2 có 8e, lớp 3 có 7e nên tổng số e = p = Z = 2 + 8 + 7 = 17 ⇒ X nằm ở Ô số 17. Nguyên tố X là Chlorine (Cl), là một phi kim điển hình rất dễ nhận thêm 1e để đạt lớp vỏ 8e bền vững của khí hiếm Argon.",
    ),
    C(
        7,
        "phan-tu",
        "Phân tử & Khối lượng phân tử",
        "🧩",
        "Hiểu khái niệm phân tử là hạt đại diện cho chất và tính chính xác khối lượng phân tử theo đơn vị amu.",
        "Từ nguyên tử riêng lẻ đến phân tử",
        "Các nguyên tử hiếm khi tồn tại một mình (trừ khí hiếm), mà thường kết hợp với nhau tạo thành phân tử như H₂O (nước), O₂ (khí oxygen), CO₂ (khí carbon dioxide).",
        "Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất. Khối lượng phân tử của một chất bằng tổng khối lượng của các nguyên tử có trong phân tử chất đó (đơn vị là amu).",
        "• Đối với các chất cộng hóa trị (như H₂, O₂, N₂, Cl₂, H₂O, CO₂, NH₃, CH₄), hạt hợp thành là các phân tử rời rạc.\n"
        "• Đối với các hợp chất ion (như NaCl, CaCO₃, CuSO₄), các ion sắp xếp liên tục thành mạng tinh thể nên ta dùng khái niệm 'đơn vị công thức' tương đương để tính khối lượng phân tử.\n"
        "• Cách phân biệt cách viết: '3 H' chỉ 3 nguyên tử Hydrogen riêng rẽ; còn '3 H₂' chỉ 3 phân tử khí Hydrogen (mỗi phân tử gồm 2 nguyên tử H liên kết với nhau, tổng cộng có 6 nguyên tử H).",
        [
            {
                "category": "I. Cách đọc Ký hiệu Hệ số và Chỉ số phân tử",
                "items": [
                    {"name": "Biểu diễn n phân tử AₓBᵧ (n · AₓBᵧ)", "formula": "n: hệ số (số phân tử) ; x, y: chỉ số chân (số nguyên tử A, B trong 1 phân tử)", "note": "Tổng số nguyên tử = n · (x + y)"},
                ],
            },
            {
                "category": "II. Công thức tính Khối lượng phân tử (KLPT - đơn vị amu)",
                "items": [
                    {"name": "Đối với phân tử AₓBᵧC_z", "formula": "KLPT(AₓBᵧC_z) = x · M_A + y · M_B + z · M_C (amu)", "note": "M_A, M_B, M_C là khối lượng nguyên tử của A, B, C"},
                    {"name": "Đối với công thức có dấu ngoặc Aₓ(BCₙ)ᵧ", "formula": "KLPT = x · M_A + y · (M_B + n · M_C) (amu)", "note": "Chỉ số y ngoài ngoặc nhân với toàn bộ cụm trong ngoặc"},
                ],
            },
        ],
        "Tính khối lượng phân tử của: a) Calcium carbonate CaCO₃; b) Aluminium sulfate Al₂(SO₄)₃. Cho biết: Ca = 40, C = 12, O = 16, Al = 27, S = 32.",
        "a) KLPT(CaCO₃) = 40 + 12 + 3 · 16 = 100 (amu). b) KLPT(Al₂(SO₄)₃) = 2 · 27 + 3 · (32 + 4 · 16) = 54 + 3 · 96 = 342 (amu).",
        "Trong cách viết '4 CO₂', có bao nhiêu phân tử CO₂ và tổng cộng bao nhiêu nguyên tử Oxygen (O)?",
        [
            "4 phân tử CO₂ và 2 nguyên tử O",
            "4 phân tử CO₂ và 4 nguyên tử O",
            "4 phân tử CO₂ và 8 nguyên tử O",
            "2 phân tử CO₂ và 8 nguyên tử O",
        ],
        2,
        "Tính khối lượng phân tử giúp so sánh xem chất khí nào nặng hơn hay nhẹ hơn không khí (KLPT trung bình của không khí ≈ 29 amu) và tính toán thành phần hóa chất.",
        "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 3 nguyên tử Oxygen (công thức XO₃) và có khối lượng phân tử bằng 80 amu. Hãy tìm khối lượng nguyên tử của X và cho biết X là nguyên tố nào (biết O = 16, C = 12, N = 14, S = 32).",
        "Ta có: KLPT(XO₃) = M_X + 3 · 16 = 80 ⇔ M_X + 48 = 80 ⇒ M_X = 32 (amu). Vậy X là nguyên tố Sulfur (Lưu huỳnh - S) và công thức phân tử của hợp chất là SO₃ (Sulfur trioxide).",
    ),
    C(
        7,
        "don-chat-hop-chat",
        "Đơn chất và Hợp chất",
        "🧱",
        "Phân biệt đơn chất (tạo nên từ 1 nguyên tố hóa học) với hợp chất (tạo nên từ 2 nguyên tố hóa học trở lên) và phân biệt hợp chất với hỗn hợp.",
        "Kim cương, than chì, khí Oxygen và Nước",
        "Khí Oxygen (O₂), khí Ozone (O₃) và Kim cương (C) đều chỉ do một nguyên tố tạo nên; trong khi Nước (H₂O) và Muối ăn (NaCl) do hai nguyên tố khác nhau tạo nên.",
        "Đơn chất là những chất được tạo nên từ MỘT nguyên tố hóa học. Hợp chất là những chất được tạo nên từ HAI hay NHIỀU nguyên tố hóa học trở lên.",
        "• Phân loại đơn chất:\n"
        "  + Đơn chất kim loại (Fe, Cu, Al, Mg, Na, Ag...): các nguyên tử sắp xếp khít nhau, có ánh kim, dẫn điện và dẫn nhiệt tốt; công thức hóa học trùng với ký hiệu nguyên tố.\n"
        "  + Đơn chất phi kim (H₂, O₂, N₂, Cl₂, C, S, P...): các phi kim ở thể khí thường gồm 2 nguyên tử liên kết với nhau (H₂, O₂, N₂, F₂, Cl₂).\n"
        "  + Đơn chất khí hiếm (He, Ne, Ar...): tồn tại dưới dạng các nguyên tử độc lập.\n"
        "• Phân loại hợp chất: Hợp chất vô cơ (như H₂O, CO₂, NaCl, H₂SO₄, CaCO₃) và Hợp chất hữu cơ (như CH₄, C₂H₅OH, glucose C₆H₁₂O₆).\n"
        "• Lưu ý quan trọng: Cả đơn chất và hợp chất đều là CHẤT TINH KHIẾT (có công thức hóa học duy nhất), khác với hỗn hợp (gồm nhiều chất trộn lẫn).",
        [
            {
                "category": "I. Sơ đồ Phân loại Chất tinh khiết (Đơn chất vs Hợp chất)",
                "items": [
                    {"name": "Đơn chất (Chỉ gồm 1 nguyên tố)", "formula": "Kim loại: Fe, Cu, Al... ; Phi kim: H₂, O₂, N₂, Cl₂, O₃, C, S, P... ; Khí hiếm: He, Ne, Ar", "note": "Lưu ý: O₂ và O₃ (ozone) đều là ĐƠN CHẤT của nguyên tố Oxygen"},
                    {"name": "Hợp chất (Từ 2 nguyên tố trở lên)", "formula": "Vô cơ: H₂O, CO₂, NaCl, CaCO₃... ; Hữu cơ: CH₄, C₆H₁₂O₆, C₁₂H₂₂O₁₁...", "note": "Tính chất của hợp chất khác hẳn tính chất của các đơn chất tạo nên nó"},
                ],
            },
            {
                "category": "II. Tính Phần trăm khối lượng của nguyên tố trong Hợp chất AₓBᵧ",
                "items": [
                    {"name": "Phần trăm khối lượng nguyên tố A", "formula": "%m_A = [ (x · M_A) / KLPT(AₓBᵧ) ] × 100%", "note": "Tổng phần trăm các nguyên tố trong hợp chất luôn bằng 100%"},
                ],
            },
        ],
        "Cho các chất có công thức hóa học sau: Br₂, H₂SO₄, Mg, NH₃, O₃, CaCO₃, Ne. Hãy sắp xếp các chất trên vào hai nhóm: Đơn chất và Hợp chất.",
        "Nhóm Đơn chất (chỉ tạo từ 1 nguyên tố): Br₂, Mg, O₃, Ne (4 chất). Nhóm Hợp chất (tạo từ 2 nguyên tố trở lên): H₂SO₄, NH₃, CaCO₃ (3 chất).",
        "Dãy chất nào dưới đây CHỈ gồm toàn các HỢP CHẤT?",
        [
            "H₂O, CO₂, O₂, NaCl",
            "CH₄, H₂O, NH₃, CaCO₃",
            "Fe, Cu, Al, Zn",
            "H₂, N₂, Cl₂, HCl",
        ],
        1,
        "Phân biệt đơn chất và hợp chất giúp hiểu cấu trúc vật liệu (như hai dạng đơn chất thù hình của Carbon là Kim cương siêu cứng và Than chì mềm dẫn điện) và tính hàm lượng dinh dưỡng.",
        "Khí Hydrogen (H₂) là một chất khí rất dễ cháy nổ, còn khí Oxygen (O₂) là chất khí duy trì sự cháy. Nhưng khi nguyên tố H và nguyên tố O liên kết với nhau tạo thành hợp chất Nước (H₂O), tại sao nước lại không cháy mà còn dùng để dập tắt lửa?",
        "Vì khi các nguyên tử H và O liên kết hóa học với nhau tạo thành phân tử hợp chất mới là H₂O, cấu trúc electron và phân tử đã thay đổi hoàn toàn. Hợp chất luôn có những tính chất vật lý và hóa học mới, khác hẳn với tính chất của các đơn chất tạo nên nó (khác với hỗn hợp chỉ trộn lẫn cơ học).",
    ),
    C(
        7,
        "hoa-tri-lien-ket",
        "Liên kết hóa học (Liên kết Ion - Liên kết Cộng hóa trị), Hóa trị & Quy tắc Hóa trị",
        "🔗",
        "Hiểu quy tắc Octet (bát tử), sự tạo thành ion dương/âm trong liên kết ion, sự góp chung electron trong liên kết cộng hóa trị và quy tắc hóa trị a·x = b·y.",
        "Vì sao các nguyên tử lại gắn kết với nhau?",
        "Trừ các khí hiếm (He, Ne, Ar) đã có lớp vỏ ngoài cùng bền vững (8e hoặc 2e với He), nguyên tử của các nguyên tố khác đều có xu hướng nhường, nhận hoặc góp chung electron để đạt được lớp vỏ bền vững giống khí hiếm.",
        "Liên kết hóa học là sự kết hợp giữa các nguyên tử tạo thành phân tử hay tinh thể bền vững hơn. Hóa trị là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác (lấy hóa trị của H làm І và của O làm II).",
        "• Liên kết Ion: được hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu (thường giữa điển hình KIM LOẠI và PHI KIM). Nguyên tử kim loại (1, 2, 3e ngoài cùng) nhường electron tạo thành ion dương (Cation: Na⁺, Mg²⁺, Al³⁺); nguyên tử phi kim (5, 6, 7e ngoài cùng) nhận electron tạo thành ion âm (Anion: Cl⁻, O²⁻). Các hợp chất ion (như NaCl, MgO, CaCl₂) là chất rắn kết tinh ở điều kiện thường, có nhiệt độ nóng chảy và nhiệt độ sôi cao, khi tan trong nước tạo dung dịch dẫn điện.\n"
        "• Liên kết Cộng hóa trị: được hình thành bằng sự DÙNG CHUNG (góp chung) một hay nhiều cặp electron giữa hai nguyên tử (thường giữa PHI KIM với PHI KIM như H₂, O₂, N₂, H₂O, CO₂, HCl, NH₃, CH₄). Các chất cộng hóa trị có thể ở thể khí, lỏng hoặc rắn, thường có nhiệt độ nóng chảy và nhiệt độ sôi thấp.\n"
        "• Quy tắc hóa trị cho hợp chất hai nguyên tố AₓBᵧ (với a, b lần lượt là hóa trị của A và B): x · a = y · b ⇒ x / y = b / a (tối giản).",
        [
            {
                "category": "I. Liên kết Ion (Nhường - Nhận e) vs Liên kết Cộng hóa trị (Góp chung e)",
                "items": [
                    {"name": "Sự tạo thành Ion & Liên kết Ion (Kim loại + Phi kim)", "formula": "Kim loại M − ne → Mⁿ⁺ (ion dương) ; Phi kim X + me → Xᵐ⁻ (ion âm) ⇒ Mⁿ⁺ hút Xᵐ⁻", "note": "Ví dụ: Na + Cl → Na⁺Cl⁻ ; Mg + O → Mg²⁺O²⁻"},
                    {"name": "Liên kết Cộng hóa trị (Phi kim + Phi kim)", "formula": "Mỗi nguyên tử góp chung electron tạo các cặp e dùng chung (H–H, O=O, N≡N, H–O–H, O=C=O)", "note": "Không tạo thành ion trong quá trình hình thành phân tử"},
                ],
            },
            {
                "category": "II. Quy tắc Hóa trị & Lập Công thức Hóa học (CTHH)",
                "items": [
                    {"name": "Quy tắc hóa trị trong hợp chất AₓᵃBᵧᵇ", "formula": "x · a = y · b  ⇒  x / y = b / a = b' / a' (phân số tối giản)", "note": "Quy tắc bắt chéo hóa trị tối giản: x = b' và y = a'"},
                    {"name": "Hóa trị các nguyên tố & nhóm nguyên tử thường gặp", "formula": "I: H, Na, K, Ag, Cl, (OH), (NO₃) ; II: O, Mg, Ca, Ba, Zn, Cu, Fe(II), (SO₄), (CO₃) ; III: Al, Fe(III), (PO₄)", "note": ""},
                ],
            },
        ],
        "Lập công thức hóa học và tính khối lượng phân tử của hợp chất tạo bởi: a) Aluminium (hóa trị III) và Oxygen (hóa trị II); b) Calcium (hóa trị II) và nhóm phosphate (PO₄) (hóa trị III). Cho Al = 27, O = 16, Ca = 40, P = 31.",
        "a) Gọi công thức là AlₓOᵧ. Theo quy tắc hóa trị: x · III = y · II ⇒ x/y = 2/3 ⇒ x = 2, y = 3. Công thức là Al₂O₃, KLPT = 2·27 + 3·16 = 102 (amu). b) Gọi công thức là Caₓ(PO₄)ᵧ: x · II = y · III ⇒ x/y = 3/2 ⇒ Công thức là Ca₃(PO₄)₂, KLPT = 3·40 + 2·(31 + 4·16) = 310 (amu).",
        "Hợp chất nào dưới đây được hình thành bởi LIÊN KẾT ION?",
        [
            "Nước (H₂O)",
            "Khí Carbon dioxide (CO₂)",
            "Magnesium oxide (MgO) và Muối ăn (NaCl)",
            "Khí Methane (CH₄)",
        ],
        2,
        "Giải thích vì sao muối ăn (NaCl) rắn rất cứng, chỉ nóng chảy ở 801°C và dung dịch muối ăn dẫn điện tốt, trong khi đường saccharose (hợp chất cộng hóa trị) dễ nóng chảy và dung dịch đường không dẫn điện.",
        "Tìm hóa trị của nguyên tố Iron (Fe) trong hợp chất Fe₂(SO₄)₃ và của nguyên tố Nitrogen (N) trong hợp chất N₂O₅, biết nhóm (SO₄) có hóa trị II và O có hóa trị II.",
        "Trong Fe₂(SO₄)₃: gọi a là hóa trị của Fe, ta có 2 · a = 3 · II ⇒ a = III (Iron có hóa trị III). Trong N₂O₅: gọi b là hóa trị của N, ta có 2 · b = 5 · II ⇒ b = V (Nitrogen có hóa trị V).",
    ),
    C(
        7,
        "phan-ung-hoa-hoc",
        "Phản ứng hóa học, Diễn biến phân tử & Phản ứng Tỏa nhiệt - Thu nhiệt",
        "💥",
        "Hiểu bản chất phản ứng hóa học là sự thay đổi liên kết giữa các nguyên tử (số nguyên tử mỗi nguyên tố bảo toàn) và phân biệt phản ứng tỏa nhiệt, thu nhiệt.",
        "Sự tái sắp xếp các nguyên tử",
        "Khi khí Hydrogen cháy trong khí Oxygen tạo thành Nước, các phân tử H₂ và O₂ tách ra thành các nguyên tử rồi ghép lại với nhau theo trật tự mới tạo thành phân tử H₂O.",
        "Phản ứng hóa học là quá trình biến đổi từ chất này (chất phản ứng hay chất tham gia) thành chất khác (sản phẩm hay chất tạo thành).",
        "• Bản chất vi mô của phản ứng hóa học: Trước phản ứng, các nguyên tử liên kết với nhau trong phân tử chất tham gia; trong phản ứng, các liên kết cũ bị phá vỡ và các liên kết mới được hình thành tạo ra phân tử sản phẩm. Do đó: LIÊN KẾT GIỮA CÁC NGUYÊN TỬ THAY ĐỔI làm phân tử này biến đổi thành phân tử khác, nhưng SỐ NGUYÊN TỬ CỦA MỖI NGUYÊN TỐ TRƯỚC VÀ SAU PHẢN ỨNG GIỮ NGUYÊN (không đổi)!\n"
        "• Phương trình chữ của phản ứng hóa học: Tên các chất phản ứng → Tên các sản phẩm.\n"
        "• Năng lượng trong phản ứng: Phản ứng tỏa nhiệt (giải phóng năng lượng dạng nhiệt ra môi trường làm nhiệt độ xung quanh tăng lên, như đốt than, cồn, khí gas) và Phản ứng thu nhiệt (hấp thụ nhiệt năng từ môi trường trong suốt quá trình phản ứng, như nung đá vôi, hòa tan viên C sủi vào nước).",
        [
            {
                "category": "I. Phương trình chữ & Bản chất vi mô của Phản ứng hóa học",
                "items": [
                    {"name": "Sơ đồ phương trình chữ", "formula": "Chất phản ứng (Chất tham gia)  ───►  Sản phẩm (Chất tạo thành)", "note": "Mũi tên (→) đọc là 'tạo thành' hoặc 'sinh ra' ; dấu '+' đọc là 'tác dụng với' (ở vế trái) hoặc 'và' (ở vế phải)"},
                    {"name": "Đại lượng thay đổi vs Đại lượng bảo toàn", "formula": "Thay đổi: Liên kết giữa các nguyên tử & Số phân tử ; Bảo toàn: Số nguyên tử của mỗi nguyên tố & Tổng khối lượng", "note": ""},
                ],
            },
            {
                "category": "II. Phản ứng Tỏa nhiệt & Phản ứng Thu nhiệt",
                "items": [
                    {"name": "Phản ứng Tỏa nhiệt", "formula": "Tỏa nhiệt ra môi trường ⇒ Làm nhiệt độ môi trường xung quanh TĂNG LÊN", "note": "Ví dụ: Đốt nhiên liệu, hô hấp tế bào, tôi vôi sống CaO + H₂O"},
                    {"name": "Phản ứng Thu nhiệt", "formula": "Nhận nhiệt từ môi trường ⇒ Cần đun nóng liên tục hoặc làm môi trường LẠNH ĐI", "note": "Ví dụ: Nung đá vôi CaCO₃, quang hợp, viên sủi vitamin C tan trong nước"},
                ],
            },
        ],
        "Đun nóng hỗn hợp bột Iron (sắt) và bột Sulfur (lưu huỳnh) trong ống nghiệm thì hỗn hợp nóng đỏ rực lên và tạo thành chất rắn màu xám đen là Iron(II) sulfide (không còn bị nam châm hút nữa). Hãy viết phương trình chữ của phản ứng và xác định chất tham gia, sản phẩm.",
        "Phương trình chữ: Iron + Sulfur ──(t°)──► Iron(II) sulfide. Chất tham gia phản ứng là: Iron và Sulfur. Sản phẩm tạo thành là: Iron(II) sulfide.",
        "Trong một phản ứng hóa học, yếu tố nào dưới đây LUÔN ĐƯỢC GIỮ NGUYÊN (không thay đổi) trước và sau phản ứng?",
        [
            "Số phân tử của các chất",
            "Trạng thái vật lý và màu sắc của các chất",
            "Số lượng nguyên tử của mỗi nguyên tố hóa học",
            "Liên kết hóa học giữa các nguyên tử",
        ],
        2,
        "Ứng dụng các phản ứng tỏa nhiệt để cung cấp năng lượng cho động cơ, luyện kim, nấu ăn và túi chườm nóng/lạnh y tế.",
        "Khi thả một viên vitamin C sủi (chứa baking soda NaHCO₃ và citric acid) vào cốc nước lọc, ta thấy bọt khí CO₂ sủi lên mạnh và khi chạm tay vào thành cốc thấy cốc nước mát lạnh đi. Hãy cho biết phản ứng này là phản ứng tỏa nhiệt hay thu nhiệt?",
        "Vì phản ứng lấy bớt nhiệt năng từ nước trong cốc làm nhiệt độ của cốc nước giảm xuống (thấy mát lạnh), nên đây là một PHẢN ỨNG THU NHIỆT.",
    ),
    C(
        7,
        "bao-toan-khoi-luong",
        "Định luật Bảo toàn Khối lượng",
        "⚖️",
        "Hiểu cơ sở phân tử - nguyên tử của Định luật bảo toàn khối lượng (Lomonosov – Lavoisier) và vận dụng giải bài toán tính khối lượng chất.",
        "Chiếc cân hóa học trước và sau phản ứng",
        "Năm 1748 và 1789, hai nhà bác học Lomonosov và Lavoisier đã tiến hành các thí nghiệm nung kim loại trong bình kín và chứng minh rằng tổng khối lượng các chất trước và sau phản ứng luôn bằng nhau.",
        "Định luật bảo toàn khối lượng phát biểu: 'Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng'.",
        "• Giải thích định luật: Trong phản ứng hóa học chỉ có liên kết giữa các nguyên tử thay đổi, còn số lượng nguyên tử của mỗi nguyên tố trước và sau phản ứng hoàn toàn giữ nguyên và khối lượng của mỗi nguyên tử không đổi, vì vậy tổng khối lượng các chất được bảo toàn.\n"
        "• Nếu một phản ứng có n chất (kể cả chất tham gia và sản phẩm), khi biết khối lượng của (n − 1) chất thì ta luôn tính được khối lượng của chất còn lại.\n"
        "• Lưu ý quan trọng: Khối lượng chất tham gia chỉ tính phần khối lượng ĐÃ THỰC SỰ PHẢN ỨNG (không tính phần chất còn dư và tạp chất trơ!). Khi phản ứng thực hiện trong bình hở có chất khí (như O₂) từ không khí tham gia hoặc có khí (CO₂, H₂) thoát ra ngoài, cần tính cả khối lượng các chất khí đó vào phương trình bảo toàn.",
        [
            {
                "category": "I. Biểu thức Định luật Bảo toàn Khối lượng",
                "items": [
                    {"name": "Xét phản ứng: A + B → C + D", "formula": "m_A(phản_ứng) + m_B(phản_ứng) = m_C + m_D", "note": "Tổng khối lượng các chất phản ứng = Tổng khối lượng các sản phẩm"},
                    {"name": "Khi có chất A còn dư sau phản ứng", "formula": "m_A(phản_ứng) = m_A(ban_đầu) − m_A(dư)", "note": ""},
                ],
            },
            {
                "category": "II. Bài toán Nung chất rắn tạo khí hoặc Đốt kim loại trong không khí",
                "items": [
                    {"name": "Nung đá vôi: CaCO₃ → CaO + CO₂↑", "formula": "m_CaCO₃(pư) = m_CaO + m_CO₂  ⇒  Độ giảm khối lượng rắn = m_CO₂(thoát_ra)", "note": ""},
                    {"name": "Đốt kim loại trong không khí: Kim loại + O₂ → Oxide", "formula": "m_kim_loại + m_O₂ = m_Oxide  ⇒  Độ tăng khối lượng rắn = m_O₂(phản_ứng)", "note": ""},
                ],
            },
        ],
        "Đốt cháy hoàn toàn 9 gam kim loại Magnesium (Mg) trong không khí thu được 15 gam hợp chất Magnesium oxide (MgO). Viết công thức khối lượng của phản ứng và tính khối lượng khí Oxygen (O₂) đã phản ứng.",
        "Phương trình chữ: Magnesium + Oxygen → Magnesium oxide. Theo định luật bảo toàn khối lượng: m_Mg + m_O₂ = m_MgO ⇒ m_O₂ = m_MgO − m_Mg = 15 − 9 = 6 (gam).",
        "Nung nóng 100 kg đá vôi chứa 90% Calcium carbonate (CaCO₃) (còn lại 10% là tạp chất trơ không bị phân hủy), sau khi CaCO₃ phân hủy hết thu được 39,6 kg khí Carbon dioxide (CO₂). Khối lượng vôi sống (CaO) nguyên chất tạo thành là:",
        ["60,4 kg", "50,4 kg", "49,6 kg", "54,0 kg"],
        1,
        "Định luật bảo toàn khối lượng là công cụ cốt lõi để kiểm soát hao hụt nguyên liệu trong sản xuất công nghiệp hóa chất, luyện kim và xi măng.",
        "Đặt một cốc đựng dung dịch Hydrochloric acid (HCl) và một viên đá vôi (CaCO₃) lên đĩa cân điện tử thì cân chỉ 150,0 gam. Khi thả viên đá vôi vào trong cốc dung dịch acid (cốc để hở miệng), thấy có bọt khí CO₂ sủi lên; sau khi phản ứng kết thúc, cân điện tử chỉ 147,8 gam. Hiện tượng này có trái với Định luật bảo toàn khối lượng không? Hãy tính khối lượng khí CO₂ đã thoát ra ngoài không khí.",
        "Hiện tượng này hoàn toàn TUÂN THEO Định luật bảo toàn khối lượng! Số chỉ của cân giảm đi là do cốc để hở miệng nên khí CO₂ sinh ra đã bay thoát ra ngoài không khí. Khối lượng khí CO₂ đã thoát ra đúng bằng độ giảm số chỉ của cân: m_CO₂ = 150,0 − 147,8 = 2,2 (gam).",
    ),
    # =========================================================
    # HÓA HỌC LỚP 8 (7 BÀI)
    # =========================================================
    C(
        8,
        "cong-thuc-hoa-hoc",
        "Công thức Hóa học & Tính toán theo Công thức Hóa học",
        "🧾",
        "Xác định thành phần phần trăm khối lượng các nguyên tố từ công thức hóa học và bài toán ngược tìm công thức hóa học.",
        "Từ nhãn phân bón đến công thức phân tử",
        "Trên bao bì phân đạm Urea có ghi công thức (NH₂)₂CO và độ đạm 46% N. Làm thế nào các nhà hóa học tính được con số 46% đó từ công thức?",
        "Công thức hóa học (CTHH) của một chất dùng ký hiệu hóa học và chỉ số chân để biểu diễn thành phần nguyên tố và số lượng nguyên tử của mỗi nguyên tố trong một phân tử (hoặc một đơn vị công thức) chất đó.",
        "• Ý nghĩa của CTHH AₓBᵧ: Cho biết nguyên tố tạo nên chất, số nguyên tử của mỗi nguyên tố trong 1 phân tử chất và khối lượng phân tử (hoặc khối lượng mol M) của chất.\n"
        "• Dạng toán 1 (Bài toán thuận): Biết CTHH AₓBᵧ, tính phần trăm khối lượng (%m) của mỗi nguyên tố trong hợp chất.\n"
        "• Dạng toán 2 (Bài toán ngược): Biết phần trăm khối lượng các nguyên tố và khối lượng mol phân tử M của hợp chất, lập CTHH của hợp chất đó.",
        [
            {
                "category": "I. Bài toán Thuận: Tính % khối lượng nguyên tố từ CTHH AₓBᵧC_z",
                "items": [
                    {"name": "Khối lượng mol phân tử M", "formula": "M = x · M_A + y · M_B + z · M_C  (g/mol)", "note": ""},
                    {"name": "Phần trăm khối lượng mỗi nguyên tố", "formula": "%m_A = (x · M_A / M) × 100%  ;  %m_B = (y · M_B / M) × 100%  ;  %m_C = 100% − (%m_A + %m_B)", "note": ""},
                ],
            },
            {
                "category": "II. Bài toán Ngược: Lập CTHH AₓBᵧ khi biết %m và Khối lượng mol M",
                "items": [
                    {"name": "Cách 1 (Khi đã biết M)", "formula": "x = (%m_A · M) / (100% · M_A)  ;  y = (%m_B · M) / (100% · M_B)", "note": ""},
                    {"name": "Cách 2 (Lập tỉ lệ số mol nguyên tử khi chưa biết M)", "formula": "x : y = (%m_A / M_A) : (%m_B / M_B) = (m_A / M_A) : (m_B / M_B)", "note": "Rút gọn về tỉ lệ số nguyên tối giản"},
                ],
            },
        ],
        "Tính phần trăm khối lượng của nguyên tố Nitrogen (N) trong hai loại phân đạm là Ammonium nitrate (NH₄NO₃) và Urea ((NH₂)₂CO). Cho N = 14, H = 1, C = 12, O = 16.",
        "Với NH₄NO₃ (có 2 nguyên tử N): M = 2·14 + 4·1 + 3·16 = 80 (g/mol) ⇒ %N = (28 / 80) × 100% = 35%. Với (NH₂)₂CO (có 2 nguyên tử N): M = 2·(14 + 2) + 12 + 16 = 60 (g/mol) ⇒ %N = (28 / 60) × 100% ≈ 46,67% (Urea có hàm lượng đạm cao hơn!).",
        "Trong hợp chất Iron(III) oxide (Fe₂O₃, biết Fe = 56, O = 16), nguyên tố Iron (Fe) chiếm bao nhiêu phần trăm về khối lượng?",
        ["30%", "56%", "70%", "77,78%"],
        2,
        "Tính thành phần nguyên tố giúp đánh giá chất lượng quặng kim loại, hàm lượng hoạt chất trong dược phẩm và dinh dưỡng phân bón.",
        "Một oxide của nguyên tố Copper (Đồng - Cu) có khối lượng phân tử là 80 amu, trong đó Copper chiếm 80% về khối lượng, còn lại là Oxygen (biết Cu = 64, O = 16). Hãy xác định công thức hóa học của oxide đó.",
        "Gọi CTHH của oxide là CuₓOᵧ (M = 80 g/mol, %O = 100% − 80% = 20%). Ta có: x = (80% · 80) / (100% · 64) = 64 / 64 = 1 ; y = (20% · 80) / (100% · 16) = 16 / 16 = 1. Vậy công thức hóa học của oxide là CuO (Copper(II) oxide).",
    ),
    C(
        8,
        "mol-va-khoi-luong-mol",
        "Mol, Hằng số Avogadro, Khối lượng mol, Thể tích mol chất khí (đkc 24,79 L) & Tỉ khối chất khí",
        "🧪",
        "Làm chủ trọn bộ công thức chuyển đổi giữa Số mol (n), Số hạt (N), Khối lượng (m), Thể tích khí ở đkc (24,79 L/mol) và Tỉ khối chất khí d_A/B.",
        "Đếm những hạt vi mô bằng đơn vị Mol",
        "Vì nguyên tử và phân tử quá nhỏ bé không thể đếm từng hạt, các nhà hóa học sử dụng đơn vị 'Mol' (giống như 'tá' là 12 chiếc, thì 1 mol chứa đúng 6,022 × 10²³ hạt vi mô).",
        "Mol là lượng chất có chứa N_A = 6,022 × 10²³ hạt vi mô (nguyên tử, phân tử hoặc ion) của chất đó. Con số N_A = 6,022 × 10²³ mol⁻¹ được gọi là hằng số Avogadro.",
        "• Khối lượng mol (ký hiệu M, đơn vị g/mol) của một chất là khối lượng tính bằng gam của N_A nguyên tử hoặc phân tử chất đó (có trị số bằng khối lượng nguyên tử hoặc phân tử tính theo amu).\n"
        "• Thể tích mol của chất khí: Ở cùng điều kiện nhiệt độ và áp suất, 1 mol của BẤT KỲ CHẤT KHÍ NÀO đều chiếm thể tích bằng nhau. Ở điều kiện chuẩn (đkc: 25°C và 1 bar), 1 mol chất khí chiếm thể tích là 24,79 lít: V = n × 24,79 (L) (Lưu ý: ở đktc cũ 0°C và 1 atm là 22,4 L).\n"
        "• Tỉ khối của khí A đối với khí B (d_A/B = M_A / M_B) và đối với không khí (d_A/kk = M_A / 29) cho biết khí A nặng hay nhẹ hơn khí B (hoặc không khí) bao nhiêu lần.",
        [
            {
                "category": "I. Bộ 3 Công thức chuyển đổi Số mol (n - đơn vị mol)",
                "items": [
                    {"name": "1. Theo Số lượng hạt vi mô N", "formula": "n = N / N_A  ⇔  N = n · N_A  (với N_A ≈ 6,022 · 10²³ hạt/mol)", "note": ""},
                    {"name": "2. Theo Khối lượng chất m (gam)", "formula": "n = m / M  ⇔  m = n · M  ;  M = m / n", "note": "M: khối lượng mol (g/mol)"},
                    {"name": "3. Theo Thể tích chất khí V ở điều kiện chuẩn (25°C, 1 bar)", "formula": "n = V / 24,79  ⇔  V = n × 24,79 (lít)", "note": "Ở đktc cũ (0°C, 1 atm): V = n × 22,4 (lít)"},
                ],
            },
            {
                "category": "II. Tỉ khối của Chất khí (d_A/B) & Khối lượng mol trung bình hỗn hợp khí",
                "items": [
                    {"name": "Tỉ khối của khí A đối với khí B và đối với Không khí", "formula": "d_(A/B) = M_A / M_B  ;  d_(A/kk) = M_A / 29", "note": "d_(A/kk) > 1 (M_A > 29): nặng hơn không khí ; d_(A/kk) < 1: nhẹ hơn không khí"},
                    {"name": "Khối lượng mol trung bình của hỗn hợp khí", "formula": "M̄ = m_hh / n_hh = (n₁·M₁ + n₂·M₂) / (n₁ + n₂)", "note": "Vì cùng điều kiện T, p nên tỉ lệ số mol chất khí bằng tỉ lệ thể tích!"},
                ],
            },
        ],
        "Tính thể tích ở điều kiện chuẩn (25°C, 1 bar) và số phân tử có trong 8,8 gam khí Carbon dioxide (CO₂, biết C = 12, O = 16). Khí CO₂ nặng hay nhẹ hơn không khí bao nhiêu lần?",
        "Ta có M_CO₂ = 12 + 2·16 = 44 (g/mol). Số mol CO₂ là: n = m / M = 8,8 / 44 = 0,2 (mol). Thể tích ở đkc là: V = 0,2 × 24,79 = 4,958 (lít). Số phân tử CO₂ là: N = 0,2 × 6,022·10²³ = 1,2044 · 10²³ (phân tử). Tỉ khối so với không khí: d_(CO₂/kk) = 44 / 29 ≈ 1,52 (CO₂ nặng hơn không khí 1,52 lần).",
        "Ở điều kiện chuẩn (25°C và 1 bar), 0,5 mol khí Hydrogen (H₂) chiếm thể tích bằng bao nhiêu lít?",
        ["11,20 lít", "12,395 lít", "24,79 lít", "49,58 lít"],
        1,
        "Tính toán lượng chất theo mol là bước đầu tiên bắt buộc của mọi bài toán hóa học, pha chế dung dịch và tính lượng khí phát thải.",
        "Một hỗn hợp khí X ở điều kiện chuẩn gồm 0,2 mol khí Nitrogen (N₂, M = 28) và 0,3 mol khí Oxygen (O₂, M = 32). Hãy tính tổng thể tích của hỗn hợp khí X (ở đkc), khối lượng mol trung bình M̄ của hỗn hợp X và tỉ khối của X đối với khí Hydrogen (H₂, M = 2).",
        "Tổng số mol hỗn hợp: n_X = 0,2 + 0,3 = 0,5 (mol). Thể tích hỗn hợp X ở đkc: V = 0,5 × 24,79 = 12,395 (lít). Tổng khối lượng: m_X = 0,2·28 + 0,3·32 = 5,6 + 9,6 = 15,2 (g). Khối lượng mol trung bình: M̄_X = 15,2 / 0,5 = 30,4 (g/mol). Tỉ khối đối với H₂: d_(X/H₂) = 30,4 / 2 = 15,2.",
    ),
    C(
        8,
        "phuong-trinh-hoa-hoc",
        "Phương trình Hóa học, Tính theo Phương trình Hóa học & Hiệu suất phản ứng (H%)",
        "⚗️",
        "Cân bằng phương trình hóa học, giải bài toán tính theo PTHH (kể cả bài toán chất dư - chất hết) và tính hiệu suất phản ứng H%.",
        "Bản thiết kế định lượng của phản ứng hóa học",
        "Phương trình hóa học không chỉ cho biết chất nào phản ứng tạo ra chất nào, mà hệ số cân bằng còn cho biết chính xác tỉ lệ số mol giữa tất cả các chất trong phản ứng.",
        "Phương trình hóa học (PTHH) biểu diễn ngắn gọn phản ứng hóa học bằng công thức hóa học của các chất tham gia và chất sản phẩm kèm theo các hệ số thích hợp sao cho số nguyên tử của mỗi nguyên tố ở hai vế bằng nhau.",
        "• Nguyên tắc vàng khi cân bằng PTHH: CHỈ ĐƯỢC viết thêm hệ số đằng trước CTHH, TUYỆT ĐỐI KHÔNG được thay đổi chỉ số chân trong CTHH đã viết đúng!\n"
        "• Ý nghĩa của PTHH aA + bB → cC + dD: Tỉ lệ số phân tử (hay tỉ lệ số mol) là n_A : n_B : n_C : n_D = a : b : c : d.\n"
        "• Bài toán cho biết lượng của CẢ HAI chất tham gia A và B (Bài toán lượng chất dư): So sánh tỉ số n_A(ban_đầu)/a và n_B(ban_đầu)/b. Tỉ số nào NHỎ HƠN thì chất đó phản ứng HẾT, chất kia CÒN DƯ; mọi tính toán lượng sản phẩm phải tính theo chất phản ứng HẾT!\n"
        "• Hiệu suất phản ứng (H%): Trong thực tế, do nhiều nguyên nhân, lượng sản phẩm thu được thực tế (m_thực_tế hoặc n_thực_tế) thường nhỏ hơn lượng tính theo lý thuyết PTHH (0% < H% ≤ 100%).",
        [
            {
                "category": "I. Tỉ lệ Số mol theo PTHH: aA + bB → cC + dD",
                "items": [
                    {"name": "Hệ thức tỉ lệ số mol phản ứng", "formula": "n_A(pư) / a = n_B(pư) / b = n_C(tạo_thành) / c = n_D(tạo_thành) / d", "note": ""},
                    {"name": "Quy tắc xét Chất hết – Chất dư", "formula": "Nếu n_A(bđ) / a < n_B(bđ) / b  ⇒  A phản ứng HẾT, B còn DƯ ; Tính mọi chất theo n_A(bđ)", "note": "Lượng B dư: n_B(dư) = n_B(bđ) − (b/a)·n_A(bđ)"},
                ],
            },
            {
                "category": "II. Công thức tính Hiệu suất phản ứng (H%)",
                "items": [
                    {"name": "Tính H% theo Sản phẩm hoặc Chất tham gia", "formula": "H% = (n_sp_thực_tế / n_sp_lý_thuyết) × 100% = (n_tg_thực_tế_pư / n_tg_ban_đầu) × 100%", "note": "Có thể thay số mol n bằng khối lượng m hoặc thể tích khí V"},
                    {"name": "Mẹo ghi nhớ nhanh ('Phải nhân – Trái chia')", "formula": "m_sản_phẩm(thực_tế) = m_sp(lý_thuyết) × H%  ;  m_tham_gia(cần_dùng) = m_tg(lý_thuyết) / H%", "note": "Tìm chất bên PHẢI mũi tên thì NHÂN H%; tìm chất bên TRÁI mũi tên thì CHIA H%"},
                ],
            },
        ],
        "Cho 5,6 gam Iron (Fe, M = 56) tác dụng với dung dịch chứa 0,25 mol Hydrochloric acid (HCl) theo sơ đồ: Fe + HCl → FeCl₂ + H₂↑. Hãy lập PTHH, xác định chất nào còn dư sau phản ứng và tính thể tích khí H₂ thu được ở đkc (25°C, 1 bar).",
        "PTHH cân bằng: Fe + 2HCl → FeCl₂ + H₂↑. Số mol Fe ban đầu: n_Fe = 5,6 / 56 = 0,1 (mol). Xét tỉ lệ: n_Fe / 1 = 0,1/1 = 0,1 < n_HCl / 2 = 0,25/2 = 0,125 ⇒ Fe phản ứng HẾT, HCl còn DƯ. Tính theo Fe: n_H₂ = n_Fe = 0,1 (mol) (và n_HCl_dư = 0,25 − 2·0,1 = 0,05 mol). Thể tích khí H₂ (đkc) là: V = 0,1 × 24,79 = 2,479 (lít).",
        "Cân bằng phương trình hóa học: a Al + b O₂ ──(t°)──► c Al₂O₃. Bộ hệ số nguyên tối giản (a, b, c) lần lượt là:",
        ["(2, 3, 1)", "(4, 3, 2)", "(2, 1, 1)", "(4, 2, 2)"],
        1,
        "Tính toán theo PTHH và hiệu suất giúp các kỹ sư hóa học xác định chính xác lượng nguyên liệu cần nhập cho nhà máy mà không gây lãng phí.",
        "Nung 200 kg đá vôi (chứa CaCO₃ nguyên chất, M = 100 g/mol) ở nhiệt độ cao theo PTHH: CaCO₃ ──(t°)──► CaO + CO₂↑. Biết hiệu suất của phản ứng nhiệt phân là H = 85%. Tính khối lượng vôi sống CaO (M = 56 g/mol) thực tế thu được.",
        "Theo PTHH, cứ 100 kg CaCO₃ phản ứng hoàn toàn (lý thuyết 100%) thì tạo ra 56 kg CaO. Vậy từ 200 kg CaCO₃, khối lượng CaO lý thuyết là: m_CaO(lt) = (200 · 56) / 100 = 112 (kg). Vì hiệu suất H = 85% (CaO nằm ở vế phải - sản phẩm nên NHÂN H%), khối lượng CaO thực tế thu được là: m_CaO(tt) = 112 × 85% = 95,2 (kg).",
    ),
    C(
        8,
        "dung-dich-nong-do",
        "Nồng độ Dung dịch (C% và C_M), Chuyển đổi C% ⇄ C_M & Bài toán Pha chế dung dịch",
        "🥛",
        "Thành thạo công thức nồng độ phần trăm C%, nồng độ mol C_M = n/V, công thức liên hệ C_M = (10·D·C%)/M và quy tắc đường chéo pha trộn.",
        "Kiểm soát độ đậm đặc của dung dịch trong phòng thí nghiệm",
        "Trong y học và phòng thí nghiệm, mỗi dung dịch đều phải được pha chế ở một nồng độ chính xác (theo phần trăm khối lượng C% hoặc theo số mol trên lít C_M).",
        "Nồng độ phần trăm (C%) cho biết số gam chất tan có trong 100 gam dung dịch. Nồng độ mol (C_M, đơn vị mol/L hay M) cho biết số mol chất tan có trong 1 lít (1 000 mL) dung dịch.",
        "• Công thức nồng độ phần trăm: C% = (m_ct / m_dd) × 100% (trong đó m_dd = m_ct + m_H₂O, hoặc nếu trộn có phản ứng tạo khí/kết tủa thì m_dd_sau = Σm_trước − m_khí − m_kết_tủa).\n"
        "• Công thức nồng độ mol: C_M = n / V_dd (Lưu ý: Thể tích dung dịch V_dd bắt buộc phải đổi ra đơn vị LÍT - L: 1 L = 1 000 mL!).\n"
        "• Công thức vàng chuyển đổi trực tiếp giữa C_M và C% khi biết khối lượng riêng D (g/mL) của dung dịch: C_M = (10 · D · C%) / M.\n"
        "• Bài toán pha loãng hoặc trộn hai dung dịch cùng chất tan (bảo toàn số mol chất tan n_sau = n₁ + n₂ hoặc bảo toàn khối lượng chất tan m_ct_sau = m_ct1 + m_ct2).",
        [
            {
                "category": "I. Công thức Nồng độ phần trăm (C%) & Nồng độ mol (C_M)",
                "items": [
                    {"name": "Nồng độ phần trăm C%", "formula": "C% = (m_ct / m_dd) × 100%  ⇒  m_ct = (m_dd · C%) / 100%  ;  m_dd = (m_ct · 100%) / C%", "note": "m_ct, m_dd tính bằng gam (g)"},
                    {"name": "Nồng độ mol C_M (mol/L hay M)", "formula": "C_M = n / V_dd  ⇒  n = C_M · V_dd  ;  V_dd = n / C_M", "note": "V_dd tính bằng LÍT (L): V(L) = V(mL) / 1000"},
                    {"name": "Khối lượng dung dịch sau phản ứng hóa học", "formula": "m_dd_sau = m_các_chất_cho_vào − m_kết_tủa(↓) − m_khí(↑)", "note": "Rất quan trọng khi tính C% sau phản ứng!"},
                ],
            },
            {
                "category": "II. Công thức chuyển đổi C_M ⇄ C% & Pha loãng dung dịch",
                "items": [
                    {"name": "Liên hệ giữa C_M, C%, KLR D (g/mL) và Khối lượng mol M", "formula": "C_M = (10 · D · C%) / M  ⇔  C% = (C_M · M) / (10 · D)", "note": "D đơn vị là g/mL (hoặc g/cm³)"},
                    {"name": "Bảo toàn chất tan khi Pha loãng (thêm nước) hoặc Pha trộn", "formula": "Pha loãng: C₁ · V₁ = C₂ · V₂ (hoặc m_dd1 · C₁% = m_dd2 · C₂%) ; Trộn: n_tổng = C₁V₁ + C₂V₂", "note": ""},
                ],
            },
        ],
        "Hòa tan hoàn toàn 16 gam Copper(II) sulfate (CuSO₄, M = 160 g/mol) vào nước để thu được 200 mL dung dịch. Tính nồng độ mol (C_M) của dung dịch thu được.",
        "Số mol CuSO₄ là: n = m / M = 16 / 160 = 0,1 (mol). Đổi thể tích dung dịch: V = 200 mL = 0,2 (L). Nồng độ mol của dung dịch là: C_M = n / V = 0,1 / 0,2 = 0,5 (M).",
        "Dung dịch Sulfuric acid (H₂SO₄, M = 98 g/mol) có nồng độ C% = 98% và khối lượng riêng D = 1,84 g/mL. Nồng độ mol C_M của dung dịch acid đặc này là:",
        ["9,8 M", "18,4 M", "1,84 M", "10,0 M"],
        1,
        "Kiểm soát nồng độ giúp pha chế thuốc tiêm truyền, dung dịch thủy canh cây trồng, nước muối sát khuẩn và chuẩn độ hóa học.",
        "Cần lấy bao nhiêu mL dung dịch HCl 2 M trộn với bao nhiêu mL dung dịch HCl 0,5 M để thu được 600 mL dung dịch HCl có nồng độ 1 M (coi thể tích hao hụt không đáng kể)?",
        "Gọi thể tích dung dịch HCl 2 M và 0,5 M cần lấy lần lượt là V₁ và V₂ (L). Tổng thể tích: V₁ + V₂ = 0,6 (L) (1). Bảo toàn số mol HCl: 2·V₁ + 0,5·V₂ = 1 · 0,6 = 0,6 (mol) (2). Giải hệ (1) và (2) được: V₁ = 0,2 (L) = 200 (mL) và V₂ = 0,4 (L) = 400 (mL).",
    ),
    C(
        8,
        "axit-bazo-muoi",
        "Acid – Base – Thang pH – Muối & Điều kiện phản ứng trao đổi",
        "🍋",
        "Nhận diện công thức và tính chất hóa học của Acid, Base (Kiềm), Muối, thang đo pH và điều kiện xảy ra phản ứng trao đổi trong dung dịch.",
        "Thế giới pH từ quả chanh đến xà phòng",
        "Vị chua của chanh và giấm ăn là do Acid; cảm giác nhờn của nước vôi và xà phòng là do Base; còn vị mặn của nước biển là do các loại Muối.",
        "Theo thuyết điện li cơ bản: Acid là những hợp chất trong phân tử có nguyên tử Hydrogen (H) liên kết với gốc acid, khi tan trong nước tạo ra ion H⁺; Base là những hợp chất trong phân tử có nguyên tử kim loại liên kết với nhóm hydroxide (–OH), khi tan trong nước tạo ra ion OH⁻; Muối là hợp chất tạo bởi ion kim loại (hoặc NH₄⁺) liên kết với gốc acid.",
        "• Thang pH (từ 1 đến 14) đo độ acid/base của dung dịch: pH < 7 là môi trường ACID (làm quỳ tím hóa ĐỎ, phenolphthalein không màu); pH = 7 là môi trường TRUNG TÍNH; pH > 7 là môi trường BASE/KIỀM (làm quỳ tím hóa XANH, phenolphthalein hóa HỒNG).\n"
        "• Bốn base tan mạnh trong nước (gọi là KIỀM): NaOH, KOH, Ca(OH)₂, Ba(OH)₂; các base khác như Cu(OH)₂ (kết tủa xanh lam), Fe(OH)₃ (kết tủa nâu đỏ), Mg(OH)₂ (kết tủa trắng) không tan trong nước.\n"
        "• Tính chất hóa học của Acid (HCl, H₂SO₄ loãng): làm quỳ tím hóa đỏ; tác dụng với kim loại đứng trước H (Mg, Al, Zn, Fe — trừ Cu, Ag, Au!) giải phóng khí H₂; tác dụng với Base và Basic oxide tạo muối và nước; tác dụng với muối carbonate tạo khí CO₂.\n"
        "• Điều kiện để phản ứng trao đổi giữa các dung dịch (Muối + Acid, Muối + Kiềm, Muối + Muối) xảy ra: Sản phẩm phải có chất KẾT TỦA (↓), hoặc chất KHÍ (↑), hoặc chất điện li yếu như H₂O!",
        [
            {
                "category": "I. Cấu tạo, Chất chỉ thị màu & Thang đo pH",
                "items": [
                    {"name": "Acid (HₙA) & Base (M(OH)ₘ) & Muối (MₓAᵧ)", "formula": "Acid → H⁺ + Aⁿ⁻  ;  Base tan (Kiềm: NaOH, KOH, Ca(OH)₂, Ba(OH)₂) → Mᵐ⁺ + m OH⁻", "note": ""},
                    {"name": "Thang pH & Đổi màu chất chỉ thị", "formula": "pH < 7 (Acid): Quỳ tím → ĐỎ  ;  pH = 7 (Trung tính)  ;  pH > 7 (Base): Quỳ tím → XANH, Phenolphthalein → HỒNG", "note": "pH = −log[H⁺]"},
                ],
            },
            {
                "category": "II. Các phản ứng đặc trưng của Acid, Base & Điều kiện phản ứng trao đổi",
                "items": [
                    {"name": "1. Acid (HCl, H₂SO₄ loãng) + Kim loại (trước H)", "formula": "Kim loại (Mg, Al, Zn, Fe) + Acid → Muối + H₂↑  (Ví dụ: Fe + 2HCl → FeCl₂ + H₂↑)", "note": "Cu, Ag, Au KHÔNG phản ứng với HCl và H₂SO₄ loãng"},
                    {"name": "2. Phản ứng Trung hòa (Acid + Base)", "formula": "Acid + Base → Muối + H₂O  (Bản chất ion: H⁺ + OH⁻ → H₂O)", "note": "Ví dụ: H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O"},
                    {"name": "3. Điều kiện phản ứng trao đổi trong dung dịch", "formula": "Chỉ xảy ra khi tạo thành KẾT TỦA (như BaSO₄↓ trắng, AgCl↓ trắng, CaCO₃↓ trắng, Cu(OH)₂↓ xanh) hoặc KHÍ (CO₂↑, SO₂↑, NH₃↑) hoặc H₂O", "note": ""},
                ],
            },
        ],
        "Cho 100 mL dung dịch H₂SO₄ 1 M tác dụng vừa đủ với dung dịch Barium chloride (BaCl₂). Viết PTHH, nêu hiện tượng quan sát được và tính khối lượng chất kết tủa tạo thành (biết Ba = 137, S = 32, O = 16, Cl = 35,5).",
        "PTHH: H₂SO₄ + BaCl₂ → BaSO₄↓ + 2HCl. Hiện tượng: xuất hiện kết tủa màu trắng không tan trong acid (BaSO₄). Số mol H₂SO₄ là: n = 0,1 · 1 = 0,1 (mol). Theo PTHH: n_BaSO₄ = n_H₂SO₄ = 0,1 (mol). Khối lượng kết tủa BaSO₄ (M = 233 g/mol) là: m = 0,1 · 233 = 23,3 (gam).",
        "Cặp chất nào dưới đây trong dung dịch sẽ XẢY RA phản ứng trao đổi?",
        [
            "NaCl + KNO₃",
            "Na₂CO₃ + HCl (tạo khí CO₂↑ và H₂O)",
            "CuSO₄ + HCl",
            "NaOH + KCl",
        ],
        1,
        "Ứng dụng vôi tôi Ca(OH)₂ để khử chua đất trồng trọt (tăng pH đất), dùng thuốc kháng acid Mg(OH)₂/NaHCO₃ chữa đau dạ dày và xử lý nước thải công nghiệp.",
        "Dịch vị dạ dày người chứa Hydrochloric acid (HCl) với pH khoảng 1,5 – 2,5 giúp tiêu hóa thức ăn. Khi nồng độ acid vượt mức gây bệnh ợ chua và đau dạ dày, bác sĩ thường kê đơn thuốc có chứa bột Baking soda (NaHCO₃) hoặc Magnesium hydroxide (Mg(OH)₂). Hãy viết các PTHH giải thích tác dụng của thuốc.",
        "Các chất có tính base yếu hoặc muối hydrogen carbonate trong thuốc sẽ phản ứng trung hòa bớt lượng HCl dư trong dạ dày, làm tăng pH dịch vị về mức bình thường: Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O và NaHCO₃ + HCl → NaCl + CO₂↑ + H₂O.",
    ),
    C(
        8,
        "oxide-phan-bon",
        "Oxide (Acidic, Basic, Lưỡng tính, Trung tính) & Phân bón Hóa học (Đạm - Lân - Kali - NPK)",
        "🌾",
        "Phân loại 4 nhóm Oxide theo tính chất hóa học và nắm vững thành phần, vai trò, độ dinh dưỡng của các loại phân bón hóa học.",
        "Từ đá vôi xây dựng đến dinh dưỡng cho cây trồng",
        "Oxide có mặt khắp nơi: cát thạch anh (SiO₂), vôi sống (CaO), quặng sắt (Fe₂O₃), khí nhà kính (CO₂). Đồng thời, cây trồng cần các nguyên tố đa lượng N, P, K từ phân bón hóa học để sinh trưởng và cho năng suất cao.",
        "Oxide là hợp chất của hai nguyên tố, trong đó có một nguyên tố là Oxygen (O). Dựa vào tính chất hóa học, oxide được chia thành 4 loại: Basic oxide, Acidic oxide, Amphoteric oxide (Oxide lưỡng tính) và Neutral oxide (Oxide trung tính).",
        "• Basic oxide (Oxide base: Na₂O, K₂O, CaO, BaO, CuO, FeO, Fe₂O₃, MgO...): tác dụng với dung dịch Acid tạo thành muối và nước; một số basic oxide của kim loại kiềm/kiềm thổ (Na₂O, K₂O, CaO, BaO) tác dụng trực tiếp với nước tạo dung dịch Kiềm.\n"
        "• Acidic oxide (Oxide acid: CO₂, SO₂, SO₃, P₂O₅, N₂O₅, SiO₂...): tác dụng với dung dịch Base (kiềm) tạo thành muối và nước; đa số tác dụng với nước tạo dung dịch Acid (trừ SiO₂).\n"
        "• Amphoteric oxide (Oxide lưỡng tính: Al₂O₃, ZnO, Cr₂O₃): vừa tác dụng được với dung dịch Acid, vừa tác dụng được với dung dịch Kiềm mạnh (NaOH, KOH) tạo muối và nước.\n"
        "• Neutral oxide (Oxide trung tính / không tạo muối: CO, NO, N₂O): KHÔNG tác dụng với acid, base và nước.\n"
        "• Ba nhóm phân bón hóa học đơn và phân hỗn hợp NPK:\n"
        "  1. Phân đạm (cung cấp N — kích thích cây phát triển thân, lá; độ dinh dưỡng tính bằng %N): Urea (NH₂)₂CO, NH₄NO₃, (NH₄)₂SO₄.\n"
        "  2. Phân lân (cung cấp P — kích thích bộ rễ, ra hoa; độ dinh dưỡng tính bằng %P₂O₅): Superphosphate Ca(H₂PO₄)₂.\n"
        "  3. Phân kali (cung cấp K — giúp cây cứng cáp, chịu hạn, tạo củ quả ngọt; độ dinh dưỡng tính bằng %K₂O): KCl, K₂SO₄.",
        [
            {
                "category": "I. Bốn loại Oxide & Phản ứng hóa học đặc trưng",
                "items": [
                    {"name": "1. Basic oxide (CaO, CuO, Fe₂O₃...)", "formula": "Basic oxide + Acid → Muối + H₂O  (Ví dụ: CuO + 2HCl → CuCl₂ + H₂O ; CaO + H₂O → Ca(OH)₂)", "note": ""},
                    {"name": "2. Acidic oxide (CO₂, SO₂, SO₃, P₂O₅...)", "formula": "Acidic oxide + Kiềm → Muối + H₂O  (Ví dụ: CO₂ + Ca(OH)₂ → CaCO₃↓ + H₂O ; SO₃ + H₂O → H₂SO₄)", "note": "Tác dụng với Basic oxide tan: CaO + CO₂ → CaCO₃"},
                    {"name": "3. Oxide lưỡng tính (Al₂O₃, ZnO) & 4. Oxide trung tính (CO, NO)", "formula": "Al₂O₃ tác dụng cả HCl và NaOH  ;  CO, NO không tạo muối với acid hay base", "note": ""},
                ],
            },
            {
                "category": "II. Phân bón Hóa học & Chỉ số trên bao bì Phân NPK",
                "items": [
                    {"name": "Tiêu chuẩn đánh giá Độ dinh dưỡng", "formula": "Phân Đạm: %m_N  ;  Phân Lân: %m_P₂O₅  ;  Phân Kali: %m_K₂O", "note": ""},
                    {"name": "Ý nghĩa 3 con số trên bao phân NPK (ví dụ NPK 16–16–8)", "formula": "16% khối lượng N  ;  16% khối lượng P₂O₅  ;  8% khối lượng K₂O", "note": "Giúp tính chính xác khối lượng N, P, K bón cho cây"},
                ],
            },
        ],
        "Dẫn 0,15 mol khí Carbon dioxide (CO₂) vào bình đựng dung dịch nước vôi trong Ca(OH)₂ lấy dư. Viết PTHH và tính khối lượng kết tủa trắng thu được (biết Ca = 40, C = 12, O = 16).",
        "Vì Ca(OH)₂ dư nên toàn bộ CO₂ chuyển hết thành kết tủa Calcium carbonate: CO₂ + Ca(OH)₂ → CaCO₃↓ + H₂O. Số mol kết tủa là: n_CaCO₃ = n_CO₂ = 0,15 (mol). Khối lượng kết tủa trắng thu được là: m = 0,15 · 100 = 15 (gam).",
        "Dãy các chất nào sau đây gồm một Oxide lưỡng tính và một Oxide trung tính (không tạo muối)?",
        [
            "CaO và CO₂",
            "Al₂O₃ và CO",
            "Fe₂O₃ và SO₂",
            "ZnO và SO₃",
        ],
        1,
        "Chọn gói hút ẩm vôi sống CaO cho thực phẩm và tính toán công thức phối trộn phân bón NPK cân đối cho từng giai đoạn sinh trưởng của cây trồng.",
        "Tại sao người nông dân tuyệt đối KHÔNG ĐƯỢC trộn chung phân đạm Ammonium (như NH₄NO₃, (NH₄)₂SO₄, NH₄Cl) với vôi tôi Ca(OH)₂ hoặc tro bếp (chứa K₂CO₃ có tính kiềm) để bón cùng lúc cho ruộng lúa?",
        "Vì khi trộn phân đạm chứa ion Ammonium (NH₄⁺) với chất có tính kiềm như vôi Ca(OH)₂ hoặc tro bếp, sẽ xảy ra phản ứng trao đổi giải phóng khí Ammonia (NH₃) bay mất vào không khí: 2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2NH₃↑ + 2H₂O. Điều này làm mất đi lượng đạm (Nitrogen) quý giá của phân bón và gây ngộ độc cho lá cây.",
    ),
    C(
        8,
        "oxi-hoa-khu",
        "Sự Oxi hóa, Phản ứng Cháy – Nổ & Tốc độ phản ứng - Chất xúc tác cơ bản",
        "🔥",
        "Hiểu sự oxi hóa của chất với oxygen, phản ứng tỏa nhiệt khi đốt nhiên liệu và các yếu tố làm thay đổi tốc độ phản ứng.",
        "Từ ngọn lửa bếp gas đến động cơ tên lửa",
        "Sự tác dụng của một chất với oxygen được gọi là sự oxi hóa: có sự oxi hóa diễn ra rất nhanh kèm tỏa nhiệt và phát sáng (sự cháy), nhưng cũng có sự oxi hóa diễn ra âm thầm như sắt bị gỉ hay sự hô hấp.",
        "Sự oxi hóa (theo khái niệm cơ bản ở THCS) là sự tác dụng của oxygen với một chất (đơn chất hoặc hợp chất). Phản ứng cháy là sự oxi hóa có tỏa nhiệt và phát sáng.",
        "• Phản ứng của Oxygen với kim loại (3Fe + 2O₂ ──(t°)──► Fe₃O₄; 2Mg + O₂ ──(t°)──► 2MgO), với phi kim (C + O₂ ──(t°)──► CO₂; S + O₂ ──(t°)──► SO₂; 4P + 5O₂ ──(t°)──► 2P₂O₅) và đốt cháy hợp chất (CH₄ + 2O₂ ──(t°)──► CO₂ + 2H₂O).\n"
        "• Tốc độ phản ứng chỉ mức độ diễn ra nhanh hay chậm của phản ứng hóa học.\n"
        "• Năm yếu tố làm tăng tốc độ phản ứng: 1) Tăng nồng độ chất phản ứng; 2) Tăng nhiệt độ; 3) Tăng áp suất (với chất khí); 4) Tăng diện tích bề mặt tiếp xúc (đập nhỏ, nghiền mịn chất rắn); 5) Sử dụng Chất xúc tác (chất làm tăng tốc độ phản ứng nhưng vẫn giữ nguyên về lượng và bản chất hóa học sau khi phản ứng kết thúc).",
        [
            {
                "category": "I. Các Phương trình Hóa học của Sự Oxi hóa & Sự Cháy",
                "items": [
                    {"name": "Đốt cháy Kim loại & Phi kim", "formula": "3Fe + 2O₂ → Fe₃O₄ (Iron(II,III) oxide) ; 2Cu + O₂ → 2CuO ; 2H₂ + O₂ → 2H₂O", "note": "Hỗn hợp V_H₂ : V_O₂ = 2 : 1 là hỗn hợp nổ mạnh nhất"},
                    {"name": "Đốt cháy Hydrocarbon / Nhiên liệu", "formula": "CH₄ + 2O₂ → CO₂ + 2H₂O ; C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O", "note": "Nếu thiếu O₂ sẽ sinh ra muội than (C) và khí CO cực độc!"},
                ],
            },
            {
                "category": "II. Năm yếu tố ảnh hưởng đến Tốc độ phản ứng",
                "items": [
                    {"name": "Các yếu tố làm TĂNG tốc độ phản ứng", "formula": "Tăng Nồng độ (C) + Tăng Nhiệt độ (t°) + Tăng Áp suất (p, với khí) + Đập nhỏ chất rắn (tăng S) + Dùng Chất xúc tác", "note": "Enzyme sinh học là chất xúc tác trong cơ thể sống"},
                ],
            },
        ],
        "Để điều chế khí Oxygen trong phòng thí nghiệm hoặc làm vết thương sủi bọt sát trùng, người ta phân hủy dung dịch Hydrogen peroxide (nước oxy già H₂O₂) có mặt bột Manganese dioxide (MnO₂) làm xúc tác: 2H₂O₂ ──(MnO₂)──► 2H₂O + O₂↑. Hỏi vai trò của MnO₂ là gì và nếu phân hủy hết 0,2 mol H₂O₂ thì thu được bao nhiêu lít khí O₂ ở đkc?",
        "MnO₂ đóng vai trò là CHẤT XÚC TÁC giúp phản ứng phân hủy H₂O₂ diễn ra nhanh gấp hàng nghìn lần ở nhiệt độ thường, và khối lượng MnO₂ không bị mất đi sau phản ứng. Theo PTHH: n_O₂ = (1/2) · n_H₂O₂ = 0,1 (mol). Thể tích khí O₂ ở đkc là: V = 0,1 × 24,79 = 2,479 (lít).",
        "Tại sao người ta thường chẻ nhỏ củi trước khi đun nấu và tạo nhiều lỗ rỗng trong viên than tổ ong?",
        [
            "Để giảm khối lượng của củi và than",
            "Để làm tăng diện tích bề mặt tiếp xúc của nhiên liệu với khí Oxygen trong không khí, giúp phản ứng cháy diễn ra nhanh hơn và hoàn toàn hơn",
            "Để củi và than đóng vai trò là chất xúc tác",
            "Để làm giảm nhiệt độ bắt cháy của than",
        ],
        1,
        "Thiết kế buồng đốt động cơ phun nhiên liệu dạng sương mù, sử dụng bộ xúc tác xử lý khí thải ô tô và bảo quản thực phẩm trong tủ lạnh.",
        "Đốt cháy hoàn toàn 3,2 gam khí Methane (CH₄, M = 16 g/mol) cần vừa đủ V lít không khí (ở đkc 25°C, 1 bar). Biết khí Oxygen chiếm 20% thể tích không khí. Hãy viết PTHH và tính giá trị của V cùng khối lượng nước tạo thành.",
        "PTHH: CH₄ + 2O₂ ──(t°)──► CO₂ + 2H₂O. Số mol CH₄: n_CH₄ = 3,2 / 16 = 0,2 (mol). Theo PTHH: n_O₂ = 2 · n_CH₄ = 0,4 (mol) và n_H₂O = 2 · n_CH₄ = 0,4 (mol). Thể tích khí O₂ ở đkc là: V_O₂ = 0,4 × 24,79 = 9,916 (lít). Vì O₂ chiếm 20% (1/5) thể tích không khí nên thể tích không khí cần dùng là: V_kk = 5 × 9,916 = 49,58 (lít). Khối lượng nước tạo thành: m_H₂O = 0,4 × 18 = 7,2 (gam).",
    ),

    # =========================================================
    # HÓA HỌC LỚP 9 (7 BÀI)
    # =========================================================
    C(
        9,
        "kim-loai",
        "Tính chất Vật lý - Hóa học của Kim loại, Hợp kim & Tách kim loại (Luyện kim)",
        "🔩",
        "Nắm vững 4 tính chất vật lý chung (do electron tự do), tính chất hóa học của kim loại, các hợp kim quan trọng (Gang, Thép, Duralumin) và 3 phương pháp điều chế kim loại.",
        "Từ quặng Bauxite, Hematite đến những tòa nhà chọc trời",
        "Kim loại chiếm hơn 80% các nguyên tố trong Bảng tuần hoàn. Nhờ cấu trúc mạng tinh thể có các electron tự do chuyển động, kim loại có những tính chất vật lý và cơ học vô cùng quý giá.",
        "Kim loại có 4 tính chất vật lý chung (gây ra bởi các electron tự do trong mạng tinh thể kim loại): Tính dẻo, Tính dẫn điện, Tính dẫn nhiệt và Ánh kim. Về mặt hóa học, kim loại thể hiện tính khử (dễ nhường electron tạo ion dương): tác dụng với phi kim, với dung dịch acid và với dung dịch muối.",
        "• Các kim loại có tính chất vật lý cực trị cần nhớ: Dẫn điện & dẫn nhiệt tốt nhất là Ag > Cu > Au > Al > Fe; Dẻo nhất là Au (vàng); Cứng nhất là Cr (Chromium); Nhiệt độ nóng chảy cao nhất là W (Tungsten/Vonfram ~3410°C – làm dây tóc bóng đèn), thấp nhất là Hg (Thủy ngân −39°C – kim loại duy nhất ở thể lỏng ở nhiệt độ thường); Nhẹ nhất là Li (D = 0,53 g/cm³), nặng nhất là Os.\n"
        "• Hợp kim là vật liệu kim loại có chứa một kim loại cơ bản và một số kim loại hoặc phi kim khác (Gang và Thép là hợp kim của Fe với C: Gang chứa 2% – 5% C; Thép chứa < 2% C; Thép không gỉ Inox chứa thêm Cr và Ni; Hợp kim nhôm Duralumin siêu nhẹ dùng chế tạo vỏ máy bay).\n"
        "• Ba phương pháp tách kim loại khỏi quặng (oxide): 1) Điện phân nóng chảy (cho kim loại mạnh K, Na, Ca, Mg, Al: 2Al₂O₃ → 4Al + 3O₂); 2) Nhiệt luyện (dùng C, CO, H₂, Al khử oxide của kim loại trung bình Zn, Fe, Cu ở nhiệt độ cao); 3) Thủy luyện (dùng kim loại mạnh hơn đẩy kim loại yếu như Cu, Ag ra khỏi dung dịch muối).",
        [
            {
                "category": "I. Tính chất Hóa học đặc trưng của Kim loại",
                "items": [
                    {"name": "1. Tác dụng với Phi kim (O₂, Cl₂, S)", "formula": "3Fe + 2O₂ ──(t°)──► Fe₃O₄ ; 2Fe + 3Cl₂ ──(t°)──► 2FeCl₃ (hóa trị III!) ; Fe + S ──(t°)──► FeS (hóa trị II!)", "note": "Ag, Au không bị oxi hóa bởi O₂ ở mọi nhiệt độ"},
                    {"name": "2. Tác dụng với Dung dịch Acid (HCl, H₂SO₄ loãng)", "formula": "Kim loại (đứng trước H) + HCl / H₂SO₄ loãng → Muối (hóa trị thấp) + H₂↑", "note": "Ví dụ: Fe + H₂SO₄(loãng) → FeSO₄ + H₂↑ ; 2Al + 6HCl → 2AlCl₃ + 3H₂↑"},
                    {"name": "3. Tác dụng với Dung dịch Muối", "formula": "Kim loại mạnh hơn (trừ K, Na, Ca, Ba) + Muối của kim loại yếu hơn → Muối mới + Kim loại mới", "note": "Ví dụ: Fe + CuSO₄ → FeSO₄ + Cu↓"},
                ],
            },
            {
                "category": "II. Ba phương pháp Tách Kim loại trong Công nghiệp Luyện kim",
                "items": [
                    {"name": "1. Điện phân nóng chảy (Kim loại mạnh: K, Na, Mg, Al)", "formula": "2Al₂O₃ ──(đpnc, cryolite)──► 4Al + 3O₂↑  ;  2NaCl ──(đpnc)──► 2Na + Cl₂↑", "note": "Quặng Bauxite chứa Al₂O₃"},
                    {"name": "2. Nhiệt luyện (Kim loại trung bình: Zn, Fe, Sn, Pb, Cu)", "formula": "Fe₂O₃ + 3CO ──(t° cao, lò cao)──► 2Fe + 3CO₂↑  ;  CuO + H₂ ──(t°)──► Cu + H₂O", "note": "CO, H₂, C chỉ khử được oxide của kim loại đứng SAU Al!"},
                    {"name": "3. Thủy luyện (Kim loại yếu: Cu, Ag, Au)", "formula": "Fe + CuSO₄ → FeSO₄ + Cu↓", "note": ""},
                ],
            },
        ],
        "Cho 11,2 gam bột Iron (Fe, M = 56) vào 200 mL dung dịch H₂SO₄ 1,5 M (loãng). Tính thể tích khí H₂ thoát ra ở đkc (25°C, 1 bar) và khối lượng muối thu được sau phản ứng.",
        "PTHH: Fe + H₂SO₄ → FeSO₄ + H₂↑. Ta có n_Fe = 11,2 / 56 = 0,2 (mol) và n_H₂SO₄ = 0,2 · 1,5 = 0,3 (mol). Vì 0,2 < 0,3 nên Fe phản ứng hết, H₂SO₄ dư 0,1 mol. Suy ra n_H₂ = n_FeSO₄ = n_Fe = 0,2 (mol). Thể tích khí H₂ (đkc): V = 0,2 × 24,79 = 4,958 (lít). Khối lượng muối FeSO₄ (M = 152 g/mol): m = 0,2 × 152 = 30,4 (gam).",
        "Oxide nào dưới đây KHÔNG bị khử bởi khí Carbon monoxide (CO) ở nhiệt độ cao (mà bắt buộc phải điều chế kim loại bằng phương pháp điện phân nóng chảy)?",
        [
            "CuO (Copper(II) oxide)",
            "Fe₂O₃ (Iron(III) oxide)",
            "Al₂O₃ (Aluminium oxide) và MgO (Magnesium oxide)",
            "ZnO (Zinc oxide)",
        ],
        2,
        "Chế tạo dây cáp điện (Cu, Al), sản xuất gang thép từ quặng Hematite (Fe₂O₃) trong lò cao và chế tạo hợp kim hàng không vũ trụ.",
        "Khử hoàn toàn 32 gam bột Iron(III) oxide (Fe₂O₃, M = 160 g/mol) ở nhiệt độ cao bằng khí CO dư theo phản ứng: Fe₂O₃ + 3CO ──(t°)──► 2Fe + 3CO₂. Toàn bộ lượng khí CO₂ sinh ra được dẫn vào bình đựng dung dịch nước vôi trong Ca(OH)₂ dư. Tính khối lượng kim loại Fe và khối lượng kết tủa CaCO₃ thu được.",
        "Số mol Fe₂O₃ là: n_Fe₂O₃ = 32 / 160 = 0,2 (mol). Theo PTHH: n_Fe = 2 · n_Fe₂O₃ = 0,4 (mol) ⇒ khối lượng sắt thu được là m_Fe = 0,4 × 56 = 22,4 (gam). Số mol CO₂ sinh ra là: n_CO₂ = 3 · n_Fe₂O₃ = 0,6 (mol). Khi dẫn vào Ca(OH)₂ dư: CO₂ + Ca(OH)₂ → CaCO₃↓ + H₂O ⇒ n_CaCO₃ = n_CO₂ = 0,6 (mol) ⇒ m_CaCO₃ = 0,6 × 100 = 60 (gam).",
    ),
    C(
        9,
        "day-hoat-dong-kim-loai",
        "Dãy hoạt động hóa học của Kim loại & Bài toán Thanh kim loại nhúng vào dung dịch muối",
        "📋",
        "Thuộc lòng dãy hoạt động hóa học của kim loại, 4 ý nghĩa dự đoán phản ứng và giải bài toán tăng giảm khối lượng thanh kim loại.",
        "Trật tự sức mạnh của các kim loại",
        "Tại sao đinh sắt nhúng vào dung dịch Copper(II) sulfate màu xanh lam lại làm dung dịch nhạt màu dần và có lớp đồng màu đỏ bám ngoài đinh sắt, nhưng dây đồng nhúng vào dung dịch muối sắt lại không có hiện tượng gì?",
        "Dãy hoạt động hóa học của kim loại là dãy các kim loại được sắp xếp theo chiều giảm dần mức độ hoạt động hóa học của chúng: K – Na – Ba – Ca – Mg – Al – Zn – Fe – Ni – Sn – Pb – (H) – Cu – Hg – Ag – Pt – Au.",
        "• Bốn ý nghĩa quan trọng của dãy hoạt động hóa học:\n"
        "  1. Mức độ hoạt động hóa học của các kim loại giảm dần từ trái sang phải.\n"
        "  2. Các kim loại đứng đầu dãy (K, Na, Ba, Ca) tác dụng mãnh liệt với NƯỚC ở ngay nhiệt độ thường tạo thành dung dịch kiềm (Base tan) và giải phóng khí H₂: 2Na + 2H₂O → 2NaOH + H₂↑.\n"
        "  3. Các kim loại đứng TRƯỚC H (từ K đến Pb) tác dụng được với dung dịch acid (HCl, H₂SO₄ loãng) giải phóng khí H₂; các kim loại đứng SAU H (Cu, Hg, Ag, Pt, Au) không phản ứng.\n"
        "  4. Kim loại đứng trước (TRỪ K, Na, Ba, Ca vì chúng phản ứng với nước trước!) đẩy được kim loại đứng sau ra khỏi dung dịch muối của nó.",
        [
            {
                "category": "I. Dãy hoạt động hóa học của Kim loại & Mẹo ghi nhớ",
                "items": [
                    {"name": "Dãy hoạt động giảm dần từ trái sang phải", "formula": "K – Na – Ba – Ca – Mg – Al – Zn – Fe – Ni – Sn – Pb – (H) – Cu – Hg – Ag – Pt – Au", "note": "Mẹo nhớ: 'Khi Nào Ba Cần May Áo Giáp Sắt Nhớ Sang Phố Hỏi Cửa Hàng Á Phi Âu'"},
                    {"name": "Bẫy kinh điển khi cho K, Na, Ba, Ca vào dung dịch muối (ví dụ CuSO₄)", "formula": "B1: 2Na + 2H₂O → 2NaOH + H₂↑  ;  B2: 2NaOH + CuSO₄ → Cu(OH)₂↓ (xanh) + Na₂SO₄", "note": "Na KHÔNG đẩy được kim loại Cu, mà phản ứng với nước tạo kiềm rồi tạo kết tủa hydroxide!"},
                ],
            },
            {
                "category": "II. Phương pháp Tăng – Giảm khối lượng khi nhúng thanh Kim loại M vào dung dịch muối N",
                "items": [
                    {"name": "Độ tăng khối lượng thanh kim loại (khi m_bám_vào > m_tan_ra)", "formula": "Δm_thanh_tăng = m_kim_loại_bám_vào − m_kim_loại_tan_ra = m_dung_dịch_giảm", "note": "Ví dụ: Fe (56) + CuSO₄ → FeSO₄ + Cu (64): cứ 1 mol Fe phản ứng thì thanh sắt tăng 64 − 56 = 8 g"},
                    {"name": "Độ giảm khối lượng thanh kim loại (khi m_bám_vào < m_tan_ra)", "formula": "Δm_thanh_giảm = m_kim_loại_tan_ra − m_kim_loại_bám_vào = m_dung_dịch_tăng", "note": "Ví dụ: Zn (65) + CuSO₄ → ZnSO₄ + Cu (64): cứ 1 mol Zn phản ứng thì thanh kẽm giảm 65 − 64 = 1 g"},
                ],
            },
        ],
        "Nhúng một đinh sắt (Fe, M = 56) đã đánh sạch gỉ nặng 10 gam vào dung dịch Copper(II) sulfate (CuSO₄). Sau một thời gian lấy đinh sắt ra, rửa nhẹ, làm khô và cân lại thấy đinh sắt nặng 10,8 gam (giả sử toàn bộ Cu sinh ra bám hết vào đinh sắt, biết Cu = 64). Tính khối lượng Fe đã phản ứng và khối lượng Cu sinh ra.",
        "PTHH: Fe + CuSO₄ → FeSO₄ + Cu↓. Gọi số mol Fe đã phản ứng là x (mol) ⇒ số mol Cu bám vào cũng là x (mol). Độ tăng khối lượng của đinh sắt là: Δm = m_Cu − m_Fe = 64x − 56x = 8x = 10,8 − 10 = 0,8 (gam) ⇒ x = 0,1 (mol). Vậy khối lượng Fe đã tan ra là: 0,1 · 56 = 5,6 (gam) và khối lượng Cu bám vào là: 0,1 · 64 = 6,4 (gam).",
        "Cho một mẩu nhỏ kim loại Sodium (Na) vào cốc đựng dung dịch Copper(II) sulfate (CuSO₄). Hiện tượng quan sát được là:",
        [
            "Mẩu Na tan dần và có kim loại màu đỏ (Cu) bám vào mẩu Na",
            "Không có hiện tượng gì xảy ra",
            "Mẩu Na chạy trên mặt nước, sủi bọt khí không màu (H₂) và xuất hiện kết tủa màu xanh lam (Cu(OH)₂)",
            "Chỉ có sủi bọt khí không màu, dung dịch vẫn trong suốt",
        ],
        2,
        "Dự đoán chiều hướng phản ứng thế kim loại, thu hồi kim loại quý (Ag, Au, Cu) từ nước thải công nghiệp và tránh dùng thùng tôn kẽm/sắt đựng dung dịch muối đồng hay acid.",
        "Có một dung dịch muối Iron(II) sulfate (FeSO₄) bị lẫn tạp chất là muối Copper(II) sulfate (CuSO₄). Hãy chọn một kim loại duy nhất để làm sạch dung dịch FeSO₄ và viết PTHH giải thích.",
        "Ta cho một lượng dư bột kim loại Iron (Fe) vào dung dịch hỗn hợp và khuấy đều, sau đó lọc bỏ phần chất rắn (gồm Cu tạo thành và Fe dư). Vì Fe hoạt động mạnh hơn Cu nên đẩy hoàn toàn Cu ra khỏi dung dịch và chỉ tạo thêm chính muối FeSO₄ cần làm sạch: Fe + CuSO₄ → FeSO₄ + Cu↓.",
    ),
    C(
        9,
        "phi-kim",
        "Phi kim (Carbon, Silicon, Chlorine) & Sự khác biệt giữa Kim loại và Phi kim",
        "🌫️",
        "Nắm vững tính chất của các phi kim quan trọng (Carbon, Silicon, Chlorine), ứng dụng thực tiễn và bảng đối chiếu tính chất Kim loại – Phi kim.",
        "Từ lõi bút chì, chip bán dẫn Silicon đến khí Chlorine khử trùng nước",
        "Dù số lượng nguyên tố phi kim ít hơn nhiều so với kim loại, nhưng phi kim (C, H, O, N, P, S, Si, Cl...) lại là thành phần cốt lõi của cơ thể sống, khí quyển, vỏ Trái Đất và công nghệ bán dẫn hiện đại.",
        "Phi kim ở điều kiện thường có thể tồn tại ở cả 3 thể: thể khí (H₂, O₂, N₂, F₂, Cl₂), thể lỏng (duy nhất Bromine - Br₂ là chất lỏng màu nâu đỏ) và thể rắn (C, S, P, Si, I₂). Đa số phi kim không dẫn điện (trừ than chì - graphite), không dẫn nhiệt, không có ánh kim và có nhiệt độ nóng chảy thấp.",
        "• Tính chất hóa học chung của phi kim (dễ nhận thêm hoặc góp chung electron):\n"
        "  1. Tác dụng với kim loại tạo thành muối hoặc oxide (2Na + Cl₂ ──(t°)──► 2NaCl; Fe + S ──(t°)──► FeS).\n"
        "  2. Tác dụng với khí Hydrogen (H₂) tạo hợp chất khí (H₂ + Cl₂ ──(ánh sáng)──► 2HCl; N₂ + 3H₂ ⇄ 2NH₃).\n"
        "  3. Tác dụng với khí Oxygen (O₂) tạo thành Acidic oxide (C + O₂ ──(t°)──► CO₂; S + O₂ ──(t°)──► SO₂; 4P + 5O₂ ──(t°)──► 2P₂O₅).\n"
        "• Ba phi kim tiêu biểu:\n"
        "  + Carbon (C): có các dạng thù hình là Kim cương (cứng nhất, trang sức/mũi khoan), Than chì (graphite - dẫn điện, làm điện cực/ruột bút chì) và Than hoạt tính (có tính hấp phụ mạnh chất màu và khí độc, dùng trong mặt nạ phòng độc, máy lọc nước).\n"
        "  + Chlorine (Cl₂): khí màu vàng lục, mùi hắc, độc; tác dụng với nước tạo nước Chlorine có tính tẩy màu và sát trùng mạnh (Cl₂ + H₂O ⇄ HCl + HClO); tác dụng với dung dịch NaOH ở nhiệt độ thường tạo nước Javel.\n"
        "  + Silicon (Si) và hợp chất SiO₂: nguyên liệu sản xuất thủy tinh, gốm sứ, xi măng, sợi quang học và vi mạch bán dẫn, pin mặt trời.",
        [
            {
                "category": "I. Các Phương trình Hóa học trọng tâm của Carbon & Chlorine",
                "items": [
                    {"name": "Tính khử của Carbon ở nhiệt độ cao", "formula": "C + O₂ ──(t°)──► CO₂  ;  C + CO₂ ──(t°)──► 2CO  ;  C + 2CuO ──(t°)──► 2Cu + CO₂↑", "note": ""},
                    {"name": "Khí Chlorine (Cl₂) với Nước & với Dung dịch NaOH (Nước Javel)", "formula": "Cl₂ + H₂O ⇄ HCl + HClO (Hypochlorous acid có tính oxi hóa tẩy màu mạnh)  ;  Cl₂ + 2NaOH → NaCl + NaClO + H₂O", "note": "Hỗn hợp dung dịch NaCl + NaClO là nước tẩy Javel"},
                    {"name": "Điều chế khí Cl₂ trong công nghiệp (Điện phân dd NaCl có màng ngăn)", "formula": "2NaCl + 2H₂O ──(đpdd, có màng ngăn)──► 2NaOH + H₂↑ + Cl₂↑", "note": "Nếu không có màng ngăn thì Cl₂ tác dụng với NaOH tạo nước Javel"},
                ],
            },
            {
                "category": "II. So sánh toàn diện Kim loại và Phi kim",
                "items": [
                    {"name": "Xu hướng hóa học & Bản chất Oxide", "formula": "Kim loại: Nhường e tạo ion dương ⇒ Tạo Basic oxide  ;  Phi kim: Nhận/góp e ⇒ Tạo Acidic oxide", "note": ""},
                ],
            },
        ],
        "Khi dẫn khí Chlorine (Cl₂) vào cốc nước rồi nhúng một mẩu giấy quỳ tím vào dung dịch thu được, hiện tượng quan sát được trên mẩu giấy quỳ tím là gì? Giải thích bằng PTHH.",
        "Giấy quỳ tím lúc đầu chuyển sang màu ĐỎ, nhưng ngay sau đó bị MẤT MÀU (trở nên trắng). Giải thích: Cl₂ tác dụng với nước theo phản ứng thuận nghịch Cl₂ + H₂O ⇄ HCl + HClO. Ban đầu acid HCl làm quỳ tím hóa đỏ, sau đó HClO (hypochlorous acid) có tính oxi hóa rất mạnh đã tẩy trắng màu của giấy quỳ.",
        "Ở điều kiện thường (25°C, 1 bar), phi kim duy nhất tồn tại ở THỂ LỎNG là:",
        [
            "Chlorine (Cl₂ - thể khí màu vàng lục)",
            "Bromine (Br₂ - chất lỏng màu nâu đỏ)",
            "Iodine (I₂ - tinh thể rắn màu đen tím, dễ thăng hoa)",
            "Mercury (Hg - thủy ngân, đây là kim loại lỏng chứ không phải phi kim)",
        ],
        1,
        "Ứng dụng than hoạt tính trong lõi lọc nước RO và khẩu trang hoạt tính, dùng Chlorine khử trùng nước máy sinh hoạt và dùng Silicon siêu tinh khiết chế tạo chip máy tính, tấm pin năng lượng mặt trời.",
        "Tại sao trong công nghiệp điện phân dung dịch muối ăn bão hòa (NaCl + H₂O) để sản xuất xút (NaOH) và khí Chlorine (Cl₂), người ta bắt buộc phải đặt một MÀNG NGĂN xốp giữa hai điện cực? Nếu bỏ màng ngăn đi thì sản phẩm thu được là gì?",
        "Khi điện phân có màng ngăn: 2NaCl + 2H₂O → 2NaOH + H₂↑ (ở cathode) + Cl₂↑ (ở anode). Màng ngăn giữ không cho khí Cl₂ mới sinh ra tiếp xúc với dung dịch NaOH. Nếu bỏ màng ngăn đi, khí Cl₂ sẽ tác dụng ngay với dung dịch NaOH tạo thành dung dịch NƯỚC JAVEL: Cl₂ + 2NaOH → NaCl + NaClO + H₂O.",
    ),
    C(
        9,
        "acid-bazo-muoi",
        "Mối quan hệ chuyển hóa giữa các hợp chất Vô cơ (Oxide – Acid – Base – Muối)",
        "🧴",
        "Hệ thống hóa sơ đồ chuyển hóa qua lại giữa Kim loại, Phi kim, Oxide, Acid, Base, Muối và nhận biết các ion trong dung dịch.",
        "Bản đồ giao thông của các hợp chất vô cơ",
        "Bốn loại hợp chất vô cơ chính (Oxide, Acid, Base, Muối) không tồn tại tách biệt mà có thể chuyển hóa qua lại lẫn nhau thông qua các phản ứng hóa học xác định.",
        "Mối quan hệ giữa các loại hợp chất vô cơ tổng kết toàn bộ tính chất hóa học của Basic oxide, Acidic oxide, Acid, Base và Muối, cho phép thiết lập chuỗi phương trình điều chế chất và nhận biết hóa chất.",
        "• Chuỗi chuyển hóa từ Kim loại: Kim loại → Basic oxide → Base → Muối (hoặc Nhiệt phân Base không tan → Basic oxide + H₂O: 2Fe(OH)₃ ──(t°)──► Fe₂O₃ + 3H₂O; Cu(OH)₂ ──(t°)──► CuO + H₂O).\n"
        "• Chuỗi chuyển hóa từ Phi kim: Phi kim → Acidic oxide → Acid → Muối.\n"
        "• Bảng nhận biết các dung dịch vô cơ thông dụng:\n"
        "  + Dùng quỳ tím để phân biệt: Acid (đỏ), Base kiềm (xanh), Muối trung tính (tím).\n"
        "  + Nhận biết gốc sulfate (=SO₄) và H₂SO₄: dùng dung dịch muối Barium (BaCl₂, Ba(NO₃)₂) tạo kết tủa trắng BaSO₄↓ không tan trong acid.\n"
        "  + Nhận biết gốc chloride (–Cl) và HCl: dùng dung dịch Silver nitrate (AgNO₃) tạo kết tủa trắng AgCl↓.\n"
        "  + Nhận biết gốc carbonate (=CO₃): dùng dung dịch Acid (HCl) thấy sủi bọt khí không màu CO₂↑.",
        [
            {
                "category": "I. Sơ đồ Chuyển hóa tổng quát các Hợp chất Vô cơ",
                "items": [
                    {"name": "Nhiệt phân Base không tan (Cu(OH)₂, Fe(OH)₃, Mg(OH)₂, Al(OH)₃)", "formula": "Base không tan ──(t°)──► Basic oxide + H₂O  (Ví dụ: 2Al(OH)₃ ──(t°)──► Al₂O₃ + 3H₂O)", "note": "NaOH và KOH bền nhiệt, KHÔNG bị nhiệt phân hủy thành oxide!"},
                    {"name": "CO₂ / SO₂ tác dụng với dung dịch NaOH (Xét tỉ lệ T = n_NaOH / n_CO₂)", "formula": "T ≤ 1: chỉ tạo muối acid NaHCO₃ ; T ≥ 2: chỉ tạo muối trung hòa Na₂CO₃ ; 1 < T < 2: tạo cả 2 muối", "note": "CO₂ + NaOH → NaHCO₃ ; CO₂ + 2NaOH → Na₂CO₃ + H₂O"},
                ],
            },
            {
                "category": "II. Thuốc thử Nhận biết các Ion / Gốc Acid đặc trưng",
                "items": [
                    {"name": "Nhận biết H₂SO₄ và muối Sulfate (=SO₄)", "formula": "Thuốc thử: dd BaCl₂ hoặc Ba(OH)₂  ⇒  Hiện tượng: Kết tủa trắng BaSO₄↓ (không tan trong acid mạnh)", "note": ""},
                    {"name": "Nhận biết HCl và muối Chloride (–Cl)", "formula": "Thuốc thử: dd AgNO₃  ⇒  Hiện tượng: Kết tủa trắng AgCl↓", "note": ""},
                    {"name": "Nhận biết muối Carbonate (=CO₃) và Sulfite (=SO₃)", "formula": "Thuốc thử: dd HCl hoặc H₂SO₄ loãng  ⇒  Hiện tượng: Sủi bọt khí CO₂↑ (hoặc SO₂↑ mùi hắc)", "note": ""},
                ],
            },
        ],
        "Trình bày phương pháp hóa học để phân biệt 4 dung dịch không màu đựng trong 4 lọ mất nhãn: HCl, H₂SO₄, NaOH và NaCl.",
        "Bước 1: Trích mẫu thử và nhúng giấy quỳ tím vào 4 mẫu: Mẫu làm quỳ tím hóa XANH là NaOH; mẫu không làm đổi màu quỳ tím là NaCl; hai mẫu làm quỳ tím hóa ĐỎ là hai acid HCl và H₂SO₄. Bước 2: Nhỏ dung dịch BaCl₂ vào hai mẫu acid: mẫu nào xuất hiện kết tủa trắng (BaSO₄↓) là H₂SO₄; mẫu còn lại không có hiện tượng là HCl. PTHH: H₂SO₄ + BaCl₂ → BaSO₄↓ + 2HCl.",
        "Khi nung nóng chất rắn Copper(II) hydroxide (Cu(OH)₂ - màu xanh lam) đến khối lượng không đổi thì thu được chất rắn có màu gì và công thức là gì?",
        [
            "Chất rắn màu đỏ gạch là kim loại Cu",
            "Chất rắn màu đen là Copper(II) oxide (CuO)",
            "Chất rắn màu trắng là CuSO₄ khan",
            "Không xảy ra phản ứng vì Cu(OH)₂ bền với nhiệt",
        ],
        1,
        "Thiết kế quy trình xử lý khí thải SO₂, CO₂ của nhà máy nhiệt điện bằng dung dịch kiềm hoặc sữa vôi và kiểm nghiệm chất lượng nước.",
        "Hấp thụ hoàn toàn 0,15 mol khí Carbon dioxide (CO₂) vào dung dịch chứa 0,2 mol Sodium hydroxide (NaOH). Hãy xác định các muối tạo thành và tính khối lượng của mỗi muối sau phản ứng (biết Na = 23, H = 1, C = 12, O = 16).",
        "Xét tỉ lệ số mol: T = n_NaOH / n_CO₂ = 0,2 / 0,15 = 4/3. Vì 1 < T < 2 nên phản ứng tạo ra CẢ HAI MUỐI là NaHCO₃ (x mol) và Na₂CO₃ (y mol). Viết 2 PTHH: CO₂ + NaOH → NaHCO₃ (x mol) và CO₂ + 2NaOH → Na₂CO₃ + H₂O (y mol). Ta có hệ: { x + y = 0,15 (bảo toàn C) ; x + 2y = 0,20 (bảo toàn Na) } ⇒ x = 0,10 (mol) và y = 0,05 (mol). Khối lượng mỗi muối là: m_NaHCO₃ = 0,10 × 84 = 8,4 (g) và m_Na₂CO₃ = 0,05 × 106 = 5,3 (g).",
    ),
    C(
        9,
        "hydrocarbon",
        "Hợp chất Hữu cơ & Hydrocarbon: Alkane (Methane) – Alkene (Ethylene) – Nguồn nhiên liệu",
        "⛽",
        "Phân biệt hợp chất hữu cơ (Hydrocarbon và Dẫn xuất), công thức cấu tạo của Methane (CH₄) - Ethylene (C₂H₄) và các phản ứng thế, cộng, trùng hợp, cháy.",
        "Từ khí thiên nhiên, dầu mỏ đến công nghiệp hóa dầu",
        "Hợp chất hữu cơ là hợp chất của Carbon (trừ CO, CO₂, H₂CO₃, các muối carbonate, cyanide, carbide...). Trong hợp chất hữu cơ, Carbon luôn có hóa trị IV và có khả năng liên kết với nhau tạo thành mạch thẳng, mạch nhánh hoặc mạch vòng.",
        "Hydrocarbon là những hợp chất hữu cơ mà phân tử CHỈ gồm hai nguyên tố Carbon (C) và Hydrogen (H). Hai đại diện quan trọng nhất ở lớp 9 là Alkane (như Methane CH₄, Ethane C₂H₆, Propane C₃H₈, Butane C₄H₁₀) và Alkene (như Ethylene CH₂=CH₂).",
        "• Alkane (mạch hở chỉ chứa liên kết đơn C–C và C–H, công thức chung CₙH₂ₙ₊₂ với n ≥ 1): đại diện là Methane (CH₄ - thành phần chính của khí thiên nhiên và khí biogas). Phản ứng đặc trưng là phản ứng cháy tỏa nhiều nhiệt và phản ứng thế với Chlorine (ngoài ánh sáng: CH₄ + Cl₂ ──(as)──► CH₃Cl + HCl).\n"
        "• Alkene (mạch hở có 1 liên kết đôi C=C trong đó có 1 liên kết kém bền dễ đứt ra, công thức chung CₙH₂ₙ với n ≥ 2): đại diện là Ethylene (C₂H₄ hay CH₂=CH₂ - hormone thực vật kích thích quả mau chín). Phản ứng đặc trưng là PHẢN ỨNG CỘNG làm mất màu nâu đỏ của dung dịch nước Bromine (C₂H₄ + Br₂ → C₂H₄Br₂) và phản ứng trùng hợp tạo nhựa PE.\n"
        "• Dầu mỏ, khí thiên nhiên và khí mỏ dầu: chưng cất phân đoạn dầu mỏ thu được khí đốt LPG (propane + butane), xăng, dầu hỏa, dầu diesel, dầu nhờn và nhựa đường.",
        [
            {
                "category": "I. Cấu tạo, Công thức chung & Phản ứng đặc trưng của Alkane vs Alkene",
                "items": [
                    {"name": "Alkane (CₙH₂ₙ₊₂, n ≥ 1): Methane CH₄", "formula": "Chỉ có liên kết đơn C–C, C–H  ;  Phản ứng thế: CH₄ + Cl₂ ──(ánh sáng)──► CH₃Cl + HCl", "note": "CH₄ không làm mất màu dung dịch nước Bromine"},
                    {"name": "Alkene (CₙH₂ₙ, n ≥ 2): Ethylene CH₂=CH₂", "formula": "Có 1 liên kết đôi C=C  ;  Phản ứng cộng: CH₂=CH₂ + Br₂ (nâu đỏ) → BrCH₂–CH₂Br (không màu)", "note": "Dùng dd nước Bromine để nhận biết và làm sạch CH₄ lẫn C₂H₄!"},
                ],
            },
            {
                "category": "II. Phản ứng Đốt cháy hoàn toàn Hydrocarbon",
                "items": [
                    {"name": "Đốt cháy Alkane CₙH₂ₙ₊₂", "formula": "CₙH₂ₙ₊₂ + (3n + 1)/2 O₂ ──(t°)──► n CO₂ + (n + 1) H₂O", "note": "Luôn có: n_H₂O > n_CO₂  và  n_Alkane = n_H₂O − n_CO₂"},
                    {"name": "Đốt cháy Alkene CₙH₂ₙ", "formula": "CₙH₂ₙ + (3n / 2) O₂ ──(t°)──► n CO₂ + n H₂O", "note": "Luôn có: n_H₂O = n_CO₂"},
                ],
            },
        ],
        "Dẫn 4,958 lít (ở đkc 25°C, 1 bar) hỗn hợp khí gồm Methane (CH₄) và Ethylene (C₂H₄) đi từ từ qua bình đựng dung dịch nước Bromine (Br₂) dư thì thấy màu nâu đỏ của dung dịch nhạt dần và có 16 gam Br₂ đã tham gia phản ứng (biết Br = 80). Viết PTHH và tính thành phần phần trăm theo thể tích của mỗi khí trong hỗn hợp ban đầu.",
        "Tổng số mol hỗn hợp khí: n_hh = 4,958 / 24,79 = 0,2 (mol). Chỉ có Ethylene (C₂H₄) phản ứng cộng với dung dịch Br₂: CH₂=CH₂ + Br₂ → CH₂Br–CH₂Br. Số mol Br₂ phản ứng là: n_Br₂ = 16 / 160 = 0,1 (mol) ⇒ n_C₂H₄ = n_Br₂ = 0,1 (mol). Suy ra n_CH₄ = 0,2 − 0,1 = 0,1 (mol). Vì tỉ lệ thể tích chất khí ở cùng điều kiện bằng tỉ lệ số mol nên: %V_C₂H₄ = %V_CH₄ = (0,1 / 0,2) × 100% = 50%.",
        "Hóa chất nào dưới đây dùng để phân biệt hai chất khí không màu là Methane (CH₄) và Ethylene (C₂H₄)?",
        [
            "Giấy quỳ tím ẩm",
            "Dung dịch nước vôi trong Ca(OH)₂",
            "Dung dịch nước Bromine (Br₂ có màu nâu đỏ - bị C₂H₄ làm mất màu)",
            "Dung dịch Phenolphthalein",
        ],
        2,
        "Sử dụng khí đốt tự nhiên (CNG, LPG) an toàn, hiệu quả và ứng dụng khí Ethylene để ủ chín trái cây đồng loạt sau thu hoạch.",
        "Tại sao khi muốn một sọt quả xanh (như chuối xanh, xoài xanh) nhanh chín đều, người dân thường xếp xen vào giữa sọt vài quả đã chín hoàn toàn rồi đậy kín lại?",
        "Vì trong quá trình chín tự nhiên, các quả đã chín tiết ra một lượng nhỏ khí Ethylene (C₂H₄). Khí Ethylene đóng vai trò là hormone thực vật kích thích quá trình chín của các quả xanh xung quanh diễn ra nhanh hơn và đồng đều hơn.",
    ),
    C(
        9,
        "dan-xuat-hydrocarbon-lop-9",
        "Dẫn xuất Hydrocarbon & Hợp chất Sinh học: Ethylic Alcohol, Acetic Acid, Chất béo & Carbohydrate – Protein",
        "🍷",
        "Làm chủ cấu tạo, nhóm chức và phản ứng đặc trưng của Ethylic alcohol (–OH), Acetic acid (–COOH), phản ứng Ester hóa, Chất béo và Glucose - Saccharose - Tinh bột - Cellulose - Protein.",
        "Hóa học hữu cơ trong từng bữa ăn và y tế",
        "Cồn y tế 70° sát khuẩn là Ethylic alcohol; giấm ăn có vị chua là dung dịch Acetic acid 2%–5%; dầu ăn và mỡ động vật là Chất béo; còn cơm, bánh mì, đường, thịt, trứng là Carbohydrate và Protein.",
        "Dẫn xuất của hydrocarbon ngoài C và H còn có thêm các nguyên tố khác như Oxygen (O), Nitrogen (N)... tạo nên các nhóm chức quyết định tính chất hóa học đặc trưng của phân tử.",
        "• Ethylic alcohol (Ethanol: C₂H₅OH hay CH₃–CH₂–OH): chất lỏng không màu, sôi ở 78,3°C, nhẹ hơn nước (D ≈ 0,8 g/mL), tan vô hạn trong nước. Độ cồn là số mL ethylic alcohol nguyên chất có trong 100 mL dung dịch. Có nhóm –OH nên tác dụng với kim loại Na giải phóng khí H₂ (2C₂H₅OH + 2Na → 2C₂H₅ONa + H₂↑), phản ứng cháy và phản ứng với acetic acid.\n"
        "• Acetic acid (Ethanoic acid: CH₃COOH, M = 60): có nhóm carboxyl (–COOH) gây ra tính acid đầy đủ (làm quỳ tím hóa đỏ, tác dụng với kim loại trước H, basic oxide, base, muối carbonate CaCO₃) và phản ứng Ester hóa với ethylic alcohol (xúc tác H₂SO₄ đặc, đun nóng) tạo Ethyl acetate có mùi thơm.\n"
        "• Lipid – Chất béo ((RCOO)₃C₃H₅ - triester của glycerol và acid béo): thủy phân trong môi trường kiềm NaOH/KOH đun nóng (phản ứng xà phòng hóa) tạo Glycerol C₃H₅(OH)₃ và muối của acid béo (xà phòng).\n"
        "• Carbohydrate & Protein: Glucose (C₆H₁₂O₆ - phản ứng tráng bạc với AgNO₃/NH₃ và lên men rượu), Saccharose (C₁₂H₂₂O₁₁ - thủy phân tạo glucose + fructose), Tinh bột & Cellulose ((C₆H₁₀O₅)ₙ - hồ tinh bột gặp Iodine I₂ chuyển màu XANH TÍM đặc trưng!), và Protein (thủy phân tạo các amino acid; bị đông tụ khi đun nóng hoặc gặp acid/kiềm).",
        [
            {
                "category": "I. Độ cồn & Phản ứng của Ethylic alcohol (C₂H₅OH) và Acetic acid (CH₃COOH)",
                "items": [
                    {"name": "Công thức tính Độ cồn (° hoặc %V) & Khối lượng rượu", "formula": "Độ cồn = (V_C₂H₅OH / V_dung_dịch) × 100  ;  m_C₂H₅OH = V_C₂H₅OH × D_rượu (D ≈ 0,8 g/mL)", "note": "Cồn 70° nghĩa là trong 100 mL dung dịch cồn có 70 mL C₂H₅OH nguyên chất"},
                    {"name": "Phản ứng với Na & Phản ứng của nhóm –COOH", "formula": "2C₂H₅OH + 2Na → 2C₂H₅ONa + H₂↑ ; 2CH₃COOH + CaCO₃ → (CH₃COO)₂Ca + CO₂↑ + H₂O", "note": "Dùng CaCO₃ hoặc quỳ tím để phân biệt CH₃COOH và C₂H₅OH"},
                    {"name": "Phản ứng Ester hóa (Thuận nghịch, cần H₂SO₄ đặc, t°)", "formula": "CH₃COOH + C₂H₅OH ⇄ (H₂SO₄ đặc, t°) ⇄ CH₃COOC₂H₅ (Ethyl acetate - mùi thơm) + H₂O", "note": "H₂SO₄ đặc vừa làm xúc tác vừa hút nước để tăng hiệu suất tạo ester"},
                ],
            },
            {
                "category": "II. Chất béo, Glucose, Tinh bột & Protein",
                "items": [
                    {"name": "Phản ứng Xà phòng hóa Chất béo", "formula": "(RCOO)₃C₃H₅ + 3NaOH ──(t°)──► 3RCOONa (Xà phòng) + C₃H₅(OH)₃ (Glycerol)", "note": "Bảo toàn khối lượng: m_chất_béo + m_NaOH = m_xà_phòng + m_glycerol"},
                    {"name": "Phản ứng Tráng bạc & Lên men rượu của Glucose (C₆H₁₂O₆)", "formula": "C₆H₁₂O₆ + Ag₂O ──(NH₃, t°)──► C₆H₁₂O₇ + 2Ag↓ ; C₆H₁₂O₆ ──(enzyme)──► 2C₂H₅OH + 2CO₂↑", "note": "1 mol Glucose tráng gương tạo 2 mol Ag và lên men tạo 2 mol C₂H₅OH"},
                    {"name": "Thủy phân Tinh bột / Cellulose & Nhận biết Hồ tinh bột", "formula": "(C₆H₁₀O₅)ₙ + nH₂O ──(H⁺/enzyme, t°)──► nC₆H₁₂O₆ ; Hồ tinh bột + dd I₂ → Màu XANH TÍM", "note": ""},
                ],
            },
        ],
        "Đun nóng 30 gam Acetic acid (CH₃COOH, M = 60) với một lượng dư Ethylic alcohol (C₂H₅OH) có mặt H₂SO₄ đặc làm xúc tác. Biết hiệu suất của phản ứng ester hóa là H = 60%. Tính khối lượng ester Ethyl acetate (CH₃COOC₂H₅, M = 88) thu được.",
        "PTHH: CH₃COOH + C₂H₅OH ⇄ CH₃COOC₂H₅ + H₂O. Số mol CH₃COOH ban đầu là: n = 30 / 60 = 0,5 (mol). Theo lý thuyết (H = 100%), số mol ester tạo thành bằng số mol acid: n_ester(lt) = 0,5 (mol). Do hiệu suất H = 60%, số mol ester thực tế thu được là: n_ester(tt) = 0,5 × 60% = 0,3 (mol). Khối lượng Ethyl acetate thu được là: m = 0,3 × 88 = 26,4 (gam).",
        "Khi nhỏ vài giọt dung dịch Iodine (I₂ / cồn iốt) lên mặt cắt của củ khoai lang, củ sắn hoặc cơm trắng thì xuất hiện màu gì đặc trưng?",
        [
            "Màu đỏ gạch",
            "Màu xanh tím đặc trưng (do tinh bột hấp phụ I₂)",
            "Màu vàng nhạt",
            "Kết tủa màu bạc sáng bóng",
        ],
        1,
        "Pha chế cồn y tế 70° sát khuẩn hiệu quả nhất, dùng giấm ăn tẩy cặn vôi (CaCO₃) trong ấm đun nước, sản xuất xà phòng từ dầu thực vật và lên men tinh bột sản xuất xăng sinh học E5.",
        "Xăng sinh học E5 chứa 5% thể tích là Ethylic alcohol (C₂H₅OH) khan và 95% thể tích là xăng truyền thống. Nếu lên men 1,62 tấn tinh bột (coi phân tử khối mỗi mắt xích C₆H₁₀O₅ là 162 g/mol) với hiệu suất toàn bộ quá trình thủy phân và lên men đạt 80%, thì thu được bao nhiêu lít Ethylic alcohol nguyên chất (biết khối lượng riêng của C₂H₅OH là D = 0,8 g/mL) và pha được bao nhiêu lít xăng E5?",
        "Sơ đồ chuyển hóa theo mắt xích: C₆H₁₀O₅ (162) → C₆H₁₂O₆ → 2C₂H₅OH (2 × 46 = 92). Đổi 1,62 tấn = 1 620 kg ⇒ số kmol mắt xích tinh bột là 1620 / 162 = 10 (kmol). Với hiệu suất 80%, số kmol C₂H₅OH thu được là: n_rượu = 2 · 10 · 80% = 16 (kmol) ⇒ khối lượng C₂H₅OH là: m = 16 × 46 = 736 (kg). Thể tích C₂H₅OH nguyên chất là: V_rượu = m / D = 736 / 0,8 = 920 (lít). Vì xăng E5 chứa 5% thể tích C₂H₅OH nên thể tích xăng E5 pha được là: V_E5 = 920 / 5% = 18 400 (lít).",
    ),
    C(
        9,
        "polime-vat-lieu",
        "Polymer & Vật liệu Polymer (Chất dẻo – Tơ – Cao su – Vật liệu Composite)",
        "🧵",
        "Hiểu khái niệm Polymer, mắt xích, hệ số polymer hóa n, phản ứng trùng hợp và phân loại 4 nhóm vật liệu polymer hiện đại.",
        "Vật liệu của kỷ nguyên hiện đại và bài toán môi trường",
        "Từ túi nhựa PE, ống nước PVC, quần áo sợi bông/nylon đến lốp xe cao su và vỏ máy bay composite — tất cả đều được cấu tạo từ những phân tử khổng lồ gọi là Polymer.",
        "Polymer là những hợp chất có khối lượng phân tử rất lớn do nhiều đơn vị nhỏ (gọi là mắt xích) liên kết với nhau tạo nên. Các phân tử nhỏ ban đầu tham gia phản ứng tạo nên polymer được gọi là monomer.",
        "• Trong công thức polymer như Polyethylene (–CH₂–CH₂–)ₙ: monomer ban đầu là Ethylene (CH₂=CH₂), mắt xích cơ sở là –CH₂–CH₂– (M_mắt_xích = 28 g/mol) và n được gọi là hệ số polymer hóa (độ polymer hóa): M_polymer = n × M_mắt_xích.\n"
        "• Nguồn gốc polymer: Polymer thiên nhiên (tinh bột, cellulose, bông, tơ tằm, cao su thiên nhiên, protein) và Polymer tổng hợp (PE, PP, PVC, PS, tơ nylon, cao su buna).\n"
        "• Bốn nhóm vật liệu polymer quan trọng: 1) Chất dẻo (PE, PP, PVC, PS... có tính dẻo); 2) Tơ (tơ thiên nhiên như bông, len, tơ tằm; tơ tổng hợp như tơ nylon-6,6, tơ nitron); 3) Cao su (có tính đàn hồi); 4) Vật liệu Composite (tổ hợp từ vật liệu nền là polymer với vật liệu cốt như sợi carbon, sợi thủy tinh giúp siêu bền, siêu nhẹ).\n"
        "• Ô nhiễm trắng (rác thải nhựa khó phân hủy) và nguyên tắc 3R + sử dụng nhựa phân hủy sinh học.",
        [
            {
                "category": "I. Cấu trúc Polymer, Hệ số Polymer hóa (n) & Phản ứng Trùng hợp",
                "items": [
                    {"name": "Hệ số polymer hóa n (số mắt xích trong 1 phân tử polymer)", "formula": "n = M_polymer / M_mắt_xích", "note": "Ví dụ: PE có M_mắt_xích = 28 ; PVC (–CH₂–CHCl–)ₙ có M_mắt_xích = 62,5 ; Tinh bột/Cellulose có M_mắt_xích = 162"},
                    {"name": "Phản ứng trùng hợp Ethylene tạo nhựa PE (Polyethylene)", "formula": "n CH₂=CH₂ ──(t°, p, xt)──► (–CH₂–CH₂–)ₙ", "note": ""},
                    {"name": "Phản ứng trùng hợp Vinyl chloride tạo nhựa PVC (Poly(vinyl chloride))", "formula": "n CH₂=CHCl ──(t°, p, xt)──► (–CH₂–CHCl–)ₙ", "note": ""},
                ],
            },
            {
                "category": "II. Phân biệt Tơ thiên nhiên (Tơ tằm, Lông cừu) & Tơ tổng hợp (Nylon)",
                "items": [
                    {"name": "Đốt thử sợi vải", "formula": "Tơ tằm / Lông cừu (chứa Protein): khi cháy có mùi khét như tóc cháy  ;  Bông (Cellulose) / Nylon: không có mùi tóc cháy", "note": "Mẹo thực tế phân biệt lụa tơ tằm thật và lụa nhân tạo"},
                ],
            },
        ],
        "Một phân tử Polyethylene (PE: (–CH₂–CH₂–)ₙ) có khối lượng phân tử trung bình là 56 000 amu. Hãy tính hệ số polymer hóa n (số mắt xích –CH₂–CH₂–) của phân tử PE đó (biết C = 12, H = 1).",
        "Khối lượng của một mắt xích –CH₂–CH₂– là: M_mắt_xích = 2·12 + 4·1 = 28 (amu). Hệ số polymer hóa (số mắt xích) của phân tử PE là: n = M_PE / M_mắt_xích = 56 000 / 28 = 2 000 (mắt xích).",
        "Polymer nào dưới đây thuộc loại POLYMER THIÊN NHIÊN?",
        [
            "Polyethylene (PE) và Poly(vinyl chloride) (PVC)",
            "Tinh bột, Cellulose, Tơ tằm và Cao su thiên nhiên",
            "Tơ nylon-6,6 và Nhựa Polystyrene (PS)",
            "Cao su buna",
        ],
        1,
        "Nhận biết ký hiệu tái chế nhựa (từ số 1 PET đến số 7), lựa chọn màng bọc thực phẩm PE an toàn và phân biệt lụa tơ tằm thật.",
        "Làm thế nào để phân biệt nhanh một mảnh vải dệt bằng tơ tằm tự nhiên thật với một mảnh vải dệt bằng sợi bông (cotton) hoặc sợi polyester tổng hợp bằng một thí nghiệm đơn giản?",
        "Rút vài sợi chỉ nhỏ từ mỗi mảnh vải rồi đốt trên ngọn lửa: Sợi tơ tằm tự nhiên có bản chất là PROTEIN nên khi cháy sẽ có mùi khét đặc trưng giống hệt mùi tóc hoặc lông gà cháy và tạo tàn tro bóp dễ vỡ vụn. Sợi bông (bản chất là cellulose) khi cháy có mùi như đốt giấy; còn sợi polyester tổng hợp sẽ chảy nhựa vón cục cứng.",
    ),
]

LESSONS += [
    # =========================================================
    # HÓA HỌC LỚP 10 (7 BÀI)
    # =========================================================
    C(
        10,
        "cau-tao-nguyen-tu",
        "Thành phần Nguyên tử, Số khối (A = Z + N), Đồng vị & Nguyên tử khối trung bình",
        "⚛️",
        "Nắm vững ký hiệu nguyên tử ᴬ_Z X, khái niệm đồng vị và công thức tính nguyên tử khối trung bình Ā từ phần trăm số nguyên tử các đồng vị.",
        "Tại sao nguyên tử khối của Chlorine lại là số lẻ 35,5?",
        "Mặc dù số proton và số neutron trong hạt nhân đều là các số nguyên, nhưng nguyên tử khối của Chlorine trong Bảng tuần hoàn lại là 35,5 vì trong tự nhiên Chlorine là hỗn hợp của hai đồng vị bền ³⁵Cl (75%) và ³⁷Cl (25%).",
        "Ký hiệu nguyên tử ᴬ_Z X cho biết số hiệu nguyên tử Z (số hạt proton) và số khối A = Z + N (tổng số hạt proton và neutron). Đồng vị của cùng một nguyên tố hóa học là những nguyên tử có CÙNG số hạt proton (cùng Z) nhưng KHÁC nhau về số hạt neutron (N), do đó số khối A của chúng khác nhau.",
        "• Kích thước và khối lượng: Đường kính nguyên tử (~10⁻¹⁰ m = 1 Å) lớn gấp khoảng 10 000 lần đường kính hạt nhân (~10⁻¹⁴ m); m_p ≈ m_n ≈ 1 amu; m_e ≈ 0,00055 amu.\n"
        "• Trong ion đơn nguyên tử: Nguyên tử trung hòa nhường k electron tạo thành cation Mᵏ⁺ (có số e = Z − k); nguyên tử nhận thêm m electron tạo thành anion Xᵐ⁻ (có số e = Z + m).\n"
        "• Bất đẳng thức bền của hạt nhân các nguyên tố có Z ≤ 82 (trừ ¹₁H): 1 ≤ N / Z ≤ 1,52 ⇒ S / 3,52 ≤ Z ≤ S / 3 (với S = 2Z + N là tổng số hạt).\n"
        "• Công thức tính Nguyên tử khối trung bình Ā từ phần trăm số nguyên tử của các đồng vị.",
        [
            {
                "category": "I. Ký hiệu Nguyên tử ᴬ_Z X, Ion & Hệ thức tổng hạt S",
                "items": [
                    {"name": "Số khối A & Số neutron N", "formula": "A = Z + N  ⇒  N = A − Z", "note": "Trong nguyên tử trung hòa: p = e = Z"},
                    {"name": "Số hạt trong Ion Mᵏ⁺ và Xᵐ⁻", "formula": "Trong Mᵏ⁺: p = Z, e = Z − k ; Trong Xᵐ⁻: p = Z, e = Z + m", "note": "Khi tạo thành ion chỉ có số ELECTRON thay đổi, số p và n giữ nguyên!"},
                    {"name": "Hệ thức xác định nhanh Z từ tổng số hạt S = 2Z + N (với 2 ≤ Z ≤ 82)", "formula": "1 ≤ N / Z ≤ 1,52  ⇔  S / 3,52 ≤ Z ≤ S / 3", "note": "Với các nguyên tố nhẹ (Z ≤ 20) thường có 1 ≤ N/Z ≤ 1,22"},
                ],
            },
            {
                "category": "II. Đồng vị & Công thức Nguyên tử khối trung bình (Ā)",
                "items": [
                    {"name": "Nguyên tử khối trung bình của hỗn hợp đồng vị", "formula": "Ā = (A₁ · x₁ + A₂ · x₂ + ... + Aₖ · xₖ) / (x₁ + x₂ + ... + xₖ)", "note": "Aᵢ: số khối đồng vị i ; xᵢ: % số nguyên tử (tổng xᵢ = 100%) hoặc tỉ lệ số nguyên tử"},
                ],
            },
        ],
        "Trong tự nhiên, nguyên tố Copper (Đồng - Cu) có hai đồng vị bền là ⁶³₂₉Cu và ⁶⁵₂₉Cu. Biết nguyên tử khối trung bình của Cu là 63,54. Hãy tính thành phần phần trăm số nguyên tử của mỗi đồng vị và phần trăm khối lượng của ⁶³Cu trong hợp chất CuSO₄ (cho S = 32, O = 16).",
        "Gọi % số nguyên tử của ⁶³Cu là x (%) ⇒ của ⁶⁵Cu là (100 − x) (%). Áp dụng công thức: Ā = [63x + 65(100 − x)] / 100 = 63,54 ⇔ 6500 − 2x = 6354 ⇒ x = 73%. Vậy ⁶³Cu chiếm 73% và ⁶⁵Cu chiếm 27%. Phân tử khối trung bình của CuSO₄ là: M = 63,54 + 32 + 4·16 = 159,54. Phần trăm khối lượng của đồng vị ⁶³Cu trong CuSO₄ là: %m_(⁶³Cu) = (63 × 0,73 / 159,54) × 100% ≈ 28,83%.",
        "Cation Iron(III) có ký hiệu ⁵⁶₂₆Fe³⁺ có số hạt proton (p), neutron (n) và electron (e) lần lượt là:",
        [
            "p = 26, n = 30, e = 26",
            "p = 26, n = 30, e = 23",
            "p = 26, n = 30, e = 29",
            "p = 23, n = 30, e = 26",
        ],
        1,
        "Ứng dụng đồng vị phóng xạ ⁶⁰Co, ¹³¹I trong điều trị ung thư, đồng vị ¹⁴C định tuổi cổ vật và phổ khối lượng (MS) xác định nguyên tử khối.",
        "Trong tự nhiên, Hydrogen có 3 đồng vị: ¹₁H, ²₁H (Deuterium) và ³₁H (Tritium); còn Oxygen có 3 đồng vị: ¹⁶₈O, ¹⁷₈O và ¹⁸₈O. Hỏi có thể tạo thành tối đa bao nhiêu loại phân tử nước (H₂O) khác nhau từ các đồng vị trên?",
        "Một phân tử H₂O gồm 2 nguyên tử H và 1 nguyên tử O. Số cách chọn cặp 2 nguyên tử H từ 3 đồng vị (có thể giống nhau hoặc khác nhau): gồm 3 cặp giống nhau (¹H–¹H, ²H–²H, ³H–³H) và 3 cặp khác nhau (¹H–²H, ¹H–³H, ²H–³H), tổng cộng là 6 cách chọn bộ H₂. Kết hợp với 3 cách chọn đồng vị Oxygen (¹⁶O, ¹⁷O, ¹⁸O), số loại phân tử H₂O tối đa tạo thành là: 6 × 3 = 18 (loại phân tử H₂O).",
    ),
    C(
        10,
        "cau-hinh-electron",
        "Orbital nguyên tử (AO), Lớp & Phân lớp electron (s, p, d, f) & Cấu hình electron nguyên tử",
        "🔵",
        "Hiểu hình dạng AO (s hình cầu, p hình số tám nổi), 3 nguyên lý/quy tắc phân bố electron (Pauli, Vững bền, Hund) và viết cấu hình electron chuẩn.",
        "Bản đồ phân bố các electron quanh hạt nhân",
        "Theo mô hình hiện đại của cơ học lượng tử, các electron chuyển động rất nhanh xung quanh hạt nhân không theo quỹ đạo tròn cố định mà tạo thành đám mây xác suất gọi là Orbital nguyên tử (AO).",
        "Orbital nguyên tử (AO) là khu vực không gian xung quanh hạt nhân mà tại đó xác suất tìm thấy electron là lớn nhất (khoảng 90%). Cấu hình electron nguyên tử biểu diễn sự phân bố electron trên các phân lớp thuộc các lớp khác nhau.",
        "• Hình dạng và số lượng AO trong mỗi phân lớp: Phân lớp s có 1 AO (hình cầu), chứa tối đa 2e; Phân lớp p có 3 AO (p_x, p_y, p_z hình số 8 nổi), chứa tối đa 6e; Phân lớp d có 5 AO, chứa tối đa 10e; Phân lớp f có 7 AO, chứa tối đa 14e.\n"
        "• Ba nguyên lý và quy tắc điền electron: 1) Nguyên lý vững bền (điền từ mức năng lượng thấp đến cao: 1s 2s 2p 3s 3p 4s 3d 4p...); 2) Nguyên lý ngăn cấm Pauli (mỗi ô orbital chứa tối đa 2 electron có chiều tự quay ngược nhau ↑↓); 3) Quy tắc Hund (trong cùng một phân lớp, các electron phân bố vào các AO sao cho số electron độc thân là tối đa).\n"
        "• Hai trường hợp đặc biệt bão hòa và bán bão hòa sớm của phân lớp 3d: Chromium Cr (Z = 24): [Ar] 3d⁵ 4s¹ (có 6e độc thân!) và Copper Cu (Z = 29): [Ar] 3d¹⁰ 4s¹.\n"
        "• Dựa vào số electron lớp ngoài cùng: 1, 2, 3e → Kim loại (trừ H, He, B); 5, 6, 7e → Phi kim; 8e (2e với He) → Khí hiếm.",
        [
            {
                "category": "I. Sức chứa của Phân lớp & Lớp electron thứ n",
                "items": [
                    {"name": "Số AO và Số e tối đa trong phân lớp s, p, d, f", "formula": "s (1 AO): tối đa 2e ; p (3 AO): tối đa 6e ; d (5 AO): tối đa 10e ; f (7 AO): tối đa 14e", "note": "Mỗi AO chứa tối đa 2e ghép đôi (↑↓)"},
                    {"name": "Số AO và Số e tối đa trong lớp thứ n (n ≤ 4)", "formula": "Số AO của lớp thứ n = n²  ;  Số e tối đa của lớp thứ n = 2n²", "note": "Lớp K (n=1): 2e ; Lớp L (n=2): 8e ; Lớp M (n=3): 18e ; Lớp N (n=4): 32e"},
                ],
            },
            {
                "category": "II. Thứ tự mức năng lượng & Hai cấu hình đặc biệt cần nhớ (Cr và Cu)",
                "items": [
                    {"name": "Thứ tự mức năng lượng (Chú ý 4s điền trước 3d!)", "formula": "1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s...", "note": "Khi viết cấu hình e phải sắp xếp lại theo thứ tự lớp: ...3s² 3p⁶ 3dⁿ 4s²"},
                    {"name": "Cấu hình bán bão hòa Cr (Z=24) & bão hòa Cu (Z=29)", "formula": "Cr (Z=24): 1s²2s²2p⁶3s²3p⁶ 3d⁵4s¹ ([Ar]3d⁵4s¹)  ;  Cu (Z=29): 1s²2s²2p⁶3s²3p⁶ 3d¹⁰4s¹ ([Ar]3d¹⁰4s¹)", "note": "Do phân lớp d⁵ (bán bão hòa) và d¹⁰ (bão hòa) rất bền"},
                ],
            },
        ],
        "Viết cấu hình electron đầy đủ của nguyên tử Iron (Fe, Z = 26), cation Fe²⁺ và cation Fe³⁺. Cho biết trong nguyên tử Fe ở trạng thái cơ bản có bao nhiêu electron độc thân?",
        "Với Fe (Z = 26): Điền theo mức năng lượng được 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶, sắp xếp theo lớp được cấu hình của Fe là: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s² (hay [Ar] 3d⁶ 4s²). Phân lớp 3d⁶ có 5 AO: điền 5e vào 5 AO trước rồi ghép đôi 1 AO, nên còn 4 electron độc thân. Khi nhường e tạo ion, nguyên tử nhường e ở lớp ngoài cùng (4s) trước: Fe²⁺ (24e): [Ar] 3d⁶ ; Fe³⁺ (23e): [Ar] 3d⁵ (bán bão hòa rất bền!).",
        "Ở trạng thái cơ bản, cấu hình electron đúng của nguyên tử Chromium (Cr, có Z = 24) và số electron độc thân của nó lần lượt là:",
        [
            "[Ar] 3d⁴ 4s² (có 4 electron độc thân)",
            "[Ar] 3d⁵ 4s¹ (có 6 electron độc thân)",
            "[Ar] 3d⁵ 4s¹ (có 1 electron độc thân)",
            "[Ar] 3d⁶ (có 4 electron độc thân)",
        ],
        1,
        "Giải thích tính từ của vật liệu sắt từ (do có nhiều electron độc thân), số oxi hóa của các nguyên tố chuyển tiếp d và cơ chế liên kết hóa học.",
        "Nguyên tử của nguyên tố X ở trạng thái cơ bản có tổng số electron trong các phân lớp p là 11. Hãy viết cấu hình electron của nguyên tử X, xác định số hiệu nguyên tử Z và cho biết X là kim loại, phi kim hay khí hiếm?",
        "Các phân lớp p lần lượt là 2p và 3p. Để tổng số e trên các phân lớp p bằng 11 thì phân lớp 2p phải bão hòa (2p⁶) và phân lớp 3p có 11 − 6 = 5 electron (3p⁵). Do đó cấu hình electron đầy đủ của X là: 1s² 2s² 2p⁶ 3s² 3p⁵. Tổng số electron là Z = 17 (Chlorine - Cl). Vì lớp ngoài cùng (lớp thứ 3: 3s² 3p⁵) có 7 electron nên X là một PHI KIM.",
    ),
    C(
        10,
        "bang-tuan-hoan",
        "Bảng tuần hoàn & Định luật Tuần hoàn (Xu hướng Bán kính nguyên tử, Độ âm điện, Tính Kim loại - Phi kim)",
        "🧭",
        "Nắm vững mối liên hệ giữa cấu hình electron và vị trí trong BTH, quy luật biến đổi tuần hoàn bán kính nguyên tử R, độ âm điện χ, tính kim loại - phi kim và tính acid - base của oxide/hydroxide.",
        "Quy luật biến thiên kỳ diệu của các nguyên tố",
        "Chỉ cần biết vị trí của một nguyên tố trong Bảng tuần hoàn, ta có thể dự đoán chính xác cấu hình electron, hóa trị cao nhất với oxygen, hóa trị với hydrogen và so sánh tính kim loại - phi kim với các nguyên tố lân cận.",
        "Định luật tuần hoàn phát biểu: 'Tính chất của các nguyên tố và đơn chất, cũng như thành phần và tính chất của các hợp chất tạo nên từ các nguyên tố đó biến đổi tuần hoàn theo chiều tăng của điện tích hạt nhân nguyên tử'.",
        "• Quy luật biến đổi trong MỘT CHU KỲ (từ trái sang phải theo chiều Z tăng, số lớp e không đổi nhưng điện tích hạt nhân tăng hút lớp vỏ co lại): Bán kính nguyên tử (R) GIẢM dần; Độ âm điện (χ) TĂNG dần; Tính kim loại GIẢM dần; Tính phi kim TĂNG dần; Tính base của oxide và hydroxide giảm dần, tính acid của chúng tăng dần.\n"
        "• Quy luật biến đổi trong MỘT NHÓM A (từ trên xuống dưới theo chiều Z tăng, số lớp electron tăng lên): Bán kính nguyên tử (R) TĂNG dần; Độ âm điện (χ) GIẢM dần; Tính kim loại TĂNG dần; Tính phi kim GIẢM dần.\n"
        "• Công thức hợp chất của nguyên tố nhóm nA (n từ IV đến VII): Oxide cao nhất có công thức R₂Oₙ (với n lẻ) hoặc RO_(n/2) (với n chẵn), trong đó R có hóa trị cao nhất bằng số thứ tự nhóm n; Hợp chất khí với Hydrogen có công thức RH_(8−n).",
        [
            {
                "category": "I. Bảng tổng hợp Quy luật biến đổi tuần hoàn (Theo chiều Z tăng)",
                "items": [
                    {"name": "Trong 1 Chu kỳ (Trái → Phải)", "formula": "Bán kính R GIẢM ↓ ; Tính Kim loại GIẢM ↓ ; Độ âm điện χ TĂNG ↑ ; Tính Phi kim TĂNG ↑ ; Tính Acid của Oxide/Hydroxide TĂNG ↑", "note": ""},
                    {"name": "Trong 1 Nhóm A (Trên → Dưới)", "formula": "Bán kính R TĂNG ↑ ; Tính Kim loại TĂNG ↑ ; Độ âm điện χ GIẢM ↓ ; Tính Phi kim GIẢM ↓ ; Tính Base của Hydroxide TĂNG ↑", "note": "Phi kim mạnh nhất (χ lớn nhất = 3,98) là Fluorine (F) ; Kim loại mạnh nhất là Francium/Cesium (Cs)"},
                ],
            },
            {
                "category": "II. Hóa trị cao nhất với Oxygen & Hợp chất khí với Hydrogen (Nhóm nA, IV ≤ n ≤ VII)",
                "items": [
                    {"name": "Tổng hóa trị của Phi kim", "formula": "Hóa trị cao nhất với O (bằng n) + Hóa trị với H (bằng 8 − n) = 8", "note": ""},
                    {"name": "Công thức Oxide cao nhất & Hợp chất khí với H", "formula": "Nhóm IVA: RO₂ & RH₄ ; Nhóm VA: R₂O₅ & RH₃ ; Nhóm VIA: RO₃ & RH₂ ; Nhóm VIIA: R₂O₇ & RH", "note": "Hydroxide cao nhất tương ứng: H₂RO₃, H₃RO₄ (hoặc HRO₃), H₂RO₄, HRO₄"},
                ],
            },
        ],
        "Cho bốn nguyên tố: Sodium (₁₁Na), Magnesium (₁₂Mg), Aluminium (₁₃Al) và Potassium (₁₉K). Hãy sắp xếp các nguyên tố trên theo chiều tăng dần bán kính nguyên tử và chiều tăng dần tính base của các hydroxide tương ứng.",
        "Na, Mg, Al cùng thuộc chu kỳ 3 (Z = 11, 12, 13); K thuộc chu kỳ 4, nhóm IA (đứng ngay dưới Na). Trong chu kỳ 3 từ trái sang phải, bán kính và tính kim loại giảm dần: R_Na > R_Mg > R_Al. Trong nhóm IA từ trên xuống, K có bán kính và tính kim loại lớn hơn Na: R_K > R_Na. Vậy chiều tăng dần bán kính nguyên tử là: Al < Mg < Na < K; và chiều tăng dần tính base của các hydroxide là: Al(OH)₃ < Mg(OH)₂ < NaOH < KOH.",
        "Cho các ion và nguyên tử có cùng 10 electron (đẳng electron): O²⁻ (Z = 8), F⁻ (Z = 9), Ne (Z = 10), Na⁺ (Z = 11), Mg²⁺ (Z = 12). Thứ tự giảm dần bán kính của các hạt trên là:",
        [
            "Mg²⁺ > Na⁺ > Ne > F⁻ > O²⁻",
            "O²⁻ > F⁻ > Ne > Na⁺ > Mg²⁺ (Cùng số e, điện tích hạt nhân Z càng lớn thì hút vỏ càng mạnh làm bán kính càng nhỏ!)",
            "Na⁺ > Mg²⁺ > O²⁻ > F⁻ > Ne",
            "Bán kính của cả 5 hạt bằng nhau vì cùng có 10 electron",
        ],
        1,
        "Dự đoán tính chất vật liệu bán dẫn, thiết kế chất xúc tác và giải nhanh bài toán tìm nguyên tố từ công thức oxide cao nhất / hợp chất khí với hydrogen.",
        "Nguyên tố R thuộc nhóm VIA trong Bảng tuần hoàn. Trong hợp chất oxide cao nhất của R, nguyên tố Oxygen chiếm 60% về khối lượng. Hãy xác định tên nguyên tố R, công thức oxide cao nhất, công thức hợp chất khí với hydrogen và tính phần trăm khối lượng của R trong hợp chất khí với hydrogen.",
        "Vì R thuộc nhóm VIA (n = 6) nên công thức oxide cao nhất của R là RO₃ và công thức hợp chất khí với H là RH₂ (hay H₂R). Trong RO₃, Oxygen chiếm 60% khối lượng nên R chiếm 40%: M_R / (M_R + 3·16) = 40 / 60 ⇒ M_R / (M_R + 48) = 2 / 3 ⇒ 3·M_R = 2·M_R + 96 ⇒ M_R = 32 (g/mol). Vậy R là nguyên tố Sulfur (Lưu huỳnh - S), oxide cao nhất là SO₃ và hợp chất khí với H là H₂S (M = 34 g/mol), trong đó %m_S = (32 / 34) × 100% ≈ 94,12%.",
    ),
    C(
        10,
        "lien-ket-hoa-hoc",
        "Quy tắc Octet, Liên kết Ion, Liên kết Cộng hóa trị (Liên kết σ và π) & Liên kết Hydrogen - Tương tác Van der Waals",
        "🔗",
        "Phân loại liên kết theo hiệu độ âm điện Δχ, xác định số liên kết sigma (σ) và pi (π), và giải thích ảnh hưởng của liên kết Hydrogen đến nhiệt độ sôi, độ tan.",
        "Vì sao Nước (H₂O, M = 18) lại là chất lỏng sôi ở 100°C trong khi H₂S (M = 34) lại là chất khí?",
        "Mặc dù phân tử khối của H₂O nhỏ hơn H₂S, nhưng ở điều kiện thường H₂O là chất lỏng có nhiệt độ sôi cao bất thường (100°C) nhờ sự hình thành Liên kết Hydrogen giữa các phân tử nước.",
        "Theo quy tắc Octet (bát tử), trong quá trình hình thành liên kết hóa học, nguyên tử của các nguyên tố nhóm A có xu hướng nhường, nhận hoặc góp chung electron để đạt tới cấu hình bền vững có 8 electron ở lớp ngoài cùng của khí hiếm (hoặc 2e như Helium).",
        "• Phân loại liên kết hóa học dựa vào Hiệu độ âm điện Δχ = |χ_A − χ_B|:\n"
        "  + 0 ≤ Δχ < 0,4: Liên kết cộng hóa trị KHÔNG PHÂN CỰC (như H₂, Cl₂, O₂, N₂, CH₄).\n"
        "  + 0,4 ≤ Δχ < 1,7: Liên kết cộng hóa trị PHÂN CỰC (cặp e chung lệch về phía nguyên tử có độ âm điện lớn hơn, như HCl, H₂O, NH₃).\n"
        "  + Δχ ≥ 1,7: Liên kết ION (thường giữa kim loại điển hình và phi kim điển hình, như NaCl, KF, CaO, MgCl₂).\n"
        "• Liên kết Sigma (σ - xen phủ trục bền vững) và Liên kết Pi (π - xen phủ bên kém bền hơn): Liên kết đơn (A–B) gồm 1σ; Liên kết đôi (A=B) gồm 1σ + 1π; Liên kết ba (A≡B) gồm 1σ + 2π.\n"
        "• Liên kết Hydrogen (liên kết yếu hình thành giữa nguyên tử H đã liên kết với nguyên tử có độ âm điện lớn F, O, N với nguyên tử F, O, N còn cặp e hóa trị chưa liên kết của phân tử khác: ...X–H•••Y): làm TĂNG nhiệt độ sôi và TĂNG độ tan trong nước (như HF, H₂O, NH₃, C₂H₅OH, CH₃COOH).\n"
        "• Tương tác Van der Waals: tăng theo sự tăng khối lượng phân tử và kích thước lớp vỏ electron (làm nhiệt độ sôi tăng dần từ F₂ < Cl₂ < Br₂ < I₂).",
        [
            {
                "category": "I. Thang Hiệu độ âm điện (Δχ) & Đếm số Liên kết Sigma (σ) – Pi (π)",
                "items": [
                    {"name": "Phân loại liên kết theo Δχ = |χ_A − χ_B|", "formula": "0 ≤ Δχ < 0,4: CHT không cực ; 0,4 ≤ Δχ < 1,7: CHT có cực ; Δχ ≥ 1,7: Liên kết Ion", "note": "Một số ngoại lệ như HF (Δχ=1,78 là CHT phân cực mạnh), AlCl₃ (CHT)"},
                    {"name": "Số liên kết σ và π trong liên kết đơn, đôi, ba", "formula": "Liên kết đơn (–): 1σ ; Liên kết đôi (=): 1σ + 1π ; Liên kết ba (≡): 1σ + 2π", "note": "Ví dụ: N≡N có 1σ + 2π (năng lượng liên kết rất lớn nên N₂ rất trơ ở t° thường)"},
                ],
            },
            {
                "category": "II. Liên kết Hydrogen (...X–H•••Y với X, Y ∈ {F, O, N}) & Tương tác Van der Waals",
                "items": [
                    {"name": "Điều kiện tạo Liên kết Hydrogen liên phân tử", "formula": "Phân tử chứa nhóm –O–H (H₂O, ROH, RCOOH), H–F hoặc –N–H (NH₃, RNH₂)", "note": "Biểu diễn bằng dấu ba chấm (•••)"},
                    {"name": "Thứ tự Nhiệt độ sôi của các hợp chất hữu cơ cùng C", "formula": "Carboxylic acid (RCOOH) > Alcohol (ROH) > Ester / Aldehyde > Hydrocarbon", "note": "Do RCOOH tạo liên kết hydrogen dạng dimer bền hơn ROH, còn hydrocarbon không có LK hydrogen"},
                ],
            },
        ],
        "Xét phân tử Ethylene (CH₂=CH₂) và phân tử Acetylene (CH≡CH). Hãy xác định tổng số liên kết sigma (σ) và số liên kết pi (π) có trong mỗi phân tử.",
        "Trong phân tử Ethylene (H₂C=CH₂) có 4 liên kết đơn C–H (4σ) và 1 liên kết đôi C=C (1σ + 1π) ⇒ tổng cộng có 5 liên kết σ và 1 liên kết π. Trong phân tử Acetylene (H–C≡C–H) có 2 liên kết đơn C–H (2σ) và 1 liên kết ba C≡C (1σ + 2π) ⇒ tổng cộng có 3 liên kết σ và 2 liên kết π.",
        "Vì sao ở điều kiện thường, Ethanol (C₂H₅OH, M = 46) là chất lỏng sôi ở 78,3°C và tan vô hạn trong nước, trong khi Dimethyl ether (CH₃–O–CH₃, cũng có cùng công thức phân tử C₂H₆O và M = 46) lại là chất khí sôi ở −24°C và ít tan trong nước?",
        [
            "Vì C₂H₅OH có khối lượng phân tử lớn hơn CH₃–O–CH₃",
            "Vì trong C₂H₅OH có liên kết ion bền vững",
            "Vì C₂H₅OH có nguyên tử H linh động gắn trực tiếp với O (nhóm –OH) nên tạo được LIÊN KẾT HYDROGEN liên phân tử giữa các phân tử rượu và với nước, còn CH₃–O–CH₃ không tạo được liên kết hydrogen giữa các phân tử của nó",
            "Vì CH₃–O–CH₃ có liên kết ba bền vững",
        ],
        2,
        "Giải thích cấu trúc xoắn kép bền vững của phân tử DNA di truyền (nhờ hàng triệu liên kết hydrogen giữa các cặp base A–T và G–C), tính chất bất thường của nước đá nổi trên nước lỏng và thiết kế dung môi.",
        "Tại sao khi nước đóng băng thành nước đá ở 0°C, thể tích của nước đá lại TĂNG LÊN (khối lượng riêng giảm xuống còn ~0,92 g/cm³) khiến nước đá nổi trên mặt nước và làm vỡ chai thủy tinh đựng đầy nước để trong ngăn đá tủ lạnh?",
        "Ở trạng thái nước đá rắn, các phân tử H₂O liên kết với nhau bằng mạng lưới liên kết hydrogen chặt chẽ theo cấu trúc tứ diện đều, tạo ra cấu trúc tinh thể rỗng có nhiều khoảng trống hình lục giác bên trong. Do đó cùng một khối lượng nước khi đông đặc thành đá sẽ chiếm thể tích lớn hơn (~tăng 9% thể tích), làm giảm khối lượng riêng và gây áp lực làm nứt vỡ chai thủy tinh đậy kín.",
    ),
    C(
        10,
        "phan-ung-oxy-hoa-khu",
        "Số oxi hóa, Phản ứng Oxi hóa – Khử & Phương pháp Thăng bằng Electron (Bảo toàn Electron)",
        "⚡",
        "Xác định nhanh số oxi hóa của nguyên tố, phân biệt chất khử - chất oxi hóa và cân bằng phản ứng oxi hóa - khử bằng phương pháp thăng bằng electron.",
        "Cuộc trao đổi electron giữa các nguyên tử",
        "Trong công nghệ luyện kim, pin điện thoại, quá trình hô hấp và quang hợp, bản chất sâu xa của các phản ứng chính là sự dịch chuyển electron từ chất khử sang chất oxi hóa.",
        "Phản ứng oxi hóa – khử là phản ứng hóa học trong đó có sự chuyển dịch electron giữa các chất phản ứng, hay là phản ứng có sự THAY ĐỔI SỐ OXI HÓA của ít nhất một nguyên tố hóa học.",
        "• Bốn quy tắc xác định Số oxi hóa: 1) Trong đơn chất, số oxi hóa của nguyên tố bằng 0; 2) Trong phân tử, tổng số oxi hóa của các nguyên tử bằng 0; 3) Trong ion đơn nguyên tử, số oxi hóa bằng điện tích ion; trong ion đa nguyên tử, tổng số oxi hóa bằng điện tích ion; 4) Trong hầu hết hợp chất: H có số oxi hóa +1 (trừ hydride kim loại NaH, CaH₂ là −1), O có số oxi hóa −2 (trừ H₂O₂, Na₂O₂ là −1 và OF₂ là +2), kim loại kiềm (nhóm IA) luôn +1, kiềm thổ (IIA) luôn +2, Al luôn +3, F luôn −1.\n"
        "• Khái niệm cốt lõi (Mẹo nhớ: 'Khử cho – O nhận ; Khử tăng – O giảm'):\n"
        "  + CHẤT KHỬ (chất bị oxi hóa): là chất NHƯỜNG electron (có số oxi hóa TĂNG sau phản ứng). Quá trình chất khử nhường electron gọi là QUÁ TRÌNH OXI HÓA (sự oxi hóa).\n"
        "  + CHẤT OXI HÓA (chất bị khử): là chất NHẬN electron (có số oxi hóa GIẢM sau phản ứng). Quá trình chất oxi hóa nhận electron gọi là QUÁ TRÌNH KHỬ (sự khử).\n"
        "• Định luật Bảo toàn Electron (chìa khóa giải nhanh bài toán kim loại tác dụng với HNO₃, H₂SO₄ đặc): Tổng số mol electron mà các chất khử nhường luôn bằng tổng số mol electron mà các chất oxi hóa nhận (Σn_e_nhường = Σn_e_nhận).",
        [
            {
                "category": "I. Khái niệm Chất khử – Chất oxi hóa ('Khử cho – O nhận ; Khử tăng – O giảm')",
                "items": [
                    {"name": "Chất khử (Chất bị oxi hóa)", "formula": "Nhường electron (Số oxi hóa TĂNG ↑)  ───►  Quá trình OXI HÓA (Sự oxi hóa)", "note": "Ví dụ: Fe⁰ → Fe⁺³ + 3e (Fe là chất khử)"},
                    {"name": "Chất oxi hóa (Chất bị khử)", "formula": "Nhận electron (Số oxi hóa GIẢM ↓)  ───►  Quá trình KHỬ (Sự khử)", "note": "Ví dụ: N⁺⁵ + 3e → N⁺² (HNO₃ là chất oxi hóa)"},
                ],
            },
            {
                "category": "II. Định luật Bảo toàn Electron (Giải siêu tốc bài toán Kim loại + HNO₃ / H₂SO₄ đặc)",
                "items": [
                    {"name": "Phương trình Bảo toàn Electron", "formula": "Σn_e(nhường) = Σn_e(nhận)", "note": "Không cần viết và cân bằng từng PTHH dài dòng!"},
                    {"name": "Kim loại M (hóa trị cao nhất n) tác dụng với HNO₃ tạo các sản phẩm khử", "formula": "n · n_M = 1 · n_NO₂ + 3 · n_NO + 8 · n_N₂O + 10 · n_N₂ + 8 · n_NH₄NO₃", "note": "Do N⁺⁵ → N⁺⁴(NO₂, 1e) ; N⁺²(NO, 3e) ; 2N⁺¹(N₂O, 8e) ; 2N⁰(N₂, 10e) ; N⁻³(NH₄⁺, 8e)"},
                    {"name": "Kim loại M tác dụng với H₂SO₄ đặc, nóng tạo SO₂, S, H₂S", "formula": "n · n_M = 2 · n_SO₂ + 6 · n_S + 8 · n_H₂S", "note": "Do S⁺⁶ → S⁺⁴(SO₂, 2e) ; S⁰(6e) ; S⁻²(H₂S, 8e)"},
                ],
            },
        ],
        "Xác định chất khử, chất oxi hóa và cân bằng phản ứng sau bằng phương pháp thăng bằng electron: Cu + HNO₃(loãng) → Cu(NO₃)₂ + NO↑ + H₂O.",
        "Số oxi hóa thay đổi: Cu⁰ → Cu⁺² + 2e (nhân hệ số 3) và N⁺⁵ + 3e → N⁺² (nhân hệ số 2). Trong đó Cu là chất khử, HNO₃ là chất oxi hóa (kiêm môi trường tạo muối). Điền hệ số 3 vào Cu(NO₃)₂ và 2 vào NO; đếm tổng số nguyên tử N ở vế phải là 3·2 + 2 = 8 ⇒ điền 8 vào HNO₃ và 4 vào H₂O. Phương trình cân bằng: 3Cu + 8HNO₃ → 3Cu(NO₃)₂ + 2NO↑ + 4H₂O.",
        "Số oxi hóa của nguyên tố Manganese (Mn), Chromium (Cr) và Nitrogen (N) trong các hợp chất/ion KMnO₄, K₂Cr₂O₇ và NH₄NO₃ lần lượt là:",
        [
            "+7 ; +6 ; (−3 và +5)",
            "+6 ; +6 ; (+3 và +5)",
            "+7 ; +3 ; (−3 và +5)",
            "+5 ; +6 ; (−3 và +3)",
        ],
        0,
        "Giải thích nguyên lý pin điện hóa, máy đo nồng độ cồn của cảnh sát giao thông (oxi hóa C₂H₅OH bằng K₂Cr₂O₇ làm đổi màu từ da cam sang xanh lục Cr³⁺) và luyện kim.",
        "Hòa tan hoàn toàn 11,6 gam hỗn hợp gồm hai kim loại Iron (Fe, M = 56) và Copper (Cu, M = 64) vào dung dịch HNO₃ loãng dư, sau phản ứng thu được 4,958 lít khí NO duy nhất (ở đkc 25°C, 1 bar; NO là sản phẩm khử duy nhất). Hãy áp dụng định luật Bảo toàn Electron để tính khối lượng của mỗi kim loại trong hỗn hợp ban đầu.",
        "Gọi số mol của Fe và Cu trong hỗn hợp lần lượt là x và y (mol). Tổng khối lượng hỗn hợp: 56x + 64y = 11,6 (1). Số mol khí NO (đkc) là: n_NO = 4,958 / 24,79 = 0,2 (mol). Quá trình nhường e: Fe⁰ → Fe⁺³ + 3e (3x mol e) và Cu⁰ → Cu⁺² + 2e (2y mol e). Quá trình nhận e: N⁺⁵ + 3e → N⁺² (3 · 0,2 = 0,6 mol e). Theo định luật bảo toàn electron: 3x + 2y = 0,6 (2). Giải hệ (1) và (2) được: x = 0,1 (mol) và y = 0,15 (mol). Vậy m_Fe = 0,1 × 56 = 5,6 (gam) và m_Cu = 0,15 × 64 = 9,6 (gam).",
    ),
    C(
        10,
        "nang-luong-hoa-hoc",
        "Năng lượng Hóa học – Biến thiên Enthalpy chuẩn (Δ_r H°₂₉₈) & Tính Δ_r H°₂₉₈ theo Nhiệt tạo thành và Năng lượng liên kết",
        "🔥",
        "Hiểu phương trình nhiệt hóa học, dấu của biến thiên enthalpy (Δ_r H°₂₉₈ < 0 tỏa nhiệt, > 0 thu nhiệt) và 2 công thức tính Δ_r H°₂₉₈.",
        "Định lượng năng lượng tỏa ra hay thu vào của phản ứng",
        "Tại sao đốt 1 mol khí Methane lại tỏa ra đúng 890 kJ nhiệt lượng, còn nung 1 mol đá vôi CaCO₃ lại cần cung cấp 178,5 kJ nhiệt lượng? Nhiệt hóa học giúp ta tính toán chính xác năng lượng của mọi phản ứng.",
        "Biến thiên enthalpy của phản ứng (nhiệt phản ứng, ký hiệu Δ_r H, ở điều kiện chuẩn 25°C = 298 K, 1 bar ký hiệu là Δ_r H°₂₉₈, đơn vị kJ hoặc kJ/mol) là nhiệt lượng tỏa ra hay thu vào của một phản ứng hóa học khi được thực hiện ở áp suất không đổi.",
        "• Quy ước dấu của Δ_r H°₂₉₈:\n"
        "  + Nếu Δ_r H°₂₉₈ < 0 (dấu ÂM): Phản ứng TỎA NHIỆT (năng lượng của hệ chất phản ứng lớn hơn năng lượng của hệ sản phẩm; phản ứng càng tỏa nhiều nhiệt thì càng dễ tự diễn ra).\n"
        "  + Nếu Δ_r H°₂₉₈ > 0 (dấu DƯƠNG): Phản ứng THU NHIỆT (cần cung cấp nhiệt từ bên ngoài).\n"
        "• Enthalpy tạo thành chuẩn (Nhiệt tạo thành chuẩn, ký hiệu Δ_f H°₂₉₈, đơn vị kJ/mol): là biến thiên enthalpy của phản ứng tạo thành 1 mol chất đó từ các ĐƠN CHẤT ở dạng bền vững nhất ở điều kiện chuẩn. Lưu ý: Nhiệt tạo thành chuẩn của mọi ĐƠN CHẤT ở dạng bền nhất (như O₂(g), H₂(g), N₂(g), Fe(s), C(graphite)...) luôn BẰNG 0!\n"
        "• Hai công thức tính biến thiên enthalpy chuẩn Δ_r H°₂₉₈ của phản ứng (Tuyệt đối không nhầm lẫn chiều trừ của hai công thức này!).",
        [
            {
                "category": "I. Hai Công thức Vàng tính Biến thiên Enthalpy chuẩn Δ_r H°₂₉₈",
                "items": [
                    {"name": "1. Tính theo Enthalpy tạo thành chuẩn Δ_f H°₂₉₈ ('SẢN PHẨM trừ ĐẦU')", "formula": "Δ_r H°₂₉₈ = Σ [ ν_sp · Δ_f H°₂₉₈(sản_phẩm) ]  −  Σ [ ν_tg · Δ_f H°₂₉₈(chất_đầu) ]", "note": "Lưu ý: Δ_f H°₂₉₈ của ĐƠN CHẤT bền bằng 0! ; ν là hệ số cân bằng trong PTHH"},
                    {"name": "2. Tính theo Năng lượng liên kết E_b (chất ở thể khí, 'ĐẦU trừ SẢN PHẨM')", "formula": "Δ_r H°₂₉₈ = Σ [ E_b(chất_đầu) ]  −  Σ [ E_b(sản_phẩm) ]", "note": "Phá vỡ liên kết cũ (chất đầu) cần thu năng lượng (+) ; Hình thành liên kết mới (sản phẩm) tỏa năng lượng (−)"},
                ],
            },
            {
                "category": "II. Biến đổi Phương trình Nhiệt hóa học (Định luật Hess)",
                "items": [
                    {"name": "Nhân hệ số k hoặc Đảo chiều phản ứng", "formula": "Nhân PTHH với k ⇒ nhân Δ_r H°₂₉₈ với k  ;  Đảo chiều phản ứng ⇒ ĐỔI DẤU Δ_r H°₂₉₈", "note": "Cộng hai PTHH ⇒ cộng đại số hai giá trị Δ_r H°₂₉₈"},
                ],
            },
        ],
        "Cho phản ứng đốt cháy hoàn toàn khí Methane: CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l). Biết nhiệt tạo thành chuẩn Δ_f H°₂₉₈ của các chất lần lượt là: CH₄(g) = −74,6 kJ/mol; CO₂(g) = −393,5 kJ/mol; H₂O(l) = −285,8 kJ/mol. Hãy tính biến thiên enthalpy chuẩn Δ_r H°₂₉₈ của phản ứng trên và cho biết phản ứng tỏa nhiệt hay thu nhiệt.",
        "Vì O₂(g) là đơn chất bền nên Δ_f H°₂₉₈(O₂(g)) = 0. Áp dụng công thức tính theo nhiệt tạo thành ('Sản phẩm trừ Đầu'): Δ_r H°₂₉₈ = [ 1·Δ_f H°₂₉₈(CO₂) + 2·Δ_f H°₂₉₈(H₂O) ] − [ 1·Δ_f H°₂₉₈(CH₄) + 2·Δ_f H°₂₉₈(O₂) ] = [ (−393,5) + 2·(−285,8) ] − [ (−74,6) + 0 ] = −965,1 + 74,6 = −890,5 (kJ). Vì Δ_r H°₂₉₈ = −890,5 kJ < 0 nên đây là phản ứng TỎA NHIỆT rất mạnh.",
        "Cho phản ứng tổng hợp khí Hydrogen chloride: H₂(g) + Cl₂(g) → 2HCl(g). Biết năng lượng liên kết E_b (ở điều kiện chuẩn) của H–H là 436 kJ/mol, của Cl–Cl là 243 kJ/mol và của H–Cl là 432 kJ/mol. Biến thiên enthalpy chuẩn Δ_r H°₂₉₈ của phản ứng trên bằng:",
        ["+185 kJ", "−185 kJ", "−247 kJ", "+247 kJ"],
        1,
        "Tính toán năng suất tỏa nhiệt của các loại nhiên liệu (xăng, khí thiên nhiên, hydrogen xanh) và tính toán năng lượng calo trong khẩu phần dinh dưỡng.",
        "Phản ứng quang hợp ở cây xanh tổng hợp Glucose từ khí CO₂ và H₂O nhờ năng lượng ánh sáng Mặt Trời có phương trình nhiệt hóa học: 6CO₂(g) + 6H₂O(l) → C₆H₁₂O₆(s) + 6O₂(g) với Δ_r H°₂₉₈ = +2 803 kJ. Ngược lại, trong cơ thể người, quá trình hô hấp tế bào oxi hóa hoàn toàn 18 gam Glucose C₆H₁₂O₆(s) (M = 180 g/mol) thành CO₂(g) và H₂O(l) ở điều kiện chuẩn sẽ giải phóng ra bao nhiêu kJ năng lượng?",
        "Phản ứng oxi hóa Glucose trong hô hấp tế bào là phản ứng ngược của phản ứng quang hợp: C₆H₁₂O₆(s) + 6O₂(g) → 6CO₂(g) + 6H₂O(l) nên có biến thiên enthalpy chuẩn đổi dấu là Δ_r H°₂₉₈ = −2 803 kJ/mol (tức 1 mol Glucose bị oxi hóa tỏa ra 2 803 kJ năng lượng). Số mol của 18 gam Glucose là: n = 18 / 180 = 0,1 (mol). Vậy nhiệt lượng giải phóng ra là: Q = 0,1 × 2 803 = 280,3 (kJ).",
    ),
    C(
        10,
        "nhom-halogen",
        "Nguyên tố Nhóm Halogen (Nhóm VIIA: F₂, Cl₂, Br₂, I₂), Hydrogen Halide (HX) & Muối Halide",
        "🧪",
        "Nắm vững quy luật biến đổi tính chất đơn chất nhóm Halogen (từ F₂ đến I₂), dãy độ mạnh acid HF < HCl < HBr < HI, tính khử của HX và nhận biết ion Halide bằng AgNO₃.",
        "Từ muối biển, kem đánh răng Fluorine đến muối Iốt phòng bướu cổ",
        "Nhóm Halogen (nhóm VIIA, nghĩa là 'tạo ra muối') gồm các nguyên tố Fluorine (F), Chlorine (Cl), Bromine (Br), Iodine (I)... có 7 electron hóa trị ns²np⁵, là những phi kim điển hình nhất trong Bảng tuần hoàn.",
        "Ở dạng đơn chất, các halogen tồn tại dưới dạng phân tử hai nguyên tử X₂ (F₂, Cl₂, Br₂, I₂) với liên kết cộng hóa trị không phân cực. Đi từ F₂ đến I₂, tính oxi hóa giảm dần còn nhiệt độ nóng chảy và nhiệt độ sôi tăng dần.",
        "• Biến đổi trạng thái và màu sắc đơn chất X₂ ở điều kiện thường (do tương tác Van der Waals tăng theo kích thước phân tử): F₂ (khí màu lục nhạt) → Cl₂ (khí màu vàng lục) → Br₂ (chất lỏng màu nâu đỏ) → I₂ (tinh thể rắn màu đen tím, có tính THĂNG HOA: chuyển thẳng từ rắn sang hơi màu tím khi đun nóng mà không qua thể lỏng!).\n"
        "• Tính oxi hóa của đơn chất giảm dần: F₂ > Cl₂ > Br₂ > I₂ (Halogen mạnh đẩy được halogen yếu hơn ra khỏi dung dịch muối halide từ Cl₂ trở đi: Cl₂ + 2NaBr → 2NaCl + Br₂; Br₂ + 2NaI → 2NaBr + I₂. Riêng F₂ mãnh liệt bốc cháy ngay với nước: 2F₂ + 2H₂O → 4HF + O₂↑!).\n"
        "• Các Hydrogen halide (HF, HCl, HBr, HI): Khi tan trong nước tạo thành dung dịch Hydrohalic acid với TÍNH ACID TĂNG DẦN: HF (acid yếu, có khả năng ăn mòn thủy tinh SiO₂!) < HCl < HBr < HI (acid rất mạnh); đồng thời TÍNH KHỬ TĂNG DẦN: HF (không có tính khử) < HCl < HBr < HI (HBr và HI khử được H₂SO₄ đặc thành SO₂, H₂S).\n"
        "• Nhận biết các ion Halide (F⁻, Cl⁻, Br⁻, I⁻) bằng dung dịch Silver nitrate (AgNO₃).",
        [
            {
                "category": "I. Quy luật biến đổi trong Nhóm Halogen (F₂ → Cl₂ → Br₂ → I₂) & Phản ứng đặc trưng",
                "items": [
                    {"name": "Tính oxi hóa đơn chất giảm dần & Phản ứng thế Halide", "formula": "Tính oxi hóa: F₂ > Cl₂ > Br₂ > I₂  ;  Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂  ;  Br₂ + 2I⁻ → 2Br⁻ + I₂", "note": "Riêng F₂ tác dụng mãnh liệt với H₂O ở ngay t° thường: 2F₂ + 2H₂O → 4HF + O₂↑"},
                    {"name": "Điều chế khí Cl₂ trong PTN (từ HCl đặc + chất oxi hóa mạnh)", "formula": "MnO₂ + 4HCl(đặc) ──(t°)──► MnCl₂ + Cl₂↑ + 2H₂O  ;  2KMnO₄ + 16HCl(đặc) → 2KCl + 2MnCl₂ + 5Cl₂↑ + 8H₂O", "note": ""},
                ],
            },
            {
                "category": "II. Dãy Hydrohalic acid (HF, HCl, HBr, HI) & Nhận biết Ion Halide bằng dd AgNO₃",
                "items": [
                    {"name": "Quy luật Tính Acid & Tính Khử của HX", "formula": "Tính Acid tăng dần: HF (yếu) < HCl < HBr < HI (mạnh nhất)  ;  Tính Khử tăng dần: HCl < HBr < HI", "note": "HF ăn mòn thủy tinh: SiO₂ + 4HF → SiF₄↑ + 2H₂O (dùng khắc chữ lên thủy tinh)"},
                    {"name": "Phản ứng nhận biết F⁻, Cl⁻, Br⁻, I⁻ bằng dung dịch AgNO₃", "formula": "F⁻ + Ag⁺: KHÔNG kết tủa (AgF tan!) ; Cl⁻: AgCl↓ TRẮNG ; Br⁻: AgBr↓ VÀNG NHẠT ; I⁻: AgI↓ VÀNG ĐẬM", "note": "Dấu hiệu màu sắc kết tủa tăng dần độ đậm từ Cl⁻ → Br⁻ → I⁻"},
                ],
            },
        ],
        "Trình bày cách phân biệt 4 dung dịch muối không màu đựng trong 4 lọ mất nhãn: NaF, NaCl, NaBr và NaI chỉ bằng một thuốc thử duy nhất.",
        "Dùng dung dịch Silver nitrate (AgNO₃) nhỏ vào 4 mẫu thử của 4 dung dịch: Mẫu không xuất hiện kết tủa là NaF (vì AgF tan trong nước); mẫu xuất hiện kết tủa màu TRẮNG (AgCl↓) là NaCl; mẫu xuất hiện kết tủa màu VÀNG NHẠT (AgBr↓) là NaBr; mẫu xuất hiện kết tủa màu VÀNG ĐẬM (AgI↓) là NaI.",
        "Vì sao người ta KHÔNG THỂ đựng dung dịch Hydrofluoric acid (HF) trong lọ bằng thủy tinh (chứa thành phần chính là SiO₂) mà phải đựng trong lọ bằng nhựa chất dẻo?",
        [
            "Vì HF là một acid mạnh nhất trong dãy HX",
            "Vì dung dịch HF có tính oxi hóa mạnh làm nổ thủy tinh",
            "Vì HF phản ứng hóa học hòa tan Silicon dioxide (SiO₂) trong thủy tinh theo phương trình: SiO₂ + 4HF → SiF₄↑ + 2H₂O",
            "Vì ánh sáng xuyên qua lọ thủy tinh làm phân hủy HF",
        ],
        2,
        "Sử dụng hợp chất Fluorine trong kem đánh răng ngừa sâu răng và lớp chống dính Teflon, dùng hợp chất Iodine (KIO₃/KI) trộn vào muối ăn phòng bệnh bướu cổ và dùng AgBr trong phim ảnh.",
        "Cho 15,8 gam Potassium permanganate (KMnO₄, M = 158 g/mol) tác dụng hoàn toàn với dung dịch Hydrochloric acid (HCl) đặc, dư theo phản ứng: 2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂↑ + 8H₂O. Toàn bộ lượng khí Cl₂ sinh ra được dẫn vào dung dịch chứa 40 gam Sodium bromide (NaBr, M = 103 g/mol). Hãy tính thể tích khí Cl₂ (ở đkc) và khối lượng Bromine (Br₂, M = 160) tạo thành.",
        "Số mol KMnO₄ là: n_KMnO₄ = 15,8 / 158 = 0,1 (mol). Theo PTHH (hoặc bảo toàn e: 5·n_KMnO₄ = 2·n_Cl₂): n_Cl₂ = 2,5 · 0,1 = 0,25 (mol). Thể tích khí Cl₂ (đkc): V = 0,25 × 24,79 = 6,1975 (lít). Khi dẫn Cl₂ vào dd NaBr (n_NaBr = 40 / 103 ≈ 0,388 mol): Cl₂ + 2NaBr → 2NaCl + Br₂. Vì n_Cl₂ / 1 = 0,25 > n_NaBr / 2 ≈ 0,194 nên NaBr phản ứng hết (tính theo NaBr hoặc nếu lấy 51,5 g NaBr = 0,5 mol thì vừa đủ 0,25 mol Br₂): với 40 g NaBr thì n_Br₂ = (1/2) · n_NaBr = 20 / 103 (mol) ⇒ m_Br₂ = (20 / 103) × 160 ≈ 31,07 (gam).",
    ),

    # =========================================================
    # HÓA HỌC LỚP 11 (7 BÀI)
    # =========================================================
    C(
        11,
        "toc-do-phan-ung",
        "Tốc độ Phản ứng, Định luật Tác dụng khối lượng (v = k·C_A^a·C_B^b) & Hệ số nhiệt độ Van't Hoff (γ)",
        "⏱️",
        "Tính tốc độ trung bình của phản ứng, viết biểu thức tốc độ tức thời theo định luật tác dụng khối lượng và vận dụng công thức hệ số nhiệt độ Van't Hoff.",
        "Kiểm soát tốc độ phản ứng từ phòng thí nghiệm đến nhà máy",
        "Có những phản ứng xảy ra trong tích tắc như pháo hoa nổ hay kết tủa AgCl, nhưng có phản ứng kéo dài hàng năm như sự ăn mòn kim loại hay hàng triệu năm như sự hình thành than đá.",
        "Tốc độ phản ứng của một phản ứng hóa học là đại lượng đặc trưng cho sự biến thiên nồng độ của một trong các chất phản ứng hoặc sản phẩm trong một đơn vị thời gian (đơn vị thường dùng: mol/(L·s) hay M/s).",
        "• Tốc độ trung bình của phản ứng aA + bB → cC + dD: v̄ = −(1/a)·(ΔC_A / Δt) = −(1/b)·(ΔC_B / Δt) = +(1/c)·(ΔC_C / Δt) = +(1/d)·(ΔC_D / Δt) (có dấu '−' trước chất tham gia vì nồng độ chất tham gia giảm dần theo thời gian để v̄ luôn dương).\n"
        "• Định luật tác dụng khối lượng (Guldberg – Waage) cho phản ứng đơn giản aA + bB → sản phẩm: v = k · C_Aᵃ · C_Bᵇ (trong đó k là hằng số tốc độ phản ứng, chỉ phụ thuộc vào bản chất chất phản ứng và nhiệt độ; Lưu ý: KHÔNG đưa nồng độ của chất RẮN vào biểu thức tốc độ!).\n"
        "• Quy tắc Van't Hoff về ảnh hưởng của nhiệt độ đến tốc độ phản ứng: Khi nhiệt độ tăng thêm 10°C thì tốc độ của đa số phản ứng tăng từ 2 đến 4 lần (con số γ = 2 ÷ 4 gọi là hệ số nhiệt độ Van't Hoff): v₂ / v₁ = γ^((t₂ − t₁)/10).",
        [
            {
                "category": "I. Tốc độ trung bình (v̄) & Định luật Tác dụng khối lượng (v)",
                "items": [
                    {"name": "Tốc độ trung bình của phản ứng aA + bB → cC + dD", "formula": "v̄ = −(1/a) · [(C₂ − C₁) / Δt]_A = +(1/c) · [(C₂ − C₁) / Δt]_C = (1 / hệ_số) · (|ΔC| / Δt)", "note": "Đơn vị: M/s hoặc M/phút"},
                    {"name": "Biểu thức tốc độ tức thời (Phản ứng đơn giản)", "formula": "v = k · C_Aᵃ · C_Bᵇ", "note": "Chất rắn nguyên chất có nồng độ coi như hằng số nên KHÔNG có mặt trong biểu thức v!"},
                ],
            },
            {
                "category": "II. Công thức Hệ số nhiệt độ Van't Hoff (γ)",
                "items": [
                    {"name": "Tỉ số tốc độ phản ứng khi nhiệt độ thay đổi từ t₁°C đến t₂°C", "formula": "v₂ / v₁ = k₂ / k₁ = γ^[ (t₂ − t₁) / 10 ]", "note": "γ: hệ số nhiệt độ Van't Hoff (thường γ = 2 ÷ 4)"},
                    {"name": "Tỉ số thời gian thực hiện phản ứng (tỉ lệ nghịch với tốc độ)", "formula": "τ₁ / τ₂ = v₂ / v₁ = γ^[ (t₂ − t₁) / 10 ]", "note": "Tốc độ tăng bao nhiêu lần thì thời gian phản ứng giảm bấy nhiêu lần"},
                ],
            },
        ],
        "Xét phản ứng đơn giản xảy ra trong bình kín giữa các chất khí: 2NO(g) + O₂(g) → 2NO₂(g). Hãy viết biểu thức tốc độ tức thời của phản ứng và cho biết tốc độ phản ứng thay đổi như thế nào nếu giữ nguyên nhiệt độ và tăng áp suất chung của hệ (bằng cách nén giảm thể tích bình) lên gấp 3 lần?",
        "Biểu thức tốc độ tức thời: v = k · C_NO² · C_O₂. Khi nén bình để áp suất tăng gấp 3 lần (thể tích giảm 3 lần) ở nhiệt độ không đổi thì nồng độ mol của cả NO và O₂ đều tăng gấp 3 lần (C'_NO = 3C_NO và C'_O₂ = 3C_O₂). Khi đó tốc độ mới là: v' = k · (3C_NO)² · (3C_O₂) = 27 · k · C_NO² · C_O₂ = 27v. Vậy tốc độ phản ứng tăng lên 27 lần!",
        "Một phản ứng hóa học có hệ số nhiệt độ Van't Hoff là γ = 3. Nếu tăng nhiệt độ của phản ứng từ 20°C lên 50°C thì tốc độ của phản ứng này tăng lên bao nhiêu lần?",
        ["9 lần", "12 lần", "27 lần", "81 lần"],
        2,
        "Điều chỉnh nhiệt độ, áp suất và xúc tác trong lò tổng hợp công nghiệp, sử dụng nồi áp suất nấu chín thức ăn nhanh hơn (do tăng áp suất làm nhiệt độ sôi của nước tăng lên ~120°C).",
        "Ở 25°C, một phản ứng hóa học cần 32 phút để hoàn thành. Biết hệ số nhiệt độ Van't Hoff của phản ứng trong khoảng nhiệt độ xét là γ = 2. Hỏi nếu thực hiện phản ứng đó ở nhiệt độ 65°C thì phản ứng sẽ hoàn thành sau bao nhiêu phút?",
        "Độ tăng nhiệt độ là: Δt = 65 − 25 = 40 (°C). Theo quy tắc Van't Hoff, khi tăng nhiệt độ từ 25°C lên 65°C thì tốc độ phản ứng tăng lên: v₂ / v₁ = 2^(40/10) = 2⁴ = 16 (lần). Do thời gian phản ứng tỉ lệ nghịch với tốc độ nên thời gian hoàn thành ở 65°C là: τ₂ = τ₁ / 16 = 32 / 16 = 2 (phút).",
    ),
    C(
        11,
        "can-bang-hoa-hoc",
        "Phản ứng Thuận nghịch, Cân bằng Hóa học, Hằng số cân bằng (K_C) & Nguyên lý chuyển dịch cân bằng Le Chatelier",
        "⚖️",
        "Hiểu bản chất cân bằng động (v_thuận = v_nghịch), viết biểu thức hằng số cân bằng K_C và vận dụng nguyên lý Le Chatelier để dịch chuyển cân bằng.",
        "Cân bằng động và cách tối ưu hiệu suất tổng hợp Ammonia",
        "Trong công nghiệp tổng hợp NH₃ (quy trình Haber – Bosch: N₂ + 3H₂ ⇄ 2NH₃), phản ứng xảy ra theo cả hai chiều thuận và nghịch. Nhờ nguyên lý Le Chatelier, các kỹ sư đã chọn được điều kiện nhiệt độ và áp suất tối ưu nhất.",
        "Phản ứng thuận nghịch (biểu diễn bằng mũi tên hai chiều ⇄) là phản ứng xảy ra theo hai chiều trái ngược nhau trong cùng điều kiện. Trạng thái cân bằng hóa học là trạng thái của phản ứng thuận nghịch khi tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch (v_t = v_n).",
        "• Cân bằng hóa học là một CÂN BẰNG ĐỘNG: tại trạng thái cân bằng, phản ứng thuận và phản ứng nghịch KHÔNG dừng lại mà vẫn tiếp tục diễn ra với tốc độ bằng nhau, do đó nồng độ của tất cả các chất trong hệ giữ không đổi.\n"
        "• Biểu thức hằng số cân bằng K_C của phản ứng aA + bB ⇄ cC + dD: K_C = ([C]ᶜ · [D]ᵈ) / ([A]ᵃ · [B]ᵇ), trong đó [A], [B], [C], [D] là nồng độ mol ở trạng thái cân bằng. Lưu ý cực kỳ quan trọng: K_C CHỈ PHỤ THUỘC VÀO NHIỆT ĐỘ và bản chất phản ứng (không phụ thuộc nồng độ ban đầu); KHÔNG biểu diễn chất RẮN (s) và chất LỎNG nguyên chất (l, như H₂O lỏng khi là dung môi) vào biểu thức K_C!\n"
        "• Nguyên lý chuyển dịch cân bằng Le Chatelier: 'Một phản ứng thuận nghịch đang ở trạng thái cân bằng, khi chịu một tác động từ bên ngoài như biến đổi NỒNG ĐỘ, NHIỆT ĐỘ, ÁP SUẤT thì cân bằng sẽ chuyển dịch theo chiều làm GIẢM tác động bên ngoài đó'. (Lưu ý: Chất xúc tác làm tăng đều tốc độ cả chiều thuận và nghịch nên KHÔNG làm chuyển dịch cân bằng, chỉ giúp hệ nhanh đạt cân bằng hơn!).",
        [
            {
                "category": "I. Trạng thái Cân bằng động & Biểu thức Hằng số cân bằng K_C",
                "items": [
                    {"name": "Điều kiện tại trạng thái cân bằng", "formula": "v_thuận = v_nghịch > 0  ⇒  Nồng độ [A], [B], [C], [D] không đổi theo thời gian", "note": ""},
                    {"name": "Hằng số cân bằng K_C cho phản ứng: aA(g) + bB(g) ⇄ cC(g) + dD(g)", "formula": "K_C = ( [C]ᶜ · [D]ᵈ ) / ( [A]ᵃ · [B]ᵇ )", "note": "KHÔNG viết chất rắn (s) vào K_C! Ví dụ: CaCO₃(s) ⇄ CaO(s) + CO₂(g) có K_C = [CO₂]"},
                ],
            },
            {
                "category": "II. Quy tắc vận dụng Nguyên lý Le Chatelier (3 yếu tố: C, p, T)",
                "items": [
                    {"name": "1. Thay đổi Nồng độ (C)", "formula": "Tăng nồng độ chất X ⇒ Cân bằng chuyển dịch theo chiều làm GIẢM chất X (tiêu thụ X)", "note": "Lấy bớt chất Y ra ⇒ chuyển dịch theo chiều tạo thêm Y"},
                    {"name": "2. Thay đổi Áp suất chung (p - với hệ có chất khí)", "formula": "Tăng áp suất p ⇒ Chuyển dịch về phía có SỐ MOL KHÍ ÍT HƠN ; Giảm p ⇒ về phía số mol khí NHIỀU HƠN", "note": "Nếu tổng hệ số mol khí 2 vế bằng nhau (Δn_khí = 0) thì áp suất không làm dịch chuyển CB!"},
                    {"name": "3. Thay đổi Nhiệt độ (T) — ('Tăng Thu – Giảm Tỏa')", "formula": "TĂNG nhiệt độ ⇒ dịch theo chiều THU NHIỆT (ΔH > 0) ; GIẢM nhiệt độ ⇒ dịch theo chiều TỎA NHIỆT (ΔH < 0)", "note": "Chất xúc tác KHÔNG làm chuyển dịch cân bằng!"},
                ],
            },
        ],
        "Xét cân bằng tổng hợp Ammonia trong công nghiệp: N₂(g) + 3H₂(g) ⇄ 2NH₃(g) có Δ_r H°₂₉₈ = −91,8 kJ < 0 (chiều thuận là tỏa nhiệt và giảm số mol khí từ 4 mol xuống 2 mol). Để cân bằng chuyển dịch theo chiều thuận (tăng hiệu suất tạo NH₃), ta cần tác động vào nồng độ, nhiệt độ và áp suất như thế nào?",
        "Theo nguyên lý Le Chatelier, để cân bằng chuyển dịch theo chiều thuận (tạo thêm NH₃), ta cần: 1) Về nồng độ: Tăng nồng độ N₂ hoặc H₂ và liên tục hóa lỏng tách NH₃ ra khỏi hỗn hợp; 2) Về áp suất: TĂNG áp suất chung của hệ (vì chiều thuận làm giảm số mol khí từ 4 mol xuống 2 mol); 3) Về nhiệt độ: GIẢM nhiệt độ thích hợp (vì chiều thuận là chiều tỏa nhiệt ΔH < 0; trong thực tế duy trì ~400–450°C kết hợp xúc tác bột Fe để đảm bảo tốc độ phản ứng đủ nhanh).",
        "Cho cân bằng hóa học: H₂(g) + I₂(g) ⇄ 2HI(g) có Δ_r H°₂₉₈ < 0. Yếu tố nào dưới đây KHÔNG làm chuyển dịch cân bằng của hệ?",
        [
            "Hạ nhiệt độ của bình phản ứng",
            "Thêm khí H₂ vào bình phản ứng",
            "Tăng áp suất chung của hệ bằng cách nén giảm thể tích bình (vì số mol khí hai vế bằng nhau: 1 + 1 = 2)",
            "Lấy bớt khí HI ra khỏi bình",
        ],
        2,
        "Tối ưu hóa quy trình sản xuất Ammonia (Haber-Bosch), sản xuất Sulfuric acid (tiếp xúc SO₂ + O₂ ⇄ SO₃) và giải thích hiện tượng thạch nhũ trong hang động đá vôi (CaCO₃ + CO₂ + H₂O ⇄ Ca(HCO₃)₂).",
        "Trong một bình kín dung tích 1 lít ở nhiệt độ T không đổi, người ta cho vào 1,0 mol khí CO và 1,0 mol hơi nước H₂O để thực hiện phản ứng thuận nghịch: CO(g) + H₂O(g) ⇄ CO₂(g) + H₂(g). Khi phản ứng đạt tới trạng thái cân bằng thì thu được 0,6 mol khí CO₂. Hãy tính hằng số cân bằng K_C của phản ứng ở nhiệt độ T và hiệu suất của phản ứng thuận.",
        "Vì thể tích bình V = 1 L nên nồng độ mol bằng số mol. Gọi lượng phản ứng là x (M): tại cân bằng [CO₂] = [H₂] = x = 0,6 M. Suy ra nồng độ còn lại tại cân bằng của chất đầu là: [CO] = 1,0 − 0,6 = 0,4 M và [H₂O] = 1,0 − 0,6 = 0,4 M. Hằng số cân bằng ở nhiệt độ T là: K_C = ([CO₂] · [H₂]) / ([CO] · [H₂O]) = (0,6 · 0,6) / (0,4 · 0,4) = 0,36 / 0,16 = 2,25. Hiệu suất phản ứng là: H = (0,6 / 1,0) × 100% = 60%.",
    ),
    C(
        11,
        "su-dien-li",
        "Sự Điện li, Thuyết Acid – Base của Brønsted – Lowry, Giá trị pH & Chuẩn độ Acid – Base",
        "💧",
        "Phân biệt chất điện li mạnh - yếu, định nghĩa Acid (nhường H⁺) - Base (nhận H⁺) theo Brønsted–Lowry, tính pH = −log[H⁺] và bài toán chuẩn độ.",
        "Bản chất của dung dịch dẫn điện và cân bằng pH trong máu người",
        "Máu người luôn duy trì pH ổn định nghiêm ngặt trong khoảng 7,35 – 7,45 nhờ các hệ đệm ion. Thuyết điện li của Arrhenius và thuyết Acid–Base của Brønsted–Lowry giúp giải thích toàn diện các phản ứng trong dung dịch nước.",
        "Sự điện li là quá trình phân li các chất trong nước ra ion. Theo thuyết Brønsted – Lowry (tổng quát hơn thuyết Arrhenius): ACID là chất cho proton (H⁺) và BASE là chất nhận proton (H⁺); chất vừa có khả năng cho H⁺ vừa có khả năng nhận H⁺ được gọi là chất lưỡng tính.",
        "• Phân loại chất điện li:\n"
        "  + Chất điện li MẠNH (phân li hoàn toàn, dùng mũi tên 1 chiều →): gồm các Acid mạnh (HCl, HBr, HI, HNO₃, H₂SO₄, HClO₄), các Base mạnh (NaOH, KOH, Ca(OH)₂, Ba(OH)₂) và hầu hết các Muối tan.\n"
        "  + Chất điện li YẾU (chỉ phân li một phần, dùng mũi tên thuận nghịch ⇄): gồm các Acid yếu (CH₃COOH, HF, H₂CO₃, H₂S, H₂SO₃, HClO...), Base yếu (NH₃, các hydroxide không tan).\n"
        "• Theo thuyết Brønsted – Lowry: NH₃, CO₃²⁻, S²⁻, CH₃COO⁻ là các BASE (vì nhận H⁺ từ nước tạo OH⁻ làm môi trường có pH > 7!); NH₄⁺, Al³⁺, Fe³⁺ là các ACID (thủy phân cho H⁺ làm pH < 7!); HCO₃⁻, HSO₃⁻, HS⁻, H₂PO₄⁻, HPO₄²⁻, Al(OH)₃, Zn(OH)₂, H₂O là các hạt LƯỠNG TÍNH!\n"
        "• Tích số ion của nước ở 25°C: K_w = [H⁺] · [OH⁻] = 10⁻¹⁴; công thức pH = −log[H⁺] và chuẩn độ Acid – Base.",
        [
            {
                "category": "I. Thuyết Acid – Base của Brønsted – Lowry & Sự thủy phân của Muối",
                "items": [
                    {"name": "Định nghĩa Brønsted – Lowry", "formula": "ACID: chất cho proton (H⁺)  ;  BASE: chất nhận proton (H⁺)  ;  LƯỠNG TÍNH: vừa cho vừa nhận H⁺", "note": "Ví dụ: NH₃ + H₂O ⇄ NH₄⁺ + OH⁻ (NH₃ nhận H⁺ nên là Base; H₂O cho H⁺ nên là Acid)"},
                    {"name": "Dự đoán nhanh Môi trường & pH của dung dịch Muối", "formula": "Muối của (KL mạnh + Gốc acid mạnh như NaCl, K₂SO₄): pH = 7 ; (KL mạnh + Gốc acid yếu như Na₂CO₃): pH > 7 ; (KL yếu/NH₄⁺ + Gốc acid mạnh như NH₄Cl, AlCl₃, FeCl₃): pH < 7", "note": ""},
                ],
            },
            {
                "category": "II. Tích số ion của Nước, Công thức tính pH & Chuẩn độ Acid – Base",
                "items": [
                    {"name": "Tích số ion của nước (ở 25°C) & Liên hệ pH, pOH", "formula": "[H⁺] · [OH⁻] = 10⁻¹⁴  ;  pH = −log[H⁺] ⇔ [H⁺] = 10^(−pH)  ;  pOH = −log[OH⁻]  ;  pH + pOH = 14", "note": "Chú ý: Nếu biết [OH⁻] thì tính pOH = −log[OH⁻] rồi suy ra pH = 14 − pOH!"},
                    {"name": "Công thức tại Điểm tương đương trong Chuẩn độ (HCl bằng NaOH)", "formula": "n_H⁺ = n_OH⁻  ⇔  C_A · V_A = C_B · V_B (đối với đơn acid HCl và đơn base NaOH)", "note": "Chất chỉ thị Phenolphthalein chuyển từ không màu sang hồng nhạt bền trong 20s"},
                ],
            },
        ],
        "Tính pH của các dung dịch sau ở 25°C: a) Dung dịch HCl 0,01 M; b) Dung dịch H₂SO₄ 0,005 M (coi phân li hoàn toàn cả 2 nấc); c) Dung dịch Ba(OH)₂ 0,005 M.",
        "a) HCl → H⁺ + Cl⁻ ⇒ [H⁺] = 0,01 = 10⁻² M ⇒ pH = −log(10⁻²) = 2. b) H₂SO₄ → 2H⁺ + SO₄²⁻ ⇒ [H⁺] = 2 · 0,005 = 0,01 = 10⁻² M ⇒ pH = 2. c) Ba(OH)₂ → Ba²⁺ + 2OH⁻ ⇒ [OH⁻] = 2 · 0,005 = 0,01 = 10⁻² M ⇒ pOH = −log(10⁻²) = 2 ⇒ pH = 14 − 2 = 12.",
        "Theo thuyết Brønsted – Lowry, ion nào dưới đây đóng vai trò là chất LƯỠNG TÍNH (vừa có khả năng cho H⁺, vừa có khả năng nhận H⁺) trong dung dịch nước?",
        [
            "Ion Carbonate (CO₃²⁻ — chỉ nhận H⁺ nên là base)",
            "Ion Ammonium (NH₄⁺ — chỉ cho H⁺ nên là acid)",
            "Ion Hydrogencarbonate (HCO₃⁻: cho H⁺ tạo CO₃²⁻ và nhận H⁺ tạo H₂CO₃)",
            "Ion Chloride (Cl⁻ — trung tính)",
        ],
        2,
        "Giải thích vì sao dùng phèn chua KAl(SO₄)₂·12H₂O làm trong nước và dùng vôi khử chua đất phèn (chứa nhiều ion Al³⁺, Fe³⁺ thủy phân tạo môi trường acid pH thấp); thực hành chuẩn độ xác định nồng độ acid trong giấm ăn.",
        "Trộn 200 mL dung dịch HCl 0,15 M với 300 mL dung dịch NaOH 0,12 M. Hãy tính pH của dung dịch thu được sau khi trộn ở 25°C (coi thể tích dung dịch sau khi trộn bằng tổng thể tích hai dung dịch ban đầu).",
        "Tổng thể tích dung dịch sau khi trộn là: V_sau = 0,2 + 0,3 = 0,5 (L). Số mol H⁺ ban đầu: n_H⁺ = 0,2 · 0,15 = 0,030 (mol). Số mol OH⁻ ban đầu: n_OH⁻ = 0,3 · 0,12 = 0,036 (mol). Phản ứng trung hòa: H⁺ + OH⁻ → H₂O. Vì 0,036 > 0,030 nên sau phản ứng OH⁻ còn dư: n_OH⁻(dư) = 0,036 − 0,030 = 0,006 (mol). Nồng độ [OH⁻] dư là: [OH⁻] = 0,006 / 0,5 = 0,012 (M) ⇒ pOH = −log(0,012) ≈ 1,92 ⇒ pH = 14 − 1,92 = 12,08.",
    ),
    C(
        11,
        "nitrogen-ammonia",
        "Đơn chất Nitrogen (N₂), Ammonia (NH₃), Muối Ammonium (NH₄⁺), Nitric Acid (HNO₃) & Hiện tượng Phú dưỡng",
        "🌱",
        "Hiểu liên kết ba siêu bền N≡N của khí N₂, tính base và tính khử của NH₃, tính oxi hóa cực mạnh của HNO₃ và nguyên nhân - hậu quả của hiện tượng phú dưỡng.",
        "Từ khí quyển trơ đến phân đạm và thuốc nổ",
        "Phân tử N₂ có liên kết ba N≡N cực kỳ bền vững (E_b = 945 kJ/mol) nên rất trơ ở nhiệt độ thường, nhưng khi có tia lửa điện sấm sét (3000°C) hoặc trong lò tổng hợp Haber, N₂ chuyển hóa thành các hợp chất nuôi sống toàn bộ cây trồng trên Trái Đất.",
        "Nitrogen (₇N: 1s²2s²2p³) thuộc chu kỳ 2, nhóm VA, có các số oxi hóa từ −3 (NH₃, NH₄⁺), 0 (N₂), +1 (N₂O), +2 (NO), +3 (HNO₂), +4 (NO₂) đến +5 (HNO₃, muối nitrate NO₃⁻).",
        "• Đơn chất N₂: có số oxi hóa 0 trung gian nên vừa có tính oxi hóa (tác dụng với H₂ và kim loại mạnh như Li ở t° thường, Mg, Al ở t° cao tạo nitride), vừa có tính khử (tác dụng với O₂ ở ~3000°C hoặc hồ quang điện tạo NO không màu, sau đó NO hóa nâu ngay trong không khí tạo NO₂!).\n"
        "• Ammonia (NH₃): phân tử có cấu trúc chóp tam giác, phân cực mạnh và tạo liên kết hydrogen nên tan cực tốt trong nước (1 L nước hòa tan ~700 L khí NH₃!). Có 2 tính chất hóa học chính: 1) Tính BASE yếu (làm quỳ tím ẩm hóa xanh, phenolphthalein hóa hồng, tác dụng với acid tạo muối ammonium và kết tủa các hydroxide kim loại như Al(OH)₃↓); 2) Tính KHỬ (N⁻³ bị oxi hóa bởi O₂: cháy tạo N₂, nếu có xúc tác Pt ở 850°C thì tạo NO để sản xuất HNO₃).\n"
        "• Muối Ammonium (NH₄⁺): dễ tan, kém bền nhiệt và tác dụng với dung dịch kiềm giải phóng khí NH₃ mùi khai (dùng để nhận biết ion NH₄⁺).\n"
        "• Nitric acid (HNO₃): là một acid mạnh VÀ là một chất OXI HÓA RẤT MẠNH (oxi hóa hầu hết các kim loại kể cả Cu, Ag — trừ Au và Pt — lên số oxi hóa cao nhất và KHÔNG giải phóng khí H₂! Lưu ý: Al, Fe, Cr bị THỤ ĐỘNG HÓA trong HNO₃ đặc, nguội!).\n"
        "• Hiện tượng Phú dưỡng (Eutrophication): do dư thừa chất dinh dưỡng chứa Nitrogen (NO₃⁻, NH₄⁺) và Phosphorus (PO₄³⁻) trong nước ao hồ khiến tảo bùng phát xanh kín mặt nước, làm cạn kiệt O₂ hòa tan khiến cá chết hàng loạt.",
        [
            {
                "category": "I. Chuỗi chuyển hóa Công nghiệp từ N₂ → NH₃ → NO → NO₂ → HNO₃",
                "items": [
                    {"name": "1. Tổng hợp NH₃ & Đốt cháy NH₃ có xúc tác Pt (Quy trình Ostwald)", "formula": "N₂ + 3H₂ ⇄ (t°, p, Fe) ⇄ 2NH₃  ;  4NH₃ + 5O₂ ──(Pt, 850°C)──► 4NO + 6H₂O", "note": "Nếu đốt NH₃ trong O₂ không có xúc tác thì tạo N₂ + H₂O"},
                    {"name": "2. Từ NO tạo NO₂ và sản xuất Nitric acid (HNO₃)", "formula": "2NO (không màu) + O₂ → 2NO₂ (nâu đỏ)  ;  4NO₂ + O₂ + 2H₂O → 4HNO₃", "note": "Cũng là cơ chế tạo đạm tự nhiên khi có sấm chớp ('Lúa chiêm lấp ló đầu bờ...')"},
                ],
            },
            {
                "category": "II. Tính chất của NH₃, Muối Ammonium (NH₄⁺) & Nitric acid (HNO₃)",
                "items": [
                    {"name": "NH₃ kết tủa Al³⁺, Fe³⁺ & Nhận biết NH₄⁺ bằng Kiềm", "formula": "AlCl₃ + 3NH₃ + 3H₂O → Al(OH)₃↓(keo trắng, không tan trong NH₃ dư) + 3NH₄Cl  ;  NH₄⁺ + OH⁻ ──(t°)──► NH₃↑(mùi khai, làm xanh quỳ ẩm) + H₂O", "note": ""},
                    {"name": "HNO₃ tác dụng với Kim loại (trừ Au, Pt; Al, Fe, Cr thụ động trong HNO₃ đặc nguội)", "formula": "Cu + 4HNO₃(đặc) → Cu(NO₃)₂ + 2NO₂↑(nâu đỏ) + 2H₂O  ;  3Cu + 8HNO₃(loãng) → 3Cu(NO₃)₂ + 2NO↑ + 4H₂O", "note": "Số mol HNO₃ phản ứng = 2·n_NO₂ + 4·n_NO + 10·n_N₂O + 12·n_N₂ + 10·n_NH₄NO₃"},
                ],
            },
        ],
        "Giải thích câu ca dao của ông cha ta: 'Lúa chiêm lấp ló đầu bờ / Hễ nghe tiếng sấm phất cờ mà lên' bằng chuỗi phương trình hóa học.",
        "Khi có sấm sét (tia lửa điện nhiệt độ ~3000°C), khí N₂ và O₂ trong không khí kết hợp tạo thành khí NO: N₂ + O₂ ──(tia lửa điện)──► 2NO. Ngay lập tức NO kết hợp với O₂ không khí tạo NO₂ màu nâu đỏ: 2NO + O₂ → 2NO₂. Sau đó NO₂ hòa tan vào nước mưa cùng với O₂ tạo thành Nitric acid: 4NO₂ + O₂ + 2H₂O → 4HNO₃. Nước mưa mang theo ion nitrate (NO₃⁻) rơi xuống đất cung cấp nguồn phân đạm tự nhiên giúp cây lúa tốt tươi nhanh chóng.",
        "Kim loại nào dưới đây KHÔNG tác dụng được với dung dịch Nitric acid (HNO₃) ĐẶC, NGUỘI do bị thụ động hóa?",
        [
            "Copper (Cu) và Silver (Ag)",
            "Zinc (Zn) và Magnesium (Mg)",
            "Aluminium (Al), Iron (Fe) và Chromium (Cr)",
            "Calcium (Ca) và Sodium (Na)",
        ],
        2,
        "Sử dụng khí N₂ lỏng (−196°C) để bảo quản mẫu y sinh và bơm vào gói bim bim chống oxi hóa; vận chuyển HNO₃ đặc nguội trong bồn bằng nhôm hoặc thép; kiểm soát nước thải tránh phú dưỡng.",
        "Hòa tan hoàn toàn m gam bột Copper (Cu, M = 64) vào dung dịch HNO₃ dư thì thu được 7,437 lít hỗn hợp khí X (ở đkc 25°C, 1 bar) gồm hai khí NO (M = 30) và NO₂ (M = 46) có tỉ khối đối với H₂ bằng 19. Hãy tính số mol mỗi khí trong X và giá trị của m.",
        "Tổng số mol hỗn hợp khí X là: n_X = 7,437 / 24,79 = 0,3 (mol). Khối lượng mol trung bình của X là: M̄_X = 19 × 2 = 38 (g/mol). Gọi số mol NO và NO₂ lần lượt là a và b (mol). Ta có hệ: { a + b = 0,3 ; 30a + 46b = 38 · 0,3 = 11,4 } ⇒ a = 0,15 (mol NO) và b = 0,15 (mol NO₂). Bảo toàn electron: 2 · n_Cu = 3 · n_NO + 1 · n_NO₂ = 3·0,15 + 1·0,15 = 0,60 (mol) ⇒ n_Cu = 0,30 (mol). Vậy khối lượng đồng đã phản ứng là: m = 0,30 × 64 = 19,2 (gam).",
    ),
    C(
        11,
        "sulfuric-acid",
        "Sulfur (S), Sulfur Dioxide (SO₂ – Mưa Acid) & Sulfuric Acid (H₂SO₄ loãng vs H₂SO₄ đặc) – Muối Sulfate",
        "🧴",
        "Nắm vững tính chất của S, SO₂ (chất gây mưa acid), sự khác biệt cốt lõi giữa H₂SO₄ loãng và H₂SO₄ đặc (tính oxi hóa mạnh & tính háo nước) và nhận biết ion SO₄²⁻.",
        "Hóa chất số 1 của nền công nghiệp thế giới",
        "Sản lượng Sulfuric acid (H₂SO₄) của một quốc gia được xem là thước đo trình độ phát triển công nghiệp hóa chất của quốc gia đó (dùng sản xuất phân bón, chất tẩy rửa, ắc-quy, luyện kim, chế biến dầu mỏ).",
        "Sulfur (₁₆S: [Ne]3s²3p⁴) thuộc chu kỳ 3, nhóm VIA, có các số oxi hóa phổ biến là −2 (H₂S), 0 (S), +4 (SO₂, H₂SO₃) và +6 (SO₃, H₂SO₄, muối sulfate SO₄²⁻).",
        "• Đơn chất Sulfur (S - chất rắn màu vàng, không tan trong nước): vừa có tính oxi hóa (tác dụng với H₂ và kim loại; đặc biệt S phản ứng với thủy ngân Hg ngay ở nhiệt độ thường nên dùng bột S để thu gom thủy ngân rơi vãi khi vỡ nhiệt kế!), vừa có tính khử (cháy trong O₂ tạo SO₂).\n"
        "• Sulfur dioxide (SO₂ - khí không màu, mùi hắc, độc): là một Acidic oxide, vừa có tính khử (làm mất màu dung dịch nước Bromine và thuốc tím KMnO₄: SO₂ + Br₂ + 2H₂O → 2HBr + H₂SO₄), vừa có tính oxi hóa (SO₂ + 2H₂S → 3S↓ + 2H₂O). Khí SO₂ và NOₓ thải ra từ đốt than đá, dầu mỏ là thủ phạm chính gây ra MƯA ACID (pH < 5,6)!\n"
        "• Sulfuric acid (H₂SO₄): điều chế trong công nghiệp bằng phương pháp tiếp xúc qua 3 giai đoạn (FeS₂/S → SO₂ → SO₃ → Oleum H₂SO₄·nSO₃ → H₂SO₄).\n"
        "  + H₂SO₄ LOÃNG: thể hiện tính chất của một acid mạnh điển hình (do H⁺ gây ra: tác dụng kim loại trước H tạo muối hóa trị thấp + H₂↑).\n"
        "  + H₂SO₄ ĐẶC: có TÍNH OXI HÓA RẤT MẠNH (do S⁺⁶ gây ra: oxi hóa hầu hết kim loại kể cả Cu, Ag lên hóa trị cao nhất tạo muối + SO₂/S/H₂S + H₂O, KHÔNG tạo H₂; Al, Fe, Cr bị thụ động hóa trong H₂SO₄ đặc, nguội!) và có TÍNH HÁO NƯỚC mãnh liệt (than hóa đường saccharose C₁₂H₂₂O₁₁ thành cột than đen xốp C).",
        [
            {
                "category": "I. Ba giai đoạn sản xuất H₂SO₄ (Phương pháp Tiếp xúc) & Công thức Oleum",
                "items": [
                    {"name": "Chuỗi 3 giai đoạn điều chế H₂SO₄ công nghiệp", "formula": "(1) S + O₂ → SO₂ (hoặc 4FeS₂ + 11O₂ → 2Fe₂O₃ + 8SO₂) ; (2) 2SO₂ + O₂ ⇄ (V₂O₅, 450°C) ⇄ 2SO₃ ; (3) H₂SO₄(đặc) + nSO₃ → H₂SO₄·nSO₃ (Oleum)", "note": "Hấp thụ SO₃ bằng H₂SO₄ 98% tạo Oleum rồi mới pha loãng với nước"},
                    {"name": "Phản ứng của H₂SO₄ đặc làm than hóa đường (Tính háo nước + oxi hóa)", "formula": "C₁₂H₂₂O₁₁ ──(H₂SO₄ đặc)──► 12C + 11H₂O  ;  C + 2H₂SO₄(đặc) → CO₂↑ + 2SO₂↑ + 2H₂O", "note": "Cột than đen sủi bọt khí đẩy trào lên khỏi cốc"},
                ],
            },
            {
                "category": "II. So sánh Phản ứng của Iron (Fe) với H₂SO₄ loãng vs H₂SO₄ đặc, nóng",
                "items": [
                    {"name": "Fe + H₂SO₄ LOÃNG (Tạo muối Iron(II) và khí H₂)", "formula": "Fe + H₂SO₄(loãng) → FeSO₄ + H₂↑", "note": "Cu, Ag không phản ứng với H₂SO₄ loãng"},
                    {"name": "Fe + H₂SO₄ ĐẶC, NÓNG dư (Tạo muối Iron(III) và khí SO₂)", "formula": "2Fe + 6H₂SO₄(đặc, nóng) → Fe₂(SO₄)₃ + 3SO₂↑ + 6H₂O", "note": "Số mol H₂SO₄ đặc phản ứng = 2·n_SO₂ + 4·n_S + 5·n_H₂S"},
                ],
            },
        ],
        "Nêu hiện tượng và viết các PTHH xảy ra khi nhỏ vài mL dung dịch H₂SO₄ đặc (98%) vào cốc đựng một ít đường kính trắng (Saccharose: C₁₂H₂₂O₁₁).",
        "Hiện tượng: Đường trắng chuyển dần sang màu vàng, nâu rồi hóa thành khối than màu ĐEN XỐP, đồng thời tỏa nhiều nhiệt và có khí thoát ra đẩy khối than đen phồng trào lên miệng cốc. Giải thích: H₂SO₄ đặc có tính háo nước rất mạnh lấy đi các nguyên tố H và O (theo tỉ lệ H₂O) của đường tạo thành than (C): C₁₂H₂₂O₁₁ ──(H₂SO₄ đặc)──► 12C + 11H₂O. Sau đó một phần C bị H₂SO₄ đặc nóng oxi hóa tiếp tạo khí CO₂ và SO₂ đẩy cột than xốp trào lên: C + 2H₂SO₄(đặc) → CO₂↑ + 2SO₂↑ + 2H₂O.",
        "Khi làm vỡ nhiệt kế thủy ngân trong phòng học, hóa chất nào sẵn có dưới đây được rắc ngay lên các giọt thủy ngân (Hg) rơi vãi để thu hồi chúng thành hợp chất rắn không bay hơi ngay ở nhiệt độ thường?",
        [
            "Muối ăn (NaCl)",
            "Bột lưu huỳnh (Sulfur - S: phản ứng Hg + S → HgS rắn ngay ở nhiệt độ thường)",
            "Cát mịn (SiO₂)",
            "Vôi bột (CaO)",
        ],
        1,
        "Quy tắc an toàn tuyệt đối khi pha loãng H₂SO₄ đặc (rót từ từ acid vào nước), xử lý sự cố vỡ nhiệt kế thủy ngân bằng bột lưu huỳnh và ứng dụng muối sulfate: thạch cao nung CaSO₄·H₂O bó bột y tế, Barium sulfate BaSO₄ làm thuốc cản quang chụp X-quang dạ dày.",
        "Hòa tan hoàn toàn 12,8 gam kim loại Copper (Cu, M = 64) vào dung dịch H₂SO₄ đặc, nóng, dư. Hãy viết PTHH, tính thể tích khí SO₂ (sản phẩm khử duy nhất, ở đkc 25°C, 1 bar) thoát ra và tính số mol H₂SO₄ đã tham gia phản ứng.",
        "PTHH: Cu + 2H₂SO₄(đặc, nóng) → CuSO₄ + SO₂↑ + 2H₂O. Số mol Cu là: n_Cu = 12,8 / 64 = 0,2 (mol). Theo PTHH: n_SO₂ = n_Cu = 0,2 (mol) và số mol H₂SO₄ đã tham gia phản ứng là: n_H₂SO₄ = 2 · n_Cu = 0,4 (mol) (trong đó 0,2 mol đóng vai trò chất oxi hóa tạo SO₂ và 0,2 mol đóng vai trò môi trường tạo muối CuSO₄). Thể tích khí SO₂ (đkc) là: V = 0,2 × 24,79 = 4,958 (lít).",
    ),
    C(
        11,
        "hydrocarbon-huu-co",
        "Đại cương Hóa học Hữu cơ (Đồng đẳng, Đồng phân, Phổ IR - MS) & Hệ thống Hydrocarbon (Alkane, Alkene, Alkadiene, Alkyne, Arene)",
        "🧬",
        "Làm chủ độ bất bão hòa k, đọc phổ hồng ngoại IR - phổ khối lượng MS, quy tắc thế Markovnikov / tách Zaitsev và tính chất của Alkane, Alkene, Alkyne (tráng kết tủa vàng với AgNO₃/NH₃), Benzene - Toluene.",
        "Thế giới hàng chục triệu hợp chất của Carbon",
        "Nhờ khả năng tạo liên kết đơn, đôi, ba và nối thành mạch thẳng, nhánh, vòng, nguyên tố Carbon tạo nên hàng chục triệu hợp chất hữu cơ. Phổ IR và MS hiện đại giúp xác định nhanh nhóm chức và khối lượng phân tử.",
        "Đồng đẳng là những hợp chất có thành phần phân tử hơn kém nhau một hay nhiều nhóm –CH₂– nhưng có cấu tạo và tính chất hóa học tương tự nhau. Đồng phân là những chất khác nhau nhưng có CÙNG công thức phân tử (đồng phân cấu tạo và đồng phân hình học cis–trans).",
        "• Độ bất bão hòa (tổng số liên kết π và số vòng) của hợp chất CₓHᵧO_zN_tCl_u: k = (2x + 2 + t − y − u) / 2.\n"
        "• Phổ khối lượng (MS): mảnh ion phân tử [M⁺] có giá trị m/z lớn nhất cho biết phân tử khối M của chất. Phổ hồng ngoại (IR): nhận diện nhóm chức qua số sóng hấp thụ đặc trưng (–OH alcohol: 3650–3200 cm⁻¹ tù rộng; C=O carbonyl: ~1740–1680 cm⁻¹ nhọn mạnh; –COOH: có cả C=O ~1700 cm⁻¹ và O–H rộng 3300–2500 cm⁻¹).\n"
        "• Hệ thống các dãy đồng đẳng Hydrocarbon:\n"
        "  1. Alkane (CₙH₂ₙ₊₂, n ≥ 1, k = 0): phản ứng thế halogen (ưu tiên thế H ở C bậc cao hơn), cracking, reforming.\n"
        "  2. Alkene (CₙH₂ₙ, n ≥ 2, k = 1, có 1 liên kết đôi C=C): phản ứng cộng H₂ (xt Ni/Pt/Pd), cộng Br₂, cộng HX/H₂O theo QUY TẮC MARKOVNIKOV (H cộng vào C bậc thấp hơn có nhiều H hơn, X/OH cộng vào C bậc cao hơn!), làm mất màu dung dịch thuốc tím KMnO₄ và phản ứng trùng hợp.\n"
        "  3. Alkyne (CₙH₂ₙ₋₂, n ≥ 2, k = 2, có 1 liên kết ba C≡C): cộng H₂ (xúc tác Ni ra alkane; xúc tác Lindlar Pd/PbCO₃ dừng lại ở alkene!), đặc biệt các Alk-1-yne (có liên kết ba ở đầu mạch R–C≡CH như Acetylene HC≡CH, Propyne CH₃–C≡CH) tác dụng với dung dịch AgNO₃/NH₃ tạo kết tủa màu VÀNG NHẠT!\n"
        "  4. Arene – Hydrocarbon thơm (CₙH₂ₙ₋₆, n ≥ 6, k = 4: Benzene C₆H₆, Toluene C₆H₅CH₃, Styrene C₆H₅–CH=CH₂): Toluene làm mất màu dung dịch KMnO₄ khi đun nóng (tạo C₆H₅COOK), còn Benzene không làm mất màu KMnO₄.",
        [
            {
                "category": "I. Độ bất bão hòa (k), Quy tắc Cộng Markovnikov & Tách Zaitsev",
                "items": [
                    {"name": "Công thức tính Độ bất bão hòa k = π + v (cho CₓHᵧO_zN_t)", "formula": "k = (2x + 2 + t − y) / 2", "note": "k = 0: chỉ có liên kết đơn mạch hở ; Mọi hydrocarbon luôn có số nguyên tử H (y) là SỐ CHẴN!"},
                    {"name": "Quy tắc Markovnikov (Cộng HX hoặc H–OH vào Alkene bất đối xứng)", "formula": "CH₃–CH=CH₂ + HBr → CH₃–CHBr–CH₃ (sản phẩm chính) + CH₃–CH₂–CH₂Br (sản phẩm phụ)", "note": "H ưu tiên cộng vào C nối đôi có nhiều H hơn (bậc thấp hơn)"},
                ],
            },
            {
                "category": "II. Phản ứng Nhận biết đặc trưng của Alkene, Alk-1-yne & Arene",
                "items": [
                    {"name": "Phản ứng của Alk-1-yne (R–C≡CH) với thuốc thử Tollens (AgNO₃ / NH₃)", "formula": "HC≡CH + 2AgNO₃ + 2NH₃ → Ag–C≡C–Ag↓(vàng nhạt) + 2NH₄NO₃ ; R–C≡CH + AgNO₃ + NH₃ → R–C≡C–Ag↓(vàng) + NH₄NO₃", "note": "Đây là phản ứng THẾ ion Ag⁺ vào H linh động của C≡CH (không phải phản ứng tráng bạc!)"},
                    {"name": "Oxi hóa không hoàn toàn bằng dd KMnO₄ (Phân biệt Alkene, Toluene, Benzene)", "formula": "Alkene (C₂H₄, styrene): mất màu KMnO₄ ngay ở t° thường ; Toluene (C₆H₅CH₃): mất màu KMnO₄ khi ĐUN NÓNG ; Benzene (C₆H₆): không phản ứng", "note": "3CH₂=CH₂ + 2KMnO₄ + 4H₂O → 3HO–CH₂–CH₂–OH (ethylene glycol) + 2MnO₂↓ + 2KOH"},
                ],
            },
        ],
        "Trình bày phương pháp hóa học để phân biệt 3 chất khí không màu đựng trong 3 bình riêng biệt: Ethane (C₂H₆), Ethylene (CH₂=CH₂) và Acetylene (CH≡CH).",
        "Bước 1: Dẫn từng khí qua bình đựng dung dịch AgNO₃ trong NH₃ dư: khí nào tạo kết tủa màu VÀNG NHẠT (AgC≡CAg↓) là Acetylene (C₂H₂). Bước 2: Dẫn hai khí còn lại qua dung dịch nước Bromine (Br₂ màu nâu đỏ): khí nào làm mất màu nâu đỏ của dung dịch Br₂ là Ethylene (C₂H₄); khí còn lại không có hiện tượng là Ethane (C₂H₆).",
        "Hợp chất nào dưới đây có đồng phân hình học (cis – trans)? (Điều kiện có đồng phân hình học: phân tử có liên kết đôi C=C và ở MỖI nguyên tử C của liên kết đôi phải liên kết với hai nguyên tử/nhóm nguyên tử khác nhau: abC=Ccd với a ≠ b và c ≠ d)",
        [
            "Propene (CH₂=CH–CH₃)",
            "But-1-ene (CH₂=CH–CH₂–CH₃)",
            "But-2-ene (CH₃–CH=CH–CH₃)",
            "2-methylpropene (CH₂=C(CH₃)₂)",
        ],
        2,
        "Sản xuất xăng chỉ số octane cao (reforming), tổng hợp nhựa PE, PP, PS, cao su Buna, dung môi hữu cơ và thuốc bảo vệ thực vật, dược phẩm.",
        "Cho 6,1975 lít (ở đkc 25°C, 1 bar) hỗn hợp khí X gồm Propane (C₃H₈), Propene (CH₂=CH–CH₃) và Propyne (CH≡C–CH₃) lội từ từ qua bình thứ nhất đựng dung dịch AgNO₃/NH₃ dư thì thu được 14,7 gam kết tủa màu vàng. Khí thoát ra khỏi bình thứ nhất được dẫn tiếp qua bình thứ hai đựng dung dịch Br₂ dư thì thấy có 16 gam Br₂ đã phản ứng (biết Ag = 108, Br = 80). Hãy tính số mol của mỗi chất trong hỗn hợp X.",
        "Tổng số mol hỗn hợp X là: n_X = 6,1975 / 24,79 = 0,25 (mol). Tại bình 1, chỉ có Propyne (CH≡C–CH₃, có liên kết ba đầu mạch) phản ứng tạo kết tủa vàng CAg≡C–CH₃ (M = 147 g/mol): CH≡C–CH₃ + AgNO₃ + NH₃ → CAg≡C–CH₃↓ + NH₄NO₃ ⇒ n_Propyne = n_kết_tủa = 14,7 / 147 = 0,10 (mol). Tại bình 2, chỉ có Propene phản ứng cộng với Br₂ theo tỉ lệ 1:1 (M_Br₂ = 160): n_Propene = n_Br₂ = 16 / 160 = 0,10 (mol). Suy ra số mol Propane còn lại là: n_Propane = 0,25 − (0,10 + 0,10) = 0,05 (mol).",
    ),
    C(
        11,
        "dan-xuat-alcohol-carbonyl-acid",
        "Dẫn xuất Halogen, Alcohol – Phenol, Hợp chất Carbonyl (Aldehyde – Ketone) & Carboxylic Acid",
        "🧪",
        "Làm chủ tính chất của Alcohol đa chức (hòa tan Cu(OH)₂), Phenol (tác dụng NaOH và Br₂ tạo kết tủa trắng), Aldehyde (phản ứng tráng bạc & Cu(OH)₂/OH⁻, Iodoform) và Carboxylic acid.",
        "Hệ thống các nhóm chức hữu cơ chứa Oxygen",
        "Khi thay thế nguyên tử H của hydrocarbon bằng các nhóm chức như –X (halogen), –OH (alcohol, phenol), –CHO (aldehyde), –CO– (ketone) hay –COOH (carboxylic acid), ta thu được các họ hợp chất hữu cơ có tính chất hóa học vô cùng đặc sắc.",
        "Nhóm chức là nguyên tử hoặc nhóm nguyên tử gây ra những tính chất hóa học đặc trưng của hợp chất hữu cơ.",
        "• Dẫn xuất Halogen (R–X): Phản ứng thủy phân thế nguyên tử halogen bằng nhóm –OH khi đun nóng với dung dịch kiềm (R–Cl + NaOH ──(t°)──► R–OH + NaCl) và phản ứng tách HX (trong KOH/C₂H₅OH đun nóng tạo Alkene theo quy tắc Zaitsev).\n"
        "• Alcohol (R–OH, nhóm –OH gắn vào nguyên tử C no): tác dụng với Na; oxi hóa alcohol bậc I bằng CuO nung nóng tạo Aldehyde (RCH₂OH + CuO → RCHO + Cu + H₂O), alcohol bậc II tạo Ketone. Đặc biệt: Các Polyalcohol có ít nhất 2 nhóm –OH đính vào các C KỀ NHAU (như Ethylene glycol C₂H₄(OH)₂, Glycerol C₃H₅(OH)₃) hòa tan được Cu(OH)₂ ở nhiệt độ thường tạo dung dịch phức đồng màu XANH LAM THẪM!\n"
        "• Phenol (C₆H₅–OH, nhóm –OH đính trực tiếp vào vòng benzene): có tính acid yếu (mạnh hơn H₂O và alcohol nhưng yếu hơn H₂CO₃; không làm đổi màu quỳ tím), tác dụng được với cả Na VÀ dung dịch NaOH (C₆H₅OH + NaOH → C₆H₅ONa + H₂O — khác hẳn alcohol không tác dụng với NaOH!), và tác dụng với nước Bromine tạo kết tủa TRẮNG 2,4,6-tribromophenol.\n"
        "• Hợp chất Carbonyl (Aldehyde R–CHO và Ketone R–CO–R'): Cộng H₂ tạo alcohol bậc I / bậc II. Riêng Aldehyde (và HCOOH, HCOOR, Glucose) có phản ứng TRÁNG BẠC với thuốc thử Tollens [Ag(NH₃)₂]OH đun nóng tạo lớp bạc sáng bóng Ag↓ và tác dụng với Cu(OH)₂/NaOH đun nóng tạo kết tủa ĐỎ GẠCH Cu₂O↓. Các hợp chất chứa cụm CH₃–C=O (như CH₃CHO, acetone CH₃COCH₃) tác dụng với I₂/NaOH tạo kết tủa màu VÀNG CHI₃↓ (phản ứng Iodoform).\n"
        "• Carboxylic acid (R–COOH): tính acid đầy đủ và phản ứng ester hóa.",
        [
            {
                "category": "I. So sánh Alcohol (R–OH), Polyalcohol (Glycerol) & Phenol (C₆H₅OH)",
                "items": [
                    {"name": "Phân biệt Alcohol và Phenol bằng dd NaOH và dd Br₂", "formula": "Alcohol (C₂H₅OH): chỉ tác dụng Na (không tác dụng NaOH, Br₂) ; Phenol (C₆H₅OH): tác dụng cả Na, NaOH và tạo kết tủa TRẮNG với dd Br₂", "note": "C₆H₅OH + 3Br₂ → C₆H₂Br₃OH↓(trắng) + 3HBr"},
                    {"name": "Nhận biết Polyalcohol có ≥ 2 nhóm –OH kề nhau (Glycerol, Ethylene glycol)", "formula": "2C₃H₅(OH)₃ + Cu(OH)₂ → [C₃H₅(OH)₂O]₂Cu (dung dịch phức màu XANH LAM THẪM) + 2H₂O", "note": "Alcohol đơn chức (C₂H₅OH) hoặc 2 nhóm –OH cách xa (HO–CH₂–CH₂–CH₂–OH) không hòa tan Cu(OH)₂!"},
                ],
            },
            {
                "category": "II. Phản ứng Đặc trưng của Aldehyde (R–CHO) & Carboxylic Acid (R–COOH)",
                "items": [
                    {"name": "Phản ứng Tráng bạc (với thuốc thử Tollens: AgNO₃/NH₃, t°)", "formula": "R–CHO + 2[Ag(NH₃)₂]OH ──(t°)──► R–COONH₄ + 2Ag↓ + 3NH₃ + H₂O  (Tỉ lệ: 1 nhóm –CHO → 2 Ag)", "note": "ĐẶC BIỆT: Formaldehyde HCHO (và HCOOH) tráng bạc tạo 4 Ag↓ (1 mol HCHO → 4 mol Ag)!"},
                    {"name": "Phản ứng với Cu(OH)₂/OH⁻ đun nóng & Phản ứng Iodoform (CH₃–CO–)", "formula": "RCHO + 2Cu(OH)₂ + NaOH ──(t°)──► RCOONa + Cu₂O↓(đỏ gạch) + 3H₂O  ;  CH₃COR + 3I₂ + 4NaOH → CHI₃↓(vàng) + RCOONa + 3NaI + 3H₂O", "note": ""},
                ],
            },
        ],
        "Cho 4,4 gam Acetaldehyde (Ethanal: CH₃CHO, M = 44 g/mol) tác dụng hoàn toàn với lượng dư dung dịch AgNO₃ trong NH₃ đun nóng (thuốc thử Tollens). Viết PTHH và tính khối lượng bạc (Ag, M = 108) kết tủa thu được. Nếu thay 4,4 gam CH₃CHO bằng 3,0 gam Formaldehyde (Methanal: HCHO, M = 30 g/mol) thì thu được bao nhiêu gam Ag?",
        "Với CH₃CHO: n_CH₃CHO = 4,4 / 44 = 0,1 (mol). PTHH: CH₃CHO + 2[Ag(NH₃)₂]OH ──(t°)──► CH₃COONH₄ + 2Ag↓ + 3NH₃ + H₂O ⇒ n_Ag = 2 · 0,1 = 0,2 (mol) ⇒ m_Ag = 0,2 × 108 = 21,6 (gam). Với 3,0 gam HCHO (n = 3,0 / 30 = 0,1 mol): vì 1 phân tử HCHO có 2 nguyên tử H gắn vào C=O nên tráng bạc tạo 4 Ag (HCHO + 4[Ag(NH₃)₂]OH → (NH₄)₂CO₃ + 4Ag↓ + 6NH₃ + 2H₂O) ⇒ n_Ag = 4 · 0,1 = 0,4 (mol) ⇒ m_Ag = 0,4 × 108 = 43,2 (gam).",
        "Để phân biệt 3 chất lỏng: Ethanol (C₂H₅OH), Glycerol (C₃H₅(OH)₃) và Acetaldehyde (CH₃CHO), người ta có thể chỉ dùng một thuốc thử duy nhất là:",
        [
            "Kim loại Sodium (Na)",
            "Cu(OH)₂ trong môi trường kiềm (ở nhiệt độ thường và khi đun nóng)",
            "Giấy quỳ tím",
            "Dung dịch NaCl",
        ],
        1,
        "Ứng dụng phản ứng tráng gương sản xuất ruột phích nước và gương soi, dùng Glycerol giữ ẩm trong mỹ phẩm, Phenol sản xuất nhựa phenol-formaldehyde và Acetone làm dung môi.",
        "Chia 27,6 gam hỗn hợp X gồm Ethanol (C₂H₅OH, M = 46) và Phenol (C₆H₅OH, M = 94) thành hai phần bằng nhau. Phần 1 cho tác dụng với lượng dư dung dịch nước Bromine (Br₂) thì thu được 33,1 gam kết tủa trắng 2,4,6-tribromophenol (C₆H₂Br₃OH, M = 331 g/mol). Phần 2 cho tác dụng hết với kim loại Sodium (Na) dư. Hãy tính khối lượng mỗi chất trong hỗn hợp X ban đầu và thể tích khí H₂ (ở đkc) thoát ra ở Phần 2.",
        "Mỗi phần có khối lượng là: 27,6 / 2 = 13,8 (gam). Ở Phần 1, chỉ có Phenol phản ứng với dd Br₂ tạo kết tủa trắng: C₆H₅OH + 3Br₂ → C₆H₂Br₃OH↓ + 3HBr. Số mol kết tủa là: n = 33,1 / 331 = 0,10 (mol) ⇒ trong mỗi phần có n_Phenol = 0,10 (mol) (khối lượng Phenol trong 1 phần là 0,10 × 94 = 9,4 g). Suy ra trong 1 phần có m_Ethanol = 13,8 − 9,4 = 4,4 (g) (Lẻ? Nếu hỗn hợp X ban đầu nặng 28,0 g thì mỗi phần 14,0 g ⇒ m_Ethanol = 14,0 − 9,4 = 4,6 g = 0,10 mol; với 27,6 g ban đầu thì trong cả hỗn hợp X có: m_Phenol = 2 × 9,4 = 18,8 g và m_Ethanol = 27,6 − 18,8 = 8,8 g). Ở Phần 2, cả Phenol và Ethanol đều tác dụng với Na theo tỉ lệ 1 nhóm –OH : 1/2 H₂: n_H₂ = (1/2) · (n_Phenol + n_Ethanol) = 0,5 · (0,10 + 4,4/46) ≈ 0,0978 (mol) ⇒ V_H₂ ≈ 2,425 (lít).",
    ),

    # =========================================================
    # HÓA HỌC LỚP 12 (7 BÀI)
    # =========================================================
    C(
        12,
        "este-lipit",
        "Ester – Lipid (Chất béo), Phản ứng Thủy phân – Xà phòng hóa & Chất giặt rửa",
        "🧴",
        "Làm chủ danh pháp Ester (RCOOR'), số đồng phân, phản ứng thủy phân trong môi trường acid/kiềm (kể cả ester của phenol), bài toán chất béo - xà phòng hóa và cơ chế giặt rửa.",
        "Hương thơm trái cây và công nghiệp sản xuất xà phòng",
        "Isoamyl acetate mang hương chuối chín, ethyl butyrate mang hương dứa, benzyl acetate mang hương hoa nhài — tất cả đều là các hợp chất Ester. Trong khi đó, dầu thực vật và mỡ động vật là các Triester của Glycerol với các Acid béo.",
        "Khi thay nhóm –OH ở nhóm carboxyl (–COOH) của carboxylic acid bằng nhóm –OR' (với R' là gốc hydrocarbon), ta được hợp chất Ester có công thức chung R–COO–R'. Lipid (mà đại diện quan trọng nhất là Chất béo / Triglyceride) là triester của Glycerol C₃H₅(OH)₃ với các acid béo (acid đơn chức có mạch carbon dài, không phân nhánh).",
        "• Danh pháp Ester R–COO–R': Tên gốc R' + Tên gốc acid RCOO– (đổi đuôi '-ic' thành '-ate'). Ví dụ: HCOOCH₃ (Methyl formate / methanoate); CH₃COOC₂H₅ (Ethyl acetate / ethanoate); CH₃COOCH=CH₂ (Vinyl acetate); CH₂=C(CH₃)COOCH₃ (Methyl methacrylate - dùng điều chế thủy tinh hữu cơ Plexiglas).\n"
        "• Số đồng phân Ester đơn chức no CₙH₂ₙO₂ (n ≥ 2): N_ester = 2^(n−2) (với 2 ≤ n ≤ 4: C₂H₄O₂ có 1; C₃H₆O₂ có 2; C₄H₈O₂ có 4 đồng phân ester).\n"
        "• Phản ứng Thủy phân Ester:\n"
        "  1. Thủy phân trong môi trường ACID (H⁺, t°): là phản ứng THUẬN NGHỊCH (trừ khi tạo aldehyde/ketone).\n"
        "  2. Thủy phân trong môi trường KIỀM (NaOH/KOH, t° - Phản ứng Xà phòng hóa): là phản ứng MỘT CHIỀU!\n"
        "  + Chú ý 2 trường hợp Ester đặc biệt: Ester dạng RCOOCH=CH–R' thủy phân tạo Muối + Aldehyde (R'CH₂CHO); Ester của Phenol (R–COO–C₆H₄–R') tác dụng với NaOH theo tỉ lệ 1 : 2 tạo ra HAI MUỐI và NƯỚC (RCOOC₆H₅ + 2NaOH → RCOONa + C₆H₅ONa + H₂O)!\n"
        "• Các Acid béo và Chất béo cần nhớ thuộc lòng phân tử khối:\n"
        "  + Palmitic acid: C₁₅H₃₁COOH (M = 256, no) → Tripalmitin: (C₁₅H₃₁COO)₃C₃H₅ (M = 806).\n"
        "  + Stearic acid: C₁₇H₃₅COOH (M = 284, no) → Tristearin: (C₁₇H₃₅COO)₃C₃H₅ (M = 890).\n"
        "  + Oleic acid: C₁₇H₃₃COOH (M = 282, có 1 nối đôi C=C cis, cấu hình dạng chữ U gấp khúc) → Triolein: (C₁₇H₃₃COO)₃C₃H₅ (M = 884, chất béo lỏng).\n"
        "  + Linoleic acid: C₁₇H₃₁COOH (M = 280, có 2 nối đôi C=C; thuộc nhóm acid béo thiết yếu Omega-6).\n"
        "• Cấu tạo phân tử Xà phòng (RCOONa) và Chất giặt rửa tổng hợp (R–SO₃Na / R–OSO₃Na): gồm ĐẦU ƯA NƯỚC (nhóm phân cực –COO⁻Na⁺ hoặc –SO₃⁻Na⁺) và ĐUÔI KỴ NƯỚC / ƯA DẦU MỠ (gốc hydrocarbon dài R–).",
        [
            {
                "category": "I. Phản ứng Thủy phân Ester thông thường & Các Ester đặc biệt",
                "items": [
                    {"name": "Thủy phân trong Acid (Thuận nghịch) vs trong Kiềm (1 chiều)", "formula": "RCOOR' + H₂O ⇄ (H⁺, t°) ⇄ RCOOH + R'OH  ;  RCOOR' + NaOH ──(t°)──► RCOONa + R'OH", "note": "Nếu M_R' < 23 (tức R' là –CH₃ có M=15) thì m_muối RCOONa > m_ester!"},
                    {"name": "Ester của Vinyl (RCOOCH=CH₂) & Ester của Phenol (RCOOC₆H₅)", "formula": "RCOOCH=CH₂ + NaOH ──(t°)──► RCOONa + CH₃CHO  ;  RCOOC₆H₅ + 2NaOH ──(t°)──► RCOONa + C₆H₅ONa + H₂O", "note": "Dấu hiệu nhận biết Ester của Phenol: n_NaOH / n_ester = 2 và thu được 2 muối + H₂O!"},
                ],
            },
            {
                "category": "II. Công thức tính toán nhanh Bài toán Chất béo (Triglyceride)",
                "items": [
                    {"name": "Hydrogen hóa chất béo lỏng (Triolein → Tristearin - Bơ thực vật)", "formula": "(C₁₇H₃₃COO)₃C₃H₅ (lỏng, M=884) + 3H₂ ──(Ni, t°)──► (C₁₇H₃₅COO)₃C₃H₅ (rắn, M=890)", "note": "Số mol H₂ (hoặc Br₂) phản ứng = (k − 3) · n_chất_béo (vì 3 nhóm COO có 3 liên kết π không cộng H₂/Br₂)"},
                    {"name": "Xà phòng hóa Chất béo & Định luật Bảo toàn Khối lượng", "formula": "(RCOO)₃C₃H₅ + 3NaOH ──(t°)──► 3RCOONa (Xà phòng) + C₃H₅(OH)₃ (Glycerol, M=92)", "note": "Tỉ lệ vàng: n_NaOH = 3 · n_chất_béo = 3 · n_glycerol  và  m_chất_béo + 40·(3n_cb) = m_xà_phòng + 92·n_cb"},
                ],
            },
        ],
        "Xà phòng hóa hoàn toàn 177,6 gam hỗn hợp hai chất béo gồm Tristearin ((C₁₇H₃₅COO)₃C₃H₅, M = 890) và Triolein ((C₁₇H₃₃COO)₃C₃H₅, M = 884) bằng dung dịch NaOH vừa đủ thì thu được 18,4 gam Glycerol (C₃H₅(OH)₃, M = 92). Tính khối lượng muối (xà phòng nguyên chất) thu được.",
        "Số mol Glycerol là: n_glycerol = 18,4 / 92 = 0,2 (mol). Theo PTHH tổng quát: (RCOO)₃C₃H₅ + 3NaOH → 3RCOONa + C₃H₅(OH)₃, ta luôn có: n_NaOH = 3 · n_glycerol = 3 · 0,2 = 0,6 (mol) ⇒ m_NaOH = 0,6 × 40 = 24,0 (gam). Áp dụng định luật bảo toàn khối lượng: m_chất_béo + m_NaOH = m_muối + m_glycerol ⇒ m_muối = 177,6 + 24,0 − 18,4 = 183,2 (gam).",
        "Cho 0,1 mol Phenyl acetate (CH₃COOC₆H₅, M = 136 g/mol) tác dụng hoàn toàn với dung dịch chứa 0,25 mol NaOH đun nóng, cô cạn dung dịch sau phản ứng thì thu được bao nhiêu gam chất rắn khan (biết Na = 23, C = 12, H = 1, O = 16)?",
        ["8,2 gam", "19,8 gam", "21,8 gam", "15,6 gam"],
        2,
        "Sản xuất xà phòng, chất giặt rửa tổng hợp, nước hoa, hương liệu thực phẩm, bơ thực vật (margarin) và bổ sung acid béo Omega-3, Omega-6 tốt cho tim mạch.",
        "Giải thích cơ chế làm sạch vết dầu mỡ của xà phòng và giải thích vì sao KHÔNG NÊN dùng xà phòng để giặt quần áo trong nước cứng (nước chứa nhiều ion Ca²⁺ và Mg²⁺), trong khi bột giặt tổng hợp vẫn giặt tốt trong nước cứng?",
        "Phân tử muối xà phòng (RCOONa) gồm phần đuôi kỵ nước (gốc R– ưa dầu mỡ) và phần đầu ưa nước (–COO⁻Na⁺). Khi giặt, đuôi kỵ nước cắm sâu vào giọt dầu mỡ trên sợi vải, còn đầu ưa nước hướng ra ngoài phân tử nước, chia nhỏ giọt dầu mỡ thành các hạt nhũ tương (micelle) bị nước cuốn trôi. Trong nước cứng (chứa nhiều Ca²⁺, Mg²⁺), muối xà phòng tạo kết tủa bết dính không tan là Calcium/Magnesium stearate: 2C₁₇H₃₅COONa + Ca²⁺ → (C₁₇H₃₅COO)₂Ca↓ + 2Na⁺ làm tốn xà phòng và làm mục vải; còn muối sulfonate (R–SO₃Na) trong bột giặt tổng hợp không tạo kết tủa với Ca²⁺, Mg²⁺.",
    ),
    C(
        12,
        "carbohydrate",
        "Carbohydrate: Glucose – Fructose, Saccharose – Maltose & Tinh bột – Cellulose",
        "🍚",
        "Nắm vững cấu tạo mạch hở và mạch vòng của Glucose - Fructose, tính chất polyalcohol - aldehyde, phản ứng thủy phân và bài toán tráng bạc, lên men, sản xuất tơ - thuốc súng không khói.",
        "Nguồn năng lượng sống và vật liệu sinh học xanh",
        "Carbohydrate (còn gọi là glucid hay đường, công thức chung thường có dạng Cₙ(H₂O)ₘ) được chia thành 3 nhóm: Monosaccharide (không bị thủy phân: Glucose, Fructose), Disaccharide (thủy phân cho 2 phân tử monosaccharide: Saccharose, Maltose) và Polysaccharide (Tinh bột, Cellulose).",
        "Carbohydrate là những hợp chất hữu cơ tạp chức (chứa nhiều nhóm –OH alcohol và nhóm carbonyl –CHO hoặc –CO–), tồn tại chủ yếu ở dạng mạch vòng (α và β) cân bằng với một lượng nhỏ dạng mạch hở trong dung dịch.",
        "• Monosaccharide — Glucose và Fructose (đồng phân của nhau, cùng CTPT C₆H₁₂O₆, M = 180):\n"
        "  + Ở dạng mạch hở, Glucose là CH₂OH–[CHOH]₄–CHO (5 nhóm –OH kề nhau + 1 nhóm –CHO); Fructose là CH₂OH–[CHOH]₃–CO–CH₂OH (5 nhóm –OH + 1 nhóm ketone –CO–).\n"
        "  + Tính chất chung của cả Glucose và Fructose: Hòa tan Cu(OH)₂ ở t° thường tạo dung dịch xanh lam; cộng H₂ (xt Ni, t°) tạo Sorbitol C₆H₁₄O₆; ĐẶC BIỆT trong môi trường kiềm (NH₃ hoặc OH⁻), Fructose chuyển hóa thuận nghịch thành Glucose nên Fructose CŨNG có phản ứng tráng bạc (1 mol → 2 mol Ag↓) và tác dụng với Cu(OH)₂/OH⁻ đun nóng tạo kết tủa đỏ gạch Cu₂O↓!\n"
        "  + Phân biệt Glucose và Fructose: Dùng dung dịch NƯỚC BROMINE (Br₂): chỉ có Glucose làm mất màu dung dịch nước Br₂ (tạo gluconic acid), còn Fructose KHÔNG làm mất màu nước Br₂!\n"
        "• Disaccharide — Saccharose và Maltose (cùng CTPT C₁₂H₂₂O₁₁, M = 342):\n"
        "  + Saccharose (đường mía: 1 α-glucose + 1 β-fructose nối qua C₁–O–C₂): không còn nhóm –OH hemiacetal tự do nên KHÔNG mở vòng được ⇒ Saccharose chỉ hòa tan Cu(OH)₂ tạo dd xanh lam và bị thủy phân (C₁₂H₂₂O₁₁ + H₂O ──(H⁺, t°)──► Glucose + Fructose), hoàn toàn KHÔNG có phản ứng tráng bạc!\n"
        "  + Maltose (đường mạch nha: 2 đơn vị α-glucose): mở vòng được nên vừa hòa tan Cu(OH)₂, vừa có phản ứng tráng bạc (1 mol Maltose → 2 mol Ag) và thủy phân tạo 2 phân tử Glucose.\n"
        "• Polysaccharide — Tinh bột và Cellulose (cùng công thức (C₆H₁₀O₅)ₙ, M_mắt_xích = 162, nhưng KHÔNG phải đồng phân vì n khác nhau!): Tinh bột (gồm amylose mạch thẳng xoắn và amylopectin mạch nhánh; gặp I₂ hóa xanh tím); Cellulose (mạch thẳng từ các gốc β-glucose, mỗi mắt xích có 3 nhóm –OH nên viết là [C₆H₇O₂(OH)₃]ₙ, tác dụng với HNO₃ đặc/H₂SO₄ đặc tạo Cellulose trinitrate làm thuốc súng không khói!).",
        [
            {
                "category": "I. Bảng tổng hợp Tính chất Hóa học của 6 chất Carbohydrate",
                "items": [
                    {"name": "1. Hòa tan Cu(OH)₂ ở t° thường tạo dd Xanh lam", "formula": "Có ở: Glucose, Fructose, Saccharose, Maltose (Tinh bột và Cellulose KHÔNG có)", "note": "Do có nhiều nhóm –OH liền kề"},
                    {"name": "2. Phản ứng Tráng bạc (AgNO₃/NH₃, t°) & Cu(OH)₂/OH⁻ (t° tạo Cu₂O↓)", "formula": "Có ở: Glucose, Fructose, Maltose (1 mol → 2 mol Ag↓) ; Saccharose, Tinh bột, Cellulose KHÔNG tráng bạc", "note": "Chú ý: Sau khi THỦY PHÂN Saccharose (tạo 1 Glu + 1 Fruc) thì tráng bạc thu được 4 mol Ag / 1 mol Saccharose!"},
                    {"name": "3. Làm mất màu dung dịch Nước Bromine (Br₂)", "formula": "Chỉ có ở: Glucose (và Maltose) ; Fructose và Saccharose KHÔNG làm mất màu nước Br₂!", "note": "Dùng nước Br₂ để phân biệt Glucose và Fructose"},
                ],
            },
            {
                "category": "II. Các Sơ đồ Định lượng Vàng trong Bài toán Carbohydrate",
                "items": [
                    {"name": "Thủy phân Saccharose (M=342) rồi Tráng bạc", "formula": "1 mol Saccharose ──(+H₂O)──► 1 mol Glucose + 1 mol Fructose ──(+AgNO₃/NH₃)──► 4 mol Ag↓", "note": ""},
                    {"name": "Thủy phân Tinh bột / Cellulose (M=162) → Glucose (M=180) → Ethanol (M=46)", "formula": "(C₆H₁₀O₅)ₙ (162) → C₆H₁₂O₆ (180) → 2C₂H₅OH (2×46) + 2CO₂↑ (2×44)", "note": "Nếu dẫn CO₂ vào Ca(OH)₂ dư: n_CaCO₃ = n_CO₂ = 2 · n_glucose(pư)"},
                    {"name": "Sản xuất Thuốc súng không khói (Cellulose trinitrate, M = 297)", "formula": "[C₆H₇O₂(OH)₃]ₙ (162) + 3n HNO₃ ──(H₂SO₄ đặc, t°)──► [C₆H₇O₂(ONO₂)₃]ₙ (297) + 3n H₂O", "note": "Cứ 162 kg Cellulose + 3×63 = 189 kg HNO₃ tạo ra 297 kg Cellulose trinitrate"},
                ],
            },
        ],
        "Thủy phân hoàn toàn 34,2 gam Saccharose (C₁₂H₂₂O₁₁, M = 342) trong môi trường acid, trung hòa acid rồi lấy toàn bộ dung dịch thu được đem thực hiện phản ứng tráng bạc với lượng dư dung dịch AgNO₃ trong NH₃ đun nóng. Tính khối lượng bạc (Ag, M = 108) kết tủa thu được.",
        "Số mol Saccharose là: n_sac = 34,2 / 342 = 0,1 (mol). Phản ứng thủy phân: C₁₂H₂₂O₁₁ + H₂O → C₆H₁₂O₆ (Glucose) + C₆H₁₂O₆ (Fructose). Cả Glucose (0,1 mol) và Fructose (0,1 mol) đều tham gia phản ứng tráng bạc trong môi trường NH₃ tạo ra 2Ag cho mỗi mol. Vậy tổng số mol Ag thu được là: n_Ag = 2 · n_glucose + 2 · n_fructose = 4 · n_sac = 4 · 0,1 = 0,4 (mol). Khối lượng Ag kết tủa là: m_Ag = 0,4 × 108 = 43,2 (gam).",
        "Cặp chất nào dưới đây đều KHÔNG tham gia phản ứng tráng bạc với thuốc thử Tollens (AgNO₃/NH₃), nhưng sản phẩm thủy phân của chúng lại tham gia phản ứng tráng bạc?",
        [
            "Glucose và Fructose",
            "Saccharose và Tinh bột (hoặc Cellulose)",
            "Saccharose và Maltose",
            "Fructose và Tinh bột",
        ],
        1,
        "Pha dịch truyền tĩnh mạch Glucose 5% cho bệnh nhân suy nhược, tráng ruột phích và gương bằng Glucose (an toàn, không độc như dùng formaldehyde), sản xuất tơ visco, tơ acetate và giấy từ Cellulose.",
        "Từ 16,2 tấn mùn cưa chứa 50% Cellulose (M_mắt_xích = 162) đem tác dụng với lượng dư dung dịch HNO₃ đặc (có H₂SO₄ đặc xúc tác, đun nóng) với hiệu suất phản ứng đạt 90%. Hãy tính khối lượng thuốc súng không khói Cellulose trinitrate ([C₆H₇O₂(ONO₂)₃]ₙ, M_mắt_xích = 297) thu được và thể tích dung dịch HNO₃ 63% (có khối lượng riêng D = 1,4 g/mL) đã phản ứng.",
        "Khối lượng Cellulose nguyên chất trong mùn cưa là: m_cell = 16,2 × 50% = 8,1 (tấn) = 8 100 (kg) ⇒ số kmol mắt xích là: n = 8100 / 162 = 50 (kmol). Với hiệu suất H = 90%, số kmol mắt xích thực tế đã phản ứng là: n_pư = 50 × 90% = 45 (kmol). Theo PTHH: [C₆H₇O₂(OH)₃]ₙ + 3n HNO₃ → [C₆H₇O₂(ONO₂)₃]ₙ + 3n H₂O. Khối lượng Cellulose trinitrate thu được là: m_sp = 45 × 297 = 13 365 (kg) = 13,365 (tấn). Số kmol HNO₃ đã phản ứng là: n_HNO₃ = 3 × 45 = 135 (kmol) ⇒ m_HNO₃ = 135 × 63 = 8 505 (kg). Khối lượng dung dịch HNO₃ 63% là: m_dd = 8505 / 0,63 = 13 500 (kg) ⇒ Thể tích dung dịch HNO₃ đã phản ứng là: V_dd = 13 500 / 1,4 ≈ 9 642,86 (lít).",
    ),
    C(
        12,
        "amin-amino-acid-protein",
        "Amine, Amino Acid, Peptide & Protein – Enzyme",
        "🧬",
        "Làm chủ lực base của các Amine, tính chất lưỡng tính và điểm đẳng điện của Amino acid (Gly, Ala, Val, Glu, Lys), liên kết Peptide và phản ứng màu Biuret.",
        "Những viên gạch kiến tạo nên sự sống",
        "Cơ thể con người được xây dựng và vận hành bởi hàng chục nghìn loại Protein khác nhau (cơ bắp, collagen, kháng thể, hormone insulin, hemoglobin và các chất xúc tác sinh học Enzyme), mà đơn vị cấu tạo cơ sở chính là các α-Amino acid.",
        "Amine là dẫn xuất thu được khi thay thế một hay nhiều nguyên tử H trong phân tử NH₃ bằng gốc hydrocarbon. Amino acid là hợp chất hữu cơ tạp chức trong phân tử chứa đồng thời nhóm amino (–NH₂, có tính base) và nhóm carboxyl (–COOH, có tính acid). Peptide và Protein là các chuỗi gồm nhiều gốc α-amino acid liên kết với nhau bằng liên kết peptide (–CO–NH–).",
        "• Amine (Bậc của amine = số nguyên tử H trong NH₃ bị thay thế bởi gốc R): Methylamine (CH₃NH₂), Ethylamine (C₂H₅NH₂), Dimethylamine ((CH₃)₂NH), Trimethylamine ((CH₃)₃N) là các chất KHÍ ở điều kiện thường, mùi khai tanh, tan nhiều trong nước và làm quỳ tím hóa xanh.\n"
        "  + So sánh lực Base của Amine: Gốc alkyl đẩy electron làm tăng lực base; gốc phenyl (C₆H₅–) hút electron làm giảm mạnh lực base ⇒ Lực base: (R)₂NH > R–NH₂ > NH₃ > C₆H₅NH₂ (Aniline). Lưu ý: Aniline (C₆H₅NH₂, M = 93, chất lỏng ít tan trong nước) có tính base rất yếu nên KHÔNG làm đổi màu quỳ tím và phenolphthalein, nhưng tác dụng với dung dịch nước Bromine tạo kết tủa TRẮNG 2,4,6-tribromoaniline!\n"
        "• Năm α-Amino acid tự nhiên bắt buộc phải thuộc lòng công thức và phân tử khối M:\n"
        "  1. Glycine (Gly): H₂N–CH₂–COOH (M = 75 ; 1 nhóm NH₂, 1 nhóm COOH ⇒ quỳ tím KHÔNG đổi màu).\n"
        "  2. Alanine (Ala): CH₃–CH(NH₂)–COOH (M = 89 ; quỳ tím không đổi màu).\n"
        "  3. Valine (Val): (CH₃)₂CH–CH(NH₂)–COOH (M = 117 ; quỳ tím không đổi màu).\n"
        "  4. Glutamic acid (Glu): HOOC–CH₂–CH₂–CH(NH₂)–COOH (M = 147 ; có 1 nhóm NH₂ và 2 nhóm COOH ⇒ làm quỳ tím hóa ĐỎ; muối monosodium glutamate là mì chính / bột ngọt!).\n"
        "  5. Lysine (Lys): H₂N–[CH₂]₄–CH(NH₂)–COOH (M = 146 ; có 2 nhóm NH₂ và 1 nhóm COOH ⇒ làm quỳ tím hóa XANH!).\n"
        "• Ở điều kiện thường, các amino acid tồn tại chủ yếu ở dạng ION LƯỠNG CỰC (H₃N⁺–CHR–COO⁻) nên đều là chất rắn kết tinh, dễ tan trong nước, có nhiệt độ nóng chảy cao và có khả năng dịch chuyển trong điện trường (hiện tượng điện di) tùy theo pH dung dịch.\n"
        "• Peptide & Protein: Một n-peptide (tạo bởi n gốc α-amino acid) có (n − 1) liên kết peptide –CO–NH–. Các peptide có từ 2 liên kết peptide trở lên (Tripeptide trở lên, nghĩa là từ 3 mắt xích trở lên — TRỪ Dipeptide chỉ có 1 liên kết peptide!) và Protein tác dụng với Cu(OH)₂/OH⁻ tạo phức màu TÍM ĐẶC TRƯNG (Phản ứng màu Biuret).",
        [
            {
                "category": "I. Bảng 5 α-Amino acid chuẩn & Tính chất Lưỡng tính (Tác dụng cả HCl và NaOH)",
                "items": [
                    {"name": "5 Amino acid: Gly (75), Ala (89), Val (117), Lys (146), Glu (147)", "formula": "Gly, Ala, Val (1 NH₂, 1 COOH): pH ≈ 6–7 (quỳ không đổi màu) ; Glu (1 NH₂, 2 COOH): quỳ → ĐỎ ; Lys (2 NH₂, 1 COOH): quỳ → XANH", "note": ""},
                    {"name": "Phản ứng của (H₂N)ₐR(COOH)_b với HCl và NaOH", "formula": "1 mol AA tác dụng tối đa với a mol HCl (vào nhóm –NH₂, M tăng 36,5a) và b mol NaOH (vào nhóm –COOH, M tăng 22b)", "note": "Bài toán nối tiếp: Cho AA + HCl dư rồi + NaOH dư thì coi như cả AA và HCl ban đầu cùng tác dụng với NaOH!"},
                ],
            },
            {
                "category": "II. Công thức tính Phân tử khối & Thủy phân Peptide (Xₙ gồm n mắt xích α-AA)",
                "items": [
                    {"name": "Số liên kết peptide & Phân tử khối của n-Peptide", "formula": "Số liên kết peptide = n − 1  ;  M_(n-peptide) = ΣM_(các_amino_acid) − 18 · (n − 1)", "note": "Do tách ra (n − 1) phân tử H₂O khi ngưng tụ"},
                    {"name": "Thủy phân hoàn toàn 1 mol n-Peptide (giả sử các AA chỉ có 1 nhóm COOH, 1 NH₂)", "formula": "Trong nước (H⁺): Xₙ + (n − 1)H₂O → n AA ; Trong kiềm: Xₙ + n NaOH → n Muối + 1 H₂O", "note": "Chú ý: Nếu trong peptide có thêm k gốc Glu thì cần thêm k mol NaOH và sinh ra (1 + k) mol H₂O!"},
                    {"name": "Phản ứng màu Biuret (với Cu(OH)₂ / OH⁻ tạo màu Tím)", "formula": "Dipeptide (2 AA, chỉ có 1 liên kết –CO–NH–): KHÔNG có phản ứng màu Biuret ; Từ Tripeptide (≥ 3 AA) và Protein: CÓ màu tím Biuret!", "note": ""},
                ],
            },
        ],
        "Tính phân tử khối của tripeptide Gly–Ala–Val và tính khối lượng muối thu được khi thủy phân hoàn toàn 0,1 mol tripeptide Gly–Ala–Val trong dung dịch chứa 0,3 mol NaOH vừa đủ (biết Gly = 75, Ala = 89, Val = 117).",
        "Tripeptide Gly–Ala–Val gồm n = 3 mắt xích (có 3 − 1 = 2 liên kết peptide), nên có phân tử khối là: M = 75 + 89 + 117 − 18 · 2 = 281 − 36 = 245 (g/mol). Khi thủy phân hoàn toàn 0,1 mol Gly–Ala–Val bằng 0,3 mol NaOH vừa đủ: Gly–Ala–Val + 3NaOH → Muối + H₂O (số mol H₂O sinh ra bằng số mol peptide = 0,1 mol). Theo định luật bảo toàn khối lượng: m_muối = m_peptide + m_NaOH − m_H₂O = 0,1·245 + 0,3·40 − 0,1·18 = 24,5 + 12,0 − 1,8 = 34,7 (gam).",
        "Sắp xếp các chất sau theo thứ tự LỰC BASE TĂNG DẦN trong dung dịch nước: (1) Ammonia (NH₃), (2) Aniline (C₆H₅NH₂), (3) Ethylamine (C₂H₅NH₂), (4) Diethylamine ((C₂H₅)₂NH).",
        [
            "(1) < (2) < (3) < (4)",
            "(2) < (1) < (3) < (4)",
            "(4) < (3) < (1) < (2)",
            "(2) < (3) < (1) < (4)",
        ],
        1,
        "Ứng dụng Glutamic acid làm thuốc bổ thần kinh và sản xuất bột ngọt (MSG), giải thích hiện tượng nấu canh cua riêu cua nổi lên thành từng mảng (đông tụ protein bởi nhiệt độ và acid), và ứng dụng enzyme trong bột giặt sinh học, chế biến thực phẩm.",
        "Cho 0,15 mol Glutamic acid (HOOC–CH₂–CH₂–CH(NH₂)–COOH, M = 147 g/mol) vào dung dịch chứa 0,25 mol HCl thu được dung dịch X. Sau đó cho tiếp 0,60 mol NaOH vào dung dịch X đến khi các phản ứng xảy ra hoàn toàn, cô cạn dung dịch sau phản ứng thì thu được bao nhiêu gam chất rắn khan?",
        "Áp dụng phương pháp quy đổi nối tiếp: Toàn bộ lượng chất trong dung dịch sau cùng là kết quả của 0,15 mol Glutamic acid (có 2 nhóm –COOH nên phản ứng tối đa với 2 · 0,15 = 0,30 mol NaOH) và 0,25 mol HCl (phản ứng với 0,25 mol NaOH) cùng tác dụng với 0,60 mol NaOH. Tổng số mol NaOH đã phản ứng với Glu và HCl là: n_NaOH(pư) = 2·0,15 + 0,25 = 0,55 (mol) < 0,60 (mol) (NaOH còn dư 0,05 mol) ⇒ số mol H₂O sinh ra đúng bằng số mol NaOH phản ứng: n_H₂O = 0,55 (mol). Bảo toàn khối lượng: m_rắn = m_Glu + m_HCl + m_NaOH(tổng) − m_H₂O = 0,15·147 + 0,25·36,5 + 0,60·40 − 0,55·18 = 22,05 + 9,125 + 24,0 − 9,9 = 45,275 (gam).",
    ),
    C(
        12,
        "polymer",
        "Phản ứng Trùng hợp vs Trùng ngưng & Chuyên sâu Chất dẻo – Tơ – Cao su – Keo dán",
        "♻️",
        "Phân biệt điều kiện cấu tạo monomer để tham gia phản ứng Trùng hợp (có liên kết bội C=C hoặc vòng kém bền) với Trùng ngưng (có ít nhất 2 nhóm chức phản ứng tạo phân tử nhỏ H₂O).",
        "Công nghệ tổng hợp đại phân tử",
        "Làm thế nào để biết một polymer như Tơ nylon-6,6 hay Tơ lapsan được điều chế bằng phản ứng trùng hợp hay phản ứng trùng ngưng? Câu trả lời nằm ở cấu trúc của monomer ban đầu.",
        "Có hai phương pháp tổng hợp polymer chính: Phản ứng TRÙNG HỢP (kết hợp nhiều phân tử nhỏ monomer giống nhau hay tương tự nhau thành phân tử lớn polymer mà KHÔNG giải phóng phân tử nhỏ khác) và Phản ứng TRÙNG NGƯNG (kết hợp nhiều phân tử nhỏ monomer thành phân tử lớn polymer ĐỒNG THỜI giải phóng nhiều phân tử nhỏ như H₂O).",
        "• Điều kiện cần về cấu tạo của Monomer:\n"
        "  + Để tham gia phản ứng TRÙNG HỢP: Monomer phải có LIÊN KẾT BỘI (như CH₂=CH₂, CH₂=CH–CH₃, CH₂=CHCl, CH₂=CH–C₆H₅, CH₂=C(CH₃)–COOCH₃, CH₂=CH–CN, buta-1,3-diene CH₂=CH–CH=CH₂) hoặc VÒNG KÉM BỀN (như caprolactam).\n"
        "  + Để tham gia phản ứng TRÙNG NGƯNG: Monomer phải có ÍT NHẤT 2 NHÓM CHỨC có khả năng phản ứng để tạo liên kết với nhau (như ε-aminocaproic acid H₂N–[CH₂]₅–COOH, ω-aminoenanthic acid H₂N–[CH₂]₆–COOH, cặp hexamethylenediamine H₂N–[CH₂]₆–NH₂ + adipic acid HOOC–[CH₂]₄–COOH, hoặc cặp terephthalic acid + ethylene glycol).\n"
        "• Phân loại kỹ các loại Tơ và độ bền của chúng:\n"
        "  + Tơ thiên nhiên: bông, gai (cellulose), len, tơ tằm (protein).\n"
        "  + Tơ bán tổng hợp (tơ nhân tạo - đi từ polymer thiên nhiên cellulose chế biến hóa học): Tơ visco, Tơ cellulose acetate!\n"
        "  + Tơ tổng hợp: Tơ polyamide (chứa liên kết –CO–NH– như Tơ nylon-6, Tơ enan/nylon-7, Tơ nylon-6,6), Tơ polyester (chứa liên kết –COO– như Tơ lapsan / PET) và Tơ vinylic (như Tơ nitron / olon điều chế từ acrylonitrile CH₂=CH–CN). Lưu ý: Các tơ chứa liên kết amide (–CO–NH–: tơ tằm, nylon-6, nylon-6,6) và liên kết ester (–COO–: tơ lapsan) đều KÉM BỀN trong môi trường acid và môi trường kiềm do bị thủy phân!",
        [
            {
                "category": "I. Bảng phân loại Polymer điều chế bằng Trùng hợp vs Trùng ngưng",
                "items": [
                    {"name": "Nhóm điều chế bằng TRÙNG HỢP (và Đồng trùng hợp)", "formula": "PE, PP, PVC, PS, PMMA (thủy tinh hữu cơ), Teflon (PTFE), Tơ nitron (olon), Cao su buna, Buna-S, Buna-N, Isoprene, Chloroprene", "note": "Không tách ra phân tử H₂O"},
                    {"name": "Nhóm điều chế bằng TRÙNG NGƯNG (có tách ra H₂O)", "formula": "Tơ nylon-6,6 ; Tơ lapsan (PET) ; Tơ enan (nylon-7) ; Nhựa phenol-formaldehyde (PF)", "note": "Riêng Tơ nylon-6 có thể điều chế bằng trùng ngưng ε-aminocaproic acid HOẶC trùng hợp mở vòng caprolactam"},
                ],
            },
            {
                "category": "II. Các Phương trình Tổng hợp Tơ & Cao su quan trọng nhất",
                "items": [
                    {"name": "Tơ Nylon-6,6 (Trùng ngưng Hexamethylenediamine + Adipic acid)", "formula": "n H₂N–[CH₂]₆–NH₂ + n HOOC–[CH₂]₄–COOH ──(t°)──► (–NH–[CH₂]₆–NH–CO–[CH₂]₄–CO–)ₙ + 2n H₂O", "note": "M_mắt_xích = 226 g/mol"},
                    {"name": "Tơ Lapsan / Poly(ethylene terephthalate) - PET", "formula": "n HOOC–C₆H₄–COOH + n HO–CH₂–CH₂–OH ──(t°)──► (–OC–C₆H₄–COO–CH₂–CH₂–O–)ₙ + 2n H₂O", "note": "M_mắt_xích = 192 g/mol"},
                    {"name": "Đồng trùng hợp Cao su Buna-S (Buta-1,3-diene + Styrene)", "formula": "n CH₂=CH–CH=CH₂ + n CH(C₆H₅)=CH₂ ──(t°, p, Na)──► (–CH₂–CH=CH–CH₂–CH(C₆H₅)–CH₂–)ₙ", "note": "Lưu hóa cao su bằng Sulfur (S) tạo cầu nối disulfide –S–S– khâu mạch không gian làm tăng độ đàn hồi và độ bền"},
                ],
            },
        ],
        "Phân tử khối trung bình của một mẫu tơ Nylon-6,6 là 33 900 amu; còn của một mẫu sợi Bông (Cellulose) là 1 620 000 amu. Hãy tính số mắt xích (hệ số polymer hóa n) của mỗi loại polymer trên.",
        "Với tơ Nylon-6,6: công thức một mắt xích là –NH–[CH₂]₆–NH–CO–[CH₂]₄–CO– (C₁₂H₂₂N₂O₂) có M_mắt_xích = 12·12 + 22·1 + 2·14 + 2·16 = 226 (amu). Số mắt xích của tơ Nylon-6,6 là: n₁ = 33 900 / 226 = 150 (mắt xích). Với sợi Bông (Cellulose: (C₆H₁₀O₅)ₙ) có M_mắt_xích = 162 (amu): số mắt xích là n₂ = 1 620 000 / 162 = 10 000 (mắt xích).",
        "Dãy các loại tơ nào dưới đây CHỈ gồm các TƠ BÁN TỔNG HỢP (hay còn gọi là tơ nhân tạo, xuất phát từ nguồn cellulose thiên nhiên)?",
        [
            "Tơ tằm và Sợi bông",
            "Tơ visco và Tơ cellulose acetate",
            "Tơ nylon-6,6 và Tơ nitron (olon)",
            "Tơ lapsan và Tơ capron",
        ],
        1,
        "Giải thích vì sao không nên giặt quần áo bằng lụa tơ tằm, len lông cừu hoặc vải nylon bằng xà phòng có độ kiềm cao hay ngâm trong nước quá nóng; ứng dụng lưu hóa cao su sản xuất lốp xe.",
        "Đốt cháy hoàn toàn một lượng cao su Buna-S (được tạo nên từ phản ứng đồng trùng hợp giữa a mắt xích Buta-1,3-diene C₄H₆ và b mắt xích Styrene C₈H₈) hoặc cho m gam cao su Buna-S phản ứng tối đa với dung dịch chứa 0,15 mol Bromine (Br₂), biết trong mẫu cao su Buna-S này tỉ lệ số mắt xích Buta-1,3-diene : Styrene là 2 : 1. Hãy tính giá trị của m.",
        "Cứ 2 mắt xích Buta-1,3-diene (–CH₂–CH=CH–CH₂–, M = 54, còn 1 liên kết đôi C=C mạch hở) ghép với 1 mắt xích Styrene (–CH(C₆H₅)–CH₂–, M = 104, vòng benzene không cộng với dd Br₂) tạo thành một cụm có khối lượng mol là: M_cụm = 2·54 + 1·104 = 212 (g/mol) và cụm này có 2 liên kết đôi C=C nên cộng tối đa với 2 phân tử Br₂. Vì n_Br₂ = 0,15 (mol) nên số mol cụm là: n_cụm = 0,15 / 2 = 0,075 (mol). Khối lượng cao su Buna-S là: m = 0,075 × 212 = 15,9 (gam).",
    ),
    C(
        12,
        "dien-hoa",
        "Thế điện cực chuẩn (E°), Quy tắc Alpha (α) & Pin điện hóa (Pin Galvani – Pin nhiên liệu – Ắc quy)",
        "🔋",
        "Hiểu cặp oxi hóa - khử của kim loại Mⁿ⁺/M, dãy điện hóa, quy tắc α dự đoán chiều phản ứng oxi hóa - khử và tính sức điện động chuẩn E°_pin = E°_(+) − E°_(−).",
        "Từ thí nghiệm của Galvani, Volta đến Pin Lithium-ion trên xe điện",
        "Mọi chiếc điện thoại thông minh, laptop và xe điện hiện nay đều hoạt động nhờ Pin điện hóa — thiết bị biến đổi trực tiếp năng lượng của phản ứng oxi hóa – khử tự diễn biến thành điện năng.",
        "Dạng oxi hóa (Mⁿ⁺) và dạng khử (M) của cùng một nguyên tố kim loại tạo nên cặp oxi hóa – khử, ký hiệu là Mⁿ⁺/M (dạng oxi hóa viết trước, dạng khử viết sau). Thế điện cực chuẩn (E°_(Mⁿ⁺/M), đơn vị Volt - V) đặc trưng cho khả năng khử của kim loại M và khả năng oxi hóa của ion Mⁿ⁺ ở điều kiện chuẩn ([Mⁿ⁺] = 1 M, 25°C, 1 bar; lấy thế điện cực chuẩn của điện cực Hydrogen chuẩn 2H⁺/H₂ bằng 0,00 V).",
        "• Ý nghĩa của Thế điện cực chuẩn E°_(Mⁿ⁺/M):\n"
        "  + Giá trị E° càng NHỎ (càng âm) ⇒ Tính khử của dạng khử M càng MẠNH, tính oxi hóa của dạng oxi hóa Mⁿ⁺ càng YẾU.\n"
        "  + Giá trị E° càng LỚN (càng dương) ⇒ Tính oxi hóa của dạng oxi hóa Mⁿ⁺ càng MẠNH, tính khử của dạng khử M càng YẾU.\n"
        "  + Chú ý cực kỳ quan trọng trong dãy điện hóa: Cặp Fe³⁺/Fe²⁺ (E° = +0,771 V) đứng SAU cặp Cu²⁺/Cu (E° = +0,340 V) và đứng TRƯỚC cặp Ag⁺/Ag (E° = +0,799 V)! Do đó: Cu tan được trong dung dịch Fe³⁺ (Cu + 2Fe³⁺ → Cu²⁺ + 2Fe²⁺) và Fe²⁺ bị Ag⁺ dư oxi hóa lên Fe³⁺ (Fe²⁺ + Ag⁺ → Fe³⁺ + Ag↓)!\n"
        "• Quy tắc Alpha (α): Khi sắp xếp các cặp oxi hóa – khử theo chiều tăng dần của E° từ trái sang phải, chất oxi hóa mạnh hơn (ở trên bên phải) sẽ tác dụng với chất khử mạnh hơn (ở dưới bên trái) tạo ra chất oxi hóa yếu hơn và chất khử yếu hơn theo chiều nét viết chữ α.\n"
        "• Cấu tạo và hoạt động của Pin Galvani (ví dụ Pin Zn–Cu): Điện cực có E° NHỎ HƠN (kim loại mạnh hơn: Zn) đóng vai trò là ANODE (Cực ÂM −): nơi xảy ra quá trình OXI HÓA (Zn → Zn²⁺ + 2e, thanh Zn tan dần); Điện cực có E° LỚN HƠN (Cu) đóng vai trò là CATHODE (Cực DƯƠNG +): nơi xảy ra quá trình KHỬ (Cu²⁺ + 2e → Cu↓, thanh Cu dày thêm); Cầu muối (chứa KCl/KNO₃) giúp trung hòa điện tích hai dung dịch.",
        [
            {
                "category": "I. Dãy Điện hóa chuẩn (Theo chiều E° tăng dần từ trái sang phải) & Quy tắc Alpha (α)",
                "items": [
                    {"name": "Thứ tự các cặp Oxi hóa – Khử quan trọng cần nhớ", "formula": "K⁺/K < Na⁺/Na < Mg²⁺/Mg < Al³⁺/Al < Zn²⁺/Zn(−0,76V) < Fe²⁺/Fe(−0,44V) < Ni²⁺/Ni < Sn²⁺/Sn < Pb²⁺/Pb < 2H⁺/H₂(0,00V) < Cu²⁺/Cu(+0,34V) < Fe³⁺/Fe²⁺(+0,77V) < Ag⁺/Ag(+0,80V) < Au³⁺/Au(+1,50V)", "note": "Chú ý vị trí cặp Fe³⁺/Fe²⁺ nằm giữa Cu²⁺/Cu và Ag⁺/Ag!"},
                    {"name": "Hai phản ứng đặc biệt suy ra từ cặp Fe³⁺/Fe²⁺", "formula": "Cu + 2FeCl₃ → CuCl₂ + 2FeCl₂  ;  Fe + 2FeCl₃ → 3FeCl₂  ;  FeCl₂ + 3AgNO₃(dư) → Fe(NO₃)₃ + Ag↓ + 2AgCl↓", "note": "Cho Fe tác dụng với AgNO₃ dư thì tạo muối Fe(NO₃)₃!"},
                ],
            },
            {
                "category": "II. Pin Điện hóa Galvani & Công thức tính Sức điện động chuẩn (E°_pin)",
                "items": [
                    {"name": "Vai trò 2 điện cực trong Pin Galvani (Mẹo nhớ: 'Anode Oxi hóa – Cathode Khử')", "formula": "ANODE (Cực ÂM −, kim loại mạnh có E° nhỏ hơn): M → Mⁿ⁺ + ne (tan ra)  ;  CATHODE (Cực DƯƠNG +, E° lớn hơn): Xᵐ⁺ + me → X↓ (bám vào)", "note": "Dòng electron chạy ở mạch ngoài từ Anode (−) sang Cathode (+)"},
                    {"name": "Công thức tính Sức điện động chuẩn của Pin (E°_pin > 0)", "formula": "E°_pin = E°_cathode(+) − E°_anode(−) = E°_lớn − E°_nhỏ", "note": "Sức điện động của pin luôn là một số DƯƠNG"},
                ],
            },
        ],
        "Cho biết thế điện cực chuẩn của hai cặp oxi hóa – khử: E°_(Ni²⁺/Ni) = −0,257 V và E°_(Ag⁺/Ag) = +0,799 V. Khi thiết lập một pin Galvani Ni–Ag ở điều kiện chuẩn: a) Hãy xác định điện cực nào là Anode (cực âm), điện cực nào là Cathode (cực dương); b) Viết các bán phản ứng tại mỗi điện cực, phương trình hóa học tổng quát của pin và tính sức điện động chuẩn E°_pin.",
        "a) Vì E°_(Ni²⁺/Ni) = −0,257 V < E°_(Ag⁺/Ag) = +0,799 V nên thanh Nickel (Ni) là ANODE (cực âm −) và thanh Silver (Ag) là CATHODE (cực dương +). b) Tại Anode (−) xảy ra quá trình oxi hóa: Ni(s) → Ni²⁺(aq) + 2e (thanh Ni tan dần). Tại Cathode (+) xảy ra quá trình khử: Ag⁺(aq) + 1e → Ag(s) (bạc kết tủa bám vào thanh Ag). Phản ứng tổng quát trong pin: Ni(s) + 2Ag⁺(aq) → Ni²⁺(aq) + 2Ag(s). Sức điện động chuẩn của pin là: E°_pin = E°_(Ag⁺/Ag) − E°_(Ni²⁺/Ni) = 0,799 − (−0,257) = 1,056 (V).",
        "Cho bột kim loại Iron (Fe) vào dung dịch chứa lượng dư Silver nitrate (AgNO₃). Sau khi các phản ứng xảy ra hoàn toàn, thu được dung dịch X chứa các muối nào?",
        [
            "Chỉ chứa Fe(NO₃)₂ và AgNO₃ dư",
            "Chứa Fe(NO₃)₃ và AgNO₃ dư (vì ban đầu Fe + 2Ag⁺ → Fe²⁺ + 2Ag, sau đó Ag⁺ dư tiếp tục oxi hóa Fe²⁺ + Ag⁺ → Fe³⁺ + Ag↓)",
            "Chứa Fe(NO₃)₂ và Fe(NO₃)₃",
            "Chỉ chứa Fe(NO₃)₃",
        ],
        1,
        "Chế tạo pin khô (Leclanché), pin kiềm, ắc-quy chì cho ô tô – xe máy, pin sạc Lithium-ion cho điện thoại và pin nhiên liệu Hydrogen – Oxygen không phát thải khí nhà kính.",
        "Một pin Galvani Zn–Cu đang hoạt động. Sau một thời gian, người ta lấy hai thanh điện cực Zn và Cu ra làm khô và cân lại. Biết rằng khối lượng của thanh cực âm (Zn, M = 65) đã giảm đi 3,25 gam. Hỏi khối lượng của thanh cực dương (Cu, M = 64) đã tăng thêm bao nhiêu gam và có bao nhiêu mol electron đã di chuyển qua dây dẫn mạch ngoài?",
        "Tại cực âm Anode (Zn): Zn → Zn²⁺ + 2e. Số mol Zn đã tan ra là: n_Zn = 3,25 / 65 = 0,05 (mol). Số mol electron đã di chuyển qua mạch ngoài là: n_e = 2 · n_Zn = 2 · 0,05 = 0,10 (mol). Tại cực dương Cathode (Cu): Cu²⁺ + 2e → Cu↓. Số mol Cu bám vào thanh cực dương là: n_Cu = n_e / 2 = 0,05 (mol). Vậy khối lượng thanh cực dương Cu đã tăng thêm là: Δm_Cu = 0,05 × 64 = 3,20 (gam).",
    ),
    C(
        12,
        "dai-cuong-kim-loai-phuc-chat",
        "Điện phân (Định luật Faraday), Ăn mòn Điện hóa, Kim loại Nhóm IA – IIA (Nước cứng) & Sơ lược về Phức chất",
        "⚙️",
        "Làm chủ nguyên tắc điện phân nóng chảy - điện phân dung dịch, công thức Faraday, điều kiện ăn mòn điện hóa, cách làm mềm nước cứng và cấu tạo của phức chất.",
        "Từ luyện nhôm, mạ vàng điện phân đến bảo vệ vỏ tàu biển",
        "Điện phân là quá trình ngược lại với Pin điện hóa: dùng dòng điện một chiều từ bên ngoài để buộc một phản ứng oxi hóa – khử không tự diễn biến phải xảy ra, dùng để điều chế kim loại mạnh và mạ điện. Đồng thời, hiểu cơ chế ăn mòn điện hóa giúp ta bảo vệ các công trình thép trên biển.",
        "Điện phân là quá trình oxi hóa – khử xảy ra trên bề mặt các điện cực khi có dòng điện một chiều đi qua chất điện li nóng chảy hoặc dung dịch chất điện li. Ăn mòn điện hóa là sự phá hủy kim loại do sự hình thành các pin điện hóa vi mô ngay trên bề mặt hợp kim tiếp xúc với môi trường điện li.",
        "• Quy tắc Điện phân (Ghi nhớ: Dù ở Pin điện hóa hay Bình điện phân thì tại ANODE luôn xảy ra sự OXI HÓA và tại CATHODE luôn xảy ra sự KHỬ; nhưng trong Bình điện phân thì Anode là cực DƯƠNG (+) và Cathode là cực ÂM (−)!):\n"
        "  + Tại Cathode (−): Các cation kim loại từ K⁺ đến Al³⁺ KHÔNG bị điện phân trong nước (mà H₂O bị khử tạo H₂↑: 2H₂O + 2e → H₂↑ + 2OH⁻); các cation sau Al³⁺ (từ Zn²⁺ đến Au³⁺) bị khử theo thứ tự tính oxi hóa giảm dần (Ag⁺ > Fe³⁺ > Cu²⁺ > H⁺ > Fe²⁺ > Zn²⁺).\n"
        "  + Tại Anode (+) trơ (graphite, Pt): Các anion gốc acid không chứa oxygen (I⁻ > Br⁻ > Cl⁻) bị oxi hóa trước; còn các anion chứa oxygen (NO₃⁻, SO₄²⁻, PO₄³⁻, CO₃²⁻) và F⁻ KHÔNG bị điện phân trong nước (mà H₂O bị oxi hóa tạo O₂↑: 2H₂O → O₂↑ + 4H⁺ + 4e)!\n"
        "• Ba điều kiện cần và đủ để xảy ra ĂN MÒN ĐIỆN HÓA: 1) Hai điện cực phải khác nhau về bản chất (KL–KL hoặc KL–PK như Fe–C trong gang thép); 2) Hai điện cực phải tiếp xúc trực tiếp hoặc gián tiếp với nhau qua dây dẫn; 3) Hai điện cực cùng tiếp xúc với một dung dịch chất điện li (như không khí ẩm, nước biển). Kim loại mạnh hơn đóng vai trò Anode và bị ăn mòn! Phương pháp bảo vệ điện hóa (vật hy sinh): gắn các tấm Kẽm (Zn) vào vỏ tàu biển bằng thép (Fe) để Zn bị ăn mòn thay cho vỏ tàu!\n"
        "• Kim loại Kiềm (IA) – Kiềm thổ (IIA) & Nước cứng (chứa nhiều Ca²⁺, Mg²⁺): Nước cứng tạm thời (chứa HCO₃⁻ - đun sôi sẽ mất tính cứng!), Nước cứng vĩnh cửu (chứa Cl⁻, SO₄²⁻) và Nước cứng toàn phần. Hóa chất làm mềm mọi loại nước cứng: Na₂CO₃ (soda) hoặc Na₃PO₄ (hoặc nhựa trao đổi ion).\n"
        "• Sơ lược về Phức chất (Complex compound, theo chương trình GDPT 2018 mới): gồm Cầu nội (đặt trong ngoặc vuông [M(L)ₙ]^q± gồm Nguyên tử trung tâm M là cation kim loại chuyển tiếp d có orbital trống và các Phối tử L có cặp electron hóa trị riêng cho vào AO trống của M qua liên kết cho – nhận, như NH₃, H₂O, Cl⁻, CN⁻, OH⁻) và Cầu ngoại. Dạng hình học phổ biến: Số phối trí 6 → Bát diện (như [Co(NH₃)₆]³⁺, [Fe(CN)₆]⁴⁻); Số phối trí 4 → Tứ diện hoặc Vuông phẳng (như [Cu(NH₃)₄]²⁺ màu xanh lam thẫm, thuốc chống ung thư Cisplatin [PtCl₂(NH₃)₂]); Số phối trí 2 → Đường thẳng (như [Ag(NH₃)₂]⁺).",
        [
            {
                "category": "I. Công thức Định luật Faraday về Điện phân & Bán phản ứng của Nước ở Điện cực",
                "items": [
                    {"name": "Số mol electron trao đổi ở mỗi điện cực & Công thức Faraday", "formula": "n_e = (I · t) / F  ⇒  m = (A · I · t) / (n · F) = (M / n) · n_e", "note": "I: dòng điện (A) ; t: thời gian (giây - s) ; F = 96 500 C/mol ; n: số e trao đổi của 1 ion"},
                    {"name": "Bán phản ứng của H₂O tại Cathode (−) và Anode (+)", "formula": "Ở Cathode (−, khi hết Cu²⁺...): 2H₂O + 2e → H₂↑ + 2OH⁻  ;  Ở Anode (+, có SO₄²⁻, NO₃⁻): 2H₂O → O₂↑ + 4H⁺ + 4e", "note": "Ví dụ: CuSO₄ + H₂O ──(đpdd)──► Cu↓ + (1/2)O₂↑ + H₂SO₄"},
                ],
            },
            {
                "category": "II. Nước cứng (Ca²⁺, Mg²⁺) & Cấu trúc Phức chất [M(L)ₙ]^q±",
                "items": [
                    {"name": "3 loại Nước cứng & Hóa chất làm mềm vạn năng (Na₂CO₃, Na₃PO₄)", "formula": "Tạm thời: chứa Ca(HCO₃)₂, Mg(HCO₃)₂ (đun sôi tạo CaCO₃↓) ; Vĩnh cửu: chứa Cl⁻, SO₄²⁻ ; Làm mềm chung: dùng Na₂CO₃ hoặc Na₃PO₄", "note": "Ca(HCO₃)₂ + Ca(OH)₂(vừa đủ) → 2CaCO₃↓ + 2H₂O"},
                    {"name": "Thành phần Phức chất (Ví dụ: [Cu(NH₃)₄]SO₄ hoặc K₄[Fe(CN)₆])", "formula": "Nguyên tử trung tâm M (Cu²⁺, Fe²⁺, Ag⁺, Pt²⁺, Co³⁺) + Phối tử L (NH₃, H₂O, CN⁻, Cl⁻) = Cầu nội [M(L)ₙ]", "note": "Liên kết giữa phối tử L và nguyên tử trung tâm M là liên kết CỘNG HÓA TRỊ CHO – NHẬN"},
                ],
            },
        ],
        "Điện phân 200 mL dung dịch Copper(II) sulfate (CuSO₄) 0,5 M với hai điện cực trơ bằng dòng điện một chiều có cường độ không đổi I = 5 A trong thời gian t = 1 930 giây (biết F = 96 500 C/mol, Cu = 64). Hãy tính khối lượng kim loại Cu bám vào Cathode và thể tích khí thoát ra ở Anode (ở đkc 25°C, 1 bar).",
        "Tổng số mol electron chạy qua bình điện phân là: n_e = (I · t) / F = (5 · 1930) / 96 500 = 0,10 (mol). Số mol CuSO₄ ban đầu là: n_Cu²⁺ = 0,2 · 0,5 = 0,10 (mol). Tại Cathode (−): Cu²⁺ + 2e → Cu↓. Vì 2·n_Cu²⁺ = 0,20 mol > n_e = 0,10 mol nên Cu²⁺ chưa điện phân hết, số mol Cu thu được là: n_Cu = n_e / 2 = 0,10 / 2 = 0,05 (mol) ⇒ khối lượng Cu bám vào Cathode là: m_Cu = 0,05 × 64 = 3,20 (gam). Tại Anode (+), ion SO₄²⁻ không bị điện phân mà H₂O bị oxi hóa: 2H₂O → O₂↑ + 4H⁺ + 4e ⇒ số mol khí O₂ thoát ra là: n_O₂ = n_e / 4 = 0,10 / 4 = 0,025 (mol). Thể tích khí O₂ (ở đkc) là: V_O₂ = 0,025 × 24,79 = 0,61975 (lít).",
        "Xét phức chất [Co(NH₃)₆]Cl₃ (Hexaamminecobalt(III) chloride). Trong phức chất này, nguyên tử trung tâm, phối tử và số phối trí của nguyên tử trung tâm lần lượt là:",
        [
            "Nguyên tử trung tâm là Co³⁺, phối tử là Cl⁻, số phối trí là 3",
            "Nguyên tử trung tâm là Co³⁺, phối tử là phân tử NH₃, số phối trí là 6 (dạng hình học bát diện)",
            "Nguyên tử trung tâm là NH₃, phối tử là Co³⁺, số phối trí là 6",
            "Nguyên tử trung tâm là Co²⁺, phối tử là NH₃ và Cl⁻, số phối trí là 9",
        ],
        1,
        "Bảo vệ vỏ tàu biển, giàn khoan dầu khí bằng phương pháp điện hóa (gắn lá kẽm Zn hy sinh), làm mềm nước cứng cho nồi hơi công nghiệp, sản xuất nhôm bằng điện phân nóng chảy Al₂O₃ và ứng dụng phức chất Cisplatin [PtCl₂(NH₃)₂] trong điều trị ung thư.",
        "Một mẫu nước cứng chứa các ion: Ca²⁺ (0,004 mol), Mg²⁺ (0,002 mol), HCO₃⁻ (0,006 mol) và Cl⁻ (x mol). a) Hãy áp dụng định luật bảo toàn điện tích trong dung dịch để tìm giá trị của x và cho biết mẫu nước này thuộc loại nước cứng gì? b) Cần thêm tối thiểu bao nhiêu gam Sodium carbonate (Na₂CO₃, M = 106) vào mẫu nước trên để làm mất hoàn toàn tính cứng của nước?",
        "a) Áp dụng định luật bảo toàn điện tích trong dung dịch (Tổng mol điện tích dương = Tổng mol điện tích âm): 2 · n_Ca²⁺ + 2 · n_Mg²⁺ = 1 · n_HCO₃⁻ + 1 · n_Cl⁻ ⇔ 2·0,004 + 2·0,002 = 0,006 + x ⇔ 0,012 = 0,006 + x ⇒ x = 0,006 (mol). Vì mẫu nước chứa đồng thời cả Ca²⁺, Mg²⁺ với HCO₃⁻ (tính cứng tạm thời) và Cl⁻ (tính cứng vĩnh cửu) nên đây là NƯỚC CỨNG TOÀN PHẦN. b) Khi thêm Na₂CO₃ vào, ion CO₃²⁻ kết tủa toàn bộ Ca²⁺ và Mg²⁺ (Ca²⁺ + CO₃²⁻ → CaCO₃↓ và Mg²⁺ + CO₃²⁻ → MgCO₃↓): n_Na₂CO₃ = n_CO₃²⁻ = n_Ca²⁺ + n_Mg²⁺ = 0,004 + 0,002 = 0,006 (mol). Khối lượng Na₂CO₃ tối thiểu cần dùng là: m = 0,006 × 106 = 0,636 (gam).",
    ),
    C(
        12,
        "hoa-hoc-moi-truong",
        "Hóa học Xanh (Green Chemistry), Hiệu ứng nhà kính – Mưa Acid – Tầng Ozone & Phát triển bền vững",
        "🌱",
        "Nắm vững 12 nguyên tắc Hóa học xanh (Độ kinh tế nguyên tử AE%), cơ chế gây Hiệu ứng nhà kính, Mưa acid, Suy giảm tầng Ozone và giải pháp phát triển bền vững.",
        "Hóa học vì một hành tinh xanh bền vững",
        "Thế kỷ 21 đặt ra yêu cầu bức thiết cho ngành hóa học: thiết kế các quy trình sản xuất không tạo chất thải độc hại, sử dụng nguồn nguyên liệu tái tạo và xử lý triệt để ô nhiễm không khí, đất và nguồn nước.",
        "Hóa học xanh (Green Chemistry) là việc thiết kế các sản phẩm và quy trình hóa học nhằm giảm thiểu hoặc loại bỏ hoàn toàn việc sử dụng và tạo ra các chất độc hại đối với sức khỏe con người và môi trường.",
        "• Độ kinh tế nguyên tử (Atom Economy - AE%): đo lường hiệu quả của một phản ứng hóa học trong việc chuyển hóa các nguyên tử của chất tham gia thành sản phẩm mong muốn: AE% = [ Tổng khối lượng mol của sản phẩm mong muốn / Tổng khối lượng mol của tất cả các chất tham gia (hoặc tất cả sản phẩm) ] × 100%. (Các phản ứng cộng và phản ứng trùng hợp không có sản phẩm phụ nên có AE% = 100%!).\n"
        "• Bốn vấn đề môi trường toàn cầu và tác nhân hóa học chính:\n"
        "  1. Hiệu ứng nhà kính & Biến đổi khí hậu: do sự gia tăng nồng độ các khí nhà kính hấp thụ bức xạ hồng ngoại là CO₂ (nhiều nhất, từ đốt nhiên liệu hóa thạch), CH₄ (từ bãi rác, chăn nuôi, ruộng ngập nước), N₂O, CFC.\n"
        "  2. Mưa acid (nước mưa có pH < 5,6): do khí SO₂ và NOₓ (NO, NO₂) chuyển hóa trong khí quyển thành H₂SO₄ và HNO₃ hòa tan vào nước mưa, làm ăn mòn công trình đá vôi/kim loại, hủy diệt rừng và làm chua đất, nước.\n"
        "  3. Suy giảm tầng Ozone (O₃ ở tầng bình lưu bảo vệ Trái Đất khỏi tia tử ngoại UV): do các hợp chất Freon / CFC (Chlorofluorocarbon như CF₂Cl₂) phân hủy dưới tia UV giải phóng gốc tự do Cl• phá hủy hàng trăm nghìn phân tử O₃ theo phản ứng dây chuyền.\n"
        "  4. Hiện tượng Phú dưỡng nguồn nước (dư thừa N, P) và Ô nhiễm trắng (rác thải nhựa polymer khó phân hủy).",
        [
            {
                "category": "I. Công thức Độ kinh tế nguyên tử (Atom Economy – AE%) trong Hóa học Xanh",
                "items": [
                    {"name": "Độ kinh tế nguyên tử AE% (Tính theo PTHH cân bằng)", "formula": "AE% = [ (ν_sp · M_sản_phẩm_mong_muốn) / Σ(ν_i · M_chất_tham_gia_i) ] × 100%", "note": "AE% càng gần 100% thì lượng chất thải phụ (waste) càng ít"},
                    {"name": "Phản ứng có AE% = 100% (Tối ưu nhất theo Hóa học xanh)", "formula": "Phản ứng Cộng (C₂H₄ + H₂O → C₂H₅OH) & Phản ứng Trùng hợp (nCH₂=CH₂ → PE) đều có AE% = 100%", "note": "Vì chỉ có duy nhất 1 sản phẩm tạo thành, không có sản phẩm phụ"},
                ],
            },
            {
                "category": "II. Bảng đối chiếu Tác nhân Hóa học và Các vấn đề Môi trường",
                "items": [
                    {"name": "Hiệu ứng nhà kính vs Mưa acid vs Thủng tầng Ozone", "formula": "Nhà kính: CO₂, CH₄, N₂O ; Mưa acid (pH < 5,6): SO₂, NO, NO₂ ; Thủng tầng Ozone (O₃): CFC (Freon)", "note": "Khí CO (Carbon monoxide) không gây mưa acid nhưng cực độc vì kết hợp chặt với Hemoglobin trong máu!"},
                ],
            },
        ],
        "Để sản xuất Ethylene oxide (C₂H₄O, M = 44 g/mol — nguyên liệu quan trọng trong công nghiệp hóa chất), người ta có thể dùng hai quy trình sau:\n"
        "• Quy trình 1 (Cũ): C₂H₄ + Cl₂ + Ca(OH)₂ → C₂H₄O + CaCl₂ + H₂O (tổng M các chất tham gia = 28 + 71 + 74 = 173 g/mol).\n"
        "• Quy trình 2 (Hiện đại, dùng xúc tác Ag): 2C₂H₄ + O₂ ──(Ag, t°)──► 2C₂H₄O.\n"
        "Hãy tính Độ kinh tế nguyên tử (AE%) của mỗi quy trình và cho biết quy trình nào đáp ứng tiêu chí Hóa học xanh?",
        "Ở Quy trình 1: tạo ra sản phẩm phụ CaCl₂ và H₂O nên độ kinh tế nguyên tử chỉ là: AE₁% = (44 / 173) × 100% ≈ 25,43% (gần 75% khối lượng nguyên liệu biến thành chất thải!). Ở Quy trình 2: toàn bộ các nguyên tử của chất tham gia (2C₂H₄ + O₂) đều chuyển hết vào sản phẩm mong muốn (2C₂H₄O, không có sản phẩm phụ): AE₂% = (2·44) / (2·28 + 32) × 100% = (88 / 88) × 100% = 100%. Vậy Quy trình 2 hoàn toàn đáp ứng tiêu chí Hóa học xanh.",
        "Hai chất khí nào dưới đây là nguyên nhân chính trực tiếp gây ra hiện tượng MƯA ACID (làm pH của nước mưa giảm xuống dưới 5,6)?",
        [
            "CO₂ và CH₄",
            "SO₂ và NOₓ (NO, NO₂)",
            "CO và H₂S",
            "CFC và N₂",
        ],
        1,
        "Chuyển dịch sang kinh tế tuần hoàn, năng lượng tái tạo (Hydrogen xanh sản xuất từ điện phân nước bằng điện mặt trời/gió), sử dụng nhựa sinh học tự phân hủy (PLA, PHA) và xử lý khí thải công nghiệp.",
        "Khí thải của một nhà máy nhiệt điện đốt than có chứa khí SO₂ gây ô nhiễm và mưa acid. Để xử lý khí SO₂ trước khi thải ra môi trường, các kỹ sư dẫn khí thải đi qua tháp phun vôi sữa chứa Calcium hydroxide Ca(OH)₂ (hoặc bột đá vôi CaCO₃) có mặt không khí (O₂) để chuyển hóa hoàn toàn SO₂ thành thạch cao (CaSO₄·2H₂O, M = 172 g/mol) dùng sản xuất tấm trần thạch cao xây dựng. Nếu mỗi ngày nhà máy thu hồi và xử lý được 640 kg khí SO₂ (M = 64 g/mol) với hiệu suất 95%, thì tạo ra được bao nhiêu tấn thạch cao CaSO₄·2H₂O mỗi ngày?",
        "Phương trình tổng quát quá trình khử lưu huỳnh ướt tạo thạch cao: 2SO₂ + 2Ca(OH)₂ + O₂ + 2H₂O → 2CaSO₄·2H₂O↓. Số kmol SO₂ thu hồi mỗi ngày là: n_SO₂ = 640 / 64 = 10 (kmol). Với hiệu suất 95%, số kmol thạch cao CaSO₄·2H₂O tạo thành là: n_thạch_cao = 10 × 95% = 9,5 (kmol). Khối lượng thạch cao thu được mỗi ngày là: m = 9,5 × 172 = 1 634 (kg) = 1,634 (tấn).",
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
        print(f"ĐÃ XỬ LÝ: {len(LESSONS)} BÀI HÓA HỌC LỚP 6–12")
        print(f"TẠO MỚI:  {created}")
        print(f"CẬP NHẬT: {updated}")
        print("=" * 60)

    except Exception as e:
        db.rollback()
        print("\n" + "=" * 60)
        print("LỖI KHI CẬP NHẬT HÓA HỌC:")
        print(e)
        print("=" * 60)
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()