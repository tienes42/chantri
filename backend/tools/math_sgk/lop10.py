"""TOÁN 10 — Kết nối tri thức với cuộc sống (tập một, tập hai).

9 chương đánh số (I – IX) đúng thứ tự mục lục SGK (Bài 1 – Bài 27).
Mỗi chương: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 10

LESSONS = [
    {
        "topic": "l10-ch01-menh-de-va-tap-hop",
        "title": "Mệnh đề và tập hợp",
        "icon": "🧠",
        "description": "Chương I · SGK Toán 10 tập một: Bài 1 – Bài 2. Mệnh đề, mệnh đề chứa biến, mệnh đề phủ định, mệnh đề kéo theo, mệnh đề đảo, hai mệnh đề tương đương, kí hiệu với mọi và tồn tại; tập hợp, tập con, hai tập hợp bằng nhau, các tập con của tập số thực và các phép toán giao, hợp, hiệu, phần bù trên tập hợp.",
        "requirements": [
            "Thiết lập và phát biểu được các mệnh đề toán học, bao gồm: mệnh đề phủ định $\\overline{P}$; mệnh đề đảo; mệnh đề tương đương $P \\Leftrightarrow Q$; mệnh đề có chứa kí hiệu $\\forall, \\exists$; điều kiện cần, điều kiện đủ, điều kiện cần và đủ.",
            "Xác định được tính đúng, sai của một mệnh đề toán học trong những trường hợp đơn giản.",
            "Nhận biết được các khái niệm cơ bản về tập hợp (tập con $A \\subset B$, hai tập hợp bằng nhau $A = B$, tập rỗng $\\varnothing$) và biết sử dụng biểu đồ Ven để biểu diễn tập hợp.",
            "Thực hiện được các phép toán trên các tập hợp (hợp $A \\cup B$, giao $A \\cap B$, hiệu của hai tập hợp $A \\setminus B$, phần bù của một tập con $C_E A$) và dùng biểu đồ Ven để biểu diễn chúng trong những trường hợp cụ thể.",
            "Giải quyết được một số bài toán thực tiễn liên quan đến đếm số phần tử của tập hợp và các phép toán trên tập hợp (ví dụ: những bài toán liên quan đến thu thập, phân loại dữ liệu khảo sát).",
        ],
        "definition": (
            "- **Mệnh đề** là một khẳng định hoặc đúng hoặc sai, không thể vừa đúng vừa sai. Khẳng định có tính đúng sai phụ thuộc vào biến gọi là **mệnh đề chứa biến** $P(x)$.\n"
            "- **Mệnh đề phủ định** của $P$ là $\\overline{P}$ (đúng khi $P$ sai, sai khi $P$ đúng). **Mệnh đề kéo theo** $P \\Rightarrow Q$ chỉ sai khi $P$ đúng và $Q$ sai. **Mệnh đề tương đương** $P \\Leftrightarrow Q$ đúng khi cả $P \\Rightarrow Q$ và $Q \\Rightarrow P$ cùng đúng.\n"
            "- **Tập hợp**: $x \\in A$ ($x$ thuộc $A$), $x \\notin A$ ($x$ không thuộc $A$). Tập $A$ là **tập con** của $B$ ($A \\subset B$) nếu $\\forall x, x \\in A \\Rightarrow x \\in B$.\n"
            "- **Các phép toán trên tập hợp**: Giao $A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$; Hợp $A \\cup B = \\{x \\mid x \\in A \\text{ hoặc } x \\in B\\}$; Hiệu $A \\setminus B = \\{x \\mid x \\in A \\text{ và } x \\notin B\\}$; Phần bù $C_E A = E \\setminus A$ (khi $A \\subset E$)."
        ),
        "theory": (
            "### Bài 1. Mệnh đề\n"
            "- **Mệnh đề và mệnh đề chứa biến**: Các câu khẳng định có tính đúng hoặc sai xác định là mệnh đề; câu hỏi, câu cảm thán, câu mệnh lệnh không phải là mệnh đề.\n"
            "- **Mệnh đề kéo theo và mệnh đề đảo**: Trong $P \\Rightarrow Q$, $P$ là giả thiết (điều kiện đủ để có $Q$) và $Q$ là kết luận (điều kiện cần để có $P$). Mệnh đề $Q \\Rightarrow P$ là mệnh đề đảo của $P \\Rightarrow Q$.\n"
            "- **Mệnh đề tương đương**: Khi $P \\Leftrightarrow Q$ đúng, ta nói $P$ là điều kiện cần và đủ để có $Q$.\n"
            "- **Kí hiệu $\\forall$ và $\\exists$**: Phủ định của mệnh đề $\\forall x \\in X, P(x)$ là $\\exists x \\in X, \\overline{P(x)}$; phủ định của $\\exists x \\in X, P(x)$ là $\\forall x \\in X, \\overline{P(x)}$.\n"
            "### Bài 2. Tập hợp và các phép toán trên tập hợp\n"
            "- **Tập hợp và tập con**: Tập hợp được cho bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng. Tập rỗng $\\varnothing$ là tập con của mọi tập hợp; tập hợp có $n$ phần tử thì có $2^n$ tập con.\n"
            "- **Các tập hợp số**: $\\mathbb{N}^* \\subset \\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$. Các tập con thường dùng của $\\mathbb{R}$: khoảng $(a; b)$, $(a; +\\infty)$, $(-\\infty; b)$; đoạn $[a; b]$; nửa khoảng $[a; b)$, $(a; b]$, $[a; +\\infty)$, $(-\\infty; b]$.\n"
            "- **Các phép toán giao, hợp, hiệu, phần bù**: Sử dụng trục số để tìm giao, hợp, hiệu của các khoảng và đoạn; sử dụng biểu đồ Ven và công thức $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$ cho hai tập hữu hạn.\n"
            "### Bài tập cuối chương I"
        ),
        "formulas": [
            G("I. Logic mệnh đề", F("Phủ định mệnh đề với mọi", "$\\overline{\\forall x \\in X, P(x)} \\iff \\exists x \\in X, \\overline{P(x)}$"), F("Phủ định mệnh đề tồn tại", "$\\overline{\\exists x \\in X, P(x)} \\iff \\forall x \\in X, \\overline{P(x)}$"), F("Mệnh đề tương đương", "$P \\Leftrightarrow Q \\iff (P \\Rightarrow Q) \\text{ và } (Q \\Rightarrow P)$")),
            G("II. Các tập con của tập số thực", F("Đoạn và khoảng", "$[a; b] = \\{x \\in \\mathbb{R} \\mid a \\le x \\le b\\}, \\quad (a; b) = \\{x \\in \\mathbb{R} \\mid a < x < b\\}$"), F("Nửa khoảng", "$[a; b) = \\{x \\in \\mathbb{R} \\mid a \\le x < b\\}, \\quad (a; b] = \\{x \\in \\mathbb{R} \\mid a < x \\le b\\}$")),
            G("III. Phép toán tập hợp & Công thức đếm", F("Giao và hợp", "$A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}, \\quad A \\cup B = \\{x \\mid x \\in A \\text{ hoặc } x \\in B\\}$"), F("Hiệu và phần bù", "$A \\setminus B = \\{x \\mid x \\in A \\text{ và } x \\notin B\\}, \\quad C_E A = E \\setminus A \\; (A \\subset E)$"), F("Số phần tử của hợp hai tập hữu hạn", "$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$"), F("Số tập con của tập n phần tử", "$N_{\\text{tập con}} = 2^n$")),
        ],
        "example": (
            "a) Phát biểu mệnh đề phủ định của mệnh đề $P: \\text{“}\\forall x \\in \\mathbb{R}, x^2 - 4x + 5 > 0\\text{”}$ và xét tính đúng sai của $P$.\n"
            "b) Cho hai tập hợp $A = [-2; 4)$ và $B = (1; 6]$. Tìm $A \\cap B$, $A \\cup B$, $A \\setminus B$ và $C_{\\mathbb{R}} A$."
        ),
        "example_answer": (
            "a) Mệnh đề phủ định là $\\overline{P}: \\text{“}\\exists x \\in \\mathbb{R}, x^2 - 4x + 5 \\le 0\\text{”}$.\n"
            "Vì $x^2 - 4x + 5 = (x - 2)^2 + 1 \\ge 1 > 0, \\forall x \\in \\mathbb{R}$ nên mệnh đề $P$ **đúng** và $\\overline{P}$ **sai**.\n"
            "b) Biểu diễn trên trục số:\n"
            "- $A \\cap B = (1; 4)$;\n"
            "- $A \\cup B = [-2; 6]$;\n"
            "- $A \\setminus B = [-2; 1]$;\n"
            "- $C_{\\mathbb{R}} A = \\mathbb{R} \\setminus [-2; 4) = (-\\infty; -2) \\cup [4; +\\infty)$."
        ),
        "real_life": (
            "- Mệnh đề logic là nền tảng của cấu trúc rẽ nhánh `if...else` và các biểu thức điều kiện trong lập trình máy tính, mạch điện tử số.\n"
            "- Phép toán tập hợp và biểu đồ Ven giúp thống kê số lượng học sinh tham gia các câu lạc bộ, phân loại khách hàng và truy vấn cơ sở dữ liệu."
        ),
        "quiz": [
            mcq("biet", "Trong các câu sau, câu nào là một mệnh đề?", ["Số $17$ là một số nguyên tố.", "Bạn có thích học môn Toán không?", "Hãy làm bài tập về nhà đầy đủ!", "Hôm nay trời đẹp quá!"], 0, "Câu khẳng định “Số $17$ là một số nguyên tố” có tính đúng sai xác định (là mệnh đề đúng), các câu còn lại là câu hỏi, câu cầu khiến, câu cảm thán nên không phải mệnh đề."),
            mcq("biet", "Mệnh đề phủ định của mệnh đề $P: \\text{“}\\forall x \\in \\mathbb{R}, x^2 + 1 > 0\\text{”}$ là:", ["$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0$", "$\\exists x \\in \\mathbb{R}, x^2 + 1 < 0$", "$\\forall x \\in \\mathbb{R}, x^2 + 1 \\le 0$", "$\\exists x \\in \\mathbb{R}, x^2 + 1 = 0$"], 0, "Phủ định của lượng từ $\\forall$ là $\\exists$, và phủ định của quan hệ $> 0$ là $\\le 0$. Vậy $\\overline{P}: \\text{“}\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0\\text{”}$."),
            mcq("biet", "Cho tập hợp $X = \\{a; b; c\\}$. Số tập con của tập hợp $X$ là:", ["$8$", "$6$", "$3$", "$9$"], 0, "Tập hợp $X$ có $n = 3$ phần tử nên số tập con của $X$ là $2^3 = 8$."),
            mcq("biet", "Tập hợp $M = \\{x \\in \\mathbb{R} \\mid -3 < x \\le 5\\}$ được viết dưới dạng khoảng, đoạn, nửa khoảng là:", ["$(-3; 5]$", "$[-3; 5)$", "$[-3; 5]$", "$(-3; 5)$"], 0, "Theo định nghĩa nửa khoảng, $\\{x \\in \\mathbb{R} \\mid -3 < x \\le 5\\} = (-3; 5]$."),
            mcq("hieu", "Cho hai tập hợp $A = [-1; 5)$ và $B = (2; 7]$. Tập hợp $A \\cap B$ là:", ["$(2; 5)$", "$[2; 5]$", "$[-1; 7]$", "$[-1; 2]$"], 0, "Lấy phần chung của $[-1; 5)$ và $(2; 7]$ trên trục số, ta được $A \\cap B = (2; 5)$."),
            mcq("hieu", "Tập hợp $A = \\{x \\in \\mathbb{Z} \\mid (x - 2)(2x^2 - 5x + 2) = 0\\}$ có bao nhiêu phần tử?", ["$1$", "$2$", "$3$", "$0$"], 0, "Giải phương trình: $x - 2 = 0 \\Leftrightarrow x = 2$; $2x^2 - 5x + 2 = 0 \\Leftrightarrow x = 2$ hoặc $x = \\dfrac{1}{2}$. Vì $x \\in \\mathbb{Z}$ và $\\dfrac{1}{2} \\notin \\mathbb{Z}$ nên $A = \\{2\\}$ có đúng $1$ phần tử."),
            tf4("hieu", "Cho hai mệnh đề $P: \\text{“Tam giác } ABC \\text{ là tam giác đều”}$ và $Q: \\text{“Tam giác } ABC \\text{ là tam giác cân”}$. Xét tính đúng sai của các khẳng định sau:", ["a) Mệnh đề kéo theo $P \\Rightarrow Q$ là một mệnh đề đúng.", "b) Mệnh đề đảo $Q \\Rightarrow P$ là một mệnh đề đúng.", "c) $P$ là điều kiện đủ để có $Q$.", "d) Hai mệnh đề $P$ và $Q$ là hai mệnh đề tương đương ($P \\Leftrightarrow Q$)."], [True, False, True, False], "a) Đúng vì mọi tam giác đều thì đều là tam giác cân.\nb) Sai vì một tam giác cân (ví dụ có góc ở đỉnh bằng $100^\\circ$) chưa chắc là tam giác đều.\nc) Đúng vì $P \\Rightarrow Q$ đúng nên $P$ là điều kiện đủ để có $Q$.\nd) Sai vì $Q \\Rightarrow P$ sai nên $P$ và $Q$ không tương đương."),
            tf4("hieu", "Cho hai tập hợp $A = (-\\infty; 3]$ và $B = (1; 6)$. Xét tính đúng sai của các khẳng định sau:", ["a) $A \\cap B = (1; 3]$.", "b) $A \\cup B = (-\\infty; 6)$.", "c) $B \\setminus A = [3; 6)$.", "d) Phần bù của $A$ trong $\\mathbb{R}$ là $C_{\\mathbb{R}} A = (3; +\\infty)$."], [True, True, False, True], "a) Đúng vì các số thực vừa thuộc $(-\\infty; 3]$ vừa thuộc $(1; 6)$ tạo thành nửa khoảng $(1; 3]$.\nb) Đúng vì hợp của $(-\\infty; 3]$ và $(1; 6)$ trên trục số là $(-\\infty; 6)$.\nc) Sai vì $3 \\in A$ nên $3 \\notin B \\setminus A$, do đó $B \\setminus A = (3; 6)$ chứ không phải $[3; 6)$.\nd) Đúng vì $C_{\\mathbb{R}} A = \\mathbb{R} \\setminus (-\\infty; 3] = (3; +\\infty)$."),
            mcq("vandung", "Lớp 10A có $42$ học sinh, trong đó có $25$ học sinh tham gia câu lạc bộ Tiếng Anh, $20$ học sinh tham gia câu lạc bộ Tin học và $10$ học sinh tham gia cả hai câu lạc bộ trên. Hỏi lớp 10A có bao nhiêu học sinh không tham gia câu lạc bộ nào trong hai câu lạc bộ đó?", ["$7$", "$5$", "$12$", "$15$"], 0, "Gọi $A, B$ lần lượt là tập hợp học sinh tham gia CLB Tiếng Anh và CLB Tin học. Số học sinh tham gia ít nhất một CLB là $n(A \\cup B) = n(A) + n(B) - n(A \\cap B) = 25 + 20 - 10 = 35$. Số học sinh không tham gia CLB nào là $42 - 35 = 7$ (học sinh)."),
            short("vandung", "Cho hai tập hợp $A = [-4; 3]$ và $B = (1; 5]$. Tập hợp $A \\setminus B$ có chứa bao nhiêu số nguyên?", ["6"], "Ta có $A \\setminus B = [-4; 3] \\setminus (1; 5] = [-4; 1]$. Các số nguyên thuộc $[-4; 1]$ là $\\{-4; -3; -2; -1; 0; 1\\}$, gồm $6$ số nguyên."),
        ],
    },
    {
        "topic": "l10-ch02-bat-phuong-trinh-va-he-bat-phuong-trinh-bac-nhat-hai-an",
        "title": "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
        "icon": "📐",
        "description": "Chương II · SGK Toán 10 tập một: Bài 3 – Bài 4. Bất phương trình bậc nhất hai ẩn, nghiệm và biểu diễn miền nghiệm của bất phương trình bậc nhất hai ẩn trên mặt phẳng toạ độ; hệ bất phương trình bậc nhất hai ẩn, miền nghiệm của hệ và ứng dụng tìm giá trị lớn nhất, giá trị nhỏ nhất của biểu thức bậc nhất trên một miền đa giác.",
        "requirements": [
            "Nhận biết được bất phương trình và hệ bất phương trình bậc nhất hai ẩn.",
            "Biểu diễn được miền nghiệm của bất phương trình và hệ bất phương trình bậc nhất hai ẩn trên mặt phẳng toạ độ $Oxy$.",
            "Vận dụng được kiến thức về bất phương trình, hệ bất phương trình bậc nhất hai ẩn vào giải quyết một số bài toán thực tiễn (ví dụ: bài toán quy hoạch tuyến tính hai biến tìm phương án tối ưu về chi phí, lợi nhuận).",
        ],
        "definition": (
            "- **Bất phương trình bậc nhất hai ẩn** $x, y$ có dạng tổng quát $ax + by < c$ (hoặc $ax + by > c, ax + by \\le c, ax + by \\ge c$), trong đó $a, b, c \\in \\mathbb{R}$ và $a, b$ không đồng thời bằng $0$ ($a^2 + b^2 > 0$).\n"
            "- Cặp số $(x_0; y_0)$ làm cho bất phương trình trở thành mệnh đề đúng gọi là một **nghiệm** của bất phương trình. Tập hợp các điểm $(x_0; y_0)$ trên mặt phẳng $Oxy$ là một nửa mặt phẳng bờ là đường thẳng $d: ax + by = c$, gọi là **miền nghiệm**.\n"
            "- **Hệ bất phương trình bậc nhất hai ẩn** gồm hai hay nhiều bất phương trình bậc nhất hai ẩn. Miền nghiệm của hệ là giao các miền nghiệm của từng bất phương trình trong hệ (thường là một miền đa giác lồi)."
        ),
        "theory": (
            "### Bài 3. Bất phương trình bậc nhất hai ẩn\n"
            "- **Cách xác định miền nghiệm của $ax + by < c$**:\n"
            "  + Bước 1: Trên mặt phẳng $Oxy$, vẽ đường thẳng bờ $d: ax + by = c$.\n"
            "  + Bước 2: Lấy một điểm $M_0(x_0; y_0)$ không thuộc $d$ (thường lấy gốc toạ độ $O(0; 0)$ nếu $c \\ne 0$) và tính $ax_0 + by_0$.\n"
            "  + Bước 3: Kết luận: Nếu $ax_0 + by_0 < c$ thì nửa mặt phẳng bờ $d$ chứa $M_0$ là miền nghiệm; ngược lại, nửa mặt phẳng bờ $d$ không chứa $M_0$ là miền nghiệm. Lưu ý: Với dấu $\\le, \\ge$ thì miền nghiệm kể cả bờ $d$; với dấu $<, >$ thì không kể bờ $d$.\n"
            "### Bài 4. Hệ bất phương trình bậc nhất hai ẩn\n"
            "- **Biểu diễn miền nghiệm của hệ**: Biểu diễn miền nghiệm của từng bất phương trình trong hệ trên cùng mặt phẳng toạ độ (gạch bỏ phần không thuộc miền nghiệm); phần mặt phẳng không bị gạch còn lại là miền nghiệm của hệ.\n"
            "- **Ứng dụng tối ưu (Quy hoạch tuyến tính)**: Giá trị lớn nhất và giá trị nhỏ nhất của biểu thức bậc nhất $F(x; y) = mx + ny$ trên một miền nghiệm là miền đa giác lồi luôn đạt được tại một trong các **đỉnh** của đa giác đó.\n"
            "### Bài tập cuối chương II"
        ),
        "formulas": [
            G("I. Bất phương trình bậc nhất hai ẩn", F("Dạng tổng quát", "$ax + by < c \\; (\\text{hoặc } >, \\le, \\ge), \\quad a^2 + b^2 > 0$"), F("Đường thẳng bờ", "$d: ax + by = c$"), F("Kiểm tra bằng gốc O(0; 0) (khi c khác 0)", "Thay $(0; 0)$ vào $ax + by < c \\Rightarrow 0 < c$: nếu đúng thì miền nghiệm chứa $O(0; 0)$")),
            G("II. Bài toán tối ưu trên miền đa giác", F("Hàm mục tiêu bậc nhất", "$F(x; y) = mx + ny$"), F("Định lí cực trị trên miền đa giác", "$\\max F(x; y)$ và $\\min F(x; y)$ trên miền đa giác $A_1 A_2 \\dots A_k$ đạt tại một trong các đỉnh $A_i$")),
        ],
        "example": (
            "Tìm giá trị lớn nhất và giá trị nhỏ nhất của biểu thức $F(x; y) = 3x + 2y$ trên miền nghiệm của hệ bất phương trình:\n"
            "$\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le 4 \\\\ 2x + y \\le 6 \\end{cases}$."
        ),
        "example_answer": (
            "Biểu diễn miền nghiệm của hệ trên mặt phẳng $Oxy$, ta được miền tứ giác lồi $OABC$ với toạ độ các đỉnh:\n"
            "- $O(0; 0)$;\n"
            "- $A(0; 4)$ (giao của $x = 0$ và $x + y = 4$);\n"
            "- $B(2; 2)$ (giao của $x + y = 4$ và $2x + y = 6$);\n"
            "- $C(3; 0)$ (giao của $y = 0$ và $2x + y = 6$).\n"
            "Tính giá trị của $F(x; y) = 3x + 2y$ tại các đỉnh:\n"
            "- $F(0; 0) = 0$; $F(0; 4) = 8$; $F(2; 2) = 3 \\cdot 2 + 2 \\cdot 2 = 10$; $F(3; 0) = 9$.\n"
            "Vậy $\\max F(x; y) = 10$ tại $(x; y) = (2; 2)$ và $\\min F(x; y) = 0$ tại $(x; y) = (0; 0)$."
        ),
        "real_life": (
            "- Lập kế hoạch sản xuất tối ưu trong doanh nghiệp nhằm cực đại hoá lợi nhuận hoặc cực tiểu hoá chi phí nguyên vật liệu, nhân công.\n"
            "- Thiết kế khẩu phần dinh dưỡng hằng ngày đảm bảo đủ lượng protein, vitamin với chi phí thấp nhất."
        ),
        "quiz": [
            mcq("biet", "Bất phương trình nào sau đây là bất phương trình bậc nhất hai ẩn $x, y$?", ["$2x - 5y + 3 > 0$", "$x^2 + 2y \\le 4$", "$3xy - y > 1$", "$0x + 0y \\ge -2$"], 0, "Bất phương trình bậc nhất hai ẩn có dạng $ax + by + c > 0$ với $a^2 + b^2 > 0$. Chỉ có $2x - 5y + 3 > 0$ thoả mãn."),
            mcq("biet", "Cặp số $(x; y)$ nào dưới đây là một nghiệm của bất phương trình $3x - 2y < 4$?", ["$(1; 1)$", "$(2; 1)$", "$(3; 2)$", "$(4; 0)$"], 0, "Thay $(1; 1)$ vào vế trái: $3 \\cdot 1 - 2 \\cdot 1 = 1 < 4$ (đúng). Các cặp còn lại lần lượt cho giá trị $4, 5, 12$ đều không nhỏ hơn $4$."),
            mcq("biet", "Miền nghiệm của bất phương trình $x + 2y - 6 \\le 0$ là nửa mặt phẳng bờ $d: x + 2y - 6 = 0$ (kể cả bờ $d$) có đặc điểm nào?", ["Chứa gốc toạ độ $O(0; 0)$", "Không chứa gốc toạ độ $O(0; 0)$", "Chỉ gồm các điểm có hoành độ dương", "Không chứa điểm $(1; 1)$"], 0, "Thay $O(0; 0)$ vào bất phương trình: $0 + 2 \\cdot 0 - 6 = -6 \\le 0$ (đúng), nên miền nghiệm chứa gốc toạ độ $O(0; 0)$."),
            mcq("biet", "Hệ nào dưới đây là một hệ bất phương trình bậc nhất hai ẩn?", ["$\\begin{cases} x + y \\le 5 \\\\ 2x - y > 1 \\end{cases}$", "$\\begin{cases} x^2 + y \\le 5 \\\\ x - y > 0 \\end{cases}$", "$\\begin{cases} x + y = 5 \\\\ 2x - y = 1 \\end{cases}$", "$\\begin{cases} xy \\ge 2 \\\\ x + y \\le 4 \\end{cases}$"], 0, "Hệ bất phương trình bậc nhất hai ẩn chỉ gồm các bất phương trình bậc nhất hai ẩn $x, y$, nên $\\begin{cases} x + y \\le 5 \\\\ 2x - y > 1 \\end{cases}$ là đáp án đúng."),
            mcq("hieu", "Điểm nào sau đây thuộc miền nghiệm của hệ bất phương trình $\\begin{cases} 2x + y - 4 \\le 0 \\\\ x - y + 1 > 0 \\end{cases}$?", ["$(1; 1)$", "$(2; 1)$", "$(0; 2)$", "$(1; 3)$"], 0, "Thay $(1; 1)$ vào hệ: $2(1) + 1 - 4 = -1 \\le 0$ (đúng) và $1 - 1 + 1 = 1 > 0$ (đúng). Vậy $(1; 1)$ thuộc miền nghiệm của hệ."),
            mcq("hieu", "Cho biểu thức $F(x; y) = 4x - y$ trên miền tam giác $OAB$ với các đỉnh $O(0; 0)$, $A(0; 3)$, $B(2; 1)$. Giá trị lớn nhất của $F(x; y)$ trên miền tam giác $OAB$ bằng:", ["$7$", "$8$", "$0$", "$-3$"], 0, "Tính giá trị của $F$ tại ba đỉnh: $F(0; 0) = 0$, $F(0; 3) = -3$, $F(2; 1) = 4 \\cdot 2 - 1 = 7$. Vậy giá trị lớn nhất của $F(x; y)$ bằng $7$."),
            tf4("hieu", "Cho bất phương trình bậc nhất hai ẩn $2x + 3y - 6 \\ge 0$. Xét tính đúng sai của các khẳng định sau:", ["a) Đường thẳng bờ của miền nghiệm là $d: 2x + 3y - 6 = 0$ đi qua hai điểm $(3; 0)$ và $(0; 2)$.", "b) Gốc toạ độ $O(0; 0)$ thuộc miền nghiệm của bất phương trình đã cho.", "c) Điểm $M(2; 2)$ thuộc miền nghiệm của bất phương trình đã cho.", "d) Miền nghiệm của bất phương trình bao gồm cả các điểm nằm trên đường thẳng $d$."], [True, False, True, True], "a) Đúng vì thay $(3; 0)$ và $(0; 2)$ vào $2x + 3y - 6 = 0$ đều thoả mãn.\nb) Sai vì thay $O(0; 0)$ được $-6 \\ge 0$ (vô lí).\nc) Đúng vì $2 \\cdot 2 + 3 \\cdot 2 - 6 = 4 \\ge 0$.\nd) Đúng vì bất phương trình có dấu $\\ge$ nên miền nghiệm tính cả đường thẳng bờ $d$."),
            tf4("hieu", "Cho hệ bất phương trình $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + 2y \\le 6 \\end{cases}$. Xét tính đúng sai của các khẳng định sau:", ["a) Miền nghiệm của hệ là miền tam giác $OAB$ (kể cả biên) với $O(0; 0), A(6; 0), B(0; 3)$.", "b) Diện tích của miền đa giác biểu diễn miền nghiệm của hệ bằng $18$.", "c) Điểm $I(2; 1)$ nằm trong miền nghiệm của hệ.", "d) Giá trị lớn nhất của biểu thức $P(x; y) = 2x + 5y$ trên miền nghiệm của hệ bằng $15$."], [True, False, True, True], "a) Đúng vì các đường thẳng $x = 0, y = 0, x + 2y = 6$ cắt nhau tạo thành tam giác vuông $OAB$ tại $O$ với $A(6; 0), B(0; 3)$.\nb) Sai vì diện tích tam giác vuông $OAB$ là $S = \\dfrac{1}{2} \\cdot OA \\cdot OB = \\dfrac{1}{2} \\cdot 6 \\cdot 3 = 9 \\ne 18$.\nc) Đúng vì $2 \\ge 0, 1 \\ge 0$ và $2 + 2 \\cdot 1 = 4 \\le 6$.\nd) Đúng vì $P(0; 0) = 0, P(6; 0) = 12, P(0; 3) = 15$ nên $\\max P = 15$."),
            mcq("vandung", "Một xưởng cơ khí có hai máy dùng để sản xuất hai loại sản phẩm I và II. Để sản xuất $1$ tấn sản phẩm I cần dùng máy thứ nhất $3$ giờ và máy thứ hai $1$ giờ, thu lãi $4$ triệu đồng. Để sản xuất $1$ tấn sản phẩm II cần dùng máy thứ nhất $1$ giờ và máy thứ hai $2$ giờ, thu lãi $3$ triệu đồng. Biết mỗi ngày máy thứ nhất hoạt động không quá $9$ giờ và máy thứ hai hoạt động không quá $8$ giờ. Tiền lãi lớn nhất xưởng có thể đạt được trong một ngày là:", ["$17$ triệu đồng", "$12$ triệu đồng", "$15$ triệu đồng", "$19$ triệu đồng"], 0, "Gọi $x, y \\ge 0$ là số tấn sản phẩm I, II sản xuất trong ngày. Ta có hệ $\\begin{cases} x \\ge 0, y \\ge 0 \\\\ 3x + y \\le 9 \\\\ x + 2y \\le 8 \\end{cases}$. Các đỉnh của miền nghiệm tứ giác lồi là $O(0; 0)$, $A(3; 0)$, $B(2; 3)$ và $C(0; 4)$. Hàm tiền lãi $L(x; y) = 4x + 3y$ (triệu đồng) tại các đỉnh: $L(0; 0) = 0$; $L(3; 0) = 12$; $L(2; 3) = 4 \\cdot 2 + 3 \\cdot 3 = 17$; $L(0; 4) = 12$. Vậy tiền lãi lớn nhất là $17$ triệu đồng."),
            short("vandung", "Tìm giá trị lớn nhất của biểu thức $F(x; y) = 5x + 3y$ trên miền nghiệm của hệ bất phương trình $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le 5 \\\\ 2x + y \\le 8 \\end{cases}$.", ["21"], "Các đỉnh của miền nghiệm tứ giác lồi là $O(0; 0), A(0; 5), B(3; 2), C(4; 0)$. Tính giá trị của $F(x; y) = 5x + 3y$ tại các đỉnh: $F(0; 0) = 0$, $F(0; 5) = 15$, $F(3; 2) = 5 \\cdot 3 + 3 \\cdot 2 = 21$, $F(4; 0) = 20$. Vậy giá trị lớn nhất của $F(x; y)$ bằng $21$."),
        ],
    },
    {
        "topic": "l10-ch03-he-thuc-luong-trong-tam-giac",
        "title": "Hệ thức lượng trong tam giác",
        "icon": "📏",
        "description": "Chương III · SGK Toán 10 tập một: Bài 5 – Bài 6. Giá trị lượng giác của một góc từ 0 độ đến 180 độ, quan hệ giữa các giá trị lượng giác của hai góc phụ nhau và hai góc bù nhau; định lí côsin, định lí sin, các công thức tính diện tích tam giác và giải tam giác.",
        "requirements": [
            "Nhận biết được giá trị lượng giác của một góc từ $0^\\circ$ đến $180^\\circ$.",
            "Giải thích được hệ thức liên hệ giữa giá trị lượng giác của các góc phụ nhau, bù nhau.",
            "Sử dụng được máy tính cầm tay để tính các giá trị lượng giác của một góc.",
            "Giải thích được định lí côsin, định lí sin, các công thức tính diện tích tam giác.",
            "Giải quyết được một số vấn đề thực tiễn gắn với việc giải tam giác (ví dụ: tính khoảng cách, chiều cao của vật thể khi không thể đo trực tiếp).",
        ],
        "definition": (
            "- **Giá trị lượng giác của góc $\\alpha$ ($0^\\circ \\le \\alpha \\le 180^\\circ$)**: Trên nửa đường tròn đơn vị tâm $O$ bán kính $R = 1$, lấy điểm $M(x_0; y_0)$ sao cho $\\widehat{xOM} = \\alpha$. Khi đó $\\sin\\alpha = y_0$, $\\cos\\alpha = x_0$, $\\tan\\alpha = \\dfrac{y_0}{x_0}$ ($\\alpha \\ne 90^\\circ$), $\\cot\\alpha = \\dfrac{x_0}{y_0}$ ($\\alpha \\ne 0^\\circ, 180^\\circ$).\n"
            "- **Định lí côsin**: Trong $\\triangle ABC$ với $BC = a, CA = b, AB = c$, ta có $a^2 = b^2 + c^2 - 2bc\\cos A$.\n"
            "- **Định lí sin**: $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R$ (với $R$ là bán kính đường tròn ngoại tiếp $\\triangle ABC$)."
        ),
        "theory": (
            "### Bài 5. Giá trị lượng giác của một góc từ $0^\circ$ đến $180^\circ$\n"
            "- **Dấu của giá trị lượng giác**: Với $0^\\circ < \\alpha < 90^\\circ$ (góc nhọn), cả bốn giá trị lượng giác đều dương; với $90^\\circ < \\alpha < 180^\\circ$ (góc tù), $\\sin\\alpha > 0$ còn $\\cos\\alpha < 0, \\tan\\alpha < 0, \\cot\\alpha < 0$.\n"
            "- **Hai góc bù nhau ($\\alpha$ và $180^\\circ - \\alpha$)**: $\\sin(180^\\circ - \\alpha) = \\sin\\alpha$; $\\cos(180^\\circ - \\alpha) = -\\cos\\alpha$; $\\tan(180^\\circ - \\alpha) = -\\tan\\alpha$; $\\cot(180^\\circ - \\alpha) = -\\cot\\alpha$.\n"
            "- **Các hệ thức cơ bản**: $\\sin^2\\alpha + \\cos^2\\alpha = 1$; $\\tan\\alpha \\cdot \\cot\\alpha = 1$; $1 + \\tan^2\\alpha = \\dfrac{1}{\\cos^2\\alpha}$; $1 + \\cot^2\\alpha = \\dfrac{1}{\\sin^2\\alpha}$.\n"
            "### Bài 6. Hệ thức lượng trong tam giác\n"
            "- **Định lí côsin và hệ quả**: $a^2 = b^2 + c^2 - 2bc\\cos A \\Rightarrow \\cos A = \\dfrac{b^2 + c^2 - a^2}{2bc}$ (tương tự cho $b, c$ và $\\cos B, \\cos C$).\n"
            "- **Định lí sin**: $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R$.\n"
            "- **Các công thức tính diện tích tam giác**: $S = \\dfrac{1}{2}ah_a = \\dfrac{1}{2}bc\\sin A = \\dfrac{abc}{4R} = pr = \\sqrt{p(p - a)(p - b)(p - c)}$ (công thức Heron, với nửa chu vi $p = \\dfrac{a + b + c}{2}$ và bán kính đường tròn nội tiếp $r$).\n"
            "### Bài tập cuối chương III"
        ),
        "formulas": [
            G("I. Giá trị lượng giác ($0^\\circ \\le \\alpha \\le 180^\\circ$)", F("Hai góc bù nhau", "$\\sin(180^\\circ - \\alpha) = \\sin\\alpha, \\quad \\cos(180^\\circ - \\alpha) = -\\cos\\alpha$"), F("Hệ thức lượng giác cơ bản", "$\\sin^2\\alpha + \\cos^2\\alpha = 1, \\quad 1 + \\tan^2\\alpha = \\dfrac{1}{\\cos^2\\alpha} \\; (\\alpha \\ne 90^\\circ)$")),
            G("II. Định lí côsin & Định lí sin", F("Định lí côsin", "$a^2 = b^2 + c^2 - 2bc\\cos A, \\quad \\cos A = \\dfrac{b^2 + c^2 - a^2}{2bc}$"), F("Định lí sin", "$\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R$")),
            G("III. Diện tích tam giác", F("Theo hai cạnh và góc xen giữa", "$S = \\dfrac{1}{2}bc\\sin A = \\dfrac{1}{2}ca\\sin B = \\dfrac{1}{2}ab\\sin C$"), F("Theo bán kính R, r", "$S = \\dfrac{abc}{4R} = pr \\quad \\left(p = \\dfrac{a + b + c}{2}\\right)$"), F("Công thức Heron", "$S = \\sqrt{p(p - a)(p - b)(p - c)}$")),
        ],
        "example": (
            "Cho tam giác $ABC$ có $AB = 5$, $AC = 8$ và $\\widehat{A} = 60^\\circ$.\n"
            "a) Tính độ dài cạnh $BC$ và diện tích $S$ của tam giác $ABC$.\n"
            "b) Tính bán kính đường tròn ngoại tiếp $R$ và bán kính đường tròn nội tiếp $r$ của tam giác $ABC$."
        ),
        "example_answer": (
            "a) Áp dụng định lí côsin trong $\\triangle ABC$:\n"
            "$BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos 60^\\circ = 5^2 + 8^2 - 2 \\cdot 5 \\cdot 8 \\cdot \\dfrac{1}{2} = 49 \\Rightarrow BC = 7$.\n"
            "Diện tích tam giác: $S = \\dfrac{1}{2} \\cdot AB \\cdot AC \\cdot \\sin 60^\\circ = \\dfrac{1}{2} \\cdot 5 \\cdot 8 \\cdot \\dfrac{\\sqrt{3}}{2} = 10\\sqrt{3}$.\n"
            "b) Theo định lí sin: $R = \\dfrac{BC}{2\\sin A} = \\dfrac{7}{2 \\cdot \\dfrac{\\sqrt{3}}{2}} = \\dfrac{7\\sqrt{3}}{3}$.\n"
            "Nửa chu vi $p = \\dfrac{5 + 8 + 7}{2} = 10$, suy ra $r = \\dfrac{S}{p} = \\dfrac{10\\sqrt{3}}{10} = \\sqrt{3}$."
        ),
        "real_life": (
            "- Đo khoảng cách giữa hai địa điểm bị ngăn cách bởi sông hồ hoặc đồi núi và đo chiều cao tháp bằng giác kế.\n"
            "- Định vị hàng hải, hàng không và trắc địa bản đồ dựa trên phương pháp tam giác đạc."
        ),
        "quiz": [
            mcq("biet", "Với góc $\\alpha$ bất kì thoả mãn $0^\\circ \\le \\alpha \\le 180^\\circ$, khẳng định nào sau đây đúng?", ["$\\sin(180^\\circ - \\alpha) = \\sin\\alpha$", "$\\cos(180^\\circ - \\alpha) = \\cos\\alpha$", "$\\sin(180^\\circ - \\alpha) = -\\sin\\alpha$", "$\\tan(180^\\circ - \\alpha) = \\tan\\alpha$"], 0, "Theo tính chất hai góc bù nhau, $\\sin(180^\\circ - \\alpha) = \\sin\\alpha$ còn $\\cos, \\tan, \\cot$ đổi dấu."),
            mcq("biet", "Giá trị của $\\cos 120^\\circ$ bằng bao nhiêu?", ["$-\\dfrac{1}{2}$", "$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$", "$-\\dfrac{\\sqrt{3}}{2}$"], 0, "Ta có $\\cos 120^\\circ = \\cos(180^\\circ - 60^\\circ) = -\\cos 60^\\circ = -\\dfrac{1}{2}$."),
            mcq("biet", "Trong tam giác $ABC$ với $BC = a, CA = b, AB = c$, định lí côsin tại đỉnh $A$ được phát biểu là:", ["$a^2 = b^2 + c^2 - 2bc\\cos A$", "$a^2 = b^2 + c^2 + 2bc\\cos A$", "$a^2 = b^2 + c^2 - bc\\cos A$", "$a^2 = b^2 + c^2 - 2bc\\sin A$"], 0, "Theo định lí côsin trong tam giác $ABC$, ta có $a^2 = b^2 + c^2 - 2bc\\cos A$."),
            mcq("biet", "Trong tam giác $ABC$ có bán kính đường tròn ngoại tiếp là $R$, hệ thức nào sau đây đúng theo định lí sin?", ["$\\dfrac{a}{\\sin A} = 2R$", "$\\dfrac{a}{\\sin A} = R$", "$\\dfrac{a}{\\cos A} = 2R$", "$a\\sin A = 2R$"], 0, "Theo định lí sin trong tam giác $ABC$, ta có $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R$."),
            mcq("hieu", "Cho góc tù $\\alpha$ ($90^\\circ < \\alpha < 180^\\circ$) thoả mãn $\\sin\\alpha = \\dfrac{3}{5}$. Giá trị của $\\cos\\alpha$ là:", ["$-\\dfrac{4}{5}$", "$\\dfrac{4}{5}$", "$-\\dfrac{16}{25}$", "$-\\dfrac{3}{4}$"], 0, "Vì $90^\\circ < \\alpha < 180^\\circ$ nên $\\cos\\alpha < 0$. Ta có $\\cos\\alpha = -\\sqrt{1 - \\sin^2\\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = -\\dfrac{4}{5}$."),
            mcq("hieu", "Cho tam giác $ABC$ có $b = 6, c = 8$ và $\\widehat{A} = 60^\\circ$. Diện tích $S$ của tam giác $ABC$ bằng:", ["$12\\sqrt{3}$", "$24\\sqrt{3}$", "$12$", "$24$"], 0, "Áp dụng công thức diện tích: $S = \\dfrac{1}{2}bc\\sin A = \\dfrac{1}{2} \\cdot 6 \\cdot 8 \\cdot \\sin 60^\\circ = 24 \\cdot \\dfrac{\\sqrt{3}}{2} = 12\\sqrt{3}$."),
            tf4("hieu", "Cho tam giác $ABC$ có $AB = 5, AC = 8$ và $\\widehat{A} = 60^\\circ$. Xét tính đúng sai của các khẳng định sau:", ["a) Độ dài cạnh $BC$ bằng $7$.", "b) Diện tích của tam giác $ABC$ bằng $10\\sqrt{3}$.", "c) Bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R = \\dfrac{7\\sqrt{3}}{3}$.", "d) Bán kính đường tròn nội tiếp tam giác $ABC$ là $r = 2\\sqrt{3}$."], [True, True, True, False], "a) Đúng vì $BC^2 = 5^2 + 8^2 - 2 \\cdot 5 \\cdot 8 \\cos 60^\\circ = 49 \\Rightarrow BC = 7$.\nb) Đúng vì $S = \\dfrac{1}{2} \\cdot 5 \\cdot 8 \\cdot \\sin 60^\\circ = 10\\sqrt{3}$.\nc) Đúng vì $R = \\dfrac{BC}{2\\sin A} = \\dfrac{7}{2 \\cdot \\dfrac{\\sqrt{3}}{2}} = \\dfrac{7\\sqrt{3}}{3}$.\nd) Sai vì nửa chu vi $p = \\dfrac{5 + 8 + 7}{2} = 10$ nên $r = \\dfrac{S}{p} = \\dfrac{10\\sqrt{3}}{10} = \\sqrt{3} \\ne 2\\sqrt{3}$."),
            tf4("hieu", "Cho góc $\\alpha$ thoả mãn $0^\\circ < \\alpha < 180^\\circ$ và $\\cos\\alpha = -\\dfrac{1}{3}$. Xét tính đúng sai của các khẳng định sau:", ["a) Góc $\\alpha$ là một góc tù ($90^\\circ < \\alpha < 180^\\circ$).", "b) Giá trị của $\\sin\\alpha$ là một số âm.", "c) Giá trị của $\\sin\\alpha$ bằng $\\dfrac{2\\sqrt{2}}{3}$.", "d) Giá trị của $\\tan\\alpha$ bằng $-2\\sqrt{2}$."], [True, False, True, True], "a) Đúng vì $\\cos\\alpha < 0$ với $0^\\circ < \\alpha < 180^\\circ$ nên $90^\\circ < \\alpha < 180^\\circ$.\nb) Sai vì với mọi góc $\\alpha \\in (0^\\circ; 180^\\circ)$, ta luôn có $\\sin\\alpha > 0$.\nc) Đúng vì $\\sin\\alpha = \\sqrt{1 - \\cos^2\\alpha} = \\sqrt{1 - \\dfrac{1}{9}} = \\dfrac{2\\sqrt{2}}{3}$.\nd) Đúng vì $\\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha} = \\dfrac{2\\sqrt{2}}{3} : \\left(-\\dfrac{1}{3}\\right) = -2\\sqrt{2}$."),
            mcq("vandung", "Hai tàu thuỷ cùng xuất phát từ một bến cảng $A$, đi thẳng theo hai hướng tạo với nhau một góc $60^\\circ$. Tàu thứ nhất chạy với tốc độ $15\\text{ km} mỗi giờ$, tàu thứ hai chạy với tốc độ $24\\text{ km} mỗi giờ$. Hỏi sau $2$ giờ kể từ lúc xuất phát, khoảng cách giữa hai tàu là bao nhiêu kilômét?", ["$42\\text{ km}$", "$36\\text{ km}$", "$45\\text{ km}$", "$39\\text{ km}$"], 0, "Sau $2$ giờ, quãng đường hai tàu đi được lần lượt là $AB = 15 \\cdot 2 = 30\\text{ (km)}$ và $AC = 24 \\cdot 2 = 48\\text{ (km)}$. Áp dụng định lí côsin trong $\\triangle ABC$ có $\\widehat{A} = 60^\\circ$: $BC^2 = 30^2 + 48^2 - 2 \\cdot 30 \\cdot 48 \\cdot \\cos 60^\\circ = 900 + 2304 - 1440 = 1764 \\Rightarrow BC = \\sqrt{1764} = 42\\text{ (km)}$."),
            short("vandung", "Cho tam giác $ABC$ có độ dài ba cạnh lần lượt là $a = 13, b = 14, c = 15$. Tính bán kính $r$ của đường tròn nội tiếp tam giác $ABC$.", ["4"], "Nửa chu vi của tam giác là $p = \\dfrac{13 + 14 + 15}{2} = 21$. Theo công thức Heron, diện tích tam giác là $S = \\sqrt{21(21 - 13)(21 - 14)(21 - 15)} = \\sqrt{21 \\cdot 8 \\cdot 7 \\cdot 6} = 84$. Bán kính đường tròn nội tiếp là $r = \\dfrac{S}{p} = \\dfrac{84}{21} = 4$."),
        ],
    },
    {
        "topic": "l10-ch04-vecto",
        "title": "Vectơ",
        "icon": "🧭",
        "description": "Chương IV · SGK Toán 10 tập một: Bài 7 – Bài 11. Các khái niệm mở đầu về vectơ; tổng và hiệu của hai vectơ; tích của một vectơ với một số; vectơ trong mặt phẳng toạ độ; tích vô hướng của hai vectơ và ứng dụng.",
        "requirements": [
            "Nhận biết được khái niệm vectơ, hai vectơ cùng phương, cùng hướng, ngược hướng, hai vectơ bằng nhau, hai vectơ đối nhau và vectơ-không $\\overrightarrow{0}$.",
            "Thực hiện được các phép toán trên vectơ (tổng, hiệu hai vectơ theo quy tắc ba điểm, quy tắc hình bình hành; tích của một vectơ với một số; tích vô hướng của hai vectơ) và mô tả được những tính chất hình học (ba điểm thẳng hàng, trung điểm đoạn thẳng, trọng tâm tam giác) bằng vectơ.",
            "Tìm được toạ độ của một điểm và của một vectơ trên mặt phẳng toạ độ $Oxy$; biểu thị được các phép toán vectơ, độ dài vectơ và góc giữa hai vectơ theo toạ độ.",
            "Vận dụng được vectơ vào giải quyết một số bài toán hình học và bài toán thực tiễn (ví dụ: tổng hợp lực, tính công cơ học của một lực).",
        ],
        "definition": (
            "- **Vectơ** là một đoạn thẳng có hướng, kí hiệu $\\overrightarrow{AB}$ (điểm đầu $A$, điểm cuối $B$) hoặc $\\overrightarrow{a}, \\overrightarrow{u}$. Hai vectơ **bằng nhau** ($\\overrightarrow{a} = \\overrightarrow{b}$) nếu chúng có cùng hướng và cùng độ dài.\n"
            "- **Quy tắc ba điểm**: $\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$ và $\\overrightarrow{OB} - \\overrightarrow{OA} = \\overrightarrow{AB}$.\n"
            "- **Vectơ trong mặt phẳng toạ độ $Oxy$**: $\\overrightarrow{u} = x\\overrightarrow{i} + y\\overrightarrow{j} \\Leftrightarrow \\overrightarrow{u} = (x; y)$.\n"
            "- **Tích vô hướng của hai vectơ**: $\\overrightarrow{u} \\cdot \\overrightarrow{v} = |\\overrightarrow{u}| \\cdot |\\overrightarrow{v}| \\cdot \\cos(\\overrightarrow{u}, \\overrightarrow{v}) = x_1 x_2 + y_1 y_2$."
        ),
        "theory": (
            "### Bài 7. Các khái niệm mở đầu\n"
            "- Giá của vectơ $\\overrightarrow{AB}$ là đường thẳng $AB$. Hai vectơ **cùng phương** nếu giá của chúng song song hoặc trùng nhau; hai vectơ cùng phương có thể **cùng hướng** hoặc **ngược hướng**. Vectơ-không $\\overrightarrow{0}$ có độ dài bằng $0$ và cùng phương, cùng hướng với mọi vectơ.\n"
            "### Bài 8. Tổng và hiệu của hai vectơ\n"
            "- **Quy tắc ba điểm**: Với ba điểm $A, B, C$ bất kì, $\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$.\n"
            "- **Quy tắc hình bình hành**: Nếu $ABCD$ là hình bình hành thì $\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$.\n"
            "- **Vectơ đối và hiệu hai vectơ**: $\\overrightarrow{BA} = -\\overrightarrow{AB}$; quy tắc hiệu $\\overrightarrow{OB} - \\overrightarrow{OA} = \\overrightarrow{AB}$.\n"
            "### Bài 9. Tích của một vectơ với một số\n"
            "- Vectơ $k\\overrightarrow{a}$ có độ dài $|k| \\cdot |\\overrightarrow{a}|$, cùng hướng với $\\overrightarrow{a}$ nếu $k \\ge 0$ và ngược hướng với $\\overrightarrow{a}$ nếu $k < 0$.\n"
            "- **Tính chất trung điểm và trọng tâm**: $I$ là trung điểm $AB \\Leftrightarrow \\overrightarrow{IA} + \\overrightarrow{IB} = \\overrightarrow{0} \\Leftrightarrow \\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$; $G$ là trọng tâm $\\triangle ABC \\Leftrightarrow \\overrightarrow{GA} + \\overrightarrow{GB} + \\overrightarrow{GC} = \\overrightarrow{0} \\Leftrightarrow \\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = 3\\overrightarrow{MG}$.\n"
            "- **Điều kiện cùng phương**: $\\overrightarrow{b}$ cùng phương với $\\overrightarrow{a} \\; (\\overrightarrow{a} \\ne \\overrightarrow{0}) \\Leftrightarrow \\exists k \\in \\mathbb{R}: \\overrightarrow{b} = k\\overrightarrow{a}$.\n"
            "### Bài 10. Vectơ trong mặt phẳng toạ độ\n"
            "- Cho $A(x_A; y_A), B(x_B; y_B) \\Rightarrow \\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$ và $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.\n"
            "- Cho $\\overrightarrow{u} = (x_1; y_1), \\overrightarrow{v} = (x_2; y_2) \\Rightarrow \\overrightarrow{u} \\pm \\overrightarrow{v} = (x_1 \\pm x_2; y_1 \\pm y_2)$ và $k\\overrightarrow{u} = (kx_1; ky_1)$.\n"
            "### Bài 11. Tích vô hướng của hai vectơ\n"
            "- Công thức định nghĩa: $\\overrightarrow{u} \\cdot \\overrightarrow{v} = |\\overrightarrow{u}| \\cdot |\\overrightarrow{v}| \\cdot \\cos(\\overrightarrow{u}, \\overrightarrow{v})$.\n"
            "- Biểu thức toạ độ: $\\overrightarrow{u} \\cdot \\overrightarrow{v} = x_1 x_2 + y_1 y_2$; $\\overrightarrow{u} \\perp \\overrightarrow{v} \\Leftrightarrow x_1 x_2 + y_1 y_2 = 0$; $\\cos(\\overrightarrow{u}, \\overrightarrow{v}) = \\dfrac{x_1 x_2 + y_1 y_2}{\\sqrt{x_1^2 + y_1^2} \\cdot \\sqrt{x_2^2 + y_2^2}}$.\n"
            "### Bài tập cuối chương IV"
        ),
        "formulas": [
            G("I. Quy tắc vectơ & Hệ thức đặc biệt", F("Quy tắc ba điểm và quy tắc hiệu", "$\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}, \\quad \\overrightarrow{OB} - \\overrightarrow{OA} = \\overrightarrow{AB}$"), F("Quy tắc hình bình hành ABCD", "$\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$"), F("Hệ thức trung điểm I và trọng tâm G", "$\\overrightarrow{IA} + \\overrightarrow{IB} = \\overrightarrow{0}, \\quad \\overrightarrow{GA} + \\overrightarrow{GB} + \\overrightarrow{GC} = \\overrightarrow{0}$")),
            G("II. Toạ độ vectơ & Điểm trong mặt phẳng Oxy", F("Toạ độ và độ dài vectơ AB", "$\\overrightarrow{AB} = (x_B - x_A; y_B - y_A), \\quad AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$"), F("Toạ độ trung điểm I và trọng tâm G", "$I\\left(\\dfrac{x_A + x_B}{2}; \\dfrac{y_A + y_B}{2}\\right), \\quad G\\left(\\dfrac{x_A + x_B + x_C}{3}; \\dfrac{y_A + y_B + y_C}{3}\\right)$")),
            G("III. Tích vô hướng của hai vectơ", F("Định nghĩa và biểu thức toạ độ", "$\\overrightarrow{u} \\cdot \\overrightarrow{v} = |\\overrightarrow{u}| \\cdot |\\overrightarrow{v}| \\cdot \\cos(\\overrightarrow{u}, \\overrightarrow{v}) = x_1 x_2 + y_1 y_2$"), F("Điều kiện vuông góc và góc giữa hai vectơ", "$\\overrightarrow{u} \\perp \\overrightarrow{v} \\iff x_1 x_2 + y_1 y_2 = 0, \\quad \\cos(\\overrightarrow{u}, \\overrightarrow{v}) = \\dfrac{x_1 x_2 + y_1 y_2}{\\sqrt{x_1^2 + y_1^2}\\sqrt{x_2^2 + y_2^2}}$")),
        ],
        "example": (
            "Trong mặt phẳng toạ độ $Oxy$, cho ba điểm $A(1; 2)$, $B(4; 6)$ và $C(-3; 5)$.\n"
            "a) Tìm toạ độ các vectơ $\\overrightarrow{AB}, \\overrightarrow{AC}$ và chứng minh tam giác $ABC$ vuông cân tại $A$.\n"
            "b) Tìm toạ độ trọng tâm $G$ của tam giác $ABC$ và đỉnh $D$ để tứ giác $ABCD$ là hình bình hành."
        ),
        "example_answer": (
            "a) Ta có $\\overrightarrow{AB} = (4 - 1; 6 - 2) = (3; 4)$ và $\\overrightarrow{AC} = (-3 - 1; 5 - 2) = (-4; 3)$.\n"
            "Vì $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = 3 \\cdot (-4) + 4 \\cdot 3 = 0$ nên $\\overrightarrow{AB} \\perp \\overrightarrow{AC}$, hay $\\triangle ABC$ vuông tại $A$.\n"
            "Mặt khác $AB = \\sqrt{3^2 + 4^2} = 5$ và $AC = \\sqrt{(-4)^2 + 3^2} = 5$, suy ra $\\triangle ABC$ **vuông cân tại $A$**.\n"
            "b) Trọng tâm $G$ có toạ độ $G\\left(\\dfrac{1 + 4 - 3}{3}; \\dfrac{2 + 6 + 5}{3}\\right) = G\\left(\\dfrac{2}{3}; \\dfrac{13}{3}\\right)$.\n"
            "Để $ABCD$ là hình bình hành thì $\\overrightarrow{AD} = \\overrightarrow{BC} = (-7; -1) \\Rightarrow D(1 - 7; 2 - 1) = D(-6; 1)$."
        ),
        "real_life": (
            "- Biểu diễn các đại lượng có hướng trong Vật lí như độ dịch chuyển $\\overrightarrow{d}$, vận tốc $\\overrightarrow{v}$, gia tốc $\\overrightarrow{a}$ và lực $\\overrightarrow{F}$.\n"
            "- Tính công cơ học của lực không đổi theo tích vô hướng $A = \\overrightarrow{F} \\cdot \\overrightarrow{d} = F \\cdot d \\cdot \\cos\\alpha$."
        ),
        "quiz": [
            mcq("biet", "Cho ba điểm $A, B, C$ bất kì. Theo quy tắc ba điểm, khẳng định nào dưới đây đúng?", ["$\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$", "$\\overrightarrow{AB} + \\overrightarrow{AC} = \\overrightarrow{BC}$", "$\\overrightarrow{AB} - \\overrightarrow{BC} = \\overrightarrow{AC}$", "$\\overrightarrow{BA} + \\overrightarrow{BC} = \\overrightarrow{AC}$"], 0, "Theo quy tắc ba điểm đối với phép cộng vectơ, ta luôn có $\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$."),
            mcq("biet", "Cho hình bình hành $ABCD$. Theo quy tắc hình bình hành, tổng $\\overrightarrow{AB} + \\overrightarrow{AD}$ bằng vectơ nào?", ["$\\overrightarrow{AC}$", "$\\overrightarrow{BD}$", "$\\overrightarrow{CA}$", "$\\overrightarrow{DB}$"], 0, "Trong hình bình hành $ABCD$, theo quy tắc hình bình hành ta có $\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$."),
            mcq("biet", "Trong mặt phẳng toạ độ $Oxy$, cho hai điểm $A(x_A; y_A)$ và $B(x_B; y_B)$. Toạ độ của vectơ $\\overrightarrow{AB}$ là:", ["$(x_B - x_A; y_B - y_A)$", "$(x_A - x_B; y_A - y_B)$", "$(x_A + x_B; y_A + y_B)$", "$\\left(\\dfrac{x_A + x_B}{2}; \\dfrac{y_A + y_B}{2}\\right)$"], 0, "Toạ độ của vectơ $\\overrightarrow{AB}$ lấy toạ độ điểm cuối trừ toạ độ điểm đầu: $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$."),
            mcq("biet", "Trong mặt phẳng toạ độ $Oxy$, tích vô hướng của hai vectơ $\\overrightarrow{u} = (x_1; y_1)$ và $\\overrightarrow{v} = (x_2; y_2)$ bằng:", ["$x_1 x_2 + y_1 y_2$", "$x_1 y_2 - x_2 y_1$", "$x_1 x_2 - y_1 y_2$", "$(x_1 + x_2)(y_1 + y_2)$"], 0, "Theo biểu thức toạ độ của tích vô hướng, $\\overrightarrow{u} \\cdot \\overrightarrow{v} = x_1 x_2 + y_1 y_2$."),
            mcq("hieu", "Cho đoạn thẳng $AB$ có trung điểm $I$ và điểm $M$ bất kì. Khẳng định nào sau đây đúng?", ["$\\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$", "$\\overrightarrow{MA} + \\overrightarrow{MB} = \\overrightarrow{MI}$", "$\\overrightarrow{MA} - \\overrightarrow{MB} = 2\\overrightarrow{MI}$", "$\\overrightarrow{MA} + \\overrightarrow{MB} = \\overrightarrow{0}$"], 0, "Với $I$ là trung điểm của đoạn thẳng $AB$ và điểm $M$ bất kì, ta luôn có $\\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$."),
            mcq("hieu", "Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\\overrightarrow{a} = (3; -4)$ và $\\overrightarrow{b} = (-1; 2)$. Toạ độ của vectơ $\\overrightarrow{u} = 2\\overrightarrow{a} - 3\\overrightarrow{b}$ là:", ["$(9; -14)$", "$(3; -2)$", "$(9; -2)$", "$(3; -14)$"], 0, "Ta có $2\\overrightarrow{a} = (6; -8)$ và $3\\overrightarrow{b} = (-3; 6)$, suy ra $\\overrightarrow{u} = 2\\overrightarrow{a} - 3\\overrightarrow{b} = (6 - (-3); -8 - 6) = (9; -14)$."),
            tf4("hieu", "Cho tam giác đều $ABC$ có cạnh bằng $4$ và $M$ là trung điểm của cạnh $BC$. Xét tính đúng sai của các khẳng định sau:", ["a) Độ dài của vectơ $\\overrightarrow{AB}$ bằng $4$.", "b) Đẳng thức $\\overrightarrow{AB} + \\overrightarrow{AC} = 2\\overrightarrow{AM}$ luôn đúng.", "c) Góc giữa hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{BC}$ bằng $60^\\circ$.", "d) Tích vô hướng $\\overrightarrow{AB} \\cdot \\overrightarrow{AC}$ bằng $8$."], [True, True, False, True], "a) Đúng vì $|\\overrightarrow{AB}| = AB = 4$.\nb) Đúng theo hệ thức trung điểm $M$ của cạnh $BC$.\nc) Sai vì khi dựng $\\overrightarrow{BD} = \\overrightarrow{AB}$ thì góc giữa $\\overrightarrow{AB}$ và $\\overrightarrow{BC}$ là $\\widehat{DBC} = 180^\\circ - 60^\\circ = 120^\\circ$.\nd) Đúng vì $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = AB \\cdot AC \\cdot \\cos 60^\\circ = 4 \\cdot 4 \\cdot \\dfrac{1}{2} = 8$."),
            tf4("hieu", "Trong mặt phẳng toạ độ $Oxy$, cho ba điểm $A(1; 2), B(4; 6), C(-3; 5)$. Xét tính đúng sai của các khẳng định sau:", ["a) Vectơ $\\overrightarrow{AB}$ có toạ độ $(3; 4)$ và độ dài đoạn thẳng $AB = 5$.", "b) Trọng tâm $G$ của tam giác $ABC$ có toạ độ là $G\\left(\\dfrac{2}{3}; \\dfrac{13}{3}\\right)$.", "c) Tích vô hướng $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = 0$ nên tam giác $ABC$ vuông tại $A$.", "d) Chu vi của tam giác $ABC$ bằng $15$."], [True, True, True, False], "a) Đúng vì $\\overrightarrow{AB} = (3; 4) \\Rightarrow AB = \\sqrt{3^2 + 4^2} = 5$.\nb) Đúng vì $x_G = \\dfrac{1 + 4 - 3}{3} = \\dfrac{2}{3}$ và $y_G = \\dfrac{2 + 6 + 5}{3} = \\dfrac{13}{3}$.\nc) Đúng vì $\\overrightarrow{AC} = (-4; 3) \\Rightarrow \\overrightarrow{AB} \\cdot \\overrightarrow{AC} = 3(-4) + 4 \\cdot 3 = 0$.\nd) Sai vì $AB = 5, AC = 5$ nhưng $BC = \\sqrt{(-7)^2 + (-1)^2} = 5\\sqrt{2}$ nên chu vi là $10 + 5\\sqrt{2} \\ne 15$."),
            mcq("vandung", "Hai lực $\\overrightarrow{F_1}, \\overrightarrow{F_2}$ cùng tác dụng vào một vật tại điểm $O$, biết cường độ hai lực là $|\\overrightarrow{F_1}| = 30\\text{ N}, |\\overrightarrow{F_2}| = 40\\text{ N}$ và góc hợp bởi hai vectơ lực bằng $60^\\circ$. Cường độ hợp lực $\\overrightarrow{F} = \\overrightarrow{F_1} + \\overrightarrow{F_2}$ tác dụng lên vật là:", ["$10\\sqrt{37}\\text{ N}$", "$50\\text{ N}$", "$70\\text{ N}$", "$10\\sqrt{13}\\text{ N}$"], 0, "Ta có $|\\overrightarrow{F}|^2 = (\\overrightarrow{F_1} + \\overrightarrow{F_2})^2 = F_1^2 + F_2^2 + 2 F_1 F_2 \\cos 60^\\circ = 30^2 + 40^2 + 2 \\cdot 30 \\cdot 40 \\cdot \\dfrac{1}{2} = 3700$. Suy ra $|\\overrightarrow{F}| = \\sqrt{3700} = 10\\sqrt{37}\\text{ (N)}$."),
            short("vandung", "Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\\overrightarrow{u} = (2; -1)$ và $\\overrightarrow{v} = (m; 6)$. Tìm giá trị của tham số $m$ để hai vectơ $\\overrightarrow{u}$ và $\\overrightarrow{v}$ vuông góc với nhau.", ["3"], "Để $\\overrightarrow{u} \\perp \\overrightarrow{v}$ thì $\\overrightarrow{u} \\cdot \\overrightarrow{v} = 0 \\Leftrightarrow 2 \\cdot m + (-1) \\cdot 6 = 0 \\Leftrightarrow 2m = 6 \\Leftrightarrow m = 3$."),
        ],
    },
    {
        "topic": "l10-ch05-cac-so-dac-trung-cua-mau-so-lieu-khong-ghep-nhom",
        "title": "Các số đặc trưng của mẫu số liệu không ghép nhóm",
        "icon": "📊",
        "description": "Chương V · SGK Toán 10 tập một: Bài 12 – Bài 14. Số gần đúng, sai số tuyệt đối, sai số tương đối và số quy tròn; các số đặc trưng đo xu thế trung tâm gồm số trung bình, trung vị, tứ phân vị và mốt; các số đặc trưng đo độ phân tán gồm khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn và phát hiện giá trị bất thường.",
        "requirements": [
            "Hiểu được khái niệm số gần đúng, sai số tuyệt đối $\\Delta_a$, độ chính xác $d$, sai số tương đối $\\delta_a$ và quy tròn được số gần đúng căn cứ vào độ chính xác cho trước.",
            "Tính được các số đặc trưng đo xu thế trung tâm cho mẫu số liệu không ghép nhóm: số trung bình $\\bar{x}$, trung vị $M_e$, tứ phân vị $Q_1, Q_2, Q_3$, mốt $M_o$ và giải thích được ý nghĩa của chúng.",
            "Tính được các số đặc trưng đo độ phân tán cho mẫu số liệu không ghép nhóm: khoảng biến thiên $R$, khoảng tứ phân vị $\\Delta_Q$, phương sai $s^2$, độ lệch chuẩn $s$ và giải thích được ý nghĩa của chúng.",
            "Chỉ ra được những kết luận hợp lí dựa trên các số đặc trưng và phát hiện được giá trị bất thường (ngoại lệ) trong mẫu số liệu bằng khoảng tứ phân vị.",
        ],
        "definition": (
            "- **Sai số tuyệt đối** của số gần đúng $a$ so với số đúng $\\bar{a}$ là $\\Delta_a = |\\bar{a} - a| \\le d$ (với $d$ là độ chính xác). **Sai số tương đối** là $\\delta_a = \\dfrac{\\Delta_a}{|a|} \\le \\dfrac{d}{|a|}$.\n"
            "- **Các số đặc trưng đo xu thế trung tâm**: Số trung bình $\\bar{x}$, trung vị $M_e$ (hay $Q_2$), bộ ba tứ phân vị $Q_1, Q_2, Q_3$ chia mẫu đã sắp xếp thành $4$ phần bằng nhau, và mốt $M_o$ (giá trị có tần số lớn nhất).\n"
            "- **Các số đặc trưng đo độ phân tán**: Khoảng biến thiên $R = x_{\\max} - x_{\\min}$; khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$; phương sai $s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2$ và độ lệch chuẩn $s = \\sqrt{s^2}$."
        ),
        "theory": (
            "### Bài 12. Số gần đúng và sai số\n"
            "- Nếu $|\\bar{a} - a| \\le d$ thì $\\bar{a} = a \\pm d$ ($d$ là độ chính xác). **Quy tắc làm tròn theo độ chính xác $d$**: Nếu hàng lớn nhất của $d$ là hàng nào thì ta quy tròn số gần đúng $a$ đến hàng kế trước nó (ví dụ $d$ ở hàng phần trăm thì quy tròn $a$ đến hàng phần mười; $d$ ở hàng trăm thì quy tròn $a$ đến hàng nghìn).\n"
            "### Bài 13. Các số đặc trưng đo xu thế trung tâm\n"
            "- **Số trung bình**: $\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + x_n}{n}$ (hoặc $\\bar{x} = \\dfrac{n_1 x_1 + \\dots + n_k x_k}{n}$ với bảng tần số).\n"
            "- **Trung vị ($M_e$) và Tứ phân vị ($Q_1, Q_2, Q_3$)**: Sắp xếp mẫu số liệu theo thứ tự không giảm. $Q_2 = M_e$ là trung vị của cả mẫu; $Q_1$ là trung vị của nửa mẫu bên trái $Q_2$ (không bao gồm $Q_2$ nếu $n$ lẻ); $Q_3$ là trung vị của nửa mẫu bên phải $Q_2$.\n"
            "- **Mốt ($M_o$)**: Giá trị xuất hiện với tần số lớn nhất trong mẫu.\n"
            "### Bài 14. Các số đặc trưng đo độ phân tán\n"
            "- **Khoảng biến thiên và khoảng tứ phân vị**: $R = x_{\\max} - x_{\\min}$ và $\\Delta_Q = Q_3 - Q_1$. Giá trị $x$ trong mẫu được coi là **giá trị bất thường (ngoại lệ)** nếu $x > Q_3 + 1,5\\Delta_Q$ hoặc $x < Q_1 - 1,5\\Delta_Q$.\n"
            "- **Phương sai và độ lệch chuẩn**: $s^2 = \\dfrac{1}{n}\\left[(x_1 - \\bar{x})^2 + \\dots + (x_n - \\bar{x})^2\\right] = \\left(\\dfrac{1}{n}\\sum_{i=1}^n x_i^2\\right) - \\bar{x}^2$, độ lệch chuẩn $s = \\sqrt{s^2}$ có cùng đơn vị đo với dữ liệu.\n"
            "### Bài tập cuối chương V"
        ),
        "formulas": [
            G("I. Số gần đúng & Sai số", F("Sai số tuyệt đối và độ chính xác", "$\\Delta_a = |\\bar{a} - a| \\le d \\iff a - d \\le \\bar{a} \\le a + d$"), F("Đánh giá sai số tương đối", "$\\delta_a = \\dfrac{\\Delta_a}{|a|} \\le \\dfrac{d}{|a|}$")),
            G("II. Số đặc trưng đo xu thế trung tâm", F("Số trung bình cộng", "$\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + x_n}{n} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$"), F("Tứ phân vị", "$Q_2 = M_e; \\quad Q_1: \\text{trung vị nửa dưới}; \\quad Q_3: \\text{trung vị nửa trên}$")),
            G("III. Số đặc trưng đo độ phân tán", F("Khoảng biến thiên và khoảng tứ phân vị", "$R = x_{\\max} - x_{\\min}, \\quad \\Delta_Q = Q_3 - Q_1$"), F("Phương sai và độ lệch chuẩn", "$s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2, \\quad s = \\sqrt{s^2}$"), F("Ngưỡng phát hiện giá trị ngoại lệ", "$x < Q_1 - 1,5\\Delta_Q \\quad \\text{hoặc} \\quad x > Q_3 + 1,5\\Delta_Q$")),
        ],
        "example": (
            "Cho mẫu số liệu thống kê điểm bài kiểm tra của $8$ học sinh: $4; 5; 6; 6; 8; 8; 9; 10$.\n"
            "a) Tìm số trung bình $\\bar{x}$, các tứ phân vị $Q_1, Q_2, Q_3$ và khoảng tứ phân vị $\\Delta_Q$.\n"
            "b) Tính phương sai $s^2$ và độ lệch chuẩn $s$ của mẫu số liệu trên."
        ),
        "example_answer": (
            "a) Mẫu số liệu đã sắp xếp không giảm với $n = 8$:\n"
            "- Số trung bình: $\\bar{x} = \\dfrac{4 + 5 + 6 + 6 + 8 + 8 + 9 + 10}{8} = \\dfrac{56}{8} = 7$.\n"
            "- Trung vị $Q_2 = \\dfrac{6 + 8}{2} = 7$; nửa dưới $4; 5; 6; 6 \\Rightarrow Q_1 = \\dfrac{5 + 6}{2} = 5,5$; nửa trên $8; 8; 9; 10 \\Rightarrow Q_3 = \\dfrac{8 + 9}{2} = 8,5$.\n"
            "- Khoảng tứ phân vị: $\\Delta_Q = Q_3 - Q_1 = 8,5 - 5,5 = 3$.\n"
            "b) Phương sai: $s^2 = \\dfrac{(4 - 7)^2 + (5 - 7)^2 + 2(6 - 7)^2 + 2(8 - 7)^2 + (9 - 7)^2 + (10 - 7)^2}{8} = \\dfrac{9 + 4 + 2 + 2 + 4 + 9}{8} = \\dfrac{30}{8} = 3,75$.\n"
            "Độ lệch chuẩn: $s = \\sqrt{3,75} = \\dfrac{\\sqrt{15}}{2} \\approx 1,94$."
        ),
        "real_life": (
            "- Đánh giá độ ổn định của nhiệt độ thời tiết, năng suất cây trồng, chất lượng dây chuyền sản xuất công nghiệp hoặc rủi ro biến động giá cổ phiếu thông qua độ lệch chuẩn $s$.\n"
            "- Sử dụng trung vị và tứ phân vị để phân tích mức thu nhập dân cư mà không bị sai lệch bởi một vài giá trị thu nhập quá cao (giá trị ngoại lệ)."
        ),
        "quiz": [
            mcq("biet", "Nếu $a$ là số gần đúng của số đúng $\\bar{a}$ thì sai số tuyệt đối $\\Delta_a$ được xác định bởi công thức nào?", ["$\\Delta_a = |\\bar{a} - a|$", "$\\Delta_a = \\dfrac{|\\bar{a} - a|}{|a|}$", "$\\Delta_a = \\bar{a} + a$", "$\\Delta_a = |\\bar{a}| + |a|$"], 0, "Theo định nghĩa, sai số tuyệt đối của số gần đúng $a$ là $\\Delta_a = |\\bar{a} - a|$."),
            mcq("biet", "Số đặc trưng nào dưới đây bằng hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất của mẫu số liệu?", ["Khoảng biến thiên $R$", "Khoảng tứ phân vị $\\Delta_Q$", "Phương sai $s^2$", "Trung vị $M_e$"], 0, "Khoảng biến thiên $R = x_{\\max} - x_{\\min}$ là hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất của mẫu số liệu."),
            mcq("biet", "Khoảng tứ phân vị $\\Delta_Q$ của một mẫu số liệu được tính theo công thức nào?", ["$\\Delta_Q = Q_3 - Q_1$", "$\\Delta_Q = Q_3 - Q_2$", "$\\Delta_Q = Q_2 - Q_1$", "$\\Delta_Q = \\dfrac{Q_1 + Q_3}{2}$"], 0, "Theo định nghĩa, khoảng tứ phân vị là hiệu giữa tứ phân vị thứ ba và tứ phân vị thứ nhất: $\\Delta_Q = Q_3 - Q_1$."),
            mcq("biet", "Căn bậc hai số học của phương sai $s^2$ của một mẫu số liệu được gọi là gì?", ["Độ lệch chuẩn $s$", "Khoảng biến thiên $R$", "Sai số tương đối $\\delta_a$", "Số trung bình $\\bar{x}$"], 0, "Căn bậc hai số học của phương sai $s^2$ là độ lệch chuẩn $s = \\sqrt{s^2}$."),
            mcq("hieu", "Quy tròn số gần đúng $a = 24,6782$ với độ chính xác $d = 0,02$, ta được số quy tròn là:", ["$24,7$", "$24,68$", "$24,678$", "$25$"], 0, "Hàng lớn nhất của độ chính xác $d = 0,02$ là hàng phần trăm, do đó ta quy tròn số $a$ đến hàng phần mười được $24,7$."),
            mcq("hieu", "Cho mẫu số liệu điểm kiểm tra của $7$ học sinh: $5; 6; 7; 7; 8; 9; 10$. Trung vị $M_e$ và mốt $M_o$ của mẫu số liệu lần lượt là:", ["$M_e = 7$ và $M_o = 7$", "$M_e = 7,5$ và $M_o = 7$", "$M_e = 7$ và $M_o = 10$", "$M_e = 8$ và $M_o = 7$"], 0, "Mẫu gồm $7$ số đã sắp xếp có số chính giữa (thứ $4$) là $7$ nên $M_e = 7$; số $7$ xuất hiện nhiều nhất ($2$ lần) nên $M_o = 7$."),
            tf4("hieu", "Cho mẫu số liệu gồm $8$ giá trị đã sắp xếp không giảm: $2; 4; 5; 6; 8; 9; 10; 12$. Xét tính đúng sai của các khẳng định sau:", ["a) Số trung bình của mẫu số liệu là $\\bar{x} = 7$.", "b) Trung vị (tứ phân vị thứ hai $Q_2$) của mẫu số liệu là $Q_2 = 7$.", "c) Tứ phân vị thứ nhất là $Q_1 = 4,5$ và tứ phân vị thứ ba là $Q_3 = 9,5$.", "d) Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = 6$."], [True, True, True, False], "a) Đúng vì $\\bar{x} = \\dfrac{2 + 4 + 5 + 6 + 8 + 9 + 10 + 12}{8} = \\dfrac{56}{8} = 7$.\nb) Đúng vì $Q_2 = \\dfrac{6 + 8}{2} = 7$.\nc) Đúng vì nửa dưới $2; 4; 5; 6$ có $Q_1 = \\dfrac{4 + 5}{2} = 4,5$; nửa trên $8; 9; 10; 12$ có $Q_3 = \\dfrac{9 + 10}{2} = 9,5$.\nd) Sai vì $\\Delta_Q = Q_3 - Q_1 = 9,5 - 4,5 = 5 \\ne 6$."),
            tf4("hieu", "Cho mẫu số liệu gồm $5$ giá trị: $4; 6; 8; 10; 12$. Xét tính đúng sai của các khẳng định sau:", ["a) Khoảng biến thiên của mẫu số liệu là $R = 8$.", "b) Số trung bình của mẫu số liệu là $\\bar{x} = 8$.", "c) Phương sai của mẫu số liệu là $s^2 = 8$.", "d) Độ lệch chuẩn của mẫu số liệu là $s = 4$."], [True, True, True, False], "a) Đúng vì $R = 12 - 4 = 8$.\nb) Đúng vì $\\bar{x} = \\dfrac{4 + 6 + 8 + 10 + 12}{5} = 8$.\nc) Đúng vì $s^2 = \\dfrac{(4 - 8)^2 + (6 - 8)^2 + (8 - 8)^2 + (10 - 8)^2 + (12 - 8)^2}{5} = \\dfrac{40}{5} = 8$.\nd) Sai vì độ lệch chuẩn là $s = \\sqrt{8} = 2\\sqrt{2} \\approx 2,83 \\ne 4$."),
            mcq("vandung", "Một mẫu số liệu thống kê có tứ phân vị thứ nhất $Q_1 = 14$ và tứ phân vị thứ ba $Q_3 = 22$. Giá trị nào dưới đây nếu xuất hiện trong mẫu số liệu sẽ được xem là giá trị bất thường (ngoại lệ)?", ["$36$", "$30$", "$5$", "$34$"], 0, "Khoảng tứ phân vị là $\\Delta_Q = Q_3 - Q_1 = 22 - 14 = 8 \\Rightarrow 1,5\\Delta_Q = 12$. Giá trị bất thường khi nhỏ hơn $Q_1 - 1,5\\Delta_Q = 2$ hoặc lớn hơn $Q_3 + 1,5\\Delta_Q = 34$. Vì $36 > 34$ nên $36$ là giá trị bất thường."),
            short("vandung", "Cho mẫu số liệu gồm $4$ giá trị: $3; 5; 7; 9$. Tính phương sai $s^2$ của mẫu số liệu trên.", ["5"], "Ta có số trung bình $\\bar{x} = \\dfrac{3 + 5 + 7 + 9}{4} = 6$. Phương sai của mẫu số liệu là $s^2 = \\dfrac{(3 - 6)^2 + (5 - 6)^2 + (7 - 6)^2 + (9 - 6)^2}{4} = \\dfrac{9 + 1 + 1 + 9}{4} = 5$."),
        ],
    },
    {
        "topic": "l10-ch06-ham-so-do-thi-va-ung-dung",
        "game_title": "Hàm số bậc nhất – bậc hai trong bài toán Quản lý cửa hàng",
        "game_description": "Vận dụng hàm số bậc nhất (chi phí) và hàm số bậc hai (doanh thu, lợi nhuận) để tìm mức giá tối ưu giúp cửa hàng đạt lợi nhuận cực đại.",
        "game_type": "store-management",
        "title": "Hàm số, đồ thị và ứng dụng",
        "icon": "📈",
        "description": "Chương VI · SGK Toán 10 tập hai: Bài 15 – Bài 18. Hàm số, tập xác định, tập giá trị, sự biến thiên và đồ thị của hàm số; hàm số bậc hai và parabol; dấu của tam thức bậc hai và bất phương trình bậc hai một ẩn; hai dạng phương trình chứa căn thức quy về phương trình bậc hai.",
        "requirements": [
            "Nhận biết được những mô hình thực tế dẫn đến khái niệm hàm số; tìm được tập xác định, tập giá trị và xét được sự đồng biến, nghịch biến của hàm số trên một khoảng dựa vào đồ thị hoặc bảng biến thiên.",
            "Thiết lập được bảng giá trị, vẽ được đồ thị hàm số bậc hai $y = ax^2 + bx + c \\; (a \\ne 0)$ và nhận biết được các tính chất cơ bản của parabol (đỉnh, trục đối xứng, khoảng đồng biến, nghịch biến, giá trị lớn nhất hoặc nhỏ nhất).",
            "Giải thích được định lí về dấu của tam thức bậc hai $f(x) = ax^2 + bx + c \\; (a \\ne 0)$ từ việc quan sát đồ thị và giải được bất phương trình bậc hai một ẩn.",
            "Giải được phương trình chứa căn thức có dạng $\\sqrt{ax^2 + bx + c} = \\sqrt{dx^2 + ex + f}$ và $\\sqrt{ax^2 + bx + c} = dx + e$ quy về phương trình bậc hai.",
            "Vận dụng được kiến thức về hàm số bậc hai và bất phương trình bậc hai vào giải quyết một số bài toán thực tiễn (ví dụ: chuyển động ném xiên, thiết kế vòm cầu parabol, bài toán tối ưu doanh thu).",
        ],
        "definition": (
            "- **Hàm số**: Nếu với mỗi giá trị của $x$ thuộc tập hợp số $D$ có một và chỉ một giá trị tương ứng của $y$ thuộc $\\mathbb{R}$ thì ta có một hàm số. $D$ gọi là **tập xác định**, $T = \\{y = f(x) \\mid x \\in D\\}$ gọi là **tập giá trị**.\n"
            "- **Hàm số bậc hai**: $y = ax^2 + bx + c \\; (a \\ne 0)$ có tập xác định $\\mathbb{R}$ và đồ thị là một đường **parabol** có đỉnh $I\\left(-\\dfrac{b}{2a}; -\\dfrac{\\Delta}{4a}\\right)$, trục đối xứng $x = -\\dfrac{b}{2a}$ (với $\\Delta = b^2 - 4ac$).\n"
            "- **Tam thức bậc hai**: Biểu thức dạng $f(x) = ax^2 + bx + c \\; (a \\ne 0)$.\n"
            "- **Định lí về dấu của tam thức bậc hai**: Nếu $\\Delta < 0$ thì $f(x)$ cùng dấu với $a$ với mọi $x \\in \\mathbb{R}$; nếu $\\Delta = 0$ thì $f(x)$ cùng dấu với $a$ với mọi $x \\ne -\\dfrac{b}{2a}$; nếu $\\Delta > 0$ ($2$ nghiệm $x_1 < x_2$) thì $f(x)$ trái dấu với $a$ trên $(x_1; x_2)$ và cùng dấu với $a$ trên $(-\\infty; x_1) \\cup (x_2; +\\infty)$."
        ),
        "theory": (
            "### Bài 15. Hàm số\n"
            "- **Tập xác định**: Tập tất cả các số thực $x$ sao cho biểu thức $f(x)$ có nghĩa (mẫu thức khác $0$: $\\dfrac{1}{A(x)} \\Rightarrow A(x) \\ne 0$; căn bậc hai: $\\sqrt{A(x)} \\Rightarrow A(x) \\ge 0$).\n"
            "- **Sự biến thiên**: Trên khoảng $(a; b)$, hàm số **đồng biến** nếu $\\forall x_1, x_2 \\in (a; b), x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$ (đồ thị đi lên từ trái sang phải); **nghịch biến** nếu $x_1 < x_2 \\Rightarrow f(x_1) > f(x_2)$ (đồ thị đi xuống từ trái sang phải).\n"
            "### Bài 16. Hàm số bậc hai\n"
            "- Đồ thị hàm số $y = ax^2 + bx + c \\; (a \\ne 0)$ là parabol có đỉnh $I\\left(-\\dfrac{b}{2a}; -\\dfrac{\\Delta}{4a}\\right)$ và trục đối xứng $x = -\\dfrac{b}{2a}$.\n"
            "- Nếu $a > 0$: bề lõm quay lên trên, hàm số nghịch biến trên $\\left(-\\infty; -\\dfrac{b}{2a}\\right)$, đồng biến trên $\\left(-\\dfrac{b}{2a}; +\\infty\\right)$ và đạt giá trị nhỏ nhất $-\\dfrac{\\Delta}{4a}$ tại $x = -\\dfrac{b}{2a}$.\n"
            "- Nếu $a < 0$: bề lõm quay xuống dưới, hàm số đồng biến trên $\\left(-\\infty; -\\dfrac{b}{2a}\\right)$, nghịch biến trên $\\left(-\\dfrac{b}{2a}; +\\infty\\right)$ và đạt giá trị lớn nhất $-\\dfrac{\\Delta}{4a}$ tại $x = -\\dfrac{b}{2a}$.\n"
            "### Bài 17. Dấu của tam thức bậc hai\n"
            "- Quy tắc xét dấu khi $\\Delta > 0$: **Trong trái, ngoài cùng** (trong khoảng hai nghiệm $(x_1; x_2)$ thì $f(x)$ trái dấu với $a$; ngoài khoảng hai nghiệm thì $f(x)$ cùng dấu với $a$).\n"
            "- Điều kiện tam thức không đổi dấu trên $\\mathbb{R}$: $f(x) > 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 \\\\ \\Delta < 0 \\end{cases}$; $f(x) \\ge 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 \\\\ \\Delta \\le 0 \\end{cases}$.\n"
            "### Bài 18. Phương trình quy về phương trình bậc hai\n"
            "- **Dạng 1**: $\\sqrt{ax^2 + bx + c} = \\sqrt{dx^2 + ex + f}$: bình phương hai vế được $ax^2 + bx + c = dx^2 + ex + f$, giải tìm $x$ rồi thay lại vào phương trình ban đầu để thử nghiệm.\n"
            "- **Dạng 2**: $\\sqrt{ax^2 + bx + c} = dx + e$: bình phương hai vế được $ax^2 + bx + c = (dx + e)^2$, giải tìm $x$ rồi thử lại (hoặc kiểm tra điều kiện $dx + e \\ge 0$).\n"
            "### Bài tập cuối chương VI"
        ),
        "formulas": [
            G("I. Hàm số bậc hai & Parabol", F("Toạ độ đỉnh và trục đối xứng", "$I\\left(-\\dfrac{b}{2a}; -\\dfrac{\\Delta}{4a}\\right), \\quad \\text{trục đối xứng } x = -\\dfrac{b}{2a} \\quad (\\Delta = b^2 - 4ac)$"), F("Cực trị của hàm số bậc hai", "Nếu $a > 0 \\Rightarrow \\min_{\\mathbb{R}} y = -\\dfrac{\\Delta}{4a}$; nếu $a < 0 \\Rightarrow \\max_{\\mathbb{R}} y = -\\dfrac{\\Delta}{4a}$")),
            G("II. Dấu của tam thức bậc hai", F("Điều kiện luôn dương trên R", "$ax^2 + bx + c > 0, \\forall x \\in \\mathbb{R} \\iff \\begin{cases} a > 0 \\\\ \\Delta < 0 \\end{cases}$"), F("Điều kiện luôn âm trên R", "$ax^2 + bx + c < 0, \\forall x \\in \\mathbb{R} \\iff \\begin{cases} a < 0 \\\\ \\Delta < 0 \\end{cases}$")),
            G("III. Phương trình quy về bậc hai", F("Phương trình căn bằng căn", "$\\sqrt{A(x)} = \\sqrt{B(x)} \\iff \\begin{cases} B(x) \\ge 0 \\\\ A(x) = B(x) \\end{cases}$"), F("Phương trình căn bằng nhị thức", "$\\sqrt{A(x)} = B(x) \\iff \\begin{cases} B(x) \\ge 0 \\\\ A(x) = [B(x)]^2 \\end{cases}$")),
        ],
        "example": (
            "a) Tìm toạ độ đỉnh, trục đối xứng và khoảng đồng biến, nghịch biến của hàm số $y = x^2 - 4x + 3$.\n"
            "b) Giải bất phương trình $-x^2 + 5x - 4 > 0$ và phương trình $\\sqrt{2x^2 - 3x + 1} = x - 1$."
        ),
        "example_answer": (
            "a) Hàm số $y = x^2 - 4x + 3$ có $a = 1 > 0, b = -4, c = 3$.\n"
            "- Hoành độ đỉnh $x_I = -\\dfrac{-4}{2 \\cdot 1} = 2$, tung độ đỉnh $y_I = 2^2 - 4 \\cdot 2 + 3 = -1 \\Rightarrow$ Đỉnh $I(2; -1)$, trục đối xứng $x = 2$.\n"
            "- Vì $a = 1 > 0$ nên hàm số nghịch biến trên $(-\\infty; 2)$ và đồng biến trên $(2; +\\infty)$.\n"
            "b) Tam thức $f(x) = -x^2 + 5x - 4$ có $a = -1 < 0$ và hai nghiệm $x_1 = 1, x_2 = 4$, nên $f(x) > 0 \\Leftrightarrow x \\in (1; 4)$.\n"
            "Với phương trình $\\sqrt{2x^2 - 3x + 1} = x - 1$: điều kiện $x - 1 \\ge 0 \\Leftrightarrow x \\ge 1$. Bình phương hai vế: $2x^2 - 3x + 1 = (x - 1)^2 \\Leftrightarrow x^2 - x = 0 \\Leftrightarrow x = 0$ (loại) hoặc $x = 1$ (nhận). Vậy nghiệm là $x = 1$."
        ),
        "real_life": (
            "- Quỹ đạo của vật chuyển động ném xiên (quả bóng đá, tia nước đài phun), hình dạng dây cáp cầu treo và gương phản xạ ăng-ten parabol.\n"
            "- Tối ưu hoá giá bán sản phẩm để doanh thu hoặc lợi nhuận (là hàm bậc hai theo mức tăng giá) đạt giá trị lớn nhất."
        ),
        "quiz": [
            mcq("biet", "Tập xác định của hàm số $y = \\dfrac{x + 1}{x - 3}$ là:", ["$\\mathbb{R} \\setminus \\{3\\}$", "$\\mathbb{R} \\setminus \\{-1\\}$", "$(3; +\\infty)$", "$\\mathbb{R}$"], 0, "Biểu thức $\\dfrac{x + 1}{x - 3}$ xác định khi và chỉ khi mẫu thức $x - 3 \\ne 0 \\Leftrightarrow x \\ne 3$. Vậy tập xác định là $D = \\mathbb{R} \\setminus \\{3\\}$."),
            mcq("biet", "Đồ thị của hàm số bậc hai $y = ax^2 + bx + c \\; (a \\ne 0)$ là một đường parabol có trục đối xứng là đường thẳng:", ["$x = -\\dfrac{b}{2a}$", "$x = \\dfrac{b}{2a}$", "$x = -\\dfrac{b}{a}$", "$y = -\\dfrac{\\Delta}{4a}$"], 0, "Parabol $y = ax^2 + bx + c \\; (a \\ne 0)$ luôn nhận đường thẳng $x = -\\dfrac{b}{2a}$ làm trục đối xứng."),
            mcq("biet", "Biểu thức nào dưới đây là một tam thức bậc hai đối với biến $x$?", ["$f(x) = 2x^2 - 5x + 3$", "$f(x) = 3x - 7$", "$f(x) = x^3 - 2x^2 + 1$", "$f(x) = 0x^2 + 4x - 1$"], 0, "Tam thức bậc hai có dạng $ax^2 + bx + c$ với $a \\ne 0$, nên $f(x) = 2x^2 - 5x + 3$ (có $a = 2 \\ne 0$) là tam thức bậc hai."),
            mcq("biet", "Cho tam thức bậc hai $f(x) = ax^2 + bx + c \\; (a \\ne 0)$ có biệt thức $\\Delta = b^2 - 4ac < 0$. Khẳng định nào sau đây đúng?", ["$f(x)$ cùng dấu với hệ số $a$ với mọi $x \\in \\mathbb{R}$", "$f(x)$ trái dấu với hệ số $a$ với mọi $x \\in \\mathbb{R}$", "$f(x) = 0$ có hai nghiệm phân biệt", "$f(x)$ luôn dương với mọi $x \\in \\mathbb{R}$"], 0, "Theo định lí về dấu của tam thức bậc hai, khi $\\Delta < 0$ thì $f(x)$ luôn cùng dấu với hệ số $a$ với mọi $x \\in \\mathbb{R}$."),
            mcq("hieu", "Toạ độ đỉnh $I$ của parabol $(P): y = x^2 - 4x + 3$ là:", ["$I(2; -1)$", "$I(-2; 15)$", "$I(2; 1)$", "$I(4; 3)$"], 0, "Ta có $x_I = -\\dfrac{-4}{2 \\cdot 1} = 2$ và $y_I = 2^2 - 4 \\cdot 2 + 3 = -1$, suy ra đỉnh $I(2; -1)$."),
            mcq("hieu", "Tập nghiệm $S$ của bất phương trình $x^2 - 5x + 6 \\le 0$ là:", ["$S = [2; 3]$", "$S = (2; 3)$", "$S = (-\\infty; 2] \\cup [3; +\\infty)$", "$S = [-3; -2]$"], 0, "Tam thức $f(x) = x^2 - 5x + 6$ có $a = 1 > 0$ và hai nghiệm $x = 2, x = 3$. Theo quy tắc trong trái ngoài cùng, $f(x) \\le 0 \\Leftrightarrow x \\in [2; 3]$."),
            tf4("hieu", "Cho hàm số bậc hai $y = -x^2 + 4x - 3$ có đồ thị là parabol $(P)$. Xét tính đúng sai của các khẳng định sau:", ["a) Parabol $(P)$ có bề lõm quay xuống dưới và trục đối xứng là đường thẳng $x = 2$.", "b) Toạ độ đỉnh của parabol $(P)$ là $I(2; 1)$.", "c) Hàm số đồng biến trên khoảng $(-\\infty; 2)$ và nghịch biến trên khoảng $(2; +\\infty)$.", "d) Giá trị nhỏ nhất của hàm số trên tập số thực $\\mathbb{R}$ bằng $1$."], [True, True, True, False], "a) Đúng vì $a = -1 < 0$ và trục đối xứng là $x = -\\dfrac{4}{2(-1)} = 2$.\nb) Đúng vì tại $x = 2$, $y = -2^2 + 4 \\cdot 2 - 3 = 1 \\Rightarrow I(2; 1)$.\nc) Đúng vì $a = -1 < 0$ nên hàm số đồng biến trên $(-\\infty; 2)$ và nghịch biến trên $(2; +\\infty)$.\nd) Sai vì $a < 0$ nên $y = 1$ là giá trị lớn nhất của hàm số trên $\\mathbb{R}$, không phải giá trị nhỏ nhất."),
            tf4("hieu", "Cho tam thức bậc hai $f(x) = x^2 - 2mx + m + 2$ (với $m$ là tham số) và phương trình $\\sqrt{2x^2 - 3x + 1} = x - 1 \\; (*)$. Xét tính đúng sai của các khẳng định sau:", ["a) Khi $m = 2$, ta có $f(x) = (x - 2)^2 \\ge 0$ với mọi $x \\in \\mathbb{R}$.", "b) Biệt thức thu gọn của tam thức $f(x)$ là $\\Delta' = m^2 - m - 2$.", "c) Tam thức $f(x) > 0$ với mọi $x \\in \\mathbb{R}$ khi và chỉ khi $-1 < m < 2$.", "d) Phương trình $(*)$ có hai nghiệm phân biệt là $x = 0$ và $x = 1$."], [True, True, True, False], "a) Đúng vì khi $m = 2$, $f(x) = x^2 - 4x + 4 = (x - 2)^2 \\ge 0, \\forall x \\in \\mathbb{R}$.\nb) Đúng vì $\\Delta' = (-m)^2 - 1 \\cdot (m + 2) = m^2 - m - 2$.\nc) Đúng vì $a = 1 > 0$ nên $f(x) > 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\Delta' < 0 \\Leftrightarrow m^2 - m - 2 < 0 \\Leftrightarrow -1 < m < 2$.\nd) Sai vì với $x = 0$, vế phải của $(*)$ là $0 - 1 = -1 < 0$ nên $x = 0$ không là nghiệm; phương trình $(*)$ chỉ có nghiệm duy nhất $x = 1$."),
            mcq("vandung", "Một quả bóng được đá lên từ mặt đất, độ cao $h$ (tính bằng mét) của quả bóng so với mặt đất sau $t$ (giây) được cho bởi công thức $h(t) = -5t^2 + 20t$. Độ cao lớn nhất mà quả bóng đạt được là bao nhiêu mét?", ["$20\\text{ m}$", "$15\\text{ m}$", "$25\\text{ m}$", "$40\\text{ m}$"], 0, "Hàm số bậc hai $h(t) = -5t^2 + 20t$ có $a = -5 < 0$ đạt giá trị lớn nhất tại $t = -\\dfrac{20}{2 \\cdot (-5)} = 2$ (giây). Độ cao lớn nhất của quả bóng là $h(2) = -5 \\cdot 2^2 + 20 \\cdot 2 = 20\\text{ (m)}$."),
            short("vandung", "Tính tổng tất cả các nghiệm của phương trình $\\sqrt{x^2 - 3x + 6} = \\sqrt{x + 3}$.", ["4"], "Bình phương hai vế ta được $x^2 - 3x + 6 = x + 3 \\Leftrightarrow x^2 - 4x + 3 = 0 \\Leftrightarrow x = 1$ hoặc $x = 3$. Thay lại vào điều kiện $x + 3 \\ge 0$, cả hai giá trị $x = 1$ và $x = 3$ đều thoả mãn. Vậy tổng các nghiệm của phương trình là $1 + 3 = 4$."),
        ],
    },
    {
        "topic": "l10-ch07-phuong-phap-toa-do-trong-mat-phang",
        "title": "Phương pháp toạ độ trong mặt phẳng",
        "icon": "🎯",
        "description": "Chương VII · SGK Toán 10 tập hai: Bài 19 – Bài 22. Phương trình tham số và phương trình tổng quát của đường thẳng; vị trí tương đối giữa hai đường thẳng, góc và khoảng cách; phương trình đường tròn và phương trình tiếp tuyến của đường tròn; ba đường conic gồm elip, hypebol, parabol và ứng dụng.",
        "requirements": [
            "Mô tả được phương trình tổng quát và phương trình tham số của đường thẳng trong mặt phẳng toạ độ $Oxy$; lập được phương trình đường thẳng khi biết các yếu tố xác định.",
            "Nhận biết được hai đường thẳng cắt nhau, song song, trùng nhau, vuông góc với nhau và tính được góc giữa hai đường thẳng, khoảng cách từ một điểm đến một đường thẳng.",
            "Thiết lập được phương trình đường tròn khi biết tâm và bán kính hoặc biết ba điểm thuộc đường tròn; nhận biết được tâm, bán kính từ phương trình đường tròn và viết được phương trình tiếp tuyến của đường tròn tại một điểm.",
            "Nhận biết được ba đường conic (elip, hypebol, parabol) bằng hình học, nhận biết được phương trình chính tắc và các yếu tố cơ bản (tiêu điểm, tiêu cự, trục lớn, trục nhỏ, đường chuẩn) của chúng.",
            "Giải quyết được một số vấn đề thực tiễn gắn với đường thẳng, đường tròn và ba đường conic (ví dụ: tính toán cổng vòm elip, chảo parabol, hệ thống định vị hypebol).",
        ],
        "definition": (
            "- **Vectơ chỉ phương (VTCP)** $\\overrightarrow{u} \\ne \\overrightarrow{0}$ có giá song song hoặc trùng với đường thẳng $\\Delta$; **vectơ pháp tuyến (VTPT)** $\\overrightarrow{n} \\ne \\overrightarrow{0}$ có giá vuông góc với $\\Delta$. Nếu $\\overrightarrow{u} = (u_1; u_2)$ thì $\\overrightarrow{n} = (-u_2; u_1)$ hoặc $(u_2; -u_1)$.\n"
            "- **Phương trình đường tròn** tâm $I(a; b)$, bán kính $R$: $(x - a)^2 + (y - b)^2 = R^2$, hay dạng khai triển $x^2 + y^2 - 2ax - 2by + c = 0$ (với $a^2 + b^2 - c > 0, R = \\sqrt{a^2 + b^2 - c}$).\n"
            "- **Phương trình chính tắc của ba đường conic**: Elip $\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1 \\; (a > b > 0, c^2 = a^2 - b^2)$; Hypebol $\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1 \\; (a, b > 0, c^2 = a^2 + b^2)$; Parabol $y^2 = 2px \\; (p > 0)$."
        ),
        "theory": (
            "### Bài 19. Phương trình đường thẳng\n"
            "- **Phương trình tham số** của đường thẳng đi qua $M_0(x_0; y_0)$ và có VTCP $\\overrightarrow{u} = (u_1; u_2)$: $\\begin{cases} x = x_0 + u_1 t \\\\ y = y_0 + u_2 t \\end{cases} \\; (t \\in \\mathbb{R})$.\n"
            "- **Phương trình tổng quát** của đường thẳng đi qua $M_0(x_0; y_0)$ và có VTPT $\\overrightarrow{n} = (a; b)$: $a(x - x_0) + b(y - y_0) = 0 \\Leftrightarrow ax + by + c = 0 \\; (a^2 + b^2 > 0)$.\n"
            "### Bài 20. Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách\n"
            "- Vị trí tương đối của $\\Delta_1: a_1 x + b_1 y + c_1 = 0$ và $\\Delta_2: a_2 x + b_2 y + c_2 = 0$ được xác định qua số nghiệm của hệ hai phương trình.\n"
            "- **Góc giữa hai đường thẳng** ($0^\\circ \\le \\varphi \\le 90^\\circ$): $\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\overrightarrow{n_1} \\cdot \\overrightarrow{n_2}|}{|\\overrightarrow{n_1}| \\cdot |\\overrightarrow{n_2}|} = \\dfrac{|a_1 a_2 + b_1 b_2|}{\\sqrt{a_1^2 + b_1^2}\\sqrt{a_2^2 + b_2^2}}$.\n"
            "- **Khoảng cách từ điểm $M(x_0; y_0)$ đến $\\Delta: ax + by + c = 0$**: $d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$.\n"
            "### Bài 21. Đường tròn trong mặt phẳng toạ độ\n"
            "- Đường tròn $(C)$ tâm $I(a; b)$, bán kính $R$ có phương trình $(x - a)^2 + (y - b)^2 = R^2$.\n"
            "- **Phương trình tiếp tuyến** của đường tròn $(C)$ tại điểm $M_0(x_0; y_0) \\in (C)$ nhận $\\overrightarrow{IM_0} = (x_0 - a; y_0 - b)$ làm VTPT: $(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0$.\n"
            "### Bài 22. Ba đường conic\n"
            "- **Elip $(E): \\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1 \\; (a > b > 0)$**: $M \\in (E) \\Leftrightarrow MF_1 + MF_2 = 2a$; tiêu điểm $F_1(-c; 0), F_2(c; 0)$ với $c = \\sqrt{a^2 - b^2}$; trục lớn $2a$, trục nhỏ $2b$, tiêu cự $2c$.\n"
            "- **Hypebol $(H): \\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1 \\; (a, b > 0)$**: $M \\in (H) \\Leftrightarrow |MF_1 - MF_2| = 2a$; tiêu điểm $F_1(-c; 0), F_2(c; 0)$ với $c = \\sqrt{a^2 + b^2}$; trục thực $2a$, trục ảo $2b$, tiêu cự $2c$.\n"
            "- **Parabol $(P): y^2 = 2px \\; (p > 0)$**: $M \\in (P) \\Leftrightarrow MF = d(M, \\Delta)$; tiêu điểm $F\\left(\\dfrac{p}{2}; 0\\right)$, đường chuẩn $\\Delta: x = -\\dfrac{p}{2}$, tham số tiêu $p = d(F, \\Delta)$.\n"
            "### Bài tập cuối chương VII"
        ),
        "formulas": [
            G("I. Đường thẳng trong mặt phẳng Oxy", F("Phương trình tham số và tổng quát", "$\\begin{cases} x = x_0 + u_1 t \\\\ y = y_0 + u_2 t \\end{cases}, \\quad a(x - x_0) + b(y - y_0) = 0$"), F("Góc giữa hai đường thẳng", "$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1 a_2 + b_1 b_2|}{\\sqrt{a_1^2 + b_1^2}\\sqrt{a_2^2 + b_2^2}}$"), F("Khoảng cách từ M(x0; y0) đến đường thẳng", "$d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$")),
            G("II. Đường tròn & Tiếp tuyến", F("Phương trình đường tròn tâm I(a; b), bán kính R", "$(x - a)^2 + (y - b)^2 = R^2$"), F("Bán kính từ dạng khai triển", "$x^2 + y^2 - 2ax - 2by + c = 0 \\Rightarrow I(a; b), \\; R = \\sqrt{a^2 + b^2 - c}$"), F("Tiếp tuyến tại M0(x0; y0) thuộc (C)", "$(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0$")),
            G("III. Phương trình chính tắc ba đường conic", F("Elip (a > b > 0)", "$\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1, \\quad c^2 = a^2 - b^2, \\quad MF_1 + MF_2 = 2a$"), F("Hypebol (a, b > 0)", "$\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1, \\quad c^2 = a^2 + b^2, \\quad |MF_1 - MF_2| = 2a$"), F("Parabol (p > 0)", "$y^2 = 2px, \\quad F\\left(\\dfrac{p}{2}; 0\\right), \\quad \\Delta: x = -\\dfrac{p}{2}$")),
        ],
        "example": (
            "a) Trong mặt phẳng $Oxy$, viết phương trình đường tròn $(C)$ có tâm $I(1; -2)$ và tiếp xúc với đường thẳng $\\Delta: 3x - 4y + 4 = 0$.\n"
            "b) Cho elip $(E): \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1$. Tìm độ dài trục lớn, trục nhỏ, tiêu cự và toạ độ các tiêu điểm của $(E)$."
        ),
        "example_answer": (
            "a) Vì đường tròn $(C)$ tâm $I(1; -2)$ tiếp xúc với $\\Delta$ nên bán kính $R$ bằng khoảng cách từ $I$ đến $\\Delta$:\n"
            "$R = d(I, \\Delta) = \\dfrac{|3 \\cdot 1 - 4 \\cdot (-2) + 4|}{\\sqrt{3^2 + (-4)^2}} = \\dfrac{15}{5} = 3$.\n"
            "Phương trình đường tròn $(C)$ là $(x - 1)^2 + (y + 2)^2 = 9$.\n"
            "b) Từ phương trình $(E)$ ta có $a^2 = 25 \\Rightarrow a = 5$; $b^2 = 9 \\Rightarrow b = 3$; $c = \\sqrt{a^2 - b^2} = \\sqrt{25 - 9} = 4$.\n"
            "Vậy $(E)$ có độ dài trục lớn $2a = 10$, độ dài trục nhỏ $2b = 6$, tiêu cự $2c = 8$ và hai tiêu điểm $F_1(-4; 0), F_2(4; 0)$."
        ),
        "real_life": (
            "- Quỹ đạo các hành tinh chuyển động quanh Mặt Trời theo đường elip (Định luật I Kepler), bàn bi-a elip và phòng thì thầm.\n"
            "- Tháp làm mát nhà máy nhiệt điện có hình dạng hypebol, hệ thống định vị vô tuyến LORAN và gương pha đèn ô tô dạng parabol."
        ),
        "quiz": [
            mcq("biet", "Trong mặt phẳng toạ độ $Oxy$, đường thẳng $\\Delta: 3x - 4y + 5 = 0$ có một vectơ pháp tuyến là:", ["$\\overrightarrow{n} = (3; -4)$", "$\\overrightarrow{n} = (4; 3)$", "$\\overrightarrow{n} = (3; 4)$", "$\\overrightarrow{n} = (-4; 3)$"], 0, "Đường thẳng $ax + by + c = 0$ nhận $\\overrightarrow{n} = (a; b)$ làm một vectơ pháp tuyến, nên $\\Delta$ có VTPT $\\overrightarrow{n} = (3; -4)$."),
            mcq("biet", "Trong mặt phẳng toạ độ $Oxy$, khoảng cách từ điểm $M(x_0; y_0)$ đến đường thẳng $\\Delta: ax + by + c = 0 \\; (a^2 + b^2 > 0)$ được tính bởi công thức:", ["$d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$", "$d(M, \\Delta) = \\dfrac{ax_0 + by_0 + c}{\\sqrt{a^2 + b^2}}$", "$d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{a^2 + b^2}$", "$d(M, \\Delta) = \\dfrac{|ax_0 + by_0|}{\\sqrt{a^2 + b^2}}$"], 0, "Công thức tính khoảng cách từ điểm $M(x_0; y_0)$ đến đường thẳng $\\Delta: ax + by + c = 0$ là $d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$."),
            mcq("biet", "Đường tròn $(C): (x - 2)^2 + (y + 3)^2 = 16$ có tâm $I$ và bán kính $R$ lần lượt là:", ["$I(2; -3)$ và $R = 4$", "$I(-2; 3)$ và $R = 4$", "$I(2; -3)$ và $R = 16$", "$I(-2; 3)$ và $R = 16$"], 0, "So sánh với dạng $(x - a)^2 + (y - b)^2 = R^2$, ta có tâm $I(2; -3)$ và bán kính $R = \\sqrt{16} = 4$."),
            mcq("biet", "Phương trình chính tắc của elip $(E)$ có độ dài trục lớn $2a$ và độ dài trục nhỏ $2b \\; (a > b > 0)$ là:", ["$\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$", "$\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$", "$\\dfrac{x^2}{b^2} + \\dfrac{y^2}{a^2} = 1$", "$y^2 = 2px$"], 0, "Phương trình chính tắc của elip có dạng $\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$ với $a > b > 0$."),
            mcq("hieu", "Khoảng cách từ điểm $M(1; -2)$ đến đường thẳng $\\Delta: 3x - 4y - 1 = 0$ bằng:", ["$2$", "$10$", "$\\dfrac{6}{5}$", "$4$"], 0, "Áp dụng công thức khoảng cách: $d(M, \\Delta) = \\dfrac{|3 \\cdot 1 - 4 \\cdot (-2) - 1|}{\\sqrt{3^2 + (-4)^2}} = \\dfrac{10}{5} = 2$."),
            mcq("hieu", "Cho đường tròn $(C): x^2 + y^2 - 4x + 6y - 12 = 0$. Bán kính $R$ của đường tròn $(C)$ bằng:", ["$5$", "$25$", "$1$", "$\\sqrt{13}$"], 0, "Từ phương trình $(C)$ suy ra $a = 2, b = -3, c = -12$. Bán kính là $R = \\sqrt{a^2 + b^2 - c} = \\sqrt{2^2 + (-3)^2 - (-12)} = \\sqrt{25} = 5$."),
            tf4("hieu", "Trong mặt phẳng toạ độ $Oxy$, cho hai đường thẳng $\\Delta_1: x - 2y + 3 = 0$ và $\\Delta_2: 2x + y - 4 = 0$. Xét tính đúng sai của các khẳng định sau:", ["a) Đường thẳng $\\Delta_1$ có một vectơ pháp tuyến là $\\overrightarrow{n_1} = (1; -2)$ và một vectơ chỉ phương là $\\overrightarrow{u_1} = (2; 1)$.", "b) Hai đường thẳng $\\Delta_1$ và $\\Delta_2$ vuông góc với nhau.", "c) Giao điểm của hai đường thẳng $\\Delta_1$ và $\\Delta_2$ là điểm $A(1; 2)$.", "d) Khoảng cách từ gốc toạ độ $O(0; 0)$ đến đường thẳng $\\Delta_2$ bằng $4$."], [True, True, True, False], "a) Đúng vì $\\Delta_1$ có VTPT $\\overrightarrow{n_1} = (1; -2)$ nên VTCP là $\\overrightarrow{u_1} = (2; 1)$.\nb) Đúng vì $\\overrightarrow{n_1} \\cdot \\overrightarrow{n_2} = 1 \\cdot 2 + (-2) \\cdot 1 = 0$.\nc) Đúng vì nghiệm của hệ $\\begin{cases} x - 2y = -3 \\\\ 2x + y = 4 \\end{cases}$ là $(1; 2)$.\nd) Sai vì $d(O, \\Delta_2) = \\dfrac{|-4|}{\\sqrt{2^2 + 1^2}} = \\dfrac{4\\sqrt{5}}{5} \\ne 4$."),
            tf4("hieu", "Trong mặt phẳng toạ độ $Oxy$, cho đường tròn $(C): (x - 1)^2 + (y - 2)^2 = 25$ và elip $(E): \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1$. Xét tính đúng sai của các khẳng định sau:", ["a) Đường tròn $(C)$ có tâm $I(1; 2)$ và bán kính $R = 5$.", "b) Điểm $M(4; 6)$ nằm trên đường tròn $(C)$ và tiếp tuyến của $(C)$ tại $M$ có phương trình $3x + 4y - 36 = 0$.", "c) Elip $(E)$ có độ dài trục lớn bằng $10$ và độ dài trục nhỏ bằng $6$.", "d) Tiêu cự của elip $(E)$ bằng $4$."], [True, True, True, False], "a) Đúng theo phương trình chính tắc của đường tròn $(C)$.\nb) Đúng vì $(4 - 1)^2 + (6 - 2)^2 = 25$ và tiếp tuyến tại $M(4; 6)$ là $3(x - 4) + 4(y - 6) = 0 \\Leftrightarrow 3x + 4y - 36 = 0$.\nc) Đúng vì $a = 5 \\Rightarrow 2a = 10$ và $b = 3 \\Rightarrow 2b = 6$.\nd) Sai vì $c = \\sqrt{a^2 - b^2} = \\sqrt{25 - 9} = 4$ nên tiêu cự của $(E)$ là $2c = 8 \\ne 4$."),
            mcq("vandung", "Một cổng vòm có hình dạng là một nửa elip với chiều rộng chân cổng (độ dài trục lớn) là $10\\text{ m}$ và chiều cao tại điểm chính giữa cổng (nửa trục nhỏ) là $4\\text{ m}$. Tại vị trí cách điểm chính giữa chân cổng $3\\text{ m}$, chiều cao của cổng vòm bằng bao nhiêu mét?", ["$3,2\\text{ m}$", "$3,5\\text{ m}$", "$2,8\\text{ m}$", "$3,6\\text{ m}$"], 0, "Chọn hệ trục $Oxy$ với gốc $O$ là trung điểm chân cổng, ta có $a = 5, b = 4$ nên phương trình elip là $\\dfrac{x^2}{25} + \\dfrac{y^2}{16} = 1 \\; (y \\ge 0)$. Tại $x = 3$: $\\dfrac{3^2}{25} + \\dfrac{y^2}{16} = 1 \\Rightarrow \\dfrac{y^2}{16} = \\dfrac{16}{25} \\Rightarrow y = \\dfrac{16}{5} = 3,2\\text{ (m)}$."),
            short("vandung", "Trong mặt phẳng toạ độ $Oxy$, cho parabol $(P)$ có phương trình chính tắc $y^2 = 12x$. Tính khoảng cách từ tiêu điểm $F$ đến đường chuẩn $\\Delta$ của parabol $(P)$.", ["6"], "So sánh phương trình $y^2 = 12x$ với dạng chính tắc $y^2 = 2px$, ta có $2p = 12 \\Rightarrow p = 6$. Khoảng cách từ tiêu điểm $F\\left(\\dfrac{p}{2}; 0\\right)$ đến đường chuẩn $\\Delta: x = -\\dfrac{p}{2}$ chính bằng tham số tiêu $p = 6$."),
        ],
    },
    {
        "topic": "l10-ch08-dai-so-to-hop",
        "title": "Đại số tổ hợp",
        "icon": "🎲",
        "description": "Chương VIII · SGK Toán 10 tập hai: Bài 23 – Bài 25. Quy tắc cộng, quy tắc nhân và sơ đồ hình cây; hoán vị, chỉnh hợp, tổ hợp và ứng dụng trong các bài toán đếm; công thức nhị thức Newton với số mũ 4 và số mũ 5 cùng tam giác Pascal.",
        "requirements": [
            "Vận dụng được quy tắc cộng và quy tắc nhân trong một số tình huống đơn giản (ví dụ: đếm số khả năng xuất hiện trong một số thí nghiệm, đếm số cách lập số tự nhiên) và biết dùng sơ đồ hình cây.",
            "Nhận biết được khái niệm hoán vị $P_n$, chỉnh hợp $A_n^k$, tổ hợp $C_n^k$; tính được số các hoán vị, chỉnh hợp, tổ hợp bằng công thức và bằng máy tính cầm tay.",
            "Vận dụng được hoán vị, chỉnh hợp, tổ hợp vào giải các bài toán đếm trong toán học và thực tiễn.",
            "Khai triển được nhị thức Newton $(a + b)^n$ với số mũ thấp ($n = 4$ hoặc $n = 5$) bằng cách vận dụng tổ hợp.",
        ],
        "definition": (
            "- **Quy tắc cộng**: Công việc thực hiện bởi một trong hai phương án độc lập ($m$ cách hoặc $n$ cách) có $m + n$ cách. **Quy tắc nhân**: Công việc thực hiện qua hai công đoạn liên tiếp ($m$ cách rồi $n$ cách) có $m \\cdot n$ cách.\n"
            "- **Hoán vị ($P_n$)**: Sắp xếp thứ tự $n$ phần tử ($n \\ge 1$), số hoán vị là $P_n = n! = 1 \\cdot 2 \\cdots n$ (quy ước $0! = 1$).\n"
            "- **Chỉnh hợp ($A_n^k$)**: Chọn $k$ phần tử từ $n$ phần tử **có phân biệt thứ tự**, $A_n^k = \\dfrac{n!}{(n - k)!}$. **Tổ hợp ($C_n^k$)**: Chọn $k$ phần tử từ $n$ phần tử **không phân biệt thứ tự**, $C_n^k = \\dfrac{n!}{k!(n - k)!}$.\n"
            "- **Nhị thức Newton**: $(a + b)^n = C_n^0 a^n + C_n^1 a^{n-1}b + \\dots + C_n^k a^{n-k}b^k + \\dots + C_n^n b^n$."
        ),
        "theory": (
            "### Bài 23. Quy tắc đếm\n"
            "- **Quy tắc cộng**: Áp dụng khi chia bài toán thành các trường hợp rời nhau (mỗi trường hợp tự nó đã hoàn thành công việc).\n"
            "- **Quy tắc nhân**: Áp dụng khi chia công việc thành các bước (công đoạn) liên tiếp nhau; có thể minh hoạ trực quan bằng **sơ đồ hình cây**.\n"
            "### Bài 24. Hoán vị, chỉnh hợp và tổ hợp\n"
            "- **Hoán vị**: $P_n = n! = n(n - 1)\\cdots 2 \\cdot 1$.\n"
            "- **Chỉnh hợp chập $k$ của $n$ phần tử** ($1 \\le k \\le n$): $A_n^k = n(n - 1)\\cdots(n - k + 1) = \\dfrac{n!}{(n - k)!}$.\n"
            "- **Tổ hợp chập $k$ của $n$ phần tử** ($0 \\le k \\le n$): $C_n^k = \\dfrac{A_n^k}{k!} = \\dfrac{n!}{k!(n - k)!}$. Các tính chất cơ bản: $C_n^k = C_n^{n-k}$ và $C_n^{k-1} + C_n^k = C_{n+1}^k$.\n"
            "- **Phân biệt nhanh**: Có sắp thứ tự $\\rightarrow$ dùng chỉnh hợp $A_n^k$ (hoặc hoán vị $P_n$ khi $k = n$); chỉ chọn tập con không sắp thứ tự $\\rightarrow$ dùng tổ hợp $C_n^k$.\n"
            "### Bài 25. Nhị thức Newton\n"
            "- Khai triển bậc $4$: $(a + b)^4 = C_4^0 a^4 + C_4^1 a^3 b + C_4^2 a^2 b^2 + C_4^3 a b^3 + C_4^4 b^4 = a^4 + 4a^3 b + 6a^2 b^2 + 4a b^3 + b^4$.\n"
            "- Khai triển bậc $5$: $(a + b)^5 = C_5^0 a^5 + C_5^1 a^4 b + C_5^2 a^3 b^2 + C_5^3 a^2 b^3 + C_5^4 a b^4 + C_5^5 b^5 = a^5 + 5a^4 b + 10a^3 b^2 + 10a^2 b^3 + 5a b^4 + b^5$.\n"
            "- Số hạng tổng quát thứ $k + 1$ trong khai triển $(a + b)^n$ là $T_{k+1} = C_n^k a^{n-k} b^k \\; (0 \\le k \\le n)$, gồm $n + 1$ số hạng.\n"
            "### Bài tập cuối chương VIII"
        ),
        "formulas": [
            G("I. Hai quy tắc đếm cơ bản", F("Quy tắc cộng (k phương án rời nhau)", "$N = n_1 + n_2 + \\dots + n_k$"), F("Quy tắc nhân (k công đoạn liên tiếp)", "$N = n_1 \\cdot n_2 \\cdots n_k$")),
            G("II. Hoán vị, Chỉnh hợp & Tổ hợp", F("Hoán vị của n phần tử", "$P_n = n! = 1 \\cdot 2 \\cdots n \\quad (0! = 1)$"), F("Chỉnh hợp chập k của n phần tử", "$A_n^k = \\dfrac{n!}{(n - k)!} = n(n - 1)\\cdots(n - k + 1) \\quad (1 \\le k \\le n)$"), F("Tổ hợp chập k của n phần tử", "$C_n^k = \\dfrac{n!}{k!(n - k)!}, \\quad C_n^k = C_n^{n-k}, \\quad C_n^{k-1} + C_n^k = C_{n+1}^k$")),
            G("III. Công thức nhị thức Newton", F("Khai triển bậc 4", "$(a + b)^4 = a^4 + 4a^3 b + 6a^2 b^2 + 4ab^3 + b^4$"), F("Khai triển bậc 5", "$(a + b)^5 = a^5 + 5a^4 b + 10a^3 b^2 + 10a^2 b^3 + 5ab^4 + b^5$"), F("Số hạng tổng quát", "$T_{k+1} = C_n^k a^{n-k} b^k \\quad (0 \\le k \\le n)$")),
        ],
        "example": (
            "a) Một lớp có $20$ học sinh nam và $15$ học sinh nữ. Có bao nhiêu cách chọn một ban cán sự gồm $1$ lớp trưởng, $1$ lớp phó học tập và $1$ bí thư? Có bao nhiêu cách chọn một đội tình nguyện gồm $4$ học sinh có cả nam và nữ?\n"
            "b) Tìm hệ số của $x^3$ trong khai triển nhị thức $(2x - 3)^5$."
        ),
        "example_answer": (
            "a) Lớp có $35$ học sinh:\n"
            "- Chọn $3$ học sinh giữ $3$ chức vụ khác nhau (có phân biệt thứ tự) có $A_{35}^3 = 35 \\cdot 34 \\cdot 33 = 39\\,270$ cách.\n"
            "- Số cách chọn $4$ học sinh bất kì là $C_{35}^4 = 52\\,360$; số cách chọn $4$ nam là $C_{20}^4 = 4\\,845$; số cách chọn $4$ nữ là $C_{15}^4 = 1\\,365$. Vậy số cách chọn $4$ học sinh có cả nam và nữ là $52\\,360 - 4\\,845 - 1\\,365 = 46\\,150$ cách.\n"
            "b) Số hạng tổng quát trong khai triển $(2x - 3)^5$ là $T_{k+1} = C_5^k (2x)^{5-k} (-3)^k = C_5^k \\cdot 2^{5-k} \\cdot (-3)^k \\cdot x^{5-k}$.\n"
            "Số hạng chứa $x^3$ ứng với $5 - k = 3 \\Leftrightarrow k = 2$. Hệ số của $x^3$ là $C_5^2 \\cdot 2^3 \\cdot (-3)^2 = 10 \\cdot 8 \\cdot 9 = 720$."
        ),
        "real_life": (
            "- Tính số lượng mật khẩu bảo mật, biển số xe cơ giới, mã vạch hàng hoá và địa chỉ mạng IP.\n"
            "- Lập lịch thi đấu thể thao vòng tròn ($C_n^2$ trận đấu) và tính xác suất di truyền các alen trong Sinh học."
        ),
        "quiz": [
            mcq("biet", "Một công việc được hoàn thành bởi một trong hai hành động: hành động thứ nhất có $m$ cách thực hiện, hành động thứ hai có $n$ cách thực hiện (không trùng với bất kì cách nào của hành động thứ nhất). Theo quy tắc cộng, số cách hoàn thành công việc đó là:", ["$m + n$", "$m \\cdot n$", "$m^n$", "$m - n$"], 0, "Theo quy tắc cộng, khi công việc được chia thành hai phương án độc lập không giao nhau thì tổng số cách hoàn thành là $m + n$."),
            mcq("biet", "Số các hoán vị của một tập hợp có $n$ phần tử ($n \\ge 1$) được tính bởi công thức nào?", ["$P_n = n!$", "$P_n = n^2$", "$P_n = \\dfrac{n(n - 1)}{2}$", "$P_n = (n - 1)!$"], 0, "Số các hoán vị của tập hợp gồm $n$ phần tử ($n \\ge 1$) là $P_n = n! = 1 \\cdot 2 \\cdots n$."),
            mcq("biet", "Với $k, n$ là các số nguyên dương thoả mãn $1 \\le k \\le n$, công thức tính số tổ hợp chập $k$ của $n$ phần tử là:", ["$C_n^k = \\dfrac{n!}{k!(n - k)!}$", "$C_n^k = \\dfrac{n!}{(n - k)!}$", "$C_n^k = \\dfrac{k!}{n!(n - k)!}$", "$C_n^k = \\dfrac{(n - k)!}{n! k!}$"], 0, "Theo định nghĩa, số tổ hợp chập $k$ của $n$ phần tử là $C_n^k = \\dfrac{n!}{k!(n - k)!}$."),
            mcq("biet", "Khai triển nhị thức Newton của biểu thức $(a + b)^4$ có tất cả bao nhiêu số hạng?", ["$5$", "$4$", "$6$", "$8$"], 0, "Khai triển nhị thức Newton của $(a + b)^n$ có $n + 1$ số hạng, nên với $n = 4$ có $4 + 1 = 5$ số hạng."),
            mcq("hieu", "Từ các chữ số $1; 2; 3; 4; 5; 6$ có thể lập được bao nhiêu số tự nhiên gồm $3$ chữ số đôi một khác nhau?", ["$120$", "$216$", "$20$", "$18$"], 0, "Mỗi số tự nhiên gồm $3$ chữ số đôi một khác nhau lập từ $6$ chữ số đã cho là một chỉnh hợp chập $3$ của $6$ phần tử, nên có $A_6^3 = 6 \\cdot 5 \\cdot 4 = 120$ (số)."),
            mcq("hieu", "Hệ số của $x^3$ trong khai triển nhị thức Newton của $(x + 2)^4$ là:", ["$8$", "$4$", "$6$", "$24$"], 0, "Ta có $(x + 2)^4 = C_4^0 x^4 + C_4^1 x^3 \\cdot 2^1 + C_4^2 x^2 \\cdot 2^2 + C_4^3 x \\cdot 2^3 + C_4^4 \\cdot 2^4$, nên hệ số của $x^3$ là $C_4^1 \\cdot 2 = 4 \\cdot 2 = 8$."),
            tf4("hieu", "Một tổ học sinh có $6$ học sinh nam và $4$ học sinh nữ. Xét tính đúng sai của các khẳng định sau:", ["a) Số cách chọn ra $1$ học sinh bất kì của tổ để làm trực nhật là $10$ cách.", "b) Số cách chọn ra $1$ học sinh nam và $1$ học sinh nữ để tham gia đôi song ca là $24$ cách.", "c) Số cách xếp cả $10$ học sinh của tổ thành một hàng dọc là $10!$ cách.", "d) Số cách chọn ra một nhóm gồm $3$ học sinh bất kì trong tổ là $A_{10}^3 = 720$ cách."], [True, True, True, False], "a) Đúng theo quy tắc cộng: $6 + 4 = 10$ (cách).\nb) Đúng theo quy tắc nhân: $6 \\cdot 4 = 24$ (cách).\nc) Đúng vì xếp $10$ học sinh vào $10$ vị trí theo hàng dọc là hoán vị $P_{10} = 10!$ (cách).\nd) Sai vì chọn một nhóm $3$ học sinh không phân biệt thứ tự là tổ hợp $C_{10}^3 = 120$ cách, không phải chỉnh hợp $A_{10}^3$."),
            tf4("hieu", "Cho nhị thức $(2x - 1)^5$. Xét tính đúng sai của các khẳng định sau:", ["a) Khai triển của nhị thức có tất cả $6$ số hạng.", "b) Số hạng chứa $x^5$ trong khai triển là $32x^5$.", "c) Hệ số của $x^3$ trong khai triển là $80$.", "d) Tổng tất cả các hệ số trong khai triển đa thức của $(2x - 1)^5$ bằng $32$."], [True, True, True, False], "a) Đúng vì bậc $n = 5$ nên khai triển có $5 + 1 = 6$ số hạng.\nb) Đúng vì số hạng đầu là $C_5^0 (2x)^5 (-1)^0 = 32x^5$.\nc) Đúng vì số hạng chứa $x^3$ ứng với $k = 2$: $C_5^2 (2x)^3 (-1)^2 = 10 \\cdot 8x^3 \\cdot 1 = 80x^3$.\nd) Sai vì thay $x = 1$ vào $(2x - 1)^5$, tổng tất cả các hệ số của đa thức bằng $(2 \\cdot 1 - 1)^5 = 1^5 = 1 \\ne 32$."),
            mcq("vandung", "Một hộp có $5$ viên bi đỏ và $4$ viên bi xanh đôi một khác nhau. Có bao nhiêu cách lấy ra $3$ viên bi từ hộp sao cho trong $3$ viên bi lấy ra có ít nhất $1$ viên bi đỏ?", ["$80$", "$84$", "$74$", "$60$"], 0, "Số cách chọn $3$ viên bi bất kì từ $9$ viên bi là $C_9^3 = 84$. Số cách chọn $3$ viên bi toàn màu xanh (không có bi đỏ nào) là $C_4^3 = 4$. Vậy số cách chọn có ít nhất $1$ viên bi đỏ là $84 - 4 = 80$ (cách)."),
            short("vandung", "Tìm hệ số của $x^2$ trong khai triển nhị thức Newton của $(3x - 2)^4$.", ["216"], "Số hạng tổng quát trong khai triển $(3x - 2)^4$ là $T_{k+1} = C_4^k (3x)^{4-k} (-2)^k$. Số hạng chứa $x^2$ ứng với $4 - k = 2 \\Leftrightarrow k = 2$, khi đó hệ số của $x^2$ là $C_4^2 \\cdot 3^2 \\cdot (-2)^2 = 6 \\cdot 9 \\cdot 4 = 216$."),
        ],
    },
    {
        "topic": "l10-ch09-tinh-xac-suat-theo-dinh-nghia-co-dien",
        "title": "Tính xác suất theo định nghĩa cổ điển",
        "icon": "🎯",
        "description": "Chương IX · SGK Toán 10 tập hai: Bài 26 – Bài 27. Phép thử ngẫu nhiên, không gian mẫu, biến cố, biến cố đối và định nghĩa cổ điển của xác suất; thực hành tính xác suất theo định nghĩa cổ điển bằng phương pháp tổ hợp, sơ đồ hình cây và quy tắc tính xác suất của biến cố đối.",
        "requirements": [
            "Nhận biết được một số khái niệm về xác suất cổ điển: phép thử ngẫu nhiên, không gian mẫu $\\Omega$, biến cố (là tập con của không gian mẫu), biến cố chắc chắn, biến cố không thể và biến cố đối $\\overline{A}$.",
            "Mô tả được định nghĩa cổ điển của xác suất $P(A) = \\dfrac{n(A)}{n(\\Omega)}$ và các tính chất cơ bản của xác suất ($0 \\le P(A) \\le 1$, $P(\\Omega) = 1$, $P(\\varnothing) = 0$).",
            "Tính được xác suất của biến cố trong một số bài toán đơn giản bằng phương pháp tổ hợp và bằng cách sử dụng sơ đồ hình cây.",
            "Tính được xác suất trong một số bài toán có sử dụng công thức xác suất của biến cố đối $P(\\overline{A}) = 1 - P(A)$.",
        ],
        "definition": (
            "- **Phép thử ngẫu nhiên** là phép thử mà ta không đoán trước được kết quả của nó, tuy nhiên có thể xác định được tập hợp tất cả các kết quả có thể xảy ra, gọi là **không gian mẫu** $\\Omega$.\n"
            "- **Biến cố** $A$ là một tập con của không gian mẫu ($A \\subset \\Omega$); $\\varnothing$ là biến cố không thể, $\\Omega$ là biến cố chắc chắn, và $\\overline{A} = \\Omega \\setminus A$ là **biến cố đối** của biến cố $A$.\n"
            "- **Định nghĩa cổ điển của xác suất**: Khi mọi kết quả của $\\Omega$ đều đồng khả năng, xác suất của biến cố $A$ là $P(A) = \\dfrac{n(A)}{n(\\Omega)}$, trong đó $n(A)$ là số kết quả thuận lợi cho $A$ và $n(\\Omega)$ là số phần tử của không gian mẫu."
        ),
        "theory": (
            "### Bài 26. Biến cố và định nghĩa cổ điển của xác suất\n"
            "- Với mỗi biến cố $A \\subset \\Omega$, xác suất cổ điển là $P(A) = \\dfrac{n(A)}{n(\\Omega)}$.\n"
            "- **Tính chất cơ bản của xác suất**: $P(\\varnothing) = 0$; $P(\\Omega) = 1$; $0 \\le P(A) \\le 1$ với mọi biến cố $A$. Nếu $A$ và $B$ xung khắc ($A \\cap B = \\varnothing$) thì $P(A \\cup B) = P(A) + P(B)$.\n"
            "### Bài 27. Thực hành tính xác suất theo định nghĩa cổ điển\n"
            "- **Sử dụng phương pháp tổ hợp**: Dùng quy tắc cộng, quy tắc nhân, hoán vị $P_n$, chỉnh hợp $A_n^k$ và tổ hợp $C_n^k$ để đếm $n(\\Omega)$ và $n(A)$.\n"
            "- **Sử dụng sơ đồ hình cây**: Liệt kê trực quan tất cả các kết quả của phép thử gồm nhiều bước liên tiếp để đếm chính xác $n(\\Omega)$ và $n(A)$.\n"
            "- **Xác suất của biến cố đối**: Vì $n(A) + n(\\overline{A}) = n(\\Omega)$ nên $P(\\overline{A}) = 1 - P(A)$ (rất hiệu quả khi biến cố $A$ có từ khoá “ít nhất một”, “không đều cùng màu”, v.v.).\n"
            "### Bài tập cuối chương IX"
        ),
        "formulas": [
            G("I. Định nghĩa cổ điển của xác suất", F("Công thức xác suất cổ điển", "$P(A) = \\dfrac{n(A)}{n(\\Omega)}$"), F("Tập giá trị của xác suất", "$0 \\le P(A) \\le 1, \\quad P(\\varnothing) = 0, \\quad P(\\Omega) = 1$")),
            G("II. Biến cố đối & Biến cố xung khắc", F("Biến cố đối", "$\\overline{A} = \\Omega \\setminus A, \\quad n(\\overline{A}) = n(\\Omega) - n(A)$"), F("Công thức xác suất biến cố đối", "$P(\\overline{A}) = 1 - P(A) \\iff P(A) = 1 - P(\\overline{A})$"), F("Hai biến cố xung khắc (A giao B rỗng)", "$P(A \\cup B) = P(A) + P(B) \\quad (A \\cap B = \\varnothing)$")),
        ],
        "example": (
            "Một chiếc hộp đựng $5$ viên bi trắng và $4$ viên bi đỏ có cùng kích thước và khối lượng. Lấy ngẫu nhiên đồng thời $3$ viên bi từ hộp.\n"
            "a) Tính xác suất của biến cố $A$: “Ba viên bi lấy ra có đúng $2$ viên bi trắng và $1$ viên bi đỏ”.\n"
            "b) Tính xác suất của biến cố $B$: “Trong ba viên bi lấy ra có ít nhất $1$ viên bi đỏ”."
        ),
        "example_answer": (
            "Số phần tử của không gian mẫu là số cách chọn $3$ viên bi từ $9$ viên bi: $n(\\Omega) = C_9^3 = 84$.\n"
            "a) Số kết quả thuận lợi cho biến cố $A$ là $n(A) = C_5^2 \\cdot C_4^1 = 10 \\cdot 4 = 40$.\n"
            "Xác suất của biến cố $A$ là $P(A) = \\dfrac{40}{84} = \\dfrac{10}{21}$.\n"
            "b) Biến cố đối của $B$ là $\\overline{B}$: “Cả ba viên bi lấy ra đều là bi trắng”, có $n(\\overline{B}) = C_5^3 = 10$.\n"
            "Do đó $P(B) = 1 - P(\\overline{B}) = 1 - \\dfrac{10}{84} = \\dfrac{74}{84} = \\dfrac{37}{42}$."
        ),
        "real_life": (
            "- Kiểm định chất lượng lô hàng công nghiệp thông qua xác suất lấy mẫu ngẫu nhiên không có phế phẩm.\n"
            "- Đánh giá rủi ro trong bảo hiểm, tài chính, dự báo thời tiết và phân tích xác suất thắng thua trong các trò chơi may rủi."
        ),
        "quiz": [
            mcq("biet", "Trong một phép thử ngẫu nhiên, tập hợp tất cả các kết quả có thể xảy ra của phép thử được gọi là gì?", ["Không gian mẫu $\\Omega$", "Biến cố chắc chắn", "Biến cố đối $\\overline{A}$", "Biến cố sơ cấp"], 0, "Theo định nghĩa, tập hợp tất cả các kết quả có thể xảy ra của một phép thử ngẫu nhiên được gọi là không gian mẫu, kí hiệu là $\\Omega$."),
            mcq("biet", "Nếu một phép thử có không gian mẫu $\\Omega$ gồm hữu hạn các kết quả đồng khả năng và $A$ là một biến cố thì xác suất cổ điển của biến cố $A$ được tính theo công thức nào?", ["$P(A) = \\dfrac{n(A)}{n(\\Omega)}$", "$P(A) = \\dfrac{n(\\Omega)}{n(A)}$", "$P(A) = n(\\Omega) - n(A)$", "$P(A) = 1 - \\dfrac{n(A)}{n(\\Omega)}$"], 0, "Theo định nghĩa cổ điển của xác suất, $P(A) = \\dfrac{n(A)}{n(\\Omega)}$."),
            mcq("biet", "Với mọi biến cố $A$, nếu $\\overline{A}$ là biến cố đối của $A$ thì hệ thức nào sau đây luôn đúng?", ["$P(\\overline{A}) = 1 - P(A)$", "$P(\\overline{A}) = P(A) - 1$", "$P(\\overline{A}) = \\dfrac{1}{P(A)}$", "$P(\\overline{A}) = P(A)$"], 0, "Theo quy tắc xác suất của biến cố đối, ta luôn có $P(A) + P(\\overline{A}) = 1 \\Leftrightarrow P(\\overline{A}) = 1 - P(A)$."),
            mcq("biet", "Gieo một đồng xu cân đối và đồng chất $3$ lần liên tiếp. Số phần tử của không gian mẫu $n(\\Omega)$ bằng bao nhiêu?", ["$8$", "$6$", "$9$", "$4$"], 0, "Mỗi lần gieo đồng xu có $2$ kết quả có thể xảy ra ($S$ hoặc $N$), nên gieo $3$ lần liên tiếp có $n(\\Omega) = 2^3 = 8$ kết quả."),
            mcq("hieu", "Gieo một con xúc xắc cân đối và đồng chất $1$ lần. Xác suất để xuất hiện mặt có số chấm là một số nguyên tố bằng:", ["$\\dfrac{1}{2}$", "$\\dfrac{1}{3}$", "$\\dfrac{2}{3}$", "$\\dfrac{1}{6}$"], 0, "Không gian mẫu $\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ có $n(\\Omega) = 6$. Biến cố $A = \\{2; 3; 5\\}$ có $n(A) = 3$. Vậy $P(A) = \\dfrac{3}{6} = \\dfrac{1}{2}$."),
            mcq("hieu", "Một hộp chứa $4$ quả cầu trắng và $6$ quả cầu đen có cùng kích thước và khối lượng. Lấy ngẫu nhiên đồng thời $2$ quả cầu từ hộp. Xác suất để lấy được $2$ quả cầu cùng màu trắng là:", ["$\\dfrac{2}{15}$", "$\\dfrac{1}{3}$", "$\\dfrac{2}{5}$", "$\\dfrac{4}{15}$"], 0, "Số phần tử không gian mẫu là $n(\\Omega) = C_{10}^2 = 45$. Số cách lấy được $2$ quả cầu trắng là $n(A) = C_4^2 = 6$. Suy ra $P(A) = \\dfrac{6}{45} = \\dfrac{2}{15}$."),
            tf4("hieu", "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Gọi $A$ là biến cố “Tổng số chấm xuất hiện trên hai con xúc xắc bằng $7$” và $B$ là biến cố “Ít nhất một con xúc xắc xuất hiện mặt $6$ chấm”. Xét tính đúng sai của các khẳng định sau:", ["a) Số phần tử của không gian mẫu là $n(\\Omega) = 36$.", "b) Biến cố $A$ có $6$ kết quả thuận lợi nên $P(A) = \\dfrac{1}{6}$.", "c) Biến cố đối của $B$ là $\\overline{B}$: “Cả hai con xúc xắc đều không xuất hiện mặt $6$ chấm” và $n(\\overline{B}) = 25$.", "d) Xác suất của biến cố $B$ là $P(B) = \\dfrac{1}{3}$."], [True, True, True, False], "a) Đúng vì $n(\\Omega) = 6 \\cdot 6 = 36$.\nb) Đúng vì $A = \\{(1; 6), (2; 5), (3; 4), (4; 3), (5; 2), (6; 1)\\}$ có $n(A) = 6 \\Rightarrow P(A) = \\dfrac{6}{36} = \\dfrac{1}{6}$.\nc) Đúng vì mỗi con xúc xắc có $5$ cách không ra mặt $6$ chấm nên $n(\\overline{B}) = 5 \\cdot 5 = 25$.\nd) Sai vì $P(B) = 1 - P(\\overline{B}) = 1 - \\dfrac{25}{36} = \\dfrac{11}{36} \\ne \\dfrac{1}{3}$."),
            tf4("hieu", "Một tổ có $5$ học sinh nam và $4$ học sinh nữ. Chọn ngẫu nhiên đồng thời $3$ học sinh từ tổ để đi dự hội thảo. Xét tính đúng sai của các khẳng định sau:", ["a) Số phần tử của không gian mẫu là $n(\\Omega) = C_9^3 = 84$.", "b) Xác suất để chọn được cả $3$ học sinh đều là nữ bằng $\\dfrac{1}{21}$.", "c) Xác suất để chọn được $2$ học sinh nam và $1$ học sinh nữ bằng $\\dfrac{10}{21}$.", "d) Xác suất để trong $3$ học sinh được chọn có ít nhất $1$ học sinh nam bằng $\\dfrac{19}{21}$."], [True, True, True, False], "a) Đúng vì chọn $3$ học sinh từ $9$ học sinh có $C_9^3 = 84$ cách.\nb) Đúng vì xác suất chọn $3$ nữ là $\\dfrac{C_4^3}{84} = \\dfrac{4}{84} = \\dfrac{1}{21}$.\nc) Đúng vì xác suất chọn $2$ nam và $1$ nữ là $\\dfrac{C_5^2 \\cdot C_4^1}{84} = \\dfrac{10 \\cdot 4}{84} = \\dfrac{10}{21}$.\nd) Sai vì biến cố đối là cả $3$ đều là nữ có xác suất $\\dfrac{1}{21}$, nên xác suất có ít nhất $1$ nam là $1 - \\dfrac{1}{21} = \\dfrac{20}{21} \\ne \\dfrac{19}{21}$."),
            mcq("vandung", "Một chiếc hộp có $6$ viên bi đỏ, $5$ viên bi xanh và $4$ viên bi vàng đôi một khác nhau. Lấy ngẫu nhiên đồng thời $3$ viên bi từ hộp. Xác suất để $3$ viên bi lấy ra có đủ cả ba màu là:", ["$\\dfrac{24}{91}$", "$\\dfrac{12}{91}$", "$\\dfrac{30}{91}$", "$\\dfrac{15}{91}$"], 0, "Tổng số viên bi là $6 + 5 + 4 = 15$, nên $n(\\Omega) = C_{15}^3 = 455$. Số cách lấy ra $3$ viên bi có đủ ba màu (mỗi màu $1$ viên) là $n(A) = 6 \\cdot 5 \\cdot 4 = 120$. Vậy xác suất cần tìm là $P(A) = \\dfrac{120}{455} = \\dfrac{24}{91}$."),
            short("vandung", "Gieo một đồng xu cân đối và đồng chất $4$ lần liên tiếp. Tính xác suất để mặt ngửa xuất hiện ít nhất $1$ lần (viết kết quả dưới dạng số thập phân).", ["0,9375", "0.9375"], "Số phần tử không gian mẫu là $n(\\Omega) = 2^4 = 16$. Biến cố đối $\\overline{A}$: “Cả $4$ lần gieo đều xuất hiện mặt sấp” chỉ có $1$ kết quả thuận lợi là $(S, S, S, S)$. Vậy xác suất cần tìm là $P(A) = 1 - P(\\overline{A}) = 1 - \\dfrac{1}{16} = \\dfrac{15}{16} = 0,9375$."),
        ],
    },
]
