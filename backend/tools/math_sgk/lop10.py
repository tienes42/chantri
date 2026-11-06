"""Dữ liệu bài học SGK Toán Lớp 10 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 10 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học (title).
Mỗi bài học gồm đầy đủ Yêu cầu cần đạt (requirements), Định nghĩa, Lý thuyết, Công thức, Ví dụ, Ứng dụng thực tế
và đúng 10 câu hỏi luyện tập theo 3 mức độ: 4 Nhận biết + 4 Thông hiểu + 2 Vận dụng.
"""

GRADE = 10

LESSONS = [{'topic': 'l10-ch01-menh-de-tap-hop',
  'context_title': 'Chương I: Mệnh đề và tập hợp',
  'context': 'Chương I · SGK Toán 10: Mệnh đề và tập hợp.',
  'title': 'Bài 1: Mệnh đề',
  'icon': '💡',
  'description': 'Nhận biết mệnh đề, mệnh đề chứa biến, mệnh đề phủ định, mệnh đề kéo theo, tương đương và '
                 'các lượng từ.',
  'requirements': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của một '
                   'mệnh đề.',
                   'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow Q$, '
                   'mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                   'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
  'definition': 'Mệnh đề là một câu khẳng định có tính đúng hoặc sai (không thể vừa đúng vừa sai). Câu không '
                'phải là câu khẳng định hoặc không xác định được tính đúng sai thì không phải là mệnh đề.',
  'theory': '1. Mệnh đề phủ định của mệnh đề $P$ kí hiệu là $\\overline{P}$: $\\overline{P}$ đúng khi $P$ '
            'sai và $\\overline{P}$ sai khi $P$ đúng.\n'
            '2. Mệnh đề kéo theo $P \\Rightarrow Q$ chỉ sai khi $P$ đúng và $Q$ sai. Khi $P \\Rightarrow Q$ '
            'là định lí, $P$ là giả thiết (điều kiện đủ để có $Q$) và $Q$ là kết luận (điều kiện cần để có '
            '$P$).\n'
            '3. Mệnh đề tương đương $P \\Leftrightarrow Q$ đúng khi cả hai mệnh đề $P \\Rightarrow Q$ và $Q '
            '\\Rightarrow P$ cùng đúng.\n'
            "4. Phủ định của mệnh đề '$\\forall x \\in X, P(x)$' là '$\\exists x \\in X, \\overline{P(x)}$' "
            'và ngược lại.',
  'formulas': [{'category': 'Các phép toán mệnh đề và lượng từ',
                'items': [{'name': 'Mệnh đề kéo theo',
                           'formula': '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                           'note': '$P$: điều kiện đủ; $Q$: điều kiện cần'},
                          {'name': 'Mệnh đề tương đương',
                           'formula': '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai',
                           'note': '$P$ là điều kiện cần và đủ để có $Q$'},
                          {'name': 'Phủ định mệnh đề có lượng từ',
                           'formula': '$\\overline{\\forall x \\in X, P(x)} \\equiv \\exists x \\in X, '
                                      '\\overline{P(x)}$',
                           'note': 'Đổi $\\forall$ thành $\\exists$ và phủ định tính chất $P(x)$'}]}],
  'example': "Lập mệnh đề phủ định của mệnh đề $P$: '$\\forall x \\in \\mathbb{R}, x^2 + 1 > 0$' và xét tính "
             'đúng sai của mệnh đề phủ định đó.',
  'example_answer': "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0$'.\n"
                    'Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ nên mệnh '
                    'đề $P$ đúng, suy ra mệnh đề $\\overline{P}$ sai.',
  'real_life': 'Xây dựng các điều kiện rẽ nhánh logic (if-then-else) trong lập trình máy tính và kiểm tra '
               'quy tắc hợp đồng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Câu nào sau đây là một mệnh đề?',
            'options': ['Số $15$ chia hết cho $3$.',
                        'Hôm nay trời đẹp quá!',
                        'Bạn có thích học môn Toán không?',
                        '$2x + 1 = 5$.'],
            'answer': 0,
            'solution': "Câu 'Số $15$ chia hết cho $3$' là câu khẳng định đúng nên là một mệnh đề.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Mệnh đề phủ định của mệnh đề '$\\forall x \\in \\mathbb{R}, x^2 \\ge 0$' là:",
            'options': ['$\\forall x \\in \\mathbb{R}, x^2 < 0$',
                        '$\\exists x \\in \\mathbb{R}, x^2 < 0$',
                        '$\\exists x \\in \\mathbb{R}, x^2 \\le 0$',
                        '$\\forall x \\in \\mathbb{R}, x^2 \\neq 0$'],
            'answer': 1,
            'solution': 'Đổi lượng từ $\\forall$ thành $\\exists$ và phủ định $\\ge 0$ thành $< 0$, ta được '
                        "'$\\exists x \\in \\mathbb{R}, x^2 < 0$'.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 1: Mệnh đề**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Mệnh đề kéo theo**?',
            'options': ['$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai',
                        '$\\overline{\\forall x \\in X, P(x)} \\equiv \\exists x \\in X, \\overline{P(x)}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$; $A \\cup B = \\{x \\mid '
                        'x \\in A \\text{ hoặc } x \\in B\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 1: Mệnh đề, **Mệnh đề kéo theo** được xác '
                        'định bởi: $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai. ($P$: điều kiện đủ; '
                        '$Q$: điều kiện cần)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Mệnh đề**, nội dung/biểu thức $P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng '
                 'tính đúng sai là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Mệnh đề kéo theo',
                        'Phủ định mệnh đề có lượng từ',
                        'Giao và Hợp',
                        'Mệnh đề tương đương'],
            'answer': 3,
            'solution': 'Trong Bài 1: Mệnh đề, biểu thức/quy tắc $P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng '
                        'tính đúng sai chính là nội dung của **Mệnh đề tương đương**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho mệnh đề chứa biến $P(x)$: '$x^2 - 3x + 2 = 0$'. Mệnh đề nào sau đây là mệnh đề đúng?",
            'options': ['$P(1)$', '$P(0)$', '$P(3)$', '$P(-1)$'],
            'answer': 0,
            'solution': 'Thay $x = 1$ vào $P(x)$ ta được $1^2 - 3(1) + 2 = 0$ (đúng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Mệnh đề** (Chương I: Mệnh đề và tập hợp), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Mô tả được tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng; nhận '
                        'biết được tập con và hai tập hợp bằng nhau.',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Sử dụng được kí hiệu các tập con của $\\mathbb{R}$ (khoảng, đoạn, nửa khoảng).',
                        'Thực hiện được các phép toán trên tập hợp: giao ($A \\cap B$), hợp ($A \\cup B$), '
                        'hiệu ($A \\setminus B$) và phần bù ($C_E A$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 1: Mệnh đề: Nhận biết được mệnh đề toán học, mệnh đề '
                        'chứa biến và xác định tính đúng sai của một mệnh đề.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho hai mệnh đề $P$: 'Tứ giác $ABCD$ là hình thoi' và $Q$: 'Tứ giác $ABCD$ có hai đường "
                 "chéo vuông góc với nhau'.",
            'statements': ['Mệnh đề kéo theo $P \\Rightarrow Q$ là một mệnh đề đúng.',
                           'Mệnh đề đảo $Q \\Rightarrow P$ là một mệnh đề đúng.',
                           '$P$ là điều kiện đủ để có $Q$.',
                           'Hai mệnh đề $P$ và $Q$ là hai mệnh đề tương đương ($P \\Leftrightarrow Q$).'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng vì hình thoi luôn có hai đường chéo vuông góc. b) Sai vì tứ giác có hai '
                        'đường chéo vuông góc chưa chắc là hình thoi. c) Đúng. d) Sai vì $Q \\Rightarrow P$ '
                        'sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 1: Mệnh đề**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được mệnh đề toán học, '
                           'mệnh đề chứa biến và xác định tính đúng sai của một mệnh đề.',
                           'Quy tắc/công thức **Mệnh đề kéo theo** trong bài được xác định bởi: $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai.',
                           'Trong mọi trường hợp, **Mệnh đề kéo theo** luôn được tính bằng công thức $A '
                           '\\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$; $A \\cup B = \\{x \\mid '
                           'x \\in A \\text{ hoặc } x \\in B\\}$ (thuộc Giao và Hợp) mà không cần điều kiện '
                           'của Bài 1: Mệnh đề.',
                           "Với bài toán minh họa: “Lập mệnh đề phủ định của mệnh đề $P$: '$\\forall x \\in "
                           "\\mathbb{R}, x^2 + 1 > 0$' và xét tính đúng sai của mệnh đề phủ định đó.”, lời "
                           "giải đúng là: Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in "
                           "\\mathbb{R}, x^2 + 1 \\le 0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ "
                           'với mọi $x \\in \\mathbb{R}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Mệnh đề. b) **Đúng** theo công thức '
                        'trọng tâm **Mệnh đề kéo theo** ($P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai). '
                        'c) **Sai** vì $A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$; $A \\cup '
                        'B = \\{x \\mid x \\in A \\text{ hoặc } x \\in B\\}$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Mệnh đề kéo theo**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 1: Mệnh đề** để giải quyết tình huống sau: Lập mệnh đề phủ định '
                 "của mệnh đề $P$: '$\\forall x \\in \\mathbb{R}, x^2 + 1 > 0$' và xét tính đúng sai của "
                 'mệnh đề phủ định đó. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác: $F(0; 0) = 0$; $F(0; 4) = 8$; '
                        '$F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = 12$. Vậy giá trị lớn...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Mệnh đề: Mệnh đề phủ định là $\\overline{P}$: '
                        "'$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0$'.\n"
                        'Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ nên '
                        'mệnh đề $P$ đúng, suy ra mệnh đề $\\overline{P}$ sai.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu giá trị nguyên của $x$ thuộc đoạn $[-3; 3]$ để mệnh đề chứa biến $P(x)$: '
                 "'$x^2 - 4 \\le 0$' là mệnh đề đúng?",
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $x^2 - 4 \\le 0 \\Leftrightarrow -2 \\le x \\le 2$. Các giá trị nguyên thỏa '
                        'mãn là $-2; -1; 0; 1; 2$, gồm $5$ giá trị.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch01-menh-de-tap-hop',
  'context_title': 'Chương I: Mệnh đề và tập hợp',
  'context': 'Chương I · SGK Toán 10: Mệnh đề và tập hợp.',
  'title': 'Bài 2: Tập hợp và các phép toán trên tập hợp',
  'icon': '⭕',
  'description': 'Biểu diễn tập hợp, tập hợp con và thực hiện các phép toán giao, hợp, hiệu của hai tập hợp.',
  'requirements': ['Mô tả được tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng; nhận biết '
                   'được tập con và hai tập hợp bằng nhau.',
                   'Sử dụng được kí hiệu các tập con của $\\mathbb{R}$ (khoảng, đoạn, nửa khoảng).',
                   'Thực hiện được các phép toán trên tập hợp: giao ($A \\cap B$), hợp ($A \\cup B$), hiệu '
                   '($A \\setminus B$) và phần bù ($C_E A$).'],
  'definition': 'Giao của hai tập hợp $A$ và $B$ ($A \\cap B$) gồm các phần tử thuộc cả $A$ và $B$. Hợp của '
                '$A$ và $B$ ($A \\cup B$) gồm các phần tử thuộc $A$ hoặc thuộc $B$. Hiệu của $A$ và $B$ ($A '
                '\\setminus B$) gồm các phần tử thuộc $A$ nhưng không thuộc $B$.',
  'theory': '1. Một tập hợp có $n$ phần tử thì có tất cả $2^n$ tập hợp con.\n'
            '2. Nếu $A \\subset E$ thì hiệu $E \\setminus A$ được gọi là phần bù của $A$ trong $E$, kí hiệu '
            'là $C_E A$.\n'
            '3. Công thức tính số phần tử của hợp hai tập hợp hữu hạn: $n(A \\cup B) = n(A) + n(B) - n(A '
            '\\cap B)$.',
  'formulas': [{'category': 'Các phép toán trên tập hợp',
                'items': [{'name': 'Giao và Hợp',
                           'formula': '$A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$; $A \\cup '
                                      'B = \\{x \\mid x \\in A \\text{ hoặc } x \\in B\\}$',
                           'note': 'Biểu diễn trực quan bằng biểu đồ Venn hoặc trục số'},
                          {'name': 'Hiệu và Phần bù',
                           'formula': '$A \\setminus B = \\{x \\mid x \\in A \\text{ và } x \\notin B\\}$; '
                                      '$C_E A = E \\setminus A$ ($A \\subset E$)',
                           'note': 'Chú ý lấy đúng dấu ngoặc tròn/vuông khi tìm phần bù trên $\\mathbb{R}$'},
                          {'name': 'Công thức lực lượng',
                           'formula': '$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$',
                           'note': 'Khi $A \\cap B = \\varnothing$ thì $n(A \\cup B) = n(A) + n(B)$'}]}],
  'example': 'Cho hai tập hợp $A = [-2; 3)$ và $B = (1; 5]$. Tìm $A \\cap B$, $A \\cup B$ và $A \\setminus '
             'B$.',
  'example_answer': 'Biểu diễn trên trục số, ta được:\n'
                    '- $A \\cap B = (1; 3)$;\n'
                    '- $A \\cup B = [-2; 5]$;\n'
                    '- $A \\setminus B = [-2; 1]$.',
  'real_life': 'Lọc dữ liệu khách hàng đồng thời mua hai nhóm sản phẩm hoặc thống kê số học sinh đăng kí các '
               'câu lạc bộ ngoại khóa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai tập hợp $A = \\{1; 2; 3; 4\\}$ và $B = \\{3; 4; 5; 6\\}$. Tập hợp $A \\cap B$ là:',
            'options': ['$\\{1; 2\\}$', '$\\{3; 4\\}$', '$\\{5; 6\\}$', '$\\{1; 2; 3; 4; 5; 6\\}$'],
            'answer': 1,
            'solution': 'Các phần tử thuộc cả $A$ và $B$ là $3$ và $4$, nên $A \\cap B = \\{3; 4\\}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập hợp $X = \\{x \\in \\mathbb{R} \\mid -1 \\le x < 4\\}$ được viết dưới dạng nửa khoảng '
                 'là:',
            'options': ['$(-1; 4]$', '$[-1; 4]$', '$[-1; 4)$', '$(-1; 4)$'],
            'answer': 2,
            'solution': 'Dấu $\\le$ ứng với ngoặc vuông tại $-1$ và dấu $<$ ứng với ngoặc tròn tại $4$, tức '
                        'là $[-1; 4)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 2: Tập hợp và các phép toán trên tập hợp**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Giao và Hợp**?',
            'options': ['$A \\setminus B = \\{x \\mid x \\in A \\text{ và } x \\notin B\\}$; $C_E A = E '
                        '\\setminus A$ ($A \\subset E$)',
                        '$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$; $A \\cup B = \\{x \\mid '
                        'x \\in A \\text{ hoặc } x \\in B\\}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 2: Tập hợp và các phép toán trên tập hợp, '
                        '**Giao và Hợp** được xác định bởi: $A \\cap B = \\{x \\mid x \\in A \\text{ và } x '
                        '\\in B\\}$; $A \\cup B = \\{x \\mid x \\in A \\text{ hoặc } x \\in B\\}$. (Biểu '
                        'diễn trực quan bằng biểu đồ Venn hoặc trục số)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Tập hợp và các phép toán trên tập hợp**, nội dung/biểu thức $A \\setminus B '
                 '= \\{x \\mid x \\in A \\text{ và } x \\notin B\\}$; $C_E A = E \\setminus A$ ($A \\subset '
                 'E$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hiệu và Phần bù', 'Giao và Hợp', 'Công thức lực lượng', 'Mệnh đề kéo theo'],
            'answer': 0,
            'solution': 'Trong Bài 2: Tập hợp và các phép toán trên tập hợp, biểu thức/quy tắc $A \\setminus '
                        'B = \\{x \\mid x \\in A \\text{ và } x \\notin B\\}$; $C_E A = E \\setminus A$ ($A '
                        '\\subset E$) chính là nội dung của **Hiệu và Phần bù**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai tập hợp $A = (-\\infty; 2]$ và $B = (0; +\\infty)$. Tập hợp $A \\setminus B$ là:',
            'options': ['$(-\\infty; 0)$', '$(-\\infty; 0]$', '$(0; 2]$', '$[0; 2]$'],
            'answer': 1,
            'solution': 'Các phần tử thuộc $A$ nhưng không thuộc $B$ (tức là $x \\le 2$ và $x \\le 0$) tạo '
                        'thành tập $(-\\infty; 0]$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Tập hợp và các phép toán trên tập hợp** (Chương I: Mệnh đề và tập hợp), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Mô tả được tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng; nhận '
                        'biết được tập con và hai tập hợp bằng nhau.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 2: Tập hợp và các phép toán trên tập hợp: Mô tả được '
                        'tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng; nhận biết được '
                        'tập con và hai tập hợp bằng nhau.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tập hợp $A = \\{a; b; c\\}$ và hai tập số thực $M = [-3; 2], N = (0; 5)$.',
            'statements': ['Tập hợp $A$ có tất cả $8$ tập hợp con.',
                           'Giao của hai tập hợp $M$ và $N$ là $M \\cap N = (0; 2]$.',
                           'Hợp của hai tập hợp $M$ và $N$ là $M \\cup N = [-3; 5]$.',
                           'Phần bù của tập $N$ trong $\\mathbb{R}$ là $C_{\\mathbb{R}}N = (-\\infty; 0] '
                           '\\cup [5; +\\infty)$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $2^3 = 8$. b) Đúng. c) Sai vì $5 \\notin N$ nên $M \\cup N = [-3; 5)$. '
                        'd) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 2: Tập hợp và các phép '
                 'toán trên tập hợp**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được tập hợp bằng cách liệt '
                           'kê phần tử hoặc chỉ ra tính chất đặc trưng; nhận biết được tập con và hai tập '
                           'hợp bằng nhau.',
                           'Quy tắc/công thức **Giao và Hợp** trong bài được xác định bởi: $A \\cap B = \\{x '
                           '\\mid x \\in A \\text{ và } x \\in B\\}$; $A \\cup B = \\{x \\mid x \\in A '
                           '\\text{ hoặc } x \\in B\\}$.',
                           'Trong mọi trường hợp, **Giao và Hợp** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 2: Tập hợp và các phép toán trên tập hợp.',
                           'Với bài toán minh họa: “Cho hai tập hợp $A = [-2; 3)$ và $B = (1; 5]$. Tìm $A '
                           '\\cap B$, $A \\cup B$ và $A \\setminus B$.”, lời giải đúng là: Biểu diễn trên '
                           'trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - $A '
                           '\\setminus B = [-2; 1]$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Tập hợp và các phép toán trên tập hợp. '
                        'b) **Đúng** theo công thức trọng tâm **Giao và Hợp** ($A \\cap B = \\{x \\mid x '
                        '\\in A \\text{ và } x \\in B\\}$; $A \\cup B = \\{x \\mid x \\in A \\text{ hoặc } x '
                        '\\in B\\}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Giao và Hợp**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 2: Tập hợp và các phép toán trên tập hợp** để giải quyết tình '
                 'huống sau: Cho hai tập hợp $A = [-2; 3)$ và $B = (1; 5]$. Tìm $A \\cap B$, $A \\cup B$ và '
                 '$A \\setminus B$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        'Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác: $F(0; 0) = 0$; $F(0; 4) = 8$; '
                        '$F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = 12$. Vậy giá trị lớn...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Tập hợp và các phép toán trên tập hợp: Biểu diễn trên '
                        'trục số, ta được:\n'
                        '- $A \\cap B = (1; 3)$;\n'
                        '- $A \\cup B = [-2; 5]$;\n'
                        '- $A \\setminus B = [-2; 1]$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một lớp học có $40$ học sinh, trong đó có $25$ em thích môn Toán, $20$ em thích môn Văn và '
                 '$10$ em thích cả hai môn Toán và Văn. Hỏi có bao nhiêu học sinh trong lớp không thích cả '
                 'hai môn này?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Số học sinh thích ít nhất một trong hai môn là $n(T \\cup V) = 25 + 20 - 10 = 35$. '
                        'Số học sinh không thích cả hai môn là $40 - 35 = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch02-bat-phuong-trinh-hai-an',
  'context_title': 'Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn',
  'context': 'Chương II · SGK Toán 10: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn.',
  'title': 'Bài 3: Bất phương trình bậc nhất hai ẩn',
  'icon': '🗺️',
  'description': 'Nhận biết bất phương trình bậc nhất hai ẩn và biểu diễn miền nghiệm trên mặt phẳng tọa độ.',
  'requirements': ['Nhận biết được bất phương trình bậc nhất hai ẩn và nghiệm của nó.',
                   'Biểu diễn được miền nghiệm của bất phương trình bậc nhất hai ẩn trên mặt phẳng tọa độ '
                   '$Oxy$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Đường thẳng bờ** ($d: ax + by = c$) vào '
                   'giải bài tập.'],
  'definition': 'Bất phương trình bậc nhất hai ẩn $x, y$ có dạng tổng quát là $ax + by < c$ (hoặc $ax + by > '
                'c, ax + by \\le c, ax + by \\ge c$), trong đó $a, b, c$ là những số thực đã cho, $a$ và $b$ '
                'không đồng thời bằng $0$.',
  'theory': 'Cách biểu diễn miền nghiệm của bất phương trình $ax + by < c$ trên mặt phẳng tọa độ $Oxy$:\n'
            '- Bước 1: Vẽ đường thẳng bờ $d: ax + by = c$.\n'
            '- Bước 2: Lấy một điểm $M_0(x_0; y_0)$ không nằm trên $d$ (thường lấy gốc tọa độ $O(0; 0)$ nếu '
            '$c \\neq 0$) và tính $ax_0 + by_0$.\n'
            '- Bước 3: Nếu $ax_0 + by_0 < c$ thì nửa mặt phẳng bờ $d$ chứa $M_0$ là miền nghiệm; ngược lại '
            'nửa mặt phẳng bờ $d$ không chứa $M_0$ là miền nghiệm.',
  'formulas': [{'category': 'Bất phương trình bậc nhất hai ẩn',
                'items': [{'name': 'Đường thẳng bờ',
                           'formula': '$d: ax + by = c$',
                           'note': 'Chia mặt phẳng thành hai nửa mặt phẳng'},
                          {'name': 'Quy tắc điểm thử $M_0(x_0; y_0) \\notin d$',
                           'formula': 'Thay tọa độ $(x_0; y_0)$ vào bất phương trình',
                           'note': 'Nếu đúng thì miền nghiệm chứa $M_0$'}]}],
  'example': 'Kiểm tra xem điểm $A(1; 2)$ có thuộc miền nghiệm của bất phương trình $2x - 3y + 1 < 0$ hay '
             'không.',
  'example_answer': 'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 = -3 '
                    '< 0$ (đúng).\n'
                    'Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương trình đã cho.',
  'real_life': 'Xác định tập hợp các phương án mua hai loại nguyên liệu không vượt quá ngân sách cho phép.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bất phương trình nào sau đây là bất phương trình bậc nhất hai ẩn?',
            'options': ['$x^2 + y \\le 4$', '$2x - 3xy < 1$', '$2x - 5y > 3$', '$0x + 0y \\ge -1$'],
            'answer': 2,
            'solution': 'Bất phương trình $2x - 5y > 3$ có dạng $ax + by > c$ với $a = 2, b = -5$ không đồng '
                        'thời bằng $0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cặp số nào sau đây là một nghiệm của bất phương trình $x + 2y > 4$?',
            'options': ['$(1; 1)$', '$(0; 2)$', '$(2; 0)$', '$(3; 1)$'],
            'answer': 3,
            'solution': 'Thay $x = 3, y = 1$ ta được $3 + 2(1) = 5 > 4$ (thỏa mãn).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 3: Bất phương trình bậc nhất hai ẩn**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Đường thẳng bờ**?',
            'options': ['$d: ax + by = c$',
                        'Thay tọa độ $(x_0; y_0)$ vào bất phương trình',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 3: Bất phương trình bậc nhất hai ẩn, **Đường '
                        'thẳng bờ** được xác định bởi: $d: ax + by = c$. (Chia mặt phẳng thành hai nửa mặt '
                        'phẳng)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Bất phương trình bậc nhất hai ẩn**, nội dung/biểu thức Thay tọa độ $(x_0; '
                 'y_0)$ vào bất phương trình là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Đường thẳng bờ',
                        'Quy tắc điểm thử $M_0(x_0; y_0) \\notin d$',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương'],
            'answer': 1,
            'solution': 'Trong Bài 3: Bất phương trình bậc nhất hai ẩn, biểu thức/quy tắc Thay tọa độ $(x_0; '
                        'y_0)$ vào bất phương trình chính là nội dung của **Quy tắc điểm thử $M_0(x_0; y_0) '
                        '\\notin d$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Miền nghiệm của bất phương trình $3x - 2y \\le 6$ (tính cả bờ) chứa điểm nào sau đây?',
            'options': ['$A(3; 1)$', '$B(4; 0)$', '$O(0; 0)$', '$C(2; -1)$'],
            'answer': 2,
            'solution': 'Thay $O(0; 0)$ vào bất phương trình được $0 \\le 6$ (đúng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Bất phương trình bậc nhất hai ẩn** (Chương II: Bất phương trình và hệ bất '
                 'phương trình bậc nhất hai ẩn), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Nhận biết được bất phương trình bậc nhất hai ẩn và nghiệm của nó.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 3: Bất phương trình bậc nhất hai ẩn: Nhận biết được '
                        'bất phương trình bậc nhất hai ẩn và nghiệm của nó.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho bất phương trình bậc nhất hai ẩn $2x + y - 4 < 0$ (1).',
            'statements': ['Đường thẳng bờ của miền nghiệm bất phương trình (1) là $d: 2x + y - 4 = 0$.',
                           'Miền nghiệm của bất phương trình (1) bao gồm cả các điểm nằm trên đường thẳng '
                           '$d$.',
                           'Gốc tọa độ $O(0; 0)$ thuộc miền nghiệm của bất phương trình (1).',
                           'Điểm $M(2; 1)$ không thuộc miền nghiệm của bất phương trình (1).'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì dấu bất phương trình là $<$ (ngặt) nên không lấy bờ $d$. c) Đúng '
                        'vì $0 + 0 - 4 = -4 < 0$. d) Đúng vì $2(2) + 1 - 4 = 1 > 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 3: Bất phương trình bậc '
                 'nhất hai ẩn**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được bất phương trình '
                           'bậc nhất hai ẩn và nghiệm của nó.',
                           'Quy tắc/công thức **Đường thẳng bờ** trong bài được xác định bởi: $d: ax + by = '
                           'c$.',
                           'Trong mọi trường hợp, **Đường thẳng bờ** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 3: Bất phương trình bậc nhất hai ẩn.',
                           'Với bài toán minh họa: “Kiểm tra xem điểm $A(1; 2)$ có thuộc miền nghiệm của bất '
                           'phương trình $2x - 3y + 1 < 0$ hay không.”, lời giải đúng là: Thay $x = 1, y = '
                           '2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 = -3 < 0$ '
                           '(đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm củ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Bất phương trình bậc nhất hai ẩn. b) '
                        '**Đúng** theo công thức trọng tâm **Đường thẳng bờ** ($d: ax + by = c$). c) **Sai** '
                        'vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Đường thẳng bờ**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 3: Bất phương trình bậc nhất hai ẩn** để giải quyết tình huống '
                 'sau: Kiểm tra xem điểm $A(1; 2)$ có thuộc miền nghiệm của bất phương trình $2x - 3y + 1 < '
                 '0$ hay không. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác: $F(0; 0) = 0$; $F(0; 4) = 8$; '
                        '$F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = 12$. Vậy giá trị lớn...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Bất phương trình bậc nhất hai ẩn: Thay $x = 1, y = 2$ '
                        'vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 = -3 < 0$ (đúng).\n'
                        'Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương trình đã cho.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu cặp số nguyên dương $(x; y)$ thỏa mãn bất phương trình $2x + 3y \\le 8$?',
            'answer': ['3'],
            'unit': None,
            'solution': 'Vì $x, y \\in \\mathbb{N}^*$ nên nếu $y = 1 \\Rightarrow 2x \\le 5 \\Rightarrow x '
                        '\\in \\{1; 2\\}$ (2 cặp); nếu $y = 2 \\Rightarrow 2x \\le 2 \\Rightarrow x = 1$ (1 '
                        'cặp); nếu $y \\ge 3$ không có $x$. Vậy có tất cả $3$ cặp: $(1; 1), (2; 1), (1; 2)$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch02-bat-phuong-trinh-hai-an',
  'context_title': 'Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn',
  'context': 'Chương II · SGK Toán 10: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn.',
  'title': 'Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy hoạch tuyến tính',
  'icon': '🏭',
  'description': 'Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn và tìm giá trị lớn nhất, nhỏ '
                 'nhất của biểu thức bậc nhất trên miền đa giác.',
  'requirements': ['Nhận biết được hệ bất phương trình bậc nhất hai ẩn và biểu diễn miền nghiệm của hệ.',
                   'Vận dụng tìm giá trị lớn nhất hoặc giá trị nhỏ nhất của biểu thức $F(x; y) = ax + by$ '
                   'trên miền nghiệm là miền đa giác (quy hoạch tuyến tính).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hàm mục tiêu** ($F(x; y) = ax + by$) vào '
                   'giải bài tập.'],
  'definition': 'Hệ bất phương trình bậc nhất hai ẩn là một hệ gồm hai hay nhiều bất phương trình bậc nhất '
                'hai ẩn. Miền nghiệm của hệ là giao các miền nghiệm của tất cả các bất phương trình trong '
                'hệ.',
  'theory': 'Định lí cực trị trên miền đa giác: Giá trị lớn nhất (hay nhỏ nhất) của biểu thức bậc nhất $F(x; '
            'y) = ax + by$ trên một miền đa giác lồi (kể cả biên) luôn đạt được tại một trong các đỉnh của '
            'đa giác đó.\n'
            'Do đó, để tìm giá trị lớn nhất/nhỏ nhất của $F(x; y)$, ta xác định tọa độ các đỉnh của miền đa '
            'giác rồi tính giá trị của $F$ tại từng đỉnh để so sánh.',
  'formulas': [{'category': 'Bài toán tối ưu trên miền đa giác',
                'items': [{'name': 'Hàm mục tiêu',
                           'formula': '$F(x; y) = ax + by$',
                           'note': 'Biểu thị lợi nhuận cần tối đa hóa hoặc chi phí cần tối thiểu hóa'},
                          {'name': 'Nguyên tắc đỉnh đa giác',
                           'formula': '$\\max F$ và $\\min F$ đạt tại các đỉnh $A_i(x_i; y_i)$ của miền đa '
                                      'giác',
                           'note': 'So sánh trực tiếp $F(x_i; y_i)$ tại tất cả các đỉnh'}]}],
  'example': 'Tìm giá trị lớn nhất của biểu thức $F(x; y) = 3x + 2y$ trên miền tứ giác lồi $OABC$ có các '
             'đỉnh $O(0; 0), A(0; 4), B(2; 3), C(4; 0)$.',
  'example_answer': 'Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác:\n'
                    '$F(0; 0) = 0$; $F(0; 4) = 8$; $F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = 12$.\n'
                    'Vậy giá trị lớn nhất của $F(x; y)$ trên miền đã cho bằng $12$.',
  'real_life': 'Lập kế hoạch sản xuất hai mặt hàng từ nguồn nguyên liệu và giờ công giới hạn để thu được '
               'tổng lợi nhuận cao nhất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Điểm nào sau đây thuộc miền nghiệm của hệ bất phương trình $\\begin{cases} x \\ge 0 \\\\ y '
                 '\\ge 0 \\\\ x + y \\le 4 \\end{cases}$?',
            'options': ['$(-1; 2)$', '$(2; 3)$', '$(3; -1)$', '$(1; 2)$'],
            'answer': 3,
            'solution': 'Thay $(1; 2)$ vào hệ ta thấy $1 \\ge 0, 2 \\ge 0$ và $1 + 2 = 3 \\le 4$ đều thỏa '
                        'mãn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị lớn nhất và giá trị nhỏ nhất của biểu thức $F(x; y) = ax + by$ trên một miền đa '
                 'giác lồi luôn đạt được tại:',
            'options': ['Một trong các đỉnh của miền đa giác đó',
                        'Trọng tâm của miền đa giác đó',
                        'Trung điểm các cạnh của đa giác',
                        'Gốc tọa độ $O(0; 0)$'],
            'answer': 0,
            'solution': 'Theo định lí quy hoạch tuyến tính, cực trị của $F(x; y) = ax + by$ trên miền đa '
                        'giác đạt tại một trong các đỉnh của đa giác.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy '
                 'hoạch tuyến tính**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hàm mục tiêu**?',
            'options': ['$\\max F$ và $\\min F$ đạt tại các đỉnh $A_i(x_i; y_i)$ của miền đa giác',
                        '$F(x; y) = ax + by$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài '
                        'toán quy hoạch tuyến tính, **Hàm mục tiêu** được xác định bởi: $F(x; y) = ax + by$. '
                        '(Biểu thị lợi nhuận cần tối đa hóa hoặc chi phí cần tối thiểu hóa)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy hoạch tuyến tính**, nội '
                 'dung/biểu thức $\\max F$ và $\\min F$ đạt tại các đỉnh $A_i(x_i; y_i)$ của miền đa giác là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hàm mục tiêu', 'Mệnh đề kéo theo', 'Nguyên tắc đỉnh đa giác', 'Mệnh đề tương đương'],
            'answer': 2,
            'solution': 'Trong Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy hoạch tuyến tính, '
                        'biểu thức/quy tắc $\\max F$ và $\\min F$ đạt tại các đỉnh $A_i(x_i; y_i)$ của miền '
                        'đa giác chính là nội dung của **Nguyên tắc đỉnh đa giác**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Miền nghiệm của hệ bất phương trình $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ 2x + y '
                 '\\le 4 \\end{cases}$ là miền tam giác $OAB$. Diện tích của tam giác $OAB$ bằng:',
            'options': ['$8$', '$2$', '$6$', '$4$'],
            'answer': 3,
            'solution': 'Tam giác $OAB$ vuông tại $O(0; 0)$ với hai đỉnh $A(2; 0)$ và $B(0; 4)$, có diện '
                        'tích $S = \\dfrac{1}{2} \\cdot 2 \\cdot 4 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy hoạch tuyến tính** '
                 '(Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được hệ bất phương trình bậc nhất hai ẩn và biểu diễn miền nghiệm của hệ.',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy '
                        'hoạch tuyến tính: Nhận biết được hệ bất phương trình bậc nhất hai ẩn và biểu diễn '
                        'miền nghiệm của hệ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hệ bất phương trình $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le 5 \\\\ x '
                 '\\le 3 \\end{cases}$ có miền nghiệm là tứ giác $OABC$ và biểu thức $F(x; y) = 2x + 3y$.',
            'statements': ['Điểm $O(0; 0)$ là một đỉnh của miền nghiệm.',
                           'Các đỉnh của miền nghiệm là $O(0; 0), A(3; 0), B(3; 2), C(0; 5)$.',
                           'Giá trị của biểu thức $F$ tại đỉnh $B(3; 2)$ bằng $12$.',
                           'Giá trị lớn nhất của biểu thức $F$ trên miền nghiệm bằng $12$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng. c) Đúng vì $F(3; 2) = 2(3) + 3(2) = 12$. d) Sai vì tại $C(0; 5)$ '
                        'ta có $F(0; 5) = 15 > 12$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 4: Hệ bất phương trình '
                 'bậc nhất hai ẩn và bài toán quy hoạch tuyến tính**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hệ bất phương trình '
                           'bậc nhất hai ẩn và biểu diễn miền nghiệm của hệ.',
                           'Quy tắc/công thức **Hàm mục tiêu** trong bài được xác định bởi: $F(x; y) = ax + '
                           'by$.',
                           'Trong mọi trường hợp, **Hàm mục tiêu** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy '
                           'hoạch tuyến tính.',
                           'Với bài toán minh họa: “Tìm giá trị lớn nhất của biểu thức $F(x; y) = 3x + 2y$ '
                           'trên miền tứ giác lồi $OABC$ có các đỉnh $O(0; 0), A(0; 4), B(2; 3), C(4; 0)$.”, '
                           'lời giải đúng là: Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác: $F(0; 0) '
                           '= 0$; $F(0; 4) = 8$; $F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = '
                           '12$....'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Hệ bất phương trình bậc nhất hai ẩn và '
                        'bài toán quy hoạch tuyến tính. b) **Đúng** theo công thức trọng tâm **Hàm mục '
                        'tiêu** ($F(x; y) = ax + by$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ '
                        'đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung của **Hàm '
                        'mục tiêu**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy hoạch '
                 'tuyến tính** để giải quyết tình huống sau: Tìm giá trị lớn nhất của biểu thức $F(x; y) = '
                 '3x + 2y$ trên miền tứ giác lồi $OABC$ có các đỉnh $O(0; 0), A(0; 4), B(2; 3), C(4; 0)$. '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác: $F(0; 0) = 0$; $F(0; 4) = 8$; '
                        '$F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = 12$. Vậy giá trị lớn...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Hệ bất phương trình bậc nhất hai ẩn và bài toán quy '
                        'hoạch tuyến tính: Tính giá trị của $F(x; y)$ tại các đỉnh của tứ giác:\n'
                        '$F(0; 0) = 0$; $F(0; 4) = 8$; $F(2; 3) = 3(2) + 2(3) = 12$; $F(4; 0) = 3(4) + 0 = '
                        '12$.\n'
                        'Vậy giá trị lớn nhất của $F(x; y)$ trên miền đã cho bằng $12$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm giá trị lớn nhất của biểu thức $F(x; y) = 4x + 5y$ trên miền tam giác có ba đỉnh là '
                 '$O(0; 0), A(4; 0), B(2; 3)$.',
            'answer': ['23'],
            'unit': None,
            'solution': 'Ta có $F(0; 0) = 0$; $F(4; 0) = 16$; $F(2; 3) = 4(2) + 5(3) = 23$. Vậy giá trị lớn '
                        'nhất của $F$ bằng $23$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch03-he-thuc-luong-tam-giac',
  'context_title': 'Chương III: Hệ thức lượng trong tam giác',
  'context': 'Chương III · SGK Toán 10: Hệ thức lượng trong tam giác.',
  'title': 'Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ',
  'icon': '🧭',
  'description': 'Xác định giá trị lượng giác trên nửa đường tròn đơn vị và mối liên hệ giữa hai góc bù '
                 'nhau.',
  'requirements': ['Nhận biết được giá trị lượng giác ($\\sin, \\cos, \\tan, \\cot$) của một góc $\\alpha$ '
                   'từ $0^\\circ$ đến $180^\\circ$ thông qua nửa đường tròn đơn vị.',
                   'Vận dụng được tính chất lượng giác của hai góc bù nhau ($\\alpha$ và $180^\\circ - '
                   '\\alpha$).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hai góc bù nhau** ($\\sin(180^\\circ - '
                   '\\alpha) = \\sin \\alpha$; $\\cos(180^\\circ - \\alpha) = -\\cos \\alpha$) vào giải bài '
                   'tập.'],
  'definition': 'Với mỗi góc $\\alpha$ ($0^\\circ \\le \\alpha \\le 180^\\circ$), gọi $M(x_0; y_0)$ là điểm '
                'trên nửa đường tròn đơn vị sao cho $\\widehat{xOM} = \\alpha$. Khi đó: $\\sin \\alpha = '
                'y_0$, $\\cos \\alpha = x_0$, $\\tan \\alpha = \\dfrac{y_0}{x_0}$ ($\\alpha \\neq '
                '90^\\circ$), $\\cot \\alpha = \\dfrac{x_0}{y_0}$ ($0^\\circ < \\alpha < 180^\\circ$).',
  'theory': '1. Dấu của các giá trị lượng giác: Với $0^\\circ < \\alpha < 180^\\circ$, $\\sin \\alpha > 0$ '
            'luôn dương; nếu $\\alpha$ là góc nhọn ($0^\\circ < \\alpha < 90^\\circ$) thì $\\cos \\alpha, '
            '\\tan \\alpha, \\cot \\alpha > 0$; nếu $\\alpha$ là góc tù ($90^\\circ < \\alpha < 180^\\circ$) '
            'thì $\\cos \\alpha, \\tan \\alpha, \\cot \\alpha < 0$.\n'
            '2. Hai góc bù nhau ($\\alpha$ và $180^\\circ - \\alpha$): $\\sin(180^\\circ - \\alpha) = \\sin '
            '\\alpha$, còn $\\cos, \\tan, \\cot$ của chúng đối nhau.',
  'formulas': [{'category': 'Giá trị lượng giác của góc từ $0^\\circ$ đến $180^\\circ$',
                'items': [{'name': 'Hai góc bù nhau',
                           'formula': '$\\sin(180^\\circ - \\alpha) = \\sin \\alpha$; $\\cos(180^\\circ - '
                                      '\\alpha) = -\\cos \\alpha$',
                           'note': '$\\tan(180^\\circ - \\alpha) = -\\tan \\alpha$; $\\cot(180^\\circ - '
                                   '\\alpha) = -\\cot \\alpha$'},
                          {'name': 'Hệ thức lượng giác cơ bản',
                           'formula': '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$; $1 + \\tan^2 \\alpha = '
                                      '\\dfrac{1}{\\cos^2 \\alpha}$',
                           'note': 'Áp dụng cho mọi góc mà biểu thức xác định'}]}],
  'example': 'Cho biết $\\sin \\alpha = \\dfrac{3}{5}$ với $90^\\circ < \\alpha < 180^\\circ$. Tính $\\cos '
             '\\alpha$ và $\\tan \\alpha$.',
  'example_answer': 'Ta có $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = 1 - \\left(\\dfrac{3}{5}\\right)^2 = '
                    '\\dfrac{16}{25}$.\n'
                    'Vì $90^\\circ < \\alpha < 180^\\circ$ nên $\\cos \\alpha < 0$, suy ra $\\cos \\alpha = '
                    '-\\dfrac{4}{5}$ và $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha} = '
                    '-\\dfrac{3}{4}$.',
  'real_life': 'Tính hình chiếu của lực kéo hợp với phương chuyển động một góc tù trong cơ học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với góc $\\alpha$ bất kì thỏa mãn $0^\\circ \\le \\alpha \\le 180^\\circ$, khẳng định nào '
                 'sau đây là đúng?',
            'options': ['$\\sin(180^\\circ - \\alpha) = \\sin \\alpha$',
                        '$\\cos(180^\\circ - \\alpha) = \\cos \\alpha$',
                        '$\\sin(180^\\circ - \\alpha) = -\\sin \\alpha$',
                        '$\\tan(180^\\circ - \\alpha) = \\tan \\alpha$'],
            'answer': 0,
            'solution': 'Hai góc bù nhau có sin bằng nhau: $\\sin(180^\\circ - \\alpha) = \\sin \\alpha$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của $\\cos 120^\\circ$ bằng:',
            'options': ['$\\dfrac{1}{2}$',
                        '$-\\dfrac{1}{2}$',
                        '$-\\dfrac{\\sqrt{3}}{2}$',
                        '$\\dfrac{\\sqrt{3}}{2}$'],
            'answer': 1,
            'solution': 'Ta có $\\cos 120^\\circ = -\\cos 60^\\circ = -\\dfrac{1}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hai góc bù nhau**?',
            'options': ['$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$; $1 + \\tan^2 \\alpha = \\dfrac{1}{\\cos^2 '
                        '\\alpha}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$\\sin(180^\\circ - \\alpha) = \\sin \\alpha$; $\\cos(180^\\circ - \\alpha) = '
                        '-\\cos \\alpha$',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 5: Giá trị lượng giác của một góc từ 0 đến '
                        '180 độ, **Hai góc bù nhau** được xác định bởi: $\\sin(180^\\circ - \\alpha) = \\sin '
                        '\\alpha$; $\\cos(180^\\circ - \\alpha) = -\\cos \\alpha$. ($\\tan(180^\\circ - '
                        '\\alpha) = -\\tan \\alpha$; $\\cot(180^\\circ - \\alpha) = -\\cot \\alpha$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ**, nội dung/biểu thức '
                 '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$; $1 + \\tan^2 \\alpha = \\dfrac{1}{\\cos^2 '
                 '\\alpha}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hai góc bù nhau',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương',
                        'Hệ thức lượng giác cơ bản'],
            'answer': 3,
            'solution': 'Trong Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ, biểu thức/quy tắc '
                        '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$; $1 + \\tan^2 \\alpha = \\dfrac{1}{\\cos^2 '
                        '\\alpha}$ chính là nội dung của **Hệ thức lượng giác cơ bản**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho góc tù $\\alpha$ ($90^\\circ < \\alpha < 180^\\circ$) có $\\cos \\alpha = '
                 '-\\dfrac{3}{5}$. Giá trị của $\\sin \\alpha$ bằng:',
            'options': ['$\\dfrac{4}{5}$', '$-\\dfrac{4}{5}$', '$\\dfrac{2}{5}$', '$\\dfrac{3}{4}$'],
            'answer': 0,
            'solution': 'Vì $90^\\circ < \\alpha < 180^\\circ$ nên $\\sin \\alpha > 0$, suy ra $\\sin '
                        '\\alpha = \\sqrt{1 - \\cos^2 \\alpha} = \\sqrt{1 - \\dfrac{9}{25}} = '
                        '\\dfrac{4}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ** (Chương III: Hệ thức '
                 'lượng trong tam giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Nhận biết được giá trị lượng giác ($\\sin, \\cos, \\tan, \\cot$) của một góc '
                        '$\\alpha$ từ $0^\\circ$ đến $180^\\circ$ thông qua nửa đường tròn đơn vị.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ: '
                        'Nhận biết được giá trị lượng giác ($\\sin, \\cos, \\tan, \\cot$) của một góc '
                        '$\\alpha$ từ $0^\\circ$ đến $180^\\circ$ thông qua nửa đường tròn đơn vị.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho góc $\\alpha$ thỏa mãn $90^\\circ < \\alpha < 180^\\circ$.',
            'statements': ['$\\sin \\alpha > 0$.',
                           '$\\cos \\alpha < 0$.',
                           '$\\tan \\alpha > 0$.',
                           '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$.'],
            'answer': [True, True, False, True],
            'solution': 'Với góc tù $\\alpha$: a) Đúng ($\\sin \\alpha > 0$). b) Đúng ($\\cos \\alpha < 0$). '
                        'c) Sai vì $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha} < 0$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 5: Giá trị lượng giác '
                 'của một góc từ 0 đến 180 độ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được giá trị lượng giác '
                           '($\\sin, \\cos, \\tan, \\cot$) của một góc $\\alpha$ từ $0^\\circ$ đến '
                           '$180^\\circ$ thông qua nửa đường tròn đơn vị.',
                           'Quy tắc/công thức **Hai góc bù nhau** trong bài được xác định bởi: '
                           '$\\sin(180^\\circ - \\alpha) = \\sin \\alpha$; $\\cos(180^\\circ - \\alpha) = '
                           '-\\cos \\alpha$.',
                           'Trong mọi trường hợp, **Hai góc bù nhau** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ.',
                           'Với bài toán minh họa: “Cho biết $\\sin \\alpha = \\dfrac{3}{5}$ với $90^\\circ '
                           '< \\alpha < 180^\\circ$. Tính $\\cos \\alpha$ và $\\tan \\alpha$.”, lời giải '
                           'đúng là: Ta có $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = 1 - '
                           '\\left(\\dfrac{3}{5}\\right)^2 = \\dfrac{16}{25}$. Vì $90^\\circ < \\alpha < '
                           '180^\\circ$ nên $\\cos \\alpha < 0$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Giá trị lượng giác của một góc từ 0 đến '
                        '180 độ. b) **Đúng** theo công thức trọng tâm **Hai góc bù nhau** ($\\sin(180^\\circ '
                        '- \\alpha) = \\sin \\alpha$; $\\cos(180^\\circ - \\alpha) = -\\cos \\alpha$). c) '
                        '**Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Hai góc bù nhau**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ** để giải quyết '
                 'tình huống sau: Cho biết $\\sin \\alpha = \\dfrac{3}{5}$ với $90^\\circ < \\alpha < '
                 '180^\\circ$. Tính $\\cos \\alpha$ và $\\tan \\alpha$. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Ta có $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = 1 - \\left(\\dfrac{3}{5}\\right)^2 = '
                        '\\dfrac{16}{25}$. Vì $90^\\circ < \\alpha < 180^\\circ$ nên $\\cos \\alpha < 0$, '
                        'suy...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ: Ta có '
                        '$\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = 1 - \\left(\\dfrac{3}{5}\\right)^2 = '
                        '\\dfrac{16}{25}$.\n'
                        'Vì $90^\\circ < \\alpha < 180^\\circ$ nên $\\cos \\alpha < 0$, suy ra $\\cos '
                        '\\alpha = -\\dfrac{4}{5}$ và $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha} '
                        '= -\\dfrac{3}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $P = \\cos 30^\\circ + \\cos 150^\\circ + \\sin 90^\\circ$.',
            'answer': ['1'],
            'unit': None,
            'solution': 'Vì $30^\\circ$ và $150^\\circ$ bù nhau nên $\\cos 150^\\circ = -\\cos 30^\\circ$. '
                        'Do đó $P = 0 + \\sin 90^\\circ = 1$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch03-he-thuc-luong-tam-giac',
  'context_title': 'Chương III: Hệ thức lượng trong tam giác',
  'context': 'Chương III · SGK Toán 10: Hệ thức lượng trong tam giác.',
  'title': 'Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí sin và công thức diện tích)',
  'icon': '📐',
  'description': 'Vận dụng định lí côsin, định lí sin và các công thức tính diện tích tam giác để giải tam '
                 'giác và bài toán thực tế.',
  'requirements': ['Phát biểu và vận dụng được định lí côsin và định lí sin trong tam giác.',
                   'Vận dụng được các công thức tính diện tích tam giác (theo hai cạnh và góc xen giữa, theo '
                   '$R, r$, công thức Heron).',
                   'Giải được tam giác và ứng dụng vào đo đạc khoảng cách thực tế.'],
  'definition': 'Trong tam giác $ABC$ có $BC = a, CA = b, AB = c$, bán kính đường tròn ngoại tiếp $R$, bán '
                'kính đường tròn nội tiếp $r$ và nửa chu vi $p = \\dfrac{a + b + c}{2}$.',
  'theory': '1. Định lí côsin: Bình phương một cạnh của tam giác bằng tổng bình phương hai cạnh còn lại trừ '
            'đi hai lần tích của hai cạnh đó với côsin của góc xen giữa.\n'
            '2. Định lí sin: Tỉ số giữa một cạnh và sin của góc đối diện luôn bằng đường kính $2R$ của đường '
            'tròn ngoại tiếp tam giác.\n'
            '3. Năm công thức tính diện tích tam giác $S$ cho phép tìm $S$, chiều cao $h_a$, bán kính $R$ và '
            '$r$.',
  'formulas': [{'category': 'Định lí côsin, định lí sin và công thức diện tích',
                'items': [{'name': 'Định lí côsin',
                           'formula': '$a^2 = b^2 + c^2 - 2bc \\cos A \\Rightarrow \\cos A = \\dfrac{b^2 + '
                                      'c^2 - a^2}{2bc}$',
                           'note': 'Tương tự cho $b^2$ và $c^2$'},
                          {'name': 'Định lí sin',
                           'formula': '$\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = '
                                      '2R$',
                           'note': '$R$ là bán kính đường tròn ngoại tiếp'},
                          {'name': 'Các công thức diện tích',
                           'formula': '$S = \\dfrac{1}{2}bc \\sin A = \\dfrac{abc}{4R} = pr = \\sqrt{p(p - '
                                      'a)(p - b)(p - c)}$',
                           'note': '$p = \\dfrac{a + b + c}{2}$ (công thức Heron)'}]}],
  'example': 'Cho tam giác $ABC$ có $b = 5, c = 8$ và $\\widehat{A} = 60^\\circ$. Tính độ dài cạnh $a$ và '
             'diện tích $S$ của tam giác.',
  'example_answer': 'Theo định lí côsin: $a^2 = b^2 + c^2 - 2bc \\cos A = 5^2 + 8^2 - 2 \\cdot 5 \\cdot 8 '
                    '\\cdot \\cos 60^\\circ = 25 + 64 - 40 = 49 \\Rightarrow a = 7$.\n'
                    'Diện tích tam giác là $S = \\dfrac{1}{2}bc \\sin A = \\dfrac{1}{2} \\cdot 5 \\cdot 8 '
                    '\\cdot \\sin 60^\\circ = 10\\sqrt{3}$.',
  'real_life': 'Đo khoảng cách giữa hai địa điểm bị ngăn cách bởi hồ nước hoặc đồi núi mà không thể căng dây '
               'đo trực tiếp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong tam giác $ABC$ với $BC = a, CA = b, AB = c$, hệ thức nào sau đây là định lí côsin?',
            'options': ['$a^2 = b^2 + c^2 + 2bc \\cos A$',
                        '$a^2 = b^2 + c^2 - 2bc \\cos A$',
                        '$a^2 = b^2 + c^2 - bc \\cos A$',
                        '$a^2 = b^2 + c^2 - 2bc \\sin A$'],
            'answer': 1,
            'solution': 'Theo định lí côsin trong tam giác $ABC$: $a^2 = b^2 + c^2 - 2bc \\cos A$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong tam giác $ABC$ có bán kính đường tròn ngoại tiếp $R$, theo định lí sin thì tỉ số '
                 '$\\dfrac{a}{\\sin A}$ bằng:',
            'options': ['$R$', '$\\dfrac{R}{2}$', '$2R$', '$4R$'],
            'answer': 2,
            'solution': 'Theo định lí sin: $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} '
                        '= 2R$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí '
                 'sin và công thức diện tích)**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Định lí '
                 'côsin**?',
            'options': ['$\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R$',
                        '$S = \\dfrac{1}{2}bc \\sin A = \\dfrac{abc}{4R} = pr = \\sqrt{p(p - a)(p - b)(p - '
                        'c)}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$a^2 = b^2 + c^2 - 2bc \\cos A \\Rightarrow \\cos A = \\dfrac{b^2 + c^2 - '
                        'a^2}{2bc}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 6: Hệ thức lượng trong tam giác (Định lí '
                        'côsin, định lí sin và công thức diện tích), **Định lí côsin** được xác định bởi: '
                        '$a^2 = b^2 + c^2 - 2bc \\cos A \\Rightarrow \\cos A = \\dfrac{b^2 + c^2 - '
                        'a^2}{2bc}$. (Tương tự cho $b^2$ và $c^2$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí sin và công thức diện '
                 'tích)**, nội dung/biểu thức $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin '
                 'C} = 2R$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định lí sin', 'Định lí côsin', 'Các công thức diện tích', 'Mệnh đề kéo theo'],
            'answer': 0,
            'solution': 'Trong Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí sin và công thức '
                        'diện tích), biểu thức/quy tắc $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = '
                        '\\dfrac{c}{\\sin C} = 2R$ chính là nội dung của **Định lí sin**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tam giác $ABC$ có $AB = 4, AC = 6$ và $\\widehat{A} = 30^\\circ$. Diện tích của tam '
                 'giác $ABC$ bằng:',
            'options': ['$12$', '$6$', '$6\\sqrt{3}$', '$24$'],
            'answer': 1,
            'solution': 'Ta có $S = \\dfrac{1}{2} AB \\cdot AC \\cdot \\sin A = \\dfrac{1}{2} \\cdot 4 '
                        '\\cdot 6 \\cdot \\sin 30^\\circ = 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí sin và công thức '
                 'diện tích)** (Chương III: Hệ thức lượng trong tam giác), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Phát biểu và vận dụng được định lí côsin và định lí sin trong tam giác.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định '
                        'lí sin và công thức diện tích): Phát biểu và vận dụng được định lí côsin và định lí '
                        'sin trong tam giác.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác $ABC$ có ba cạnh $a = 13, b = 14, c = 15$.',
            'statements': ['Nửa chu vi của tam giác $ABC$ là $p = 21$.',
                           'Theo công thức Heron, diện tích tam giác $ABC$ bằng $84$.',
                           'Bán kính đường tròn nội tiếp tam giác $ABC$ là $r = 4$.',
                           'Góc $C$ là góc tù.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $p = \\dfrac{13 + 14 + 15}{2} = 21$. b) Đúng vì $S = \\sqrt{21 \\cdot 8 '
                        '\\cdot 7 \\cdot 6} = 84$. c) Đúng vì $r = \\dfrac{S}{p} = \\dfrac{84}{21} = 4$. d) '
                        'Sai vì $a^2 + b^2 = 169 + 196 = 365 > c^2 = 225$ nên $\\cos C > 0$, góc $C$ nhọn.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 6: Hệ thức lượng trong '
                 'tam giác (Định lí côsin, định lí sin và công thức diện tích)**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phát biểu và vận dụng được định lí '
                           'côsin và định lí sin trong tam giác.',
                           'Quy tắc/công thức **Định lí côsin** trong bài được xác định bởi: $a^2 = b^2 + '
                           'c^2 - 2bc \\cos A \\Rightarrow \\cos A = \\dfrac{b^2 + c^2 - a^2}{2bc}$.',
                           'Trong mọi trường hợp, **Định lí côsin** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí '
                           'sin và công thức diện tích).',
                           'Với bài toán minh họa: “Cho tam giác $ABC$ có $b = 5, c = 8$ và $\\widehat{A} = '
                           '60^\\circ$. Tính độ dài cạnh $a$ và diện tích $S$ của tam giác.”, lời giải đúng '
                           'là: Theo định lí côsin: $a^2 = b^2 + c^2 - 2bc \\cos A = 5^2 + 8^2 - 2 \\cdot 5 '
                           '\\cdot 8 \\cdot \\cos 60^\\circ = 25 + 64 - 40 = 49 \\Rightarrow a = 7$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Hệ thức lượng trong tam giác (Định lí '
                        'côsin, định lí sin và công thức diện tích). b) **Đúng** theo công thức trọng tâm '
                        '**Định lí côsin** ($a^2 = b^2 + c^2 - 2bc \\cos A \\Rightarrow \\cos A = '
                        '\\dfrac{b^2 + c^2 - a^2}{2bc}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ '
                        'đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung của **Định '
                        'lí côsin**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí sin và '
                 'công thức diện tích)** để giải quyết tình huống sau: Cho tam giác $ABC$ có $b = 5, c = 8$ '
                 'và $\\widehat{A} = 60^\\circ$. Tính độ dài cạnh $a$ và diện tích $S$ của tam giác. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        'Theo định lí côsin: $a^2 = b^2 + c^2 - 2bc \\cos A = 5^2 + 8^2 - 2 \\cdot 5 \\cdot '
                        '8 \\cdot \\cos 60^\\circ = 25 + 64 - 40 = 49 \\Rightarrow a = 7$. Diện tích tam...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Hệ thức lượng trong tam giác (Định lí côsin, định lí '
                        'sin và công thức diện tích): Theo định lí côsin: $a^2 = b^2 + c^2 - 2bc \\cos A = '
                        '5^2 + 8^2 - 2 \\cdot 5 \\cdot 8 \\cdot \\cos 60^\\circ = 25 + 64 - 40 = 49 '
                        '\\Rightarrow a = 7$.\n'
                        'Diện tích tam giác là $S = \\dfrac{1}{2}bc \\sin A = \\dfrac{1}{2} \\cdot 5 \\cdot '
                        '8 \\cdot \\sin 60^\\circ = 10\\sqrt{3}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tam giác $ABC$ có cạnh $BC = 10$ và góc $\\widehat{A} = 30^\\circ$. Tính bán kính $R$ '
                 'của đường tròn ngoại tiếp tam giác $ABC$.',
            'answer': ['10'],
            'unit': None,
            'solution': 'Theo định lí sin: $2R = \\dfrac{BC}{\\sin A} = \\dfrac{10}{\\sin 30^\\circ} = 20 '
                        '\\Rightarrow R = 10$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch04-vecto',
  'context_title': 'Chương IV: Vectơ',
  'context': 'Chương IV · SGK Toán 10: Vectơ.',
  'title': 'Bài 7: Các khái niệm mở đầu về vectơ',
  'icon': '➡️',
  'description': 'Nhận biết vectơ, giá và độ dài của vectơ, hai vectơ cùng phương, cùng hướng và hai vectơ '
                 'bằng nhau.',
  'requirements': ['Nhận biết được khái niệm vectơ, điểm đầu, điểm cuối, giá và độ dài của vectơ, '
                   'vectơ-không $\\overrightarrow{0}$.',
                   'Nhận biết được hai vectơ cùng phương, cùng hướng, ngược hướng và điều kiện để hai vectơ '
                   'bằng nhau.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Điều kiện bằng nhau** '
                   '($\\overrightarrow{AB} = \\overrightarrow{CD} \\Leftrightarrow \\begin{cases} '
                   '\\overrightarrow{AB}, \\overrightarrow{CD} \\text{ cùng hướng} \\\\ AB = CD '
                   '\\end{cases}$) vào giải bài tập.'],
  'definition': 'Vectơ là một đoạn thẳng có hướng. Vectơ có điểm đầu $A$, điểm cuối $B$ được kí hiệu là '
                '$\\overrightarrow{AB}$, độ dài của nó kí hiệu là $|\\overrightarrow{AB}| = AB$.',
  'theory': '1. Đường thẳng đi qua điểm đầu và điểm cuối của một vectơ gọi là giá của vectơ đó. Hai vectơ '
            'được gọi là cùng phương nếu giá của chúng song song hoặc trùng nhau.\n'
            '2. Hai vectơ cùng phương thì chỉ có thể cùng hướng hoặc ngược hướng.\n'
            '3. Hai vectơ $\\overrightarrow{a}$ và $\\overrightarrow{b}$ bằng nhau ($\\overrightarrow{a} = '
            '\\overrightarrow{b}$) nếu chúng có cùng hướng và cùng độ dài.\n'
            '4. Vectơ-không $\\overrightarrow{0}$ có độ dài bằng $0$ và cùng hướng với mọi vectơ.',
  'formulas': [{'category': 'Hai vectơ bằng nhau',
                'items': [{'name': 'Điều kiện bằng nhau',
                           'formula': '$\\overrightarrow{AB} = \\overrightarrow{CD} \\Leftrightarrow '
                                      '\\begin{cases} \\overrightarrow{AB}, \\overrightarrow{CD} \\text{ '
                                      'cùng hướng} \\\\ AB = CD \\end{cases}$',
                           'note': 'Nếu $A, B, C, D$ không thẳng hàng thì $ABDC$ là hình bình hành'}]}],
  'example': 'Cho hình bình hành $ABCD$. Tìm vectơ bằng vectơ $\\overrightarrow{AB}$ và vectơ đối hướng '
             'nhưng cùng độ dài với $\\overrightarrow{AD}$.',
  'example_answer': 'Trong hình bình hành $ABCD$, hai cạnh đối song song và bằng nhau nên:\n'
                    '- Vectơ bằng vectơ $\\overrightarrow{AB}$ là $\\overrightarrow{DC}$.\n'
                    '- Vectơ ngược hướng và cùng độ dài với $\\overrightarrow{AD}$ là $\\overrightarrow{DA}$ '
                    'và $\\overrightarrow{CB}$.',
  'real_life': 'Biểu diễn đại lượng vận tốc, gia tốc hoặc lực tác dụng (có cả độ lớn và phương, chiều) trong '
               'Vật lí.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai vectơ được gọi là bằng nhau khi và chỉ khi:',
            'options': ['Chúng cùng phương và có cùng độ dài',
                        'Chúng có cùng độ dài',
                        'Chúng cùng hướng và có cùng độ dài',
                        'Giá của chúng trùng nhau'],
            'answer': 2,
            'solution': 'Hai vectơ bằng nhau khi và chỉ khi chúng cùng hướng và cùng độ dài.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho ba điểm phân biệt $A, B, C$. Từ ba điểm này có thể lập được bao nhiêu vectơ khác '
                 'vectơ-không có điểm đầu và điểm cuối là các điểm đã cho?',
            'options': ['$3$', '$9$', '$4$', '$6$'],
            'answer': 3,
            'solution': 'Từ 3 điểm phân biệt lập được $3 \\cdot 2 = 6$ vectơ khác $\\overrightarrow{0}$: '
                        '$\\overrightarrow{AB}, \\overrightarrow{BA}, \\overrightarrow{AC}, '
                        '\\overrightarrow{CA}, \\overrightarrow{BC}, \\overrightarrow{CB}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 7: Các khái niệm mở đầu về vectơ**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Điều kiện bằng nhau**?',
            'options': ['$\\overrightarrow{AB} = \\overrightarrow{CD} \\Leftrightarrow \\begin{cases} '
                        '\\overrightarrow{AB}, \\overrightarrow{CD} \\text{ cùng hướng} \\\\ AB = CD '
                        '\\end{cases}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai',
                        '$\\overline{\\forall x \\in X, P(x)} \\equiv \\exists x \\in X, \\overline{P(x)}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 7: Các khái niệm mở đầu về vectơ, **Điều kiện '
                        'bằng nhau** được xác định bởi: $\\overrightarrow{AB} = \\overrightarrow{CD} '
                        '\\Leftrightarrow \\begin{cases} \\overrightarrow{AB}, \\overrightarrow{CD} \\text{ '
                        'cùng hướng} \\\\ AB = CD \\end{cases}$. (Nếu $A, B, C, D$ không thẳng hàng thì '
                        '$ABDC$ là hình bình hành)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Các khái niệm mở đầu về vectơ**, nội dung/biểu thức $\\overrightarrow{AB} = '
                 '\\overrightarrow{CD} \\Leftrightarrow \\begin{cases} \\overrightarrow{AB}, '
                 '\\overrightarrow{CD} \\text{ cùng hướng} \\\\ AB = CD \\end{cases}$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Mệnh đề kéo theo',
                        'Điều kiện bằng nhau',
                        'Mệnh đề tương đương',
                        'Phủ định mệnh đề có lượng từ'],
            'answer': 1,
            'solution': 'Trong Bài 7: Các khái niệm mở đầu về vectơ, biểu thức/quy tắc $\\overrightarrow{AB} '
                        '= \\overrightarrow{CD} \\Leftrightarrow \\begin{cases} \\overrightarrow{AB}, '
                        '\\overrightarrow{CD} \\text{ cùng hướng} \\\\ AB = CD \\end{cases}$ chính là nội '
                        'dung của **Điều kiện bằng nhau**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình bình hành $ABCD$. Khẳng định nào sau đây là đúng?',
            'options': ['$\\overrightarrow{AB} = \\overrightarrow{CD}$',
                        '$\\overrightarrow{AC} = \\overrightarrow{BD}$',
                        '$\\overrightarrow{AB} = \\overrightarrow{DC}$',
                        '$\\overrightarrow{AD} = \\overrightarrow{CB}$'],
            'answer': 2,
            'solution': 'Trong hình bình hành $ABCD$, hai vectơ $\\overrightarrow{AB}$ và '
                        '$\\overrightarrow{DC}$ cùng hướng và có cùng độ dài nên $\\overrightarrow{AB} = '
                        '\\overrightarrow{DC}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Các khái niệm mở đầu về vectơ** (Chương IV: Vectơ), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Nhận biết được khái niệm vectơ, điểm đầu, điểm cuối, giá và độ dài của vectơ, '
                        'vectơ-không $\\overrightarrow{0}$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 7: Các khái niệm mở đầu về vectơ: Nhận biết được khái '
                        'niệm vectơ, điểm đầu, điểm cuối, giá và độ dài của vectơ, vectơ-không '
                        '$\\overrightarrow{0}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho lục giác đều $ABCDEF$ có tâm $O$.',
            'statements': ['Vectơ $\\overrightarrow{AB}$ và vectơ $\\overrightarrow{ED}$ cùng phương.',
                           'Ta có $\\overrightarrow{AB} = \\overrightarrow{FO}$.',
                           'Độ dài $|\\overrightarrow{AD}| = 2|\\overrightarrow{AB}|$.',
                           'Hai vectơ $\\overrightarrow{OA}$ và $\\overrightarrow{OD}$ bằng nhau.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $AB // ED$. b) Đúng vì $\\overrightarrow{AB}$ và $\\overrightarrow{FO}$ '
                        'cùng hướng và có cùng độ dài bằng bán kính đường tròn ngoại tiếp. c) Đúng vì $AD = '
                        '2R = 2AB$. d) Sai vì $\\overrightarrow{OA}$ và $\\overrightarrow{OD}$ ngược hướng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 7: Các khái niệm mở đầu '
                 'về vectơ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được khái niệm vectơ, '
                           'điểm đầu, điểm cuối, giá và độ dài của vectơ, vectơ-không $\\overrightarrow{0}$.',
                           'Quy tắc/công thức **Điều kiện bằng nhau** trong bài được xác định bởi: '
                           '$\\overrightarrow{AB} = \\overrightarrow{CD} \\Leftrightarrow \\begin{cases} '
                           '\\overrightarrow{AB}, \\overrightarrow{CD} \\text{ cùng hướng} \\\\ AB = CD '
                           '\\end{cases}$.',
                           'Trong mọi trường hợp, **Điều kiện bằng nhau** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 7: Các khái niệm mở đầu về vectơ.',
                           'Với bài toán minh họa: “Cho hình bình hành $ABCD$. Tìm vectơ bằng vectơ '
                           '$\\overrightarrow{AB}$ và vectơ đối hướng nhưng cùng độ dài với '
                           '$\\overrightarrow{AD}$.”, lời giải đúng là: Trong hình bình hành $ABCD$, hai '
                           'cạnh đối song song và bằng nhau nên: - Vectơ bằng vectơ $\\overrightarrow{AB}$ '
                           'là $\\overrightarrow{DC}$. - V...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Các khái niệm mở đầu về vectơ. b) '
                        '**Đúng** theo công thức trọng tâm **Điều kiện bằng nhau** ($\\overrightarrow{AB} = '
                        '\\overrightarrow{CD} \\Leftrightarrow \\begin{cases} \\overrightarrow{AB}, '
                        '\\overrightarrow{CD} \\text{ cùng hướng} \\\\ AB = CD \\end{cases}$). c) **Sai** vì '
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Điều kiện bằng nhau**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 7: Các khái niệm mở đầu về vectơ** để giải quyết tình huống sau: '
                 'Cho hình bình hành $ABCD$. Tìm vectơ bằng vectơ $\\overrightarrow{AB}$ và vectơ đối hướng '
                 'nhưng cùng độ dài với $\\overrightarrow{AD}$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Trong hình bình hành $ABCD$, hai cạnh đối song song và bằng nhau nên: - Vectơ bằng '
                        'vectơ $\\overrightarrow{AB}$ là $\\overrightarrow{DC}$. - Vectơ ngược hướn...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Các khái niệm mở đầu về vectơ: Trong hình bình hành '
                        '$ABCD$, hai cạnh đối song song và bằng nhau nên:\n'
                        '- Vectơ bằng vectơ $\\overrightarrow{AB}$ là $\\overrightarrow{DC}$.\n'
                        '- Vectơ ngược hướng và cùng độ dài với $\\overrightarrow{AD}$ là '
                        '$\\overrightarrow{DA}$ và $\\overrightarrow{CB}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hình chữ nhật $ABCD$ có $AB = 3$ và $BC = 4$. Tính độ dài của vectơ '
                 '$\\overrightarrow{AC}$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $|\\overrightarrow{AC}| = AC = \\sqrt{AB^2 + BC^2} = \\sqrt{3^2 + 4^2} = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch04-vecto',
  'context_title': 'Chương IV: Vectơ',
  'context': 'Chương IV · SGK Toán 10: Vectơ.',
  'title': 'Bài 8: Tổng và hiệu của hai vectơ',
  'icon': '➕',
  'description': 'Thực hiện phép cộng, phép trừ vectơ theo quy tắc ba điểm, quy tắc hình bình hành và vectơ '
                 'đối.',
  'requirements': ['Vận dụng được quy tắc ba điểm và quy tắc hình bình hành để tìm tổng của hai vectơ.',
                   'Nhận biết được vectơ đối và vận dụng quy tắc hiệu hai vectơ.',
                   'Áp dụng được tính chất trung điểm đoạn thẳng và trọng tâm tam giác.'],
  'definition': 'Với ba điểm bất kì $A, B, C$, vectơ $\\overrightarrow{AC}$ được gọi là tổng của hai vectơ '
                '$\\overrightarrow{AB}$ và $\\overrightarrow{BC}$, kí hiệu $\\overrightarrow{AB} + '
                '\\overrightarrow{BC} = \\overrightarrow{AC}$.',
  'theory': '1. Quy tắc ba điểm (cộng): $\\overrightarrow{AB} + \\overrightarrow{BC} = '
            '\\overrightarrow{AC}$.\n'
            '2. Quy tắc hình bình hành: Nếu $ABCD$ là hình bình hành thì $\\overrightarrow{AB} + '
            '\\overrightarrow{AD} = \\overrightarrow{AC}$.\n'
            '3. Quy tắc hiệu: Với ba điểm $O, A, B$ bất kì, ta có $\\overrightarrow{OA} - '
            '\\overrightarrow{OB} = \\overrightarrow{BA}$.\n'
            '4. Hệ thức trung điểm và trọng tâm:\n'
            '- $I$ là trung điểm của đoạn thẳng $AB \\Leftrightarrow \\overrightarrow{IA} + '
            '\\overrightarrow{IB} = \\overrightarrow{0}$.\n'
            '- $G$ là trọng tâm của tam giác $ABC \\Leftrightarrow \\overrightarrow{GA} + '
            '\\overrightarrow{GB} + \\overrightarrow{GC} = \\overrightarrow{0}$.',
  'formulas': [{'category': 'Các quy tắc tổng và hiệu vectơ',
                'items': [{'name': 'Quy tắc ba điểm',
                           'formula': '$\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$; '
                                      '$\\overrightarrow{OA} - \\overrightarrow{OB} = \\overrightarrow{BA}$',
                           'note': 'Áp dụng cho 3 điểm bất kì'},
                          {'name': 'Quy tắc hình bình hành',
                           'formula': '$\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$',
                           'note': '$ABCD$ là hình bình hành'},
                          {'name': 'Trung điểm $I$ và Trọng tâm $G$',
                           'formula': '$\\overrightarrow{IA} + \\overrightarrow{IB} = \\overrightarrow{0}$; '
                                      '$\\overrightarrow{GA} + \\overrightarrow{GB} + \\overrightarrow{GC} = '
                                      '\\overrightarrow{0}$',
                           'note': 'Đặc trưng vectơ của trung điểm và trọng tâm'}]}],
  'example': 'Cho bốn điểm bất kì $A, B, C, D$. Chứng minh rằng $\\overrightarrow{AB} + \\overrightarrow{CD} '
             '= \\overrightarrow{AD} + \\overrightarrow{CB}$.',
  'example_answer': 'Áp dụng quy tắc ba điểm, ta có:\n'
                    '$\\overrightarrow{AB} + \\overrightarrow{CD} = (\\overrightarrow{AD} + '
                    '\\overrightarrow{DB}) + (\\overrightarrow{CB} + \\overrightarrow{BD}) = '
                    '\\overrightarrow{AD} + \\overrightarrow{CB} + (\\overrightarrow{DB} + '
                    '\\overrightarrow{BD}) = \\overrightarrow{AD} + \\overrightarrow{CB} + '
                    '\\overrightarrow{0} = \\overrightarrow{AD} + \\overrightarrow{CB}$.',
  'real_life': 'Tổng hợp hai lực đồng quy tác dụng lên một vật hoặc tính vận tốc tổng hợp của thuyền khi qua '
               'sông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với ba điểm bất kì $A, B, C$, tổng $\\overrightarrow{AB} + \\overrightarrow{BC}$ bằng:',
            'options': ['$\\overrightarrow{CA}$',
                        '$\\overrightarrow{BA}$',
                        '$\\overrightarrow{0}$',
                        '$\\overrightarrow{AC}$'],
            'answer': 3,
            'solution': 'Theo quy tắc ba điểm: $\\overrightarrow{AB} + \\overrightarrow{BC} = '
                        '\\overrightarrow{AC}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Với ba điểm bất kì $O, A, B$, hiệu $\\overrightarrow{OA} - \\overrightarrow{OB}$ bằng:',
            'options': ['$\\overrightarrow{BA}$',
                        '$\\overrightarrow{AB}$',
                        '$\\overrightarrow{OB}$',
                        '$\\overrightarrow{AO}$'],
            'answer': 0,
            'solution': 'Theo quy tắc hiệu: $\\overrightarrow{OA} - \\overrightarrow{OB} = '
                        '\\overrightarrow{BA}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 8: Tổng và hiệu của hai vectơ**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Quy tắc ba điểm**?',
            'options': ['$\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$',
                        '$\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$; '
                        '$\\overrightarrow{OA} - \\overrightarrow{OB} = \\overrightarrow{BA}$',
                        '$\\overrightarrow{IA} + \\overrightarrow{IB} = \\overrightarrow{0}$; '
                        '$\\overrightarrow{GA} + \\overrightarrow{GB} + \\overrightarrow{GC} = '
                        '\\overrightarrow{0}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 8: Tổng và hiệu của hai vectơ, **Quy tắc ba '
                        'điểm** được xác định bởi: $\\overrightarrow{AB} + \\overrightarrow{BC} = '
                        '\\overrightarrow{AC}$; $\\overrightarrow{OA} - \\overrightarrow{OB} = '
                        '\\overrightarrow{BA}$. (Áp dụng cho 3 điểm bất kì)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Tổng và hiệu của hai vectơ**, nội dung/biểu thức $\\overrightarrow{AB} + '
                 '\\overrightarrow{AD} = \\overrightarrow{AC}$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Quy tắc ba điểm',
                        'Trung điểm $I$ và Trọng tâm $G$',
                        'Quy tắc hình bình hành',
                        'Mệnh đề kéo theo'],
            'answer': 2,
            'solution': 'Trong Bài 8: Tổng và hiệu của hai vectơ, biểu thức/quy tắc $\\overrightarrow{AB} + '
                        '\\overrightarrow{AD} = \\overrightarrow{AC}$ chính là nội dung của **Quy tắc hình '
                        'bình hành**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình bình hành $ABCD$. Tổng $\\overrightarrow{AB} + \\overrightarrow{AD}$ bằng:',
            'options': ['$\\overrightarrow{BD}$',
                        '$\\overrightarrow{CA}$',
                        '$\\overrightarrow{DB}$',
                        '$\\overrightarrow{AC}$'],
            'answer': 3,
            'solution': 'Theo quy tắc hình bình hành, $\\overrightarrow{AB} + \\overrightarrow{AD} = '
                        '\\overrightarrow{AC}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Tổng và hiệu của hai vectơ** (Chương IV: Vectơ), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Vận dụng được quy tắc ba điểm và quy tắc hình bình hành để tìm tổng của hai vectơ.',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 8: Tổng và hiệu của hai vectơ: Vận dụng được quy tắc '
                        'ba điểm và quy tắc hình bình hành để tìm tổng của hai vectơ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác đều $ABC$ có cạnh bằng $a$ và $M$ là trung điểm của $BC$.',
            'statements': ['$\\overrightarrow{MB} + \\overrightarrow{MC} = \\overrightarrow{0}$.',
                           '$\\overrightarrow{AB} - \\overrightarrow{AC} = \\overrightarrow{BC}$.',
                           '$|\\overrightarrow{AB} - \\overrightarrow{AC}| = a$.',
                           '$|\\overrightarrow{AB} + \\overrightarrow{AC}| = a\\sqrt{3}$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $M$ là trung điểm $BC$. b) Sai vì $\\overrightarrow{AB} - '
                        '\\overrightarrow{AC} = \\overrightarrow{CB}$. c) Đúng vì $|\\overrightarrow{CB}| = '
                        'BC = a$. d) Đúng vì $|\\overrightarrow{AB} + \\overrightarrow{AC}| = 2AM = 2 \\cdot '
                        '\\dfrac{a\\sqrt{3}}{2} = a\\sqrt{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 8: Tổng và hiệu của hai '
                 'vectơ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Vận dụng được quy tắc ba điểm và '
                           'quy tắc hình bình hành để tìm tổng của hai vectơ.',
                           'Quy tắc/công thức **Quy tắc ba điểm** trong bài được xác định bởi: '
                           '$\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$; '
                           '$\\overrightarrow{OA} - \\overrightarrow{OB} = \\overrightarrow{BA}$.',
                           'Trong mọi trường hợp, **Quy tắc ba điểm** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 8: Tổng và hiệu của hai vectơ.',
                           'Với bài toán minh họa: “Cho bốn điểm bất kì $A, B, C, D$. Chứng minh rằng '
                           '$\\overrightarrow{AB} + \\overrightarrow{CD} = \\overrightarrow{AD} + '
                           '\\overrightarrow{CB}$.”, lời giải đúng là: Áp dụng quy tắc ba điểm, ta có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Tổng và hiệu của hai vectơ. b) **Đúng** '
                        'theo công thức trọng tâm **Quy tắc ba điểm** ($\\overrightarrow{AB} + '
                        '\\overrightarrow{BC} = \\overrightarrow{AC}$; $\\overrightarrow{OA} - '
                        '\\overrightarrow{OB} = \\overrightarrow{BA}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ '
                        'sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung '
                        'của **Quy tắc ba điểm**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 8: Tổng và hiệu của hai vectơ** để giải quyết tình huống sau: Cho '
                 'bốn điểm bất kì $A, B, C, D$. Chứng minh rằng $\\overrightarrow{AB} + \\overrightarrow{CD} '
                 '= \\overrightarrow{AD} + \\overrightarrow{CB}$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Áp dụng quy tắc ba điểm, ta có...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Tổng và hiệu của hai vectơ: Áp dụng quy tắc ba điểm, '
                        'ta có:\n'
                        '$\\overrightarrow{AB} + \\overrightarrow{CD} = (\\overrightarrow{AD} + '
                        '\\overrightarrow{DB}) + (\\overrightarrow{CB} + \\overrightarrow{BD}) = '
                        '\\overrightarrow{AD} + \\overrightarrow{CB} + (\\overrightarrow{DB} + '
                        '\\overrightarrow{BD}) = \\overrightarrow{AD} + \\overrightarrow{CB} + '
                        '\\overrightarrow{0} = \\overrightarrow{AD} + \\overrightarrow{CB}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có $AB = 6, AC = 8$. Tính độ dài của vectơ '
                 '$\\overrightarrow{AB} + \\overrightarrow{AC}$.',
            'answer': ['10'],
            'unit': None,
            'solution': 'Dựng hình chữ nhật $ABDC$, theo quy tắc hình bình hành $\\overrightarrow{AB} + '
                        '\\overrightarrow{AC} = \\overrightarrow{AD}$. Trong hình chữ nhật $ABDC$: $AD = BC '
                        '= \\sqrt{6^2 + 8^2} = 10$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch04-vecto',
  'context_title': 'Chương IV: Vectơ',
  'context': 'Chương IV · SGK Toán 10: Vectơ.',
  'title': 'Bài 9: Tích của một vectơ với một số',
  'icon': '✖️',
  'description': 'Thực hiện phép nhân một vectơ với một số, điều kiện hai vectơ cùng phương và phân tích một '
                 'vectơ theo hai vectơ không cùng phương.',
  'requirements': ['Xác định được hướng và độ dài của vectơ $k\\overrightarrow{a}$.',
                   'Vận dụng được điều kiện để hai vectơ cùng phương và ba điểm thẳng hàng.',
                   'Phân tích (biểu thị) được một vectơ theo hai vectơ không cùng phương.'],
  'definition': 'Tích của một vectơ $\\overrightarrow{a} \\neq \\overrightarrow{0}$ với một số thực $k \\neq '
                '0$ là một vectơ, kí hiệu là $k\\overrightarrow{a}$, cùng hướng với $\\overrightarrow{a}$ '
                'nếu $k > 0$, ngược hướng với $\\overrightarrow{a}$ nếu $k < 0$ và có độ dài bằng $|k| '
                '\\cdot |\\overrightarrow{a}|$.',
  'theory': '1. Với $I$ là trung điểm của đoạn thẳng $AB$ và điểm $M$ bất kì: $\\overrightarrow{MA} + '
            '\\overrightarrow{MB} = 2\\overrightarrow{MI}$.\n'
            '2. Với $G$ là trọng tâm của tam giác $ABC$ và điểm $M$ bất kì: $\\overrightarrow{MA} + '
            '\\overrightarrow{MB} + \\overrightarrow{MC} = 3\\overrightarrow{MG}$.\n'
            '3. Điều kiện cùng phương: $\\overrightarrow{b}$ cùng phương với $\\overrightarrow{a}$ '
            '($\\overrightarrow{a} \\neq \\overrightarrow{0}$) $\\Leftrightarrow$ tồn tại duy nhất số thực '
            '$k$ sao cho $\\overrightarrow{b} = k\\overrightarrow{a}$.\n'
            '4. Ba điểm phân biệt $A, B, C$ thẳng hàng $\\Leftrightarrow \\overrightarrow{AB} = '
            'k\\overrightarrow{AC}$.',
  'formulas': [{'category': 'Tích của vectơ với một số và hệ thức cơ bản',
                'items': [{'name': 'Độ dài tích số với vectơ',
                           'formula': '$|k\\overrightarrow{a}| = |k| \\cdot |\\overrightarrow{a}|$',
                           'note': '$k > 0$: cùng hướng; $k < 0$: ngược hướng'},
                          {'name': 'Hệ thức trung điểm $I$ và trọng tâm $G$',
                           'formula': '$\\overrightarrow{MA} + \\overrightarrow{MB} = '
                                      '2\\overrightarrow{MI}$; $\\overrightarrow{MA} + \\overrightarrow{MB} '
                                      '+ \\overrightarrow{MC} = 3\\overrightarrow{MG}$',
                           'note': 'Đúng với mọi điểm $M$'},
                          {'name': 'Điều kiện ba điểm thẳng hàng',
                           'formula': '$A, B, C$ thẳng hàng $\\Leftrightarrow \\overrightarrow{AB} = '
                                      'k\\overrightarrow{AC}$',
                           'note': 'Hai vectơ $\\overrightarrow{AB}, \\overrightarrow{AC}$ cùng phương'}]}],
  'example': 'Cho tam giác $ABC$ có trung tuyến $AM$. Hãy biểu thị vectơ $\\overrightarrow{AM}$ theo hai '
             'vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{AC}$.',
  'example_answer': 'Vì $M$ là trung điểm của đoạn thẳng $BC$ nên với điểm $A$, ta có:\n'
                    '$\\overrightarrow{AB} + \\overrightarrow{AC} = 2\\overrightarrow{AM} \\Rightarrow '
                    '\\overrightarrow{AM} = \\dfrac{1}{2}\\overrightarrow{AB} + '
                    '\\dfrac{1}{2}\\overrightarrow{AC}$.',
  'real_life': 'Biểu diễn gia tốc $\\overrightarrow{a}$ cùng hướng với hợp lực $\\overrightarrow{F}$ theo '
               'định luật II Newton $\\overrightarrow{F} = m\\overrightarrow{a}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho vectơ $\\overrightarrow{a} \\neq \\overrightarrow{0}$. Vectơ $-3\\overrightarrow{a}$ '
                 'có tính chất nào sau đây?',
            'options': ['Ngược hướng với $\\overrightarrow{a}$ và có độ dài bằng $3|\\overrightarrow{a}|$',
                        'Cùng hướng với $\\overrightarrow{a}$ và có độ dài bằng $3|\\overrightarrow{a}|$',
                        'Ngược hướng với $\\overrightarrow{a}$ và có độ dài bằng $-3|\\overrightarrow{a}|$',
                        'Cùng phương với $\\overrightarrow{a}$ và có độ dài bằng $|\\overrightarrow{a}|$'],
            'answer': 0,
            'solution': 'Vì $k = -3 < 0$ nên $-3\\overrightarrow{a}$ ngược hướng với $\\overrightarrow{a}$ '
                        'và có độ dài $|-3| \\cdot |\\overrightarrow{a}| = 3|\\overrightarrow{a}|$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $I$ là trung điểm của đoạn thẳng $AB$. Với điểm $M$ bất kì, hệ thức nào sau đây luôn '
                 'đúng?',
            'options': ['$\\overrightarrow{MA} + \\overrightarrow{MB} = \\overrightarrow{MI}$',
                        '$\\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$',
                        '$\\overrightarrow{MA} - \\overrightarrow{MB} = 2\\overrightarrow{MI}$',
                        '$\\overrightarrow{MA} + \\overrightarrow{MB} = \\overrightarrow{0}$'],
            'answer': 1,
            'solution': 'Theo tính chất trung điểm đoạn thẳng, $\\overrightarrow{MA} + \\overrightarrow{MB} '
                        '= 2\\overrightarrow{MI}$ với mọi điểm $M$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 9: Tích của một vectơ với một số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Độ dài tích số với vectơ**?',
            'options': ['$\\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$; '
                        '$\\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = '
                        '3\\overrightarrow{MG}$',
                        '$A, B, C$ thẳng hàng $\\Leftrightarrow \\overrightarrow{AB} = '
                        'k\\overrightarrow{AC}$',
                        '$|k\\overrightarrow{a}| = |k| \\cdot |\\overrightarrow{a}|$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 9: Tích của một vectơ với một số, **Độ dài '
                        'tích số với vectơ** được xác định bởi: $|k\\overrightarrow{a}| = |k| \\cdot '
                        '|\\overrightarrow{a}|$. ($k > 0$: cùng hướng; $k < 0$: ngược hướng)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Tích của một vectơ với một số**, nội dung/biểu thức $\\overrightarrow{MA} + '
                 '\\overrightarrow{MB} = 2\\overrightarrow{MI}$; $\\overrightarrow{MA} + '
                 '\\overrightarrow{MB} + \\overrightarrow{MC} = 3\\overrightarrow{MG}$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Độ dài tích số với vectơ',
                        'Điều kiện ba điểm thẳng hàng',
                        'Mệnh đề kéo theo',
                        'Hệ thức trung điểm $I$ và trọng tâm $G$'],
            'answer': 3,
            'solution': 'Trong Bài 9: Tích của một vectơ với một số, biểu thức/quy tắc $\\overrightarrow{MA} '
                        '+ \\overrightarrow{MB} = 2\\overrightarrow{MI}$; $\\overrightarrow{MA} + '
                        '\\overrightarrow{MB} + \\overrightarrow{MC} = 3\\overrightarrow{MG}$ chính là nội '
                        'dung của **Hệ thức trung điểm $I$ và trọng tâm $G$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tam giác $ABC$ có trọng tâm $G$ và $M$ là trung điểm của $BC$. Khẳng định nào sau đây '
                 'là đúng?',
            'options': ['$\\overrightarrow{AG} = \\dfrac{2}{3}\\overrightarrow{AM}$',
                        '$\\overrightarrow{AG} = -\\dfrac{2}{3}\\overrightarrow{AM}$',
                        '$\\overrightarrow{AG} = \\dfrac{1}{3}\\overrightarrow{AM}$',
                        '$\\overrightarrow{GA} = \\dfrac{2}{3}\\overrightarrow{AM}$'],
            'answer': 0,
            'solution': 'Trọng tâm $G$ nằm trên đoạn $AM$ và $AG = \\dfrac{2}{3}AM$, hai vectơ '
                        '$\\overrightarrow{AG}, \\overrightarrow{AM}$ cùng hướng nên $\\overrightarrow{AG} = '
                        '\\dfrac{2}{3}\\overrightarrow{AM}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Tích của một vectơ với một số** (Chương IV: Vectơ), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Xác định được hướng và độ dài của vectơ $k\\overrightarrow{a}$.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 9: Tích của một vectơ với một số: Xác định được hướng '
                        'và độ dài của vectơ $k\\overrightarrow{a}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác $ABC$ có trọng tâm $G$ và $I$ là trung điểm của cạnh $BC$.',
            'statements': ['$\\overrightarrow{AI} = \\dfrac{1}{2}\\overrightarrow{AB} + '
                           '\\dfrac{1}{2}\\overrightarrow{AC}$.',
                           '$\\overrightarrow{AG} = \\dfrac{1}{3}\\overrightarrow{AB} + '
                           '\\dfrac{1}{3}\\overrightarrow{AC}$.',
                           '$\\overrightarrow{GA} + 2\\overrightarrow{GI} = \\overrightarrow{0}$.',
                           'Với mọi điểm $O$, ta có $\\overrightarrow{OA} + \\overrightarrow{OB} + '
                           '\\overrightarrow{OC} = \\overrightarrow{OG}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $\\overrightarrow{AG} = \\dfrac{2}{3}\\overrightarrow{AI} = '
                        '\\dfrac{1}{3}(\\overrightarrow{AB} + \\overrightarrow{AC})$. c) Đúng vì '
                        '$\\overrightarrow{GB} + \\overrightarrow{GC} = 2\\overrightarrow{GI}$. d) Sai vì vế '
                        'phải phải là $3\\overrightarrow{OG}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 9: Tích của một vectơ '
                 'với một số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được hướng và độ dài của '
                           'vectơ $k\\overrightarrow{a}$.',
                           'Quy tắc/công thức **Độ dài tích số với vectơ** trong bài được xác định bởi: '
                           '$|k\\overrightarrow{a}| = |k| \\cdot |\\overrightarrow{a}|$.',
                           'Trong mọi trường hợp, **Độ dài tích số với vectơ** luôn được tính bằng công thức '
                           '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà '
                           'không cần điều kiện của Bài 9: Tích của một vectơ với một số.',
                           'Với bài toán minh họa: “Cho tam giác $ABC$ có trung tuyến $AM$. Hãy biểu thị '
                           'vectơ $\\overrightarrow{AM}$ theo hai vectơ $\\overrightarrow{AB}$ và '
                           '$\\overrightarrow{AC}$...”, lời giải đúng là: Vì $M$ là trung điểm của đoạn '
                           'thẳng $BC$ nên với điểm $A$, ta có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Tích của một vectơ với một số. b) '
                        '**Đúng** theo công thức trọng tâm **Độ dài tích số với vectơ** '
                        '($|k\\overrightarrow{a}| = |k| \\cdot |\\overrightarrow{a}|$). c) **Sai** vì $P '
                        '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Độ dài tích số với vectơ**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 9: Tích của một vectơ với một số** để giải quyết tình huống sau: '
                 'Cho tam giác $ABC$ có trung tuyến $AM$. Hãy biểu thị vectơ $\\overrightarrow{AM}$ theo hai '
                 'vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{AC}$. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Vì $M$ là trung điểm của đoạn thẳng $BC$ nên với điểm $A$, ta có...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Tích của một vectơ với một số: Vì $M$ là trung điểm '
                        'của đoạn thẳng $BC$ nên với điểm $A$, ta có:\n'
                        '$\\overrightarrow{AB} + \\overrightarrow{AC} = 2\\overrightarrow{AM} \\Rightarrow '
                        '\\overrightarrow{AM} = \\dfrac{1}{2}\\overrightarrow{AB} + '
                        '\\dfrac{1}{2}\\overrightarrow{AC}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho vectơ $\\overrightarrow{a}$ có độ dài $|\\overrightarrow{a}| = 4$. Tính độ dài của '
                 'vectơ $\\overrightarrow{u} = -5\\overrightarrow{a}$.',
            'answer': ['20'],
            'unit': None,
            'solution': 'Ta có $|\\overrightarrow{u}| = |-5| \\cdot |\\overrightarrow{a}| = 5 \\cdot 4 = '
                        '20$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch04-vecto',
  'context_title': 'Chương IV: Vectơ',
  'context': 'Chương IV · SGK Toán 10: Vectơ.',
  'title': 'Bài 10: Vectơ trong mặt phẳng tọa độ',
  'icon': '🌐',
  'description': 'Xác định tọa độ của điểm và vectơ, tính toán các phép toán vectơ theo tọa độ trong mặt '
                 'phẳng Oxy.',
  'requirements': ['Xác định được tọa độ của một điểm và tọa độ của một vectơ trên mặt phẳng tọa độ $Oxy$.',
                   'Vận dụng được biểu thức tọa độ của các phép toán vectơ, tọa độ trung điểm đoạn thẳng và '
                   'tọa độ trọng tâm tam giác.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Vectơ $\\overrightarrow{AB}$ và độ dài** '
                   '($\\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$; $AB = \\sqrt{(x_B - x_A)^2 + (y_B - '
                   'y_A)^2}$) vào giải bài tập.'],
  'definition': 'Trên mặt phẳng tọa độ $Oxy$ với hai vectơ đơn vị $\\overrightarrow{i}, \\overrightarrow{j}$ '
                'trên hai trục $Ox, Oy$: $\\overrightarrow{u} = (x; y) \\Leftrightarrow \\overrightarrow{u} '
                '= x\\overrightarrow{i} + y\\overrightarrow{j}$. Điểm $M(x; y) \\Leftrightarrow '
                '\\overrightarrow{OM} = x\\overrightarrow{i} + y\\overrightarrow{j}$.',
  'theory': '1. Cho hai điểm $A(x_A; y_A)$ và $B(x_B; y_B)$, ta có $\\overrightarrow{AB} = (x_B - x_A; y_B - '
            'y_A)$ và độ dài $AB = |\\overrightarrow{AB}| = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.\n'
            "2. Cho $\\overrightarrow{u} = (x; y)$ và $\\overrightarrow{v} = (x'; y')$: $\\overrightarrow{u} "
            "\\pm \\overrightarrow{v} = (x \\pm x'; y \\pm y')$; $k\\overrightarrow{u} = (kx; ky)$.\n"
            '3. Tọa độ trung điểm $I$ của $AB$: $x_I = \\dfrac{x_A + x_B}{2}, y_I = \\dfrac{y_A + y_B}{2}$. '
            'Tọa độ trọng tâm $G$ của $\\triangle ABC$: $x_G = \\dfrac{x_A + x_B + x_C}{3}, y_G = '
            '\\dfrac{y_A + y_B + y_C}{3}$.',
  'formulas': [{'category': 'Biểu thức tọa độ của vectơ và điểm',
                'items': [{'name': 'Vectơ $\\overrightarrow{AB}$ và độ dài',
                           'formula': '$\\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$; $AB = \\sqrt{(x_B - '
                                      'x_A)^2 + (y_B - y_A)^2}$',
                           'note': 'Lấy tọa độ điểm cuối trừ tọa độ điểm đầu'},
                          {'name': 'Các phép toán tọa độ',
                           'formula': "$\\overrightarrow{u} + \\overrightarrow{v} = (x + x'; y + y')$; "
                                      '$k\\overrightarrow{u} = (kx; ky)$',
                           'note': 'Hai vectơ bằng nhau khi hoành độ bằng hoành độ, tung độ bằng tung độ'},
                          {'name': 'Trung điểm $I$ và Trọng tâm $G$',
                           'formula': '$I\\left(\\dfrac{x_A + x_B}{2}; \\dfrac{y_A + y_B}{2}\\right)$; '
                                      '$G\\left(\\dfrac{x_A + x_B + x_C}{3}; \\dfrac{y_A + y_B + '
                                      'y_C}{3}\\right)$',
                           'note': 'Trung bình cộng tọa độ các đỉnh'}]}],
  'example': 'Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; -2)$ và $B(5; 4)$. Tìm tọa độ vectơ '
             '$\\overrightarrow{AB}$ và tọa độ trung điểm $I$ của đoạn thẳng $AB$.',
  'example_answer': 'Ta có $\\overrightarrow{AB} = (5 - 1; 4 - (-2)) = (4; 6)$.\n'
                    'Tọa độ trung điểm $I$ của đoạn thẳng $AB$ là $x_I = \\dfrac{1 + 5}{2} = 3$ và $y_I = '
                    '\\dfrac{-2 + 4}{2} = 1$, vậy $I(3; 1)$.',
  'real_life': 'Định vị tọa độ máy bay, tàu thủy trên bản đồ số và tính khoảng cách di chuyển giữa hai vị '
               'trí GPS.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho $\\overrightarrow{u} = 3\\overrightarrow{i} - '
                 '4\\overrightarrow{j}$. Tọa độ của vectơ $\\overrightarrow{u}$ là:',
            'options': ['$(-4; 3)$', '$(3; -4)$', '$(3; 4)$', '$(-3; 4)$'],
            'answer': 1,
            'solution': 'Vì $\\overrightarrow{u} = 3\\overrightarrow{i} - 4\\overrightarrow{j}$ nên '
                        '$\\overrightarrow{u} = (3; -4)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai điểm $A(2; 1)$ và $B(5; -3)$. Tọa độ của vectơ $\\overrightarrow{AB}$ là:',
            'options': ['$(-3; 4)$', '$(7; -2)$', '$(3; -4)$', '$(3; 4)$'],
            'answer': 2,
            'solution': 'Ta có $\\overrightarrow{AB} = (5 - 2; -3 - 1) = (3; -4)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 10: Vectơ trong mặt phẳng tọa độ**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Vectơ $\\overrightarrow{AB}$ và độ dài**?',
            'options': ["$\\overrightarrow{u} + \\overrightarrow{v} = (x + x'; y + y')$; "
                        '$k\\overrightarrow{u} = (kx; ky)$',
                        '$I\\left(\\dfrac{x_A + x_B}{2}; \\dfrac{y_A + y_B}{2}\\right)$; '
                        '$G\\left(\\dfrac{x_A + x_B + x_C}{3}; \\dfrac{y_A + y_B + y_C}{3}\\right)$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$\\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$; $AB = \\sqrt{(x_B - x_A)^2 + (y_B '
                        '- y_A)^2}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 10: Vectơ trong mặt phẳng tọa độ, **Vectơ '
                        '$\\overrightarrow{AB}$ và độ dài** được xác định bởi: $\\overrightarrow{AB} = (x_B '
                        '- x_A; y_B - y_A)$; $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$. (Lấy tọa độ điểm '
                        'cuối trừ tọa độ điểm đầu)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Vectơ trong mặt phẳng tọa độ**, nội dung/biểu thức $\\overrightarrow{u} + '
                 "\\overrightarrow{v} = (x + x'; y + y')$; $k\\overrightarrow{u} = (kx; ky)$ là quy tắc hoặc "
                 'công thức của mục nào sau đây?',
            'options': ['Các phép toán tọa độ',
                        'Vectơ $\\overrightarrow{AB}$ và độ dài',
                        'Trung điểm $I$ và Trọng tâm $G$',
                        'Mệnh đề kéo theo'],
            'answer': 0,
            'solution': 'Trong Bài 10: Vectơ trong mặt phẳng tọa độ, biểu thức/quy tắc $\\overrightarrow{u} '
                        "+ \\overrightarrow{v} = (x + x'; y + y')$; $k\\overrightarrow{u} = (kx; ky)$ chính "
                        'là nội dung của **Các phép toán tọa độ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong mặt phẳng $Oxy$, cho tam giác $ABC$ có $A(1; 2), B(4; -1), C(1; 5)$. Tọa độ trọng '
                 'tâm $G$ của tam giác $ABC$ là:',
            'options': ['$(3; 3)$', '$(2; 2)$', '$(6; 6)$', '$(2; 3)$'],
            'answer': 1,
            'solution': 'Ta có $x_G = \\dfrac{1 + 4 + 1}{3} = 2$ và $y_G = \\dfrac{2 + (-1) + 5}{3} = 2$, '
                        'vậy $G(2; 2)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Vectơ trong mặt phẳng tọa độ** (Chương IV: Vectơ), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Xác định được tọa độ của một điểm và tọa độ của một vectơ trên mặt phẳng tọa độ '
                        '$Oxy$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 10: Vectơ trong mặt phẳng tọa độ: Xác định được tọa độ '
                        'của một điểm và tọa độ của một vectơ trên mặt phẳng tọa độ $Oxy$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\overrightarrow{a} = (2; -1)$, '
                 '$\\overrightarrow{b} = (3; 4)$ và hai điểm $M(1; 3), N(5; 0)$.',
            'statements': ['Tổng hai vectơ $\\overrightarrow{a} + \\overrightarrow{b}$ có tọa độ là $(5; '
                           '3)$.',
                           'Độ dài của vectơ $\\overrightarrow{b}$ bằng $5$.',
                           'Hai vectơ $\\overrightarrow{a}$ và $\\overrightarrow{b}$ cùng phương.',
                           'Khoảng cách giữa hai điểm $M$ và $N$ bằng $5$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $(2 + 3; -1 + 4) = (5; 3)$. b) Đúng vì $|\\overrightarrow{b}| = '
                        '\\sqrt{3^2 + 4^2} = 5$. c) Sai vì $\\dfrac{2}{3} \\neq \\dfrac{-1}{4}$. d) Đúng vì '
                        '$\\overrightarrow{MN} = (4; -3) \\Rightarrow MN = \\sqrt{4^2 + (-3)^2} = 5$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 10: Vectơ trong mặt '
                 'phẳng tọa độ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được tọa độ của một điểm '
                           'và tọa độ của một vectơ trên mặt phẳng tọa độ $Oxy$.',
                           'Quy tắc/công thức **Vectơ $\\overrightarrow{AB}$ và độ dài** trong bài được xác '
                           'định bởi: $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$; $AB = \\sqrt{(x_B - '
                           'x_A)^2 + (y_B - y_A)^2}$.',
                           'Trong mọi trường hợp, **Vectơ $\\overrightarrow{AB}$ và độ dài** luôn được tính '
                           'bằng công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề '
                           'kéo theo) mà không cần điều kiện của Bài 10: Vectơ trong mặt phẳng tọa độ.',
                           'Với bài toán minh họa: “Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; -2)$ và '
                           '$B(5; 4)$. Tìm tọa độ vectơ $\\overrightarrow{AB}$ và tọa độ trung điểm $I$ của '
                           'đoạn...”, lời giải đúng là: Ta có $\\overrightarrow{AB} = (5 - 1; 4 - (-2)) = '
                           '(4; 6)$. Tọa độ trung điểm $I$ của đoạn thẳng $AB$ là $x_I = \\dfrac{1 + 5}{2} = '
                           '3$ và $y_I = \\dfrac{-2 + 4}{2} = 1$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Vectơ trong mặt phẳng tọa độ. b) '
                        '**Đúng** theo công thức trọng tâm **Vectơ $\\overrightarrow{AB}$ và độ dài** '
                        '($\\overrightarrow{AB} = (x_B - x_A; y_B - y_A)$; $AB = \\sqrt{(x_B - x_A)^2 + (y_B '
                        '- y_A)^2}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Vectơ $\\overrightarrow{AB}$ '
                        'và độ dài**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 10: Vectơ trong mặt phẳng tọa độ** để giải quyết tình huống sau: '
                 'Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; -2)$ và $B(5; 4)$. Tìm tọa độ vectơ '
                 '$\\overrightarrow{AB}$ và tọa độ trung điểm $I$ của đoạn thẳng $AB$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        'Ta có $\\overrightarrow{AB} = (5 - 1; 4 - (-2)) = (4; 6)$. Tọa độ trung điểm $I$ '
                        'của đoạn thẳng $AB$ là $x_I = \\dfrac{1 + 5}{2} = 3$ và $y_I = \\dfrac{-2 + 4}{2} = '
                        '1$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Vectơ trong mặt phẳng tọa độ: Ta có '
                        '$\\overrightarrow{AB} = (5 - 1; 4 - (-2)) = (4; 6)$.\n'
                        'Tọa độ trung điểm $I$ của đoạn thẳng $AB$ là $x_I = \\dfrac{1 + 5}{2} = 3$ và $y_I '
                        '= \\dfrac{-2 + 4}{2} = 1$, vậy $I(3; 1)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho hình bình hành $ABCD$ biết $A(1; 2), B(3; 5), C(6; 4)$. '
                 'Tìm tổng hoành độ và tung độ của đỉnh $D$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Gọi $D(x; y)$. Vì $ABCD$ là hình bình hành nên $\\overrightarrow{AB} = '
                        '\\overrightarrow{DC} \\Leftrightarrow (2; 3) = (6 - x; 4 - y) \\Rightarrow x = 4, y '
                        '= 1$. Tổng $x + y = 4 + 1 = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch04-vecto',
  'context_title': 'Chương IV: Vectơ',
  'context': 'Chương IV · SGK Toán 10: Vectơ.',
  'title': 'Bài 11: Tích vô hướng của hai vectơ',
  'icon': '⚡',
  'description': 'Xác định góc giữa hai vectơ, tính tích vô hướng theo định nghĩa và theo tọa độ, ứng dụng '
                 'chứng minh vuông góc.',
  'requirements': ['Xác định được góc giữa hai vectơ $(\\overrightarrow{a}, \\overrightarrow{b})$ từ '
                   '$0^\\circ$ đến $180^\\circ$.',
                   'Tính được tích vô hướng của hai vectơ theo định nghĩa hình học và theo biểu thức tọa độ.',
                   'Vận dụng điều kiện $\\overrightarrow{a} \\perp \\overrightarrow{b} \\Leftrightarrow '
                   '\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$ để giải toán.'],
  'definition': 'Tích vô hướng của hai vectơ khác vectơ-không $\\overrightarrow{a}$ và $\\overrightarrow{b}$ '
                'là một số thực, kí hiệu là $\\overrightarrow{a} \\cdot \\overrightarrow{b}$, được xác định '
                'bởi công thức: $\\overrightarrow{a} \\cdot \\overrightarrow{b} = |\\overrightarrow{a}| '
                '\\cdot |\\overrightarrow{b}| \\cdot \\cos(\\overrightarrow{a}, \\overrightarrow{b})$.',
  'theory': '1. Điều kiện vuông góc: Với hai vectơ $\\overrightarrow{a}, \\overrightarrow{b}$ khác '
            '$\\overrightarrow{0}$, ta có $\\overrightarrow{a} \\perp \\overrightarrow{b} \\Leftrightarrow '
            '\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$.\n'
            '2. Bình phương vô hướng của một vectơ bằng bình phương độ dài của nó: $\\overrightarrow{a}^2 = '
            '|\\overrightarrow{a}|^2$.\n'
            "3. Biểu thức tọa độ: Cho $\\overrightarrow{a} = (x; y)$ và $\\overrightarrow{b} = (x'; y')$, "
            "khi đó $\\overrightarrow{a} \\cdot \\overrightarrow{b} = xx' + yy'$.",
  'formulas': [{'category': 'Công thức tích vô hướng và góc giữa hai vectơ',
                'items': [{'name': 'Định nghĩa tích vô hướng',
                           'formula': '$\\overrightarrow{a} \\cdot \\overrightarrow{b} = '
                                      '|\\overrightarrow{a}| \\cdot |\\overrightarrow{b}| \\cdot '
                                      '\\cos(\\overrightarrow{a}, \\overrightarrow{b})$',
                           'note': 'Kết quả của tích vô hướng là một số thực'},
                          {'name': 'Biểu thức tọa độ',
                           'formula': "$\\overrightarrow{a} \\cdot \\overrightarrow{b} = xx' + yy'$; "
                                      "$\\overrightarrow{a} \\perp \\overrightarrow{b} \\Leftrightarrow xx' "
                                      "+ yy' = 0$",
                           'note': "Với $\\overrightarrow{a} = (x; y), \\overrightarrow{b} = (x'; y')$"},
                          {'name': 'Côsin góc giữa hai vectơ',
                           'formula': '$\\cos(\\overrightarrow{a}, \\overrightarrow{b}) = '
                                      '\\dfrac{\\overrightarrow{a} \\cdot '
                                      '\\overrightarrow{b}}{|\\overrightarrow{a}| \\cdot '
                                      "|\\overrightarrow{b}|} = \\dfrac{xx' + yy'}{\\sqrt{x^2 + "
                                      "y^2}\\sqrt{x'^2 + y'^2}}$",
                           'note': 'Với $\\overrightarrow{a}, \\overrightarrow{b} \\neq '
                                   '\\overrightarrow{0}$'}]}],
  'example': 'Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\overrightarrow{a} = (1; 2)$ và '
             '$\\overrightarrow{b} = (4; -2)$. Tính $\\overrightarrow{a} \\cdot \\overrightarrow{b}$ và góc '
             'giữa hai vectơ.',
  'example_answer': 'Ta có $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 1 \\cdot 4 + 2 \\cdot (-2) = 4 '
                    '- 4 = 0$.\n'
                    'Vì $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$ nên $\\overrightarrow{a} \\perp '
                    '\\overrightarrow{b}$, suy ra góc giữa hai vectơ bằng $90^\\circ$.',
  'real_life': 'Tính công cơ học $A = \\overrightarrow{F} \\cdot \\overrightarrow{d} = F \\cdot d \\cdot '
               '\\cos \\alpha$ khi lực $\\overrightarrow{F}$ làm vật dịch chuyển một độ dời '
               '$\\overrightarrow{d}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Cho hai vectơ $\\overrightarrow{a} = (x; y)$ và $\\overrightarrow{b} = (x'; y')$. Biểu "
                 'thức tọa độ của tích vô hướng $\\overrightarrow{a} \\cdot \\overrightarrow{b}$ là:',
            'options': ["$xx' - yy'$", "$xy' + x'y$", "$xx' + yy'$", "$\\sqrt{xx' + yy'}$"],
            'answer': 2,
            'solution': 'Theo công thức tọa độ của tích vô hướng: $\\overrightarrow{a} \\cdot '
                        "\\overrightarrow{b} = xx' + yy'$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai vectơ khác vectơ-không $\\overrightarrow{a}$ và $\\overrightarrow{b}$ vuông góc với '
                 'nhau khi và chỉ khi:',
            'options': ['$\\overrightarrow{a} \\cdot \\overrightarrow{b} = 1$',
                        '$\\overrightarrow{a} + \\overrightarrow{b} = \\overrightarrow{0}$',
                        '$|\\overrightarrow{a}| = |\\overrightarrow{b}|$',
                        '$\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$'],
            'answer': 3,
            'solution': 'Hai vectơ vuông góc khi và chỉ khi tích vô hướng của chúng bằng $0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 11: Tích vô hướng của hai vectơ**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Định nghĩa tích vô hướng**?',
            'options': ['$\\overrightarrow{a} \\cdot \\overrightarrow{b} = |\\overrightarrow{a}| \\cdot '
                        '|\\overrightarrow{b}| \\cdot \\cos(\\overrightarrow{a}, \\overrightarrow{b})$',
                        "$\\overrightarrow{a} \\cdot \\overrightarrow{b} = xx' + yy'$; $\\overrightarrow{a} "
                        "\\perp \\overrightarrow{b} \\Leftrightarrow xx' + yy' = 0$",
                        '$\\cos(\\overrightarrow{a}, \\overrightarrow{b}) = \\dfrac{\\overrightarrow{a} '
                        '\\cdot \\overrightarrow{b}}{|\\overrightarrow{a}| \\cdot |\\overrightarrow{b}|} = '
                        "\\dfrac{xx' + yy'}{\\sqrt{x^2 + y^2}\\sqrt{x'^2 + y'^2}}$",
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 11: Tích vô hướng của hai vectơ, **Định nghĩa '
                        'tích vô hướng** được xác định bởi: $\\overrightarrow{a} \\cdot \\overrightarrow{b} '
                        '= |\\overrightarrow{a}| \\cdot |\\overrightarrow{b}| \\cdot '
                        '\\cos(\\overrightarrow{a}, \\overrightarrow{b})$. (Kết quả của tích vô hướng là một '
                        'số thực)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Tích vô hướng của hai vectơ**, nội dung/biểu thức $\\overrightarrow{a} '
                 "\\cdot \\overrightarrow{b} = xx' + yy'$; $\\overrightarrow{a} \\perp \\overrightarrow{b} "
                 "\\Leftrightarrow xx' + yy' = 0$ là quy tắc hoặc công thức của mục nào sau đây?",
            'options': ['Định nghĩa tích vô hướng',
                        'Biểu thức tọa độ',
                        'Côsin góc giữa hai vectơ',
                        'Mệnh đề kéo theo'],
            'answer': 1,
            'solution': 'Trong Bài 11: Tích vô hướng của hai vectơ, biểu thức/quy tắc $\\overrightarrow{a} '
                        "\\cdot \\overrightarrow{b} = xx' + yy'$; $\\overrightarrow{a} \\perp "
                        "\\overrightarrow{b} \\Leftrightarrow xx' + yy' = 0$ chính là nội dung của **Biểu "
                        'thức tọa độ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tam giác đều $ABC$ có cạnh bằng $4$. Giá trị của tích vô hướng $\\overrightarrow{AB} '
                 '\\cdot \\overrightarrow{AC}$ bằng:',
            'options': ['$16$', '$-8$', '$8$', '$8\\sqrt{3}$'],
            'answer': 2,
            'solution': 'Hai vectơ $\\overrightarrow{AB}, \\overrightarrow{AC}$ có cùng điểm đầu $A$ nên '
                        '$(\\overrightarrow{AB}, \\overrightarrow{AC}) = \\widehat{BAC} = 60^\\circ$. Suy ra '
                        '$\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = 4 \\cdot 4 \\cdot \\cos '
                        '60^\\circ = 8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Tích vô hướng của hai vectơ** (Chương IV: Vectơ), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Xác định được góc giữa hai vectơ $(\\overrightarrow{a}, \\overrightarrow{b})$ từ '
                        '$0^\\circ$ đến $180^\\circ$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 11: Tích vô hướng của hai vectơ: Xác định được góc '
                        'giữa hai vectơ $(\\overrightarrow{a}, \\overrightarrow{b})$ từ $0^\\circ$ đến '
                        '$180^\\circ$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\overrightarrow{u} = (3; 1)$ và '
                 '$\\overrightarrow{v} = (1; 2)$.',
            'statements': ['Tích vô hướng $\\overrightarrow{u} \\cdot \\overrightarrow{v} = 5$.',
                           'Độ dài của hai vectơ lần lượt là $|\\overrightarrow{u}| = \\sqrt{10}$ và '
                           '$|\\overrightarrow{v}| = \\sqrt{5}$.',
                           'Góc giữa hai vectơ $\\overrightarrow{u}$ và $\\overrightarrow{v}$ bằng '
                           '$45^\\circ$.',
                           'Vectơ $\\overrightarrow{w} = (2; -6)$ vuông góc với vectơ '
                           '$\\overrightarrow{v}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $3 \\cdot 1 + 1 \\cdot 2 = 5$. b) Đúng. c) Đúng vì '
                        '$\\cos(\\overrightarrow{u}, \\overrightarrow{v}) = \\dfrac{5}{\\sqrt{10}\\sqrt{5}} '
                        '= \\dfrac{\\sqrt{2}}{2} \\Rightarrow (\\overrightarrow{u}, \\overrightarrow{v}) = '
                        '45^\\circ$. d) Sai vì $\\overrightarrow{w} \\cdot \\overrightarrow{v} = 2 - 12 = '
                        '-10 \\neq 0$ (mà $\\overrightarrow{w} \\perp \\overrightarrow{u}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 11: Tích vô hướng của '
                 'hai vectơ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được góc giữa hai vectơ '
                           '$(\\overrightarrow{a}, \\overrightarrow{b})$ từ $0^\\circ$ đến $180^\\circ$.',
                           'Quy tắc/công thức **Định nghĩa tích vô hướng** trong bài được xác định bởi: '
                           '$\\overrightarrow{a} \\cdot \\overrightarrow{b} = |\\overrightarrow{a}| \\cdot '
                           '|\\overrightarrow{b}| \\cdot \\cos(\\overrightarrow{a}, \\overrightarrow{b})$.',
                           'Trong mọi trường hợp, **Định nghĩa tích vô hướng** luôn được tính bằng công thức '
                           '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà '
                           'không cần điều kiện của Bài 11: Tích vô hướng của hai vectơ.',
                           'Với bài toán minh họa: “Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ '
                           '$\\overrightarrow{a} = (1; 2)$ và $\\overrightarrow{b} = (4; -2)$. Tính '
                           '$\\overrightarrow{a} \\cdot \\overrightarrow{b}$...”, lời giải đúng là: Ta có '
                           '$\\overrightarrow{a} \\cdot \\overrightarrow{b} = 1 \\cdot 4 + 2 \\cdot (-2) = 4 '
                           '- 4 = 0$. Vì $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Tích vô hướng của hai vectơ. b) '
                        '**Đúng** theo công thức trọng tâm **Định nghĩa tích vô hướng** '
                        '($\\overrightarrow{a} \\cdot \\overrightarrow{b} = |\\overrightarrow{a}| \\cdot '
                        '|\\overrightarrow{b}| \\cdot \\cos(\\overrightarrow{a}, \\overrightarrow{b})$). c) '
                        '**Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Định nghĩa tích vô hướng**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 11: Tích vô hướng của hai vectơ** để giải quyết tình huống sau: '
                 'Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\overrightarrow{a} = (1; 2)$ và '
                 '$\\overrightarrow{b} = (4; -2)$. Tính $\\overrightarrow{a} \\cdot \\overrightarrow{b}$ và '
                 'góc giữa hai vectơ. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 1 \\cdot 4 + 2 \\cdot (-2) '
                        '= 4 - 4 = 0$. Vì $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$ nên '
                        '$\\overrightarrow{a} \\perp \\overrightarrow{b}$...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Tích vô hướng của hai vectơ: Ta có '
                        '$\\overrightarrow{a} \\cdot \\overrightarrow{b} = 1 \\cdot 4 + 2 \\cdot (-2) = 4 - '
                        '4 = 0$.\n'
                        'Vì $\\overrightarrow{a} \\cdot \\overrightarrow{b} = 0$ nên $\\overrightarrow{a} '
                        '\\perp \\overrightarrow{b}$, suy ra góc giữa hai vectơ bằng $90^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm giá trị của tham số $m$ để hai vectơ $\\overrightarrow{a} = (3; -2)$ và '
                 '$\\overrightarrow{b} = (m; 6)$ vuông góc với nhau.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Để $\\overrightarrow{a} \\perp \\overrightarrow{b}$ thì $\\overrightarrow{a} \\cdot '
                        '\\overrightarrow{b} = 0 \\Leftrightarrow 3m - 12 = 0 \\Leftrightarrow m = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch05-thong-ke',
  'context_title': 'Chương V: Các số đặc trưng của mẫu số liệu không ghép nhóm',
  'context': 'Chương V · SGK Toán 10: Các số đặc trưng của mẫu số liệu không ghép nhóm.',
  'title': 'Bài 12: Số gần đúng và sai số',
  'icon': '🎯',
  'description': 'Nhận biết số gần đúng, tính sai số tuyệt đối, sai số tương đối và quy tròn số gần đúng.',
  'requirements': ['Hiểu được khái niệm số gần đúng, sai số tuyệt đối $\\Delta_a$, độ chính xác $d$ và sai '
                   'số tương đối $\\delta_a$.',
                   'Thực hiện được việc quy tròn số đúng và quy tròn số gần đúng căn cứ vào độ chính xác cho '
                   'trước.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Sai số tuyệt đối và độ chính xác** '
                   '($\\Delta_a = |\\bar{a} - a| \\le d \\Leftrightarrow a - d \\le \\bar{a} \\le a + d$) '
                   'vào giải bài tập.'],
  'definition': 'Nếu $a$ là số gần đúng của số đúng $\\bar{a}$ thì $\\Delta_a = |\\bar{a} - a|$ được gọi là '
                'sai số tuyệt đối của số gần đúng $a$. Nếu $\\Delta_a \\le d$ thì $d$ được gọi là độ chính '
                'xác của số gần đúng, viết là $\\bar{a} = a \\pm d$.',
  'theory': '1. Sai số tương đối của số gần đúng $a$ là tỉ số $\\delta_a = \\dfrac{\\Delta_a}{|a|}$. Nếu '
            '$\\bar{a} = a \\pm d$ thì $\\delta_a \\le \\dfrac{d}{|a|}$. Sai số tương đối càng nhỏ thì chất '
            'lượng phép đo càng cao.\n'
            '2. Quy tắc làm tròn số gần đúng với độ chính xác $d$: Nếu $d$ là số ở hàng nào thì ta quy tròn '
            'số gần đúng $a$ đến hàng lớn hơn kế tiếp (ví dụ: $d = 0,01$ ở hàng phần trăm thì quy tròn $a$ '
            'đến hàng phần mười).',
  'formulas': [{'category': 'Công thức sai số',
                'items': [{'name': 'Sai số tuyệt đối và độ chính xác',
                           'formula': '$\\Delta_a = |\\bar{a} - a| \\le d \\Leftrightarrow a - d \\le '
                                      '\\bar{a} \\le a + d$',
                           'note': 'Kí hiệu: $\\bar{a} = a \\pm d$'},
                          {'name': 'Sai số tương đối',
                           'formula': '$\\delta_a = \\dfrac{\\Delta_a}{|a|} \\le \\dfrac{d}{|a|}$',
                           'note': 'Thường viết dưới dạng phần trăm'}]}],
  'example': 'Cho số gần đúng $a = 23,476$ với độ chính xác $d = 0,02$. Hãy viết số quy tròn của số $a$.',
  'example_answer': 'Vì độ chính xác $d = 0,02$ đến hàng phần trăm nên ta quy tròn số $a = 23,476$ đến hàng '
                    'phần mười.\n'
                    'Chữ số sau hàng phần mười là $7 \\ge 5$ nên số quy tròn của $a$ là $23,5$.',
  'real_life': 'Đánh giá độ chính xác của các thiết bị đo lường trong phòng thí nghiệm, trắc địa và gia công '
               'cơ khí chính xác.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu $a$ là số gần đúng của số đúng $\\bar{a}$ thì sai số tuyệt đối $\\Delta_a$ được xác '
                 'định bởi công thức:',
            'options': ['$\\Delta_a = \\bar{a} - a$',
                        '$\\Delta_a = \\dfrac{|\\bar{a} - a|}{|a|}$',
                        '$\\Delta_a = \\bar{a} + a$',
                        '$\\Delta_a = |\\bar{a} - a|$'],
            'answer': 3,
            'solution': 'Theo định nghĩa, sai số tuyệt đối là $\\Delta_a = |\\bar{a} - a|$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Quy tròn số $15,368$ đến hàng phần mười ta được số:',
            'options': ['$15,4$', '$15,3$', '$15,37$', '$15$'],
            'answer': 0,
            'solution': 'Chữ số ở hàng phần trăm là $6 \\ge 5$ nên quy tròn đến hàng phần mười được $15,4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 12: Số gần đúng và sai số**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Sai số tuyệt đối và độ chính xác**?',
            'options': ['$\\delta_a = \\dfrac{\\Delta_a}{|a|} \\le \\dfrac{d}{|a|}$',
                        '$\\Delta_a = |\\bar{a} - a| \\le d \\Leftrightarrow a - d \\le \\bar{a} \\le a + d$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 12: Số gần đúng và sai số, **Sai số tuyệt đối '
                        'và độ chính xác** được xác định bởi: $\\Delta_a = |\\bar{a} - a| \\le d '
                        '\\Leftrightarrow a - d \\le \\bar{a} \\le a + d$. (Kí hiệu: $\\bar{a} = a \\pm d$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Số gần đúng và sai số**, nội dung/biểu thức $\\delta_a = '
                 '\\dfrac{\\Delta_a}{|a|} \\le \\dfrac{d}{|a|}$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Sai số tuyệt đối và độ chính xác',
                        'Mệnh đề kéo theo',
                        'Sai số tương đối',
                        'Mệnh đề tương đương'],
            'answer': 2,
            'solution': 'Trong Bài 12: Số gần đúng và sai số, biểu thức/quy tắc $\\delta_a = '
                        '\\dfrac{\\Delta_a}{|a|} \\le \\dfrac{d}{|a|}$ chính là nội dung của **Sai số tương '
                        'đối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho số gần đúng $a = 3456$ với độ chính xác $d = 30$. Số quy tròn của số $a$ là:',
            'options': ['$3460$', '$3400$', '$3000$', '$3500$'],
            'answer': 3,
            'solution': 'Vì $d = 30$ ở hàng chục nên ta quy tròn $a$ đến hàng trăm. Chữ số hàng chục là $5$ '
                        'nên quy tròn thành $3500$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Số gần đúng và sai số** (Chương V: Các số đặc trưng của mẫu số liệu '
                 'không ghép nhóm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Hiểu được khái niệm số gần đúng, sai số tuyệt đối $\\Delta_a$, độ chính xác $d$ và '
                        'sai số tương đối $\\delta_a$.',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 12: Số gần đúng và sai số: Hiểu được khái niệm số gần '
                        'đúng, sai số tuyệt đối $\\Delta_a$, độ chính xác $d$ và sai số tương đối '
                        '$\\delta_a$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Độ dài một cây cầu được đo và ghi nhận là $\\bar{l} = 250\\text{ m} \\pm 0,5\\text{ m}$.',
            'statements': ['Số gần đúng của độ dài cây cầu là $l = 250$ m.',
                           'Độ chính xác của phép đo là $d = 0,5$ m.',
                           'Độ dài thực $\\bar{l}$ của cây cầu nằm trong đoạn $[249,5; 250,5]$ (m).',
                           'Sai số tương đối của phép đo vượt quá $1\\%$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng. c) Đúng. d) Sai vì $\\delta_l \\le \\dfrac{0,5}{250} = 0,002 = '
                        '0,2\\% < 1\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 12: Số gần đúng và sai '
                 'số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được khái niệm số gần đúng, '
                           'sai số tuyệt đối $\\Delta_a$, độ chính xác $d$ và sai số tương đối $\\delta_a$.',
                           'Quy tắc/công thức **Sai số tuyệt đối và độ chính xác** trong bài được xác định '
                           'bởi: $\\Delta_a = |\\bar{a} - a| \\le d \\Leftrightarrow a - d \\le \\bar{a} '
                           '\\le a + d$.',
                           'Trong mọi trường hợp, **Sai số tuyệt đối và độ chính xác** luôn được tính bằng '
                           'công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo '
                           'theo) mà không cần điều kiện của Bài 12: Số gần đúng và sai số.',
                           'Với bài toán minh họa: “Cho số gần đúng $a = 23,476$ với độ chính xác $d = '
                           '0,02$. Hãy viết số quy tròn của số $a$.”, lời giải đúng là: Vì độ chính xác $d = '
                           '0,02$ đến hàng phần trăm nên ta quy tròn số $a = 23,476$ đến hàng phần mười. Chữ '
                           'số sau hàng phần mười là $7 \\ge 5$ nên...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Số gần đúng và sai số. b) **Đúng** '
                        'theo công thức trọng tâm **Sai số tuyệt đối và độ chính xác** ($\\Delta_a = '
                        '|\\bar{a} - a| \\le d \\Leftrightarrow a - d \\le \\bar{a} \\le a + d$). c) **Sai** '
                        'vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Sai số tuyệt đối và độ chính xác**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 12: Số gần đúng và sai số** để giải quyết tình huống sau: Cho số '
                 'gần đúng $a = 23,476$ với độ chính xác $d = 0,02$. Hãy viết số quy tròn của số $a$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Vì độ chính xác $d = 0,02$ đến hàng phần trăm nên ta quy tròn số $a = 23,476$ đến '
                        'hàng phần mười. Chữ số sau hàng phần mười là $7 \\ge 5$ nên số quy tròn củ...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Số gần đúng và sai số: Vì độ chính xác $d = 0,02$ '
                        'đến hàng phần trăm nên ta quy tròn số $a = 23,476$ đến hàng phần mười.\n'
                        'Chữ số sau hàng phần mười là $7 \\ge 5$ nên số quy tròn của $a$ là $23,5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một phép đo khối lượng cho kết quả $m = 50\\text{ g} \\pm 0,2\\text{ g}$. Sai số tương đối '
                 'tối đa $\\dfrac{d}{|m|}$ của phép đo này bằng bao nhiêu phần trăm (viết dưới dạng số thập '
                 'phân)?',
            'answer': ['0,4', '0.4'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{d}{|m|} = \\dfrac{0,2}{50} \\cdot 100\\% = 0,4\\%$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch05-thong-ke',
  'context_title': 'Chương V: Các số đặc trưng của mẫu số liệu không ghép nhóm',
  'context': 'Chương V · SGK Toán 10: Các số đặc trưng của mẫu số liệu không ghép nhóm.',
  'title': 'Bài 13: Các số đặc trưng đo xu thế trung tâm',
  'icon': '📊',
  'description': 'Tính số trung bình, trung vị, tứ phân vị và mốt của mẫu số liệu không ghép nhóm.',
  'requirements': ['Tính được số trung bình ($\\bar{x}$), trung vị ($M_e$), tứ phân vị ($Q_1, Q_2, Q_3$) và '
                   'mốt ($M_o$) của mẫu số liệu.',
                   'Giải thích được ý nghĩa và biết chọn số đặc trưng đo xu thế trung tâm phù hợp cho từng '
                   'mẫu số liệu.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Số trung bình** ($\\bar{x} = \\dfrac{x_1 + '
                   'x_2 + \\dots + x_n}{n} = \\dfrac{m_1x_1 + \\dots + m_kx_k}{n}$) vào giải bài tập.'],
  'definition': 'Các số đặc trưng đo xu thế trung tâm của mẫu số liệu gồm: Số trung bình cộng ($\\bar{x}$), '
                'Trung vị ($M_e$), Tứ phân vị ($Q_1, Q_2, Q_3$) và Mốt ($M_o$).',
  'theory': '1. Số trung bình: $\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + x_n}{n}$.\n'
            '2. Trung vị ($M_e$): Sắp xếp mẫu số liệu theo thứ tự không giảm. Nếu cỡ mẫu $n$ lẻ thì $M_e$ là '
            'số đứng chính giữa; nếu $n$ chẵn thì $M_e$ là trung bình cộng của hai số đứng giữa.\n'
            '3. Tứ phân vị: $Q_2 = M_e$; $Q_1$ là trung vị của nửa số liệu bên trái $Q_2$ (không kể $Q_2$ '
            'nếu $n$ lẻ); $Q_3$ là trung vị của nửa số liệu bên phải $Q_2$.\n'
            '4. Mốt ($M_o$): Giá trị có tần số lớn nhất trong mẫu số liệu.',
  'formulas': [{'category': 'Các số đặc trưng đo xu thế trung tâm',
                'items': [{'name': 'Số trung bình',
                           'formula': '$\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + x_n}{n} = \\dfrac{m_1x_1 + '
                                      '\\dots + m_kx_k}{n}$',
                           'note': 'Nhạy cảm với các giá trị bất thường'},
                          {'name': 'Trung vị và Tứ phân vị',
                           'formula': '$Q_2 = M_e$; $Q_1$: trung vị nửa dưới; $Q_3$: trung vị nửa trên',
                           'note': 'Chia mẫu số liệu đã sắp xếp thành 4 phần bằng nhau'}]}],
  'example': 'Cho mẫu số liệu: $2, 5, 3, 8, 5, 10, 9$. Tìm số trung bình, trung vị, tứ phân vị và mốt của '
             'mẫu số liệu.',
  'example_answer': 'Sắp xếp mẫu theo thứ tự không giảm: $2, 3, 5, 5, 8, 9, 10$ ($n = 7$).\n'
                    '- Số trung bình: $\\bar{x} = \\dfrac{2 + 3 + 5 + 5 + 8 + 9 + 10}{7} = 6$.\n'
                    '- Trung vị (cũng là $Q_2$): $M_e = Q_2 = 5$ (số hạng thứ 4).\n'
                    '- Tứ phân vị: nửa dưới là $2, 3, 5 \\Rightarrow Q_1 = 3$; nửa trên là $8, 9, 10 '
                    '\\Rightarrow Q_3 = 9$.\n'
                    '- Mốt: $M_o = 5$ (xuất hiện 2 lần).',
  'real_life': 'Đánh giá mức lương trung vị của người lao động (không bị lệch bởi một vài mức lương quá cao) '
               'và điểm thi trung bình của lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho mẫu số liệu: $3; 5; 7; 5; 9; 5; 8$. Mốt ($M_o$) của mẫu số liệu này là:',
            'options': ['$5$', '$6$', '$7$', '$9$'],
            'answer': 0,
            'solution': 'Giá trị $5$ xuất hiện nhiều nhất ($3$ lần) nên $M_o = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trung vị của mẫu số liệu $2; 4; 6; 8; 10$ là:',
            'options': ['$5$', '$6$', '$4$', '$8$'],
            'answer': 1,
            'solution': 'Mẫu đã sắp xếp có $n = 5$ phần tử, số đứng chính giữa là $6$ nên $M_e = 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 13: Các số đặc trưng đo xu thế trung tâm**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Số trung bình**?',
            'options': ['$Q_2 = M_e$; $Q_1$: trung vị nửa dưới; $Q_3$: trung vị nửa trên',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + x_n}{n} = \\dfrac{m_1x_1 + \\dots + '
                        'm_kx_k}{n}$',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 13: Các số đặc trưng đo xu thế trung tâm, '
                        '**Số trung bình** được xác định bởi: $\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + '
                        'x_n}{n} = \\dfrac{m_1x_1 + \\dots + m_kx_k}{n}$. (Nhạy cảm với các giá trị bất '
                        'thường)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Các số đặc trưng đo xu thế trung tâm**, nội dung/biểu thức $Q_2 = M_e$; '
                 '$Q_1$: trung vị nửa dưới; $Q_3$: trung vị nửa trên là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Số trung bình', 'Mệnh đề kéo theo', 'Mệnh đề tương đương', 'Trung vị và Tứ phân vị'],
            'answer': 3,
            'solution': 'Trong Bài 13: Các số đặc trưng đo xu thế trung tâm, biểu thức/quy tắc $Q_2 = M_e$; '
                        '$Q_1$: trung vị nửa dưới; $Q_3$: trung vị nửa trên chính là nội dung của **Trung vị '
                        'và Tứ phân vị**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho mẫu số liệu gồm 6 giá trị: $1; 3; 4; 6; 8; 10$. Trung vị $M_e$ của mẫu số liệu là:',
            'options': ['$5$', '$4$', '$6$', '$5,5$'],
            'answer': 0,
            'solution': 'Vì $n = 6$ chẵn nên trung vị là trung bình cộng của số thứ 3 và thứ 4: $M_e = '
                        '\\dfrac{4 + 6}{2} = 5$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Các số đặc trưng đo xu thế trung tâm** (Chương V: Các số đặc trưng của '
                 'mẫu số liệu không ghép nhóm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Tính được số trung bình ($\\bar{x}$), trung vị ($M_e$), tứ phân vị ($Q_1, Q_2, '
                        'Q_3$) và mốt ($M_o$) của mẫu số liệu.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 13: Các số đặc trưng đo xu thế trung tâm: Tính được số '
                        'trung bình ($\\bar{x}$), trung vị ($M_e$), tứ phân vị ($Q_1, Q_2, Q_3$) và mốt '
                        '($M_o$) của mẫu số liệu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho mẫu số liệu đã sắp xếp theo thứ tự không giảm: $3; 4; 6; 7; 8; 10; 11$.',
            'statements': ['Số trung bình cộng của mẫu số liệu là $\\bar{x} = 7$.',
                           'Trung vị của mẫu số liệu là $Q_2 = 7$.',
                           'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1 = 4$.',
                           'Tứ phân vị thứ ba của mẫu số liệu là $Q_3 = 9$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $\\bar{x} = \\dfrac{49}{7} = 7$. b) Đúng (số hạng thứ 4 là $7$). c) Đúng '
                        '(trung vị của $3; 4; 6$ là $4$). d) Sai vì trung vị của nửa trên $8; 10; 11$ là '
                        '$Q_3 = 10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 13: Các số đặc trưng đo '
                 'xu thế trung tâm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được số trung bình '
                           '($\\bar{x}$), trung vị ($M_e$), tứ phân vị ($Q_1, Q_2, Q_3$) và mốt ($M_o$) của '
                           'mẫu số liệu.',
                           'Quy tắc/công thức **Số trung bình** trong bài được xác định bởi: $\\bar{x} = '
                           '\\dfrac{x_1 + x_2 + \\dots + x_n}{n} = \\dfrac{m_1x_1 + \\dots + m_kx_k}{n}$.',
                           'Trong mọi trường hợp, **Số trung bình** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 13: Các số đặc trưng đo xu thế trung tâm.',
                           'Với bài toán minh họa: “Cho mẫu số liệu: $2, 5, 3, 8, 5, 10, 9$. Tìm số trung '
                           'bình, trung vị, tứ phân vị và mốt của mẫu số liệu.”, lời giải đúng là: Sắp xếp '
                           'mẫu theo thứ tự không giảm: $2, 3, 5, 5, 8, 9, 10$ ($n = 7$). - Số trung bình: '
                           '$\\bar{x} = \\dfrac{2 + 3 + 5 + 5 + 8 + 9 + 10}{7} = 6$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Các số đặc trưng đo xu thế trung tâm. '
                        'b) **Đúng** theo công thức trọng tâm **Số trung bình** ($\\bar{x} = \\dfrac{x_1 + '
                        'x_2 + \\dots + x_n}{n} = \\dfrac{m_1x_1 + \\dots + m_kx_k}{n}$). c) **Sai** vì $P '
                        '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Số trung bình**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 13: Các số đặc trưng đo xu thế trung tâm** để giải quyết tình '
                 'huống sau: Cho mẫu số liệu: $2, 5, 3, 8, 5, 10, 9$. Tìm số trung bình, trung vị, tứ phân '
                 'vị và mốt của mẫu số liệu. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Sắp xếp mẫu theo thứ tự không giảm: $2, 3, 5, 5, 8, 9, 10$ ($n = 7$). - Số trung '
                        'bình: $\\bar{x} = \\dfrac{2 + 3 + 5 + 5 + 8 + 9 + 10}{7} = 6$. - Trung vị (c...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Các số đặc trưng đo xu thế trung tâm: Sắp xếp mẫu '
                        'theo thứ tự không giảm: $2, 3, 5, 5, 8, 9, 10$ ($n = 7$).\n'
                        '- Số trung bình: $\\bar{x} = \\dfrac{2 + 3 + 5 + 5 + 8 + 9 + 10}{7} = 6$.\n'
                        '- Trung vị (cũng là $Q_2$): $M_e = Q_2 = 5$ (số hạng thứ 4).\n'
                        '- Tứ phân vị: nửa dưới là $2, 3, 5 \\Rightarrow Q_1 = 3$; nửa trên là $8, 9, 10 '
                        '\\Rightarrow Q_3 = 9$.\n'
                        '- Mốt: $M_o = 5$ (xuất hiện 2 lần).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Điểm 5 bài kiểm tra của bạn An là $7; 8; 8; 9; x$. Biết điểm trung bình của 5 bài là '
                 '$8,2$. Tìm giá trị của $x$.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{7 + 8 + 8 + 9 + x}{5} = 8,2 \\Rightarrow 32 + x = 41 \\Rightarrow x '
                        '= 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch05-thong-ke',
  'context_title': 'Chương V: Các số đặc trưng của mẫu số liệu không ghép nhóm',
  'context': 'Chương V · SGK Toán 10: Các số đặc trưng của mẫu số liệu không ghép nhóm.',
  'title': 'Bài 14: Các số đặc trưng đo độ phân tán',
  'icon': '📈',
  'description': 'Tính khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn và phát hiện giá trị '
                 'bất thường.',
  'requirements': ['Tính được khoảng biến thiên ($R$), khoảng tứ phân vị ($\\Delta_Q$), phương sai ($s^2$) '
                   'và độ lệch chuẩn ($s$).',
                   'Sử dụng khoảng tứ phân vị để phát hiện giá trị bất thường (ngoại lệ) và giải thích ý '
                   'nghĩa của độ phân tán.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Khoảng biến thiên và Khoảng tứ phân vị** '
                   '($R = x_{\\max} - x_{\\min}$; $\\Delta_Q = Q_3 - Q_1$) vào giải bài tập.'],
  'definition': 'Các số đặc trưng đo độ phân tán gồm: Khoảng biến thiên $R = x_{\\max} - x_{\\min}$, Khoảng '
                'tứ phân vị $\\Delta_Q = Q_3 - Q_1$, Phương sai $s^2$ và Độ lệch chuẩn $s = \\sqrt{s^2}$.',
  'theory': '1. Phương sai mẫu: $s^2 = \\dfrac{1}{n}[(x_1 - \\bar{x})^2 + (x_2 - \\bar{x})^2 + \\dots + (x_n '
            '- \\bar{x})^2]$. Độ lệch chuẩn $s = \\sqrt{s^2}$ có cùng đơn vị đo với số liệu.\n'
            '2. Độ lệch chuẩn (hoặc phương sai) càng nhỏ thì số liệu càng đồng đều (ít phân tán quanh số '
            'trung bình).\n'
            '3. Giá trị $x$ trong mẫu số liệu được coi là giá trị bất thường (ngoại lệ) nếu $x > Q_3 + '
            '1,5\\Delta_Q$ hoặc $x < Q_1 - 1,5\\Delta_Q$.',
  'formulas': [{'category': 'Các số đặc trưng đo độ phân tán',
                'items': [{'name': 'Khoảng biến thiên và Khoảng tứ phân vị',
                           'formula': '$R = x_{\\max} - x_{\\min}$; $\\Delta_Q = Q_3 - Q_1$',
                           'note': 'Giá trị bất thường: $x < Q_1 - 1,5\\Delta_Q$ hoặc $x > Q_3 + '
                                   '1,5\\Delta_Q$'},
                          {'name': 'Phương sai và Độ lệch chuẩn',
                           'formula': '$s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2$; $s = '
                                      '\\sqrt{s^2}$',
                           'note': '$s^2 = \\dfrac{1}{n}\\sum_{i=1}^n x_i^2 - \\bar{x}^2$'}]}],
  'example': 'Tính khoảng biến thiên, phương sai và độ lệch chuẩn của mẫu số liệu: $2; 4; 6; 8; 10$.',
  'example_answer': '- Khoảng biến thiên: $R = 10 - 2 = 8$.\n'
                    '- Số trung bình: $\\bar{x} = \\dfrac{2 + 4 + 6 + 8 + 10}{5} = 6$.\n'
                    '- Phương sai: $s^2 = \\dfrac{(2 - 6)^2 + (4 - 6)^2 + (6 - 6)^2 + (8 - 6)^2 + (10 - '
                    '6)^2}{5} = \\dfrac{16 + 4 + 0 + 4 + 16}{5} = 8$.\n'
                    '- Độ lệch chuẩn: $s = \\sqrt{8} = 2\\sqrt{2}$.',
  'real_life': 'Đánh giá độ ổn định của nhiệt độ ngày đêm giữa hai vùng khí hậu hoặc độ đồng đều về kích '
               'thước chi tiết máy trên dây chuyền.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho mẫu số liệu: $12; 5; 18; 9; 25; 7$. Khoảng biến thiên $R$ của mẫu số liệu này là:',
            'options': ['$18$', '$20$', '$13$', '$25$'],
            'answer': 1,
            'solution': 'Ta có $x_{\\max} = 25$ và $x_{\\min} = 5$, nên khoảng biến thiên là $R = 25 - 5 = '
                        '20$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu một mẫu số liệu có phương sai $s^2 = 9$ thì độ lệch chuẩn $s$ của mẫu số liệu đó bằng:',
            'options': ['$81$', '$9$', '$3$', '$4,5$'],
            'answer': 2,
            'solution': 'Độ lệch chuẩn là căn bậc hai số học của phương sai: $s = \\sqrt{s^2} = \\sqrt{9} = '
                        '3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 14: Các số đặc trưng đo độ phân tán**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Khoảng biến thiên và Khoảng tứ phân vị**?',
            'options': ['$s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2$; $s = \\sqrt{s^2}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai',
                        '$R = x_{\\max} - x_{\\min}$; $\\Delta_Q = Q_3 - Q_1$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 14: Các số đặc trưng đo độ phân tán, **Khoảng '
                        'biến thiên và Khoảng tứ phân vị** được xác định bởi: $R = x_{\\max} - x_{\\min}$; '
                        '$\\Delta_Q = Q_3 - Q_1$. (Giá trị bất thường: $x < Q_1 - 1,5\\Delta_Q$ hoặc $x > '
                        'Q_3 + 1,5\\Delta_Q$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Các số đặc trưng đo độ phân tán**, nội dung/biểu thức $s^2 = '
                 '\\dfrac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2$; $s = \\sqrt{s^2}$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Phương sai và Độ lệch chuẩn',
                        'Khoảng biến thiên và Khoảng tứ phân vị',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương'],
            'answer': 0,
            'solution': 'Trong Bài 14: Các số đặc trưng đo độ phân tán, biểu thức/quy tắc $s^2 = '
                        '\\dfrac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2$; $s = \\sqrt{s^2}$ chính là nội dung '
                        'của **Phương sai và Độ lệch chuẩn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một mẫu số liệu có tứ phân vị thứ nhất $Q_1 = 15$ và tứ phân vị thứ ba $Q_3 = 23$. Khoảng '
                 'tứ phân vị $\\Delta_Q$ bằng:',
            'options': ['$38$', '$8$', '$19$', '$4$'],
            'answer': 1,
            'solution': 'Ta có $\\Delta_Q = Q_3 - Q_1 = 23 - 15 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Các số đặc trưng đo độ phân tán** (Chương V: Các số đặc trưng của mẫu số '
                 'liệu không ghép nhóm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Tính được khoảng biến thiên ($R$), khoảng tứ phân vị ($\\Delta_Q$), phương sai '
                        '($s^2$) và độ lệch chuẩn ($s$).',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 14: Các số đặc trưng đo độ phân tán: Tính được khoảng '
                        'biến thiên ($R$), khoảng tứ phân vị ($\\Delta_Q$), phương sai ($s^2$) và độ lệch '
                        'chuẩn ($s$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho mẫu số liệu gồm 4 giá trị: $2; 4; 6; 8$.',
            'statements': ['Khoảng biến thiên của mẫu số liệu là $R = 6$.',
                           'Số trung bình cộng của mẫu số liệu là $\\bar{x} = 5$.',
                           'Phương sai của mẫu số liệu là $s^2 = 5$.',
                           'Nếu cộng thêm $10$ vào mỗi giá trị của mẫu số liệu thì phương sai tăng thêm '
                           '$10$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng ($8 - 2 = 6$). b) Đúng ($\\dfrac{20}{4} = 5$). c) Đúng vì $s^2 = \\dfrac{9 '
                        '+ 1 + 1 + 9}{4} = 5$. d) Sai vì khi cộng cùng một hằng số vào mọi giá trị thì độ '
                        'phân tán (phương sai) không thay đổi.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 14: Các số đặc trưng đo '
                 'độ phân tán**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được khoảng biến thiên ($R$), '
                           'khoảng tứ phân vị ($\\Delta_Q$), phương sai ($s^2$) và độ lệch chuẩn ($s$).',
                           'Quy tắc/công thức **Khoảng biến thiên và Khoảng tứ phân vị** trong bài được xác '
                           'định bởi: $R = x_{\\max} - x_{\\min}$; $\\Delta_Q = Q_3 - Q_1$.',
                           'Trong mọi trường hợp, **Khoảng biến thiên và Khoảng tứ phân vị** luôn được tính '
                           'bằng công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề '
                           'kéo theo) mà không cần điều kiện của Bài 14: Các số đặc trưng đo độ phân tán.',
                           'Với bài toán minh họa: “Tính khoảng biến thiên, phương sai và độ lệch chuẩn của '
                           'mẫu số liệu: $2; 4; 6; 8; 10$.”, lời giải đúng là: - Khoảng biến thiên: $R = 10 '
                           '- 2 = 8$. - Số trung bình: $\\bar{x} = \\dfrac{2 + 4 + 6 + 8 + 10}{5} = 6$. - '
                           'Phương sai...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Các số đặc trưng đo độ phân tán. b) '
                        '**Đúng** theo công thức trọng tâm **Khoảng biến thiên và Khoảng tứ phân vị** ($R = '
                        'x_{\\max} - x_{\\min}$; $\\Delta_Q = Q_3 - Q_1$). c) **Sai** vì $P \\Rightarrow Q$ '
                        'chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc '
                        'chung của **Khoảng biến thiên và Khoảng tứ phân vị**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 14: Các số đặc trưng đo độ phân tán** để giải quyết tình huống '
                 'sau: Tính khoảng biến thiên, phương sai và độ lệch chuẩn của mẫu số liệu: $2; 4; 6; 8; '
                 '10$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        '- Khoảng biến thiên: $R = 10 - 2 = 8$. - Số trung bình: $\\bar{x} = \\dfrac{2 + 4 + '
                        '6 + 8 + 10}{5} = 6$. - Phương sai...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Các số đặc trưng đo độ phân tán: - Khoảng biến '
                        'thiên: $R = 10 - 2 = 8$.\n'
                        '- Số trung bình: $\\bar{x} = \\dfrac{2 + 4 + 6 + 8 + 10}{5} = 6$.\n'
                        '- Phương sai: $s^2 = \\dfrac{(2 - 6)^2 + (4 - 6)^2 + (6 - 6)^2 + (8 - 6)^2 + (10 - '
                        '6)^2}{5} = \\dfrac{16 + 4 + 0 + 4 + 16}{5} = 8$.\n'
                        '- Độ lệch chuẩn: $s = \\sqrt{8} = 2\\sqrt{2}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mẫu số liệu có $Q_1 = 20$ và $Q_3 = 30$. Một giá trị $x$ vượt quá ngưỡng $Q_3 + '
                 '1,5\\Delta_Q$ được coi là giá trị bất thường lớn. Tính giá trị ngưỡng $Q_3 + '
                 '1,5\\Delta_Q$.',
            'answer': ['45'],
            'unit': None,
            'solution': 'Ta có $\\Delta_Q = Q_3 - Q_1 = 30 - 20 = 10$. Ngưỡng cần tìm là $30 + 1,5 \\cdot 10 '
                        '= 45$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch06-ham-so-do-thi',
  'context_title': 'Chương VI: Hàm số, đồ thị và ứng dụng',
  'context': 'Chương VI · SGK Toán 10: Hàm số, đồ thị và ứng dụng.',
  'title': 'Bài 15: Hàm số',
  'icon': '📈',
  'description': 'Tìm tập xác định, tập giá trị, xét tính đồng biến, nghịch biến và đọc đồ thị của hàm số.',
  'requirements': ['Nhận biết được hàm số cho bằng bảng, biểu đồ hoặc công thức; tìm được tập xác định và '
                   'tập giá trị của hàm số.',
                   'Xét được sự biến thiên (đồng biến, nghịch biến) của hàm số trên một khoảng thông qua '
                   'công thức hoặc đồ thị.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Điều kiện có nghĩa** ($\\dfrac{1}{B(x)} '
                   '\\Rightarrow B(x) \\neq 0$; $\\sqrt{A(x)} \\Rightarrow A(x) \\ge 0$) vào giải bài tập.'],
  'definition': 'Nếu với mỗi giá trị của $x$ thuộc tập hợp số $D$ có một và chỉ một giá trị tương ứng của '
                '$y$ thuộc $\\mathbb{R}$ thì ta có một hàm số. $x$ gọi là biến số, $y$ gọi là hàm số của '
                '$x$, $D$ gọi là tập xác định của hàm số.',
  'theory': '1. Tập xác định của hàm số $y = f(x)$ là tập hợp tất cả các số thực $x$ sao cho biểu thức '
            '$f(x)$ có nghĩa:\n'
            '- Biểu thức $\\dfrac{A(x)}{B(x)}$ có nghĩa khi $B(x) \\neq 0$.\n'
            '- Biểu thức $\\sqrt{A(x)}$ có nghĩa khi $A(x) \\ge 0$.\n'
            '2. Trên khoảng $(a; b)$: Hàm số đồng biến (tăng) nếu $x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$ '
            '(đồ thị đi lên từ trái sang phải); hàm số nghịch biến (giảm) nếu $x_1 < x_2 \\Rightarrow f(x_1) '
            '> f(x_2)$ (đồ thị đi xuống từ trái sang phải).',
  'formulas': [{'category': 'Tập xác định và sự biến thiên của hàm số',
                'items': [{'name': 'Điều kiện có nghĩa',
                           'formula': '$\\dfrac{1}{B(x)} \\Rightarrow B(x) \\neq 0$; $\\sqrt{A(x)} '
                                      '\\Rightarrow A(x) \\ge 0$',
                           'note': '$\\dfrac{1}{\\sqrt{A(x)}} \\Rightarrow A(x) > 0$'},
                          {'name': 'Đồng biến và Nghịch biến',
                           'formula': 'Đồng biến: $x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$; Nghịch biến: '
                                      '$x_1 < x_2 \\Rightarrow f(x_1) > f(x_2)$',
                           'note': 'Xét với mọi $x_1, x_2 \\in K$'}]}],
  'example': 'Tìm tập xác định của hàm số $y = \\sqrt{x - 1} + \\dfrac{2}{x - 3}$.',
  'example_answer': 'Biểu thức có nghĩa khi $\\begin{cases} x - 1 \\ge 0 \\\\ x - 3 \\neq 0 \\end{cases} '
                    '\\Leftrightarrow \\begin{cases} x \\ge 1 \\\\ x \\neq 3 \\end{cases}$.\n'
                    'Vậy tập xác định của hàm số là $D = [1; +\\infty) \\setminus \\{3\\}$.',
  'real_life': 'Biểu diễn cước phí taxi theo số kilômét di chuyển hoặc biểu đồ nhiệt độ theo các giờ trong '
               'ngày.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tập xác định của hàm số $y = \\dfrac{x + 1}{x - 2}$ là:',
            'options': ['$D = \\mathbb{R} \\setminus \\{-1\\}$',
                        '$D = (2; +\\infty)$',
                        '$D = \\mathbb{R} \\setminus \\{2\\}$',
                        '$D = \\mathbb{R}$'],
            'answer': 2,
            'solution': 'Hàm số xác định khi mẫu số $x - 2 \\neq 0 \\Leftrightarrow x \\neq 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập xác định của hàm số $y = \\sqrt{4 - 2x}$ là:',
            'options': ['$[2; +\\infty)$',
                        '$(-\\infty; 2)$',
                        '$\\mathbb{R} \\setminus \\{2\\}$',
                        '$(-\\infty; 2]$'],
            'answer': 3,
            'solution': 'Hàm số xác định khi $4 - 2x \\ge 0 \\Leftrightarrow x \\le 2$, tức là $D = '
                        '(-\\infty; 2]$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 15: Hàm số**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Điều kiện có nghĩa**?',
            'options': ['$\\dfrac{1}{B(x)} \\Rightarrow B(x) \\neq 0$; $\\sqrt{A(x)} \\Rightarrow A(x) \\ge '
                        '0$',
                        'Đồng biến: $x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$; Nghịch biến: $x_1 < x_2 '
                        '\\Rightarrow f(x_1) > f(x_2)$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 15: Hàm số, **Điều kiện có nghĩa** được xác '
                        'định bởi: $\\dfrac{1}{B(x)} \\Rightarrow B(x) \\neq 0$; $\\sqrt{A(x)} \\Rightarrow '
                        'A(x) \\ge 0$. ($\\dfrac{1}{\\sqrt{A(x)}} \\Rightarrow A(x) > 0$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Hàm số**, nội dung/biểu thức Đồng biến: $x_1 < x_2 \\Rightarrow f(x_1) < '
                 'f(x_2)$; Nghịch biến: $x_1 < x_2 \\Rightarrow f(x_1) > f(x_2)$ là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Điều kiện có nghĩa',
                        'Đồng biến và Nghịch biến',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương'],
            'answer': 1,
            'solution': 'Trong Bài 15: Hàm số, biểu thức/quy tắc Đồng biến: $x_1 < x_2 \\Rightarrow f(x_1) < '
                        'f(x_2)$; Nghịch biến: $x_1 < x_2 \\Rightarrow f(x_1) > f(x_2)$ chính là nội dung '
                        'của **Đồng biến và Nghịch biến**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hàm số bậc nhất nào sau đây nghịch biến trên $\\mathbb{R}$?',
            'options': ['$y = 3x - 1$', '$y = x + 4$', '$y = -2x + 5$', '$y = 2x$'],
            'answer': 2,
            'solution': 'Hàm số bậc nhất $y = ax + b$ nghịch biến trên $\\mathbb{R}$ khi $a < 0$, nên $y = '
                        '-2x + 5$ nghịch biến.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Hàm số** (Chương VI: Hàm số, đồ thị và ứng dụng), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Nhận biết được hàm số cho bằng bảng, biểu đồ hoặc công thức; tìm được tập xác định '
                        'và tập giá trị của hàm số.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 15: Hàm số: Nhận biết được hàm số cho bằng bảng, biểu '
                        'đồ hoặc công thức; tìm được tập xác định và tập giá trị của hàm số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $f(x) = \\sqrt{x + 2} + \\dfrac{1}{x - 2}$.',
            'statements': ['Tập xác định của hàm số là $D = [-2; +\\infty) \\setminus \\{2\\}$.',
                           'Giá trị của hàm số tại $x = 7$ là $f(7) = \\dfrac{16}{5}$.',
                           'Điểm $M(-2; -\\dfrac{1}{4})$ thuộc đồ thị của hàm số.',
                           'Số $x = 2$ thuộc tập xác định của hàm số.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $f(7) = \\sqrt{9} + \\dfrac{1}{5} = 3 + \\dfrac{1}{5} = '
                        '\\dfrac{16}{5}$. c) Đúng vì $f(-2) = 0 + \\dfrac{1}{-4} = -\\dfrac{1}{4}$. d) Sai '
                        'vì tại $x = 2$ mẫu số bằng $0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 15: Hàm số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hàm số cho bằng '
                           'bảng, biểu đồ hoặc công thức; tìm được tập xác định và tập giá trị của hàm số.',
                           'Quy tắc/công thức **Điều kiện có nghĩa** trong bài được xác định bởi: '
                           '$\\dfrac{1}{B(x)} \\Rightarrow B(x) \\neq 0$; $\\sqrt{A(x)} \\Rightarrow A(x) '
                           '\\ge 0$.',
                           'Trong mọi trường hợp, **Điều kiện có nghĩa** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 15: Hàm số.',
                           'Với bài toán minh họa: “Tìm tập xác định của hàm số $y = \\sqrt{x - 1} + '
                           '\\dfrac{2}{x - 3}$.”, lời giải đúng là: Biểu thức có nghĩa khi $\\begin{cases} x '
                           '- 1 \\ge 0 \\\\ x - 3 \\neq 0 \\end{cases} \\Leftrightarrow \\begin{cases} x '
                           '\\ge 1 \\\\ x \\neq 3 \\end{cases}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Hàm số. b) **Đúng** theo công thức '
                        'trọng tâm **Điều kiện có nghĩa** ($\\dfrac{1}{B(x)} \\Rightarrow B(x) \\neq 0$; '
                        '$\\sqrt{A(x)} \\Rightarrow A(x) \\ge 0$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai '
                        'khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Điều kiện có nghĩa**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 15: Hàm số** để giải quyết tình huống sau: Tìm tập xác định của '
                 'hàm số $y = \\sqrt{x - 1} + \\dfrac{2}{x - 3}$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Biểu thức có nghĩa khi $\\begin{cases} x - 1 \\ge 0 \\\\ x - 3 \\neq 0 \\end{cases} '
                        '\\Leftrightarrow \\begin{cases} x \\ge 1 \\\\ x \\neq 3 \\end{cases}$. Vậy tập xác '
                        'đ...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Hàm số: Biểu thức có nghĩa khi $\\begin{cases} x - 1 '
                        '\\ge 0 \\\\ x - 3 \\neq 0 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge 1 '
                        '\\\\ x \\neq 3 \\end{cases}$.\n'
                        'Vậy tập xác định của hàm số là $D = [1; +\\infty) \\setminus \\{3\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hàm số $f(x) = \\begin{cases} 2x + 1 & \\text{khi } x \\ge 1 \\\\ x^2 + 4 & \\text{khi '
                 '} x < 1 \\end{cases}$. Tính tổng $f(2) + f(-1)$.',
            'answer': ['10'],
            'unit': None,
            'solution': 'Vì $2 \\ge 1$ nên $f(2) = 2(2) + 1 = 5$. Vì $-1 < 1$ nên $f(-1) = (-1)^2 + 4 = 5$. '
                        'Vậy $f(2) + f(-1) = 5 + 5 = 10$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch06-ham-so-do-thi',
  'context_title': 'Chương VI: Hàm số, đồ thị và ứng dụng',
  'context': 'Chương VI · SGK Toán 10: Hàm số, đồ thị và ứng dụng.',
  'title': 'Bài 16: Hàm số bậc hai',
  'icon': '🌈',
  'description': 'Xác định đỉnh, trục đối xứng, khoảng biến thiên và vẽ đồ thị parabol của hàm số bậc hai.',
  'requirements': ['Xác định được tọa độ đỉnh $I$, trục đối xứng và lập bảng biến thiên của hàm số bậc hai '
                   '$y = ax^2 + bx + c$ ($a \\neq 0$).',
                   'Vẽ được đồ thị parabol và vận dụng hàm số bậc hai để giải các bài toán thực tế về cực '
                   'trị.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tọa độ đỉnh $I$** ($x_I = -\\dfrac{b}{2a}$; '
                   '$y_I = f(x_I) = -\\dfrac{\\Delta}{4a}$) vào giải bài tập.'],
  'definition': 'Hàm số bậc hai là hàm số cho bởi công thức $y = ax^2 + bx + c$, trong đó $x$ là biến số, '
                '$a, b, c$ là các hằng số và $a \\neq 0$. Tập xác định của hàm số bậc hai là $\\mathbb{R}$.',
  'theory': 'Đồ thị hàm số $y = ax^2 + bx + c$ ($a \\neq 0$) là một đường parabol:\n'
            '- Có đỉnh là điểm $I\\left(-\\dfrac{b}{2a}; -\\dfrac{\\Delta}{4a}\\right)$ và trục đối xứng là '
            'đường thẳng $x = -\\dfrac{b}{2a}$.\n'
            '- Nếu $a > 0$: bề lõm quay lên trên; hàm số nghịch biến trên $\\left(-\\infty; '
            '-\\dfrac{b}{2a}\\right)$, đồng biến trên $\\left(-\\dfrac{b}{2a}; +\\infty\\right)$ và đạt giá '
            'trị nhỏ nhất tại $x = -\\dfrac{b}{2a}$.\n'
            '- Nếu $a < 0$: bề lõm quay xuống dưới; hàm số đồng biến trên $\\left(-\\infty; '
            '-\\dfrac{b}{2a}\\right)$, nghịch biến trên $\\left(-\\dfrac{b}{2a}; +\\infty\\right)$ và đạt '
            'giá trị lớn nhất tại $x = -\\dfrac{b}{2a}$.',
  'formulas': [{'category': 'Hàm số bậc hai $y = ax^2 + bx + c$ ($a \\neq 0$)',
                'items': [{'name': 'Tọa độ đỉnh $I$',
                           'formula': '$x_I = -\\dfrac{b}{2a}$; $y_I = f(x_I) = -\\dfrac{\\Delta}{4a}$',
                           'note': 'Trục đối xứng là đường thẳng $x = -\\dfrac{b}{2a}$'},
                          {'name': 'Cực trị trên $\\mathbb{R}$',
                           'formula': '$a > 0 \\Rightarrow \\min_{\\mathbb{R}} y = y_I$; $a < 0 \\Rightarrow '
                                      '\\max_{\\mathbb{R}} y = y_I$',
                           'note': 'Đạt tại $x = -\\dfrac{b}{2a}$'}]}],
  'example': 'Xác định tọa độ đỉnh, trục đối xứng và các khoảng đồng biến, nghịch biến của hàm số $y = x^2 - '
             '4x + 3$.',
  'example_answer': 'Ta có $a = 1 > 0, b = -4, c = 3$. Hoành độ đỉnh $x_I = -\\dfrac{-4}{2 \\cdot 1} = 2 '
                    '\\Rightarrow y_I = 2^2 - 4(2) + 3 = -1$.\n'
                    '- Đỉnh $I(2; -1)$, trục đối xứng là đường thẳng $x = 2$.\n'
                    '- Vì $a = 1 > 0$ nên hàm số nghịch biến trên $(-\\infty; 2)$ và đồng biến trên $(2; '
                    '+\\infty)$.',
  'real_life': 'Xác định góc ném hoặc mức giá bán sản phẩm tối ưu để doanh thu đạt giá trị cực đại.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trục đối xứng của parabol $y = x^2 - 6x + 5$ là đường thẳng:',
            'options': ['$x = -3$', '$x = 6$', '$y = 3$', '$x = 3$'],
            'answer': 3,
            'solution': 'Trục đối xứng là $x = -\\dfrac{b}{2a} = -\\dfrac{-6}{2 \\cdot 1} = 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tọa độ đỉnh $I$ của parabol $y = -x^2 + 2x + 3$ là:',
            'options': ['$I(1; 4)$', '$I(-1; 0)$', '$I(1; 2)$', '$I(2; 3)$'],
            'answer': 0,
            'solution': 'Ta có $x_I = -\\dfrac{2}{2(-1)} = 1$ và $y_I = -(1)^2 + 2(1) + 3 = 4$, nên đỉnh là '
                        '$I(1; 4)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 16: Hàm số bậc hai**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Tọa độ đỉnh $I$**?',
            'options': ['$a > 0 \\Rightarrow \\min_{\\mathbb{R}} y = y_I$; $a < 0 \\Rightarrow '
                        '\\max_{\\mathbb{R}} y = y_I$',
                        '$x_I = -\\dfrac{b}{2a}$; $y_I = f(x_I) = -\\dfrac{\\Delta}{4a}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 16: Hàm số bậc hai, **Tọa độ đỉnh $I$** được '
                        'xác định bởi: $x_I = -\\dfrac{b}{2a}$; $y_I = f(x_I) = -\\dfrac{\\Delta}{4a}$. '
                        '(Trục đối xứng là đường thẳng $x = -\\dfrac{b}{2a}$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Hàm số bậc hai**, nội dung/biểu thức $a > 0 \\Rightarrow '
                 '\\min_{\\mathbb{R}} y = y_I$; $a < 0 \\Rightarrow \\max_{\\mathbb{R}} y = y_I$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Tọa độ đỉnh $I$',
                        'Mệnh đề kéo theo',
                        'Cực trị trên $\\mathbb{R}$',
                        'Mệnh đề tương đương'],
            'answer': 2,
            'solution': 'Trong Bài 16: Hàm số bậc hai, biểu thức/quy tắc $a > 0 \\Rightarrow '
                        '\\min_{\\mathbb{R}} y = y_I$; $a < 0 \\Rightarrow \\max_{\\mathbb{R}} y = y_I$ '
                        'chính là nội dung của **Cực trị trên $\\mathbb{R}$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hàm số $y = 2x^2 - 4x + 1$ đồng biến trên khoảng nào sau đây?',
            'options': ['$(-\\infty; 1)$', '$(-1; +\\infty)$', '$(-\\infty; 2)$', '$(1; +\\infty)$'],
            'answer': 3,
            'solution': 'Vì $a = 2 > 0$ và hoành độ đỉnh $x_I = 1$ nên hàm số đồng biến trên khoảng $(1; '
                        '+\\infty)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Hàm số bậc hai** (Chương VI: Hàm số, đồ thị và ứng dụng), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Xác định được tọa độ đỉnh $I$, trục đối xứng và lập bảng biến thiên của hàm số bậc '
                        'hai $y = ax^2 + bx + c$ ($a \\neq 0$).',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 16: Hàm số bậc hai: Xác định được tọa độ đỉnh $I$, '
                        'trục đối xứng và lập bảng biến thiên của hàm số bậc hai $y = ax^2 + bx + c$ ($a '
                        '\\neq 0$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho parabol $(P): y = x^2 - 2x - 3$.',
            'statements': ['Parabol $(P)$ có đỉnh là $I(1; -4)$.',
                           'Hàm số đạt giá trị nhỏ nhất bằng $-4$ tại $x = 1$.',
                           'Parabol $(P)$ cắt trục tung tại điểm $A(0; -3)$.',
                           'Parabol $(P)$ không cắt trục hoành.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng ($x_I = 1, y_I = -4$). b) Đúng vì $a = 1 > 0$. c) Đúng. d) Sai vì phương '
                        'trình $x^2 - 2x - 3 = 0$ có hai nghiệm $x = -1, x = 3$ nên $(P)$ cắt $Ox$ tại 2 '
                        'điểm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 16: Hàm số bậc hai**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được tọa độ đỉnh $I$, '
                           'trục đối xứng và lập bảng biến thiên của hàm số bậc hai $y = ax^2 + bx + c$ ($a '
                           '\\neq 0$).',
                           'Quy tắc/công thức **Tọa độ đỉnh $I$** trong bài được xác định bởi: $x_I = '
                           '-\\dfrac{b}{2a}$; $y_I = f(x_I) = -\\dfrac{\\Delta}{4a}$.',
                           'Trong mọi trường hợp, **Tọa độ đỉnh $I$** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 16: Hàm số bậc hai.',
                           'Với bài toán minh họa: “Xác định tọa độ đỉnh, trục đối xứng và các khoảng đồng '
                           'biến, nghịch biến của hàm số $y = x^2 - 4x + 3$.”, lời giải đúng là: Ta có $a = '
                           '1 > 0, b = -4, c = 3$. Hoành độ đỉnh $x_I = -\\dfrac{-4}{2 \\cdot 1} = 2 '
                           '\\Rightarrow y_I = 2^2 - 4(2) + 3 = -1$. - Đỉnh $I(2; -1)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Hàm số bậc hai. b) **Đúng** theo công '
                        'thức trọng tâm **Tọa độ đỉnh $I$** ($x_I = -\\dfrac{b}{2a}$; $y_I = f(x_I) = '
                        '-\\dfrac{\\Delta}{4a}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ '
                        'sai là công thức của nội dung khác, không phải quy tắc chung của **Tọa độ đỉnh '
                        '$I$**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 16: Hàm số bậc hai** để giải quyết tình huống sau: Xác định tọa '
                 'độ đỉnh, trục đối xứng và các khoảng đồng biến, nghịch biến của hàm số $y = x^2 - 4x + 3$. '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Ta có $a = 1 > 0, b = -4, c = 3$. Hoành độ đỉnh $x_I = -\\dfrac{-4}{2 \\cdot 1} = 2 '
                        '\\Rightarrow y_I = 2^2 - 4(2) + 3 = -1$. - Đỉnh $I(2; -1)$, trục đối xứng...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Hàm số bậc hai: Ta có $a = 1 > 0, b = -4, c = 3$. '
                        'Hoành độ đỉnh $x_I = -\\dfrac{-4}{2 \\cdot 1} = 2 \\Rightarrow y_I = 2^2 - 4(2) + 3 '
                        '= -1$.\n'
                        '- Đỉnh $I(2; -1)$, trục đối xứng là đường thẳng $x = 2$.\n'
                        '- Vì $a = 1 > 0$ nên hàm số nghịch biến trên $(-\\infty; 2)$ và đồng biến trên $(2; '
                        '+\\infty)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một quả bóng được đá lên từ mặt đất có độ cao $h$ (mét) sau $t$ (giây) được tính bởi công '
                 'thức $h(t) = -5t^2 + 20t$. Độ cao lớn nhất mà quả bóng đạt được là bao nhiêu mét?',
            'answer': ['20'],
            'unit': None,
            'solution': 'Hàm số $h(t) = -5t^2 + 20t$ có $a = -5 < 0$, đạt giá trị lớn nhất tại $t = '
                        '-\\dfrac{20}{2(-5)} = 2$ (giây). Độ cao lớn nhất là $h(2) = -5(4) + 20(2) = 20$ '
                        '(m).',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch06-ham-so-do-thi',
  'context_title': 'Chương VI: Hàm số, đồ thị và ứng dụng',
  'context': 'Chương VI · SGK Toán 10: Hàm số, đồ thị và ứng dụng.',
  'title': 'Bài 17: Dấu của tam thức bậc hai',
  'icon': '⚖️',
  'description': 'Xét dấu của tam thức bậc hai và giải bất phương trình bậc hai một ẩn.',
  'requirements': ['Nhận biết được tam thức bậc hai và vận dụng định lí về dấu của tam thức bậc hai.',
                   'Giải được bất phương trình bậc hai một ẩn và bài toán tìm tham số để tam thức bậc hai '
                   'luôn âm hoặc luôn dương.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Khi $\\Delta > 0$ (hai nghiệm $x_1 < '
                   'x_2$)** (Trong khoảng $(x_1; x_2)$: trái dấu $a$; Ngoài khoảng: cùng dấu $a$) vào giải '
                   'bài tập.'],
  'definition': 'Tam thức bậc hai (đối với $x$) là biểu thức có dạng $f(x) = ax^2 + bx + c$, trong đó $a, b, '
                'c$ là những số thực cho trước và $a \\neq 0$.',
  'theory': 'Định lí về dấu của tam thức bậc hai $f(x) = ax^2 + bx + c$ ($\\Delta = b^2 - 4ac$):\n'
            '- Nếu $\\Delta < 0$ thì $f(x)$ cùng dấu với hệ số $a$ với mọi $x \\in \\mathbb{R}$.\n'
            '- Nếu $\\Delta = 0$ thì $f(x)$ cùng dấu với hệ số $a$ với mọi $x \\neq -\\dfrac{b}{2a}$ và '
            '$f\\left(-\\dfrac{b}{2a}\\right) = 0$.\n'
            '- Nếu $\\Delta > 0$ ($f(x)$ có hai nghiệm $x_1 < x_2$): $f(x)$ trái dấu với $a$ khi $x \\in '
            '(x_1; x_2)$ và cùng dấu với $a$ khi $x \\in (-\\infty; x_1) \\cup (x_2; +\\infty)$ (quy tắc '
            "'trong trái, ngoài cùng').",
  'formulas': [{'category': 'Định lí dấu tam thức bậc hai $f(x) = ax^2 + bx + c$ ($a \\neq 0$)',
                'items': [{'name': 'Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)',
                           'formula': 'Trong khoảng $(x_1; x_2)$: trái dấu $a$; Ngoài khoảng: cùng dấu $a$',
                           'note': "Quy tắc: 'Trong trái, ngoài cùng'"},
                          {'name': 'Điều kiện không đổi dấu trên $\\mathbb{R}$',
                           'formula': '$f(x) > 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow '
                                      '\\begin{cases} a > 0 \\\\ \\Delta < 0 \\end{cases}$; $f(x) \\ge 0, '
                                      '\\forall x \\in \\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 '
                                      '\\\\ \\Delta \\le 0 \\end{cases}$',
                           'note': 'Tương tự với $f(x) < 0$ khi $a < 0, \\Delta < 0$'}]}],
  'example': 'Giải bất phương trình $x^2 - 5x + 6 \\le 0$.',
  'example_answer': 'Tam thức $f(x) = x^2 - 5x + 6$ có $a = 1 > 0$ và hai nghiệm phân biệt $x_1 = 2, x_2 = '
                    '3$.\n'
                    "Theo quy tắc 'trong trái, ngoài cùng', $f(x) \\le 0 \\Leftrightarrow 2 \\le x \\le 3$.\n"
                    'Vậy tập nghiệm của bất phương trình là $S = [2; 3]$.',
  'real_life': 'Xác định khoảng giá bán sản phẩm để lợi nhuận của doanh nghiệp vượt qua một mức mục tiêu cho '
               'trước.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tam thức bậc hai $f(x) = ax^2 + bx + c$ ($a \\neq 0$) có biệt thức $\\Delta < 0$. '
                 'Khẳng định nào sau đây là đúng?',
            'options': ['$f(x)$ cùng dấu với hệ số $a$ với mọi $x \\in \\mathbb{R}$',
                        '$f(x)$ trái dấu với hệ số $a$ với mọi $x \\in \\mathbb{R}$',
                        '$f(x) > 0$ với mọi $x \\in \\mathbb{R}$',
                        '$f(x) < 0$ với mọi $x \\in \\mathbb{R}$'],
            'answer': 0,
            'solution': 'Theo định lí về dấu của tam thức bậc hai, khi $\\Delta < 0$ thì $f(x)$ luôn cùng '
                        'dấu với hệ số $a$ trên $\\mathbb{R}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập nghiệm của bất phương trình $x^2 - 4 < 0$ là:',
            'options': ['$(-\\infty; -2) \\cup (2; +\\infty)$', '$(-2; 2)$', '$[-2; 2]$', '$(-4; 4)$'],
            'answer': 1,
            'solution': 'Tam thức $x^2 - 4$ có $a = 1 > 0$ và hai nghiệm $-2; 2$ nên nhận giá trị âm trong '
                        'khoảng $(-2; 2)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 17: Dấu của tam thức bậc hai**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)**?',
            'options': ['$f(x) > 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 \\\\ '
                        '\\Delta < 0 \\end{cases}$; $f(x) \\ge 0, \\forall x \\in \\mathbb{R} '
                        '\\Leftrightarrow \\begin{cases} a > 0 \\\\ \\Delta \\le 0 \\end{cases}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        'Trong khoảng $(x_1; x_2)$: trái dấu $a$; Ngoài khoảng: cùng dấu $a$',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 17: Dấu của tam thức bậc hai, **Khi $\\Delta '
                        '> 0$ (hai nghiệm $x_1 < x_2$)** được xác định bởi: Trong khoảng $(x_1; x_2)$: trái '
                        "dấu $a$; Ngoài khoảng: cùng dấu $a$. (Quy tắc: 'Trong trái, ngoài cùng')"},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Dấu của tam thức bậc hai**, nội dung/biểu thức $f(x) > 0, \\forall x \\in '
                 '\\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 \\\\ \\Delta < 0 \\end{cases}$; $f(x) '
                 '\\ge 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 \\\\ \\Delta '
                 '\\le 0 \\end{cases}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương',
                        'Điều kiện không đổi dấu trên $\\mathbb{R}$'],
            'answer': 3,
            'solution': 'Trong Bài 17: Dấu của tam thức bậc hai, biểu thức/quy tắc $f(x) > 0, \\forall x '
                        '\\in \\mathbb{R} \\Leftrightarrow \\begin{cases} a > 0 \\\\ \\Delta < 0 '
                        '\\end{cases}$; $f(x) \\ge 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow '
                        '\\begin{cases} a > 0 \\\\ \\Delta \\le 0 \\end{cases}$ chính là nội dung của **Điều '
                        'kiện không đổi dấu trên $\\mathbb{R}$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tam thức bậc hai nào sau đây luôn nhận giá trị dương với mọi $x \\in \\mathbb{R}$?',
            'options': ['$f(x) = x^2 - 2x + 5$',
                        '$f(x) = x^2 - 4x + 4$',
                        '$f(x) = -x^2 + 2x - 3$',
                        '$f(x) = x^2 - 5x + 6$'],
            'answer': 0,
            'solution': 'Tam thức $x^2 - 2x + 5 = (x - 1)^2 + 4 > 0$ với mọi $x \\in \\mathbb{R}$ (vì $a = 1 '
                        "> 0$ và $\\Delta' = -4 < 0$).",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Dấu của tam thức bậc hai** (Chương VI: Hàm số, đồ thị và ứng dụng), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Nhận biết được tam thức bậc hai và vận dụng định lí về dấu của tam thức bậc hai.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 17: Dấu của tam thức bậc hai: Nhận biết được tam thức '
                        'bậc hai và vận dụng định lí về dấu của tam thức bậc hai.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam thức bậc hai $f(x) = -x^2 + 4x - 3$.',
            'statements': ['Hệ số $a = -1 < 0$ và tam thức có hai nghiệm là $x_1 = 1, x_2 = 3$.',
                           '$f(x) > 0$ khi và chỉ khi $x \\in (1; 3)$.',
                           '$f(x) \\le 0$ khi và chỉ khi $x \\in [1; 3]$.',
                           'Tổng các nghiệm nguyên của bất phương trình $f(x) \\ge 0$ bằng $6$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng (trong khoảng hai nghiệm trái dấu với $a = -1$). c) Sai vì $f(x) '
                        '\\le 0 \\Leftrightarrow x \\in (-\\infty; 1] \\cup [3; +\\infty)$. d) Đúng vì các '
                        'nghiệm nguyên thuộc $[1; 3]$ là $1, 2, 3$ có tổng bằng $6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 17: Dấu của tam thức '
                 'bậc hai**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được tam thức bậc hai và '
                           'vận dụng định lí về dấu của tam thức bậc hai.',
                           'Quy tắc/công thức **Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)** trong bài được '
                           'xác định bởi: Trong khoảng $(x_1; x_2)$: trái dấu $a$; Ngoài khoảng: cùng dấu '
                           '$a$.',
                           'Trong mọi trường hợp, **Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)** luôn được '
                           'tính bằng công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh '
                           'đề kéo theo) mà không cần điều kiện của Bài 17: Dấu của tam thức bậc hai.',
                           'Với bài toán minh họa: “Giải bất phương trình $x^2 - 5x + 6 \\le 0$.”, lời giải '
                           'đúng là: Tam thức $f(x) = x^2 - 5x + 6$ có $a = 1 > 0$ và hai nghiệm phân biệt '
                           "$x_1 = 2, x_2 = 3$. Theo quy tắc 'trong trái, ngoài cùng', $f(x) \\le 0 "
                           '\\Leftrightarrow 2 \\le x \\le 3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Dấu của tam thức bậc hai. b) **Đúng** '
                        'theo công thức trọng tâm **Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)** (Trong '
                        'khoảng $(x_1; x_2)$: trái dấu $a$; Ngoài khoảng: cùng dấu $a$). c) **Sai** vì $P '
                        '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Khi $\\Delta > 0$ (hai nghiệm $x_1 < x_2$)**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 17: Dấu của tam thức bậc hai** để giải quyết tình huống sau: Giải '
                 'bất phương trình $x^2 - 5x + 6 \\le 0$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Tam thức $f(x) = x^2 - 5x + 6$ có $a = 1 > 0$ và hai nghiệm phân biệt $x_1 = 2, x_2 '
                        "= 3$. Theo quy tắc 'trong trái, ngoài cùng', $f(x) \\le 0 \\Leftrightarrow 2 \\le x "
                        '\\le 3$...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Dấu của tam thức bậc hai: Tam thức $f(x) = x^2 - 5x '
                        '+ 6$ có $a = 1 > 0$ và hai nghiệm phân biệt $x_1 = 2, x_2 = 3$.\n'
                        "Theo quy tắc 'trong trái, ngoài cùng', $f(x) \\le 0 \\Leftrightarrow 2 \\le x \\le "
                        '3$.\n'
                        'Vậy tập nghiệm của bất phương trình là $S = [2; 3]$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu giá trị nguyên của tham số $m$ để tam thức bậc hai $f(x) = x^2 - 2mx + 9$ '
                 'luôn dương với mọi $x \\in \\mathbb{R}$?',
            'answer': ['5'],
            'unit': None,
            'solution': "Để $f(x) > 0, \\forall x \\in \\mathbb{R}$ thì $\\Delta' = m^2 - 9 < 0 "
                        '\\Leftrightarrow -3 < m < 3$. Các giá trị nguyên của $m$ là $-2; -1; 0; 1; 2$, gồm '
                        '$5$ giá trị.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch06-ham-so-do-thi',
  'context_title': 'Chương VI: Hàm số, đồ thị và ứng dụng',
  'context': 'Chương VI · SGK Toán 10: Hàm số, đồ thị và ứng dụng.',
  'title': 'Bài 18: Phương trình quy về phương trình bậc hai',
  'icon': '🔄',
  'description': 'Giải phương trình chứa căn thức có dạng căn A = căn B và căn A = B quy về phương trình bậc '
                 'hai.',
  'requirements': ['Giải được phương trình dạng $\\sqrt{ax^2 + bx + c} = \\sqrt{dx^2 + ex + f}$.',
                   'Giải được phương trình dạng $\\sqrt{ax^2 + bx + c} = dx + e$ và kiểm tra nghiệm ngoại '
                   'lai.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$** (Bình '
                   'phương hai vế: $A(x) = B(x)$ (với điều kiện $A(x) \\ge 0$)) vào giải bài tập.'],
  'definition': 'Hai dạng phương trình chứa căn thức thường gặp quy về phương trình bậc hai là $\\sqrt{A(x)} '
                '= \\sqrt{B(x)}$ và $\\sqrt{A(x)} = B(x)$, trong đó $A(x)$ là tam thức bậc hai.',
  'theory': '1. Để giải phương trình $\\sqrt{A(x)} = \\sqrt{B(x)}$, ta bình phương hai vế để được phương '
            'trình $A(x) = B(x)$, giải phương trình này rồi thử lại các nghiệm vào phương trình ban đầu '
            '(hoặc đối chiếu điều kiện $A(x) \\ge 0$).\n'
            '2. Để giải phương trình $\\sqrt{A(x)} = B(x)$, ta bình phương hai vế để được phương trình $A(x) '
            '= [B(x)]^2$, giải phương trình này rồi thử lại nghiệm vào phương trình ban đầu (hoặc kết hợp '
            'điều kiện $B(x) \\ge 0$).',
  'formulas': [{'category': 'Các dạng phương trình chứa căn quy về bậc hai',
                'items': [{'name': 'Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$',
                           'formula': 'Bình phương hai vế: $A(x) = B(x)$ (với điều kiện $A(x) \\ge 0$)',
                           'note': 'Thử lại nghiệm vào phương trình đã cho'},
                          {'name': 'Dạng $\\sqrt{A(x)} = B(x)$',
                           'formula': '$\\sqrt{A(x)} = B(x) \\Leftrightarrow \\begin{cases} B(x) \\ge 0 \\\\ '
                                      'A(x) = [B(x)]^2 \\end{cases}$',
                           'note': 'Hoặc bình phương hai vế rồi thử lại nghiệm'}]}],
  'example': 'Giải phương trình $\\sqrt{2x^2 - 3x + 1} = x - 1$.',
  'example_answer': 'Bình phương hai vế của phương trình ta được:\n'
                    '$2x^2 - 3x + 1 = (x - 1)^2 \\Rightarrow 2x^2 - 3x + 1 = x^2 - 2x + 1 \\Rightarrow x^2 - '
                    'x = 0 \\Rightarrow x = 0$ hoặc $x = 1$.\n'
                    'Thử lại vào phương trình ban đầu: Với $x = 0$, vế trái bằng $1$, vế phải bằng $-1$ '
                    '(loại); với $x = 1$, cả hai vế đều bằng $0$ (thỏa mãn).\n'
                    'Vậy phương trình có nghiệm duy nhất $x = 1$.',
  'real_life': 'Xác định vị trí điểm trên bờ sông để tổng thời gian chèo thuyền và chạy bộ đến đích bằng một '
               'giá trị cho trước.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi bình phương hai vế của phương trình $\\sqrt{x^2 + 3} = 2$, ta thu được phương trình '
                 'nào?',
            'options': ['$x^2 + 3 = 2$', '$x^2 + 3 = 4$', '$x + 3 = 4$', '$x^2 + 9 = 4$'],
            'answer': 1,
            'solution': 'Bình phương hai vế ta được $x^2 + 3 = 2^2 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phương trình $\\sqrt{A(x)} = B(x)$ tương đương với hệ nào sau đây?',
            'options': ['$\\begin{cases} A(x) \\ge 0 \\\\ A(x) = [B(x)]^2 \\end{cases}$',
                        '$\\begin{cases} B(x) \\ge 0 \\\\ A(x) = B(x) \\end{cases}$',
                        '$\\begin{cases} B(x) \\ge 0 \\\\ A(x) = [B(x)]^2 \\end{cases}$',
                        '$\\begin{cases} A(x) \\le 0 \\\\ A(x) = [B(x)]^2 \\end{cases}$'],
            'answer': 2,
            'solution': 'Khi $B(x) \\ge 0$ và $A(x) = [B(x)]^2$ thì hiển nhiên $A(x) \\ge 0$, nên hai điều '
                        'kiện này là tương đương với phương trình.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 18: Phương trình quy về phương trình bậc hai**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$**?',
            'options': ['$\\sqrt{A(x)} = B(x) \\Leftrightarrow \\begin{cases} B(x) \\ge 0 \\\\ A(x) = '
                        '[B(x)]^2 \\end{cases}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai',
                        'Bình phương hai vế: $A(x) = B(x)$ (với điều kiện $A(x) \\ge 0$)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 18: Phương trình quy về phương trình bậc hai, '
                        '**Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$** được xác định bởi: Bình phương hai vế: $A(x) '
                        '= B(x)$ (với điều kiện $A(x) \\ge 0$). (Thử lại nghiệm vào phương trình đã cho)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Phương trình quy về phương trình bậc hai**, nội dung/biểu thức '
                 '$\\sqrt{A(x)} = B(x) \\Leftrightarrow \\begin{cases} B(x) \\ge 0 \\\\ A(x) = [B(x)]^2 '
                 '\\end{cases}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Dạng $\\sqrt{A(x)} = B(x)$',
                        'Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương'],
            'answer': 0,
            'solution': 'Trong Bài 18: Phương trình quy về phương trình bậc hai, biểu thức/quy tắc '
                        '$\\sqrt{A(x)} = B(x) \\Leftrightarrow \\begin{cases} B(x) \\ge 0 \\\\ A(x) = '
                        '[B(x)]^2 \\end{cases}$ chính là nội dung của **Dạng $\\sqrt{A(x)} = B(x)$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tập nghiệm của phương trình $\\sqrt{x^2 - 2x + 4} = x$ là:',
            'options': ['$S = \\{-2; 2\\}$', '$S = \\{2\\}$', '$S = \\varnothing$', '$S = \\{0; 2\\}$'],
            'answer': 1,
            'solution': 'Với $x \\ge 0$, bình phương hai vế được $x^2 - 2x + 4 = x^2 \\Rightarrow 2x = 4 '
                        '\\Rightarrow x = 2$ (thỏa mãn).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Phương trình quy về phương trình bậc hai** (Chương VI: Hàm số, đồ thị và '
                 'ứng dụng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Giải được phương trình dạng $\\sqrt{ax^2 + bx + c} = \\sqrt{dx^2 + ex + f}$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 18: Phương trình quy về phương trình bậc hai: Giải '
                        'được phương trình dạng $\\sqrt{ax^2 + bx + c} = \\sqrt{dx^2 + ex + f}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình $\\sqrt{x^2 + x - 2} = \\sqrt{2x + 4}$ (1).',
            'statements': ['Bình phương hai vế của (1) ta được phương trình $x^2 - x - 6 = 0$.',
                           'Phương trình $x^2 - x - 6 = 0$ có hai nghiệm là $x = 3$ và $x = -2$.',
                           'Thay $x = -2$ vào phương trình (1) ta thấy hai vế đều có nghĩa và bằng $0$.',
                           'Phương trình (1) chỉ có duy nhất một nghiệm là $x = 3$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $x^2 + x - 2 = 2x + 4 \\Leftrightarrow x^2 - x - 6 = 0$. b) Đúng. c) '
                        'Đúng vì tại $x = -2$, $2x + 4 = 0 \\ge 0$. d) Sai vì phương trình có hai nghiệm là '
                        '$x = 3$ và $x = -2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 18: Phương trình quy về '
                 'phương trình bậc hai**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Giải được phương trình dạng '
                           '$\\sqrt{ax^2 + bx + c} = \\sqrt{dx^2 + ex + f}$.',
                           'Quy tắc/công thức **Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$** trong bài được xác định '
                           'bởi: Bình phương hai vế: $A(x) = B(x)$ (với điều kiện $A(x) \\ge 0$).',
                           'Trong mọi trường hợp, **Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$** luôn được tính bằng '
                           'công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo '
                           'theo) mà không cần điều kiện của Bài 18: Phương trình quy về phương trình bậc '
                           'hai.',
                           'Với bài toán minh họa: “Giải phương trình $\\sqrt{2x^2 - 3x + 1} = x - 1$.”, lời '
                           'giải đúng là: Bình phương hai vế của phương trình ta được: $2x^2 - 3x + 1 = (x - '
                           '1)^2 \\Rightarrow 2x^2 - 3x + 1 = x^2 - 2x + 1 \\Rightarrow x^2 - x = 0 '
                           '\\Rightarrow x = 0$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Phương trình quy về phương trình bậc '
                        'hai. b) **Đúng** theo công thức trọng tâm **Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$** '
                        '(Bình phương hai vế: $A(x) = B(x)$ (với điều kiện $A(x) \\ge 0$)). c) **Sai** vì $P '
                        '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Dạng $\\sqrt{A(x)} = \\sqrt{B(x)}$**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 18: Phương trình quy về phương trình bậc hai** để giải quyết tình '
                 'huống sau: Giải phương trình $\\sqrt{2x^2 - 3x + 1} = x - 1$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        'Bình phương hai vế của phương trình ta được: $2x^2 - 3x + 1 = (x - 1)^2 '
                        '\\Rightarrow 2x^2 - 3x + 1 = x^2 - 2x + 1 \\Rightarrow x^2 - x = 0 \\Rightarrow x = '
                        '0$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Phương trình quy về phương trình bậc hai: Bình '
                        'phương hai vế của phương trình ta được:\n'
                        '$2x^2 - 3x + 1 = (x - 1)^2 \\Rightarrow 2x^2 - 3x + 1 = x^2 - 2x + 1 \\Rightarrow '
                        'x^2 - x = 0 \\Rightarrow x = 0$ hoặc $x = 1$.\n'
                        'Thử lại vào phương trình ban đầu: Với $x = 0$, vế trái bằng $1$, vế phải bằng $-1$ '
                        '(loại); với $x = 1$, cả hai vế đều bằng $0$ (thỏa mãn).\n'
                        'Vậy phương trình có nghiệm duy nhất $x = 1$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Giải phương trình $\\sqrt{x^2 + 5} = x + 1$ được nghiệm $x$ bằng bao nhiêu?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Điều kiện $x \\ge -1$. Bình phương hai vế: $x^2 + 5 = (x + 1)^2 = x^2 + 2x + 1 '
                        '\\Rightarrow 2x = 4 \\Rightarrow x = 2$ (thỏa mãn).',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch07-toa-do-mat-phang',
  'context_title': 'Chương VII: Phương pháp tọa độ trong mặt phẳng',
  'context': 'Chương VII · SGK Toán 10: Phương pháp tọa độ trong mặt phẳng.',
  'title': 'Bài 19: Phương trình đường thẳng',
  'icon': '📏',
  'description': 'Xác định vectơ chỉ phương, vectơ pháp tuyến và lập phương trình tham số, phương trình tổng '
                 'quát của đường thẳng.',
  'requirements': ['Nhận biết và chuyển đổi được giữa vectơ chỉ phương và vectơ pháp tuyến của một đường '
                   'thẳng.',
                   'Lập được phương trình tham số và phương trình tổng quát của đường thẳng khi biết một '
                   'điểm và vectơ chỉ phương (hoặc vectơ pháp tuyến), hoặc biết hai điểm.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Liên hệ giữa VTCP và VTPT** '
                   '($\\overrightarrow{u} = (a; b) \\leftrightarrow \\overrightarrow{n} = (-b; a)$ hoặc $(b; '
                   '-a)$) vào giải bài tập.'],
  'definition': 'Vectơ $\\overrightarrow{u} \\neq \\overrightarrow{0}$ có giá song song hoặc trùng với đường '
                'thẳng $\\Delta$ gọi là vectơ chỉ phương (VTCP) của $\\Delta$. Vectơ $\\overrightarrow{n} '
                '\\neq \\overrightarrow{0}$ có giá vuông góc với $\\Delta$ gọi là vectơ pháp tuyến (VTPT) '
                'của $\\Delta$.',
  'theory': '1. Nếu $\\Delta$ có VTCP $\\overrightarrow{u} = (a; b)$ thì có một VTPT là $\\overrightarrow{n} '
            '= (-b; a)$ (hoặc $(b; -a)$) vì $\\overrightarrow{u} \\cdot \\overrightarrow{n} = 0$.\n'
            '2. Đường thẳng $\\Delta$ đi qua $M_0(x_0; y_0)$ và có VTCP $\\overrightarrow{u} = (a; b)$ có '
            'phương trình tham số: $\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\end{cases}$ ($t \\in '
            '\\mathbb{R}$).\n'
            '3. Đường thẳng $\\Delta$ đi qua $M_0(x_0; y_0)$ và có VTPT $\\overrightarrow{n} = (a; b)$ có '
            'phương trình tổng quát: $a(x - x_0) + b(y - y_0) = 0 \\Leftrightarrow ax + by + c = 0$.',
  'formulas': [{'category': 'Các dạng phương trình đường thẳng',
                'items': [{'name': 'Liên hệ giữa VTCP và VTPT',
                           'formula': '$\\overrightarrow{u} = (a; b) \\leftrightarrow \\overrightarrow{n} = '
                                      '(-b; a)$ hoặc $(b; -a)$',
                           'note': '$\\overrightarrow{u} \\perp \\overrightarrow{n}$'},
                          {'name': 'Phương trình tham số',
                           'formula': '$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\end{cases}$ ($t \\in '
                                      '\\mathbb{R}$)',
                           'note': 'Đi qua $M_0(x_0; y_0)$, VTCP $\\overrightarrow{u} = (a; b)$'},
                          {'name': 'Phương trình tổng quát',
                           'formula': '$a(x - x_0) + b(y - y_0) = 0$',
                           'note': 'Đi qua $M_0(x_0; y_0)$, VTPT $\\overrightarrow{n} = (a; b)$'}]}],
  'example': 'Lập phương trình tổng quát của đường thẳng $d$ đi qua điểm $A(2; -1)$ và có vectơ pháp tuyến '
             '$\\overrightarrow{n} = (3; 4)$.',
  'example_answer': 'Phương trình tổng quát của đường thẳng $d$ là:\n'
                    '$3(x - 2) + 4(y + 1) = 0 \\Leftrightarrow 3x + 4y - 2 = 0$.',
  'real_life': 'Mô tả quỹ đạo chuyển động thẳng của robot hoặc tàu biển theo tham số thời gian $t$ trên bản '
               'đồ tọa độ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một vectơ pháp tuyến của đường thẳng $d: 2x - 3y + 5 = 0$ là:',
            'options': ['$\\overrightarrow{n} = (3; 2)$',
                        '$\\overrightarrow{n} = (2; 3)$',
                        '$\\overrightarrow{n} = (2; -3)$',
                        '$\\overrightarrow{n} = (-3; 2)$'],
            'answer': 2,
            'solution': 'Đường thẳng $ax + by + c = 0$ có một vectơ pháp tuyến là $\\overrightarrow{n} = (a; '
                        'b) = (2; -3)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đường thẳng $\\Delta$ có phương trình tham số $\\begin{cases} x = 1 + 2t \\\\ y = -3 + '
                 '5t \\end{cases}$. Một vectơ chỉ phương của $\\Delta$ là:',
            'options': ['$\\overrightarrow{u} = (1; -3)$',
                        '$\\overrightarrow{u} = (5; -2)$',
                        '$\\overrightarrow{u} = (2; -5)$',
                        '$\\overrightarrow{u} = (2; 5)$'],
            'answer': 3,
            'solution': 'Hệ số của tham số $t$ cho tọa độ vectơ chỉ phương $\\overrightarrow{u} = (2; 5)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 19: Phương trình đường thẳng**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Liên hệ giữa VTCP và VTPT**?',
            'options': ['$\\overrightarrow{u} = (a; b) \\leftrightarrow \\overrightarrow{n} = (-b; a)$ hoặc '
                        '$(b; -a)$',
                        '$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\end{cases}$ ($t \\in \\mathbb{R}$)',
                        '$a(x - x_0) + b(y - y_0) = 0$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 19: Phương trình đường thẳng, **Liên hệ giữa '
                        'VTCP và VTPT** được xác định bởi: $\\overrightarrow{u} = (a; b) \\leftrightarrow '
                        '\\overrightarrow{n} = (-b; a)$ hoặc $(b; -a)$. ($\\overrightarrow{u} \\perp '
                        '\\overrightarrow{n}$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Phương trình đường thẳng**, nội dung/biểu thức $\\begin{cases} x = x_0 + '
                 'at \\\\ y = y_0 + bt \\end{cases}$ ($t \\in \\mathbb{R}$) là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Liên hệ giữa VTCP và VTPT',
                        'Phương trình tham số',
                        'Phương trình tổng quát',
                        'Mệnh đề kéo theo'],
            'answer': 1,
            'solution': 'Trong Bài 19: Phương trình đường thẳng, biểu thức/quy tắc $\\begin{cases} x = x_0 + '
                        'at \\\\ y = y_0 + bt \\end{cases}$ ($t \\in \\mathbb{R}$) chính là nội dung của '
                        '**Phương trình tham số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phương trình tổng quát của đường thẳng đi qua điểm $M(1; 2)$ và có vectơ chỉ phương '
                 '$\\overrightarrow{u} = (3; -1)$ là:',
            'options': ['$3x - y - 1 = 0$', '$x - 3y + 5 = 0$', '$x + 3y - 7 = 0$', '$3x + y - 5 = 0$'],
            'answer': 2,
            'solution': 'Vì VTCP $\\overrightarrow{u} = (3; -1)$ nên VTPT là $\\overrightarrow{n} = (1; 3)$. '
                        'Phương trình là $1(x - 1) + 3(y - 2) = 0 \\Leftrightarrow x + 3y - 7 = 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Phương trình đường thẳng** (Chương VII: Phương pháp tọa độ trong mặt '
                 'phẳng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Nhận biết và chuyển đổi được giữa vectơ chỉ phương và vectơ pháp tuyến của một '
                        'đường thẳng.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 19: Phương trình đường thẳng: Nhận biết và chuyển đổi '
                        'được giữa vectơ chỉ phương và vectơ pháp tuyến của một đường thẳng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $\\Delta$ đi qua hai điểm $A(1; 2)$ và $B(3; '
                 '6)$.',
            'statements': ['Vectơ $\\overrightarrow{AB} = (2; 4)$ là một vectơ chỉ phương của đường thẳng '
                           '$\\Delta$.',
                           'Vectơ $\\overrightarrow{n} = (2; -1)$ là một vectơ pháp tuyến của đường thẳng '
                           '$\\Delta$.',
                           'Phương trình tổng quát của đường thẳng $\\Delta$ là $2x - y = 0$.',
                           'Điểm $C(2; 5)$ nằm trên đường thẳng $\\Delta$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $\\overrightarrow{n} \\cdot \\overrightarrow{AB} = 2(2) + '
                        '(-1)(4) = 0$. c) Đúng vì $2(x - 1) - 1(y - 2) = 0 \\Leftrightarrow 2x - y = 0$. d) '
                        'Sai vì $2(2) - 5 = -1 \\neq 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 19: Phương trình đường '
                 'thẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết và chuyển đổi được giữa '
                           'vectơ chỉ phương và vectơ pháp tuyến của một đường thẳng.',
                           'Quy tắc/công thức **Liên hệ giữa VTCP và VTPT** trong bài được xác định bởi: '
                           '$\\overrightarrow{u} = (a; b) \\leftrightarrow \\overrightarrow{n} = (-b; a)$ '
                           'hoặc $(b; -a)$.',
                           'Trong mọi trường hợp, **Liên hệ giữa VTCP và VTPT** luôn được tính bằng công '
                           'thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) '
                           'mà không cần điều kiện của Bài 19: Phương trình đường thẳng.',
                           'Với bài toán minh họa: “Lập phương trình tổng quát của đường thẳng $d$ đi qua '
                           'điểm $A(2; -1)$ và có vectơ pháp tuyến $\\overrightarrow{n} = (3; 4)$.”, lời '
                           'giải đúng là: Phương trình tổng quát của đường thẳng $d$ là: $3(x - 2) + 4(y + '
                           '1) = 0 \\Leftrightarrow 3x + 4y - 2 = 0$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Phương trình đường thẳng. b) **Đúng** '
                        'theo công thức trọng tâm **Liên hệ giữa VTCP và VTPT** ($\\overrightarrow{u} = (a; '
                        'b) \\leftrightarrow \\overrightarrow{n} = (-b; a)$ hoặc $(b; -a)$). c) **Sai** vì '
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Liên hệ giữa VTCP và VTPT**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 19: Phương trình đường thẳng** để giải quyết tình huống sau: Lập '
                 'phương trình tổng quát của đường thẳng $d$ đi qua điểm $A(2; -1)$ và có vectơ pháp tuyến '
                 '$\\overrightarrow{n} = (3; 4)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Phương trình tổng quát của đường thẳng $d$ là: $3(x - 2) + 4(y + 1) = 0 '
                        '\\Leftrightarrow 3x + 4y - 2 = 0$.',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Phương trình đường thẳng: Phương trình tổng quát của '
                        'đường thẳng $d$ là:\n'
                        '$3(x - 2) + 4(y + 1) = 0 \\Leftrightarrow 3x + 4y - 2 = 0$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Đường thẳng $d: 3x + 4y - 12 = 0$ cắt trục hoành tại điểm $A$ và cắt trục tung tại điểm '
                 '$B$. Tính diện tích tam giác $OAB$ (với $O$ là gốc tọa độ).',
            'answer': ['6'],
            'unit': None,
            'solution': 'Cho $y = 0 \\Rightarrow x = 4 \\Rightarrow A(4; 0)$; cho $x = 0 \\Rightarrow y = 3 '
                        '\\Rightarrow B(0; 3)$. Diện tích tam giác vuông $OAB$ là $S = \\dfrac{1}{2} OA '
                        '\\cdot OB = \\dfrac{1}{2} \\cdot 4 \\cdot 3 = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch07-toa-do-mat-phang',
  'context_title': 'Chương VII: Phương pháp tọa độ trong mặt phẳng',
  'context': 'Chương VII · SGK Toán 10: Phương pháp tọa độ trong mặt phẳng.',
  'title': 'Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng cách',
  'icon': '📐',
  'description': 'Xét vị trí tương đối giữa hai đường thẳng, tính góc giữa hai đường thẳng và khoảng cách từ '
                 'một điểm đến một đường thẳng.',
  'requirements': ['Xác định được vị trí tương đối (cắt nhau, song song, trùng nhau) và tính được góc giữa '
                   'hai đường thẳng ($0^\\circ \\le \\varphi \\le 90^\\circ$).',
                   'Tính được khoảng cách từ một điểm đến một đường thẳng.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Côsin góc giữa hai đường thẳng** '
                   '($\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1a_2 + b_1b_2|}{\\sqrt{a_1^2 + '
                   'b_1^2}\\sqrt{a_2^2 + b_2^2}}$) vào giải bài tập.'],
  'definition': 'Góc giữa hai đường thẳng $\\Delta_1$ và $\\Delta_2$ là góc nhỏ nhất tạo bởi hai đường thẳng '
                'đó, luôn thỏa mãn $0^\\circ \\le (\\Delta_1, \\Delta_2) \\le 90^\\circ$.',
  'theory': '1. Vị trí tương đối của $\\Delta_1: a_1x + b_1y + c_1 = 0$ và $\\Delta_2: a_2x + b_2y + c_2 = '
            '0$ phụ thuộc vào số nghiệm của hệ phương trình tạo bởi hai đường thẳng.\n'
            '2. Góc $\\varphi$ giữa $\\Delta_1$ (VTPT $\\overrightarrow{n_1} = (a_1; b_1)$) và $\\Delta_2$ '
            '(VTPT $\\overrightarrow{n_2} = (a_2; b_2)$): $\\cos \\varphi = |\\cos(\\overrightarrow{n_1}, '
            '\\overrightarrow{n_2})| = \\dfrac{|a_1a_2 + b_1b_2|}{\\sqrt{a_1^2 + b_1^2}\\sqrt{a_2^2 + '
            'b_2^2}}$.\n'
            '3. Khoảng cách từ điểm $M_0(x_0; y_0)$ đến đường thẳng $\\Delta: ax + by + c = 0$ là $d(M_0, '
            '\\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$.',
  'formulas': [{'category': 'Công thức góc và khoảng cách',
                'items': [{'name': 'Côsin góc giữa hai đường thẳng',
                           'formula': '$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1a_2 + '
                                      'b_1b_2|}{\\sqrt{a_1^2 + b_1^2}\\sqrt{a_2^2 + b_2^2}}$',
                           'note': '$\\Delta_1 \\perp \\Delta_2 \\Leftrightarrow a_1a_2 + b_1b_2 = 0$'},
                          {'name': 'Khoảng cách từ điểm đến đường thẳng',
                           'formula': '$d(M_0, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$',
                           'note': 'Với $M_0(x_0; y_0)$ và $\\Delta: ax + by + c = 0$'}]}],
  'example': 'Tính khoảng cách từ điểm $M(1; -2)$ đến đường thẳng $\\Delta: 3x - 4y - 1 = 0$.',
  'example_answer': 'Áp dụng công thức khoảng cách:\n'
                    '$d(M, \\Delta) = \\dfrac{|3(1) - 4(-2) - 1|}{\\sqrt{3^2 + (-4)^2}} = \\dfrac{|3 + 8 - '
                    '1|}{5} = \\dfrac{10}{5} = 2$.',
  'real_life': 'Tính chiều dài đoạn đường ngắn nhất cần mở để nối từ một ngôi làng đến tuyến đường cao tốc '
               'chạy thẳng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khoảng cách từ điểm $M(x_0; y_0)$ đến đường thẳng $\\Delta: ax + by + c = 0$ ($a^2 + b^2 > '
                 '0$) được tính bằng công thức:',
            'options': ['$d(M, \\Delta) = \\dfrac{ax_0 + by_0 + c}{\\sqrt{a^2 + b^2}}$',
                        '$d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{a^2 + b^2}$',
                        '$d(M, \\Delta) = \\dfrac{|ax_0 + by_0|}{\\sqrt{a^2 + b^2}}$',
                        '$d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$'],
            'answer': 3,
            'solution': 'Theo công thức SGK, $d(M, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + '
                        'b^2}}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đường thẳng $d_1: 2x - y + 1 = 0$ và $d_2: 4x - 2y + 5 = 0$ có vị trí tương đối là:',
            'options': ['Song song', 'Cắt nhau', 'Trùng nhau', 'Vuông góc'],
            'answer': 0,
            'solution': 'Vì $\\dfrac{2}{4} = \\dfrac{-1}{-2} \\neq \\dfrac{1}{5}$ nên hai đường thẳng song '
                        'song với nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng '
                 'cách**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Côsin góc giữa hai đường '
                 'thẳng**?',
            'options': ['$d(M_0, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$',
                        '$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1a_2 + b_1b_2|}{\\sqrt{a_1^2 + '
                        'b_1^2}\\sqrt{a_2^2 + b_2^2}}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 20: Vị trí tương đối giữa hai đường thẳng, '
                        'góc và khoảng cách, **Côsin góc giữa hai đường thẳng** được xác định bởi: '
                        '$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1a_2 + b_1b_2|}{\\sqrt{a_1^2 + '
                        'b_1^2}\\sqrt{a_2^2 + b_2^2}}$. ($\\Delta_1 \\perp \\Delta_2 \\Leftrightarrow a_1a_2 '
                        '+ b_1b_2 = 0$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng cách**, nội dung/biểu '
                 'thức $d(M_0, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Côsin góc giữa hai đường thẳng',
                        'Mệnh đề kéo theo',
                        'Khoảng cách từ điểm đến đường thẳng',
                        'Mệnh đề tương đương'],
            'answer': 2,
            'solution': 'Trong Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng cách, biểu '
                        'thức/quy tắc $d(M_0, \\Delta) = \\dfrac{|ax_0 + by_0 + c|}{\\sqrt{a^2 + b^2}}$ '
                        'chính là nội dung của **Khoảng cách từ điểm đến đường thẳng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Góc giữa hai đường thẳng $\\Delta_1: x - 2y + 3 = 0$ và $\\Delta_2: 3x - y - 1 = 0$ bằng:',
            'options': ['$60^\\circ$', '$30^\\circ$', '$90^\\circ$', '$45^\\circ$'],
            'answer': 3,
            'solution': 'Ta có $\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|1 \\cdot 3 + '
                        '(-2)(-1)|}{\\sqrt{5}\\sqrt{10}} = \\dfrac{5}{5\\sqrt{2}} = \\dfrac{\\sqrt{2}}{2} '
                        '\\Rightarrow (\\Delta_1, \\Delta_2) = 45^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng cách** (Chương VII: '
                 'Phương pháp tọa độ trong mặt phẳng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Xác định được vị trí tương đối (cắt nhau, song song, trùng nhau) và tính được góc '
                        'giữa hai đường thẳng ($0^\\circ \\le \\varphi \\le 90^\\circ$).',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và '
                        'khoảng cách: Xác định được vị trí tương đối (cắt nhau, song song, trùng nhau) và '
                        'tính được góc giữa hai đường thẳng ($0^\\circ \\le \\varphi \\le 90^\\circ$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho hai đường thẳng $d_1: 3x + 4y - 10 = 0$ và $d_2: 4x - 3y '
                 '+ 5 = 0$.',
            'statements': ['Hai đường thẳng $d_1$ và $d_2$ vuông góc với nhau.',
                           'Giao điểm của hai đường thẳng $d_1$ và $d_2$ là điểm $I\\left(\\dfrac{2}{5}; '
                           '\\dfrac{11}{5}\\right)$.',
                           'Khoảng cách từ gốc tọa độ $O(0; 0)$ đến đường thẳng $d_1$ bằng $2$.',
                           'Khoảng cách từ gốc tọa độ $O(0; 0)$ đến đường thẳng $d_2$ bằng $5$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $3 \\cdot 4 + 4 \\cdot (-3) = 0$. b) Đúng (giải hệ phương trình). c) '
                        'Đúng vì $d(O, d_1) = \\dfrac{|-10|}{5} = 2$. d) Sai vì $d(O, d_2) = \\dfrac{|5|}{5} '
                        '= 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 20: Vị trí tương đối '
                 'giữa hai đường thẳng, góc và khoảng cách**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được vị trí tương đối '
                           '(cắt nhau, song song, trùng nhau) và tính được góc giữa hai đường thẳng '
                           '($0^\\circ \\le \\varphi \\le 90^\\circ$).',
                           'Quy tắc/công thức **Côsin góc giữa hai đường thẳng** trong bài được xác định '
                           'bởi: $\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1a_2 + b_1b_2|}{\\sqrt{a_1^2 + '
                           'b_1^2}\\sqrt{a_2^2 + b_2^2}}$.',
                           'Trong mọi trường hợp, **Côsin góc giữa hai đường thẳng** luôn được tính bằng '
                           'công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo '
                           'theo) mà không cần điều kiện của Bài 20: Vị trí tương đối giữa hai đường thẳng, '
                           'góc và khoảng cách.',
                           'Với bài toán minh họa: “Tính khoảng cách từ điểm $M(1; -2)$ đến đường thẳng '
                           '$\\Delta: 3x - 4y - 1 = 0$.”, lời giải đúng là: Áp dụng công thức khoảng cách: '
                           '$d(M, \\Delta) = \\dfrac{|3(1) - 4(-2) - 1|}{\\sqrt{3^2 + (-4)^2}} = \\dfrac{|3 '
                           '+ 8 - 1|}{5} = \\dfrac{10}{5} = 2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 20: Vị trí tương đối giữa hai đường thẳng, '
                        'góc và khoảng cách. b) **Đúng** theo công thức trọng tâm **Côsin góc giữa hai đường '
                        'thẳng** ($\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|a_1a_2 + b_1b_2|}{\\sqrt{a_1^2 + '
                        'b_1^2}\\sqrt{a_2^2 + b_2^2}}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ '
                        'đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung của **Côsin '
                        'góc giữa hai đường thẳng**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng cách** '
                 'để giải quyết tình huống sau: Tính khoảng cách từ điểm $M(1; -2)$ đến đường thẳng '
                 '$\\Delta: 3x - 4y - 1 = 0$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Áp dụng công thức khoảng cách: $d(M, \\Delta) = \\dfrac{|3(1) - 4(-2) - '
                        '1|}{\\sqrt{3^2 + (-4)^2}} = \\dfrac{|3 + 8 - 1|}{5} = \\dfrac{10}{5} = 2$.',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng '
                        'cách: Áp dụng công thức khoảng cách:\n'
                        '$d(M, \\Delta) = \\dfrac{|3(1) - 4(-2) - 1|}{\\sqrt{3^2 + (-4)^2}} = \\dfrac{|3 + 8 '
                        '- 1|}{5} = \\dfrac{10}{5} = 2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính khoảng cách từ điểm $A(2; 3)$ đến đường thẳng $\\Delta: 4x + 3y + 3 = 0$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $d(A, \\Delta) = \\dfrac{|4(2) + 3(3) + 3|}{\\sqrt{4^2 + 3^2}} = '
                        '\\dfrac{20}{5} = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch07-toa-do-mat-phang',
  'context_title': 'Chương VII: Phương pháp tọa độ trong mặt phẳng',
  'context': 'Chương VII · SGK Toán 10: Phương pháp tọa độ trong mặt phẳng.',
  'title': 'Bài 21: Đường tròn trong mặt phẳng tọa độ',
  'icon': '⭕',
  'description': 'Xác định tâm, bán kính và viết phương trình đường tròn, phương trình tiếp tuyến của đường '
                 'tròn.',
  'requirements': ['Tìm được tọa độ tâm $I$ và bán kính $R$ của đường tròn từ phương trình chính tắc hoặc '
                   'phương trình dạng khai triển.',
                   'Viết được phương trình đường tròn và phương trình tiếp tuyến của đường tròn tại một điểm '
                   'thuộc đường tròn.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Phương trình đường tròn tâm $I(a; b)$, bán '
                   'kính $R$** ($(x - a)^2 + (y - b)^2 = R^2$) vào giải bài tập.'],
  'definition': 'Phương trình đường tròn $(C)$ có tâm $I(a; b)$ và bán kính $R > 0$ là $(x - a)^2 + (y - '
                'b)^2 = R^2$.',
  'theory': '1. Phương trình dạng khai triển $x^2 + y^2 - 2ax - 2by + c = 0$ là phương trình của một đường '
            'tròn khi và chỉ khi $a^2 + b^2 - c > 0$. Khi đó đường tròn có tâm $I(a; b)$ và bán kính $R = '
            '\\sqrt{a^2 + b^2 - c}$.\n'
            '2. Tiếp tuyến của đường tròn $(C)$ tâm $I(a; b)$ tại điểm $M_0(x_0; y_0) \\in (C)$ đi qua $M_0$ '
            'và nhận vectơ $\\overrightarrow{IM_0} = (x_0 - a; y_0 - b)$ làm vectơ pháp tuyến.',
  'formulas': [{'category': 'Phương trình đường tròn và tiếp tuyến',
                'items': [{'name': 'Phương trình đường tròn tâm $I(a; b)$, bán kính $R$',
                           'formula': '$(x - a)^2 + (y - b)^2 = R^2$',
                           'note': 'Mọi điểm $M(x; y) \\in (C) \\Leftrightarrow IM = R$'},
                          {'name': 'Dạng khai triển',
                           'formula': '$x^2 + y^2 - 2ax - 2by + c = 0$ ($a^2 + b^2 - c > 0$)',
                           'note': 'Tâm $I(a; b)$, bán kính $R = \\sqrt{a^2 + b^2 - c}$'},
                          {'name': 'Tiếp tuyến tại $M_0(x_0; y_0) \\in (C)$',
                           'formula': '$(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0$',
                           'note': 'Nhận $\\overrightarrow{IM_0}$ làm vectơ pháp tuyến'}]}],
  'example': 'Tìm tâm và bán kính của đường tròn $(C): x^2 + y^2 - 4x + 6y - 12 = 0$.',
  'example_answer': 'Phương trình có dạng $x^2 + y^2 - 2ax - 2by + c = 0$ với $a = 2, b = -3, c = -12$.\n'
                    'Vậy đường tròn $(C)$ có tâm $I(2; -3)$ và bán kính $R = \\sqrt{2^2 + (-3)^2 - (-12)} = '
                    '\\sqrt{4 + 9 + 12} = 5$.',
  'real_life': 'Xác định phương trình biên vùng an toàn hình tròn xung quanh tâm chấn hoặc trạm phát sóng '
               'trên bản đồ tọa độ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đường tròn $(C): (x - 2)^2 + (y + 3)^2 = 16$ có tâm $I$ và bán kính $R$ là:',
            'options': ['$I(2; -3), R = 4$', '$I(-2; 3), R = 4$', '$I(2; -3), R = 16$', '$I(-2; 3), R = 16$'],
            'answer': 0,
            'solution': 'So sánh với $(x - a)^2 + (y - b)^2 = R^2$ ta được tâm $I(2; -3)$ và bán kính $R = '
                        '\\sqrt{16} = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phương trình đường tròn có tâm $O(0; 0)$ và bán kính $R = 3$ là:',
            'options': ['$x^2 + y^2 = 3$',
                        '$x^2 + y^2 = 9$',
                        '$(x - 3)^2 + (y - 3)^2 = 9$',
                        '$x^2 - y^2 = 9$'],
            'answer': 1,
            'solution': 'Thay $a = 0, b = 0, R = 3$ vào phương trình đường tròn ta được $x^2 + y^2 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 21: Đường tròn trong mặt phẳng tọa độ**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Phương trình đường tròn tâm $I(a; b)$, bán kính '
                 '$R$**?',
            'options': ['$x^2 + y^2 - 2ax - 2by + c = 0$ ($a^2 + b^2 - c > 0$)',
                        '$(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0$',
                        '$(x - a)^2 + (y - b)^2 = R^2$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 21: Đường tròn trong mặt phẳng tọa độ, '
                        '**Phương trình đường tròn tâm $I(a; b)$, bán kính $R$** được xác định bởi: $(x - '
                        'a)^2 + (y - b)^2 = R^2$. (Mọi điểm $M(x; y) \\in (C) \\Leftrightarrow IM = R$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Đường tròn trong mặt phẳng tọa độ**, nội dung/biểu thức $x^2 + y^2 - 2ax - '
                 '2by + c = 0$ ($a^2 + b^2 - c > 0$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phương trình đường tròn tâm $I(a; b)$, bán kính $R$',
                        'Tiếp tuyến tại $M_0(x_0; y_0) \\in (C)$',
                        'Mệnh đề kéo theo',
                        'Dạng khai triển'],
            'answer': 3,
            'solution': 'Trong Bài 21: Đường tròn trong mặt phẳng tọa độ, biểu thức/quy tắc $x^2 + y^2 - 2ax '
                        '- 2by + c = 0$ ($a^2 + b^2 - c > 0$) chính là nội dung của **Dạng khai triển**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phương trình nào sau đây là phương trình của một đường tròn?',
            'options': ['$x^2 + y^2 - 2x + 4y - 4 = 0$',
                        '$x^2 + y^2 - 2x + 4y + 6 = 0$',
                        '$2x^2 + y^2 - 4x + 2y - 1 = 0$',
                        '$x^2 - y^2 - 2x + 4y - 4 = 0$'],
            'answer': 0,
            'solution': 'Với $x^2 + y^2 - 2x + 4y - 4 = 0$, ta có $a = 1, b = -2, c = -4 \\Rightarrow a^2 + '
                        'b^2 - c = 1 + 4 + 4 = 9 > 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Đường tròn trong mặt phẳng tọa độ** (Chương VII: Phương pháp tọa độ '
                 'trong mặt phẳng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Tìm được tọa độ tâm $I$ và bán kính $R$ của đường tròn từ phương trình chính tắc '
                        'hoặc phương trình dạng khai triển.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 21: Đường tròn trong mặt phẳng tọa độ: Tìm được tọa độ '
                        'tâm $I$ và bán kính $R$ của đường tròn từ phương trình chính tắc hoặc phương trình '
                        'dạng khai triển.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho đường tròn $(C): (x - 1)^2 + (y - 2)^2 = 25$.',
            'statements': ['Đường tròn $(C)$ có tâm $I(1; 2)$ và bán kính $R = 5$.',
                           'Điểm $M(4; 6)$ nằm trên đường tròn $(C)$.',
                           'Vectơ $\\overrightarrow{IM} = (3; 4)$ là một vectơ pháp tuyến của tiếp tuyến với '
                           '$(C)$ tại $M(4; 6)$.',
                           'Phương trình tiếp tuyến của $(C)$ tại điểm $M(4; 6)$ là $3x + 4y - 12 = 0$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $(4 - 1)^2 + (6 - 2)^2 = 9 + 16 = 25$. c) Đúng. d) Sai vì tiếp '
                        'tuyến là $3(x - 4) + 4(y - 6) = 0 \\Leftrightarrow 3x + 4y - 36 = 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 21: Đường tròn trong '
                 'mặt phẳng tọa độ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tìm được tọa độ tâm $I$ và bán '
                           'kính $R$ của đường tròn từ phương trình chính tắc hoặc phương trình dạng khai '
                           'triển.',
                           'Quy tắc/công thức **Phương trình đường tròn tâm $I(a; b)$, bán kính $R$** trong '
                           'bài được xác định bởi: $(x - a)^2 + (y - b)^2 = R^2$.',
                           'Trong mọi trường hợp, **Phương trình đường tròn tâm $I(a; b)$, bán kính $R$** '
                           'luôn được tính bằng công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai '
                           '(thuộc Mệnh đề kéo theo) mà không cần điều kiện của Bài 21: Đường tròn trong mặt '
                           'phẳng tọa độ.',
                           'Với bài toán minh họa: “Tìm tâm và bán kính của đường tròn $(C): x^2 + y^2 - 4x '
                           '+ 6y - 12 = 0$.”, lời giải đúng là: Phương trình có dạng $x^2 + y^2 - 2ax - 2by '
                           '+ c = 0$ với $a = 2, b = -3, c = -12$. Vậy đường tròn $(C)$ có tâm $I(2; -3)$ và '
                           'bán kính $R = \\sqrt{2^2 + (-3)^2 - (-12)} = \\sqrt{4 + 9 + 12} = 5$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 21: Đường tròn trong mặt phẳng tọa độ. b) '
                        '**Đúng** theo công thức trọng tâm **Phương trình đường tròn tâm $I(a; b)$, bán kính '
                        '$R$** ($(x - a)^2 + (y - b)^2 = R^2$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi '
                        '$P$ đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Phương trình đường tròn tâm $I(a; b)$, bán kính $R$**. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 21: Đường tròn trong mặt phẳng tọa độ** để giải quyết tình huống '
                 'sau: Tìm tâm và bán kính của đường tròn $(C): x^2 + y^2 - 4x + 6y - 12 = 0$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Phương trình có dạng $x^2 + y^2 - 2ax - 2by + c = 0$ với $a = 2, b = -3, c = -12$. '
                        'Vậy đường tròn $(C)$ có tâm $I(2; -3)$ và bán kính $R = \\sqrt{2^2 + (-3)^2 - '
                        '(-12)} = \\sqrt{4 + 9 + 12} = 5$...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Đường tròn trong mặt phẳng tọa độ: Phương trình có '
                        'dạng $x^2 + y^2 - 2ax - 2by + c = 0$ với $a = 2, b = -3, c = -12$.\n'
                        'Vậy đường tròn $(C)$ có tâm $I(2; -3)$ và bán kính $R = \\sqrt{2^2 + (-3)^2 - '
                        '(-12)} = \\sqrt{4 + 9 + 12} = 5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; 1)$ và $B(7; 9)$. Đường tròn đường kính '
                 '$AB$ có bán kính $R$ bằng bao nhiêu?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Độ dài đường kính $AB = \\sqrt{(7 - 1)^2 + (9 - 1)^2} = \\sqrt{36 + 64} = 10$. Bán '
                        'kính đường tròn là $R = \\dfrac{AB}{2} = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch07-toa-do-mat-phang',
  'context_title': 'Chương VII: Phương pháp tọa độ trong mặt phẳng',
  'context': 'Chương VII · SGK Toán 10: Phương pháp tọa độ trong mặt phẳng.',
  'title': 'Bài 22: Ba đường conic (Elip, Hypebol, Parabol)',
  'icon': '🪐',
  'description': 'Nhận biết phương trình chính tắc, tiêu điểm, tiêu cự của ba đường conic: Elip, Hypebol và '
                 'Parabol.',
  'requirements': ['Nhận biết được định nghĩa, phương trình chính tắc, các đỉnh, tiêu điểm $F_1, F_2$ và '
                   'tiêu cự $2c$ của Elip và Hypebol.',
                   'Nhận biết được phương trình chính tắc, tiêu điểm $F$ và đường chuẩn $\\Delta$ của '
                   'Parabol.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Elip ($a > b > 0$)** ($\\dfrac{x^2}{a^2} + '
                   '\\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 - b^2$) vào giải bài tập.'],
  'definition': 'Ba đường conic gồm: Elip (tập hợp các điểm $M$ có $MF_1 + MF_2 = 2a$), Hypebol (tập hợp các '
                'điểm $M$ có $|MF_1 - MF_2| = 2a$) và Parabol (tập hợp các điểm $M$ cách đều tiêu điểm $F$ '
                'và đường chuẩn $\\Delta$).',
  'theory': '1. Elip $(E): \\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$ ($a > b > 0$): tiêu điểm $F_1(-c; 0), '
            'F_2(c; 0)$, tiêu cự $2c$ với $c^2 = a^2 - b^2$.\n'
            '2. Hypebol $(H): \\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$ ($a > 0, b > 0$): tiêu điểm '
            '$F_1(-c; 0), F_2(c; 0)$, tiêu cự $2c$ với $c^2 = a^2 + b^2$.\n'
            '3. Parabol $(P): y^2 = 2px$ ($p > 0$): đỉnh $O(0; 0)$, tiêu điểm $F\\left(\\dfrac{p}{2}; '
            '0\\right)$, đường chuẩn $\\Delta: x = -\\dfrac{p}{2}$.',
  'formulas': [{'category': 'Phương trình chính tắc của ba đường conic',
                'items': [{'name': 'Elip ($a > b > 0$)',
                           'formula': '$\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 - b^2$',
                           'note': 'Tiêu điểm $F_1(-c; 0), F_2(c; 0)$; độ dài trục lớn $2a$, trục nhỏ $2b$'},
                          {'name': 'Hypebol ($a, b > 0$)',
                           'formula': '$\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 + b^2$',
                           'note': 'Tiêu điểm $F_1(-c; 0), F_2(c; 0)$; độ dài trục thực $2a$, trục ảo $2b$'},
                          {'name': 'Parabol ($p > 0$)',
                           'formula': '$y^2 = 2px$',
                           'note': 'Tiêu điểm $F\\left(\\dfrac{p}{2}; 0\\right)$, đường chuẩn $x = '
                                   '-\\dfrac{p}{2}$'}]}],
  'example': 'Cho elip $(E): \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1$. Tìm độ dài trục lớn, trục nhỏ, tọa độ '
             'các tiêu điểm và tiêu cự của $(E)$.',
  'example_answer': 'Ta có $a^2 = 25 \\Rightarrow a = 5$; $b^2 = 9 \\Rightarrow b = 3$; $c = \\sqrt{a^2 - '
                    'b^2} = \\sqrt{25 - 9} = 4$.\n'
                    '- Độ dài trục lớn $2a = 10$, độ dài trục nhỏ $2b = 6$.\n'
                    '- Hai tiêu điểm là $F_1(-4; 0), F_2(4; 0)$ và tiêu cự là $2c = 8$.',
  'real_life': 'Quỹ đạo elip của các hành tinh quay quanh Mặt Trời, hệ thống định vị hàng hải LORAN '
               '(hypebol) và gương phản xạ đèn pha ô tô (parabol).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho elip $(E): \\dfrac{x^2}{16} + \\dfrac{y^2}{9} = 1$. Độ dài trục lớn của elip $(E)$ '
                 'bằng:',
            'options': ['$4$', '$8$', '$6$', '$16$'],
            'answer': 1,
            'solution': 'Ta có $a^2 = 16 \\Rightarrow a = 4$, nên độ dài trục lớn là $2a = 8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho parabol $(P): y^2 = 8x$. Tọa độ tiêu điểm $F$ của parabol $(P)$ là:',
            'options': ['$F(4; 0)$', '$F(-2; 0)$', '$F(2; 0)$', '$F(0; 2)$'],
            'answer': 2,
            'solution': 'So sánh với $y^2 = 2px$ ta có $2p = 8 \\Rightarrow p = 4$, nên tiêu điểm là '
                        '$F\\left(\\dfrac{p}{2}; 0\\right) = F(2; 0)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 22: Ba đường conic (Elip, Hypebol, Parabol)**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Elip ($a > b > 0$)**?',
            'options': ['$\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 + b^2$',
                        '$y^2 = 2px$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 - b^2$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 22: Ba đường conic (Elip, Hypebol, Parabol), '
                        '**Elip ($a > b > 0$)** được xác định bởi: $\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = '
                        '1$ với $c^2 = a^2 - b^2$. (Tiêu điểm $F_1(-c; 0), F_2(c; 0)$; độ dài trục lớn $2a$, '
                        'trục nhỏ $2b$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Ba đường conic (Elip, Hypebol, Parabol)**, nội dung/biểu thức '
                 '$\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 + b^2$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Hypebol ($a, b > 0$)',
                        'Elip ($a > b > 0$)',
                        'Parabol ($p > 0$)',
                        'Mệnh đề kéo theo'],
            'answer': 0,
            'solution': 'Trong Bài 22: Ba đường conic (Elip, Hypebol, Parabol), biểu thức/quy tắc '
                        '$\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 + b^2$ chính là nội dung '
                        'của **Hypebol ($a, b > 0$)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hypebol $(H): \\dfrac{x^2}{9} - \\dfrac{y^2}{16} = 1$. Tiêu cự $2c$ của hypebol $(H)$ '
                 'bằng:',
            'options': ['$5$', '$10$', '$2\\sqrt{7}$', '$14$'],
            'answer': 1,
            'solution': 'Trong hypebol, $c = \\sqrt{a^2 + b^2} = \\sqrt{9 + 16} = 5$, suy ra tiêu cự $2c = '
                        '10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Ba đường conic (Elip, Hypebol, Parabol)** (Chương VII: Phương pháp tọa '
                 'độ trong mặt phẳng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Nhận biết được định nghĩa, phương trình chính tắc, các đỉnh, tiêu điểm $F_1, F_2$ '
                        'và tiêu cự $2c$ của Elip và Hypebol.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 22: Ba đường conic (Elip, Hypebol, Parabol): Nhận biết '
                        'được định nghĩa, phương trình chính tắc, các đỉnh, tiêu điểm $F_1, F_2$ và tiêu cự '
                        '$2c$ của Elip và Hypebol.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho elip $(E): \\dfrac{x^2}{100} + \\dfrac{y^2}{64} = 1$.',
            'statements': ['Elip $(E)$ có $a = 10$ và $b = 8$.',
                           'Tiêu cự của elip $(E)$ là $2c = 12$.',
                           'Hai tiêu điểm của elip là $F_1(-6; 0)$ và $F_2(6; 0)$.',
                           'Với mọi điểm $M$ thuộc elip $(E)$, tổng khoảng cách $MF_1 + MF_2$ bằng $10$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $c = \\sqrt{100 - 64} = 6 \\Rightarrow 2c = 12$. c) Đúng. d) '
                        'Sai vì theo định nghĩa elip, $MF_1 + MF_2 = 2a = 20$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 22: Ba đường conic '
                 '(Elip, Hypebol, Parabol)**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được định nghĩa, phương '
                           'trình chính tắc, các đỉnh, tiêu điểm $F_1, F_2$ và tiêu cự $2c$ của Elip và '
                           'Hypebol.',
                           'Quy tắc/công thức **Elip ($a > b > 0$)** trong bài được xác định bởi: '
                           '$\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 - b^2$.',
                           'Trong mọi trường hợp, **Elip ($a > b > 0$)** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 22: Ba đường conic (Elip, Hypebol, Parabol).',
                           'Với bài toán minh họa: “Cho elip $(E): \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1$. '
                           'Tìm độ dài trục lớn, trục nhỏ, tọa độ các tiêu điểm và tiêu cự của $(E)$.”, lời '
                           'giải đúng là: Ta có $a^2 = 25 \\Rightarrow a = 5$; $b^2 = 9 \\Rightarrow b = 3$; '
                           '$c = \\sqrt{a^2 - b^2} = \\sqrt{25 - 9} = 4$. - Độ dài trục lớn $2a = 10$, '
                           'độ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 22: Ba đường conic (Elip, Hypebol, '
                        'Parabol). b) **Đúng** theo công thức trọng tâm **Elip ($a > b > 0$)** '
                        '($\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1$ với $c^2 = a^2 - b^2$). c) **Sai** vì '
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Elip ($a > b > 0$)**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 22: Ba đường conic (Elip, Hypebol, Parabol)** để giải quyết tình '
                 'huống sau: Cho elip $(E): \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1$. Tìm độ dài trục lớn, '
                 'trục nhỏ, tọa độ các tiêu điểm và tiêu cự của $(E)$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        'Ta có $a^2 = 25 \\Rightarrow a = 5$; $b^2 = 9 \\Rightarrow b = 3$; $c = \\sqrt{a^2 '
                        '- b^2} = \\sqrt{25 - 9} = 4$. - Độ dài trục lớn $2a = 10$, độ dài trục nhỏ $2b = '
                        '6$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Ba đường conic (Elip, Hypebol, Parabol): Ta có $a^2 '
                        '= 25 \\Rightarrow a = 5$; $b^2 = 9 \\Rightarrow b = 3$; $c = \\sqrt{a^2 - b^2} = '
                        '\\sqrt{25 - 9} = 4$.\n'
                        '- Độ dài trục lớn $2a = 10$, độ dài trục nhỏ $2b = 6$.\n'
                        '- Hai tiêu điểm là $F_1(-4; 0), F_2(4; 0)$ và tiêu cự là $2c = 8$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho parabol $(P): y^2 = 12x$ có tiêu điểm $F$. Điểm $M(x_0; y_0)$ thuộc $(P)$ có hoành độ '
                 '$x_0 = 5$. Tính độ dài đoạn thẳng $MF$ (bán kính qua tiêu của điểm $M$).',
            'answer': ['8'],
            'unit': None,
            'solution': 'Ta có $2p = 12 \\Rightarrow p = 6$. Khoảng cách từ $M(x_0; y_0) \\in (P)$ đến tiêu '
                        'điểm $F$ bằng khoảng cách từ $M$ đến đường chuẩn $x = -\\dfrac{p}{2} = -3$: $MF = '
                        'x_0 + \\dfrac{p}{2} = 5 + 3 = 8$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch08-dai-so-to-hop',
  'context_title': 'Chương VIII: Đại số tổ hợp',
  'context': 'Chương VIII · SGK Toán 10: Đại số tổ hợp.',
  'title': 'Bài 23: Quy tắc đếm',
  'icon': '🔢',
  'description': 'Vận dụng quy tắc cộng, quy tắc nhân và sơ đồ hình cây để đếm số phương án thực hiện một '
                 'công việc.',
  'requirements': ['Phân biệt và vận dụng được quy tắc cộng (công việc chia theo các phương án độc lập) và '
                   'quy tắc nhân (công việc gồm các công đoạn liên tiếp).',
                   'Sử dụng được sơ đồ hình cây trong các bài toán đếm đơn giản.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Quy tắc cộng** ($N = m + n$) vào giải bài '
                   'tập.'],
  'definition': 'Quy tắc cộng dùng khi một công việc được hoàn thành bởi một trong các phương án khác nhau; '
                'Quy tắc nhân dùng khi một công việc được hoàn thành qua nhiều công đoạn liên tiếp.',
  'theory': '1. Quy tắc cộng: Giả sử một công việc có thể được thực hiện theo phương án $A$ (có $m$ cách) '
            'hoặc phương án $B$ (có $n$ cách không trùng với $A$). Khi đó có $m + n$ cách thực hiện công '
            'việc.\n'
            '2. Quy tắc nhân: Giả sử một công việc bao gồm hai công đoạn liên tiếp: công đoạn 1 có $m$ cách '
            'thực hiện và ứng với mỗi cách đó công đoạn 2 có $n$ cách thực hiện. Khi đó có $m \\cdot n$ cách '
            'hoàn thành công việc.',
  'formulas': [{'category': 'Hai quy tắc đếm cơ bản',
                'items': [{'name': 'Quy tắc cộng',
                           'formula': '$N = m + n$',
                           'note': 'Chia trường hợp / phương án độc lập (từ khóa: HOẶC)'},
                          {'name': 'Quy tắc nhân',
                           'formula': '$N = m \\cdot n$',
                           'note': 'Thực hiện liên tiếp đủ các bước / công đoạn (từ khóa: VÀ)'}]}],
  'example': 'Một tủ sách có 6 quyển sách Toán và 4 quyển sách Vật lí khác nhau. Hỏi có bao nhiêu cách: a) '
             'Chọn 1 quyển sách bất kì? b) Chọn 1 quyển Toán và 1 quyển Vật lí?',
  'example_answer': 'a) Theo quy tắc cộng, số cách chọn 1 quyển sách bất kì là $6 + 4 = 10$ (cách).\n'
                    'b) Theo quy tắc nhân, số cách chọn 1 quyển Toán và 1 quyển Vật lí là $6 \\cdot 4 = 24$ '
                    '(cách).',
  'real_life': 'Đếm số lượng biển số xe, số lượng mã PIN ngân hàng hoặc số thực đơn bữa ăn có thể phối hợp '
               'tại nhà hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một tổ có $7$ học sinh nam và $5$ học sinh nữ. Số cách chọn $1$ học sinh trong tổ làm tổ '
                 'trưởng là:',
            'options': ['$35$', '$7$', '$12$', '$2$'],
            'answer': 2,
            'solution': 'Theo quy tắc cộng, số cách chọn 1 học sinh (nam hoặc nữ) là $7 + 5 = 12$ (cách).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bạn An có $4$ chiếc áo sơ mi và $3$ chiếc quần âu khác nhau. Số cách chọn một bộ trang '
                 'phục gồm $1$ áo và $1$ quần là:',
            'options': ['$7$', '$16$', '$9$', '$12$'],
            'answer': 3,
            'solution': 'Theo quy tắc nhân, số cách chọn một bộ trang phục là $4 \\cdot 3 = 12$ (cách).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 23: Quy tắc đếm**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Quy tắc cộng**?',
            'options': ['$N = m + n$',
                        '$N = m \\cdot n$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 23: Quy tắc đếm, **Quy tắc cộng** được xác '
                        'định bởi: $N = m + n$. (Chia trường hợp / phương án độc lập (từ khóa: HOẶC))'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Quy tắc đếm**, nội dung/biểu thức $N = m \\cdot n$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Quy tắc cộng', 'Quy tắc nhân', 'Mệnh đề kéo theo', 'Mệnh đề tương đương'],
            'answer': 1,
            'solution': 'Trong Bài 23: Quy tắc đếm, biểu thức/quy tắc $N = m \\cdot n$ chính là nội dung của '
                        '**Quy tắc nhân**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Từ các chữ số $1, 2, 3, 4, 5$ có thể lập được bao nhiêu số tự nhiên có $3$ chữ số đôi một '
                 'khác nhau?',
            'options': ['$125$', '$15$', '$60$', '$27$'],
            'answer': 2,
            'solution': 'Chữ số hàng trăm có $5$ cách chọn, hàng chục có $4$ cách, hàng đơn vị có $3$ cách. '
                        'Theo quy tắc nhân có $5 \\cdot 4 \\cdot 3 = 60$ số.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Quy tắc đếm** (Chương VIII: Đại số tổ hợp), khẳng định nào sau đây phản '
                 'ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Phân biệt và vận dụng được quy tắc cộng (công việc chia theo các phương án độc lập) '
                        'và quy tắc nhân (công việc gồm các công đoạn liên tiếp).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 23: Quy tắc đếm: Phân biệt và vận dụng được quy tắc '
                        'cộng (công việc chia theo các phương án độc lập) và quy tắc nhân (công việc gồm các '
                        'công đoạn liên tiếp).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Từ thành phố $A$ đến thành phố $B$ có $3$ con đường, từ thành phố $B$ đến thành phố $C$ có '
                 '$4$ con đường.',
            'statements': ['Số cách đi từ $A$ đến $C$ có đi qua $B$ là $7$ cách.',
                           'Số cách đi từ $A$ đến $C$ (qua $B$) rồi quay về $A$ (cũng qua $B$) là $144$ '
                           'cách.',
                           'Nếu mở thêm $2$ đường bay thẳng từ $A$ đến $C$ (không qua $B$) thì tổng số cách '
                           'đi từ $A$ đến $C$ là $14$ cách.',
                           'Số cách đi từ $A$ đến $B$ rồi quay về $A$ bằng một con đường khác lúc đi là $6$ '
                           'cách.'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì theo quy tắc nhân có $3 \\cdot 4 = 12$ cách. b) Đúng vì $12 \\cdot 12 = '
                        '144$ cách. c) Đúng vì $12 + 2 = 14$ cách. d) Đúng vì lúc đi có $3$ cách, lúc về có '
                        '$2$ cách ($3 \\cdot 2 = 6$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 23: Quy tắc đếm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phân biệt và vận dụng được quy tắc '
                           'cộng (công việc chia theo các phương án độc lập) và quy tắc nhân (công việc gồm '
                           'các công đoạn liên tiếp).',
                           'Quy tắc/công thức **Quy tắc cộng** trong bài được xác định bởi: $N = m + n$.',
                           'Trong mọi trường hợp, **Quy tắc cộng** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 23: Quy tắc đếm.',
                           'Với bài toán minh họa: “Một tủ sách có 6 quyển sách Toán và 4 quyển sách Vật lí '
                           'khác nhau. Hỏi có bao nhiêu cách: a) Chọn 1 quyển sách bất kì? b) Chọn 1 quyển '
                           'Toán...”, lời giải đúng là: a) Theo quy tắc cộng, số cách chọn 1 quyển sách bất '
                           'kì là $6 + 4 = 10$ (cách). b) Theo quy tắc nhân, số cách chọn 1 quyển Toán và 1 '
                           'quyển Vậ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 23: Quy tắc đếm. b) **Đúng** theo công '
                        'thức trọng tâm **Quy tắc cộng** ($N = m + n$). c) **Sai** vì $P \\Rightarrow Q$ chỉ '
                        'sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung '
                        'của **Quy tắc cộng**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 23: Quy tắc đếm** để giải quyết tình huống sau: Một tủ sách có 6 '
                 'quyển sách Toán và 4 quyển sách Vật lí khác nhau. Hỏi có bao nhiêu cách: a) Chọn 1 quyển '
                 'sách bất kì? b) Chọn 1 quyển Toán và 1 quyển Vật lí? Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['a) Theo quy tắc cộng, số cách chọn 1 quyển sách bất kì là $6 + 4 = 10$ (cách). b) '
                        'Theo quy tắc nhân, số cách chọn 1 quyển Toán và 1 quyển Vật lí là $6 \\cdot 4 = '
                        '24$...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Quy tắc đếm: a) Theo quy tắc cộng, số cách chọn 1 '
                        'quyển sách bất kì là $6 + 4 = 10$ (cách).\n'
                        'b) Theo quy tắc nhân, số cách chọn 1 quyển Toán và 1 quyển Vật lí là $6 \\cdot 4 = '
                        '24$ (cách).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Từ các chữ số $0, 1, 2, 3, 4, 5$, có thể lập được bao nhiêu số tự nhiên chẵn có $2$ chữ '
                 'số?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Gọi số tự nhiên chẵn có 2 chữ số là $\\overline{ab}$: chữ số hàng chục $a \\in '
                        '\\{1; 2; 3; 4; 5\\}$ có $5$ cách chọn; chữ số hàng đơn vị $b \\in \\{0; 2; 4\\}$ có '
                        '$3$ cách chọn. Theo quy tắc nhân, có $5 \\cdot 3 = 15$ số.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch08-dai-so-to-hop',
  'context_title': 'Chương VIII: Đại số tổ hợp',
  'context': 'Chương VIII · SGK Toán 10: Đại số tổ hợp.',
  'title': 'Bài 24: Hoán vị, chỉnh hợp và tổ hợp',
  'icon': '🔀',
  'description': 'Phân biệt và vận dụng công thức tính số hoán vị, số chỉnh hợp và số tổ hợp để giải bài '
                 'toán đếm.',
  'requirements': ['Tính được số các hoán vị $P_n$, số các chỉnh hợp $A_n^k$ và số các tổ hợp $C_n^k$.',
                   'Phân biệt được khi nào dùng chỉnh hợp (có thứ tự) và khi nào dùng tổ hợp (không phân '
                   'biệt thứ tự).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hoán vị** ($P_n = n!$) vào giải bài tập.'],
  'definition': 'Cho tập hợp $A$ gồm $n$ phần tử ($n \\ge 1$): Hoán vị là cách sắp xếp thứ tự cả $n$ phần '
                'tử; Chỉnh hợp chập $k$ của $n$ là việc lấy $k$ phần tử từ $n$ phần tử và sắp xếp theo thứ '
                'tự; Tổ hợp chập $k$ của $n$ là một tập con gồm $k$ phần tử của $A$ (không phân biệt thứ '
                'tự).',
  'theory': '1. Số hoán vị của $n$ phần tử: $P_n = n! = n(n - 1)\\dots 2 \\cdot 1$ (quy ước $0! = 1$).\n'
            '2. Số chỉnh hợp chập $k$ của $n$ phần tử ($1 \\le k \\le n$): $A_n^k = \\dfrac{n!}{(n - k)!} = '
            'n(n - 1)\\dots(n - k + 1)$.\n'
            '3. Số tổ hợp chập $k$ của $n$ phần tử ($0 \\le k \\le n$): $C_n^k = \\dfrac{n!}{k!(n - k)!} = '
            '\\dfrac{A_n^k}{k!}$.',
  'formulas': [{'category': 'Công thức Hoán vị, Chỉnh hợp và Tổ hợp',
                'items': [{'name': 'Hoán vị',
                           'formula': '$P_n = n!$',
                           'note': 'Sắp xếp cả $n$ phần tử (có thứ tự)'},
                          {'name': 'Chỉnh hợp',
                           'formula': '$A_n^k = \\dfrac{n!}{(n - k)!}$ ($1 \\le k \\le n$)',
                           'note': 'Chọn $k$ phần tử trong $n$ phần tử và sắp thứ tự'},
                          {'name': 'Tổ hợp',
                           'formula': '$C_n^k = \\dfrac{n!}{k!(n - k)!}$ ($0 \\le k \\le n$)',
                           'note': 'Chọn $k$ phần tử trong $n$ phần tử không kể thứ tự'}]}],
  'example': 'Một tổ có 10 học sinh. Hỏi có bao nhiêu cách: a) Chọn ra 3 học sinh đi trực nhật? b) Chọn ra 3 '
             'học sinh làm Tổ trưởng, Tổ phó và Thư kí?',
  'example_answer': 'a) Chọn 3 học sinh đi trực nhật không phân biệt thứ tự nên số cách chọn là $C_{10}^3 = '
                    '\\dfrac{10!}{3!7!} = 120$ (cách).\n'
                    'b) Chọn 3 học sinh giữ 3 chức vụ khác nhau có phân biệt thứ tự nên số cách chọn là '
                    '$A_{10}^3 = 10 \\cdot 9 \\cdot 8 = 720$ (cách).',
  'real_life': 'Xếp lịch thi đấu thể thao, xếp chỗ ngồi trong rạp chiếu phim hoặc chọn ban đại diện từ một '
               'tập thể.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số cách sắp xếp $5$ học sinh thành một hàng dọc là:',
            'options': ['$25$', '$5$', '$60$', '$120$'],
            'answer': 3,
            'solution': 'Số cách xếp 5 học sinh vào 5 vị trí là $P_5 = 5! = 120$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của số tổ hợp $C_6^2$ bằng:',
            'options': ['$15$', '$30$', '$12$', '$36$'],
            'answer': 0,
            'solution': 'Ta có $C_6^2 = \\dfrac{6!}{2!4!} = \\dfrac{6 \\cdot 5}{2} = 15$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 24: Hoán vị, chỉnh hợp và tổ hợp**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Hoán vị**?',
            'options': ['$A_n^k = \\dfrac{n!}{(n - k)!}$ ($1 \\le k \\le n$)',
                        '$P_n = n!$',
                        '$C_n^k = \\dfrac{n!}{k!(n - k)!}$ ($0 \\le k \\le n$)',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 24: Hoán vị, chỉnh hợp và tổ hợp, **Hoán vị** '
                        'được xác định bởi: $P_n = n!$. (Sắp xếp cả $n$ phần tử (có thứ tự))'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: Hoán vị, chỉnh hợp và tổ hợp**, nội dung/biểu thức $A_n^k = \\dfrac{n!}{(n '
                 '- k)!}$ ($1 \\le k \\le n$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hoán vị', 'Tổ hợp', 'Chỉnh hợp', 'Mệnh đề kéo theo'],
            'answer': 2,
            'solution': 'Trong Bài 24: Hoán vị, chỉnh hợp và tổ hợp, biểu thức/quy tắc $A_n^k = '
                        '\\dfrac{n!}{(n - k)!}$ ($1 \\le k \\le n$) chính là nội dung của **Chỉnh hợp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $10$ điểm phân biệt trong mặt phẳng, không có $3$ điểm nào thẳng hàng. Số tam giác có '
                 'các đỉnh được chọn từ $10$ điểm đã cho là:',
            'options': ['$720$', '$30$', '$45$', '$120$'],
            'answer': 3,
            'solution': 'Mỗi bộ 3 điểm không thẳng hàng tạo thành 1 tam giác (không phân biệt thứ tự đỉnh), '
                        'nên có $C_{10}^3 = 120$ tam giác.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: Hoán vị, chỉnh hợp và tổ hợp** (Chương VIII: Đại số tổ hợp), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Tính được số các hoán vị $P_n$, số các chỉnh hợp $A_n^k$ và số các tổ hợp $C_n^k$.',
                        'Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 24: Hoán vị, chỉnh hợp và tổ hợp: Tính được số các '
                        'hoán vị $P_n$, số các chỉnh hợp $A_n^k$ và số các tổ hợp $C_n^k$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một hộp có $6$ viên bi đỏ và $4$ viên bi xanh đôi một khác nhau.',
            'statements': ['Số cách chọn ngẫu nhiên $3$ viên bi bất kì từ hộp là $C_{10}^3 = 120$ cách.',
                           'Số cách chọn $3$ viên bi sao cho cả $3$ viên đều màu đỏ là $C_6^3 = 20$ cách.',
                           'Số cách chọn $2$ viên bi đỏ và $1$ viên bi xanh là $C_6^2 + C_4^1 = 19$ cách.',
                           'Số cách xếp cả $10$ viên bi thành một hàng ngang là $10!$ cách.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì chọn 2 đỏ VÀ 1 xanh phải dùng quy tắc nhân: $C_6^2 '
                        '\\cdot C_4^1 = 15 \\cdot 4 = 60$ cách. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 24: Hoán vị, chỉnh hợp '
                 'và tổ hợp**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được số các hoán vị $P_n$, số '
                           'các chỉnh hợp $A_n^k$ và số các tổ hợp $C_n^k$.',
                           'Quy tắc/công thức **Hoán vị** trong bài được xác định bởi: $P_n = n!$.',
                           'Trong mọi trường hợp, **Hoán vị** luôn được tính bằng công thức $P \\Rightarrow '
                           'Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không cần điều kiện '
                           'của Bài 24: Hoán vị, chỉnh hợp và tổ hợp.',
                           'Với bài toán minh họa: “Một tổ có 10 học sinh. Hỏi có bao nhiêu cách: a) Chọn ra '
                           '3 học sinh đi trực nhật? b) Chọn ra 3 học sinh làm Tổ trưởng, Tổ phó và Thư '
                           'kí?”, lời giải đúng là: a) Chọn 3 học sinh đi trực nhật không phân biệt thứ tự '
                           'nên số cách chọn là $C_{10}^3 = \\dfrac{10!}{3!7!} = 120$ (cách). b) Chọn 3 học '
                           'sinh g...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 24: Hoán vị, chỉnh hợp và tổ hợp. b) '
                        '**Đúng** theo công thức trọng tâm **Hoán vị** ($P_n = n!$). c) **Sai** vì $P '
                        '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Hoán vị**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 24: Hoán vị, chỉnh hợp và tổ hợp** để giải quyết tình huống sau: '
                 'Một tổ có 10 học sinh. Hỏi có bao nhiêu cách: a) Chọn ra 3 học sinh đi trực nhật? b) Chọn '
                 'ra 3 học sinh làm Tổ trưởng, Tổ phó và Thư kí? Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'a) Chọn 3 học sinh đi trực nhật không phân biệt thứ tự nên số cách chọn là '
                        '$C_{10}^3 = \\dfrac{10!}{3!7!} = 120$ (cách). b) Chọn 3 học sinh giữ 3 chức vụ '
                        'kh...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: Hoán vị, chỉnh hợp và tổ hợp: a) Chọn 3 học sinh đi '
                        'trực nhật không phân biệt thứ tự nên số cách chọn là $C_{10}^3 = \\dfrac{10!}{3!7!} '
                        '= 120$ (cách).\n'
                        'b) Chọn 3 học sinh giữ 3 chức vụ khác nhau có phân biệt thứ tự nên số cách chọn là '
                        '$A_{10}^3 = 10 \\cdot 9 \\cdot 8 = 720$ (cách).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đa giác lồi có $10$ đỉnh thì có tất cả bao nhiêu đường chéo?',
            'answer': ['35'],
            'unit': None,
            'solution': 'Số đoạn thẳng nối 2 đỉnh bất kì trong 10 đỉnh là $C_{10}^2 = 45$ (gồm các cạnh và '
                        'các đường chéo). Trừ đi $10$ cạnh của đa giác, số đường chéo là $45 - 10 = 35$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch08-dai-so-to-hop',
  'context_title': 'Chương VIII: Đại số tổ hợp',
  'context': 'Chương VIII · SGK Toán 10: Đại số tổ hợp.',
  'title': 'Bài 25: Nhị thức Newton',
  'icon': '🧮',
  'description': 'Khai triển nhị thức Newton với số mũ bằng 4 hoặc 5 và tìm hệ số của một số hạng trong khai '
                 'triển.',
  'requirements': ['Viết được khai triển nhị thức Newton của $(a + b)^4$ và $(a + b)^5$.',
                   'Xác định được hệ số của $x^k$ trong khai triển của $(ax + b)^4$ hoặc $(ax + b)^5$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Bậc 4 ($n = 4$)** ($(a + b)^4 = a^4 + 4a^3b '
                   '+ 6a^2b^2 + 4ab^3 + b^4$) vào giải bài tập.'],
  'definition': 'Công thức nhị thức Newton với $n = 4$ và $n = 5$ biểu diễn lũy thừa $(a + b)^n$ thành tổng '
                'các đơn thức đồng bậc với các hệ số tổ hợp $C_n^k$.',
  'theory': '1. Khai triển với $n = 4$:\n'
            '$(a + b)^4 = C_4^0 a^4 + C_4^1 a^3b + C_4^2 a^2b^2 + C_4^3 ab^3 + C_4^4 b^4 = a^4 + 4a^3b + '
            '6a^2b^2 + 4ab^3 + b^4$.\n'
            '2. Khai triển với $n = 5$:\n'
            '$(a + b)^5 = C_5^0 a^5 + C_5^1 a^4b + C_5^2 a^3b^2 + C_5^3 a^2b^3 + C_5^4 ab^4 + C_5^5 b^5 = '
            'a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$.\n'
            '3. Số hạng tổng quát thứ $k + 1$ trong khai triển $(a + b)^n$ là $T_{k+1} = C_n^k a^{n-k} b^k$.',
  'formulas': [{'category': 'Công thức nhị thức Newton bậc 4 và bậc 5',
                'items': [{'name': 'Bậc 4 ($n = 4$)',
                           'formula': '$(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$',
                           'note': 'Các hệ số dòng 4 tam giác Pascal: $1, 4, 6, 4, 1$'},
                          {'name': 'Bậc 5 ($n = 5$)',
                           'formula': '$(a + b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$',
                           'note': 'Các hệ số dòng 5 tam giác Pascal: $1, 5, 10, 10, 5, 1$'},
                          {'name': 'Tổng các hệ số tổ hợp',
                           'formula': '$C_n^0 + C_n^1 + \\dots + C_n^n = 2^n$',
                           'note': 'Thay $a = b = 1$ vào khai triển $(a + b)^n$'}]}],
  'example': 'Tìm hệ số của $x^3$ trong khai triển của biểu thức $(x + 2)^4$.',
  'example_answer': 'Áp dụng công thức $(a + b)^4$ với $a = x, b = 2$: số hạng chứa $x^3$ là $C_4^1 x^3 '
                    '\\cdot 2^1 = 4 \\cdot 2 \\cdot x^3 = 8x^3$.\n'
                    'Vậy hệ số của $x^3$ trong khai triển là $8$.',
  'real_life': 'Tính xấp xỉ lãi kép $(1 + r)^n$ trong tài chính ngân hàng và tính xác suất phân phối nhị '
               'thức trong di truyền học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong khai triển nhị thức Newton của $(a + b)^4$, có tất cả bao nhiêu số hạng?',
            'options': ['$5$', '$4$', '$6$', '$8$'],
            'answer': 0,
            'solution': 'Khai triển của $(a + b)^n$ có $n + 1$ số hạng, nên với $n = 4$ có $4 + 1 = 5$ số '
                        'hạng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khai triển của $(x + 1)^4$ là:',
            'options': ['$x^4 + 4x^3 + 4x^2 + 4x + 1$',
                        '$x^4 + 4x^3 + 6x^2 + 4x + 1$',
                        '$x^4 + 5x^3 + 10x^2 + 5x + 1$',
                        '$x^4 - 4x^3 + 6x^2 - 4x + 1$'],
            'answer': 1,
            'solution': 'Thay $a = x, b = 1$ vào công thức $(a + b)^4$ ta được $x^4 + 4x^3 + 6x^2 + 4x + 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 25: Nhị thức Newton**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Bậc 4 ($n = 4$)**?',
            'options': ['$(a + b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$',
                        '$C_n^0 + C_n^1 + \\dots + C_n^n = 2^n$',
                        '$(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 25: Nhị thức Newton, **Bậc 4 ($n = 4$)** được '
                        'xác định bởi: $(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$. (Các hệ số dòng 4 '
                        'tam giác Pascal: $1, 4, 6, 4, 1$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Nhị thức Newton**, nội dung/biểu thức $(a + b)^5 = a^5 + 5a^4b + 10a^3b^2 '
                 '+ 10a^2b^3 + 5ab^4 + b^5$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Bậc 4 ($n = 4$)', 'Tổng các hệ số tổ hợp', 'Mệnh đề kéo theo', 'Bậc 5 ($n = 5$)'],
            'answer': 3,
            'solution': 'Trong Bài 25: Nhị thức Newton, biểu thức/quy tắc $(a + b)^5 = a^5 + 5a^4b + '
                        '10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$ chính là nội dung của **Bậc 5 ($n = 5$)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hệ số của $x^3$ trong khai triển của $(x - 2)^5$ là:',
            'options': ['$40$', '$-40$', '$10$', '$80$'],
            'answer': 0,
            'solution': 'Số hạng chứa $x^3$ trong $(x + (-2))^5$ ứng với $k = 2$: $C_5^2 x^3 (-2)^2 = 10 '
                        '\\cdot 4 x^3 = 40x^3$. Hệ số là $40$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Nhị thức Newton** (Chương VIII: Đại số tổ hợp), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Viết được khai triển nhị thức Newton của $(a + b)^4$ và $(a + b)^5$.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 25: Nhị thức Newton: Viết được khai triển nhị thức '
                        'Newton của $(a + b)^4$ và $(a + b)^5$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho khai triển nhị thức Newton của biểu thức $P(x) = (2x - 1)^4$.',
            'statements': ['Khai triển của $P(x)$ có $5$ số hạng.',
                           'Hệ số của $x^4$ trong khai triển là $16$.',
                           'Số hạng không chứa $x$ (hệ số tự do) trong khai triển là $-1$.',
                           'Tổng tất cả các hệ số của các số hạng trong khai triển của $P(x)$ bằng $1$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $C_4^0 (2x)^4 = 16x^4$. c) Sai vì số hạng tự do là $C_4^4 '
                        '(-1)^4 = 1$. d) Đúng vì tổng các hệ số bằng $P(1) = (2 \\cdot 1 - 1)^4 = 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 25: Nhị thức Newton**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Viết được khai triển nhị thức '
                           'Newton của $(a + b)^4$ và $(a + b)^5$.',
                           'Quy tắc/công thức **Bậc 4 ($n = 4$)** trong bài được xác định bởi: $(a + b)^4 = '
                           'a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$.',
                           'Trong mọi trường hợp, **Bậc 4 ($n = 4$)** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 25: Nhị thức Newton.',
                           'Với bài toán minh họa: “Tìm hệ số của $x^3$ trong khai triển của biểu thức $(x + '
                           '2)^4$.”, lời giải đúng là: Áp dụng công thức $(a + b)^4$ với $a = x, b = 2$: số '
                           'hạng chứa $x^3$ là $C_4^1 x^3 \\cdot 2^1 = 4 \\cdot 2 \\cdot x^3 = 8x^3$. Vậy hệ '
                           'số của $x^3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 25: Nhị thức Newton. b) **Đúng** theo công '
                        'thức trọng tâm **Bậc 4 ($n = 4$)** ($(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + '
                        'b^4$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai là công thức '
                        'của nội dung khác, không phải quy tắc chung của **Bậc 4 ($n = 4$)**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 25: Nhị thức Newton** để giải quyết tình huống sau: Tìm hệ số của '
                 '$x^3$ trong khai triển của biểu thức $(x + 2)^4$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Áp dụng công thức $(a + b)^4$ với $a = x, b = 2$: số hạng chứa $x^3$ là $C_4^1 x^3 '
                        '\\cdot 2^1 = 4 \\cdot 2 \\cdot x^3 = 8x^3$. Vậy hệ số của $x^3$ trong khai...',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25: Nhị thức Newton: Áp dụng công thức $(a + b)^4$ với '
                        '$a = x, b = 2$: số hạng chứa $x^3$ là $C_4^1 x^3 \\cdot 2^1 = 4 \\cdot 2 \\cdot x^3 '
                        '= 8x^3$.\n'
                        'Vậy hệ số của $x^3$ trong khai triển là $8$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính tổng $S = C_5^0 + C_5^1 + C_5^2 + C_5^3 + C_5^4 + C_5^5$.',
            'answer': ['32'],
            'unit': None,
            'solution': 'Thay $a = 1, b = 1$ vào khai triển $(a + b)^5$ ta được $S = (1 + 1)^5 = 2^5 = 32$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch09-xac-suat',
  'context_title': 'Chương IX: Tính xác suất theo định nghĩa cổ điển',
  'context': 'Chương IX · SGK Toán 10: Tính xác suất theo định nghĩa cổ điển.',
  'title': 'Bài 26: Biến cố và định nghĩa cổ điển của xác suất',
  'icon': '🎲',
  'description': 'Nhận biết biến cố, biến cố đối và tính xác suất của biến cố theo định nghĩa cổ điển.',
  'requirements': ['Mô tả được không gian mẫu $\\Omega$, biến cố $A$, biến cố chắc chắn, biến cố không thể '
                   'và biến cố đối $\\overline{A}$.',
                   'Tính được xác suất của biến cố theo định nghĩa cổ điển $P(A) = '
                   '\\dfrac{n(A)}{n(\\Omega)}$ và tính chất $P(\\overline{A}) = 1 - P(A)$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Xác suất cổ điển** ($P(A) = '
                   '\\dfrac{n(A)}{n(\\Omega)}$) vào giải bài tập.'],
  'definition': 'Mỗi tập con $A$ của không gian mẫu $\\Omega$ được gọi là một biến cố. Biến cố đối của biến '
                "cố $A$ là biến cố 'không xảy ra $A$', kí hiệu là $\\overline{A} = \\Omega \\setminus A$. "
                'Xác suất cổ điển: $P(A) = \\dfrac{n(A)}{n(\\Omega)}$.',
  'theory': 'Tính chất của xác suất:\n'
            '- $P(\\varnothing) = 0$; $P(\\Omega) = 1$; $0 \\le P(A) \\le 1$ với mọi biến cố $A$.\n'
            '- Với mọi biến cố $A$, ta có $n(\\overline{A}) = n(\\Omega) - n(A)$ và $P(\\overline{A}) = 1 - '
            'P(A)$.',
  'formulas': [{'category': 'Định nghĩa cổ điển và tính chất của xác suất',
                'items': [{'name': 'Xác suất cổ điển',
                           'formula': '$P(A) = \\dfrac{n(A)}{n(\\Omega)}$',
                           'note': 'Khi các kết quả của $\\Omega$ đồng khả năng'},
                          {'name': 'Xác suất của biến cố đối',
                           'formula': '$P(\\overline{A}) = 1 - P(A)$',
                           'note': "Thường dùng khi biến cố $A$ có từ 'ít nhất một'"}]}],
  'example': "Gieo một con xúc xắc cân đối và đồng chất 2 lần. Tính xác suất của biến cố $A$: 'Có ít nhất "
             "một lần xuất hiện mặt 6 chấm'.",
  'example_answer': 'Không gian mẫu có $n(\\Omega) = 6 \\cdot 6 = 36$.\n'
                    "Biến cố đối $\\overline{A}$: 'Cả hai lần đều không xuất hiện mặt 6 chấm' có "
                    '$n(\\overline{A}) = 5 \\cdot 5 = 25$.\n'
                    'Suy ra $P(A) = 1 - P(\\overline{A}) = 1 - \\dfrac{25}{36} = \\dfrac{11}{36}$.',
  'real_life': 'Đánh giá rủi ro hỏng hóc của hệ thống máy móc hoặc tính xác suất trúng thưởng trong trò chơi '
               'may rủi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho biến cố $A$ có xác suất $P(A) = 0,35$. Xác suất của biến cố đối $\\overline{A}$ là:',
            'options': ['$0,35$', '$0,65$', '$1,35$', '$0,75$'],
            'answer': 1,
            'solution': 'Ta có $P(\\overline{A}) = 1 - P(A) = 1 - 0,35 = 0,65$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các mệnh đề sau về xác suất của biến cố, mệnh đề nào là đúng?',
            'options': ['$P(\\varnothing) = 1$ và $P(\\Omega) = 0$',
                        '$P(A) > 1$ với mọi biến cố $A$',
                        '$P(\\varnothing) = 0$ và $P(\\Omega) = 1$',
                        '$P(A) + P(\\overline{A}) = 0$'],
            'answer': 2,
            'solution': 'Biến cố không thể $\\varnothing$ có xác suất bằng $0$ và biến cố chắc chắn '
                        '$\\Omega$ có xác suất bằng $1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 26: Biến cố và định nghĩa cổ điển của xác suất**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Xác suất cổ điển**?',
            'options': ['$P(\\overline{A}) = 1 - P(A)$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai',
                        '$P(A) = \\dfrac{n(A)}{n(\\Omega)}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 26: Biến cố và định nghĩa cổ điển của xác '
                        'suất, **Xác suất cổ điển** được xác định bởi: $P(A) = \\dfrac{n(A)}{n(\\Omega)}$. '
                        '(Khi các kết quả của $\\Omega$ đồng khả năng)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Biến cố và định nghĩa cổ điển của xác suất**, nội dung/biểu thức '
                 '$P(\\overline{A}) = 1 - P(A)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Xác suất của biến cố đối',
                        'Xác suất cổ điển',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương'],
            'answer': 0,
            'solution': 'Trong Bài 26: Biến cố và định nghĩa cổ điển của xác suất, biểu thức/quy tắc '
                        '$P(\\overline{A}) = 1 - P(A)$ chính là nội dung của **Xác suất của biến cố đối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tung một đồng xu cân đối và đồng chất $3$ lần liên tiếp. Số phần tử của không gian mẫu '
                 '$\\Omega$ là:',
            'options': ['$6$', '$8$', '$9$', '$4$'],
            'answer': 1,
            'solution': 'Mỗi lần tung có $2$ kết quả nên tung 3 lần có $n(\\Omega) = 2^3 = 8$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Biến cố và định nghĩa cổ điển của xác suất** (Chương IX: Tính xác suất '
                 'theo định nghĩa cổ điển), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Mô tả được không gian mẫu $\\Omega$, biến cố $A$, biến cố chắc chắn, biến cố không '
                        'thể và biến cố đối $\\overline{A}$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 26: Biến cố và định nghĩa cổ điển của xác suất: Mô tả '
                        'được không gian mẫu $\\Omega$, biến cố $A$, biến cố chắc chắn, biến cố không thể và '
                        'biến cố đối $\\overline{A}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Tung một đồng xu cân đối và đồng chất $3$ lần liên tiếp. Xét biến cố $A$: 'Có ít nhất một "
                 "lần xuất hiện mặt ngửa'.",
            'statements': ['Số phần tử của không gian mẫu là $n(\\Omega) = 8$.',
                           "Biến cố đối $\\overline{A}$ là: 'Cả 3 lần tung đều xuất hiện mặt sấp'.",
                           'Số phần tử của biến cố đối $\\overline{A}$ là $n(\\overline{A}) = 1$.',
                           'Xác suất của biến cố $A$ là $P(A) = \\dfrac{3}{8}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng. c) Đúng (chỉ có kết quả SSS). d) Sai vì $P(A) = 1 - \\dfrac{1}{8} '
                        '= \\dfrac{7}{8}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 26: Biến cố và định '
                 'nghĩa cổ điển của xác suất**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được không gian mẫu '
                           '$\\Omega$, biến cố $A$, biến cố chắc chắn, biến cố không thể và biến cố đối '
                           '$\\overline{A}$.',
                           'Quy tắc/công thức **Xác suất cổ điển** trong bài được xác định bởi: $P(A) = '
                           '\\dfrac{n(A)}{n(\\Omega)}$.',
                           'Trong mọi trường hợp, **Xác suất cổ điển** luôn được tính bằng công thức $P '
                           '\\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh đề kéo theo) mà không '
                           'cần điều kiện của Bài 26: Biến cố và định nghĩa cổ điển của xác suất.',
                           'Với bài toán minh họa: “Gieo một con xúc xắc cân đối và đồng chất 2 lần. Tính '
                           "xác suất của biến cố $A$: 'Có ít nhất một lần xuất hiện mặt 6 chấm'.”, lời giải "
                           'đúng là: Không gian mẫu có $n(\\Omega) = 6 \\cdot 6 = 36$. Biến cố đối '
                           "$\\overline{A}$: 'Cả hai lần đều không xuất hiện mặt 6 chấm' có "
                           '$n(\\overline{A}) = 5 \\cdot 5 = 25$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 26: Biến cố và định nghĩa cổ điển của xác '
                        'suất. b) **Đúng** theo công thức trọng tâm **Xác suất cổ điển** ($P(A) = '
                        '\\dfrac{n(A)}{n(\\Omega)}$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, '
                        '$Q$ sai là công thức của nội dung khác, không phải quy tắc chung của **Xác suất cổ '
                        'điển**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 26: Biến cố và định nghĩa cổ điển của xác suất** để giải quyết '
                 'tình huống sau: Gieo một con xúc xắc cân đối và đồng chất 2 lần. Tính xác suất của biến cố '
                 "$A$: 'Có ít nhất một lần xuất hiện mặt 6 chấm'. Kết quả và hướng giải nào dưới đây là "
                 '**đúng**?',
            'options': ["Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...',
                        "Không gian mẫu có $n(\\Omega) = 6 \\cdot 6 = 36$. Biến cố đối $\\overline{A}$: 'Cả "
                        "hai lần đều không xuất hiện mặt 6 chấm' có $n(\\overline{A}) = 5 \\cdot 5 = 25$..."],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 26: Biến cố và định nghĩa cổ điển của xác suất: Không '
                        'gian mẫu có $n(\\Omega) = 6 \\cdot 6 = 36$.\n'
                        "Biến cố đối $\\overline{A}$: 'Cả hai lần đều không xuất hiện mặt 6 chấm' có "
                        '$n(\\overline{A}) = 5 \\cdot 5 = 25$.\n'
                        'Suy ra $P(A) = 1 - P(\\overline{A}) = 1 - \\dfrac{25}{36} = \\dfrac{11}{36}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Chọn ngẫu nhiên một số tự nhiên từ $1$ đến $20$. Tính xác suất để số được chọn chia hết '
                 'cho $5$ (viết kết quả dưới dạng số thập phân).',
            'answer': ['0,2', '0.2'],
            'unit': None,
            'solution': 'Không gian mẫu có $20$ phần tử. Các số chia hết cho 5 là $5, 10, 15, 20$ (gồm $4$ '
                        'số). Xác suất là $\\dfrac{4}{20} = 0,2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l10-ch09-xac-suat',
  'context_title': 'Chương IX: Tính xác suất theo định nghĩa cổ điển',
  'context': 'Chương IX · SGK Toán 10: Tính xác suất theo định nghĩa cổ điển.',
  'title': 'Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển',
  'icon': '🏆',
  'description': 'Vận dụng quy tắc đếm, hoán vị, chỉnh hợp, tổ hợp và biến cố đối để tính xác suất trong các '
                 'bài toán tổng hợp.',
  'requirements': ['Kết hợp quy tắc cộng, quy tắc nhân, hoán vị, chỉnh hợp, tổ hợp để tính $n(\\Omega)$ và '
                   '$n(A)$.',
                   'Sử dụng linh hoạt phương pháp đếm trực tiếp hoặc sử dụng biến cố đối để tính xác suất.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Chọn ngẫu nhiên $k$ phần tử từ $n$ phần '
                   'tử** ($n(\\Omega) = C_n^k$) vào giải bài tập.'],
  'definition': 'Trong các phép thử có số phần tử không gian mẫu lớn, ta sử dụng các công cụ đại số tổ hợp '
                '($P_n, A_n^k, C_n^k$) để tính $n(\\Omega)$ và $n(A)$ thay vì liệt kê từng phần tử.',
  'theory': 'Hai phương pháp chính để tính xác suất của biến cố $A$:\n'
            '- Phương pháp 1 (Đếm trực tiếp): Tính $n(\\Omega)$, chia trường hợp để đếm trực tiếp $n(A)$ rồi '
            'tính $P(A) = \\dfrac{n(A)}{n(\\Omega)}$.\n'
            "- Phương pháp 2 (Sử dụng biến cố đối): Khi biến cố $A$ có nhiều trường hợp (như 'có ít "
            "nhất...', 'không quá...'), ta tính số phần tử của biến cố đối $n(\\overline{A})$ rồi dùng công "
            'thức $P(A) = 1 - \\dfrac{n(\\overline{A})}{n(\\Omega)}$.',
  'formulas': [{'category': 'Kết hợp Đại số tổ hợp và Xác suất',
                'items': [{'name': 'Chọn ngẫu nhiên $k$ phần tử từ $n$ phần tử',
                           'formula': '$n(\\Omega) = C_n^k$',
                           'note': 'Không phân biệt thứ tự lấy ra'},
                          {'name': 'Công thức biến cố đối',
                           'formula': '$P(A) = 1 - \\dfrac{n(\\overline{A})}{n(\\Omega)}$',
                           'note': "Rất hiệu quả cho bài toán 'có ít nhất 1 phần tử...'"}]}],
  'example': 'Một hộp có 5 quả cầu trắng và 3 quả cầu đen. Lấy ngẫu nhiên đồng thời 2 quả cầu. Tính xác suất '
             'để lấy được 2 quả cầu cùng màu.',
  'example_answer': 'Số phần tử của không gian mẫu là $n(\\Omega) = C_8^2 = 28$.\n'
                    "Gọi $A$ là biến cố 'Lấy được 2 quả cầu cùng màu' (cùng trắng hoặc cùng đen). Ta có "
                    '$n(A) = C_5^2 + C_3^2 = 10 + 3 = 13$.\n'
                    'Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{13}{28}$.',
  'real_life': 'Kiểm định chất lượng sản phẩm theo lô (lấy mẫu ngẫu nhiên không hoàn lại) trong dây chuyền '
               'sản xuất công nghiệp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Từ một nhóm gồm $8$ học sinh, chọn ngẫu nhiên $3$ học sinh. Số phần tử của không gian mẫu '
                 '$n(\\Omega)$ là:',
            'options': ['$A_8^3 = 336$', '$8^3 = 512$', '$C_8^3 = 56$', '$3! = 6$'],
            'answer': 2,
            'solution': 'Chọn ngẫu nhiên 3 học sinh từ 8 học sinh không phân biệt thứ tự nên $n(\\Omega) = '
                        'C_8^3 = 56$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Xếp ngẫu nhiên $4$ bạn vào một bàn dài có $4$ ghế. Số phần tử của không gian mẫu là:',
            'options': ['$16$', '$4$', '$12$', '$24$'],
            'answer': 3,
            'solution': 'Số cách xếp 4 bạn vào 4 ghế là $P_4 = 4! = 24$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Chọn ngẫu nhiên $k$ phần tử từ $n$ '
                 'phần tử**?',
            'options': ['$n(\\Omega) = C_n^k$',
                        '$P(A) = 1 - \\dfrac{n(\\overline{A})}{n(\\Omega)}$',
                        '$P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai',
                        '$P \\Leftrightarrow Q$ đúng khi $P, Q$ cùng tính đúng sai'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 27: Thực hành tính xác suất theo định nghĩa '
                        'cổ điển, **Chọn ngẫu nhiên $k$ phần tử từ $n$ phần tử** được xác định bởi: '
                        '$n(\\Omega) = C_n^k$. (Không phân biệt thứ tự lấy ra)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển**, nội dung/biểu thức '
                 '$P(A) = 1 - \\dfrac{n(\\overline{A})}{n(\\Omega)}$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Chọn ngẫu nhiên $k$ phần tử từ $n$ phần tử',
                        'Công thức biến cố đối',
                        'Mệnh đề kéo theo',
                        'Mệnh đề tương đương'],
            'answer': 1,
            'solution': 'Trong Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển, biểu thức/quy tắc '
                        '$P(A) = 1 - \\dfrac{n(\\overline{A})}{n(\\Omega)}$ chính là nội dung của **Công '
                        'thức biến cố đối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hộp có $4$ bi đỏ và $3$ bi xanh. Lấy ngẫu nhiên đồng thời $2$ viên bi. Xác suất để lấy '
                 'được $2$ viên bi khác màu là:',
            'options': ['$\\dfrac{3}{7}$', '$\\dfrac{2}{7}$', '$\\dfrac{4}{7}$', '$\\dfrac{12}{49}$'],
            'answer': 2,
            'solution': 'Ta có $n(\\Omega) = C_7^2 = 21$. Số cách lấy 1 đỏ và 1 xanh là $4 \\cdot 3 = 12$. '
                        'Xác suất là $\\dfrac{12}{21} = \\dfrac{4}{7}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển** (Chương IX: Tính xác '
                 'suất theo định nghĩa cổ điển), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Nhận biết được mệnh đề toán học, mệnh đề chứa biến và xác định tính đúng sai của '
                        'một mệnh đề.',
                        'Thiết lập được mệnh đề phủ định $\\overline{P}$, mệnh đề kéo theo $P \\Rightarrow '
                        'Q$, mệnh đề đảo và mệnh đề tương đương $P \\Leftrightarrow Q$.',
                        'Sử dụng đúng kí hiệu với mọi ($\\forall$) và tồn tại ($\\exists$).',
                        'Kết hợp quy tắc cộng, quy tắc nhân, hoán vị, chỉnh hợp, tổ hợp để tính $n(\\Omega)$ '
                        'và $n(A)$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển: '
                        'Kết hợp quy tắc cộng, quy tắc nhân, hoán vị, chỉnh hợp, tổ hợp để tính $n(\\Omega)$ '
                        'và $n(A)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một tổ gồm $6$ học sinh nam và $4$ học sinh nữ. Chọn ngẫu nhiên $3$ học sinh từ tổ đi dự '
                 'hội nghị.',
            'statements': ['Số phần tử của không gian mẫu là $n(\\Omega) = C_{10}^3 = 120$.',
                           "Số kết quả thuận lợi cho biến cố 'Cả $3$ học sinh được chọn đều là nam' là "
                           '$C_6^3 = 20$.',
                           'Xác suất để chọn được đúng $2$ nam và $1$ nữ là $\\dfrac{1}{2}$.',
                           'Xác suất để có ít nhất $1$ học sinh nữ được chọn là $\\dfrac{1}{6}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng. c) Đúng vì $\\dfrac{C_6^2 \\cdot C_4^1}{120} = \\dfrac{15 \\cdot '
                        '4}{120} = \\dfrac{1}{2}$. d) Sai vì xác suất có ít nhất 1 nữ là $1 - '
                        '\\dfrac{C_6^3}{120} = 1 - \\dfrac{1}{6} = \\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 27: Thực hành tính xác '
                 'suất theo định nghĩa cổ điển**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Kết hợp quy tắc cộng, quy tắc '
                           'nhân, hoán vị, chỉnh hợp, tổ hợp để tính $n(\\Omega)$ và $n(A)$.',
                           'Quy tắc/công thức **Chọn ngẫu nhiên $k$ phần tử từ $n$ phần tử** trong bài được '
                           'xác định bởi: $n(\\Omega) = C_n^k$.',
                           'Trong mọi trường hợp, **Chọn ngẫu nhiên $k$ phần tử từ $n$ phần tử** luôn được '
                           'tính bằng công thức $P \\Rightarrow Q$ chỉ sai khi $P$ đúng, $Q$ sai (thuộc Mệnh '
                           'đề kéo theo) mà không cần điều kiện của Bài 27: Thực hành tính xác suất theo '
                           'định nghĩa cổ điển.',
                           'Với bài toán minh họa: “Một hộp có 5 quả cầu trắng và 3 quả cầu đen. Lấy ngẫu '
                           'nhiên đồng thời 2 quả cầu. Tính xác suất để lấy được 2 quả cầu cùng màu.”, lời '
                           'giải đúng là: Số phần tử của không gian mẫu là $n(\\Omega) = C_8^2 = 28$. Gọi '
                           "$A$ là biến cố 'Lấy được 2 quả cầu cùng màu' (cùng trắng hoặc cùng đen). Ta "
                           'c...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 27: Thực hành tính xác suất theo định '
                        'nghĩa cổ điển. b) **Đúng** theo công thức trọng tâm **Chọn ngẫu nhiên $k$ phần tử '
                        'từ $n$ phần tử** ($n(\\Omega) = C_n^k$). c) **Sai** vì $P \\Rightarrow Q$ chỉ sai '
                        'khi $P$ đúng, $Q$ sai là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Chọn ngẫu nhiên $k$ phần tử từ $n$ phần tử**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển** để giải '
                 'quyết tình huống sau: Một hộp có 5 quả cầu trắng và 3 quả cầu đen. Lấy ngẫu nhiên đồng '
                 'thời 2 quả cầu. Tính xác suất để lấy được 2 quả cầu cùng màu. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ["Số phần tử của không gian mẫu là $n(\\Omega) = C_8^2 = 28$. Gọi $A$ là biến cố 'Lấy "
                        "được 2 quả cầu cùng màu' (cùng trắng hoặc cùng đen). Ta có $n(A) = C_5^2 + C_3^2 = "
                        '10 + 3 = 13$...',
                        "Mệnh đề phủ định là $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le "
                        "0$'. Vì $x^2 \\ge 0 \\Rightarrow x^2 + 1 \\ge 1 > 0$ với mọi $x \\in \\mathbb{R}$ "
                        'nê...',
                        'Biểu diễn trên trục số, ta được: - $A \\cap B = (1; 3)$; - $A \\cup B = [-2; 5]$; - '
                        '$A \\setminus B = [-2; 1]$.',
                        'Thay $x = 1, y = 2$ vào vế trái của bất phương trình: $2(1) - 3(2) + 1 = 2 - 6 + 1 '
                        '= -3 < 0$ (đúng). Vậy điểm $A(1; 2)$ thuộc miền nghiệm của bất phương tr...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển: Số '
                        'phần tử của không gian mẫu là $n(\\Omega) = C_8^2 = 28$.\n'
                        "Gọi $A$ là biến cố 'Lấy được 2 quả cầu cùng màu' (cùng trắng hoặc cùng đen). Ta có "
                        '$n(A) = C_5^2 + C_3^2 = 10 + 3 = 13$.\n'
                        'Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{13}{28}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp có $6$ sản phẩm tốt và $4$ sản phẩm lỗi. Lấy ngẫu nhiên đồng thời $2$ sản phẩm để '
                 'kiểm tra. Tính xác suất để cả $2$ sản phẩm lấy ra đều là sản phẩm tốt (viết kết quả dưới '
                 'dạng phân số tối giản $a/b$).',
            'answer': ['1/3'],
            'unit': None,
            'solution': 'Ta có $n(\\Omega) = C_{10}^2 = 45$; số cách lấy 2 sản phẩm tốt là $C_6^2 = 15$. Xác '
                        'suất cần tìm là $\\dfrac{15}{45} = \\dfrac{1}{3}$.',
            'alt': None,
            'note': None}]}]
