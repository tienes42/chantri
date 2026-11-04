"""VẬT LÍ 9 (KHOA HỌC TỰ NHIÊN 9) — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).

Bao phủ đầy đủ các chương Vật lí trong SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống:
- Chương I. Năng lượng cơ học (Bài 2 – Bài 4)
- Chương II. Ánh sáng (Bài 5 – Bài 10)
- Chương III. Điện (Bài 11 – Bài 13)
- Chương IV. Điện từ (Bài 14 – Bài 15) & Chương V. Năng lượng với cuộc sống (Bài 16 – Bài 17)

7 chủ đề tương thích hệ thống game:
1. co-nang-khuc-xa-anh-sang (game_type="game_co_nang_khuc_xa")
2. quang-hoc (game_type="game_quanghoc")
3. dien-tro (game_type="game_ohm")
4. doan-mach-noi-tiep (game_type="game_doanmachnoitiep")
5. doan-mach-song-song (game_type="game_doanmachsongsong")
6. cong-va-cong-suat-dien (game_type="game_congsuatdien")
7. dien-tu (game_type="game_dientu")

Mỗi chủ đề gồm: Yêu cầu cần đạt (CT GDPT 2018), định nghĩa, lý thuyết chi tiết theo từng bài SGK,
nhóm công thức KaTeX, ví dụ minh họa, ứng dụng thực tiễn, thông tin trò chơi và 10 câu hỏi
(4 câu Biết MCQ, 2 câu Hiểu MCQ, 2 câu Hiểu Đúng/Sai 4 mệnh đề a–d, 1 câu Vận dụng MCQ, 1 câu Vận dụng Trả lời ngắn).
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 9

LESSONS = [
    # ===================== CHỦ ĐỀ 1: CƠ NĂNG VÀ KHÚC XẠ ÁNH SÁNG =====================
    {
        "topic": "co-nang-khuc-xa-anh-sang",
        "title": "Động năng, Thế năng, Cơ năng và Khúc xạ ánh sáng, Phản xạ toàn phần, Tán sắc qua lăng kính, Màu sắc các vật",
        "icon": "💎",
        "description": "Chương I (Bài 2 – Bài 4) và Chương II (Bài 5 – Bài 7) · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống: Động năng, thế năng, cơ năng, công và công suất; khúc xạ ánh sáng, phản xạ toàn phần, tán sắc ánh sáng qua lăng kính và màu sắc các vật.",
        "requirements": [
            r"Viết được biểu thức tính động năng $W_{\text{đ}} = \dfrac{1}{2}mv^2$ và thế năng trọng trường $W_{\text{t}} = P \cdot h$; nêu được cơ năng là tổng động năng và thế năng của vật và vận dụng khái niệm cơ năng để mô tả sự chuyển hóa năng lượng.",
            r"Tính được công và công suất trong một số trường hợp đơn giản theo công thức $A = F \cdot s$ và $\mathcal{P} = \dfrac{A}{t} = F \cdot v$.",
            r"Thực hiện thí nghiệm chứng tỏ được khi truyền từ môi trường này sang môi trường khác, tia sáng có thể bị khúc xạ; nêu được chiết suất $n = \dfrac{c}{v}$ và vận dụng được biểu thức $\dfrac{\sin i}{\sin r} = \dfrac{n_2}{n_1}$.",
            r"Thực hiện thí nghiệm để rút ra được điều kiện xảy ra phản xạ toàn phần và xác định được góc tới hạn $\sin i_{\text{th}} = \dfrac{n_2}{n_1}$.",
            r"Thực hiện thí nghiệm với lăng kính tạo được quang phổ của ánh sáng trắng; giải thích được một cách định tính sự tán sắc ánh sáng Mặt Trời qua lăng kính và màu sắc của các vật dưới ánh sáng trắng hoặc ánh sáng màu.",
        ],
        "definition": r"""- **Cơ năng** của một vật bằng tổng động năng và thế năng của vật: $W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}mv^2 + P \cdot h$ (đơn vị: jun, kí hiệu $\text{J}$).
- **Khúc xạ ánh sáng** là hiện tượng tia sáng truyền từ môi trường trong suốt này sang môi trường trong suốt khác bị gãy khúc tại mặt phân cách giữa hai môi trường: $n_1 \sin i = n_2 \sin r$.
- **Phản xạ toàn phần** là hiện tượng phản xạ toàn bộ tia tới xảy ra tại mặt phân cách giữa hai môi trường trong suốt khi $n_1 > n_2$ và $i \ge i_{\text{th}}$ (với $\sin i_{\text{th}} = \dfrac{n_2}{n_1}$).""",
        "theory": r"""### Bài 2. Động năng. Thế năng
- **Động năng ($W_{\text{đ}}$)**: Năng lượng vật có được do chuyển động. Một vật có khối lượng $m$ ($\text{kg}$) đang chuyển động với tốc độ $v$ ($\text{m/s}$) thì có động năng $W_{\text{đ}} = \dfrac{1}{2}mv^2$ ($\text{J}$).
- **Thế năng trọng trường ($W_{\text{t}}$)**: Năng lượng của một vật khi ở một độ cao $h$ nhất định so với mặt đất hoặc so với một vị trí được chọn làm mốc thế năng: $W_{\text{t}} = P \cdot h = 10m \cdot h$ ($\text{J}$), với $P$ ($\text{N}$) là trọng lượng của vật và $h$ ($\text{m}$) là độ cao.
### Bài 3. Cơ năng
- **Khái niệm và sự chuyển hóa cơ năng**: Tổng động năng và thế năng của vật gọi là cơ năng: $W = W_{\text{đ}} + W_{\text{t}}$. Trong quá trình vật chuyển động (như con lắc dao động, vật rơi từ trên cao), động năng và thế năng có thể chuyển hóa qua lại lẫn nhau. Nếu bỏ qua mọi lực cản và ma sát thì cơ năng của vật được bảo toàn ($W = \text{hằng số}$).
### Bài 4. Công và công suất
- **Công cơ học ($A$)**: Khi một lực không đổi $F$ tác dụng lên một vật và điểm đặt của lực chuyển dời một đoạn $s$ theo hướng của lực thì công của lực là $A = F \cdot s$ ($1\text{ J} = 1\text{ N}\cdot\text{m}$).
- **Công suất ($\mathcal{P}$)**: Tốc độ thực hiện công gọi là công suất: $\mathcal{P} = \dfrac{A}{t} = F \cdot v$ ($1\text{ W} = 1\text{ J/s}$; $1\text{ kW} = 1000\text{ W}$; $1\text{ HP} \approx 746\text{ W}$).
### Bài 5. Khúc xạ ánh sáng
- **Định luật khúc xạ ánh sáng**: Tia khúc xạ nằm trong mặt phẳng tới (tạo bởi tia tới và pháp tuyến) và ở phía bên kia pháp tuyến so với tia tới. Với hai môi trường trong suốt nhất định, tỉ số giữa $\sin$ góc tới ($\sin i$) và $\sin$ góc khúc xạ ($\sin r$) luôn không đổi: $\dfrac{\sin i}{\sin r} = \dfrac{n_2}{n_1} \iff n_1 \sin i = n_2 \sin r$.
- **Chiết suất của môi trường**: Chiết suất tuyệt đối $n = \dfrac{c}{v} \ge 1$, trong đó $c \approx 3 \cdot 10^8\text{ m/s}$ là tốc độ ánh sáng trong chân không (hoặc không khí có $n \approx 1$) và $v$ là tốc độ ánh sáng trong môi trường đó. Khi ánh sáng truyền từ không khí vào nước hoặc thủy tinh ($n_1 < n_2$) thì góc khúc xạ nhỏ hơn góc tới ($r < i$); ngược lại khi truyền từ nước hoặc thủy tinh ra không khí ($n_1 > n_2$) thì $r > i$.
### Bài 6. Phản xạ toàn phần
- **Điều kiện phản xạ toàn phần**: Hiện tượng toàn bộ tia sáng tới bị phản xạ trở lại môi trường cũ tại mặt phân cách gọi là phản xạ toàn phần. Hai điều kiện bắt buộc: (1) Ánh sáng truyền từ môi trường có chiết suất lớn sang môi trường có chiết suất nhỏ hơn ($n_1 > n_2$); (2) Góc tới lớn hơn hoặc bằng góc tới hạn ($i \ge i_{\text{th}}$) với $\sin i_{\text{th}} = \dfrac{n_2}{n_1}$.
### Bài 7. Lăng kính
- **Tán sắc ánh sáng qua lăng kính**: Khi chiếu một chùm ánh sáng trắng hẹp (như ánh sáng Mặt Trời) qua lăng kính, chùm tia ló bị lệch về phía đáy lăng kính và tách thành một dải màu biến thiên liên tục từ đỏ đến tím (đỏ, da cam, vàng, lục, lam, chàm, tím) gọi là quang phổ của ánh sáng trắng. Chiết suất của lăng kính đối với ánh sáng đỏ là nhỏ nhất (bị lệch ít nhất) và đối với ánh sáng tím là lớn nhất (bị lệch nhiều nhất).
- **Màu sắc các vật**: Ánh sáng có một màu nhất định và không bị tán sắc khi qua lăng kính gọi là ánh sáng đơn sắc. Màu sắc của một vật được nhìn thấy phụ thuộc vào màu sắc của ánh sáng bị vật đó tán xạ (phản xạ) hoặc truyền qua vào mắt: vật màu nào thì tán xạ mạnh ánh sáng màu đó và hấp thụ các màu còn lại; vật màu trắng tán xạ tốt tất cả các ánh sáng màu; vật màu đen hấp thụ hầu hết các ánh sáng màu.""",
        "formulas": [
            G(
                "I. Động năng, thế năng, cơ năng, công và công suất",
                F("Động năng và thế năng trọng trường", r"$W_{\text{đ}} = \dfrac{1}{2}mv^2;\quad W_{\text{t}} = P \cdot h = 10m \cdot h$", r"$m$ ($\text{kg}$), $v$ ($\text{m/s}$), $h$ ($\text{m}$), $W$ ($\text{J}$)"),
                F("Cơ năng và bảo toàn cơ năng (bỏ qua ma sát)", r"$W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}mv^2 + P \cdot h = \text{hằng số}$", r"Khi rơi tự do từ độ cao $H$: $v_{\text{chạm đất}} = \sqrt{2gH}$"),
                F("Công cơ học và công suất", r"$A = F \cdot s;\quad \mathcal{P} = \dfrac{A}{t} = F \cdot v$", r"$A$ ($\text{J}$), $\mathcal{P}$ ($\text{W}$)"),
            ),
            G(
                "II. Khúc xạ ánh sáng, phản xạ toàn phần và lăng kính",
                F("Chiết suất của môi trường", r"$n = \dfrac{c}{v} \ge 1\quad (c \approx 3 \cdot 10^8\text{ m/s})$", r"$n_{\text{không khí}} \approx 1;\quad n_{\text{nước}} \approx \dfrac{4}{3} \approx 1{,}33$"),
                F("Định luật khúc xạ ánh sáng", r"$\dfrac{\sin i}{\sin r} = \dfrac{n_2}{n_1} \iff n_1 \sin i = n_2 \sin r$", r"$n_2 > n_1 \Rightarrow r < i;\quad n_2 < n_1 \Rightarrow r > i$"),
                F("Điều kiện và góc tới hạn phản xạ toàn phần", r"$n_1 > n_2 \text{ và } i \ge i_{\text{th}} \text{ với } \sin i_{\text{th}} = \dfrac{n_2}{n_1}$", r"Tia đỏ lệch ít nhất, tia tím lệch nhiều nhất qua lăng kính"),
            ),
        ],
        "example": r"Một vật nhỏ có khối lượng $m = 0{,}5\text{ kg}$ được thả rơi từ độ cao $h = 20\text{ m}$ không vận tốc đầu xuống mặt đất (chọn mốc thế năng tại mặt đất, lấy $P = 10m$, bỏ qua sức cản không khí). Tính cơ năng của vật, tốc độ của vật ngay khi chạm đất và độ cao $h'$ nơi vật có động năng bằng $3$ lần thế năng.",
        "example_answer": r"""- Tại vị trí thả rơi ($h = 20\text{ m}, v_0 = 0$), cơ năng của vật bằng thế năng ban đầu:
$$W = W_{\text{t max}} = P \cdot h = 10 \cdot 0{,}5 \cdot 20 = 100\text{ J}$$
- Ngay khi chạm đất ($W_{\text{t}} = 0$), toàn bộ cơ năng đã chuyển hóa thành động năng:
$$W_{\text{đ max}} = \dfrac{1}{2}mv^2 = W \iff \dfrac{1}{2} \cdot 0{,}5 \cdot v^2 = 100 \Rightarrow v^2 = 400 \Rightarrow v = 20\text{ m/s}$$
- Tại vị trí có $W_{\text{đ}} = 3W_{\text{t}}$, áp dụng bảo toàn cơ năng:
$$W = W_{\text{đ}} + W_{\text{t}} = 4W_{\text{t}} = 100\text{ J} \Rightarrow W_{\text{t}} = 25\text{ J} \iff 10m \cdot h' = 25 \Rightarrow h' = \dfrac{25}{5} = 5\text{ m}$$""",
        "real_life": r"""- **Thủy điện và trò chơi cảm giác mạnh**: Các nhà máy thủy điện xây đập dâng nước lên cao để tích trữ thế năng trọng trường khổng lồ rồi chuyển hóa thành động năng làm quay tua-bin phát điện; tàu lượn siêu tốc hoạt động nhờ sự chuyển hóa liên tục giữa thế năng và động năng.
- **Cáp quang viễn thông và y học**: Sợi cáp quang Internet và ống nội soi dạ dày có lõi thủy tinh chiết suất $n_1$ lớn hơn lớp vỏ $n_2$, dẫn truyền tín hiệu ánh sáng đi xa nhờ hiện tượng phản xạ toàn phần liên tiếp.""",
        "game_title": "Thử thách thực tế: Cơ năng và Khúc xạ ánh sáng",
        "game_description": "Mô phỏng chuyển hóa động năng – thế năng trên đường trượt và điều chỉnh góc tới tia laser để tạo phản xạ toàn phần trong cáp quang.",
        "game_type": "game_co_nang_khuc_xa",
        "quiz": [
            mcq(
                "biet",
                r"Một vật có khối lượng $m$ ($\text{kg}$) đang chuyển động với tốc độ $v$ ($\text{m/s}$) thì động năng của vật được tính theo công thức nào?",
                [r"$W_{\text{đ}} = m \cdot v$", r"$W_{\text{đ}} = \dfrac{1}{2}mv^2$", r"$W_{\text{đ}} = m \cdot v^2$", r"$W_{\text{đ}} = 2mv^2$"],
                1,
                r"Động năng của vật khối lượng $m$ chuyển động với tốc độ $v$ được xác định bởi công thức $W_{\text{đ}} = \dfrac{1}{2}mv^2$.",
            ),
            mcq(
                "biet",
                r"Khi chiếu một tia sáng truyền xiên góc từ không khí ($n_1 \approx 1$) vào nước ($n_2 = \dfrac{4}{3}$), quan hệ giữa góc tới $i$ và góc khúc xạ $r$ là:",
                [r"$r > i$", r"$r = i$", r"$r < i$", r"$r = 90^\circ$"],
                2,
                r"Theo định luật khúc xạ $\dfrac{\sin i}{\sin r} = \dfrac{n_2}{n_1}$, vì $n_2 > n_1$ nên $\sin r < \sin i \Rightarrow r < i$ (tia khúc xạ lệch lại gần pháp tuyến hơn).",
            ),
            mcq(
                "biet",
                r"Khi chiếu một chùm tia sáng trắng hẹp đi qua một lăng kính thủy tinh, tia sáng đơn sắc nào sau đây bị lệch ít nhất về phía đáy lăng kính?",
                [r"Tia màu tím", r"Tia màu lam", r"Tia màu lục", r"Tia màu đỏ"],
                3,
                r"Chiết suất của thủy tinh đối với ánh sáng đỏ là nhỏ nhất nên tia đỏ bị lệch ít nhất, còn tia tím bị lệch nhiều nhất.",
            ),
            mcq(
                "biet",
                r"Dưới ánh sáng trắng của Mặt Trời, ta nhìn thấy bông hoa hồng có màu đỏ là vì:",
                [
                    r"Bông hoa tự phát ra ánh sáng màu đỏ trong bóng tối",
                    r"Cánh hoa hồng hấp thụ hoàn toàn ánh sáng đỏ và tán xạ các màu khác",
                    r"Cánh hoa hồng tán xạ mạnh ánh sáng màu đỏ vào mắt ta và hấp thụ hầu hết các ánh sáng màu khác",
                    r"Cánh hoa hồng tán xạ tất cả các màu trong ánh sáng trắng như nhau",
                ],
                2,
                r"Vật có màu đỏ vì nó tán xạ mạnh ánh sáng màu đỏ truyền tới mắt và hấp thụ hầu hết các ánh sáng màu khác.",
            ),
            mcq(
                "hieu",
                r"Một quả bóng có khối lượng $m = 400\text{ g}$ đang bay với tốc độ $v = 10\text{ m/s}$ ở độ cao $h = 5\text{ m}$ so với mặt đất (lấy $P = 10m$). Cơ năng của quả bóng lúc đó so với mặt đất bằng:",
                [r"$20\text{ J}$", r"$40\text{ J}$", r"$60\text{ J}$", r"$220\text{ J}$"],
                1,
                r"Đổi $m = 400\text{ g} = 0{,}4\text{ kg}$. Động năng $W_{\text{đ}} = \dfrac{1}{2} \cdot 0{,}4 \cdot 10^2 = 20\text{ J}$; thế năng $W_{\text{t}} = 10 \cdot 0{,}4 \cdot 5 = 20\text{ J}$. Cơ năng $W = W_{\text{đ}} + W_{\text{t}} = 40\text{ J}$.",
            ),
            mcq(
                "hieu",
                r"Chiếu một tia sáng từ không khí ($n_1 = 1$) vào một khối chất trong suốt dưới góc tới $i = 45^\circ$ thì góc khúc xạ đo được là $r = 30^\circ$. Chiết suất $n_2$ của khối chất trong suốt đó là:",
                [r"$\sqrt{2} \approx 1{,}41$", r"$\sqrt{3} \approx 1{,}73$", r"$1{,}5$", r"$\dfrac{\sqrt{2}}{2} \approx 0{,}71$"],
                0,
                r"Ta có $n_1 \sin i = n_2 \sin r \Rightarrow n_2 = \dfrac{1 \cdot \sin 45^\circ}{\sin 30^\circ} = \dfrac{\frac{\sqrt{2}}{2}}{\frac{1}{2}} = \sqrt{2} \approx 1{,}41$.",
            ),
            tf4(
                "hieu",
                r"Một viên bi thép có khối lượng $m = 0{,}2\text{ kg}$ được ném thẳng đứng lên cao từ mặt đất với tốc độ ban đầu $v_0 = 10\text{ m/s}$ (chọn mốc thế năng tại mặt đất, lấy $P = 10m$, bỏ qua sức cản không khí). Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Động năng ban đầu của viên bi ngay lúc ném tại mặt đất là $W_{\text{đ0}} = 10\text{ J}$.",
                    r"b) Khi viên bi đang bay lên cao, động năng của viên bi tăng dần còn thế năng giảm dần.",
                    r"c) Tại vị trí cao nhất mà viên bi lên tới được, tốc độ của viên bi bằng $0$ và thế năng đạt giá trị cực đại bằng $10\text{ J}$.",
                    r"d) Độ cao cực đại mà viên bi đạt được so với mặt đất là $h_{\max} = 5\text{ m}$.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $W_{\text{đ0}} = \dfrac{1}{2}mv_0^2 = \dfrac{1}{2} \cdot 0{,}2 \cdot 10^2 = 10\text{ J}$. b) Sai vì khi bay lên cao độ cao $h$ tăng còn tốc độ $v$ giảm nên động năng chuyển hóa thành thế năng ($W_{\text{đ}}$ giảm, $W_{\text{t}}$ tăng). c) Đúng theo bảo toàn cơ năng. d) Đúng vì $W_{\text{t max}} = 10m \cdot h_{\max} = 10 \iff 2h_{\max} = 10 \Rightarrow h_{\max} = 5\text{ m}$.",
            ),
            tf4(
                "hieu",
                r"Cho chiết suất của thủy tinh là $n_1 = 1{,}5$ và của không khí là $n_2 = 1$. Xét sự truyền ánh sáng qua mặt phân cách giữa thủy tinh và không khí. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Tốc độ truyền ánh sáng trong khối thủy tinh trên bằng $v = 2 \cdot 10^8\text{ m/s}$.",
                    r"b) Hiện tượng phản xạ toàn phần có thể xảy ra khi chiếu tia sáng từ ngoài không khí vào trong khối thủy tinh.",
                    r"c) Giá trị $\sin$ của góc tới hạn phản xạ toàn phần khi tia sáng truyền từ thủy tinh ra không khí là $\sin i_{\text{th}} = \dfrac{2}{3}$ ($i_{\text{th}} \approx 41{,}8^\circ$).",
                    r"d) Nếu chiếu một tia sáng từ trong khối thủy tinh tới mặt phân cách với không khí dưới góc tới $i = 45^\circ$ thì toàn bộ tia sáng bị phản xạ toàn phần trở lại thủy tinh.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $v = \dfrac{c}{n_1} = \dfrac{3 \cdot 10^8}{1{,}5} = 2 \cdot 10^8\text{ m/s}$. b) Sai vì phản xạ toàn phần chỉ xảy ra khi truyền từ môi trường chiết suất lớn sang môi trường chiết suất nhỏ ($n_1 > n_2$). c) Đúng vì $\sin i_{\text{th}} = \dfrac{n_2}{n_1} = \dfrac{1}{1{,}5} = \dfrac{2}{3}$. d) Đúng vì $i = 45^\circ > i_{\text{th}} \approx 41{,}8^\circ$.",
            ),
            mcq(
                "vandung",
                r"Chiếu một tia sáng đơn sắc từ không khí ($n_1 = 1$) vào mặt một khối thủy tinh có chiết suất $n_2 = \sqrt{3}$ dưới góc tới $i = 60^\circ$. Góc lệch $D = |i - r|$ giữa phương của tia tới và phương của tia khúc xạ là:",
                [r"$15^\circ$", r"$30^\circ$", r"$45^\circ$", r"$60^\circ$"],
                1,
                r"Theo định luật khúc xạ: $1 \cdot \sin 60^\circ = \sqrt{3} \cdot \sin r \iff \dfrac{\sqrt{3}}{2} = \sqrt{3} \sin r \Rightarrow \sin r = \dfrac{1}{2} \Rightarrow r = 30^\circ$. Góc lệch là $D = i - r = 60^\circ - 30^\circ = 30^\circ$.",
            ),
            short(
                "vandung",
                r"Một thác nước cao $h = 30\text{ m}$ có lưu lượng nước chảy từ đỉnh thác xuống đáy thác là $m = 4000\text{ kg}$ trong mỗi giây (lấy $P = 10m$). Giả sử $80\%$ công của trọng lực dòng nước được máy phát thủy điện chuyển hóa thành điện năng. Tính công suất phát điện $\mathcal{P}_{\text{điện}}$ của nhà máy theo đơn vị $\text{kW}$.",
                ["960"],
                r"Trong mỗi giây ($t = 1\text{ s}$), công toàn phần của trọng lực khi $4000\text{ kg}$ nước rơi từ độ cao $30\text{ m}$ là $A = P \cdot h = 10 \cdot 4000 \cdot 30 = 1200000\text{ J}$. Công suất dòng nước là $\mathcal{P}_0 = \dfrac{A}{t} = 1200000\text{ W} = 1200\text{ kW}$. Công suất phát điện là $\mathcal{P}_{\text{điện}} = 0{,}8 \cdot 1200 = 960\text{ kW}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 2: QUANG HỌC (THẤU KÍNH VÀ KÍNH LÚP) =====================
    {
        "topic": "quang-hoc",
        "title": "Thấu kính hội tụ, Thấu kính phân kì, Tiêu cự và Kính lúp",
        "icon": "🔍",
        "description": "Chương II · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống (Bài 8 – Bài 10): Thấu kính hội tụ, thấu kính phân kì, trục chính, quang tâm, tiêu điểm, tiêu cự, thực hành đo tiêu cự của thấu kính hội tụ, kính lúp và bài tập thấu kính.",
        "requirements": [
            r"Giải thích được nguyên lí hoạt động của thấu kính bằng việc sử dụng sự khúc xạ của một số các lăng kính nhỏ; nêu được các khái niệm: quang tâm, trục chính, tiêu điểm chính và tiêu cự của thấu kính.",
            r"Tiến hành thí nghiệm rút ra được đường truyền của các tia sáng đặc biệt qua thấu kính hội tụ và thấu kính phân kì.",
            r"Vẽ được ảnh qua thấu kính và nhận biết được độ lớn, tính chất của ảnh (ảnh thật hay ảnh ảo, cùng chiều hay ngược chiều) tạo bởi thấu kính hội tụ và thấu kính phân kì.",
            r"Đo được tiêu cự của thấu kính hội tụ bằng dụng cụ thực hành (phương pháp ảnh thật cao bằng vật khi $d = d' = 2f$).",
            r"Mô tả được cấu tạo, cách sử dụng kính lúp và vận dụng được kiến thức hình học đồng dạng để giải bài tập về thấu kính.",
        ],
        "definition": r"""- **Thấu kính** là một khối chất trong suốt (thủy tinh, nhựa quang học) được giới hạn bởi hai mặt cầu hoặc một mặt cầu và một mặt phẳng.
- **Thấu kính hội tụ** (thấu kính rìa mỏng) biến chùm tia tới song song thành chùm tia ló hội tụ tại tiêu điểm chính $F'$.
- **Thấu kính phân kì** (thấu kính rìa dày) biến chùm tia tới song song thành chùm tia ló phân kì có đường kéo dài đi qua tiêu điểm chính $F'$.
- **Kính lúp** là một thấu kính hội tụ có tiêu cự ngắn (vài $\text{cm}$) dùng để quan sát các vật nhỏ ($d < f$).""",
        "theory": r"""### Bài 8. Thấu kính
- **Phân loại và các yếu tố của thấu kính**:
  + **Thấu kính hội tụ** có phần rìa mỏng hơn phần giữa; **thấu kính phân kì** có phần rìa dày hơn phần giữa.
  + **Quang tâm $O$**: Điểm chính giữa của thấu kính mà mọi tia sáng đi qua đều truyền thẳng không bị đổi hướng.
  + **Trục chính $\Delta$**: Đường thẳng đi qua quang tâm $O$ và vuông góc với bề mặt thấu kính.
  + **Tiêu điểm chính $F, F'$ và tiêu cự $f$**: Hai điểm nằm trên trục chính, đối xứng nhau qua quang tâm $O$. Khoảng cách từ quang tâm đến tiêu điểm chính gọi là tiêu cự của thấu kính: $OF = OF' = f$.
- **Đường truyền của các tia sáng đặc biệt**:
  + Tia tới đi qua quang tâm $O$ thì tia ló tiếp tục truyền thẳng theo phương của tia tới (cho cả hai loại thấu kính).
  + Tia tới song song với trục chính thì tia ló đi qua tiêu điểm chính $F'$ (đối với thấu kính hội tụ) hoặc có đường kéo dài đi qua tiêu điểm chính $F'$ nằm cùng phía tia tới (đối với thấu kính phân kì).
  + Tia tới đi qua tiêu điểm chính $F$ trước khi tới thấu kính hội tụ thì tia ló song song với trục chính.
- **Đặc điểm ảnh của một vật tạo bởi thấu kính**:
  + **Thấu kính hội tụ**: Khi đặt vật ngoài khoảng tiêu cự ($d > f$) thì cho **ảnh thật**, ngược chiều với vật (nếu $d > 2f$ thì ảnh nhỏ hơn vật; nếu $d = 2f$ thì ảnh bằng vật và $d' = 2f$; nếu $f < d < 2f$ thì ảnh lớn hơn vật). Khi đặt vật trong khoảng tiêu cự ($d < f$) thì cho **ảnh ảo**, cùng chiều và lớn hơn vật ($d' > d$).
  + **Thấu kính phân kì**: Với mọi vị trí đặt vật thật ($d > 0$), thấu kính phân kì **luôn cho ảnh ảo**, cùng chiều, nhỏ hơn vật và luôn nằm trong khoảng từ quang tâm $O$ đến tiêu điểm $F$ ($d' < f$).
### Bài 9. Thực hành đo tiêu cự của thấu kính hội tụ
- **Nguyên tắc đo (phương pháp đối xứng Bessel – Silbermann)**: Khi đặt vật sáng trước thấu kính hội tụ cách thấu kính một khoảng $d = 2f$ thì ảnh thật hiện rõ nét trên màn chắn ở vị trí cách thấu kính một khoảng $d' = 2f$ và có chiều cao bằng đúng chiều cao của vật ($h' = h$). Khi đó khoảng cách từ vật đến màn ảnh là $L = d + d' = 4f$, suy ra tiêu cự của thấu kính hội tụ là $f = \dfrac{d + d'}{4} = \dfrac{L}{4}$.
### Bài 10. Kính lúp. Bài tập thấu kính
- **Kính lúp**: Là thấu kính hội tụ có tiêu cự ngắn (thường từ vài $\text{cm}$ đến vài chục $\text{cm}$) dùng để quan sát các vật nhỏ. Khi dùng kính lúp, phải đặt vật trong khoảng tiêu cự của kính ($d < f$) để mắt nhìn thấy một **ảnh ảo, cùng chiều và lớn hơn vật**. Trên vành kính lúp thường ghi số bội giác $G$ như $2\text{x}, 3\text{x}, 5\text{x}, 10\text{x}$ với hệ thức $G = \dfrac{25}{f\text{ (cm)}}$.
- **Giải bài tập thấu kính bằng tam giác đồng dạng**: Sử dụng hai cặp tam giác vuông đồng dạng $\triangle OAB \sim \triangle OA'B'$ (suy ra $\dfrac{h'}{h} = \dfrac{d'}{d}$) và $\triangle F'OI \sim \triangle F'A'B'$ (với $OI = AB = h$) để lập hệ thức tính khoảng cách ảnh $d'$ và chiều cao ảnh $h'$.""",
        "formulas": [
            G(
                "I. Hệ thức vị trí vật – ảnh và độ phóng đại qua thấu kính",
                F("Tỉ số chiều cao ảnh và chiều cao vật", r"$\dfrac{h'}{h} = \dfrac{d'}{d} \Rightarrow h' = h \cdot \dfrac{d'}{d}$", r"Từ $\triangle OAB \sim \triangle OA'B'$"),
                F("Thấu kính hội tụ tạo ảnh thật ($d > f$)", r"$\dfrac{1}{f} = \dfrac{1}{d} + \dfrac{1}{d'} \Rightarrow d' = \dfrac{d \cdot f}{d - f}$", r"Thực hành khi $d = d' = 2f \Rightarrow f = \dfrac{d + d'}{4}$"),
                F("Thấu kính hội tụ tạo ảnh ảo ($d < f$)", r"$\dfrac{1}{f} = \dfrac{1}{d} - \dfrac{1}{d'} \Rightarrow d' = \dfrac{d \cdot f}{f - d}$", r"Ảnh ảo cùng chiều, lớn hơn vật ($d' > d$)"),
                F("Thấu kính phân kì (luôn tạo ảnh ảo với mọi $d > 0$)", r"$\dfrac{1}{f} = \dfrac{1}{d'} - \dfrac{1}{d} \Rightarrow d' = \dfrac{d \cdot f}{d + f}$", r"$f, d, d'$ lấy giá trị độ lớn dương; luôn có $d' < f$ và $h' < h$"),
            ),
            G(
                "II. Kính lúp",
                F("Điều kiện đặt vật khi ngắm qua kính lúp", r"$0 < d < f$", r"Tạo ảnh ảo cùng chiều, lớn hơn vật"),
                F("Số bội giác ghi trên vành kính lúp", r"$G = \dfrac{25}{f} \iff f = \dfrac{25}{G}\quad (f \text{ tính bằng cm})$", r"Ví dụ: kính lúp ghi $5\text{x}$ có $f = \dfrac{25}{5} = 5\text{ cm}$"),
            ),
        ],
        "example": r"Đặt một vật sáng $AB$ hình mũi tên cao $h = 4\text{ cm}$ vuông góc với trục chính của một thấu kính hội tụ có tiêu cự $f = 12\text{ cm}$ ($A$ nằm trên trục chính) và cách thấu kính một khoảng $d = 36\text{ cm}$. Hãy xác định tính chất của ảnh $A'B'$, khoảng cách $d'$ từ ảnh đến thấu kính và chiều cao $h'$ của ảnh.",
        "example_answer": r"""- Vì vật đặt ngoài khoảng tiêu cự ($d = 36\text{ cm} > f = 12\text{ cm}$) nên ảnh $A'B'$ là **ảnh thật, ngược chiều với vật**.
- Áp dụng hệ thức từ hai cặp tam giác đồng dạng $\triangle OAB \sim \triangle OA'B'$ và $\triangle F'OI \sim \triangle F'A'B'$:
$$\dfrac{1}{f} = \dfrac{1}{d} + \dfrac{1}{d'} \Rightarrow d' = \dfrac{d \cdot f}{d - f} = \dfrac{36 \cdot 12}{36 - 12} = \dfrac{432}{24} = 18\text{ cm}$$
- Chiều cao của ảnh $A'B'$ là:
$$h' = h \cdot \dfrac{d'}{d} = 4 \cdot \dfrac{18}{36} = 2\text{ cm}$$""",
        "real_life": r"""- **Dụng cụ quang học và nhiếp ảnh**: Ống kính máy ảnh, máy chiếu phim, kính hiển vi và kính thiên văn sử dụng hệ thấu kính hội tụ để thu nhận hoặc phóng đại hình ảnh; kính lúp giúp thợ sửa đồng hồ, nhà thực vật học quan sát chi tiết nhỏ.
- **Y học nhãn khoa**: Thấu kính phân kì được dùng làm kính đeo sửa tật cận thị, còn thấu kính hội tụ được dùng làm kính đeo sửa tật viễn thị và lão thị.""",
        "game_title": "Thử thách thực tế: Quang học và Thấu kính",
        "game_description": "Dịch chuyển vật sáng và màn hứng ảnh trên giá quang học để vẽ đường truyền tia sáng, đo tiêu cự và lấy nét ảnh.",
        "game_type": "game_quanghoc",
        "quiz": [
            mcq(
                "biet",
                r"Chiếu một tia sáng đi qua quang tâm $O$ của một thấu kính (hội tụ hoặc phân kì) thì tia ló sẽ:",
                [
                    r"Đi qua tiêu điểm chính $F'$ của thấu kính",
                    r"Truyền song song với trục chính của thấu kính",
                    r"Tiếp tục truyền thẳng theo phương của tia tới mà không bị đổi hướng",
                    r"Phản xạ ngược trở lại theo đường cũ",
                ],
                2,
                r"Mọi tia sáng đi qua quang tâm $O$ của thấu kính đều tiếp tục truyền thẳng theo phương của tia tới.",
            ),
            mcq(
                "biet",
                r"Đặc điểm của ảnh tạo bởi một vật thật đặt trước thấu kính phân kì ở mọi vị trí ($d > 0$) là:",
                [
                    r"Ảnh thật, ngược chiều và nhỏ hơn vật",
                    r"Ảnh ảo, cùng chiều và lớn hơn vật",
                    r"Ảnh ảo, cùng chiều, nhỏ hơn vật và nằm trong khoảng tiêu cự",
                    r"Ảnh thật, cùng chiều và bằng vật",
                ],
                2,
                r"Vật thật đặt trước thấu kính phân kì luôn cho ảnh ảo, cùng chiều, nhỏ hơn vật và nằm trong khoảng từ quang tâm $O$ đến tiêu điểm $F$.",
            ),
            mcq(
                "biet",
                r"Khi dùng kính lúp có tiêu cự $f$ để quan sát một vật nhỏ, ta phải đặt vật ở vị trí nào trước kính để nhìn thấy ảnh ảo lớn hơn vật?",
                [
                    r"Đặt vật cách kính một khoảng lớn hơn $2f$ ($d > 2f$)",
                    r"Đặt vật cách kính một khoảng đúng bằng $2f$ ($d = 2f$)",
                    r"Đặt vật trong khoảng tiêu cự của kính ($d < f$)",
                    r"Đặt vật ngoài khoảng tiêu cự ($f < d < 2f$)",
                ],
                2,
                r"Kính lúp là thấu kính hội tụ có tiêu cự ngắn; để tạo ảnh ảo lớn hơn vật thì vật phải đặt trong khoảng tiêu cự ($d < f$).",
            ),
            mcq(
                "biet",
                r"Trong bài thực hành đo tiêu cự của thấu kính hội tụ, khi điều chỉnh sao cho ảnh thật trên màn cao bằng vật ($h' = h$) và $d = d'$ thì tiêu cự $f$ được tính theo khoảng cách $L = d + d'$ từ vật đến màn bằng công thức:",
                [r"$f = \dfrac{L}{2}$", r"$f = \dfrac{L}{4}$", r"$f = 2L$", r"$f = L$"],
                1,
                r"Khi ảnh thật cao bằng vật thì $d = d' = 2f \Rightarrow L = d + d' = 4f \Rightarrow f = \dfrac{L}{4}$.",
            ),
            mcq(
                "hieu",
                r"Trên vành của một chiếc kính lúp có ghi kí hiệu $5\text{x}$. Tiêu cự $f$ của chiếc kính lúp này là bao nhiêu?",
                [r"$2{,}5\text{ cm}$", r"$5\text{ cm}$", r"$10\text{ cm}$", r"$25\text{ cm}$"],
                1,
                r"Áp dụng công thức số bội giác trên kính lúp: $G = \dfrac{25}{f} \Rightarrow f = \dfrac{25}{G} = \dfrac{25}{5} = 5\text{ cm}$.",
            ),
            mcq(
                "hieu",
                r"Đặt một vật sáng $AB$ vuông góc với trục chính của một thấu kính hội tụ có tiêu cự $f = 10\text{ cm}$, cách thấu kính một khoảng $d = 15\text{ cm}$. Khoảng cách $d'$ từ ảnh $A'B'$ đến thấu kính là:",
                [r"$6\text{ cm}$", r"$20\text{ cm}$", r"$30\text{ cm}$", r"$25\text{ cm}$"],
                2,
                r"Vì $d = 15\text{ cm} > f = 10\text{ cm}$ nên thấu kính cho ảnh thật: $d' = \dfrac{d \cdot f}{d - f} = \dfrac{15 \cdot 10}{15 - 10} = 30\text{ cm}$.",
            ),
            tf4(
                "hieu",
                r"Một vật sáng $AB$ cao $h = 3\text{ cm}$ đặt vuông góc với trục chính của một thấu kính phân kì có độ lớn tiêu cự $f = 12\text{ cm}$, cách thấu kính một khoảng $d = 24\text{ cm}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Chùm tia ló ra khỏi thấu kính phân kì là chùm tia phân kì nên không thể hứng được ảnh trên màn chắn.",
                    r"b) Ảnh $A'B'$ của vật $AB$ là ảnh ảo, cùng chiều với vật.",
                    r"c) Khoảng cách từ ảnh ảo $A'B'$ đến thấu kính phân kì là $d' = 8\text{ cm}$.",
                    r"d) Chiều cao của ảnh $A'B'$ bằng $2\text{ cm}$.",
                ],
                [True, True, True, False],
                r"a) Đúng vì ảnh ảo không hứng được trên màn chắn. b) Đúng. c) Đúng vì đối với thấu kính phân kì: $d' = \dfrac{d \cdot f}{d + f} = \dfrac{24 \cdot 12}{24 + 12} = 8\text{ cm}$. d) Sai vì chiều cao của ảnh là $h' = h \cdot \dfrac{d'}{d} = 3 \cdot \dfrac{8}{24} = 1\text{ cm}$.",
            ),
            tf4(
                "hieu",
                r"Đặt một vật sáng $AB$ cao $h = 2\text{ cm}$ vuông góc với trục chính của một thấu kính hội tụ có tiêu cự $f = 15\text{ cm}$ tại vị trí cách thấu kính một khoảng $d = 10\text{ cm}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Vì $d < f$ nên ảnh $A'B'$ tạo bởi thấu kính hội tụ là ảnh ảo, cùng chiều và lớn hơn vật.",
                    r"b) Ảnh $A'B'$ nằm cùng phía với vật $AB$ so với thấu kính và cách thấu kính một đoạn $d' = 30\text{ cm}$.",
                    r"c) Chiều cao của ảnh $A'B'$ là $h' = 6\text{ cm}$.",
                    r"d) Nếu dịch chuyển vật ra xa thấu kính tới vị trí $d = 30\text{ cm}$ thì ảnh thu được vẫn là ảnh ảo.",
                ],
                [True, True, True, False],
                r"a) Đúng vì $d = 10\text{ cm} < f = 15\text{ cm}$. b) Đúng vì $\dfrac{1}{f} = \dfrac{1}{d} - \dfrac{1}{d'} \Rightarrow d' = \dfrac{d \cdot f}{f - d} = \dfrac{10 \cdot 15}{15 - 10} = 30\text{ cm}$. c) Đúng vì $h' = h \cdot \dfrac{d'}{d} = 2 \cdot \dfrac{30}{10} = 6\text{ cm}$. d) Sai vì khi $d = 30\text{ cm} = 2f > f$ thì ảnh thu được là ảnh thật, ngược chiều và cao bằng vật.",
            ),
            mcq(
                "vandung",
                r"Đặt một vật sáng phẳng vuông góc với trục chính của một thấu kính hội tụ có tiêu cự $f = 20\text{ cm}$. Để thu được trên màn chắn một ảnh thật cao gấp $4$ lần vật ($h' = 4h$) thì phải đặt vật cách thấu kính một khoảng $d$ bằng bao nhiêu?",
                [r"$25\text{ cm}$", r"$15\text{ cm}$", r"$40\text{ cm}$", r"$80\text{ cm}$"],
                0,
                r"Vì ảnh thật cao gấp $4$ lần vật nên $\dfrac{h'}{h} = \dfrac{d'}{d} = 4 \Rightarrow d' = 4d$. Thay vào công thức ảnh thật của thấu kính hội tụ: $\dfrac{1}{f} = \dfrac{1}{d} + \dfrac{1}{4d} = \dfrac{5}{4d} \Rightarrow d = \dfrac{5f}{4} = \dfrac{5 \cdot 20}{4} = 25\text{ cm}$.",
            ),
            short(
                "vandung",
                r"Trong giờ thực hành đo tiêu cự thấu kính hội tụ, học sinh điều chỉnh vật sáng và màn ảnh đối xứng nhau qua thấu kính sao cho ảnh thật hiện rõ nét trên màn có chiều cao đúng bằng vật. Khi đó khoảng cách từ vật sáng đến màn ảnh đo được là $L = 64\text{ cm}$. Tính tiêu cự $f$ của thấu kính hội tụ đó theo đơn vị $\text{cm}$.",
                ["16"],
                r"Khi ảnh thật cao bằng vật thì $d = d' = 2f$, nên khoảng cách từ vật đến màn ảnh là $L = d + d' = 4f \Rightarrow f = \dfrac{L}{4} = \dfrac{64}{4} = 16\text{ cm}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 3: ĐIỆN TRỞ VÀ ĐỊNH LUẬT OHM =====================
    {
        "topic": "dien-tro",
        "title": "Điện trở, Định luật Ohm và Sự phụ thuộc của điện trở vào dây dẫn",
        "icon": "🎛️",
        "description": "Chương III · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống (Bài 11): Khái niệm điện trở, đường đặc trưng vôn – ampe, định luật Ohm, công thức tính điện trở của dây dẫn theo chiều dài, tiết diện, điện trở suất và biến trở.",
        "requirements": [
            r"Thực hiện thí nghiệm đơn giản để nêu được điện trở có tác dụng cản trở dòng điện và khảo sát sự phụ thuộc của cường độ dòng điện vào hiệu điện thế giữa hai đầu đoạn dây dẫn.",
            r"Nêu được mối quan hệ tỉ lệ thuận giữa cường độ dòng điện và hiệu điện thế; phát biểu và vận dụng được định luật Ohm: $I = \dfrac{U}{R}$.",
            r"Nêu được đơn vị đo điện trở ($\Omega$, $\text{k}\Omega$, $\text{M}\Omega$) và xác định được giá trị điện trở bằng vôn kế và ampe kế.",
            r"Nêu được công thức tính điện trở của một đoạn dây dẫn theo chiều dài, tiết diện, điện trở suất: $R = \rho \dfrac{l}{S}$; vận dụng được công thức này để tính toán và giải thích nguyên lí hoạt động của biến trở.",
        ],
        "definition": r"""- **Điện trở** ($R$) của một dây dẫn là đại lượng đặc trưng cho mức độ cản trở dòng điện nhiều hay ít của dây dẫn đó (đơn vị: ôm, kí hiệu $\Omega$, với $1\text{ }\Omega = \dfrac{1\text{ V}}{1\text{ A}}$).
- **Định luật Ohm**: Cường độ dòng điện chạy qua một đoạn dây dẫn tỉ lệ thuận với hiệu điện thế giữa hai đầu đoạn dây và tỉ lệ nghịch với điện trở của nó: $I = \dfrac{U}{R}$.
- **Điện trở của dây dẫn hình trụ đồng chất**: $R = \rho \dfrac{l}{S}$.""",
        "theory": r"""### Bài 11. Điện trở. Định luật Ohm
- **Thí nghiệm khảo sát và đồ thị đặc trưng vôn – ampe**: Khi thay đổi hiệu điện thế $U$ đặt vào hai đầu một đoạn dây dẫn kim loại (ở nhiệt độ không đổi), cường độ dòng điện $I$ chạy qua dây dẫn tăng giảm tỉ lệ thuận với hiệu điện thế: $\dfrac{U_1}{U_2} = \dfrac{I_1}{I_2}$. Đồ thị biểu diễn sự phụ thuộc của $I$ vào $U$ là một **đường thẳng đi qua gốc tọa độ** $O(0; 0)$.
- **Khái niệm điện trở và định luật Ohm**: Thương số $R = \dfrac{U}{I}$ không đổi đối với mỗi dây dẫn nhất định và được gọi là điện trở của dây dẫn đó. Định luật Ohm được biểu diễn bởi công thức $I = \dfrac{U}{R}$ (suy ra $U = I \cdot R$ và $R = \dfrac{U}{I}$). Lưu ý: Điện trở $R$ là thuộc tính bản chất của vật dẫn, **không phụ thuộc vào $U$ và $I$** (khi $U = 0$ thì $I = 0$ nhưng điện trở $R$ của dây dẫn vẫn giữ nguyên giá trị).
- **Đơn vị điện trở**: $1\text{ }\Omega = 1\text{ V/A}$; các bội số thường dùng là ki-lô-ôm ($1\text{ k}\Omega = 1000\text{ }\Omega = 10^3\text{ }\Omega$) và mê-ga-ôm ($1\text{ M}\Omega = 1000000\text{ }\Omega = 10^6\text{ }\Omega$).
- **Công thức tính điện trở của đoạn dây dẫn**: Điện trở $R$ của một đoạn dây dẫn tỉ lệ thuận với chiều dài $l$ ($\text{m}$) của dây, tỉ lệ nghịch với tiết diện ngang $S$ ($\text{m}^2$) của dây và phụ thuộc vào vật liệu làm dây dẫn: $R = \rho \dfrac{l}{S}$.
- **Điện trở suất ($\rho$)**: Là điện trở của một đoạn dây dẫn hình trụ có chiều dài $1\text{ m}$ và tiết diện $1\text{ m}^2$, đơn vị là ôm mét ($\Omega\cdot\text{m}$). Điện trở suất của vật liệu càng nhỏ thì vật liệu đó dẫn điện càng tốt (ví dụ ở $20^\circ\text{C}$: bạc $\rho_{\text{Ag}} = 1{,}6 \cdot 10^{-8}\text{ }\Omega\cdot\text{m}$; đồng $\rho_{\text{Cu}} = 1{,}7 \cdot 10^{-8}\text{ }\Omega\cdot\text{m}$; nhôm $\rho_{\text{Al}} = 2{,}8 \cdot 10^{-8}\text{ }\Omega\cdot\text{m}$; hợp kim nicrom $\rho \approx 1{,}1 \cdot 10^{-6}\text{ }\Omega\cdot\text{m}$).
- **Biến trở**: Là điện trở có thể thay đổi trị số (như biến trở con chạy, chiết áp) dựa trên việc thay đổi chiều dài $l$ của phần cuộn dây hợp kim có dòng điện chạy qua, dùng để điều chỉnh cường độ dòng điện trong mạch (điều chỉnh độ sáng đèn, âm lượng loa).""",
        "formulas": [
            G(
                "I. Định luật Ohm và đơn vị điện trở",
                F("Hệ thức định luật Ohm", r"$I = \dfrac{U}{R} \Rightarrow U = I \cdot R;\quad R = \dfrac{U}{I}$", r"$I$ ($\text{A}$), $U$ ($\text{V}$), $R$ ($\Omega$)"),
                F("Tỉ lệ trên cùng một dây dẫn", r"$\dfrac{I_1}{I_2} = \dfrac{U_1}{U_2}$", r"Khi $U$ tăng bao nhiêu lần thì $I$ tăng bấy nhiêu lần ($R$ không đổi)"),
                F("Quy đổi đơn vị điện trở", r"$1\text{ k}\Omega = 10^3\text{ }\Omega = 1000\text{ }\Omega;\quad 1\text{ M}\Omega = 10^6\text{ }\Omega$", r""),
            ),
            G(
                "II. Sự phụ thuộc của điện trở vào dây dẫn",
                F("Công thức tính điện trở dây dẫn", r"$R = \rho \dfrac{l}{S} \Rightarrow l = \dfrac{R \cdot S}{\rho};\quad S = \dfrac{\rho \cdot l}{R}$", r"$\rho$ ($\Omega\cdot\text{m}$), $l$ ($\text{m}$), $S$ ($\text{m}^2$)"),
                F("Tiết diện dây dẫn tròn và đổi đơn vị tiết diện", r"$S = \pi r^2 = \dfrac{\pi d^2}{4};\quad 1\text{ mm}^2 = 10^{-6}\text{ m}^2$", r"Nếu đường kính $d$ tăng $2$ lần thì $S$ tăng $4$ lần $\Rightarrow R$ giảm $4$ lần"),
            ),
        ],
        "example": r"Một cuộn dây dẫn bằng đồng có chiều dài $l = 100\text{ m}$ và tiết diện ngang $S = 2\text{ mm}^2$. Biết điện trở suất của đồng là $\rho = 1{,}7 \cdot 10^{-8}\text{ }\Omega\cdot\text{m}$. Tính điện trở $R$ của cuộn dây đồng và cường độ dòng điện $I$ chạy qua cuộn dây khi đặt vào hai đầu dây một hiệu điện thế $U = 3{,}4\text{ V}$.",
        "example_answer": r"""- Đổi đơn vị tiết diện dây dẫn:
$$S = 2\text{ mm}^2 = 2 \cdot 10^{-6}\text{ m}^2$$
- Điện trở của cuộn dây đồng là:
$$R = \rho \dfrac{l}{S} = 1{,}7 \cdot 10^{-8} \cdot \dfrac{100}{2 \cdot 10^{-6}} = 0{,}85\text{ }\Omega$$
- Áp dụng định luật Ohm, cường độ dòng điện chạy qua cuộn dây là:
$$I = \dfrac{U}{R} = \dfrac{3{,}4}{0{,}85} = 4\text{ A}$$""",
        "real_life": r"""- **Lựa chọn vật liệu kĩ thuật điện**: Dây dẫn tải điện trong gia đình thường làm bằng đồng có $\rho$ rất nhỏ để giảm hao phí nhiệt; ngược lại dây đốt nóng của bàn là, bếp hồng ngoại làm bằng hợp kim nicrom hoặc constantan có $\rho$ lớn và chịu được nhiệt độ cao.
- **Điều khiển thiết bị**: Chiết áp vặn chỉnh âm lượng trên amply, núm chỉnh tốc độ quạt trần và độ sáng đèn bàn học đều là ứng dụng trực tiếp của biến trở.""",
        "game_title": "Thử thách thực tế: Điện trở và Định luật Ohm",
        "game_description": "Thay đổi hiệu điện thế, chiều dài, tiết diện dây dẫn và dịch chuyển con chạy biến trở để kiểm nghiệm định luật Ohm.",
        "game_type": "game_ohm",
        "quiz": [
            mcq(
                "biet",
                r"Biểu thức nào dưới đây là hệ thức của định luật Ohm đối với một đoạn dây dẫn có điện trở $R$?",
                [r"$I = U \cdot R$", r"$I = \dfrac{U}{R}$", r"$I = \dfrac{R}{U}$", r"$R = U \cdot I$"],
                1,
                r"Theo định luật Ohm, cường độ dòng điện tỉ lệ thuận với hiệu điện thế và tỉ lệ nghịch với điện trở: $I = \dfrac{U}{R}$.",
            ),
            mcq(
                "biet",
                r"Đồ thị biểu diễn sự phụ thuộc của cường độ dòng điện $I$ chạy qua một dây dẫn vào hiệu điện thế $U$ đặt vào hai đầu dây dẫn đó có dạng là:",
                [
                    r"Một đường thẳng đi qua gốc tọa độ $O(0; 0)$",
                    r"Một đường cong parabol",
                    r"Một đường thẳng song song với trục hoành",
                    r"Một đường tròn tâm $O$",
                ],
                0,
                r"Vì $I = \dfrac{1}{R} U$ ($I$ tỉ lệ thuận với $U$) nên đồ thị đặc trưng vôn – ampe là một đường thẳng đi qua gốc tọa độ $O(0; 0)$.",
            ),
            mcq(
                "biet",
                r"Công thức tính điện trở $R$ của một đoạn dây dẫn có chiều dài $l$, tiết diện đều $S$ và làm bằng vật liệu có điện trở suất $\rho$ là:",
                [r"$R = \rho \cdot l \cdot S$", r"$R = \dfrac{\rho \cdot S}{l}$", r"$R = \rho \dfrac{l}{S}$", r"$R = \dfrac{l}{\rho \cdot S}$"],
                2,
                r"Điện trở dây dẫn tỉ lệ thuận với chiều dài $l$, tỉ lệ nghịch với tiết diện $S$ và phụ thuộc vào điện trở suất $\rho$: $R = \rho \dfrac{l}{S}$.",
            ),
            mcq(
                "biet",
                r"Đơn vị đo của điện trở suất $\rho$ trong hệ đo lường quốc tế SI là:",
                [r"$\Omega$", r"$\Omega/\text{m}$", r"$\Omega\cdot\text{m}$", r"$\Omega/\text{m}^2$"],
                2,
                r"Từ công thức $\rho = \dfrac{R \cdot S}{l}$, với $R$ đo bằng $\Omega$, $S$ đo bằng $\text{m}^2$ và $l$ đo bằng $\text{m}$, đơn vị của điện trở suất là ôm mét ($\Omega\cdot\text{m}$).",
            ),
            mcq(
                "hieu",
                r"Khi đặt vào hai đầu một dây dẫn hiệu điện thế $U_1 = 6\text{ V}$ thì cường độ dòng điện chạy qua nó là $I_1 = 0{,}4\text{ A}$. Nếu tăng hiệu điện thế đặt vào hai đầu dây dẫn đó thêm $3\text{ V}$ nữa thì cường độ dòng điện chạy qua dây dẫn là:",
                [r"$0{,}2\text{ A}$", r"$0{,}6\text{ A}$", r"$0{,}8\text{ A}$", r"$1{,}2\text{ A}$"],
                1,
                r"Điện trở của dây dẫn là $R = \dfrac{U_1}{I_1} = \dfrac{6}{0{,}4} = 15\text{ }\Omega$. Khi tăng hiệu điện thế thêm $3\text{ V}$ thì $U_2 = 6 + 3 = 9\text{ V}$, suy ra $I_2 = \dfrac{U_2}{R} = \dfrac{9}{15} = 0{,}6\text{ A}$.",
            ),
            mcq(
                "hieu",
                r"Hai dây dẫn bằng đồng có cùng chiều dài. Dây thứ nhất có tiết diện $S_1 = 0{,}5\text{ mm}^2$ và điện trở $R_1 = 12\text{ }\Omega$; dây thứ hai có tiết diện $S_2 = 1{,}5\text{ mm}^2$. Điện trở $R_2$ của dây thứ hai bằng:",
                [r"$36\text{ }\Omega$", r"$4\text{ }\Omega$", r"$6\text{ }\Omega$", r"$18\text{ }\Omega$"],
                1,
                r"Cùng vật liệu và cùng chiều dài thì điện trở tỉ lệ nghịch với tiết diện: $\dfrac{R_2}{R_1} = \dfrac{S_1}{S_2} = \dfrac{0{,}5}{1{,}5} = \dfrac{1}{3} \Rightarrow R_2 = \dfrac{12}{3} = 4\text{ }\Omega$.",
            ),
            tf4(
                "hieu",
                r"Đặt hiệu điện thế $U = 12\text{ V}$ vào hai đầu một điện trở $R = 24\text{ }\Omega$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Cường độ dòng điện chạy qua điện trở khi đó là $I = 0{,}5\text{ A}$.",
                    r"b) Nếu tăng hiệu điện thế giữa hai đầu điện trở lên gấp đôi ($U' = 24\text{ V}$) thì giá trị điện trở $R$ cũng tăng lên gấp đôi thành $48\text{ }\Omega$.",
                    r"c) Nếu ngắt nguồn điện để hiệu điện thế hai đầu điện trở bằng $0\text{ V}$ thì điện trở của vật dẫn đó vẫn bằng $24\text{ }\Omega$.",
                    r"d) Để cường độ dòng điện chạy qua điện trở này đạt $0{,}75\text{ A}$ thì hiệu điện thế đặt vào hai đầu nó phải bằng $18\text{ V}$.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $I = \dfrac{U}{R} = \dfrac{12}{24} = 0{,}5\text{ A}$. b) Sai vì điện trở $R$ chỉ phụ thuộc vào bản chất và kích thước dây dẫn, không phụ thuộc vào $U$; khi $U$ tăng gấp đôi thì $I$ tăng gấp đôi còn $R = 24\text{ }\Omega$ không đổi. c) Đúng. d) Đúng vì $U = I \cdot R = 0{,}75 \cdot 24 = 18\text{ V}$.",
            ),
            tf4(
                "hieu",
                r"Một dây dẫn bằng hợp kim nicrom có điện trở suất $\rho = 1{,}1 \cdot 10^{-6}\text{ }\Omega\cdot\text{m}$, chiều dài $l = 30\text{ m}$ và tiết diện đều $S = 0{,}5\text{ mm}^2$ được dùng để quấn một biến trở con chạy. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Tiết diện của dây dẫn khi đổi sang đơn vị chuẩn SI là $S = 0{,}5 \cdot 10^{-6}\text{ m}^2$.",
                    r"b) Điện trở lớn nhất của biến trở con chạy này là $R_{\max} = 66\text{ }\Omega$.",
                    r"c) Khi dịch chuyển con chạy để chiều dài phần dây dẫn có dòng điện chạy qua giảm đi một nửa thì điện trở của biến trở tăng lên gấp đôi.",
                    r"d) Nếu thay dây nicrom bằng dây đồng có cùng kích thước ($l = 30\text{ m}, S = 0{,}5\text{ mm}^2$, biết $\rho_{\text{Cu}} = 1{,}7 \cdot 10^{-8}\text{ }\Omega\cdot\text{m}$) thì điện trở lớn nhất chỉ còn $1{,}02\text{ }\Omega$.",
                ],
                [True, True, False, True],
                r"a) Đúng vì $1\text{ mm}^2 = 10^{-6}\text{ m}^2$. b) Đúng vì $R_{\max} = \rho \dfrac{l}{S} = 1{,}1 \cdot 10^{-6} \cdot \dfrac{30}{0{,}5 \cdot 10^{-6}} = 66\text{ }\Omega$. c) Sai vì $R$ tỉ lệ thuận với chiều dài $l$, nên $l$ giảm một nửa thì $R$ giảm một nửa. d) Đúng vì $R_{\text{Cu}} = 1{,}7 \cdot 10^{-8} \cdot \dfrac{30}{0{,}5 \cdot 10^{-6}} = 1{,}02\text{ }\Omega$.",
            ),
            mcq(
                "vandung",
                r"Hai dây dẫn hình trụ tròn đều được làm từ cùng một loại kim loại. Dây thứ nhất có chiều dài $l_1 = 2l_2$ và đường kính tiết diện $d_1 = 2d_2$. Tỉ số điện trở $\dfrac{R_1}{R_2}$ của hai dây dẫn đó bằng:",
                [r"$1$", r"$2$", r"$\dfrac{1}{2}$", r"$\dfrac{1}{4}$"],
                2,
                r"Vì tiết diện hình tròn là $S = \dfrac{\pi d^2}{4}$ nên $\dfrac{S_1}{S_2} = \left(\dfrac{d_1}{d_2}\right)^2 = 2^2 = 4$. Khi đó $\dfrac{R_1}{R_2} = \dfrac{l_1}{l_2} \cdot \dfrac{S_2}{S_1} = 2 \cdot \dfrac{1}{4} = \dfrac{1}{2}$.",
            ),
            short(
                "vandung",
                r"Một cuộn dây dẫn bằng nhôm có điện trở suất $\rho = 2{,}8 \cdot 10^{-8}\text{ }\Omega\cdot\text{m}$ và tiết diện đều $S = 1{,}4\text{ mm}^2$. Khi đặt vào hai đầu cuộn dây hiệu điện thế $U = 14\text{ V}$ thì cường độ dòng điện chạy qua cuộn dây là $I = 2{,}5\text{ A}$. Tính chiều dài $l$ của cuộn dây nhôm đó theo đơn vị mét ($\text{m}$).",
                ["280"],
                r"Điện trở của cuộn dây nhôm là $R = \dfrac{U}{I} = \dfrac{14}{2{,}5} = 5{,}6\text{ }\Omega$. Đổi $S = 1{,}4\text{ mm}^2 = 1{,}4 \cdot 10^{-6}\text{ m}^2$. Chiều dài của cuộn dây là $l = \dfrac{R \cdot S}{\rho} = \dfrac{5{,}6 \cdot 1{,}4 \cdot 10^{-6}}{2{,}8 \cdot 10^{-8}} = 280\text{ m}$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 4: ĐOẠN MẠCH NỐI TIẾP =====================
    {
        "topic": "doan-mach-noi-tiep",
        "title": "Đoạn mạch nối tiếp",
        "icon": "🔗",
        "description": "Chương III · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống (Bài 12 – Phần I): Sơ đồ đoạn mạch nối tiếp, tính chất cường độ dòng điện, hiệu điện thế, công thức tính điện trở tương đương và quy tắc phân áp trong đoạn mạch nối tiếp.",
        "requirements": [
            r"Vẽ được sơ đồ và lắp được đoạn mạch điện nối tiếp gồm các điện trở hoặc bóng đèn.",
            r"Nêu được mối liên hệ về cường độ dòng điện ($I = I_1 = I_2 = \dots = I_n$) và hiệu điện thế ($U = U_1 + U_2 + \dots + U_n$) trong đoạn mạch nối tiếp.",
            r"Thực hiện thí nghiệm rút ra được: trong đoạn mạch điện mắc nối tiếp, điện trở tương đương bằng tổng các điện trở thành phần: $R_{\text{tđ}} = R_1 + R_2 + \dots + R_n$.",
            r"Tính được điện trở tương đương, cường độ dòng điện và hiệu điện thế trên từng điện trở trong đoạn mạch một chiều nối tiếp trong một số trường hợp đơn giản.",
        ],
        "definition": r"""- **Đoạn mạch nối tiếp** là đoạn mạch gồm các điện trở (hoặc thiết bị điện) được mắc liên tiếp với nhau thành một dãy duy nhất không có điểm rẽ nhánh.
- **Tính chất cơ bản**:
  + Cường độ dòng điện có giá trị như nhau tại mọi điểm: $I = I_1 = I_2 = \dots = I_n$.
  + Hiệu điện thế hai đầu đoạn mạch bằng tổng các hiệu điện thế thành phần: $U = U_1 + U_2 + \dots + U_n$.
  + Điện trở tương đương bằng tổng các điện trở thành phần: $R_{\text{tđ}} = R_1 + R_2 + \dots + R_n$.""",
        "theory": r"""### Bài 12. Đoạn mạch nối tiếp, song song (Phần I: Đoạn mạch nối tiếp)
- **Cường độ dòng điện và hiệu điện thế trong đoạn mạch nối tiếp**: Trong đoạn mạch gồm hai điện trở $R_1$ và $R_2$ mắc nối tiếp, dòng điện chỉ có một đường truyền duy nhất nên cường độ dòng điện chạy qua các điện trở là bằng nhau: $I = I_1 = I_2$. Hiệu điện thế giữa hai đầu cả đoạn mạch bằng tổng hiệu điện thế trên mỗi điện trở: $U = U_1 + U_2$.
- **Điện trở tương đương của đoạn mạch nối tiếp**: Điện trở tương đương ($R_{\text{tđ}}$) của một đoạn mạch là điện trở có thể thay thế cho các điện trở trong mạch sao cho với cùng hiệu điện thế $U$ thì cường độ dòng điện $I$ chạy qua mạch vẫn không thay đổi. Từ $U = U_1 + U_2 \iff I \cdot R_{\text{tđ}} = I \cdot R_1 + I \cdot R_2$, ta rút ra công thức: $R_{\text{tđ}} = R_1 + R_2$. Mở rộng cho $n$ điện trở mắc nối tiếp: $R_{\text{tđ}} = R_1 + R_2 + \dots + R_n$. Như vậy, điện trở tương đương của đoạn mạch nối tiếp luôn **lớn hơn** mỗi điện trở thành phần.
- **Hệ quả phân áp (chia hiệu điện thế)**: Vì $I_1 = I_2 \iff \dfrac{U_1}{R_1} = \dfrac{U_2}{R_2}$ nên $\dfrac{U_1}{U_2} = \dfrac{R_1}{R_2}$. Trong đoạn mạch nối tiếp, hiệu điện thế giữa hai đầu mỗi điện trở tỉ lệ thuận với giá trị điện trở đó (điện trở nào lớn hơn thì chịu hiệu điện thế lớn hơn).
- **Ưu, nhược điểm và ứng dụng**: Mắc nối tiếp thêm một điện trở bảo vệ (hoặc biến trở) giúp hạn chế dòng điện và giảm bớt hiệu điện thế đặt vào thiết bị (như bảo vệ bóng đèn LED khi dùng nguồn có điện áp lớn hơn điện áp định mức của đèn). Tuy nhiên, nếu một thiết bị trong dãy nối tiếp bị đứt mạch thì toàn bộ mạch điện bị hở và các thiết bị còn lại đều ngừng hoạt động.""",
        "formulas": [
            G(
                "I. Các hệ thức cơ bản của đoạn mạch nối tiếp",
                F("Cường độ dòng điện", r"$I = I_1 = I_2 = \dots = I_n = \dfrac{U}{R_{\text{tđ}}}$", r"Bằng nhau tại mọi vị trí trên đoạn mạch"),
                F("Hiệu điện thế toàn mạch", r"$U = U_1 + U_2 + \dots + U_n$", r"Tổng các hiệu điện thế thành phần"),
                F("Điện trở tương đương", r"$R_{\text{tđ}} = R_1 + R_2 + \dots + R_n$", r"Nếu có $n$ điện trở giống nhau $R_0$: $R_{\text{tđ}} = n \cdot R_0$"),
            ),
            G(
                "II. Quy tắc phân áp và điện trở bảo vệ",
                F("Tỉ lệ hiệu điện thế giữa hai điện trở nối tiếp", r"$\dfrac{U_1}{U_2} = \dfrac{R_1}{R_2}$", r"Hiệu điện thế tỉ lệ thuận với điện trở"),
                F("Công thức tính nhanh $U_1, U_2$ theo $U$", r"$U_1 = U \cdot \dfrac{R_1}{R_1 + R_2};\quad U_2 = U \cdot \dfrac{R_2}{R_1 + R_2}$", r""),
                F(r"Điện trở hạn dòng mắc nối tiếp với đèn ($U_{\text{Đ}}, I_{\text{Đ}}$)", r"$R_{\text{bảo vệ}} = \dfrac{U - U_{\text{Đ}}}{I_{\text{Đ}}}$", r"Với hiệu điện thế nguồn $U > U_{\text{Đ}}$"),
            ),
        ],
        "example": r"Cho hai điện trở $R_1 = 15\text{ }\Omega$ và $R_2 = 25\text{ }\Omega$ được mắc nối tiếp với nhau vào hai cực của nguồn điện có hiệu điện thế không đổi $U = 12\text{ V}$. Tính điện trở tương đương của đoạn mạch, cường độ dòng điện chạy trong mạch và hiệu điện thế giữa hai đầu mỗi điện trở.",
        "example_answer": r"""- Điện trở tương đương của đoạn mạch nối tiếp là:
$$R_{\text{tđ}} = R_1 + R_2 = 15 + 25 = 40\text{ }\Omega$$
- Cường độ dòng điện chạy trong đoạn mạch và qua mỗi điện trở là:
$$I = I_1 = I_2 = \dfrac{U}{R_{\text{tđ}}} = \dfrac{12}{40} = 0{,}3\text{ A}$$
- Hiệu điện thế giữa hai đầu mỗi điện trở là:
$$U_1 = I_1 \cdot R_1 = 0{,}3 \cdot 15 = 4{,}5\text{ V}$$
$$U_2 = I_2 \cdot R_2 = 0{,}3 \cdot 25 = 7{,}5\text{ V}\quad (\text{Kiểm tra: } U_1 + U_2 = 4{,}5 + 7{,}5 = 12\text{ V} = U)$$""",
        "real_life": r"""- **Bảo vệ linh kiện điện tử**: Khi mắc một bóng đèn LED (chỉ chịu được $U_{\text{Đ}} \approx 2\text{ V} - 3\text{ V}$) vào nguồn $5\text{ V}$ hay $9\text{ V}$, người ta luôn mắc nối tiếp một điện trở hạn dòng để gánh bớt điện áp dư, giữ cho LED không bị cháy.
- **Thiết bị đóng ngắt và bảo vệ**: Công tắc, cầu chì và aptomat luôn được mắc nối tiếp với thiết bị điện cần điều khiển hoặc bảo vệ để khi ngắt mạch thì dòng điện qua thiết bị lập tức bằng $0$.""",
        "game_title": "Thử thách thực tế: Đoạn mạch nối tiếp",
        "game_description": "Lựa chọn các điện trở mắc nối tiếp để thiết kế cầu phân áp và bảo vệ đèn LED hoạt động đúng cường độ dòng điện định mức.",
        "game_type": "game_doanmachnoitiep",
        "quiz": [
            mcq(
                "biet",
                r"Trong đoạn mạch gồm hai điện trở $R_1$ và $R_2$ mắc nối tiếp, hệ thức nào sau đây là ĐÚNG?",
                [
                    r"$I = I_1 + I_2$",
                    r"$U = U_1 = U_2$",
                    r"$R_{\text{tđ}} = R_1 + R_2$",
                    r"$\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$",
                ],
                2,
                r"Trong đoạn mạch nối tiếp, điện trở tương đương bằng tổng các điện trở thành phần: $R_{\text{tđ}} = R_1 + R_2$.",
            ),
            mcq(
                "biet",
                r"Mắc nối tiếp ba điện trở $R_1 = 10\text{ }\Omega$, $R_2 = 15\text{ }\Omega$ và $R_3 = 25\text{ }\Omega$. Điện trở tương đương $R_{\text{tđ}}$ của đoạn mạch này bằng:",
                [r"$50\text{ }\Omega$", r"$40\text{ }\Omega$", r"$25\text{ }\Omega$", r"$5\text{ }\Omega$"],
                0,
                r"Ta có $R_{\text{tđ}} = R_1 + R_2 + R_3 = 10 + 15 + 25 = 50\text{ }\Omega$.",
            ),
            mcq(
                "biet",
                r"Khi hai điện trở $R_1$ và $R_2$ được mắc nối tiếp vào một nguồn điện không đổi, tỉ số hiệu điện thế $\dfrac{U_1}{U_2}$ giữa hai đầu mỗi điện trở thỏa mãn hệ thức nào?",
                [
                    r"$\dfrac{U_1}{U_2} = \dfrac{R_2}{R_1}$",
                    r"$\dfrac{U_1}{U_2} = \dfrac{R_1}{R_2}$",
                    r"$U_1 \cdot R_1 = U_2 \cdot R_2$",
                    r"$U_1 = U_2$",
                ],
                1,
                r"Vì $I_1 = I_2 \iff \dfrac{U_1}{R_1} = \dfrac{U_2}{R_2} \Rightarrow \dfrac{U_1}{U_2} = \dfrac{R_1}{R_2}$.",
            ),
            mcq(
                "biet",
                r"Nếu một dây đèn trang trí gồm $20$ bóng đèn nhỏ mắc nối tiếp với nhau đang sáng mà có $1$ bóng đèn bị đứt dây tóc thì $19$ bóng đèn còn lại sẽ:",
                [
                    r"Sáng mạnh hơn lúc trước",
                    r"Vẫn sáng bình thường như cũ",
                    r"Tất cả đều tắt vì mạch điện bị hở",
                    r"Sáng yếu đi một chút",
                ],
                2,
                r"Trong đoạn mạch nối tiếp, khi một bóng đèn bị đứt dây tóc thì toàn bộ mạch điện bị hở nên không còn dòng điện chạy qua các bóng còn lại.",
            ),
            mcq(
                "hieu",
                r"Hai điện trở $R_1 = 12\text{ }\Omega$ và $R_2 = 18\text{ }\Omega$ được mắc nối tiếp vào hai điểm có hiệu điện thế $U = 15\text{ V}$. Cường độ dòng điện chạy qua điện trở $R_1$ là:",
                [r"$1{,}25\text{ A}$", r"$0{,}83\text{ A}$", r"$0{,}5\text{ A}$", r"$2{,}0\text{ A}$"],
                2,
                r"Điện trở tương đương là $R_{\text{tđ}} = 12 + 18 = 30\text{ }\Omega$. Cường độ dòng điện qua $R_1$ bằng dòng điện mạch chính: $I_1 = I = \dfrac{U}{R_{\text{tđ}}} = \dfrac{15}{30} = 0{,}5\text{ A}$.",
            ),
            mcq(
                "hieu",
                r"Hai điện trở $R_1$ và $R_2 = 3R_1$ được mắc nối tiếp với nhau vào hiệu điện thế $U = 24\text{ V}$. Hiệu điện thế $U_2$ giữa hai đầu điện trở $R_2$ là:",
                [r"$6\text{ V}$", r"$8\text{ V}$", r"$16\text{ V}$", r"$18\text{ V}$"],
                3,
                r"Theo quy tắc phân áp: $U_2 = U \cdot \dfrac{R_2}{R_1 + R_2} = 24 \cdot \dfrac{3R_1}{R_1 + 3R_1} = 24 \cdot \dfrac{3}{4} = 18\text{ V}$.",
            ),
            tf4(
                "hieu",
                r"Cho mạch điện gồm hai điện trở $R_1 = 20\text{ }\Omega$ và $R_2 = 30\text{ }\Omega$ mắc nối tiếp với nhau. Biết ampe kế mắc trong mạch chỉ $I = 0{,}4\text{ A}$ (bỏ qua điện trở của ampe kế và dây nối). Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Điện trở tương đương của đoạn mạch bằng $50\text{ }\Omega$.",
                    r"b) Cường độ dòng điện chạy qua $R_1$ lớn hơn cường độ dòng điện chạy qua $R_2$ vì $R_1 < R_2$.",
                    r"c) Hiệu điện thế giữa hai đầu điện trở $R_1$ là $U_1 = 8\text{ V}$ và giữa hai đầu điện trở $R_2$ là $U_2 = 12\text{ V}$.",
                    r"d) Hiệu điện thế giữa hai đầu cả đoạn mạch là $U = 20\text{ V}$.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $R_{\text{tđ}} = 20 + 30 = 50\text{ }\Omega$. b) Sai vì trong đoạn mạch nối tiếp thì $I_1 = I_2 = I = 0{,}4\text{ A}$. c) Đúng vì $U_1 = 0{,}4 \cdot 20 = 8\text{ V}$ và $U_2 = 0{,}4 \cdot 30 = 12\text{ V}$. d) Đúng vì $U = U_1 + U_2 = 8 + 12 = 20\text{ V}$.",
            ),
            tf4(
                "hieu",
                r"Một bóng đèn nhỏ có hiệu điện thế định mức $U_{\text{Đ}} = 6\text{ V}$ và cường độ dòng điện định mức $I_{\text{Đ}} = 0{,}5\text{ A}$ được mắc nối tiếp với một biến trở $R_{\text{b}}$ vào nguồn điện có hiệu điện thế không đổi $U = 9\text{ V}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Điện trở của bóng đèn khi sáng bình thường là $R_{\text{Đ}} = 12\text{ }\Omega$.",
                    r"b) Để bóng đèn sáng bình thường thì cường độ dòng điện chạy qua biến trở phải bằng $0{,}5\text{ A}$.",
                    r"c) Khi đèn sáng bình thường, hiệu điện thế giữa hai đầu biến trở là $U_{\text{b}} = 9\text{ V}$.",
                    r"d) Giá trị của biến trở cần điều chỉnh để đèn sáng bình thường là $R_{\text{b}} = 6\text{ }\Omega$.",
                ],
                [True, True, False, True],
                r"a) Đúng vì $R_{\text{Đ}} = \dfrac{U_{\text{Đ}}}{I_{\text{Đ}}} = \dfrac{6}{0{,}5} = 12\text{ }\Omega$. b) Đúng vì biến trở mắc nối tiếp với đèn nên $I_{\text{b}} = I_{\text{Đ}} = 0{,}5\text{ A}$. c) Sai vì $U_{\text{b}} = U - U_{\text{Đ}} = 9 - 6 = 3\text{ V}$. d) Đúng vì $R_{\text{b}} = \dfrac{U_{\text{b}}}{I_{\text{b}}} = \dfrac{3}{0{,}5} = 6\text{ }\Omega$.",
            ),
            mcq(
                "vandung",
                r"Cho hai điện trở $R_1 = 15\text{ }\Omega$ (chịu được dòng điện tối đa $I_{1\max} = 1{,}2\text{ A}$) và $R_2 = 25\text{ }\Omega$ (chịu được dòng điện tối đa $I_{2\max} = 0{,}8\text{ A}$). Nếu mắc nối tiếp hai điện trở này với nhau thì hiệu điện thế tối đa $U_{\max}$ có thể đặt vào hai đầu đoạn mạch để không có điện trở nào bị hỏng là:",
                [r"$48\text{ V}$", r"$32\text{ V}$", r"$38\text{ V}$", r"$20\text{ V}$"],
                1,
                r"Khi mắc nối tiếp, dòng điện qua hai điện trở bằng nhau nên dòng điện tối đa cho phép trong mạch là $I_{\max} = \min(1{,}2\text{ A};\; 0{,}8\text{ A}) = 0{,}8\text{ A}$. Khi đó hiệu điện thế tối đa là $U_{\max} = I_{\max} \cdot (R_1 + R_2) = 0{,}8 \cdot (15 + 25) = 32\text{ V}$.",
            ),
            short(
                "vandung",
                r"Một bóng đèn LED có hiệu điện thế định mức $U_{\text{Đ}} = 2{,}5\text{ V}$ và cường độ dòng điện định mức $I_{\text{Đ}} = 20\text{ mA}$. Để mắc bóng đèn LED này vào nguồn điện $U = 12\text{ V}$ sao cho đèn sáng bình thường, cần phải mắc nối tiếp với đèn một điện trở bảo vệ $R$ có giá trị bằng bao nhiêu $\Omega$?",
                ["475"],
                r"Đổi $I_{\text{Đ}} = 20\text{ mA} = 0{,}02\text{ A}$. Hiệu điện thế trên điện trở bảo vệ khi đèn sáng bình thường là $U_R = U - U_{\text{Đ}} = 12 - 2{,}5 = 9{,}5\text{ V}$. Giá trị điện trở cần mắc nối tiếp là $R = \dfrac{U_R}{I_{\text{Đ}}} = \dfrac{9{,}5}{0{,}02} = 475\text{ }\Omega$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 5: ĐOẠN MẠCH SONG SONG =====================
    {
        "topic": "doan-mach-song-song",
        "title": "Đoạn mạch song song",
        "icon": "🔀",
        "description": "Chương III · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống (Bài 12 – Phần II): Sơ đồ đoạn mạch song song, tính chất hiệu điện thế, cường độ dòng điện, công thức tính điện trở tương đương, quy tắc phân dòng và mạng điện gia đình.",
        "requirements": [
            r"Vẽ được sơ đồ và lắp được đoạn mạch điện mắc song song gồm các điện trở hoặc bóng đèn.",
            r"Nêu được mối liên hệ về hiệu điện thế ($U = U_1 = U_2 = \dots = U_n$) và cường độ dòng điện ($I = I_1 + I_2 + \dots + I_n$) trong đoạn mạch song song.",
            r"Thực hiện thí nghiệm rút ra được: trong đoạn mạch điện mắc song song, nghịch đảo của điện trở tương đương bằng tổng các nghịch đảo của từng điện trở thành phần: $\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots + \dfrac{1}{R_n}$.",
            r"Tính được điện trở tương đương và cường độ dòng điện trong đoạn mạch một chiều mắc song song và hỗn hợp trong một số trường hợp đơn giản; giải thích được vì sao các thiết bị điện trong gia đình được mắc song song.",
        ],
        "definition": r"""- **Đoạn mạch song song** là đoạn mạch gồm các nhánh điện trở có hai đầu được nối chung vào hai điểm nút của mạch điện.
- **Tính chất cơ bản**:
  + Hiệu điện thế giữa hai đầu các nhánh bằng nhau: $U = U_1 = U_2 = \dots = U_n$.
  + Cường độ dòng điện mạch chính bằng tổng cường độ dòng điện qua các nhánh rẽ: $I = I_1 + I_2 + \dots + I_n$.
  + Công thức điện trở tương đương: $\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots + \dfrac{1}{R_n}$ (với hai điện trở: $R_{\text{tđ}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$).""",
        "theory": r"""### Bài 12. Đoạn mạch nối tiếp, song song (Phần II: Đoạn mạch song song)
- **Hiệu điện thế và cường độ dòng điện trong đoạn mạch song song**: Khi mắc hai điện trở $R_1$ và $R_2$ song song với nhau vào nguồn điện $U$, hai đầu của $R_1$ và hai đầu của $R_2$ cùng nối chung vào hai điểm nút nên chịu cùng một hiệu điện thế: $U = U_1 = U_2$. Tại nút phân nhánh, dòng điện mạch chính $I$ tách thành hai dòng điện nhánh $I_1$ và $I_2$, nên cường độ dòng điện mạch chính bằng tổng cường độ dòng điện qua các mạch rẽ: $I = I_1 + I_2$.
- **Điện trở tương đương của đoạn mạch song song**: Từ $I = I_1 + I_2 \iff \dfrac{U}{R_{\text{tđ}}} = \dfrac{U}{R_1} + \dfrac{U}{R_2}$, chia hai vế cho $U$ ta được: $\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} \iff R_{\text{tđ}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$. Mở rộng cho $n$ điện trở mắc song song: $\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots + \dfrac{1}{R_n}$. Điện trở tương đương của đoạn mạch song song luôn **nhỏ hơn mỗi điện trở thành phần** (mắc thêm nhánh song song làm $R_{\text{tđ}}$ giảm và dòng điện mạch chính $I$ tăng lên).
- **Hệ quả phân dòng (chia dòng điện)**: Vì $U_1 = U_2 \iff I_1 \cdot R_1 = I_2 \cdot R_2 \Rightarrow \dfrac{I_1}{I_2} = \dfrac{R_2}{R_1}$. Trong đoạn mạch song song, cường độ dòng điện chạy qua mỗi nhánh tỉ lệ nghịch với điện trở của nhánh đó (nhánh có điện trở nhỏ hơn thì có dòng điện lớn hơn đi qua).
- **Ứng dụng trong mạng điện gia đình**: Tất cả các thiết bị điện trong gia đình (đèn chiếu sáng, quạt điện, tủ lạnh, tivi, máy giặt) đều có hiệu điện thế định mức $220\text{ V}$ nên phải được mắc **song song** vào nguồn điện $220\text{ V}$ để mỗi thiết bị đều được cấp đúng điện áp định mức và có thể bật, tắt hoàn toàn độc lập với nhau.""",
        "formulas": [
            G(
                "I. Các hệ thức cơ bản của đoạn mạch song song",
                F("Hiệu điện thế trên các nhánh", r"$U = U_1 = U_2 = \dots = U_n$", r"Bằng nhau trên mọi nhánh song song"),
                F("Cường độ dòng điện mạch chính", r"$I = I_1 + I_2 + \dots + I_n$", r"Tổng dòng điện các nhánh rẽ"),
                F("Điện trở tương đương", r"$\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots + \dfrac{1}{R_n};\quad R_{12} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$", r"Nếu có $n$ điện trở giống nhau $R_0$: $R_{\text{tđ}} = \dfrac{R_0}{n}$"),
            ),
            G(
                "II. Quy tắc phân dòng",
                F("Tỉ số cường độ dòng điện qua hai nhánh", r"$\dfrac{I_1}{I_2} = \dfrac{R_2}{R_1}$", r"Cường độ dòng điện tỉ lệ nghịch với điện trở"),
                F("Công thức tính nhanh $I_1, I_2$ theo dòng mạch chính $I$", r"$I_1 = I \cdot \dfrac{R_2}{R_1 + R_2};\quad I_2 = I \cdot \dfrac{R_1}{R_1 + R_2}$", r""),
            ),
        ],
        "example": r"Cho hai điện trở $R_1 = 30\text{ }\Omega$ và $R_2 = 20\text{ }\Omega$ được mắc song song với nhau vào nguồn điện có hiệu điện thế không đổi $U = 24\text{ V}$. Tính điện trở tương đương của đoạn mạch, cường độ dòng điện chạy qua mỗi nhánh và cường độ dòng điện trong mạch chính.",
        "example_answer": r"""- Điện trở tương đương của đoạn mạch gồm $R_1$ song song với $R_2$ là:
$$R_{\text{tđ}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2} = \dfrac{30 \cdot 20}{30 + 20} = \dfrac{600}{50} = 12\text{ }\Omega$$
- Vì $R_1$ mắc song song với $R_2$ nên $U_1 = U_2 = U = 24\text{ V}$. Cường độ dòng điện qua mỗi nhánh là:
$$I_1 = \dfrac{U_1}{R_1} = \dfrac{24}{30} = 0{,}8\text{ A};\quad I_2 = \dfrac{U_2}{R_2} = \dfrac{24}{20} = 1{,}2\text{ A}$$
- Cường độ dòng điện trong mạch chính là:
$$I = I_1 + I_2 = 0{,}8 + 1{,}2 = 2{,}0\text{ A}\quad \left(\text{Hoặc } I = \dfrac{U}{R_{\text{tđ}}} = \dfrac{24}{12} = 2{,}0\text{ A}\right)$$""",
        "real_life": r"""- **Mạng điện sinh hoạt $220\text{ V}$**: Các ổ cắm và bóng đèn trong nhà đều mắc song song để khi tắt đèn phòng khách thì tủ lạnh trong bếp vẫn chạy bình thường.
- **Nguy cơ quá tải ổ cắm nối dài**: Khi cắm đồng thời quá nhiều thiết bị công suất lớn (bếp từ, ấm siêu tốc, bàn là) vào chung một ổ cắm (tức là mắc song song thêm nhiều nhánh), điện trở tương đương giảm mạnh làm tổng dòng điện $I = I_1 + I_2 + \dots$ trên dây dẫn chính tăng vọt, dễ gây nóng chảy vỏ nhựa và chập cháy.""",
        "game_title": "Thử thách thực tế: Đoạn mạch song song",
        "game_description": "Thiết kế mạng điện các nhánh song song, đóng ngắt từng nhánh độc lập và theo dõi sự phân bố dòng điện qua các ampe kế.",
        "game_type": "game_doanmachsongsong",
        "quiz": [
            mcq(
                "biet",
                r"Cho hai điện trở $R_1$ và $R_2$ mắc song song với nhau. Công thức tính điện trở tương đương $R_{\text{tđ}}$ của đoạn mạch là:",
                [
                    r"$R_{\text{tđ}} = R_1 + R_2$",
                    r"$R_{\text{tđ}} = \dfrac{R_1 + R_2}{R_1 \cdot R_2}$",
                    r"$R_{\text{tđ}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$",
                    r"$R_{\text{tđ}} = R_1 - R_2$",
                ],
                2,
                r"Từ $\dfrac{1}{R_{\text{tđ}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} = \dfrac{R_1 + R_2}{R_1 \cdot R_2}$, suy ra $R_{\text{tđ}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$.",
            ),
            mcq(
                "biet",
                r"Hai điện trở $R_1 = 6\text{ }\Omega$ và $R_2 = 3\text{ }\Omega$ được mắc song song với nhau. Điện trở tương đương của đoạn mạch bằng:",
                [r"$9\text{ }\Omega$", r"$4{,}5\text{ }\Omega$", r"$2\text{ }\Omega$", r"$0{,}5\text{ }\Omega$"],
                2,
                r"Ta có $R_{\text{tđ}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2} = \dfrac{6 \cdot 3}{6 + 3} = \dfrac{18}{9} = 2\text{ }\Omega$.",
            ),
            mcq(
                "biet",
                r"Trong đoạn mạch gồm hai điện trở $R_1$ và $R_2$ mắc song song, tỉ số cường độ dòng điện $\dfrac{I_1}{I_2}$ chạy qua hai nhánh thỏa mãn hệ thức nào?",
                [
                    r"$\dfrac{I_1}{I_2} = \dfrac{R_1}{R_2}$",
                    r"$\dfrac{I_1}{I_2} = \dfrac{R_2}{R_1}$",
                    r"$I_1 = I_2$",
                    r"$\dfrac{I_1}{I_2} = \left(\dfrac{R_1}{R_2}\right)^2$",
                ],
                1,
                r"Vì $U_1 = U_2 \iff I_1 R_1 = I_2 R_2 \Rightarrow \dfrac{I_1}{I_2} = \dfrac{R_2}{R_1}$ (cường độ dòng điện tỉ lệ nghịch với điện trở).",
            ),
            mcq(
                "biet",
                r"Vì sao các thiết bị điện trong gia đình (bóng đèn, quạt điện, tivi, tủ lạnh có cùng hiệu điện thế định mức $220\text{ V}$) đều được mắc song song vào mạng điện $220\text{ V}$?",
                [
                    r"Để cường độ dòng điện qua mọi thiết bị đều bằng nhau",
                    r"Để mỗi thiết bị đều được đặt dưới đúng hiệu điện thế định mức $220\text{ V}$ và có thể bật, tắt độc lập với nhau",
                    r"Để làm tăng điện trở tương đương của mạng điện gia đình",
                    r"Để khi một bóng đèn bị hỏng thì tất cả các thiết bị khác tự động tắt theo",
                ],
                1,
                r"Mắc song song giúp các thiết bị có cùng hiệu điện thế $U = 220\text{ V}$ và hoạt động độc lập (tắt một thiết bị không làm ngắt mạch các thiết bị khác).",
            ),
            mcq(
                "hieu",
                r"Ba điện trở giống hệt nhau có cùng giá trị $R_0 = 24\text{ }\Omega$ được mắc song song với nhau. Điện trở tương đương của đoạn mạch này là:",
                [r"$72\text{ }\Omega$", r"$24\text{ }\Omega$", r"$12\text{ }\Omega$", r"$8\text{ }\Omega$"],
                3,
                r"Khi mắc $n = 3$ điện trở giống nhau $R_0 = 24\text{ }\Omega$ song song thì $R_{\text{tđ}} = \dfrac{R_0}{3} = \dfrac{24}{3} = 8\text{ }\Omega$.",
            ),
            mcq(
                "hieu",
                r"Cho hai điện trở $R_1 = 10\text{ }\Omega$ và $R_2 = 15\text{ }\Omega$ mắc song song vào nguồn điện. Biết cường độ dòng điện chạy qua điện trở $R_1$ là $I_1 = 1{,}2\text{ A}$. Cường độ dòng điện $I$ trong mạch chính bằng:",
                [r"$0{,}8\text{ A}$", r"$1{,}8\text{ A}$", r"$2{,}0\text{ A}$", r"$3{,}0\text{ A}$"],
                2,
                r"Hiệu điện thế hai đầu mạch là $U = U_1 = I_1 \cdot R_1 = 1{,}2 \cdot 10 = 12\text{ V}$. Dòng điện qua $R_2$ là $I_2 = \dfrac{U}{R_2} = \dfrac{12}{15} = 0{,}8\text{ A}$. Dòng điện mạch chính là $I = I_1 + I_2 = 1{,}2 + 0{,}8 = 2{,}0\text{ A}$.",
            ),
            tf4(
                "hieu",
                r"Cho đoạn mạch gồm hai điện trở $R_1 = 20\text{ }\Omega$ và $R_2 = 30\text{ }\Omega$ mắc song song với nhau vào nguồn điện có hiệu điện thế không đổi $U = 12\text{ V}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Điện trở tương đương của đoạn mạch bằng $12\text{ }\Omega$, nhỏ hơn cả $R_1$ và $R_2$.",
                    r"b) Cường độ dòng điện chạy qua điện trở $R_1$ là $I_1 = 0{,}6\text{ A}$ và qua điện trở $R_2$ là $I_2 = 0{,}4\text{ A}$.",
                    r"c) Cường độ dòng điện trong mạch chính là $I = 1{,}0\text{ A}$.",
                    r"d) Nếu mắc thêm một điện trở $R_3 = 60\text{ }\Omega$ song song với hai điện trở trên thì điện trở tương đương của cả mạch sẽ tăng lên.",
                ],
                [True, True, True, False],
                r"a) Đúng vì $R_{\text{tđ}} = \dfrac{20 \cdot 30}{20 + 30} = 12\text{ }\Omega$. b) Đúng vì $I_1 = \dfrac{12}{20} = 0{,}6\text{ A}$ và $I_2 = \dfrac{12}{30} = 0{,}4\text{ A}$. c) Đúng vì $I = I_1 + I_2 = 1{,}0\text{ A}$. d) Sai vì mắc thêm nhánh song song thì điện trở tương đương giảm xuống còn $R'_{\text{tđ}} = \dfrac{12 \cdot 60}{12 + 60} = 10\text{ }\Omega$.",
            ),
            tf4(
                "hieu",
                r"Xét một mạch điện hỗn hợp gồm điện trở $R_1 = 8\text{ }\Omega$ mắc nối tiếp với cụm hai điện trở $(R_2 \parallel R_3)$, trong đó $R_2 = 30\text{ }\Omega$ và $R_3 = 20\text{ }\Omega$. Đặt vào hai đầu cả đoạn mạch hiệu điện thế $U = 40\text{ V}$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Điện trở tương đương của cụm song song $(R_2 \parallel R_3)$ là $R_{23} = 12\text{ }\Omega$.",
                    r"b) Điện trở tương đương của toàn bộ đoạn mạch là $R_{\text{tđ}} = 20\text{ }\Omega$.",
                    r"c) Cường độ dòng điện chạy qua điện trở $R_1$ là $I_1 = 2\text{ A}$.",
                    r"d) Hiệu điện thế giữa hai đầu điện trở $R_2$ bằng $40\text{ V}$.",
                ],
                [True, True, True, False],
                r"a) Đúng vì $R_{23} = \dfrac{30 \cdot 20}{30 + 20} = 12\text{ }\Omega$. b) Đúng vì $R_{\text{tđ}} = R_1 + R_{23} = 8 + 12 = 20\text{ }\Omega$. c) Đúng vì $I_1 = I = \dfrac{U}{R_{\text{tđ}}} = \dfrac{40}{20} = 2\text{ A}$. d) Sai vì hiệu điện thế trên cụm song song chỉ là $U_{23} = U_2 = U_3 = I \cdot R_{23} = 2 \cdot 12 = 24\text{ V}$ (còn $U_1 = 16\text{ V}$).",
            ),
            mcq(
                "vandung",
                r"Cho hai điện trở $R_1 = 10\text{ }\Omega$ (chịu được dòng điện tối đa $I_{1\max} = 1{,}5\text{ A}$) và $R_2 = 20\text{ }\Omega$ (chịu được dòng điện tối đa $I_{2\max} = 1{,}0\text{ A}$) được mắc song song với nhau. Hiệu điện thế tối đa $U_{\max}$ có thể đặt vào hai đầu đoạn mạch song song này để không điện trở nào bị hỏng là:",
                [r"$15\text{ V}$", r"$20\text{ V}$", r"$35\text{ V}$", r"$25\text{ V}$"],
                0,
                r"Hiệu điện thế tối đa mà $R_1$ chịu được là $U_{1\max} = I_{1\max} \cdot R_1 = 1{,}5 \cdot 10 = 15\text{ V}$. Hiệu điện thế tối đa mà $R_2$ chịu được là $U_{2\max} = I_{2\max} \cdot R_2 = 1{,}0 \cdot 20 = 20\text{ V}$. Vì mắc song song chịu chung hiệu điện thế nên $U_{\max} = \min(15\text{ V};\; 20\text{ V}) = 15\text{ V}$.",
            ),
            short(
                "vandung",
                r"Mắc song song hai điện trở $R_1 = 15\text{ }\Omega$ và $R_2$ vào nguồn điện có hiệu điện thế $U = 18\text{ V}$ thì cường độ dòng điện trong mạch chính đo được là $I = 1{,}8\text{ A}$. Tính giá trị của điện trở $R_2$ theo đơn vị $\Omega$.",
                ["30"],
                r"Cường độ dòng điện chạy qua $R_1$ là $I_1 = \dfrac{U}{R_1} = \dfrac{18}{15} = 1{,}2\text{ A}$. Cường độ dòng điện chạy qua $R_2$ là $I_2 = I - I_1 = 1{,}8 - 1{,}2 = 0{,}6\text{ A}$. Vậy giá trị điện trở $R_2 = \dfrac{U}{I_2} = \dfrac{18}{0{,}6} = 30\text{ }\Omega$.",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 6: NĂNG LƯỢNG VÀ CÔNG SUẤT ĐIỆN =====================
    {
        "topic": "cong-va-cong-suat-dien",
        "title": "Năng lượng của dòng điện, Công suất điện và Định luật Joule – Lenz",
        "icon": "💡",
        "description": "Chương III · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống (Bài 13): Năng lượng của dòng điện (điện năng tiêu thụ), công suất điện, công suất định mức trên thiết bị điện, đơn vị ki-lô-oát giờ và định luật Joule – Lenz.",
        "requirements": [
            r"Lấy ví dụ chứng tỏ được dòng điện có năng lượng và tính được năng lượng của dòng điện theo công thức $W = U \cdot I \cdot t$.",
            r"Nêu được công suất điện định mức của dụng cụ điện (số oát ghi trên dụng cụ) và tính được công suất điện theo công thức $\mathcal{P} = U \cdot I = I^2 R = \dfrac{U^2}{R}$.",
            r"Đổi được đơn vị đo năng lượng điện giữa jun ($\text{J}$) và ki-lô-oát giờ ($\text{kWh}$, số đếm công tơ điện) để tính lượng điện năng tiêu thụ và tiền điện trong gia đình.",
            r"Vận dụng được công thức nhiệt lượng tỏa ra trên dây dẫn có điện trở $R$: $Q = I^2 R t$ để giải các bài toán đun nóng bằng điện.",
        ],
        "definition": r"""- **Năng lượng của dòng điện** (công của dòng điện) tiêu thụ trên một đoạn mạch được xác định bằng tích của hiệu điện thế, cường độ dòng điện và thời gian dòng điện chạy qua: $W = A = U \cdot I \cdot t = \mathcal{P} \cdot t$ (đơn vị: $\text{J}$ hoặc $\text{kWh}$).
- **Công suất điện** ($\mathcal{P}$) cho biết năng lượng điện mà đoạn mạch tiêu thụ trong một đơn vị thời gian: $\mathcal{P} = \dfrac{W}{t} = U \cdot I = I^2 R = \dfrac{U^2}{R}$ (đơn vị: $\text{W}$).
- **Định luật Joule – Lenz**: Nhiệt lượng tỏa ra ở dây dẫn có điện trở $R$ khi có dòng điện $I$ chạy qua trong thời gian $t$ là $Q = I^2 R t$.""",
        "theory": r"""### Bài 13. Năng lượng của dòng điện và công suất điện
- **Năng lượng của dòng điện ($W$)**: Dòng điện chạy qua các thiết bị điện có thể chuyển hóa năng lượng điện thành các dạng năng lượng khác (như nhiệt năng trong bàn là, ấm điện; quang năng và nhiệt năng trong bóng đèn; cơ năng và nhiệt năng trong quạt điện, máy bơm). Năng lượng điện mà một đoạn mạch tiêu thụ được tính bằng công thức $W = U \cdot I \cdot t$, trong đó $U$ đo bằng $\text{V}$, $I$ đo bằng $\text{A}$, $t$ đo bằng $\text{s}$ và $W$ đo bằng jun ($\text{J}$, với $1\text{ J} = 1\text{ V}\cdot\text{A}\cdot\text{s} = 1\text{ W}\cdot\text{s}$).
- **Đơn vị ki-lô-oát giờ ($\text{kWh}$) và công tơ điện**: Trong thực tế đời sống, lượng điện năng tiêu thụ của các hộ gia đình được đo bằng **công tơ điện** theo đơn vị ki-lô-oát giờ ($\text{kWh}$), thường gọi là một **số điện**: $1\text{ kWh} = 1000\text{ W} \cdot 3600\text{ s} = 3600000\text{ J} = 3{,}6 \cdot 10^6\text{ J}$.
- **Công suất điện ($\mathcal{P}$)**: Công suất điện đặc trưng cho tốc độ tiêu thụ năng lượng điện của đoạn mạch hay thiết bị điện: $\mathcal{P} = \dfrac{W}{t} = U \cdot I$. Đối với đoạn mạch chỉ có điện trở thuần $R$ (như dây đốt nóng), kết hợp với định luật Ohm $I = \dfrac{U}{R}$ ta có: $\mathcal{P} = U \cdot I = I^2 R = \dfrac{U^2}{R}$.
- **Số ghi định mức trên dụng cụ điện**: Trên mỗi dụng cụ điện thường ghi hai thông số $U_{\text{đm}} - \mathcal{P}_{\text{đm}}$ (ví dụ: trên bóng đèn ghi $220\text{ V} - 60\text{ W}$, trên ấm siêu tốc ghi $220\text{ V} - 1500\text{ W}$), cho biết **hiệu điện thế định mức** và **công suất điện định mức** khi dụng cụ hoạt động bình thường ở đúng hiệu điện thế đó. Từ đó suy ra dòng điện định mức $I_{\text{đm}} = \dfrac{\mathcal{P}_{\text{đm}}}{U_{\text{đm}}}$ và điện trở của dụng cụ $R = \dfrac{U_{\text{đm}}^2}{\mathcal{P}_{\text{đm}}}$.
- **Định luật Joule – Lenz**: Khi dòng điện chạy qua vật dẫn chỉ có điện trở $R$, toàn bộ điện năng tiêu thụ biến đổi thành nhiệt năng tỏa ra: $Q = I^2 R t = \mathcal{P} \cdot t$ ($\text{J}$).""",
        "formulas": [
            G(
                "I. Công suất điện và thông số định mức trên thiết bị",
                F("Các công thức tính công suất điện", r"$\mathcal{P} = U \cdot I = I^2 R = \dfrac{U^2}{R}$", r"$\mathcal{P}$ ($\text{W}$), $U$ ($\text{V}$), $I$ ($\text{A}$), $R$ ($\Omega$)"),
                F("Dòng điện định mức và điện trở thiết bị", r"$I_{\text{đm}} = \dfrac{\mathcal{P}_{\text{đm}}}{U_{\text{đm}}};\quad R = \dfrac{U_{\text{đm}}^2}{\mathcal{P}_{\text{đm}}}$", r"Khi đặt vào $U \neq U_{\text{đm}}$ ($R$ không đổi): $\mathcal{P} = \left(\dfrac{U}{U_{\text{đm}}}\right)^2 \mathcal{P}_{\text{đm}}$"),
            ),
            G(
                "II. Năng lượng điện tiêu thụ, công tơ điện và nhiệt lượng tỏa ra",
                F("Năng lượng của dòng điện", r"$W = \mathcal{P} \cdot t = U \cdot I \cdot t = I^2 R t$", r"Nếu $\mathcal{P}$ ($\text{kW}$) và $t$ ($\text{h}$) thì $W = \mathcal{P} \cdot t$ ($\text{kWh}$)"),
                F("Quy đổi số đếm công tơ điện", r"$1\text{ số điện} = 1\text{ kWh} = 3600000\text{ J} = 3{,}6 \cdot 10^6\text{ J}$", r""),
                F("Định luật Joule – Lenz và hiệu suất đun nước", r"$Q_{\text{tỏa}} = I^2 R t;\quad H = \dfrac{Q_{\text{thu}}}{W_{\text{điện}}} \cdot 100\% = \dfrac{m c \Delta t}{\mathcal{P} \cdot t} \cdot 100\%$", r""),
            ),
        ],
        "example": r"Một ấm đun nước bằng điện có ghi $220\text{ V} - 1500\text{ W}$ được sử dụng ở đúng hiệu điện thế $U = 220\text{ V}$ để đun sôi $2\text{ kg}$ nước từ nhiệt độ ban đầu $t_1 = 20^\circ\text{C}$ đến $t_2 = 100^\circ\text{C}$. Biết hiệu suất của ấm là $H = 80\%$ và nhiệt dung riêng của nước là $c = 4200\text{ J/(kg}\cdot\text{K)}$. Tính cường độ dòng điện chạy qua ấm, thời gian đun sôi nước và điện năng tiêu thụ theo đơn vị $\text{kWh}$.",
        "example_answer": r"""- Vì ấm dùng ở đúng $U = U_{\text{đm}} = 220\text{ V}$ nên công suất thực tế là $\mathcal{P} = 1500\text{ W}$. Cường độ dòng điện qua ấm là:
$$I = \dfrac{\mathcal{P}}{U} = \dfrac{1500}{220} \approx 6{,}82\text{ A}$$
- Nhiệt lượng có ích mà $2\text{ kg}$ nước cần thu vào để sôi là:
$$Q_{\text{ích}} = m \cdot c \cdot (t_2 - t_1) = 2 \cdot 4200 \cdot (100 - 20) = 672000\text{ J}$$
- Điện năng toàn phần mà ấm đã tiêu thụ là:
$$W = \dfrac{Q_{\text{ích}}}{H} = \dfrac{672000}{0{,}8} = 840000\text{ J}$$
- Thời gian đun sôi nước và số $\text{kWh}$ tiêu thụ là:
$$t = \dfrac{W}{\mathcal{P}} = \dfrac{840000}{1500} = 560\text{ s}\text{ (tức } 9\text{ phút } 20\text{ giây)};\quad W = \dfrac{840000}{3600000} \approx 0{,}233\text{ kWh}$$""",
        "real_life": r"""- **Quản lí chi tiêu điện năng gia đình**: Đọc chỉ số công tơ điện ($\text{kWh}$), tính toán chi phí điện hàng tháng và lựa chọn các thiết bị dán nhãn năng lượng tiết kiệm điện (như thay đèn sợi đốt $60\text{ W}$ bằng đèn LED $9\text{ W}$ có cùng độ sáng).
- **An toàn phòng cháy chữa cháy điện**: Lựa chọn aptomat tổng phù hợp với tổng công suất các thiết bị trong nhà ($I_{\text{tổng}} = \dfrac{\mathcal{P}_{\text{tổng}}}{U}$) để tự động ngắt điện khi quá tải.""",
        "game_title": "Thử thách thực tế: Công và Công suất điện",
        "game_description": "Vận hành các thiết bị điện trong ngôi nhà thông minh, theo dõi công suất tức thời, số đếm công tơ điện và tránh quá tải aptomat.",
        "game_type": "game_congsuatdien",
        "quiz": [
            mcq(
                "biet",
                r"Công thức nào dưới đây dùng để tính năng lượng của dòng điện (điện năng tiêu thụ) trên một đoạn mạch có hiệu điện thế $U$, cường độ dòng điện $I$ trong thời gian $t$?",
                [r"$W = \dfrac{U \cdot I}{t}$", r"$W = U \cdot I \cdot t$", r"$W = U \cdot I^2 \cdot t$", r"$W = \dfrac{U \cdot t}{I}$"],
                1,
                r"Năng lượng của dòng điện được xác định bởi công thức $W = U \cdot I \cdot t = \mathcal{P} \cdot t$.",
            ),
            mcq(
                "biet",
                r"Một số đếm trên công tơ điện tương ứng với $1\text{ kWh}$. Đổi sang đơn vị jun ($\text{J}$), $1\text{ kWh}$ bằng bao nhiêu?",
                [r"$1000\text{ J}$", r"$3600\text{ J}$", r"$360000\text{ J}$", r"$3600000\text{ J}$"],
                3,
                r"Ta có $1\text{ kWh} = 1000\text{ W} \cdot 3600\text{ s} = 3600000\text{ J} = 3{,}6 \cdot 10^6\text{ J}$.",
            ),
            mcq(
                "biet",
                r"Trên vỏ một chiếc bàn là điện có ghi $220\text{ V} - 1100\text{ W}$. Con số $1100\text{ W}$ cho biết điều gì?",
                [
                    r"Công suất điện mà bàn là luôn tiêu thụ ở mọi hiệu điện thế bất kì",
                    r"Năng lượng điện mà bàn là tiêu thụ trong $1$ giờ",
                    r"Công suất điện định mức của bàn là khi được sử dụng ở đúng hiệu điện thế $220\text{ V}$",
                    r"Điện trở của dây đốt nóng bên trong bàn là bằng $1100\text{ }\Omega$",
                ],
                2,
                r"Số oát ghi trên dụng cụ điện cho biết công suất định mức khi dụng cụ hoạt động bình thường ở hiệu điện thế định mức $220\text{ V}$.",
            ),
            mcq(
                "biet",
                r"Theo định luật Joule – Lenz, nhiệt lượng $Q$ tỏa ra trên một dây dẫn có điện trở $R$ khi có dòng điện cường độ $I$ chạy qua trong thời gian $t$ được tính bằng công thức:",
                [r"$Q = I \cdot R \cdot t$", r"$Q = I^2 \cdot R \cdot t$", r"$Q = I \cdot R^2 \cdot t$", r"$Q = \dfrac{I^2 \cdot t}{R}$"],
                1,
                r"Nhiệt lượng tỏa ra trên dây dẫn tỉ lệ thuận với bình phương cường độ dòng điện, với điện trở và thời gian: $Q = I^2 R t$.",
            ),
            mcq(
                "hieu",
                r"Một bóng đèn có ghi $220\text{ V} - 100\text{ W}$. Khi đèn sáng bình thường ở hiệu điện thế $220\text{ V}$ thì điện trở $R$ của dây tóc bóng đèn có giá trị bằng:",
                [r"$484\text{ }\Omega$", r"$2{,}2\text{ }\Omega$", r"$220\text{ }\Omega$", r"$48{,}4\text{ }\Omega$"],
                0,
                r"Điện trở của bóng đèn khi sáng bình thường là $R = \dfrac{U_{\text{đm}}^2}{\mathcal{P}_{\text{đm}}} = \dfrac{220^2}{100} = \dfrac{48400}{100} = 484\text{ }\Omega$.",
            ),
            mcq(
                "hieu",
                r"Một gia đình sử dụng một máy điều hòa có công suất tiêu thụ trung bình $\mathcal{P} = 1{,}2\text{ kW}$ trong $5$ giờ mỗi ngày. Trong $30$ ngày, riêng máy điều hòa này tiêu thụ bao nhiêu số điện ($\text{kWh}$)?",
                [r"$6\text{ kWh}$", r"$36\text{ kWh}$", r"$180\text{ kWh}$", r"$1800\text{ kWh}$"],
                2,
                r"Tổng thời gian sử dụng trong $30$ ngày là $t = 5 \cdot 30 = 150\text{ h}$. Điện năng tiêu thụ là $W = \mathcal{P} \cdot t = 1{,}2 \cdot 150 = 180\text{ kWh}$ ($180$ số điện).",
            ),
            tf4(
                "hieu",
                r"Một bếp điện có ghi $220\text{ V} - 880\text{ W}$ được mắc vào mạng điện có hiệu điện thế $U = 220\text{ V}$ và sử dụng liên tục trong thời gian $30\text{ phút}$. Giả sử điện trở của dây đốt nóng không thay đổi theo nhiệt độ. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Cường độ dòng điện chạy qua bếp điện khi đó là $I = 4\text{ A}$.",
                    r"b) Điện trở của dây đốt nóng trong bếp điện là $R = 55\text{ }\Omega$.",
                    r"c) Điện năng mà bếp tiêu thụ trong $30\text{ phút}$ là $0{,}44\text{ kWh}$ (tương ứng $1584000\text{ J}$).",
                    r"d) Nếu cắm bếp điện này vào nguồn điện có hiệu điện thế $U' = 110\text{ V}$ thì công suất tỏa nhiệt của bếp giảm đi một nửa còn $440\text{ W}$.",
                ],
                [True, True, True, False],
                r"a) Đúng vì $I = \dfrac{\mathcal{P}}{U} = \dfrac{880}{220} = 4\text{ A}$. b) Đúng vì $R = \dfrac{U}{I} = \dfrac{220}{4} = 55\text{ }\Omega$. c) Đúng vì $t = 30\text{ phút} = 0{,}5\text{ h} = 1800\text{ s} \Rightarrow W = 0{,}88\text{ kW} \cdot 0{,}5\text{ h} = 0{,}44\text{ kWh} = 880 \cdot 1800 = 1584000\text{ J}$. d) Sai vì theo công thức $\mathcal{P}' = \dfrac{U'^2}{R}$, khi $U$ giảm đi $2$ lần thì công suất $\mathcal{P}$ giảm đi $2^2 = 4$ lần, chỉ còn $\dfrac{880}{4} = 220\text{ W}$.",
            ),
            tf4(
                "hieu",
                r"Cho hai bóng đèn sợi đốt có ghi $\text{Đ}_1(220\text{ V} - 100\text{ W})$ và $\text{Đ}_2(220\text{ V} - 40\text{ W})$. Giả sử điện trở của hai bóng đèn không phụ thuộc vào nhiệt độ. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Điện trở của đèn $\text{Đ}_1$ là $R_1 = 484\text{ }\Omega$ và của đèn $\text{Đ}_2$ là $R_2 = 1210\text{ }\Omega$ ($R_2 > R_1$).",
                    r"b) Khi mắc song song hai bóng đèn này vào hiệu điện thế $220\text{ V}$ thì cả hai đèn đều sáng bình thường và đèn $\text{Đ}_1$ sáng mạnh hơn đèn $\text{Đ}_2$.",
                    r"c) Nếu đem mắc nối tiếp hai bóng đèn này với nhau vào nguồn điện $220\text{ V}$ thì cường độ dòng điện chạy qua hai đèn bằng nhau.",
                    r"d) Khi mắc nối tiếp hai đèn vào nguồn $220\text{ V}$, bóng đèn $\text{Đ}_1$ ($100\text{ W}$) vẫn sáng mạnh hơn bóng đèn $\text{Đ}_2$ ($40\text{ W}$).",
                ],
                [True, True, True, False],
                r"a) Đúng vì $R_1 = \dfrac{220^2}{100} = 484\text{ }\Omega$ và $R_2 = \dfrac{220^2}{40} = 1210\text{ }\Omega$. b) Đúng vì khi mắc song song vào $220\text{ V}$, $\mathcal{P}_1 = 100\text{ W} > \mathcal{P}_2 = 40\text{ W}$. c) Đúng theo tính chất đoạn mạch nối tiếp. d) Sai vì khi mắc nối tiếp, hai đèn có cùng dòng điện $I$ nên công suất thực tế là $\mathcal{P} = I^2 R$; vì $R_2 > R_1$ nên $\mathcal{P}_2 > \mathcal{P}_1$, tức là đèn $\text{Đ}_2$ sáng mạnh hơn đèn $\text{Đ}_1$.",
            ),
            mcq(
                "vandung",
                r"Một dây điện trở có trị số $R = 40\text{ }\Omega$ được nhúng ngập trong một bình đựng nước và mắc vào hiệu điện thế $U = 200\text{ V}$. Nhiệt lượng mà dây điện trở tỏa ra trong thời gian $t = 5\text{ phút}$ là:",
                [r"$5000\text{ J}$", r"$300\text{ kJ}$", r"$150\text{ kJ}$", r"$60\text{ kJ}$"],
                1,
                r"Công suất tỏa nhiệt của dây điện trở là $\mathcal{P} = \dfrac{U^2}{R} = \dfrac{200^2}{40} = 1000\text{ W}$. Đổi $t = 5\text{ phút} = 300\text{ s}$. Nhiệt lượng tỏa ra là $Q = \mathcal{P} \cdot t = 1000 \cdot 300 = 300000\text{ J} = 300\text{ kJ}$.",
            ),
            short(
                "vandung",
                r"Một hộ gia đình sử dụng các thiết bị điện ở hiệu điện thế $220\text{ V}$ gồm: $4$ bóng đèn LED loại $20\text{ W}$ hoạt động $5\text{ giờ/ngày}$; $1$ tủ lạnh công suất trung bình $120\text{ W}$ hoạt động $24\text{ giờ/ngày}$ và $1$ nồi cơm điện $720\text{ W}$ hoạt động $1\text{ giờ/ngày}$. Tính tổng tiền điện hộ gia đình đó phải trả cho các thiết bị trên trong $1\text{ tháng}$ ($30\text{ ngày}$) theo đơn vị nghìn đồng, biết giá điện trung bình là $2{,}5\text{ nghìn đồng/kWh}$.",
                ["300"],
                r"Điện năng tiêu thụ trong $1$ ngày của các thiết bị là: $W_{\text{ngày}} = 4 \cdot 0{,}02\text{ kW} \cdot 5\text{ h} + 0{,}12\text{ kW} \cdot 24\text{ h} + 0{,}72\text{ kW} \cdot 1\text{ h} = 0{,}4 + 2{,}88 + 0{,}72 = 4\text{ kWh}$. Trong $30$ ngày, tổng điện năng tiêu thụ là $W_{\text{tháng}} = 4 \cdot 30 = 120\text{ kWh}$. Số tiền điện phải trả là $120 \cdot 2{,}5 = 300$ (nghìn đồng).",
            ),
        ],
    },
    # ===================== CHỦ ĐỀ 7: ĐIỆN TỪ =====================
    {
        "topic": "dien-tu",
        "title": "Cảm ứng điện từ, Dòng điện xoay chiều và Các tác dụng của dòng điện xoay chiều",
        "icon": "🧲",
        "description": "Chương IV (Bài 14 – Bài 15) và Chương V (Bài 16 – Bài 17) · SGK Khoa học tự nhiên 9 Kết nối tri thức với cuộc sống: Hiện tượng cảm ứng điện từ, nguyên tắc tạo ra dòng điện xoay chiều, các tác dụng của dòng điện xoay chiều, truyền tải điện năng và năng lượng với cuộc sống.",
        "requirements": [
            r"Thực hiện thí nghiệm để rút ra được: khi số đường sức từ xuyên qua tiết diện của cuộn dây dẫn kín biến thiên thì trong cuộn dây đó xuất hiện dòng điện cảm ứng.",
            r"Thực hiện thí nghiệm để nêu được nguyên tắc tạo ra dòng điện xoay chiều (dòng điện luân phiên đổi chiều) dựa trên hiện tượng cảm ứng điện từ.",
            r"Lấy được ví dụ chứng tỏ dòng điện xoay chiều có tác dụng nhiệt, phát sáng, từ, sinh lí; phân biệt được sự khác nhau về tác dụng từ và tác dụng hóa học giữa dòng điện xoay chiều và dòng điện một chiều.",
            r"Vận dụng được nguyên tắc cảm ứng điện từ trong máy phát điện, máy biến áp ($\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$), giảm hao phí truyền tải điện năng đi xa ($\mathcal{P}_{\text{hp}} = \dfrac{\mathcal{P}^2 R}{U^2}$) và sử dụng năng lượng tái tạo bảo vệ môi trường.",
        ],
        "definition": r"""- **Hiện tượng cảm ứng điện từ**: Khi số đường sức từ xuyên qua tiết diện của một cuộn dây dẫn kín biến thiên (tăng hoặc giảm) thì trong cuộn dây xuất hiện **dòng điện cảm ứng**.
- **Dòng điện xoay chiều (AC)**: Là dòng điện có chiều và cường độ biến thiên tuần hoàn theo thời gian (ở mạng điện dân dụng Việt Nam có hiệu điện thế hiệu dụng $U = 220\text{ V}$ và tần số $f = 50\text{ Hz}$).""",
        "theory": r"""### Bài 14. Cảm ứng điện từ. Nguyên tắc tạo ra dòng điện xoay chiều
- **Thí nghiệm Faraday về cảm ứng điện từ**: Khi đưa một cực của nam châm lại gần hoặc ra xa một cuộn dây dẫn kín (hoặc đóng, ngắt dòng điện qua nam châm điện đặt gần cuộn dây), kim điện kế nhạy nối với cuộn dây bị lệch đi, chứng tỏ trong cuộn dây xuất hiện **dòng điện cảm ứng**.
- **Điều kiện xuất hiện dòng điện cảm ứng**: Dòng điện cảm ứng xuất hiện trong cuộn dây dẫn kín trong thời gian **số đường sức từ xuyên qua tiết diện của cuộn dây dẫn đó đang biến thiên** (tăng lên hoặc giảm đi). Nếu nam châm và cuộn dây đứng yên so với nhau thì số đường sức từ không đổi nên không có dòng điện cảm ứng.
- **Nguyên tắc tạo ra dòng điện xoay chiều**: Khi cho một khung dây dẫn kín quay đều trong từ trường của một nam châm (hoặc cho nam châm quay đều trước cuộn dây dẫn kín), số đường sức từ xuyên qua tiết diện khung dây luân phiên tăng rồi giảm, làm xuất hiện trong khung dây một dòng điện cảm ứng luân phiên đổi chiều gọi là **dòng điện xoay chiều**. Đây là nguyên tắc cấu tạo của các máy phát điện xoay chiều (gồm hai bộ phận chính là phần cảm tạo ra từ trường và phần ứng tạo ra dòng điện; bộ phận đứng yên gọi là stato, bộ phận quay gọi là rôto).
### Bài 15. Tác dụng của dòng điện xoay chiều
- **Các tác dụng của dòng điện xoay chiều**: Dòng điện xoay chiều có đầy đủ các tác dụng như dòng điện một chiều gồm: **tác dụng nhiệt** (bàn là, bếp hồng ngoại, lò nướng), **tác dụng phát sáng** (đèn sợi đốt, đèn huỳnh quang, đèn LED), **tác dụng từ** (nam châm điện, quạt điện, loa điện, bếp từ) và **tác dụng sinh lí** (gây co giật nguy hiểm ở điện áp $220\text{ V}$, ứng dụng trong y tế).
- **Đặc trưng tác dụng từ của dòng điện xoay chiều**: Khi dòng điện một chiều chạy qua cuộn dây thì lực từ có chiều không đổi; còn khi dòng điện xoay chiều chạy qua cuộn dây thì các cực từ của cuộn dây đổi chiều liên tục theo tần số của dòng điện nên một nam châm vĩnh cửu đặt gần đó sẽ bị **lực từ đẩy – hút luân phiên** (làm lá thép đàn hồi rung động hoặc tạo ra từ trường biến thiên trong máy biến áp).
- **Máy biến áp và truyền tải điện năng đi xa**: Máy biến áp hoạt động dựa trên hiện tượng cảm ứng điện từ của dòng điện xoay chiều với công thức $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$. Khi truyền tải công suất điện $\mathcal{P}$ đi xa trên đường dây có điện trở $R$ dưới hiệu điện thế $U$, công suất hao phí do tỏa nhiệt là $\mathcal{P}_{\text{hp}} = I^2 R = \dfrac{\mathcal{P}^2 R}{U^2}$; tăng $U$ lên $n$ lần thì $\mathcal{P}_{\text{hp}}$ giảm $n^2$ lần.
### Bài 16 & Bài 17. Vòng năng lượng trên Trái Đất, Năng lượng hóa thạch và Năng lượng tái tạo
- **Các nguồn năng lượng sản xuất điện**: Hầu hết các nhà máy nhiệt điện (đốt nhiên liệu hóa thạch như than đá, dầu mỏ, khí thiên nhiên), thủy điện, điện gió, điện sóng biển, điện địa nhiệt đều làm quay tua-bin của máy phát điện xoay chiều dựa trên hiện tượng cảm ứng điện từ; riêng pin Mặt Trời biến đổi trực tiếp quang năng thành điện năng một chiều.""",
        "formulas": [
            G(
                "I. Điều kiện cảm ứng điện từ và máy biến áp",
                F("Điều kiện xuất hiện dòng điện cảm ứng", r"$\Phi \text{ (số đường sức từ qua cuộn dây kín) biến thiên } \Rightarrow i_{\text{c}} \neq 0$", r"Khi số đường sức từ tăng và khi giảm thì dòng cảm ứng có chiều ngược nhau"),
                F("Công thức máy biến áp lí tưởng", r"$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2};\quad \dfrac{I_1}{I_2} = \dfrac{U_2}{U_1} = \dfrac{N_2}{N_1}$", r"$N_2 > N_1$: máy tăng áp ($U_2 > U_1$); $N_2 < N_1$: máy hạ áp ($U_2 < U_1$)"),
            ),
            G(
                "II. Truyền tải điện năng đi xa",
                F("Cường độ dòng điện trên đường dây truyền tải", r"$I = \dfrac{\mathcal{P}}{U}$", r"$\mathcal{P}$: công suất truyền đi ($\text{W}$), $U$: hiệu điện thế truyền tải ($\text{V}$)"),
                F("Công suất hao phí tỏa nhiệt trên đường dây", r"$\mathcal{P}_{\text{hp}} = I^2 R = \dfrac{\mathcal{P}^2 \cdot R}{U^2}$", r"Tăng hiệu điện thế $U$ lên $n$ lần thì công suất hao phí giảm $n^2$ lần"),
                F("Hiệu suất truyền tải điện năng", r"$H = \dfrac{\mathcal{P} - \mathcal{P}_{\text{hp}}}{\mathcal{P}} \cdot 100\%$", r""),
            ),
        ],
        "example": r"Một nhà máy điện truyền tải một công suất điện không đổi $\mathcal{P} = 1000\text{ kW}$ đi xa dưới hiệu điện thế $U = 10\text{ kV}$ trên đường dây tải điện có tổng điện trở $R = 10\text{ }\Omega$. Tính cường độ dòng điện trên dây, công suất hao phí $\mathcal{P}_{\text{hp}}$ do tỏa nhiệt trên đường dây và hiệu suất truyền tải điện $H$. Nếu dùng máy biến áp nâng hiệu điện thế truyền tải lên $U' = 100\text{ kV}$ thì công suất hao phí còn lại bao nhiêu?",
        "example_answer": r"""- Đổi đơn vị: $\mathcal{P} = 1000\text{ kW} = 10^6\text{ W}$ và $U = 10\text{ kV} = 10^4\text{ V}$. Cường độ dòng điện trên đường dây là:
$$I = \dfrac{\mathcal{P}}{U} = \dfrac{10^6}{10^4} = 100\text{ A}$$
- Công suất hao phí do tỏa nhiệt trên đường dây và hiệu suất truyền tải là:
$$\mathcal{P}_{\text{hp}} = I^2 R = 100^2 \cdot 10 = 100000\text{ W} = 100\text{ kW};\quad H = \dfrac{1000 - 100}{1000} \cdot 100\% = 90\%$$
- Khi tăng hiệu điện thế từ $10\text{ kV}$ lên $100\text{ kV}$ (tăng gấp $n = 10$ lần), công suất hao phí giảm đi $n^2 = 10^2 = 100$ lần:
$$\mathcal{P}'_{\text{hp}} = \dfrac{100\text{ kW}}{100} = 1\text{ kW}\quad (\text{Hiệu suất tăng lên } 99{,}9\%)$$""",
        "real_life": r"""- **Hệ thống lưới điện quốc gia**: Các nhà máy thủy điện, nhiệt điện, điện gió tạo ra dòng điện xoay chiều, đưa qua trạm biến áp tăng áp lên $220\text{ kV}$ hoặc $500\text{ kV}$ để truyền tải đi xa rồi hạ áp xuống $220\text{ V}$ phục vụ sinh hoạt.
- **Thiết bị hiện đại**: Bếp từ đun nấu bằng dòng điện cảm ứng (dòng Foucault) sinh ra trực tiếp trong đáy nồi nhiễm từ; sạc không dây điện thoại và đinamô xe đạp đều hoạt động dựa trên hiện tượng cảm ứng điện từ.""",
        "game_title": "Thử thách thực tế: Cảm ứng điện từ và Lưới điện",
        "game_description": "Thí nghiệm đưa nam châm qua cuộn dây, điều chỉnh tốc độ quay máy phát điện và chọn tỉ số vòng dây máy biến áp để tối ưu truyền tải điện.",
        "game_type": "game_dientu",
        "quiz": [
            mcq(
                "biet",
                r"Điều kiện để xuất hiện dòng điện cảm ứng trong một cuộn dây dẫn kín là gì?",
                [
                    r"Đặt một thanh nam châm mạnh nằm đứng yên bên trong lòng cuộn dây dẫn kín",
                    r"Số đường sức từ xuyên qua tiết diện của cuộn dây dẫn kín đó biến thiên (tăng hoặc giảm)",
                    r"Nối cuộn dây dẫn với một viên pin một chiều không đổi",
                    r"Cho cuộn dây dẫn chuyển động tịnh tiến trong vùng không có từ trường",
                ],
                1,
                r"Dòng điện cảm ứng chỉ xuất hiện trong cuộn dây dẫn kín khi số đường sức từ xuyên qua tiết diện của cuộn dây biến thiên (tăng hoặc giảm).",
            ),
            mcq(
                "biet",
                r"Nguyên tắc tạo ra dòng điện xoay chiều trong các máy phát điện xoay chiều dựa trên hiện tượng vật lí nào?",
                [
                    r"Hiện tượng nhiễm điện do cọ xát",
                    r"Hiện tượng cảm ứng điện từ",
                    r"Tác dụng hóa học của dòng điện",
                    r"Hiện tượng giãn nở vì nhiệt của kim loại",
                ],
                1,
                r"Máy phát điện xoay chiều hoạt động dựa trên hiện tượng cảm ứng điện từ khi số đường sức từ qua tiết diện cuộn dây biến thiên tuần hoàn.",
            ),
            mcq(
                "biet",
                r"Khi cho dòng điện xoay chiều chạy qua một cuộn dây dẫn quấn quanh lõi sắt non, nếu đặt một cực của nam châm vĩnh cửu lại gần một đầu cuộn dây thì hiện tượng gì xảy ra?",
                [
                    r"Cuộn dây chỉ hút cực nam châm đó đứng yên tại một chỗ",
                    r"Cuộn dây chỉ đẩy cực nam châm đó ra xa",
                    r"Cuộn dây luân phiên hút và đẩy cực nam châm đó do dòng điện đổi chiều liên tục",
                    r"Cuộn dây không tác dụng bất kì lực từ nào lên nam châm",
                ],
                2,
                r"Vì dòng điện xoay chiều đổi chiều liên tục nên từ trường của cuộn dây cũng đổi chiều liên tục, gây ra lực từ hút và đẩy nam châm luân phiên.",
            ),
            mcq(
                "biet",
                r"Một máy biến áp lí tưởng có số vòng dây cuộn sơ cấp là $N_1$ và số vòng dây cuộn thứ cấp là $N_2$. Khi đặt hiệu điện thế xoay chiều $U_1$ vào hai đầu cuộn sơ cấp thì hiệu điện thế $U_2$ ở hai đầu cuộn thứ cấp để hở thỏa mãn hệ thức nào?",
                [
                    r"$\dfrac{U_1}{U_2} = \dfrac{N_2}{N_1}$",
                    r"$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$",
                    r"$U_1 \cdot N_1 = U_2 \cdot N_2$",
                    r"$\dfrac{U_1}{U_2} = \left(\dfrac{N_1}{N_2}\right)^2$",
                ],
                1,
                r"Trong máy biến áp lí tưởng, hiệu điện thế ở hai đầu mỗi cuộn dây tỉ lệ thuận với số vòng dây của cuộn đó: $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$.",
            ),
            mcq(
                "hieu",
                r"Một máy biến áp có cuộn sơ cấp gồm $N_1 = 2200\text{ vòng}$ và cuộn thứ cấp gồm $N_2 = 120\text{ vòng}$. Khi đặt vào hai đầu cuộn sơ cấp một hiệu điện thế xoay chiều $U_1 = 220\text{ V}$ thì hiệu điện thế xoay chiều $U_2$ ở hai đầu cuộn thứ cấp là:",
                [r"$12\text{ V}$ (máy hạ áp)", r"$24\text{ V}$ (máy hạ áp)", r"$4033\text{ V}$ (máy tăng áp)", r"$120\text{ V}$ (máy hạ áp)"],
                0,
                r"Ta có $U_2 = U_1 \cdot \dfrac{N_2}{N_1} = 220 \cdot \dfrac{120}{2200} = 12\text{ V}$. Vì $U_2 < U_1$ nên đây là máy hạ áp.",
            ),
            mcq(
                "hieu",
                r"Trên cùng một đường dây tải điện và cùng một công suất điện $\mathcal{P}$ cần truyền đi, nếu dùng máy biến áp để tăng hiệu điện thế ở nơi truyền đi lên gấp $5$ lần thì công suất hao phí do tỏa nhiệt trên đường dây sẽ:",
                [r"Giảm đi $5$ lần", r"Tăng lên $5$ lần", r"Giảm đi $25$ lần", r"Giảm đi $10$ lần"],
                2,
                r"Theo công thức $\mathcal{P}_{\text{hp}} = \dfrac{\mathcal{P}^2 R}{U^2}$, công suất hao phí tỉ lệ nghịch với bình phương hiệu điện thế nên khi $U$ tăng $5$ lần thì $\mathcal{P}_{\text{hp}}$ giảm $5^2 = 25$ lần.",
            ),
            tf4(
                "hieu",
                r"Một học sinh bố trí thí nghiệm gồm một cuộn dây dẫn kín mắc với hai bóng đèn LED song song nhưng ngược cực nhau và một thanh nam châm vĩnh cửu. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Khi đưa cực Bắc ($\text{N}$) của thanh nam châm lại gần cuộn dây, số đường sức từ xuyên qua tiết diện cuộn dây tăng lên và một trong hai đèn LED lóe sáng.",
                    r"b) Khi giữ thanh nam châm đứng yên bên trong lòng cuộn dây thì cả hai đèn LED đều sáng liên tục.",
                    r"c) Khi kéo cực Bắc ($\text{N}$) của thanh nam châm ra xa cuộn dây, số đường sức từ qua cuộn dây giảm đi làm xuất hiện dòng điện cảm ứng ngược chiều với lúc đưa vào nên chiếc đèn LED thứ hai lóe sáng.",
                    r"d) Nếu giữ nam châm đứng yên và dịch chuyển cuộn dây lại gần hoặc ra xa nam châm thì trong cuộn dây vẫn xuất hiện dòng điện cảm ứng.",
                ],
                [True, False, True, True],
                r"a) Đúng vì số đường sức từ tăng sinh ra dòng điện cảm ứng theo một chiều làm sáng đèn LED ứng với chiều đó. b) Sai vì khi nam châm đứng yên, số đường sức từ không biến thiên nên không có dòng điện cảm ứng, cả hai đèn đều tắt. c) Đúng vì khi số đường sức từ giảm thì dòng điện cảm ứng đổi chiều ngược lại. d) Đúng.",
            ),
            tf4(
                "hieu",
                r"Xét các tính chất, tác dụng của dòng điện xoay chiều và các nguồn năng lượng sản xuất điện. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Mạng điện xoay chiều dân dụng ở Việt Nam có hiệu điện thế hiệu dụng $220\text{ V}$ và tần số $50\text{ Hz}$ (dòng điện đổi chiều $100$ lần trong mỗi giây).",
                    r"b) Có thể sử dụng trực tiếp dòng điện xoay chiều $220\text{ V}$ để tiến hành mạ điện (mạ vàng, mạ bạc) giống hệt như dòng điện một chiều.",
                    r"c) Máy biến áp chỉ hoạt động được với dòng điện xoay chiều, không thể dùng máy biến áp để biến đổi hiệu điện thế của nguồn điện một chiều không đổi (như ắc quy).",
                    r"d) Năng lượng gió, năng lượng Mặt Trời và năng lượng sóng biển là các nguồn năng lượng tái tạo sạch giúp giảm phát thải khí nhà kính so với đốt nhiên liệu hóa thạch.",
                ],
                [True, False, True, True],
                r"a) Đúng (mỗi chu kì dòng điện đổi chiều $2$ lần nên tần số $50\text{ Hz}$ đổi chiều $100$ lần mỗi giây). b) Sai vì dòng điện xoay chiều đổi chiều liên tục nên không dùng trực tiếp để mạ điện được (phải chỉnh lưu thành dòng điện một chiều). c) Đúng vì dòng một chiều không đổi không tạo ra từ trường biến thiên qua cuộn thứ cấp. d) Đúng.",
            ),
            mcq(
                "vandung",
                r"Một máy phát điện xoay chiều truyền đi một công suất điện $\mathcal{P} = 500\text{ kW}$ dưới hiệu điện thế $U = 25\text{ kV}$ trên đường dây tải điện có tổng điện trở $R = 20\text{ }\Omega$. Công suất hao phí do tỏa nhiệt trên đường dây này là:",
                [r"$4\text{ kW}$", r"$8\text{ kW}$", r"$20\text{ kW}$", r"$40\text{ kW}$"],
                1,
                r"Đổi $\mathcal{P} = 500\text{ kW} = 5 \cdot 10^5\text{ W}$ và $U = 25\text{ kV} = 2{,}5 \cdot 10^4\text{ V}$. Cường độ dòng điện trên dây là $I = \dfrac{\mathcal{P}}{U} = \dfrac{5 \cdot 10^5}{2{,}5 \cdot 10^4} = 20\text{ A}$. Công suất hao phí là $\mathcal{P}_{\text{hp}} = I^2 R = 20^2 \cdot 20 = 8000\text{ W} = 8\text{ kW}$.",
            ),
            short(
                "vandung",
                r"Một máy biến áp lí tưởng có số vòng dây cuộn sơ cấp là $N_1 = 1500\text{ vòng}$. Khi đặt vào hai đầu cuộn sơ cấp hiệu điện thế xoay chiều $U_1 = 200\text{ V}$ thì hiệu điện thế đo được ở hai đầu cuộn thứ cấp để hở là $U_2 = 60\text{ V}$. Tính số vòng dây $N_2$ của cuộn thứ cấp.",
                ["450"],
                r"Áp dụng công thức máy biến áp: $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2} \Rightarrow N_2 = N_1 \cdot \dfrac{U_2}{U_1} = 1500 \cdot \dfrac{60}{200} = 450\text{ vòng}$.",
            ),
        ],
    },
]
