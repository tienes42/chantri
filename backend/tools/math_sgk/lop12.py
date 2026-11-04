"""TOÁN 12 — Kết nối tri thức với cuộc sống (tập một, tập hai).

6 chương đánh số (I – VI) đúng thứ tự mục lục SGK:
- Tập một: Chương I, Chương II, Chương III.
- Tập hai: Chương IV, Chương V, Chương VI.
Mỗi chương: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 12

LESSONS = [
    # ===================== CHƯƠNG I =====================
    {
        "topic": "l12-ch01-ung-dung-dao-ham-khao-sat-va-ve-do-thi-ham-so",
        "game_title": "Biệt Đội Cực Trị: Ứng dụng Đạo hàm để Khảo sát và Vẽ đồ thị Hàm số",
        "game_description": "Vận dụng đạo hàm xét tính đơn điệu, tìm cực trị và giá trị lớn nhất – nhỏ nhất để giải các bài toán tối ưu thực tiễn.",
        "game_type": "game_ung_dung_dao_ham",
        "title": "Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
        "icon": "📈",
        "description": (
            "Chương I · SGK Toán 12 tập một: Bài 1 – Bài 5. Tính đơn điệu và cực trị của hàm số; "
            "giá trị lớn nhất và giá trị nhỏ nhất của hàm số; đường tiệm cận của đồ thị hàm số; "
            "khảo sát sự biến thiên và vẽ đồ thị của hàm số; ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn."
        ),
        "requirements": [
            "Nhận biết được tính đồng biến, nghịch biến của một hàm số trên một khoảng dựa vào dấu của đạo hàm cấp một của nó.",
            "Thể hiện được tính đồng biến, nghịch biến của hàm số trong bảng biến thiên.",
            "Nhận biết được tính đơn điệu, điểm cực trị, giá trị cực trị của hàm số thông qua bảng biến thiên hoặc thông qua hình ảnh hình học của đồ thị hàm số.",
            "Nhận biết được giá trị lớn nhất, giá trị nhỏ nhất của hàm số trên một tập xác định cho trước; tìm được giá trị lớn nhất và giá trị nhỏ nhất của hàm số bằng đạo hàm trong những trường hợp đơn giản.",
            "Nhận biết được hình ảnh hình học của đường tiệm cận ngang, đường tiệm cận đứng, đường tiệm cận xiên của đồ thị hàm số.",
            "Mô tả được sơ đồ tổng quát để khảo sát hàm số (tìm tập xác định, xét chiều biến thiên, tìm cực trị, tìm tiệm cận, lập bảng biến thiên, vẽ đồ thị).",
            "Khảo sát được tập xác định, chiều biến thiên, cực trị, tiệm cận, bảng biến thiên và vẽ đồ thị của các hàm số: $y = ax^3 + bx^2 + cx + d$ $(a \\neq 0)$; $y = \\dfrac{ax + b}{cx + d}$ $(c \\neq 0, ad - bc \\neq 0)$; $y = \\dfrac{ax^2 + bx + c}{mx + n}$ $(a \\neq 0, m \\neq 0)$ và đa thức tử không chia hết cho đa thức mẫu.",
            "Nhận biết được tính đối xứng (trục đối xứng, tâm đối xứng) của đồ thị các hàm số trên.",
            "Vận dụng được đạo hàm và khảo sát hàm số để giải quyết một số vấn đề liên quan đến thực tiễn (tối ưu hoá chi phí, doanh thu, lợi nhuận, thể tích, tốc độ thay đổi).",
        ],
        "definition": (
            "- **Tính đơn điệu và dấu đạo hàm**: Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $K$. Nếu $f'(x) > 0$ với mọi $x \\in K$ thì $f(x)$ **đồng biến** trên $K$; nếu $f'(x) < 0$ với mọi $x \\in K$ thì $f(x)$ **nghịch biến** trên $K$. Nếu $f'(x) \\geq 0$ (hoặc $f'(x) \\leq 0$) với mọi $x \\in K$ và $f'(x) = 0$ chỉ tại một số hữu hạn điểm của $K$ thì hàm số vẫn đồng biến (hoặc nghịch biến) trên $K$.\n"
            "- **Cực trị của hàm số**: Nếu $f'(x)$ đổi dấu từ dương sang âm khi $x$ đi qua $x_0$ thì $x_0$ là **điểm cực đại**, $f(x_0)$ là **giá trị cực đại** (ký hiệu $y_{\\text{CĐ}}$). Nếu $f'(x)$ đổi dấu từ âm sang dương khi $x$ đi qua $x_0$ thì $x_0$ là **điểm cực tiểu**, $f(x_0)$ là **giá trị cực tiểu** (ký hiệu $y_{\\text{CT}}$). Điểm $(x_0; f(x_0))$ gọi là **điểm cực trị của đồ thị hàm số**.\n"
            "- **Giá trị lớn nhất – Giá trị nhỏ nhất**: Cho hàm số $y = f(x)$ xác định trên tập $D$. Số $M = \\max_{D} f(x)$ nếu $f(x) \\leq M$ với mọi $x \\in D$ và tồn tại $x_0 \\in D$ sao cho $f(x_0) = M$. Số $m = \\min_{D} f(x)$ nếu $f(x) \\geq m$ với mọi $x \\in D$ và tồn tại $x_0 \\in D$ sao cho $f(x_0) = m$.\n"
            "- **Đường tiệm cận của đồ thị hàm số**: Đường thẳng $y = y_0$ là **tiệm cận ngang** nếu $\\lim_{x \\to +\\infty} f(x) = y_0$ hoặc $\\lim_{x \\to -\\infty} f(x) = y_0$. Đường thẳng $x = x_0$ là **tiệm cận đứng** nếu ít nhất một trong các giới hạn $\\lim_{x \\to x_0^+} f(x)$, $\\lim_{x \\to x_0^-} f(x)$ bằng $+\\infty$ hoặc $-\\infty$. Đường thẳng $y = ax + b$ $(a \\neq 0)$ là **tiệm cận xiên** nếu $\\lim_{x \\to +\\infty} [f(x) - (ax + b)] = 0$ hoặc $\\lim_{x \\to -\\infty} [f(x) - (ax + b)] = 0$."
        ),
        "theory": (
            "### Bài 1. Tính đơn điệu và cực trị của hàm số\n"
            "- **Các bước xét tính đơn điệu và tìm cực trị**: (1) Tìm tập xác định $D$; (2) Tính đạo hàm $f'(x)$, tìm các điểm $x_i \\in D$ mà tại đó $f'(x) = 0$ hoặc $f'(x)$ không tồn tại; (3) Lập bảng biến thiên xét dấu $f'(x)$; (4) Kết luận các khoảng đồng biến, nghịch biến và các điểm cực đại, cực tiểu.\n"
            "- **Chú ý**: Đối với hàm phân thức $y = \\dfrac{ax + b}{cx + d}$ $(c \\neq 0, ad - bc \\neq 0)$, ta kết luận đồng biến hoặc nghịch biến trên từng khoảng xác định $\\left(-\\infty; -\\dfrac{d}{c}\\right)$ và $\\left(-\\dfrac{d}{c}; +\\infty\\right)$, tuyệt đối không gộp bằng ký hiệu hợp $\\cup$.\n"
            "### Bài 2. Giá trị lớn nhất và giá trị nhỏ nhất của hàm số\n"
            "- **Quy tắc tìm $\\max_{[a;b]} f(x)$ và $\\min_{[a;b]} f(x)$ của hàm số liên tục trên đoạn $[a; b]$**: (1) Tìm các điểm $x_1, x_2, \\dots, x_n \\in (a; b)$ tại đó $f'(x) = 0$ hoặc $f'(x)$ không tồn tại; (2) Tính $f(a), f(b), f(x_1), \\dots, f(x_n)$; (3) Số lớn nhất trong các giá trị đó là $\\max_{[a;b]} f(x)$ và số nhỏ nhất là $\\min_{[a;b]} f(x)$.\n"
            "### Bài 3. Đường tiệm cận của đồ thị hàm số\n"
            "- **Hàm bậc nhất trên bậc nhất** $y = \\dfrac{ax + b}{cx + d}$ $(c \\neq 0, ad - bc \\neq 0)$: có tiệm cận đứng $x = -\\dfrac{d}{c}$ và tiệm cận ngang $y = \\dfrac{a}{c}$.\n"
            "- **Hàm bậc hai trên bậc nhất** $y = \\dfrac{ax^2 + bx + c}{mx + n} = px + q + \\dfrac{r}{mx + n}$ $(a \\neq 0, m \\neq 0, r \\neq 0)$: có tiệm cận đứng $x = -\\dfrac{n}{m}$ và tiệm cận xiên $y = px + q$.\n"
            "### Bài 4. Khảo sát sự biến thiên và vẽ đồ thị của hàm số\n"
            "- **Sơ đồ khảo sát**: (1) Tìm tập xác định; (2) Xét sự biến thiên (tính $y'$, tìm cực trị, giới hạn tại vô cực và các đường tiệm cận, lập bảng biến thiên); (3) Vẽ đồ thị (xác định các điểm cực trị, giao điểm với các trục toạ độ, tâm đối xứng).\n"
            "- **Tâm đối xứng**: Đồ thị hàm bậc ba $y = ax^3 + bx^2 + cx + d$ nhận điểm uốn $I(x_0; y_0)$ với $x_0 = -\\dfrac{b}{3a}$ (nghiệm của $y'' = 0$) làm tâm đối xứng. Đồ thị hàm phân thức nhận giao điểm hai đường tiệm cận làm tâm đối xứng.\n"
            "### Bài 5. Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn\n"
            "- **Tốc độ thay đổi tức thời**: Nếu đại lượng $y = f(t)$ phụ thuộc thời gian $t$ thì $f'(t_0)$ là tốc độ thay đổi tức thời của $y$ tại thời điểm $t_0$ (như vận tốc tức thời $v(t) = s'(t)$, gia tốc $a(t) = v'(t)$, chi phí biên $C'(x)$, doanh thu biên $R'(x)$).\n"
            "- **Bài toán tối ưu thực tiễn**: Chọn biến số $x$ kèm điều kiện xác định thực tế, biểu diễn đại lượng cần tối ưu thành hàm số $f(x)$, rồi dùng đạo hàm tìm $\\max$ hoặc $\\min$.\n"
            "### Bài tập cuối chương I"
        ),
        "formulas": [
            G(
                "I. Đạo hàm, đơn điệu và cực trị",
                F("Đồng biến trên $K$", "$f'(x) \\geq 0, \\forall x \\in K$ (bằng $0$ tại hữu hạn điểm)"),
                F("Nghịch biến trên $K$", "$f'(x) \\leq 0, \\forall x \\in K$ (bằng $0$ tại hữu hạn điểm)"),
                F("Điều kiện cần của cực trị", "Nếu hàm khả vi đạt cực trị tại $x_0$ thì $f'(x_0) = 0$"),
                F("Đạo hàm hàm phân thức bậc nhất", "$\\left(\\dfrac{ax + b}{cx + d}\\right)' = \\dfrac{ad - bc}{(cx + d)^2}$"),
            ),
            G(
                "II. Giá trị lớn nhất – Giá trị nhỏ nhất trên đoạn $[a; b]$",
                F("Giá trị lớn nhất", "$M = \\max_{[a;b]} f(x) = \\max\\{f(a), f(b), f(x_1), \\dots, f(x_n)\\}$"),
                F("Giá trị nhỏ nhất", "$m = \\min_{[a;b]} f(x) = \\min\\{f(a), f(b), f(x_1), \\dots, f(x_n)\\}$"),
            ),
            G(
                "III. Các đường tiệm cận và tâm đối xứng",
                F("Tiệm cận ngang", "$\\lim_{x \\to +\\infty} f(x) = y_0$ hoặc $\\lim_{x \\to -\\infty} f(x) = y_0 \\Rightarrow y = y_0$"),
                F("Tiệm cận đứng", "$\\lim_{x \\to x_0^+} f(x) = \\pm\\infty$ hoặc $\\lim_{x \\to x_0^-} f(x) = \\pm\\infty \\Rightarrow x = x_0$"),
                F("Tiệm cận xiên", "$\\lim_{x \\to \\pm\\infty} [f(x) - (ax + b)] = 0 \\Rightarrow y = ax + b$ $(a \\neq 0)$"),
                F("Tâm đối xứng đồ thị bậc ba", "$I\\left(-\\dfrac{b}{3a}; f\\left(-\\dfrac{b}{3a}\\right)\\right)$ với $y''(x_0) = 0$"),
            ),
        ],
        "example": "Tìm các khoảng đơn điệu, cực trị và giá trị lớn nhất, giá trị nhỏ nhất trên đoạn $[0; 3]$ của hàm số $y = f(x) = x^3 - 3x^2 + 2$.",
        "example_answer": (
            "Tập xác định $D = \\mathbb{R}$. Đạo hàm $f'(x) = 3x^2 - 6x = 3x(x - 2)$; $f'(x) = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$.\n"
            "- Hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên $(0; 2)$.\n"
            "- Hàm số đạt cực đại tại $x = 0$, $y_{\\text{CĐ}} = f(0) = 2$; đạt cực tiểu tại $x = 2$, $y_{\\text{CT}} = f(2) = -2$.\n"
            "- Trên đoạn $[0; 3]$: ta có $x = 2 \\in (0; 3)$, tính $f(0) = 2$, $f(2) = -2$, $f(3) = 2$. Vậy $\\max_{[0;3]} f(x) = \\mathbf{2}$ và $\\min_{[0;3]} f(x) = \\mathbf{-2}$."
        ),
        "real_life": (
            "- Thiết kế bao bì, hộp chứa hàng hoá sao cho tiết kiệm vật liệu nhất (diện tích toàn phần nhỏ nhất) hoặc thể tích lớn nhất.\n"
            "- Phân tích hàm chi phí $C(x)$, hàm doanh thu $R(x)$ và tối đa hoá lợi nhuận $P(x) = R(x) - C(x)$ trong sản xuất kinh doanh."
        ),
        "quiz": [
            mcq(
                "biet",
                "Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x - 3$ với mọi $x \\in \\mathbb{R}$. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
                ["$(3; +\\infty)$", "$(-\\infty; 3)$", "$(-\\infty; +\\infty)$", "$(0; 3)$"],
                0,
                "Ta có $f'(x) > 0 \\Leftrightarrow x - 3 > 0 \\Leftrightarrow x > 3$. Vậy hàm số đồng biến trên khoảng **$(3; +\\infty)$**.",
            ),
            mcq(
                "biet",
                "Điểm cực tiểu của hàm số $y = x^3 - 3x + 1$ là:",
                ["$x = 1$", "$x = -1$", "$y = -1$", "$y = 3$"],
                0,
                "Ta có $y' = 3x^2 - 3 = 0 \\Leftrightarrow x = \\pm 1$. Vì $y'$ đổi dấu từ âm sang dương khi qua $x = 1$ nên điểm cực tiểu của hàm số là **$x = 1$**.",
            ),
            mcq(
                "biet",
                "Đường tiệm cận ngang của đồ thị hàm số $y = \\dfrac{2x - 1}{x + 3}$ là đường thẳng có phương trình:",
                ["$y = 2$", "$x = -3$", "$y = -3$", "$x = 2$"],
                0,
                "Vì $\\lim_{x \\to \\pm\\infty} \\dfrac{2x - 1}{x + 3} = 2$ nên đường tiệm cận ngang của đồ thị hàm số là **$y = 2$**.",
            ),
            mcq(
                "biet",
                "Đường tiệm cận đứng của đồ thị hàm số $y = \\dfrac{x + 2}{x - 4}$ là đường thẳng:",
                ["$x = 4$", "$x = -2$", "$y = 1$", "$y = 4$"],
                0,
                "Tập xác định $D = \\mathbb{R} \\setminus \\{4\\}$. Vì $\\lim_{x \\to 4^+} \\dfrac{x + 2}{x - 4} = +\\infty$ nên đường thẳng **$x = 4$** là tiệm cận đứng.",
            ),
            mcq(
                "hieu",
                "Giá trị lớn nhất của hàm số $f(x) = x^3 - 3x^2 - 9x + 10$ trên đoạn $[-2; 2]$ bằng:",
                ["$15$", "$10$", "$-12$", "$0$"],
                0,
                "Trên $[-2; 2]$, ta có $f'(x) = 3x^2 - 6x - 9 = 0 \\Leftrightarrow x = -1 \\in (-2; 2)$ (loại $x = 3 \\notin [-2; 2]$). Tính $f(-2) = 8$, $f(-1) = 15$, $f(2) = -12$. Vậy $\\max_{[-2;2]} f(x) = \\mathbf{15}$.",
            ),
            mcq(
                "hieu",
                "Đồ thị hàm số $y = \\dfrac{x^2 + 2x + 3}{x + 1}$ có đường tiệm cận xiên là:",
                ["$y = x + 1$", "$y = x + 2$", "$y = x - 1$", "$y = 2x + 1$"],
                0,
                "Chia đa thức: $y = \\dfrac{(x + 1)^2 + 2}{x + 1} = x + 1 + \\dfrac{2}{x + 1}$. Do $\\lim_{x \\to \\pm\\infty} [y - (x + 1)] = \\lim_{x \\to \\pm\\infty} \\dfrac{2}{x + 1} = 0$ nên tiệm cận xiên là **$y = x + 1$**.",
            ),
            tf4(
                "hieu",
                "Cho hàm số $y = f(x) = x^3 - 3x^2 + 4$ có đồ thị $(C)$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Đạo hàm của hàm số là $f'(x) = 3x^2 - 6x$.",
                    "b) Hàm số đồng biến trên khoảng $(0; 2)$.",
                    "c) Giá trị cực đại của hàm số bằng $4$ và giá trị cực tiểu bằng $0$.",
                    "d) Đồ thị $(C)$ nhận điểm $I(1; 2)$ làm tâm đối xứng.",
                ],
                [True, False, True, True],
                "a) $f'(x) = 3x^2 - 6x \\Rightarrow$ **Đúng**.\n"
                "b) Trên $(0; 2)$, $f'(x) = 3x(x - 2) < 0$ nên hàm số nghịch biến trên $(0; 2) \\Rightarrow$ **Sai**.\n"
                "c) Hàm số đạt cực đại tại $x = 0 \\Rightarrow y_{\\text{CĐ}} = f(0) = 4$; đạt cực tiểu tại $x = 2 \\Rightarrow y_{\\text{CT}} = f(2) = 0 \\Rightarrow$ **Đúng**.\n"
                "d) Ta có $f''(x) = 6x - 6 = 0 \\Leftrightarrow x = 1$, $f(1) = 2$ nên $I(1; 2)$ là tâm đối xứng của $(C) \\Rightarrow$ **Đúng**.",
            ),
            tf4(
                "hieu",
                "Cho hàm số $y = f(x) = x + 1 + \\dfrac{4}{x - 1}$ với $x \\neq 1$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Đồ thị hàm số có tiệm cận đứng là đường thẳng $x = 1$.",
                    "b) Đồ thị hàm số có tiệm cận xiên là đường thẳng $y = x + 1$.",
                    "c) Đạo hàm của hàm số là $f'(x) = 1 + \\dfrac{4}{(x - 1)^2}$ với mọi $x \\neq 1$.",
                    "d) Giá trị nhỏ nhất của hàm số trên khoảng $(1; +\\infty)$ bằng $6$.",
                ],
                [True, True, False, True],
                "a) $\\lim_{x \\to 1^+} f(x) = +\\infty$ nên $x = 1$ là tiệm cận đứng $\\Rightarrow$ **Đúng**.\n"
                "b) $\\lim_{x \\to \\pm\\infty} [f(x) - (x + 1)] = \\lim_{x \\to \\pm\\infty} \\dfrac{4}{x - 1} = 0$ nên $y = x + 1$ là tiệm cận xiên $\\Rightarrow$ **Đúng**.\n"
                "c) $f'(x) = 1 - \\dfrac{4}{(x - 1)^2} \\Rightarrow$ **Sai**.\n"
                "d) Trên $(1; +\\infty)$, $f'(x) = 0 \\Leftrightarrow (x - 1)^2 = 4 \\Leftrightarrow x = 3$. Bảng biến thiên trên $(1; +\\infty)$ cho $\\min_{(1;+\\infty)} f(x) = f(3) = 3 + 1 + \\dfrac{4}{2} = 6 \\Rightarrow$ **Đúng**.",
            ),
            mcq(
                "vandung",
                "Một tấm bìa hình vuông cạnh $12\\text{ cm}$ được cắt bỏ bốn hình vuông nhỏ bằng nhau có cạnh $x\\text{ cm}$ ở bốn góc rồi gấp lên thành một hình hộp chữ nhật không nắp. Thể tích lớn nhất của chiếc hộp đó bằng:",
                ["$128\\text{ cm}^3$", "$144\\text{ cm}^3$", "$108\\text{ cm}^3$", "$96\\text{ cm}^3$"],
                0,
                "Đáy hộp là hình vuông cạnh $12 - 2x$ và chiều cao là $x$ với $0 < x < 6$. Thể tích $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2$. Ta có $V'(x) = 4[(6 - x)^2 - 2x(6 - x)] = 4(6 - x)(6 - 3x) = 0 \\Leftrightarrow x = 2 \\in (0; 6)$. Khi đó $V_{\\max} = V(2) = 2 \\cdot (12 - 4)^2 = \\mathbf{128\\text{ cm}^3}$.",
            ),
            short(
                "vandung",
                "Một doanh nghiệp sản xuất $x$ sản phẩm trong một ngày $(1 \\leq x \\leq 50)$ có tổng lợi nhuận (đơn vị: triệu đồng) được mô tả bởi hàm số $P(x) = -x^3 + 30x^2 + 50$. Hỏi doanh nghiệp cần sản xuất bao nhiêu sản phẩm mỗi ngày để đạt lợi nhuận lớn nhất?",
                ["20"],
                "Ta có $P'(x) = -3x^2 + 60x = 3x(20 - x)$. Trên đoạn $[1; 50]$, $P'(x) = 0 \\Leftrightarrow x = 20$. Vì $P'(x) > 0$ trên $(1; 20)$ và $P'(x) < 0$ trên $(20; 50)$ nên lợi nhuận đạt giá trị lớn nhất tại $x = \\mathbf{20}$ sản phẩm.",
                unit="sản phẩm",
            ),
        ],
    },
    # ===================== CHƯƠNG II =====================
    {
        "topic": "l12-ch02-vecto-va-he-truc-toa-do-trong-khong-gian",
        "title": "Vectơ và hệ trục toạ độ trong không gian",
        "icon": "🧭",
        "description": (
            "Chương II · SGK Toán 12 tập một: Bài 6 – Bài 8. Vectơ trong không gian; "
            "hệ trục toạ độ trong không gian; biểu thức toạ độ của các phép toán vectơ."
        ),
        "requirements": [
            "Nhận biết được vectơ và các phép toán vectơ trong không gian (tổng và hiệu của hai vectơ, tích của một số với một vectơ, tích vô hướng của hai vectơ).",
            "Vận dụng được quy tắc hình hộp, quy tắc ba điểm, quy tắc hình bình hành và tính chất trọng tâm để thực hiện các phép toán vectơ trong không gian.",
            "Nhận biết được toạ độ của một điểm và toạ độ của một vectơ đối với hệ trục toạ độ $Oxyz$ trong không gian.",
            "Xác định được độ dài của một vectơ, khoảng cách giữa hai điểm, toạ độ trung điểm đoạn thẳng và toạ độ trọng tâm tam giác khi biết toạ độ.",
            "Sử dụng được biểu thức toạ độ của các phép toán vectơ (cộng, trừ, nhân với một số, tích vô hướng) và tính được côsin góc giữa hai vectơ.",
            "Vận dụng được toạ độ và các phép toán vectơ để giải một số bài toán thực tiễn (tổng hợp lực trong không gian, định vị vị trí 3D).",
        ],
        "definition": (
            "- **Vectơ trong không gian**: Là một đoạn thẳng có hướng. Ký hiệu $\\overrightarrow{AB}$ chỉ vectơ có điểm đầu $A$, điểm cuối $B$; độ dài là $|\\overrightarrow{AB}| = AB$.\n"
            "- **Quy tắc hình hộp**: Cho hình hộp $ABCD.A'B'C'D'$, khi đó $\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$.\n"
            "- **Hệ trục toạ độ $Oxyz$**: Gồm ba trục $Ox, Oy, Oz$ đôi một vuông góc tại gốc $O$ với các vectơ đơn vị tương ứng $\\overrightarrow{i}, \\overrightarrow{j}, \\overrightarrow{k}$ thoả mãn $|\\overrightarrow{i}| = |\\overrightarrow{j}| = |\\overrightarrow{k}| = 1$.\n"
            "- **Toạ độ của điểm và vectơ**: Nếu $\\overrightarrow{u} = x\\overrightarrow{i} + y\\overrightarrow{j} + z\\overrightarrow{k}$ thì $\\overrightarrow{u} = (x; y; z)$. Điểm $M(x; y; z) \\Leftrightarrow \\overrightarrow{OM} = x\\overrightarrow{i} + y\\overrightarrow{j} + z\\overrightarrow{k}$."
        ),
        "theory": (
            "### Bài 6. Vectơ trong không gian\n"
            "- **Các quy tắc cơ bản**: Quy tắc ba điểm $\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$; quy tắc hiệu $\\overrightarrow{AB} - \\overrightarrow{AC} = \\overrightarrow{CB}$; quy tắc hình bình hành $\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$; quy tắc hình hộp $\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$.\n"
            "- **Hệ thức trung điểm và trọng tâm**: Nếu $I$ là trung điểm $AB$ thì $\\overrightarrow{IA} + \\overrightarrow{IB} = \\overrightarrow{0}$ và $\\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$. Nếu $G$ là trọng tâm tam giác $ABC$ thì $\\overrightarrow{GA} + \\overrightarrow{GB} + \\overrightarrow{GC} = \\overrightarrow{0}$.\n"
            "- **Tích vô hướng**: $\\overrightarrow{a} \\cdot \\overrightarrow{b} = |\\overrightarrow{a}| \\cdot |\\overrightarrow{b}| \\cdot \\cos(\\overrightarrow{a}, \\overrightarrow{b})$. Hai vectơ khác $\\overrightarrow{0}$ vuông góc khi và chỉ khi $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$.\n"
            "### Bài 7. Hệ trục toạ độ trong không gian\n"
            "- **Toạ độ vectơ theo hai đầu mút**: Với $A(x_A; y_A; z_A)$ và $B(x_B; y_B; z_B)$, ta có $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)$.\n"
            "- **Hình chiếu của điểm $M(x_0; y_0; z_0)$**: Trên $Ox$ là $(x_0; 0; 0)$, trên $Oy$ là $(0; y_0; 0)$, trên $Oz$ là $(0; 0; z_0)$; trên mặt phẳng $(Oxy)$ là $(x_0; y_0; 0)$, trên $(Oyz)$ là $(0; y_0; z_0)$, trên $(Ozx)$ là $(x_0; 0; z_0)$.\n"
            "### Bài 8. Biểu thức toạ độ của các phép toán vectơ\n"
            "- Cho $\\overrightarrow{u} = (x_1; y_1; z_1)$ và $\\overrightarrow{v} = (x_2; y_2; z_2)$: $\\overrightarrow{u} \\pm \\overrightarrow{v} = (x_1 \\pm x_2; y_1 \\pm y_2; z_1 \\pm z_2)$ và $k\\overrightarrow{u} = (kx_1; ky_1; kz_1)$.\n"
            "- **Tích vô hướng và độ dài**: $\\overrightarrow{u} \\cdot \\overrightarrow{v} = x_1x_2 + y_1y_2 + z_1z_2$; $|\\overrightarrow{u}| = \\sqrt{x_1^2 + y_1^2 + z_1^2}$.\n"
            "### Bài tập cuối chương II"
        ),
        "formulas": [
            G(
                "I. Các phép toán vectơ trong không gian",
                F("Quy tắc ba điểm và hiệu", "$\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC} \\quad ; \\quad \\overrightarrow{AB} - \\overrightarrow{AC} = \\overrightarrow{CB}$"),
                F("Quy tắc hình hộp", "$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$"),
                F("Tích vô hướng", "$\\overrightarrow{a} \\cdot \\overrightarrow{b} = |\\overrightarrow{a}| \\cdot |\\overrightarrow{b}| \\cdot \\cos(\\overrightarrow{a}, \\overrightarrow{b})$"),
            ),
            G(
                "II. Biểu thức toạ độ của vectơ",
                F("Tổng, hiệu và tích với số", "$\\overrightarrow{u} \\pm \\overrightarrow{v} = (x_1 \\pm x_2; y_1 \\pm y_2; z_1 \\pm z_2) \\quad ; \\quad k\\overrightarrow{u} = (kx_1; ky_1; kz_1)$"),
                F("Tích vô hướng theo toạ độ", "$\\overrightarrow{u} \\cdot \\overrightarrow{v} = x_1x_2 + y_1y_2 + z_1z_2$"),
                F("Độ dài và khoảng cách", "$|\\overrightarrow{u}| = \\sqrt{x_1^2 + y_1^2 + z_1^2} \\quad ; \\quad AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$"),
                F("Côsin góc giữa hai vectơ", "$\\cos(\\overrightarrow{u}, \\overrightarrow{v}) = \\dfrac{x_1x_2 + y_1y_2 + z_1z_2}{\\sqrt{x_1^2 + y_1^2 + z_1^2}\\sqrt{x_2^2 + y_2^2 + z_2^2}}$"),
            ),
            G(
                "III. Toạ độ trung điểm và trọng tâm",
                F("Trung điểm $I$ của $AB$", "$I\\left(\\dfrac{x_A + x_B}{2}; \\dfrac{y_A + y_B}{2}; \\dfrac{z_A + z_B}{2}\\right)$"),
                F("Trọng tâm $G$ của $\\triangle ABC$", "$G\\left(\\dfrac{x_A + x_B + x_C}{3}; \\dfrac{y_A + y_B + y_C}{3}; \\dfrac{z_A + z_C + z_B}{3}\\right)$"),
            ),
        ],
        "example": "Trong không gian $Oxyz$, cho ba điểm $A(1; 2; -1)$, $B(3; 0; 3)$ và $C(2; 4; 1)$. Tìm toạ độ vectơ $\\overrightarrow{AB}$, độ dài đoạn $AB$, toạ độ trung điểm $I$ của $AB$ và trọng tâm $G$ của tam giác $ABC$.",
        "example_answer": (
            "- Ta có $\\overrightarrow{AB} = (3 - 1; 0 - 2; 3 - (-1)) = \\mathbf{(2; -2; 4)}$.\n"
            "- Độ dài $AB = |\\overrightarrow{AB}| = \\sqrt{2^2 + (-2)^2 + 4^2} = \\sqrt{24} = \\mathbf{2\\sqrt{6}}$.\n"
            "- Trung điểm $I$ của $AB$: $I\\left(\\dfrac{1 + 3}{2}; \\dfrac{2 + 0}{2}; \\dfrac{-1 + 3}{2}\\right) = \\mathbf{I(2; 1; 1)}$.\n"
            "- Trọng tâm $G$ của $\\triangle ABC$: $G\\left(\\dfrac{1 + 3 + 2}{3}; \\dfrac{2 + 0 + 4}{3}; \\dfrac{-1 + 3 + 1}{3}\\right) = \\mathbf{G(2; 2; 1)}$."
        ),
        "real_life": (
            "- Định vị toạ độ máy bay, tàu biển hoặc thiết bị bay không người lái (drone) trong hệ toạ độ không gian ba chiều $Oxyz$.\n"
            "- Tổng hợp các lực căng dây cáp treo một vật nặng trong không gian xây dựng và cơ khí."
        ),
        "quiz": [
            mcq(
                "biet",
                "Trong không gian $Oxyz$, cho $\\overrightarrow{u} = 2\\overrightarrow{i} - 3\\overrightarrow{j} + 4\\overrightarrow{k}$. Toạ độ của vectơ $\\overrightarrow{u}$ là:",
                ["$(2; -3; 4)$", "$(2; 3; 4)$", "$(-2; 3; -4)$", "$(4; -3; 2)$"],
                0,
                "Theo định nghĩa toạ độ của vectơ, $\\overrightarrow{u} = 2\\overrightarrow{i} - 3\\overrightarrow{j} + 4\\overrightarrow{k} \\Rightarrow \\overrightarrow{u} = \\mathbf{(2; -3; 4)}$.",
            ),
            mcq(
                "biet",
                "Trong không gian $Oxyz$, cho hai điểm $A(1; -2; 3)$ và $B(4; 2; -1)$. Toạ độ của vectơ $\\overrightarrow{AB}$ là:",
                ["$(3; 4; -4)$", "$(-3; -4; 4)$", "$(5; 0; 2)$", "$(4; -4; -3)$"],
                0,
                "Ta có $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (4 - 1; 2 - (-2); -1 - 3) = \\mathbf{(3; 4; -4)}$.",
            ),
            mcq(
                "biet",
                "Trong không gian $Oxyz$, hình chiếu vuông góc của điểm $M(3; -4; 5)$ trên mặt phẳng $(Oxy)$ có toạ độ là:",
                ["$(3; -4; 0)$", "$(0; -4; 5)$", "$(3; 0; 5)$", "$(0; 0; 5)$"],
                0,
                "Hình chiếu vuông góc của điểm $M(x_0; y_0; z_0)$ trên mặt phẳng $(Oxy)$ có cao độ $z = 0$, tức là **$(3; -4; 0)$**.",
            ),
            mcq(
                "biet",
                "Trong không gian $Oxyz$, cho hai điểm $A(2; 4; -2)$ và $B(6; 0; 4)$. Toạ độ trung điểm $I$ của đoạn thẳng $AB$ là:",
                ["$(4; 2; 1)$", "$(8; 4; 2)$", "$(2; -2; 3)$", "$(4; 4; 1)$"],
                0,
                "Trung điểm $I$ có toạ độ $\\left(\\dfrac{2 + 6}{2}; \\dfrac{4 + 0}{2}; \\dfrac{-2 + 4}{2}\\right) = \\mathbf{(4; 2; 1)}$.",
            ),
            mcq(
                "hieu",
                "Trong không gian $Oxyz$, cho hai vectơ $\\overrightarrow{a} = (1; -2; 2)$ và $\\overrightarrow{b} = (2; 1; -2)$. Tích vô hướng $\\overrightarrow{a} \\cdot \\overrightarrow{b}$ bằng:",
                ["$-4$", "$4$", "$0$", "$-2$"],
                0,
                "Ta có $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 1 \\cdot 2 + (-2) \\cdot 1 + 2 \\cdot (-2) = 2 - 2 - 4 = \\mathbf{-4}$.",
            ),
            mcq(
                "hieu",
                "Trong không gian $Oxyz$, cho hai vectơ $\\overrightarrow{u} = (1; 2; -1)$ và $\\overrightarrow{v} = (3; 0; 2)$. Toạ độ của vectơ $\\overrightarrow{w} = 2\\overrightarrow{u} - \\overrightarrow{v}$ là:",
                ["$(-1; 4; -4)$", "$(5; 4; 0)$", "$(-1; 2; -4)$", "$(1; -4; 4)$"],
                0,
                "Ta có $2\\overrightarrow{u} = (2; 4; -2)$, suy ra $\\overrightarrow{w} = 2\\overrightarrow{u} - \\overrightarrow{v} = (2 - 3; 4 - 0; -2 - 2) = \\mathbf{(-1; 4; -4)}$.",
            ),
            tf4(
                "hieu",
                "Cho hình hộp $ABCD.A'B'C'D'$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) $\\overrightarrow{AB} = \\overrightarrow{D'C'}$.",
                    "b) $\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$.",
                    "c) $\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$.",
                    "d) $\\overrightarrow{AB} + \\overrightarrow{B'C'} + \\overrightarrow{DD'} = \\overrightarrow{AC}$.",
                ],
                [True, True, True, False],
                "a) Trong hình hộp, $AB \\parallel D'C'$ và $AB = D'C'$, hai vectơ $\\overrightarrow{AB}, \\overrightarrow{D'C'}$ cùng hướng nên $\\overrightarrow{AB} = \\overrightarrow{D'C'} \\Rightarrow$ **Đúng**.\n"
                "b) Theo quy tắc hình bình hành trong đáy $ABCD$, $\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC} \\Rightarrow$ **Đúng**.\n"
                "c) Theo quy tắc hình hộp, $\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'} \\Rightarrow$ **Đúng**.\n"
                "d) Vì $\\overrightarrow{B'C'} = \\overrightarrow{AD}$ và $\\overrightarrow{DD'} = \\overrightarrow{AA'}$ nên $\\overrightarrow{AB} + \\overrightarrow{B'C'} + \\overrightarrow{DD'} = \\overrightarrow{AC'} \\neq \\overrightarrow{AC} \\Rightarrow$ **Sai**.",
            ),
            tf4(
                "hieu",
                "Trong không gian $Oxyz$, cho ba điểm $A(1; 0; 2)$, $B(2; 2; 4)$ và $C(0; 1; 0)$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Toạ độ của vectơ $\\overrightarrow{AB}$ là $(1; 2; 2)$.",
                    "b) Độ dài đoạn thẳng $AB$ bằng $3$.",
                    "c) Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{AC}$ vuông góc với nhau.",
                    "d) Trọng tâm $G$ của tam giác $ABC$ có toạ độ là $(1; 1; 2)$.",
                ],
                [True, True, False, True],
                "a) $\\overrightarrow{AB} = (2 - 1; 2 - 0; 4 - 2) = (1; 2; 2) \\Rightarrow$ **Đúng**.\n"
                "b) $AB = \\sqrt{1^2 + 2^2 + 2^2} = \\sqrt{9} = 3 \\Rightarrow$ **Đúng**.\n"
                "c) Ta có $\\overrightarrow{AC} = (-1; 1; -2)$ nên $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = 1(-1) + 2(1) + 2(-2) = -3 \\neq 0 \\Rightarrow$ **Sai**.\n"
                "d) Trọng tâm $G\\left(\\dfrac{1 + 2 + 0}{3}; \\dfrac{0 + 2 + 1}{3}; \\dfrac{2 + 4 + 0}{3}\\right) = (1; 1; 2) \\Rightarrow$ **Đúng**.",
            ),
            mcq(
                "vandung",
                "Trong không gian $Oxyz$ (đơn vị trên mỗi trục là kilômét), một trạm kiểm soát không lưu đặt tại gốc toạ độ $O(0; 0; 0)$ phát hiện hai máy bay tại các vị trí $A(3; 4; 2)$ và $B(6; 8; 14)$. Khoảng cách giữa hai máy bay tại thời điểm đó bằng:",
                ["$13\\text{ km}$", "$12\\text{ km}$", "$15\\text{ km}$", "$10\\text{ km}$"],
                0,
                "Ta có $\\overrightarrow{AB} = (6 - 3; 8 - 4; 14 - 2) = (3; 4; 12)$. Khoảng cách giữa hai máy bay là $AB = \\sqrt{3^2 + 4^2 + 12^2} = \\sqrt{9 + 16 + 144} = \\sqrt{169} = \\mathbf{13\\text{ km}}$.",
            ),
            short(
                "vandung",
                "Một vật nặng trong không gian chịu tác dụng đồng thời của ba lực $\\overrightarrow{F_1} = (2; 1; 3)$, $\\overrightarrow{F_2} = (1; -3; 2)$ và $\\overrightarrow{F_3} = (0; 6; -5)$ (đơn vị trên mỗi trục là Newton). Tính độ lớn của hợp lực $\\overrightarrow{F} = \\overrightarrow{F_1} + \\overrightarrow{F_2} + \\overrightarrow{F_3}$ tác dụng lên vật.",
                ["5"],
                "Ta có hợp lực $\\overrightarrow{F} = \\overrightarrow{F_1} + \\overrightarrow{F_2} + \\overrightarrow{F_3} = (2 + 1 + 0; 1 - 3 + 6; 3 + 2 - 5) = (3; 4; 0)$. Độ lớn hợp lực là $|\\overrightarrow{F}| = \\sqrt{3^2 + 4^2 + 0^2} = \\mathbf{5}\\text{ N}$.",
                unit="N",
            ),
        ],
    },
    # ===================== CHƯƠNG III =====================
    {
        "topic": "l12-ch03-cac-so-dac-trung-do-muc-do-phan-tan-cua-mau-so-lieu-ghep-nhom",
        "title": "Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm",
        "icon": "📊",
        "description": (
            "Chương III · SGK Toán 12 tập một: Bài 9 – Bài 10. Khoảng biến thiên và khoảng tứ phân vị "
            "của mẫu số liệu ghép nhóm; phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm."
        ),
        "requirements": [
            "Tính được khoảng biến thiên, khoảng tứ phân vị của mẫu số liệu ghép nhóm.",
            "Tính được phương sai, độ lệch chuẩn của mẫu số liệu ghép nhóm.",
            "Hiểu được ý nghĩa và vai trò của khoảng biến thiên, khoảng tứ phân vị, phương sai và độ lệch chuẩn trong việc đo mức độ phân tán của mẫu số liệu ghép nhóm.",
            "Chỉ ra được những kết luận hợp lí dựa trên việc so sánh các số đặc trưng đo mức độ phân tán của hai mẫu số liệu ghép nhóm trong thực tiễn.",
        ],
        "definition": (
            "- **Khoảng biến thiên của mẫu số liệu ghép nhóm**: Cho mẫu số liệu ghép nhóm có nhóm đầu tiên là $[a_1; a_2)$ và nhóm cuối cùng là $[a_k; a_{k+1})$ (các nhóm có tần số dương). Khoảng biến thiên là $R = a_{k+1} - a_1$.\n"
            "- **Khoảng tứ phân vị của mẫu số liệu ghép nhóm**: Là hiệu giữa tứ phân vị thứ ba $Q_3$ và tứ phân vị thứ nhất $Q_1$, ký hiệu $\\Delta_Q = Q_3 - Q_1$.\n"
            "- **Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm**: Với cỡ mẫu $n = n_1 + n_2 + \\dots + n_k$, giá trị đại diện nhóm thứ $i$ là $x_i = \\dfrac{a_i + a_{i+1}}{2}$ và số trung bình $\\bar{x} = \\dfrac{1}{n}\\sum_{i=1}^k n_i x_i$, **phương sai** là $s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = \\left(\\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2\\right) - (\\bar{x})^2$, còn **độ lệch chuẩn** là $s = \\sqrt{s^2}$."
        ),
        "theory": (
            "### Bài 9. Khoảng biến thiên và khoảng tứ phân vị\n"
            "- **Khoảng biến thiên** $R = a_{k+1} - a_1$: tính nhanh nhưng phụ thuộc hoàn toàn vào hai đầu mút nên dễ bị ảnh hưởng bởi các giá trị bất thường.\n"
            "- **Tứ phân vị thứ $r$** $(r \\in \\{1; 2; 3\\})$: Giả sử nhóm $[u_m; u_{m+1})$ là nhóm đầu tiên có tần số tích luỹ lớn hơn hoặc bằng $\\dfrac{rn}{4}$. Khi đó $Q_r = u_m + \\dfrac{\\dfrac{rn}{4} - C}{n_m}(u_{m+1} - u_m)$, trong đó $n_m$ là tần số của nhóm chứa $Q_r$ và $C$ là tần số tích luỹ của các nhóm đứng trước nhóm đó.\n"
            "- **Ý nghĩa của khoảng tứ phân vị** $\\Delta_Q = Q_3 - Q_1$: đo mức độ phân tán của $50\%$ số liệu chính giữa và **không bị ảnh hưởng** bởi các giá trị ngoại lệ.\n"
            "### Bài 10. Phương sai và độ lệch chuẩn\n"
            "- **Các bước tính phương sai $s^2$ và độ lệch chuẩn $s$**: (1) Xác định giá trị đại diện $x_i = \\dfrac{a_i + a_{i+1}}{2}$ của mỗi nhóm; (2) Tính số trung bình $\\bar{x} = \\dfrac{n_1x_1 + \\dots + n_kx_k}{n}$; (3) Tính $s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2$ và $s = \\sqrt{s^2}$.\n"
            "- **Ý nghĩa**: Độ lệch chuẩn $s$ có **cùng đơn vị đo** với dữ liệu gốc. Phương sai $s^2$ và độ lệch chuẩn $s$ càng nhỏ thì số liệu càng tập trung quanh số trung bình $\\bar{x}$ (độ đồng đều, độ ổn định càng cao).\n"
            "### Bài tập cuối chương III"
        ),
        "formulas": [
            G(
                "I. Khoảng biến thiên và khoảng tứ phân vị",
                F("Khoảng biến thiên", "$R = a_{k+1} - a_1$"),
                F("Công thức tứ phân vị $Q_r$ $(r = 1, 2, 3)$", "$Q_r = u_m + \\dfrac{\\dfrac{rn}{4} - C}{n_m}(u_{m+1} - u_m)$"),
                F("Khoảng tứ phân vị", "$\\Delta_Q = Q_3 - Q_1$"),
            ),
            G(
                "II. Phương sai và độ lệch chuẩn",
                F("Giá trị đại diện nhóm $[a_i; a_{i+1})$", "$x_i = \\dfrac{a_i + a_{i+1}}{2}$"),
                F("Số trung bình mẫu ghép nhóm", "$\\bar{x} = \\dfrac{1}{n}(n_1x_1 + n_2x_2 + \\dots + n_kx_k)$"),
                F("Phương sai mẫu ghép nhóm", "$s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_ix_i^2 - (\\bar{x})^2$"),
                F("Độ lệch chuẩn", "$s = \\sqrt{s^2}$"),
            ),
        ],
        "example": (
            "Thời gian tự học mỗi ngày (đơn vị: phút) của $20$ học sinh được ghép thành $3$ nhóm: "
            "$[20; 40)$ có $5$ học sinh; $[40; 60)$ có $10$ học sinh; $[60; 80)$ có $5$ học sinh. "
            "Tính khoảng biến thiên $R$, số trung bình $\\bar{x}$, phương sai $s^2$ và độ lệch chuẩn $s$."
        ),
        "example_answer": (
            "- Khoảng biến thiên: $R = 80 - 20 = \\mathbf{60}$ (phút).\n"
            "- Giá trị đại diện các nhóm: $x_1 = 30$, $x_2 = 50$, $x_3 = 70$. Số trung bình: $\\bar{x} = \\dfrac{5 \\cdot 30 + 10 \\cdot 50 + 5 \\cdot 70}{20} = \\mathbf{50}$ (phút).\n"
            "- Phương sai: $s^2 = \\dfrac{5(30 - 50)^2 + 10(50 - 50)^2 + 5(70 - 50)^2}{20} = \\dfrac{5 \\cdot 400 + 0 + 5 \\cdot 400}{20} = \\mathbf{200}$.\n"
            "- Độ lệch chuẩn: $s = \\sqrt{200} = \\mathbf{10\\sqrt{2}} \\approx 14,14$ (phút)."
        ),
        "real_life": (
            "- Đánh giá độ ổn định của nhiệt độ giữa các vùng địa lí, độ đồng đều về khối lượng sản phẩm trên dây chuyền đóng gói tự động.\n"
            "- So sánh mức độ biến động (rủi ro) của lợi suất đầu tư giữa các danh mục tài chính."
        ),
        "quiz": [
            mcq(
                "biet",
                "Cho mẫu số liệu ghép nhóm có nhóm đầu tiên là $[10; 20)$ và nhóm cuối cùng là $[50; 60)$. Khoảng biến thiên $R$ của mẫu số liệu ghép nhóm đó bằng:",
                ["$50$", "$40$", "$10$", "$60$"],
                0,
                "Khoảng biến thiên của mẫu số liệu ghép nhóm là $R = a_{k+1} - a_1 = 60 - 10 = \\mathbf{50}$.",
            ),
            mcq(
                "biet",
                "Cho mẫu số liệu ghép nhóm có tứ phân vị thứ nhất $Q_1 = 18$ và tứ phân vị thứ ba $Q_3 = 31$. Khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu đó bằng:",
                ["$13$", "$49$", "$18$", "$31$"],
                0,
                "Theo định nghĩa, khoảng tứ phân vị là $\\Delta_Q = Q_3 - Q_1 = 31 - 18 = \\mathbf{13}$.",
            ),
            mcq(
                "biet",
                "Một mẫu số liệu ghép nhóm có phương sai bằng $36$. Độ lệch chuẩn $s$ của mẫu số liệu đó bằng:",
                ["$6$", "$18$", "$1296$", "$12$"],
                0,
                "Độ lệch chuẩn là căn bậc hai số học của phương sai: $s = \\sqrt{s^2} = \\sqrt{36} = \\mathbf{6}$.",
            ),
            mcq(
                "biet",
                "Trong một mẫu số liệu ghép nhóm, giá trị đại diện của nhóm $[15; 25)$ bằng:",
                ["$20$", "$10$", "$15$", "$25$"],
                0,
                "Giá trị đại diện của nhóm $[15; 25)$ là trung bình cộng hai đầu mút: $x_i = \\dfrac{15 + 25}{2} = \\mathbf{20}$.",
            ),
            mcq(
                "hieu",
                "Khảo sát điểm kiểm tra của hai lớp $12A$ và $12B$ thu được cùng số trung bình $\\bar{x}_A = \\bar{x}_B = 7,5$, nhưng độ lệch chuẩn lần lượt là $s_A = 0,8$ và $s_B = 1,5$. Khẳng định nào dưới đây đúng?",
                [
                    "Điểm kiểm tra của lớp $12A$ đồng đều hơn lớp $12B$.",
                    "Điểm kiểm tra của lớp $12B$ đồng đều hơn lớp $12A$.",
                    "Mức độ phân tán điểm của hai lớp là như nhau.",
                    "Khoảng biến thiên của lớp $12A$ chắc chắn lớn hơn lớp $12B$.",
                ],
                0,
                "Vì $s_A = 0,8 < s_B = 1,5$ nên mức độ phân tán điểm của lớp $12A$ nhỏ hơn, tức là **điểm kiểm tra của lớp $12A$ đồng đều hơn lớp $12B$**.",
            ),
            mcq(
                "hieu",
                "Cho mẫu số liệu ghép nhóm có $3$ nhóm $[0; 10)$, $[10; 20)$, $[20; 30)$ với tần số lần lượt là $2, 6, 2$. Phương sai $s^2$ của mẫu số liệu ghép nhóm trên bằng:",
                ["$40$", "$20$", "$15$", "$100$"],
                0,
                "Cỡ mẫu $n = 10$; giá trị đại diện $x_1 = 5, x_2 = 15, x_3 = 25$; số trung bình $\\bar{x} = \\dfrac{2 \\cdot 5 + 6 \\cdot 15 + 2 \\cdot 25}{10} = 15$. Phương sai $s^2 = \\dfrac{2(5 - 15)^2 + 6(15 - 15)^2 + 2(25 - 15)^2}{10} = \\dfrac{200 + 0 + 200}{10} = \\mathbf{40}$.",
            ),
            tf4(
                "hieu",
                "Xét các tính chất của các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm. Mỗi khẳng định sau đúng hay sai?",
                [
                    "a) Khoảng biến thiên $R$ chỉ phụ thuộc vào đầu mút trái của nhóm đầu tiên và đầu mút phải của nhóm cuối cùng.",
                    "b) Khoảng tứ phân vị $\\Delta_Q$ không bị ảnh hưởng bởi các giá trị ngoại lệ (quá lớn hoặc quá nhỏ).",
                    "c) Phương sai $s^2$ luôn có cùng đơn vị đo với đơn vị của mẫu số liệu gốc.",
                    "d) Độ lệch chuẩn càng nhỏ thì các số liệu trong mẫu càng ít phân tán quanh giá trị trung bình.",
                ],
                [True, True, False, True],
                "a) $R = a_{k+1} - a_1$ nên chỉ phụ thuộc hai đầu mút ngoài cùng $\\Rightarrow$ **Đúng**.\n"
                "b) $\\Delta_Q = Q_3 - Q_1$ đo độ trải của $50\%$ số liệu ở giữa nên không bị ảnh hưởng bởi giá trị ngoại lệ $\\Rightarrow$ **Đúng**.\n"
                "c) Đơn vị của phương sai là bình phương đơn vị gốc, chỉ có độ lệch chuẩn $s$ mới cùng đơn vị với dữ liệu gốc $\\Rightarrow$ **Sai**.\n"
                "d) Độ lệch chuẩn càng nhỏ thì số liệu càng tập trung sát quanh $\\bar{x} \\Rightarrow$ **Đúng**.",
            ),
            tf4(
                "hieu",
                "Chiều cao (đơn vị: $\\text{cm}$) của $40$ cây giống được ghép thành $4$ nhóm: $[10; 20)$ có $8$ cây; $[20; 30)$ có $12$ cây; $[30; 40)$ có $12$ cây; $[40; 50)$ có $8$ cây. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Khoảng biến thiên của mẫu số liệu ghép nhóm là $R = 40\\text{ cm}$.",
                    "b) Số trung bình của mẫu số liệu ghép nhóm là $\\bar{x} = 30\\text{ cm}$.",
                    "c) Tứ phân vị thứ nhất của mẫu số liệu là $Q_1 = 20\\text{ cm}$.",
                    "d) Phương sai của mẫu số liệu ghép nhóm là $s^2 = 110$.",
                ],
                [True, True, False, True],
                "a) $R = 50 - 10 = 40\\text{ cm} \\Rightarrow$ **Đúng**.\n"
                "b) Giá trị đại diện: $15, 25, 35, 45$. Ta có $\\bar{x} = \\dfrac{8 \\cdot 15 + 12 \\cdot 25 + 12 \\cdot 35 + 8 \\cdot 45}{40} = 30\\text{ cm} \\Rightarrow$ **Đúng**.\n"
                "c) Ta có $\\dfrac{n}{4} = 10$; nhóm $[20; 30)$ chứa $Q_1$ với $C = 8, n_2 = 12 \\Rightarrow Q_1 = 20 + \\dfrac{10 - 8}{12} \\cdot 10 = \\dfrac{65}{3} \\neq 20 \\Rightarrow$ **Sai**.\n"
                "d) $s^2 = \\dfrac{8(15 - 30)^2 + 12(25 - 30)^2 + 12(35 - 30)^2 + 8(45 - 30)^2}{40} = \\dfrac{1800 + 300 + 300 + 1800}{40} = 110 \\Rightarrow$ **Đúng**.",
            ),
            mcq(
                "vandung",
                "Cho mẫu số liệu ghép nhóm gồm $20$ số liệu được chia thành $3$ nhóm: $[0; 10)$ có tần số $5$; $[10; 20)$ có tần số $10$; $[20; 30)$ có tần số $5$. Khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu ghép nhóm này bằng:",
                ["$10$", "$15$", "$20$", "$5$"],
                0,
                "Cỡ mẫu $n = 20$. Ta có $\\dfrac{n}{4} = 5$ nên nhóm $[0; 10)$ chứa $Q_1$: $Q_1 = 0 + \\dfrac{5 - 0}{5} \\cdot 10 = 10$. Tiếp theo $\\dfrac{3n}{4} = 15$, tần số tích luỹ nhóm $1$ là $5$, nhóm $2$ là $15$ nên $Q_3$ thuộc nhóm $[10; 20)$: $Q_3 = 10 + \\dfrac{15 - 5}{10} \\cdot 10 = 20$. Vậy $\\Delta_Q = Q_3 - Q_1 = 20 - 10 = \\mathbf{10}$.",
            ),
            short(
                "vandung",
                "Khối lượng (đơn vị: gam) của $10$ quả táo được chia thành $2$ nhóm: nhóm $[180; 200)$ có $5$ quả và nhóm $[200; 220)$ có $5$ quả. Tính độ lệch chuẩn $s$ của mẫu số liệu ghép nhóm trên.",
                ["10"],
                "Giá trị đại diện hai nhóm là $x_1 = 190$ và $x_2 = 210$. Số trung bình $\\bar{x} = \\dfrac{5 \\cdot 190 + 5 \\cdot 210}{10} = 200$. Phương sai $s^2 = \\dfrac{5(190 - 200)^2 + 5(210 - 200)^2}{10} = 100$. Vậy độ lệch chuẩn là $s = \\sqrt{100} = \\mathbf{10}$ gam.",
                unit="gam",
            ),
        ],
    },
    # ===================== CHƯƠNG IV =====================
    {
        "topic": "l12-ch04-nguyen-ham-va-tich-phan",
        "game_title": "Nguyên Hàm & Tích Phân: Tổng tích lũy thực tiễn",
        "game_description": "Vận dụng nguyên hàm và công thức tích phân Newton – Leibniz để tính quãng đường chuyển động, diện tích hình phẳng và thể tích vật thể.",
        "game_type": "game_nguyen_ham",
        "title": "Nguyên hàm và tích phân",
        "icon": "📐",
        "description": (
            "Chương IV · SGK Toán 12 tập hai: Bài 11 – Bài 13. Nguyên hàm; "
            "tích phân; ứng dụng hình học của tích phân."
        ),
        "requirements": [
            "Nhận biết được khái niệm nguyên hàm của một hàm số và giải thích được tính chất cơ bản của nguyên hàm.",
            "Xác định được nguyên hàm của một số hàm số sơ cấp thường gặp (hàm luỹ thừa, hàm phân thức $\\dfrac{1}{x}$, hàm lượng giác, hàm mũ).",
            "Nhận biết được định nghĩa và các tính chất của tích phân; tính được tích phân trong những trường hợp đơn giản bằng công thức Newton – Leibniz.",
            "Sử dụng được tích phân để tính diện tích của một số hình phẳng giới hạn bởi các đường cong và tính thể tích của một số hình khối tròn xoay trong không gian.",
            "Vận dụng được nguyên hàm và tích phân để giải quyết một số bài toán thực tiễn (tính quãng đường từ vận tốc, lưu lượng nước, công cơ học).",
        ],
        "definition": (
            "- **Nguyên hàm**: Cho hàm số $f(x)$ xác định trên khoảng $K$. Hàm số $F(x)$ được gọi là **nguyên hàm** của $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x \\in K$. Họ tất cả các nguyên hàm của $f(x)$ trên $K$ là $\\int f(x)\\,\\text{d}x = F(x) + C$ $(C \\in \\mathbb{R})$.\n"
            "- **Tích phân (Công thức Newton – Leibniz)**: Cho $f(x)$ là hàm số liên tục trên đoạn $[a; b]$ và $F(x)$ là một nguyên hàm của $f(x)$ trên $[a; b]$. Khi đó $\\int_a^b f(x)\\,\\text{d}x = F(x)\\Big|_a^b = F(b) - F(a)$.\n"
            "- **Diện tích hình phẳng**: Diện tích hình phẳng giới hạn bởi đồ thị $y = f(x)$, $y = g(x)$ (liên tục trên $[a; b]$) và hai đường thẳng $x = a$, $x = b$ là $S = \\int_a^b |f(x) - g(x)|\\,\\text{d}x$.\n"
            "- **Thể tích khối tròn xoay**: Quay hình phẳng giới hạn bởi $y = f(x)$, trục $Ox$, $x = a$, $x = b$ quanh trục $Ox$ tạo thành khối tròn xoay có thể tích $V = \\pi \\int_a^b [f(x)]^2\\,\\text{d}x$."
        ),
        "theory": (
            "### Bài 11. Nguyên hàm\n"
            "- **Tính chất cơ bản của nguyên hàm**: $\\int kf(x)\\,\\text{d}x = k\\int f(x)\\,\\text{d}x$ $(k \\neq 0)$ và $\\int [f(x) \\pm g(x)]\\,\\text{d}x = \\int f(x)\\,\\text{d}x \\pm \\int g(x)\\,\\text{d}x$.\n"
            "- **Bảng nguyên hàm các hàm số sơ cấp**: $\\int x^\\alpha\\,\\text{d}x = \\dfrac{x^{\\alpha+1}}{\\alpha + 1} + C$ $(\\alpha \\neq -1)$; $\\int \\dfrac{1}{x}\\,\\text{d}x = \\ln|x| + C$; $\\int e^x\\,\\text{d}x = e^x + C$; $\\int a^x\\,\\text{d}x = \\dfrac{a^x}{\\ln a} + C$; $\\int \\cos x\\,\\text{d}x = \\sin x + C$; $\\int \\sin x\\,\\text{d}x = -\\cos x + C$; $\\int \\dfrac{1}{\\cos^2 x}\\,\\text{d}x = \\tan x + C$; $\\int \\dfrac{1}{\\sin^2 x}\\,\\text{d}x = -\\cot x + C$.\n"
            "### Bài 12. Tích phân\n"
            "- **Quy ước và tính chất**: $\\int_a^a f(x)\\,\\text{d}x = 0$; $\\int_a^b f(x)\\,\\text{d}x = -\\int_b^a f(x)\\,\\text{d}x$; tính chất chèn cận $\\int_a^b f(x)\\,\\text{d}x = \\int_a^c f(x)\\,\\text{d}x + \\int_c^b f(x)\\,\\text{d}x$.\n"
            "- **Ý nghĩa vật lí**: Nếu vật chuyển động thẳng với vận tốc $v(t) \\geq 0$ thì quãng đường vật đi được từ thời điểm $t = a$ đến $t = b$ là $s = \\int_a^b v(t)\\,\\text{d}t$.\n"
            "### Bài 13. Ứng dụng hình học của tích phân\n"
            "- **Diện tích hình phẳng**: Giới hạn bởi $y = f(x)$, trục $Ox$, $x = a, x = b$ là $S = \\int_a^b |f(x)|\\,\\text{d}x$. Giới hạn bởi hai đồ thị $y = f(x)$ và $y = g(x)$ từ $x = a$ đến $x = b$ là $S = \\int_a^b |f(x) - g(x)|\\,\\text{d}x$.\n"
            "- **Thể tích vật thể**: Cắt vật thể bởi mặt phẳng vuông góc trục $Ox$ tại $x \\in [a; b]$ được thiết diện có diện tích $S(x)$ liên tục thì $V = \\int_a^b S(x)\\,\\text{d}x$. Đặc biệt, khối tròn xoay quanh $Ox$ có $V = \\pi \\int_a^b [f(x)]^2\\,\\text{d}x$.\n"
            "### Bài tập cuối chương IV"
        ),
        "formulas": [
            G(
                "I. Bảng nguyên hàm cơ bản",
                F("Nguyên hàm hàm luỹ thừa", "$\\int x^\\alpha\\,\\text{d}x = \\dfrac{x^{\\alpha+1}}{\\alpha + 1} + C \\quad (\\alpha \\neq -1) \\quad ; \\quad \\int \\dfrac{1}{x}\\,\\text{d}x = \\ln|x| + C$"),
                F("Nguyên hàm hàm mũ", "$\\int e^x\\,\\text{d}x = e^x + C \\quad ; \\quad \\int a^x\\,\\text{d}x = \\dfrac{a^x}{\\ln a} + C \\quad (0 < a \\neq 1)$"),
                F("Nguyên hàm hàm lượng giác", "$\\int \\cos x\\,\\text{d}x = \\sin x + C \\quad ; \\quad \\int \\sin x\\,\\text{d}x = -\\cos x + C$"),
                F("Nguyên hàm $\\tan, \\cot$", "$\\int \\dfrac{1}{\\cos^2 x}\\,\\text{d}x = \\tan x + C \\quad ; \\quad \\int \\dfrac{1}{\\sin^2 x}\\,\\text{d}x = -\\cot x + C$"),
            ),
            G(
                "II. Định nghĩa và tính chất tích phân",
                F("Công thức Newton – Leibniz", "$\\int_a^b f(x)\\,\\text{d}x = F(x)\\Big|_a^b = F(b) - F(a)$"),
                F("Tính chất tuyến tính", "$\\int_a^b [kf(x) \\pm lg(x)]\\,\\text{d}x = k\\int_a^b f(x)\\,\\text{d}x \\pm l\\int_a^b g(x)\\,\\text{d}x$"),
                F("Tính chất chèn cận", "$\\int_a^b f(x)\\,\\text{d}x = \\int_a^c f(x)\\,\\text{d}x + \\int_c^b f(x)\\,\\text{d}x$"),
            ),
            G(
                "III. Ứng dụng hình học và vật lí của tích phân",
                F("Diện tích hình phẳng", "$S = \\int_a^b |f(x) - g(x)|\\,\\text{d}x$"),
                F("Thể tích theo thiết diện và khối tròn xoay", "$V = \\int_a^b S(x)\\,\\text{d}x \\quad ; \\quad V_{Ox} = \\pi \\int_a^b [f(x)]^2\\,\\text{d}x$"),
                F("Quãng đường chuyển động", "$s = \\int_{t_1}^{t_2} v(t)\\,\\text{d}t \\quad (\\text{khi } v(t) \\geq 0)$"),
            ),
        ],
        "example": "Tính tích phân $I = \\int_0^2 (3x^2 - 2x + 1)\\,\\text{d}x$ và diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = x^2 - 4$, trục hoành $Ox$ và hai đường thẳng $x = 0$, $x = 2$.",
        "example_answer": (
            "- Tính tích phân: $I = \\left(x^3 - x^2 + x\\right)\\Big|_0^2 = (8 - 4 + 2) - 0 = \\mathbf{6}$.\n"
            "- Trên đoạn $[0; 2]$, ta có $x^2 - 4 \\leq 0$ nên diện tích hình phẳng là $S = \\int_0^2 |x^2 - 4|\\,\\text{d}x = \\int_0^2 (4 - x^2)\\,\\text{d}x = \\left(4x - \\dfrac{x^3}{3}\\right)\\Big|_0^2 = 8 - \\dfrac{8}{3} = \\mathbf{\\dfrac{16}{3}}$."
        ),
        "real_life": (
            "- Tính quãng đường ô tô đi được khi phanh gấp từ biểu thức vận tốc $v(t)$.\n"
            "- Tính diện tích mặt cắt cổng chào hình parabol và thể tích của bình gốm, chi tiết máy có dạng khối tròn xoay."
        ),
        "quiz": [
            mcq(
                "biet",
                "Họ tất cả các nguyên hàm của hàm số $f(x) = 4x^3 + 2x$ trên $\\mathbb{R}$ là:",
                ["$x^4 + x^2 + C$", "$12x^2 + 2 + C$", "$4x^4 + 2x^2 + C$", "$\\dfrac{x^4}{4} + x^2 + C$"],
                0,
                "Ta có $\\int (4x^3 + 2x)\\,\\text{d}x = 4 \\cdot \\dfrac{x^4}{4} + 2 \\cdot \\dfrac{x^2}{2} + C = \\mathbf{x^4 + x^2 + C}$.",
            ),
            mcq(
                "biet",
                "Trên khoảng $(0; +\\infty)$, họ tất cả các nguyên hàm của hàm số $f(x) = e^x + \\dfrac{1}{x}$ là:",
                ["$e^x + \\ln x + C$", "$e^x - \\dfrac{1}{x^2} + C$", "$e^x + \\dfrac{1}{x^2} + C$", "$xe^x + \\ln x + C$"],
                0,
                "Với $x > 0$, ta có $\\int \\left(e^x + \\dfrac{1}{x}\\right)\\text{d}x = \\mathbf{e^x + \\ln x + C}$.",
            ),
            mcq(
                "biet",
                "Giá trị của tích phân $\\int_0^1 (3x^2 + 1)\\,\\text{d}x$ bằng:",
                ["$2$", "$1$", "$4$", "$3$"],
                0,
                "Ta có $\\int_0^1 (3x^2 + 1)\\,\\text{d}x = (x^3 + x)\\Big|_0^1 = (1 + 1) - 0 = \\mathbf{2}$.",
            ),
            mcq(
                "biet",
                "Cho hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$. Diện tích $S$ của hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành $Ox$ và hai đường thẳng $x = a$, $x = b$ được tính theo công thức:",
                [
                    "$S = \\int_a^b |f(x)|\\,\\text{d}x$",
                    "$S = \\pi \\int_a^b [f(x)]^2\\,\\text{d}x$",
                    "$S = \\int_a^b f(x)\\,\\text{d}x$",
                    "$S = \\pi \\int_a^b |f(x)|\\,\\text{d}x$",
                ],
                0,
                "Theo định nghĩa, diện tích hình phẳng giới hạn bởi $y = f(x)$, trục $Ox$, $x = a, x = b$ là **$S = \\int_a^b |f(x)|\\,\\text{d}x$**.",
            ),
            mcq(
                "hieu",
                "Cho biết $\\int_1^3 f(x)\\,\\text{d}x = 5$ và $\\int_1^3 g(x)\\,\\text{d}x = -2$. Giá trị của $\\int_1^3 [2f(x) - 3g(x)]\\,\\text{d}x$ bằng:",
                ["$16$", "$4$", "$10$", "$-16$"],
                0,
                "Theo tính chất tuyến tính của tích phân: $\\int_1^3 [2f(x) - 3g(x)]\\,\\text{d}x = 2\\int_1^3 f(x)\\,\\text{d}x - 3\\int_1^3 g(x)\\,\\text{d}x = 2 \\cdot 5 - 3 \\cdot (-2) = \\mathbf{16}$.",
            ),
            mcq(
                "hieu",
                "Cho hàm số $f(x) = 2x + 3$ có một nguyên hàm là $F(x)$ thoả mãn $F(1) = 6$. Giá trị của $F(2)$ bằng:",
                ["$12$", "$10$", "$8$", "$14$"],
                0,
                "Ta có $F(x) = \\int (2x + 3)\\,\\text{d}x = x^2 + 3x + C$. Do $F(1) = 6 \\Rightarrow 1 + 3 + C = 6 \\Rightarrow C = 2$. Vậy $F(2) = 2^2 + 3 \\cdot 2 + 2 = \\mathbf{12}$.",
            ),
            tf4(
                "hieu",
                "Cho hai hàm số $f(x) = 3x^2 - 2x$ và $g(x) = \\cos x$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Một nguyên hàm của hàm số $f(x)$ trên $\\mathbb{R}$ là $F(x) = x^3 - x^2$.",
                    "b) Họ tất cả các nguyên hàm của hàm số $g(x)$ là $\\int \\cos x\\,\\text{d}x = -\\sin x + C$.",
                    "c) Tích phân $\\int_0^2 f(x)\\,\\text{d}x$ có giá trị bằng $4$.",
                    "d) Tích phân $\\int_0^{\\pi} g(x)\\,\\text{d}x$ có giá trị bằng $0$.",
                ],
                [True, False, True, True],
                "a) $(x^3 - x^2)' = 3x^2 - 2x = f(x) \\Rightarrow$ **Đúng**.\n"
                "b) $\\int \\cos x\\,\\text{d}x = \\sin x + C$ (không có dấu trừ) $\\Rightarrow$ **Sai**.\n"
                "c) $\\int_0^2 (3x^2 - 2x)\\,\\text{d}x = (x^3 - x^2)\\Big|_0^2 = 8 - 4 = 4 \\Rightarrow$ **Đúng**.\n"
                "d) $\\int_0^{\\pi} \\cos x\\,\\text{d}x = \\sin x\\Big|_0^{\\pi} = \\sin\\pi - \\sin 0 = 0 \\Rightarrow$ **Đúng**.",
            ),
            tf4(
                "hieu",
                "Xét hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = x^2$, trục hoành $Ox$ và hai đường thẳng $x = 0$, $x = 2$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Diện tích của hình phẳng $(H)$ được tính bởi công thức $S = \\int_0^2 x^2\\,\\text{d}x$.",
                    "b) Giá trị diện tích của hình phẳng $(H)$ bằng $\\dfrac{8}{3}$.",
                    "c) Thể tích khối tròn xoay khi quay $(H)$ quanh trục $Ox$ là $V = \\int_0^2 x^4\\,\\text{d}x$.",
                    "d) Thể tích khối tròn xoay khi quay $(H)$ quanh trục $Ox$ bằng $\\dfrac{32\\pi}{5}$.",
                ],
                [True, True, False, True],
                "a) Vì $x^2 \\geq 0$ trên $[0; 2]$ nên $S = \\int_0^2 |x^2|\\,\\text{d}x = \\int_0^2 x^2\\,\\text{d}x \\Rightarrow$ **Đúng**.\n"
                "b) $S = \\dfrac{x^3}{3}\\Big|_0^2 = \\dfrac{8}{3} \\Rightarrow$ **Đúng**.\n"
                "c) Công thức thể tích khối tròn xoay quanh $Ox$ phải có thừa số $\\pi$: $V = \\pi \\int_0^2 x^4\\,\\text{d}x \\Rightarrow$ **Sai**.\n"
                "d) $V = \\pi \\cdot \\dfrac{x^5}{5}\\Big|_0^2 = \\dfrac{32\\pi}{5} \\Rightarrow$ **Đúng**.",
            ),
            mcq(
                "vandung",
                "Diện tích hình phẳng giới hạn bởi parabol $y = x^2 - 2x$ và đường thẳng $y = x$ bằng:",
                ["$\\dfrac{9}{2}$", "$\\dfrac{7}{2}$", "$9$", "$\\dfrac{9}{4}$"],
                0,
                "Phương trình hoành độ giao điểm: $x^2 - 2x = x \\Leftrightarrow x^2 - 3x = 0 \\Leftrightarrow x = 0$ hoặc $x = 3$. Trên $[0; 3]$, ta có $x \\geq x^2 - 2x$ nên diện tích cần tìm là $S = \\int_0^3 (3x - x^2)\\,\\text{d}x = \\left(\\dfrac{3x^2}{2} - \\dfrac{x^3}{3}\\right)\\Big|_0^3 = \\dfrac{27}{2} - 9 = \\mathbf{\\dfrac{9}{2}}$.",
            ),
            short(
                "vandung",
                "Một ô tô đang chạy với vận tốc $20\\text{ m}\\cdot\\text{s}^{-1}$ thì người lái đạp phanh; từ thời điểm đó ô tô chuyển động chậm dần đều với vận tốc $v(t) = 20 - 5t$ (đơn vị: $\\text{m}\\cdot\\text{s}^{-1}$), trong đó $t$ là thời gian tính bằng giây kể từ lúc bắt đầu đạp phanh. Hỏi từ lúc đạp phanh đến khi dừng hẳn, ô tô còn di chuyển được bao nhiêu mét?",
                ["40"],
                "Khi ô tô dừng hẳn thì $v(t) = 0 \\Leftrightarrow 20 - 5t = 0 \\Leftrightarrow t = 4\\text{ (s)}$. Quãng đường ô tô đi được từ lúc đạp phanh đến khi dừng hẳn là $s = \\int_0^4 (20 - 5t)\\,\\text{d}t = \\left(20t - \\dfrac{5t^2}{2}\\right)\\Big|_0^4 = 80 - 40 = \\mathbf{40}\\text{ (m)}$.",
                unit="m",
            ),
        ],
    },
    # ===================== CHƯƠNG V =====================
    {
        "topic": "l12-ch05-phuong-phap-toa-do-trong-khong-gian",
        "game_title": "Không gian Oxyz: Phương trình Mặt phẳng, Đường thẳng & Mặt cầu",
        "game_description": "Mô hình hóa không gian ba chiều Oxyz để xác định tọa độ, khoảng cách, góc và vị trí tương đối giữa mặt phẳng, đường thẳng và mặt cầu.",
        "game_type": "game_toa_do_oxyz",
        "title": "Phương pháp toạ độ trong không gian",
        "icon": "🌐",
        "description": (
            "Chương V · SGK Toán 12 tập hai: Bài 14 – Bài 17. Phương trình mặt phẳng; "
            "phương trình đường thẳng trong không gian; công thức tính góc trong không gian; phương trình mặt cầu."
        ),
        "requirements": [
            "Nhận biết được khái niệm vectơ pháp tuyến của mặt phẳng, viết được phương trình tổng quát của mặt phẳng và tính được khoảng cách từ một điểm đến một mặt phẳng.",
            "Nhận biết được vectơ chỉ phương của đường thẳng; viết được phương trình tham số và phương trình chính tắc của đường thẳng trong không gian; xét được vị trí tương đối giữa hai đường thẳng.",
            "Vận dụng được công thức tính góc giữa hai đường thẳng, góc giữa đường thẳng và mặt phẳng, góc giữa hai mặt phẳng trong không gian.",
            "Nhận biết được phương trình mặt cầu, xác định được tâm và bán kính mặt cầu, lập được phương trình mặt cầu và giải quyết các bài toán thực tiễn liên quan (vùng phủ sóng radar, định vị vệ tinh).",
        ],
        "definition": (
            "- **Phương trình tổng quát của mặt phẳng**: Trong không gian $Oxyz$, mọi mặt phẳng đều có phương trình dạng $Ax + By + Cz + D = 0$ với $A^2 + B^2 + C^2 > 0$, nhận $\\overrightarrow{n} = (A; B; C)$ làm một **vectơ pháp tuyến**.\n"
            "- **Phương trình đường thẳng**: Đường thẳng $\\Delta$ đi qua $M_0(x_0; y_0; z_0)$ và có **vectơ chỉ phương** $\\overrightarrow{u} = (a; b; c) \\neq \\overrightarrow{0}$ có phương trình tham số $x = x_0 + at, y = y_0 + bt, z = z_0 + ct$ $(t \\in \\mathbb{R})$ và phương trình chính tắc $\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c}$ (khi $abc \\neq 0$).\n"
            "- **Phương trình mặt cầu**: Mặt cầu $(S)$ tâm $I(a; b; c)$, bán kính $R > 0$ có phương trình $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$."
        ),
        "theory": (
            "### Bài 14. Phương trình mặt phẳng\n"
            "- **Tích có hướng của hai vectơ**: Cho $\\overrightarrow{u} = (x_1; y_1; z_1)$ và $\\overrightarrow{v} = (x_2; y_2; z_2)$. Vectơ $\\left[\\overrightarrow{u}, \\overrightarrow{v}\\right] = (y_1z_2 - z_1y_2; z_1x_2 - x_1z_2; x_1y_2 - y_1x_2)$ vuông góc với cả $\\overrightarrow{u}$ và $\\overrightarrow{v}$. Nếu mặt phẳng $(\\alpha)$ có cặp vectơ chỉ phương không cùng phương $\\overrightarrow{u}, \\overrightarrow{v}$ thì $\\overrightarrow{n} = \\left[\\overrightarrow{u}, \\overrightarrow{v}\\right]$ là một vectơ pháp tuyến.\n"
            "- **Mặt phẳng qua $M_0(x_0; y_0; z_0)$ có vectơ pháp tuyến $\\overrightarrow{n} = (A; B; C)$**: $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$.\n"
            "- **Phương trình mặt phẳng theo đoạn chắn**: Đi qua $A(a; 0; 0)$, $B(0; b; 0)$, $C(0; 0; c)$ với $abc \\neq 0$ là $\\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1$.\n"
            "- **Khoảng cách từ điểm $M_0(x_0; y_0; z_0)$ đến mặt phẳng $(P): Ax + By + Cz + D = 0$**: $d(M_0, (P)) = \\dfrac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}$.\n"
            "### Bài 15. Phương trình đường thẳng trong không gian\n"
            "- **Vị trí tương đối của hai đường thẳng**: Trong không gian, hai đường thẳng có thể song song, trùng nhau, cắt nhau hoặc chéo nhau.\n"
            "### Bài 16. Công thức tính góc trong không gian\n"
            "- **Góc giữa hai đường thẳng $\\Delta_1, \\Delta_2$** (có vectơ chỉ phương $\\overrightarrow{u_1}, \\overrightarrow{u_2}$): $\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\overrightarrow{u_1} \\cdot \\overrightarrow{u_2}|}{|\\overrightarrow{u_1}| \\cdot |\\overrightarrow{u_2}|}$.\n"
            "- **Góc giữa đường thẳng $\\Delta$** (vectơ chỉ phương $\\overrightarrow{u}$) và **mặt phẳng $(P)$** (vectơ pháp tuyến $\\overrightarrow{n}$): $\\sin(\\Delta, (P)) = \\dfrac{|\\overrightarrow{u} \\cdot \\overrightarrow{n}|}{|\\overrightarrow{u}| \\cdot |\\overrightarrow{n}|}$.\n"
            "- **Góc giữa hai mặt phẳng $(P_1), (P_2)$** (vectơ pháp tuyến $\\overrightarrow{n_1}, \\overrightarrow{n_2}$): $\\cos((P_1), (P_2)) = \\dfrac{|\\overrightarrow{n_1} \\cdot \\overrightarrow{n_2}|}{|\\overrightarrow{n_1}| \\cdot |\\overrightarrow{n_2}|}$.\n"
            "### Bài 17. Phương trình mặt cầu\n"
            "- **Dạng khai triển**: Phương trình $x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$ là phương trình mặt cầu khi và chỉ khi $a^2 + b^2 + c^2 - d > 0$; khi đó tâm là $I(a; b; c)$ và bán kính $R = \\sqrt{a^2 + b^2 + c^2 - d}$.\n"
            "### Bài tập cuối chương V"
        ),
        "formulas": [
            G(
                "I. Phương trình mặt phẳng và khoảng cách",
                F("Phương trình tổng quát mặt phẳng", "$Ax + By + Cz + D = 0 \\quad (\\overrightarrow{n} = (A; B; C))$"),
                F("Phương trình theo đoạn chắn", "$\\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1 \\quad (abc \\neq 0)$"),
                F("Khoảng cách từ điểm đến mặt phẳng", "$d(M_0, (P)) = \\dfrac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}$"),
            ),
            G(
                "II. Phương trình đường thẳng và góc trong không gian",
                F("Phương trình chính tắc đường thẳng", "$\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c} \\quad (\\overrightarrow{u} = (a; b; c))$"),
                F("Góc giữa hai đường thẳng", "$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\overrightarrow{u_1} \\cdot \\overrightarrow{u_2}|}{|\\overrightarrow{u_1}| \\cdot |\\overrightarrow{u_2}|}$"),
                F("Góc giữa đường thẳng và mặt phẳng", "$\\sin(\\Delta, (P)) = \\dfrac{|\\overrightarrow{u} \\cdot \\overrightarrow{n}|}{|\\overrightarrow{u}| \\cdot |\\overrightarrow{n}|}$"),
                F("Góc giữa hai mặt phẳng", "$\\cos((P_1), (P_2)) = \\dfrac{|\\overrightarrow{n_1} \\cdot \\overrightarrow{n_2}|}{|\\overrightarrow{n_1}| \\cdot |\\overrightarrow{n_2}|}$"),
            ),
            G(
                "III. Phương trình mặt cầu",
                F("Phương trình chính tắc mặt cầu", "$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$"),
                F("Bán kính từ dạng khai triển", "$R = \\sqrt{a^2 + b^2 + c^2 - d} \\quad (a^2 + b^2 + c^2 - d > 0)$"),
            ),
        ],
        "example": (
            "Trong không gian $Oxyz$, cho điểm $I(1; -2; 3)$ và mặt phẳng $(P): 2x - 2y + z + 3 = 0$. "
            "Tính khoảng cách từ $I$ đến $(P)$ và viết phương trình mặt cầu $(S)$ tâm $I$ tiếp xúc với mặt phẳng $(P)$."
        ),
        "example_answer": (
            "- Khoảng cách từ tâm $I(1; -2; 3)$ đến mặt phẳng $(P)$ là:\n"
            "  $d(I, (P)) = \\dfrac{|2 \\cdot 1 - 2 \\cdot (-2) + 1 \\cdot 3 + 3|}{\\sqrt{2^2 + (-2)^2 + 1^2}} = \\dfrac{12}{3} = \\mathbf{4}$.\n"
            "- Vì mặt cầu $(S)$ tiếp xúc với $(P)$ nên bán kính mặt cầu là $R = d(I, (P)) = 4$.\n"
            "- Phương trình mặt cầu $(S)$ là: $\\mathbf{(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 16}$."
        ),
        "real_life": (
            "- Xác định vùng phủ sóng hình cầu của trạm radar hàng không hoặc trạm phát sóng viễn thông.\n"
            "- Kiểm tra hành trình bay thẳng của máy bay trong không gian xem có đi vào vùng phủ sóng hoặc vùng cấm bay hay không."
        ),
        "quiz": [
            mcq(
                "biet",
                "Trong không gian $Oxyz$, mặt phẳng $(P): 2x - 3y + 5z - 7 = 0$ có một vectơ pháp tuyến là:",
                [
                    "$\\overrightarrow{n} = (2; -3; 5)$",
                    "$\\overrightarrow{n} = (2; 3; 5)$",
                    "$\\overrightarrow{n} = (-3; 5; -7)$",
                    "$\\overrightarrow{n} = (2; -3; -7)$",
                ],
                0,
                "Mặt phẳng $Ax + By + Cz + D = 0$ nhận $\\overrightarrow{n} = (A; B; C) = \\mathbf{(2; -3; 5)}$ làm một vectơ pháp tuyến.",
            ),
            mcq(
                "biet",
                "Trong không gian $Oxyz$, đường thẳng $d: \\dfrac{x - 1}{2} = \\dfrac{y + 2}{-1} = \\dfrac{z - 3}{4}$ có một vectơ chỉ phương là:",
                [
                    "$\\overrightarrow{u} = (2; -1; 4)$",
                    "$\\overrightarrow{u} = (1; -2; 3)$",
                    "$\\overrightarrow{u} = (-1; 2; -3)$",
                    "$\\overrightarrow{u} = (2; 1; 4)$",
                ],
                0,
                "Đường thẳng có phương trình chính tắc $\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c}$ nhận $\\overrightarrow{u} = (a; b; c) = \\mathbf{(2; -1; 4)}$ làm vectơ chỉ phương.",
            ),
            mcq(
                "biet",
                "Trong không gian $Oxyz$, mặt cầu $(S): (x - 1)^2 + (y + 3)^2 + (z - 2)^2 = 9$ có tâm $I$ và bán kính $R$ lần lượt là:",
                [
                    "$I(1; -3; 2), R = 3$",
                    "$I(-1; 3; -2), R = 3$",
                    "$I(1; -3; 2), R = 9$",
                    "$I(1; 3; 2), R = 3$",
                ],
                0,
                "Từ phương trình $(x - 1)^2 + (y + 3)^2 + (z - 2)^2 = 3^2$, suy ra tâm **$I(1; -3; 2)$** và bán kính **$R = 3$**.",
            ),
            mcq(
                "biet",
                "Trong không gian $Oxyz$, khoảng cách từ điểm $M(1; 2; 1)$ đến mặt phẳng $(P): 2x - y + 2z + 5 = 0$ bằng:",
                ["$3$", "$9$", "$2$", "$4$"],
                0,
                "Ta có $d(M, (P)) = \\dfrac{|2 \\cdot 1 - 1 \\cdot 2 + 2 \\cdot 1 + 5|}{\\sqrt{2^2 + (-1)^2 + 2^2}} = \\dfrac{7 + 2}{3} = \\mathbf{3}$.",
            ),
            mcq(
                "hieu",
                "Trong không gian $Oxyz$, phương trình mặt phẳng đi qua điểm $A(1; 0; -2)$ và vuông góc với đường thẳng $d: \\dfrac{x}{2} = \\dfrac{y - 1}{1} = \\dfrac{z + 3}{-3}$ là:",
                [
                    "$2x + y - 3z - 8 = 0$",
                    "$2x + y - 3z + 8 = 0$",
                    "$x - 2z - 5 = 0$",
                    "$2x - y - 3z - 8 = 0$",
                ],
                0,
                "Mặt phẳng vuông góc với $d$ nên nhận vectơ chỉ phương của $d$ là $\\overrightarrow{n} = (2; 1; -3)$ làm vectơ pháp tuyến. Phương trình mặt phẳng là $2(x - 1) + 1(y - 0) - 3(z + 2) = 0 \\Leftrightarrow \\mathbf{2x + y - 3z - 8 = 0}$.",
            ),
            mcq(
                "hieu",
                "Trong không gian $Oxyz$, góc giữa đường thẳng $d: \\dfrac{x}{1} = \\dfrac{y}{1} = \\dfrac{z}{0}$ và mặt phẳng $(P): x + y + \\sqrt{2}z - 1 = 0$ bằng:",
                ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"],
                0,
                "Đường thẳng $d$ có $\\overrightarrow{u} = (1; 1; 0)$ với $|\\overrightarrow{u}| = \\sqrt{2}$; mặt phẳng $(P)$ có $\\overrightarrow{n} = (1; 1; \\sqrt{2})$ với $|\\overrightarrow{n}| = 2$. Ta có $\\sin(d, (P)) = \\dfrac{|1 \\cdot 1 + 1 \\cdot 1 + 0 \\cdot \\sqrt{2}|}{\\sqrt{2} \\cdot 2} = \\dfrac{2}{2\\sqrt{2}} = \\dfrac{\\sqrt{2}}{2} \\Rightarrow (d, (P)) = \\mathbf{45^\\circ}$.",
            ),
            tf4(
                "hieu",
                "Trong không gian $Oxyz$, cho điểm $A(1; 2; -1)$ và mặt phẳng $(P): x - 2y + 2z + 6 = 0$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Vectơ $\\overrightarrow{n} = (1; -2; 2)$ là một vectơ pháp tuyến của mặt phẳng $(P)$.",
                    "b) Điểm $A(1; 2; -1)$ thuộc mặt phẳng $(P)$.",
                    "c) Khoảng cách từ gốc toạ độ $O(0; 0; 0)$ đến mặt phẳng $(P)$ bằng $2$.",
                    "d) Đường thẳng đi qua $A$ và vuông góc với $(P)$ có phương trình tham số là $x = 1 + t, y = 2 - 2t, z = -1 + 2t$.",
                ],
                [True, False, True, True],
                "a) Hệ số của $x, y, z$ trong $(P)$ là $(1; -2; 2) \\Rightarrow$ **Đúng**.\n"
                "b) Thay toạ độ $A$ vào $(P)$: $1 - 2 \\cdot 2 + 2 \\cdot (-1) + 6 = 1 \\neq 0$ nên $A \\notin (P) \\Rightarrow$ **Sai**.\n"
                "c) $d(O, (P)) = \\dfrac{|6|}{\\sqrt{1^2 + (-2)^2 + 2^2}} = \\dfrac{6}{3} = 2 \\Rightarrow$ **Đúng**.\n"
                "d) Đường thẳng qua $A(1; 2; -1)$ vuông góc với $(P)$ nhận $\\overrightarrow{n} = (1; -2; 2)$ làm vectơ chỉ phương nên có phương trình $x = 1 + t, y = 2 - 2t, z = -1 + 2t \\Rightarrow$ **Đúng**.",
            ),
            tf4(
                "hieu",
                "Trong không gian $Oxyz$, cho phương trình $x^2 + y^2 + z^2 - 2x + 4y - 6z - 11 = 0$ $(1)$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Phương trình $(1)$ là phương trình của một mặt cầu $(S)$.",
                    "b) Tâm của mặt cầu $(S)$ có toạ độ là $I(-1; 2; -3)$.",
                    "c) Bán kính của mặt cầu $(S)$ bằng $5$.",
                    "d) Điểm $M(1; 1; 7)$ nằm trên mặt cầu $(S)$.",
                ],
                [True, False, True, True],
                "a) Ta có $a = 1, b = -2, c = 3, d = -11 \\Rightarrow a^2 + b^2 + c^2 - d = 1 + 4 + 9 + 11 = 25 > 0$ nên $(1)$ là phương trình mặt cầu $\\Rightarrow$ **Đúng**.\n"
                "b) Tâm mặt cầu là $I(1; -2; 3)$ chứ không phải $(-1; 2; -3) \\Rightarrow$ **Sai**.\n"
                "c) Bán kính $R = \\sqrt{25} = 5 \\Rightarrow$ **Đúng**.\n"
                "d) Ta có $IM = \\sqrt{(1 - 1)^2 + (1 + 2)^2 + (7 - 3)^2} = \\sqrt{0 + 9 + 16} = 5 = R$ nên $M \\in (S) \\Rightarrow$ **Đúng**.",
            ),
            mcq(
                "vandung",
                "Trong không gian $Oxyz$, mặt phẳng $(P)$ đi qua ba điểm $A(2; 0; 0)$, $B(0; 3; 0)$, $C(0; 0; 6)$ có phương trình tổng quát là:",
                [
                    "$3x + 2y + z - 6 = 0$",
                    "$2x + 3y + 6z - 6 = 0$",
                    "$3x + 2y + z + 6 = 0$",
                    "$x + 2y + 3z - 6 = 0$",
                ],
                0,
                "Theo phương trình mặt phẳng theo đoạn chắn: $\\dfrac{x}{2} + \\dfrac{y}{3} + \\dfrac{z}{6} = 1 \\Leftrightarrow \\mathbf{3x + 2y + z - 6 = 0}$.",
            ),
            short(
                "vandung",
                "Trong không gian $Oxyz$ (đơn vị trên mỗi trục là kilômét), một trạm radar đặt tại điểm $I(2; 3; 1)$ có bán kính quét sóng tối đa là $10\\text{ km}$. Một thiết bị bay ở vị trí $M(8; 11; 1)$. Hỏi khoảng cách từ thiết bị bay $M$ đến trạm radar $I$ bằng bao nhiêu kilômét?",
                ["10"],
                "Khoảng cách từ $M(8; 11; 1)$ đến trạm radar $I(2; 3; 1)$ là $IM = \\sqrt{(8 - 2)^2 + (11 - 3)^2 + (1 - 1)^2} = \\sqrt{36 + 64 + 0} = \\sqrt{100} = \\mathbf{10}\\text{ km}$.",
                unit="km",
            ),
        ],
    },
    # ===================== CHƯƠNG VI =====================
    {
        "topic": "l12-ch06-xac-suat-co-dieu-kien",
        "game_title": "Tổng ôn Toán THPT & Mô hình hóa Xác suất Bayes thực tiễn",
        "game_description": "Vận dụng xác suất có điều kiện, công thức xác suất toàn phần và công thức Bayes để phân tích quyết định trong y học, kiểm định chất lượng và dự báo.",
        "game_type": "game_on_tap_thpt",
        "title": "Xác suất có điều kiện",
        "icon": "🎲",
        "description": (
            "Chương VI · SGK Toán 12 tập hai: Bài 18 – Bài 19. Xác suất có điều kiện; "
            "công thức xác suất toàn phần và công thức Bayes."
        ),
        "requirements": [
            "Nhận biết được khái niệm xác suất có điều kiện và giải thích được ý nghĩa của xác suất có điều kiện trong những tình huống thực tiễn quen thuộc.",
            "Sử dụng được công thức tính xác suất có điều kiện $P(A|B) = \\dfrac{P(AB)}{P(B)}$ và công thức nhân xác suất $P(AB) = P(B) \\cdot P(A|B)$.",
            "Mô tả được công thức xác suất toàn phần, công thức Bayes thông qua bảng dữ liệu thống kê $2 \\times 2$ và sơ đồ hình cây.",
            "Sử dụng được công thức xác suất toàn phần và công thức Bayes để tính xác suất trong một số bài toán thực tiễn (chẩn đoán y khoa, kiểm định chất lượng sản phẩm).",
        ],
        "definition": (
            "- **Xác suất có điều kiện**: Cho hai biến cố $A$ và $B$ với $P(B) > 0$. Xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra được ký hiệu là $P(A|B)$ và xác định bởi công thức $P(A|B) = \\dfrac{P(AB)}{P(B)}$.\n"
            "- **Công thức nhân xác suất**: Với hai biến cố $A, B$ bất kỳ, $P(AB) = P(B) \\cdot P(A|B) = P(A) \\cdot P(B|A)$ (khi $P(A) > 0, P(B) > 0$).\n"
            "- **Công thức xác suất toàn phần**: Cho hai biến cố $A$ và $B$ với $0 < P(B) < 1$, khi đó $P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B})$.\n"
            "- **Công thức Bayes**: Với $P(A) > 0$ và $0 < P(B) < 1$, ta có $P(B|A) = \\dfrac{P(B) \\cdot P(A|B)}{P(A)} = \\dfrac{P(B) \\cdot P(A|B)}{P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B})}$."
        ),
        "theory": (
            "### Bài 18. Xác suất có điều kiện\n"
            "- **Tính chất**: Với $P(B) > 0$, ta luôn có $0 \\leq P(A|B) \\leq 1$ và $P(\\overline{A}|B) = 1 - P(A|B)$.\n"
            "- **Liên hệ với biến cố độc lập**: Hai biến cố $A$ và $B$ (với $0 < P(A) < 1, 0 < P(B) < 1$) độc lập khi và chỉ khi $P(A|B) = P(A) = P(A|\\overline{B})$, tương đương với $P(AB) = P(A) \\cdot P(B)$.\n"
            "- **Tính trực tiếp trong không gian mẫu đồng khả năng**: $P(A|B) = \\dfrac{n(AB)}{n(B)}$, trong đó $n(B)$ và $n(AB)$ là số phần tử của $B$ và $AB$.\n"
            "### Bài 19. Công thức xác suất toàn phần và công thức Bayes\n"
            "- **Sử dụng sơ đồ hình cây**: Nhánh cấp $1$ biểu diễn biến cố điều kiện $B$ và $\\overline{B}$ với xác suất $P(B), P(\\overline{B})$; nhánh cấp $2$ biểu diễn $A$ và $\\overline{A}$ với xác suất có điều kiện $P(A|B), P(A|\\overline{B})$.\n"
            "- **Ý nghĩa của công thức Bayes**: Cho phép cập nhật xác suất xảy ra của nguyên nhân $B$ sau khi đã quan sát thấy kết quả $A$ xảy ra.\n"
            "### Bài tập cuối chương VI"
        ),
        "formulas": [
            G(
                "I. Xác suất có điều kiện và công thức nhân",
                F("Định nghĩa xác suất có điều kiện", "$P(A|B) = \\dfrac{P(AB)}{P(B)} \\quad (P(B) > 0)$"),
                F("Trường hợp đồng khả năng", "$P(A|B) = \\dfrac{n(AB)}{n(B)}$"),
                F("Biến cố đối có điều kiện", "$P(\\overline{A}|B) = 1 - P(A|B)$"),
                F("Công thức nhân xác suất", "$P(AB) = P(B) \\cdot P(A|B) = P(A) \\cdot P(B|A)$"),
            ),
            G(
                "II. Công thức xác suất toàn phần và công thức Bayes",
                F("Công thức xác suất toàn phần", "$P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B})$"),
                F("Công thức Bayes", "$P(B|A) = \\dfrac{P(B) \\cdot P(A|B)}{P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B})}$"),
            ),
        ],
        "example": (
            "Một nhà máy có hai dây chuyền sản xuất $I$ và $II$ cung cấp lần lượt $60\%$ và $40\%$ tổng sản lượng. "
            "Tỉ lệ phế phẩm của dây chuyền $I$ là $2\%$ và của dây chuyền $II$ là $3\%$. Chọn ngẫu nhiên một sản phẩm của nhà máy. "
            "Tính xác suất để sản phẩm đó là phế phẩm; nếu biết sản phẩm đó là phế phẩm, tính xác suất nó do dây chuyền $I$ sản xuất."
        ),
        "example_answer": (
            "Gọi $B$ là biến cố “Sản phẩm do dây chuyền $I$ sản xuất” $\\Rightarrow P(B) = 0,6$ và $P(\\overline{B}) = 0,4$. Gọi $A$ là biến cố “Sản phẩm là phế phẩm” $\\Rightarrow P(A|B) = 0,02$ và $P(A|\\overline{B}) = 0,03$.\n"
            "- Theo công thức xác suất toàn phần: $P(A) = 0,6 \\cdot 0,02 + 0,4 \\cdot 0,03 = 0,012 + 0,012 = \\mathbf{0,024}$.\n"
            "- Theo công thức Bayes, xác suất phế phẩm đó do dây chuyền $I$ sản xuất là: $P(B|A) = \\dfrac{0,6 \\cdot 0,02}{0,024} = \\dfrac{0,012}{0,024} = \\mathbf{0,5}$."
        ),
        "real_life": (
            "- Đánh giá độ chính xác thực tế của xét nghiệm y tế (xác suất một người thực sự mắc bệnh khi có kết quả xét nghiệm dương tính).\n"
            "- Truy xuất nguồn gốc lỗi sản phẩm giữa các phân xưởng sản xuất và lọc thư rác (spam filter) trong trí tuệ nhân tạo."
        ),
        "quiz": [
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ với $P(B) > 0$. Công thức tính xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra là:",
                [
                    "$P(A|B) = \\dfrac{P(AB)}{P(B)}$",
                    "$P(A|B) = \\dfrac{P(AB)}{P(A)}$",
                    "$P(A|B) = P(A) \\cdot P(B)$",
                    "$P(A|B) = \\dfrac{P(A)}{P(B)}$",
                ],
                0,
                "Theo định nghĩa xác suất có điều kiện, với $P(B) > 0$ ta có **$P(A|B) = \\dfrac{P(AB)}{P(B)}$**.",
            ),
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ thoả mãn $P(B) = 0,5$ và $P(AB) = 0,2$. Giá trị của $P(A|B)$ bằng:",
                ["$0,4$", "$0,1$", "$0,7$", "$0,25$"],
                0,
                "Áp dụng công thức $P(A|B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{0,2}{0,5} = \\mathbf{0,4}$.",
            ),
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ thoả mãn $P(A) = 0,6$ và $P(B|A) = 0,5$. Xác suất của biến cố giao $AB$ bằng:",
                ["$0,3$", "$0,1$", "$0,8$", "$0,55$"],
                0,
                "Theo công thức nhân xác suất: $P(AB) = P(A) \\cdot P(B|A) = 0,6 \\cdot 0,5 = \\mathbf{0,3}$.",
            ),
            mcq(
                "biet",
                "Cho hai biến cố $A$ và $B$ với $P(B) > 0$ và $P(A|B) = 0,35$. Khi đó $P(\\overline{A}|B)$ bằng:",
                ["$0,65$", "$0,35$", "$0,5$", "$0,75$"],
                0,
                "Theo tính chất của xác suất có điều kiện: $P(\\overline{A}|B) = 1 - P(A|B) = 1 - 0,35 = \\mathbf{0,65}$.",
            ),
            mcq(
                "hieu",
                "Một lớp học có $40$ học sinh, trong đó có $25$ học sinh thích môn Toán, $20$ học sinh thích môn Vật lí và $15$ học sinh thích cả hai môn Toán và Vật lí. Chọn ngẫu nhiên một học sinh trong lớp. Biết rằng học sinh đó thích môn Toán, xác suất để học sinh đó cũng thích môn Vật lí bằng:",
                ["$\\dfrac{3}{5}$", "$\\dfrac{3}{4}$", "$\\dfrac{3}{8}$", "$\\dfrac{1}{2}$"],
                0,
                "Gọi $A$ là biến cố “Học sinh thích môn Vật lí”, $B$ là biến cố “Học sinh thích môn Toán”. Ta có $n(B) = 25$ và $n(AB) = 15$, suy ra $P(A|B) = \\dfrac{n(AB)}{n(B)} = \\dfrac{15}{25} = \\mathbf{\\dfrac{3}{5}}$.",
            ),
            mcq(
                "hieu",
                "Cho hai biến cố $A$ và $B$ thoả mãn $P(B) = 0,4$, $P(A|B) = 0,7$ và $P(A|\\overline{B}) = 0,2$. Theo công thức xác suất toàn phần, xác suất $P(A)$ bằng:",
                ["$0,4$", "$0,45$", "$0,9$", "$0,28$"],
                0,
                "Ta có $P(\\overline{B}) = 1 - P(B) = 0,6$. Áp dụng công thức xác suất toàn phần: $P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B}) = 0,4 \\cdot 0,7 + 0,6 \\cdot 0,2 = 0,28 + 0,12 = \\mathbf{0,4}$.",
            ),
            tf4(
                "hieu",
                "Một hộp có $6$ bi trắng và $4$ bi đen cùng kích thước. Lấy ngẫu nhiên lần lượt $2$ viên bi không hoàn lại. Gọi $A$ là biến cố “Viên bi thứ nhất màu trắng” và $B$ là biến cố “Viên bi thứ hai màu trắng”. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Xác suất của biến cố $A$ là $P(A) = \\dfrac{3}{5}$.",
                    "b) Biết viên thứ nhất màu trắng, xác suất viên thứ hai màu trắng là $P(B|A) = \\dfrac{5}{9}$.",
                    "c) Xác suất cả hai viên bi lấy ra đều màu trắng là $P(AB) = \\dfrac{1}{3}$.",
                    "d) Hai biến cố $A$ và $B$ là hai biến cố độc lập.",
                ],
                [True, True, True, False],
                "a) $P(A) = \\dfrac{6}{10} = \\dfrac{3}{5} \\Rightarrow$ **Đúng**.\n"
                "b) Khi $A$ đã xảy ra, trong hộp còn $9$ bi gồm $5$ bi trắng nên $P(B|A) = \\dfrac{5}{9} \\Rightarrow$ **Đúng**.\n"
                "c) $P(AB) = P(A) \\cdot P(B|A) = \\dfrac{3}{5} \\cdot \\dfrac{5}{9} = \\dfrac{1}{3} \\Rightarrow$ **Đúng**.\n"
                "d) Vì lấy không hoàn lại nên $P(B|A) = \\dfrac{5}{9} \\neq P(B|\\overline{A}) = \\dfrac{6}{9}$, do đó $A$ và $B$ không độc lập $\\Rightarrow$ **Sai**.",
            ),
            tf4(
                "hieu",
                "Cho hai biến cố $A$ và $B$ thoả mãn $P(B) = 0,8$, $P(\\overline{B}) = 0,2$, $P(A|B) = 0,5$ và $P(A|\\overline{B}) = 0,5$. Xét tính đúng sai của các mệnh đề sau:",
                [
                    "a) Xác suất $P(AB)$ bằng $0,4$.",
                    "b) Theo công thức xác suất toàn phần, $P(A) = 0,5$.",
                    "c) Theo công thức Bayes, $P(B|A) = 0,6$.",
                    "d) Hai biến cố $A$ và $B$ là hai biến cố độc lập.",
                ],
                [True, True, False, True],
                "a) $P(AB) = P(B) \\cdot P(A|B) = 0,8 \\cdot 0,5 = 0,4 \\Rightarrow$ **Đúng**.\n"
                "b) $P(A) = 0,8 \\cdot 0,5 + 0,2 \\cdot 0,5 = 0,4 + 0,1 = 0,5 \\Rightarrow$ **Đúng**.\n"
                "c) Theo công thức Bayes: $P(B|A) = \\dfrac{P(AB)}{P(A)} = \\dfrac{0,4}{0,5} = 0,8 \\neq 0,6 \\Rightarrow$ **Sai**.\n"
                "d) Vì $P(AB) = 0,4 = P(A) \\cdot P(B)$ nên $A$ và $B$ độc lập $\\Rightarrow$ **Đúng**.",
            ),
            mcq(
                "vandung",
                "Một căn bệnh có tỉ lệ người mắc trong cộng đồng là $1\%$. Một xét nghiệm chẩn đoán cho kết quả dương tính với $99\%$ người mắc bệnh và cho kết quả dương tính giả với $1\%$ người không mắc bệnh. Chọn ngẫu nhiên một người đi xét nghiệm và có kết quả dương tính. Xác suất để người đó thực sự mắc bệnh bằng:",
                ["$0,5$", "$0,99$", "$0,9$", "$0,01$"],
                0,
                "Gọi $B$ là biến cố “Người đó mắc bệnh” $\\Rightarrow P(B) = 0,01$ và $P(\\overline{B}) = 0,99$. Gọi $A$ là biến cố “Xét nghiệm dương tính” $\\Rightarrow P(A|B) = 0,99$ và $P(A|\\overline{B}) = 0,01$. Theo công thức Bayes: $P(B|A) = \\dfrac{0,01 \\cdot 0,99}{0,01 \\cdot 0,99 + 0,99 \\cdot 0,01} = \\mathbf{0,5}$.",
            ),
            short(
                "vandung",
                "Có hai hộp đựng bi: hộp $I$ có $4$ bi đỏ và $6$ bi xanh; hộp $II$ có $7$ bi đỏ và $3$ bi xanh. Tung một đồng xu cân đối và đồng chất: nếu xuất hiện mặt sấp thì lấy ngẫu nhiên $1$ viên bi từ hộp $I$, nếu xuất hiện mặt ngửa thì lấy ngẫu nhiên $1$ viên bi từ hộp $II$. Biết rằng viên bi lấy ra có màu đỏ, xác suất để viên bi đó được lấy từ hộp $II$ bằng $\\dfrac{a}{b}$ (với $\\dfrac{a}{b}$ là phân số tối giản, $a, b \\in \\mathbb{N}^*$). Tính giá trị biểu thức $T = a + b$.",
                ["18"],
                "Gọi $B_1, B_2$ lần lượt là biến cố chọn hộp $I$, hộp $II$ $\\Rightarrow P(B_1) = P(B_2) = 0,5$. Gọi $A$ là biến cố “Lấy được bi đỏ” $\\Rightarrow P(A|B_1) = 0,4$ và $P(A|B_2) = 0,7$. Theo công thức Bayes: $P(B_2|A) = \\dfrac{0,5 \\cdot 0,7}{0,5 \\cdot 0,4 + 0,5 \\cdot 0,7} = \\dfrac{7}{11}$. Suy ra $a = 7, b = 11 \\Rightarrow T = a + b = \\mathbf{18}$.",
            ),
        ],
    },
]
