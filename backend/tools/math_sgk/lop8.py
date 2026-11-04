"""TOÁN 8 — Kết nối tri thức với cuộc sống (tập một, tập hai).

10 chương đánh số (I – X) đúng thứ tự mục lục SGK.
Mỗi chương: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 8

LESSONS = [
    {
        "topic": "l8-ch01-da-thuc",
        "title": "Đa thức",
        "icon": "🧮",
        "description": "Đơn thức, đa thức nhiều biến và các phép toán cộng, trừ, nhân, chia đa thức",
        "requirements": [
            "Nhận biết được đơn thức, đơn thức thu gọn, hệ số, phần biến và bậc của đơn thức; nhận biết các đơn thức đồng dạng.",
            "Thực hiện được việc thu gọn đơn thức và cộng, trừ các đơn thức đồng dạng.",
            "Nhận biết được các khái niệm về đa thức nhiều biến, hạng tử, đa thức thu gọn và bậc của đa thức.",
            "Tính được giá trị của đa thức khi biết giá trị của các biến.",
            "Thực hiện được các phép tính: phép cộng, phép trừ, phép nhân các đa thức nhiều biến trong những trường hợp đơn giản.",
            "Thực hiện được phép chia hết một đa thức cho một đơn thức trong những trường hợp đơn giản.",
        ],
        "definition": "Đơn thức là biểu thức đại số chỉ gồm một số, hoặc một biến, hoặc một tích giữa các số và các biến. Đa thức là một tổng của những đơn thức, trong đó mỗi đơn thức trong tổng gọi là một hạng tử của đa thức đó.",
        "theory": (
            "### Bài 1. Đơn thức\n"
            "- Đơn thức thu gọn là đơn thức chỉ gồm tích của một số với các biến mà mỗi biến đã được nâng lên lũy thừa với số mũ nguyên dương. Bậc của đơn thức có hệ số khác $0$ là tổng số mũ của tất cả các biến trong đơn thức đó. Hai đơn thức đồng dạng là hai đơn thức với hệ số khác $0$ và có cùng phần biến.\n"
            "### Bài 2. Đa thức\n"
            "- Đa thức thu gọn là đa thức không có hai hạng tử nào đồng dạng. Bậc của một đa thức là bậc của hạng tử có bậc cao nhất trong dạng thu gọn của đa thức đó (số $0$ là đa thức không có bậc).\n"
            "### Bài 3. Phép cộng và phép trừ đa thức\n"
            "- Để cộng (hay trừ) hai đa thức, ta nối hai đa thức bằng dấu $+$ (hay dấu $-$) rồi bỏ dấu ngoặc theo quy tắc dấu ngoặc và thu gọn các hạng tử đồng dạng.\n"
            "### Bài 4. Phép nhân đa thức\n"
            "- Muốn nhân hai đơn thức, ta nhân hai hệ số với nhau và nhân hai phần biến với nhau. Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích với nhau. Muốn nhân một đa thức với một đa thức, ta nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.\n"
            "### Bài 5. Phép chia đa thức cho đơn thức\n"
            "- Đơn thức $A$ chia hết cho đơn thức $B$ ($B \\neq 0$) khi mỗi biến của $B$ đều là biến của $A$ với số mũ không lớn hơn số mũ của nó trong $A$. Đa thức $A$ chia hết cho đơn thức $B$ nếu mọi hạng tử của $A$ đều chia hết cho $B$; ta chia từng hạng tử của $A$ cho $B$ rồi cộng các kết quả lại."
        ),
        "formulas": [
            G("Đơn thức và đơn thức đồng dạng", F("Bậc của đơn thức $a x^m y^n z^p$ ($a \\neq 0$)", "$d = m + n + p$"), F("Cộng, trừ hai đơn thức đồng dạng", "$a x^m y^n \\pm b x^m y^n = (a \\pm b) x^m y^n$"), F("Nhân hai đơn thức", "$(a x^m y^n) \\cdot (b x^p y^q) = (ab) x^{m+p} y^{n+q}$")),
            G("Các phép toán với đa thức", F("Nhân đơn thức với đa thức", "$A \\cdot (B + C) = A \\cdot B + A \\cdot C$"), F("Nhân hai đa thức", "$(A + B)(C + D) = A \\cdot C + A \\cdot D + B \\cdot C + B \\cdot D$"), F("Chia đơn thức cho đơn thức ($m \\ge p, n \\ge q, b \\neq 0$)", "$(a x^m y^n) : (b x^p y^q) = \\frac{a}{b} x^{m-p} y^{n-q}$"), F("Chia đa thức cho đơn thức", "$(A + B - C) : D = (A : D) + (B : D) - (C : D)$")),
        ],
        "example": "Cho hai đa thức $P = 3x^2y - 2xy^2 + 5$ và $Q = -x^2y + 2xy^2 - 1$. Tính tổng $M = P + Q$, tìm bậc của $M$ và tính giá trị của $M$ tại $x = -2, y = 3$.",
        "example_answer": "Ta có $M = P + Q = (3x^2y - 2xy^2 + 5) + (-x^2y + 2xy^2 - 1) = (3 - 1)x^2y + (-2 + 2)xy^2 + (5 - 1) = 2x^2y + 4$. Hạng tử $2x^2y$ có bậc $2 + 1 = 3$, hạng tử $4$ có bậc $0$, nên bậc của đa thức $M$ là $3$. Tại $x = -2, y = 3$, giá trị của $M$ là $M = 2 \\cdot (-2)^2 \\cdot 3 + 4 = 2 \\cdot 4 \\cdot 3 + 4 = 28$.",
        "real_life": "Biểu thức đa thức nhiều biến được sử dụng để lập công thức tổng diện tích bề mặt vật liệu đóng gói, tính tổng doanh thu từ nhiều mặt hàng có đơn giá và số lượng khác nhau hoặc mô hình hóa chi phí sản xuất.",
        "quiz": [
            mcq("biet", "Biểu thức nào sau đây là một đơn thức?", ["$3x^2y + 1$", "$-5x^3y^2$", "$\\frac{2x}{y}$", "$x^2 - y^2$"], 1, "Đơn thức chỉ gồm một số, một biến hoặc một tích giữa các số và các biến nên $-5x^3y^2$ là đơn thức."),
            mcq("biet", "Bậc của đơn thức $-7x^3y^4z$ là bao nhiêu?", ["$7$", "$8$", "$12$", "$-7$"], 1, "Tổng số mũ của các biến $x, y, z$ trong đơn thức $-7x^3y^4z$ là $3 + 4 + 1 = 8$."),
            mcq("biet", "Đơn thức nào dưới đây đồng dạng với đơn thức $4x^2y^3$?", ["$4x^3y^2$", "$-\\frac{1}{2}x^2y^3$", "$4x^2y$", "$0x^2y^3$"], 1, "Hai đơn thức đồng dạng có hệ số khác $0$ và cùng phần biến $x^2y^3$, nên $-\\frac{1}{2}x^2y^3$ đồng dạng với $4x^2y^3$."),
            mcq("biet", "Sau khi thu gọn, đa thức $A = 5x^2y - 3xy + 2x^2y + 3xy - 1$ có bậc là bao nhiêu?", ["$2$", "$3$", "$4$", "$1$"], 1, "Thu gọn $A = (5 + 2)x^2y + (-3 + 3)xy - 1 = 7x^2y - 1$. Hạng tử $7x^2y$ có bậc $2 + 1 = 3$ nên bậc của $A$ là $3$."),
            mcq("hieu", "Kết quả của phép nhân $(2x - y)(x^2 + xy)$ sau khi thu gọn là đa thức nào?", ["$2x^3 + x^2y - xy^2$", "$2x^3 - x^2y - xy^2$", "$2x^3 + 3x^2y - xy^2$", "$2x^3 - xy^2$"], 0, "Ta có $(2x - y)(x^2 + xy) = 2x^3 + 2x^2y - x^2y - xy^2 = 2x^3 + x^2y - xy^2$."),
            mcq("hieu", "Thương của phép chia $(12x^4y^3 - 8x^3y^2 + 4x^2y^2) : (4x^2y^2)$ là đa thức nào?", ["$3x^2y - 2x + 1$", "$3x^2y - 2x$", "$3xy^2 - 2x + 1$", "$8x^2y - 4x + 1$"], 0, "Chia từng hạng tử cho $4x^2y^2$, ta được $3x^2y - 2x + 1$."),
            tf4("hieu", "Cho hai đa thức $A = 4x^2y - 3xy^2 + 2xy$ và $B = -4x^2y + 5xy^2 + xy - 6$. Xét tính đúng sai của các khẳng định sau:", ["a) Đa thức $A$ là đa thức thu gọn và có bậc bằng $3$.", "b) Tổng hai đa thức là $A + B = 2xy^2 + 3xy - 6$.", "c) Hiệu hai đa thức là $A - B = -8xy^2 + xy + 6$.", "d) Giá trị của đa thức $A + B$ tại $x = 1, y = 2$ là $8$."], [True, True, False, True], "a) Đúng vì các hạng tử của $A$ không đồng dạng và bậc cao nhất là $2 + 1 = 3$. b) Đúng vì $A + B = (4 - 4)x^2y + (-3 + 5)xy^2 + (2 + 1)xy - 6 = 2xy^2 + 3xy - 6$. c) Sai vì $A - B = 8x^2y - 8xy^2 + xy + 6$. d) Đúng vì thay $x = 1, y = 2$ vào $A + B$ ta được $2 \\cdot 1 \\cdot 2^2 + 3 \\cdot 1 \\cdot 2 - 6 = 8 + 6 - 6 = 8$."),
            tf4("hieu", "Cho biểu thức $P = (6x^3y^2 - 9x^2y^3) : (3x^2y^2) - (2x - 3y) + 5$. Xét tính đúng sai của các khẳng định sau:", ["a) Thương của phép chia $(6x^3y^2 - 9x^2y^3) : (3x^2y^2)$ là $2x - 3y$.", "b) Sau khi rút gọn, biểu thức $P$ có giá trị không phụ thuộc vào biến $x$ và $y$.", "c) Bậc của đa thức $P$ sau khi thu gọn bằng $1$.", "d) Tại $x = 2026, y = -2027$, giá trị của $P$ bằng $5$."], [True, True, False, True], "a) Đúng vì $(6x^3y^2) : (3x^2y^2) - (9x^2y^3) : (3x^2y^2) = 2x - 3y$. b) Đúng vì $P = (2x - 3y) - (2x - 3y) + 5 = 5$. c) Sai vì $P = 5$ là đa thức bậc $0$. d) Đúng vì $P = 5$ với mọi $x \\neq 0, y \\neq 0$."),
            mcq("vandung", "Một mảnh vườn hình chữ nhật có chiều dài $2x + 3y$ (m) và chiều rộng $2x - y$ (m). Người ta đào một cái ao hình vuông có cạnh $x + y$ (m) ở bên trong mảnh vườn ($x > y > 0$). Biểu thức biểu thị diện tích phần đất còn lại của mảnh vườn là:", ["$3x^2 + 2xy - 4y^2$", "$3x^2 + 6xy - 2y^2$", "$4x^2 + 4xy - 3y^2$", "$3x^2 - 2xy - 4y^2$"], 0, "Diện tích mảnh vườn là $(2x + 3y)(2x - y) = 4x^2 - 2xy + 6xy - 3y^2 = 4x^2 + 4xy - 3y^2$. Diện tích ao là $(x + y)(x + y) = x^2 + 2xy + y^2$. Diện tích còn lại là $(4x^2 + 4xy - 3y^2) - (x^2 + 2xy + y^2) = 3x^2 + 2xy - 4y^2$."),
            short("vandung", "Cho biểu thức $Q = 3x(2x - 5y) + (15xy^2 - 6x^2y) : y + 12$ (với $y \\neq 0$). Tính giá trị của $Q$ tại $x = -15, y = 2026$.", ["12"], "Ta có $Q = 6x^2 - 15xy + 15xy - 6x^2 + 12 = 12$. Vậy tại $x = -15, y = 2026$, giá trị của $Q$ bằng $12$."),
        ],
    },
    {
        "topic": "l8-ch02-hang-dang-thuc-dang-nho-va-ung-dung",
        "title": "Hằng đẳng thức đáng nhớ và ứng dụng",
        "icon": "✨",
        "description": "Bảy hằng đẳng thức đáng nhớ và các phương pháp phân tích đa thức thành nhân tử",
        "requirements": [
            "Nhận biết được khái niệm đồng nhất thức (hằng đẳng thức).",
            "Mô tả được các hằng đẳng thức: bình phương của tổng và hiệu; hiệu hai bình phương; lập phương của tổng và hiệu; tổng và hiệu hai lập phương.",
            "Vận dụng được bảy hằng đẳng thức đáng nhớ để khai triển, rút gọn biểu thức và tính nhanh.",
            "Vận dụng được các hằng đẳng thức để phân tích đa thức thành nhân tử ở dạng: vận dụng trực tiếp hằng đẳng thức; vận dụng hằng đẳng thức thông qua nhóm hạng tử và đặt nhân tử chung.",
        ],
        "definition": "Hằng đẳng thức (đồng nhất thức) là đẳng thức mà hai vế luôn cùng nhận một giá trị khi thay các chữ trong đẳng thức bằng các số tùy ý. Phân tích đa thức thành nhân tử là biến đổi đa thức đó thành một tích của những đa thức.",
        "theory": (
            "### Bài 6. Hiệu hai bình phương. Bình phương của một tổng hay một hiệu\n"
            "- Với hai biểu thức $A, B$ tùy ý, ta có $A^2 - B^2 = (A - B)(A + B)$; $(A + B)^2 = A^2 + 2AB + B^2$; $(A - B)^2 = A^2 - 2AB + B^2$.\n"
            "### Bài 7. Lập phương của một tổng. Lập phương của một hiệu\n"
            "- Với hai biểu thức $A, B$ tùy ý, ta có $(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$ và $(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$.\n"
            "### Bài 8. Tổng và hiệu hai lập phương\n"
            "- Với hai biểu thức $A, B$ tùy ý, ta có $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$ và $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$ (trong đó $A^2 - AB + B^2$ là bình phương thiếu của một hiệu, $A^2 + AB + B^2$ là bình phương thiếu của một tổng).\n"
            "### Bài 9. Phân tích đa thức thành nhân tử\n"
            "- Ba phương pháp cơ bản để phân tích đa thức thành nhân tử là đặt nhân tử chung, sử dụng hằng đẳng thức và nhóm các hạng tử (thường kết hợp linh hoạt các phương pháp này)."
        ),
        "formulas": [
            G("Nhóm hằng đẳng thức bậc hai", F("Hiệu hai bình phương", "$A^2 - B^2 = (A - B)(A + B)$"), F("Bình phương của một tổng", "$(A + B)^2 = A^2 + 2AB + B^2$"), F("Bình phương của một hiệu", "$(A - B)^2 = A^2 - 2AB + B^2$")),
            G("Nhóm hằng đẳng thức bậc ba", F("Lập phương của một tổng", "$(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$"), F("Lập phương của một hiệu", "$(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$"), F("Tổng hai lập phương", "$A^3 + B^3 = (A + B)(A^2 - AB + B^2)$"), F("Hiệu hai lập phương", "$A^3 - B^3 = (A - B)(A^2 + AB + B^2)$")),
        ],
        "example": "Phân tích đa thức $P = x^3 - 2x^2 + x - xy^2$ thành nhân tử và tính giá trị của $P$ tại $x = 10, y = 9$.",
        "example_answer": "Đặt nhân tử chung $x$: $P = x(x^2 - 2x + 1 - y^2)$. Nhóm 3 hạng tử đầu trong ngoặc: $P = x[(x - 1)^2 - y^2] = x(x - 1 - y)(x - 1 + y)$. Tại $x = 10, y = 9$, ta có $x - 1 - y = 10 - 1 - 9 = 0$, suy ra $P = 10 \\cdot 0 \\cdot (10 - 1 + 9) = 0$.",
        "real_life": "Các hằng đẳng thức đáng nhớ giúp tính nhẩm nhanh diện tích khi mở rộng hoặc thu hẹp đất đai (như tính $99^2 = (100 - 1)^2 = 9801$ hay $52 \\cdot 48 = 50^2 - 2^2 = 2496$) và tối ưu hóa thuật toán tính toán.",
        "quiz": [
            mcq("biet", "Khai triển hằng đẳng thức $(x - 3)^2$ ta được kết quả nào sau đây?", ["$x^2 - 9$", "$x^2 - 6x + 9$", "$x^2 + 6x + 9$", "$x^2 - 3x + 9$"], 1, "Áp dụng bình phương của một hiệu: $(x - 3)^2 = x^2 - 2 \\cdot x \\cdot 3 + 3^2 = x^2 - 6x + 9$."),
            mcq("biet", "Biểu thức $4x^2 - 25y^2$ viết dưới dạng tích là:", ["$(2x - 5y)(2x + 5y)$", "$(4x - 25y)(4x + 25y)$", "$(2x - 5y)^2$", "$(2x + 5y)^2$"], 0, "Ta có $4x^2 - 25y^2 = (2x)^2 - (5y)^2 = (2x - 5y)(2x + 5y)$."),
            mcq("biet", "Biểu thức $x^3 + 8$ được phân tích thành nhân tử là:", ["$(x + 2)(x^2 - 2x + 4)$", "$(x + 2)(x^2 + 2x + 4)$", "$(x + 2)(x^2 - 4x + 4)$", "$(x + 2)^3$"], 0, "Theo hằng đẳng thức tổng hai lập phương: $x^3 + 8 = x^3 + 2^3 = (x + 2)(x^2 - 2x + 4)$."),
            mcq("biet", "Đơn thức cần điền vào chỗ trống trong đẳng thức $x^3 + 6x^2 + 12x + 8 = (x + \\dots)^3$ là:", ["$2$", "$4$", "$8$", "$6$"], 0, "Ta có $x^3 + 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 + 2^3 = (x + 2)^3$."),
            mcq("hieu", "Phân tích đa thức $x^2 - 4x + 4 - y^2$ thành nhân tử ta được:", ["$(x - 2 - y)(x - 2 + y)$", "$(x + 2 - y)(x + 2 + y)$", "$(x - y - 2)^2$", "$(x - 4 - y)(x - 4 + y)$"], 0, "Nhóm $3$ hạng tử đầu: $(x^2 - 4x + 4) - y^2 = (x - 2)^2 - y^2 = (x - 2 - y)(x - 2 + y)$."),
            mcq("hieu", "Giá trị của biểu thức $A = x^3 - 9x^2 + 27x - 27$ tại $x = 13$ là:", ["$1000$", "$100$", "$1728$", "$729$"], 0, "Ta có $A = (x - 3)^3$. Thay $x = 13$ vào được $A = (13 - 3)^3 = 10^3 = 1000$."),
            tf4("hieu", "Cho biểu thức $M = (x + 2)(x^2 - 2x + 4) - (x - 1)^3 - 3x^2$. Xét tính đúng sai của các khẳng định sau:", ["a) Tích $(x + 2)(x^2 - 2x + 4)$ bằng $x^3 + 8$.", "b) Khai triển $(x - 1)^3$ ta được $x^3 - 3x^2 + 3x - 1$.", "c) Sau khi rút gọn, biểu thức $M$ bằng $-3x + 7$.", "d) Tại $x = 3$, giá trị của biểu thức $M$ bằng $0$."], [True, True, False, True], "a) Đúng theo hằng đẳng thức tổng hai lập phương. b) Đúng theo hằng đẳng thức lập phương của một hiệu. c) Sai vì $M = (x^3 + 8) - (x^3 - 3x^2 + 3x - 1) - 3x^2 = -3x + 9$. d) Đúng vì tại $x = 3$, $M = -3 \\cdot 3 + 9 = 0$."),
            tf4("hieu", "Cho đa thức $P = 2x^3 - 8x$. Xét tính đúng sai của các khẳng định sau:", ["a) Nhân tử chung của hai hạng tử trong đa thức $P$ là $2x$.", "b) Phân tích $P$ thành nhân tử triệt để ta được $P = 2x(x - 2)(x + 2)$.", "c) Đa thức $P$ có giá trị bằng $0$ tại ba giá trị của $x$ là $x = 0, x = 2, x = -2$.", "d) Tại $x = 3$, giá trị của đa thức $P$ là $24$."], [True, True, True, False], "a) Đúng vì $2x^3 - 8x = 2x(x^2 - 4)$. b) Đúng vì $x^2 - 4 = (x - 2)(x + 2)$ nên $P = 2x(x - 2)(x + 2)$. c) Đúng vì $P = 0 \\iff 2x(x - 2)(x + 2) = 0 \\iff x \\in \\{0; 2; -2\\}$. d) Sai vì tại $x = 3$, $P = 2 \\cdot 3 \\cdot (3 - 2)(3 + 2) = 30$."),
            mcq("vandung", "Cho $x + y = 7$ và $xy = 10$. Giá trị của biểu thức $S = x^3 + y^3$ là:", ["$133$", "$343$", "$273$", "$70$"], 0, "Ta có $x^3 + y^3 = (x + y)^3 - 3xy(x + y) = 7^3 - 3 \\cdot 10 \\cdot 7 = 343 - 210 = 133$."),
            short("vandung", "Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 6x + 25$ với mọi số thực $x$.", ["16"], "Ta có $A = (x^2 - 6x + 9) + 16 = (x - 3)^2 + 16 \\ge 16$ với mọi $x \\in \\mathbb{R}$. Dấu '$=$' xảy ra khi $x = 3$. Vậy giá trị nhỏ nhất của $A$ là $16$."),
        ],
    },
    {
        "topic": "l8-ch03-tu-giac",
        "title": "Tứ giác",
        "icon": "📐",
        "description": "Tứ giác lồi, hình thang cân, hình bình hành, hình chữ nhật, hình thoi và hình vuông",
        "requirements": [
            "Mô tả được tứ giác, tứ giác lồi và giải thích được định lí về tổng các góc trong một tứ giác lồi bằng $360^\\circ$.",
            "Giải thích được tính chất về góc kề một đáy, cạnh bên, đường chéo của hình thang cân và nhận biết được dấu hiệu để một hình thang là hình thang cân.",
            "Giải thích được tính chất về cạnh đối, góc đối, đường chéo của hình bình hành và nhận biết được dấu hiệu để một tứ giác là hình bình hành.",
            "Giải thích được tính chất về hai đường chéo của hình chữ nhật và nhận biết được dấu hiệu để một hình bình hành là hình chữ nhật.",
            "Giải thích được tính chất về đường chéo của hình thoi và nhận biết được dấu hiệu để một hình bình hành là hình thoi.",
            "Giải thích được tính chất về hai đường chéo của hình vuông và nhận biết được dấu hiệu để một hình chữ nhật hoặc hình thoi là hình vuông.",
        ],
        "definition": "Tứ giác lồi là tứ giác luôn nằm về một phía của đường thẳng chứa bất kì cạnh nào của tứ giác đó. Các tứ giác đặc biệt (hình thang cân, hình bình hành, hình chữ nhật, hình thoi, hình vuông) được xác định bởi các tính chất về cạnh song song, cạnh bằng nhau, góc vuông và đường chéo.",
        "theory": (
            "### Bài 10. Tứ giác\n"
            "- Tổng các góc của một tứ giác bằng $360^\\circ$.\n"
            "### Bài 11. Hình thang cân\n"
            "- Hình thang là tứ giác có hai cạnh đối song song. Hình thang cân là hình thang có hai góc kề một đáy bằng nhau. Trong hình thang cân, hai cạnh bên bằng nhau và hai đường chéo bằng nhau. Hình thang có hai đường chéo bằng nhau là hình thang cân.\n"
            "### Bài 12. Hình bình hành\n"
            "- Hình bình hành là tứ giác có các cạnh đối song song. Trong hình bình hành: các cạnh đối bằng nhau, các góc đối bằng nhau, hai đường chéo cắt nhau tại trung điểm của mỗi đường. Tứ giác có một cặp cạnh đối vừa song song vừa bằng nhau là hình bình hành.\n"
            "### Bài 13. Hình chữ nhật\n"
            "- Hình chữ nhật là tứ giác có bốn góc vuông. Trong hình chữ nhật, hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường. Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền. Hình bình hành có một góc vuông hoặc có hai đường chéo bằng nhau là hình chữ nhật.\n"
            "### Bài 14. Hình thoi và hình vuông\n"
            "- Hình thoi là tứ giác có bốn cạnh bằng nhau; hai đường chéo của hình thoi vuông góc với nhau và là các đường phân giác của các góc. Hình vuông là tứ giác có bốn góc vuông và bốn cạnh bằng nhau (vừa là hình chữ nhật, vừa là hình thoi)."
        ),
        "formulas": [
            G("Tổng các góc và tính chất đường chéo", F("Tổng bốn góc của tứ giác $ABCD$", "$\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = 360^\\circ$"), F("Hai góc kề một cạnh bên của hình thang ($AB \\parallel CD$)", "$\\widehat{A} + \\widehat{D} = 180^\\circ, \\quad \\widehat{B} + \\widehat{C} = 180^\\circ$"), F("Đường trung tuyến $AM$ ứng với cạnh huyền $BC$ trong tam giác vuông", "$AM = \\frac{1}{2} BC$")),
            G("Chu vi và diện tích các tứ giác đặc biệt", F("Diện tích hình thang (hai đáy $a, b$, chiều cao $h$)", "$S = \\frac{(a + b) \\cdot h}{2}$"), F("Diện tích hình bình hành (cạnh $a$, chiều cao $h$)", "$S = a \\cdot h$"), F("Diện tích hình chữ nhật (hai kích thước $a, b$)", "$S = a \\cdot b$"), F("Diện tích hình thoi (hai đường chéo $d_1, d_2$)", "$S = \\frac{1}{2} d_1 \\cdot d_2$")),
        ],
        "example": "Cho tứ giác $ABCD$ có $\\widehat{A} = 110^\\circ, \\widehat{B} = 85^\\circ, \\widehat{D} = 70^\\circ$. Tính số đo góc $C$ và chứng tỏ hai cạnh $AB, CD$ song song với nhau.",
        "example_answer": "Áp dụng định lí tổng các góc của tứ giác: $\\widehat{C} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{D}) = 360^\\circ - (110^\\circ + 85^\\circ + 70^\\circ) = 95^\\circ$. Ta thấy $\\widehat{A} + \\widehat{D} = 110^\\circ + 70^\\circ = 180^\\circ$, mà hai góc này ở vị trí trong cùng phía nên $AB \\parallel CD$.",
        "real_life": "Tính chất của hình bình hành, hình chữ nhật và hình thoi được ứng dụng trong cơ cấu nâng hạ chữ X (con đội ô tô), cổng xếp tự động hình thoi, khung cửa sổ và kiểm tra góc vuông khi xây dựng bằng cách đo hai đường chéo bằng nhau.",
        "quiz": [
            mcq("biet", "Tổng các góc trong một tứ giác lồi bằng bao nhiêu độ?", ["$180^\\circ$", "$360^\\circ$", "$270^\\circ$", "$540^\\circ$"], 1, "Theo định lí tổng các góc của một tứ giác, tổng bốn góc của tứ giác lồi bằng $360^\\circ$."),
            mcq("biet", "Hình bình hành có thêm điều kiện nào sau đây thì trở thành hình chữ nhật?", ["Hai cạnh kề bằng nhau", "Hai đường chéo bằng nhau", "Hai đường chéo vuông góc", "Một đường chéo là phân giác của một góc"], 1, "Hình bình hành có hai đường chéo bằng nhau (hoặc có một góc vuông) là hình chữ nhật."),
            mcq("biet", "Tứ giác có bốn cạnh bằng nhau là hình gì?", ["Hình chữ nhật", "Hình thoi", "Hình thang cân", "Hình vuông"], 1, "Theo định nghĩa, hình thoi là tứ giác có bốn cạnh bằng nhau."),
            mcq("biet", "Trong tam giác vuông có cạnh huyền bằng $14\\text{ cm}$, độ dài đường trung tuyến ứng với cạnh huyền bằng:", ["$7\\text{ cm}$", "$14\\text{ cm}$", "$28\\text{ cm}$", "$3,5\\text{ cm}$"], 0, "Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: $14 : 2 = 7\\text{ cm}$."),
            mcq("hieu", "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{A} = 115^\\circ$. Số đo góc $C$ bằng:", ["$65^\\circ$", "$115^\\circ$", "$75^\\circ$", "$85^\\circ$"], 0, "Vì $ABCD$ là hình thang cân đáy $AB, CD$ nên $\\widehat{B} = \\widehat{A} = 115^\\circ$. Lại có $AB \\parallel CD$ nên $\\widehat{C} = 180^\\circ - \\widehat{B} = 180^\\circ - 115^\\circ = 65^\\circ$."),
            mcq("hieu", "Cho hình bình hành $ABCD$ có $\\widehat{A} - \\widehat{B} = 40^\\circ$. Số đo của $\\widehat{C}$ là:", ["$110^\\circ$", "$70^\\circ$", "$140^\\circ$", "$100^\\circ$"], 0, "Trong hình bình hành $ABCD$, $\\widehat{A} + \\widehat{B} = 180^\\circ$. Kết hợp $\\widehat{A} - \\widehat{B} = 40^\\circ$ suy ra $\\widehat{A} = (180^\\circ + 40^\\circ) : 2 = 110^\\circ$. Do đó $\\widehat{C} = \\widehat{A} = 110^\\circ$."),
            tf4("hieu", "Cho hình chữ nhật $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$, biết $AB = 8\\text{ cm}$ và $AC = 10\\text{ cm}$. Xét tính đúng sai của các khẳng định sau:", ["a) Hai đường chéo bằng nhau nên $BD = 10\\text{ cm}$.", "b) Độ dài đoạn thẳng $OA = OB = 5\\text{ cm}$.", "c) Tam giác $OAB$ là tam giác đều.", "d) Hai đường chéo $AC$ và $BD$ vuông góc với nhau tại $O$."], [True, True, False, False], "a) Đúng vì hai đường chéo của hình chữ nhật bằng nhau. b) Đúng vì $O$ là trung điểm của $AC$ và $BD$ nên $OA = OB = 10 : 2 = 5\\text{ cm}$. c) Sai vì $OA = OB = 5\\text{ cm} \\neq AB = 8\\text{ cm}$ nên $\\triangle OAB$ chỉ cân tại $O$, không đều. d) Sai vì $AB = 8\\text{ cm}$ còn $BC = \\sqrt{10^2 - 8^2} = 6\\text{ cm} \\neq AB$, nên $ABCD$ không phải hình vuông, hai đường chéo không vuông góc."),
            tf4("hieu", "Xét các dấu hiệu nhận biết tứ giác đặc biệt. Các khẳng định sau đúng hay sai?", ["a) Tứ giác có hai đường chéo cắt nhau tại trung điểm của mỗi đường là hình bình hành.", "b) Hình bình hành có hai đường chéo vuông góc với nhau là hình thoi.", "c) Hình thang có hai cạnh bên bằng nhau luôn là hình thang cân.", "d) Hình chữ nhật có hai cạnh kề bằng nhau là hình vuông."], [True, True, False, True], "a) Đúng theo dấu hiệu nhận biết hình bình hành. b) Đúng theo dấu hiệu nhận biết hình thoi. c) Sai vì hình bình hành (không phải hình chữ nhật) cũng là hình thang có hai cạnh bên bằng nhau nhưng không phải hình thang cân. d) Đúng theo dấu hiệu nhận biết hình vuông."),
            mcq("vandung", "Cho tam giác $ABC$ vuông tại $A$, điểm $M$ thuộc cạnh huyền $BC$. Gọi $D, E$ lần lượt là chân đường vuông góc kẻ từ $M$ đến $AB$ và $AC$. Để độ dài đoạn thẳng $DE$ nhỏ nhất thì điểm $M$ phải ở vị trí nào trên cạnh $BC$?", ["Chân đường cao kẻ từ $A$ xuống $BC$", "Trung điểm của cạnh $BC$", "Điểm trùng với $B$", "Giao điểm của đường phân giác góc $A$ với $BC$"], 0, "Tứ giác $ADME$ có $\\widehat{A} = \\widehat{D} = \\widehat{E} = 90^\\circ$ nên là hình chữ nhật, suy ra $DE = AM$. Để $DE$ nhỏ nhất thì $AM$ nhỏ nhất, tức là $AM \\perp BC$ hay $M$ là chân đường cao kẻ từ $A$ xuống $BC$."),
            short("vandung", "Một hình thoi có hai đường chéo dài $12\\text{ cm}$ và $16\\text{ cm}$. Tính diện tích của hình thoi đó (đơn vị $\\text{cm}^2$).", ["96"], "Diện tích của hình thoi là $S = \\frac{1}{2} \\cdot 12 \\cdot 16 = 96\\text{ (cm}^2\\text{)}$."),
        ],
    },
    {
        "topic": "l8-ch04-dinh-li-thales",
        "title": "Định lí Thalès",
        "icon": "📏",
        "description": "Đoạn thẳng tỉ lệ, định lí Thalès thuận và đảo, đường trung bình và tính chất đường phân giác của tam giác",
        "requirements": [
            "Nhận biết được tỉ số của hai đoạn thẳng và các đoạn thẳng tỉ lệ.",
            "Giải thích được định lí Thalès trong tam giác (định lí thuận và đảo) và hệ quả của định lí Thalès.",
            "Mô tả được định nghĩa đường trung bình của tam giác và giải thích được tính chất đường trung bình của tam giác.",
            "Giải thích được tính chất đường phân giác trong của tam giác.",
            "Tính được độ dài đoạn thẳng và giải quyết được một số vấn đề thực tiễn gắn với định lí Thalès, đường trung bình và đường phân giác của tam giác.",
        ],
        "definition": "Định lí Thalès thiết lập mối quan hệ tỉ lệ giữa các đoạn thẳng được tạo ra khi một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại. Từ đó suy ra tính chất của đường trung bình và mối liên hệ với tính chất đường phân giác của tam giác.",
        "theory": (
            "### Bài 15. Định lí Thalès trong tam giác\n"
            "- Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì nó định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ. Định lí Thalès đảo: Nếu một đường thẳng cắt hai cạnh của một tam giác và định ra trên hai cạnh này những đoạn thẳng tương ứng tỉ lệ thì đường thẳng đó song song với cạnh còn lại của tam giác. Hệ quả: Nếu một đường thẳng cắt hai cạnh của một tam giác và song song với cạnh còn lại thì nó tạo thành một tam giác mới có ba cạnh tương ứng tỉ lệ với ba cạnh của tam giác đã cho.\n"
            "### Bài 16. Đường trung bình của tam giác\n"
            "- Đường trung bình của tam giác là đoạn thẳng nối trung điểm hai cạnh của tam giác. Đường trung bình của tam giác thì song song với cạnh thứ ba và bằng nửa cạnh đó.\n"
            "### Bài 17. Tính chất đường phân giác của tam giác\n"
            "- Trong một tam giác, đường phân giác của một góc chia cạnh đối diện thành hai đoạn thẳng tỉ lệ với hai cạnh kề của hai đoạn ấy."
        ),
        "formulas": [
            G("Định lí Thalès và hệ quả ($DE \\parallel BC, D \\in AB, E \\in AC$)", F("Định lí Thalès thuận", "$\\frac{AD}{AB} = \\frac{AE}{AC}; \\quad \\frac{AD}{DB} = \\frac{AE}{EC}; \\quad \\frac{DB}{AB} = \\frac{EC}{AC}$"), F("Hệ quả của định lí Thalès", "$\\frac{AD}{AB} = \\frac{AE}{AC} = \\frac{DE}{BC}$")),
            G("Đường trung bình và đường phân giác của tam giác", F("Đường trung bình $MN$ ứng với cạnh $BC$", "$MN \\parallel BC \\quad \\text{và} \\quad MN = \\frac{1}{2} BC$"), F("Đường phân giác $AD$ của $\\widehat{BAC}$ ($D \\in BC$)", "$\\frac{DB}{DC} = \\frac{AB}{AC}$")),
        ],
        "example": "Cho tam giác $ABC$ có $AB = 6\\text{ cm}, AC = 9\\text{ cm}, BC = 10\\text{ cm}$. Tia phân giác của góc $A$ cắt cạnh $BC$ tại $D$. Tính độ dài các đoạn thẳng $DB$ và $DC$.",
        "example_answer": "Theo tính chất đường phân giác của tam giác $ABC$, ta có $\\frac{DB}{DC} = \\frac{AB}{AC} = \\frac{6}{9} = \\frac{2}{3}$. Áp dụng tính chất dãy tỉ số bằng nhau: $\\frac{DB}{2} = \\frac{DC}{3} = \\frac{DB + DC}{2 + 3} = \\frac{BC}{5} = \\frac{10}{5} = 2$. Vậy $DB = 2 \\cdot 2 = 4\\text{ cm}$ và $DC = 3 \\cdot 2 = 6\\text{ cm}$.",
        "real_life": "Định lí Thalès và tính chất đường trung bình giúp đo gián tiếp khoảng cách giữa hai bờ sông, đo chiều cao của cây hoặc tòa nhà thông qua bóng nắng mà không cần trèo lên đỉnh.",
        "quiz": [
            mcq("biet", "Cho đoạn thẳng $AB = 15\\text{ cm}$ và $CD = 5\\text{ dm}$. Tỉ số $\\frac{AB}{CD}$ bằng:", ["$3$", "$\\frac{3}{10}$", "$\\frac{10}{3}$", "$\\frac{1}{3}$"], 1, "Đổi cùng đơn vị: $CD = 5\\text{ dm} = 50\\text{ cm}$. Khi đó $\\frac{AB}{CD} = \\frac{15}{50} = \\frac{3}{10}$."),
            mcq("biet", "Cho $\\triangle ABC$, đường thẳng $d$ song song với $BC$ cắt $AB, AC$ lần lượt tại $M, N$. Đẳng thức nào sau đây đúng?", ["$\\frac{AM}{MB} = \\frac{AN}{NC}$", "$\\frac{AM}{AB} = \\frac{NC}{AC}$", "$\\frac{AM}{AN} = \\frac{BC}{MN}$", "$\\frac{MB}{AB} = \\frac{AN}{AC}$"], 0, "Theo định lí Thalès trong tam giác $ABC$ với $MN \\parallel BC$, ta có $\\frac{AM}{MB} = \\frac{AN}{NC}$."),
            mcq("biet", "Cho $\\triangle ABC$ có $M, N$ lần lượt là trung điểm của $AB, AC$ và $BC = 18\\text{ cm}$. Độ dài đoạn thẳng $MN$ là:", ["$9\\text{ cm}$", "$18\\text{ cm}$", "$36\\text{ cm}$", "$6\\text{ cm}$"], 0, "$MN$ là đường trung bình của $\\triangle ABC$ nên $MN = \\frac{1}{2}BC = \\frac{1}{2} \\cdot 18 = 9\\text{ cm}$."),
            mcq("biet", "Cho $\\triangle ABC$ có $AD$ là đường phân giác trong của góc $A$ ($D \\in BC$). Khẳng định nào sau đây đúng?", ["$\\frac{DB}{DC} = \\frac{AB}{AC}$", "$\\frac{DB}{DC} = \\frac{AC}{AB}$", "$\\frac{AB}{DB} = \\frac{DC}{AC}$", "$\\frac{AD}{BC} = \\frac{AB}{AC}$"], 0, "Theo tính chất đường phân giác của tam giác, đường phân giác $AD$ chia cạnh đối diện $BC$ thành hai đoạn tỉ lệ với hai cạnh kề: $\\frac{DB}{DC} = \\frac{AB}{AC}$."),
            mcq("hieu", "Cho $\\triangle ABC$ có $D \\in AB, E \\in AC$ sao cho $DE \\parallel BC$. Biết $AD = 4\\text{ cm}, DB = 6\\text{ cm}$ và $AE = 5\\text{ cm}$. Độ dài cạnh $AC$ bằng:", ["$12,5\\text{ cm}$", "$7,5\\text{ cm}$", "$10\\text{ cm}$", "$15\\text{ cm}$"], 0, "Theo định lí Thalès: $\\frac{AD}{DB} = \\frac{AE}{EC} \\implies \\frac{4}{6} = \\frac{5}{EC} \\implies EC = 7,5\\text{ cm}$. Vậy $AC = AE + EC = 5 + 7,5 = 12,5\\text{ cm}$."),
            mcq("hieu", "Cho $\\triangle ABC$ có $AB = 8\\text{ cm}, AC = 12\\text{ cm}$. Đường phân giác góc $A$ cắt $BC$ tại $D$, biết $BD = 6\\text{ cm}$. Độ dài cạnh $BC$ bằng:", ["$15\\text{ cm}$", "$9\\text{ cm}$", "$18\\text{ cm}$", "$14\\text{ cm}$"], 0, "Ta có $\\frac{BD}{CD} = \\frac{AB}{AC} \\implies \\frac{6}{CD} = \\frac{8}{12} \\implies CD = 9\\text{ cm}$. Do đó $BC = BD + CD = 6 + 9 = 15\\text{ cm}$."),
            tf4("hieu", "Cho $\\triangle ABC$ có $AB = 9\\text{ cm}, AC = 12\\text{ cm}, BC = 15\\text{ cm}$. Trên cạnh $AB$ lấy điểm $M$ sao cho $AM = 3\\text{ cm}$, trên cạnh $AC$ lấy điểm $N$ sao cho $AN = 4\\text{ cm}$. Xét tính đúng sai của các khẳng định sau:", ["a) Tỉ số $\\frac{AM}{AB}$ và $\\frac{AN}{AC}$ cùng bằng $\\frac{1}{3}$.", "b) Đường thẳng $MN$ song song với cạnh $BC$.", "c) Độ dài đoạn thẳng $MN$ bằng $5\\text{ cm}$.", "d) Đoạn thẳng $MN$ là đường trung bình của $\\triangle ABC$."], [True, True, True, False], "a) Đúng vì $\\frac{AM}{AB} = \\frac{3}{9} = \\frac{1}{3}$ và $\\frac{AN}{AC} = \\frac{4}{12} = \\frac{1}{3}$. b) Đúng theo định lí Thalès đảo. c) Đúng theo hệ quả định lí Thalès: $\\frac{MN}{BC} = \\frac{AM}{AB} = \\frac{1}{3} \\implies MN = 15 : 3 = 5\\text{ cm}$. d) Sai vì $M, N$ không phải là trung điểm của $AB, AC$."),
            tf4("hieu", "Cho tứ giác $ABCD$ có hai đường chéo $AC = 10\\text{ cm}, BD = 16\\text{ cm}$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$. Xét tính đúng sai của các khẳng định sau:", ["a) $MN$ là đường trung bình của $\\triangle ABC$ nên $MN \\parallel AC$ và $MN = 5\\text{ cm}$.", "b) $PQ$ là đường trung bình của $\\triangle ADC$ nên $PQ \\parallel AC$ và $PQ = 5\\text{ cm}$.", "c) Tứ giác $MNPQ$ là hình bình hành.", "d) Chu vi của tứ giác $MNPQ$ bằng $52\\text{ cm}$."], [True, True, True, False], "a) Đúng vì $M, N$ là trung điểm của $AB, BC$ nên $MN = \\frac{1}{2}AC = 5\\text{ cm}$. b) Đúng vì $P, Q$ là trung điểm của $CD, DA$ nên $PQ = \\frac{1}{2}AC = 5\\text{ cm}$. c) Đúng vì $MN \\parallel PQ$ và $MN = PQ = 5\\text{ cm}$ nên $MNPQ$ là hình bình hành. d) Sai vì $NP = QM = \\frac{1}{2}BD = 8\\text{ cm}$, nên chu vi $MNPQ$ là $2(5 + 8) = 26\\text{ cm}$."),
            mcq("vandung", "Để đo khoảng cách giữa hai vị trí $B$ và $C$ ở hai bên bờ hồ nước, người ta chọn điểm $A$ trên bờ rồi lấy $M$ trên $AB$, $N$ trên $AC$ sao cho $MN \\parallel BC$. Biết $AM = 15\\text{ m}, MB = 30\\text{ m}$ và $MN = 22\\text{ m}$. Khoảng cách $BC$ bằng:", ["$66\\text{ m}$", "$44\\text{ m}$", "$55\\text{ m}$", "$33\\text{ m}$"], 0, "Ta có $AB = AM + MB = 15 + 30 = 45\\text{ m}$. Vì $MN \\parallel BC$, theo hệ quả định lí Thalès: $\\frac{MN}{BC} = \\frac{AM}{AB} = \\frac{15}{45} = \\frac{1}{3} \\implies BC = 3 \\cdot 22 = 66\\text{ m}$."),
            short("vandung", "Cho $\\triangle ABC$ có chu vi bằng $42\\text{ cm}$, trong đó $BC = 14\\text{ cm}$. Tia phân giác của góc $A$ cắt $BC$ tại $D$ sao cho $\\frac{DB}{DC} = \\frac{3}{4}$. Tính độ dài cạnh $AB$ (đơn vị $\\text{cm}$).", ["12"], "Tổng hai cạnh $AB + AC = 42 - 14 = 28\\text{ cm}$. Theo tính chất đường phân giác: $\\frac{AB}{AC} = \\frac{DB}{DC} = \\frac{3}{4}$. Áp dụng tính chất dãy tỉ số bằng nhau: $\\frac{AB}{3} = \\frac{AC}{4} = \\frac{AB + AC}{7} = \\frac{28}{7} = 4 \\implies AB = 3 \\cdot 4 = 12\\text{ cm}$."),
        ],
    },
    {
        "topic": "l8-ch05-du-lieu-va-bieu-do",
        "title": "Dữ liệu và biểu đồ",
        "icon": "📊",
        "description": "Thu thập và phân loại dữ liệu, lựa chọn bảng và biểu đồ thống kê, phân tích số liệu dựa vào biểu đồ",
        "requirements": [
            "Thực hiện và lí giải được việc thu thập, phân loại dữ liệu theo các tiêu chí cho trước từ nhiều nguồn khác nhau.",
            "Nhận biết được dữ liệu định tính (không là số) và dữ liệu định lượng (là số: rời rạc và liên tục); nhận biết được tính hợp lí và tính đại diện của dữ liệu.",
            "Lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp (biểu đồ tranh, biểu đồ cột đơn/kép, biểu đồ đoạn thẳng, biểu đồ hình quạt tròn).",
            "So sánh được các dạng biểu diễn khác nhau cho một tập dữ liệu.",
            "Phát hiện và giải quyết được vấn đề, quy luật đơn giản hoặc nhận ra điểm không hợp lí dựa trên phân tích các số liệu thống kê ở dạng biểu đồ.",
        ],
        "definition": "Thống kê học nghiên cứu cách thu thập, phân loại, biểu diễn và phân tích dữ liệu. Dữ liệu được chia thành dữ liệu là số (số liệu rời rạc hoặc liên tục) và dữ liệu không là số (có thể sắp thứ tự hoặc không thể sắp thứ tự).",
        "theory": (
            "### Bài 18. Thu thập và phân loại dữ liệu\n"
            "- Dữ liệu thu thập trực tiếp (quan sát, làm thí nghiệm, lập phiếu hỏi, phỏng vấn) hoặc gián tiếp (từ sách báo, Internet). Dữ liệu chia thành hai loại: dữ liệu là số (số liệu rời rạc nhận giá trị hữu hạn/đếm được; số liệu liên tục nhận giá trị bất kì trong một khoảng) và dữ liệu không là số.\n"
            "### Bài 19. Biểu diễn dữ liệu bằng bảng, biểu đồ\n"
            "- Lựa chọn biểu đồ phù hợp với mục đích: Biểu đồ cột (so sánh các thành phần), biểu đồ cột kép (so sánh hai bộ dữ liệu cùng loại), biểu đồ đoạn thẳng (biểu diễn xu thế thay đổi theo thời gian), biểu đồ hình quạt tròn (biểu diễn tỉ lệ phần trăm các thành phần so với toàn thể).\n"
            "### Bài 20. Phân tích số liệu thống kê dựa vào biểu đồ\n"
            "- Khi đọc và phân tích biểu đồ cần chú ý gốc trục đứng, đơn vị đo, tỉ lệ chia trên các trục để tránh hiểu lầm xu thế; từ biểu đồ rút ra nhận xét về xu hướng tăng giảm, giá trị lớn nhất, nhỏ nhất và tỉ lệ tăng trưởng."
        ),
        "formulas": [
            G("Tính toán tỉ lệ trong thống kê", F("Tỉ lệ phần trăm của một thành phần", "$p\\% = \\frac{\\text{Giá trị thành phần}}{\\text{Tổng giá trị}} \\cdot 100\\%$"), F("Giá trị thành phần khi biết tổng $N$ và tỉ lệ $p\\%$", "$x = N \\cdot \\frac{p}{100}$"), F("Tỉ lệ phần trăm tăng (giảm) từ $A$ lên $B$", "$\\Delta\\% = \\frac{B - A}{A} \\cdot 100\\%$")),
        ],
        "example": "Một cửa hàng bán được $400$ chiếc áo trong tháng 10, gồm $4$ cỡ: S ($15\\%$), M ($40\\%$), L ($30\\%$) và XL (còn lại). Tính số lượng áo cỡ XL đã bán và cho biết nên dùng biểu đồ nào để thể hiện tỉ lệ phần trăm các cỡ áo.",
        "example_answer": "Tỉ lệ phần trăm áo cỡ XL là $100\\% - (15\\% + 40\\% + 30\\%) = 15\\%$. Số lượng áo cỡ XL đã bán là $400 \\cdot 15\\% = 60$ (chiếc). Để thể hiện tỉ lệ phần trăm của từng cỡ áo so với tổng số áo bán ra, ta nên sử dụng biểu đồ hình quạt tròn.",
        "real_life": "Phân loại và biểu diễn dữ liệu bằng biểu đồ được sử dụng hàng ngày trong báo cáo kinh tế, theo dõi biến đổi khí hậu (nhiệt độ, lượng mưa các tháng), khảo sát thị hiếu khách hàng và thống kê y tế.",
        "quiz": [
            mcq("biet", "Trong các dữ liệu sau, dữ liệu nào là số liệu liên tục?", ["Số học sinh của các lớp khối 8 trong trường", "Chiều cao (đo bằng $\\text{cm}$) của các học sinh trong lớp 8A", "Tên các môn thể thao yêu thích của học sinh", "Xếp loại học tập (Tốt, Khá, Đạt, Chưa đạt) của học sinh"], 1, "Chiều cao của học sinh có thể nhận giá trị thực bất kì trong một khoảng nên là số liệu liên tục."),
            mcq("biet", "Để biểu diễn sự thay đổi nhiệt độ trung bình tại Hà Nội qua $12$ tháng trong năm, loại biểu đồ nào thích hợp nhất?", ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ cột kép", "Biểu đồ tranh"], 0, "Biểu đồ đoạn thẳng thích hợp nhất để biểu diễn sự thay đổi (xu thế tăng giảm) của một đại lượng theo thời gian."),
            mcq("biet", "Để biểu diễn tỉ lệ phần trăm chi tiêu hàng tháng của một gia đình cho các khoản (Ăn uống, Giáo dục, Điện nước, Tiết kiệm), loại biểu đồ thích hợp nhất là:", ["Biểu đồ hình quạt tròn", "Biểu đồ đoạn thẳng", "Biểu đồ cột kép", "Biểu đồ tranh"], 0, "Biểu đồ hình quạt tròn dùng để biểu diễn tỉ lệ phần trăm của từng phần so với toàn thể ($100\\%$)."),
            mcq("biet", "Dữ liệu 'Mức độ hài lòng của khách hàng: Rất hài lòng, Hài lòng, Bình thường, Không hài lòng' thuộc loại dữ liệu nào?", ["Dữ liệu không là số, có thể sắp thứ tự", "Dữ liệu không là số, không thể sắp thứ tự", "Số liệu rời rạc", "Số liệu liên tục"], 0, "Các mức độ hài lòng được biểu diễn bằng từ ngữ (không là số) và có thứ tự từ cao đến thấp."),
            mcq("hieu", "Biểu đồ hình quạt tròn cho biết tỉ lệ học sinh tham gia các câu lạc bộ của khối 8 gồm: Toán ($25\\%$), Tiếng Anh ($35\\%$), Văn ($15\\%$) và Thể thao (còn lại). Biết tổng số học sinh tham gia là $200$ em và mỗi em chỉ tham gia một câu lạc bộ. Số học sinh tham gia câu lạc bộ Thể thao là:", ["$50$ học sinh", "$25$ học sinh", "$70$ học sinh", "$30$ học sinh"], 0, "Tỉ lệ học sinh tham gia câu lạc bộ Thể thao là $100\\% - (25\\% + 35\\% + 15\\%) = 25\\%$. Số học sinh là $200 \\cdot 25\\% = 50$ em."),
            mcq("hieu", "Doanh thu của một cửa hàng quý I là $120$ triệu đồng, quý II là $150$ triệu đồng. Tỉ lệ phần trăm tăng trưởng doanh thu của quý II so với quý I là:", ["$25\\%$", "$20\\%$", "$30\\%$", "$125\\%$"], 0, "Mức tăng là $150 - 120 = 30$ triệu đồng. Phần trăm tăng trưởng so với quý I là $\\frac{30}{120} \\cdot 100\\% = 25\\%$."),
            tf4("hieu", "Bảng thống kê số lượng sách mượn tại thư viện trường của hai lớp 8A và 8B trong $3$ tháng như sau: Tháng 9 (8A: $40$ quyển, 8B: $35$ quyển); Tháng 10 (8A: $50$ quyển, 8B: $45$ quyển); Tháng 11 (8A: $45$ quyển, 8B: $60$ quyển). Xét tính đúng sai của các khẳng định sau:", ["a) Dữ liệu về số quyển sách mượn là số liệu rời rạc.", "b) Để trực quan hóa việc so sánh số sách mượn của hai lớp 8A và 8B trong từng tháng, ta nên vẽ biểu đồ cột kép.", "c) Tổng số sách lớp 8A mượn trong cả $3$ tháng nhiều hơn tổng số sách lớp 8B mượn trong cả $3$ tháng.", "d) Trong tháng 11, số sách lớp 8B mượn nhiều hơn lớp 8A là $15$ quyển."], [True, True, False, True], "a) Đúng vì số quyển sách là số tự nhiên đếm được (số liệu rời rạc). b) Đúng vì biểu đồ cột kép giúp so sánh trực tiếp hai bộ dữ liệu cùng loại theo từng tháng. c) Sai vì tổng của 8A là $40 + 50 + 45 = 135$ quyển, còn tổng của 8B là $35 + 45 + 60 = 140$ quyển ($135 < 140$). d) Đúng vì trong tháng 11, $60 - 45 = 15$ quyển."),
            tf4("hieu", "Khi đánh giá tính hợp lí và tính đại diện của dữ liệu trong thống kê, xét tính đúng sai của các nhận định sau:", ["a) Để khảo sát thời gian tự học của toàn bộ học sinh khối 8 trong trường, chỉ hỏi ý kiến các bạn trong đội tuyển học sinh giỏi Toán là đảm bảo tính đại diện.", "b) Trong bảng thống kê tỉ lệ phần trăm các loại phương tiện đến trường của học sinh lớp 8C, tổng các tỉ lệ phần trăm của tất cả các thành phần bằng $105\\%$ là dữ liệu không hợp lí.", "c) Khi hai biểu đồ cột có gốc trục đứng khác nhau (một biểu đồ bắt đầu từ $0$, một biểu đồ bắt đầu từ $90$), tỉ lệ chiều cao giữa các cột trên hai biểu đồ sẽ khác nhau.", "d) Muốn chuyển dữ liệu từ bảng tần số sang biểu đồ hình quạt tròn, ta cần tính tỉ lệ phần trăm của từng thành phần so với tổng số."], [False, True, True, True], "a) Sai vì mẫu khảo sát chỉ gồm học sinh đội tuyển không đại diện cho toàn bộ học sinh khối 8. b) Đúng vì tổng tỉ lệ phần trăm các thành phần của một tổng thể phải đúng bằng $100\\%$. c) Đúng vì việc cắt bớt trục đứng làm thay đổi tỉ lệ chiều cao các cột dễ gây hiểu lầm. d) Đúng vì biểu đồ hình quạt tròn biểu diễn tỉ lệ phần trăm."),
            mcq("vandung", "Một trường THCS có $450$ học sinh khối 8. Theo biểu đồ hình quạt tròn kết quả xếp loại rèn luyện học kì I: Tốt chiếm $60\\%$, Khá chiếm $30\\%$, Đạt chiếm $8\\%$, còn lại là Chưa đạt. Hỏi số học sinh xếp loại Tốt nhiều hơn số học sinh xếp loại Chưa đạt là bao nhiêu em?", ["$261$ học sinh", "$270$ học sinh", "$252$ học sinh", "$135$ học sinh"], 0, "Tỉ lệ học sinh Chưa đạt là $100\\% - (60\\% + 30\\% + 8\\%) = 2\\%$. Hiệu tỉ lệ giữa loại Tốt và Chưa đạt là $60\\% - 2\\% = 58\\%$. Số học sinh chênh lệch là $450 \\cdot 58\\% = 261$ (học sinh)."),
            short("vandung", "Sản lượng lúa của một hợp tác xã năm 2025 đạt $800$ tấn. Năm 2026, nhờ áp dụng kĩ thuật mới, sản lượng lúa tăng thêm $15\\%$ so với năm 2025. Hỏi năm 2026 hợp tác xã thu hoạch được bao nhiêu tấn lúa?", ["920"], "Sản lượng lúa năm 2026 là $800 \\cdot (1 + 15\\%) = 800 \\cdot 1,15 = 920$ (tấn)."),
        ],
    },
    {
        "topic": "l8-ch06-phan-thuc-dai-so",
        "title": "Phân thức đại số",
        "icon": "➗",
        "description": "Khái niệm phân thức đại số, tính chất cơ bản, rút gọn, quy đồng mẫu thức và các phép toán cộng, trừ, nhân, chia phân thức",
        "requirements": [
            "Nhận biết được các khái niệm cơ bản về phân thức đại số: định nghĩa, điều kiện xác định, giá trị của phân thức đại số, hai phân thức bằng nhau.",
            "Mô tả được những tính chất cơ bản của phân thức đại số và vận dụng để rút gọn phân thức, quy đồng mẫu thức nhiều phân thức.",
            "Thực hiện được các phép tính: phép cộng, phép trừ, phép nhân, phép chia đối với hai phân thức đại số.",
            "Vận dụng được các tính chất giao hoán, kết hợp, phân phối của phép nhân đối với phép cộng, quy tắc dấu ngoặc với phân thức đại số trong tính toán và giải bài toán thực tiễn.",
        ],
        "definition": "Một phân thức đại số (hay nói gọn là phân thức) là một biểu thức có dạng $\\frac{A}{B}$, trong đó $A, B$ là những đa thức và $B$ khác đa thức $0$. $A$ được gọi là tử thức (hay tử), $B$ được gọi là mẫu thức (hay mẫu).",
        "theory": (
            "### Bài 21. Phân thức đại số\n"
            "- Hai phân thức $\\frac{A}{B}$ và $\\frac{C}{D}$ gọi là bằng nhau nếu $A \\cdot D = B \\cdot C$. Điều kiện xác định của phân thức $\\frac{A}{B}$ là điều kiện của biến để giá trị của mẫu thức $B$ khác $0$.\n"
            "### Bài 22. Tính chất cơ bản của phân thức đại số\n"
            "- Nếu nhân cả tử và mẫu của một phân thức với cùng một đa thức khác đa thức $0$ thì được một phân thức bằng phân thức đã cho. Nếu chia cả tử và mẫu của một phân thức cho một nhân tử chung của chúng thì được một phân thức bằng phân thức đã cho. Muốn rút gọn một phân thức, ta phân tích tử và mẫu thành nhân tử rồi chia cả tử và mẫu cho nhân tử chung. Muốn quy đồng mẫu thức nhiều phân thức, ta tìm mẫu thức chung (MTC) rồi nhân tử và mẫu của mỗi phân thức với nhân tử phụ tương ứng.\n"
            "### Bài 23. Phép cộng và phép trừ phân thức đại số\n"
            "- Cùng mẫu: cộng (trừ) các tử thức và giữ nguyên mẫu thức. Khác mẫu: quy đồng mẫu thức rồi cộng (trừ) các phân thức có cùng mẫu vừa tìm được. Phân thức đối của $\\frac{A}{B}$ kí hiệu là $-\\frac{A}{B} = \\frac{-A}{B} = \\frac{A}{-B}$.\n"
            "### Bài 24. Phép nhân và phép chia phân thức đại số\n"
            "- Muốn nhân hai phân thức, ta nhân các tử thức với nhau và nhân các mẫu thức với nhau. Muốn chia phân thức $\\frac{A}{B}$ cho phân thức $\\frac{C}{D}$ khác $0$, ta nhân $\\frac{A}{B}$ với phân thức nghịch đảo $\\frac{D}{C}$."
        ),
        "formulas": [
            G("Hai phân thức bằng nhau và tính chất cơ bản", F("Hai phân thức bằng nhau ($B, D \\neq 0$)", "$\\frac{A}{B} = \\frac{C}{D} \\iff A \\cdot D = B \\cdot C$"), F("Tính chất cơ bản ($M \\neq 0$; $N$ là nhân tử chung)", "$\\frac{A}{B} = \\frac{A \\cdot M}{B \\cdot M}; \\quad \\frac{A}{B} = \\frac{A : N}{B : N}$"), F("Quy tắc đổi dấu", "$\\frac{A}{B} = \\frac{-A}{-B} = -\\frac{-A}{B} = -\\frac{A}{-B}$")),
            G("Các phép toán trên phân thức đại số", F("Cộng, trừ hai phân thức cùng mẫu", "$\\frac{A}{M} \\pm \\frac{B}{M} = \\frac{A \\pm B}{M}$"), F("Nhân hai phân thức", "$\\frac{A}{B} \\cdot \\frac{C}{D} = \\frac{A \\cdot C}{B \\cdot D}$"), F("Chia hai phân thức ($\\frac{C}{D} \\neq 0$)", "$\\frac{A}{B} : \\frac{C}{D} = \\frac{A}{B} \\cdot \\frac{D}{C} = \\frac{A \\cdot D}{B \\cdot C}$")),
        ],
        "example": "Cho biểu thức $P = \\left(\\frac{1}{x - 2} + \\frac{1}{x + 2}\\right) \\cdot \\frac{x^2 - 4}{2x}$. Tìm điều kiện xác định, rút gọn $P$ và tính giá trị của $P$ tại $x = 5$.",
        "example_answer": "Điều kiện xác định của biểu thức: $x - 2 \\neq 0, x + 2 \\neq 0$ và $2x \\neq 0 \\iff x \\notin \\{0; 2; -2\\}$. Rút gọn: $P = \\frac{(x + 2) + (x - 2)}{(x - 2)(x + 2)} \\cdot \\frac{(x - 2)(x + 2)}{2x} = \\frac{2x}{x^2 - 4} \\cdot \\frac{x^2 - 4}{2x} = 1$. Tại $x = 5$ (thỏa mãn ĐKXĐ), giá trị của $P$ là $1$.",
        "real_life": "Phân thức đại số xuất hiện trong các công thức tính vận tốc trung bình trên nhiều chặng đường, năng suất công việc chung, điện trở tương đương của mạch điện song song và nồng độ dung dịch hóa học.",
        "quiz": [
            mcq("biet", "Điều kiện xác định của phân thức $\\frac{2x + 1}{x - 3}$ là:", ["$x \\neq 3$", "$x \\neq -3$", "$x \\neq -\\frac{1}{2}$", "$x > 3$"], 0, "Phân thức xác định khi mẫu thức khác $0$, tức là $x - 3 \\neq 0 \\iff x \\neq 3$."),
            mcq("biet", "Phân thức nào sau đây bằng với phân thức $\\frac{x}{x + 2}$ (với $x \\neq \\pm 2$)?", ["$\\frac{x(x - 2)}{x^2 - 4}$", "$\\frac{x^2}{x + 2}$", "$\\frac{x - 2}{x^2 - 4}$", "$\\frac{2x}{x + 4}$"], 0, "Nhân cả tử và mẫu của $\\frac{x}{x + 2}$ với $(x - 2) \\neq 0$ ta được $\\frac{x(x - 2)}{(x + 2)(x - 2)} = \\frac{x(x - 2)}{x^2 - 4}$."),
            mcq("biet", "Phân thức đối của phân thức $\\frac{3 - x}{x + 1}$ là:", ["$\\frac{x - 3}{x + 1}$", "$\\frac{x + 1}{3 - x}$", "$\\frac{-3 - x}{x + 1}$", "$\\frac{3 + x}{x + 1}$"], 0, "Phân thức đối của $\\frac{3 - x}{x + 1}$ là $-\\frac{3 - x}{x + 1} = \\frac{-(3 - x)}{x + 1} = \\frac{x - 3}{x + 1}$."),
            mcq("biet", "Kết quả rút gọn phân thức $\\frac{6x^2y^3}{9xy^4}$ (với $x \\neq 0, y \\neq 0$) là:", ["$\\frac{2x}{3y}$", "$\\frac{2y}{3x}$", "$\\frac{3x}{2y}$", "$\\frac{2x^2}{3y}$"], 0, "Chia cả tử và mẫu cho nhân tử chung $3xy^3$: $\\frac{6x^2y^3 : (3xy^3)}{9xy^4 : (3xy^3)} = \\frac{2x}{3y}$."),
            mcq("hieu", "Kết quả của phép cộng $\\frac{2x}{x + 3} + \\frac{6}{x + 3}$ (với $x \\neq -3$) sau khi rút gọn là:", ["$2$", "$2x + 6$", "$\\frac{2}{x + 3}$", "$\\frac{12x}{x + 3}$"], 0, "Ta có $\\frac{2x}{x + 3} + \\frac{6}{x + 3} = \\frac{2x + 6}{x + 3} = \\frac{2(x + 3)}{x + 3} = 2$."),
            mcq("hieu", "Thực hiện phép chia $\\frac{x^2 - 9}{x + 1} : \\frac{x - 3}{2x + 2}$ (với $x \\neq -1, x \\neq 3$) ta được kết quả là:", ["$2(x + 3)$", "$2(x - 3)$", "$\\frac{x + 3}{2}$", "$\\frac{(x - 3)^2}{2(x + 1)^2}$"], 0, "Ta có $\\frac{(x - 3)(x + 3)}{x + 1} \\cdot \\frac{2(x + 1)}{x - 3} = 2(x + 3)$."),
            tf4("hieu", "Cho phân thức $A = \\frac{x^2 - 4x + 4}{x^2 - 4}$. Xét tính đúng sai của các khẳng định sau:", ["a) Điều kiện xác định của phân thức $A$ là $x \\neq 2$ và $x \\neq -2$.", "b) Rút gọn phân thức $A$ ta được $\\frac{x - 2}{x + 2}$.", "c) Tại $x = 4$, giá trị của phân thức $A$ bằng $\\frac{1}{3}$.", "d) Giá trị của phân thức $A$ bằng $0$ khi $x = 2$."], [True, True, True, False], "a) Đúng vì $x^2 - 4 \\neq 0 \\iff (x - 2)(x + 2) \\neq 0 \\iff x \\neq \\pm 2$. b) Đúng vì $A = \\frac{(x - 2)^2}{(x - 2)(x + 2)} = \\frac{x - 2}{x + 2}$. c) Đúng vì tại $x = 4$ (thỏa mãn ĐKXĐ), $A = \\frac{4 - 2}{4 + 2} = \\frac{2}{6} = \\frac{1}{3}$. d) Sai vì tại $x = 2$ phân thức không xác định."),
            tf4("hieu", "Cho biểu thức $B = \\frac{x}{x - 1} + \\frac{1}{x + 1} + \\frac{2}{x^2 - 1}$ với $x \\neq \\pm 1$. Xét tính đúng sai của các khẳng định sau:", ["a) Mẫu thức chung của ba phân thức trong biểu thức $B$ là $(x - 1)(x + 1)$.", "b) Sau khi quy đồng mẫu thức $(x - 1)(x + 1)$, tử thức thu gọn là $(x - 1)^2$.", "c) Rút gọn biểu thức $B$ ta được $B = \\frac{x + 1}{x - 1}$.", "d) Khi $x = 3$, giá trị của biểu thức $B$ bằng $2$."], [True, False, True, True], "a) Đúng vì $x^2 - 1 = (x - 1)(x + 1)$. b) Sai vì tử thức sau khi quy đồng là $x(x + 1) + (x - 1) + 2 = x^2 + 2x + 1 = (x + 1)^2$. c) Đúng vì $B = \\frac{(x + 1)^2}{(x - 1)(x + 1)} = \\frac{x + 1}{x - 1}$. d) Đúng vì tại $x = 3$, $B = \\frac{3 + 1}{3 - 1} = 2$."),
            mcq("vandung", "Một ca nô đi xuôi dòng một quãng sông dài $40\\text{ km}$ rồi ngược dòng quãng sông đó. Biết vận tốc thực của ca nô là $x\\text{ (km/h)}$ ($x > 4$) và vận tốc dòng nước là $4\\text{ km/h}$. Phân thức biểu thị tổng thời gian ca nô đi và về là:", ["$\\frac{80x}{x^2 - 16}$", "$\\frac{80}{x^2 - 16}$", "$\\frac{320}{x^2 - 16}$", "$\\frac{40x}{x^2 - 16}$"], 0, "Thời gian xuôi dòng là $\\frac{40}{x + 4}$ (giờ), thời gian ngược dòng là $\\frac{40}{x - 4}$ (giờ). Tổng thời gian là $\\frac{40}{x + 4} + \\frac{40}{x - 4} = \\frac{40(x - 4) + 40(x + 4)}{x^2 - 16} = \\frac{80x}{x^2 - 16}$ (giờ)."),
            short("vandung", "Cho biểu thức $M = \\frac{x^2 + 2x}{x + 2} + \\frac{x^2 - 9}{x - 3}$ (với $x \\neq -2, x \\neq 3$). Tính giá trị của $M$ tại $x = 10$.", ["23"], "Với $x \\neq -2, x \\neq 3$, ta có $M = \\frac{x(x + 2)}{x + 2} + \\frac{(x - 3)(x + 3)}{x - 3} = x + (x + 3) = 2x + 3$. Tại $x = 10$, giá trị của $M$ là $2 \\cdot 10 + 3 = 23$."),
        ],
    },
    {
        "topic": "l8-ch07-phuong-trinh-bac-nhat-va-ham-so-bac-nhat",
        "title": "Phương trình bậc nhất và hàm số bậc nhất",
        "icon": "📈",
        "description": "Phương trình bậc nhất một ẩn, giải bài toán bằng cách lập phương trình, hàm số bậc nhất, đồ thị và hệ số góc của đường thẳng",
        "requirements": [
            "Hiểu được khái niệm phương trình bậc nhất một ẩn và cách giải phương trình bậc nhất một ẩn.",
            "Giải quyết được một số vấn đề thực tiễn gắn với phương trình bậc nhất (ví dụ: các bài toán chuyển động, năng suất, phần trăm, tài chính).",
            "Nhận biết được những mô hình thực tế dẫn đến khái niệm hàm số; tính được giá trị của hàm số khi biết giá trị của biến và xác định được tọa độ của một điểm trên mặt phẳng tọa độ.",
            "Thiết lập được bảng giá trị của hàm số bậc nhất $y = ax + b$ ($a \\neq 0$) và vẽ được đồ thị của hàm số bậc nhất.",
            "Nhận biết được khái niệm hệ số góc của đường thẳng $y = ax + b$ ($a \\neq 0$) và sử dụng hệ số góc để nhận biết vị trí tương đối của hai đường thẳng (song song, cắt nhau, trùng nhau).",
        ],
        "definition": "Phương trình dạng $ax + b = 0$ với $a, b$ là hai số đã cho và $a \\neq 0$ được gọi là phương trình bậc nhất một ẩn $x$. Hàm số bậc nhất là hàm số cho bởi công thức $y = ax + b$, trong đó $a, b$ là các số cho trước và $a \\neq 0$.",
        "theory": (
            "### Bài 25. Phương trình bậc nhất một ẩn\n"
            "- Phương trình bậc nhất một ẩn $ax + b = 0$ ($a \\neq 0$) luôn có một nghiệm duy nhất $x = -\\frac{b}{a}$. Ta sử dụng quy tắc chuyển vế và quy tắc nhân (chia) hai vế với cùng một số khác $0$ để giải phương trình.\n"
            "### Bài 26. Giải bài toán bằng cách lập phương trình\n"
            "- Gồm $3$ bước: Bước 1. Lập phương trình (chọn ẩn số và đặt điều kiện thích hợp cho ẩn; biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết; lập phương trình biểu thị mối quan hệ giữa các đại lượng); Bước 2. Giải phương trình; Bước 3. Kiểm tra điều kiện và kết luận.\n"
            "### Bài 27. Khái niệm hàm số và đồ thị của hàm số\n"
            "- Nếu đại lượng $y$ phụ thuộc vào đại lượng thay đổi $x$ sao cho với mỗi giá trị của $x$ ta luôn xác định được chỉ một giá trị tương ứng của $y$ thì $y$ được gọi là hàm số của $x$ và $x$ gọi là biến số. Đồ thị của hàm số $y = f(x)$ là tập hợp tất cả các điểm biểu diễn các cặp giá trị tương ứng $(x; y)$ trên mặt phẳng tọa độ $Oxy$.\n"
            "### Bài 28. Hàm số bậc nhất và đồ thị của hàm số bậc nhất\n"
            "- Đồ thị của hàm số bậc nhất $y = ax + b$ ($a \\neq 0$) là một đường thẳng cắt trục tung tại điểm có tung độ bằng $b$. Để vẽ đồ thị, ta xác định hai điểm phân biệt thuộc đồ thị rồi kẻ đường thẳng đi qua hai điểm đó.\n"
            "### Bài 29. Hệ số góc của đường thẳng\n"
            "- Số $a$ gọi là hệ số góc của đường thẳng $y = ax + b$ ($a \\neq 0$). Khi $a > 0$, góc tạo bởi đường thẳng với trục $Ox$ là góc nhọn; khi $a < 0$, góc đó là góc tù. Hai đường thẳng $y = ax + b$ và $y = a'x + b'$ ($a, a' \\neq 0$): song song khi $a = a', b \\neq b'$; trùng nhau khi $a = a', b = b'$; cắt nhau khi $a \\neq a'$."
        ),
        "formulas": [
            G("Phương trình bậc nhất một ẩn", F("Nghiệm của phương trình $ax + b = 0$ ($a \\neq 0$)", "$x = -\\frac{b}{a}$")),
            G("Hàm số bậc nhất và vị trí tương đối của hai đường thẳng", F("Công thức hàm số bậc nhất", "$y = ax + b \\quad (a \\neq 0)$"), F("Giao điểm với trục tung $Oy$ và trục hoành $Ox$", "$A(0; b), \\quad B\\left(-\\frac{b}{a}; 0\\right)$"), F("Hai đường thẳng $y = ax + b$ và $y = a'x + b'$ song song", "$a = a' \\quad \\text{và} \\quad b \\neq b'$"), F("Hai đường thẳng $y = ax + b$ và $y = a'x + b'$ cắt nhau", "$a \\neq a'$")),
        ],
        "example": "Cho hàm số bậc nhất $y = 2x - 4$ có đồ thị là đường thẳng $(d)$. Xác định hệ số góc của $(d)$, tìm tọa độ giao điểm của $(d)$ với hai trục tọa độ và tìm $m$ để đường thẳng $(d'): y = (m - 1)x + 3$ song song với $(d)$.",
        "example_answer": "Đường thẳng $(d): y = 2x - 4$ có hệ số góc $a = 2$. Cho $x = 0 \\implies y = -4$, giao điểm với trục $Oy$ là $A(0; -4)$. Cho $y = 0 \\implies 2x - 4 = 0 \\iff x = 2$, giao điểm với trục $Ox$ là $B(2; 0)$. Để $(d') \\parallel (d)$ thì $m - 1 = 2$ (và $3 \\neq -4$, luôn đúng) $\\iff m = 3$.",
        "real_life": "Phương trình và hàm số bậc nhất mô tả chính xác công thức tính cước phí taxi theo quãng đường, chuyển đổi nhiệt độ giữa độ Celsius (${}^\\circ\\text{C}$) và độ Fahrenheit (${}^\\circ\\text{F}$): $F = 1,8C + 32$, cũng như bài toán gửi tiết kiệm lãi đơn.",
        "quiz": [
            mcq("biet", "Phương trình nào dưới đây là phương trình bậc nhất một ẩn?", ["$3x - 9 = 0$", "$x^2 + 2x = 0$", "$0x + 5 = 0$", "$\\frac{2}{x} - 1 = 0$"], 0, "Phương trình $3x - 9 = 0$ có dạng $ax + b = 0$ với $a = 3 \\neq 0, b = -9$."),
            mcq("biet", "Nghiệm của phương trình $4x - 12 = 0$ là:", ["$x = 3$", "$x = -3$", "$x = 4$", "$x = 8$"], 0, "Ta có $4x - 12 = 0 \\iff 4x = 12 \\iff x = 3$."),
            mcq("biet", "Hệ số góc của đường thẳng $y = -3x + 5$ là:", ["$-3$", "$5$", "$3$", "$-5$"], 0, "Đường thẳng $y = ax + b$ ($a \\neq 0$) có hệ số góc là $a = -3$."),
            mcq("biet", "Hai đường thẳng $y = 2x + 3$ và $y = 2x - 1$ có vị trí tương đối là:", ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], 0, "Hai đường thẳng có cùng hệ số góc $a = a' = 2$ và $b = 3 \\neq b' = -1$ nên song song với nhau."),
            mcq("hieu", "Nghiệm của phương trình $\\frac{2x - 1}{3} - \\frac{x + 2}{2} = 1$ là:", ["$x = 14$", "$x = 8$", "$x = 10$", "$x = 2$"], 0, "Quy đồng mẫu số chung là $6$: $2(2x - 1) - 3(x + 2) = 6 \\iff 4x - 2 - 3x - 6 = 6 \\iff x - 8 = 6 \\iff x = 14$."),
            mcq("hieu", "Biết đồ thị hàm số $y = ax + 3$ đi qua điểm $M(2; 7)$. Giá trị của hệ số $a$ là:", ["$a = 2$", "$a = 5$", "$a = -2$", "$a = 3$"], 0, "Thay $x = 2, y = 7$ vào $y = ax + 3$ ta được $7 = 2a + 3 \\iff 2a = 4 \\iff a = 2$."),
            tf4("hieu", "Cho hàm số bậc nhất $y = f(x) = -2x + 6$ có đồ thị là đường thẳng $(d)$. Xét tính đúng sai của các khẳng định sau:", ["a) Tại $x = -1$, giá trị của hàm số là $f(-1) = 8$.", "b) Đường thẳng $(d)$ cắt trục tung $Oy$ tại điểm có tọa độ $(0; 6)$.", "c) Đường thẳng $(d)$ cắt trục hoành $Ox$ tại điểm có tọa độ $(3; 0)$.", "d) Góc tạo bởi đường thẳng $(d)$ và trục $Ox$ là góc nhọn."], [True, True, True, False], "a) Đúng vì $f(-1) = -2 \\cdot (-1) + 6 = 8$. b) Đúng vì thay $x = 0$ được $y = 6$. c) Đúng vì cho $y = 0 \\implies -2x + 6 = 0 \\iff x = 3$. d) Sai vì hệ số góc $a = -2 < 0$ nên góc tạo bởi đường thẳng $(d)$ và trục $Ox$ là góc tù."),
            tf4("hieu", "Một ô tô khởi hành từ $A$ đến $B$ với vận tốc $50\\text{ km/h}$. Sau khi đến $B$, ô tô quay về $A$ trên cùng quãng đường đó với vận tốc $40\\text{ km/h}$. Biết tổng thời gian cả đi và về là $4,5$ giờ. Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x > 0$). Xét tính đúng sai của các khẳng định sau:", ["a) Thời gian ô tô đi từ $A$ đến $B$ là $\\frac{x}{50}$ (giờ).", "b) Thời gian ô tô đi từ $B$ về $A$ là $\\frac{x}{40}$ (giờ).", "c) Phương trình biểu thị bài toán là $\\frac{x}{50} + \\frac{x}{40} = 4,5$.", "d) Độ dài quãng đường $AB$ bằng $90\\text{ km}$."], [True, True, True, False], "a) Đúng theo công thức $t = \\frac{s}{v}$. b) Đúng vì vận tốc lúc về là $40\\text{ km/h}$. c) Đúng vì tổng thời gian đi và về là $4,5$ giờ. d) Sai vì giải phương trình $\\frac{4x + 5x}{200} = 4,5 \\iff 9x = 900 \\iff x = 100\\text{ km}$."),
            mcq("vandung", "Một cửa hàng thời trang giảm giá $20\\%$ cho tất cả các mặt hàng so với giá niêm yết. Bạn An mua một chiếc áo khoác tại cửa hàng và phải trả $360\\,000$ đồng. Hỏi giá niêm yết ban đầu của chiếc áo khoác đó là bao nhiêu?", ["$450\\,000$ đồng", "$432\\,000$ đồng", "$400\\,000$ đồng", "$480\\,000$ đồng"], 0, "Gọi giá niêm yết là $x$ (đồng, $x > 0$). Sau khi giảm $20\\%$, giá bán là $(1 - 0,2)x = 0,8x$. Ta có phương trình $0,8x = 360\\,000 \\iff x = 450\\,000$ (đồng)."),
            short("vandung", "Cho hai đường thẳng $(d_1): y = 3x - 2$ và $(d_2): y = x + 4$. Gọi $I(x_0; y_0)$ là giao điểm của $(d_1)$ và $(d_2)$. Tính giá trị biểu thức $T = x_0 + y_0$.", ["10"], "Hoành độ giao điểm $I$ là nghiệm của phương trình $3x - 2 = x + 4 \\iff 2x = 6 \\iff x_0 = 3$. Suy ra $y_0 = 3 + 4 = 7$. Vậy $T = x_0 + y_0 = 3 + 7 = 10$."),
        ],
    },
    {
        "topic": "l8-ch08-mo-dau-ve-tinh-xac-suat-cua-bien-co",
        "title": "Mở đầu về tính xác suất của biến cố",
        "icon": "🎲",
        "description": "Kết quả có thể và kết quả thuận lợi, cách tính xác suất của biến cố bằng tỉ số, mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng",
        "requirements": [
            "Nhận biết được kết quả có thể và kết quả thuận lợi cho một biến cố trong các trò chơi, thí nghiệm đơn giản.",
            "Sử dụng được tỉ số để mô tả xác suất của một biến cố ngẫu nhiên trong một số ví dụ đơn giản có các kết quả có thể là đồng khả năng.",
            "Nhận biết được xác suất thực nghiệm của một biến cố trong một loạt phép thử lặp lại.",
            "Nhận biết được mối liên hệ giữa xác suất thực nghiệm của một biến cố với xác suất của biến cố đó khi số lần thực hiện phép thử ngày càng lớn và vận dụng để ước lượng quy mô quần thể.",
        ],
        "definition": "Giả sử rằng các kết quả có thể của một hành động hay thực nghiệm là đồng khả năng. Khi đó, xác suất của biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số giữa số kết quả thuận lợi cho biến cố $E$ và tổng số kết quả có thể.",
        "theory": (
            "### Bài 30. Kết quả có thể và kết quả thuận lợi\n"
            "- Một kết quả của hành động, thực nghiệm làm cho biến cố $E$ xảy ra được gọi là kết quả thuận lợi cho biến cố $E$.\n"
            "### Bài 31. Cách tính xác suất của biến cố bằng tỉ số\n"
            "- Nếu tất cả $n$ kết quả có thể của phép thử là đồng khả năng và có $k$ kết quả thuận lợi cho biến cố $E$ thì xác suất của biến cố $E$ là $P(E) = \\frac{k}{n}$ ($0 \\le P(E) \\le 1$).\n"
            "### Bài 32. Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng\n"
            "- Giả sử trong $n$ lần thực nghiệm hoặc quan sát mà biến cố $E$ xảy ra $k$ lần thì xác suất thực nghiệm của biến cố $E$ bằng $\\frac{k}{n}$. Khi số lần thực nghiệm $n$ ngày càng lớn thì xác suất thực nghiệm của biến cố $E$ ngày càng gần với xác suất lí thuyết $P(E)$ của biến cố đó."
        ),
        "formulas": [
            G("Xác suất lí thuyết và xác suất thực nghiệm", F("Xác suất của biến cố $E$ (đồng khả năng)", "$P(E) = \\frac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số kết quả có thể}} = \\frac{k}{n}$"), F("Xác suất thực nghiệm của biến cố $E$ trong $N$ phép thử", "$P_{\\text{tn}}(E) = \\frac{\\text{Số lần } E \\text{ xảy ra}}{N}$"), F("Xác suất của biến cố đối $\\overline{E}$", "$P(\\overline{E}) = 1 - P(E)$")),
        ],
        "example": "Một hộp có $12$ tấm thẻ cùng loại được đánh số từ $1$ đến $12$. Rút ngẫu nhiên một tấm thẻ trong hộp. Tính xác suất của biến cố $A$: 'Số ghi trên thẻ rút được là số nguyên tố'.",
        "example_answer": "Tổng số kết quả có thể đồng khả năng khi rút một thẻ là $n = 12$. Các kết quả thuận lợi cho biến cố $A$ là các thẻ ghi số nguyên tố: $2, 3, 5, 7, 11$ (có $k = 5$ kết quả thuận lợi). Vậy xác suất của biến cố $A$ là $P(A) = \\frac{5}{12}$.",
        "real_life": "Xác suất thực nghiệm được ứng dụng để kiểm tra tỉ lệ sản phẩm đạt chuẩn trong dây chuyền công nghiệp, ước lượng số lượng cá trong hồ bằng phương pháp bắt - đánh dấu - thả lại và dự báo rủi ro bảo hiểm.",
        "quiz": [
            mcq("biet", "Gieo một con xúc xắc cân đối và đồng chất một lần. Số kết quả có thể xảy ra đối với mặt xuất hiện của xúc xắc là:", ["$6$", "$1$", "$3$", "$12$"], 0, "Con xúc xắc có $6$ mặt từ $1$ chấm đến $6$ chấm nên có $6$ kết quả có thể."),
            mcq("biet", "Một hộp có $10$ quả bóng cùng kích thước được đánh số từ $1$ đến $10$. Lấy ngẫu nhiên một quả bóng. Số kết quả thuận lợi cho biến cố 'Lấy được quả bóng ghi số chia hết cho $3$' là:", ["$3$", "$4$", "$2$", "$5$"], 0, "Các số từ $1$ đến $10$ chia hết cho $3$ là $3, 6, 9$ nên có $3$ kết quả thuận lợi."),
            mcq("biet", "Gieo một con xúc xắc cân đối một lần. Xác suất của biến cố 'Số chấm xuất hiện trên con xúc xắc là số chẵn' bằng:", ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"], 0, "Có $3$ kết quả thuận lợi ($2, 4, 6$) trong tổng số $6$ kết quả đồng khả năng, nên xác suất là $\\frac{3}{6} = \\frac{1}{2}$."),
            mcq("biet", "Khi tung một đồng xu $50$ lần liên tiếp, bạn Nam thấy có $28$ lần xuất hiện mặt Sấp (S). Xác suất thực nghiệm của biến cố 'Xuất hiện mặt Sấp' là:", ["$\\frac{14}{25}$", "$\\frac{11}{25}$", "$\\frac{1}{2}$", "$\\frac{25}{14}$"], 0, "Xác suất thực nghiệm của biến cố xuất hiện mặt Sấp là $\\frac{28}{50} = \\frac{14}{25}$."),
            mcq("hieu", "Một túi đựng $5$ viên bi đỏ, $4$ viên bi xanh và $6$ viên bi vàng có cùng kích thước và khối lượng. Lấy ngẫu nhiên một viên bi từ túi. Xác suất của biến cố 'Viên bi lấy ra không phải màu đỏ' là:", ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "$\\frac{4}{15}$", "$\\frac{2}{5}$"], 0, "Tổng số viên bi là $5 + 4 + 6 = 15$. Số viên bi không phải màu đỏ là $4 + 6 = 10$. Xác suất cần tìm là $\\frac{10}{15} = \\frac{2}{3}$."),
            mcq("hieu", "Chọn ngẫu nhiên một số tự nhiên có hai chữ số từ $10$ đến $29$. Xác suất của biến cố 'Số được chọn là số chính phương' là:", ["$\\frac{1}{10}$", "$\\frac{3}{20}$", "$\\frac{1}{20}$", "$\\frac{1}{5}$"], 0, "Từ $10$ đến $29$ có $29 - 10 + 1 = 20$ số. Trong đó có $2$ số chính phương là $16 = 4^2$ và $25 = 5^2$. Xác suất là $\\frac{2}{20} = \\frac{1}{10}$."),
            tf4("hieu", "Một hộp có $20$ tấm thẻ cùng loại được đánh số từ $1$ đến $20$. Rút ngẫu nhiên một tấm thẻ trong hộp. Xét tính đúng sai của các khẳng định sau:", ["a) Có $20$ kết quả có thể và các kết quả này là đồng khả năng.", "b) Biến cố $A$: 'Số ghi trên thẻ chia hết cho $5$' có $4$ kết quả thuận lợi.", "c) Xác suất của biến cố $A$ là $P(A) = \\frac{1}{4}$.", "d) Xác suất của biến cố $B$: 'Số ghi trên thẻ là số nguyên tố' là $P(B) = \\frac{2}{5}$."], [True, True, False, True], "a) Đúng vì các thẻ cùng loại đánh số từ $1$ đến $20$. b) Đúng vì các số chia hết cho $5$ là $5, 10, 15, 20$ ($4$ kết quả). c) Sai vì $P(A) = \\frac{4}{20} = \\frac{1}{5}$. d) Đúng vì các số nguyên tố từ $1$ đến $20$ là $2, 3, 5, 7, 11, 13, 17, 19$ ($8$ số), nên $P(B) = \\frac{8}{20} = \\frac{2}{5}$."),
            tf4("hieu", "Một nhà máy kiểm tra ngẫu nhiên $500$ chiếc bóng đèn vừa sản xuất thì phát hiện có $10$ chiếc bị lỗi. Xét tính đúng sai của các khẳng định sau:", ["a) Số bóng đèn đạt chuẩn trong mẫu kiểm tra là $490$ chiếc.", "b) Xác suất thực nghiệm của biến cố 'Bóng đèn bị lỗi' là $0,02$.", "c) Xác suất thực nghiệm của biến cố 'Bóng đèn đạt chuẩn' là $0,98$.", "d) Trong lô hàng $10\\,000$ chiếc bóng đèn cùng loại, ước lượng có khoảng $2\\,000$ chiếc bị lỗi."], [True, True, True, False], "a) Đúng vì $500 - 10 = 490$. b) Đúng vì $\\frac{10}{500} = 0,02$. c) Đúng vì $\\frac{490}{500} = 0,98$. d) Sai vì số bóng đèn bị lỗi ước lượng khoảng $10\\,000 \\cdot 0,02 = 200$ chiếc."),
            mcq("vandung", "Để ước lượng số cá rô phi trong một hồ nuôi, người ta bắt lên $100$ con cá, đánh dấu rồi thả lại xuống hồ. Sau một thời gian cho cá bơi đều, người ta bắt ngẫu nhiên $80$ con cá thì thấy có $16$ con có đánh dấu. Ước lượng số cá rô phi trong hồ là khoảng:", ["$500$ con", "$800$ con", "$400$ con", "$640$ con"], 0, "Gọi tổng số cá trong hồ là $N$. Tỉ lệ cá có đánh dấu trong hồ là $\\frac{100}{N}$, xấp xỉ xác suất thực nghiệm $\\frac{16}{80} = \\frac{1}{5}$. Suy ra $\\frac{100}{N} \\approx \\frac{1}{5} \\implies N \\approx 500$ (con)."),
            short("vandung", "Trong một túi có một số viên bi đỏ và $18$ viên bi xanh cùng kích thước. Lấy ngẫu nhiên một viên bi từ túi, biết rằng xác suất lấy được viên bi đỏ là $\\frac{2}{5}$. Hỏi trong túi có bao nhiêu viên bi đỏ?", ["12"], "Gọi số viên bi đỏ là $x$ ($x \\in \\mathbb{N}^*$). Tổng số viên bi là $x + 18$. Ta có $\\frac{x}{x + 18} = \\frac{2}{5} \\iff 5x = 2x + 36 \\iff 3x = 36 \\iff x = 12$."),
        ],
    },
    {
        "topic": "l8-ch09-tam-giac-dong-dang",
        "title": "Tam giác đồng dạng",
        "icon": "🔺",
        "description": "Hai tam giác đồng dạng, ba trường hợp đồng dạng của hai tam giác, định lí Pythagore, tam giác vuông đồng dạng và hình đồng dạng",
        "requirements": [
            "Mô tả được định nghĩa của hai tam giác đồng dạng và tính chất của hai tam giác đồng dạng.",
            "Giải thích được các trường hợp đồng dạng của hai tam giác (cạnh - cạnh - cạnh, cạnh - góc - cạnh, góc - góc).",
            "Giải thích được định lí Pythagore (thuận và đảo) và tính được độ dài cạnh trong tam giác vuông bằng cách sử dụng định lí Pythagore.",
            "Giải thích được các trường hợp đồng dạng của hai tam giác vuông (góc nhọn, hai cạnh góc vuông, cạnh huyền - cạnh góc vuông).",
            "Nhận biết được hình đồng dạng phối cảnh (hình vị tự), hình đồng dạng và vẻ đẹp trong tự nhiên, nghệ thuật, kiến trúc.",
            "Giải quyết được một số vấn đề thực tiễn gắn với việc vận dụng kiến thức về hai tam giác đồng dạng và định lí Pythagore.",
        ],
        "definition": "Tam giác $A'B'C'$ gọi là đồng dạng với tam giác $ABC$, kí hiệu $\\triangle A'B'C' \\backsim \\triangle ABC$, nếu các góc tương ứng bằng nhau ($\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = \\widehat{C}$) và các cạnh tương ứng tỉ lệ ($\\frac{A'B'}{AB} = \\frac{B'C'}{BC} = \\frac{A'C'}{AC} = k$, với $k$ là tỉ số đồng dạng).",
        "theory": (
            "### Bài 33. Hai tam giác đồng dạng\n"
            "- Nếu $\\triangle A'B'C' \\backsim \\triangle ABC$ theo tỉ số đồng dạng $k$ thì $\\triangle ABC \\backsim \\triangle A'B'C'$ theo tỉ số $\\frac{1}{k}$. Một đường thẳng cắt hai cạnh của một tam giác và song song với cạnh còn lại sẽ tạo thành một tam giác mới đồng dạng với tam giác đã cho.\n"
            "### Bài 34. Ba trường hợp đồng dạng của hai tam giác\n"
            "- Trường hợp 1 (c.c.c): Ba cạnh của tam giác này tỉ lệ với ba cạnh của tam giác kia. Trường hợp 2 (c.g.c): Hai cạnh của tam giác này tỉ lệ với hai cạnh của tam giác kia và hai góc tạo bởi các cặp cạnh đó bằng nhau. Trường hợp 3 (g.g): Hai góc của tam giác này lần lượt bằng hai góc của tam giác kia.\n"
            "### Bài 35. Định lí Pythagore và ứng dụng\n"
            "- Trong một tam giác vuông, bình phương của cạnh huyền bằng tổng các bình phương của hai cạnh góc vuông. Định lí Pythagore đảo: Nếu một tam giác có bình phương của một cạnh bằng tổng các bình phương của hai cạnh kia thì tam giác đó là tam giác vuông.\n"
            "### Bài 36. Các trường hợp đồng dạng của hai tam giác vuông\n"
            "- Hai tam giác vuông đồng dạng nếu: (1) có một góc nhọn bằng nhau; hoặc (2) có hai cạnh góc vuông tương ứng tỉ lệ; hoặc (3) có cạnh huyền và một cạnh góc vuông của tam giác vuông này tỉ lệ với cạnh huyền và một cạnh góc vuông của tam giác vuông kia. Tỉ số hai đường cao tương ứng bằng tỉ số đồng dạng; tỉ số diện tích bằng bình phương tỉ số đồng dạng.\n"
            "### Bài 37. Hình đồng dạng\n"
            "- Cặp hình phóng to - thu nhỏ theo cùng tỉ lệ $k$ được gọi là các hình đồng dạng phối cảnh; hình $H'$ gọi là đồng dạng với hình $H$ nếu $H'$ bằng một hình đồng dạng phối cảnh với $H$."
        ),
        "formulas": [
            G("Hai tam giác đồng dạng ($\\triangle A'B'C' \\backsim \\triangle ABC$ theo tỉ số $k$)", F("Tỉ số các cạnh tương ứng", "$\\frac{A'B'}{AB} = \\frac{B'C'}{BC} = \\frac{A'C'}{AC} = k$"), F("Tỉ số chu vi và tỉ số hai đường cao tương ứng", "$\\frac{P_{A'B'C'}}{P_{ABC}} = \\frac{h'}{h} = k$"), F("Tỉ số diện tích của hai tam giác đồng dạng", "$\\frac{S_{A'B'C'}}{S_{ABC}} = k^2$")),
            G("Định lí Pythagore trong tam giác vuông ($\\triangle ABC$ vuông tại $A$)", F("Hệ thức Pythagore", "$BC^2 = AB^2 + AC^2$"), F("Tính cạnh huyền và cạnh góc vuông", "$BC = \\sqrt{AB^2 + AC^2}; \\quad AB = \\sqrt{BC^2 - AC^2}$")),
        ],
        "example": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Kẻ đường cao $AH$ ($H \\in BC$). Tính độ dài cạnh $BC$ và đường cao $AH$.",
        "example_answer": "Áp dụng định lí Pythagore trong $\\triangle ABC$ vuông tại $A$: $BC^2 = AB^2 + AC^2 = 6^2 + 8^2 = 100 \\implies BC = 10\\text{ cm}$. Xét hai tam giác vuông $\\triangle HBA$ và $\\triangle ABC$ có chung góc nhọn $B$, suy ra $\\triangle HBA \\backsim \\triangle ABC$ (g.g). Do đó $\\frac{AH}{AC} = \\frac{AB}{BC} \\implies AH = \\frac{AB \\cdot AC}{BC} = \\frac{6 \\cdot 8}{10} = 4,8\\text{ cm}$.",
        "real_life": "Tam giác đồng dạng và định lí Pythagore là công cụ cốt lõi trong trắc địa, kiến trúc và thiết kế bản vẽ tỉ lệ, giúp tính khoảng cách đường chim bay, kiểm tra góc vuông công trình (bộ ba $3 - 4 - 5$) và đo chiều cao tháp bằng gương hoặc bóng nắng.",
        "quiz": [
            mcq("biet", "Nếu $\\triangle A'B'C' \\backsim \\triangle ABC$ theo tỉ số đồng dạng $k = \\frac{2}{5}$ thì tỉ số chu vi của $\\triangle A'B'C'$ và $\\triangle ABC$ bằng:", ["$\\frac{2}{5}$", "$\\frac{5}{2}$", "$\\frac{4}{25}$", "$\\frac{25}{4}$"], 0, "Tỉ số chu vi của hai tam giác đồng dạng bằng chính tỉ số đồng dạng $k = \\frac{2}{5}$."),
            mcq("biet", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}$ và $AC = 12\\text{ cm}$. Độ dài cạnh huyền $BC$ là:", ["$13\\text{ cm}$", "$17\\text{ cm}$", "$\\sqrt{119}\\text{ cm}$", "$15\\text{ cm}$"], 0, "Theo định lí Pythagore: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{5^2 + 12^2} = \\sqrt{169} = 13\\text{ cm}$."),
            mcq("biet", "Bộ ba số đo nào dưới đây là độ dài ba cạnh của một tam giác vuông?", ["$9\\text{ cm}, 12\\text{ cm}, 15\\text{ cm}$", "$4\\text{ cm}, 5\\text{ cm}, 6\\text{ cm}$", "$6\\text{ cm}, 7\\text{ cm}, 9\\text{ cm}$", "$5\\text{ cm}, 10\\text{ cm}, 12\\text{ cm}$"], 0, "Ta có $9^2 + 12^2 = 81 + 144 = 225 = 15^2$, nên theo định lí Pythagore đảo đó là tam giác vuông."),
            mcq("biet", "Nếu $\\triangle MNP \\backsim \\triangle DEF$ theo tỉ số đồng dạng $k = 3$ thì tỉ số diện tích $\\frac{S_{MNP}}{S_{DEF}}$ bằng:", ["$9$", "$3$", "$\\frac{1}{9}$", "$6$"], 0, "Tỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng: $k^2 = 3^2 = 9$."),
            mcq("hieu", "Cho $\\triangle ABC$ và $\\triangle DEF$ có $\\widehat{A} = \\widehat{D} = 70^\\circ, AB = 4\\text{ cm}, AC = 6\\text{ cm}, DE = 6\\text{ cm}$. Để $\\triangle ABC \\backsim \\triangle DEF$ theo trường hợp cạnh - góc - cạnh thì độ dài cạnh $DF$ phải bằng:", ["$9\\text{ cm}$", "$4\\text{ cm}$", "$8\\text{ cm}$", "$12\\text{ cm}$"], 0, "Để $\\triangle ABC \\backsim \\triangle DEF$ (c.g.c) với $\\widehat{A} = \\widehat{D}$ thì $\\frac{AB}{DE} = \\frac{AC}{DF} \\implies \\frac{4}{6} = \\frac{6}{DF} \\implies DF = 9\\text{ cm}$."),
            mcq("hieu", "Một chiếc thang dài $5\\text{ m}$ dựa vào một bức tường thẳng đứng, chân thang cách chân tường $3\\text{ m}$. Hỏi đầu trên của thang chạm tường ở độ cao bao nhiêu mét so với mặt đất?", ["$4\\text{ m}$", "$2\\text{ m}$", "$\\sqrt{34}\\text{ m}$", "$3,5\\text{ m}$"], 0, "Áp dụng định lí Pythagore: $h = \\sqrt{5^2 - 3^2} = \\sqrt{16} = 4\\text{ m}$."),
            tf4("hieu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9\\text{ cm}, AC = 12\\text{ cm}$ và đường cao $AH$ ($H \\in BC$). Xét tính đúng sai của các khẳng định sau:", ["a) Độ dài cạnh huyền $BC$ bằng $15\\text{ cm}$.", "b) Tam giác $HBA$ đồng dạng với tam giác $ABC$ theo trường hợp góc - góc.", "c) Độ dài đường cao $AH$ bằng $7,2\\text{ cm}$.", "d) Độ dài đoạn thẳng $BH$ bằng $6,4\\text{ cm}$."], [True, True, True, False], "a) Đúng vì $BC = \\sqrt{9^2 + 12^2} = 15\\text{ cm}$. b) Đúng vì $\\triangle HBA$ và $\\triangle ABC$ cùng vuông và có chung góc nhọn $B$. c) Đúng vì $\\triangle HBA \\backsim \\triangle ABC \\implies \\frac{AH}{AC} = \\frac{AB}{BC} \\implies AH = \\frac{9 \\cdot 12}{15} = 7,2\\text{ cm}$. d) Sai vì $\\frac{BH}{AB} = \\frac{AB}{BC} \\implies BH = \\frac{AB^2}{BC} = \\frac{81}{15} = 5,4\\text{ cm}$."),
            tf4("hieu", "Cho $\\triangle A'B'C' \\backsim \\triangle ABC$ theo tỉ số đồng dạng $k = \\frac{3}{4}$. Biết chu vi của $\\triangle ABC$ là $40\\text{ cm}$ và diện tích của $\\triangle ABC$ là $64\\text{ cm}^2$. Xét tính đúng sai của các khẳng định sau:", ["a) Tam giác $ABC$ đồng dạng với tam giác $A'B'C'$ theo tỉ số $\\frac{4}{3}$.", "b) Chu vi của tam giác $A'B'C'$ bằng $30\\text{ cm}$.", "c) Tỉ số hai đường cao tương ứng của $\\triangle A'B'C'$ và $\\triangle ABC$ bằng $\\frac{9}{16}$.", "d) Diện tích của tam giác $A'B'C'$ bằng $36\\text{ cm}^2$."], [True, True, False, True], "a) Đúng vì tỉ số đồng dạng ngược lại là $\\frac{1}{k} = \\frac{4}{3}$. b) Đúng vì $P_{A'B'C'} = k \\cdot P_{ABC} = \\frac{3}{4} \\cdot 40 = 30\\text{ cm}$. c) Sai vì tỉ số hai đường cao tương ứng bằng $k = \\frac{3}{4}$. d) Đúng vì $S_{A'B'C'} = k^2 \\cdot S_{ABC} = \\frac{9}{16} \\cdot 64 = 36\\text{ cm}^2$."),
            mcq("vandung", "Cùng một thời điểm trong ngày, một cọc tiêu cao $1,5\\text{ m}$ cắm vuông góc với mặt đất có bóng trên mặt đất dài $2\\text{ m}$, còn một cột cờ có bóng trên mặt đất dài $12\\text{ m}$. Chiều cao của cột cờ đó là:", ["$9\\text{ m}$", "$16\\text{ m}$", "$8\\text{ m}$", "$10\\text{ m}$"], 0, "Các tia nắng mặt trời song song tạo nên hai tam giác vuông đồng dạng, suy ra $\\frac{h}{1,5} = \\frac{12}{2} = 6 \\implies h = 1,5 \\cdot 6 = 9\\text{ m}$."),
            short("vandung", "Cho hai tam giác đồng dạng có tỉ số chu vi bằng $\\frac{2}{3}$ và hiệu diện tích của chúng bằng $45\\text{ cm}^2$. Tính diện tích của tam giác nhỏ hơn (đơn vị $\\text{cm}^2$).", ["36"], "Tỉ số đồng dạng bằng tỉ số chu vi là $k = \\frac{2}{3}$, nên tỉ số diện tích là $\\frac{S_1}{S_2} = k^2 = \\frac{4}{9}$. Ta có $\\frac{S_1}{4} = \\frac{S_2}{9} = \\frac{S_2 - S_1}{9 - 4} = \\frac{45}{5} = 9 \\implies S_1 = 4 \\cdot 9 = 36\\text{ (cm}^2\\text{)}$."),
        ],
    },
    {
        "topic": "l8-ch10-mot-so-hinh-khoi-trong-thuc-tien",
        "title": "Một số hình khối trong thực tiễn",
        "icon": "⛺",
        "description": "Hình chóp tam giác đều, hình chóp tứ giác đều, diện tích xung quanh và thể tích của hình chóp đều",
        "requirements": [
            "Mô tả (đỉnh, mặt đáy, mặt bên, cạnh bên, cạnh đáy, trung đoạn, đường cao) và tạo lập được hình chóp tam giác đều và hình chóp tứ giác đều.",
            "Tính được diện tích xung quanh, diện tích toàn phần và thể tích của hình chóp tam giác đều và hình chóp tứ giác đều.",
            "Giải quyết được một số vấn đề thực tiễn gắn với việc tính thể tích, diện tích xung quanh của đồ vật, công trình có dạng hình chóp tam giác đều và hình chóp tứ giác đều.",
        ],
        "definition": "Hình chóp tam giác đều có đáy là một tam giác đều và các mặt bên là các tam giác cân bằng nhau có chung một đỉnh. Hình chóp tứ giác đều có đáy là một hình vuông và các mặt bên là các tam giác cân bằng nhau có chung một đỉnh.",
        "theory": (
            "### Bài 38. Hình chóp tam giác đều\n"
            "- Hình chóp tam giác đều $S.ABC$ có mặt đáy $ABC$ là tam giác đều, các mặt bên $SAB, SBC, SCA$ là các tam giác cân bằng nhau tại đỉnh $S$. Chân đường cao $SO$ của hình chóp trùng với trọng tâm của tam giác đáy. Đường cao vẽ từ đỉnh $S$ của mỗi mặt bên gọi là trung đoạn của hình chóp. Diện tích xung quanh bằng nửa tích của chu vi đáy với trung đoạn; thể tích bằng một phần ba tích của diện tích đáy với chiều cao.\n"
            "### Bài 39. Hình chóp tứ giác đều\n"
            "- Hình chóp tứ giác đều $S.ABCD$ có mặt đáy $ABCD$ là hình vuông, $4$ mặt bên là các tam giác cân bằng nhau tại đỉnh $S$. Chân đường cao $SO$ trùng với giao điểm hai đường chéo của mặt đáy. Diện tích xung quanh bằng nửa tích của chu vi đáy với trung đoạn; thể tích bằng một phần ba tích của diện tích đáy với chiều cao."
        ),
        "formulas": [
            G("Diện tích và thể tích hình chóp đều (tam giác đều và tứ giác đều)", F("Diện tích xung quanh (nửa chu vi đáy $p$, trung đoạn $d$)", "$S_{\\text{xq}} = p \\cdot d = \\frac{1}{2} C_{\\text{đáy}} \\cdot d$"), F("Diện tích toàn phần", "$S_{\\text{tp}} = S_{\\text{xq}} + S_{\\text{đáy}}$"), F("Thể tích (diện tích đáy $S_{\\text{đáy}}$, chiều cao $h$)", "$V = \\frac{1}{3} S_{\\text{đáy}} \\cdot h$")),
            G("Các hệ thức trong hình chóp tứ giác đều (cạnh đáy $a$, chiều cao $h$, trung đoạn $d$)", F("Chu vi đáy và diện tích đáy hình vuông", "$C_{\\text{đáy}} = 4a, \\quad S_{\\text{đáy}} = a^2, \\quad p = 2a$"), F("Diện tích xung quanh hình chóp tứ giác đều", "$S_{\\text{xq}} = 2a \\cdot d$"), F("Liên hệ giữa chiều cao $h$, trung đoạn $d$ và cạnh đáy $a$", "$d^2 = h^2 + \\left(\\frac{a}{2}\\right)^2$")),
        ],
        "example": "Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy $AB = 12\\text{ cm}$ và chiều cao $SO = 8\\text{ cm}$. Tính độ dài trung đoạn $d$, diện tích xung quanh và thể tích của hình chóp đó.",
        "example_answer": "Gọi $M$ là trung điểm của $BC$, khi đó $OM = \\frac{AB}{2} = 6\\text{ cm}$ và $SM = d$ là trung đoạn. Áp dụng định lí Pythagore trong $\\triangle SOM$ vuông tại $O$: $d = \\sqrt{SO^2 + OM^2} = \\sqrt{8^2 + 6^2} = 10\\text{ cm}$. Nửa chu vi đáy là $p = 2 \\cdot 12 = 24\\text{ cm}$, suy ra diện tích xung quanh $S_{\\text{xq}} = p \\cdot d = 24 \\cdot 10 = 240\\text{ cm}^2$. Diện tích đáy $S_{\\text{đáy}} = 12^2 = 144\\text{ cm}^2$, suy ra thể tích $V = \\frac{1}{3} \\cdot 144 \\cdot 8 = 384\\text{ cm}^3$.",
        "real_life": "Các công trình nổi tiếng như Kim tự tháp kính Louvre (Pháp), Kim tự tháp Ai Cập, mái nhà chòi nghỉ mát, lều cắm trại hay hộp quà trang trí đều mang hình dạng của hình chóp tứ giác đều hoặc hình chóp tam giác đều.",
        "quiz": [
            mcq("biet", "Mặt đáy của hình chóp tam giác đều là hình gì?", ["Tam giác đều", "Tam giác cân", "Tam giác vuông", "Hình vuông"], 0, "Theo định nghĩa, hình chóp tam giác đều có mặt đáy là một tam giác đều."),
            mcq("biet", "Các mặt bên của hình chóp tứ giác đều là những hình gì?", ["Các tam giác cân bằng nhau", "Các tam giác vuông bằng nhau", "Các hình chữ nhật bằng nhau", "Các hình vuông bằng nhau"], 0, "Hình chóp tứ giác đều có đáy là hình vuông và $4$ mặt bên là các tam giác cân bằng nhau có chung đỉnh."),
            mcq("biet", "Công thức tính thể tích $V$ của hình chóp đều có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = \\frac{1}{3} S \\cdot h$", "$V = S \\cdot h$", "$V = \\frac{1}{2} S \\cdot h$", "$V = 3 S \\cdot h$"], 0, "Thể tích hình chóp đều bằng một phần ba tích của diện tích đáy với chiều cao: $V = \\frac{1}{3} S \\cdot h$."),
            mcq("biet", "Một hình chóp tam giác đều có chu vi đáy bằng $24\\text{ cm}$ và độ dài trung đoạn bằng $10\\text{ cm}$. Diện tích xung quanh của hình chóp đó là:", ["$120\\text{ cm}^2$", "$240\\text{ cm}^2$", "$80\\text{ cm}^2$", "$360\\text{ cm}^2$"], 0, "Nửa chu vi đáy là $p = 24 : 2 = 12\\text{ cm}$. Diện tích xung quanh là $S_{\\text{xq}} = p \\cdot d = 12 \\cdot 10 = 120\\text{ cm}^2$."),
            mcq("hieu", "Một hình chóp tứ giác đều có cạnh đáy bằng $6\\text{ cm}$ và chiều cao bằng $5\\text{ cm}$. Thể tích của hình chóp tứ giác đều đó bằng:", ["$60\\text{ cm}^3$", "$180\\text{ cm}^3$", "$30\\text{ cm}^3$", "$90\\text{ cm}^3$"], 0, "Diện tích đáy hình vuông là $S = 6^2 = 36\\text{ cm}^2$. Thể tích hình chóp là $V = \\frac{1}{3} \\cdot 36 \\cdot 5 = 60\\text{ cm}^3$."),
            mcq("hieu", "Một hình chóp tứ giác đều có diện tích xung quanh bằng $160\\text{ cm}^2$ và độ dài trung đoạn bằng $8\\text{ cm}$. Độ dài cạnh đáy của hình chóp đó là:", ["$10\\text{ cm}$", "$20\\text{ cm}$", "$5\\text{ cm}$", "$8\\text{ cm}$"], 0, "Ta có $S_{\\text{xq}} = 2a \\cdot d \\implies 160 = 2a \\cdot 8 \\implies 16a = 160 \\implies a = 10\\text{ cm}$."),
            tf4("hieu", "Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy $AB = 10\\text{ cm}$ và độ dài trung đoạn $SM = 13\\text{ cm}$ ($M$ là trung điểm của $BC$), gọi $O$ là tâm của đáy. Xét tính đúng sai của các khẳng định sau:", ["a) Diện tích mặt đáy $ABCD$ bằng $100\\text{ cm}^2$.", "b) Diện tích xung quanh của hình chóp $S.ABCD$ bằng $260\\text{ cm}^2$.", "c) Độ dài đoạn thẳng $OM$ bằng $5\\text{ cm}$ và chiều cao $SO$ của hình chóp bằng $12\\text{ cm}$.", "d) Thể tích của hình chóp $S.ABCD$ bằng $1\\,200\\text{ cm}^3$."], [True, True, True, False], "a) Đúng vì $S_{\\text{đáy}} = 10^2 = 100\\text{ cm}^2$. b) Đúng vì $S_{\\text{xq}} = 2a \\cdot d = 2 \\cdot 10 \\cdot 13 = 260\\text{ cm}^2$. c) Đúng vì $OM = \\frac{10}{2} = 5\\text{ cm}$ và $SO = \\sqrt{SM^2 - OM^2} = \\sqrt{13^2 - 5^2} = 12\\text{ cm}$. d) Sai vì thể tích $V = \\frac{1}{3} S_{\\text{đáy}} \\cdot SO = \\frac{1}{3} \\cdot 100 \\cdot 12 = 400\\text{ cm}^3$."),
            tf4("hieu", "Cho hình chóp tam giác đều $S.ABC$ có cạnh đáy $AB = 8\\text{ cm}$ và cạnh bên $SA = 5\\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Xét tính đúng sai của các khẳng định sau:", ["a) Hình chóp $S.ABC$ có $4$ mặt (gồm $1$ mặt đáy và $3$ mặt bên) và $6$ cạnh.", "b) Đoạn thẳng $SM$ vuông góc với $BC$ và là một trung đoạn của hình chóp $S.ABC$.", "c) Độ dài trung đoạn $SM$ bằng $3\\text{ cm}$.", "d) Diện tích xung quanh của hình chóp $S.ABC$ bằng $72\\text{ cm}^2$."], [True, True, True, False], "a) Đúng vì hình chóp tam giác đều có $1$ mặt đáy, $3$ mặt bên, $3$ cạnh đáy và $3$ cạnh bên. b) Đúng vì $\\triangle SBC$ cân tại $S$, $M$ là trung điểm $BC$ nên $SM \\perp BC$ là trung đoạn. c) Đúng vì $BM = \\frac{8}{2} = 4\\text{ cm}$, áp dụng định lí Pythagore trong $\\triangle SBM$ vuông tại $M$ ta có $SM = \\sqrt{SB^2 - BM^2} = \\sqrt{5^2 - 4^2} = 3\\text{ cm}$. d) Sai vì nửa chu vi đáy là $p = \\frac{3 \\cdot 8}{2} = 12\\text{ cm}$ nên diện tích xung quanh là $S_{\\text{xq}} = p \\cdot SM = 12 \\cdot 3 = 36\\text{ cm}^2$."),
            mcq("vandung", "Một lều cắm trại có dạng hình chóp tứ giác đều với độ dài cạnh đáy là $3\\text{ m}$ và độ dài trung đoạn là $2,5\\text{ m}$. Người ta muốn may vải phủ kín bốn mặt bên của lều (không tính mặt đáy, coi mép khâu không đáng kể). Biết giá vải là $80\\,000\\text{ đồng/m}^2$, số tiền mua vải cần dùng là:", ["$1\\,200\\,000$ đồng", "$2\\,400\\,000$ đồng", "$600\\,000$ đồng", "$1\\,500\\,000$ đồng"], 0, "Diện tích vải cần dùng chính là diện tích xung quanh của hình chóp tứ giác đều: $S_{\\text{xq}} = 2 \\cdot 3 \\cdot 2,5 = 15\\text{ m}^2$. Số tiền mua vải là $15 \\cdot 80\\,000 = 1\\,200\\,000$ (đồng)."),
            short("vandung", "Một khối pha lê trang trí có dạng hình chóp tứ giác đều với cạnh đáy dài $9\\text{ cm}$ và chiều cao dài $10\\text{ cm}$. Tính thể tích của khối pha lê đó (đơn vị $\\text{cm}^3$).", ["270"], "Diện tích mặt đáy hình vuông là $S = 9^2 = 81\\text{ cm}^2$. Thể tích khối pha lê là $V = \\frac{1}{3} \\cdot 81 \\cdot 10 = 270\\text{ (cm}^3\\text{)}$."),
        ],
    },
]
