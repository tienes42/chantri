"""Vật lý Lớp 11 (SGK Vật lí 11 - Kết nối tri thức với cuộc sống): 4 Chương - 23 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 11

CH1 = ("l11-ch01-dao-dong", "Chương I: Dao động", "Chương I · SGK Vật lí 11: Dao động điều hòa, độ lệch pha, vận tốc – gia tốc, năng lượng dao động và hiện tượng cộng hưởng.")
CH2 = ("l11-ch02-song", "Chương II: Sóng", "Chương II · SGK Vật lí 11: Sóng cơ, sóng ngang – sóng dọc, sóng điện từ, giao thoa sóng cơ, giao thoa ánh sáng và sóng dừng.")
CH3 = ("l11-ch03-dien-truong", "Chương III: Điện trường", "Chương III · SGK Vật lí 11: Định luật Coulomb, cường độ điện trường, điện trường đều, thế năng điện, điện thế – hiệu điện thế và tụ điện.")
CH4 = ("l11-ch04-dong-dien-mach-dien", "Chương IV: Dòng điện, mạch điện", "Chương IV · SGK Vật lí 11: Cường độ dòng điện, điện trở phụ thuộc nhiệt độ, suất điện động, định luật Ohm toàn mạch và năng lượng điện.")

LESSONS = [
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 1: Dao động điều hòa",
        icon="〰️",
        description="Khái niệm dao động cơ, phương trình dao động điều hòa x = A.cos(ωt + φ), biên độ A, chu kì T, tần số f và tần số góc ω.",
        requirements=[
            "Viết được phương trình li độ của dao động điều hòa $x = A\\cos(\\omega t + \\varphi)$ và nêu ý nghĩa, đơn vị của các đại lượng $x, A, \\omega, (\\omega t + \\varphi), \\varphi$.",
            "Tính được chiều dài quỹ đạo dao động $L = 2A$ và quãng đường vật đi được trong một chu kì $S_{1T} = 4A$.",
            "Vận dụng được công thức liên hệ giữa chu kì $T$, tần số $f$ và tần số góc $\\omega$: $\\omega = \\dfrac{2\\pi}{T} = 2\\pi f$.",
        ],
        definition="Dao động điều hòa là dao động trong đó li độ của vật là một hàm côsin (hay sin) của thời gian: $x = A\\cos(\\omega t + \\varphi)$, trong đó $A > 0$ là biên độ, $\\omega > 0$ là tần số góc ($\\text{rad/s}$) và $\\varphi$ là pha ban đầu ($\\text{rad}$).",
        theory=(
            "### 1. Phương trình và các đại lượng đặc trưng của dao động điều hòa\n"
            "- **Phương trình dao động điều hòa**: $x = A\\cos(\\omega t + \\varphi)$.\n"
            "  - **Li độ ($x$)**: độ dịch chuyển của vật khỏi vị trí cân bằng $O$ tại thời điểm $t$ ($-A \\le x \\le A$).\n"
            "  - **Biên độ ($A = x_{\\max} > 0$)**: độ lệch cực đại của vật so với vị trí cân bằng. **Chiều dài quỹ đạo**: $L = 2A$. **Quãng đường đi trong 1 chu kì**: $S_{1T} = 4A$.\n"
            "  - **Pha dao động ($\\omega t + \\varphi$)**: cho biết trạng thái (vị trí và chiều chuyển động) của vật tại thời điểm $t$ ($\\text{rad}$).\n"
            "  - **Pha ban đầu ($\\varphi \\in [-\\pi, \\pi]$)**: xác định trạng thái của vật ở thời điểm $t = 0$.\n\n"
            "### 2. Chu kì, Tần số và Tần số góc\n"
            "- **Chu kì ($T$)**: khoảng thời gian để vật thực hiện được một dao động toàn phần: $T = \\dfrac{t}{N}$ ($\\text{s}$).\n"
            "- **Tần số ($f$)**: số dao động toàn phần thực hiện được trong $1\\text{ giây}$: $f = \\dfrac{1}{T} = \\dfrac{N}{t}$ ($\\text{Hz}$).\n"
            "- **Tần số góc ($\\omega$)**: $\\omega = \\dfrac{2\\pi}{T} = 2\\pi f$ ($\\text{rad/s}$)."
        ),
        formulas=[
            G(
                "Phương trình và các đại lượng của dao động điều hòa",
                F("Phương trình li độ và Quỹ đạo dao động", "$x = A\\cos(\\omega t + \\varphi); \\qquad L = 2A; \\qquad S_{1T} = 4A$", "Trong đó $A > 0$ là biên độ, $L = 2A$ là chiều dài quỹ đạo từ biên âm $-A$ đến biên dương $+A$."),
                F("Chu kì, tần số và tần số góc", "$\\omega = \\dfrac{2\\pi}{T} = 2\\pi f; \\qquad T = \\dfrac{1}{f} = \\dfrac{t}{N}$", "Trong đó $T$ tính bằng $\\text{s}$, $f$ tính bằng $\\text{Hz}$, $\\omega$ tính bằng $\\text{rad/s}$."),
            )
        ],
        example="Một chất điểm dao động điều hòa có phương trình $x = 6\\cos\\left(4\\pi t + \\dfrac{\\pi}{3}\\right)\\text{ (cm)}$ (với $t$ tính bằng $\\text{s}$). Hãy xác định biên độ $A$, chiều dài quỹ đạo $L$, tần số góc $\\omega$, chu kì $T$, tần số $f$ và quãng đường vật đi được trong $1\\text{ giây}$.",
        example_answer="Từ phương trình ta có: biên độ $A = 6\\text{ cm}$, chiều dài quỹ đạo $L = 2A = 12\\text{ cm}$, tần số góc $\\omega = 4\\pi\\text{ rad/s}$. Chu kì là $T = \\dfrac{2\\pi}{\\omega} = \\dfrac{2\\pi}{4\\pi} = 0{,}5\\text{ s}$, tần số $f = \\dfrac{1}{T} = 2\\text{ Hz}$. Trong $1\\text{ s} = 2T$, quãng đường vật đi được là $S = 2 \\cdot 4A = 8 \\cdot 6 = 48\\text{ cm}$.",
        real_life="Chuyển động đung đưa góc nhỏ của quả lắc đồng hồ treo tường và dao động của pít-tông trong xi-lanh động cơ được mô tả chính xác bằng dao động điều hòa.",
        quiz=[
            mcq("biet", "Một chất điểm dao động điều hòa với biên độ $A$. Chiều dài quỹ đạo chuyển động $L$ và quãng đường vật đi được trong một chu kì $S_{1T}$ lần lượt là:", ["$L = 2A$ và $S_{1T} = 4A$", "$L = A$ và $S_{1T} = 2A$", "$L = 4A$ và $S_{1T} = 2A$", "$L = 2A$ và $S_{1T} = 2A$"], 0, "Vật dao động giữa hai biên $-A$ và $+A$ nên quỹ đạo dài $L = 2A$, còn trong 1 chu kì vật đi hết 1 vòng khép kín nên quãng đường là $S_{1T} = 4A$."),
            mcq("biet", "Hệ thức liên hệ giữa tần số góc $\\omega$, chu kì $T$ và tần số $f$ của một dao động điều hòa là gì?", ["$\\omega = \\dfrac{2\\pi}{T} = 2\\pi f$", "$\\omega = \\dfrac{\\pi}{T} = \\pi f$", "$\\omega = 2\\pi T = \\dfrac{2\\pi}{f}$", "$\\omega = \\dfrac{T}{2\\pi}$"], 0, "Trong dao động điều hòa, $\\omega = \\dfrac{2\\pi}{T} = 2\\pi f$."),
            mcq("hieu", "Một vật dao động điều hòa theo phương trình $x = 5\\cos(2\\pi t - \\dfrac{\\pi}{4})\\text{ (cm)}$. Tại thời điểm ban đầu $t = 0$, pha của dao động bằng bao nhiêu?", ["$-\\dfrac{\\pi}{4}\\text{ rad}$", "$2\\pi\\text{ rad}$", "$5\\text{ rad}$", "$0\\text{ rad}$"], 0, "Pha dao động là $(\\omega t + \\varphi)$; tại $t = 0$, pha dao động bằng pha ban đầu $\\varphi = -\\dfrac{\\pi}{4}\\text{ rad}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dao động điều hòa $x = A\\cos(\\omega t + \\varphi)$:", [
                "Biên độ $A$ và tần số góc $\\omega$ là các hằng số dương.",
                "Đại lượng $(\\omega t + \\varphi)$ được gọi là pha của dao động tại thời điểm $t$, cho phép xác định trạng thái dao động của vật.",
                "Trong một nửa chu kì ($\\dfrac{T}{2}$), quãng đường mà vật đi được luôn bằng $2A$ dù xuất phát từ bất kì vị trí nào.",
                "Khi vật đi qua vị trí cân bằng $O$ thì li độ của vật có độ lớn cực đại $|x| = A$.",
            ], [True, True, True, False], "Ý d) sai vì tại vị trí cân bằng $O$ thì li độ bằng không ($x = 0$), còn tại hai vị trí biên mới có $|x| = A$."),
            short("vandung", "Một vật dao động điều hòa với phương trình $x = 8\\cos(5\\pi t)\\text{ (cm)}$. Chiều dài quỹ đạo dao động $L$ của vật bằng bao nhiêu $\\text{cm}$?", ["16"], "Chiều dài quỹ đạo của dao động điều hòa là $L = 2A = 2 \\cdot 8 = 16\\text{ cm}$.", unit="cm"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 2: Mô tả dao động điều hòa. Độ lệch pha",
        icon="📊",
        description="Đồ thị li độ – thời gian (x – t) hình sin, cách xác định pha ban đầu φ và độ lệch pha Δφ giữa hai dao động cùng chu kì.",
        requirements=[
            "Đọc được biên độ $A$, chu kì $T$ và trạng thái xuất phát ($t = 0$) của vật từ đồ thị li độ – thời gian ($x - t$) có dạng đường hình sin.",
            "Xác định được pha ban đầu $\\varphi$: lúc $t = 0$ ở biên dương ($x = +A \\implies \\varphi = 0$), ở biên âm ($x = -A \\implies \\varphi = \\pi$), qua VTCB theo chiều dương ($\\varphi = -\\dfrac{\\pi}{2}$), qua VTCB theo chiều âm ($\\varphi = +\\dfrac{\\pi}{2}$).",
            "Tính được độ lệch pha giữa hai dao động cùng tần số $\\Delta\\varphi = \\varphi_2 - \\varphi_1 = \\dfrac{2\\pi \\Delta t}{T}$ và phân biệt hai dao động cùng pha, ngược pha, vuông pha.",
        ],
        definition="Đồ thị li độ – thời gian ($x - t$) của dao động điều hòa là một đường hình sin. Độ lệch pha giữa hai dao động điều hòa cùng chu kì (cùng tần số) bằng hiệu hai pha ban đầu của chúng: $\\Delta\\varphi = \\varphi_2 - \\varphi_1$.",
        theory=(
            "### 1. Đồ thị $x - t$ và Pha ban đầu $\\varphi$ tại các vị trí đặc biệt\n"
            "- Đồ thị $x(t) = A\\cos(\\omega t + \\varphi)$ là một đường hình sin tuần hoàn theo chu kì $T$.\n"
            "- Tại $t = 0$: $x_0 = A\\cos\\varphi$, chiều chuyển động quy định dấu của $\\varphi$:\n"
            "  - Nếu $x_0 = +A$ (biên dương): $\\varphi = 0$.\n"
            "  - Nếu $x_0 = -A$ (biên âm): $\\varphi = \\pi\\text{ rad}$.\n"
            "  - Nếu $x_0 = 0$ và đang đi theo chiều dương ($v_0 > 0$): $\\varphi = -\\dfrac{\\pi}{2}\\text{ rad}$.\n"
            "  - Nếu $x_0 = 0$ và đang đi theo chiều âm ($v_0 < 0$): $\\varphi = +\\dfrac{\\pi}{2}\\text{ rad}$.\n\n"
            "### 2. Độ lệch pha giữa hai dao động cùng chu kì $T$\n"
            "- Nếu dao động 2 trễ thời gian $\\Delta t$ so với dao động 1 thì độ lệch pha là:\n"
            "  $$\\Delta\\varphi = \\varphi_1 - \\varphi_2 = \\omega \\Delta t = \\dfrac{2\\pi \\Delta t}{T}$$\n"
            "  - **Cùng pha**: $\\Delta\\varphi = k2\\pi$ (hai đồ thị đạt đỉnh cùng lúc).\n"
            "  - **Ngược pha**: $\\Delta\\varphi = (2k + 1)\\pi$ (khi vật 1 ở biên $+A_1$ thì vật 2 ở biên $-A_2$).\n"
            "  - **Vuông pha**: $\\Delta\\varphi = (2k + 1)\\dfrac{\\pi}{2}$ (khi vật 1 ở biên thì vật 2 qua VTCB)."
        ),
        formulas=[
            G(
                "Pha ban đầu và Độ lệch pha giữa hai dao động",
                F("Các giá trị pha ban đầu φ đặc biệt lúc t = 0", "$x_0 = +A \\iff \\varphi = 0; \\quad x_0 = -A \\iff \\varphi = \\pi; \\quad x_0 = 0 \\ (v > 0) \\iff \\varphi = -\\dfrac{\\pi}{2}; \\quad x_0 = 0 \\ (v < 0) \\iff \\varphi = +\\dfrac{\\pi}{2}$", "Tổng quát tại $t = 0$: $\\cos\\varphi = \\dfrac{x_0}{A}$ (với $\\varphi < 0$ khi $v_0 > 0$ và $\\varphi > 0$ khi $v_0 < 0$)."),
                F("Độ lệch pha theo độ lệch thời gian Δt", "$\\Delta\\varphi = |\\varphi_2 - \\varphi_1| = \\dfrac{2\\pi \\Delta t}{T}$", "Cùng pha: $\\Delta t = kT$; ngược pha: $\\Delta t = \\left(k + \\dfrac{1}{2}\\right)T$; vuông pha: $\\Delta t = \\left(k + \\dfrac{1}{2}\\right)\\dfrac{T}{2}$."),
            )
        ],
        example="Hai con lắc đơn có cùng chu kì dao động $T = 2\\text{ s}$. Con lắc thứ nhất đi qua vị trí biên dương sớm hơn con lắc thứ hai một khoảng thời gian $\\Delta t = 0{,}5\\text{ s}$. Hãy tính độ lệch pha $\\Delta\\varphi$ giữa hai dao động theo đơn vị radian và cho biết mối quan hệ pha của chúng.",
        example_answer="Độ lệch pha giữa hai dao động là $\\Delta\\varphi = \\dfrac{2\\pi \\Delta t}{T} = \\dfrac{2\\pi \\cdot 0{,}5}{2} = \\dfrac{\\pi}{2}\\text{ rad}$. Vậy hai dao động vuông pha với nhau (dao động thứ nhất sớm pha hơn dao động thứ hai góc $\\dfrac{\\pi}{2}\\text{ rad}$).",
        real_life="Màn hình máy hiện sóng (Oscilloscope) và máy đo điện tâm đồ hiển thị đồ thị dao động theo thời gian thực để kĩ sư và bác sĩ so sánh biên độ, chu kì và độ lệch pha giữa các tín hiệu.",
        quiz=[
            mcq("biet", "Đồ thị biểu diễn sự phụ thuộc của li độ $x$ vào thời gian $t$ ($x - t$) của một vật dao động điều hòa có dạng đường gì?", ["Đường hình sin", "Đường thẳng đi qua gốc tọa độ", "Đường tròn tâm $O$", "Đường hypebol"], 0, "Vì $x = A\\cos(\\omega t + \\varphi)$ nên đồ thị $x - t$ là một đường hình sin."),
            mcq("biet", "Hai dao động điều hòa cùng tần số có pha ban đầu lần lượt là $\\varphi_1 = \\dfrac{\\pi}{6}\\text{ rad}$ và $\\varphi_2 = -\\dfrac{5\\pi}{6}\\text{ rad}$. Hai dao động này có mối quan hệ pha như thế nào?", ["Ngược pha nhau (vì $\\Delta\\varphi = \\varphi_1 - \\varphi_2 = \\pi\\text{ rad}$)", "Cùng pha nhau", "Vuông pha nhau", "Lệch pha nhau góc $\\dfrac{\\pi}{3}\\text{ rad}$"], 0, "Ta có $\\Delta\\varphi = \\varphi_1 - \\varphi_2 = \\dfrac{\\pi}{6} - \\left(-\\dfrac{5\\pi}{6}\\right) = \\pi\\text{ rad}$, nên hai dao động ngược pha nhau."),
            mcq("hieu", "Một vật dao động điều hòa có phương trình $x = A\\cos(\\omega t + \\varphi)$. Nếu chọn gốc thời gian $t = 0$ lúc vật đi qua vị trí cân bằng $O$ ($x_0 = 0$) theo chiều dương ($v_0 > 0$) thì pha ban đầu $\\varphi$ bằng bao nhiêu?", ["$\\varphi = -\\dfrac{\\pi}{2}\\text{ rad}$", "$\\varphi = +\\dfrac{\\pi}{2}\\text{ rad}$", "$\\varphi = 0\\text{ rad}$", "$\\varphi = \\pi\\text{ rad}$"], 0, "Tại $t = 0$: $x_0 = A\\cos\\varphi = 0$ và $v_0 = -\\omega A\\sin\\varphi > 0 \\implies \\sin\\varphi < 0 \\implies \\varphi = -\\dfrac{\\pi}{2}\\text{ rad}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đồ thị và độ lệch pha của dao động điều hòa:", [
                "Nếu tại $t = 0$ vật bắt đầu dao động từ vị trí biên dương ($x_0 = +A$) thì pha ban đầu $\\varphi = 0$.",
                "Khoảng thời gian ngắn nhất giữa hai đỉnh dương liên tiếp trên đồ thị $x - t$ chính bằng một chu kì $T$.",
                "Hai dao động ngược pha luôn đi qua vị trí biên dương tại cùng một thời điểm.",
                "Nếu dao động 2 đạt cực đại trễ hơn dao động 1 đúng $\\dfrac{T}{2}$ thì hai dao động ngược pha nhau ($\\Delta\\varphi = \\pi\\text{ rad}$).",
            ], [True, True, False, True], "Ý c) sai vì khi hai dao động ngược pha, lúc vật 1 ở biên dương ($+A_1$) thì vật 2 đang ở biên âm ($-A_2$)."),
            short("vandung", "Hai dao động điều hòa cùng chu kì $T = 1{,}2\\text{ s}$. Dao động thứ nhất đạt giá trị cực đại sớm hơn dao động thứ hai một khoảng thời gian $\\Delta t = 0{,}6\\text{ s}$. Độ lệch pha $\\Delta\\varphi$ giữa hai dao động bằng bao nhiêu độ ($^\\circ$, biết $\\pi\\text{ rad} = 180^\\circ$)?", ["180"], "Ta có $\\Delta\\varphi = \\dfrac{360^\\circ \\cdot \\Delta t}{T} = \\dfrac{360^\\circ \\cdot 0{,}6}{1{,}2} = 180^\\circ$ (ngược pha).", unit="độ"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 3: Vận tốc, gia tốc trong dao động điều hòa",
        icon="🚀",
        description="Phương trình vận tốc v = -ωA.sin(ωt + φ) và gia tốc a = -ω²x, giá trị cực đại v_max = ωA, a_max = ω²A và hệ thức độc lập thời gian.",
        requirements=[
            "Viết được phương trình vận tốc $v = -\\omega A\\sin(\\omega t + \\varphi) = \\omega A\\cos\\left(\\omega t + \\varphi + \\dfrac{\\pi}{2}\\right)$ và phương trình gia tốc $a = -\\omega^2 x = -\\omega^2 A\\cos(\\omega t + \\varphi)$.",
            "Nêu được quan hệ pha giữa $x, v, a$ ($v$ sớm pha $\\dfrac{\\pi}{2}$ so với $x$; $a$ ngược pha với $x$) và giá trị cực đại $v_{\\max} = \\omega A$ (tại VTCB), $a_{\\max} = \\omega^2 A$ (tại hai biên).",
            "Vận dụng được các hệ thức độc lập với thời gian $A^2 = x^2 + \\dfrac{v^2}{\\omega^2}$ và $\\left(\\dfrac{v}{v_{\\max}}\\right)^2 + \\left(\\dfrac{a}{a_{\\max}}\\right)^2 = 1$.",
        ],
        definition="Trong dao động điều hòa $x = A\\cos(\\omega t + \\varphi)$, vận tốc của vật là $v = x'(t) = -\\omega A\\sin(\\omega t + \\varphi)$ (có tốc độ cực đại $v_{\\max} = \\omega A$ tại vị trí cân bằng) và gia tốc của vật là $a = v'(t) = -\\omega^2 x$ (luôn hướng về vị trí cân bằng và có độ lớn cực đại $a_{\\max} = \\omega^2 A$ tại vị trí biên).",
        theory=(
            "### 1. Vận tốc trong dao động điều hòa\n"
            "- Phương trình: $v = -\\omega A\\sin(\\omega t + \\varphi) = \\omega A\\cos\\left(\\omega t + \\varphi + \\dfrac{\\pi}{2}\\right)$.\n"
            "- Vận tốc $\\vec{v}$ luôn cùng chiều chuyển động và **sớm pha $\\dfrac{\\pi}{2}$ so với li độ $x$**.\n"
            "- **Tại vị trí cân bằng ($x = 0$)**: tốc độ đạt cực đại $|v|_{\\max} = v_{\\max} = \\omega A$.\n"
            "- **Tại hai vị trí biên ($x = \\pm A$)**: vận tốc bằng không ($v = 0$).\n\n"
            "### 2. Gia tốc và Hệ thức độc lập với thời gian\n"
            "- Phương trình: $a = -\\omega^2 x = -\\omega^2 A\\cos(\\omega t + \\varphi) = \\omega^2 A\\cos(\\omega t + \\varphi + \\pi)$.\n"
            "- Vectơ gia tốc $\\vec{a}$ luôn **hướng về vị trí cân bằng $O$**, có độ lớn tỉ lệ với độ lớn li độ ($|a| = \\omega^2 |x|$); gia tốc $a$ **ngược pha với li độ $x$** và **sớm pha $\\dfrac{\\pi}{2}$ so với vận tốc $v$**.\n"
            "- **Tại VTCB ($x = 0$)**: $a = 0$. **Tại hai biên ($x = \\pm A$)**: độ lớn gia tốc đạt cực đại $|a|_{\\max} = a_{\\max} = \\omega^2 A$.\n"
            "- **Hệ thức độc lập với thời gian**:\n"
            "  $$A^2 = x^2 + \\dfrac{v^2}{\\omega^2} \\iff \\left(\\dfrac{x}{A}\\right)^2 + \\left(\\dfrac{v}{v_{\\max}}\\right)^2 = 1; \\qquad \\left(\\dfrac{v}{v_{\\max}}\\right)^2 + \\left(\\dfrac{a}{a_{\\max}}\\right)^2 = 1$$"
        ),
        formulas=[
            G(
                "Vận tốc, Gia tốc và Hệ thức độc lập thời gian",
                F("Giá trị cực đại của vận tốc và gia tốc", "$v_{\\max} = \\omega A \\ (\\text{tại } x = 0); \\qquad a_{\\max} = \\omega^2 A = \\omega v_{\\max} \\ (\\text{tại } x = \\pm A); \\qquad a = -\\omega^2 x$", "Chú ý đổi $A$ và $x$ về cùng đơn vị ($\\text{cm}$ hoặc $\\text{m}$) khi tính toán."),
                F("Hệ thức độc lập với thời gian giữa x và v", "$A^2 = x^2 + \\dfrac{v^2}{\\omega^2} \\implies |v| = \\omega\\sqrt{A^2 - x^2}$", "Đồ thị biểu diễn mối liên hệ giữa $(x, v)$ hoặc $(v, a)$ là một đường **elip**; còn đồ thị giữa $(x, a)$ là một **đoạn thẳng** qua gốc tọa độ có hệ số góc âm."),
            )
        ],
        example="Một vật dao động điều hòa với biên độ $A = 5\\text{ cm}$ và tần số góc $\\omega = 4\\text{ rad/s}$. Hãy tính tốc độ cực đại $v_{\\max}$, độ lớn gia tốc cực đại $a_{\\max}$ và tốc độ $|v|$ của vật khi nó đi qua vị trí có li độ $x = 3\\text{ cm}$.",
        example_answer="Tốc độ cực đại là $v_{\\max} = \\omega A = 4 \\cdot 5 = 20\\text{ cm/s}$. Gia tốc cực đại là $a_{\\max} = \\omega^2 A = 4^2 \\cdot 5 = 80\\text{ cm/s}^2$. Khi $x = 3\\text{ cm}$, áp dụng hệ thức độc lập $A^2 = x^2 + \\dfrac{v^2}{\\omega^2} \\implies |v| = \\omega\\sqrt{A^2 - x^2} = 4\\sqrt{5^2 - 3^2} = 4 \\cdot 4 = 16\\text{ cm/s}$.",
        real_life="Cảm biến gia tốc (Accelerometer) trong điện thoại thông minh và hệ thống cảnh báo động đất đo trực tiếp gia tốc dao động $a = -\\omega^2 x$ để phát hiện rung chấn.",
        quiz=[
            mcq("biet", "Trong dao động điều hòa với biên độ $A$ và tần số góc $\\omega$, tốc độ cực đại $v_{\\max}$ và gia tốc cực đại $a_{\\max}$ được tính bằng công thức nào?", ["$v_{\\max} = \\omega A$ và $a_{\\max} = \\omega^2 A$", "$v_{\\max} = \\omega^2 A$ và $a_{\\max} = \\omega A$", "$v_{\\max} = \\dfrac{A}{\\omega}$ và $a_{\\max} = \\dfrac{A}{\\omega^2}$", "$v_{\\max} = 2\\omega A$ và $a_{\\max} = 4\\omega^2 A$"], 0, "Trong dao động điều hòa, $v_{\\max} = \\omega A$ (tại VTCB) và $a_{\\max} = \\omega^2 A$ (tại biên)."),
            mcq("biet", "Trong dao động điều hòa, vectơ gia tốc $\\vec{a}$ của vật luôn có đặc điểm gì?", ["Luôn hướng về vị trí cân bằng $O$ và có độ lớn tỉ lệ với độ lớn của li độ ($a = -\\omega^2 x$)", "Luôn cùng chiều với vectơ vận tốc $\\vec{v}$", "Luôn hướng ra vị trí biên và có độ lớn không đổi", "Bằng $0$ tại hai vị trí biên"], 0, "Vì $a = -\\omega^2 x$ nên vectơ gia tốc luôn hướng về vị trí cân bằng $O$."),
            mcq("hieu", "Hệ thức độc lập với thời gian liên hệ giữa biên độ $A$, li độ $x$, vận tốc $v$ và tần số góc $\\omega$ trong dao động điều hòa là gì?", ["$A^2 = x^2 + \\dfrac{v^2}{\\omega^2}$", "$A^2 = v^2 + \\dfrac{x^2}{\\omega^2}$", "$A = x + \\dfrac{v}{\\omega}$", "$A^2 = x^2 - \\dfrac{v^2}{\\omega^2}$"], 0, "Từ $\\cos^2(\\omega t + \\varphi) + \\sin^2(\\omega t + \\varphi) = 1$, ta có $\\left(\\dfrac{x}{A}\\right)^2 + \\left(\\dfrac{v}{\\omega A}\\right)^2 = 1 \\iff A^2 = x^2 + \\dfrac{v^2}{\\omega^2}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về vận tốc và gia tốc trong dao động điều hòa:", [
                "Vận tốc $v$ biến thiên điều hòa cùng tần số nhưng sớm pha $\\dfrac{\\pi}{2}$ so với li độ $x$.",
                "Gia tốc $a$ biến thiên điều hòa cùng tần số nhưng ngược pha với li độ $x$.",
                "Khi vật đi từ vị trí cân bằng ra vị trí biên thì chuyển động của vật là nhanh dần đều.",
                "Khi vật qua vị trí cân bằng ($x = 0$), tốc độ đạt cực đại $v_{\\max} = \\omega A$ và gia tốc bằng không ($a = 0$).",
            ], [True, True, False, True], "Ý c) sai vì khi đi từ VTCB ra biên, tốc độ giảm dần về $0$ và gia tốc biến thiên điều hòa nên đó là chuyển động **chậm dần** (không có chữ 'đều')."),
            short("vandung", "Một chất điểm dao động điều hòa với biên độ $A = 10\\text{ cm}$ và tần số góc $\\omega = 3\\text{ rad/s}$. Tốc độ cực đại $v_{\\max}$ của chất điểm bằng bao nhiêu $\\text{cm/s}$?", ["30"], "Áp dụng công thức $v_{\\max} = \\omega A = 3 \\cdot 10 = 30\\text{ cm/s}$.", unit="cm/s"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 4: Động năng, thế năng. Sự chuyển hóa năng lượng trong dao động điều hòa",
        icon="🔋",
        description="Chu kì của con lắc lò xo T = 2π√(m/k) và con lắc đơn T = 2π√(ℓ/g), công thức động năng, thế năng và cơ năng W = ½mω²A² = ½kA².",
        requirements=[
            "Viết và vận dụng được công thức tần số góc, chu kì của con lắc lò xo ($\\omega = \\sqrt{\\dfrac{k}{m}}, T = 2\\pi\\sqrt{\\dfrac{m}{k}}$) và của con lắc đơn ($\\omega = \\sqrt{\\dfrac{g}{\\ell}}, T = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}$).",
            "Viết và vận dụng được công thức động năng $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$, thế năng $W_{\\text{t}} = \\dfrac{1}{2}kx^2 = \\dfrac{1}{2}m\\omega^2 x^2$ và cơ năng $W = W_{\\text{đ}} + W_{\\text{t}} = \\dfrac{1}{2}kA^2 = \\dfrac{1}{2}m\\omega^2 A^2$.",
            "Nêu được động năng và thế năng biến thiên tuần hoàn với tần số góc $\\omega' = 2\\omega$, tần số $f' = 2f$ và chu kì $T' = \\dfrac{T}{2}$, còn cơ năng được bảo toàn (khi bỏ qua ma sát).",
        ],
        definition="Trong dao động điều hòa không ma sát, động năng $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$ và thế năng $W_{\\text{t}} = \\dfrac{1}{2}m\\omega^2 x^2 = \\dfrac{1}{2}kx^2$ chuyển hóa qua lại tuần hoàn với tần số $f' = 2f$ (chu kì $T' = \\dfrac{T}{2}$), nhưng tổng của chúng là cơ năng $W = W_{\\text{đ}} + W_{\\text{t}} = \\dfrac{1}{2}m\\omega^2 A^2 = \\dfrac{1}{2}kA^2$ luôn được bảo toàn.",
        theory=(
            "### 1. Con lắc lò xo và Con lắc đơn\n"
            "- **Con lắc lò xo** (độ cứng $k$, vật nặng khối lượng $m$):\n"
            "  $$\\omega = \\sqrt{\\dfrac{k}{m}}; \\qquad T = 2\\pi\\sqrt{\\dfrac{m}{k}}; \\qquad f = \\dfrac{1}{2\\pi}\\sqrt{\\dfrac{k}{m}}$$\n"
            "- **Con lắc đơn** (chiều dài dây $\\ell$, gia tốc trọng trường $g$, dao động góc nhỏ $\\alpha_0 \\le 10^\\circ$):\n"
            "  $$\\omega = \\sqrt{\\dfrac{g}{\\ell}}; \\qquad T = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}; \\qquad f = \\dfrac{1}{2\\pi}\\sqrt{\\dfrac{g}{\\ell}}$$\n\n"
            "### 2. Năng lượng trong dao động điều hòa\n"
            "- **Thế năng**: $W_{\\text{t}} = \\dfrac{1}{2}kx^2 = \\dfrac{1}{2}m\\omega^2 x^2 = \\dfrac{1}{2}kA^2\\cos^2(\\omega t + \\varphi)$.\n"
            "- **Động năng**: $W_{\\text{đ}} = \\dfrac{1}{2}mv^2 = \\dfrac{1}{2}kA^2\\sin^2(\\omega t + \\varphi) = W - W_{\\text{t}}$.\n"
            "- **Cơ năng**:\n"
            "  $$W = W_{\\text{đ}} + W_{\\text{t}} = W_{\\text{đ max}} = W_{\\text{t max}} = \\dfrac{1}{2}kA^2 = \\dfrac{1}{2}m\\omega^2 A^2 = \\text{const}$$\n"
            "  (Cơ năng tỉ lệ với **bình phương biên độ $A^2$**).\n"
            "- **Chu kì biến thiên của $W_{\\text{đ}}$ và $W_{\\text{t}}$**: vì $\\cos^2(\\omega t + \\varphi) = \\dfrac{1 + \\cos(2\\omega t + 2\\varphi)}{2}$ nên $W_{\\text{đ}}$ và $W_{\\text{t}}$ biến thiên điều hòa với tần số góc $\\omega' = 2\\omega$, tần số $f' = 2f$ và chu kì $T' = \\dfrac{T}{2}$. Trong 1 chu kì $T$, có $4$ lần $W_{\\text{đ}} = W_{\\text{t}}$ (tại $x = \\pm \\dfrac{A}{\\sqrt{2}}$)."
        ),
        formulas=[
            G(
                "Chu kì con lắc và Cơ năng dao động điều hòa",
                F("Chu kì con lắc lò xo và con lắc đơn", "$T_{\\text{lò xo}} = 2\\pi\\sqrt{\\dfrac{m}{k}}; \\qquad T_{\\text{con lắc đơn}} = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}$", "Chu kì của hai con lắc chỉ phụ thuộc đặc tính hệ ($m, k$ hoặc $\\ell, g$), không phụ thuộc biên độ dao động $A$."),
                F("Thế năng, Động năng và Cơ năng", "$W_{\\text{t}} = \\dfrac{1}{2}kx^2; \\quad W_{\\text{đ}} = \\dfrac{1}{2}mv^2 = \\dfrac{1}{2}k(A^2 - x^2); \\quad W = \\dfrac{1}{2}kA^2 = \\dfrac{1}{2}m\\omega^2 A^2$", "Khi計算 năng lượng ra Joule ($\\text{J}$), bắt buộc phải đổi $A$ và $x$ ra đơn vị mét ($\\text{m}$)!"),
            )
        ],
        example="Một con lắc lò xo gồm lò xo nhẹ có độ cứng $k = 100\\text{ N/m}$ và vật nhỏ dao động điều hòa theo phương ngang với biên độ $A = 4\\text{ cm} = 0{,}04\\text{ m}$ (bỏ qua ma sát). Hãy tính cơ năng $W$ của con lắc và động năng $W_{\\text{đ}}$ của vật khi đi qua vị trí có li độ $x = 2\\text{ cm} = 0{,}02\\text{ m}$.",
        example_answer="Đổi $A = 0{,}04\\text{ m}$ và $x = 0{,}02\\text{ m}$. Cơ năng của con lắc là $W = \\dfrac{1}{2}kA^2 = \\dfrac{1}{2} \\cdot 100 \\cdot 0{,}04^2 = 0{,}08\\text{ J}$. Thế năng tại $x = 0{,}02\\text{ m}$ là $W_{\\text{t}} = \\dfrac{1}{2}kx^2 = \\dfrac{1}{2} \\cdot 100 \\cdot 0{,}02^2 = 0{,}02\\text{ J}$. Động năng của vật lúc đó là $W_{\\text{đ}} = W - W_{\\text{t}} = 0{,}08 - 0{,}02 = 0{,}06\\text{ J}$.",
        real_life="Đồng hồ quả lắc cổ điển dựa vào tính đẳng thời của con lắc đơn ($T = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}$ chỉ phụ thuộc chiều dài $\\ell$) để đếm chuẩn từng giây: khi đồng hồ chạy nhanh hoặc chậm theo mùa, người ta vặn đai ốc nâng/hạ quả nặng để chỉnh chiều dài $\\ell$.",
        quiz=[
            mcq("biet", "Cơ năng $W$ của một con lắc lò xo có độ cứng $k$ dao động điều hòa với biên độ $A$ (bỏ qua ma sát) được tính theo công thức nào?", ["$W = \\dfrac{1}{2}kA^2$", "$W = kA^2$", "$W = \\dfrac{1}{2}kx^2$", "$W = 2kA^2$"], 0, "Cơ năng của con lắc lò xo bằng thế năng cực đại ở biên: $W = \\dfrac{1}{2}kA^2 = \\dfrac{1}{2}m\\omega^2 A^2$."),
            mcq("biet", "Chu kì dao động điều hòa $T$ của một con lắc đơn có chiều dài dây treo $\\ell$ tại nơi có gia tốc trọng trường $g$ được tính bằng công thức nào?", ["$T = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}$", "$T = 2\\pi\\sqrt{\\dfrac{g}{\\ell}}$", "$T = \\dfrac{1}{2\\pi}\\sqrt{\\dfrac{\\ell}{g}}$", "$T = 2\\pi\\sqrt{\\dfrac{m}{k}}$"], 0, "Chu kì dao động góc nhỏ của con lắc đơn là $T = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}$."),
            mcq("hieu", "Một vật dao động điều hòa với tần số $f$, chu kì $T$ và tần số góc $\\omega$. Động năng và thế năng của vật biến thiên tuần hoàn với tần số $f'$ và chu kì $T'$ bằng bao nhiêu?", ["$f' = 2f$ và $T' = \\dfrac{T}{2}$", "$f' = f$ và $T' = T$", "$f' = \\dfrac{f}{2}$ và $T' = 2T$", "$f' = 4f$ và $T' = \\dfrac{T}{4}$"], 0, "Trong một chu kì dao động $T$, động năng (và thế năng) đạt cực đại $2$ lần (khi qua VTCB theo hai chiều hoặc ở hai biên) nên chu kì biến thiên của động năng và thế năng là $T' = \\dfrac{T}{2}$ và tần số là $f' = 2f$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về năng lượng trong dao động điều hòa:", [
                "Cơ năng của một vật dao động điều hòa tỉ lệ thuận với bình phương biên độ dao động ($W \\sim A^2$).",
                "Khi vật đi từ vị trí biên về vị trí cân bằng thì thế năng giảm dần và động năng tăng dần.",
                "Chu kì dao động của con lắc đơn phụ thuộc vào khối lượng của quả nặng treo ở đầu dây.",
                "Tại vị trí có động năng bằng thế năng ($W_{\\text{đ}} = W_{\\text{t}} = \\dfrac{W}{2}$) thì li độ của vật là $x = \\pm \\dfrac{A}{\\sqrt{2}}$.",
            ], [True, True, False, True], "Ý c) sai vì chu kì con lắc đơn $T = 2\\pi\\sqrt{\\dfrac{\\ell}{g}}$ chỉ phụ thuộc vào chiều dài $\\ell$ và gia tốc trọng trường $g$, không phụ thuộc khối lượng quả nặng."),
            short("vandung", "Một con lắc lò xo có độ cứng $k = 50\\text{ N/m}$ dao động điều hòa với biên độ $A = 10\\text{ cm} = 0{,}1\\text{ m}$. Cơ năng $W$ của con lắc bằng bao nhiêu Joule ($\\text{J}$)?", ["0,25", "0.25"], "Đổi $A = 0{,}1\\text{ m}$. Cơ năng của con lắc là $W = \\dfrac{1}{2}kA^2 = \\dfrac{1}{2} \\cdot 50 \\cdot 0{,}1^2 = 0{,}25\\text{ J}$.", unit="J"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 5: Dao động tắt dần, dao động cưỡng bức. Hiện tượng cộng hưởng",
        icon="🌉",
        description="Nguyên nhân dao động tắt dần, đặc điểm của dao động cưỡng bức và điều kiện xảy ra cộng hưởng f = f₀.",
        requirements=[
            "Nêu được dao động tắt dần là dao động có biên độ và cơ năng giảm dần theo thời gian do lực ma sát và lực cản của môi trường.",
            "Nêu được các đặc điểm của dao động cưỡng bức (tần số bằng tần số của ngoại lực tuần hoàn $f$, biên độ phụ thuộc vào $F_0$, lực cản và độ chênh lệch $|f - f_0|$).",
            "Phát biểu được điều kiện xảy ra hiện tượng cộng hưởng ($f = f_0$ hay $T = T_0$) và giải thích các ứng dụng có lợi, tác hại của cộng hưởng.",
        ],
        definition="Dao động tắt dần là dao động có biên độ giảm dần theo thời gian do ma sát và lực cản của môi trường. Dao động cưỡng bức là dao động chịu tác dụng của một ngoại lực cưỡng bức tuần hoàn; khi tần số của ngoại lực cưỡng bức bằng tần số riêng của hệ ($f = f_0$), biên độ dao động cưỡng bức tăng nhanh đến giá trị cực đại — đó là hiện tượng cộng hưởng.",
        theory=(
            "### 1. Dao động tắt dần\n"
            "- **Khái niệm**: dao động có biên độ và cơ năng giảm dần theo thời gian rồi dừng lại.\n"
            "- **Nguyên nhân**: do lực ma sát và lực cản của môi trường làm cơ năng của con lắc chuyển hóa dần thành nhiệt năng.\n"
            "- Lực cản của môi trường càng lớn thì sự tắt dần diễn ra càng nhanh.\n"
            "- **Ứng dụng**: thiết bị giảm xóc ô tô, xe máy và cơ cấu đóng cửa tự động (tay co thủy lực).\n\n"
            "### 2. Dao động cưỡng bức và Hiện tượng cộng hưởng\n"
            "- **Dao động cưỡng bức**: dao động dưới tác dụng của ngoại lực tuần hoàn $F = F_0\\cos(2\\pi f t + \\varphi_F)$.\n"
            "  - Ở giai đoạn ổn định, dao động cưỡng bức là dao động điều hòa có **tần số bằng tần số $f$ của ngoại lực cưỡng bức**.\n"
            "  - Biên độ dao động cưỡng bức phụ thuộc vào: biên độ ngoại lực $F_0$, lực cản của môi trường và đặc biệt là **độ chênh lệch giữa tần số ngoại lực $f$ và tần số riêng $f_0$ của hệ**.\n"
            "- **Hiện tượng cộng hưởng**:\n"
            "  - Xảy ra khi tần số của ngoại lực cưỡng bức bằng tần số riêng của hệ:\n"
            "    $$f = f_0 \\iff T = T_0 \\iff \\omega = \\omega_0$$\n"
            "  - Lực cản môi trường càng nhỏ thì đỉnh cộng hưởng càng nhọn (biên độ cộng hưởng $A_{\\max}$ càng lớn).\n"
            "  - **Có lợi**: hộp đàn ghi-ta, vi-ô-lông, lò vi sóng (cộng hưởng với phân tử nước), thu sóng radio/tivi. **Có hại**: làm gãy cầu (như cầu Tacoma, cầu treo khi đoàn quân bước đều), sập nhà khi động đất."
        ),
        formulas=[
            G(
                "Điều kiện cộng hưởng và Độ giảm cơ năng tắt dần",
                F("Điều kiện xảy ra hiện tượng cộng hưởng cơ", "$f_{\\text{ngoại lực}} = f_0 \\iff T_{\\text{ngoại lực}} = T_0 \\iff \\omega_{\\text{ngoại lực}} = \\omega_0$", "Khi $f$ càng gần $f_0$ thì biên độ dao động cưỡng bức $A$ càng lớn; tại $f = f_0$ thì $A = A_{\\max}$."),
                F("Độ giảm cơ năng trong dao động tắt dần", "$\\Delta W = W_1 - W_2 = \\dfrac{1}{2}k(A_1^2 - A_2^2) = |A_{\\text{ma sát}}|$", "Nếu biên độ giảm đi $p\\%$ thì cơ năng còn lại là $W' = W(1 - p\\%)^2$."),
            )
        ],
        example="Một người xách một xô nước đi bộ trên đường, mỗi bước chân dài $s = 50\\text{ cm} = 0{,}5\\text{ m}$. Biết chu kì dao động riêng của nước trong xô là $T_0 = 0{,}5\\text{ s}$. Hỏi người đó đi với tốc độ $v$ bằng bao nhiêu thì nước trong xô bị sóng sánh mạnh nhất (dễ tràn ra ngoài nhất)?",
        example_answer="Nước trong xô sóng sánh mạnh nhất khi xảy ra hiện tượng cộng hưởng, nghĩa là thời gian đi mỗi bước chân bằng đúng chu kì dao động riêng của nước trong xô: $T = T_0 = 0{,}5\\text{ s}$. Khi đó tốc độ bước đi của người là $v = \\dfrac{s}{T} = \\dfrac{0{,}5}{0{,}5} = 1\\text{ m/s}$ ($3{,}6\\text{ km/h}$).",
        real_life="Khi một đoàn quân đi qua cầu treo, người chỉ huy luôn ra lệnh 'bước không đều' để tránh tần số nhịp bước chân trùng với tần số dao động riêng của cầu gây cộng hưởng làm sập cầu; ngược lại bầu đàn ghi-ta được thiết kế rỗng để tạo cộng hưởng làm tiếng đàn ngân vang.",
        quiz=[
            mcq("biet", "Nguyên nhân làm cho dao động của con lắc trong không khí hoặc trong dầu nhớt bị tắt dần là gì?", ["Do lực ma sát và lực cản của môi trường làm tiêu hao cơ năng của con lắc thành nhiệt năng", "Do trọng lực của Trái Đất giảm dần theo thời gian", "Do khối lượng của vật nặng giảm dần về không", "Do tần số riêng của con lắc bằng không"], 0, "Ma sát và lực cản môi trường sinh công cản làm cơ năng của vật chuyển hóa dần thành nhiệt năng."),
            mcq("biet", "Điều kiện để xảy ra **hiện tượng cộng hưởng** trong một hệ dao động cơ có tần số riêng $f_0$ là gì?", ["Tần số $f$ của ngoại lực cưỡng bức tuần hoàn bằng tần số riêng $f_0$ của hệ ($f = f_0$)", "Biên độ của ngoại lực cưỡng bức bằng $0$", "Lực cản của môi trường phải tiến tới vô cùng", "Tần số ngoại lực $f$ lớn gấp $100$ lần tần số riêng $f_0$"], 0, "Cộng hưởng xảy ra khi tần số của lực cưỡng bức bằng tần số riêng của hệ ($f = f_0$)."),
            mcq("hieu", "Một hệ cơ học có tần số dao động riêng là $f_0 = 6\\text{ Hz}$ chịu tác dụng của một ngoại lực cưỡng bức tuần hoàn có tần số $f = 8\\text{ Hz}$. Khi dao động cưỡng bức đã ổn định thì hệ dao động với tần số bằng bao nhiêu?", ["$8\\text{ Hz}$ (bằng tần số của ngoại lực cưỡng bức)", "$6\\text{ Hz}$", "$14\\text{ Hz}$", "$2\\text{ Hz}$"], 0, "Dao động cưỡng bức ở giai đoạn ổn định luôn có tần số bằng đúng tần số $f$ của ngoại lực cưỡng bức ($f = 8\\text{ Hz}$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dao động tắt dần, cưỡng bức và cộng hưởng:", [
                "Bộ phận giảm xóc của xe máy, ô tô là ứng dụng có lợi của dao động tắt dần.",
                "Biên độ của dao động cưỡng bức chỉ phụ thuộc vào biên độ của ngoại lực mà không phụ thuộc vào tần số của ngoại lực.",
                "Lực cản của môi trường càng nhỏ thì đỉnh của đồ thị cộng hưởng càng cao và nhọn.",
                "Hộp đàn ghi-ta, vi-ô-lông là ứng dụng có lợi của hiện tượng cộng hưởng âm.",
            ], [True, False, True, True], "Ý b) sai vì biên độ dao động cưỡng bức phụ thuộc mạnh vào độ chênh lệch $|f - f_0|$ giữa tần số ngoại lực và tần số riêng."),
            short("vandung", "Một con lắc có tần số dao động riêng $f_0 = 4\\text{ Hz}$. Khi chịu tác dụng của ngoại lực tuần hoàn $F = F_0\\cos(2\\pi f t)$, để biên độ dao động cưỡng bức đạt giá trị cực đại (cộng hưởng) thì tần số $f$ của ngoại lực phải bằng bao nhiêu $\\text{Hz}$?", ["4"], "Điều kiện cộng hưởng là $f = f_0 = 4\\text{ Hz}$.", unit="Hz"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 6: Mô tả sóng",
        icon="🌊",
        description="Quá trình truyền sóng cơ, các đại lượng đặc trưng của sóng (biên độ A, chu kì T, tần số f, tốc độ truyền sóng v) và bước sóng λ = v.T = v/f.",
        requirements=[
            "Nêu được sóng cơ là dao động cơ lan truyền trong một môi trường đàn hồi theo thời gian; khi sóng truyền đi, các phần tử môi trường chỉ dao động quanh vị trí cân bằng chứ không truyền đi theo sóng.",
            "Định nghĩa được bước sóng $\\lambda$ là quãng đường sóng truyền đi được trong một chu kì (hoặc khoảng cách ngắn nhất giữa hai điểm trên cùng phương truyền sóng dao động cùng pha).",
            "Vận dụng được công thức liên hệ giữa bước sóng, tốc độ truyền sóng, chu kì và tần số: $\\lambda = v \\cdot T = \\dfrac{v}{f}$.",
        ],
        definition="Sóng cơ là những dao động cơ lan truyền trong một môi trường vật chất theo thời gian. Bước sóng ($\\lambda$) là quãng đường mà sóng truyền được trong một chu kì $T$ (hoặc khoảng cách giữa hai đỉnh sóng liên tiếp): $\\lambda = v \\cdot T = \\dfrac{v}{f}$.",
        theory=(
            "### 1. Quá trình truyền sóng và các đại lượng đặc trưng\n"
            "- Quá trình truyền sóng là quá trình **truyền pha dao động và truyền năng lượng**, còn các phần tử vật chất của môi trường chỉ dao động tại chỗ quanh vị trí cân bằng của chúng.\n"
            "- **Biên độ sóng ($A$)**: biên độ dao động của một phần tử môi trường khi có sóng truyền qua.\n"
            "- **Chu kì ($T$) và Tần số ($f$) của sóng**: bằng chu kì và tần số của nguồn phát sóng ($f = \\dfrac{1}{T}$). Khi sóng truyền từ môi trường này sang môi trường khác, **tần số $f$ và chu kì $T$ luôn không đổi**.\n"
            "- **Tốc độ truyền sóng ($v$)**: tốc độ lan truyền pha dao động trong không gian, chỉ phụ thuộc bản chất môi trường ($v_{\\text{rắn}} > v_{\\text{lỏng}} > v_{\\text{khí}}$).\n\n"
            "### 2. Bước sóng ($\\lambda$)\n"
            "- **Định nghĩa 1**: Quãng đường mà sóng truyền đi được trong một chu kì $T$:\n"
            "  $$\\lambda = v \\cdot T = \\dfrac{v}{f} \\implies v = \\lambda \\cdot f$$\n"
            "- **Định nghĩa 2**: Khoảng cách ngắn nhất giữa hai điểm trên cùng một phương truyền sóng dao động **cùng pha** (khoảng cách giữa $N$ đỉnh sóng liên tiếp là $d = (N - 1)\\lambda$)."
        ),
        formulas=[
            G(
                "Công thức Bước sóng và Độ lệch pha trên phương truyền sóng",
                F("Liên hệ giữa bước sóng, tốc độ truyền sóng, chu kì và tần số", "$\\lambda = v \\cdot T = \\dfrac{v}{f} \\implies v = \\lambda \\cdot f$", "Khoảng cách giữa $N$ ngọn sóng (đỉnh sóng) liên tiếp trên mặt nước là $L = (N - 1)\\lambda$."),
                F("Độ lệch pha giữa hai điểm cách nhau khoảng d trên phương truyền sóng", "$\\Delta\\varphi = \\dfrac{2\\pi d}{\\lambda}$", "Hai điểm gần nhất cùng pha cách nhau $d = \\lambda$; hai điểm gần nhất ngược pha cách nhau $d = \\dfrac{\\lambda}{2}$."),
            )
        ],
        example="Một nguồn sóng cơ dao động trên mặt nước với tần số $f = 20\\text{ Hz}$. Biết tốc độ truyền sóng trên mặt nước là $v = 0{,}8\\text{ m/s} = 80\\text{ cm/s}$. Hãy tính bước sóng $\\lambda$ và khoảng cách giữa $5$ gợn lồi (đỉnh sóng) liên tiếp trên cùng một phương truyền sóng.",
        example_answer="Bước sóng trên mặt nước là $\\lambda = \\dfrac{v}{f} = \\dfrac{80}{20} = 4\\text{ cm}$. Khoảng cách giữa $5$ đỉnh sóng liên tiếp là $L = (5 - 1)\\lambda = 4 \\cdot 4 = 16\\text{ cm}$.",
        real_life="Khi ném một viên sỏi xuống mặt hồ yên lặng, các gợn sóng tròn lan rộng ra xa nhưng chiếc phao câu cá hay chiếc lá nổi trên mặt nước chỉ nhấp nhô lên xuống tại chỗ chứ không trôi theo sóng vào bờ.",
        quiz=[
            mcq("biet", "Công thức liên hệ giữa bước sóng $\\lambda$, tốc độ truyền sóng $v$, chu kì $T$ và tần số $f$ của sóng là gì?", ["$\\lambda = v \\cdot T = \\dfrac{v}{f}$", "$\\lambda = \\dfrac{v}{T} = v \\cdot f$", "$\\lambda = \\dfrac{T}{v} = \\dfrac{1}{vf}$", "$\\lambda = v + f$"], 0, "Bước sóng là quãng đường sóng truyền đi trong 1 chu kì: $\\lambda = v \\cdot T = \\dfrac{v}{f}$."),
            mcq("biet", "Khi một sóng cơ lan truyền trên mặt nước, các phần tử nước chuyển động như thế nào?", ["Dao động lên xuống tại chỗ quanh vị trí cân bằng của chúng chứ không chuyển dịch theo sóng đi xa", "Trôi dạt đi xa cùng với đỉnh sóng vào tận bờ", "Đứng yên hoàn toàn không dao động", "Bay bốc hơi lên không khí"], 0, "Quá trình truyền sóng chỉ truyền pha dao động và năng lượng, các phần tử môi trường chỉ dao động quanh vị trí cân bằng."),
            mcq("hieu", "Trên cùng một phương truyền sóng, hai điểm gần nhau nhất mà phần tử tại đó dao động **ngược pha** nhau thì cách nhau một khoảng bằng bao nhiêu?", ["$\\dfrac{\\lambda}{2}$ (nửa bước sóng)", "$\\lambda$ (một bước sóng)", "$\\dfrac{\\lambda}{4}$ (một phần tư bước sóng)", "$2\\lambda$"], 0, "Từ $\\Delta\\varphi = \\dfrac{2\\pi d}{\\lambda} = \\pi$ (ngược pha gần nhất), suy ra $d = \\dfrac{\\lambda}{2}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sóng cơ:", [
                "Bước sóng là khoảng cách ngắn nhất giữa hai điểm trên cùng phương truyền sóng dao động cùng pha.",
                "Khi sóng truyền từ không khí vào nước, tần số $f$ của sóng giữ nguyên không đổi, còn tốc độ truyền sóng $v$ và bước sóng $\\lambda$ thay đổi.",
                "Khoảng cách giữa $5$ đỉnh sóng liên tiếp trên một phương truyền sóng bằng $5\\lambda$.",
                "Nếu tần số sóng là $f = 10\\text{ Hz}$ và bước sóng $\\lambda = 3\\text{ cm}$ thì tốc độ truyền sóng là $v = \\lambda f = 30\\text{ cm/s}$.",
            ], [True, True, False, True], "Ý c) sai vì giữa $5$ đỉnh sóng liên tiếp chỉ có $5 - 1 = 4$ khoảng bước sóng, tức bằng $4\\lambda$."),
            short("vandung", "Một sóng cơ có tần số $f = 50\\text{ Hz}$ lan truyền trong một môi trường với tốc độ $v = 150\\text{ m/s}$. Bước sóng $\\lambda$ của sóng này bằng bao nhiêu mét ($\\text{m}$)?", ["3"], "Áp dụng công thức $\\lambda = \\dfrac{v}{f} = \\dfrac{150}{50} = 3\\text{ m}$.", unit="m"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 7: Sóng ngang, sóng dọc. Sự truyền năng lượng của sóng cơ",
        icon="🔊",
        description="Phân biệt sóng ngang và sóng dọc theo phương dao động và phương truyền sóng, môi trường truyền của từng loại và cường độ sóng I = P/(4πr²).",
        requirements=[
            "Phân biệt được sóng ngang (phương dao động vuông góc với phương truyền sóng) và sóng dọc (phương dao động trùng với phương truyền sóng).",
            "Nêu được môi trường truyền của sóng ngang (chất rắn và bề mặt chất lỏng) và của sóng dọc (cả chất rắn, chất lỏng và chất khí; sóng âm trong không khí là sóng dọc).",
            "Tính được cường độ sóng $I = \\dfrac{E}{S \\cdot \\Delta t} = \\dfrac{\\mathcal{P}}{S} = \\dfrac{\\mathcal{P}}{4\\pi r^2}$ (đơn vị $\\text{W/m}^2$).",
        ],
        definition="Sóng ngang là sóng trong đó các phần tử của môi trường dao động theo phương vuông góc với phương truyền sóng. Sóng dọc là sóng trong đó các phần tử của môi trường dao động theo phương trùng với phương truyền sóng.",
        theory=(
            "### 1. Sóng ngang và Sóng dọc\n"
            "- **Sóng ngang**:\n"
            "  - Phương dao động của phần tử **vuông góc ($\\perp$)** với phương truyền sóng (tạo thành các đỉnh sóng lồi và hõm sóng lõm).\n"
            "  - Môi trường truyền: chỉ truyền được trong **chất rắn** và trên **bề mặt chất lỏng** (sóng mặt nước, sóng trên dây đàn).\n"
            "- **Sóng dọc**:\n"
            "  - Phương dao động của phần tử **trùng ($\\parallel$)** với phương truyền sóng (tạo thành các miền nén và miền dãn xen kẽ).\n"
            "  - Môi trường truyền: truyền được trong cả **chất rắn, chất lỏng và chất khí** (sóng âm trong không khí và trong nước, sóng nén dãn dọc lò xo).\n\n"
            "### 2. Sự truyền năng lượng của sóng – Cường độ sóng\n"
            "- **Cường độ sóng ($I$)**: năng lượng sóng được truyền qua một đơn vị diện tích vuông góc với phương truyền sóng trong một đơn vị thời gian:\n"
            "  $$I = \\dfrac{E}{S \\cdot \\Delta t} = \\dfrac{\\mathcal{P}}{S} \\quad (\\text{đơn vị: } \\text{W/m}^2)$$\n"
            "- Với sóng cầu phát đẳng hướng từ nguồn điểm có công suất $\\mathcal{P}$, ở khoảng cách $r$ diện tích mặt cầu là $S = 4\\pi r^2$, nên:\n"
            "  $$I = \\dfrac{\\mathcal{P}}{4\\pi r^2}$$"
        ),
        formulas=[
            G(
                "Phân loại sóng cơ và Công thức cường độ sóng",
                F("Đặc trưng phương dao động và môi trường truyền", "$\\text{Sóng ngang: } \\vec{v}_{\\text{dđ}} \\perp \\vec{v}_{\\text{sóng}} \\ (\\text{Rắn, mặt Lỏng}); \\qquad \\text{Sóng dọc: } \\vec{v}_{\\text{dđ}} \\parallel \\vec{v}_{\\text{sóng}} \\ (\\text{Rắn, Lỏng, Khí})$", "Sóng âm truyền trong không khí và trong chất lỏng luôn là sóng dọc."),
                F("Cường độ sóng cầu cách nguồn khoảng r", "$I = \\dfrac{E}{S\\Delta t} = \\dfrac{\\mathcal{P}}{S} = \\dfrac{\\mathcal{P}}{4\\pi r^2} \\implies \\dfrac{I_1}{I_2} = \\left(\\dfrac{r_2}{r_1}\\right)^2$", "Trong đó $\\mathcal{P}$ là công suất nguồn sóng ($\\text{W}$), $r$ là khoảng cách tới nguồn ($\\text{m}$), $I$ có đơn vị $\\text{W/m}^2$."),
            )
        ],
        example="Một nguồn âm điểm phát sóng cầu đẳng hướng ra không gian với công suất không đổi $\\mathcal{P} = 12{,}56\\text{ W}$ (lấy $\\pi \\approx 3{,}14$). Hãy tính cường độ âm $I$ tại điểm $M$ cách nguồn một khoảng $r = 10\\text{ m}$. Nếu đi ra xa nguồn gấp đôi ($r' = 20\\text{ m}$) thì cường độ âm giảm đi mấy lần?",
        example_answer="Tại $r = 10\\text{ m}$, cường độ âm là $I = \\dfrac{\\mathcal{P}}{4\\pi r^2} = \\dfrac{12{,}56}{4 \\cdot 3{,}14 \\cdot 10^2} = \\dfrac{12{,}56}{1256} = 0{,}01\\text{ W/m}^2$. Khi khoảng cách $r$ tăng gấp $2$ lần thì cường độ âm $I \\sim \\dfrac{1}{r^2}$ giảm đi $2^2 = 4$ lần.",
        real_life="Trong một trận động đất, trạm địa chấn luôn ghi nhận được cả sóng dọc (sóng P – truyền nhanh hơn qua lòng đất) và sóng ngang (sóng S – truyền chậm hơn nhưng gây rung lắc ngang phá hủy công trình mạnh hơn).",
        quiz=[
            mcq("biet", "Sóng ngang là sóng có phương dao động của các phần tử môi trường như thế nào so với phương truyền sóng?", ["Vuông góc với phương truyền sóng", "Trùng với phương truyền sóng", "Hợp với phương truyền sóng một góc $30^\\circ$", "Không có phương xác định"], 0, "Trong sóng ngang, các phần tử môi trường dao động vuông góc với phương truyền sóng."),
            mcq("biet", "Sóng âm khi lan truyền trong không khí hoặc trong nước thuộc loại sóng nào?", ["Sóng dọc", "Sóng ngang", "Sóng điện từ", "Sóng dừng"], 0, "Trong chất khí và trong lòng chất lỏng chỉ truyền được sóng dọc (gồm các lớp nén – dãn liên tiếp), nên sóng âm trong không khí là sóng dọc."),
            mcq("hieu", "Gọi $I$ là cường độ sóng của một sóng cầu phát ra từ nguồn điểm có công suất $\\mathcal{P}$ không đổi. Khi khoảng cách $r$ từ điểm khảo sát đến nguồn tăng lên gấp $3$ lần thì cường độ sóng $I$ tại đó thay đổi như thế nào?", ["Giảm đi $9$ lần", "Giảm đi $3$ lần", "Tăng lên $3$ lần", "Tăng lên $9$ lần"], 0, "Vì $I = \\dfrac{\\mathcal{P}}{4\\pi r^2}$ tỉ lệ nghịch với bình phương khoảng cách $r^2$, nên khi $r$ tăng $3$ lần thì $I$ giảm $3^2 = 9$ lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sóng ngang, sóng dọc và cường độ sóng:", [
                "Sóng dọc truyền được trong cả chất rắn, chất lỏng và chất khí.",
                "Sóng ngang truyền được trong chất rắn và trên bề mặt chất lỏng.",
                "Đơn vị đo cường độ sóng $I$ trong hệ SI là Oát trên mét vuông ($\\text{W/m}^2$).",
                "Sóng cơ (cả sóng ngang và sóng dọc) đều truyền được rất nhanh trong chân không.",
            ], [True, True, True, False], "Ý d) sai vì sóng cơ cần môi trường vật chất đàn hồi nên hoàn toàn không truyền được trong chân không."),
            short("vandung", "Một nguồn sóng điểm phát sóng cầu đẳng hướng trong không gian (bỏ qua sự hấp thụ năng lượng). Tại điểm $A$ cách nguồn $r_1 = 2\\text{ m}$ có cường độ sóng là $I_1 = 16\\text{ W/m}^2$. Tại điểm $B$ cách nguồn $r_2 = 4\\text{ m}$ thì cường độ sóng $I_2$ bằng bao nhiêu $\\text{W/m}^2$?", ["4"], "Vì $\\dfrac{I_2}{I_1} = \\left(\\dfrac{r_1}{r_2}\\right)^2 = \\left(\\dfrac{2}{4}\\right)^2 = \\dfrac{1}{4}$, nên $I_2 = \\dfrac{16}{4} = 4\\text{ W/m}^2$.", unit="W/m²"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 8: Sóng điện từ",
        icon="📡",
        description="Bản chất sóng điện từ, tốc độ truyền trong chân không c = 3.10⁸ m/s, công thức λ = c/f và thang sóng điện từ (từ sóng vô tuyến đến tia gamma).",
        requirements=[
            "Nêu được sóng điện từ là điện từ trường lan truyền trong không gian, truyền được trong chân không với tốc độ lớn nhất $c = 3 \\cdot 10^8\\text{ m/s}$ và luôn là sóng ngang.",
            "Sắp xếp được thứ tự các bức xạ trong thang sóng điện từ theo bước sóng giảm dần (tần số tăng dần): sóng vô tuyến $\\to$ tia hồng ngoại $\\to$ ánh sáng nhìn thấy ($0{,}38\\text{ }\\mu\\text{m} - 0{,}76\\text{ }\\mu\\text{m}$) $\\to$ tia tử ngoại $\\to$ tia X $\\to$ tia gamma ($\\gamma$).",
            "Vận dụng được công thức bước sóng điện từ trong chân không $\\lambda = c \\cdot T = \\dfrac{c}{f}$ và trong môi trường có chiết suất $n$: $v = \\dfrac{c}{n}, \\lambda_n = \\dfrac{\\lambda}{n}$.",
        ],
        definition="Sóng điện từ là sự lan truyền trong không gian của điện từ trường biến thiên. Khác với sóng cơ, sóng điện từ truyền được trong chân không với tốc độ bằng tốc độ ánh sáng $c \\approx 3 \\cdot 10^8\\text{ m/s}$ và luôn là sóng ngang.",
        theory=(
            "### 1. Đặc điểm của sóng điện từ\n"
            "- Sóng điện từ truyền được trong **chân không** (với tốc độ lớn nhất $c = 3 \\cdot 10^8\\text{ m/s}$) và trong các môi trường vật chất (với tốc độ $v = \\dfrac{c}{n} < c$, trong đó $n$ là chiết suất).\n"
            "- Sóng điện từ luôn là **sóng ngang**: tại mỗi điểm, vectơ cường độ điện trường $\\vec{E}$ và vectơ cảm ứng từ $\\vec{B}$ luôn vuông góc với nhau và cùng vuông góc với phương truyền sóng $\\vec{v}$, đồng thời dao động **cùng pha**.\n"
            "- Bước sóng trong chân không: $\\lambda = c \\cdot T = \\dfrac{c}{f}$.\n\n"
            "### 2. Thang sóng điện từ (theo thứ tự bước sóng $\\lambda$ giảm dần, tần số $f$ tăng dần)\n"
            "1. **Sóng vô tuyến** ($\\lambda$ từ vài $\\text{mm}$ đến hàng $\\text{km}$): dùng trong phát thanh, truyền hình, điện thoại di động, Wifi, radar.\n"
            "2. **Tia hồng ngoại (IR)** ($0{,}76\\text{ }\\mu\\text{m} < \\lambda < 1\\text{ mm}$): tác dụng nổi bật nhất là **tác dụng nhiệt**; dùng trong điều khiển từ xa, camera hồng ngoại ban đêm, bếp hồng ngoại.\n"
            "3. **Ánh sáng nhìn thấy** ($0{,}38\\text{ }\\mu\\text{m} \\le \\lambda \\le 0{,}76\\text{ }\\mu\\text{m}$, hay $380\\text{ nm} - 760\\text{ nm}$): quang phổ từ Đỏ ($\\approx 0{,}76\\text{ }\\mu\\text{m}$) đến Tím ($\\approx 0{,}38\\text{ }\\mu\\text{m}$).\n"
            "4. **Tia tử ngoại (UV)** ($10\\text{ nm} < \\lambda < 380\\text{ nm}$): kích thích phát quang, diệt khuẩn, tổng hợp vitamin D.\n"
            "5. **Tia X (tia Rơnghen)** ($10^{-11}\\text{ m} < \\lambda < 10^{-8}\\text{ m}$): khả năng **đâm xuyên mạnh**; dùng chụp X-quang y tế, kiểm tra hành lí sân bay.\n"
            "6. **Tia gamma ($\\gamma$)** ($\\lambda < 10^{-11}\\text{ m}$): bước sóng ngắn nhất, tần số và khả năng đâm xuyên mạnh nhất, phát ra từ phản ứng hạt nhân."
        ),
        formulas=[
            G(
                "Bước sóng điện từ và Thứ tự thang sóng điện từ",
                F("Bước sóng điện từ trong chân không và trong môi trường chiết suất n", "$\\lambda = \\dfrac{c}{f} = c \\cdot T \\quad (c = 3 \\cdot 10^8\\text{ m/s}); \\qquad \\lambda_n = \\dfrac{v}{f} = \\dfrac{\\lambda}{n}$", "Đổi đơn vị: $1\\text{ MHz} = 10^6\\text{ Hz}$; $1\\text{ GHz} = 10^9\\text{ Hz}$; $1\\text{ }\\mu\\text{m} = 10^{-6}\\text{ m}$; $1\\text{ nm} = 10^{-9}\\text{ m}$."),
                F("Thứ tự bước sóng giảm dần (tần số tăng dần) trong thang sóng điện từ", "$\\lambda_{\\text{Vô tuyến}} > \\lambda_{\\text{Hồng ngoại}} > \\lambda_{\\text{Ánh sáng nhìn thấy}} > \\lambda_{\\text{Tử ngoại}} > \\lambda_{\\text{Tia X}} > \\lambda_{\\text{Tia }\\gamma}$", "Tất cả các tia này đều có cùng bản chất là sóng điện từ, chỉ khác nhau về tần số (và bước sóng)."),
            )
        ],
        example="Một đài phát thanh FM phát ra sóng vô tuyến có tần số $f = 100\\text{ MHz} = 10^8\\text{ Hz}$. Biết tốc độ truyền sóng điện từ trong không khí xấp xỉ bằng trong chân không $c = 3 \\cdot 10^8\\text{ m/s}$. Hãy tính bước sóng $\\lambda$ của sóng vô tuyến này.",
        example_answer="Đổi $f = 100\\text{ MHz} = 100 \\cdot 10^6\\text{ Hz} = 10^8\\text{ Hz}$. Bước sóng của sóng điện từ do đài phát ra là $\\lambda = \\dfrac{c}{f} = \\dfrac{3 \\cdot 10^8}{10^8} = 3\\text{ m}$.",
        real_life="Điện thoại di động, bộ phát Wifi, điều khiển tivi hồng ngoại và máy chụp X-quang trong bệnh viện đều ứng dụng các vùng khác nhau của thang sóng điện từ.",
        quiz=[
            mcq("biet", "Điểm khác biệt cơ bản nhất về môi trường truyền giữa **sóng điện từ** và **sóng cơ** là gì?", ["Sóng điện từ truyền được trong chân không (với tốc độ $c = 3 \\cdot 10^8\\text{ m/s}$), còn sóng cơ không truyền được trong chân không", "Sóng cơ truyền được trong chân không còn sóng điện từ thì không", "Sóng điện từ là sóng dọc còn sóng cơ luôn là sóng ngang", "Sóng điện từ có tốc độ bằng $340\\text{ m/s}$ trong chân không"], 0, "Sóng điện từ lan truyền được trong chân không với tốc độ $c \\approx 3 \\cdot 10^8\\text{ m/s}$, còn sóng cơ không truyền được trong chân không."),
            mcq("biet", "Trong thang sóng điện từ, bức xạ nào có khả năng đâm xuyên mạnh được ứng dụng để chụp X-quang chẩn đoán gãy xương và kiểm tra hành lí ở sân bay?", ["Tia X (tia Rơnghen)", "Tia hồng ngoại", "Sóng vô tuyến FM", "Ánh sáng màu đỏ"], 0, "Tia X có bước sóng rất ngắn ($10^{-11}\\text{ m} - 10^{-8}\\text{ m}$) và khả năng đâm xuyên mạnh qua mô mềm, vải, gỗ nhưng bị xương và kim loại cản lại."),
            mcq("hieu", "Sắp xếp nào sau đây đúng theo thứ tự **bước sóng giảm dần** (tức tần số tăng dần) trong thang sóng điện từ?", ["Sóng vô tuyến $\\to$ Tia hồng ngoại $\\to$ Ánh sáng nhìn thấy $\\to$ Tia tử ngoại $\\to$ Tia X $\\to$ Tia gamma ($\\gamma$)", "Tia gamma $\\to$ Tia X $\\to$ Tia tử ngoại $\\to$ Ánh sáng nhìn thấy $\\to$ Tia hồng ngoại $\\to$ Sóng vô tuyến", "Ánh sáng nhìn thấy $\\to$ Sóng vô tuyến $\\to$ Tia X $\\to$ Tia hồng ngoại", "Tia hồng ngoại $\\to$ Sóng vô tuyến $\\to$ Tia tử ngoại $\\to$ Ánh sáng nhìn thấy"], 0, "Bước sóng dài nhất là sóng vô tuyến, tiếp đến là hồng ngoại, ánh sáng nhìn thấy, tử ngoại, tia X và ngắn nhất là tia gamma ($\\gamma$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sóng điện từ:", [
                "Sóng điện từ luôn là sóng ngang.",
                "Tia hồng ngoại, ánh sáng nhìn thấy, tia tử ngoại và tia X đều có cùng bản chất là sóng điện từ.",
                "Trong vùng ánh sáng nhìn thấy, ánh sáng tím có bước sóng dài hơn ánh sáng đỏ.",
                "Tác dụng nổi bật nhất của tia hồng ngoại là tác dụng nhiệt.",
            ], [True, True, False, True], "Ý c) sai vì trong vùng ánh sáng nhìn thấy, ánh sáng đỏ có bước sóng dài nhất ($\\approx 0{,}76\\text{ }\\mu\\text{m}$) và ánh sáng tím có bước sóng ngắn nhất ($\\approx 0{,}38\\text{ }\\mu\\text{m}$)."),
            short("vandung", "Một sóng điện từ truyền trong chân không có tần số $f = 50\\text{ MHz} = 5 \\cdot 10^7\\text{ Hz}$. Lấy $c = 3 \\cdot 10^8\\text{ m/s}$, bước sóng $\\lambda$ của sóng này bằng bao nhiêu mét ($\\text{m}$)?", ["6"], "Áp dụng công thức $\\lambda = \\dfrac{c}{f} = \\dfrac{3 \\cdot 10^8}{5 \\cdot 10^7} = 6\\text{ m}$.", unit="m"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 9: Giao thoa sóng cơ",
        icon="💧",
        description="Hiện tượng giao thoa của hai sóng mặt nước, hai nguồn kết hợp và điều kiện cực đại d₂ - d₁ = kλ, cực tiểu d₂ - d₁ = (k + 0,5)λ.",
        requirements=[
            "Nêu được điều kiện để có giao thoa sóng cơ: hai nguồn sóng phải là hai nguồn kết hợp (dao động cùng phương, cùng tần số và có độ lệch pha không đổi theo thời gian).",
            "Viết và vận dụng được công thức hiệu đường đi từ hai nguồn cùng pha đến vị trí cực đại giao thoa $d_2 - d_1 = k\\lambda$ và cực tiểu giao thoa $d_2 - d_1 = (k + 0{,}5)\\lambda$ (với $k \\in \\mathbb{Z}$).",
            "Biết khoảng cách giữa hai cực đại (hoặc hai cực tiểu) liên tiếp trên đoạn thẳng nối hai nguồn là $\\dfrac{\\lambda}{2}$.",
        ],
        definition="Giao thoa sóng là hiện tượng hai sóng kết hợp khi gặp nhau tại những điểm xác định trong không gian luôn tăng cường nhau (cực đại giao thoa) hoặc làm suy yếu, triệt tiêu nhau (cực tiểu giao thoa). Với hai nguồn dao động cùng pha, cực đại thỏa mãn $d_2 - d_1 = k\\lambda$ và cực tiểu thỏa mãn $d_2 - d_1 = (k + 0{,}5)\\lambda$.",
        theory=(
            "### 1. Hai nguồn kết hợp và Hiện tượng giao thoa\n"
            "- **Hai nguồn kết hợp**: hai nguồn dao động cùng phương, **cùng tần số** và có **độ lệch pha không đổi** theo thời gian.\n"
            "- Khi hai sóng kết hợp gặp nhau, trên mặt nước xuất hiện các đường hypebol cố định gồm những điểm biên độ cực đại xen kẽ những điểm đứng yên (biên độ cực tiểu).\n\n"
            "### 2. Điều kiện Cực đại và Cực tiểu giao thoa (Hai nguồn $S_1, S_2$ cùng pha)\n"
            "- Xét điểm $M$ cách hai nguồn những khoảng $d_1 = S_1 M$ và $d_2 = S_2 M$:\n"
            "  - **Cực đại giao thoa** (hai sóng tới $M$ cùng pha, $A_M = A_1 + A_2$):\n"
            "    $$d_2 - d_1 = k\\lambda \\quad (k = 0, \\pm 1, \\pm 2, \\dots)$$\n"
            "    (Đường trung trực của $S_1 S_2$ ứng với $k = 0 \\implies d_2 - d_1 = 0$ là một đường cực đại trung tâm).\n"
            "  - **Cực tiểu giao thoa** (hai sóng tới $M$ ngược pha, $A_M = |A_1 - A_2|$):\n"
            "    $$d_2 - d_1 = \\left(k + \\dfrac{1}{2}\\right)\\lambda = (k + 0{,}5)\\lambda \\quad (k = 0, \\pm 1, \\pm 2, \\dots)$$\n"
            "- **Trên đoạn thẳng nối hai nguồn $S_1 S_2$**: khoảng cách giữa hai điểm cực đại (hoặc hai điểm cực tiểu) liên tiếp là $\\Delta d = \\dfrac{\\lambda}{2}$."
        ),
        formulas=[
            G(
                "Điều kiện cực đại và cực tiểu giao thoa (hai nguồn cùng pha)",
                F("Hiệu đường đi tại điểm Cực đại và Cực tiểu giao thoa", "$\\text{Cực đại: } d_2 - d_1 = k\\lambda; \\qquad \\text{Cực tiểu: } d_2 - d_1 = (k + 0{,}5)\\lambda \\quad (k \\in \\mathbb{Z})$", "Trong đó $k$ là bậc của cực đại giao thoa ($k = 0$ là cực đại trung tâm trên đường trung trực)."),
                F("Khoảng cách giữa các cực đại/cực tiểu trên đoạn nối 2 nguồn", "$d_{\\text{CĐ-CĐ liên tiếp}} = d_{\\text{CT-CT liên tiếp}} = \\dfrac{\\lambda}{2}; \\qquad d_{\\text{CĐ-CT gần nhất}} = \\dfrac{\\lambda}{4}$", "Số cực đại trên đoạn $S_1 S_2$: $-\\dfrac{S_1 S_2}{\\lambda} < k < \\dfrac{S_1 S_2}{\\lambda}$."),
            )
        ],
        example="Trong thí nghiệm giao thoa sóng trên mặt nước với hai nguồn kết hợp $S_1, S_2$ dao động cùng pha, bước sóng là $\\lambda = 4\\text{ cm}$. Xét điểm $M$ trên mặt nước cách hai nguồn lần lượt là $d_1 = 14\\text{ cm}$ và $d_2 = 22\\text{ cm}$. Hãy cho biết tại $M$ có cực đại hay cực tiểu giao thoa và thuộc bậc thứ mấy?",
        example_answer="Ta tính tỉ số hiệu đường đi chia cho bước sóng: $\\dfrac{d_2 - d_1}{\\lambda} = \\dfrac{22 - 14}{4} = \\dfrac{8}{4} = 2$ (là số nguyên $k = 2$). Vậy tại điểm $M$ có **cực đại giao thoa bậc $2$**.",
        real_life="Tai nghe chống ồn chủ động (Active Noise Cancelling – ANC) thu âm thanh tiếng ồn bên ngoài rồi phát ra sóng âm có cùng biên độ nhưng ngược pha để tạo cực tiểu giao thoa triệt tiêu tiếng ồn tại tai người nghe.",
        quiz=[
            mcq("biet", "Trong hiện tượng giao thoa của hai sóng mặt nước phát ra từ hai nguồn kết hợp cùng pha có bước sóng $\\lambda$, những điểm có biên độ dao động **cực đại** thỏa mãn điều kiện hiệu đường đi nào (với $k \\in \\mathbb{Z}$)?", ["$d_2 - d_1 = k\\lambda$", "$d_2 - d_1 = (k + 0{,}5)\\lambda$", "$d_2 + d_1 = k\\lambda$", "$d_2 - d_1 = (2k + 1)\\dfrac{\\lambda}{4}$"], 0, "Khi hai nguồn cùng pha, hiệu đường đi tới các điểm cực đại bằng một số nguyên lần bước sóng: $d_2 - d_1 = k\\lambda$."),
            mcq("biet", "Để xảy ra hiện tượng giao thoa ổn định, hai nguồn sóng phải là hai **nguồn kết hợp**, nghĩa là thỏa mãn điều kiện nào?", ["Dao động cùng phương, cùng tần số và có độ lệch pha không đổi theo thời gian", "Dao động khác tần số và khác phương", "Phải đặt trong chân không", "Có biên độ biến đổi ngẫu nhiên theo thời gian"], 0, "Hai nguồn kết hợp là hai nguồn dao động cùng phương, cùng tần số và có độ lệch pha không đổi theo thời gian."),
            mcq("hieu", "Trong giao thoa sóng mặt nước với hai nguồn cùng pha, trên đoạn thẳng nối hai nguồn $S_1 S_2$, khoảng cách giữa hai điểm cực đại giao thoa liên tiếp là bao nhiêu?", ["$\\dfrac{\\lambda}{2}$", "$\\lambda$", "$\\dfrac{\\lambda}{4}$", "$2\\lambda$"], 0, "Trên đoạn thẳng nối hai nguồn, khoảng cách giữa hai cực đại (hoặc hai cực tiểu) liên tiếp bằng nửa bước sóng $\\dfrac{\\lambda}{2}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về giao thoa sóng cơ (với hai nguồn cùng pha):", [
                "Mọi điểm nằm trên đường trung trực của đoạn thẳng nối hai nguồn ($d_1 = d_2$) đều dao động với biên độ cực đại.",
                "Tại những điểm có $d_2 - d_1 = (k + 0{,}5)\\lambda$, hai sóng truyền tới ngược pha nhau nên triệt tiêu nhau (cực tiểu giao thoa).",
                "Hiện tượng giao thoa là hiện tượng đặc trưng chỉ có ở sóng.",
                "Nếu tại điểm $M$ có $d_2 - d_1 = 3{,}5\\lambda$ thì điểm $M$ dao động với biên độ cực đại bậc $3$.",
            ], [True, True, True, False], "Ý d) sai vì $3{,}5\\lambda = (3 + 0{,}5)\\lambda$ là một số bán nguyên lần bước sóng, nên điểm $M$ là **cực tiểu giao thoa** thứ $4$."),
            short("vandung", "Trong thí nghiệm giao thoa sóng nước với hai nguồn kết hợp cùng pha, người ta đo được khoảng cách giữa hai cực đại giao thoa liên tiếp nằm trên đoạn thẳng nối hai nguồn là $3\\text{ cm}$. Bước sóng $\\lambda$ của sóng nước bằng bao nhiêu $\\text{cm}$?", ["6"], "Trên đoạn nối hai nguồn, khoảng cách giữa hai cực đại liên tiếp là $\\dfrac{\\lambda}{2} = 3\\text{ cm} \\implies \\lambda = 6\\text{ cm}$.", unit="cm"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 10: Giao thoa ánh sáng",
        icon="🌈",
        description="Thí nghiệm khe Young về giao thoa ánh sáng, công thức khoảng vân i = λD/a, vị trí vân sáng x_s = k.i và vị trí vân tối x_t = (k + 0,5)i.",
        requirements=[
            "Mô tả được thí nghiệm khe Young về giao thoa ánh sáng đơn sắc (hệ vân gồm các vạch sáng và vạch tối song song, cách đều nhau trên màn).",
            "Viết và vận dụng được công thức tính khoảng vân $i = \\dfrac{\\lambda D}{a}$ và công thức xác định bước sóng $\\lambda = \\dfrac{i \\cdot a}{D}$.",
            "Tính được tọa độ vị trí vân sáng bậc $k$: $x_s = k \\cdot i = k\\dfrac{\\lambda D}{a}$ và vị trí vân tối: $x_t = (k + 0{,}5)i$ (với $k \\in \\mathbb{Z}$).",
        ],
        definition="Trong thí nghiệm khe Young về giao thoa ánh sáng đơn sắc có bước sóng $\\lambda$, khoảng vân ($i$) là khoảng cách giữa hai vân sáng hoặc hai vân tối liên tiếp trên màn quan sát: $i = \\dfrac{\\lambda D}{a}$, trong đó $a$ là khoảng cách giữa hai khe hẹp $F_1, F_2$ và $D$ là khoảng cách từ mặt phẳng hai khe đến màn quan sát.",
        theory=(
            "### 1. Thí nghiệm khe Young và Khoảng vân\n"
            "- Hiện tượng giao thoa ánh sáng khẳng định **ánh sáng có tính chất sóng**.\n"
            "- **Khoảng vân ($i$)**: khoảng cách giữa hai vân sáng liên tiếp (hoặc hai vân tối liên tiếp):\n"
            "  $$i = \\dfrac{\\lambda D}{a} \\implies \\lambda = \\dfrac{i \\cdot a}{D}$$\n"
            "  *Quy ước đổi đơn vị nhanh*: nếu $\\lambda$ tính bằng $\\mu\\text{m}$ ($10^{-6}\\text{ m}$), $D$ tính bằng $\\text{m}$ và $a$ tính bằng $\\text{mm}$ ($10^{-3}\\text{ m}$) thì khoảng vân $i$ tự động ra đơn vị $\\text{mm}$!\n\n"
            "### 2. Vị trí vân sáng và vân tối trên màn (tính từ vân sáng trung tâm $O$)\n"
            "- **Vị trí vân sáng**:\n"
            "  $$x_s = k \\cdot i = k\\dfrac{\\lambda D}{a} \\quad (k = 0, \\pm 1, \\pm 2, \\dots)$$\n"
            "  ($k = 0$: vân sáng trung tâm tại $O$; $k = \\pm 1$: vân sáng bậc 1; $k = \\pm 2$: vân sáng bậc 2...).\n"
            "- **Vị trí vân tối**:\n"
            "  $$x_t = (k + 0{,}5)i = \\left(k + \\dfrac{1}{2}\\right)\\dfrac{\\lambda D}{a} \\quad (k = 0, \\pm 1, \\pm 2, \\dots)$$\n"
            "  (Vân tối thứ nhất ứng với $x_t = \\pm 0{,}5i$; vân tối thứ hai ứng với $x_t = \\pm 1{,}5i$; vân tối thứ $n$ ứng với $x_t = \\pm (n - 0{,}5)i$).\n"
            "- Khoảng cách giữa $N$ vân sáng liên tiếp là $L = (N - 1)i$."
        ),
        formulas=[
            G(
                "Công thức Giao thoa ánh sáng khe Young",
                F("Khoảng vân giao thoa và Bước sóng ánh sáng", "$i = \\dfrac{\\lambda D}{a} \\iff \\lambda = \\dfrac{i \\cdot a}{D}$", "Mẹo đơn vị chuẩn: $\\lambda (\\mu\\text{m}),\\ D (\\text{m}),\\ a (\\text{mm}) \\implies i (\\text{mm})$."),
                F("Vị trí vân sáng và vị trí vân tối", "$x_s = k \\cdot i; \\qquad x_t = (k + 0{,}5)i \\quad (k \\in \\mathbb{Z})$", "Khoảng cách giữa 1 vân sáng và 1 vân tối kề nhau là $\\dfrac{i}{2}$; khoảng cách giữa $N$ vân sáng liên tiếp là $(N - 1)i$."),
            )
        ],
        example="Trong thí nghiệm Young về giao thoa ánh sáng, khoảng cách giữa hai khe là $a = 1\\text{ mm}$, khoảng cách từ mặt phẳng chứa hai khe đến màn quan sát là $D = 2\\text{ m}$. Chiếu vào hai khe ánh sáng đơn sắc có bước sóng $\\lambda = 0{,}6\\text{ }\\mu\\text{m}$. Hãy tính khoảng vân $i$ và vị trí của vân sáng bậc $3$.",
        example_answer="Áp dụng công thức khoảng vân (với $\\lambda = 0{,}6\\text{ }\\mu\\text{m}, D = 2\\text{ m}, a = 1\\text{ mm}$): $i = \\dfrac{\\lambda D}{a} = \\dfrac{0{,}6 \\cdot 2}{1} = 1{,}2\\text{ mm}$. Vị trí của vân sáng bậc $3$ cách vân trung tâm một đoạn là $x_{s3} = 3i = 3 \\cdot 1{,}2 = 3{,}6\\text{ mm}$.",
        real_life="Màu sắc cầu vồng óng ánh trên mặt bong bóng xà phòng, váng dầu mỏng trên mặt nước hay mặt đĩa CD là kết quả của hiện tượng giao thoa ánh sáng trắng.",
        quiz=[
            mcq("biet", "Trong thí nghiệm Young về giao thoa ánh sáng, công thức tính khoảng vân $i$ theo bước sóng $\\lambda$, khoảng cách hai khe $a$ và khoảng cách từ hai khe đến màn $D$ là gì?", ["$i = \\dfrac{\\lambda D}{a}$", "$i = \\dfrac{\\lambda a}{D}$", "$i = \\dfrac{a D}{\\lambda}$", "$i = \\lambda \\cdot a \\cdot D$"], 0, "Khoảng vân giao thoa ánh sáng được tính bằng công thức $i = \\dfrac{\\lambda D}{a}$."),
            mcq("biet", "Trong thí nghiệm giao thoa ánh sáng khe Young với khoảng vân $i$, tọa độ các **vân sáng** trên màn được xác định bởi công thức nào (với $k \\in \\mathbb{Z}$)?", ["$x_s = k \\cdot i$", "$x_s = (k + 0{,}5)i$", "$x_s = (2k + 1)\\dfrac{i}{4}$", "$x_s = \\dfrac{i}{k}$"], 0, "Các vân sáng nằm tại vị trí $x_s = k \\cdot i = k\\dfrac{\\lambda D}{a}$."),
            mcq("hieu", "Trong cùng một bộ thí nghiệm giao thoa Young ($a$ và $D$ không đổi), nếu thay ánh sáng đơn sắc màu tím ($\\lambda_{\\text{tím}} \\approx 0{,}4\\text{ }\\mu\\text{m}$) bằng ánh sáng đơn sắc màu đỏ ($\\lambda_{\\text{đỏ}} \\approx 0{,}7\\text{ }\\mu\\text{m}$) thì khoảng vân $i$ trên màn thay đổi như thế nào?", ["Khoảng vân $i$ tăng lên (vì $\\lambda_{\\text{đỏ}} > \\lambda_{\\text{tím}}$)", "Khoảng vân $i$ giảm đi", "Khoảng vân $i$ không thay đổi", "Hệ vân biến mất hoàn toàn"], 0, "Vì $i = \\dfrac{\\lambda D}{a}$ tỉ lệ thuận với bước sóng $\\lambda$ và $\\lambda_{\\text{đỏ}} > \\lambda_{\\text{tím}}$, nên khoảng vân của ánh sáng đỏ lớn hơn của ánh sáng tím."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về giao thoa ánh sáng:", [
                "Tại tâm $O$ của màn quan sát (cách đều hai khe $F_1, F_2$) luôn là vân sáng trung tâm ứng với $k = 0$.",
                "Khoảng cách giữa một vân sáng và một vân tối liền kề nhau bằng một nửa khoảng vân ($\\dfrac{i}{2}$).",
                "Khoảng cách giữa $6$ vân sáng liên tiếp trên màn quan sát bằng $6i$.",
                "Nếu thực hiện giao thoa bằng ánh sáng trắng thì vân chính giữa là vân sáng trắng, hai bên là các dải màu như cầu vồng với tím ở trong, đỏ ở ngoài.",
            ], [True, True, False, True], "Ý c) sai vì khoảng cách giữa $6$ vân sáng liên tiếp bằng $(6 - 1)i = 5i$."),
            short("vandung", "Trong thí nghiệm Young về giao thoa ánh sáng, biết $a = 1{,}5\\text{ mm}$, $D = 3\\text{ m}$ và bước sóng ánh sáng đơn sắc dùng trong thí nghiệm là $\\lambda = 0{,}5\\text{ }\\mu\\text{m}$. Khoảng vân $i$ trên màn bằng bao nhiêu $\\text{mm}$?", ["1"], "Áp dụng công thức $i = \\dfrac{\\lambda D}{a} = \\dfrac{0{,}5 \\cdot 3}{1{,}5} = 1\\text{ mm}$.", unit="mm"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 11: Sóng dừng",
        icon="🎸",
        description="Sự phản xạ sóng ở vật cản cố định và tự do, khái niệm nút sóng – bụng sóng và điều kiện có sóng dừng trên dây hai đầu cố định ℓ = k.λ/2 hoặc một đầu cố định một đầu tự do ℓ = (2k + 1)λ/4.",
        requirements=[
            "Mô tả được hiện tượng sóng dừng là sự giao thoa của sóng tới và sóng phản xạ truyền trên cùng một phương tạo nên các nút sóng (đứng yên) và bụng sóng (biên độ cực đại) cố định trong không gian.",
            "Nêu được khoảng cách giữa hai nút sóng (hoặc hai bụng sóng) liên tiếp là $\\dfrac{\\lambda}{2}$, khoảng cách giữa một nút và một bụng liền kề là $\\dfrac{\\lambda}{4}$.",
            "Vận dụng được điều kiện có sóng dừng trên dây hai đầu cố định $\\ell = k\\dfrac{\\lambda}{2}$ (số bụng $= k$, số nút $= k + 1$) và trên dây một đầu cố định – một đầu tự do $\\ell = (2k + 1)\\dfrac{\\lambda}{4}$ (số bụng $=$ số nút $= k + 1$).",
        ],
        definition="Sóng dừng là sóng có các nút sóng (những điểm luôn đứng yên) và các bụng sóng (những điểm luôn dao động với biên độ cực đại) cố định trong không gian, được tạo thành do sự giao thoa giữa sóng tới và sóng phản xạ truyền trên cùng một phương.",
        theory=(
            "### 1. Phản xạ sóng và Đặc điểm của sóng dừng\n"
            "- **Phản xạ trên vật cản cố định**: sóng phản xạ luôn **ngược pha** với sóng tới tại điểm phản xạ (điểm cố định là một **nút sóng**).\n"
            "- **Phản xạ trên vật cản tự do**: sóng phản xạ luôn **cùng pha** với sóng tới tại điểm phản xạ (đầu tự do là một **bụng sóng**).\n"
            "- **Khoảng cách đặc trưng trên sóng dừng**:\n"
            "  - Giữa **2 nút sóng liên tiếp** (hoặc **2 bụng sóng liên tiếp**): $d = \\dfrac{\\lambda}{2}$ (chiều dài của $1$ bó sóng).\n"
            "  - Giữa **1 nút sóng và 1 bụng sóng liền kề**: $d = \\dfrac{\\lambda}{4}$.\n\n"
            "### 2. Hai điều kiện để có sóng dừng trên sợi dây chiều dài $\\ell$\n"
            "1. **Dây có hai đầu cố định** (hai đầu dây là hai nút sóng):\n"
            "   $$\\ell = k\\dfrac{\\lambda}{2} = k\\dfrac{v}{2f} \\implies f_k = k\\dfrac{v}{2\\ell} = k f_1 \\quad (k = 1, 2, 3, \\dots)$$\n"
            "   Trong đó: số bó sóng (số bụng sóng) là $N_{\\text{bụng}} = k$; tổng số nút sóng (kể cả hai đầu dây) là $N_{\\text{nút}} = k + 1$.\n"
            "2. **Dây có một đầu cố định, một đầu tự do** (hoặc cột không khí trong ống một đầu kín, một đầu hở):\n"
            "   $$\\ell = (2k + 1)\\dfrac{\\lambda}{4} = m\\dfrac{\\lambda}{4} \\quad (k = 0, 1, 2, \\dots; \\ m = 2k + 1 = 1, 3, 5, \\dots)$$\n"
            "   Trong đó: số bụng sóng bằng số nút sóng: $N_{\\text{bụng}} = N_{\\text{nút}} = k + 1$."
        ),
        formulas=[
            G(
                "Khoảng cách nút – bụng và Điều kiện có sóng dừng",
                F("Khoảng cách giữa các nút sóng và bụng sóng", "$d_{\\text{2 nút liên tiếp}} = d_{\\text{2 bụng liên tiếp}} = \\dfrac{\\lambda}{2}; \\qquad d_{\\text{nút - bụng kề nhau}} = \\dfrac{\\lambda}{4}$", "Mỗi bó sóng được giới hạn bởi hai nút sóng liên tiếp và có chiều dài bằng $\\dfrac{\\lambda}{2}$."),
                F("Điều kiện chiều dài dây có sóng dừng", "$\\text{2 đầu cố định: } \\ell = k\\dfrac{\\lambda}{2} \\ (k \\in \\mathbb{N}^*); \\qquad \\text{1 đầu cố định – 1 đầu tự do: } \\ell = (2k + 1)\\dfrac{\\lambda}{4} \\ (k \\in \\mathbb{N})$", "Với dây 2 đầu cố định: $N_{\\text{bụng}} = k$ và $N_{\\text{nút}} = k + 1$."),
            )
        ],
        example="Một sợi dây đàn hồi dài $\\ell = 1{,}2\\text{ m}$ có hai đầu cố định. Khi kích thích cho dây dao động với tần số $f = 50\\text{ Hz}$ thì trên dây xuất hiện sóng dừng với $4$ bụng sóng ($k = 4$). Hãy tính bước sóng $\\lambda$, tổng số nút sóng trên dây và tốc độ truyền sóng $v$ trên dây.",
        example_answer="Vì trên dây hai đầu cố định có $k = 4$ bụng sóng nên tổng số nút sóng (kể cả hai đầu dây) là $N_{\\text{nút}} = k + 1 = 5$ nút. Áp dụng công thức $\\ell = k\\dfrac{\\lambda}{2} \\implies \\lambda = \\dfrac{2\\ell}{k} = \\dfrac{2 \\cdot 1{,}2}{4} = 0{,}6\\text{ m}$. Tốc độ truyền sóng trên dây là $v = \\lambda \\cdot f = 0{,}6 \\cdot 50 = 30\\text{ m/s}$.",
        real_life="Các nhạc cụ dây (đàn ghi-ta, đàn bầu, đàn tranh, đàn piano) tạo ra các nốt nhạc trầm bổng dựa trên sóng dừng trên dây hai đầu cố định; còn sáo, kèn tạo ra âm nhạc dựa trên sóng dừng của cột không khí trong ống.",
        quiz=[
            mcq("biet", "Điều kiện về chiều dài $\\ell$ của một sợi dây có **hai đầu cố định** để trên dây xuất hiện sóng dừng với bước sóng $\\lambda$ là gì (với $k = 1, 2, 3, \\dots$)?", ["$\\ell = k\\dfrac{\\lambda}{2}$", "$\\ell = (2k + 1)\\dfrac{\\lambda}{4}$", "$\\ell = k\\lambda$", "$\\ell = (k + 0{,}5)\\lambda$"], 0, "Trên dây hai đầu cố định, chiều dài dây phải bằng một số nguyên lần nửa bước sóng: $\\ell = k\\dfrac{\\lambda}{2}$."),
            mcq("biet", "Trong hiện tượng sóng dừng trên dây, khoảng cách ngắn nhất giữa hai nút sóng liên tiếp (hoặc hai bụng sóng liên tiếp) bằng bao nhiêu?", ["$\\dfrac{\\lambda}{2}$", "$\\lambda$", "$\\dfrac{\\lambda}{4}$", "$2\\lambda$"], 0, "Khoảng cách giữa hai nút sóng hoặc hai bụng sóng liên tiếp đúng bằng chiều dài một bó sóng $\\dfrac{\\lambda}{2}$."),
            mcq("hieu", "Trên một sợi dây có hai đầu cố định đang có sóng dừng với $5$ bụng sóng ($k = 5$). Tổng số nút sóng trên dây (tính cả hai đầu dây) là bao nhiêu?", ["$6$ nút sóng", "$5$ nút sóng", "$4$ nút sóng", "$10$ nút sóng"], 0, "Trên dây hai đầu cố định, số nút sóng luôn nhiều hơn số bụng sóng $1$ đơn vị: $N_{\\text{nút}} = k + 1 = 5 + 1 = 6$ nút."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phản xạ sóng và sóng dừng:", [
                "Tại điểm phản xạ cố định, sóng phản xạ luôn ngược pha với sóng tới.",
                "Tại điểm phản xạ tự do, sóng phản xạ luôn cùng pha với sóng tới.",
                "Khoảng cách giữa một nút sóng và một bụng sóng liền kề nhau bằng $\\dfrac{\\lambda}{2}$.",
                "Trong hiện tượng sóng dừng, các nút sóng và bụng sóng có vị trí cố định trong không gian.",
            ], [True, True, False, True], "Ý c) sai vì khoảng cách giữa một nút sóng và một bụng sóng liền kề bằng $\\dfrac{\\lambda}{4}$ (còn giữa hai nút liên tiếp mới là $\\dfrac{\\lambda}{2}$)."),
            short("vandung", "Trên một sợi dây đàn hồi dài $\\ell = 90\\text{ cm}$ có hai đầu cố định đang có sóng dừng với $3$ bó sóng (tức $k = 3$ bụng sóng). Bước sóng $\\lambda$ của sóng truyền trên dây bằng bao nhiêu $\\text{cm}$?", ["60"], "Áp dụng công thức $\\ell = k\\dfrac{\\lambda}{2} \\implies \\lambda = \\dfrac{2\\ell}{k} = \\dfrac{2 \\cdot 90}{3} = 60\\text{ cm}$.", unit="cm"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 12: Định luật Coulomb về tương tác tĩnh điện",
        icon="⚡",
        description="Điện tích điểm, phát biểu và công thức Định luật Coulomb F = k.|q₁q₂|/(ε.r²) trong chân không và trong điện môi.",
        requirements=[
            "Nêu được khái niệm điện tích điểm, đơn vị điện tích Coulomb ($\\text{C}$) và điện tích nguyên tố $e = 1{,}6 \\cdot 10^{-19}\\text{ C}$.",
            "Phát biểu và viết được công thức Định luật Coulomb trong chân không $F = k\\dfrac{|q_1 q_2|}{r^2}$ (với $k = 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$) và trong môi trường điện môi đồng chất $F = \\dfrac{k|q_1 q_2|}{\\varepsilon r^2}$.",
            "Xác định đúng phương, chiều (hút nhau khi $q_1 q_2 < 0$, đẩy nhau khi $q_1 q_2 > 0$) và độ lớn lực tương tác tĩnh điện giữa các điện tích điểm.",
        ],
        definition="Định luật Coulomb: Lực hút hay đẩy giữa hai điện tích điểm đặt trong chân không có phương trùng với đường thẳng nối hai điện tích điểm đó, có độ lớn tỉ lệ thuận với tích độ lớn của hai điện tích và tỉ lệ nghịch với bình phương khoảng cách giữa chúng: $F = k\\dfrac{|q_1 q_2|}{r^2}$.",
        theory=(
            "### 1. Điện tích điểm và Tương tác tĩnh điện\n"
            "- **Điện tích điểm**: vật tích điện có kích thước rất nhỏ so với khoảng cách tới điểm mà ta xét.\n"
            "- Đơn vị điện tích trong hệ SI là **Coulomb** ($\\text{C}$). Các ước thường dùng: $1\\text{ mC} = 10^{-3}\\text{ C}$; $1\\text{ }\\mu\\text{C} = 10^{-6}\\text{ C}$; $1\\text{ nC} = 10^{-9}\\text{ C}$. Điện tích nguyên tố: $e = 1{,}6 \\cdot 10^{-19}\\text{ C}$.\n"
            "- Hai điện tích cùng dấu ($q_1 q_2 > 0$) thì **đẩy nhau**; trái dấu ($q_1 q_2 < 0$) thì **hút nhau**.\n\n"
            "### 2. Định luật Coulomb trong chân không và trong điện môi\n"
            "- **Trong chân không (hoặc không khí)**:\n"
            "  $$F_0 = k\\dfrac{|q_1 q_2|}{r^2} \\quad \\left(\\text{với } k = \\dfrac{1}{4\\pi\\varepsilon_0} \\approx 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2\\right)$$\n"
            "- **Trong môi trường cách điện (điện môi) đồng chất có hằng số điện môi $\\varepsilon \\ge 1$**: lực tĩnh điện giảm đi $\\varepsilon$ lần so với trong chân không:\n"
            "  $$F = \\dfrac{F_0}{\\varepsilon} = k\\dfrac{|q_1 q_2|}{\\varepsilon r^2}$$"
        ),
        formulas=[
            G(
                "Công thức Định luật Coulomb",
                F("Độ lớn lực Coulomb trong chân không và trong điện môi", "$F_0 = k\\dfrac{|q_1 q_2|}{r^2}; \\qquad F = \\dfrac{k|q_1 q_2|}{\\varepsilon r^2} = \\dfrac{F_0}{\\varepsilon} \\quad (k = 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2)$", "Chú ý đổi khoảng cách $r$ ra mét ($\\text{m}$) và điện tích ra Coulomb ($\\text{C}$, với $1\\text{ }\\mu\\text{C} = 10^{-6}\\text{ C}$)."),
                F("Quan hệ giữa lực Coulomb và khoảng cách r", "$F \\sim \\dfrac{1}{r^2} \\implies \\dfrac{F_1}{F_2} = \\left(\\dfrac{r_2}{r_1}\\right)^2$", "Khi khoảng cách $r$ giữa hai điện tích điểm tăng gấp $k$ lần thì lực tương tác giảm đi $k^2$ lần."),
            )
        ],
        example="Hai điện tích điểm $q_1 = 2 \\cdot 10^{-6}\\text{ C}$ và $q_2 = -4 \\cdot 10^{-6}\\text{ C}$ đặt cách nhau một khoảng $r = 30\\text{ cm} = 0{,}3\\text{ m}$ trong chân không ($k = 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$). Hãy cho biết hai điện tích hút hay đẩy nhau và tính độ lớn lực tương tác giữa chúng.",
        example_answer="Vì $q_1 > 0$ và $q_2 < 0$ trái dấu nhau nên hai điện tích **hút nhau**. Độ lớn lực tương tác Coulomb là $F = k\\dfrac{|q_1 q_2|}{r^2} = 9 \\cdot 10^9 \\cdot \\dfrac{2 \\cdot 10^{-6} \\cdot 4 \\cdot 10^{-6}}{0{,}3^2} = \\dfrac{0{,}072}{0{,}09} = 0{,}8\\text{ N}$.",
        real_life="Công nghệ sơn tĩnh điện (tích điện trái dấu cho hạt sơn và bề mặt kim loại cần sơn) và hệ thống lọc bụi tĩnh điện trong ống khói nhà máy nhiệt điện đều ứng dụng trực tiếp lực hút Coulomb.",
        quiz=[
            mcq("biet", "Biểu thức của Định luật Coulomb tính độ lớn lực tương tác tĩnh điện giữa hai điện tích điểm $q_1, q_2$ đặt cách nhau khoảng $r$ trong chân không là gì?", ["$F = k\\dfrac{|q_1 q_2|}{r^2}$", "$F = k\\dfrac{|q_1 q_2|}{r}$", "$F = k\\dfrac{r^2}{|q_1 q_2|}$", "$F = \\dfrac{|q_1 + q_2|}{k r^2}$"], 0, "Theo định luật Coulomb trong chân không: $F = k\\dfrac{|q_1 q_2|}{r^2}$ với $k = 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$."),
            mcq("biet", "Khi giữ nguyên độ lớn hai điện tích điểm và tăng khoảng cách $r$ giữa chúng lên gấp $2$ lần thì độ lớn lực tương tác tĩnh điện giữa chúng thay đổi như thế nào?", ["Giảm đi $4$ lần", "Giảm đi $2$ lần", "Tăng lên $2$ lần", "Tăng lên $4$ lần"], 0, "Vì $F$ tỉ lệ nghịch với $r^2$, nên khi $r$ tăng $2$ lần thì $F$ giảm $2^2 = 4$ lần."),
            mcq("hieu", "Hai điện tích điểm đặt cách nhau khoảng $r$ trong chân không thì tương tác với nhau bằng lực có độ lớn $F_0 = 12\\text{ N}$. Nếu nhúng cả hệ hai điện tích này với cùng khoảng cách $r$ vào trong dầu hỏa có hằng số điện môi $\\varepsilon = 2$ thì độ lớn lực tương tác giữa chúng bằng bao nhiêu?", ["$6\\text{ N}$", "$24\\text{ N}$", "$3\\text{ N}$", "$12\\text{ N}$"], 0, "Trong môi trường có hằng số điện môi $\\varepsilon$, lực tương tác giảm đi $\\varepsilon$ lần: $F = \\dfrac{F_0}{\\varepsilon} = \\dfrac{12}{2} = 6\\text{ N}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Định luật Coulomb:", [
                "Phương của lực tương tác Coulomb giữa hai điện tích điểm luôn trùng với đường thẳng nối hai điện tích điểm đó.",
                "Hằng số điện môi $\\varepsilon$ của chân không bằng $1$, còn của các chất cách điện đều lớn hơn $1$.",
                "Nếu $|q_1| > |q_2|$ thì lực do $q_1$ tác dụng lên $q_2$ có độ lớn lớn hơn lực do $q_2$ tác dụng lên $q_1$.",
                "Đổi đơn vị: $1\\text{ }\\mu\\text{C} = 10^{-6}\\text{ C}$ và $1\\text{ nC} = 10^{-9}\\text{ C}$.",
            ], [True, True, False, True], "Ý c) sai vì theo định luật 3 Newton, hai lực tương tác giữa hai điện tích điểm luôn có độ lớn bằng nhau ($F_{12} = F_{21} = k\\dfrac{|q_1 q_2|}{r^2}$)."),
            short("vandung", "Hai điện tích điểm có độ lớn bằng nhau $|q_1| = |q_2| = 10^{-6}\\text{ C}$ đặt cách nhau một khoảng $r = 0{,}1\\text{ m}$ trong chân không ($k = 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$). Độ lớn lực tương tác Coulomb giữa hai điện tích bằng bao nhiêu Newton ($\\text{N}$)?", ["0,9", "0.9"], "Áp dụng công thức $F = k\\dfrac{|q_1 q_2|}{r^2} = 9 \\cdot 10^9 \\cdot \\dfrac{10^{-6} \\cdot 10^{-6}}{0{,}1^2} = \\dfrac{9 \\cdot 10^{-3}}{0{,}01} = 0{,}9\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 13: Khái niệm điện trường và cường độ điện trường",
        icon="🌐",
        description="Khái niệm điện trường, vectơ cường độ điện trường E = F/q, điện trường của một điện tích điểm E = k.|Q|/(ε.r²), đường sức điện và nguyên lí chồng chất.",
        requirements=[
            "Nêu được điện trường là dạng vật chất bao quanh điện tích và truyền tương tác giữa các điện tích.",
            "Định nghĩa được vectơ cường độ điện trường $\\vec{E} = \\dfrac{\\vec{F}}{q}$ (đơn vị $\\text{V/m}$ hoặc $\\text{N/C}$) và tính độ lớn điện trường của một điện tích điểm $E = k\\dfrac{|Q|}{\\varepsilon r^2}$.",
            "Mô tả được đường sức điện (ra khỏi điện tích dương, đi vào điện tích âm) và vận dụng nguyên lí chồng chất điện trường $\\vec{E} = \\vec{E}_1 + \\vec{E}_2$.",
        ],
        definition="Điện trường là dạng vật chất (môi trường) bao quanh điện tích và gắn liền với điện tích; điện trường tác dụng lực điện lên các điện tích khác đặt trong nó. Cường độ điện trường tại một điểm là đại lượng vectơ đặc trưng cho độ mạnh yếu của điện trường về phương diện tác dụng lực tại điểm đó: $\\vec{E} = \\dfrac{\\vec{F}}{q}$ (đơn vị $\\text{V/m}$ hoặc $\\text{N/C}$).",
        theory=(
            "### 1. Cường độ điện trường và Lực điện\n"
            "- Định nghĩa: $\\vec{E} = \\dfrac{\\vec{F}}{q} \\implies \\vec{F} = q\\vec{E}$ (độ lớn $F = |q| \\cdot E$):\n"
            "  - Nếu điện tích thử $q > 0$: lực điện $\\vec{F}$ **cùng phương, cùng chiều** với $\\vec{E}$ ($\\vec{F} \\uparrow\\uparrow \\vec{E}$).\n"
            "  - Nếu điện tích thử $q < 0$: lực điện $\\vec{F}$ **cùng phương, ngược chiều** với $\\vec{E}$ ($\\vec{F} \\uparrow\\downarrow \\vec{E}$).\n"
            "- *Lưu ý*: Cường độ điện trường $E$ tại một điểm chỉ phụ thuộc vào điện tích nguồn $Q$ và vị trí điểm đó, **không phụ thuộc vào độ lớn điện tích thử $q$** đặt tại điểm đó.\n\n"
            "### 2. Điện trường của một điện tích điểm $Q$, Đường sức điện và Chồng chất điện trường\n"
            "- Độ lớn cường độ điện trường do điện tích điểm $Q$ gây ra tại điểm cách nó khoảng $r$:\n"
            "  $$E = k\\dfrac{|Q|}{\\varepsilon r^2}$$\n"
            "  - Nếu $Q > 0$: vectơ $\\vec{E}$ hướng **ra xa** điện tích $Q$.\n"
            "  - Nếu $Q < 0$: vectơ $\\vec{E}$ hướng **lại gần (vào)** điện tích $Q$.\n"
            "- **Đường sức điện**: đường mà tiếp tuyến tại mỗi điểm là giá của vectơ $\\vec{E}$ tại điểm đó; xuất phát từ điện tích dương (hoặc ở vô cực) và kết thúc ở điện tích âm (hoặc ở vô cực); các đường sức điện **không bao giờ cắt nhau**.\n"
            "- **Nguyên lí chồng chất điện trường**: $\\vec{E} = \\vec{E}_1 + \\vec{E}_2 + \\dots$"
        ),
        formulas=[
            G(
                "Cường độ điện trường và Nguyên lí chồng chất",
                F("Định nghĩa cường độ điện trường và Lực điện", "$\\vec{E} = \\dfrac{\\vec{F}}{q} \\iff \\vec{F} = q\\vec{E}; \\qquad E = \\dfrac{F}{|q|}$", "Đơn vị của $E$ trong hệ SI là Vôn trên mét ($\\text{V/m}$) hoặc Newton trên Coulomb ($\\text{N/C}$)."),
                F("Cường độ điện trường của một điện tích điểm Q", "$E = k\\dfrac{|Q|}{\\varepsilon r^2} \\quad (Q > 0: \\vec{E} \\text{ hướng ra xa } Q;\\ Q < 0: \\vec{E} \\text{ hướng về } Q)$", "Tổng hợp hai điện trường tại 1 điểm: $\\vec{E} = \\vec{E}_1 + \\vec{E}_2$ (theo quy tắc hình bình hành)."),
            )
        ],
        example="Một điện tích điểm $Q = +4 \\cdot 10^{-8}\\text{ C}$ đặt trong chân không ($\\varepsilon = 1, k = 9 \\cdot 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$). Hãy xác định chiều và độ lớn của vectơ cường độ điện trường $\\vec{E}$ tại điểm $M$ cách $Q$ một khoảng $r = 20\\text{ cm} = 0{,}2\\text{ m}$. Nếu đặt tại $M$ điện tích thử $q = -2 \\cdot 10^{-6}\\text{ C}$ thì độ lớn lực điện $F$ tác dụng lên $q$ là bao nhiêu?",
        example_answer="Vì $Q > 0$ nên tại $M$ vectơ $\\vec{E}$ có phương nối $QM$, chiều hướng **ra xa** $Q$, và độ lớn là $E = k\\dfrac{|Q|}{r^2} = 9 \\cdot 10^9 \\cdot \\dfrac{4 \\cdot 10^{-8}}{0{,}2^2} = \\dfrac{360}{0{,}04} = 9000\\text{ V/m}$. Khi đặt $q = -2 \\cdot 10^{-6}\\text{ C}$ tại $M$, lực điện có chiều ngược với $\\vec{E}$ (hướng về $Q$) và có độ lớn $F = |q|E = 2 \\cdot 10^{-6} \\cdot 9000 = 0{,}018\\text{ N}$.",
        real_life="Lồng Faraday (vỏ kim loại của máy bay, ô tô) chắn điện trường bên ngoài bảo vệ hành khách an toàn ngay cả khi máy bay bị sét đánh trúng trên bầu trời.",
        quiz=[
            mcq("biet", "Đặt một điện tích thử $q$ tại một điểm có cường độ điện trường $\\vec{E}$ thì lực điện tác dụng lên $q$ được xác định bởi biểu thức vectơ nào?", ["$\\vec{F} = q\\vec{E}$", "$\\vec{F} = \\dfrac{\\vec{E}}{q}$", "$\\vec{F} = \\dfrac{q}{\\vec{E}}$", "$\\vec{F} = -q\\vec{E}$ với mọi $q$"], 0, "Theo định nghĩa $\\vec{E} = \\dfrac{\\vec{F}}{q}$, lực điện tác dụng lên điện tích $q$ là $\\vec{F} = q\\vec{E}$."),
            mcq("biet", "Công thức tính độ lớn cường độ điện trường $E$ do một điện tích điểm $Q$ gây ra tại một điểm cách nó một khoảng $r$ trong chân không là gì?", ["$E = k\\dfrac{|Q|}{r^2}$", "$E = k\\dfrac{|Q|}{r}$", "$E = k\\dfrac{Q^2}{r^2}$", "$E = \\dfrac{|Q|}{k r^2}$"], 0, "Độ lớn cường độ điện trường của điện tích điểm $Q$ trong chân không là $E = k\\dfrac{|Q|}{r^2}$."),
            mcq("hieu", "Khi đặt một điện tích thử $q = 2 \\cdot 10^{-6}\\text{ C}$ tại điểm $M$ trong điện trường thì nó chịu lực điện $F = 0{,}04\\text{ N}$. Nếu thay điện tích thử đó bằng điện tích $q' = 4 \\cdot 10^{-6}\\text{ C}$ đặt tại đúng điểm $M$ thì cường độ điện trường $E$ tại điểm $M$ bằng bao nhiêu?", ["$20\\,000\\text{ V/m}$ (không đổi vì $E$ tại $M$ không phụ thuộc vào điện tích thử)", "$40\\,000\\text{ V/m}$", "$10\\,000\\text{ V/m}$", "$0\\text{ V/m}$"], 0, "Cường độ điện trường tại $M$ là $E = \\dfrac{F}{|q|} = \\dfrac{0{,}04}{2 \\cdot 10^{-6}} = 20\\,000\\text{ V/m}$. Giá trị $E$ là đặc trưng của điện trường tại $M$, không phụ thuộc điện tích thử đặt vào."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về điện trường và đường sức điện:", [
                "Nếu điện tích thử $q < 0$ (ví dụ electron) thì lực điện $\\vec{F}$ tác dụng lên nó ngược chiều với vectơ cường độ điện trường $\\vec{E}$.",
                "Vectơ cường độ điện trường do một điện tích điểm âm ($Q < 0$) gây ra luôn hướng về phía điện tích $Q$ đó.",
                "Qua mỗi điểm trong điện trường có thể vẽ được vô số đường sức điện cắt nhau tại điểm đó.",
                "Đơn vị của cường độ điện trường trong hệ SI là Vôn trên mét ($\\text{V/m}$), tương đương với Newton trên Coulomb ($\\text{N/C}$).",
            ], [True, True, False, True], "Ý c) sai vì tại mỗi điểm trong điện trường chỉ có một hướng duy nhất của vectơ $\\vec{E}$ nên qua mỗi điểm chỉ vẽ được **duy nhất một đường sức điện** (các đường sức điện không bao giờ cắt nhau)."),
            short("vandung", "Tại một điểm $A$ có cường độ điện trường $E = 5000\\text{ V/m}$, người ta đặt một điện tích điểm $q = 4 \\cdot 10^{-3}\\text{ C}$. Độ lớn lực điện $F$ tác dụng lên điện tích đó bằng bao nhiêu Newton ($\\text{N}$)?", ["20"], "Áp dụng công thức $F = |q| \\cdot E = 4 \\cdot 10^{-3} \\cdot 5000 = 20\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 14: Điện trường đều",
        icon="⏸️",
        description="Khái niệm điện trường đều giữa hai bản kim loại phẳng song song tích điện trái dấu, công thức E = U/d và chuyển động của điện tích trong điện trường đều.",
        requirements=[
            "Định nghĩa được điện trường đều là điện trường mà vectơ cường độ điện trường $\\vec{E}$ tại mọi điểm đều có cùng phương, cùng chiều và cùng độ lớn; các đường sức điện là những đường thẳng song song cách đều.",
            "Viết và vận dụng được công thức liên hệ giữa cường độ điện trường đều và hiệu điện thế giữa hai bản phẳng song song: $E = \\dfrac{U}{d}$ (hay $U = E \\cdot d$).",
            "Mô tả được quỹ đạo chuyển động dạng parabol của hạt mang điện bay vào điện trường đều theo phương vuông góc với đường sức điện (tương tự chuyển động ném ngang).",
        ],
        definition="Điện trường đều là điện trường mà vectơ cường độ điện trường $\\vec{E}$ tại mọi điểm đều bằng nhau (cùng hướng và cùng độ lớn); các đường sức điện là những đường thẳng song song và cách đều nhau. Giữa hai bản kim loại phẳng song song cách nhau khoảng $d$ có hiệu điện thế $U$, cường độ điện trường đều là $E = \\dfrac{U}{d}$.",
        theory=(
            "### 1. Điện trường đều giữa hai bản kim loại phẳng song song\n"
            "- Hai bản kim loại phẳng lớn đặt song song cách nhau khoảng $d$, tích điện trái dấu có độ lớn bằng nhau tạo ra **điện trường đều** ở khoảng không gian giữa hai bản.\n"
            "- Các đường sức điện là những đường thẳng song song, cách đều và vuông góc với hai bản, có chiều **đi từ bản tích điện dương ($+$) sang bản tích điện âm ($-$)**.\n"
            "- **Độ lớn cường độ điện trường đều**:\n"
            "  $$E = \\dfrac{U}{d} \\iff U = E \\cdot d$$\n"
            "  trong đó $U$ là hiệu điện thế giữa hai bản ($\\text{V}$), $d$ là khoảng cách giữa hai bản ($\\text{m}$), $E$ có đơn vị $\\text{V/m}$.\n\n"
            "### 2. Tác dụng của điện trường đều lên điện tích chuyển động\n"
            "- Điện tích $q$ khối lượng $m$ trong điện trường đều chịu lực điện không đổi $\\vec{F} = q\\vec{E}$ nên thu được gia tốc không đổi $\\vec{a} = \\dfrac{q\\vec{E}}{m}$.\n"
            "- Khi hạt mang điện bay vào điện trường đều với vận tốc đầu $\\vec{v}_0 \\perp \\vec{E}$, hạt chuyển động theo **quỹ đạo nhánh parabol** lệch về phía bản mang điện trái dấu với nó."
        ),
        formulas=[
            G(
                "Cường độ điện trường đều và Chuyển động của hạt mang điện",
                F("Liên hệ giữa cường độ điện trường đều E và hiệu điện thế U", "$E = \\dfrac{U}{d} \\implies U = E \\cdot d$", "Trong đó $U$ là hiệu điện thế giữa hai bản phẳng ($\\text{V}$), $d$ là khoảng cách giữa hai bản phẳng ($\\text{m}$)."),
                F("Gia tốc và độ lệch của hạt mang điện bay vuông góc vào điện trường đều", "$a = \\dfrac{|q|E}{m} = \\dfrac{|q|U}{md}; \\qquad y = \\dfrac{1}{2}at^2 = \\dfrac{1}{2}\\dfrac{|q|E}{m}\\left(\\dfrac{x}{v_0}\\right)^2$", "Quỹ đạo của điện tích bay vuông góc với các đường sức điện là một nhánh parabol."),
            )
        ],
        example="Hai bản kim loại phẳng đặt song song cách nhau một khoảng $d = 2\\text{ cm} = 0{,}02\\text{ m}$ được nối với nguồn điện một chiều có hiệu điện thế $U = 120\\text{ V}$. Hãy tính cường độ điện trường đều $E$ giữa hai bản và lực điện $F$ tác dụng lên một hạt bụi mang điện tích $q = 5 \\cdot 10^{-9}\\text{ C}$ nằm trong khoảng giữa hai bản.",
        example_answer="Đổi $d = 2\\text{ cm} = 0{,}02\\text{ m}$. Cường độ điện trường đều giữa hai bản phẳng là $E = \\dfrac{U}{d} = \\dfrac{120}{0{,}02} = 6000\\text{ V/m}$. Độ lớn lực điện tác dụng lên hạt bụi là $F = |q| \\cdot E = 5 \\cdot 10^{-9} \\cdot 6000 = 3 \\cdot 10^{-5}\\text{ N}$.",
        real_life="Máy in phun mực (Inkjet printer) và dao động kí điện tử sử dụng các cặp bản phẳng tạo điện trường đều để điều khiển góc lệch của các giọt mực tích điện hoặc chùm tia electron bắn chính xác vào từng điểm trên trang giấy hay màn hình.",
        quiz=[
            mcq("biet", "Đặc điểm của các đường sức điện trong một **điện trường đều** là gì?", ["Là những đường thẳng song song, cùng chiều và cách đều nhau", "Là những đường tròn đồng tâm", "Là những đường cong cắt nhau tại một điểm", "Là những đường thẳng xuất phát từ một điểm tỏa ra mọi phía"], 0, "Trong điện trường đều, vectơ $\\vec{E}$ tại mọi điểm đều như nhau nên các đường sức điện là những đường thẳng song song, cùng chiều và cách đều nhau."),
            mcq("biet", "Giữa hai bản kim loại phẳng đặt song song cách nhau một khoảng $d$, tích điện trái dấu dưới hiệu điện thế $U$, độ lớn cường độ điện trường đều $E$ giữa hai bản được tính bằng công thức nào?", ["$E = \\dfrac{U}{d}$", "$E = U \\cdot d$", "$E = \\dfrac{d}{U}$", "$E = \\dfrac{U}{d^2}$"], 0, "Trong điện trường đều giữa hai bản phẳng song song: $E = \\dfrac{U}{d}$."),
            mcq("hieu", "Một electron (mang điện tích âm $q = -e < 0$) bay vào khoảng không gian có điện trường đều giữa hai bản kim loại phẳng song song theo phương vuông góc với các đường sức điện (bỏ qua trọng lực). Quỹ đạo của electron trong điện trường đều có dạng gì và lệch về phía bản nào?", ["Là một nhánh parabol và bị lệch về phía bản tích điện dương ($+$)", "Là một nhánh parabol và bị lệch về phía bản tích điện âm ($-$)", "Là một đường thẳng truyền nguyên hướng ban đầu", "Là một đường tròn khép kín"], 0, "Electron mang điện âm nên chịu lực điện $\\vec{F} = -e\\vec{E}$ ngược chiều đường sức (hướng về phía bản dương $+$) và vuông góc với $\\vec{v}_0$, nên chuyển động theo nhánh parabol lệch về bản dương."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về điện trường đều:", [
                "Trong điện trường đều, vectơ cường độ điện trường $\\vec{E}$ tại mọi điểm đều có cùng hướng và cùng độ lớn.",
                "Đường sức điện giữa hai bản phẳng song song tích điện trái dấu có chiều hướng từ bản tích điện dương sang bản tích điện âm.",
                "Nếu giữ nguyên hiệu điện thế $U$ và tăng khoảng cách $d$ giữa hai bản lên gấp đôi thì cường độ điện trường $E$ tăng gấp đôi.",
                "Để một giọt dầu mang điện tích âm ($q < 0$) nằm lơ lửng cân bằng giữa hai bản phẳng nằm ngang thì bản kim loại phía trên phải tích điện dương ($+$) để lực điện hướng lên cân bằng với trọng lực.",
            ], [True, True, False, True], "Ý c) sai vì $E = \\dfrac{U}{d}$ tỉ lệ nghịch với $d$, nên khi $U$ không đổi mà $d$ tăng gấp đôi thì $E$ giảm đi $2$ lần."),
            short("vandung", "Hai bản kim loại phẳng đặt song song cách nhau $d = 4\\text{ cm} = 0{,}04\\text{ m}$, hiệu điện thế giữa hai bản là $U = 200\\text{ V}$. Cường độ điện trường đều $E$ ở khoảng giữa hai bản bằng bao nhiêu $\\text{V/m}$?", ["5000"], "Đổi $d = 0{,}04\\text{ m}$. Áp dụng công thức $E = \\dfrac{U}{d} = \\dfrac{200}{0{,}04} = 5000\\text{ V/m}$.", unit="V/m"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 15: Thế năng điện và công của lực điện",
        icon="🔋",
        description="Công của lực điện trong điện trường đều A_MN = q.E.d, tính chất thế của trường tĩnh điện và thế năng điện W_M = A_M∞ = q.V_M.",
        requirements=[
            "Viết và vận dụng được công thức tính công của lực điện khi điện tích $q$ di chuyển từ $M$ đến $N$ trong điện trường đều: $A_{MN} = q \\cdot E \\cdot d$ (với $d = s\\cos\\alpha$ là hình chiếu độ dịch chuyển $\\vec{MN}$ lên phương đường sức điện).",
            "Nêu được công của lực tĩnh điện không phụ thuộc vào hình dạng của đường đi mà chỉ phụ thuộc vào vị trí điểm đầu $M$ và điểm cuối $N$ (trường tĩnh điện là một trường thế).",
            "Định nghĩa được thế năng của một điện tích $q$ tại điểm $M$ trong điện trường: $W_M = A_{M\\infty}$ và liên hệ $A_{MN} = W_M - W_N$.",
        ],
        definition="Công của lực điện làm dịch chuyển điện tích $q$ từ điểm $M$ đến điểm $N$ trong điện trường đều là $A_{MN} = q \\cdot E \\cdot d$, trong đó $d$ là độ dài đại số hình chiếu của đoạn $MN$ lên một đường sức điện. Công của lực tĩnh điện không phụ thuộc vào hình dạng đường đi mà chỉ phụ thuộc vào vị trí điểm đầu $M$ và điểm cuối $N$.",
        theory=(
            "### 1. Công của lực điện trong điện trường đều\n"
            "- Khi điện tích $q$ di chuyển từ $M$ đến $N$ trong điện trường đều $\\vec{E}$:\n"
            "  $$A_{MN} = q \\cdot E \\cdot d = q \\cdot E \\cdot MN \\cdot \\cos\\alpha$$\n"
            "  trong đó $\\alpha = (\\widehat{\\vec{E}, \\vec{MN}})$ và $d = M'N' = MN\\cos\\alpha$ là độ dài đại số hình chiếu của $\\vec{MN}$ lên phương đường sức điện:\n"
            "  - Nếu đi xuôi chiều đường sức ($0^\\circ \\le \\alpha < 90^\\circ$): $d > 0$.\n"
            "  - Nếu đi ngược chiều đường sức ($90^\\circ < \\alpha \\le 180^\\circ$): $d < 0$.\n"
            "  - Nếu đi vuông góc với đường sức ($\\alpha = 90^\\circ$): $d = 0 \\implies A_{MN} = 0$.\n"
            "- **Tính chất**: Công của lực tĩnh điện **không phụ thuộc vào hình dạng đường đi**, chỉ phụ thuộc vào vị trí điểm đầu $M$ và điểm cuối $N$. Do đó công của lực tĩnh điện trên một đường cong kín bất kì luôn bằng không ($A_{\\text{kín}} = 0$).\n\n"
            "### 2. Thế năng của một điện tích trong điện trường\n"
            "- **Thế năng điện ($W_M$)** của điện tích $q$ tại điểm $M$ đặc trưng cho khả năng sinh công của điện trường khi đặt $q$ tại $M$, được đo bằng công của lực điện khi dịch chuyển $q$ từ $M$ ra xa vô cực (mốc thế năng tại $\\infty$): $W_M = A_{M\\infty}$.\n"
            "- **Liên hệ giữa công của lực điện và độ giảm thế năng điện**:\n"
            "  $$A_{MN} = W_M - W_N$$"
        ),
        formulas=[
            G(
                "Công của lực điện và Thế năng điện",
                F("Công của lực điện trong điện trường đều", "$A_{MN} = q \\cdot E \\cdot d = q \\cdot E \\cdot s \\cdot \\cos\\alpha$", "Chú ý thay cả dấu âm/dương của điện tích $q$ và dấu đại số của $d = s\\cos\\alpha$ vào công thức!"),
                F("Liên hệ giữa công của lực điện và thế năng điện", "$W_M = A_{M\\infty}; \\qquad A_{MN} = W_M - W_N$", "Trên mọi quỹ đạo khép kín (đi từ $M$ rồi quay lại đúng $M$): $A_{MM} = W_M - W_M = 0$."),
            )
        ],
        example="Một điện tích $q = +2 \\cdot 10^{-6}\\text{ C}$ di chuyển dọc theo chiều của một đường sức điện trong một điện trường đều có cường độ $E = 1000\\text{ V/m}$ trên quãng đường dài $s = 5\\text{ cm} = 0{,}05\\text{ m}$. Hãy tính công của lực điện thực hiện trong dịch chuyển đó.",
        example_answer="Vì điện tích di chuyển dọc theo chiều đường sức điện nên $\\alpha = 0^\\circ$ và $d = +s = 0{,}05\\text{ m}$. Công của lực điện là $A = q \\cdot E \\cdot d = 2 \\cdot 10^{-6} \\cdot 1000 \\cdot 0{,}05 = 10^{-4}\\text{ J} = 0{,}1\\text{ mJ}$.",
        real_life="Trong các máy gia tốc hạt và ống phóng tia X, công của lực điện $A_{MN} = W_M - W_N$ được chuyển hóa hoàn toàn thành động năng cực lớn của các hạt mang điện theo định lí động năng.",
        quiz=[
            mcq("biet", "Công thức tính công $A_{MN}$ của lực điện tác dụng lên điện tích $q$ khi nó di chuyển từ điểm $M$ đến điểm $N$ trong điện trường đều có cường độ $E$ là gì (với $d$ là hình chiếu đại số của $\\vec{MN}$ lên đường sức)?", ["$A_{MN} = q \\cdot E \\cdot d$", "$A_{MN} = \\dfrac{q \\cdot E}{d}$", "$A_{MN} = q^2 E d$", "$A_{MN} = \\dfrac{E \\cdot d}{q}$"], 0, "Công của lực điện trong điện trường đều được tính bởi công thức $A_{MN} = q \\cdot E \\cdot d$."),
            mcq("biet", "Công của lực tĩnh điện khi làm dịch chuyển một điện tích $q$ từ điểm $M$ đến điểm $N$ trong điện trường có tính chất đặc biệt nào?", ["Không phụ thuộc vào hình dạng của đường đi mà chỉ phụ thuộc vào vị trí điểm đầu $M$ và điểm cuối $N$", "Tỉ lệ thuận với độ dài quãng đường cong mà điện tích đã đi", "Luôn bằng không đối với mọi cặp điểm $M, N$ bất kì", "Chỉ phụ thuộc vào khối lượng của hạt mang điện"], 0, "Trường tĩnh điện là một trường thế, nên công của lực tĩnh điện chỉ phụ thuộc vị trí điểm đầu và điểm cuối, không phụ thuộc hình dạng đường đi."),
            mcq("hieu", "Khi một điện tích $q$ di chuyển dọc theo một đường cong khép kín bất kì trong điện trường tĩnh rồi quay trở về đúng điểm xuất phát ban đầu thì công của lực điện bằng bao nhiêu?", ["$A = 0$", "$A > 0$", "$A < 0$", "$A = 2qEd$"], 0, "Khi điểm cuối trùng với điểm đầu ($N \\equiv M$), độ giảm thế năng $A_{MM} = W_M - W_M = 0$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về công của lực điện và thế năng điện:", [
                "Nếu điện tích di chuyển trên một đoạn thẳng vuông góc với các đường sức của điện trường đều ($d = 0$) thì công của lực điện bằng $0$.",
                "Khi điện tích dương ($q > 0$) dịch chuyển cùng chiều đường sức điện ($d > 0$) thì lực điện sinh công dương ($A > 0$) và thế năng điện giảm.",
                "Khi điện tích âm ($q < 0$) dịch chuyển cùng chiều đường sức điện ($d > 0$) thì lực điện cũng sinh công dương.",
                "Hiệu thế năng điện giữa hai điểm $M$ và $N$ bằng công của lực điện dịch chuyển điện tích từ $M$ đến $N$: $W_M - W_N = A_{MN}$.",
            ], [True, True, False, True], "Ý c) sai vì khi $q < 0$ đi cùng chiều đường sức ($d > 0$), lực điện ngược chiều đường sức nên sinh công âm ($A = qEd < 0$)."),
            short("vandung", "Một điện tích $q = 5 \\cdot 10^{-3}\\text{ C}$ di chuyển dọc theo chiều đường sức của một điện trường đều $E = 2000\\text{ V/m}$ đi được một đoạn $d = 0{,}4\\text{ m}$. Công của lực điện bằng bao nhiêu Joule ($\\text{J}$)?", ["4"], "Áp dụng công thức $A = q \\cdot E \\cdot d = 5 \\cdot 10^{-3} \\cdot 2000 \\cdot 0{,}4 = 4\\text{ J}$.", unit="J"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 16: Điện thế và hiệu điện thế",
        icon="⚡",
        description="Khái niệm điện thế V_M = W_M/q = A_M∞/q, hiệu điện thế U_MN = V_M - V_N = A_MN/q = E.d và đơn vị electron-vôn (eV).",
        requirements=[
            "Định nghĩa được điện thế tại một điểm trong điện trường $V_M = \\dfrac{W_M}{q} = \\dfrac{A_{M\\infty}}{q}$ và hiệu điện thế giữa hai điểm $U_{MN} = V_M - V_N = \\dfrac{A_{MN}}{q}$ (đơn vị Vôn – $\\text{V}$).",
            "Vận dụng được công thức tính công của lực điện theo hiệu điện thế $A_{MN} = q \\cdot U_{MN}$ và hệ thức liên hệ $U_{MN} = E \\cdot d_{MN}$ (chiều đường sức điện luôn hướng từ nơi có điện thế cao sang nơi có điện thế thấp).",
            "Đổi được đơn vị năng lượng electron-vôn ($1\\text{ eV} = 1{,}6 \\cdot 10^{-19}\\text{ J}$) và vận dụng định lí động năng $\\dfrac{1}{2}mv_N^2 - \\dfrac{1}{2}mv_M^2 = q U_{MN}$.",
        ],
        definition="Điện thế tại một điểm $M$ trong điện trường là đại lượng đặc trưng riêng cho điện trường về phương diện tạo ra thế năng tại điểm đó: $V_M = \\dfrac{W_M}{q} = \\dfrac{A_{M\\infty}}{q}$ (đơn vị Vôn – $\\text{V}$). Hiệu điện thế giữa hai điểm $M$ và $N$ là $U_{MN} = V_M - V_N = \\dfrac{A_{MN}}{q}$.",
        theory=(
            "### 1. Điện thế và Hiệu điện thế\n"
            "- **Điện thế tại điểm $M$**: $V_M = \\dfrac{W_M}{q} = \\dfrac{A_{M\\infty}}{q}$ (phụ thuộc vào vị trí chọn làm mốc điện thế $V = 0$, thường chọn ở mặt đất hoặc ở vô cực; nhưng **không phụ thuộc vào điện tích thử $q$**).\n"
            "- **Hiệu điện thế giữa hai điểm $M$ và $N$**:\n"
            "  $$U_{MN} = V_M - V_N = \\dfrac{W_M - W_N}{q} = \\dfrac{A_{MN}}{q} \\implies A_{MN} = q \\cdot U_{MN}$$\n"
            "- Đơn vị của điện thế và hiệu điện thế là **Vôn** ($\\text{V}$), với $1\\text{ V} = 1\\text{ J/C}$. Lưu ý: $U_{MN} = -U_{NM}$.\n\n"
            "### 2. Liên hệ giữa $E$ và $U$ & Đơn vị electron-vôn ($\\text{eV}$)\n"
            "- Trong điện trường đều: $A_{MN} = q U_{MN} = q E d_{MN}$, suy ra:\n"
            "  $$U_{MN} = V_M - V_N = E \\cdot d_{MN} \\iff E = \\dfrac{U_{MN}}{d_{MN}}$$\n"
            "  Vì dọc theo chiều đường sức điện có $d_{MN} > 0 \\implies V_M > V_N$, nên **vectơ cường độ điện trường $\\vec{E}$ luôn hướng theo chiều giảm của điện thế**.\n"
            "- **Đơn vị năng lượng electron-vôn ($\\text{eV}$)**: năng lượng mà $1$ electron (hoặc proton) thu được khi đi qua hiệu điện thế $1\\text{ V}$:\n"
            "  $$1\\text{ eV} = 1{,}6 \\cdot 10^{-19}\\text{ C} \\cdot 1\\text{ V} = 1{,}6 \\cdot 10^{-19}\\text{ J}; \\qquad 1\\text{ MeV} = 10^6\\text{ eV} = 1{,}6 \\cdot 10^{-13}\\text{ J}$$"
        ),
        formulas=[
            G(
                "Điện thế, Hiệu điện thế và Công của lực điện",
                F("Biểu thức Điện thế và Hiệu điện thế", "$V_M = \\dfrac{A_{M\\infty}}{q}; \\qquad U_{MN} = V_M - V_N = \\dfrac{A_{MN}}{q} \\iff A_{MN} = q \\cdot U_{MN}$", "Công thức $A_{MN} = q U_{MN}$ đúng cho **mọi điện trường** (cả điện trường đều lẫn không đều)."),
                F("Liên hệ với cường độ điện trường và Định lí động năng", "$U_{MN} = E \\cdot d_{MN}; \\qquad \\dfrac{1}{2}mv_N^2 - \\dfrac{1}{2}mv_M^2 = q \\cdot U_{MN}; \\qquad 1\\text{ eV} = 1{,}6 \\cdot 10^{-19}\\text{ J}$", "Đi theo chiều đường sức điện thì điện thế giảm dần ($V_M > V_N$)."),
            )
        ],
        example="Hiệu điện thế giữa hai điểm $M$ và $N$ trong một điện trường là $U_{MN} = V_M - V_N = 50\\text{ V}$. Hãy tính công của lực điện khi làm dịch chuyển một điện tích $q = 4 \\cdot 10^{-4}\\text{ C}$ từ $M$ đến $N$. Nếu chọn mốc điện thế tại $N$ bằng $0$ ($V_N = 0\\text{ V}$) thì điện thế tại $M$ bằng bao nhiêu?",
        example_answer="Công của lực điện khi dịch chuyển $q$ từ $M$ đến $N$ là $A_{MN} = q \\cdot U_{MN} = 4 \\cdot 10^{-4} \\cdot 50 = 0{,}02\\text{ J}$. Nếu $V_N = 0\\text{ V}$ thì điện thế tại $M$ là $V_M = U_{MN} + V_N = 50 + 0 = 50\\text{ V}$.",
        real_life="Hiệu điện thế giữa đám mây dông tích điện và mặt đất có thể lên tới hàng trăm triệu Vôn ($10^8\\text{ V}$), tạo ra tia sét phóng điện mạnh trong cơn giông.",
        quiz=[
            mcq("biet", "Hệ thức liên hệ giữa hiệu điện thế $U_{MN} = V_M - V_N$, điện tích $q$ và công của lực điện $A_{MN}$ khi dịch chuyển $q$ từ $M$ đến $N$ là gì?", ["$U_{MN} = \\dfrac{A_{MN}}{q} \\iff A_{MN} = q \\cdot U_{MN}$", "$U_{MN} = q \\cdot A_{MN}$", "$U_{MN} = \\dfrac{q}{A_{MN}}$", "$U_{MN} = A_{MN} + q$"], 0, "Theo định nghĩa, hiệu điện thế giữa hai điểm $M$ và $N$ bằng thương số giữa công $A_{MN}$ và điện tích $q$: $U_{MN} = \\dfrac{A_{MN}}{q}$."),
            mcq("biet", "Đổi đơn vị năng lượng: $1\\text{ eV}$ (electron-vôn) bằng bao nhiêu Joule ($\\text{J}$)?", ["$1{,}6 \\cdot 10^{-19}\\text{ J}$", "$9{,}1 \\cdot 10^{-31}\\text{ J}$", "$1{,}6 \\cdot 10^{-13}\\text{ J}$", "$3 \\cdot 10^8\\text{ J}$"], 0, "Ta có $1\\text{ eV} = |e| \\cdot 1\\text{ V} = 1{,}6 \\cdot 10^{-19}\\text{ J}$."),
            mcq("hieu", "Một đường sức điện trong điện trường có chiều đi từ điểm $M$ đến điểm $N$. Khi so sánh điện thế tại $M$ ($V_M$) và điện thế tại $N$ ($V_N$), kết luận nào sau đây là đúng?", ["$V_M > V_N$ (điện thế giảm dần theo chiều của đường sức điện)", "$V_M < V_N$", "$V_M = V_N = 0$", "Không so sánh được"], 0, "Vì $U_{MN} = V_M - V_N = E \\cdot d_{MN} > 0$ khi đi từ $M$ đến $N$ theo chiều đường sức điện, nên $V_M > V_N$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về điện thế và hiệu điện thế:", [
                "Điện thế tại một điểm phụ thuộc vào việc chọn mốc điện thế, nhưng hiệu điện thế $U_{MN} = V_M - V_N$ giữa hai điểm thì không phụ thuộc vào việc chọn mốc điện thế.",
                "Hiệu điện thế giữa hai điểm thỏa mãn hệ thức $U_{MN} = -U_{NM}$.",
                "Mặt đẳng thế là mặt gồm các điểm có cùng điện thế; khi điện tích di chuyển trên mặt đẳng thế thì lực điện sinh công cực đại.",
                "Công của lực điện làm dịch chuyển điện tích $q = 2\\text{ C}$ qua hiệu điện thế $U = 12\\text{ V}$ là $A = 24\\text{ J}$.",
            ], [True, True, False, True], "Ý c) sai vì trên mặt đẳng thế có $V_M = V_N \\implies U_{MN} = 0$, nên công của lực điện bằng $0$ ($A_{MN} = q U_{MN} = 0$)."),
            short("vandung", "Khi dịch chuyển một điện tích $q = 0{,}02\\text{ C}$ từ điểm $M$ đến điểm $N$ trong điện trường thì lực điện thực hiện một công $A_{MN} = 3\\text{ J}$. Hiệu điện thế $U_{MN}$ giữa hai điểm đó bằng bao nhiêu Vôn ($\\text{V}$)?", ["150"], "Áp dụng công thức $U_{MN} = \\dfrac{A_{MN}}{q} = \\dfrac{3}{0{,}02} = 150\\text{ V}$.", unit="V"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 17: Tụ điện và năng lượng của tụ điện",
        icon="🔋",
        description="Cấu tạo tụ điện, công thức điện dung C = Q/U (F, μF, nF, pF), ghép tụ điện nối tiếp và song song, năng lượng của tụ điện W = ½CU² = ½QU = Q²/(2C).",
        requirements=[
            "Nêu được cấu tạo của tụ điện (hai vật dẫn đặt gần nhau và ngăn cách nhau bằng một lớp cách điện – điện môi) và định nghĩa điện dung $C = \\dfrac{Q}{U}$ (đơn vị Fara – $\\text{F}$).",
            "Vận dụng được công thức ghép tụ điện nối tiếp ($\\dfrac{1}{C_b} = \\dfrac{1}{C_1} + \\dfrac{1}{C_2}, Q_b = Q_1 = Q_2$) và ghép song song ($C_b = C_1 + C_2, U_b = U_1 = U_2$).",
            "Tính được năng lượng điện trường tích trữ trong tụ điện: $W = \\dfrac{1}{2}CU^2 = \\dfrac{1}{2}QU = \\dfrac{Q^2}{2C}$.",
        ],
        definition="Tụ điện là một hệ hai vật dẫn đặt gần nhau và ngăn cách nhau bằng một lớp cách điện (điện môi), dùng để tích và phóng điện trong mạch. Điện dung của tụ điện là đại lượng đặc trưng cho khả năng tích điện của tụ điện ở một hiệu điện thế nhất định: $C = \\dfrac{Q}{U}$ (đơn vị Fara – $\\text{F}$).",
        theory=(
            "### 1. Điện dung của tụ điện\n"
            "- Công thức định nghĩa: $C = \\dfrac{Q}{U} \\implies Q = C \\cdot U$.\n"
            "  - *Lưu ý*: Điện dung $C$ chỉ phụ thuộc vào cấu tạo hình học của tụ điện và chất điện môi ($C = \\dfrac{\\varepsilon S}{4\\pi k d}$ với tụ phẳng), **không phụ thuộc vào $Q$ và $U$**.\n"
            "- Đơn vị điện dung là **Fara** ($\\text{F}$). Các ước thông dụng:\n"
            "  $$1\\text{ mF} = 10^{-3}\\text{ F}; \\quad 1\\text{ }\\mu\\text{F} = 10^{-6}\\text{ F}; \\quad 1\\text{ nF} = 10^{-9}\\text{ F}; \\quad 1\\text{ pF} = 10^{-12}\\text{ F}$$\n"
            "- Trên vỏ tụ điện luôn ghi $C$ và **hiệu điện thế giới hạn $U_{\\text{gh}}$** (hiệu điện thế tối đa đặt vào tụ để lớp điện môi không bị đánh thủng).\n\n"
            "### 2. Ghép tụ điện và Năng lượng của tụ điện\n"
            "- **Ghép song song**: $U_b = U_1 = U_2; \\quad Q_b = Q_1 + Q_2; \\quad C_b = C_1 + C_2 + \\dots$ ($C_b$ tăng).\n"
            "- **Ghép nối tiếp**: $Q_b = Q_1 = Q_2; \\quad U_b = U_1 + U_2; \\quad \\dfrac{1}{C_b} = \\dfrac{1}{C_1} + \\dfrac{1}{C_2} \\iff C_b = \\dfrac{C_1 C_2}{C_1 + C_2}$ ($C_b$ giảm).\n"
            "- **Năng lượng của tụ điện** (năng lượng điện trường trong lớp điện môi):\n"
            "  $$W = \\dfrac{1}{2}CU^2 = \\dfrac{1}{2}QU = \\dfrac{Q^2}{2C}$$"
        ),
        formulas=[
            G(
                "Điện dung, Ghép tụ điện và Năng lượng tụ điện",
                F("Điện dung và Ghép bộ tụ điện", "$Q = C \\cdot U; \\qquad \\text{Song song: } C_b = C_1 + C_2; \\qquad \\text{Nối tiếp: } \\dfrac{1}{C_b} = \\dfrac{1}{C_1} + \\dfrac{1}{C_2} \\implies C_b = \\dfrac{C_1 C_2}{C_1 + C_2}$", "Chú ý công thức tính $C_b$ của bộ tụ điện ngược hình thức với công thức $R_{\\text{tđ}}$ của điện trở!"),
                F("Năng lượng điện trường trong tụ điện", "$W = \\dfrac{1}{2}CU^2 = \\dfrac{1}{2}QU = \\dfrac{Q^2}{2C}$", "Đổi đơn vị: $1\\text{ }\\mu\\text{F} = 10^{-6}\\text{ F}$; $1\\text{ nF} = 10^{-9}\\text{ F}$; $1\\text{ pF} = 10^{-12}\\text{ F}$."),
            )
        ],
        example="Một tụ điện có điện dung $C = 20\\text{ }\\mu\\text{F} = 20 \\cdot 10^{-6}\\text{ F}$ được tích điện dưới hiệu điện thế $U = 100\\text{ V}$. Hãy tính điện tích $Q$ và năng lượng điện trường $W$ tích trữ trong tụ điện.",
        example_answer="Điện tích của tụ điện là $Q = C \\cdot U = 20 \\cdot 10^{-6} \\cdot 100 = 2 \\cdot 10^{-3}\\text{ C} = 2\\text{ mC}$. Năng lượng tích trữ trong tụ điện là $W = \\dfrac{1}{2}CU^2 = \\dfrac{1}{2} \\cdot 20 \\cdot 10^{-6} \\cdot 100^2 = 0{,}1\\text{ J}$.",
        real_life="Đèn flash máy ảnh, máy khử rung tim cấp cứu và bộ lưu nguồn tạm thời trên bo mạch máy tính đều dùng tụ điện có điện dung lớn để tích điện rồi phóng năng lượng cực nhanh trong thời gian rất ngắn.",
        quiz=[
            mcq("biet", "Công thức định nghĩa điện dung $C$ của một tụ điện tích được điện tích $Q$ dưới hiệu điện thế $U$ là gì?", ["$C = \\dfrac{Q}{U}$", "$C = Q \\cdot U$", "$C = \\dfrac{U}{Q}$", "$C = \\dfrac{1}{2}QU^2$"], 0, "Điện dung của tụ điện được xác định bằng thương số $C = \\dfrac{Q}{U}$."),
            mcq("biet", "Khi ghép **song song** hai tụ điện có điện dung $C_1$ và $C_2$ thì điện dung tương đương $C_b$ của bộ tụ được tính theo công thức nào?", ["$C_b = C_1 + C_2$", "$\\dfrac{1}{C_b} = \\dfrac{1}{C_1} + \\dfrac{1}{C_2}$", "$C_b = \\dfrac{C_1 \\cdot C_2}{C_1 + C_2}$", "$C_b = |C_1 - C_2|$"], 0, "Khi ghép song song các tụ điện, điện dung tương đương bằng tổng các điện dung thành phần: $C_b = C_1 + C_2$."),
            mcq("hieu", "Cho hai tụ điện có điện dung $C_1 = 3\\text{ }\\mu\\text{F}$ và $C_2 = 6\\text{ }\\mu\\text{F}$ ghép **nối tiếp** với nhau. Điện dung tương đương $C_b$ của bộ tụ này bằng bao nhiêu?", ["$2\\text{ }\\mu\\text{F}$", "$9\\text{ }\\mu\\text{F}$", "$3\\text{ }\\mu\\text{F}$", "$18\\text{ }\\mu\\text{F}$"], 0, "Khi ghép nối tiếp: $C_b = \\dfrac{C_1 \\cdot C_2}{C_1 + C_2} = \\dfrac{3 \\cdot 6}{3 + 6} = \\dfrac{18}{9} = 2\\text{ }\\mu\\text{F}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tụ điện:", [
                "Đơn vị đo điện dung trong hệ SI là Fara ($\\text{F}$), với $1\\text{ }\\mu\\text{F} = 10^{-6}\\text{ F}$ và $1\\text{ pF} = 10^{-12}\\text{ F}$.",
                "Điện dung $C$ của một tụ điện cố định tỉ lệ thuận với hiệu điện thế $U$ đặt vào hai bản tụ.",
                "Trên vỏ một tụ điện ghi '$100\\text{ }\\mu\\text{F} - 250\\text{ V}$' thì $250\\text{ V}$ là hiệu điện thế giới hạn tối đa được phép đặt vào tụ.",
                "Năng lượng của tụ điện được tính bằng công thức $W = \\dfrac{1}{2}CU^2 = \\dfrac{1}{2}QU = \\dfrac{Q^2}{2C}$.",
            ], [True, False, True, True], "Ý b) sai vì điện dung $C$ chỉ phụ thuộc vào cấu tạo của bản thân tụ điện (diện tích bản, khoảng cách hai bản, chất điện môi), không phụ thuộc vào $U$ và $Q$."),
            short("vandung", "Một tụ điện có điện dung $C = 50\\text{ }\\mu\\text{F} = 50 \\cdot 10^{-6}\\text{ F}$ được tích điện ở hiệu điện thế $U = 20\\text{ V}$. Năng lượng $W$ tích trữ trong tụ điện bằng bao nhiêu miliJoule ($\\text{mJ}$, biết $1\\text{ J} = 1000\\text{ mJ}$)?", ["10"], "Ta có $W = \\dfrac{1}{2}CU^2 = \\dfrac{1}{2} \\cdot 50 \\cdot 10^{-6} \\cdot 20^2 = 0{,}01\\text{ J} = 10\\text{ mJ}$.", unit="mJ"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 18: Cường độ dòng điện và vận tốc trôi",
        icon="🔌",
        description="Định nghĩa cường độ dòng điện I = Δq/Δt, đơn vị điện lượng Coulomb (1 C = 1 A.s), số electron đi qua tiết diện và công thức vận tốc trôi I = S.n.v.e.",
        requirements=[
            "Định nghĩa được cường độ dòng điện là đại lượng đặc trưng cho tác dụng mạnh yếu của dòng điện, bằng điện lượng $\\Delta q$ chuyển qua tiết diện thẳng của vật dẫn trong một đơn vị thời gian: $I = \\dfrac{\\Delta q}{\\Delta t}$.",
            "Tính được điện lượng $\\Delta q = I \\cdot \\Delta t$ và số electron tự do đi qua tiết diện dây dẫn: $N_e = \\dfrac{\\Delta q}{e} = \\dfrac{I \\cdot \\Delta t}{1{,}6 \\cdot 10^{-19}}$.",
            "Viết và vận dụng được công thức liên hệ giữa cường độ dòng điện và tốc độ dịch chuyển có hướng (vận tốc trôi $v$) của các hạt mang điện: $I = S \\cdot n \\cdot v \\cdot e$.",
        ],
        definition="Cường độ dòng điện ($I$) được xác định bằng thương số giữa điện lượng $\\Delta q$ dịch chuyển qua tiết diện thẳng của vật dẫn trong khoảng thời gian $\\Delta t$ và khoảng thời gian đó: $I = \\dfrac{\\Delta q}{\\Delta t}$. Với dòng điện không đổi: $I = \\dfrac{q}{t} \\implies q = I \\cdot t$.",
        theory=(
            "### 1. Cường độ dòng điện và Điện lượng\n"
            "- Biểu thức tổng quát: $I = \\dfrac{\\Delta q}{\\Delta t}$. Với **dòng điện không đổi** (có chiều và cường độ không đổi theo thời gian):\n"
            "  $$I = \\dfrac{q}{t} \\iff q = I \\cdot t$$\n"
            "- Đơn vị: cường độ dòng điện là **Ampe** ($\\text{A}$), điện lượng là **Coulomb** ($\\text{C}$), với $1\\text{ C} = 1\\text{ A}\\cdot\\text{s}$ (ngoài ra dung lượng pin, ắc quy thường ghi bằng Ampe-giờ: $1\\text{ Ah} = 3600\\text{ C}$; $1\\text{ mAh} = 3{,}6\\text{ C}$).\n"
            "- Số electron tự do đi qua tiết diện thẳng của dây dẫn trong thời gian $t$: $N = \\dfrac{q}{e} = \\dfrac{I \\cdot t}{1{,}6 \\cdot 10^{-19}}$.\n\n"
            "### 2. Bản chất dòng điện trong kim loại và Vận tốc trôi ($v$)\n"
            "- Trong kim loại, các **electron tự do** chuyển động nhiệt hỗn loạn rất nhanh ($10^5 - 10^6\\text{ m/s}$); khi có điện trường ngoài, chúng đồng thời dịch chuyển có hướng ngược chiều điện trường với **vận tốc trôi $v$** rất nhỏ (cỡ $10^{-4} - 10^{-3}\\text{ m/s}$).\n"
            "- Công thức liên hệ:\n"
            "  $$I = S \\cdot n \\cdot v \\cdot e$$\n"
            "  trong đó $S$ là tiết diện thẳng của dây dẫn ($\\text{m}^2$), $n$ là mật độ hạt mang điện tự do (số electron tự do trong $1\\text{ m}^3$), $v$ là tốc độ dịch chuyển có hướng (vận tốc trôi, $\\text{m/s}$) và $e = 1{,}6 \\cdot 10^{-19}\\text{ C}$."
        ),
        formulas=[
            G(
                "Cường độ dòng điện, Điện lượng và Vận tốc trôi",
                F("Cường độ dòng điện không đổi và Số hạt electron dịch chuyển", "$I = \\dfrac{q}{t} \\iff q = I \\cdot t; \\qquad N_e = \\dfrac{q}{e} = \\dfrac{I \\cdot t}{1{,}6 \\cdot 10^{-19}}$", "Đơn vị: $1\\text{ C} = 1\\text{ A}\\cdot\\text{s}$; $1\\text{ Ah} = 3600\\text{ C}$."),
                F("Liên hệ giữa cường độ dòng điện và vận tốc trôi v", "$I = S \\cdot n \\cdot v \\cdot e \\implies v = \\dfrac{I}{S \\cdot n \\cdot e}$", "Trong đó $S$ là tiết diện dây ($\\text{m}^2$), $n$ là mật độ electron tự do ($\\text{m}^{-3}$), $v$ là tốc độ trôi ($\\text{m/s}$)."),
            )
        ],
        example="Một dòng điện không đổi có cường độ $I = 1{,}6\\text{ A}$ chạy qua một dây dẫn bằng đồng. Hãy tính điện lượng $q$ và số electron tự do $N_e$ dịch chuyển qua tiết diện thẳng của dây dẫn trong thời gian $t = 5\\text{ s}$ (biết $e = 1{,}6 \\cdot 10^{-19}\\text{ C}$).",
        example_answer="Điện lượng chuyển qua tiết diện dây trong $5\\text{ s}$ là $q = I \\cdot t = 1{,}6 \\cdot 5 = 8\\text{ C}$. Số electron tự do đi qua tiết diện dây trong thời gian đó là $N_e = \\dfrac{q}{e} = \\dfrac{8}{1{,}6 \\cdot 10^{-19}} = 5 \\cdot 10^{19}$ hạt.",
        real_life="Pin điện thoại thông minh thường ghi dung lượng $5000\\text{ mAh} = 5\\text{ Ah}$, tương ứng với tổng điện lượng $q = 5 \\cdot 3600 = 18\\,000\\text{ C}$ mà pin có thể cung cấp trước khi phải sạc lại.",
        quiz=[
            mcq("biet", "Công thức định nghĩa cường độ dòng điện $I$ theo điện lượng $\\Delta q$ dịch chuyển qua tiết diện thẳng của vật dẫn trong thời gian $\\Delta t$ là gì?", ["$I = \\dfrac{\\Delta q}{\\Delta t}$", "$I = \\Delta q \\cdot \\Delta t$", "$I = \\dfrac{\\Delta t}{\\Delta q}$", "$I = \\Delta q + \\Delta t$"], 0, "Cường độ dòng điện bằng điện lượng chuyển qua tiết diện thẳng trong một đơn vị thời gian: $I = \\dfrac{\\Delta q}{\\Delta t}$."),
            mcq("biet", "Biểu thức liên hệ giữa cường độ dòng điện $I$ trong dây dẫn kim loại với tiết diện dây $S$, mật độ electron tự do $n$, độ lớn điện tích nguyên tố $e$ và vận tốc trôi $v$ là gì?", ["$I = S \\cdot n \\cdot v \\cdot e$", "$I = \\dfrac{S \\cdot n \\cdot e}{v}$", "$I = \\dfrac{v \\cdot e}{S \\cdot n}$", "$I = S \\cdot v^2 \\cdot e$"], 0, "Cường độ dòng điện liên hệ với vận tốc trôi theo công thức $I = S \\cdot n \\cdot v \\cdot e$."),
            mcq("hieu", "Trong thời gian $t = 1\\text{ s}$, có một điện lượng $q = 3{,}2\\text{ C}$ chuyển qua tiết diện thẳng của dây dẫn kim loại. Số electron tự do đi qua tiết diện đó trong $1\\text{ s}$ là bao nhiêu (với $e = 1{,}6 \\cdot 10^{-19}\\text{ C}$)?", ["$2 \\cdot 10^{19}$ electron", "$1{,}6 \\cdot 10^{19}$ electron", "$5{,}12 \\cdot 10^{-19}$ electron", "$0{,}5 \\cdot 10^{19}$ electron"], 0, "Số electron đi qua tiết diện là $N_e = \\dfrac{q}{e} = \\dfrac{3{,}2}{1{,}6 \\cdot 10^{-19}} = 2 \\cdot 10^{19}$ hạt."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cường độ dòng điện và vận tốc trôi:", [
                "Dòng điện không đổi là dòng điện có chiều và cường độ không thay đổi theo thời gian.",
                "Đơn vị $1\\text{ Coulomb (C)}$ được định nghĩa là điện lượng chuyển qua tiết diện thẳng của dây dẫn trong $1\\text{ s}$ khi có dòng điện không đổi $1\\text{ A}$ chạy qua ($1\\text{ C} = 1\\text{ A}\\cdot\\text{s}$).",
                "Vận tốc trôi có hướng của các electron tự do trong dây đồng bằng đúng tốc độ ánh sáng $3 \\cdot 10^8\\text{ m/s}$.",
                "Một viên pin dự phòng có dung lượng $10\\text{ Ah}$ có thể cung cấp tổng điện lượng là $36\\,000\\text{ C}$.",
            ], [True, True, False, True], "Ý c) sai vì vận tốc trôi có hướng của các electron rất nhỏ (chỉ khoảng vài phần mười $\\text{mm/s}$), còn tốc độ truyền tương tác điện trường dọc theo dây dẫn mới xấp xỉ tốc độ ánh sáng."),
            short("vandung", "Một dòng điện không đổi có cường độ $I = 2{,}5\\text{ A}$ chạy qua dây dẫn trong thời gian $t = 12\\text{ s}$. Điện lượng $q$ dịch chuyển qua tiết diện thẳng của dây dẫn trong thời gian đó bằng bao nhiêu Coulomb ($\\text{C}$)?", ["30"], "Áp dụng công thức $q = I \\cdot t = 2{,}5 \\cdot 12 = 30\\text{ C}$.", unit="C"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 19: Điện trở. Định luật Ohm và sự phụ thuộc vào nhiệt độ",
        icon="🌡️",
        description="Định luật Ohm cho vật dẫn kim loại, đường đặc trưng Vôn–Ampe, sự phụ thuộc điện trở kim loại vào nhiệt độ R = R₀[1 + α(t - t₀)] và điện trở nhiệt (NTC, PTC).",
        requirements=[
            "Nêu được đường đặc trưng Vôn–Ampe của vật dẫn kim loại ở nhiệt độ không đổi là một đoạn thẳng đi qua gốc tọa độ (độ dốc tỉ lệ nghịch với $R$).",
            "Giải thích được nguyên nhân gây ra điện trở của kim loại (do sự va chạm của các electron tự do với các ion dương ở nút mạng tinh thể) và vận dụng công thức $R = R_0[1 + \\alpha(t - t_0)]$.",
            "Phân biệt được hai loại điện trở nhiệt (Thermistor): loại NTC (nhiệt độ tăng thì điện trở giảm) và loại PTC (nhiệt độ tăng thì điện trở tăng).",
        ],
        definition="Đối với vật dẫn kim loại ở nhiệt độ xác định, đường đặc trưng Vôn–Ampe là đường thẳng đi qua gốc tọa độ ($I = \\dfrac{U}{R}$). Khi nhiệt độ $t$ tăng, dao động nhiệt của các ion dương ở nút mạng tinh thể tăng lên làm điện trở của kim loại tăng theo quy luật: $R = R_0[1 + \\alpha(t - t_0)]$.",
        theory=(
            "### 1. Đường đặc trưng Vôn–Ampe và Nguyên nhân gây ra điện trở kim loại\n"
            "- **Đường đặc trưng Vôn–Ampe**: đồ thị biểu diễn sự phụ thuộc của cường độ dòng điện $I$ vào hiệu điện thế $U$. Ở nhiệt độ không đổi, đây là đường thẳng đi qua gốc tọa độ. Khi hiệu điện thế quá cao làm dây tóc bóng đèn nóng lên mạnh, điện trở $R$ tăng nên đường đặc trưng Vôn–Ampe của bóng đèn sợi đốt bị **cong xuống**.\n"
            "- **Nguyên nhân gây ra điện trở trong kim loại**: Do sự mất trật tự và dao động nhiệt của các ion dương ở nút mạng tinh thể cản trở chuyển động có hướng của các electron tự do.\n\n"
            "### 2. Sự phụ thuộc của điện trở vào nhiệt độ & Điện trở nhiệt\n"
            "- **Đối với kim loại**: khi nhiệt độ tăng thì điện trở suất và điện trở tăng gần như bậc nhất:\n"
            "  $$R = R_0 [1 + \\alpha (t - t_0)]; \\qquad \\rho = \\rho_0 [1 + \\alpha (t - t_0)]$$\n"
            "  trong đó $\\alpha > 0$ là hệ số nhiệt điện trở ($\\text{K}^{-1}$), $R_0$ là điện trở ở nhiệt độ mốc $t_0$.\n"
            "- **Điện trở nhiệt (Thermistor)** làm bằng chất bán dẫn có điện trở biến thiên rất nhạy theo nhiệt độ:\n"
            "  - **Điện trở nhiệt NTC** (Negative Temperature Coefficient – hệ số nhiệt âm): khi **nhiệt độ tăng thì điện trở giảm mạnh**.\n"
            "  - **Điện trở nhiệt PTC** (Positive Temperature Coefficient – hệ số nhiệt dương): khi **nhiệt độ tăng quá ngưỡng thì điện trở tăng đột ngột**."
        ),
        formulas=[
            G(
                "Sự phụ thuộc của điện trở kim loại vào nhiệt độ",
                F("Công thức điện trở và điện trở suất kim loại theo nhiệt độ", "$R = R_0 [1 + \\alpha(t - t_0)]; \\qquad \\rho = \\rho_0 [1 + \\alpha(t - t_0)]$", "Trong đó $R_0$ là điện trở ở nhiệt độ $t_0$, $\\alpha > 0$ là hệ số nhiệt điện trở ($\\text{K}^{-1}$ hoặc $\\text{độ}^{-1}$)."),
                F("Đặc tính của hai loại điện trở nhiệt (Thermistor)", "$\\text{NTC: } t \\uparrow \\implies R \\downarrow; \\qquad \\text{PTC: } t \\uparrow \\implies R \\uparrow$", "Dùng làm cảm biến đo nhiệt độ và rơ-le bảo vệ quá nhiệt trong mạch điện tử."),
            )
        ],
        example="Một dây tóc bóng đèn bằng vonfram ở nhiệt độ phòng $t_0 = 20^\\circ\\text{C}$ có điện trở $R_0 = 25\\text{ }\\Omega$. Biết hệ số nhiệt điện trở của vonfram là $\\alpha = 4{,}5 \\cdot 10^{-3}\\text{ K}^{-1}$. Hãy tính điện trở $R$ của dây tóc bóng đèn khi nó sáng bình thường ở nhiệt độ $t = 2020^\\circ\\text{C}$.",
        example_answer="Độ tăng nhiệt độ là $t - t_0 = 2020 - 20 = 2000^\\circ\\text{C} = 2000\\text{ K}$. Điện trở của dây tóc khi đèn sáng là $R = R_0[1 + \\alpha(t - t_0)] = 25 \\cdot [1 + 4{,}5 \\cdot 10^{-3} \\cdot 2000] = 25 \\cdot (1 + 9) = 250\\text{ }\\Omega$ (tăng gấp $10$ lần so với lúc đèn tắt).",
        real_life="Cảm biến nhiệt độ trong điều hòa nhiệt độ, nồi cơm điện tử, nhiệt kế điện tử và hệ thống báo cháy tự động đều sử dụng linh kiện điện trở nhiệt (Thermistor NTC).",
        quiz=[
            mcq("biet", "Nguyên nhân chủ yếu gây ra điện trở của dây dẫn kim loại là gì?", ["Sự va chạm của các electron tự do với các ion dương dao động nhiệt ở nút mạng tinh thể kim loại", "Sự va chạm giữa các hạt proton với nhau", "Lực đẩy Archimedes của không khí xung quanh dây dẫn", "Sự nhiễm điện do cọ xát của lớp vỏ nhựa"], 0, "Các electron tự do khi dịch chuyển có hướng va chạm với các ion dương ở nút mạng tinh thể gây ra sự cản trở dòng điện (điện trở)."),
            mcq("biet", "Công thức biểu diễn sự phụ thuộc của điện trở dây dẫn kim loại $R$ vào nhiệt độ $t$ (với $R_0$ là điện trở ở nhiệt độ $t_0$, $\\alpha$ là hệ số nhiệt điện trở) là gì?", ["$R = R_0[1 + \\alpha(t - t_0)]$", "$R = \\dfrac{R_0}{1 + \\alpha(t - t_0)}$", "$R = R_0 + \\alpha(t - t_0)$", "$R = R_0 \\cdot \\alpha(t - t_0)$"], 0, "Điện trở kim loại tăng bậc nhất theo nhiệt độ: $R = R_0[1 + \\alpha(t - t_0)]$."),
            mcq("hieu", "Đối với một linh kiện **điện trở nhiệt loại NTC** (hệ số nhiệt điện trở âm), khi nhiệt độ của môi trường xung quanh nó tăng lên thì giá trị điện trở của nó thay đổi như thế nào?", ["Điện trở giảm mạnh khi nhiệt độ tăng", "Điện trở tăng mạnh khi nhiệt độ tăng", "Điện trở luôn giữ nguyên không đổi", "Điện trở giảm về giá trị âm"], 0, "Điện trở nhiệt NTC (Negative Temperature Coefficient) có điện trở giảm nhanh khi nhiệt độ tăng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về điện trở và nhiệt độ:", [
                "Khi nhiệt độ của dây dẫn kim loại tăng lên thì điện trở của nó tăng lên.",
                "Đường đặc trưng Vôn–Ampe của một điện trở kim loại được giữ ở nhiệt độ không đổi là một đường thẳng đi qua gốc tọa độ.",
                "Điện trở của dây tóc bóng đèn sợi đốt khi đang phát sáng ở $2000^\\circ\\text{C}$ nhỏ hơn rất nhiều so với khi đèn đang tắt ở $25^\\circ\\text{C}$.",
                "Khi làm lạnh một số kim loại và hợp kim xuống dưới nhiệt độ tới hạn $T_c$ rất thấp thì điện trở của chúng đột ngột giảm về bằng $0$ (hiện tượng siêu dẫn).",
            ], [True, True, False, True], "Ý c) sai vì dây tóc vonfram là kim loại nên ở $2000^\\circ\\text{C}$ có điện trở lớn gấp khoảng $10$ đến $12$ lần so với ở nhiệt độ phòng $25^\\circ\\text{C}$."),
            short("vandung", "Một dây bạch kim ở nhiệt độ $t_0 = 20^\\circ\\text{C}$ có điện trở $R_0 = 20\\text{ }\\Omega$. Biết hệ số nhiệt điện trở của bạch kim là $\\alpha = 4 \\cdot 10^{-3}\\text{ K}^{-1}$. Khi đưa dây bạch kim vào lò nung ở nhiệt độ $t = 520^\\circ\\text{C}$ (tức $t - t_0 = 500\\text{ K}$) thì điện trở $R$ của dây bằng bao nhiêu Ôm ($\\Omega$)?", ["60"], "Áp dụng công thức $R = R_0[1 + \\alpha(t - t_0)] = 20 \\cdot [1 + 4 \\cdot 10^{-3} \\cdot 500] = 20 \\cdot (1 + 2) = 60\\text{ }\\Omega$.", unit="Ω"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 20: Nguồn điện và suất điện động",
        icon="🔋",
        description="Nguồn điện và lực lạ bên trong nguồn, định nghĩa suất điện động E = A/q (V), điện trở trong r và hiệu điện thế mạch ngoài U = E - I.r.",
        requirements=[
            "Giải thích được vai trò của lực lạ bên trong nguồn điện và định nghĩa suất điện động của nguồn điện $\\mathcal{E} = \\dfrac{A}{q}$ (đơn vị Vôn – $\\text{V}$).",
            "Nêu được mỗi nguồn điện được đặc trưng bởi hai đại lượng: suất điện động $\\mathcal{E}$ và điện trở trong $r$.",
            "Viết và vận dụng được công thức liên hệ giữa hiệu điện thế hai cực nguồn điện (hiệu điện thế mạch ngoài $U$), suất điện động $\\mathcal{E}$ và độ giảm thế trên điện trở trong $I \\cdot r$: $U = \\mathcal{E} - I \\cdot r$.",
        ],
        definition="Suất điện động ($\\mathcal{E}$) của nguồn điện là đại lượng đặc trưng cho khả năng thực hiện công của nguồn điện và được đo bằng thương số giữa công $A$ của lực lạ thực hiện khi dịch chuyển một điện tích dương $q$ ngược chiều điện trường bên trong nguồn điện và độ lớn của điện tích $q$ đó: $\\mathcal{E} = \\dfrac{A}{q}$ (đơn vị Vôn – $\\text{V}$).",
        theory=(
            "### 1. Nguồn điện và Suất điện động ($\\mathcal{E}$)\n"
            "- Ở mạch ngoài, lực điện làm các điện tích dương dịch chuyển từ cực dương về cực âm. Để duy trì hiệu điện thế giữa hai cực, bên trong nguồn điện phải có **lực lạ** (bản chất hóa học trong pin/ắc quy, bản chất từ trong máy phát) thắng lực điện để đưa các điện tích dương từ cực âm về cực dương.\n"
            "- **Suất điện động của nguồn điện**:\n"
            "  $$\\mathcal{E} = \\dfrac{A}{q} \\implies A_{\\text{ng}} = q \\cdot \\mathcal{E} = \\mathcal{E} \\cdot I \\cdot t$$\n"
            "- Đơn vị của suất điện động là **Vôn** ($\\text{V}$). Số vôn ghi trên vỏ viên pin chưa mắc vào mạch chính là suất điện động $\\mathcal{E}$ của pin.\n\n"
            "### 2. Điện trở trong $r$ và Hiệu điện thế giữa hai cực của nguồn điện\n"
            "- Bản thân các chất bên trong nguồn điện cũng cản trở dòng điện chạy qua nó, gọi là **điện trở trong $r$** (đơn vị $\\Omega$).\n"
            "- Khi nguồn phát dòng điện $I$ ra mạch ngoài, hiệu điện thế giữa hai cực của nguồn (hiệu điện thế mạch ngoài $U$) là:\n"
            "  $$U = \\mathcal{E} - I \\cdot r$$\n"
            "  - Khi mạch ngoài hở ($I = 0$) hoặc điện trở trong không đáng kể ($r \\approx 0$) thì $U = \\mathcal{E}$."
        ),
        formulas=[
            G(
                "Suất điện động và Hiệu điện thế hai cực nguồn điện",
                F("Định nghĩa suất điện động và Công của nguồn điện", "$\\mathcal{E} = \\dfrac{A}{q} \\iff A = q \\cdot \\mathcal{E} = \\mathcal{E} \\cdot I \\cdot t$", "Trong đó $A$ là công của lực lạ bên trong nguồn ($\\text{J}$), $q$ là điện lượng dịch chuyển qua nguồn ($\\text{C}$), $\\mathcal{E}$ tính bằng $\\text{V}$."),
                F("Hiệu điện thế giữa hai cực nguồn điện (mạch ngoài)", "$U = \\mathcal{E} - I \\cdot r \\implies r = \\dfrac{\\mathcal{E} - U}{I}$", "Trong đó $I \\cdot r$ là độ giảm thế bên trong nguồn điện. Khi mạch hở ($I = 0$) thì $U = \\mathcal{E}$."),
            )
        ],
        example="Một nguồn điện có suất điện động $\\mathcal{E} = 12\\text{ V}$ và điện trở trong $r = 0{,}5\\text{ }\\Omega$. Khi nối nguồn với một mạch ngoài thì dòng điện chạy qua nguồn có cường độ $I = 4\\text{ A}$. Hãy tính công của nguồn điện thực hiện khi dịch chuyển điện lượng $q = 5\\text{ C}$ qua nguồn và tính hiệu điện thế $U$ giữa hai cực của nguồn điện.",
        example_answer="Công của nguồn điện khi dịch chuyển $q = 5\\text{ C}$ là $A = q \\cdot \\mathcal{E} = 5 \\cdot 12 = 60\\text{ J}$. Hiệu điện thế giữa hai cực của nguồn điện khi có dòng $I = 4\\text{ A}$ là $U = \\mathcal{E} - I \\cdot r = 12 - 4 \\cdot 0{,}5 = 10\\text{ V}$.",
        real_life="Một viên pin cũ đã dùng lâu ngày khi đo bằng vôn kế lúc để hở mạch vẫn chỉ gần $1{,}5\\text{ V}$ (suất điện động $\\mathcal{E}$), nhưng khi lắp vào đồ chơi có dòng điện $I$ chạy qua thì hiệu điện thế tụt xuống rất thấp ($U = \\mathcal{E} - Ir \\approx 0$) vì điện trở trong $r$ của pin cũ đã tăng lên rất lớn.",
        quiz=[
            mcq("biet", "Đại lượng đặc trưng cho khả năng thực hiện công của nguồn điện, được xác định bằng thương số giữa công $A$ của lực lạ khi dịch chuyển điện tích dương $q$ bên trong nguồn và độ lớn $q$ đó gọi là gì?", ["Suất điện động $\\mathcal{E} = \\dfrac{A}{q}$", "Cường độ điện trường $E = \\dfrac{F}{q}$", "Điện dung $C = \\dfrac{Q}{U}$", "Điện trở trong $r$"], 0, "Suất điện động của nguồn điện được định nghĩa là $\\mathcal{E} = \\dfrac{A}{q}$."),
            mcq("biet", "Một nguồn điện có suất điện động $\\mathcal{E}$ và điện trở trong $r$ đang phát dòng điện có cường độ $I$ ra mạch ngoài. Hiệu điện thế $U$ giữa hai cực của nguồn điện được tính bằng công thức nào?", ["$U = \\mathcal{E} - I \\cdot r$", "$U = \\mathcal{E} + I \\cdot r$", "$U = I \\cdot r$", "$U = \\dfrac{\\mathcal{E}}{r}$"], 0, "Hiệu điện thế hai cực nguồn điện bằng suất điện động trừ đi độ giảm thế trên điện trở trong: $U = \\mathcal{E} - I \\cdot r$."),
            mcq("hieu", "Trong trường hợp nào thì hiệu điện thế $U$ giữa hai cực của một nguồn điện có giá trị bằng đúng suất điện động $\\mathcal{E}$ của nguồn đó?", ["Khi mạch ngoài bị hở ($I = 0$) hoặc khi điện trở trong của nguồn rất nhỏ không đáng kể ($r \\approx 0$)", "Khi nguồn điện bị nối tắt (đoản mạch)", "Khi dòng điện $I$ trong mạch rất lớn", "Khi điện trở mạch ngoài bằng $0$"], 0, "Từ $U = \\mathcal{E} - I \\cdot r$, ta có $U = \\mathcal{E}$ khi $I = 0$ (mạch hở) hoặc $r = 0$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nguồn điện và suất điện động:", [
                "Mỗi nguồn điện một chiều được đặc trưng bởi hai đại lượng là suất điện động $\\mathcal{E}$ và điện trở trong $r$.",
                "Đơn vị đo của suất điện động trong hệ SI là Vôn ($\\text{V}$).",
                "Bên trong nguồn điện, lực lạ dịch chuyển các điện tích dương cùng chiều với lực tĩnh điện từ cực dương sang cực âm.",
                "Khi cường độ dòng điện $I$ chạy qua nguồn tăng lên thì hiệu điện thế $U = \\mathcal{E} - Ir$ giữa hai cực của nguồn giảm đi.",
            ], [True, True, False, True], "Ý c) sai vì bên trong nguồn điện, lực lạ thực hiện công đẩy các điện tích dương đi **ngược chiều** điện trường (từ cực âm về cực dương)."),
            short("vandung", "Một nguồn điện có suất điện động $\\mathcal{E} = 9\\text{ V}$ và điện trở trong $r = 1\\text{ }\\Omega$. Khi dòng điện chạy qua nguồn có cường độ $I = 2\\text{ A}$ thì hiệu điện thế $U$ giữa hai cực của nguồn bằng bao nhiêu Vôn ($\\text{V}$)?", ["7"], "Áp dụng công thức $U = \\mathcal{E} - I \\cdot r = 9 - 2 \\cdot 1 = 7\\text{ V}$.", unit="V"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 21: Định luật Ohm cho toàn mạch và hiện tượng đoản mạch",
        icon="⚡",
        description="Phát biểu và công thức Định luật Ohm cho toàn mạch I = E/(R_N + r), hiện tượng đoản mạch I_max = E/r và cách phòng tránh.",
        requirements=[
            "Thiết lập, phát biểu và vận dụng được biểu thức Định luật Ohm cho toàn mạch: $I = \\dfrac{\\mathcal{E}}{R_N + r}$ (hay $\\mathcal{E} = I(R_N + r) = U_N + I r$).",
            "Giải thích được hiện tượng đoản mạch (ngắn mạch) khi nối trực tiếp hai cực của nguồn bằng dây dẫn có điện trở rất nhỏ ($R_N \\approx 0 \\implies I_{\\max} = \\dfrac{\\mathcal{E}}{r}$).",
            "Nêu được tác hại của hiện tượng đoản mạch đối với nguồn điện và mạng điện gia đình cùng vai trò bảo vệ của cầu chì, aptomat.",
        ],
        definition="Định luật Ohm đối với toàn mạch: Cường độ dòng điện chạy trong một mạch điện kín tỉ lệ thuận với suất điện động của nguồn điện và tỉ lệ nghịch với điện trở toàn phần của mạch đó: $I = \\dfrac{\\mathcal{E}}{R_N + r}$.",
        theory=(
            "### 1. Định luật Ohm đối với toàn mạch\n"
            "- Xét mạch điện kín gồm nguồn điện có suất điện động $\\mathcal{E}$, điện trở trong $r$ nối với mạch ngoài có điện trở tương đương $R_N$.\n"
            "- Theo định luật bảo toàn năng lượng: $A_{\\text{nguồn}} = Q_{\\text{toàn mạch}} \\iff \\mathcal{E} I t = I^2 R_N t + I^2 r t$, suy ra:\n"
            "  $$\\mathcal{E} = I(R_N + r) = U_N + I r \\iff I = \\dfrac{\\mathcal{E}}{R_N + r}$$\n"
            "  trong đó $(R_N + r)$ gọi là **điện trở toàn phần** của mạch kín, và $U_N = I \\cdot R_N = \\mathcal{E} - I \\cdot r$ là hiệu điện thế mạch ngoài.\n\n"
            "### 2. Hiện tượng đoản mạch (ngắn mạch)\n"
            "- **Hiện tượng đoản mạch**: xảy ra khi hai cực của nguồn điện được nối với nhau bằng dây dẫn có điện trở rất nhỏ ($R_N \\approx 0$, ví dụ chập hai dây điện trần vào nhau).\n"
            "- Khi đó cường độ dòng điện trong mạch tăng vọt lên giá trị cực đại:\n"
            "  $$I_{\\text{đoản mạch}} = I_{\\max} = \\dfrac{\\mathcal{E}}{r}$$\n"
            "- **Tác hại & Phòng tránh**: Với ắc quy chì hoặc mạng điện dân dụng có $r$ rất nhỏ, dòng đoản mạch cực lớn gây tỏa nhiệt dữ dội làm hỏng ắc quy, cháy vỏ dây điện và gây hỏa hoạn $\\implies$ bắt buộc phải lắp **cầu chì** hoặc **aptomat (CB)** để tự động cắt mạch khi đoản mạch."
        ),
        formulas=[
            G(
                "Định luật Ohm cho toàn mạch và Dòng điện đoản mạch",
                F("Biểu thức Định luật Ohm cho toàn mạch", "$I = \\dfrac{\\mathcal{E}}{R_N + r} \\iff \\mathcal{E} = I(R_N + r) = U_N + I \\cdot r; \\qquad U_N = I \\cdot R_N$", "Trong đó $\\mathcal{E}$ là suất điện động ($\\text{V}$), $r$ là điện trở trong ($\\Omega$), $R_N$ là điện trở tương đương mạch ngoài ($\\Omega$)."),
                F("Cường độ dòng điện khi đoản mạch (R_N ≈ 0)", "$I_{\\text{đm}} = I_{\\max} = \\dfrac{\\mathcal{E}}{r} \\quad (\\text{khi } R_N = 0,\\ U_N = 0)$", "Điện trở trong $r$ càng nhỏ thì dòng điện đoản mạch $I_{\\max}$ càng lớn và càng nguy hiểm."),
            )
        ],
        example="Cho mạch điện kín gồm một nguồn điện có suất điện động $\\mathcal{E} = 12\\text{ V}$, điện trở trong $r = 1\\text{ }\\Omega$ mắc với mạch ngoài là một điện trở $R_N = 5\\text{ }\\Omega$. Hãy tính cường độ dòng điện $I$ chạy trong mạch, hiệu điện thế mạch ngoài $U_N$ và cường độ dòng điện $I_{\\max}$ nếu nguồn điện bị đoản mạch.",
        example_answer="Theo định luật Ohm cho toàn mạch, cường độ dòng điện là $I = \\dfrac{\\mathcal{E}}{R_N + r} = \\dfrac{12}{5 + 1} = 2\\text{ A}$. Hiệu điện thế mạch ngoài là $U_N = I \\cdot R_N = 2 \\cdot 5 = 10\\text{ V}$. Nếu nguồn bị đoản mạch ($R_N = 0$), dòng điện đoản mạch là $I_{\\max} = \\dfrac{\\mathcal{E}}{r} = \\dfrac{12}{1} = 12\\text{ A}$.",
        real_life="Khi khởi động (đề nổ) ô tô, mô-tơ đề cần dòng điện hàng trăm Ampe nên ắc quy ô tô được chế tạo có điện trở trong $r$ cực nhỏ (cỡ $0{,}01\\text{ }\\Omega$); vì vậy tuyệt đối không được để cờ-lê kim loại chạm chập đồng thời vào hai cọc của ắc quy ô tô vì sẽ gây dòng đoản mạch trên $1000\\text{ A}$ làm nổ ắc quy.",
        quiz=[
            mcq("biet", "Biểu thức của Định luật Ohm đối với toàn mạch gồm nguồn điện $(\\mathcal{E}, r)$ và mạch ngoài có điện trở $R_N$ là gì?", ["$I = \\dfrac{\\mathcal{E}}{R_N + r}$", "$I = \\dfrac{\\mathcal{E}}{R_N - r}$", "$I = \\dfrac{\\mathcal{E}}{R_N}$", "$I = \\mathcal{E}(R_N + r)$"], 0, "Theo định luật Ohm cho toàn mạch: $I = \\dfrac{\\mathcal{E}}{R_N + r}$."),
            mcq("biet", "Hiện tượng **đoản mạch (ngắn mạch)** của một nguồn điện xảy ra khi nào và cường độ dòng điện khi đó bằng bao nhiêu?", ["Khi nối hai cực của nguồn bằng dây dẫn có điện trở rất nhỏ ($R_N \\approx 0$), dòng điện đạt cực đại $I_{\\max} = \\dfrac{\\mathcal{E}}{r}$", "Khi ngắt công tắc làm mạch ngoài bị hở ($R_N = \\infty$), dòng điện bằng $0$", "Khi mắc thêm một điện trở rất lớn vào mạch ngoài", "Khi mắc vôn kế song song với bóng đèn"], 0, "Đoản mạch xảy ra khi $R_N \\approx 0$, lúc đó $I = \\dfrac{\\mathcal{E}}{0 + r} = \\dfrac{\\mathcal{E}}{r}$ đạt giá trị lớn nhất."),
            mcq("hieu", "Một mạch điện kín gồm nguồn điện có $\\mathcal{E} = 6\\text{ V}, r = 0{,}5\\text{ }\\Omega$ và biến trở $R_N$ ở mạch ngoài. Khi điều chỉnh biến trở để $R_N$ tăng lên thì cường độ dòng điện $I$ trong mạch và hiệu điện thế mạch ngoài $U_N$ thay đổi như thế nào?", ["Cường độ dòng điện $I$ giảm đi và hiệu điện thế mạch ngoài $U_N$ tăng lên", "Cả $I$ và $U_N$ đều tăng lên", "Cả $I$ và $U_N$ đều giảm đi", "Cường độ dòng điện $I$ tăng lên và $U_N$ giảm đi"], 0, "Khi $R_N$ tăng thì $I = \\dfrac{\\mathcal{E}}{R_N + r}$ giảm; do đó độ giảm thế trong nguồn $I r$ giảm làm hiệu điện thế mạch ngoài $U_N = \\mathcal{E} - I r$ tăng lên."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Định luật Ohm cho toàn mạch và đoản mạch:", [
                "Tổng độ giảm điện thế ở mạch ngoài ($U_N = I R_N$) và mạch trong ($I r$) luôn bằng suất điện động $\\mathcal{E}$ của nguồn.",
                "Khi xảy ra đoản mạch ($R_N = 0$), hiệu điện thế giữa hai cực của nguồn điện giảm xuống gần bằng $0$.",
                "Pin con thỏ $1{,}5\\text{ V}$ có điện trở trong khá lớn ($r \\approx 1\\text{ }\\Omega$) nên dòng đoản mạch nhỏ hơn nhiều so với ắc quy chì có điện trở trong rất nhỏ ($r \\approx 0{,}01\\text{ }\\Omega$).",
                "Lắp cầu chì hoặc aptomat vào mạch điện có tác dụng làm tăng dòng điện đoản mạch.",
            ], [True, True, True, False], "Ý d) sai vì cầu chì và aptomat dùng để **tự động ngắt mạch** ngay khi dòng điện vượt quá giới hạn nhằm ngăn chặn tác hại của đoản mạch."),
            short("vandung", "Một nguồn điện có suất điện động $\\mathcal{E} = 15\\text{ V}$ và điện trở trong $r = 1\\text{ }\\Omega$ được nối với điện trở mạch ngoài $R_N = 4\\text{ }\\Omega$ thành mạch kín. Cường độ dòng điện $I$ chạy trong mạch bằng bao nhiêu Ampe ($\\text{A}$)?", ["3"], "Áp dụng định luật Ohm cho toàn mạch: $I = \\dfrac{\\mathcal{E}}{R_N + r} = \\dfrac{15}{4 + 1} = 3\\text{ A}$.", unit="A"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 22: Năng lượng và công suất điện",
        icon="💡",
        description="Năng lượng và công suất tiêu thụ của đoạn mạch W = UIt, P = UI, định luật Joule–Lenz Q = I²Rt, công và công suất của nguồn điện P_ng = E.I và hiệu suất nguồn H = U/E.",
        requirements=[
            "Phân biệt được công suất tiêu thụ điện của đoạn mạch ngoài $\\mathcal{P} = U \\cdot I$ và công suất toàn phần của nguồn điện $\\mathcal{P}_{\\text{ng}} = \\mathcal{E} \\cdot I$.",
            "Vận dụng được công thức định luật Joule–Lenz $Q = I^2 R t$, công của nguồn điện $A_{\\text{ng}} = \\mathcal{E} I t$ và hiệu suất của nguồn điện $H = \\dfrac{U_N}{\\mathcal{E}} = \\dfrac{R_N}{R_N + r}$.",
            "Giải được bài toán công suất tiêu thụ trên biến trở mạch ngoài đạt cực đại khi $R_N = r$ với $\\mathcal{P}_{\\max} = \\dfrac{\\mathcal{E}^2}{4r}$.",
        ],
        definition="Năng lượng điện tiêu thụ của một đoạn mạch bằng công của lực điện thực hiện khi di chuyển các điện tích qua đoạn mạch đó: $W = U I t$ (công suất $\\mathcal{P} = U I$). Đối với toàn mạch, công suất của nguồn điện là $\\mathcal{P}_{\\text{ng}} = \\mathcal{E} I$ và hiệu suất của nguồn điện là $H = \\dfrac{\\mathcal{P}_N}{\\mathcal{P}_{\\text{ng}}} = \\dfrac{U_N}{\\mathcal{E}} = \\dfrac{R_N}{R_N + r}$.",
        theory=(
            "### 1. Năng lượng và Công suất tiêu thụ của một đoạn mạch\n"
            "- **Năng lượng điện tiêu thụ**: $W = A = q U = U I t$ (đơn vị $\\text{J}$ hoặc $\\text{kWh}$).\n"
            "- **Công suất tiêu thụ điện**: $\\mathcal{P} = \\dfrac{W}{t} = U \\cdot I$ (đơn vị $\\text{W}$).\n"
            "- Nếu đoạn mạch chỉ chứa điện trở thuần $R$: $W = Q = U I t = I^2 R t = \\dfrac{U^2}{R}t$ và $\\mathcal{P} = I^2 R = \\dfrac{U^2}{R}$.\n\n"
            "### 2. Công, Công suất và Hiệu suất của nguồn điện\n"
            "- **Công của nguồn điện**: $A_{\\text{ng}} = q \\mathcal{E} = \\mathcal{E} I t$.\n"
            "- **Công suất của nguồn điện**: $\\mathcal{P}_{\\text{ng}} = \\dfrac{A_{\\text{ng}}}{t} = \\mathcal{E} \\cdot I = \\mathcal{P}_N + I^2 r$.\n"
            "- **Hiệu suất của nguồn điện**: tỉ số giữa công suất có ích cung cấp cho mạch ngoài ($\\mathcal{P}_N = U_N I$) và công suất toàn phần của nguồn ($\\mathcal{P}_{\\text{ng}} = \\mathcal{E} I$):\n"
            "  $$H = \\dfrac{\\mathcal{P}_N}{\\mathcal{P}_{\\text{ng}}} = \\dfrac{U_N}{\\mathcal{E}} = \\dfrac{R_N}{R_N + r} \\cdot 100\\%$$\n"
            "- **Định lí truyền công suất cực đại ra mạch ngoài**: Khi thay đổi $R_N$, công suất mạch ngoài $\\mathcal{P}_N = I^2 R_N = \\dfrac{\\mathcal{E}^2 R_N}{(R_N + r)^2}$ đạt cực đại khi **$R_N = r$**, và giá trị cực đại là $\\mathcal{P}_{N\\max} = \\dfrac{\\mathcal{E}^2}{4r}$ (khi đó hiệu suất nguồn là $H = 50\\%$).\""
        ),
        formulas=[
            G(
                "Công suất nguồn điện, Hiệu suất nguồn và Cực trị công suất",
                F("Công suất mạch ngoài và Công suất của nguồn điện", "$\\mathcal{P}_N = U_N I = I^2 R_N; \\qquad \\mathcal{P}_{\\text{ng}} = \\mathcal{E} \\cdot I = I^2(R_N + r)$", "Công của nguồn trong thời gian $t$: $A_{\\text{ng}} = \\mathcal{E} I t$; nhiệt lượng tỏa ra trên toàn mạch: $Q_{\\text{tp}} = I^2(R_N + r)t$."),
                F("Hiệu suất của nguồn điện và Công suất mạch ngoài cực đại", "$H = \\dfrac{U_N}{\\mathcal{E}} = \\dfrac{R_N}{R_N + r}; \\qquad \\mathcal{P}_{N\\max} = \\dfrac{\\mathcal{E}^2}{4r} \\ (\\text{khi } R_N = r)$", "Điện trở mạch ngoài $R_N$ càng lớn so với $r$ thì hiệu suất của nguồn điện càng cao."),
            )
        ],
        example="Một nguồn điện có suất điện động $\\mathcal{E} = 12\\text{ V}$, điện trở trong $r = 2\\text{ }\\Omega$ được nối với điện trở mạch ngoài $R_N = 6\\text{ }\\Omega$ thành mạch kín. Hãy tính cường độ dòng điện $I$, công suất của nguồn điện $\\mathcal{P}_{\\text{ng}}$, công suất tiêu thụ ở mạch ngoài $\\mathcal{P}_N$ và hiệu suất $H$ của nguồn điện.",
        example_answer="Cường độ dòng điện trong mạch là $I = \\dfrac{\\mathcal{E}}{R_N + r} = \\dfrac{12}{6 + 2} = 1{,}5\\text{ A}$. Công suất của nguồn điện là $\\mathcal{P}_{\\text{ng}} = \\mathcal{E} \\cdot I = 12 \\cdot 1{,}5 = 18\\text{ W}$. Công suất tiêu thụ ở mạch ngoài là $\\mathcal{P}_N = I^2 R_N = 1{,}5^2 \\cdot 6 = 13{,}5\\text{ W}$. Hiệu suất của nguồn điện là $H = \\dfrac{R_N}{R_N + r} \\cdot 100\\% = \\dfrac{6}{6 + 2} \\cdot 100\\% = 75\\%$.",
        real_life="Trong kĩ thuật âm thanh và truyền thông vô tuyến, để loa hoặc ăng-ten nhận được công suất tín hiệu lớn nhất từ bộ khuếch đại, người ta thiết kế điện trở tải bằng đúng điện trở trong của nguồn phát ($R_N = r$, gọi là phối hợp trở kháng).",
        quiz=[
            mcq("biet", "Công thức tính công suất điện toàn phần $\\mathcal{P}_{\\text{ng}}$ của một nguồn điện có suất điện động $\\mathcal{E}$ đang phát dòng điện có cường độ $I$ là gì?", ["$\\mathcal{P}_{\\text{ng}} = \\mathcal{E} \\cdot I$", "$\\mathcal{P}_{\\text{ng}} = \\dfrac{\\mathcal{E}}{I}$", "$\\mathcal{P}_{\\text{ng}} = \\mathcal{E}^2 I$", "$\\mathcal{P}_{\\text{ng}} = \\dfrac{I}{\\mathcal{E}}$"], 0, "Công của nguồn trong thời gian $t$ là $A_{\\text{ng}} = \\mathcal{E} I t$, nên công suất của nguồn điện là $\\mathcal{P}_{\\text{ng}} = \\dfrac{A_{\\text{ng}}}{t} = \\mathcal{E} \\cdot I$."),
            mcq("biet", "Hiệu suất $H$ của một nguồn điện có suất điện động $\\mathcal{E}$, điện trở trong $r$ khi cung cấp điện cho mạch ngoài có điện trở tương đương $R_N$ (hiệu điện thế mạch ngoài $U_N$) được tính theo công thức nào?", ["$H = \\dfrac{U_N}{\\mathcal{E}} = \\dfrac{R_N}{R_N + r}$", "$H = \\dfrac{\\mathcal{E}}{U_N} = \\dfrac{R_N + r}{R_N}$", "$H = \\dfrac{r}{R_N + r}$", "$H = \\dfrac{R_N}{r}$"], 0, "Hiệu suất nguồn điện là $H = \\dfrac{\\mathcal{P}_N}{\\mathcal{P}_{\\text{ng}}} = \\dfrac{U_N I}{\\mathcal{E} I} = \\dfrac{U_N}{\\mathcal{E}} = \\dfrac{R_N}{R_N + r}$."),
            mcq("hieu", "Cho một nguồn điện có suất điện động $\\mathcal{E}$ và điện trở trong $r = 4\\text{ }\\Omega$ nối với một biến trở $R$ ở mạch ngoài. Phải điều chỉnh biến trở $R$ có giá trị bằng bao nhiêu để công suất tiêu thụ trên biến trở đạt giá trị cực đại?", ["$R = r = 4\\text{ }\\Omega$", "$R = 8\\text{ }\\Omega$", "$R = 2\\text{ }\\Omega$", "$R = 0\\text{ }\\Omega$"], 0, "Theo định lí truyền công suất cực đại, công suất tiêu thụ ở mạch ngoài đạt cực đại ($\\mathcal{P}_{\\max} = \\dfrac{\\mathcal{E}^2}{4r}$) khi $R = r = 4\\text{ }\\Omega$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về năng lượng và công suất trong mạch điện kín:", [
                "Công suất tỏa nhiệt hao phí bên trong nguồn điện có điện trở trong $r$ là $\\mathcal{P}_{\\text{hp}} = I^2 r$.",
                "Công suất của nguồn điện bằng tổng công suất tiêu thụ ở mạch ngoài và công suất tỏa nhiệt bên trong nguồn: $\\mathcal{P}_{\\text{ng}} = \\mathcal{P}_N + I^2 r$.",
                "Khi mạch ngoài có $R_N = r$ thì hiệu suất của nguồn điện bằng $100\\%$.",
                "Nhiệt lượng tỏa ra trên điện trở thuần $R$ trong thời gian $t$ được tính bởi định luật Joule–Lenz: $Q = I^2 R t$.",
            ], [True, True, False, True], "Ý c) sai vì khi $R_N = r$ thì hiệu suất của nguồn điện là $H = \\dfrac{r}{r + r} = 50\\%$."),
            short("vandung", "Một nguồn điện có suất điện động $\\mathcal{E} = 10\\text{ V}$, điện trở trong $r = 1\\text{ }\\Omega$ nối với điện trở mạch ngoài $R_N = 9\\text{ }\\Omega$. Hiệu suất $H$ của nguồn điện bằng bao nhiêu phần trăm ($\\%$)?", ["90"], "Áp dụng công thức $H = \\dfrac{R_N}{R_N + r} \\cdot 100\\% = \\dfrac{9}{9 + 1} \\cdot 100\\% = 90\\%$.", unit="%"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 23: Thực hành đo suất điện động và điện trở trong của pin điện hóa",
        icon="🔬",
        description="Sơ đồ mạch điện thực hành đo (E, r) của pin bằng vôn kế, ampe kế và biến trở; cách vẽ và xử lí đồ thị U = E - I.r.",
        requirements=[
            "Vẽ và lắp được sơ đồ mạch điện thực hành đo suất điện động $\\mathcal{E}$ và điện trở trong $r$ của một viên pin điện hóa (gồm pin, khóa $K$, biến trở, điện trở bảo vệ $R_0$, ampe kế mắc nối tiếp và vôn kế mắc song song hai cực pin).",
            "Giải thích được cơ sở lí thuyết của phép đo dựa trên phương trình đường thẳng $U = \\mathcal{E} - r \\cdot I$.",
            "Xác định được suất điện động $\\mathcal{E}$ (giao điểm với trục tung $U$ khi $I = 0$) và điện trở trong $r = \\dfrac{U_1 - U_2}{I_2 - I_1}$ từ bảng số liệu hoặc đồ thị $U - I$.",
        ],
        definition="Trong bài thực hành đo suất điện động $\\mathcal{E}$ và điện trở trong $r$ của pin điện hóa, ta thay đổi giá trị biến trở để đo các cặp giá trị cường độ dòng điện $I$ và hiệu điện thế hai cực nguồn $U$. Đồ thị biểu diễn sự phụ thuộc của $U$ vào $I$ theo hệ thức $U = \\mathcal{E} - r \\cdot I$ là một đường thẳng dốc xuống cắt trục tung tại $U = \\mathcal{E}$ và có độ dốc bằng $-r$.",
        theory=(
            "### 1. Sơ đồ mạch điện và Cơ sở lí thuyết\n"
            "- **Sơ đồ mạch điện**: Pin $(\\mathcal{E}, r)$ mắc nối tiếp với khóa $K$, điện trở bảo vệ $R_0$, biến trở $R_b$ và ampe kế $\\text{A}$; còn vôn kế $\\text{V}$ mắc song song trực tiếp vào hai cực của pin (hoặc hai đầu đoạn mạch ngoài).\n"
            "- **Vai trò của điện trở bảo vệ $R_0$**: giới hạn dòng điện trong mạch không vượt quá mức an toàn ngay cả khi con chạy của biến trở dịch chuyển về vị trí $R_b = 0$ (tránh đoản mạch làm hỏng pin và ampe kế).\n\n"
            "### 2. Xử lí số liệu và Đồ thị $U - I$\n"
            "- Phương trình liên hệ: $U = \\mathcal{E} - r \\cdot I$.\n"
            "- Trên hệ trục tọa độ $(I, U)$ (trục hoành là $I$, trục tung là $U$), đường biểu diễn là một **đoạn thẳng dốc xuống**:\n"
            "  - Giao điểm của đường thẳng kéo dài với trục tung ($I = 0$) cho giá trị **suất điện động $\\mathcal{E}$**.\n"
            "  - Giao điểm của đường thẳng kéo dài với trục hoành ($U = 0$) cho giá trị dòng đoản mạch $I_{\\max} = \\dfrac{\\mathcal{E}}{r}$.\n"
            "  - Lấy hai điểm $(I_1, U_1)$ và $(I_2, U_2)$ trên đường thẳng, ta tính được **điện trở trong của pin**:\n"
            "    $$r = \\dfrac{U_1 - U_2}{I_2 - I_1} = \\dfrac{\\mathcal{E}}{I_{\\max}}$$"
        ),
        formulas=[
            G(
                "Công thức xử lí số liệu thực hành đo (E, r) của pin",
                F("Phương trình đường thẳng U theo I và cách tìm r từ 2 lần đo", "$U = \\mathcal{E} - r \\cdot I \\implies \\begin{cases} U_1 = \\mathcal{E} - I_1 r \\\\ U_2 = \\mathcal{E} - I_2 r \\end{cases} \\implies r = \\dfrac{U_1 - U_2}{I_2 - I_1}$", "Sau khi tìm được $r$, thay lại vào $\\mathcal{E} = U_1 + I_1 r$ để tìm suất điện động $\\mathcal{E}$."),
                F("Xác định (E, r) từ các giao điểm của đồ thị U - I với hai trục tọa độ", "$\\text{Tại } I = 0 \\implies U = \\mathcal{E}; \\qquad \\text{Tại } U = 0 \\implies I = I_{\\max} \\implies r = \\dfrac{\\mathcal{E}}{I_{\\max}}$", "Độ dốc của đường thẳng $U(I)$ bằng $-r$."),
            )
        ],
        example="Trong bài thực hành đo suất điện động và điện trở trong của một viên pin: khi điều chỉnh biến trở ở vị trí thứ nhất, ampe kế chỉ $I_1 = 0{,}2\\text{ A}$ và vôn kế chỉ $U_1 = 1{,}4\\text{ V}$; khi điều chỉnh biến trở sang vị trí thứ hai, ampe kế chỉ $I_2 = 0{,}4\\text{ A}$ và vôn kế chỉ $U_2 = 1{,}3\\text{ V}$. Hãy tính điện trở trong $r$ và suất điện động $\\mathcal{E}$ của viên pin.",
        example_answer="Từ hai cặp số liệu $(I_1, U_1)$ và $(I_2, U_2)$, điện trở trong của pin là $r = \\dfrac{U_1 - U_2}{I_2 - I_1} = \\dfrac{1{,}4 - 1{,}3}{0{,}4 - 0{,}2} = \\dfrac{0{,}1}{0{,}2} = 0{,}5\\text{ }\\Omega$. Thay vào phương trình thứ nhất, suất điện động của pin là $\\mathcal{E} = U_1 + I_1 \\cdot r = 1{,}4 + 0{,}2 \\cdot 0{,}5 = 1{,}5\\text{ V}$.",
        real_life="Các thiết bị kiểm tra ắc quy (Battery Tester) tại các trạm bảo dưỡng ô tô, xe máy đo điện áp ắc quy ở hai chế độ dòng tải khác nhau để tính chính xác điện trở trong $r$ và đánh giá độ chai của bình ắc quy.",
        quiz=[
            mcq("biet", "Trong bài thực hành đo suất điện động $\\mathcal{E}$ và điện trở trong $r$ của pin điện hóa, đồ thị biểu diễn hiệu điện thế $U$ giữa hai cực của pin theo cường độ dòng điện $I$ có dạng đường gì?", ["Một đường thẳng dốc xuống cắt trục tung tại $U = \\mathcal{E}$", "Một đường thẳng đi qua gốc tọa độ $O(0; 0)$", "Một đường parabol đi lên", "Một đường tròn"], 0, "Vì $U = \\mathcal{E} - r \\cdot I$ là hàm bậc nhất có hệ số góc âm ($-r$) nên đồ thị $U - I$ là một đường thẳng dốc xuống cắt trục tung tại $\\mathcal{E}$."),
            mcq("biet", "Trong sơ đồ mạch điện thực hành đo suất điện động và điện trở trong của pin, việc mắc nối tiếp thêm một điện trở bảo vệ $R_0$ (ví dụ $R_0 = 10\\text{ }\\Omega$) với biến trở nhằm mục đích chính là gì?", ["Giới hạn dòng điện cực đại trong mạch để tránh hiện tượng đoản mạch làm hỏng pin và ampe kế khi biến trở chỉnh về $0$", "Làm tăng suất điện động $\\mathcal{E}$ của viên pin", "Biến dòng điện một chiều thành dòng điện xoay chiều", "Làm cho vôn kế chỉ số $0$"], 0, "Điện trở bảo vệ $R_0$ giữ cho tổng điện trở mạch ngoài luôn $\\ge R_0$, ngăn ngừa đoản mạch khi dịch chuyển con chạy biến trở về sát mức $0$."),
            mcq("hieu", "Trên đồ thị thực nghiệm $U - I$ của một nguồn điện, đường thẳng kéo dài cắt trục tung (trục $U$, tại $I = 0$) ở điểm $4{,}5\\text{ V}$ và cắt trục hoành (trục $I$, tại $U = 0$) ở điểm $3{,}0\\text{ A}$. Suất điện động $\\mathcal{E}$ và điện trở trong $r$ của nguồn điện đó lần lượt là:", ["$\\mathcal{E} = 4{,}5\\text{ V}$ và $r = 1{,}5\\text{ }\\Omega$", "$\\mathcal{E} = 3{,}0\\text{ V}$ và $r = 4{,}5\\text{ }\\Omega$", "$\\mathcal{E} = 4{,}5\\text{ V}$ và $r = 3{,}0\\text{ }\\Omega$", "$\\mathcal{E} = 1{,}5\\text{ V}$ và $r = 4{,}5\\text{ }\\Omega$"], 0, "Giao điểm với trục tung ($I = 0$) là $\\mathcal{E} = 4{,}5\\text{ V}$; giao điểm với trục hoành ($U = 0$) là $I_{\\max} = 3{,}0\\text{ A}$, suy ra $r = \\dfrac{\\mathcal{E}}{I_{\\max}} = \\dfrac{4{,}5}{3{,}0} = 1{,}5\\text{ }\\Omega$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về thực hành đo suất điện động và điện trở trong của pin:", [
                "Trong mạch thực hành, ampe kế được mắc nối tiếp để đo dòng điện $I$, còn vôn kế được mắc song song với hai cực của pin để đo hiệu điện thế $U$.",
                "Khi lắp mạch điện thực hành, cần để công tắc $K$ ở trạng thái mở và điều chỉnh biến trở ở giá trị lớn nhất trước khi đóng khóa $K$.",
                "Sau mỗi lần đọc số chỉ $(I, U)$, nên ngắt khóa $K$ ngay để tránh viên pin phát điện lâu bị nóng lên làm thay đổi điện trở trong $r$.",
                "Khi giá trị của biến trở giảm đi thì số chỉ của ampe kế giảm và số chỉ của vôn kế tăng.",
            ], [True, True, True, False], "Ý d) sai vì khi giá trị biến trở giảm thì điện trở mạch ngoài giảm $\\implies$ cường độ dòng điện $I$ (số chỉ ampe kế) tăng và hiệu điện thế $U = \\mathcal{E} - Ir$ (số chỉ vôn kế) giảm."),
            short("vandung", "Khi thực hành đo $(\\mathcal{E}, r)$ của một nguồn điện: ở lần đo thứ nhất với $I_1 = 0{,}5\\text{ A}$ thì vôn kế chỉ $U_1 = 8\\text{ V}$; ở lần đo thứ hai với $I_2 = 1{,}5\\text{ A}$ thì vôn kế chỉ $U_2 = 6\\text{ V}$. Điện trở trong $r$ của nguồn điện bằng bao nhiêu Ôm ($\\Omega$)?", ["2"], "Áp dụng công thức $r = \\dfrac{U_1 - U_2}{I_2 - I_1} = \\dfrac{8 - 6}{1{,}5 - 0{,}5} = \\dfrac{2}{1} = 2\\text{ }\\Omega$.", unit="Ω"),
        ],
    ),
]
