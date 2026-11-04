"""TOÁN 9 — Kết nối tri thức với cuộc sống (tập một, tập hai).

10 chương đánh số (I – X) đúng thứ tự mục lục SGK.
Mỗi chương: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 9

LESSONS = [
    {
        "topic": "l9-ch01-phuong-trinh-va-he-hai-phuong-trinh-bac-nhat-hai-an",
        "title": "Phương trình và hệ hai phương trình bậc nhất hai ẩn",
        "icon": "⚖️",
        "description": "Chương I · SGK Toán 9 tập một: Bài 1 – Bài 3. Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn; giải hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế và phương pháp cộng đại số; giải bài toán bằng cách lập hệ phương trình.",
        "requirements": [
            "Nhận biết được khái niệm phương trình bậc nhất hai ẩn, hệ hai phương trình bậc nhất hai ẩn.",
            "Nhận biết được khái niệm nghiệm của phương trình bậc nhất hai ẩn, nghiệm của hệ hai phương trình bậc nhất hai ẩn.",
            "Giải được hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế và phương pháp cộng đại số.",
            "Tính được nghiệm của hệ hai phương trình bậc nhất hai ẩn bằng máy tính cầm tay.",
            "Giải quyết được một số vấn đề thực tiễn gắn với hệ hai phương trình bậc nhất hai ẩn (ví dụ: các bài toán liên quan đến chuyển động, năng suất, cân bằng phản ứng trong Hoá học).",
        ],
        "definition": (
            "- **Phương trình bậc nhất hai ẩn** $x, y$ có dạng $ax + by = c$, trong đó $a, b, c$ là các số đã biết ($a \\ne 0$ hoặc $b \\ne 0$). Cặp số $(x_0; y_0)$ thoả mãn $ax_0 + by_0 = c$ gọi là một **nghiệm** của phương trình.\n"
            "- Trong mặt phẳng toạ độ $Oxy$, tập hợp các điểm có toạ độ $(x; y)$ thoả mãn $ax + by = c$ là một **đường thẳng**.\n"
            "- **Hệ hai phương trình bậc nhất hai ẩn** có dạng $\\begin{cases} ax + by = c \\\\ a'x + b'y = c' \\end{cases}$. Cặp số $(x_0; y_0)$ đồng thời là nghiệm của cả hai phương trình gọi là **nghiệm của hệ**.\n"
            "- Hai phương pháp giải đại số cơ bản: **phương pháp thế** (biểu diễn một ẩn theo ẩn kia rồi thế vào phương trình còn lại) và **phương pháp cộng đại số** (nhân hệ số thích hợp rồi cộng hoặc trừ từng vế để khử một ẩn)."
        ),
        "theory": (
            "### Bài 1. Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn\n"
            "- Phương trình $ax + by = c$ ($a \\ne 0$ hoặc $b \\ne 0$) luôn có vô số nghiệm. Mỗi nghiệm $(x_0; y_0)$ ứng với một điểm trên đường thẳng $ax + by = c$.\n"
            "- Nghiệm của hệ $\\begin{cases} d_1: ax + by = c \\\\ d_2: a'x + b'y = c' \\end{cases}$ là toạ độ giao điểm của hai đường thẳng $d_1$ và $d_2$ (cắt nhau $\\Rightarrow$ nghiệm duy nhất; song song $\\Rightarrow$ vô nghiệm; trùng nhau $\\Rightarrow$ vô số nghiệm).\n"
            "### Bài 2. Giải hệ hai phương trình bậc nhất hai ẩn\n"
            "- **Phương pháp thế**: Từ một phương trình, biểu diễn ẩn này theo ẩn kia (ví dụ $y = c - ax$) rồi thế vào phương trình thứ hai để được phương trình bậc nhất một ẩn.\n"
            "- **Phương pháp cộng đại số**: Nhân hai vế của mỗi phương trình với số thích hợp sao cho hệ số của một ẩn bằng nhau hoặc đối nhau, sau đó trừ hoặc cộng từng vế hai phương trình để khử ẩn đó.\n"
            "### Luyện tập chung\n"
            "### Bài 3. Giải bài toán bằng cách lập hệ phương trình\n"
            "- **Bước 1 (Lập hệ phương trình)**: Chọn hai ẩn và đặt điều kiện thích hợp; biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết; lập hai phương trình biểu thị mối quan hệ giữa các đại lượng.\n"
            "- **Bước 2 (Giải hệ phương trình)**: Dùng phương pháp thế hoặc cộng đại số.\n"
            "- **Bước 3 (Trả lời)**: Kiểm tra điều kiện của ẩn và kết luận.\n"
            "### Bài tập cuối chương I"
        ),
        "formulas": [
            G("I. Phương trình và hệ phương trình", F("Phương trình bậc nhất hai ẩn", "$ax + by = c \\quad (a \\ne 0 \\text{ hoặc } b \\ne 0)$"), F("Hệ hai phương trình bậc nhất hai ẩn", "$\\begin{cases} ax + by = c \\\\ a'x + b'y = c' \\end{cases}$"), F("Điều kiện nghiệm (khi $a', b', c' \\ne 0$)", "Nghiệm duy nhất: $\\dfrac{a}{a'} \\ne \\dfrac{b}{b'}$ · Vô nghiệm: $\\dfrac{a}{a'} = \\dfrac{b}{b'} \\ne \\dfrac{c}{c'}$ · Vô số nghiệm: $\\dfrac{a}{a'} = \\dfrac{b}{b'} = \\dfrac{c}{c'}$")),
            G("II. Hai phương pháp giải hệ", F("Phương pháp thế", "Rút $x$ (hoặc $y$) từ PT (1) thế vào PT (2)", "Thuận tiện khi có hệ số $\\pm 1$."), F("Phương pháp cộng đại số", "Cộng (hệ số đối nhau) hoặc trừ (hệ số bằng nhau) từng vế để khử 1 ẩn")),
        ],
        "example": "Giải hệ phương trình: $\\begin{cases} 2x + y = 7 \\\\ 3x - 2y = 0 \\end{cases}$.",
        "example_answer": (
            "Từ phương trình đầu có $y = 7 - 2x$. Thế vào phương trình thứ hai:\n"
            "$3x - 2(7 - 2x) = 0 \\Rightarrow 7x = 14 \\Rightarrow x = 2$.\n"
            "Suy ra $y = 7 - 2 \\cdot 2 = 3$. Vậy hệ có nghiệm duy nhất **$(x; y) = (2; 3)$**."
        ),
        "real_life": (
            "- Tìm số lượng hai loại sản phẩm, giá tiền hai mặt hàng từ hoá đơn mua sắm.\n"
            "- Bài toán chuyển động (cùng chiều, ngược chiều, xuôi dòng, ngược dòng), bài toán làm chung – làm riêng công việc, cân bằng phương trình phản ứng hoá học."
        ),
        "quiz": [
            mcq("biet", "Phương trình nào sau đây là phương trình bậc nhất hai ẩn $x, y$?", ["$2x - 3y = 5$", "$x^2 + y = 1$", "$0x + 0y = 3$", "$xy + 2x = 4$"], 0, "Phương trình bậc nhất hai ẩn có dạng $ax + by = c$ với $a \\ne 0$ hoặc $b \\ne 0$ $\\Rightarrow$ **$2x - 3y = 5$**."),
            mcq("biet", "Cặp số nào sau đây là một nghiệm của phương trình $2x + y = 5$?", ["$(2; 1)$", "$(1; 2)$", "$(3; 1)$", "$(0; -5)$"], 0, "Thay $x = 2, y = 1$ vào vế trái: $2 \\cdot 2 + 1 = 5$ (đúng) $\\Rightarrow$ **$(2; 1)$**."),
            mcq("biet", "Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:", ["$(3; 2)$", "$(2; 3)$", "$(4; 1)$", "$(1; 4)$"], 0, "Cộng từng vế: $2x = 6 \\Rightarrow x = 3$, suy ra $y = 5 - 3 = 2$ $\\Rightarrow$ **$(3; 2)$**."),
            mcq("biet", "Tập nghiệm của phương trình $0x + 2y = 6$ được biểu diễn bởi đường thẳng nào trên mặt phẳng toạ độ $Oxy$?", ["$y = 3$", "$x = 3$", "$y = 6$", "$y = 2x + 6$"], 0, "Rút gọn $0x + 2y = 6$ được **$y = 3$** (đường thẳng song song với trục $Ox$)."),
            mcq("hieu", "Cho hệ phương trình $\\begin{cases} 3x + 2y = 8 \\\\ 2x - y = 3 \\end{cases}$. Nếu $(x_0; y_0)$ là nghiệm của hệ thì tổng $x_0 + y_0$ bằng:", ["$3$", "$4$", "$1$", "$5$"], 0, "Từ PT (2) có $y = 2x - 3$, thế vào PT (1): $3x + 2(2x - 3) = 8 \\Rightarrow 7x = 14 \\Rightarrow x_0 = 2, y_0 = 1$. Suy ra $x_0 + y_0 = 2 + 1 =$ **$3$**."),
            mcq("hieu", "Hệ phương trình $\\begin{cases} 2x - y = 3 \\\\ 4x - 2y = 5 \\end{cases}$ có bao nhiêu nghiệm?", ["Vô nghiệm", "Một nghiệm duy nhất", "Hai nghiệm", "Vô số nghiệm"], 0, "Ta có $\\dfrac{2}{4} = \\dfrac{-1}{-2} \\ne \\dfrac{3}{5}$ nên hai đường thẳng song song $\\Rightarrow$ hệ **vô nghiệm**."),
            tf4("hieu", "Cho hệ phương trình $\\begin{cases} 2x + y = 5 \\quad (1) \\\\ x - 3y = -1 \\quad (2) \\end{cases}$. Mỗi khẳng định sau đúng hay sai?", ["a) Từ phương trình (1) có thể biểu diễn $y = 5 - 2x$", "b) Thế $y = 5 - 2x$ vào phương trình (2) ta được $7x - 15 = -1$", "c) Nghiệm của hệ phương trình là $(2; 1)$", "d) Hai đường thẳng biểu diễn hai phương trình của hệ song song với nhau"], [True, True, True, False], "a) $2x + y = 5 \\Leftrightarrow y = 5 - 2x$ $\\rightarrow$ Đúng.\
b) $x - 3(5 - 2x) = -1 \\Leftrightarrow 7x - 15 = -1$ $\\rightarrow$ Đúng.\
c) $7x = 14 \\Rightarrow x = 2 \\Rightarrow y = 1$, nghiệm là $(2; 1)$ $\\rightarrow$ Đúng.\
d) Hệ có nghiệm duy nhất nên hai đường thẳng cắt nhau tại $(2; 1)$ $\\rightarrow$ Sai."),
            tf4("hieu", "Một mảnh vườn hình chữ nhật có chu vi $50\\text{ m}$. Nếu tăng chiều rộng thêm $3\\text{ m}$ và giảm chiều dài đi $2\\text{ m}$ thì diện tích không đổi. Gọi chiều dài và chiều rộng ban đầu của mảnh vườn lần lượt là $x, y$ ($\\text{m}$, $x > y > 0$). Mỗi khẳng định sau đúng hay sai?", ["a) Phương trình biểu thị chu vi mảnh vườn là $x + y = 50$", "b) Phương trình biểu thị diện tích không đổi là $(x - 2)(y + 3) = xy$", "c) Thu gọn phương trình diện tích ta được $3x - 2y = 6$", "d) Chiều dài ban đầu của mảnh vườn là $14\\text{ m}$"], [False, True, True, False], "a) Chu vi $2(x + y) = 50 \\Leftrightarrow x + y = 25$ (không phải $50$) $\\rightarrow$ Sai.\
b) Diện tích mới $(x - 2)(y + 3)$ bằng diện tích ban đầu $xy$ $\\rightarrow$ Đúng.\
c) $xy + 3x - 2y - 6 = xy \\Leftrightarrow 3x - 2y = 6$ $\\rightarrow$ Đúng.\
d) Giải hệ $\\begin{cases} x + y = 25 \\\\ 3x - 2y = 6 \\end{cases}$ được $x = 11,2; y = 13,8$ (hoặc thay $x = 14, y = 11$ thì $3 \\cdot 14 - 2 \\cdot 11 = 20 \\ne 6$) $\\rightarrow$ Sai."),
            mcq("vandung", "Hai vòi nước cùng chảy vào một bể cạn thì sau $6$ giờ đầy bể. Nếu mở vòi thứ nhất chảy trong $3$ giờ và vòi thứ hai chảy trong $4$ giờ thì được $\\dfrac{3}{5}$ bể. Nếu chảy một mình thì vòi thứ nhất làm đầy bể trong bao lâu?", ["$10$ giờ", "$15$ giờ", "$12$ giờ", "$8$ giờ"], 1, "Gọi $x, y$ (giờ) là thời gian vòi I, vòi II chảy một mình đầy bể ($x, y > 6$). Ta có hệ $\\begin{cases} \\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{6} \\\\ \\dfrac{3}{x} + \\dfrac{4}{y} = \\dfrac{3}{5} \\end{cases} \\Rightarrow \\dfrac{1}{y} = \\dfrac{3}{5} - \\dfrac{3}{6} = \\dfrac{1}{10} \\Rightarrow y = 10$ và $\\dfrac{1}{x} = \\dfrac{1}{6} - \\dfrac{1}{10} = \\dfrac{1}{15} \\Rightarrow x =$ **$15$ giờ**."),
            short("vandung", "Một cửa hàng bán $3$ quyển vở và $2$ chiếc bút giá $31\\,000$ đồng. Bạn An mua $5$ quyển vở và $4$ chiếc bút cùng loại hết $55\\,000$ đồng. Giá một quyển vở là bao nhiêu nghìn đồng?", ["7"], "Gọi giá $1$ quyển vở là $x$ (nghìn đồng), giá $1$ chiếc bút là $y$ (nghìn đồng). Ta có hệ $\\begin{cases} 3x + 2y = 31 \\\\ 5x + 4y = 55 \\end{cases} \\Rightarrow 6x + 4y = 62 \\Rightarrow x = 62 - 55 =$ **$7$** (nghìn đồng).", unit="nghìn đồng"),
        ],
    },
    {
        "topic": "l9-ch02-phuong-trinh-va-bat-phuong-trinh-bac-nhat-mot-an",
        "title": "Phương trình và bất phương trình bậc nhất một ẩn",
        "icon": "📈",
        "description": "Chương II · SGK Toán 9 tập một: Bài 4 – Bài 6. Phương trình quy về phương trình bậc nhất một ẩn (phương trình tích, phương trình chứa ẩn ở mẫu); bất đẳng thức và tính chất; bất phương trình bậc nhất một ẩn.",
        "requirements": [
            "Giải được phương trình tích có dạng $(a_1x + b_1)(a_2x + b_2) = 0$.",
            "Giải được phương trình chứa ẩn ở mẫu quy về phương trình bậc nhất.",
            "Nhận biết được thứ tự trên tập hợp các số thực; nhận biết được bất đẳng thức và mô tả được một số tính chất cơ bản của bất đẳng thức (tính chất bắc cầu; liên hệ giữa thứ tự và phép cộng, phép nhân).",
            "Nhận biết được khái niệm bất phương trình bậc nhất một ẩn, nghiệm của bất phương trình bậc nhất một ẩn.",
            "Giải được bất phương trình bậc nhất một ẩn và vận dụng vào giải quyết một số bài toán thực tiễn.",
        ],
        "definition": (
            "- **Phương trình tích** có dạng $(a_1x + b_1)(a_2x + b_2) = 0 \\Leftrightarrow a_1x + b_1 = 0$ hoặc $a_2x + b_2 = 0$.\n"
            "- **Phương trình chứa ẩn ở mẫu**: cần tìm **điều kiện xác định (ĐKXĐ)** để tất cả các mẫu thức khác $0$, quy đồng khử mẫu, giải phương trình nhận được và đối chiếu với ĐKXĐ.\n"
            "- **Bất đẳng thức**: hệ thức dạng $a < b, a > b, a \\le b, a \\ge b$, trong đó $a$ là vế trái, $b$ là vế phải.\n"
            "- **Bất phương trình bậc nhất một ẩn** $x$ có dạng $ax + b < 0$ (hoặc $ax + b > 0, ax + b \\le 0, ax + b \\ge 0$) với $a, b$ là hai số đã cho và $a \\ne 0$."
        ),
        "theory": (
            "### Bài 4. Phương trình quy về phương trình bậc nhất một ẩn\n"
            "- Giải phương trình tích: phân tích vế trái thành nhân tử (khi vế phải bằng $0$) rồi giải từng nhân tử bằng $0$.\n"
            "- Giải phương trình chứa ẩn ở mẫu: Bước 1: Tìm ĐKXĐ. Bước 2: Quy đồng mẫu hai vế rồi khử mẫu. Bước 3: Giải phương trình vừa tìm được. Bước 4: Kết luận (chỉ nhận các giá trị thoả mãn ĐKXĐ).\n"
            "### Bài 5. Bất đẳng thức và tính chất\n"
            "- Tính chất bắc cầu: $a < b$ và $b < c \\Rightarrow a < c$.\n"
            "- Cộng cùng một số vào hai vế: $a < b \\Rightarrow a + c < b + c$.\n"
            "- Nhân hai vế với số dương **giữ nguyên chiều**; nhân hai vế với số âm **đổi chiều** bất đẳng thức.\n"
            "### Luyện tập chung\n"
            "### Bài 6. Bất phương trình bậc nhất một ẩn\n"
            "- Giải $ax + b < 0$ ($a \\ne 0$): chuyển hạng tử tự do sang vế phải $ax < -b$, rồi chia hai vế cho $a$ (nếu $a > 0$ thì $x < -\\dfrac{b}{a}$; nếu $a < 0$ thì $x > -\\dfrac{b}{a}$).\n"
            "### Bài tập cuối chương II"
        ),
        "formulas": [
            G("I. Phương trình quy về bậc nhất", F("Phương trình tích", "$A(x) \\cdot B(x) = 0 \\Leftrightarrow A(x) = 0 \\text{ hoặc } B(x) = 0$"), F("Điều kiện xác định (chứa ẩn ở mẫu)", "Mẫu thức $\\ne 0$")),
            G("II. Tính chất bất đẳng thức", F("Liên hệ với phép cộng", "$a < b \\Leftrightarrow a + c < b + c$"), F("Nhân với số dương ($c > 0$)", "$a < b \\Rightarrow ac < bc$"), F("Nhân với số âm ($c < 0$)", "$a < b \\Rightarrow ac > bc$", "Nhân hay chia số âm phải đổi chiều.")),
            G("III. Bất phương trình bậc nhất một ẩn", F("Khi $a > 0$", "$ax + b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$"), F("Khi $a < 0$", "$ax + b < 0 \\Leftrightarrow x > -\\dfrac{b}{a}$")),
        ],
        "example": "Giải bất phương trình: $7 - 2x \\ge 1$.",
        "example_answer": (
            "Chuyển vế: $-2x \\ge 1 - 7 \\Leftrightarrow -2x \\ge -6$.\n"
            "Chia cả hai vế cho $-2 < 0$ (đổi chiều): $x \\le 3$. Vậy nghiệm của bất phương trình là **$x \\le 3$**."
        ),
        "real_life": (
            "- Tính số lượng hàng hoá tối đa có thể mua với số tiền giới hạn, tính điểm số tối thiểu cần đạt trong bài thi.\n"
            "- Bài toán năng suất, chuyển động có biểu thức thời gian chứa ẩn ở mẫu."
        ),
        "quiz": [
            mcq("biet", "Tập nghiệm của phương trình $(x - 3)(2x + 4) = 0$ là:", ["$\\{3; -2\\}$", "$\\{-3; 2\\}$", "$\\{3; 2\\}$", "$\\{-3; -2\\}$"], 0, "$x - 3 = 0 \\Rightarrow x = 3$; $2x + 4 = 0 \\Rightarrow x = -2$ $\\Rightarrow$ **$S = \\{3; -2\\}$**."),
            mcq("biet", "Điều kiện xác định của phương trình $\\dfrac{2x + 1}{x - 4} = 3$ là:", ["$x \\ne 4$", "$x \\ne -4$", "$x \\ne -\\dfrac{1}{2}$", "$x > 4$"], 0, "Mẫu thức khác $0$: $x - 4 \\ne 0 \\Leftrightarrow$ **$x \\ne 4$**."),
            mcq("biet", "Cho $a < b$. Khẳng định nào sau đây **đúng**?", ["$a + 5 < b + 5$", "$-2a < -2b$", "$a - 3 > b - 3$", "$3a > 3b$"], 0, "Cộng cùng số $5$ vào hai vế của $a < b$ giữ nguyên chiều: **$a + 5 < b + 5$**."),
            mcq("biet", "Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?", ["$3x - 5 > 0$", "$x^2 - 4 < 0$", "$0x + 7 \\le 0$", "$2x + y \\ge 1$"], 0, "Bất phương trình bậc nhất một ẩn có dạng $ax + b > 0$ với $a \\ne 0$ $\\Rightarrow$ **$3x - 5 > 0$**."),
            mcq("hieu", "Nghiệm của bất phương trình $-3x + 12 > 0$ là:", ["$x < 4$", "$x > 4$", "$x < -4$", "$x > -4$"], 0, "$-3x > -12 \\Leftrightarrow$ **$x < 4$** (chia hai vế cho $-3 < 0$ nên đổi chiều).", note="Lưu ý đổi chiều bất phương trình khi chia cho số âm."),
            mcq("hieu", "Số nghiệm của phương trình $\\dfrac{x}{x - 2} = \\dfrac{2}{x - 2}$ là:", ["$0$", "$1$", "$2$", "Vô số"], 0, "ĐKXĐ: $x \\ne 2$. Khử mẫu được $x = 2$ (không thoả mãn ĐKXĐ) nên phương trình **vô nghiệm** (số nghiệm bằng **$0$**)."),
            tf4("hieu", "Cho bất đẳng thức $m > n$. Mỗi khẳng định sau đúng hay sai?", ["a) $m - 4 > n - 4$", "b) $3m + 1 > 3n + 1$", "c) $-5m > -5n$", "d) $10 - 2m < 10 - 2n$"], [True, True, False, True], "a) Cộng $-4$ vào hai vế giữ nguyên chiều $\\rightarrow$ Đúng.\
b) Nhân với $3 > 0$ rồi cộng $1$ giữ nguyên chiều $\\rightarrow$ Đúng.\
c) Nhân với $-5 < 0$ phải đổi chiều thành $-5m < -5n$ $\\rightarrow$ Sai.\
d) $m > n \\Rightarrow -2m < -2n \\Rightarrow 10 - 2m < 10 - 2n$ $\\rightarrow$ Đúng."),
            tf4("hieu", "Xét phương trình $\\dfrac{x + 3}{x - 1} - \\dfrac{4}{x - 1} = 1$. Mỗi khẳng định sau đúng hay sai?", ["a) Điều kiện xác định của phương trình là $x \\ne 1$", "b) Sau khi khử mẫu, ta thu được phương trình $x - 1 = x - 1$", "c) Giá trị $x = 1$ là một nghiệm của phương trình đã cho", "d) Phương trình có tập nghiệm là $S = \\{x \\in \\mathbb{R} \\mid x \\ne 1\\}$"], [True, True, False, True], "a) Mẫu thức $x - 1 \\ne 0 \\Leftrightarrow x \\ne 1$ $\\rightarrow$ Đúng.\
b) Tử thức vế trái là $(x + 3) - 4 = x - 1$, khử mẫu được $x - 1 = x - 1$ $\\rightarrow$ Đúng.\
c) $x = 1$ vi phạm ĐKXĐ nên không là nghiệm $\\rightarrow$ Sai.\
d) Mọi $x \\ne 1$ đều thoả mãn $x - 1 = x - 1$ $\\rightarrow$ Đúng."),
            mcq("vandung", "Một người có $200\\,000$ đồng đi mua vở. Giá một chiếc bút máy là $35\\,000$ đồng, giá một quyển vở là $12\\,000$ đồng. Sau khi mua $1$ chiếc bút máy, người đó mua được tối đa bao nhiêu quyển vở?", ["$13$ quyển", "$14$ quyển", "$12$ quyển", "$15$ quyển"], 0, "Gọi số quyển vở mua được là $x$ ($x \\in \\mathbb{N}^*$). Ta có $35\\,000 + 12\\,000x \\le 200\\,000 \\Leftrightarrow 12x \\le 165 \\Leftrightarrow x \\le 13,75$. Vì $x \\in \\mathbb{N}^*$ nên mua được tối đa **$13$ quyển**."),
            short("vandung", "Tìm nghiệm nguyên lớn nhất của bất phương trình $5x - 3 < 2x + 11$.", ["4"], "Ta có $5x - 2x < 11 + 3 \\Leftrightarrow 3x < 14 \\Leftrightarrow x < \\dfrac{14}{3} \\approx 4,67$. Nghiệm nguyên lớn nhất là **$4$**."),
        ],
    },
    {
        "topic": "l9-ch03-can-bac-hai-va-can-bac-ba",
        "title": "Căn bậc hai và căn bậc ba",
        "icon": "√",
        "description": "Chương III · SGK Toán 9 tập một: Bài 7 – Bài 10. Căn bậc hai và căn thức bậc hai; khai căn bậc hai với phép nhân và phép chia; biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai; căn bậc ba và căn thức bậc ba.",
        "requirements": [
            "Nhận biết được khái niệm về căn bậc hai của số thực không âm, căn bậc ba của một số thực.",
            "Tính được giá trị (đúng hoặc gần đúng) căn bậc hai, căn bậc ba của một số hữu tỉ bằng máy tính cầm tay.",
            "Nhận biết được khái niệm về căn thức bậc hai và căn thức bậc ba của một biểu thức đại số, tìm điều kiện xác định của căn thức bậc hai.",
            "Thực hiện được một số phép tính đơn giản về căn bậc hai của số thực không âm (căn bậc hai của một bình phương, căn bậc hai của một tích, căn bậc hai của một thương, đưa thừa số ra ngoài hoặc vào trong dấu căn, trục căn thức ở mẫu).",
            "Thực hiện được các phép biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai.",
        ],
        "definition": (
            "- **Căn bậc hai** của số thực không âm $a$ là số $x$ sao cho $x^2 = a$. Số $a > 0$ có hai căn bậc hai là $\\sqrt{a}$ (căn bậc hai số học) và $-\\sqrt{a}$; số $0$ có một căn bậc hai là $0$; số âm không có căn bậc hai.\n"
            "- **Căn thức bậc hai** $\\sqrt{A}$ xác định khi và chỉ khi $A \\ge 0$. Với mọi biểu thức $A$, ta luôn có $\\sqrt{A^2} = |A|$.\n"
            "- **Căn bậc ba** của số thực $a$, kí hiệu $\\sqrt[3]{a}$, là số $x$ sao cho $x^3 = a$. Mọi số thực $a$ đều có duy nhất một căn bậc ba."
        ),
        "theory": (
            "### Bài 7. Căn bậc hai và căn thức bậc hai\n"
            "- Với $a \\ge 0$: $(\\sqrt{a})^2 = a$; với mọi $a \\in \\mathbb{R}$: $\\sqrt{a^2} = |a|$.\n"
            "- Điều kiện xác định của $\\sqrt{A}$ là $A \\ge 0$.\n"
            "### Bài 8. Khai căn bậc hai với phép nhân và phép chia\n"
            "- Với $A \\ge 0, B \\ge 0$: $\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$.\n"
            "- Với $A \\ge 0, B > 0$: $\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$.\n"
            "### Luyện tập chung\n"
            "### Bài 9. Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai\n"
            "- **Đưa thừa số ra ngoài dấu căn**: $\\sqrt{A^2 B} = |A|\\sqrt{B}$ ($B \\ge 0$).\n"
            "- **Đưa thừa số vào trong dấu căn**: nếu $A \\ge 0, B \\ge 0$ thì $A\\sqrt{B} = \\sqrt{A^2 B}$; nếu $A < 0, B \\ge 0$ thì $A\\sqrt{B} = -\\sqrt{A^2 B}$.\n"
            "- **Trục căn thức ở mẫu**: nhân cả tử và mẫu với biểu thức liên hợp ($\\sqrt{A} \\mp \\sqrt{B}$) để khử căn ở mẫu.\n"
            "### Bài 10. Căn bậc ba và căn thức bậc ba\n"
            "- $(\\sqrt[3]{A})^3 = \\sqrt[3]{A^3} = A$ với mọi $A$ (không cần điều kiện không âm).\n"
            "### Luyện tập chung · Bài tập cuối chương III"
        ),
        "formulas": [
            G("I. Hằng đẳng thức và phép khai căn", F("Hằng đẳng thức căn bậc hai", "$\\sqrt{A^2} = |A| = \\begin{cases} A & \\text{nếu } A \\ge 0 \\\\ -A & \\text{nếu } A < 0 \\end{cases}$"), F("Khai căn một tích", "$\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B} \\quad (A \\ge 0, B \\ge 0)$"), F("Khai căn một thương", "$\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}} \\quad (A \\ge 0, B > 0)$")),
            G("II. Biến đổi căn thức bậc hai", F("Đưa thừa số ra ngoài dấu căn", "$\\sqrt{A^2 B} = |A|\\sqrt{B} \\quad (B \\ge 0)$"), F("Trục căn thức ở mẫu (dạng 1)", "$\\dfrac{M}{\\sqrt{A}} = \\dfrac{M\\sqrt{A}}{A} \\quad (A > 0)$"), F("Trục căn thức ở mẫu (biểu thức liên hợp)", "$\\dfrac{M}{\\sqrt{A} - \\sqrt{B}} = \\dfrac{M(\\sqrt{A} + \\sqrt{B})}{A - B} \\quad (A, B \\ge 0; A \\ne B)$")),
            G("III. Căn bậc ba", F("Định nghĩa và tính chất", "$(\\sqrt[3]{A})^3 = \\sqrt[3]{A^3} = A \\cdot \\sqrt[3]{AB} = \\sqrt[3]{A}\\cdot\\sqrt[3]{B}$")),
        ],
        "example": "Rút gọn biểu thức: $P = 3\\sqrt{12} - \\sqrt{27} + \\dfrac{6}{\\sqrt{3}}$.",
        "example_answer": (
            "Ta có $3\\sqrt{12} = 3 \\cdot 2\\sqrt{3} = 6\\sqrt{3}$; $\\sqrt{27} = 3\\sqrt{3}$; $\\dfrac{6}{\\sqrt{3}} = 2\\sqrt{3}$.\n"
            "Suy ra $P = 6\\sqrt{3} - 3\\sqrt{3} + 2\\sqrt{3} =$ **$5\\sqrt{3}$**."
        ),
        "real_life": (
            "- Tính cạnh hình vuông khi biết diện tích ($a = \\sqrt{S}$), tính cạnh lập phương khi biết thể tích ($a = \\sqrt[3]{V}$).\n"
            "- Công thức chu kì con lắc đơn $T = 2\\pi\\sqrt{\\dfrac{l}{g}}$, vận tốc rơi tự do $v = \\sqrt{2gh}$."
        ),
        "quiz": [
            mcq("biet", "Căn bậc hai số học của $25$ là:", ["$5$", "$-5$", "$\\pm 5$", "$625$"], 0, "Căn bậc hai số học của $a > 0$ là số dương $\\sqrt{a}$ $\\Rightarrow \\sqrt{25} =$ **$5$**."),
            mcq("biet", "Điều kiện xác định của căn thức $\\sqrt{2x - 6}$ là:", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x \\ne 3$"], 0, "Biểu thức dưới dấu căn không âm: $2x - 6 \\ge 0 \\Leftrightarrow$ **$x \\ge 3$**."),
            mcq("biet", "Giá trị của $\\sqrt[3]{-27}$ bằng:", ["$-3$", "$3$", "$-9$", "Không tồn tại"], 0, "Vì $(-3)^3 = -27$ nên $\\sqrt[3]{-27} =$ **$-3$**."),
            mcq("biet", "Với mọi số thực $a$, biểu thức $\\sqrt{9a^2}$ bằng:", ["$3|a|$", "$3a$", "$9|a|$", "$-3a$"], 0, "$\\sqrt{9a^2} = \\sqrt{(3a)^2} =$ **$3|a|$**."),
            mcq("hieu", "Giá trị của biểu thức $\\sqrt{(3 - \\sqrt{5})^2} + \\sqrt{5}$ bằng:", ["$3$", "$-3$", "$2\\sqrt{5} - 3$", "$3 + 2\\sqrt{5}$"], 0, "Vì $3 = \\sqrt{9} > \\sqrt{5}$ nên $\\sqrt{(3 - \\sqrt{5})^2} = |3 - \\sqrt{5}| = 3 - \\sqrt{5}$. Suy ra $(3 - \\sqrt{5}) + \\sqrt{5} =$ **$3$**.", note="Luôn kiểm tra dấu biểu thức trong trị tuyệt đối."),
            mcq("hieu", "Rút gọn biểu thức $A = \\sqrt{50} - 3\\sqrt{8} + \\sqrt{32}$ ta được:", ["$3\\sqrt{2}$", "$\\sqrt{2}$", "$5\\sqrt{2}$", "$7\\sqrt{2}$"], 0, "$A = 5\\sqrt{2} - 3 \\cdot 2\\sqrt{2} + 4\\sqrt{2} = (5 - 6 + 4)\\sqrt{2} =$ **$3\\sqrt{2}$**."),
            tf4("hieu", "Xét các phép biến đổi căn thức. Mỗi khẳng định sau đúng hay sai?", ["a) $\\sqrt{16 \\cdot 25} = 4 \\cdot 5 = 20$", "b) $\\sqrt{(-7)^2} = -7$", "c) $\\dfrac{2}{\\sqrt{5} - \\sqrt{3}} = \\sqrt{5} + \\sqrt{3}$", "d) $\\sqrt[3]{8a^3} = 2a$ với mọi số thực $a$"], [True, False, True, True], "a) $\\sqrt{16} \\cdot \\sqrt{25} = 4 \\cdot 5 = 20$ $\\rightarrow$ Đúng.\
b) $\\sqrt{(-7)^2} = |-7| = 7 \\ne -7$ $\\rightarrow$ Sai.\
c) Nhân tử và mẫu với $\\sqrt{5} + \\sqrt{3}$: $\\dfrac{2(\\sqrt{5} + \\sqrt{3})}{5 - 3} = \\sqrt{5} + \\sqrt{3}$ $\\rightarrow$ Đúng.\
d) $\\sqrt[3]{(2a)^3} = 2a$ với mọi $a \\in \\mathbb{R}$ $\\rightarrow$ Đúng."),
            tf4("hieu", "Cho biểu thức $P = \\left(\\dfrac{1}{\\sqrt{x} - 1} + \\dfrac{1}{\\sqrt{x} + 1}\\right) \\cdot \\dfrac{x - 1}{\\sqrt{x}}$ với $x > 0, x \\ne 1$. Mỗi khẳng định sau đúng hay sai?", ["a) Mẫu thức chung của hai phân thức trong ngoặc là $x - 1$", "b) Tổng hai phân thức trong ngoặc rút gọn bằng $\\dfrac{2}{x - 1}$", "c) Sau khi rút gọn, $P = 2$", "d) Giá trị của $P$ không phụ thuộc vào biến $x$ (với $x > 0, x \\ne 1$)"], [True, False, True, True], "a) $(\\sqrt{x} - 1)(\\sqrt{x} + 1) = x - 1$ $\\rightarrow$ Đúng.\
b) Tử thức là $(\\sqrt{x} + 1) + (\\sqrt{x} - 1) = 2\\sqrt{x}$, nên tổng trong ngoặc là $\\dfrac{2\\sqrt{x}}{x - 1}$ $\\rightarrow$ Sai.\
c) $P = \\dfrac{2\\sqrt{x}}{x - 1} \\cdot \\dfrac{x - 1}{\\sqrt{x}} = 2$ $\\rightarrow$ Đúng.\
d) Vì $P = 2$ là hằng số trên miền xác định nên không phụ thuộc vào $x$ $\\rightarrow$ Đúng."),
            mcq("vandung", "Một bể nước hình lập phương có dung tích $27\\text{ m}^3$. Diện tích một mặt đáy của bể nước đó là:", ["$9\\text{ m}^2$", "$3\\text{ m}^2$", "$18\\text{ m}^2$", "$6\\text{ m}^2$"], 0, "Độ dài cạnh bể hình lập phương là $a = \\sqrt[3]{27} = 3\\text{ m}$. Diện tích một mặt đáy là $S = a^2 = 3^2 =$ **$9\\text{ m}^2$**."),
            short("vandung", "Tính giá trị của biểu thức $M = \\dfrac{4}{\\sqrt{5} - 1} - \\sqrt{(\\sqrt{5} - 2)^2}$.", ["3"], "Trục căn thức: $\\dfrac{4}{\\sqrt{5} - 1} = \\dfrac{4(\\sqrt{5} + 1)}{5 - 1} = \\sqrt{5} + 1$. Vì $\\sqrt{5} > 2$ nên $\\sqrt{(\\sqrt{5} - 2)^2} = \\sqrt{5} - 2$. Vậy $M = (\\sqrt{5} + 1) - (\\sqrt{5} - 2) =$ **$3$**."),
        ],
    },
    {
        "topic": "l9-ch04-he-thuc-luong-trong-tam-giac-vuong",
        "title": "Hệ thức lượng trong tam giác vuông",
        "icon": "📐",
        "description": "Chương IV · SGK Toán 9 tập một: Bài 11 – Bài 12. Tỉ số lượng giác của góc nhọn; tỉ số lượng giác của hai góc phụ nhau; một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng giải tam giác vuông.",
        "requirements": [
            "Nhận biết được các giá trị sin (sine), côsin (cosine), tang (tangent), côtang (cotangent) của góc nhọn.",
            "Giải thích được tỉ số lượng giác của các góc nhọn đặc biệt (góc $30^\\circ, 45^\\circ, 60^\\circ$) và của hai góc phụ nhau.",
            "Tính được giá trị (đúng hoặc gần đúng) tỉ số lượng giác của góc nhọn bằng máy tính cầm tay.",
            "Giải thích được một số hệ thức về cạnh và góc trong tam giác vuông (cạnh góc vuông bằng cạnh huyền nhân với sin góc đối hoặc nhân với côsin góc kề; cạnh góc vuông bằng cạnh góc vuông kia nhân với tang góc đối hoặc nhân với côtang góc kề).",
            "Giải quyết được một số vấn đề thực tiễn gắn với tỉ số lượng giác của góc nhọn (ví dụ: tính độ dài đoạn thẳng, độ lớn góc và áp dụng giải tam giác vuông).",
        ],
        "definition": (
            "- Cho góc nhọn $\\alpha$ trong tam giác vuông: $\\sin\\alpha = \\dfrac{\\text{cạnh đối}}{\\text{cạnh huyền}}$; $\\cos\\alpha = \\dfrac{\\text{cạnh kề}}{\\text{cạnh huyền}}$; $\\tan\\alpha = \\dfrac{\\text{cạnh đối}}{\\text{cạnh kề}}$; $\\cot\\alpha = \\dfrac{\\text{cạnh kề}}{\\text{cạnh đối}}$.\n"
            "- **Hai góc phụ nhau** ($\\alpha + \\beta = 90^\\circ$): $\\sin\\alpha = \\cos\\beta$, $\\cos\\alpha = \\sin\\beta$, $\\tan\\alpha = \\cot\\beta$, $\\cot\\alpha = \\tan\\beta$.\n"
            "- **Hệ thức cạnh và góc**: trong $\\triangle ABC$ vuông tại $A$ ($BC = a, AC = b, AB = c$), ta có $b = a\\sin B = a\\cos C$ và $b = c\\tan B = c\\cot C$."
        ),
        "theory": (
            "### Bài 11. Tỉ số lượng giác của góc nhọn\n"
            "- Định nghĩa $\\sin\\alpha, \\cos\\alpha, \\tan\\alpha, \\cot\\alpha$; lưu ý $0 < \\sin\\alpha < 1, 0 < \\cos\\alpha < 1$ và $\\tan\\alpha \\cdot \\cot\\alpha = 1$.\n"
            "- Bảng tỉ số lượng giác của các góc đặc biệt $30^\\circ, 45^\\circ, 60^\\circ$ và định lí tỉ số lượng giác của hai góc phụ nhau.\n"
            "### Bài 12. Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng\n"
            "- Mỗi cạnh góc vuông bằng cạnh huyền nhân với sin góc đối hoặc nhân với côsin góc kề.\n"
            "- Mỗi cạnh góc vuông bằng cạnh góc vuông kia nhân với tang góc đối hoặc nhân với côtang góc kề.\n"
            "- **Giải tam giác vuông**: tìm tất cả các cạnh và góc còn lại của tam giác vuông khi biết hai yếu tố (trong đó có ít nhất một cạnh). Góc nâng và góc hạ trong bài toán thực tế.\n"
            "### Luyện tập chung · Bài tập cuối chương IV"
        ),
        "formulas": [
            G("I. Định nghĩa tỉ số lượng giác", F("Sin và côsin", "$\\sin\\alpha = \\dfrac{\\text{cạnh đối}}{\\text{cạnh huyền}} \\cdot \\cos\\alpha = \\dfrac{\\text{cạnh kề}}{\\text{cạnh huyền}}$"), F("Tang và côtang", "$\\tan\\alpha = \\dfrac{\\text{cạnh đối}}{\\text{cạnh kề}} \\cdot \\cot\\alpha = \\dfrac{\\text{cạnh kề}}{\\text{cạnh đối}}$"), F("Hai góc phụ nhau ($\\alpha + \\beta = 90^\\circ$)", "$\\sin\\alpha = \\cos\\beta \\cdot \\tan\\alpha = \\cot\\beta$")),
            G("II. Góc đặc biệt ($30^\\circ, 45^\\circ, 60^\\circ$)", F("Góc $30^\\circ$", "$\\sin 30^\\circ = \\dfrac{1}{2} \\cdot \\cos 30^\\circ = \\dfrac{\\sqrt{3}}{2} \\cdot \\tan 30^\\circ = \\dfrac{\\sqrt{3}}{3}$"), F("Góc $45^\\circ$", "$\\sin 45^\\circ = \\cos 45^\\circ = \\dfrac{\\sqrt{2}}{2} \\cdot \\tan 45^\\circ = \\cot 45^\\circ = 1$"), F("Góc $60^\\circ$", "$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2} \\cdot \\cos 60^\\circ = \\dfrac{1}{2} \\cdot \\tan 60^\\circ = \\sqrt{3}$")),
            G("III. Hệ thức cạnh và góc ($\\triangle ABC$ vuông tại $A$)", F("Theo cạnh huyền $a$", "$b = a\\sin B = a\\cos C \\cdot c = a\\sin C = a\\cos B$"), F("Theo cạnh góc vuông", "$b = c\\tan B = c\\cot C \\cdot c = b\\tan C = b\\cot B$")),
        ],
        "example": "Cho $\\triangle ABC$ vuông tại $A$ có cạnh huyền $BC = 10\\text{ cm}$ và $\\widehat{B} = 30^\\circ$. Tính độ dài $AC$ và $AB$.",
        "example_answer": (
            "Ta có $AC = BC \\cdot \\sin B = 10 \\cdot \\sin 30^\\circ = 10 \\cdot \\dfrac{1}{2} =$ **$5\\text{ cm}$**.\n"
            "$AB = BC \\cdot \\cos B = 10 \\cdot \\cos 30^\\circ = 10 \\cdot \\dfrac{\\sqrt{3}}{2} =$ **$5\\sqrt{3}\\text{ cm}$**."
        ),
        "real_life": (
            "- Đo chiều cao tháp, cột cờ, cây xanh từ bóng nắng trên mặt đất ($h = d \\cdot \\tan\\alpha$).\n"
            "- Tính khoảng cách từ tàu thuyền đến ngọn hải đăng qua góc hạ, tính độ dốc mặt đường và chiều dài thang an toàn."
        ),
        "quiz": [
            mcq("biet", "Cho $\\triangle ABC$ vuông tại $A$. Tỉ số lượng giác $\\sin B$ được tính bằng:", ["$\\dfrac{AC}{BC}$", "$\\dfrac{AB}{BC}$", "$\\dfrac{AC}{AB}$", "$\\dfrac{AB}{AC}$"], 0, "Đối diện góc $B$ là cạnh $AC$, cạnh huyền là $BC$ $\\Rightarrow \\sin B =$ **$\\dfrac{AC}{BC}$**."),
            mcq("biet", "Giá trị của $\\sin 30^\\circ$ bằng:", ["$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{\\sqrt{2}}{2}$", "$\\sqrt{3}$"], 0, "Theo bảng giá trị lượng giác góc đặc biệt, $\\sin 30^\\circ =$ **$\\dfrac{1}{2}$**."),
            mcq("biet", "Nếu hai góc nhọn $\\alpha$ và $\\beta$ phụ nhau ($\\alpha + \\beta = 90^\\circ$) thì khẳng định nào sau đây **đúng**?", ["$\\sin\\alpha = \\cos\\beta$", "$\\sin\\alpha = \\sin\\beta$", "$\\tan\\alpha = \\tan\\beta$", "$\\cos\\alpha = \\tan\\beta$"], 0, "Hai góc phụ nhau thì sin góc này bằng côsin góc kia: **$\\sin\\alpha = \\cos\\beta$**."),
            mcq("biet", "Cho $\\triangle ABC$ vuông tại $A$ có $BC = a, AC = b, AB = c$. Hệ thức nào sau đây **đúng**?", ["$b = c\\tan B$", "$b = c\\sin B$", "$b = a\\tan B$", "$b = c\\cos B$"], 0, "Cạnh góc vuông bằng cạnh góc vuông kia nhân với tang góc đối: **$b = c\\tan B$**."),
            mcq("hieu", "Cho $\\triangle ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Khi đó $\\cos B$ bằng:", ["$\\dfrac{3}{5}$", "$\\dfrac{4}{5}$", "$\\dfrac{3}{4}$", "$\\dfrac{4}{3}$"], 0, "Theo định lí Pythagore: $BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Suy ra $\\cos B = \\dfrac{AB}{BC} = \\dfrac{6}{10} =$ **$\\dfrac{3}{5}$**."),
            mcq("hieu", "Giá trị của biểu thức $P = \\sin 35^\\circ - \\cos 55^\\circ + \\tan 45^\\circ$ bằng:", ["$1$", "$0$", "$2$", "$\\sqrt{2}$"], 0, "Vì $35^\\circ + 55^\\circ = 90^\\circ$ nên $\\sin 35^\\circ = \\cos 55^\\circ$, và $\\tan 45^\\circ = 1$. Do đó $P = 0 + 1 =$ **$1$**."),
            tf4("hieu", "Cho $\\triangle ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, \\widehat{B} = 60^\\circ$. Mỗi khẳng định sau đúng hay sai?", ["a) $\\widehat{C} = 30^\\circ$", "b) Cạnh huyền $BC = 10\\text{ cm}$", "c) Cạnh góc vuông $AC = 5\\sqrt{3}\\text{ cm}$", "d) $\\tan C = \\sqrt{3}$"], [True, True, True, False], "a) $\\widehat{C} = 90^\\circ - \\widehat{B} = 30^\\circ$ $\\rightarrow$ Đúng.\
b) $AB = BC \\cdot \\cos 60^\\circ \\Rightarrow BC = \\dfrac{5}{\\frac{1}{2}} = 10\\text{ cm}$ $\\rightarrow$ Đúng.\
c) $AC = AB \\cdot \\tan 60^\\circ = 5\\sqrt{3}\\text{ cm}$ $\\rightarrow$ Đúng.\
d) $\\tan C = \\tan 30^\\circ = \\dfrac{\\sqrt{3}}{3} \\ne \\sqrt{3}$ $\\rightarrow$ Sai."),
            tf4("hieu", "Xét các tỉ số lượng giác của góc nhọn. Mỗi khẳng định sau đúng hay sai?", ["a) Với mọi góc nhọn $\\alpha$, ta luôn có $0 < \\sin\\alpha < 1$ và $0 < \\cos\\alpha < 1$", "b) $\\tan 60^\\circ = \\cot 30^\\circ = \\sqrt{3}$", "c) $\\sin 45^\\circ + \\cos 45^\\circ = 1$", "d) Với mọi góc nhọn $\\alpha$, $\\tan\\alpha \\cdot \\cot\\alpha = 1$"], [True, True, False, True], "a) Trong tam giác vuông, cạnh góc vuông luôn nhỏ hơn cạnh huyền $\\rightarrow$ Đúng.\
b) $60^\\circ$ và $30^\\circ$ phụ nhau nên $\\tan 60^\\circ = \\cot 30^\\circ = \\sqrt{3}$ $\\rightarrow$ Đúng.\
c) $\\sin 45^\\circ + \\cos 45^\\circ = \\dfrac{\\sqrt{2}}{2} + \\dfrac{\\sqrt{2}}{2} = \\sqrt{2} \\ne 1$ $\\rightarrow$ Sai.\
d) $\\dfrac{\\text{đối}}{\\text{kề}} \\cdot \\dfrac{\\text{kề}}{\\text{đối}} = 1$ $\\rightarrow$ Đúng."),
            mcq("vandung", "Một chiếc thang dài $6\\text{ m}$ dựa vào tường tạo với mặt đất nằm ngang một góc $60^\\circ$. Khoảng cách từ chân thang đến chân tường là:", ["$3\\text{ m}$", "$3\\sqrt{3}\\text{ m}$", "$3\\sqrt{2}\\text{ m}$", "$4\\text{ m}$"], 0, "Khoảng cách từ chân thang đến tường là cạnh kề góc $60^\\circ$: $d = 6 \\cdot \\cos 60^\\circ = 6 \\cdot \\dfrac{1}{2} =$ **$3\\text{ m}$**."),
            short("vandung", "Tại thời điểm tia nắng mặt trời tạo với mặt đất một góc $45^\\circ$, bóng của một cột cờ trên mặt đất dài $12\\text{ m}$. Chiều cao của cột cờ là bao nhiêu mét?", ["12"], "Chiều cao cột cờ là $h = 12 \\cdot \\tan 45^\\circ = 12 \\cdot 1 =$ **$12\\text{ m}$**.", unit="m"),
        ],
    },
    {
        "topic": "l9-ch05-duong-tron",
        "title": "Đường tròn",
        "icon": "⭕",
        "description": "Chương V · SGK Toán 9 tập một: Bài 13 – Bài 17. Mở đầu về đường tròn; cung và dây của một đường tròn; độ dài của cung tròn, diện tích hình quạt tròn và hình vành khuyên; vị trí tương đối của đường thẳng và đường tròn, tiếp tuyến của đường tròn; vị trí tương đối của hai đường tròn.",
        "requirements": [
            "Nhận biết được tâm đối xứng, trục đối xứng của đường tròn.",
            "So sánh được độ dài của đường kính và dây; nhận biết được góc ở tâm, cung và số đo của cung.",
            "Tính được độ dài cung tròn, diện tích hình quạt tròn, diện tích hình vành khuyên.",
            "Mô tả được ba vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc nhau, không giao nhau); nhận biết được tiếp tuyến của đường tròn và tính chất hai tiếp tuyến cắt nhau.",
            "Mô tả được ba vị trí tương đối của hai đường tròn (cắt nhau, tiếp xúc nhau, không giao nhau).",
        ],
        "definition": (
            "- **Đường tròn tâm $O$ bán kính $R$**, kí hiệu $(O; R)$, gồm các điểm cách $O$ một khoảng bằng $R$. Đường tròn có **tâm đối xứng** là $O$ và **vô số trục đối xứng** (mọi đường thẳng đi qua $O$).\n"
            "- Trong các dây của đường tròn, **đường kính là dây lớn nhất** ($AB \\le 2R$). **Góc ở tâm** là góc có đỉnh trùng với tâm đường tròn; số đo cung nhỏ bằng số đo góc ở tâm chắn cung đó.\n"
            "- **Tiếp tuyến** của đường tròn là đường thẳng chỉ có một điểm chung với đường tròn và vuông góc với bán kính tại tiếp điểm ($d = R$)."
        ),
        "theory": (
            "### Bài 13. Mở đầu về đường tròn\n"
            "- Điểm $M$ nằm trong $(O; R)$ khi $OM < R$; nằm trên $(O; R)$ khi $OM = R$; nằm ngoài $(O; R)$ khi $OM > R$.\n"
            "- Đường tròn có tâm đối xứng là tâm $O$ và trục đối xứng là bất kì đường thẳng nào đi qua $O$.\n"
            "### Bài 14. Cung và dây của một đường tròn\n"
            "- Định lí: Trong một đường tròn, đường kính là dây cung lớn nhất.\n"
            "- Góc ở tâm $\\widehat{AOB}$ ($0^\\circ < \\widehat{AOB} \\le 180^\\circ$) chắn cung nhỏ $AB$: $\\text{sđ}\\overset{\\frown}{AB} = \\widehat{AOB}$; số đo cung lớn bằng $360^\\circ - \\text{sđ}\\overset{\\frown}{AB}$.\n"
            "### Bài 15. Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên\n"
            "- Độ dài cung $n^\\circ$: $l = \\dfrac{\\pi R n}{180}$. Diện tích quạt tròn $n^\\circ$: $S_q = \\dfrac{\\pi R^2 n}{360} = \\dfrac{lR}{2}$.\n"
            "- Diện tích hình vành khuyên giới hạn bởi $(O; R)$ và $(O; r)$ ($R > r$): $S_v = \\pi(R^2 - r^2)$.\n"
            "### Luyện tập chung\n"
            "### Bài 16. Vị trí tương đối của đường thẳng và đường tròn\n"
            "- Khoảng cách từ $O$ đến đường thẳng $a$ là $d$: cắt nhau ($d < R$, $2$ điểm chung); tiếp xúc ($d = R$, $1$ điểm chung); không giao nhau ($d > R$, $0$ điểm chung).\n"
            "- **Tính chất hai tiếp tuyến cắt nhau**: Nếu hai tiếp tuyến của $(O)$ cắt nhau tại $M$ (tiếp điểm $A, B$) thì $MA = MB$, $MO$ là tia phân giác của $\\widehat{AMB}$ và $OM$ là tia phân giác của $\\widehat{AOB}$.\n"
            "### Bài 17. Vị trí tương đối của hai đường tròn\n"
            "- Với hai đường tròn $(O; R)$ và $(O'; r)$ ($R \\ge r$), đặt $d = OO'$: cắt nhau khi $R - r < d < R + r$; tiếp xúc ngoài khi $d = R + r$; tiếp xúc trong khi $d = R - r > 0$; ngoài nhau khi $d > R + r$; đựng nhau khi $d < R - r$.\n"
            "### Luyện tập chung · Bài tập cuối chương V"
        ),
        "formulas": [
            G("I. Cung tròn, hình quạt tròn, vành khuyên", F("Chu vi và diện tích hình tròn", "$C = 2\\pi R \\cdot S = \\pi R^2$"), F("Độ dài cung $n^\\circ$", "$l = \\dfrac{\\pi R n}{180}$"), F("Diện tích hình quạt tròn $n^\\circ$", "$S_q = \\dfrac{\\pi R^2 n}{360} = \\dfrac{l \\cdot R}{2}$"), F("Diện tích hình vành khuyên ($R > r$)", "$S_v = \\pi(R^2 - r^2)$")),
            G("II. Vị trí tương đối và tiếp tuyến", F("Đường thẳng và $(O; R)$", "Cắt nhau: $d < R$ · Tiếp xúc: $d = R$ · Không giao nhau: $d > R$"), F("Hai tiếp tuyến cắt nhau tại $M$", "$MA = MB \\cdot \\widehat{AMO} = \\widehat{BMO} \\cdot \\widehat{AOM} = \\widehat{BOM}$"), F("Hai đường tròn $(O; R)$ và $(O'; r)$", "Cắt nhau: $R - r < OO' < R + r$ · Tiếp xúc ngoài: $OO' = R + r$ · Tiếp xúc trong: $OO' = R - r$")),
        ],
        "example": "Cho đường tròn $(O; 6\\text{ cm})$ và cung $AB$ có số đo $60^\\circ$. Tính độ dài cung $AB$ và diện tích hình quạt tròn $AOB$ (theo $\\pi$).",
        "example_answer": (
            "Độ dài cung $AB$: $l = \\dfrac{\\pi \\cdot 6 \\cdot 60}{180} =$ **$2\\pi\\text{ (cm)}$**.\n"
            "Diện tích hình quạt tròn $AOB$: $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} =$ **$6\\pi\\text{ (cm}^2\\text{)}$**."
        ),
        "real_life": (
            "- Bánh xe lăn trên mặt đường (tiếp tuyến của đường tròn); bộ truyền động bánh răng tiếp xúc ngoài/trong.\n"
            "- Tính diện tích mặt quạt giấy, diện tích mặt cắt ống nhựa hoặc vòng đệm kim loại (hình vành khuyên)."
        ),
        "quiz": [
            mcq("biet", "Đường tròn có bao nhiêu trục đối xứng?", ["Vô số", "$1$", "$2$", "$4$"], 0, "Bất kì đường thẳng nào đi qua tâm đều là trục đối xứng của đường tròn $\\Rightarrow$ **vô số**."),
            mcq("biet", "Trong một đường tròn có bán kính $R = 5\\text{ cm}$, độ dài dây cung lớn nhất bằng:", ["$10\\text{ cm}$", "$5\\text{ cm}$", "$2,5\\text{ cm}$", "$25\\text{ cm}$"], 0, "Dây lớn nhất là đường kính có độ dài $2R = 2 \\cdot 5 =$ **$10\\text{ cm}$**."),
            mcq("biet", "Cho đường tròn $(O; R)$ và đường thẳng $a$, khoảng cách từ tâm $O$ đến $a$ là $d$. Đường thẳng $a$ là tiếp tuyến của $(O; R)$ khi:", ["$d = R$", "$d < R$", "$d > R$", "$d = 2R$"], 0, "Đường thẳng tiếp xúc với đường tròn (là tiếp tuyến) khi và chỉ khi **$d = R$**."),
            mcq("biet", "Công thức tính diện tích hình quạt tròn bán kính $R$ ứng với cung $n^\\circ$ là:", ["$S = \\dfrac{\\pi R^2 n}{360}$", "$S = \\dfrac{\\pi R n}{180}$", "$S = \\dfrac{\\pi R^2 n}{180}$", "$S = \\pi R^2 n$"], 0, "Diện tích hình quạt tròn ứng với cung $n^\\circ$ là **$S = \\dfrac{\\pi R^2 n}{360}$**."),
            mcq("hieu", "Từ điểm $M$ nằm ngoài đường tròn $(O; 3\\text{ cm})$, kẻ tiếp tuyến $MA$ ($A$ là tiếp điểm). Biết $OM = 5\\text{ cm}$, độ dài đoạn thẳng $MA$ bằng:", ["$4\\text{ cm}$", "$\\sqrt{34}\\text{ cm}$", "$2\\text{ cm}$", "$8\\text{ cm}$"], 0, "Vì $MA$ là tiếp tuyến nên $OA \\perp MA$ tại $A$. Theo định lí Pythagore trong $\\triangle OAM$ vuông tại $A$: $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{5^2 - 3^2} =$ **$4\\text{ cm}$**."),
            mcq("hieu", "Cho hai đường tròn $(O; 5\\text{ cm})$ và $(O'; 3\\text{ cm})$ có khoảng cách hai tâm $OO' = 8\\text{ cm}$. Vị trí tương đối của hai đường tròn là:", ["Tiếp xúc ngoài", "Cắt nhau", "Tiếp xúc trong", "Ở ngoài nhau"], 0, "Ta có $OO' = 8\\text{ cm} = 5 + 3 = R + r$ nên hai đường tròn **tiếp xúc ngoài**."),
            tf4("hieu", "Cho đường tròn $(O; 6\\text{ cm})$ và hai điểm $A, B$ thuộc đường tròn sao cho $\\widehat{AOB} = 90^\\circ$. Mỗi khẳng định sau đúng hay sai?", ["a) Số đo cung nhỏ $AB$ bằng $90^\\circ$", "b) Độ dài cung nhỏ $AB$ bằng $3\\pi\\text{ cm}$", "c) Diện tích hình quạt tròn $AOB$ (ứng với cung nhỏ) bằng $9\\pi\\text{ cm}^2$", "d) Độ dài dây $AB$ bằng $6\\text{ cm}$"], [True, True, True, False], "a) Số đo cung nhỏ bằng góc ở tâm $\\widehat{AOB} = 90^\\circ$ $\\rightarrow$ Đúng.\
b) $l = \\dfrac{\\pi \\cdot 6 \\cdot 90}{180} = 3\\pi\\text{ cm}$ $\\rightarrow$ Đúng.\
c) $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 90}{360} = 9\\pi\\text{ cm}^2$ $\\rightarrow$ Đúng.\
d) $\\triangle OAB$ vuông cân tại $O$ nên $AB = 6\\sqrt{2}\\text{ cm} \\ne 6\\text{ cm}$ $\\rightarrow$ Sai."),
            tf4("hieu", "Từ điểm $M$ nằm ngoài đường tròn $(O; R)$, kẻ hai tiếp tuyến $MA, MB$ tới đường tròn ($A, B$ là hai tiếp điểm). Mỗi khẳng định sau đúng hay sai?", ["a) $MA = MB$", "b) Tia $MO$ là tia phân giác của $\\widehat{AMB}$", "c) Đường thẳng $OM$ vuông góc với đoạn thẳng $AB$", "d) $\\widehat{OAM} + \\widehat{OBM} = 90^\\circ$"], [True, True, True, False], "a), b) Theo tính chất hai tiếp tuyến cắt nhau $\\rightarrow$ Đúng.\
c) $OA = OB = R$ và $MA = MB$ nên $OM$ là đường trung trực của $AB \\Rightarrow OM \\perp AB$ $\\rightarrow$ Đúng.\
d) $\\widehat{OAM} = 90^\\circ$ và $\\widehat{OBM} = 90^\\circ$ nên tổng bằng $180^\\circ$ $\\rightarrow$ Sai."),
            mcq("vandung", "Một đồng hồ treo tường có kim phút dài $10\\text{ cm}$. Khi kim phút quay được $30$ phút thì đầu kim phút vạch nên một cung tròn có độ dài là:", ["$10\\pi\\text{ cm}$", "$5\\pi\\text{ cm}$", "$20\\pi\\text{ cm}$", "$15\\pi\\text{ cm}$"], 0, "Trong $30$ phút, kim phút quay được góc $n = 180^\\circ$. Độ dài cung tròn là $l = \\dfrac{\\pi \\cdot 10 \\cdot 180}{180} =$ **$10\\pi\\text{ cm}$**."),
            short("vandung", "Một chiếc đĩa CD có dạng hình vành khuyên với bán kính ngoài $R = 6\\text{ cm}$ và bán kính lỗ tròn đồng tâm bên trong $r = 2\\text{ cm}$. Diện tích bề mặt chiếc đĩa bằng $k\\pi\\text{ cm}^2$. Tìm giá trị của $k$.", ["32"], "Diện tích hình vành khuyên là $S = \\pi(R^2 - r^2) = \\pi(6^2 - 2^2) = 32\\pi\\text{ cm}^2 \\Rightarrow k =$ **$32$**."),
        ],
    },
    {
        "topic": "l9-ch06-ham-so-bac-hai-va-phuong-trinh-bac-hai-mot-an",
        "title": "Hàm số bậc hai và phương trình bậc hai một ẩn",
        "icon": "🏹",
        "description": "Chương VI · SGK Toán 9 tập hai: Bài 18 – Bài 21. Hàm số bậc hai và đồ thị parabol; phương trình bậc hai một ẩn và công thức nghiệm; định lí Viète và ứng dụng; giải bài toán bằng cách lập phương trình bậc hai.",
        "requirements": [
            "Nhận biết được hàm số $y = ax^2$ ($a \\ne 0$) và vẽ được đồ thị (parabol) của hàm số này; nhận biết được tính đối xứng (trục đối xứng) của đồ thị.",
            "Nhận biết được khái niệm phương trình bậc hai một ẩn; giải được phương trình bậc hai một ẩn và tính được nghiệm bằng máy tính cầm tay.",
            "Giải thích được định lí Viète và ứng dụng (ví dụ: tính nhẩm nghiệm của phương trình bậc hai, tìm hai số biết tổng và tích của chúng).",
            "Vận dụng được hàm số $y = ax^2$ ($a \\ne 0$) và phương trình bậc hai một ẩn vào giải quyết một số bài toán thực tiễn.",
        ],
        "definition": (
            "- **Hàm số $y = ax^2$ ($a \\ne 0$)** xác định với mọi $x \\in \\mathbb{R}$. Đồ thị là một đường cong **parabol** có đỉnh là gốc toạ độ $O(0; 0)$ và nhận trục $Oy$ làm trục đối xứng ($a > 0$: nằm phía trên trục hoành; $a < 0$: nằm phía dưới trục hoành).\n"
            "- **Phương trình bậc hai một ẩn** có dạng $ax^2 + bx + c = 0$ ($a \\ne 0$). Biệt thức $\\Delta = b^2 - 4ac$ (hoặc $\\Delta' = b'^2 - ac$ với $b = 2b'$).\n"
            "- **Định lí Viète**: Nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ ($a \\ne 0$) thì $\\begin{cases} x_1 + x_2 = -\\dfrac{b}{a} \\\\ x_1 x_2 = \\dfrac{c}{a} \\end{cases}$."
        ),
        "theory": (
            "### Bài 18. Hàm số $y = ax^2$ ($a \\ne 0$)\n"
            "- Cách vẽ đồ thị: lập bảng giá trị gồm $5$ điểm đối xứng qua trục $Oy$ (trong đó có đỉnh $O(0; 0)$) rồi nối thành đường parabol trơn.\n"
            "### Bài 19. Phương trình bậc hai một ẩn\n"
            "- Tính $\\Delta = b^2 - 4ac$: nếu $\\Delta > 0$ có $2$ nghiệm phân biệt $x_{1,2} = \\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$; nếu $\\Delta = 0$ có nghiệm kép $x_1 = x_2 = -\\dfrac{b}{2a}$; nếu $\\Delta < 0$ phương trình vô nghiệm.\n"
            "### Luyện tập chung\n"
            "### Bài 20. Định lí Viète và ứng dụng\n"
            "- **Nhẩm nghiệm**: Nếu $a + b + c = 0$ thì $x_1 = 1, x_2 = \\dfrac{c}{a}$. Nếu $a - b + c = 0$ thì $x_1 = -1, x_2 = -\\dfrac{c}{a}$.\n"
            "- **Tìm hai số biết tổng $S$ và tích $P$**: Hai số đó là nghiệm của phương trình $x^2 - Sx + P = 0$ (điều kiện $S^2 - 4P \\ge 0$).\n"
            "### Bài 21. Giải bài toán bằng cách lập phương trình\n"
            "- Chọn ẩn và đặt điều kiện $\\rightarrow$ lập phương trình bậc hai $\\rightarrow$ giải phương trình và đối chiếu điều kiện $\\rightarrow$ kết luận.\n"
            "### Luyện tập chung · Bài tập cuối chương VI"
        ),
        "formulas": [
            G("I. Công thức nghiệm phương trình $ax^2 + bx + c = 0$ ($a \\ne 0$)", F("Biệt thức $\\Delta$", "$\\Delta = b^2 - 4ac$"), F("Khi $\\Delta > 0$", "$x_1 = \\dfrac{-b + \\sqrt{\\Delta}}{2a} \\cdot x_2 = \\dfrac{-b - \\sqrt{\\Delta}}{2a}$"), F("Khi $\\Delta = 0$ (nghiệm kép)", "$x_1 = x_2 = -\\dfrac{b}{2a}$"), F("Công thức nghiệm thu gọn ($b = 2b'$)", "$\\Delta' = b'^2 - ac \\cdot x_{1,2} = \\dfrac{-b' \\pm \\sqrt{\\Delta'}}{a}$")),
            G("II. Định lí Viète và hệ quả", F("Hệ thức Viète ($\\Delta \\ge 0$)", "$S = x_1 + x_2 = -\\dfrac{b}{a} \\cdot P = x_1 x_2 = \\dfrac{c}{a}$"), F("Biểu thức đối xứng thường gặp", "$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = S^2 - 2P$"), F("Nhẩm nghiệm đặc biệt", "$a + b + c = 0 \\Rightarrow x_1 = 1, x_2 = \\dfrac{c}{a} \\cdot a - b + c = 0 \\Rightarrow x_1 = -1, x_2 = -\\dfrac{c}{a}$")),
        ],
        "example": "Không giải phương trình, hãy tính tổng và tích các nghiệm của phương trình $2x^2 - 7x + 3 = 0$, từ đó tính $A = x_1^2 + x_2^2$.",
        "example_answer": (
            "Ta có $\\Delta = (-7)^2 - 4 \\cdot 2 \\cdot 3 = 25 > 0$ nên phương trình có hai nghiệm $x_1, x_2$.\n"
            "Theo định lí Viète: $x_1 + x_2 = \\dfrac{7}{2}$ và $x_1 x_2 = \\dfrac{3}{2}$.\n"
            "Suy ra $A = (x_1 + x_2)^2 - 2x_1 x_2 = \\left(\\dfrac{7}{2}\\right)^2 - 2 \\cdot \\dfrac{3}{2} = \\dfrac{49}{4} - 3 =$ **$\\dfrac{37}{4}$**."
        ),
        "real_life": (
            "- Quỹ đạo ném bóng, tia nước đài phun, mặt cắt chảo thu sóng vệ tinh và pha đèn ô tô đều có dạng parabol.\n"
            "- Bài toán tính kích thước mảnh đất khi biết chu vi và diện tích, bài toán chuyển động biến đổi đều."
        ),
        "quiz": [
            mcq("biet", "Đồ thị của hàm số $y = 2x^2$ đi qua điểm nào sau đây?", ["$(1; 2)$", "$(1; 4)$", "$(2; 4)$", "$(-1; -2)$"], 0, "Thay $x = 1$ vào $y = 2x^2$ được $y = 2 \\cdot 1^2 = 2$ $\\Rightarrow$ đồ thị đi qua điểm **$(1; 2)$**."),
            mcq("biet", "Biệt thức $\\Delta$ của phương trình bậc hai $x^2 - 5x + 6 = 0$ bằng:", ["$1$", "$49$", "$-1$", "$25$"], 0, "$\\Delta = b^2 - 4ac = (-5)^2 - 4 \\cdot 1 \\cdot 6 = 25 - 24 =$ **$1$**."),
            mcq("biet", "Gọi $x_1, x_2$ là hai nghiệm của phương trình $x^2 - 6x + 8 = 0$. Theo định lí Viète, tổng $x_1 + x_2$ bằng:", ["$6$", "$-6$", "$8$", "$-8$"], 0, "$x_1 + x_2 = -\\dfrac{b}{a} = -\\dfrac{-6}{1} =$ **$6$**."),
            mcq("biet", "Phương trình $3x^2 - 5x + 2 = 0$ có các hệ số thoả mãn $a + b + c = 0$ nên có hai nghiệm là:", ["$x_1 = 1; x_2 = \\dfrac{2}{3}$", "$x_1 = -1; x_2 = -\\dfrac{2}{3}$", "$x_1 = 1; x_2 = -\\dfrac{2}{3}$", "$x_1 = -1; x_2 = \\dfrac{2}{3}$"], 0, "Vì $3 + (-5) + 2 = 0$ nên phương trình có nghiệm **$x_1 = 1; x_2 = \\dfrac{c}{a} = \\dfrac{2}{3}$**."),
            mcq("hieu", "Cho phương trình $x^2 - 4x + 1 = 0$ có hai nghiệm $x_1, x_2$. Giá trị của biểu thức $x_1^2 + x_2^2$ bằng:", ["$14$", "$16$", "$15$", "$18$"], 0, "Theo định lí Viète: $x_1 + x_2 = 4, x_1 x_2 = 1$. Do đó $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 4^2 - 2 \\cdot 1 =$ **$14$**."),
            mcq("hieu", "Biết đồ thị hàm số $y = ax^2$ ($a \\ne 0$) đi qua điểm $M(-2; -8)$. Giá trị của hệ số $a$ là:", ["$-2$", "$2$", "$-4$", "$4$"], 0, "Thay $x = -2, y = -8$ vào $y = ax^2$: $-8 = a \\cdot (-2)^2 \\Leftrightarrow 4a = -8 \\Leftrightarrow a =$ **$-2$**."),
            tf4("hieu", "Cho hàm số $y = \\dfrac{1}{2}x^2$ có đồ thị là parabol $(P)$. Mỗi khẳng định sau đúng hay sai?", ["a) Đồ thị $(P)$ có đỉnh là gốc toạ độ $O(0; 0)$ và nhận trục $Oy$ làm trục đối xứng", "b) Mọi điểm của $(P)$ trừ gốc toạ độ đều nằm phía trên trục hoành", "c) Điểm $A(2; 2)$ và điểm $B(-2; -2)$ cùng thuộc đồ thị $(P)$", "d) Đường thẳng $y = 2$ cắt $(P)$ tại hai điểm phân biệt có hoành độ là $2$ và $-2$"], [True, True, False, True], "a) Tính chất đồ thị $y = ax^2$ $\\rightarrow$ Đúng.\
b) Hệ số $a = \\dfrac{1}{2} > 0$ nên $(P)$ nằm phía trên trục hoành $\\rightarrow$ Đúng.\
c) Tại $x = -2$ thì $y = \\dfrac{1}{2}(-2)^2 = 2 \\ne -2$ nên $B(-2; -2) \\notin (P)$ $\\rightarrow$ Sai.\
d) $\\dfrac{1}{2}x^2 = 2 \\Leftrightarrow x^2 = 4 \\Leftrightarrow x = \\pm 2$ $\\rightarrow$ Đúng."),
            tf4("hieu", "Cho phương trình bậc hai $x^2 - 5x + 6 = 0$. Mỗi khẳng định sau đúng hay sai?", ["a) Phương trình có biệt thức $\\Delta = 1 > 0$", "b) Tổng hai nghiệm của phương trình là $-5$ và tích hai nghiệm là $6$", "c) Hai nghiệm của phương trình là $x_1 = 2$ và $x_2 = 3$", "d) Biểu thức $\\dfrac{1}{x_1} + \\dfrac{1}{x_2}$ có giá trị bằng $\\dfrac{5}{6}$"], [True, False, True, True], "a) $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = 1 > 0$ $\\rightarrow$ Đúng.\
b) $x_1 + x_2 = -\\dfrac{-5}{1} = 5$ (không phải $-5$) $\\rightarrow$ Sai.\
c) $2 + 3 = 5$ và $2 \\cdot 3 = 6$ nên hai nghiệm là $2$ và $3$ $\\rightarrow$ Đúng.\
d) $\\dfrac{1}{x_1} + \\dfrac{1}{x_2} = \\dfrac{x_1 + x_2}{x_1 x_2} = \\dfrac{5}{6}$ $\\rightarrow$ Đúng."),
            mcq("vandung", "Một mảnh đất hình chữ nhật có chiều dài hơn chiều rộng $7\\text{ m}$ và diện tích bằng $120\\text{ m}^2$. Chu vi của mảnh đất đó là:", ["$46\\text{ m}$", "$23\\text{ m}$", "$50\\text{ m}$", "$44\\text{ m}$"], 0, "Gọi chiều rộng là $x$ ($\\text{m}, x > 0$), chiều dài là $x + 7$. Ta có $x(x + 7) = 120 \\Leftrightarrow x^2 + 7x - 120 = 0 \\Rightarrow x = 8$ (nhận) hoặc $x = -15$ (loại). Chiều dài là $15\\text{ m}$. Chu vi mảnh đất là $2(8 + 15) =$ **$46\\text{ m}$**."),
            short("vandung", "Tìm giá trị dương của tham số $m$ để phương trình $x^2 - 6x + m = 0$ có hai nghiệm $x_1, x_2$ thoả mãn $x_1^2 + x_2^2 = 20$.", ["8"], "Theo định lí Viète: $x_1 + x_2 = 6, x_1 x_2 = m$ (điều kiện $\\Delta' = 9 - m \\ge 0 \\Leftrightarrow m \\le 9$). Ta có $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 \\Leftrightarrow 36 - 2m = 20 \\Leftrightarrow m =$ **$8$** (thoả mãn $m \\le 9$)."),
        ],
    },
    {
        "topic": "l9-ch07-tan-so-va-tan-so-tuong-doi",
        "title": "Tần số và tần số tương đối",
        "icon": "📊",
        "description": "Chương VII · SGK Toán 9 tập hai: Bài 22 – Bài 24. Bảng tần số và biểu đồ tần số; bảng tần số tương đối và biểu đồ tần số tương đối; bảng tần số, tần số tương đối ghép nhóm và biểu đồ.",
        "requirements": [
            "Xác định được tần số ($m_i$) của một giá trị; thiết lập được bảng tần số, biểu đồ tần số (biểu đồ cột hoặc biểu đồ đoạn thẳng).",
            "Giải thích được ý nghĩa và xác định được tần số tương đối ($f_i$) của một giá trị; thiết lập được bảng tần số tương đối, biểu đồ tần số tương đối (biểu đồ cột hoặc biểu đồ hình quạt tròn).",
            "Thiết lập được bảng tần số ghép nhóm, bảng tần số tương đối ghép nhóm.",
            "Thiết lập được biểu đồ tần số tương đối ghép nhóm (histogram) ở dạng biểu đồ cột hoặc biểu đồ đoạn thẳng.",
            "Nhận biết được mối liên hệ giữa thống kê với những kiến thức của các môn học khác và trong thực tiễn.",
        ],
        "definition": (
            "- **Tần số** $m$ của một giá trị là số lần xuất hiện giá trị đó trong mẫu dữ liệu. Tổng các tần số bằng cỡ mẫu $N = m_1 + m_2 + \\dots + m_k$.\n"
            "- **Tần số tương đối** (tỉ lệ phần trăm) của giá trị $x_i$ là $f_i = \\dfrac{m_i}{N}$ (thường viết dưới dạng phần trăm $\\dfrac{m_i}{N} \\cdot 100\\%$). Tổng tất cả các tần số tương đối bằng $1$ (hay $100\\%$).\n- **Mẫu số liệu ghép nhóm**: chia miền giá trị thành các nửa khoảng $[a; b)$ (nhóm) có độ dài bằng nhau để lập bảng tần số và tần số tương đối ghép nhóm."
        ),
        "theory": (
            "### Bài 22. Bảng tần số và biểu đồ tần số\n"
            "- Bảng tần số gồm hai dòng (hoặc hai cột): dòng trên ghi các giá trị khác nhau $x_1, x_2, \\dots, x_k$, dòng dưới ghi các tần số tương ứng $m_1, m_2, \\dots, m_k$.\n"
            "- Biểu đồ tần số thường dùng dạng **biểu đồ cột** hoặc **biểu đồ đoạn thẳng**.\n"
            "### Bài 23. Bảng tần số tương đối và biểu đồ tần số tương đối\n"
            "- Tính $f_i = \\dfrac{m_i}{N} \\cdot 100\\%$. Biểu đồ tần số tương đối thường dùng **biểu đồ cột** hoặc **biểu đồ hình quạt tròn** (số đo góc tâm quạt ứng với $f_i$ là $360^\\circ \\cdot f_i$).\n"
            "### Luyện tập chung\n"
            "### Bài 24. Bảng tần số, tần số tương đối ghép nhóm và biểu đồ\n"
            "- Nhóm $[a; b)$ gồm các giá trị $x$ thoả mãn $a \\le x < b$. Biểu đồ tần số tương đối ghép nhóm dạng cột có các cột kề sát nhau (histogram) hoặc dạng đoạn thẳng nối các điểm có hoành độ là giá trị đại diện $c_i = \\dfrac{a_i + b_i}{2}$.\n"
            "### Bài tập cuối chương VII"
        ),
        "formulas": [
            G("I. Tần số và tần số tương đối", F("Cỡ mẫu (tổng tần số)", "$N = m_1 + m_2 + \\dots + m_k$"), F("Tần số tương đối", "$f_i = \\dfrac{m_i}{N} = \\dfrac{m_i}{N} \\cdot 100\\%$"), F("Tổng tần số tương đối", "$f_1 + f_2 + \\dots + f_k = 1 = 100\\%$"), F("Góc ở tâm trên biểu đồ quạt tròn", "$\\alpha_i = f_i \\cdot 360^\\circ = \\dfrac{m_i}{N} \\cdot 360^\\circ$")),
            G("II. Số liệu ghép nhóm", F("Quy ước nhóm $[a; b)$", "Gồm các giá trị $x$ sao cho $a \\le x < b$"), F("Giá trị đại diện của nhóm $[a_i; b_i)$", "$c_i = \\dfrac{a_i + b_i}{2}$")),
        ],
        "example": "Khảo sát cỡ giày của $40$ học sinh lớp 9A, kết quả có $10$ bạn đi cỡ $38$, $18$ bạn đi cỡ $39$, $8$ bạn đi cỡ $40$ và $4$ bạn đi cỡ $41$. Tính tần số tương đối của cỡ giày $39$.",
        "example_answer": (
            "Cỡ mẫu là $N = 10 + 18 + 8 + 4 = 40$; tần số của cỡ giày $39$ là $m = 18$.\n"
            "Tần số tương đối của cỡ giày $39$ là $f = \\dfrac{18}{40} \\cdot 100\\% = 0,45 \\cdot 100\\% =$ **$45\\%$**."
        ),
        "real_life": (
            "- Thống kê điểm thi tuyển sinh vào lớp 10 theo từng khung điểm (ghép nhóm).\n"
            "- Phân tích cơ cấu thị phần, tỉ lệ nhóm máu, thời gian tự học hoặc chiều cao của học sinh trong trường."
        ),
        "quiz": [
            mcq("biet", "Trong một mẫu dữ liệu có cỡ mẫu $N$, nếu giá trị $x_i$ xuất hiện $m_i$ lần thì tần số tương đối $f_i$ của giá trị đó được tính bởi công thức:", ["$f_i = \\dfrac{m_i}{N}$", "$f_i = \\dfrac{N}{m_i}$", "$f_i = m_i \\cdot N$", "$f_i = N - m_i$"], 0, "Tần số tương đối bằng tỉ số giữa tần số $m_i$ và cỡ mẫu $N$: **$f_i = \\dfrac{m_i}{N}$**."),
            mcq("biet", "Tổng tất cả các tần số tương đối của các giá trị khác nhau trong một bảng tần số tương đối luôn bằng:", ["$100\\%$", "$50\\%$", "$360\\%$", "Cỡ mẫu $N$"], 0, "Tổng các tần số tương đối luôn bằng $1$ hay **$100\\%$**."),
            mcq("biet", "Trong bảng tần số ghép nhóm, nhóm $[150; 160)$ bao gồm các số liệu $x$ thoả mãn điều kiện nào?", ["$150 \\le x < 160$", "$150 < x \\le 160$", "$150 \\le x \\le 160$", "$150 < x < 160$"], 0, "Nửa khoảng $[150; 160)$ gồm các giá trị lớn hơn hoặc bằng $150$ và nhỏ hơn $160$: **$150 \\le x < 160$**."),
            mcq("biet", "Giá trị đại diện của nhóm $[20; 30)$ dùng khi vẽ biểu đồ đoạn thẳng là:", ["$25$", "$20$", "$30$", "$10$"], 0, "Giá trị đại diện là trung bình cộng hai đầu mút: $c = \\dfrac{20 + 30}{2} =$ **$25$**."),
            mcq("hieu", "Trong một cuộc khảo sát $50$ học sinh về môn thể thao yêu thích, có $15$ bạn chọn Cầu lông. Tần số tương đối của môn Cầu lông là:", ["$30\\%$", "$15\\%$", "$35\\%$", "$25\\%$"], 0, "Tần số tương đối: $f = \\dfrac{15}{50} \\cdot 100\\% =$ **$30\\%$**."),
            mcq("hieu", "Khi biểu diễn bảng tần số tương đối bằng biểu đồ hình quạt tròn, một nhóm có tần số tương đối $25\\%$ sẽ ứng với hình quạt có góc ở tâm bằng:", ["$90^\\circ$", "$25^\\circ$", "$45^\\circ$", "$72^\\circ$"], 0, "Số đo góc ở tâm là $25\\% \\cdot 360^\\circ = 0,25 \\cdot 360^\\circ =$ **$90^\\circ$**."),
            tf4("hieu", "Điểm kiểm tra môn Toán của học sinh lớp 9B được thống kê như sau: điểm $7$ có $8$ em; điểm $8$ có $16$ em; điểm $9$ có $12$ em; điểm $10$ có $4$ em. Mỗi khẳng định sau đúng hay sai?", ["a) Cỡ mẫu (tổng số học sinh lớp 9B) là $N = 40$", "b) Tần số của điểm $8$ là $16$", "c) Tần số tương đối của điểm $9$ là $30\\%$", "d) Tần số tương đối của các học sinh đạt từ $9$ điểm trở lên là $50\\%$"], [True, True, True, False], "a) $N = 8 + 16 + 12 + 4 = 40$ $\\rightarrow$ Đúng.\
b) Điểm $8$ có $16$ em nên tần số bằng $16$ $\\rightarrow$ Đúng.\
c) $f_9 = \\dfrac{12}{40} \\cdot 100\\% = 30\\%$ $\\rightarrow$ Đúng.\
d) Từ $9$ điểm trở lên có $12 + 4 = 16$ em, chiếm $\\dfrac{16}{40} \\cdot 100\\% = 40\\% \\ne 50\\%$ $\\rightarrow$ Sai."),
            tf4("hieu", "Khảo sát thời gian tự học mỗi ngày (đơn vị: phút) của một nhóm học sinh thu được bảng ghép nhóm gồm $3$ nhóm: $[30; 60)$ có $12$ em; $[60; 90)$ có $20$ em; $[90; 120)$ có $8$ em. Mỗi khẳng định sau đúng hay sai?", ["a) Một bạn tự học đúng $60$ phút được xếp vào nhóm $[60; 90)$", "b) Tổng số học sinh được khảo sát là $40$ em", "c) Giá trị đại diện của nhóm $[30; 60)$ là $45$", "d) Tần số tương đối của nhóm $[90; 120)$ là $25\\%$"], [True, True, True, False], "a) Nhóm $[60; 90)$ gồm $60 \\le x < 90$ nên $x = 60$ thuộc nhóm này $\\rightarrow$ Đúng.\
b) $N = 12 + 20 + 8 = 40$ $\\rightarrow$ Đúng.\
c) $\\dfrac{30 + 60}{2} = 45$ $\\rightarrow$ Đúng.\
d) $f = \\dfrac{8}{40} \\cdot 100\\% = 20\\% \\ne 25\\%$ $\\rightarrow$ Sai."),
            mcq("vandung", "Một trường THCS khảo sát $200$ học sinh khối 9 về phương tiện đi học. Biết tần số tương đối của các bạn đi xe đạp là $45\\%$, đi xe buýt là $20\\%$, còn lại là được phụ huynh đưa đón. Số học sinh được phụ huynh đưa đón là:", ["$70$ học sinh", "$65$ học sinh", "$90$ học sinh", "$35$ học sinh"], 0, "Tần số tương đối của học sinh được phụ huynh đưa đón là $100\\% - (45\\% + 20\\%) = 35\\%$. Số học sinh tương ứng là $200 \\cdot 35\\% =$ **$70$ học sinh**."),
            short("vandung", "Trong một mẫu dữ liệu thống kê, giá trị $x_1$ có tần số $m_1 = 18$ và chiếm tần số tương đối $f_1 = 36\\%$. Cỡ mẫu $N$ của mẫu dữ liệu đó bằng bao nhiêu?", ["50"], "Từ $f_1 = \\dfrac{m_1}{N} \\Rightarrow N = \\dfrac{m_1}{f_1} = \\dfrac{18}{0,36} =$ **$50$**."),
        ],
    },
    {
        "topic": "l9-ch08-xac-suat-cua-bien-co-trong-mot-so-mo-hinh-xac-suat-don-gian",
        "title": "Xác suất của biến cố trong một số mô hình xác suất đơn giản",
        "icon": "🎲",
        "description": "Chương VIII · SGK Toán 9 tập hai: Bài 25 – Bài 26. Phép thử ngẫu nhiên và không gian mẫu; xác suất của biến cố liên quan tới phép thử bằng cách kiểm đếm số kết quả có thể và số kết quả thuận lợi.",
        "requirements": [
            "Nhận biết được phép thử ngẫu nhiên và không gian mẫu ($\\Omega$).",
            "Xác định được số phần tử của không gian mẫu và số kết quả thuận lợi cho một biến cố trong các phép thử đơn giản (tung đồng xu, gieo xúc xắc, rút thẻ, chọn vật từ hộp).",
            "Tính được xác suất của biến cố bằng cách kiểm đếm số trường hợp có thể và số trường hợp thuận lợi trong một số mô hình xác suất đơn giản khi các kết quả đồng khả năng.",
        ],
        "definition": (
            "- **Phép thử ngẫu nhiên** (gọi tắt là phép thử) là một thí nghiệm hay hành động mà ta không đoán trước được kết quả của nó, nhưng biết được tập hợp tất cả các kết quả có thể xảy ra.\n"
            "- **Không gian mẫu** $\\Omega$ là tập hợp tất cả các kết quả có thể xảy ra của phép thử.\n"
            "- Khi các kết quả của phép thử là **đồng khả năng**, **xác suất của biến cố $A$** là $P(A) = \\dfrac{n(A)}{n(\\Omega)}$, trong đó $n(\\Omega)$ là số phần tử của không gian mẫu và $n(A)$ là số kết quả thuận lợi cho biến cố $A$."
        ),
        "theory": (
            "### Bài 25. Phép thử ngẫu nhiên và không gian mẫu\n"
            "- Liệt kê các phần tử của không gian mẫu $\\Omega$ bằng cách lập bảng hoặc vẽ sơ đồ hình cây (ví dụ: tung một đồng xu $2$ lần liên tiếp có $\\Omega = \\{\\text{SS}; \\text{SN}; \\text{NS}; \\text{NN}\\}$, gồm $4$ phần tử).\n"
            "### Bài 26. Xác suất của biến cố liên quan tới phép thử\n"
            "- Các bước tính xác suất của biến cố $A$: Bước 1: Xác định không gian mẫu $\\Omega$ và đếm $n(\\Omega)$. Bước 2: Kiểm đếm các kết quả thuận lợi cho $A$ để tìm $n(A)$. Bước 3: Lập tỉ số $P(A) = \\dfrac{n(A)}{n(\\Omega)}$.\n"
            "- Với mọi biến cố $A$, luôn có $0 \\le P(A) \\le 1$. Biến cố không thể có $P = 0$, biến cố chắc chắn có $P = 1$.\n"
            "### Luyện tập chung · Bài tập cuối chương VIII"
        ),
        "formulas": [
            G("I. Không gian mẫu thường gặp", F("Tung đồng xu $2$ lần", "$\\Omega = \\{\\text{SS}; \\text{SN}; \\text{NS}; \\text{NN}\\} \\Rightarrow n(\\Omega) = 4$"), F("Gieo $1$ xúc xắc ($6$ mặt)", "$n(\\Omega) = 6$"), F("Gieo $2$ xúc xắc cân đối", "$n(\\Omega) = 6 \\cdot 6 = 36$")),
            G("II. Công thức xác suất cổ điển", F("Xác suất của biến cố $A$", "$P(A) = \\dfrac{n(A)}{n(\\Omega)}$", "Áp dụng khi các kết quả của phép thử đồng khả năng."), F("Tính chất", "$0 \\le P(A) \\le 1 \\cdot P(\\overline{A}) = 1 - P(A)$")),
        ],
        "example": "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Tính xác suất của biến cố $A$: “Tổng số chấm xuất hiện trên hai con xúc xắc bằng $7$”.",
        "example_answer": (
            "Số phần tử của không gian mẫu là $n(\\Omega) = 6 \\cdot 6 = 36$ (các kết quả đồng khả năng).\n"
            "Các kết quả thuận lợi cho $A$ là: $(1; 6), (2; 5), (3; 4), (4; 3), (5; 2), (6; 1) \\Rightarrow n(A) = 6$.\n"
            "Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{6}{36} =$ **$\\dfrac{1}{6}$**."
        ),
        "real_life": (
            "- Tính xác suất trúng thưởng trong các trò chơi quay số, rút thăm.\n"
            "- Ứng dụng trong di truyền học (xác suất kiểu hình đời con trong phép lai Mendel), kiểm định chất lượng sản phẩm."
        ),
        "quiz": [
            mcq("biet", "Tung một đồng xu cân đối hai lần liên tiếp. Số phần tử của không gian mẫu $\\Omega$ là:", ["$4$", "$2$", "$6$", "$8$"], 0, "$\\Omega = \\{\\text{SS}; \\text{SN}; \\text{NS}; \\text{NN}\\}$ có **$4$** phần tử."),
            mcq("biet", "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Số phần tử của không gian mẫu là:", ["$36$", "$12$", "$6$", "$18$"], 0, "Mỗi con xúc xắc có $6$ kết quả nên số phần tử của không gian mẫu là $6 \\cdot 6 =$ **$36$**."),
            mcq("biet", "Khi các kết quả của phép thử là đồng khả năng, xác suất của biến cố $A$ được tính theo công thức:", ["$P(A) = \\dfrac{n(A)}{n(\\Omega)}$", "$P(A) = \\dfrac{n(\\Omega)}{n(A)}$", "$P(A) = n(A) \\cdot n(\\Omega)$", "$P(A) = n(\\Omega) - n(A)$"], 0, "Theo định nghĩa xác suất cổ điển: **$P(A) = \\dfrac{n(A)}{n(\\Omega)}$**."),
            mcq("biet", "Một hộp có $10$ tấm thẻ cùng loại được đánh số từ $1$ đến $10$. Rút ngẫu nhiên một tấm thẻ. Số kết quả thuận lợi cho biến cố “Số ghi trên thẻ là số nguyên tố” là:", ["$4$", "$5$", "$3$", "$6$"], 0, "Các số nguyên tố từ $1$ đến $10$ là $2, 3, 5, 7$ $\\Rightarrow$ có **$4$** kết quả thuận lợi."),
            mcq("hieu", "Tung một đồng xu cân đối hai lần liên tiếp. Xác suất của biến cố “Có đúng một lần xuất hiện mặt ngửa” là:", ["$\\dfrac{1}{2}$", "$\\dfrac{1}{4}$", "$\\dfrac{3}{4}$", "$\\dfrac{1}{3}$"], 0, "Không gian mẫu có $4$ phần tử; kết quả thuận lợi là $\\{\\text{SN}; \\text{NS}\\}$ ($2$ phần tử). Xác suất là $\\dfrac{2}{4} =$ **$\\dfrac{1}{2}$**."),
            mcq("hieu", "Một hộp có $3$ quả bóng xanh và $2$ quả bóng đỏ có cùng kích thước và khối lượng. Lấy ngẫu nhiên đồng thời $2$ quả bóng từ hộp. Số phần tử của không gian mẫu là:", ["$10$", "$20$", "$5$", "$6$"], 0, "Đánh số $5$ quả bóng từ $1$ đến $5$. Số cách lấy ra $2$ quả bóng không phân biệt thứ tự từ $5$ quả là $\\dfrac{5 \\cdot 4}{2} =$ **$10$**."),
            tf4("hieu", "Một hộp chứa $12$ tấm thẻ cùng loại được đánh số từ $1$ đến $12$. Rút ngẫu nhiên một tấm thẻ trong hộp. Mỗi khẳng định sau đúng hay sai?", ["a) Số phần tử của không gian mẫu là $n(\\Omega) = 12$", "b) Biến cố $A$: “Số ghi trên thẻ chia hết cho $3$” có $4$ kết quả thuận lợi", "c) Xác suất của biến cố $A$ là $P(A) = \\dfrac{1}{4}$", "d) Xác suất của biến cố $B$: “Số ghi trên thẻ là số chính phương” là $\\dfrac{1}{4}$"], [True, True, False, True], "a) Có $12$ thẻ từ $1$ đến $12$ $\\rightarrow$ Đúng.\
b) Các số chia hết cho $3$ là $\\{3; 6; 9; 12\\}$ gồm $4$ kết quả $\\rightarrow$ Đúng.\
c) $P(A) = \\dfrac{4}{12} = \\dfrac{1}{3} \\ne \\dfrac{1}{4}$ $\\rightarrow$ Sai.\
d) Các số chính phương là $\\{1; 4; 9\\}$ ($3$ kết quả) $\\Rightarrow P(B) = \\dfrac{3}{12} = \\dfrac{1}{4}$ $\\rightarrow$ Đúng."),
            tf4("hieu", "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Mỗi khẳng định sau đúng hay sai?", ["a) Không gian mẫu có $36$ phần tử đồng khả năng", "b) Biến cố $E$: “Hai con xúc xắc xuất hiện cùng số chấm” có $6$ kết quả thuận lợi", "c) Biến cố $F$: “Tổng số chấm trên hai con xúc xắc bằng $10$” có $4$ kết quả thuận lợi", "d) Xác suất của biến cố $E$ bằng $\\dfrac{1}{6}$"], [True, True, False, True], "a) $6 \\cdot 6 = 36$ kết quả đồng khả năng $\\rightarrow$ Đúng.\
b) $E = \\{(1; 1), (2; 2), (3; 3), (4; 4), (5; 5), (6; 6)\\}$ có $6$ phần tử $\\rightarrow$ Đúng.\
c) Tổng bằng $10$ chỉ gồm $(4; 6), (5; 5), (6; 4)$ có $3$ kết quả $\\rightarrow$ Sai.\
d) $P(E) = \\dfrac{6}{36} = \\dfrac{1}{6}$ $\\rightarrow$ Đúng."),
            mcq("vandung", "Bạn An và bạn Bình mỗi người chọn ngẫu nhiên một số tự nhiên từ tập hợp $\\{1; 2; 3; 4\\}$. Xác suất để tổng hai số mà hai bạn chọn là một số chẵn bằng:", ["$\\dfrac{1}{2}$", "$\\dfrac{1}{4}$", "$\\dfrac{3}{8}$", "$\\dfrac{5}{8}$"], 0, "Không gian mẫu có $4 \\cdot 4 = 16$ cặp $(a; b)$. Tổng $a + b$ chẵn khi cả hai cùng chẵn ($2 \\cdot 2 = 4$ cặp) hoặc cả hai cùng lẻ ($2 \\cdot 2 = 4$ cặp), tổng cộng $8$ cặp. Xác suất là $\\dfrac{8}{16} =$ **$\\dfrac{1}{2}$**."),
            short("vandung", "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Có bao nhiêu kết quả thuận lợi cho biến cố “Tổng số chấm xuất hiện trên hai con xúc xắc nhỏ hơn hoặc bằng $4$”?", ["6"], "Các cặp $(i; j)$ có $i + j \\le 4$ là: tổng bằng $2$ có $(1; 1)$; tổng bằng $3$ có $(1; 2), (2; 1)$; tổng bằng $4$ có $(1; 3), (2; 2), (3; 1)$. Tổng cộng có $1 + 2 + 3 =$ **$6$** kết quả thuận lợi."),
        ],
    },
    {
        "topic": "l9-ch09-duong-tron-ngoai-tiep-va-duong-tron-noi-tiep",
        "title": "Đường tròn ngoại tiếp và đường tròn nội tiếp",
        "icon": "🔯",
        "description": "Chương IX · SGK Toán 9 tập hai: Bài 27 – Bài 30. Góc nội tiếp; đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác; tứ giác nội tiếp; đa giác đều và phép quay.",
        "requirements": [
            "Nhận biết được góc nội tiếp và giải thích được mối liên hệ giữa số đo của góc nội tiếp với số đo của góc ở tâm cùng chắn một cung.",
            "Xác định được tâm và bán kính đường tròn ngoại tiếp tam giác, trong đó có tâm và bán kính đường tròn ngoại tiếp tam giác vuông, tam giác đều; xác định được tâm và bán kính đường tròn nội tiếp tam giác, trong đó có tam giác đều.",
            "Nhận biết được tứ giác nội tiếp đường tròn và giải thích được định lí về tổng hai góc đối của tứ giác nội tiếp bằng $180^\\circ$.",
            "Nhận dạng được đa giác đều; nhận biết được phép quay và mô tả được các phép quay giữ nguyên một đa giác đều.",
        ],
        "definition": (
            "- **Góc nội tiếp** là góc có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây cung của đường tròn đó. Trong một đường tròn, số đo góc nội tiếp bằng **nửa số đo cung bị chắn** (và bằng nửa số đo góc ở tâm cùng chắn một cung); góc nội tiếp chắn nửa đường tròn là **góc vuông** ($90^\\circ$).\n"
            "- **Đường tròn ngoại tiếp tam giác** đi qua ba đỉnh của tam giác (tâm là giao điểm ba đường trung trực). **Đường tròn nội tiếp tam giác** tiếp xúc với ba cạnh của tam giác (tâm là giao điểm ba đường phân giác trong).\n"
            "- **Tứ giác nội tiếp** có bốn đỉnh cùng thuộc một đường tròn; một tứ giác nội tiếp khi và chỉ khi tổng hai góc đối diện bằng $180^\\circ$.\n"
            "- **Đa giác đều** là đa giác có tất cả các cạnh bằng nhau và tất cả các góc bằng nhau."
        ),
        "theory": (
            "### Bài 27. Góc nội tiếp\n"
            "- Các góc nội tiếp bằng nhau chắn các cung bằng nhau; các góc nội tiếp cùng chắn một cung (hoặc chắn các cung bằng nhau) thì bằng nhau.\n"
            "- Góc nội tiếp (nhỏ hơn hoặc bằng $90^\\circ$) có số đo bằng nửa số đo góc ở tâm cùng chắn một cung; góc nội tiếp chắn nửa đường tròn bằng $90^\\circ$.\n"
            "### Bài 28. Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác\n"
            "- Tam giác vuông có tâm đường tròn ngoại tiếp là **trung điểm cạnh huyền** và bán kính $R = \\dfrac{\\text{cạnh huyền}}{2}$.\n"
            "- Tam giác đều cạnh $a$ có tâm đường tròn ngoại tiếp và nội tiếp trùng với trọng tâm $G$, với $R = \\dfrac{a\\sqrt{3}}{3}$ và $r = \\dfrac{a\\sqrt{3}}{6}$.\n"
            "### Luyện tập chung\n"
            "### Bài 29. Tứ giác nội tiếp\n"
            "- Trong một tứ giác nội tiếp, tổng số đo hai góc đối bằng $180^\\circ$: $\\widehat{A} + \\widehat{C} = 180^\\circ$ và $\\widehat{B} + \\widehat{D} = 180^\\circ$.\n"
            "- Hình chữ nhật, hình vuông, hình thang cân luôn nội tiếp được đường tròn.\n"
            "### Bài 30. Đa giác đều\n"
            "- Mỗi góc trong của $n$-giác đều bằng $\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$.\n"
            "- **Phép quay** thuận chiều (hoặc ngược chiều) tâm $O$ góc $\\alpha^\\circ$ giữ nguyên $n$-giác đều tâm $O$ khi $\\alpha^\\circ$ là bội của $\\dfrac{360^\\circ}{n}$.\n"
            "### Luyện tập chung · Bài tập cuối chương IX"
        ),
        "formulas": [
            G("I. Góc nội tiếp và tứ giác nội tiếp", F("Số đo góc nội tiếp", "$\\widehat{AMB} = \\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = \\dfrac{1}{2}\\widehat{AOB}$"), F("Góc nội tiếp chắn nửa đường tròn", "$\\widehat{AMB} = 90^\\circ$ (khi $AB$ là đường kính)"), F("Tứ giác $ABCD$ nội tiếp", "$\\widehat{A} + \\widehat{C} = 180^\\circ \\cdot \\widehat{B} + \\widehat{D} = 180^\\circ$")),
            G("II. Bán kính đường tròn ngoại tiếp ($R$) và nội tiếp ($r$)", F("Tam giác vuông (cạnh huyền $a$)", "$R = \\dfrac{a}{2}$ (tâm là trung điểm cạnh huyền)"), F("Tam giác đều cạnh $a$", "$R = \\dfrac{a\\sqrt{3}}{3} \\cdot r = \\dfrac{a\\sqrt{3}}{6} \\quad (R = 2r)$"), F("Hình chữ nhật kích thước $a, b$", "$R = \\dfrac{\\sqrt{a^2 + b^2}}{2}$ (tâm là giao điểm hai đường chéo)")),
            G("III. Đa giác đều $n$ cạnh", F("Số đo mỗi góc của $n$-giác đều", "$\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$"), F("Góc quay nhỏ nhất giữ nguyên $n$-giác đều", "$\\alpha_{\\min} = \\dfrac{360^\\circ}{n}$")),
        ],
        "example": "Cho tam giác đều $ABC$ có cạnh $a = 6\\text{ cm}$. Tính bán kính đường tròn ngoại tiếp $R$ và bán kính đường tròn nội tiếp $r$ của tam giác $ABC$.",
        "example_answer": (
            "Bán kính đường tròn ngoại tiếp: $R = \\dfrac{a\\sqrt{3}}{3} = \\dfrac{6\\sqrt{3}}{3} =$ **$2\\sqrt{3}\\text{ cm}$**.\n"
            "Bán kính đường tròn nội tiếp: $r = \\dfrac{a\\sqrt{3}}{6} = \\dfrac{6\\sqrt{3}}{6} =$ **$\\sqrt{3}\\text{ cm}$**."
        ),
        "real_life": (
            "- Thiết kế hoa văn hình đa giác đều, bánh răng cơ khí, cánh quạt đối xứng quay.\n"
            "- Xác định vị trí đặt trạm phát sóng cách đều ba điểm dân cư (tâm đường tròn ngoại tiếp tam giác)."
        ),
        "quiz": [
            mcq("biet", "Trong một đường tròn, góc nội tiếp chắn cung có số đo $80^\\circ$ thì có số đo bằng:", ["$40^\\circ$", "$80^\\circ$", "$160^\\circ$", "$20^\\circ$"], 0, "Số đo góc nội tiếp bằng nửa số đo cung bị chắn: $\\dfrac{80^\\circ}{2} =$ **$40^\\circ$**."),
            mcq("biet", "Tâm đường tròn ngoại tiếp tam giác vuông là:", ["Trung điểm của cạnh huyền", "Đỉnh góc vuông", "Trọng tâm của tam giác", "Giao điểm ba đường phân giác"], 0, "Tâm đường tròn ngoại tiếp tam giác vuông là **trung điểm của cạnh huyền**."),
            mcq("biet", "Cho tứ giác $ABCD$ nội tiếp đường tròn, biết $\\widehat{A} = 70^\\circ$. Số đo $\\widehat{C}$ bằng:", ["$110^\\circ$", "$70^\\circ$", "$20^\\circ$", "$140^\\circ$"], 0, "Trong tứ giác nội tiếp, hai góc đối bù nhau: $\\widehat{C} = 180^\\circ - \\widehat{A} = 180^\\circ - 70^\\circ =$ **$110^\\circ$**."),
            mcq("biet", "Góc quay nhỏ nhất (khác $0^\\circ$) quanh tâm $O$ biến một lục giác đều tâm $O$ thành chính nó có số đo là:", ["$60^\\circ$", "$45^\\circ$", "$90^\\circ$", "$120^\\circ$"], 0, "Lục giác đều có $n = 6$ cạnh nên góc quay nhỏ nhất là $\\dfrac{360^\\circ}{6} =$ **$60^\\circ$**."),
            mcq("hieu", "Cho $\\triangle ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Bán kính đường tròn ngoại tiếp $\\triangle ABC$ bằng:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$4\\text{ cm}$", "$3\\text{ cm}$"], 0, "Cạnh huyền $BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Bán kính đường tròn ngoại tiếp là $R = \\dfrac{BC}{2} =$ **$5\\text{ cm}$**."),
            mcq("hieu", "Cho tam giác đều $ABC$ có cạnh bằng $6\\sqrt{3}\\text{ cm}$. Bán kính đường tròn ngoại tiếp tam giác $ABC$ bằng:", ["$6\\text{ cm}$", "$3\\text{ cm}$", "$3\\sqrt{3}\\text{ cm}$", "$9\\text{ cm}$"], 0, "Áp dụng công thức $R = \\dfrac{a\\sqrt{3}}{3} = \\dfrac{6\\sqrt{3} \\cdot \\sqrt{3}}{3} =$ **$6\\text{ cm}$**."),
            tf4("hieu", "Cho đường tròn $(O)$ và hai điểm $A, B$ trên $(O)$ sao cho góc ở tâm $\\widehat{AOB} = 100^\\circ$. Lấy điểm $M$ thuộc cung lớn $AB$ và điểm $N$ thuộc cung nhỏ $AB$ (khác $A, B$). Mỗi khẳng định sau đúng hay sai?", ["a) Số đo cung nhỏ $AB$ bằng $100^\\circ$", "b) Góc nội tiếp $\\widehat{AMB}$ có số đo bằng $50^\\circ$", "c) Tứ giác $AMBN$ là tứ giác nội tiếp đường tròn $(O)$", "d) Góc $\\widehat{ANB}$ có số đo bằng $100^\\circ$"], [True, True, True, False], "a) Số đo cung nhỏ bằng số đo góc ở tâm $\\widehat{AOB} = 100^\\circ$ $\\rightarrow$ Đúng.\
b) $\\widehat{AMB} = \\dfrac{1}{2}\\widehat{AOB} = 50^\\circ$ $\\rightarrow$ Đúng.\
c) Bốn đỉnh $A, M, B, N$ cùng thuộc đường tròn $(O)$ $\\rightarrow$ Đúng.\
d) Trong tứ giác nội tiếp $AMBN$: $\\widehat{ANB} = 180^\\circ - \\widehat{AMB} = 130^\\circ \\ne 100^\\circ$ $\\rightarrow$ Sai."),
            tf4("hieu", "Cho $\\triangle ABC$ nhọn nội tiếp đường tròn $(O)$, hai đường cao $BD$ và $CE$ cắt nhau tại trực tâm $H$. Mỗi khẳng định sau đúng hay sai?", ["a) $\\widehat{BDC} = \\widehat{BEC} = 90^\\circ$", "b) Tứ giác $BCDE$ nội tiếp đường tròn đường kính $BC$", "c) Tứ giác $ADHE$ nội tiếp đường tròn đường kính $AH$", "d) $\\widehat{BHC} = \\widehat{BAC}$"], [True, True, True, False], "a) $BD \\perp AC, CE \\perp AB$ nên $\\widehat{BDC} = \\widehat{BEC} = 90^\\circ$ $\\rightarrow$ Đúng.\
b) $D, E$ cùng nhìn $BC$ dưới góc $90^\\circ$ nên $B, C, D, E$ thuộc đường tròn đường kính $BC$ $\\rightarrow$ Đúng.\
c) $\\widehat{ADH} + \\widehat{AEH} = 90^\\circ + 90^\\circ = 180^\\circ$ nên $ADHE$ nội tiếp đường tròn đường kính $AH$ $\\rightarrow$ Đúng.\
d) Trong tứ giác nội tiếp $ADHE$: $\\widehat{DHE} = 180^\\circ - \\widehat{BAC}$, mà $\\widehat{BHC} = \\widehat{DHE}$ (đối đỉnh) nên $\\widehat{BHC} = 180^\\circ - \\widehat{BAC}$ $\\rightarrow$ Sai."),
            mcq("vandung", "Một khung cửa sổ hình chữ nhật có chiều rộng $60\\text{ cm}$ và chiều cao $80\\text{ cm}$ được lắp vừa khít vào một ô tường hình tròn (bốn đỉnh khung cửa nằm trên đường tròn). Đường kính của ô tường hình tròn đó là:", ["$100\\text{ cm}$", "$140\\text{ cm}$", "$50\\text{ cm}$", "$120\\text{ cm}$"], 0, "Đường kính đường tròn ngoại tiếp hình chữ nhật bằng độ dài đường chéo của hình chữ nhật: $d = \\sqrt{60^2 + 80^2} =$ **$100\\text{ cm}$**."),
            short("vandung", "Mỗi góc trong của một ngũ giác đều có số đo bằng bao nhiêu độ?", ["108", "108°"], "Áp dụng công thức góc trong của $n$-giác đều với $n = 5$: $\\dfrac{(5 - 2) \\cdot 180^\\circ}{5} =$ **$108^\\circ$**.", unit="°"),
        ],
    },
    {
        "topic": "l9-ch10-mot-so-hinh-khoi-trong-thuc-tien",
        "title": "Một số hình khối trong thực tiễn",
        "icon": "🌐",
        "description": "Chương X · SGK Toán 9 tập hai: Bài 31 – Bài 32. Hình trụ và hình nón (các yếu tố, diện tích xung quanh, thể tích); hình cầu và mặt cầu (các yếu tố, diện tích mặt cầu, thể tích hình cầu).",
        "requirements": [
            "Mô tả được (đường sinh, chiều cao, bán kính đáy) và tạo lập được hình trụ.",
            "Mô tả được (đỉnh, đường sinh, chiều cao, bán kính đáy) và tạo lập được hình nón.",
            "Mô tả được (tâm, bán kính) và tạo lập được hình cầu, mặt cầu; nhận biết được phần chung của mặt phẳng và hình cầu.",
            "Tính được diện tích xung quanh của hình trụ, hình nón, diện tích mặt cầu; tính được thể tích của hình trụ, hình nón, hình cầu.",
            "Giải quyết được một số vấn đề thực tiễn gắn với việc tính diện tích xung quanh, thể tích của hình trụ, hình nón, hình cầu.",
        ],
        "definition": (
            "- **Hình trụ** có hai đáy là hai hình tròn bằng nhau và song song (bán kính $r$), chiều cao $h$ bằng độ dài đường sinh: $S_{\\text{xq}} = 2\\pi rh$, $V = \\pi r^2 h$.\n"
            "- **Hình nón** có đáy là hình tròn bán kính $r$, chiều cao $h$, đường sinh $l = \\sqrt{r^2 + h^2}$: $S_{\\text{xq}} = \\pi rl$, $V = \\dfrac{1}{3}\\pi r^2 h$.\n"
            "- **Hình cầu** tâm $O$ bán kính $R$: diện tích mặt cầu $S = 4\\pi R^2$, thể tích hình cầu $V = \\dfrac{4}{3}\\pi R^3$. Khi cắt hình cầu bởi một mặt phẳng thì phần chung luôn là một **hình tròn**."
        ),
        "theory": (
            "### Bài 31. Hình trụ và hình nón\n"
            "- **Hình trụ**: Quay hình chữ nhật quanh một cạnh cố định tạo thành hình trụ. Diện tích xung quanh $S_{\\text{xq}} = 2\\pi rh$; diện tích toàn phần $S_{\\text{tp}} = 2\\pi rh + 2\\pi r^2$; thể tích $V = \\pi r^2 h$.\n"
            "- **Hình nón**: Quay tam giác vuông quanh một cạnh góc vuông cố định tạo thành hình nón. Đường sinh $l$, chiều cao $h$ và bán kính đáy $r$ liên hệ bởi $l^2 = r^2 + h^2$. Diện tích xung quanh $S_{\\text{xq}} = \\pi rl$; diện tích toàn phần $S_{\\text{tp}} = \\pi rl + \\pi r^2$; thể tích $V = \\dfrac{1}{3}\\pi r^2 h$.\n"
            "### Bài 32. Hình cầu\n"
            "- Quay nửa hình tròn tâm $O$ bán kính $R$ một vòng quanh đường kính cố định được một **hình cầu**.\n"
            "- Giao của mặt phẳng với hình cầu là một hình tròn (nếu mặt phẳng đi qua tâm thì được **hình tròn lớn** có bán kính $R$).\n"
            "- Diện tích mặt cầu: $S = 4\\pi R^2$; thể tích hình cầu: $V = \\dfrac{4}{3}\\pi R^3$.\n"
            "### Luyện tập chung · Bài tập cuối chương X"
        ),
        "formulas": [
            G("I. Hình trụ (bán kính đáy $r$, chiều cao $h$)", F("Diện tích xung quanh và toàn phần", "$S_{\\text{xq}} = 2\\pi rh \\cdot S_{\\text{tp}} = 2\\pi rh + 2\\pi r^2$"), F("Thể tích hình trụ", "$V = \\pi r^2 h$")),
            G("II. Hình nón (bán kính đáy $r$, chiều cao $h$, đường sinh $l$)", F("Hệ thức liên hệ", "$l = \\sqrt{r^2 + h^2}$"), F("Diện tích xung quanh và toàn phần", "$S_{\\text{xq}} = \\pi rl \\cdot S_{\\text{tp}} = \\pi rl + \\pi r^2$"), F("Thể tích hình nón", "$V = \\dfrac{1}{3}\\pi r^2 h$")),
            G("III. Hình cầu (bán kính $R$)", F("Diện tích mặt cầu", "$S = 4\\pi R^2$"), F("Thể tích hình cầu", "$V = \\dfrac{4}{3}\\pi R^3$")),
        ],
        "example": "Một hình nón có bán kính đáy $r = 3\\text{ cm}$ và chiều cao $h = 4\\text{ cm}$. Tính độ dài đường sinh, diện tích xung quanh và thể tích của hình nón (theo $\\pi$).",
        "example_answer": (
            "Độ dài đường sinh: $l = \\sqrt{r^2 + h^2} = \\sqrt{3^2 + 4^2} =$ **$5\\text{ cm}$**.\n"
            "Diện tích xung quanh: $S_{\\text{xq}} = \\pi rl = \\pi \\cdot 3 \\cdot 5 =$ **$15\\pi\\text{ cm}^2$**.\n"
            "Thể tích hình nón: $V = \\dfrac{1}{3}\\pi r^2 h = \\dfrac{1}{3}\\pi \\cdot 3^2 \\cdot 4 =$ **$12\\pi\\text{ cm}^3$**."
        ),
        "real_life": (
            "- Tính dung tích lon nước ngọt, bồn chứa nước inox (hình trụ).\n"
            "- Tính diện tích lá làm nón lá, phễu đong (hình nón); tính diện tích da khâu quả bóng đá, thể tích bồn chứa khí hoá lỏng (hình cầu)."
        ),
        "quiz": [
            mcq("biet", "Công thức tính diện tích xung quanh của hình trụ có bán kính đáy $r$ và chiều cao $h$ là:", ["$S_{\\text{xq}} = 2\\pi rh$", "$S_{\\text{xq}} = \\pi rh$", "$S_{\\text{xq}} = \\pi r^2 h$", "$S_{\\text{xq}} = 2\\pi r^2 h$"], 0, "Diện tích xung quanh của hình trụ bằng chu vi đáy nhân chiều cao: **$S_{\\text{xq}} = 2\\pi rh$**."),
            mcq("biet", "Công thức tính thể tích của hình nón có bán kính đáy $r$ và chiều cao $h$ là:", ["$V = \\dfrac{1}{3}\\pi r^2 h$", "$V = \\pi r^2 h$", "$V = \\dfrac{4}{3}\\pi r^2 h$", "$V = \\dfrac{1}{2}\\pi r^2 h$"], 0, "Thể tích hình nón bằng một phần ba diện tích đáy nhân chiều cao: **$V = \\dfrac{1}{3}\\pi r^2 h$**."),
            mcq("biet", "Mặt cầu có bán kính $R$ thì có diện tích bằng:", ["$S = 4\\pi R^2$", "$S = \\pi R^2$", "$S = 2\\pi R^2$", "$S = \\dfrac{4}{3}\\pi R^3$"], 0, "Diện tích mặt cầu bán kính $R$ là **$S = 4\\pi R^2$**."),
            mcq("biet", "Khi cắt một hình cầu bởi một mặt phẳng thì phần chung của mặt phẳng và hình cầu luôn là một:", ["Hình tròn", "Hình vuông", "Hình elip", "Hình tam giác"], 0, "Mặt phẳng cắt hình cầu luôn tạo ra phần chung là một **hình tròn**."),
            mcq("hieu", "Một hình trụ có bán kính đáy $r = 4\\text{ cm}$ và chiều cao $h = 5\\text{ cm}$. Thể tích của hình trụ đó bằng:", ["$80\\pi\\text{ cm}^3$", "$40\\pi\\text{ cm}^3$", "$20\\pi\\text{ cm}^3$", "$100\\pi\\text{ cm}^3$"], 0, "Áp dụng công thức $V = \\pi r^2 h = \\pi \\cdot 4^2 \\cdot 5 =$ **$80\\pi\\text{ cm}^3$**."),
            mcq("hieu", "Một hình nón có bán kính đáy $r = 6\\text{ cm}$ và chiều cao $h = 8\\text{ cm}$. Diện tích xung quanh của hình nón đó bằng:", ["$60\\pi\\text{ cm}^2$", "$48\\pi\\text{ cm}^2$", "$96\\pi\\text{ cm}^2$", "$120\\pi\\text{ cm}^2$"], 0, "Đường sinh $l = \\sqrt{r^2 + h^2} = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Diện tích xung quanh là $S_{\\text{xq}} = \\pi rl = \\pi \\cdot 6 \\cdot 10 =$ **$60\\pi\\text{ cm}^2$**."),
            tf4("hieu", "Cho một hình nón có bán kính đáy $r = 3\\text{ cm}$ và chiều cao $h = 4\\text{ cm}$. Mỗi khẳng định sau đúng hay sai?", ["a) Độ dài đường sinh của hình nón là $l = 5\\text{ cm}$", "b) Diện tích xung quanh của hình nón là $15\\pi\\text{ cm}^2$", "c) Diện tích toàn phần của hình nón là $24\\pi\\text{ cm}^2$", "d) Thể tích của hình nón là $36\\pi\\text{ cm}^3$"], [True, True, True, False], "a) $l = \\sqrt{3^2 + 4^2} = 5\\text{ cm}$ $\\rightarrow$ Đúng.\
b) $S_{\\text{xq}} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi\\text{ cm}^2$ $\\rightarrow$ Đúng.\
c) $S_{\\text{tp}} = S_{\\text{xq}} + \\pi r^2 = 15\\pi + 9\\pi = 24\\pi\\text{ cm}^2$ $\\rightarrow$ Đúng.\
d) $V = \\dfrac{1}{3}\\pi r^2 h = \\dfrac{1}{3}\\pi \\cdot 9 \\cdot 4 = 12\\pi\\text{ cm}^3 \\ne 36\\pi\\text{ cm}^3$ $\\rightarrow$ Sai."),
            tf4("hieu", "Cho một hình cầu có đường kính $d = 6\\text{ cm}$. Mỗi khẳng định sau đúng hay sai?", ["a) Bán kính của hình cầu là $R = 3\\text{ cm}$", "b) Đường tròn lớn của hình cầu có chu vi bằng $6\\pi\\text{ cm}$", "c) Diện tích mặt cầu bằng $36\\pi\\text{ cm}^2$", "d) Thể tích của hình cầu bằng $108\\pi\\text{ cm}^3$"], [True, True, True, False], "a) $R = \\dfrac{d}{2} = 3\\text{ cm}$ $\\rightarrow$ Đúng.\
b) Chu vi đường tròn lớn: $C = 2\\pi R = 6\\pi\\text{ cm}$ $\\rightarrow$ Đúng.\
c) $S = 4\\pi R^2 = 4\\pi \\cdot 3^2 = 36\\pi\\text{ cm}^2$ $\\rightarrow$ Đúng.\
d) $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot 27 = 36\\pi\\text{ cm}^3 \\ne 108\\pi\\text{ cm}^3$ $\\rightarrow$ Sai."),
            mcq("vandung", "Một lon sữa đặc hình trụ có đường kính đáy $8\\text{ cm}$ và chiều cao $10\\text{ cm}$. Diện tích giấy tối thiểu dùng để dán kín mặt xung quanh của lon sữa (bỏ qua mép dán) là:", ["$80\\pi\\text{ cm}^2$", "$160\\pi\\text{ cm}^2$", "$40\\pi\\text{ cm}^2$", "$112\\pi\\text{ cm}^2$"], 0, "Bán kính đáy của lon sữa là $r = \\dfrac{8}{2} = 4\\text{ cm}$. Diện tích xung quanh là $S_{\\text{xq}} = 2\\pi rh = 2\\pi \\cdot 4 \\cdot 10 =$ **$80\\pi\\text{ cm}^2$**."),
            short("vandung", "Một bồn chứa nước hình trụ có bán kính đáy $r = 1\\text{ m}$ và chiều cao $h = 3\\text{ m}$ đang chứa đầy nước. Người ta dùng một chiếc thùng hình nón có cùng bán kính đáy $r = 1\\text{ m}$ và cùng chiều cao $h = 3\\text{ m}$ để múc nước ra. Cần múc đầy bao nhiêu thùng hình nón thì hết nước trong bồn?", ["3"], "Vì hình trụ và hình nón có cùng bán kính đáy $r$ và cùng chiều cao $h$ nên $V_{\\text{trụ}} = \\pi r^2 h = 3 \\cdot \\left(\\dfrac{1}{3}\\pi r^2 h\\right) = 3V_{\\text{nón}}$. Vậy cần múc đúng **$3$** thùng."),
        ],
    },
]
