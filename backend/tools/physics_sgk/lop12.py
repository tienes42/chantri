r"""VẬT LÍ 12 — Kết nối tri thức với cuộc sống (SGK Vật lí 12 & Chuyên đề học tập Vật lí 12).

Bao phủ toàn bộ 25 bài học thuộc 4 chương SGK Vật lí 12 và 3 chuyên đề học tập Vật lí 12
bộ sách "Kết nối tri thức với cuộc sống" (NXB Giáo dục Việt Nam) theo Chương trình GDPT 2018:
- Chương I. Vật lí nhiệt (Bài 1 – Bài 7, topic="vat-ly-nhiet").
- Chương II. Khí lí tưởng (Bài 8 – Bài 13, topic="vat-ly-nhiet-khi-ly-tuong").
- Chương III – Phần 1. Từ trường và Lực từ (Bài 14 – Bài 16, topic="tu-truong").
- Chương III – Phần 2. Máy phát điện xoay chiều, Dòng điện xoay chiều và Sóng điện từ (Bài 17 – Bài 20, topic="mach-xoay-chieu").
- Chương IV. Vật lí hạt nhân và Phóng xạ (Bài 21 – Bài 25, topic="hat-nhan").
- Chuyên đề Vật lí 12. Dòng điện xoay chiều RLC, Lượng tử ánh sáng và Thuyết tương đối (Chuyên đề 1 – 3, topic="quang-dien").

Mỗi đơn vị kiến thức gồm: Yêu cầu cần đạt (CT GDPT 2018), định nghĩa cốt lõi, lý thuyết theo từng bài SGK,
hệ thống công thức chuẩn KaTeX ($ ... $), ví dụ minh hoạ, ứng dụng thực tiễn, cấu hình game thực nghiệm
và bộ 10 câu hỏi đánh giá năng lực: Biết 4 TN | Hiểu 2 TN + 2 Đúng-Sai (4 ý a–d) | Vận dụng 1 TN + 1 Trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 12

LESSONS = [
    # =========================================================================
    # CHƯƠNG I. VẬT LÍ NHIỆT (Bài 1 – Bài 7 SGK Vật lí 12 KNTT)
    # =========================================================================
    {
        "topic": "vat-ly-nhiet",
        "title": "Chương I. Vật lí nhiệt",
        "icon": "🌡️",
        "description": (
            "Chương I · SGK Vật lí 12 Kết nối tri thức với cuộc sống (Bài 1 – Bài 7): "
            "Cấu trúc của chất và sự chuyển thể; Nội năng và Định luật 1 của nhiệt động lực học; "
            "Nhiệt độ, thang nhiệt độ Celsius – Kelvin và nhiệt kế; Nhiệt dung riêng; "
            "Nhiệt nóng chảy riêng; Nhiệt hoá hơi riêng; Bài tập về vật lí nhiệt."
        ),
        "requirements": [
            r"Sử dụng mô hình động học phân tử, nêu được sơ lược cấu trúc của chất rắn, chất lỏng, chất khí.",
            r"Giải thích được sơ lược một số hiện tượng vật lí liên quan đến sự chuyển thể: sự nóng chảy, sự đông đặc, sự hoá hơi (bay hơi và sôi), sự ngưng tụ, sự thăng hoa.",
            r"Thực hiện thí nghiệm, nêu được mối liên hệ giữa nội năng $U$ của vật với năng lượng của các phân tử tạo nên vật và phát biểu được Định luật $1$ của nhiệt động lực học $\Delta U = Q + A$.",
            r"Vận dụng được Định luật $1$ của nhiệt động lực học $\Delta U = Q + A$ (kèm quy ước dấu của nhiệt lượng $Q$ và công $A$) trong một số trường hợp thực tiễn.",
            r"Thực hiện thí nghiệm đơn giản, thảo luận để nêu được sự chênh lệch nhiệt độ giữa hai vật tiếp xúc nhau cho biết chiều truyền năng lượng nhiệt giữa chúng; khi hai vật tiếp xúc đạt trạng thái cân bằng nhiệt thì có cùng nhiệt độ.",
            r"Nêu được mỗi độ chia ($1^\circ\text{C}$) trong thang Celsius bằng $\dfrac{1}{100}$ khoảng cách giữa nhiệt độ tan chảy của nước tinh khiết đóng băng ($0^\circ\text{C}$) và nhiệt độ sôi của nước tinh khiết ($100^\circ\text{C}$) ở áp suất tiêu chuẩn; mỗi độ chia ($1\text{ K}$) trong thang Kelvin bằng $\dfrac{1}{273{,}16}$ khoảng cách giữa nhiệt độ không tuyệt đối ($0\text{ K}$) và nhiệt độ điểm ba của nước ($273{,}16\text{ K}$).",
            r"Chuyển đổi được nhiệt độ đo theo thang Celsius sang nhiệt độ đo theo thang Kelvin và ngược lại theo công thức $T\text{ (K)} = t\text{ (}^\circ\text{C)} + 273{,}15$ (hoặc $T \approx t + 273$).",
            r"Nêu được định nghĩa nhiệt dung riêng $c$ ($\text{J/(kg}\cdot\text{K)}$), nhiệt nóng chảy riêng $\lambda$ ($\text{J/kg}$), nhiệt hoá hơi riêng $L$ ($\text{J/kg}$) và đơn vị đo của chúng trong hệ SI.",
            r"Thảo luận để thiết kế phương án hoặc lựa chọn phương án và thực hiện phương án đo được nhiệt dung riêng $c$, nhiệt nóng chảy riêng $\lambda$ của nước đá và nhiệt hoá hơi riêng $L$ của nước bằng dụng cụ thực hành.",
            r"Vận dụng được các công thức $Q = mc\Delta T$, $Q = m\lambda$, $Q = mL$ và phương trình cân bằng nhiệt $Q_{\text{toả}} = Q_{\text{thu}}$ để giải các bài toán thực tiễn.",
        ],
        "definition": (
            r"- **Mô hình động học phân tử và cấu trúc chất**: Các chất được cấu tạo từ các hạt riêng biệt (phân tử, nguyên tử, ion) chuyển động nhiệt hỗn loạn không ngừng; nhiệt độ càng cao thì các hạt chuyển động càng nhanh. Giữa các hạt luôn tồn tại đồng thời lực hút và lực đẩy phân tử. Ở **thể rắn**, các hạt dao động quanh vị trí cân bằng cố định (mạng tinh thể xác định); ở **thể lỏng**, các hạt dao động quanh vị trí cân bằng có thể di chuyển; ở **thể khí**, khoảng cách giữa các hạt rất lớn nên lực tương tác không đáng kể và các hạt chuyển động hỗn loạn về mọi phía." "\n"
            r"- **Nội năng ($U$) và Định luật $1$ của nhiệt động lực học**: Nội năng $U$ của một vật là tổng động năng chuyển động nhiệt của các phân tử và thế năng tương tác giữa chúng, phụ thuộc vào nhiệt độ $T$ và thể tích $V$ của vật. Định luật $1$ của nhiệt động lực học: $\Delta U = Q + A$, trong đó $Q > 0$ nếu vật nhận nhiệt lượng, $Q < 0$ nếu vật truyền nhiệt lượng; $A > 0$ nếu vật nhận công, $A < 0$ nếu vật thực hiện công." "\n"
            r"- **Thang nhiệt độ Celsius và Kelvin**: Hai vật tiếp xúc đạt **cân bằng nhiệt** khi không còn sự truyền nhiệt tự phát và có cùng nhiệt độ. Mối liên hệ giữa thang nhiệt độ tuyệt đối Kelvin ($T$) và thang Celsius ($t$): $T\text{ (K)} = t\text{ (}^\circ\text{C)} + 273{,}15$ (thông thường lấy $T\text{ (K)} = t\text{ (}^\circ\text{C)} + 273$). Độ biến thiên nhiệt độ trên hai thang là như nhau: $\Delta T\text{ (K)} = \Delta t\text{ (}^\circ\text{C)}$." "\n"
            r"- **Nhiệt dung riêng ($c$), nhiệt nóng chảy riêng ($\lambda$), nhiệt hoá hơi riêng ($L$)**: Nhiệt dung riêng $c$ (đơn vị $\text{J/(kg}\cdot\text{K)}$) là nhiệt lượng cần truyền cho $1\text{ kg}$ chất đó để nhiệt độ tăng thêm $1\text{ K}$. Nhiệt nóng chảy riêng $\lambda$ (đơn vị $\text{J/kg}$) là nhiệt lượng cần truyền cho $1\text{ kg}$ chất rắn kết tinh nóng chảy hoàn toàn ở nhiệt độ nóng chảy. Nhiệt hoá hơi riêng $L$ (đơn vị $\text{J/kg}$) là nhiệt lượng cần truyền cho $1\text{ kg}$ chất lỏng hoá hơi hoàn toàn ở nhiệt độ xác định."
        ),
        "theory": (
            r"### Bài 1. Cấu trúc của chất. Sự chuyển thể" "\n"
            r"- **Ba thể của chất**: Chất rắn có hình dạng và thể tích riêng xác định (chất rắn kết tinh có cấu trúc tinh thể và nhiệt độ nóng chảy xác định; chất rắn vô định hình không có cấu trúc tinh thể và không có nhiệt độ nóng chảy xác định). Chất lỏng có thể tích riêng xác định nhưng có hình dạng của phần bình chứa. Chất khí không có hình dạng và thể tích riêng, luôn chiếm toàn bộ thể tích bình chứa và dễ nén." "\n"
            r"- **Sự nóng chảy và sự đông đặc**: Trong suốt quá trình nóng chảy (hoặc đông đặc) của chất rắn kết tinh ở áp suất chuẩn, nhiệt độ của vật giữ **không đổi** dù vật vẫn tiếp tục thu nhiệt để phá vỡ liên kết mạng tinh thể (hoặc toả nhiệt khi tái lập mạng tinh thể)." "\n"
            r"- **Sự hoá hơi và sự ngưng tụ**: Hoá hơi xảy ra dưới hai hình thức: **bay hơi** (xảy ra ở mặt thoáng tại mọi nhiệt độ, tốc độ bay hơi tăng khi tăng nhiệt độ, tăng diện tích mặt thoáng, có gió và giảm độ ẩm) và **sôi** (xảy ra đồng thời ở cả trong lòng và trên mặt thoáng chất lỏng ở nhiệt độ sôi xác định). Trong suốt thời gian sôi, nhiệt độ của chất lỏng không đổi." "\n"
            r"### Bài 2. Nội năng. Định luật 1 của nhiệt động lực học" "\n"
            r"- **Hai cách làm thay đổi nội năng**: **Thực hiện công** (ví dụ cọ xát miếng kim loại, nén khí trong xilanh) và **truyền nhiệt** (cho vật tiếp xúc với nguồn nhiệt mà không có sự dịch chuyển vĩ mô do lực)." "\n"
            r"- **Định luật $1$ của nhiệt động lực học**: Độ biến thiên nội năng của hệ bằng tổng công và nhiệt lượng mà hệ nhận được: $\Delta U = Q + A$." "\n"
            r"- **Quy ước dấu**: $Q > 0$ (hệ nhận nhiệt), $Q < 0$ (hệ toả nhiệt); $A > 0$ (hệ nhận công), $A < 0$ (hệ sinh công); $\Delta U > 0$ (nội năng tăng), $\Delta U < 0$ (nội năng giảm)." "\n"
            r"### Bài 3. Nhiệt độ. Thang nhiệt độ – nhiệt kế" "\n"
            r"- **Sự truyền nhiệt và cân bằng nhiệt**: Năng lượng nhiệt tự truyền từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn. Khi hai vật đạt trạng thái cân bằng nhiệt thì nhiệt độ của chúng bằng nhau." "\n"
            r"- **Thang Celsius ($t$), Kelvin ($T$) và Fahrenheit ($T_{\text{F}}$)**: Điểm đóng băng và điểm sôi của nước tinh khiết ở áp suất $1\text{ atm}$ tương ứng là $0^\circ\text{C}$ ($273{,}15\text{ K}$) và $100^\circ\text{C}$ ($373{,}15\text{ K}$). Không độ tuyệt đối $0\text{ K}$ ($-273{,}15^\circ\text{C}$) là giới hạn nhiệt độ thấp nhất mà tại đó động năng chuyển động nhiệt của các phân tử đạt giá trị tối thiểu. Điểm ba của nước (nước tinh khiết đồng thời tồn tại ở cả ba thể rắn, lỏng, hơi) có nhiệt độ chính xác bằng $273{,}16\text{ K}$ ($0{,}01^\circ\text{C}$). Công thức đổi thang Fahrenheit: $T_{\text{F}}\text{ (}^\circ\text{F)} = 1{,}8t\text{ (}^\circ\text{C)} + 32$." "\n"
            r"- **Nguyên lí nhiệt kế**: Dựa trên sự phụ thuộc của một đại lượng vật lí vào nhiệt độ như sự nở vì nhiệt của cột chất lỏng (thuỷ ngân, rượu), sự biến thiên điện trở kim loại hoặc bán dẫn (nhiệt kế điện trở), hoặc bức xạ hồng ngoại (nhiệt kế hồng ngoại)." "\n"
            r"### Bài 4. Nhiệt dung riêng" "\n"
            r"- **Công thức tính nhiệt lượng làm thay đổi nhiệt độ**: $Q = mc\Delta T = mc(t_2 - t_1)$, trong đó $m$ ($\text{kg}$) là khối lượng, $c$ ($\text{J/(kg}\cdot\text{K)}$) là nhiệt dung riêng, $\Delta T$ ($\text{K}$ hoặc ${}^\circ\text{C}$) là độ tăng nhiệt độ. Tích $C = mc$ (đơn vị $\text{J/K}$) gọi là **nhiệt dung** của vật." "\n"
            r"- **Thí nghiệm đo nhiệt dung riêng của nước**: Đun nước có khối lượng $m$ trong bình nhiệt lượng kế bằng dây điện trở công suất $\mathcal{P}$ trong thời gian $\tau$; bỏ qua hao phí nhiệt ra môi trường thì $c = \dfrac{\mathcal{P}\tau}{m\Delta T}$." "\n"
            r"### Bài 5. Nhiệt nóng chảy riêng" "\n"
            r"- **Công thức tính nhiệt lượng nóng chảy**: Ở nhiệt độ nóng chảy $t_{\text{nc}}$, nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn khối chất rắn kết tinh có khối lượng $m$ là $Q = m\lambda$, với $\lambda$ ($\text{J/kg}$) là nhiệt nóng chảy riêng (của nước đá ở $0^\circ\text{C}$ là $\lambda \approx 3{,}34 \times 10^5\text{ J/kg}$)." "\n"
            r"### Bài 6. Nhiệt hoá hơi riêng" "\n"
            r"- **Công thức tính nhiệt lượng hoá hơi**: Ở nhiệt độ hoá hơi xác định, nhiệt lượng cần cung cấp để khối chất lỏng khối lượng $m$ hoá hơi hoàn toàn là $Q = mL$, với $L$ ($\text{J/kg}$) là nhiệt hoá hơi riêng (của nước ở $100^\circ\text{C}$ là $L \approx 2{,}26 \times 10^6\text{ J/kg}$)." "\n"
            r"### Bài 7. Bài tập về vật lí nhiệt" "\n"
            r"- **Phương trình cân bằng nhiệt**: Trong một hệ cô lập về nhiệt gồm các vật chỉ truyền nhiệt cho nhau, tổng nhiệt lượng do các vật có nhiệt độ cao hơn toả ra bằng tổng nhiệt lượng do các vật có nhiệt độ thấp hơn thu vào: $\sum Q_{\text{toả}} = \sum Q_{\text{thu}}$, hay $\sum Q_i = 0$." "\n"
            r"- **Bài toán nhiều giai đoạn (vừa tăng nhiệt độ vừa chuyển thể)**: Khi đun nước đá từ $t_1 < 0^\circ\text{C}$ thành hơi nước ở $100^\circ\text{C}$, tổng nhiệt lượng cần cung cấp là $Q = m c_{\text{đá}}(0 - t_1) + m\lambda + m c_{\text{nước}}(100 - 0) + mL$."
        ),
        "formulas": [
            G(
                "I. Định luật 1 Nhiệt động lực học và Thang nhiệt độ",
                F("Định luật 1 Nhiệt động lực học", r"$\Delta U = Q + A$", r"Nhận nhiệt $Q > 0$, truyền nhiệt $Q < 0$; nhận công $A > 0$, sinh công $A < 0$."),
                F("Chuyển đổi Celsius – Kelvin", r"$T\text{ (K)} = t\text{ (}^\circ\text{C)} + 273{,}15$", r"Độ chênh lệch nhiệt độ: $\Delta T\text{ (K)} = \Delta t\text{ (}^\circ\text{C)}$."),
                F("Chuyển đổi Celsius – Fahrenheit", r"$T_{\text{F}}\text{ (}^\circ\text{F)} = 1{,}8t\text{ (}^\circ\text{C)} + 32$", r"Độ chênh lệch: $\Delta T_{\text{F}} = 1{,}8\Delta t$."),
            ),
            G(
                "II. Nhiệt dung riêng, Nhiệt nóng chảy riêng và Nhiệt hoá hơi riêng",
                F("Nhiệt lượng thay đổi nhiệt độ", r"$Q = mc\Delta T = mc(t_2 - t_1)$", r"$c$ đo bằng $\text{J/(kg}\cdot\text{K)}$; $m$ đo bằng $\text{kg}$."),
                F("Nhiệt lượng nóng chảy (đông đặc)", r"$Q = m\lambda$", r"$\lambda$ đo bằng $\text{J/kg}$; xảy ra tại nhiệt độ nóng chảy $t_{\text{nc}}$."),
                F("Nhiệt lượng hoá hơi (ngưng tụ)", r"$Q = mL$", r"$L$ đo bằng $\text{J/kg}$; tính cho phần khối lượng $m$ đã hoá hơi."),
                F("Đo thực nghiệm bằng dòng điện", r"$Q = \mathcal{P}\tau = UI\tau \Rightarrow c = \dfrac{\mathcal{P}\tau}{m\Delta T}$", r"Áp dụng khi bỏ qua hao phí nhiệt; nếu hiệu suất là $H$ thì $Q_{\text{ích}} = H\mathcal{P}\tau$."),
            ),
            G(
                "III. Phương trình cân bằng nhiệt",
                F("Hệ cô lập về nhiệt", r"$Q_{\text{toả}} = Q_{\text{thu}}$", r"$Q_{\text{toả}} = m_1 c_1 (t_1 - t_{\text{cb}})$; $Q_{\text{thu}} = m_2 c_2 (t_{\text{cb}} - t_2)$."),
                F("Nhiệt độ cân bằng (hai vật không chuyển thể)", r"$t_{\text{cb}} = \dfrac{m_1 c_1 t_1 + m_2 c_2 t_2}{m_1 c_1 + m_2 c_2}$", r"Với $t_1 > t_{\text{cb}} > t_2$."),
            ),
        ],
        "example": (
            r"Một ấm điện có công suất $\mathcal{P} = 1500\text{ W}$ và hiệu suất đun là $H = 84\%$ dùng để đun một khối nước đá "
            r"có khối lượng $m = 0{,}5\text{ kg}$ ở nhiệt độ ban đầu $t_0 = -10^\circ\text{C}$ cho đến khi nước sôi và có $20\%$ khối lượng nước đã hoá hơi ở $100^\circ\text{C}$. "
            r"Biết nhiệt dung riêng của nước đá là $c_1 = 2100\text{ J/(kg}\cdot\text{K)}$, của nước là $c_2 = 4200\text{ J/(kg}\cdot\text{K)}$, "
            r"nhiệt nóng chảy riêng của nước đá là $\lambda = 3{,}34 \times 10^5\text{ J/kg}$ và nhiệt hoá hơi riêng của nước ở $100^\circ\text{C}$ là $L = 2{,}26 \times 10^6\text{ J/kg}$. "
            r"Tính tổng nhiệt lượng có ích cần cung cấp và thời gian đun $\tau$."
        ),
        "example_answer": (
            r"- **Giai đoạn 1** (tăng nhiệt độ nước đá từ $-10^\circ\text{C}$ đến $0^\circ\text{C}$): $Q_1 = m c_1 \Delta t_1 = 0{,}5 \cdot 2100 \cdot 10 = 10\,500\text{ J}$." "\n"
            r"- **Giai đoạn 2** (nóng chảy hoàn toàn ở $0^\circ\text{C}$): $Q_2 = m\lambda = 0{,}5 \cdot 3{,}34 \times 10^5 = 167\,000\text{ J}$." "\n"
            r"- **Giai đoạn 3** (đun nước từ $0^\circ\text{C}$ đến $100^\circ\text{C}$): $Q_3 = m c_2 \Delta t_2 = 0{,}5 \cdot 4200 \cdot 100 = 210\,000\text{ J}$." "\n"
            r"- **Giai đoạn 4** (hoá hơi $20\%$ khối lượng nước, tức $\Delta m = 0{,}2 \cdot 0{,}5 = 0{,}1\text{ kg}$ ở $100^\circ\text{C}$): $Q_4 = \Delta m \cdot L = 0{,}1 \cdot 2{,}26 \times 10^6 = 226\,000\text{ J}$." "\n"
            r"- **Tổng nhiệt lượng có ích**: $Q_{\text{ích}} = Q_1 + Q_2 + Q_3 + Q_4 = 10\,500 + 167\,000 + 210\,000 + 226\,000 = \mathbf{613\,500\text{ J}} = \mathbf{613{,}5\text{ kJ}}$." "\n"
            r"- **Thời gian đun**: Từ $Q_{\text{ích}} = H\mathcal{P}\tau \Rightarrow \tau = \dfrac{Q_{\text{ích}}}{H\mathcal{P}} = \dfrac{613\,500}{0{,}84 \cdot 1500} = \dfrac{613\,500}{1260} \approx \mathbf{486{,}9\text{ s}}$ (khoảng $8\text{ phút } 7\text{ giây}$)."
        ),
        "real_life": (
            r"- **Hệ thống làm mát động cơ và điều hoà nhiệt độ**: Nước có nhiệt dung riêng lớn ($c \approx 4200\text{ J/(kg}\cdot\text{K)}$) nên được dùng làm chất tải nhiệt trong két làm mát ô tô và hệ thống sưởi ấm; máy điều hoà và tủ lạnh hoạt động dựa trên quá trình bay hơi thu nhiệt và ngưng tụ toả nhiệt của môi chất lạnh." "\n"
            r"- **Công nghệ luyện kim và đúc đồng, gang, thép**: Tính toán chính xác nhiệt lượng cần cung cấp theo nhiệt dung riêng $c$ và nhiệt nóng chảy riêng $\lambda$ của kim loại để vận hành lò nung cảm ứng tiết kiệm năng lượng." "\n"
            r"- **Sản xuất muối và chưng cất nước tinh khiết**: Ứng dụng sự bay hơi tự nhiên trên ruộng muối và quá trình sôi – ngưng tụ để chưng cất nước cất y tế, tinh dầu thực vật."
        ),
        "game_title": "Phòng thí nghiệm Vật lí Nhiệt và Chuyển thể",
        "game_description": "Thực hành đo nhiệt dung riêng, khảo sát đồ thị nhiệt độ theo thời gian khi đun nóng chảy nước đá tới khi nước sôi và kiểm chứng Định luật 1 nhiệt động lực học.",
        "game_type": "game_vat_ly_nhiet_khi_ly_tuong",
        "quiz": [
            mcq(
                "biet",
                r"Theo mô hình động học phân tử, ở thể nào các phân tử dao động xung quanh các vị trí cân bằng cố định và có trật tự xác định?",
                [
                    r"Thể rắn kết tinh",
                    r"Thể lỏng",
                    r"Thể khí",
                    r"Thể plasma",
                ],
                0,
                r"Ở **thể rắn kết tinh**, lực tương tác phân tử rất mạnh giữ các hạt dao động quanh các vị trí cân bằng cố định tạo thành mạng tinh thể.",
            ),
            mcq(
                "biet",
                r"Hệ thức của Định luật $1$ của nhiệt động lực học là $\Delta U = Q + A$. Trong quá trình chất khí nhận nhiệt lượng và thực hiện công thì dấu của $Q$ và $A$ là:",
                [
                    r"$Q > 0$ và $A < 0$",
                    r"$Q > 0$ và $A > 0$",
                    r"$Q < 0$ và $A > 0$",
                    r"$Q < 0$ và $A < 0$",
                ],
                0,
                r"Theo quy ước dấu của Định luật $1$ nhiệt động lực học: hệ nhận nhiệt lượng nên $Q > 0$; hệ thực hiện công (sinh công) nên $A < 0$.",
            ),
            mcq(
                "biet",
                r"Đơn vị đo của nhiệt dung riêng $c$, nhiệt nóng chảy riêng $\lambda$ và nhiệt hoá hơi riêng $L$ trong hệ SI lần lượt là:",
                [
                    r"$\text{J/(kg}\cdot\text{K)}$, $\text{J/kg}$ và $\text{J/kg}$",
                    r"$\text{J/kg}$, $\text{J/(kg}\cdot\text{K)}$ và $\text{J/K}$",
                    r"$\text{J/K}$, $\text{J/kg}$ và $\text{W/kg}$",
                    r"$\text{cal/g}$, $\text{J/mol}$ và $\text{J/(kg}\cdot\text{K)}$",
                ],
                0,
                r"Từ $c = \dfrac{Q}{m\Delta T}$ suy ra đơn vị của $c$ là $\text{J/(kg}\cdot\text{K)}$; từ $\lambda = \dfrac{Q}{m}$ và $L = \dfrac{Q}{m}$ suy ra đơn vị của $\lambda$ và $L$ đều là $\text{J/kg}$.",
            ),
            mcq(
                "biet",
                r"Nhiệt độ của một vật trên thang Celsius là $t = 37^\circ\text{C}$. Nhiệt độ tương ứng trên thang Kelvin (lấy $T\text{ (K)} = t\text{ (}^\circ\text{C)} + 273{,}15$) là:",
                [
                    r"$310{,}15\text{ K}$",
                    r"$236{,}15\text{ K}$",
                    r"$300{,}15\text{ K}$",
                    r"$337{,}15\text{ K}$",
                ],
                0,
                r"Áp dụng công thức $T = t + 273{,}15 = 37 + 273{,}15 = \mathbf{310{,}15\text{ K}}$.",
            ),
            mcq(
                "hieu",
                r"Trong một quá trình nén khí, người ta thực hiện công $A = 450\text{ J}$ lên khối khí, đồng thời khối khí truyền ra môi trường xung quanh nhiệt lượng $150\text{ J}$. Độ biến thiên nội năng $\Delta U$ của khối khí là:",
                [
                    r"$\Delta U = 300\text{ J}$",
                    r"$\Delta U = 600\text{ J}$",
                    r"$\Delta U = -300\text{ J}$",
                    r"$\Delta U = -600\text{ J}$",
                ],
                0,
                r"Khí nhận công nên $A = +450\text{ J}$; khí truyền nhiệt ra ngoài nên $Q = -150\text{ J}$. Theo Định luật $1$ NĐLH: $\Delta U = Q + A = -150 + 450 = \mathbf{300\text{ J}}$ (nội năng tăng $300\text{ J}$).",
            ),
            mcq(
                "hieu",
                r"Cần cung cấp nhiệt lượng bằng bao nhiêu để làm nóng chảy hoàn toàn một cục nước đá khối lượng $m = 200\text{ g}$ đang ở nhiệt độ $0^\circ\text{C}$? Biết nhiệt nóng chảy riêng của nước đá là $\lambda = 3{,}34 \times 10^5\text{ J/kg}$.",
                [
                    r"$66{,}8\text{ kJ}$",
                    r"$668\text{ kJ}$",
                    r"$33{,}4\text{ kJ}$",
                    r"$16{,}7\text{ kJ}$",
                ],
                0,
                r"Đổi $m = 200\text{ g} = 0{,}2\text{ kg}$. Nhiệt lượng cần cung cấp: $Q = m\lambda = 0{,}2 \cdot 3{,}34 \times 10^5 = 66\,800\text{ J} = \mathbf{66{,}8\text{ kJ}}$.",
            ),
            tf4(
                "hieu",
                r"Xét tính đúng hay sai của các phát biểu sau về sự chuyển thể, nội năng và các thang nhiệt độ:",
                [
                    r"a) Trong suốt quá trình nóng chảy của chất rắn kết tinh ở áp suất tiêu chuẩn, vật tiếp tục thu nhiệt nhưng nhiệt độ của vật không thay đổi.",
                    r"b) Khi nhiệt độ của một vật tăng thêm $25^\circ\text{C}$ thì trên thang Kelvin nhiệt độ của vật đó tăng thêm $298{,}15\text{ K}$.",
                    r"c) Nội năng của một vật phụ thuộc vào nhiệt độ và thể tích của vật, không phải là nhiệt lượng mà vật có được.",
                    r"d) Sự sôi là sự hoá hơi chỉ xảy ra trên bề mặt thoáng của chất lỏng ở một nhiệt độ bất kì.",
                ],
                [True, False, True, False],
                r"- **a) Đúng**: Nhiệt lượng cung cấp trong suốt quá trình nóng chảy dùng để phá vỡ mạng tinh thể nên nhiệt độ không đổi." "\n"
                r"- **b) Sai**: Độ biến thiên nhiệt độ trên hai thang bằng nhau: $\Delta T\text{ (K)} = \Delta t\text{ (}^\circ\text{C)} = 25\text{ K}$." "\n"
                r"- **c) Đúng**: Nội năng $U$ là hàm trạng thái phụ thuộc vào $T$ và $V$; còn nhiệt lượng $Q$ chỉ là số đo độ biến thiên nội năng trong quá trình truyền nhiệt." "\n"
                r"- **d) Sai**: Sự sôi xảy ra đồng thời cả trong lòng và trên mặt thoáng của chất lỏng ở nhiệt độ sôi xác định (còn bay hơi mới xảy ra ở mặt thoáng tại mọi nhiệt độ).",
            ),
            tf4(
                "hieu",
                r"Một học sinh dùng ấm đun siêu tốc công suất $\mathcal{P} = 1800\text{ W}$ để đun $m = 1{,}5\text{ kg}$ nước từ $t_1 = 20^\circ\text{C}$ đến khi sôi ở $t_2 = 100^\circ\text{C}$. Cho nhiệt dung riêng của nước $c = 4200\text{ J/(kg}\cdot\text{K)}$ và nhiệt hoá hơi riêng của nước ở $100^\circ\text{C}$ là $L = 2{,}26 \times 10^6\text{ J/kg}$. Xét các nhận định sau:",
                [
                    r"a) Nhiệt lượng có ích mà nước thu vào để tăng nhiệt độ từ $20^\circ\text{C}$ đến $100^\circ\text{C}$ là $Q_1 = 504\text{ kJ}$.",
                    r"b) Nếu bỏ qua mọi hao phí nhiệt thì thời gian đun nước từ $20^\circ\text{C}$ tới khi bắt đầu sôi ở $100^\circ\text{C}$ là $280\text{ s}$.",
                    r"c) Nếu hiệu suất của ấm đun là $H = 80\%$ thì thời gian thực tế để đun sôi lượng nước trên là $224\text{ s}$.",
                    r"d) Sau khi nước đã đạt $100^\circ\text{C}$, để làm hoá hơi thêm $100\text{ g}$ nước thì nước cần thu thêm nhiệt lượng $Q_2 = 226\text{ kJ}$.",
                ],
                [True, True, False, True],
                r"- **a) Đúng**: $Q_1 = mc(t_2 - t_1) = 1{,}5 \cdot 4200 \cdot (100 - 20) = 504\,000\text{ J} = 504\text{ kJ}$." "\n"
                r"- **b) Đúng**: Khi hiệu suất $100\%$, thời gian đun là $\tau_0 = \dfrac{Q_1}{\mathcal{P}} = \dfrac{504\,000}{1800} = 280\text{ s}$." "\n"
                r"- **c) Sai**: Khi hiệu suất $H = 80\%$, thời gian thực tế phải dài hơn: $\tau = \dfrac{Q_1}{H\mathcal{P}} = \dfrac{504\,000}{0{,}8 \cdot 1800} = 350\text{ s}$ (không phải $224\text{ s}$)." "\n"
                r"- **d) Đúng**: Với $\Delta m = 100\text{ g} = 0{,}1\text{ kg}$, nhiệt lượng hoá hơi là $Q_2 = \Delta m \cdot L = 0{,}1 \cdot 2{,}26 \times 10^6 = 226\,000\text{ J} = 226\text{ kJ}$.",
            ),
            mcq(
                "vandung",
                r"Thả một quả cầu bằng đồng có khối lượng $m_1 = 0{,}6\text{ kg}$ được nung nóng tới $t_1 = 120^\circ\text{C}$ vào một bình cách nhiệt chứa $m_2 = 0{,}5\text{ kg}$ nước ở nhiệt độ $t_2 = 20^\circ\text{C}$. Bỏ qua sự trao đổi nhiệt với bình và môi trường. Biết nhiệt dung riêng của đồng là $c_1 = 380\text{ J/(kg}\cdot\text{K)}$ và của nước là $c_2 = 4200\text{ J/(kg}\cdot\text{K)}$. Nhiệt độ khi có sự cân bằng nhiệt gần nhất với giá trị nào sau đây?",
                [
                    r"$29{,}8^\circ\text{C}$",
                    r"$35{,}4^\circ\text{C}$",
                    r"$24{,}6^\circ\text{C}$",
                    r"$70{,}0^\circ\text{C}$",
                ],
                0,
                r"Phương trình cân bằng nhiệt: $m_1 c_1 (t_1 - t) = m_2 c_2 (t - t_2) \Rightarrow t = \dfrac{m_1 c_1 t_1 + m_2 c_2 t_2}{m_1 c_1 + m_2 c_2} = \dfrac{0{,}6 \cdot 380 \cdot 120 + 0{,}5 \cdot 4200 \cdot 20}{0{,}6 \cdot 380 + 0{,}5 \cdot 4200} = \dfrac{27\,360 + 42\,000}{228 + 2100} = \dfrac{69\,360}{2328} \approx \mathbf{29{,}8^\circ\text{C}}$.",
            ),
            short(
                "vandung",
                r"Người ta bỏ một cục nước đá khối lượng $m_1 = 100\text{ g}$ ở $t_1 = 0^\circ\text{C}$ vào một bình cách nhiệt chứa $m_2 = 400\text{ g}$ nước ở $t_2 = 35^\circ\text{C}$. Cho nhiệt nóng chảy riêng của nước đá $\lambda = 3{,}36 \times 10^5\text{ J/kg}$ và nhiệt dung riêng của nước $c = 4200\text{ J/(kg}\cdot\text{K)}$. Bỏ qua nhiệt dung của bình. Tính nhiệt độ cân bằng cuối cùng của hỗn hợp theo đơn vị ${}^\circ\text{C}$.",
                ["12"],
                r"Đổi $m_1 = 0{,}1\text{ kg}$, $m_2 = 0{,}4\text{ kg}$. Nhiệt lượng cần để nước đá tan hết ở $0^\circ\text{C}$ là $Q_{\text{nc}} = m_1\lambda = 0{,}1 \cdot 3{,}36 \times 10^5 = 33\,600\text{ J}$. "
                r"Nhiệt lượng tối đa mà $0{,}4\text{ kg}$ nước ở $35^\circ\text{C}$ toả ra khi hạ về $0^\circ\text{C}$ là $Q_{\max} = m_2 c t_2 = 0{,}4 \cdot 4200 \cdot 35 = 58\,800\text{ J} > Q_{\text{nc}}$, nên nước đá tan hết. "
                r"Phương trình cân bằng nhiệt: $m_1\lambda + m_1 c(t - 0) = m_2 c(35 - t) \Rightarrow 33\,600 + 0{,}1 \cdot 4200 \cdot t = 58\,800 - 0{,}4 \cdot 4200 \cdot t \Rightarrow 2100t = 25\,200 \Rightarrow t = \mathbf{12}^\circ\text{C}$.",
                unit=r"${}^\circ\text{C}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG II. KHÍ LÍ TƯỞNG (Bài 8 – Bài 13 SGK Vật lí 12 KNTT)
    # =========================================================================
    {
        "topic": "vat-ly-nhiet-khi-ly-tuong",
        "title": "Chương II. Khí lí tưởng",
        "icon": "🎈",
        "description": (
            "Chương II · SGK Vật lí 12 Kết nối tri thức với cuộc sống (Bài 8 – Bài 13): "
            "Mô hình động học phân tử chất khí; Định luật Boyle (quá trình đẳng nhiệt); "
            "Định luật Charles (quá trình đẳng áp); Phương trình trạng thái của khí lí tưởng và phương trình Clapeyron; "
            "Áp suất khí theo mô hình động học phân tử và quan hệ giữa động năng phân tử với nhiệt độ; Bài tập về khí lí tưởng."
        ),
        "requirements": [
            r"Phân tích kết quả thí nghiệm chuyển động Brown để rút ra được các phân tử chất khí chuyển động hỗn loạn, không ngừng và nhiệt độ càng cao thì tốc độ chuyển động của các phân tử khí càng lớn.",
            r"Nêu được các giả thuyết của thuyết động học phân tử chất khí và định nghĩa mô hình khí lí tưởng.",
            r"Thực hiện thí nghiệm khảo sát định luật Boyle: nêu được mối hệ tỉ lệ nghịch giữa áp suất $p$ và thể tích $V$ của một khối lượng khí xác định khi giữ nhiệt độ không đổi ($pV = \text{hằng số}$, hay $p_1 V_1 = p_2 V_2$).",
            r"Thực hiện thí nghiệm minh hoạ định luật Charles: khi giữ áp suất của một khối lượng khí xác định không đổi thì thể tích $V$ của khí tỉ lệ thuận với nhiệt độ tuyệt đối $T$ của nó ($\dfrac{V}{T} = \text{hằng số}$, hay $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$).",
            r"Sử dụng định luật Boyle và định luật Charles rút ra được phương trình trạng thái của một lượng khí lí tưởng xác định $\dfrac{pV}{T} = \text{hằng số}$ và phương trình Clapeyron $pV = nRT$.",
            r"Vận dụng được phương trình trạng thái của khí lí tưởng $\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}$ và phương trình Clapeyron $pV = nRT$ để giải quyết các bài toán thực tế.",
            r"Giải thích được chuyển động của các phân tử khí ảnh hưởng như thế nào đến áp suất tác dụng lên thành bình và từ đó rút ra được hệ thức $p = \dfrac{1}{3}\mu m\overline{v^2} = \dfrac{2}{3}\mu \overline{W_{\text{đ}}}$ với $\mu = \dfrac{N}{V}$ là mật độ phân tử.",
            r"Nêu được biểu thức hằng số Boltzmann $k = \dfrac{R}{N_{\text{A}}}$, rút ra được động năng tịnh tiến trung bình của phân tử khí tỉ lệ thuận với nhiệt độ tuyệt đối $T$ theo hệ thức $\overline{W_{\text{đ}}} = \dfrac{3}{2}kT$ và vận dụng được hệ thức này.",
        ],
        "definition": (
            r"- **Mô hình khí lí tưởng**: Là chất khí tuân theo đúng các giả thuyết: các phân tử khí được coi là các chất điểm (bỏ qua thể tích riêng so với thể tích bình chứa), chỉ tương tác với nhau và với thành bình khi va chạm hoàn toàn đàn hồi. Ba thông số trạng thái của một lượng khí xác định là **áp suất** $p$ ($\text{Pa}$, $\text{atm}$, $\text{mmHg}$), **thể tích** $V$ ($\text{m}^3$, $\text{L}$) và **nhiệt độ tuyệt đối** $T$ ($\text{K}$)." "\n"
            r"- **Định luật Boyle (quá trình đẳng nhiệt, $T = \text{hằng số}$)**: Với một khối lượng khí xác định ở nhiệt độ không đổi, áp suất $p$ tỉ lệ nghịch với thể tích $V$: $pV = \text{hằng số}$, hay $p_1 V_1 = p_2 V_2$. Đường đẳng nhiệt trong hệ toạ độ $(p, V)$ là một nhánh đường hyperbol." "\n"
            r"- **Định luật Charles (quá trình đẳng áp, $p = \text{hằng số}$)**: Với một khối lượng khí xác định ở áp suất không đổi, thể tích $V$ tỉ lệ thuận với nhiệt độ tuyệt đối $T$: $\dfrac{V}{T} = \text{hằng số}$, hay $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$." "\n"
            r"- **Phương trình trạng thái khí lí tưởng và phương trình Clapeyron**: Với một lượng khí xác định: $\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2} = \text{hằng số}$. Với $n = \dfrac{m}{M} = \dfrac{N}{N_{\text{A}}}$ mol khí lí tưởng: $pV = nRT$, trong đó $R \approx 8{,}31\text{ J/(mol}\cdot\text{K)}$." "\n"
            r"- **Áp suất phân tử và Động năng tịnh tiến trung bình**: $p = \dfrac{1}{3}\mu m\overline{v^2} = \dfrac{2}{3}\mu\overline{W_{\text{đ}}}$ và $\overline{W_{\text{đ}}} = \dfrac{1}{2}m\overline{v^2} = \dfrac{3}{2}kT$, với hằng số Boltzmann $k = \dfrac{R}{N_{\text{A}}} \approx 1{,}38 \times 10^{-23}\text{ J/K}$."
        ),
        "theory": (
            r"### Bài 8. Mô hình động học phân tử chất khí" "\n"
            r"- **Chuyển động Brown**: Là chuyển động hỗn loạn, không ngừng, có quỹ đạo là những đường gấp khúc bất kì của các hạt rất nhỏ (hạt phấn hoa, hạt khói) lơ lửng trong chất lỏng hoặc chất khí, do các phân tử môi trường chuyển động nhiệt va chạm không cân bằng từ mọi phía." "\n"
            r"- **Ba nội dung của thuyết động học phân tử chất khí**: (1) Chất khí được cấu tạo từ các phân tử có kích thước rất nhỏ so với khoảng cách giữa chúng; (2) Các phân tử khí chuyển động hỗn loạn không ngừng, nhiệt độ càng cao thì tốc độ trung bình càng lớn; (3) Khi chuyển động hỗn loạn, các phân tử khí va chạm vào nhau và va chạm vào thành bình gây ra áp suất chất khí lên thành bình." "\n"
            r"### Bài 9. Định luật Boyle" "\n"
            r"- **Quá trình đẳng nhiệt**: Là quá trình biến đổi trạng thái trong đó nhiệt độ tuyệt đối $T$ được giữ không đổi." "\n"
            r"- **Định luật Boyle**: $p_1 V_1 = p_2 V_2$. Trong hệ toạ độ $(p, V)$, đường đẳng nhiệt ứng với nhiệt độ cao hơn ($T_2 > T_1$) nằm phía trên đường đẳng nhiệt ứng với nhiệt độ thấp hơn. Trong hệ toạ độ $(p, T)$ hoặc $(V, T)$, đường đẳng nhiệt là đoạn thẳng vuông góc với trục $OT$." "\n"
            r"### Bài 10. Định luật Charles" "\n"
            r"- **Quá trình đẳng áp**: Là quá trình biến đổi trạng thái trong đó áp suất $p$ được giữ không đổi." "\n"
            r"- **Định luật Charles**: $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$. Trong hệ toạ độ $(V, T)$, đường đẳng áp là đường thẳng có đường kéo dài đi qua gốc toạ độ tuyệt đối $O(0\text{ K}, 0)$; ứng với áp suất lớn hơn ($p_2 > p_1$) thì hệ số góc $\dfrac{nR}{p}$ nhỏ hơn nên đường đẳng áp nằm gần trục $OT$ hơn." "\n"
            r"### Bài 11. Phương trình trạng thái của khí lí tưởng" "\n"
            r"- **Phương trình trạng thái**: Kết hợp định luật Boyle và định luật Charles qua trạng thái trung gian, ta thu được $\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}$. Hệ quả cho quá trình **đẳng tích** ($V = \text{hằng số}$): $\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}$." "\n"
            r"- **Phương trình Clapeyron**: $pV = nRT = \dfrac{m}{M}RT$, suy ra khối lượng riêng của khí $\rho = \dfrac{m}{V} = \dfrac{pM}{RT}$. Nếu lấy $p$ tính theo $\text{Pa}$ ($\text{N/m}^2$), $V$ tính theo $\text{m}^3$, $T$ tính theo $\text{K}$ thì $R \approx 8{,}31\text{ J/(mol}\cdot\text{K)}$; nếu lấy $p$ tính theo $\text{atm}$ và $V$ tính theo $\text{L}$ thì $R \approx 0{,}082\text{ atm}\cdot\text{L/(mol}\cdot\text{K)}$." "\n"
            r"### Bài 12. Áp suất khí theo mô hình động học phân tử. Quan hệ giữa động năng phân tử và nhiệt độ" "\n"
            r"- **Công thức áp suất khí theo mô hình động học phân tử**: $p = \dfrac{1}{3}\mu m\overline{v^2} = \dfrac{2}{3}\mu\overline{W_{\text{đ}}}$, trong đó $\mu = \dfrac{N}{V}$ ($\text{m}^{-3}$) là mật độ phân tử, $m$ ($\text{kg}$) là khối lượng một phân tử khí, $\overline{v^2}$ là trung bình của bình phương tốc độ phân tử và $\overline{W_{\text{đ}}} = \dfrac{1}{2}m\overline{v^2}$ là động năng tịnh tiến trung bình của một phân tử." "\n"
            r"- **Liên hệ giữa động năng phân tử và nhiệt độ tuyệt đối**: Kết hợp $pV = nRT = N k T$ (với $k = \dfrac{R}{N_{\text{A}}} \approx 1{,}38 \times 10^{-23}\text{ J/K}$) và $pV = \dfrac{2}{3}N\overline{W_{\text{đ}}}$, ta suy ra $\overline{W_{\text{đ}}} = \dfrac{3}{2}kT$ và $p = \mu k T$. Căn bậc hai của $\overline{v^2}$ là tốc độ căn quân phương $v_{\text{rms}} = \sqrt{\overline{v^2}} = \sqrt{\dfrac{3kT}{m}} = \sqrt{\dfrac{3RT}{M}}$." "\n"
            r"### Bài 13. Bài tập về khí lí tưởng" "\n"
            r"- **Phương pháp giải bài toán khí lí tưởng**: (1) Xác định lượng khí có không đổi hay có sự nạp thêm hoặc thoát bớt khí; (2) Liệt kê các thông số trạng thái $(p_1, V_1, T_1)$ và $(p_2, V_2, T_2)$ với $T$ bắt buộc đổi sang đơn vị Kelvin ($\text{K}$); (3) Áp dụng định luật đẳng quá trình hoặc phương trình trạng thái $\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}$ hoặc phương trình Clapeyron $pV = nRT$."
        ),
        "formulas": [
            G(
                "I. Các đẳng quá trình của một lượng khí xác định",
                F(r"Định luật Boyle (đẳng nhiệt $T = \text{hằng số}$)", r"$p_1 V_1 = p_2 V_2$", r"Áp suất $p$ tỉ lệ nghịch với thể tích $V$."),
                F(r"Định luật Charles (đẳng áp $p = \text{hằng số}$)", r"$\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$", r"Thể tích $V$ tỉ lệ thuận với nhiệt độ tuyệt đối $T\text{ (K)}$."),
                F(r"Quá trình đẳng tích ($V = \text{hằng số}$)", r"$\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}$", r"Áp suất $p$ tỉ lệ thuận với nhiệt độ tuyệt đối $T\text{ (K)}$."),
            ),
            G(
                "II. Phương trình trạng thái và Phương trình Clapeyron",
                F("Phương trình trạng thái khí lí tưởng", r"$\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2} = \text{hằng số}$", r"Áp dụng cho một khối lượng khí không đổi."),
                F("Phương trình Clapeyron", r"$pV = nRT = \dfrac{m}{M}RT$", r"$R \approx 8{,}31\text{ J/(mol}\cdot\text{K)}$ khi $p$ ($\text{Pa}$), $V$ ($\text{m}^3$), $T$ ($\text{K}$)."),
                F("Đổi đơn vị áp suất và thể tích", r"$1\text{ atm} = 101\,325\text{ Pa} \approx 760\text{ mmHg}$", r"$1\text{ bar} = 10^5\text{ Pa}$; $1\text{ L} = 1\text{ dm}^3 = 10^{-3}\text{ m}^3$."),
            ),
            G(
                "III. Áp suất vi mô và Động năng tịnh tiến phân tử",
                F("Áp suất khí theo mô hình phân tử", r"$p = \dfrac{1}{3}\mu m\overline{v^2} = \dfrac{2}{3}\mu\overline{W_{\text{đ}}} = \mu k T$", r"$\mu = \dfrac{N}{V}$ là mật độ phân tử ($\text{hạt/m}^3$)."),
                F("Động năng tịnh tiến trung bình", r"$\overline{W_{\text{đ}}} = \dfrac{3}{2}kT$", r"$k = \dfrac{R}{N_{\text{A}}} \approx 1{,}38 \times 10^{-23}\text{ J/K}$."),
                F("Tốc độ căn quân phương", r"$v_{\text{rms}} = \sqrt{\overline{v^2}} = \sqrt{\dfrac{3kT}{m}} = \sqrt{\dfrac{3RT}{M}}$", r"$M$ trong công thức này đổi ra đơn vị $\text{kg/mol}$."),
            ),
        ],
        "example": (
            r"Một bình kín có dung tích $V = 16{,}62\text{ L}$ chứa khí helium ($\text{He}$, có khối lượng mol $M = 4\text{ g/mol}$) ở áp suất $p_1 = 3 \times 10^5\text{ Pa}$ và nhiệt độ $t_1 = 27^\circ\text{C}$. "
            r"Lấy $R = 8{,}31\text{ J/(mol}\cdot\text{K)}$ và $k = 1{,}38 \times 10^{-23}\text{ J/K}$. "
            r"a) Tính số mol $n$ và khối lượng $m$ của khí helium trong bình. "
            r"b) Khi đun nóng bình tới nhiệt độ $t_2 = 127^\circ\text{C}$ (bỏ qua sự nở vì nhiệt của bình), hãy tính áp suất $p_2$ và động năng tịnh tiến trung bình $\overline{W_{\text{đ}}}$ của mỗi phân tử khí helium ở trạng thái này."
        ),
        "example_answer": (
            r"- **Câu a**: Đổi $V = 16{,}62\text{ L} = 16{,}62 \times 10^{-3}\text{ m}^3$; $T_1 = 27 + 273 = 300\text{ K}$." "\n"
            r"  Áp dụng phương trình Clapeyron: $n = \dfrac{p_1 V}{RT_1} = \dfrac{3 \times 10^5 \cdot 16{,}62 \times 10^{-3}}{8{,}31 \cdot 300} = \mathbf{2\text{ mol}}$." "\n"
            r"  Khối lượng khí helium trong bình: $m = nM = 2 \cdot 4 = \mathbf{8\text{ g}}$." "\n"
            r"- **Câu b**: Đổi $T_2 = 127 + 273 = 400\text{ K}$. Vì bình kín có thể tích không đổi ($V = \text{hằng số}$) nên:" "\n"
            r"  $p_2 = p_1 \dfrac{T_2}{T_1} = 3 \times 10^5 \cdot \dfrac{400}{300} = \mathbf{4 \times 10^5\text{ Pa}}$." "\n"
            r"  Động năng tịnh tiến trung bình của mỗi phân tử khí ở $T_2 = 400\text{ K}$ là:" "\n"
            r"  $\overline{W_{\text{đ}}} = \dfrac{3}{2}kT_2 = 1{,}5 \cdot 1{,}38 \times 10^{-23} \cdot 400 = \mathbf{8{,}28 \times 10^{-21}\text{ J}}$."
        ),
        "real_life": (
            r"- **Bình dưỡng khí lặn biển và bình oxy y tế**: Nén khí ở áp suất cao (theo định luật Boyle) để tích trữ một lượng lớn khí trong thể tích bình nhỏ gọn." "\n"
            r"- **Lốp xe ô tô và an toàn giao thông mùa hè**: Khi xe chạy đường dài dưới trời nắng nóng, nhiệt độ khí trong lốp tăng làm áp suất tăng theo hệ thức $\dfrac{p}{T} = \text{hằng số}$, do đó cảm biến áp suất lốp (TPMS) giúp cảnh báo nguy cơ nổ lốp." "\n"
            r"- **Khinh khí cầu và bóng thám không khí tượng**: Khi đốt nóng không khí trong vòm khinh khí cầu ở áp suất khí quyển (định luật Charles), khí nở ra và giảm khối lượng riêng $\rho = \dfrac{pM}{RT}$ giúp lực đẩy Archimedes nâng khinh khí cầu bay lên."
        ),
        "game_title": "Mô phỏng Động học Phân tử và Trạng thái Khí lí tưởng",
        "game_description": "Thay đổi thể tích pít-tông, nhiệt độ nguồn nhiệt và số hạt phân tử để quan sát chuyển động va chạm vi mô và vẽ đồ thị đẳng nhiệt Boyle, đẳng áp Charles.",
        "game_type": "game_vat_ly_nhiet_khi_ly_tuong",
        "quiz": [
            mcq(
                "biet",
                r"Hệ thức nào sau đây biểu diễn đúng định luật Boyle đối với một khối lượng khí lí tưởng xác định ở nhiệt độ không đổi?",
                [
                    r"$p_1 V_1 = p_2 V_2$",
                    r"$\dfrac{p_1}{V_1} = \dfrac{p_2}{V_2}$",
                    r"$\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$",
                    r"$\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}$",
                ],
                0,
                r"Theo định luật Boyle, trong quá trình đẳng nhiệt ($T = \text{hằng số}$), áp suất tỉ lệ nghịch với thể tích: $p_1 V_1 = p_2 V_2$.",
            ),
            mcq(
                "biet",
                r"Trong hệ toạ độ $(V, T)$ với $T$ là nhiệt độ tuyệt đối, đường đẳng áp của một lượng khí lí tưởng xác định có dạng là:",
                [
                    r"Đường thẳng mà đường kéo dài đi qua gốc toạ độ $O$",
                    r"Một nhánh của đường hyperbol",
                    r"Đường thẳng song song với trục nhiệt độ $OT$",
                    r"Đường parabol có đỉnh tại gốc toạ độ $O$",
                ],
                0,
                r"Theo định luật Charles, khi $p = \text{hằng số}$ thì $V = \left(\dfrac{nR}{p}\right)T$, nên đồ thị $(V, T)$ là đường thẳng có đường kéo dài đi qua gốc toạ độ tuyệt đối $O$.",
            ),
            mcq(
                "biet",
                r"Động năng tịnh tiến trung bình $\overline{W_{\text{đ}}}$ của các phân tử khí lí tưởng ở nhiệt độ tuyệt đối $T$ được xác định bởi công thức nào sau đây (với $k$ là hằng số Boltzmann)?",
                [
                    r"$\overline{W_{\text{đ}}} = \dfrac{3}{2}kT$",
                    r"$\overline{W_{\text{đ}}} = \dfrac{2}{3}kT$",
                    r"$\overline{W_{\text{đ}}} = \dfrac{1}{3}kT$",
                    r"$\overline{W_{\text{đ}}} = 3kT$",
                ],
                0,
                r"Động năng tịnh tiến trung bình của phân tử khí lí tưởng tỉ lệ thuận với nhiệt độ tuyệt đối: $\overline{W_{\text{đ}}} = \dfrac{3}{2}kT$.",
            ),
            mcq(
                "biet",
                r"Công thức tính áp suất $p$ của chất khí tác dụng lên thành bình theo mô hình động học phân tử (với $\mu$ là mật độ phân tử, $m$ là khối lượng một phân tử, $\overline{v^2}$ là trung bình của bình phương tốc độ) là:",
                [
                    r"$p = \dfrac{1}{3}\mu m\overline{v^2}$",
                    r"$p = \dfrac{2}{3}\mu m\overline{v^2}$",
                    r"$p = \dfrac{3}{2}\mu m\overline{v^2}$",
                    r"$p = \mu m\overline{v^2}$",
                ],
                0,
                r"Áp suất khí theo mô hình động học phân tử được tính bằng $p = \dfrac{1}{3}\mu m\overline{v^2} = \dfrac{2}{3}\mu\overline{W_{\text{đ}}}$.",
            ),
            mcq(
                "hieu",
                r"Một lượng khí lí tưởng xác định có thể tích $V_1 = 6\text{ L}$ ở áp suất $p_1 = 1{,}5\text{ atm}$. Nếu nén đẳng nhiệt lượng khí này để thể tích giảm xuống còn $V_2 = 4\text{ L}$ thì áp suất $p_2$ của khí là:",
                [
                    r"$2{,}25\text{ atm}$",
                    r"$1{,}00\text{ atm}$",
                    r"$3{,}00\text{ atm}$",
                    r"$2{,}50\text{ atm}$",
                ],
                0,
                r"Áp dụng định luật Boyle cho quá trình đẳng nhiệt: $p_1 V_1 = p_2 V_2 \Rightarrow p_2 = \dfrac{p_1 V_1}{V_2} = \dfrac{1{,}5 \cdot 6}{4} = \mathbf{2{,}25\text{ atm}}$.",
            ),
            mcq(
                "hieu",
                r"Một khối khí lí tưởng thực hiện quá trình giãn nở đẳng áp từ nhiệt độ $t_1 = 27^\circ\text{C}$ đến nhiệt độ $t_2 = 127^\circ\text{C}$. Nếu thể tích ban đầu là $V_1 = 3\text{ L}$ thì thể tích $V_2$ ở cuối quá trình là:",
                [
                    r"$4\text{ L}$",
                    r"$14{,}1\text{ L}$",
                    r"$2{,}25\text{ L}$",
                    r"$6\text{ L}$",
                ],
                0,
                r"Đổi sang nhiệt độ tuyệt đối: $T_1 = 27 + 273 = 300\text{ K}$, $T_2 = 127 + 273 = 400\text{ K}$. Theo định luật Charles: $V_2 = V_1 \dfrac{T_2}{T_1} = 3 \cdot \dfrac{400}{300} = \mathbf{4\text{ L}}$.",
            ),
            tf4(
                "hieu",
                r"Cho các phát biểu sau về mô hình động học phân tử chất khí và các định luật chất khí:",
                [
                    r"a) Chuyển động Brown của các hạt phấn hoa trong nước là bằng chứng thực nghiệm chứng tỏ các phân tử môi trường chuyển động hỗn loạn không ngừng.",
                    r"b) Khi nhiệt độ tuyệt đối $T$ của một khối khí lí tưởng tăng gấp $4$ lần thì tốc độ căn quân phương $v_{\text{rms}} = \sqrt{\overline{v^2}}$ của các phân tử khí tăng gấp $4$ lần.",
                    r"c) Ở cùng một nhiệt độ tuyệt đối $T$, động năng tịnh tiến trung bình của phân tử khí hydrogen ($\text{H}_2$) bằng động năng tịnh tiến trung bình của phân tử khí oxygen ($\text{O}_2$).",
                    r"d) Trong quá trình biến đổi đẳng tích của một lượng khí lí tưởng xác định, nếu nhiệt độ Celsius $t$ tăng gấp đôi từ $20^\circ\text{C}$ lên $40^\circ\text{C}$ thì áp suất khí tăng gấp đôi.",
                ],
                [True, False, True, False],
                r"- **a) Đúng**: Các phân tử môi trường chuyển động nhiệt va chạm không cân bằng vào hạt phấn hoa gây ra chuyển động Brown." "\n"
                r"- **b) Sai**: Vì $v_{\text{rms}} = \sqrt{\dfrac{3RT}{M}} \propto \sqrt{T}$, nên khi $T$ tăng gấp $4$ lần thì $v_{\text{rms}}$ chỉ tăng gấp $\sqrt{4} = 2$ lần." "\n"
                r"- **c) Đúng**: $\overline{W_{\text{đ}}} = \dfrac{3}{2}kT$ chỉ phụ thuộc vào nhiệt độ tuyệt đối $T$, không phụ thuộc vào bản chất hay khối lượng phân tử khí." "\n"
                r"- **d) Sai**: Áp suất tỉ lệ thuận với nhiệt độ tuyệt đối $T\text{ (K)}$, không tỉ lệ thuận với nhiệt độ Celsius $t\text{ (}^\circ\text{C)}$: $\dfrac{p_2}{p_1} = \dfrac{40 + 273}{20 + 273} = \dfrac{313}{293} \approx 1{,}068 \neq 2$.",
            ),
            tf4(
                "hieu",
                r"Một xilanh kín có pít-tông di chuyển không ma sát chứa $n = 0{,}5\text{ mol}$ khí lí tưởng ở trạng thái $(1)$ có áp suất $p_1 = 10^5\text{ Pa}$ và nhiệt độ $T_1 = 300\text{ K}$. Lấy $R = 8{,}31\text{ J/(mol}\cdot\text{K)}$ và $N_{\text{A}} = 6{,}02 \times 10^{23}\text{ mol}^{-1}$. Xét tính đúng hay sai của các mệnh đề sau:",
                [
                    r"a) Số phân tử khí chứa trong xilanh là $N = 3{,}01 \times 10^{23}$ phân tử.",
                    r"b) Thể tích của khối khí ở trạng thái $(1)$ là $V_1 = 12{,}465\text{ L}$.",
                    r"c) Nếu nén đẳng nhiệt khối khí đến thể tích $V_2 = \dfrac{V_1}{3}$ thì áp suất của khí ở trạng thái $(2)$ là $p_2 = 3 \times 10^5\text{ Pa}$.",
                    r"d) Từ trạng thái $(2)$, nếu nung nóng đẳng tích khối khí đến nhiệt độ $T_3 = 450\text{ K}$ thì áp suất ở trạng thái $(3)$ là $p_3 = 2 \times 10^5\text{ Pa}$.",
                ],
                [True, True, True, False],
                r"- **a) Đúng**: $N = n N_{\text{A}} = 0{,}5 \cdot 6{,}02 \times 10^{23} = 3{,}01 \times 10^{23}$ phân tử." "\n"
                r"- **b) Đúng**: $V_1 = \dfrac{nRT_1}{p_1} = \dfrac{0{,}5 \cdot 8{,}31 \cdot 300}{10^5} = 0{,}012465\text{ m}^3 = 12{,}465\text{ L}$." "\n"
                r"- **c) Đúng**: Nén đẳng nhiệt từ $(1)$ sang $(2)$ với $V_2 = \dfrac{V_1}{3} \Rightarrow p_2 = 3p_1 = 3 \times 10^5\text{ Pa}$." "\n"
                r"- **d) Sai**: Nung nóng đẳng tích từ $(2)$ sang $(3)$: $p_3 = p_2 \dfrac{T_3}{T_2} = 3 \times 10^5 \cdot \dfrac{450}{300} = 4{,}5 \times 10^5\text{ Pa}$ (không phải $2 \times 10^5\text{ Pa}$).",
            ),
            mcq(
                "vandung",
                r"Một bọt khí nổi từ đáy một hồ nước sâu $h = 15\text{ m}$ lên sát mặt nước. Biết nhiệt độ ở đáy hồ là $t_1 = 7^\circ\text{C}$, nhiệt độ ở sát mặt nước là $t_2 = 27^\circ\text{C}$, áp suất khí quyển là $p_0 = 10^5\text{ Pa}$, khối lượng riêng của nước hồ là $\rho = 1000\text{ kg/m}^3$ và $g = 10\text{ m/s}^2$. Khi lên tới sát mặt nước, thể tích của bọt khí tăng lên bao nhiêu lần so với ở đáy hồ?",
                [
                    r"$2{,}68\text{ lần}$",
                    r"$2{,}50\text{ lần}$",
                    r"$1{,}50\text{ lần}$",
                    r"$3{,}21\text{ lần}$",
                ],
                0,
                r"Ở đáy hồ: $p_1 = p_0 + \rho g h = 10^5 + 1000 \cdot 10 \cdot 15 = 2{,}5 \times 10^5\text{ Pa}$; $T_1 = 7 + 273 = 280\text{ K}$. "
                r"Ở sát mặt nước: $p_2 = p_0 = 10^5\text{ Pa}$; $T_2 = 27 + 273 = 300\text{ K}$. "
                r"Theo phương trình trạng thái khí lí tưởng: $\dfrac{V_2}{V_1} = \dfrac{p_1 T_2}{p_2 T_1} = \dfrac{2{,}5 \times 10^5 \cdot 300}{10^5 \cdot 280} = \dfrac{75}{28} \approx \mathbf{2{,}68\text{ lần}}$.",
            ),
            short(
                "vandung",
                r"Một bình chứa khí oxygen ($\text{O}_2$, có khối lượng mol $M = 32\text{ g/mol}$) có dung tích $V = 8{,}31\text{ L}$ ở áp suất $p = 6 \times 10^5\text{ Pa}$ và nhiệt độ $t = 27^\circ\text{C}$. Lấy $R = 8{,}31\text{ J/(mol}\cdot\text{K)}$. Khối lượng khí oxygen trong bình bằng bao nhiêu gam?",
                ["64"],
                r"Đổi $V = 8{,}31\text{ L} = 8{,}31 \times 10^{-3}\text{ m}^3$; $T = 27 + 273 = 300\text{ K}$. "
                r"Số mol khí oxygen trong bình: $n = \dfrac{pV}{RT} = \dfrac{6 \times 10^5 \cdot 8{,}31 \times 10^{-3}}{8{,}31 \cdot 300} = 2\text{ mol}$. "
                r"Khối lượng khí oxygen: $m = nM = 2 \cdot 32 = \mathbf{64}\text{ g}$.",
                unit=r"$\text{g}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG III – PHẦN 1. TỪ TRƯỜNG VÀ LỰC TỪ (Bài 14 – Bài 16 SGK Vật lí 12 KNTT)
    # =========================================================================
    {
        "topic": "tu-truong",
        "title": "Chương III (Phần 1). Từ trường và Lực từ",
        "icon": "🧲",
        "description": (
            "Chương III (Phần 1) · SGK Vật lí 12 Kết nối tri thức với cuộc sống (Bài 14 – Bài 16): "
            "Từ trường, đường sức từ và từ trường đều; Lực từ tác dụng lên đoạn dây dẫn mang dòng điện và cảm ứng từ; "
            "Từ thông, hiện tượng cảm ứng điện từ, định luật Lenz và định luật Faraday."
        ),
        "requirements": [
            r"Thực hiện thí nghiệm (hoặc quan sát thí nghiệm Oersted, từ phổ mạt sắt) tạo ra được các đường sức từ quanh nam châm và dây dẫn mang dòng điện; mô tả được khái niệm từ trường và tính chất của đường sức từ.",
            r"Xác định được chiều của đường sức từ của dòng điện chạy trong dây dẫn thẳng dài, dây dẫn uốn thành vòng tròn và ống dây có dòng điện chạy qua bằng quy tắc nắm tay phải.",
            r"Thực hiện thí nghiệm để mô tả được hướng của lực từ tác dụng lên đoạn dây dẫn mang dòng điện đặt trong từ trường (quy tắc bàn tay trái).",
            r"Định nghĩa được cảm ứng từ $\vec{B}$ và đơn vị tesla ($\text{T}$); nêu được phương pháp đo cảm ứng từ bằng cân dòng điện.",
            r"Vận dụng được biểu thức tính độ lớn lực từ tác dụng lên đoạn dây dẫn mang dòng điện $F = BIL\sin\theta$ và lực Lorentz $f = |q|vB\sin\theta$.",
            r"Định nghĩa được từ thông $\Phi = NBS\cos\alpha$ và đơn vị weber ($\text{Wb}$).",
            r"Tiến hành các thí nghiệm đơn giản minh hoạ được hiện tượng cảm ứng điện từ; phát biểu và vận dụng được định luật Lenz về chiều dòng điện cảm ứng và định luật Faraday về độ lớn suất điện động cảm ứng $e_{\text{c}} = -\dfrac{\Delta \Phi}{\Delta t}$.",
        ],
        "definition": (
            r"- **Từ trường và Đường sức từ**: **Từ trường** là dạng vật chất tồn tại trong không gian xung quanh nam châm, dòng điện hoặc điện tích chuyển động, biểu hiện cụ thể bằng lực từ tác dụng lên nam châm hay dòng điện khác đặt trong nó. **Đường sức từ** là những đường vẽ trong không gian có từ trường sao cho tiếp tuyến tại mỗi điểm trùng với phương của vectơ cảm ứng từ $\vec{B}$ tại điểm đó; chiều của đường sức từ tuân theo quy tắc **vào Nam ra Bắc** (hoặc quy tắc nắm tay phải). Các đường sức từ là những đường cong khép kín và không cắt nhau." "\n"
            r"- **Lực từ và Cảm ứng từ ($\vec{B}$)**: Đoạn dây dẫn thẳng chiều dài $L$ mang dòng điện $I$ đặt trong từ trường đều $\vec{B}$ hợp góc $\theta$ với dây dẫn chịu tác dụng của lực từ $\vec{F}$ có phương vuông góc với mặt phẳng chứa dây dẫn và $\vec{B}$, chiều tuân theo **quy tắc bàn tay trái**, độ lớn $F = BIL\sin\theta$. Độ lớn cảm ứng từ: $B = \dfrac{F}{IL\sin\theta}$, đơn vị trong hệ SI là **tesla** ($\text{T}$), với $1\text{ T} = 1\text{ N/(A}\cdot\text{m)}$." "\n"
            r"- **Từ thông ($\Phi$) và Cảm ứng điện từ**: Từ thông qua khung dây phẳng gồm $N$ vòng dây có diện tích mỗi vòng là $S$ đặt trong từ trường đều $\vec{B}$: $\Phi = NBS\cos\alpha$ (đơn vị **weber**, ký hiệu $\text{Wb}$, $1\text{ Wb} = 1\text{ T}\cdot\text{m}^2$), với $\alpha = (\vec{n}, \vec{B})$ là góc hợp bởi vectơ pháp tuyến $\vec{n}$ của mặt phẳng khung và $\vec{B}$." "\n"
            r"- **Định luật Lenz và Định luật Faraday**: Khi từ thông $\Phi$ qua một mạch kín biến thiên thì trong mạch xuất hiện dòng điện cảm ứng có chiều sao cho từ trường cảm ứng $\vec{B}_{\text{c}}$ có tác dụng chống lại sự biến thiên của từ thông ban đầu qua mạch (**Định luật Lenz**). Suất điện động cảm ứng trong mạch kín tỉ lệ với tốc độ biến thiên của từ thông qua mạch (**Định luật Faraday**): $e_{\text{c}} = -\dfrac{\Delta \Phi}{\Delta t}$ (độ lớn $|e_{\text{c}}| = \left|\dfrac{\Delta \Phi}{\Delta t}\right|$)."
        ),
        "theory": (
            r"### Bài 14. Từ trường" "\n"
            r"- **Tương tác từ**: Là tương tác giữa nam châm với nam châm, giữa nam châm với dòng điện (thí nghiệm Oersted) và giữa hai dòng điện với nhau." "\n"
            r"- **Tính chất của đường sức từ**: (1) Tại mỗi điểm trong từ trường chỉ vẽ được một đường sức từ đi qua; (2) Các đường sức từ là những đường cong khép kín; (3) Nơi nào từ trường mạnh hơn thì các đường sức từ được vẽ dày hơn, nơi nào từ trường yếu hơn thì vẽ thưa hơn. **Từ trường đều** là từ trường có vectơ cảm ứng từ $\vec{B}$ tại mọi điểm đều bằng nhau (các đường sức từ song song và cách đều nhau, như trong lòng ống dây hình trụ dài hay giữa hai cực nam châm hình chữ U)." "\n"
            r"- **Quy tắc nắm tay phải**: Đối với dòng điện thẳng dài: ngón cái choãi ra chỉ chiều dòng điện $I$, bốn ngón tay khum lại chỉ chiều đường sức từ (là các đường tròn đồng tâm vuông góc với dây). Đối với vòng dây tròn và ống dây hình trụ: bốn ngón tay khum theo chiều dòng điện $I$ chạy qua các vòng dây, ngón cái choãi ra chỉ chiều đường sức từ đi xuyên qua lòng ống dây." "\n"
            r"### Bài 15. Lực từ tác dụng lên dây dẫn mang dòng điện. Cảm ứng từ" "\n"
            r"- **Quy tắc bàn tay trái (xác định lực từ $\vec{F}$)**: Đặt bàn tay trái duỗi thẳng sao cho các đường sức từ ($\vec{B}$) hướng vào lòng bàn tay, chiều từ cổ tay đến bốn ngón tay trùng với chiều dòng điện $I$, khi đó ngón tay cái choãi ra $90^\circ$ chỉ chiều của lực từ $\vec{F}$ tác dụng lên đoạn dây dẫn." "\n"
            r"- **Độ lớn lực từ và định nghĩa cảm ứng từ**: $F = BIL\sin\theta$, trong đó $\theta$ là góc hợp bởi chiều dòng điện và vectơ $\vec{B}$. Khi $\theta = 0^\circ$ hoặc $\theta = 180^\circ$ (dây dẫn song song với $\vec{B}$) thì $F = 0$; khi $\theta = 90^\circ$ (dây dẫn vuông góc với $\vec{B}$) thì lực từ đạt cực đại $F_{\max} = BIL$." "\n"
            r"- **Thí nghiệm cân dòng điện**: Dùng để đo độ lớn cảm ứng từ $B$ trong lòng nam châm thông qua việc cân bằng lực từ $F = BIL$ tác dụng lên đoạn dây dẫn nằm ngang với trọng lực của các quả cân (hoặc số chỉ lực kế điện tử)." "\n"
            r"- **Mở rộng – Cảm ứng từ của một số dòng điện đặc biệt và lực Lorentz**: Dây dẫn thẳng dài: $B = 2 \times 10^{-7}\dfrac{I}{r}$; tâm khung dây tròn $N$ vòng: $B = 2\pi \times 10^{-7}\dfrac{NI}{R}$; trong lòng ống dây hình trụ: $B = 4\pi \times 10^{-7}\dfrac{NI}{\ell} = 4\pi \times 10^{-7}nI$. Hạt điện tích $q$ chuyển động với vận tốc $\vec{v}$ trong từ trường chịu lực Lorentz $f = |q|vB\sin\theta$." "\n"
            r"### Bài 16. Từ thông. Hiện tượng cảm ứng điện từ" "\n"
            r"- **Từ thông**: $\Phi = NBS\cos\alpha$. Lưu ý phân biệt góc $\alpha = (\vec{n}, \vec{B})$ với góc $\beta$ hợp bởi $\vec{B}$ và mặt phẳng khung dây ($\alpha + \beta = 90^\circ \Rightarrow \cos\alpha = \sin\beta$)." "\n"
            r"- **Định luật Lenz**: Nếu từ thông $\Phi$ qua mạch kín **tăng** ($\Delta \Phi > 0$) thì từ trường cảm ứng $\vec{B}_{\text{c}}$ **ngược chiều** với từ trường ban đầu $\vec{B}$ ($\vec{B}_{\text{c}} \uparrow\downarrow \vec{B}$); nếu từ thông $\Phi$ **giảm** ($\Delta \Phi < 0$) thì $\vec{B}_{\text{c}}$ **cùng chiều** với $\vec{B}$ ($\vec{B}_{\text{c}} \uparrow\uparrow \vec{B}$)." "\n"
            r"- **Định luật Faraday và dòng điện cảm ứng**: Độ lớn suất điện động cảm ứng $|e_{\text{c}}| = \left|\dfrac{\Delta \Phi}{\Delta t}\right|$. Nếu mạch kín có tổng điện trở $R$ thì cường độ dòng điện cảm ứng là $I_{\text{c}} = \dfrac{|e_{\text{c}}|}{R}$. Đối với đoạn dây dẫn chiều dài $\ell$ chuyển động cắt các đường sức từ với vận tốc $v$: $|e_{\text{c}}| = B\ell v\sin\theta$."
        ),
        "formulas": [
            G(
                "I. Lực từ và Cảm ứng từ",
                F("Độ lớn lực từ Ampere", r"$F = BIL\sin\theta$", r"$\theta = (\vec{I}, \vec{B})$; khi $\vec{I} \perp \vec{B}$ thì $F_{\max} = BIL$."),
                F("Độ lớn cảm ứng từ", r"$B = \dfrac{F}{IL\sin\theta}$", r"Đơn vị: tesla ($\text{T}$), $1\text{ T} = 1\text{ N/(A}\cdot\text{m)} = 10^4\text{ G}$."),
                F("Từ trường dòng điện thẳng, tròn, ống dây", r"$B_{\text{thẳng}} = 2 \times 10^{-7}\dfrac{I}{r}; \quad B_{\text{tròn}} = 2\pi \times 10^{-7}\dfrac{NI}{R}; \quad B_{\text{ống}} = 4\pi \times 10^{-7}\dfrac{NI}{\ell}$", r"Áp dụng trong chân không hoặc không khí."),
                F("Lực Lorentz lên hạt mang điện", r"$f = |q|vB\sin\theta; \quad R = \dfrac{mv}{|q|B}\text{ (khi }\vec{v} \perp \vec{B}\text{)}$", r"Bán kính quỹ đạo tròn trong từ trường đều."),
            ),
            G(
                "II. Từ thông và Hiện tượng cảm ứng điện từ",
                F("Từ thông qua khung dây $N$ vòng", r"$\Phi = NBS\cos\alpha = NBS\sin\beta$", r"$\alpha = (\vec{n}, \vec{B})$, $\beta = (\vec{B}, \text{mp khung})$; đơn vị: $\text{Wb}$."),
                F("Định luật Faraday về cảm ứng điện từ", r"$e_{\text{c}} = -\dfrac{\Delta \Phi}{\Delta t} \Rightarrow |e_{\text{c}}| = \left|\dfrac{\Delta \Phi}{\Delta t}\right|$", r"Dấu trừ biểu thị định luật Lenz."),
                F("Cường độ dòng điện cảm ứng và Điện lượng dịch chuyển", r"$I_{\text{c}} = \dfrac{|e_{\text{c}}|}{R}; \quad \Delta q = I_{\text{c}}\Delta t = \dfrac{|\Delta \Phi|}{R}$", r"$R$ là tổng điện trở của mạch kín."),
                F("Suất điện động cảm ứng trong thanh chuyển động", r"$|e_{\text{c}}| = B\ell v\sin\theta$", r"Chiều xác định bằng quy tắc bàn tay phải."),
            ),
        ],
        "example": (
            r"Một khung dây dẫn phẳng hình vuông gồm $N = 100\text{ vòng}$ dây, mỗi cạnh dài $a = 10\text{ cm}$, có tổng điện trở $R = 2\text{ }\Omega$. "
            r"Khung dây được đặt trong một từ trường đều có vectơ cảm ứng từ $\vec{B}$ hợp với mặt phẳng khung dây một góc $\beta = 30^\circ$. "
            r"Trong khoảng thời gian $\Delta t = 0{,}05\text{ s}$, độ lớn cảm ứng từ giảm đều từ $B_1 = 0{,}4\text{ T}$ về $B_2 = 0\text{ T}$. "
            r"Tính độ biến thiên từ thông qua khung dây, độ lớn suất điện động cảm ứng $|e_{\text{c}}|$ và cường độ dòng điện cảm ứng $I_{\text{c}}$ trong khung."
        ),
        "example_answer": (
            r"- **Diện tích mỗi vòng dây**: $S = a^2 = (0{,}1\text{ m})^2 = 0{,}01\text{ m}^2$." "\n"
            r"- **Góc hợp bởi vectơ pháp tuyến $\vec{n}$ và $\vec{B}$**: Vì $\vec{B}$ hợp với mặt phẳng khung dây góc $\beta = 30^\circ$ nên $\alpha = 90^\circ - \beta = 60^\circ \Rightarrow \cos\alpha = \cos 60^\circ = 0{,}5$." "\n"
            r"- **Từ thông ban đầu và lúc sau**: $\Phi_1 = N B_1 S \cos\alpha = 100 \cdot 0{,}4 \cdot 0{,}01 \cdot 0{,}5 = 0{,}2\text{ Wb}$; $\Phi_2 = 0\text{ Wb}$. Độ biến thiên từ thông: $\Delta \Phi = \Phi_2 - \Phi_1 = -0{,}2\text{ Wb}$." "\n"
            r"- **Độ lớn suất điện động cảm ứng**: $|e_{\text{c}}| = \left|\dfrac{\Delta \Phi}{\Delta t}\right| = \dfrac{0{,}2}{0{,}05} = \mathbf{4\text{ V}}$." "\n"
            r"- **Cường độ dòng điện cảm ứng trong khung**: $I_{\text{c}} = \dfrac{|e_{\text{c}}|}{R} = \dfrac{4}{2} = \mathbf{2\text{ A}}$."
        ),
        "real_life": (
            r"- **Động cơ điện một chiều và loa điện động**: Dòng điện chạy qua cuộn dây đặt trong từ trường của nam châm vĩnh cửu chịu lực từ $F = BIL$ làm quay rôto động cơ hoặc làm dao động màng loa phát ra âm thanh." "\n"
            r"- **Cân dòng điện trong phòng thí nghiệm**: Ứng dụng lực từ cân bằng với trọng lực để đo chính xác độ lớn cảm ứng từ $B$ của nam châm." "\n"
            r"- **Đầu đọc thẻ từ, cảm biến tốc độ bánh xe ABS và micro điện động**: Dựa trên hiện tượng cảm ứng điện từ xuất hiện suất điện động $e_{\text{c}} = -\dfrac{\Delta \Phi}{\Delta t}$ khi từ thông biến thiên."
        ),
        "game_title": "Thí nghiệm Lực từ, Cân dòng điện và Cảm ứng điện từ Faraday",
        "game_description": "Khảo sát quy tắc bàn tay trái, đo cảm ứng từ bằng cân dòng điện và dịch chuyển nam châm qua cuộn dây để kiểm nghiệm định luật Lenz – Faraday.",
        "game_type": "game_tu_truong",
        "quiz": [
            mcq(
                "biet",
                r"Đoạn dây dẫn thẳng có chiều dài $L$ mang dòng điện cường độ $I$ đặt trong từ trường đều có cảm ứng từ $\vec{B}$ hợp với dây dẫn một góc $\theta$. Độ lớn của lực từ $F$ tác dụng lên đoạn dây dẫn được tính bằng công thức nào?",
                [
                    r"$F = BIL\sin\theta$",
                    r"$F = BIL\cos\theta$",
                    r"$F = BIL\tan\theta$",
                    r"$F = \dfrac{BI}{L}\sin\theta$",
                ],
                0,
                r"Độ lớn lực từ tác dụng lên đoạn dây dẫn mang dòng điện đặt trong từ trường đều là $F = BIL\sin\theta$.",
            ),
            mcq(
                "biet",
                r"Đơn vị của từ thông $\Phi$ và đơn vị của cảm ứng từ $B$ trong hệ SI lần lượt là:",
                [
                    r"Weber ($\text{Wb}$) và tesla ($\text{T}$)",
                    r"Tesla ($\text{T}$) và weber ($\text{Wb}$)",
                    r"Henry ($\text{H}$) và tesla ($\text{T}$)",
                    r"Weber ($\text{Wb}$) và volt ($\text{V}$)",
                ],
                0,
                r"Trong hệ SI, từ thông $\Phi$ có đơn vị là weber ($\text{Wb}$) và cảm ứng từ $B$ có đơn vị là tesla ($\text{T}$), với $1\text{ Wb} = 1\text{ T}\cdot\text{m}^2$.",
            ),
            mcq(
                "biet",
                r"Theo định luật Lenz, dòng điện cảm ứng xuất hiện trong một mạch kín có chiều sao cho từ trường cảm ứng do nó sinh ra:",
                [
                    r"Có tác dụng chống lại sự biến thiên của từ thông ban đầu qua mạch kín",
                    r"Luôn cùng chiều với từ trường ban đầu qua mạch kín",
                    r"Luôn ngược chiều với từ trường ban đầu qua mạch kín",
                    r"Luôn vuông góc với các đường sức của từ trường ban đầu",
                ],
                0,
                r"Định luật Lenz khẳng định: dòng điện cảm ứng xuất hiện trong mạch kín có chiều sao cho từ trường cảm ứng có tác dụng chống lại sự biến thiên của từ thông ban đầu qua mạch.",
            ),
            mcq(
                "biet",
                r"Biểu thức của định luật Faraday về suất điện động cảm ứng $e_{\text{c}}$ xuất hiện trong một mạch kín có từ thông biến thiên lượng $\Delta \Phi$ trong khoảng thời gian $\Delta t$ là:",
                [
                    r"$e_{\text{c}} = -\dfrac{\Delta \Phi}{\Delta t}$",
                    r"$e_{\text{c}} = -\Delta \Phi \cdot \Delta t$",
                    r"$e_{\text{c}} = -\dfrac{\Delta t}{\Delta \Phi}$",
                    r"$e_{\text{c}} = \dfrac{1}{2}\Delta \Phi (\Delta t)^2$",
                ],
                0,
                r"Theo định luật Faraday, suất điện động cảm ứng trong mạch kín tỉ lệ với tốc độ biến thiên của từ thông: $e_{\text{c}} = -\dfrac{\Delta \Phi}{\Delta t}$.",
            ),
            mcq(
                "hieu",
                r"Một đoạn dây dẫn thẳng dài $L = 40\text{ cm}$ có dòng điện cường độ $I = 5\text{ A}$ chạy qua được đặt trong một từ trường đều có độ lớn cảm ứng từ $B = 0{,}25\text{ T}$ sao cho dây dẫn hợp với vectơ cảm ứng từ $\vec{B}$ một góc $\theta = 30^\circ$. Độ lớn lực từ tác dụng lên đoạn dây dẫn là:",
                [
                    r"$0{,}25\text{ N}$",
                    r"$0{,}50\text{ N}$",
                    r"$0{,}43\text{ N}$",
                    r"$2{,}50\text{ N}$",
                ],
                0,
                r"Đổi $L = 40\text{ cm} = 0{,}4\text{ m}$. Áp dụng công thức: $F = BIL\sin\theta = 0{,}25 \cdot 5 \cdot 0{,}4 \cdot \sin 30^\circ = 0{,}5 \cdot 0{,}5 = \mathbf{0{,}25\text{ N}}$.",
            ),
            mcq(
                "hieu",
                r"Một khung dây phẳng gồm $N = 200\text{ vòng}$ dây, diện tích mỗi vòng là $S = 25\text{ cm}^2$, đặt trong từ trường đều có cảm ứng từ $B = 0{,}4\text{ T}$ sao cho mặt phẳng khung dây vuông góc với các đường sức từ. Từ thông qua khung dây là:",
                [
                    r"$0{,}2\text{ Wb}$",
                    r"$0\text{ Wb}$",
                    r"$2000\text{ Wb}$",
                    r"$0{,}001\text{ Wb}$",
                ],
                0,
                r"Đổi $S = 25\text{ cm}^2 = 25 \times 10^{-4}\text{ m}^2$. Vì mặt phẳng khung dây vuông góc với đường sức từ nên vectơ pháp tuyến $\vec{n}$ song song với $\vec{B}$ ($\alpha = 0^\circ \Rightarrow \cos\alpha = 1$). Do đó $\Phi = NBS\cos 0^\circ = 200 \cdot 0{,}4 \cdot 25 \times 10^{-4} \cdot 1 = \mathbf{0{,}2\text{ Wb}}$.",
            ),
            tf4(
                "hieu",
                r"Xét tính đúng hay sai của các phát biểu sau về từ trường, đường sức từ và lực từ:",
                [
                    r"a) Các đường sức từ là những đường cong khép kín; đối với nam châm, ở bên ngoài nam châm các đường sức từ đi ra từ cực Bắc và đi vào cực Nam.",
                    r"b) Khi đoạn dây dẫn mang dòng điện đặt song song với các đường sức từ ($\theta = 0^\circ$ hoặc $\theta = 180^\circ$) thì lực từ tác dụng lên đoạn dây dẫn đạt giá trị cực đại.",
                    r"c) Từ trường trong lòng một ống dây hình trụ dài có dòng điện không đổi chạy qua là từ trường đều, có các đường sức từ là những đường thẳng song song và cách đều nhau.",
                    r"d) Lực từ tác dụng lên đoạn dây dẫn mang dòng điện luôn có phương vuông góc với cả đoạn dây dẫn và vectơ cảm ứng từ $\vec{B}$.",
                ],
                [True, False, True, True],
                r"- **a) Đúng**: Đường sức từ luôn là đường cong khép kín, tuân theo quy tắc vào Nam (S) ra Bắc (N)." "\n"
                r"- **b) Sai**: Khi $\theta = 0^\circ$ hoặc $180^\circ$ thì $\sin\theta = 0 \Rightarrow F = BIL\sin\theta = 0$ (dây dẫn không chịu lực từ)." "\n"
                r"- **c) Đúng**: Trong lòng ống dây hình trụ dài, từ trường là từ trường đều." "\n"
                r"- **d) Đúng**: Vectơ lực từ $\vec{F}$ luôn vuông góc với mặt phẳng chứa dòng điện và vectơ cảm ứng từ $\vec{B}$.",
            ),
            tf4(
                "hieu",
                r"Một vòng dây dẫn kín phẳng có diện tích $S = 100\text{ cm}^2$ và điện trở $R = 0{,}5\text{ }\Omega$ được đặt cố định trong từ trường đều sao cho vectơ cảm ứng từ $\vec{B}$ vuông góc với mặt phẳng vòng dây. Trong khoảng thời gian $\Delta t = 0{,}04\text{ s}$, cảm ứng từ tăng đều từ $B_1 = 0{,}1\text{ T}$ lên $B_2 = 0{,}5\text{ T}$. Xét các khẳng định sau:",
                [
                    r"a) Độ biến thiên từ thông qua vòng dây trong khoảng thời gian trên là $\Delta \Phi = 4 \times 10^{-3}\text{ Wb}$.",
                    r"b) Vì từ thông qua vòng dây tăng nên từ trường cảm ứng $\vec{B}_{\text{c}}$ do dòng điện cảm ứng sinh ra cùng chiều với từ trường ban đầu $\vec{B}$.",
                    r"c) Độ lớn suất điện động cảm ứng xuất hiện trong vòng dây là $|e_{\text{c}}| = 0{,}1\text{ V}$.",
                    r"d) Cường độ dòng điện cảm ứng chạy trong vòng dây là $I_{\text{c}} = 0{,}2\text{ A}$.",
                ],
                [True, False, True, True],
                r"- **a) Đúng**: Đổi $S = 100\text{ cm}^2 = 0{,}01\text{ m}^2$, $\alpha = 0^\circ$. Ta có $\Delta \Phi = (B_2 - B_1)S = (0{,}5 - 0{,}1) \cdot 0{,}01 = 4 \times 10^{-3}\text{ Wb}$." "\n"
                r"- **b) Sai**: Theo định luật Lenz, khi từ thông $\Phi$ tăng thì từ trường cảm ứng $\vec{B}_{\text{c}}$ phải **ngược chiều** với từ trường ban đầu $\vec{B}$ để chống lại sự tăng từ thông." "\n"
                r"- **c) Đúng**: $|e_{\text{c}}| = \dfrac{|\Delta \Phi|}{\Delta t} = \dfrac{4 \times 10^{-3}}{0{,}04} = 0{,}1\text{ V}$." "\n"
                r"- **d) Đúng**: $I_{\text{c}} = \dfrac{|e_{\text{c}}|}{R} = \dfrac{0{,}1}{0{,}5} = 0{,}2\text{ A}$.",
            ),
            mcq(
                "vandung",
                r"Một đoạn dây dẫn bằng đồng có khối lượng $m = 12\text{ g}$ và chiều dài $L = 30\text{ cm}$ được treo nằm ngang bằng hai sợi dây mảnh không giãn trong một từ trường đều có vectơ cảm ứng từ $\vec{B}$ nằm ngang và vuông góc với đoạn dây dẫn, độ lớn $B = 0{,}2\text{ T}$. Lấy $g = 10\text{ m/s}^2$. Để lực căng của hai sợi dây treo bằng $0$ thì dòng điện chạy qua đoạn dây đồng phải có cường độ bằng bao nhiêu?",
                [
                    r"$2{,}0\text{ A}$",
                    r"$1{,}5\text{ A}$",
                    r"$0{,}5\text{ A}$",
                    r"$4{,}0\text{ A}$",
                ],
                0,
                r"Đổi $m = 12\text{ g} = 0{,}012\text{ kg}$, $L = 30\text{ cm} = 0{,}3\text{ m}$. Để lực căng dây treo bằng $0$, lực từ $\vec{F}$ phải hướng thẳng đứng lên trên và cân bằng với trọng lực $\vec{P}$: $BIL = mg \Rightarrow I = \dfrac{mg}{BL} = \dfrac{0{,}012 \cdot 10}{0{,}2 \cdot 0{,}3} = \dfrac{0{,}12}{0{,}06} = \mathbf{2{,}0\text{ A}}$.",
            ),
            short(
                "vandung",
                r"Một cuộn dây phẳng gồm $N = 500\text{ vòng}$ dây, diện tích mỗi vòng là $S = 40\text{ cm}^2$, đặt trong từ trường đều có $\vec{B}$ hợp với mặt phẳng khung dây góc $\beta = 30^\circ$. Khi cho cảm ứng từ giảm đều từ $B = 0{,}6\text{ T}$ về $0\text{ T}$ trong thời gian $\Delta t = 0{,}02\text{ s}$ thì suất điện động cảm ứng xuất hiện trong cuộn dây có độ lớn bằng bao nhiêu vôn ($\text{V}$)?",
                ["30"],
                r"Đổi $S = 40\text{ cm}^2 = 4 \times 10^{-3}\text{ m}^2$. Góc hợp bởi pháp tuyến $\vec{n}$ và $\vec{B}$ là $\alpha = 90^\circ - 30^\circ = 60^\circ \Rightarrow \cos\alpha = 0{,}5$. "
                r"Từ thông ban đầu: $\Phi_1 = NBS\cos 60^\circ = 500 \cdot 0{,}6 \cdot 4 \times 10^{-3} \cdot 0{,}5 = 0{,}6\text{ Wb}$. "
                r"Độ lớn suất điện động cảm ứng: $|e_{\text{c}}| = \dfrac{|\Delta \Phi|}{\Delta t} = \dfrac{0{,}6}{0{,}02} = \mathbf{30}\text{ V}$.",
                unit=r"$\text{V}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG III – PHẦN 2. MÁY PHÁT ĐIỆN XOAY CHIỀU, DÒNG ĐIỆN XOAY CHIỀU VÀ SÓNG ĐIỆN TỪ (Bài 17 – Bài 20 SGK Vật lí 12 KNTT)
    # =========================================================================
    {
        "topic": "mach-xoay-chieu",
        "title": "Chương III (Phần 2). Máy phát điện xoay chiều, Dòng điện xoay chiều và Sóng điện từ",
        "icon": "⚡",
        "description": (
            "Chương III (Phần 2) · SGK Vật lí 12 Kết nối tri thức với cuộc sống (Bài 17 – Bài 20): "
            "Máy phát điện xoay chiều, suất điện động xoay chiều và các giá trị hiệu dụng; "
            "Ứng dụng hiện tượng cảm ứng điện từ (dòng điện Foucault, bếp từ, phanh điện từ, đàn guitar điện, sạc không dây); "
            "Điện từ trường và mô hình sóng điện từ; Bài tập về từ trường."
        ),
        "requirements": [
            r"Nêu được nguyên tắc tạo ra dòng điện xoay chiều dựa trên hiện tượng cảm ứng điện từ và mô tả được cấu tạo cơ bản của máy phát điện xoay chiều (phần cảm và phần ứng).",
            r"Viết được biểu thức từ thông $\Phi = \Phi_0\cos(\omega t + \varphi_0)$ và suất điện động cảm ứng xoay chiều $e = E_0\cos\left(\omega t + \varphi_0 - \dfrac{\pi}{2}\right)$ với $E_0 = NBS\omega$.",
            r"Nêu được chu kì $T$, tần số $f$, giá trị cực đại ($I_0, U_0, E_0$) và định nghĩa giá trị hiệu dụng ($I = \dfrac{I_0}{\sqrt{2}}$, $U = \dfrac{U_0}{\sqrt{2}}$, $E = \dfrac{E_0}{\sqrt{2}}$) dựa trên tác dụng nhiệt của dòng điện.",
            r"Thảo luận để nêu được các quy tắc an toàn khi sử dụng dòng điện xoay chiều trong gia đình và sản xuất.",
            r"Giải thích được một số ứng dụng của hiện tượng cảm ứng điện từ trong cuộc sống và kĩ thuật: dòng điện Foucault (dòng điện xoáy), phanh điện từ, bếp từ, lò nung cảm ứng, đàn guitar điện, máy biến áp và sạc không dây.",
            r"Nêu được mối liên hệ mật thiết giữa điện trường biến thiên và từ trường biến thiên để tạo thành điện từ trường thống nhất theo thuyết điện từ Maxwell.",
            r"Mô tả được mô hình sóng điện từ là sóng ngang (các vectơ $\vec{E}, \vec{B}, \vec{v}$ đôi một vuông góc tạo thành tam diện thuận, $\vec{E}$ và $\vec{B}$ luôn dao động cùng pha) và vận dụng được công thức bước sóng $\lambda = \dfrac{c}{f} = cT$.",
        ],
        "definition": (
            r"- **Nguyên tắc tạo dòng điện xoay chiều**: Khi khung dây dẫn phẳng gồm $N$ vòng, diện tích $S$ quay đều với tốc độ góc $\omega$ quanh một trục cố định đặt trong từ trường đều $\vec{B}$ ($\vec{B} \perp \text{trục quay}$), từ thông qua khung biến thiên điều hoà: $\Phi = NBS\cos(\omega t + \varphi_0) = \Phi_0\cos(\omega t + \varphi_0)$. Trong khung xuất hiện suất điện động xoay chiều: $e = -\Phi'(t) = NBS\omega\sin(\omega t + \varphi_0) = E_0\cos\left(\omega t + \varphi_0 - \dfrac{\pi}{2}\right)$, với $E_0 = NBS\omega = \Phi_0\omega$." "\n"
            r"- **Dòng điện xoay chiều và Giá trị hiệu dụng**: Dòng điện xoay chiều là dòng điện có cường độ biến thiên điều hoà theo thời gian: $i = I_0\cos(\omega t + \varphi_i)$, điện áp xoay chiều $u = U_0\cos(\omega t + \varphi_u)$. **Giá trị hiệu dụng** của cường độ dòng điện xoay chiều bằng cường độ của một dòng điện không đổi mà khi chạy qua cùng một điện trở $R$ trong cùng một thời gian đủ dài (nguyên lần chu kì) thì toả ra nhiệt lượng bằng nhau: $I = \dfrac{I_0}{\sqrt{2}}$, $U = \dfrac{U_0}{\sqrt{2}}$, $E = \dfrac{E_0}{\sqrt{2}}$. Số chỉ của ampe kế và vôn kế xoay chiều là giá trị hiệu dụng." "\n"
            r"- **Ứng dụng cảm ứng điện từ (Dòng điện Foucault)**: Dòng điện cảm ứng sinh ra trong khối vật dẫn đặt trong từ trường biến thiên (hoặc chuyển động trong từ trường) gọi là **dòng điện Foucault** (dòng điện xoáy), được ứng dụng trong bếp từ, lò tôi kim loại, phanh điện từ; để giảm hao phí nhiệt do dòng Foucault trong lõi máy biến áp và động cơ, người ta ghép lõi từ bằng các lá thép kĩ thuật điện mỏng sơn cách điện." "\n"
            r"- **Điện từ trường và Mô hình sóng điện từ**: Điện trường biến thiên theo thời gian sinh ra từ trường xoáy; ngược lại, từ trường biến thiên theo thời gian sinh ra điện trường xoáy. Hai trường biến thiên này gắn kết tạo thành **điện từ trường** lan truyền trong không gian dưới dạng **sóng điện từ** với tốc độ trong chân không $c \approx 3 \times 10^8\text{ m/s}$, bước sóng $\lambda = \dfrac{c}{f} = cT$."
        ),
        "theory": (
            r"### Bài 17. Máy phát điện xoay chiều" "\n"
            r"- **Cấu tạo máy phát điện xoay chiều**: Gồm hai bộ phận chính là **phần cảm** (nam châm vĩnh cửu hoặc nam châm điện tạo ra từ trường, thường là rôto trong các máy công suất lớn) và **phần ứng** (các cuộn dây dẫn trong đó xuất hiện suất điện động cảm ứng, thường là stato). Nếu rôto có $p$ cặp cực quay với tốc độ $n$ ($\text{vòng/s}$) thì tần số dòng điện xoay chiều là $f = pn$ (hoặc $f = \dfrac{pn}{60}$ nếu $n$ tính bằng $\text{vòng/phút}$)." "\n"
            r"- **Quan hệ pha giữa từ thông và suất điện động**: Suất điện động cảm ứng $e$ luôn trễ pha $\dfrac{\pi}{2}$ so với từ thông $\Phi$ qua khung dây; do đó tại thời điểm từ thông có độ lớn cực đại ($|\Phi| = \Phi_0$) thì $e = 0$, và khi $\Phi = 0$ thì $|e| = E_0$." "\n"
            r"- **Giá trị hiệu dụng và Công suất toả nhiệt**: Công suất toả nhiệt trung bình trên điện trở $R$ là $\mathcal{P} = I^2 R = \dfrac{I_0^2}{2}R = \dfrac{U^2}{R}$. Ở mạng điện dân dụng Việt Nam, điện áp xoay chiều có giá trị hiệu dụng $U = 220\text{ V}$ (cực đại $U_0 = 220\sqrt{2} \approx 311\text{ V}$) và tần số $f = 50\text{ Hz}$ (chu kì $T = 0{,}02\text{ s}$, dòng điện đổi chiều $2f = 100\text{ lần}$ trong mỗi giây)." "\n"
            r"### Bài 18. Ứng dụng hiện tượng cảm ứng điện từ" "\n"
            r"- **Phanh điện từ (hãm điện từ)**: Đĩa kim loại quay qua vùng từ trường mạnh của nam châm điện làm xuất hiện dòng điện Foucault trong đĩa; theo định luật Lenz, lực từ tác dụng lên dòng Foucault sinh ra mômen cản chuyển động quay mà không gây mài mòn cơ học." "\n"
            r"- **Bếp từ**: Cuộn dây dưới mặt bếp có dòng điện xoay chiều tần số cao ($20\text{ kHz} - 30\text{ kHz}$) chạy qua tạo ra từ trường biến thiên xuyên qua đáy nồi nhiễm từ, sinh ra dòng điện Foucault làm nóng trực tiếp đáy nồi với hiệu suất cao." "\n"
            r"- **Đàn guitar điện**: Dây đàn bằng thép nằm trên cuộn dây cảm ứng (pickup) gắn nam châm vĩnh cửu; khi gảy đàn, đoạn dây đàn nhiễm từ dao động làm biến thiên từ thông qua cuộn dây, tạo ra tín hiệu điện xoay chiều có cùng tần số với âm thanh đưa tới bộ khuếch đại." "\n"
            r"### Bài 19. Điện từ trường. Mô hình sóng điện từ" "\n"
            r"- **Thuyết điện từ Maxwell**: Xung quanh một từ trường biến thiên xuất hiện một điện trường xoáy (có đường sức là những đường cong khép kín); xung quanh một điện trường biến thiên xuất hiện một từ trường xoáy." "\n"
            r"- **Đặc điểm của sóng điện từ**: (1) Truyền được trong mọi môi trường vật chất (rắn, lỏng, khí) và cả trong **chân không** với tốc độ $c \approx 3 \times 10^8\text{ m/s}$ (trong môi trường chiết suất $n$, tốc độ là $v = \dfrac{c}{n}$); (2) Là **sóng ngang**: tại mọi điểm trên phương truyền sóng, $\vec{E} \perp \vec{B}$ và cả hai đều vuông góc với phương truyền sóng $\vec{v}$ sao cho $(\vec{E}, \vec{B}, \vec{v})$ lập thành một tam diện thuận; (3) Tại mỗi điểm, cường độ điện trường $E$ và cảm ứng từ $B$ luôn **biến thiên cùng pha** ($\dfrac{E}{E_0} = \dfrac{B}{B_0}$); (4) Sóng điện từ mang năng lượng và tuân theo các quy luật truyền thẳng, phản xạ, khúc xạ, giao thoa, nhiễu xạ." "\n"
            r"### Bài 20. Bài tập về từ trường" "\n"
            r"- **Tổng hợp các dạng toán Chương III**: Kết hợp bài toán lực từ – cân bằng thanh dẫn, bài toán từ thông – suất điện động máy phát điện xoay chiều $E_0 = NBS\omega$, bài toán giá trị hiệu dụng và bài toán bước sóng điện từ $\lambda = \dfrac{c}{f}$."
        ),
        "formulas": [
            G(
                "I. Máy phát điện xoay chiều và Suất điện động cảm ứng",
                F("Từ thông qua khung dây quay đều", r"$\Phi = \Phi_0\cos(\omega t + \varphi_0)$ với $\Phi_0 = NBS$", r"$\omega = 2\pi f = \dfrac{2\pi}{T}$ ($\text{rad/s}$)."),
                F("Suất điện động xoay chiều", r"$e = E_0\cos\left(\omega t + \varphi_0 - \dfrac{\pi}{2}\right)$ với $E_0 = NBS\omega = \Phi_0\omega$", r"$e$ trễ pha $\dfrac{\pi}{2}$ so với $\Phi$; hệ thức độc lập: $\left(\dfrac{\Phi}{\Phi_0}\right)^2 + \left(\dfrac{e}{E_0}\right)^2 = 1$."),
                F("Tần số máy phát có $p$ cặp cực", r"$f = pn\text{ (với }n\text{ vòng/s)} = \dfrac{pn}{60}\text{ (với }n\text{ vòng/phút)}$", r"Số lần dòng điện đổi chiều trong $1\text{ s}$ (nếu tại $t=0$ thì $i=0$) là $2f$."),
            ),
            G(
                "II. Đại lượng đặc trưng của Dòng điện xoay chiều",
                F("Giá trị hiệu dụng", r"$I = \dfrac{I_0}{\sqrt{2}}; \quad U = \dfrac{U_0}{\sqrt{2}}; \quad E = \dfrac{E_0}{\sqrt{2}}$", r"Xác định dựa trên tác dụng nhiệt của dòng điện."),
                F("Công suất và Nhiệt lượng toả ra trên điện trở $R$", r"$\mathcal{P} = I^2 R = \dfrac{I_0^2}{2}R = UI\cos\varphi; \quad Q = I^2 R t$", r"Với đoạn mạch chỉ chứa điện trở thuần $R$ thì $\cos\varphi = 1$."),
            ),
            G(
                "III. Điện từ trường và Sóng điện từ",
                F("Bước sóng điện từ trong chân không", r"$\lambda = cT = \dfrac{c}{f}$", r"Tốc độ ánh sáng trong chân không $c = 3 \times 10^8\text{ m/s}$."),
                F(r"Quan hệ cùng pha giữa $\vec{E}$ và $\vec{B}$", r"$\dfrac{E}{E_0} = \dfrac{B}{B_0} = \cos(\omega t - kx + \varphi)$", r"Ba vectơ $(\vec{E}, \vec{B}, \vec{v})$ đôi một vuông góc theo quy tắc đinh ốc thuận."),
            ),
        ],
        "example": (
            r"Một khung dây dẫn phẳng gồm $N = 250\text{ vòng}$ dây, diện tích mỗi vòng là $S = 200\text{ cm}^2$, quay đều với tốc độ $n = 3000\text{ vòng/phút}$ "
            r"quanh một trục cố định nằm trong mặt phẳng khung dây và vuông góc với các đường sức của một từ trường đều có cảm ứng từ $B = \dfrac{0{,}2}{\pi}\text{ T}$. "
            r"Chọn gốc thời gian $t = 0$ lúc vectơ pháp tuyến $\vec{n}$ của khung dây cùng hướng với vectơ cảm ứng từ $\vec{B}$. "
            r"a) Tìm tần số $f$, từ thông cực đại $\Phi_0$ và suất điện động cực đại $E_0$, hiệu dụng $E$. "
            r"b) Viết biểu thức từ thông $\Phi(t)$ và suất điện động cảm ứng $e(t)$ trong khung dây."
        ),
        "example_answer": (
            r"- **Câu a**: Đổi $S = 200\text{ cm}^2 = 0{,}02\text{ m}^2$; tốc độ quay $f = \dfrac{n}{60} = \dfrac{3000}{60} = \mathbf{50\text{ Hz}} \Rightarrow \omega = 2\pi f = 100\pi\text{ rad/s}$." "\n"
            r"  Từ thông cực đại qua khung: $\Phi_0 = NBS = 250 \cdot \dfrac{0{,}2}{\pi} \cdot 0{,}02 = \mathbf{\dfrac{1}{\pi}\text{ Wb}} \approx 0{,}318\text{ Wb}$." "\n"
            r"  Suất điện động cực đại: $E_0 = \Phi_0\omega = \dfrac{1}{\pi} \cdot 100\pi = \mathbf{100\text{ V}}$. Suất điện động hiệu dụng: $E = \dfrac{E_0}{\sqrt{2}} = \mathbf{50\sqrt{2}\text{ V}} \approx 70{,}7\text{ V}$." "\n"
            r"- **Câu b**: Tại $t = 0$, $\vec{n} \uparrow\uparrow \vec{B}$ nên $\varphi_0 = 0$. Do đó:" "\n"
            r"  $\Phi(t) = \dfrac{1}{\pi}\cos(100\pi t)\text{ (Wb)}$ và $e(t) = 100\cos\left(100\pi t - \dfrac{\pi}{2}\right)\text{ (V)}$."
        ),
        "real_life": (
            r"- **Nhà máy thuỷ điện, nhiệt điện và điện gió**: Các tuabin quay rôto máy phát điện xoay chiều công suất lớn tạo ra dòng điện xoay chiều tần số $50\text{ Hz}$ hoà vào lưới điện quốc gia." "\n"
            r"- **Bếp từ gia đình, sạc không dây điện thoại và thẻ từ NFC**: Ứng dụng trực tiếp dòng điện Foucault và hiện tượng cảm ứng điện từ để truyền năng lượng hoặc dữ liệu không tiếp xúc." "\n"
            r"- **Truyền thông vô tuyến, mạng $5\text{G}$, Wi-Fi và hệ thống định vị vệ tinh GPS**: Sử dụng sóng điện từ có bước sóng từ vùng vi ba đến sóng vô tuyến để truyền tải thông tin với tốc độ ánh sáng $c = 3 \times 10^8\text{ m/s}$."
        ),
        "game_title": "Mô phỏng Máy phát điện Xoay chiều và Sóng điện từ 3D",
        "game_description": "Điều chỉnh tốc độ quay của khung dây trong từ trường để quan sát đồ thị từ thông – suất điện động xoay chiều và khảo sát sự lan truyền của hai vectơ E, B trong sóng điện từ.",
        "game_type": "game_mach_xoay_chieu",
        "quiz": [
            mcq(
                "biet",
                r"Một dòng điện xoay chiều có biểu thức cường độ tức thời $i = I_0\cos(\omega t + \varphi)$ (với $I_0 > 0$). Giá trị hiệu dụng $I$ của cường độ dòng điện này bằng:",
                [
                    r"$I = \dfrac{I_0}{\sqrt{2}}$",
                    r"$I = I_0\sqrt{2}$",
                    r"$I = \dfrac{I_0}{2}$",
                    r"$I = 2I_0$",
                ],
                0,
                r"Giá trị hiệu dụng của cường độ dòng điện xoay chiều hình sin bằng giá trị cực đại chia cho $\sqrt{2}$: $I = \dfrac{I_0}{\sqrt{2}}$.",
            ),
            mcq(
                "biet",
                r"Khi một khung dây phẳng gồm $N$ vòng dây, mỗi vòng có diện tích $S$, quay đều với tốc độ góc $\omega$ quanh trục vuông góc với các đường sức của một từ trường đều có cảm ứng từ $B$ thì suất điện động cực đại $E_0$ xuất hiện trong khung là:",
                [
                    r"$E_0 = NBS\omega$",
                    r"$E_0 = \dfrac{NBS}{\omega}$",
                    r"$E_0 = NBS\omega^2$",
                    r"$E_0 = \dfrac{NB\omega}{S}$",
                ],
                0,
                r"Từ $\Phi = NBS\cos(\omega t + \varphi_0)$ suy ra $e = -\Phi'(t) = NBS\omega\sin(\omega t + \varphi_0)$, nên biên độ suất điện động là $E_0 = NBS\omega$.",
            ),
            mcq(
                "biet",
                r"Trong quá trình lan truyền của sóng điện từ trong chân không, tại một điểm bất kì trên phương truyền sóng, vectơ cường độ điện trường $\vec{E}$ và vectơ cảm ứng từ $\vec{B}$ luôn:",
                [
                    r"Có phương vuông góc với nhau và dao động cùng pha",
                    r"Có phương trùng nhau và dao động ngược pha",
                    r"Có phương vuông góc với nhau và dao động lệch pha $\dfrac{\pi}{2}$",
                    r"Có phương song song với phương truyền sóng và dao động cùng pha",
                ],
                0,
                r"Sóng điện từ là sóng ngang: $\vec{E} \perp \vec{B} \perp \vec{v}$ theo tam diện thuận, nhưng về mặt thời gian thì $E$ và $B$ tại cùng một điểm luôn biến thiên **cùng pha**.",
            ),
            mcq(
                "biet",
                r"Thiết bị nào sau đây hoạt động dựa trên tác dụng nhiệt của dòng điện Foucault (dòng điện xoáy) sinh ra trong đáy nồi kim loại nhiễm từ?",
                [
                    r"Bếp từ",
                    r"Bếp hồng ngoại (bếp điện trở)",
                    r"Lò vi sóng",
                    r"Ấm đun nước siêu tốc dùng dây mayso",
                ],
                0,
                r"**Bếp từ** tạo ra từ trường biến thiên tần số cao xuyên qua đáy nồi nhiễm từ, sinh ra dòng điện Foucault làm nóng trực tiếp đáy nồi.",
            ),
            mcq(
                "hieu",
                r"Mạng điện xoay chiều dân dụng ở Việt Nam có biểu thức điện áp $u = 220\sqrt{2}\cos(100\pi t)\text{ (V)}$. Điện áp hiệu dụng $U$ và tần số $f$ của mạng điện này lần lượt là:",
                [
                    r"$U = 220\text{ V}$ và $f = 50\text{ Hz}$",
                    r"$U = 220\sqrt{2}\text{ V}$ và $f = 50\text{ Hz}$",
                    r"$U = 220\text{ V}$ và $f = 100\text{ Hz}$",
                    r"$U = 110\sqrt{2}\text{ V}$ và $f = 100\pi\text{ Hz}$",
                ],
                0,
                r"Từ $u = U_0\cos(\omega t)$ với $U_0 = 220\sqrt{2}\text{ V}$ và $\omega = 100\pi\text{ rad/s}$, ta có $U = \dfrac{U_0}{\sqrt{2}} = 220\text{ V}$ và $f = \dfrac{\omega}{2\pi} = \dfrac{100\pi}{2\pi} = 50\text{ Hz}$.",
            ),
            mcq(
                "hieu",
                r"Một đài phát thanh FM phát ra sóng điện từ có tần số $f = 100\text{ MHz}$ truyền trong không khí với tốc độ $c = 3 \times 10^8\text{ m/s}$. Bước sóng $\lambda$ của sóng điện từ này là:",
                [
                    r"$3{,}0\text{ m}$",
                    r"$30\text{ m}$",
                    r"$0{,}33\text{ m}$",
                    r"$300\text{ m}$",
                ],
                0,
                r"Đổi $f = 100\text{ MHz} = 10^8\text{ Hz}$. Bước sóng của sóng điện từ: $\lambda = \dfrac{c}{f} = \dfrac{3 \times 10^8}{10^8} = \mathbf{3{,}0\text{ m}}$.",
            ),
            tf4(
                "hieu",
                r"Xét một khung dây dẫn phẳng quay đều trong từ trường đều tạo ra từ thông $\Phi = \Phi_0\cos(\omega t)$ và suất điện động cảm ứng $e = E_0\cos\left(\omega t - \dfrac{\pi}{2}\right)$. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Suất điện động cảm ứng $e$ trong khung dây biến thiên điều hoà cùng tần số nhưng trễ pha $\dfrac{\pi}{2}$ so với từ thông $\Phi$.",
                    r"b) Tại thời điểm từ thông qua khung dây có độ lớn cực đại ($|\Phi| = \Phi_0$) thì độ lớn suất điện động cảm ứng trong khung cũng đạt cực đại ($|e| = E_0$).",
                    r"c) Nếu giữ nguyên từ trường nhưng tăng tốc độ quay của khung dây lên gấp đôi thì cả tần số $f$ và biên độ suất điện động $E_0$ đều tăng gấp đôi.",
                    r"d) Khi nối hai đầu khung dây với một vôn kế xoay chiều lí tưởng thì số chỉ của vôn kế là $E_0$.",
                ],
                [True, False, True, False],
                r"- **a) Đúng**: Từ biểu thức thấy ngay $e$ cùng tần số góc $\omega$ và trễ pha $\dfrac{\pi}{2}$ so với $\Phi$." "\n"
                r"- **b) Sai**: Vì $e$ và $\Phi$ vuông pha nên khi $|\Phi| = \Phi_0$ thì $e = 0$ (tốc độ biến thiên từ thông tại đỉnh bằng $0$)." "\n"
                r"- **c) Đúng**: Vì $f = \dfrac{\omega}{2\pi} \propto \omega$ và $E_0 = NBS\omega \propto \omega$, nên khi $\omega$ tăng gấp đôi thì cả $f$ và $E_0$ đều tăng gấp đôi." "\n"
                r"- **d) Sai**: Vôn kế xoay chiều đo **giá trị hiệu dụng** $E = \dfrac{E_0}{\sqrt{2}}$, không phải giá trị cực đại $E_0$.",
            ),
            tf4(
                "hieu",
                r"Xét tính đúng hay sai của các phát biểu sau về sóng điện từ và ứng dụng hiện tượng cảm ứng điện từ:",
                [
                    r"a) Khác với sóng cơ học, sóng điện từ truyền được trong chân không với tốc độ $c \approx 3 \times 10^8\text{ m/s}$.",
                    r"b) Khi sóng điện từ lan truyền theo phương thẳng đứng từ dưới lên trên, nếu tại một điểm và một thời điểm vectơ $\vec{E}$ hướng về phía Bắc thì vectơ $\vec{B}$ hướng về phía Đông (theo quy tắc tam diện thuận).",
                    r"c) Để tăng hiệu quả của dòng điện Foucault trong lõi máy biến áp, người ta chế tạo lõi máy biến áp bằng một khối thép đặc nguyên khối.",
                    r"d) Tại một điểm trong không gian có sóng điện từ truyền qua với cảm ứng từ cực đại $B_0 = 0{,}12\text{ T}$ và cường độ điện trường cực đại $E_0 = 600\text{ V/m}$, ở thời điểm $E = 300\text{ V/m}$ thì cảm ứng từ có độ lớn $B = 0{,}06\text{ T}$.",
                ],
                [True, True, False, True],
                r"- **a) Đúng**: Sóng điện từ là sự lan truyền của điện từ trường nên truyền được cả trong chân không." "\n"
                r"- **b) Đúng**: Theo quy tắc đinh ốc thuận $(\vec{E}, \vec{B}, \vec{v})$, khi quay từ hướng Bắc ($\vec{E}$) sang hướng Đông ($\vec{B}$) thì chiều tiến của đinh ốc hướng thẳng đứng từ dưới lên trên ($\vec{v}$)." "\n"
                r"- **c) Sai**: Trong lõi máy biến áp, dòng điện Foucault gây toả nhiệt hao phí nên người ta phải **giảm** dòng Foucault bằng cách ghép lõi từ các lá thép kĩ thuật điện mỏng sơn cách điện với nhau." "\n"
                r"- **d) Đúng**: Vì $E$ và $B$ biến thiên cùng pha nên $\dfrac{B}{B_0} = \dfrac{E}{E_0} = \dfrac{300}{600} = 0{,}5 \Rightarrow B = 0{,}5 \cdot 0{,}12 = 0{,}06\text{ T}$.",
            ),
            mcq(
                "vandung",
                r"Cho dòng điện xoay chiều có biểu thức $i = 4\sqrt{2}\cos(100\pi t)\text{ (A)}$ chạy qua một điện trở thuần $R = 25\text{ }\Omega$. Nhiệt lượng toả ra trên điện trở này trong thời gian $t = 2\text{ phút}$ là:",
                [
                    r"$48\text{ kJ}$",
                    r"$96\text{ kJ}$",
                    r"$24\text{ kJ}$",
                    r"$800\text{ J}$",
                ],
                0,
                r"Cường độ dòng điện hiệu dụng là $I = \dfrac{I_0}{\sqrt{2}} = \dfrac{4\sqrt{2}}{\sqrt{2}} = 4\text{ A}$. Đổi $t = 2\text{ phút} = 120\text{ s}$. Nhiệt lượng toả ra trên điện trở: $Q = I^2 R t = 4^2 \cdot 25 \cdot 120 = 48\,000\text{ J} = \mathbf{48\text{ kJ}}$.",
            ),
            short(
                "vandung",
                r"Một máy phát điện xoay chiều một pha có phần cảm là rôto gồm $p = 4$ cặp cực từ. Để tạo ra suất điện động xoay chiều có tần số $f = 50\text{ Hz}$ thì rôto phải quay với tốc độ bằng bao nhiêu $\text{vòng/phút}$?",
                ["750"],
                r"Áp dụng công thức tần số của máy phát điện xoay chiều với $n$ tính bằng $\text{vòng/phút}$: $f = \dfrac{pn}{60} \Rightarrow n = \dfrac{60f}{p} = \dfrac{60 \cdot 50}{4} = \mathbf{750}\text{ vòng/phút}$.",
                unit=r"$\text{vòng/phút}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG IV. VẬT LÍ HẠT NHÂN VÀ PHÓNG XẠ (Bài 21 – Bài 25 SGK Vật lí 12 KNTT)
    # =========================================================================
    {
        "topic": "hat-nhan",
        "title": "Chương IV. Vật lí hạt nhân và Phóng xạ",
        "icon": "☢️",
        "description": (
            "Chương IV · SGK Vật lí 12 Kết nối tri thức với cuộc sống (Bài 21 – Bài 25): "
            "Cấu trúc hạt nhân (thí nghiệm tán xạ hạt alpha, nucleon, đồng vị, bán kính hạt nhân); "
            "Phản ứng hạt nhân, hệ thức Einstein, độ hụt khối và năng lượng liên kết; "
            "Hiện tượng phóng xạ, chu kì bán rã và độ phóng xạ; Công nghiệp hạt nhân và bài tập vật lí hạt nhân."
        ),
        "requirements": [
            r"Rút ra được sự tồn tại và kích thước rất nhỏ của hạt nhân từ kết quả thí nghiệm tán xạ hạt alpha ($\alpha$) của Rutherford; biểu diễn được kí hiệu hạt nhân ${}_Z^A\text{X}$ và nêu được khái niệm đồng vị.",
            r"Nêu được bản chất của lực hạt nhân là lực tương tác mạnh giữa các nucleon trong phạm vi kích thước hạt nhân ($\sim 10^{-15}\text{ m}$); sử dụng được đơn vị khối lượng nguyên tử $\text{amu}$ ($1\text{ amu} \approx 931{,}5\text{ MeV}/c^2$).",
            r"Nêu được mối liên hệ giữa năng lượng và khối lượng theo hệ thức Einstein $E = mc^2$; định nghĩa và tính được độ hụt khối $\Delta m = [Zm_p + (A - Z)m_n] - m_{\text{X}}$, năng lượng liên kết $W_{\text{lk}} = \Delta m \cdot c^2$ và năng lượng liên kết riêng $W_{\text{lkr}} = \dfrac{W_{\text{lk}}}{A}$ để so sánh mức độ bền vững của các hạt nhân.",
            r"Nêu được khái niệm phản ứng hạt nhân (tự phát và kích thích), các định luật bảo toàn trong phản ứng hạt nhân (bảo toàn số nucleon $A$, bảo toàn điện tích $Z$, bảo toàn năng lượng toàn phần và bảo toàn động lượng), phản ứng phân hạch và phản ứng tổng hợp hạt nhân (nhiệt hạch).",
            r"Nêu được bản chất tự phát, ngẫu nhiên của sự phóng xạ và đặc điểm của ba loại tia phóng xạ $\alpha$ (${}_{2}^{4}\text{He}$), $\beta$ ($\beta^-$ là ${}_{ -1}^{0}\text{e}$, $\beta^+$ là ${}_{ +1}^{0}\text{e}$) và $\gamma$ (photon năng lượng cao).",
            r"Định nghĩa được chu kì bán rã $T$, hằng số phóng xạ $\lambda = \dfrac{\ln 2}{T}$, độ phóng xạ $H = \lambda N$ (đơn vị becquerel $\text{Bq}$) và vận dụng được các công thức định luật phóng xạ $N(t) = N_0 \cdot 2^{-\frac{t}{T}} = N_0 e^{-\lambda t}$, $H(t) = H_0 \cdot 2^{-\frac{t}{T}}$.",
            r"Mô tả được nguyên tắc hoạt động của nhà máy điện hạt nhân, các ứng dụng của đồng vị phóng xạ trong y học, nông nghiệp, khảo cổ học (${}_{6}^{14}\text{C}$) và các quy tắc an toàn phóng xạ.",
        ],
        "definition": (
            r"- **Cấu trúc hạt nhân (${}_Z^A\text{X}$)**: Hạt nhân nguyên tử có điện tích $+Ze$, cấu tạo từ $A$ **nucleon** gồm $Z$ **proton** ($m_p \approx 1{,}00728\text{ amu}$) và $N = A - Z$ **neutron** ($m_n \approx 1{,}00866\text{ amu}$). Bán kính hạt nhân: $R = R_0 A^{\frac{1}{3}}$ với $R_0 \approx 1{,}2 \times 10^{-15}\text{ m}$. **Đồng vị** là các hạt nhân có cùng số proton $Z$ nhưng khác nhau số neutron $N$ (khác số khối $A$)." "\n"
            r"- **Độ hụt khối và Năng lượng liên kết**: Khối lượng của một hạt nhân luôn nhỏ hơn tổng khối lượng của các nucleon tạo thành nó một lượng gọi là **độ hụt khối**: $\Delta m = [Zm_p + (A - Z)m_n] - m_{\text{X}}$. **Năng lượng liên kết** $W_{\text{lk}} = \Delta m \cdot c^2$ là năng lượng tối thiểu cần cung cấp để tách hạt nhân thành các nucleon riêng rẽ. **Năng lượng liên kết riêng** $W_{\text{lkr}} = \dfrac{W_{\text{lk}}}{A}$ đặc trưng cho mức độ bền vững của hạt nhân (các hạt nhân trung bình có $50 \le A \le 80$ như ${}_{26}^{56}\text{Fe}$ có $W_{\text{lkr}} \approx 8{,}8\text{ MeV/nucleon}$ lớn nhất nên bền vững nhất)." "\n"
            r"- **Phản ứng hạt nhân**: Trong phản ứng ${}_{Z_1}^{A_1}\text{X}_1 + {}_{Z_2}^{A_2}\text{X}_2 \rightarrow {}_{Z_3}^{A_3}\text{X}_3 + {}_{Z_4}^{A_4}\text{X}_4$, luôn bảo toàn số nucleon ($A_1 + A_2 = A_3 + A_4$) và bảo toàn số nguyên tử hay điện tích ($Z_1 + Z_2 = Z_3 + Z_4$). Năng lượng phản ứng hạt nhân: $\Delta E = (m_{\text{trước}} - m_{\text{sau}})c^2$; nếu $\Delta E > 0$ thì phản ứng toả năng lượng, nếu $\Delta E < 0$ thì phản ứng thu năng lượng." "\n"
            r"- **Định luật phóng xạ và Độ phóng xạ**: Số hạt nhân (và khối lượng) chất phóng xạ còn lại sau thời gian $t$: $N(t) = N_0 \cdot 2^{-\frac{t}{T}} = N_0 e^{-\lambda t}$ và $m(t) = m_0 \cdot 2^{-\frac{t}{T}}$, với hằng số phóng xạ $\lambda = \dfrac{\ln 2}{T}$. **Độ phóng xạ** $H(t) = \lambda N(t) = H_0 \cdot 2^{-\frac{t}{T}}$ (đơn vị trong hệ SI là **becquerel**, ký hiệu $\text{Bq}$, $1\text{ Bq} = 1\text{ phân rã/s}$; $1\text{ Ci} = 3{,}7 \times 10^{10}\text{ Bq}$)."
        ),
        "theory": (
            r"### Bài 21. Cấu trúc hạt nhân" "\n"
            r"- **Thí nghiệm tán xạ hạt alpha ($\alpha$) của Rutherford**: Chùm hạt $\alpha$ (${}_{2}^{4}\text{He}$) bắn vào lá vàng cực mỏng thì hầu hết đi thẳng, chỉ một tỉ lệ rất nhỏ bị lệch góc lớn hoặc bật ngược trở lại. Điều này chứng tỏ nguyên tử có cấu tạo rỗng, toàn bộ điện tích dương và gần như toàn bộ khối lượng nguyên tử tập trung tại **hạt nhân** có kích thước rất nhỏ ($\sim 10^{-15}\text{ m} - 10^{-14}\text{ m}$) so với kích thước nguyên tử ($\sim 10^{-10}\text{ m}$)." "\n"
            r"- **Đơn vị khối lượng nguyên tử ($\text{amu}$)**: $1\text{ amu}$ bằng $\dfrac{1}{12}$ khối lượng nguyên tử đồng vị carbon ${}_{6}^{12}\text{C}$: $1\text{ amu} \approx 1{,}66054 \times 10^{-27}\text{ kg} \approx 931{,}5\text{ MeV}/c^2$." "\n"
            r"### Bài 22. Phản ứng hạt nhân và năng lượng liên kết" "\n"
            r"- **Lực hạt nhân**: Là lực hút tương tác mạnh giữa các nucleon (proton – proton, neutron – neutron, proton – neutron), không phụ thuộc vào điện tích và chỉ phát huy tác dụng trong phạm vi bán kính khoảng $10^{-15}\text{ m}$." "\n"
            r"- **Phản ứng phân hạch**: Là phản ứng trong đó một hạt nhân nặng (như ${}_{92}^{235}\text{U}$ hoặc ${}_{94}^{239}\text{Pu}$) hấp thụ một neutron chậm rồi vỡ thành hai hạt nhân trung bình kèm theo $2$ đến $3$ neutron mới và toả ra năng lượng lớn (khoảng $200\text{ MeV}$ cho mỗi phân hạch). Nếu số neutron trung bình sau mỗi phân hạch tiếp tục gây phân hạch mới là $k = 1$, ta có phản ứng dây chuyền tự duy trì có điều khiển (trong lò phản ứng hạt nhân)." "\n"
            r"- **Phản ứng tổng hợp hạt nhân (nhiệt hạch)**: Là quá trình hai hạt nhân rất nhẹ (như ${}_{1}^{2}\text{H}$ và ${}_{1}^{3}\text{H}$) kết hợp thành một hạt nhân nặng hơn (${}_{2}^{4}\text{He}$) ở nhiệt độ cực cao (hàng chục đến hàng trăm triệu độ Kelvin), toả ra năng lượng tính trên một đơn vị khối lượng nhiên liệu lớn hơn nhiều so với phân hạch." "\n"
            r"### Bài 23. Hiện tượng phóng xạ" "\n"
            r"- **Ba loại tia phóng xạ**: (1) **Phóng xạ $\alpha$**: ${}_Z^A\text{X} \rightarrow {}_{Z-2}^{A-4}\text{Y} + {}_{2}^{4}\text{He}$ (khả năng ion hoá mạnh nhưng đâm xuyên yếu, bị chặn bởi một tờ giấy); (2) **Phóng xạ $\beta^-$**: ${}_Z^A\text{X} \rightarrow {}_{Z+1}^{A}\text{Y} + {}_{-1}^{0}\text{e} + \tilde{\nu}$ và **phóng xạ $\beta^+$**: ${}_Z^A\text{X} \rightarrow {}_{Z-1}^{A}\text{Y} + {}_{+1}^{0}\text{e} + \nu$ (bị lệch trong điện trường và từ trường, đâm xuyên mạnh hơn tia $\alpha$); (3) **Phóng xạ $\gamma$**: Là sóng điện từ bước sóng rất ngắn ($\lambda < 10^{-11}\text{ m}$), không mang điện, không làm thay đổi $A$ và $Z$, khả năng đâm xuyên rất mạnh (cần tấm chì dày hoặc bê tông dày để chắn)." "\n"
            r"- **Chu kì bán rã ($T$) và Độ phóng xạ ($H$)**: Sau mỗi chu kì bán rã $T$, một nửa số hạt nhân hiện có bị phân rã. Số hạt nhân đã bị phân rã (bằng số hạt nhân con tạo thành) sau thời gian $t$ là $\Delta N = N_0 - N(t) = N_0\left(1 - 2^{-\frac{t}{T}}\right)$." "\n"
            r"### Bài 24. Công nghiệp hạt nhân" "\n"
            r"- **Nhà máy điện hạt nhân**: Nhiệt năng toả ra từ phản ứng phân hạch dây chuyền có điều khiển ($k = 1$, dùng các thanh điều khiển chứa boron hoặc cadmium để hấp thụ neutron thừa) được chất tải nhiệt đưa tới sinh hơi làm quay tuabin máy phát điện." "\n"
            r"- **Ứng dụng trong y học, nông nghiệp, công nghiệp và khảo cổ**: Xạ trị ung thư bằng đồng vị ${}_{27}^{60}\text{Co}$ hoặc dược chất phóng xạ ${}_{53}^{131}\text{I}$; chiếu xạ bảo quản thực phẩm và tạo giống cây trồng đột biến; kiểm tra khuyết tật mối hàn kim loại; định tuổi cổ vật hữu cơ bằng đồng vị ${}_{6}^{14}\text{C}$ ($T \approx 5730\text{ năm}$)." "\n"
            r"- **Ba nguyên tắc cơ bản về an toàn phóng xạ**: (1) **Giảm thời gian** tiếp xúc với nguồn phóng xạ; (2) **Tăng khoảng cách** tới nguồn phóng xạ; (3) **Che chắn** bằng các vật liệu hấp thụ thích hợp (chì, bê tông)." "\n"
            r"### Bài 25. Bài tập về vật lí hạt nhân" "\n"
            r"- **Các dạng bài tập trọng tâm**: Tính độ hụt khối $\Delta m$, năng lượng liên kết $W_{\text{lk}}$ và năng lượng liên kết riêng $W_{\text{lkr}}$; cân bằng phương trình phản ứng hạt nhân và tính năng lượng thu vào hoặc toả ra $\Delta E$; bài toán định luật phóng xạ tìm $N(t)$, $m(t)$, độ phóng xạ $H(t)$ và tỉ số $\dfrac{N_{\text{Y}}}{N_{\text{X}}} = 2^{\frac{t}{T}} - 1$."
        ),
        "formulas": [
            G(
                "I. Cấu trúc hạt nhân, Độ hụt khối và Năng lượng liên kết",
                F("Số khối và Bán kính hạt nhân", r"$A = Z + N; \quad R = R_0 A^{\frac{1}{3}}\text{ (với }R_0 \approx 1{,}2 \times 10^{-15}\text{ m)}$", r"Thể tích hạt nhân tỉ lệ thuận với số khối $A$."),
                F(r"Độ hụt khối của hạt nhân ${}_Z^A\text{X}$", r"$\Delta m = [Zm_p + (A - Z)m_n] - m_{\text{X}}$", r"$1\text{ amu} \approx 931{,}5\text{ MeV}/c^2$."),
                F("Năng lượng liên kết và Năng lượng liên kết riêng", r"$W_{\text{lk}} = \Delta m \cdot c^2; \quad W_{\text{lkr}} = \dfrac{W_{\text{lk}}}{A}$", r"$W_{\text{lkr}}$ càng lớn thì hạt nhân càng bền vững."),
            ),
            G(
                "II. Các định luật bảo toàn và Năng lượng phản ứng hạt nhân",
                F("Bảo toàn số nucleon và Bảo toàn điện tích", r"$A_1 + A_2 = A_3 + A_4; \quad Z_1 + Z_2 = Z_3 + Z_4$", r"Áp dụng cho mọi phản ứng hạt nhân và phân rã phóng xạ."),
                F("Năng lượng phản ứng hạt nhân", r"$\Delta E = (m_{\text{trước}} - m_{\text{sau}})c^2 = W_{\text{lk sau}} - W_{\text{lk trước}} = W_{\text{đ sau}} - W_{\text{đ trước}}$", r"$\Delta E > 0$: phản ứng toả năng lượng; $\Delta E < 0$: phản ứng thu năng lượng."),
            ),
            G(
                "III. Định luật Phóng xạ và Độ phóng xạ",
                F("Số hạt nhân và Khối lượng còn lại", r"$N(t) = N_0 \cdot 2^{-\frac{t}{T}} = N_0 e^{-\lambda t}; \quad m(t) = m_0 \cdot 2^{-\frac{t}{T}}$", r"Hằng số phóng xạ: $\lambda = \dfrac{\ln 2}{T} \approx \dfrac{0{,}693}{T}$."),
                F("Số hạt nhân bị phân rã và Tỉ số hạt con trên hạt mẹ", r"$\Delta N = N_0\left(1 - 2^{-\frac{t}{T}}\right); \quad \dfrac{N_{\text{con}}}{N_{\text{mẹ}}} = \dfrac{\Delta N}{N(t)} = 2^{\frac{t}{T}} - 1$", r"Khối lượng hạt nhân con sinh ra: $m_{\text{con}} = \dfrac{A_{\text{con}}}{A_{\text{mẹ}}} m_0\left(1 - 2^{-\frac{t}{T}}\right)$."),
                F("Độ phóng xạ", r"$H(t) = \lambda N(t) = \dfrac{\ln 2}{T}N(t) = H_0 \cdot 2^{-\frac{t}{T}}$", r"Đơn vị: $\text{Bq}$ (khi $T$ tính bằng giây $\text{s}$)."),
            ),
        ],
        "example": (
            r"Cho hạt nhân helium ${}_{2}^{4}\text{He}$ có khối lượng $m_{\text{He}} = 4{,}0015\text{ amu}$. Biết khối lượng của proton là $m_p = 1{,}0073\text{ amu}$, "
            r"khối lượng của neutron là $m_n = 1{,}0087\text{ amu}$ và $1\text{ amu} = 931{,}5\text{ MeV}/c^2$. "
            r"a) Tính độ hụt khối $\Delta m$, năng lượng liên kết $W_{\text{lk}}$ và năng lượng liên kết riêng $W_{\text{lkr}}$ của hạt nhân ${}_{2}^{4}\text{He}$. "
            r"b) Một mẫu chất phóng xạ polonium ${}_{84}^{210}\text{Po}$ (phóng xạ $\alpha$ tạo thành hạt nhân chì ${}_{82}^{206}\text{Pb}$) có chu kì bán rã $T = 138\text{ ngày}$ và khối lượng ban đầu $m_0 = 42\text{ g}$. "
            r"Tính khối lượng ${}_{84}^{210}\text{Po}$ còn lại và khối lượng chì ${}_{82}^{206}\text{Pb}$ được tạo thành sau thời gian $t = 276\text{ ngày}$."
        ),
        "example_answer": (
            r"- **Câu a**: Hạt nhân ${}_{2}^{4}\text{He}$ có $Z = 2$ proton và $N = 4 - 2 = 2$ neutron." "\n"
            r"  Độ hụt khối: $\Delta m = (2m_p + 2m_n) - m_{\text{He}} = 2(1{,}0073 + 1{,}0087) - 4{,}0015 = 4{,}0320 - 4{,}0015 = \mathbf{0{,}0305\text{ amu}}$." "\n"
            r"  Năng lượng liên kết: $W_{\text{lk}} = \Delta m \cdot c^2 = 0{,}0305 \cdot 931{,}5 \approx \mathbf{28{,}41\text{ MeV}}$." "\n"
            r"  Năng lượng liên kết riêng: $W_{\text{lkr}} = \dfrac{W_{\text{lk}}}{A} = \dfrac{28{,}41}{4} \approx \mathbf{7{,}10\text{ MeV/nucleon}}$." "\n"
            r"- **Câu b**: Ta có $\dfrac{t}{T} = \dfrac{276}{138} = 2$ chu kì bán rã." "\n"
            r"  Khối lượng ${}_{84}^{210}\text{Po}$ còn lại: $m = m_0 \cdot 2^{-\frac{t}{T}} = 42 \cdot 2^{-2} = \mathbf{10{,}5\text{ g}}$." "\n"
            r"  Số mol ${}_{84}^{210}\text{Po}$ đã bị phân rã là $\Delta n = \dfrac{m_0 - m}{210} = \dfrac{42 - 10{,}5}{210} = 0{,}15\text{ mol}$. Khối lượng chì ${}_{82}^{206}\text{Pb}$ tạo thành là $m_{\text{Pb}} = \Delta n \cdot 206 = 0{,}15 \cdot 206 = \mathbf{30{,}9\text{ g}}$."
        ),
        "real_life": (
            r"- **Y học hạt nhân và điều trị ung thư**: Sử dụng đồng vị phóng xạ ${}_{53}^{131}\text{I}$ ($T = 8\text{ ngày}$) trong chẩn đoán và điều trị bệnh tuyến giáp, tia $\gamma$ từ nguồn ${}_{27}^{60}\text{Co}$ hoặc dao gamma trong xạ trị khối u." "\n"
            r"- **Nhà máy điện hạt nhân và năng lượng sạch**: Một kilôgam ${}_{92}^{235}\text{U}$ phân hạch hoàn toàn toả ra năng lượng tương đương việc đốt cháy khoảng $2500\text{ tấn}$ than đá mà không phát thải khí nhà kính $\text{CO}_2$." "\n"
            r"- **Định tuổi khảo cổ học và địa chất**: Đo độ phóng xạ của đồng vị carbon ${}_{6}^{14}\text{C}$ trong mẫu gỗ, xương cổ để xác định niên đại di chỉ khảo cổ lên tới hàng chục nghìn năm."
        ),
        "game_title": "Mô phỏng Phản ứng Hạt nhân, Phân hạch và Chu kì Bán rã",
        "game_description": "Thực hiện thí nghiệm tán xạ Rutherford, lắp ráp nucleon tính năng lượng liên kết, điều khiển lò phản ứng phân hạch U-235 và khảo sát đường cong phân rã phóng xạ.",
        "game_type": "game_hat_nhan",
        "quiz": [
            mcq(
                "biet",
                r"Số neutron $N$ có trong một hạt nhân uranium ${}_{92}^{235}\text{U}$ là:",
                [
                    r"$143$",
                    r"$92$",
                    r"$235$",
                    r"$327$",
                ],
                0,
                r"Hạt nhân ${}_{92}^{235}\text{U}$ có số khối $A = 235$ và số proton $Z = 92$, suy ra số neutron là $N = A - Z = 235 - 92 = \mathbf{143}$.",
            ),
            mcq(
                "biet",
                r"Đại lượng nào sau đây đặc trưng trực tiếp cho mức độ bền vững của một hạt nhân nguyên tử?",
                [
                    r"Năng lượng liên kết riêng $W_{\text{lkr}} = \dfrac{W_{\text{lk}}}{A}$",
                    r"Độ hụt khối $\Delta m$ của hạt nhân",
                    r"Năng lượng liên kết toàn phần $W_{\text{lk}}$",
                    r"Số khối $A$ của hạt nhân",
                ],
                0,
                r"**Năng lượng liên kết riêng** $W_{\text{lkr}} = \dfrac{W_{\text{lk}}}{A}$ (năng lượng liên kết tính trên một nucleon) càng lớn thì hạt nhân càng bền vững.",
            ),
            mcq(
                "biet",
                r"Trong ba loại tia phóng xạ $\alpha$, $\beta$ và $\gamma$, tia phóng xạ nào có bản chất là sóng điện từ có bước sóng rất ngắn và không bị lệch khi đi qua điện trường hay từ trường?",
                [
                    r"Tia $\gamma$",
                    r"Tia $\alpha$",
                    r"Tia $\beta^-$",
                    r"Tia $\beta^+$",
                ],
                0,
                r"**Tia $\gamma$** là dòng photon có năng lượng rất cao (sóng điện từ bước sóng $\lambda < 10^{-11}\text{ m}$), không mang điện tích nên không bị lệch trong điện trường và từ trường.",
            ),
            mcq(
                "biet",
                r"Gọi $N_0$ là số hạt nhân ban đầu của một mẫu chất phóng xạ có chu kì bán rã $T$. Số hạt nhân $N(t)$ của chất phóng xạ đó còn lại sau khoảng thời gian $t$ được xác định bởi công thức nào?",
                [
                    r"$N(t) = N_0 \cdot 2^{-\frac{t}{T}}$",
                    r"$N(t) = N_0 \cdot 2^{\frac{t}{T}}$",
                    r"$N(t) = N_0\left(1 - 2^{-\frac{t}{T}}\right)$",
                    r"$N(t) = \dfrac{N_0 \cdot T}{2t}$",
                ],
                0,
                r"Theo định luật phóng xạ, số hạt nhân chất phóng xạ còn lại giảm theo hàm mũ: $N(t) = N_0 \cdot 2^{-\frac{t}{T}} = N_0 e^{-\lambda t}$.",
            ),
            mcq(
                "hieu",
                r"Cho phản ứng hạt nhân: ${}_{0}^{1}\text{n} + {}_{92}^{235}\text{U} \rightarrow {}_{56}^{144}\text{Ba} + {}_{36}^{89}\text{Kr} + k\,{}_{0}^{1}\text{n}$. Giá trị của hệ số $k$ (số neutron giải phóng) trong phản ứng phân hạch trên là:",
                [
                    r"$k = 3$",
                    r"$k = 2$",
                    r"$k = 1$",
                    r"$k = 4$",
                ],
                0,
                r"Áp dụng định luật bảo toàn số nucleon (số khối $A$): $1 + 235 = 144 + 89 + k \cdot 1 \Rightarrow 236 = 233 + k \Rightarrow \mathbf{k = 3}$.",
            ),
            mcq(
                "hieu",
                r"Một mẫu chất phóng xạ iodine ${}_{53}^{131}\text{I}$ dùng trong y tế có chu kì bán rã $T = 8\text{ ngày}$ và độ phóng xạ ban đầu là $H_0 = 640\text{ MBq}$. Độ phóng xạ $H$ của mẫu chất này sau $24\text{ ngày}$ là:",
                [
                    r"$80\text{ MBq}$",
                    r"$160\text{ MBq}$",
                    r"$320\text{ MBq}$",
                    r"$40\text{ MBq}$",
                ],
                0,
                r"Ta có $\dfrac{t}{T} = \dfrac{24}{8} = 3$ chu kì bán rã. Độ phóng xạ sau $24\text{ ngày}$ là: $H = H_0 \cdot 2^{-\frac{t}{T}} = 640 \cdot 2^{-3} = \dfrac{640}{8} = \mathbf{80\text{ MBq}}$.",
            ),
            tf4(
                "hieu",
                r"Xét tính đúng hay sai của các phát biểu sau về cấu trúc hạt nhân, lực hạt nhân và hiện tượng phóng xạ:",
                [
                    r"a) Lực hạt nhân là lực tương tác mạnh liên kết các nucleon trong hạt nhân, có bán kính tác dụng rất ngắn vào cỡ $10^{-15}\text{ m}$ và không phụ thuộc vào điện tích của nucleon.",
                    r"b) Trong mọi phản ứng hạt nhân, tổng khối lượng nghỉ của các hạt trước phản ứng luôn bằng tổng khối lượng nghỉ của các hạt sau phản ứng.",
                    r"c) Khi hạt nhân ${}_Z^A\text{X}$ phóng xạ $\alpha$ (${}_{2}^{4}\text{He}$) thì hạt nhân con tạo thành có số khối giảm đi $4$ và số hiệu nguyên tử giảm đi $2$.",
                    r"d) Nếu tăng nhiệt độ và áp suất tác dụng lên một mẫu chất phóng xạ thì chu kì bán rã $T$ của chất phóng xạ đó sẽ giảm xuống.",
                ],
                [True, False, True, False],
                r"- **a) Đúng**: Lực hạt nhân là tương tác mạnh, bán kính tác dụng cỡ kích thước hạt nhân ($\sim 10^{-15}\text{ m}$) và độc lập với điện tích." "\n"
                r"- **b) Sai**: Trong phản ứng hạt nhân không có định luật bảo toàn khối lượng nghỉ (mà bảo toàn số nucleon $A$ và bảo toàn năng lượng toàn phần); độ chênh lệch khối lượng nghỉ chuyển hoá thành năng lượng thu vào hoặc toả ra $\Delta E = \Delta m \cdot c^2$." "\n"
                r"- **c) Đúng**: Phương trình phóng xạ $\alpha$ là ${}_Z^A\text{X} \rightarrow {}_{Z-2}^{A-4}\text{Y} + {}_{2}^{4}\text{He}$." "\n"
                r"- **d) Sai**: Quá trình phóng xạ có bản chất hạt nhân, hoàn toàn không phụ thuộc vào các tác động lí – hoá bên ngoài như nhiệt độ hay áp suất.",
            ),
            tf4(
                "hieu",
                r"Xét phản ứng tổng hợp hạt nhân (nhiệt hạch): ${}_{1}^{2}\text{H} + {}_{1}^{3}\text{H} \rightarrow {}_{2}^{4}\text{He} + {}_{0}^{1}\text{n}$. Biết khối lượng của các hạt nhân là $m_{\text{D}} = 2{,}0141\text{ amu}$, $m_{\text{T}} = 3{,}0160\text{ amu}$, $m_{\text{He}} = 4{,}0026\text{ amu}$, $m_n = 1{,}0087\text{ amu}$ và lấy $1\text{ amu} = 931{,}5\text{ MeV}/c^2$. Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Hai hạt nhân ${}_{1}^{2}\text{H}$ (deuterium) và ${}_{1}^{3}\text{H}$ (tritium) là hai đồng vị của nguyên tố hydrogen.",
                    r"b) Tổng khối lượng của các hạt trước phản ứng lớn hơn tổng khối lượng của các hạt sau phản ứng một lượng $\Delta m = 0{,}0188\text{ amu}$.",
                    r"c) Phản ứng trên là phản ứng thu năng lượng với nhiệt lượng thu vào cho mỗi phản ứng là $17{,}51\text{ MeV}$.",
                    r"d) Để thực hiện phản ứng tổng hợp hạt nhân này, hỗn hợp nhiên liệu cần được nung nóng đến nhiệt độ cực cao (hàng chục triệu đến hàng trăm triệu độ Kelvin) để các hạt nhân thắng được lực đẩy tĩnh điện Coulomb.",
                ],
                [True, True, False, True],
                r"- **a) Đúng**: ${}_{1}^{2}\text{H}$ và ${}_{1}^{3}\text{H}$ có cùng $Z = 1$ proton nhưng khác số khối $A$ nên là hai đồng vị của hydrogen." "\n"
                r"- **b) Đúng**: $m_{\text{trước}} = 2{,}0141 + 3{,}0160 = 5{,}0301\text{ amu}$; $m_{\text{sau}} = 4{,}0026 + 1{,}0087 = 5{,}0113\text{ amu}$. Suy ra $\Delta m = m_{\text{trước}} - m_{\text{sau}} = 5{,}0301 - 5{,}0113 = 0{,}0188\text{ amu}$." "\n"
                r"- **c) Sai**: Vì $m_{\text{trước}} > m_{\text{sau}}$ nên phản ứng **toả** năng lượng $\Delta E = 0{,}0188 \cdot 931{,}5 \approx 17{,}51\text{ MeV}$ (không phải thu năng lượng)." "\n"
                r"- **d) Đúng**: Phản ứng tổng hợp hạt nhân đòi hỏi nhiệt độ cực cao (phản ứng nhiệt hạch) để các hạt nhân mang điện dương lại gần nhau trong phạm vi tác dụng của lực hạt nhân.",
            ),
            mcq(
                "vandung",
                r"Hạt nhân sắt ${}_{26}^{56}\text{Fe}$ có khối lượng $m_{\text{Fe}} = 55{,}9207\text{ amu}$. Cho khối lượng của proton là $m_p = 1{,}0073\text{ amu}$, của neutron là $m_n = 1{,}0087\text{ amu}$ và $1\text{ amu} = 931{,}5\text{ MeV}/c^2$. Năng lượng liên kết riêng $W_{\text{lkr}}$ của hạt nhân ${}_{26}^{56}\text{Fe}$ gần nhất với giá trị nào sau đây?",
                [
                    r"$8{,}79\text{ MeV/nucleon}$",
                    r"$7{,}45\text{ MeV/nucleon}$",
                    r"$8{,}12\text{ MeV/nucleon}$",
                    r"$9{,}42\text{ MeV/nucleon}$",
                ],
                0,
                r"Hạt nhân ${}_{26}^{56}\text{Fe}$ có $Z = 26$ proton và $N = 56 - 26 = 30$ neutron. Độ hụt khối: $\Delta m = 26 \cdot 1{,}0073 + 30 \cdot 1{,}0087 - 55{,}9207 = 26{,}1898 + 30{,}2610 - 55{,}9207 = 0{,}5301\text{ amu}$. Năng lượng liên kết: $W_{\text{lk}} = 0{,}5301 \cdot 931{,}5 \approx 493{,}79\text{ MeV}$. Năng lượng liên kết riêng: $W_{\text{lkr}} = \dfrac{493{,}79}{56} \approx \mathbf{8{,}82\text{ MeV/nucleon}}$ (gần nhất với $8{,}79\text{ MeV/nucleon}$).",
            ),
            short(
                "vandung",
                r"Ban đầu có một mẫu chất phóng xạ nguyên chất ${}_Z^A\text{X}$ có chu kì bán rã $T = 15\text{ giờ}$, phân rã tạo thành hạt nhân con bền $\text{Y}$. Sau khoảng thời gian $t$ bằng bao nhiêu giờ thì tỉ số giữa số hạt nhân con $\text{Y}$ tạo thành và số hạt nhân mẹ $\text{X}$ còn lại trong mẫu bằng $7$?",
                ["45"],
                r"Số hạt nhân con tạo thành bằng số hạt nhân mẹ đã phân rã: $N_{\text{Y}} = \Delta N = N_0\left(1 - 2^{-\frac{t}{T}}\right)$. "
                r"Theo đề bài: $\dfrac{N_{\text{Y}}}{N_{\text{X}}} = 2^{\frac{t}{T}} - 1 = 7 \Rightarrow 2^{\frac{t}{T}} = 8 = 2^3 \Rightarrow \dfrac{t}{T} = 3 \Rightarrow t = 3T = 3 \cdot 15 = \mathbf{45}\text{ giờ}$.",
                unit=r"$\text{giờ}$",
            ),
        ],
    },

    # =========================================================================
    # CHUYÊN ĐỀ VẬT LÍ 12. DÒNG ĐIỆN XOAY CHIỀU RLC, LƯỢNG TỬ ÁNH SÁNG VÀ THUYẾT TƯƠNG ĐỐI
    # =========================================================================
    {
        "topic": "quang-dien",
        "title": "Chuyên đề Vật lí 12. Dòng điện xoay chiều RLC, Lượng tử ánh sáng và Thuyết tương đối",
        "icon": "🔬",
        "description": (
            "Chuyên đề học tập Vật lí 12 · Bộ sách Kết nối tri thức với cuộc sống (Bài 1 – Bài 12): "
            "Chuyên đề 1. Đặc trưng của dòng điện xoay chiều, đoạn mạch RLC mắc nối tiếp, máy biến áp và chỉnh lưu dòng điện xoay chiều; "
            "Chuyên đề 2. Tia X, ứng dụng vật lí trong chẩn đoán y học (X-quang, CT, siêu âm, MRI), hiện tượng quang điện và năng lượng photon; "
            "Chuyên đề 3. Lưỡng tính sóng hạt, quang phổ vạch nguyên tử, vùng năng lượng chất rắn và Hệ thức Einstein."
        ),
        "requirements": [
            r"Nêu được biểu thức cảm kháng $Z_L = \omega L$, dung kháng $Z_C = \dfrac{1}{\omega C}$, tổng trở $Z = \sqrt{R^2 + (Z_L - Z_C)^2}$, định luật Ohm $I = \dfrac{U}{Z}$ và độ lệch pha $\tan\varphi = \dfrac{Z_L - Z_C}{R}$ của đoạn mạch xoay chiều $RLC$ mắc nối tiếp.",
            r"Mô tả và vận dụng được điều kiện cộng hưởng điện trong mạch $RLC$ nối tiếp ($Z_L = Z_C \Leftrightarrow \omega_0 = \dfrac{1}{\sqrt{LC}}$), công thức công suất tiêu thụ $\mathcal{P} = UI\cos\varphi = I^2 R$ và hệ số công suất $\cos\varphi = \dfrac{R}{Z}$.",
            r"Nêu được nguyên tắc hoạt động của máy biến áp ($\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$), vai trò của máy biến áp trong việc giảm hao phí điện năng $\Delta \mathcal{P} = \dfrac{\mathcal{P}^2 R}{U^2\cos^2\varphi}$ khi truyền tải đi xa và nguyên lí chỉnh lưu dòng điện xoay chiều bằng diode bán dẫn.",
            r"Trình bày được bản chất, cách tạo ra tia X (tia Röntgen), sự suy giảm cường độ tia X ($I = I_0 e^{-\mu x}$) và nguyên lí cơ bản của các kĩ thuật chẩn đoán hình ảnh y học: chụp X-quang, chụp cắt lớp vi tính (CT), siêu âm và chụp cộng hưởng từ (MRI).",
            r"Nêu được thuyết lượng tử ánh sáng, công thức năng lượng photon $\varepsilon = hf = \dfrac{hc}{\lambda}$, định nghĩa giới hạn quang điện $\lambda_0 = \dfrac{hc}{A}$ và điều kiện xảy ra hiện tượng quang điện ngoài $\lambda \le \lambda_0$.",
            r"Vận dụng được hệ thức Einstein về hiện tượng quang điện $hf = A + W_{\text{đ0max}} = A + \dfrac{1}{2}mv_{0\max}^2 = A + eU_{\text{h}}$ để giải các bài toán thực nghiệm.",
            r"Nêu được lưỡng tính sóng – hạt của ánh sáng và hạt vi mô (bước sóng de Broglie $\lambda = \dfrac{h}{p} = \dfrac{h}{mv}$), giải thích được sự tạo thành quang phổ vạch của nguyên tử hydrogen theo tiên đề Bohr ($E_n - E_m = hf_{nm}$) và sơ lược vùng năng lượng của tinh thể chất rắn (vùng hoá trị, vùng cấm, vùng dẫn).",
            r"Vận dụng được hệ thức năng lượng – khối lượng của thuyết tương đối hẹp Einstein $E = mc^2$, năng lượng nghỉ $E_0 = m_0 c^2$ và động năng tương đối tính $W_{\text{đ}} = E - E_0 = (m - m_0)c^2$.",
        ],
        "definition": (
            r"- **Đoạn mạch điện xoay chiều $RLC$ mắc nối tiếp và Máy biến áp (Chuyên đề 1)**: Đặt điện áp $u = U\sqrt{2}\cos(\omega t + \varphi_u)$ vào hai đầu đoạn mạch gồm điện trở $R$, cuộn cảm thuần $L$ (cảm kháng $Z_L = \omega L$) và tụ điện $C$ (dung kháng $Z_C = \dfrac{1}{\omega C}$) mắc nối tiếp thì dòng điện trong mạch có cường độ hiệu dụng $I = \dfrac{U}{Z}$ với tổng trở $Z = \sqrt{R^2 + (Z_L - Z_C)^2}$, độ lệch pha $\varphi = \varphi_u - \varphi_i$ xác định bởi $\tan\varphi = \dfrac{Z_L - Z_C}{R}$. Khi $Z_L = Z_C$ ($\omega_0 = \dfrac{1}{\sqrt{LC}}$) xảy ra **cộng hưởng điện**: $Z_{\min} = R$, $I_{\max} = \dfrac{U}{R}$, $\varphi = 0$, $\mathcal{P}_{\max} = \dfrac{U^2}{R}$. Máy biến áp lí tưởng: $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2} = \dfrac{I_2}{I_1}$." "\n"
            r"- **Tia X, Hiện tượng quang điện và Năng lượng photon $\varepsilon = hf$ (Chuyên đề 2 và Chuyên đề 3)**: Chùm ánh sáng (và mọi bức xạ điện từ như tia X, tia $\gamma$) là chùm các hạt lượng tử gọi là **photon**; mỗi photon của bức xạ đơn sắc tần số $f$ (bước sóng $\lambda$ trong chân không) mang năng lượng xác định $\varepsilon = hf = \dfrac{hc}{\lambda}$ (với hằng số Planck $h = 6{,}626 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 3 \times 10^8\text{ m/s}$). Trong hiện tượng quang điện ngoài, khi chiếu bức xạ có $\lambda \le \lambda_0 = \dfrac{hc}{A}$ vào kim loại có công thoát $A$, electron hấp thụ trọn vẹn một photon theo **hệ thức Einstein**: $hf = A + W_{\text{đ0max}} = A + \dfrac{1}{2}mv_{0\max}^2 = A + eU_{\text{h}}$." "\n"
            r"- **Lưỡng tính sóng – hạt, Quang phổ nguyên tử và Hệ thức Einstein $E = mc^2$ (Chuyên đề 3)**: Mọi vi hạt có động lượng $p = mv$ đều gắn liền với một sóng de Broglie có bước sóng $\lambda = \dfrac{h}{p} = \dfrac{h}{mv}$. Nguyên tử chỉ bức xạ hay hấp thụ photon khi chuyển giữa hai trạng thái dừng có năng lượng $E_n$ và $E_m$: $\varepsilon = hf_{nm} = |E_n - E_m|$. Theo thuyết tương đối hẹp Einstein, một vật có khối lượng nghỉ $m_0$ chuyển động với tốc độ $v$ có khối lượng tương đối tính $m = \dfrac{m_0}{\sqrt{1 - \frac{v^2}{c^2}}}$ và năng lượng toàn phần $E = mc^2 = E_0 + W_{\text{đ}}$."
        ),
        "theory": (
            r"### Chuyên đề 1. Đặc trưng của dòng điện xoay chiều, Mạch RLC nối tiếp và Máy biến áp (Bài 1 – Bài 4 Chuyên đề Vật lí 12 KNTT)" "\n"
            r"- **Bài 1 và Bài 2. Đoạn mạch xoay chiều $RLC$ mắc nối tiếp**: Trên $R$, $u_R$ cùng pha với $i$; trên cuộn cảm thuần $L$, $u_L$ sớm pha $\dfrac{\pi}{2}$ so với $i$; trên tụ điện $C$, $u_C$ trễ pha $\dfrac{\pi}{2}$ so với $i$. Điện áp hiệu dụng: $U = \sqrt{U_R^2 + (U_L - U_C)^2}$. Công suất tiêu thụ của mạch: $\mathcal{P} = UI\cos\varphi = I^2 R$, với hệ số công suất $\cos\varphi = \dfrac{R}{Z} = \dfrac{U_R}{U}$." "\n"
            r"- **Bài 3. Máy biến áp và Truyền tải điện năng**: Máy biến áp hoạt động dựa trên hiện tượng cảm ứng điện từ, dùng để đổi điện áp xoay chiều mà không làm thay đổi tần số: $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$ ($N_2 > N_1$ là máy tăng áp, $N_2 < N_1$ là máy hạ áp). Khi truyền tải công suất $\mathcal{P}$ đi xa trên đường dây có điện trở $R$, công suất hao phí do toả nhiệt là $\Delta \mathcal{P} = \dfrac{\mathcal{P}^2 R}{U^2\cos^2\varphi}$; tăng điện áp truyền tải $U$ lên $k$ lần giúp giảm công suất hao phí $k^2$ lần." "\n"
            r"- **Bài 4. Chỉnh lưu dòng điện xoay chiều**: Sử dụng tính dẫn điện một chiều của diode bán dẫn để biến đổi dòng điện xoay chiều thành dòng điện một chiều thông qua mạch chỉnh lưu nửa chu kì (dùng $1$ diode) hoặc mạch chỉnh lưu cả chu kì (dùng cầu chỉnh lưu $4$ diode kết hợp tụ lọc)." "\n"
            r"### Chuyên đề 2. Tia X, Hiện tượng quang điện và Năng lượng photon $\varepsilon = hf$ (Bài 5 – Bài 12 Chuyên đề Vật lí 12 KNTT)" "\n"
            r"- **Bài 5 – Bài 8. Tia X và Chẩn đoán hình ảnh y học**: Tia X là sóng điện từ có bước sóng từ $10^{-11}\text{ m}$ đến $10^{-8}\text{ m}$, được tạo ra khi chùm electron có động năng lớn ($eU_{\text{AK}}$) đập vào đối katốt (anode) bằng kim loại có nguyên tử lượng lớn và nhiệt độ nóng chảy cao (như tungsten hay vonfram). Bước sóng ngắn nhất của tia X phát ra xác định bởi $hf_{\max} = \dfrac{hc}{\lambda_{\min}} = eU_{\text{AK}}$. Trong y học, chụp X-quang và chụp cắt lớp CT dựa trên sự hấp thụ tia X khác nhau của xương và mô mềm; siêu âm dùng sóng cơ tần số $f > 20\text{ kHz}$; chụp cộng hưởng từ (MRI) dựa trên hiện tượng cộng hưởng từ hạt nhân hydrogen (${}_{1}^{1}\text{H}$) trong cơ thể mà không dùng bức xạ ion hoá." "\n"
            r"- **Bài 9. Hiệu ứng quang điện và Năng lượng của photon**: Hiện tượng ánh sáng làm bật các electron ra khỏi bề mặt kim loại gọi là hiện tượng quang điện ngoài. Điều kiện xảy ra là bước sóng ánh sáng kích thích phải nhỏ hơn hoặc bằng giới hạn quang điện của kim loại: $\lambda \le \lambda_0 = \dfrac{hc}{A}$ (với $1\text{ eV} = 1{,}6 \times 10^{-19}\text{ J}$). Động năng ban đầu cực đại của quang electron liên hệ với hiệu điện thế hãm $U_{\text{h}}$ theo công thức $W_{\text{đ0max}} = \dfrac{1}{2}mv_{0\max}^2 = eU_{\text{h}} = hf - A$." "\n"
            r"- **Bài 10 – Bài 12. Lưỡng tính sóng hạt, Quang phổ vạch và Vùng năng lượng chất rắn**: Bước sóng de Broglie của vi hạt $\lambda = \dfrac{h}{mv}$. Trong nguyên tử hydrogen, các mức năng lượng dừng $E_n = -\dfrac{13{,}6}{n^2}\text{ (eV)}$ ($n \in \mathbb{N}^*$); khi electron chuyển từ mức $E_n$ về mức $E_m$ thấp hơn thì phát ra vạch quang phổ có bước sóng $\dfrac{hc}{\lambda_{nm}} = E_n - E_m$. Trong tinh thể chất rắn, dựa vào độ rộng vùng cấm $E_g$ giữa vùng hoá trị và vùng dẫn, ta phân biệt được chất dẫn điện (vùng dẫn và vùng hoá trị chồng lấn), chất bán dẫn ($E_g$ nhỏ, cỡ $0{,}1\text{ eV} - 4\text{ eV}$) và chất điện môi ($E_g > 4\text{ eV}$)." "\n"
            r"### Chuyên đề 3. Hệ thức Einstein $E = mc^2$ và Vật lí hiện đại" "\n"
            r"- **Hai tiên đề của Thuyết tương đối hẹp Einstein**: (1) **Tiên đề về nguyên lí tương đối**: Mọi định luật vật lí đều có cùng một dạng như nhau trong mọi hệ quy chiếu quán tính; (2) **Tiên đề về sự bất biến của tốc độ ánh sáng**: Tốc độ ánh sáng trong chân không luôn có cùng độ lớn $c \approx 3 \times 10^8\text{ m/s}$ trong mọi hệ quy chiếu quán tính, không phụ thuộc vào phương truyền hay tốc độ của nguồn sáng và máy thu." "\n"
            r"- **Hệ thức năng lượng – khối lượng Einstein**: Một vật có khối lượng nghỉ $m_0$ khi đứng yên có năng lượng nghỉ $E_0 = m_0 c^2$; khi chuyển động với tốc độ $v$, năng lượng toàn phần của vật là $E = mc^2 = \dfrac{m_0 c^2}{\sqrt{1 - \frac{v^2}{c^2}}}$, và động năng tương đối tính của vật là $W_{\text{đ}} = E - E_0 = (m - m_0)c^2$."
        ),
        "formulas": [
            G(
                "I. Mạch điện xoay chiều RLC nối tiếp và Máy biến áp (Chuyên đề 1)",
                F("Cảm kháng, Dung kháng và Tổng trở", r"$Z_L = \omega L; \quad Z_C = \dfrac{1}{\omega C}; \quad Z = \sqrt{R^2 + (Z_L - Z_C)^2}$", r"Định luật Ohm: $I = \dfrac{U}{Z} = \dfrac{U_R}{R} = \dfrac{U_L}{Z_L} = \dfrac{U_C}{Z_C}$."),
                F("Độ lệch pha, Công suất và Hệ số công suất", r"$\tan\varphi = \dfrac{Z_L - Z_C}{R}; \quad \cos\varphi = \dfrac{R}{Z}; \quad \mathcal{P} = UI\cos\varphi = I^2 R$", r"Cộng hưởng điện khi $Z_L = Z_C \Leftrightarrow \omega_0 = \dfrac{1}{\sqrt{LC}}$."),
                F("Máy biến áp lí tưởng và Hao phí truyền tải", r"$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2} = \dfrac{I_2}{I_1}; \quad \Delta \mathcal{P} = \dfrac{\mathcal{P}^2 R}{U^2\cos^2\varphi}$", r"Tăng điện áp $U$ lên $k$ lần thì công suất hao phí $\Delta \mathcal{P}$ giảm $k^2$ lần."),
            ),
            G(
                "II. Tia X, Lượng tử ánh sáng và Hiện tượng quang điện (Chuyên đề 2)",
                F("Năng lượng photon và Giới hạn quang điện", r"$\varepsilon = hf = \dfrac{hc}{\lambda}; \quad \lambda_0 = \dfrac{hc}{A}$", r"$h = 6{,}626 \times 10^{-34}\text{ J}\cdot\text{s}$; $1\text{ eV} = 1{,}6 \times 10^{-19}\text{ J}$."),
                F("Hệ thức Einstein về hiện tượng quang điện", r"$hf = A + W_{\text{đ0max}} = A + \dfrac{1}{2}mv_{0\max}^2 = A + eU_{\text{h}}$", r"Điều kiện xảy ra quang điện ngoài: $\lambda \le \lambda_0$ (hay $f \ge f_0$)."),
                F("Bước sóng ngắn nhất của Tia X", r"$hf_{\max} = \dfrac{hc}{\lambda_{\min}} = eU_{\text{AK}} \Rightarrow \lambda_{\min} = \dfrac{hc}{eU_{\text{AK}}}$", r"$U_{\text{AK}}$ là hiệu điện thế tăng tốc giữa anode và cathode."),
            ),
            G(
                "III. Lưỡng tính sóng hạt, Tiên đề Bohr và Hệ thức Einstein (Chuyên đề 3)",
                F("Bước sóng de Broglie và Tiên đề Bohr", r"$\lambda_{\text{dB}} = \dfrac{h}{p} = \dfrac{h}{mv}; \quad hf_{nm} = \dfrac{hc}{\lambda_{nm}} = E_n - E_m$", r"Với nguyên tử hydrogen: $E_n = -\dfrac{13{,}6}{n^2}\text{ (eV)}$."),
                F("Hệ thức năng lượng – khối lượng Einstein", r"$E = mc^2 = \dfrac{m_0 c^2}{\sqrt{1 - \frac{v^2}{c^2}}}; \quad W_{\text{đ}} = E - E_0 = (m - m_0)c^2$", r"Năng lượng nghỉ: $E_0 = m_0 c^2$."),
            ),
        ],
        "example": (
            r"Công thoát của electron khỏi bề mặt kim loại sodium ($\text{Na}$) là $A = 2{,}48\text{ eV}$. "
            r"Lấy $h = 6{,}625 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 3 \times 10^8\text{ m/s}$, $e = 1{,}6 \times 10^{-19}\text{ C}$ và $1\text{ eV} = 1{,}6 \times 10^{-19}\text{ J}$. "
            r"a) Tính giới hạn quang điện $\lambda_0$ của sodium theo đơn vị $\mu\text{m}$. "
            r"b) Khi chiếu vào tấm sodium chùm bức xạ tử ngoại có bước sóng $\lambda = 0{,}30\text{ }\mu\text{m}$, hãy tính năng lượng photon $\varepsilon$ (theo $\text{eV}$), động năng ban đầu cực đại $W_{\text{đ0max}}$ của quang electron và hiệu điện thế hãm $U_{\text{h}}$."
        ),
        "example_answer": (
            r"- **Câu a**: Đổi công thoát $A = 2{,}48 \cdot 1{,}6 \times 10^{-19} = 3{,}968 \times 10^{-19}\text{ J}$." "\n"
            r"  Giới hạn quang điện của sodium: $\lambda_0 = \dfrac{hc}{A} = \dfrac{6{,}625 \times 10^{-34} \cdot 3 \times 10^8}{3{,}968 \times 10^{-19}} \approx 5{,}01 \times 10^{-7}\text{ m} = \mathbf{0{,}501\text{ }\mu\text{m}}$." "\n"
            r"- **Câu b**: Với $\lambda = 0{,}30\text{ }\mu\text{m} = 3 \times 10^{-7}\text{ m} < \lambda_0$, hiện tượng quang điện xảy ra." "\n"
            r"  Năng lượng của mỗi photon kích thích: $\varepsilon = \dfrac{hc}{\lambda} = \dfrac{6{,}625 \times 10^{-34} \cdot 3 \times 10^8}{3 \times 10^{-7}} = 6{,}625 \times 10^{-19}\text{ J} \approx \mathbf{4{,}14\text{ eV}}$." "\n"
            r"  Theo hệ thức Einstein: $W_{\text{đ0max}} = \varepsilon - A = 4{,}14 - 2{,}48 = \mathbf{1{,}66\text{ eV}} \approx \mathbf{2{,}66 \times 10^{-19}\text{ J}}$." "\n"
            r"  Hiệu điện thế hãm cần thiết để triệt tiêu dòng quang điện: $U_{\text{h}} = \dfrac{W_{\text{đ0max}}}{e} = \mathbf{1{,}66\text{ V}}$."
        ),
        "real_life": (
            r"- **Tế bào quang điện (Pin mặt trời), cảm biến ánh sáng tự động và cáp quang**: Chuyển đổi trực tiếp quang năng của các photon thành điện năng dựa trên hiện tượng quang điện." "\n"
            r"- **Trạm biến áp cao thế $500\text{ kV}$ Bắc – Nam và bộ sạc điện thoại (Adapter)**: Sử dụng máy biến áp nâng điện áp để giảm hao phí truyền tải và dùng mạch cầu diode chỉnh lưu dòng điện xoay chiều $220\text{ V}$ thành dòng điện một chiều sạc pin." "\n"
            r"- **Chẩn đoán y khoa hiện đại (X-quang kỹ thuật số, CT Scanner, MRI) và hiệu chỉnh đồng hồ vệ tinh GPS**: Vận dụng tia X, cộng hưởng từ hạt nhân và thuyết tương đối Einstein trong y học và định vị toàn cầu chính xác tới từng nanô-giây."
        ),
        "game_title": "Phòng thí nghiệm Mạch RLC, Quang điện Tế bào và Vật lí Lượng tử",
        "game_description": "Khảo sát hiện tượng cộng hưởng điện trong mạch RLC nối tiếp, chiếu bức xạ đơn sắc vào tế bào quang điện để đo hiệu điện thế hãm và mô phỏng dịch chuyển mức năng lượng nguyên tử Bohr.",
        "game_type": "game_quang_dien",
        "quiz": [
            mcq(
                "biet",
                r"Gọi $h$ là hằng số Planck, $c$ là tốc độ ánh sáng trong chân không. Một bức xạ đơn sắc có tần số $f$ và bước sóng $\lambda$ trong chân không thì mỗi photon của bức xạ đó mang năng lượng $\varepsilon$ bằng:",
                [
                    r"$\varepsilon = hf = \dfrac{hc}{\lambda}$",
                    r"$\varepsilon = \dfrac{h}{f} = h\lambda$",
                    r"$\varepsilon = \dfrac{hf}{c} = \dfrac{h}{\lambda}$",
                    r"$\varepsilon = hc\lambda$",
                ],
                0,
                r"Theo thuyết lượng tử ánh sáng, năng lượng của một photon là $\varepsilon = hf = \dfrac{hc}{\lambda}$.",
            ),
            mcq(
                "biet",
                r"Đặt điện áp xoay chiều có tần số góc $\omega$ vào hai đầu đoạn mạch gồm điện trở thuần $R$, cuộn cảm thuần có độ tự cảm $L$ và tụ điện có điện dung $C$ mắc nối tiếp. Tổng trở $Z$ của đoạn mạch được tính bằng công thức nào?",
                [
                    r"$Z = \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}$",
                    r"$Z = \sqrt{R^2 + \left(\omega L + \dfrac{1}{\omega C}\right)^2}$",
                    r"$Z = R + \omega L - \dfrac{1}{\omega C}$",
                    r"$Z = \sqrt{R^2 + \left(\omega C - \dfrac{1}{\omega L}\right)^2}$",
                ],
                0,
                r"Với cảm kháng $Z_L = \omega L$ và dung kháng $Z_C = \dfrac{1}{\omega C}$, tổng trở của đoạn mạch $RLC$ mắc nối tiếp là $Z = \sqrt{R^2 + (Z_L - Z_C)^2} = \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}$.",
            ),
            mcq(
                "biet",
                r"Theo thuyết tương đối của Einstein, một vật có khối lượng $m$ thì có năng lượng toàn phần $E$ liên hệ với tốc độ ánh sáng trong chân không $c$ theo hệ thức nào?",
                [
                    r"$E = mc^2$",
                    r"$E = \dfrac{1}{2}mc^2$",
                    r"$E = mc$",
                    r"$E = \dfrac{m}{c^2}$",
                ],
                0,
                r"Hệ thức liên hệ giữa năng lượng toàn phần và khối lượng theo thuyết tương đối Einstein là $E = mc^2$.",
            ),
            mcq(
                "biet",
                r"Một máy biến áp lí tưởng có số vòng dây của cuộn sơ cấp là $N_1$, số vòng dây của cuộn thứ cấp là $N_2$. Khi đặt vào hai đầu cuộn sơ cấp điện áp xoay chiều hiệu dụng $U_1$ thì điện áp hiệu dụng $U_2$ ở hai đầu cuộn thứ cấp để hở thoả mãn hệ thức:",
                [
                    r"$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$",
                    r"$\dfrac{U_1}{U_2} = \dfrac{N_2}{N_1}$",
                    r"$\dfrac{U_1}{U_2} = \left(\dfrac{N_1}{N_2}\right)^2$",
                    r"$\dfrac{U_1}{U_2} = \sqrt{\dfrac{N_1}{N_2}}$",
                ],
                0,
                r"Trong máy biến áp lí tưởng, tỉ số điện áp hiệu dụng ở hai cuộn dây bằng tỉ số vòng dây tương ứng: $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$.",
            ),
            mcq(
                "hieu",
                r"Đặt điện áp xoay chiều $u = 100\sqrt{2}\cos(100\pi t)\text{ (V)}$ vào hai đầu đoạn mạch $RLC$ mắc nối tiếp có điện trở $R = 40\text{ }\Omega$, cảm kháng $Z_L = 70\text{ }\Omega$ và dung kháng $Z_C = 40\text{ }\Omega$. Cường độ dòng điện hiệu dụng $I$ và hệ số công suất $\cos\varphi$ của đoạn mạch lần lượt là:",
                [
                    r"$I = 2{,}0\text{ A}$ và $\cos\varphi = 0{,}8$",
                    r"$I = 2{,}5\text{ A}$ và $\cos\varphi = 1{,}0$",
                    r"$I = 2\sqrt{2}\text{ A}$ và $\cos\varphi = 0{,}6$",
                    r"$I = 1{,}0\text{ A}$ và $\cos\varphi = 0{,}8$",
                ],
                0,
                r"Tổng trở của mạch: $Z = \sqrt{R^2 + (Z_L - Z_C)^2} = \sqrt{40^2 + (70 - 40)^2} = 50\text{ }\Omega$. Điện áp hiệu dụng $U = 100\text{ V} \Rightarrow I = \dfrac{U}{Z} = \dfrac{100}{50} = \mathbf{2{,}0\text{ A}}$ và $\cos\varphi = \dfrac{R}{Z} = \dfrac{40}{50} = \mathbf{0{,}8}$.",
            ),
            mcq(
                "hieu",
                r"Một kim loại có giới hạn quang điện là $\lambda_0 = 0{,}36\text{ }\mu\text{m}$. Khi chiếu lần lượt bốn bức xạ đơn sắc có bước sóng $\lambda_1 = 0{,}65\text{ }\mu\text{m}$, $\lambda_2 = 0{,}50\text{ }\mu\text{m}$, $\lambda_3 = 0{,}42\text{ }\mu\text{m}$ và $\lambda_4 = 0{,}28\text{ }\mu\text{m}$ vào bề mặt kim loại này thì bức xạ nào gây ra được hiện tượng quang điện ngoài?",
                [
                    r"Chỉ bức xạ $\lambda_4 = 0{,}28\text{ }\mu\text{m}$",
                    r"Cả ba bức xạ $\lambda_1, \lambda_2$ và $\lambda_3$",
                    r"Hai bức xạ $\lambda_3 = 0{,}42\text{ }\mu\text{m}$ và $\lambda_4 = 0{,}28\text{ }\mu\text{m}$",
                    r"Cả bốn bức xạ $\lambda_1, \lambda_2, \lambda_3$ và $\lambda_4$",
                ],
                0,
                r"Điều kiện xảy ra hiện tượng quang điện ngoài là $\lambda \le \lambda_0 = 0{,}36\text{ }\mu\text{m}$. Trong bốn bức xạ đã cho, chỉ có $\lambda_4 = 0{,}28\text{ }\mu\text{m} \le 0{,}36\text{ }\mu\text{m}$ thoả mãn.",
            ),
            tf4(
                "hieu",
                r"Đặt điện áp xoay chiều có giá trị hiệu dụng $U = 120\text{ V}$ và tần số góc $\omega$ thay đổi được vào hai đầu đoạn mạch $RLC$ mắc nối tiếp có $R = 60\text{ }\Omega$. Khi điều chỉnh $\omega = \omega_0 = \dfrac{1}{\sqrt{LC}}$ thì trong mạch xảy ra hiện tượng cộng hưởng điện. Xét tính đúng hay sai của các khẳng định sau:",
                [
                    r"a) Khi xảy ra cộng hưởng điện, cảm kháng $Z_L$ bằng dung kháng $Z_C$ và tổng trở của đoạn mạch đạt giá trị nhỏ nhất $Z_{\min} = R = 60\text{ }\Omega$.",
                    r"b) Khi xảy ra cộng hưởng điện, cường độ dòng điện trong mạch cùng pha với điện áp hai đầu đoạn mạch ($\varphi = 0$) và hệ số công suất đạt cực đại $\cos\varphi = 1$.",
                    r"c) Cường độ dòng điện hiệu dụng cực đại trong mạch khi cộng hưởng là $I_{\max} = 2\text{ A}$ và công suất tiêu thụ cực đại là $\mathcal{P}_{\max} = 240\text{ W}$.",
                    r"d) Khi xảy ra cộng hưởng điện, điện áp hiệu dụng giữa hai đầu cuộn cảm $U_L$ và điện áp hiệu dụng giữa hai đầu tụ điện $U_C$ đều bằng $0\text{ V}$.",
                ],
                [True, True, True, False],
                r"- **a) Đúng**: Khi $\omega = \omega_0 = \dfrac{1}{\sqrt{LC}}$ thì $Z_L = Z_C \Rightarrow Z_{\min} = R = 60\text{ }\Omega$." "\n"
                r"- **b) Đúng**: Khi $Z_L = Z_C$ thì $\tan\varphi = 0 \Rightarrow \varphi = 0$ ($i$ cùng pha với $u$) và $\cos\varphi = 1$." "\n"
                r"- **c) Đúng**: $I_{\max} = \dfrac{U}{R} = \dfrac{120}{60} = 2\text{ A}$ và $\mathcal{P}_{\max} = I_{\max}^2 R = 2^2 \cdot 60 = 240\text{ W}$." "\n"
                r"- **d) Sai**: Khi cộng hưởng thì $U_L = I_{\max} Z_L = U_C = I_{\max} Z_C \neq 0$ (hai điện áp tức thời $u_L$ và $u_C$ ngược pha triệt tiêu nhau nên $U_{LC} = |U_L - U_C| = 0$, nhưng bản thân $U_L$ và $U_C$ đều khác $0$).",
            ),
            tf4(
                "hieu",
                r"Xét tính đúng hay sai của các phát biểu sau về tia X, lưỡng tính sóng – hạt, quang phổ nguyên tử và hệ thức Einstein:",
                [
                    r"a) Tia X có khả năng đâm xuyên mạnh qua các mô mềm nhưng bị xương hấp thụ mạnh hơn, nhờ đó được ứng dụng để chụp X-quang và chụp cắt lớp vi tính (CT) trong chẩn đoán y học.",
                    r"b) Khi tăng cường độ chùm sáng kích thích (giữ nguyên bước sóng $\lambda \le \lambda_0$) chiếu vào kim loại thì động năng ban đầu cực đại $W_{\text{đ0max}}$ của các quang electron bật ra cũng tăng tỉ lệ thuận.",
                    r"c) Theo tiên đề Bohr, khi electron trong nguyên tử hydrogen chuyển từ quỹ đạo dừng có năng lượng $E_3 = -1{,}51\text{ eV}$ về quỹ đạo dừng có năng lượng $E_2 = -3{,}40\text{ eV}$ thì nguyên tử phát ra một photon có năng lượng $\varepsilon = 1{,}89\text{ eV}$.",
                    r"d) Một hạt có khối lượng nghỉ $m_0$ chuyển động với tốc độ $v = 0{,}6c$ thì có khối lượng tương đối tính $m = 1{,}25m_0$ và động năng tương đối tính $W_{\text{đ}} = 0{,}25m_0 c^2$.",
                ],
                [True, False, True, True],
                r"- **a) Đúng**: Sự suy giảm tia X phụ thuộc mạnh vào khối lượng riêng và nguyên tử số của vật chất nên tạo độ tương phản rõ nét giữa xương và mô mềm." "\n"
                r"- **b) Sai**: Theo hệ thức Einstein $W_{\text{đ0max}} = \dfrac{hc}{\lambda} - A$, động năng ban đầu cực đại chỉ phụ thuộc vào bước sóng $\lambda$ (tần số $f$) của ánh sáng kích thích và bản chất kim loại ($A$), hoàn toàn không phụ thuộc vào cường độ chùm sáng." "\n"
                r"- **c) Đúng**: $\varepsilon = E_3 - E_2 = -1{,}51 - (-3{,}40) = 1{,}89\text{ eV}$." "\n"
                r"- **d) Đúng**: Khi $v = 0{,}6c$ thì $\sqrt{1 - \dfrac{v^2}{c^2}} = \sqrt{1 - 0{,}36} = 0{,}8 \Rightarrow m = \dfrac{m_0}{0{,}8} = 1{,}25m_0$ và $W_{\text{đ}} = (m - m_0)c^2 = 0{,}25m_0 c^2$.",
            ),
            mcq(
                "vandung",
                r"Trong một ống phát tia X, hiệu điện thế tăng tốc giữa anode và cathode là $U_{\text{AK}} = 25\text{ kV}$. Bỏ qua động năng ban đầu của electron khi bứt ra khỏi cathode. Cho $h = 6{,}625 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 3 \times 10^8\text{ m/s}$ và $e = 1{,}6 \times 10^{-19}\text{ C}$. Bước sóng ngắn nhất $\lambda_{\min}$ của tia X mà ống có thể phát ra là:",
                [
                    r"$4{,}97 \times 10^{-11}\text{ m}$",
                    r"$2{,}48 \times 10^{-11}\text{ m}$",
                    r"$4{,}97 \times 10^{-10}\text{ m}$",
                    r"$1{,}99 \times 10^{-11}\text{ m}$",
                ],
                0,
                r"Đổi $U_{\text{AK}} = 25\text{ kV} = 2{,}5 \times 10^4\text{ V}$. Khi toàn bộ động năng của electron chuyển hoá thành năng lượng của photon tia X: $\dfrac{hc}{\lambda_{\min}} = eU_{\text{AK}} \Rightarrow \lambda_{\min} = \dfrac{hc}{eU_{\text{AK}}} = \dfrac{6{,}625 \times 10^{-34} \cdot 3 \times 10^8}{1{,}6 \times 10^{-19} \cdot 2{,}5 \times 10^4} = \dfrac{1{,}9875 \times 10^{-25}}{4 \times 10^{-15}} \approx \mathbf{4{,}97 \times 10^{-11}\text{ m}}$.",
            ),
            short(
                "vandung",
                r"Khi chiếu một bức xạ đơn sắc có năng lượng mỗi photon là $\varepsilon = 4{,}5\text{ eV}$ vào bề mặt một tấm kim loại có công thoát $A = 2{,}1\text{ eV}$ thì động năng ban đầu cực đại $W_{\text{đ0max}}$ của các quang electron bật ra khỏi kim loại bằng bao nhiêu electron-volt ($\text{eV}$)? (Viết kết quả dưới dạng số thập phân với dấu phẩy hoặc dấu chấm).",
                ["2,4", "2.4"],
                r"Áp dụng hệ thức Einstein về hiện tượng quang điện: $W_{\text{đ0max}} = \varepsilon - A = 4{,}5 - 2{,}1 = \mathbf{2{,}4}\text{ eV}$.",
                unit=r"$\text{eV}$",
            ),
        ],
    },
]
