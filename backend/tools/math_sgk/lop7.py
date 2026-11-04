"""TOÁN 7 — Kết nối tri thức với cuộc sống (tập một, tập hai).

10 chương đánh số (I – X) đúng thứ tự mục lục SGK.
Mỗi chương: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 7

LESSONS = [
    {
        "topic": "l7-ch01-so-huu-ti",
        "title": "Số hữu tỉ",
        "icon": "➗",
        "description": "Tập hợp các số hữu tỉ Q, các phép tính cộng, trừ, nhân, chia, lũy thừa với số mũ tự nhiên, thứ tự thực hiện các phép tính và quy tắc chuyển vế (Bài 1 - Bài 4, SGK Toán 7 Tập 1).",
        "requirements": [
            "Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ; nhận biết được tập hợp các số hữu tỉ Q.",
            "Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.",
            "Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.",
            "Thực hiện được các phép tính: cộng, trừ, nhân, chia và lũy thừa với số mũ tự nhiên của một số hữu tỉ.",
            "Vận dụng được các tính chất giao hoán, kết hợp, phân phối của phép nhân đối với phép cộng, quy tắc dấu ngoặc và quy tắc chuyển vế trong tập hợp số hữu tỉ để tính nhẩm, tính hợp lí và tìm thành phần chưa biết.",
            "Giải quyết được một số vấn đề thực tiễn gắn với các phép tính về số hữu tỉ.",
        ],
        "definition": "Số hữu tỉ là số viết được dưới dạng phân số $\\frac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\neq 0$. Tập hợp các số hữu tỉ được kí hiệu là $\\mathbb{Q}$. Mọi số nguyên, số thập phân hữu hạn và hỗn số đều là số hữu tỉ.",
        "theory": (
            "### Bài 1. Tập hợp các số hữu tỉ (trang 5)\n"
            "- Số hữu tỉ viết dưới dạng $\\frac{a}{b}$ ($a, b \\in \\mathbb{Z}, b \\neq 0$). Trên trục số, hai điểm biểu diễn hai số hữu tỉ đối nhau ($x$ và $-x$) nằm về hai phía của gốc $O$ và cách đều gốc $O$. Với hai số hữu tỉ $a, b$ bất kì, luôn có $a = b$, $a < b$ hoặc $a > b$; nếu $a < b$ thì điểm $a$ nằm trước điểm $b$ trên trục số.\n"
            "### Bài 2. Cộng, trừ, nhân, chia số hữu tỉ (trang 10)\n"
            "- Mọi số hữu tỉ đều viết được dưới dạng phân số nên ta cộng, trừ, nhân, chia hai số hữu tỉ bằng cách viết chúng dưới dạng phân số rồi áp dụng quy tắc cộng, trừ, nhân, chia phân số. Phép cộng và phép nhân số hữu tỉ có đầy đủ các tính chất giao hoán, kết hợp, cộng với $0$, nhân với $1$ và tính chất phân phối của phép nhân đối với phép cộng.\n"
            "### Bài 3. Lũy thừa với số mũ tự nhiên của một số hữu tỉ (trang 16)\n"
            "- Lũy thừa bậc $n$ của số hữu tỉ $x$ (kí hiệu $x^n$, $n \\in \\mathbb{N}^*$) là tích của $n$ thừa số $x$. Quy ước $x^1 = x$ và $x^0 = 1$ ($x \\neq 0$). Khi nhân hoặc chia hai lũy thừa cùng cơ số, hoặc tính lũy thừa của lũy thừa, lũy thừa của một tích, một thương, ta áp dụng các công thức lũy thừa tương ứng.\n"
            "### Bài 4. Thứ tự thực hiện các phép tính. Quy tắc chuyển vế (trang 20)\n"
            "- Đối với biểu thức không có dấu ngoặc: Lũy thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ. Đối với biểu thức có dấu ngoặc: $() \\rightarrow [] \\rightarrow \\{\\}$. Quy tắc chuyển vế: Khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải đổi dấu số hạng đó."
        ),
        "formulas": [
            G("Định nghĩa & Số đối", F("Tập hợp số hữu tỉ", "$\\mathbb{Q} = \\left\\{ \\frac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$"), F("Tổng hai số đối nhau", "$x + (-x) = 0, \\quad -(-x) = x$")),
            G("Các phép tính cơ bản trên Q", F("Cộng, trừ hai số hữu tỉ", "$\\frac{a}{m} + \\frac{b}{m} = \\frac{a + b}{m}, \\quad \\frac{a}{m} - \\frac{b}{m} = \\frac{a - b}{m} \\quad (m > 0)$"), F("Nhân hai số hữu tỉ", "$\\frac{a}{b} \\cdot \\frac{c}{d} = \\frac{a \\cdot c}{b \\cdot d} \\quad (b, d \\neq 0)$"), F("Chia hai số hữu tỉ", "$\\frac{a}{b} : \\frac{c}{d} = \\frac{a}{b} \\cdot \\frac{d}{c} = \\frac{a \\cdot d}{b \\cdot c} \\quad (b, c, d \\neq 0)$")),
            G("Lũy thừa & Quy tắc chuyển vế", F("Lũy thừa của một thương", "$\\left(\\frac{a}{b}\\right)^n = \\frac{a^n}{b^n} \\quad (b \\neq 0, n \\in \\mathbb{N})$"), F("Nhân, chia hai lũy thừa cùng cơ số", "$x^m \\cdot x^n = x^{m+n}, \\quad x^m : x^n = x^{m-n} \\quad (x \\neq 0, m \\ge n)$"), F("Lũy thừa của lũy thừa và của một tích", "$(x^m)^n = x^{m \\cdot n}, \\quad (x \\cdot y)^n = x^n \\cdot y^n$"), F("Quy tắc chuyển vế", "$x + y = z \\Rightarrow x = z - y; \\quad x - y = z \\Rightarrow x = z + y$")),
        ],
        "example": (
            "Thực hiện phép tính một cách hợp lí và tìm $x$:\n"
            "a) Tính giá trị biểu thức $A = \\frac{-3}{7} \\cdot \\frac{5}{9} + \\frac{-3}{7} \\cdot \\frac{4}{9} + \\left(-\\frac{1}{2}\\right)^2$.\n"
            "b) Tìm $x$ biết: $x - \\frac{2}{5} = \\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4}$."
        ),
        "example_answer": (
            "a) Áp dụng tính chất phân phối của phép nhân đối với phép cộng và tính lũy thừa:\n"
            "$A = \\frac{-3}{7} \\cdot \\left(\\frac{5}{9} + \\frac{4}{9}\\right) + \\frac{1}{4} = \\frac{-3}{7} \\cdot 1 + \\frac{1}{4} = \\frac{-12 + 7}{28} = -\\frac{5}{28}$.\n"
            "b) Thu gọn vế phải trước:\n"
            "$\\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4} = -\\frac{1}{8} \\cdot 4 = -\\frac{1}{2}$.\n"
            "Áp dụng quy tắc chuyển vế:\n"
            "$x - \\frac{2}{5} = -\\frac{1}{2} \\Rightarrow x = -\\frac{1}{2} + \\frac{2}{5} = \\frac{-5 + 4}{10} = -\\frac{1}{10}$."
        ),
        "real_life": "Số hữu tỉ xuất hiện thường xuyên trong việc đo độ cao so với mực nước biển (ví dụ rãnh Mariana sâu $-10,994\\text{ km}$), tính toán lãi suất ngân hàng, định lượng nguyên liệu nấu ăn theo tỉ lệ phân số và quy đổi múi giờ quốc tế.",
        "quiz": [
            mcq("biet", "Tập hợp các số hữu tỉ được kí hiệu là gì?", ["$\\mathbb{Q}$", "$\\mathbb{N}$", "$\\mathbb{Z}$", "$\\mathbb{R}$"], 0, "Tập hợp các số hữu tỉ được kí hiệu là $\\mathbb{Q}$."),
            mcq("biet", "Số đối của số hữu tỉ $-\\frac{5}{8}$ là số nào dưới đây?", ["$\\frac{5}{8}$", "$\\frac{8}{5}$", "$-\\frac{8}{5}$", "$-0,625$"], 0, "Số đối của số hữu tỉ $x$ là $-x$, nên số đối của $-\\frac{5}{8}$ là $-\\left(-\\frac{5}{8}\\right) = \\frac{5}{8}$."),
            mcq("biet", "Với mọi số hữu tỉ $x \\neq 0$, giá trị của $x^0$ bằng bao nhiêu?", ["$1$", "$0$", "$x$", "$-1$"], 0, "Theo quy ước, với mọi số hữu tỉ $x \\neq 0$, ta luôn có $x^0 = 1$."),
            mcq("biet", "Cho đẳng thức $x - \\frac{3}{4} = \\frac{1}{2}$. Khi áp dụng quy tắc chuyển vế, ta thu được kết quả nào?", ["$x = \\frac{1}{2} + \\frac{3}{4}$", "$x = \\frac{1}{2} - \\frac{3}{4}$", "$x = -\\frac{1}{2} + \\frac{3}{4}$", "$x = -\\frac{1}{2} - \\frac{3}{4}$"], 0, "Khi chuyển số hạng $-\\frac{3}{4}$ từ vế trái sang vế phải, ta đổi dấu thành $+\\frac{3}{4}$, được $x = \\frac{1}{2} + \\frac{3}{4}$."),
            mcq("hieu", "Giá trị của biểu thức $\\left(-\\frac{2}{3}\\right)^3$ bằng bao nhiêu?", ["$-\\frac{8}{27}$", "$\\frac{8}{27}$", "$-\\frac{6}{9}$", "$\\frac{6}{27}$"], 0, "Ta có $\\left(-\\frac{2}{3}\\right)^3 = \\frac{(-2)^3}{3^3} = \\frac{-8}{27} = -\\frac{8}{27}$."),
            mcq("hieu", "Kết quả của phép tính $\\frac{3}{5} + \\frac{2}{5} \\cdot \\left(-\\frac{10}{4}\\right)$ là:", ["$-\\frac{2}{5}$", "$-\\frac{5}{2}$", "$\\frac{2}{5}$", "$-1$"], 0, "Thực hiện phép nhân trước: $\\frac{2}{5} \\cdot \\left(-\\frac{10}{4}\\right) = \\frac{-20}{20} = -1$. Sau đó cộng: $\\frac{3}{5} + (-1) = -\\frac{2}{5}$."),
            tf4("hieu", "Xét tính đúng sai của các khẳng định sau về tập hợp số hữu tỉ $\\mathbb{Q}$:", ["a) Mọi số nguyên đều là số hữu tỉ, tức là $\\mathbb{Z} \\subset \\mathbb{Q}$.", "b) Số $0$ là số hữu tỉ dương nhỏ nhất.", "c) Trên trục số, điểm biểu diễn số hữu tỉ $-1,25$ nằm bên trái điểm biểu diễn số hữu tỉ $-0,75$.", "d) Số hữu tỉ $-1\\frac{2}{3}$ viết dưới dạng phân số tối giản là $-\\frac{5}{3}$."], [True, False, True, True], "a) Đúng vì mọi số nguyên $a \\in \\mathbb{Z}$ đều viết được dưới dạng $\\frac{a}{1} \\in \\mathbb{Q}$.\nb) Sai vì số $0$ không là số hữu tỉ dương cũng không là số hữu tỉ âm.\nc) Đúng vì $-1,25 < -0,75$ nên điểm $-1,25$ nằm trước (bên trái) điểm $-0,75$ trên trục số nằm ngang.\nd) Đúng vì $-1\\frac{2}{3} = -\\left(1 + \\frac{2}{3}\\right) = -\\frac{5}{3}$."),
            tf4("hieu", "Cho hai biểu thức $M = \\left(\\frac{1}{2}\\right)^3 \\cdot \\left(\\frac{1}{2}\\right)^2$ và $N = \\left[\\left(-\\frac{1}{2}\\right)^2\\right]^3$. Xét các khẳng định sau:", ["a) Giá trị của biểu thức $M$ viết dưới dạng lũy thừa cơ số $\\frac{1}{2}$ là $\\left(\\frac{1}{2}\\right)^5$.", "b) Giá trị của biểu thức $M$ bằng $\\frac{1}{64}$.", "c) Giá trị của biểu thức $N$ bằng $\\frac{1}{64}$.", "d) Thương $M : N$ bằng $2$."], [True, False, True, True], "a) Đúng vì $\\left(\\frac{1}{2}\\right)^3 \\cdot \\left(\\frac{1}{2}\\right)^2 = \\left(\\frac{1}{2}\\right)^{3+2} = \\left(\\frac{1}{2}\\right)^5$.\nb) Sai vì $M = \\left(\\frac{1}{2}\\right)^5 = \\frac{1}{32} \\neq \\frac{1}{64}$.\nc) Đúng vì $N = \\left(-\\frac{1}{2}\\right)^{2 \\cdot 3} = \\left(-\\frac{1}{2}\\right)^6 = \\frac{1}{64}$.\nd) Đúng vì $M : N = \\frac{1}{32} : \\frac{1}{64} = \\frac{64}{32} = 2$."),
            mcq("vandung", "Một kho lạnh ban đầu ở nhiệt độ $3,5^\\circ\\text{C}$. Cứ mỗi phút hệ thống làm lạnh giảm được $0,8^\\circ\\text{C}$. Hỏi sau $12$ phút hoạt động liên tục, nhiệt độ trong kho lạnh là bao nhiêu độ C?", ["$-6,1^\\circ\\text{C}$", "$-5,9^\\circ\\text{C}$", "$-9,6^\\circ\\text{C}$", "$6,1^\\circ\\text{C}$"], 0, "Sau $12$ phút, nhiệt độ giảm đi $12 \\cdot 0,8 = 9,6^\\circ\\text{C}$. Nhiệt độ kho lạnh khi đó là $3,5 - 9,6 = -6,1^\\circ\\text{C}$."),
            short("vandung", "Tìm số hữu tỉ $x$ thỏa mãn $\\frac{3}{4} + \\frac{1}{4} : x = 2$ (viết kết quả dưới dạng số thập phân).", ["0,2", "0.2"], "Từ $\\frac{3}{4} + \\frac{1}{4} : x = 2 \\Rightarrow \\frac{1}{4} : x = 2 - \\frac{3}{4} = \\frac{5}{4} \\Rightarrow x = \\frac{1}{4} : \\frac{5}{4} = \\frac{1}{5} = 0,2$."),
        ],
    },
    {
        "topic": "l7-ch02-so-thuc",
        "title": "Số thực",
        "icon": "√",
        "description": "Số thập phân vô hạn tuần hoàn, làm tròn số, số vô tỉ, căn bậc hai số học, tập hợp các số thực R và giá trị tuyệt đối của một số thực (Bài 5 - Bài 7, SGK Toán 7 Tập 1).",
        "requirements": [
            "Nhận biết được số thập phân hữu hạn và số thập phân vô hạn tuần hoàn.",
            "Thực hiện được việc làm tròn số thập phân căn cứ vào độ chính xác cho trước.",
            "Nhận biết được số vô tỉ và lấy được ví dụ về số vô tỉ (như $\\sqrt{2}, \\sqrt{3}, \\pi$).",
            "Nhận biết được khái niệm căn bậc hai số học của một số không âm và tính được căn bậc hai số học bằng định nghĩa hoặc máy tính cầm tay.",
            "Nhận biết được số thực, tập hợp các số thực R, trục số thực, số đối và thứ tự trong tập hợp các số thực.",
            "Nhận biết được giá trị tuyệt đối của một số thực và tính được giá trị tuyệt đối của một số thực.",
        ],
        "definition": "Số hữu tỉ và số vô tỉ được gọi chung là số thực. Tập hợp các số thực được kí hiệu là $\\mathbb{R}$. Mỗi số thực được biểu diễn bởi một điểm trên trục số và ngược lại, mỗi điểm trên trục số đều biểu diễn một số thực (trục số thực).",
        "theory": (
            "### Bài 5. Làm quen với số thập phân vô hạn tuần hoàn (trang 27)\n"
            "- Mọi số hữu tỉ đều viết được dưới dạng số thập phân hữu hạn (khi phân số tối giản có mẫu dương không có ước nguyên tố khác $2$ và $5$) hoặc vô hạn tuần hoàn (kí hiệu chu kì trong ngoặc đơn, ví dụ $0,333... = 0,(3)$). Khi làm tròn số với độ chính xác $d$: nếu $d = 0,05$ ta làm tròn đến hàng phần mười; nếu $d = 0,005$ ta làm tròn đến hàng phần trăm; nếu $d = 50$ ta làm tròn đến hàng trăm.\n"
            "### Bài 6. Số vô tỉ. Căn bậc hai số học (trang 30)\n"
            "- Số vô tỉ là số viết được dưới dạng số thập phân vô hạn không tuần hoàn, tập hợp số vô tỉ kí hiệu là $\\mathbb{I}$. Căn bậc hai số học của một số $a$ không âm ($a \\ge 0$), kí hiệu là $\\sqrt{a}$, là số không âm $x$ sao cho $x^2 = a$.\n"
            "### Bài 7. Tập hợp các số thực (trang 33)\n"
            "- Tập số thực $\\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$. Với hai số thực $a, b \\ge 0$, ta có $a < b \\Leftrightarrow \\sqrt{a} < \\sqrt{b}$. Khoảng cách từ điểm $a$ trên trục số đến gốc $O$ là giá trị tuyệt đối của số $a$, kí hiệu $|a|$. Giá trị tuyệt đối luôn không âm ($|a| \\ge 0$) và $|a| = |-a|$."
        ),
        "formulas": [
            G("Căn bậc hai số học", F("Định nghĩa căn bậc hai số học", "$\\sqrt{a} = x \\iff \\begin{cases} x \\ge 0 \\\\ x^2 = a \\end{cases} \\quad (a \\ge 0)$"), F("Bình phương của căn bậc hai số học", "$(\\sqrt{a})^2 = a \\quad (a \\ge 0), \\quad \\sqrt{x^2} = |x|$"), F("So sánh hai căn bậc hai số học", "$0 \\le a < b \\iff \\sqrt{a} < \\sqrt{b}$")),
            G("Tập hợp số thực & Giá trị tuyệt đối", F("Quan hệ bao hàm giữa các tập hợp số", "$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}, \\quad \\mathbb{I} \\subset \\mathbb{R}, \\quad \\mathbb{Q} \\cap \\mathbb{I} = \\varnothing$"), F("Định nghĩa giá trị tuyệt đối", "$|x| = \\begin{cases} x & \\text{nếu } x \\ge 0 \\\\ -x & \\text{nếu } x < 0 \\end{cases}$"), F("Tính chất của giá trị tuyệt đối", "$|x| \\ge 0 \\; (\\forall x \\in \\mathbb{R}); \\quad |-x| = |x|$")),
        ],
        "example": (
            "a) Tính giá trị của biểu thức $P = \\sqrt{81} - 3 \\cdot \\sqrt{\\frac{4}{9}} + |-2,5|$.\n"
            "b) Tìm tất cả các số thực $x$ thỏa mãn $|x - 1,5| = 3,5$."
        ),
        "example_answer": (
            "a) Ta có $\\sqrt{81} = 9$; $\\sqrt{\\frac{4}{9}} = \\frac{2}{3}$ và $|-2,5| = 2,5$.\n"
            "Do đó $P = 9 - 3 \\cdot \\frac{2}{3} + 2,5 = 9 - 2 + 2,5 = 9,5$.\n"
            "b) Từ $|x - 1,5| = 3,5$, suy ra hai trường hợp:\n"
            "- Trường hợp 1: $x - 1,5 = 3,5 \\Rightarrow x = 3,5 + 1,5 = 5$.\n"
            "- Trường hợp 2: $x - 1,5 = -3,5 \\Rightarrow x = -3,5 + 1,5 = -2$.\n"
            "Vậy $x \\in \\{-2; 5\\}$."
        ),
        "real_life": "Căn bậc hai và số thực được ứng dụng để tính độ dài đường chéo màn hình tivi (theo inch), tính cạnh của mảnh đất hình vuông khi biết diện tích, và làm tròn số liệu dân số hoặc diện tích địa lí theo độ chính xác cho trước.",
        "quiz": [
            mcq("biet", "Phân số $\\frac{5}{11}$ viết dưới dạng số thập phân vô hạn tuần hoàn là:", ["$0,(45)$", "$0,4(5)$", "$0,(54)$", "$0,45$"], 0, "Thực hiện phép chia $5 : 11 = 0,454545... = 0,(45)$ với chu kì là $45$."),
            mcq("biet", "Căn bậc hai số học của $49$ là số nào?", ["$7$", "$-7$", "$7$ và $-7$", "$2401$"], 0, "Vì $7 > 0$ và $7^2 = 49$ nên căn bậc hai số học của $49$ là $\\sqrt{49} = 7$."),
            mcq("biet", "Trong các số sau đây, số nào là số vô tỉ?", ["$\\sqrt{5}$", "$\\sqrt{16}$", "$-\\frac{3}{7}$", "$0,(12)$"], 0, "Ta có $\\sqrt{16} = 4 \\in \\mathbb{Q}$, $-\\frac{3}{7} \\in \\mathbb{Q}$, $0,(12) \\in \\mathbb{Q}$. Chỉ có $\\sqrt{5} = 2,2360679...$ là số thập phân vô hạn không tuần hoàn nên là số vô tỉ."),
            mcq("biet", "Giá trị tuyệt đối của số thực $-\\sqrt{7}$, tức là $|-\\sqrt{7}|$, bằng:", ["$\\sqrt{7}$", "$-\\sqrt{7}$", "$7$", "$-7$"], 0, "Vì $-\\sqrt{7} < 0$ nên $|-\\sqrt{7}| = -(-\\sqrt{7}) = \\sqrt{7}$."),
            mcq("hieu", "Làm tròn số $314,5682$ với độ chính xác $d = 0,005$ (tức là làm tròn đến hàng phần trăm) ta được kết quả là:", ["$314,57$", "$314,56$", "$314,6$", "$314,568$"], 0, "Độ chính xác $d = 0,005$ tương ứng với việc làm tròn đến hàng phần trăm. Chữ số hàng phần nghìn là $8 \\ge 5$ nên $314,5682 \\approx 314,57$."),
            mcq("hieu", "So sánh hai số thực $a = 4$ và $b = \\sqrt{15}$, khẳng định nào sau đây đúng?", ["$a > b$", "$a < b$", "$a = b$", "$a \\le b$"], 0, "Ta có $a = 4 = \\sqrt{16}$. Vì $16 > 15 > 0$ nên $\\sqrt{16} > \\sqrt{15}$, hay $a > b$."),
            tf4("hieu", "Xét tính đúng sai của các khẳng định sau về số thực và căn bậc hai số học:", ["a) Ta luôn có $\\sqrt{25} = 5$ và $-\\sqrt{25} = -5$.", "b) Căn bậc hai số học của $(-6)^2$ bằng $-6$.", "c) Mọi số hữu tỉ đều là số thực, tức là $\\mathbb{Q} \\subset \\mathbb{R}$.", "d) Tồn tại số thực $x$ vừa là số hữu tỉ vừa là số vô tỉ."], [True, False, True, False], "a) Đúng theo định nghĩa căn bậc hai số học của $25$.\nb) Sai vì $(-6)^2 = 36$ và căn bậc hai số học của $36$ luôn không âm nên $\\sqrt{(-6)^2} = \\sqrt{36} = 6 \\neq -6$.\nc) Đúng vì tập số thực $\\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$ chứa toàn bộ tập số hữu tỉ $\\mathbb{Q}$.\nd) Sai vì mỗi số thực hoặc là số hữu tỉ hoặc là số vô tỉ ($\\mathbb{Q} \\cap \\mathbb{I} = \\varnothing$)."),
            tf4("hieu", "Cho biểu thức $A = |x - 2| + \\sqrt{16}$. Xét tính đúng sai của các khẳng định sau:", ["a) Khi $x = -1$ thì giá trị của biểu thức $A$ bằng $7$.", "b) Với mọi số thực $x$, ta luôn có $|x - 2| \\ge 0$.", "c) Giá trị nhỏ nhất của biểu thức $A$ trên tập số thực $\\mathbb{R}$ bằng $4$.", "d) Có đúng hai giá trị thực của $x$ để $A = 3$."], [True, True, True, False], "a) Đúng vì khi $x = -1$, $A = |-1 - 2| + 4 = |-3| + 4 = 3 + 4 = 7$.\nb) Đúng theo tính chất giá trị tuyệt đối của mọi số thực luôn không âm.\nc) Đúng vì $|x - 2| \\ge 0 \\Rightarrow A = |x - 2| + 4 \\ge 4$; dấu bằng xảy ra khi $x = 2$.\nd) Sai vì $A \\ge 4$ với mọi $x \\in \\mathbb{R}$ nên không có giá trị nào của $x$ để $A = 3$."),
            mcq("vandung", "Một căn phòng hình vuông có diện tích $20,25\\text{ m}^2$. Người ta muốn lát nền căn phòng bằng các viên gạch hình vuông có cạnh $0,5\\text{ m}$ (không kể mạch vữa). Hỏi cần bao nhiêu viên gạch và độ dài cạnh căn phòng là bao nhiêu mét?", ["Cạnh phòng $4,5\\text{ m}$ và cần $81$ viên gạch", "Cạnh phòng $4,5\\text{ m}$ và cần $90$ viên gạch", "Cạnh phòng $5,5\\text{ m}$ và cần $81$ viên gạch", "Cạnh phòng $4,25\\text{ m}$ và cần $85$ viên gạch"], 0, "Độ dài cạnh căn phòng là $\\sqrt{20,25} = 4,5\\text{ (m)}$. Diện tích mỗi viên gạch là $0,5^2 = 0,25\\text{ (m}^2\\text{)}$. Số viên gạch cần dùng là $20,25 : 0,25 = 81$ (viên)."),
            short("vandung", "Tính giá trị của biểu thức $T = \\sqrt{144} + 5 \\cdot \\sqrt{0,36} - |-4,5|$.", ["10,5", "10.5"], "Ta có $\\sqrt{144} = 12$; $\\sqrt{0,36} = 0,6$ và $|-4,5| = 4,5$. Do đó $T = 12 + 5 \\cdot 0,6 - 4,5 = 12 + 3 - 4,5 = 10,5$."),
        ],
    },
    {
        "topic": "l7-ch03-goc-va-duong-thang-song-song",
        "title": "Góc và đường thẳng song song",
        "icon": "📐",
        "description": "Hai góc kề bù, hai góc đối đỉnh, tia phân giác của một góc, dấu hiệu nhận biết và tính chất của hai đường thẳng song song, tiên đề Euclid, định lí và chứng minh định lí (Bài 8 - Bài 11, SGK Toán 7 Tập 1).",
        "requirements": [
            "Nhận biết được các góc ở vị trí đặc biệt (hai góc kề bù, hai góc đối đỉnh) và tính chất của chúng.",
            "Nhận biết được tia phân giác của một góc và tính chất chia đôi góc của tia phân giác.",
            "Nhận biết được các cặp góc so le trong, đồng vị tạo bởi một đường thẳng cắt hai đường thẳng.",
            "Mô tả được dấu hiệu song song của hai đường thẳng thông qua cặp góc đồng vị, cặp góc so le trong.",
            "Nhận biết được tiên đề Euclid về đường thẳng song song và mô tả được các tính chất của hai đường thẳng song song.",
            "Nhận biết được thế nào là một định lí, phân biệt được phần giả thiết và kết luận của định lí, bước đầu biết chứng minh một định lí.",
        ],
        "definition": "Hai góc đối đỉnh thì bằng nhau; hai góc kề bù có tổng số đo bằng $180^\\circ$. Khi một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong bằng nhau, hai góc đồng vị bằng nhau. Tiên đề Euclid: Qua một điểm ở ngoài một đường thẳng, chỉ có một đường thẳng song song với đường thẳng đó.",
        "theory": (
            "### Bài 8. Góc ở vị trí đặc biệt. Tia phân giác của một góc (trang 40)\n"
            "- Hai góc có một cạnh chung, hai cạnh còn lại là hai tia đối nhau được gọi là hai góc kề bù; hai góc kề bù có tổng số đo bằng $180^\\circ$. Hai góc đối đỉnh là hai góc mà mỗi cạnh của góc này là tia đối của một cạnh của góc kia; hai góc đối đỉnh thì bằng nhau. Tia nằm giữa hai cạnh của một góc và tạo với hai cạnh ấy hai góc bằng nhau được gọi là tia phân giác của góc đó.\n"
            "### Bài 9. Hai đường thẳng song song và dấu hiệu nhận biết (trang 46)\n"
            "- Nếu đường thẳng $c$ cắt hai đường thẳng phân biệt $a, b$ và trong các góc tạo thành có một cặp góc so le trong bằng nhau (hoặc một cặp góc đồng vị bằng nhau) thì $a$ và $b$ song song với nhau ($a \\parallel b$). Hệ quả: Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau.\n"
            "### Bài 10. Tiên đề Euclid. Tính chất của hai đường thẳng song song (trang 51)\n"
            "- Tiên đề Euclid khẳng định qua một điểm nằm ngoài một đường thẳng chỉ kẻ được duy nhất một đường thẳng song song với đường thẳng đó. Tính chất: Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong bằng nhau, hai góc đồng vị bằng nhau. Hệ quả: Một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với đường thẳng kia; hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì song song với nhau.\n"
            "### Bài 11. Định lí và chứng minh định lí (trang 55)\n"
            "- Định lí là một khẳng định được suy ra từ những khẳng định đúng đã biết. Mỗi định lí thường được phát biểu dưới dạng \"Nếu ... thì ...\", phần giữa từ \"Nếu\" và từ \"thì\" là giả thiết (GT), phần sau từ \"thì\" là kết luận (KL). Chứng minh định lí là dùng lập luận để từ giả thiết và những khẳng định đúng đã biết suy ra kết luận."
        ),
        "formulas": [
            G("Góc ở vị trí đặc biệt & Tia phân giác", F("Hai góc kề bù xOy và yOz", "$\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$"), F("Hai góc đối đỉnh", "$\\widehat{O_1} \\text{ và } \\widehat{O_3} \\text{ đối đỉnh} \\Rightarrow \\widehat{O_1} = \\widehat{O_3}$"), F("Tia phân giác Oz của góc xOy", "$\\widehat{xOz} = \\widehat{zOy} = \\frac{1}{2}\\widehat{xOy}$")),
            G("Hai đường thẳng song song & Quan hệ vuông góc", F("Dấu hiệu & Tính chất hai đường thẳng song song", "$a \\parallel b \\iff \\text{Góc so le trong bằng nhau (hoặc góc đồng vị bằng nhau)}$"), F("Hai góc trong cùng phía (khi a // b)", "$\\widehat{A_1} + \\widehat{B_2} = 180^\\circ$"), F("Quan hệ giữa tính vuông góc và tính song song", "$\\begin{cases} a \\perp c \\\\ b \\perp c \\end{cases} \\Rightarrow a \\parallel b; \\qquad \\begin{cases} a \\parallel b \\\\ c \\perp a \\end{cases} \\Rightarrow c \\perp b$")),
        ],
        "example": (
            "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$, biết $\\widehat{xOy} = 110^\\circ$.\n"
            "a) Tính số đo góc $\\widehat{yOz}$.\n"
            "b) Gọi $Ot$ là tia phân giác của góc $\\widehat{xOy}$ và $Om$ là tia phân giác của góc $\\widehat{yOz}$. Tính số đo góc $\\widehat{tOm}$."
        ),
        "example_answer": (
            "a) Vì $\\widehat{xOy}$ và $\\widehat{yOz}$ là hai góc kề bù nên $\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$.\n"
            "Suy ra $\\widehat{yOz} = 180^\\circ - 110^\\circ = 70^\\circ$.\n"
            "b) Vì $Ot$ là tia phân giác của $\\widehat{xOy}$ nên $\\widehat{tOy} = \\frac{1}{2}\\widehat{xOy} = \\frac{110^\\circ}{2} = 55^\\circ$.\n"
            "Vì $Om$ là tia phân giác của $\\widehat{yOz}$ nên $\\widehat{yOm} = \\frac{1}{2}\\widehat{yOz} = \\frac{70^\\circ}{2} = 35^\\circ$.\n"
            "Tia $Oy$ nằm giữa hai tia $Ot$ và $Om$ nên $\\widehat{tOm} = \\widehat{tOy} + \\widehat{yOm} = 55^\\circ + 35^\\circ = 90^\\circ$."
        ),
        "real_life": "Tính chất của hai đường thẳng song song và góc đồng vị, so le trong được các thợ mộc và kĩ sư xây dựng dùng để kiểm tra độ song song của các thanh xà, bậc cầu thang, chấn song cửa sổ hoặc kẻ vạch phân làn đường giao thông.",
        "quiz": [
            mcq("biet", "Cho hai góc $\\widehat{xOy}$ và $\\widehat{x'Oy'}$ là hai góc đối đỉnh. Biết $\\widehat{xOy} = 65^\\circ$, số đo góc $\\widehat{x'Oy'}$ là:", ["$65^\\circ$", "$115^\\circ$", "$25^\\circ$", "$130^\\circ$"], 0, "Hai góc đối đỉnh thì bằng nhau nên $\\widehat{x'Oy'} = \\widehat{xOy} = 65^\\circ$."),
            mcq("biet", "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$, trong đó $\\widehat{AOB} = 72^\\circ$. Số đo góc $\\widehat{BOC}$ bằng:", ["$108^\\circ$", "$72^\\circ$", "$18^\\circ$", "$118^\\circ$"], 0, "Hai góc kề bù có tổng số đo bằng $180^\\circ$, suy ra $\\widehat{BOC} = 180^\\circ - 72^\\circ = 108^\\circ$."),
            mcq("biet", "Theo Tiên đề Euclid, qua một điểm $M$ nằm ngoài đường thẳng $a$, có bao nhiêu đường thẳng đi qua $M$ và song song với đường thẳng $a$?", ["Chỉ có một", "Có hai", "Có vô số", "Không có đường thẳng nào"], 0, "Tiên đề Euclid khẳng định: Qua một điểm ở ngoài một đường thẳng, chỉ có một đường thẳng song song với đường thẳng đó."),
            mcq("biet", "Cho góc $\\widehat{xOy} = 128^\\circ$, tia $Oz$ là tia phân giác của góc $\\widehat{xOy}$. Số đo góc $\\widehat{xOz}$ bằng:", ["$64^\\circ$", "$128^\\circ$", "$52^\\circ$", "$32^\\circ$"], 0, "Vì $Oz$ là tia phân giác của $\\widehat{xOy}$ nên $\\widehat{xOz} = \\frac{1}{2}\\widehat{xOy} = \\frac{128^\\circ}{2} = 64^\\circ$."),
            mcq("hieu", "Đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$ lần lượt tại $A$ và $B$. Biết một góc tạo thành tại đỉnh $A$ là $\\widehat{A_1} = 55^\\circ$, số đo góc so le trong với $\\widehat{A_1}$ tại đỉnh $B$ và góc kề bù với góc đó lần lượt là:", ["$55^\\circ$ và $125^\\circ$", "$125^\\circ$ và $55^\\circ$", "$55^\\circ$ và $35^\\circ$", "$135^\\circ$ và $55^\\circ$"], 0, "Do $a \\parallel b$ nên góc so le trong với $\\widehat{A_1}$ bằng $\\widehat{A_1} = 55^\\circ$; góc kề bù với nó có số đo $180^\\circ - 55^\\circ = 125^\\circ$."),
            mcq("hieu", "Trong định lí: \"Nếu hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau\", phần kết luận (KL) là gì?", ["Chúng song song với nhau", "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba", "Hai đường thẳng phân biệt cắt nhau", "Hai đường thẳng trùng nhau"], 0, "Phần đứng sau từ \"thì\" là phần kết luận của định lí: \"chúng song song với nhau\"."),
            tf4("hieu", "Cho hai đường thẳng song song $a, b$ và đường thẳng $c$ cắt cả $a$ và $b$. Xét tính đúng sai của các khẳng định sau:", ["a) Hai góc so le trong tạo thành luôn bằng nhau.", "b) Hai góc đồng vị tạo thành luôn bằng nhau.", "c) Nếu đường thẳng $c$ vuông góc với đường thẳng $a$ thì $c$ cũng vuông góc với đường thẳng $b$.", "d) Hai góc đối đỉnh bất kì luôn có tổng số đo bằng $180^\\circ$."], [True, True, True, False], "a), b), c) Đúng theo tính chất của hai đường thẳng song song.\nd) Sai vì hai góc đối đỉnh thì bằng nhau, tổng của chúng chỉ bằng $180^\\circ$ khi mỗi góc bằng $90^\\circ$."),
            tf4("hieu", "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$ với $\\widehat{xOy} = 4 \\cdot \\widehat{yOz}$. Gọi $Ot$ là tia phân giác của $\\widehat{xOy}$. Xét các khẳng định sau:", ["a) Tổng số đo $\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$.", "b) Số đo góc $\\widehat{yOz}$ bằng $36^\\circ$.", "c) Số đo góc $\\widehat{xOy}$ bằng $144^\\circ$.", "d) Số đo góc $\\widehat{tOz}$ bằng $100^\\circ$."], [True, True, True, False], "a) Đúng vì hai góc kề bù có tổng bằng $180^\\circ$.\nb), c) Đúng vì $4\\widehat{yOz} + \\widehat{yOz} = 180^\\circ \\Rightarrow 5\\widehat{yOz} = 180^\\circ \\Rightarrow \\widehat{yOz} = 36^\\circ$ và $\\widehat{xOy} = 144^\\circ$.\nd) Sai vì $\\widehat{tOy} = \\frac{144^\\circ}{2} = 72^\\circ \\Rightarrow \\widehat{tOz} = \\widehat{tOy} + \\widehat{yOz} = 72^\\circ + 36^\\circ = 108^\\circ \\neq 100^\\circ$."),
            mcq("vandung", "Cho hình vẽ có hai tia $Ax \\parallel Cy$ và điểm $B$ nằm trong khoảng giữa hai đường thẳng chứa $Ax, Cy$ sao cho $\\widehat{xAB} = 40^\\circ$, $\\widehat{BCy} = 55^\\circ$ (hai tia $Ax, Cy$ cùng nằm về một phía so với đường gấp khúc $ABC$). Số đo góc $\\widehat{ABC}$ bằng:", ["$95^\\circ$", "$85^\\circ$", "$15^\\circ$", "$105^\\circ$"], 0, "Qua $B$ kẻ tia $Bz \\parallel Ax$ (cùng chiều với $Ax, Cy$). Do $Ax \\parallel Cy$ nên $Bz \\parallel Cy$. Theo tính chất góc so le trong, $\\widehat{ABz} = \\widehat{xAB} = 40^\\circ$ và $\\widehat{zBC} = \\widehat{BCy} = 55^\\circ$. Vậy $\\widehat{ABC} = 40^\\circ + 55^\\circ = 95^\\circ$."),
            short("vandung", "Cho hai đường thẳng $xx'$ và $yy'$ cắt nhau tại $O$. Biết $\\widehat{xOy} + \\widehat{x'Oy'} = 150^\\circ$. Tính số đo góc $\\widehat{xOy'}$ (đơn vị: độ).", ["105"], "Vì $\\widehat{xOy}$ và $\\widehat{x'Oy'}$ là hai góc đối đỉnh nên $\\widehat{xOy} = \\widehat{x'Oy'} = \\frac{150^\\circ}{2} = 75^\\circ$. Góc $\\widehat{xOy'}$ kề bù với $\\widehat{xOy}$ nên $\\widehat{xOy'} = 180^\\circ - 75^\\circ = 105^\\circ$."),
        ],
    },
    {
        "topic": "l7-ch04-tam-giac-bang-nhau",
        "title": "Tam giác bằng nhau",
        "icon": "🔺",
        "description": "Tổng ba góc trong một tam giác, góc ngoài của tam giác, các trường hợp bằng nhau của tam giác thường và tam giác vuông, tam giác cân, tam giác đều và đường trung trực của đoạn thẳng (Bài 12 - Bài 16, SGK Toán 7 Tập 1).",
        "requirements": [
            "Giải thích được định lí về tổng các góc trong một tam giác bằng 180 độ và tính chất góc ngoài của tam giác.",
            "Nhận biết được hai tam giác bằng nhau và kí hiệu sự bằng nhau của hai tam giác theo đúng thứ tự đỉnh tương ứng.",
            "Giải thích được các trường hợp bằng nhau của hai tam giác: cạnh - cạnh - cạnh (c.c.c), cạnh - góc - cạnh (c.g.c), góc - cạnh - góc (g.c.g).",
            "Giải thích được các trường hợp bằng nhau của hai tam giác vuông, bao gồm trường hợp cạnh huyền - góc nhọn và cạnh huyền - cạnh góc vuông.",
            "Mô tả được tam giác cân, tam giác đều cùng các tính chất và dấu hiệu nhận biết của chúng.",
            "Nhận biết được đường trung trực của một đoạn thẳng và tính chất cơ bản của đường trung trực.",
            "Lập luận và chứng minh được các đoạn thẳng bằng nhau, các góc bằng nhau từ các điều kiện ban đầu liên quan đến tam giác.",
        ],
        "definition": "Tổng ba góc trong một tam giác bằng $180^\\circ$. Hai tam giác bằng nhau là hai tam giác có các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau. Đường trung trực của một đoạn thẳng là đường thẳng vuông góc với đoạn thẳng đó tại trung điểm của nó.",
        "theory": (
            "### Bài 12. Tổng các góc trong một tam giác (trang 60)\n"
            "- Tổng ba góc trong một tam giác bằng $180^\\circ$. Trong tam giác vuông, hai góc nhọn phụ nhau (tổng bằng $90^\\circ$). Góc ngoài của tam giác là góc kề bù với một góc trong của tam giác; mỗi góc ngoài của tam giác bằng tổng hai góc trong không kề với nó.\n"
            "### Bài 13. Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất của tam giác (trang 63)\n"
            "- $\\triangle ABC = \\triangle A'B'C'$ khi các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau. Trường hợp cạnh - cạnh - cạnh (c.c.c): Nếu ba cạnh của tam giác này bằng ba cạnh của tam giác kia thì hai tam giác đó bằng nhau.\n"
            "### Bài 14. Trường hợp bằng nhau thứ hai và thứ ba của tam giác (trang 69)\n"
            "- Trường hợp cạnh - góc - cạnh (c.g.c): Nếu hai cạnh và góc xen giữa của tam giác này bằng hai cạnh và góc xen giữa của tam giác kia thì hai tam giác đó bằng nhau. Trường hợp góc - cạnh - góc (g.c.g): Nếu một cạnh và hai góc kề của tam giác này bằng một cạnh và hai góc kề của tam giác kia thì hai tam giác đó bằng nhau.\n"
            "### Bài 15. Các trường hợp bằng nhau của tam giác vuông (trang 75)\n"
            "- Ngoài hai trường hợp hai cạnh góc vuông (c.g.c) và một cạnh góc vuông - góc nhọn kề (g.c.g), hai tam giác vuông còn bằng nhau trong trường hợp cạnh huyền - góc nhọn (cạnh huyền và một góc nhọn bằng nhau) và trường hợp cạnh huyền - cạnh góc vuông (cạnh huyền và một cạnh góc vuông bằng nhau).\n"
            "### Bài 16. Tam giác cân. Đường trung trực của đoạn thẳng (trang 79)\n"
            "- Tam giác cân là tam giác có hai cạnh bằng nhau; trong một tam giác cân, hai góc ở đáy bằng nhau và ngược lại. Tam giác đều có ba cạnh bằng nhau và ba góc đều bằng $60^\\circ$. Điểm nằm trên đường trung trực của một đoạn thẳng thì cách đều hai mút của đoạn thẳng đó và ngược lại."
        ),
        "formulas": [
            G("Tổng các góc & Góc ngoài của tam giác", F("Tổng ba góc trong tam giác ABC", "$\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$"), F("Hai góc nhọn trong tam giác vuông (vuông tại A)", "$\\widehat{B} + \\widehat{C} = 90^\\circ$"), F("Góc ngoài tại đỉnh C của tam giác ABC", "$\\widehat{ACx} = \\widehat{A} + \\widehat{B}$")),
            G("Các trường hợp bằng nhau của tam giác", F("Ba trường hợp bằng nhau của tam giác thường", "$\\text{(c.c.c)}, \\quad \\text{(c.g.c)}, \\quad \\text{(g.c.g)}$"), F("Hai trường hợp đặc biệt của tam giác vuông", "$\\text{Cạnh huyền - góc nhọn}, \\quad \\text{Cạnh huyền - cạnh góc vuông}$")),
            G("Tam giác cân, Tam giác đều & Đường trung trực", F("Tam giác ABC cân tại A", "$AB = AC \\iff \\widehat{B} = \\widehat{C} = \\frac{180^\\circ - \\widehat{A}}{2}$"), F("Tam giác ABC đều", "$AB = BC = CA \\iff \\widehat{A} = \\widehat{B} = \\widehat{C} = 60^\\circ$"), F("Tính chất đường trung trực d của đoạn AB", "$M \\in d \\iff MA = MB$")),
        ],
        "example": (
            "Cho tam giác $ABC$ cân tại $A$ có $\\widehat{A} = 50^\\circ$. Gọi $M$ là trung điểm của cạnh đáy $BC$.\n"
            "a) Tính số đo các góc $\\widehat{B}$ và $\\widehat{C}$ của tam giác $ABC$.\n"
            "b) Chứng minh $\\triangle ABM = \\triangle ACM$ và $AM \\perp BC$."
        ),
        "example_answer": (
            "a) Vì $\\triangle ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C}$. Áp dụng định lí tổng ba góc trong $\\triangle ABC$:\n"
            "$\\widehat{B} = \\widehat{C} = \\frac{180^\\circ - \\widehat{A}}{2} = \\frac{180^\\circ - 50^\\circ}{2} = 65^\\circ$.\n"
            "b) Xét $\\triangle ABM$ và $\\triangle ACM$ có:\n"
            "- $AB = AC$ (vì $\\triangle ABC$ cân tại $A$),\n"
            "- $BM = CM$ (vì $M$ là trung điểm của $BC$),\n"
            "- $AM$ là cạnh chung.\n"
            "Do đó $\\triangle ABM = \\triangle ACM$ (c.c.c). Suy ra $\\widehat{AMB} = \\widehat{AMC}$ (hai góc tương ứng). Mà $\\widehat{AMB} + \\widehat{AMC} = 180^\\circ$ (hai góc kề bù) nên $\\widehat{AMB} = \\widehat{AMC} = 90^\\circ$, hay $AM \\perp BC$."
        ),
        "real_life": "Kết cấu hình tam giác bằng nhau và tam giác cân được ứng dụng rộng rãi trong dàn khung mái nhà, chân máy ảnh, nhịp cầu thép vì tam giác là hình có tính ổn định vững chắc khi biết độ dài ba cạnh (trường hợp c.c.c).",
        "quiz": [
            mcq("biet", "Cho tam giác $ABC$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 75^\\circ$. Số đo góc $\\widehat{C}$ bằng:", ["$45^\\circ$", "$55^\\circ$", "$35^\\circ$", "$65^\\circ$"], 0, "Tổng ba góc trong một tam giác bằng $180^\\circ$ nên $\\widehat{C} = 180^\\circ - (60^\\circ + 75^\\circ) = 45^\\circ$."),
            mcq("biet", "Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = 5\\text{ cm}, BC = 7\\text{ cm}, DF = 6\\text{ cm}$. Độ dài cạnh $AC$ bằng:", ["$6\\text{ cm}$", "$5\\text{ cm}$", "$7\\text{ cm}$", "$12\\text{ cm}$"], 0, "Vì $\\triangle ABC = \\triangle DEF$ nên hai cạnh tương ứng $AC$ và $DF$ bằng nhau, suy ra $AC = DF = 6\\text{ cm}$."),
            mcq("biet", "Mỗi góc của một tam giác đều có số đo bằng bao nhiêu độ?", ["$60^\\circ$", "$45^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0, "Trong tam giác đều, ba góc bằng nhau và tổng bằng $180^\\circ$ nên mỗi góc có số đo $\\frac{180^\\circ}{3} = 60^\\circ$."),
            mcq("biet", "Nếu điểm $M$ nằm trên đường trung trực của đoạn thẳng $AB$ và $MA = 8\\text{ cm}$ thì độ dài đoạn thẳng $MB$ bằng:", ["$8\\text{ cm}$", "$4\\text{ cm}$", "$16\\text{ cm}$", "$6\\text{ cm}$"], 0, "Mọi điểm nằm trên đường trung trực của một đoạn thẳng đều cách đều hai mút của đoạn thẳng đó, nên $MB = MA = 8\\text{ cm}$."),
            mcq("hieu", "Cho tam giác $ABC$ cân tại $A$ có góc ở đáy $\\widehat{B} = 52^\\circ$. Số đo góc ở đỉnh $\\widehat{A}$ là:", ["$76^\\circ$", "$52^\\circ$", "$64^\\circ$", "$104^\\circ$"], 0, "Vì $\\triangle ABC$ cân tại $A$ nên $\\widehat{C} = \\widehat{B} = 52^\\circ$. Suy ra $\\widehat{A} = 180^\\circ - 2 \\cdot 52^\\circ = 76^\\circ$."),
            mcq("hieu", "Cho hai tam giác $ABC$ và $MNP$ có $AB = MN, AC = MP$. Cần thêm một điều kiện nào sau đây để $\\triangle ABC = \\triangle MNP$ theo trường hợp cạnh - góc - cạnh (c.g.c)?", ["$\\widehat{A} = \\widehat{M}$", "$\\widehat{B} = \\widehat{N}$", "$\\widehat{C} = \\widehat{P}$", "$BC = NP$"], 0, "Góc xen giữa hai cạnh $AB, AC$ là $\\widehat{A}$ và góc xen giữa hai cạnh $MN, MP$ là $\\widehat{M}$. Do đó cần điều kiện $\\widehat{A} = \\widehat{M}$ để hai tam giác bằng nhau theo trường hợp (c.g.c)."),
            tf4("hieu", "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$. Xét tính đúng sai của các khẳng định sau:", ["a) Hai góc nhọn $\\widehat{B}$ và $\\widehat{C}$ phụ nhau, tức là $\\widehat{B} + \\widehat{C} = 90^\\circ$.", "b) Số đo góc $\\widehat{C}$ bằng $30^\\circ$.", "c) Góc ngoài tại đỉnh $C$ của tam giác $ABC$ có số đo bằng $150^\\circ$.", "d) Tam giác $ABC$ là một tam giác cân."], [True, True, True, False], "a) Đúng vì trong tam giác vuông, hai góc nhọn luôn phụ nhau.\nb) Đúng vì $\\widehat{C} = 90^\\circ - \\widehat{B} = 90^\\circ - 60^\\circ = 30^\\circ$.\nc) Đúng vì góc ngoài tại đỉnh $C$ bằng $\\widehat{A} + \\widehat{B} = 90^\\circ + 60^\\circ = 150^\\circ$ (hoặc $180^\\circ - 30^\\circ = 150^\\circ$).\nd) Sai vì ba góc của tam giác là $90^\\circ, 60^\\circ, 30^\\circ$ đôi một khác nhau nên tam giác không cân."),
            tf4("hieu", "Cho tam giác $ABC$ cân tại $A$ ($AB = AC$). Gọi $I$ là trung điểm của đoạn thẳng $BC$. Xét các khẳng định sau:", ["a) $\\triangle ABI = \\triangle ACI$ theo trường hợp cạnh - cạnh - cạnh (c.c.c).", "b) Tia $AI$ là tia phân giác của góc $\\widehat{BAC}$.", "c) Đường thẳng $AI$ là đường trung trực của đoạn thẳng $BC$.", "d) Nếu $\\widehat{BAC} = 60^\\circ$ thì tam giác $ABC$ trở thành tam giác đều."], [True, True, True, True], "a) Đúng vì $AB = AC$, $IB = IC$ và $AI$ là cạnh chung.\nb) Đúng vì từ $\\triangle ABI = \\triangle ACI$ suy ra $\\widehat{BAI} = \\widehat{CAI}$ nên $AI$ là tia phân giác của $\\widehat{BAC}$.\nc) Đúng vì $AB = AC$ và $IB = IC$ nên cả $A$ và $I$ đều cách đều $B, C$, tức là $AI$ là đường trung trực của $BC$.\nd) Đúng vì tam giác cân có một góc bằng $60^\\circ$ là tam giác đều."),
            mcq("vandung", "Cho tam giác $ABC$ có $\\widehat{B} = 70^\\circ, \\widehat{C} = 40^\\circ$. Tia phân giác của góc $\\widehat{A}$ cắt cạnh $BC$ tại $D$. Số đo góc $\\widehat{ADB}$ bằng bao nhiêu độ?", ["$75^\\circ$", "$105^\\circ$", "$70^\\circ$", "$80^\\circ$"], 0, "Ta có $\\widehat{BAC} = 180^\\circ - (70^\\circ + 40^\\circ) = 70^\\circ$. Vì $AD$ là tia phân giác của $\\widehat{BAC}$ nên $\\widehat{DAC} = \\frac{70^\\circ}{2} = 35^\\circ$. Góc $\\widehat{ADB}$ là góc ngoài tại đỉnh $D$ của $\\triangle ADC$ nên $\\widehat{ADB} = \\widehat{DAC} + \\widehat{C} = 35^\\circ + 40^\\circ = 75^\\circ$."),
            short("vandung", "Trong một tam giác cân, biết góc ở đỉnh có số đo bằng $44^\\circ$. Tính số đo một góc ở đáy của tam giác cân đó (đơn vị: độ).", ["68"], "Gọi số đo mỗi góc ở đáy là $x$. Ta có $2x + 44^\\circ = 180^\\circ \\Rightarrow 2x = 136^\\circ \\Rightarrow x = 68^\\circ$."),
        ],
    },
    {
        "topic": "l7-ch05-thu-thap-va-bieu-dien-du-lieu",
        "title": "Thu thập và biểu diễn dữ liệu",
        "icon": "📊",
        "description": "Thu thập và phân loại dữ liệu (số liệu và dữ liệu không là số), tính đại diện của dữ liệu, đọc và phân tích biểu đồ hình quạt tròn và biểu đồ đoạn thẳng (Bài 17 - Bài 19, SGK Toán 7 Tập 1).",
        "requirements": [
            "Thực hiện và lí giải được việc thu thập, phân loại dữ liệu theo các tiêu chí cho trước từ những nguồn như văn bản, bảng biểu, kiến thức trong các môn học khác và trong thực tiễn.",
            "Giải thích được tính hợp lí và tính đại diện của dữ liệu theo các tiêu chí toán học đơn giản.",
            "Đọc và mô tả thành thạo các dữ liệu ở dạng biểu đồ thống kê: biểu đồ hình quạt tròn (pie chart) và biểu đồ đoạn thẳng (line graph).",
            "Lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp ở dạng biểu đồ hình quạt tròn (cho sẵn hình tròn chia phần) và biểu đồ đoạn thẳng.",
            "Nhận biết được những dạng biểu diễn khác nhau cho một tập dữ liệu và giải quyết được các vấn đề đơn giản liên quan đến các số liệu thu được.",
        ],
        "definition": "Dữ liệu được chia thành hai loại: dữ liệu là số (số liệu / dữ liệu định lượng) và dữ liệu không là số (dữ liệu định tính, gồm loại có thể sắp thứ tự và loại không thể sắp thứ tự). Biểu đồ hình quạt tròn dùng để biểu diễn tỉ lệ phần trăm của từng phần so với toàn thể; biểu đồ đoạn thẳng dùng để biểu diễn sự thay đổi của một đại lượng theo thời gian.",
        "theory": (
            "### Bài 17. Thu thập và phân loại dữ liệu (trang 89)\n"
            "- Có nhiều cách thu thập dữ liệu như quan sát, làm thí nghiệm, lập phiếu hỏi hoặc thu thập từ các nguồn có sẵn (sách báo, trang web uy tín). Để đưa ra kết luận hợp lí, dữ liệu thu được phải đảm bảo tính đại diện cho toàn bộ đối tượng đang được quan tâm.\n"
            "### Bài 18. Biểu đồ hình quạt tròn (trang 94)\n"
            "- Biểu đồ hình quạt tròn dùng các hình quạt tròn trong một hình tròn để biểu diễn tỉ lệ phần trăm của các phần so với toàn bộ dữ liệu (cả hình tròn ứng với $100\\%$ và góc ở tâm $360^\\circ$). Hai hình quạt tròn bằng nhau biểu diễn cùng một tỉ lệ.\n"
            "### Bài 19. Biểu đồ đoạn thẳng (trang 101)\n"
            "- Biểu đồ đoạn thẳng thường dùng để biểu diễn sự thay đổi của một đại lượng theo thời gian. Trục ngang biểu diễn thời gian, trục đứng biểu diễn đại lượng đang quan tâm, mỗi điểm biểu diễn giá trị của đại lượng tại một thời điểm và các điểm liên tiếp được nối với nhau bằng các đoạn thẳng."
        ),
        "formulas": [
            G("Tính toán trên Biểu đồ hình quạt tròn", F("Tổng tỉ lệ phần trăm trên toàn bộ biểu đồ", "$p_1\\% + p_2\\% + \\dots + p_k\\% = 100\\%$"), F("Giá trị của một phần khi biết tổng N và tỉ lệ p%", "$\\text{Giá trị phần} = N \\cdot \\frac{p}{100}$"), F("Số đo góc ở tâm ứng với tỉ lệ p%", "$\\alpha = 360^\\circ \\cdot \\frac{p}{100}$")),
            G("Phân tích Biểu đồ đoạn thẳng", F("Độ tăng / giảm giữa hai thời điểm", "$\\Delta y = y_2 - y_1$"), F("Tỉ lệ phần trăm tăng trưởng", "$\\%\\text{ tăng} = \\frac{y_2 - y_1}{y_1} \\cdot 100\\%$")),
        ],
        "example": (
            "Biểu đồ hình quạt tròn thống kê kết quả học tập học kì I của $400$ học sinh khối 7 tại một trường THCS gồm 4 mức: Tốt ($25\\%$), Khá ($45\\%$), Đạt ($25\\%$) và Chưa đạt (phần còn lại).\n"
            "a) Tính tỉ lệ phần trăm và số học sinh ở mức Chưa đạt.\n"
            "b) Tính số học sinh xếp loại Khá."
        ),
        "example_answer": (
            "a) Tổng tỉ lệ phần trăm của cả 4 mức là $100\\%$. Do đó tỉ lệ học sinh ở mức Chưa đạt là:\n"
            "$100\\% - (25\\% + 45\\% + 25\\%) = 5\\%$.\n"
            "Số học sinh ở mức Chưa đạt là: $400 \\cdot 5\\% = 400 \\cdot \\frac{5}{100} = 20$ (học sinh).\n"
            "b) Số học sinh xếp loại Khá là: $400 \\cdot 45\\% = 400 \\cdot \\frac{45}{100} = 180$ (học sinh)."
        ),
        "real_life": "Biểu đồ hình quạt tròn giúp các gia đình quản lí cơ cấu chi tiêu hàng tháng (ăn uống, giáo dục, tiết kiệm), còn biểu đồ đoạn thẳng giúp theo dõi biến động nhiệt độ trong tuần, lượng mưa các tháng trong năm hoặc doanh thu cửa hàng.",
        "quiz": [
            mcq("biet", "Trong các dữ liệu sau, dữ liệu nào là số liệu (dữ liệu định lượng)?", ["Chiều cao (tính bằng cm) của các học sinh trong tổ 1", "Tên các môn thể thao yêu thích của học sinh lớp 7A", "Xếp loại mức độ hài lòng: Rất hài lòng, Hài lòng, Chưa hài lòng", "Nơi sinh của các bạn học sinh trong lớp"], 0, "Chiều cao được biểu diễn bằng các con số cụ thể nên là số liệu (dữ liệu định lượng); các phương án còn lại là dữ liệu không là số."),
            mcq("biet", "Để biểu diễn sự thay đổi nhiệt độ trung bình của Hà Nội qua $12$ tháng trong năm, loại biểu đồ nào sau đây là thích hợp nhất?", ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ tranh", "Sơ đồ Ven"], 0, "Biểu đồ đoạn thẳng là công cụ thích hợp nhất để biểu diễn sự thay đổi của một đại lượng (nhiệt độ) theo thời gian (12 tháng)."),
            mcq("biet", "Trong một biểu đồ hình quạt tròn, tổng các tỉ lệ phần trăm của tất cả các hình quạt thành phần luôn bằng:", ["$100\\%$", "$360\\%$", "$50\\%$", "$180\\%$"], 0, "Cả hình tròn biểu diễn toàn bộ dữ liệu nên tổng tỉ lệ phần trăm của tất cả các thành phần luôn bằng $100\\%$."),
            mcq("biet", "Trong dữ liệu định tính gồm các mức đánh giá: \"Tốt, Khá, Đạt, Chưa đạt\", đây là loại dữ liệu nào?", ["Dữ liệu không là số, có thể sắp thứ tự", "Dữ liệu không là số, không thể sắp thứ tự", "Số liệu rời rạc", "Số liệu liên tục"], 0, "Các mức \"Tốt, Khá, Đạt, Chưa đạt\" không phải là số nhưng có thể sắp xếp theo thứ tự từ cao xuống thấp nên là dữ liệu không là số, có thể sắp thứ tự."),
            mcq("hieu", "Muốn khảo sát về thời gian tự học ở nhà của toàn bộ học sinh khối 7 trong trường, cách chọn mẫu khảo sát nào sau đây đảm bảo tính đại diện tốt nhất?", ["Chọn ngẫu nhiên $10$ học sinh ở mỗi lớp thuộc khối 7", "Chỉ hỏi các bạn trong đội tuyển học sinh giỏi Toán khối 7", "Chỉ hỏi các bạn nam trong câu lạc bộ bóng đá của trường", "Chỉ hỏi $20$ bạn học sinh của duy nhất lớp 7A1"], 0, "Chọn ngẫu nhiên học sinh từ tất cả các lớp trong khối 7 giúp mẫu khảo sát khách quan và có tính đại diện cho toàn khối."),
            mcq("hieu", "Trên biểu đồ hình quạt tròn biểu diễn diện tích đất của một trang trại rộng $250\\text{ ha}$, phần đất trồng cây ăn quả chiếm $36\\%$. Diện tích đất trồng cây ăn quả là:", ["$90\\text{ ha}$", "$80\\text{ ha}$", "$72\\text{ ha}$", "$100\\text{ ha}$"], 0, "Diện tích đất trồng cây ăn quả là $250 \\cdot 36\\% = 250 \\cdot \\frac{36}{100} = 90\\text{ (ha)}$."),
            tf4("hieu", "Một biểu đồ hình quạt tròn biểu diễn tỉ lệ các loại sách trong thư viện trường học (gồm tổng cộng $1200$ cuốn): Sách giáo khoa ($40\\%$), Sách tham khảo ($35\\%$), Truyện thiếu nhi ($15\\%$) và Báo - Tạp chí (phần còn lại). Xét các khẳng định sau:", ["a) Tỉ lệ phần trăm của Báo - Tạp chí trong thư viện là $10\\%$.", "b) Số lượng Sách giáo khoa trong thư viện là $480$ cuốn.", "c) Số lượng Sách tham khảo nhiều hơn Truyện thiếu nhi là $200$ cuốn.", "d) Hình quạt biểu diễn Sách giáo khoa lớn gấp $4$ lần hình quạt biểu diễn Báo - Tạp chí."], [True, True, False, True], "a) Đúng vì $100\\% - (40\\% + 35\\% + 15\\%) = 10\\%$.\nb) Đúng vì $1200 \\cdot 40\\% = 480$ (cuốn).\nc) Sai vì hiệu tỉ lệ là $35\\% - 15\\% = 20\\%$, tương ứng với $1200 \\cdot 20\\% = 240$ cuốn ($\\neq 200$ cuốn).\nd) Đúng vì $40\\% : 10\\% = 4$."),
            tf4("hieu", "Biểu đồ đoạn thẳng ghi lại số lượng máy tính bán được của một cửa hàng trong 4 quý năm 2025 lần lượt là: Quý I: $120$ chiếc; Quý II: $150$ chiếc; Quý III: $135$ chiếc; Quý IV: $195$ chiếc. Xét các khẳng định sau:", ["a) Trục ngang của biểu đồ biểu diễn các quý trong năm, trục đứng biểu diễn số lượng máy tính bán được.", "b) Tổng số máy tính cửa hàng bán được trong cả năm 2025 là $600$ chiếc.", "c) Từ Quý I sang Quý II, số lượng máy tính bán được tăng $25\\%$.", "d) Đoạn thẳng nối từ Quý II sang Quý III đi lên từ trái sang phải."], [True, True, True, False], "a) Đúng theo cấu tạo của biểu đồ đoạn thẳng.\nb) Đúng vì $120 + 150 + 135 + 195 = 600$ (chiếc).\nc) Đúng vì mức tăng là $\\frac{150 - 120}{120} \\cdot 100\\% = \\frac{30}{120} \\cdot 100\\% = 25\\%$.\nd) Sai vì từ Quý II ($150$ chiếc) sang Quý III ($135$ chiếc) số lượng giảm nên đoạn thẳng đi xuống."),
            mcq("vandung", "Gia đình bạn An có tổng thu nhập hàng tháng là $25$ triệu đồng, được phân bổ trên biểu đồ hình quạt tròn gồm: Chi tiêu sinh hoạt ($52\\%$), Giáo dục ($20\\%$), Y tế & Dự phòng ($8\\%$) và phần còn lại để Tiết kiệm. Hỏi sau $1$ năm ($12$ tháng), gia đình bạn An tiết kiệm được bao nhiêu triệu đồng?", ["$60$ triệu đồng", "$50$ triệu đồng", "$48$ triệu đồng", "$72$ triệu đồng"], 0, "Tỉ lệ tiền tiết kiệm mỗi tháng là $100\\% - (52\\% + 20\\% + 8\\%) = 20\\%$. Số tiền tiết kiệm mỗi tháng là $25 \\cdot 20\\% = 5$ (triệu đồng). Sau $12$ tháng, tổng số tiền tiết kiệm được là $5 \\cdot 12 = 60$ (triệu đồng)."),
            short("vandung", "Khảo sát môn thể thao yêu thích của học sinh khối 7 thu được biểu đồ hình quạt tròn, trong đó môn Cầu lông chiếm $22,5\\%$ và có $54$ học sinh lựa chọn. Hỏi tổng số học sinh khối 7 tham gia khảo sát là bao nhiêu em?", ["240"], "Tổng số học sinh khối 7 tham gia khảo sát là $54 : 22,5\\% = 54 : \\frac{22,5}{100} = 240$ (học sinh)."),
        ],
    },
    {
        "topic": "l7-ch06-ti-le-thuc-va-dai-luong-ti-le",
        "title": "Tỉ lệ thức và đại lượng tỉ lệ",
        "icon": "⚖️",
        "description": "Tỉ lệ thức, tính chất của dãy tỉ số bằng nhau, đại lượng tỉ lệ thuận, đại lượng tỉ lệ nghịch và ứng dụng giải bài toán thực tiễn (Bài 20 - Bài 23, SGK Toán 7 Tập 2).",
        "requirements": [
            "Nhận biết được tỉ lệ thức và các tính chất của tỉ lệ thức.",
            "Nhận biết được dãy tỉ số bằng nhau và vận dụng được tính chất của dãy tỉ số bằng nhau trong giải toán.",
            "Nhận biết được hai đại lượng tỉ lệ thuận, hệ số tỉ lệ và các tính chất của hai đại lượng tỉ lệ thuận.",
            "Nhận biết được hai đại lượng tỉ lệ nghịch, hệ số tỉ lệ và các tính chất của hai đại lượng tỉ lệ nghịch.",
            "Giải được một số bài toán đơn giản về đại lượng tỉ lệ thuận và đại lượng tỉ lệ nghịch (ví dụ bài toán chia một số thành các phần tỉ lệ thuận hoặc tỉ lệ nghịch với các số cho trước, bài toán năng suất lao động, chuyển động).",
        ],
        "definition": "Tỉ lệ thức là đẳng thức của hai tỉ số $\\frac{a}{b} = \\frac{c}{d}$ ($b, d \\neq 0$). Đại lượng $y$ tỉ lệ thuận với đại lượng $x$ theo hệ số tỉ lệ $k$ ($k \\neq 0$) nếu $y = kx$. Đại lượng $y$ tỉ lệ nghịch với đại lượng $x$ theo hệ số tỉ lệ $a$ ($a \\neq 0$) nếu $y = \\frac{a}{x}$ (hay $xy = a$).",
        "theory": (
            "### Bài 20. Tỉ lệ thức (trang 4)\n"
            "- Tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$ còn được viết là $a : b = c : d$. Tính chất cơ bản: Nếu $\\frac{a}{b} = \\frac{c}{d}$ thì $ad = bc$. Ngược lại, nếu $ad = bc$ và $a, b, c, d \\neq 0$ thì ta lập được $4$ tỉ lệ thức: $\\frac{a}{b} = \\frac{c}{d}$, $\\frac{a}{c} = \\frac{b}{d}$, $\\frac{d}{b} = \\frac{c}{a}$, $\\frac{d}{c} = \\frac{b}{a}$.\n"
            "### Bài 21. Tính chất của dãy tỉ số bằng nhau (trang 8)\n"
            "- Từ $\\frac{a}{b} = \\frac{c}{d}$ suy ra $\\frac{a}{b} = \\frac{c}{d} = \\frac{a+c}{b+d} = \\frac{a-c}{b-d}$ (với các mẫu số khác $0$). Mở rộng cho dãy ba tỉ số bằng nhau $\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f}$. Khi nói các số $a, b, c$ tỉ lệ với các số $x, y, z$, ta viết $\\frac{a}{x} = \\frac{b}{y} = \\frac{c}{z}$ hoặc $a : b : c = x : y : z$.\n"
            "### Bài 22. Đại lượng tỉ lệ thuận (trang 11)\n"
            "- Nếu $y = kx$ ($k \\neq 0$) thì $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $k$, và $x$ tỉ lệ thuận với $y$ theo hệ số tỉ lệ $\\frac{1}{k}$. Tính chất: Tỉ số hai giá trị tương ứng luôn không đổi ($\\frac{y_1}{x_1} = \\frac{y_2}{x_2} = \\dots = k$) và tỉ số hai giá trị bất kì của đại lượng này bằng tỉ số hai giá trị tương ứng của đại lượng kia ($\\frac{y_1}{y_2} = \\frac{x_1}{x_2}$).\n"
            "### Bài 23. Đại lượng tỉ lệ nghịch (trang 15)\n"
            "- Nếu $y = \\frac{a}{x}$ hay $xy = a$ ($a \\neq 0$) thì $y$ tỉ lệ nghịch với $x$ theo hệ số tỉ lệ $a$ (và $x$ cũng tỉ lệ nghịch với $y$ theo hệ số tỉ lệ $a$). Tính chất: Tích hai giá trị tương ứng luôn không đổi ($x_1 y_1 = x_2 y_2 = \\dots = a$) và tỉ số hai giá trị bất kì của đại lượng này bằng nghịch đảo của tỉ số hai giá trị tương ứng của đại lượng kia ($\\frac{y_1}{y_2} = \\frac{x_2}{x_1}$)."
        ),
        "formulas": [
            G("Tỉ lệ thức & Dãy tỉ số bằng nhau", F("Tính chất cơ bản của tỉ lệ thức", "$\\frac{a}{b} = \\frac{c}{d} \\iff a \\cdot d = b \\cdot c \\quad (b, d \\neq 0)$"), F("Tính chất của dãy hai tỉ số bằng nhau", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{a + c}{b + d} = \\frac{a - c}{b - d} \\quad (b \\pm d \\neq 0)$"), F("Tính chất mở rộng cho ba tỉ số", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{a + c + e}{b + d + f} = \\frac{a - c + e}{b - d + f}$")),
            G("Đại lượng tỉ lệ thuận & Đại lượng tỉ lệ nghịch", F("Đại lượng tỉ lệ thuận (hệ số k khác 0)", "$y = kx \\implies \\frac{y_1}{x_1} = \\frac{y_2}{x_2} = k, \\quad \\frac{y_1}{y_2} = \\frac{x_1}{x_2}$"), F("Đại lượng tỉ lệ nghịch (hệ số a khác 0)", "$y = \\frac{a}{x} \\iff x \\cdot y = a \\implies x_1 y_1 = x_2 y_2 = a, \\quad \\frac{y_1}{y_2} = \\frac{x_2}{x_1}$")),
        ],
        "example": "Ba lớp 7A, 7B, 7C tham gia trồng cây xanh hưởng ứng Tết trồng cây. Biết số cây trồng được của ba lớp 7A, 7B, 7C tỉ lệ với các số $3; 4; 5$ và tổng số cây ba lớp trồng được là $96$ cây. Tính số cây mỗi lớp đã trồng.",
        "example_answer": (
            "Gọi số cây trồng được của ba lớp 7A, 7B, 7C lần lượt là $x, y, z$ ($x, y, z \\in \\mathbb{N}^*$).\n"
            "Theo đề bài, ta có $\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5}$ và $x + y + z = 96$.\n"
            "Áp dụng tính chất của dãy tỉ số bằng nhau:\n"
            "$\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5} = \\frac{x + y + z}{3 + 4 + 5} = \\frac{96}{12} = 8$.\n"
            "Suy ra:\n"
            "- $x = 3 \\cdot 8 = 24$ (cây);\n"
            "- $y = 4 \\cdot 8 = 32$ (cây);\n"
            "- $z = 5 \\cdot 8 = 40$ (cây).\n"
            "Vậy lớp 7A trồng được $24$ cây, lớp 7B trồng được $32$ cây và lớp 7C trồng được $40$ cây."
        ),
        "real_life": "Tỉ lệ thức và đại lượng tỉ lệ được ứng dụng khi đọc tỉ lệ bản đồ, pha chế dung dịch hoặc công thức làm bánh theo số người ăn (tỉ lệ thuận), và tính số công nhân cần thiết để hoàn thành công trình đúng tiến độ (tỉ lệ nghịch).",
        "quiz": [
            mcq("biet", "Từ đẳng thức $2 \\cdot 15 = 5 \\cdot 6$, ta có thể lập được tỉ lệ thức nào dưới đây?", ["$\\frac{2}{5} = \\frac{6}{15}$", "$\\frac{2}{15} = \\frac{5}{6}$", "$\\frac{2}{6} = \\frac{15}{5}$", "$\\frac{5}{2} = \\frac{6}{15}$"], 0, "Với $\\frac{2}{5} = \\frac{6}{15}$, tích chéo là $2 \\cdot 15 = 5 \\cdot 6 = 30$ (đúng)."),
            mcq("biet", "Cho biết đại lượng $y$ tỉ lệ thuận với đại lượng $x$ theo hệ số tỉ lệ $k = -3$. Công thức biểu diễn $y$ theo $x$ là:", ["$y = -3x$", "$y = -\\frac{3}{x}$", "$y = -\\frac{1}{3}x$", "$x = -3y$"], 0, "Theo định nghĩa, $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $k = -3$ thì $y = -3x$."),
            mcq("biet", "Cho hai đại lượng $x$ và $y$ tỉ lệ nghịch với nhau. Biết khi $x = 4$ thì $y = 9$. Hệ số tỉ lệ $a$ của $y$ đối với $x$ bằng:", ["$36$", "$\\frac{9}{4}$", "$\\frac{4}{9}$", "$13$"], 0, "Hai đại lượng tỉ lệ nghịch có hệ số tỉ lệ $a = x \\cdot y = 4 \\cdot 9 = 36$."),
            mcq("biet", "Nếu ba số $a, b, c$ tỉ lệ với các số $2; 5; 7$ thì dãy tỉ số bằng nhau nào sau đây là đúng?", ["$\\frac{a}{2} = \\frac{b}{5} = \\frac{c}{7}$", "$2a = 5b = 7c$", "$\\frac{a}{7} = \\frac{b}{5} = \\frac{c}{2}$", "$a : 5 = b : 2 = c : 7$"], 0, "Ba số $a, b, c$ tỉ lệ với $2; 5; 7$ được viết là $\\frac{a}{2} = \\frac{b}{5} = \\frac{c}{7}$."),
            mcq("hieu", "Tìm hai số $x, y$ biết $\\frac{x}{4} = \\frac{y}{7}$ và $x + y = 33$.", ["$x = 12; y = 21$", "$x = 21; y = 12$", "$x = 8; y = 25$", "$x = 16; y = 17$"], 0, "Áp dụng tính chất dãy tỉ số bằng nhau: $\\frac{x}{4} = \\frac{y}{7} = \\frac{x+y}{4+7} = \\frac{33}{11} = 3$. Suy ra $x = 12$ và $y = 21$."),
            mcq("hieu", "Cho $x$ và $y$ là hai đại lượng tỉ lệ thuận với nhau. Biết khi $x = 5$ thì $y = 15$. Hỏi khi $x = -4$ thì giá trị của $y$ bằng bao nhiêu?", ["$-12$", "$12$", "$-\\frac{4}{3}$", "$-20$"], 0, "Hệ số tỉ lệ của $y$ đối với $x$ là $k = \\frac{y}{x} = \\frac{15}{5} = 3$. Khi $x = -4$ thì $y = 3 \\cdot (-4) = -12$."),
            tf4("hieu", "Cho hai số thực $x, y$ thỏa mãn $\\frac{x}{5} = \\frac{y}{3}$ và $x - y = 16$. Xét tính đúng sai của các khẳng định sau:", ["a) Theo tính chất dãy tỉ số bằng nhau, ta có $\\frac{x}{5} = \\frac{y}{3} = \\frac{x - y}{5 - 3}$.", "b) Giá trị chung của mỗi tỉ số $\\frac{x}{5}$ và $\\frac{y}{3}$ bằng $8$.", "c) Giá trị của $x$ bằng $40$ và giá trị của $y$ bằng $24$.", "d) Tổng $x + y$ bằng $56$."], [True, True, True, False], "a), b) Đúng vì $\\frac{x}{5} = \\frac{y}{3} = \\frac{x - y}{5 - 3} = \\frac{16}{2} = 8$.\nc) Đúng vì $x = 5 \\cdot 8 = 40$ và $y = 3 \\cdot 8 = 24$.\nd) Sai vì $x + y = 40 + 24 = 64 \\neq 56$."),
            tf4("hieu", "Một đội công nhân cần hoàn thành một công việc có khối lượng cố định (năng suất làm việc của mỗi công nhân như nhau). Gọi $x$ là số công nhân và $y$ là số giờ để hoàn thành công việc đó. Biết $12$ công nhân làm xong công việc trong $8$ giờ. Xét các khẳng định sau:", ["a) Hai đại lượng $x$ và $y$ là hai đại lượng tỉ lệ thuận.", "b) Hệ số tỉ lệ giữa $x$ và $y$ là $a = x \\cdot y = 96$.", "c) Nếu có $16$ công nhân thì thời gian hoàn thành công việc là $6$ giờ.", "d) Muốn hoàn thành công việc đó trong $4$ giờ thì cần $24$ công nhân."], [False, True, True, True], "a) Sai vì với cùng một công việc, số công nhân và số giờ hoàn thành là hai đại lượng tỉ lệ nghịch.\nb) Đúng vì tích $x \\cdot y = 12 \\cdot 8 = 96$.\nc) Đúng vì khi $x = 16$ thì $y = \\frac{96}{16} = 6$ (giờ).\nd) Đúng vì khi $y = 4$ thì $x = \\frac{96}{4} = 24$ (công nhân)."),
            mcq("vandung", "Số đo ba góc $\\widehat{A}, \\widehat{B}, \\widehat{C}$ của một tam giác $ABC$ tỉ lệ với các số $2; 3; 4$. Số đo góc lớn nhất của tam giác $ABC$ là:", ["$80^\\circ$", "$60^\\circ$", "$40^\\circ$", "$90^\\circ$"], 0, "Trong $\\triangle ABC$, $\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$. Áp dụng tính chất dãy tỉ số bằng nhau: $\\frac{\\widehat{A}}{2} = \\frac{\\widehat{B}}{3} = \\frac{\\widehat{C}}{4} = \\frac{180^\\circ}{2+3+4} = 20^\\circ$. Góc lớn nhất là $\\widehat{C} = 4 \\cdot 20^\\circ = 80^\\circ$."),
            short("vandung", "Tìm số thực $x$ trong tỉ lệ thức $\\frac{x - 1}{6} = \\frac{15}{9}$.", ["11"], "Từ $\\frac{x - 1}{6} = \\frac{15}{9} \\Rightarrow x - 1 = \\frac{6 \\cdot 15}{9} = 10 \\Rightarrow x = 11$."),
        ],
    },
    {
        "topic": "l7-ch07-bieu-thuc-dai-so-va-da-thuc-mot-bien",
        "title": "Biểu thức đại số và đa thức một biến",
        "icon": "🧮",
        "description": "Biểu thức đại số, giá trị của biểu thức đại số, đơn thức và đa thức một biến, bậc, hệ số và nghiệm của đa thức một biến, các phép cộng, trừ, nhân, chia đa thức một biến (Bài 24 - Bài 28, SGK Toán 7 Tập 2).",
        "requirements": [
            "Nhận biết được biểu thức số, biểu thức đại số và tính được giá trị của một biểu thức đại số tại những giá trị cho trước của biến.",
            "Nhận biết được định nghĩa đơn thức một biến, đa thức một biến và thu gọn, sắp xếp được đa thức một biến.",
            "Xác định được bậc, hệ số cao nhất và hệ số tự do của một đa thức một biến.",
            "Nhận biết được nghiệm của đa thức một biến và kiểm tra một số có là nghiệm của đa thức hay không.",
            "Thực hiện được các phép tính: phép cộng, phép trừ, phép nhân và phép chia hết (hoặc chia có dư) hai đa thức một biến.",
        ],
        "definition": "Biểu thức đại số là biểu thức mà ngoài các số, các kí hiệu phép toán cộng, trừ, nhân, chia, nâng lên lũy thừa, còn có các chữ đại diện cho các số (biến số). Đa thức một biến là tổng của những đơn thức của cùng một biến; mỗi số thực cũng được coi là một đa thức một biến.",
        "theory": (
            "### Bài 24. Biểu thức đại số (trang 22)\n"
            "- Biểu thức không chứa chữ gọi là biểu thức số; biểu thức chứa chữ đại diện cho số gọi là biểu thức đại số. Để tính giá trị của một biểu thức đại số tại những giá trị cho trước của các biến, ta thay các giá trị cho trước đó vào biểu thức rồi thực hiện các phép tính.\n"
            "### Bài 25. Đa thức một biến (trang 25)\n"
            "- Đơn thức một biến là biểu thức đại số có dạng tích của một số thực với một lũy thừa của biến (hệ số nhân với phần biến $x^k$, bậc là $k$). Đa thức một biến thu gọn là đa thức không còn hai đơn thức nào cùng bậc. Trong đa thức khác đa thức không đã thu gọn: bậc của hạng tử có bậc cao nhất là bậc của đa thức; hệ số của hạng tử bậc cao nhất gọi là hệ số cao nhất; hệ số của hạng tử bậc $0$ gọi là hệ số tự do. Nếu tại $x = a$, đa thức $P(x)$ có giá trị bằng $0$ ($P(a) = 0$) thì $a$ là một nghiệm của đa thức $P(x)$.\n"
            "### Bài 26. Phép cộng và phép trừ đa thức một biến (trang 31)\n"
            "- Để cộng hoặc trừ hai đa thức một biến, ta có thể đặt tính theo cột dọc (các đơn thức cùng bậc ở cùng một cột) hoặc bỏ dấu ngoặc rồi nhóm các hạng tử cùng bậc để thu gọn.\n"
            "### Bài 27. Phép nhân đa thức một biến (trang 35)\n"
            "- Muốn nhân hai đơn thức một biến, ta nhân hai hệ số với nhau và nhân hai phần biến với nhau ($ax^m \\cdot bx^n = (ab)x^{m+n}$). Muốn nhân một đa thức với một đa thức, ta nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.\n"
            "### Bài 28. Phép chia đa thức một biến (trang 39)\n"
            "- Với hai đa thức một biến $A$ và $B$ ($B \\neq 0$), luôn tồn tại duy nhất cặp đa thức $Q$ (thương) và $R$ (dư) sao cho $A = B \\cdot Q + R$, trong đó $R = 0$ (phép chia hết) hoặc bậc của $R$ nhỏ hơn bậc của $B$ (phép chia có dư)."
        ),
        "formulas": [
            G("Đơn thức & Đa thức một biến", F("Nhân hai đơn thức một biến", "$(a x^m) \\cdot (b x^n) = (a \\cdot b) x^{m+n}$"), F("Cộng, trừ hai đơn thức cùng bậc", "$a x^k + b x^k = (a + b) x^k, \\quad a x^k - b x^k = (a - b) x^k$"), F("Đa thức một biến sắp xếp theo lũy thừa giảm của biến", "$P(x) = a_n x^n + a_{n-1} x^{n-1} + \\dots + a_1 x + a_0 \\quad (a_n \\neq 0)$"), F("Điều kiện nghiệm của đa thức P(x)", "$x = a \\text{ là nghiệm của } P(x) \\iff P(a) = 0$")),
            G("Các phép toán trên Đa thức một biến", F("Nhân đơn thức với đa thức", "$A \\cdot (B + C) = A \\cdot B + A \\cdot C$"), F("Nhân hai đa thức", "$(A + B) \\cdot (C + D) = A \\cdot C + A \\cdot D + B \\cdot C + B \\cdot D$"), F("Phép chia đa thức A cho đa thức B (B khác 0)", "$A = B \\cdot Q + R \\quad (R = 0 \\text{ hoặc } \\deg(R) < \\deg(B))$")),
        ],
        "example": (
            "Cho hai đa thức $P(x) = 3x^3 - 2x^2 + 5x - 4$ và $Q(x) = -3x^3 + 2x^2 - x + 12$.\n"
            "a) Tính tổng $H(x) = P(x) + Q(x)$ và xác định bậc, hệ số cao nhất, hệ số tự do của $H(x)$.\n"
            "b) Tìm nghiệm của đa thức $H(x)$."
        ),
        "example_answer": (
            "a) Ta có:\n"
            "$H(x) = P(x) + Q(x) = (3x^3 - 3x^3) + (-2x^2 + 2x^2) + (5x - x) + (-4 + 12) = 4x + 8$.\n"
            "Đa thức $H(x) = 4x + 8$ có bậc là $1$, hệ số cao nhất là $4$ và hệ số tự do là $8$.\n"
            "b) Cho $H(x) = 0 \\Leftrightarrow 4x + 8 = 0 \\Leftrightarrow 4x = -8 \\Leftrightarrow x = -2$.\n"
            "Vậy nghiệm của đa thức $H(x)$ là $x = -2$."
        ),
        "real_life": "Biểu thức đại số và đa thức một biến giúp mô tả công thức tính quãng đường chuyển động, công thức tính diện tích, thể tích hình hộp khi kích thước thay đổi theo biến $x$, hoặc tính tổng cước phí taxi theo số kilômét di chuyển.",
        "quiz": [
            mcq("biet", "Biểu thức đại số biểu thị \"Tổng của hai lần số $x$ và bình phương của số $y$\" là:", ["$2x + y^2$", "$2(x + y)^2$", "$2x + 2y$", "$(2x + y)^2$"], 0, "Hai lần số $x$ là $2x$, bình phương của số $y$ là $y^2$, nên tổng của chúng là $2x + y^2$."),
            mcq("biet", "Cho đa thức một biến đã thu gọn $P(x) = -5x^4 + 3x^2 - 7x + 9$. Bậc và hệ số cao nhất của đa thức $P(x)$ lần lượt là:", ["Bậc $4$ và hệ số cao nhất là $-5$", "Bậc $4$ và hệ số cao nhất là $9$", "Bậc $4$ và hệ số cao nhất là $5$", "Bậc $3$ và hệ số cao nhất là $-5$"], 0, "Hạng tử có bậc cao nhất trong $P(x)$ là $-5x^4$ nên đa thức có bậc là $4$ và hệ số cao nhất là $-5$."),
            mcq("biet", "Số nào dưới đây là nghiệm của đa thức $F(x) = 2x - 6$?", ["$3$", "$-3$", "$6$", "$2$"], 0, "Thay $x = 3$ vào $F(x)$ ta được $F(3) = 2 \\cdot 3 - 6 = 0$, nên $x = 3$ là nghiệm của $F(x)$."),
            mcq("biet", "Tích của hai đơn thức $(-3x^2)$ và $(4x^3)$ bằng:", ["$-12x^5$", "$-12x^6$", "$12x^5$", "$x^5$"], 0, "Ta có $(-3x^2) \\cdot (4x^3) = (-3 \\cdot 4) \\cdot (x^2 \\cdot x^3) = -12x^5$."),
            mcq("hieu", "Giá trị của biểu thức đại số $A = 2x^2 - 3x + 1$ tại $x = -2$ là:", ["$15$", "$3$", "$-1$", "$11$"], 0, "Thay $x = -2$ vào $A$, ta được $A = 2 \\cdot (-2)^2 - 3 \\cdot (-2) + 1 = 2 \\cdot 4 + 6 + 1 = 15$."),
            mcq("hieu", "Kết quả của phép nhân $(x - 2)(x + 3)$ sau khi thu gọn là:", ["$x^2 + x - 6$", "$x^2 - x - 6$", "$x^2 + 5x - 6$", "$x^2 - 6$"], 0, "Ta có $(x - 2)(x + 3) = x^2 + 3x - 2x - 6 = x^2 + x - 6$."),
            tf4("hieu", "Cho đa thức $P(x) = 2x^3 - 4x^2 + 3x - 2x^3 + 4x^2 - 9$. Xét tính đúng sai của các khẳng định sau:", ["a) Đa thức $P(x)$ sau khi thu gọn là $P(x) = 3x - 9$.", "b) Bậc của đa thức $P(x)$ bằng $3$.", "c) Hệ số tự do của đa thức $P(x)$ là $-9$.", "d) Đa thức $P(x)$ có nghiệm duy nhất là $x = 3$."], [True, False, True, True], "a) Đúng vì $P(x) = (2x^3 - 2x^3) + (-4x^2 + 4x^2) + 3x - 9 = 3x - 9$.\nb) Sai vì bậc của đa thức được xác định sau khi thu gọn; $P(x) = 3x - 9$ có bậc là $1$ ($\\neq 3$).\nc) Đúng vì hạng tử bậc $0$ của $P(x)$ là $-9$.\nd) Đúng vì $P(x) = 0 \\Leftrightarrow 3x - 9 = 0 \\Leftrightarrow x = 3$."),
            tf4("hieu", "Cho hai đa thức $A(x) = x^2 - 5x + 6$ và $B(x) = x - 2$. Xét tính đúng sai của các khẳng định sau:", ["a) $x = 2$ là một nghiệm chung của cả hai đa thức $A(x)$ và $B(x)$.", "b) Hiệu $A(x) - B(x)$ bằng $x^2 - 6x + 8$.", "c) Phép chia đa thức $A(x)$ cho đa thức $B(x)$ là phép chia hết và có thương là $Q(x) = x - 3$.", "d) Tại $x = 3$, giá trị của đa thức $A(x)$ bằng $6$."], [True, True, True, False], "a) Đúng vì $A(2) = 2^2 - 5 \\cdot 2 + 6 = 0$ và $B(2) = 2 - 2 = 0$.\nb) Đúng vì $A(x) - B(x) = (x^2 - 5x + 6) - (x - 2) = x^2 - 6x + 8$.\nc) Đúng vì $(x - 2)(x - 3) = x^2 - 5x + 6 = A(x)$, nên $A(x) : B(x) = x - 3$.\nd) Sai vì tại $x = 3$, $A(3) = 3^2 - 5 \\cdot 3 + 6 = 0 \\neq 6$."),
            mcq("vandung", "Tìm hệ số $a$ để đa thức $P(x) = x^3 - 3x^2 + 5x + a$ chia hết cho đa thức $x - 1$.", ["$a = -3$", "$a = 3$", "$a = -1$", "$a = 1$"], 0, "Thực hiện phép chia hoặc biến đổi $P(x) = (x - 1)(x^2 - 2x + 3) + (a + 3)$. Để phép chia là phép chia hết thì số dư phải bằng $0$, tức là $a + 3 = 0 \\Leftrightarrow a = -3$."),
            short("vandung", "Cho đa thức $M(x) = 3x^2 - 5x + m$. Tìm giá trị của $m$ biết rằng $x = 2$ là một nghiệm của đa thức $M(x)$.", ["-2"], "Vì $x = 2$ là nghiệm của $M(x)$ nên $M(2) = 0 \\Leftrightarrow 3 \\cdot 2^2 - 5 \\cdot 2 + m = 0 \\Leftrightarrow 12 - 10 + m = 0 \\Leftrightarrow m = -2$."),
        ],
    },
    {
        "topic": "l7-ch08-lam-quen-voi-bien-co-va-xac-suat-cua-bien-co",
        "title": "Làm quen với biến cố và xác suất của biến cố",
        "icon": "🎲",
        "description": "Biến cố chắc chắn, biến cố không thể, biến cố ngẫu nhiên và xác suất của biến cố trong một số trò chơi, thí nghiệm đơn giản (Bài 29 - Bài 30, SGK Toán 7 Tập 2).",
        "requirements": [
            "Làm quen với các khái niệm mở đầu về biến cố ngẫu nhiên, biến cố chắc chắn và biến cố không thể trong các ví dụ đơn giản.",
            "Nhận biết được xác suất của một biến cố là một con số từ 0 đến 1 đo lường khả năng xảy ra của biến cố đó.",
            "Biết xác suất của biến cố không thể bằng 0, xác suất của biến cố chắc chắn bằng 1.",
            "Tính được xác suất của một biến cố ngẫu nhiên trong một số ví dụ có các kết quả đồng khả năng (như tung đồng xu, gieo xúc xắc, rút thẻ ngẫu nhiên).",
        ],
        "definition": "Các hiện tượng, sự kiện trong tự nhiên hay trong một phép thử được gọi là biến cố. Biến cố chắc chắn là biến cố biết trước luôn xảy ra (xác suất bằng $1$); biến cố không thể là biến cố biết trước không bao giờ xảy ra (xác suất bằng $0$); biến cố ngẫu nhiên là biến cố không thể biết trước có xảy ra hay không.",
        "theory": (
            "### Bài 29. Làm quen với biến cố (trang 47)\n"
            "- Trong các trò chơi hay thí nghiệm (như gieo xúc xắc, rút thẻ trong hộp, quay vòng quay), sự kiện chắc chắn xảy ra gọi là biến cố chắc chắn; sự kiện không bao giờ xảy ra gọi là biến cố không thể; sự kiện có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả phép thử gọi là biến cố ngẫu nhiên.\n"
            "### Bài 30. Làm quen với xác suất của biến cố (trang 52)\n"
            "- Khả năng xảy ra của một biến cố được đo lường bởi một số nhận giá trị từ $0$ đến $1$, gọi là xác suất của biến cố đó, kí hiệu $P(A)$. Nếu một phép thử có $n$ kết quả có cùng khả năng xảy ra (đồng khả năng) và chỉ có duy nhất $1$ kết quả thuận lợi cho biến cố $A$ thì xác suất của $A$ là $\\frac{1}{n}$; tổng quát nếu có $k$ kết quả thuận lợi cho biến cố $A$ thì $P(A) = \\frac{k}{n}$."
        ),
        "formulas": [
            G("Xác suất của các loại biến cố", F("Xác suất của biến cố không thể", "$P(A) = 0$"), F("Xác suất của biến cố chắc chắn", "$P(A) = 1$"), F("Tập giá trị của xác suất mọi biến cố", "$0 \\le P(A) \\le 1$")),
            G("Xác suất của biến cố đồng khả năng", F("Xác suất của 1 kết quả trong n kết quả đồng khả năng", "$P = \\frac{1}{n}$"), F("Xác suất của biến cố A có k kết quả thuận lợi trong n kết quả đồng khả năng", "$P(A) = \\frac{k}{n}$")),
        ],
        "example": (
            "Một hộp có $12$ chiếc thẻ cùng loại, mỗi thẻ được ghi một trong các số $1, 2, 3, \\dots, 12$; hai thẻ khác nhau thì ghi hai số khác nhau. Rút ngẫu nhiên một chiếc thẻ trong hộp.\n"
            "a) Xét các biến cố $A$: \"Số xuất hiện trên thẻ nhỏ hơn $15$\" và $B$: \"Số xuất hiện trên thẻ là số chia hết cho $5$\". Hãy cho biết biến cố nào là biến cố chắc chắn, biến cố nào là biến cố ngẫu nhiên.\n"
            "b) Tính xác suất của biến cố $A$ và biến cố $B$."
        ),
        "example_answer": (
            "a) Vì các số trên thẻ từ $1$ đến $12$ đều nhỏ hơn $15$ nên $A$ là biến cố chắc chắn. Biến cố $B$ có thể xảy ra (nếu rút được thẻ số $5$ hoặc $10$) hoặc không xảy ra, nên $B$ là biến cố ngẫu nhiên.\n"
            "b) Vì $A$ là biến cố chắc chắn nên $P(A) = 1$.\n"
            "Trong $12$ kết quả đồng khả năng ($1, 2, \\dots, 12$), có $2$ kết quả thuận lợi cho biến cố $B$ là $5$ và $10$. Do đó xác suất của biến cố $B$ là:\n"
            "$P(B) = \\frac{2}{12} = \\frac{1}{6}$."
        ),
        "real_life": "Xác suất của biến cố được sử dụng trong dự báo thời tiết (ví dụ khả năng mưa là $70\\%$), phân tích rủi ro trong bảo hiểm, kiểm định chất lượng sản phẩm trong dây chuyền sản xuất và các trò chơi bốc thăm trúng thưởng.",
        "quiz": [
            mcq("biet", "Gieo một con xúc xắc $6$ mặt cân đối. Biến cố nào sau đây là biến cố không thể?", ["Số chấm xuất hiện trên con xúc xắc bằng $7$", "Số chấm xuất hiện trên con xúc xắc là số chẵn", "Số chấm xuất hiện trên con xúc xắc nhỏ hơn $7$", "Số chấm xuất hiện trên con xúc xắc là số nguyên tố"], 0, "Con xúc xắc chỉ có các mặt từ $1$ đến $6$ chấm nên không bao giờ xuất hiện mặt $7$ chấm; đó là biến cố không thể."),
            mcq("biet", "Xác suất của một biến cố chắc chắn luôn bằng bao nhiêu?", ["$1$", "$0$", "$0,5$", "$100$"], 0, "Theo định nghĩa, xác suất của biến cố chắc chắn luôn bằng $1$ (hay $100\\%$)."),
            mcq("biet", "Tung một đồng xu cân đối và đồng chất một lần. Xác suất của biến cố \"Đồng xu xuất hiện mặt sấp (S)\" là:", ["$\\frac{1}{2}$", "$1$", "$0$", "$\\frac{1}{4}$"], 0, "Khi tung đồng xu cân đối có $2$ kết quả đồng khả năng là Sấp (S) và Ngửa (N), nên xác suất xuất hiện mặt Sấp là $\\frac{1}{2}$."),
            mcq("biet", "Gieo một con xúc xắc $6$ mặt cân đối và đồng chất một lần. Xác suất để xuất hiện mặt $6$ chấm là:", ["$\\frac{1}{6}$", "$\\frac{1}{2}$", "$\\frac{1}{3}$", "$1$"], 0, "Có $6$ kết quả đồng khả năng từ $1$ đến $6$ chấm, nên xác suất xuất hiện mặt $6$ chấm là $\\frac{1}{6}$."),
            mcq("hieu", "Gieo một con xúc xắc $6$ mặt cân đối và đồng chất. Xác suất của biến cố \"Số chấm xuất hiện là một số nguyên tố\" bằng:", ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{1}{6}$"], 0, "Trong các số từ $1$ đến $6$, các số nguyên tố là $2, 3, 5$ (có $3$ kết quả thuận lợi). Vậy xác suất là $\\frac{3}{6} = \\frac{1}{2}$."),
            mcq("hieu", "Một túi đựng $5$ viên bi màu đỏ, $3$ viên bi màu xanh và $2$ viên bi màu vàng có cùng kích thước và khối lượng. Lấy ngẫu nhiên một viên bi từ túi. Xác suất để lấy được viên bi màu xanh là:", ["$\\frac{3}{10}$", "$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{7}$"], 0, "Tổng số viên bi trong túi là $5 + 3 + 2 = 10$ viên, trong đó có $3$ viên bi màu xanh. Xác suất lấy được bi xanh là $\\frac{3}{10}$."),
            tf4("hieu", "Gieo một con xúc xắc $6$ mặt cân đối và đồng chất một lần. Xét tính đúng sai của các khẳng định sau:", ["a) Biến cố $A$: \"Số chấm xuất hiện là một số tự nhiên từ $1$ đến $6$\" là biến cố chắc chắn và có $P(A) = 1$.", "b) Biến cố $B$: \"Số chấm xuất hiện bằng $0$\" là biến cố không thể và có $P(B) = 0$.", "c) Biến cố $C$: \"Số chấm xuất hiện là ước của $6$\" có $4$ kết quả thuận lợi.", "d) Xác suất của biến cố $C$: \"Số chấm xuất hiện là ước của $6$\" bằng $\\frac{1}{2}$."], [True, True, True, False], "a), b) Đúng theo định nghĩa biến cố chắc chắn và biến cố không thể.\nc) Đúng vì các ước tự nhiên của $6$ từ $1$ đến $6$ là $1, 2, 3, 6$ (gồm $4$ kết quả thuận lợi).\nd) Sai vì $P(C) = \\frac{4}{6} = \\frac{2}{3} \\neq \\frac{1}{2}$."),
            tf4("hieu", "Một hộp có $10$ tấm thẻ cùng loại được đánh số từ $1$ đến $10$. Rút ngẫu nhiên một tấm thẻ từ trong hộp. Xét tính đúng sai của các khẳng định sau:", ["a) Có $10$ kết quả đồng khả năng đối với số xuất hiện trên thẻ được rút ra.", "b) Xác suất của biến cố \"Số trên thẻ là số lẻ\" bằng $0,5$.", "c) Xác suất của biến cố \"Số trên thẻ là số chính phương\" bằng $0,3$.", "d) Xác suất của biến cố \"Số trên thẻ chia hết cho $3$\" lớn hơn xác suất của biến cố \"Số trên thẻ là số chẵn\"."], [True, True, True, False], "a) Đúng vì $10$ thẻ cùng loại nên đồng khả năng.\nb) Đúng vì có $5$ số lẻ ($1, 3, 5, 7, 9$) nên xác suất là $\\frac{5}{10} = 0,5$.\nc) Đúng vì các số chính phương từ $1$ đến $10$ là $1, 4, 9$ (có $3$ số) nên xác suất là $\\frac{3}{10} = 0,3$.\nd) Sai vì chỉ có $3$ số chia hết cho $3$ ($3, 6, 9$, xác suất $0,3$) nhỏ hơn xác suất rút được số chẵn ($0,5$)."),
            mcq("vandung", "Một hộp có các quả bóng màu xanh và màu trắng cùng kích thước. Biết trong hộp có $12$ quả bóng màu xanh và xác suất lấy ngẫu nhiên được một quả bóng màu xanh là $\\frac{3}{8}$. Hỏi trong hộp có bao nhiêu quả bóng màu trắng?", ["$20$ quả", "$32$ quả", "$16$ quả", "$24$ quả"], 0, "Tổng số quả bóng trong hộp là $12 : \\frac{3}{8} = 32$ (quả). Số quả bóng màu trắng là $32 - 12 = 20$ (quả)."),
            short("vandung", "Rút ngẫu nhiên một tấm thẻ từ hộp gồm $20$ tấm thẻ cùng loại được đánh số từ $1$ đến $20$. Tính xác suất của biến cố \"Số xuất hiện trên thẻ là số chia hết cho $4$\" (viết kết quả dưới dạng số thập phân).", ["0,25", "0.25"], "Từ $1$ đến $20$ có $5$ số chia hết cho $4$ là $4, 8, 12, 16, 20$. Xác suất của biến cố là $\\frac{5}{20} = \\frac{1}{4} = 0,25$."),
        ],
    },
    {
        "topic": "l7-ch09-quan-he-giua-cac-yeu-to-trong-mot-tam-giac",
        "title": "Quan hệ giữa các yếu tố trong một tam giác",
        "icon": "📏",
        "description": "Quan hệ giữa góc và cạnh đối diện, quan hệ giữa đường vuông góc và đường xiên, bất đẳng thức tam giác và sự đồng quy của ba đường trung tuyến, ba đường phân giác, ba đường trung trực, ba đường cao trong một tam giác (Bài 31 - Bài 35, SGK Toán 7 Tập 2).",
        "requirements": [
            "Giải thích được quan hệ giữa góc và cạnh đối diện trong một tam giác (góc đối diện với cạnh lớn hơn là góc lớn hơn và ngược lại).",
            "Giải thích được quan hệ giữa đường vuông góc và đường xiên; nhận biết được khoảng cách từ một điểm đến một đường thẳng.",
            "Giải thích được quan hệ giữa ba cạnh của một tam giác (bất đẳng thức tam giác) và vận dụng để kiểm tra bộ ba đoạn thẳng có tạo thành tam giác hay không.",
            "Nhận biết được các đường đặc biệt trong tam giác: đường trung tuyến, đường phân giác, đường trung trực, đường cao.",
            "Giải thích được tính chất sự đồng quy của ba đường trung tuyến (trọng tâm), ba đường phân giác, ba đường trung trực và ba đường cao (trực tâm) trong một tam giác.",
        ],
        "definition": "Trong một tam giác, góc đối diện với cạnh lớn hơn là góc lớn hơn và ngược lại; tổng độ dài hai cạnh bất kì luôn lớn hơn độ dài cạnh còn lại. Trong một tam giác, ba đường trung tuyến đồng quy tại trọng tâm $G$, ba đường phân giác đồng quy tại điểm $I$ cách đều ba cạnh, ba đường trung trực đồng quy tại điểm $O$ cách đều ba đỉnh, và ba đường cao đồng quy tại trực tâm $H$.",
        "theory": (
            "### Bài 31. Quan hệ giữa góc và cạnh đối diện trong một tam giác (trang 59)\n"
            "- Trong một tam giác, góc đối diện với cạnh lớn hơn là góc lớn hơn; cạnh đối diện với góc lớn hơn là cạnh lớn hơn. Trong tam giác vuông, cạnh huyền là cạnh lớn nhất; trong tam giác tù, cạnh đối diện với góc tù là cạnh lớn nhất.\n"
            "### Bài 32. Quan hệ giữa đường vuông góc và đường xiên (trang 63)\n"
            "- Trong các đoạn thẳng nối từ một điểm ở ngoài một đường thẳng đến các điểm trên đường thẳng đó, đường vuông góc luôn ngắn hơn mọi đường xiên. Độ dài đoạn vuông góc $AH$ gọi là khoảng cách từ điểm $A$ đến đường thẳng $d$.\n"
            "### Bài 33. Quan hệ giữa ba cạnh của một tam giác (trang 67)\n"
            "- Trong một tam giác, độ dài của một cạnh bất kì luôn nhỏ hơn tổng độ dài hai cạnh còn lại và lớn hơn hiệu độ dài hai cạnh đó ($|b - c| < a < b + c$).\n"
            "### Bài 34. Sự đồng quy của ba trung tuyến, ba đường phân giác trong một tam giác (trang 71)\n"
            "- Ba đường trung tuyến của một tam giác cùng đi qua một điểm gọi là trọng tâm $G$; trọng tâm cách mỗi đỉnh một khoảng bằng $\\frac{2}{3}$ độ dài đường trung tuyến đi qua đỉnh ấy. Ba đường phân giác của một tam giác cùng đi qua một điểm $I$ và điểm này cách đều ba cạnh của tam giác.\n"
            "### Bài 35. Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác (trang 77)\n"
            "- Ba đường trung trực của một tam giác cùng đi qua một điểm $O$ và điểm này cách đều ba đỉnh của tam giác ($OA = OB = OC$). Ba đường cao của một tam giác cùng đi qua một điểm gọi là trực tâm $H$ của tam giác."
        ),
        "formulas": [
            G("Quan hệ cạnh - góc & Đường vuông góc - đường xiên", F("Quan hệ giữa cạnh và góc đối diện trong tam giác ABC", "$BC > AC > AB \\iff \\widehat{A} > \\widehat{B} > \\widehat{C}$"), F("Đường vuông góc AH và đường xiên AB đến đường thẳng d", "$AH \\perp d, B \\in d \\; (B \\neq H) \\implies AH < AB$"), F("Bất đẳng thức tam giác (với ba cạnh a, b, c)", "$|b - c| < a < b + c$")),
            G("Các đường đồng quy trong tam giác", F("Tính chất trọng tâm G (với trung tuyến AM, BN, CP)", "$\\frac{AG}{AM} = \\frac{BG}{BN} = \\frac{CG}{CP} = \\frac{2}{3}, \\quad GM = \\frac{1}{3}AM, \\quad AG = 2GM$"), F("Giao điểm O của ba đường trung trực", "$OA = OB = OC$"), F("Giao điểm I của ba đường phân giác", "$d(I, AB) = d(I, BC) = d(I, CA)$")),
        ],
        "example": (
            "Cho tam giác $ABC$ có hai cạnh $AB = 4\\text{ cm}, BC = 9\\text{ cm}$ và độ dài cạnh $AC$ là một số nguyên tố (tính theo cm).\n"
            "a) Tìm độ dài cạnh $AC$ và so sánh các góc của tam giác $ABC$.\n"
            "b) Gọi $AM$ là đường trung tuyến của tam giác $ABC$ và $G$ là trọng tâm. Biết $AM = 7,5\\text{ cm}$, tính độ dài $AG$ và $GM$."
        ),
        "example_answer": (
            "a) Theo bất đẳng thức tam giác trong $\\triangle ABC$, ta có:\n"
            "$BC - AB < AC < BC + AB \\Rightarrow 9 - 4 < AC < 9 + 4 \\Rightarrow 5 < AC < 13$.\n"
            "Vì độ dài $AC$ là một số nguyên tố nằm giữa $5$ và $13$ nên $AC \\in \\{7; 11\\}\\text{ (cm)}$.\n"
            "- Nếu $AC = 7\\text{ cm}$ thì $AB < AC < BC$ ($4 < 7 < 9$) nên $\\widehat{C} < \\widehat{B} < \\widehat{A}$.\n"
            "- Nếu $AC = 11\\text{ cm}$ thì $AB < BC < AC$ ($4 < 9 < 11$) nên $\\widehat{C} < \\widehat{A} < \\widehat{B}$.\n"
            "b) Vì $G$ là trọng tâm của $\\triangle ABC$ và $AM$ là đường trung tuyến nên:\n"
            "$AG = \\frac{2}{3}AM = \\frac{2}{3} \\cdot 7,5 = 5\\text{ (cm)}$ và $GM = \\frac{1}{3}AM = 2,5\\text{ (cm)}$."
        ),
        "real_life": "Các tính chất đồng quy trong tam giác giúp xác định vị trí đặt trạm phát sóng hoặc giếng nước cách đều ba ngôi làng (giao điểm ba đường trung trực), hoặc đặt bồn hoa tròn cách đều ba con đường bao quanh một công viên hình tam giác (giao điểm ba đường phân giác).",
        "quiz": [
            mcq("biet", "Cho tam giác $ABC$ có $AB = 5\\text{ cm}, BC = 8\\text{ cm}, AC = 7\\text{ cm}$. Khẳng định nào sau đây đúng khi so sánh các góc của tam giác $ABC$?", ["$\\widehat{C} < \\widehat{B} < \\widehat{A}$", "$\\widehat{A} < \\widehat{B} < \\widehat{C}$", "$\\widehat{B} < \\widehat{C} < \\widehat{A}$", "$\\widehat{C} < \\widehat{A} < \\widehat{B}$"], 0, "Ta có $AB < AC < BC$ ($5 < 7 < 8$). Góc đối diện với cạnh lớn hơn là góc lớn hơn nên $\\widehat{C} < \\widehat{B} < \\widehat{A}$."),
            mcq("biet", "Bộ ba độ dài đoạn thẳng nào dưới đây có thể là độ dài ba cạnh của một tam giác?", ["$4\\text{ cm}; 5\\text{ cm}; 6\\text{ cm}$", "$2\\text{ cm}; 3\\text{ cm}; 5\\text{ cm}$", "$3\\text{ cm}; 4\\text{ cm}; 8\\text{ cm}$", "$1\\text{ cm}; 2\\text{ cm}; 4\\text{ cm}$"], 0, "Chỉ có bộ $4\\text{ cm}; 5\\text{ cm}; 6\\text{ cm}$ thỏa mãn bất đẳng thức tam giác vì $4 + 5 = 9 > 6$. Các bộ còn lại đều có tổng hai cạnh nhỏ hơn hoặc bằng cạnh lớn nhất."),
            mcq("biet", "Trong một tam giác, giao điểm của ba đường trung tuyến được gọi là gì?", ["Trọng tâm của tam giác", "Trực tâm của tam giác", "Tâm đường tròn ngoại tiếp tam giác", "Tâm đường tròn nội tiếp tam giác"], 0, "Giao điểm của ba đường trung tuyến trong một tam giác được gọi là trọng tâm của tam giác đó."),
            mcq("biet", "Điểm cách đều ba đỉnh của một tam giác là giao điểm của ba đường nào trong tam giác đó?", ["Ba đường trung trực", "Ba đường phân giác", "Ba đường trung tuyến", "Ba đường cao"], 0, "Ba đường trung trực của một tam giác đồng quy tại một điểm cách đều ba đỉnh của tam giác."),
            mcq("hieu", "Cho tam giác $ABC$ có đường trung tuyến $AM = 12\\text{ cm}$ và trọng tâm $G$. Độ dài đoạn thẳng $AG$ bằng:", ["$8\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$", "$9\\text{ cm}$"], 0, "Theo tính chất trọng tâm của tam giác, $AG = \\frac{2}{3}AM = \\frac{2}{3} \\cdot 12 = 8\\text{ cm}$."),
            mcq("hieu", "Một tam giác cân có độ dài hai cạnh là $3\\text{ cm}$ và $7\\text{ cm}$. Chu vi của tam giác cân đó bằng bao nhiêu?", ["$17\\text{ cm}$", "$13\\text{ cm}$", "$10\\text{ cm}$", "$13\\text{ cm}$ hoặc $17\\text{ cm}$"], 0, "Cạnh bên của tam giác cân phải là $7\\text{ cm}$ (vì nếu cạnh bên là $3\\text{ cm}$ thì $3 + 3 = 6 < 7$, không thỏa mãn bất đẳng thức tam giác). Vậy ba cạnh là $7\\text{ cm}, 7\\text{ cm}, 3\\text{ cm}$ và chu vi là $7 + 7 + 3 = 17\\text{ cm}$."),
            tf4("hieu", "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ, \\widehat{B} = 60^\\circ$. Kẻ $AH \\perp BC$ tại $H$. Xét tính đúng sai của các khẳng định sau:", ["a) Số đo góc $\\widehat{C}$ bằng $40^\\circ$.", "b) Cạnh lớn nhất của tam giác $ABC$ là cạnh $BC$.", "c) Cạnh nhỏ nhất của tam giác $ABC$ là cạnh $AC$.", "d) Đoạn vuông góc $AH$ luôn nhỏ hơn cả hai cạnh bên $AB$ và $AC$."], [True, True, False, True], "a) Đúng vì $\\widehat{C} = 180^\\circ - (80^\\circ + 60^\\circ) = 40^\\circ$.\nb) Đúng vì góc $\\widehat{A} = 80^\\circ$ lớn nhất nên cạnh đối diện $BC$ là cạnh lớn nhất.\nc) Sai vì góc $\\widehat{C} = 40^\\circ$ nhỏ nhất nên cạnh đối diện $AB$ mới là cạnh nhỏ nhất (không phải $AC$).\nd) Đúng vì $AH$ là đường vuông góc còn $AB, AC$ là các đường xiên kẻ từ $A$ đến đường thẳng $BC$."),
            tf4("hieu", "Cho tam giác $ABC$. Gọi $G$ là giao điểm ba đường trung tuyến, $I$ là giao điểm ba đường phân giác, $O$ là giao điểm ba đường trung trực và $H$ là giao điểm ba đường cao. Xét các khẳng định sau:", ["a) Điểm $I$ luôn nằm bên trong tam giác $ABC$ và cách đều ba cạnh $AB, BC, CA$.", "b) Điểm $O$ cách đều ba đỉnh của tam giác, tức là $OA = OB = OC$.", "c) Nếu $AM$ là đường trung tuyến của tam giác $ABC$ thì $AG = 3GM$.", "d) Nếu tam giác $ABC$ là tam giác đều thì bốn điểm $G, I, O, H$ trùng nhau."], [True, True, False, True], "a) Đúng theo tính chất giao điểm ba đường phân giác.\nb) Đúng theo tính chất giao điểm ba đường trung trực.\nc) Sai vì $AG = \\frac{2}{3}AM$ và $GM = \\frac{1}{3}AM$ nên $AG = 2GM$ ($\\neq 3GM$).\nd) Đúng vì trong tam giác đều, đường trung tuyến xuất phát từ mỗi đỉnh đồng thời là đường phân giác, đường trung trực và đường cao."),
            mcq("vandung", "Cho tam giác $ABC$ có hai đường phân giác của góc $\\widehat{B}$ và góc $\\widehat{C}$ cắt nhau tại $I$. Biết $\\widehat{BIC} = 125^\\circ$, số đo góc $\\widehat{BAC}$ bằng bao nhiêu độ?", ["$70^\\circ$", "$55^\\circ$", "$65^\\circ$", "$50^\\circ$"], 0, "Trong $\\triangle IBC$, ta có $\\widehat{IBC} + \\widehat{ICB} = 180^\\circ - 125^\\circ = 55^\\circ$. Vì $BI, CI$ là các tia phân giác nên $\\widehat{ABC} + \\widehat{ACB} = 2(\\widehat{IBC} + \\widehat{ICB}) = 2 \\cdot 55^\\circ = 110^\\circ$. Vậy $\\widehat{BAC} = 180^\\circ - 110^\\circ = 70^\\circ$."),
            short("vandung", "Cho tam giác $ABC$ có trọng tâm $G$, đường trung tuyến $BM$. Biết đoạn thẳng $GM = 4,5\\text{ cm}$. Tính độ dài đường trung tuyến $BM$ (đơn vị: cm).", ["13,5", "13.5"], "Vì $G$ là trọng tâm của $\\triangle ABC$ nên $GM = \\frac{1}{3}BM \\Rightarrow BM = 3 \\cdot GM = 3 \\cdot 4,5 = 13,5\\text{ (cm)}$."),
        ],
    },
    {
        "topic": "l7-ch10-mot-so-hinh-khoi-trong-thuc-tien",
        "title": "Một số hình khối trong thực tiễn",
        "icon": "📦",
        "description": "Các yếu tố đỉnh, cạnh, mặt, diện tích xung quanh và thể tích của hình hộp chữ nhật, hình lập phương, hình lăng trụ đứng tam giác và hình lăng trụ đứng tứ giác (Bài 36 - Bài 37, SGK Toán 7 Tập 2).",
        "requirements": [
            "Mô tả được một số yếu tố cơ bản (đỉnh, cạnh, góc, đường chéo, mặt đáy, mặt bên) của hình hộp chữ nhật và hình lập phương.",
            "Giải quyết được một số vấn đề thực tiễn gắn với việc tính thể tích, diện tích xung quanh của hình hộp chữ nhật và hình lập phương.",
            "Mô tả và tạo lập được hình lăng trụ đứng tam giác và hình lăng trụ đứng tứ giác.",
            "Tính được diện tích xung quanh và thể tích của hình lăng trụ đứng tam giác, hình lăng trụ đứng tứ giác và vận dụng giải các bài toán thực tiễn.",
        ],
        "definition": "Hình hộp chữ nhật có $6$ mặt là các hình chữ nhật, $8$ đỉnh, $12$ cạnh và $4$ đường chéo; hình lập phương là hình hộp chữ nhật có $6$ mặt là các hình vuông bằng nhau. Hình lăng trụ đứng tam giác (hoặc tứ giác) có hai mặt đáy song song là hai tam giác (hoặc tứ giác) bằng nhau và các mặt bên là các hình chữ nhật.",
        "theory": (
            "### Bài 36. Hình hộp chữ nhật và hình lập phương (trang 85)\n"
            "- Hình hộp chữ nhật có $6$ mặt (hai mặt đáy và bốn mặt bên đều là hình chữ nhật), $8$ đỉnh, $12$ cạnh, $4$ đường chéo cắt nhau tại trung điểm của mỗi đường. Với ba kích thước chiều dài $a$, chiều rộng $b$, chiều cao $c$: diện tích xung quanh $S_{xq} = 2(a+b)c$ và thể tích $V = abc$. Hình lập phương cạnh $d$ có $S_{xq} = 4d^2$, diện tích toàn phần $S_{tp} = 6d^2$ và thể tích $V = d^3$.\n"
            "### Bài 37. Hình lăng trụ đứng tam giác và hình lăng trụ đứng tứ giác (trang 93)\n"
            "- Hình lăng trụ đứng tam giác (hoặc tứ giác) có hai mặt đáy song song với nhau, các mặt bên là những hình chữ nhật, các cạnh bên song song và bằng nhau; độ dài một cạnh bên được gọi là chiều cao $h$ của hình lăng trụ đứng. Diện tích xung quanh bằng chu vi đáy nhân với chiều cao ($S_{xq} = C_{\\text{đáy}} \\cdot h$); thể tích bằng diện tích đáy nhân với chiều cao ($V = S_{\\text{đáy}} \\cdot h$). Chú ý: Hình hộp chữ nhật và hình lập phương chính là những hình lăng trụ đứng tứ giác đặc biệt."
        ),
        "formulas": [
            G("Hình hộp chữ nhật & Hình lập phương", F("Diện tích xung quanh và thể tích Hình hộp chữ nhật (kích thước a, b, c)", "$S_{xq} = 2(a + b)c, \\qquad V = a \\cdot b \\cdot c$"), F("Diện tích toàn phần Hình hộp chữ nhật", "$S_{tp} = S_{xq} + 2S_{\\text{đáy}} = 2(a + b)c + 2ab$"), F("Diện tích xung quanh, toàn phần và thể tích Hình lập phương cạnh d", "$S_{xq} = 4d^2, \\qquad S_{tp} = 6d^2, \\qquad V = d^3$")),
            G("Hình lăng trụ đứng tam giác & Hình lăng trụ đứng tứ giác", F("Diện tích xung quanh Hình lăng trụ đứng", "$S_{xq} = C_{\\text{đáy}} \\cdot h \\quad (C_{\\text{đáy}} \\text{ là chu vi đáy}, h \\text{ là chiều cao})$"), F("Diện tích toàn phần Hình lăng trụ đứng", "$S_{tp} = S_{xq} + 2S_{\\text{đáy}}$"), F("Thể tích Hình lăng trụ đứng", "$V = S_{\\text{đáy}} \\cdot h \\quad (S_{\\text{đáy}} \\text{ là diện tích đáy}, h \\text{ là chiều cao})$")),
        ],
        "example": (
            "Một chiếc lều cắm trại có dạng hình lăng trụ đứng tam giác $ABC.A'B'C'$, trong đó hai mặt đáy $ABC$ và $A'B'C'$ là hai tam giác cân có cạnh đáy $BC = 2,4\\text{ m}$, hai cạnh bên $AB = AC = 1,5\\text{ m}$, chiều cao của tam giác đáy kẻ từ đỉnh $A$ xuống $BC$ là $0,9\\text{ m}$. Chiều dài chiếc lều (cạnh bên $AA'$) là $3\\text{ m}$.\n"
            "a) Tính diện tích vải bạt cần dùng để làm hai mái bên $ABB'A'$ và $ACC'A'$ của lều (không tính mặt sàn $BCC'B'$).\n"
            "b) Tính thể tích không gian bên trong chiếc lều."
        ),
        "example_answer": (
            "a) Hai mái bên $ABB'A'$ và $ACC'A'$ là hai hình chữ nhật có chiều rộng $AB = AC = 1,5\\text{ m}$ và chiều dài $AA' = 3\\text{ m}$.\n"
            "Diện tích vải bạt làm hai mái bên là:\n"
            "$S = (1,5 + 1,5) \\cdot 3 = 3 \\cdot 3 = 9\\text{ (m}^2\\text{)}$.\n"
            "b) Diện tích mặt đáy tam giác $ABC$ là:\n"
            "$S_{\\text{đáy}} = \\frac{1}{2} \\cdot 2,4 \\cdot 0,9 = 1,08\\text{ (m}^2\\text{)}$.\n"
            "Thể tích không gian bên trong chiếc lều là:\n"
            "$V = S_{\\text{đáy}} \\cdot h = 1,08 \\cdot 3 = 3,24\\text{ (m}^3\\text{)}$."
        ),
        "real_life": "Công thức diện tích xung quanh và thể tích hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng được dùng để tính diện tích sơn tường căn phòng, tính lượng nước chứa trong bể bơi, làm hộp quà, thùng carton hoặc lều bạt dã ngoại.",
        "quiz": [
            mcq("biet", "Một hình hộp chữ nhật có bao nhiêu đỉnh và bao nhiêu cạnh?", ["$8$ đỉnh và $12$ cạnh", "$6$ đỉnh và $12$ cạnh", "$8$ đỉnh và $6$ cạnh", "$12$ đỉnh và $8$ cạnh"], 0, "Mọi hình hộp chữ nhật (và hình lập phương) đều có $6$ mặt, $8$ đỉnh, $12$ cạnh và $4$ đường chéo."),
            mcq("biet", "Cho hình lập phương có độ dài cạnh bằng $d$. Công thức tính diện tích xung quanh $S_{xq}$ và thể tích $V$ của hình lập phương đó là:", ["$S_{xq} = 4d^2$ và $V = d^3$", "$S_{xq} = 6d^2$ và $V = d^3$", "$S_{xq} = 4d^2$ và $V = 3d^2$", "$S_{xq} = 4d$ và $V = d^3$"], 0, "Hình lập phương cạnh $d$ có $4$ mặt bên là các hình vuông diện tích $d^2$ nên $S_{xq} = 4d^2$, và thể tích $V = d^3$."),
            mcq("biet", "Các mặt bên của một hình lăng trụ đứng tam giác là hình gì?", ["Hình chữ nhật", "Hình tam giác", "Hình thang cân", "Hình thoi"], 0, "Theo tính chất của hình lăng trụ đứng tam giác, hai mặt đáy là hai tam giác bằng nhau và $3$ mặt bên đều là các hình chữ nhật."),
            mcq("biet", "Một hình lăng trụ đứng có chu vi đáy là $C_{\\text{đáy}}$, diện tích đáy là $S_{\\text{đáy}}$ và chiều cao là $h$. Công thức tính thể tích $V$ của hình lăng trụ đứng đó là:", ["$V = S_{\\text{đáy}} \\cdot h$", "$V = C_{\\text{đáy}} \\cdot h$", "$V = \\frac{1}{3} S_{\\text{đáy}} \\cdot h$", "$V = 2 S_{\\text{đáy}} \\cdot h$"], 0, "Thể tích của hình lăng trụ đứng bằng diện tích đáy nhân với chiều cao: $V = S_{\\text{đáy}} \\cdot h$."),
            mcq("hieu", "Một hình hộp chữ nhật có chiều dài $6\\text{ cm}$, chiều rộng $4\\text{ cm}$ và chiều cao $5\\text{ cm}$. Diện tích xung quanh của hình hộp chữ nhật đó bằng:", ["$100\\text{ cm}^2$", "$120\\text{ cm}^2$", "$148\\text{ cm}^2$", "$50\\text{ cm}^2$"], 0, "Ta có $S_{xq} = 2(a + b)c = 2 \\cdot (6 + 4) \\cdot 5 = 100\\text{ (cm}^2\\text{)}$."),
            mcq("hieu", "Một hình lăng trụ đứng tam giác có đáy là tam giác vuông với hai cạnh góc vuông lần lượt là $3\\text{ cm}$ và $4\\text{ cm}$, chiều cao của hình lăng trụ là $10\\text{ cm}$. Thể tích của hình lăng trụ đứng đó là:", ["$60\\text{ cm}^3$", "$120\\text{ cm}^3$", "$70\\text{ cm}^3$", "$30\\text{ cm}^3$"], 0, "Diện tích đáy tam giác vuông là $S_{\\text{đáy}} = \\frac{1}{2} \\cdot 3 \\cdot 4 = 6\\text{ (cm}^2\\text{)}$. Thể tích lăng trụ là $V = S_{\\text{đáy}} \\cdot h = 6 \\cdot 10 = 60\\text{ (cm}^3\\text{)}$."),
            tf4("hieu", "Cho một hình lập phương có độ dài cạnh bằng $5\\text{ cm}$. Xét tính đúng sai của các khẳng định sau:", ["a) Hình lập phương có $4$ đường chéo bằng nhau.", "b) Diện tích một mặt của hình lập phương là $25\\text{ cm}^2$.", "c) Diện tích xung quanh của hình lập phương là $150\\text{ cm}^2$.", "d) Thể tích của hình lập phương là $125\\text{ cm}^3$."], [True, True, False, True], "a) Đúng theo tính chất hình lập phương.\nb) Đúng vì mỗi mặt là hình vuông cạnh $5\\text{ cm}$ nên diện tích là $5^2 = 25\\text{ cm}^2$.\nc) Sai vì $S_{xq} = 4d^2 = 4 \\cdot 25 = 100\\text{ cm}^2$ (còn $150\\text{ cm}^2$ là diện tích toàn phần $6d^2$).\nd) Đúng vì $V = d^3 = 5^3 = 125\\text{ cm}^3$."),
            tf4("hieu", "Cho hình lăng trụ đứng tam giác $ABC.A'B'C'$ có đáy $ABC$ là tam giác với $AB = 5\\text{ cm}, BC = 6\\text{ cm}, CA = 7\\text{ cm}$ và cạnh bên $AA' = 8\\text{ cm}$. Xét các khẳng định sau:", ["a) Hình lăng trụ đứng tam giác $ABC.A'B'C'$ có $6$ đỉnh, $9$ cạnh và $5$ mặt.", "b) Các cạnh bên thỏa mãn $AA' = BB' = CC' = 8\\text{ cm}$.", "c) Chu vi đáy của hình lăng trụ đứng là $18\\text{ cm}$.", "d) Diện tích xung quanh của hình lăng trụ đứng là $120\\text{ cm}^2$."], [True, True, True, False], "a), b) Đúng theo cấu tạo và tính chất của hình lăng trụ đứng tam giác.\nc) Đúng vì $C_{\\text{đáy}} = 5 + 6 + 7 = 18\\text{ (cm)}$.\nd) Sai vì $S_{xq} = C_{\\text{đáy}} \\cdot h = 18 \\cdot 8 = 144\\text{ cm}^2 \\neq 120\\text{ cm}^2$."),
            mcq("vandung", "Một căn phòng hình hộp chữ nhật có chiều dài $8\\text{ m}$, chiều rộng $5\\text{ m}$ và chiều cao $4\\text{ m}$. Người ta muốn lăn sơn bốn bức tường bên trong và trần nhà. Biết tổng diện tích các cửa ra vào và cửa sổ là $12\\text{ m}^2$, diện tích phần cần lăn sơn là:", ["$132\\text{ m}^2$", "$144\\text{ m}^2$", "$172\\text{ m}^2$", "$92\\text{ m}^2$"], 0, "Diện tích $4$ bức tường xung quanh là $S_{xq} = 2 \\cdot (8 + 5) \\cdot 4 = 104\\text{ (m}^2\\text{)}$. Diện tích trần nhà là $8 \\cdot 5 = 40\\text{ (m}^2\\text{)}$. Diện tích cần lăn sơn (trừ diện tích cửa) là $104 + 40 - 12 = 132\\text{ (m}^2\\text{)}$."),
            short("vandung", "Một bể cá dạng hình hộp chữ nhật có chiều dài $80\\text{ cm}$, chiều rộng $40\\text{ cm}$ và chiều cao $50\\text{ cm}$. Hiện tại mực nước trong bể cao bằng $\\frac{3}{4}$ chiều cao của bể. Hỏi trong bể đang chứa bao nhiêu lít nước (biết $1\\text{ lít} = 1\\text{ dm}^3 = 1000\\text{ cm}^3$)?", ["120"], "Đổi kích thước ra đêximét: dài $8\\text{ dm}$, rộng $4\\text{ dm}$, cao $5\\text{ dm}$. Thể tích toàn bộ bể là $8 \\cdot 4 \\cdot 5 = 160\\text{ (dm}^3\\text{)}$. Thể tích nước trong bể là $160 \\cdot \\frac{3}{4} = 120\\text{ (lít)}$."),
        ],
    },
]
