"""Vật lý Lớp 8 (KHTN 8 - Kết nối tri thức với cuộc sống): 4 Chương - 14 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 8

CH1_TOPIC = "l8-ch01-khoi-luong-rieng-ap-suat"
CH1_TITLE = "Chương I: Khối lượng riêng và Áp suất"
CH1_DESC = "Chương I · Vật lý 8 (KHTN 8): Khối lượng riêng, thực hành đo khối lượng riêng, lực đẩy Archimedes và áp suất."

CH2_TOPIC = "l8-ch02-tac-dung-lam-quay"
CH2_TITLE = "Chương II: Tác dụng làm quay của lực"
CH2_DESC = "Chương II · Vật lý 8 (KHTN 8): Tác dụng làm quay của lực, moment lực, đòn bẩy và ứng dụng thực tiễn."

CH3_TOPIC = "l8-ch03-dien-hoc"
CH3_TITLE = "Chương III: Điện"
CH3_DESC = "Chương III · Vật lý 8 (KHTN 8): Sự nhiễm điện do cọ xát, dòng điện – nguồn điện, mạch điện và đo cường độ dòng điện, hiệu điện thế."

CH4_TOPIC = "l8-ch04-nhiet-hoc"
CH4_TITLE = "Chương IV: Nhiệt"
CH4_DESC = "Chương IV · Vật lý 8 (KHTN 8): Năng lượng nhiệt và nội năng, sự truyền nhiệt và sự nở vì nhiệt của các chất."

LESSONS = [
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 1: Khối lượng riêng",
        icon="🧊",
        description="Khái niệm khối lượng riêng, trọng lượng riêng, công thức D = m/V và quy đổi đơn vị kg/m³ sang g/cm³.",
        requirements=[
            "Nêu được định nghĩa khối lượng riêng của một chất là khối lượng của một đơn vị thể tích chất đó: $D = \\dfrac{m}{V}$.",
            "Quy đổi được đơn vị đo khối lượng riêng giữa $\\text{kg/m}^3$ và $\\text{g/cm}^3$ ($1\\text{ g/cm}^3 = 1000\\text{ kg/m}^3$).",
            "Vận dụng được công thức $D = \\dfrac{m}{V}$ và công thức trọng lượng riêng $d = \\dfrac{P}{V} = 10D$ để giải bài tập.",
        ],
        definition="Khối lượng riêng của một chất cho biết khối lượng của một đơn vị thể tích chất đó, được xác định bằng thương số giữa khối lượng $m$ và thể tích $V$ của vật: $D = \\dfrac{m}{V}$.",
        theory=(
            "### 1. Khối lượng riêng và đơn vị đo\n"
            "- Công thức: $D = \\dfrac{m}{V} \\implies m = D \\cdot V; \\quad V = \\dfrac{m}{D}$.\n"
            "- Đơn vị hợp pháp trong hệ SI là **kilôgam trên mét khối** ($\\text{kg/m}^3$). Ngoài ra còn dùng $\\text{g/cm}^3$ hoặc $\\text{g/mL}$:\n"
            "  $$1\\text{ g/cm}^3 = 1\\text{ g/mL} = 1000\\text{ kg/m}^3$$\n\n"
            "### 2. Trọng lượng riêng\n"
            "- Trọng lượng của một mét khối một chất gọi là **trọng lượng riêng** $d$ của chất đó: $d = \\dfrac{P}{V}$ (đơn vị $\\text{N/m}^3$).\n"
            "- Vì $P = 10m$ nên ta luôn có mối liên hệ: $d = 10D$ (với $D$ tính bằng $\\text{kg/m}^3$)."
        ),
        formulas=[
            G(
                "Khối lượng riêng và Trọng lượng riêng",
                F("Công thức tính khối lượng riêng", "$D = \\dfrac{m}{V} \\implies m = D \\cdot V; \\quad V = \\dfrac{m}{D}$", "Quy đổi: $1\\text{ g/cm}^3 = 1000\\text{ kg/m}^3$; $1\\text{ L} = 1\\text{ dm}^3 = 10^{-3}\\text{ m}^3$."),
                F("Công thức tính trọng lượng riêng", "$d = \\dfrac{P}{V} = 10D$", "Trong đó $d$ có đơn vị $\\text{N/m}^3$, $D$ có đơn vị $\\text{kg/m}^3$."),
            )
        ],
        example="Một khối nhôm đặc có thể tích $V = 200\\text{ cm}^3$ và khối lượng $m = 540\\text{ g}$. Hãy tính khối lượng riêng của nhôm theo đơn vị $\\text{g/cm}^3$ và $\\text{kg/m}^3$.",
        example_answer="Khối lượng riêng của nhôm là $D = \\dfrac{m}{V} = \\dfrac{540}{200} = 2{,}7\\text{ g/cm}^3$. Đổi ra $\\text{kg/m}^3$: $D = 2{,}7 \\cdot 1000 = 2700\\text{ kg/m}^3$.",
        real_life="Biết khối lượng riêng của vàng nguyên chất là $19{,}3\\text{ g/cm}^3$, thợ kim hoàn có thể kiểm tra một món đồ trang sức có phải vàng đặc nguyên chất hay đã pha tạp kim loại nhẹ hơn.",
        quiz=[
            mcq("biet", "Công thức tính khối lượng riêng $D$ của một vật có khối lượng $m$ và thể tích $V$ là gì?", ["$D = \\dfrac{m}{V}$", "$D = m \\cdot V$", "$D = \\dfrac{V}{m}$", "$D = m + V$"], 0, "Khối lượng riêng bằng khối lượng chia cho thể tích: $D = \\dfrac{m}{V}$."),
            mcq("biet", "Đổi đơn vị: $1\\text{ g/cm}^3$ bằng bao nhiêu $\\text{kg/m}^3$?", ["$1000\\text{ kg/m}^3$", "$100\\text{ kg/m}^3$", "$10\\text{ kg/m}^3$", "$0{,}001\\text{ kg/m}^3$"], 0, "Ta có $1\\text{ g/cm}^3 = \\dfrac{10^{-3}\\text{ kg}}{10^{-6}\\text{ m}^3} = 1000\\text{ kg/m}^3$."),
            mcq("hieu", "Biết khối lượng riêng của sắt là $D = 7800\\text{ kg/m}^3$. Trọng lượng riêng $d$ của sắt là bao nhiêu?", ["$78\\,000\\text{ N/m}^3$", "$780\\text{ N/m}^3$", "$7800\\text{ N/m}^3$", "$7{,}8\\text{ N/m}^3$"], 0, "Ta có $d = 10D = 10 \\cdot 7800 = 78\\,000\\text{ N/m}^3$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về khối lượng riêng:", [
                "Nước nguyên chất có khối lượng riêng $D = 1000\\text{ kg/m}^3 = 1\\text{ g/cm}^3$.",
                "Hai vật làm bằng cùng một chất đặc thì vật có thể tích gấp đôi sẽ có khối lượng riêng gấp đôi.",
                "Dầu ăn nổi trên mặt nước vì khối lượng riêng của dầu ăn ($\\approx 800\\text{ kg/m}^3$) nhỏ hơn khối lượng riêng của nước.",
                "Một khối sắt đặc có thể tích $0{,}01\\text{ m}^3$ và khối lượng riêng $7800\\text{ kg/m}^3$ thì nặng $78\\text{ kg}$.",
            ], [True, False, True, True], "Ý b) sai vì khối lượng riêng là đặc trưng của chất làm vật, không phụ thuộc kích thước to hay nhỏ của vật đặc đó."),
            short("vandung", "Một thỏi đồng đặc có thể tích $V = 50\\text{ cm}^3$ và khối lượng $m = 445\\text{ g}$. Khối lượng riêng của đồng bằng bao nhiêu $\\text{g/cm}^3$?", ["8,9", "8.9"], "Áp dụng công thức $D = \\dfrac{m}{V} = \\dfrac{445}{50} = 8{,}9\\text{ g/cm}^3$.", unit="g/cm³"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 2: Thực hành xác định khối lượng riêng",
        icon="🧪",
        description="Phương pháp thực hành đo khối lượng riêng của khối hộp chữ nhật, vật rắn không thấm nước và chất lỏng.",
        requirements=[
            "Trình bày được cách xác định khối lượng riêng của một khối hộp chữ nhật bằng cân và thước thẳng ($V = a \\cdot b \\cdot c$).",
            "Trình bày được cách đo thể tích vật rắn hình dạng bất kì không thấm nước bằng bình chia độ ($V = V_2 - V_1$).",
            "Tính được khối lượng riêng của chất lỏng bằng cân điện tử và bình chia độ ($m_{\\text{lỏng}} = m_{\\text{cả bình}} - m_{\\text{bình rỗng}}$).",
        ],
        definition="Để thực hành xác định khối lượng riêng $D = \\dfrac{m}{V}$ của một vật rắn hoặc chất lỏng, ta dùng cân để đo khối lượng $m$ và dùng thước hoặc bình chia độ để đo thể tích $V$.",
        theory=(
            "### 1. Xác định khối lượng riêng của vật rắn\n"
            "- **Khối hộp chữ nhật**: Dùng cân đo khối lượng $m$; dùng thước đo 3 kích thước dài $a$, rộng $b$, cao $c$, tính thể tích $V = a \\cdot b \\cdot c$ rồi tính $D = \\dfrac{m}{V}$.\n"
            "- **Vật rắn nhỏ không thấm nước có hình dạng bất kì (viên sỏi, quả nặng)**:\n"
            "  1. Dùng cân điện tử đo khối lượng $m$ của vật.\n"
            "  2. Đổ nước vào bình chia độ, ghi thể tích $V_1$.\n"
            "  3. Thả chìm hoàn toàn vật vào bình chia độ, ghi mực nước mới $V_2$. Thể tích vật là $V = V_2 - V_1$.\n"
            "  4. Tính khối lượng riêng: $D = \\dfrac{m}{V_2 - V_1}$.\n\n"
            "### 2. Xác định khối lượng riêng của một lượng chất lỏng\n"
            "- Cân cốc rỗng được $m_1$, đổ thể tích $V$ chất lỏng vào cốc rồi cân được $m_2$. Khối lượng chất lỏng là $m = m_2 - m_1$, suy ra $D = \\dfrac{m_2 - m_1}{V}$."
        ),
        formulas=[
            G(
                "Công thức thực hành đo khối lượng riêng",
                F("Khối lượng riêng của vật rắn đo bằng bình chia độ", "$V = V_2 - V_1 \\implies D = \\dfrac{m}{V_2 - V_1}$", "Trong đó $V_1$ là thể tích nước ban đầu, $V_2$ là thể tích nước khi thả chìm vật ($1\\text{ mL} = 1\\text{ cm}^3$)."),
                F("Khối lượng riêng của chất lỏng", "$m = m_2 - m_1 \\implies D = \\dfrac{m_2 - m_1}{V}$", "Trong đó $m_1$ là khối lượng bình rỗng, $m_2$ là khối lượng bình chứa thể tích $V$ chất lỏng."),
            )
        ],
        example="Trong bài thực hành đo khối lượng riêng của một hòn sỏi: cân điện tử chỉ khối lượng hòn sỏi là $m = 65\\text{ g}$. Khi thả chìm hoàn toàn hòn sỏi vào bình chia độ đang chứa $V_1 = 50\\text{ cm}^3$ nước thì mực nước dâng lên tới vạch $V_2 = 75\\text{ cm}^3$. Tính khối lượng riêng của hòn sỏi.",
        example_answer="Thể tích của hòn sỏi là $V = V_2 - V_1 = 75 - 50 = 25\\text{ cm}^3$. Khối lượng riêng của hòn sỏi là $D = \\dfrac{m}{V} = \\dfrac{65}{25} = 2{,}6\\text{ g/cm}^3 = 2600\\text{ kg/m}^3$.",
        real_life="Truyền thuyết kể rằng nhà bác học Archimedes đã tìm ra cách đo thể tích chiếc vương miện có hình dáng phức tạp của nhà vua bằng phần nước dâng lên khi nhúng chìm vương miện vào nước.",
        quiz=[
            mcq("biet", "Để đo thể tích của một viên sỏi nhỏ không thấm nước có hình dạng bất kì trong phòng thực hành, dụng cụ nào sau đây được sử dụng?", ["Bình chia độ chứa nước", "Thước thẳng milimét", "Lực kế lò xo", "Nhiệt kế rượu"], 0, "Viên sỏi có hình dạng bất kì không thể tính bằng công thức hình học đơn giản nên dùng bình chia độ chứa nước ($V = V_2 - V_1$)."),
            mcq("biet", "Khi thả chìm hoàn toàn một vật rắn không thấm nước vào bình chia độ có mực nước ban đầu $V_1$, mực nước dâng lên đến vạch $V_2$. Thể tích $V$ của vật rắn là:", ["$V = V_2 - V_1$", "$V = V_2 + V_1$", "$V = \\dfrac{V_2 + V_1}{2}$", "$V = V_1 \\cdot V_2$"], 0, "Phần nước dâng lên trong bình chia độ chính bằng thể tích của vật rắn bị chìm: $V = V_2 - V_1$."),
            mcq("hieu", "Khi thực hành đo khối lượng riêng của một viên sỏi, vì sao ta nên cân khối lượng $m$ của viên sỏi khô **trước** khi thả viên sỏi vào bình chia độ chứa nước?", ["Vì nếu nhúng nước trước rồi mới cân thì nước bám vào bề mặt viên sỏi làm khối lượng đo được bị lớn hơn thực tế", "Vì viên sỏi sau khi nhúng nước sẽ tan hết", "Vì cân điện tử không hoạt động sau khi dùng bình chia độ", "Vì thể tích viên sỏi tăng gấp đôi sau khi cân"], 0, "Cân lúc viên sỏi còn khô giúp tránh sai số do các giọt nước bám dính trên bề mặt viên sỏi."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về thực hành đo khối lượng riêng:", [
                "Đối với khối gỗ hình hộp chữ nhật có các cạnh $a, b, c$, ta có thể đo thể tích bằng thước theo công thức $V = a \\cdot b \\cdot c$.",
                "Đơn vị $1\\text{ mL}$ ghi trên vạch bình chia độ đúng bằng $1\\text{ cm}^3$.",
                "Khi thả vật vào bình chia độ, nếu nước bị tràn ra ngoài miệng bình thì hiệu $V_2 - V_1$ trên vạch bình vẫn đúng bằng thể tích vật.",
                "Để giảm sai số phép đo, người ta tiến hành đo khối lượng và thể tích $3$ lần rồi lấy giá trị trung bình.",
            ], [True, True, False, True], "Ý c) sai vì khi nước tràn ra ngoài bình chia độ thì $V_2 - V_1$ nhỏ hơn thể tích thật của vật (lúc đó phải dùng bình tràn)."),
            short("vandung", "Một bình chia độ rỗng có khối lượng $m_1 = 40\\text{ g}$. Khi rót thêm $V = 50\\text{ cm}^3$ dầu ăn vào bình và đặt lên cân điện tử thì cân chỉ $m_2 = 80\\text{ g}$. Khối lượng riêng của dầu ăn bằng bao nhiêu $\\text{g/cm}^3$?", ["0,8", "0.8"], "Khối lượng dầu ăn là $m = m_2 - m_1 = 80 - 40 = 40\\text{ g}$. Khối lượng riêng của dầu ăn là $D = \\dfrac{40}{50} = 0{,}8\\text{ g/cm}^3$.", unit="g/cm³"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 3: Tác dụng của chất lỏng lên vật đặt trong nó. Lực đẩy Archimedes",
        icon="🚢",
        description="Phương, chiều, công thức độ lớn lực đẩy Archimedes F_A = d.V và điều kiện định tính – định lượng để vật nổi, lơ lửng, chìm.",
        requirements=[
            "Mô tả được một vật nhúng trong chất lỏng chịu tác dụng của lực đẩy Archimedes có phương thẳng đứng, chiều từ dưới lên trên.",
            "Viết và vận dụng được công thức tính độ lớn lực đẩy Archimedes: $F_A = d \\cdot V$ (bằng trọng lượng phần chất lỏng bị vật chiếm chỗ).",
            "Giải thích được điều kiện để một vật chìm xuống ($F_A < P$ hay $d_{\\text{vật}} > d_{\\text{lỏng}}$), lơ lửng ($F_A = P$) và nổi lên ($F_A > P$).",
        ],
        definition="Mọi vật nhúng vào chất lỏng đều bị chất lỏng đẩy thẳng đứng từ dưới lên với một lực có độ lớn bằng trọng lượng của phần chất lỏng mà vật chiếm chỗ. Lực này gọi là lực đẩy Archimedes: $F_A = d \\cdot V$.",
        theory=(
            "### 1. Lực đẩy Archimedes\n"
            "- **Phương và chiều**: phương thẳng đứng, chiều **từ dưới lên trên** (ngược chiều với trọng lực $\\vec{P}$).\n"
            "- **Công thức tính độ lớn**:\n"
            "  $$F_A = d \\cdot V$$\n"
            "  trong đó $d$ là trọng lượng riêng của chất lỏng ($\\text{N/m}^3$), $V$ là thể tích **phần chất lỏng bị vật chiếm chỗ** ($\\text{m}^3$).\n"
            "- Khi treo vật vào lực kế: ngoài không khí lực kế chỉ $P$, khi nhúng chìm vật trong chất lỏng lực kế chỉ $P' = P - F_A \\implies F_A = P - P'$.\n\n"
            "### 2. Điều kiện vật nổi, vật chìm\n"
            "- Thả một vật đặc có trọng lượng $P$ (trọng lượng riêng $d_v$) vào chất lỏng có trọng lượng riêng $d_l$:\n"
            "  - **Vật chìm xuống đáy** khi $F_A < P \\iff d_v > d_l$.\n"
            "  - **Vật lơ lửng trong chất lỏng** khi $F_A = P \\iff d_v = d_l$.\n"
            "  - **Vật nổi lên mặt thoáng** khi $F_A > P \\iff d_v < d_l$ (khi đã nằm cân bằng trên mặt thoáng thì $F_A' = d_l V_{\\text{chìm}} = P$)."
        ),
        formulas=[
            G(
                "Công thức lực đẩy Archimedes và điều kiện nổi",
                F("Độ lớn lực đẩy Archimedes", "$F_A = d \\cdot V = 10 \\cdot D \\cdot V$", "Trong đó $d$ là trọng lượng riêng chất lỏng ($\\text{N/m}^3$), $V$ là thể tích phần vật chìm trong chất lỏng ($\\text{m}^3$)."),
                F("Xác định lực đẩy Archimedes bằng lực kế", "$F_A = P - P'$", "Trong đó $P$ là số chỉ lực kế khi treo vật ngoài không khí, $P'$ là số chỉ lực kế khi nhúng vật trong chất lỏng."),
            )
        ],
        example="Một vật rắn có thể tích $V = 0{,}002\\text{ m}^3$ được nhúng chìm hoàn toàn trong nước có trọng lượng riêng $d = 10\\,000\\text{ N/m}^3$. Hãy tính độ lớn lực đẩy Archimedes tác dụng lên vật.",
        example_answer="Áp dụng công thức lực đẩy Archimedes: $F_A = d \\cdot V = 10\\,000 \\cdot 0{,}002 = 20\\text{ N}$.",
        real_life="Tàu thủy làm bằng thép (có $d_{\\text{thép}} > d_{\\text{nước}}$) vẫn nổi được trên mặt biển vì thân tàu được thiết kế rỗng có thể tích phần chìm $V$ rất lớn làm tăng lực đẩy Archimedes $F_A = P_{\\text{tàu}}$.",
        quiz=[
            mcq("biet", "Lực đẩy Archimedes tác dụng lên một vật nhúng trong chất lỏng có phương và chiều như thế nào?", ["Phương thẳng đứng, chiều từ dưới lên trên", "Phương thẳng đứng, chiều từ trên xuống dưới", "Phương nằm ngang, chiều từ trái sang phải", "Mọi phương đều như nhau"], 0, "Lực đẩy Archimedes luôn có phương thẳng đứng và chiều hướng từ dưới lên trên."),
            mcq("biet", "Công thức tính độ lớn lực đẩy Archimedes $F_A$ là gì (với $d$ là trọng lượng riêng của chất lỏng, $V$ là thể tích phần chất lỏng bị vật chiếm chỗ)?", ["$F_A = d \\cdot V$", "$F_A = \\dfrac{d}{V}$", "$F_A = \\dfrac{V}{d}$", "$F_A = d + V$"], 0, "Theo định luật Archimedes, $F_A = d \\cdot V$."),
            mcq("hieu", "Treo một quả nặng vào lực kế ngoài không khí thì lực kế chỉ $P = 12\\text{ N}$. Khi nhúng chìm quả nặng vào trong nước thì lực kế chỉ $P' = 7\\text{ N}$. Độ lớn lực đẩy Archimedes của nước tác dụng lên quả nặng là bao nhiêu?", ["$5\\text{ N}$", "$19\\text{ N}$", "$7\\text{ N}$", "$12\\text{ N}$"], 0, "Độ lớn lực đẩy Archimedes là $F_A = P - P' = 12 - 7 = 5\\text{ N}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về lực đẩy Archimedes:", [
                "Một thỏi nhôm và một thỏi chì có cùng thể tích $V$ khi nhúng chìm hoàn toàn vào cùng một chậu nước thì chịu lực đẩy Archimedes bằng nhau.",
                "Một vật đặc sẽ nổi lên khi trọng lượng riêng của vật nhỏ hơn trọng lượng riêng của chất lỏng ($d_{\\text{vật}} < d_{\\text{lỏng}}$).",
                "Lực đẩy Archimedes phụ thuộc vào độ sâu của vật đã chìm hoàn toàn trong chất lỏng.",
                "Khinh khí cầu bay lên cao được trong không khí cũng nhờ lực đẩy Archimedes của không khí tác dụng lên nó.",
            ], [True, True, False, True], "Ý c) sai vì khi vật đã chìm hoàn toàn trong chất lỏng đồng chất thì thể tích chiếm chỗ $V$ không đổi nên $F_A = d \\cdot V$ không phụ thuộc độ sâu."),
            short("vandung", "Một vật có thể tích $V = 500\\text{ cm}^3 = 0{,}0005\\text{ m}^3$ được nhúng chìm hoàn toàn trong nước có trọng lượng riêng $d = 10\\,000\\text{ N/m}^3$. Lực đẩy Archimedes tác dụng lên vật có độ lớn bằng bao nhiêu Newton ($\\text{N}$)?", ["5"], "Ta có $F_A = d \\cdot V = 10\\,000 \\cdot 0{,}0005 = 5\\text{ N}$.", unit="N"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 4: Áp suất trên một bề mặt",
        icon="📌",
        description="Khái niệm áp lực, công thức tính áp suất p = F/S, đơn vị Pascal (Pa) và nguyên tắc làm tăng, giảm áp suất.",
        requirements=[
            "Nêu được áp lực là lực ép có phương vuông góc với mặt bị ép.",
            "Viết và vận dụng được công thức tính áp suất $p = \\dfrac{F}{S}$ và đơn vị Pascal ($1\\text{ Pa} = 1\\text{ N/m}^2$).",
            "Giải thích được các cách làm tăng áp suất (tăng $F$, giảm diện tích bị ép $S$) hoặc giảm áp suất (giảm $F$, tăng diện tích bị ép $S$) trong đời sống.",
        ],
        definition="Áp lực là lực ép có phương vuông góc với mặt bị ép. Áp suất được tính bằng độ lớn của áp lực trên một đơn vị diện tích bị ép: $p = \\dfrac{F}{S}$ (đơn vị $\\text{Pa} = \\text{N/m}^2$).",
        theory=(
            "### 1. Áp lực và áp suất\n"
            "- **Áp lực ($F$)**: lực ép có phương vuông góc với bề mặt bị ép. Khi một vật đặt yên trên mặt phẳng nằm ngang thì áp lực của vật lên mặt sàn bằng chính trọng lượng của vật ($F = P$).\n"
            "- **Áp suất ($p$)**: đặc trưng cho tác dụng mạnh hay yếu của áp lực trên một đơn vị diện tích bị ép:\n"
            "  $$p = \\dfrac{F}{S}$$\n"
            "- **Đơn vị đo áp suất**: **Pascal** (kí hiệu $\\text{Pa}$), với $1\\text{ Pa} = 1\\text{ N/m}^2$ và $1\\text{ kPa} = 1000\\text{ Pa}$.\n\n"
            "### 2. Tăng và giảm áp suất trong thực tiễn\n"
            "- **Làm tăng áp suất** ($p$ tăng): tăng áp lực $F$ hoặc **giảm diện tích bị ép $S$** (mài sắc lưỡi dao, vuốt nhọn mũi đinh, mũi kim tiêm).\n"
            "- **Làm giảm áp suất** ($p$ giảm): giảm áp lực $F$ hoặc **tăng diện tích bị ép $S$** (xe tăng dùng bánh xích bản rộng, kê ván gỗ dưới bánh ô tô khi qua bùn lầy, làm móng nhà rộng)."
        ),
        formulas=[
            G(
                "Công thức tính áp suất trên một bề mặt",
                F("Công thức tính áp suất", "$p = \\dfrac{F}{S} \\implies F = p \\cdot S; \\quad S = \\dfrac{F}{p}$", "Trong đó $F$ là áp lực ($\\text{N}$), $S$ là diện tích bị ép ($\\text{m}^2$), $p$ là áp suất ($\\text{Pa} = \\text{N/m}^2$)."),
                F("Quy đổi đơn vị diện tích và áp suất", "$1\\text{ cm}^2 = 10^{-4}\\text{ m}^2; \\qquad 1\\text{ kPa} = 1000\\text{ Pa}$", "Lưu ý luôn đổi diện tích bị ép ra $\\text{m}^2$ trước khi tính áp suất ra $\\text{Pa}$."),
            )
        ],
        example="Một người có trọng lượng $P = 600\\text{ N}$ đứng bằng cả hai bàn chân trên mặt sàn nằm ngang. Biết diện tích tiếp xúc của mỗi bàn chân với mặt sàn là $S_1 = 0{,}015\\text{ m}^2$. Hãy tính áp suất của người đó tác dụng lên mặt sàn.",
        example_answer="Tổng diện tích bị ép của hai bàn chân là $S = 2 \\cdot 0{,}015 = 0{,}03\\text{ m}^2$. Áp lực lên mặt sàn bằng trọng lượng của người: $F = P = 600\\text{ N}$. Áp suất tác dụng lên sàn là $p = \\dfrac{F}{S} = \\dfrac{600}{0{,}03} = 20\\,000\\text{ Pa} = 20\\text{ kPa}$.",
        real_life="Xe tăng nặng hàng chục tấn nhưng chạy được trên đất mềm nhờ lắp bản xích sắt có diện tích tiếp xúc $S$ rất lớn để làm giảm áp suất, còn lưỡi dao kéo được mài thật mỏng (diện tích $S$ rất nhỏ) để tạo áp suất lớn dễ cắt thái.",
        quiz=[
            mcq("biet", "Công thức tính áp suất $p$ trên một bề mặt chịu áp lực $F$ có diện tích bị ép $S$ là gì?", ["$p = \\dfrac{F}{S}$", "$p = F \\cdot S$", "$p = \\dfrac{S}{F}$", "$p = F + S$"], 0, "Áp suất bằng độ lớn áp lực chia cho diện tích bị ép: $p = \\dfrac{F}{S}$."),
            mcq("biet", "Đơn vị đo áp suất Pascal ($\\text{Pa}$) tương ứng với biểu thức đơn vị nào sau đây?", ["$1\\text{ Pa} = 1\\text{ N/m}^2$", "$1\\text{ Pa} = 1\\text{ N}\\cdot\\text{m}^2$", "$1\\text{ Pa} = 1\\text{ kg/m}^3$", "$1\\text{ Pa} = 1\\text{ N/m}^3$"], 0, "Vì $p = \\dfrac{F}{S}$ nên $1\\text{ Pa} = 1\\text{ N/m}^2$."),
            mcq("hieu", "Vì sao mũi đinh, mũi kim khâu và mũi kim tiêm đều được chế tạo rất nhọn?", ["Để giảm diện tích bị ép $S$, từ đó làm tăng mạnh áp suất giúp dễ đâm xuyên qua vật", "Để tăng diện tích bị ép $S$, giúp giảm áp suất", "Để làm giảm áp lực $F$ của tay", "Để tăng khối lượng của chiếc đinh"], 0, "Với cùng một áp lực $F$, mũi đinh càng nhọn thì diện tích bị ép $S$ càng nhỏ nên áp suất $p = \\dfrac{F}{S}$ càng lớn."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về áp lực và áp suất:", [
                "Áp lực là lực ép có phương vuông góc với mặt bị ép.",
                "Khi một người đang đứng bằng hai chân mà co một chân lên thì áp suất tác dụng lên mặt sàn tăng gấp đôi.",
                "Bánh xe tăng dùng dây xích bản rộng có tác dụng làm tăng áp suất lên mặt đất mềm.",
                "Một thùng hàng nặng $400\\text{ N}$ có diện tích đáy tiếp xúc sàn là $0{,}2\\text{ m}^2$ gây ra áp suất $2000\\text{ Pa}$.",
            ], [True, True, False, True], "Ý c) sai vì dây xích bản rộng làm tăng diện tích tiếp xúc $S$ nhằm giảm áp suất để xe tăng không bị lún."),
            short("vandung", "Một thùng gỗ có trọng lượng $F = 900\\text{ N}$ đặt trên mặt sàn nằm ngang với diện tích tiếp xúc là $S = 0{,}3\\text{ m}^2$. Áp suất của thùng gỗ tác dụng lên mặt sàn bằng bao nhiêu $\\text{Pa}$?", ["3000"], "Áp dụng công thức $p = \\dfrac{F}{S} = \\dfrac{900}{0{,}3} = 3000\\text{ Pa}$.", unit="Pa"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 5: Áp suất chất lỏng và áp suất khí quyển",
        icon="🌊",
        description="Áp suất chất lỏng p = d.h, nguyên lý bình thông nhau, máy nén thủy lực và sự tồn tại của áp suất khí quyển.",
        requirements=[
            "Mô tả được chất lỏng gây ra áp suất theo mọi phương lên đáy bình, thành bình và các vật ở trong lòng nó.",
            "Vận dụng được công thức tính áp suất chất lỏng $p = d \\cdot h$ và nguyên tắc máy nén thủy lực $\\dfrac{F_1}{F_2} = \\dfrac{S_1}{S_2}$.",
            "Giải thích được sự tồn tại của áp suất khí quyển và các hiện tượng thực tế như giác mút, ống hút, lỗ thông khí trên nắp ấm trà.",
        ],
        definition="Chất lỏng gây ra áp suất theo mọi phương lên đáy bình, thành bình và các vật ở trong lòng nó. Tại độ sâu $h$ tính từ mặt thoáng chất lỏng, áp suất do cột chất lỏng gây ra là $p = d \\cdot h$.",
        theory=(
            "### 1. Áp suất chất lỏng và bình thông nhau\n"
            "- Công thức áp suất chất lỏng: $p = d \\cdot h$, trong đó $d$ là trọng lượng riêng chất lỏng ($\\text{N/m}^3$), $h$ là **độ sâu tính từ mặt thoáng chất lỏng đến điểm xét** ($\\text{m}$).\n"
            "- **Bình thông nhau**: Trong bình thông nhau chứa cùng một chất lỏng đứng yên, các mặt thoáng của chất lỏng ở các nhánh khác nhau đều ở cùng một độ cao.\n"
            "- **Máy nén thủy lực**: Áp suất tác dụng lên chất lỏng trong bình kín được truyền nguyên vẹn đi mọi hướng (nguyên lí Pascal), do đó $\\dfrac{F_1}{F_2} = \\dfrac{S_1}{S_2}$.\n\n"
            "### 2. Áp suất khí quyển\n"
            "- Trái Đất được bao bọc bởi lớp khí quyển dày hàng ngàn kilômét; vì không khí có trọng lượng nên gây ra **áp suất khí quyển** theo mọi phương (ở ngang mực nước biển $p_0 \\approx 101\\,300\\text{ Pa} \\approx 760\\text{ mmHg}$).\n"
            "- Càng lên cao, không khí càng loãng nên áp suất khí quyển càng giảm."
        ),
        formulas=[
            G(
                "Áp suất chất lỏng và Máy nén thủy lực",
                F("Công thức áp suất chất lỏng ở độ sâu h", "$p = d \\cdot h = 10 \\cdot D \\cdot h$", "Lưu ý $h$ luôn tính từ mặt thoáng chất lỏng xuống điểm đang xét (không phải khoảng cách từ điểm đó xuống đáy bình)."),
                F("Hệ thức máy nén thủy lực (Nguyên lí Pascal)", "$\\dfrac{F_1}{F_2} = \\dfrac{S_1}{S_2} \\implies F_2 = F_1 \\cdot \\dfrac{S_2}{S_1}$", "Nếu diện tích pít-tông lớn $S_2$ gấp $k$ lần diện tích pít-tông nhỏ $S_1$ thì lực nâng $F_2$ lớn gấp $k$ lần lực ép $F_1$."),
            )
        ],
        example="Một người thợ lặn đang lặn ở độ sâu $h = 15\\text{ m}$ dưới mặt nước biển. Biết trọng lượng riêng của nước biển là $d = 10\\,300\\text{ N/m}^3$. Hãy tính áp suất của cột nước biển tác dụng lên người thợ lặn ở độ sâu đó.",
        example_answer="Áp suất do cột nước biển gây ra ở độ sâu $h = 15\\text{ m}$ là $p = d \\cdot h = 10\\,300 \\cdot 15 = 154\\,500\\text{ Pa} = 154{,}5\\text{ kPa}$.",
        real_life="Đê chắn nước và đập thủy điện luôn có phần chân đập xây rộng và dày hơn phần đỉnh đập vì càng xuống sâu dưới nước, áp suất chất lỏng $p = d \\cdot h$ càng lớn.",
        quiz=[
            mcq("biet", "Công thức tính áp suất chất lỏng $p$ tại một điểm ở độ sâu $h$ so với mặt thoáng chất lỏng có trọng lượng riêng $d$ là gì?", ["$p = d \\cdot h$", "$p = \\dfrac{d}{h}$", "$p = \\dfrac{h}{d}$", "$p = d + h$"], 0, "Áp suất chất lỏng tại độ sâu $h$ được tính bằng công thức $p = d \\cdot h$."),
            mcq("biet", "Trong một bình thông nhau chứa cùng một chất lỏng đứng yên, mực chất lỏng ở các nhánh có đặc điểm gì?", ["Luôn ở cùng một độ cao dù tiết diện các nhánh khác nhau", "Nhánh nào to hơn thì mực chất lỏng thấp hơn", "Nhánh nào nhỏ hơn thì mực chất lỏng thấp hơn", "Phụ thuộc vào hình dạng cong hay thẳng của nhánh"], 0, "Trong bình thông nhau chứa cùng một chất lỏng đứng yên, các mặt thoáng luôn ở cùng một độ cao."),
            mcq("hieu", "Vì sao trên nắp ấm pha trà thường có một lỗ nhỏ thông với không khí bên ngoài?", ["Để áp suất khí quyển đẩy vào mặt nước trong ấm, giúp rót nước trà ra khỏi vòi dễ dàng", "Để hơi nước không bay ra ngoài được", "Để làm giảm khối lượng của chiếc nắp ấm", "Để tăng nhiệt độ sôi của nước trong ấm"], 0, "Nhờ lỗ nhỏ trên nắp ấm, áp suất khí quyển nén lên mặt nước bên trong cân bằng với áp suất khí quyển ở đầu vòi, giúp nước chảy ra đều đặn."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về áp suất chất lỏng và áp suất khí quyển:", [
                "Càng lặn sâu xuống đáy biển, áp suất của nước biển tác dụng lên cơ thể người thợ lặn càng lớn.",
                "Một thùng cao $1{,}2\\text{ m}$ chứa đầy nước ($d = 10\\,000\\text{ N/m}^3$) gây ra áp suất ở đáy thùng là $12\\,000\\text{ Pa}$.",
                "Càng lên đỉnh núi cao, áp suất khí quyển càng tăng mạnh.",
                "Kích thủy lực dùng để nâng ô tô hoạt động dựa trên sự truyền nguyên vẹn áp suất trong chất lỏng.",
            ], [True, True, False, True], "Ý c) sai vì càng lên cao không khí càng loãng và bề dày lớp khí quyển phía trên giảm nên áp suất khí quyển giảm."),
            short("vandung", "Một bể bơi chứa nước ngọt ($d = 10\\,000\\text{ N/m}^3$) có độ sâu của nước là $h = 2\\text{ m}$. Áp suất do nước gây ra tại đáy bể bơi bằng bao nhiêu $\\text{Pa}$?", ["20000"], "Áp dụng công thức $p = d \\cdot h = 10\\,000 \\cdot 2 = 20\\,000\\text{ Pa}$.", unit="Pa"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 6: Tác dụng làm quay của lực. Moment lực",
        icon="🔧",
        description="Điều kiện để lực làm quay vật quanh một trục, khái niệm cánh tay đòn và công thức moment lực M = F.d.",
        requirements=[
            "Nêu được khi giá của lực không cắt trục quay và không song song với trục quay thì lực có tác dụng làm vật quay quanh trục đó.",
            "Xác định được cánh tay đòn $d$ của lực là khoảng cách vuông góc từ trục quay đến giá của lực.",
            "Viết và vận dụng được công thức tính moment lực $M = F \\cdot d$ (đơn vị $\\text{N}\\cdot\\text{m}$).",
        ],
        definition="Moment lực đối với một trục quay là đại lượng đặc trưng cho tác dụng làm quay của lực và được đo bằng tích của độ lớn lực $F$ với cánh tay đòn $d$ của nó: $M = F \\cdot d$ (đơn vị $\\text{N}\\cdot\\text{m}$).",
        theory=(
            "### 1. Tác dụng làm quay của lực\n"
            "- Một lực tác dụng lên vật có trục quay cố định $O$ sẽ làm quay vật nếu **giá của lực không đi qua trục quay** ($d > 0$) và không song song với trục quay.\n"
            "- **Cánh tay đòn ($d$)**: khoảng cách vuông góc từ trục quay $O$ đến giá của lực $\\vec{F}$ (đơn vị $\\text{m}$).\n\n"
            "### 2. Công thức tính Moment lực\n"
            "- Độ lớn moment lực:\n"
            "  $$M = F \\cdot d$$\n"
            "- Đơn vị của moment lực trong hệ SI là **Newton nhân mét** ($\\text{N}\\cdot\\text{m}$).\n"
            "- Lực $F$ càng lớn hoặc cánh tay đòn $d$ càng dài thì moment lực $M$ càng lớn (tác dụng làm quay càng mạnh)."
        ),
        formulas=[
            G(
                "Công thức tính Moment lực",
                F("Biểu thức tính moment lực", "$M = F \\cdot d$", "Trong đó $F$ là độ lớn của lực ($\\text{N}$), $d$ là cánh tay đòn ($\\text{m}$), $M$ có đơn vị $\\text{N}\\cdot\\text{m}$."),
                F("Khi giá của lực đi qua trục quay", "$d = 0 \\implies M = 0$", "Lực có giá cắt trục quay thì không gây ra tác dụng làm quay vật."),
            )
        ],
        example="Một người thợ dùng cờ-lê để vặn một đai ốc với lực $F = 40\\text{ N}$ vuông góc với thân cờ-lê tại điểm cách tâm đai ốc (trục quay) một khoảng $d = 25\\text{ cm} = 0{,}25\\text{ m}$. Hãy tính moment lực do người thợ tạo ra.",
        example_answer="Đổi $d = 25\\text{ cm} = 0{,}25\\text{ m}$. Moment lực tác dụng lên đai ốc là $M = F \\cdot d = 40 \\cdot 0{,}25 = 10\\text{ N}\\cdot\\text{m}$.",
        real_life="Tay nắm cửa luôn được lắp ở mép ngoài cánh cửa (xa bản lề nhất) để tăng cánh tay đòn $d$, giúp mở cửa nhẹ nhàng với một lực nhỏ.",
        quiz=[
            mcq("biet", "Công thức tính moment lực $M$ của một lực $F$ có cánh tay đòn $d$ đối với trục quay là gì?", ["$M = F \\cdot d$", "$M = \\dfrac{F}{d}$", "$M = \\dfrac{d}{F}$", "$M = F + d$"], 0, "Moment lực bằng tích độ lớn của lực với cánh tay đòn của nó: $M = F \\cdot d$."),
            mcq("biet", "Đơn vị của moment lực trong hệ SI là gì?", ["$\\text{N}\\cdot\\text{m}$", "$\\text{N/m}$", "$\\text{N/m}^2$", "$\\text{kg}\\cdot\\text{m}$"], 0, "Vì $F$ tính bằng $\\text{N}$ và $d$ tính bằng $\\text{m}$ nên moment lực $M = F \\cdot d$ có đơn vị $\\text{N}\\cdot\\text{m}$."),
            mcq("hieu", "Vì sao để tháo một chiếc bu-lông bị rỉ sét chặt, người thợ máy thường nối thêm một đoạn ống thép dài vào cán cờ-lê?", ["Để làm tăng cánh tay đòn $d$, từ đó làm tăng moment lực $M$ giúp vặn bu-lông dễ hơn", "Để làm giảm cánh tay đòn $d$", "Để làm giảm moment lực $M$", "Để giá của lực đi qua tâm bu-lông"], 0, "Nối dài cán cờ-lê giúp tăng cánh tay đòn $d$, nên với cùng một lực tay $F$ sẽ tạo ra moment lực $M = F \\cdot d$ lớn hơn nhiều."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về moment lực:", [
                "Cánh tay đòn của lực là khoảng cách vuông góc từ trục quay đến giá của lực.",
                "Nếu lực tác dụng có giá đi thẳng qua bản lề (trục quay) của cánh cửa thì cánh cửa sẽ không quay.",
                "Tác dụng làm quay của lực chỉ phụ thuộc vào độ lớn của lực mà không phụ thuộc vị trí đặt lực.",
                "Một lực $20\\text{ N}$ có cánh tay đòn $0{,}5\\text{ m}$ tạo ra moment lực bằng $10\\text{ N}\\cdot\\text{m}$.",
            ], [True, True, False, True], "Ý c) sai vì tác dụng làm quay phụ thuộc vào cả độ lớn lực $F$ lẫn cánh tay đòn $d$."),
            short("vandung", "Tác dụng một lực $F = 50\\text{ N}$ vuông góc với cánh cửa tại tay nắm cách trục bản lề một khoảng $d = 0{,}8\\text{ m}$. Moment của lực đó bằng bao nhiêu $\\text{N}\\cdot\\text{m}$?", ["40"], "Áp dụng công thức $M = F \\cdot d = 50 \\cdot 0{,}8 = 40\\text{ N}\\cdot\\text{m}$.", unit="N.m"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 7: Đòn bẩy và ứng dụng",
        icon="⚖️",
        description="Cấu tạo đòn bẩy (điểm tựa O, hai lực F₁ và F₂), điều kiện cân bằng đòn bẩy F₁.d₁ = F₂.d₂ và các loại đòn bẩy.",
        requirements=[
            "Chỉ ra được các yếu tố của một đòn bẩy: điểm tựa (trục quay) $O$, điểm tác dụng của lực nâng vật $F_1$ và lực tác dụng của người $F_2$.",
            "Vận dụng được điều kiện cân bằng của đòn bẩy: $F_1 \\cdot d_1 = F_2 \\cdot d_2$ (hay $\\dfrac{F_1}{F_2} = \\dfrac{d_2}{d_1}$).",
            "Phân loại và lấy được ví dụ về các loại đòn bẩy trong kỹ thuật, đời sống và trên cơ thể người.",
        ],
        definition="Đòn bẩy là một thanh cứng có thể quay quanh một điểm cố định gọi là điểm tựa $O$. Đòn bẩy cân bằng khi moment của hai lực làm quay đòn bẩy theo hai chiều ngược nhau bằng nhau: $F_1 \\cdot d_1 = F_2 \\cdot d_2$.",
        theory=(
            "### 1. Quy tắc cân bằng của đòn bẩy\n"
            "- Gọi $F_1$ là lực của vật tác dụng lên đòn bẩy (cánh tay đòn $d_1$) và $F_2$ là lực người tác dụng lên đòn bẩy (cánh tay đòn $d_2$).\n"
            "- Khi đòn bẩy cân bằng:\n"
            "  $$M_1 = M_2 \\iff F_1 \\cdot d_1 = F_2 \\cdot d_2 \\iff \\dfrac{F_1}{F_2} = \\dfrac{d_2}{d_1}$$\n"
            "- Nếu cánh tay đòn của lực người lớn hơn cánh tay đòn của vật ($d_2 > d_1$) thì lực người cần tác dụng nhỏ hơn trọng lượng vật ($F_2 < F_1$), tức là **được lợi về lực**.\n\n"
            "### 2. Các loại đòn bẩy trong đời sống\n"
            "- **Loại 1 (Điểm tựa $O$ ở giữa $F_1$ và $F_2$)**: bập bênh, cái kéo, kìm cắt sắt, xà beng bẩy đá, cân đòn.\n"
            "- **Loại 2 (Điểm tựa $O$ ở một đầu, vật ở giữa, lực tác dụng ở đầu kia, luôn $d_2 > d_1$)**: xe rùa đẩy gạch, kẹp tách hạt dẻ, dụng cụ mở nắp chai.\n"
            "- **Loại 3 (Điểm tựa $O$ ở một đầu, lực tác dụng ở giữa, vật ở đầu kia, $d_2 < d_1$ nhưng lợi về đường đi/tốc độ)**: đũa ăn cơm, nhíp gắp, cần câu cá, cánh tay người nâng tạ."
        ),
        formulas=[
            G(
                "Điều kiện cân bằng của đòn bẩy",
                F("Phương trình cân bằng đòn bẩy", "$F_1 \\cdot d_1 = F_2 \\cdot d_2 \\implies F_2 = F_1 \\cdot \\dfrac{d_1}{d_2}$", "Muốn dùng lực nhỏ $F_2$ để nâng vật nặng $F_1$, ta phải đặt điểm tựa $O$ gần vật hơn ($d_1 < d_2$)."),
                F("Hệ số lợi về lực của đòn bẩy", "$k = \\dfrac{F_1}{F_2} = \\dfrac{d_2}{d_1}$", "Cánh tay đòn $d_2$ dài gấp mấy lần $d_1$ thì ta được lợi bấy nhiêu lần về lực."),
            )
        ],
        example="Dùng một chiếc xà beng làm đòn bẩy để bẩy một tảng đá có trọng lượng $F_1 = 1200\\text{ N}$. Biết khoảng cách từ điểm tựa $O$ đến điểm tì vào tảng đá là $d_1 = 0{,}2\\text{ m}$ và khoảng cách từ điểm tựa $O$ đến tay người ấn là $d_2 = 1{,}2\\text{ m}$. Tính lực tối thiểu $F_2$ mà tay người cần tác dụng để nâng tảng đá.",
        example_answer="Theo điều kiện cân bằng của đòn bẩy: $F_1 \\cdot d_1 = F_2 \\cdot d_2 \\implies F_2 = \\dfrac{F_1 \\cdot d_1}{d_2} = \\dfrac{1200 \\cdot 0{,}2}{1{,}2} = 200\\text{ N}$.",
        real_life="Trên cơ thể người, khớp khuỷu tay đóng vai trò là điểm tựa $O$, cơ nhị đầu co lại tạo lực kéo và bàn tay cầm quả tạ tạo thành một đòn bẩy sinh học.",
        quiz=[
            mcq("biet", "Hệ thức biểu thị điều kiện cân bằng của đòn bẩy chịu tác dụng của hai lực $F_1$ (cánh tay đòn $d_1$) và $F_2$ (cánh tay đòn $d_2$) là gì?", ["$F_1 \\cdot d_1 = F_2 \\cdot d_2$", "$\\dfrac{F_1}{d_1} = \\dfrac{F_2}{d_2}$", "$F_1 + d_1 = F_2 + d_2$", "$F_1 \\cdot F_2 = d_1 \\cdot d_2$"], 0, "Đòn bẩy cân bằng khi $M_1 = M_2 \\iff F_1 \\cdot d_1 = F_2 \\cdot d_2$."),
            mcq("biet", "Để dùng đòn bẩy nâng một vật nặng có trọng lượng $F_1$ bằng một lực $F_2$ nhỏ hơn trọng lượng của vật ($F_2 < F_1$), ta phải bố trí điểm tựa $O$ như thế nào?", ["Đặt điểm tựa $O$ gần điểm đặt của vật hơn gần tay người ($d_1 < d_2$)", "Đặt điểm tựa $O$ cách đều vật và tay người ($d_1 = d_2$)", "Đặt điểm tựa $O$ gần tay người hơn gần vật ($d_2 < d_1$)", "Đặt điểm tựa $O$ trùng với vị trí tay người ($d_2 = 0$)"], 0, "Vì $F_2 = F_1 \\cdot \\dfrac{d_1}{d_2}$, nên muốn $F_2 < F_1$ thì phải có $d_1 < d_2$."),
            mcq("hieu", "Hai bạn nhỏ chơi bập bênh: bạn An nặng $400\\text{ N}$ ngồi cách trục quay ở giữa một đoạn $d_1 = 1{,}5\\text{ m}$. Bạn Bình nặng $300\\text{ N}$ phải ngồi ở phía bên kia cách trục quay bao nhiêu mét để bập bênh nằm ngang cân bằng?", ["$2{,}0\\text{ m}$", "$1{,}5\\text{ m}$", "$1{,}0\\text{ m}$", "$2{,}5\\text{ m}$"], 0, "Ta có $F_1 d_1 = F_2 d_2 \\implies d_2 = \\dfrac{400 \\cdot 1{,}5}{300} = 2{,}0\\text{ m}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đòn bẩy:", [
                "Chiếc kéo cắt giấy và chiếc bập bênh là đòn bẩy có điểm tựa nằm ở khoảng giữa hai lực.",
                "Xe rùa đẩy vật liệu xây dựng là đòn bẩy có điểm tựa ở trục bánh xe, luôn cho lợi về lực.",
                "Dùng đũa gắp thức ăn hoặc dùng nhíp gắp vật nhỏ luôn cho ta lợi về lực ($F_2 < F_1$).",
                "Nếu cánh tay đòn của lực người dài gấp $4$ lần cánh tay đòn của vật nặng thì lực người cần tác dụng chỉ bằng $\\dfrac{1}{4}$ trọng lượng vật.",
            ], [True, True, False, True], "Ý c) sai vì đũa và nhíp có điểm tựa ở đầu trên, tay cầm ở giữa ($d_2 < d_1$) nên không lợi về lực nhưng lợi về đường đi và sự khéo léo."),
            short("vandung", "Một đòn bẩy dùng để nâng vật nặng $F_1 = 600\\text{ N}$ có khoảng cách từ vật đến điểm tựa là $d_1 = 0{,}3\\text{ m}$. Nếu tay người tác dụng lực ở đầu kia cách điểm tựa $d_2 = 1{,}5\\text{ m}$ thì lực $F_2$ tối thiểu để nâng vật bằng bao nhiêu Newton ($\\text{N}$)?", ["120"], "Áp dụng công thức $F_2 = \\dfrac{F_1 \\cdot d_1}{d_2} = \\dfrac{600 \\cdot 0{,}3}{1{,}5} = 120\\text{ N}$.", unit="N"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 8: Sự nhiễm điện do cọ xát",
        icon="🎈",
        description="Hiện tượng vật nhiễm điện do cọ xát, hai loại điện tích dương (+) và âm (-), tương tác điện và sự dịch chuyển electron.",
        requirements=[
            "Mô tả được một vật sau khi bị cọ xát có khả năng hút các vật nhẹ (vụn giấy, sợi bông) hoặc tạo tia lửa điện là vật đã bị nhiễm điện.",
            "Nêu được có hai loại điện tích là điện tích dương ($+$) và điện tích âm ($-$); các điện tích cùng loại thì đẩy nhau, khác loại thì hút nhau.",
            "Giải thích được sơ lược sự nhiễm điện do cọ xát dựa vào sự dịch chuyển của các electron giữa hai vật.",
        ],
        definition="Nhiều vật sau khi bị cọ xát có khả năng hút các vật nhẹ khác được gọi là các vật nhiễm điện (hay vật mang điện tích). Có hai loại điện tích là điện tích dương ($+$) và điện tích âm ($-$): hai vật nhiễm điện cùng loại thì đẩy nhau, khác loại thì hút nhau.",
        theory=(
            "### 1. Hai loại điện tích và tương tác điện\n"
            "- Quy ước:\n"
            "  - Điện tích của **thanh thủy tinh cọ xát vào lụa** là **điện tích dương ($+$)**.\n"
            "  - Điện tích của **thanh nhựa sẫm màu (hoặc thước nhựa) cọ xát vào vải khô** là **điện tích âm ($-$)**.\n"
            "- **Tương tác giữa các vật mang điện**: Hai điện tích **cùng dấu** ($+$ với $+$, hoặc $-$ với $-$) thì **đẩy nhau**; hai điện tích **trái dấu** ($+$ với $-$) thì **hút nhau**.\n\n"
            "### 2. Giải thích bằng cấu tạo nguyên tử\n"
            "- Bình thường nguyên tử trung hòa về điện (tổng điện tích dương của hạt nhân bằng tổng điện tích âm của các electron).\n"
            "- Khi cọ xát, chỉ có các **electron** dịch chuyển từ vật này sang vật khác:\n"
            "  - Vật **nhận thêm electron** sẽ nhiễm điện **âm ($-$)**.\n"
            "  - Vật **mất bớt electron** sẽ nhiễm điện **dương ($+$)**."
        ),
        formulas=[
            G(
                "Quy tắc nhiễm điện và tương tác điện tích",
                F("Quy tắc nhiễm điện do dịch chuyển electron", "$\\text{Nhận thêm } e^- \\implies \\text{Nhiễm điện âm } (-); \\qquad \\text{Mất bớt } e^- \\implies \\text{Nhiễm điện dương } (+)$", "Hạt nhân mang điện dương nằm sâu bên trong nguyên tử nên không dịch chuyển khi cọ xát."),
                F("Quy tắc tương tác giữa hai điện tích", "$q_1, q_2 \\text{ cùng dấu } \\implies \\text{Đẩy nhau}; \\qquad q_1, q_2 \\text{ trái dấu } \\implies \\text{Hút nhau}$", "Một vật nhiễm điện (dù dương hay âm) cũng đều hút được các vật nhẹ chưa nhiễm điện (như vụn giấy)."),
            )
        ],
        example="Khi cọ xát một chiếc lược nhựa vào mảnh vải len khô, có một lượng electron dịch chuyển từ mảnh vải len sang chiếc lược nhựa. Hỏi sau khi cọ xát, chiếc lược nhựa và mảnh vải len mang điện tích loại gì?",
        example_answer="Chiếc lược nhựa nhận thêm electron nên nhiễm điện **âm ($-$)**; mảnh vải len bị mất bớt electron nên nhiễm điện **dương ($+$)**.",
        real_life="Vào những ngày mùa đông hanh khô, khi cởi áo len ta thường nghe thấy tiếng lách tách nhỏ và thấy áo hút tóc do sự nhiễm điện khi cọ xát; xe chở xăng dầu luôn có một dây xích sắt thả chạm đất để truyền điện tích phát sinh do ma sát xuống đất, tránh tia lửa điện gây cháy nổ.",
        quiz=[
            mcq("biet", "Trong tự nhiên có mấy loại điện tích và đó là những loại nào?", ["$2$ loại: điện tích dương ($+$) và điện tích âm ($-$)", "$2$ loại: cực Bắc ($\\text{N}$) và cực Nam ($\\text{S}$)", "$3$ loại: dương, âm và trung tính", "$1$ loại duy nhất là điện tích âm"], 0, "Có $2$ loại điện tích là điện tích dương ($+$) và điện tích âm ($-$)."),
            mcq("biet", "Một vật trung hòa về điện sau khi cọ xát trở thành vật nhiễm điện **dương ($+$)** là do nguyên nhân nào?", ["Do vật đó bị mất bớt một số electron", "Do vật đó nhận thêm một số electron", "Do vật đó nhận thêm hạt nhân từ vật khác", "Do các electron trong vật biến thành hạt nhân"], 0, "Electron mang điện tích âm; khi vật mất bớt electron thì phần điện tích dương của hạt nhân trội hơn nên vật nhiễm điện dương."),
            mcq("hieu", "Treo hai quả cầu nhẹ $A$ và $B$ đã nhiễm điện bằng hai sợi chỉ tơ mảnh gần nhau thì thấy chúng đẩy nhau. Biết quả cầu $A$ nhiễm điện âm ($-$), hỏi quả cầu $B$ nhiễm điện gì?", ["Quả cầu $B$ cũng nhiễm điện âm ($-$)", "Quả cầu $B$ nhiễm điện dương ($+$)", "Quả cầu $B$ không mang điện", "Quả cầu $B$ vừa mang điện dương vừa mang điện âm"], 0, "Hai vật nhiễm điện đẩy nhau khi chúng mang điện tích cùng loại, do đó $B$ cũng nhiễm điện âm ($-$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sự nhiễm điện do cọ xát:", [
                "Theo quy ước, thanh thủy tinh sau khi cọ xát vào lụa thì nhiễm điện dương ($+$).",
                "Hai vật nhiễm điện trái dấu đặt gần nhau thì hút nhau.",
                "Khi cọ xát hai vật trung hòa với nhau, hạt nhân mang điện dương di chuyển từ vật này sang vật kia.",
                "Cánh quạt điện quay lâu ngày bám nhiều bụi bẩn ở mép cánh vì cánh quạt cọ xát với không khí bị nhiễm điện và hút các hạt bụi nhẹ.",
            ], [True, True, False, True], "Ý c) sai vì chỉ có các electron mới dịch chuyển từ vật này sang vật kia khi cọ xát."),
            short("vandung", "Có tất cả bao nhiêu loại điện tích trong tự nhiên (dương và âm)?", ["2"], "Có $2$ loại điện tích là điện tích dương ($+$) và điện tích âm ($-$)."),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 9: Dòng điện và nguồn điện",
        icon="🔋",
        description="Định nghĩa dòng điện, bản chất dòng điện trong kim loại, chiều dòng điện quy ước, nguồn điện, vật dẫn điện và vật cách điện.",
        requirements=[
            "Nêu được dòng điện là dòng chuyển dời có hướng của các hạt mang điện; trong kim loại đó là dòng các electron tự do dịch chuyển có hướng.",
            "Trình bày đúng quy ước chiều dòng điện: đi từ cực dương ($+$) qua dây dẫn và các thiết bị điện tới cực âm ($-$) của nguồn điện.",
            "Phân biệt được nguồn điện (pin, ắc quy), vật dẫn điện (kim loại, dung dịch muối/axit) và vật cách điện (nhựa, cao su, sứ, thủy tinh).",
        ],
        definition="Dòng điện là dòng chuyển dời có hướng của các hạt mang điện. Chiều dòng điện được quy ước là chiều từ cực dương ($+$) qua dây dẫn và các dụng cụ điện tới cực âm ($-$) của nguồn điện.",
        theory=(
            "### 1. Dòng điện và chiều dòng điện quy ước\n"
            "- **Dòng điện**: dòng chuyển dời có hướng của các hạt mang điện.\n"
            "- **Trong dây dẫn kim loại**: các hạt mang điện dịch chuyển là các **electron tự do** (mang điện âm, đi từ cực âm sang cực dương của nguồn).\n"
            "- **Chiều dòng điện quy ước**: từ **cực dương ($+$)** qua dây dẫn và thiết bị điện tới **cực âm ($-$)** của nguồn điện (ngược với chiều dịch chuyển của electron tự do trong kim loại).\n\n"
            "### 2. Nguồn điện, vật dẫn điện và vật cách điện\n"
            "- **Nguồn điện**: thiết bị tạo ra và duy trì dòng điện lâu dài trong mạch kín; mỗi nguồn điện یک chiều (pin, ắc quy) đều có 2 cực: cực dương ($+$) và cực âm ($-$).\n"
            "- **Vật dẫn điện**: vật cho dòng điện đi qua (đồng, nhôm, sắt, bạc, than chì, dung dịch muối, axit...).\n"
            "- **Vật cách điện**: vật không cho dòng điện đi qua (nhựa, cao su, sứ, thủy tinh, gỗ khô, nước cất tinh khiết)."
        ),
        formulas=[
            G(
                "Quy ước chiều dòng điện và phân loại vật liệu điện",
                F("Chiều dòng điện quy ước trong mạch kín", "$\\text{Cực dương } (+) \\longrightarrow \\text{Dây dẫn \\& Thiết bị} \\longrightarrow \\text{Cực âm } (-)$", "Ngược chiều với chiều dịch chuyển có hướng của các electron tự do ($(-) \\to (+)$) trong kim loại."),
                F("Điều kiện để có dòng điện chạy qua thiết bị", "$\\text{Nguồn điện} + \\text{Mạch điện dẫn điện khép kín (Công tắc đóng)}$", "Nếu công tắc mở (mạch hở) thì dòng điện không chạy qua mạch."),
            )
        ],
        example="Trong một mạch điện kín gồm một viên pin nối với một bóng đèn nhỏ bằng dây đồng, hãy so sánh chiều của dòng điện theo quy ước và chiều dịch chuyển có hướng của các electron tự do trong dây đồng.",
        example_answer="Chiều dòng điện theo quy ước đi từ cực dương ($+$) của viên pin qua dây đồng và bóng đèn về cực âm ($-$) của pin; còn các electron tự do trong dây đồng bị cực âm đẩy và cực dương hút nên dịch chuyển ngược lại từ cực âm ($-$) qua bóng đèn về cực dương ($+$).",
        real_life="Dây điện trong gia đình luôn có lõi làm bằng đồng (vật dẫn điện rất tốt) và lớp vỏ bọc bên ngoài làm bằng nhựa dẻo PVC (vật cách điện an toàn).",
        quiz=[
            mcq("biet", "Theo quy ước, chiều của dòng điện trong một mạch điện kín được xác định như thế nào?", ["Chiều từ cực dương ($+$) qua dây dẫn và các thiết bị điện tới cực âm ($-$) của nguồn điện", "Chiều từ cực âm ($-$) qua dây dẫn tới cực dương ($+$) của nguồn điện", "Chiều trùng với chiều chuyển động của các electron tự do trong kim loại", "Dòng điện không có chiều xác định"], 0, "Chiều dòng điện được quy ước là chiều từ cực dương ($+$) qua dây dẫn và dụng cụ điện tới cực âm ($-$) của nguồn điện."),
            mcq("biet", "Nhóm các vật liệu nào sau đây đều là **vật dẫn điện** ở điều kiện thường?", ["Đồng, nhôm, bạc, ruột bút chì (than chì)", "Nhựa, cao su, sứ, thủy tinh", "Gỗ khô, giấy khô, vải khô", "Không khí khô, nước cất nguyên chất, cao su"], 0, "Các kim loại (đồng, nhôm, bạc) và than chì có nhiều electron tự do nên dẫn điện tốt."),
            mcq("hieu", "Vì sao cán của tua-vít thử điện, kìm điện và vỏ phích cắm điện luôn được bọc bằng nhựa cứng hoặc cao su?", ["Vì nhựa và cao su là vật cách điện, ngăn dòng điện truyền sang tay người gây điện giật", "Vì nhựa và cao su dẫn điện tốt hơn đồng", "Để làm tăng cường độ dòng điện trong mạch", "Để biến dòng điện một chiều thành xoay chiều"], 0, "Nhựa và cao su là các chất cách điện giúp đảm bảo an toàn điện cho người sử dụng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dòng điện và nguồn điện:", [
                "Dòng điện trong kim loại là dòng các electron tự do dịch chuyển có hướng.",
                "Chiều dịch chuyển có hướng của các electron tự do trong dây đồng ngược với chiều quy ước của dòng điện.",
                "Mỗi nguồn điện một chiều như pin hay ắc quy đều có hai cực là cực dương ($+$) và cực âm ($-$).",
                "Nước muối loãng và nước chanh là các chất cách điện hoàn toàn.",
            ], [True, True, True, False], "Ý d) sai vì dung dịch muối và dung dịch axit (nước chanh) có chứa các ion tự do nên là chất dẫn điện."),
            short("vandung", "Cho 4 vật sau: (1) Lõi dây đồng, (2) Thanh nhôm, (3) Vỏ bọc nhựa PVC, (4) Găng tay cao su khô. Có bao nhiêu vật trong 4 vật trên là **vật dẫn điện**?", ["2"], "Lõi dây đồng (1) và thanh nhôm (2) là $2$ vật dẫn điện; còn nhựa PVC và cao su khô là vật cách điện."),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 10: Mạch điện đơn giản và các tác dụng của dòng điện",
        icon="💡",
        description="Kí hiệu các bộ phận trên sơ đồ mạch điện, mạch kín – mạch hở và 5 tác dụng của dòng điện.",
        requirements=[
            "Nhận biết được kí hiệu sơ đồ của nguồn điện (pin), công tắc đóng/mở, bóng đèn, điện trở, chuông điện, điốt phát quang (LED) và dây nối.",
            "Vẽ được sơ đồ mạch điện đơn giản và biểu diễn chiều dòng điện bằng mũi tên trên sơ đồ khi công tắc đóng.",
            "Nêu và lấy được ví dụ về các tác dụng của dòng điện: tác dụng nhiệt, tác dụng phát sáng, tác dụng hóa học, tác dụng từ và tác dụng sinh lí.",
        ],
        definition="Sơ đồ mạch điện là hình vẽ sử dụng các kí hiệu quy ước để mô tả cách mắc các bộ phận của mạch điện. Khi có dòng điện chạy qua, dòng điện có thể gây ra tác dụng nhiệt, phát sáng, hóa học, từ và sinh lí.",
        theory=(
            "### 1. Sơ đồ mạch điện đơn giản\n"
            "- Một mạch điện cơ bản gồm: **nguồn điện** (cực dài là $+$, cực ngắn và dày là $-$), **công tắc (khóa $K$)**, **thiết bị tiêu thụ điện** (bóng đèn, chuông, quạt) và **dây dẫn**.\n"
            "- **Cầu chì** hoặc **cầu dao tự động (aptomat)** được mắc vào mạch điện để tự động ngắt mạch bảo vệ khi dòng điện tăng quá mức (đoản mạch, quá tải).\n\n"
            "### 2. Các tác dụng của dòng điện\n"
            "1. **Tác dụng nhiệt**: làm nóng vật dẫn (bàn là điện, nồi cơm điện, ấm siêu tốc, cầu chì).\n"
            "2. **Tác dụng phát sáng**: làm đèn LED, đèn bút thử điện, đèn huỳnh quang phát sáng.\n"
            "3. **Tác dụng hóa học**: phân tích dung dịch điện phân (dùng để mạ điện như mạ vàng, mạ kẽm, tinh luyện đồng).\n"
            "4. **Tác dụng từ**: làm quay kim nam châm, tạo nam châm điện (chuông điện, quạt điện, động cơ điện).\n"
            "5. **Tác dụng sinh lí**: đi qua cơ thể người và động vật làm co giật cơ (ứng dụng trong máy sốc tim y học, châm cứu điện; nhưng nguy hiểm gây điện giật nếu bất cẩn)."
        ),
        formulas=[
            G(
                "Nguyên tắc mạch điện và 5 tác dụng của dòng điện",
                F("Trạng thái khóa K và dòng điện trong mạch", "$K \\text{ đóng (mạch kín)} \\implies I > 0; \\qquad K \\text{ mở (mạch hở)} \\implies I = 0$", "Trên sơ đồ mạch kín, mũi tên chỉ chiều dòng điện luôn vẽ đi ra từ cực dương ($+$) và đi vào cực âm ($-$)."),
                F("5 tác dụng đặc trưng của dòng điện", "$\\text{Dòng điện} \\longrightarrow \\{\\text{Nhiệt, Phát sáng, Hóa học, Từ, Sinh lí}\\}$", "Mỗi thiết bị điện được chế tạo dựa trên một hoặc hai tác dụng chính có ích của dòng điện."),
            )
        ],
        example="Người ta dùng dòng điện chạy qua dung dịch muối đồng sunfat ($\\text{CuSO}_4$) để phủ một lớp đồng mỏng màu đỏ lên bề mặt một chiếc chìa khóa bằng sắt nối với cực âm. Hiện tượng này dựa trên tác dụng nào của dòng điện?",
        example_answer="Quá trình mạ đồng lên chiếc chìa khóa sắt dựa trên **tác dụng hóa học** của dòng điện khi đi qua dung dịch muối kim loại.",
        real_life="Cầu chì và aptomat trong tủ điện gia đình tự động ngắt mạch khi có sự cố chập điện, giúp phòng chống cháy nổ do tác dụng nhiệt quá mức của dòng điện.",
        quiz=[
            mcq("biet", "Các dụng cụ nào sau đây hoạt động chủ yếu dựa trên **tác dụng nhiệt** của dòng điện?", ["Bàn là điện, nồi cơm điện và ấm đun nước siêu tốc", "Đèn LED báo nguồn và bút thử điện", "Bình điện phân để mạ vàng trang sức", "La bàn từ"], 0, "Bàn là, nồi cơm điện và ấm đun nước biến đổi điện năng thành nhiệt năng dựa trên tác dụng nhiệt của dòng điện."),
            mcq("biet", "Trên sơ đồ mạch điện, kí hiệu của nguồn điện 1 pin gồm hai đoạn thẳng song song dài ngắn khác nhau. Đoạn thẳng dài hơn biểu diễn cực nào của pin?", ["Cực dương ($+$)", "Cực âm ($-$)", "Công tắc đóng", "Bóng đèn sợi đốt"], 0, "Theo quy ước sơ đồ mạch điện, vạch thẳng dài và mảnh là cực dương ($+$), vạch ngắn và đậm là cực âm ($-$)."),
            mcq("hieu", "Ứng dụng mạ vàng, mạ bạc lên vỏ đồng hồ hoặc mạ kẽm chống gỉ cho các tấm tôn dựa trên tác dụng nào của dòng điện?", ["Tác dụng hóa học", "Tác dụng sinh lí", "Tác dụng phát sáng", "Tác dụng cơ học"], 0, "Mạ điện là ứng dụng điển hình của tác dụng hóa học của dòng điện khi chạy qua dung dịch chất điện phân."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về mạch điện và tác dụng của dòng điện:", [
                "Khi công tắc (khóa $K$) mở, mạch điện bị hở nên bóng đèn không sáng.",
                "Đèn điốt phát quang (đèn LED) chỉ cho dòng điện đi qua theo một chiều nhất định và hoạt động dựa trên tác dụng phát sáng.",
                "Máy khử rung tim (sốc điện cấp cứu) trong y học là ứng dụng của tác dụng sinh lí của dòng điện.",
                "Cầu chì được mắc trong mạch điện chỉ để làm bóng đèn sáng mạnh gấp đôi.",
            ], [True, True, True, False], "Ý d) sai vì cầu chì dùng để bảo vệ mạch điện, tự động nóng chảy và ngắt mạch khi dòng điện tăng quá mức an toàn."),
            short("vandung", "Trong chương trình Vật lý 8, dòng điện có mấy tác dụng cơ bản được xét (nhiệt, phát sáng, hóa học, từ, sinh lí)?", ["5"], "Dòng điện có $5$ tác dụng cơ bản: tác dụng nhiệt, phát sáng, hóa học, từ và sinh lí."),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 11: Cường độ dòng điện và hiệu điện thế",
        icon="🎛️",
        description="Cường độ dòng điện I (A, mA) đo bằng ampe kế mắc nối tiếp; hiệu điện thế U (V, mV, kV) đo bằng vôn kế mắc song song.",
        requirements=[
            "Nêu được cường độ dòng điện ($I$) cho biết mức độ mạnh, yếu của dòng điện, có đơn vị là Ampe ($\\text{A}$) và đo bằng ampe kế mắc nối tiếp.",
            "Nêu được hiệu điện thế ($U$) có đơn vị là Vôn ($\\text{V}$) và đo bằng vôn kế mắc song song với dụng cụ cần đo.",
            "Quy đổi thành thạo giữa các đơn vị $\\text{A} \\leftrightarrow \\text{mA}$ và $\\text{kV} \\leftrightarrow \\text{V} \\leftrightarrow \\text{mV}$.",
        ],
        definition="Cường độ dòng điện (kí hiệu $I$, đơn vị Ampe – $\\text{A}$) là đại lượng đặc trưng cho độ mạnh, yếu của dòng điện và được đo bằng ampe kế. Hiệu điện thế (kí hiệu $U$, đơn vị Vôn – $\\text{V}$) được tạo ra giữa hai cực của nguồn điện và được đo bằng vôn kế.",
        theory=(
            "### 1. Cường độ dòng điện và Ampe kế\n"
            "- Kí hiệu cường độ dòng điện: $I$. Đơn vị trong hệ SI: **Ampe** ($\\text{A}$). Bội và ước: $1\\text{ A} = 1000\\text{ mA}$; $1\\text{ mA} = 0{,}001\\text{ A}$.\n"
            "- **Ampe kế** (kí hiệu chữ $\\text{A}$ trong vòng tròn) dùng để đo cường độ dòng điện.\n"
            "- **Cách mắc Ampe kế**: mắc **nối tiếp** với bộ phận cần đo sao cho chốt dương ($+$) của ampe kế nối về phía cực dương ($+$) của nguồn điện (tuyệt đối không mắc trực tiếp hai chốt của ampe kế vào hai cực nguồn điện).\n\n"
            "### 2. Hiệu điện thế và Vôn kế\n"
            "- Kí hiệu hiệu điện thế: $U$. Đơn vị trong hệ SI: **Vôn** ($\\text{V}$). Đổi đơn vị: $1\\text{ kV} = 1000\\text{ V}$; $1\\text{ V} = 1000\\text{ mV}$.\n"
            "- **Vôn kế** (kí hiệu chữ $\\text{V}$ trong vòng tròn) dùng để đo hiệu điện thế.\n"
            "- **Cách mắc Vôn kế**: mắc **song song** vào hai đầu thiết bị điện hoặc hai cực của nguồn điện (chốt $+$ nối về phía cực $+$ của nguồn).\n"
            "- Số vôn ghi trên dụng cụ điện là **hiệu điện thế định mức** để dụng cụ hoạt động bình thường."
        ),
        formulas=[
            G(
                "Đơn vị và quy tắc mắc Ampe kế – Vôn kế",
                F("Quy đổi đơn vị Cường độ dòng điện I", "$1\\text{ A} = 1000\\text{ mA}; \\qquad 1\\text{ mA} = 10^{-3}\\text{ A}$", "Ampe kế luôn mắc **nối tiếp** vào đoạn mạch cần đo."),
                F("Quy đổi đơn vị Hiệu điện thế U", "$1\\text{ kV} = 1000\\text{ V}; \\qquad 1\\text{ V} = 1000\\text{ mV}$", "Vôn kế luôn mắc **song song** với hai đầu dụng cụ cần đo."),
            )
        ],
        example="Một bóng đèn pin khi sáng bình thường có dòng điện chạy qua là $I = 0{,}35\\text{ A}$ ở hiệu điện thế $U = 3\\text{ V}$. Hãy đổi cường độ dòng điện này ra đơn vị miliampe ($\\text{mA}$) và hiệu điện thế này ra đơn vị milivôn ($\\text{mV}$).",
        example_answer="Ta có $I = 0{,}35\\text{ A} = 0{,}35 \\cdot 1000 = 350\\text{ mA}$ và $U = 3\\text{ V} = 3 \\cdot 1000 = 3000\\text{ mV}$.",
        real_life="Ổ cắm điện lưới sinh hoạt ở Việt Nam có hiệu điện thế $220\\text{ V}$, trong khi một viên pin con thỏ có hiệu điện thế $1{,}5\\text{ V}$ và ắc quy xe máy có hiệu điện thế $12\\text{ V}$.",
        quiz=[
            mcq("biet", "Để đo cường độ dòng điện chạy qua một bóng đèn, ta dùng dụng cụ nào và mắc như thế nào vào mạch điện?", ["Dùng ampe kế mắc nối tiếp với bóng đèn", "Dùng vôn kế mắc song song với bóng đèn", "Dùng ampe kế mắc song song với bóng đèn", "Dùng vôn kế mắc nối tiếp với bóng đèn"], 0, "Cường độ dòng điện được đo bằng ampe kế mắc nối tiếp với dụng cụ cần đo."),
            mcq("biet", "Đơn vị đo hiệu điện thế trong hệ SI là gì?", ["Vôn ($\\text{V}$)", "Ampe ($\\text{A}$)", "Newton ($\\text{N}$)", "Pascal ($\\text{Pa}$)"], 0, "Đơn vị đo hiệu điện thế là Vôn (kí hiệu $\\text{V}$)."),
            mcq("hieu", "Đổi đơn vị: Cường độ dòng điện $I = 250\\text{ mA}$ tương ứng với bao nhiêu Ampe ($\\text{A}$)?", ["$0{,}25\\text{ A}$", "$2{,}5\\text{ A}$", "$25\\text{ A}$", "$250\\,000\\text{ A}$"], 0, "Vì $1\\text{ A} = 1000\\text{ mA}$ nên $250\\text{ mA} = \\dfrac{250}{1000} = 0{,}25\\text{ A}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cường độ dòng điện và hiệu điện thế:", [
                "Vôn kế được mắc song song với hai đầu bóng đèn để đo hiệu điện thế giữa hai đầu bóng đèn.",
                "Chốt dương ($+$) của ampe kế và vôn kế đều phải được nối về phía cực dương ($+$) của nguồn điện.",
                "Ta có thể mắc trực tiếp hai chốt của ampe kế vào hai cực của nguồn điện mà không cần qua bóng đèn.",
                "Đổi đơn vị: $0{,}5\\text{ kV} = 500\\text{ V}$.",
            ], [True, True, False, True], "Ý c) sai vì mắc trực tiếp hai chốt của ampe kế vào hai cực nguồn điện sẽ gây đoản mạch làm hỏng ampe kế và nguồn điện."),
            short("vandung", "Một ampe kế đo dòng điện chạy qua bóng đèn chỉ $I = 0{,}6\\text{ A}$. Giá trị cường độ dòng điện này bằng bao nhiêu miliampe ($\\text{mA}$)?", ["600"], "Đổi $I = 0{,}6\\text{ A} = 0{,}6 \\cdot 1000 = 600\\text{ mA}$.", unit="mA"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 12: Năng lượng nhiệt và nội năng",
        icon="🔥",
        description="Chuyển động nhiệt của các phân tử, khái niệm năng lượng nhiệt (nhiệt năng), nội năng và mối liên hệ với nhiệt độ.",
        requirements=[
            "Nêu được các phân tử, nguyên tử cấu tạo nên vật luôn chuyển động không ngừng; nhiệt độ của vật càng cao thì các phân tử chuyển động càng nhanh.",
            "Định nghĩa được nội năng của một vật là tổng động năng và thế năng của các phân tử cấu tạo nên vật.",
            "Giải thích được khi một vật được làm nóng lên thì nhiệt độ và nội năng của vật đều tăng.",
        ],
        definition="Nội năng của một vật là tổng động năng và thế năng tương tác của các phân tử, nguyên tử cấu tạo nên vật. Năng lượng nhiệt (nhiệt năng) là phần năng lượng vật nhận thêm hay mất bớt trong quá trình truyền nhiệt.",
        theory=(
            "### 1. Chuyển động nhiệt của phân tử và Nội năng\n"
            "- Các phân tử cấu tạo nên vật chuyển động hỗn loạn không ngừng nên chúng có **động năng**; đồng thời giữa các phân tử có lực tương tác và khoảng cách nên chúng có **thế năng**.\n"
            "- **Nội năng ($U$)** của vật bằng tổng động năng và thế năng của toàn bộ các phân tử cấu tạo nên vật:\n"
            "  $$U = \\sum W_{\\text{đ phân tử}} + \\sum W_{\\text{t phân tử}}$$\n\n"
            "### 2. Liên hệ giữa Nội năng, Nhiệt năng và Nhiệt độ\n"
            "- Khi **nhiệt độ của vật tăng**, các phân tử chuyển động hỗn loạn **nhanh hơn**, động năng phân tử tăng nên **nội năng của vật tăng**.\n"
            "- Có hai cách làm tăng nội năng của vật: **thực hiện công** (cọ xát đồng xu xuống mặt bàn) hoặc **truyền nhiệt** (nhúng thìa vào cốc nước nóng)."
        ),
        formulas=[
            G(
                "Nội năng và sự biến đổi nội năng theo nhiệt độ",
                F("Biểu thức khái niệm Nội năng", "$U = W_{\\text{đ phân tử}} + W_{\\text{t phân tử}}$", "Mọi vật ở bất kì nhiệt độ nào (kể cả nước đá ở $0^\\circ\\text{C}$) đều luôn có nội năng vì các phân tử luôn chuyển động."),
                F("Quan hệ giữa nhiệt độ và nội năng của một vật", "$T \\text{ tăng} \\implies v_{\\text{phân tử}} \\text{ tăng} \\implies \\text{Nội năng } U \\text{ tăng}$", "Nhiệt lượng $Q$ là số đo phần năng lượng nhiệt được truyền từ vật nóng hơn sang vật lạnh hơn."),
            )
        ],
        example="Khi thả một chiếc thìa bằng bạc ở nhiệt độ phòng ($25^\\circ\\text{C}$) vào một cốc nước sôi ($95^\\circ\\text{C}$), nhiệt độ và nội năng của chiếc thìa bạc và của nước trong cốc thay đổi như thế nào?",
        example_answer="Nhiệt truyền từ nước sôi sang thìa bạc nên chiếc thìa bạc nóng lên: **nhiệt độ và nội năng của thìa bạc tăng lên**; ngược lại nước trong cốc nguội bớt nên **nhiệt độ và nội năng của nước giảm đi**.",
        real_life="Khi bơm xe đạp bằng bơm tay hoặc khi cưa một thanh sắt, thân ống bơm và lưỡi cưa nóng ran lên vì nội năng của chúng đã tăng lên do ma sát và nén khí.",
        quiz=[
            mcq("biet", "Nội năng của một vật là gì?", ["Tổng động năng và thế năng của các phân tử, nguyên tử cấu tạo nên vật", "Chỉ riêng động năng của cả vật khi vật đang chạy trên đường", "Chỉ riêng thế năng hấp dẫn của vật so với mặt đất", "Nhiệt độ của môi trường bên ngoài vật"], 0, "Nội năng của vật là tổng động năng và thế năng tương tác của các phân tử cấu tạo nên vật."),
            mcq("biet", "Khi nhiệt độ của một vật tăng lên thì chuyển động của các phân tử cấu tạo nên vật và nội năng của vật thay đổi như thế nào?", ["Các phân tử chuyển động nhanh hơn và nội năng của vật tăng lên", "Các phân tử chuyển động chậm lại và nội năng của vật giảm đi", "Các phân tử đứng yên hoàn toàn và nội năng bằng $0$", "Chuyển động phân tử và nội năng không thay đổi"], 0, "Nhiệt độ càng cao thì các phân tử chuyển động nhiệt càng nhanh, làm động năng phân tử và nội năng của vật tăng."),
            mcq("hieu", "Một cục nước đá đang ở nhiệt độ $0^\\circ\\text{C}$ có nội năng hay không? Vì sao?", ["Có nội năng, vì các phân tử nước trong cục nước đá vẫn luôn chuyển động không ngừng và tương tác với nhau", "Không có nội năng, vì nhiệt độ của nó bằng $0^\\circ\\text{C}$", "Chỉ có nội năng khi nước đá đã tan hết thành nước lỏng", "Chỉ có nội năng khi nước đá đang rơi từ trên cao xuống"], 0, "Ở mọi nhiệt độ (kể cả $0^\\circ\\text{C}$ hay dưới $0^\\circ\\text{C}$), các phân tử cấu tạo nên vật vẫn dao động không ngừng nên vật luôn có nội năng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về năng lượng nhiệt và nội năng:", [
                "Khi cọ xát một đồng xu kim loại lên mặt bàn nhám, đồng xu nóng lên và nội năng của nó tăng.",
                "Năng lượng nhiệt tự truyền từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn.",
                "Hai cốc chứa cùng một lượng nước như nhau, cốc nước ở $80^\\circ\\text{C}$ có nội năng lớn hơn cốc nước ở $30^\\circ\\text{C}$.",
                "Chỉ những vật có nhiệt độ trên $100^\\circ\\text{C}$ mới có nội năng.",
            ], [True, True, True, False], "Ý d) sai vì mọi vật ở mọi nhiệt độ đều có nội năng."),
            short("vandung", "Nội năng của một vật là tổng của mấy dạng năng lượng của các phân tử cấu tạo nên vật (động năng phân tử và thế năng phân tử)?", ["2"], "Nội năng của vật gồm tổng của $2$ thành phần: động năng của các phân tử và thế năng tương tác giữa các phân tử."),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 13: Sự truyền nhiệt",
        icon="🍲",
        description="Ba hình thức truyền nhiệt (dẫn nhiệt, đối lưu, bức xạ nhiệt), vật dẫn nhiệt tốt – vật cách nhiệt tốt và ứng dụng.",
        requirements=[
            "Phân biệt được 3 hình thức truyền nhiệt: dẫn nhiệt (chủ yếu ở chất rắn), đối lưu (chủ yếu ở chất lỏng và chất khí) và bức xạ nhiệt (truyền bằng các tia nhiệt đi thẳng, truyền được cả trong chân không).",
            "So sánh được tính dẫn nhiệt của các chất: kim loại dẫn nhiệt rất tốt; chất lỏng, chất khí, gỗ, nhựa, len, xốp dẫn nhiệt kém (cách nhiệt tốt).",
            "Giải thích được nguyên lý cấu tạo của phích (bình giữ nhiệt), cách lắp điều hòa trên cao và lò sưởi ở dưới thấp.",
        ],
        definition="Sự truyền nhiệt có thể thực hiện theo ba hình thức: dẫn nhiệt (truyền trực tiếp qua va chạm phân tử, chủ yếu trong chất rắn), đối lưu (truyền bằng các dòng chất lỏng hoặc chất khí nóng nổi lên, lạnh chìm xuống) và bức xạ nhiệt (truyền bằng các tia nhiệt đi thẳng, truyền được trong chân không).",
        theory=(
            "### 1. Ba hình thức truyền nhiệt\n"
            "1. **Dẫn nhiệt**: Hình thức truyền nhiệt chủ yếu của **chất rắn**. Kim loại (bạc, đồng, nhôm, sắt) dẫn nhiệt rất tốt; gỗ, nhựa, thủy tinh, len, không khí dẫn nhiệt kém (cách nhiệt tốt).\n"
            "2. **Đối lưu**: Hình thức truyền nhiệt chủ yếu của **chất lỏng và chất khí** thành dòng (lớp chất lỏng/khí ở dưới nóng lên nở ra, nhẹ đi nên nổi lên trên; lớp lạnh hơn ở trên nặng hơn chìm xuống dưới).\n"
            "3. **Bức xạ nhiệt**: Sự truyền nhiệt bằng các **tia nhiệt đi thẳng** (tia hồng ngoại). Bức xạ nhiệt truyền được ngay cả trong **chân không** (ví dụ: nhiệt từ Mặt Trời truyền tới Trái Đất).\n\n"
            "### 2. Hấp thụ bức xạ nhiệt và ứng dụng\n"
            "- Vật có bề mặt **màu sẫm (đen) và nhám** hấp thụ tia nhiệt tốt hơn vật có bề mặt **màu sáng (trắng) và nhẵn bóng**.\n"
            "- **Phích nước (bình giữ nhiệt)** có hai lớp thủy tinh ở giữa hút chân không (ngăn dẫn nhiệt và đối lưu), mặt trong tráng bạc (phản xạ lại các tia bức xạ nhiệt) và có nút đậy kín."
        ),
        formulas=[
            G(
                "Đặc điểm 3 hình thức truyền nhiệt",
                F("Môi trường truyền nhiệt chủ yếu", "$\\text{Rắn: Dẫn nhiệt}; \\qquad \\text{Lỏng \\& Khí: Đối lưu}; \\qquad \\text{Chân không: Bức xạ nhiệt}$", "Trong chân không, dẫn nhiệt và đối lưu hoàn toàn không xảy ra, chỉ có bức xạ nhiệt truyền qua được."),
                F("So sánh khả năng dẫn nhiệt của các chất", "$\\text{Kim loại (Rắn)} > \\text{Chất lỏng} > \\text{Chất khí}$", "Không khí dẫn nhiệt rất kém, nên áo bông, chăn len xốp chứa nhiều lớp không khí giúp giữ ấm cơ thể."),
            )
        ],
        example="Vì sao khi đun nước bằng ấm trên bếp, người ta luôn đun từ đáy ấm ở phía dưới, trong khi dàn lạnh của máy điều hòa nhiệt độ trong phòng lại luôn được lắp ở trên cao gần sát trần nhà?",
        example_answer="Cả hai đều ứng dụng hiện tượng **đối lưu**: khi đun ở đáy ấm, lớp nước nóng ở dưới nhẹ hơn nổi lên trên và lớp nước lạnh ở trên chìm xuống làm cả ấm nước nóng đều. Ngược lại, không khí lạnh từ điều hòa nặng hơn không khí nóng nên tự chìm từ trên cao xuống dưới làm mát toàn bộ căn phòng.",
        real_life="Xoong nồi nấu ăn có phần thân làm bằng nhôm hoặc inox để dẫn nhiệt tốt giúp thức ăn nhanh chín, còn phần tay cầm bọc nhựa cứng hoặc gỗ để cách nhiệt không làm bỏng tay.",
        quiz=[
            mcq("biet", "Năng lượng nhiệt từ Mặt Trời truyền qua khoảng không vũ trụ (chân không) tới Trái Đất bằng hình thức truyền nhiệt nào?", ["Bức xạ nhiệt", "Dẫn nhiệt", "Đối lưu", "Truyền âm"], 0, "Khoảng không vũ trụ là chân không nên nhiệt từ Mặt Trời truyền tới Trái Đất bằng bức xạ nhiệt."),
            mcq("biet", "Hình thức truyền nhiệt chủ yếu trong chất lỏng và chất khí là gì?", ["Đối lưu", "Dẫn nhiệt", "Bức xạ nhiệt", "Nhiễm điện"], 0, "Trong chất lỏng và chất khí, nhiệt được truyền chủ yếu bằng các dòng đối lưu."),
            mcq("hieu", "Vì sao vào mùa hè nắng nóng, chúng ta nên mặc quần áo sáng màu thay vì quần áo màu đen sẫm?", ["Vì quần áo sáng màu phản xạ tốt các tia bức xạ nhiệt và hấp thụ ít nhiệt từ ánh nắng Mặt Trời hơn quần áo màu đen", "Vì quần áo sáng màu ngăn cản hoàn toàn đối lưu không khí", "Vì quần áo màu đen dẫn điện tốt hơn", "Vì quần áo sáng màu nặng hơn quần áo màu đen"], 0, "Bề mặt sáng màu phản xạ tia nhiệt tốt và hấp thụ bức xạ nhiệt kém nên giúp cơ thể đỡ nóng bức hơn."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sự truyền nhiệt:", [
                "Kim loại là chất dẫn nhiệt tốt nhất trong các chất rắn, còn gỗ, nhựa và không khí dẫn nhiệt rất kém.",
                "Trong chân không, cả dẫn nhiệt và đối lưu đều không thể xảy ra.",
                "Khi đun nước trong ấm, nước nóng lên chủ yếu là nhờ hình thức dẫn nhiệt từ trên mặt nước xuống đáy ấm.",
                "Lớp chân không giữa hai thành bình thủy tinh của phích nước có tác dụng ngăn cản sự dẫn nhiệt và đối lưu.",
            ], [True, True, False, True], "Ý c) sai vì nước trong ấm nóng đều lên chủ yếu nhờ dòng đối lưu từ đáy ấm đi lên."),
            short("vandung", "Có bao nhiêu hình thức truyền nhiệt cơ bản (dẫn nhiệt, đối lưu, bức xạ nhiệt)?", ["3"], "Có $3$ hình thức truyền nhiệt cơ bản: dẫn nhiệt, đối lưu và bức xạ nhiệt."),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 14: Sự nở vì nhiệt của các chất",
        icon="🛤️",
        description="Sự nở vì nhiệt của chất rắn, chất lỏng, chất khí; so sánh độ nở vì nhiệt và ứng dụng băng kép, khe hở đường ray.",
        requirements=[
            "Nêu được các chất rắn, chất lỏng và chất khí đều nở ra (thể tích tăng) khi nóng lên và co lại (thể tích giảm) khi lạnh đi.",
            "So sánh được độ nở vì nhiệt: các chất rắn và chất lỏng khác nhau nở vì nhiệt khác nhau, các chất khí khác nhau nở vì nhiệt giống nhau; chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn.",
            "Giải thích được nguyên lý của băng kép (cong về phía kim loại dãn nở vì nhiệt ít hơn khi bị đốt nóng) và tác dụng của khe hở giữa hai đầu thanh ray tàu hỏa.",
        ],
        definition="Hầu hết các chất rắn, chất lỏng và chất khí đều nở ra khi nóng lên và co lại khi lạnh đi. Chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn.",
        theory=(
            "### 1. Đặc điểm sự nở vì nhiệt của Rắn – Lỏng – Khí\n"
            "- Khi nóng lên: kích thước và thể tích $V$ của vật **tăng**, khối lượng $m$ không đổi nên khối lượng riêng $D = \\dfrac{m}{V}$ **giảm**.\n"
            "- Khi lạnh đi: kích thước và thể tích $V$ của vật **giảm** (riêng nước có sự nở đặc biệt từ $0^\\circ\\text{C}$ đến $4^\\circ\\text{C}$, ở $4^\\circ\\text{C}$ nước có khối lượng riêng lớn nhất).\n"
            "- **So sánh**:\n"
            "  - Các chất **rắn** khác nhau nở vì nhiệt **khác nhau** (ví dụ: nhôm nở nhiều hơn đồng, đồng nở nhiều hơn sắt).\n"
            "  - Các chất **lỏng** khác nhau nở vì nhiệt **khác nhau** (rượu nở nhiều hơn dầu, dầu nở nhiều hơn nước).\n"
            "  - Các chất **khí** khác nhau nở vì nhiệt **giống nhau**.\n"
            "  - Thứ tự độ nở vì nhiệt: **Khí $>$ Lỏng $>$ Rắn**.\n\n"
            "### 2. Lực xuất hiện khi co dãn vì nhiệt và Ứng dụng\n"
            "- Sự co dãn vì nhiệt khi bị ngăn cản sẽ gây ra những **lực rất lớn** (làm cong đường ray tàu hỏa, nứt dầm cầu).\n"
            "- **Băng kép**: gồm hai thanh kim loại có bản chất khác nhau (ví dụ đồng và thép) tán chặt vào nhau dọc theo chiều dài. Khi bị đốt nóng, băng kép luôn **cong về phía thanh kim loại nở vì nhiệt ít hơn** (phía thanh thép), được dùng làm rơ-le tự động đóng ngắt mạch điện trong bàn là, nồi cơm điện, ấm siêu tốc."
        ),
        formulas=[
            G(
                "Quy luật nở vì nhiệt của các chất",
                F("So sánh mức độ nở vì nhiệt giữa 3 thể", "$\\Delta V_{\\text{khí}} > \\Delta V_{\\text{lỏng}} > \\Delta V_{\\text{rắn}}$", "Với cùng thể tích ban đầu và cùng độ tăng nhiệt độ $\\Delta t$."),
                F("Biến đổi thể tích và khối lượng riêng khi đun nóng", "$t \\text{ tăng} \\implies V \\text{ tăng},\\ m = \\text{const} \\implies D = \\dfrac{m}{V} \\text{ giảm}$", "Khi đun nóng một vật, khối lượng $m$ không đổi nhưng thể tích $V$ tăng nên khối lượng riêng $D$ giảm."),
            )
        ],
        example="Một băng kép gồm một thanh đồng và một thanh thép được tán chặt vào nhau. Biết đồng nở vì nhiệt nhiều hơn thép. Khi hơ nóng băng kép này trên ngọn lửa đèn cồn thì băng kép sẽ cong về phía thanh đồng hay thanh thép?",
        example_answer="Khi bị hơ nóng, cả hai thanh đều dài ra nhưng thanh đồng nở vì nhiệt nhiều hơn nên dài hơn thanh thép và nằm ở phía lưng vòng cung; do đó **băng kép bị uốn cong về phía thanh thép** (kim loại nở vì nhiệt ít hơn).",
        real_life="Giữa hai đầu thanh ray đường sắt hoặc giữa các nhịp cầu bê tông cốt thép luôn để một khe hở nhỏ (gối đỡ con lăn) để khi trời nắng nóng thanh ray và dầm cầu nở dài ra không bị kích cong vênh.",
        quiz=[
            mcq("biet", "Khi so sánh sự nở vì nhiệt của chất rắn, chất lỏng và chất khí (cùng thể tích ban đầu và cùng độ tăng nhiệt độ), nhận xét nào sau đây là đúng?", ["Chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn", "Chất rắn nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất khí", "Ba chất rắn, lỏng, khí nở vì nhiệt bằng nhau", "Chất lỏng nở vì nhiệt nhiều hơn chất khí"], 0, "Chất khí nở vì nhiệt nhiều nhất, tiếp đến là chất lỏng và ít nhất là chất rắn."),
            mcq("biet", "Khi nung nóng một quả cầu bằng kim loại đặc thì đại lượng nào của quả cầu **tăng lên** và đại lượng nào **giảm đi**?", ["Thể tích tăng lên và khối lượng riêng giảm đi", "Khối lượng tăng lên và thể tích giảm đi", "Khối lượng riêng tăng lên và thể tích giảm đi", "Cả khối lượng và thể tích đều giảm đi"], 0, "Khi nóng lên, quả cầu nở ra làm thể tích $V$ tăng, trong khi khối lượng $m$ không đổi nên khối lượng riêng $D = \\dfrac{m}{V}$ giảm đi."),
            mcq("hieu", "Vì sao khi đun nước, ta không nên đổ nước thật đầy tràn đến tận miệng ấm?", ["Vì khi đun nóng, nước nở vì nhiệt nhiều hơn ấm nhôm nên nước sẽ tràn ra ngoài làm tắt bếp hoặc gây bỏng", "Vì ấm nhôm nở vì nhiệt nhiều hơn nước", "Vì đổ đầy ấm làm nước không thể sôi được", "Vì nước khi nóng lên sẽ co lại"], 0, "Chất lỏng (nước) nở vì nhiệt nhiều hơn chất rắn (ấm nhôm), nên nếu đổ đầy tràn thì khi nóng lên nước sẽ trào ra khỏi ấm."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sự nở vì nhiệt:", [
                "Các chất khí khác nhau (như khí ôxi, khí nitơ, không khí) nở vì nhiệt giống nhau.",
                "Các chất rắn khác nhau (như nhôm, đồng, sắt) nở vì nhiệt khác nhau.",
                "Khi bị đốt nóng, băng kép gồm đồng và thép luôn cong về phía thanh đồng (chất nở vì nhiệt nhiều hơn).",
                "Chỗ tiếp nối hai đầu thanh ray đường sắt có để một khe hở nhỏ để tránh đường ray bị uốn cong khi trời nắng nóng.",
            ], [True, True, False, True], "Ý c) sai vì khi bị đốt nóng, thanh đồng dãn dài hơn sẽ bao phía ngoài và đẩy băng kép cong về phía thanh thép (chất nở vì nhiệt ít hơn)."),
            short("vandung", "Xét $3$ bình có cùng dung tích $1\\text{ lít}$ chứa đầy: (1) Rượu, (2) Không khí, (3) Khối sắt. Khi cùng tăng nhiệt độ thêm $30^\\circ\\text{C}$, chất trong bình số mấy (nhập 1, 2 hoặc 3) nở vì nhiệt nhiều nhất?", ["2"], "Chất khí (không khí ở bình số $2$) nở vì nhiệt nhiều hơn chất lỏng và chất rắn."),
        ],
        chapter_desc=CH4_DESC,
    ),
]


from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("physics", 8, _l)
    _l["game_type"] = _gt
    _l["game_title"] = _gtitle
    _l["game_description"] = _gdesc
