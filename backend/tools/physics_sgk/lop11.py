# -*- coding: utf-8 -*-
r"""VẬT LÍ 11 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).

Bao phủ toàn bộ 4 chương (26 bài học, từ Bài 1 đến Bài 26) theo đúng mục lục SGK Vật lí 11
bộ Kết nối tri thức với cuộc sống và Yêu cầu cần đạt Chương trình GDPT 2018 môn Vật lí lớp 11
(Thông tư 32/2018/TT-BGDĐT). Chia thành 6 chủ đề tương thích với hệ thống game thực nghiệm.
Mỗi chủ đề có đủ: Yêu cầu cần đạt, định nghĩa, lý thuyết theo từng bài, công thức phân nhóm,
ví dụ minh họa, ứng dụng thực tiễn, cấu hình game và 10 câu hỏi phân hóa:
Biết (4 câu TN) | Hiểu (2 câu TN + 2 câu Đúng - Sai 4 ý a-d) | Vận dụng (1 câu TN + 1 câu trả lời ngắn).
"""

from ._helpers import F, G, mcq, short, tf4

GRADE = 11

LESSONS = [
    # =========================================================================
    # CHƯƠNG I. DAO ĐỘNG (BÀI 1 – BÀI 7)
    # =========================================================================
    {
        "topic": "dao-dong",
        "title": "Chương I. Dao động",
        "icon": "⏱️",
        "description": (
            "Chương I · SGK Vật lí 11 Kết nối tri thức với cuộc sống (tr. 5–30): Bài 1 – Bài 7. "
            "Dao động điều hoà; các đại lượng đặc trưng và độ lệch pha; vận tốc, gia tốc trong dao động điều hoà; "
            "động năng, thế năng và sự chuyển hoá năng lượng; dao động tắt dần, dao động cưỡng bức và hiện tượng cộng hưởng."
        ),
        "requirements": [
            r"Thực hiện thí nghiệm đơn giản tạo ra được dao động và mô tả được một số ví dụ đơn giản về dao động tự do.",
            r"Dùng đồ thị li độ – thời gian có dạng hình sin (tạo ra bằng thí nghiệm, hoặc hình vẽ cho trước), nêu được định nghĩa: biên độ $A$, chu kì $T$, tần số $f$, tần số góc $\omega$, độ lệch pha $\Delta\varphi$.",
            r"Vận dụng được các khái niệm: biên độ $A$, chu kì $T$, tần số $f$, tần số góc $\omega$, độ lệch pha $\Delta\varphi$ để mô tả dao động điều hoà.",
            r"Sử dụng đồ thị, phân tích và thực hiện phép tính cần thiết để xác định được: độ dịch chuyển (li độ $x$), vận tốc $v$ và gia tốc $a$ trong dao động điều hoà.",
            r"Vận dụng được các phương trình về li độ $x = A\cos(\omega t + \varphi)$, vận tốc $v = -\omega A\sin(\omega t + \varphi)$ và gia tốc $a = -\omega^2 A\cos(\omega t + \varphi)$ của dao động điều hoà.",
            r"Vận dụng được phương trình độc lập và hệ thức $a = -\omega^2 x$ của dao động điều hoà.",
            r"Sử dụng đồ thị, phân tích và thực hiện phép tính cần thiết để mô tả được sự chuyển hoá động năng $W_{\text{đ}}$ và thế năng $W_{\text{t}}$ trong dao động điều hoà.",
            r"Nêu được ví dụ thực tế về dao động tắt dần, dao động cưỡng bức và hiện tượng cộng hưởng; thảo luận, đánh giá được sự có lợi hay có hại của cộng hưởng trong một số trường hợp cụ thể.",
        ],
        "definition": (
            r"- **Dao động cơ**: Chuyển động qua lại của vật quanh một vị trí đặc biệt gọi là vị trí cân bằng. "
            r"Dao động tuần hoàn là dao động mà sau những khoảng thời gian bằng nhau gọi là chu kì $T$, vật trở lại vị trí cũ theo hướng cũ." "\n"
            r"- **Dao động điều hoà**: Dao động trong đó li độ của vật là một hàm cosin (hay sin) của thời gian: "
            r"$x = A\cos(\omega t + \varphi)$, với $A$, $\omega$, $\varphi$ là các hằng số." "\n"
            r"- **Cơ năng trong dao động điều hoà**: Khi bỏ qua ma sát, cơ năng $W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}m\omega^2 A^2$ được bảo toàn; "
            r"động năng và thế năng biến thiên tuần hoàn chuyển hoá qua lại với chu kì $T' = \dfrac{T}{2}$ và tần số $f' = 2f$."
        ),
        "theory": (
            r"### Bài 1. Dao động điều hoà" "\n"
            r"- **Dao động cơ và dao động tuần hoàn**: Vật chuyển động qua lại quanh vị trí cân bằng gọi là dao động cơ. Nếu sau những khoảng thời gian bằng nhau vật trở lại vị trí cũ theo hướng cũ thì gọi là dao động tuần hoàn." "\n"
            r"- **Đồ thị và phương trình dao động điều hoà**: Đồ thị li độ – thời gian $(x - t)$ của dao động điều hoà là một đường hình sin. Phương trình li độ có dạng:" "\n"
            r"  $$x = A\cos(\omega t + \varphi)$$" "\n"
            r"  Trong đó: $x$ là li độ (độ dịch chuyển từ vị trí cân bằng đến vị trí của vật tại thời điểm $t$, đơn vị $\text{m}$ hoặc $\text{cm}$); $A > 0$ là biên độ (li độ cực đại $x_{\max} = A$); $(\omega t + \varphi)$ là pha của dao động tại thời điểm $t$ ($\text{rad}$); $\varphi \in [-\pi; \pi]$ ($\text{rad}$) là pha ban đầu." "\n"
            r"- **Mối liên hệ với chuyển động tròn đều**: Hình chiếu của một chất điểm chuyển động tròn đều bán kính $A$, tốc độ góc $\omega$ lên một đường kính là một dao động điều hoà biên độ $A$, tần số góc $\omega$." "\n\n"
            r"### Bài 2. Mô tả dao động điều hoà" "\n"
            r"- **Chu kì $T$ và tần số $f$**: Chu kì $T$ ($\text{s}$) là khoảng thời gian để vật thực hiện được một dao động toàn phần: $T = \dfrac{\Delta t}{N}$. Tần số $f$ ($\text{Hz}$) là số dao động toàn phần thực hiện được trong $1\text{ s}$: $f = \dfrac{1}{T} = \dfrac{N}{\Delta t}$." "\n"
            r"- **Tần số góc $\omega$**: Liên hệ với chu kì và tần số qua hệ thức $\omega = \dfrac{2\pi}{T} = 2\pi f$ (đơn vị $\text{rad/s}$)." "\n"
            r"- **Pha ban đầu và độ lệch pha**: Pha ban đầu $\varphi$ cho biết trạng thái (vị trí và chiều chuyển động) của vật ở thời điểm $t = 0$. Với hai dao động điều hoà cùng chu kì (cùng tần số góc $\omega$), độ lệch pha giữa dao động $1$ và dao động $2$ bằng hiệu hai pha ban đầu: $\Delta\varphi = \varphi_1 - \varphi_2$. Nếu $\varphi_1 = \varphi_2$ thì hai dao động đồng pha; nếu $\varphi_1 = \varphi_2 \pm \pi$ thì hai dao động ngược pha; nếu $\varphi_1 = \varphi_2 \pm \dfrac{\pi}{2}$ thì hai dao động vuông pha." "\n\n"
            r"### Bài 3. Vận tốc, gia tốc trong dao động điều hoà" "\n"
            r"- **Vận tốc tức thời**: Là đạo hàm của li độ theo thời gian, biểu thị bằng độ dốc của đồ thị $(x - t)$:" "\n"
            r"  $$v = x' = -\omega A\sin(\omega t + \varphi) = \omega A\cos\left(\omega t + \varphi + \dfrac{\pi}{2}\right)$$" "\n"
            r"  Vận tốc biến thiên điều hoà cùng tần số nhưng sớm pha $\dfrac{\pi}{2}$ so với li độ. Tại vị trí cân bằng ($x = 0$), tốc độ đạt cực đại $|v|_{\max} = v_{\max} = \omega A$; tại vị trí biên ($x = \pm A$), vận tốc bằng $0$ ($v = 0$). Hệ thức độc lập: $v = \pm\omega\sqrt{A^2 - x^2}$ hay $\dfrac{x^2}{A^2} + \dfrac{v^2}{v_{\max}^2} = 1$." "\n"
            r"- **Gia tốc tức thời**: Là đạo hàm của vận tốc theo thời gian:" "\n"
            r"  $$a = v' = -\omega^2 A\cos(\omega t + \varphi) = -\omega^2 x = \omega^2 A\cos(\omega t + \varphi + \pi)$$" "\n"
            r"  Gia tốc biến thiên điều hoà ngược pha với li độ và sớm pha $\dfrac{\pi}{2}$ so với vận tốc; vectơ gia tốc $\vec{a}$ luôn hướng về vị trí cân bằng và có độ lớn tỉ lệ với độ lớn li độ. Tại vị trí cân bằng ($x = 0$), $a = 0$; tại vị trí biên ($x = \pm A$), độ lớn gia tốc đạt cực đại $|a|_{\max} = a_{\max} = \omega^2 A$." "\n\n"
            r"### Bài 4. Bài tập về dao động điều hoà" "\n"
            r"- **Xác định các đại lượng từ phương trình và đồ thị**: Chiều dài quỹ đạo dao động là $L = 2A$; quãng đường vật đi được trong một chu kì luôn bằng $S_{1T} = 4A$, trong nửa chu kì luôn bằng $S_{0,5T} = 2A$." "\n"
            r"- **Chu kì riêng của con lắc lò xo và con lắc đơn**: Con lắc lò xo gồm vật nặng khối lượng $m$ và lò xo độ cứng $k$ có $\omega = \sqrt{\dfrac{k}{m}}$, $T = 2\pi\sqrt{\dfrac{m}{k}}$. Con lắc đơn chiều dài $l$ tại nơi có gia tốc trọng trường $g$ (góc lệch nhỏ $\alpha_0 \le 10^\circ$) có $\omega = \sqrt{\dfrac{g}{l}}$, $T = 2\pi\sqrt{\dfrac{l}{g}}$." "\n\n"
            r"### Bài 5. Động năng. Thế năng. Sự chuyển hoá giữa động năng và thế năng trong dao động điều hoà" "\n"
            r"- **Động năng**: $W_{\text{đ}} = \dfrac{1}{2}mv^2 = \dfrac{1}{2}m\omega^2 A^2\sin^2(\omega t + \varphi) = \dfrac{1}{2}m\omega^2(A^2 - x^2)$." "\n"
            r"- **Thế năng (mốc thế năng tại vị trí cân bằng)**: $W_{\text{t}} = \dfrac{1}{2}m\omega^2 x^2 = \dfrac{1}{2}m\omega^2 A^2\cos^2(\omega t + \varphi)$ (với con lắc lò xo thì $k = m\omega^2$ nên $W_{\text{t}} = \dfrac{1}{2}kx^2$)." "\n"
            r"- **Sự chuyển hoá và bảo toàn cơ năng**: Khi không có lực cản, cơ năng $W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}m\omega^2 A^2 = \dfrac{1}{2}kA^2 = \text{hằng số}$. Khi vật đi từ vị trí cân bằng ra biên, động năng giảm dần từ $W$ về $0$, thế năng tăng dần từ $0$ đến $W$; khi đi từ biên về vị trí cân bằng thì ngược lại." "\n\n"
            r"### Bài 6. Dao động tắt dần. Dao động cưỡng bức. Hiện tượng cộng hưởng" "\n"
            r"- **Dao động tắt dần**: Là dao động có biên độ và cơ năng giảm dần theo thời gian do lực cản (ma sát) của môi trường. Lực cản càng lớn thì sự tắt dần càng nhanh (ứng dụng: bộ giảm xóc ô tô, xe máy; cơ cấu đóng cửa tự động)." "\n"
            r"- **Dao động cưỡng bức**: Là dao động của vật dưới tác dụng của một ngoại lực cưỡng bức tuần hoàn $F = F_0\cos(\omega_{\text{cb}}t + \varphi_0)$. Khi ổn định, dao động cưỡng bức là dao động điều hoà có tần số bằng tần số $f_{\text{cb}}$ của ngoại lực; biên độ phụ thuộc vào biên độ ngoại lực $F_0$, lực cản môi trường và độ chênh lệch $|f_{\text{cb}} - f_0|$." "\n"
            r"- **Hiện tượng cộng hưởng**: Là hiện tượng biên độ của dao động cưỡng bức tăng nhanh đến giá trị cực đại khi tần số $f_{\text{cb}}$ của lực cưỡng bức tiến tới bằng tần số riêng $f_0$ của hệ dao động ($f_{\text{cb}} = f_0$ hay $T_{\text{cb}} = T_0$). Cộng hưởng có lợi trong hộp đàn guitar, lò vi sóng, máy chụp cộng hưởng từ ($\text{MRI}$), nhưng có hại đối với cầu cống, toà nhà, bệ máy." "\n\n"
            r"### Bài 7. Bài tập về sự chuyển hoá năng lượng trong dao động điều hoà" "\n"
            r"- **Tỉ số động năng và thế năng**: Nếu tại vị trí có li độ $x$ mà $W_{\text{đ}} = nW_{\text{t}}$ thì $W = (n + 1)W_{\text{t}}$, suy ra $x = \pm\dfrac{A}{\sqrt{n + 1}}$ và $v = \pm\omega A\sqrt{\dfrac{n}{n + 1}}$." "\n"
            r"- **Độ giảm cơ năng trong dao động tắt dần**: Phần cơ năng tiêu hao biến thành nhiệt năng do công của lực ma sát."
        ),
        "formulas": [
            G(
                "I. Phương trình và các đại lượng đặc trưng của dao động điều hoà",
                F("Phương trình li độ", r"$x = A\cos(\omega t + \varphi)$", r"Chiều dài quỹ đạo $L = 2A$; quãng đường trong $1$ chu kì $S = 4A$"),
                F("Chu kì, tần số và tần số góc", r"$\omega = \dfrac{2\pi}{T} = 2\pi f, \quad T = \dfrac{1}{f} = \dfrac{\Delta t}{N}$", r"$\omega$ ($\text{rad/s}$), $T$ ($\text{s}$), $f$ ($\text{Hz}$)"),
                F("Độ lệch pha hai dao động cùng chu kì", r"$\Delta\varphi = \varphi_1 - \varphi_2 = \omega\Delta t = \dfrac{2\pi\Delta t}{T}$", r"Đồng pha: $\Delta\varphi = 2k\pi$; ngược pha: $\Delta\varphi = (2k + 1)\pi$"),
                F("Tần số góc con lắc lò xo và con lắc đơn", r"$\omega_{\text{lx}} = \sqrt{\dfrac{k}{m}}, \quad \omega_{\text{đơn}} = \sqrt{\dfrac{g}{l}}$", r"$k$ ($\text{N/m}$), $m$ ($\text{kg}$), $l$ ($\text{m}$), $g$ ($\text{m/s}^2$)"),
            ),
            G(
                "II. Vận tốc, gia tốc và hệ thức độc lập thời gian",
                F("Phương trình vận tốc", r"$v = -\omega A\sin(\omega t + \varphi) = \omega A\cos\left(\omega t + \varphi + \dfrac{\pi}{2}\right)$", r"Sớm pha $\dfrac{\pi}{2}$ so với li độ; $v_{\max} = \omega A$ tại $x = 0$"),
                F("Phương trình gia tốc", r"$a = -\omega^2 x = -\omega^2 A\cos(\omega t + \varphi)$", r"Ngược pha với li độ; $a_{\max} = \omega^2 A$ tại $x = \pm A$"),
                F("Hệ thức độc lập thời gian", r"$A^2 = x^2 + \dfrac{v^2}{\omega^2}, \quad \dfrac{x^2}{A^2} + \dfrac{v^2}{v_{\max}^2} = 1, \quad \dfrac{v^2}{v_{\max}^2} + \dfrac{a^2}{a_{\max}^2} = 1$", r"Áp dụng cho hai đại lượng vuông pha"),
            ),
            G(
                "III. Năng lượng dao động và điều kiện cộng hưởng",
                F("Thế năng và động năng", r"$W_{\text{t}} = \dfrac{1}{2}m\omega^2 x^2 = \dfrac{1}{2}kx^2, \quad W_{\text{đ}} = \dfrac{1}{2}mv^2 = \dfrac{1}{2}m\omega^2(A^2 - x^2)$", r"Biến thiên với tần số $f' = 2f$, chu kì $T' = \dfrac{T}{2}$"),
                F("Cơ năng bảo toàn", r"$W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}m\omega^2 A^2 = \dfrac{1}{2}kA^2 = \dfrac{1}{2}mv_{\max}^2$", r"Tỉ lệ thuận với bình phương biên độ $A^2$"),
                F(r"Vị trí khi $W_{\text{đ}} = nW_{\text{t}}$", r"$x = \pm\dfrac{A}{\sqrt{n + 1}}, \quad v = \pm\dfrac{v_{\max}}{\sqrt{1 + \dfrac{1}{n}}}$", r"Khi $W_{\text{đ}} = W_{\text{t}}$ ($n = 1$) thì $x = \pm\dfrac{A}{\sqrt{2}}$"),
                F("Điều kiện cộng hưởng cơ", r"$f_{\text{cb}} = f_0 \iff \omega_{\text{cb}} = \omega_0 \iff T_{\text{cb}} = T_0$", r"Biên độ dao động cưỡng bức đạt cực đại $A_{\max}$"),
            ),
        ],
        "example": (
            r"Một vật nhỏ có khối lượng $m = 200\text{ g}$ dao động điều hoà dọc theo trục $Ox$ với phương trình "
            r"$x = 10\cos\left(5\pi t - \dfrac{\pi}{3}\right)$ ($\text{cm}$), trong đó $t$ tính bằng giây ($\text{s}$). "
            r"Lấy $\pi^2 = 10$. Hãy xác định: (a) Biên độ, tần số góc, chu kì, tần số và pha ban đầu của dao động; "
            r"(b) Tốc độ cực đại, gia tốc cực đại và độ lớn vận tốc của vật khi đi qua vị trí có li độ $x = 6\text{ cm}$; "
            r"(c) Cơ năng của vật và động năng của vật tại vị trí có li độ $x = 6\text{ cm}$."
        ),
        "example_answer": (
            r"- **(a) Các đại lượng đặc trưng**: Từ phương trình $x = 10\cos\left(5\pi t - \dfrac{\pi}{3}\right)$ ($\text{cm}$), ta có biên độ $A = 10\text{ cm} = 0,1\text{ m}$; tần số góc $\omega = 5\pi\text{ rad/s}$; pha ban đầu $\varphi = -\dfrac{\pi}{3}\text{ rad}$. Chu kì dao động là $T = \dfrac{2\pi}{\omega} = \dfrac{2\pi}{5\pi} = 0,4\text{ s}$; tần số dao động là $f = \dfrac{1}{T} = \dfrac{1}{0,4} = 2,5\text{ Hz}$." "\n"
            r"- **(b) Vận tốc và gia tốc**: Tốc độ cực đại tại vị trí cân bằng là $v_{\max} = \omega A = 5\pi \cdot 10 = 50\pi\text{ cm/s} \approx 157,1\text{ cm/s}$. Độ lớn gia tốc cực đại tại vị trí biên là $a_{\max} = \omega^2 A = (5\pi)^2 \cdot 0,1 = 25\pi^2 \cdot 0,1 = 25 \cdot 10 \cdot 0,1 = 25\text{ m/s}^2$. Tại vị trí $x = 6\text{ cm}$, áp dụng hệ thức độc lập thời gian: $|v| = \omega\sqrt{A^2 - x^2} = 5\pi\sqrt{10^2 - 6^2} = 5\pi \cdot 8 = 40\pi\text{ cm/s} = 0,4\pi\text{ m/s}$." "\n"
            r"- **(c) Năng lượng dao động**: Đổi $m = 200\text{ g} = 0,2\text{ kg}$, $A = 0,1\text{ m}$, $x = 0,06\text{ m}$. Cơ năng của vật là $W = \dfrac{1}{2}m\omega^2 A^2 = \dfrac{1}{2} \cdot 0,2 \cdot (5\pi)^2 \cdot 0,1^2 = 0,1 \cdot 250 \cdot 0,01 = \mathbf{0,25\text{ J}}$. Thế năng tại $x = 0,06\text{ m}$ là $W_{\text{t}} = \dfrac{1}{2}m\omega^2 x^2 = 0,1 \cdot 250 \cdot 0,06^2 = 0,09\text{ J}$, suy ra động năng là $W_{\text{đ}} = W - W_{\text{t}} = 0,25 - 0,09 = \mathbf{0,16\text{ J}}$."
        ),
        "real_life": (
            r"- **Con lắc đồng hồ và pít-tông động cơ**: Quả lắc đồng hồ duy trì nhịp dao động điều hoà giúp đếm thời gian chính xác; chuyển động của pít-tông trong xi-lanh động cơ đốt trong gần đúng là một dao động điều hoà với biên độ bằng một nửa hành trình pít-tông ($A = \dfrac{L}{2}$)." "\n"
            r"- **Hệ thống giảm xóc và chống rung chấn**: Phuộc nhún ô tô, xe máy sử dụng dầu thuỷ lực để biến dao động của khung xe thành dao động tắt dần nhanh sau khi qua ổ gà; các toà nhà cao tầng như Taipei 101 lắp quả cầu giảm chấn khối lượng lớn để triệt tiêu cộng hưởng khi có động đất hoặc bão lớn."
        ),
        "game_title": "Phòng thí nghiệm ảo: Khảo sát Dao động điều hoà và Cộng hưởng cơ",
        "game_description": "Điều chỉnh biên độ, tần số góc, pha ban đầu và hệ số cản để quan sát trực quan đồ thị li độ, vận tốc, gia tốc, sự chuyển hoá năng lượng và hiện tượng cộng hưởng.",
        "game_type": "game_dao_dong",
        "quiz": [
            mcq(
                "biet",
                r"Một vật dao động điều hoà theo phương trình $x = A\cos(\omega t + \varphi)$ với $A > 0$, $\omega > 0$. Đại lượng $(\omega t + \varphi)$ được gọi là:",
                [
                    r"Pha của dao động tại thời điểm $t$",
                    r"Pha ban đầu của dao động",
                    r"Tần số góc của dao động",
                    r"Li độ của dao động tại thời điểm $t$",
                ],
                0,
                r"Trong phương trình $x = A\cos(\omega t + \varphi)$, đại lượng $(\omega t + \varphi)$ là **pha của dao động tại thời điểm $t$** (đơn vị $\text{rad}$), cho phép xác định trạng thái (li độ và chiều chuyển động) của vật ở thời điểm $t$.",
            ),
            mcq(
                "biet",
                r"Trong dao động điều hoà, mối liên hệ giữa tần số góc $\omega$, chu kì $T$ và tần số $f$ là:",
                [
                    r"$\omega = \dfrac{2\pi}{f} = 2\pi T$",
                    r"$\omega = \dfrac{2\pi}{T} = 2\pi f$",
                    r"$\omega = \dfrac{T}{2\pi} = \dfrac{1}{2\pi f}$",
                    r"$\omega = \pi T = \dfrac{\pi}{f}$",
                ],
                1,
                r"Tần số góc $\omega$ ($\text{rad/s}$) liên hệ với chu kì $T$ ($\text{s}$) và tần số $f$ ($\text{Hz}$) theo công thức **$\omega = \dfrac{2\pi}{T} = 2\pi f$**.",
            ),
            mcq(
                "biet",
                r"Khi một vật dao động điều hoà với biên độ $A$ và tần số góc $\omega$, gia tốc $a$ của vật liên hệ với li độ $x$ theo công thức nào sau đây?",
                [
                    r"$a = \omega^2 x$",
                    r"$a = -\omega x^2$",
                    r"$a = -\omega^2 x$",
                    r"$a = -\omega x$",
                ],
                2,
                r"Gia tốc tức thời trong dao động điều hoà là $a = -\omega^2 A\cos(\omega t + \varphi) = \mathbf{-\omega^2 x}$, luôn ngược dấu với li độ $x$ và hướng về vị trí cân bằng.",
            ),
            mcq(
                "biet",
                r"Hiện tượng biên độ của dao động cưỡng bức tăng nhanh đến giá trị cực đại khi tần số $f_{\text{cb}}$ của lực cưỡng bức tiến tới bằng tần số riêng $f_0$ của hệ dao động được gọi là:",
                [
                    r"Hiện tượng dao động tắt dần",
                    r"Hiện tượng giao thoa cơ học",
                    r"Hiện tượng cộng hưởng",
                    r"Hiện tượng dao động tự do",
                ],
                2,
                r"Khi tần số của ngoại lực cưỡng bức bằng tần số riêng của hệ ($f_{\text{cb}} = f_0$), biên độ dao động cưỡng bức đạt giá trị cực đại, gọi là **hiện tượng cộng hưởng**.",
            ),
            mcq(
                "hieu",
                r"Một pít-tông chuyển động thẳng qua lại trong xi-lanh trên một đoạn thẳng dài $L = 16\text{ cm}$ và được coi là dao động điều hoà với tần số $f = 5\text{ Hz}$. Tốc độ cực đại của một điểm trên mặt pít-tông là:",
                [
                    r"$80\pi\text{ cm/s}$",
                    r"$160\pi\text{ cm/s}$",
                    r"$40\pi\text{ cm/s}$",
                    r"$20\pi\text{ cm/s}$",
                ],
                0,
                r"Chiều dài quỹ đạo $L = 2A = 16\text{ cm} \Rightarrow$ biên độ $A = \dfrac{L}{2} = 8\text{ cm}$. Tần số góc $\omega = 2\pi f = 2\pi \cdot 5 = 10\pi\text{ rad/s}$. Tốc độ cực đại là $v_{\max} = \omega A = 10\pi \cdot 8 = \mathbf{80\pi\text{ cm/s}}$.",
            ),
            mcq(
                "hieu",
                r"Một vật nhỏ dao động điều hoà với biên độ $A = 8\text{ cm}$. Tại vị trí mà động năng của vật bằng $3$ lần thế năng ($W_{\text{đ}} = 3W_{\text{t}}$), vật cách vị trí cân bằng một đoạn bằng:",
                [
                    r"$2\text{ cm}$",
                    r"$4\text{ cm}$",
                    r"$4\sqrt{2}\text{ cm}$",
                    r"$4\sqrt{3}\text{ cm}$",
                ],
                1,
                r"Khi $W_{\text{đ}} = 3W_{\text{t}}$, cơ năng $W = W_{\text{đ}} + W_{\text{t}} = 4W_{\text{t}} \Rightarrow \dfrac{1}{2}m\omega^2 A^2 = 4 \cdot \dfrac{1}{2}m\omega^2 x^2 \Rightarrow |x| = \dfrac{A}{2} = \dfrac{8}{2} = \mathbf{4\text{ cm}}$.",
            ),
            tf4(
                "hieu",
                r"Một chất điểm có khối lượng $m = 100\text{ g}$ dao động điều hoà trên trục $Ox$ với phương trình $x = 5\cos\left(4\pi t + \dfrac{\pi}{2}\right)$ ($\text{cm}$), trong đó $t$ tính bằng giây ($\text{s}$). Lấy $\pi^2 = 10$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Biên độ dao động của chất điểm là $A = 5\text{ cm}$ và chu kì dao động là $T = 0,5\text{ s}$.",
                    r"b) Tại thời điểm ban đầu $t = 0$, chất điểm đang đi qua vị trí cân bằng $x = 0$ theo chiều âm của trục $Ox$.",
                    r"c) Tốc độ cực đại của chất điểm trong quá trình dao động là $v_{\max} = 20\text{ cm/s}$.",
                    r"d) Cơ năng dao động của chất điểm bằng $0,02\text{ J}$.",
                ],
                [True, True, False, True],
                r"a) Từ phương trình, biên độ $A = 5\text{ cm}$ và $\omega = 4\pi\text{ rad/s} \Rightarrow T = \dfrac{2\pi}{\omega} = \dfrac{2\pi}{4\pi} = 0,5\text{ s}$ → **Đúng**." "\n"
                r"b) Khi $t = 0$, pha ban đầu $\varphi = \dfrac{\pi}{2}\text{ rad}$ nên $x(0) = 5\cos\dfrac{\pi}{2} = 0$ và $v(0) = -\omega A\sin\dfrac{\pi}{2} = -\omega A < 0$ (chuyển động theo chiều âm) → **Đúng**." "\n"
                r"c) Tốc độ cực đại là $v_{\max} = \omega A = 4\pi \cdot 5 = 20\pi\text{ cm/s} \neq 20\text{ cm/s}$ → **Sai**." "\n"
                r"d) Đổi $m = 0,1\text{ kg}$, $A = 0,05\text{ m}$. Cơ năng $W = \dfrac{1}{2}m\omega^2 A^2 = \dfrac{1}{2} \cdot 0,1 \cdot (4\pi)^2 \cdot 0,05^2 = 0,05 \cdot 160 \cdot 0,0025 = 0,02\text{ J}$ → **Đúng**.",
            ),
            tf4(
                "hieu",
                r"Khi khảo sát sự chuyển hoá năng lượng và các loại dao động cơ trong thực tế, mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Khi vật dao động điều hoà đi từ vị trí biên về vị trí cân bằng thì thế năng giảm dần còn động năng tăng dần.",
                    r"b) Nếu vật dao động điều hoà với tần số $f = 4\text{ Hz}$ thì động năng và thế năng của vật biến thiên tuần hoàn với tần số $f' = 8\text{ Hz}$.",
                    r"c) Dao động cưỡng bức khi đã ổn định luôn có tần số bằng tần số riêng $f_0$ của hệ dao động.",
                    r"d) Bộ phận giảm xóc của xe máy, ô tô là ứng dụng có lợi của dao động tắt dần.",
                ],
                [True, True, False, True],
                r"a) Từ biên về vị trí cân bằng, $|x|$ giảm về $0$ nên thế năng $W_{\text{t}}$ giảm, tốc độ $|v|$ tăng đến $v_{\max}$ nên động năng $W_{\text{đ}}$ tăng → **Đúng**." "\n"
                r"b) Động năng và thế năng biến thiên tuần hoàn với tần số gấp đôi tần số của li độ: $f' = 2f = 2 \cdot 4 = 8\text{ Hz}$ → **Đúng**." "\n"
                r"c) Dao động cưỡng bức khi ổn định có tần số bằng tần số $f_{\text{cb}}$ của ngoại lực cưỡng bức, không phải luôn bằng tần số riêng $f_0$ → **Sai**." "\n"
                r"d) Bộ giảm xóc tận dụng lực cản lớn của dầu thuỷ lực để dập tắt nhanh dao động của khung xe sau khi qua chỗ xóc → **Đúng**.",
            ),
            mcq(
                "vandung",
                r"Một chất điểm dao động điều hoà trên trục $Ox$. Khi chất điểm có li độ $x_1 = 3\text{ cm}$ thì tốc độ của nó là $v_1 = 40\text{ cm/s}$; khi chất điểm có li độ $x_2 = 4\text{ cm}$ thì tốc độ của nó là $v_2 = 30\text{ cm/s}$. Biên độ $A$ và tần số góc $\omega$ của chất điểm lần lượt là:",
                [
                    r"$A = 5\text{ cm}, \ \omega = 10\text{ rad/s}$",
                    r"$A = 5\text{ cm}, \ \omega = 20\text{ rad/s}$",
                    r"$A = 7\text{ cm}, \ \omega = 10\text{ rad/s}$",
                    r"$A = 10\text{ cm}, \ \omega = 5\text{ rad/s}$",
                ],
                0,
                r"Áp dụng hệ thức độc lập thời gian $A^2 = x_1^2 + \dfrac{v_1^2}{\omega^2} = x_2^2 + \dfrac{v_2^2}{\omega^2}$, ta suy ra: "
                r"$\omega = \sqrt{\dfrac{v_1^2 - v_2^2}{x_2^2 - x_1^2}} = \sqrt{\dfrac{40^2 - 30^2}{4^2 - 3^2}} = \sqrt{\dfrac{700}{7}} = \mathbf{10\text{ rad/s}}$. "
                r"Thay $\omega = 10\text{ rad/s}$ vào biểu thức biên độ: $A = \sqrt{3^2 + \left(\dfrac{40}{10}\right)^2} = \sqrt{9 + 16} = \mathbf{5\text{ cm}}$.",
            ),
            short(
                "vandung",
                r"Một con lắc lò xo gồm vật nhỏ khối lượng $m = 250\text{ g}$ gắn vào lò xo nhẹ có độ cứng $k = 100\text{ N/m}$, dao động điều hoà trên mặt phẳng ngang không ma sát. Kéo vật lệch khỏi vị trí cân bằng một đoạn $x_0 = 3\text{ cm}$ rồi truyền cho vật vận tốc ban đầu $v_0 = 80\text{ cm/s}$ dọc theo trục lò xo. Cơ năng của con lắc bằng bao nhiêu $\text{mJ}$?",
                ["125"],
                r"Đổi $m = 0,25\text{ kg}$, $x_0 = 0,03\text{ m}$, $v_0 = 0,8\text{ m/s}$. Tần số góc $\omega = \sqrt{\dfrac{k}{m}} = \sqrt{\dfrac{100}{0,25}} = 20\text{ rad/s}$. "
                r"Biên độ dao động là $A = \sqrt{x_0^2 + \dfrac{v_0^2}{\omega^2}} = \sqrt{0,03^2 + \left(\dfrac{0,8}{20}\right)^2} = 0,05\text{ m}$. "
                r"Cơ năng của con lắc là $W = \dfrac{1}{2}kA^2 = \dfrac{1}{2} \cdot 100 \cdot 0,05^2 = 0,125\text{ J} = \mathbf{125\text{ mJ}}$.",
                unit=r"$\text{mJ}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG II – PHẦN 1. SÓNG CƠ HỌC VÀ SỰ TRUYỀN SÓNG (BÀI 8 – BÀI 10)
    # =========================================================================
    {
        "topic": "song-co",
        "title": "Chương II – Phần 1. Sóng cơ học và Sự truyền sóng",
        "icon": "🌊",
        "description": (
            "Chương II · SGK Vật lí 11 Kết nối tri thức với cuộc sống (tr. 31–43): Bài 8 – Bài 10. "
            "Mô tả sóng và các đại lượng đặc trưng của sóng; phân biệt sóng ngang, sóng dọc và sự truyền năng lượng của sóng cơ; "
            "thực hành đo tần số của sóng âm bằng dao động kí."
        ),
        "requirements": [
            r"Từ đồ thị độ dịch chuyển – khoảng cách (tạo ra bằng thí nghiệm, hoặc hình vẽ cho trước), mô tả được sóng qua các khái niệm: bước sóng $\lambda$, biên độ $A$, chu kì $T$, tần số $f$, tốc độ truyền sóng $v$ và cường độ sóng $I$.",
            r"Từ định nghĩa của vận tốc, tần số và bước sóng, rút ra được biểu thức $v = \lambda f = \dfrac{\lambda}{T}$ và vận dụng được biểu thức này.",
            r"Nêu được ví dụ chứng tỏ sóng truyền năng lượng.",
            r"Thực hiện thí nghiệm (hoặc sử dụng tài liệu đa phương tiện), thảo luận để nêu được mối liên hệ giữa các đại lượng đặc trưng của sóng với các đại lượng đặc trưng cho dao động của phần tử môi trường.",
            r"Quan sát hình ảnh (hoặc tài liệu đa phương tiện) về chuyển động của phần tử môi trường, thảo luận để so sánh được sóng dọc và sóng ngang; sử dụng mô hình sóng giải thích được một số tính chất đơn giản của âm thanh và ánh sáng.",
            r"Thảo luận để thiết kế phương án hoặc lựa chọn phương án và thực hiện phương án, đo được tần số của sóng âm bằng dao động kí hoặc dụng cụ thực hành.",
        ],
        "definition": (
            r"- **Sóng cơ**: Là những biến dạng cơ (dao động cơ) lan truyền trong một môi trường đàn hồi (rắn, lỏng, khí). "
            r"Quá trình truyền sóng là quá trình truyền pha dao động và truyền năng lượng, còn các phần tử vật chất của môi trường chỉ dao động quanh vị trí cân bằng cố định của chúng chứ không truyền đi theo sóng." "\n"
            r"- **Bước sóng $\lambda$**: Là quãng đường mà sóng truyền được trong một chu kì $T$ ($\lambda = vT = \dfrac{v}{f}$), cũng là khoảng cách ngắn nhất giữa hai điểm trên cùng một phương truyền sóng dao động cùng pha." "\n"
            r"- **Sóng ngang và sóng dọc**: Sóng ngang có phương dao động của các phần tử môi trường vuông góc với phương truyền sóng; sóng dọc có phương dao động của các phần tử môi trường trùng với phương truyền sóng."
        ),
        "theory": (
            r"### Bài 8. Mô tả sóng" "\n"
            r"- **Thí nghiệm tạo sóng mặt nước**: Khi nguồn $O$ dao động điều hoà theo phương thẳng đứng trên mặt nước, các gợn sóng tròn đồng tâm lan rộng ra xa, còn miếng nút bấc nổi trên mặt nước chỉ dao động lên xuống tại chỗ." "\n"
            r"- **Các đại lượng đặc trưng của sóng**:" "\n"
            r"  - **Biên độ sóng $A$**: Là độ dịch chuyển cực đại của phần tử môi trường khỏi vị trí cân bằng khi có sóng truyền qua." "\n"
            r"  - **Chu kì sóng $T$ ($\text{s}$) và tần số sóng $f$ ($\text{Hz}$)**: Bằng chu kì và tần số dao động của các phần tử môi trường (và bằng tần số của nguồn sóng): $f = \dfrac{1}{T}$." "\n"
            r"  - **Tốc độ truyền sóng $v$ ($\text{m/s}$)**: Là tốc độ lan truyền biến dạng (hoặc đỉnh sóng) trong môi trường, phụ thuộc vào bản chất và nhiệt độ của môi trường ($v_{\text{rắn}} > v_{\text{lỏng}} > v_{\text{khí}}$)." "\n"
            r"  - **Bước sóng $\lambda$ ($\text{m}$)**: Quãng đường sóng truyền đi trong một chu kì: $\lambda = vT = \dfrac{v}{f}$. Hai điểm gần nhau nhất trên một phương truyền sóng dao động cùng pha cách nhau $\lambda$; hai điểm gần nhau nhất dao động ngược pha cách nhau $\dfrac{\lambda}{2}$." "\n"
            r"  - **Phương trình sóng và độ lệch pha**: Nếu tại nguồn $O$ có $u_O = A\cos(\omega t)$ thì tại điểm $M$ cách $O$ một đoạn $x$ theo phương truyền sóng có $u_M = A\cos\left[\omega\left(t - \dfrac{x}{v}\right)\right] = A\cos\left(\omega t - \dfrac{2\pi x}{\lambda}\right)$. Độ lệch pha giữa hai điểm cách nhau một đoạn $d$ trên cùng phương truyền sóng là $\Delta\varphi = \dfrac{2\pi d}{\lambda}$." "\n\n"
            r"### Bài 9. Sóng ngang. Sóng dọc. Sự truyền năng lượng của sóng cơ" "\n"
            r"- **Sóng ngang**: Các phần tử của môi trường dao động theo phương vuông góc với phương truyền sóng. Sóng ngang cơ học truyền được trong chất rắn và trên bề mặt chất lỏng." "\n"
            r"- **Sóng dọc**: Các phần tử của môi trường dao động theo phương trùng với phương truyền sóng (tạo thành các vùng nén và vùng dãn kế tiếp nhau). Sóng dọc truyền được trong cả ba môi trường: rắn, lỏng và khí (ví dụ: sóng âm trong không khí, sóng trên lò xo nén dãn)." "\n"
            r"- **Sự truyền năng lượng của sóng cơ và cường độ sóng $I$**: Sóng truyền tới đâu thì làm phần tử môi trường ở đó dao động, tức là truyền năng lượng cho chúng. Cường độ sóng $I$ (đơn vị $\text{W/m}^2$) là năng lượng sóng được truyền qua một đơn vị diện tích vuông góc với phương truyền sóng trong một đơn vị thời gian: $I = \dfrac{E}{S\cdot\Delta t} = \dfrac{\mathcal{P}}{S}$. Với sóng cầu phát đẳng hướng từ nguồn công suất $\mathcal{P}$ ở khoảng cách $r$, diện tích mặt cầu là $S = 4\pi r^2$ nên $I = \dfrac{\mathcal{P}}{4\pi r^2}$." "\n"
            r"- **Sóng âm**: Các sóng cơ lan truyền trong môi trường gây ra cảm giác âm ở tai người có tần số từ $16\text{ Hz}$ đến $20\,000\text{ Hz}$ ($20\text{ kHz}$). Sóng hạ âm có $f < 16\text{ Hz}$; sóng siêu âm có $f > 20\,000\text{ Hz}$." "\n\n"
            r"### Bài 10. Thực hành: Đo tần số của sóng âm" "\n"
            r"- **Nguyên lí đo bằng dao động kí (hoặc cảm biến âm nối với máy tính)**: Micro biến đổi dao động âm thành tín hiệu điện biến thiên cùng chu kì và hiển thị đồ thị hình sin trên màn hình." "\n"
            r"- **Cách xác định chu kì $T$ và tần số $f$**: Đếm số ô ngang $n_{\text{ô}}$ ứng với một chu kì (hoặc $k$ chu kì) trên màn hình và nhân với hệ số thời gian trên mỗi ô $\Delta t_{\text{ô}}$ ($\text{s/div}$ hoặc $\text{ms/div}$): $T = n_{\text{ô}} \cdot \Delta t_{\text{ô}}$, từ đó suy ra tần số của sóng âm $f = \dfrac{1}{T}$."
        ),
        "formulas": [
            G(
                "I. Bước sóng, tốc độ truyền sóng và phương trình sóng",
                F("Liên hệ bước sóng, tốc độ và tần số", r"$\lambda = vT = \dfrac{v}{f} \iff v = \lambda f = \dfrac{\lambda}{T}$", r"$\lambda$ ($\text{m}$), $v$ ($\text{m/s}$), $T$ ($\text{s}$), $f$ ($\text{Hz}$)"),
                F("Khoảng cách giữa $n$ ngọn sóng liên tiếp", r"$L = (n - 1)\lambda$", r"Ví dụ: $5$ ngọn sóng liên tiếp cách nhau $4\lambda$"),
                F("Phương trình truyền sóng từ nguồn $O$", r"$u_M = A\cos\left(\omega t - \dfrac{2\pi x}{\lambda}\right)$", r"Điểm $M$ cách nguồn $O$ khoảng $x$ theo phương truyền sóng"),
                F("Độ lệch pha trên phương truyền sóng", r"$\Delta\varphi = \dfrac{2\pi d}{\lambda} = \dfrac{\omega d}{v}$", r"Cùng pha: $d = k\lambda$; ngược pha: $d = \left(k + \dfrac{1}{2}\right)\lambda$; vuông pha: $d = \left(k + \dfrac{1}{4}\right)\lambda$"),
            ),
            G(
                "II. Cường độ sóng và thực hành đo tần số sóng âm",
                F("Định nghĩa cường độ sóng", r"$I = \dfrac{E}{S\cdot\Delta t} = \dfrac{\mathcal{P}}{S}$", r"Đơn vị chuẩn $\text{SI}$ là $\text{W/m}^2$; $\mathcal{P}$ ($\text{W}$) là công suất truyền sóng"),
                F("Cường độ sóng cầu đẳng hướng", r"$I = \dfrac{\mathcal{P}}{4\pi r^2} \implies \dfrac{I_1}{I_2} = \dfrac{r_2^2}{r_1^2}$", r"Tỉ lệ nghịch với bình phương khoảng cách $r$ tới nguồn"),
                F("Đo tần số sóng âm trên dao động kí", r"$T = n_{\text{ô}} \cdot \Delta t_{\text{ô}}, \quad f = \dfrac{1}{T}$", r"$n_{\text{ô}}$ là số ô của $1$ chu kì, $\Delta t_{\text{ô}}$ là thời gian ứng với $1$ ô chia"),
            ),
        ],
        "example": (
            r"Một nguồn sóng cơ dao động điều hoà trên mặt nước với tần số $f = 20\text{ Hz}$. Người ta quan sát thấy khoảng cách giữa $6$ gợn lồi (đỉnh sóng) liên tiếp trên cùng một phương truyền sóng là $25\text{ cm}$. "
            r"Hãy tính: (a) Bước sóng $\lambda$ và tốc độ truyền sóng $v$ trên mặt nước; "
            r"(b) Độ lệch pha giữa hai điểm $M$, $N$ trên cùng một phương truyền sóng cách nhau một đoạn $d = 2,5\text{ cm}$."
        ),
        "example_answer": (
            r"- **(a) Bước sóng và tốc độ truyền sóng**: Khoảng cách giữa $n = 6$ đỉnh sóng liên tiếp bằng $(6 - 1)\lambda = 5\lambda$. Ta có $5\lambda = 25\text{ cm} \Rightarrow \lambda = \dfrac{25}{5} = \mathbf{5\text{ cm}} = 0,05\text{ m}$. Tốc độ truyền sóng trên mặt nước là $v = \lambda f = 5 \cdot 20 = \mathbf{100\text{ cm/s}} = \mathbf{1\text{ m/s}}$." "\n"
            r"- **(b) Độ lệch pha giữa hai điểm $M$, $N$**: Với khoảng cách $d = 2,5\text{ cm}$, độ lệch pha giữa $M$ và $N$ là $\Delta\varphi = \dfrac{2\pi d}{\lambda} = \dfrac{2\pi \cdot 2,5}{5} = \mathbf{\pi\text{ rad}}$, suy ra hai điểm $M$ và $N$ dao động ngược pha nhau."
        ),
        "real_life": (
            r"- **Sóng địa chấn và cảnh báo động đất**: Động đất phát ra đồng thời sóng dọc $P$ (tốc độ khoảng $5\text{ km/s}$ – $8\text{ km/s}$, truyền qua cả lớp nhân lỏng Trái Đất) và sóng ngang $S$ (tốc độ khoảng $3\text{ km/s}$ – $4,5\text{ km/s}$, chỉ truyền trong lớp đá rắn). Các trạm địa chấn đo độ chênh thời gian đến giữa sóng $P$ và sóng $S$ để xác định tâm chấn và phát cảnh báo sớm." "\n"
            r"- **Siêu âm y học và đo sâu hàng hải (Sonar)**: Sóng siêu âm ($f > 20\text{ kHz}$) có tính định hướng cao, được dùng trong chẩn đoán hình ảnh y khoa và thiết bị Sonar xác định độ sâu đáy biển hoặc đàn cá."
        ),
        "game_title": "Mô phỏng Sóng cơ học: Sóng ngang, Sóng dọc và Dao động kí âm thanh",
        "game_description": "Thay đổi tần số nguồn sóng và tốc độ môi trường để đo bước sóng, so sánh chuyển động hạt môi trường trong sóng ngang và sóng dọc, và đọc tần số âm trên màn hình dao động kí.",
        "game_type": "game_song_co",
        "quiz": [
            mcq(
                "biet",
                r"Bước sóng $\lambda$ của một sóng cơ học được định nghĩa là:",
                [
                    r"Quãng đường mà sóng truyền được trong một chu kì $T$",
                    r"Quãng đường mà sóng truyền được trong một giây",
                    r"Khoảng cách ngắn nhất giữa hai điểm dao động ngược pha trên cùng phương truyền sóng",
                    r"Biên độ dao động cực đại của các phần tử môi trường",
                ],
                0,
                r"**Bước sóng $\lambda$** là quãng đường mà sóng truyền được trong một chu kì $T$ ($\lambda = vT$), đồng thời là khoảng cách ngắn nhất giữa hai điểm trên cùng một phương truyền sóng dao động cùng pha.",
            ),
            mcq(
                "biet",
                r"Trong sự truyền sóng cơ học, sóng dọc là sóng mà các phần tử của môi trường dao động theo phương:",
                [
                    r"Vuông góc với phương truyền sóng",
                    r"Trùng với phương truyền sóng",
                    r"Luôn thẳng đứng từ trên xuống dưới",
                    r"Hợp với phương truyền sóng một góc $45^\circ$",
                ],
                1,
                r"**Sóng dọc** là sóng trong đó các phần tử của môi trường dao động theo phương **trùng với phương truyền sóng**.",
            ),
            mcq(
                "biet",
                r"Công thức liên hệ giữa tốc độ truyền sóng $v$, bước sóng $\lambda$, chu kì $T$ và tần số $f$ của sóng là:",
                [
                    r"$\lambda = \dfrac{v}{T} = vf$",
                    r"$\lambda = vT = \dfrac{v}{f}$",
                    r"$v = \lambda T = \dfrac{\lambda}{f}$",
                    r"$f = v\lambda = \dfrac{1}{T}$",
                ],
                1,
                r"Trong một chu kì $T$, sóng truyền đi được quãng đường bằng một bước sóng $\lambda$, do đó **$\lambda = vT = \dfrac{v}{f}$** (hay $v = \lambda f$).",
            ),
            mcq(
                "biet",
                r"Đơn vị đo cường độ sóng $I$ trong hệ đơn vị $\text{SI}$ là:",
                [
                    r"$\text{J/m}^2$",
                    r"$\text{W/m}^2$",
                    r"$\text{W/s}$",
                    r"$\text{N/m}^2$",
                ],
                1,
                r"Cường độ sóng $I = \dfrac{\mathcal{P}}{S}$ là năng lượng sóng truyền qua một đơn vị diện tích vuông góc với phương truyền sóng trong một đơn vị thời gian, có đơn vị chuẩn $\text{SI}$ là **$\text{W/m}^2$**.",
            ),
            mcq(
                "hieu",
                r"Một người quan sát một chiếc phao trên mặt biển thấy nó nhô cao $6$ lần trong khoảng thời gian $15\text{ s}$ và khoảng cách giữa hai đỉnh sóng liên tiếp là $6\text{ m}$. Tốc độ truyền sóng trên mặt biển là:",
                [
                    r"$2,0\text{ m/s}$",
                    r"$2,4\text{ m/s}$",
                    r"$1,5\text{ m/s}$",
                    r"$3,0\text{ m/s}$",
                ],
                0,
                r"Phao nhô cao $6$ lần liên tiếp ứng với $6 - 1 = 5$ chu kì sóng, nên $5T = 15\text{ s} \Rightarrow T = 3\text{ s}$. Khoảng cách giữa hai đỉnh sóng liên tiếp là $\lambda = 6\text{ m}$. Tốc độ truyền sóng là $v = \dfrac{\lambda}{T} = \dfrac{6}{3} = \mathbf{2,0\text{ m/s}}$.",
            ),
            mcq(
                "hieu",
                r"Trong bài thực hành đo tần số của sóng âm bằng dao động kí điện tử, bộ thang thời gian theo trục ngang được đặt ở mức $0,5\text{ ms/ô}$. Nếu một chu kì của tín hiệu âm thanh chiếm đúng $4\text{ ô}$ theo chiều ngang trên màn hình thì tần số của sóng âm đó là:",
                [
                    r"$250\text{ Hz}$",
                    r"$500\text{ Hz}$",
                    r"$1\,000\text{ Hz}$",
                    r"$2\,000\text{ Hz}$",
                ],
                1,
                r"Chu kì của sóng âm là $T = 4 \cdot 0,5\text{ ms} = 2\text{ ms} = 2 \cdot 10^{-3}\text{ s}$. Suy ra tần số của sóng âm là $f = \dfrac{1}{T} = \dfrac{1}{2 \cdot 10^{-3}} = \mathbf{500\text{ Hz}}$.",
            ),
            tf4(
                "hieu",
                r"Một sóng cơ hình sin truyền dọc theo trục $Ox$ với phương trình $u = 4\cos\left(20\pi t - \dfrac{\pi x}{5}\right)$ ($\text{cm}$), trong đó $x$ tính bằng $\text{cm}$, $t$ tính bằng giây ($\text{s}$). Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Biên độ của sóng là $A = 4\text{ cm}$ và tần số của sóng là $f = 10\text{ Hz}$.",
                    r"b) Bước sóng của sóng này bằng $\lambda = 10\text{ cm}$.",
                    r"c) Tốc độ truyền sóng trong môi trường là $v = 1\text{ m/s}$.",
                    r"d) Hai điểm trên trục $Ox$ cách nhau $5\text{ cm}$ luôn dao động cùng pha với nhau.",
                ],
                [True, True, True, False],
                r"a) Từ phương trình sóng, biên độ $A = 4\text{ cm}$ và $\omega = 20\pi\text{ rad/s} \Rightarrow f = \dfrac{\omega}{2\pi} = 10\text{ Hz}$ → **Đúng**." "\n"
                r"b) So sánh số hạng pha theo không gian: $\dfrac{2\pi x}{\lambda} = \dfrac{\pi x}{5} \Rightarrow \lambda = 10\text{ cm}$ → **Đúng**." "\n"
                r"c) Tốc độ truyền sóng là $v = \lambda f = 10 \cdot 10 = 100\text{ cm/s} = 1\text{ m/s}$ → **Đúng**." "\n"
                r"d) Hai điểm cách nhau $d = 5\text{ cm} = \dfrac{\lambda}{2}$ có độ lệch pha $\Delta\varphi = \dfrac{2\pi \cdot 5}{10} = \pi\text{ rad}$ nên dao động ngược pha nhau, không phải cùng pha → **Sai**.",
            ),
            tf4(
                "hieu",
                r"Khi so sánh đặc điểm của sóng ngang, sóng dọc và sóng âm trong các môi trường, mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Sóng âm khi truyền từ không khí vào nước thì tần số $f$ không đổi nhưng tốc độ truyền âm $v$ và bước sóng $\lambda$ đều tăng lên.",
                    r"b) Sóng cơ học có thể truyền được trong chân không giống như sóng ánh sáng.",
                    r"c) Sóng âm truyền trong chất khí và chất lỏng là sóng dọc.",
                    r"d) Khi sóng cơ truyền đi, các phần tử vật chất của môi trường cũng di chuyển đi xa theo sóng đến vị trí mới.",
                ],
                [True, False, True, False],
                r"a) Khi sóng truyền qua hai môi trường khác nhau, tần số $f$ giữ nguyên bằng tần số nguồn; vì $v_{\text{nước}} > v_{\text{khí}}$ nên bước sóng $\lambda = \dfrac{v}{f}$ tăng lên → **Đúng**." "\n"
                r"b) Sóng cơ học đòi hỏi môi trường vật chất đàn hồi nên không truyền được trong chân không → **Sai**." "\n"
                r"c) Trong chất khí và trong lòng chất lỏng, lực đàn hồi chỉ xuất hiện khi bị nén hoặc dãn thể tích nên sóng âm truyền trong đó là sóng dọc → **Đúng**." "\n"
                r"d) Các phần tử môi trường chỉ dao động quanh vị trí cân bằng cố định của mình, chỉ có pha dao động và năng lượng được truyền đi → **Sai**.",
            ),
            mcq(
                "vandung",
                r"Một nguồn âm điểm $O$ phát sóng âm đẳng hướng ra không gian không hấp thụ âm với công suất không đổi $\mathcal{P} = 12,56\text{ W}$. Lấy $\pi = 3,14$. Cường độ âm $I$ tại điểm $M$ cách nguồn một khoảng $r = 10\text{ m}$ là:",
                [
                    r"$0,01\text{ W/m}^2$",
                    r"$0,10\text{ W/m}^2$",
                    r"$0,02\text{ W/m}^2$",
                    r"$1,00\text{ W/m}^2$",
                ],
                0,
                r"Áp dụng công thức cường độ sóng cầu đẳng hướng: $I = \dfrac{\mathcal{P}}{4\pi r^2} = \dfrac{12,56}{4 \cdot 3,14 \cdot 10^2} = \dfrac{12,56}{1\,256} = \mathbf{0,01\text{ W/m}^2}$.",
            ),
            short(
                "vandung",
                r"Một sóng cơ có tần số $f = 50\text{ Hz}$ truyền theo phương $Ox$ với tốc độ $v = 120\text{ cm/s}$. Trên phương truyền sóng, hai điểm $M$ và $N$ cách nhau một đoạn $d = 3,6\text{ cm}$ dao động lệch pha nhau một góc $\Delta\varphi = k\pi$ ($\text{rad}$). Giá trị của $k$ bằng bao nhiêu (viết dưới dạng số thập phân gọn nhất, dùng dấu phẩy)?",
                ["1,5", "1.5"],
                r"Bước sóng của sóng là $\lambda = \dfrac{v}{f} = \dfrac{120}{50} = 2,4\text{ cm}$. "
                r"Độ lệch pha giữa hai điểm $M$ và $N$ là $\Delta\varphi = \dfrac{2\pi d}{\lambda} = \dfrac{2\pi \cdot 3,6}{2,4} = 1,5\pi\text{ rad}$. "
                r"Vậy $k = \mathbf{1,5}$.",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG II – PHẦN 2. SÓNG ĐIỆN TỪ, GIAO THOA SÓNG VÀ SÓNG DỪNG (BÀI 11 – BÀI 15)
    # =========================================================================
    {
        "topic": "song-dien-tu-giao-thoa-tu-dien",
        "title": "Chương II – Phần 2. Sóng điện từ, Giao thoa sóng và Sóng dừng",
        "icon": "📡",
        "description": (
            "Chương II · SGK Vật lí 11 Kết nối tri thức với cuộc sống (tr. 44–60): Bài 11 – Bài 15. "
            "Sóng điện từ và thang sóng điện từ; giao thoa sóng cơ và giao thoa ánh sáng qua hai khe Young; "
            "sóng dừng trên dây đàn hồi và trong cột khí; thực hành đo tốc độ truyền âm."
        ),
        "requirements": [
            r"Nêu được trong chân không, tất cả các sóng điện từ đều truyền với cùng tốc độ $c \approx 3 \cdot 10^8\text{ m/s}$; liệt kê được bậc độ lớn bước sóng của các bức xạ chủ yếu trong thang sóng điện từ.",
            r"Thực hiện (hoặc mô tả) được thí nghiệm chứng minh sự giao thoa hai sóng kết hợp bằng dụng cụ thực hành sử dụng sóng nước (hoặc sóng ánh sáng).",
            r"Phân tích, đánh giá kết quả thu được từ thí nghiệm, nêu được các điều kiện cần thiết để quan sát được hệ vân giao thoa; vận dụng được biểu thức khoảng vân $i = \dfrac{\lambda D}{a}$ cho giao thoa ánh sáng qua hai khe hẹp.",
            r"Thực hiện thí nghiệm tạo sóng dừng và giải thích được sự hình thành sóng dừng; sử dụng hình ảnh (tạo ra bằng thí nghiệm, hoặc hình vẽ cho trước), xác định được nút và bụng của sóng dừng.",
            r"Sử dụng các cách biểu diễn đại số và đồ thị để phân tích, xác định được vị trí nút và bụng của sóng dừng.",
            r"Thảo luận để thiết kế phương án hoặc lựa chọn phương án và thực hiện phương án, đo được tốc độ truyền âm bằng dụng cụ thực hành.",
        ],
        "definition": (
            r"- **Sóng điện từ**: Là điện từ trường biến thiên lan truyền trong không gian. Sóng điện từ là sóng ngang ($\vec{E} \perp \vec{B} \perp \vec{v}$), truyền được trong chân không với tốc độ ánh sáng $c = 3 \cdot 10^8\text{ m/s}$." "\n"
            r"- **Giao thoa sóng**: Là hiện tượng hai sóng kết hợp (cùng phương, cùng tần số và có độ lệch pha không đổi theo thời gian) khi gặp nhau thì có những điểm ở đó chúng luôn tăng cường lẫn nhau (cực đại giao thoa) và có những điểm ở đó chúng luôn triệt tiêu lẫn nhau (cực tiểu giao thoa)." "\n"
            r"- **Sóng dừng**: Là sóng truyền trên một sợi dây (hoặc cột khí) trong trường hợp xuất hiện các nút sóng (điểm luôn đứng yên) và các bụng sóng (điểm luôn dao động với biên độ cực đại) cố định trong không gian do sự giao thoa của sóng tới và sóng phản xạ."
        ),
        "theory": (
            r"### Bài 11. Sóng điện từ" "\n"
            r"- **Bản chất và đặc điểm**: Sóng điện từ là sóng ngang, trong đó vectơ cường độ điện trường $\vec{E}$ và vectơ cảm ứng từ $\vec{B}$ luôn vuông góc với nhau và vuông góc với phương truyền sóng. Khác với sóng cơ, sóng điện từ truyền được trong chân không với tốc độ lớn nhất $c \approx 3 \cdot 10^8\text{ m/s}$. Trong môi trường có chiết suất $n$, tốc độ truyền sóng điện từ là $v = \dfrac{c}{n}$ và bước sóng là $\lambda = \dfrac{\lambda_0}{n}$ (với $\lambda_0 = \dfrac{c}{f}$)." "\n"
            r"- **Thang sóng điện từ (theo thứ tự bước sóng $\lambda$ giảm dần, tần số $f$ tăng dần)**:" "\n"
            r"  1. **Sóng vô tuyến** ($\lambda$ từ $1\text{ mm}$ đến hàng chục $\text{km}$): Dùng trong thông tin liên lạc, phát thanh, truyền hình, radar." "\n"
            r"  2. **Tia hồng ngoại** ($0,76\,\mu\text{m} \le \lambda \le 1\text{ mm}$): Tác dụng nhiệt nổi bật; dùng trong điều khiển từ xa, camera hồng ngoại, sưởi ấm." "\n"
            r"  3. **Ánh sáng nhìn thấy (khả kiến)** ($0,38\,\mu\text{m} \le \lambda \le 0,76\,\mu\text{m}$ hay $380\text{ nm}$ – $760\text{ nm}$): Quang phổ liên tục từ đỏ ($\lambda \approx 0,76\,\mu\text{m}$) đến tím ($\lambda \approx 0,38\,\mu\text{m}$)." "\n"
            r"  4. **Tia tử ngoại (UV)** ($10\text{ nm} \le \lambda \le 380\text{ nm}$): Kích thích phát quang, diệt khuẩn, tổng hợp vitamin $\text{D}$." "\n"
            r"  5. **Tia X (tia Rơnghen)** ($10^{-11}\text{ m} = 0,01\text{ nm} \le \lambda \le 10\text{ nm}$): Đâm xuyên mạnh; dùng chụp X-quang y tế, kiểm tra hành lí sân bay, tìm khuyết tật vật đúc." "\n"
            r"  6. **Tia gamma ($\gamma$)** ($\lambda < 10^{-11}\text{ m}$): Sinh ra trong phân rã hạt nhân, khả năng đâm xuyên lớn nhất; dùng trong xạ trị ung thư và công nghiệp hạt nhân." "\n\n"
            r"### Bài 12. Giao thoa sóng" "\n"
            r"- **Giao thoa hai sóng mặt nước từ hai nguồn kết hợp đồng pha $S_1, S_2$**: Xét điểm $M$ cách hai nguồn những khoảng $d_1, d_2$." "\n"
            r"  - Điểm $M$ dao động với biên độ cực đại khi hiệu đường đi bằng một số nguyên lần bước sóng: $d_2 - d_1 = k\lambda$ ($k \in \mathbb{Z}$)." "\n"
            r"  - Điểm $M$ dao động với biên độ cực tiểu (triệt tiêu) khi hiệu đường đi bằng một số bán nguyên lần bước sóng: $d_2 - d_1 = \left(k + \dfrac{1}{2}\right)\lambda$ ($k \in \mathbb{Z}$)." "\n"
            r"- **Thí nghiệm Young về giao thoa ánh sáng đơn sắc**: Gọi $a$ là khoảng cách giữa hai khe hẹp $F_1, F_2$; $D$ là khoảng cách từ mặt phẳng chứa hai khe đến màn quan sát; $\lambda$ là bước sóng ánh sáng." "\n"
            r"  - **Khoảng vân $i$**: Là khoảng cách giữa hai vân sáng (hoặc hai vân tối) liên tiếp trên màn: $i = \dfrac{\lambda D}{a}$." "\n"
            r"  - **Vị trí vân sáng bậc $k$**: $x_{\text{s}} = ki = k\dfrac{\lambda D}{a}$ ($k = 0, \pm 1, \pm 2, \dots$; $k = 0$ là vân sáng trung tâm)." "\n"
            r"  - **Vị trí vân tối thứ $k$**: $x_{\text{t}} = \left(k + \dfrac{1}{2}\right)i = \left(k + 0,5\right)\dfrac{\lambda D}{a}$ ($k = 0, \pm 1, \pm 2, \dots$)." "\n\n"
            r"### Bài 13. Sóng dừng" "\n"
            r"- **Phản xạ sóng**: Khi phản xạ trên vật cản cố định, sóng phản xạ luôn ngược pha với sóng tới ở điểm phản xạ. Khi phản xạ trên vật cản tự do, sóng phản xạ luôn cùng pha với sóng tới ở điểm phản xạ." "\n"
            r"- **Đặc điểm của sóng dừng**: Khoảng cách giữa hai nút sóng liên tiếp hoặc hai bụng sóng liên tiếp bằng một nửa bước sóng ($\dfrac{\lambda}{2}$). Khoảng cách giữa một nút sóng và một bụng sóng liền kề bằng một phần tư bước sóng ($\dfrac{\lambda}{4}$)." "\n"
            r"- **Điều kiện có sóng dừng trên dây chiều dài $L$**:" "\n"
            r"  - **Hai đầu dây cố định** (hai đầu là hai nút): $L = k\dfrac{\lambda}{2} \implies f = k\dfrac{v}{2L}$ với $k \in \mathbb{N}^*$. Khi đó trên dây có $k$ bó sóng, $k$ bụng sóng và $(k + 1)$ nút sóng." "\n"
            r"  - **Một đầu cố định, một đầu tự do** (hoặc cột khí một đầu kín, một đầu hở): $L = (2k + 1)\dfrac{\lambda}{4} = \left(k + \dfrac{1}{2}\right)\dfrac{\lambda}{2} \implies f = (2k + 1)\dfrac{v}{4L}$ với $k \in \mathbb{N}$. Khi đó trên dây có $(k + 1)$ bụng sóng và $(k + 1)$ nút sóng." "\n\n"
            r"### Bài 14. Bài tập về sóng" "\n"
            r"- **Vận dụng tổng hợp**: Giải các bài toán liên hệ giữa tốc độ truyền sóng, tần số, bước sóng, số cực đại và cực tiểu giao thoa trên đoạn thẳng nối hai nguồn, tính bước sóng ánh sáng qua thí nghiệm Young và xác định tần số các hoạ âm trên dây đàn." "\n\n"
            r"### Bài 15. Thực hành: Đo tốc độ truyền âm" "\n"
            r"- **Nguyên lí cộng hưởng sóng dừng trong ống hình trụ**: Dùng âm thoa (hoặc loa phát tần số $f$ đã biết) đặt gần miệng ống trụ chứa cột không khí có chiều dài thay đổi được nhờ pít-tông (hoặc mực nước). Dịch chuyển pít-tông giữa hai vị trí liên tiếp nghe thấy âm to nhất (cộng hưởng âm tại miệng ống là bụng sóng): hiệu chiều dài cột khí giữa hai lần cộng hưởng liên tiếp đúng bằng nửa bước sóng: $\Delta l = l_{n+1} - l_n = \dfrac{\lambda}{2} \implies \lambda = 2\Delta l$, từ đó tính được tốc độ truyền âm $v = \lambda f = 2f\Delta l$."
        ),
        "formulas": [
            G(
                "I. Sóng điện từ",
                F("Bước sóng điện từ trong chân không", r"$\lambda_0 = cT = \dfrac{c}{f} \quad (c \approx 3 \cdot 10^8\text{ m/s})$", r"$c$ là tốc độ ánh sáng trong chân không"),
                F("Tốc độ và bước sóng trong môi trường chiết suất $n$", r"$v = \dfrac{c}{n}, \quad \lambda = \dfrac{\lambda_0}{n}$", r"Tần số $f$ không đổi khi truyền qua các môi trường"),
            ),
            G(
                "II. Giao thoa sóng cơ và giao thoa ánh sáng (khe Young)",
                F("Cực đại và cực tiểu giao thoa (2 nguồn cùng pha)", r"$d_2 - d_1 = k\lambda \ \text{(cực đại)}, \quad d_2 - d_1 = \left(k + \dfrac{1}{2}\right)\lambda \ \text{(cực tiểu)}$", r"$k \in \mathbb{Z}$; trên đoạn nối hai nguồn, hai cực đại liên tiếp cách nhau $\dfrac{\lambda}{2}$"),
                F("Khoảng vân giao thoa ánh sáng", r"$i = \dfrac{\lambda D}{a} \iff \lambda = \dfrac{ia}{D}$", r"Thường đổi: $\lambda$ ($\mu\text{m}$), $D$ ($\text{m}$), $a$ ($\text{mm}$) thì $i$ ($\text{mm}$)"),
                F("Vị trí vân sáng và vân tối trên màn", r"$x_{\text{s}} = ki = k\dfrac{\lambda D}{a}, \quad x_{\text{t}} = \left(k + 0,5\right)i$", r"$k \in \mathbb{Z}$"),
            ),
            G(
                "III. Sóng dừng và thực hành đo tốc độ truyền âm",
                F("Sóng dừng trên dây hai đầu cố định", r"$L = k\dfrac{\lambda}{2} = k\dfrac{v}{2f} \quad (k = 1, 2, 3, \dots)$", r"Số bụng $= k$, số nút $= k + 1$; tần số cơ bản $f_1 = \dfrac{v}{2L}$"),
                F("Sóng dừng một đầu cố định, một đầu tự do", r"$L = (2k + 1)\dfrac{\lambda}{4} = (2k + 1)\dfrac{v}{4f} \quad (k = 0, 1, 2, \dots)$", r"Số bụng $=$ số nút $= k + 1$; tần số cơ bản $f_1 = \dfrac{v}{4L}$"),
                F("Đo tốc độ truyền âm bằng cộng hưởng cột khí", r"$\Delta l = l_2 - l_1 = \dfrac{\lambda}{2} \implies v = \lambda f = 2f(l_2 - l_1)$", r"$l_1, l_2$ là hai chiều dài cột khí liên tiếp cho âm to nhất"),
            ),
        ],
        "example": (
            r"Trong thí nghiệm Young về giao thoa ánh sáng đơn sắc, hai khe hẹp cách nhau một khoảng $a = 1,2\text{ mm}$ và mặt phẳng chứa hai khe cách màn quan sát một khoảng $D = 1,8\text{ m}$. "
            r"Người ta đo được khoảng cách giữa $5$ vân sáng liên tiếp trên màn là $3,6\text{ mm}$. "
            r"Hãy xác định: (a) Khoảng vân $i$ và bước sóng $\lambda$ của ánh sáng đơn sắc dùng trong thí nghiệm; "
            r"(b) Vị trí của vân sáng bậc $3$ và vân tối thứ $4$ (kể từ vân sáng trung tâm)."
        ),
        "example_answer": (
            r"- **(a) Khoảng vân và bước sóng ánh sáng**: Khoảng cách giữa $5$ vân sáng liên tiếp trên màn là $(5 - 1)i = 4i = 3,6\text{ mm} \Rightarrow i = \dfrac{3,6}{4} = \mathbf{0,9\text{ mm}}$. Bước sóng của ánh sáng đơn sắc là $\lambda = \dfrac{ia}{D} = \dfrac{0,9 \cdot 10^{-3} \cdot 1,2 \cdot 10^{-3}}{1,8} = 0,6 \cdot 10^{-6}\text{ m} = \mathbf{0,6\,\mu\text{m}} = 600\text{ nm}$ (ánh sáng màu da cam)." "\n"
            r"- **(b) Vị trí vân sáng bậc $3$ và vân tối thứ $4$**: Vị trí vân sáng bậc $3$ là $x_{\text{s3}} = \pm 3i = \pm 3 \cdot 0,9 = \mathbf{\pm 2,7\text{ mm}}$. Vị trí vân tối thứ $4$ tính từ vân trung tâm ứng với $k = 3$ (hoặc $k = -4$): $x_{\text{t4}} = \pm 3,5i = \pm 3,5 \cdot 0,9 = \mathbf{\pm 3,15\text{ mm}}$."
        ),
        "real_life": (
            r"- **Viễn thông không dây và y học hiện đại**: Sóng vô tuyến và vi sóng truyền dữ liệu điện thoại di động, $\text{Wi-Fi}$, vệ tinh $\text{GPS}$; tia hồng ngoại dùng trong cảm biến cửa tự động và thiết bị nhìn đêm; tia X dùng chụp X-quang và cắt lớp vi tính ($\text{CT}$)." "\n"
            r"- **Chế tạo nhạc cụ dây và nhạc cụ hơi**: Đàn guitar, đàn bầu, sáo trúc hoạt động dựa trên nguyên lí sóng dừng: khi người nghệ sĩ bấm phím đàn là đang thay đổi chiều dài hiệu dụng $L$ của dây đàn để thay đổi tần số âm cơ bản $f_1 = \dfrac{v}{2L}$ phát ra."
        ),
        "game_title": "Phòng thí nghiệm Giao thoa Khe Young, Sóng dừng và Phổ Sóng điện từ",
        "game_description": "Thực hiện thí nghiệm giao thoa ánh sáng Young, kích thích sóng dừng trên dây đàn hồi để đếm số bụng sóng, nút sóng và khám phá ứng dụng của các bức xạ trong thang sóng điện từ.",
        "game_type": "game_song_dien_tu_giao_thoa_tu_dien",
        "quiz": [
            mcq(
                "biet",
                r"Trong chân không, tất cả các sóng điện từ đều lan truyền với cùng một tốc độ bằng:",
                [
                    r"$3 \cdot 10^8\text{ m/s}$",
                    r"$340\text{ m/s}$",
                    r"$3 \cdot 10^5\text{ m/s}$",
                    r"$1,5 \cdot 10^8\text{ m/s}$",
                ],
                0,
                r"Trong chân không, mọi bức xạ trong thang sóng điện từ đều truyền với cùng tốc độ bằng tốc độ ánh sáng **$c \approx 3 \cdot 10^8\text{ m/s}$**.",
            ),
            mcq(
                "biet",
                r"Trong thang sóng điện từ, bức xạ nào sau đây có bước sóng ngắn nhất?",
                [
                    r"Tia hồng ngoại",
                    r"Tia tử ngoại",
                    r"Tia X (tia Rơnghen)",
                    r"Tia gamma ($\gamma$)",
                ],
                3,
                r"Sắp xếp theo bước sóng giảm dần: sóng vô tuyến $\rightarrow$ tia hồng ngoại $\rightarrow$ ánh sáng nhìn thấy $\rightarrow$ tia tử ngoại $\rightarrow$ tia X $\rightarrow$ **tia gamma ($\gamma$)** (có $\lambda < 10^{-11}\text{ m}$, ngắn nhất).",
            ),
            mcq(
                "biet",
                r"Trong thí nghiệm Young về giao thoa ánh sáng đơn sắc, gọi $\lambda$ là bước sóng ánh sáng, $a$ là khoảng cách giữa hai khe hẹp và $D$ là khoảng cách từ mặt phẳng hai khe đến màn quan sát. Công thức tính khoảng vân $i$ là:",
                [
                    r"$i = \dfrac{\lambda a}{D}$",
                    r"$i = \dfrac{\lambda D}{a}$",
                    r"$i = \dfrac{aD}{\lambda}$",
                    r"$i = \dfrac{\lambda D}{2a}$",
                ],
                1,
                r"Khoảng vân giao thoa là khoảng cách giữa hai vân sáng (hoặc hai vân tối) liên tiếp trên màn: **$i = \dfrac{\lambda D}{a}$**.",
            ),
            mcq(
                "biet",
                r"Khi có sóng dừng trên một sợi dây đàn hồi với bước sóng $\lambda$, khoảng cách giữa hai nút sóng liên tiếp (hoặc hai bụng sóng liên tiếp) bằng:",
                [
                    r"$\lambda$",
                    r"$\dfrac{\lambda}{2}$",
                    r"$\dfrac{\lambda}{4}$",
                    r"$2\lambda$",
                ],
                1,
                r"Trên dây có sóng dừng, khoảng cách giữa hai nút sóng liên tiếp hoặc hai bụng sóng liên tiếp luôn bằng một nửa bước sóng (**$\dfrac{\lambda}{2}$**).",
            ),
            mcq(
                "hieu",
                r"Tại mặt chất lỏng có hai nguồn phát sóng kết hợp $S_1, S_2$ dao động cùng pha theo phương thẳng đứng với bước sóng $\lambda = 4\text{ cm}$. Xét điểm $M$ trên mặt chất lỏng cách $S_1$ một đoạn $d_1 = 14\text{ cm}$ và cách $S_2$ một đoạn $d_2 = 22\text{ cm}$. Tại điểm $M$ có:",
                [
                    r"Cực đại giao thoa bậc $2$",
                    r"Cực tiểu giao thoa thứ $2$",
                    r"Cực đại giao thoa bậc $4$",
                    r"Cực tiểu giao thoa thứ $3$",
                ],
                0,
                r"Hiệu đường đi của hai sóng tới điểm $M$ là $d_2 - d_1 = 22 - 14 = 8\text{ cm} = 2\lambda$ (ứng với $k = 2 \in \mathbb{Z}$). Vì hai nguồn cùng pha nên tại $M$ là **cực đại giao thoa bậc $2$**.",
            ),
            mcq(
                "hieu",
                r"Một sợi dây đàn hồi dài $L = 1,2\text{ m}$ có hai đầu cố định. Khi kích thích cho dây dao động với tần số $f = 50\text{ Hz}$ thì trên dây hình thành sóng dừng ổn định với $4$ bụng sóng. Tốc độ truyền sóng trên dây là:",
                [
                    r"$15\text{ m/s}$",
                    r"$30\text{ m/s}$",
                    r"$60\text{ m/s}$",
                    r"$40\text{ m/s}$",
                ],
                1,
                r"Dây hai đầu cố định có $k = 4$ bụng sóng nên $L = 4 \cdot \dfrac{\lambda}{2} = 2\lambda \Rightarrow \lambda = \dfrac{L}{2} = \dfrac{1,2}{2} = 0,6\text{ m}$. Tốc độ truyền sóng trên dây là $v = \lambda f = 0,6 \cdot 50 = \mathbf{30\text{ m/s}}$.",
            ),
            tf4(
                "hieu",
                r"Trong thí nghiệm Young về giao thoa ánh sáng đơn sắc có bước sóng $\lambda = 0,5\,\mu\text{m}$, khoảng cách giữa hai khe là $a = 1\text{ mm}$, khoảng cách từ mặt phẳng chứa hai khe đến màn quan sát là $D = 2\text{ m}$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Khoảng vân giao thoa đo được trên màn là $i = 1\text{ mm}$.",
                    r"b) Tại điểm $M$ trên màn cách vân sáng trung tâm một đoạn $x_M = 3\text{ mm}$ là vân sáng bậc $3$.",
                    r"c) Tại điểm $N$ trên màn cách vân sáng trung tâm một đoạn $x_N = 2,5\text{ mm}$ là một vân sáng.",
                    r"d) Nếu giữ nguyên các điều kiện khác và thay ánh sáng trên bằng ánh sáng đơn sắc có bước sóng $\lambda' = 0,6\,\mu\text{m}$ thì khoảng vân tăng lên thành $1,2\text{ mm}$.",
                ],
                [True, True, False, True],
                r"a) Khoảng vân $i = \dfrac{\lambda D}{a} = \dfrac{0,5 \cdot 10^{-6} \cdot 2}{1 \cdot 10^{-3}} = 10^{-3}\text{ m} = 1\text{ mm}$ → **Đúng**." "\n"
                r"b) Vì $\dfrac{x_M}{i} = \dfrac{3}{1} = 3 \in \mathbb{Z}$ nên tại $M$ là vân sáng bậc $3$ → **Đúng**." "\n"
                r"c) Vì $\dfrac{x_N}{i} = \dfrac{2,5}{1} = 2,5 = 2 + 0,5$ nên tại $N$ là vân tối thứ $3$ kể từ vân trung tâm, không phải vân sáng → **Sai**." "\n"
                r"d) Khi $\lambda' = 0,6\,\mu\text{m}$ thì $i' = \dfrac{\lambda' D}{a} = \dfrac{0,6 \cdot 2}{1} = 1,2\text{ mm}$ → **Đúng**.",
            ),
            tf4(
                "hieu",
                r"Xét một sợi dây đàn hồi dài $L = 90\text{ cm}$ có hai đầu cố định, đang có sóng dừng ổn định với $3$ bó sóng (tức $3$ bụng sóng). Biết tần số rung của dây là $f = 40\text{ Hz}$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Tổng số nút sóng trên toàn bộ sợi dây (kể cả hai đầu dây) là $4$ nút.",
                    r"b) Bước sóng của sóng truyền trên sợi dây là $\lambda = 30\text{ cm}$.",
                    r"c) Khoảng cách giữa một nút sóng và một bụng sóng liền kề trên dây là $15\text{ cm}$.",
                    r"d) Tốc độ truyền sóng trên sợi dây là $v = 24\text{ m/s}$.",
                ],
                [True, False, True, True],
                r"a) Dây hai đầu cố định có $k = 3$ bụng sóng thì số nút sóng là $k + 1 = 4$ nút → **Đúng**." "\n"
                r"b) Ta có $L = 3\dfrac{\lambda}{2} = 90\text{ cm} \Rightarrow \dfrac{\lambda}{2} = 30\text{ cm} \Rightarrow \lambda = 60\text{ cm} \neq 30\text{ cm}$ → **Sai**." "\n"
                r"c) Khoảng cách giữa một nút và một bụng liền kề là $\dfrac{\lambda}{4} = \dfrac{60}{4} = 15\text{ cm}$ → **Đúng**." "\n"
                r"d) Tốc độ truyền sóng trên dây là $v = \lambda f = 0,6\text{ m} \cdot 40\text{ Hz} = 24\text{ m/s}$ → **Đúng**.",
            ),
            mcq(
                "vandung",
                r"Trong bài thực hành đo tốc độ truyền âm trong không khí bằng phương pháp cộng hưởng sóng dừng trong ống trụ thẳng đứng, nguồn âm có tần số $f = 850\text{ Hz}$. Khi thay đổi chiều cao cột không khí trong ống, hai vị trí liên tiếp của mực nước cho âm nghe to nhất (cộng hưởng) cách nhau một đoạn $\Delta l = 20\text{ cm}$. Tốc độ truyền âm trong không khí đo được trong thí nghiệm này là:",
                [
                    r"$340\text{ m/s}$",
                    r"$320\text{ m/s}$",
                    r"$330\text{ m/s}$",
                    r"$170\text{ m/s}$",
                ],
                0,
                r"Khoảng cách giữa hai vị trí mực nước liên tiếp xảy ra cộng hưởng âm bằng một nửa bước sóng: $\Delta l = \dfrac{\lambda}{2} = 20\text{ cm} \Rightarrow \lambda = 40\text{ cm} = 0,4\text{ m}$. Tốc độ truyền âm là $v = \lambda f = 0,4 \cdot 850 = \mathbf{340\text{ m/s}}$.",
            ),
            short(
                "vandung",
                r"Trong thí nghiệm Young về giao thoa ánh sáng với ánh sáng đơn sắc có bước sóng $\lambda = 0,6\,\mu\text{m}$, khoảng cách giữa hai khe là $a = 1,5\text{ mm}$, khoảng cách từ mặt phẳng chứa hai khe đến màn quan sát là $D = 2,5\text{ m}$. Trên màn quan sát, xét đoạn thẳng $MN$ đối xứng qua vân sáng trung tâm có độ dài $L = 9\text{ mm}$. Trên đoạn $MN$ (tính cả hai đầu mút $M, N$) có tổng cộng bao nhiêu vân sáng?",
                ["9"],
                r"Khoảng vân giao thoa là $i = \dfrac{\lambda D}{a} = \dfrac{0,6 \cdot 2,5}{1,5} = 1,0\text{ mm}$. "
                r"Vì đoạn $MN$ dài $L = 9\text{ mm}$ đối xứng qua vân trung tâm $O$ nên toạ độ hai đầu mút là $x_M = -4,5\text{ mm}$ và $x_N = +4,5\text{ mm}$. "
                r"Các vân sáng trên đoạn $MN$ thoả mãn $-4,5 \le k \cdot 1,0 \le 4,5$ với $k \in \mathbb{Z}$, tức $k \in \{-4; -3; -2; -1; 0; 1; 2; 3; 4\}$. "
                r"Vậy có tất cả $\mathbf{9}$ vân sáng.",
                unit="vân sáng",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG III – PHẦN 1. LỰC TĨNH ĐIỆN VÀ CƯỜNG ĐỘ ĐIỆN TRƯỜNG (BÀI 16 – BÀI 18)
    # =========================================================================
    {
        "topic": "dien-truong",
        "title": "Chương III – Phần 1. Lực tĩnh điện và Cường độ điện trường",
        "icon": "⚡",
        "description": (
            "Chương III · SGK Vật lí 11 Kết nối tri thức với cuộc sống (tr. 61–75): Bài 16 – Bài 18. "
            "Lực tương tác tĩnh điện giữa hai điện tích điểm (định luật Coulomb); khái niệm điện trường, "
            "cường độ điện trường và đường sức điện; điện trường đều và chuyển động của hạt mang điện trong điện trường đều."
        ),
        "requirements": [
            r"Thực hiện thí nghiệm hoặc bằng ví dụ thực tế, mô tả được sự hút (hoặc đẩy) của một điện tích vào một điện tích khác.",
            r"Phát biểu được định luật Coulomb và nêu được đơn vị đo điện tích là coulomb ($\text{C}$).",
            r"Sử dụng biểu thức $F = \dfrac{|q_1 q_2|}{4\pi\varepsilon_0 r^2} = k\dfrac{|q_1 q_2|}{r^2}$, tính và mô tả được lực tương tác giữa hai điện tích điểm đặt trong chân không (hoặc trong không khí).",
            r"Nêu được khái niệm điện trường là trường lực được tạo ra bởi điện tích, là dạng vật chất tồn tại quanh điện tích và truyền tương tác giữa các điện tích.",
            r"Nêu được ý nghĩa của cường độ điện trường và định nghĩa được cường độ điện trường tại một điểm được đo bằng tỉ số giữa lực điện tác dụng lên một điện tích dương đặt tại điểm đó và độ lớn của điện tích đó ($E = \dfrac{F}{q}$).",
            r"Sử dụng biểu thức $E = \dfrac{|Q|}{4\pi\varepsilon_0 r^2} = k\dfrac{|Q|}{r^2}$, tính và mô tả được cường độ điện trường do một điện tích điểm $Q$ đặt trong chân không hoặc trong không khí gây ra tại một điểm cách nó một khoảng $r$.",
            r"Dùng dụng cụ tạo ra (hoặc vẽ) được điện phổ trong một số trường hợp đơn giản; vận dụng được biểu thức $E = \dfrac{U}{d}$ đối với điện trường đều giữa hai bản phẳng nhiễm điện trái dấu và mô tả được tác dụng của điện trường đều lên chuyển động của điện tích bay vào điện trường đều theo phương vuông góc với đường sức.",
        ],
        "definition": (
            r"- **Định luật Coulomb**: Lực hút hay đẩy giữa hai điện tích điểm đặt trong chân không có phương trùng với đường thẳng nối hai điện tích điểm đó, có độ lớn tỉ lệ thuận với tích độ lớn của hai điện tích và tỉ lệ nghịch với bình phương khoảng cách giữa chúng: $F = k\dfrac{|q_1 q_2|}{r^2} = \dfrac{|q_1 q_2|}{4\pi\varepsilon_0 r^2}$." "\n"
            r"- **Điện trường và cường độ điện trường**: Điện trường là dạng vật chất (trường lực) tồn tại xung quanh điện tích và truyền tương tác giữa các điện tích. Cường độ điện trường $\vec{E} = \dfrac{\vec{F}}{q}$ đặc trưng cho độ mạnh yếu của điện trường về phương diện tác dụng lực tại điểm đang xét." "\n"
            r"- **Điện trường đều**: Là điện trường mà vectơ cường độ điện trường $\vec{E}$ tại mọi điểm đều có cùng phương, chiều và độ lớn ($E = \dfrac{U}{d}$); các đường sức điện là những đường thẳng song song và cách đều nhau."
        ),
        "theory": (
            r"### Bài 16. Lực tương tác giữa hai điện tích" "\n"
            r"- **Hai loại điện tích và sự tương tác điện**: Có hai loại điện tích là điện tích dương ($q > 0$) và điện tích âm ($q < 0$). Hai điện tích cùng dấu thì đẩy nhau, hai điện tích trái dấu thì hút nhau. Điện tích nguyên tố có độ lớn $e = 1,6 \cdot 10^{-19}\text{ C}$. Đơn vị đo điện tích trong hệ $\text{SI}$ là coulomb ($\text{C}$); các ước số thường dùng: $1\text{ mC} = 10^{-3}\text{ C}$, $1\,\mu\text{C} = 10^{-6}\text{ C}$, $1\text{ nC} = 10^{-9}\text{ C}$, $1\text{ pC} = 10^{-12}\text{ C}$." "\n"
            r"- **Định luật Coulomb trong chân không**: Độ lớn lực tương tác giữa hai điện tích điểm $q_1, q_2$ cách nhau khoảng $r$ trong chân không là:" "\n"
            r"  $$F = \dfrac{|q_1 q_2|}{4\pi\varepsilon_0 r^2} = k\dfrac{|q_1 q_2|}{r^2}$$" "\n"
            r"  Trong đó hằng số điện của chân không $\varepsilon_0 \approx 8,85 \cdot 10^{-12}\text{ C}^2\text{/(N}\cdot\text{m}^2)$ và hệ số tỉ lệ $k = \dfrac{1}{4\pi\varepsilon_0} \approx 9 \cdot 10^9\text{ N}\cdot\text{m}^2\text{/C}^2$. Trong môi trường điện môi đồng chất có hằng số điện môi $\varepsilon \ge 1$ (không khí có $\varepsilon \approx 1$), lực tương tác giảm đi $\varepsilon$ lần: $F = k\dfrac{|q_1 q_2|}{\varepsilon r^2}$." "\n\n"
            r"### Bài 17. Khái niệm điện trường" "\n"
            r"- **Khái niệm điện trường**: Điện trường là trường lực được tạo ra bởi điện tích, là dạng vật chất tồn tại quanh điện tích và truyền tương tác giữa các điện tích." "\n"
            r"- **Cường độ điện trường**: Giả sử đặt điện tích thử dương $q > 0$ tại một điểm trong điện trường và nó chịu lực điện $\vec{F}$, thì cường độ điện trường tại điểm đó là $\vec{E} = \dfrac{\vec{F}}{q}$ (đơn vị là $\text{N/C}$ hoặc $\text{V/m}$). Khi đó lực điện tác dụng lên một điện tích $q$ bất kì đặt tại điểm có $\vec{E}$ là $\vec{F} = q\vec{E}$: nếu $q > 0$ thì $\vec{F} \uparrow\uparrow \vec{E}$; nếu $q < 0$ thì $\vec{F} \uparrow\downarrow \vec{E}$." "\n"
            r"- **Cường độ điện trường của một điện tích điểm $Q$**: Tại điểm $M$ cách $Q$ khoảng $r$ trong chân không, vectơ $\vec{E}$ có phương nằm trên đường thẳng nối $Q$ và $M$, hướng ra xa $Q$ nếu $Q > 0$, hướng lại gần $Q$ nếu $Q < 0$, và có độ lớn:" "\n"
            r"  $$E = \dfrac{|Q|}{4\pi\varepsilon_0 r^2} = k\dfrac{|Q|}{r^2}$$" "\n"
            r"- **Nguyên lí chồng chất điện trường và đường sức điện**: Nếu tại một điểm có nhiều điện trường $\vec{E}_1, \vec{E}_2, \dots$ đồng thời gây ra thì $\vec{E} = \vec{E}_1 + \vec{E}_2 + \dots$. Đường sức điện là đường mà tiếp tuyến tại mỗi điểm của nó là giá của vectơ $\vec{E}$ tại điểm đó; đường sức điện xuất phát từ điện tích dương (hoặc ở vô cực) và kết thúc ở điện tích âm (hoặc ở vô cực), các đường sức điện không bao giờ cắt nhau." "\n\n"
            r"### Bài 18. Điện trường đều" "\n"
            r"- **Điện trường đều giữa hai bản phẳng kim loại song song tích điện trái dấu**: Khi hai bản phẳng song song cách nhau một khoảng $d$ (nhỏ so với kích thước bản) được tích điện trái dấu có hiệu điện thế $U$, điện trường ở vùng không gian giữa hai bản là điện trường đều có các đường sức thẳng, song song, cách đều nhau, hướng từ bản dương sang bản âm, với độ lớn:" "\n"
            r"  $$E = \dfrac{U}{d}$$" "\n"
            r"- **Tác dụng của điện trường đều lên chuyển động của điện tích**: Khi hạt mang điện tích $q$, khối lượng $m$ bay vào điện trường đều $\vec{E}$ với vận tốc ban đầu $\vec{v}_0 \perp \vec{E}$ (bỏ qua trọng lực), hạt chịu lực điện không đổi $\vec{F} = q\vec{E}$ dọc theo phương đường sức, tạo ra gia tốc $a_y = \dfrac{|q|E}{m}$. Chuyển động của hạt tương tự chuyển động ném ngang với quỹ đạo là một nhánh parabol ($x = v_0 t$, $y = \dfrac{1}{2}a_y t^2 = \dfrac{|q|E}{2mv_0^2}x^2$)."
        ),
        "formulas": [
            G(
                "I. Định luật Coulomb và lực tương tác tĩnh điện",
                F("Định luật Coulomb trong chân không", r"$F = \dfrac{|q_1 q_2|}{4\pi\varepsilon_0 r^2} = k\dfrac{|q_1 q_2|}{r^2}$", r"$k = \dfrac{1}{4\pi\varepsilon_0} = 9 \cdot 10^9\text{ N}\cdot\text{m}^2\text{/C}^2$"),
                F("Định luật Coulomb trong điện môi đồng chất", r"$F = k\dfrac{|q_1 q_2|}{\varepsilon r^2}$", r"$\varepsilon \ge 1$ là hằng số điện môi của môi trường"),
                F("Điện tích của vật nhiễm điện", r"$|q| = N\cdot e \quad (e = 1,6 \cdot 10^{-19}\text{ C})$", r"$N$ là số electron thừa hoặc thiếu"),
            ),
            G(
                "II. Cường độ điện trường và nguyên lí chồng chất",
                F("Định nghĩa cường độ điện trường", r"$\vec{E} = \dfrac{\vec{F}}{q} \iff \vec{F} = q\vec{E}, \quad E = \dfrac{F}{|q|}$", r"Đơn vị: $\text{V/m}$ hoặc $\text{N/C}$; $q > 0 \Rightarrow \vec{F} \uparrow\uparrow \vec{E}$, $q < 0 \Rightarrow \vec{F} \uparrow\downarrow \vec{E}$"),
                F("Điện trường của điện tích điểm $Q$", r"$E = \dfrac{|Q|}{4\pi\varepsilon_0 r^2} = k\dfrac{|Q|}{\varepsilon r^2}$", r"$Q > 0$: $\vec{E}$ hướng ra xa $Q$; $Q < 0$: $\vec{E}$ hướng về phía $Q$"),
                F("Nguyên lí chồng chất điện trường", r"$\vec{E} = \vec{E}_1 + \vec{E}_2 \implies E = \sqrt{E_1^2 + E_2^2 + 2E_1 E_2\cos\alpha}$", r"Cùng chiều: $E = E_1 + E_2$; ngược chiều: $E = |E_1 - E_2|$; vuông góc: $E = \sqrt{E_1^2 + E_2^2}$"),
            ),
            G(
                "III. Điện trường đều và chuyển động của hạt mang điện",
                F("Cường độ điện trường đều giữa hai bản phẳng", r"$E = \dfrac{U}{d} \iff U = Ed$", r"$U$ ($\text{V}$) là hiệu điện thế giữa hai bản, $d$ ($\text{m}$) là khoảng cách giữa hai bản"),
                F(r"Gia tốc và độ lệch của hạt mang điện ($\vec{v}_0 \perp \vec{E}$)", r"$a = \dfrac{|q|E}{m} = \dfrac{|q|U}{md}, \quad y = \dfrac{1}{2}at^2 = \dfrac{|q|E}{2mv_0^2}x^2$", r"Quỹ đạo chuyển động là một nhánh parabol"),
            ),
        ],
        "example": (
            r"Hai điện tích điểm $q_1 = +4\,\mu\text{C}$ và $q_2 = -4\,\mu\text{C}$ đặt cố định tại hai điểm $A$, $B$ cách nhau một khoảng $AB = 20\text{ cm}$ trong chân không. "
            r"Lấy $k = 9 \cdot 10^9\text{ N}\cdot\text{m}^2\text{/C}^2$. Hãy xác định: (a) Phương, chiều và độ lớn của lực tương tác tĩnh điện giữa hai điện tích; "
            r"(b) Hướng và độ lớn của vectơ cường độ điện trường tổng hợp $\vec{E}_M$ tại trung điểm $M$ của đoạn thẳng $AB$."
        ),
        "example_answer": (
            r"- **(a) Lực tương tác tĩnh điện giữa $q_1$ và $q_2$**: Vì $q_1$ và $q_2$ trái dấu nên hai điện tích hút nhau dọc theo đường thẳng $AB$. Đổi $|q_1| = |q_2| = 4 \cdot 10^{-6}\text{ C}$, $r = AB = 0,2\text{ m}$. Độ lớn lực hút là:" "\n"
            r"  $$F = k\dfrac{|q_1 q_2|}{r^2} = 9 \cdot 10^9 \cdot \dfrac{4 \cdot 10^{-6} \cdot 4 \cdot 10^{-6}}{0,2^2} = \dfrac{0,144}{0,04} = \mathbf{3,6\text{ N}}$$" "\n"
            r"- **(b) Cường độ điện trường tổng hợp tại trung điểm $M$**: Điểm $M$ cách $A$ và $B$ một khoảng $r_1 = r_2 = \dfrac{AB}{2} = 10\text{ cm} = 0,1\text{ m}$. Do $q_1 > 0$ nên $\vec{E}_1$ hướng ra xa $A$ (tức hướng từ $A$ đến $B$); do $q_2 < 0$ nên $\vec{E}_2$ hướng về phía $B$ (cũng hướng từ $A$ đến $B$). Hai vectơ $\vec{E}_1$ và $\vec{E}_2$ cùng hướng từ $A$ sang $B$ với độ lớn:" "\n"
            r"  $$E_1 = E_2 = k\dfrac{|q_1|}{r_1^2} = 9 \cdot 10^9 \cdot \dfrac{4 \cdot 10^{-6}}{0,1^2} = 3,6 \cdot 10^6\text{ V/m}$$" "\n"
            r"  Vậy $\vec{E}_M = \vec{E}_1 + \vec{E}_2$ hướng từ $A$ đến $B$ và có độ lớn $E_M = E_1 + E_2 = \mathbf{7,2 \cdot 10^6\text{ V/m}}$."
        ),
        "real_life": (
            r"- **Công nghệ lọc bụi tĩnh điện và sơn tĩnh điện**: Trong ống khói nhà máy nhiệt điện hoặc nhà máy xi măng, điện trường mạnh làm các hạt bụi khói nhiễm điện âm rồi hút chúng về phía bản cực dương, thu hồi tới trên $98\%$ bụi mịn. Trong công nghệ sơn tĩnh điện, hạt bột sơn mang điện tích dương bị hút chặt và phủ đều lên bề mặt chi tiết kim loại nối đất (tích điện âm)." "\n"
            r"- **Bản lái tia trong dao động kí và máy in phun (Inkjet)**: Máy in phun tích điện cho các giọt mực siêu nhỏ rồi cho bay qua điện trường đều giữa hai bản phẳng có hiệu điện thế điều khiển $U$, làm lệch quỹ đạo giọt mực tới đúng vị trí điểm ảnh trên trang giấy."
        ),
        "game_title": "Thí nghiệm Tương tác Điện tích, Đường sức Điện trường và Lọc bụi tĩnh điện",
        "game_description": "Đặt các điện tích điểm vào không gian để quan sát lực Coulomb, hệ đường sức điện trường tổng hợp và điều khiển bản cực điện trường đều để bẻ cong quỹ đạo chùm hạt mang điện.",
        "game_type": "game_dien_truong",
        "quiz": [
            mcq(
                "biet",
                r"Theo định luật Coulomb, độ lớn của lực tương tác tĩnh điện giữa hai điện tích điểm đặt trong chân không:",
                [
                    r"Tỉ lệ thuận với khoảng cách $r$ giữa hai điện tích",
                    r"Tỉ lệ nghịch với khoảng cách $r$ giữa hai điện tích",
                    r"Tỉ lệ nghịch với bình phương khoảng cách $r^2$ giữa hai điện tích",
                    r"Tỉ lệ thuận với bình phương khoảng cách $r^2$ giữa hai điện tích",
                ],
                2,
                r"Theo định luật Coulomb $F = k\dfrac{|q_1 q_2|}{r^2}$, độ lớn lực tương tác giữa hai điện tích điểm **tỉ lệ nghịch với bình phương khoảng cách $r^2$** giữa chúng.",
            ),
            mcq(
                "biet",
                r"Cường độ điện trường tại một điểm đặc trưng cho điện trường tại điểm đó về:",
                [
                    r"Phương diện dự trữ năng lượng điện",
                    r"Phương diện tác dụng lực",
                    r"Khả năng dẫn điện của môi trường",
                    r"Thể tích vùng không gian có điện trường",
                ],
                1,
                r"Cường độ điện trường $\vec{E} = \dfrac{\vec{F}}{q}$ là đại lượng vectơ đặc trưng cho điện trường tại điểm đang xét về **phương diện tác dụng lực**.",
            ),
            mcq(
                "biet",
                r"Giữa hai bản kim loại phẳng song song đặt cách nhau một khoảng $d$, tích điện trái dấu với hiệu điện thế $U$, cường độ điện trường đều $E$ giữa hai bản được tính bằng công thức:",
                [
                    r"$E = U\cdot d$",
                    r"$E = \dfrac{U}{d}$",
                    r"$E = \dfrac{d}{U}$",
                    r"$E = \dfrac{U}{d^2}$",
                ],
                1,
                r"Trong điện trường đều giữa hai bản phẳng song song cách nhau một khoảng $d$, liên hệ giữa cường độ điện trường và hiệu điện thế là **$E = \dfrac{U}{d}$**.",
            ),
            mcq(
                "biet",
                r"Khi đặt một điện tích thử âm ($q < 0$) tại một điểm có vectơ cường độ điện trường $\vec{E}$ thì lực điện $\vec{F}$ tác dụng lên điện tích đó có chiều:",
                [
                    r"Cùng phương, cùng chiều với $\vec{E}$",
                    r"Cùng phương, ngược chiều với $\vec{E}$",
                    r"Vuông góc với $\vec{E}$",
                    r"Hợp với $\vec{E}$ một góc $45^\circ$",
                ],
                1,
                r"Ta có $\vec{F} = q\vec{E}$. Vì $q < 0$ nên vectơ lực điện $\vec{F}$ luôn **cùng phương, ngược chiều với vectơ cường độ điện trường $\vec{E}$**.",
            ),
            mcq(
                "hieu",
                r"Một điện tích điểm $Q = +2 \cdot 10^{-8}\text{ C}$ đặt trong chân không. Lấy $k = 9 \cdot 10^9\text{ N}\cdot\text{m}^2\text{/C}^2$. Độ lớn cường độ điện trường do $Q$ gây ra tại điểm $M$ cách nó một khoảng $r = 3\text{ cm}$ là:",
                [
                    r"$2 \cdot 10^5\text{ V/m}$",
                    r"$6 \cdot 10^3\text{ V/m}$",
                    r"$2 \cdot 10^4\text{ V/m}$",
                    r"$1,8 \cdot 10^5\text{ V/m}$",
                ],
                0,
                r"Đổi $r = 3\text{ cm} = 0,03\text{ m}$. Độ lớn cường độ điện trường tại $M$ là $E = k\dfrac{|Q|}{r^2} = 9 \cdot 10^9 \cdot \dfrac{2 \cdot 10^{-8}}{0,03^2} = \dfrac{180}{9 \cdot 10^{-4}} = \mathbf{2 \cdot 10^5\text{ V/m}}$.",
            ),
            mcq(
                "hieu",
                r"Hai bản kim loại phẳng nằm ngang song song cách nhau $d = 2\text{ cm}$, hiệu điện thế giữa hai bản là $U = 120\text{ V}$. Một hạt bụi mang điện tích $q = 5 \cdot 10^{-10}\text{ C}$ nằm trong khoảng không gian giữa hai bản sẽ chịu tác dụng của lực điện có độ lớn là:",
                [
                    r"$3 \cdot 10^{-6}\text{ N}$",
                    r"$6 \cdot 10^{-6}\text{ N}$",
                    r"$3 \cdot 10^{-8}\text{ N}$",
                    r"$1,2 \cdot 10^{-7}\text{ N}$",
                ],
                0,
                r"Đổi $d = 0,02\text{ m}$. Cường độ điện trường đều giữa hai bản là $E = \dfrac{U}{d} = \dfrac{120}{0,02} = 6\,000\text{ V/m}$. Độ lớn lực điện tác dụng lên hạt bụi là $F = |q|E = 5 \cdot 10^{-10} \cdot 6\,000 = \mathbf{3 \cdot 10^{-6}\text{ N}}$.",
            ),
            tf4(
                "hieu",
                r"Cho hai điện tích điểm $q_1 = +2\,\mu\text{C}$ và $q_2 = -6\,\mu\text{C}$ đặt cách nhau một khoảng $r = 30\text{ cm}$ trong chân không. Lấy $k = 9 \cdot 10^9\text{ N}\cdot\text{m}^2\text{/C}^2$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Lực tương tác tĩnh điện giữa hai điện tích $q_1$ và $q_2$ là lực hút.",
                    r"b) Độ lớn lực tương tác giữa hai điện tích ở khoảng cách $r = 30\text{ cm}$ là $F = 1,2\text{ N}$.",
                    r"c) Nếu tăng khoảng cách giữa hai điện tích lên gấp đôi ($r' = 60\text{ cm}$) thì độ lớn lực tương tác giảm đi một nửa còn $0,6\text{ N}$.",
                    r"d) Nếu nhúng toàn bộ hệ hai điện tích (giữ nguyên khoảng cách $r = 30\text{ cm}$) vào dầu hoả có hằng số điện môi $\varepsilon = 2$ thì độ lớn lực tương tác là $0,6\text{ N}$.",
                ],
                [True, True, False, True],
                r"a) Hai điện tích $q_1 > 0$ và $q_2 < 0$ trái dấu nên hút nhau → **Đúng**." "\n"
                r"b) Đổi $r = 0,3\text{ m}$. Ta có $F = k\dfrac{|q_1 q_2|}{r^2} = 9 \cdot 10^9 \cdot \dfrac{2 \cdot 10^{-6} \cdot 6 \cdot 10^{-6}}{0,3^2} = \dfrac{0,108}{0,09} = 1,2\text{ N}$ → **Đúng**." "\n"
                r"c) Vì $F \sim \dfrac{1}{r^2}$ nên khi $r$ tăng gấp $2$ lần thì $F$ giảm $2^2 = 4$ lần, còn $\dfrac{1,2}{4} = 0,3\text{ N} \neq 0,6\text{ N}$ → **Sai**." "\n"
                r"d) Trong điện môi có $\varepsilon = 2$, lực tương tác giảm $\varepsilon = 2$ lần: $F' = \dfrac{F}{\varepsilon} = \dfrac{1,2}{2} = 0,6\text{ N}$ → **Đúng**.",
            ),
            tf4(
                "hieu",
                r"Khi khảo sát tính chất của đường sức điện và chuyển động của hạt mang điện trong điện trường đều, mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Qua một điểm bất kì trong điện trường chỉ vẽ được duy nhất một đường sức điện nên các đường sức điện không bao giờ cắt nhau.",
                    r"b) Các đường sức của điện trường đều là những đường thẳng song song và cách đều nhau.",
                    r"c) Khi một electron ($q = -e < 0$) bay vào điện trường đều theo phương vuông góc với đường sức điện thì nó bị lệch về phía theo chiều của đường sức điện.",
                    r"d) Nơi nào có cường độ điện trường lớn hơn thì các đường sức điện ở nơi đó được vẽ mau (dày) hơn.",
                ],
                [True, True, False, True],
                r"a) Tại mỗi điểm trong điện trường vectơ $\vec{E}$ có một hướng xác định duy nhất, nên qua mỗi điểm chỉ có một đường sức điện và chúng không cắt nhau → **Đúng**." "\n"
                r"b) Điện trường đều có $\vec{E}$ như nhau tại mọi điểm nên đường sức điện là các đường thẳng song song, cách đều → **Đúng**." "\n"
                r"c) Electron mang điện tích âm ($q = -e < 0$) nên lực điện $\vec{F} = -e\vec{E}$ ngược chiều với $\vec{E}$; do đó electron bị lệch ngược chiều đường sức điện (về phía bản dương) → **Sai**." "\n"
                r"d) Theo quy ước vẽ đường sức điện, mật độ đường sức tỉ lệ với độ lớn cường độ điện trường $E$ → **Đúng**.",
            ),
            mcq(
                "vandung",
                r"Tại hai điểm $A$ và $B$ cách nhau $10\text{ cm}$ trong chân không có đặt hai điện tích điểm $q_1 = +16 \cdot 10^{-8}\text{ C}$ và $q_2 = -12 \cdot 10^{-8}\text{ C}$. Lấy $k = 9 \cdot 10^9\text{ N}\cdot\text{m}^2\text{/C}^2$. Cường độ điện trường tổng hợp tại điểm $C$ cách $A$ một đoạn $CA = 8\text{ cm}$ và cách $B$ một đoạn $CB = 6\text{ cm}$ có độ lớn là:",
                [
                    r"$4,50 \cdot 10^5\text{ V/m}$",
                    r"$5,25 \cdot 10^5\text{ V/m}$",
                    r"$3,75 \cdot 10^5\text{ V/m}$",
                    r"$2,25 \cdot 10^5\text{ V/m}$",
                ],
                2,
                r"Nhận thấy $CA^2 + CB^2 = 8^2 + 6^2 = 100 = 10^2 = AB^2$ nên tam giác $ABC$ vuông tại $C$, suy ra hai đường thẳng $AC$ và $BC$ vuông góc với nhau ($\vec{E}_1 \perp \vec{E}_2$). "
                r"Độ lớn cường độ điện trường thành phần tại $C$ là: "
                r"$E_1 = k\dfrac{|q_1|}{CA^2} = 9 \cdot 10^9 \cdot \dfrac{16 \cdot 10^{-8}}{0,08^2} = 2,25 \cdot 10^5\text{ V/m}$ và "
                r"$E_2 = k\dfrac{|q_2|}{CB^2} = 9 \cdot 10^9 \cdot \dfrac{12 \cdot 10^{-8}}{0,06^2} = 3,00 \cdot 10^5\text{ V/m}$. "
                r"Vì $\vec{E}_1 \perp \vec{E}_2$ nên $E_C = \sqrt{E_1^2 + E_2^2} = \sqrt{2,25^2 + 3,00^2} \cdot 10^5 = \mathbf{3,75 \cdot 10^5\text{ V/m}}$.",
            ),
            short(
                "vandung",
                r"Hai điện tích điểm $q_1 = +4\,\mu\text{C}$ và $q_2 = +9\,\mu\text{C}$ được giữ cố định tại hai điểm $A$ và $B$ cách nhau $50\text{ cm}$ trong chân không. Điểm $M$ trên đoạn thẳng $AB$ mà tại đó cường độ điện trường tổng hợp bằng không ($\vec{E}_M = \vec{0}$) cách điểm $A$ bao nhiêu $\text{cm}$?",
                ["20"],
                r"Vì $q_1$ và $q_2$ cùng dấu dương nên điểm $M$ có $\vec{E}_M = \vec{E}_1 + \vec{E}_2 = \vec{0}$ phải nằm trên đoạn thẳng $AB$, thoả mãn $r_1 + r_2 = AB = 50\text{ cm}$ và $E_1 = E_2$. "
                r"Ta có $k\dfrac{|q_1|}{r_1^2} = k\dfrac{|q_2|}{r_2^2} \Rightarrow \dfrac{r_1}{r_2} = \sqrt{\dfrac{|q_1|}{|q_2|}} = \sqrt{\dfrac{4}{9}} = \dfrac{2}{3}$. "
                r"Kết hợp với $r_1 + r_2 = 50\text{ cm}$, suy ra $r_1 = \dfrac{2}{2 + 3} \cdot 50 = \mathbf{20\text{ cm}}$.",
                unit=r"$\text{cm}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG III – PHẦN 2. THẾ NĂNG ĐIỆN, ĐIỆN THẾ VÀ TỤ ĐIỆN (BÀI 19 – BÀI 21)
    # =========================================================================
    {
        "topic": "dien-the",
        "title": "Chương III – Phần 2. Thế năng điện, Điện thế và Tụ điện",
        "icon": "🔋",
        "description": (
            "Chương III · SGK Vật lí 11 Kết nối tri thức với cuộc sống (tr. 76–89): Bài 19 – Bài 21. "
            "Công của lực điện và thế năng điện; điện thế, hiệu điện thế và mối liên hệ với cường độ điện trường; "
            "tụ điện, điện dung của bộ tụ ghép nối tiếp và song song, năng lượng của tụ điện."
        ),
        "requirements": [
            r"Thảo luận qua quan sát hình ảnh (hoặc tài liệu đa phương tiện) nêu được công của lực điện tác dụng lên một điện tích $q$ di chuyển trong điện trường đều không phụ thuộc vào hình dạng đường đi mà chỉ phụ thuộc vào vị trí điểm đầu và điểm cuối ($A = qEd$).",
            r"Nêu được thế năng của một điện tích $q$ trong điện trường đặc trưng cho khả năng sinh công của điện trường khi đặt điện tích $q$ tại điểm đang xét ($W_M = A_{M\infty} = qV_M$).",
            r"Nêu được điện thế tại một điểm trong điện trường đặc trưng cho điện trường tại điểm đó về thế năng, được xác định bằng công dịch chuyển một đơn vị điện tích dương từ điểm đó ra vô cực ($V_M = \dfrac{A_{M\infty}}{q}$); nêu được đơn vị đo điện thế là vôn ($\text{V}$).",
            r"Vận dụng được mối liên hệ hiệu điện thế $U_{MN} = V_M - V_N = \dfrac{A_{MN}}{q}$ và hệ thức $E = \dfrac{U}{d}$ giữa cường độ điện trường đều với hiệu điện thế.",
            r"Định nghĩa được điện dung $C = \dfrac{Q}{U}$ và đơn vị đo điện dung là fara ($\text{F}$).",
            r"Thảo luận để xây dựng được biểu thức tính điện dung của bộ tụ điện ghép nối tiếp và ghép song song; vận dụng được các công thức này.",
            r"Thảo luận để xây dựng được biểu thức tính năng lượng tụ điện $W = \dfrac{1}{2}QU = \dfrac{1}{2}CU^2 = \dfrac{Q^2}{2C}$ và nêu được một số ứng dụng của tụ điện trong cuộc sống.",
        ],
        "definition": (
            r"- **Công của lực điện và thế năng điện**: Lực tĩnh điện là lực thế; công của lực điện trong dịch chuyển của điện tích $q$ từ $M$ đến $N$ trong điện trường đều là $A_{MN} = qEd$ (với $d$ là độ dài đại số hình chiếu của $\overrightarrow{MN}$ lên chiều đường sức). Thế năng của điện tích $q$ tại điểm $M$ là $W_M = A_{M\infty}$." "\n"
            r"- **Điện thế và hiệu điện thế**: Điện thế tại điểm $M$ là $V_M = \dfrac{W_M}{q} = \dfrac{A_{M\infty}}{q}$ ($\text{V}$). Hiệu điện thế giữa hai điểm $M$, $N$ là $U_{MN} = V_M - V_N = \dfrac{A_{MN}}{q}$." "\n"
            r"- **Tụ điện và điện dung**: Tụ điện là một hệ hai vật dẫn đặt gần nhau và ngăn cách nhau bằng một lớp cách điện (điện môi), dùng để tích và phóng điện trong mạch. Điện dung của tụ điện là $C = \dfrac{Q}{U}$ (đơn vị fara, kí hiệu $\text{F}$), đặc trưng cho khả năng tích điện của tụ điện ở một hiệu điện thế nhất định."
        ),
        "theory": (
            r"### Bài 19. Thế năng điện" "\n"
            r"- **Công của lực điện trong điện trường đều**: Khi điện tích $q$ di chuyển từ điểm $M$ đến điểm $N$ trong điện trường đều $\vec{E}$, công của lực điện không phụ thuộc vào hình dạng đường đi mà chỉ phụ thuộc vào vị trí điểm đầu $M$ và điểm cuối $N$:" "\n"
            r"  $$A_{MN} = qEd$$" "\n"
            r"  Trong đó $d = s\cos\alpha$ là hình chiếu đại số của độ dịch chuyển $\overrightarrow{MN}$ lên phương và chiều của đường sức điện ($d > 0$ nếu hình chiếu cùng chiều $\vec{E}$, $d < 0$ nếu ngược chiều $\vec{E}$). Trong trường hợp tổng quát, trường tĩnh điện là một trường thế." "\n"
            r"- **Thế năng của một điện tích trong điện trường**: Thế năng điện $W_M$ của một điện tích $q$ tại điểm $M$ trong điện trường đặc trưng cho khả năng sinh công của điện trường khi đặt điện tích $q$ tại điểm đó, được đo bằng công của lực điện khi dịch chuyển điện tích $q$ từ điểm $M$ ra xa vô cực (hoặc tới bản cực chọn làm mốc thế năng bằng $0$): $W_M = A_{M\infty}$ và $A_{MN} = W_M - W_N$." "\n\n"
            r"### Bài 20. Điện thế" "\n"
            r"- **Khái niệm điện thế**: Thương số $V_M = \dfrac{W_M}{q} = \dfrac{A_{M\infty}}{q}$ không phụ thuộc vào độ lớn của điện tích thử $q$ mà chỉ phụ thuộc vào điện trường và vị trí điểm $M$, được gọi là điện thế tại điểm $M$ (đơn vị vôn, kí hiệu $\text{V}$, với $1\text{ V} = 1\text{ J/C}$)." "\n"
            r"- **Hiệu điện thế**: Hiệu điện thế giữa hai điểm $M$ và $N$ là hiệu điện thế tại $M$ và tại $N$:" "\n"
            r"  $$U_{MN} = V_M - V_N = \dfrac{W_M - W_N}{q} = \dfrac{A_{MN}}{q} \iff A_{MN} = qU_{MN}$$" "\n"
            r"- **Liên hệ giữa cường độ điện trường và hiệu điện thế**: Dọc theo chiều của đường sức điện, điện thế giảm dần ($V_M > V_N$ khi đi từ $M$ đến $N$ theo chiều $\vec{E}$). Trong điện trường đều, với hai điểm $M, N$ cách nhau khoảng $d$ dọc theo đường sức: $E = \dfrac{U_{MN}}{d}$. Đơn vị năng lượng thường dùng trong vật lí nguyên tử là electron-volt ($\text{eV}$): $1\text{ eV} = 1,6 \cdot 10^{-19}\text{ C} \cdot 1\text{ V} = 1,6 \cdot 10^{-19}\text{ J}$." "\n\n"
            r"### Bài 21. Tụ điện" "\n"
            r"- **Cấu tạo và điện dung của tụ điện**: Tụ điện phẳng gồm hai bản kim loại đặt song song cách nhau khoảng $d$, ngăn cách bởi lớp điện môi có hằng số điện môi $\varepsilon$. Khi nối hai bản với hiệu điện thế $U$, bản nối cực dương tích điện $+Q$, bản nối cực âm tích điện $-Q$. Điện dung của tụ là $C = \dfrac{Q}{U}$ ($\text{F}$). Các ước của fara: $1\text{ mF} = 10^{-3}\text{ F}$, $1\,\mu\text{F} = 10^{-6}\text{ F}$, $1\text{ nF} = 10^{-9}\text{ F}$, $1\text{ pF} = 10^{-12}\text{ F}$. Điện dung của tụ phẳng là $C = \dfrac{\varepsilon\varepsilon_0 S}{d} = \dfrac{\varepsilon S}{4\pi kd}$ (phụ thuộc cấu tạo hình học và chất điện môi, không phụ thuộc $Q$ và $U$)." "\n"
            r"- **Ghép các tụ điện**:" "\n"
            r"  - **Ghép nối tiếp**: $Q_{\text{bộ}} = Q_1 = Q_2 = \dots = Q_n$; $U_{\text{bộ}} = U_1 + U_2 + \dots + U_n$; $\dfrac{1}{C_{\text{bộ}}} = \dfrac{1}{C_1} + \dfrac{1}{C_2} + \dots + \dfrac{1}{C_n}$ (với $2$ tụ nối tiếp: $C_{\text{bộ}} = \dfrac{C_1 C_2}{C_1 + C_2}$)." "\n"
            r"  - **Ghép song song**: $U_{\text{bộ}} = U_1 = U_2 = \dots = U_n$; $Q_{\text{bộ}} = Q_1 + Q_2 + \dots + Q_n$; $C_{\text{bộ}} = C_1 + C_2 + \dots + C_n$." "\n"
            r"- **Năng lượng của tụ điện (năng lượng điện trường trong tụ)**:" "\n"
            r"  $$W = \dfrac{1}{2}QU = \dfrac{1}{2}CU^2 = \dfrac{Q^2}{2C}$$"
        ),
        "formulas": [
            G(
                "I. Công của lực điện, thế năng điện và hiệu điện thế",
                F("Công của lực điện trong điện trường đều", r"$A_{MN} = qEd = qEs\cos\alpha = W_M - W_N$", r"$d = s\cos\alpha$ là hình chiếu đại số của $\overrightarrow{MN}$ lên chiều $\vec{E}$"),
                F("Điện thế và hiệu điện thế", r"$V_M = \dfrac{A_{M\infty}}{q} = \dfrac{W_M}{q}, \quad U_{MN} = V_M - V_N = \dfrac{A_{MN}}{q}$", r"Suy ra $A_{MN} = qU_{MN}$; đơn vị điện thế và hiệu điện thế là $\text{V}$"),
                F("Định lí động năng cho hạt mang điện", r"$\Delta W_{\text{đ}} = \dfrac{1}{2}mv_N^2 - \dfrac{1}{2}mv_M^2 = A_{MN} = qU_{MN}$", r"Đổi đơn vị: $1\text{ eV} = 1,6 \cdot 10^{-19}\text{ J}$"),
            ),
            G(
                "II. Điện dung, ghép tụ điện và năng lượng tụ điện",
                F("Định nghĩa điện dung của tụ điện", r"$C = \dfrac{Q}{U} \iff Q = CU$", r"$C$ ($\text{F}$), $Q$ ($\text{C}$), $U$ ($\text{V}$); với tụ phẳng $C = \dfrac{\varepsilon\varepsilon_0 S}{d}$"),
                F("Bộ tụ điện ghép nối tiếp", r"$Q_{\text{bộ}} = Q_1 = Q_2, \quad U_{\text{bộ}} = U_1 + U_2, \quad \dfrac{1}{C_{\text{bộ}}} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$", r"Điện dung tương đương nhỏ hơn điện dung thành phần nhỏ nhất"),
                F("Bộ tụ điện ghép song song", r"$U_{\text{bộ}} = U_1 = U_2, \quad Q_{\text{bộ}} = Q_1 + Q_2, \quad C_{\text{bộ}} = C_1 + C_2$", r"Điện dung tương đương bằng tổng các điện dung thành phần"),
                F("Năng lượng điện trường trong tụ điện", r"$W = \dfrac{1}{2}QU = \dfrac{1}{2}CU^2 = \dfrac{Q^2}{2C}$", r"Đơn vị năng lượng là jun ($\text{J}$)"),
            ),
        ],
        "example": (
            r"Cho hai tụ điện có điện dung lần lượt là $C_1 = 3\,\mu\text{F}$ và $C_2 = 6\,\mu\text{F}$. "
            r"(a) Khi mắc nối tiếp hai tụ điện này rồi đặt vào hai đầu bộ tụ một hiệu điện thế $U = 120\text{ V}$, hãy tính điện dung tương đương $C_{\text{nt}}$, điện tích và hiệu điện thế trên mỗi tụ điện, cùng năng lượng của cả bộ tụ; "
            r"(b) Nếu mắc song song hai tụ điện đó vào cùng hiệu điện thế $U = 120\text{ V}$ thì điện dung tương đương $C_{\text{ss}}$ và năng lượng của bộ tụ bằng bao nhiêu?"
        ),
        "example_answer": (
            r"- **(a) Khi ghép nối tiếp hai tụ điện**: Điện dung tương đương là $C_{\text{nt}} = \dfrac{C_1 C_2}{C_1 + C_2} = \dfrac{3 \cdot 6}{3 + 6} = \mathbf{2\,\mu\text{F}} = 2 \cdot 10^{-6}\text{ F}$. Điện tích của bộ tụ bằng điện tích mỗi tụ: $Q = Q_1 = Q_2 = C_{\text{nt}}U = 2 \cdot 10^{-6} \cdot 120 = 2,4 \cdot 10^{-4}\text{ C} = \mathbf{240\,\mu\text{C}}$. Hiệu điện thế trên từng tụ là $U_1 = \dfrac{Q_1}{C_1} = \dfrac{240}{3} = \mathbf{80\text{ V}}$ và $U_2 = \dfrac{Q_2}{C_2} = \dfrac{240}{6} = \mathbf{40\text{ V}}$. Năng lượng của bộ tụ là $W_{\text{nt}} = \dfrac{1}{2}C_{\text{nt}}U^2 = \dfrac{1}{2} \cdot 2 \cdot 10^{-6} \cdot 120^2 = \mathbf{0,0144\text{ J}} = 14,4\text{ mJ}$." "\n"
            r"- **(b) Khi ghép song song hai tụ điện**: Điện dung tương đương là $C_{\text{ss}} = C_1 + C_2 = 3 + 6 = \mathbf{9\,\mu\text{F}} = 9 \cdot 10^{-6}\text{ F}$. Năng lượng của bộ tụ khi đó là $W_{\text{ss}} = \dfrac{1}{2}C_{\text{ss}}U^2 = \dfrac{1}{2} \cdot 9 \cdot 10^{-6} \cdot 120^2 = \mathbf{0,0648\text{ J}} = 64,8\text{ mJ}$."
        ),
        "real_life": (
            r"- **Máy khử rung tim (Defibrillator) và đèn Flash máy ảnh**: Tụ điện có khả năng tích điện từ từ rồi phóng trả toàn bộ năng lượng cực nhanh trong vài phần nghìn giây, tạo xung dòng điện lớn giúp kích nhịp tim cấp cứu hoặc làm loé sáng đèn Flash." "\n"
            r"- **Màn hình cảm ứng điện dung và bộ nhớ DRAM**: Màn hình điện thoại thông minh hoạt động dựa trên lưới tụ điện siêu nhỏ; khi ngón tay (vật dẫn) chạm vào màn hình sẽ làm thay đổi điện dung cục bộ tại điểm chạm, giúp chip xử lí định vị toạ độ chạm chính xác."
        ),
        "game_title": "Phòng thí nghiệm Điện thế và Lắp mạch Tụ điện (Nối tiếp – Song song)",
        "game_description": "Khảo sát các mặt đẳng thế trong điện trường, đo công của lực điện khi di chuyển điện tích và lắp ghép các bộ tụ điện nối tiếp, song song để nạp và phóng năng lượng điện trường.",
        "game_type": "game_dien_the",
        "quiz": [
            mcq(
                "biet",
                r"Công của lực điện tác dụng lên một điện tích $q$ di chuyển từ điểm $M$ đến điểm $N$ trong một điện trường tĩnh:",
                [
                    r"Phụ thuộc vào hình dạng của quỹ đạo chuyển động từ $M$ đến $N$",
                    r"Không phụ thuộc vào hình dạng đường đi mà chỉ phụ thuộc vào vị trí điểm đầu $M$ và điểm cuối $N$",
                    r"Luôn bằng không với mọi cặp điểm $M$ và $N$ bất kì",
                    r"Tỉ lệ thuận với tốc độ di chuyển của điện tích $q$",
                ],
                1,
                r"Trường tĩnh điện là trường thế nên công của lực điện **không phụ thuộc vào hình dạng của đường đi mà chỉ phụ thuộc vào vị trí của điểm đầu $M$ và điểm cuối $N$** ($A_{MN} = qU_{MN}$).",
            ),
            mcq(
                "biet",
                r"Mối liên hệ giữa hiệu điện thế $U_{MN}$, điện thế tại $M$ ($V_M$), điện thế tại $N$ ($V_N$) và công $A_{MN}$ của lực điện khi dịch chuyển điện tích $q$ từ $M$ đến $N$ là:",
                [
                    r"$U_{MN} = V_N - V_M = \dfrac{A_{MN}}{q}$",
                    r"$U_{MN} = V_M - V_N = \dfrac{A_{MN}}{q}$",
                    r"$U_{MN} = V_M - V_N = q\cdot A_{MN}$",
                    r"$U_{MN} = V_M + V_N = \dfrac{q}{A_{MN}}$",
                ],
                1,
                r"Hiệu điện thế giữa hai điểm $M$ và $N$ được xác định bởi công thức **$U_{MN} = V_M - V_N = \dfrac{A_{MN}}{q}$**.",
            ),
            mcq(
                "biet",
                r"Đại lượng đặc trưng cho khả năng tích điện của tụ điện ở một hiệu điện thế nhất định là điện dung $C$, được xác định bằng công thức:",
                [
                    r"$C = Q\cdot U$",
                    r"$C = \dfrac{U}{Q}$",
                    r"$C = \dfrac{Q}{U}$",
                    r"$C = \dfrac{1}{2}QU^2$",
                ],
                2,
                r"Điện dung của tụ điện là thương số giữa điện tích $Q$ của tụ điện và hiệu điện thế $U$ giữa hai bản của tụ: **$C = \dfrac{Q}{U}$** (đơn vị fara, $\text{F}$).",
            ),
            mcq(
                "biet",
                r"Khi ghép song song hai tụ điện có điện dung $C_1$ và $C_2$ thì điện dung tương đương $C_{\text{bộ}}$ của bộ tụ được tính theo công thức:",
                [
                    r"$C_{\text{bộ}} = C_1 + C_2$",
                    r"$C_{\text{bộ}} = \dfrac{C_1 C_2}{C_1 + C_2}$",
                    r"$C_{\text{bộ}} = |C_1 - C_2|$",
                    r"$\dfrac{1}{C_{\text{bộ}}} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$",
                ],
                0,
                r"Khi ghép các tụ điện song song, hiệu điện thế trên các tụ bằng nhau và điện tích cộng lại nên **$C_{\text{bộ}} = C_1 + C_2$**.",
            ),
            mcq(
                "hieu",
                r"Một điện tích $q = +2\,\mu\text{C}$ di chuyển trong một điện trường đều có cường độ $E = 2\,000\text{ V/m}$ dọc theo một đường sức điện một đoạn $s = 5\text{ cm}$ theo chiều của đường sức điện. Công của lực điện trong dịch chuyển đó bằng:",
                [
                    r"$2 \cdot 10^{-4}\text{ J}$",
                    r"$-2 \cdot 10^{-4}\text{ J}$",
                    r"$2 \cdot 10^{-2}\text{ J}$",
                    r"$4 \cdot 10^{-4}\text{ J}$",
                ],
                0,
                r"Vì điện tích di chuyển cùng chiều đường sức nên $d = s = 0,05\text{ m}$. Công của lực điện là $A = qEd = 2 \cdot 10^{-6} \cdot 2\,000 \cdot 0,05 = \mathbf{2 \cdot 10^{-4}\text{ J}}$.",
            ),
            mcq(
                "hieu",
                r"Một tụ điện có điện dung $C = 20\,\mu\text{F}$ được tích điện dưới hiệu điện thế $U = 50\text{ V}$. Điện tích $Q$ và năng lượng điện trường $W$ dự trữ trong tụ điện lần lượt là:",
                [
                    r"$Q = 10^{-3}\text{ C}, \ W = 0,025\text{ J}$",
                    r"$Q = 10^{-3}\text{ C}, \ W = 0,050\text{ J}$",
                    r"$Q = 4 \cdot 10^{-7}\text{ C}, \ W = 0,025\text{ J}$",
                    r"$Q = 10^{-2}\text{ C}, \ W = 0,250\text{ J}$",
                ],
                0,
                r"Đổi $C = 20 \cdot 10^{-6}\text{ F}$. Điện tích của tụ là $Q = CU = 20 \cdot 10^{-6} \cdot 50 = \mathbf{10^{-3}\text{ C}}$. Năng lượng của tụ điện là $W = \dfrac{1}{2}CU^2 = \dfrac{1}{2} \cdot 20 \cdot 10^{-6} \cdot 50^2 = \mathbf{0,025\text{ J}}$.",
            ),
            tf4(
                "hieu",
                r"Trong một điện trường đều có cường độ $E = 1\,000\text{ V/m}$, xét tam giác vuông $ABC$ vuông tại $A$ có cạnh $AB = 6\text{ cm}$ song song và cùng chiều với vectơ cường độ điện trường $\vec{E}$, cạnh $AC = 8\text{ cm}$ vuông góc với $\vec{E}$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Hai điểm $A$ và $C$ nằm trên cùng một mặt đẳng thế nên hiệu điện thế $U_{AC} = V_A - V_C = 0\text{ V}$.",
                    r"b) Hiệu điện thế giữa hai điểm $A$ và $B$ là $U_{AB} = V_A - V_B = 60\text{ V}$.",
                    r"c) Hiệu điện thế giữa hai điểm $B$ và $C$ là $U_{BC} = 60\text{ V}$.",
                    r"d) Công của lực điện khi dịch chuyển một điện tích $q = 5\,\mu\text{C}$ dọc theo đường gấp khúc $A \rightarrow C \rightarrow B$ là $A_{ACB} = 3 \cdot 10^{-4}\text{ J}$.",
                ],
                [True, True, False, True],
                r"a) Vì $AC \perp \vec{E}$ nên hình chiếu của $AC$ lên phương $\vec{E}$ bằng $0$ ($d_{AC} = 0$), suy ra $U_{AC} = Ed_{AC} = 0\text{ V}$ hay $V_A = V_C$ → **Đúng**." "\n"
                r"b) Đổi $d_{AB} = 0,06\text{ m}$. Vì $\overrightarrow{AB} \uparrow\uparrow \vec{E}$ nên $U_{AB} = Ed_{AB} = 1\,000 \cdot 0,06 = 60\text{ V}$ → **Đúng**." "\n"
                r"c) Ta có $U_{BC} = V_B - V_C = V_B - V_A = -U_{AB} = -60\text{ V} \neq 60\text{ V}$ → **Sai**." "\n"
                r"d) Công của lực điện không phụ thuộc đường đi: $A_{ACB} = A_{AB} = qU_{AB} = 5 \cdot 10^{-6} \cdot 60 = 3 \cdot 10^{-4}\text{ J}$ → **Đúng**.",
            ),
            tf4(
                "hieu",
                r"Một tụ điện phẳng không khí ($\varepsilon = 1$) có điện dung $C_0 = 10\,\mu\text{F}$ được nối vào hai cực của một nguồn điện không đổi có hiệu điện thế $U = 20\text{ V}$. Trên vỏ tụ điện có ghi thông số $10\,\mu\text{F} - 50\text{ V}$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Giá trị $50\text{ V}$ ghi trên vỏ tụ điện là hiệu điện thế định mức (tối đa) mà tụ có thể chịu được mà không bị đánh thủng lớp điện môi.",
                    r"b) Khi đang nối với nguồn $U = 20\text{ V}$, điện tích trên tụ điện là $Q_0 = 200\,\mu\text{C}$.",
                    r"c) Nếu giữ nguyên kết nối với nguồn $U = 20\text{ V}$ và tăng hiệu điện thế của nguồn lên gấp đôi ($U' = 40\text{ V}$) thì điện dung $C_0$ của tụ điện cũng tăng lên gấp đôi thành $20\,\mu\text{F}$.",
                    r"d) Nếu ngắt tụ điện khỏi nguồn (điện tích $Q_0 = 200\,\mu\text{C}$ được giữ không đổi) rồi lấp đầy khoảng giữa hai bản bằng chất điện môi có $\varepsilon = 2$ thì hiệu điện thế giữa hai bản tụ giảm xuống còn $10\text{ V}$.",
                ],
                [True, True, False, True],
                r"a) Số vôn ghi trên vỏ tụ điện là điện áp giới hạn (định mức) để tụ hoạt động an toàn → **Đúng**." "\n"
                r"b) Ta có $Q_0 = C_0 U = 10\,\mu\text{F} \cdot 20\text{ V} = 200\,\mu\text{C}$ → **Đúng**." "\n"
                r"c) Điện dung $C_0$ của tụ điện chỉ phụ thuộc vào cấu tạo của tụ, không phụ thuộc vào hiệu điện thế đặt vào tụ → **Sai**." "\n"
                r"d) Khi đưa điện môi $\varepsilon = 2$ vào, điện dung tăng lên thành $C' = \varepsilon C_0 = 20\,\mu\text{F}$; vì đã ngắt khỏi nguồn nên $Q_0 = 200\,\mu\text{C}$ không đổi, suy ra $U' = \dfrac{Q_0}{C'} = \dfrac{200}{20} = 10\text{ V}$ → **Đúng**.",
            ),
            mcq(
                "vandung",
                r"Một electron (điện tích $q = -1,6 \cdot 10^{-19}\text{ C}$, khối lượng $m = 9,1 \cdot 10^{-31}\text{ kg}$) bắt đầu chuyển động không vận tốc đầu từ bản âm sang bản dương giữa hai bản phẳng song song có hiệu điện thế $U = 45,5\text{ V}$ đặt trong chân không. Bỏ qua tác dụng của trọng lực. Tốc độ của electron ngay khi vừa tới bản dương là:",
                [
                    r"$4 \cdot 10^6\text{ m/s}$",
                    r"$2 \cdot 10^6\text{ m/s}$",
                    r"$8 \cdot 10^6\text{ m/s}$",
                    r"$1,6 \cdot 10^7\text{ m/s}$",
                ],
                0,
                r"Áp dụng định lí động năng cho electron di chuyển từ bản âm (vận tốc đầu $v_0 = 0$) đến bản dương dưới hiệu điện thế tăng tốc $U = 45,5\text{ V}$: "
                r"$\dfrac{1}{2}mv^2 - 0 = |q|U \Rightarrow v = \sqrt{\dfrac{2|q|U}{m}} = \sqrt{\dfrac{2 \cdot 1,6 \cdot 10^{-19} \cdot 45,5}{9,1 \cdot 10^{-31}}} = \sqrt{16 \cdot 10^{12}} = \mathbf{4 \cdot 10^6\text{ m/s}}$.",
            ),
            short(
                "vandung",
                r"Một bộ tụ điện trong đèn Flash máy ảnh có điện dung tương đương $C = 800\,\mu\text{F}$ được nạp đầy điện ở hiệu điện thế $U = 300\text{ V}$. Khi bấm chụp, tụ điện phóng toàn bộ năng lượng dự trữ của nó qua bóng đèn trong khoảng thời gian $\Delta t = 2\text{ ms}$. Công suất trung bình của lần phóng điện này bằng bao nhiêu $\text{kW}$?",
                ["18"],
                r"Đổi $C = 800 \cdot 10^{-6}\text{ F} = 8 \cdot 10^{-4}\text{ F}$, $\Delta t = 2\text{ ms} = 2 \cdot 10^{-3}\text{ s}$. "
                r"Năng lượng điện trường tích trữ trong tụ điện là $W = \dfrac{1}{2}CU^2 = \dfrac{1}{2} \cdot 8 \cdot 10^{-4} \cdot 300^2 = 36\text{ J}$. "
                r"Công suất trung bình khi phóng điện là $\mathcal{P} = \dfrac{W}{\Delta t} = \dfrac{36}{2 \cdot 10^{-3}} = 18\,000\text{ W} = \mathbf{18\text{ kW}}$.",
                unit=r"$\text{kW}$",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG IV. DÒNG ĐIỆN, MẠCH ĐIỆN (BÀI 22 – BÀI 26)
    # =========================================================================
    {
        "topic": "dong-dien",
        "title": "Chương IV. Dòng điện, Mạch điện",
        "icon": "🔌",
        "description": (
            "Chương IV · SGK Vật lí 11 Kết nối tri thức với cuộc sống (tr. 90–113): Bài 22 – Bài 26. "
            "Cường độ dòng điện và tốc độ dịch chuyển có hướng của hạt mang điện; điện trở, định luật Ohm và điện trở nhiệt; "
            "nguồn điện, suất điện động và định luật Ohm cho toàn mạch; năng lượng điện, công suất điện và thực hành đo suất điện động, điện trở trong của pin."
        ),
        "requirements": [
            r"Định nghĩa được cường độ dòng điện là đại lượng đặc trưng cho tác dụng mạnh, yếu của dòng điện và được xác định bằng điện lượng chuyển qua tiết diện thẳng của vật dẫn trong một đơn vị thời gian ($I = \dfrac{\Delta q}{\Delta t}$).",
            r"Vận dụng được biểu thức $I = Snve$ cho dây dẫn có dòng điện, với $n$ là mật độ hạt mang điện tự do, $S$ là tiết diện thẳng của dây, $v$ là tốc độ dịch chuyển có hướng của hạt mang điện tích $e$; định nghĩa được đơn vị đo điện lượng coulomb ($\text{C}$) là lượng điện tích chuyển qua tiết diện thẳng của dây dẫn trong $1\text{ s}$ khi có cường độ dòng điện $1\text{ A}$ chạy qua.",
            r"Định nghĩa được điện trở $R = \dfrac{U}{I}$, đơn vị đo điện trở là ôm ($\Omega$) và nêu được các nguyên nhân chính gây ra điện trở trong kim loại.",
            r"Vẽ phác và thảo luận được về đường đặc trưng vôn – ampe ($I - U$) của vật dẫn kim loại ở nhiệt độ xác định; mô tả được sơ lược ảnh hưởng của nhiệt độ lên điện trở của đèn sợi đốt và điện trở nhiệt (thermistor); phát biểu được định luật Ohm cho vật dẫn kim loại.",
            r"Định nghĩa được suất điện động $\mathcal{E} = \dfrac{A}{q}$ qua năng lượng dịch chuyển một điện tích đơn vị theo vòng kín; mô tả được ảnh hưởng của điện trở trong $r$ của nguồn điện lên hiệu điện thế giữa hai cực của nguồn ($U = \mathcal{E} - Ir$); so sánh được suất điện động và hiệu điện thế.",
            r"Nêu được năng lượng điện tiêu thụ của đoạn mạch được đo bằng công của lực điện thực hiện khi dịch chuyển các điện tích; công suất tiêu thụ năng lượng điện của một đoạn mạch là năng lượng điện mà đoạn mạch tiêu thụ trong một đơn vị thời gian; tính được năng lượng điện $W = UIt$ và công suất điện $\mathcal{P} = UI$ của đoạn mạch.",
            r"Thảo luận để thiết kế phương án hoặc lựa chọn phương án và thực hiện phương án, đo được suất điện động $\mathcal{E}$ và điện trở trong $r$ của pin hoặc acquy bằng dụng cụ thực hành.",
        ],
        "definition": (
            r"- **Cường độ dòng điện**: Là đại lượng đặc trưng cho tác dụng mạnh, yếu của dòng điện, được đo bằng thương số giữa điện lượng $\Delta q$ dịch chuyển qua tiết diện thẳng của vật dẫn và khoảng thời gian $\Delta t$: $I = \dfrac{\Delta q}{\Delta t}$. Với dòng điện không đổi: $I = \dfrac{q}{t} = Snve$." "\n"
            r"- **Điện trở và định luật Ohm**: Điện trở $R = \dfrac{U}{I}$ ($\Omega$) đặc trưng cho mức độ cản trở dòng điện của vật dẫn. Định luật Ohm cho vật dẫn kim loại: Ở nhiệt độ không đổi, cường độ dòng điện $I$ chạy qua dây dẫn tỉ lệ thuận với hiệu điện thế $U$ giữa hai đầu dây và tỉ lệ nghịch với điện trở $R$ của nó ($I = \dfrac{U}{R}$)." "\n"
            r"- **Nguồn điện và công suất điện**: Suất điện động $\mathcal{E} = \dfrac{A}{q}$ ($\text{V}$) đặc trưng cho khả năng thực hiện công của nguồn điện. Định luật Ohm cho toàn mạch: $I = \dfrac{\mathcal{E}}{R_{\text{N}} + r}$. Công suất tiêu thụ điện của đoạn mạch là $\mathcal{P} = UI$, năng lượng điện tiêu thụ là $W = \mathcal{P}t = UIt$."
        ),
        "theory": (
            r"### Bài 22. Cường độ dòng điện" "\n"
            r"- **Dòng điện và chiều dòng điện quy ước**: Dòng điện là dòng dịch chuyển có hướng của các hạt mang điện. Trong kim loại, hạt tải điện là các electron tự do dịch chuyển có hướng ngược chiều điện trường. Chiều quy ước của dòng điện là chiều dịch chuyển có hướng của các điện tích dương (ngược chiều dịch chuyển của các electron tự do)." "\n"
            r"- **Cường độ dòng điện và đơn vị điện lượng coulomb ($\text{C}$)**: $I = \dfrac{\Delta q}{\Delta t}$. Với dòng điện không đổi (chiều và cường độ không đổi theo thời gian): $I = \dfrac{q}{t} \iff q = It$. Đơn vị cường độ dòng điện là ampe ($\text{A}$); đơn vị điện lượng $1\text{ C} = 1\text{ A}\cdot 1\text{ s}$." "\n"
            r"- **Liên hệ với tốc độ dịch chuyển có hướng của hạt mang điện**: Xét dây dẫn hình trụ tiết diện thẳng $S$, mật độ hạt mang điện tự do là $n$ (số hạt trong $1\text{ m}^3$), mỗi hạt mang điện tích có độ lớn $e$ và dịch chuyển có hướng với tốc độ trung bình $v$, ta có:" "\n"
            r"  $$I = Snve$$" "\n\n"
            r"### Bài 23. Điện trở. Định luật Ohm" "\n"
            r"- **Định nghĩa điện trở**: $R = \dfrac{U}{I}$, đơn vị là ôm ($\Omega$, với $1\,\Omega = 1\text{ V/A}$; $1\text{ k}\Omega = 10^3\,\Omega$, $1\text{ M}\Omega = 10^6\,\Omega$). Với dây dẫn đồng chất tiết diện đều $S$, chiều dài $l$, điện trở suất $\rho$: $R = \rho\dfrac{l}{S}$." "\n"
            r"- **Định luật Ohm cho vật dẫn kim loại và đường đặc trưng $I - U$**: Với vật dẫn kim loại ở nhiệt độ xác định, $I = \dfrac{U}{R}$; đường đặc trưng vôn – ampe ($I - U$) là một đoạn thẳng đi qua gốc toạ độ, độ dốc càng lớn thì điện trở $R$ càng nhỏ." "\n"
            r"- **Nguyên nhân gây ra điện trở và ảnh hưởng của nhiệt độ**: Nguyên nhân chính gây ra điện trở của kim loại là sự va chạm của các electron tự do với các ion dương đang dao động nhiệt quanh nút mạng tinh thể. Khi nhiệt độ $T$ tăng, các ion dao động mạnh hơn nên điện trở của kim loại (như dây tóc bóng đèn sợi đốt) tăng theo công thức $R = R_0[1 + \alpha(t - t_0)]$, làm đường đặc trưng $I - U$ bị cong đi ở hiệu điện thế cao. Điện trở nhiệt (thermistor) là linh kiện bán dẫn có điện trở biến thiên nhạy theo nhiệt độ: loại $\text{NTC}$ có điện trở giảm mạnh khi nhiệt độ tăng, còn loại $\text{PTC}$ có điện trở tăng khi nhiệt độ tăng." "\n\n"
            r"### Bài 24. Nguồn điện" "\n"
            r"- **Nguồn điện và suất điện động $\mathcal{E}$**: Nguồn điện dùng lực lạ (bản chất phi tĩnh điện) để tách và duy trì sự chênh lệch điện thế giữa hai cực. Suất điện động $\mathcal{E}$ được đo bằng thương số giữa công $A$ của lực lạ khi dịch chuyển một điện tích dương $q$ ngược chiều điện trường bên trong nguồn (hoặc đi trọn một vòng kín) và độ lớn $q$: $\mathcal{E} = \dfrac{A}{q}$ (đơn vị vôn, $\text{V}$)." "\n"
            r"- **Điện trở trong $r$ và định luật Ohm cho toàn mạch**: Mỗi nguồn điện đều có điện trở trong $r$. Khi nối nguồn ($\mathcal{E}, r$) với mạch ngoài có điện trở tương đương $R_{\text{N}}$ tạo thành mạch kín:" "\n"
            r"  $$I = \dfrac{\mathcal{E}}{R_{\text{N}} + r} \iff \mathcal{E} = I(R_{\text{N}} + r) = U_{\text{N}} + Ir \implies U_{\text{N}} = \mathcal{E} - Ir$$" "\n"
            r"  Khi mạch hở ($I = 0$) hoặc $r = 0$ thì $U_{\text{N}} = \mathcal{E}$. Hiện tượng đoản mạch xảy ra khi $R_{\text{N}} \approx 0$, lúc đó dòng điện đạt cực đại $I_{\text{đm}} = \dfrac{\mathcal{E}}{r}$ rất lớn, dễ gây cháy nổ." "\n\n"
            r"### Bài 25. Năng lượng và công suất điện" "\n"
            r"- **Năng lượng điện và công suất tiêu thụ của đoạn mạch**: Năng lượng điện tiêu thụ của đoạn mạch trong thời gian $t$ là $W = A = Uq = UIt$ ($\text{J}$). Công suất điện tiêu thụ là $\mathcal{P} = \dfrac{W}{t} = UI$ ($\text{W}$). Trên công tơ điện, $1\text{ kWh} = 1\,000\text{ W} \cdot 3\,600\text{ s} = 3,6 \cdot 10^6\text{ J}$." "\n"
            r"- **Định luật Joule – Lenz cho đoạn mạch thuần trở $R$**: Nhiệt lượng toả ra trên điện trở $R$ là $Q = I^2 Rt = \dfrac{U^2}{R}t = UIt$, công suất toả nhiệt là $\mathcal{P}_{\text{nhiệt}} = I^2 R = \dfrac{U^2}{R}$." "\n"
            r"- **Công, công suất và hiệu suất của nguồn điện**: Công của nguồn điện là $A_{\text{ng}} = \mathcal{E}It$, công suất của nguồn điện là $\mathcal{P}_{\text{ng}} = \mathcal{E}I$. Hiệu suất của nguồn điện là $H = \dfrac{\mathcal{P}_{\text{N}}}{\mathcal{P}_{\text{ng}}} = \dfrac{U_{\text{N}}}{\mathcal{E}} = \dfrac{R_{\text{N}}}{R_{\text{N}} + r}$." "\n\n"
            r"### Bài 26. Thực hành: Đo suất điện động và điện trở trong của pin điện hoá" "\n"
            r"- **Phương pháp thực hành**: Mắc pin điện hoá ($\mathcal{E}, r$) với biến trở, điện trở bảo vệ $R_0$, ampe kế nối tiếp và vôn kế mắc song song vào hai cực của pin. Thay đổi giá trị biến trở để đọc các cặp giá trị $(I, U)$ tương ứng. Vẽ đồ thị $U$ theo $I$ dựa trên phương trình đường thẳng $U = \mathcal{E} - rI$: giao điểm của đường thẳng với trục tung ($I = 0$) cho giá trị $\mathcal{E}$, và độ dốc của đường thẳng cho giá trị điện trở trong $r = -\dfrac{\Delta U}{\Delta I} = \dfrac{U_1 - U_2}{I_2 - I_1}$."
        ),
        "formulas": [
            G(
                "I. Cường độ dòng điện, điện trở và định luật Ohm đoạn mạch",
                F("Cường độ dòng điện", r"$I = \dfrac{\Delta q}{\Delta t}, \quad I = \dfrac{q}{t} = \dfrac{N\cdot e}{t} \quad (\text{dòng không đổi})$", r"$q$ ($\text{C}$), $t$ ($\text{s}$), $I$ ($\text{A}$); $e = 1,6 \cdot 10^{-19}\text{ C}$"),
                F("Công thức vi mô của dòng điện", r"$I = Snve \iff v = \dfrac{I}{Sne}$", r"$n$ ($\text{m}^{-3}$) là mật độ hạt tải, $S$ ($\text{m}^2$), $v$ ($\text{m/s}$)"),
                F("Định luật Ohm và điện trở dây dẫn", r"$I = \dfrac{U}{R} \iff R = \dfrac{U}{I}, \quad R = \rho\dfrac{l}{S}$", r"Nối tiếp: $R_{\text{td}} = R_1 + R_2$; song song: $\dfrac{1}{R_{\text{td}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$"),
            ),
            G(
                "II. Nguồn điện và định luật Ohm cho toàn mạch",
                F("Suất điện động của nguồn điện", r"$\mathcal{E} = \dfrac{A}{q} \iff A = q\mathcal{E} = \mathcal{E}It$", r"$A$ ($\text{J}$) là công của lực lạ dịch chuyển điện tích $q$"),
                F("Định luật Ohm cho toàn mạch và hiệu điện thế hai cực", r"$I = \dfrac{\mathcal{E}}{R_{\text{N}} + r}, \quad U_{\text{N}} = I R_{\text{N}} = \mathcal{E} - Ir$", r"Khi đoản mạch ($R_{\text{N}} = 0$): $I_{\text{đm}} = \dfrac{\mathcal{E}}{r}$"),
                F(r"Xác định $\mathcal{E}, r$ từ hai phép đo thực hành", r"$r = \dfrac{U_1 - U_2}{I_2 - I_1}, \quad \mathcal{E} = U_1 + I_1 r$", r"Từ phương trình đường thẳng $U = \mathcal{E} - rI$"),
            ),
            G(
                "III. Năng lượng điện, công suất điện và hiệu suất nguồn",
                F("Năng lượng và công suất tiêu thụ đoạn mạch", r"$W = UIt, \quad \mathcal{P} = \dfrac{W}{t} = UI$", r"$1\text{ kWh} = 3,6 \cdot 10^6\text{ J}$"),
                F("Công suất toả nhiệt trên điện trở $R$", r"$\mathcal{P}_{\text{nhiệt}} = I^2 R = \dfrac{U^2}{R}, \quad Q = I^2 Rt$", r"Áp dụng cho đoạn mạch thuần điện trở"),
                F("Công suất và hiệu suất của nguồn điện", r"$\mathcal{P}_{\text{ng}} = \mathcal{E}I, \quad H = \dfrac{U_{\text{N}}}{\mathcal{E}} = \dfrac{R_{\text{N}}}{R_{\text{N}} + r}$", r"Công suất mạch ngoài cực đại khi $R_{\text{N}} = r$: $\mathcal{P}_{\text{N}\max} = \dfrac{\mathcal{E}^2}{4r}$"),
            ),
        ],
        "example": (
            r"Một nguồn điện một chiều có suất điện động $\mathcal{E} = 12\text{ V}$ và điện trở trong $r = 1\,\Omega$ được nối với mạch ngoài gồm hai điện trở $R_1 = 6\,\Omega$ và $R_2 = 12\,\Omega$ mắc song song với nhau tạo thành mạch kín. "
            r"Hãy tính: (a) Điện trở tương đương $R_{\text{N}}$ của mạch ngoài và cường độ dòng điện chính $I$ chạy qua nguồn; "
            r"(b) Hiệu điện thế $U_{\text{N}}$ giữa hai cực của nguồn và cường độ dòng điện chạy qua mỗi điện trở $R_1$, $R_2$; "
            r"(c) Công suất của nguồn điện $\mathcal{P}_{\text{ng}}$, công suất tiêu thụ ở mạch ngoài $\mathcal{P}_{\text{N}}$ và hiệu suất $H$ của nguồn điện."
        ),
        "example_answer": (
            r"- **(a) Điện trở mạch ngoài và dòng điện qua nguồn**: Vì $R_1 \parallel R_2$ nên điện trở tương đương của mạch ngoài là $R_{\text{N}} = \dfrac{R_1 R_2}{R_1 + R_2} = \dfrac{6 \cdot 12}{6 + 12} = \mathbf{4\,\Omega}$. Áp dụng định luật Ohm cho toàn mạch: $I = \dfrac{\mathcal{E}}{R_{\text{N}} + r} = \dfrac{12}{4 + 1} = \mathbf{2,4\text{ A}}$." "\n"
            r"- **(b) Hiệu điện thế mạch ngoài và dòng điện nhánh**: Hiệu điện thế giữa hai cực của nguồn là $U_{\text{N}} = \mathcal{E} - Ir = 12 - 2,4 \cdot 1 = \mathbf{9,6\text{ V}}$ (hoặc $U_{\text{N}} = IR_{\text{N}} = 2,4 \cdot 4 = 9,6\text{ V}$). Cường độ dòng điện qua từng điện trở là $I_1 = \dfrac{U_{\text{N}}}{R_1} = \dfrac{9,6}{6} = \mathbf{1,6\text{ A}}$ và $I_2 = \dfrac{U_{\text{N}}}{R_2} = \dfrac{9,6}{12} = \mathbf{0,8\text{ A}}$." "\n"
            r"- **(c) Công suất và hiệu suất của nguồn**: Công suất của nguồn điện là $\mathcal{P}_{\text{ng}} = \mathcal{E}I = 12 \cdot 2,4 = \mathbf{28,8\text{ W}}$. Công suất tiêu thụ ở mạch ngoài là $\mathcal{P}_{\text{N}} = U_{\text{N}}I = 9,6 \cdot 2,4 = \mathbf{23,04\text{ W}}$. Hiệu suất của nguồn điện là $H = \dfrac{U_{\text{N}}}{\mathcal{E}} = \dfrac{9,6}{12} = 0,8 = \mathbf{80\%}$."
        ),
        "real_life": (
            r"- **Cảm biến nhiệt độ dùng điện trở nhiệt (Thermistor)**: Các nhiệt kế điện tử, mạch ngắt nhiệt chống quá tải của pin điện thoại và hệ thống điều hoà nhiệt độ ô tô sử dụng thermistor $\text{NTC}$ hoặc $\text{PTC}$ để biến sự thay đổi nhiệt độ thành tín hiệu điện áp." "\n"
            r"- **Kiểm tra tình trạng ắc quy ô tô và tính toán hoá đơn tiền điện**: Khi ắc quy cũ đi, điện trở trong $r$ tăng cao làm điện áp hai cực $U = \mathcal{E} - Ir$ sụt mạnh khi đề nổ máy (dòng $I$ lớn). Trong gia đình, công tơ điện đo tổng năng lượng điện tiêu thụ theo đơn vị $\text{kWh}$ ($1\text{ kWh} = 3,6 \cdot 10^6\text{ J}$)."
        ),
        "game_title": "Phòng thí nghiệm Mạch điện Một chiều: Định luật Ohm và Đo Pin điện hoá",
        "game_description": "Lắp ráp mạch điện với nguồn điện, biến trở, vôn kế và ampe kế để khảo sát đường đặc trưng vôn – ampe, kiểm chứng định luật Ohm và đo suất điện động, điện trở trong của pin.",
        "game_type": "game_dong_dien",
        "quiz": [
            mcq(
                "biet",
                r"Biểu thức liên hệ giữa cường độ dòng điện $I$ chạy trong dây dẫn kim loại hình trụ với tiết diện thẳng $S$, mật độ electron tự do $n$, độ lớn điện tích electron $e$ và tốc độ dịch chuyển có hướng $v$ của electron là:",
                [
                    r"$I = \dfrac{Snv}{e}$",
                    r"$I = Snve$",
                    r"$I = \dfrac{Sne}{v}$",
                    r"$I = \dfrac{nve}{S}$",
                ],
                1,
                r"Cường độ dòng điện chạy qua dây dẫn liên hệ với tốc độ dịch chuyển có hướng $v$ của các hạt mang điện theo công thức **$I = Snve$**.",
            ),
            mcq(
                "biet",
                r"Theo định luật Ohm cho vật dẫn kim loại ở nhiệt độ xác định, cường độ dòng điện $I$ chạy qua vật dẫn:",
                [
                    r"Tỉ lệ thuận với hiệu điện thế $U$ đặt vào hai đầu vật dẫn và tỉ lệ nghịch với điện trở $R$ của vật dẫn",
                    r"Tỉ lệ nghịch với hiệu điện thế $U$ đặt vào hai đầu vật dẫn và tỉ lệ thuận với điện trở $R$ của vật dẫn",
                    r"Tỉ lệ thuận với cả hiệu điện thế $U$ và điện trở $R$ của vật dẫn",
                    r"Không phụ thuộc vào hiệu điện thế $U$ giữa hai đầu vật dẫn",
                ],
                0,
                r"Theo định luật Ohm $I = \dfrac{U}{R}$, ở nhiệt độ không đổi, cường độ dòng điện $I$ **tỉ lệ thuận với hiệu điện thế $U$ và tỉ lệ nghịch với điện trở $R$**.",
            ),
            mcq(
                "biet",
                r"Một nguồn điện có suất điện động $\mathcal{E}$ và điện trở trong $r$ phát dòng điện có cường độ $I$ ra mạch ngoài. Hiệu điện thế $U$ giữa hai cực của nguồn điện được xác định bằng biểu thức:",
                [
                    r"$U = \mathcal{E} + Ir$",
                    r"$U = \mathcal{E} - Ir$",
                    r"$U = I\cdot r - \mathcal{E}$",
                    r"$U = \dfrac{\mathcal{E}}{r}$",
                ],
                1,
                r"Hiệu điện thế giữa hai cực của nguồn điện bằng suất điện động trừ đi độ giảm thế trên điện trở trong của nguồn: **$U = \mathcal{E} - Ir$**.",
            ),
            mcq(
                "biet",
                r"Công suất tiêu thụ năng lượng điện $\mathcal{P}$ của một đoạn mạch có hiệu điện thế $U$ giữa hai đầu và dòng điện không đổi cường độ $I$ chạy qua được tính bằng công thức:",
                [
                    r"$\mathcal{P} = \dfrac{U}{I}$",
                    r"$\mathcal{P} = UI$",
                    r"$\mathcal{P} = UIt^2$",
                    r"$\mathcal{P} = \dfrac{I}{U}$",
                ],
                1,
                r"Công suất tiêu thụ năng lượng điện của một đoạn mạch bằng tích của hiệu điện thế giữa hai đầu đoạn mạch và cường độ dòng điện chạy qua nó: **$\mathcal{P} = UI$**.",
            ),
            mcq(
                "hieu",
                r"Trong khoảng thời gian $\Delta t = 4\text{ s}$, có một điện lượng $\Delta q = 10\text{ C}$ dịch chuyển qua tiết diện thẳng của một dây dẫn kim loại. Cường độ dòng điện không đổi chạy qua dây dẫn và số electron dịch chuyển qua tiết diện thẳng đó trong $1\text{ s}$ lần lượt là (biết $e = 1,6 \cdot 10^{-19}\text{ C}$):",
                [
                    r"$I = 2,5\text{ A}; \ N_1 = 1,5625 \cdot 10^{19}\text{ hạt}$",
                    r"$I = 2,5\text{ A}; \ N_1 = 6,25 \cdot 10^{19}\text{ hạt}$",
                    r"$I = 0,4\text{ A}; \ N_1 = 2,5 \cdot 10^{18}\text{ hạt}$",
                    r"$I = 40\text{ A}; \ N_1 = 1,5625 \cdot 10^{19}\text{ hạt}$",
                ],
                0,
                r"Cường độ dòng điện là $I = \dfrac{\Delta q}{\Delta t} = \dfrac{10}{4} = \mathbf{2,5\text{ A}}$. Trong $t_1 = 1\text{ s}$, điện lượng qua tiết diện là $q_1 = It_1 = 2,5\text{ C}$, nên số electron đi qua là $N_1 = \dfrac{q_1}{e} = \dfrac{2,5}{1,6 \cdot 10^{-19}} = \mathbf{1,5625 \cdot 10^{19}\text{ hạt}}$.",
            ),
            mcq(
                "hieu",
                r"Một bàn là điện có ghi thông số định mức $220\text{ V} - 1\,100\text{ W}$ được sử dụng đúng với hiệu điện thế định mức $U = 220\text{ V}$. Cường độ dòng điện chạy qua bàn là và điện trở của bàn là khi hoạt động bình thường lần lượt là:",
                [
                    r"$I = 5\text{ A}, \ R = 44\,\Omega$",
                    r"$I = 5\text{ A}, \ R = 22\,\Omega$",
                    r"$I = 0,2\text{ A}, \ R = 44\,\Omega$",
                    r"$I = 10\text{ A}, \ R = 22\,\Omega$",
                ],
                0,
                r"Khi hoạt động bình thường ở $U = 220\text{ V}$, cường độ dòng điện là $I = \dfrac{\mathcal{P}}{U} = \dfrac{1\,100}{220} = \mathbf{5\text{ A}}$ và điện trở của bàn là là $R = \dfrac{U}{I} = \dfrac{220}{5} = \mathbf{44\,\Omega}$.",
            ),
            tf4(
                "hieu",
                r"Khi khảo sát tính chất dẫn điện, đường đặc trưng vôn – ampe ($I - U$) của dây dẫn kim loại, bóng đèn sợi đốt và điện trở nhiệt (thermistor), mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Nguyên nhân chính gây ra điện trở của kim loại là sự cản trở của các ion dương ở nút mạng tinh thể đối với chuyển động có hướng của các electron tự do.",
                    r"b) Đường đặc trưng $I - U$ của một vật dẫn kim loại được giữ ở nhiệt độ không đổi là một đường thẳng đi qua gốc toạ độ.",
                    r"c) Khi hiệu điện thế đặt vào bóng đèn sợi đốt tăng cao làm dây tóc nóng sáng thì điện trở của dây tóc giảm đi.",
                    r"d) Điện trở nhiệt loại $\text{NTC}$ có giá trị điện trở giảm xuống khi nhiệt độ của nó tăng lên.",
                ],
                [True, True, False, True],
                r"a) Sự va chạm của các electron tự do với các ion dương dao động nhiệt quanh nút mạng tinh thể là nguyên nhân chính gây ra điện trở của kim loại → **Đúng**." "\n"
                r"b) Khi nhiệt độ không đổi, $R = \text{hằng số}$ nên $I = \dfrac{1}{R}U$ có đồ thị là đường thẳng qua gốc toạ độ → **Đúng**." "\n"
                r"c) Khi dây tóc đèn sợi đốt nóng lên, nhiệt độ tăng làm dao động nhiệt của ion mạng tinh thể mạnh lên nên điện trở của dây tóc tăng lên, không phải giảm đi → **Sai**." "\n"
                r"d) Thermistor hệ số nhiệt âm ($\text{NTC}$) có mật độ hạt tải tăng mạnh khi nhiệt độ tăng nên điện trở giảm khi nhiệt độ tăng → **Đúng**.",
            ),
            tf4(
                "hieu",
                r"Trong bài thực hành đo suất điện động $\mathcal{E}$ và điện trở trong $r$ của một pin điện hoá, học sinh điều chỉnh biến trở mạch ngoài và ghi được hai cặp số liệu: khi cường độ dòng điện là $I_1 = 0,2\text{ A}$ thì số chỉ vôn kế ở hai cực pin là $U_1 = 1,4\text{ V}$; khi cường độ dòng điện là $I_2 = 0,6\text{ A}$ thì số chỉ vôn kế là $U_2 = 1,2\text{ V}$. Mỗi nhận định sau đây là đúng hay sai?",
                [
                    r"a) Điện trở trong của pin điện hoá đo được trong thí nghiệm là $r = 0,5\,\Omega$.",
                    r"b) Suất điện động của pin điện hoá là $\mathcal{E} = 1,5\text{ V}$.",
                    r"c) Đồ thị biểu diễn sự phụ thuộc của hiệu điện thế $U$ vào cường độ dòng điện $I$ là một đoạn thẳng có hệ số góc dương.",
                    r"d) Nếu xảy ra đoản mạch ở hai cực của pin ($R_{\text{N}} = 0$) thì cường độ dòng điện đoản mạch qua pin là $I_{\text{đm}} = 3\text{ A}$.",
                ],
                [True, True, False, True],
                r"a) Từ $U = \mathcal{E} - Ir$, ta có $r = \dfrac{U_1 - U_2}{I_2 - I_1} = \dfrac{1,4 - 1,2}{0,6 - 0,2} = \dfrac{0,2}{0,4} = 0,5\,\Omega$ → **Đúng**." "\n"
                r"b) Thay $r = 0,5\,\Omega$ vào phương trình thứ nhất: $\mathcal{E} = U_1 + I_1 r = 1,4 + 0,2 \cdot 0,5 = 1,5\text{ V}$ → **Đúng**." "\n"
                r"c) Vì $U = \mathcal{E} - rI$ với $r > 0$ nên khi $I$ tăng thì $U$ giảm; đồ thị $U(I)$ là đoạn thẳng đi xuống (hệ số góc âm bằng $-r$) → **Sai**." "\n"
                r"d) Khi đoản mạch ($R_{\text{N}} = 0$), dòng điện cực đại là $I_{\text{đm}} = \dfrac{\mathcal{E}}{r} = \dfrac{1,5}{0,5} = 3\text{ A}$ → **Đúng**.",
            ),
            mcq(
                "vandung",
                r"Một dây dẫn bằng đồng có tiết diện thẳng $S = 1\text{ mm}^2$ mang dòng điện không đổi có cường độ $I = 1,6\text{ A}$. Biết mật độ electron tự do trong đồng là $n = 8 \cdot 10^{28}\text{ m}^{-3}$ và độ lớn điện tích của electron là $e = 1,6 \cdot 10^{-19}\text{ C}$. Tốc độ dịch chuyển có hướng $v$ của các electron tự do trong dây dẫn đó bằng:",
                [
                    r"$0,125\text{ mm/s}$",
                    r"$1,25\text{ mm/s}$",
                    r"$0,25\text{ mm/s}$",
                    r"$12,5\text{ mm/s}$",
                ],
                0,
                r"Đổi $S = 1\text{ mm}^2 = 10^{-6}\text{ m}^2$. Từ công thức $I = Snve$, ta suy ra tốc độ dịch chuyển có hướng của các electron là: "
                r"$v = \dfrac{I}{Sne} = \dfrac{1,6}{10^{-6} \cdot 8 \cdot 10^{28} \cdot 1,6 \cdot 10^{-19}} = \dfrac{1}{8\,000}\text{ m/s} = 1,25 \cdot 10^{-4}\text{ m/s} = \mathbf{0,125\text{ mm/s}}$.",
            ),
            short(
                "vandung",
                r"Một nguồn điện có suất điện động $\mathcal{E} = 9\text{ V}$ và điện trở trong $r = 1\,\Omega$ được mắc với một điện trở mạch ngoài $R = 8\,\Omega$ tạo thành mạch kín. Trong thời gian $t = 5\text{ phút}$, nhiệt lượng toả ra trên điện trở mạch ngoài $R$ bằng bao nhiêu $\text{J}$?",
                ["2400"],
                r"Đổi $t = 5\text{ phút} = 300\text{ s}$. Cường độ dòng điện chạy trong mạch kín là $I = \dfrac{\mathcal{E}}{R + r} = \dfrac{9}{8 + 1} = 1\text{ A}$. "
                r"Nhiệt lượng toả ra trên điện trở mạch ngoài $R$ trong thời gian $t = 300\text{ s}$ là $Q = I^2 Rt = 1^2 \cdot 8 \cdot 300 = \mathbf{2\,400\text{ J}}$.",
                unit=r"$\text{J}$",
            ),
        ],
    },
]
