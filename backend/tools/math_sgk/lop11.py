# -*- coding: utf-8 -*-
"""Dữ liệu bài học và câu hỏi trắc nghiệm Toán 11 - Kết nối tri thức với cuộc sống (GDPT 2018)."""

from ._helpers import F, G, mcq, short, tf4

GRADE = 11

LESSONS = [
    # =========================================================================
    # CHƯƠNG I. HÀM SỐ LƯỢNG GIÁC VÀ PHƯƠNG TRÌNH LƯỢNG GIÁC
    # =========================================================================
    {
        "topic": "l11-ch01-ham-so-luong-giac-va-phuong-trinh-luong-giac",
        "title": "Chương I. Hàm số lượng giác và phương trình lượng giác",
        "icon": "📐",
        "description": (
            "Tìm hiểu góc lượng giác, đơn vị rađian, đường tròn lượng giác, các công thức "
            "biến đổi lượng giác, tính chất và đồ thị hàm số lượng giác cùng cách giải "
            "các phương trình lượng giác cơ bản."
        ),
        "requirements": [
            "Nhận biết được các khái niệm cơ bản về góc lượng giác: khái niệm góc lượng giác, số đo của góc lượng giác, hệ thức Chasles cho các góc lượng giác, đường tròn lượng giác.",
            "Nhận biết được khái niệm giá trị lượng giác của một góc lượng giác.",
            "Mô tả được bảng giá trị lượng giác của một số góc lượng giác thường gặp; hệ thức cơ bản giữa các giá trị lượng giác của một góc lượng giác; quan hệ giữa các giá trị lượng giác của các góc lượng giác có liên quan đặc biệt: bù nhau, phụ nhau, đối nhau, hơn kém nhau $\\pi$.",
            "Sử dụng được máy tính cầm tay để tính giá trị lượng giác của một góc lượng giác khi biết số đo của góc đó.",
            "Mô tả được các phép biến đổi lượng giác cơ bản: công thức cộng, công thức góc nhân đôi, công thức biến đổi tích thành tổng và công thức biến đổi tổng thành tích.",
            "Nhận biết được các khái niệm về hàm số chẵn, hàm số lẻ, hàm số tuần hoàn và các đặc trưng hình học của đồ thị các hàm số đó.",
            "Nhận biết được định nghĩa các hàm số lượng giác $y = \\sin x$, $y = \\cos x$, $y = \\tan x$, $y = \\cot x$ thông qua đường tròn lượng giác; mô tả được bảng giá trị và vẽ được đồ thị của chúng.",
            "Giải thích được tập xác định, tập giá trị, tính chất chẵn lẻ, tính tuần hoàn, chu kì, khoảng đồng biến và nghịch biến của các hàm số $y = \\sin x$, $y = \\cos x$, $y = \\tan x$, $y = \\cot x$ dựa vào đồ thị.",
            "Nhận biết được công thức nghiệm của phương trình lượng giác cơ bản $\\sin x = m$, $\\cos x = m$, $\\tan x = m$, $\\cot x = m$ và giải được phương trình lượng giác ở dạng vận dụng trực tiếp.",
            "Giải quyết được một số vấn đề thực tiễn gắn với giá trị lượng giác, hàm số lượng giác và phương trình lượng giác (như bài toán dao động điều hòa trong Vật lí).",
        ],
        "definition": (
            "Chương học mở rộng khái niệm góc hình học sang góc lượng giác có hướng trên đường tròn lượng giác, "
            "xây dựng hệ thống công thức lượng giác, khảo sát bốn hàm số tuần hoàn $y = \\sin x$, $y = \\cos x$, "
            "$y = \\tan x$, $y = \\cot x$ và thiết lập công thức nghiệm cho các phương trình lượng giác cơ bản."
        ),
        "theory": (
            "### Bài 1. Giá trị lượng giác của góc lượng giác\n"
            "- **Góc lượng giác và số đo:** Cho hai tia $Ou$, $Ov$. Góc lượng giác tia đầu $Ou$, tia cuối $Ov$ kí hiệu là $(Ou, Ov)$. "
            "Số đo của các góc lượng giác có cùng tia đầu $Ou$ và tia cuối $Ov$ sai khác nhau một bội nguyên của $360^\\circ$ (hay $2\\pi$ rad):\n"
            "  $$\\text{sđ}(Ou, Ov) = \\alpha^\\circ + k360^\\circ \\quad \\text{hoặc} \\quad \\text{sđ}(Ou, Ov) = \\alpha + k2\\pi \\quad (k \\in \\mathbb{Z})$$\n"
            "- **Đơn vị rađian và độ dài cung tròn:** Cung tròn có độ dài bằng bán kính $R$ thì chắn góc ở tâm có số đo $1\\text{ rad}$. "
            "Quan hệ giữa độ và rađian: $180^\\circ = \\pi\\text{ rad}$. Cung có số đo $\\alpha\\text{ rad}$ trên đường tròn bán kính $R$ có độ dài $l = R\\alpha$.\n"
            "- **Hệ thức Chasles:** Với ba tia $Ou$, $Ov$, $Ow$ bất kì, ta có:\n"
            "  $$(Ou, Ov) + (Ov, Ow) = (Ou, Ow) + k2\\pi \\quad (k \\in \\mathbb{Z})$$\n"
            "- **Đường tròn lượng giác và giá trị lượng giác:** Đường tròn lượng giác là đường tròn tâm $O(0; 0)$ bán kính $R = 1$ trong mặt phẳng $Oxy$, "
            "điểm gốc $A(1; 0)$, chiều dương ngược chiều kim đồng hồ. Điểm $M(x_0; y_0)$ biểu diễn góc lượng giác $\\alpha$ có:\n"
            "  $$\\sin\\alpha = y_0, \\quad \\cos\\alpha = x_0, \\quad \\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} \\ (\\cos\\alpha \\neq 0), \\quad \\cot\\alpha = \\dfrac{\\cos\\alpha}{\\sin\\alpha} \\ (\\sin\\alpha \\neq 0)$$\n"
            "- **Góc liên quan đặc biệt:** Hai góc đối nhau ($\\alpha$ và $-\\alpha$: *cos đối*), bù nhau ($\\alpha$ và $\\pi - \\alpha$: *sin bù*), "
            "phụ nhau ($\\alpha$ và $\\dfrac{\\pi}{2} - \\alpha$: *phụ chéo*), hơn kém $\\pi$ ($\\alpha$ và $\\alpha + \\pi$: *khác pi tan, cot*).\n\n"
            "### Bài 2. Công thức lượng giác\n"
            "- **Công thức cộng:** Biểu diễn giá trị lượng giác của tổng hoặc hiệu hai góc $\\alpha \\pm \\beta$ qua các giá trị lượng giác của $\\alpha$ và $\\beta$.\n"
            "- **Công thức nhân đôi và hạ bậc:** Cho $\\beta = \\alpha$ trong công thức cộng, ta thu được công thức tính $\\sin 2\\alpha$, $\\cos 2\\alpha$, $\\tan 2\\alpha$ và công thức hạ bậc cho $\\sin^2\\alpha$, $\\cos^2\\alpha$.\n"
            "- **Công thức biến đổi tích thành tổng và tổng thành tích:** Giúp chuyển đổi giữa tổng hoặc hiệu các hàm lượng giác và tích của chúng để rút gọn biểu thức hoặc giải phương trình.\n\n"
            "### Bài 3. Hàm số lượng giác\n"
            "- **Hàm số chẵn, hàm số lẻ, hàm số tuần hoàn:** Hàm số $y = f(x)$ có tập xác định $D$ đối xứng là hàm số chẵn nếu $f(-x) = f(x)$ (đồ thị đối xứng qua trục $Oy$), "
            "là hàm số lẻ nếu $f(-x) = -f(x)$ (đồ thị đối xứng qua gốc $O$). Hàm số tuần hoàn với chu kì $T > 0$ nhỏ nhất thỏa mãn $f(x + T) = f(x), \\forall x \\in D$.\n"
            "- **Bốn hàm số lượng giác cơ bản:**\n"
            "  - $y = \\sin x$: Tập xác định $D = \\mathbb{R}$, tập giá trị $[-1; 1]$, là hàm số lẻ, tuần hoàn với chu kì $T = 2\\pi$. Đồng biến trên $\\left(-\\dfrac{\\pi}{2} + k2\\pi; \\dfrac{\\pi}{2} + k2\\pi\\right)$ và nghịch biến trên $\\left(\\dfrac{\\pi}{2} + k2\\pi; \\dfrac{3\\pi}{2} + k2\\pi\\right)$.\n"
            "  - $y = \\cos x$: Tập xác định $D = \\mathbb{R}$, tập giá trị $[-1; 1]$, là hàm số chẵn, tuần hoàn với chu kì $T = 2\\pi$. Đồng biến trên $(-\\pi + k2\\pi; k2\\pi)$ và nghịch biến trên $(k2\\pi; \\pi + k2\\pi)$.\n"
            "  - $y = \\tan x$: Tập xác định $D = \\mathbb{R} \\setminus \\left\\{\\dfrac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z}\\right\\}$, tập giá trị $\\mathbb{R}$, là hàm số lẻ, tuần hoàn với chu kì $T = \\pi$, đồng biến trên mỗi khoảng $\\left(-\\dfrac{\\pi}{2} + k\\pi; \\dfrac{\\pi}{2} + k\\pi\\right)$.\n"
            "  - $y = \\cot x$: Tập xác định $D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$, tập giá trị $\\mathbb{R}$, là hàm số lẻ, tuần hoàn với chu kì $T = \\pi$, nghịch biến trên mỗi khoảng $(k\\pi; \\pi + k\\pi)$.\n\n"
            "### Bài 4. Phương trình lượng giác cơ bản\n"
            "- **Phương trình $\\sin x = m$ và $\\cos x = m$:** Có nghiệm khi và chỉ khi $|m| \\le 1$. Khi đó tồn tại góc $\\alpha$ để đưa về dạng $\\sin u = \\sin\\alpha$ hoặc $\\cos u = \\cos\\alpha$.\n"
            "- **Phương trình $\\tan x = m$ và $\\cot x = m$:** Luôn có nghiệm với mọi $m \\in \\mathbb{R}$, họ nghiệm có đuôi $+ k\\pi \\ (k \\in \\mathbb{Z})$."
        ),
        "formulas": [
            G(
                "Đổi đơn vị và hệ thức lượng giác cơ bản",
                F("Đổi độ và rađian", "$\\alpha^\\circ = \\dfrac{\\pi \\alpha}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$"),
                F("Độ dài cung tròn", "$l = R\\alpha \\quad (\\alpha \\text{ tính bằng rad})$"),
                F("Hệ thức cơ bản", "$\\sin^2\\alpha + \\cos^2\\alpha = 1, \\quad 1 + \\tan^2\\alpha = \\dfrac{1}{\\cos^2\\alpha}, \\quad 1 + \\cot^2\\alpha = \\dfrac{1}{\\sin^2\\alpha}, \\quad \\tan\\alpha \\cdot \\cot\\alpha = 1$"),
            ),
            G(
                "Công thức cộng và công thức nhân đôi",
                F("Công thức cộng cos", "$\\cos(a \\mp b) = \\cos a\\cos b \\pm \\sin a\\sin b$"),
                F("Công thức cộng sin", "$\\sin(a \\pm b) = \\sin a\\cos b \\pm \\cos a\\sin b$"),
                F("Công thức cộng tan", "$\\tan(a \\pm b) = \\dfrac{\\tan a \\pm \\tan b}{1 \\mp \\tan a\\tan b}$"),
                F("Công thức nhân đôi", "$\\sin 2a = 2\\sin a\\cos a, \\quad \\cos 2a = \\cos^2 a - \\sin^2 a = 2\\cos^2 a - 1 = 1 - 2\\sin^2 a, \\quad \\tan 2a = \\dfrac{2\\tan a}{1 - \\tan^2 a}$"),
                F("Công thức hạ bậc", "$\\sin^2 a = \\dfrac{1 - \\cos 2a}{2}, \\quad \\cos^2 a = \\dfrac{1 + \\cos 2a}{2}$"),
            ),
            G(
                "Công thức biến đổi tổng và tích",
                F("Tích thành tổng", "$\\cos a\\cos b = \\dfrac{1}{2}[\\cos(a - b) + \\cos(a + b)], \\quad \\sin a\\sin b = \\dfrac{1}{2}[\\cos(a - b) - \\cos(a + b)], \\quad \\sin a\\cos b = \\dfrac{1}{2}[\\sin(a - b) + \\sin(a + b)]$"),
                F("Tổng thành tích cos", "$\\cos u + \\cos v = 2\\cos\\dfrac{u + v}{2}\\cos\\dfrac{u - v}{2}, \\quad \\cos u - \\cos v = -2\\sin\\dfrac{u + v}{2}\\sin\\dfrac{u - v}{2}$"),
                F("Tổng thành tích sin", "$\\sin u + \\sin v = 2\\sin\\dfrac{u + v}{2}\\cos\\dfrac{u - v}{2}, \\quad \\sin u - \\sin v = 2\\cos\\dfrac{u + v}{2}\\sin\\dfrac{u - v}{2}$"),
            ),
            G(
                "Phương trình lượng giác cơ bản",
                F("Phương trình sin", "$\\sin u = \\sin\\alpha \\Leftrightarrow u = \\alpha + k2\\pi \\text{ hoặc } u = \\pi - \\alpha + k2\\pi \\quad (k \\in \\mathbb{Z})$"),
                F("Phương trình cos", "$\\cos u = \\cos\\alpha \\Leftrightarrow u = \\alpha + k2\\pi \\text{ hoặc } u = -\\alpha + k2\\pi \\quad (k \\in \\mathbb{Z})$"),
                F("Phương trình tan và cot", "$\\tan u = \\tan\\alpha \\Leftrightarrow u = \\alpha + k\\pi; \\quad \\cot u = \\cot\\alpha \\Leftrightarrow u = \\alpha + k\\pi \\quad (k \\in \\mathbb{Z})$"),
            ),
        ],
        "example": (
            "Cho góc lượng giác $\\alpha$ thỏa mãn $\\sin\\alpha = \\dfrac{3}{5}$ và $\\dfrac{\\pi}{2} < \\alpha < \\pi$. "
            "Hãy tính giá trị của $\\cos\\alpha$, $\\sin 2\\alpha$, $\\cos 2\\alpha$ và giải phương trình $\\cos\\left(2x - \\dfrac{\\pi}{3}\\right) = \\dfrac{1}{2}$."
        ),
        "example_answer": (
            "**Bước 1: Tính $\\cos\\alpha$, $\\sin 2\\alpha$, $\\cos 2\\alpha$**\n"
            "- Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos\\alpha < 0$. Áp dụng hệ thức $\\sin^2\\alpha + \\cos^2\\alpha = 1$, ta có:\n"
            "  $$\\cos\\alpha = -\\sqrt{1 - \\sin^2\\alpha} = -\\sqrt{1 - \\left(\\dfrac{3}{5}\\right)^2} = -\\sqrt{\\dfrac{16}{25}} = -\\dfrac{4}{5}$$\n"
            "- Áp dụng công thức nhân đôi:\n"
            "  $$\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2 \\cdot \\dfrac{3}{5} \\cdot \\left(-\\dfrac{4}{5}\\right) = -\\dfrac{24}{25}$$\n"
            "  $$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha = 1 - 2 \\cdot \\dfrac{9}{25} = \\dfrac{7}{25}$$\n\n"
            "**Bước 2: Giải phương trình $\\cos\\left(2x - \\dfrac{\\pi}{3}\\right) = \\dfrac{1}{2}$**\n"
            "- Ta có $\\dfrac{1}{2} = \\cos\\dfrac{\\pi}{3}$, nên phương trình tương đương với:\n"
            "  $$\\cos\\left(2x - \\dfrac{\\pi}{3}\\right) = \\cos\\dfrac{\\pi}{3} \\Leftrightarrow \\left[\\begin{aligned} &2x - \\dfrac{\\pi}{3} = \\dfrac{\\pi}{3} + k2\\pi \\\\ &2x - \\dfrac{\\pi}{3} = -\\dfrac{\\pi}{3} + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} &x = \\dfrac{\\pi}{3} + k\\pi \\\\ &x = k\\pi \\end{aligned}\\right. \\quad (k \\in \\mathbb{Z})$$"
        ),
        "real_life": (
            "Hàm số lượng giác là công cụ toán học cốt lõi để mô hình hóa các hiện tượng tuần hoàn trong tự nhiên và kĩ thuật: "
            "dao động của con lắc, dòng điện xoay chiều $i = I_0\\cos(\\omega t + \\varphi)$, sóng âm thanh, sóng điện từ, "
            "thủy triều lên xuống và sự biến thiên độ cao của cabin trên vòng quay Mặt Trời."
        ),
        "quiz": [
            mcq(
                "biet",
                "Góc có số đo $120^\\circ$ đổi sang đơn vị rađian bằng bao nhiêu?",
                ["$\\dfrac{2\\pi}{3}$", "$\\dfrac{\\pi}{3}$", "$\\dfrac{3\\pi}{2}$", "$\\dfrac{5\\pi}{6}$"],
                0,
                "Ta có $\\alpha = 120 \\cdot \\dfrac{\\pi}{180} = \\dfrac{2\\pi}{3}\\text{ rad}$.",
            ),
            mcq(
                "biet",
                "Trong các công thức lượng giác sau, công thức nào đúng?",
                [
                    "$\\cos(a - b) = \\cos a\\cos b + \\sin a\\sin b$",
                    "$\\cos(a - b) = \\cos a\\cos b - \\sin a\\sin b$",
                    "$\\sin(a + b) = \\sin a\\cos b - \\cos a\\sin b$",
                    "$\\cos 2a = 2\\sin a\\cos a$",
                ],
                0,
                "Theo công thức cộng đối với côsin, ta có $\\cos(a - b) = \\cos a\\cos b + \\sin a\\sin b$.",
            ),
            mcq(
                "biet",
                "Tập xác định của hàm số $y = \\tan x$ là:",
                [
                    "$D = \\mathbb{R} \\setminus \\left\\{\\dfrac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z}\\right\\}$",
                    "$D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$",
                    "$D = \\mathbb{R} \\setminus \\left\\{\\dfrac{\\pi}{2} + k2\\pi \\mid k \\in \\mathbb{Z}\\right\\}$",
                    "$D = \\mathbb{R}$",
                ],
                0,
                "Hàm số $y = \\tan x = \\dfrac{\\sin x}{\\cos x}$ xác định khi $\\cos x \\neq 0 \\Leftrightarrow x \\neq \\dfrac{\\pi}{2} + k\\pi \\ (k \\in \\mathbb{Z})$.",
            ),
            mcq(
                "biet",
                "Nghiệm của phương trình lượng giác cơ bản $\\cos x = 1$ là:",
                [
                    "$x = k2\\pi \\ (k \\in \\mathbb{Z})$",
                    "$x = k\\pi \\ (k \\in \\mathbb{Z})$",
                    "$x = \\dfrac{\\pi}{2} + k2\\pi \\ (k \\in \\mathbb{Z})$",
                    "$x = \\pi + k2\\pi \\ (k \\in \\mathbb{Z})$",
                ],
                0,
                "Trên đường tròn lượng giác, $\\cos x = 1$ tại điểm gốc $A(1; 0)$ ứng với $x = k2\\pi \\ (k \\in \\mathbb{Z})$.",
            ),
            mcq(
                "hieu",
                "Cho góc lượng giác $\\alpha$ thỏa mãn $\\cos\\alpha = -\\dfrac{3}{5}$ và $\\dfrac{\\pi}{2} < \\alpha < \\pi$. Giá trị của $\\sin 2\\alpha$ bằng:",
                [
                    "$-\\dfrac{24}{25}$",
                    "$\\dfrac{24}{25}$",
                    "$-\\dfrac{7}{25}$",
                    "$\\dfrac{12}{25}$",
                ],
                0,
                "Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\sin\\alpha > 0 \\Rightarrow \\sin\\alpha = \\sqrt{1 - \\cos^2\\alpha} = \\sqrt{1 - \\dfrac{9}{25}} = \\dfrac{4}{5}$. Do đó $\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2 \\cdot \\dfrac{4}{5} \\cdot \\left(-\\dfrac{3}{5}\\right) = -\\dfrac{24}{25}$.",
            ),
            mcq(
                "hieu",
                "Tập giá trị $T$ của hàm số $y = 3\\sin\\left(2x - \\dfrac{\\pi}{4}\\right) - 2$ là:",
                [
                    "$T = [-5; 1]$",
                    "$T = [-3; 3]$",
                    "$T = [-1; 5]$",
                    "$T = [-2; 3]$",
                ],
                0,
                "Vì $-1 \\le \\sin\\left(2x - \\dfrac{\\pi}{4}\\right) \\le 1, \\forall x \\in \\mathbb{R}$ nên $-3 \\le 3\\sin\\left(2x - \\dfrac{\\pi}{4}\\right) \\le 3 \\Rightarrow -5 \\le y \\le 1$. Vậy $T = [-5; 1]$.",
            ),
            tf4(
                "hieu",
                "Cho hàm số $f(x) = \\sin 2x$ xét trên tập số thực $\\mathbb{R}$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Tập giá trị của hàm số $f(x)$ là đoạn $[-1; 1]$.",
                    "Hàm số $f(x) = \\sin 2x$ là một hàm số chẵn trên $\\mathbb{R}$.",
                    "Hàm số $f(x) = \\sin 2x$ tuần hoàn với chu kì nhỏ nhất là $T = \\pi$.",
                    "Trên đoạn $[0; \\pi]$, phương trình $f(x) = \\dfrac{1}{2}$ có đúng $2$ nghiệm phân biệt.",
                ],
                [True, False, True, True],
                "a) Đúng vì $\\sin 2x \\in [-1; 1]$.\n"
                "b) Sai vì $f(-x) = \\sin(-2x) = -\\sin 2x = -f(x)$ nên $f(x)$ là hàm số lẻ.\n"
                "c) Đúng vì chu kì của hàm số $y = \\sin(ax + b)$ với $a > 0$ là $T = \\dfrac{2\\pi}{a} = \\dfrac{2\\pi}{2} = \\pi$.\n"
                "d) Đúng vì $\\sin 2x = \\dfrac{1}{2} \\Leftrightarrow 2x = \\dfrac{\\pi}{6} + k2\\pi$ hoặc $2x = \\dfrac{5\\pi}{6} + k2\\pi \\Leftrightarrow x = \\dfrac{\\pi}{12} + k\\pi$ hoặc $x = \\dfrac{5\\pi}{12} + k\\pi$. Với $x \\in [0; \\pi]$, có đúng $2$ nghiệm là $x = \\dfrac{\\pi}{12}$ và $x = \\dfrac{5\\pi}{12}$.",
            ),
            tf4(
                "hieu",
                "Cho góc lượng giác $\\alpha$ thỏa mãn $\\sin\\alpha = \\dfrac{4}{5}$ và $0 < \\alpha < \\dfrac{\\pi}{2}$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Giá trị của $\\cos\\alpha$ là $\\dfrac{3}{5}$.",
                    "Giá trị của $\\tan\\alpha$ là $\\dfrac{3}{4}$.",
                    "Giá trị của $\\cos 2\\alpha$ là $-\\dfrac{7}{25}$.",
                    "Giá trị của $\\sin\\left(\\alpha + \\dfrac{\\pi}{4}\\right)$ bằng $\\dfrac{7\\sqrt{2}}{10}$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $0 < \\alpha < \\dfrac{\\pi}{2} \\Rightarrow \\cos\\alpha > 0$, nên $\\cos\\alpha = \\sqrt{1 - \\left(\\dfrac{4}{5}\\right)^2} = \\dfrac{3}{5}$.\n"
                "b) Sai vì $\\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} = \\dfrac{4}{3} \\neq \\dfrac{3}{4}$.\n"
                "c) Đúng vì $\\cos 2\\alpha = 1 - 2\\sin^2\\alpha = 1 - 2 \\cdot \\dfrac{16}{25} = -\\dfrac{7}{25}$.\n"
                "d) Đúng vì $\\sin\\left(\\alpha + \\dfrac{\\pi}{4}\\right) = \\sin\\alpha\\cos\\dfrac{\\pi}{4} + \\cos\\alpha\\sin\\dfrac{\\pi}{4} = \\left(\\dfrac{4}{5} + \\dfrac{3}{5}\\right)\\dfrac{\\sqrt{2}}{2} = \\dfrac{7\\sqrt{2}}{10}$.",
            ),
            mcq(
                "vandung",
                "Huyết áp của một người thay đổi theo thời gian $t$ (tính bằng giây) được mô hình hóa bởi hàm số $p(t) = 100 + 20\\cos\\left(\\dfrac{8\\pi}{3}t\\right)$ (đơn vị: $\\text{mmHg}$). Trong khoảng thời gian $3$ giây đầu tiên, số nhịp tim (số chu kì tuần hoàn của huyết áp) của người đó là:",
                ["$4$", "$3$", "$6$", "$8$"],
                0,
                "Chu kì của hàm huyết áp $p(t)$ là $T = \\dfrac{2\\pi}{\\dfrac{8\\pi}{3}} = \\dfrac{3}{4}\\text{ (giây)}$. Trong khoảng thời gian $3$ giây, số chu kì thực hiện được là $\\dfrac{3}{T} = \\dfrac{3}{\\dfrac{3}{4}} = 4$ (nhịp).",
            ),
            short(
                "vandung",
                "Độ cao $h$ (tính bằng mét) của một cabin trên vòng quay Mặt Trời so với mặt đất sau $t$ phút kể từ khi bắt đầu quay được cho bởi công thức $h(t) = 32 - 30\\cos\\left(\\dfrac{\\pi}{6}t\\right)$. Hỏi sau bao nhiêu phút kể từ lúc khởi hành ($t > 0$) thì cabin đạt độ cao $47\\text{ m}$ lần đầu tiên?",
                ["4"],
                "Ta giải phương trình $h(t) = 47 \\Leftrightarrow 32 - 30\\cos\\left(\\dfrac{\\pi}{6}t\\right) = 47 \\Leftrightarrow \\cos\\left(\\dfrac{\\pi}{6}t\\right) = -\\dfrac{1}{2} = \\cos\\dfrac{2\\pi}{3}$.\n"
                "Suy ra $\\dfrac{\\pi}{6}t = \\pm\\dfrac{2\\pi}{3} + k2\\pi \\Leftrightarrow t = \\pm 4 + 12k \\ (k \\in \\mathbb{Z})$. Thời điểm dương nhỏ nhất là $t = 4$ (phút).",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG II. DÃY SỐ. CẤP SỐ CỘNG VÀ CẤP SỐ NHÂN
    # =========================================================================
    {
        "topic": "l11-ch02-day-so-cap-so-cong-va-cap-so-nhan",
        "title": "Chương II. Dãy số. Cấp số cộng và cấp số nhân",
        "icon": "🔢",
        "description": (
            "Khám phá khái niệm dãy số, tính tăng giảm và bị chặn của dãy số; nắm vững định nghĩa, "
            "công thức số hạng tổng quát, tính chất và tổng của n số hạng đầu tiên đối với cấp số cộng và cấp số nhân."
        ),
        "requirements": [
            "Nhận biết được dãy số hữu hạn, dãy số vô hạn.",
            "Thể hiện được cách cho dãy số bằng liệt kê các số hạng, bằng công thức tổng quát, bằng hệ thức truy hồi và bằng cách mô tả.",
            "Nhận biết được tính chất tăng, giảm, bị chặn của dãy số trong những trường hợp đơn giản.",
            "Nhận biết được một dãy số là cấp số cộng; giải thích được công thức xác định số hạng tổng quát và tính được tổng của $n$ số hạng đầu tiên của cấp số cộng.",
            "Nhận biết được một dãy số là cấp số nhân; giải thích được công thức xác định số hạng tổng quát và tính được tổng của $n$ số hạng đầu tiên của cấp số nhân.",
            "Giải quyết được một số vấn đề thực tiễn gắn với cấp số cộng và cấp số nhân (như bài toán lãi kép, tăng trưởng dân số, sinh học).",
        ],
        "definition": (
            "Dãy số là một hàm số xác định trên tập hợp các số nguyên dương $\\mathbb{N}^*$ (hoặc tập con $\\{1; 2; \\dots; m\\}$). "
            "Trong đó, cấp số cộng là dãy số có hiệu hai số hạng liên tiếp không đổi ($d$), còn cấp số nhân là dãy số có thương "
            "(tỉ số) hai số hạng liên tiếp không đổi ($q$)."
        ),
        "theory": (
            "### Bài 5. Dãy số\n"
            "- **Khái niệm dãy số:** Mỗi hàm số $u$ xác định trên $\\mathbb{N}^* = \\{1; 2; 3; \\dots\\}$ được gọi là một dãy số vô hạn, kí hiệu $(u_n)$, trong đó $u_n = u(n)$ là số hạng thứ $n$ (số hạng tổng quát) và $u_1$ là số hạng đầu.\n"
            "- **Các cách cho một dãy số:** Liệt kê các số hạng; cho công thức của số hạng tổng quát $u_n$; cho bằng hệ thức truy hồi (cho số hạng đầu và công thức tính $u_n$ theo các số hạng đứng trước); hoặc cho bằng lời mô tả.\n"
            "- **Dãy số tăng, dãy số giảm:**\n"
            "  - Dãy số $(u_n)$ là *dãy số tăng* nếu $u_{n+1} > u_n, \\forall n \\in \\mathbb{N}^*$ (tức $u_{n+1} - u_n > 0$).\n"
            "  - Dãy số $(u_n)$ là *dãy số giảm* nếu $u_{n+1} < u_n, \\forall n \\in \\mathbb{N}^*$ (tức $u_{n+1} - u_n < 0$).\n"
            "- **Dãy số bị chặn:** Dãy $(u_n)$ bị chặn trên nếu $\\exists M \\in \\mathbb{R}: u_n \\le M, \\forall n \\in \\mathbb{N}^*$; bị chặn dưới nếu $\\exists m \\in \\mathbb{R}: u_n \\ge m, \\forall n \\in \\mathbb{N}^*$; bị chặn nếu vừa bị chặn trên vừa bị chặn dưới.\n\n"
            "### Bài 6. Cấp số cộng\n"
            "- **Định nghĩa:** Cấp số cộng là một dãy số (hữu hạn hoặc vô hạn), trong đó kể từ số hạng thứ hai, mỗi số hạng đều bằng số hạng đứng ngay trước nó cộng với một số không đổi $d$ (gọi là *công sai*):\n"
            "  $$u_n = u_{n-1} + d \\quad (n \\ge 2)$$\n"
            "- **Số hạng tổng quát:** $u_n = u_1 + (n - 1)d$ với mọi $n \\ge 2$.\n"
            "- **Tính chất các số hạng:** Ba số hạng liên tiếp $u_{k-1}, u_k, u_{k+1}$ thỏa mãn $u_k = \\dfrac{u_{k-1} + u_{k+1}}{2}$ ($k \\ge 2$).\n"
            "- **Tổng $n$ số hạng đầu:** $S_n = u_1 + u_2 + \\dots + u_n = \\dfrac{n(u_1 + u_n)}{2} = \\dfrac{n[2u_1 + (n - 1)d]}{2}$.\n\n"
            "### Bài 7. Cấp số nhân\n"
            "- **Định nghĩa:** Cấp số nhân là một dãy số (hữu hạn hoặc vô hạn), trong đó kể từ số hạng thứ hai, mỗi số hạng đều bằng số hạng đứng ngay trước nó nhân với một số không đổi $q$ (gọi là *công bội*):\n"
            "  $$u_n = u_{n-1} \\cdot q \\quad (n \\ge 2)$$\n"
            "- **Số hạng tổng quát:** $u_n = u_1 \\cdot q^{n-1}$ với mọi $n \\ge 2$.\n"
            "- **Tính chất các số hạng:** Ba số hạng liên tiếp thỏa mãn $u_k^2 = u_{k-1} \\cdot u_{k+1}$ ($k \\ge 2$).\n"
            "- **Tổng $n$ số hạng đầu:** Khi $q \\neq 1$, ta có $S_n = \\dfrac{u_1(1 - q^n)}{1 - q}$. Khi $q = 1$, $S_n = n \\cdot u_1$."
        ),
        "formulas": [
            G(
                "Dãy số tăng, giảm và bị chặn",
                F("Dãy số tăng và dãy số giảm", "$u_{n+1} - u_n > 0 \\text{ (tăng)}, \\quad u_{n+1} - u_n < 0 \\text{ (giảm)}$"),
                F("Dãy số bị chặn", "$m \\le u_n \\le M, \\quad \\forall n \\in \\mathbb{N}^*$"),
            ),
            G(
                "Cấp số cộng (Công sai d)",
                F("Định nghĩa truy hồi", "$u_n = u_{n-1} + d \\quad (n \\ge 2)$"),
                F("Số hạng tổng quát", "$u_n = u_1 + (n - 1)d \\quad (n \\ge 2)$"),
                F("Trung bình cộng", "$u_k = \\dfrac{u_{k-1} + u_{k+1}}{2} \\quad (k \\ge 2)$"),
                F("Tổng n số hạng đầu", "$S_n = \\dfrac{n(u_1 + u_n)}{2} = \\dfrac{n[2u_1 + (n - 1)d]}{2}$"),
            ),
            G(
                "Cấp số nhân (Công bội q)",
                F("Định nghĩa truy hồi", "$u_n = u_{n-1} \\cdot q \\quad (n \\ge 2)$"),
                F("Số hạng tổng quát", "$u_n = u_1 \\cdot q^{n-1} \\quad (n \\ge 2)$"),
                F("Trung bình nhân", "$u_k^2 = u_{k-1} \\cdot u_{k+1} \\quad (k \\ge 2)$"),
                F("Tổng n số hạng đầu", "$S_n = \\dfrac{u_1(1 - q^n)}{1 - q} \\quad (q \\neq 1)$"),
            ),
        ],
        "example": (
            "a) Cho cấp số cộng $(u_n)$ thỏa mãn $u_2 + u_5 = 24$ và $u_7 - u_3 = 16$. Tìm số hạng đầu $u_1$, công sai $d$ và tổng $15$ số hạng đầu tiên $S_{15}$.\n"
            "b) Cho cấp số nhân $(v_n)$ có $v_1 = 3$ và công bội $q = 2$. Tính $v_6$ và tổng $8$ số hạng đầu tiên $S_8$."
        ),
        "example_answer": (
            "**a) Giải bài toán cấp số cộng:**\n"
            "- Áp dụng công thức $u_n = u_1 + (n - 1)d$, ta chuyển hệ điều kiện về $u_1$ và $d$:\n"
            "  $$\\begin{cases} (u_1 + d) + (u_1 + 4d) = 24 \\\\ (u_1 + 6d) - (u_1 + 2d) = 16 \\end{cases} \\Leftrightarrow \\begin{cases} 2u_1 + 5d = 24 \\\\ 4d = 16 \\end{cases} \\Leftrightarrow \\begin{cases} u_1 = 2 \\\\ d = 4 \\end{cases}$$\n"
            "- Tổng $15$ số hạng đầu tiên của cấp số cộng là:\n"
            "  $$S_{15} = \\dfrac{15[2u_1 + 14d]}{2} = \\dfrac{15(2 \\cdot 2 + 14 \\cdot 4)}{2} = \\dfrac{15 \\cdot 60}{2} = 450$$\n\n"
            "**b) Giải bài toán cấp số nhân:**\n"
            "- Số hạng thứ $6$ của cấp số nhân là: $v_6 = v_1 \\cdot q^5 = 3 \\cdot 2^5 = 3 \\cdot 32 = 96$.\n"
            "- Tổng $8$ số hạng đầu tiên là:\n"
            "  $$S_8 = \\dfrac{v_1(1 - q^8)}{1 - q} = \\dfrac{3(1 - 2^8)}{1 - 2} = 3(256 - 1) = 765$$"
        ),
        "real_life": (
            "Cấp số cộng xuất hiện khi xếp ghế trong rạp hát theo từng hàng tăng đều, tính khấu hao tài sản tuyến tính hoặc xếp gạch xây tháp; "
            "cấp số nhân mô tả chính xác bài toán lãi kép ngân hàng, sự nhân đôi của vi khuẩn trong sinh học và sự phân rã phóng xạ."
        ),
        "quiz": [
            mcq(
                "biet",
                "Cho dãy số $(u_n)$ với công thức số hạng tổng quát $u_n = 2n^2 - 1$. Số hạng thứ $4$ của dãy số là:",
                ["$31$", "$15$", "$7$", "$33$"],
                0,
                "Thay $n = 4$ vào công thức $u_n = 2n^2 - 1$, ta được $u_4 = 2 \\cdot 4^2 - 1 = 31$.",
            ),
            mcq(
                "biet",
                "Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = -3$ và công sai $d = 4$. Số hạng thứ $5$ của cấp số cộng đó bằng:",
                ["$13$", "$17$", "$9$", "$15$"],
                0,
                "Áp dụng công thức $u_n = u_1 + (n - 1)d$, ta có $u_5 = u_1 + 4d = -3 + 4 \\cdot 4 = 13$.",
            ),
            mcq(
                "biet",
                "Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 2$ và công bội $q = -3$. Số hạng $u_4$ của cấp số nhân bằng:",
                ["$-54$", "$54$", "$-18$", "$162$"],
                0,
                "Ta có $u_4 = u_1 \\cdot q^3 = 2 \\cdot (-3)^3 = 2 \\cdot (-27) = -54$.",
            ),
            mcq(
                "biet",
                "Trong các dãy số cho bởi công thức số hạng tổng quát dưới đây, dãy số nào là dãy số tăng?",
                [
                    "$u_n = 3n + 1$",
                    "$u_n = -2n + 5$",
                    "$u_n = \\dfrac{1}{n}$",
                    "$u_n = (-1)^n$",
                ],
                0,
                "Với $u_n = 3n + 1$, ta có $u_{n+1} - u_n = 3(n + 1) + 1 - (3n + 1) = 3 > 0, \\forall n \\in \\mathbb{N}^*$, nên $(u_n)$ là dãy số tăng.",
            ),
            mcq(
                "hieu",
                "Cho cấp số cộng $(u_n)$ thỏa mãn $u_1 = 5$ và $u_8 = 26$. Tổng $10$ số hạng đầu tiên $S_{10}$ của cấp số cộng bằng:",
                ["$185$", "$170$", "$200$", "$155$"],
                0,
                "Ta có $u_8 = u_1 + 7d \\Rightarrow 26 = 5 + 7d \\Rightarrow d = 3$. Khi đó $S_{10} = \\dfrac{10(2u_1 + 9d)}{2} = 5(2 \\cdot 5 + 9 \\cdot 3) = 5 \\cdot 37 = 185$.",
            ),
            mcq(
                "hieu",
                "Cho cấp số nhân $(u_n)$ có các số hạng đều dương, biết $u_2 = 6$ và $u_5 = 162$. Tổng $5$ số hạng đầu tiên của cấp số nhân đó là:",
                ["$242$", "$240$", "$180$", "$726$"],
                0,
                "Ta có $\\dfrac{u_5}{u_2} = q^3 = \\dfrac{162}{6} = 27 \\Rightarrow q = 3$ và $u_1 = \\dfrac{u_2}{q} = \\dfrac{6}{3} = 2$. Tổng $5$ số hạng đầu là $S_5 = \\dfrac{u_1(1 - q^5)}{1 - q} = \\dfrac{2(1 - 3^5)}{1 - 3} = 242$.",
            ),
            tf4(
                "hieu",
                "Cho cấp số cộng $(u_n)$ có số hạng tổng quát $u_n = 4n - 1$ với mọi $n \\in \\mathbb{N}^*$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Số hạng đầu của cấp số cộng là $u_1 = 3$.",
                    "Công sai của cấp số cộng là $d = -1$.",
                    "Số $199$ là số hạng thứ $50$ của cấp số cộng.",
                    "Tổng của $20$ số hạng đầu tiên của cấp số cộng là $S_{20} = 820$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $u_1 = 4 \\cdot 1 - 1 = 3$.\n"
                "b) Sai vì $d = u_{n+1} - u_n = 4(n + 1) - 1 - (4n - 1) = 4 \\neq -1$.\n"
                "c) Đúng vì $u_{50} = 4 \\cdot 50 - 1 = 199$.\n"
                "d) Đúng vì $u_{20} = 4 \\cdot 20 - 1 = 79$, do đó $S_{20} = \\dfrac{20(u_1 + u_{20})}{2} = 10 \\cdot (3 + 79) = 820$.",
            ),
            tf4(
                "hieu",
                "Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 2$ và công bội $q = 3$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Số hạng thứ $3$ của cấp số nhân là $u_3 = 18$.",
                    "Dãy số $(u_n)$ là một dãy số giảm.",
                    "Số $486$ là số hạng thứ $6$ của cấp số nhân đã cho.",
                    "Tổng $6$ số hạng đầu tiên của cấp số nhân bằng $728$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $u_3 = u_1 \\cdot q^2 = 2 \\cdot 3^2 = 18$.\n"
                "b) Sai vì $u_1 = 2 > 0$ và $q = 3 > 1$ nên $u_{n+1} = 3u_n > u_n$, dãy số $(u_n)$ là dãy số tăng.\n"
                "c) Đúng vì $u_6 = 2 \\cdot 3^5 = 2 \\cdot 243 = 486$.\n"
                "d) Đúng vì $S_6 = \\dfrac{u_1(1 - q^6)}{1 - q} = \\dfrac{2(1 - 729)}{1 - 3} = 728$.",
            ),
            mcq(
                "vandung",
                "Một nhà hát có $20$ hàng ghế. Hàng thứ nhất có $15$ ghế, mỗi hàng kế tiếp có nhiều hơn hàng liền trước nó $3$ ghế. Tổng số ghế của nhà hát đó là:",
                ["$870$", "$840$", "$900$", "$720$"],
                0,
                "Số ghế ở mỗi hàng lập thành một cấp số cộng với $u_1 = 15$, công sai $d = 3$ và số hàng $n = 20$. Tổng số ghế là $S_{20} = \\dfrac{20(2 \\cdot 15 + 19 \\cdot 3)}{2} = 10 \\cdot (30 + 57) = 870$ (ghế).",
            ),
            short(
                "vandung",
                "Một loại vi khuẩn cứ sau mỗi $30$ phút lại phân đôi một lần. Ban đầu có $100$ con vi khuẩn. Hỏi sau $3$ giờ sẽ có tất cả bao nhiêu con vi khuẩn?",
                ["6400"],
                "Trong $3$ giờ ($180$ phút) có $\\dfrac{180}{30} = 6$ chu kì phân đôi. Số vi khuẩn sau mỗi chu kì lập thành cấp số nhân với $u_1 = 100$ và $q = 2$. Sau $6$ chu kì, số vi khuẩn là $N = 100 \\cdot 2^6 = 100 \\cdot 64 = 6400$ (con).",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG III. CÁC SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM CỦA MẪU SỐ LIỆU GHÉP NHÓM
    # =========================================================================
    {
        "topic": "l11-ch03-cac-so-dac-trung-do-xu-the-trung-tam-cua-mau-so-lieu-ghep-nhom",
        "title": "Chương III. Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm",
        "icon": "📊",
        "description": (
            "Tìm hiểu cách biểu diễn mẫu số liệu ghép nhóm bằng bảng tần số ghép nhóm "
            "và tính toán, giải thích ý nghĩa của các số đặc trưng đo xu thế trung tâm: "
            "số trung bình, trung vị, tứ phân vị và mốt."
        ),
        "requirements": [
            "Nhận biết được mẫu số liệu ghép nhóm và biết cách chuyển mẫu số liệu không ghép nhóm sang mẫu số liệu ghép nhóm.",
            "Tính được các số đặc trưng đo xu thế trung tâm cho mẫu số liệu ghép nhóm: số trung bình cộng (hay số trung bình), trung vị (median), tứ phân vị (quartiles), mốt (mode).",
            "Hiểu được ý nghĩa và vai trò của các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm trong thực tiễn.",
            "Rút ra được kết luận nhờ ý nghĩa của các số đặc trưng nói trên của mẫu số liệu trong trường hợp đơn giản.",
            "Nhận biết được mối liên hệ giữa thống kê với những kiến thức của các môn học khác trong Chương trình lớp 11 và trong thực tiễn.",
        ],
        "definition": (
            "Mẫu số liệu ghép nhóm là mẫu số liệu được phân chia thành các nhóm (thường dưới dạng các nửa khoảng $[a_i; a_{i+1})$) "
            "kèm theo tần số của mỗi nhóm. Các số đặc trưng đo xu thế trung tâm ($\\bar{x}, M_e, Q_1, Q_2, Q_3, M_o$) giúp ước lượng "
            "giá trị đại diện và phân bố của toàn bộ mẫu số liệu lớn."
        ),
        "theory": (
            "### Bài 8. Mẫu số liệu ghép nhóm\n"
            "- **Khái niệm:** Khi mẫu số liệu có kích thước lớn hoặc biến thiên liên tục (như chiều cao, cân nặng, thời gian), ta ghép các số liệu vào các nhóm có dạng $[a; b)$ (gồm các giá trị $x$ thỏa mãn $a \\le x < b$, nhóm cuối thường lấy cả đầu mút phải $[a; b]$).\n"
            "- **Độ dài và giá trị đại diện của nhóm:** Với nhóm $[a_i; a_{i+1})$, độ dài nhóm là $L = a_{i+1} - a_i$ và *giá trị đại diện* là trung điểm $c_i = \\dfrac{a_i + a_{i+1}}{2}$.\n\n"
            "### Bài 9. Các số đặc trưng đo xu thế trung tâm\n"
            "- **Số trung bình của mẫu số liệu ghép nhóm ($\\bar{x}$):** Được tính xấp xỉ bằng trung bình cộng có trọng số của các giá trị đại diện $c_i$ với tần số $m_i$ (cỡ mẫu $n = m_1 + m_2 + \\dots + m_k$).\n"
            "- **Trung vị ($M_e$):** Chia mẫu số liệu đã sắp xếp thành hai phần bằng nhau. Đầu tiên xác định nhóm thứ $p$ đầu tiên có tần số tích lũy lớn hơn hoặc bằng $\\dfrac{n}{2}$, sau đó dùng công thức nội suy trên nhóm $[u_p; u_{p+1})$.\n"
            "- **Tứ phân vị ($Q_1, Q_2, Q_3$):** Chia mẫu số liệu thành $4$ phần có số lượng số liệu bằng nhau. Trong đó $Q_2 = M_e$, còn $Q_1$ và $Q_3$ được nội suy tương tự trung vị tại các ngưỡng $\\dfrac{n}{4}$ và $\\dfrac{3n}{4}$.\n"
            "- **Mốt ($M_o$):** Đặc trưng cho giá trị xuất hiện nhiều nhất. Xác định *nhóm chứa mốt* là nhóm có tần số lớn nhất (giả sử là nhóm $j$ có độ dài chuẩn), rồi tính $M_o$ theo tần số nhóm đó và hai nhóm kề cận."
        ),
        "formulas": [
            G(
                "Giá trị đại diện và Số trung bình",
                F("Giá trị đại diện nhóm", "$c_i = \\dfrac{a_i + a_{i+1}}{2}$"),
                F("Cỡ mẫu", "$n = m_1 + m_2 + \\dots + m_k$"),
                F("Số trung bình", "$\\bar{x} = \\dfrac{m_1 c_1 + m_2 c_2 + \\dots + m_k c_k}{n}$"),
            ),
            G(
                "Trung vị và Tứ phân vị",
                F("Trung vị (nhóm p)", "$M_e = u_p + \\dfrac{\\dfrac{n}{2} - C}{m_p} \\cdot (u_{p+1} - u_p) \\quad (C = m_1 + \\dots + m_{p-1})$"),
                F("Tứ phân vị thứ nhất (nhóm p)", "$Q_1 = u_p + \\dfrac{\\dfrac{n}{4} - C}{m_p} \\cdot (u_{p+1} - u_p)$"),
                F("Tứ phân vị thứ ba (nhóm p)", "$Q_3 = u_p + \\dfrac{\\dfrac{3n}{4} - C}{m_p} \\cdot (u_{p+1} - u_p)$"),
            ),
            G(
                "Mốt của mẫu số liệu ghép nhóm",
                F("Công thức Mốt (nhóm j)", "$M_o = u_j + \\dfrac{m_j - m_{j-1}}{(m_j - m_{j-1}) + (m_j - m_{j+1})} \\cdot (u_{j+1} - u_j)$"),
            ),
        ],
        "example": (
            "Thời gian tự học mỗi ngày (đơn vị: phút) của $40$ học sinh lớp 11A được thống kê trong bảng ghép nhóm sau:\n"
            "- Nhóm $[0; 30)$: $4$ học sinh\n"
            "- Nhóm $[30; 60)$: $12$ học sinh\n"
            "- Nhóm $[60; 90)$: $16$ học sinh\n"
            "- Nhóm $[90; 120]$: $8$ học sinh\n"
            "Hãy tính số trung bình $\\bar{x}$, trung vị $M_e$ và mốt $M_o$ của mẫu số liệu ghép nhóm trên."
        ),
        "example_answer": (
            "**Bước 1: Tính số trung bình $\\bar{x}$**\n"
            "- Giá trị đại diện của $4$ nhóm lần lượt là: $c_1 = 15$, $c_2 = 45$, $c_3 = 75$, $c_4 = 105$. Cỡ mẫu $n = 4 + 12 + 16 + 8 = 40$.\n"
            "- Số trung bình của mẫu số liệu ghép nhóm là:\n"
            "  $$\\bar{x} = \\dfrac{4 \\cdot 15 + 12 \\cdot 45 + 16 \\cdot 75 + 8 \\cdot 105}{40} = \\dfrac{60 + 540 + 1200 + 840}{40} = \\dfrac{2640}{40} = 66\\text{ (phút)}$$\n\n"
            "**Bước 2: Tính trung vị $M_e$**\n"
            "- Ta có $\\dfrac{n}{2} = 20$. Tần số tích lũy của hai nhóm đầu là $4 + 12 = 16 < 20$, của ba nhóm đầu là $16 + 16 = 32 \\ge 20$. Vậy nhóm chứa trung vị là nhóm $3$: $[60; 90)$ với $u_3 = 60$, $m_3 = 16$, $C = 16$, độ dài nhóm $90 - 60 = 30$.\n"
            "  $$M_e = 60 + \\dfrac{20 - 16}{16} \\cdot 30 = 60 + \\dfrac{4}{16} \\cdot 30 = 67{,}5\\text{ (phút)}$$\n\n"
            "**Bước 3: Tính mốt $M_o$**\n"
            "- Nhóm có tần số lớn nhất là nhóm $3$: $[60; 90)$ với $m_3 = 16$, $m_2 = 12$, $m_4 = 8$.\n"
            "  $$M_o = 60 + \\dfrac{16 - 12}{(16 - 12) + (16 - 8)} \\cdot 30 = 60 + \\dfrac{4}{4 + 8} \\cdot 30 = 60 + 10 = 70\\text{ (phút)}$$"
        ),
        "real_life": (
            "Thống kê mẫu số liệu ghép nhóm được ứng dụng rộng rãi trong điều tra dân số, phân tích phổ điểm thi tốt nghiệp THPT, "
            "đánh giá mức thu nhập trung bình của người lao động, theo dõi chỉ số sinh học trong y tế và phân tích hành vi khách hàng."
        ),
        "quiz": [
            mcq(
                "biet",
                "Giá trị đại diện của nhóm số liệu $[20; 30)$ là:",
                ["$25$", "$20$", "$30$", "$10$"],
                0,
                "Giá trị đại diện của nhóm $[a; b)$ là trung điểm $c = \\dfrac{20 + 30}{2} = 25$.",
            ),
            mcq(
                "biet",
                "Độ dài của nhóm số liệu $[15; 25)$ bằng:",
                ["$10$", "$20$", "$15$", "$25$"],
                0,
                "Độ dài của nhóm $[15; 25)$ là $25 - 15 = 10$.",
            ),
            mcq(
                "biet",
                "Trong mẫu số liệu ghép nhóm có các nhóm cùng độ dài, nhóm chứa mốt là nhóm có:",
                [
                    "Tần số lớn nhất",
                    "Tần số nhỏ nhất",
                    "Giá trị đại diện lớn nhất",
                    "Tần số tích lũy bằng nửa cỡ mẫu",
                ],
                0,
                "Theo định nghĩa, nhóm chứa mốt của mẫu số liệu ghép nhóm là nhóm có tần số lớn nhất.",
            ),
            mcq(
                "biet",
                "Đối với mẫu số liệu ghép nhóm bất kì, tứ phân vị thứ hai $Q_2$ luôn bằng:",
                [
                    "Trung vị $M_e$",
                    "Số trung bình $\\bar{x}$",
                    "Mốt $M_o$",
                    "Trung bình cộng của $Q_1$ và $Q_3$",
                ],
                0,
                "Theo định nghĩa tứ phân vị, tứ phân vị thứ hai $Q_2$ chính là trung vị $M_e$ của mẫu số liệu.",
            ),
            mcq(
                "hieu",
                "Khảo sát điểm kiểm tra của $20$ học sinh thu được bảng ghép nhóm: $[0; 4)$ có $2$ học sinh; $[4; 8)$ có $10$ học sinh; $[8; 10]$ có $8$ học sinh. Số trung bình $\\bar{x}$ của mẫu số liệu trên là:",
                ["$6{,}8$", "$6{,}5$", "$7{,}2$", "$6{,}0$"],
                0,
                "Giá trị đại diện của các nhóm lần lượt là $2; 6; 9$. Ta có $\\bar{x} = \\dfrac{2 \\cdot 2 + 10 \\cdot 6 + 8 \\cdot 9}{20} = \\dfrac{4 + 60 + 72}{20} = \\dfrac{136}{20} = 6{,}8$.",
            ),
            mcq(
                "hieu",
                "Cho mẫu số liệu ghép nhóm có cỡ mẫu $n = 40$ gồm $4$ nhóm: $[10; 20)$ có tần số $6$; $[20; 30)$ có tần số $10$; $[30; 40)$ có tần số $16$; $[40; 50]$ có tần số $8$. Trung vị $M_e$ của mẫu số liệu là:",
                ["$32{,}5$", "$35{,}0$", "$31{,}5$", "$34{,}0$"],
                0,
                "Ta có $\\dfrac{n}{2} = 20$. Tần số tích lũy của $2$ nhóm đầu là $6 + 10 = 16 < 20$, của $3$ nhóm đầu là $16 + 16 = 32 \\ge 20$. Nhóm chứa trung vị là $[30; 40)$, nên $M_e = 30 + \\dfrac{20 - 16}{16} \\cdot 10 = 32{,}5$.",
            ),
            tf4(
                "hieu",
                "Chiều cao (đơn vị: $\\text{cm}$) của $50$ cây giống được ghi lại ở bảng ghép nhóm: $[10; 20)$ có $5$ cây; $[20; 30)$ có $15$ cây; $[30; 40)$ có $20$ cây; $[40; 50]$ có $10$ cây. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Cỡ mẫu của mẫu số liệu trên là $n = 50$.",
                    "Giá trị đại diện của nhóm $[30; 40)$ là $30$.",
                    "Chiều cao trung bình của $50$ cây giống là $\\bar{x} = 32\\text{ cm}$.",
                    "Trung vị của mẫu số liệu ghép nhóm trên là $M_e = 32{,}5\\text{ cm}$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $n = 5 + 15 + 20 + 10 = 50$.\n"
                "b) Sai vì giá trị đại diện của nhóm $[30; 40)$ là $\\dfrac{30 + 40}{2} = 35 \\neq 30$.\n"
                "c) Đúng vì $\\bar{x} = \\dfrac{5 \\cdot 15 + 15 \\cdot 25 + 20 \\cdot 35 + 10 \\cdot 45}{50} = \\dfrac{75 + 375 + 700 + 450}{50} = \\dfrac{1600}{50} = 32\\text{ cm}$.\n"
                "d) Đúng vì $\\dfrac{n}{2} = 25$, tần số tích lũy $2$ nhóm đầu là $5 + 15 = 20 < 25$, nhóm chứa trung vị là $[30; 40)$ có $m_3 = 20$, nên $M_e = 30 + \\dfrac{25 - 20}{20} \\cdot 10 = 32{,}5\\text{ cm}$.",
            ),
            tf4(
                "hieu",
                "Cho mẫu số liệu ghép nhóm về thời gian hoàn thành bài tập (đơn vị: phút) của $36$ học sinh: $[0; 10)$ có $4$ em; $[10; 20)$ có $8$ em; $[20; 30)$ có $15$ em; $[30; 40]$ có $9$ em. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Nhóm chứa mốt của mẫu số liệu là nhóm $[20; 30)$.",
                    "Nhóm chứa tứ phân vị thứ nhất $Q_1$ là nhóm $[0; 10)$.",
                    "Giá trị của tứ phân vị thứ nhất là $Q_1 = 16{,}25$ phút.",
                    "Giá trị của tứ phân vị thứ ba là $Q_3 = 30$ phút.",
                ],
                [True, False, True, True],
                "a) Đúng vì nhóm $[20; 30)$ có tần số lớn nhất ($m_3 = 15$).\n"
                "b) Sai vì $\\dfrac{n}{4} = \\dfrac{36}{4} = 9$. Nhóm $[0; 10)$ có tần số $4 < 9$, tần số tích lũy đến hết nhóm $[10; 20)$ là $4 + 8 = 12 \\ge 9$, nên nhóm chứa $Q_1$ là $[10; 20)$.\n"
                "c) Đúng vì $Q_1 = 10 + \\dfrac{9 - 4}{8} \\cdot 10 = 10 + 6{,}25 = 16{,}25$ (phút).\n"
                "d) Đúng vì $\\dfrac{3n}{4} = 27$, tần số tích lũy của $3$ nhóm đầu là $4 + 8 + 15 = 27$, nên $Q_3 = 20 + \\dfrac{27 - 12}{15} \\cdot 10 = 30$ (phút).",
            ),
            mcq(
                "vandung",
                "Khảo sát cân nặng (đơn vị: $\\text{kg}$) của một nhóm học sinh được bảng ghép nhóm: $[40; 45)$ có $5$ em; $[45; 50)$ có $11$ em; $[50; 55)$ có $19$ em; $[55; 60]$ có $13$ em. Mốt $M_o$ của mẫu số liệu ghép nhóm trên là:",
                ["$52{,}86$", "$52{,}50$", "$53{,}20$", "$51{,}75$"],
                0,
                "Nhóm chứa mốt là nhóm $3$: $[50; 55)$ với $u_3 = 50$, $m_3 = 19$, $m_2 = 11$, $m_4 = 13$, độ dài nhóm $5$. Áp dụng công thức: $M_o = 50 + \\dfrac{19 - 11}{(19 - 11) + (19 - 13)} \\cdot 5 = 50 + \\dfrac{8}{8 + 6} \\cdot 5 = 50 + \\dfrac{20}{7} \\approx 52{,}86$.",
            ),
            short(
                "vandung",
                "Số cuộc gọi điện thoại mỗi tuần của $20$ nhân viên tư vấn được thống kê như sau: $[10; 20)$ có $2$ người; $[20; 30)$ có $6$ người; $[30; 40)$ có $8$ người; $[40; 50]$ có $4$ người. Hãy tính số cuộc gọi trung bình của mỗi nhân viên trong một tuần.",
                ["32"],
                "Giá trị đại diện của $4$ nhóm lần lượt là $15; 25; 35; 45$. Số cuộc gọi trung bình là $\\bar{x} = \\dfrac{2 \\cdot 15 + 6 \\cdot 25 + 8 \\cdot 35 + 4 \\cdot 45}{20} = \\dfrac{30 + 150 + 280 + 180}{20} = \\dfrac{640}{20} = 32$.",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG IV. QUAN HỆ SONG SONG TRONG KHÔNG GIAN
    # =========================================================================
    {
        "topic": "l11-ch04-quan-he-song-song-trong-khong-gian",
        "title": "Chương IV. Quan hệ song song trong không gian",
        "icon": "🧊",
        "description": (
            "Xây dựng nền tảng hình học không gian: đại cương về đường thẳng và mặt phẳng, "
            "hình chóp và hình tứ diện, quan hệ song song giữa hai đường thẳng, giữa đường thẳng "
            "và mặt phẳng, giữa hai mặt phẳng cùng phép chiếu song song."
        ),
        "requirements": [
            "Nhận biết được các quan hệ liên thuộc cơ bản giữa điểm, đường thẳng, mặt phẳng trong không gian và mô tả được ba cách xác định mặt phẳng.",
            "Xác định được giao tuyến của hai mặt phẳng, giao điểm của đường thẳng và mặt phẳng; nhận biết được hình chóp và hình tứ diện.",
            "Nhận biết được vị trí tương đối của hai đường thẳng trong không gian (trùng nhau, song song, cắt nhau, chéo nhau) và giải thích được tính chất cơ bản về hai đường thẳng song song.",
            "Nhận biết và giải thích được điều kiện, tính chất cơ bản để đường thẳng song song với mặt phẳng.",
            "Nhận biết và giải thích được điều kiện, tính chất cơ bản về hai mặt phẳng song song; định lí Thalès trong không gian; tính chất cơ bản của hình lăng trụ và hình hộp.",
            "Nhận biết được khái niệm và tính chất cơ bản của phép chiếu song song; vẽ được hình biểu diễn của một số hình khối đơn giản và vận dụng quan hệ song song vào thực tiễn.",
        ],
        "definition": (
            "Chương học thiết lập các tính chất thừa nhận của hình học không gian và nghiên cứu trọn vẹn ba cấp độ "
            "của quan hệ song song: hai đường thẳng song song ($a \\parallel b$), đường thẳng song song với mặt phẳng ($d \\parallel (\\alpha)$), "
            "hai mặt phẳng song song ($(\\alpha) \\parallel (\\beta)$), cùng cơ sở toán học để biểu diễn hình không gian lên mặt phẳng thông qua phép chiếu song song."
        ),
        "theory": (
            "### Bài 10. Đường thẳng và mặt phẳng trong không gian\n"
            "- **Ba cách xác định một mặt phẳng:** Qua ba điểm không thẳng hàng $A, B, C$; qua một đường thẳng $d$ và một điểm $A \\notin d$; qua hai đường thẳng cắt nhau $a$ và $b$.\n"
            "- **Cách tìm giao tuyến của hai mặt phẳng:** Tìm hai điểm chung phân biệt của hai mặt phẳng, đường thẳng nối hai điểm chung đó là giao tuyến.\n"
            "- **Cách tìm giao điểm của đường thẳng $d$ và mặt phẳng $(\\alpha)$:** Chọn mặt phẳng phụ $(\\beta)$ chứa $d$, tìm giao tuyến $\\Delta = (\\alpha) \\cap (\\beta)$, khi đó giao điểm $I = d \\cap \\Delta$ chính là $d \\cap (\\alpha)$.\n"
            "- **Hình chóp và hình tứ diện:** Hình chóp có đáy là đa giác lồi và các mặt bên là các tam giác có chung đỉnh $S$. Hình tứ diện là hình chóp tam giác (có $4$ mặt là tam giác, $4$ đỉnh, $6$ cạnh).\n\n"
            "### Bài 11. Hai đường thẳng song song\n"
            "- **Vị trí tương đối của hai đường thẳng trong không gian:** Có $4$ vị trí: *đồng phẳng* (cắt nhau, song song, trùng nhau) và *không đồng phẳng* (chéo nhau).\n"
            "- **Định lí về giao tuyến của ba mặt phẳng:** Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến ấy hoặc đồng quy hoặc đôi một song song.\n\n"
            "### Bài 12. Đường thẳng và mặt phẳng song song\n"
            "- **Dấu hiệu nhận biết:** Nếu đường thẳng $d$ không nằm trong mặt phẳng $(\\alpha)$ và $d$ song song với một đường thẳng $d'$ nằm trong $(\\alpha)$ thì $d \\parallel (\\alpha)$.\n"
            "- **Tính chất:** Nếu $d \\parallel (\\alpha)$ thì mọi mặt phẳng $(\\beta)$ chứa $d$ và cắt $(\\alpha)$ đều cắt theo một giao tuyến song song với $d$.\n\n"
            "### Bài 13. Hai mặt phẳng song song\n"
            "- **Dấu hiệu nhận biết:** Nếu mặt phẳng $(\\alpha)$ chứa hai đường thẳng cắt nhau $a, b$ và $a, b$ cùng song song với mặt phẳng $(\\beta)$ thì $(\\alpha) \\parallel (\\beta)$.\n"
            "- **Tính chất:** Một mặt phẳng thứ ba cắt hai mặt phẳng song song thì hai giao tuyến tạo thành song song với nhau. Định lí Thalès: Ba mặt phẳng đôi một song song chắn trên hai cát tuyến bất kì những đoạn thẳng tương ứng tỉ lệ.\n"
            "- **Hình lăng trụ và hình hộp:** Hình lăng trụ có hai đáy là hai đa giác nằm trên hai mặt phẳng song song và các cạnh bên song song, bằng nhau. Hình hộp là hình lăng trụ có đáy là hình bình hành.\n\n"
            "### Bài 14. Phép chiếu song song\n"
            "- **Tính chất:** Phép chiếu song song biến ba điểm thẳng hàng thành ba điểm thẳng hàng và không làm thay đổi thứ tự; biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau; giữ nguyên tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng hoặc trên hai đường thẳng song song."
        ),
        "formulas": [
            G(
                "Số đỉnh, cạnh, mặt của hình khối cơ bản",
                F("Hình chóp n-giác", "$\\text{Số đỉnh} = n + 1, \\quad \\text{Số mặt} = n + 1, \\quad \\text{Số cạnh} = 2n$"),
                F("Hình lăng trụ n-giác", "$\\text{Số đỉnh} = 2n, \\quad \\text{Số mặt} = n + 2, \\quad \\text{Số cạnh} = 3n$"),
            ),
            G(
                "Các định lí quan hệ song song",
                F("Đường thẳng song song mặt phẳng", "$\\begin{cases} d \\not\\subset (\\alpha) \\\\ d \\parallel d' \\\\ d' \\subset (\\alpha) \\end{cases} \\Rightarrow d \\parallel (\\alpha)$"),
                F("Giao tuyến khi đường thẳng song song mặt phẳng", "$\\begin{cases} d \\parallel (\\alpha) \\\\ d \\subset (\\beta) \\\\ (\\alpha) \\cap (\\beta) = \\Delta \\end{cases} \\Rightarrow \\Delta \\parallel d$"),
                F("Hai mặt phẳng song song", "$\\begin{cases} a, b \\subset (\\alpha), \\ a \\cap b = I \\\\ a \\parallel (\\beta), \\ b \\parallel (\\beta) \\end{cases} \\Rightarrow (\\alpha) \\parallel (\\beta)$"),
                F("Định lí Thalès không gian", "$\\dfrac{AB}{A'B'} = \\dfrac{BC}{B'C'} = \\dfrac{AC}{A'C'}$"),
            ),
        ],
        "example": (
            "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N$ lần lượt là trung điểm của $SA$ và $SD$.\n"
            "a) Chứng minh rằng đường thẳng $MN$ song song với mặt phẳng $(SBC)$.\n"
            "b) Gọi $P$ là trung điểm của $AB$. Chứng minh mặt phẳng $(OMN)$ song song với mặt phẳng $(SBC)$ và tính tỉ số diện tích của thiết diện tạo bởi $(OMN)$ với hình chóp so với diện tích tam giác $SBC$."
        ),
        "example_answer": (
            "**a) Chứng minh $MN \\parallel (SBC)$:**\n"
            "- Trong $\\triangle SAD$, $M$ và $N$ lần lượt là trung điểm của $SA, SD$ nên $MN$ là đường trung bình của $\\triangle SAD \\Rightarrow MN \\parallel AD$.\n"
            "- Vì $ABCD$ là hình bình hành nên $AD \\parallel BC$. Từ đó suy ra $MN \\parallel BC$.\n"
            "- Mà $MN \\not\\subset (SBC)$ và $BC \\subset (SBC)$ nên $MN \\parallel (SBC)$.\n\n"
            "**b) Chứng minh $(OMN) \\parallel (SBC)$ và xét thiết diện:**\n"
            "- Trong $\\triangle SAC$, $O$ là trung điểm của $AC$ và $M$ là trung điểm của $SA$ nên $OM$ là đường trung bình $\\Rightarrow OM \\parallel SC$. Vì $SC \\subset (SBC)$ nên $OM \\parallel (SBC)$.\n"
            "- Mặt phẳng $(OMN)$ chứa hai đường thẳng cắt nhau $MN$ và $OM$ cùng song song với $(SBC)$, suy ra $(OMN) \\parallel (SBC)$.\n"
            "- Gọi $P, Q$ lần lượt là trung điểm của $AB, CD$. Khi đó đường thẳng $PQ$ đi qua $O$ và $PQ \\parallel BC \\parallel MN$. Thiết diện là hình thang $MNPQ$ có các kích thước bằng một nửa các kích thước tương ứng khi cắt bởi các mặt bên."
        ),
        "real_life": (
            "Quan hệ song song và phép chiếu song song là cơ sở của bản vẽ kĩ thuật, kiến trúc xây dựng (các tầng nhà song song, "
            "cột trụ song song), hiện tượng bóng nắng của các vật thể dưới ánh sáng mặt trời và thiết kế đồ họa 3D."
        ),
        "quiz": [
            mcq(
                "biet",
                "Trong không gian, qua ba điểm không thẳng hàng xác định được bao nhiêu mặt phẳng?",
                ["$1$", "$2$", "$3$", "Vô số"],
                0,
                "Theo tính chất thừa nhận của hình học không gian, có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng.",
            ),
            mcq(
                "biet",
                "Hai đường thẳng chéo nhau trong không gian là hai đường thẳng:",
                [
                    "Không cùng nằm trong bất kì mặt phẳng nào",
                    "Cùng nằm trong một mặt phẳng và không có điểm chung",
                    "Có đúng một điểm chung",
                    "Cùng vuông góc với một đường thẳng thứ ba",
                ],
                0,
                "Theo định nghĩa, hai đường thẳng chéo nhau là hai đường thẳng không đồng phẳng (không cùng thuộc một mặt phẳng nào).",
            ),
            mcq(
                "biet",
                "Hình tứ diện có tất cả bao nhiêu cạnh?",
                ["$6$", "$4$", "$8$", "$5$"],
                0,
                "Hình tứ diện là hình chóp tam giác ($n = 3$) nên có số cạnh là $2n = 2 \\cdot 3 = 6$ cạnh.",
            ),
            mcq(
                "biet",
                "Qua phép chiếu song song, hình biểu diễn của một hình bình hành (nằm trong mặt phẳng không song song với phương chiếu) là:",
                [
                    "Một hình bình hành",
                    "Một hình thang không phải hình bình hành",
                    "Luôn là một hình chữ nhật",
                    "Luôn là một hình vuông",
                ],
                0,
                "Phép chiếu song song bảo toàn tính song song của các cặp cạnh đối, nên hình biểu diễn của hình bình hành là một hình bình hành.",
            ),
            mcq(
                "hieu",
                "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và:",
                [
                    "Song song với $AD$ và $BC$",
                    "Song song với $AB$ và $CD$",
                    "Cắt đường thẳng $AC$",
                    "Đi qua tâm $O$ của đáy $ABCD$",
                ],
                0,
                "Hai mặt phẳng $(SAD)$ và $(SBC)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song $AD \\parallel BC$, nên giao tuyến của chúng là đường thẳng $Sx$ đi qua $S$ và song song với $AD, BC$.",
            ),
            mcq(
                "hieu",
                "Cho tứ diện $ABCD$. Gọi $G_1$ và $G_2$ lần lượt là trọng tâm của hai tam giác $ABC$ và $ABD$. Khẳng định nào sau đây đúng?",
                [
                    "$G_1 G_2 \\parallel CD$ và $G_1 G_2 = \\dfrac{1}{3}CD$",
                    "$G_1 G_2 \\parallel AB$ và $G_1 G_2 = \\dfrac{1}{3}AB$",
                    "$G_1 G_2 \\parallel CD$ và $G_1 G_2 = \\dfrac{2}{3}CD$",
                    "$G_1 G_2$ cắt $CD$",
                ],
                0,
                "Gọi $M$ là trung điểm của $AB$. Khi đó $G_1 \\in MC, G_2 \\in MD$ và $\\dfrac{MG_1}{MC} = \\dfrac{MG_2}{MD} = \\dfrac{1}{3}$. Theo định lí Thalès trong $\\triangle MCD$, ta có $G_1 G_2 \\parallel CD$ và $G_1 G_2 = \\dfrac{1}{3}CD$.",
            ),
            tf4(
                "hieu",
                "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N, P$ lần lượt là trung điểm của $SA, SB, SC$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Đường thẳng $MN$ song song với đường thẳng $CD$.",
                    "Đường thẳng $MP$ cắt đường thẳng $AC$.",
                    "Đường thẳng $OP$ song song với mặt phẳng $(SAB)$.",
                    "Mặt phẳng $(MNP)$ song song với mặt phẳng $(ABCD)$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $MN$ là đường trung bình của $\\triangle SAB$ nên $MN \\parallel AB$, mà $AB \\parallel CD \\Rightarrow MN \\parallel CD$.\n"
                "b) Sai vì $MP$ là đường trung bình của $\\triangle SAC$ nên $MP \\parallel AC$ (không cắt nhau).\n"
                "c) Đúng vì $OP$ là đường trung bình của $\\triangle SAC$ nên $OP \\parallel SA$, mà $SA \\subset (SAB) \\Rightarrow OP \\parallel (SAB)$.\n"
                "d) Đúng vì $(MNP)$ chứa hai đường thẳng cắt nhau $MN$ và $MP$ lần lượt song song với $AB$ và $AC$ nằm trong $(ABCD)$, nên $(MNP) \\parallel (ABCD)$.",
            ),
            tf4(
                "hieu",
                "Cho hình hộp $ABCD.A'B'C'D'$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Tứ giác $ACC'A'$ là một hình bình hành.",
                    "Hai đường thẳng $AB'$ và $DC'$ chéo nhau.",
                    "Mặt phẳng $(AB'D')$ song song với mặt phẳng $(BC'D)$.",
                    "Đường chéo $AC'$ đi qua trọng tâm của hai tam giác $AB'D'$ và $CB'D$ (hoặc $BC'D$).",
                ],
                [True, False, True, True],
                "a) Đúng vì $AA' \\parallel CC'$ và $AA' = CC'$ nên $ACC'A'$ là hình bình hành.\n"
                "b) Sai vì $AB'C'D$ có $AD \\parallel B'C'$ và $AD = B'C'$ nên là hình bình hành, suy ra $AB' \\parallel DC'$ (đồng phẳng).\n"
                "c) Đúng vì $AB' \\parallel DC'$ và $AD' \\parallel BC'$ nên $(AB'D') \\parallel (BC'D)$.\n"
                "d) Đúng vì theo tính chất hình hộp, đường chéo $AC'$ cắt hai mặt phẳng $(AB'D')$ và $(BC'D)$ tại trọng tâm của hai tam giác tương ứng $AB'D'$ và $BC'D$.",
            ),
            mcq(
                "vandung",
                "Cho tứ diện $ABCD$ có $AB = CD = 6\\text{ cm}$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AC, BC, BD, AD$. Chu vi của tứ giác $MNPQ$ bằng:",
                ["$12\\text{ cm}$", "$24\\text{ cm}$", "$18\\text{ cm}$", "$6\\text{ cm}$"],
                0,
                "Theo tính chất đường trung bình của tam giác: $MN = PQ = \\dfrac{1}{2}AB = 3\\text{ cm}$ và $NP = MQ = \\dfrac{1}{2}CD = 3\\text{ cm}$. Vậy $MNPQ$ là hình thoi có chu vi $4 \\cdot 3 = 12\\text{ cm}$.",
            ),
            short(
                "vandung",
                "Cho hình chóp $S.ABC$ có diện tích đáy $ABC$ bằng $36\\text{ cm}^2$. Mặt phẳng $(\\alpha)$ song song với đáy $(ABC)$ và cắt cạnh $SA$ tại điểm $M$ sao cho $SM = \\dfrac{2}{3}SA$. Tính diện tích thiết diện của hình chóp cắt bởi mặt phẳng $(\\alpha)$ (đơn vị: $\\text{cm}^2$).",
                ["16"],
                "Mặt phẳng $(\\alpha) \\parallel (ABC)$ cắt hình chóp theo thiết diện là tam giác $MNP$ đồng dạng với $\\triangle ABC$ theo tỉ số $k = \\dfrac{SM}{SA} = \\dfrac{2}{3}$. Do đó diện tích thiết diện là $S_{MNP} = k^2 \\cdot S_{ABC} = \\left(\\dfrac{2}{3}\\right)^2 \\cdot 36 = \\dfrac{4}{9} \\cdot 36 = 16\\text{ (cm}^2\\text{)}$.",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG V. GIỚI HẠN. HÀM SỐ LIÊN TỤC
    # =========================================================================
    {
        "topic": "l11-ch05-gioi-han-ham-so-lien-tuc",
        "title": "Chương V. Giới hạn. Hàm số liên tục",
        "icon": "♾️",
        "description": (
            "Làm quen với giải tích thông qua giới hạn của dãy số, tổng của cấp số nhân lùi vô hạn, "
            "giới hạn hữu hạn và vô cực của hàm số, cùng khái niệm và tính chất của hàm số liên tục."
        ),
        "requirements": [
            "Nhận biết được khái niệm giới hạn của dãy số.",
            "Giải thích được một số giới hạn cơ bản như $\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\ (k \\in \\mathbb{N}^*)$, $\\lim_{n \\to +\\infty} q^n = 0 \\ (|q| < 1)$ và vận dụng các phép toán giới hạn dãy số.",
            "Tính được tổng của một cấp số nhân lùi vô hạn và vận dụng được kết quả đó để giải quyết một số tình huống thực tiễn.",
            "Nhận biết được khái niệm giới hạn hữu hạn của hàm số, giới hạn hữu hạn một phía của hàm số tại một điểm, giới hạn tại vô cực và giới hạn vô cực.",
            "Tính được một số giới hạn của hàm số bằng cách vận dụng các phép toán trên giới hạn hàm số.",
            "Nhận dạng được hàm số liên tục tại một điểm, trên một khoảng hoặc trên một đoạn; nhận dạng được tính liên tục của tổng, hiệu, tích, thương của hai hàm số liên tục và các hàm số sơ cấp cơ bản.",
        ],
        "definition": (
            "Giới hạn là khái niệm nền tảng của Giải tích, mô tả xu hướng tiến gần tới một giá trị xác định $L$ (hoặc tiến ra $\\pm\\infty$) "
            "của dãy số $(u_n)$ khi $n \\to +\\infty$, hoặc của hàm số $f(x)$ khi $x \\to x_0$ (hay $x \\to \\pm\\infty$). "
            "Hàm số $f(x)$ được gọi là liên tục tại $x_0$ nếu giới hạn của hàm số khi $x \\to x_0$ đúng bằng giá trị $f(x_0)$."
        ),
        "theory": (
            "### Bài 15. Giới hạn của dãy số\n"
            "- **Giới hạn hữu hạn:** Dãy số $(u_n)$ có giới hạn là $0$ khi $n \\to +\\infty$, kí hiệu $\\lim_{n \\to +\\infty} u_n = 0$, nếu $|u_n|$ có thể nhỏ hơn một số dương bé tùy ý kể từ một số hạng nào đó trở đi. Dãy $(u_n)$ có giới hạn là $a$ nếu $\\lim_{n \\to +\\infty} (u_n - a) = 0$.\n"
            "- **Các giới hạn đặc biệt:** $\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\ (k \\in \\mathbb{N}^*)$; $\\lim_{n \\to +\\infty} q^n = 0$ nếu $|q| < 1$; $\\lim_{n \\to +\\infty} c = c$.\n"
            "- **Cấp số nhân lùi vô hạn:** Cấp số nhân vô hạn $(u_n)$ có công bội $q$ thỏa mãn $|q| < 1$ được gọi là cấp số nhân lùi vô hạn. Tổng của nó là:\n"
            "  $$S = u_1 + u_2 + \\dots + u_n + \\dots = \\dfrac{u_1}{1 - q} \\quad (|q| < 1)$$\n\n"
            "### Bài 16. Giới hạn của hàm số\n"
            "- **Giới hạn hữu hạn tại một điểm:** $\\lim_{x \\to x_0} f(x) = L$. Hàm số có giới hạn $L$ khi $x \\to x_0$ khi và chỉ khi giới hạn trái và giới hạn phải bằng nhau: $\\lim_{x \\to x_0^-} f(x) = \\lim_{x \\to x_0^+} f(x) = L$.\n"
            "- **Khử dạng vô định $\\dfrac{0}{0}$:** Khi tính $\\lim_{x \\to x_0} \\dfrac{P(x)}{Q(x)}$ mà $P(x_0) = Q(x_0) = 0$, ta phân tích tử và mẫu thành nhân tử chứa $(x - x_0)$ hoặc nhân lượng liên hợp đối với biểu thức chứa căn.\n"
            "- **Giới hạn tại vô cực và giới hạn vô cực:** Áp dụng quy tắc đặt lũy thừa bậc cao nhất của $x$ làm nhân tử chung và sử dụng $\\lim_{x \\to \\pm\\infty} \\dfrac{c}{x^k} = 0$.\n\n"
            "### Bài 17. Hàm số liên tục\n"
            "- **Liên tục tại một điểm:** Hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ chứa $x_0$ được gọi là liên tục tại $x_0$ nếu $\\lim_{x \\to x_0} f(x) = f(x_0)$.\n"
            "- **Liên tục trên khoảng, đoạn:** Hàm số đa thức, hàm phân thức hữu tỉ, hàm căn thức và các hàm số lượng giác đều liên tục trên từng khoảng xác định của chúng.\n"
            "- **Tính chất nghiệm phương trình:** Nếu hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \\cdot f(b) < 0$ thì tồn tại ít nhất một điểm $c \\in (a; b)$ sao cho $f(c) = 0$."
        ),
        "formulas": [
            G(
                "Giới hạn của dãy số và cấp số nhân lùi vô hạn",
                F("Giới hạn cơ bản của dãy", "$\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\ (k \\in \\mathbb{N}^*), \\quad \\lim_{n \\to +\\infty} q^n = 0 \\ (|q| < 1)$"),
                F("Tổng cấp số nhân lùi vô hạn", "$S = \\dfrac{u_1}{1 - q} \\quad (|q| < 1)$"),
                F("Giới hạn phân thức cùng bậc", "$\\lim_{n \\to +\\infty} \\dfrac{a n^k + \\dots}{b n^k + \\dots} = \\dfrac{a}{b} \\quad (a, b \\neq 0)$"),
            ),
            G(
                "Giới hạn của hàm số",
                F("Điều kiện có giới hạn tại x0", "$\\lim_{x \\to x_0} f(x) = L \\Leftrightarrow \\lim_{x \\to x_0^-} f(x) = \\lim_{x \\to x_0^+} f(x) = L$"),
                F("Giới hạn cơ bản tại vô cực", "$\\lim_{x \\to \\pm\\infty} \\dfrac{c}{x^k} = 0 \\ (k \\in \\mathbb{N}^*), \\quad \\lim_{x \\to +\\infty} x^k = +\\infty$"),
                F("Hằng đẳng thức liên hợp", "$\\sqrt{A} - \\sqrt{B} = \\dfrac{A - B}{\\sqrt{A} + \\sqrt{B}}$"),
            ),
            G(
                "Hàm số liên tục",
                F("Điều kiện liên tục tại x0", "$\\lim_{x \\to x_0} f(x) = f(x_0) \\Leftrightarrow \\lim_{x \\to x_0^-} f(x) = \\lim_{x \\to x_0^+} f(x) = f(x_0)$"),
                F("Định lí giá trị trung gian", "$f(x) \\text{ liên tục trên } [a; b] \\text{ và } f(a) \\cdot f(b) < 0 \\Rightarrow \\exists c \\in (a; b): f(c) = 0$"),
            ),
        ],
        "example": (
            "a) Tính các giới hạn sau: $L_1 = \\lim_{n \\to +\\infty} \\dfrac{3n^2 - 2n + 1}{n^2 + 4}$ và $L_2 = \\lim_{x \\to 2} \\dfrac{\\sqrt{x + 2} - 2}{x - 2}$.\n"
            "b) Tìm giá trị của tham số $m$ để hàm số $f(x) = \\begin{cases} \\dfrac{x^2 - 9}{x - 3} & \\text{khi } x \\neq 3 \\\\ 2m + 1 & \\text{khi } x = 3 \\end{cases}$ liên tục tại điểm $x_0 = 3$."
        ),
        "example_answer": (
            "**a) Tính giới hạn $L_1$ và $L_2$:**\n"
            "- Chia cả tử và mẫu của $L_1$ cho $n^2$:\n"
            "  $$L_1 = \\lim_{n \\to +\\infty} \\dfrac{3 - \\dfrac{2}{n} + \\dfrac{1}{n^2}}{1 + \\dfrac{4}{n^2}} = \\dfrac{3 - 0 + 0}{1 + 0} = 3$$\n"
            "- Nhân cả tử và mẫu của $L_2$ với lượng liên hợp $\\sqrt{x + 2} + 2$:\n"
            "  $$L_2 = \\lim_{x \\to 2} \\dfrac{(x + 2) - 4}{(x - 2)(\\sqrt{x + 2} + 2)} = \\lim_{x \\to 2} \\dfrac{1}{\\sqrt{x + 2} + 2} = \\dfrac{1}{\\sqrt{2 + 2} + 2} = \\dfrac{1}{4}$$\n\n"
            "**b) Tìm $m$ để hàm số liên tục tại $x_0 = 3$:**\n"
            "- Ta có $f(3) = 2m + 1$ và:\n"
            "  $$\\lim_{x \\to 3} f(x) = \\lim_{x \\to 3} \\dfrac{(x - 3)(x + 3)}{x - 3} = \\lim_{x \\to 3} (x + 3) = 6$$\n"
            "- Hàm số liên tục tại $x_0 = 3 \\Leftrightarrow \\lim_{x \\to 3} f(x) = f(3) \\Leftrightarrow 2m + 1 = 6 \\Leftrightarrow m = \\dfrac{5}{2}$."
        ),
        "real_life": (
            "Giới hạn và cấp số nhân lùi vô hạn giải thích nghịch lí Zeno (Achilles và con rùa), tính tổng quãng đường quả bóng nảy "
            "đến khi dừng hẳn, mô tả các đường tiệm cận và trạng thái ổn định lâu dài của các hệ thống vật lí, kinh tế."
        ),
        "quiz": [
            mcq(
                "biet",
                "Giá trị của giới hạn $\\lim_{n \\to +\\infty} \\dfrac{4n - 1}{2n + 3}$ bằng:",
                ["$2$", "$-\\dfrac{1}{3}$", "$4$", "$0$"],
                0,
                "Chia cả tử và mẫu cho $n$, ta có $\\lim_{n \\to +\\infty} \\dfrac{4 - \\dfrac{1}{n}}{2 + \\dfrac{3}{n}} = \\dfrac{4}{2} = 2$.",
            ),
            mcq(
                "biet",
                "Trong các giới hạn dãy số sau, giới hạn nào bằng $0$?",
                [
                    "$\\lim_{n \\to +\\infty} \\left(\\dfrac{2}{3}\\right)^n$",
                    "$\\lim_{n \\to +\\infty} \\left(\\dfrac{4}{3}\\right)^n$",
                    "$\\lim_{n \\to +\\infty} (-2)^n$",
                    "$\\lim_{n \\to +\\infty} n^3$",
                ],
                0,
                "Vì $\\left|\\dfrac{2}{3}\\right| < 1$ nên theo giới hạn cơ bản $\\lim_{n \\to +\\infty} \\left(\\dfrac{2}{3}\\right)^n = 0$.",
            ),
            mcq(
                "biet",
                "Giá trị của giới hạn $\\lim_{x \\to 2} (3x^2 - x + 1)$ bằng:",
                ["$11$", "$9$", "$13$", "$5$"],
                0,
                "Thay trực tiếp $x = 2$ vào hàm đa thức liên tục: $\\lim_{x \\to 2} (3x^2 - x + 1) = 3 \\cdot 2^2 - 2 + 1 = 11$.",
            ),
            mcq(
                "biet",
                "Hàm số $f(x) = \\dfrac{x + 1}{x - 2}$ gián đoạn tại điểm nào dưới đây?",
                ["$x = 2$", "$x = -1$", "$x = 0$", "$x = 1$"],
                0,
                "Hàm phân thức hữu tỉ xác định và liên tục trên $\\mathbb{R} \\setminus \\{2\\}$, nên gián đoạn tại $x = 2$.",
            ),
            mcq(
                "hieu",
                "Tổng của cấp số nhân lùi vô hạn $S = 1 + \\dfrac{1}{3} + \\dfrac{1}{9} + \\dots + \\dfrac{1}{3^n} + \\dots$ bằng:",
                ["$\\dfrac{3}{2}$", "$\\dfrac{2}{3}$", "$2$", "$\\dfrac{4}{3}$"],
                0,
                "Đây là cấp số nhân lùi vô hạn với $u_1 = 1$ và công bội $q = \\dfrac{1}{3}$. Do đó $S = \\dfrac{u_1}{1 - q} = \\dfrac{1}{1 - \\dfrac{1}{3}} = \\dfrac{3}{2}$.",
            ),
            mcq(
                "hieu",
                "Giá trị của giới hạn $\\lim_{x \\to 3} \\dfrac{x^2 - 5x + 6}{x - 3}$ bằng:",
                ["$1$", "$5$", "$0$", "$-1$"],
                0,
                "Ta phân tích tử thức: $\\lim_{x \\to 3} \\dfrac{(x - 2)(x - 3)}{x - 3} = \\lim_{x \\to 3} (x - 2) = 3 - 2 = 1$.",
            ),
            tf4(
                "hieu",
                "Cho hai dãy số $(u_n)$ và $(v_n)$ với $u_n = \\dfrac{2n^2 + 1}{n^2 + 3}$ và $v_n = \\left(\\dfrac{1}{2}\\right)^n$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Giới hạn của dãy số $(u_n)$ khi $n \\to +\\infty$ bằng $2$.",
                    "Giới hạn của dãy số $(v_n)$ khi $n \\to +\\infty$ bằng $\\dfrac{1}{2}$.",
                    "Giới hạn $\\lim_{n \\to +\\infty} (u_n + v_n)$ bằng $2$.",
                    "Tổng của cấp số nhân lùi vô hạn $(v_n)$ với $n \\ge 1$ là $S = v_1 + v_2 + \\dots = 1$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $\\lim_{n \\to +\\infty} \\dfrac{2 + \\dfrac{1}{n^2}}{1 + \\dfrac{3}{n^2}} = 2$.\n"
                "b) Sai vì $\\left|\\dfrac{1}{2}\\right| < 1$ nên $\\lim_{n \\to +\\infty} v_n = 0 \\neq \\dfrac{1}{2}$.\n"
                "c) Đúng vì $\\lim_{n \\to +\\infty} (u_n + v_n) = 2 + 0 = 2$.\n"
                "d) Đúng vì $(v_n)$ có $v_1 = \\dfrac{1}{2}$ và $q = \\dfrac{1}{2}$, nên $S = \\dfrac{v_1}{1 - q} = \\dfrac{\\dfrac{1}{2}}{1 - \\dfrac{1}{2}} = 1$.",
            ),
            tf4(
                "hieu",
                "Cho hàm số $f(x) = \\begin{cases} \\dfrac{x^2 - 4}{x - 2} & \\text{khi } x \\neq 2 \\\\ m + 1 & \\text{khi } x = 2 \\end{cases}$ với $m$ là tham số thực. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Tập xác định của hàm số $f(x)$ là $D = \\mathbb{R}$.",
                    "Giới hạn $\\lim_{x \\to 2} f(x)$ bằng $2$.",
                    "Hàm số $f(x)$ liên tục trên các khoảng $(-\\infty; 2)$ và $(2; +\\infty)$ với mọi $m$.",
                    "Hàm số $f(x)$ liên tục tại điểm $x = 2$ khi và chỉ khi $m = 3$.",
                ],
                [True, False, True, True],
                "a) Đúng vì hàm số được định nghĩa với cả $x \\neq 2$ và $x = 2$, nên $D = \\mathbb{R}$.\n"
                "b) Sai vì $\\lim_{x \\to 2} f(x) = \\lim_{x \\to 2} \\dfrac{(x - 2)(x + 2)}{x - 2} = \\lim_{x \\to 2} (x + 2) = 4 \\neq 2$.\n"
                "c) Đúng vì khi $x \\neq 2$, $f(x) = x + 2$ là hàm đa thức nên liên tục trên $(-\\infty; 2)$ và $(2; +\\infty)$.\n"
                "d) Đúng vì $f(x)$ liên tục tại $x = 2 \\Leftrightarrow f(2) = \\lim_{x \\to 2} f(x) \\Leftrightarrow m + 1 = 4 \\Leftrightarrow m = 3$.",
            ),
            mcq(
                "vandung",
                "Một quả bóng cao su được thả rơi thẳng đứng từ độ cao $10\\text{ m}$ xuống mặt đất. Mỗi lần chạm đất, quả bóng lại nảy lên theo phương thẳng đứng đạt độ cao bằng $\\dfrac{3}{5}$ độ cao của lần rơi ngay trước đó. Tổng quãng đường quả bóng đi được kể từ lúc thả cho đến khi dừng hẳn bằng:",
                ["$40\\text{ m}$", "$25\\text{ m}$", "$30\\text{ m}$", "$50\\text{ m}$"],
                0,
                "Quãng đường lần rơi đầu tiên là $10\\text{ m}$. Các lần nảy lên và rơi xuống tiếp theo mỗi độ cao được đi $2$ lần, tạo thành cấp số nhân lùi vô hạn có $u_1 = 10 \\cdot \\dfrac{3}{5} = 6\\text{ m}$ và $q = \\dfrac{3}{5}$. Tổng quãng đường là $S = 10 + 2 \\cdot \\dfrac{6}{1 - \\dfrac{3}{5}} = 10 + 2 \\cdot 15 = 40\\text{ m}$.",
            ),
            short(
                "vandung",
                "Biết rằng giới hạn $\\lim_{x \\to 1} \\dfrac{\\sqrt{3x + 1} - 2}{x - 1} = \\dfrac{a}{b}$, trong đó $\\dfrac{a}{b}$ là phân số tối giản và $a, b \\in \\mathbb{N}^*$. Tính giá trị của biểu thức $P = a + b$.",
                ["7"],
                "Nhân lượng liên hợp: $\\lim_{x \\to 1} \\dfrac{\\sqrt{3x + 1} - 2}{x - 1} = \\lim_{x \\to 1} \\dfrac{3(x - 1)}{(x - 1)(\\sqrt{3x + 1} + 2)} = \\lim_{x \\to 1} \\dfrac{3}{\\sqrt{3x + 1} + 2} = \\dfrac{3}{4}$. Suy ra $a = 3, b = 4 \\Rightarrow P = a + b = 7$.",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG VI. HÀM SỐ MŨ VÀ HÀM SỐ LÔGARIT
    # =========================================================================
    {
        "topic": "l11-ch06-ham-so-mu-va-ham-so-logarit",
        "title": "Chương VI. Hàm số mũ và hàm số lôgarit",
        "icon": "📈",
        "description": (
            "Mở rộng phép tính lũy thừa sang số mũ thực, tìm hiểu khái niệm và các quy tắc tính lôgarit, "
            "khảo sát đồ thị, tính chất của hàm số mũ và hàm số lôgarit cùng cách giải phương trình, bất phương trình mũ và lôgarit."
        ),
        "requirements": [
            "Nhận biết được khái niệm và các tính chất của phép tính lũy thừa với số mũ nguyên, số mũ hữu tỉ và số mũ thực.",
            "Rút gọn được biểu thức chứa lũy thừa và tính được giá trị biểu thức bằng máy tính cầm tay.",
            "Nhận biết được khái niệm lôgarit cơ số $a$ ($a > 0, a \\neq 1$) của một số thực dương và giải thích được các tính chất của phép tính lôgarit (lôgarit của tích, thương, lũy thừa, đổi cơ số).",
            "Nhận biết được hàm số mũ $y = a^x$ và hàm số lôgarit $y = \\log_a x$; nhận dạng đồ thị và giải thích các tính chất của chúng thông qua đồ thị.",
            "Giải được phương trình, bất phương trình mũ và lôgarit ở dạng đơn giản.",
            "Giải quyết được một số vấn đề liên môn hoặc thực tiễn gắn với hàm số, phương trình, bất phương trình mũ và lôgarit (như lãi suất kép, tăng trưởng dân số, độ pH, độ lớn động đất Richter, mức cường độ âm).",
        ],
        "definition": (
            "Với cơ số $a > 0, a \\neq 1$, phép lấy lũy thừa $b = a^\\alpha$ và phép lấy lôgarit $\\alpha = \\log_a b$ ($b > 0$) là hai phép toán "
            "ngược nhau. Từ đó hình thành hai lớp hàm số siêu việt cơ bản là hàm số mũ $y = a^x$ và hàm số lôgarit $y = \\log_a x$ "
            "có tính đơn điệu phụ thuộc hoàn toàn vào việc $a > 1$ hay $0 < a < 1$."
        ),
        "theory": (
            "### Bài 18. Luỹ thừa với số mũ thực\n"
            "- **Lũy thừa với số mũ nguyên và hữu tỉ:** Với $a \\neq 0$ và $n \\in \\mathbb{N}^*$, ta có $a^0 = 1$, $a^{-n} = \\dfrac{1}{a^n}$. Với $a > 0$ và số hữu tỉ $r = \\dfrac{m}{n}$ ($m \\in \\mathbb{Z}, n \\in \\mathbb{N}^*, n \\ge 2$), ta có $a^r = a^{\\dfrac{m}{n}} = \\sqrt[n]{a^m}$.\n"
            "- **Tính chất lũy thừa với số mũ thực:** Với $a, b > 0$ và $\\alpha, \\beta \\in \\mathbb{R}$, các quy tắc nhân, chia lũy thừa cùng cơ số, lũy thừa của lũy thừa, lũy thừa của một tích hoặc thương hoàn toàn tương tự số mũ tự nhiên.\n\n"
            "### Bài 19. Lôgarit\n"
            "- **Định nghĩa:** Cho $a > 0, a \\neq 1$ và $b > 0$. Số thực $\\alpha$ thỏa mãn $a^\\alpha = b$ được gọi là lôgarit cơ số $a$ của $b$, kí hiệu $\\log_a b = \\alpha$.\n"
            "- **Tính chất cơ bản:** $\\log_a 1 = 0$; $\\log_a a = 1$; $\\log_a (a^\\alpha) = \\alpha$; $a^{\\log_a b} = b$.\n"
            "- **Quy tắc tính và đổi cơ số:** Với $a > 0, a \\neq 1$ và $M, N > 0$: lôgarit của một tích bằng tổng các lôgarit, lôgarit của một thương bằng hiệu các lôgarit, $\\log_a M^\\alpha = \\alpha\\log_a M$, và công thức đổi cơ số $\\log_a b = \\dfrac{\\log_c b}{\\log_c a}$.\n"
            "- **Lôgarit thập phân và lôgarit tự nhiên:** Lôgarit cơ số $10$ kí hiệu là $\\log x$ (hoặc $\\lg x$); lôgarit cơ số $e \\approx 2{,}71828$ kí hiệu là $\\ln x$.\n\n"
            "### Bài 20. Hàm số mũ và hàm số lôgarit\n"
            "- **Hàm số mũ $y = a^x \\ (a > 0, a \\neq 1)$:** Tập xác định $D = \\mathbb{R}$, tập giá trị $T = (0; +\\infty)$, đồ thị luôn đi qua $(0; 1)$ và nằm phía trên trục hoành $Ox$.\n"
            "- **Hàm số lôgarit $y = \\log_a x \\ (a > 0, a \\neq 1)$:** Tập xác định $D = (0; +\\infty)$, tập giá trị $T = \\mathbb{R}$, đồ thị luôn đi qua $(1; 0)$ và nằm bên phải trục tung $Oy$.\n"
            "- **Tính đơn điệu:** Cả hai hàm số đều đồng biến trên tập xác định khi $a > 1$ và nghịch biến trên tập xác định khi $0 < a < 1$.\n\n"
            "### Bài 21. Phương trình, bất phương trình mũ và lôgarit\n"
            "- **Phương trình cơ bản:** $a^x = b \\ (b > 0) \\Leftrightarrow x = \\log_a b$; $\\log_a x = b \\Leftrightarrow x = a^b \\ (x > 0)$.\n"
            "- **Bất phương trình cơ bản:** Khi $a > 1$, bất phương trình giữ nguyên chiều ($a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) > g(x)$). Khi $0 < a < 1$, bất phương trình đổi chiều ($a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) < g(x)$). Luôn đặt điều kiện xác định cho biểu thức dưới dấu lôgarit dương."
        ),
        "formulas": [
            G(
                "Phép tính lũy thừa với cơ số dương",
                F("Số mũ âm và hữu tỉ", "$a^{-n} = \\dfrac{1}{a^n} \\ (a \\neq 0), \\quad a^{\\dfrac{m}{n}} = \\sqrt[n]{a^m}$"),
                F("Quy tắc lũy thừa", "$a^\\alpha \\cdot a^\\beta = a^{\\alpha + \\beta}, \\quad \\dfrac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}, \\quad (a^\\alpha)^\\beta = a^{\\alpha\\beta}, \\quad (ab)^\\alpha = a^\\alpha b^\\alpha$"),
            ),
            G(
                "Phép tính lôgarit",
                F("Định nghĩa lôgarit", "$\\alpha = \\log_a b \\Leftrightarrow a^\\alpha = b$"),
                F("Quy tắc tích, thương, mũ", "$\\log_a(MN) = \\log_a M + \\log_a N, \\quad \\log_a\\left(\\dfrac{M}{N}\\right) = \\log_a M - \\log_a N, \\quad \\log_a(M^\\alpha) = \\alpha\\log_a M$"),
                F("Công thức đổi cơ số", "$\\log_a b = \\dfrac{\\log_c b}{\\log_c a}, \\quad \\log_a b = \\dfrac{1}{\\log_b a}, \\quad \\log_{a^\\alpha} b = \\dfrac{1}{\\alpha}\\log_a b \\ (\\alpha \\neq 0)$"),
            ),
            G(
                "Phương trình, bất phương trình và lãi kép",
                F("Phương trình mũ & lôgarit", "$a^{f(x)} = b \\Leftrightarrow f(x) = \\log_a b \\ (b > 0); \\quad \\log_a f(x) = b \\Leftrightarrow f(x) = a^b$"),
                F("Bất phương trình mũ", "$a^{f(x)} > a^{g(x)} \\Leftrightarrow \\begin{cases} f(x) > g(x) & \\text{nếu } a > 1 \\\\ f(x) < g(x) & \\text{nếu } 0 < a < 1 \\end{cases}$"),
                F("Công thức lãi kép", "$A = P(1 + r)^n, \\quad A = P e^{rt} \\text{ (lãi kép liên tục)}$"),
            ),
        ],
        "example": (
            "a) Cho $\\log_2 3 = a$ và $\\log_2 5 = b$. Hãy biểu diễn $\\log_6 45$ theo $a$ và $b$.\n"
            "b) Giải bất phương trình lôgarit: $\\log_{\\dfrac{1}{2}}(2x - 2) \\ge -2$."
        ),
        "example_answer": (
            "**a) Biểu diễn $\\log_6 45$ theo $a$ và $b$:**\n"
            "- Đổi về cơ số $2$ và phân tích $45 = 3^2 \\cdot 5$, $6 = 2 \\cdot 3$:\n"
            "  $$\\log_6 45 = \\dfrac{\\log_2 45}{\\log_2 6} = \\dfrac{\\log_2(3^2 \\cdot 5)}{\\log_2(2 \\cdot 3)} = \\dfrac{2\\log_2 3 + \\log_2 5}{\\log_2 2 + \\log_2 3} = \\dfrac{2a + b}{1 + a}$$\n\n"
            "**b) Giải bất phương trình $\\log_{\\dfrac{1}{2}}(2x - 2) \\ge -2$:**\n"
            "- Điều kiện xác định: $2x - 2 > 0 \\Leftrightarrow x > 1$.\n"
            "- Vì cơ số $a = \\dfrac{1}{2} \\in (0; 1)$ nên bất phương trình đổi chiều:\n"
            "  $$\\log_{\\dfrac{1}{2}}(2x - 2) \\ge -2 \\Leftrightarrow 2x - 2 \\le \\left(\\dfrac{1}{2}\\right)^{-2} \\Leftrightarrow 2x - 2 \\le 4 \\Leftrightarrow x \\le 3$$\n"
            "- Kết hợp với điều kiện $x > 1$, tập nghiệm của bất phương trình là $S = (1; 3]$."
        ),
        "real_life": (
            "Hàm số mũ và lôgarit được dùng để tính lãi kép trong tài chính ngân hàng, xác định niên đại cổ vật bằng đồng vị phóng xạ "
            "$\\text{C}^{14}$, đo độ pH của dung dịch ($\\text{pH} = -\\log[\\text{H}^+]$), đo mức cường độ âm theo đơn vị đề-xi-ben (dB) "
            "và độ lớn của trận động đất theo thang độ Richter."
        ),
        "quiz": [
            mcq(
                "biet",
                "Với $a$ là số thực dương tùy ý, biểu thức $P = a^{\\dfrac{5}{3}} \\cdot \\sqrt[3]{a}$ bằng:",
                ["$a^2$", "$a^{\\dfrac{5}{9}}$", "$a^{\\dfrac{4}{3}}$", "$a^3$"],
                0,
                "Ta có $P = a^{\\dfrac{5}{3}} \\cdot a^{\\dfrac{1}{3}} = a^{\\dfrac{5}{3} + \\dfrac{1}{3}} = a^2$.",
            ),
            mcq(
                "biet",
                "Với $a > 0, a \\neq 1$, giá trị của biểu thức $\\log_a (a^4)$ bằng:",
                ["$4$", "$\\dfrac{1}{4}$", "$-4$", "$a^4$"],
                0,
                "Theo tính chất cơ bản của lôgarit, $\\log_a(a^\\alpha) = \\alpha$, nên $\\log_a(a^4) = 4$.",
            ),
            mcq(
                "biet",
                "Trong các hàm số sau đây, hàm số nào đồng biến trên tập xác định của nó?",
                [
                    "$y = 3^x$",
                    "$y = \\left(\\dfrac{1}{2}\\right)^x$",
                    "$y = \\log_{\\dfrac{1}{3}} x$",
                    "$y = (0{,}4)^x$",
                ],
                0,
                "Hàm số mũ $y = a^x$ đồng biến trên $\\mathbb{R}$ khi $a > 1$. Vì $3 > 1$ nên $y = 3^x$ đồng biến trên $\\mathbb{R}$.",
            ),
            mcq(
                "biet",
                "Nghiệm của phương trình $2^{x - 1} = 8$ là:",
                ["$x = 4$", "$x = 3$", "$x = 2$", "$x = 5$"],
                0,
                "Ta có $2^{x - 1} = 8 = 2^3 \\Leftrightarrow x - 1 = 3 \\Leftrightarrow x = 4$.",
            ),
            mcq(
                "hieu",
                "Tập xác định $D$ của hàm số $y = \\log_3(6 - 2x)$ là:",
                [
                    "$D = (-\\infty; 3)$",
                    "$D = (3; +\\infty)$",
                    "$D = (-\\infty; 3]$",
                    "$D = \\mathbb{R} \\setminus \\{3\\}$",
                ],
                0,
                "Hàm số xác định khi biểu thức trong lôgarit dương: $6 - 2x > 0 \\Leftrightarrow x < 3$. Vậy $D = (-\\infty; 3)$.",
            ),
            mcq(
                "hieu",
                "Tập nghiệm $S$ của bất phương trình $\\log_{\\dfrac{1}{3}}(x - 1) > -2$ là:",
                [
                    "$S = (1; 10)$",
                    "$S = (-\\infty; 10)$",
                    "$S = (10; +\\infty)$",
                    "$S = [1; 10)$",
                ],
                0,
                "Điều kiện: $x - 1 > 0 \\Leftrightarrow x > 1$. Vì cơ số $\\dfrac{1}{3} \\in (0; 1)$ nên bất phương trình tương đương với $x - 1 < \\left(\\dfrac{1}{3}\\right)^{-2} = 9 \\Leftrightarrow x < 10$. Kết hợp điều kiện ta được $S = (1; 10)$.",
            ),
            tf4(
                "hieu",
                "Cho hai số thực dương $a, b$ thỏa mãn $a \\neq 1$ và $\\log_a b = 3$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Giá trị của $\\log_a(a^2 b)$ bằng $5$.",
                    "Giá trị của $\\log_b a$ bằng $-3$.",
                    "Giá trị của $\\log_a\\left(\\dfrac{\\sqrt{b}}{a}\\right)$ bằng $\\dfrac{1}{2}$.",
                    "Giá trị của $\\log_{a^2}(a b^3)$ bằng $5$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $\\log_a(a^2 b) = \\log_a(a^2) + \\log_a b = 2 + 3 = 5$.\n"
                "b) Sai vì $\\log_b a = \\dfrac{1}{\\log_a b} = \\dfrac{1}{3} \\neq -3$.\n"
                "c) Đúng vì $\\log_a\\left(\\dfrac{\\sqrt{b}}{a}\\right) = \\dfrac{1}{2}\\log_a b - \\log_a a = \\dfrac{3}{2} - 1 = \\dfrac{1}{2}$.\n"
                "d) Đúng vì $\\log_{a^2}(a b^3) = \\dfrac{1}{2}(\\log_a a + 3\\log_a b) = \\dfrac{1}{2}(1 + 3 \\cdot 3) = 5$.",
            ),
            tf4(
                "hieu",
                "Cho hàm số $f(x) = 2^{x^2 - 3x + 2}$ và hàm số $g(x) = \\log_2(x + 2)$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Tập xác định của hàm số $g(x)$ là khoảng $(-2; +\\infty)$.",
                    "Đồ thị hàm số $g(x)$ đi qua điểm $A(0; 2)$.",
                    "Phương trình $f(x) = 1$ có đúng $2$ nghiệm phân biệt là $x = 1$ và $x = 2$.",
                    "Tập nghiệm của bất phương trình $g(x) \\le 3$ là nửa khoảng $(-2; 6]$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $g(x)$ xác định khi $x + 2 > 0 \\Leftrightarrow x > -2$.\n"
                "b) Sai vì $g(0) = \\log_2 2 = 1 \\neq 2$, nên đồ thị đi qua $(0; 1)$ chứ không đi qua $(0; 2)$.\n"
                "c) Đúng vì $f(x) = 1 \\Leftrightarrow 2^{x^2 - 3x + 2} = 2^0 \\Leftrightarrow x^2 - 3x + 2 = 0 \\Leftrightarrow x = 1$ hoặc $x = 2$.\n"
                "d) Đúng vì với điều kiện $x > -2$, ta có $\\log_2(x + 2) \\le 3 \\Leftrightarrow x + 2 \\le 2^3 = 8 \\Leftrightarrow x \\le 6$. Vậy tập nghiệm là $(-2; 6]$.",
            ),
            mcq(
                "vandung",
                "Bác An gửi tiết kiệm $100$ triệu đồng vào ngân hàng theo hình thức lãi kép kì hạn $1$ năm với lãi suất $8\\%$ một năm. Nếu không rút tiền ra khỏi ngân hàng thì sau ít nhất bao nhiêu năm (số nguyên năm) tổng số tiền cả vốn lẫn lãi của bác An vượt quá $150$ triệu đồng?",
                ["$6$ năm", "$5$ năm", "$7$ năm", "$4$ năm"],
                0,
                "Sau $n$ năm, số tiền là $A = 100(1 + 0{,}08)^n = 100 \\cdot (1{,}08)^n$. Ta cần $100 \\cdot (1{,}08)^n > 150 \\Leftrightarrow (1{,}08)^n > 1{,}5 \\Leftrightarrow n > \\log_{1{,}08}(1{,}5) \\approx 5{,}27$. Vì $n \\in \\mathbb{N}^*$ nên cần ít nhất $6$ năm.",
            ),
            short(
                "vandung",
                "Tổng tất cả các nghiệm thực của phương trình $\\log_2(x - 1) + \\log_2(x - 3) = 3$ bằng bao nhiêu?",
                ["5"],
                "Điều kiện: $\\begin{cases} x - 1 > 0 \\\\ x - 3 > 0 \\end{cases} \\Leftrightarrow x > 3$. Phương trình tương đương với $\\log_2[(x - 1)(x - 3)] = 3 \\Leftrightarrow x^2 - 4x + 3 = 8 \\Leftrightarrow x^2 - 4x - 5 = 0 \\Leftrightarrow x = 5$ (thỏa mãn) hoặc $x = -1$ (loại). Vậy phương trình có nghiệm duy nhất $x = 5$.",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG VII. QUAN HỆ VUÔNG GÓC TRONG KHÔNG GIAN
    # =========================================================================
    {
        "topic": "l11-ch07-quan-he-vuong-goc-trong-khong-gian",
        "title": "Chương VII. Quan hệ vuông góc trong không gian",
        "icon": "📐",
        "description": (
            "Nghiên cứu góc và quan hệ vuông góc giữa các đường thẳng và mặt phẳng trong không gian, "
            "phép chiếu vuông góc, góc nhị diện, cách xác định và tính khoảng cách cùng công thức "
            "tính thể tích của khối chóp, khối chóp cụt đều, khối lăng trụ và khối hộp."
        ),
        "requirements": [
            "Nhận biết được khái niệm góc giữa hai đường thẳng và chứng minh được hai đường thẳng vuông góc trong không gian.",
            "Nhận biết và xác định được điều kiện để đường thẳng vuông góc với mặt phẳng; giải thích được định lí ba đường vuông góc và mối liên hệ giữa tính song song và tính vuông góc.",
            "Nhận biết được phép chiếu vuông góc; xác định và tính được góc giữa đường thẳng và mặt phẳng trong những trường hợp đơn giản.",
            "Nhận biết được hai mặt phẳng vuông góc, góc nhị diện và góc phẳng nhị diện; giải thích được tính chất cơ bản của hình lăng trụ đứng, lăng trụ đều, hình hộp đứng, hình hộp chữ nhật, hình lập phương, hình chóp đều, hình chóp cụt đều.",
            "Xác định và tính được khoảng cách từ một điểm đến một đường thẳng, đến một mặt phẳng; khoảng cách giữa các đường thẳng và mặt phẳng song song; khoảng cách giữa hai đường thẳng chéo nhau trong những trường hợp đơn giản.",
            "Nhận biết được công thức và tính được thể tích của khối chóp, khối chóp cụt đều, khối lăng trụ, khối hộp và vận dụng vào thực tiễn.",
        ],
        "definition": (
            "Chương học xây dựng hệ thống đo lường hình học trong không gian dựa trên quan hệ vuông góc: "
            "từ góc và tính vuông góc giữa đường thẳng với đường thẳng, đường thẳng với mặt phẳng, mặt phẳng với mặt phẳng (góc nhị diện) "
            "đến việc tính khoảng cách và thể tích các khối đa diện."
        ),
        "theory": (
            "### Bài 22. Hai đường thẳng vuông góc\n"
            "- **Góc giữa hai đường thẳng trong không gian:** Góc giữa hai đường thẳng $a$ và $b$ là góc giữa hai đường thẳng $a'$ và $b'$ cùng đi qua một điểm $O$ bất kì và lần lượt song song (hoặc trùng) với $a$ và $b$. Số đo góc $(a, b)$ luôn thỏa mãn $0^\\circ \\le (a, b) \\le 90^\\circ$.\n"
            "- **Hai đường thẳng vuông góc:** $a \\perp b \\Leftrightarrow (a, b) = 90^\\circ$. Hai đường thẳng vuông góc có thể cắt nhau hoặc chéo nhau.\n\n"
            "### Bài 23. Đường thẳng vuông góc với mặt phẳng\n"
            "- **Định nghĩa và điều kiện:** Đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ nếu $d$ vuông góc với mọi đường thẳng $a$ nằm trong $(\\alpha)$. *Điều kiện đủ:* Nếu $d$ vuông góc với hai đường thẳng cắt nhau nằm trong $(\\alpha)$ thì $d \\perp (\\alpha)$.\n"
            "- **Tính chất:** Có duy nhất một mặt phẳng đi qua một điểm và vuông góc với một đường thẳng cho trước; có duy nhất một đường thẳng đi qua một điểm và vuông góc với một mặt phẳng cho trước.\n\n"
            "### Bài 24. Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng\n"
            "- **Góc giữa đường thẳng và mặt phẳng:** Nếu $d \\perp (\\alpha)$ thì góc $(d, (\\alpha)) = 90^\\circ$. Nếu $d$ không vuông góc với $(\\alpha)$ thì góc giữa $d$ và $(\\alpha)$ là góc giữa $d$ và hình chiếu vuông góc $d'$ của nó trên $(\\alpha)$ (với $0^\\circ \\le \\varphi < 90^\\circ$).\n"
            "- **Định lí ba đường vuông góc:** Cho đường thẳng $a$ nằm trong $(\\alpha)$ và đường thẳng $b$ không nằm trong $(\\alpha)$ đồng thời không vuông góc với $(\\alpha)$. Gọi $b'$ là hình chiếu vuông góc của $b$ trên $(\\alpha)$. Khi đó $a \\perp b \\Leftrightarrow a \\perp b'$.\n\n"
            "### Bài 25. Hai mặt phẳng vuông góc\n"
            "- **Góc nhị diện:** Hình gồm hai nửa mặt phẳng $(P), (Q)$ có chung bờ $d$ được gọi là một góc nhị diện, kí hiệu $[P, d, Q]$. Góc $\\widehat{xOy}$ tạo bởi hai tia $Ox \\subset (P), Oy \\subset (Q)$ cùng vuông góc với $d$ tại $O$ gọi là *góc phẳng nhị diện* (số đo từ $0^\\circ$ đến $180^\\circ$).\n"
            "- **Hai mặt phẳng vuông góc:** $(\\alpha) \\perp (\\beta)$ nếu mặt phẳng này chứa một đường thẳng vuông góc với mặt phẳng kia. Nếu hai mặt phẳng cắt nhau cùng vuông góc với mặt phẳng thứ ba thì giao tuyến của chúng vuông góc với mặt phẳng thứ ba đó.\n"
            "- **Các hình khối đặc biệt:** Hình lăng trụ đứng (cạnh bên vuông góc với đáy), lăng trụ đều (lăng trụ đứng có đáy là đa giác đều), hình hộp chữ nhật, hình lập phương, hình chóp đều (đáy là đa giác đều và chân đường cao trùng với tâm của đáy), hình chóp cụt đều.\n\n"
            "### Bài 26. Khoảng cách\n"
            "- **Khoảng cách từ điểm đến mặt phẳng:** $d(M, (\\alpha)) = MH$ với $H$ là hình chiếu vuông góc của $M$ trên $(\\alpha)$.\n"
            "- **Khoảng cách giữa hai đường thẳng chéo nhau:** Là độ dài đoạn vuông góc chung $MN$ của hai đường thẳng đó, hoặc bằng khoảng cách từ một đường thẳng đến mặt phẳng song song chứa đường thẳng kia.\n\n"
            "### Bài 27. Thể tích\n"
            "- **Thể tích khối chóp, khối chóp cụt đều và khối lăng trụ:** Được xác định qua diện tích đáy $S$ và chiều cao $h$ (khoảng cách giữa hai đáy hoặc từ đỉnh đến mặt đáy)."
        ),
        "formulas": [
            G(
                "Điều kiện vuông góc và góc trong không gian",
                F("Đường thẳng vuông góc mặt phẳng", "$\\begin{cases} a, b \\subset (\\alpha), \\ a \\cap b = I \\\\ d \\perp a, \\ d \\perp b \\end{cases} \\Rightarrow d \\perp (\\alpha)$"),
                F("Góc giữa đường thẳng và mặt phẳng", "$(d, (\\alpha)) = (d, d') \\text{ với } d' \\text{ là hình chiếu vuông góc của } d \\text{ trên } (\\alpha)$"),
                F("Hai mặt phẳng vuông góc", "$\\begin{cases} d \\subset (\\beta) \\\\ d \\perp (\\alpha) \\end{cases} \\Rightarrow (\\alpha) \\perp (\\beta)$"),
            ),
            G(
                "Hệ thức tính khoảng cách từ chân đường cao H",
                F("Khoảng cách từ chân đường cao đến mặt bên", "$\\dfrac{1}{d(H, (SBC))^2} = \\dfrac{1}{SH^2} + \\dfrac{1}{HK^2}$"),
                F("Đổi khoảng cách qua giao điểm I", "$\\dfrac{d(A, (P))}{d(B, (P))} = \\dfrac{IA}{IB} \\quad (AB \\cap (P) = I)$"),
            ),
            G(
                "Công thức thể tích khối đa diện",
                F("Thể tích khối chóp", "$V = \\dfrac{1}{3} S \\cdot h$"),
                F("Thể tích khối lăng trụ", "$V = S \\cdot h$"),
                F("Thể tích khối hộp chữ nhật và khối lập phương", "$V_{\\text{hộp}} = a \\cdot b \\cdot c, \\quad V_{\\text{lập phương}} = a^3$"),
                F("Thể tích khối chóp cụt đều", "$V = \\dfrac{1}{3} h \\left(S + \\sqrt{S \\cdot S'} + S'\\right)$"),
            ),
        ],
        "example": (
            "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, cạnh bên $SA \\perp (ABCD)$ và $SA = a\\sqrt{3}$.\n"
            "a) Chứng minh $BC \\perp (SAB)$ và tính góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$.\n"
            "b) Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBD)$ và thể tích khối chóp $S.ABCD$."
        ),
        "example_answer": (
            "**a) Chứng minh $BC \\perp (SAB)$ và tính góc $(SC, (ABCD))$:**\n"
            "- Vì $ABCD$ là hình vuông nên $BC \\perp AB$. Mặt khác $SA \\perp (ABCD) \\Rightarrow SA \\perp BC$. Do $AB \\cap SA = A$ trong $(SAB)$ nên $BC \\perp (SAB)$.\n"
            "- Vì $SA \\perp (ABCD)$ tại $A$ nên $AC$ là hình chiếu vuông góc của $SC$ trên $(ABCD)$. Suy ra $(SC, (ABCD)) = (SC, AC) = \\widehat{SCA}$.\n"
            "- Trong $\\triangle SAC$ vuông tại $A$, có $AC = a\\sqrt{2}$, $SA = a\\sqrt{3}$:\n"
            "  $$\\tan\\widehat{SCA} = \\dfrac{SA}{AC} = \\dfrac{a\\sqrt{3}}{a\\sqrt{2}} = \\sqrt{\\dfrac{3}{2}}$$\n\n"
            "**b) Tính $d(A, (SBD))$ và thể tích $V_{S.ABCD}$:**\n"
            "- Gọi $O = AC \\cap BD$. Vì $ABCD$ là hình vuông nên $AO \\perp BD$ và $AO = \\dfrac{a\\sqrt{2}}{2}$. Kẻ $AH \\perp SO$ tại $H$, khi đó $AH \\perp (SBD)$ nên $d(A, (SBD)) = AH$:\n"
            "  $$\\dfrac{1}{AH^2} = \\dfrac{1}{SA^2} + \\dfrac{1}{AO^2} = \\dfrac{1}{3a^2} + \\dfrac{2}{a^2} = \\dfrac{7}{3a^2} \\Rightarrow AH = \\dfrac{a\\sqrt{21}}{7}$$\n"
            "- Thể tích khối chóp $S.ABCD$ là:\n"
            "  $$V_{S.ABCD} = \\dfrac{1}{3} S_{ABCD} \\cdot SA = \\dfrac{1}{3} a^2 \\cdot a\\sqrt{3} = \\dfrac{a^3\\sqrt{3}}{3}$$"
        ),
        "real_life": (
            "Quan hệ vuông góc, khoảng cách và thể tích được ứng dụng trực tiếp trong xây dựng (dây dọi kiểm tra tường thẳng đứng, "
            "độ dốc mái nhà chính là góc phẳng nhị diện), tính dung tích bể chứa, thể tích kim tự tháp và thiết kế cơ khí."
        ),
        "quiz": [
            mcq(
                "biet",
                "Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $AB$ và $B'C'$ bằng:",
                ["$90^\\circ$", "$60^\\circ$", "$45^\\circ$", "$30^\\circ$"],
                0,
                "Vì $B'C' \\parallel BC$ nên $(AB, B'C') = (AB, BC) = \\widehat{ABC} = 90^\\circ$.",
            ),
            mcq(
                "biet",
                "Đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ khi và chỉ khi:",
                [
                    "$d$ vuông góc với hai đường thẳng cắt nhau nằm trong $(\\alpha)$",
                    "$d$ vuông góc với hai đường thẳng song song nằm trong $(\\alpha)$",
                    "$d$ vuông góc với một đường thẳng bất kì nằm trong $(\\alpha)$",
                    "$d$ song song với một đường thẳng nằm trong $(\\alpha)$",
                ],
                0,
                "Theo định lí điều kiện để đường thẳng vuông góc với mặt phẳng, $d \\perp (\\alpha)$ khi và chỉ khi $d$ vuông góc với hai đường thẳng cắt nhau cùng nằm trong $(\\alpha)$.",
            ),
            mcq(
                "biet",
                "Công thức tính thể tích $V$ của khối chóp có diện tích đáy $S$ và chiều cao $h$ là:",
                [
                    "$V = \\dfrac{1}{3} S \\cdot h$",
                    "$V = S \\cdot h$",
                    "$V = \\dfrac{1}{2} S \\cdot h$",
                    "$V = \\dfrac{1}{6} S \\cdot h$",
                ],
                0,
                "Thể tích của một khối chóp bằng một phần ba tích của diện tích mặt đáy và chiều cao: $V = \\dfrac{1}{3} S \\cdot h$.",
            ),
            mcq(
                "biet",
                "Cho khối lăng trụ có diện tích đáy $S = 12\\text{ cm}^2$ và chiều cao $h = 5\\text{ cm}$. Thể tích của khối lăng trụ đó bằng:",
                [
                    "$60\\text{ cm}^3$",
                    "$20\\text{ cm}^3$",
                    "$30\\text{ cm}^3$",
                    "$17\\text{ cm}^3$",
                ],
                0,
                "Áp dụng công thức thể tích khối lăng trụ: $V = S \\cdot h = 12 \\cdot 5 = 60\\text{ cm}^3$.",
            ),
            mcq(
                "hieu",
                "Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, tam giác $ABC$ vuông tại $B$, $AB = a, BC = a\\sqrt{3}$ và $SA = 2a$. Góc giữa đường thẳng $SC$ và mặt phẳng $(ABC)$ bằng:",
                ["$45^\\circ$", "$60^\\circ$", "$30^\\circ$", "$90^\\circ$"],
                0,
                "Vì $SA \\perp (ABC)$ nên $AC$ là hình chiếu vuông góc của $SC$ trên $(ABC)$, suy ra $(SC, (ABC)) = \\widehat{SCA}$. Trong $\\triangle ABC$ vuông tại $B$: $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{a^2 + 3a^2} = 2a$. Do đó $\\tan\\widehat{SCA} = \\dfrac{SA}{AC} = \\dfrac{2a}{2a} = 1 \\Rightarrow \\widehat{SCA} = 45^\\circ$.",
            ),
            mcq(
                "hieu",
                "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = a, AD = 2a$, cạnh bên $SA \\perp (ABCD)$ và $SA = a$. Khoảng cách từ điểm $A$ đến mặt phẳng $(SCD)$ bằng:",
                [
                    "$\\dfrac{2a\\sqrt{5}}{5}$",
                    "$\\dfrac{a\\sqrt{5}}{5}$",
                    "$\\dfrac{a\\sqrt{2}}{2}$",
                    "$a\\sqrt{2}$",
                ],
                0,
                "Ta có $CD \\perp AD$ và $CD \\perp SA \\Rightarrow CD \\perp (SAD)$. Kẻ $AH \\perp SD$ tại $H$ thì $AH \\perp (SCD)$, nên $d(A, (SCD)) = AH = \\dfrac{SA \\cdot AD}{\\sqrt{SA^2 + AD^2}} = \\dfrac{a \\cdot 2a}{\\sqrt{a^2 + 4a^2}} = \\dfrac{2a\\sqrt{5}}{5}$.",
            ),
            tf4(
                "hieu",
                "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, $SA \\perp (ABCD)$ và $SA = a$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Đường thẳng $BC$ vuông góc với mặt phẳng $(SAB)$.",
                    "Góc giữa đường thẳng $SB$ và mặt phẳng $(ABCD)$ bằng $60^\\circ$.",
                    "Hai mặt phẳng $(SAC)$ và $(SBD)$ vuông góc với nhau.",
                    "Thể tích của khối chóp $S.ABCD$ bằng $\\dfrac{a^3}{3}$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $BC \\perp AB$ và $BC \\perp SA \\Rightarrow BC \\perp (SAB)$.\n"
                "b) Sai vì $(SB, (ABCD)) = \\widehat{SBA}$ mà $\\tan\\widehat{SBA} = \\dfrac{SA}{AB} = 1 \\Rightarrow \\widehat{SBA} = 45^\\circ \\neq 60^\\circ$.\n"
                "c) Đúng vì $BD \\perp AC$ và $BD \\perp SA \\Rightarrow BD \\perp (SAC)$, mà $BD \\subset (SBD)$ nên $(SBD) \\perp (SAC)$.\n"
                "d) Đúng vì $V_{S.ABCD} = \\dfrac{1}{3} S_{ABCD} \\cdot SA = \\dfrac{1}{3} a^2 \\cdot a = \\dfrac{a^3}{3}$.",
            ),
            tf4(
                "hieu",
                "Cho hình lăng trụ đều $ABC.A'B'C'$ có tất cả các cạnh (cạnh đáy và cạnh bên) đều bằng $a$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Cạnh bên $AA'$ vuông góc với mặt phẳng đáy $(ABC)$.",
                    "Diện tích đáy tam giác đều $ABC$ bằng $\\dfrac{a^2\\sqrt{3}}{2}$.",
                    "Khoảng cách giữa hai đường thẳng chéo nhau $AA'$ và $BC$ bằng $\\dfrac{a\\sqrt{3}}{2}$.",
                    "Thể tích của khối lăng trụ $ABC.A'B'C'$ bằng $\\dfrac{a^3\\sqrt{3}}{4}$.",
                ],
                [True, False, True, True],
                "a) Đúng vì lăng trụ đều là lăng trụ đứng nên cạnh bên vuông góc với mặt đáy.\n"
                "b) Sai vì diện tích tam giác đều cạnh $a$ là $S_{ABC} = \\dfrac{a^2\\sqrt{3}}{4} \\neq \\dfrac{a^2\\sqrt{3}}{2}$.\n"
                "c) Đúng vì gọi $M$ là trung điểm $BC$, ta có $AM \\perp BC$ và $AM \\perp AA'$ nên $AM$ là đoạn vuông góc chung của $AA'$ và $BC$, với $AM = \\dfrac{a\\sqrt{3}}{2}$.\n"
                "d) Đúng vì $V = S_{ABC} \\cdot AA' = \\dfrac{a^2\\sqrt{3}}{4} \\cdot a = \\dfrac{a^3\\sqrt{3}}{4}$.",
            ),
            mcq(
                "vandung",
                "Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $2a$ và cạnh bên bằng $a\\sqrt{6}$. Thể tích của khối chóp $S.ABCD$ bằng:",
                [
                    "$\\dfrac{8a^3}{3}$",
                    "$\\dfrac{4a^3}{3}$",
                    "$8a^3$",
                    "$\\dfrac{4a^3\\sqrt{2}}{3}$",
                ],
                0,
                "Gọi $O$ là tâm hình vuông $ABCD$ cạnh $2a$, ta có $SO \\perp (ABCD)$ và $OA = \\dfrac{2a\\sqrt{2}}{2} = a\\sqrt{2}$. Chiều cao khối chóp là $SO = \\sqrt{SA^2 - OA^2} = \\sqrt{6a^2 - 2a^2} = 2a$. Vậy $V = \\dfrac{1}{3} S_{ABCD} \\cdot SO = \\dfrac{1}{3} (2a)^2 \\cdot 2a = \\dfrac{8a^3}{3}$.",
            ),
            short(
                "vandung",
                "Một khối chóp cụt tứ giác đều có cạnh đáy lớn bằng $6\\text{ cm}$, cạnh đáy nhỏ bằng $3\\text{ cm}$ và chiều cao bằng $4\\text{ cm}$. Tính thể tích của khối chóp cụt đều đó (đơn vị: $\\text{cm}^3$).",
                ["84"],
                "Diện tích đáy lớn là $S = 6^2 = 36\\text{ cm}^2$, diện tích đáy nhỏ là $S' = 3^2 = 9\\text{ cm}^2$. Áp dụng công thức thể tích khối chóp cụt đều: $V = \\dfrac{1}{3} h (S + \\sqrt{S \\cdot S'} + S') = \\dfrac{1}{3} \\cdot 4 \\cdot (36 + \\sqrt{36 \\cdot 9} + 9) = \\dfrac{4}{3} \\cdot (36 + 18 + 9) = \\dfrac{4}{3} \\cdot 63 = 84\\text{ cm}^3$.",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG VIII. CÁC QUY TẮC TÍNH XÁC SUẤT
    # =========================================================================
    {
        "topic": "l11-ch08-cac-quy-tac-tinh-xac-suat",
        "title": "Chương VIII. Các quy tắc tính xác suất",
        "icon": "🎲",
        "description": (
            "Tìm hiểu biến cố hợp, biến cố giao, hai biến cố xung khắc và hai biến cố độc lập; "
            "vận dụng công thức cộng xác suất và công thức nhân xác suất cho hai biến cố độc lập "
            "để giải các bài toán xác suất thực tiễn."
        ),
        "requirements": [
            "Nhận biết được một số khái niệm về xác suất cổ điển: hợp và giao các biến cố; biến cố xung khắc; biến cố độc lập.",
            "Tính được xác suất của biến cố hợp bằng cách sử dụng công thức cộng xác suất (cho cả hai biến cố xung khắc và hai biến cố bất kì).",
            "Tính được xác suất của biến cố giao bằng cách sử dụng công thức nhân xác suất cho trường hợp hai biến cố độc lập.",
            "Tính được xác suất của biến cố trong một số bài toán đơn giản bằng phương pháp tổ hợp và sơ đồ hình cây.",
        ],
        "definition": (
            "Chương học phát triển các phép toán trên biến cố (hợp $A \\cup B$, giao $A \\cap B$ hay $AB$, biến cố đối $\\bar{A}$) "
            "và thiết lập hai quy tắc nền tảng để tính xác suất mà không cần đếm trực tiếp toàn bộ không gian mẫu: "
            "công thức cộng xác suất cho biến cố hợp và công thức nhân xác suất cho các biến cố độc lập."
        ),
        "theory": (
            "### Bài 28. Biến cố hợp, biến cố giao, biến cố độc lập\n"
            "- **Biến cố hợp ($A \\cup B$):** Cho hai biến cố $A$ và $B$ cùng liên quan đến một phép thử. Biến cố \"*$A$ xảy ra hoặc $B$ xảy ra*\" được gọi là biến cố hợp của $A$ và $B$, kí hiệu $A \\cup B$.\n"
            "- **Biến cố giao ($A \\cap B$ hoặc $AB$):** Biến cố \"*Cả $A$ và $B$ đều xảy ra*\" được gọi là biến cố giao của $A$ và $B$, kí hiệu $A \\cap B$ hay $AB$.\n"
            "- **Hai biến cố xung khắc:** Hai biến cố $A$ và $B$ được gọi là *xung khắc* nếu chúng không đồng thời xảy ra trong cùng một lần thực hiện phép thử, tức là $A \\cap B = \\varnothing$.\n"
            "- **Hai biến cố độc lập:** Hai biến cố $A$ và $B$ được gọi là *độc lập* nếu việc xảy ra hay không xảy ra của biến cố này không làm ảnh hưởng tới xác suất xảy ra của biến cố kia. Nếu $A, B$ độc lập thì các cặp $(A, \\bar{B})$, $(\\bar{A}, B)$, $(\\bar{A}, \\bar{B})$ cũng độc lập.\n\n"
            "### Bài 29. Công thức cộng xác suất\n"
            "- **Công thức cộng cho hai biến cố xung khắc:** Nếu $A$ và $B$ là hai biến cố xung khắc ($A \\cap B = \\varnothing$) thì:\n"
            "  $$P(A \\cup B) = P(A) + P(B)$$\n"
            "- **Công thức cộng tổng quát:** Với hai biến cố $A$ và $B$ bất kì, ta luôn có:\n"
            "  $$P(A \\cup B) = P(A) + P(B) - P(AB)$$\n\n"
            "### Bài 30. Công thức nhân xác suất cho hai biến cố độc lập\n"
            "- **Công thức nhân:** Nếu hai biến cố $A$ và $B$ độc lập với nhau thì:\n"
            "  $$P(AB) = P(A) \\cdot P(B)$$\n"
            "- **Nhận biết tính độc lập qua xác suất:** Ngược lại, nếu $P(AB) \\neq P(A) \\cdot P(B)$ thì hai biến cố $A$ và $B$ không độc lập (phụ thuộc).\n"
            "- **Phương pháp biến cố đối:** Để tính xác suất biến cố \"*có ít nhất một biến cố xảy ra*\", ta thường xét biến cố đối \"*không có biến cố nào xảy ra*\": $P(A \\cup B) = 1 - P(\\bar{A}\\bar{B})$."
        ),
        "formulas": [
            G(
                "Xác suất cổ điển và biến cố đối",
                F("Định nghĩa cổ điển", "$P(A) = \\dfrac{n(A)}{n(\\Omega)}$"),
                F("Xác suất biến cố đối", "$P(\\bar{A}) = 1 - P(A)$"),
            ),
            G(
                "Công thức cộng xác suất",
                F("Hai biến cố xung khắc", "$P(A \\cup B) = P(A) + P(B)$"),
                F("Hai biến cố bất kì", "$P(A \\cup B) = P(A) + P(B) - P(AB)$"),
            ),
            G(
                "Công thức nhân xác suất (A, B độc lập)",
                F("Xác suất biến cố giao", "$P(AB) = P(A) \\cdot P(B)$"),
                F("Hệ quả với biến cố đối", "$P(A \\cup B) = 1 - P(\\bar{A}) \\cdot P(\\bar{B})$"),
            ),
        ],
        "example": (
            "Hai xạ thủ $A$ và $B$ cùng bắn độc lập vào một mục tiêu, mỗi người bắn một viên đạn. Xác suất bắn trúng mục tiêu của xạ thủ $A$ là $0{,}8$ và của xạ thủ $B$ là $0{,}7$.\n"
            "a) Tính xác suất để cả hai xạ thủ đều bắn trúng mục tiêu.\n"
            "b) Tính xác suất để mục tiêu bị bắn trúng (tức là có ít nhất một xạ thủ bắn trúng)."
        ),
        "example_answer": (
            "Gọi $A$ là biến cố \"Xạ thủ $A$ bắn trúng mục tiêu\" và $B$ là biến cố \"Xạ thủ $B$ bắn trúng mục tiêu\". Theo giả thiết, $A$ và $B$ là hai biến cố độc lập với $P(A) = 0{,}8$ và $P(B) = 0{,}7$.\n\n"
            "**a) Xác suất để cả hai xạ thủ đều bắn trúng mục tiêu:**\n"
            "- Biến cố cả hai cùng bắn trúng là biến cố giao $AB$. Áp dụng công thức nhân xác suất cho hai biến cố độc lập:\n"
            "  $$P(AB) = P(A) \\cdot P(B) = 0{,}8 \\cdot 0{,}7 = 0{,}56$$\n\n"
            "**b) Xác suất để mục tiêu bị bắn trúng:**\n"
            "- Biến cố mục tiêu bị bắn trúng là biến cố hợp $A \\cup B$. Áp dụng công thức cộng xác suất:\n"
            "  $$P(A \\cup B) = P(A) + P(B) - P(AB) = 0{,}8 + 0{,}7 - 0{,}56 = 0{,}94$$\n"
            "*(Cách 2: Dùng biến cố đối $P(A \\cup B) = 1 - P(\\bar{A})P(\\bar{B}) = 1 - 0{,}2 \\cdot 0{,}3 = 0{,}94$)*."
        ),
        "real_life": (
            "Các quy tắc tính xác suất được ứng dụng trực tiếp trong đánh giá độ tin cậy của hệ thống kĩ thuật (mạch điện mắc nối tiếp "
            "hoặc song song), tính phí bảo hiểm, dự báo rủi ro tài chính, kiểm định chất lượng sản phẩm và di truyền học Mendel."
        ),
        "quiz": [
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ xung khắc với nhau, biết $P(A) = 0{,}3$ và $P(B) = 0{,}4$. Giá trị của $P(A \\cup B)$ bằng:",
                ["$0{,}7$", "$0{,}12$", "$0{,}58$", "$0{,}1$"],
                0,
                "Vì $A$ và $B$ là hai biến cố xung khắc nên $P(A \\cup B) = P(A) + P(B) = 0{,}3 + 0{,}4 = 0{,}7$.",
            ),
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ độc lập với nhau, biết $P(A) = 0{,}6$ và $P(B) = 0{,}5$. Giá trị của $P(AB)$ bằng:",
                ["$0{,}3$", "$0{,}8$", "$0{,}1$", "$1{,}1$"],
                0,
                "Vì $A$ và $B$ độc lập nên theo công thức nhân xác suất: $P(AB) = P(A) \\cdot P(B) = 0{,}6 \\cdot 0{,}5 = 0{,}3$.",
            ),
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ bất kì. Công thức cộng xác suất nào sau đây luôn đúng?",
                [
                    "$P(A \\cup B) = P(A) + P(B) - P(AB)$",
                    "$P(A \\cup B) = P(A) + P(B)$",
                    "$P(A \\cup B) = P(A) \\cdot P(B)$",
                    "$P(A \\cup B) = P(A) + P(B) + P(AB)$",
                ],
                0,
                "Theo định lí công thức cộng xác suất cho hai biến cố bất kì, $P(A \\cup B) = P(A) + P(B) - P(AB)$.",
            ),
            mcq(
                "biet",
                "Nếu biến cố $A$ có xác suất $P(A) = 0{,}25$ thì biến cố đối $\\bar{A}$ có xác suất $P(\\bar{A})$ bằng:",
                ["$0{,}75$", "$0{,}25$", "$0{,}5$", "$0{,}85$"],
                0,
                "Ta có $P(\\bar{A}) = 1 - P(A) = 1 - 0{,}25 = 0{,}75$.",
            ),
            mcq(
                "hieu",
                "Cho hai biến cố $A$ và $B$ có $P(A) = 0{,}5$, $P(B) = 0{,}6$ và $P(AB) = 0{,}2$. Xác suất của biến cố hợp $P(A \\cup B)$ bằng:",
                ["$0{,}9$", "$0{,}8$", "$0{,}7$", "$1{,}1$"],
                0,
                "Áp dụng công thức cộng xác suất: $P(A \\cup B) = P(A) + P(B) - P(AB) = 0{,}5 + 0{,}6 - 0{,}2 = 0{,}9$.",
            ),
            mcq(
                "hieu",
                "Một hộp có $10$ tấm thẻ được đánh số từ $1$ đến $10$. Rút ngẫu nhiên $1$ tấm thẻ. Xác suất để rút được tấm thẻ ghi số chia hết cho $2$ hoặc chia hết cho $5$ là:",
                [
                    "$\\dfrac{3}{5}$",
                    "$\\dfrac{7}{10}$",
                    "$\\dfrac{1}{2}$",
                    "$\\dfrac{2}{5}$",
                ],
                0,
                "Gọi $A$: \"Thẻ chia hết cho $2$\" $\\Rightarrow A = \\{2; 4; 6; 8; 10\\}$, $P(A) = \\dfrac{5}{10}$. Gọi $B$: \"Thẻ chia hết cho $5$\" $\\Rightarrow B = \\{5; 10\\}$, $P(B) = \\dfrac{2}{10}$. Giao $AB = \\{10\\} \\Rightarrow P(AB) = \\dfrac{1}{10}$. Vậy $P(A \\cup B) = \\dfrac{5}{10} + \\dfrac{2}{10} - \\dfrac{1}{10} = \\dfrac{6}{10} = \\dfrac{3}{5}$.",
            ),
            tf4(
                "hieu",
                "Cho hai biến cố độc lập $A$ và $B$ với $P(A) = 0{,}4$ và $P(B) = 0{,}5$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Xác suất của biến cố đối $\\bar{A}$ là $P(\\bar{A}) = 0{,}6$.",
                    "Hai biến cố $A$ và $B$ là hai biến cố xung khắc.",
                    "Xác suất của biến cố giao $AB$ là $P(AB) = 0{,}2$.",
                    "Xác suất của biến cố hợp $A \\cup B$ là $P(A \\cup B) = 0{,}7$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $P(\\bar{A}) = 1 - P(A) = 1 - 0{,}4 = 0{,}6$.\n"
                "b) Sai vì $A, B$ độc lập nên $P(AB) = P(A)P(B) = 0{,}2 \\neq 0$, do đó $A \\cap B \\neq \\varnothing$ (không xung khắc).\n"
                "c) Đúng vì $P(AB) = 0{,}4 \\cdot 0{,}5 = 0{,}2$.\n"
                "d) Đúng vì $P(A \\cup B) = P(A) + P(B) - P(AB) = 0{,}4 + 0{,}5 - 0{,}2 = 0{,}7$.",
            ),
            tf4(
                "hieu",
                "Một lớp học có $40$ học sinh, trong đó có $25$ học sinh giỏi Toán, $20$ học sinh giỏi Văn và $10$ học sinh giỏi cả hai môn Toán và Văn. Chọn ngẫu nhiên $1$ học sinh trong lớp. Gọi $A$ là biến cố \"Học sinh được chọn giỏi Toán\" và $B$ là biến cố \"Học sinh được chọn giỏi Văn\". Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Xác suất của biến cố $A$ là $P(A) = \\dfrac{5}{8}$.",
                    "Xác suất của biến cố giao $AB$ là $P(AB) = \\dfrac{5}{16}$.",
                    "Xác suất để học sinh được chọn giỏi ít nhất một trong hai môn Toán hoặc Văn là $\\dfrac{7}{8}$.",
                    "Xác suất để học sinh được chọn không giỏi cả hai môn Toán và Văn là $\\dfrac{1}{8}$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $P(A) = \\dfrac{25}{40} = \\dfrac{5}{8}$.\n"
                "b) Sai vì có $10$ học sinh giỏi cả hai môn nên $P(AB) = \\dfrac{10}{40} = \\dfrac{1}{4} = \\dfrac{4}{16} \\neq \\dfrac{5}{16}$.\n"
                "c) Đúng vì $P(A \\cup B) = P(A) + P(B) - P(AB) = \\dfrac{25}{40} + \\dfrac{20}{40} - \\dfrac{10}{40} = \\dfrac{35}{40} = \\dfrac{7}{8}$.\n"
                "d) Đúng vì biến cố không giỏi môn nào là biến cố đối của $A \\cup B$, có xác suất $1 - \\dfrac{7}{8} = \\dfrac{1}{8}$.",
            ),
            mcq(
                "vandung",
                "Một hệ thống bảo vệ gồm $2$ rơ-le hoạt động độc lập. Xác suất hoạt động tốt của rơ-le thứ nhất là $0{,}9$ và của rơ-le thứ hai là $0{,}8$. Hệ thống hoạt động tốt nếu có ít nhất một rơ-le hoạt động tốt. Xác suất để hệ thống hoạt động tốt là:",
                ["$0{,}98$", "$0{,}72$", "$0{,}90$", "$0{,}85$"],
                0,
                "Xác suất để cả hai rơ-le đều hỏng là $(1 - 0{,}9)(1 - 0{,}8) = 0{,}1 \\cdot 0{,}2 = 0{,}02$. Vậy xác suất để có ít nhất một rơ-le hoạt động tốt là $1 - 0{,}02 = 0{,}98$.",
            ),
            short(
                "vandung",
                "Ba cầu thủ sút phạt đền độc lập với nhau, mỗi người sút $1$ quả. Xác suất sút vào lưới của ba cầu thủ lần lượt là $0{,}8$; $0{,}7$ và $0{,}5$. Tính xác suất để có ít nhất một cầu thủ sút vào lưới (viết kết quả dưới dạng số thập phân).",
                ["0.97", "0,97"],
                "Xác suất để cả ba cầu thủ đều sút trượt là $P(\\bar{A}\\bar{B}\\bar{C}) = (1 - 0{,}8)(1 - 0{,}7)(1 - 0{,}5) = 0{,}2 \\cdot 0{,}3 \\cdot 0{,}5 = 0{,}03$. Vậy xác suất để có ít nhất một cầu thủ sút vào lưới là $1 - 0{,}03 = 0{,}97$.",
            ),
        ],
    },
    # =========================================================================
    # CHƯƠNG IX. ĐẠO HÀM
    # =========================================================================
    {
        "topic": "l11-ch09-dao-ham",
        "game_title": "Điều khiển xe đạt tốc độ tối ưu bằng Đạo hàm",
        "game_description": "Xây dựng hàm quãng đường $s(t)$, dùng đạo hàm $v(t) = s'(t)$ và $a(t) = s''(t)$ để xác định thời điểm xe đạt vận tốc cực đại.",
        "game_type": "function_challenge",
        "title": "Chương IX. Đạo hàm",
        "icon": "📉",
        "description": (
            "Tìm hiểu định nghĩa đạo hàm, ý nghĩa hình học (hệ số góc tiếp tuyến) và ý nghĩa vật lí "
            "(vận tốc tức thời) của đạo hàm; nắm vững bảng đạo hàm các hàm số sơ cấp cơ bản, "
            "các quy tắc tính đạo hàm, đạo hàm của hàm hợp và đạo hàm cấp hai."
        ),
        "requirements": [
            "Nhận biết được một số bài toán dẫn đến khái niệm đạo hàm như: xác định vận tốc tức thời của một vật chuyển động không đều, xác định tốc độ thay đổi của nhiệt độ.",
            "Nhận biết được định nghĩa đạo hàm và tính được đạo hàm của một số hàm đơn giản bằng định nghĩa.",
            "Nhận biết được ý nghĩa hình học của đạo hàm và thiết lập được phương trình tiếp tuyến của đồ thị hàm số tại một điểm thuộc đồ thị.",
            "Tính được đạo hàm của một số hàm số sơ cấp cơ bản (hàm đa thức, hàm căn thức đơn giản, hàm số lượng giác, hàm số mũ, hàm số lôgarit).",
            "Sử dụng được các công thức tính đạo hàm của tổng, hiệu, tích, thương của các hàm số và đạo hàm của hàm hợp.",
            "Nhận biết được khái niệm đạo hàm cấp hai của một hàm số, tính được đạo hàm cấp hai của một số hàm số đơn giản và vận dụng giải quyết bài toán thực tiễn (như tính gia tốc tức thời).",
        ],
        "definition": (
            "Đạo hàm của hàm số $y = f(x)$ tại điểm $x_0$, kí hiệu $f'(x_0)$, là giới hạn của tỉ số giữa số gia của hàm số $\\Delta y = f(x) - f(x_0)$ "
            "và số gia của đối số $\\Delta x = x - x_0$ khi $x \\to x_0$. Đạo hàm cấp một đặc trưng cho tốc độ biến thiên tức thời "
            "và hệ số góc tiếp tuyến của đồ thị, còn đạo hàm cấp hai $f''(x) = [f'(x)]'$ đặc trưng cho gia tốc của chuyển động."
        ),
        "theory": (
            "### Bài 31. Định nghĩa và ý nghĩa của đạo hàm\n"
            "- **Định nghĩa đạo hàm tại một điểm:** Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ và điểm $x_0 \\in (a; b)$. Nếu tồn tại giới hạn hữu hạn:\n"
            "  $$f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0} = \\lim_{\\Delta x \\to 0} \\dfrac{f(x_0 + \\Delta x) - f(x_0)}{\\Delta x}$$\n"
            "  thì giới hạn đó được gọi là *đạo hàm* của hàm số $y = f(x)$ tại điểm $x_0$.\n"
            "- **Ý nghĩa hình học:** Đạo hàm $f'(x_0)$ là hệ số góc của tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm $M_0(x_0; f(x_0))$. Phương trình tiếp tuyến tại $M_0$ là:\n"
            "  $$y = f'(x_0)(x - x_0) + f(x_0)$$\n"
            "- **Ý nghĩa vật lí:** Nếu phương trình chuyển động của chất điểm là $s = s(t)$ thì vận tốc tức thời tại thời điểm $t_0$ là $v(t_0) = s'(t_0)$.\n\n"
            "### Bài 32. Các quy tắc tính đạo hàm\n"
            "- **Đạo hàm của các hàm số sơ cấp cơ bản:** Gồm đạo hàm của hàm hằng, hàm lũy thừa $(x^n)' = n x^{n-1}$, hàm căn bậc hai $(\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}}$, các hàm số lượng giác, hàm số mũ $(e^x)' = e^x$, $(a^x)' = a^x \\ln a$ và hàm số lôgarit $(\\ln x)' = \\dfrac{1}{x}$, $(\\log_a x)' = \\dfrac{1}{x \\ln a}$.\n"
            "- **Quy tắc đạo hàm của tổng, hiệu, tích, thương:** Áp dụng cho hai hàm số có đạo hàm $u = u(x)$ và $v = v(x)$.\n"
            "- **Đạo hàm của hàm hợp:** Nếu $y = f(u)$ và $u = u(x)$ thì $y'_x = y'_u \\cdot u'_x$.\n\n"
            "### Bài 33. Đạo hàm cấp hai\n"
            "- **Định nghĩa:** Cho hàm số $y = f(x)$ có đạo hàm $f'(x)$ tại mọi $x \\in (a; b)$. Nếu hàm số $f'(x)$ lại có đạo hàm thì đạo hàm của nó được gọi là *đạo hàm cấp hai* của hàm số $y = f(x)$, kí hiệu $f''(x)$ hoặc $y''$: $f''(x) = [f'(x)]'$.\n"
            "- **Ý nghĩa cơ học của đạo hàm cấp hai:** Gia tốc tức thời của chuyển động $s = s(t)$ tại thời điểm $t$ bằng đạo hàm cấp hai của quãng đường: $a(t) = v'(t) = s''(t)$."
        ),
        "formulas": [
            G(
                "Định nghĩa, tiếp tuyến và quy tắc cơ bản",
                F("Định nghĩa đạo hàm", "$f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0}$"),
                F("Phương trình tiếp tuyến", "$y = f'(x_0)(x - x_0) + f(x_0)$"),
                F("Tổng, hiệu, tích, thương", "$(u \\pm v)' = u' \\pm v', \\quad (uv)' = u'v + uv', \\quad \\left(\\dfrac{u}{v}\\right)' = \\dfrac{u'v - uv'}{v^2}$"),
                F("Đạo hàm hàm hợp", "$y'_x = y'_u \\cdot u'_x$"),
            ),
            G(
                "Bảng đạo hàm các hàm số sơ cấp cơ bản",
                F("Hàm lũy thừa và căn thức", "$(c)' = 0, \\quad (x^n)' = n x^{n-1}, \\quad (\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}} \\ (x > 0)$"),
                F("Hàm số lượng giác", "$(\\sin x)' = \\cos x, \\quad (\\cos x)' = -\\sin x, \\quad (\\tan x)' = \\dfrac{1}{\\cos^2 x}, \\quad (\\cot x)' = -\\dfrac{1}{\\sin^2 x}$"),
                F("Hàm số mũ", "$(e^x)' = e^x, \\quad (a^x)' = a^x \\ln a \\ (0 < a \\neq 1)$"),
                F("Hàm số lôgarit", "$(\\ln x)' = \\dfrac{1}{x} \\ (x > 0), \\quad (\\log_a x)' = \\dfrac{1}{x \\ln a} \\ (x > 0, 0 < a \\neq 1)$"),
            ),
            G(
                "Đạo hàm cấp hai và ý nghĩa vật lí",
                F("Đạo hàm cấp hai", "$f''(x) = [f'(x)]'$"),
                F("Vận tốc và gia tốc tức thời", "$v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$"),
            ),
        ],
        "example": (
            "a) Viết phương trình tiếp tuyến của đồ thị hàm số $y = f(x) = x^3 - 3x^2 + 2$ tại điểm có hoành độ $x_0 = 3$.\n"
            "b) Một chất điểm chuyển động thẳng có phương trình quãng đường $s(t) = t^3 - 3t^2 + 12t + 5$ (trong đó $t$ tính bằng giây, $s$ tính bằng mét). Tính vận tốc và gia tốc tức thời của chất điểm tại thời điểm $t = 3$ giây."
        ),
        "example_answer": (
            "**a) Viết phương trình tiếp tuyến tại $x_0 = 3$:**\n"
            "- Ta có $f(3) = 3^3 - 3 \\cdot 3^2 + 2 = 2$.\n"
            "- Đạo hàm của hàm số là $f'(x) = 3x^2 - 6x \\Rightarrow f'(3) = 3 \\cdot 3^2 - 6 \\cdot 3 = 9$.\n"
            "- Phương trình tiếp tuyến tại điểm $M(3; 2)$ là:\n"
            "  $$y = f'(3)(x - 3) + f(3) \\Leftrightarrow y = 9(x - 3) + 2 \\Leftrightarrow y = 9x - 25$$\n\n"
            "**b) Tính vận tốc và gia tốc tại $t = 3$ giây:**\n"
            "- Vận tốc tức thời của chất điểm là $v(t) = s'(t) = 3t^2 - 6t + 12$. Tại $t = 3\\text{ s}$:\n"
            "  $$v(3) = 3 \\cdot 3^2 - 6 \\cdot 3 + 12 = 21\\text{ (m/s)}$$\n"
            "- Gia tốc tức thời của chất điểm là $a(t) = s''(t) = 6t - 6$. Tại $t = 3\\text{ s}$:\n"
            "  $$a(3) = 6 \\cdot 3 - 6 = 12\\text{ (m/s}^2\\text{)}$$"
        ),
        "real_life": (
            "Đạo hàm là công cụ trung tâm của Vật lí, Kinh tế và Kĩ thuật: đo vận tốc và gia tốc tức thời trên đồng hồ tốc độ ô tô, "
            "tính cường độ dòng điện tức thời $i(t) = q'(t)$, xác định chi phí biên và doanh thu biên trong kinh tế học."
        ),
        "quiz": [
            mcq(
                "biet",
                "Đạo hàm của hàm số $y = x^4 - 3x^2 + 5$ là:",
                [
                    "$y' = 4x^3 - 6x$",
                    "$y' = 4x^3 - 3x$",
                    "$y' = x^3 - 6x$",
                    "$y' = 4x^3 - 6x + 5$",
                ],
                0,
                "Áp dụng quy tắc đạo hàm của hàm đa thức: $y' = (x^4)' - 3(x^2)' + (5)' = 4x^3 - 6x$.",
            ),
            mcq(
                "biet",
                "Trong các công thức đạo hàm của hàm số lượng giác sau, công thức nào đúng?",
                [
                    "$(\\cos x)' = -\\sin x$",
                    "$(\\cos x)' = \\sin x$",
                    "$(\\sin x)' = -\\cos x$",
                    "$(\\tan x)' = -\\dfrac{1}{\\cos^2 x}$",
                ],
                0,
                "Theo bảng đạo hàm cơ bản, $(\\cos x)' = -\\sin x$ và $(\\sin x)' = \\cos x$.",
            ),
            mcq(
                "biet",
                "Trên khoảng $(0; +\\infty)$, đạo hàm của hàm số $y = \\ln x$ là:",
                [
                    "$y' = \\dfrac{1}{x}$",
                    "$y' = e^x$",
                    "$y' = -\\dfrac{1}{x^2}$",
                    "$y' = \\dfrac{1}{x \\ln 10}$",
                ],
                0,
                "Với $x > 0$, đạo hàm của hàm số lôgarit tự nhiên là $(\\ln x)' = \\dfrac{1}{x}$.",
            ),
            mcq(
                "biet",
                "Cho hàm số $f(x) = x^3 + 2x^2 - 5x + 1$. Đạo hàm cấp hai $f''(x)$ của hàm số đã cho là:",
                [
                    "$f''(x) = 6x + 4$",
                    "$f''(x) = 3x^2 + 4x - 5$",
                    "$f''(x) = 6x + 2$",
                    "$f''(x) = 3x + 4$",
                ],
                0,
                "Ta có $f'(x) = 3x^2 + 4x - 5 \\Rightarrow f''(x) = (3x^2 + 4x - 5)' = 6x + 4$.",
            ),
            mcq(
                "hieu",
                "Đạo hàm của hàm số $y = \\dfrac{2x + 1}{x - 1}$ với $x \\neq 1$ là:",
                [
                    "$y' = -\\dfrac{3}{(x - 1)^2}$",
                    "$y' = \\dfrac{3}{(x - 1)^2}$",
                    "$y' = -\\dfrac{1}{(x - 1)^2}$",
                    "$y' = \\dfrac{4x - 1}{(x - 1)^2}$",
                ],
                0,
                "Áp dụng quy tắc đạo hàm của một thương: $y' = \\dfrac{(2x + 1)'(x - 1) - (2x + 1)(x - 1)'}{(x - 1)^2} = \\dfrac{2(x - 1) - (2x + 1)}{(x - 1)^2} = -\\dfrac{3}{(x - 1)^2}$.",
            ),
            mcq(
                "hieu",
                "Phương trình tiếp tuyến của đồ thị hàm số $y = x^2 - 4x + 5$ tại điểm $M(3; 2)$ là:",
                [
                    "$y = 2x - 4$",
                    "$y = 2x + 4$",
                    "$y = 6x - 16$",
                    "$y = -2x + 8$",
                ],
                0,
                "Ta có $y' = 2x - 4 \\Rightarrow y'(3) = 2 \\cdot 3 - 4 = 2$. Phương trình tiếp tuyến tại $M(3; 2)$ là $y = 2(x - 3) + 2 \\Leftrightarrow y = 2x - 4$.",
            ),
            tf4(
                "hieu",
                "Cho hàm số $f(x) = x^3 - 3x^2 + 4$ có đồ thị $(C)$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Đạo hàm cấp một của hàm số là $f'(x) = 3x^2 - 6x$.",
                    "Hệ số góc của tiếp tuyến của đồ thị $(C)$ tại điểm có hoành độ $x_0 = 1$ bằng $3$.",
                    "Phương trình $f'(x) = 0$ có đúng hai nghiệm phân biệt là $x = 0$ và $x = 2$.",
                    "Phương trình tiếp tuyến của đồ thị $(C)$ tại điểm $A(3; 4)$ là $y = 9x - 23$.",
                ],
                [True, False, True, True],
                "a) Đúng vì $(x^3 - 3x^2 + 4)' = 3x^2 - 6x$.\n"
                "b) Sai vì hệ số góc tại $x_0 = 1$ là $f'(1) = 3 \\cdot 1^2 - 6 \\cdot 1 = -3 \\neq 3$.\n"
                "c) Đúng vì $3x^2 - 6x = 0 \\Leftrightarrow 3x(x - 2) = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$.\n"
                "d) Đúng vì $f'(3) = 3 \\cdot 9 - 18 = 9$, phương trình tiếp tuyến tại $A(3; 4)$ là $y = 9(x - 3) + 4 = 9x - 23$.",
            ),
            tf4(
                "hieu",
                "Cho hai hàm số $f(x) = \\sin 2x$ và $g(x) = e^{2x + 1}$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "Đạo hàm cấp một của hàm số $f(x)$ là $f'(x) = 2\\cos 2x$.",
                    "Đạo hàm cấp một của hàm số $g(x)$ là $g'(x) = e^{2x + 1}$.",
                    "Đạo hàm cấp hai của hàm số $f(x)$ thỏa mãn hệ thức $f''(x) + 4f(x) = 0, \\forall x \\in \\mathbb{R}$.",
                    "Giá trị của đạo hàm cấp hai $g''(0)$ bằng $4e$.",
                ],
                [True, False, True, True],
                "a) Đúng vì theo công thức đạo hàm hàm hợp, $(\\sin 2x)' = (2x)' \\cos 2x = 2\\cos 2x$.\n"
                "b) Sai vì $g'(x) = (2x + 1)' e^{2x + 1} = 2e^{2x + 1} \\neq e^{2x + 1}$.\n"
                "c) Đúng vì $f''(x) = (2\\cos 2x)' = -4\\sin 2x = -4f(x) \\Rightarrow f''(x) + 4f(x) = 0$.\n"
                "d) Đúng vì $g''(x) = (2e^{2x + 1})' = 4e^{2x + 1}$, suy ra $g''(0) = 4e^1 = 4e$.",
            ),
            mcq(
                "vandung",
                "Một vật chuyển động theo quy luật $s(t) = -t^3 + 6t^2 + 9t$, với $t$ (giây) là khoảng thời gian tính từ lúc vật bắt đầu chuyển động và $s$ (mét) là quãng đường vật đi được trong thời gian đó. Vận tốc lớn nhất của vật đạt được trong khoảng thời gian từ $t = 0$ đến khi vật dừng lại là:",
                [
                    "$21\\text{ m/s}$",
                    "$18\\text{ m/s}$",
                    "$15\\text{ m/s}$",
                    "$27\\text{ m/s}$",
                ],
                0,
                "Vận tốc tức thời của vật là $v(t) = s'(t) = -3t^2 + 12t + 9 = -3(t - 2)^2 + 21 \\le 21$. Dấu bằng xảy ra tại $t = 2$ (giây). Vậy vận tốc lớn nhất là $21\\text{ m/s}$.",
            ),
            short(
                "vandung",
                "Một chất điểm chuyển động thẳng với phương trình quãng đường $s(t) = t^3 - 3t^2 + 15t + 2$ ($s$ tính bằng mét, $t$ tính bằng giây). Tính vận tốc tức thời của chất điểm tại thời điểm gia tốc tức thời của nó bằng $12\\text{ m/s}^2$ (đơn vị: $\\text{m/s}$).",
                ["15"],
                "Ta có vận tốc $v(t) = s'(t) = 3t^2 - 6t + 15$ và gia tốc $a(t) = v'(t) = 6t - 6$. Khi $a(t) = 12 \\Leftrightarrow 6t - 6 = 12 \\Leftrightarrow t = 3$ (giây). Thay $t = 3$ vào $v(t)$, ta được $v(3) = 3 \\cdot 3^2 - 6 \\cdot 3 + 15 = 15\\text{ (m/s)}$.",
            ),
        ],
    },
]
