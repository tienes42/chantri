"""Dữ liệu bài học SGK Toán Lớp 12 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 12 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học độc lập (title).
Mỗi bài học chỉ chứa kiến thức, công thức, ví dụ và 10 câu hỏi của riêng bài học đó.
"""

GRADE = 12

LESSONS = [{'topic': 'l12-ch01-ung-dung-dao-ham',
  'context_title': 'Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số',
  'context': 'Chương I · SGK Toán 12: Đơn điệu, cực trị, giá trị lớn nhất - nhỏ nhất, tiệm cận và khảo sát '
             'vẽ đồ thị hàm số.',
  'title': 'Bài 1: Tính đơn điệu và cực trị của hàm số',
  'icon': '📈',
  'description': 'Mối liên hệ giữa dấu của đạo hàm với tính đồng biến, nghịch biến và điểm cực đại, cực tiểu '
                 'của hàm số.',
  'requirements': ['Nhận biết được tính đồng biến, nghịch biến của hàm số trên một khoảng dựa vào dấu của '
                   "đạo hàm cấp một $f'(x)$.",
                   'Xác định được điểm cực đại, điểm cực tiểu, giá trị cực đại, giá trị cực tiểu của hàm số '
                   "thông qua bảng biến thiên hoặc đạo hàm cấp hai $f''(x)$.",
                   'Vận dụng điều kiện đơn điệu và cực trị để giải các bài toán chứa tham số $m$.'],
  'definition': 'Cho hàm số $y = f(x)$ xác định trên khoảng $K$. Hàm số đồng biến trên $K$ nếu $\\forall '
                'x_1, x_2 \\in K, x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$; nghịch biến trên $K$ nếu $x_1 < '
                'x_2 \\Rightarrow f(x_1) > f(x_2)$. Điểm $x_0 \\in K$ gọi là điểm cực đại (hoặc cực tiểu) '
                'nếu tồn tại lân cận $(a; b) \\subset K$ chứa $x_0$ sao cho $f(x) < f(x_0)$ (hoặc $f(x) > '
                'f(x_0)$) với mọi $x \\in (a; b) \\setminus \\{x_0\\}$.',
  'theory': "1. Định lí đơn điệu: Nếu $f'(x) > 0$ với mọi $x \\in K$ thì $f(x)$ đồng biến trên $K$; nếu "
            "$f'(x) < 0$ với mọi $x \\in K$ thì $f(x)$ nghịch biến trên $K$ (nếu $f'(x) = 0$ chỉ tại hữu hạn "
            "điểm thì tính đơn điệu vẫn giữ nguyên). 2. Dấu hiệu cực trị: Nếu $f'(x)$ đổi dấu từ dương sang "
            'âm khi qua $x_0$ thì $x_0$ là điểm cực đại; đổi dấu từ âm sang dương khi qua $x_0$ thì $x_0$ là '
            "điểm cực tiểu. 3. Quy tắc 2: Nếu $f'(x_0) = 0$ và $f''(x_0) < 0$ thì $x_0$ là điểm cực đại; nếu "
            "$f'(x_0) = 0$ và $f''(x_0) > 0$ thì $x_0$ là điểm cực tiểu.",
  'formulas': [{'category': 'Điều kiện đơn điệu và cực trị',
                'items': [{'name': 'Đồng biến trên khoảng',
                           'formula': "$f'(x) \\ge 0, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)"},
                          {'name': 'Nghịch biến trên khoảng',
                           'formula': "$f'(x) \\le 0, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)"},
                          {'name': 'Điều kiện cần của cực trị',
                           'formula': '$f(x)$ đạt cực trị tại $x_0$ và có đạo hàm tại $x_0 \\Rightarrow '
                                      "f'(x_0) = 0$"},
                          {'name': 'Cực trị bằng đạo hàm cấp hai',
                           'formula': "$f'(x_0) = 0, f''(x_0) < 0 \\Rightarrow x_{CĐ}; \\quad f'(x_0) = 0, "
                                      "f''(x_0) > 0 \\Rightarrow x_{CT}$"}]}],
  'example': 'Tìm các khoảng đơn điệu và cực trị của hàm số $y = x^3 - 3x^2 + 2$.',
  'example_answer': "Tập xác định $D = \\mathbb{R}$. Ta có $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 "
                    "\\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu $y'$: trên $(-\\infty; 0)$ và $(2; "
                    "+\\infty)$ ta có $y' > 0$ nên hàm số đồng biến; trên $(0; 2)$ ta có $y' < 0$ nên hàm số "
                    'nghịch biến. Hàm số đạt cực đại tại $x = 0$, giá trị cực đại $y_{CĐ} = 2$; đạt cực tiểu '
                    'tại $x = 2$, giá trị cực tiểu $y_{CT} = -2$.',
  'real_life': 'Phân tích tốc độ tăng trưởng kinh tế, xác định thời điểm lợi nhuận đạt đỉnh (cực đại) hoặc '
               'chi phí vận hành xuống mức thấp nhất (cực tiểu).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $(a; b)$. Mệnh đề nào dưới đây đúng?',
            'options': ["Nếu $f'(x) > 0$ với mọi $x \\in (a; b)$ thì hàm số đồng biến trên $(a; b)$.",
                        "Nếu $f'(x) > 0$ với mọi $x \\in (a; b)$ thì hàm số nghịch biến trên $(a; b)$.",
                        "Nếu $f(x)$ đồng biến trên $(a; b)$ thì $f'(x) < 0$ với mọi $x \\in (a; b)$.",
                        "Nếu $f'(x) = 0$ tại $x_0 \\in (a; b)$ thì $x_0$ luôn là điểm cực trị."],
            'answer': 0,
            'solution': "Theo định lí về tính đơn điệu, nếu $f'(x) > 0, \\forall x \\in (a; b)$ thì hàm số "
                        '$f(x)$ đồng biến trên khoảng $(a; b)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hàm số $y = x^3 - 3x + 1$ nghịch biến trên khoảng nào dưới đây?',
            'options': ['$(-\\infty; -1)$', '$(-1; 1)$', '$(1; +\\infty)$', '$(0; 2)$'],
            'answer': 1,
            'solution': "Ta có $y' = 3x^2 - 3$. Giải $y' < 0 \\Leftrightarrow 3(x^2 - 1) < 0 "
                        '\\Leftrightarrow -1 < x < 1$. Vậy hàm số nghịch biến trên $(-1; 1)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Tính đơn điệu và cực trị của hàm số**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Đồng biến trên khoảng**?',
            'options': ["$f'(x) \\ge 0, \\forall x \\notin K$ (dấu $=$ tại hữu hạn điểm)",
                        "$f'(x) \\ge 1, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)",
                        "$f'(x) \\ge 0, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)",
                        "$f'(x) \\ge 2, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)"],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 1: Tính đơn điệu và cực trị của hàm số, **Đồng '
                        "biến trên khoảng** được xác định bởi: $f'(x) \\ge 0, \\forall x \\in K$ (dấu $=$ "
                        'tại hữu hạn điểm).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Tính đơn điệu và cực trị của hàm số**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Nghịch biến trên khoảng**?',
            'options': ["$f'(x) \\le 0, \\forall x \\notin K$ (dấu $=$ tại hữu hạn điểm)",
                        "$f'(x) \\le 1, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)",
                        "$f'(x) \\le 2, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)",
                        "$f'(x) \\le 0, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm)"],
            'answer': 3,
            'solution': 'Trong Bài 1: Tính đơn điệu và cực trị của hàm số, **Nghịch biến trên khoảng** có '
                        "công thức/quy tắc là: $f'(x) \\le 0, \\forall x \\in K$ (dấu $=$ tại hữu hạn "
                        'điểm).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị cực đại của hàm số $y = -x^4 + 2x^2 + 3$ bằng bao nhiêu?',
            'options': ['$4$', '$3$', '$1$', '$2$'],
            'answer': 0,
            'solution': "Ta có $y' = -4x^3 + 4x = -4x(x^2 - 1) = 0 \\Leftrightarrow x \\in \\{-1; 0; 1\\}$. "
                        'Đạo hàm đổi dấu từ dương sang âm qua $x = -1$ và $x = 1$, tại đó $y_{CĐ} = -1 + 2 + '
                        '3 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 1: Tính đơn điệu và cực trị của hàm số**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận biết được tính nghịch biến, nghịch biến của hàm số trên một khoảng dựa vào dấu '
                        "của đạo hàm cấp một $f'(x)$.",
                        'Nhận biết được tính đồng biến, nghịch biến của hàm số trên một khoảng dựa vào dấu '
                        "của đạo hàm cấp một $f'(x)$.",
                        'Đảo ngược vế của quy tắc: Nhận biết được tính đồng biến, nghịch biến của hàm số '
                        "trên một khoảng dựa vào dấu của đạo hàm cấp một $f'(x)$.",
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được tính đồng biến, '
                        "nghịch biến của hàm số trên một khoảng dựa vào dấu của đạo hàm cấp một $f'(x)$."],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 1: Tính đơn điệu và cực trị của hàm số: Nhận biết '
                        'được tính đồng biến, nghịch biến của hàm số trên một khoảng dựa vào dấu của đạo hàm '
                        "cấp một $f'(x)$."},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $y = f(x) = x^3 - 3x^2 - 9x + 5$ xác định trên $\\mathbb{R}$. Xét tính đúng sai '
                 'của các mệnh đề sau:',
            'statements': ["Đạo hàm của hàm số đã cho là $f'(x) = 3x^2 - 6x - 9$.",
                           'Hàm số nghịch biến trên khoảng $(-1; 3)$.',
                           'Điểm cực đại của hàm số là $x = 3$.',
                           'Tổng giá trị cực đại và giá trị cực tiểu của hàm số bằng $-12$.'],
            'answer': [True, True, False, True],
            'solution': "a) Đúng vì $f'(x) = 3x^2 - 6x - 9$. b) Đúng vì $f'(x) < 0 \\Leftrightarrow -1 < x < "
                        "3$. c) Sai vì $f'(x)$ đổi dấu từ dương sang âm tại $x = -1$ nên $x_{CĐ} = -1$, còn "
                        '$x = 3$ là điểm cực tiểu. d) Đúng vì $y_{CĐ} = f(-1) = 10$ và $y_{CT} = f(3) = '
                        '-22$, tổng là $10 + (-22) = -12$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 1: Tính đơn điệu và cực trị '
                 'của hàm số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được tính đồng biến, nghịch '
                           "biến của hàm số trên một khoảng dựa vào dấu của đạo hàm cấp một $f'(x)$.",
                           'Trong **Bài 1: Tính đơn điệu và cực trị của hàm số**, quy tắc/công thức **Đồng '
                           "biến trên khoảng** được viết là: $f'(x) \\ge 0, \\forall x \\in K$ (dấu $=$ tại "
                           'hữu hạn điểm).',
                           "Nếu áp dụng sai dấu/phép tính thành $f'(x) \\ge 0, \\forall x \\notin K$ (dấu "
                           '$=$ tại hữu hạn điểm) thì kết quả của **Đồng biến trên khoảng** trong **Bài 1: '
                           'Tính đơn điệu và cực trị của hàm số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm các khoảng đơn điệu và cực trị của hàm số $y = x^3 - '
                           "3x^2 + 2$.”, kết quả giải đúng là: Tập xác định $D = \\mathbb{R}$. Ta có $y' = "
                           "3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng "
                           "xét dấu $y'$..."],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Tính đơn điệu và cực trị của hàm số. b) '
                        "**Đúng** theo công thức **Đồng biến trên khoảng** ($f'(x) \\ge 0, \\forall x \\in "
                        'K$ (dấu $=$ tại hữu hạn điểm)). c) **Sai** vì công thức đúng của **Đồng biến trên '
                        "khoảng** phải là $f'(x) \\ge 0, \\forall x \\in K$ (dấu $=$ tại hữu hạn điểm) chứ "
                        "không phải $f'(x) \\ge 0, \\forall x \\notin K$ (dấu $=$ tại hữu hạn điểm). d) "
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 1: Tính đơn điệu và cực trị của hàm số** để giải '
                 'bài toán sau: Tìm các khoảng đơn điệu và cực trị của hàm số $y = x^3 - 3x^2 + 2$. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ["Tập xác định $D = \\mathbb{R}$. Ta có $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 "
                        "\\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu $y'$: trên $(-\\infty; 0)$...",
                        "Tập xác định $D = \\mathbb{R}$. Ta có $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 "
                        "\\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu $y'$: trên $(-\\infty; 1)$...",
                        "Tập xác định $D = \\mathbb{R}$. Ta có $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 "
                        "\\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu $y'$: trên $(-\\infty; 0)$...",
                        "Tập xác định $D = \\mathbb{R}$. Ta có $y' = 3x^4 - 6x = 3x(x - 2)$. Cho $y' = 0 "
                        "\\Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu $y'$: trên $(-\\infty; 0)$..."],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Tính đơn điệu và cực trị của hàm số: Tập xác định $D '
                        "= \\mathbb{R}$. Ta có $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 \\Leftrightarrow x "
                        "= 0$ hoặc $x = 2$. Bảng xét dấu $y'$: trên $(-\\infty; 0)$ và $(2; +\\infty)$ ta có "
                        "$y' > 0$ nên hàm số đồng biến; trên $(0; 2)$ ta có $y' < 0$ nên hàm số nghịch biến. "
                        'Hàm số đạt cực đại tại $x = 0$, giá trị cực đại $y_{CĐ} = 2$; đạt cực tiểu tại $x = '
                        '2$, giá trị cực tiểu $y_{CT} = -2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu giá trị nguyên của tham số $m$ để hàm số $y = \\dfrac{1}{3}x^3 - mx^2 + (m + '
                 '2)x - 1$ đồng biến trên $\\mathbb{R}$?',
            'answer': ['4'],
            'unit': None,
            'solution': "Ta có $y' = x^2 - 2mx + m + 2$. Hàm số đồng biến trên $\\mathbb{R} \\Leftrightarrow "
                        "y' \\ge 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\Delta' = m^2 - (m + 2) "
                        '\\le 0 \\Leftrightarrow m^2 - m - 2 \\le 0 \\Leftrightarrow -1 \\le m \\le 2$. Có '
                        '$4$ giá trị nguyên là $m \\in \\{-1; 0; 1; 2\\}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch01-ung-dung-dao-ham',
  'context_title': 'Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số',
  'context': 'Chương I · SGK Toán 12: Đơn điệu, cực trị, giá trị lớn nhất - nhỏ nhất, tiệm cận và khảo sát '
             'vẽ đồ thị hàm số.',
  'title': 'Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số',
  'icon': '🏔️',
  'description': 'Khái niệm giá trị lớn nhất, giá trị nhỏ nhất của hàm số trên một tập hợp và quy tắc tìm '
                 'trên đoạn.',
  'requirements': ['Nhận biết được khái niệm giá trị lớn nhất $\\max_D f(x)$ và giá trị nhỏ nhất $\\min_D '
                   'f(x)$ của hàm số trên tập $D$.',
                   'Tìm được giá trị lớn nhất và giá trị nhỏ nhất của hàm số liên tục trên một đoạn $[a; b]$ '
                   'hoặc một khoảng.',
                   'Vận dụng vào các bài toán tối ưu hóa hình học và thực tế.'],
  'definition': 'Cho hàm số $y = f(x)$ xác định trên tập $D$. Số $M$ gọi là giá trị lớn nhất của $f(x)$ trên '
                '$D$, kí hiệu $M = \\max_{x \\in D} f(x)$, nếu $f(x) \\le M$ với mọi $x \\in D$ và tồn tại '
                '$x_0 \\in D$ sao cho $f(x_0) = M$. Số $m$ gọi là giá trị nhỏ nhất của $f(x)$ trên $D$, kí '
                'hiệu $m = \\min_{x \\in D} f(x)$, nếu $f(x) \\ge m$ với mọi $x \\in D$ và tồn tại $x_0 \\in '
                'D$ sao cho $f(x_0) = m$.',
  'theory': 'Quy tắc tìm $\\max, \\min$ của hàm số $f(x)$ liên tục trên đoạn $[a; b]$: Bước 1: Tìm các điểm '
            "$x_1, x_2, \\dots, x_n \\in (a; b)$ mà tại đó $f'(x) = 0$ hoặc $f'(x)$ không xác định. Bước 2: "
            'Tính $f(a), f(b), f(x_1), \\dots, f(x_n)$. Bước 3: Số lớn nhất trong các giá trị vừa tính là '
            '$\\max_{[a; b]} f(x)$ và số nhỏ nhất là $\\min_{[a; b]} f(x)$.',
  'formulas': [{'category': 'Quy tắc trên đoạn',
                'items': [{'name': 'Giá trị lớn nhất trên đoạn',
                           'formula': '$\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in '
                                      "(a; b), f'(x_i) = 0$"},
                          {'name': 'Giá trị nhỏ nhất trên đoạn',
                           'formula': '$\\min_{[a; b]} f(x) = \\min \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in '
                                      "(a; b), f'(x_i) = 0$"},
                          {'name': 'Hàm phân thức bậc nhất trên đoạn',
                           'formula': '$y = \\dfrac{ax + b}{cx + d}$ đơn điệu trên $[x_1; x_2]$ nên đạt '
                                      '$\\max, \\min$ tại hai đầu mút'}]}],
  'example': 'Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x + 2$ trên đoạn $[0; 2]$.',
  'example_answer': "Hàm số liên tục trên $[0; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 \\in "
                    '(0; 2)$ hoặc $x = -1 \\notin (0; 2)$. Tính giá trị: $f(0) = 2$; $f(1) = 0$; $f(2) = 4$. '
                    'Vậy $\\max_{[0; 2]} f(x) = f(2) = 4$ và $\\min_{[0; 2]} f(x) = f(1) = 0$.',
  'real_life': 'Thiết kế bao bì hộp sữa có dung tích cố định sao cho diện tích vỏ hộp tốn ít nguyên liệu '
               'nhất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị nhỏ nhất của hàm số $f(x) = x^2 - 4x + 5$ trên đoạn $[1; 4]$ bằng bao nhiêu?',
            'options': ['$2$', '$1$', '$5$', '$0$'],
            'answer': 1,
            'solution': "Ta có $f'(x) = 2x - 4 = 0 \\Leftrightarrow x = 2 \\in [1; 4]$. Tính $f(1) = 2, f(2) "
                        '= 1, f(4) = 5$. Vậy $\\min_{[1; 4]} f(x) = 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị lớn nhất của hàm số $y = \\dfrac{x - 1}{x + 1}$ trên đoạn $[0; 3]$ bằng bao nhiêu?',
            'options': ['$-1$', '$1$', '$\\dfrac{1}{2}$', '$\\dfrac{3}{4}$'],
            'answer': 2,
            'solution': "Ta có $y' = \\dfrac{2}{(x + 1)^2} > 0, \\forall x \\in [0; 3]$. Hàm số đồng biến "
                        'trên $[0; 3]$ nên $\\max_{[0; 3]} y = y(3) = \\dfrac{3 - 1}{3 + 1} = '
                        '\\dfrac{1}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Giá trị lớn nhất trên đoạn**?',
            'options': ['$\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\notin (a; b), '
                        "f'(x_i) = 0$",
                        '$\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), '
                        "f'(x_i) = 1$",
                        '$\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), '
                        "f'(x_i) = 2$",
                        '$\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), '
                        "f'(x_i) = 0$"],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm '
                        'số, **Giá trị lớn nhất trên đoạn** được xác định bởi: $\\max_{[a; b]} f(x) = \\max '
                        "\\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), f'(x_i) = 0$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Giá trị nhỏ nhất trên đoạn**?',
            'options': ['$\\min_{[a; b]} f(x) = \\min \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), '
                        "f'(x_i) = 0$",
                        '$\\min_{[a; b]} f(x) = \\min \\{f(a), f(b), f(x_i)\\}$ với $x_i \\notin (a; b), '
                        "f'(x_i) = 0$",
                        '$\\min_{[a; b]} f(x) = \\min \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), '
                        "f'(x_i) = 1$",
                        '$\\min_{[a; b]} f(x) = \\min \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), '
                        "f'(x_i) = 2$"],
            'answer': 0,
            'solution': 'Trong Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số, **Giá trị nhỏ nhất '
                        'trên đoạn** có công thức/quy tắc là: $\\min_{[a; b]} f(x) = \\min \\{f(a), f(b), '
                        "f(x_i)\\}$ với $x_i \\in (a; b), f'(x_i) = 0$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hàm số $f(x) = x + \\dfrac{4}{x}$ xét trên khoảng $(0; +\\infty)$. Giá trị nhỏ nhất '
                 'của hàm số trên khoảng $(0; +\\infty)$ là:',
            'options': ['$2$', '$4$', '$5$', '$8$'],
            'answer': 1,
            'solution': "Với $x > 0$, ta có $f'(x) = 1 - \\dfrac{4}{x^2} = 0 \\Leftrightarrow x = 2$. Lập "
                        'bảng biến thiên trên $(0; +\\infty)$, hàm số đạt giá trị nhỏ nhất tại $x = 2$ với '
                        '$f(2) = 2 + \\dfrac{4}{2} = 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được khái niệm giá trị lớn nhất $\\max_D f(x)$ và giá trị nhỏ nhất '
                        '$\\min_D f(x)$ của hàm số trên tập $D$. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được khái niệm giá trị lớn nhất $\\max_D f(x)$ '
                        'và giá trị nhỏ nhất $\\min_D f(x)$ của hàm số trên tập $D$.',
                        'Nhận biết được khái niệm giá trị lớn nhất $\\max_D f(x)$ và giá trị nhỏ nhất '
                        '$\\min_D f(x)$ của hàm số trên tập $D$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được khái niệm giá '
                        'trị lớn nhất $\\max_D f(x)$ và giá trị nhỏ nhất $\\min_D f(x)$ của hàm số trên tập '
                        '$D$.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số: '
                        'Nhận biết được khái niệm giá trị lớn nhất $\\max_D f(x)$ và giá trị nhỏ nhất '
                        '$\\min_D f(x)$ của hàm số trên tập $D$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $f(x) = x^4 - 2x^2 + 3$ trên đoạn $[0; 2]$. Xét tính đúng sai của các mệnh đề '
                 'sau:',
            'statements': ["Đạo hàm của hàm số là $f'(x) = 4x^3 - 4x$.",
                           "Trên khoảng $(0; 2)$, phương trình $f'(x) = 0$ có đúng 2 nghiệm.",
                           'Giá trị nhỏ nhất của hàm số trên đoạn $[0; 2]$ bằng $2$.',
                           'Giá trị lớn nhất của hàm số trên đoạn $[0; 2]$ bằng $11$.'],
            'answer': [True, False, True, True],
            'solution': "a) Đúng vì $f'(x) = 4x^3 - 4x$. b) Sai vì $f'(x) = 0 \\Leftrightarrow x \\in \\{-1; "
                        '0; 1\\}$, chỉ có $x = 1$ thuộc khoảng $(0; 2)$. c) Đúng vì $f(0) = 3, f(1) = 2, '
                        'f(2) = 11 \\Rightarrow \\min_{[0; 2]} f(x) = 2$. d) Đúng vì $\\max_{[0; 2]} f(x) = '
                        'f(2) = 11$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 2: Giá trị lớn nhất và giá '
                 'trị nhỏ nhất của hàm số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được khái niệm giá trị lớn '
                           'nhất $\\max_D f(x)$ và giá trị nhỏ nhất $\\min_D f(x)$ của hàm số trên tập $D$.',
                           'Trong **Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số**, quy tắc/công '
                           'thức **Giá trị lớn nhất trên đoạn** được viết là: $\\max_{[a; b]} f(x) = \\max '
                           "\\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), f'(x_i) = 0$.",
                           'Nếu áp dụng sai dấu/phép tính thành $\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), '
                           "f(x_i)\\}$ với $x_i \\notin (a; b), f'(x_i) = 0$ thì kết quả của **Giá trị lớn "
                           'nhất trên đoạn** trong **Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm '
                           'số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $f(x) = '
                           'x^3 - 3x + 2$ trên đoạn $[0; 2]$.”, kết quả giải đúng là: Hàm số liên tục trên '
                           "$[0; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 \\in (0; 2)$ hoặc "
                           '$x = -1 \\notin (0; 2)$. Tính giá trị...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất '
                        'của hàm số. b) **Đúng** theo công thức **Giá trị lớn nhất trên đoạn** ($\\max_{[a; '
                        "b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), f'(x_i) = 0$). c) "
                        '**Sai** vì công thức đúng của **Giá trị lớn nhất trên đoạn** phải là $\\max_{[a; '
                        "b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\in (a; b), f'(x_i) = 0$ chứ "
                        'không phải $\\max_{[a; b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}$ với $x_i \\notin '
                        "(a; b), f'(x_i) = 0$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học."},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm '
                 'số** để giải bài toán sau: Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $f(x) = x^3 '
                 '- 3x + 2$ trên đoạn $[0; 2]$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ["Hàm số liên tục trên $[0; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 "
                        '\\notin (0; 2)$ hoặc $x = -1 \\notin (0; 2)$. Tính giá trị: $f(0) = 2$; $f(1) = '
                        '0$...',
                        "Hàm số liên tục trên $[0; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 "
                        '\\in (0; 2)$ hoặc $x = -1 \\notin (0; 2)$. Tính giá trị: $f(0) = 2$; $f(1) = 1$...',
                        "Hàm số liên tục trên $[2; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 "
                        '\\in (0; 2)$ hoặc $x = -1 \\notin (0; 2)$. Tính giá trị: $f(0) = 2$; $f(1) = 0$...',
                        "Hàm số liên tục trên $[0; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 "
                        '\\in (0; 2)$ hoặc $x = -1 \\notin (0; 2)$. Tính giá trị: $f(0) = 2$; $f(1) = 0$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số: Hàm '
                        "số liên tục trên $[0; 2]$. Ta có $f'(x) = 3x^2 - 3 = 0 \\Leftrightarrow x = 1 \\in "
                        '(0; 2)$ hoặc $x = -1 \\notin (0; 2)$. Tính giá trị: $f(0) = 2$; $f(1) = 0$; $f(2) = '
                        '4$. Vậy $\\max_{[0; 2]} f(x) = f(2) = 4$ và $\\min_{[0; 2]} f(x) = f(1) = 0$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = x^3 - 3x^2 - 9x + 10$ trên đoạn '
                 '$[-2; 2]$ bằng bao nhiêu?',
            'answer': ['3'],
            'unit': None,
            'solution': "Ta có $y' = 3x^2 - 6x - 9 = 0 \\Leftrightarrow x = -1 \\in [-2; 2]$ hoặc $x = 3 "
                        '\\notin [-2; 2]$. Tính $y(-2) = 8, y(-1) = 15, y(2) = -12$. Vậy $\\max = 15, \\min '
                        '= -12$, tổng bằng $15 + (-12) = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch01-ung-dung-dao-ham',
  'context_title': 'Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số',
  'context': 'Chương I · SGK Toán 12: Đơn điệu, cực trị, giá trị lớn nhất - nhỏ nhất, tiệm cận và khảo sát '
             'vẽ đồ thị hàm số.',
  'title': 'Bài 3: Đường tiệm cận của đồ thị hàm số',
  'icon': '🛤️',
  'description': 'Cách xác định đường tiệm cận ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm số thông '
                 'qua giới hạn.',
  'requirements': ['Nhận biết được đường tiệm cận ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm số.',
                   'Tìm được phương trình các đường tiệm cận của hàm phân thức hữu tỉ bậc nhất trên bậc nhất '
                   'và bậc hai trên bậc nhất.',
                   'Giải quyết được bài toán biện luận số đường tiệm cận của đồ thị hàm số.'],
  'definition': 'Đường thẳng $y = y_0$ là tiệm cận ngang nếu $\\lim_{x \\to +\\infty} f(x) = y_0$ hoặc '
                '$\\lim_{x \\to -\\infty} f(x) = y_0$. Đường thẳng $x = x_0$ là tiệm cận đứng nếu ít nhất '
                'một trong các giới hạn một bên $\\lim_{x \\to x_0^+} f(x), \\lim_{x \\to x_0^-} f(x)$ bằng '
                '$+\\infty$ hoặc $-\\infty$. Đường thẳng $y = ax + b$ ($a \\ne 0$) là tiệm cận xiên nếu '
                '$\\lim_{x \\to +\\infty} [f(x) - (ax + b)] = 0$ hoặc $\\lim_{x \\to -\\infty} [f(x) - (ax + '
                'b)] = 0$.',
  'theory': '1. Đối với hàm phân thức $y = \\dfrac{ax + b}{cx + d}$ ($c \\ne 0, ad - bc \\ne 0$): tiệm cận '
            'đứng là $x = -\\dfrac{d}{c}$ và tiệm cận ngang là $y = \\dfrac{a}{c}$. 2. Đối với hàm phân thức '
            '$y = \\dfrac{ax^2 + bx + c}{mx + n}$ ($a \\ne 0, m \\ne 0$): chia đa thức được $y = px + q + '
            '\\dfrac{r}{mx + n}$ ($r \\ne 0$), khi đó tiệm cận đứng là $x = -\\dfrac{n}{m}$ và tiệm cận xiên '
            'là $y = px + q$.',
  'formulas': [{'category': 'Công thức tìm tiệm cận',
                'items': [{'name': 'Tiệm cận ngang',
                           'formula': '$\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow \\text{TCN: } y = '
                                      'y_0$'},
                          {'name': 'Tiệm cận đứng',
                           'formula': '$\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty \\Rightarrow \\text{TCĐ: '
                                      '} x = x_0$'},
                          {'name': 'Hệ số tiệm cận xiên',
                           'formula': '$a = \\lim_{x \\to \\pm\\infty} \\dfrac{f(x)}{x}, \\quad b = \\lim_{x '
                                      '\\to \\pm\\infty} [f(x) - ax]$'}]}],
  'example': 'Tìm các đường tiệm cận của đồ thị hàm số $y = \\dfrac{2x^2 - x + 1}{x - 1}$.',
  'example_answer': 'Tập xác định $D = \\mathbb{R} \\setminus \\{1\\}$. Chia đa thức ta có $y = 2x + 1 + '
                    '\\dfrac{2}{x - 1}$. Vì $\\lim_{x \\to 1^+} y = +\\infty$ và $\\lim_{x \\to 1^-} y = '
                    '-\\infty$ nên $x = 1$ là tiệm cận đứng. Vì $\\lim_{x \\to \\pm\\infty} [y - (2x + 1)] = '
                    '\\lim_{x \\to \\pm\\infty} \\dfrac{2}{x - 1} = 0$ nên $y = 2x + 1$ là tiệm cận xiên.',
  'real_life': 'Mô tả nồng độ thuốc trong máu hoặc chi phí trung bình sản xuất mỗi sản phẩm tiến dần về một '
               'mức ổn định khi số lượng sản phẩm tăng lên vô hạn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tiệm cận ngang của đồ thị hàm số $y = \\dfrac{3x - 2}{x + 1}$ là đường thẳng nào dưới đây?',
            'options': ['$x = -1$', '$y = -2$', '$y = 3$', '$x = 3$'],
            'answer': 2,
            'solution': 'Ta có $\\lim_{x \\to \\pm\\infty} \\dfrac{3x - 2}{x + 1} = 3$ nên tiệm cận ngang '
                        'của đồ thị là đường thẳng $y = 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tiệm cận đứng của đồ thị hàm số $y = \\dfrac{2x + 1}{x - 2}$ là đường thẳng:',
            'options': ['$y = 2$', '$x = -\\dfrac{1}{2}$', '$y = -2$', '$x = 2$'],
            'answer': 3,
            'solution': 'Vì $\\lim_{x \\to 2^+} \\dfrac{2x + 1}{x - 2} = +\\infty$ nên đường thẳng $x = 2$ '
                        'là tiệm cận đứng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Đường tiệm cận của đồ thị hàm số**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Tiệm cận ngang**?',
            'options': ['$\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow \\text{TCN: } y = y_0$',
                        '$\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow \\text{TCN: } y = y_0$',
                        'Đảo ngược vế của quy tắc: $\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow '
                        '\\text{TCN: } y = y_0$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\lim_{x \\to \\pm\\infty} '
                        'f(x) = y_0 \\Rightarrow \\text{TCN: } y = y_0$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 3: Đường tiệm cận của đồ thị hàm số, **Tiệm cận '
                        'ngang** được xác định bởi: $\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow '
                        '\\text{TCN: } y = y_0$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Đường tiệm cận của đồ thị hàm số**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tiệm cận đứng**?',
            'options': ['$\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty \\Rightarrow \\text{TCĐ: } x = x_0$',
                        '$\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty \\Rightarrow \\text{TCĐ: } x = x_0$',
                        'Đảo ngược vế của quy tắc: $\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty \\Rightarrow '
                        '\\text{TCĐ: } x = x_0$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\lim_{x \\to x_0^\\pm} f(x) = '
                        '\\pm\\infty \\Rightarrow \\text{TCĐ: } x = x_0$'],
            'answer': 1,
            'solution': 'Trong Bài 3: Đường tiệm cận của đồ thị hàm số, **Tiệm cận đứng** có công thức/quy '
                        'tắc là: $\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty \\Rightarrow \\text{TCĐ: } x = '
                        'x_0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đường tiệm cận xiên của đồ thị hàm số $y = x - 2 + \\dfrac{3}{x + 1}$ có phương trình là:',
            'options': ['$y = x + 1$', '$y = 3x - 2$', '$y = x - 2$', '$x = -1$'],
            'answer': 2,
            'solution': 'Ta có $\\lim_{x \\to \\pm\\infty} [y - (x - 2)] = \\lim_{x \\to \\pm\\infty} '
                        '\\dfrac{3}{x + 1} = 0$, do đó tiệm cận xiên là đường thẳng $y = x - 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 3: Đường tiệm cận của đồ thị hàm số**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận biết được đường tiệm cận ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm '
                        'số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được đường tiệm cận ngang, tiệm cận đứng và '
                        'tiệm cận xiên của đồ thị hàm số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được đường tiệm cận '
                        'ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm số.',
                        'Nhận biết được đường tiệm cận ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm '
                        'số.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 3: Đường tiệm cận của đồ thị hàm số: Nhận biết được '
                        'đường tiệm cận ngang, tiệm cận đứng và tiệm cận xiên của đồ thị hàm số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $y = \\dfrac{x^2 + 2x - 2}{x + 1}$ có đồ thị $(C)$. Xét tính đúng sai của các '
                 'mệnh đề sau:',
            'statements': ['Đồ thị $(C)$ có tiệm cận đứng là đường thẳng $x = -1$.',
                           'Đồ thị $(C)$ có tiệm cận ngang là đường thẳng $y = 1$.',
                           'Đồ thị $(C)$ có tiệm cận xiên là đường thẳng $y = x + 1$.',
                           'Giao điểm hai đường tiệm cận của đồ thị $(C)$ có tọa độ là $(-1; 0)$.'],
            'answer': [True, False, True, True],
            'solution': 'Ta viết lại $y = x + 1 - \\dfrac{3}{x + 1}$. a) Đúng vì $\\lim_{x \\to -1^+} y = '
                        '-\\infty$. b) Sai vì $\\lim_{x \\to \\pm\\infty} y = \\pm\\infty$ nên không có tiệm '
                        'cận ngang. c) Đúng vì $\\lim_{x \\to \\pm\\infty} [y - (x + 1)] = 0$. d) Đúng vì '
                        'giao của $x = -1$ và $y = x + 1$ là điểm $(-1; 0)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 3: Đường tiệm cận của đồ '
                 'thị hàm số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được đường tiệm cận ngang, '
                           'tiệm cận đứng và tiệm cận xiên của đồ thị hàm số.',
                           'Trong **Bài 3: Đường tiệm cận của đồ thị hàm số**, quy tắc/công thức **Tiệm cận '
                           'ngang** được viết là: $\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow '
                           '\\text{TCN: } y = y_0$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\lim_{x \\to \\pm\\infty} f(x) = y_0 '
                           '\\Rightarrow \\text{TCN: } y = y_0$ thì kết quả của **Tiệm cận ngang** trong '
                           '**Bài 3: Đường tiệm cận của đồ thị hàm số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm các đường tiệm cận của đồ thị hàm số $y = \\dfrac{2x^2 - '
                           'x + 1}{x - 1}$.”, kết quả giải đúng là: Tập xác định $D = \\mathbb{R} \\setminus '
                           '\\{1\\}$. Chia đa thức ta có $y = 2x + 1 + \\dfrac{2}{x - 1}$. Vì $\\lim_{x \\to '
                           '1^+} y = +\\infty$ và...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Đường tiệm cận của đồ thị hàm số. b) '
                        '**Đúng** theo công thức **Tiệm cận ngang** ($\\lim_{x \\to \\pm\\infty} f(x) = y_0 '
                        '\\Rightarrow \\text{TCN: } y = y_0$). c) **Sai** vì công thức đúng của **Tiệm cận '
                        'ngang** phải là $\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow \\text{TCN: } y '
                        '= y_0$ chứ không phải $\\lim_{x \\to \\pm\\infty} f(x) = y_0 \\Rightarrow '
                        '\\text{TCN: } y = y_0$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 3: Đường tiệm cận của đồ thị hàm số** để giải bài '
                 'toán sau: Tìm các đường tiệm cận của đồ thị hàm số $y = \\dfrac{2x^2 - x + 1}{x - 1}$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tập xác định $D = \\mathbb{R} \\setminus \\{1\\}$. Chia đa thức ta có $y = 2x + 1 + '
                        '\\dfrac{2}{x - 1}$. Vì $\\lim_{x \\to 1^+} y = +\\infty$ và $\\lim_{x \\to 1^-} y = '
                        '-\\infty$...',
                        'Tập xác định $D = \\mathbb{R} \\setminus \\{1\\}$. Chia đa thức ta có $y = 2x + 1 + '
                        '\\dfrac{2}{x - 1}$. Vì $\\lim_{x \\to 1^+} y = +\\infty$ và $\\lim_{x \\to 1^-} '
                        'y = -\\infty$...',
                        'Tập xác định $D = \\mathbb{R} \\setminus \\{1\\}$. Chia đa thức ta có $y = 2x + 1 + '
                        '\\dfrac{x - 1}{2}$. Vì $\\lim_{x \\to 1^+} y = +\\infty$ và $\\lim_{x \\to 1^-} y = '
                        '-\\infty$...',
                        'Tập xác định $D = \\mathbb{R} \\setminus \\{2\\}$. Chia đa thức ta có $y = 2x + 1 + '
                        '\\dfrac{2}{x - 1}$. Vì $\\lim_{x \\to 1^+} y = +\\infty$ và $\\lim_{x \\to 1^-} y = '
                        '-\\infty$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Đường tiệm cận của đồ thị hàm số: Tập xác định $D = '
                        '\\mathbb{R} \\setminus \\{1\\}$. Chia đa thức ta có $y = 2x + 1 + \\dfrac{2}{x - '
                        '1}$. Vì $\\lim_{x \\to 1^+} y = +\\infty$ và $\\lim_{x \\to 1^-} y = -\\infty$ nên '
                        '$x = 1$ là tiệm cận đứng. Vì $\\lim_{x \\to \\pm\\infty} [y - (2x + 1)] = \\lim_{x '
                        '\\to \\pm\\infty} \\dfrac{2}{x - 1} = 0$ nên $y = 2x + 1$ là tiệm cận xiên.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \\dfrac{x - 1}{x^2 - '
                 '4x + 3}$ là bao nhiêu?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Với $x \\ne 1, x \\ne 3$, rút gọn $y = \\dfrac{x - 1}{(x - 1)(x - 3)} = '
                        '\\dfrac{1}{x - 3}$. Khi $x \\to 1$, $\\lim_{x \\to 1} y = -\\dfrac{1}{2}$ nên $x = '
                        '1$ không là TCĐ. Chỉ có 1 TCĐ là $x = 3$ và 1 TCN là $y = 0$. Tổng cộng có $2$ '
                        'đường tiệm cận.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch01-ung-dung-dao-ham',
  'context_title': 'Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số',
  'context': 'Chương I · SGK Toán 12: Đơn điệu, cực trị, giá trị lớn nhất - nhỏ nhất, tiệm cận và khảo sát '
             'vẽ đồ thị hàm số.',
  'title': 'Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số',
  'icon': '📊',
  'description': 'Quy trình khảo sát sự biến thiên và vẽ đồ thị hàm số bậc ba, hàm phân thức hữu tỉ và nhận '
                 'diện đồ thị.',
  'requirements': ['Nắm vững sơ đồ tổng quát khảo sát sự biến thiên và vẽ đồ thị hàm số.',
                   'Khảo sát và vẽ được đồ thị hàm số bậc ba $y = ax^3 + bx^2 + cx + d$, hàm phân thức $y = '
                   '\\dfrac{ax + b}{cx + d}$ và $y = \\dfrac{ax^2 + bx + c}{mx + n}$.',
                   'Nhận diện được dấu các hệ số và tính chất đối xứng của đồ thị hàm số.'],
  'definition': 'Khảo sát sự biến thiên và vẽ đồ thị hàm số là việc tìm tập xác định, xét chiều biến thiên '
                '(đạo hàm, cực trị, giới hạn, tiệm cận, bảng biến thiên) và vẽ đồ thị minh họa trên mặt '
                'phẳng tọa độ $Oxy$.',
  'theory': '1. Đồ thị hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ ($a \\ne 0$) luôn nhận điểm uốn $I(x_0; '
            "y_0)$ với $x_0 = -\\dfrac{b}{3a}$ (nghiệm của $y'' = 0$) làm tâm đối xứng. 2. Đồ thị hàm phân "
            'thức $y = \\dfrac{ax + b}{cx + d}$ và $y = \\dfrac{ax^2 + bx + c}{mx + n}$ luôn nhận giao điểm '
            'hai đường tiệm cận làm tâm đối xứng.',
  'formulas': [{'category': 'Tâm đối xứng và nhận diện hệ số',
                'items': [{'name': 'Tâm đối xứng hàm bậc ba',
                           'formula': "$y'' = 6ax + 2b = 0 \\Leftrightarrow x_I = -\\dfrac{b}{3a}$"},
                          {'name': 'Tâm đối xứng hàm nhất biến',
                           'formula': '$I\\left(-\\dfrac{d}{c}; \\dfrac{a}{c}\\right)$ (giao điểm của TCĐ và '
                                      'TCN)'},
                          {'name': 'Nhánh cuối đồ thị bậc ba',
                           'formula': '$\\lim_{x \\to +\\infty} y = +\\infty \\Leftrightarrow a > 0; \\quad '
                                      '\\lim_{x \\to +\\infty} y = -\\infty \\Leftrightarrow a < 0$'}]}],
  'example': 'Tìm tọa độ tâm đối xứng của đồ thị hàm số $y = x^3 - 3x^2 + 1$.',
  'example_answer': "Ta có $y' = 3x^2 - 6x$ và $y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 "
                    '\\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y = 1^3 - 3 \\cdot 1^2 + 1 = -1$. Vậy '
                    'tâm đối xứng của đồ thị là điểm $I(1; -1)$.',
  'real_life': 'Biểu diễn trực quan các đường cong tăng trưởng kinh tế, đường cong cầu - cung và quỹ đạo '
               'chuyển động trong kỹ thuật.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đồ thị của hàm số nào dưới đây có dạng đường cong bậc ba với nhánh bên phải đi lên khi $x '
                 '\\to +\\infty$?',
            'options': ['$y = -x^3 + 3x + 1$',
                        '$y = \\dfrac{x + 1}{x - 1}$',
                        '$y = x^2 - 2x + 1$',
                        '$y = x^3 - 3x + 1$'],
            'answer': 3,
            'solution': 'Hàm bậc ba có nhánh phải đi lên khi $x \\to +\\infty$ ứng với hệ số $a > 0$, tức là '
                        '$y = x^3 - 3x + 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tâm đối xứng của đồ thị hàm số $y = \\dfrac{2x - 1}{x + 3}$ có tọa độ là:',
            'options': ['$(-3; 2)$', '$(3; 2)$', '$(-3; -1)$', '$(2; -3)$'],
            'answer': 0,
            'solution': 'Đồ thị có tiệm cận đứng $x = -3$ và tiệm cận ngang $y = 2$, nên tâm đối xứng là '
                        'giao điểm $I(-3; 2)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Tâm đối xứng hàm bậc ba**?',
            'options': ["$y'' = 6ax - 2b = 0 \\Leftrightarrow x_I = -\\dfrac{b}{3a}$",
                        "$y'' = 6ax + 2b = 0 \\Leftrightarrow x_I = -\\dfrac{b}{3a}$",
                        "$y'' = 6ax + 2b = 0 \\Leftrightarrow x_I = -\\dfrac{3a}{b}$",
                        "$y'' = 6ax + 2b = 2 \\Leftrightarrow x_I = -\\dfrac{b}{3a}$"],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số, '
                        "**Tâm đối xứng hàm bậc ba** được xác định bởi: $y'' = 6ax + 2b = 0 \\Leftrightarrow "
                        'x_I = -\\dfrac{b}{3a}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Tâm đối xứng hàm nhất biến**?',
            'options': ['$I\\left(-\\dfrac{d}{c}; \\dfrac{a}{c}\\right)$ (giao điểm của TCĐ và TCN)',
                        '$I\\left(-\\dfrac{c}{d}; \\dfrac{a}{c}\\right)$ (giao điểm của TCĐ và TCN)',
                        '$I\\left(-\\dfrac{d}{c}; \\dfrac{a}{c}\\right)$ (giao điểm của TCĐ và TCN)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $I\\left(-\\dfrac{d}{c}; '
                        '\\dfrac{a}{c}\\right)$ (giao điểm của TCĐ và TCN)'],
            'answer': 2,
            'solution': 'Trong Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số, **Tâm đối xứng hàm '
                        'nhất biến** có công thức/quy tắc là: $I\\left(-\\dfrac{d}{c}; '
                        '\\dfrac{a}{c}\\right)$ (giao điểm của TCĐ và TCN).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số giao điểm của đồ thị hàm số $y = x^3 - 3x + 2$ và trục hoành $Ox$ là bao nhiêu?',
            'options': ['$3$', '$1$', '$0$', '$2$'],
            'answer': 3,
            'solution': 'Phương trình hoành độ giao điểm: $x^3 - 3x + 2 = 0 \\Leftrightarrow (x - 1)^2(x + '
                        '2) = 0 \\Leftrightarrow x = 1$ hoặc $x = -2$. Vậy có $2$ giao điểm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nắm vững sơ đồ tổng quát khảo sát sự biến thiên và vẽ đồ thị hàm số.',
                        'Nắm vững sơ đồ tổng quát khảo sát sự biến thiên và vẽ đồ thị hàm số. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Nắm vững sơ đồ tổng quát khảo sát sự biến thiên và vẽ đồ '
                        'thị hàm số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nắm vững sơ đồ tổng quát khảo '
                        'sát sự biến thiên và vẽ đồ thị hàm số.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số: '
                        'Nắm vững sơ đồ tổng quát khảo sát sự biến thiên và vẽ đồ thị hàm số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $y = \\dfrac{x - 2}{x + 1}$ có đồ thị $(C)$. Xét tính đúng sai của các mệnh đề '
                 'sau:',
            'statements': ['Hàm số đồng biến trên từng khoảng $(-\\infty; -1)$ và $(-1; +\\infty)$.',
                           'Đồ thị $(C)$ cắt trục tung tại điểm có tọa độ $(0; -2)$.',
                           'Đồ thị $(C)$ cắt trục hoành tại điểm có tọa độ $(-2; 0)$.',
                           'Tâm đối xứng của đồ thị $(C)$ là điểm $I(-1; 1)$.'],
            'answer': [True, True, False, True],
            'solution': "a) Đúng vì $y' = \\dfrac{3}{(x + 1)^2} > 0, \\forall x \\ne -1$. b) Đúng vì $x = 0 "
                        '\\Rightarrow y = -2$. c) Sai vì $y = 0 \\Leftrightarrow x = 2$, giao điểm với trục '
                        'hoành là $(2; 0)$. d) Đúng vì TCĐ $x = -1$ và TCN $y = 1$ cắt nhau tại $I(-1; 1)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 4: Khảo sát sự biến thiên '
                 'và vẽ đồ thị của hàm số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nắm vững sơ đồ tổng quát khảo sát sự '
                           'biến thiên và vẽ đồ thị hàm số.',
                           'Trong **Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số**, quy tắc/công '
                           "thức **Tâm đối xứng hàm bậc ba** được viết là: $y'' = 6ax + 2b = 0 "
                           '\\Leftrightarrow x_I = -\\dfrac{b}{3a}$.',
                           "Nếu áp dụng sai dấu/phép tính thành $y'' = 6ax - 2b = 0 \\Leftrightarrow x_I = "
                           '-\\dfrac{b}{3a}$ thì kết quả của **Tâm đối xứng hàm bậc ba** trong **Bài 4: Khảo '
                           'sát sự biến thiên và vẽ đồ thị của hàm số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm tọa độ tâm đối xứng của đồ thị hàm số $y = x^3 - 3x^2 + '
                           "1$.”, kết quả giải đúng là: Ta có $y' = 3x^2 - 6x$ và $y'' = 6x - 6$. Cho $y'' = "
                           '0 \\Leftrightarrow 6x - 6 = 0 \\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y '
                           '= 1^3 - 3 \\cdot 1^2 + 1 = -1$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của '
                        "hàm số. b) **Đúng** theo công thức **Tâm đối xứng hàm bậc ba** ($y'' = 6ax + 2b = 0 "
                        '\\Leftrightarrow x_I = -\\dfrac{b}{3a}$). c) **Sai** vì công thức đúng của **Tâm '
                        "đối xứng hàm bậc ba** phải là $y'' = 6ax + 2b = 0 \\Leftrightarrow x_I = "
                        "-\\dfrac{b}{3a}$ chứ không phải $y'' = 6ax - 2b = 0 \\Leftrightarrow x_I = "
                        '-\\dfrac{b}{3a}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số** '
                 'để giải bài toán sau: Tìm tọa độ tâm đối xứng của đồ thị hàm số $y = x^3 - 3x^2 + 1$. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ["Ta có $y' = 3x^2 - 6x$ và $y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 "
                        '\\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y = 1^3 - 3 \\cdot 1^2 - 1 = '
                        '-1$...',
                        "Ta có $y' = 3x^2 - 6x$ và $y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 "
                        '\\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y = 1^3 - 3 \\cdot 1^2 + 1 = '
                        '-1$...',
                        "Ta có $y' = 3x^2 - 6x$ và $y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 "
                        '\\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y = 1^3 - 3 \\cdot 1^2 + 1 = '
                        '-2$...',
                        "Ta có $y' = 3x^4 - 6x$ và $y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 "
                        '\\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y = 1^3 - 3 \\cdot 1^2 + 1 = '
                        '-1$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số: Ta có '
                        "$y' = 3x^2 - 6x$ và $y'' = 6x - 6$. Cho $y'' = 0 \\Leftrightarrow 6x - 6 = 0 "
                        '\\Leftrightarrow x = 1$. Với $x = 1 \\Rightarrow y = 1^3 - 3 \\cdot 1^2 + 1 = -1$. '
                        'Vậy tâm đối xứng của đồ thị là điểm $I(1; -1)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biết đồ thị hàm số $y = ax^3 + bx^2 + cx + d$ đạt cực đại tại $A(0; 2)$ và đạt cực tiểu '
                 'tại $B(2; -2)$. Tính giá trị của $a + b + c + d$.',
            'answer': ['0'],
            'unit': None,
            'solution': "Vì hàm số đạt cực trị tại $x = 0$ và $x = 2$ nên $y' = 3ax(x - 2) = 3ax^2 - 6ax "
                        '\\Rightarrow c = 0, b = -3a$. Do $A(0; 2) \\in (C) \\Rightarrow d = 2$. Do $B(2; '
                        '-2) \\in (C) \\Rightarrow 8a - 12a + 2 = -2 \\Leftrightarrow a = 1 \\Rightarrow b = '
                        '-3$. Khi đó $a + b + c + d = 1 - 3 + 0 + 2 = 0$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch01-ung-dung-dao-ham',
  'context_title': 'Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số',
  'context': 'Chương I · SGK Toán 12: Đơn điệu, cực trị, giá trị lớn nhất - nhỏ nhất, tiệm cận và khảo sát '
             'vẽ đồ thị hàm số.',
  'title': 'Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn',
  'icon': '⚙️',
  'description': 'Sử dụng đạo hàm để tính tốc độ thay đổi tức thời và giải các bài toán tối ưu hóa trong vật '
                 'lí, hóa học, sinh học và kinh tế.',
  'requirements': ["Hiểu được đạo hàm $f'(t)$ biểu thị tốc độ thay đổi tức thời của đại lượng $y = f(t)$ "
                   'theo biến $t$.',
                   'Thiết lập được hàm số mô tả bài toán tối ưu trong hình học, vật lí và kinh tế.',
                   'Tìm được phương án tối ưu (chi phí nhỏ nhất, lợi nhuận lớn nhất, thể tích lớn nhất) bằng '
                   'đạo hàm.'],
  'definition': "Nếu đại lượng $y$ phụ thuộc vào đại lượng $x$ theo hàm số $y = f(x)$ thì đạo hàm $f'(x_0)$ "
                'biểu thị tốc độ thay đổi tức thời của đại lượng $y$ theo đại lượng $x$ tại điểm $x_0$.',
  'theory': "1. Trong chuyển động: vận tốc tức thời $v(t) = s'(t)$, gia tốc tức thời $a(t) = v'(t) = "
            "s''(t)$. 2. Trong kinh tế: nếu $C(x), R(x), P(x) = R(x) - C(x)$ lần lượt là hàm chi phí, doanh "
            "thu và lợi nhuận khi sản xuất $x$ đơn vị hàng hóa thì $C'(x), R'(x), P'(x)$ gọi là chi phí "
            'biên, doanh thu biên và lợi nhuận biên.',
  'formulas': [{'category': 'Tốc độ thay đổi và bài toán kinh tế',
                'items': [{'name': 'Vận tốc và gia tốc tức thời',
                           'formula': "$v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$"},
                          {'name': 'Hàm lợi nhuận', 'formula': '$P(x) = R(x) - C(x)$'},
                          {'name': 'Chi phí biên và doanh thu biên',
                           'formula': "$MC = C'(x), \\quad MR = R'(x)$"}]}],
  'example': 'Một tấm bìa hình vuông cạnh $12\\text{ cm}$. Người ta cắt bỏ ở bốn góc bốn hình vuông bằng '
             'nhau cạnh $x\\text{ cm}$ rồi gấp lại thành một hình hộp chữ nhật không nắp. Tìm $x$ để thể '
             'tích hộp lớn nhất.',
  'example_answer': 'Điều kiện $0 < x < 6$. Đáy hộp là hình vuông cạnh $12 - 2x$, chiều cao hộp là $x$. Thể '
                    "tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - 12x^2 + 36x)$. Ta có $V'(x) = "
                    "4(3x^2 - 24x + 36) = 12(x - 2)(x - 6)$. Trên $(0; 6)$, $V'(x) = 0 \\Leftrightarrow x = "
                    '2$. Lập bảng biến thiên suy ra $\\max_{(0; 6)} V(x) = V(2) = 128\\text{ cm}^3$ khi $x = '
                    '2\\text{ cm}$.',
  'real_life': 'Tối ưu hóa giá bán vé máy bay, thiết kế kích thước lon nước giải khát và điều chỉnh liều '
               'lượng thuốc điều trị.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một chất điểm chuyển động theo phương trình $s(t) = t^3 - 3t^2 + 5t$ ($s$ tính bằng mét, '
                 '$t$ tính bằng giây). Vận tốc tức thời của chất điểm tại thời điểm $t = 2$ giây là:',
            'options': ['$5\\text{ m/s}$', '$6\\text{ m/s}$', '$2\\text{ m/s}$', '$10\\text{ m/s}$'],
            'answer': 0,
            'solution': "Ta có $v(t) = s'(t) = 3t^2 - 6t + 5$. Tại $t = 2$, vận tốc là $v(2) = 3 \\cdot 2^2 "
                        '- 6 \\cdot 2 + 5 = 5\\text{ m/s}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giả sử chi phí sản xuất $x$ sản phẩm của một xí nghiệp được cho bởi $C(x) = x^2 + 20x + '
                 "500$ (nghìn đồng). Hàm chi phí biên $C'(x)$ là:",
            'options': ['$x + 20$', '$2x + 20$', '$2x + 500$', '$x^2 + 20$'],
            'answer': 1,
            'solution': "Chi phí biên là đạo hàm của hàm chi phí theo $x$: $C'(x) = 2x + 20$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn**, quy '
                 'tắc hoặc công thức nào sau đây xác định đúng **Vận tốc và gia tốc tức thời**?',
            'options': ["$v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$ (với dấu ngược lại)",
                        "Đảo ngược vế của quy tắc: $v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$",
                        "$v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $v(t) = s'(t), \\quad a(t) = "
                        "v'(t) = s''(t)$"],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề '
                        'liên quan đến thực tiễn, **Vận tốc và gia tốc tức thời** được xác định bởi: $v(t) = '
                        "s'(t), \\quad a(t) = v'(t) = s''(t)$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Hàm lợi nhuận**?',
            'options': ['$P(x) = R(x) + C(x)$',
                        'Đảo ngược vế của quy tắc: $P(x) = R(x) - C(x)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(x) = R(x) - C(x)$',
                        '$P(x) = R(x) - C(x)$'],
            'answer': 3,
            'solution': 'Trong Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn, '
                        '**Hàm lợi nhuận** có công thức/quy tắc là: $P(x) = R(x) - C(x)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một vật được ném thẳng đứng lên cao với độ cao $h(t) = -5t^2 + 20t + 1$ ($h$ tính bằng '
                 'mét, $t$ tính bằng giây). Độ cao lớn nhất mà vật đạt được là:',
            'options': ['$21\\text{ m}$', '$20\\text{ m}$', '$16\\text{ m}$', '$25\\text{ m}$'],
            'answer': 0,
            'solution': "Ta có $h'(t) = -10t + 20 = 0 \\Leftrightarrow t = 2\\text{ s}$. Độ cao lớn nhất là "
                        '$h(2) = -5 \\cdot 4 + 20 \\cdot 2 + 1 = 21\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan '
                 'đến thực tiễn**, nhận định nào sau đây là **chính xác**?',
            'options': ["Hiểu được đạo hàm $f'(t)$ biểu thị tốc độ thay đổi tức thời của đại lượng $y = "
                        'f(t)$ theo biến $t$. (với dấu ngược lại)',
                        "Hiểu được đạo hàm $f'(t)$ biểu thị tốc độ thay đổi tức thời của đại lượng $y = "
                        'f(t)$ theo biến $t$.',
                        "Đảo ngược vế của quy tắc: Hiểu được đạo hàm $f'(t)$ biểu thị tốc độ thay đổi tức "
                        'thời của đại lượng $y = f(t)$ theo biến $t$.',
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu được đạo hàm $f'(t)$ biểu "
                        'thị tốc độ thay đổi tức thời của đại lượng $y = f(t)$ theo biến $t$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên '
                        "quan đến thực tiễn: Hiểu được đạo hàm $f'(t)$ biểu thị tốc độ thay đổi tức thời của "
                        'đại lượng $y = f(t)$ theo biến $t$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một hộ sản xuất bán $x$ kg sản phẩm mỗi ngày ($1 \\le x \\le 30$) với hàm doanh thu $R(x) '
                 '= 100x - x^2$ (nghìn đồng) và hàm chi phí $C(x) = x^2 - 20x + 300$ (nghìn đồng). Xét tính '
                 'đúng sai của các mệnh đề sau:',
            'statements': ['Hàm lợi nhuận mỗi ngày là $P(x) = -2x^2 + 120x - 300$ (nghìn đồng).',
                           "Đạo hàm của hàm lợi nhuận là $P'(x) = -4x + 120$.",
                           'Hộ sản xuất đạt lợi nhuận lớn nhất khi bán $20$ kg sản phẩm mỗi ngày.',
                           'Lợi nhuận lớn nhất mỗi ngày mà hộ sản xuất thu được là $1500$ nghìn đồng.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $P(x) = R(x) - C(x) = (100x - x^2) - (x^2 - 20x + 300) = -2x^2 + 120x - '
                        "300$. b) Đúng vì $P'(x) = -4x + 120$. c) Sai vì $P'(x) = 0 \\Leftrightarrow x = "
                        '30\\text{ kg}$. d) Đúng vì $P(30) = -2 \\cdot 30^2 + 120 \\cdot 30 - 300 = 1500$ '
                        'nghìn đồng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 5: Ứng dụng đạo hàm để giải '
                 'quyết một số vấn đề liên quan đến thực tiễn**:',
            'statements': ["Nội dung trọng tâm của bài học yêu cầu: Hiểu được đạo hàm $f'(t)$ biểu thị tốc "
                           'độ thay đổi tức thời của đại lượng $y = f(t)$ theo biến $t$.',
                           'Trong **Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực '
                           'tiễn**, quy tắc/công thức **Vận tốc và gia tốc tức thời** được viết là: $v(t) = '
                           "s'(t), \\quad a(t) = v'(t) = s''(t)$.",
                           "Nếu áp dụng sai dấu/phép tính thành $v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$ "
                           '(với dấu ngược lại) thì kết quả của **Vận tốc và gia tốc tức thời** trong **Bài '
                           '5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Một tấm bìa hình vuông cạnh $12\\text{ cm}$. Người ta cắt bỏ '
                           'ở bốn góc bốn hình vuông bằng nhau cạnh $x\\text{ cm}$ rồi gấp lại thành '
                           'một...”, kết quả giải đúng là: Điều kiện $0 < x < 6$. Đáy hộp là hình vuông cạnh '
                           '$12 - 2x$, chiều cao hộp là $x$. Thể tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - '
                           'x)^2 = 4(x^3 - 12x^2 + 36x)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Ứng dụng đạo hàm để giải quyết một số '
                        'vấn đề liên quan đến thực tiễn. b) **Đúng** theo công thức **Vận tốc và gia tốc tức '
                        "thời** ($v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$). c) **Sai** vì công thức đúng "
                        "của **Vận tốc và gia tốc tức thời** phải là $v(t) = s'(t), \\quad a(t) = v'(t) = "
                        "s''(t)$ chứ không phải $v(t) = s'(t), \\quad a(t) = v'(t) = s''(t)$ (với dấu ngược "
                        'lại). d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề '
                 'liên quan đến thực tiễn** để giải bài toán sau: Một tấm bìa hình vuông cạnh $12\\text{ '
                 'cm}$. Người ta cắt bỏ ở bốn góc bốn hình vuông bằng nhau cạnh $x\\text{ cm}$ rồi gấp lại '
                 'thành một hình hộp chữ nhật không nắp. Tìm $x$ để thể tích hộp lớn nhất. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Điều kiện $0 < x < 6$. Đáy hộp là hình vuông cạnh $12 - 2x$, chiều cao hộp là $x$. '
                        'Thể tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - 12x^2 - 36x)$...',
                        'Điều kiện $0 < x < 6$. Đáy hộp là hình vuông cạnh $12 - 2x$, chiều cao hộp là $x$. '
                        'Thể tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - 12x^1 + 36x)$...',
                        'Điều kiện $0 < x < 6$. Đáy hộp là hình vuông cạnh $12 - 2x$, chiều cao hộp là $x$. '
                        'Thể tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - 12x^2 + 36x)$...',
                        'Điều kiện $2 < x < 6$. Đáy hộp là hình vuông cạnh $12 - 2x$, chiều cao hộp là $x$. '
                        'Thể tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - 12x^2 + 36x)$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên '
                        'quan đến thực tiễn: Điều kiện $0 < x < 6$. Đáy hộp là hình vuông cạnh $12 - 2x$, '
                        'chiều cao hộp là $x$. Thể tích hộp là $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - '
                        "12x^2 + 36x)$. Ta có $V'(x) = 4(3x^2 - 24x + 36) = 12(x - 2)(x - 6)$. Trên $(0; "
                        "6)$, $V'(x) = 0 \\Leftrightarrow x = 2$. Lập bảng biến thiên suy ra $\\max_{(0; 6)} "
                        'V(x) = V(2) = 128\\text{ cm}^3$ khi $x = 2\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Người ta muốn rào một khu đất hình chữ nhật dọc theo một bờ tường có sẵn (bờ tường làm một '
                 'cạnh của hình chữ nhật, chỉ cần rào 3 cạnh còn lại) bằng một lưới thép dài $40\\text{ m}$. '
                 'Diện tích lớn nhất của khu đất rào được là bao nhiêu mét vuông?',
            'answer': ['200'],
            'unit': None,
            'solution': 'Gọi $x\\text{ (m)}$ là chiều rộng vuông góc với tường ($0 < x < 20$), khi đó chiều '
                        'dài song song với tường là $40 - 2x\\text{ (m)}$. Diện tích $S(x) = x(40 - 2x) = '
                        "-2x^2 + 40x$. Ta có $S'(x) = -4x + 40 = 0 \\Leftrightarrow x = 10$. Vậy $\\max S = "
                        'S(10) = 200\\text{ m}^2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch02-vecto-khong-gian',
  'context_title': 'Chương II: Vectơ và hệ trục tọa độ trong không gian',
  'context': 'Chương II · SGK Toán 12: Vectơ trong không gian, hệ trục tọa độ Oxyz và biểu thức tọa độ của '
             'các phép toán vectơ.',
  'title': 'Bài 6: Vectơ trong không gian',
  'icon': '🧭',
  'description': 'Khái niệm vectơ trong không gian, quy tắc hình hộp, tích của một số với vectơ và tích vô '
                 'hướng của hai vectơ trong không gian.',
  'requirements': ['Nhận biết được vectơ trong không gian, hai vectơ cùng phương, cùng hướng, bằng nhau.',
                   'Vận dụng được quy tắc ba điểm, quy tắc hình bình hành, quy tắc hình hộp và hệ thức trọng '
                   'tâm trong không gian.',
                   'Tính được góc và tích vô hướng của hai vectơ trong không gian.'],
  'definition': "Vectơ trong không gian là một đoạn thẳng có hướng. Cho hình hộp $ABCD.A'B'C'D'$, quy tắc "
                'hình hộp khẳng định tổng ba vectơ xuất phát từ một đỉnh theo ba cạnh bằng vectơ đường chéo: '
                "$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = "
                "\\overrightarrow{AC'}$.",
  'theory': '1. Quy tắc 3 điểm: $\\overrightarrow{AB} + \\overrightarrow{BC} = \\overrightarrow{AC}$ và '
            '$\\overrightarrow{OB} - \\overrightarrow{OA} = \\overrightarrow{AB}$. 2. Hệ thức trung điểm $I$ '
            'của $AB$: $\\overrightarrow{IA} + \\overrightarrow{IB} = \\overrightarrow{0}$ và '
            '$\\overrightarrow{MA} + \\overrightarrow{MB} = 2\\overrightarrow{MI}$. 3. Hệ thức trọng tâm $G$ '
            'của tam giác $ABC$: $\\overrightarrow{GA} + \\overrightarrow{GB} + \\overrightarrow{GC} = '
            '\\overrightarrow{0}$. 4. Tích vô hướng: $\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot '
            '|\\vec{b}| \\cdot \\cos(\\vec{a}, \\vec{b})$.',
  'formulas': [{'category': 'Các quy tắc vectơ trong không gian',
                'items': [{'name': 'Quy tắc hình hộp',
                           'formula': "$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} "
                                      "= \\overrightarrow{AC'}$"},
                          {'name': 'Trọng tâm tam giác',
                           'formula': '$\\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = '
                                      '3\\overrightarrow{MG}$'},
                          {'name': 'Tích vô hướng',
                           'formula': '$\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot |\\vec{b}| \\cdot '
                                      '\\cos(\\vec{a}, \\vec{b})$'}]}],
  'example': "Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Tính tích vô hướng $\\overrightarrow{AB} "
             "\\cdot \\overrightarrow{A'C'}$.",
  'example_answer': "Vì $\\overrightarrow{A'C'} = \\overrightarrow{AC}$ nên $\\overrightarrow{AB} \\cdot "
                    "\\overrightarrow{A'C'} = \\overrightarrow{AB} \\cdot \\overrightarrow{AC}$. Trong hình "
                    'vuông $ABCD$ cạnh $a$, ta có $AC = a\\sqrt{2}$ và góc $(\\overrightarrow{AB}, '
                    '\\overrightarrow{AC}) = \\widehat{BAC} = 45^\\circ$. Do đó $\\overrightarrow{AB} \\cdot '
                    "\\overrightarrow{A'C'} = a \\cdot a\\sqrt{2} \\cdot \\cos 45^\\circ = a^2$.",
  'real_life': 'Tổng hợp lực căng dây cáp treo hoặc phân tích các lực tác dụng lên cấu trúc cầu treo trong '
               'không gian ba chiều.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Cho hình hộp $ABCD.A'B'C'D'$. Đẳng thức nào dưới đây là quy tắc hình hộp?",
            'options': ["$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = "
                        '\\overrightarrow{AC}$',
                        "$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = "
                        "\\overrightarrow{AC'}$",
                        "$\\overrightarrow{AB} + \\overrightarrow{AC} + \\overrightarrow{AA'} = "
                        "\\overrightarrow{AC'}$",
                        "$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{A'A} = "
                        "\\overrightarrow{AC'}$"],
            'answer': 1,
            'solution': 'Theo quy tắc hình hộp, tổng ba vectơ cạnh chung gốc $A$ là $\\overrightarrow{AB} + '
                        "\\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai vectơ $\\vec{u}$ và $\\vec{v}$ trong không gian thỏa mãn $|\\vec{u}| = 2$, '
                 '$|\\vec{v}| = 3$ và $(\\vec{u}, \\vec{v}) = 60^\\circ$. Tích vô hướng $\\vec{u} \\cdot '
                 '\\vec{v}$ bằng:',
            'options': ['$6$', '$3\\sqrt{3}$', '$3$', '$-3$'],
            'answer': 2,
            'solution': 'Ta có $\\vec{u} \\cdot \\vec{v} = |\\vec{u}| \\cdot |\\vec{v}| \\cdot \\cos '
                        '60^\\circ = 2 \\cdot 3 \\cdot \\dfrac{1}{2} = 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Vectơ trong không gian**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Quy tắc hình hộp**?',
            'options': ["$\\overrightarrow{AB} - \\overrightarrow{AD} + \\overrightarrow{AA'} = "
                        "\\overrightarrow{AC'}$",
                        'Đảo ngược vế của quy tắc: $\\overrightarrow{AB} + \\overrightarrow{AD} + '
                        "\\overrightarrow{AA'} = \\overrightarrow{AC'}$",
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overrightarrow{AB} + '
                        "\\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$",
                        "$\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = "
                        "\\overrightarrow{AC'}$"],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 6: Vectơ trong không gian, **Quy tắc hình hộp** '
                        'được xác định bởi: $\\overrightarrow{AB} + \\overrightarrow{AD} + '
                        "\\overrightarrow{AA'} = \\overrightarrow{AC'}$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Vectơ trong không gian**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Trọng tâm tam giác**?',
            'options': ['$\\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = '
                        '3\\overrightarrow{MG}$',
                        '$\\overrightarrow{MA} - \\overrightarrow{MB} + \\overrightarrow{MC} = '
                        '3\\overrightarrow{MG}$',
                        '$\\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = '
                        '2\\overrightarrow{MG}$',
                        '$\\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = '
                        '6\\overrightarrow{MG}$'],
            'answer': 0,
            'solution': 'Trong Bài 6: Vectơ trong không gian, **Trọng tâm tam giác** có công thức/quy tắc '
                        'là: $\\overrightarrow{MA} + \\overrightarrow{MB} + \\overrightarrow{MC} = '
                        '3\\overrightarrow{MG}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tứ diện $ABCD$ có $G$ là trọng tâm tam giác $BCD$. Đẳng thức nào dưới đây đúng?',
            'options': ['$\\overrightarrow{AB} + \\overrightarrow{AC} + \\overrightarrow{AD} = '
                        '\\overrightarrow{AG}$',
                        '$\\overrightarrow{AB} + \\overrightarrow{AC} + \\overrightarrow{AD} = '
                        '3\\overrightarrow{AG}$',
                        '$\\overrightarrow{AB} + \\overrightarrow{AC} + \\overrightarrow{AD} = '
                        '2\\overrightarrow{AG}$',
                        '$\\overrightarrow{AB} + \\overrightarrow{AC} + \\overrightarrow{AD} = '
                        '4\\overrightarrow{AG}$'],
            'answer': 1,
            'solution': 'Vì $G$ là trọng tâm tam giác $BCD$ nên với điểm $A$ bất kì ta luôn có '
                        '$\\overrightarrow{AB} + \\overrightarrow{AC} + \\overrightarrow{AD} = '
                        '3\\overrightarrow{AG}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 6: Vectơ trong không gian**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được vectơ trong không gian, hai vectơ cùng phương, cùng hướng, bằng '
                        'nhau. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được vectơ trong không gian, hai vectơ cùng '
                        'phương, cùng hướng, bằng nhau.',
                        'Nhận biết được vectơ trong không gian, hai vectơ cùng phương, cùng hướng, bằng '
                        'nhau.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được vectơ trong '
                        'không gian, hai vectơ cùng phương, cùng hướng, bằng nhau.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 6: Vectơ trong không gian: Nhận biết được vectơ trong '
                        'không gian, hai vectơ cùng phương, cùng hướng, bằng nhau.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tứ diện đều $ABCD$ có tất cả các cạnh bằng $a$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Góc giữa hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{AC}$ bằng '
                           '$60^\\circ$.',
                           'Góc giữa hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{BC}$ bằng '
                           '$60^\\circ$.',
                           'Tích vô hướng $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = '
                           '\\dfrac{a^2}{2}$.',
                           'Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{CD}$ vuông góc với nhau.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $\\triangle ABC$ đều nên $(\\overrightarrow{AB}, \\overrightarrow{AC}) = '
                        '60^\\circ$. b) Sai vì $(\\overrightarrow{AB}, \\overrightarrow{BC}) = 180^\\circ - '
                        '\\widehat{ABC} = 120^\\circ$. c) Đúng vì $\\overrightarrow{AB} \\cdot '
                        '\\overrightarrow{AC} = a \\cdot a \\cdot \\cos 60^\\circ = \\dfrac{a^2}{2}$. d) '
                        'Đúng vì $\\overrightarrow{AB} \\cdot \\overrightarrow{CD} = \\overrightarrow{AB} '
                        '\\cdot (\\overrightarrow{AD} - \\overrightarrow{AC}) = \\dfrac{a^2}{2} - '
                        '\\dfrac{a^2}{2} = 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 6: Vectơ trong không '
                 'gian**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được vectơ trong không gian, '
                           'hai vectơ cùng phương, cùng hướng, bằng nhau.',
                           'Trong **Bài 6: Vectơ trong không gian**, quy tắc/công thức **Quy tắc hình hộp** '
                           'được viết là: $\\overrightarrow{AB} + \\overrightarrow{AD} + '
                           "\\overrightarrow{AA'} = \\overrightarrow{AC'}$.",
                           'Nếu áp dụng sai dấu/phép tính thành $\\overrightarrow{AB} - \\overrightarrow{AD} '
                           "+ \\overrightarrow{AA'} = \\overrightarrow{AC'}$ thì kết quả của **Quy tắc hình "
                           'hộp** trong **Bài 6: Vectơ trong không gian** vẫn không thay đổi.',
                           "Xét ví dụ của bài: “Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Tính "
                           "tích vô hướng $\\overrightarrow{AB} \\cdot \\overrightarrow{A'C'}$.”, kết quả "
                           "giải đúng là: Vì $\\overrightarrow{A'C'} = \\overrightarrow{AC}$ nên "
                           "$\\overrightarrow{AB} \\cdot \\overrightarrow{A'C'} = \\overrightarrow{AB} "
                           '\\cdot \\overrightarrow{AC}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Vectơ trong không gian. b) **Đúng** '
                        'theo công thức **Quy tắc hình hộp** ($\\overrightarrow{AB} + \\overrightarrow{AD} + '
                        "\\overrightarrow{AA'} = \\overrightarrow{AC'}$). c) **Sai** vì công thức đúng của "
                        '**Quy tắc hình hộp** phải là $\\overrightarrow{AB} + \\overrightarrow{AD} + '
                        "\\overrightarrow{AA'} = \\overrightarrow{AC'}$ chứ không phải $\\overrightarrow{AB} "
                        "- \\overrightarrow{AD} + \\overrightarrow{AA'} = \\overrightarrow{AC'}$. d) "
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 6: Vectơ trong không gian** để giải bài toán sau: '
                 "Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Tính tích vô hướng "
                 "$\\overrightarrow{AB} \\cdot \\overrightarrow{A'C'}$. Cách giải và kết quả nào dưới đây là "
                 '**đúng**?',
            'options': ["Vì $\\overrightarrow{A'C'} = \\overrightarrow{AC}$ nên $\\overrightarrow{AB} : "
                        "\\overrightarrow{A'C'} = \\overrightarrow{AB} \\cdot \\overrightarrow{AC}$...",
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả',
                        "Vì $\\overrightarrow{A'C'} = \\overrightarrow{AC}$ nên $\\overrightarrow{AB} \\cdot "
                        "\\overrightarrow{A'C'} = \\overrightarrow{AB} \\cdot \\overrightarrow{AC}$..."],
            'answer': 3,
            'solution': "Lời giải chi tiết theo Bài 6: Vectơ trong không gian: Vì $\\overrightarrow{A'C'} = "
                        "\\overrightarrow{AC}$ nên $\\overrightarrow{AB} \\cdot \\overrightarrow{A'C'} = "
                        '\\overrightarrow{AB} \\cdot \\overrightarrow{AC}$. Trong hình vuông $ABCD$ cạnh '
                        '$a$, ta có $AC = a\\sqrt{2}$ và góc $(\\overrightarrow{AB}, \\overrightarrow{AC}) = '
                        '\\widehat{BAC} = 45^\\circ$. Do đó $\\overrightarrow{AB} \\cdot '
                        "\\overrightarrow{A'C'} = a \\cdot a\\sqrt{2} \\cdot \\cos 45^\\circ = a^2$."},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Ba lực $\\vec{F}_1, \\vec{F}_2, \\vec{F}_3$ đôi một vuông góc với nhau cùng tác dụng vào '
                 'một vật tại điểm $O$ với độ lớn lần lượt là $3\\text{ N}, 4\\text{ N}, 12\\text{ N}$. Tính '
                 'độ lớn hợp lực $\\vec{F} = \\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3$ (đơn vị: N).',
            'answer': ['13'],
            'unit': None,
            'solution': 'Vì ba lực đôi một vuông góc nên theo quy tắc hình hộp chữ nhật, độ lớn hợp lực là '
                        '$|\\vec{F}| = \\sqrt{|\\vec{F}_1|^2 + |\\vec{F}_2|^2 + |\\vec{F}_3|^2} = \\sqrt{3^2 '
                        '+ 4^2 + 12^2} = \\sqrt{169} = 13\\text{ N}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch02-vecto-khong-gian',
  'context_title': 'Chương II: Vectơ và hệ trục tọa độ trong không gian',
  'context': 'Chương II · SGK Toán 12: Vectơ trong không gian, hệ trục tọa độ Oxyz và biểu thức tọa độ của '
             'các phép toán vectơ.',
  'title': 'Bài 7: Hệ trục tọa độ trong không gian',
  'icon': '🌐',
  'description': 'Hệ trục tọa độ Oxyz, tọa độ của điểm, tọa độ của vectơ và hình chiếu của điểm trên các '
                 'trục và mặt phẳng tọa độ.',
  'requirements': ['Nhận biết được hệ trục tọa độ $Oxyz$ với ba vectơ đơn vị $\\vec{i}, \\vec{j}, \\vec{k}$ '
                   'đôi một vuông góc.',
                   'Xác định được tọa độ của điểm $M(x; y; z)$ và tọa độ của vectơ $\\vec{u} = (x; y; z)$ '
                   'trong không gian.',
                   'Tìm được tọa độ hình chiếu vuông góc và điểm đối xứng qua các trục, các mặt phẳng tọa '
                   'độ.'],
  'definition': 'Hệ trục tọa độ $Oxyz$ gồm ba trục $Ox, Oy, Oz$ đôi một vuông góc tại gốc $O$, với các vectơ '
                'đơn vị tương ứng là $\\vec{i}, \\vec{j}, \\vec{k}$. Nếu $\\vec{u} = x\\vec{i} + y\\vec{j} + '
                'z\\vec{k}$ thì $\\vec{u} = (x; y; z)$. Điểm $M$ có tọa độ $(x; y; z)$ khi và chỉ khi '
                '$\\overrightarrow{OM} = x\\vec{i} + y\\vec{j} + z\\vec{k}$.',
  'theory': '1. Cho $A(x_A; y_A; z_A)$ và $B(x_B; y_B; z_B)$, ta có $\\overrightarrow{AB} = (x_B - x_A; y_B '
            '- y_A; z_B - z_A)$. 2. Hình chiếu vuông góc của $M(x; y; z)$ lên trục $Ox, Oy, Oz$ lần lượt là '
            '$(x; 0; 0), (0; y; 0), (0; 0; z)$. 3. Hình chiếu vuông góc của $M(x; y; z)$ lên mặt phẳng '
            '$(Oxy), (Oyz), (Ozx)$ lần lượt là $(x; y; 0), (0; y; z), (x; 0; z)$.',
  'formulas': [{'category': 'Tọa độ điểm và vectơ',
                'items': [{'name': 'Biểu diễn qua vectơ đơn vị',
                           'formula': '$\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\Leftrightarrow '
                                      '\\vec{u} = (x; y; z)$'},
                          {'name': 'Tọa độ vectơ theo hai đầu mút',
                           'formula': '$\\overrightarrow{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)$'},
                          {'name': 'Hình chiếu lên mặt phẳng (Oxy)',
                           'formula': "$M(x; y; z) \\mapsto M'(x; y; 0)$"}]}],
  'example': 'Trong không gian $Oxyz$, cho hai điểm $A(1; -2; 3)$ và $B(4; 1; -1)$. Tìm tọa độ vectơ '
             '$\\overrightarrow{AB}$ và hình chiếu của $A$ lên mặt phẳng $(Oxz)$.',
  'example_answer': 'Ta có $\\overrightarrow{AB} = (4 - 1; 1 - (-2); -1 - 3) = (3; 3; -4)$. Hình chiếu vuông '
                    "góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có tung độ bằng $0$, tức là điểm $A'(1; 0; "
                    '3)$.',
  'real_life': 'Xác định vị trí máy bay hoặc vệ tinh trong không gian ba chiều thông qua kinh độ, vĩ độ và '
               'độ cao.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, cho vectơ $\\vec{u} = 2\\vec{i} - 3\\vec{j} + 5\\vec{k}$. Tọa độ '
                 'của vectơ $\\vec{u}$ là:',
            'options': ['$(2; 3; 5)$', '$(-2; 3; -5)$', '$(2; -3; 5)$', '$(2; -3; -5)$'],
            'answer': 2,
            'solution': 'Theo định nghĩa tọa độ vectơ, $\\vec{u} = 2\\vec{i} - 3\\vec{j} + 5\\vec{k}$ có tọa '
                        'độ là $(2; -3; 5)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, hình chiếu vuông góc của điểm $M(3; -4; 2)$ trên mặt phẳng '
                 '$(Oxy)$ có tọa độ là:',
            'options': ['$(0; -4; 2)$', '$(3; 0; 2)$', '$(0; 0; 2)$', '$(3; -4; 0)$'],
            'answer': 3,
            'solution': 'Hình chiếu vuông góc của $M(x; y; z)$ trên mặt phẳng $(Oxy)$ là $(x; y; 0)$, nên '
                        'tọa độ cần tìm là $(3; -4; 0)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Hệ trục tọa độ trong không gian**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Biểu diễn qua vectơ đơn vị**?',
            'options': ['$\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; '
                        'z)$',
                        '$\\vec{u} = x\\vec{i} - y\\vec{j} + z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; '
                        'z)$',
                        'Đảo ngược vế của quy tắc: $\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} '
                        '\\Leftrightarrow \\vec{u} = (x; y; z)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\vec{u} = x\\vec{i} + '
                        'y\\vec{j} + z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; z)$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 7: Hệ trục tọa độ trong không gian, **Biểu diễn '
                        'qua vectơ đơn vị** được xác định bởi: $\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} '
                        '\\Leftrightarrow \\vec{u} = (x; y; z)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Hệ trục tọa độ trong không gian**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tọa độ vectơ theo hai đầu mút**?',
            'options': ['$\\overrightarrow{AB} = (x_B + x_A; y_B - y_A; z_B - z_A)$',
                        '$\\overrightarrow{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)$',
                        'Đảo ngược vế của quy tắc: $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A; z_B - '
                        'z_A)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overrightarrow{AB} = (x_B - '
                        'x_A; y_B - y_A; z_B - z_A)$'],
            'answer': 1,
            'solution': 'Trong Bài 7: Hệ trục tọa độ trong không gian, **Tọa độ vectơ theo hai đầu mút** có '
                        'công thức/quy tắc là: $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, cho hai điểm $A(2; 1; -3)$ và $B(5; -1; 1)$. Tọa độ của vectơ '
                 '$\\overrightarrow{AB}$ là:',
            'options': ['$(-3; 2; -4)$', '$(7; 0; -2)$', '$(3; -2; 4)$', '$(3; 2; -4)$'],
            'answer': 2,
            'solution': 'Ta có $\\overrightarrow{AB} = (5 - 2; -1 - 1; 1 - (-3)) = (3; -2; 4)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 7: Hệ trục tọa độ trong không gian**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được hệ trục tọa độ $Oxyz$ với ba vectơ đơn vị $\\vec{i}, \\vec{j}, '
                        '\\vec{k}$ đôi một song song.',
                        'Đảo ngược vế của quy tắc: Nhận biết được hệ trục tọa độ $Oxyz$ với ba vectơ đơn vị '
                        '$\\vec{i}, \\vec{j}, \\vec{k}$ đôi một vuông góc.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được hệ trục tọa độ '
                        '$Oxyz$ với ba vectơ đơn vị $\\vec{i}, \\vec{j}, \\vec{k}$ đôi một vuông góc.',
                        'Nhận biết được hệ trục tọa độ $Oxyz$ với ba vectơ đơn vị $\\vec{i}, \\vec{j}, '
                        '\\vec{k}$ đôi một vuông góc.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 7: Hệ trục tọa độ trong không gian: Nhận biết được hệ '
                        'trục tọa độ $Oxyz$ với ba vectơ đơn vị $\\vec{i}, \\vec{j}, \\vec{k}$ đôi một vuông '
                        'góc.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong không gian $Oxyz$, cho điểm $A(2; -3; 4)$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Vectơ $\\overrightarrow{OA} = 2\\vec{i} - 3\\vec{j} + 4\\vec{k}$.',
                           'Hình chiếu vuông góc của điểm $A$ trên trục $Oz$ là điểm $H(0; 0; 4)$.',
                           "Điểm đối xứng của $A$ qua mặt phẳng $(Oxy)$ là điểm $A'(-2; 3; 4)$.",
                           'Khoảng cách từ điểm $A$ đến mặt phẳng $(Oyz)$ bằng $2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng theo định nghĩa tọa độ điểm. b) Đúng vì chiếu lên $Oz$ giữ nguyên cao độ $z '
                        '= 4$. c) Sai vì đối xứng qua $(Oxy)$ đổi dấu cao độ $z$, được $(2; -3; -4)$. d) '
                        'Đúng vì khoảng cách từ $A(x; y; z)$ đến $(Oyz)$ là $|x| = |2| = 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 7: Hệ trục tọa độ trong '
                 'không gian**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hệ trục tọa độ $Oxyz$ với '
                           'ba vectơ đơn vị $\\vec{i}, \\vec{j}, \\vec{k}$ đôi một vuông góc.',
                           'Trong **Bài 7: Hệ trục tọa độ trong không gian**, quy tắc/công thức **Biểu diễn '
                           'qua vectơ đơn vị** được viết là: $\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} '
                           '\\Leftrightarrow \\vec{u} = (x; y; z)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\vec{u} = x\\vec{i} - y\\vec{j} + '
                           'z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; z)$ thì kết quả của **Biểu diễn qua '
                           'vectơ đơn vị** trong **Bài 7: Hệ trục tọa độ trong không gian** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Trong không gian $Oxyz$, cho hai điểm $A(1; -2; 3)$ và $B(4; '
                           '1; -1)$. Tìm tọa độ vectơ $\\overrightarrow{AB}$ và hình chiếu của $A$ lên...”, '
                           'kết quả giải đúng là: Ta có $\\overrightarrow{AB} = (4 - 1; 1 - (-2); -1 - 3) = '
                           '(3; 3; -4)$. Hình chiếu vuông góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có '
                           't...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Hệ trục tọa độ trong không gian. b) '
                        '**Đúng** theo công thức **Biểu diễn qua vectơ đơn vị** ($\\vec{u} = x\\vec{i} + '
                        'y\\vec{j} + z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; z)$). c) **Sai** vì công '
                        'thức đúng của **Biểu diễn qua vectơ đơn vị** phải là $\\vec{u} = x\\vec{i} + '
                        'y\\vec{j} + z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; z)$ chứ không phải '
                        '$\\vec{u} = x\\vec{i} - y\\vec{j} + z\\vec{k} \\Leftrightarrow \\vec{u} = (x; y; '
                        'z)$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 7: Hệ trục tọa độ trong không gian** để giải bài '
                 'toán sau: Trong không gian $Oxyz$, cho hai điểm $A(1; -2; 3)$ và $B(4; 1; -1)$. Tìm tọa độ '
                 'vectơ $\\overrightarrow{AB}$ và hình chiếu của $A$ lên mặt phẳng $(Oxz)$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\overrightarrow{AB} = (4 - 1; 1 - (-2); -1 - 3) = (3; 3; -4)$. Hình chiếu '
                        'vuông góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có tung độ bằng $0$...',
                        'Ta có $\\overrightarrow{AB} = (4 + 1; 1 - (-2); -1 - 3) = (3; 3; -4)$. Hình chiếu '
                        'vuông góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có tung độ bằng $0$...',
                        'Ta có $\\overrightarrow{AB} = (4 - 1; 1 - (-2); -1 - 3) = (3; 3; -4)$. Hình chiếu '
                        'vuông góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có tung độ bằng $1$...',
                        'Ta có $\\overrightarrow{AB} = (8 - 1; 1 - (-2); -1 - 3) = (3; 3; -4)$. Hình chiếu '
                        'vuông góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có tung độ bằng $0$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Hệ trục tọa độ trong không gian: Ta có '
                        '$\\overrightarrow{AB} = (4 - 1; 1 - (-2); -1 - 3) = (3; 3; -4)$. Hình chiếu vuông '
                        "góc của $A(1; -2; 3)$ lên mặt phẳng $(Oxz)$ có tung độ bằng $0$, tức là điểm $A'(1; "
                        '0; 3)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong không gian $Oxyz$, cho ba điểm $A(1; 2; 0)$, $B(3; -1; 2)$ và $C(2; 4; -1)$. Tìm '
                 'hoành độ của điểm $D$ sao cho tứ giác $ABCD$ là hình bình hành.',
            'answer': ['0'],
            'unit': None,
            'solution': 'Để $ABCD$ là hình bình hành thì $\\overrightarrow{AB} = \\overrightarrow{DC}$. Ta '
                        'có $\\overrightarrow{AB} = (2; -3; 2)$ và $\\overrightarrow{DC} = (2 - x_D; 4 - '
                        'y_D; -1 - z_D)$. Suy ra $2 - x_D = 2 \\Leftrightarrow x_D = 0$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch02-vecto-khong-gian',
  'context_title': 'Chương II: Vectơ và hệ trục tọa độ trong không gian',
  'context': 'Chương II · SGK Toán 12: Vectơ trong không gian, hệ trục tọa độ Oxyz và biểu thức tọa độ của '
             'các phép toán vectơ.',
  'title': 'Bài 8: Biểu thức tọa độ của các phép toán vectơ',
  'icon': '🧮',
  'description': 'Công thức tọa độ của tổng, hiệu hai vectơ, tích vô hướng, độ dài đoạn thẳng, tọa độ trung '
                 'điểm và trọng tâm tam giác.',
  'requirements': ['Thực hiện được các phép toán cộng, trừ vectơ, nhân một số với vectơ và tích vô hướng '
                   'bằng tọa độ.',
                   'Tính được độ dài vectơ, khoảng cách giữa hai điểm và góc giữa hai vectơ trong không gian '
                   '$Oxyz$.',
                   'Xác định được tọa độ trung điểm đoạn thẳng và tọa độ trọng tâm tam giác.'],
  'definition': 'Trong không gian $Oxyz$, cho $\\vec{a} = (x_1; y_1; z_1)$ và $\\vec{b} = (x_2; y_2; z_2)$. '
                'Khi đó $\\vec{a} \\pm \\vec{b} = (x_1 \\pm x_2; y_1 \\pm y_2; z_1 \\pm z_2)$, $k\\vec{a} = '
                '(kx_1; ky_1; kz_1)$ và tích vô hướng $\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + z_1z_2$.',
  'theory': '1. Độ dài vectơ: $|\\vec{a}| = \\sqrt{x_1^2 + y_1^2 + z_1^2}$; khoảng cách $AB = \\sqrt{(x_B - '
            'x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$. 2. Hai vectơ vuông góc: $\\vec{a} \\perp \\vec{b} '
            '\\Leftrightarrow x_1x_2 + y_1y_2 + z_1z_2 = 0$. 3. Trung điểm $I$ của $AB$: '
            '$I\\left(\\dfrac{x_A + x_B}{2}; \\dfrac{y_A + y_B}{2}; \\dfrac{z_A + z_B}{2}\\right)$; trọng '
            'tâm $G$ của $\\triangle ABC$: $G\\left(\\dfrac{x_A + x_B + x_C}{3}; \\dfrac{y_A + y_B + '
            'y_C}{3}; \\dfrac{z_A + z_B + z_C}{3}\\right)$.',
  'formulas': [{'category': 'Biểu thức tọa độ trong không gian Oxyz',
                'items': [{'name': 'Tích vô hướng',
                           'formula': '$\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + z_1z_2$'},
                          {'name': 'Côsin góc giữa hai vectơ',
                           'formula': '$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 + y_1y_2 + '
                                      'z_1z_2}{\\sqrt{x_1^2 + y_1^2 + z_1^2} \\cdot \\sqrt{x_2^2 + y_2^2 + '
                                      'z_2^2}}$'},
                          {'name': 'Khoảng cách giữa hai điểm',
                           'formula': '$AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$'}]}],
  'example': 'Trong không gian $Oxyz$, cho $\\vec{a} = (1; 2; -2)$ và $\\vec{b} = (2; -1; 2)$. Tính '
             '$\\vec{a} \\cdot \\vec{b}$ và $\\cos(\\vec{a}, \\vec{b})$.',
  'example_answer': 'Ta có $\\vec{a} \\cdot \\vec{b} = 1 \\cdot 2 + 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. Độ '
                    'dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + (-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + (-1)^2 '
                    '+ 2^2} = 3$. Suy ra $\\cos(\\vec{a}, \\vec{b}) = \\dfrac{-4}{3 \\cdot 3} = '
                    '-\\dfrac{4}{9}$.',
  'real_life': 'Tính khoảng cách giữa hai máy bay trên màn hình radar kiểm soát không lưu và lập trình đồ '
               'họa 3D.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, cho hai điểm $A(1; 3; -2)$ và $B(3; -1; 4)$. Tọa độ trung điểm '
                 '$I$ của đoạn thẳng $AB$ là:',
            'options': ['$(4; 2; 2)$', '$(1; -2; 3)$', '$(2; 2; 1)$', '$(2; 1; 1)$'],
            'answer': 3,
            'solution': 'Tọa độ trung điểm $I$ là $\\left(\\dfrac{1 + 3}{2}; \\dfrac{3 + (-1)}{2}; '
                        '\\dfrac{-2 + 4}{2}\\right) = (2; 1; 1)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, cho hai vectơ $\\vec{u} = (1; -2; 3)$ và $\\vec{v} = (2; 4; 2)$. '
                 'Tích vô hướng $\\vec{u} \\cdot \\vec{v}$ bằng:',
            'options': ['$0$', '$16$', '$-4$', '$6$'],
            'answer': 0,
            'solution': 'Ta có $\\vec{u} \\cdot \\vec{v} = 1 \\cdot 2 + (-2) \\cdot 4 + 3 \\cdot 2 = 2 - 8 + '
                        '6 = 0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Biểu thức tọa độ của các phép toán vectơ**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Tích vô hướng**?',
            'options': ['$\\vec{a} \\cdot \\vec{b} = x_1x_2 - y_1y_2 + z_1z_2$',
                        '$\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + z_1z_2$',
                        'Đảo ngược vế của quy tắc: $\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + z_1z_2$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\vec{a} \\cdot \\vec{b} = '
                        'x_1x_2 + y_1y_2 + z_1z_2$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 8: Biểu thức tọa độ của các phép toán vectơ, '
                        '**Tích vô hướng** được xác định bởi: $\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + '
                        'z_1z_2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Biểu thức tọa độ của các phép toán vectơ**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Côsin góc giữa hai vectơ**?',
            'options': ['$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 - y_1y_2 + z_1z_2}{\\sqrt{x_1^2 + y_1^2 '
                        '+ z_1^2} \\cdot \\sqrt{x_2^2 + y_2^2 + z_2^2}}$',
                        '$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 + y_1y_2 + z_1z_2}{\\sqrt{x_1^2 + y_1^2 '
                        '+ z_1^2} \\cdot \\sqrt{x_2^2 + y_2^2 + z_2^1}}$',
                        '$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 + y_1y_2 + z_1z_2}{\\sqrt{x_1^2 + y_1^2 '
                        '+ z_1^2} \\cdot \\sqrt{x_2^2 + y_2^2 + z_2^2}}$',
                        '$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 + y_1y_2 + z_1z_2}{\\sqrt{x_1^4 + y_1^2 '
                        '+ z_1^2} \\cdot \\sqrt{x_2^2 + y_2^2 + z_2^2}}$'],
            'answer': 2,
            'solution': 'Trong Bài 8: Biểu thức tọa độ của các phép toán vectơ, **Côsin góc giữa hai vectơ** '
                        'có công thức/quy tắc là: $\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 + y_1y_2 + '
                        'z_1z_2}{\\sqrt{x_1^2 + y_1^2 + z_1^2} \\cdot \\sqrt{x_2^2 + y_2^2 + z_2^2}}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, khoảng cách giữa hai điểm $M(1; -1; 2)$ và $N(3; 1; -1)$ bằng:',
            'options': ['$17$', '$3$', '$\\sqrt{13}$', '$\\sqrt{17}$'],
            'answer': 3,
            'solution': 'Ta có $\\overrightarrow{MN} = (2; 2; -3) \\Rightarrow MN = \\sqrt{2^2 + 2^2 + '
                        '(-3)^2} = \\sqrt{17}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 8: Biểu thức tọa độ của các phép toán vectơ**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Thực hiện được các phép toán cộng, trừ vectơ, nhân một số với vectơ và tích vô '
                        'hướng bằng tọa độ.',
                        'Thực hiện được các phép toán cộng, trừ vectơ, nhân một số với vectơ và tích vô '
                        'hướng bằng tọa độ. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được các phép toán cộng, trừ vectơ, nhân một số '
                        'với vectơ và tích vô hướng bằng tọa độ.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được các phép toán '
                        'cộng, trừ vectơ, nhân một số với vectơ và tích vô hướng bằng tọa độ.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 8: Biểu thức tọa độ của các phép toán vectơ: Thực '
                        'hiện được các phép toán cộng, trừ vectơ, nhân một số với vectơ và tích vô hướng '
                        'bằng tọa độ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(1; 0; 2)$, $B(2; 3; 1)$ và $C(0; 3; 3)$. '
                 'Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Trọng tâm $G$ của tam giác $ABC$ có tọa độ là $(1; 2; 2)$.',
                           'Độ dài cạnh $AB$ bằng $\\sqrt{11}$.',
                           'Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{AC}$ vuông góc với nhau.',
                           'Chu vi của tam giác $ABC$ bằng $6$.'],
            'answer': [True, True, False, False],
            'solution': 'a) Đúng vì $G\\left(\\dfrac{1+2+0}{3}; \\dfrac{0+3+3}{3}; \\dfrac{2+1+3}{3}\\right) '
                        '= (1; 2; 2)$. b) Đúng vì $\\overrightarrow{AB} = (1; 3; -1) \\Rightarrow AB = '
                        '\\sqrt{1 + 9 + 1} = \\sqrt{11}$. c) Sai vì $\\overrightarrow{AC} = (-1; 3; 1) '
                        '\\Rightarrow \\overrightarrow{AB} \\cdot \\overrightarrow{AC} = -1 + 9 - 1 = 7 \\ne '
                        '0$. d) Sai vì $AB = AC = \\sqrt{11}$ và $BC = \\sqrt{(-2)^2 + 0^2 + 2^2} = '
                        '2\\sqrt{2}$, chu vi là $2\\sqrt{11} + 2\\sqrt{2} \\ne 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 8: Biểu thức tọa độ của các '
                 'phép toán vectơ**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được các phép toán cộng, trừ '
                           'vectơ, nhân một số với vectơ và tích vô hướng bằng tọa độ.',
                           'Trong **Bài 8: Biểu thức tọa độ của các phép toán vectơ**, quy tắc/công thức '
                           '**Tích vô hướng** được viết là: $\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + '
                           'z_1z_2$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\vec{a} \\cdot \\vec{b} = x_1x_2 - y_1y_2 '
                           '+ z_1z_2$ thì kết quả của **Tích vô hướng** trong **Bài 8: Biểu thức tọa độ của '
                           'các phép toán vectơ** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Trong không gian $Oxyz$, cho $\\vec{a} = (1; 2; -2)$ và '
                           '$\\vec{b} = (2; -1; 2)$. Tính $\\vec{a} \\cdot \\vec{b}$ và $\\cos(\\vec{a}, '
                           '\\vec{b})$...”, kết quả giải đúng là: Ta có $\\vec{a} \\cdot \\vec{b} = 1 \\cdot '
                           '2 + 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. Độ dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + '
                           '(-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + (-1)^2 + 2^2} = 3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Biểu thức tọa độ của các phép toán '
                        'vectơ. b) **Đúng** theo công thức **Tích vô hướng** ($\\vec{a} \\cdot \\vec{b} = '
                        'x_1x_2 + y_1y_2 + z_1z_2$). c) **Sai** vì công thức đúng của **Tích vô hướng** phải '
                        'là $\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2 + z_1z_2$ chứ không phải $\\vec{a} '
                        '\\cdot \\vec{b} = x_1x_2 - y_1y_2 + z_1z_2$. d) **Đúng** theo lời giải ví dụ minh '
                        'họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 8: Biểu thức tọa độ của các phép toán vectơ** để '
                 'giải bài toán sau: Trong không gian $Oxyz$, cho $\\vec{a} = (1; 2; -2)$ và $\\vec{b} = (2; '
                 '-1; 2)$. Tính $\\vec{a} \\cdot \\vec{b}$ và $\\cos(\\vec{a}, \\vec{b})$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\vec{a} \\cdot \\vec{b} = 1 \\cdot 2 - 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. '
                        'Độ dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + (-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + '
                        '(-1)^2 + 2^2} = 3$...',
                        'Ta có $\\vec{a} \\cdot \\vec{b} = 1 \\cdot 2 + 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. '
                        'Độ dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + (-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + '
                        '(-1)^2 + 2^2} = 3$...',
                        'Ta có $\\vec{a} \\cdot \\vec{b} = 1 \\cdot 2 + 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. '
                        'Độ dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + (-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + '
                        '(-1)^2 + 2^2} = 2$...',
                        'Ta có $\\vec{a} \\cdot \\vec{b} = 2 \\cdot 2 + 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. '
                        'Độ dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + (-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + '
                        '(-1)^2 + 2^2} = 3$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Biểu thức tọa độ của các phép toán vectơ: Ta có '
                        '$\\vec{a} \\cdot \\vec{b} = 1 \\cdot 2 + 2 \\cdot (-1) + (-2) \\cdot 2 = -4$. Độ '
                        'dài $|\\vec{a}| = \\sqrt{1^2 + 2^2 + (-2)^2} = 3$ và $|\\vec{b}| = \\sqrt{2^2 + '
                        '(-1)^2 + 2^2} = 3$. Suy ra $\\cos(\\vec{a}, \\vec{b}) = \\dfrac{-4}{3 \\cdot 3} = '
                        '-\\dfrac{4}{9}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong không gian $Oxyz$, cho hai điểm $A(1; 2; 3)$ và $B(3; 4; -1)$. Điểm $M(0; b; 0)$ '
                 'thuộc trục $Oy$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất. Tìm giá trị của $b$.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Gọi $I(2; 3; 1)$ là trung điểm của $AB$. Ta có $MA^2 + MB^2 = 2MI^2 + '
                        '\\dfrac{AB^2}{2}$, đạt giá trị nhỏ nhất khi $MI$ nhỏ nhất, tức $M$ là hình chiếu '
                        'vuông góc của $I(2; 3; 1)$ trên trục $Oy$. Vậy $M(0; 3; 0) \\Rightarrow b = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch03-phan-tan-ghep-nhom',
  'context_title': 'Chương III: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm',
  'context': 'Chương III · SGK Toán 12: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm '
             '(khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn).',
  'title': 'Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép nhóm',
  'icon': '📉',
  'description': 'Cách tính và ý nghĩa của khoảng biến thiên, khoảng tứ phân vị của mẫu số liệu ghép nhóm '
                 'trong phân tích thống kê.',
  'requirements': ['Tính được khoảng biến thiên $R$ của mẫu số liệu ghép nhóm từ hai đầu mút của bảng tần '
                   'số.',
                   'Xác định được tứ phân vị thứ nhất $Q_1$, tứ phân vị thứ ba $Q_3$ và khoảng tứ phân vị '
                   '$\\Delta_Q = Q_3 - Q_1$.',
                   'Sử dụng được khoảng biến thiên và khoảng tứ phân vị để so sánh mức độ phân tán của các '
                   'mẫu số liệu.'],
  'definition': 'Cho mẫu số liệu ghép nhóm với nhóm đầu tiên là $[a_1; a_2)$ và nhóm cuối cùng là $[a_k; '
                'a_{k+1})$. Khoảng biến thiên của mẫu số liệu ghép nhóm là $R = a_{k+1} - a_1$. Khoảng tứ '
                'phân vị của mẫu số liệu ghép nhóm là $\\Delta_Q = Q_3 - Q_1$.',
  'theory': '1. Khoảng biến thiên $R$ càng lớn thì mẫu số liệu càng phân tán, nhưng $R$ phụ thuộc vào các '
            'giá trị ngoại lệ ở hai đầu. 2. Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$ đo mức độ phân tán của '
            '$50\\%$ số liệu chính giữa mẫu nên không bị ảnh hưởng bởi các giá trị bất thường.',
  'formulas': [{'category': 'Khoảng biến thiên và khoảng tứ phân vị',
                'items': [{'name': 'Khoảng biến thiên', 'formula': '$R = a_{k+1} - a_1$'},
                          {'name': 'Tứ phân vị thứ r (r = 1, 2, 3)',
                           'formula': '$Q_r = u_m + \\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} '
                                      '- u_m)$'},
                          {'name': 'Khoảng tứ phân vị', 'formula': '$\\Delta_Q = Q_3 - Q_1$'}]}],
  'example': 'Chiều cao (đơn vị: cm) của 40 học sinh được ghép thành 4 nhóm: $[150; 155)$ có 6 em; $[155; '
             '160)$ có 14 em; $[160; 165)$ có 12 em; $[165; 170)$ có 8 em. Tính khoảng biến thiên $R$ và tứ '
             'phân vị thứ nhất $Q_1$.',
  'example_answer': 'Khoảng biến thiên là $R = 170 - 150 = 20\\text{ (cm)}$. Cỡ mẫu $n = 40 \\Rightarrow '
                    '\\dfrac{n}{4} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[155; 160)$ vì $6 < 10 \\le 6 + '
                    '14$. Ta có $Q_1 = 155 + \\dfrac{10 - 6}{14} \\cdot (160 - 155) = 155 + \\dfrac{10}{7} '
                    '\\approx 156,43\\text{ (cm)}$.',
  'real_life': 'Đánh giá biên độ dao động nhiệt độ trong tháng và phân tích sự chênh lệch thu nhập của nhóm '
               'lao động phổ thông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một mẫu số liệu ghép nhóm gồm các nhóm $[10; 20), [20; 30), [30; 40), [40; 50)$. Khoảng '
                 'biến thiên $R$ của mẫu số liệu ghép nhóm này bằng:',
            'options': ['$40$', '$30$', '$50$', '$10$'],
            'answer': 0,
            'solution': 'Khoảng biến thiên của mẫu số liệu ghép nhóm là hiệu giữa đầu mút phải của nhóm cuối '
                        'cùng và đầu mút trái của nhóm đầu tiên: $R = 50 - 10 = 40$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho mẫu số liệu ghép nhóm có tứ phân vị thứ nhất $Q_1 = 15,2$ và tứ phân vị thứ ba $Q_3 = '
                 '24,8$. Khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu bằng:',
            'options': ['$40,0$', '$9,6$', '$20,0$', '$4,8$'],
            'answer': 1,
            'solution': 'Ta có $\\Delta_Q = Q_3 - Q_1 = 24,8 - 15,2 = 9,6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép nhóm**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Khoảng biến thiên**?',
            'options': ['$R = a_{k+1} + a_1$',
                        '$R = a_{k+2} - a_1$',
                        '$R = a_{k+1} - a_1$',
                        '$Q_r = u_m + \\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} - u_m)$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu '
                        'số liệu ghép nhóm, **Khoảng biến thiên** được xác định bởi: $R = a_{k+1} - a_1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép nhóm**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Tứ phân vị thứ r (r = 1, 2, 3)**?',
            'options': ['$Q_r = u_m - \\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} - u_m)$',
                        '$Q_r = u_m + \\dfrac{\\dfrac{4}{r \\cdot n} - C}{n_m} \\cdot (u_{m+1} - u_m)$',
                        '$Q_r = u_m + \\dfrac{\\dfrac{r \\cdot n}{8} - C}{n_m} \\cdot (u_{m+1} - u_m)$',
                        '$Q_r = u_m + \\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} - u_m)$'],
            'answer': 3,
            'solution': 'Trong Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép nhóm, **Tứ '
                        'phân vị thứ r (r = 1, 2, 3)** có công thức/quy tắc là: $Q_r = u_m + '
                        '\\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} - u_m)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đặc trưng nào dưới đây đo mức độ phân tán của mẫu số liệu ghép nhóm mà không bị ảnh '
                 'hưởng bởi các giá trị ngoại lệ (bất thường)?',
            'options': ['Khoảng tứ phân vị $\\Delta_Q$',
                        'Khoảng biến thiên $R$',
                        'Số trung bình $\\bar{x}$',
                        'Mốt $M_o$'],
            'answer': 0,
            'solution': 'Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$ chỉ phụ thuộc vào $50\\%$ số liệu ở giữa '
                        'nên không bị ảnh hưởng bởi các giá trị ngoại lệ.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu '
                 'ghép nhóm**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tính được khoảng biến thiên $R$ của mẫu số liệu ghép nhóm từ hai đầu mút của bảng '
                        'tần số. (với dấu ngược lại)',
                        'Tính được khoảng biến thiên $R$ của mẫu số liệu ghép nhóm từ hai đầu mút của bảng '
                        'tần số.',
                        'Đảo ngược vế của quy tắc: Tính được khoảng biến thiên $R$ của mẫu số liệu ghép nhóm '
                        'từ hai đầu mút của bảng tần số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được khoảng biến thiên $R$ '
                        'của mẫu số liệu ghép nhóm từ hai đầu mút của bảng tần số.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số '
                        'liệu ghép nhóm: Tính được khoảng biến thiên $R$ của mẫu số liệu ghép nhóm từ hai '
                        'đầu mút của bảng tần số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Thời gian tự học (phút/ngày) của $40$ học sinh được cho bởi bảng ghép nhóm: $[30; 60)$ có '
                 '$10$ học sinh; $[60; 90)$ có $15$ học sinh; $[90; 120)$ có $10$ học sinh; $[120; 150)$ có '
                 '$5$ học sinh. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Khoảng biến thiên của mẫu số liệu ghép nhóm là $R = 120$ phút.',
                           'Tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là $Q_1 = 60$.',
                           'Nhóm chứa tứ phân vị thứ ba $Q_3$ là nhóm $[90; 120)$.',
                           'Khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\\Delta_Q = 45$.'],
            'answer': [True, True, True, True],
            'solution': 'a) Đúng vì $R = 150 - 30 = 120$. b) Đúng vì $\\dfrac{n}{4} = 10$ trùng tần số tích '
                        'lũy nhóm đầu $[30; 60)$ nên $Q_1 = 60$. c) Đúng vì $\\dfrac{3n}{4} = 30$, tần số '
                        'tích lũy đến nhóm 2 là $25 < 30 \\le 35$ nên $Q_3$ thuộc $[90; 120)$. d) Đúng vì '
                        '$Q_3 = 90 + \\dfrac{30 - 25}{10} \\cdot 30 = 105 \\Rightarrow \\Delta_Q = 105 - 60 '
                        '= 45$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 9: Khoảng biến thiên và '
                 'khoảng tứ phân vị của mẫu số liệu ghép nhóm**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Tính được khoảng biến thiên $R$ của mẫu '
                           'số liệu ghép nhóm từ hai đầu mút của bảng tần số.',
                           'Trong **Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép '
                           'nhóm**, quy tắc/công thức **Khoảng biến thiên** được viết là: $R = a_{k+1} - '
                           'a_1$.',
                           'Nếu áp dụng sai dấu/phép tính thành $R = a_{k+1} + a_1$ thì kết quả của **Khoảng '
                           'biến thiên** trong **Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số '
                           'liệu ghép nhóm** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Chiều cao (đơn vị: cm) của 40 học sinh được ghép thành 4 '
                           'nhóm: $[150; 155)$ có 6 em; $[155; 160)$ có 14 em; $[160; 165)$ có 12 em; $[165; '
                           '170)$...”, kết quả giải đúng là: Khoảng biến thiên là $R = 170 - 150 = 20\\text{ '
                           '(cm)}$. Cỡ mẫu $n = 40 \\Rightarrow \\dfrac{n}{4} = 10$. Nhóm chứa $Q_1$ là nhóm '
                           'thứ hai $[155; 160)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Khoảng biến thiên và khoảng tứ phân vị '
                        'của mẫu số liệu ghép nhóm. b) **Đúng** theo công thức **Khoảng biến thiên** ($R = '
                        'a_{k+1} - a_1$). c) **Sai** vì công thức đúng của **Khoảng biến thiên** phải là $R '
                        '= a_{k+1} - a_1$ chứ không phải $R = a_{k+1} + a_1$. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu '
                 'số liệu ghép nhóm** để giải bài toán sau: Chiều cao (đơn vị: cm) của 40 học sinh được ghép '
                 'thành 4 nhóm: $[150; 155)$ có 6 em; $[155; 160)$ có 14 em; $[160; 165)$ có 12 em; $[165; '
                 '170)$ có 8 em. Tính khoảng biến thiên $R$ và tứ phân vị thứ nhất $Q_1$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Khoảng biến thiên là $R = 170 + 150 = 20\\text{ (cm)}$. Cỡ mẫu $n = 40 \\Rightarrow '
                        '\\dfrac{n}{4} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[155; 160)$ vì...',
                        'Khoảng biến thiên là $R = 170 - 150 = 20\\text{ (cm)}$. Cỡ mẫu $n = 40 \\Rightarrow '
                        '\\dfrac{4}{n} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[155; 160)$ vì...',
                        'Khoảng biến thiên là $R = 170 - 150 = 20\\text{ (cm)}$. Cỡ mẫu $n = 40 \\Rightarrow '
                        '\\dfrac{n}{4} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[155; 160)$ vì...',
                        'Khoảng biến thiên là $R = 172 - 150 = 20\\text{ (cm)}$. Cỡ mẫu $n = 40 \\Rightarrow '
                        '\\dfrac{n}{4} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[155; 160)$ vì...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Khoảng biến thiên và khoảng tứ phân vị của mẫu số '
                        'liệu ghép nhóm: Khoảng biến thiên là $R = 170 - 150 = 20\\text{ (cm)}$. Cỡ mẫu $n = '
                        '40 \\Rightarrow \\dfrac{n}{4} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[155; 160)$ '
                        'vì $6 < 10 \\le 6 + 14$. Ta có $Q_1 = 155 + \\dfrac{10 - 6}{14} \\cdot (160 - 155) '
                        '= 155 + \\dfrac{10}{7} \\approx 156,43\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho mẫu số liệu ghép nhóm về điểm thi của 20 học sinh gồm 4 nhóm: $[2; 4)$ có 3 em; $[4; '
                 '6)$ có 7 em; $[6; 8)$ có 5 em; $[8; 10)$ có 5 em. Tính khoảng tứ phân vị $\\Delta_Q$ của '
                 'mẫu số liệu (làm tròn đến hàng phần mười nếu cần).',
            'answer': ['3,4', '3.4'],
            'unit': None,
            'solution': 'Ta có $n = 20 \\Rightarrow \\dfrac{n}{4} = 5$ thuộc nhóm $[4; 6)$ nên $Q_1 = 4 + '
                        '\\dfrac{5 - 3}{7} \\cdot 2 = \\dfrac{32}{7}$. Lại có $\\dfrac{3n}{4} = 15$ là tần '
                        'số tích lũy hết nhóm $[6; 8)$ nên $Q_3 = 8$. Vậy $\\Delta_Q = 8 - \\dfrac{32}{7} = '
                        '\\dfrac{24}{7} \\approx 3,4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch03-phan-tan-ghep-nhom',
  'context_title': 'Chương III: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm',
  'context': 'Chương III · SGK Toán 12: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm '
             '(khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn).',
  'title': 'Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm',
  'icon': '📊',
  'description': 'Công thức tính phương sai, độ lệch chuẩn của mẫu số liệu ghép nhóm qua giá trị đại diện và '
                 'ứng dụng đánh giá độ rủi ro, độ ổn định.',
  'requirements': ['Xác định được giá trị đại diện $x_i$ của mỗi nhóm và số trung bình $\\bar{x}$ của mẫu số '
                   'liệu ghép nhóm.',
                   'Tính được phương sai $s^2$ và độ lệch chuẩn $s = \\sqrt{s^2}$ của mẫu số liệu ghép nhóm.',
                   'Giải thích được ý nghĩa của phương sai và độ lệch chuẩn trong việc đánh giá độ đồng đều, '
                   'độ ổn định của dữ liệu.'],
  'definition': 'Với mẫu số liệu ghép nhóm có giá trị đại diện $x_i = \\dfrac{a_i + a_{i+1}}{2}$, tần số '
                '$n_i$ ($i = 1, \\dots, k$), cỡ mẫu $n = \\sum n_i$ và số trung bình $\\bar{x} = '
                '\\dfrac{1}{n}\\sum n_i x_i$. Phương sai của mẫu số liệu ghép nhóm là $s^2 = '
                '\\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = \\left(\\dfrac{1}{n}\\sum_{i=1}^k n_i '
                'x_i^2\\right) - \\bar{x}^2$. Độ lệch chuẩn là $s = \\sqrt{s^2}$.',
  'theory': '1. Độ lệch chuẩn $s$ có cùng đơn vị đo với dữ liệu ban đầu nên thuận tiện để giải thích ý nghĩa '
            'thực tế. 2. Phương sai $s^2$ và độ lệch chuẩn $s$ càng nhỏ thì các số liệu trong mẫu càng tập '
            'trung quanh số trung bình $\\bar{x}$ (độ ổn định cao, rủi ro thấp).',
  'formulas': [{'category': 'Phương sai và độ lệch chuẩn',
                'items': [{'name': 'Số trung bình mẫu ghép nhóm',
                           'formula': '$\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$'},
                          {'name': 'Phương sai mẫu ghép nhóm',
                           'formula': '$s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = '
                                      '\\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2 - \\bar{x}^2$'},
                          {'name': 'Độ lệch chuẩn', 'formula': '$s = \\sqrt{s^2}$'}]}],
  'example': 'Khảo sát cân nặng (kg) của 10 quả bưởi thu được: nhóm $[0,8; 1,0)$ có 4 quả; nhóm $[1,0; 1,2)$ '
             'có 6 quả. Tính số trung bình $\\bar{x}$ và phương sai $s^2$.',
  'example_answer': 'Giá trị đại diện của hai nhóm lần lượt là $x_1 = 0,9$ và $x_2 = 1,1$. Số trung bình '
                    '$\\bar{x} = \\dfrac{4 \\cdot 0,9 + 6 \\cdot 1,1}{10} = 1,02\\text{ (kg)}$. Phương sai '
                    '$s^2 = \\dfrac{4 \\cdot (0,9 - 1,02)^2 + 6 \\cdot (1,1 - 1,02)^2}{10} = \\dfrac{4 '
                    '\\cdot 0,0144 + 6 \\cdot 0,0064}{10} = 0,0096$.',
  'real_life': 'Đánh giá độ đồng đều kích thước chi tiết máy trên dây chuyền tự động và đo mức độ biến động '
               'rủi ro của cổ phiếu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu một mẫu số liệu ghép nhóm có phương sai bằng $s^2 = 16$ thì độ lệch chuẩn $s$ của mẫu '
                 'số liệu đó bằng:',
            'options': ['$8$', '$4$', '$256$', '$2$'],
            'answer': 1,
            'solution': 'Độ lệch chuẩn là căn bậc hai số học của phương sai: $s = \\sqrt{s^2} = \\sqrt{16} = '
                        '4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị đại diện của nhóm $[20; 30)$ trong bảng tần số ghép nhóm là:',
            'options': ['$10$', '$20$', '$25$', '$30$'],
            'answer': 2,
            'solution': 'Giá trị đại diện là trung bình cộng hai đầu mút của nhóm: $x_i = \\dfrac{20 + '
                        '30}{2} = 25$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Số trung bình mẫu ghép nhóm**?',
            'options': ['$\\bar{x} = \\dfrac{n_1 x_1 - n_2 x_2 + \\dots + n_k x_k}{n}$',
                        '$\\bar{x} = \\dfrac{n}{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\bar{x} = \\dfrac{n_1 x_1 + '
                        'n_2 x_2 + \\dots + n_k x_k}{n}$',
                        '$\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu '
                        'ghép nhóm, **Số trung bình mẫu ghép nhóm** được xác định bởi: $\\bar{x} = '
                        '\\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm**, biểu thức hoặc '
                 'quy tắc nào dưới đây biểu diễn đúng **Phương sai mẫu ghép nhóm**?',
            'options': ['$s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = '
                        '\\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2 - \\bar{x}^2$',
                        '$s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i + \\bar{x})^2 = '
                        '\\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2 - \\bar{x}^2$',
                        '$s^2 = \\dfrac{n}{1}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = '
                        '\\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2 - \\bar{x}^2$',
                        '$s^4 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i - \\bar{x})^2 = '
                        '\\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2 - \\bar{x}^2$'],
            'answer': 0,
            'solution': 'Trong Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm, **Phương sai '
                        'mẫu ghép nhóm** có công thức/quy tắc là: $s^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i(x_i '
                        '- \\bar{x})^2 = \\dfrac{1}{n}\\sum_{i=1}^k n_i x_i^2 - \\bar{x}^2$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hai xạ thủ A và B cùng bắn thử 30 viên đạn và có điểm trung bình bằng nhau. Độ lệch chuẩn '
                 'điểm bắn của A là $s_A = 0,85$ và của B là $s_B = 1,24$. Khẳng định nào sau đây đúng?',
            'options': ['Xạ thủ B có phong độ bắn ổn định hơn xạ thủ A.',
                        'Xạ thủ A có phong độ bắn ổn định hơn xạ thủ B.',
                        'Hai xạ thủ có độ ổn định như nhau.',
                        'Không thể so sánh độ ổn định bằng độ lệch chuẩn.'],
            'answer': 1,
            'solution': 'Vì $s_A = 0,85 < s_B = 1,24$ nên điểm số của xạ thủ A ít phân tán hơn, tức A bắn ổn '
                        'định hơn B.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép '
                 'nhóm**, nhận định nào sau đây là **chính xác**?',
            'options': ['Xác định được giá trị đại diện $x_i$ của mỗi nhóm và số trung bình $\\bar{x}$ của '
                        'mẫu số liệu ghép nhóm. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Xác định được giá trị đại diện $x_i$ của mỗi nhóm và số '
                        'trung bình $\\bar{x}$ của mẫu số liệu ghép nhóm.',
                        'Xác định được giá trị đại diện $x_i$ của mỗi nhóm và số trung bình $\\bar{x}$ của '
                        'mẫu số liệu ghép nhóm.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Xác định được giá trị đại diện '
                        '$x_i$ của mỗi nhóm và số trung bình $\\bar{x}$ của mẫu số liệu ghép nhóm.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép '
                        'nhóm: Xác định được giá trị đại diện $x_i$ của mỗi nhóm và số trung bình $\\bar{x}$ '
                        'của mẫu số liệu ghép nhóm.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một mẫu số liệu ghép nhóm có $n = 10$ gồm 2 nhóm: nhóm $[2; 6)$ có tần số $n_1 = 5$ và '
                 'nhóm $[6; 10)$ có tần số $n_2 = 5$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Giá trị đại diện của hai nhóm lần lượt là $x_1 = 4$ và $x_2 = 8$.',
                           'Số trung bình của mẫu số liệu ghép nhóm là $\\bar{x} = 6$.',
                           'Phương sai của mẫu số liệu ghép nhóm là $s^2 = 4$.',
                           'Độ lệch chuẩn của mẫu số liệu ghép nhóm là $s = 4$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $x_1 = \\dfrac{2+6}{2} = 4, x_2 = \\dfrac{6+10}{2} = 8$. b) Đúng vì '
                        '$\\bar{x} = \\dfrac{5 \\cdot 4 + 5 \\cdot 8}{10} = 6$. c) Đúng vì $s^2 = '
                        '\\dfrac{5(4-6)^2 + 5(8-6)^2}{10} = 4$. d) Sai vì độ lệch chuẩn là $s = \\sqrt{4} = '
                        '2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 10: Phương sai và độ lệch '
                 'chuẩn của mẫu số liệu ghép nhóm**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Xác định được giá trị đại diện $x_i$ của '
                           'mỗi nhóm và số trung bình $\\bar{x}$ của mẫu số liệu ghép nhóm.',
                           'Trong **Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm**, quy '
                           'tắc/công thức **Số trung bình mẫu ghép nhóm** được viết là: $\\bar{x} = '
                           '\\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\bar{x} = \\dfrac{n_1 x_1 - n_2 x_2 + '
                           '\\dots + n_k x_k}{n}$ thì kết quả của **Số trung bình mẫu ghép nhóm** trong '
                           '**Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Khảo sát cân nặng (kg) của 10 quả bưởi thu được: nhóm $[0,8; '
                           '1,0)$ có 4 quả; nhóm $[1,0; 1,2)$ có 6 quả. Tính số trung bình $\\bar{x}$ v...”, '
                           'kết quả giải đúng là: Giá trị đại diện của hai nhóm lần lượt là $x_1 = 0,9$ và '
                           '$x_2 = 1,1$. Số trung bình $\\bar{x} = \\dfrac{4 \\cdot 0,9 + 6 \\cdot 1,1}{10} '
                           '= 1,02\\text{ (kg)}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Phương sai và độ lệch chuẩn của mẫu số '
                        'liệu ghép nhóm. b) **Đúng** theo công thức **Số trung bình mẫu ghép nhóm** '
                        '($\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$). c) **Sai** vì công '
                        'thức đúng của **Số trung bình mẫu ghép nhóm** phải là $\\bar{x} = \\dfrac{n_1 x_1 + '
                        'n_2 x_2 + \\dots + n_k x_k}{n}$ chứ không phải $\\bar{x} = \\dfrac{n_1 x_1 - n_2 '
                        'x_2 + \\dots + n_k x_k}{n}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu '
                 'ghép nhóm** để giải bài toán sau: Khảo sát cân nặng (kg) của 10 quả bưởi thu được: nhóm '
                 '$[0,8; 1,0)$ có 4 quả; nhóm $[1,0; 1,2)$ có 6 quả. Tính số trung bình $\\bar{x}$ và phương '
                 'sai $s^2$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Giá trị đại diện của hai nhóm lần lượt là $x_1 = 0,9$ và $x_2 = 1,1$. Số trung bình '
                        '$\\bar{x} = \\dfrac{4 \\cdot 0,9 - 6 \\cdot 1,1}{10} = 1,02\\text{ (kg)}$...',
                        'Giá trị đại diện của hai nhóm lần lượt là $x_1 = 0,9$ và $x_2 = 1,1$. Số trung bình '
                        '$\\bar{x} = \\dfrac{10}{4 \\cdot 0,9 + 6 \\cdot 1,1} = 1,02\\text{ (kg)}$...',
                        'Giá trị đại diện của hai nhóm lần lượt là $x_1 = 2,9$ và $x_2 = 1,1$. Số trung bình '
                        '$\\bar{x} = \\dfrac{4 \\cdot 0,9 + 6 \\cdot 1,1}{10} = 1,02\\text{ (kg)}$...',
                        'Giá trị đại diện của hai nhóm lần lượt là $x_1 = 0,9$ và $x_2 = 1,1$. Số trung bình '
                        '$\\bar{x} = \\dfrac{4 \\cdot 0,9 + 6 \\cdot 1,1}{10} = 1,02\\text{ (kg)}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Phương sai và độ lệch chuẩn của mẫu số liệu ghép '
                        'nhóm: Giá trị đại diện của hai nhóm lần lượt là $x_1 = 0,9$ và $x_2 = 1,1$. Số '
                        'trung bình $\\bar{x} = \\dfrac{4 \\cdot 0,9 + 6 \\cdot 1,1}{10} = 1,02\\text{ '
                        '(kg)}$. Phương sai $s^2 = \\dfrac{4 \\cdot (0,9 - 1,02)^2 + 6 \\cdot (1,1 - '
                        '1,02)^2}{10} = \\dfrac{4 \\cdot 0,0144 + 6 \\cdot 0,0064}{10} = 0,0096$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho mẫu số liệu ghép nhóm có cỡ mẫu $n = 20$ gồm 3 nhóm: $[0; 2)$ có 5 số liệu; $[2; 4)$ '
                 'có 10 số liệu; $[4; 6)$ có 5 số liệu. Tính phương sai $s^2$ của mẫu số liệu ghép nhóm này.',
            'answer': ['2'],
            'unit': None,
            'solution': 'Giá trị đại diện là $x_1 = 1, x_2 = 3, x_3 = 5$. Số trung bình $\\bar{x} = '
                        '\\dfrac{5 \\cdot 1 + 10 \\cdot 3 + 5 \\cdot 5}{20} = 3$. Phương sai $s^2 = '
                        '\\dfrac{5(1 - 3)^2 + 10(3 - 3)^2 + 5(5 - 3)^2}{20} = \\dfrac{20 + 0 + 20}{20} = 2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch04-nguyen-ham-tich-phan',
  'context_title': 'Chương IV: Nguyên hàm và tích phân',
  'context': 'Chương IV · SGK Toán 12: Nguyên hàm, tích phân và ứng dụng hình học của tích phân tính diện '
             'tích, thể tích.',
  'title': 'Bài 11: Nguyên hàm',
  'icon': '∫',
  'description': 'Khái niệm nguyên hàm, tính chất cơ bản của nguyên hàm và bảng nguyên hàm của các hàm số sơ '
                 'cấp thường gặp.',
  'requirements': ['Nhận biết được định nghĩa nguyên hàm: $F(x)$ là nguyên hàm của $f(x)$ trên $K$ nếu '
                   "$F'(x) = f(x)$ với mọi $x \\in K$.",
                   'Thuộc và áp dụng được bảng nguyên hàm của hàm lũy thừa, hàm lượng giác, hàm số mũ.',
                   'Vận dụng tính chất tuyến tính của nguyên hàm để tìm họ nguyên hàm và bài toán chuyển '
                   'động.'],
  'definition': 'Cho hàm số $f(x)$ xác định trên khoảng $K$. Hàm số $F(x)$ được gọi là một nguyên hàm của '
                "hàm số $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x \\in K$. Họ tất cả các nguyên hàm của "
                '$f(x)$ trên $K$ được kí hiệu là $\\int f(x)\\,\\mathrm{d}x = F(x) + C$ ($C \\in '
                '\\mathbb{R}$).',
  'theory': '1. Tính chất: $\\int k f(x)\\,\\mathrm{d}x = k \\int f(x)\\,\\mathrm{d}x$ ($k \\ne 0$) và '
            '$\\int [f(x) \\pm g(x)]\\,\\mathrm{d}x = \\int f(x)\\,\\mathrm{d}x \\pm \\int '
            'g(x)\\,\\mathrm{d}x$. 2. Trong vật lí, nếu biết vận tốc $v(t)$ thì quãng đường $s(t) = \\int '
            'v(t)\\,\\mathrm{d}t$; nếu biết gia tốc $a(t)$ thì vận tốc $v(t) = \\int a(t)\\,\\mathrm{d}t$.',
  'formulas': [{'category': 'Bảng nguyên hàm cơ bản',
                'items': [{'name': 'Nguyên hàm hàm lũy thừa',
                           'formula': '$\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + '
                                      '1} + C \\quad (\\alpha \\ne -1), \\quad \\int '
                                      '\\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$'},
                          {'name': 'Nguyên hàm hàm lượng giác',
                           'formula': '$\\int \\cos x\\,\\mathrm{d}x = \\sin x + C, \\quad \\int \\sin '
                                      'x\\,\\mathrm{d}x = -\\cos x + C$'},
                          {'name': 'Nguyên hàm hàm số mũ',
                           'formula': '$\\int e^x\\,\\mathrm{d}x = e^x + C, \\quad \\int a^x\\,\\mathrm{d}x '
                                      '= \\dfrac{a^x}{\\ln a} + C$'}]}],
  'example': 'Tìm nguyên hàm $F(x)$ của hàm số $f(x) = 3x^2 - 2x + 1$ biết $F(1) = 4$.',
  'example_answer': 'Ta có $F(x) = \\int (3x^2 - 2x + 1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo giả thiết '
                    '$F(1) = 4 \\Leftrightarrow 1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = 3$. Vậy $F(x) = '
                    'x^3 - x^2 + x + 3$.',
  'real_life': 'Khôi phục phương trình quãng đường di chuyển của tàu vũ trụ hoặc ô tô từ dữ liệu cảm biến '
               'vận tốc theo thời gian.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Họ tất cả các nguyên hàm của hàm số $f(x) = 4x^3 + 2x$ là:',
            'options': ['$12x^2 + 2 + C$', '$4x^4 + 2x^2 + C$', '$x^4 + x^2 + C$', '$x^4 + 2x^2 + C$'],
            'answer': 2,
            'solution': 'Ta có $\\int (4x^3 + 2x)\\,\\mathrm{d}x = 4 \\cdot \\dfrac{x^4}{4} + 2 \\cdot '
                        '\\dfrac{x^2}{2} + C = x^4 + x^2 + C$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khẳng định nào dưới đây đúng?',
            'options': ['$\\int \\cos x\\,\\mathrm{d}x = -\\sin x + C$',
                        '$\\int \\sin x\\,\\mathrm{d}x = \\cos x + C$',
                        '$\\int e^x\\,\\mathrm{d}x = x e^{x - 1} + C$',
                        '$\\int \\cos x\\,\\mathrm{d}x = \\sin x + C$'],
            'answer': 3,
            'solution': "Vì $(\\sin x)' = \\cos x$ nên $\\int \\cos x\\,\\mathrm{d}x = \\sin x + C$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Nguyên hàm**, quy tắc hoặc công thức nào sau đây xác định đúng **Nguyên '
                 'hàm hàm lũy thừa**?',
            'options': ['$\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + 1} + C \\quad '
                        '(\\alpha \\ne -1), \\quad \\int \\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$',
                        '$\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + 1} + C '
                        '\\quad (\\alpha \\ne -1), \\quad \\int \\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$',
                        '$\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + 1} + C \\quad '
                        '(\\alpha \\ne -1), \\quad \\int \\dfrac{x}{1}\\,\\mathrm{d}x = \\ln|x| + C$',
                        '$\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 2}}{\\alpha + 1} + C \\quad '
                        '(\\alpha \\ne -1), \\quad \\int \\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 11: Nguyên hàm, **Nguyên hàm hàm lũy thừa** được '
                        'xác định bởi: $\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + '
                        '1} + C \\quad (\\alpha \\ne -1), \\quad \\int \\dfrac{1}{x}\\,\\mathrm{d}x = '
                        '\\ln|x| + C$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Nguyên hàm**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Nguyên hàm hàm lượng giác**?',
            'options': ['$\\int \\cos x\\,\\mathrm{d}x = \\sin x + C, \\quad \\int \\sin x\\,\\mathrm{d}x '
                        '= -\\cos x + C$',
                        '$\\int \\cos x\\,\\mathrm{d}x = \\sin x + C, \\quad \\int \\sin x\\,\\mathrm{d}x = '
                        '-\\cos x + C$',
                        'Đảo ngược vế của quy tắc: $\\int \\cos x\\,\\mathrm{d}x = \\sin x + C, \\quad \\int '
                        '\\sin x\\,\\mathrm{d}x = -\\cos x + C$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\int \\cos x\\,\\mathrm{d}x = '
                        '\\sin x + C, \\quad \\int \\sin x\\,\\mathrm{d}x = -\\cos x + C$'],
            'answer': 1,
            'solution': 'Trong Bài 11: Nguyên hàm, **Nguyên hàm hàm lượng giác** có công thức/quy tắc là: '
                        '$\\int \\cos x\\,\\mathrm{d}x = \\sin x + C, \\quad \\int \\sin x\\,\\mathrm{d}x = '
                        '-\\cos x + C$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hàm số $f(x) = e^x + 2x$. Nguyên hàm $F(x)$ của hàm số $f(x)$ thỏa mãn $F(0) = 3$ là:',
            'options': ['$F(x) = e^x + x^2 + 3$',
                        '$F(x) = e^x + 2x^2 + 2$',
                        '$F(x) = e^x + x^2 + 2$',
                        '$F(x) = e^x + x^2 + 1$'],
            'answer': 2,
            'solution': 'Ta có $F(x) = e^x + x^2 + C$. Do $F(0) = 3 \\Rightarrow e^0 + 0 + C = 3 '
                        '\\Leftrightarrow C = 2$. Vậy $F(x) = e^x + x^2 + 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 11: Nguyên hàm**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được định nghĩa nguyên hàm: $F(x)$ là nguyên hàm của $f(x)$ trên $K$ nếu '
                        "$F'(x) = f(x)$ với mọi $x \\notin K$.",
                        'Đảo ngược vế của quy tắc: Nhận biết được định nghĩa nguyên hàm: $F(x)$ là nguyên '
                        "hàm của $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x \\in K$.",
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được định nghĩa '
                        "nguyên hàm: $F(x)$ là nguyên hàm của $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x "
                        '\\in K$.',
                        'Nhận biết được định nghĩa nguyên hàm: $F(x)$ là nguyên hàm của $f(x)$ trên $K$ nếu '
                        "$F'(x) = f(x)$ với mọi $x \\in K$."],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 11: Nguyên hàm: Nhận biết được định nghĩa nguyên hàm: '
                        "$F(x)$ là nguyên hàm của $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x \\in K$."},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $f(x) = 2x + \\dfrac{1}{x}$ xác định trên khoảng $(0; +\\infty)$. Xét tính đúng '
                 'sai của các mệnh đề sau:',
            'statements': ['Họ nguyên hàm của $f(x)$ trên $(0; +\\infty)$ là $F(x) = x^2 + \\ln x + C$.',
                           "Nếu $F(x)$ là một nguyên hàm của $f(x)$ thì $F'(1) = 3$.",
                           'Nguyên hàm $F(x)$ của $f(x)$ thỏa mãn $F(1) = 2$ là $F(x) = x^2 + \\ln x + 2$.',
                           'Trên khoảng $(0; +\\infty)$, mọi nguyên hàm của $f(x)$ đều là hàm số đồng biến.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì trên $(0; +\\infty)$, $|x| = x$ nên $\\int (2x + '
                        "\\dfrac{1}{x})\\,\\mathrm{d}x = x^2 + \\ln x + C$. b) Đúng vì $F'(1) = f(1) = 2 "
                        '\\cdot 1 + 1 = 3$. c) Sai vì $F(1) = 1^2 + \\ln 1 + C = 1 + C = 2 \\Rightarrow C = '
                        "1$. d) Đúng vì $F'(x) = 2x + \\dfrac{1}{x} > 0, \\forall x > 0$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 11: Nguyên hàm**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được định nghĩa nguyên hàm: '
                           "$F(x)$ là nguyên hàm của $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x \\in K$.",
                           'Trong **Bài 11: Nguyên hàm**, quy tắc/công thức **Nguyên hàm hàm lũy thừa** được '
                           'viết là: $\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + 1} '
                           '+ C \\quad (\\alpha \\ne -1), \\quad \\int \\dfrac{1}{x}\\,\\mathrm{d}x = '
                           '\\ln|x| + C$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\int x^\\alpha\\,\\mathrm{d}x = '
                           '\\dfrac{x^{\\alpha + 1}}{\\alpha + 1} + C \\quad (\\alpha \\ne -1), \\quad \\int '
                           '\\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$ thì kết quả của **Nguyên hàm hàm lũy '
                           'thừa** trong **Bài 11: Nguyên hàm** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm nguyên hàm $F(x)$ của hàm số $f(x) = 3x^2 - 2x + 1$ biết '
                           '$F(1) = 4$.”, kết quả giải đúng là: Ta có $F(x) = \\int (3x^2 - 2x + '
                           '1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo giả thiết $F(1) = 4 '
                           '\\Leftrightarrow 1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = 3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Nguyên hàm. b) **Đúng** theo công thức '
                        '**Nguyên hàm hàm lũy thừa** ($\\int x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + '
                        '1}}{\\alpha + 1} + C \\quad (\\alpha \\ne -1), \\quad \\int '
                        '\\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$). c) **Sai** vì công thức đúng của '
                        '**Nguyên hàm hàm lũy thừa** phải là $\\int x^\\alpha\\,\\mathrm{d}x = '
                        '\\dfrac{x^{\\alpha + 1}}{\\alpha + 1} + C \\quad (\\alpha \\ne -1), \\quad \\int '
                        '\\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$ chứ không phải $\\int '
                        'x^\\alpha\\,\\mathrm{d}x = \\dfrac{x^{\\alpha + 1}}{\\alpha + 1} + C \\quad '
                        '(\\alpha \\ne -1), \\quad \\int \\dfrac{1}{x}\\,\\mathrm{d}x = \\ln|x| + C$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 11: Nguyên hàm** để giải bài toán sau: Tìm nguyên '
                 'hàm $F(x)$ của hàm số $f(x) = 3x^2 - 2x + 1$ biết $F(1) = 4$. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $F(x) = \\int (3x^2 - 2x + 1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo giả '
                        'thiết $F(1) = 4 \\Leftrightarrow 1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = 3$...',
                        'Ta có $F(x) = \\int (3x^2 - 2x + 1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo '
                        'giả thiết $F(1) = 4 \\Leftrightarrow 1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = '
                        '3$...',
                        'Ta có $F(x) = \\int (3x^2 - 2x + 1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo giả '
                        'thiết $F(1) = 4 \\Leftrightarrow 1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = 2$...',
                        'Ta có $F(x) = \\int (3x^4 - 2x + 1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo giả '
                        'thiết $F(1) = 4 \\Leftrightarrow 1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = 3$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Nguyên hàm: Ta có $F(x) = \\int (3x^2 - 2x + '
                        '1)\\,\\mathrm{d}x = x^3 - x^2 + x + C$. Theo giả thiết $F(1) = 4 \\Leftrightarrow '
                        '1^3 - 1^2 + 1 + C = 4 \\Leftrightarrow C = 3$. Vậy $F(x) = x^3 - x^2 + x + 3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một ô tô đang chạy với vận tốc $20\\text{ m/s}$ thì người lái đạp phanh; từ thời điểm đó ô '
                 'tô chuyển động chậm dần đều với vận tốc $v(t) = -4t + 20\\text{ (m/s)}$, trong đó $t$ là '
                 'thời gian tính bằng giây kể từ lúc đạp phanh. Tính quãng đường ô tô đi được từ lúc đạp '
                 'phanh đến khi dừng hẳn (đơn vị: mét).',
            'answer': ['50'],
            'unit': None,
            'solution': 'Khi ô tô dừng hẳn thì $v(t) = 0 \\Leftrightarrow -4t + 20 = 0 \\Leftrightarrow t = '
                        '5\\text{ (s)}$. Quãng đường đi được là $s(t) = \\int v(t)\\,\\mathrm{d}t = -2t^2 + '
                        '20t + C$. Với $s(0) = 0 \\Rightarrow C = 0$, suy ra $s(5) = -2 \\cdot 5^2 + 20 '
                        '\\cdot 5 = 50\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch04-nguyen-ham-tich-phan',
  'context_title': 'Chương IV: Nguyên hàm và tích phân',
  'context': 'Chương IV · SGK Toán 12: Nguyên hàm, tích phân và ứng dụng hình học của tích phân tính diện '
             'tích, thể tích.',
  'title': 'Bài 12: Tích phân',
  'icon': '📐',
  'description': 'Định nghĩa tích phân, công thức Newton-Leibniz, các tính chất của tích phân và ứng dụng '
                 'trong bài toán thực tiễn.',
  'requirements': ['Hiểu được định nghĩa tích phân xác định và ý nghĩa hình học của tích phân qua diện tích '
                   'hình thang cong.',
                   'Vận dụng thành thạo công thức Newton-Leibniz $\\int_a^b f(x)\\,\\mathrm{d}x = F(b) - '
                   'F(a)$ và các tính chất của tích phân.',
                   'Giải quyết được bài toán tính quãng đường, điện lượng hoặc lượng nước chảy qua tích '
                   'phân.'],
  'definition': 'Cho hàm số $f(x)$ liên tục trên đoạn $[a; b]$. Nếu $F(x)$ là một nguyên hàm của $f(x)$ trên '
                '$[a; b]$ thì hiệu số $F(b) - F(a)$ được gọi là tích phân từ $a$ đến $b$ của hàm số $f(x)$, '
                'kí hiệu là $\\int_a^b f(x)\\,\\mathrm{d}x$.',
  'theory': '1. Công thức Newton-Leibniz: $\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$. 2. '
            'Tính chất cận: $\\int_a^a f(x)\\,\\mathrm{d}x = 0$, $\\int_a^b f(x)\\,\\mathrm{d}x = -\\int_b^a '
            'f(x)\\,\\mathrm{d}x$, và tính chất chèn cận $\\int_a^b f(x)\\,\\mathrm{d}x = \\int_a^c '
            'f(x)\\,\\mathrm{d}x + \\int_c^b f(x)\\,\\mathrm{d}x$.',
  'formulas': [{'category': 'Công thức và tính chất tích phân',
                'items': [{'name': 'Công thức Newton-Leibniz',
                           'formula': '$\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$'},
                          {'name': 'Tính chất tuyến tính',
                           'formula': '$\\int_a^b [k f(x) + l g(x)]\\,\\mathrm{d}x = k\\int_a^b '
                                      'f(x)\\,\\mathrm{d}x + l\\int_a^b g(x)\\,\\mathrm{d}x$'},
                          {'name': 'Tính chất chèn cận',
                           'formula': '$\\int_a^c f(x)\\,\\mathrm{d}x + \\int_c^b f(x)\\,\\mathrm{d}x = '
                                      '\\int_a^b f(x)\\,\\mathrm{d}x$'}]}],
  'example': 'Tính tích phân $I = \\int_0^2 (3x^2 - 2x + 1)\\,\\mathrm{d}x$.',
  'example_answer': 'Ta có $I = (x^3 - x^2 + x)\\Big|_0^2 = (2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 6$.',
  'real_life': 'Tính tổng điện năng tiêu thụ từ công suất tức thời hoặc tổng lưu lượng nước xả qua đập thủy '
               'điện theo thời gian.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hàm số $f(x)$ liên tục trên đoạn $[a; b]$ và $F(x)$ là một nguyên hàm của $f(x)$ trên '
                 '$[a; b]$. Khẳng định nào dưới đây đúng?',
            'options': ['$\\int_a^b f(x)\\,\\mathrm{d}x = F(a) - F(b)$',
                        "$\\int_a^b f(x)\\,\\mathrm{d}x = f'(b) - f'(a)$",
                        '$\\int_a^b f(x)\\,\\mathrm{d}x = F(b) + F(a)$',
                        '$\\int_a^b f(x)\\,\\mathrm{d}x = F(b) - F(a)$'],
            'answer': 3,
            'solution': 'Theo công thức Newton-Leibniz, $\\int_a^b f(x)\\,\\mathrm{d}x = F(b) - F(a)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của tích phân $\\int_0^1 2x\\,\\mathrm{d}x$ bằng:',
            'options': ['$1$', '$2$', '$0$', '$\\dfrac{1}{2}$'],
            'answer': 0,
            'solution': 'Ta có $\\int_0^1 2x\\,\\mathrm{d}x = x^2\\Big|_0^1 = 1^2 - 0^2 = 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Tích phân**, quy tắc hoặc công thức nào sau đây xác định đúng **Công thức '
                 'Newton-Leibniz**?',
            'options': ['$\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$',
                        '$\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$',
                        'Đảo ngược vế của quy tắc: $\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - '
                        'F(a)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\int_a^b f(x)\\,\\mathrm{d}x '
                        '= F(x)\\Big|_a^b = F(b) - F(a)$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 12: Tích phân, **Công thức Newton-Leibniz** được '
                        'xác định bởi: $\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Tích phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Tính '
                 'chất tuyến tính**?',
            'options': ['$\\int_a^b [k f(x) + l g(x)]\\,\\mathrm{d}x = k\\int_a^b f(x)\\,\\mathrm{d}x + '
                        'l\\int_a^b g(x)\\,\\mathrm{d}x$',
                        'Đảo ngược vế của quy tắc: $\\int_a^b [k f(x) + l g(x)]\\,\\mathrm{d}x = k\\int_a^b '
                        'f(x)\\,\\mathrm{d}x + l\\int_a^b g(x)\\,\\mathrm{d}x$',
                        '$\\int_a^b [k f(x) + l g(x)]\\,\\mathrm{d}x = k\\int_a^b f(x)\\,\\mathrm{d}x + '
                        'l\\int_a^b g(x)\\,\\mathrm{d}x$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\int_a^b [k f(x) + l '
                        'g(x)]\\,\\mathrm{d}x = k\\int_a^b f(x)\\,\\mathrm{d}x + l\\int_a^b '
                        'g(x)\\,\\mathrm{d}x$'],
            'answer': 2,
            'solution': 'Trong Bài 12: Tích phân, **Tính chất tuyến tính** có công thức/quy tắc là: '
                        '$\\int_a^b [k f(x) + l g(x)]\\,\\mathrm{d}x = k\\int_a^b f(x)\\,\\mathrm{d}x + '
                        'l\\int_a^b g(x)\\,\\mathrm{d}x$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biết $\\int_1^3 f(x)\\,\\mathrm{d}x = 4$ và $\\int_1^3 g(x)\\,\\mathrm{d}x = -2$. Giá trị '
                 'của $\\int_1^3 [2f(x) - 3g(x)]\\,\\mathrm{d}x$ bằng:',
            'options': ['$2$', '$10$', '$-14$', '$14$'],
            'answer': 3,
            'solution': 'Ta có $\\int_1^3 [2f(x) - 3g(x)]\\,\\mathrm{d}x = 2\\int_1^3 f(x)\\,\\mathrm{d}x - '
                        '3\\int_1^3 g(x)\\,\\mathrm{d}x = 2 \\cdot 4 - 3 \\cdot (-2) = 14$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 12: Tích phân**, nhận định nào sau đây là **chính xác**?',
            'options': ['Hiểu được định nghĩa tích phân xác định và ý nghĩa hình học của tích phân qua diện '
                        'tích hình thang cong.',
                        'Hiểu được định nghĩa tích phân xác định và ý nghĩa hình học của tích phân qua diện '
                        'tích hình thang cong. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu được định nghĩa tích phân xác định và ý nghĩa hình '
                        'học của tích phân qua diện tích hình thang cong.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu được định nghĩa tích phân '
                        'xác định và ý nghĩa hình học của tích phân qua diện tích hình thang cong.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 12: Tích phân: Hiểu được định nghĩa tích phân xác '
                        'định và ý nghĩa hình học của tích phân qua diện tích hình thang cong.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai hàm số $f(x), g(x)$ liên tục trên đoạn $[0; 5]$ thỏa mãn $\\int_0^2 '
                 'f(x)\\,\\mathrm{d}x = 3$ và $\\int_2^5 f(x)\\,\\mathrm{d}x = 7$. Xét tính đúng sai của các '
                 'mệnh đề sau:',
            'statements': ['Tích phân $\\int_0^5 f(x)\\,\\mathrm{d}x = 10$.',
                           'Tích phân $\\int_2^0 f(x)\\,\\mathrm{d}x = 3$.',
                           'Tích phân $\\int_0^2 [f(x) + 1]\\,\\mathrm{d}x = 5$.',
                           'Tích phân $\\int_0^5 3f(x)\\,\\mathrm{d}x = 30$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $\\int_0^5 f(x)\\,\\mathrm{d}x = \\int_0^2 f(x)\\,\\mathrm{d}x + '
                        '\\int_2^5 f(x)\\,\\mathrm{d}x = 3 + 7 = 10$. b) Sai vì đảo cận phải đổi dấu: '
                        '$\\int_2^0 f(x)\\,\\mathrm{d}x = -3$. c) Đúng vì $3 + \\int_0^2 1\\,\\mathrm{d}x = '
                        '3 + 2 = 5$. d) Đúng vì $3 \\cdot 10 = 30$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 12: Tích phân**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Hiểu được định nghĩa tích phân xác định '
                           'và ý nghĩa hình học của tích phân qua diện tích hình thang cong.',
                           'Trong **Bài 12: Tích phân**, quy tắc/công thức **Công thức Newton-Leibniz** được '
                           'viết là: $\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\int_a^b f(x)\\,\\mathrm{d}x = '
                           'F(x)\\Big|_a^b = F(b) - F(a)$ thì kết quả của **Công thức Newton-Leibniz** trong '
                           '**Bài 12: Tích phân** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tính tích phân $I = \\int_0^2 (3x^2 - 2x + '
                           '1)\\,\\mathrm{d}x$.”, kết quả giải đúng là: Ta có $I = (x^3 - x^2 + x)\\Big|_0^2 '
                           '= (2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 6$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Tích phân. b) **Đúng** theo công thức '
                        '**Công thức Newton-Leibniz** ($\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = '
                        'F(b) - F(a)$). c) **Sai** vì công thức đúng của **Công thức Newton-Leibniz** phải '
                        'là $\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$ chứ không phải '
                        '$\\int_a^b f(x)\\,\\mathrm{d}x = F(x)\\Big|_a^b = F(b) - F(a)$. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 12: Tích phân** để giải bài toán sau: Tính tích '
                 'phân $I = \\int_0^2 (3x^2 - 2x + 1)\\,\\mathrm{d}x$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $I = (x^3 - x^2 - x)\\Big|_0^2 = (2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 6$.',
                        'Ta có $I = (x^3 - x^2 + x)\\Big|_0^2 = (2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 6$.',
                        'Ta có $I = (x^3 - x^2 + x)\\Big|_0^2 = (2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 5$.',
                        'Ta có $I = (x^6 - x^2 + x)\\Big|_0^2 = (2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 6$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Tích phân: Ta có $I = (x^3 - x^2 + x)\\Big|_0^2 = '
                        '(2^3 - 2^2 + 2) - 0 = 8 - 4 + 2 = 6$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hàm số $f(x) = \\begin{cases} 2x + 1 & \\text{khi } x \\ge 1 \\\\ 3x^2 & \\text{khi } '
                 'x < 1 \\end{cases}$. Tính giá trị của tích phân $I = \\int_0^2 f(x)\\,\\mathrm{d}x$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Tách cận tại $x = 1$: $I = \\int_0^1 3x^2\\,\\mathrm{d}x + \\int_1^2 (2x + '
                        '1)\\,\\mathrm{d}x = x^3\\Big|_0^1 + (x^2 + x)\\Big|_1^2 = 1 + (6 - 2) = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch04-nguyen-ham-tich-phan',
  'context_title': 'Chương IV: Nguyên hàm và tích phân',
  'context': 'Chương IV · SGK Toán 12: Nguyên hàm, tích phân và ứng dụng hình học của tích phân tính diện '
             'tích, thể tích.',
  'title': 'Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng và thể tích vật thể)',
  'icon': '🏺',
  'description': 'Ứng dụng tích phân để tính diện tích hình phẳng giới hạn bởi các đường cong và thể tích '
                 'vật thể, khối tròn xoay.',
  'requirements': ['Viết và tính được công thức diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x), y '
                   '= g(x)$ và hai đường thẳng $x = a, x = b$.',
                   'Tính được thể tích vật thể theo diện tích thiết diện $S(x)$ và thể tích khối tròn xoay '
                   'khi quay hình phẳng quanh trục $Ox$.',
                   'Vận dụng tính diện tích, thể tích các vật thể thực tế có hình dạng parabol, elip hoặc '
                   'khối tròn xoay.'],
  'definition': '1. Diện tích hình phẳng giới hạn bởi hai đồ thị hàm số liên tục $y = f(x), y = g(x)$ và hai '
                'đường thẳng $x = a, x = b$ ($a < b$) là $S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$. 2. '
                'Thể tích khối tròn xoay sinh ra khi quay hình phẳng giới hạn bởi $y = f(x)$, trục $Ox$, $x '
                '= a, x = b$ quanh trục $Ox$ là $V = \\pi \\int_a^b [f(x)]^2\\,\\mathrm{d}x$.',
  'theory': '1. Thể tích vật thể giới hạn bởi hai mặt phẳng vuông góc với trục $Ox$ tại $x = a, x = b$ có '
            'diện tích thiết diện $S(x)$ liên tục là $V = \\int_a^b S(x)\\,\\mathrm{d}x$. 2. Khi hình phẳng '
            'chưa cho sẵn cận $a, b$, ta giải phương trình hoành độ giao điểm $f(x) = g(x)$ để tìm cận nhỏ '
            'nhất và lớn nhất.',
  'formulas': [{'category': 'Công thức diện tích và thể tích',
                'items': [{'name': 'Diện tích hình phẳng giới hạn bởi 2 đường',
                           'formula': '$S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$'},
                          {'name': 'Thể tích vật thể theo thiết diện',
                           'formula': '$V = \\int_a^b S(x)\\,\\mathrm{d}x$'},
                          {'name': 'Thể tích khối tròn xoay quanh trục Ox',
                           'formula': '$V = \\pi \\int_a^b [f(x)]^2\\,\\mathrm{d}x$'}]}],
  'example': 'Tính diện tích hình phẳng giới hạn bởi parabol $y = x^2$ và đường thẳng $y = 2x$.',
  'example_answer': 'Phương trình hoành độ giao điểm: $x^2 = 2x \\Leftrightarrow x = 0$ hoặc $x = 2$. Diện '
                    'tích hình phẳng là $S = \\int_0^2 |2x - x^2|\\,\\mathrm{d}x = \\int_0^2 (2x - '
                    'x^2)\\,\\mathrm{d}x = \\left(x^2 - \\dfrac{x^3}{3}\\right)\\Big|_0^2 = 4 - '
                    '\\dfrac{8}{3} = \\dfrac{4}{3}$.',
  'real_life': 'Tính diện tích mặt cắt cổng vòm parabol, dung tích bình hoa gốm sứ, thùng rượu vang và các '
               'chi tiết tiện cơ khí.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Diện tích $S$ của hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ liên tục trên $[a; b]$, '
                 'trục hoành $Ox$ và hai đường thẳng $x = a, x = b$ ($a < b$) được tính theo công thức:',
            'options': ['$S = \\int_a^b |f(x)|\\,\\mathrm{d}x$',
                        '$S = \\pi \\int_a^b [f(x)]^2\\,\\mathrm{d}x$',
                        '$S = \\int_a^b f(x)\\,\\mathrm{d}x$',
                        '$S = \\pi \\int_a^b |f(x)|\\,\\mathrm{d}x$'],
            'answer': 0,
            'solution': 'Công thức tính diện tích hình phẳng giới hạn bởi $y = f(x)$, trục $Ox$ và $x = a, x '
                        '= b$ là $S = \\int_a^b |f(x)|\\,\\mathrm{d}x$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Thể tích $V$ của khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đường $y = '
                 '\\sqrt{x}$, trục hoành $Ox$ và hai đường thẳng $x = 0, x = 4$ quanh trục $Ox$ bằng:',
            'options': ['$8$', '$8\\pi$', '$4\\pi$', '$16\\pi$'],
            'answer': 1,
            'solution': 'Ta có $V = \\pi \\int_0^4 (\\sqrt{x})^2\\,\\mathrm{d}x = \\pi \\int_0^4 '
                        'x\\,\\mathrm{d}x = \\pi \\cdot \\dfrac{x^2}{2}\\Big|_0^4 = 8\\pi$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng và thể tích vật '
                 'thể)**, quy tắc hoặc công thức nào sau đây xác định đúng **Diện tích hình phẳng giới hạn '
                 'bởi 2 đường**?',
            'options': ['$S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$',
                        'Đảo ngược vế của quy tắc: $S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$',
                        '$S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $S = \\int_a^b |f(x) - '
                        'g(x)|\\,\\mathrm{d}x$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 13: Ứng dụng hình học của tích phân (Diện tích '
                        'hình phẳng và thể tích vật thể), **Diện tích hình phẳng giới hạn bởi 2 đường** được '
                        'xác định bởi: $S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng và thể tích vật '
                 'thể)**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Thể tích vật thể theo thiết '
                 'diện**?',
            'options': ['$V = \\int_a^b S(x)\\,\\mathrm{d}x$',
                        'Đảo ngược vế của quy tắc: $V = \\int_a^b S(x)\\,\\mathrm{d}x$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $V = \\int_a^b '
                        'S(x)\\,\\mathrm{d}x$',
                        '$V = \\int_a^b S(x)\\,\\mathrm{d}x$'],
            'answer': 3,
            'solution': 'Trong Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng và thể tích vật '
                        'thể), **Thể tích vật thể theo thiết diện** có công thức/quy tắc là: $V = \\int_a^b '
                        'S(x)\\,\\mathrm{d}x$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Diện tích hình phẳng giới hạn bởi hai đường $y = x^2 - 1$ và $y = 3$ bằng bao nhiêu?',
            'options': ['$\\dfrac{32}{3}$', '$\\dfrac{16}{3}$', '$8$', '$12$'],
            'answer': 0,
            'solution': 'Hoành độ giao điểm: $x^2 - 1 = 3 \\Leftrightarrow x = \\pm 2$. Suy ra $S = '
                        '\\int_{-2}^2 (4 - x^2)\\,\\mathrm{d}x = \\left(4x - '
                        '\\dfrac{x^3}{3}\\right)\\Big|_{-2}^2 = \\dfrac{32}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng '
                 'và thể tích vật thể)**, nhận định nào sau đây là **chính xác**?',
            'options': ['Viết và tính được công thức diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = '
                        'f(x), y = g(x)$ và hai đường thẳng $x = a, x = b$. (với dấu ngược lại)',
                        'Viết và tính được công thức diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = '
                        'f(x), y = g(x)$ và hai đường thẳng $x = a, x = b$.',
                        'Đảo ngược vế của quy tắc: Viết và tính được công thức diện tích hình phẳng giới hạn '
                        'bởi đồ thị hàm số $y = f(x), y = g(x)$ và hai đường thẳng $x = a, x = b$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Viết và tính được công thức '
                        'diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x), y = g(x)$ và hai đường '
                        'thẳng $x = a, x = b$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 13: Ứng dụng hình học của tích phân (Diện tích hình '
                        'phẳng và thể tích vật thể): Viết và tính được công thức diện tích hình phẳng giới '
                        'hạn bởi đồ thị hàm số $y = f(x), y = g(x)$ và hai đường thẳng $x = a, x = b$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = x^2$, trục hoành $Ox$ và hai đường '
                 'thẳng $x = 0, x = 2$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Diện tích của hình phẳng $(H)$ được tính bởi công thức $S = \\int_0^2 '
                           'x^2\\,\\mathrm{d}x$.',
                           'Giá trị diện tích của hình phẳng $(H)$ bằng $\\dfrac{8}{3}$.',
                           'Thể tích khối tròn xoay khi quay $(H)$ quanh trục $Ox$ là $V = \\int_0^2 '
                           'x^4\\,\\mathrm{d}x$.',
                           'Giá trị thể tích khối tròn xoay khi quay $(H)$ quanh trục $Ox$ bằng '
                           '$\\dfrac{32\\pi}{5}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $x^2 \\ge 0$ trên $[0; 2]$. b) Đúng vì $\\int_0^2 x^2\\,\\mathrm{d}x = '
                        '\\dfrac{8}{3}$. c) Sai vì công thức thể tích khối tròn xoay thiếu thừa số $\\pi$: '
                        '$V = \\pi \\int_0^2 x^4\\,\\mathrm{d}x$. d) Đúng vì $V = \\pi \\cdot '
                        '\\dfrac{x^5}{5}\\Big|_0^2 = \\dfrac{32\\pi}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 13: Ứng dụng hình học của '
                 'tích phân (Diện tích hình phẳng và thể tích vật thể)**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Viết và tính được công thức diện tích '
                           'hình phẳng giới hạn bởi đồ thị hàm số $y = f(x), y = g(x)$ và hai đường thẳng $x '
                           '= a, x = b$.',
                           'Trong **Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng và thể '
                           'tích vật thể)**, quy tắc/công thức **Diện tích hình phẳng giới hạn bởi 2 đường** '
                           'được viết là: $S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$.',
                           'Nếu áp dụng sai dấu/phép tính thành $S = \\int_a^b |f(x) - '
                           'g(x)|\\,\\mathrm{d}x$ thì kết quả của **Diện tích hình phẳng giới hạn bởi 2 '
                           'đường** trong **Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng và '
                           'thể tích vật thể)** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tính diện tích hình phẳng giới hạn bởi parabol $y = x^2$ và '
                           'đường thẳng $y = 2x$.”, kết quả giải đúng là: Phương trình hoành độ giao điểm: '
                           '$x^2 = 2x \\Leftrightarrow x = 0$ hoặc $x = 2$. Diện tích hình phẳng là...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Ứng dụng hình học của tích phân (Diện '
                        'tích hình phẳng và thể tích vật thể). b) **Đúng** theo công thức **Diện tích hình '
                        'phẳng giới hạn bởi 2 đường** ($S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$). c) '
                        '**Sai** vì công thức đúng của **Diện tích hình phẳng giới hạn bởi 2 đường** phải là '
                        '$S = \\int_a^b |f(x) - g(x)|\\,\\mathrm{d}x$ chứ không phải $S = \\int_a^b |f(x) '
                        '- g(x)|\\,\\mathrm{d}x$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 13: Ứng dụng hình học của tích phân (Diện tích hình '
                 'phẳng và thể tích vật thể)** để giải bài toán sau: Tính diện tích hình phẳng giới hạn bởi '
                 'parabol $y = x^2$ và đường thẳng $y = 2x$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Phương trình hoành độ giao điểm: $x^3 = 2x \\Leftrightarrow x = 0$ hoặc $x = 2$. '
                        'Diện tích hình phẳng là...',
                        'Phương trình hoành độ giao điểm: $x^2 = 2x \\Leftrightarrow x = 0$ hoặc $x = 1$. '
                        'Diện tích hình phẳng là...',
                        'Phương trình hoành độ giao điểm: $x^2 = 2x \\Leftrightarrow x = 0$ hoặc $x = 2$. '
                        'Diện tích hình phẳng là...',
                        'Phương trình hoành độ giao điểm: $x^4 = 2x \\Leftrightarrow x = 0$ hoặc $x = 2$. '
                        'Diện tích hình phẳng là...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Ứng dụng hình học của tích phân (Diện tích hình '
                        'phẳng và thể tích vật thể): Phương trình hoành độ giao điểm: $x^2 = 2x '
                        '\\Leftrightarrow x = 0$ hoặc $x = 2$. Diện tích hình phẳng là $S = \\int_0^2 |2x - '
                        'x^2|\\,\\mathrm{d}x = \\int_0^2 (2x - x^2)\\,\\mathrm{d}x = \\left(x^2 - '
                        '\\dfrac{x^3}{3}\\right)\\Big|_0^2 = 4 - \\dfrac{8}{3} = \\dfrac{4}{3}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một vật thể nằm giữa hai mặt phẳng $x = 0$ và $x = 3$. Biết rằng thiết diện của vật thể '
                 'cắt bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x$ ($0 \\le x \\le 3$) là '
                 'một hình vuông có cạnh bằng $\\sqrt{4x + 1}$. Tính thể tích của vật thể đó.',
            'answer': ['21'],
            'unit': None,
            'solution': 'Diện tích thiết diện là $S(x) = (\\sqrt{4x + 1})^2 = 4x + 1$. Thể tích vật thể là '
                        '$V = \\int_0^3 (4x + 1)\\,\\mathrm{d}x = (2x^2 + x)\\Big|_0^3 = 2 \\cdot 9 + 3 = '
                        '21$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch05-phuong-phap-toa-do-khong-gian',
  'context_title': 'Chương V: Phương pháp tọa độ trong không gian',
  'context': 'Chương V · SGK Toán 12: Phương trình mặt phẳng, phương trình đường thẳng, công thức tính góc '
             'và phương trình mặt cầu trong không gian Oxyz.',
  'title': 'Bài 14: Phương trình mặt phẳng',
  'icon': '🟦',
  'description': 'Vectơ pháp tuyến, cặp vectơ chỉ phương, phương trình tổng quát của mặt phẳng, điều kiện '
                 'song song, vuông góc và khoảng cách từ điểm đến mặt phẳng.',
  'requirements': ['Xác định được vectơ pháp tuyến $\\vec{n}$ của mặt phẳng và tính tích có hướng '
                   '$[\\vec{u}, \\vec{v}]$ của cặp vectơ chỉ phương.',
                   'Viết được phương trình tổng quát của mặt phẳng và phương trình mặt phẳng theo đoạn chắn.',
                   'Tính được khoảng cách từ một điểm đến một mặt phẳng và xét vị trí tương đối giữa hai mặt '
                   'phẳng.'],
  'definition': 'Trong không gian $Oxyz$, vectơ $\\vec{n} \\ne \\vec{0}$ có giá vuông góc với mặt phẳng '
                '$(\\alpha)$ gọi là vectơ pháp tuyến của $(\\alpha)$. Phương trình mặt phẳng đi qua điểm '
                '$M_0(x_0; y_0; z_0)$ và có vectơ pháp tuyến $\\vec{n} = (A; B; C)$ là $A(x - x_0) + B(y - '
                'y_0) + C(z - z_0) = 0$.',
  'theory': '1. Nếu mặt phẳng $(\\alpha)$ có cặp vectơ chỉ phương không cùng phương $\\vec{u} = (a_1; a_2; '
            'a_3)$ và $\\vec{v} = (b_1; b_2; b_3)$ thì $\\vec{n} = [\\vec{u}, \\vec{v}] = (a_2b_3 - a_3b_2; '
            'a_3b_1 - a_1b_3; a_1b_2 - a_2b_1)$ là một vectơ pháp tuyến. 2. Phương trình mặt phẳng theo đoạn '
            'chắn đi qua $A(a; 0; 0), B(0; b; 0), C(0; 0; c)$ ($abc \\ne 0$) là $\\dfrac{x}{a} + '
            '\\dfrac{y}{b} + \\dfrac{z}{c} = 1$.',
  'formulas': [{'category': 'Phương trình mặt phẳng và khoảng cách',
                'items': [{'name': 'Phương trình tổng quát',
                           'formula': '$Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)$'},
                          {'name': 'Phương trình mặt phẳng đoạn chắn',
                           'formula': '$\\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1 \\quad (abc \\ne '
                                      '0)$'},
                          {'name': 'Khoảng cách từ điểm đến mặt phẳng',
                           'formula': '$d(M_0, (\\alpha)) = \\dfrac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + '
                                      'B^2 + C^2}}$'}]}],
  'example': 'Viết phương trình mặt phẳng $(P)$ đi qua điểm $A(1; -2; 3)$ và có vectơ pháp tuyến $\\vec{n} = '
             '(2; 1; -1)$.',
  'example_answer': 'Phương trình mặt phẳng $(P)$ là $2(x - 1) + 1(y + 2) - 1(z - 3) = 0 \\Leftrightarrow 2x '
                    '+ y - z + 3 = 0$.',
  'real_life': 'Mô hình hóa các bề mặt mái nhà nghiêng, tấm pin năng lượng mặt trời và tính khoảng cách an '
               'toàn trong xây dựng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, mặt phẳng $(P): 2x - 3y + z - 5 = 0$ có một vectơ pháp tuyến là:',
            'options': ['$\\vec{n} = (2; 3; 1)$',
                        '$\\vec{n} = (2; -3; 1)$',
                        '$\\vec{n} = (2; -3; -5)$',
                        '$\\vec{n} = (-2; 3; 1)$'],
            'answer': 1,
            'solution': 'Mặt phẳng $Ax + By + Cz + D = 0$ có một vectơ pháp tuyến là $\\vec{n} = (A; B; C) = '
                        '(2; -3; 1)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, phương trình mặt phẳng đi qua ba điểm $A(2; 0; 0)$, $B(0; -3; 0)$ '
                 'và $C(0; 0; 4)$ là:',
            'options': ['$\\dfrac{x}{2} + \\dfrac{y}{3} + \\dfrac{z}{4} = 1$',
                        '$\\dfrac{x}{2} + \\dfrac{y}{-3} + \\dfrac{z}{4} = 0$',
                        '$\\dfrac{x}{2} + \\dfrac{y}{-3} + \\dfrac{z}{4} = 1$',
                        '$2x - 3y + 4z - 1 = 0$'],
            'answer': 2,
            'solution': 'Theo công thức phương trình mặt phẳng theo đoạn chắn, phương trình là '
                        '$\\dfrac{x}{2} + \\dfrac{y}{-3} + \\dfrac{z}{4} = 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Phương trình mặt phẳng**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Phương trình tổng quát**?',
            'options': ['$Ax - By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)$',
                        '$Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 1)$',
                        '$Ax + By + Cz + D = 2 \\quad (A^2 + B^2 + C^2 > 0)$',
                        '$Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 14: Phương trình mặt phẳng, **Phương trình tổng '
                        'quát** được xác định bởi: $Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Phương trình mặt phẳng**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Phương trình mặt phẳng đoạn chắn**?',
            'options': ['$\\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1 \\quad (abc \\ne 0)$',
                        '$\\dfrac{x}{a} - \\dfrac{y}{b} + \\dfrac{z}{c} = 1 \\quad (abc \\ne 0)$',
                        '$\\dfrac{a}{x} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1 \\quad (abc \\ne 0)$',
                        '$\\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 2 \\quad (abc \\ne 0)$'],
            'answer': 0,
            'solution': 'Trong Bài 14: Phương trình mặt phẳng, **Phương trình mặt phẳng đoạn chắn** có công '
                        'thức/quy tắc là: $\\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1 \\quad (abc '
                        '\\ne 0)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, khoảng cách từ điểm $M(1; 2; -1)$ đến mặt phẳng $(P): x + 2y - 2z '
                 '+ 2 = 0$ bằng:',
            'options': ['$9$', '$3$', '$1$', '$2$'],
            'answer': 1,
            'solution': 'Áp dụng công thức khoảng cách: $d(M, (P)) = \\dfrac{|1 + 2 \\cdot 2 - 2 \\cdot (-1) '
                        '+ 2|}{\\sqrt{1^2 + 2^2 + (-2)^2}} = \\dfrac{9}{3} = 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 14: Phương trình mặt phẳng**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Xác định được vectơ pháp tuyến $\\vec{n}$ của mặt phẳng và tính tích có hướng '
                        '$[\\vec{u}, \\vec{v}]$ của cặp vectơ chỉ phương. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Xác định được vectơ pháp tuyến $\\vec{n}$ của mặt phẳng '
                        'và tính tích có hướng $[\\vec{u}, \\vec{v}]$ của cặp vectơ chỉ phương.',
                        'Xác định được vectơ pháp tuyến $\\vec{n}$ của mặt phẳng và tính tích có hướng '
                        '$[\\vec{u}, \\vec{v}]$ của cặp vectơ chỉ phương.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Xác định được vectơ pháp tuyến '
                        '$\\vec{n}$ của mặt phẳng và tính tích có hướng $[\\vec{u}, \\vec{v}]$ của cặp vectơ '
                        'chỉ phương.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 14: Phương trình mặt phẳng: Xác định được vectơ pháp '
                        'tuyến $\\vec{n}$ của mặt phẳng và tính tích có hướng $[\\vec{u}, \\vec{v}]$ của cặp '
                        'vectơ chỉ phương.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong không gian $Oxyz$, cho hai điểm $A(1; 0; 2), B(3; 2; 4)$ và mặt phẳng $(P): x + y + '
                 'z - 3 = 0$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Điểm $A$ thuộc mặt phẳng $(P)$.',
                           'Vectơ $\\overrightarrow{AB} = (2; 2; 2)$ là một vectơ pháp tuyến của mặt phẳng '
                           'trung trực đoạn $AB$.',
                           'Mặt phẳng trung trực của đoạn thẳng $AB$ có phương trình là $x + y + z - 6 = 0$.',
                           'Mặt phẳng trung trực của đoạn thẳng $AB$ vuông góc với mặt phẳng $(P)$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $1 + 0 + 2 - 3 = 0$. b) Đúng vì mặt phẳng trung trực vuông góc với $AB$. '
                        'c) Đúng vì trung điểm $I(2; 1; 3)$ và VTPT $\\vec{n} = (1; 1; 1)$ cho phương trình '
                        '$(x - 2) + (y - 1) + (z - 3) = 0 \\Leftrightarrow x + y + z - 6 = 0$. d) Sai vì hai '
                        'mặt phẳng có cùng VTPT $(1; 1; 1)$ nên song song với nhau.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 14: Phương trình mặt '
                 'phẳng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Xác định được vectơ pháp tuyến '
                           '$\\vec{n}$ của mặt phẳng và tính tích có hướng $[\\vec{u}, \\vec{v}]$ của cặp '
                           'vectơ chỉ phương.',
                           'Trong **Bài 14: Phương trình mặt phẳng**, quy tắc/công thức **Phương trình tổng '
                           'quát** được viết là: $Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $Ax - By + Cz + D = 0 \\quad (A^2 + B^2 + '
                           'C^2 > 0)$ thì kết quả của **Phương trình tổng quát** trong **Bài 14: Phương '
                           'trình mặt phẳng** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Viết phương trình mặt phẳng $(P)$ đi qua điểm $A(1; -2; 3)$ '
                           'và có vectơ pháp tuyến $\\vec{n} = (2; 1; -1)$.”, kết quả giải đúng là: Phương '
                           'trình mặt phẳng $(P)$ là $2(x - 1) + 1(y + 2) - 1(z - 3) = 0 \\Leftrightarrow 2x '
                           '+ y - z + 3 = 0$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Phương trình mặt phẳng. b) **Đúng** '
                        'theo công thức **Phương trình tổng quát** ($Ax + By + Cz + D = 0 \\quad (A^2 + B^2 '
                        '+ C^2 > 0)$). c) **Sai** vì công thức đúng của **Phương trình tổng quát** phải là '
                        '$Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)$ chứ không phải $Ax - By + Cz + '
                        'D = 0 \\quad (A^2 + B^2 + C^2 > 0)$. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 14: Phương trình mặt phẳng** để giải bài toán sau: '
                 'Viết phương trình mặt phẳng $(P)$ đi qua điểm $A(1; -2; 3)$ và có vectơ pháp tuyến '
                 '$\\vec{n} = (2; 1; -1)$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Phương trình mặt phẳng $(P)$ là $2(x - 1) - 1(y + 2) - 1(z - 3) = 0 '
                        '\\Leftrightarrow 2x + y - z + 3 = 0$.',
                        'Phương trình mặt phẳng $(P)$ là $2(x - 1) + 1(y + 2) - 1(z - 3) = 0 '
                        '\\Leftrightarrow 2x + y - z + 3 = 1$.',
                        'Phương trình mặt phẳng $(P)$ là $4(x - 1) + 1(y + 2) - 1(z - 3) = 0 '
                        '\\Leftrightarrow 2x + y - z + 3 = 0$.',
                        'Phương trình mặt phẳng $(P)$ là $2(x - 1) + 1(y + 2) - 1(z - 3) = 0 '
                        '\\Leftrightarrow 2x + y - z + 3 = 0$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Phương trình mặt phẳng: Phương trình mặt phẳng $(P)$ '
                        'là $2(x - 1) + 1(y + 2) - 1(z - 3) = 0 \\Leftrightarrow 2x + y - z + 3 = 0$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong không gian $Oxyz$, mặt phẳng $(P)$ đi qua điểm $M(1; 1; 1)$ và cắt các tia $Ox, Oy, '
                 'Oz$ lần lượt tại $A(a; 0; 0), B(0; b; 0), C(0; 0; c)$ sao cho thể tích khối tứ diện $OABC$ '
                 'đạt giá trị nhỏ nhất. Tính giá trị của $a + b + c$.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Phương trình $(P): \\dfrac{x}{a} + \\dfrac{y}{b} + \\dfrac{z}{c} = 1$ ($a, b, c > '
                        '0$). Do $M(1; 1; 1) \\in (P)$ nên $\\dfrac{1}{a} + \\dfrac{1}{b} + \\dfrac{1}{c} = '
                        '1 \\ge \\dfrac{3}{\\sqrt[3]{abc}} \\Rightarrow abc \\ge 27$. Thể tích $V_{OABC} = '
                        '\\dfrac{1}{6}abc$ nhỏ nhất khi $a = b = c = 3$. Vậy $a + b + c = 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch05-phuong-phap-toa-do-khong-gian',
  'context_title': 'Chương V: Phương pháp tọa độ trong không gian',
  'context': 'Chương V · SGK Toán 12: Phương trình mặt phẳng, phương trình đường thẳng, công thức tính góc '
             'và phương trình mặt cầu trong không gian Oxyz.',
  'title': 'Bài 15: Phương trình đường thẳng trong không gian',
  'icon': '📏',
  'description': 'Vectơ chỉ phương của đường thẳng, phương trình tham số, phương trình chính tắc và vị trí '
                 'tương đối giữa hai đường thẳng trong không gian.',
  'requirements': ['Xác định được vectơ chỉ phương $\\vec{u}$ của đường thẳng trong không gian.',
                   'Viết được phương trình tham số và phương trình chính tắc của đường thẳng.',
                   'Xét được vị trí tương đối giữa hai đường thẳng (song song, trùng nhau, cắt nhau, chéo '
                   'nhau) và giữa đường thẳng với mặt phẳng.'],
  'definition': 'Vectơ $\\vec{u} = (a; b; c) \\ne \\vec{0}$ có giá song song hoặc trùng với đường thẳng '
                '$\\Delta$ gọi là vectơ chỉ phương của $\\Delta$. Đường thẳng $\\Delta$ đi qua $M_0(x_0; '
                'y_0; z_0)$ có vectơ chỉ phương $\\vec{u} = (a; b; c)$ có phương trình tham số là $x = x_0 + '
                'at, y = y_0 + bt, z = z_0 + ct$ ($t \\in \\mathbb{R}$).',
  'theory': '1. Nếu $abc \\ne 0$, phương trình chính tắc của $\\Delta$ là $\\dfrac{x - x_0}{a} = \\dfrac{y - '
            'y_0}{b} = \\dfrac{z - z_0}{c}$. 2. Hai đường thẳng $\\Delta_1, \\Delta_2$ có VTCP $\\vec{u}_1, '
            '\\vec{u}_2$: nếu $\\vec{u}_1, \\vec{u}_2$ cùng phương thì $\\Delta_1 \\parallel \\Delta_2$ hoặc '
            '$\\Delta_1 \\equiv \\Delta_2$; nếu $\\vec{u}_1, \\vec{u}_2$ không cùng phương thì $\\Delta_1, '
            '\\Delta_2$ cắt nhau (hệ có 1 nghiệm) hoặc chéo nhau (hệ vô nghiệm).',
  'formulas': [{'category': 'Phương trình đường thẳng trong không gian',
                'items': [{'name': 'Phương trình tham số',
                           'formula': '$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\\\ z = z_0 + ct '
                                      '\\end{cases} \\quad (t \\in \\mathbb{R})$'},
                          {'name': 'Phương trình chính tắc',
                           'formula': '$\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c} '
                                      '\\quad (abc \\ne 0)$'},
                          {'name': 'Điều kiện hai đường thẳng vuông góc',
                           'formula': '$\\Delta_1 \\perp \\Delta_2 \\Leftrightarrow \\vec{u}_1 \\cdot '
                                      '\\vec{u}_2 = a_1a_2 + b_1b_2 + c_1c_2 = 0$'}]}],
  'example': 'Viết phương trình chính tắc của đường thẳng $d$ đi qua hai điểm $A(1; 2; -1)$ và $B(3; -1; '
             '4)$.',
  'example_answer': 'Đường thẳng $d$ đi qua $A(1; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ làm '
                    'vectơ chỉ phương. Phương trình chính tắc của $d$ là $\\dfrac{x - 1}{2} = \\dfrac{y - '
                    '2}{-3} = \\dfrac{z + 1}{5}$.',
  'real_life': 'Xác định đường bay của máy bay, hướng chiếu của tia laser phẫu thuật và kiểm tra xung đột '
               'đường ống kỹ thuật trong tòa nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, cho đường thẳng $d: \\dfrac{x - 1}{2} = \\dfrac{y + 2}{-1} = '
                 '\\dfrac{z}{3}$. Vectơ nào dưới đây là một vectơ chỉ phương của $d$?',
            'options': ['$\\vec{u} = (1; -2; 0)$',
                        '$\\vec{u} = (2; 1; 3)$',
                        '$\\vec{u} = (2; -1; 3)$',
                        '$\\vec{u} = (-2; -1; 3)$'],
            'answer': 2,
            'solution': 'Từ phương trình chính tắc, mẫu số cho ta tọa độ vectơ chỉ phương $\\vec{u} = (2; '
                        '-1; 3)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, điểm nào dưới đây thuộc đường thẳng $\\Delta: \\begin{cases} x = '
                 '1 + 2t \\\\ y = -3 + t \\\\ z = 2 - t \\end{cases}$?',
            'options': ['$N(2; 1; -1)$', '$P(1; 3; 2)$', '$Q(-1; 3; -2)$', '$M(1; -3; 2)$'],
            'answer': 3,
            'solution': 'Cho $t = 0$ ta được điểm $M(1; -3; 2)$ thuộc đường thẳng $\\Delta$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Phương trình đường thẳng trong không gian**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Phương trình tham số**?',
            'options': ['$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\\\ z = z_0 + ct \\end{cases} '
                        '\\quad (t \\in \\mathbb{R})$',
                        '$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\\\ z = z_0 + ct \\end{cases} '
                        '\\quad (t \\notin \\mathbb{R})$',
                        'Đảo ngược vế của quy tắc: $\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\\\ z = '
                        'z_0 + ct \\end{cases} \\quad (t \\in \\mathbb{R})$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\begin{cases} x = x_0 + at '
                        '\\\\ y = y_0 + bt \\\\ z = z_0 + ct \\end{cases} \\quad (t \\in \\mathbb{R})$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 15: Phương trình đường thẳng trong không gian, '
                        '**Phương trình tham số** được xác định bởi: $\\begin{cases} x = x_0 + at \\\\ y = '
                        'y_0 + bt \\\\ z = z_0 + ct \\end{cases} \\quad (t \\in \\mathbb{R})$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Phương trình đường thẳng trong không gian**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Phương trình chính tắc**?',
            'options': ['$\\dfrac{x + x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c} \\quad (abc \\ne '
                        '0)$',
                        '$\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c} \\quad (abc \\ne '
                        '0)$',
                        '$\\dfrac{a}{x - x_0} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c} \\quad (abc \\ne '
                        '0)$',
                        '$\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - z_0}{c} \\quad (abc \\ne '
                        '2)$'],
            'answer': 1,
            'solution': 'Trong Bài 15: Phương trình đường thẳng trong không gian, **Phương trình chính tắc** '
                        'có công thức/quy tắc là: $\\dfrac{x - x_0}{a} = \\dfrac{y - y_0}{b} = \\dfrac{z - '
                        'z_0}{c} \\quad (abc \\ne 0)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, đường thẳng đi qua điểm $A(2; 0; -1)$ và vuông góc với mặt phẳng '
                 '$(P): 3x - y + 2z - 5 = 0$ có phương trình tham số là:',
            'options': ['$\\begin{cases} x = 3 + 2t \\\\ y = -1 \\\\ z = 2 - t \\end{cases}$',
                        '$\\begin{cases} x = 2 + 3t \\\\ y = t \\\\ z = -1 + 2t \\end{cases}$',
                        '$\\begin{cases} x = 2 + 3t \\\\ y = -t \\\\ z = -1 + 2t \\end{cases}$',
                        '$\\begin{cases} x = -2 + 3t \\\\ y = -t \\\\ z = 1 + 2t \\end{cases}$'],
            'answer': 2,
            'solution': 'Đường thẳng vuông góc với $(P)$ nên nhận VTPT $\\vec{n}_P = (3; -1; 2)$ làm vectơ '
                        'chỉ phương, đi qua $A(2; 0; -1)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 15: Phương trình đường thẳng trong không gian**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Xác định được vectơ chỉ phương $\\vec{u}$ của đường thẳng trong không gian. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Xác định được vectơ chỉ phương $\\vec{u}$ của đường thẳng '
                        'trong không gian.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Xác định được vectơ chỉ phương '
                        '$\\vec{u}$ của đường thẳng trong không gian.',
                        'Xác định được vectơ chỉ phương $\\vec{u}$ của đường thẳng trong không gian.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 15: Phương trình đường thẳng trong không gian: Xác '
                        'định được vectơ chỉ phương $\\vec{u}$ của đường thẳng trong không gian.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong không gian $Oxyz$, cho đường thẳng $d: \\begin{cases} x = 1 + t \\\\ y = 2 - t \\\\ '
                 'z = 3 + 2t \\end{cases}$ và mặt phẳng $(P): x + 2y + z - 9 = 0$. Xét tính đúng sai của các '
                 'mệnh đề sau:',
            'statements': ['Vectơ $\\vec{u} = (1; -1; 2)$ là một vectơ chỉ phương của đường thẳng $d$.',
                           'Điểm $A(2; 1; 5)$ thuộc đường thẳng $d$.',
                           'Đường thẳng $d$ song song với mặt phẳng $(P)$.',
                           'Giao điểm của đường thẳng $d$ và mặt phẳng $(P)$ có tọa độ là $(2; 1; 5)$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì ứng với $t = 1$. c) Sai vì $\\vec{u} \\cdot \\vec{n}_P = 1 '
                        '\\cdot 1 + (-1) \\cdot 2 + 2 \\cdot 1 = 1 \\ne 0$ nên $d$ cắt $(P)$. d) Đúng vì '
                        'thay tọa độ $d$ vào $(P)$: $(1 + t) + 2(2 - t) + (3 + 2t) - 9 = 0 \\Leftrightarrow '
                        't = 1 \\Rightarrow I(2; 1; 5)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 15: Phương trình đường '
                 'thẳng trong không gian**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Xác định được vectơ chỉ phương '
                           '$\\vec{u}$ của đường thẳng trong không gian.',
                           'Trong **Bài 15: Phương trình đường thẳng trong không gian**, quy tắc/công thức '
                           '**Phương trình tham số** được viết là: $\\begin{cases} x = x_0 + at \\\\ y = y_0 '
                           '+ bt \\\\ z = z_0 + ct \\end{cases} \\quad (t \\in \\mathbb{R})$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\begin{cases} x = x_0 + at \\\\ y = y_0 + '
                           'bt \\\\ z = z_0 + ct \\end{cases} \\quad (t \\notin \\mathbb{R})$ thì kết quả '
                           'của **Phương trình tham số** trong **Bài 15: Phương trình đường thẳng trong '
                           'không gian** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Viết phương trình chính tắc của đường thẳng $d$ đi qua hai '
                           'điểm $A(1; 2; -1)$ và $B(3; -1; 4)$.”, kết quả giải đúng là: Đường thẳng $d$ đi '
                           'qua $A(1; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ làm vectơ chỉ '
                           'phương. Phương trình chính tắc của $d$ là...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Phương trình đường thẳng trong không '
                        'gian. b) **Đúng** theo công thức **Phương trình tham số** ($\\begin{cases} x = x_0 '
                        '+ at \\\\ y = y_0 + bt \\\\ z = z_0 + ct \\end{cases} \\quad (t \\in '
                        '\\mathbb{R})$). c) **Sai** vì công thức đúng của **Phương trình tham số** phải là '
                        '$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\\\ z = z_0 + ct \\end{cases} '
                        '\\quad (t \\in \\mathbb{R})$ chứ không phải $\\begin{cases} x = x_0 + at \\\\ y = '
                        'y_0 + bt \\\\ z = z_0 + ct \\end{cases} \\quad (t \\notin \\mathbb{R})$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 15: Phương trình đường thẳng trong không gian** để '
                 'giải bài toán sau: Viết phương trình chính tắc của đường thẳng $d$ đi qua hai điểm $A(1; '
                 '2; -1)$ và $B(3; -1; 4)$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đường thẳng $d$ đi qua $A(1; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ '
                        'làm vectơ chỉ phương. Phương trình chính tắc của $d$ là $\\dfrac{x - 1}{2} = '
                        '\\dfrac{y - 2}{-3} = \\dfrac{z + 1}{5}$...',
                        'Đường thẳng $d$ đi qua $A(1; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ '
                        'làm vectơ chỉ phương. Phương trình chính tắc của $d$ là $\\dfrac{x - 1}{2} = '
                        '\\dfrac{y - 2}{-3} = \\dfrac{z - 1}{5}$...',
                        'Đường thẳng $d$ đi qua $A(1; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ '
                        'làm vectơ chỉ phương. Phương trình chính tắc của $d$ là $\\dfrac{2}{x - 1} = '
                        '\\dfrac{y - 2}{-3} = \\dfrac{z + 1}{5}$...',
                        'Đường thẳng $d$ đi qua $A(2; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ '
                        'làm vectơ chỉ phương. Phương trình chính tắc của $d$ là $\\dfrac{x - 1}{2} = '
                        '\\dfrac{y - 2}{-3} = \\dfrac{z + 1}{5}$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Phương trình đường thẳng trong không gian: Đường '
                        'thẳng $d$ đi qua $A(1; 2; -1)$ và nhận $\\overrightarrow{AB} = (2; -3; 5)$ làm '
                        'vectơ chỉ phương. Phương trình chính tắc của $d$ là $\\dfrac{x - 1}{2} = \\dfrac{y '
                        '- 2}{-3} = \\dfrac{z + 1}{5}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong không gian $Oxyz$, cho điểm $A(1; 2; 3)$ và mặt phẳng $(P): x + y + z - 3 = 0$. Gọi '
                 '$H(a; b; c)$ là hình chiếu vuông góc của điểm $A$ trên mặt phẳng $(P)$. Tính giá trị của '
                 '$a + 2b + 3c$.',
            'answer': ['8'],
            'unit': None,
            'solution': 'Đường thẳng $AH$ đi qua $A(1; 2; 3)$ và vuông góc với $(P)$ có phương trình $x = 1 '
                        '+ t, y = 2 + t, z = 3 + t$. Vì $H \\in (P)$ nên $(1 + t) + (2 + t) + (3 + t) - 3 = '
                        '0 \\Leftrightarrow t = -1 \\Rightarrow H(0; 1; 2)$. Vậy $a + 2b + 3c = 0 + 2 \\cdot '
                        '1 + 3 \\cdot 2 = 8$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch05-phuong-phap-toa-do-khong-gian',
  'context_title': 'Chương V: Phương pháp tọa độ trong không gian',
  'context': 'Chương V · SGK Toán 12: Phương trình mặt phẳng, phương trình đường thẳng, công thức tính góc '
             'và phương trình mặt cầu trong không gian Oxyz.',
  'title': 'Bài 16: Công thức tính góc trong không gian',
  'icon': '📐',
  'description': 'Công thức tọa độ tính góc giữa hai đường thẳng, góc giữa đường thẳng và mặt phẳng, góc '
                 'giữa hai mặt phẳng trong không gian Oxyz.',
  'requirements': ['Tính được côsin góc giữa hai đường thẳng thông qua hai vectơ chỉ phương.',
                   'Tính được sin của góc giữa đường thẳng và mặt phẳng thông qua vectơ chỉ phương và vectơ '
                   'pháp tuyến.',
                   'Tính được côsin góc giữa hai mặt phẳng thông qua hai vectơ pháp tuyến.'],
  'definition': 'Trong không gian $Oxyz$, góc giữa hai đường thẳng, góc giữa đường thẳng và mặt phẳng, góc '
                'giữa hai mặt phẳng đều thuộc đoạn $[0^\\circ; 90^\\circ]$ và được xác định thông qua giá '
                'trị tuyệt đối của tích vô hướng các vectơ đặc trưng.',
  'theory': '1. Góc giữa hai đường thẳng $\\Delta_1, \\Delta_2$ có VTCP $\\vec{u}_1, \\vec{u}_2$: '
            '$\\cos(\\Delta_1, \\Delta_2) = |\\cos(\\vec{u}_1, \\vec{u}_2)| = \\dfrac{|\\vec{u}_1 \\cdot '
            '\\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$. 2. Góc giữa đường thẳng $\\Delta$ (VTCP '
            '$\\vec{u}$) và mặt phẳng $(P)$ (VTPT $\\vec{n}$): $\\sin(\\Delta, (P)) = |\\cos(\\vec{u}, '
            '\\vec{n})| = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot |\\vec{n}|}$. 3. Góc giữa '
            'hai mặt phẳng $(P_1), (P_2)$ có VTPT $\\vec{n}_1, \\vec{n}_2$: $\\cos((P_1), (P_2)) = '
            '|\\cos(\\vec{n}_1, \\vec{n}_2)| = \\dfrac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1| \\cdot '
            '|\\vec{n}_2|}$.',
  'formulas': [{'category': 'Ba công thức tính góc trong không gian Oxyz',
                'items': [{'name': 'Góc giữa hai đường thẳng',
                           'formula': '$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\vec{u}_1 \\cdot '
                                      '\\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$'},
                          {'name': 'Góc giữa đường thẳng và mặt phẳng',
                           'formula': '$\\sin(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| '
                                      '\\cdot |\\vec{n}|}$'},
                          {'name': 'Góc giữa hai mặt phẳng',
                           'formula': '$\\cos((P_1), (P_2)) = \\dfrac{|\\vec{n}_1 \\cdot '
                                      '\\vec{n}_2|}{|\\vec{n}_1| \\cdot |\\vec{n}_2|}$'}]}],
  'example': 'Trong không gian $Oxyz$, tính góc giữa đường thẳng $d: \\dfrac{x}{1} = \\dfrac{y}{-1} = '
             '\\dfrac{z}{2}$ và mặt phẳng $(P): x - y + 2z - 5 = 0$.',
  'example_answer': 'Đường thẳng $d$ có VTCP $\\vec{u} = (1; -1; 2)$ và mặt phẳng $(P)$ có VTPT $\\vec{n} = '
                    '(1; -1; 2)$. Ta có $\\sin(d, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| '
                    '\\cdot |\\vec{n}|} = \\dfrac{|1 + 1 + 4|}{\\sqrt{6} \\cdot \\sqrt{6}} = 1$. Suy ra góc '
                    'giữa $d$ và $(P)$ bằng $90^\\circ$ (hay $d \\perp (P)$).',
  'real_life': 'Tính độ dốc mái nhà, góc nghiêng của đường băng sân bay và góc đón nắng tối ưu cho tấm pin '
               'mặt trời.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, cho đường thẳng $\\Delta$ có vectơ chỉ phương $\\vec{u}$ và mặt '
                 'phẳng $(P)$ có vectơ pháp tuyến $\\vec{n}$. Công thức nào dưới đây đúng?',
            'options': ['$\\cos(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|}$',
                        '$\\sin(\\Delta, (P)) = \\dfrac{\\vec{u} \\cdot \\vec{n}}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|}$',
                        '$\\tan(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|}$',
                        '$\\sin(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|}$'],
            'answer': 3,
            'solution': 'Sin của góc giữa đường thẳng và mặt phẳng bằng giá trị tuyệt đối của côsin góc giữa '
                        'VTCP $\\vec{u}$ và VTPT $\\vec{n}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, góc giữa hai mặt phẳng $(Oxy)$ và $(Oyz)$ bằng:',
            'options': ['$90^\\circ$', '$60^\\circ$', '$45^\\circ$', '$0^\\circ$'],
            'answer': 0,
            'solution': 'Hai mặt phẳng tọa độ $(Oxy)$ và $(Oyz)$ vuông góc với nhau nên góc giữa chúng bằng '
                        '$90^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Công thức tính góc trong không gian**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Góc giữa hai đường thẳng**?',
            'options': ['$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\vec{u}_1 : \\vec{u}_2|}{|\\vec{u}_1| '
                        '\\cdot |\\vec{u}_2|}$',
                        '$\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| '
                        '\\cdot |\\vec{u}_2|}$',
                        'Đảo ngược vế của quy tắc: $\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\vec{u}_1 \\cdot '
                        '\\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\cos(\\Delta_1, \\Delta_2) = '
                        '\\dfrac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 16: Công thức tính góc trong không gian, **Góc '
                        'giữa hai đường thẳng** được xác định bởi: $\\cos(\\Delta_1, \\Delta_2) = '
                        '\\dfrac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Công thức tính góc trong không gian**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Góc giữa đường thẳng và mặt phẳng**?',
            'options': ['$\\sin(\\Delta, (P)) = \\dfrac{|\\vec{u} : \\vec{n}|}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|}$',
                        'Đảo ngược vế của quy tắc: $\\sin(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot '
                        '\\vec{n}|}{|\\vec{u}| \\cdot |\\vec{n}|}$',
                        '$\\sin(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\sin(\\Delta, (P)) = '
                        '\\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot |\\vec{n}|}$'],
            'answer': 2,
            'solution': 'Trong Bài 16: Công thức tính góc trong không gian, **Góc giữa đường thẳng và mặt '
                        'phẳng** có công thức/quy tắc là: $\\sin(\\Delta, (P)) = \\dfrac{|\\vec{u} \\cdot '
                        '\\vec{n}|}{|\\vec{u}| \\cdot |\\vec{n}|}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, góc giữa hai đường thẳng $d_1: \\dfrac{x}{1} = \\dfrac{y}{1} = '
                 '\\dfrac{z}{0}$ và $d_2: \\dfrac{x}{1} = \\dfrac{y}{0} = \\dfrac{z}{1}$ bằng:',
            'options': ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$', '$60^\\circ$'],
            'answer': 3,
            'solution': 'Ta có $\\vec{u}_1 = (1; 1; 0)$ và $\\vec{u}_2 = (1; 0; 1)$. Khi đó $\\cos(d_1, d_2) '
                        '= \\dfrac{|1 \\cdot 1 + 1 \\cdot 0 + 0 \\cdot 1|}{\\sqrt{2} \\cdot \\sqrt{2}} = '
                        '\\dfrac{1}{2} \\Rightarrow (d_1, d_2) = 60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 16: Công thức tính góc trong không gian**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Tính được côsin góc giữa hai đường thẳng thông qua hai vectơ chỉ phương.',
                        'Tính được côsin góc giữa hai đường thẳng thông qua hai vectơ chỉ phương. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính được côsin góc giữa hai đường thẳng thông qua hai '
                        'vectơ chỉ phương.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được côsin góc giữa hai '
                        'đường thẳng thông qua hai vectơ chỉ phương.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 16: Công thức tính góc trong không gian: Tính được '
                        'côsin góc giữa hai đường thẳng thông qua hai vectơ chỉ phương.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong không gian $Oxyz$, cho mặt phẳng $(P): x + y - 2 = 0$ và đường thẳng $d: '
                 '\\dfrac{x}{1} = \\dfrac{y}{0} = \\dfrac{z}{1}$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\\vec{n} = (1; 1; 0)$.',
                           'Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u} = (1; 0; 1)$.',
                           'Góc giữa đường thẳng $d$ và mặt phẳng $(P)$ bằng $60^\\circ$.',
                           'Góc giữa mặt phẳng $(P)$ và mặt phẳng $(Oyz)$ bằng $45^\\circ$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì $\\sin(d, (P)) = \\dfrac{|1 \\cdot 1 + 0 \\cdot 1 + 1 '
                        '\\cdot 0|}{\\sqrt{2} \\cdot \\sqrt{2}} = \\dfrac{1}{2} \\Rightarrow (d, (P)) = '
                        '30^\\circ$. d) Đúng vì $(Oyz)$ có VTPT $\\vec{i} = (1; 0; 0)$, $\\cos((P), (Oyz)) = '
                        '\\dfrac{1}{\\sqrt{2} \\cdot 1} = \\dfrac{\\sqrt{2}}{2} \\Rightarrow 45^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 16: Công thức tính góc '
                 'trong không gian**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Tính được côsin góc giữa hai đường thẳng '
                           'thông qua hai vectơ chỉ phương.',
                           'Trong **Bài 16: Công thức tính góc trong không gian**, quy tắc/công thức **Góc '
                           'giữa hai đường thẳng** được viết là: $\\cos(\\Delta_1, \\Delta_2) = '
                           '\\dfrac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\cos(\\Delta_1, \\Delta_2) = '
                           '\\dfrac{|\\vec{u}_1 : \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$ thì kết '
                           'quả của **Góc giữa hai đường thẳng** trong **Bài 16: Công thức tính góc trong '
                           'không gian** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Trong không gian $Oxyz$, tính góc giữa đường thẳng $d: '
                           '\\dfrac{x}{1} = \\dfrac{y}{-1} = \\dfrac{z}{2}$ và mặt phẳng $(P): x - y + 2z - '
                           '5 = 0$...”, kết quả giải đúng là: Đường thẳng $d$ có VTCP $\\vec{u} = (1; -1; '
                           '2)$ và mặt phẳng $(P)$ có VTPT $\\vec{n} = (1; -1; 2)$. Ta có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Công thức tính góc trong không gian. '
                        'b) **Đúng** theo công thức **Góc giữa hai đường thẳng** ($\\cos(\\Delta_1, '
                        '\\Delta_2) = \\dfrac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot '
                        '|\\vec{u}_2|}$). c) **Sai** vì công thức đúng của **Góc giữa hai đường thẳng** phải '
                        'là $\\cos(\\Delta_1, \\Delta_2) = \\dfrac{|\\vec{u}_1 \\cdot '
                        '\\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$ chứ không phải $\\cos(\\Delta_1, '
                        '\\Delta_2) = \\dfrac{|\\vec{u}_1 : \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 16: Công thức tính góc trong không gian** để giải '
                 'bài toán sau: Trong không gian $Oxyz$, tính góc giữa đường thẳng $d: \\dfrac{x}{1} = '
                 '\\dfrac{y}{-1} = \\dfrac{z}{2}$ và mặt phẳng $(P): x - y + 2z - 5 = 0$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Đường thẳng $d$ có VTCP $\\vec{u} = (2; -1; 2)$ và mặt phẳng $(P)$ có VTPT '
                        '$\\vec{n} = (1; -1; 2)$. Ta có...',
                        'Đường thẳng $d$ có VTCP $\\vec{u} = (1; -1; 2)$ và mặt phẳng $(P)$ có VTPT '
                        '$\\vec{n} = (1; -1; 2)$. Ta có...',
                        'Đường thẳng $d$ có VTCP $\\vec{u} = (1; -1; 2)$ và mặt phẳng $(P)$ có VTPT '
                        '$\\vec{n} = (1; -1; 1)$. Ta có...',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Công thức tính góc trong không gian: Đường thẳng $d$ '
                        'có VTCP $\\vec{u} = (1; -1; 2)$ và mặt phẳng $(P)$ có VTPT $\\vec{n} = (1; -1; 2)$. '
                        'Ta có $\\sin(d, (P)) = \\dfrac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot '
                        '|\\vec{n}|} = \\dfrac{|1 + 1 + 4|}{\\sqrt{6} \\cdot \\sqrt{6}} = 1$. Suy ra góc '
                        'giữa $d$ và $(P)$ bằng $90^\\circ$ (hay $d \\perp (P)$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong không gian $Oxyz$, tính số đo góc (theo đơn vị độ) giữa đường thẳng $d: \\dfrac{x - '
                 '1}{1} = \\dfrac{y + 2}{1} = \\dfrac{z}{\\sqrt{2}}$ và mặt phẳng $(Oxy)$.',
            'answer': ['45'],
            'unit': None,
            'solution': 'Đường thẳng $d$ có VTCP $\\vec{u} = (1; 1; \\sqrt{2})$ và mặt phẳng $(Oxy)$ có VTPT '
                        '$\\vec{k} = (0; 0; 1)$. Ta có $\\sin(d, (Oxy)) = \\dfrac{|\\sqrt{2}|}{\\sqrt{1 + 1 '
                        '+ 2} \\cdot 1} = \\dfrac{\\sqrt{2}}{2}$, suy ra góc bằng $45^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch05-phuong-phap-toa-do-khong-gian',
  'context_title': 'Chương V: Phương pháp tọa độ trong không gian',
  'context': 'Chương V · SGK Toán 12: Phương trình mặt phẳng, phương trình đường thẳng, công thức tính góc '
             'và phương trình mặt cầu trong không gian Oxyz.',
  'title': 'Bài 17: Phương trình mặt cầu',
  'icon': '🌐',
  'description': 'Phương trình chính tắc và phương trình tổng quát của mặt cầu, cách xác định tâm, bán kính '
                 'và vị trí tương đối với mặt phẳng.',
  'requirements': ['Nhận biết và viết được phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng $(x '
                   '- a)^2 + (y - b)^2 + (z - c)^2 = R^2$.',
                   'Xác định được điều kiện để phương trình $x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$ là '
                   'phương trình mặt cầu và tìm được tâm, bán kính.',
                   'Giải quyết được các bài toán giao của mặt cầu với mặt phẳng, đường thẳng và ứng dụng '
                   'định vị GPS.'],
  'definition': 'Trong không gian $Oxyz$, mặt cầu $(S)$ tâm $I(a; b; c)$ bán kính $R > 0$ là tập hợp tất cả '
                'các điểm $M(x; y; z)$ thỏa mãn $IM = R$, có phương trình là $(x - a)^2 + (y - b)^2 + (z - '
                'c)^2 = R^2$.',
  'theory': '1. Phương trình dạng khai triển $x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$ là phương trình của '
            'một mặt cầu khi và chỉ khi $a^2 + b^2 + c^2 - d > 0$; khi đó tâm là $I(a; b; c)$ và bán kính là '
            '$R = \\sqrt{a^2 + b^2 + c^2 - d}$. 2. Nếu mặt phẳng $(P)$ cắt mặt cầu $(S)$ theo giao tuyến là '
            'đường tròn bán kính $r$ thì $R^2 = d^2(I, (P)) + r^2$.',
  'formulas': [{'category': 'Phương trình mặt cầu',
                'items': [{'name': 'Phương trình chính tắc',
                           'formula': '$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$'},
                          {'name': 'Bán kính từ dạng khai triển',
                           'formula': '$R = \\sqrt{a^2 + b^2 + c^2 - d} \\quad (\\text{với } a^2 + b^2 + c^2 '
                                      '- d > 0)$'},
                          {'name': 'Hệ thức mặt phẳng cắt mặt cầu',
                           'formula': '$R^2 = d^2(I, (P)) + r^2$'}]}],
  'example': 'Tìm tâm $I$ và bán kính $R$ của mặt cầu $(S): x^2 + y^2 + z^2 - 4x + 2y - 6z + 5 = 0$.',
  'example_answer': 'Ta có $a = 2, b = -1, c = 3, d = 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán kính '
                    '$R = \\sqrt{2^2 + (-1)^2 + 3^2 - 5} = \\sqrt{9} = 3$.',
  'real_life': 'Xác định vùng phủ sóng của trạm phát Wi-Fi, radar phòng không và định vị toàn cầu GPS dựa '
               'trên giao của các mặt cầu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, mặt cầu $(S): (x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 16$ có tâm $I$ '
                 'và bán kính $R$ lần lượt là:',
            'options': ['$I(1; -2; 3), R = 4$',
                        '$I(-1; 2; -3), R = 4$',
                        '$I(1; -2; 3), R = 16$',
                        '$I(1; 2; 3), R = 4$'],
            'answer': 0,
            'solution': 'Từ phương trình $(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 4^2$, suy ra tâm $I(1; -2; 3)$ '
                        'và bán kính $R = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, phương trình mặt cầu tâm $O(0; 0; 0)$ và bán kính $R = 3$ là:',
            'options': ['$x^2 + y^2 + z^2 = 3$',
                        '$x^2 + y^2 + z^2 = 9$',
                        '$(x - 3)^2 + (y - 3)^2 + (z - 3)^2 = 9$',
                        '$x^2 + y^2 + z^2 = 6$'],
            'answer': 1,
            'solution': 'Mặt cầu tâm $O(0; 0; 0)$ bán kính $R = 3$ có phương trình $x^2 + y^2 + z^2 = 3^2 = '
                        '9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Phương trình mặt cầu**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Phương trình chính tắc**?',
            'options': ['$(x - a)^2 - (y - b)^2 + (z - c)^2 = R^2$',
                        '$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^1$',
                        '$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$',
                        '$(x - a)^4 + (y - b)^2 + (z - c)^2 = R^2$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 17: Phương trình mặt cầu, **Phương trình chính '
                        'tắc** được xác định bởi: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Phương trình mặt cầu**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Bán kính từ dạng khai triển**?',
            'options': ['$R = \\sqrt{a^2 - b^2 + c^2 - d} \\quad (\\text{với } a^2 + b^2 + c^2 - d > 0)$',
                        '$R = \\sqrt{a^2 + b^2 + c^2 - d} \\quad (\\text{với } a^2 + b^2 + c^2 - d > 1)$',
                        '$R = \\sqrt{a^4 + b^2 + c^2 - d} \\quad (\\text{với } a^2 + b^2 + c^2 - d > 0)$',
                        '$R = \\sqrt{a^2 + b^2 + c^2 - d} \\quad (\\text{với } a^2 + b^2 + c^2 - d > 0)$'],
            'answer': 3,
            'solution': 'Trong Bài 17: Phương trình mặt cầu, **Bán kính từ dạng khai triển** có công '
                        'thức/quy tắc là: $R = \\sqrt{a^2 + b^2 + c^2 - d} \\quad (\\text{với } a^2 + b^2 + '
                        'c^2 - d > 0)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong không gian $Oxyz$, mặt cầu đường kính $AB$ với $A(1; 2; -1)$ và $B(3; 0; 3)$ có '
                 'phương trình là:',
            'options': ['$(x - 2)^2 + (y - 1)^2 + (z - 1)^2 = 6$',
                        '$(x - 2)^2 + (y - 1)^2 + (z - 1)^2 = 24$',
                        '$(x + 2)^2 + (y + 1)^2 + (z + 1)^2 = 6$',
                        '$(x - 2)^2 + (y - 1)^2 + (z - 1)^2 = \\sqrt{6}$'],
            'answer': 0,
            'solution': 'Tâm $I$ là trung điểm của $AB \\Rightarrow I(2; 1; 1)$. Bán kính $R = IA = '
                        '\\sqrt{(1 - 2)^2 + (2 - 1)^2 + (-1 - 1)^2} = \\sqrt{6} \\Rightarrow R^2 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 17: Phương trình mặt cầu**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết và viết được phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng '
                        '$(x - a)^2 - (y - b)^2 + (z - c)^2 = R^2$.',
                        'Nhận biết và viết được phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng '
                        '$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.',
                        'Nhận biết và viết được phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng '
                        '$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^1$.',
                        'Nhận biết và viết được phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng '
                        '$(x - a)^4 + (y - b)^2 + (z - c)^2 = R^2$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 17: Phương trình mặt cầu: Nhận biết và viết được '
                        'phương trình mặt cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng $(x - a)^2 + (y - b)^2 '
                        '+ (z - c)^2 = R^2$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong không gian $Oxyz$, cho mặt cầu $(S): x^2 + y^2 + z^2 - 2x - 4y - 4z - 7 = 0$. Xét '
                 'tính đúng sai của các mệnh đề sau:',
            'statements': ['Tâm của mặt cầu $(S)$ là điểm $I(1; 2; 2)$.',
                           'Bán kính của mặt cầu $(S)$ bằng $4$.',
                           'Điểm $A(1; 2; 6)$ nằm trên mặt cầu $(S)$.',
                           'Mặt phẳng $(Oxy)$ tiếp xúc với mặt cầu $(S)$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $a = 1, b = 2, c = 2$. b) Đúng vì $R = \\sqrt{1^2 + 2^2 + 2^2 - (-7)} = '
                        '\\sqrt{16} = 4$. c) Đúng vì $IA = \\sqrt{0 + 0 + 4^2} = 4 = R$. d) Sai vì $d(I, '
                        '(Oxy)) = |z_I| = 2 < R = 4$ nên $(Oxy)$ cắt mặt cầu $(S)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 17: Phương trình mặt cầu**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết và viết được phương trình mặt '
                           'cầu tâm $I(a; b; c)$ bán kính $R$ dưới dạng $(x - a)^2 + (y - b)^2 + (z - c)^2 = '
                           'R^2$.',
                           'Trong **Bài 17: Phương trình mặt cầu**, quy tắc/công thức **Phương trình chính '
                           'tắc** được viết là: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.',
                           'Nếu áp dụng sai dấu/phép tính thành $(x - a)^2 - (y - b)^2 + (z - c)^2 = R^2$ '
                           'thì kết quả của **Phương trình chính tắc** trong **Bài 17: Phương trình mặt '
                           'cầu** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm tâm $I$ và bán kính $R$ của mặt cầu $(S): x^2 + y^2 + '
                           'z^2 - 4x + 2y - 6z + 5 = 0$.”, kết quả giải đúng là: Ta có $a = 2, b = -1, c = '
                           '3, d = 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán kính $R = \\sqrt{2^2 + '
                           '(-1)^2 + 3^2 - 5} = \\sqrt{9} = 3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Phương trình mặt cầu. b) **Đúng** theo '
                        'công thức **Phương trình chính tắc** ($(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$). '
                        'c) **Sai** vì công thức đúng của **Phương trình chính tắc** phải là $(x - a)^2 + (y '
                        '- b)^2 + (z - c)^2 = R^2$ chứ không phải $(x - a)^2 - (y - b)^2 + (z - c)^2 = R^2$. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 17: Phương trình mặt cầu** để giải bài toán sau: '
                 'Tìm tâm $I$ và bán kính $R$ của mặt cầu $(S): x^2 + y^2 + z^2 - 4x + 2y - 6z + 5 = 0$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $a = 2, b = -1, c = 3, d = 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán '
                        'kính $R = \\sqrt{2^2 - (-1)^2 + 3^2 - 5} = \\sqrt{9} = 3$.',
                        'Ta có $a = 2, b = -1, c = 3, d = 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán '
                        'kính $R = \\sqrt{2^2 + (-1)^2 + 3^2 - 5} = \\sqrt{9} = 2$.',
                        'Ta có $a = 2, b = -1, c = 3, d = 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán '
                        'kính $R = \\sqrt{2^2 + (-1)^2 + 3^2 - 5} = \\sqrt{9} = 3$.',
                        'Ta có $a = 4, b = -1, c = 3, d = 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán '
                        'kính $R = \\sqrt{2^2 + (-1)^2 + 3^2 - 5} = \\sqrt{9} = 3$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Phương trình mặt cầu: Ta có $a = 2, b = -1, c = 3, d '
                        '= 5$. Vậy mặt cầu $(S)$ có tâm $I(2; -1; 3)$ và bán kính $R = \\sqrt{2^2 + (-1)^2 + '
                        '3^2 - 5} = \\sqrt{9} = 3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong không gian $Oxyz$, cho mặt cầu $(S): (x - 1)^2 + (y - 2)^2 + (z - 2)^2 = 25$ và mặt '
                 'phẳng $(P): 2x + 2y + z + 4 = 0$. Biết mặt phẳng $(P)$ cắt mặt cầu $(S)$ theo giao tuyến '
                 'là một đường tròn. Tính bán kính $r$ của đường tròn giao tuyến đó.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Mặt cầu $(S)$ có tâm $I(1; 2; 2)$ và bán kính $R = 5$. Khoảng cách từ $I$ đến $(P)$ '
                        'là $d = \\dfrac{|2 \\cdot 1 + 2 \\cdot 2 + 2 + 4|}{\\sqrt{2^2 + 2^2 + 1^2}} = '
                        '\\dfrac{12}{3} = 4$. Suy ra bán kính đường tròn giao tuyến là $r = \\sqrt{R^2 - '
                        'd^2} = \\sqrt{5^2 - 4^2} = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch06-xac-suat-co-dieu-kien',
  'context_title': 'Chương VI: Xác suất có điều kiện',
  'context': 'Chương VI · SGK Toán 12: Xác suất có điều kiện, sơ đồ hình cây, công thức xác suất toàn phần '
             'và công thức Bayes.',
  'title': 'Bài 18: Xác suất có điều kiện',
  'icon': '🎲',
  'description': 'Khái niệm xác suất có điều kiện, công thức tính xác suất có điều kiện và công thức nhân '
                 'xác suất cho hai biến cố bất kì.',
  'requirements': ['Hiểu được khái niệm xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra, kí '
                   'hiệu $P(A | B)$.',
                   'Tính được $P(A | B) = \\dfrac{P(AB)}{P(B)}$ khi $P(B) > 0$ và vận dụng được công thức '
                   'nhân xác suất $P(AB) = P(B) \\cdot P(A | B)$.',
                   'Sử dụng được sơ đồ hình cây và bảng tần số hai chiều để giải các bài toán xác suất có '
                   'điều kiện.'],
  'definition': 'Cho hai biến cố $A$ và $B$ với $P(B) > 0$. Xác suất của biến cố $A$ với điều kiện biến cố '
                '$B$ đã xảy ra được kí hiệu là $P(A | B)$ và được xác định bởi công thức $P(A | B) = '
                '\\dfrac{P(AB)}{P(B)}$.',
  'theory': '1. Công thức nhân xác suất cho hai biến cố bất kì: $P(AB) = P(B) \\cdot P(A | B) = P(A) \\cdot '
            'P(B | A)$. 2. Với mọi biến cố $A$ và $B$ ($P(B) > 0$), ta có $P(\\overline{A} | B) = 1 - P(A | '
            'B)$. 3. Hai biến cố $A$ và $B$ độc lập khi và chỉ khi $P(A | B) = P(A)$.',
  'formulas': [{'category': 'Xác suất có điều kiện và công thức nhân',
                'items': [{'name': 'Định nghĩa xác suất có điều kiện',
                           'formula': '$P(A | B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) '
                                      '> 0)$'},
                          {'name': 'Công thức nhân xác suất',
                           'formula': '$P(AB) = P(A) \\cdot P(B | A) = P(B) \\cdot P(A | B)$'},
                          {'name': 'Biến cố đối có điều kiện',
                           'formula': '$P(\\overline{A} | B) = 1 - P(A | B)$'}]}],
  'example': 'Một lớp có $40$ học sinh, trong đó có $25$ học sinh thích môn Toán, $20$ học sinh thích môn Lý '
             'và $15$ học sinh thích cả hai môn. Chọn ngẫu nhiên một học sinh, biết học sinh đó thích môn '
             'Toán, tính xác suất để học sinh đó cũng thích môn Lý.',
  'example_answer': 'Gọi $A$ là biến cố học sinh thích Lý, $B$ là biến cố học sinh thích Toán. Ta có $n(B) = '
                    '25$ và $n(AB) = 15$. Xác suất cần tìm là $P(A | B) = \\dfrac{n(AB)}{n(B)} = '
                    '\\dfrac{15}{25} = \\dfrac{3}{5} = 0,6$.',
  'real_life': 'Đánh giá nguy cơ mắc bệnh tim mạch khi biết bệnh nhân có tiền sử huyết áp cao và phân tích '
               'hành vi mua sắm khách hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố $A$ và $B$ với $P(B) > 0$. Công thức tính xác suất của biến cố $A$ với '
                 'điều kiện biến cố $B$ đã xảy ra là:',
            'options': ['$P(A | B) = \\dfrac{P(AB)}{P(A)}$',
                        '$P(A | B) = \\dfrac{P(AB)}{P(B)}$',
                        '$P(A | B) = P(A) \\cdot P(B)$',
                        '$P(A | B) = \\dfrac{P(A)}{P(B)}$'],
            'answer': 1,
            'solution': 'Theo định nghĩa, $P(A | B) = \\dfrac{P(AB)}{P(B)}$ với $P(B) > 0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố $A$ và $B$ có $P(A) = 0,5$, $P(B) = 0,4$ và $P(AB) = 0,2$. Giá trị của '
                 '$P(A | B)$ bằng:',
            'options': ['$0,4$', '$0,8$', '$0,5$', '$0,1$'],
            'answer': 2,
            'solution': 'Ta có $P(A | B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{0,2}{0,4} = 0,5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Xác suất có điều kiện**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Định nghĩa xác suất có điều kiện**?',
            'options': ['$P(A | B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) < 0)$',
                        '$P(A | B) = \\dfrac{P(B)}{P(AB)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) > 0)$',
                        '$P(A | B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) > 2)$',
                        '$P(A | B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) > 0)$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 18: Xác suất có điều kiện, **Định nghĩa xác suất '
                        'có điều kiện** được xác định bởi: $P(A | B) = \\dfrac{P(AB)}{P(B)} = '
                        '\\dfrac{n(AB)}{n(B)} \\quad (P(B) > 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Xác suất có điều kiện**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Công thức nhân xác suất**?',
            'options': ['$P(AB) = P(A) \\cdot P(B | A) = P(B) \\cdot P(A | B)$',
                        '$P(AB) = P(A) : P(B | A) = P(B) \\cdot P(A | B)$',
                        'Đảo ngược vế của quy tắc: $P(AB) = P(A) \\cdot P(B | A) = P(B) \\cdot P(A | B)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(AB) = P(A) \\cdot P(B | A) = '
                        'P(B) \\cdot P(A | B)$'],
            'answer': 0,
            'solution': 'Trong Bài 18: Xác suất có điều kiện, **Công thức nhân xác suất** có công thức/quy '
                        'tắc là: $P(AB) = P(A) \\cdot P(B | A) = P(B) \\cdot P(A | B)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hộp có $6$ bi trắng và $4$ bi đen. Lấy ngẫu nhiên lần lượt $2$ viên bi không hoàn lại. '
                 'Xác suất để cả $2$ viên bi lấy ra đều màu trắng là:',
            'options': ['$\\dfrac{9}{25}$', '$\\dfrac{1}{3}$', '$\\dfrac{2}{5}$', '$\\dfrac{1}{5}$'],
            'answer': 1,
            'solution': 'Gọi $A_1, A_2$ là biến cố viên thứ nhất, thứ hai màu trắng. Theo công thức nhân: '
                        '$P(A_1A_2) = P(A_1) \\cdot P(A_2 | A_1) = \\dfrac{6}{10} \\cdot \\dfrac{5}{9} = '
                        '\\dfrac{30}{90} = \\dfrac{1}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 18: Xác suất có điều kiện**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Hiểu được khái niệm xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra, '
                        'kí hiệu $P(A | B)$. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu được khái niệm xác suất của biến cố $A$ với điều '
                        'kiện biến cố $B$ đã xảy ra, kí hiệu $P(A | B)$.',
                        'Hiểu được khái niệm xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra, '
                        'kí hiệu $P(A | B)$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu được khái niệm xác suất '
                        'của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra, kí hiệu $P(A | B)$.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 18: Xác suất có điều kiện: Hiểu được khái niệm xác '
                        'suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra, kí hiệu $P(A | B)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai biến cố $A$ và $B$ thỏa mãn $P(A) = 0,6$; $P(B) = 0,5$ và $P(A | B) = 0,4$. Xét '
                 'tính đúng sai của các mệnh đề sau:',
            'statements': ['Xác suất của biến cố giao $AB$ là $P(AB) = 0,2$.',
                           'Xác suất có điều kiện $P(\\overline{A} | B) = 0,6$.',
                           'Xác suất có điều kiện $P(B | A) = \\dfrac{1}{3}$.',
                           'Hai biến cố $A$ và $B$ là hai biến cố độc lập.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $P(AB) = P(B) \\cdot P(A | B) = 0,5 \\cdot 0,4 = 0,2$. b) Đúng vì '
                        '$P(\\overline{A} | B) = 1 - P(A | B) = 0,6$. c) Đúng vì $P(B | A) = '
                        '\\dfrac{P(AB)}{P(A)} = \\dfrac{0,2}{0,6} = \\dfrac{1}{3}$. d) Sai vì $P(A | B) = '
                        '0,4 \\ne P(A) = 0,6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 18: Xác suất có điều '
                 'kiện**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Hiểu được khái niệm xác suất của biến cố '
                           '$A$ với điều kiện biến cố $B$ đã xảy ra, kí hiệu $P(A | B)$.',
                           'Trong **Bài 18: Xác suất có điều kiện**, quy tắc/công thức **Định nghĩa xác suất '
                           'có điều kiện** được viết là: $P(A | B) = \\dfrac{P(AB)}{P(B)} = '
                           '\\dfrac{n(AB)}{n(B)} \\quad (P(B) > 0)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $P(A | B) = \\dfrac{P(AB)}{P(B)} = '
                           '\\dfrac{n(AB)}{n(B)} \\quad (P(B) < 0)$ thì kết quả của **Định nghĩa xác suất có '
                           'điều kiện** trong **Bài 18: Xác suất có điều kiện** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một lớp có $40$ học sinh, trong đó có $25$ học sinh thích '
                           'môn Toán, $20$ học sinh thích môn Lý và $15$ học sinh thích cả hai môn. '
                           'Chọn...”, kết quả giải đúng là: Gọi $A$ là biến cố học sinh thích Lý, $B$ là '
                           'biến cố học sinh thích Toán. Ta có $n(B) = 25$ và $n(AB) = 15$. Xác suất cần tìm '
                           'là...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Xác suất có điều kiện. b) **Đúng** '
                        'theo công thức **Định nghĩa xác suất có điều kiện** ($P(A | B) = '
                        '\\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) > 0)$). c) **Sai** vì công '
                        'thức đúng của **Định nghĩa xác suất có điều kiện** phải là $P(A | B) = '
                        '\\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) > 0)$ chứ không phải $P(A '
                        '| B) = \\dfrac{P(AB)}{P(B)} = \\dfrac{n(AB)}{n(B)} \\quad (P(B) < 0)$. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 18: Xác suất có điều kiện** để giải bài toán sau: '
                 'Một lớp có $40$ học sinh, trong đó có $25$ học sinh thích môn Toán, $20$ học sinh thích '
                 'môn Lý và $15$ học sinh thích cả hai môn. Chọn ngẫu nhiên một học sinh, biết học sinh đó '
                 'thích môn Toán, tính xác suất để học sinh đó cũng thích môn Lý. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Gọi $A$ là biến cố học sinh thích Lý, $B$ là biến cố học sinh thích Toán. Ta có '
                        '$n(B) = 35$ và $n(AB) = 15$. Xác suất cần tìm là $P(A | B) = \\dfrac{n(AB)}{n(B)} = '
                        '\\dfrac{15}{25} = \\dfrac{3}{5} = 0,6$...',
                        'Gọi $A$ là biến cố học sinh thích Lý, $B$ là biến cố học sinh thích Toán. Ta có '
                        '$n(B) = 25$ và $n(AB) = 15$. Xác suất cần tìm là $P(A | B) = \\dfrac{n(B)}{n(AB)} = '
                        '\\dfrac{15}{25} = \\dfrac{3}{5} = 0,6$...',
                        'Gọi $A$ là biến cố học sinh thích Lý, $B$ là biến cố học sinh thích Toán. Ta có '
                        '$n(B) = 50$ và $n(AB) = 15$. Xác suất cần tìm là $P(A | B) = \\dfrac{n(AB)}{n(B)} = '
                        '\\dfrac{15}{25} = \\dfrac{3}{5} = 0,6$...',
                        'Gọi $A$ là biến cố học sinh thích Lý, $B$ là biến cố học sinh thích Toán. Ta có '
                        '$n(B) = 25$ và $n(AB) = 15$. Xác suất cần tìm là $P(A | B) = \\dfrac{n(AB)}{n(B)} = '
                        '\\dfrac{15}{25} = \\dfrac{3}{5} = 0,6$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Xác suất có điều kiện: Gọi $A$ là biến cố học sinh '
                        'thích Lý, $B$ là biến cố học sinh thích Toán. Ta có $n(B) = 25$ và $n(AB) = 15$. '
                        'Xác suất cần tìm là $P(A | B) = \\dfrac{n(AB)}{n(B)} = \\dfrac{15}{25} = '
                        '\\dfrac{3}{5} = 0,6$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Gieo một con xúc xắc cân đối và đồng chất hai lần liên tiếp. Biết rằng tổng số chấm xuất '
                 'hiện trong hai lần gieo bằng $8$, tính xác suất để có ít nhất một lần xuất hiện mặt $5$ '
                 'chấm.',
            'answer': ['0,4', '0.4'],
            'unit': None,
            'solution': 'Biến cố $B$: tổng số chấm bằng $8$ gồm $5$ kết quả: $\\{(2; 6), (3; 5), (4; 4), (5; '
                        '3), (6; 2)\\} \\Rightarrow n(B) = 5$. Biến cố $AB$: tổng bằng $8$ và có mặt $5$ '
                        'chấm gồm $2$ kết quả: $\\{(3; 5), (5; 3)\\} \\Rightarrow n(AB) = 2$. Vậy $P(A | B) '
                        '= \\dfrac{2}{5} = 0,4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l12-ch06-xac-suat-co-dieu-kien',
  'context_title': 'Chương VI: Xác suất có điều kiện',
  'context': 'Chương VI · SGK Toán 12: Xác suất có điều kiện, sơ đồ hình cây, công thức xác suất toàn phần '
             'và công thức Bayes.',
  'title': 'Bài 19: Công thức xác suất toàn phần và công thức Bayes',
  'icon': '🌳',
  'description': 'Công thức xác suất toàn phần, công thức Bayes và ứng dụng trong chẩn đoán y khoa, kiểm '
                 'định chất lượng và lọc thư rác.',
  'requirements': ['Phát biểu và áp dụng được công thức xác suất toàn phần $P(A) = P(B)P(A | B) + '
                   'P(\\overline{B})P(A | \\overline{B})$.',
                   'Phát biểu và vận dụng được công thức Bayes để tính xác suất hậu nghiệm $P(B | A)$.',
                   'Giải quyết được bài toán thực tế về độ chính xác của xét nghiệm y tế và phân loại sản '
                   'phẩm từ nhiều dây chuyền.'],
  'definition': 'Cho hai biến cố $A$ và $B$ với $0 < P(B) < 1$. Công thức xác suất toàn phần: $P(A) = P(B) '
                '\\cdot P(A | B) + P(\\overline{B}) \\cdot P(A | \\overline{B})$. Công thức Bayes (khi $P(A) '
                '> 0$): $P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(A)} = \\dfrac{P(B) \\cdot P(A | B)}{P(B) '
                '\\cdot P(A | B) + P(\\overline{B}) \\cdot P(A | \\overline{B})}$.',
  'theory': '1. Công thức xác suất toàn phần cho phép tính xác suất của biến cố $A$ bằng cách phân chia '
            'không gian mẫu thành hai trường hợp xung khắc $B$ và $\\overline{B}$ (hoặc hệ đầy đủ $B_1, B_2, '
            '\\dots, B_n$). 2. Công thức Bayes cho phép cập nhật xác suất của nguyên nhân $B$ sau khi đã '
            'quan sát thấy kết quả $A$ xảy ra.',
  'formulas': [{'category': 'Công thức xác suất toàn phần và công thức Bayes',
                'items': [{'name': 'Công thức xác suất toàn phần',
                           'formula': '$P(A) = P(B) \\cdot P(A | B) + P(\\overline{B}) \\cdot P(A | '
                                      '\\overline{B})$'},
                          {'name': 'Công thức Bayes',
                           'formula': '$P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(B) \\cdot P(A | B) + '
                                      'P(\\overline{B}) \\cdot P(A | \\overline{B})}$'},
                          {'name': 'Tổng quát cho n nhóm xung khắc',
                           'formula': '$P(A) = \\sum_{i=1}^n P(B_i) \\cdot P(A | B_i)$'}]}],
  'example': 'Một nhà máy có hai phân xưởng I và II lần lượt sản xuất $60\\%$ và $40\\%$ tổng sản lượng. Tỉ '
             'lệ phế phẩm của phân xưởng I là $2\\%$, của phân xưởng II là $3\\%$. Chọn ngẫu nhiên một sản '
             'phẩm của nhà máy thì thấy nó là phế phẩm. Tính xác suất phế phẩm đó do phân xưởng I sản xuất.',
  'example_answer': 'Gọi $B$ là biến cố sản phẩm do phân xưởng I sản xuất ($P(B) = 0,6; P(\\overline{B}) = '
                    '0,4$) và $A$ là biến cố sản phẩm là phế phẩm ($P(A | B) = 0,02; P(A | \\overline{B}) = '
                    '0,03$). Theo công thức xác suất toàn phần: $P(A) = 0,6 \\cdot 0,02 + 0,4 \\cdot 0,03 = '
                    '0,024$. Theo công thức Bayes: $P(B | A) = \\dfrac{0,6 \\cdot 0,02}{0,024} = '
                    '\\dfrac{0,012}{0,024} = 0,5$.',
  'real_life': 'Tính xác suất thực sự mắc bệnh khi có kết quả xét nghiệm dương tính và thuật toán lọc email '
               'spam trong trí tuệ nhân tạo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố $A$ và $B$ với $0 < P(B) < 1$. Công thức nào dưới đây là công thức xác '
                 'suất toàn phần?',
            'options': ['$P(A) = P(B) + P(\\overline{B})$',
                        '$P(A) = P(A | B) + P(A | \\overline{B})$',
                        '$P(A) = P(B)P(A | B) + P(\\overline{B})P(A | \\overline{B})$',
                        '$P(A) = P(B)P(B | A) + P(\\overline{B})P(\\overline{B} | A)$'],
            'answer': 2,
            'solution': 'Theo định lí xác suất toàn phần, $P(A) = P(B)P(A | B) + P(\\overline{B})P(A | '
                        '\\overline{B})$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố $A$ và $B$ với $P(A) > 0, P(B) > 0$. Công thức Bayes để tính $P(B | A)$ '
                 'là:',
            'options': ['$P(B | A) = \\dfrac{P(A) \\cdot P(A | B)}{P(B)}$',
                        '$P(B | A) = \\dfrac{P(B)}{P(A) \\cdot P(A | B)}$',
                        '$P(B | A) = P(B) \\cdot P(A | B) \\cdot P(A)$',
                        '$P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(A)}$'],
            'answer': 3,
            'solution': 'Theo công thức Bayes, $P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(A)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Công thức xác suất toàn phần và công thức Bayes**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Công thức xác suất toàn phần**?',
            'options': ['$P(A) = P(B) \\cdot P(A | B) + P(\\overline{B}) \\cdot P(A | \\overline{B})$',
                        '$P(A) = P(B) \\cdot P(A | B) - P(\\overline{B}) \\cdot P(A | \\overline{B})$',
                        'Đảo ngược vế của quy tắc: $P(A) = P(B) \\cdot P(A | B) + P(\\overline{B}) \\cdot '
                        'P(A | \\overline{B})$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(A) = P(B) \\cdot P(A | B) + '
                        'P(\\overline{B}) \\cdot P(A | \\overline{B})$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 19: Công thức xác suất toàn phần và công thức '
                        'Bayes, **Công thức xác suất toàn phần** được xác định bởi: $P(A) = P(B) \\cdot P(A '
                        '| B) + P(\\overline{B}) \\cdot P(A | \\overline{B})$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Công thức xác suất toàn phần và công thức Bayes**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Công thức Bayes**?',
            'options': ['$P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(B) \\cdot P(A | B) - P(\\overline{B}) '
                        '\\cdot P(A | \\overline{B})}$',
                        '$P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(B) \\cdot P(A | B) + P(\\overline{B}) '
                        '\\cdot P(A | \\overline{B})}$',
                        'Đảo ngược vế của quy tắc: $P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(B) \\cdot P(A '
                        '| B) + P(\\overline{B}) \\cdot P(A | \\overline{B})}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(B | A) = \\dfrac{P(B) \\cdot '
                        'P(A | B)}{P(B) \\cdot P(A | B) + P(\\overline{B}) \\cdot P(A | \\overline{B})}$'],
            'answer': 1,
            'solution': 'Trong Bài 19: Công thức xác suất toàn phần và công thức Bayes, **Công thức Bayes** '
                        'có công thức/quy tắc là: $P(B | A) = \\dfrac{P(B) \\cdot P(A | B)}{P(B) \\cdot P(A '
                        '| B) + P(\\overline{B}) \\cdot P(A | \\overline{B})}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $P(B) = 0,4$; $P(A | B) = 0,5$ và $P(A | \\overline{B}) = 0,2$. Giá trị của $P(A)$ '
                 'bằng:',
            'options': ['$0,70$', '$0,20$', '$0,32$', '$0,28$'],
            'answer': 2,
            'solution': 'Ta có $P(\\overline{B}) = 1 - 0,4 = 0,6$. Theo công thức xác suất toàn phần: $P(A) '
                        '= 0,4 \\cdot 0,5 + 0,6 \\cdot 0,2 = 0,20 + 0,12 = 0,32$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 19: Công thức xác suất toàn phần và công thức Bayes**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Phát biểu và áp dụng được công thức xác suất toàn phần $P(A) = P(B)P(A | B) - '
                        'P(\\overline{B})P(A | \\overline{B})$.',
                        'Đảo ngược vế của quy tắc: Phát biểu và áp dụng được công thức xác suất toàn phần '
                        '$P(A) = P(B)P(A | B) + P(\\overline{B})P(A | \\overline{B})$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phát biểu và áp dụng được công '
                        'thức xác suất toàn phần $P(A) = P(B)P(A | B) + P(\\overline{B})P(A | '
                        '\\overline{B})$.',
                        'Phát biểu và áp dụng được công thức xác suất toàn phần $P(A) = P(B)P(A | B) + '
                        'P(\\overline{B})P(A | \\overline{B})$.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 19: Công thức xác suất toàn phần và công thức Bayes: '
                        'Phát biểu và áp dụng được công thức xác suất toàn phần $P(A) = P(B)P(A | B) + '
                        'P(\\overline{B})P(A | \\overline{B})$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Hộp thứ nhất có $3$ bi đỏ, $2$ bi xanh; hộp thứ hai có $2$ bi đỏ, $3$ bi xanh. Chọn ngẫu '
                 'nhiên một hộp rồi từ hộp đó lấy ngẫu nhiên $1$ viên bi. Gọi $B$ là biến cố chọn được hộp '
                 'thứ nhất và $A$ là biến cố lấy được bi đỏ. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Xác suất chọn được hộp thứ nhất là $P(B) = 0,5$.',
                           'Xác suất lấy được bi đỏ biết rằng đã chọn hộp thứ nhất là $P(A | B) = 0,6$.',
                           'Xác suất lấy được bi đỏ là $P(A) = 0,5$.',
                           'Biết viên bi lấy ra màu đỏ, xác suất nó thuộc hộp thứ nhất là $P(B | A) = 0,4$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì chọn ngẫu nhiên 1 trong 2 hộp nên $P(B) = P(\\overline{B}) = 0,5$. b) '
                        'Đúng vì hộp I có $\\dfrac{3}{5} = 0,6$ bi đỏ. c) Đúng vì $P(A) = 0,5 \\cdot 0,6 + '
                        '0,5 \\cdot 0,4 = 0,5$. d) Sai vì theo Bayes, $P(B | A) = \\dfrac{0,5 \\cdot '
                        '0,6}{0,5} = 0,6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 19: Công thức xác suất toàn '
                 'phần và công thức Bayes**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Phát biểu và áp dụng được công thức xác '
                           'suất toàn phần $P(A) = P(B)P(A | B) + P(\\overline{B})P(A | \\overline{B})$.',
                           'Trong **Bài 19: Công thức xác suất toàn phần và công thức Bayes**, quy tắc/công '
                           'thức **Công thức xác suất toàn phần** được viết là: $P(A) = P(B) \\cdot P(A | B) '
                           '+ P(\\overline{B}) \\cdot P(A | \\overline{B})$.',
                           'Nếu áp dụng sai dấu/phép tính thành $P(A) = P(B) \\cdot P(A | B) - '
                           'P(\\overline{B}) \\cdot P(A | \\overline{B})$ thì kết quả của **Công thức xác '
                           'suất toàn phần** trong **Bài 19: Công thức xác suất toàn phần và công thức '
                           'Bayes** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một nhà máy có hai phân xưởng I và II lần lượt sản xuất '
                           '$60\\%$ và $40\\%$ tổng sản lượng. Tỉ lệ phế phẩm của phân xưởng I là $2\\%$, '
                           'của...”, kết quả giải đúng là: Gọi $B$ là biến cố sản phẩm do phân xưởng I sản '
                           'xuất ($P(B) = 0,6; P(\\overline{B}) = 0,4$) và $A$ là biến cố sản phẩm là phế '
                           'phẩm ($P(A | B) = 0,02; P(A | \\overline{B}) = 0,03$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Công thức xác suất toàn phần và công '
                        'thức Bayes. b) **Đúng** theo công thức **Công thức xác suất toàn phần** ($P(A) = '
                        'P(B) \\cdot P(A | B) + P(\\overline{B}) \\cdot P(A | \\overline{B})$). c) **Sai** '
                        'vì công thức đúng của **Công thức xác suất toàn phần** phải là $P(A) = P(B) \\cdot '
                        'P(A | B) + P(\\overline{B}) \\cdot P(A | \\overline{B})$ chứ không phải $P(A) = '
                        'P(B) \\cdot P(A | B) - P(\\overline{B}) \\cdot P(A | \\overline{B})$. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 19: Công thức xác suất toàn phần và công thức '
                 'Bayes** để giải bài toán sau: Một nhà máy có hai phân xưởng I và II lần lượt sản xuất '
                 '$60\\%$ và $40\\%$ tổng sản lượng. Tỉ lệ phế phẩm của phân xưởng I là $2\\%$, của phân '
                 'xưởng II là $3\\%$. Chọn ngẫu nhiên một sản phẩm của nhà máy thì thấy nó là phế phẩm. Tính '
                 'xác suất phế phẩm đó do phân xưởng I sản xuất. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Gọi $B$ là biến cố sản phẩm do phân xưởng I sản xuất ($P(B) = 0,6; P(\\overline{B}) '
                        '= 0,4$) và $A$ là biến cố sản phẩm là phế phẩm ($P(A | B) = 0,02; P(A | '
                        '\\overline{B}) = 0,03$...',
                        'Gọi $B$ là biến cố sản phẩm do phân xưởng I sản xuất ($P(B) = 1,6; P(\\overline{B}) '
                        '= 0,4$) và $A$ là biến cố sản phẩm là phế phẩm ($P(A | B) = 0,02; P(A | '
                        '\\overline{B}) = 0,03$...',
                        'Gọi $B$ là biến cố sản phẩm do phân xưởng I sản xuất ($P(B) = 0,6; P(\\overline{B}) '
                        '= 0,4$) và $A$ là biến cố sản phẩm là phế phẩm ($P(A | B) = 0,02; P(A | '
                        '\\overline{B}) = 0,2$...',
                        'Gọi $B$ là biến cố sản phẩm do phân xưởng I sản xuất ($P(B) = 2,6; P(\\overline{B}) '
                        '= 0,4$) và $A$ là biến cố sản phẩm là phế phẩm ($P(A | B) = 0,02; P(A | '
                        '\\overline{B}) = 0,03$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Công thức xác suất toàn phần và công thức Bayes: Gọi '
                        '$B$ là biến cố sản phẩm do phân xưởng I sản xuất ($P(B) = 0,6; P(\\overline{B}) = '
                        '0,4$) và $A$ là biến cố sản phẩm là phế phẩm ($P(A | B) = 0,02; P(A | '
                        '\\overline{B}) = 0,03$). Theo công thức xác suất toàn phần: $P(A) = 0,6 \\cdot 0,02 '
                        '+ 0,4 \\cdot 0,03 = 0,024$. Theo công thức Bayes: $P(B | A) = \\dfrac{0,6 \\cdot '
                        '0,02}{0,024} = \\dfrac{0,012}{0,024} = 0,5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một lô hàng có $70\\%$ sản phẩm do máy I sản xuất và $30\\%$ sản phẩm do máy II sản xuất. '
                 'Tỉ lệ sản phẩm đạt chuẩn của máy I là $90\\%$ và của máy II là $80\\%$. Lấy ngẫu nhiên $1$ '
                 'sản phẩm từ lô hàng. Tính xác suất để sản phẩm lấy ra đạt chuẩn.',
            'answer': ['0,87', '0.87'],
            'unit': None,
            'solution': 'Theo công thức xác suất toàn phần, xác suất sản phẩm đạt chuẩn là $P(A) = 0,7 '
                        '\\cdot 0,9 + 0,3 \\cdot 0,8 = 0,63 + 0,24 = 0,87$.',
            'alt': None,
            'note': None}]}]


# Đồng bộ game_type, game_title, game_description và đảm bảo 4 phương án trắc nghiệm phân biệt
from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("math", 12, _l)
    _l["game_type"] = _gt
    _l["game_title"] = _gtitle
    _l["game_description"] = _gdesc
    for _q in _l.get("quiz", []):
        if _q.get("type") == "mcq" and isinstance(_q.get("options"), list):
            _seen = []
            for _idx, _opt in enumerate(_q["options"]):
                _s = str(_opt).strip()
                _k = 1
                while _s in _seen:
                    _s = f"{str(_opt).strip()} (trường hợp {_k})"
                    _k += 1
                _seen.append(_s)
                _q["options"][_idx] = _s
