"""VẬT LÍ 8 (KHOA HỌC TỰ NHIÊN 8) — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).

Bao phủ đầy đủ các chương Vật lí trong SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống:
- Chương III. Khối lượng riêng và áp suất (Bài 13 – Bài 17)
- Chương IV. Tác dụng làm quay của lực (Bài 18 – Bài 19) & Chuyên đề Công – Công suất cơ học
- Chương V. Điện (Bài 20 – Bài 25)
- Chương VI. Nhiệt (Bài 26 – Bài 29)

7 chủ đề tương thích hệ thống game:
1. khoi-luong-rieng (game_type="simulation")
2. ap-suat (game_type="simulation")
3. luc-day-archimedes (game_type="simulation")
4. moment-luc-don-bay (game_type="game_moment_luc_don_bay")
5. cong-suat (game_type="game_congsuat")
6. nhiet-nang (game_type="game_nhietnang")
7. dien (game_type="game_dien")

Mỗi chủ đề gồm: Yêu cầu cần đạt (CT GDPT 2018), định nghĩa, lý thuyết chi tiết theo từng bài SGK,
nhóm công thức KaTeX, ví dụ minh họa, ứng dụng thực tiễn, thông tin trò chơi và 10 câu hỏi
(4 câu Biết MCQ, 2 câu Hiểu MCQ, 2 câu Hiểu Đúng/Sai 4 mệnh đề a–d, 1 câu Vận dụng MCQ, 1 câu Vận dụng Trả lời ngắn).
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 8

LESSONS = [
    # ===================== CHỦ ĐỀ 1: KHỐI LƯỢNG RIÊNG =====================
    {
        "topic": "khoi-luong-rieng",
        "title": "Khối lượng riêng và Thực hành xác định khối lượng riêng",
        "icon": "🧱",
        "description": "Chương III · SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống (Bài 13 – Bài 14): Khái niệm khối lượng riêng, đơn vị đo, trọng lượng riêng và phương pháp thực hành xác định khối lượng riêng của vật rắn, chất lỏng.",
        "requirements": [
            r"Nêu được định nghĩa khối lượng riêng, xác định được khối lượng riêng qua khối lượng và thể tích tương ứng theo công thức $D = \dfrac{m}{V}$.",
            r"Liệt kê được một số đơn vị khối lượng riêng thường dùng ($\text{kg/m}^3$, $\text{g/cm}^3$, $\text{g/mL}$) và thực hiện được việc đổi đơn vị đo.",
            r"Nêu được khái niệm trọng lượng riêng và vận dụng được hệ thức liên hệ $d = \dfrac{P}{V} = 10D$.",
            r"Thực hiện được thí nghiệm để xác định được khối lượng riêng của một khối hộp chữ nhật, của một vật có hình dạng bất kì không thấm nước và của một lượng chất lỏng.",
        ],
        "definition": r"""- **Khối lượng riêng** của một chất được xác định bằng khối lượng của một đơn vị thể tích chất đó: $D = \dfrac{m}{V}$. Khối lượng riêng là đại lượng đặc trưng cho từng chất, giúp nhận biết chất tạo nên vật và giải thích sự nổi hay chìm của vật.
- **Trọng lượng riêng** của một chất được xác định bằng trọng lượng của một đơn vị thể tích chất đó: $d = \dfrac{P}{V} \approx 10D$ (tại mặt đất với $P \approx 10m$).""",
        "theory": r"""### Bài 13. Khối lượng riêng
- **Khái niệm và công thức**: Khi biết khối lượng $m$ của một vật làm bằng chất đồng nhất có thể tích $V$, khối lượng riêng của chất đó được tính bằng $D = \dfrac{m}{V}$ (một số tài liệu kí hiệu là $\rho$). Từ đó suy ra khối lượng $m = D \cdot V$ và thể tích $V = \dfrac{m}{D}$.
- **Đơn vị đo**: Đơn vị chuẩn trong hệ SI của khối lượng riêng là ki-lô-gam trên mét khối ($\text{kg/m}^3$). Ngoài ra người ta còn dùng gam trên xăng-ti-mét khối ($\text{g/cm}^3$) hoặc gam trên mi-li-lít ($\text{g/mL}$) với quy đổi: $1\text{ g/cm}^3 = 1\text{ g/mL} = 1000\text{ kg/m}^3$.
- **Khối lượng riêng của một số chất ở điều kiện thường**: Nước nguyên chất có $D_{\text{nước}} = 1000\text{ kg/m}^3 = 1\text{ g/cm}^3$; nước đá có $D_{\text{đá}} \approx 920\text{ kg/m}^3$; dầu ăn có $D_{\text{dầu}} \approx 800\text{ kg/m}^3$; nhôm có $D_{\text{Al}} = 2700\text{ kg/m}^3$; sắt có $D_{\text{Fe}} = 7800\text{ kg/m}^3$; đồng có $D_{\text{Cu}} = 8900\text{ kg/m}^3$; vàng có $D_{\text{Au}} = 19300\text{ kg/m}^3$.
- **Trọng lượng riêng**: Đại lượng $d = \dfrac{P}{V}$ (đơn vị $\text{N/m}^3$) gọi là trọng lượng riêng của chất. Do trọng lượng liên hệ với khối lượng theo $P = 10m$ nên $d = 10D$.
### Bài 14. Thực hành xác định khối lượng riêng
- **Xác định khối lượng riêng của khối hộp chữ nhật**: Dùng cân điện tử đo khối lượng $m$; dùng thước thẳng đo ba kích thước chiều dài $a$, chiều rộng $b$, chiều cao $c$ để tính thể tích $V = a \cdot b \cdot c$; sau đó tính $D = \dfrac{m}{V}$.
- **Xác định khối lượng riêng của một lượng chất lỏng**: Cân cốc khô có khối lượng $m_1$; đổ chất lỏng vào cốc rồi cân tổng khối lượng $m_2$, suy ra khối lượng chất lỏng $m = m_2 - m_1$. Đổ chất lỏng vào bình chia độ để đọc thể tích $V$, rồi tính $D = \dfrac{m}{V}$.
- **Xác định khối lượng riêng của vật rắn không thấm nước có hình dạng bất kì (viên sỏi)**: Dùng cân điện tử đo khối lượng $m$ của viên sỏi khô. Rót nước vào bình chia độ tới vạch thể tích $V_1$, buộc chỉ thả chìm hoàn toàn viên sỏi vào bình chia độ thì mực nước dâng tới vạch $V_2$, suy ra thể tích viên sỏi $V = V_2 - V_1$ và tính $D = \dfrac{m}{V_2 - V_1}$.""",
        "formulas": [
            G(
                "I. Công thức khối lượng riêng và trọng lượng riêng",
                F("Khối lượng riêng", r"$D = \dfrac{m}{V} \Rightarrow m = D \cdot V;\quad V = \dfrac{m}{D}$", r"$D$ ($\text{kg/m}^3$), $m$ ($\text{kg}$), $V$ ($\text{m}^3$)"),
                F("Trọng lượng riêng", r"$d = \dfrac{P}{V} = 10D$", r"$d$ ($\text{N/m}^3$), $P$ ($\text{N}$), $V$ ($\text{m}^3$)"),
                F("Khối lượng riêng trung bình của hỗn hợp (không hao hụt thể tích)", r"$D_{\text{tb}} = \dfrac{m_1 + m_2}{V_1 + V_2}$", r"Không lấy trung bình cộng $\dfrac{D_1 + D_2}{2}$ khi $V_1 \neq V_2$"),
            ),
            G(
                "II. Quy đổi đơn vị và công thức thực hành",
                F("Đổi đơn vị khối lượng riêng", r"$1\text{ g/cm}^3 = 1\text{ g/mL} = 1000\text{ kg/m}^3$", r"$1\text{ kg/m}^3 = 10^{-3}\text{ g/cm}^3$"),
                F("Đổi đơn vị thể tích", r"$1\text{ m}^3 = 1000\text{ dm}^3 = 1000\text{ L} = 10^6\text{ cm}^3 = 10^6\text{ mL}$", r"$1\text{ dm}^3 = 1\text{ L} = 1000\text{ cm}^3$"),
                F("Thể tích vật rắn bằng bình chia độ", r"$V = V_2 - V_1$", r"$V_1$: mực nước ban đầu; $V_2$: mực nước khi thả chìm vật"),
            ),
        ],
        "example": r"Trong giờ thực hành, một học sinh dùng cân điện tử đo được khối lượng của một hòn sỏi khô là $m = 130\text{ g}$. Khi thả chìm hoàn toàn hòn sỏi vào bình chia độ đang chứa $V_1 = 50\text{ cm}^3$ nước thì mực nước dâng lên đến vạch $V_2 = 100\text{ cm}^3$. Hãy tính thể tích, khối lượng riêng (theo $\text{g/cm}^3$ và $\text{kg/m}^3$) và trọng lượng riêng của hòn sỏi.",
        "example_answer": r"""- Thể tích của hòn sỏi bằng thể tích phần nước dâng lên trong bình chia độ:
$$V = V_2 - V_1 = 100 - 50 = 50\text{ cm}^3$$
- Khối lượng riêng của hòn sỏi là:
$$D = \dfrac{m}{V} = \dfrac{130}{50} = 2{,}6\text{ g/cm}^3 = 2600\text{ kg/m}^3$$
- Trọng lượng riêng của hòn sỏi là:
$$d = 10D = 10 \cdot 2600 = 26000\text{ N/m}^3$$""",
        "real_life": r"""- **Công nghiệp hàng không và chế tạo máy**: Sử dụng hợp kim nhôm và titan có khối lượng riêng nhỏ ($D_{\text{Al}} = 2700\text{ kg/m}^3$) nhưng độ bền cao để giảm khối lượng máy bay, tiết kiệm nhiên liệu.
- **Xây dựng và kiểm định chất lượng**: Tính toán khối lượng dầm bê tông, cột thép từ thể tích thiết kế; kiểm tra độ nguyên chất của vàng, bạc hoặc phát hiện lỗ rỗng bên trong vật đúc kim loại.""",
        "game_title": "Thử thách thực tế: Khối lượng riêng",
        "game_description": "Đo khối lượng và thể tích các mẫu vật trong phòng thí nghiệm ảo để xác định khối lượng riêng và kiểm tra vật đặc hay rỗng.",
        "game_type": "simulation",
        "quiz": [
            mcq(
                "biet",
                r"Công thức nào sau đây dùng để tính khối lượng riêng của một vật có khối lượng $m$ và thể tích $V$?",
                [r"$D = m \cdot V$", r"$D = \dfrac{m}{V}$", r"$D = \dfrac{V}{m}$", r"$D = m + V$"],
                1,
                r"Khối lượng riêng của một chất được xác định bằng khối lượng của một đơn vị thể tích chất đó: $D = \dfrac{m}{V}$.",
            ),
            mcq(
                "biet",
                r"Đơn vị chuẩn của khối lượng riêng trong hệ đo lường quốc tế SI là gì?",
                [r"$\text{N/m}^3$", r"$\text{kg/m}^2$", r"$\text{kg/m}^3$", r"$\text{g/cm}^2$"],
                2,
                r"Trong hệ SI, khối lượng đo bằng $\text{kg}$ và thể tích đo bằng $\text{m}^3$ nên đơn vị chuẩn của khối lượng riêng là $\text{kg/m}^3$.",
            ),
            mcq(
                "biet",
                r"Biết khối lượng riêng của nhôm là $2700\text{ kg/m}^3$. Giá trị này khi đổi sang đơn vị $\text{g/cm}^3$ bằng bao nhiêu?",
                [r"$0{,}27\text{ g/cm}^3$", r"$2{,}7\text{ g/cm}^3$", r"$27\text{ g/cm}^3$", r"$270\text{ g/cm}^3$"],
                1,
                r"Vì $1\text{ g/cm}^3 = 1000\text{ kg/m}^3$ nên $2700\text{ kg/m}^3 = \dfrac{2700}{1000} = 2{,}7\text{ g/cm}^3$.",
            ),
            mcq(
                "biet",
                r"Hệ thức nào dưới đây biểu diễn đúng mối liên hệ giữa trọng lượng riêng $d$ ($\text{N/m}^3$) và khối lượng riêng $D$ ($\text{kg/m}^3$) của cùng một chất?",
                [r"$d = 10D$", r"$D = 10d$", r"$d = \dfrac{D}{100}$", r"$d = D^2$"],
                0,
                r"Ta có $d = \dfrac{P}{V} = \dfrac{10m}{V} = 10D$.",
            ),
            mcq(
                "hieu",
                r"Biết khối lượng riêng của sắt là $7800\text{ kg/m}^3$. Một thanh sắt đặc có thể tích $V = 2\text{ dm}^3$ sẽ có khối lượng bằng bao nhiêu?",
                [r"$3{,}9\text{ kg}$", r"$7{,}8\text{ kg}$", r"$15{,}6\text{ kg}$", r"$156\text{ kg}$"],
                2,
                r"Đổi $V = 2\text{ dm}^3 = 0{,}002\text{ m}^3$. Khối lượng của thanh sắt là $m = D \cdot V = 7800 \cdot 0{,}002 = 15{,}6\text{ kg}$.",
            ),
            mcq(
                "hieu",
                r"Khi thả chìm hoàn toàn một viên đá có khối lượng $m = 104\text{ g}$ vào bình chia độ chứa $60\text{ cm}^3$ nước thì mực nước dâng lên tới vạch $100\text{ cm}^3$. Khối lượng riêng của viên đá là:",
                [r"$1{,}04\text{ g/cm}^3$", r"$1{,}73\text{ g/cm}^3$", r"$2{,}6\text{ g/cm}^3$", r"$4{,}0\text{ g/cm}^3$"],
                2,
                r"Thể tích viên đá là $V = V_2 - V_1 = 100 - 60 = 40\text{ cm}^3$. Khối lượng riêng của viên đá là $D = \dfrac{m}{V} = \dfrac{104}{40} = 2{,}6\text{ g/cm}^3$.",
            ),
            tf4(
                "hieu",
                r"Một khối gỗ hình hộp chữ nhật đặc có các kích thước $10\text{ cm} \times 5\text{ cm} \times 4\text{ cm}$ và có khối lượng $m = 160\text{ g}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Thể tích của khối gỗ hình hộp chữ nhật đó bằng $200\text{ cm}^3$.",
                    r"b) Khối lượng riêng của loại gỗ này bằng $0{,}8\text{ g/cm}^3$.",
                    r"c) Đổi sang đơn vị chuẩn SI, khối lượng riêng của gỗ là $80\text{ kg/m}^3$.",
                    r"d) Nếu cưa đôi khối gỗ này thành hai phần bằng nhau thì khối lượng riêng của mỗi phần giảm đi một nửa.",
                ],
                [True, True, False, False],
                r"a) Đúng vì $V = 10 \cdot 5 \cdot 4 = 200\text{ cm}^3$. b) Đúng vì $D = \dfrac{m}{V} = \dfrac{160}{200} = 0{,}8\text{ g/cm}^3$. c) Sai vì $0{,}8\text{ g/cm}^3 = 0{,}8 \cdot 1000 = 800\text{ kg/m}^3$. d) Sai vì khối lượng riêng là thuộc tính bản chất của chất tạo nên vật, khi chia đôi thì cả $m$ và $V$ cùng giảm $2$ lần nên $D$ không đổi.",
            ),
            tf4(
                "hieu",
                r"Trong phòng thí nghiệm, học sinh tiến hành xác định khối lượng riêng của dầu ăn và của một viên bi thép. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Để xác định khối lượng riêng của dầu ăn, ta chỉ cần dùng cân điện tử và bình chia độ.",
                    r"b) Khối lượng dầu ăn trong cốc bằng khối lượng tổng cộng của cốc chứa dầu trừ đi khối lượng của cốc khô rỗng.",
                    r"c) Dầu ăn có khối lượng riêng khoảng $800\text{ kg/m}^3$, nhỏ hơn khối lượng riêng của nước ($1000\text{ kg/m}^3$) nên dầu ăn nổi trên mặt nước.",
                    r"d) Khi đo thể tích viên bi thép bằng bình chia độ, chỉ cần thả viên bi ngập một nửa trong nước là đọc được chính xác thể tích viên bi.",
                ],
                [True, True, True, False],
                r"a) Đúng vì cân đo khối lượng $m$ và bình chia độ đo thể tích $V$. b) Đúng vì $m_{\text{dầu}} = m_2 - m_1$. c) Đúng vì $D_{\text{dầu}} < D_{\text{nước}}$. d) Sai vì viên bi phải ngập chìm hoàn toàn trong nước thì phần nước dâng lên mới bằng toàn bộ thể tích viên bi.",
            ),
            mcq(
                "vandung",
                r"Một bức tượng bằng đồng có khối lượng $m = 1{,}78\text{ kg}$, khi nhúng chìm hoàn toàn vào bình tràn chứa đầy nước thì lượng nước tràn ra có thể tích $V = 250\text{ cm}^3$. Biết khối lượng riêng của đồng nguyên chất là $D = 8{,}9\text{ g/cm}^3$. Thể tích phần rỗng bên trong bức tượng là:",
                [r"$0\text{ cm}^3$ (tượng đặc)", r"$25\text{ cm}^3$", r"$50\text{ cm}^3$", r"$72\text{ cm}^3$"],
                2,
                r"Đổi $m = 1{,}78\text{ kg} = 1780\text{ g}$. Thể tích phần đồng đặc thực sự là $V_{\text{đồng}} = \dfrac{m}{D} = \dfrac{1780}{8{,}9} = 200\text{ cm}^3$. Vì thể tích toàn bộ bức tượng là $250\text{ cm}^3$ nên thể tích phần rỗng bên trong là $V_{\text{rỗng}} = 250 - 200 = 50\text{ cm}^3$.",
            ),
            short(
                "vandung",
                r"Một hợp kim gồm $m_1 = 540\text{ g}$ nhôm (có khối lượng riêng $D_1 = 2{,}7\text{ g/cm}^3$) và $m_2 = 890\text{ g}$ đồng (có khối lượng riêng $D_2 = 8{,}9\text{ g/cm}^3$). Giả sử thể tích của hợp kim bằng tổng thể tích các kim loại thành phần. Tính khối lượng riêng của hợp kim đó theo đơn vị $\text{kg/m}^3$ (làm tròn đến hàng đơn vị).",
                ["4767"],
                r"Thể tích nhôm là $V_1 = \dfrac{m_1}{D_1} = \dfrac{540}{2{,}7} = 200\text{ cm}^3$. Thể tích đồng là $V_2 = \dfrac{m_2}{D_2} = \dfrac{890}{8{,}9} = 100\text{ cm}^3$. Khối lượng riêng của hợp kim là $D = \dfrac{m_1 + m_2}{V_1 + V_2} = \dfrac{540 + 890}{200 + 100} = \dfrac{1430}{300} \approx 4{,}767\text{ g/cm}^3 = 4767\text{ kg/m}^3$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 2: ÁP SUẤT =====================
    {
        "topic": "ap-suat",
        "title": "Áp suất trên một bề mặt, Áp suất chất lỏng và Áp suất khí quyển",
        "icon": "🚜",
        "description": "Chương III · SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống (Bài 15 – Bài 16): Áp lực, công thức tính áp suất trên một bề mặt, nguyên tắc tăng giảm áp suất, áp suất chất lỏng, bình thông nhau và áp suất khí quyển.",
        "requirements": [
            r"Dùng dụng cụ thực hành, khẳng định được áp suất sinh ra khi có áp lực tác dụng lên một diện tích bề mặt: $p = \dfrac{F}{S}$.",
            r"Liệt kê được một số đơn vị đo áp suất thông dụng ($\text{Pa}$, $\text{N/m}^2$, $\text{kPa}$, $\text{atm}$, $\text{mmHg}$) và thảo luận được công dụng của việc tăng, giảm áp suất qua một số hiện tượng thực tế.",
            r"Nêu được chất lỏng gây ra áp suất theo mọi phương lên đáy bình, thành bình và các vật ở trong lòng nó; vận dụng được công thức $p = d \cdot h$.",
            r"Thực hiện được thí nghiệm chứng tỏ tồn tại áp suất khí quyển và áp suất này tác dụng theo mọi phương; mô tả được một số hiện tượng và ứng dụng của áp suất khí quyển, giác mút, bình xịt, tàu đệm khí.",
        ],
        "definition": r"""- **Áp lực** là lực ép có phương vuông góc với mặt bị ép.
- **Áp suất** ($p$) được tính bằng độ lớn của áp lực ($F$) trên một đơn vị diện tích bị ép ($S$): $p = \dfrac{F}{S}$.
- **Áp suất chất lỏng** tại độ sâu $h$ so với mặt thoáng là $p = d \cdot h = D \cdot g \cdot h$, tác dụng theo mọi phương.
- **Áp suất khí quyển** là áp suất do lớp không khí bao quanh Trái Đất gây ra theo mọi phương lên mọi vật trên mặt đất.""",
        "theory": r"""### Bài 15. Áp suất trên một bề mặt
- **Áp lực**: Tác dụng của áp lực lên mặt bị ép phụ thuộc vào hai yếu tố: độ lớn của áp lực $F$ và diện tích bị ép $S$. Khi vật đặt nằm yên trên mặt phẳng nằm ngang thì áp lực của vật lên mặt sàn có độ lớn bằng trọng lượng của vật: $F = P = 10m$.
- **Công thức và đơn vị áp suất**: $p = \dfrac{F}{S}$. Đơn vị áp suất trong hệ SI là па-xcan ($\text{Pa}$), với $1\text{ Pa} = 1\text{ N/m}^2$; bội số thường dùng là $1\text{ kPa} = 1000\text{ Pa}$ và $1\text{ MPa} = 10^6\text{ Pa}$.
- **Tăng, giảm áp suất trong thực tiễn**:
  + Để **tăng áp suất** ($p$ lớn): tăng áp lực $F$ hoặc giảm diện tích bị ép $S$ (ví dụ: mài sắc lưỡi dao, làm nhọn đầu đinh, đầu cọc).
  + Để **giảm áp suất** ($p$ nhỏ): giảm áp lực $F$ hoặc tăng diện tích bị ép $S$ (ví dụ: xe tăng dùng bánh xích bản rộng, móng nhà xây to bản, kê ván gỗ dưới bánh xe ô tô khi đi qua đất lún).
### Bài 16. Áp suất chất lỏng. Áp suất khí quyển
- **Áp suất chất lỏng**: Chất lỏng không chỉ gây áp suất lên đáy bình mà còn gây áp suất lên thành bình và theo mọi phương lên các vật ở trong lòng chất lỏng. Tại một điểm ở độ sâu $h$ tính từ mặt thoáng chất lỏng có trọng lượng riêng $d$, áp suất chất lỏng là $p = d \cdot h$. Trong cùng một chất lỏng đứng yên, áp suất tại những điểm trên cùng một mặt phẳng nằm ngang (cùng độ sâu $h$) luôn có độ lớn bằng nhau.
- **Truyền áp suất trong chất lỏng và máy nén thủy lực**: Độ tăng áp suất lên một chất lỏng chứa trong bình kín được truyền nguyên vẹn tới mọi điểm của chất lỏng và thành bình (nguyên lí Pascal). Trong máy nén thủy lực có hai pít-tông diện tích $S_1$ và $S_2$: $\dfrac{F_2}{F_1} = \dfrac{S_2}{S_1}$.
- **Áp suất khí quyển**: Vì không khí cũng có trọng lượng nên khí quyển gây ra áp suất theo mọi phương. Ở ngang mực nước biển, áp suất khí quyển chuẩn xấp xỉ $p_0 \approx 760\text{ mmHg} \approx 101325\text{ Pa} = 1\text{ atm}$. Càng lên cao, không khí càng loãng nên áp suất khí quyển càng giảm (khi thay đổi độ cao đột ngột, sự chênh lệch áp suất hai bên màng nhĩ gây ra cảm giác ù tai).""",
        "formulas": [
            G(
                "I. Áp suất trên một bề mặt rắn",
                F("Công thức tính áp suất", r"$p = \dfrac{F}{S} \Rightarrow F = p \cdot S;\quad S = \dfrac{F}{p}$", r"$F$: áp lực ($\text{N}$), $S$: diện tích bị ép ($\text{m}^2$), $p$: áp suất ($\text{Pa}$)"),
                F("Đổi đơn vị diện tích và áp suất", r"$1\text{ Pa} = 1\text{ N/m}^2;\quad 1\text{ kPa} = 1000\text{ Pa};\quad 1\text{ cm}^2 = 10^{-4}\text{ m}^2$", r"Luôn đổi $S$ ra $\text{m}^2$ trước khi tính $p$"),
            ),
            G(
                "II. Áp suất chất lỏng, máy nén thủy lực và áp suất khí quyển",
                F("Áp suất cột chất lỏng ở độ sâu $h$", r"$p = d \cdot h = 10D \cdot h$", r"$d$: trọng lượng riêng chất lỏng ($\text{N/m}^3$), $h$: độ sâu tính từ mặt thoáng ($\text{m}$)"),
                F("Áp suất tuyệt đối tại độ sâu $h$", r"$p_{\text{tổng}} = p_0 + d \cdot h$", r"$p_0$: áp suất khí quyển trên mặt thoáng ($\text{Pa}$)"),
                F("Hệ thức máy nén thủy lực", r"$\dfrac{F_2}{F_1} = \dfrac{S_2}{S_1}$", r"Diện tích pít-tông lớn gấp bao nhiêu lần thì lực nâng gấp bấy nhiêu lần"),
            ),
        ],
        "example": r"Một người có khối lượng $m = 60\text{ kg}$ đứng thẳng bằng cả hai bàn chân trên mặt sàn nằm ngang. Biết diện tích tiếp xúc của mỗi bàn chân với mặt sàn là $S_1 = 150\text{ cm}^2$. Tính áp lực và áp suất của người đó tác dụng lên mặt sàn khi đứng bằng cả hai chân và khi co một chân.",
        "example_answer": r"""- Áp lực của người đó lên mặt sàn bằng trọng lượng cơ thể:
$$F = P = 10m = 10 \cdot 60 = 600\text{ N}$$
- Diện tích tiếp xúc của $1$ bàn chân là $S_1 = 150\text{ cm}^2 = 0{,}015\text{ m}^2$; của cả $2$ bàn chân là $S_2 = 2S_1 = 0{,}03\text{ m}^2$.
- Áp suất khi đứng bằng cả hai chân:
$$p_2 = \dfrac{F}{S_2} = \dfrac{600}{0{,}03} = 20000\text{ Pa} = 20\text{ kPa}$$
- Áp suất khi đứng co một chân:
$$p_1 = \dfrac{F}{S_1} = \dfrac{600}{0{,}015} = 40000\text{ Pa} = 40\text{ kPa}$$""",
        "real_life": r"""- **Kĩ thuật xây dựng và thủy lợi**: Đê chắn sóng và đập thủy điện luôn được xây có phần chân đê rộng hơn nhiều so với mặt đê vì càng xuống sâu áp suất nước $p = d \cdot h$ càng lớn.
- **Cơ khí và đời sống**: Kích thủy lực nâng ô tô, phanh thủy lực, giác mút treo tường, ống hút nước, lỗ nhỏ trên nắp ấm trà giúp không khí tràn vào để rót nước dễ dàng.""",
        "game_title": "Thử thách thực tế: Áp suất và Thủy lực",
        "game_description": "Thay đổi diện tích chân đế, độ sâu tàu lặn và tỉ số diện tích pít-tông máy nén thủy lực để kiểm chứng các quy luật áp suất.",
        "game_type": "game_chat_luu",
        "quiz": [
            mcq(
                "biet",
                r"Đơn vị đo áp suất पा-xcan ($\text{Pa}$) bằng đơn vị nào sau đây?",
                [r"$1\text{ N}\cdot\text{m}$", r"$1\text{ N/m}^2$", r"$1\text{ N/m}^3$", r"$1\text{ kg/m}^3$"],
                1,
                r"Từ công thức $p = \dfrac{F}{S}$, đơn vị của áp suất là $\text{N/m}^2$ và $1\text{ Pa} = 1\text{ N/m}^2$.",
            ),
            mcq(
                "biet",
                r"Muốn làm tăng áp suất tác dụng lên một bề mặt thì ta có thể thực hiện cách nào sau đây?",
                [
                    r"Giảm áp lực và tăng diện tích bị ép",
                    r"Giữ nguyên áp lực và tăng diện tích bị ép",
                    r"Giữ nguyên áp lực và giảm diện tích bị ép",
                    r"Giảm áp lực và giữ nguyên diện tích bị ép",
                ],
                2,
                r"Theo công thức $p = \dfrac{F}{S}$, khi giữ nguyên áp lực $F$ và giảm diện tích bị ép $S$ thì áp suất $p$ sẽ tăng.",
            ),
            mcq(
                "biet",
                r"Công thức tính áp suất của chất lỏng tại một điểm ở độ sâu $h$ so với mặt thoáng chất lỏng (có trọng lượng riêng $d$) là:",
                [r"$p = \dfrac{d}{h}$", r"$p = d \cdot h$", r"$p = \dfrac{h}{d}$", r"$p = d + h$"],
                1,
                r"Áp suất chất lỏng ở độ sâu $h$ tính từ mặt thoáng được xác định bởi công thức $p = d \cdot h$.",
            ),
            mcq(
                "biet",
                r"Hiện tượng nào sau đây là do áp suất khí quyển gây ra?",
                [
                    r"Quả táo rụng từ trên cây xuống mặt đất",
                    r"Hộp sữa giấy bị bẹp lại về nhiều phía khi ta hút hết sữa và không khí bên trong hộp",
                    r"Viên bi sắt lăn chậm dần trên sàn nhà do ma sát",
                    r"Thanh sắt nở dài ra khi bị nung nóng",
                ],
                1,
                r"Khi hút bớt không khí trong hộp sữa, áp suất bên trong nhỏ hơn áp suất khí quyển bên ngoài nên áp suất khí quyển ép bẹp vỏ hộp từ mọi phía.",
            ),
            mcq(
                "hieu",
                r"Một vật có trọng lượng $P = 180\text{ N}$ đặt trên mặt bàn nằm ngang, diện tích tiếp xúc giữa vật và mặt bàn là $S = 300\text{ cm}^2$. Áp suất của vật tác dụng lên mặt bàn là:",
                [r"$0{,}6\text{ Pa}$", r"$600\text{ Pa}$", r"$6000\text{ Pa}$", r"$54000\text{ Pa}$"],
                2,
                r"Đổi $S = 300\text{ cm}^2 = 0{,}03\text{ m}^2$. Áp suất tác dụng lên mặt bàn là $p = \dfrac{F}{S} = \dfrac{180}{0{,}03} = 6000\text{ Pa}$.",
            ),
            mcq(
                "hieu",
                r"Một thợ lặn đang làm việc ở độ sâu $h = 20\text{ m}$ dưới mặt nước biển. Biết trọng lượng riêng của nước biển là $d = 10300\text{ N/m}^3$. Áp suất do riêng cột nước biển gây ra tại vị trí của thợ lặn là:",
                [r"$20600\text{ Pa}$", r"$206000\text{ Pa}$", r"$515\text{ Pa}$", r"$103000\text{ Pa}$"],
                1,
                r"Áp suất do nước biển gây ra ở độ sâu $h = 20\text{ m}$ là $p = d \cdot h = 10300 \cdot 20 = 206000\text{ Pa}$.",
            ),
            tf4(
                "hieu",
                r"Một bình hình trụ cao $80\text{ cm}$ đựng đầy nước có trọng lượng riêng $d = 10000\text{ N/m}^3$. Xét một điểm $M$ nằm trong nước cách đáy bình $20\text{ cm}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Nước trong bình chỉ gây ra áp suất lên đáy bình chứ không gây áp suất lên thành bình.",
                    r"b) Độ sâu của điểm $M$ tính từ mặt thoáng chất lỏng là $h_M = 60\text{ cm} = 0{,}6\text{ m}$.",
                    r"c) Áp suất do nước gây ra tại điểm $M$ bằng $2000\text{ Pa}$.",
                    r"d) Áp suất do nước gây ra tại đáy bình bằng $8000\text{ Pa}$.",
                ],
                [False, True, False, True],
                r"a) Sai vì chất lỏng gây áp suất theo mọi phương lên cả đáy bình và thành bình. b) Đúng vì $h_M = 80 - 20 = 60\text{ cm} = 0{,}6\text{ m}$. c) Sai vì $p_M = d \cdot h_M = 10000 \cdot 0{,}6 = 6000\text{ Pa}$ (không lấy khoảng cách tới đáy bình). d) Đúng vì tại đáy bình $h = 0{,}8\text{ m} \Rightarrow p = 10000 \cdot 0{,}8 = 8000\text{ Pa}$.",
            ),
            tf4(
                "hieu",
                r"Xét các ứng dụng thực tế liên quan đến áp suất. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Lưỡi dao được mài mỏng và sắc để giảm diện tích tiếp xúc, giúp tăng áp suất khi thái thực phẩm.",
                    r"b) Xe tăng chiến đấu có khối lượng rất lớn phải dùng bánh xích bản rộng để làm tăng áp suất lên mặt đất.",
                    r"c) Khi đi máy bay lên cao hoặc đi cáp treo lên núi cao, áp suất khí quyển bên ngoài giảm đột ngột làm màng nhĩ bị đẩy ra phía ngoài gây ù tai.",
                    r"d) Trong máy nén thủy lực, nếu diện tích pít-tông lớn gấp $25$ lần diện tích pít-tông nhỏ thì lực nâng ở pít-tông lớn gấp $25$ lần lực ép ở pít-tông nhỏ.",
                ],
                [True, False, True, True],
                r"a) Đúng vì giảm $S$ thì tăng $p$. b) Sai vì bánh xích bản rộng làm tăng diện tích bị ép $S$ để giảm áp suất $p$, giúp xe không bị lún. c) Đúng vì càng lên cao áp suất khí quyển càng giảm. d) Đúng theo hệ thức $\dfrac{F_2}{F_1} = \dfrac{S_2}{S_1} = 25$.",
            ),
            mcq(
                "vandung",
                r"Một viên gạch hình hộp chữ nhật có các kích thước $20\text{ cm} \times 10\text{ cm} \times 5\text{ cm}$ và có trọng lượng $P = 20\text{ N}$ được đặt trên mặt sàn nằm ngang. Áp suất lớn nhất mà viên gạch có thể gây ra trên mặt sàn là:",
                [r"$1000\text{ Pa}$", r"$2000\text{ Pa}$", r"$4000\text{ Pa}$", r"$500\text{ Pa}$"],
                2,
                r"Áp suất đạt giá trị lớn nhất khi diện tích mặt bị ép nhỏ nhất: $S_{\min} = 10\text{ cm} \times 5\text{ cm} = 50\text{ cm}^2 = 0{,}005\text{ m}^2$. Khi đó $p_{\max} = \dfrac{P}{S_{\min}} = \dfrac{20}{0{,}005} = 4000\text{ Pa}$.",
            ),
            short(
                "vandung",
                r"Một máy nâng thủy lực trong trạm bảo dưỡng có diện tích pít-tông nhỏ là $S_1 = 12\text{ cm}^2$ và diện tích pít-tông lớn là $S_2 = 300\text{ cm}^2$. Để nâng một chiếc ô tô có trọng lượng $F_2 = 15000\text{ N}$ thì cần tác dụng lên pít-tông nhỏ một lực $F_1$ tối thiểu bằng bao nhiêu $\text{N}$?",
                ["600"],
                r"Áp dụng công thức máy nén thủy lực: $\dfrac{F_1}{F_2} = \dfrac{S_1}{S_2} \Rightarrow F_1 = F_2 \cdot \dfrac{S_1}{S_2} = 15000 \cdot \dfrac{12}{300} = 600\text{ N}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 3: LỰC ĐẨY ARCHIMEDES =====================
    {
        "topic": "luc-day-archimedes",
        "title": "Lực đẩy Archimedes và Sự nổi của vật",
        "icon": "🚢",
        "description": "Chương III · SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống (Bài 17): Phương, chiều và độ lớn của lực đẩy Archimedes, điều kiện định tính và định lượng để vật chìm, lơ lửng hoặc nổi trong chất lỏng.",
        "requirements": [
            r"Thực hiện thí nghiệm khảo sát tác dụng của chất lỏng lên vật đặt trong chất lỏng, rút ra được: điều kiện định tính về vật nổi, vật chìm; định luật Archimedes.",
            r"Nêu được phương, chiều và vận dụng được công thức tính độ lớn của lực đẩy Archimedes: $F_{\text{A}} = d \cdot V$.",
            r"Giải thích được điều kiện nổi, lơ lửng, chìm dựa trên so sánh trọng lượng riêng (hoặc khối lượng riêng) của vật và chất lỏng.",
            r"Vận dụng được kiến thức về lực đẩy Archimedes để giải thích nguyên lí hoạt động của tàu thủy, tàu ngầm, khinh khí cầu và giải bài toán thực tế.",
        ],
        "definition": r"""- **Định luật Archimedes**: Một vật nhúng vào chất lỏng bị chất lỏng đẩy thẳng đứng từ dưới lên với một lực có độ lớn bằng trọng lượng của phần chất lỏng mà vật chiếm chỗ. Lực này gọi là **lực đẩy Archimedes** ($F_{\text{A}}$).
- **Công thức**: $F_{\text{A}} = d \cdot V$ (trong đó $d$ là trọng lượng riêng của chất lỏng tính bằng $\text{N/m}^3$, $V$ là thể tích phần chất lỏng bị vật chiếm chỗ tính bằng $\text{m}^3$).""",
        "theory": r"""### Bài 17. Lực đẩy Archimedes
- **Tác dụng của chất lỏng lên vật nhúng trong nó**: Mọi vật nhúng trong chất lỏng (hoặc chất khí) đều chịu tác dụng của một lực đẩy có **phương thẳng đứng**, **chiều từ dưới lên trên** gọi là lực đẩy Archimedes.
- **Độ lớn của lực đẩy Archimedes**: Khi treo vật vào lực kế ngoài không khí, lực kế chỉ trọng lượng $P$ của vật; khi nhúng vật vào chất lỏng, lực kế chỉ giá trị $F < P$. Độ giảm số chỉ của lực kế chính là độ lớn lực đẩy Archimedes: $F_{\text{A}} = P - F$. Theo định luật Archimedes: $F_{\text{A}} = d_{\text{lỏng}} \cdot V_{\text{chìm}}$.
- **Điều kiện định tính và định lượng về sự nổi của vật**: Khi thả một vật đặc có trọng lượng $P = d_{\text{vật}} \cdot V$ vào trong lòng chất lỏng có trọng lượng riêng $d_{\text{lỏng}}$:
  + Vật **chìm xuống** đáy bình khi $P > F_{\text{A}}$ hay $d_{\text{vật}} > d_{\text{lỏng}}$ ($D_{\text{vật}} > D_{\text{lỏng}}$).
  + Vật **lơ lửng** trong lòng chất lỏng khi $P = F_{\text{A}}$ hay $d_{\text{vật}} = d_{\text{lỏng}}$ ($D_{\text{vật}} = D_{\text{lỏng}}$).
  + Vật **nổi lên** mặt thoáng khi $P < F_{\text{A}}$ hay $d_{\text{vật}} < d_{\text{lỏng}}$ ($D_{\text{vật}} < D_{\text{lỏng}}$).
- **Trạng thái cân bằng khi vật nổi trên mặt thoáng**: Khi vật đã nổi lên và đứng yên cân bằng trên mặt thoáng chất lỏng (một phần thể tích $V_{\text{chìm}}$ ngập dưới mặt thoáng), lực đẩy Archimedes lúc đó cân bằng với trọng lượng của vật: $F_{\text{A}} = P \iff d_{\text{lỏng}} \cdot V_{\text{chìm}} = d_{\text{vật}} \cdot V_{\text{vật}}$.""",
        "formulas": [
            G(
                "I. Độ lớn lực đẩy Archimedes",
                F("Công thức định luật Archimedes", r"$F_{\text{A}} = d_{\text{lỏng}} \cdot V_{\text{chìm}} = 10D_{\text{lỏng}} \cdot V_{\text{chìm}}$", r"$d_{\text{lỏng}}$ ($\text{N/m}^3$), $V_{\text{chìm}}$ ($\text{m}^3$): thể tích phần vật ngập trong chất lỏng"),
                F(r"Xác định $F_{\text{A}}$ bằng lực kế", r"$F_{\text{A}} = P - F_{\text{biểu kiến}}$", r"$P$: số chỉ lực kế ngoài không khí; $F_{\text{biểu kiến}}$: số chỉ lực kế khi nhúng vật vào chất lỏng"),
            ),
            G(
                "II. Điều kiện nổi, chìm và cân bằng trên mặt thoáng",
                F("So sánh theo khối lượng riêng", r"$D_{\text{vật}} > D_{\text{lỏng}}\text{: chìm};\quad D_{\text{vật}} = D_{\text{lỏng}}\text{: lơ lửng};\quad D_{\text{vật}} < D_{\text{lỏng}}\text{: nổi}$", r""),
                F("Khi vật nổi đứng yên trên mặt thoáng", r"$F_{\text{A}} = P \iff d_{\text{lỏng}} \cdot V_{\text{chìm}} = d_{\text{vật}} \cdot V_{\text{vật}} \Rightarrow \dfrac{V_{\text{chìm}}}{V_{\text{vật}}} = \dfrac{D_{\text{vật}}}{D_{\text{lỏng}}}$", r"Tỉ lệ phần thể tích chìm bằng tỉ số khối lượng riêng"),
            ),
        ],
        "example": r"Một vật bằng kim loại đặc khi treo vào lực kế ở ngoài không khí thì lực kế chỉ $P = 7{,}8\text{ N}$. Khi nhúng vật chìm hoàn toàn vào trong nước (có trọng lượng riêng $d_0 = 10000\text{ N/m}^3$) thì lực kế chỉ $F = 6{,}8\text{ N}$. Tính độ lớn lực đẩy Archimedes tác dụng lên vật, thể tích của vật và khối lượng riêng của kim loại làm vật.",
        "example_answer": r"""- Độ lớn lực đẩy Archimedes tác dụng lên vật là:
$$F_{\text{A}} = P - F = 7{,}8 - 6{,}8 = 1{,}0\text{ N}$$
- Thể tích của vật (do vật chìm hoàn toàn nên $V = V_{\text{chìm}}$):
$$V = \dfrac{F_{\text{A}}}{d_0} = \dfrac{1{,}0}{10000} = 10^{-4}\text{ m}^3 = 100\text{ cm}^3$$
- Trọng lượng riêng và khối lượng riêng của kim loại làm vật là:
$$d = \dfrac{P}{V} = \dfrac{7{,}8}{10^{-4}} = 78000\text{ N/m}^3 \Rightarrow D = \dfrac{d}{10} = 7800\text{ kg/m}^3\text{ (sắt/thép)}$$""",
        "real_life": r"""- **Đóng tàu thủy**: Thép có khối lượng riêng lớn hơn nước rất nhiều ($7800\text{ kg/m}^3 > 1000\text{ kg/m}^3$), nhưng tàu biển được chế tạo có khoang rỗng lớn nên khối lượng riêng trung bình của con tàu nhỏ hơn nước, giúp tàu nổi và chở được hàng chục nghìn tấn hàng.
- **Tàu ngầm và khinh khí cầu**: Tàu ngầm điều chỉnh việc lặn xuống hay nổi lên bằng cách bơm nước biển vào hoặc đẩy nước ra khỏi các khoang chứa nước bằng khí nén.""",
        "game_title": "Thử thách thực tế: Lực đẩy Archimedes",
        "game_description": "Chất hàng hóa lên tàu và điều chỉnh khoang dằn tàu ngầm để khảo sát lực đẩy Archimedes cùng điều kiện nổi - chìm.",
        "game_type": "simulation",
        "quiz": [
            mcq(
                "biet",
                r"Lực đẩy Archimedes tác dụng lên một vật nhúng trong chất lỏng có phương và chiều như thế nào?",
                [
                    r"Phương thẳng đứng, chiều từ trên xuống dưới",
                    r"Phương thẳng đứng, chiều từ dưới lên trên",
                    r"Phương nằm ngang, chiều từ trái sang phải",
                    r"Phương vuông góc với mặt bên của vật theo mọi hướng",
                ],
                1,
                r"Lực đẩy Archimedes luôn có phương thẳng đứng và chiều hướng từ dưới lên trên.",
            ),
            mcq(
                "biet",
                r"Trong công thức tính độ lớn lực đẩy Archimedes $F_{\text{A}} = d \cdot V$, đại lượng $d$ và $V$ lần lượt là:",
                [
                    r"Trọng lượng riêng của vật và thể tích của toàn bộ vật",
                    r"Trọng lượng riêng của chất lỏng và thể tích phần chất lỏng bị vật chiếm chỗ",
                    r"Khối lượng riêng của chất lỏng và thể tích toàn bộ chất lỏng trong bình",
                    r"Trọng lượng riêng của chất lỏng và diện tích mặt đáy của vật",
                ],
                1,
                r"Theo định luật Archimedes, $d$ là trọng lượng riêng của chất lỏng ($\text{N/m}^3$) và $V$ là thể tích phần chất lỏng bị vật chiếm chỗ ($\text{m}^3$).",
            ),
            mcq(
                "biet",
                r"Thả một vật đặc có trọng lượng riêng $d_{\text{vật}}$ vào trong một chất lỏng có trọng lượng riêng $d_{\text{lỏng}}$. Vật sẽ nổi lên mặt thoáng khi:",
                [
                    r"$d_{\text{vật}} > d_{\text{lỏng}}$",
                    r"$d_{\text{vật}} = d_{\text{lỏng}}$",
                    r"$d_{\text{vật}} < d_{\text{lỏng}}$",
                    r"$d_{\text{vật}} = 2d_{\text{lỏng}}$",
                ],
                2,
                r"Khi $d_{\text{vật}} < d_{\text{lỏng}}$ thì trọng lượng của vật nhỏ hơn lực đẩy Archimedes cực đại khi ngập hoàn toàn nên vật nổi lên.",
            ),
            mcq(
                "biet",
                r"Treo một vật vào lực kế ngoài không khí thì lực kế chỉ $12\text{ N}$. Khi nhúng vật chìm trong nước thì lực kế chỉ $8{,}5\text{ N}$. Độ lớn lực đẩy Archimedes tác dụng lên vật là:",
                [r"$20{,}5\text{ N}$", r"$8{,}5\text{ N}$", r"$3{,}5\text{ N}$", r"$12\text{ N}$"],
                2,
                r"Độ lớn lực đẩy Archimedes bằng độ giảm số chỉ của lực kế: $F_{\text{A}} = P - F = 12 - 8{,}5 = 3{,}5\text{ N}$.",
            ),
            mcq(
                "hieu",
                r"Một quả cầu bằng sắt có thể tích $V = 400\text{ cm}^3$ được nhúng chìm hoàn toàn trong nước có trọng lượng riêng $d = 10000\text{ N/m}^3$. Lực đẩy Archimedes tác dụng lên quả cầu có độ lớn là:",
                [r"$4000\text{ N}$", r"$40\text{ N}$", r"$4\text{ N}$", r"$0{,}4\text{ N}$"],
                2,
                r"Đổi $V = 400\text{ cm}^3 = 4 \cdot 10^{-4}\text{ m}^3$. Lực đẩy Archimedes là $F_{\text{A}} = d \cdot V = 10000 \cdot 4 \cdot 10^{-4} = 4\text{ N}$.",
            ),
            mcq(
                "hieu",
                r"Hai quả cầu đặc có cùng thể tích $V$, quả cầu thứ nhất bằng nhôm ($D_1 = 2700\text{ kg/m}^3$) và quả cầu thứ hai bằng đồng ($D_2 = 8900\text{ kg/m}^3$), cùng được nhúng chìm hoàn toàn vào một bể nước. So sánh lực đẩy Archimedes $F_{\text{A1}}$ và $F_{\text{A2}}$ tác dụng lên hai quả cầu:",
                [r"$F_{\text{A1}} < F_{\text{A2}}$", r"$F_{\text{A1}} > F_{\text{A2}}$", r"$F_{\text{A1}} = F_{\text{A2}}$", r"$F_{\text{A2}} = 3F_{\text{A1}}$"],
                2,
                r"Vì hai quả cầu có cùng thể tích $V$ và đều chìm hoàn toàn trong cùng một chất lỏng (nước) nên $F_{\text{A1}} = F_{\text{A2}} = d_{\text{nước}} \cdot V$.",
            ),
            tf4(
                "hieu",
                r"Một khối gỗ đặc có thể tích $V = 1000\text{ cm}^3$ và khối lượng riêng $D_{\text{gỗ}} = 600\text{ kg/m}^3$ được thả vào một bể nước có khối lượng riêng $D_{\text{nước}} = 1000\text{ kg/m}^3$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Trọng lượng của khối gỗ ngoài không khí là $P = 6\text{ N}$.",
                    r"b) Khi thả vào bể nước, khối gỗ sẽ chìm hẳn xuống đáy bể vì có thể tích lớn.",
                    r"c) Khi khối gỗ nổi và đứng yên cân bằng trên mặt nước, độ lớn lực đẩy Archimedes tác dụng lên khối gỗ bằng đúng $6\text{ N}$.",
                    r"d) Thể tích phần khối gỗ chìm dưới mặt nước khi cân bằng là $600\text{ cm}^3$.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $m = D_{\text{gỗ}} \cdot V = 600 \cdot 10^{-3} = 0{,}6\text{ kg} \Rightarrow P = 10m = 6\text{ N}$. b) Sai vì $D_{\text{gỗ}} < D_{\text{nước}}$ nên khối gỗ nổi. c) Đúng vì khi nổi cân bằng thì $F_{\text{A}} = P = 6\text{ N}$. d) Đúng vì $V_{\text{chìm}} = \dfrac{F_{\text{A}}}{d_{\text{nước}}} = \dfrac{6}{10000} = 6 \cdot 10^{-4}\text{ m}^3 = 600\text{ cm}^3$.",
            ),
            tf4(
                "hieu",
                r"Một con tàu vận tải đi từ sông (nước ngọt có $d_1 = 10000\text{ N/m}^3$) ra biển (nước mặn có $d_2 = 10300\text{ N/m}^3$), giả sử tổng khối lượng của tàu không thay đổi. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Trọng lượng $P$ của con tàu khi ở trên biển lớn hơn khi ở trên sông.",
                    r"b) Vì tàu đều nổi cân bằng trên mặt nước nên lực đẩy Archimedes tác dụng lên tàu khi ở trên sông và khi ở trên biển có độ lớn bằng nhau ($F_{\text{A1}} = F_{\text{A2}} = P$).",
                    r"c) Thể tích phần vỏ tàu chìm trong nước biển nhỏ hơn thể tích phần vỏ tàu chìm trong nước sông.",
                    r"d) Khi đi từ sông ra biển, mớn nước của tàu hạ thấp xuống (thân tàu nhô cao lên thêm một chút).",
                ],
                [False, True, True, True],
                r"a) Sai vì khối lượng tàu không đổi nên trọng lượng $P$ không đổi. b) Đúng vì ở cả hai nơi tàu đều nổi cân bằng nên $F_{\text{A1}} = F_{\text{A2}} = P$. c) Đúng vì $d_1 V_{\text{chìm 1}} = d_2 V_{\text{chìm 2}}$, mà $d_2 > d_1$ nên $V_{\text{chìm 2}} < V_{\text{chìm 1}}$. d) Đúng vì thể tích phần chìm giảm nên thân tàu nhô cao lên.",
            ),
            mcq(
                "vandung",
                r"Một vật đặc có khối lượng $m = 540\text{ g}$ và khối lượng riêng $D = 2{,}7\text{ g/cm}^3$ được treo vào lực kế rồi nhúng chìm hoàn toàn vào một bình đựng dầu có trọng lượng riêng $d_{\text{dầu}} = 8000\text{ N/m}^3$. Số chỉ của lực kế khi đó là:",
                [r"$5{,}4\text{ N}$", r"$1{,}6\text{ N}$", r"$3{,}8\text{ N}$", r"$3{,}4\text{ N}$"],
                2,
                r"Trọng lượng của vật ngoài không khí là $P = 10m = 10 \cdot 0{,}54 = 5{,}4\text{ N}$. Thể tích của vật là $V = \dfrac{m}{D} = \dfrac{540}{2{,}7} = 200\text{ cm}^3 = 2 \cdot 10^{-4}\text{ m}^3$. Lực đẩy Archimedes của dầu là $F_{\text{A}} = d_{\text{dầu}} \cdot V = 8000 \cdot 2 \cdot 10^{-4} = 1{,}6\text{ N}$. Số chỉ lực kế là $F = P - F_{\text{A}} = 5{,}4 - 1{,}6 = 3{,}8\text{ N}$.",
            ),
            short(
                "vandung",
                r"Một tảng băng trôi trên mặt biển có thể tích phần nhô lên khỏi mặt nước biển là $V_{\text{nổi}} = 100\text{ m}^3$. Biết khối lượng riêng của băng là $D_{\text{băng}} = 920\text{ kg/m}^3$ và của nước biển là $D_{\text{biển}} = 1020\text{ kg/m}^3$. Tính tổng thể tích $V$ của cả tảng băng theo đơn vị $\text{m}^3$.",
                ["1020"],
                r"Gọi tổng thể tích tảng băng là $V$ ($\text{m}^3$), thể tích phần chìm dưới nước biển là $V_{\text{chìm}} = V - 100$. Khi băng nổi cân bằng: $F_{\text{A}} = P \iff D_{\text{biển}} \cdot (V - 100) = D_{\text{băng}} \cdot V \iff 1020(V - 100) = 920V \iff 100V = 102000 \Rightarrow V = 1020\text{ m}^3$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 4: MOMENT LỰC VÀ ĐÒN BẨY =====================
    {
        "topic": "moment-luc-don-bay",
        "title": "Tác dụng làm quay của lực, Moment lực và Đòn bẩy",
        "icon": "🔧",
        "description": "Chương IV · SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống (Bài 18 – Bài 19): Tác dụng làm quay của lực quanh một trục, khái niệm cánh tay đòn, công thức tính moment lực và nguyên tắc hoạt động của các loại đòn bẩy.",
        "requirements": [
            r"Thực hiện thí nghiệm để mô tả được tác dụng làm quay của lực lên một vật có trục quay cố định hoặc có điểm tựa.",
            r"Nêu được tác dụng làm quay của lực lên một vật quanh một điểm hoặc một trục được đặc trưng bằng moment lực; tính được moment lực theo công thức $M = F \cdot d$.",
            r"Dùng dụng cụ đơn giản, minh họa được đòn bẩy có thể làm thay đổi hướng tác dụng của lực và làm giảm lực nâng vật khi quy tắc cân bằng $F_1 \cdot d_1 = F_2 \cdot d_2$ thỏa mãn.",
            r"Lấy được ví dụ và phân loại được một số đòn bẩy trong thực tiễn (đòn bẩy loại 1, loại 2, loại 3) cũng như hệ đòn bẩy trên cơ thể người để sử dụng an toàn, hiệu quả.",
        ],
        "definition": r"""- **Moment lực** ($M$) đối với một trục quay là đại lượng đặc trưng cho tác dụng làm quay của lực và được đo bằng tích của độ lớn lực ($F$) với cánh tay đòn ($d$) của nó: $M = F \cdot d$ (đơn vị $\text{N}\cdot\text{m}$).
- **Cánh tay đòn** ($d$) của lực là khoảng cách vuông góc từ trục quay (hoặc điểm tựa $O$) đến giá của lực.
- **Điều kiện cân bằng của đòn bẩy**: $F_1 \cdot d_1 = F_2 \cdot d_2$.""",
        "theory": r"""### Bài 18. Tác dụng làm quay của lực. Moment lực
- **Tác dụng làm quay của lực**: Khi lực tác dụng vào một vật có trục quay cố định mà giá của lực không cắt và không song song với trục quay thì lực đó có tác dụng làm vật quay quanh trục. Nếu giá của lực đi qua trục quay ($d = 0$) thì lực không có tác dụng làm quay vật.
- **Moment lực**: Tác dụng làm quay của lực phụ thuộc vào độ lớn của lực $F$ và khoảng cách vuông góc $d$ từ trục quay đến giá của lực (cánh tay đòn). Công thức tính moment lực là $M = F \cdot d$, trong đó $F$ đo bằng niu-tơn ($\text{N}$), $d$ đo bằng mét ($\text{m}$) và $M$ có đơn vị là niu-tơn mét ($\text{N}\cdot\text{m}$). Lực càng lớn và cánh tay đòn càng dài thì tác dụng làm quay càng mạnh.
### Bài 19. Đòn bẩy và ứng dụng
- **Cấu tạo và quy tắc cân bằng của đòn bẩy**: Đòn bẩy là một thanh cứng có thể quay quanh một điểm tựa cố định $O$. Khi đòn bẩy cân bằng dưới tác dụng của hai lực $F_1$ và $F_2$ có cánh tay đòn tương ứng $d_1$ và $d_2$, moment của hai lực đối với điểm tựa $O$ phải bằng nhau: $F_1 \cdot d_1 = F_2 \cdot d_2 \iff \dfrac{F_1}{F_2} = \dfrac{d_2}{d_1}$. Muốn dùng lực $F_2$ nhỏ hơn trọng lượng $F_1$ của vật thì cánh tay đòn $d_2$ phải lớn hơn $d_1$.
- **Ba loại đòn bẩy trong thực tiễn**:
  + **Đòn bẩy loại 1**: Điểm tựa $O$ nằm ở khoảng giữa điểm đặt của vật ($F_1$) và điểm đặt lực tác dụng ($F_2$). Đòn bẩy này làm đổi hướng của lực và cho lợi về lực nếu $d_2 > d_1$ (ví dụ: bập bênh, cái kéo, kìm cắt sắt, xà beng bẩy đá, mái chèo thuyền).
  + **Đòn bẩy loại 2 (có điểm tựa ở một đầu, vật ở giữa)**: Điểm tựa $O$ ở một đầu, vật chịu lực đặt ở giữa $O$ và lực tác dụng $F_2$. Vì luôn có $d_2 > d_1$ nên đòn bẩy này **luôn cho lợi về lực** (ví dụ: xe rùa đẩy vật liệu, dụng cụ mở nắp chai, kẹp tách hạt cứng, khớp bàn chân khi kiễng gót).
  + **Đòn bẩy loại 3 (có điểm tựa ở một đầu, lực tác dụng ở giữa)**: Điểm tựa $O$ ở một đầu, lực tác dụng $F_2$ đặt ở giữa $O$ và vật. Vì $d_2 < d_1$ nên không lợi về lực nhưng **lợi về đường đi và tốc độ thao tác** (ví dụ: đôi đũa, nhíp, kẹp gắp thức ăn, cần câu cá, cánh tay người khi nâng tạ với khuỷu tay là điểm tựa).""",
        "formulas": [
            G(
                "I. Moment lực và điều kiện cân bằng đòn bẩy",
                F("Công thức tính moment lực", r"$M = F \cdot d$", r"$F$: độ lớn lực ($\text{N}$), $d$: cánh tay đòn ($\text{m}$), $M$: moment lực ($\text{N}\cdot\text{m}$)"),
                F("Quy tắc cân bằng của đòn bẩy", r"$M_1 = M_2 \iff F_1 \cdot d_1 = F_2 \cdot d_2 \iff \dfrac{F_1}{F_2} = \dfrac{d_2}{d_1}$", r"Lực tác dụng tỉ lệ nghịch với cánh tay đòn"),
            ),
            G(
                "II. Phân loại đòn bẩy theo vị trí điểm tựa $O$",
                F("Đòn bẩy loại 1 ($O$ ở giữa $F_1$ và $F_2$)", r"$d_2 > d_1 \Rightarrow F_2 < F_1$", r"Ví dụ: bập bênh, cái kéo, kìm, xà beng"),
                F("Đòn bẩy loại 2 (vật $F_1$ ở giữa $O$ và $F_2$)", r"$d_2 > d_1 \Rightarrow F_2 < F_1\text{ (luôn lợi về lực)}$", r"Ví dụ: xe rùa, cái mở nắp chai, kẹp hạt dẻ"),
                F("Đòn bẩy loại 3 (lực $F_2$ ở giữa $O$ và vật $F_1$)", r"$d_2 < d_1 \Rightarrow F_2 > F_1\text{ (lợi về đường đi)}$", r"Ví dụ: đôi đũa, kẹp gắp đá, cơ cẳng tay người"),
            ),
        ],
        "example": r"Một người dùng xà beng dài $1{,}5\text{ m}$ làm đòn bẩy để bẩy một tảng đá nặng $F_1 = 1200\text{ N}$. Biết điểm tựa $O$ cách đầu xà beng tì vào tảng đá một đoạn $d_1 = 0{,}25\text{ m}$ và người đó tác dụng lực vuông góc tại đầu còn lại của xà beng (cách điểm tựa $d_2 = 1{,}5 - 0{,}25 = 1{,}25\text{ m}$). Tính moment của trọng lực tảng đá đối với $O$ và độ lớn lực tối thiểu $F_2$ mà người đó cần tác dụng.",
        "example_answer": r"""- Moment của lực $F_1$ do tảng đá đè lên đầu xà beng đối với điểm tựa $O$ là:
$$M_1 = F_1 \cdot d_1 = 1200 \cdot 0{,}25 = 300\text{ N}\cdot\text{m}$$
- Để nâng được tảng đá, moment lực $M_2$ của người phải cân bằng với $M_1$:
$$F_2 \cdot d_2 = M_1 \Rightarrow F_2 = \dfrac{M_1}{d_2} = \dfrac{300}{1{,}25} = 240\text{ N}$$
(Nhờ đòn bẩy có $d_2 = 5d_1$, người đó được lợi $5$ lần về lực).""",
        "real_life": r"""- **Dụng cụ cơ khí và gia đình**: Tay nắm cửa luôn lắp ở mép xa bản lề để tăng cánh tay đòn $d$; dùng cờ-lê cán dài hoặc nối thêm ống thép vào tay vặn để tạo moment lực lớn khi tháo bu-lông rỉ sét.
- **Sinh học cơ thể người**: Hầu hết các khớp xương trên cơ thể người (khớp cổ, khớp khuỷu tay, khớp bàn chân) hoạt động như các hệ đòn bẩy tinh vi.""",
        "game_title": "Thử thách thực tế: Moment lực và Đòn bẩy",
        "game_description": "Điều chỉnh vị trí điểm tựa, chiều dài cánh tay đòn và các quả nặng để thiết lập trạng thái cân bằng moment lực.",
        "game_type": "game_moment_luc_don_bay",
        "quiz": [
            mcq(
                "biet",
                r"Đại lượng vật lí đặc trưng cho tác dụng làm quay của một lực quanh một trục hay điểm tựa cố định được gọi là gì?",
                [r"Áp suất của lực", r"Moment lực", r"Cường độ lực", r"Trọng lượng riêng"],
                1,
                r"Tác dụng làm quay của lực quanh một điểm hoặc một trục quay được đặc trưng bằng moment lực ($M = F \cdot d$).",
            ),
            mcq(
                "biet",
                r"Đơn vị đo của moment lực trong hệ đo lường quốc tế SI là:",
                [r"$\text{N/m}$", r"$\text{N/m}^2$", r"$\text{N}\cdot\text{m}$", r"$\text{J/s}$"],
                2,
                r"Từ công thức $M = F \cdot d$ với $F$ tính bằng $\text{N}$ và $d$ tính bằng $\text{m}$, đơn vị của moment lực là niu-tơn mét ($\text{N}\cdot\text{m}$).",
            ),
            mcq(
                "biet",
                r"Trường hợp nào sau đây lực tác dụng lên cánh cửa KHÔNG làm cánh cửa quay quanh bản lề?",
                [
                    r"Đẩy vuông góc vào tay nắm cửa ở xa bản lề",
                    r"Kéo vuông góc vào chính giữa cánh cửa",
                    r"Tác dụng lực có giá đi xuyên qua trục bản lề của cánh cửa",
                    r"Đẩy vuông góc vào mép ngoài của cánh cửa",
                ],
                2,
                r"Khi giá của lực cắt (hoặc đi qua) trục quay bản lề thì cánh tay đòn $d = 0$, nên moment lực $M = 0$ và lực không làm quay cửa.",
            ),
            mcq(
                "biet",
                r"Dụng cụ nào dưới đây là ứng dụng của đòn bẩy có điểm tựa nằm ở một đầu và vật chịu lực nằm ở giữa (luôn cho lợi về lực)?",
                [r"Chiếc bập bênh ngoài công viên", r"Xe rùa đẩy gạch xây dựng", r"Đôi đũa gắp thức ăn", r"Chiếc cân đòn (cân Roberval)"],
                1,
                r"Xe rùa có trục bánh xe ở mũi xe là điểm tựa $O$, thùng hàng ở giữa và tay người nâng ở càng xe phía sau nên luôn có $d_2 > d_1$, cho lợi về lực.",
            ),
            mcq(
                "hieu",
                r"Một người dùng cờ-lê để vặn một đai ốc với lực $F = 50\text{ N}$ có phương vuông góc với thân cờ-lê tại điểm cách tâm đai ốc một khoảng $d = 20\text{ cm}$. Moment của lực đó đối với tâm đai ốc bằng:",
                [r"$1000\text{ N}\cdot\text{m}$", r"$10\text{ N}\cdot\text{m}$", r"$2{,}5\text{ N}\cdot\text{m}$", r"$100\text{ N}\cdot\text{m}$"],
                1,
                r"Đổi $d = 20\text{ cm} = 0{,}2\text{ m}$. Moment lực là $M = F \cdot d = 50 \cdot 0{,}2 = 10\text{ N}\cdot\text{m}$.",
            ),
            mcq(
                "hieu",
                r"Hai bạn An (trọng lượng $P_1 = 450\text{ N}$) và Bình (trọng lượng $P_2 = 300\text{ N}$) ngồi ở hai bên của một chiếc bập bênh. Biết An ngồi cách trục quay ở giữa một đoạn $d_1 = 1{,}2\text{ m}$. Để bập bênh cân bằng nằm ngang thì Bình phải ngồi cách trục quay một đoạn $d_2$ bằng:",
                [r"$0{,}8\text{ m}$", r"$1{,}5\text{ m}$", r"$1{,}8\text{ m}$", r"$2{,}0\text{ m}$"],
                2,
                r"Áp dụng điều kiện cân bằng đòn bẩy: $P_1 \cdot d_1 = P_2 \cdot d_2 \Rightarrow d_2 = \dfrac{450 \cdot 1{,}2}{300} = 1{,}8\text{ m}$.",
            ),
            tf4(
                "hieu",
                r"Xét một thanh đòn bẩy cứng nhẹ $AB$ có điểm tựa cố định tại $O$ nằm trong khoảng $AB$ với $OA = 30\text{ cm}$ và $OB = 90\text{ cm}$. Tại đầu $A$ treo một vật nặng có trọng lượng $F_1 = 120\text{ N}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Đòn bẩy này thuộc loại đòn bẩy có điểm tựa ở giữa (đòn bẩy loại 1).",
                    r"b) Cánh tay đòn của lực tại $B$ lớn gấp $3$ lần cánh tay đòn của lực tại $A$.",
                    r"c) Để giữ cho thanh đòn bẩy cân bằng nằm ngang, cần tác dụng thẳng đứng xuống dưới tại đầu $B$ một lực $F_2 = 360\text{ N}$.",
                    r"d) Nếu dịch chuyển điểm tựa $O$ ra xa đầu $A$ hơn (tăng $OA$, giảm $OB$) thì lực $F_2$ cần thiết ở đầu $B$ sẽ phải tăng lên.",
                ],
                [True, True, False, True],
                r"a) Đúng vì $O$ nằm giữa $A$ và $B$. b) Đúng vì $\dfrac{OB}{OA} = \dfrac{90}{30} = 3$. c) Sai vì $F_2 = F_1 \cdot \dfrac{OA}{OB} = 120 \cdot \dfrac{30}{90} = 40\text{ N}$. d) Đúng vì khi $OA$ tăng và $OB$ giảm thì tỉ số $\dfrac{OA}{OB}$ tăng nên $F_2 = F_1 \cdot \dfrac{OA}{OB}$ tăng.",
            ),
            tf4(
                "hieu",
                r"Xét các hệ đòn bẩy trên cơ thể người và các dụng cụ quen thuộc. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Khi dùng cẳng tay nâng một quả tạ trong lòng bàn tay, khớp khuỷu tay đóng vai trò là điểm tựa của đòn bẩy.",
                    r"b) Khi dùng kìm cắt dây thép cứng, người ta thường đặt sợi dây thép vào sát trục quay của kìm để giảm cánh tay đòn của lực cản.",
                    r"c) Đôi đũa khi gắp thức ăn giúp ta lợi về lực vì điểm đặt ngón tay gần điểm tựa hơn miếng thức ăn.",
                    r"d) Tay nắm cửa được lắp càng gần bản lề thì việc mở cửa càng nhẹ nhàng.",
                ],
                [True, True, False, False],
                r"a) Đúng vì cẳng tay quay quanh khớp khuỷu tay. b) Đúng vì giảm $d_1$ giúp lực cắt ở mũi kìm lớn hơn nhiều lần lực bóp của tay. c) Sai vì đôi đũa có $d_{\text{tay}} < d_{\text{vật}}$ nên thiệt về lực nhưng lợi về đường đi và sự linh hoạt. d) Sai vì lắp gần bản lề làm cánh tay đòn $d$ nhỏ nên cần lực rất lớn mới mở được cửa.",
            ),
            mcq(
                "vandung",
                r"Một người gánh hai thúng hàng trên một chiếc đòn gánh dài $1{,}5\text{ m}$ (bỏ qua khối lượng đòn gánh). Thúng gạo ở đầu $A$ nặng $P_1 = 300\text{ N}$, thúng ngô ở đầu $B$ nặng $P_2 = 200\text{ N}$. Để đòn gánh cân bằng nằm ngang, vai người đó (điểm tựa $O$) phải đặt cách đầu $A$ (thúng gạo) một khoảng bằng:",
                [r"$0{,}6\text{ m}$", r"$0{,}9\text{ m}$", r"$0{,}75\text{ m}$", r"$0{,}5\text{ m}$"],
                0,
                r"Gọi khoảng cách từ vai $O$ đến đầu $A$ là $d_1 = x$ ($\text{m}$), suy ra khoảng cách đến đầu $B$ là $d_2 = 1{,}5 - x$ ($\text{m}$). Điều kiện cân bằng: $P_1 \cdot d_1 = P_2 \cdot d_2 \iff 300x = 200(1{,}5 - x) \iff 500x = 300 \Rightarrow x = 0{,}6\text{ m}$.",
            ),
            short(
                "vandung",
                r"Một thanh chắn đường sắt đồng chất dài $AB = 4\text{ m}$ có trục quay cố định tại $O$ cách đầu $A$ một đoạn $OA = 0{,}5\text{ m}$. Để giữ thanh cân bằng nằm ngang, người ta gắn vào đầu $A$ một đối trọng có trọng lượng $F_1 = 700\text{ N}$. Biết trọng lực $P$ của bản thân thanh chắn đặt tại chính giữa thanh (trung điểm $G$ của $AB$). Tính trọng lượng $P$ của thanh chắn theo đơn vị $\text{N}$.",
                ["233", "233,3", "233.3"],
                r"Trung điểm $G$ của thanh cách đầu $A$ một đoạn $AG = \dfrac{4}{2} = 2\text{ m}$, nên khoảng cách từ trục quay $O$ đến giá của trọng lực $P$ tại $G$ là $d_2 = OG = AG - OA = 2 - 0{,}5 = 1{,}5\text{ m}$. Áp dụng quy tắc cân bằng moment lực quanh $O$: $F_1 \cdot OA = P \cdot OG \iff 700 \cdot 0{,}5 = P \cdot 1{,}5 \Rightarrow P = \dfrac{350}{1{,}5} \approx 233{,}3\text{ N}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 5: CƠ NĂNG, CÔNG VÀ CÔNG SUẤT CƠ HỌC =====================
    {
        "topic": "cong-suat",
        "title": "Cơ năng, Công và Công suất cơ học",
        "icon": "⚙️",
        "description": "Chuyên đề Cơ học KHTN 8 – 9 Kết nối tri thức với cuộc sống: Khái niệm cơ năng (động năng, thế năng), điều kiện xuất hiện công cơ học, công thức tính công và công suất, định luật về công và hiệu suất máy cơ đơn giản.",
        "requirements": [
            r"Phân tích được sự chuyển hóa giữa động năng và thế năng của vật trong một số hiện tượng cơ học.",
            r"Nêu được điều kiện để có công cơ học và tính được công cơ học theo công thức $A = F \cdot s$ khi lực cùng hướng với chuyển dời.",
            r"Nêu được ý nghĩa vật lí của công suất (tốc độ thực hiện công), liệt kê được các đơn vị đo công suất ($\text{W}$, $\text{kW}$, $\text{MW}$, $\text{HP}$) và vận dụng được công thức $\mathcal{P} = \dfrac{A}{t} = F \cdot v$.",
            r"Vận dụng được định luật về công và tính được hiệu suất của các máy cơ đơn giản (mặt phẳng nghiêng, đòn bẩy, ròng rọc) trong thực tế.",
        ],
        "definition": r"""- **Công cơ học** ($A$) của một lực không đổi $F$ làm vật dịch chuyển một quãng đường $s$ theo đúng hướng của lực được xác định bởi: $A = F \cdot s$ (đơn vị: jun, kí hiệu $\text{J}$, với $1\text{ J} = 1\text{ N}\cdot\text{m}$).
- **Công suất** ($\mathcal{P}$) là đại lượng đặc trưng cho tốc độ thực hiện công, được xác định bằng công thực hiện được trong một đơn vị thời gian: $\mathcal{P} = \dfrac{A}{t} = F \cdot v$ (đơn vị: oát, kí hiệu $\text{W}$, với $1\text{ W} = 1\text{ J/s}$).""",
        "theory": r"""### Bài 1. Cơ năng (Động năng và Thế năng)
- **Thế năng trọng trường và thế năng đàn hồi**: Vật ở độ cao $h$ so với mặt đất (hoặc mốc chọn trước) có thế năng trọng trường $W_{\text{t}} = P \cdot h = 10m \cdot h$; vật bị biến dạng đàn hồi (như lò xo bị nén hoặc giãn, cánh cung giương lên) dự trữ thế năng đàn hồi.
- **Động năng**: Năng lượng vật có được do chuyển động gọi là động năng ($W_{\text{đ}} = \dfrac{1}{2}mv^2$). Khối lượng vật càng lớn và tốc độ chuyển động càng nhanh thì động năng càng lớn. Tổng động năng và thế năng của vật gọi là **cơ năng**: $W = W_{\text{đ}} + W_{\text{t}}$.
### Bài 2. Công cơ học và Định luật về công
- **Điều kiện xuất hiện công cơ học**: Chỉ có công cơ học khi có lực tác dụng vào vật và làm cho vật dịch chuyển (nếu $s = 0$ hoặc lực vuông góc với phương dịch chuyển thì công bằng $0$). Khi lực $F$ cùng hướng dịch chuyển: $A = F \cdot s$. Khi nâng đều vật có trọng lượng $P$ lên độ cao $h$: $A = P \cdot h$.
- **Định luật về công**: Không một máy cơ đơn giản nào (mặt phẳng nghiêng, đòn bẩy, ròng rọc động) cho ta lợi về công. Được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi và ngược lại: $A_1 = A_2 \iff F_1 \cdot s_1 = F_2 \cdot s_2$.
- **Hiệu suất máy cơ**: Trong thực tế luôn có ma sát nên công toàn phần $A_{\text{tp}}$ luôn lớn hơn công có ích $A_{\text{ích}}$ ($A_{\text{tp}} = A_{\text{ích}} + A_{\text{hp}}$). Hiệu suất là $H = \dfrac{A_{\text{ích}}}{A_{\text{tp}}} \cdot 100\%$.
### Bài 3. Công suất cơ học
- **Khái niệm và công thức**: Để biết máy nào hay người nào làm việc khỏe hơn (thực hiện công nhanh hơn), người ta tính công thực hiện trong $1\text{ s}$ gọi là công suất: $\mathcal{P} = \dfrac{A}{t}$. Nếu vật chuyển động đều với tốc độ $v = \dfrac{s}{t}$ dưới tác dụng của lực kéo $F$ cùng hướng thì $\mathcal{P} = \dfrac{F \cdot s}{t} = F \cdot v$.
- **Đơn vị đo**: $1\text{ W} = 1\text{ J/s}$; $1\text{ kW} = 1000\text{ W}$; $1\text{ MW} = 10^6\text{ W}$; $1\text{ HP}\text{ (mã lực)} \approx 746\text{ W}$.""",
        "formulas": [
            G(
                "I. Công cơ học và công suất cơ học",
                F("Công cơ học khi lực cùng hướng chuyển dời", r"$A = F \cdot s;\quad A_{\text{nâng}} = P \cdot h = 10m \cdot h$", r"$A$ ($\text{J}$), $F$ ($\text{N}$), $s$ ($\text{m}$); $1\text{ kJ} = 1000\text{ J}$"),
                F("Công suất cơ học", r"$\mathcal{P} = \dfrac{A}{t} = F \cdot v$", r"$\mathcal{P}$ ($\text{W}$), $t$ ($\text{s}$), $v$ ($\text{m/s}$); $1\text{ kW} = 1000\text{ W}$"),
            ),
            G(
                "II. Định luật về công và hiệu suất máy cơ đơn giản",
                F("Mặt phẳng nghiêng lí tưởng (bỏ qua ma sát)", r"$F \cdot l = P \cdot h \Rightarrow F = P \cdot \dfrac{h}{l}$", r"$l$: chiều dài mặt phẳng nghiêng, $h$: chiều cao nâng vật"),
                F("Ròng rọc động lí tưởng", r"$F = \dfrac{P}{2};\quad s = 2h$", r"Lợi $2$ lần về lực thì thiệt $2$ lần về đường đi"),
                F("Hiệu suất của máy cơ thực tế", r"$H = \dfrac{A_{\text{ích}}}{A_{\text{tp}}} \cdot 100\% = \dfrac{P \cdot h}{F \cdot l} \cdot 100\%$", r"$A_{\text{tp}} = A_{\text{ích}} + A_{\text{ma sát}}$"),
            ),
        ],
        "example": r"Một cần cẩu nâng đều một kiện hàng có khối lượng $m = 1{,}5\text{ tấn}$ lên độ cao $h = 8\text{ m}$ trong thời gian $t = 20\text{ s}$. Tính công có ích mà cần cẩu đã thực hiện và công suất nâng hàng của cần cẩu (lấy $P = 10m$).",
        "example_answer": r"""- Đổi khối lượng $m = 1{,}5\text{ tấn} = 1500\text{ kg}$, suy ra trọng lượng kiện hàng là:
$$P = 10m = 10 \cdot 1500 = 15000\text{ N}$$
- Công cơ học cần cẩu thực hiện để nâng đều kiện hàng lên cao $8\text{ m}$ là:
$$A = P \cdot h = 15000 \cdot 8 = 120000\text{ J} = 120\text{ kJ}$$
- Công suất nâng hàng của cần cẩu là:
$$\mathcal{P} = \dfrac{A}{t} = \dfrac{120000}{20} = 6000\text{ W} = 6\text{ kW}$$""",
        "real_life": r"""- **Giao thông và cơ giới hóa**: Đánh giá sức kéo và tốc độ của đầu máy xe lửa, ô tô, máy bơm nước, thang máy chung cư thông qua chỉ số công suất ($\text{kW}$ hoặc mã lực $\text{HP}$).
- **Lao động và xây dựng**: Dùng cầu dẫn (mặt phẳng nghiêng) để đưa xe máy vào nhà hoặc dùng hệ thống pa-lăng ròng rọc để kéo vật liệu nặng lên tầng cao.""",
        "game_title": "Thử thách thực tế: Công và Công suất",
        "game_description": "Lựa chọn công suất động cơ, hệ ròng rọc và mặt phẳng nghiêng để nâng kiện hàng lên độ cao yêu cầu với hiệu suất tối ưu.",
        "game_type": "game_congsuat",
        "quiz": [
            mcq(
                "biet",
                r"Trong trường hợp nào dưới đây có công cơ học của lực được nhắc tới?",
                [
                    r"Một lực sĩ đang đứng yên giữ quả tạ ở trên cao",
                    r"Trọng lực tác dụng lên hòn bi đang lăn trên mặt bàn phẳng nằm ngang",
                    r"Lực kéo của đầu tàu hỏa làm đoàn tàu chuyển động trên đường ray",
                    r"Một học sinh dùng tay đẩy mạnh vào bức tường bê tông nhưng tường không dịch chuyển",
                ],
                2,
                r"Chỉ có công cơ học khi có lực tác dụng vào vật và làm vật dịch chuyển theo phương không vuông góc với lực.",
            ),
            mcq(
                "biet",
                r"Đơn vị đo công suất trong hệ đo lường quốc tế SI là oát ($\text{W}$). Một oát ($1\text{ W}$) bằng:",
                [r"$1\text{ J}\cdot\text{s}$", r"$1\text{ J/s}$", r"$1\text{ N}\cdot\text{m}$", r"$1\text{ N/s}$"],
                1,
                r"Từ công thức $\mathcal{P} = \dfrac{A}{t}$, với $A$ đo bằng $\text{J}$ và $t$ đo bằng $\text{s}$, ta có $1\text{ W} = 1\text{ J/s}$.",
            ),
            mcq(
                "biet",
                r"Phát biểu nào sau đây là ĐÚNG về định luật về công đối với các máy cơ đơn giản?",
                [
                    r"Ròng rọc động vừa cho lợi $2$ lần về lực vừa cho lợi $2$ lần về đường đi",
                    r"Mặt phẳng nghiêng giúp ta thực hiện công ít hơn so với nâng trực tiếp",
                    r"Không một máy cơ đơn giản nào cho ta lợi về công; được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi",
                    r"Đòn bẩy luôn cho lợi về công cơ học",
                ],
                2,
                r"Theo định luật về công, không một máy cơ đơn giản nào cho lợi về công: được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi và ngược lại.",
            ),
            mcq(
                "biet",
                r"Nếu một vật chuyển động thẳng đều với tốc độ $v$ dưới tác dụng của lực kéo $F$ cùng hướng chuyển động thì công suất của lực kéo được tính bằng công thức nào?",
                [r"$\mathcal{P} = \dfrac{F}{v}$", r"$\mathcal{P} = F \cdot v$", r"$\mathcal{P} = \dfrac{v}{F}$", r"$\mathcal{P} = F \cdot v^2$"],
                1,
                r"Ta có $\mathcal{P} = \dfrac{A}{t} = \dfrac{F \cdot s}{t} = F \cdot v$.",
            ),
            mcq(
                "hieu",
                r"Một người dùng một ròng rọc động (bỏ qua ma sát và khối lượng ròng rọc) để nâng đều một thùng vữa có trọng lượng $P = 400\text{ N}$ lên cao $h = 3\text{ m}$. Lực kéo dây $F$ và quãng đường đầu dây phải kéo đi $s$ lần lượt là:",
                [
                    r"$F = 200\text{ N}$ và $s = 6\text{ m}$",
                    r"$F = 200\text{ N}$ và $s = 3\text{ m}$",
                    r"$F = 400\text{ N}$ và $s = 6\text{ m}$",
                    r"$F = 800\text{ N}$ và $s = 1{,}5\text{ m}$",
                ],
                0,
                r"Dùng ròng rọc động cho ta lợi $2$ lần về lực ($F = \dfrac{P}{2} = \dfrac{400}{2} = 200\text{ N}$) và thiệt $2$ lần về đường đi ($s = 2h = 2 \cdot 3 = 6\text{ m}$).",
            ),
            mcq(
                "hieu",
                r"Một máy bơm nước thực hiện một công $A = 360\text{ kJ}$ trong thời gian $t = 2\text{ phút}$. Công suất của máy bơm đó là:",
                [r"$180\text{ W}$", r"$3000\text{ W}$", r"$180\text{ kW}$", r"$720\text{ W}$"],
                1,
                r"Đổi $A = 360\text{ kJ} = 360000\text{ J}$ và $t = 2\text{ phút} = 120\text{ s}$. Công suất của máy bơm là $\mathcal{P} = \dfrac{A}{t} = \dfrac{360000}{120} = 3000\text{ W}$.",
            ),
            tf4(
                "hieu",
                r"Người ta dùng một mặt phẳng nghiêng dài $l = 5\text{ m}$ để kéo đều một thùng hàng có trọng lượng $P = 600\text{ N}$ lên sàn xe tải cao $h = 1{,}2\text{ m}$. Biết lực kéo thực tế dọc theo mặt phẳng nghiêng là $F = 180\text{ N}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Công có ích để đưa thùng hàng lên độ cao $1{,}2\text{ m}$ là $A_{\text{ích}} = 720\text{ J}$.",
                    r"b) Công toàn phần của lực kéo trên mặt phẳng nghiêng là $A_{\text{tp}} = 900\text{ J}$.",
                    r"c) Nếu không có ma sát trên mặt phẳng nghiêng thì lực kéo chỉ cần bằng $144\text{ N}$.",
                    r"d) Hiệu suất của mặt phẳng nghiêng trong trường hợp này là $75\%$.",
                ],
                [True, True, True, False],
                r"a) Đúng vì $A_{\text{ích}} = P \cdot h = 600 \cdot 1{,}2 = 720\text{ J}$. b) Đúng vì $A_{\text{tp}} = F \cdot l = 180 \cdot 5 = 900\text{ J}$. c) Đúng vì nếu không có ma sát thì $F_0 = \dfrac{A_{\text{ích}}}{l} = \dfrac{720}{5} = 144\text{ N}$. d) Sai vì hiệu suất là $H = \dfrac{A_{\text{ích}}}{A_{\text{tp}}} \cdot 100\% = \dfrac{720}{900} \cdot 100\% = 80\%$.",
            ),
            tf4(
                "hieu",
                r"Một quả bóng có khối lượng $m = 0{,}4\text{ kg}$ được thả rơi từ độ cao $h = 5\text{ m}$ xuống mặt đất. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Khi bắt đầu thả ở độ cao $5\text{ m}$, quả bóng có thế năng trọng trường cực đại và động năng bằng $0$.",
                    r"b) Trong quá trình quả bóng rơi xuống, thế năng trọng trường tăng dần còn động năng giảm dần.",
                    r"c) Công của trọng lực thực hiện khi quả bóng rơi từ độ cao $5\text{ m}$ tới mặt đất là $A = 20\text{ J}$ (lấy $P = 10m$).",
                    r"d) Nếu quả bóng rơi mất thời gian $t = 1\text{ s}$ thì công suất trung bình của trọng lực trong thời gian rơi là $20\text{ W}$.",
                ],
                [True, False, True, True],
                r"a) Đúng vì lúc vừa buông tay $v = 0$ nên $W_{\text{đ}} = 0$ và độ cao $h$ lớn nhất nên $W_{\text{t}}$ cực đại. b) Sai vì khi rơi xuống độ cao giảm còn tốc độ tăng nên thế năng chuyển hóa thành động năng ($W_{\text{t}}$ giảm, $W_{\text{đ}}$ tăng). c) Đúng vì $P = 10 \cdot 0{,}4 = 4\text{ N} \Rightarrow A = P \cdot h = 4 \cdot 5 = 20\text{ J}$. d) Đúng vì $\mathcal{P} = \dfrac{A}{t} = \dfrac{20}{1} = 20\text{ W}$.",
            ),
            mcq(
                "vandung",
                r"Một động cơ ô tô có công suất không đổi $\mathcal{P} = 45\text{ kW}$ đang kéo xe chuyển động thẳng đều trên đường nằm ngang với tốc độ $v = 54\text{ km/h}$. Độ lớn của lực kéo do động cơ tạo ra là:",
                [r"$833{,}3\text{ N}$", r"$2430\text{ N}$", r"$3000\text{ N}$", r"$1500\text{ N}$"],
                2,
                r"Đổi $\mathcal{P} = 45\text{ kW} = 45000\text{ W}$ và tốc độ $v = 54\text{ km/h} = \dfrac{54}{3{,}6} = 15\text{ m/s}$. Lực kéo của động cơ là $F = \dfrac{\mathcal{P}}{v} = \dfrac{45000}{15} = 3000\text{ N}$.",
            ),
            short(
                "vandung",
                r"Một máy kéo dùng dây cáp kéo một kiện gỗ trượt đều trên mặt phẳng nghiêng dài $l = 10\text{ m}$ để lên cao $h = 3\text{ m}$ trong thời gian $t = 25\text{ s}$. Biết kiện gỗ có trọng lượng $P = 2000\text{ N}$ và hiệu suất của mặt phẳng nghiêng là $H = 80\%$. Tính công suất $\mathcal{P}$ của máy kéo theo đơn vị $\text{W}$.",
                ["300"],
                r"Công có ích để nâng kiện gỗ là $A_{\text{ích}} = P \cdot h = 2000 \cdot 3 = 6000\text{ J}$. Công toàn phần máy kéo thực hiện là $A_{\text{tp}} = \dfrac{A_{\text{ích}}}{H} = \dfrac{6000}{0{,}8} = 7500\text{ J}$. Công suất của máy kéo là $\mathcal{P} = \dfrac{A_{\text{tp}}}{t} = \dfrac{7500}{25} = 300\text{ W}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 6: NHIỆT NĂNG =====================
    {
        "topic": "nhiet-nang",
        "title": "Năng lượng nhiệt, Nội năng, Sự truyền nhiệt và Sự nở vì nhiệt",
        "icon": "🔥",
        "description": "Chương VI · SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống (Bài 26 – Bài 29): Năng lượng nhiệt, nội năng, thực hành đo năng lượng nhiệt bằng Joulemeter, ba hình thức truyền nhiệt (dẫn nhiệt, đối lưu, bức xạ nhiệt) và sự nở vì nhiệt của các chất.",
        "requirements": [
            r"Nêu được khái niệm năng lượng nhiệt, khái niệm nội năng và giải thích được khi nhiệt độ của vật càng cao thì các phân tử cấu tạo nên vật chuyển động càng nhanh và nội năng của vật càng lớn.",
            r"Thực hiện được thí nghiệm đo năng lượng nhiệt mà vật nhận được khi đun nước bằng dụng cụ thực hành (oát kế hoặc Joulemeter).",
            r"Lấy được ví dụ và phân biệt được ba hình thức truyền nhiệt: dẫn nhiệt, đối lưu, bức xạ nhiệt; giải thích được một số hiện tượng truyền nhiệt và cách nhiệt trong thực tế.",
            r"Thực hiện thí nghiệm để chứng tỏ được các chất khác nhau nở vì nhiệt khác nhau (chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn) và nêu được công dụng, tác hại của sự nở vì nhiệt.",
        ],
        "definition": r"""- **Năng lượng nhiệt** là năng lượng mà vật có được nhờ chuyển động nhiệt của các phân tử. Phần năng lượng nhiệt mà vật nhận thêm hay mất đi trong quá trình truyền nhiệt gọi là **nhiệt lượng** ($Q$, đơn vị $\text{J}$).
- **Nội năng** của một vật là tổng động năng và thế năng của các phân tử, nguyên tử cấu tạo nên vật.
- **Ba hình thức truyền nhiệt**: dẫn nhiệt (chủ yếu ở chất rắn), đối lưu (ở chất lỏng và chất khí) và bức xạ nhiệt (truyền bằng các tia nhiệt đi thẳng, truyền được cả trong chân không).""",
        "theory": r"""### Bài 26. Năng lượng nhiệt và nội năng
- **Chuyển động nhiệt và nội năng**: Các phân tử, nguyên tử cấu tạo nên vật chuyển động hỗn độn không ngừng nên có động năng; đồng thời giữa chúng có lực tương tác phân tử nên có thế năng. Tổng động năng và thế năng của các hạt phân tử, nguyên tử cấu tạo nên vật gọi là **nội năng** của vật.
- **Mối liên hệ với nhiệt độ**: Khi một vật được làm nóng, nhiệt độ của vật tăng lên, các phân tử chuyển động hỗn độn nhanh hơn nên động năng phân tử và nội năng của vật tăng lên. Hai cách làm thay đổi nội năng của vật là **thực hiện công** (như cọ xát đồng xu trên mặt bàn) và **truyền nhiệt** (như nhúng thìa vào cốc nước nóng).
### Bài 27. Thực hành đo năng lượng nhiệt bằng Joulemeter
- **Nguyên tắc đo**: Đun nóng một lượng nước trong bình nhiệt lượng kế bằng dây điện trở nối với nguồn điện qua Joulemeter (dụng cụ đo năng lượng điện tiêu thụ chuyển hóa thành nhiệt năng truyền cho nước).
- **Kết quả thực nghiệm**: Nhiệt lượng $Q$ mà một lượng chất thu vào để nóng lên tỉ lệ thuận với khối lượng $m$ của vật, độ tăng nhiệt độ $\Delta t = t_2 - t_1$ và phụ thuộc vào bản chất của chất làm vật (thể hiện qua nhiệt dung riêng $c$): $Q = m \cdot c \cdot \Delta t$.
### Bài 28. Sự truyền nhiệt
- **Dẫn nhiệt**: Sự truyền năng lượng nhiệt từ phần này sang phần khác của một vật hoặc từ vật này sang vật khác khi tiếp xúc trực tiếp. Đây là hình thức truyền nhiệt chủ yếu của **chất rắn**. Kim loại (bạc, đồng, nhôm) dẫn nhiệt rất tốt; chất lỏng, chất khí và các vật liệu xốp như gỗ, len, bông, thủy tinh, nhựa dẫn nhiệt rất kém (dùng để cách nhiệt).
- **Đối lưu**: Sự truyền nhiệt bằng các dòng chất lỏng hoặc chất khí dịch chuyển (phần chất lỏng hoặc chất khí nóng hơn nở ra, khối lượng riêng giảm nên đi lên trên; phần lạnh hơn nặng hơn chìm xuống dưới tạo thành dòng đối lưu). Đây là hình thức truyền nhiệt chủ yếu của **chất lỏng và chất khí**; đối lưu không xảy ra trong chất rắn và chân không.
- **Bức xạ nhiệt**: Sự truyền nhiệt bằng các tia nhiệt đi thẳng. Bức xạ nhiệt xảy ra được cả trong **chân không** (như năng lượng nhiệt từ Mặt Trời truyền tới Trái Đất). Vật có bề mặt sẫm màu và xù xì hấp thụ cũng như phát xạ tia nhiệt tốt hơn vật có bề mặt sáng màu và nhẵn bóng.
### Bài 29. Sự nở vì nhiệt
- **Đặc điểm sự nở vì nhiệt của các chất**: Hầu hết các chất rắn, lỏng, khí đều **nở ra khi nóng lên** và **co lại khi lạnh đi**. Các chất rắn khác nhau, chất lỏng khác nhau thì nở vì nhiệt khác nhau (ví dụ: nhôm nở vì nhiệt nhiều hơn đồng, đồng nhiều hơn sắt; rượu nở vì nhiệt nhiều hơn dầu, dầu nhiều hơn nước). Ngược lại, **các chất khí khác nhau nở vì nhiệt giống nhau**.
- **So sánh mức độ nở vì nhiệt**: Chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn. Khi sự co giãn vì nhiệt của vật rắn bị ngăn cản, nó sẽ gây ra những lực rất lớn (làm cong đường ray, nứt dầm cầu bê tông).
- **Ứng dụng**: Chế tạo băng kép (gồm hai thanh kim loại có bản chất khác nhau như đồng và thép tán chặt vào nhau; khi bị đốt nóng băng kép luôn cong về phía kim loại nở vì nhiệt ít hơn là thép) dùng làm rơ-le tự động đóng ngắt mạch điện trong bàn là, ấm đun nước; để khe hở ở chỗ tiếp nối thanh ray tàu hỏa và gối đỡ hai đầu cầu.""",
        "formulas": [
            G(
                "I. Nhiệt lượng và cân bằng nhiệt",
                F("Nhiệt lượng thu vào hoặc tỏa ra", r"$Q = m \cdot c \cdot \Delta t = m \cdot c \cdot |t_2 - t_1|$", r"$Q$ ($\text{J}$), $m$ ($\text{kg}$), $c$: nhiệt dung riêng ($\text{J/(kg}\cdot\text{K)}$), $\Delta t$ (${}^\circ\text{C}$ hoặc $\text{K}$)"),
                F("Phương trình cân bằng nhiệt (bỏ qua hao phí)", r"$Q_{\text{tỏa}} = Q_{\text{thu}} \iff m_1 c_1 (t_1 - t) = m_2 c_2 (t - t_2)$", r"$t$: nhiệt độ khi có cân bằng nhiệt ($t_2 < t < t_1$)"),
            ),
            G(
                "II. Ba hình thức truyền nhiệt và sự nở vì nhiệt",
                F("Hình thức truyền nhiệt chủ yếu theo môi trường", r"$\text{Rắn: Dẫn nhiệt};\quad \text{Lỏng, Khí: Đối lưu};\quad \text{Chân không: Bức xạ nhiệt}$", r""),
                F("So sánh độ nở vì nhiệt của ba thể", r"$\text{Chất khí} > \text{Chất lỏng} > \text{Chất rắn}$", r"Các chất khí khác nhau nở vì nhiệt giống nhau"),
                F("Quy tắc uốn cong của băng kép (Đồng – Thép)", r"$t \text{ tăng} \Rightarrow \text{cong về phía Thép};\quad t \text{ giảm} \Rightarrow \text{cong về phía Đồng}$", r"Vì đồng nở và co vì nhiệt nhiều hơn thép"),
            ),
        ],
        "example": r"Dùng ấm điện đun nóng $m = 1{,}5\text{ kg}$ nước từ nhiệt độ ban đầu $t_1 = 20^\circ\text{C}$ đến khi nước sôi ở $t_2 = 100^\circ\text{C}$. Biết nhiệt dung riêng của nước là $c = 4200\text{ J/(kg}\cdot\text{K)}$. Tính nhiệt lượng mà nước đã thu vào.",
        "example_answer": r"""- Độ tăng nhiệt độ của nước là:
$$\Delta t = t_2 - t_1 = 100 - 20 = 80^\circ\text{C}$$
- Nhiệt lượng mà $1{,}5\text{ kg}$ nước đã thu vào để sôi là:
$$Q = m \cdot c \cdot \Delta t = 1{,}5 \cdot 4200 \cdot 80 = 504000\text{ J} = 504\text{ kJ}$$""",
        "real_life": r"""- **Bình giữ nhiệt (phích nước)**: Gồm hai lớp thủy tinh có lớp chân không ở giữa để ngăn **dẫn nhiệt** và **đối lưu**; mặt trong tráng bạc phản xạ các tia nhiệt để ngăn **bức xạ nhiệt**; nút đậy bằng nhựa hoặc gỗ xốp ngăn đối lưu.
- **Lắp đặt thiết bị và công trình**: Lắp điều hòa làm lạnh ở trên cao và đặt lò sưởi ở dưới thấp để tận dụng dòng đối lưu không khí; tạo khe hở nhiệt trên đường ray, cầu thép và ống dẫn hơi nóng.""",
        "game_title": "Thử thách thực tế: Nhiệt năng và Truyền nhiệt",
        "game_description": "Thử nghiệm các lớp vật liệu cách nhiệt, quan sát dòng đối lưu và sự uốn cong của băng kép khi thay đổi nhiệt độ.",
        "game_type": "game_nhietnang",
        "quiz": [
            mcq(
                "biet",
                r"Khi nhiệt độ của một vật tăng lên thì các phân tử cấu tạo nên vật và nội năng của vật thay đổi như thế nào?",
                [
                    r"Các phân tử chuyển động chậm đi và nội năng của vật giảm",
                    r"Các phân tử chuyển động nhanh hơn và nội năng của vật tăng lên",
                    r"Các phân tử đứng yên và nội năng của vật không đổi",
                    r"Kích thước của mỗi phân tử phình to ra làm nội năng giảm",
                ],
                1,
                r"Nhiệt độ của vật càng cao thì các phân tử chuyển động nhiệt càng nhanh, làm động năng phân tử và nội năng của vật tăng lên.",
            ),
            mcq(
                "biet",
                r"Trong chân không (như khoảng không vũ trụ giữa Mặt Trời và Trái Đất), năng lượng nhiệt được truyền đi bằng hình thức nào?",
                [r"Dẫn nhiệt", r"Đối lưu", r"Bức xạ nhiệt", r"Cả dẫn nhiệt và đối lưu"],
                2,
                r"Dẫn nhiệt và đối lưu đều cần môi trường vật chất (hạt phân tử); chỉ có bức xạ nhiệt mới truyền được qua chân không.",
            ),
            mcq(
                "biet",
                r"Trong các chất: nhôm, nước, rượu và không khí, chất nào nở vì nhiệt nhiều nhất khi cùng tăng thêm một độ tăng nhiệt độ $\Delta t$ như nhau?",
                [r"Nhôm", r"Nước", r"Rượu", r"Không khí"],
                3,
                r"Chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn; do đó không khí nở vì nhiệt nhiều nhất.",
            ),
            mcq(
                "biet",
                r"Một băng kép gồm một thanh đồng và một thanh thép được tán chặt vào nhau. Biết đồng nở vì nhiệt nhiều hơn thép. Khi bị đốt nóng, băng kép sẽ:",
                [
                    r"Cong về phía thanh đồng",
                    r"Cong về phía thanh thép",
                    r"Giữ nguyên hình dạng thẳng",
                    r"Xoắn tròn lại quanh trục dọc",
                ],
                1,
                r"Khi bị đốt nóng, đồng giãn dài ra nhiều hơn thép nên thanh đồng nằm ở phía vòng cung ngoài và đẩy băng kép cong về phía thanh thép.",
            ),
            mcq(
                "hieu",
                r"Tại sao khi đun nước bằng ấm, ta luôn đun từ phía dưới đáy ấm mà không đun từ phía trên miệng ấm?",
                [
                    r"Vì nước dẫn nhiệt tốt hơn kim loại làm đáy ấm",
                    r"Để tạo thành dòng đối lưu: lớp nước ở dưới nóng lên nở ra, nhẹ đi nên nổi lên trên và lớp nước lạnh ở trên chìm xuống dưới giúp cả ấm nước nóng đều",
                    r"Để tăng bức xạ nhiệt qua khoảng chân không trong nước",
                    r"Vì đáy ấm làm bằng chất cách nhiệt",
                ],
                1,
                r"Chất lỏng truyền nhiệt chủ yếu bằng đối lưu; đun từ dưới đáy giúp tạo dòng đối lưu tự nhiên làm nóng toàn bộ lượng nước.",
            ),
            mcq(
                "hieu",
                r"Tại sao vào mùa hè nắng nóng, người ta thường thích mặc áo sáng màu hơn là mặc áo màu đen hoặc màu sẫm?",
                [
                    r"Vì vải sáng màu dẫn nhiệt tốt hơn vải tối màu",
                    r"Vì các vật có bề mặt sáng màu ít hấp thụ các tia nhiệt (bức xạ nhiệt) từ Mặt Trời hơn vật sẫm màu nên đỡ nóng hơn",
                    r"Vì vải tối màu ngăn cản hoàn toàn hiện tượng đối lưu",
                    r"Vì áo sáng màu có khối lượng riêng lớn hơn áo tối màu",
                ],
                1,
                r"Vật có bề mặt sáng màu phản xạ tốt các tia nhiệt và hấp thụ bức xạ nhiệt kém hơn vật sẫm màu nên giúp cơ thể mát hơn dưới nắng.",
            ),
            tf4(
                "hieu",
                r"Xét cấu tạo của một chiếc bình giữ nhiệt (phích nước) dùng để đựng nước nóng. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Lớp chân không ở giữa hai thành bình thủy tinh có tác dụng ngăn cản sự dẫn nhiệt và sự đối lưu nhiệt ra môi trường ngoài.",
                    r"b) Hai mặt đối diện của thành bình thủy tinh được tráng bạc nhẵn bóng nhằm làm tăng sự bức xạ nhiệt ra bên ngoài.",
                    r"c) Nút bình được làm bằng nhựa rỗng hoặc gỗ xốp để hạn chế sự truyền nhiệt bằng đối lưu và dẫn nhiệt ở miệng bình.",
                    r"d) Nếu bình giữ nhiệt bị gãy đầu vòi hút chân không ở đáy làm không khí tràn vào giữa hai lớp thủy tinh thì bình vẫn giữ nhiệt tốt như ban đầu.",
                ],
                [True, False, True, False],
                r"a) Đúng vì chân không không dẫn nhiệt và không đối lưu. b) Sai vì lớp tráng bạc dùng để phản xạ các tia nhiệt trở lại vào trong nước, ngăn cản hao phí do bức xạ nhiệt. c) Đúng. d) Sai vì khi không khí lọt vào sẽ xảy ra dẫn nhiệt và đối lưu qua lớp không khí làm nước nhanh nguội.",
            ),
            tf4(
                "hieu",
                r"Xét các hiện tượng về sự nở vì nhiệt của các chất trong đời sống và kĩ thuật. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Các chất rắn khác nhau nở vì nhiệt khác nhau, còn các chất khí khác nhau (như oxygen, nitrogen, hydrogen) nở vì nhiệt giống nhau.",
                    r"b) Khi rót nước thật sôi vào cốc thủy tinh dày thì cốc dễ bị nứt vỡ hơn cốc thủy tinh mỏng vì lớp thủy tinh bên trong nóng lên nở ra trước trong khi lớp bên ngoài chưa kịp nóng lên.",
                    r"c) Khi đóng các chai nước ngọt có ga trong nhà máy, người ta luôn rót thật đầy tràn tới sát nắp chai để tránh vỡ chai khi trời nóng.",
                    r"d) Chỗ tiếp nối hai đầu thanh ray đường sắt phải để một khe hở nhỏ để khi trời nắng nóng thanh ray nở dài ra không bị cong vênh.",
                ],
                [True, True, False, True],
                r"a) Đúng. b) Đúng vì thủy tinh dẫn nhiệt kém nên cốc dày giãn nở không đều gây lực nội làm vỡ cốc. c) Sai vì người ta phải chừa một khoảng không khí ở cổ chai để khi nhiệt độ tăng chất lỏng nở ra không làm bung nắp hoặc nổ chai. d) Đúng.",
            ),
            mcq(
                "vandung",
                r"Dùng một Joulemeter đo năng lượng nhiệt cung cấp cho một cốc chứa $m = 200\text{ g}$ nước. Khi nhiệt độ của nước tăng từ $t_1 = 25^\circ\text{C}$ lên $t_2 = 45^\circ\text{C}$ (bỏ qua hao phí nhiệt ra môi trường, lấy nhiệt dung riêng của nước là $c = 4200\text{ J/(kg}\cdot\text{K)}$) thì số chỉ năng lượng tăng thêm trên Joulemeter là:",
                [r"$1680\text{ J}$", r"$16800\text{ J}$", r"$37800\text{ J}$", r"$8400\text{ J}$"],
                1,
                r"Đổi $m = 200\text{ g} = 0{,}2\text{ kg}$ và $\Delta t = 45 - 25 = 20^\circ\text{C}$. Nhiệt lượng truyền cho nước là $Q = m \cdot c \cdot \Delta t = 0{,}2 \cdot 4200 \cdot 20 = 16800\text{ J}$.",
            ),
            short(
                "vandung",
                r"Thả một thỏi đồng có khối lượng $m_1 = 0{,}5\text{ kg}$ đang ở nhiệt độ $t_1 = 120^\circ\text{C}$ vào một bình cách nhiệt chứa $m_2 = 0{,}5\text{ kg}$ nước ở nhiệt độ $t_2 = 20^\circ\text{C}$. Biết nhiệt dung riêng của đồng là $c_1 = 380\text{ J/(kg}\cdot\text{K)}$ và của nước là $c_2 = 4200\text{ J/(kg}\cdot\text{K)}$. Bỏ qua sự trao đổi nhiệt với bình và môi trường. Tính nhiệt độ cân bằng $t$ của hệ theo đơn vị ${}^\circ\text{C}$ (làm tròn đến hàng phần mười).",
                ["28,3", "28.3"],
                r"Áp dụng phương trình cân bằng nhiệt $Q_{\text{tỏa}} = Q_{\text{thu}}$: $m_1 c_1 (t_1 - t) = m_2 c_2 (t - t_2) \iff 0{,}5 \cdot 380 \cdot (120 - t) = 0{,}5 \cdot 4200 \cdot (t - 20) \iff 38(120 - t) = 420(t - 20) \iff 4560 - 38t = 420t - 8400 \iff 458t = 12960 \Rightarrow t \approx 28{,}3^\circ\text{C}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 7: ĐIỆN =====================
    {
        "topic": "dien",
        "title": "Sự nhiễm điện, Dòng điện, Nguồn điện, Mạch điện, Các tác dụng và Đo cường độ dòng điện, hiệu điện thế",
        "icon": "⚡",
        "description": "Chương V · SGK Khoa học tự nhiên 8 Kết nối tri thức với cuộc sống (Bài 20 – Bài 25): Hiện tượng nhiễm điện do cọ xát, dòng điện và nguồn điện, sơ đồ mạch điện đơn giản, các tác dụng của dòng điện, cường độ dòng điện và hiệu điện thế.",
        "requirements": [
            r"Giải thích được sơ lược nguyên nhân một vật cách điện nhiễm điện do cọ xát và tương tác giữa hai vật mang điện tích cùng loại hoặc khác loại.",
            r"Định nghĩa được dòng điện là dòng chuyển dời có hướng của các hạt mang điện; phân biệt được vật dẫn điện và vật cách điện; vẽ được sơ đồ mạch điện đơn giản gồm nguồn điện, công tắc, bóng đèn, chuông điện, điện trở, cầu chì.",
            r"Thực hiện thí nghiệm minh họa được các tác dụng cơ bản của dòng điện: nhiệt, phát sáng, hóa học, sinh lí.",
            r"Nêu được đơn vị đo cường độ dòng điện ($\text{A}$, $\text{mA}$) và đơn vị đo hiệu điện thế ($\text{V}$, $\text{mV}$, $\text{kV}$); thực hành đo được cường độ dòng điện bằng ampe kế và hiệu điện thế bằng vôn kế.",
        ],
        "definition": r"""- **Sự nhiễm điện**: Có hai loại điện tích là điện tích dương ($+$) và điện tích âm ($-$). Các điện tích cùng dấu thì đẩy nhau, trái dấu thì hút nhau.
- **Dòng điện**: Là dòng chuyển dời có hướng của các hạt mang điện (trong kim loại là dòng các electron tự do dịch chuyển có hướng).
- **Cường độ dòng điện** ($I$, đơn vị $\text{A}$) đặc trưng cho tác dụng mạnh hay yếu của dòng điện; **Hiệu điện thế** ($U$, đơn vị $\text{V}$) đặc trưng cho khả năng tạo ra dòng điện của nguồn điện.""",
        "theory": r"""### Bài 20. Hiện tượng nhiễm điện do cọ xát
- **Tính chất của vật nhiễm điện**: Nhiều vật sau khi bị cọ xát có khả năng hút các vật nhẹ (như mẩu giấy vụn, sợi bông) hoặc làm sáng bút thử điện, gọi là các vật nhiễm điện (vật mang điện tích).
- **Hai loại điện tích và sự dịch chuyển electron**: Có hai loại điện tích là điện tích dương ($+$) và điện tích âm ($-$); hai vật nhiễm điện cùng loại thì đẩy nhau, khác loại thì hút nhau. Bình thường nguyên tử trung hòa về điện; khi cọ xát hai vật, các electron có thể dịch chuyển từ vật này sang vật kia: vật **nhận thêm electron** sẽ nhiễm điện **âm** ($-$), còn vật **mất bớt electron** sẽ nhiễm điện **dương** ($+$).
### Bài 21. Dòng điện, nguồn điện
- **Dòng điện và nguồn điện**: Dòng điện là dòng chuyển dời có hướng của các hạt mang điện. Nguồn điện (pin, ắc quy, máy phát điện) có khả năng cung cấp và duy trì dòng điện lâu dài trong mạch. Mỗi nguồn điện một chiều đều có hai cực: cực dương ($+$) và cực âm ($-$).
- **Vật dẫn điện và vật cách điện**: Vật dẫn điện là vật cho dòng điện chạy qua vì có chứa nhiều hạt mang điện tự do (như các kim loại đồng, nhôm, bạc, than chì, dung dịch muối, acid). Vật cách điện là vật không cho dòng điện chạy qua (như nhựa, cao su, sứ, thủy tinh, gỗ khô, nước nguyên chất).
### Bài 22. Mạch điện đơn giản
- **Sơ đồ mạch điện và chiều dòng điện quy ước**: Mạch điện đơn giản gồm nguồn điện, dây dẫn, công tắc (khóa $K$), thiết bị tiêu thụ điện (bóng đèn, chuông điện, biến trở) và thiết bị bảo vệ (cầu chì, rơ-le, cầu dao tự động). Dòng điện chỉ chạy trong mạch điện kín.
- **Quy ước về chiều dòng điện**: Chiều dòng điện theo quy ước là chiều từ cực dương ($+$) của nguồn điện qua dây dẫn và các thiết bị điện tới cực âm ($-$) của nguồn điện (ngược chiều dịch chuyển có hướng của các electron tự do trong dây dẫn kim loại).
### Bài 23. Tác dụng của dòng điện
- **Các tác dụng cơ bản của dòng điện**:
  + **Tác dụng nhiệt**: Làm nóng vật dẫn có dòng điện chạy qua (ứng dụng trong bàn là, nồi cơm điện, ấm siêu tốc, lò sưởi điện, cầu chì bảo vệ mạch).
  + **Tác dụng phát sáng**: Làm sáng đèn LED (điốt phát quang chỉ cho dòng điện đi qua theo một chiều nhất định), đèn bút thử điện, đèn huỳnh quang.
  + **Tác dụng hóa học**: Khi dòng điện đi qua dung dịch muối đồng ($\text{CuSO}_4$), nó tách đồng nguyên chất bám vào thỏi than nối với cực âm (ứng dụng trong mạ điện: mạ vàng, mạ bạc, mạ kẽm, tinh luyện kim loại).
  + **Tác dụng sinh lí**: Dòng điện đi qua cơ thể người và động vật làm cơ co giật, tim ngừng đập, ngạt thở và tê liệt thần kinh (ứng dụng an toàn trong y học như máy sốc điện tim, điện châm).
### Bài 24. Cường độ dòng điện và hiệu điện thế
- **Cường độ dòng điện ($I$)**: Đại lượng đặc trưng cho độ mạnh yếu của dòng điện, đơn vị chuẩn là ampe ($\text{A}$), ước số là mi-li-ampe ($\text{mA}$) với $1\text{ A} = 1000\text{ mA}$. Dụng cụ đo là **ampe kế** (kí hiệu chữ $\text{A}$ trong vòng tròn).
- **Hiệu điện thế ($U$)**: Giữa hai cực của nguồn điện luôn có một hiệu điện thế, đơn vị chuẩn là vôn ($\text{V}$), với $1\text{ V} = 1000\text{ mV}$ và $1\text{ kV} = 1000\text{ V}$. Dụng cụ đo là **vôn kế** (kí hiệu chữ $\text{V}$ trong vòng tròn).
### Bài 25. Thực hành đo cường độ dòng điện và hiệu điện thế
- **Cách mắc ampe kế**: Phải mắc **nối tiếp** với thiết bị cần đo sao cho chốt dương ($+$) của ampe kế nối về phía cực dương ($+$) của nguồn điện (không bao giờ mắc trực tiếp hai chốt của ampe kế vào hai cực nguồn điện vì sẽ làm hỏng ampe kế và nguồn).
- **Cách mắc vôn kế**: Phải mắc **song song** với hai đầu thiết bị (hoặc hai cực nguồn điện) cần đo, chốt dương ($+$) nối về phía cực dương ($+$) của nguồn điện.""",
        "formulas": [
            G(
                "I. Quy đổi đơn vị cường độ dòng điện và hiệu điện thế",
                F("Đơn vị cường độ dòng điện ($I$)", r"$1\text{ A} = 1000\text{ mA};\quad 1\text{ mA} = 10^{-3}\text{ A} = 0{,}001\text{ A}$", r"Đo bằng ampe kế mắc nối tiếp"),
                F("Đơn vị hiệu điện thế ($U$)", r"$1\text{ kV} = 1000\text{ V};\quad 1\text{ V} = 1000\text{ mV} = 10^3\text{ mV}$", r"Đo bằng vôn kế mắc song song"),
            ),
            G(
                "II. Quy tắc dòng điện và thiết bị mạch điện",
                F("Sự nhiễm điện do trao đổi electron", r"$\text{Nhận thêm } e^- \Rightarrow \text{nhiễm điện âm } (-);\quad \text{Mất bớt } e^- \Rightarrow \text{nhiễm điện dương } (+)$", r""),
                F("Chiều dòng điện quy ước trong kim loại", r"$\text{Chiều dòng điện quy ước } (+\to -) \text{ ngược với chiều dịch chuyển của } e^- (-\to +)$", r""),
                F("Tác dụng của cầu chì và mạ điện", r"$\text{Cầu chì: Tác dụng nhiệt};\quad \text{Mạ điện: Tác dụng hóa học (vật cần mạ nối cực âm)}$", r""),
            ),
        ],
        "example": r"Trong thí nghiệm thực hành, một học sinh đo cường độ dòng điện chạy qua bóng đèn được $I = 350\text{ mA}$ và hiệu điện thế giữa hai đầu bóng đèn là $U = 4{,}5\text{ V}$. Hãy đổi giá trị cường độ dòng điện sang đơn vị ampe ($\text{A}$), hiệu điện thế sang đơn vị mi-li-vôn ($\text{mV}$) và nêu rõ cách mắc ampe kế, vôn kế trong mạch.",
        "example_answer": r"""- Đổi đơn vị cường độ dòng điện và hiệu điện thế:
$$I = 350\text{ mA} = \dfrac{350}{1000} = 0{,}35\text{ A}$$
$$U = 4{,}5\text{ V} = 4{,}5 \cdot 1000 = 4500\text{ mV}$$
- Cách mắc dụng cụ đo:
  + **Ampe kế** được mắc **nối tiếp** với bóng đèn.
  + **Vôn kế** được mắc **song song** vào hai đầu bóng đèn.
  + Chốt dương ($+$) của cả ampe kế và vôn kế đều phải nối về phía cực dương ($+$) của nguồn điện.""",
        "real_life": r"""- **Phòng chống tĩnh điện**: Xe bồn chở xăng dầu luôn có một sợi dây xích sắt thả chạm mặt đường để dẫn các điện tích sinh ra do ma sát truyền xuống đất, tránh phóng tia lửa điện gây cháy nổ.
- **Kĩ thuật điện gia dụng và công nghiệp**: Đèn LED tiết kiệm điện, công nghệ mạ vàng trang sức, mạ crom chống gỉ cho chi tiết máy, cầu chì và aptomat bảo vệ mạng điện gia đình.""",
        "game_title": "Thử thách thực tế: Điện và Mạch điện",
        "game_description": "Lắp ráp sơ đồ mạch điện đơn giản, mắc đúng ampe kế và vôn kế để đo thông số và chẩn đoán sự cố trong mạch.",
        "game_type": "game_dien",
        "quiz": [
            mcq(
                "biet",
                r"Khi cọ xát một thanh nhựa sẫm màu vào mảnh vải khô, thanh nhựa nhiễm điện âm. Nguyên nhân là vì:",
                [
                    r"Các hạt nhân mang điện dương di chuyển từ thanh nhựa sang mảnh vải",
                    r"Các electron dịch chuyển từ mảnh vải sang thanh nhựa làm thanh nhựa thừa electron",
                    r"Các electron dịch chuyển từ thanh nhựa sang mảnh vải",
                    r"Các hạt proton di chuyển từ mảnh vải sang thanh nhựa",
                ],
                1,
                r"Chỉ có các electron mới dịch chuyển từ vật này sang vật khác khi cọ xát; thanh nhựa nhận thêm electron từ mảnh vải nên nhiễm điện âm.",
            ),
            mcq(
                "biet",
                r"Trong các nhóm vật liệu dưới đây, nhóm nào chỉ gồm các vật dẫn điện ở điều kiện thường?",
                [
                    r"Đồng, nhôm, dung dịch muối ăn, ruột bút chì (than chì)",
                    r"Bạc, nhựa dẻo, thủy tinh, nước cất nguyên chất",
                    r"Cao su, gỗ khô, sứ cách điện, dây sắt",
                    r"Giấy khô, không khí khô, dây đồng, vàng",
                ],
                0,
                r"Đồng, nhôm, than chì và dung dịch muối ăn đều có nhiều hạt mang điện tự do nên dẫn điện tốt.",
            ),
            mcq(
                "biet",
                r"Theo quy ước, chiều của dòng điện trong một mạch điện kín là:",
                [
                    r"Chiều từ cực âm qua dây dẫn và các dụng cụ điện tới cực dương của nguồn điện",
                    r"Chiều dịch chuyển có hướng của các electron tự do trong dây dẫn kim loại",
                    r"Chiều từ cực dương qua dây dẫn và các thiết bị điện tới cực âm của nguồn điện",
                    r"Chiều ngẫu nhiên thay đổi liên tục trong pin một chiều",
                ],
                2,
                r"Chiều dòng điện quy ước là chiều đi từ cực dương ($+$) của nguồn điện qua dây dẫn và các thiết bị tiêu thụ điện tới cực âm ($-$) của nguồn điện.",
            ),
            mcq(
                "biet",
                r"Khi sử dụng ampe kế để đo cường độ dòng điện chạy qua một bóng đèn, ta phải mắc ampe kế như thế nào?",
                [
                    r"Mắc song song với hai đầu bóng đèn",
                    r"Mắc nối tiếp với bóng đèn sao cho chốt dương ($+$) nối về phía cực dương của nguồn điện",
                    r"Mắc trực tiếp hai chốt của ampe kế vào hai cực của nguồn điện mà không qua đèn",
                    r"Mắc nối tiếp với bóng đèn và chốt dương ($+$) nối về phía cực âm của nguồn điện",
                ],
                1,
                r"Ampe kế luôn phải mắc nối tiếp với thiết bị cần đo và chốt dương ($+$) nối về phía cực dương của nguồn điện.",
            ),
            mcq(
                "hieu",
                r"Một ampe kế có giới hạn đo là $3\text{ A}$, trên mặt chia độ từ vạch $0$ đến vạch $3\text{ A}$ được chia thành $30$ khoảng nhỏ bằng nhau. Độ chia nhỏ nhất (ĐCNN) của ampe kế này là:",
                [r"$1\text{ A}$", r"$0{,}1\text{ A}$", r"$0{,}01\text{ A}$", r"$0{,}3\text{ A}$"],
                1,
                r"Độ chia nhỏ nhất của ampe kế là $\text{ĐCNN} = \dfrac{3 - 0}{30} = 0{,}1\text{ A} = 100\text{ mA}$.",
            ),
            mcq(
                "hieu",
                r"Để mạ một lớp bạc mỏng lên một chiếc vỏ đồng hồ bằng kim loại nhờ tác dụng hóa học của dòng điện (nhúng trong dung dịch muối bạc), người ta phải nối chiếc vỏ đồng hồ với cực nào của nguồn điện một chiều?",
                [
                    r"Nối với cực dương ($+$) của nguồn điện",
                    r"Nối với cực âm ($-$) của nguồn điện",
                    r"Nối đồng thời vào cả hai cực của nguồn điện",
                    r"Không cần nối với nguồn điện, chỉ cần ngâm trong dung dịch",
                ],
                1,
                r"Trong mạ điện, các ion kim loại mang điện dương trong dung dịch sẽ di chuyển về phía cực âm và bám vào vật cần mạ, nên vật cần mạ phải nối với cực âm ($-$).",
            ),
            tf4(
                "hieu",
                r"Xét các tác dụng của dòng điện và các thiết bị bảo vệ trong mạch điện. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Cầu chì bảo vệ mạch điện hoạt động dựa trên tác dụng nhiệt của dòng điện: khi dòng điện tăng quá mức cho phép, dây chì nóng chảy và tự ngắt mạch.",
                    r"b) Đèn điốt phát quang (đèn LED) cho dòng điện đi qua theo cả hai chiều và đều phát sáng như nhau.",
                    r"c) Trong dây dẫn bằng kim loại, các electron tự do dịch chuyển có hướng từ cực âm của nguồn điện qua dây dẫn tới cực dương của nguồn điện.",
                    r"d) Khi đổi giá trị cường độ dòng điện $I = 0{,}45\text{ A}$ sang đơn vị mi-li-ampe, ta được $I = 45\text{ mA}$.",
                ],
                [True, False, True, False],
                r"a) Đúng. b) Sai vì đèn LED chỉ cho dòng điện đi qua theo một chiều nhất định (từ bản cực dương sang bản cực âm). c) Đúng vì electron mang điện âm bị cực âm đẩy và cực dương hút. d) Sai vì $0{,}45\text{ A} = 0{,}45 \cdot 1000 = 450\text{ mA}$.",
            ),
            tf4(
                "hieu",
                r"Một học sinh lắp mạch điện gồm một nguồn điện (hai pin nối tiếp có hiệu điện thế $3\text{ V}$), một công tắc đóng, một bóng đèn đang sáng bình thường, một ampe kế đo dòng điện qua đèn và một vôn kế đo hiệu điện thế hai đầu đèn. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Vôn kế được mắc song song với hai đầu bóng đèn.",
                    r"b) Nếu ngắt công tắc (khóa $K$ mở) thì mạch điện bị hở và số chỉ của ampe kế bằng $0\text{ A}$.",
                    r"c) Nếu tháo bóng đèn ra khỏi đui đèn thì vôn kế mắc ở hai đầu đui đèn cũng lập tức bị cháy hỏng.",
                    r"d) Nếu mắc nhầm ampe kế song song trực tiếp vào hai đầu bóng đèn thì dòng điện lớn sẽ đi qua ampe kế gây đoản mạch và làm đèn tắt.",
                ],
                [True, True, False, True],
                r"a) Đúng. b) Đúng vì mạch hở không có dòng điện chạy qua. c) Sai vì vôn kế có điện trở rất lớn, khi tháo bóng đèn ra thì vôn kế chỉ đo hiệu điện thế của nguồn ($3\text{ V}$) và hoàn toàn an toàn. d) Đúng vì ampe kế có điện trở rất nhỏ nên mắc song song sẽ làm đoản mạch hai đầu đèn.",
            ),
            mcq(
                "vandung",
                r"Cho ba quả cầu nhẹ $A, B, C$ được treo bằng các sợi chỉ tơ mảnh cách điện. Biết quả cầu $A$ đã được tích điện dương ($+$). Khi đưa lại gần nhau, ta thấy quả cầu $A$ đẩy quả cầu $B$, còn quả cầu $B$ lại hút quả cầu $C$ (biết cả ba quả cầu đều mang điện tích). Điện tích của quả cầu $B$ và $C$ lần lượt là:",
                [
                    r"$B$ mang điện dương ($+$), $C$ mang điện dương ($+$)",
                    r"$B$ mang điện dương ($+$), $C$ mang điện âm ($-$)",
                    r"$B$ mang điện âm ($-$), $C$ mang điện dương ($+$)",
                    r"$B$ mang điện âm ($-$), $C$ mang điện âm ($-$)",
                ],
                1,
                r"Vì $A$ tích điện dương ($+$) mà $A$ đẩy $B$ nên $B$ cùng dấu với $A$, tức là $B$ mang điện dương ($+$). Vì $B$ hút $C$ và $C$ có mang điện nên $C$ trái dấu với $B$, tức là $C$ mang điện âm ($-$).",
            ),
            short(
                "vandung",
                r"Trên mặt một vôn kế có giới hạn đo là $6\text{ V}$, khoảng từ vạch $0$ đến vạch $6\text{ V}$ được chia đều thành $30$ khoảng nhỏ bằng nhau. Khi mắc vôn kế vào hai đầu một bóng đèn đang sáng, kim vôn kế chỉ đúng vạch thứ $22$ tính từ vạch số $0$. Hiệu điện thế giữa hai đầu bóng đèn bằng bao nhiêu $\text{mV}$?",
                ["4400"],
                r"Độ chia nhỏ nhất của vôn kế là $\text{ĐCNN} = \dfrac{6}{30} = 0{,}2\text{ V}$. Khi kim chỉ vạch thứ $22$, hiệu điện thế đọc được là $U = 22 \cdot 0{,}2 = 4{,}4\text{ V} = 4400\text{ mV}$.",
            ),
        ],
    },
]
