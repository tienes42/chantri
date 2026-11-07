"""Vật lý Lớp 9 (KHTN 9 - Kết nối tri thức với cuộc sống): 4 Chương - 16 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 9

CH1_TOPIC = "l9-ch01-nang-luong-co-hoc"
CH1_TITLE = "Chương I: Năng lượng cơ học"
CH1_DESC = "Chương I · Vật lý 9 (KHTN 9): Công, công suất, động năng, thế năng và cơ năng."

CH2_TOPIC = "l9-ch02-anh-sang-quang-hoc"
CH2_TITLE = "Chương II: Ánh sáng"
CH2_DESC = "Chương II · Vật lý 9 (KHTN 9): Khúc xạ ánh sáng, phản xạ toàn phần, tán sắc qua lăng kính, thấu kính và kính lúp."

CH3_TOPIC = "l9-ch03-dien-hoc-dinh-luat-ohm"
CH3_TITLE = "Chương III: Điện"
CH3_DESC = "Chương III · Vật lý 9 (KHTN 9): Điện trở, định luật Ohm, đoạn mạch nối tiếp – song song và công suất điện."

CH4_TOPIC = "l9-ch04-dien-tu-cam-ung"
CH4_TITLE = "Chương IV: Điện từ và Năng lượng trên Trái Đất"
CH4_DESC = "Chương IV · Vật lý 9 (KHTN 9): Cảm ứng điện từ, dòng điện xoay chiều, máy biến áp và các nguồn năng lượng."

LESSONS = [
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 1: Công và công suất",
        icon="🏗️",
        description="Điều kiện có công cơ học, công thức tính công A = F.s (J) và công suất P = A/t = F.v (W).",
        requirements=[
            "Nêu được điều kiện để lực sinh công cơ học và viết được công thức tính công khi lực cùng hướng dịch chuyển: $A = F \\cdot s$ (đơn vị Joule – $\\text{J}$).",
            "Nêu được ý nghĩa của công suất là tốc độ thực hiện công và viết công thức $\\mathcal{P} = \\dfrac{A}{t}$ (đơn vị Oát – $\\text{W}$).",
            "Vận dụng được các công thức $A = F \\cdot s$, $A = P \\cdot h$ và $\\mathcal{P} = \\dfrac{A}{t} = F \\cdot v$ để giải bài tập thực tế.",
        ],
        definition="Khi có lực $F$ không đổi tác dụng vào vật và làm vật dịch chuyển một quãng đường $s$ theo đúng hướng của lực thì công cơ học của lực đó là $A = F \\cdot s$ (đơn vị $\\text{J}$). Công suất là công thực hiện được trong một đơn vị thời gian: $\\mathcal{P} = \\dfrac{A}{t}$ (đơn vị $\\text{W}$).",
        theory=(
            "### 1. Công cơ học\n"
            "- Khi lực $\\vec{F}$ cùng hướng với độ dịch chuyển $s$: $A = F \\cdot s$.\n"
            "- Khi nâng đều một vật có trọng lượng $P$ lên độ cao $h$: $A = P \\cdot h = 10m \\cdot h$.\n"
            "- Đơn vị của công là **Joule** ($\\text{J}$), với $1\\text{ J} = 1\\text{ N}\\cdot\\text{m}$; $1\\text{ kJ} = 1000\\text{ J}$; $1\\text{ MJ} = 10^6\\text{ J}$.\n"
            "- Nếu có lực tác dụng nhưng vật đứng yên ($s = 0$) hoặc lực vuông góc với phương dịch chuyển thì công của lực bằng $0$ ($A = 0$).\n\n"
            "### 2. Công suất\n"
            "- Đặc trưng cho tốc độ sinh công nhanh hay chậm:\n"
            "  $$\\mathcal{P} = \\dfrac{A}{t} = \\dfrac{F \\cdot s}{t} = F \\cdot v$$\n"
            "- Đơn vị công suất trong hệ SI là **Oát** ($\\text{W}$), với $1\\text{ W} = 1\\text{ J/s}$; $1\\text{ kW} = 1000\\text{ W}$; $1\\text{ MW} = 10^6\\text{ W}$; $1\\text{ HP (mã lực)} \\approx 746\\text{ W}$."
        ),
        formulas=[
            G(
                "Công cơ học và Công suất",
                F("Công thức tính công cơ học", "$A = F \\cdot s \\quad (\\text{khi nâng đều lên độ cao } h: A = P \\cdot h)$", "Trong đó $F$ là lực tác dụng ($\\text{N}$), $s$ là quãng đường dịch chuyển theo phương của lực ($\\text{m}$), $A$ tính bằng $\\text{J}$."),
                F("Công thức tính công suất", "$\\mathcal{P} = \\dfrac{A}{t} = F \\cdot v$", "Trong đó $t$ là thời gian thực hiện công ($\\text{s}$), $v$ là tốc độ ($\\text{m/s}$), $\\mathcal{P}$ tính bằng $\\text{W}$ ($1\\text{ kW} = 1000\\text{ W}$)."),
            )
        ],
        example="Một cần cẩu nâng đều một kiện hàng có trọng lượng $P = 4000\\text{ N}$ lên độ cao $h = 6\\text{ m}$ trong thời gian $t = 12\\text{ s}$. Hãy tính công và công suất của lực nâng cần cẩu.",
        example_answer="Công của lực nâng là $A = P \\cdot h = 4000 \\cdot 6 = 24\\,000\\text{ J} = 24\\text{ kJ}$. Công suất của cần cẩu là $\\mathcal{P} = \\dfrac{A}{t} = \\dfrac{24\\,000}{12} = 2000\\text{ W} = 2\\text{ kW}$.",
        real_life="Thông số công suất ghi trên động cơ máy bơm nước, thang máy và ô tô (theo đơn vị $\\text{kW}$ hoặc mã lực $\\text{HP}$) cho biết khả năng thực hiện công nhanh hay chậm của máy.",
        quiz=[
            mcq("biet", "Khi lực không đổi $F$ tác dụng lên vật làm vật dịch chuyển một quãng đường $s$ theo đúng hướng của lực, công cơ học $A$ được tính bằng công thức nào?", ["$A = F \\cdot s$", "$A = \\dfrac{F}{s}$", "$A = \\dfrac{s}{F}$", "$A = F + s$"], 0, "Công cơ học khi lực cùng hướng dịch chuyển là $A = F \\cdot s$."),
            mcq("biet", "Đơn vị đo công suất trong hệ SI là gì?", ["Oát ($\\text{W}$)", "Joule ($\\text{J}$)", "Newton ($\\text{N}$)", "Pascal ($\\text{Pa}$)"], 0, "Công suất $\\mathcal{P} = \\dfrac{A}{t}$ có đơn vị trong hệ SI là Oát ($\\text{W}$, với $1\\text{ W} = 1\\text{ J/s}$)."),
            mcq("hieu", "Trong trường hợp nào dưới đây lực tác dụng lên vật **không** thực hiện công cơ học ($A = 0$)?", ["Một lực sĩ đang đứng yên giữ quả tạ ở trên cao", "Đầu tàu hỏa đang kéo các toa tàu chuyển động trên đường ray", "Một người đang kéo gầu nước từ dưới giếng lên", "Quả táo đang rơi từ trên cành cây xuống đất"], 0, "Khi giữ yên quả tạ, quãng đường dịch chuyển $s = 0$ nên công cơ học $A = F \\cdot 0 = 0$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về công và công suất:", [
                "Đơn vị $1\\text{ J}$ bằng $1\\text{ N}\\cdot\\text{m}$.",
                "Máy nào có công suất lớn hơn thì thực hiện cùng một công trong thời gian ngắn hơn.",
                "Trọng lực tác dụng lên hòn bi đang lăn trên mặt bàn nằm ngang thực hiện một công dương rất lớn.",
                "Một lực kéo $50\\text{ N}$ làm vật đi được $4\\text{ m}$ theo hướng của lực trong $5\\text{ s}$ thì có công là $200\\text{ J}$ và công suất là $40\\text{ W}$.",
            ], [True, True, False, True], "Ý c) sai vì trọng lực có phương thẳng đứng vuông góc với mặt bàn nằm ngang nên không sinh công khi bi lăn ngang."),
            short("vandung", "Một người kéo đều một thùng nước nặng $P = 150\\text{ N}$ từ dưới giếng sâu $h = 8\\text{ m}$ lên trong thời gian $t = 20\\text{ s}$. Công suất của người kéo bằng bao nhiêu Oát ($\\text{W}$)?", ["60"], "Công thực hiện là $A = P \\cdot h = 150 \\cdot 8 = 1200\\text{ J}$. Công suất là $\\mathcal{P} = \\dfrac{1200}{20} = 60\\text{ W}$.", unit="W"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 2: Động năng. Thế năng. Cơ năng",
        icon="🎢",
        description="Công thức động năng W_đ = ½mv², thế năng trọng trường W_t = P.h = mgh, cơ năng W = W_đ + W_t và sự chuyển hóa cơ năng.",
        requirements=[
            "Viết và vận dụng được công thức tính động năng của vật chuyển động: $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$.",
            "Viết và vận dụng được công thức tính thế năng trọng trường của vật ở độ cao $h$ so với mốc thế năng: $W_{\\text{t}} = P \\cdot h = mgh$.",
            "Phân tích được sự chuyển hóa qua lại giữa động năng và thế năng và vận dụng bảo toàn cơ năng $W = W_{\\text{đ}} + W_{\\text{t}}$ khi bỏ qua ma sát.",
        ],
        definition="Cơ năng của một vật bằng tổng động năng và thế năng của nó: $W = W_{\\text{đ}} + W_{\\text{t}} = \\dfrac{1}{2}mv^2 + P \\cdot h$. Khi vật chuyển động chỉ dưới tác dụng của trọng lực (bỏ qua ma sát và sức cản), động năng và thế năng chuyển hóa qua lại nhưng cơ năng được bảo toàn.",
        theory=(
            "### 1. Động năng và Thế năng trọng trường\n"
            "- **Động năng ($W_{\\text{đ}}$)**: năng lượng vật có được do chuyển động:\n"
            "  $$W_{\\text{đ}} = \\dfrac{1}{2}mv^2$$\n"
            "  trong đó $m$ là khối lượng ($\\text{kg}$), $v$ là tốc độ của vật ($\\text{m/s}$), $W_{\\text{đ}}$ tính bằng Joule ($\\text{J}$).\n"
            "- **Thế năng trọng trường ($W_{\\text{t}}$)**: năng lượng vật có được khi ở độ cao $h$ so với vị trí chọn làm mốc thế năng (thường chọn mặt đất):\n"
            "  $$W_{\\text{t}} = P \\cdot h = mgh \\approx 10m \\cdot h$$\n\n"
            "### 2. Cơ năng và sự chuyển hóa cơ năng\n"
            "- **Cơ năng**: $W = W_{\\text{đ}} + W_{\\text{t}}$.\n"
            "- Khi vật rơi từ trên cao xuống: độ cao $h$ giảm nên **thế năng giảm**, tốc độ $v$ tăng nên **động năng tăng** (thế năng chuyển hóa thành động năng).\n"
            "- Khi ném vật thẳng đứng lên cao: **động năng giảm**, **thế năng tăng**. Nếu bỏ qua sức cản không khí thì $W_1 = W_2 = \\text{const}$."
        ),
        formulas=[
            G(
                "Động năng, Thế năng và Cơ năng",
                F("Công thức tính động năng", "$W_{\\text{đ}} = \\dfrac{1}{2}mv^2$", "Trong đó $m$ tính bằng $\\text{kg}$, $v$ tính bằng $\\text{m/s}$, $W_{\\text{đ}}$ tính bằng $\\text{J}$. Nếu tốc độ $v$ tăng gấp $2$ lần thì động năng tăng gấp $4$ lần."),
                F("Thế năng trọng trường và Cơ năng", "$W_{\\text{t}} = P \\cdot h = 10mh; \\qquad W = W_{\\text{đ}} + W_{\\text{t}} = \\dfrac{1}{2}mv^2 + P \\cdot h$", "Khi bỏ qua ma sát/lực cản: $W_{\\text{đ}1} + W_{\\text{t}1} = W_{\\text{đ}2} + W_{\\text{t}2}$."),
            )
        ],
        example="Một vật có khối lượng $m = 2\\text{ kg}$ đang bay ở độ cao $h = 5\\text{ m}$ so với mặt đất với tốc độ $v = 6\\text{ m/s}$ (lấy $P = 10m$, chọn mặt đất làm mốc thế năng). Hãy tính động năng, thế năng và cơ năng của vật.",
        example_answer="Động năng của vật là $W_{\\text{đ}} = \\dfrac{1}{2}mv^2 = \\dfrac{1}{2} \\cdot 2 \\cdot 6^2 = 36\\text{ J}$. Thế năng trọng trường là $W_{\\text{t}} = 10mh = 10 \\cdot 2 \\cdot 5 = 100\\text{ J}$. Cơ năng của vật là $W = W_{\\text{đ}} + W_{\\text{t}} = 36 + 100 = 136\\text{ J}$.",
        real_life="Nhà máy thủy điện tích nước trong hồ chứa ở trên cao để tạo thế năng trọng trường rất lớn, sau đó xả nước chảy qua ống dẫn xuống dưới làm chuyển hóa thế năng thành động năng quay tua-bin phát điện.",
        quiz=[
            mcq("biet", "Công thức tính động năng $W_{\\text{đ}}$ của một vật có khối lượng $m$ đang chuyển động với tốc độ $v$ là gì?", ["$W_{\\text{đ}} = \\dfrac{1}{2}mv^2$", "$W_{\\text{đ}} = mv^2$", "$W_{\\text{đ}} = \\dfrac{1}{2}mv$", "$W_{\\text{đ}} = 2mv^2$"], 0, "Động năng của vật được tính theo công thức $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$."),
            mcq("biet", "Khi một quả bóng đang rơi từ trên cao xuống mặt đất, có sự chuyển hóa năng lượng như thế nào?", ["Thế năng trọng trường giảm dần và chuyển hóa thành động năng tăng dần", "Động năng giảm dần và chuyển hóa thành thế năng tăng dần", "Cả động năng và thế năng đều tăng dần", "Cả động năng và thế năng đều bằng $0$"], 0, "Khi rơi xuống, độ cao $h$ giảm nên thế năng giảm, tốc độ $v$ tăng nên động năng tăng."),
            mcq("hieu", "Nếu khối lượng của ô tô không đổi nhưng tốc độ của ô tô tăng lên gấp $2$ lần thì động năng của ô tô tăng lên gấp mấy lần?", ["Tăng gấp $4$ lần", "Tăng gấp $2$ lần", "Tăng gấp $8$ lần", "Không thay đổi"], 0, "Vì $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$ tỉ lệ với bình phương tốc độ $v^2$, nên khi $v$ tăng gấp $2$ lần thì $W_{\\text{đ}}$ tăng $2^2 = 4$ lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về động năng, thế năng và cơ năng:", [
                "Chọn mặt đất làm mốc thế năng thì vật nằm yên trên mặt đất có thế năng trọng trường bằng $0$.",
                "Đơn vị của động năng, thế năng và cơ năng trong hệ SI đều là Joule ($\\text{J}$).",
                "Khi ném một hòn đá thẳng đứng lên cao, động năng của hòn đá đạt cực đại ở điểm cao nhất.",
                "Một vật có khối lượng $m = 4\\text{ kg}$ chuyển động với tốc độ $v = 5\\text{ m/s}$ có động năng bằng $50\\text{ J}$.",
            ], [True, True, False, True], "Ý c) sai vì ở điểm cao nhất vận tốc tức thời của hòn đá bằng $0$ nên động năng bằng $0$ và thế năng đạt cực đại."),
            short("vandung", "Một viên bi sắt có khối lượng $m = 0{,}5\\text{ kg}$ được thả rơi từ độ cao $h = 4\\text{ m}$ so với mặt đất (lấy $P = 10m$, bỏ qua sức cản không khí). Cơ năng của viên bi ngay khi chạm mặt đất bằng bao nhiêu Joule ($\\text{J}$)?", ["20"], "Theo định luật bảo toàn cơ năng, cơ năng lúc chạm đất bằng thế năng ở đỉnh dốc ban đầu: $W = P \\cdot h = 10 \\cdot 0{,}5 \\cdot 4 = 20\\text{ J}$.", unit="J"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 3: Khúc xạ ánh sáng",
        icon="🥤",
        description="Hiện tượng khúc xạ ánh sáng, chiết suất của môi trường n = c/v và định luật khúc xạ ánh sáng n₁.sin i = n₂.sin r.",
        requirements=[
            "Mô tả được hiện tượng khúc xạ ánh sáng là hiện tượng tia sáng bị gãy khúc tại mặt phân cách khi truyền xiên góc từ môi trường trong suốt này sang môi trường trong suốt khác.",
            "Nêu được chiết suất của môi trường $n = \\dfrac{c}{v} \\ge 1$ đặc trưng cho tốc độ truyền ánh sáng trong môi trường đó.",
            "Vận dụng được biểu thức định luật khúc xạ ánh sáng $n_1 \\sin i = n_2 \\sin r$ để tính góc tới hoặc góc khúc xạ.",
        ],
        definition="Khúc xạ ánh sáng là hiện tượng tia sáng truyền từ môi trường trong suốt này sang môi trường trong suốt khác bị gãy khúc tại mặt phân cách giữa hai môi trường. Định luật khúc xạ ánh sáng được biểu diễn bởi hệ thức: $n_1 \\sin i = n_2 \\sin r$.",
        theory=(
            "### 1. Hiện tượng khúc xạ và Chiết suất của môi trường\n"
            "- **Chiết suất tuyệt đối ($n$)** của một môi trường bằng tỉ số giữa tốc độ ánh sáng trong chân không ($c \\approx 3 \\cdot 10^8\\text{ m/s}$) và tốc độ ánh sáng trong môi trường đó ($v$): $n = \\dfrac{c}{v} \\ge 1$ (không khí có $n \\approx 1$, nước $n \\approx \\dfrac{4}{3} \\approx 1{,}33$, thủy tinh $n \\approx 1{,}5$).\n\n"
            "### 2. Định luật khúc xạ ánh sáng\n"
            "- Tia khúc xạ nằm trong mặt phẳng tới (tạo bởi tia tới $SI$ và pháp tuyến $NN'$) và ở phía bên kia pháp tuyến so với tia tới.\n"
            "- Hệ thức liên hệ giữa góc tới $i$ và góc khúc xạ $r$:\n"
            "  $$n_1 \\sin i = n_2 \\sin r \\iff \\dfrac{\\sin i}{\\sin r} = \\dfrac{n_2}{n_1} = n_{21}$$\n"
            "- Hệ quả:\n"
            "  - Nếu truyền từ môi trường chiết suất nhỏ sang môi trường chiết suất lớn hơn ($n_1 < n_2$, ví dụ từ không khí vào nước): **góc khúc xạ nhỏ hơn góc tới ($r < i$)**.\n"
            "  - Nếu truyền từ môi trường chiết suất lớn sang môi trường chiết suất nhỏ hơn ($n_1 > n_2$, ví dụ từ nước ra không khí): **góc khúc xạ lớn hơn góc tới ($r > i$)**.\n"
            "  - Nếu tia sáng vuông góc với mặt phân cách ($i = 0^\\circ$) thì tia sáng truyền thẳng ($r = 0^\\circ$)."
        ),
        formulas=[
            G(
                "Chiết suất và Định luật khúc xạ ánh sáng",
                F("Chiết suất của môi trường trong suốt", "$n = \\dfrac{c}{v} \\ge 1 \\quad (c = 3 \\cdot 10^8\\text{ m/s})$", "Môi trường có chiết suất $n$ càng lớn thì tốc độ truyền ánh sáng $v$ trong môi trường đó càng nhỏ."),
                F("Hệ thức Định luật khúc xạ ánh sáng", "$n_1 \\sin i = n_2 \\sin r \\implies \\sin r = \\dfrac{n_1 \\sin i}{n_2}$", "Nếu $n_2 > n_1$ thì $r < i$; nếu $n_2 < n_1$ thì $r > i$; nếu $i = 0^\\circ$ thì $r = 0^\\circ$."),
            )
        ],
        example="Chiếu một tia sáng từ không khí ($n_1 = 1$) vào mặt nước có chiết suất $n_2 = \\sqrt{2}$ dưới góc tới $i = 45^\\circ$. Hãy tính góc khúc xạ $r$ của tia sáng trong nước.",
        example_answer="Áp dụng định luật khúc xạ ánh sáng: $n_1 \\sin i = n_2 \\sin r \\implies 1 \\cdot \\sin 45^\\circ = \\sqrt{2} \\cdot \\sin r$. Vì $\\sin 45^\\circ = \\dfrac{\\sqrt{2}}{2}$ nên $\\sin r = \\dfrac{1}{2} = 0{,}5 \\implies r = 30^\\circ$.",
        real_life="Khi cắm nghiêng một chiếc đũa hoặc ống hút vào cốc nước trong suốt, ta thấy chiếc đũa như bị gãy khúc tại mặt nước và đáy bể bơi nhìn từ trên bờ có vẻ nông hơn độ sâu thực tế do hiện tượng khúc xạ ánh sáng.",
        quiz=[
            mcq("biet", "Biểu thức nào sau đây thể hiện đúng Định luật khúc xạ ánh sáng khi tia sáng truyền từ môi trường chiết suất $n_1$ sang môi trường chiết suất $n_2$?", ["$n_1 \\sin i = n_2 \\sin r$", "$n_1 \\sin r = n_2 \\sin i$", "$\\dfrac{n_1}{\\sin i} = \\dfrac{n_2}{\\sin r}$", "$n_1 \\cdot i = n_2 \\cdot r$"], 0, "Theo định luật khúc xạ ánh sáng: $n_1 \\sin i = n_2 \\sin r$."),
            mcq("biet", "Khi một tia sáng truyền xiên góc từ không khí ($n_1 = 1$) vào trong nước ($n_2 = 1{,}33$) thì quan hệ giữa góc khúc xạ $r$ và góc tới $i$ là gì?", ["Góc khúc xạ nhỏ hơn góc tới ($r < i$)", "Góc khúc xạ lớn hơn góc tới ($r > i$)", "Góc khúc xạ bằng góc tới ($r = i$)", "Góc khúc xạ luôn bằng $90^\\circ$"], 0, "Vì $n_2 > n_1$ nên $\\sin r < \\sin i \\implies r < i$ (tia khúc xạ lệch lại gần pháp tuyến hơn)."),
            mcq("hieu", "Chiếu một tia sáng đi từ không khí vuông góc với mặt phẳng của một khối thủy tinh ($i = 0^\\circ$). Khi đi vào khối thủy tinh, tia sáng sẽ truyền như thế nào?", ["Truyền thẳng không bị đổi hướng ($r = 0^\\circ$)", "Bị gãy khúc một góc $45^\\circ$", "Bị gãy khúc một góc $90^\\circ$", "Không thể đi vào thủy tinh"], 0, "Khi $i = 0^\\circ$ thì $\\sin r = \\dfrac{n_1 \\sin 0^\\circ}{n_2} = 0 \\implies r = 0^\\circ$, tia sáng tiếp tục truyền thẳng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về khúc xạ ánh sáng:", [
                "Chiết suất của chân không bằng $1$ và chiết suất của không khí xấp xỉ bằng $1$.",
                "Khi tia sáng truyền xiên góc từ nước ($n_1 = 1{,}33$) ra không khí ($n_2 = 1$), góc khúc xạ lớn hơn góc tới ($r > i$).",
                "Tốc độ ánh sáng truyền trong thủy tinh ($n = 1{,}5$) lớn hơn tốc độ ánh sáng truyền trong chân không.",
                "Hiện tượng đáy chậu nước nhìn có vẻ nâng cao hơn thực tế là do sự khúc xạ của các tia sáng đi từ đáy chậu qua mặt nước tới mắt.",
            ], [True, True, False, True], "Ý c) sai vì $v = \\dfrac{c}{n} = \\dfrac{c}{1{,}5} < c$, ánh sáng truyền trong thủy tinh chậm hơn trong chân không."),
            short("vandung", "Biết tốc độ ánh sáng trong chân không là $c = 300\\,000\\text{ km/s}$. Trong một khối thủy tinh có chiết suất $n = 1{,}5$, tốc độ truyền ánh sáng bằng bao nhiêu nghìn $\\text{km/s}$ (nhập số theo đơn vị nghìn km/s, ví dụ 200)?", ["200"], "Ta có $v = \\dfrac{c}{n} = \\dfrac{300\\,000}{1{,}5} = 200\\,000\\text{ km/s} = 200\\text{ nghìn km/s}$.", unit="nghìn km/s"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 4: Phản xạ toàn phần",
        icon="🌐",
        description="Điều kiện xảy ra hiện tượng phản xạ toàn phần, góc giới hạn sin(i_gh) = n₂/n₁ và ứng dụng cáp quang.",
        requirements=[
            "Nêu được hiện tượng phản xạ toàn phần là hiện tượng phản xạ lại toàn bộ ánh sáng tới tại mặt phân cách giữa hai môi trường trong suốt (không còn tia khúc xạ).",
            "Trình bày được 2 điều kiện cần và đủ để có phản xạ toàn phần: ánh sáng truyền từ môi trường chiết suất lớn sang môi trường chiết suất nhỏ hơn ($n_1 > n_2$) và góc tới $i \\ge i_{\\text{gh}}$ với $\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1}$.",
            "Giải thích được nguyên lý truyền tín hiệu ánh sáng trong sợi quang (cáp quang) trong viễn thông và nội soi y học.",
        ],
        definition="Phản xạ toàn phần là hiện tượng toàn bộ tia sáng tới bị phản xạ trở lại môi trường cũ tại mặt phân cách giữa hai môi trường trong suốt (không còn tia khúc xạ). Hiện tượng này xảy ra khi ánh sáng truyền từ môi trường chiết suất lớn sang môi trường chiết suất nhỏ hơn ($n_1 > n_2$) với góc tới $i \\ge i_{\\text{gh}}$, trong đó $\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1}$.",
        theory=(
            "### 1. Góc giới hạn và hai điều kiện phản xạ toàn phần\n"
            "- Khi tia sáng truyền từ môi trường có chiết suất lớn $n_1$ sang môi trường có chiết suất nhỏ $n_2$ ($n_1 > n_2$), góc khúc xạ $r > i$.\n"
            "- Khi góc tới đạt giá trị **góc giới hạn $i_{\\text{gh}}$** thì góc khúc xạ $r = 90^\\circ$ (tia khúc xạ đi sát mặt phân cách):\n"
            "  $$\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1}$$\n"
            "- **Hai điều kiện để xảy ra phản xạ toàn phần**:\n"
            "  1. Ánh sáng truyền từ môi trường chiết suất lớn sang môi trường chiết suất nhỏ hơn: $n_1 > n_2$.\n"
            "  2. Góc tới lớn hơn hoặc bằng góc giới hạn: $i \\ge i_{\\text{gh}}$.\n\n"
            "### 2. Ứng dụng của phản xạ toàn phần\n"
            "- **Cáp quang (sợi quang)**: gồm phần lõi trong suốt bằng thủy tinh siêu tinh khiết có chiết suất $n_1$ lớn và phần vỏ bọc có chiết suất $n_2 < n_1$. Tia sáng truyền trong lõi liên tục bị phản xạ toàn phần để truyền internet tốc độ cao hoặc dùng trong ống nội soi y học."
        ),
        formulas=[
            G(
                "Góc giới hạn và Điều kiện phản xạ toàn phần",
                F("Công thức tính góc giới hạn phản xạ toàn phần", "$\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1} \\quad (\\text{với } n_1 > n_2)$", "Nếu môi trường thứ hai là không khí ($n_2 = 1$) thì $\\sin i_{\\text{gh}} = \\dfrac{1}{n_1}$."),
                F("Điều kiện xảy ra phản xạ toàn phần", "$\\begin{cases} n_1 > n_2 \\\\ i \\ge i_{\\text{gh}} \\end{cases}$", "Khi xảy ra phản xạ toàn phần, không còn tia khúc xạ và tia phản xạ tuân theo định luật phản xạ $i' = i$."),
            )
        ],
        example="Một khối thủy tinh trong suốt có chiết suất $n_1 = 2$ đặt trong không khí ($n_2 = 1$). Hãy tính góc giới hạn phản xạ toàn phần $i_{\\text{gh}}$ khi chiếu tia sáng từ trong khối thủy tinh ra không khí.",
        example_answer="Áp dụng công thức $\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1} = \\dfrac{1}{2} = 0{,}5$. Suy ra góc giới hạn phản xạ toàn phần là $i_{\\text{gh}} = 30^\\circ$.",
        real_life="Cáp quang biển truyền dữ liệu internet xuyên đại dương và ống nội soi dạ dày trong bệnh viện đều hoạt động nhờ hiện tượng phản xạ toàn phần trong sợi quang.",
        quiz=[
            mcq("biet", "Công thức tính góc giới hạn phản xạ toàn phần $i_{\\text{gh}}$ khi ánh sáng truyền từ môi trường có chiết suất $n_1$ sang môi trường có chiết suất $n_2$ ($n_1 > n_2$) là gì?", ["$\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1}$", "$\\sin i_{\\text{gh}} = \\dfrac{n_1}{n_2}$", "$\\sin i_{\\text{gh}} = n_1 \\cdot n_2$", "$\\sin i_{\\text{gh}} = n_1 - n_2$"], 0, "Khi $r = 90^\\circ$ thì $n_1 \\sin i_{\\text{gh}} = n_2 \\sin 90^\\circ = n_2 \\implies \\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1}$."),
            mcq("biet", "Hiện tượng phản xạ toàn phần **chỉ** có thể xảy ra khi ánh sáng truyền theo chiều nào sau đây?", ["Truyền từ môi trường có chiết suất lớn sang môi trường có chiết suất nhỏ hơn ($n_1 > n_2$)", "Truyền từ không khí ($n = 1$) vào trong nước ($n = 1{,}33$)", "Truyền từ không khí ($n = 1$) vào kim cương ($n = 2{,}42$)", "Truyền vuông góc với mặt phân cách giữa hai môi trường"], 0, "Điều kiện cần đầu tiên của phản xạ toàn phần là ánh sáng phải truyền từ môi trường chiết suất lớn sang môi trường chiết suất nhỏ hơn ($n_1 > n_2$)."),
            mcq("hieu", "Trong cấu tạo của sợi quang học (cáp quang), chiết suất của phần lõi ($n_1$) và chiết suất của phần vỏ bọc ($n_2$) phải thỏa mãn điều kiện nào?", ["$n_1 > n_2$ để tia sáng truyền trong lõi bị phản xạ toàn phần tại mặt tiếp giáp lõi – vỏ", "$n_1 < n_2$ để tia sáng truyền ra ngoài vỏ", "$n_1 = n_2$ để tia sáng truyền thẳng ra ngoài", "$n_1 = 0$"], 0, "Lõi sợi quang phải có chiết suất $n_1$ lớn hơn chiết suất vỏ $n_2$ để tia sáng bị phản xạ toàn phần liên tiếp bên trong lõi."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phản xạ toàn phần:", [
                "Khi chiếu tia sáng từ không khí vào nước, dù tăng góc tới lớn đến đâu cũng không bao giờ xảy ra phản xạ toàn phần.",
                "Khi góc tới $i$ lớn hơn hoặc bằng góc giới hạn $i_{\\text{gh}}$ (với $n_1 > n_2$), tia khúc xạ biến mất hoàn toàn.",
                "Kim cương ($n = 2{,}42$) lấp lánh rực rỡ vì có chiết suất rất lớn nên góc giới hạn phản xạ toàn phần rất nhỏ ($\\approx 24{,}4^\\circ$).",
                "Trong cáp quang, tín hiệu được truyền đi bằng dòng điện một chiều chạy trong lõi đồng.",
            ], [True, True, True, False], "Ý d) sai vì cáp quang truyền tín hiệu bằng các xung ánh sáng phản xạ toàn phần trong sợi thủy tinh hoặc nhựa trong suốt."),
            short("vandung", "Chiếu một tia sáng từ một chất lỏng có chiết suất $n_1 = \\sqrt{2}$ ra ngoài không khí ($n_2 = 1$). Góc giới hạn phản xạ toàn phần $i_{\\text{gh}}$ bằng bao nhiêu độ?", ["45"], "Ta có $\\sin i_{\\text{gh}} = \\dfrac{n_2}{n_1} = \\dfrac{1}{\\sqrt{2}} = \\dfrac{\\sqrt{2}}{2} \\implies i_{\\text{gh}} = 45^\\circ$.", unit="độ"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 5: Tán sắc ánh sáng qua lăng kính. Màu sắc các vật",
        icon="🌈",
        description="Sự khúc xạ và tán sắc ánh sáng trắng qua lăng kính (7 màu từ đỏ đến tím), ánh sáng đơn sắc và màu sắc các vật.",
        requirements=[
            "Mô tả được lăng kính phân tích chùm ánh sáng trắng (như ánh sáng Mặt Trời) thành một dải màu biến thiên liên tục từ đỏ đến tím (đỏ, da cam, vàng, lục, lam, chàm, tím) gọi là hiện tượng tán sắc ánh sáng.",
            "Nêu được tia đỏ bị lệch ít nhất và tia tím bị lệch nhiều nhất khi đi qua lăng kính; ánh sáng đơn sắc không bị tán sắc khi qua lăng kính.",
            "Giải thích được màu sắc của các vật dưới ánh sáng trắng và dưới ánh sáng màu dựa vào khả năng phản xạ (tán xạ) và hấp thụ ánh sáng màu.",
        ],
        definition="Hiện tượng chùm ánh sáng trắng khi đi qua lăng kính bị phân tách thành nhiều chùm sáng màu khác nhau (biến thiên liên tục từ đỏ, da cam, vàng, lục, lam, chàm đến tím) được gọi là sự tán sắc ánh sáng.",
        theory=(
            "### 1. Tán sắc ánh sáng qua lăng kính\n"
            "- **Lăng kính** là một khối chất trong suốt (thủy tinh, nhựa) hình lăng trụ tam giác. Tia sáng qua lăng kính luôn bị khúc xạ **lệch về phía đáy** của lăng kính.\n"
            "- **Ánh sáng đơn sắc**: ánh sáng có một màu nhất định và **không bị tán sắc** (không đổi màu) khi truyền qua lăng kính.\n"
            "- **Ánh sáng trắng** là tập hợp của vô số ánh sáng đơn sắc có màu biến thiên liên tục từ **Đỏ $\\to$ Da cam $\\to$ Vàng $\\to$ Lục $\\to$ Lam $\\to$ Chàm $\\to$ Tím**.\n"
            "- Chiết suất của thủy tinh đối với các ánh sáng đơn sắc khác nhau là khác nhau ($n_{\\text{đỏ}} < n_{\\text{cam}} < \\dots < n_{\\text{tím}}$), nên qua lăng kính **tia đỏ lệch ít nhất** và **tia tím lệch nhiều nhất**.\n\n"
            "### 2. Màu sắc các vật\n"
            "- Dưới ánh sáng trắng: **vật màu nào thì tán xạ (phản xạ) mạnh ánh sáng màu đó** và hấp thụ các ánh sáng màu còn lại.\n"
            "- **Vật màu trắng** tán xạ tốt tất cả các ánh sáng màu; **vật màu đen** hấp thụ hầu hết tất cả các ánh sáng màu."
        ),
        formulas=[
            G(
                "Quy luật tán sắc qua lăng kính và màu sắc các vật",
                F("Thứ tự chiết suất và góc lệch qua lăng kính", "$n_{\\text{đỏ}} < n_{\\text{da cam}} < n_{\\text{vàng}} < n_{\\text{lục}} < n_{\\text{lam}} < n_{\\text{chàm}} < n_{\\text{tím}} \\implies D_{\\text{đỏ}} < D_{\\text{tím}}$", "Qua lăng kính, tia đỏ lệch về phía đáy ít nhất, tia tím lệch về phía đáy nhiều nhất."),
                F("Quy tắc nhìn thấy màu sắc của vật", "$\\text{Vật màu } X \\implies \\text{Tán xạ mạnh ánh sáng màu } X \\text{ và hấp thụ các màu khác}$", "Ví dụ: chiếc lá màu lục dưới ánh sáng đỏ sẽ hấp thụ ánh sáng đỏ nên nhìn thấy có màu đen."),
            )
        ],
        example="Trong một căn phòng tối chỉ bật một ngọn đèn phát ra ánh sáng đơn sắc màu đỏ. Khi chiếu ánh sáng đỏ này vào một tờ giấy trắng và một chiếc lá cây màu lục thì mắt ta sẽ nhìn thấy tờ giấy và chiếc lá có màu gì?",
        example_answer="Tờ giấy trắng phản xạ tốt mọi ánh sáng màu nên phản xạ ánh sáng đỏ tới mắt, ta thấy **tờ giấy có màu đỏ**. Chiếc lá màu lục chỉ phản xạ ánh sáng lục và hấp thụ ánh sáng đỏ, nên không có ánh sáng từ lá truyền tới mắt, ta thấy **chiếc lá có màu đen (tối sẫm)**.",
        real_life="Cầu vồng xuất hiện trên bầu trời sau cơn mưa là do ánh sáng trắng của Mặt Trời bị khúc xạ, phản xạ và tán sắc qua vô số hạt nước mưa nhỏ li ti trong không khí.",
        quiz=[
            mcq("biet", "Khi chiếu một chùm tia sáng trắng hẹp đi qua một lăng kính thủy tinh, tia sáng màu nào bị lệch về phía đáy lăng kính **ít nhất** và tia màu nào bị lệch **nhiều nhất**?", ["Tia đỏ lệch ít nhất, tia tím lệch nhiều nhất", "Tia tím lệch ít nhất, tia đỏ lệch nhiều nhất", "Tia lục lệch ít nhất, tia vàng lệch nhiều nhất", "Tất cả các tia màu đều lệch một góc bằng nhau"], 0, "Vì chiết suất của thủy tinh đối với ánh sáng đỏ là nhỏ nhất và đối với ánh sáng tím là lớn nhất nên tia đỏ lệch ít nhất, tia tím lệch nhiều nhất."),
            mcq("biet", "Vì sao dưới ánh nắng Mặt Trời (ánh sáng trắng), ta nhìn thấy bông hoa hồng có màu đỏ?", ["Vì cánh hoa hồng tán xạ (phản xạ) mạnh ánh sáng màu đỏ truyền vào mắt ta và hấp thụ các ánh sáng màu khác", "Vì cánh hoa hồng tự phát ra ánh sáng màu đỏ trong bóng tối", "Vì cánh hoa hồng hấp thụ hết ánh sáng màu đỏ và phản xạ ánh sáng màu tím", "Vì mắt người tự phát ra tia màu đỏ chiếu vào bông hoa"], 0, "Vật có màu đỏ vì nó tán xạ mạnh ánh sáng màu đỏ trong chùm sáng trắng tới mắt và hấp thụ các màu còn lại."),
            mcq("hieu", "Chiếu một chùm tia laser màu lục (ánh sáng đơn sắc) đi qua một lăng kính thủy tinh thì chùm tia ló ra khỏi lăng kính có đặc điểm gì?", ["Bị lệch về phía đáy lăng kính nhưng vẫn chỉ có một màu lục (không bị tán sắc)", "Bị tách thành $7$ màu cầu vồng", "Đổi thành màu đỏ", "Truyền thẳng không bị lệch hướng"], 0, "Ánh sáng đơn sắc khi đi qua lăng kính chỉ bị khúc xạ lệch về phía đáy chứ không bị tán sắc (không đổi màu)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tán sắc ánh sáng và màu sắc các vật:", [
                "Dải màu chính trong quang phổ của ánh sáng trắng gồm 7 màu cơ bản: đỏ, da cam, vàng, lục, lam, chàm, tím.",
                "Vật màu đen hấp thụ hầu hết tất cả các ánh sáng màu chiếu tới nó.",
                "Nếu chiếu ánh sáng đơn sắc màu lam vào một quả cà chua chín màu đỏ thì ta nhìn thấy quả cà chua có màu gần như đen.",
                "Chiết suất của thủy tinh đối với các ánh sáng đơn sắc màu khác nhau đều bằng nhau.",
            ], [True, True, True, False], "Ý d) sai vì chiết suất của môi trường phụ thuộc màu sắc ánh sáng ($n_{\\text{đỏ}} < n_{\\text{tím}}$), đó chính là nguyên nhân gây ra sự tán sắc."),
            short("vandung", "Dải màu quang phổ chính của ánh sáng Mặt Trời khi tán sắc qua lăng kính thường được chia thành mấy màu cơ bản (đỏ, da cam, vàng, lục, lam, chàm, tím)?", ["7"], "Phổ ánh sáng trắng qua lăng kính gồm $7$ màu cơ bản: đỏ, da cam, vàng, lục, lam, chàm, tím."),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 6: Thấu kính hội tụ và thấu kính phân kì",
        icon="🔍",
        description="Phân biệt thấu kính hội tụ (rìa mỏng) và thấu kính phân kì (rìa dày), trục chính, quang tâm O, tiêu điểm F và tiêu cự f.",
        requirements=[
            "Phân biệt được thấu kính hội tụ (phần rìa mỏng hơn phần giữa, biến chùm tia tới song song thành chùm tia ló hội tụ) và thấu kính phân kì (phần rìa dày hơn phần giữa, biến chùm tia tới song song thành chùm tia ló phân kì).",
            "Xác định được trục chính $\\Delta$, quang tâm $O$, tiêu điểm chính $F, F'$ và tiêu cự $f = OF = OF'$ của thấu kính.",
            "Vẽ được đường truyền của các tia sáng đặc biệt qua thấu kính hội tụ và thấu kính phân kì.",
        ],
        definition="Thấu kính là một khối chất trong suốt giới hạn bởi hai mặt cong (hoặc một mặt cong và một mặt phẳng). Thấu kính hội tụ có phần rìa mỏng hơn phần giữa; thấu kính phân kì có phần rìa dày hơn phần giữa.",
        theory=(
            "### 1. Phân loại và các yếu tố của thấu kính\n"
            "- **Thấu kính hội tụ (thấu kính rìa mỏng)**: Chiếu chùm tia tới song song với trục chính thì chùm tia ló **hội tụ** tại tiêu điểm chính $F'$ ở phía bên kia thấu kính.\n"
            "- **Thấu kính phân kì (thấu kính rìa dày)**: Chiếu chùm tia tới song song với trục chính thì chùm tia ló **phân kì**, có đường kéo dài cắt nhau tại tiêu điểm chính $F'$ nằm cùng phía với tia tới.\n"
            "- **Quang tâm $O$**: điểm chính giữa của thấu kính mà mọi tia sáng đi qua đều truyền thẳng.\n"
            "- **Tiêu cự $f$**: khoảng cách từ quang tâm đến tiêu điểm chính: $f = OF = OF'$.\n\n"
            "### 2. Đường truyền của các tia sáng đặc biệt\n"
            "1. **Tia tới qua quang tâm $O$**: tia ló tiếp tục **truyền thẳng** không đổi hướng.\n"
            "2. **Tia tới song song với trục chính $\\Delta$**:\n"
            "   - Với thấu kính hội tụ: tia ló **đi qua tiêu điểm $F'$**.\n"
            "   - Với thấu kính phân kì: tia ló có **đường kéo dài đi qua tiêu điểm $F'$**.\n"
            "3. **Tia tới đi qua tiêu điểm $F$ (với TKHT)**: tia ló **song song với trục chính**."
        ),
        formulas=[
            G(
                "Tiêu cự và đường truyền tia sáng qua thấu kính",
                F("Tiêu cự của thấu kính", "$f = OF = OF'$", "Hai tiêu điểm chính $F$ và $F'$ nằm trên trục chính $\\Delta$ và đối xứng nhau qua quang tâm $O$."),
                F("Độ tụ của thấu kính (mở rộng)", "$D = \\pm \\dfrac{1}{f(\\text{m})} \\quad (\\text{đơn vị điốp } \\text{dp})$", "Thấu kính hội tụ có $D > 0$, thấu kính phân kì (như kính cận) có $D < 0$."),
            )
        ],
        example="Chiếu một chùm tia sáng Mặt Trời (coi là chùm sáng song song) vuông góc với mặt một thấu kính hội tụ thì thấy chùm tia ló hội tụ tại một điểm sáng chói trên màn chắn đặt cách quang tâm thấu kính $15\\text{ cm}$. Tiêu cự $f$ của thấu kính hội tụ này bằng bao nhiêu?",
        example_answer="Chùm sáng song song vuông góc với thấu kính hội tụ sẽ hội tụ tại tiêu điểm chính $F'$, do đó tiêu cự của thấu kính là $f = OF' = 15\\text{ cm}$.",
        real_life="Kính lão (kính viễn) là thấu kính hội tụ, còn kính cận thị mà học sinh bị cận thường đeo là thấu kính phân kì (sờ tay thấy phần rìa kính dày hơn phần chính giữa).",
        quiz=[
            mcq("biet", "Đặc điểm hình dạng về độ dày của thấu kính hội tụ là gì?", ["Có phần rìa mỏng hơn phần chính giữa (thấu kính rìa mỏng)", "Có phần rìa dày hơn phần chính giữa (thấu kính rìa dày)", "Có độ dày ở rìa và ở giữa bằng nhau như tấm kính phẳng", "Luôn được làm bằng kim loại"], 0, "Thấu kính hội tụ có phần rìa mỏng hơn phần giữa."),
            mcq("biet", "Tia sáng đi qua điểm nào của thấu kính (cả hội tụ và phân kì) thì tia ló tiếp tục truyền thẳng không bị đổi hướng?", ["Quang tâm $O$", "Tiêu điểm chính $F$", "Tiêu điểm chính $F'$", "Mép ngoài cùng của rìa thấu kính"], 0, "Mọi tia sáng đi qua quang tâm $O$ của thấu kính đều truyền thẳng không đổi hướng."),
            mcq("hieu", "Khi chiếu một chùm tia tới song song với trục chính của một thấu kính phân kì có tiêu cự $f = 20\\text{ cm}$, chùm tia ló có đặc điểm gì?", ["Là chùm tia phân kì có đường kéo dài cắt nhau tại tiêu điểm nằm trước thấu kính cách quang tâm $20\\text{ cm}$", "Là chùm tia hội tụ tại một điểm sau thấu kính cách quang tâm $20\\text{ cm}$", "Là chùm tia song song với trục chính", "Bị phản xạ ngược trở lại toàn bộ"], 0, "Qua thấu kính phân kì, chùm tia tới song song với trục chính cho chùm tia ló loe rộng ra (phân kì) có đường kéo dài đi qua tiêu điểm cách $O$ một khoảng $f = 20\\text{ cm}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về thấu kính hội tụ và thấu kính phân kì:", [
                "Hai tiêu điểm chính $F$ và $F'$ nằm trên trục chính và cách đều quang tâm $O$ ($OF = OF' = f$).",
                "Thấu kính phân kì có phần rìa dày hơn phần giữa.",
                "Có thể dùng thấu kính phân kì hứng ánh nắng Mặt Trời để tập trung ánh sáng đốt cháy một mảnh giấy.",
                "Tia sáng tới song song với trục chính của thấu kính hội tụ cho tia ló đi qua tiêu điểm chính.",
            ], [True, True, False, True], "Ý c) sai vì chỉ có thấu kính hội tụ mới tập trung được chùm nắng Mặt Trời tại tiêu điểm để đốt nóng mảnh giấy, còn thấu kính phân kì làm chùm sáng loe rộng ra."),
            short("vandung", "Một thấu kính hội tụ có khoảng cách giữa hai tiêu điểm chính $F$ và $F'$ nằm ở hai bên quang tâm là $FF' = 36\\text{ cm}$. Tiêu cự $f$ của thấu kính này bằng bao nhiêu $\\text{cm}$?", ["18"], "Vì $O$ là trung điểm của $FF'$ nên tiêu cự của thấu kính là $f = \\dfrac{FF'}{2} = \\dfrac{36}{2} = 18\\text{ cm}$.", unit="cm"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 7: Ảnh của vật tạo bởi thấu kính. Kính lúp",
        icon="🔎",
        description="Tính chất và cách dựng ảnh của vật qua thấu kính hội tụ, thấu kính phân kì; cấu tạo và số bội giác của kính lúp G = 25/f.",
        requirements=[
            "Nêu được tính chất ảnh của vật sáng qua thấu kính hội tụ (khi $d > f$ cho ảnh thật ngược chiều, khi $d < f$ cho ảnh ảo cùng chiều và lớn hơn vật) và qua thấu kính phân kì (luôn cho ảnh ảo, cùng chiều, nhỏ hơn vật).",
            "Vận dụng được hệ thức thấu kính và tam giác đồng dạng $\\dfrac{h'}{h} = \\dfrac{d'}{d}$ để xác định vị trí và chiều cao của ảnh.",
            "Nêu được kính lúp là một thấu kính hội tụ có tiêu cự ngắn dùng để quan sát vật nhỏ và tính được số bội giác $G = \\dfrac{25}{f(\\text{cm})}$.",
        ],
        definition="Vật đặt ngoài khoảng tiêu cự ($d > f$) của thấu kính hội tụ cho ảnh thật, ngược chiều với vật; đặt trong khoảng tiêu cự ($d < f$) cho ảnh ảo, cùng chiều và lớn hơn vật. Vật đặt ở mọi vị trí trước thấu kính phân kì luôn cho ảnh ảo, cùng chiều và nhỏ hơn vật.",
        theory=(
            "### 1. Tính chất ảnh tạo bởi hai loại thấu kính\n"
            "- **Thấu kính hội tụ**:\n"
            "  - Khi $d > f$: cho **ảnh thật**, **ngược chiều** với vật (hứng được trên màn chắn): $\\dfrac{1}{f} = \\dfrac{1}{d} + \\dfrac{1}{d'}$ (trong đó nếu $d > 2f$ thì ảnh nhỏ hơn vật, $d = 2f$ thì ảnh bằng vật, $f < d < 2f$ thì ảnh lớn hơn vật).\n"
            "  - Khi $d < f$: cho **ảnh ảo**, **cùng chiều** và **lớn hơn vật** ($d'$ cách thấu kính xa hơn vật: $\\dfrac{1}{f} = \\dfrac{1}{d} - \\dfrac{1}{d'}$).\n"
            "- **Thấu kính phân kì**: Với mọi vị trí đặt vật ($d > 0$), luôn cho **ảnh ảo**, **cùng chiều**, **nhỏ hơn vật** và nằm trong khoảng tiêu cự ($d' < f$): $\\dfrac{1}{f} = \\dfrac{1}{d'} - \\dfrac{1}{d}$.\n\n"
            "### 2. Kính lúp\n"
            "- **Kính lúp** là một thấu kính hội tụ có tiêu cự ngắn (vài xăng-ti-mét), dùng để quan sát các vật nhỏ. Khi dùng kính lúp, phải đặt vật **trong khoảng tiêu cự ($d < f$)** để nhìn thấy ảnh ảo lớn hơn vật.\n"
            "- Trên vành kính lúp thường ghi giá trị **số bội giác** ($2\\times, 3\\times, 5\\times, 10\\times$), liên hệ với tiêu cự $f(\\text{cm})$ bởi: $G = \\dfrac{25}{f(\\text{cm})}$."
        ),
        formulas=[
            G(
                "Công thức thấu kính và Số bội giác kính lúp",
                F("Hệ thức vị trí và chiều cao ảnh (ảnh thật qua TKHT)", "$\\dfrac{1}{f} = \\dfrac{1}{d} + \\dfrac{1}{d'} \\implies d' = \\dfrac{d \\cdot f}{d - f}; \\qquad \\dfrac{h'}{h} = \\dfrac{d'}{d}$", "Khi $d < f$ (ảnh ảo qua TKHT): $d' = \\dfrac{d \\cdot f}{f - d}$; khi qua TKPK: $d' = \\dfrac{d \\cdot f}{d + f}$."),
                F("Số bội giác của kính lúp", "$G = \\dfrac{25}{f(\\text{cm})}$", "Ví dụ: kính lúp ghi $5\\times$ ($G = 5$) có tiêu cự $f = \\dfrac{25}{5} = 5\\text{ cm}$."),
            )
        ],
        example="Một vật sáng $AB$ cao $h = 2\\text{ cm}$ đặt vuông góc với trục chính của một thấu kính hội tụ có tiêu cự $f = 10\\text{ cm}$ và cách thấu kính một khoảng $d = 30\\text{ cm}$. Hãy tính khoảng cách từ ảnh đến thấu kính $d'$ và chiều cao $h'$ của ảnh.",
        example_answer="Vì $d = 30\\text{ cm} > f = 10\\text{ cm}$ nên ảnh là ảnh thật. Ta có $\\dfrac{1}{f} = \\dfrac{1}{d} + \\dfrac{1}{d'} \\implies d' = \\dfrac{d \\cdot f}{d - f} = \\dfrac{30 \\cdot 10}{30 - 10} = 15\\text{ cm}$. Chiều cao của ảnh là $h' = h \\cdot \\dfrac{d'}{d} = 2 \\cdot \\dfrac{15}{30} = 1\\text{ cm}$.",
        real_life="Thợ sửa đồng hồ, nhà thực vật học và người lớn tuổi đọc chữ nhỏ sử dụng kính lúp; máy ảnh và máy chiếu trong lớp học sử dụng hệ thấu kính hội tụ để tạo ảnh thật rõ nét.",
        quiz=[
            mcq("biet", "Đặt một vật sáng ở bất kì vị trí nào trước một **thấu kính phân kì** thì ta luôn thu được ảnh có tính chất gì?", ["Ảnh ảo, cùng chiều với vật và nhỏ hơn vật", "Ảnh thật, ngược chiều với vật và lớn hơn vật", "Ảnh ảo, cùng chiều với vật và lớn hơn vật", "Ảnh thật, cùng chiều với vật"], 0, "Thấu kính phân kì luôn cho ảnh ảo, cùng chiều và nhỏ hơn vật ở mọi vị trí đặt vật."),
            mcq("biet", "Khi dùng kính lúp (thấu kính hội tụ có tiêu cự $f$) để quan sát một vật nhỏ, ta phải đặt vật ở vị trí nào so với kính lúp?", ["Đặt vật trong khoảng tiêu cự của kính lúp ($d < f$)", "Đặt vật ngoài khoảng tiêu cự rất xa ($d > 2f$)", "Đặt vật cách kính đúng bằng $2f$", "Đặt vật ở phía sau mắt người"], 0, "Để kính lúp tạo ảnh ảo cùng chiều và phóng đại lớn hơn vật, cần đặt vật trong khoảng tiêu cự ($d < f$)."),
            mcq("hieu", "Trên vành của một chiếc kính lúp có ghi kí hiệu $5\\times$ (số bội giác $G = 5$). Tiêu cự $f$ của chiếc kính lúp này bằng bao nhiêu?", ["$5\\text{ cm}$", "$25\\text{ cm}$", "$125\\text{ cm}$", "$0{,}2\\text{ cm}$"], 0, "Từ công thức $G = \\dfrac{25}{f(\\text{cm})} \\implies f = \\dfrac{25}{G} = \\dfrac{25}{5} = 5\\text{ cm}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về ảnh qua thấu kính và kính lúp:", [
                "Khi đặt vật cách thấu kính hội tụ một khoảng $d = 2f$ thì thu được ảnh thật ngược chiều và cao bằng vật ($h' = h$).",
                "Ảnh thật tạo bởi thấu kính hội tụ có thể hứng được trên màn chắn, còn ảnh ảo thì không hứng được trên màn chắn.",
                "Một thấu kính hội tụ và một thấu kính phân kì khi đặt gần trang sách đều cho ảnh chữ phóng to như nhau.",
                "Kính lúp có tiêu cự càng ngắn thì số bội giác $G$ càng lớn.",
            ], [True, True, False, True], "Ý c) sai vì đặt gần trang sách ($d < f$), thấu kính hội tụ cho ảnh chữ phóng to còn thấu kính phân kì cho ảnh chữ thu nhỏ."),
            short("vandung", "Một kính lúp có tiêu cự $f = 2{,}5\\text{ cm}$. Số bội giác $G$ ghi trên vành kính lúp này bằng bao nhiêu (theo công thức $G = \\dfrac{25}{f(\\text{cm})}$)?", ["10"], "Áp dụng công thức $G = \\dfrac{25}{f} = \\dfrac{25}{2{,}5} = 10$.", unit="x"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 8: Điện trở. Định luật Ohm",
        icon="⚡",
        description="Khái niệm điện trở R (Ω), định luật Ohm I = U/R, công thức điện trở dây dẫn R = ρ.ℓ/S và biến trở.",
        requirements=[
            "Nêu được điện trở ($R$, đơn vị Ôm – $\\Omega$) là đại lượng đặc trưng cho mức độ cản trở dòng điện của vật dẫn.",
            "Phát biểu và vận dụng được Định luật Ohm: cường độ dòng điện chạy qua một đoạn dây dẫn tỉ lệ thuận với hiệu điện thế đặt vào hai đầu dây và tỉ lệ nghịch với điện trở của nó ($I = \\dfrac{U}{R}$).",
            "Vận dụng được công thức điện trở của dây dẫn $R = \\rho \\dfrac{\\ell}{S}$ và giải thích nguyên tắc hoạt động của biến trở.",
        ],
        definition="Theo Định luật Ohm: Cường độ dòng điện chạy qua một đoạn dây dẫn tỉ lệ thuận với hiệu điện thế đặt vào hai đầu dây và tỉ lệ nghịch với điện trở của nó: $I = \\dfrac{U}{R}$.",
        theory=(
            "### 1. Điện trở và Định luật Ohm\n"
            "- **Điện trở** của dây dẫn: $R = \\dfrac{U}{I}$ (đối với một dây dẫn nhất định ở nhiệt độ không đổi, $R$ là hằng số không phụ thuộc vào $U$ và $I$).\n"
            "- Đơn vị điện trở trong hệ SI là **Ôm** (kí hiệu $\\Omega$): $1\\text{ k}\\Omega = 1000\\text{ }\\Omega$; $1\\text{ M}\\Omega = 10^6\\text{ }\\Omega$.\n"
            "- **Định luật Ohm**:\n"
            "  $$I = \\dfrac{U}{R} \\implies U = I \\cdot R; \\quad R = \\dfrac{U}{I}$$\n"
            "- Đồ thị biểu diễn sự phụ thuộc của $I$ vào $U$ là một **đường thẳng đi qua gốc tọa độ $O(0; 0)$**.\n\n"
            "### 2. Sự phụ thuộc của điện trở vào dây dẫn và Biến trở\n"
            "- Điện trở của một dây dẫn tỉ lệ thuận với chiều dài $\\ell$, tỉ lệ nghịch với tiết diện $S$ và phụ thuộc vào vật liệu làm dây dẫn (điện trở suất $\\rho$, đơn vị $\\Omega\\cdot\\text{m}$):\n"
            "  $$R = \\rho \\dfrac{\\ell}{S}$$\n"
            "- **Biến trở**: điện trở có thể thay đổi trị số (nhờ dịch chuyển con chạy làm thay đổi chiều dài phần dây dẫn có dòng điện chạy qua), dùng để điều chỉnh cường độ dòng điện trong mạch."
        ),
        formulas=[
            G(
                "Định luật Ohm và Công thức điện trở dây dẫn",
                F("Hệ thức Định luật Ohm", "$I = \\dfrac{U}{R} \\iff U = I \\cdot R \\iff R = \\dfrac{U}{I}$", "Trong đó $U$ tính bằng $\\text{V}$, $R$ tính bằng $\\Omega$ và $I$ tính bằng $\\text{A}$."),
                F("Điện trở của dây dẫn hình trụ đồng chất", "$R = \\rho \\dfrac{\\ell}{S}$", "Trong đó $\\rho$ là điện trở suất ($\\Omega\\cdot\\text{m}$), $\\ell$ là chiều dài dây ($\\text{m}$), $S$ là tiết diện ngang của dây ($\\text{m}^2$, với $1\\text{ mm}^2 = 10^{-6}\\text{ m}^2$)."),
            )
        ],
        example="Đặt một hiệu điện thế $U = 12\\text{ V}$ vào hai đầu một điện trở $R = 24\\text{ }\\Omega$. Hãy tính cường độ dòng điện $I$ chạy qua điện trở đó. Nếu tăng hiệu điện thế lên $U' = 18\\text{ V}$ thì cường độ dòng điện lúc đó là bao nhiêu?",
        example_answer="Theo định luật Ohm, cường độ dòng điện ban đầu là $I = \\dfrac{U}{R} = \\dfrac{12}{24} = 0{,}5\\text{ A}$. Khi tăng hiệu điện thế lên $U' = 18\\text{ V}$ (điện trở $R = 24\\text{ }\\Omega$ không đổi), cường độ dòng điện mới là $I' = \\dfrac{U'}{R} = \\dfrac{18}{24} = 0{,}75\\text{ A}$.",
        real_life="Núm xoay chỉnh âm lượng (Volume) trên loa đài hay chiết áp chỉnh độ sáng của đèn bàn chính là các biến trở giúp thay đổi cường độ dòng điện chạy trong mạch.",
        quiz=[
            mcq("biet", "Biểu thức của Định luật Ohm đối với một đoạn dây dẫn có điện trở $R$ là gì?", ["$I = \\dfrac{U}{R}$", "$I = U \\cdot R$", "$I = \\dfrac{R}{U}$", "$U = \\dfrac{I}{R}$"], 0, "Theo định luật Ohm, cường độ dòng điện $I = \\dfrac{U}{R}$."),
            mcq("biet", "Điện trở $R$ của một dây dẫn kim loại đồng chất có chiều dài $\\ell$, tiết diện $S$ và điện trở suất $\\rho$ được tính theo công thức nào?", ["$R = \\rho \\dfrac{\\ell}{S}$", "$R = \\rho \\dfrac{S}{\\ell}$", "$R = \\dfrac{\\ell}{\\rho S}$", "$R = \\rho \\cdot \\ell \\cdot S$"], 0, "Điện trở dây dẫn tỉ lệ thuận với $\\ell$ và tỉ lệ nghịch với $S$: $R = \\rho \\dfrac{\\ell}{S}$."),
            mcq("hieu", "Khi đặt hiệu điện thế $U = 6\\text{ V}$ vào hai đầu một dây dẫn thì dòng điện chạy qua nó có cường độ $I = 0{,}3\\text{ A}$. Nếu tăng hiệu điện thế đặt vào hai đầu dây dẫn đó lên thành $12\\text{ V}$ thì điện trở $R$ của dây dẫn đó bằng bao nhiêu?", ["$20\\text{ }\\Omega$ (không đổi)", "$40\\text{ }\\Omega$", "$10\\text{ }\\Omega$", "$3{,}6\\text{ }\\Omega$"], 0, "Điện trở của dây dẫn là $R = \\dfrac{U}{I} = \\dfrac{6}{0{,}3} = 20\\text{ }\\Omega$. Khi tăng $U$ lên $12\\text{ V}$ thì $I$ tăng lên $0{,}6\\text{ A}$, còn giá trị điện trở $R = 20\\text{ }\\Omega$ của dây dẫn vẫn không đổi."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về điện trở và định luật Ohm:", [
                "Đơn vị đo điện trở trong hệ SI là Ôm ($\\Omega$), với $1\\text{ k}\\Omega = 1000\\text{ }\\Omega$.",
                "Với hai dây dẫn làm bằng cùng một chất và có cùng tiết diện, dây nào dài gấp $3$ lần thì có điện trở lớn gấp $3$ lần.",
                "Với hai dây dẫn cùng chất và cùng chiều dài, dây nào có tiết diện lớn gấp $2$ lần thì có điện trở lớn gấp $2$ lần.",
                "Biến trở con chạy hoạt động dựa trên việc thay đổi chiều dài phần dây dẫn có dòng điện chạy qua.",
            ], [True, True, False, True], "Ý c) sai vì điện trở tỉ lệ nghịch với tiết diện $S$, nên tiết diện lớn gấp $2$ lần thì điện trở giảm đi $2$ lần."),
            short("vandung", "Đặt một hiệu điện thế $U = 9\\text{ V}$ vào hai đầu một điện trở $R = 15\\text{ }\\Omega$. Cường độ dòng điện $I$ chạy qua điện trở bằng bao nhiêu Ampe ($\\text{A}$)?", ["0,6", "0.6"], "Áp dụng định luật Ohm: $I = \\dfrac{U}{R} = \\dfrac{9}{15} = 0{,}6\\text{ A}$.", unit="A"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 9: Đoạn mạch nối tiếp",
        icon="🔗",
        description="Tính chất cường độ dòng điện, hiệu điện thế và công thức điện trở tương đương R_tđ = R₁ + R₂ của đoạn mạch mắc nối tiếp.",
        requirements=[
            "Nêu được trong đoạn mạch mắc nối tiếp, cường độ dòng điện có giá trị như nhau tại mọi điểm ($I = I_1 = I_2 = \\dots$) và hiệu điện thế giữa hai đầu đoạn mạch bằng tổng các hiệu điện thế thành phần ($U = U_1 + U_2 + \\dots$).",
            "Viết và vận dụng được công thức tính điện trở tương đương của đoạn mạch nối tiếp: $R_{\\text{tđ}} = R_1 + R_2 + \\dots + R_n$.",
            "Vận dụng được hệ thức phân áp $\\dfrac{U_1}{U_2} = \\dfrac{R_1}{R_2}$ để giải các bài toán mạch điện nối tiếp.",
        ],
        definition="Trong đoạn mạch gồm các điện trở mắc nối tiếp, dòng điện chỉ có một đường truyền duy nhất nên cường độ dòng điện bằng nhau tại mọi vị trí ($I = I_1 = I_2$), hiệu điện thế toàn mạch bằng tổng các hiệu điện thế thành phần ($U = U_1 + U_2$) và điện trở tương đương bằng tổng các điện trở thành phần ($R_{\\text{tđ}} = R_1 + R_2$).",
        theory=(
            "### 1. Các hệ thức của đoạn mạch gồm hai điện trở $R_1$ nối tiếp $R_2$\n"
            "- **Cường độ dòng điện**: $I = I_1 = I_2$.\n"
            "- **Hiệu điện thế**: $U = U_1 + U_2$.\n"
            "- **Điện trở tương đương**:\n"
            "  $$R_{\\text{tđ}} = R_1 + R_2$$\n"
            "  (Điện trở tương đương của đoạn mạch nối tiếp luôn **lớn hơn** mỗi điện trở thành phần).\n\n"
            "### 2. Quy tắc chia thế (phân áp) trong mạch nối tiếp\n"
            "- Vì $I_1 = I_2 \\iff \\dfrac{U_1}{R_1} = \\dfrac{U_2}{R_2}$, nên hiệu điện thế giữa hai đầu mỗi điện trở tỉ lệ thuận với điện trở đó:\n"
            "  $$\\dfrac{U_1}{U_2} = \\dfrac{R_1}{R_2}$$"
        ),
        formulas=[
            G(
                "Các công thức của đoạn mạch mắc nối tiếp",
                F("Dòng điện, hiệu điện thế và điện trở tương đương", "$I = I_1 = I_2; \\qquad U = U_1 + U_2; \\qquad R_{\\text{tđ}} = R_1 + R_2$", "Mở rộng cho $n$ điện trở giống nhau có giá trị $R_0$ mắc nối tiếp: $R_{\\text{tđ}} = n \\cdot R_0$."),
                F("Hệ thức phân áp trên hai điện trở nối tiếp", "$\\dfrac{U_1}{U_2} = \\dfrac{R_1}{R_2} \\implies U_1 = U \\cdot \\dfrac{R_1}{R_1 + R_2}$", "Trong mạch nối tiếp, điện trở nào lớn hơn thì chịu hiệu điện thế lớn hơn."),
            )
        ],
        example="Cho hai điện trở $R_1 = 10\\text{ }\\Omega$ và $R_2 = 15\\text{ }\\Omega$ mắc nối tiếp nhau vào nguồn điện có hiệu điện thế $U = 10\\text{ V}$. Hãy tính điện trở tương đương $R_{\\text{tđ}}$ của đoạn mạch, cường độ dòng điện $I$ chạy trong mạch và hiệu điện thế $U_1, U_2$ trên mỗi điện trở.",
        example_answer="Điện trở tương đương của đoạn mạch là $R_{\\text{tđ}} = R_1 + R_2 = 10 + 15 = 25\\text{ }\\Omega$. Cường độ dòng điện trong mạch là $I = I_1 = I_2 = \\dfrac{U}{R_{\\text{tđ}}} = \\dfrac{10}{25} = 0{,}4\\text{ A}$. Hiệu điện thế trên từng điện trở là $U_1 = I \\cdot R_1 = 0{,}4 \\cdot 10 = 4\\text{ V}$ và $U_2 = I \\cdot R_2 = 0{,}4 \\cdot 15 = 6\\text{ V}$.",
        real_life="Cầu chì, công tắc và biến trở điều chỉnh dòng điện luôn được mắc nối tiếp với thiết bị điện cần bảo vệ hoặc điều khiển.",
        quiz=[
            mcq("biet", "Công thức tính điện trở tương đương $R_{\\text{tđ}}$ của đoạn mạch gồm hai điện trở $R_1$ và $R_2$ mắc nối tiếp là gì?", ["$R_{\\text{tđ}} = R_1 + R_2$", "$R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}$", "$\\dfrac{1}{R_{\\text{tđ}}} = \\dfrac{1}{R_1} + \\dfrac{1}{R_2}$", "$R_{\\text{tđ}} = |R_1 - R_2|$"], 0, "Trong đoạn mạch mắc nối tiếp, điện trở tương đương bằng tổng các điện trở thành phần: $R_{\\text{tđ}} = R_1 + R_2$."),
            mcq("biet", "Trong đoạn mạch gồm hai bóng đèn mắc nối tiếp, nếu dây tóc của một bóng đèn bị đứt thì bóng đèn còn lại sẽ như thế nào?", ["Bóng đèn còn lại cũng tắt ngay vì mạch điện bị hở", "Bóng đèn còn lại sáng mạnh gấp đôi", "Bóng đèn còn lại vẫn sáng bình thường", "Bóng đèn còn lại nhấp nháy liên tục"], 0, "Trong mạch mắc nối tiếp chỉ có một đường truyền dòng điện duy nhất, khi một đèn đứt dây tóc làm mạch bị hở nên đèn kia cũng tắt."),
            mcq("hieu", "Mắc nối tiếp hai điện trở $R_1 = 6\\text{ }\\Omega$ và $R_2 = 18\\text{ }\\Omega$ vào một hiệu điện thế không đổi. Tỉ số hiệu điện thế giữa hai đầu điện trở thứ hai và thứ nhất $\\dfrac{U_2}{U_1}$ bằng bao nhiêu?", ["$3$", "$\\dfrac{1}{3}$", "$12$", "$24$"], 0, "Vì $I_1 = I_2$ nên $\\dfrac{U_2}{U_1} = \\dfrac{R_2}{R_1} = \\dfrac{18}{6} = 3$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đoạn mạch mắc nối tiếp:", [
                "Cường độ dòng điện có giá trị như nhau tại mọi điểm trên đoạn mạch nối tiếp ($I = I_1 = I_2$).",
                "Điện trở tương đương của đoạn mạch nối tiếp luôn lớn hơn mỗi điện trở thành phần.",
                "Hiệu điện thế giữa hai đầu đoạn mạch nối tiếp bằng hiệu điện thế trên từng điện trở ($U = U_1 = U_2$).",
                "Ba điện trở giống nhau mỗi chiếc $10\\text{ }\\Omega$ mắc nối tiếp có điện trở tương đương là $30\\text{ }\\Omega$.",
            ], [True, True, False, True], "Ý c) sai vì trong đoạn mạch nối tiếp thì $U = U_1 + U_2$, còn $U = U_1 = U_2$ là tính chất của đoạn mạch song song."),
            short("vandung", "Hai điện trở $R_1 = 8\\text{ }\\Omega$ và $R_2 = 12\\text{ }\\Omega$ được mắc nối tiếp vào hiệu điện thế $U = 40\\text{ V}$. Cường độ dòng điện $I$ chạy trong đoạn mạch bằng bao nhiêu Ampe ($\\text{A}$)?", ["2"], "Ta có $R_{\\text{tđ}} = R_1 + R_2 = 8 + 12 = 20\\text{ }\\Omega$. Cường độ dòng điện là $I = \\dfrac{U}{R_{\\text{tđ}}} = \\dfrac{40}{20} = 2\\text{ A}$.", unit="A"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 10: Đoạn mạch song song",
        icon="🔀",
        description="Tính chất hiệu điện thế, cường độ dòng điện và công thức điện trở tương đương 1/R_tđ = 1/R₁ + 1/R₂ của đoạn mạch mắc song song.",
        requirements=[
            "Nêu được trong đoạn mạch mắc song song, hiệu điện thế giữa hai đầu các nhánh bằng nhau ($U = U_1 = U_2$) và cường độ dòng điện mạch chính bằng tổng cường độ dòng điện các nhánh rẽ ($I = I_1 + I_2$).",
            "Viết và vận dụng được công thức tính điện trở tương đương của đoạn mạch song song: $\\dfrac{1}{R_{\\text{tđ}}} = \\dfrac{1}{R_1} + \\dfrac{1}{R_2}$ hay $R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}$.",
            "Giải thích được vì sao các thiết bị điện trong gia đình (đèn, quạt, tivi, tủ lạnh) đều được mắc song song vào mạng điện $220\\text{ V}$.",
        ],
        definition="Trong đoạn mạch gồm các điện trở mắc song song, hiệu điện thế giữa hai đầu mỗi nhánh bằng hiệu điện thế hai đầu đoạn mạch ($U = U_1 = U_2$), cường độ dòng điện mạch chính bằng tổng cường độ dòng điện chạy qua các nhánh ($I = I_1 + I_2$) và nghịch đảo điện trở tương đương bằng tổng các nghịch đảo điện trở thành phần ($\\dfrac{1}{R_{\\text{tđ}}} = \\dfrac{1}{R_1} + \\dfrac{1}{R_2}$).",
        theory=(
            "### 1. Các hệ thức của đoạn mạch gồm $R_1$ mắc song song $R_2$\n"
            "- **Hiệu điện thế**: $U = U_1 = U_2$.\n"
            "- **Cường độ dòng điện**: $I = I_1 + I_2$.\n"
            "- **Điện trở tương đương**:\n"
            "  $$\\dfrac{1}{R_{\\text{tđ}}} = \\dfrac{1}{R_1} + \\dfrac{1}{R_2} \\iff R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}$$\n"
            "  (Điện trở tương đương của đoạn mạch song song luôn **nhỏ hơn** mỗi điện trở thành phần).\n\n"
            "### 2. Quy tắc chia dòng (phân dòng) và Ứng dụng\n"
            "- Vì $U_1 = U_2 \\iff I_1 R_1 = I_2 R_2$, nên cường độ dòng điện qua mỗi nhánh tỉ lệ nghịch với điện trở của nhánh đó:\n"
            "  $$\\dfrac{I_1}{I_2} = \\dfrac{R_2}{R_1}$$\n"
            "- Trong mạng điện gia đình, các thiết bị có cùng hiệu điện thế định mức $220\\text{ V}$ được **mắc song song** để mỗi thiết bị đều nhận đủ $220\\text{ V}$ và có thể bật/tắt độc lập mà không ảnh hưởng đến thiết bị khác."
        ),
        formulas=[
            G(
                "Các công thức của đoạn mạch mắc song song",
                F("Hiệu điện thế, dòng điện và điện trở tương đương", "$U = U_1 = U_2; \\qquad I = I_1 + I_2; \\qquad R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}$", "Nếu có $n$ điện trở giống nhau mỗi chiếc $R_0$ mắc song song thì $R_{\\text{tđ}} = \\dfrac{R_0}{n}$."),
                F("Hệ thức phân dòng qua hai nhánh song song", "$\\dfrac{I_1}{I_2} = \\dfrac{R_2}{R_1}$", "Trong mạch song song, nhánh nào có điện trở nhỏ hơn thì có dòng điện chạy qua lớn hơn."),
            )
        ],
        example="Cho hai điện trở $R_1 = 6\\text{ }\\Omega$ và $R_2 = 12\\text{ }\\Omega$ mắc song song với nhau vào nguồn điện có hiệu điện thế $U = 12\\text{ V}$. Hãy tính điện trở tương đương $R_{\\text{tđ}}$, cường độ dòng điện qua mỗi nhánh $I_1, I_2$ và cường độ dòng điện trong mạch chính $I$.",
        example_answer="Điện trở tương đương là $R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2} = \\dfrac{6 \\cdot 12}{6 + 12} = 4\\text{ }\\Omega$. Vì mắc song song nên $U_1 = U_2 = U = 12\\text{ V}$. Dòng điện qua các nhánh là $I_1 = \\dfrac{U}{R_1} = \\dfrac{12}{6} = 2\\text{ A}$ và $I_2 = \\dfrac{U}{R_2} = \\dfrac{12}{12} = 1\\text{ A}$. Dòng điện mạch chính là $I = I_1 + I_2 = 2 + 1 = 3\\text{ A}$.",
        real_life="Hệ thống đèn chiếu sáng, quạt trần, điều hòa và tủ lạnh trong nhà đều được mắc song song vào nguồn $220\\text{ V}$ để khi tắt đèn đi ngủ thì tủ lạnh vẫn hoạt động bình thường.",
        quiz=[
            mcq("biet", "Công thức tính điện trở tương đương $R_{\\text{tđ}}$ của hai điện trở $R_1$ và $R_2$ mắc song song là gì?", ["$R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}$", "$R_{\\text{tđ}} = R_1 + R_2$", "$R_{\\text{tđ}} = \\dfrac{R_1 + R_2}{R_1 \\cdot R_2}$", "$R_{\\text{tđ}} = R_1 \\cdot R_2$"], 0, "Từ $\\dfrac{1}{R_{\\text{tđ}}} = \\dfrac{1}{R_1} + \\dfrac{1}{R_2}$ suy ra $R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}$."),
            mcq("biet", "Vì sao các dụng cụ điện trong gia đình (như bóng đèn, quạt điện, tivi) có hiệu điện thế định mức $220\\text{ V}$ lại được mắc **song song** vào mạng điện $220\\text{ V}$?", ["Để tất cả các dụng cụ đều được đặt dưới hiệu điện thế $220\\text{ V}$ và hoạt động độc lập với nhau", "Để dòng điện qua mọi dụng cụ luôn bằng nhau", "Để khi tắt một bóng đèn thì cả nhà đều mất điện", "Để làm tăng điện trở tương đương của mạng điện"], 0, "Mắc song song giúp $U = U_1 = U_2 = 220\\text{ V}$ và bật/tắt từng thiết bị không làm ngắt mạch các thiết bị khác."),
            mcq("hieu", "Mắc song song hai điện trở $R_1 = 10\\text{ }\\Omega$ và $R_2 = 10\\text{ }\\Omega$ giống hệt nhau. Điện trở tương đương $R_{\\text{tđ}}$ của đoạn mạch là bao nhiêu?", ["$5\\text{ }\\Omega$", "$20\\text{ }\\Omega$", "$10\\text{ }\\Omega$", "$100\\text{ }\\Omega$"], 0, "Ta có $R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2} = \\dfrac{10 \\cdot 10}{10 + 10} = 5\\text{ }\\Omega$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đoạn mạch mắc song song:", [
                "Trong đoạn mạch song song, hiệu điện thế giữa hai đầu các nhánh luôn bằng nhau ($U = U_1 = U_2$).",
                "Cường độ dòng điện mạch chính bằng tổng cường độ dòng điện chạy qua các nhánh rẽ ($I = I_1 + I_2$).",
                "Điện trở tương đương của đoạn mạch song song luôn nhỏ hơn mỗi điện trở thành phần.",
                "Khi mắc thêm một dụng cụ điện song song vào ổ cắm gia đình thì điện trở tương đương của toàn mạch tăng lên.",
            ], [True, True, True, False], "Ý d) sai vì khi mắc thêm nhánh song song thì điện trở tương đương giảm xuống và cường độ dòng điện mạch chính tăng lên."),
            short("vandung", "Cho hai điện trở $R_1 = 20\\text{ }\\Omega$ và $R_2 = 30\\text{ }\\Omega$ mắc song song với nhau. Điện trở tương đương $R_{\\text{tđ}}$ của đoạn mạch bằng bao nhiêu Ôm ($\\Omega$)?", ["12"], "Ta có $R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2} = \\dfrac{20 \\cdot 30}{20 + 30} = \\dfrac{600}{50} = 12\\text{ }\\Omega$.", unit="Ω"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 11: Năng lượng điện và công suất điện",
        icon="🔌",
        description="Công suất điện P = U.I = I²R = U²/R, năng lượng điện tiêu thụ W = P.t = U.I.t, đơn vị kWh và định luật Joule–Lenz.",
        requirements=[
            "Viết và vận dụng được các công thức tính công suất điện: $\\mathcal{P} = U \\cdot I = I^2 R = \\dfrac{U^2}{R}$ (đơn vị Oát – $\\text{W}$).",
            "Giải thích được ý nghĩa các số ghi định mức trên dụng cụ điện (ví dụ $220\\text{ V} - 100\\text{ W}$).",
            "Tính được năng lượng điện tiêu thụ $W = \\mathcal{P} \\cdot t = U I t$, nhiệt lượng tỏa ra $Q = I^2 R t$ và số đếm công tơ điện ($1\\text{ kWh} = 3\\,600\\,000\\text{ J}$).",
        ],
        definition="Công suất điện của một đoạn mạch cho biết năng lượng điện mà đoạn mạch tiêu thụ trong một đơn vị thời gian, bằng tích của hiệu điện thế giữa hai đầu đoạn mạch và cường độ dòng điện chạy qua nó: $\\mathcal{P} = U \\cdot I$. Năng lượng điện tiêu thụ trong thời gian $t$ là $W = \\mathcal{P} \\cdot t = U I t$.",
        theory=(
            "### 1. Công suất điện và Số ghi định mức\n"
            "- Công thức tính công suất điện:\n"
            "  $$\\mathcal{P} = U \\cdot I = I^2 R = \\dfrac{U^2}{R}$$\n"
            "- Trên mỗi thiết bị điện đều ghi **Hiệu điện thế định mức ($U_{\\text{đm}}$)** và **Công suất định mức ($\\mathcal{P}_{\\text{đm}}$)** (ví dụ: bóng đèn ghi $220\\text{ V} - 60\\text{ W}$ nghĩa là khi đặt vào $U = 220\\text{ V}$ thì đèn hoạt động bình thường và tiêu thụ công suất $60\\text{ W}$, điện trở của đèn là $R = \\dfrac{U_{\\text{đm}}^2}{\\mathcal{P}_{\\text{đm}}}$).\n\n"
            "### 2. Năng lượng điện tiêu thụ (Điện năng) và Công tơ điện\n"
            "- Năng lượng điện tiêu thụ trong thời gian $t$: $W = \\mathcal{P} \\cdot t = U I t$.\n"
            "- Với đoạn mạch chỉ có điện trở thuần (bàn là, bếp điện), toàn bộ điện năng biến đổi thành nhiệt lượng (Định luật Joule–Lenz): $Q = I^2 R t$.\n"
            "- **Đơn vị đo điện năng thực tế trên công tơ điện**: mỗi 'số' điện là $1\\text{ kilôoát giờ}$ ($1\\text{ kWh}$):\n"
            "  $$1\\text{ kWh} = 1000\\text{ W} \\cdot 3600\\text{ s} = 3\\,600\\,000\\text{ J} = 3{,}6\\text{ MJ}$$"
        ),
        formulas=[
            G(
                "Công suất điện và Năng lượng điện tiêu thụ",
                F("Các công thức tính công suất điện", "$\\mathcal{P} = U \\cdot I = I^2 R = \\dfrac{U^2}{R} \\implies R = \\dfrac{U_{\\text{đm}}^2}{\\mathcal{P}_{\\text{đm}}}$", "Trong đó $U$ tính bằng $\\text{V}$, $I$ tính bằng $\\text{A}$, $R$ tính bằng $\\Omega$, $\\mathcal{P}$ tính bằng $\\text{W}$."),
                F("Năng lượng điện tiêu thụ và Số đếm công tơ điện", "$W = \\mathcal{P} \\cdot t = U I t; \\qquad 1\\text{ kWh (1 số điện)} = 3\\,600\\,000\\text{ J}$", "Để tính trực tiếp số chữ điện ($\\text{kWh}$), ta đổi $\\mathcal{P}$ ra $\\text{kW}$ và thời gian $t$ ra giờ ($\\text{h}$): $W(\\text{kWh}) = \\mathcal{P}(\\text{kW}) \\cdot t(\\text{h})$."),
            )
        ],
        example="Một ấm đun nước bằng điện có ghi $220\\text{ V} - 1100\\text{ W}$ được sử dụng ở hiệu điện thế đúng $220\\text{ V}$. Hãy tính cường độ dòng điện chạy qua ấm và số 'số điện' ($\\text{kWh}$) mà ấm tiêu thụ nếu đun nước trung bình $2\\text{ giờ}$ mỗi ngày trong suốt $30\\text{ ngày}$.",
        example_answer="Vì $U = U_{\\text{đm}} = 220\\text{ V}$ nên $\\mathcal{P} = 1100\\text{ W} = 1{,}1\\text{ kW}$. Cường độ dòng điện qua ấm là $I = \\dfrac{\\mathcal{P}}{U} = \\dfrac{1100}{220} = 5\\text{ A}$. Tổng thời gian sử dụng trong tháng là $t = 2 \\cdot 30 = 60\\text{ h}$. Điện năng tiêu thụ trong tháng là $W = \\mathcal{P} \\cdot t = 1{,}1 \\cdot 60 = 66\\text{ kWh}$ ($66$ số điện).",
        real_life="Dựa vào công suất ghi trên nhãn năng lượng của điều hòa, tủ lạnh, máy giặt và thời gian sử dụng hằng ngày, mỗi gia đình có thể tự tính được lượng điện tiêu thụ ($\\text{kWh}$) và tiền điện hằng tháng.",
        quiz=[
            mcq("biet", "Công thức nào sau đây tính công suất điện $\\mathcal{P}$ của một đoạn mạch có hiệu điện thế $U$ và cường độ dòng điện $I$?", ["$\\mathcal{P} = U \\cdot I$", "$\\mathcal{P} = \\dfrac{U}{I}$", "$\\mathcal{P} = \\dfrac{I}{U}$", "$\\mathcal{P} = U + I$"], 0, "Công suất điện của đoạn mạch bằng tích của hiệu điện thế và cường độ dòng điện: $\\mathcal{P} = U \\cdot I$."),
            mcq("biet", "Một 'số' đếm trên công tơ điện gia đình tương ứng với $1\\text{ kWh}$. Đổi ra đơn vị Joule ($\\text{J}$), $1\\text{ kWh}$ bằng bao nhiêu?", ["$3\\,600\\,000\\text{ J}$", "$3600\\text{ J}$", "$1000\\text{ J}$", "$360\\,000\\text{ J}$"], 0, "Ta có $1\\text{ kWh} = 1000\\text{ W} \\cdot 3600\\text{ s} = 3\\,600\\,000\\text{ J}$."),
            mcq("hieu", "Trên một bàn là điện có ghi $220\\text{ V} - 1100\\text{ W}$. Khi bàn là hoạt động bình thường ở hiệu điện thế $220\\text{ V}$, cường độ dòng điện chạy qua bàn là bằng bao nhiêu?", ["$5\\text{ A}$", "$0{,}2\\text{ A}$", "$22\\text{ A}$", "$50\\text{ A}$"], 0, "Ta có $I = \\dfrac{\\mathcal{P}}{U} = \\dfrac{1100}{220} = 5\\text{ A}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về năng lượng điện và công suất điện:", [
                "Công suất điện cho biết lượng điện năng tiêu thụ trong một đơn vị thời gian.",
                "Một bóng đèn ghi $220\\text{ V} - 100\\text{ W}$ có điện trở khi sáng bình thường là $R = \\dfrac{220^2}{100} = 484\\text{ }\\Omega$.",
                "Khi hiệu điện thế đặt vào bóng đèn nhỏ hơn hiệu điện thế định mức thì đèn sẽ sáng mạnh hơn bình thường.",
                "Một máy điều hòa công suất $1{,}5\\text{ kW}$ hoạt động liên tục trong $4\\text{ giờ}$ tiêu thụ $6\\text{ kWh}$ điện năng.",
            ], [True, True, False, True], "Ý c) sai vì khi $U < U_{\\text{đm}}$ thì công suất thực tế $\\mathcal{P} < \\mathcal{P}_{\\text{đm}}$ nên đèn sáng yếu hơn bình thường."),
            short("vandung", "Một bếp điện có công suất $\\mathcal{P} = 2000\\text{ W} = 2\\text{ kW}$ hoạt động liên tục trong thời gian $t = 1{,}5\\text{ giờ}$. Điện năng mà bếp tiêu thụ trong thời gian đó bằng bao nhiêu $\\text{kWh}$ (số điện)?", ["3"], "Áp dụng công thức $W = \\mathcal{P}(\\text{kW}) \\cdot t(\\text{h}) = 2 \\cdot 1{,}5 = 3\\text{ kWh}$.", unit="kWh"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 12: Cảm ứng điện từ",
        icon="🧲",
        description="Thí nghiệm tạo dòng điện cảm ứng bằng nam châm và cuộn dây dẫn kín, điều kiện xuất hiện dòng điện cảm ứng.",
        requirements=[
            "Mô tả được thí nghiệm dùng nam châm vĩnh cửu hoặc nam châm điện để tạo ra dòng điện trong một cuộn dây dẫn kín (dòng điện cảm ứng).",
            "Phát biểu được điều kiện xuất hiện dòng điện cảm ứng: khi số đường sức từ xuyên qua tiết diện của cuộn dây dẫn kín biến thiên (tăng lên hoặc giảm đi).",
            "Giải thích được sự chuyển hóa từ cơ năng thành điện năng trong hiện tượng cảm ứng điện từ.",
        ],
        definition="Hiện tượng xuất hiện dòng điện trong cuộn dây dẫn kín khi số đường sức từ xuyên qua tiết diện của cuộn dây đó biến thiên (tăng hoặc giảm) được gọi là hiện tượng cảm ứng điện từ; dòng điện tạo ra gọi là dòng điện cảm ứng.",
        theory=(
            "### 1. Thí nghiệm về hiện tượng cảm ứng điện từ (Michael Faraday, 1831)\n"
            "- Nối hai đầu một cuộn dây dẫn với điện kế nhạy (hoặc hai đèn LED mắc song song ngược chiều) thành mạch kín.\n"
            "- **Các cách làm xuất hiện dòng điện cảm ứng**:\n"
            "  1. Đưa một cực của nam châm **lại gần** hoặc **ra xa** cuộn dây dẫn kín.\n"
            "  2. Giữ nam châm đứng yên và cho cuộn dây **chuyển động lại gần hoặc ra xa** nam châm.\n"
            "  3. Cho nam châm **quay** trước cuộn dây dẫn kín.\n"
            "  4. Đóng hoặc ngắt mạch điện của một nam châm điện đặt gần cuộn dây dẫn kín.\n\n"
            "### 2. Điều kiện xuất hiện dòng điện cảm ứng\n"
            "- Nếu cả nam châm và cuộn dây đều đứng yên đối với nhau thì số đường sức từ xuyên qua tiết diện $S$ của cuộn dây không đổi $\\implies$ **không có dòng điện cảm ứng**.\n"
            "- **Kết luận**: Dòng điện cảm ứng xuất hiện trong cuộn dây dẫn kín trong thời gian **số đường sức từ xuyên qua tiết diện của cuộn dây dẫn đó biến thiên (tăng lên hoặc giảm đi)**."
        ),
        formulas=[
            G(
                "Điều kiện xuất hiện dòng điện cảm ứng",
                F("Điều kiện cần và đủ để có dòng điện cảm ứng", "$\\text{Cuộn dây dẫn kín} + \\Delta N_{\\text{đường sức từ qua } S} \\ne 0 \\implies i_{\\text{cảm ứng}} \\ne 0$", "Số đường sức từ xuyên qua tiết diện $S$ của cuộn dây phải đang tăng hoặc đang giảm."),
                F("Đổi chiều dòng điện cảm ứng", "$\\text{Số đường sức từ đang tăng} \\leftrightarrow \\text{Số đường sức từ đang giảm} \\implies i_{\\text{cảm ứng}} \\text{ đổi chiều}$", "Khi đưa nam châm lại gần cuộn dây thì dòng điện cảm ứng có chiều ngược với khi kéo nam châm ra xa cuộn dây."),
            )
        ],
        example="Đặt một thanh nam châm rất mạnh nằm yên hoàn toàn bên trong lòng một cuộn dây dẫn kín nối với điện kế. Hỏi kim điện kế có bị lệch không? Làm thế nào để kim điện kế lệch?",
        example_answer="Khi thanh nam châm nằm yên trong lòng cuộn dây, số đường sức từ xuyên qua tiết diện cuộn dây tuy lớn nhưng **không biến thiên** nên không có dòng điện cảm ứng và **kim điện kế không lệch (chỉ vạch số $0$)**. Để kim điện kế lệch, ta phải rút nam châm ra hoặc đẩy nam châm chuyển động tương đối so với cuộn dây.",
        real_life="Đinamô xe đạp, bếp từ đun nấu không khói và sạc không dây cho điện thoại thông minh đều hoạt động dựa trên hiện tượng cảm ứng điện từ.",
        quiz=[
            mcq("biet", "Điều kiện để xuất hiện dòng điện cảm ứng trong một cuộn dây dẫn kín là gì?", ["Số đường sức từ xuyên qua tiết diện của cuộn dây dẫn kín biến thiên (tăng hoặc giảm)", "Số đường sức từ xuyên qua tiết diện của cuộn dây dẫn kín luôn giữ nguyên không đổi", "Cuộn dây dẫn bị cắt đứt thành mạch hở", "Đặt một thanh đồng không nhiễm từ đứng yên cạnh cuộn dây"], 0, "Dòng điện cảm ứng chỉ xuất hiện trong cuộn dây dẫn kín khi số đường sức từ xuyên qua tiết diện của cuộn dây biến thiên."),
            mcq("biet", "Nhà bác học nào đã khám phá ra hiện tượng cảm ứng điện từ vào năm 1831, đặt nền móng cho các máy phát điện hiện đại?", ["Michael Faraday", "Isaac Newton", "Archimedes", "Georg Simon Ohm"], 0, "Nhà bác học người Anh Michael Faraday đã phát hiện ra hiện tượng cảm ứng điện từ vào năm 1831."),
            mcq("hieu", "Khi đưa cực Bắc ($\\text{N}$) của thanh nam châm lại gần cuộn dây dẫn kín thì đèn LED thứ nhất sáng; nếu sau đó kéo cực Bắc ($\\text{N}$) của thanh nam châm ra xa cuộn dây thì hiện tượng gì xảy ra?", ["Chiều dòng điện cảm ứng đổi ngược lại làm đèn LED thứ hai (mắc ngược chiều) phát sáng", "Cả hai đèn LED đều tắt", "Đèn LED thứ nhất vẫn tiếp tục sáng", "Thanh nam châm mất hết từ tính"], 0, "Khi đưa lại gần, số đường sức từ tăng; khi kéo ra xa, số đường sức từ giảm nên dòng điện cảm ứng đổi chiều ngược lại."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về hiện tượng cảm ứng điện từ:", [
                "Nếu giữ nam châm đứng yên và dịch chuyển cuộn dây dẫn kín lại gần nam châm thì trong cuộn dây vẫn xuất hiện dòng điện cảm ứng.",
                "Đặt một nam châm cực mạnh đứng yên mãi mãi bên cạnh cuộn dây dẫn kín sẽ tạo ra dòng điện cảm ứng liên tục.",
                "Trong đinamô xe đạp, khi bánh xe làm núm đinamô và nam châm quay trước cuộn dây, cơ năng đã chuyển hóa thành điện năng thắp sáng đèn.",
                "Khi đóng hoặc ngắt công tắc của nam châm điện đặt gần một cuộn dây kín thì trong cuộn dây kín xuất hiện dòng điện cảm ứng.",
            ], [True, False, True, True], "Ý b) sai vì khi nam châm và cuộn dây đứng yên đối với nhau thì số đường sức từ qua tiết diện cuộn dây không biến thiên nên không có dòng điện cảm ứng."),
            short("vandung", "Xét 3 trường hợp với một cuộn dây dẫn kín: (1) Đưa nam châm lại gần cuộn dây; (2) Giữ nam châm đứng yên trong lòng cuộn dây; (3) Kéo nam châm ra xa cuộn dây. Có bao nhiêu trường hợp trong 3 trường hợp trên xuất hiện **dòng điện cảm ứng**?", ["2"], "Trường hợp (1) số đường sức từ tăng và trường hợp (3) số đường sức từ giảm nên có $2$ trường hợp xuất hiện dòng điện cảm ứng; còn trường hợp (2) không biến thiên nên không có dòng điện cảm ứng."),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 13: Nguyên tắc tạo ra dòng điện xoay chiều",
        icon="🔄",
        description="Khái niệm dòng điện xoay chiều (AC), nguyên tắc khung dây quay trong từ trường và cấu tạo máy phát điện xoay chiều.",
        requirements=[
            "Phân biệt được dòng điện một chiều (DC – có chiều không đổi) và dòng điện xoay chiều (AC – có chiều và cường độ luân phiên thay đổi theo thời gian).",
            "Giải thích được khi cho khung dây dẫn kín quay trong từ trường (hoặc cho nam châm quay trước cuộn dây) thì số đường sức từ qua khung dây luân phiên tăng – giảm, tạo ra dòng điện cảm ứng xoay chiều.",
            "Nêu được hai bộ phận chính của máy phát điện xoay chiều là nam châm (tạo từ trường) và cuộn dây dẫn (tạo dòng điện cảm ứng), trong đó bộ phận đứng yên gọi là stato, bộ phận quay gọi là rôto.",
        ],
        definition="Dòng điện luân phiên đổi chiều được gọi là dòng điện xoay chiều (kí hiệu AC). Khi một khung dây dẫn kín quay trong từ trường của nam châm (hoặc nam châm quay trước cuộn dây), trong khung dây xuất hiện dòng điện cảm ứng xoay chiều vì số đường sức từ xuyên qua tiết diện khung dây luân phiên tăng và giảm.",
        theory=(
            "### 1. Dòng điện xoay chiều (AC)\n"
            "- **Dòng điện một chiều (DC)**: dòng điện có chiều không đổi theo thời gian (do pin, ắc quy tạo ra).\n"
            "- **Dòng điện xoay chiều (AC)**: dòng điện có cường độ và chiều luân phiên thay đổi theo thời gian (mạng điện sinh hoạt gia đình ở Việt Nam là dòng điện xoay chiều có hiệu điện thế $220\\text{ V}$, tần số $f = 50\\text{ Hz}$).\n\n"
            "### 2. Nguyên tắc tạo ra dòng điện xoay chiều và Máy phát điện\n"
            "- Dựa trên **hiện tượng cảm ứng điện từ**: khi khung dây dẫn quay trong từ trường (hoặc nam châm quay quanh cuộn dây), trong nửa vòng quay đầu số đường sức từ xuyên qua khung tăng lên rồi giảm đi theo một phía, sang nửa vòng quay tiếp theo đường sức từ xuyên qua mặt ngược lại nên **dòng điện cảm ứng đổi chiều mỗi nửa vòng quay**.\n"
            "- **Cấu tạo máy phát điện xoay chiều** luôn gồm 2 bộ phận chính: **nam châm** và **cuộn dây dẫn**. Bộ phận đứng yên gọi là **stato**, bộ phận quay gọi là **rôto**."
        ),
        formulas=[
            G(
                "Tần số và sự đổi chiều của dòng điện xoay chiều",
                F("Số lần đổi chiều của dòng điện xoay chiều tần số f", "$N_{\\text{đổi chiều trong 1 s}} = 2f$", "Trong mỗi chu kì (1 vòng quay), dòng điện xoay chiều đổi chiều $2$ lần. Ở mạng điện Việt Nam $f = 50\\text{ Hz}$, dòng điện đổi chiều $100$ lần trong $1\\text{ giây}$."),
                F("Tần số dòng điện theo tốc độ quay n (vòng/giây)", "$f = n \\cdot p$", "Trong đó $n$ là số vòng quay của rôto trong $1\\text{ giây}$ và $p$ là số cặp cực của nam châm."),
            )
        ],
        example="Mạng điện xoay chiều dân dụng tại Việt Nam có tần số $f = 50\\text{ Hz}$ (tức thực hiện $50$ chu kì dao động trong $1\\text{ giây}$). Biết rằng trong mỗi chu kì dòng điện xoay chiều đổi chiều $2$ lần, hỏi trong $1\\text{ giây}$ dòng điện này đổi chiều bao nhiêu lần?",
        example_answer="Trong $1\\text{ giây}$ có $50$ chu kì, mỗi chu kì dòng điện đổi chiều $2$ lần nên số lần dòng điện đổi chiều trong $1\\text{ giây}$ là $N = 2f = 2 \\cdot 50 = 100$ lần.",
        real_life="Các tổ máy phát điện tại nhà máy thủy điện Hòa Bình, Sơn La dùng sức nước làm quay rôto (nam châm điện khổng lồ) bên trong stato (hệ thống cuộn dây) để tạo ra dòng điện xoay chiều hòa vào lưới điện quốc gia.",
        quiz=[
            mcq("biet", "Nguyên tắc hoạt động của máy phát điện xoay chiều dựa trên hiện tượng vật lí nào?", ["Hiện tượng cảm ứng điện từ", "Hiện tượng nhiễm điện do cọ xát", "Hiện tượng phản xạ toàn phần", "Tác dụng hóa học của dòng điện"], 0, "Máy phát điện xoay chiều hoạt động dựa trên hiện tượng cảm ứng điện từ khi số đường sức từ qua cuộn dây biến thiên tuần hoàn."),
            mcq("biet", "Hai bộ phận chính không thể thiếu của mọi máy phát điện xoay chiều là gì?", ["Nam châm và cuộn dây dẫn", "Bình điện phân và biến trở", "Ampe kế và vôn kế", "Tụ điện và cầu chì"], 0, "Mọi máy phát điện xoay chiều đều có hai bộ phận chính là nam châm (tạo từ trường) và cuộn dây dẫn (tạo dòng điện cảm ứng)."),
            mcq("hieu", "Vì sao khi cho một khung dây dẫn kín quay đều trong từ trường của một nam châm thì dòng điện cảm ứng trong khung lại là dòng điện xoay chiều?", ["Vì số đường sức từ xuyên qua tiết diện khung dây luân phiên tăng rồi giảm và đổi chiều xuyên qua mặt khung sau mỗi nửa vòng quay", "Vì khung dây bị nóng lên khi quay", "Vì từ trường của nam châm tự động biến mất khi khung dây quay", "Vì trọng lực tác dụng lên khung dây thay đổi"], 0, "Khi khung dây quay, số đường sức từ xuyên qua khung luân phiên tăng và giảm tuần hoàn làm dòng điện cảm ứng liên tục đổi chiều."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dòng điện xoay chiều và máy phát điện:", [
                "Dòng điện do pin và ắc quy cung cấp là dòng điện một chiều, còn dòng điện ở ổ cắm gia đình là dòng điện xoay chiều.",
                "Trong máy phát điện xoay chiều, bộ phận đứng yên gọi là stato và bộ phận quay gọi là rôto.",
                "Máy phát điện xoay chiều biến đổi trực tiếp cơ năng thành điện năng.",
                "Dòng điện xoay chiều tần số $50\\text{ Hz}$ giữ nguyên một chiều duy nhất trong suốt thời gian hoạt động.",
            ], [True, True, True, False], "Ý d) sai vì dòng điện xoay chiều luôn luân phiên đổi chiều ($100$ lần mỗi giây đối với tần số $50\\text{ Hz}$)."),
            short("vandung", "Dòng điện xoay chiều trong mạng điện gia đình ở Việt Nam có tần số $f = 50\\text{ Hz}$. Biết mỗi chu kì dòng điện đổi chiều $2$ lần, hỏi trong $1\\text{ giây}$ dòng điện đổi chiều bao nhiêu lần?", ["100"], "Số lần đổi chiều trong $1\\text{ giây}$ là $2f = 2 \\cdot 50 = 100$ lần.", unit="lần"),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 14: Tác dụng của dòng điện xoay chiều và máy biến áp",
        icon="🗼",
        description="Các tác dụng của dòng điện xoay chiều, cấu tạo và công thức máy biến áp U₁/U₂ = N₁/N₂, bài toán truyền tải điện năng đi xa.",
        requirements=[
            "Nêu được các tác dụng của dòng điện xoay chiều: tác dụng nhiệt, tác dụng phát sáng, tác dụng từ (lực từ đổi chiều khi dòng điện đổi chiều) và tác dụng sinh lí.",
            "Trình bày được cấu tạo của máy biến áp (hai cuộn dây có số vòng $N_1 \\ne N_2$ quấn trên lõi sắt pha silic chung) và vận dụng công thức $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2}$.",
            "Giải thích được vì sao khi truyền tải điện năng đi xa phải dùng máy biến áp để tăng hiệu điện thế dựa trên công thức hao phí $\\mathcal{P}_{\\text{hp}} = \\dfrac{\\mathcal{P}^2 R}{U^2}$.",
        ],
        definition="Dòng điện xoay chiều có tác dụng nhiệt, phát sáng, từ và sinh lí. Máy biến áp là thiết bị dùng để biến đổi hiệu điện thế của dòng điện xoay chiều theo hệ thức: $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2}$.",
        theory=(
            "### 1. Tác dụng của dòng điện xoay chiều\n"
            "- Dòng điện xoay chiều gây ra **tác dụng nhiệt** (bàn là, bếp hồng ngoại), **tác dụng phát sáng** (bóng đèn), **tác dụng từ** (nam châm điện xoay chiều có cực từ luân phiên đổi chiều) và **tác dụng sinh lí**.\n"
            "- Điểm khác với dòng điện một chiều: khi dòng điện xoay chiều đổi chiều thì **lực từ tác dụng lên nam châm cũng đổi chiều** (và dòng điện xoay chiều không dùng trực tiếp để mạ điện).\n\n"
            "### 2. Máy biến áp và Truyền tải điện năng đi xa\n"
            "- **Máy biến áp**: gồm cuộn sơ cấp ($N_1$ vòng, đặt vào điện áp xoay chiều $U_1$) và cuộn thứ cấp ($N_2$ vòng, lấy ra điện áp xoay chiều $U_2$) quấn trên một lõi sắt (thép) pha silic chung:\n"
            "  $$\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2}$$\n"
            "  - Nếu $N_2 > N_1 \\implies U_2 > U_1$: **máy tăng áp**.\n"
            "  - Nếu $N_2 < N_1 \\implies U_2 < U_1$: **máy hạ áp**.\n"
            "  - *Lưu ý*: Máy biến áp **chỉ hoạt động với dòng điện xoay chiều**, không hoạt động với dòng điện một chiều không đổi.\n"
            "- **Công suất hao phí do tỏa nhiệt trên đường dây truyền tải**: $\\mathcal{P}_{\\text{hp}} = I^2 R = \\dfrac{\\mathcal{P}^2 R}{U^2}$ (tăng $U$ lên $k$ lần thì công suất hao phí giảm $k^2$ lần)."
        ),
        formulas=[
            G(
                "Công thức Máy biến áp và Truyền tải điện năng",
                F("Hệ thức hiệu điện thế và số vòng dây máy biến áp", "$\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} \\implies U_2 = U_1 \\cdot \\dfrac{N_2}{N_1}$", "Nếu $N_2 > N_1$ là máy tăng áp; nếu $N_2 < N_1$ là máy hạ áp."),
                F("Công suất hao phí trên đường dây truyền tải", "$\\mathcal{P}_{\\text{hp}} = \\dfrac{\\mathcal{P}^2 \\cdot R}{U^2}$", "Khi tăng hiệu điện thế truyền tải $U$ lên $10$ lần thì công suất hao phí $\\mathcal{P}_{\\text{hp}}$ giảm đi $10^2 = 100$ lần."),
            )
        ],
        example="Cuộn sơ cấp của một máy biến áp có $N_1 = 2200$ vòng dây được nối vào mạng điện xoay chiều có hiệu điện thế $U_1 = 220\\text{ V}$. Muốn lấy ra ở cuộn thứ cấp hiệu điện thế $U_2 = 12\\text{ V}$ để nạp ắc quy thì cuộn thứ cấp phải có bao nhiêu vòng dây ($N_2$)?",
        example_answer="Áp dụng công thức máy biến áp: $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} \\implies N_2 = N_1 \\cdot \\dfrac{U_2}{U_1} = 2200 \\cdot \\dfrac{12}{220} = 120$ vòng dây.",
        real_life="Đường dây truyền tải điện Bắc – Nam nâng hiệu điện thế lên tới $500\\text{ kV}$ ($500\\,000\\text{ V}$) nhờ các trạm biến áp tăng áp để giảm tối đa điện năng hao phí tỏa nhiệt trên đường dây dài hàng nghìn kilômét, sau đó hạ áp xuống $220\\text{ V}$ trước khi đưa vào từng hộ gia đình.",
        quiz=[
            mcq("biet", "Hệ thức liên hệ giữa hiệu điện thế ở hai đầu cuộn sơ cấp ($U_1$), cuộn thứ cấp ($U_2$) và số vòng dây tương ứng ($N_1, N_2$) của một máy biến áp lí tưởng là gì?", ["$\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2}$", "$\\dfrac{U_1}{U_2} = \\dfrac{N_2}{N_1}$", "$U_1 \\cdot U_2 = N_1 \\cdot N_2$", "$U_1 + N_1 = U_2 + N_2$"], 0, "Hiệu điện thế ở hai đầu mỗi cuộn dây của máy biến áp tỉ lệ thuận với số vòng dây của mỗi cuộn: $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2}$."),
            mcq("biet", "Biện pháp hiệu quả và kinh tế nhất để giảm công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện năng đi xa là gì?", ["Dùng máy biến áp tăng hiệu điện thế $U$ trước khi truyền tải trên đường dây", "Làm dây dẫn bằng bạc nguyên chất có đường kính thật lớn", "Xây nhà máy điện ngay bên trong từng ngôi nhà", "Giảm hiệu điện thế truyền tải xuống thật nhỏ"], 0, "Vì $\\mathcal{P}_{\\text{hp}} = \\dfrac{\\mathcal{P}^2 R}{U^2}$ tỉ lệ nghịch với $U^2$, nên tăng hiệu điện thế $U$ giúp giảm hao phí mạnh nhất mà không tốn kim loại làm dây."),
            mcq("hieu", "Nếu ta nối hai đầu cuộn sơ cấp của một máy biến áp vào hai cực của một bình ắc quy (nguồn điện một chiều không đổi $U_1 = 12\\text{ V}$) thì hiệu điện thế $U_2$ ở hai đầu cuộn thứ cấp sẽ bằng bao nhiêu?", ["$0\\text{ V}$ (vì dòng điện một chiều không đổi không tạo ra từ trường biến thiên qua cuộn thứ cấp)", "$220\\text{ V}$", "$12\\text{ V}$", "$24\\text{ V}$"], 0, "Dòng điện một chiều không đổi chỉ tạo ra từ trường không đổi, số đường sức từ qua cuộn thứ cấp không biến thiên nên không có cảm ứng điện từ ($U_2 = 0\\text{ V}$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dòng điện xoay chiều và máy biến áp:", [
                "Dòng điện xoay chiều có đầy đủ các tác dụng nhiệt, phát sáng, từ và sinh lí.",
                "Máy biến áp có số vòng cuộn thứ cấp lớn hơn cuộn sơ cấp ($N_2 > N_1$) là máy tăng áp.",
                "Khi tăng hiệu điện thế truyền tải lên gấp $10$ lần thì công suất hao phí trên đường dây giảm đi $100$ lần.",
                "Có thể dùng trực tiếp dòng điện xoay chiều $220\\text{ V}$ để mạ vàng cho đồ trang sức trong bình điện phân.",
            ], [True, True, True, False], "Ý d) sai vì dòng điện xoay chiều liên tục đổi chiều nên không thể dùng trực tiếp để mạ điện (phải dùng dòng điện một chiều)."),
            short("vandung", "Một máy biến áp có cuộn sơ cấp $N_1 = 1000$ vòng dây và cuộn thứ cấp $N_2 = 200$ vòng dây. Khi đặt vào hai đầu cuộn sơ cấp hiệu điện thế xoay chiều $U_1 = 220\\text{ V}$ thì hiệu điện thế xoay chiều ở hai đầu cuộn thứ cấp $U_2$ bằng bao nhiêu Vôn ($\\text{V}$)?", ["44"], "Ta có $U_2 = U_1 \\cdot \\dfrac{N_2}{N_1} = 220 \\cdot \\dfrac{200}{1000} = 44\\text{ V}$.", unit="V"),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 15: Vòng năng lượng trên Trái Đất và năng lượng hóa thạch",
        icon="⛽",
        description="Vai trò của Mặt Trời trong chu trình năng lượng trên Trái Đất (quang hợp, vòng tuần hoàn nước, gió) và nhiên liệu hóa thạch.",
        requirements=[
            "Mô tả được vòng năng lượng trên Trái Đất và giải thích vì sao phần lớn các nguồn năng lượng trên Trái Đất đều có nguồn gốc từ năng lượng Mặt Trời.",
            "Trình bày được sự hình thành của các nguồn năng lượng hóa thạch (than đá, dầu mỏ, khí thiên nhiên) từ xác sinh vật cổ đại.",
            "Phân tích được ưu điểm và các tác động tiêu cực của việc đốt nhiên liệu hóa thạch (phát thải khí nhà kính $\\text{CO}_2$, ô nhiễm môi trường, nguy cơ cạn kiệt).",
        ],
        definition="Mặt Trời là nguồn cung cấp năng lượng chủ yếu cho sự sống và các chu trình tự nhiên trên Trái Đất (như quang hợp, vòng tuần hoàn của nước, chuyển động của gió). Năng lượng hóa thạch (than đá, dầu mỏ, khí tự nhiên) là nguồn năng lượng không tái tạo được hình thành qua hàng trăm triệu năm.",
        theory=(
            "### 1. Vòng năng lượng trên Trái Đất\n"
            "- **Vòng năng lượng qua sinh vật (Quang hợp)**: Thực vật hấp thụ quang năng của Mặt Trời để chuyển hóa $\\text{CO}_2$ và $\\text{H}_2\\text{O}$ thành chất hữu cơ (hóa năng) và giải phóng $\\text{O}_2$; động vật và con người lấy năng lượng từ thực vật.\n"
            "- **Vòng tuần hoàn của nước và gió**: Bức xạ Mặt Trời làm nước biển bay hơi tạo mây, mưa rơi xuống các hồ trên cao tạo ra **thế năng của nước** (thủy điện); đồng thời sự đốt nóng không đều các vùng khí quyển tạo ra **động năng của gió**.\n\n"
            "### 2. Năng lượng hóa thạch\n"
            "- Gồm **than đá, dầu mỏ và khí thiên nhiên**, hình thành từ xác thực vật và động vật bị chôn vùi dưới lòng đất cách đây hàng trăm triệu năm (nên thực chất là năng lượng Mặt Trời tích lũy từ thời cổ đại).\n"
            "- **Ưu điểm**: trữ lượng tập trung, dễ khai thác, vận chuyển, cất trữ và công nghệ đốt phát điện đã hoàn thiện.\n"
            "- **Nhược điểm**: là nguồn năng lượng **không tái tạo** (sẽ cạn kiệt) và khi đốt cháy thải ra lượng lớn khí nhà kính ($\\text{CO}_2, \\text{SO}_2, \\text{NO}_x$) gây **hiệu ứng nhà kính**, biến đổi khí hậu và mưa axit."
        ),
        formulas=[
            G(
                "Chu trình chuyển hóa năng lượng từ Mặt Trời",
                F("Chuỗi chuyển hóa năng lượng thủy điện", "$\\text{Quang năng \\& Nhiệt năng Mặt Trời} \\longrightarrow \\text{Thế năng nước (mưa trên cao)} \\longrightarrow \\text{Động năng dòng nước} \\longrightarrow \\text{Điện năng}$", "Năng lượng thủy điện và năng lượng gió đều bắt nguồn từ năng lượng Mặt Trời."),
                F("Chuỗi chuyển hóa năng lượng hóa thạch", "$\\text{Quang năng Mặt Trời (cổ đại)} \\longrightarrow \\text{Hóa năng (than, dầu, khí)} \\longrightarrow \\text{Nhiệt năng (đốt cháy)} \\longrightarrow \\text{Cơ năng / Điện năng}$", "Quá trình đốt nhiên liệu hóa thạch phát thải nhiều khí $\\text{CO}_2$ làm tăng nhiệt độ Trái Đất."),
            )
        ],
        example="Hãy giải thích vì sao năng lượng của dòng nước chảy trong các nhà máy thủy điện thực chất lại có nguồn gốc từ năng lượng Mặt Trời?",
        example_answer="Nhờ năng lượng nhiệt của bức xạ Mặt Trời chiếu xuống đại dương, nước biển mới bay hơi bay lên cao tạo thành mây và rơi xuống thành mưa ở các vùng núi cao (tích trữ thế năng trọng trường của nước trong hồ thủy điện). Do đó năng lượng thủy điện có nguồn gốc từ Mặt Trời.",
        real_life="Các nhà máy nhiệt điện chạy than và các phương tiện giao thông chạy xăng dầu hiện vẫn cung cấp phần lớn năng lượng thế giới nhưng đang dần được chuyển dịch sang năng lượng sạch để giảm phát thải ròng về $0$ (Net Zero).",
        quiz=[
            mcq("biet", "Nguồn năng lượng nào sau đây thuộc nhóm **năng lượng hóa thạch** (không tái tạo)?", ["Than đá, dầu mỏ và khí thiên nhiên", "Năng lượng ánh sáng Mặt Trời", "Năng lượng của sức gió", "Năng lượng thủy triều"], 0, "Than đá, dầu mỏ và khí thiên nhiên là các nhiên liệu hóa thạch được hình thành qua hàng trăm triệu năm."),
            mcq("biet", "Phần lớn các dạng năng lượng trong vòng năng lượng trên Trái Đất (như năng lượng gió, năng lượng dòng nước, năng lượng sinh khối) đều bắt nguồn từ đâu?", ["Năng lượng bức xạ từ Mặt Trời", "Năng lượng từ tâm Mặt Trăng", "Năng lượng do con người tự tạo ra từ hư không", "Năng lượng từ các sao chổi"], 0, "Bức xạ Mặt Trời là nguồn gốc của quá trình quang hợp, vòng tuần hoàn nước và sự hình thành gió trên Trái Đất."),
            mcq("hieu", "Tác hại lớn nhất đối với môi trường toàn cầu khi đốt một lượng khổng lồ nhiên liệu hóa thạch (than đá, xăng dầu) là gì?", ["Thải ra lượng lớn khí $\\text{CO}_2$ và các khí độc hại gây hiệu ứng nhà kính, biến đổi khí hậu và ô nhiễm không khí", "Làm Trái Đất quay quanh trục nhanh hơn", "Làm tăng lượng khí ôxi trong khí quyển", "Làm giảm mực nước biển trên toàn cầu"], 0, "Đốt nhiên liệu hóa thạch giải phóng khí nhà kính ($\\text{CO}_2$) và các khí gây mưa axit ($\\text{SO}_2, \\text{NO}_x$), dẫn đến nóng lên toàn cầu."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về vòng năng lượng trên Trái Đất và năng lượng hóa thạch:", [
                "Thông qua quá trình quang hợp, cây xanh chuyển hóa quang năng của Mặt Trời thành hóa năng tích trữ trong chất hữu cơ.",
                "Năng lượng hóa thạch là nguồn năng lượng vô tận, có thể tự bổ sung lại chỉ trong vài ngày.",
                "Sự chênh lệch nhiệt độ giữa các vùng khí quyển do Mặt Trời chiếu sáng không đều tạo ra gió.",
                "Giá thành nhiên liệu hóa thạch chưa tính hết các chi phí khắc phục hậu quả ô nhiễm môi trường và biến đổi khí hậu.",
            ], [True, False, True, True], "Ý b) sai vì nhiên liệu hóa thạch cần hàng trăm triệu năm để hình thành nên là nguồn năng lượng không tái tạo, có nguy cơ cạn kiệt."),
            short("vandung", "Có mấy loại nhiên liệu hóa thạch chính thường dùng trong công nghiệp và đời sống (than đá, dầu mỏ, khí thiên nhiên)?", ["3"], "Có $3$ loại nhiên liệu hóa thạch chính: than đá, dầu mỏ và khí thiên nhiên."),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 16: Năng lượng tái tạo",
        icon="☀️",
        description="Các nguồn năng lượng tái tạo (mặt trời, gió, nước, địa nhiệt, thủy triều, sinh khối), ưu nhược điểm và giải pháp bảo vệ môi trường.",
        requirements=[
            "Nêu được năng lượng tái tạo là năng lượng từ những nguồn liên tục được bổ sung thông qua các quá trình tự nhiên (mặt trời, gió, dòng nước, thủy triều, địa nhiệt, sinh khối).",
            "Trình bày được sự chuyển hóa năng lượng trong pin mặt trời (quang năng $\\to$ điện năng), tua-bin gió (động năng gió $\\to$ điện năng) và nhà máy điện địa nhiệt.",
            "So sánh được ưu điểm (sạch, ít phát thải khí nhà kính, không cạn kiệt) và hạn chế (phụ thuộc thời tiết, chi phí đầu tư ban đầu và lưu trữ) của năng lượng tái tạo.",
        ],
        definition="Năng lượng tái tạo (năng lượng sạch) là năng lượng thu được từ những nguồn tự nhiên liên tục được bổ sung và không bị cạn kiệt theo thời gian sử dụng của con người, bao gồm năng lượng mặt trời, năng lượng gió, năng lượng nước (thủy điện, sóng biển, thủy triều), địa nhiệt và sinh khối.",
        theory=(
            "### 1. Các nguồn năng lượng tái tạo chủ yếu\n"
            "1. **Năng lượng mặt trời**: dùng tấm thu nhiệt đun nước nóng (quang năng $\\to$ nhiệt năng) hoặc dùng **tấm pin mặt trời** biến đổi trực tiếp quang năng thành điện năng.\n"
            "2. **Năng lượng gió**: dùng cánh quạt **tua-bin gió** biến đổi động năng của gió thành cơ năng quay máy phát điện.\n"
            "3. **Năng lượng nước**: gồm thủy điện trên sông, năng lượng **thủy triều** (do lực hấp dẫn của Mặt Trăng và Mặt Trời) và năng lượng sóng biển.\n"
            "4. **Năng lượng địa nhiệt**: khai thác nguồn nhiệt năng có sẵn sâu trong lòng Trái Đất.\n"
            "5. **Năng lượng sinh khối (Biomass)**: từ phụ phẩm nông – lâm nghiệp (trấu, mùn cưa, bã mía), khí sinh học (biogas), xăng sinh học ($\\text{E5}, \\text{E10}$).\n\n"
            "### 2. Ưu điểm và thách thức của năng lượng tái tạo\n"
            "- **Ưu điểm**: có trữ lượng dồi dào gần như vô tận, rất ít phát thải khí nhà kính ($\\text{CO}_2$), bảo vệ môi trường bền vững.\n"
            "- **Thách thức**: phụ thuộc nhiều vào thời tiết, thời gian trong ngày và vị trí địa lí (ví dụ: điện mặt trời không phát vào ban đêm, điện gió phụ thuộc tốc độ gió), cần hệ thống lưu trữ năng lượng và xử lí rác thải tấm pin hết hạn."
        ),
        formulas=[
            G(
                "Chuyển hóa năng lượng trong các thiết bị năng lượng tái tạo",
                F("Pin quang điện (Pin mặt trời)", "$\\text{Quang năng (Ánh sáng Mặt Trời)} \\longrightarrow \\text{Điện năng một chiều (DC)}$", "Bình nước nóng năng lượng mặt trời chuyển hóa: $\\text{Quang năng} \\longrightarrow \\text{Nhiệt năng}$."),
                F("Tua-bin điện gió", "$\\text{Động năng của gió} \\longrightarrow \\text{Động năng quay cánh quạt} \\longrightarrow \\text{Điện năng}$", "Công suất điện gió tăng rất nhanh khi tốc độ gió $v$ tăng."),
            )
        ],
        example="Hãy nêu sự chuyển hóa năng lượng chính diễn ra trong: (a) Tấm pin mặt trời lắp trên mái nhà; (b) Hầm ủ khí sinh học (Biogas) đun bếp ở trang trại chăn nuôi.",
        example_answer="(a) Trong tấm pin mặt trời: **quang năng** của ánh sáng Mặt Trời chuyển hóa trực tiếp thành **điện năng**. (b) Trong hầm Biogas: **năng lượng sinh khối (hóa năng)** của chất thải hữu cơ chuyển hóa thành hóa năng của khí mê-tan ($\\text{CH}_4$), khi đốt bếp chuyển hóa thành **nhiệt năng**.",
        real_life="Tại khu vực Đồng bằng sông Cửu Long (như Bạc Liêu, Sóc Trăng, Trà Vinh) và Nam Trung Bộ (Ninh Thuận, Bình Thuận), hàng trăm trụ tua-bin điện gió ngoài khơi và cánh đồng điện mặt trời đang cung cấp nguồn điện sạch lớn cho đất nước.",
        quiz=[
            mcq("biet", "Nguồn năng lượng nào dưới đây thuộc nhóm **năng lượng tái tạo**?", ["Năng lượng mặt trời, năng lượng gió và năng lượng địa nhiệt", "Than đá và dầu mỏ", "Khí đốt thiên nhiên", "Xăng A95 và dầu diesel"], 0, "Năng lượng mặt trời, gió và địa nhiệt tự nhiên liên tục được bổ sung nên là năng lượng tái tạo."),
            mcq("biet", "Tấm pin mặt trời (pin quang điện) lắp trên mái nhà hoạt động dựa trên sự chuyển hóa trực tiếp dạng năng lượng nào thành dạng năng lượng nào?", ["Chuyển hóa trực tiếp quang năng (năng lượng ánh sáng) thành điện năng", "Chuyển hóa động năng của gió thành nhiệt năng", "Chuyển hóa thế năng hấp dẫn thành hóa năng", "Chuyển hóa năng lượng âm thanh thành điện năng"], 0, "Tế bào quang điện trong tấm pin mặt trời biến đổi trực tiếp quang năng của ánh sáng Mặt Trời thành điện năng."),
            mcq("hieu", "Hạn chế lớn nhất của điện mặt trời và điện gió khi vận hành trong hệ thống điện là gì?", ["Công suất phát điện không ổn định do phụ thuộc vào thời tiết, ngày đêm và tốc độ gió", "Thải ra quá nhiều khí $\\text{CO}_2$ và khói bụi khi đang phát điện", "Nguồn ánh sáng Mặt Trời và gió sẽ cạn kiệt hoàn toàn sau vài năm", "Không thể biến đổi thành dòng điện xoay chiều"], 0, "Điện mặt trời chỉ phát ban ngày khi có nắng và điện gió phụ thuộc tốc độ gió, nên cần kết hợp hệ thống pin lưu trữ hoặc các nguồn điện điều tần khác."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về năng lượng tái tạo:", [
                "Năng lượng địa nhiệt là nguồn năng lượng thu được từ sức nóng bên trong lòng Trái Đất và không phụ thuộc vào thời tiết ngày hay đêm.",
                "Năng lượng thủy triều xuất hiện chủ yếu do lực hấp dẫn của Mặt Trăng và Mặt Trời tác dụng lên lớp nước đại dương trên Trái Đất.",
                "Sử dụng xăng sinh học E5 (pha $5\\%$ cồn sinh học ethanol từ sắn, mía) là một ứng dụng của năng lượng sinh khối.",
                "Đập thủy điện quy mô lớn hoàn toàn không gây ra bất kì tác động nào đến hệ sinh thái rừng và dòng chảy hạ lưu.",
            ], [True, True, True, False], "Ý d) sai vì xây dựng hồ thủy điện lớn có thể làm ngập diện tích rừng lớn và thay đổi dòng chảy, lượng phù sa ở hạ lưu nên cần đánh giá tác động môi trường kỹ lưỡng."),
            short("vandung", "Cho 5 nguồn năng lượng sau: (1) Năng lượng mặt trời, (2) Than đá, (3) Năng lượng gió, (4) Dầu mỏ, (5) Năng lượng địa nhiệt. Có bao nhiêu nguồn trong danh sách trên là **năng lượng tái tạo**?", ["3"], "Các nguồn (1) Mặt trời, (3) Gió và (5) Địa nhiệt là $3$ nguồn năng lượng tái tạo; còn than đá và dầu mỏ là nhiên liệu hóa thạch không tái tạo."),
        ],
        chapter_desc=CH4_DESC,
    ),
]
