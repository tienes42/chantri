"""KHOA HỌC TỰ NHIÊN 7 (PHẦN VẬT LÍ) — Kết nối tri thức với cuộc sống.

Bao phủ đầy đủ 4 chương Vật lí trong SGK KHTN 7 KNTT (Chương III: Tốc độ; Chương IV: Âm thanh; Chương V: Ánh sáng; Chương VI: Từ, từ Bài 8 đến Bài 20), chia thành 7 chủ đề tương thích hệ thống game thực nghiệm.
Mỗi chủ đề: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 7

LESSONS = [
    {
        "topic": "toc-do-chuyen-dong",
        "title": "Tốc độ chuyển động, Đo tốc độ và Đồ thị quãng đường - thời gian",
        "icon": "📈",
        "description": "Chương III · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (tr. 45–59): Bài 8 – Bài 11. Khái niệm tốc độ chuyển động và đơn vị đo; đo tốc độ bằng đồng hồ bấm giây và cổng quang điện; vẽ và đọc đồ thị quãng đường – thời gian; ảnh hưởng của tốc độ trong an toàn giao thông và quy tắc giữ khoảng cách an toàn.",
        "requirements": [
            r"Nêu được ý nghĩa vật lí của tốc độ, xác định được tốc độ qua quãng đường vật đi được trong một khoảng thời gian tương ứng ($v = \dfrac{s}{t}$) và đổi được các đơn vị đo tốc độ ($\text{m/s}$, $\text{km/h}$).",
            r"Mô tả được sơ lược cách đo tốc độ bằng đồng hồ bấm giây và bằng đồng hồ đo thời gian hiện số dùng cổng quang điện trong phòng thực hành; nêu được thiết bị “bắn tốc độ” trong kiểm tra giao thông.",
            r"Vẽ được đồ thị quãng đường – thời gian ($s - t$) cho chuyển động thẳng từ bảng số liệu cho trước và tìm được tốc độ, quãng đường hoặc thời gian từ đồ thị.",
            r"Dựa vào tranh ảnh hoặc số liệu thực tế, thảo luận để nêu được ảnh hưởng của tốc độ trong an toàn giao thông và vận dụng được quy tắc “$3\text{ giây}$” để ước lượng khoảng cách an toàn tối thiểu giữa hai xe.",
        ],
        "definition": (
            r"- **Tốc độ chuyển động** (kí hiệu $v$) cho biết mức độ nhanh hay chậm của chuyển động, được tính bằng quãng đường đi được trong một đơn vị thời gian: $v = \dfrac{s}{t}$. Tốc độ trung bình trên nhiều chặng được tính bằng tổng quãng đường chia cho tổng thời gian: $v_{\text{tb}} = \dfrac{s_1 + s_2 + \dots}{t_1 + t_2 + \dots}$." "\n"
            r"- **Đồ thị quãng đường – thời gian ($s - t$)** mô tả liên hệ giữa quãng đường đi được $s$ (trục tung) và thời gian $t$ (trục hoành): đường biểu diễn là **đường thẳng xiên góc** khi vật chuyển động với tốc độ không đổi và là **đường thẳng nằm ngang song song với trục thời gian** khi vật đứng yên." "\n"
            r"- **Quy tắc “$3\text{ giây}$” trên đường cao tốc**: Khoảng cách an toàn tối thiểu (tính bằng $\text{m}$) bằng quãng đường xe đi được trong $3\text{ s}$: $d_{\min} = v(\text{m/s}) \cdot 3$."
        ),
        "theory": (
            r"### Bài 8. Tốc độ chuyển động" "\n"
            r"- Công thức tính tốc độ: $v = \dfrac{s}{t}$, suy ra $s = v \cdot t$ và $t = \dfrac{s}{v}$." "\n"
            r"- Trong hệ SI, đơn vị tốc độ là $\text{m/s}$; trong thực tế thường dùng $\text{km/h}$, $\text{cm/s}$. Chuyển đổi: $1\text{ m/s} = 3{,}6\text{ km/h}$." "\n"
            r"### Bài 9. Đo tốc độ" "\n"
            r"- **Dùng đồng hồ bấm giây**: Đánh dấu vạch xuất phát $A$ và vạch đích $B$, dùng thước đo khoảng cách $s = AB$, dùng đồng hồ bấm giây đo thời gian $t$ vật đi từ $A$ đến $B$, rồi tính $v = \dfrac{s}{t}$." "\n"
            r"- **Dùng cổng quang điện và đồng hồ đo thời gian hiện số**: Đặt hai cổng quang điện $C_1, C_2$ cách nhau quãng đường $s$; khi vật chắn tia hồng ngoại ở $C_1$ đồng hồ tự động bắt đầu đếm và khi tới $C_2$ đồng hồ tự động dừng (chế độ $A \leftrightarrow B$), giúp loại bỏ sai số phản xạ bấm tay của người đo." "\n"
            r"- **Thiết bị “bắn tốc độ”** (súng bắn tốc độ radar hoặc laser hoặc camera giám sát): Đo thời gian rất ngắn giữa hai lần chụp ảnh hoặc thu sóng phản xạ để tính chính xác tốc độ phương tiện." "\n"
            r"### Bài 10. Đồ thị quãng đường - thời gian" "\n"
            r"- Trục hoành $Ot$ biểu diễn thời gian $t$, trục tung $Os$ biểu diễn quãng đường $s$." "\n"
            r"- Trên đồ thị $s - t$, đường biểu diễn **càng dốc** (tạo với trục $Ot$ góc càng lớn) thì tốc độ chuyển động của vật **càng lớn**." "\n"
            r"- Nếu đoạn đồ thị là đường thẳng nằm ngang (quãng đường $s$ không tăng khi thời gian $t$ trôi đi) thì trong khoảng thời gian đó vật **đứng yên** ($v = 0$)." "\n"
            r"### Bài 11. Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông" "\n"
            r"- Khi tốc độ càng cao, thời gian để người lái xe xử lí tình huống càng ngắn và quãng đường phanh dừng xe càng dài, nếu xảy ra va chạm thì hậu quả càng nghiêm trọng." "\n"
            r"- Người tham gia giao thông phải tuân thủ biển báo tốc độ tối đa, tốc độ tối thiểu (theo làn đường, loại phương tiện và điều kiện thời tiết mưa trơn) và giữ khoảng cách an toàn tối thiểu giữa hai xe."
        ),
        "formulas": [
            G(
                "I. Tốc độ chuyển động & Tốc độ trung bình",
                F("Công thức tốc độ", r"$v = \dfrac{s}{t} \iff s = v \cdot t \iff t = \dfrac{s}{v}$"),
                F("Tốc độ trung bình trên nhiều chặng", r"$v_{\text{tb}} = \dfrac{s_1 + s_2 + \dots + s_n}{t_1 + t_2 + \dots + t_n}$", r"Không lấy trung bình cộng $\dfrac{v_1 + v_2}{2}$ khi thời gian hai chặng khác nhau."),
                F("Đổi đơn vị tốc độ", r"$v(\text{km/h}) = 3{,}6 \cdot v(\text{m/s}); \quad v(\text{m/s}) = \dfrac{v(\text{km/h})}{3{,}6}$"),
            ),
            G(
                "II. Đồ thị s - t & Khoảng cách an toàn giao thông",
                F("Tốc độ trên một đoạn thẳng đồ thị s - t", r"$v = \dfrac{\Delta s}{\Delta t} = \dfrac{s_2 - s_1}{t_2 - t_1}$", r"Độ dốc của đồ thị $s - t$ biểu thị tốc độ."),
                F("Khoảng cách an toàn theo quy tắc 3 giây", r"$d_{\min}(\text{m}) = v(\text{m/s}) \cdot 3 = \dfrac{v(\text{km/h})}{3{,}6} \cdot 3$", r"Áp dụng trên đường cao tốc khi mặt đường khô ráo."),
            ),
        ],
        "example": (
            r"Một ô tô đi trên chặng đường đầu dài $s_1 = 30\text{ km}$ hết thời gian $t_1 = 0{,}5\text{ h}$, sau đó dừng nghỉ $15\text{ phút}$ rồi đi tiếp chặng đường thứ hai dài $s_2 = 45\text{ km}$ hết thời gian $t_2 = 0{,}75\text{ h}$. Tính tốc độ của ô tô trên từng chặng và tốc độ trung bình trên toàn bộ hành trình (kể cả thời gian nghỉ)."
        ),
        "example_answer": (
            r"- Tốc độ trên chặng thứ nhất: $v_1 = \dfrac{s_1}{t_1} = \dfrac{30}{0{,}5} = 60\text{ km/h}$." "\n"
            r"- Tốc độ trên chặng thứ hai: $v_2 = \dfrac{s_2}{t_2} = \dfrac{45}{0{,}75} = 60\text{ km/h}$." "\n"
            r"- Thời gian dừng nghỉ là $t_{\text{nghỉ}} = 15\text{ phút} = 0{,}25\text{ h}$. Tổng thời gian toàn hành trình là $t = 0{,}5 + 0{,}25 + 0{,}75 = 1{,}5\text{ h}$ và tổng quãng đường là $s = 30 + 45 = 75\text{ km}$." "\n"
            r"- Tốc độ trung bình trên cả hành trình là: $v_{\text{tb}} = \dfrac{75}{1{,}5} = 50\text{ km/h}$."
        ),
        "real_life": (
            r"- Hệ thống camera giám sát tốc độ trên quốc lộ và đường cao tốc giúp phát hiện phương tiện chạy quá tốc độ quy định để giảm thiểu tai nạn giao thông." "\n"
            r"- Theo quy định của Bộ Giao thông vận tải Việt Nam trên đường bộ ngoài khu đông dân cư (mặt đường khô ráo): tốc độ $v = 60\text{ km/h}$ cần giữ khoảng cách tối thiểu $35\text{ m}$; từ trên $60$ đến $80\text{ km/h}$ là $55\text{ m}$; từ trên $80$ đến $100\text{ km/h}$ là $70\text{ m}$; từ trên $100$ đến $120\text{ km/h}$ là $100\text{ m}$."
        ),
        "game_title": "Mô phỏng Đồ thị Quãng đường - Thời gian và An toàn giao thông",
        "game_description": "Đo tốc độ qua cổng quang điện, vẽ đồ thị quãng đường – thời gian của chuyển động và tính khoảng cách an toàn tối thiểu theo quy tắc 3 giây.",
        "game_type": "game_speed",
        "quiz": [
            mcq(
                "biet",
                r"Trong phòng thực hành Khoa học tự nhiên $7$, để đo thời gian chuyển động của viên bi thép trên máng nghiêng một cách tự động và giảm sai số do phản xạ của người bấm, người ta thường kết hợp đồng hồ đo thời gian hiện số với dụng cụ nào?",
                [
                    r"Cổng quang điện.",
                    r"Nhiệt kế điện tử.",
                    r"Lực kế lò xo.",
                    r"Cân Roberval.",
                ],
                0,
                r"**Cổng quang điện** phát và thu tia hồng ngoại giúp đóng hoặc ngắt đồng hồ đo thời gian hiện số hoàn toàn tự động khi viên bi đi qua.",
            ),
            mcq(
                "biet",
                r"Trên đồ thị quãng đường – thời gian ($s - t$) của một vật, nếu đường biểu diễn là một đoạn thẳng **nằm ngang song song với trục thời gian $Ot$** thì trong khoảng thời gian đó vật đang ở trạng thái nào?",
                [
                    r"Đứng yên ($v = 0$).",
                    r"Chuyển động thẳng với tốc độ không đổi khác $0$.",
                    r"Chuyển động nhanh dần.",
                    r"Quay tròn tại chỗ với tốc độ rất lớn.",
                ],
                0,
                r"Đường biểu diễn song song với trục $Ot$ có nghĩa là khi thời gian $t$ tăng lên thì quãng đường $s$ không thay đổi, chứng tỏ vật đang **đứng yên**.",
            ),
            mcq(
                "biet",
                r"Theo quy tắc “$3\text{ giây}$” dùng để ước lượng khoảng cách an toàn tối thiểu $d_{\min}$ trên đường cao tốc, nếu xe chạy với tốc độ $v$ (tính bằng $\text{m/s}$) thì khoảng cách an toàn tối thiểu được tính theo công thức nào?",
                [
                    r"$d_{\min} = v \cdot 3$.",
                    r"$d_{\min} = \dfrac{v}{3}$.",
                    r"$d_{\min} = v + 3$.",
                    r"$d_{\min} = v^3$.",
                ],
                0,
                r"Theo quy tắc “$3\text{ giây}$”, khoảng cách an toàn tối thiểu bằng quãng đường xe đi được trong $3\text{ s}$: $d_{\min}(\text{m}) = v(\text{m/s}) \cdot 3$.",
            ),
            mcq(
                "biet",
                r"Khi trời mưa to làm mặt đường trơn trượt và tầm nhìn bị hạn chế, người điều khiển phương tiện giao thông cần thực hiện biện pháp nào sau đây để đảm bảo an toàn?",
                [
                    r"Giảm tốc độ và tăng khoảng cách an toàn với xe chạy liền trước.",
                    r"Tăng tốc độ để nhanh chóng vượt qua khu vực trời mưa.",
                    r"Giữ nguyên tốc độ tối đa và bám thật sát đuôi xe phía trước.",
                    r"Tắt hết đèn chiếu sáng để tiết kiệm điện ắc quy.",
                ],
                0,
                r"Khi trời mưa đường trơn, lực ma sát giảm làm quãng đường phanh dài ra nên người lái phải **giảm tốc độ và tăng khoảng cách an toàn**.",
            ),
            mcq(
                "hieu",
                r"Trong thí nghiệm đo tốc độ bằng hai cổng quang điện đặt cách nhau một khoảng $s = 0{,}6\text{ m}$, đồng hồ đo thời gian hiện số ở chế độ $A \leftrightarrow B$ hiển thị thời gian viên bi lăn từ cổng thứ nhất đến cổng thứ hai là $t = 0{,}4\text{ s}$. Tốc độ của viên bi trên đoạn đường giữa hai cổng là:",
                [
                    r"$1{,}5\text{ m/s}$.",
                    r"$0{,}24\text{ m/s}$.",
                    r"$2{,}4\text{ m/s}$.",
                    r"$0{,}67\text{ m/s}$.",
                ],
                0,
                r"Áp dụng công thức tính tốc độ: $v = \dfrac{s}{t} = \dfrac{0{,}6}{0{,}4} = 1{,}5\text{ m/s}$.",
            ),
            mcq(
                "hieu",
                r"Một ô tô đang chạy trên đường cao tốc với tốc độ ổn định $v = 72\text{ km/h}$. Theo quy tắc “$3\text{ giây}$”, khoảng cách an toàn tối thiểu mà người lái xe cần giữ đối với xe chạy ngay phía trước là:",
                [
                    r"$60\text{ m}$.",
                    r"$216\text{ m}$.",
                    r"$20\text{ m}$.",
                    r"$72\text{ m}$.",
                ],
                0,
                r"Đổi $v = 72\text{ km/h} = \dfrac{72}{3{,}6}\text{ m/s} = 20\text{ m/s}$. Theo quy tắc “$3\text{ giây}$”, khoảng cách an toàn tối thiểu là $d_{\min} = 20 \cdot 3 = 60\text{ m}$.",
            ),
            tf4(
                "hieu",
                r"Trên cùng một hệ trục toạ độ đồ thị quãng đường – thời gian ($s - t$ với $s$ tính bằng $\text{km}$, $t$ tính bằng $\text{h}$), đường biểu diễn chuyển động của xe $A$ đi qua gốc $O(0; 0)$ và điểm $M(2; 80)$, còn đường biểu diễn của xe $B$ đi qua gốc $O(0; 0)$ và điểm $N(2; 50)$. Xét tính đúng sai của các khẳng định sau:",
                [
                    r"a) Tốc độ chuyển động của xe $A$ là $40\text{ km/h}$.",
                    r"b) Tốc độ chuyển động của xe $B$ là $25\text{ km/h}$.",
                    r"c) Trên đồ thị $s - t$, đường biểu diễn của xe $A$ nằm thấp hơn (ít dốc hơn) đường biểu diễn của xe $B$.",
                    r"d) Sau $3\text{ h}$ chuyển động liên tục với tốc độ như trên, hai xe cách nhau một quãng đường $45\text{ km}$ (nếu cùng xuất phát tại $O$ và đi cùng chiều).",
                ],
                [True, True, False, True],
                r"a) Đúng vì $v_A = \dfrac{80}{2} = 40\text{ km/h}$." "\n"
                r"b) Đúng vì $v_B = \dfrac{50}{2} = 25\text{ km/h}$." "\n"
                r"c) Sai vì tại cùng $t = 2\text{ h}$ thì $s_A = 80\text{ km} > s_B = 50\text{ km}$ nên đường biểu diễn của xe $A$ dốc hơn (nằm cao hơn) xe $B$." "\n"
                r"d) Đúng vì sau $3\text{ h}$, quãng đường hai xe đi được chênh lệch $\Delta s = (40 - 25) \cdot 3 = 45\text{ km}$.",
            ),
            tf4(
                "hieu",
                r"Đồ thị quãng đường – thời gian của một người đi xe đạp gồm $3$ giai đoạn: từ $t = 0$ đến $t_1 = 0{,}5\text{ h}$, quãng đường tăng đều từ $0$ đến $8\text{ km}$; từ $t_1 = 0{,}5\text{ h}$ đến $t_2 = 0{,}75\text{ h}$, quãng đường giữ nguyên ở $8\text{ km}$; từ $t_2 = 0{,}75\text{ h}$ đến $t_3 = 1{,}25\text{ h}$, quãng đường tăng đều từ $8\text{ km}$ lên $18\text{ km}$. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Trong giai đoạn đầu ($0$ đến $0{,}5\text{ h}$), người đó đạp xe với tốc độ $16\text{ km/h}$.",
                    r"b) Người đó đã dừng lại nghỉ ngơi trong khoảng thời gian $15\text{ phút}$ (từ $0{,}5\text{ h}$ đến $0{,}75\text{ h}$).",
                    r"c) Trong giai đoạn cuối ($0{,}75\text{ h}$ đến $1{,}25\text{ h}$), tốc độ của người đó là $36\text{ km/h}$.",
                    r"d) Tốc độ trung bình trên toàn bộ hành trình $1{,}25\text{ h}$ là $14{,}4\text{ km/h}$.",
                ],
                [True, True, False, True],
                r"a) Đúng vì $v_1 = \dfrac{8 - 0}{0{,}5 - 0} = 16\text{ km/h}$." "\n"
                r"b) Đúng vì quãng đường không đổi trong $\Delta t_2 = 0{,}75 - 0{,}5 = 0{,}25\text{ h} = 15\text{ phút}$." "\n"
                r"c) Sai vì trong giai đoạn cuối, người đó đi thêm $\Delta s_3 = 18 - 8 = 10\text{ km}$ trong thời gian $\Delta t_3 = 1{,}25 - 0{,}75 = 0{,}5\text{ h}$ nên tốc độ là $v_3 = \dfrac{10}{0{,}5} = 20\text{ km/h}$." "\n"
                r"d) Đúng vì tốc độ trung bình trên cả hành trình là $v_{\text{tb}} = \dfrac{18}{1{,}25} = 14{,}4\text{ km/h}$.",
            ),
            mcq(
                "vandung",
                r"Một vận động viên xe đạp leo một đoạn đèo dài $s_1 = 6\text{ km}$ với tốc độ $v_1 = 12\text{ km/h}$, sau đó lập tức đổ đèo trên đoạn đường dài $s_2 = 9\text{ km}$ với tốc độ $v_2 = 36\text{ km/h}$. Tốc độ trung bình của vận động viên trên cả hai đoạn đường leo đèo và đổ đèo là:",
                [
                    r"$20\text{ km/h}$.",
                    r"$24\text{ km/h}$.",
                    r"$18\text{ km/h}$.",
                    r"$22{,}5\text{ km/h}$.",
                ],
                0,
                r"Thời gian leo đèo là $t_1 = \dfrac{s_1}{v_1} = \dfrac{6}{12} = 0{,}5\text{ h}$. Thời gian đổ đèo là $t_2 = \dfrac{s_2}{v_2} = \dfrac{9}{36} = 0{,}25\text{ h}$. Tốc độ trung bình trên cả quãng đường là $v_{\text{tb}} = \dfrac{s_1 + s_2}{t_1 + t_2} = \dfrac{6 + 9}{0{,}5 + 0{,}25} = \dfrac{15}{0{,}75} = 20\text{ km/h}$.",
            ),
            short(
                "vandung",
                r"Một camera bắn tốc độ trên đường cao tốc ghi nhận một chiếc ô tô đi qua hai vạch mốc cách nhau $s = 50\text{ m}$ trong khoảng thời gian $t = 1{,}8\text{ s}$. Tính tốc độ của ô tô đó theo đơn vị ki-lô-mét trên giờ ($\text{km/h}$).",
                ["100", "100,0", "100.0"],
                r"Tốc độ của ô tô tính theo $\text{m/s}$ là $v = \dfrac{50}{1{,}8}\text{ m/s}$. Đổi sang $\text{km/h}$: $v = \dfrac{50}{1{,}8} \cdot 3{,}6 = 50 \cdot 2 = 100\text{ km/h}$.",
            ),
        ],
    },
    {
        "topic": "am-thanh",
        "title": "Sóng âm, Độ to và độ cao của âm, Phản xạ âm",
        "icon": "🔊",
        "description": "Chương IV · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (tr. 60–72): Bài 12 – Bài 14. Nguồn âm, dao động âm và sự truyền sóng âm trong các môi trường rắn, lỏng, khí; biên độ dao động và độ to của âm, tần số dao động và độ cao của âm; hiện tượng phản xạ âm, tiếng vang, vật liệu phản xạ âm tốt – hấp thụ âm tốt và các biện pháp chống ô nhiễm tiếng ồn.",
        "requirements": [
            r"Thực hiện thí nghiệm tạo sóng âm (như gảy đàn, gõ âm thoa) để chứng tỏ được sóng âm có thể truyền được trong chất rắn, chất lỏng, chất khí và không truyền được trong chân không.",
            r"Giải thích được sự truyền sóng âm trong không khí là sự lan truyền dao động của các lớp không khí (gồm các miền nén và dãn xen kẽ).",
            r"Từ hình ảnh hoặc đồ thị dao động âm trên màn hình dao động kí, nêu được mối liên hệ giữa độ to của âm với biên độ dao động và giữa độ cao của âm với tần số dao động ($f = \dfrac{N}{t}$).",
            r"Lấy được ví dụ về vật phản xạ âm tốt, vật phản xạ âm kém (hấp thụ âm tốt); giải thích được sự tạo thành tiếng vang và nguyên tắc đo độ sâu đáy biển bằng sóng siêu âm (Sonar).",
            r"Đề xuất được phương án đơn giản để hạn chế tiếng ồn ảnh hưởng đến sức khoẻ và học tập.",
        ],
        "definition": (
            r"- **Nguồn âm** là vật phát ra âm; mọi nguồn âm khi phát ra âm đều **dao động** (chuyển động qua lại quanh vị trí cân bằng). **Sóng âm** là sự lan truyền dao động của nguồn âm trong môi trường rắn, lỏng, khí; sóng âm **không truyền được trong chân không** ($v_{\text{rắn}} > v_{\text{lỏng}} > v_{\text{khí}}$)." "\n"
            r"- **Biên độ dao động** là độ lệch lớn nhất của vật dao động so với vị trí cân bằng; biên độ càng lớn thì âm nghe càng **to** (đơn vị độ to là **đề-xi-ben**, kí hiệu $\text{dB}$)." "\n"
            r"- **Tần số** (kí hiệu $f$, đơn vị là **héc**, kí hiệu $\text{Hz}$) là số dao động thực hiện được trong $1\text{ s}$: $f = \dfrac{N}{t}$. Tần số càng lớn thì âm nghe càng **cao (bổng)**; tần số càng nhỏ thì âm nghe càng **thấp (trầm)**." "\n"
            r"- **Tiếng vang** là âm phản xạ nghe được cách âm truyền trực tiếp ít nhất là $\dfrac{1}{15}\text{ s}$."
        ),
        "theory": (
            r"### Bài 12. Sóng âm" "\n"
            r"- Khi nhánh âm thoa hoặc màng loa dao động, nó làm lớp không khí tiếp xúc bị nén và dãn liên tiếp, truyền dao động đi xa tới màng nhĩ làm tai ta nghe được âm." "\n"
            r"- **Môi trường truyền âm**: Sóng âm truyền được trong chất rắn, chất lỏng và chất khí, nhưng không truyền được trong chân không. Nhìn chung, tốc độ truyền âm trong chất rắn lớn hơn trong chất lỏng, và trong chất lỏng lớn hơn trong chất khí (ví dụ ở nhiệt độ thường: $v_{\text{không khí}} \approx 340\text{ m/s}$, $v_{\text{nước}} \approx 1500\text{ m/s}$, $v_{\text{thép}} \approx 6100\text{ m/s}$)." "\n"
            r"### Bài 13. Độ to và độ cao của âm" "\n"
            r"- **Độ cao của âm và tần số**: Tần số $f = \dfrac{N}{t}$ ($\text{Hz}$). Tai người bình thường nghe được âm có tần số từ $20\text{ Hz}$ đến $20\,000\text{ Hz}$; âm có $f < 20\text{ Hz}$ là **hạ âm** (voi, chim bồ câu nghe được), âm có $f > 20\,000\text{ Hz}$ là **siêu âm** (dơi, cá heo, chó nghe được)." "\n"
            r"- **Độ to của âm và biên độ**: Trên màn hình dao động kí (oscilloscope), đỉnh sóng càng cao thì biên độ dao động càng lớn và âm càng to; các đỉnh sóng càng dày (mau) thì tần số càng lớn và âm càng cao." "\n"
            r"### Bài 14. Phản xạ âm, chống ô nhiễm tiếng ồn" "\n"
            r"- **Vật phản xạ âm tốt**: Những vật cứng, có bề mặt nhẵn (tường gạch phẳng, mặt kính, tấm kim loại, mặt đá hoa). **Vật phản xạ âm kém (hấp thụ âm tốt)**: Những vật mềm, xốp, bề mặt gồ ghề (rèm nhung, thảm len, mút xốp, tường sần sùi, cây xanh)." "\n"
            r"- **Điều kiện có tiếng vang trong không khí** ($v \approx 340\text{ m/s}$): Thời gian từ lúc âm phát ra đến khi nhận âm phản xạ là $t \ge \dfrac{1}{15}\text{ s}$. Quãng đường âm đi và về là $2d = v \cdot t$, nên khoảng cách ngắn nhất từ nguồn âm đến mặt chắn là $d_{\min} = \dfrac{v \cdot t_{\min}}{2} = \dfrac{340 \cdot \dfrac{1}{15}}{2} \approx 11{,}33\text{ m}$." "\n"
            r"- **Chống ô nhiễm tiếng ồn** (tiếng ồn lớn, kéo dài vượt ngưỡng $70\text{ dB} - 80\text{ dB}$): (1) Tác động vào nguồn âm (giảm độ to, cấm bóp còi gần bệnh viện, trường học); (2) Phân tán âm trên đường truyền (trồng nhiều cây xanh, xây tường chắn âm); (3) Ngăn chặn âm truyền tới tai (đóng cửa kính hai lớp, treo rèm nhung, đeo nút bịt tai)."
        ),
        "formulas": [
            G(
                "I. Tần số dao động âm",
                F("Công thức tính tần số", r"$f = \dfrac{N}{t} \iff N = f \cdot t$", r"$N$ là số dao động toàn phần, $t$ là thời gian thực hiện ($\text{s}$), $f$ tính bằng $\text{Hz}$."),
                F("Dải tần số tai người nghe được", r"$20\text{ Hz} \le f \le 20\,000\text{ Hz}$", r"Hạ âm: $f < 20\text{ Hz}$; Siêu âm: $f > 20\,000\text{ Hz}$."),
            ),
            G(
                "II. Phản xạ âm, Tiếng vang & Đo độ sâu Sonar",
                F("Khoảng cách từ nguồn âm đến vật chắn phản xạ", r"$2d = v \cdot t \iff d = \dfrac{v \cdot t}{2}$", r"Vì sóng âm phải đi từ nguồn tới vật chắn rồi phản xạ ngược về nơi thu (quãng đường $s = 2d$)."),
                F("Khoảng cách tối thiểu để nghe thấy tiếng vang trong không khí", r"$d_{\min} = \dfrac{v \cdot \dfrac{1}{15}}{2} = \dfrac{340}{30} \approx 11{,}33\text{ m}$", r"Khi $t \ge \dfrac{1}{15}\text{ s}$ và $v = 340\text{ m/s}$."),
            ),
        ],
        "example": (
            r"a) Một cánh ong mật đang bay vỗ cánh đều đặn $3300\text{ lần}$ trong thời gian $10\text{ s}$. Tính tần số dao động của cánh ong và cho biết tai người có nghe được âm do cánh ong phát ra không." "\n"
            r"b) Một tàu khảo sát phát một tín hiệu siêu âm thẳng đứng xuống đáy biển và thu được âm phản xạ sau $t = 1{,}2\text{ s}$. Biết tốc độ truyền siêu âm trong nước biển là $v = 1500\text{ m/s}$. Tính độ sâu $d$ của đáy biển tại vị trí đó."
        ),
        "example_answer": (
            r"a) Tần số dao động của cánh ong là: $f = \dfrac{N}{t} = \dfrac{3300}{10} = 330\text{ Hz}$." "\n"
            r"Vì $20\text{ Hz} \le 330\text{ Hz} \le 20\,000\text{ Hz}$ nên tai người **nghe được** tiếng vo ve của cánh ong." "\n"
            r"b) Trong thời gian $t = 1{,}2\text{ s}$, sóng siêu âm đã đi từ tàu xuống đáy biển rồi phản xạ ngược lên tàu (quãng đường $2d$), do đó độ sâu đáy biển là: $d = \dfrac{v \cdot t}{2} = \dfrac{1500 \cdot 1{,}2}{2} = 900\text{ m}$."
        ),
        "real_life": (
            r"- Trong các phòng thu âm, rạp chiếu phim và nhà hát, tường luôn được làm gồ ghề, ốp mút xốp và treo rèm nhung dày để hấp thụ âm, tránh tiếng vang làm nhoè âm thanh." "\n"
            r"- Loài dơi phát ra sóng siêu âm khi bay ban đêm và lắng nghe âm phản xạ để xác định khoảng cách tới vật cản và con mồi; tàu biển dùng máy **Sonar** để đo độ sâu đáy biển và dò đàn cá."
        ),
        "game_title": "Phòng thí nghiệm Sóng âm và Tiếng vang Sonar",
        "game_description": "Thay đổi biên độ và tần số dao động trên dao động kí để khảo sát độ to, độ cao của âm và ứng dụng phản xạ sóng siêu âm Sonar để đo độ sâu đáy biển.",
        "game_type": "game_amthanh",
        "quiz": [
            mcq(
                "biet",
                r"Sóng âm **không thể** truyền được trong môi trường nào sau đây?",
                [
                    r"Chân không.",
                    r"Chất khí (không khí).",
                    r"Chất lỏng (nước biển).",
                    r"Chất rắn (thanh thép, mặt đất).",
                ],
                0,
                r"Sóng âm là sự lan truyền dao động của các hạt vật chất nên **không truyền được trong chân không** (nơi không có các hạt vật chất).",
            ),
            mcq(
                "biet",
                r"Độ cao (bổng, trầm) của âm phụ thuộc vào yếu tố nào của nguồn âm?",
                [
                    r"Tần số dao động của nguồn âm.",
                    r"Biên độ dao động của nguồn âm.",
                    r"Thời gian nguồn âm phát ra âm dài hay ngắn.",
                    r"Nhiệt độ của môi trường truyền âm.",
                ],
                0,
                r"Tần số dao động càng lớn thì âm phát ra càng cao (bổng); tần số càng nhỏ thì âm càng thấp (trầm).",
            ),
            mcq(
                "biet",
                r"So sánh tốc độ truyền âm trong các môi trường chất rắn ($v_{\text{rắn}}$), chất lỏng ($v_{\text{lỏng}}$) và chất khí ($v_{\text{khí}}$), hệ thức nào sau đây là đúng?",
                [
                    r"$v_{\text{rắn}} > v_{\text{lỏng}} > v_{\text{khí}}$.",
                    r"$v_{\text{khí}} > v_{\text{lỏng}} > v_{\text{rắn}}$.",
                    r"$v_{\text{lỏng}} > v_{\text{rắn}} > v_{\text{khí}}$.",
                    r"$v_{\text{rắn}} = v_{\text{lỏng}} = v_{\text{khí}}$.",
                ],
                0,
                r"Tốc độ truyền âm trong chất rắn lớn hơn trong chất lỏng, và trong chất lỏng lớn hơn trong chất khí: $v_{\text{rắn}} > v_{\text{lỏng}} > v_{\text{khí}}$.",
            ),
            mcq(
                "biet",
                r"Vật nào sau đây là vật **phản xạ âm kém** (tức là hấp thụ âm tốt)?",
                [
                    r"Tấm rèm nhung dày và tấm mút xốp.",
                    r"Mặt gương phẳng bằng thuỷ tinh.",
                    r"Tường gạch phẳng trát xi măng nhẵn.",
                    r"Mặt sàn lát gạch đá hoa bóng.",
                ],
                0,
                r"Những vật mềm, xốp, có bề mặt gồ ghề như **rèm nhung dày, mút xốp, thảm len** phản xạ âm kém (hấp thụ âm tốt).",
            ),
            mcq(
                "hieu",
                r"Dây đàn thứ nhất thực hiện được $880\text{ dao động}$ trong $2\text{ s}$; dây đàn thứ hai thực hiện được $1500\text{ dao động}$ trong $3\text{ s}$. Kết luận nào sau đây là đúng?",
                [
                    r"Tần số của dây thứ nhất là $440\text{ Hz}$, dây thứ hai là $500\text{ Hz}$ nên dây thứ hai phát ra âm cao hơn.",
                    r"Tần số của dây thứ nhất là $440\text{ Hz}$, dây thứ hai là $500\text{ Hz}$ nên dây thứ nhất phát ra âm cao hơn.",
                    r"Dây thứ hai phát ra âm to hơn dây thứ nhất vì có tần số lớn hơn.",
                    r"Hai dây đàn phát ra hai âm có cùng độ cao.",
                ],
                0,
                r"Ta có $f_1 = \dfrac{880}{2} = 440\text{ Hz}$ và $f_2 = \dfrac{1500}{3} = 500\text{ Hz}$. Vì $f_2 > f_1$ nên dây đàn thứ hai phát ra âm **cao (bổng) hơn** dây thứ nhất.",
            ),
            mcq(
                "hieu",
                r"Một người đứng trước một vách núi đá lớn và hét to một tiếng, sau $0{,}5\text{ s}$ thì nghe thấy tiếng vang của chính mình vọng lại. Biết tốc độ truyền âm trong không khí là $340\text{ m/s}$. Khoảng cách từ người đó đến vách núi là:",
                [
                    r"$85\text{ m}$.",
                    r"$170\text{ m}$.",
                    r"$340\text{ m}$.",
                    r"$42{,}5\text{ m}$.",
                ],
                0,
                r"Trong thời gian $t = 0{,}5\text{ s}$, âm truyền từ người tới vách núi rồi phản xạ trở lại tai người (quãng đường $2d$). Vậy khoảng cách đến vách núi là $d = \dfrac{v \cdot t}{2} = \dfrac{340 \cdot 0{,}5}{2} = 85\text{ m}$.",
            ),
            tf4(
                "hieu",
                r"Khi gõ vào một chiếc trống da và khi gảy dây đàn ghi-ta trong phòng thực hành, ta khảo sát mối liên hệ giữa dao động và đặc trưng của âm. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Khi gõ mạnh vào mặt trống, mặt trống dao động với biên độ lớn hơn lúc gõ nhẹ nên phát ra âm to hơn.",
                    r"b) Khi gảy mạnh hơn vào cùng một dây đàn ở cùng một phím bấm, biên độ dao động tăng lên làm độ cao (tần số) của âm tăng gấp đôi.",
                    r"c) Tai người bình thường chỉ nghe được âm có tần số trong khoảng từ $20\text{ Hz}$ đến $20\,000\text{ Hz}$.",
                    r"d) Trên màn hình dao động kí, hai sóng âm có cùng khoảng cách giữa các đỉnh sóng nhưng sóng thứ nhất có đỉnh cao hơn sóng thứ hai thì âm thứ nhất to hơn và có cùng độ cao với âm thứ hai.",
                ],
                [True, False, True, True],
                r"a) Đúng vì gõ mạnh làm biên độ dao động của mặt trống lớn hơn nên âm to hơn." "\n"
                r"b) Sai vì gảy mạnh hơn trên cùng một dây đàn chỉ làm tăng biên độ (âm to hơn) chứ không làm thay đổi tần số (độ cao của âm không đổi)." "\n"
                r"c) Đúng theo giới hạn nghe của tai người ($20\text{ Hz} - 20\,000\text{ Hz}$)." "\n"
                r"d) Đúng vì đỉnh sóng cao hơn ứng với biên độ lớn hơn (âm to hơn), còn độ thưa hay dày của các đỉnh bằng nhau ứng với cùng tần số (cùng độ cao).",
            ),
            tf4(
                "hieu",
                r"Xét hiện tượng phản xạ âm và các biện pháp chống ô nhiễm tiếng ồn. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Trong không khí ở nhiệt độ thường ($v = 340\text{ m/s}$), để nghe thấy tiếng vang thì khoảng cách từ nguồn âm đến bức tường phản xạ phải tối thiểu khoảng $11{,}33\text{ m}$.",
                    r"b) Trong phòng học nhỏ có tường cách nhau $5\text{ m}$, khi thầy cô giảng bài không có âm phản xạ từ tường.",
                    r"c) Trồng nhiều cây xanh xung quanh trường học và bệnh viện giúp lá cây phản xạ âm theo nhiều hướng khác nhau, từ đó phân tán âm trên đường truyền và giảm tiếng ồn.",
                    r"d) Việc treo biển báo “Cấm bóp còi” ở gần cổng bệnh viện là biện pháp chống ô nhiễm tiếng ồn bằng cách tác động vào nguồn âm.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $d_{\min} = \dfrac{340 \cdot \dfrac{1}{15}}{2} \approx 11{,}33\text{ m}$." "\n"
                r"b) Sai vì trong phòng nhỏ vẫn luôn có âm phản xạ từ tường, nhưng do âm phản xạ đến tai gần như cùng lúc với âm trực tiếp (sớm hơn $\dfrac{1}{15}\text{ s}$) nên không tạo thành tiếng vang tách biệt mà chỉ làm âm nghe to hơn." "\n"
                r"c) Đúng vì tán lá cây làm phân tán sóng âm trên đường truyền." "\n"
                r"d) Đúng vì cấm bóp còi là ngăn chặn, hạn chế ngay tại nguồn phát âm.",
            ),
            mcq(
                "vandung",
                r"Một người gõ một nhát búa vào đầu một đường ray bằng thép dài $l = 306\text{ m}$. Một người khác áp tai vào đầu kia của đường ray thì nghe thấy hai tiếng gõ cách nhau một khoảng thời gian $\Delta t$. Biết tốc độ truyền âm trong không khí là $v_1 = 340\text{ m/s}$ và trong thép là $v_2 = 6120\text{ m/s}$. Giá trị của $\Delta t$ là:",
                [
                    r"$0{,}85\text{ s}$.",
                    r"$0{,}90\text{ s}$.",
                    r"$0{,}95\text{ s}$.",
                    r"$0{,}05\text{ s}$.",
                ],
                0,
                r"Thời gian âm truyền trong thanh thép là $t_2 = \dfrac{l}{v_2} = \dfrac{306}{6120} = 0{,}05\text{ s}$ (đến tai trước). Thời gian âm truyền trong không khí là $t_1 = \dfrac{l}{v_1} = \dfrac{306}{340} = 0{,}90\text{ s}$ (đến tai sau). Khoảng thời gian giữa hai tiếng gõ nghe được là $\Delta t = t_1 - t_2 = 0{,}90 - 0{,}05 = 0{,}85\text{ s}$.",
            ),
            short(
                "vandung",
                r"Một tàu nghiên cứu biển sử dụng thiết bị Sonar phát một xung siêu âm thẳng đứng xuống đáy biển và thu được tín hiệu phản xạ sau thời gian $t = 0{,}8\text{ s}$. Biết tốc độ truyền siêu âm trong nước biển là $v = 1500\text{ m/s}$. Độ sâu của đáy biển tại nơi đó là bao nhiêu mét?",
                ["600", "600,0", "600.0"],
                r"Quãng đường sóng siêu âm đi xuống đáy biển và phản xạ ngược lên tàu là $2d = v \cdot t$. Suy ra độ sâu đáy biển là $d = \dfrac{1500 \cdot 0{,}8}{2} = 600\text{ m}$.",
            ),
        ],
    },
    {
        "topic": "anh-sang",
        "title": "Năng lượng ánh sáng, Tia sáng, Vùng tối và Sự phản xạ ánh sáng",
        "icon": "☀️",
        "description": "Chương V · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (tr. 73–81): Bài 15 – Bài 16. Ánh sáng là một dạng năng lượng; tia sáng, chùm sáng song song, hội tụ, phân kì; vùng tối và vùng nửa tối, giải thích hiện tượng nhật thực và nguyệt thực; định luật phản xạ ánh sáng, phân biệt phản xạ gương và phản xạ khuếch tán.",
        "requirements": [
            r"Thực hiện được thí nghiệm thu năng lượng ánh sáng (dùng pin mặt trời hoặc kính lúp hội tụ ánh sáng) để chứng tỏ ánh sáng là một dạng năng lượng.",
            r"Biểu diễn được đường truyền của ánh sáng bằng tia sáng (đường thẳng có mũi tên chỉ hướng) và phân biệt được ba loại chùm sáng: song song, hội tụ, phân kì.",
            r"Vẽ được hình biểu diễn và giải thích được sự tạo thành vùng tối (bóng tối) do nguồn sáng hẹp và vùng nửa tối (bóng nửa tối) do nguồn sáng rộng phía sau vật cản sáng.",
            r"Thực hiện được thí nghiệm rút ra Định luật phản xạ ánh sáng; xác định được tia tới, tia phản xạ, pháp tuyến, góc tới $i$, góc phản xạ $i'$ và vận dụng hệ thức $i' = i$ để giải bài tập quang hình.",
            r"Phân biệt được sự phản xạ (phản xạ gương trên bề mặt nhẵn bóng) và sự phản xạ khuếch tán (tán xạ trên bề mặt gồ ghề).",
        ],
        "definition": (
            r"- **Ánh sáng** là một dạng năng lượng (quang năng). Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo **đường thẳng**, được biểu diễn bằng một đường thẳng có mũi tên chỉ hướng truyền gọi là **tia sáng**." "\n"
            r"- **Vùng tối** là vùng nằm phía sau vật cản sáng, hoàn toàn **không nhận được** ánh sáng từ nguồn sáng truyền tới. **Vùng nửa tối** là vùng nằm phía sau vật cản sáng, nhận được ánh sáng từ **một phần** của nguồn sáng rộng truyền tới." "\n"
            r"- **Định luật phản xạ ánh sáng**: (1) Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến của gương ở điểm tới; (2) Góc phản xạ luôn bằng góc tới ($i' = i$)."
        ),
        "theory": (
            r"### Bài 15. Năng lượng ánh sáng. Tia sáng, vùng tối" "\n"
            r"- **Năng lượng ánh sáng**: Có thể chuyển hoá thành điện năng (trong pin quang điện mặt trời), thành nhiệt năng (làm nóng nước, đun bếp mặt trời) và hoá năng (trong quá trình quang hợp của cây xanh)." "\n"
            r"- **Ba loại chùm sáng**:" "\n"
            r"  + **Chùm sáng song song**: Các tia sáng không giao nhau trên đường truyền của chúng." "\n"
            r"  + **Chùm sáng hội tụ**: Các tia sáng giao nhau (chụm lại) tại một điểm trên đường truyền." "\n"
            r"  + **Chùm sáng phân kì**: Các tia sáng loe rộng ra trên đường truyền." "\n"
            r"- **Vùng tối và vùng nửa tối**: Khi chiếu sáng một vật cản mờ đục bằng **nguồn sáng hẹp** (như đèn LED nhỏ), phía sau vật chỉ có vùng tối sắc nét; khi chiếu bằng **nguồn sáng rộng** (như bóng đèn huỳnh quang dài hoặc Mặt Trời), phía sau vật có vùng tối ở giữa và vùng nửa tối bao quanh. Đây là cơ sở giải thích hiện tượng **nhật thực** (Mặt Trăng chắn giữa Mặt Trời và Trái Đất) và **nguyệt thực** (Trái Đất chắn giữa Mặt Trời và Mặt Trăng)." "\n"
            r"### Bài 16. Sự phản xạ ánh sáng" "\n"
            r"- **Các khái niệm tại điểm tới $I$ trên gương phẳng $G$**:" "\n"
            r"  + $SI$: tia tới; $IR$: tia phản xạ; $IN \perp G$: đường pháp tuyến tại điểm tới $I$." "\n"
            r"  + **Góc tới $i = \widehat{SIN}$** là góc hợp bởi tia tới $SI$ và pháp tuyến $IN$." "\n"
            r"  + **Góc phản xạ $i' = \widehat{NIR}$** là góc hợp bởi tia phản xạ $IR$ và pháp tuyến $IN$." "\n"
            r"- **Lưu ý quan trọng**: Nếu đề bài cho góc hợp bởi tia tới $SI$ và mặt gương là $\alpha$ thì vì pháp tuyến $IN$ vuông góc với mặt gương ($\alpha + i = 90^\circ$) nên góc tới là $i = 90^\circ - \alpha$." "\n"
            r"- **Phản xạ và phản xạ khuếch tán**: Khi chùm sáng song song chiếu tới bề mặt **nhẵn bóng** (gương, mặt nước phẳng lặng), các tia phản xạ vẫn song song theo một hướng (nhìn thấy ảnh của vật — gọi là **phản xạ gương**); khi chiếu tới bề mặt **không nhẵn (gồ ghề)** (trang giấy, mặt tường, mặt nước gợn sóng), các tia phản xạ bị hắt lại theo mọi hướng khác nhau (không nhìn thấy ảnh — gọi là **phản xạ khuếch tán**)."
        ),
        "formulas": [
            G(
                "I. Định luật phản xạ ánh sáng",
                F("Hệ thức góc phản xạ và góc tới", r"$i' = i$", r"$i = \widehat{SIN}$ là góc tới, $i' = \widehat{NIR}$ là góc phản xạ (tính so với pháp tuyến $IN$)."),
                F("Góc tới khi biết góc hợp bởi tia tới và mặt gương", r"$i = 90^\circ - \alpha \iff \alpha + i = 90^\circ$", r"$\alpha$ là góc tạo bởi tia tới $SI$ và mặt gương phẳng."),
                F("Góc hợp bởi tia tới và tia phản xạ", r"$\widehat{SIR} = i + i' = 2i$", r"Pháp tuyến $IN$ là tia phân giác của góc $\widehat{SIR}$."),
            ),
            G(
                "II. Trường hợp đặc biệt & Quay gương",
                F("Tia tới vuông góc với mặt gương", r"$\alpha = 90^\circ \Rightarrow i = 0^\circ \Rightarrow i' = 0^\circ$", r"Tia phản xạ truyền ngược lại trùng với đường truyền của tia tới."),
                F("Góc quay của tia phản xạ khi giữ tia tới cố định và quay gương góc beta", r"$\Delta \varphi = 2\beta$", r"Khi gương phẳng quay đi một góc $\beta$ thì tia phản xạ quay đi một góc $2\beta$."),
            ),
        ],
        "example": (
            r"Chiếu một tia sáng $SI$ tới một gương phẳng sao cho tia tới $SI$ hợp với mặt gương một góc $\alpha = 35^\circ$. Hãy tính góc tới $i$, góc phản xạ $i'$ và góc $\widehat{SIR}$ hợp bởi tia tới và tia phản xạ."
        ),
        "example_answer": (
            r"- Vì pháp tuyến $IN$ vuông góc với mặt gương tại điểm tới $I$ nên góc tới $i$ phụ với góc $\alpha$: $i = 90^\circ - \alpha = 90^\circ - 35^\circ = 55^\circ$." "\n"
            r"- Theo định luật phản xạ ánh sáng, góc phản xạ bằng góc tới: $i' = i = 55^\circ$." "\n"
            r"- Góc hợp bởi tia tới và tia phản xạ là: $\widehat{SIR} = i + i' = 55^\circ + 55^\circ = 110^\circ$."
        ),
        "real_life": (
            r"- Ở những chỗ ngồi trên Trái Đất nằm trong **vùng tối** của Mặt Trăng sẽ quan sát thấy **nhật thực toàn phần**; những nơi nằm trong **vùng nửa tối** của Mặt Trăng sẽ quan sát thấy **nhật thực một phần**." "\n"
            r"- Trang giấy sách giáo khoa được làm có độ nhám vi mô để tạo phản xạ khuếch tán giúp mắt đọc chữ từ mọi góc nhìn mà không bị chói loá như giấy bóng gương."
        ),
        "game_title": "Thí nghiệm Quang hình: Vùng tối và Định luật Phản xạ ánh sáng",
        "game_description": "Điều chỉnh góc tới của tia laser chiếu vào gương phẳng để kiểm chứng định luật phản xạ ánh sáng và quan sát sự tạo thành vùng tối, vùng nửa tối.",
        "game_type": "game_anhsang",
        "quiz": [
            mcq(
                "biet",
                r"Quy ước biểu diễn một **tia sáng** trong quang học là:",
                [
                    r"Một đường thẳng có mũi tên chỉ hướng truyền của ánh sáng.",
                    r"Một đường cong bất kì không có mũi tên.",
                    r"Một đường gấp khúc nối từ mắt người tới nguồn sáng.",
                    r"Một đoạn thẳng nét đứt không có hướng.",
                ],
                0,
                r"Đường truyền của ánh sáng được biểu diễn bằng một **đường thẳng có mũi tên chỉ hướng**, gọi là **tia sáng**.",
            ),
            mcq(
                "biet",
                r"Theo Định luật phản xạ ánh sáng, mối quan hệ giữa góc phản xạ $i'$ và góc tới $i$ là:",
                [
                    r"$i' = i$.",
                    r"$i' = 2i$.",
                    r"$i' = 90^\circ - i$.",
                    r"$i' + i = 180^\circ$.",
                ],
                0,
                r"Định luật phản xạ ánh sáng khẳng định: góc phản xạ luôn bằng góc tới ($i' = i$).",
            ),
            mcq(
                "biet",
                r"Khi chiếu một chùm sáng song song tới một bề mặt nhẵn bóng (như mặt gương phẳng hoặc mặt hồ nước phẳng lặng), hiện tượng các tia sáng bị hắt trở lại theo cùng một hướng xác định được gọi là:",
                [
                    r"Sự phản xạ (phản xạ gương).",
                    r"Sự phản xạ khuếch tán (tán xạ).",
                    r"Sự khúc xạ ánh sáng.",
                    r"Sự phân tích ánh sáng.",
                ],
                0,
                r"Trên bề mặt nhẵn bóng, chùm tia tới song song cho chùm tia phản xạ song song theo một hướng xác định, gọi là **sự phản xạ (phản xạ gương)**.",
            ),
            mcq(
                "biet",
                r"Hiện tượng **nhật thực** xảy ra vào ban ngày khi vị trí của Mặt Trời, Trái Đất và Mặt Trăng như thế nào?",
                [
                    r"Ba thiên thể thẳng hàng và Mặt Trăng nằm ở khoảng giữa Mặt Trời và Trái Đất, che khuất ánh sáng Mặt Trời chiếu xuống Trái Đất.",
                    r"Ba thiên thể thẳng hàng và Trái Đất nằm ở khoảng giữa Mặt Trời và Mặt Trăng.",
                    r"Ba thiên thể thẳng hàng và Mặt Trời nằm ở khoảng giữa Trái Đất và Mặt Trăng.",
                    r"Mặt Trăng tự phát sáng mạnh hơn Mặt Trời vào ban đêm.",
                ],
                0,
                r"Nhật thực xảy ra khi Mặt Trăng đi vào giữa Mặt Trời và Trái Đất trên cùng một đường thẳng, tạo ra vùng tối và vùng nửa tối trên bề mặt Trái Đất.",
            ),
            mcq(
                "hieu",
                r"Chiếu một tia sáng tới mặt một gương phẳng sao cho tia tới hợp với mặt gương một góc $30^\circ$. Giá trị của góc phản xạ $i'$ là:",
                [
                    r"$60^\circ$.",
                    r"$30^\circ$.",
                    r"$120^\circ$.",
                    r"$45^\circ$.",
                ],
                0,
                r"Góc hợp bởi tia tới và mặt gương là $\alpha = 30^\circ$, nên góc tới (hợp với pháp tuyến vuông góc mặt gương) là $i = 90^\circ - 30^\circ = 60^\circ$. Theo định luật phản xạ ánh sáng, góc phản xạ là $i' = i = 60^\circ$.",
            ),
            mcq(
                "hieu",
                r"Chiếu một tia sáng tới gương phẳng sao cho góc hợp bởi tia tới và tia phản xạ bằng $80^\circ$. Góc tới $i$ và góc hợp bởi tia tới với mặt gương $\alpha$ lần lượt là:",
                [
                    r"$i = 40^\circ$ và $\alpha = 50^\circ$.",
                    r"$i = 80^\circ$ và $\alpha = 10^\circ$.",
                    r"$i = 40^\circ$ và $\alpha = 40^\circ$.",
                    r"$i = 50^\circ$ và $\alpha = 40^\circ$.",
                ],
                0,
                r"Vì $i + i' = 80^\circ$ và $i' = i$ nên $2i = 80^\circ \Rightarrow i = 40^\circ$. Góc hợp bởi tia tới và mặt gương là $\alpha = 90^\circ - i = 90^\circ - 40^\circ = 50^\circ$.",
            ),
            tf4(
                "hieu",
                r"Xét các tính chất của năng lượng ánh sáng, chùm sáng và sự tạo thành vùng tối, vùng nửa tối. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Pin mặt trời sử dụng trên mái nhà hoặc trong máy tính bỏ túi hoạt động dựa trên sự chuyển hoá trực tiếp năng lượng ánh sáng thành điện năng.",
                    r"b) Chùm sáng phát ra từ bút chiếu tia laser được coi là mô hình thực tế của một chùm sáng song song.",
                    r"c) Vùng nửa tối phía sau vật cản sáng là vùng hoàn toàn không nhận được bất kì tia sáng nào từ nguồn sáng rộng.",
                    r"d) Trong phòng mổ bệnh viện, người ta dùng đèn mổ gồm rất nhiều bóng đèn nhỏ ghép thành một nguồn sáng rộng để tránh tạo vùng tối đậm dưới bàn tay của bác sĩ phẫu thuật.",
                ],
                [True, True, False, True],
                r"a) Đúng vì pin quang điện mặt trời biến quang năng thành điện năng." "\n"
                r"b) Đúng vì tia laser có độ chuẩn trực rất cao, tạo chùm sáng mảnh gần như song song." "\n"
                r"c) Sai vì vùng nửa tối vẫn nhận được ánh sáng từ **một phần** của nguồn sáng rộng truyền tới; chỉ có vùng tối mới hoàn toàn không nhận được ánh sáng." "\n"
                r"d) Đúng vì khi bàn tay bác sĩ che một số bóng đèn thì các bóng đèn ở vị trí khác trong cụm đèn mổ vẫn chiếu sáng được vùng phẫu thuật.",
            ),
            tf4(
                "hieu",
                r"Chiếu một tia sáng $SI$ tới điểm $I$ trên một gương phẳng $G$, với $IN$ là pháp tuyến tại $I$ và $IR$ là tia phản xạ. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Tia phản xạ $IR$ luôn nằm trong cùng một mặt phẳng với tia tới $SI$ và pháp tuyến $IN$.",
                    r"b) Nếu chiếu tia tới $SI$ vuông góc với mặt gương phẳng thì góc tới bằng $90^\circ$ và góc phản xạ bằng $90^\circ$.",
                    r"c) Khi mặt hồ nước phẳng lặng ta thấy ảnh rõ nét của hàng cây ven hồ là do phản xạ gương; khi có gió thổi làm mặt nước gợn sóng ta không nhìn rõ ảnh nữa là do phản xạ khuếch tán.",
                    r"d) Nếu tia tới hợp với pháp tuyến một góc $25^\circ$ thì góc hợp bởi tia phản xạ và mặt gương là $65^\circ$.",
                ],
                [True, False, True, True],
                r"a) Đúng theo nội dung thứ nhất của định luật phản xạ ánh sáng." "\n"
                r"b) Sai vì khi tia tới vuông góc với mặt gương thì tia tới trùng với pháp tuyến $IN$, do đó góc tới $i = 0^\circ$ và góc phản xạ $i' = 0^\circ$." "\n"
                r"c) Đúng vì mặt nước phẳng lặng phản xạ gương, còn mặt nước gợn sóng làm các tia phản xạ tán xạ theo nhiều hướng khác nhau." "\n"
                r"d) Đúng vì $i = 25^\circ \Rightarrow i' = 25^\circ$, suy ra góc giữa tia phản xạ và mặt gương là $90^\circ - 25^\circ = 65^\circ$.",
            ),
            mcq(
                "vandung",
                r"Một tia sáng Mặt Trời chiếu xiên từ trên xuống hợp với phương nằm ngang một góc $\varphi = 40^\circ$. Để hắt tia sáng đó truyền thẳng đứng từ trên xuống dưới vào đáy một cái giếng sâu, người ta cần đặt một gương phẳng nghiêng một góc bao nhiêu độ so với phương nằm ngang?",
                [
                    r"$65^\circ$.",
                    r"$25^\circ$.",
                    r"$50^\circ$.",
                    r"$45^\circ$.",
                ],
                0,
                r"Tia tới hợp với phương ngang góc $40^\circ$, tia phản xạ hướng thẳng đứng xuống dưới (hợp với phương ngang góc $90^\circ$) nên góc hợp bởi tia tới và tia phản xạ là $\widehat{SIR} = 40^\circ + 90^\circ = 130^\circ$. Suy ra góc tới $i = \dfrac{130^\circ}{2} = 65^\circ$, và góc giữa mặt gương với tia phản xạ (phương thẳng đứng) là $\alpha = 90^\circ - 65^\circ = 25^\circ$. Vậy mặt gương hợp với phương nằm ngang một góc $90^\circ - 25^\circ = 65^\circ$.",
            ),
            short(
                "vandung",
                r"Chiếu một tia sáng $SI$ tới một gương phẳng sao cho góc hợp bởi tia tới và mặt gương bằng một nửa góc tới ($\alpha = \dfrac{1}{2}i$). Hãy tính số đo góc hợp bởi tia tới và tia phản xạ $\widehat{SIR}$ theo đơn vị độ ($^\circ$).",
                ["120", "120,0", "120.0"],
                r"Ta có $\alpha + i = 90^\circ$. Thay $\alpha = \dfrac{1}{2}i$ vào được $\dfrac{3}{2}i = 90^\circ \Rightarrow i = 60^\circ$. Góc hợp bởi tia tới và tia phản xạ là $\widehat{SIR} = 2i = 2 \cdot 60^\circ = 120^\circ$.",
            ),
        ],
    },
    {
        "topic": "guong-phang",
        "title": "Ảnh của vật qua gương phẳng",
        "icon": "🪞",
        "description": "Chương V · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (tr. 82–85): Bài 17. Tính chất của ảnh tạo bởi gương phẳng (ảnh ảo, độ lớn của ảnh bằng độ lớn của vật, khoảng cách từ ảnh đến gương bằng khoảng cách từ vật đến gương); hai cách dựng ảnh của vật qua gương phẳng và các ứng dụng trong đời sống.",
        "requirements": [
            r"Thực hiện được thí nghiệm với tấm kính phẳng trong suốt và hai cây nến giống nhau để nêu được các tính chất của ảnh tạo bởi gương phẳng.",
            r"Nêu được ảnh của vật qua gương phẳng là ảnh ảo (không hứng được trên màn chắn), có độ lớn bằng vật và khoảng cách từ một điểm của vật đến gương phẳng bằng khoảng cách từ ảnh của điểm đó đến gương ($d' = d$).",
            r"Vẽ được ảnh của một điểm sáng và của một vật phẳng đặt trước gương phẳng bằng hai cách: dựa vào định luật phản xạ ánh sáng và dựa vào tính chất đối xứng của ảnh qua gương.",
            r"Vận dụng được kiến thức về gương phẳng để giải thích nguyên tắc cấu tạo kính tiềm vọng và các ứng dụng của gương phẳng trong đời sống.",
        ],
        "definition": (
            r"- **Tính chất ảnh của vật tạo bởi gương phẳng**:" "\n"
            r"  1. Ảnh của vật tạo bởi gương phẳng là **ảnh ảo**, không hứng được trên màn chắn nhưng mắt nhìn thấy được." "\n"
            r"  2. Độ lớn của ảnh **bằng** độ lớn của vật ($h' = h$)." "\n"
            r"  3. Điểm sáng và ảnh của nó tạo bởi gương phẳng nằm **đối xứng** với nhau qua mặt gương: khoảng cách từ một điểm của vật đến gương phẳng bằng khoảng cách từ ảnh của điểm đó đến gương ($d' = d$)."
        ),
        "theory": (
            r"### Bài 17. Ảnh của vật qua gương phẳng" "\n"
            r"- **Vì sao mắt nhìn thấy ảnh ảo $S'$ của điểm sáng $S$?**: Các tia sáng xuất phát từ điểm sáng $S$ tới gương phẳng bị phản xạ theo định luật phản xạ ánh sáng. Khi chùm tia phản xạ lọt vào mắt, **đường kéo dài về phía sau gương** của các tia phản xạ này cắt nhau tại một điểm $S'$; mắt ta có cảm giác như các tia sáng xuất phát trực tiếp từ $S'$, nên $S'$ là ảnh ảo của $S$." "\n"
            r"- **Hai cách dựng ảnh của vật qua gương phẳng**:" "\n"
            r"  + *Cách 1 (Dựa vào định luật phản xạ ánh sáng)*: Từ điểm sáng $S$, vẽ hai tia tới $SI_1, SI_2$ bất kì tới gương, dùng pháp tuyến vẽ hai tia phản xạ $I_1 R_1, I_2 R_2$ tương ứng ($i' = i$); kéo dài hai tia phản xạ về phía sau gương bằng **nét đứt**, giao điểm $S'$ chính là ảnh ảo của $S$." "\n"
            r"  + *Cách 2 (Dựa vào tính chất đối xứng — thường dùng nhất)*: Từ các điểm đầu mút $A, B$ của vật sáng $AB$, hạ các đường vuông góc xuống mặt gương tại $H, K$ rồi kéo dài về phía sau gương lấy $HA' = HA$, $KB' = KB$. Nối $A'B'$ bằng **nét đứt** (vì là ảnh ảo), ta được ảnh $A'B'$ của vật $AB$." "\n"
            r"- **Các tư thế đặt vật trước gương phẳng**:" "\n"
            r"  + Vật đặt **song song** với gương phẳng $\Rightarrow$ ảnh song song, **cùng chiều** và bằng vật." "\n"
            r"  + Vật đặt **vuông góc** với gương phẳng $\Rightarrow$ ảnh vuông góc với gương, **ngược chiều** với vật và bằng vật." "\n"
            r"- **Ứng dụng**: Gương soi trong gia đình, gương chiếu hậu phẳng, gương trang trí tạo cảm giác phòng rộng gấp đôi, **kính tiềm vọng** (gồm hai gương phẳng đặt song song nhau và nghiêng góc $45^\circ$ so với phương ngang và phương thẳng đứng để quan sát vượt qua chướng ngại vật)."
        ),
        "formulas": [
            G(
                "I. Hệ thức kích thước và khoảng cách qua gương phẳng",
                F("Chiều cao (độ lớn) của ảnh", r"$h' = h \iff A'B' = AB$", r"Độ lớn của ảnh ảo qua gương phẳng luôn bằng vật, không phụ thuộc khoảng cách tới gương."),
                F("Khoảng cách từ ảnh đến gương", r"$d' = d \iff S'H = SH$", r"$d$ là khoảng cách từ vật đến gương, $d'$ là khoảng cách từ ảnh đến gương."),
                F("Khoảng cách giữa vật và ảnh của nó", r"$L = d + d' = 2d$", r"Khi vật tiến lại gần gương một đoạn $\Delta d$ thì khoảng cách giữa vật và ảnh giảm đi $2\Delta d$."),
            ),
            G(
                "II. Hệ hai gương trong kính tiềm vọng",
                F("Góc nghiêng của hai gương phẳng trong kính tiềm vọng", r"$\alpha_1 = \alpha_2 = 45^\circ$", r"Mỗi gương làm tia sáng đổi phương một góc $90^\circ$ ($i = i' = 45^\circ$)."),
            ),
        ],
        "example": (
            r"Một bạn học sinh cao $h = 1{,}55\text{ m}$ đứng trước một chiếc gương phẳng treo thẳng đứng trên tường và cách mặt gương một khoảng $d_1 = 2{,}0\text{ m}$." "\n"
            r"a) Tính chiều cao ảnh của bạn đó trong gương và khoảng cách từ bạn đó đến ảnh của mình." "\n"
            r"b) Nếu bạn đó bước tiến lại gần gương một đoạn $\Delta d = 0{,}6\text{ m}$ theo phương vuông góc với mặt gương thì chiều cao của ảnh và khoảng cách giữa bạn đó với ảnh lúc này là bao nhiêu?"
        ),
        "example_answer": (
            r"a) Chiều cao của ảnh trong gương phẳng luôn bằng chiều cao của vật: $h' = h = 1{,}55\text{ m}$." "\n"
            r"Khoảng cách từ ảnh đến gương là $d_1' = d_1 = 2{,}0\text{ m}$, nên khoảng cách từ bạn đó đến ảnh của mình là: $L_1 = 2d_1 = 2 \cdot 2{,}0 = 4{,}0\text{ m}$." "\n"
            r"b) Khi bạn bước lại gần gương $0{,}6\text{ m}$, chiều cao của ảnh **không thay đổi**, vẫn bằng $h' = 1{,}55\text{ m}$." "\n"
            r"Khoảng cách mới từ bạn đến gương là $d_2 = 2{,}0 - 0{,}6 = 1{,}4\text{ m}$, nên khoảng cách giữa bạn và ảnh lúc này là: $L_2 = 2d_2 = 2 \cdot 1{,}4 = 2{,}8\text{ m}$ (giảm đi $2 \cdot 0{,}6 = 1{,}2\text{ m}$)."
        ),
        "real_life": (
            r"- Tại các phòng khám mắt có diện tích hẹp (ví dụ chỉ dài $2{,}5\text{ m}$), bác sĩ đặt bảng thử thị lực ở ngay phía sau lưng bệnh nhân và treo một gương phẳng ở bức tường đối diện cách bệnh nhân $2{,}5\text{ m}$; khi đó ảnh của bảng thị lực trong gương sẽ cách mắt bệnh nhân $5{,}0\text{ m}$ đúng chuẩn đo thị lực." "\n"
            r"- Trên mũi các xe cứu thương (Ambulance), dòng chữ `AMBULANCE` thường được in ngược trái – phải (`ECNALUBMA`) để người lái xe phía trước khi nhìn qua gương chiếu hậu phẳng sẽ đọc được chữ xuôi."
        ),
        "game_title": "Dựng ảnh qua Gương phẳng và Kính tiềm vọng",
        "game_description": "Thực hành dựng ảnh ảo của vật qua gương phẳng theo tính chất đối xứng và lắp đặt hệ hai gương phẳng song song trong kính tiềm vọng.",
        "game_type": "game_guongphang",
        "quiz": [
            mcq(
                "biet",
                r"Ảnh của một vật tạo bởi gương phẳng có tính chất nào sau đây?",
                [
                    r"Là ảnh ảo, không hứng được trên màn chắn và có độ lớn bằng vật.",
                    r"Là ảnh thật, hứng được trên màn chắn và có độ lớn bằng vật.",
                    r"Là ảnh ảo và luôn lớn hơn vật khi đưa vật lại gần gương.",
                    r"Là ảnh ảo và luôn nhỏ hơn vật khi đưa vật ra xa gương.",
                ],
                0,
                r"Ảnh của vật tạo bởi gương phẳng luôn là **ảnh ảo**, không hứng được trên màn chắn và **có độ lớn bằng vật**.",
            ),
            mcq(
                "biet",
                r"Mối quan hệ giữa khoảng cách $d$ từ một điểm sáng $S$ đến gương phẳng và khoảng cách $d'$ từ ảnh $S'$ của nó đến gương phẳng là:",
                [
                    r"$d' = d$.",
                    r"$d' = 2d$.",
                    r"$d' = \dfrac{1}{2}d$.",
                    r"$d' = d^2$.",
                ],
                0,
                r"Điểm sáng $S$ và ảnh ảo $S'$ đối xứng nhau qua mặt gương phẳng nên khoảng cách từ ảnh đến gương bằng khoảng cách từ vật đến gương ($d' = d$).",
            ),
            mcq(
                "biet",
                r"Khi vẽ hình biểu diễn ảnh ảo $A'B'$ của vật sáng $AB$ và phần kéo dài của các tia phản xạ ở phía sau mặt gương phẳng, ta phải dùng kí hiệu nét vẽ nào?",
                [
                    r"Nét đứt.",
                    r"Nét liền đậm có mũi tên.",
                    r"Đường lượn sóng.",
                    r"Đường gạch chéo.",
                ],
                0,
                r"Vì ở phía sau gương phẳng không có ánh sáng truyền tới thật sự (chỉ là đường kéo dài tưởng tượng và ảnh ảo) nên trên hình vẽ quy ước vẽ bằng **nét đứt**.",
            ),
            mcq(
                "biet",
                r"Trong một chiếc **kính tiềm vọng** đơn giản dùng trên tàu ngầm, người ta lắp hai chiếc gương phẳng ở hai đầu ống theo cách nào?",
                [
                    r"Hai mặt gương quay vào nhau, đặt song song với nhau và nghiêng một góc $45^\circ$ so với trục ống.",
                    r"Hai mặt gương đặt vuông góc với nhau và vuông góc với trục ống.",
                    r"Hai mặt gương úp lưng vào nhau ở chính giữa ống.",
                    r"Một gương phẳng đặt nằm ngang và một tấm bìa đen đặt thẳng đứng.",
                ],
                0,
                r"Trong kính tiềm vọng, hai gương phẳng đặt **song song với nhau**, mặt phản xạ quay vào nhau và nghiêng góc $45^\circ$ so với phương ngang hoặc trục ống để phản xạ tia sáng hai lần góc $90^\circ$ đưa vào mắt.",
            ),
            mcq(
                "hieu",
                r"Đặt một điểm sáng $S$ trước một gương phẳng và cách mặt gương một khoảng $18\text{ cm}$. Khoảng cách giữa điểm sáng $S$ và ảnh ảo $S'$ của nó tạo bởi gương là:",
                [
                    r"$36\text{ cm}$.",
                    r"$18\text{ cm}$.",
                    r"$9\text{ cm}$.",
                    r"$54\text{ cm}$.",
                ],
                0,
                r"Ảnh $S'$ nằm sau gương và cách gương $d' = d = 18\text{ cm}$. Vậy khoảng cách giữa điểm sáng $S$ và ảnh $S'$ là $SS' = d + d' = 18 + 18 = 36\text{ cm}$.",
            ),
            mcq(
                "hieu",
                r"Đặt một chiếc bút chì $AB$ dài $12\text{ cm}$ trước một gương phẳng. Nếu ta dịch chuyển chiếc bút chì ra xa gương thêm một đoạn $20\text{ cm}$ thì độ dài ảnh $A'B'$ của chiếc bút chì trong gương sẽ:",
                [
                    r"Không thay đổi và vẫn bằng $12\text{ cm}$.",
                    r"Nhỏ đi chỉ còn $6\text{ cm}$.",
                    r"Tăng lên thành $32\text{ cm}$.",
                    r"Giảm đi còn $8\text{ cm}$.",
                ],
                0,
                r"Độ lớn của ảnh tạo bởi gương phẳng **luôn bằng độ lớn của vật** ($A'B' = AB = 12\text{ cm}$) và không phụ thuộc vào khoảng cách từ vật tới gương (khi ra xa chỉ là góc nhìn của mắt nhỏ đi làm ta có cảm giác ảnh nhỏ đi).",
            ),
            tf4(
                "hieu",
                r"Đặt một vật sáng hình mũi tên $AB$ trước một gương phẳng $G$. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Nếu đặt mũi tên $AB$ song song với mặt gương phẳng thì ảnh ảo $A'B'$ cũng song song với gương và cùng chiều với vật $AB$.",
                    r"b) Nếu đặt mũi tên $AB$ vuông góc với mặt gương phẳng (đầu $B$ hướng vào gương) thì ảnh ảo $A'B'$ vuông góc với gương và cùng chiều với vật $AB$.",
                    r"c) Ta nhìn thấy ảnh ảo $S'$ trong gương phẳng là vì có các tia sáng thực sự đi xuyên qua mặt gương hội tụ tại $S'$ rồi truyền ngược lại mắt.",
                    r"d) Nếu đặt một tấm bìa cứng ở phía sau gương phẳng tại đúng vị trí của ảnh $A'B'$ thì trên tấm bìa không thu được hình ảnh nào của vật $AB$.",
                ],
                [True, False, False, True],
                r"a) Đúng vì khi $AB \parallel G$ thì $AA' = BB'$ nên $A'B' \parallel AB$ và cùng chiều." "\n"
                r"b) Sai vì khi đặt $AB \perp G$ (đầu $B$ gần gương hơn đầu $A$) thì ảnh $B'$ cũng gần gương hơn $A'$, làm mũi tên ảnh $A'B'$ hướng **ngược chiều** với mũi tên vật $AB$." "\n"
                r"c) Sai vì ánh sáng không đi xuyên ra sau gương; mắt nhìn thấy $S'$ là do chùm tia phản xạ trước gương truyền vào mắt có đường kéo dài cắt nhau tại $S'$." "\n"
                r"d) Đúng vì ảnh qua gương phẳng là ảnh ảo, không hứng được trên màn chắn.",
            ),
            tf4(
                "hieu",
                r"Xét các bài toán khoảng cách và chuyển động của vật trước gương phẳng. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Một người đứng cách gương phẳng $1{,}2\text{ m}$ thì ảnh của người đó cách người đó $2{,}4\text{ m}$.",
                    r"b) Nếu người đó lùi ra xa gương thêm $0{,}5\text{ m}$ theo phương vuông góc với gương thì khoảng cách giữa người đó và ảnh tăng thêm $0{,}5\text{ m}$.",
                    r"c) Một chiếc đồng hồ kim không có số chỉ giờ đang chỉ $3\text{ giờ } 00\text{ phút}$; khi nhìn ảnh của mặt đồng hồ đó trong gương phẳng treo đối diện thì ảnh sẽ giống như đang chỉ $9\text{ giờ } 00\text{ phút}$.",
                    r"d) Trong kính tiềm vọng có hai gương phẳng đặt song song và nghiêng $45^\circ$, tia sáng đi từ vật qua hai lần phản xạ liên tiếp sẽ giữ nguyên phương ban đầu để đi vào mắt người quan sát.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $L = 2d = 2 \cdot 1{,}2 = 2{,}4\text{ m}$." "\n"
                r"b) Sai vì khi người lùi xa gương $0{,}5\text{ m}$ thì ảnh cũng lùi xa gương $0{,}5\text{ m}$ về phía sau, nên khoảng cách giữa người và ảnh tăng thêm $2 \cdot 0{,}5 = 1{,}0\text{ m}$." "\n"
                r"c) Đúng vì gương phẳng làm đảo ngược chiều trái – phải nên kim giờ chỉ sang phải ($3\text{ giờ}$) sẽ có ảnh chỉ sang trái ($9\text{ giờ}$)." "\n"
                r"d) Đúng vì mỗi gương nghiêng $45^\circ$ làm tia sáng bẻ góc $90^\circ$, qua hai gương song song tia ló song song và cùng hướng với tia tới ban đầu.",
            ),
            mcq(
                "vandung",
                r"Trong một phòng khám nhãn khoa nhỏ, bác sĩ đặt bảng thử thị lực ở sát bức tường phía sau lưng người bệnh và treo một gương phẳng ở bức tường đối diện trước mặt người bệnh. Biết người bệnh ngồi cách gương phẳng $2{,}2\text{ m}$ và cách bảng thử thị lực phía sau lưng mình $0{,}6\text{ m}$. Khoảng cách từ mắt người bệnh đến **ảnh của bảng thử thị lực** trong gương phẳng là:",
                [
                    r"$5{,}0\text{ m}$.",
                    r"$4{,}4\text{ m}$.",
                    r"$2{,}8\text{ m}$.",
                    r"$5{,}6\text{ m}$.",
                ],
                0,
                r"Khoảng cách từ bảng thử thị lực đến gương phẳng là $d_{\text{bảng}} = 2{,}2 + 0{,}6 = 2{,}8\text{ m}$. Do đó ảnh của bảng thử thị lực nằm ở phía sau gương và cách gương một đoạn $d'_{\text{bảng}} = 2{,}8\text{ m}$. Vì mắt người bệnh cách mặt gương $2{,}2\text{ m}$ ở phía trước nên khoảng cách từ mắt người bệnh đến ảnh của bảng thử thị lực là $L = 2{,}2 + 2{,}8 = 5{,}0\text{ m}$.",
            ),
            short(
                "vandung",
                r"Một điểm sáng $S$ đặt cách gương phẳng $80\text{ cm}$. Khi dịch chuyển điểm sáng $S$ lại gần gương thêm một đoạn $25\text{ cm}$ theo phương vuông góc với mặt gương thì khoảng cách giữa điểm sáng $S$ và ảnh ảo $S'$ của nó lúc sau bằng bao nhiêu xăng-ti-mét?",
                ["110", "110,0", "110.0"],
                r"Khoảng cách mới từ điểm sáng $S$ đến gương phẳng là $d_2 = 80 - 25 = 55\text{ cm}$. Khoảng cách giữa điểm sáng $S$ và ảnh ảo $S'$ lúc sau là $L_2 = 2d_2 = 2 \cdot 55 = 110\text{ cm}$.",
            ),
        ],
    },
    {
        "topic": "anh-sang-mau",
        "title": "Ánh sáng màu và Sự phân tích ánh sáng trắng",
        "icon": "🌈",
        "description": "Chủ đề mở rộng Chương V · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (bổ trợ Bài 15 Năng lượng ánh sáng và thực nghiệm quang học phổ thông). Nguồn phát ánh sáng trắng và ánh sáng đơn sắc, sự phân tích ánh sáng trắng qua lăng kính tạo dải màu cầu vồng, sự trộn các ánh sáng màu cơ bản và khả năng hấp thụ năng lượng ánh sáng của các vật màu sáng – màu tối.",
        "requirements": [
            r"Phân biệt được nguồn phát ánh sáng trắng (Mặt Trời, đèn sợi đốt, đèn LED trắng) và nguồn phát ánh sáng màu đơn sắc (đèn laser đỏ, đèn LED màu).",
            r"Mô tả được sự phân tích một chùm ánh sáng trắng khi đi qua lăng kính thuỷ tinh thành dải màu biến thiên liên tục từ đỏ đến tím (đỏ, da cam, vàng, lục, lam, chàm, tím) và giải thích được sự hình thành cầu vồng.",
            r"Nêu được kết quả trộn ba ánh sáng màu cơ bản (Đỏ, Lục, Lam) với nhau và giải thích được vì sao ta nhìn thấy màu sắc của các vật dưới ánh sáng trắng.",
            r"So sánh được khả năng phản xạ và hấp thụ năng lượng ánh sáng (chuyển thành nhiệt năng) của các vật có bề mặt màu trắng hoặc sáng và màu đen hoặc tối để ứng dụng trong đời sống.",
        ],
        "definition": (
            r"- **Ánh sáng trắng** (như ánh sáng Mặt Trời) không phải là ánh sáng đơn lẻ mà là hỗn hợp của vô số ánh sáng màu có màu biến thiên liên tục từ **đỏ đến tím** ($7$ màu chính: **Đỏ, Da cam, Vàng, Lục, Lam, Chàm, Tím**)." "\n"
            r"- **Ánh sáng đơn sắc** là ánh sáng có một màu nhất định và không bị phân tích thành các màu khác khi đi qua lăng kính." "\n"
            r"- **Ba màu ánh sáng cơ bản (sơ cấp)** trong quang học là **Đỏ (Red), Lục (Green) và Lam (Blue)** — hệ màu $\text{RGB}$; khi trộn ba chùm sáng màu này với cường độ thích hợp sẽ thu được **ánh sáng trắng**."
        ),
        "theory": (
            r"### Bài 15 (Chuyên sâu). Năng lượng ánh sáng và sự hấp thụ ánh sáng của các vật" "\n"
            r"- Khi ánh sáng chiếu vào một vật, một phần năng lượng ánh sáng bị phản xạ (hoặc tán xạ) trở lại, phần còn lại bị vật **hấp thụ** và chuyển hoá thành **nhiệt năng** làm vật nóng lên." "\n"
            r"- **Sự phụ thuộc vào màu sắc bề mặt**:" "\n"
            r"  + **Vật màu trắng (hoặc màu sáng, tráng bạc)**: Phản xạ hầu hết các ánh sáng màu chiếu tới và hấp thụ rất ít năng lượng ánh sáng nên **ít nóng lên**." "\n"
            r"  + **Vật màu đen (hoặc màu sẫm tối)**: Hấp thụ hầu hết các ánh sáng màu chiếu tới (không phản xạ ánh sáng nào) nên chuyển hoá nhiều quang năng thành nhiệt năng và **nóng lên nhanh hơn, nhiều hơn**." "\n"
            r"### Mở rộng thực nghiệm Chương V. Ánh sáng trắng, ánh sáng màu và sự phân tích ánh sáng" "\n"
            r"- **Sự phân tích ánh sáng trắng bằng lăng kính (Thí nghiệm Newton)**: Khi chiếu một chùm tia sáng trắng hẹp đi qua một **lăng kính** tam giác trong suốt, chùm sáng vừa bị lệch về phía đáy lăng kính vừa bị tách thành một dải màu liên tục như cầu vồng: tia **đỏ** bị lệch ít nhất, tia **tím** bị lệch nhiều nhất. Hiện tượng **cầu vồng** sau cơn mưa là do các giọt nước mưa nhỏ li ti trong không khí đóng vai trò như hàng triệu lăng kính phân tích ánh sáng Mặt Trời." "\n"
            r"- **Tạo ánh sáng màu bằng tấm lọc màu**: Chiếu ánh sáng trắng qua tấm lọc màu nào thì tấm lọc chỉ cho ánh sáng màu đó đi qua và hấp thụ các ánh sáng màu khác (ví dụ tấm lọc màu đỏ chỉ cho ánh sáng đỏ đi qua)." "\n"
            r"- **Sự trộn các ánh sáng màu ($\text{RGB}$)**:" "\n"
            r"  + Đỏ $+$ Lục $\rightarrow$ **Vàng**;" "\n"
            r"  + Đỏ $+$ Lam $\rightarrow$ **Hồng sẫm (Đỏ cánh sen)**;" "\n"
            r"  + Lục $+$ Lam $\rightarrow$ **Lam ngọc (Xanh lơ)**;" "\n"
            r"  + Đỏ $+$ Lục $+$ Lam $\rightarrow$ **Ánh sáng trắng**." "\n"
            r"- **Màu sắc các vật dưới ánh sáng**: Vật màu nào thì tán xạ mạnh ánh sáng màu đó vào mắt và hấp thụ các màu còn lại (ví dụ lá cây màu lục vì tán xạ ánh sáng lục và hấp thụ ánh sáng đỏ, lam để quang hợp)."
        ),
        "formulas": [
            G(
                "I. Phân tích và Tổng hợp ánh sáng",
                F("Thứ tự 7 vùng màu quang phổ ánh sáng trắng", r"$\text{Đỏ} \rightarrow \text{Da cam} \rightarrow \text{Vàng} \rightarrow \text{Lục} \rightarrow \text{Lam} \rightarrow \text{Chàm} \rightarrow \text{Tím}$", r"Qua lăng kính, tia đỏ lệch ít nhất, tia tím lệch nhiều nhất."),
                F("Tổng hợp 3 màu ánh sáng cơ bản RGB", r"$\text{Đỏ (R)} + \text{Lục (G)} + \text{Lam (B)} \rightarrow \text{Ánh sáng trắng}$", r"Nguyên lí hiển thị màu của màn hình tivi, điện thoại, máy tính."),
                F("Trộn từng cặp ánh sáng màu cơ bản", r"$\text{Đỏ} + \text{Lục} \rightarrow \text{Vàng}; \quad \text{Đỏ} + \text{Lam} \rightarrow \text{Hồng sẫm}; \quad \text{Lục} + \text{Lam} \rightarrow \text{Xanh lơ}$"),
            ),
            G(
                "II. Hấp thụ năng lượng ánh sáng theo màu sắc",
                F("So sánh độ tăng nhiệt độ khi phơi nắng cùng thời gian", r"$\Delta t_{\text{vật màu đen}} > \Delta t_{\text{vật màu trắng}}$", r"Vật màu đen hấp thụ quang năng chuyển thành nhiệt năng mạnh nhất."),
            ),
        ],
        "example": (
            r"Đặt hai chiếc bình kim loại giống hệt nhau chứa cùng một lượng nước ở $25^\circ\text{C}$ dưới ánh nắng Mặt Trời gay gắt trong $45\text{ phút}$: bình $A$ được sơn mặt ngoài màu đen nhám, bình $B$ được sơn mặt ngoài màu trắng bóng. Hỏi nước trong bình nào sẽ có nhiệt độ cao hơn? Giải thích vì sao vào mùa hè ta nên mặc áo sáng màu, còn vào mùa đông nên mặc áo tối màu."
        ),
        "example_answer": (
            r"- Nước trong **bình $A$ (sơn màu đen)** sẽ có nhiệt độ cao hơn nhiều so với bình $B$ (sơn màu trắng). Nguyên nhân là bề mặt màu đen hấp thụ hầu hết năng lượng ánh sáng Mặt Trời và chuyển hoá thành nhiệt năng truyền cho nước, trong khi bề mặt màu trắng bóng phản xạ phần lớn ánh sáng chiếu tới." "\n"
            r"- **Ứng dụng trang phục**: Vào mùa hè nắng nóng, mặc quần áo màu trắng hoặc màu sáng giúp phản xạ bớt ánh sáng Mặt Trời nên cơ thể mát hơn; vào mùa đông lạnh, mặc quần áo màu tối giúp hấp thụ nhiều năng lượng ánh sáng hơn để giữ ấm cơ thể."
        ),
        "real_life": (
            r"- Các ống thu nhiệt của **máy nước nóng năng lượng Mặt Trời** trên mái nhà luôn được phủ lớp hấp thụ màu đen sẫm để thu được tối đa quang năng biến thành nhiệt năng đun sôi nước." "\n"
            r"- Màn hình điện thoại thông minh, máy tính và tivi màu tạo ra hàng triệu màu sắc sống động chỉ bằng cách phối hợp độ sáng của ba điểm ảnh phụ (sub-pixel) phát ánh sáng màu **Đỏ (R), Lục (G) và Lam (B)**."
        ),
        "game_title": "Phòng thí nghiệm Lăng kính và Pha trộn Ánh sáng màu",
        "game_description": "Chiếu chùm sáng trắng qua lăng kính để quan sát quang phổ bảy màu và pha trộn ba chùm sáng màu cơ bản Đỏ, Lục, Lam.",
        "game_type": "game_anhsangmau",
        "quiz": [
            mcq(
                "biet",
                r"Khi chiếu một chùm ánh sáng trắng hẹp đi qua một lăng kính thuỷ tinh, ta thu được dải màu biến thiên liên tục theo thứ tự $7$ màu chính là:",
                [
                    r"Đỏ, da cam, vàng, lục, lam, chàm, tím.",
                    r"Đỏ, vàng, da cam, lục, chàm, lam, tím.",
                    r"Tím, đỏ, vàng, lục, da cam, lam, chàm.",
                    r"Trắng, đen, xám, đỏ, vàng, lục, lam.",
                ],
                0,
                r"Dải quang phổ của ánh sáng trắng qua lăng kính gồm $7$ màu chính theo đúng thứ tự: **đỏ, da cam, vàng, lục, lam, chàm, tím**.",
            ),
            mcq(
                "biet",
                r"Ba màu ánh sáng cơ bản (sơ cấp) được dùng để pha trộn tạo ra ánh sáng trắng và mọi màu sắc trên màn hình tivi, điện thoại là:",
                [
                    r"Đỏ, Lục, Lam ($\text{RGB}$).",
                    r"Đỏ, Vàng, Đen.",
                    r"Trắng, Đen, Xám.",
                    r"Cam, Chàm, Tím.",
                ],
                0,
                r"Ba màu ánh sáng cơ bản trong quang học là **Đỏ (Red), Lục (Green) và Lam (Blue)**.",
            ),
            mcq(
                "biet",
                r"Dưới ánh sáng Mặt Trời, vật có màu nào sau đây hấp thụ năng lượng ánh sáng mạnh nhất và nóng lên nhanh nhất?",
                [
                    r"Vật có bề mặt màu đen.",
                    r"Vật có bề mặt màu trắng.",
                    r"Vật có bề mặt tráng bạc bóng loáng.",
                    r"Vật có bề mặt màu vàng nhạt.",
                ],
                0,
                r"Vật **màu đen** hấp thụ hầu hết tất cả các ánh sáng màu chiếu tới nó và chuyển hoá mạnh thành nhiệt năng nên nóng lên nhanh nhất.",
            ),
            mcq(
                "biet",
                r"Hiện tượng tự nhiên nào sau đây là kết quả của sự phân tích ánh sáng Mặt Trời khi truyền qua các giọt nước mưa nhỏ li ti trong không khí?",
                [
                    r"Hiện tượng cầu vồng.",
                    r"Hiện tượng nhật thực.",
                    r"Hiện tượng nguyệt thực.",
                    r"Hiện tượng tiếng vang.",
                ],
                0,
                r"Các giọt nước mưa đóng vai trò như những lăng kính nhỏ phân tích ánh sáng trắng của Mặt Trời thành dải màu **cầu vồng**.",
            ),
            mcq(
                "hieu",
                r"Khi chiếu đồng thời hai chùm sáng màu **Đỏ** và màu **Lục** có cùng cường độ chồng lên nhau trên một màn chắn màu trắng trong buồng tối, tại vùng giao nhau trên màn chắn ta sẽ nhìn thấy màu gì?",
                [
                    r"Màu vàng.",
                    r"Màu trắng.",
                    r"Màu tím.",
                    r"Màu đen.",
                ],
                0,
                r"Theo quy tắc trộn ánh sáng màu cơ bản: ánh sáng **Đỏ** trộn với ánh sáng **Lục** cho ta ánh sáng **màu Vàng**.",
            ),
            mcq(
                "hieu",
                r"Chiếu một chùm sáng trắng đi qua một tấm kính lọc **màu đỏ**, sau đó cho chùm sáng ló ra tiếp tục chiếu vào một tấm kính lọc **màu lam** đặt nối tiếp phía sau. Phía sau tấm kính lọc màu lam ta sẽ thu được:",
                [
                    r"Hầu như không có ánh sáng truyền qua (tối đen).",
                    r"Chùm sáng màu trắng.",
                    r"Chùm sáng màu lục.",
                    r"Chùm sáng màu vàng rực rỡ.",
                ],
                0,
                r"Tấm lọc màu đỏ chỉ cho ánh sáng đỏ đi qua; khi ánh sáng đỏ này gặp tấm lọc màu lam thì bị tấm lọc màu lam hấp thụ hoàn toàn nên phía sau **tối đen** (không có ánh sáng truyền qua).",
            ),
            tf4(
                "hieu",
                r"Xét các thí nghiệm phân tích và trộn ánh sáng màu trong phòng thực hành. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Khi chiếu chùm tia laser màu đỏ đi qua một lăng kính thuỷ tinh, chùm tia ló ra khỏi lăng kính chỉ bị lệch đường truyền nhưng vẫn giữ nguyên màu đỏ chứ không tách thành nhiều màu.",
                    r"b) Khi chiếu chùm sáng trắng qua lăng kính, tia sáng màu đỏ bị lệch nhiều nhất còn tia sáng màu tím bị lệch ít nhất.",
                    r"c) Trộn ba chùm sáng màu Đỏ, Lục và Lam với cường độ thích hợp trên màn trắng sẽ thu được ánh sáng màu trắng.",
                    r"d) Dưới ánh sáng trắng của Mặt Trời, ta nhìn thấy bông hoa hồng có màu đỏ vì cánh hoa tán xạ mạnh ánh sáng màu đỏ vào mắt ta và hấp thụ các ánh sáng màu khác.",
                ],
                [True, False, True, True],
                r"a) Đúng vì tia laser đỏ là ánh sáng đơn sắc nên không bị phân tích thành các màu khác khi qua lăng kính." "\n"
                r"b) Sai vì khi đi qua lăng kính, tia **đỏ** bị lệch ít nhất còn tia **tím** bị lệch nhiều nhất." "\n"
                r"c) Đúng theo nguyên lí tổng hợp ba màu ánh sáng cơ bản $\text{RGB}$." "\n"
                r"d) Đúng vì vật màu đỏ tán xạ tốt ánh sáng đỏ và hấp thụ các màu còn lại.",
            ),
            tf4(
                "hieu",
                r"Xét ứng dụng của sự hấp thụ năng lượng ánh sáng và màu sắc trong đời sống. Mỗi phát biểu sau đúng hay sai?",
                [
                    r"a) Bồn chứa xăng dầu và vỏ máy bay dân dụng thường được sơn màu trắng hoặc màu bạc sáng để phản xạ tốt ánh sáng Mặt Trời, hạn chế bị nung nóng.",
                    r"b) Trong các bộ thu nhiệt của máy nước nóng năng lượng Mặt Trời, các ống thu nhiệt được sơn màu trắng tinh để hấp thụ được nhiều nhiệt nhất.",
                    r"c) Trong buồng tối chỉ thắp một ngọn đèn LED phát ánh sáng đơn sắc màu lục, nếu ta nhìn vào một tờ giấy trắng thì sẽ thấy tờ giấy có màu lục.",
                    r"d) Lá cây xanh hấp thụ rất mạnh ánh sáng màu lục để thực hiện quá trình quang hợp.",
                ],
                [True, False, True, False],
                r"a) Đúng vì sơn màu trắng hoặc bạc sáng giúp phản xạ ánh sáng, tránh nóng lên gây nguy cơ cháy nổ xăng dầu hoặc tốn năng lượng làm mát." "\n"
                r"b) Sai vì ống thu nhiệt của máy nước nóng năng lượng Mặt Trời phải được phủ **màu đen sẫm** để hấp thụ tối đa năng lượng ánh sáng." "\n"
                r"c) Đúng vì tờ giấy trắng phản xạ tốt mọi ánh sáng màu chiếu tới nó; khi chỉ chiếu ánh sáng lục thì nó phản xạ ánh sáng lục vào mắt." "\n"
                r"d) Sai vì lá cây có màu lục chính là do chất diệp lục **không hấp thụ** (mà phản xạ và tán xạ) ánh sáng màu lục; lá cây hấp thụ mạnh ánh sáng vùng đỏ và lam tím để quang hợp.",
            ),
            mcq(
                "vandung",
                r"Một học sinh làm thí nghiệm phơi nắng hai cốc thuỷ tinh giống nhau chứa cùng $200\text{ ml}$ nước có nhiệt độ ban đầu là $26^\circ\text{C}$. Cốc thứ nhất bọc giấy bạc sáng bóng, cốc thứ hai bọc giấy đen mờ. Sau $30\text{ phút}$ phơi nắng, nước trong cốc bọc giấy bạc tăng thêm $4^\circ\text{C}$, còn độ tăng nhiệt độ của nước trong cốc bọc giấy đen gấp $2{,}5\text{ lần}$ độ tăng nhiệt độ của cốc bọc giấy bạc. Nhiệt độ của nước trong cốc bọc giấy đen lúc đó là:",
                [
                    r"$36^\circ\text{C}$.",
                    r"$30^\circ\text{C}$.",
                    r"$40^\circ\text{C}$.",
                    r"$34^\circ\text{C}$.",
                ],
                0,
                r"Độ tăng nhiệt độ của nước trong cốc bọc giấy đen là $\Delta t_2 = 2{,}5 \cdot 4^\circ\text{C} = 10^\circ\text{C}$. Vậy nhiệt độ của nước trong cốc bọc giấy đen sau $30\text{ phút}$ là $t_2 = 26^\circ\text{C} + 10^\circ\text{C} = 36^\circ\text{C}$.",
            ),
            short(
                "vandung",
                r"Một tấm pin mặt trời có diện tích tiếp nhận ánh sáng nhận được $1500\text{ J}$ năng lượng ánh sáng Mặt Trời trong mỗi giây và chuyển hoá được $18\%$ năng lượng ánh sáng đó thành điện năng. Tính lượng điện năng mà tấm pin mặt trời này tạo ra trong $1\text{ s}$ theo đơn vị jun ($\text{J}$).",
                ["270", "270,0", "270.0"],
                r"Lượng điện năng tạo ra trong mỗi giây là $W_{\text{điện}} = 18\% \cdot 1500 = 0{,}18 \cdot 1500 = 270\text{ J}$.",
            ),
        ],
    },
    {
        "topic": "nam-cham",
        "title": "Nam châm, Từ trường và Đường sức từ",
        "icon": "🧲",
        "description": "Chương VI · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (tr. 86–93): Bài 18 – Bài 19 (Phần I, II, III). Nam châm vĩnh cửu, vật liệu có tính chất từ, hai cực Bắc (N) và Nam (S) của nam châm, sự tương tác giữa hai cực nam châm; từ trường quanh nam châm và quanh dây dẫn mang dòng điện (thí nghiệm Oersted), từ phổ và quy ước chiều đường sức từ.",
        "requirements": [
            r"Tiến hành thí nghiệm để nêu được: nam châm là vật có từ tính (hút được các vật bằng sắt, thép, niken, côban); mỗi nam châm đều có hai cực là cực Bắc ($\text{N}$) và cực Nam ($\text{S}$).",
            r"Thực hiện thí nghiệm và phát biểu được quy luật tương tác giữa hai nam châm: hai cực cùng tên thì đẩy nhau, hai cực khác tên thì hút nhau.",
            r"Mô tả được thí nghiệm của Oersted để chứng tỏ xung quanh nam châm và xung quanh dây dẫn có dòng điện chạy qua đều có **từ trường** (tác dụng lực từ lên kim nam châm đặt trong nó).",
            r"Nhận biết được từ phổ bằng cách rắc mạt sắt và vẽ được đường sức từ quanh thanh nam châm thẳng, nam châm hình chữ U theo quy ước chiều đi ra từ cực Bắc ($\text{N}$) và đi vào cực Nam ($\text{S}$).",
        ],
        "definition": (
            r"- **Nam châm** là những vật có **từ tính** (có khả năng hút các vật làm bằng vật liệu từ như **sắt, thép, niken, côban**, ... và không hút đồng, nhôm, nhựa, gỗ). Mỗi nam châm luôn có hai cực: **cực Bắc** (kí hiệu $\text{N}$ — North, thường sơn màu đỏ) và **cực Nam** (kí hiệu $\text{S}$ — South, thường sơn màu xanh hoặc trắng)." "\n"
            r"- **Tương tác giữa hai nam châm**: Khi đưa từ cực của hai nam châm lại gần nhau thì **hai từ cực cùng tên đẩy nhau** ($\text{N} - \text{N}$ hoặc $\text{S} - \text{S}$), **hai từ cực khác tên hút nhau** ($\text{N} - \text{S}$)." "\n"
            r"- **Từ trường** là khoảng không gian bao quanh một nam châm hoặc bao quanh một dây dẫn mang dòng điện, mà bất kì kim nam châm nào đặt trong đó cũng chịu tác dụng của **lực từ**." "\n"
            r"- **Đường sức từ** là những đường cong khép kín (hoặc nối từ cực này sang cực kia) mô tả hình dạng từ trường; ở bên ngoài thanh nam châm, đường sức từ có chiều **đi ra từ cực Bắc ($\text{N}$) và đi vào cực Nam ($\text{S}$)**."
        ),
        "theory": (
            r"### Bài 18. Nam châm" "\n"
            r"- **Tính chất định hướng của kim nam châm tự do**: Khi một kim nam châm (hoặc thanh nam châm treo bằng sợi chỉ mềm không xoắn) nằm cân bằng tự do trên trục nhọn, nó luôn chỉ theo hướng **Bắc – Nam địa lí**: đầu luôn hướng về phía Bắc gọi là cực Bắc ($\text{N}$), đầu luôn hướng về phía Nam gọi là cực Nam ($\text{S}$)." "\n"
            r"- **Tính mạnh yếu trên thanh nam châm**: Lực từ mạnh nhất ở **hai đầu cực** của thanh nam châm và rất yếu ở vùng chính giữa (vùng trung hoà). Lưu ý: Không thể tách riêng một cực Bắc hoặc một cực Nam độc lập — nếu cưa đôi một thanh nam châm, ta luôn thu được hai thanh nam châm mới mà mỗi thanh đều có đủ hai cực $\text{N}$ và $\text{S}$." "\n"
            r"### Bài 19. Từ trường" "\n"
            r"- **Nhận biết từ trường**: Mắt thường không nhìn thấy từ trường. Để nhận biết ở một điểm trong không gian có từ trường hay không, người ta dùng **kim nam châm thử**: nếu kim nam châm bị lệch khỏi hướng Bắc – Nam ban đầu thì tại đó có từ trường." "\n"
            r"- **Thí nghiệm Oersted ($1820$)**: Khi cho dòng điện chạy qua một dây dẫn thẳng đặt song song phía trên một kim nam châm, kim nam châm bị quay lệch đi; khi ngắt dòng điện, kim nam châm quay về vị trí cũ. Điều đó chứng tỏ **xung quanh dây dẫn có dòng điện cũng tồn tại một từ trường**." "\n"
            r"- **Từ phổ và đường sức từ**:" "\n"
            r"  + **Từ phổ** là hình ảnh trực quan của các đường mạt sắt sắp xếp thành những đường cong nối từ cực này sang cực kia khi rắc mạt sắt lên tấm nhựa phẳng đặt trên thanh nam châm rồi gõ nhẹ." "\n"
            r"  + Nơi nào mạt sắt dày (các đường sức từ **mau (dày)**) thì từ trường ở đó **mạnh** (như ở gần hai đầu cực); nơi nào mạt sắt thưa (các đường sức từ **thưa**) thì từ trường ở đó **yếu**." "\n"
            r"  + Kim nam châm đặt trên đường sức từ luôn định hướng dọc theo đường sức từ đó: cực Bắc ($\text{N}$) của kim nam châm hướng về phía cực Nam ($\text{S}$) của thanh nam châm."
        ),
        "formulas": [
            G(
                "I. Quy luật tương tác từ & Vật liệu từ",
                F("Hai cực cùng tên", r"$\text{Cực N} \leftrightarrow \text{Cực N} \text{ (hoặc } \text{S} \leftrightarrow \text{S}\text{)} \Rightarrow \text{Đẩy nhau}$"),
                F("Hai cực khác tên", r"$\text{Cực N} \leftrightarrow \text{Cực S} \Rightarrow \text{Hút nhau}$"),
                F("Vật liệu có tính chất từ", r"$\text{Sắt (Fe), Thép, Niken (Ni), Côban (Co)}$", r"Nam châm không hút đồng ($\text{Cu}$), nhôm ($\text{Al}$), bạc ($\text{Ag}$), vàng ($\text{Au}$), nhựa, gỗ."),
            ),
            G(
                "II. Quy ước Đường sức từ bên ngoài nam châm",
                F("Chiều đường sức từ bên ngoài nam châm", r"$\text{Đi ra từ cực Bắc (N)} \rightarrow \text{Đi vào cực Nam (S)}$"),
                F("Độ mạnh yếu của từ trường theo mật độ đường sức", r"$\text{Đường sức từ càng dày (mau)} \iff \text{Từ trường càng mạnh}$", r"Từ trường mạnh nhất ở sát hai từ cực $\text{N}, \text{S}$."),
            ),
        ],
        "example": (
            r"Có hai thanh kim loại $A$ và $B$ bề ngoài giống hệt nhau, trong đó một thanh là nam châm vĩnh cửu và thanh kia là thanh sắt non chưa bị nhiễm từ. Không dùng thêm bất kì vật nào khác, làm thế nào để nhận biết thanh nào là thanh nam châm?"
        ),
        "example_answer": (
            r"- **Cách thực hiện**: Ta cầm một đầu của thanh $A$ đưa chạm vào chính giữa của thanh $B$ (tạo thành hình chữ $\text{T}$):" "\n"
            r"  + **Trường hợp 1**: Nếu đầu thanh $A$ **hút mạnh** phần chính giữa của thanh $B$ thì chứng tỏ đầu thanh $A$ là từ cực nam châm $\Rightarrow$ **thanh $A$ là nam châm**, còn thanh $B$ là thanh sắt." "\n"
            r"  + **Trường hợp 2**: Nếu đầu thanh $A$ **hầu như không hút** phần chính giữa của thanh $B$ (vì vùng chính giữa của thanh nam châm có từ tính rất yếu) $\Rightarrow$ **thanh $B$ là nam châm**, còn thanh $A$ là thanh sắt."
        ),
        "real_life": (
            r"- Nam châm vĩnh cửu được dùng để phân loại phế liệu sắt thép ra khỏi phế liệu đồng, nhôm, nhựa; dùng trong chốt giữ cửa tủ lạnh, hộp bút có nắp từ, loa điện động và tai nghe." "\n"
            r"- Tàu đệm từ (Maglev) sử dụng lực đẩy và hút cực mạnh giữa các từ cực để nâng đoàn tàu lơ lửng cách đường ray một khoảng nhỏ, triệt tiêu ma sát lăn giúp tàu đạt tốc độ trên $500\text{ km/h}$."
        ),
        "game_title": "Thí nghiệm Tương tác từ và Đường sức từ",
        "game_description": "Rắc mạt sắt và đặt kim nam châm thử quanh thanh nam châm thẳng, nam châm chữ U để quan sát từ phổ và xác định chiều đường sức từ.",
        "game_type": "game_namcham",
        "quiz": [
            mcq(
                "biet",
                r"Một thanh nam châm vĩnh cửu có thể hút mạnh các vật được làm bằng chất liệu nào sau đây?",
                [
                    r"Sắt, thép, niken và côban.",
                    r"Đồng đỏ, nhôm và bạc.",
                    r"Nhựa cứng, cao su và gỗ khô.",
                    r"Thuỷ tinh, sứ và giấy bìa.",
                ],
                0,
                r"Nam châm chỉ hút các vật làm bằng **vật liệu từ** như **sắt, thép, niken, côban, gadolini**; không hút đồng, nhôm, nhựa, gỗ.",
            ),
            mcq(
                "biet",
                r"Khi đưa cực Bắc ($\text{N}$) của thanh nam châm thứ nhất lại gần cực Bắc ($\text{N}$) của thanh nam châm thứ hai được treo tự do thì hiện tượng gì xảy ra?",
                [
                    r"Hai cực đẩy nhau ra xa.",
                    r"Hai cực hút chặt lấy nhau.",
                    r"Hai thanh nam châm không tương tác gì với nhau.",
                    r"Cả hai thanh nam châm đều mất hết từ tính ngay lập tức.",
                ],
                0,
                r"Hai từ cực **cùng tên** ($\text{N}$ và $\text{N}$, hoặc $\text{S}$ và $\text{S}$) khi đặt gần nhau sẽ **đẩy nhau**.",
            ),
            mcq(
                "biet",
                r"Theo quy ước, ở bên ngoài một thanh nam châm, các đường sức từ có chiều như thế nào?",
                [
                    r"Đi ra từ cực Bắc ($\text{N}$) và đi vào cực Nam ($\text{S}$).",
                    r"Đi ra từ cực Nam ($\text{S}$) và đi vào cực Bắc ($\text{N}$).",
                    r"Đi từ điểm chính giữa thanh nam châm ra cả hai đầu cực.",
                    r"Đi từ hai đầu cực tiến vào điểm chính giữa của thanh nam châm.",
                ],
                0,
                r"Quy ước chiều đường sức từ bên ngoài nam châm là **đi ra từ cực Bắc ($\text{N}$) và đi vào cực Nam ($\text{S}$)**.",
            ),
            mcq(
                "biet",
                r"Để nhận biết tại một điểm $M$ trong không gian có tồn tại **từ trường** hay không, dụng cụ đơn giản nhất mà người ta sử dụng là:",
                [
                    r"Một kim nam châm nhỏ quay tự do trên trục nhọn (kim nam châm thử).",
                    r"Một chiếc nhiệt kế thuỷ ngân.",
                    r"Một chiếc cân Roberval.",
                    r"Một chiếc thước kẹp kim loại bằng đồng.",
                ],
                0,
                r"Từ trường tác dụng lực từ lên kim nam châm đặt trong nó làm kim bị lệch hướng, nên ta dùng **kim nam châm thử** để phát hiện từ trường.",
            ),
            mcq(
                "hieu",
                r"Đặt một kim nam châm nhỏ tự do trên đường sức từ nằm trên trục của một thanh nam châm thẳng và ở gần đầu cực Bắc ($\text{N}$) của thanh nam châm đó. Khi kim nam châm nằm cân bằng, đầu cực nào của kim nam châm sẽ quay về phía cực Bắc ($\text{N}$) của thanh nam châm?",
                [
                    r"Cực Nam ($\text{S}$) của kim nam châm.",
                    r"Cực Bắc ($\text{N}$) của kim nam châm.",
                    r"Điểm chính giữa của kim nam châm.",
                    r"Kim nam châm quay tròn liên tục không dừng lại.",
                ],
                0,
                r"Vì hai cực khác tên hút nhau (và đường sức từ đi ra từ cực $\text{N}$ của thanh nam châm), nên **cực Nam ($\text{S}$)** của kim nam châm sẽ bị hút quay về phía cực Bắc ($\text{N}$) của thanh nam châm.",
            ),
            mcq(
                "hieu",
                r"Một bạn học sinh trộn lẫn các vụn nhỏ gồm: mạt sắt, vụn đồng, vụn nhôm và mạt cưa gỗ. Khi đưa một thanh nam châm bọc trong túi nilon mỏng lướt sát trên hỗn hợp đó, chất nào sẽ bám vào ngoài túi nilon?",
                [
                    r"Chỉ có mạt sắt.",
                    r"Cả mạt sắt, vụn đồng và vụn nhôm vì đều là kim loại.",
                    r"Chỉ có vụn đồng và vụn nhôm.",
                    r"Cả bốn chất đều bị hút bám vào túi.",
                ],
                0,
                r"Trong các kim loại trên, chỉ có **sắt** là vật liệu từ bị nam châm hút, còn đồng, nhôm và gỗ không bị nam châm hút.",
            ),
            tf4(
                "hieu",
                r"Xét các tính chất của nam châm vĩnh cửu và tương tác từ. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Trên một thanh nam châm thẳng, lực hút các vụn sắt mạnh nhất ở hai đầu từ cực và yếu nhất ở phần chính giữa thanh.",
                    r"b) Nếu một thanh nam châm thẳng chẳng may bị gãy làm đôi ở chính giữa, ta sẽ thu được một nửa chỉ có cực Bắc ($\text{N}$) và nửa kia chỉ có cực Nam ($\text{S}$).",
                    r"c) Nếu đầu $A$ của một thanh kim loại hút được cực Bắc ($\text{N}$) của kim nam châm thì chắc chắn thanh kim loại đó phải là một nam châm và đầu $A$ là cực Nam ($\text{S}$).",
                    r"d) Nếu đầu $A$ của một thanh kim loại đẩy cực Bắc ($\text{N}$) của kim nam châm thì chắc chắn thanh kim loại đó là nam châm và đầu $A$ là cực Bắc ($\text{N}$).",
                ],
                [True, False, False, True],
                r"a) Đúng vì từ trường tập trung mạnh nhất ở hai đầu cực." "\n"
                r"b) Sai vì không thể tách riêng một cực từ; mỗi nửa bị gãy đều trở thành một nam châm hoàn chỉnh có đủ cả hai cực $\text{N}$ và $\text{S}$." "\n"
                r"c) Sai vì một thanh sắt thường (chưa phải nam châm) cũng bị cực Bắc của kim nam châm hút; hiện tượng hút chưa đủ kết luận thanh đó là nam châm." "\n"
                r"d) Đúng vì chỉ có hai từ cực cùng tên mới đẩy nhau, nên hiện tượng **đẩy** là dấu hiệu chắc chắn chứng tỏ đầu $A$ là cực Bắc ($\text{N}$) của một nam châm.",
            ),
            tf4(
                "hieu",
                r"Xét từ phổ, đường sức từ và thí nghiệm Oersted. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Trong thí nghiệm Oersted, khi cho dòng điện chạy qua dây dẫn thẳng đặt gần kim nam châm thì kim nam châm bị lệch, chứng tỏ xung quanh dòng điện có từ trường.",
                    r"b) Ở vùng không gian càng gần hai đầu cực của thanh nam châm, các đường mạt sắt trong từ phổ càng thưa thớt vì từ trường ở đó yếu.",
                    r"c) Trong lòng khoảng giữa hai nhánh thẳng song song của một nam châm hình chữ $\text{U}$, các đường sức từ là những đường thẳng gần như song song và cách đều nhau.",
                    r"d) Tại một điểm bất kì trong từ trường của một thanh nam châm, các đường sức từ có thể cắt nhau tại nhiều điểm.",
                ],
                [True, False, True, False],
                r"a) Đúng theo kết quả thí nghiệm Oersted ($1820$)." "\n"
                r"b) Sai vì ở gần hai đầu cực của nam châm, từ trường rất mạnh nên các đường mạt sắt xếp **rất dày (mau)**." "\n"
                r"c) Đúng vì trong lòng nam châm chữ $\text{U}$ từ trường gần như đều nên các đường sức từ gần như song song cách đều nhau, đi từ cực $\text{N}$ sang cực $\text{S}$." "\n"
                r"d) Sai vì tại mỗi điểm trong từ trường chỉ có một hướng xác định của lực từ nên hai đường sức từ **không bao giờ cắt nhau**.",
            ),
            mcq(
                "vandung",
                r"Có ba thanh nam châm thẳng $1, 2, 3$. Đưa cực $A$ của thanh $1$ lại gần cực $B$ của thanh $2$ thì chúng **hút nhau**; đưa cực $B$ của thanh $2$ lại gần cực $C$ của thanh $3$ thì chúng **đẩy nhau**; đưa cực $C$ của thanh $3$ lại gần đầu cực còn lại $D$ của thanh $3$ thì chắc chắn $C$ và $D$ là hai cực trái tên. Biết cực $A$ của thanh $1$ là cực Bắc ($\text{N}$). Tên của các từ cực $B, C, D$ lần lượt là:",
                [
                    r"$B$ là cực Nam ($\text{S}$), $C$ là cực Nam ($\text{S}$), $D$ là cực Bắc ($\text{N}$).",
                    r"$B$ là cực Bắc ($\text{N}$), $C$ là cực Nam ($\text{S}$), $D$ là cực Bắc ($\text{N}$).",
                    r"$B$ là cực Nam ($\text{S}$), $C$ là cực Bắc ($\text{N}$), $D$ là cực Nam ($\text{S}$).",
                    r"$B$ là cực Nam ($\text{S}$), $C$ là cực Nam ($\text{S}$), $D$ là cực Nam ($\text{S}$).",
                ],
                0,
                r"Vì $A$ là cực $\text{N}$ và $A$ hút $B$ nên $B$ là cực $\text{S}$ (khác tên). Vì $B$ ($\text{S}$) đẩy $C$ nên $C$ cùng tên với $B$, tức $C$ là cực $\text{S}$. Vì $C$ và $D$ là hai đầu của cùng thanh nam châm $3$ nên $D$ phải là cực Bắc ($\text{N}$).",
            ),
            short(
                "vandung",
                r"Một học sinh cưa một thanh nam châm thẳng dài thành $4$ đoạn nhỏ rời nhau. Hỏi tổng số từ cực (tính cả cực Bắc $\text{N}$ và cực Nam $\text{S}$) có trên cả $4$ đoạn nam châm nhỏ đó là bao nhiêu cực?",
                ["8"],
                r"Mỗi đoạn nam châm sau khi cắt rời đều là một nam châm hoàn chỉnh có đúng $2$ từ cực ($1$ cực $\text{N}$ và $1$ cực $\text{S}$). Vậy $4$ đoạn nam châm có tất cả $4 \cdot 2 = 8$ từ cực.",
            ),
        ],
    },
    {
        "topic": "nam-cham-dien-tu-truong-trai-dat",
        "title": "Từ trường Trái Đất, La bàn và Chế tạo nam châm điện đơn giản",
        "icon": "🧭",
        "description": "Chương VI · SGK Khoa học tự nhiên 7 Kết nối tri thức với cuộc sống (tr. 93–98): Bài 19 (Phần IV) – Bài 20. Từ trường Trái Đất, sự lệch giữa cực từ và cực địa lí, cấu tạo và cách sử dụng la bàn để xác định phương hướng; cấu tạo, nguyên tắc hoạt động của nam châm điện và các yếu tố làm thay đổi lực từ, cực từ của nam châm điện.",
        "requirements": [
            r"Dựa vào ảnh (hoặc hình vẽ, mô hình) khẳng định được Trái Đất có từ trường và nêu được cực Bắc địa lí và cực Bắc từ trường không trùng nhau (cực Bắc địa lí nằm gần cực Nam từ của Trái Đất).",
            r"Mô tả được cấu tạo của la bàn và sử dụng được la bàn để tìm hướng địa lí (Bắc, Nam, Đông, Tây).",
            r"Chế tạo được nam châm điện đơn giản (gồm ống dây dẫn quấn quanh lõi sắt non và nguồn điện) và tiến hành thí nghiệm khảo sát tác dụng từ của nam châm điện.",
            r"Nêu được các cách làm tăng lực từ của nam châm điện (tăng cường độ dòng điện, tăng số vòng dây, dùng lõi sắt non) và cách đổi tên từ cực của nam châm điện bằng cách đổi chiều dòng điện.",
        ],
        "definition": (
            r"- **Từ trường Trái Đất**: Trái Đất là một thanh nam châm khổng lồ có hai cực từ. Vì cực Bắc ($\text{N}$) của kim la bàn luôn bị hút hướng về phía **cực Bắc địa lí** của Trái Đất, nên về mặt bản chất từ học, ở gần cực Bắc địa lí là **cực Nam từ** của nam châm Trái Đất (và ở gần cực Nam địa lí là **cực Bắc từ** của nam châm Trái Đất). Trục từ và trục quay địa lí của Trái Đất không trùng khít mà lệch nhau một góc nhỏ." "\n"
            r"- **La bàn** là dụng cụ dùng để xác định phương hướng trên mặt đất, có bộ phận chính là một **kim nam châm** quay tự do trên trục nhọn đặt trên mặt chia độ ($0^\circ - 360^\circ$ với các hướng $\text{N}, \text{S}, \text{E}, \text{W}$)." "\n"
            r"- **Nam châm điện** gồm một **ống dây dẫn** có dòng điện một chiều chạy qua và bên trong ống dây có đặt một **lõi sắt non**."
        ),
        "theory": (
            r"### Bài 19 (Phần IV). Từ trường Trái Đất và La bàn" "\n"
            r"- **Vai trò của từ trường Trái Đất**: Từ trường Trái Đất tạo thành một “lá chắn từ quyển” làm lệch hướng các hạt mang điện năng lượng cao từ gió Mặt Trời và tia vũ trụ, bảo vệ bầu khí quyển và sự sống trên Trái Đất (đồng thời tạo nên hiện tượng **cực quang** ở vùng gần hai cực)." "\n"
            r"- **Cấu tạo và cách sử dụng la bàn**:" "\n"
            r"  + Các kí hiệu trên mặt la bàn: $\text{N}$ (North — hướng Bắc), $\text{S}$ (South — hướng Nam), $\text{E}$ (East — hướng Đông), $\text{W}$ (West — hướng Tây); ngoài ra còn có $\text{NE}$ (Đông Bắc), $\text{SE}$ (Đông Nam), $\text{SW}$ (Tây Nam), $\text{NW}$ (Tây Bắc)." "\n"
            r"  + **Các bước xác định hướng bằng la bàn**: (1) Đặt la bàn nằm ngang trên mặt phẳng, **cách xa các nam châm khác, dòng điện và các vật bằng sắt thép** (để tránh làm nhiễu kim la bàn); (2) Chờ cho kim nam châm đứng yên ổn định (luôn nằm dọc hướng Bắc – Nam); (3) Xoay nhẹ vỏ la bàn sao cho vạch chữ $\text{N}$ (số $0^\circ$) trên mặt chia độ trùng khít với đầu cực Bắc (thường sơn đỏ) của kim nam châm; (4) Đọc hướng của đối tượng cần xác định trên mặt chia độ." "\n"
            r"### Bài 20. Chế tạo nam châm điện đơn giản" "\n"
            r"- **Nguyên tắc hoạt động**: Khi đóng công tắc cho dòng điện chạy qua ống dây quấn quanh lõi sắt non, dòng điện sinh ra từ trường làm lõi sắt non bị nhiễm từ mạnh và trở thành một **nam châm điện** hút được các ghim sắt. Khi **ngắt dòng điện**, lõi sắt non **mất hết từ tính ngay lập tức** và các ghim sắt rơi xuống (vì vậy lõi nam châm điện phải dùng **sắt non** chứ không dùng thép — vì thép sau khi ngắt điện vẫn giữ từ tính lâu dài, biến thành nam châm vĩnh cửu, không điều khiển nhả vật được)." "\n"
            r"- **Cách làm thay đổi lực từ và cực từ của nam châm điện**:" "\n"
            r"  + **Tăng độ mạnh (lực từ) của nam châm điện**: Tăng **cường độ dòng điện** $I$ chạy qua ống dây (tăng số pin hoặc hiệu điện thế nguồn) hoặc tăng **số vòng dây** $N$ của ống dây trên cùng một đơn vị chiều dài." "\n"
            r"  + **Đổi tên hai từ cực ($\text{N} \leftrightarrow \text{S}$)**: Chỉ cần **đổi chiều dòng điện** chạy qua ống dây (đảo hai đầu dây nối với hai cực dương $+$, âm $-$ của pin)."
        ),
        "formulas": [
            G(
                "I. La bàn và Các hướng địa lí trên mặt chia độ",
                F("Bốn hướng chính trên la bàn", r"$\text{Bắc (N)} = 0^\circ; \quad \text{Đông (E)} = 90^\circ; \quad \text{Nam (S)} = 180^\circ; \quad \text{Tây (W)} = 270^\circ$"),
                F("Bốn hướng phụ chính giữa", r"$\text{Đông Bắc (NE)} = 45^\circ; \quad \text{Đông Nam (SE)} = 135^\circ; \quad \text{Tây Nam (SW)} = 225^\circ; \quad \text{Tây Bắc (NW)} = 315^\circ$"),
            ),
            G(
                "II. Quy luật điều khiển Nam châm điện",
                F("Các yếu tố làm tăng lực từ của nam châm điện", r"$I \text{ tăng hoặc } N_{\text{vòng dây}} \text{ tăng} \Rightarrow F_{\text{từ}} \text{ tăng}$", r"$I$ là cường độ dòng điện, $N_{\text{vòng dây}}$ là số vòng dây quấn quanh lõi sắt non."),
                F("Đổi chiều dòng điện qua ống dây", r"$\text{Đảo cực nguồn điện } (+ \leftrightarrow -) \Rightarrow \text{Đổi từ cực } (\text{N} \leftrightarrow \text{S})$"),
                F("Ngắt dòng điện qua ống dây lõi sắt non", r"$I = 0 \Rightarrow \text{Lõi sắt non mất từ tính ngay lập tức}$"),
            ),
        ],
        "example": (
            r"Một nhóm học sinh chế tạo nam châm điện bằng cách quấn dây đồng có vỏ cách điện quanh một chiếc đinh sắt non rồi nối hai đầu dây với một viên pin $1{,}5\text{ V}$. Khi đóng khoá $K$, đinh sắt hút được $6$ chiếc ghim giấy bằng sắt và đầu nhọn của đinh sắt đẩy cực Bắc ($\text{N}$) của một kim nam châm thử đặt gần đó." "\n"
            r"a) Đầu nhọn của đinh sắt đang là từ cực gì của nam châm điện?" "\n"
            r"b) Nêu hai cách giúp chiếc nam châm điện này hút được nhiều ghim sắt hơn và nêu hiện tượng xảy ra khi mở khoá $K$ (ngắt mạch điện)."
        ),
        "example_answer": (
            r"a) Vì đầu nhọn của đinh sắt **đẩy** cực Bắc ($\text{N}$) của kim nam châm thử (hai cực cùng tên đẩy nhau) nên đầu nhọn của đinh sắt đang là **cực Bắc ($\text{N}$)** của nam châm điện." "\n"
            r"b) **Hai cách làm tăng lực từ để hút được nhiều ghim sắt hơn**:" "\n"
            r"  - *Cách 1*: Quấn tăng thêm số vòng dây đồng quanh chiếc đinh sắt non (ví dụ từ $30\text{ vòng}$ lên $60\text{ vòng}$)." "\n"
            r"  - *Cách 2*: Tăng cường độ dòng điện qua ống dây bằng cách mắc nối tiếp hai viên pin $1{,}5\text{ V}$ (tạo nguồn $3\text{ V}$)." "\n"
            r"- Khi **mở khoá $K$ (ngắt dòng điện)**: Lõi đinh sắt non mất từ tính ngay lập tức nên các chiếc ghim sắt bị rơi ra."
        ),
        "real_life": (
            r"- **Cần cẩu điện từ** trong các nhà máy thép và bến cảng dùng nam châm điện cỡ lớn: khi đóng điện nó hút hàng tấn sắt thép phế liệu để di chuyển, khi tới thùng xe tải chỉ cần ngắt điện là toàn bộ sắt thép tự động rơi xuống." "\n"
            r"- Nam châm điện còn là bộ phận cốt lõi trong **chuông điện**, **rơ-le điện từ**, loa truyền thanh và động cơ điện; chim di cư, rùa biển và cá voi định hướng đường đi hàng nghìn ki-lô-mét nhờ cảm nhận được từ trường Trái Đất."
        ),
        "game_title": "Chế tạo Nam châm điện và Định hướng bằng La bàn",
        "game_description": "Thay đổi số vòng dây, cường độ dòng điện và lõi sắt non để khảo sát độ mạnh của nam châm điện và sử dụng la bàn xác định phương hướng trong từ trường Trái Đất.",
        "game_type": "game_nam_cham_dien",
        "quiz": [
            mcq(
                "biet",
                r"Trên mặt chia độ của một chiếc la bàn thông thường, bốn chữ cái viết tắt tiếng Anh $\text{N}, \text{S}, \text{E}, \text{W}$ lần lượt chỉ các hướng địa lí nào?",
                [
                    r"Bắc ($\text{N}$), Nam ($\text{S}$), Đông ($\text{E}$), Tây ($\text{W}$).",
                    r"Nam ($\text{N}$), Bắc ($\text{S}$), Đông ($\text{E}$), Tây ($\text{W}$).",
                    r"Bắc ($\text{N}$), Nam ($\text{S}$), Tây ($\text{E}$), Đông ($\text{W}$).",
                    r"Đông ($\text{N}$), Tây ($\text{S}$), Bắc ($\text{E}$), Nam ($\text{W}$).",
                ],
                0,
                r"Các kí hiệu quốc tế trên la bàn gồm: $\text{N}$ (North — Bắc), $\text{S}$ (South — Nam), $\text{E}$ (East — Đông), $\text{W}$ (West — Tây).",
            ),
            mcq(
                "biet",
                r"Tại sao lõi của một chiếc nam châm điện thường được làm bằng **sắt non** mà không làm bằng **thép**?",
                [
                    r"Vì khi ngắt dòng điện, sắt non mất ngay từ tính giúp ta điều khiển việc hút – nhả vật dễ dàng, còn thép vẫn giữ từ tính lâu dài.",
                    r"Vì thép hoàn toàn không bị nhiễm từ khi đặt trong ống dây có dòng điện.",
                    r"Vì sắt non nhẹ hơn thép gấp $10\text{ lần}$.",
                    r"Vì thép là chất cách điện còn sắt non là chất dẫn nhiệt.",
                ],
                0,
                r"Sắt non nhiễm từ mạnh khi có dòng điện và **mất từ tính ngay khi ngắt điện**; còn thép sau khi bị nhiễm từ sẽ giữ từ tính lâu dài (trở thành nam châm vĩnh cửu) nên không thể ngắt lực từ theo ý muốn.",
            ),
            mcq(
                "biet",
                r"Cách nào sau đây làm **đổi tên hai từ cực** (cực Bắc $\text{N}$ thành cực Nam $\text{S}$ và ngược lại) của một nam châm điện?",
                [
                    r"Đổi chiều dòng điện chạy qua ống dây (đảo hai cực của nguồn pin nối với ống dây).",
                    r"Tăng gấp đôi số vòng dây của ống dây theo cùng chiều quấn cũ.",
                    r"Mắc nối tiếp thêm một viên pin cùng chiều với viên pin ban đầu.",
                    r"Đưa thêm một số ghim sắt lại gần đầu lõi sắt non.",
                ],
                0,
                r"Chiều từ trường của nam châm điện phụ thuộc vào chiều dòng điện chạy trong các vòng dây, nên **đổi chiều dòng điện** sẽ làm đổi tên hai từ cực của nam châm điện.",
            ),
            mcq(
                "biet",
                r"Khi nói về từ trường của Trái Đất, phát biểu nào sau đây là **đúng**?",
                [
                    r"Cực Bắc địa lí và cực từ nằm gần đó của Trái Đất không trùng khít nhau mà lệch nhau một khoảng.",
                    r"Trục từ trường của Trái Đất trùng khít hoàn toàn tuyệt đối với trục quay địa lí.",
                    r"Xung quanh Trái Đất hoàn toàn không có từ trường, kim la bàn quay là do lực cản của gió.",
                    r"Ở gần cực Bắc địa lí của Trái Đất chỉ tồn tại lực hấp dẫn chứ không có đường sức từ.",
                ],
                0,
                r"Trục từ của Trái Đất và trục quay địa lí lệch nhau một góc nhỏ, do đó cực địa lí và cực từ của Trái Đất **không trùng nhau**.",
            ),
            mcq(
                "hieu",
                r"Vì sao cực Bắc ($\text{N}$) của kim nam châm trong chiếc la bàn khi để tự do lại luôn bị hút hướng về phía **cực Bắc địa lí** của Trái Đất?",
                [
                    r"Vì ở gần vùng cực Bắc địa lí của Trái Đất thực chất là cực Nam từ của “thanh nam châm khổng lồ Trái Đất” (hai cực khác tên hút nhau).",
                    r"Vì hai cực cùng tên Bắc ($\text{N}$) luôn hút nhau rất mạnh.",
                    r"Vì gió ở bán cầu Bắc luôn thổi đẩy kim la bàn về phía Bắc.",
                    r"Vì vỏ la bàn bằng đồng hút cực Bắc của kim nam châm.",
                ],
                0,
                r"Theo quy luật hai cực khác tên hút nhau, cực Bắc ($\text{N}$) của kim la bàn hướng về phía Bắc địa lí chứng tỏ ở gần cực Bắc địa lí là **cực Nam từ** của nam châm Trái Đất (và các đường sức từ Trái Đất đi từ vùng cực Nam địa lí ra ngoài không gian rồi đi vào vùng cực Bắc địa lí).",
            ),
            mcq(
                "hieu",
                r"Có bốn nam châm điện $A, B, C, D$ dùng cùng một loại lõi sắt non: nam châm $A$ có $N_A = 40\text{ vòng dây}$ và dòng điện $I_A = 1\text{ A}$; nam châm $B$ có $N_B = 40\text{ vòng dây}$ và $I_B = 2\text{ A}$; nam châm $C$ có $N_C = 80\text{ vòng dây}$ và $I_C = 1\text{ A}$; nam châm $D$ có $N_D = 80\text{ vòng dây}$ và $I_D = 2\text{ A}$. Nam châm điện nào có lực từ **mạnh nhất**?",
                [
                    r"Nam châm điện $D$ ($80\text{ vòng}$, $2\text{ A}$).",
                    r"Nam châm điện $A$ ($40\text{ vòng}$, $1\text{ A}$).",
                    r"Nam châm điện $B$ ($40\text{ vòng}$, $2\text{ A}$).",
                    r"Nam châm điện $C$ ($80\text{ vòng}$, $1\text{ A}$).",
                ],
                0,
                r"Lực từ của nam châm điện tăng khi tăng số vòng dây $N$ và tăng cường độ dòng điện $I$. Nam châm $D$ có cả $N = 80\text{ vòng}$ lớn nhất và $I = 2\text{ A}$ lớn nhất nên có **lực từ mạnh nhất**.",
            ),
            tf4(
                "hieu",
                r"Xét quy tắc sử dụng la bàn và đặc điểm của từ trường Trái Đất. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Khi sử dụng la bàn để tìm hướng địa lí, ta phải đặt la bàn cách xa các thanh nam châm, dây điện đang hoạt động và các vật bằng sắt thép.",
                    r"b) Khi kim la bàn đã đứng yên ổn định, bước tiếp theo là dùng ngón tay đẩy trực tiếp vào kim nam châm cho kim chỉ đúng vào chữ $\text{N}$.",
                    r"c) Trên mặt chia độ của la bàn ($0^\circ$ tại hướng Bắc $\text{N}$, tăng theo chiều kim đồng hồ qua hướng Đông $\text{E}$), hướng Đông Nam ($\text{SE}$) ứng với góc $135^\circ$.",
                    r"d) Các đường sức từ của từ trường Trái Đất ở bên ngoài Trái Đất đi từ vùng cực Nam địa lí hướng về vùng cực Bắc địa lí.",
                ],
                [True, False, True, True],
                r"a) Đúng vì các vật bằng sắt thép, nam châm hay dòng điện gần đó sẽ gây nhiễu làm kim la bàn chỉ sai hướng địa lí." "\n"
                r"b) Sai vì không được chạm tay vào kim nam châm mà phải **xoay nhẹ vỏ la bàn** sao cho vạch chữ $\text{N}$ trùng với đầu cực Bắc của kim nam châm." "\n"
                r"c) Đúng vì hướng Đông ($\text{E}$) là $90^\circ$ và hướng Nam ($\text{S}$) là $180^\circ$, nên hướng chính giữa Đông Nam ($\text{SE}$) ứng với $\dfrac{90^\circ + 180^\circ}{2} = 135^\circ$." "\n"
                r"d) Đúng vì ở gần cực Nam địa lí là cực Bắc từ của Trái Đất, nên các đường sức từ đi ra từ vùng cực Nam địa lí và đi vào vùng cực Bắc địa lí.",
            ),
            tf4(
                "hieu",
                r"So sánh những ưu điểm vượt trội của **nam châm điện** so với **nam châm vĩnh cửu** trong kĩ thuật và công nghiệp. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Nam châm điện có thể bật hoặc tắt từ tính một cách tức thời chỉ bằng cách đóng hoặc ngắt công tắc dòng điện.",
                    r"b) Độ mạnh yếu của lực từ ở nam châm điện có thể điều chỉnh linh hoạt bằng cách thay đổi cường độ dòng điện chạy qua ống dây.",
                    r"c) Có thể dễ dàng đổi tên hai cực Bắc ($\text{N}$) và Nam ($\text{S}$) của nam châm điện bằng cách đổi chiều dòng điện mà không cần tháo lắp hay quay đầu cuộn dây.",
                    r"d) Nếu tháo bỏ lõi sắt non ra khỏi lòng ống dây dẫn đang có dòng điện thì lực từ hút các đinh sắt của ống dây sẽ tăng lên gấp nhiều lần.",
                ],
                [True, True, True, False],
                r"a) Đúng vì lõi sắt non chỉ có từ tính khi có dòng điện chạy qua ống dây." "\n"
                r"b) Đúng vì tăng hoặc giảm dòng điện $I$ sẽ làm tăng hoặc giảm lực từ của nam châm điện." "\n"
                r"c) Đúng vì đổi chiều dòng điện làm đảo cực từ $\text{N} \leftrightarrow \text{S}$." "\n"
                r"d) Sai vì lõi sắt non có vai trò làm tăng tác dụng từ của ống dây lên rất nhiều lần; nếu rút lõi sắt non ra thì lực từ của ống dây sẽ **yếu đi rất nhiều**.",
            ),
            mcq(
                "vandung",
                r"Một bạn hướng dẫn viên du lịch đặt la bàn trên mặt phẳng ngang. Sau khi kim la bàn đứng yên và bạn đã xoay vỏ la bàn để vạch chữ $\text{N}$ ($0^\circ$) trùng khít với đầu cực Bắc của kim nam châm, bạn nhìn thấy cổng chính của khu cắm trại nằm đúng theo vạch $270^\circ$ trên mặt chia độ (vòng chia độ tăng từ $0^\circ$ ở $\text{N}$ qua $90^\circ$ ở $\text{E}$). Cổng chính của khu cắm trại nằm ở hướng nào so với vị trí đứng của bạn?",
                [
                    r"Hướng Tây ($\text{W}$).",
                    r"Hướng Đông ($\text{E}$).",
                    r"Hướng Nam ($\text{S}$).",
                    r"Hướng Đông Bắc ($\text{NE}$).",
                ],
                0,
                r"Trên mặt chia độ chuẩn của la bàn: Bắc ($\text{N}$) ứng với $0^\circ$, Đông ($\text{E}$) ứng với $90^\circ$, Nam ($\text{S}$) ứng với $180^\circ$ và **Tây ($\text{W}$)** ứng với $270^\circ$. Vậy cổng khu cắm trại nằm ở **hướng Tây ($\text{W}$)**.",
            ),
            short(
                "vandung",
                r"Một bạn học sinh đặt la bàn đã hiệu chỉnh đúng hướng Bắc ($\text{N}$ ứng với $0^\circ$, hướng Đông $\text{E}$ ứng với $90^\circ$, hướng Nam $\text{S}$ ứng với $180^\circ$, hướng Tây $\text{W}$ ứng với $270^\circ$). Ngôi trường học nằm ở chính giữa hướng Bắc và hướng Đông (tức hướng Đông Bắc $\text{NE}$). Hỏi tia ngắm từ tâm la bàn về phía ngôi trường ứng với vạch bao nhiêu độ trên mặt chia độ của la bàn?",
                ["45", "45,0", "45.0"],
                r"Hướng Đông Bắc ($\text{NE}$) nằm ở chính giữa hướng Bắc ($0^\circ$) và hướng Đông ($90^\circ$), nên ứng với góc $\dfrac{0^\circ + 90^\circ}{2} = 45^\circ$ trên mặt chia độ la bàn.",
            ),
        ],
    },
]
