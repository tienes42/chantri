"""Dữ liệu bài học SGK Toán Lớp 6 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 6 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học (title).
Mỗi bài học gồm đầy đủ Yêu cầu cần đạt (requirements), Định nghĩa, Lý thuyết, Công thức, Ví dụ, Ứng dụng thực tế
và đúng 10 câu hỏi luyện tập theo 3 mức độ: 4 Nhận biết + 4 Thông hiểu + 2 Vận dụng.
"""

GRADE = 6

LESSONS = [{'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 1: Tập hợp',
  'icon': '🔢',
  'description': 'Khái niệm tập hợp, phần tử thuộc hoặc không thuộc tập hợp và hai cách mô tả một tập hợp.',
  'requirements': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) một '
                   'tập hợp.',
                   'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng cho '
                   'các phần tử.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Quan hệ phần tử – tập hợp** ($x \\in A$ '
                   '($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)) vào giải bài tập.'],
  'definition': '- Một **tập hợp** (gọi tắt là tập) bao gồm những đối tượng nhất định; các đối tượng ấy được '
                'gọi là những **phần tử** của tập hợp.\n'
                '- Kí hiệu $a \\in A$ đọc là “$a$ thuộc $A$”; $b \\notin A$ đọc là “$b$ không thuộc $A$”.',
  'theory': '### 1. Kí hiệu và cách viết tập hợp\n'
            '- Người ta thường đặt tên tập hợp bằng chữ cái in hoa ($A, B, C, \\dots$). Các phần tử của tập '
            'hợp được viết trong hai dấu ngoặc nhọn $\\{\\ \\}$, cách nhau bởi dấu “$;$” (nếu có phần tử là '
            'số) hoặc dấu “$,$”. Mỗi phần tử được liệt kê **một lần**, thứ tự liệt kê tuỳ ý.\n'
            '### 2. Hai cách mô tả một tập hợp\n'
            '- **Cách 1 (Liệt kê các phần tử)**: ví dụ $A = \\{0; 1; 2; 3; 4\\}$.\n'
            '- **Cách 2 (Chỉ ra tính chất đặc trưng)**: ví dụ $A = \\{x \\in \\mathbb{N} \\mid x < 5\\}$.',
  'formulas': [{'category': 'I. Kí hiệu và cách mô tả tập hợp',
                'items': [{'name': 'Quan hệ phần tử – tập hợp',
                           'formula': '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'},
                          {'name': 'Hai cách mô tả',
                           'formula': 'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in '
                                      '\\mathbb{N} \\mid x < 4\\}$'}]}],
  'example': 'Viết tập hợp $M$ các chữ cái trong từ “TOÁN HỌC” và cho biết số phần tử của $M$.',
  'example_answer': 'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ (chữ '
                    'O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
  'real_life': 'Lập danh sách học sinh tham gia câu lạc bộ Toán hoặc danh sách các môn học trong ngày thứ '
               'Hai.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tập hợp $A = \\{2; 4; 6; 8\\}$. Khẳng định nào sau đây là đúng?',
            'options': ['$6 \\in A$', '$3 \\in A$', '$8 \\notin A$', '$4 \\notin A$'],
            'answer': 0,
            'solution': 'Số $6$ là một phần tử của tập hợp $A$ nên $6 \\in A$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập hợp các chữ cái trong từ “SÔNG HỒNG” có bao nhiêu phần tử?',
            'options': ['$8$ phần tử', '$5$ phần tử', '$6$ phần tử', '$7$ phần tử'],
            'answer': 1,
            'solution': 'Tập hợp gồm $\\{\\text{S}, \\text{Ô}, \\text{N}, \\text{G}, \\text{H}\\}$ có $5$ '
                        'phần tử.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 1: Tập hợp**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Quan hệ phần tử – tập hợp**?',
            'options': ['Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        '$\\overline{abc} = a \\times 100 + b \\times 10 + c$ ($a \\ne 0$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$\\text{IV} = 4$, $\\text{VI} = 6$, $\\text{IX} = 9$, $\\text{XI} = 11$, '
                        '$\\text{XX} = 20$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 1: Tập hợp, **Quan hệ phần tử – tập hợp** '
                        'được xác định bởi: $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc '
                        '$A$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Tập hợp**, nội dung/biểu thức Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng '
                 '$A = \\{x \\in \\mathbb{N} \\mid x < 4\\}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quan hệ phần tử – tập hợp',
                        'Cấu tạo số tự nhiên',
                        'Quy tắc số La Mã',
                        'Hai cách mô tả'],
            'answer': 3,
            'solution': 'Trong Bài 1: Tập hợp, biểu thức/quy tắc Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc '
                        'trưng $A = \\{x \\in \\mathbb{N} \\mid x < 4\\}$ chính là nội dung của **Hai cách '
                        'mô tả**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tập hợp $B = \\{x \\in \\mathbb{N} \\mid x < 4\\}$ viết bằng cách liệt kê các phần tử là:',
            'options': ['$\\{0; 1; 2; 3\\}$',
                        '$\\{1; 2; 3\\}$',
                        '$\\{0; 1; 2; 3; 4\\}$',
                        '$\\{1; 2; 3; 4\\}$'],
            'answer': 0,
            'solution': 'Các số tự nhiên nhỏ hơn $4$ là $0; 1; 2; 3$ nên $B = \\{0; 1; 2; 3\\}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Tập hợp** (Chương I: Tập hợp các số tự nhiên), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Đọc và viết được các số tự nhiên từ $1$ đến $30$ bằng chữ số La Mã.',
                        'Biểu diễn được các số tự nhiên trên tia số và so sánh hai số tự nhiên.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 1: Tập hợp: Sử dụng được thuật ngữ tập hợp, phần tử '
                        'thuộc ($\\in$) hoặc không thuộc ($\\notin$) một tập hợp.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tập hợp $P = \\{1; 3; 5; 7; 9\\}$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$5 \\in P$',
                           '$2 \\in P$',
                           'Tập hợp $P$ có $5$ phần tử',
                           '$P$ là tập hợp các số tự nhiên lẻ nhỏ hơn $10$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $5$ thuộc $P$. b) Sai vì $2 \\notin P$. c) Đúng vì $P$ có $5$ phần tử. '
                        'd) Đúng vì $1; 3; 5; 7; 9$ là các số tự nhiên lẻ nhỏ hơn $10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 1: Tập hợp**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Sử dụng được thuật ngữ tập hợp, '
                           'phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) một tập hợp.',
                           'Quy tắc/công thức **Quan hệ phần tử – tập hợp** trong bài được xác định bởi: $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$).',
                           'Trong mọi trường hợp, **Quan hệ phần tử – tập hợp** luôn được tính bằng công '
                           'thức $\\overline{abc} = a \\times 100 + b \\times 10 + c$ ($a \\ne 0$) (thuộc '
                           'Cấu tạo số tự nhiên) mà không cần điều kiện của Bài 1: Tập hợp.',
                           'Với bài toán minh họa: “Viết tập hợp $M$ các chữ cái trong từ “TOÁN HỌC” và cho '
                           'biết số phần tử của $M$.”, lời giải đúng là: Ta có $M = \\{\\text{T}, \\text{O}, '
                           '\\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ (chữ O xuất hiện $2$ lần nhưng '
                           'chỉ viết $1$ lần). Tập hợp $M$ có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Tập hợp. b) **Đúng** theo công thức '
                        'trọng tâm **Quan hệ phần tử – tập hợp** ($x \\in A$ ($x$ thuộc $A$); $y \\notin A$ '
                        '($y$ không thuộc $A$)). c) **Sai** vì $\\overline{abc} = a \\times 100 + b \\times '
                        '10 + c$ ($a \\ne 0$) là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Quan hệ phần tử – tập hợp**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 1: Tập hợp** để giải quyết tình huống sau: Viết tập hợp $M$ các '
                 'chữ cái trong từ “TOÁN HỌC” và cho biết số phần tử của $M$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Nhóm các cặp số tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = 600$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Tập hợp: Ta có $M = \\{\\text{T}, \\text{O}, '
                        '\\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ (chữ O xuất hiện $2$ lần nhưng chỉ '
                        'viết $1$ lần). Tập hợp $M$ có $6$ phần tử.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tập hợp $A$ gồm các số tự nhiên chẵn nhỏ hơn $10$. Hỏi tập hợp $A$ có bao nhiêu phần '
                 'tử?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $A = \\{0; 2; 4; 6; 8\\}$ nên tập hợp $A$ có $5$ phần tử.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 2: Cách ghi số tự nhiên',
  'icon': '🔢',
  'description': 'Tập hợp số tự nhiên, cách ghi số tự nhiên trong hệ thập phân và cách đọc, viết số La Mã từ '
                 '1 đến 30.',
  'requirements': ['Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng chữ '
                   'số của số tự nhiên trong hệ thập phân.',
                   'Đọc và viết được các số tự nhiên từ $1$ đến $30$ bằng chữ số La Mã.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Cấu tạo số tự nhiên** ($\\overline{abc} = a '
                   '\\times 100 + b \\times 10 + c$ ($a \\ne 0$)) vào giải bài tập.'],
  'definition': '- Tập hợp các số tự nhiên: $\\mathbb{N} = \\{0; 1; 2; 3; \\dots\\}$; tập hợp các số tự '
                'nhiên khác $0$: $\\mathbb{N}^* = \\{1; 2; 3; \\dots\\}$.\n'
                '- Trong hệ thập phân: $\\overline{ab} = a \\times 10 + b$; $\\overline{abc} = a \\times 100 '
                '+ b \\times 10 + c$ (với $a \\ne 0$).\n'
                '- Chữ số La Mã cơ bản: $\\text{I} = 1$, $\\text{V} = 5$, $\\text{X} = 10$, $\\text{IV} = '
                '4$, $\\text{IX} = 9$.',
  'theory': '### 1. Hệ thập phân\n'
            '- Cứ $10$ đơn vị ở một hàng thì làm thành $1$ đơn vị ở hàng liền trước nó. Ví dụ: $2045 = 2 '
            '\\times 1000 + 0 \\times 100 + 4 \\times 10 + 5$.\n'
            '### 2. Số La Mã từ 1 đến 30\n'
            '- Mỗi chữ số $\\text{I}, \\text{X}$ không viết liền nhau quá $3$ lần. Ví dụ: $\\text{XIV} = '
            '14$, $\\text{XIX} = 19$, $\\text{XXIV} = 24$, $\\text{XXIX} = 29$.',
  'formulas': [{'category': 'I. Cấu tạo thập phân và Số La Mã',
                'items': [{'name': 'Cấu tạo số tự nhiên',
                           'formula': '$\\overline{abc} = a \\times 100 + b \\times 10 + c$ ($a \\ne 0$)'},
                          {'name': 'Quy tắc số La Mã',
                           'formula': '$\\text{IV} = 4$, $\\text{VI} = 6$, $\\text{IX} = 9$, $\\text{XI} = '
                                      '11$, $\\text{XX} = 20$'}]}],
  'example': 'Viết số $27$ và $19$ bằng chữ số La Mã; viết số $\\overline{ab}$ dưới dạng tổng các hàng.',
  'example_answer': 'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có $\\overline{ab} = '
                    'a \\times 10 + b$.',
  'real_life': 'Đọc số giờ trên mặt đồng hồ La Mã và số thứ tự các chương sách, thế kỉ lịch sử.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số La Mã $\\text{XXIV}$ có giá trị trong hệ thập phân là:',
            'options': ['$26$', '$24$', '$16$', '$14$'],
            'answer': 1,
            'solution': 'Ta có $\\text{XX} = 20$ và $\\text{IV} = 4$ nên $\\text{XXIV} = 24$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khẳng định nào sau đây là đúng?',
            'options': ['$0 \\in \\mathbb{N}^*$',
                        '$0 \\notin \\mathbb{N}$',
                        '$0 \\in \\mathbb{N}$',
                        '$1 \\notin \\mathbb{N}^*$'],
            'answer': 2,
            'solution': 'Số $0$ là số tự nhiên nên $0 \\in \\mathbb{N}$ (nhưng $0 \\notin \\mathbb{N}^*$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 2: Cách ghi số tự nhiên**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Cấu tạo số tự nhiên**?',
            'options': ['$\\text{IV} = 4$, $\\text{VI} = 6$, $\\text{IX} = 9$, $\\text{XI} = 11$, '
                        '$\\text{XX} = 20$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        '$\\overline{abc} = a \\times 100 + b \\times 10 + c$ ($a \\ne 0$)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 2: Cách ghi số tự nhiên, **Cấu tạo số tự '
                        'nhiên** được xác định bởi: $\\overline{abc} = a \\times 100 + b \\times 10 + c$ ($a '
                        '\\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Cách ghi số tự nhiên**, nội dung/biểu thức $\\text{IV} = 4$, $\\text{VI} = '
                 '6$, $\\text{IX} = 9$, $\\text{XI} = 11$, $\\text{XX} = 20$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Quy tắc số La Mã',
                        'Cấu tạo số tự nhiên',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 2: Cách ghi số tự nhiên, biểu thức/quy tắc $\\text{IV} = 4$, $\\text{VI} '
                        '= 6$, $\\text{IX} = 9$, $\\text{XI} = 11$, $\\text{XX} = 20$ chính là nội dung của '
                        '**Quy tắc số La Mã**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong số tự nhiên $35\\,708$, giá trị của chữ số $5$ gấp mấy lần giá trị của chữ số $5$ '
                 'trong số $1520$?',
            'options': ['$100$ lần', '$10$ lần', '$5$ lần', '$1000$ lần'],
            'answer': 1,
            'solution': 'Trong $35\\,708$ chữ số $5$ có giá trị $5000$; trong $1520$ chữ số $5$ có giá trị '
                        '$500$. Ta có $5000 : 500 = 10$ lần.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Cách ghi số tự nhiên** (Chương I: Tập hợp các số tự nhiên), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Biểu diễn được các số tự nhiên trên tia số và so sánh hai số tự nhiên.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 2: Cách ghi số tự nhiên: Phân biệt được tập hợp '
                        '$\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng chữ số của số tự nhiên '
                        'trong hệ thập phân.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét cách ghi số tự nhiên và số La Mã. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Số $\\text{XIX}$ biểu diễn số $19$',
                           '$\\overline{abc} = a + b + c$',
                           'Số tự nhiên nhỏ nhất trong $\\mathbb{N}^*$ là $1$',
                           'Số $28$ viết bằng chữ số La Mã là $\\text{XXVIII}$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng ($10 + 9 = 19$). b) Sai vì $\\overline{abc} = 100a + 10b + c$. c) Đúng vì '
                        '$\\mathbb{N}^* = \\{1; 2; 3; \\dots\\}$. d) Đúng ($20 + 8 = 28$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 2: Cách ghi số tự '
                 'nhiên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phân biệt được tập hợp '
                           '$\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng chữ số của số tự '
                           'nhiên trong hệ thập phân.',
                           'Quy tắc/công thức **Cấu tạo số tự nhiên** trong bài được xác định bởi: '
                           '$\\overline{abc} = a \\times 100 + b \\times 10 + c$ ($a \\ne 0$).',
                           'Trong mọi trường hợp, **Cấu tạo số tự nhiên** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 2: Cách ghi số tự nhiên.',
                           'Với bài toán minh họa: “Viết số $27$ và $19$ bằng chữ số La Mã; viết số '
                           '$\\overline{ab}$ dưới dạng tổng các hàng.”, lời giải đúng là: Số $27$ viết là '
                           '$\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có $\\overline{ab} = a '
                           '\\times 10 + b$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Cách ghi số tự nhiên. b) **Đúng** theo '
                        'công thức trọng tâm **Cấu tạo số tự nhiên** ($\\overline{abc} = a \\times 100 + b '
                        '\\times 10 + c$ ($a \\ne 0$)). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin '
                        'A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung '
                        'của **Cấu tạo số tự nhiên**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 2: Cách ghi số tự nhiên** để giải quyết tình huống sau: Viết số '
                 '$27$ và $19$ bằng chữ số La Mã; viết số $\\overline{ab}$ dưới dạng tổng các hàng. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Nhóm các cặp số tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = 600$.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Cách ghi số tự nhiên: Số $27$ viết là '
                        '$\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có $\\overline{ab} = a \\times '
                        '10 + b$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Khi viết thêm chữ số $3$ vào bên trái một số tự nhiên có hai chữ số thì số đó tăng thêm '
                 'bao nhiêu đơn vị?',
            'answer': ['300'],
            'unit': None,
            'solution': 'Ta có $\\overline{3ab} = 300 + \\overline{ab}$ nên số đó tăng thêm $300$ đơn vị.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 3: Thứ tự trong tập hợp các số tự nhiên',
  'icon': '🔢',
  'description': 'Thứ tự trên tia số, số liền trước, số liền sau và tính chất bắc cầu của quan hệ thứ tự.',
  'requirements': ['Biểu diễn được các số tự nhiên trên tia số và so sánh hai số tự nhiên.',
                   'Tìm được số liền trước, số liền sau và liệt kê các phần tử của tập hợp xác định bởi bất '
                   'đẳng thức.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Số liền trước và liền sau** (Liền trước của '
                   '$n$ ($n \\ge 1$) là $n - 1$; liền sau của $n$ là $n + 1$) vào giải bài tập.'],
  'definition': '- Trong hai số tự nhiên khác nhau, luôn có một số nhỏ hơn số kia. Nếu $a < b$ thì trên tia '
                'số nằm ngang, điểm $a$ nằm **bên trái** điểm $b$.\n'
                '- Số $n + 1$ là **số liền sau** của $n$; số $n - 1$ (với $n \\in \\mathbb{N}^*$) là **số '
                'liền trước** của $n$. Số $0$ không có số tự nhiên liền trước.',
  'theory': '### 1. Tia số và tính chất bắc cầu\n'
            '- Mỗi số tự nhiên được biểu diễn bởi một điểm trên tia số; điểm $0$ là gốc của tia số.\n'
            '- Tính chất bắc cầu: nếu $a < b$ và $b < c$ thì $a < c$.\n'
            '### 2. Kí hiệu $\\le$ và $\\ge$\n'
            '- $a \\le b$ nghĩa là $a < b$ hoặc $a = b$. Ví dụ: $\\{x \\in \\mathbb{N} \\mid 3 \\le x < 7\\} '
            '= \\{3; 4; 5; 6\\}$.',
  'formulas': [{'category': 'I. Quan hệ thứ tự trong N',
                'items': [{'name': 'Số liền trước và liền sau',
                           'formula': 'Liền trước của $n$ ($n \\ge 1$) là $n - 1$; liền sau của $n$ là $n + '
                                      '1$'},
                          {'name': 'Ba số tự nhiên liên tiếp',
                           'formula': '$n - 1;\\ n;\\ n + 1$ (với $n \\in \\mathbb{N}^*$)'}]}],
  'example': 'Viết tập hợp $A = \\{x \\in \\mathbb{N} \\mid 4 \\le x \\le 8\\}$ bằng cách liệt kê các phần '
             'tử.',
  'example_answer': 'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
  'real_life': 'Đánh số nhà liên tiếp trên phố, số ghế trong rạp chiếu phim và sắp xếp thứ tự chiều cao.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số tự nhiên liền trước của số $100$ là:',
            'options': ['$101$', '$98$', '$99$', '$90$'],
            'answer': 2,
            'solution': 'Số liền trước của $n$ là $n - 1 = 100 - 1 = 99$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 3 \\le x < 7\\}$ viết bằng cách liệt kê các phần '
                 'tử là:',
            'options': ['$\\{3; 4; 5; 6; 7\\}$',
                        '$\\{4; 5; 6\\}$',
                        '$\\{4; 5; 6; 7\\}$',
                        '$\\{3; 4; 5; 6\\}$'],
            'answer': 3,
            'solution': 'Vì $3 \\le x < 7$ nên $x$ nhận các giá trị $3; 4; 5; 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 3: Thứ tự trong tập hợp các số tự nhiên**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Số liền trước và liền sau**?',
            'options': ['Liền trước của $n$ ($n \\ge 1$) là $n - 1$; liền sau của $n$ là $n + 1$',
                        '$n - 1;\\ n;\\ n + 1$ (với $n \\in \\mathbb{N}^*$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 3: Thứ tự trong tập hợp các số tự nhiên, **Số '
                        'liền trước và liền sau** được xác định bởi: Liền trước của $n$ ($n \\ge 1$) là $n - '
                        '1$; liền sau của $n$ là $n + 1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Thứ tự trong tập hợp các số tự nhiên**, nội dung/biểu thức $n - 1;\\ n;\\ n '
                 '+ 1$ (với $n \\in \\mathbb{N}^*$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số liền trước và liền sau',
                        'Ba số tự nhiên liên tiếp',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 3: Thứ tự trong tập hợp các số tự nhiên, biểu thức/quy tắc $n - 1;\\ n;\\ '
                        'n + 1$ (với $n \\in \\mathbb{N}^*$) chính là nội dung của **Ba số tự nhiên liên '
                        'tiếp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho ba số tự nhiên liên tiếp tăng dần là $m;\\ 15;\\ n$. Khi đó tổng $m + n$ bằng:',
            'options': ['$29$', '$31$', '$30$', '$16$'],
            'answer': 2,
            'solution': 'Ta có $m = 14$ và $n = 16$, suy ra $m + n = 14 + 16 = 30$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Thứ tự trong tập hợp các số tự nhiên** (Chương I: Tập hợp các số tự '
                 'nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Biểu diễn được các số tự nhiên trên tia số và so sánh hai số tự nhiên.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 3: Thứ tự trong tập hợp các số tự nhiên: Biểu diễn '
                        'được các số tự nhiên trên tia số và so sánh hai số tự nhiên.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét thứ tự trong tập hợp các số tự nhiên $\\mathbb{N}$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Số $0$ là số tự nhiên nhỏ nhất',
                           'Mọi số tự nhiên đều có số tự nhiên liền trước',
                           'Trên tia số nằm ngang, điểm $5$ nằm bên trái điểm $8$',
                           'Có $4$ số tự nhiên $x$ thỏa mãn $2 < x \\le 6$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì số $0$ không có số tự nhiên liền trước. c) Đúng vì $5 < 8$. d) '
                        'Đúng, đó là $3; 4; 5; 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 3: Thứ tự trong tập hợp '
                 'các số tự nhiên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Biểu diễn được các số tự nhiên '
                           'trên tia số và so sánh hai số tự nhiên.',
                           'Quy tắc/công thức **Số liền trước và liền sau** trong bài được xác định bởi: '
                           'Liền trước của $n$ ($n \\ge 1$) là $n - 1$; liền sau của $n$ là $n + 1$.',
                           'Trong mọi trường hợp, **Số liền trước và liền sau** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 3: Thứ tự trong tập hợp các '
                           'số tự nhiên.',
                           'Với bài toán minh họa: “Viết tập hợp $A = \\{x \\in \\mathbb{N} \\mid 4 \\le x '
                           '\\le 8\\}$ bằng cách liệt kê các phần tử.”, lời giải đúng là: Các số tự nhiên từ '
                           '$4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Thứ tự trong tập hợp các số tự nhiên. '
                        'b) **Đúng** theo công thức trọng tâm **Số liền trước và liền sau** (Liền trước của '
                        '$n$ ($n \\ge 1$) là $n - 1$; liền sau của $n$ là $n + 1$). c) **Sai** vì $x \\in A$ '
                        '($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung '
                        'khác, không phải quy tắc chung của **Số liền trước và liền sau**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 3: Thứ tự trong tập hợp các số tự nhiên** để giải quyết tình '
                 'huống sau: Viết tập hợp $A = \\{x \\in \\mathbb{N} \\mid 4 \\le x \\le 8\\}$ bằng cách '
                 'liệt kê các phần tử. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Nhóm các cặp số tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = 600$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Thứ tự trong tập hợp các số tự nhiên: Các số tự nhiên '
                        'từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tổng của ba số tự nhiên liên tiếp bằng $63$. Tìm số lớn nhất trong ba số đó.',
            'answer': ['22'],
            'unit': None,
            'solution': 'Số ở giữa là $63 : 3 = 21$. Ba số là $20; 21; 22$, vậy số lớn nhất là $22$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 4: Phép cộng và phép trừ số tự nhiên',
  'icon': '🔢',
  'description': 'Phép cộng, phép trừ số tự nhiên, các tính chất của phép cộng và điều kiện thực hiện phép '
                 'trừ.',
  'requirements': ['Vận dụng tính chất giao hoán và kết hợp của phép cộng để tính nhẩm, tính hợp lí.',
                   'Nắm được điều kiện thực hiện phép trừ trong $\\mathbb{N}$ ($a \\ge b$) và giải bài toán '
                   'tìm $x$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Giao hoán, kết hợp** ($a + b = b + a$; $(a '
                   '+ b) + c = a + (b + c)$) vào giải bài tập.'],
  'definition': '- Phép cộng: $a + b = c$ ($a, b$ là các **số hạng**, $c$ là **tổng**).\n'
                '- Phép trừ: nếu có số tự nhiên $x$ sao cho $b + x = a$ thì ta có phép trừ $a - b = x$ ($a$: '
                'số bị trừ, $b$: số trừ, $x$: hiệu). Điều kiện để thực hiện được trong $\\mathbb{N}$ là $a '
                '\\ge b$.',
  'theory': '### 1. Tính chất của phép cộng\n'
            '- Giao hoán: $a + b = b + a$.\n'
            '- Kết hợp: $(a + b) + c = a + (b + c)$.\n'
            '- Cộng với số $0$: $a + 0 = 0 + a = a$.\n'
            '### 2. Mối quan hệ giữa phép cộng và phép trừ\n'
            '- Số hạng chưa biết $=$ Tổng $-$ Số hạng đã biết; Số bị trừ $=$ Hiệu $+$ Số trừ; Số trừ $=$ Số '
            'bị trừ $-$ Hiệu.',
  'formulas': [{'category': 'I. Tính chất và quy tắc tìm x',
                'items': [{'name': 'Giao hoán, kết hợp',
                           'formula': '$a + b = b + a$; $(a + b) + c = a + (b + c)$'},
                          {'name': 'Tìm thành phần chưa biết',
                           'formula': '$x + b = c \\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - '
                                      'c$'}]}],
  'example': 'Tính một cách hợp lí: $135 + 360 + 65 + 40$.',
  'example_answer': 'Nhóm các cặp số tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = 600$.',
  'real_life': 'Tính tổng quãng đường di chuyển qua nhiều chặng và số tiền còn dư sau khi mua hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép trừ $45 - 18 = 27$, số $18$ được gọi là:',
            'options': ['Số bị trừ', 'Hiệu', 'Số hạng', 'Số trừ'],
            'answer': 3,
            'solution': 'Trong $a - b = c$ thì $a$ là số bị trừ, $b$ là số trừ, $c$ là hiệu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính hợp lí tổng $47 + 185 + 53$ ta được:',
            'options': ['$285$', '$275$', '$295$', '$265$'],
            'answer': 0,
            'solution': 'Nhóm $(47 + 53) + 185 = 100 + 185 = 285$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 4: Phép cộng và phép trừ số tự nhiên**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Giao hoán, kết hợp**?',
            'options': ['$x + b = c \\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$',
                        '$a + b = b + a$; $(a + b) + c = a + (b + c)$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 4: Phép cộng và phép trừ số tự nhiên, **Giao '
                        'hoán, kết hợp** được xác định bởi: $a + b = b + a$; $(a + b) + c = a + (b + c)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Phép cộng và phép trừ số tự nhiên**, nội dung/biểu thức $x + b = c '
                 '\\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Giao hoán, kết hợp',
                        'Quan hệ phần tử – tập hợp',
                        'Tìm thành phần chưa biết',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 4: Phép cộng và phép trừ số tự nhiên, biểu thức/quy tắc $x + b = c '
                        '\\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$ chính là nội dung của '
                        '**Tìm thành phần chưa biết**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số tự nhiên $x$ biết $124 - (x - 16) = 80$:',
            'options': ['$x = 28$', '$x = 44$', '$x = 188$', '$x = 60$'],
            'answer': 3,
            'solution': 'Ta có $x - 16 = 124 - 80 = 44 \\Rightarrow x = 44 + 16 = 60$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Phép cộng và phép trừ số tự nhiên** (Chương I: Tập hợp các số tự nhiên), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Vận dụng tính chất giao hoán và kết hợp của phép cộng để tính nhẩm, tính hợp lí.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 4: Phép cộng và phép trừ số tự nhiên: Vận dụng tính '
                        'chất giao hoán và kết hợp của phép cộng để tính nhẩm, tính hợp lí.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Với mọi số tự nhiên $a, b$ ($a \\ge b$), mỗi khẳng định sau đúng hay sai?',
            'statements': ['$a + 0 = a$',
                           '$a - a = 0$',
                           '$a - 0 = 0$',
                           'Phép trừ $b - a$ luôn thực hiện được trong $\\mathbb{N}$ khi $a > b$'],
            'answer': [True, True, False, False],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì $a - 0 = a$. d) Sai vì trong $\\mathbb{N}$ phép trừ chỉ '
                        'thực hiện được khi số bị trừ lớn hơn hoặc bằng số trừ.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 4: Phép cộng và phép '
                 'trừ số tự nhiên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Vận dụng tính chất giao hoán và '
                           'kết hợp của phép cộng để tính nhẩm, tính hợp lí.',
                           'Quy tắc/công thức **Giao hoán, kết hợp** trong bài được xác định bởi: $a + b = b '
                           '+ a$; $(a + b) + c = a + (b + c)$.',
                           'Trong mọi trường hợp, **Giao hoán, kết hợp** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 4: Phép cộng và phép trừ số tự '
                           'nhiên.',
                           'Với bài toán minh họa: “Tính một cách hợp lí: $135 + 360 + 65 + 40$.”, lời giải '
                           'đúng là: Nhóm các cặp số tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = '
                           '600$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Phép cộng và phép trừ số tự nhiên. b) '
                        '**Đúng** theo công thức trọng tâm **Giao hoán, kết hợp** ($a + b = b + a$; $(a + b) '
                        '+ c = a + (b + c)$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ '
                        'không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Giao hoán, kết hợp**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 4: Phép cộng và phép trừ số tự nhiên** để giải quyết tình huống '
                 'sau: Tính một cách hợp lí: $135 + 360 + 65 + 40$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Nhóm các cặp số tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = 600$.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Phép cộng và phép trừ số tự nhiên: Nhóm các cặp số '
                        'tròn trăm: $(135 + 65) + (360 + 40) = 200 + 400 = 600$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thư viện có $2450$ quyển sách. Đầu năm học thư viện nhập thêm $550$ quyển và cho mượn '
                 '$680$ quyển. Hỏi trong thư viện còn lại bao nhiêu quyển sách?',
            'answer': ['2320'],
            'unit': None,
            'solution': 'Số sách còn lại là $(2450 + 550) - 680 = 3000 - 680 = 2320$ (quyển).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 5: Phép nhân và phép chia số tự nhiên',
  'icon': '🔢',
  'description': 'Phép nhân, phép chia hết và phép chia có dư trong tập hợp số tự nhiên.',
  'requirements': ['Vận dụng tính chất giao hoán, kết hợp và phân phối của phép nhân đối với phép cộng để '
                   'tính hợp lí.',
                   'Nắm vững công thức phép chia có dư $a = b \\cdot q + r$ ($0 \\le r < b$) và giải bài '
                   'toán thực tế.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tính chất phân phối** ($a \\cdot (b + c) = '
                   'a \\cdot b + a \\cdot c$; $a \\cdot (b - c) = a \\cdot b - a \\cdot c$) vào giải bài '
                   'tập.'],
  'definition': '- Phép nhân: $a \\cdot b = c$ ($a, b$: thừa số; $c$: tích). Trong tích chứa chữ, ta có thể '
                'bỏ dấu nhân: $a \\cdot b = ab$.\n'
                '- Với hai số tự nhiên $a$ và $b$ ($b \\ne 0$), luôn tìm được duy nhất hai số tự nhiên $q$ '
                '(thương) và $r$ (số dư) sao cho $a = b \\cdot q + r$, trong đó $0 \\le r < b$.',
  'theory': '### 1. Tính chất của phép nhân\n'
            '- Giao hoán: $a \\cdot b = b \\cdot a$. Kết hợp: $(a \\cdot b) \\cdot c = a \\cdot (b \\cdot '
            'c)$.\n'
            '- Nhân với $1$ và $0$: $a \\cdot 1 = a$; $a \\cdot 0 = 0$.\n'
            '- Phân phối đối với phép cộng/trừ: $a \\cdot (b \\pm c) = a \\cdot b \\pm a \\cdot c$.\n'
            '### 2. Phép chia hết và phép chia có dư\n'
            '- Nếu $r = 0$ thì $a = b \\cdot q$ là phép chia hết ($a : b = q$). Nếu $r \\ne 0$ thì đó là '
            'phép chia có dư.',
  'formulas': [{'category': 'I. Tính chất phép nhân và Phép chia có dư',
                'items': [{'name': 'Tính chất phân phối',
                           'formula': '$a \\cdot (b + c) = a \\cdot b + a \\cdot c$; $a \\cdot (b - c) = a '
                                      '\\cdot b - a \\cdot c$'},
                          {'name': 'Phép chia có dư',
                           'formula': '$a = b \\cdot q + r$ với $0 \\le r < b$ ($b \\ne 0$)'}]}],
  'example': 'Tính nhanh: $25 \\cdot 37 \\cdot 4$ và tìm thương, số dư khi chia $47$ cho $5$.',
  'example_answer': 'Ta có $(25 \\cdot 4) \\cdot 37 = 100 \\cdot 37 = 3700$. Vì $47 = 5 \\cdot 9 + 2$ nên '
                    'thương là $9$ và số dư là $2$.',
  'real_life': 'Tính số xe ô tô tối thiểu cần thuê để chở hết số học sinh đi tham quan.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính hợp lí tích $25 \\cdot 37 \\cdot 4$ ta được kết quả là:',
            'options': ['$3700$', '$370$', '$740$', '$37\\,000$'],
            'answer': 0,
            'solution': 'Nhóm $(25 \\cdot 4) \\cdot 37 = 100 \\cdot 37 = 3700$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép chia $47$ cho $5$, số dư là:',
            'options': ['$1$', '$2$', '$3$', '$4$'],
            'answer': 1,
            'solution': 'Vì $47 = 5 \\cdot 9 + 2$ nên thương là $9$ và số dư là $2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 5: Phép nhân và phép chia số tự nhiên**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Tính chất phân phối**?',
            'options': ['$a = b \\cdot q + r$ với $0 \\le r < b$ ($b \\ne 0$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$a \\cdot (b + c) = a \\cdot b + a \\cdot c$; $a \\cdot (b - c) = a \\cdot b - a '
                        '\\cdot c$',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 5: Phép nhân và phép chia số tự nhiên, **Tính '
                        'chất phân phối** được xác định bởi: $a \\cdot (b + c) = a \\cdot b + a \\cdot c$; '
                        '$a \\cdot (b - c) = a \\cdot b - a \\cdot c$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Phép nhân và phép chia số tự nhiên**, nội dung/biểu thức $a = b \\cdot q + '
                 'r$ với $0 \\le r < b$ ($b \\ne 0$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tính chất phân phối',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả',
                        'Phép chia có dư'],
            'answer': 3,
            'solution': 'Trong Bài 5: Phép nhân và phép chia số tự nhiên, biểu thức/quy tắc $a = b \\cdot q '
                        '+ r$ với $0 \\le r < b$ ($b \\ne 0$) chính là nội dung của **Phép chia có dư**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một phép chia có số chia là $8$, thương là $12$ và số dư là số dư lớn nhất có thể. Số bị '
                 'chia là:',
            'options': ['$103$', '$96$', '$104$', '$97$'],
            'answer': 0,
            'solution': 'Số dư lớn nhất khi chia cho $8$ là $7$. Số bị chia là $8 \\cdot 12 + 7 = 103$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Phép nhân và phép chia số tự nhiên** (Chương I: Tập hợp các số tự nhiên), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Vận dụng tính chất giao hoán, kết hợp và phân phối của phép nhân đối với phép cộng '
                        'để tính hợp lí.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 5: Phép nhân và phép chia số tự nhiên: Vận dụng tính '
                        'chất giao hoán, kết hợp và phân phối của phép nhân đối với phép cộng để tính hợp '
                        'lí.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phép chia số tự nhiên $47$ cho $5$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Thương của phép chia là $9$',
                           'Số dư của phép chia là $3$',
                           'Ta viết được $47 = 5 \\cdot 9 + 2$',
                           'Số dư trong phép chia cho $5$ có thể bằng $5$'],
            'answer': [True, False, True, False],
            'solution': 'Vì $47 = 5 \\cdot 9 + 2$ nên a) Đúng, b) Sai (dư $2$), c) Đúng, d) Sai vì số dư '
                        'luôn nhỏ hơn số chia ($0 \\le r < 5$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 5: Phép nhân và phép '
                 'chia số tự nhiên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Vận dụng tính chất giao hoán, kết '
                           'hợp và phân phối của phép nhân đối với phép cộng để tính hợp lí.',
                           'Quy tắc/công thức **Tính chất phân phối** trong bài được xác định bởi: $a \\cdot '
                           '(b + c) = a \\cdot b + a \\cdot c$; $a \\cdot (b - c) = a \\cdot b - a \\cdot '
                           'c$.',
                           'Trong mọi trường hợp, **Tính chất phân phối** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 5: Phép nhân và phép chia số tự '
                           'nhiên.',
                           'Với bài toán minh họa: “Tính nhanh: $25 \\cdot 37 \\cdot 4$ và tìm thương, số dư '
                           'khi chia $47$ cho $5$.”, lời giải đúng là: Ta có $(25 \\cdot 4) \\cdot 37 = 100 '
                           '\\cdot 37 = 3700$. Vì $47 = 5 \\cdot 9 + 2$ nên thương là $9$ và số dư là $2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Phép nhân và phép chia số tự nhiên. b) '
                        '**Đúng** theo công thức trọng tâm **Tính chất phân phối** ($a \\cdot (b + c) = a '
                        '\\cdot b + a \\cdot c$; $a \\cdot (b - c) = a \\cdot b - a \\cdot c$). c) **Sai** '
                        'vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của '
                        'nội dung khác, không phải quy tắc chung của **Tính chất phân phối**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 5: Phép nhân và phép chia số tự nhiên** để giải quyết tình huống '
                 'sau: Tính nhanh: $25 \\cdot 37 \\cdot 4$ và tìm thương, số dư khi chia $47$ cho $5$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Ta có $(25 \\cdot 4) \\cdot 37 = 100 \\cdot 37 = 3700$. Vì $47 = 5 \\cdot 9 + 2$ '
                        'nên thương là $9$ và số dư là $2$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Phép nhân và phép chia số tự nhiên: Ta có $(25 \\cdot '
                        '4) \\cdot 37 = 100 \\cdot 37 = 3700$. Vì $47 = 5 \\cdot 9 + 2$ nên thương là $9$ và '
                        'số dư là $2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một trường có $1245$ học sinh đi tham quan bằng xe ô tô $45$ chỗ ngồi (mỗi học sinh ngồi '
                 '$1$ chỗ). Cần thuê ít nhất bao nhiêu xe để chở hết số học sinh đó?',
            'answer': ['28'],
            'unit': None,
            'solution': 'Ta có $1245 = 45 \\cdot 27 + 30$. Vì $27$ xe chở được $1215$ em, còn dư $30$ em cần '
                        'thêm $1$ xe nữa nên cần ít nhất $28$ xe.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 6: Luỹ thừa với số mũ tự nhiên',
  'icon': '🔢',
  'description': 'Định nghĩa luỹ thừa với số mũ tự nhiên, bình phương, lập phương và quy tắc nhân, chia hai '
                 'luỹ thừa cùng cơ số.',
  'requirements': ['Viết và tính được giá trị của luỹ thừa với số mũ tự nhiên; nhận biết cơ số và số mũ.',
                   'Thực hiện đúng phép nhân và phép chia hai luỹ thừa cùng cơ số.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Định nghĩa và quy ước** ($a^n = a \\cdot a '
                   '\\cdots a$ ($n$ thừa số); $a^1 = a$; $a^0 = 1$ ($a \\ne 0$)) vào giải bài tập.'],
  'definition': '- **Luỹ thừa bậc $n$ của $a$**, kí hiệu $a^n$, là tích của $n$ thừa số bằng nhau, mỗi thừa '
                'số bằng $a$: $a^n = \\underbrace{a \\cdot a \\cdots a}_{n\\text{ thừa số}}$ ($n \\in '
                '\\mathbb{N}^*$), trong đó $a$ là **cơ số**, $n$ là **số mũ**.\n'
                '- Quy ước: $a^1 = a$ và $a^0 = 1$ (với $a \\ne 0$).',
  'theory': '### 1. Bình phương và lập phương\n'
            '- $a^2$ còn gọi là **$a$ bình phương**; $a^3$ còn gọi là **$a$ lập phương**.\n'
            '### 2. Nhân và chia hai luỹ thừa cùng cơ số\n'
            '- Khi **nhân** hai luỹ thừa cùng cơ số, ta giữ nguyên cơ số và **cộng** các số mũ: $a^m \\cdot '
            'a^n = a^{m+n}$.\n'
            '- Khi **chia** hai luỹ thừa cùng cơ số (khác $0$), ta giữ nguyên cơ số và **trừ** các số mũ: '
            '$a^m : a^n = a^{m-n}$ ($a \\ne 0, m \\ge n$).',
  'formulas': [{'category': 'I. Các công thức luỹ thừa',
                'items': [{'name': 'Định nghĩa và quy ước',
                           'formula': '$a^n = a \\cdot a \\cdots a$ ($n$ thừa số); $a^1 = a$; $a^0 = 1$ ($a '
                                      '\\ne 0$)'},
                          {'name': 'Nhân hai luỹ thừa cùng cơ số', 'formula': '$a^m \\cdot a^n = a^{m+n}$'},
                          {'name': 'Chia hai luỹ thừa cùng cơ số',
                           'formula': '$a^m : a^n = a^{m-n}$ ($a \\ne 0, m \\ge n$)'}]}],
  'example': 'Viết kết quả dưới dạng một luỹ thừa và tính giá trị: $2^3 \\cdot 2^4$ và $5^6 : 5^4$.',
  'example_answer': 'Ta có $2^3 \\cdot 2^4 = 2^{3+4} = 2^7 = 128$ và $5^6 : 5^4 = 5^{6-4} = 5^2 = 25$.',
  'real_life': 'Biểu diễn sự nhân đôi của vi khuẩn theo từng giờ hoặc dung lượng bộ nhớ máy tính ($2^{10} = '
               '1024\\text{ byte}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của luỹ thừa $2^5$ bằng:',
            'options': ['$10$', '$32$', '$25$', '$7$'],
            'answer': 1,
            'solution': 'Ta có $2^5 = 2 \\cdot 2 \\cdot 2 \\cdot 2 \\cdot 2 = 32$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $7^8 : 7^6$ viết dưới dạng một luỹ thừa là:',
            'options': ['$7^{14}$', '$1^2$', '$7^2$', '$7^{48}$'],
            'answer': 2,
            'solution': 'Theo quy tắc chia hai luỹ thừa cùng cơ số: $7^8 : 7^6 = 7^{8-6} = 7^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 6: Luỹ thừa với số mũ tự nhiên**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Định nghĩa và quy ước**?',
            'options': ['$a^m \\cdot a^n = a^{m+n}$',
                        '$a^m : a^n = a^{m-n}$ ($a \\ne 0, m \\ge n$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$a^n = a \\cdot a \\cdots a$ ($n$ thừa số); $a^1 = a$; $a^0 = 1$ ($a \\ne 0$)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 6: Luỹ thừa với số mũ tự nhiên, **Định nghĩa '
                        'và quy ước** được xác định bởi: $a^n = a \\cdot a \\cdots a$ ($n$ thừa số); $a^1 = '
                        'a$; $a^0 = 1$ ($a \\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Luỹ thừa với số mũ tự nhiên**, nội dung/biểu thức $a^m \\cdot a^n = '
                 'a^{m+n}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Nhân hai luỹ thừa cùng cơ số',
                        'Định nghĩa và quy ước',
                        'Chia hai luỹ thừa cùng cơ số',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 0,
            'solution': 'Trong Bài 6: Luỹ thừa với số mũ tự nhiên, biểu thức/quy tắc $a^m \\cdot a^n = '
                        'a^{m+n}$ chính là nội dung của **Nhân hai luỹ thừa cùng cơ số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số tự nhiên $n$ biết $3^n = 81$:',
            'options': ['$n = 3$', '$n = 4$', '$n = 9$', '$n = 27$'],
            'answer': 1,
            'solution': 'Vì $81 = 3 \\cdot 3 \\cdot 3 \\cdot 3 = 3^4$ nên $n = 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Luỹ thừa với số mũ tự nhiên** (Chương I: Tập hợp các số tự nhiên), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Viết và tính được giá trị của luỹ thừa với số mũ tự nhiên; nhận biết cơ số và số '
                        'mũ.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 6: Luỹ thừa với số mũ tự nhiên: Viết và tính được giá '
                        'trị của luỹ thừa với số mũ tự nhiên; nhận biết cơ số và số mũ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các phép tính về luỹ thừa. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$3^4 = 81$', '$2^3 \\cdot 2^2 = 2^6$', '$10^0 = 1$', '$5^7 : 5^7 = 1$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng ($3^4 = 81$). b) Sai vì $2^3 \\cdot 2^2 = 2^{3+2} = 2^5$. c) Đúng theo quy '
                        'ước $a^0 = 1$. d) Đúng vì $5^7 : 5^7 = 5^0 = 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 6: Luỹ thừa với số mũ '
                 'tự nhiên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Viết và tính được giá trị của luỹ '
                           'thừa với số mũ tự nhiên; nhận biết cơ số và số mũ.',
                           'Quy tắc/công thức **Định nghĩa và quy ước** trong bài được xác định bởi: $a^n = '
                           'a \\cdot a \\cdots a$ ($n$ thừa số); $a^1 = a$; $a^0 = 1$ ($a \\ne 0$).',
                           'Trong mọi trường hợp, **Định nghĩa và quy ước** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 6: Luỹ thừa với số mũ tự nhiên.',
                           'Với bài toán minh họa: “Viết kết quả dưới dạng một luỹ thừa và tính giá trị: '
                           '$2^3 \\cdot 2^4$ và $5^6 : 5^4$.”, lời giải đúng là: Ta có $2^3 \\cdot 2^4 = '
                           '2^{3+4} = 2^7 = 128$ và $5^6 : 5^4 = 5^{6-4} = 5^2 = 25$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Luỹ thừa với số mũ tự nhiên. b) '
                        '**Đúng** theo công thức trọng tâm **Định nghĩa và quy ước** ($a^n = a \\cdot a '
                        '\\cdots a$ ($n$ thừa số); $a^1 = a$; $a^0 = 1$ ($a \\ne 0$)). c) **Sai** vì $x \\in '
                        'A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung '
                        'khác, không phải quy tắc chung của **Định nghĩa và quy ước**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 6: Luỹ thừa với số mũ tự nhiên** để giải quyết tình huống sau: '
                 'Viết kết quả dưới dạng một luỹ thừa và tính giá trị: $2^3 \\cdot 2^4$ và $5^6 : 5^4$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Ta có $2^3 \\cdot 2^4 = 2^{3+4} = 2^7 = 128$ và $5^6 : 5^4 = 5^{6-4} = 5^2 = 25$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Luỹ thừa với số mũ tự nhiên: Ta có $2^3 \\cdot 2^4 = '
                        '2^{3+4} = 2^7 = 128$ và $5^6 : 5^4 = 5^{6-4} = 5^2 = 25$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một loại vi khuẩn cứ sau mỗi giờ lại phân đôi (số lượng tăng gấp đôi). Ban đầu có $1$ con '
                 'vi khuẩn, hỏi sau $8$ giờ có bao nhiêu con vi khuẩn?',
            'answer': ['256'],
            'unit': None,
            'solution': 'Sau $8$ giờ số vi khuẩn là $2^8 = 256$ (con).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch01-tap-hop-cac-so-tu-nhien',
  'context_title': 'Chương I: Tập hợp các số tự nhiên',
  'context': 'Chương I · SGK Toán 6: Tập hợp, các phép tính và lũy thừa trong tập hợp số tự nhiên.',
  'title': 'Bài 7: Thứ tự thực hiện các phép tính',
  'icon': '🔢',
  'description': 'Quy tắc về thứ tự thực hiện các phép tính đối với biểu thức không có dấu ngoặc và biểu '
                 'thức có dấu ngoặc.',
  'requirements': ['Thực hiện đúng thứ tự phép tính: Luỹ thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ '
                   'Cộng và trừ.',
                   'Thực hiện đúng thứ tự dấu ngoặc: Ngoặc tròn $( ) \\rightarrow$ Ngoặc vuông $[ ] '
                   '\\rightarrow$ Ngoặc nhọn $\\{ \\}$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Không có ngoặc** ($\\text{Luỹ thừa} '
                   '\\rightarrow \\text{Nhân, chia} \\rightarrow \\text{Cộng, trừ}$) vào giải bài tập.'],
  'definition': '- Đối với biểu thức **không có dấu ngoặc**: **Luỹ thừa $\\rightarrow$ Nhân và chia '
                '$\\rightarrow$ Cộng và trừ** (nếu chỉ có cộng, trừ hoặc chỉ có nhân, chia thì thực hiện từ '
                'trái sang phải).\n'
                '- Đối với biểu thức **có dấu ngoặc**: thực hiện theo thứ tự **$( ) \\rightarrow [ ] '
                '\\rightarrow \\{ \\}$**.',
  'theory': '### 1. Biểu thức không có dấu ngoặc\n'
            '- Ví dụ: $5 \\cdot 2^3 - 18 : 3^2 = 5 \\cdot 8 - 18 : 9 = 40 - 2 = 38$.\n'
            '### 2. Biểu thức có dấu ngoặc\n'
            '- Ví dụ: $100 : \\{2 \\cdot [52 - (35 - 8)]\\} = 100 : \\{2 \\cdot [52 - 27]\\} = 100 : \\{2 '
            '\\cdot 25\\} = 100 : 50 = 2$.',
  'formulas': [{'category': 'I. Thứ tự ưu tiên',
                'items': [{'name': 'Không có ngoặc',
                           'formula': '$\\text{Luỹ thừa} \\rightarrow \\text{Nhân, chia} \\rightarrow '
                                      '\\text{Cộng, trừ}$'},
                          {'name': 'Có dấu ngoặc',
                           'formula': '$(\\ ) \\rightarrow [\\ ] \\rightarrow \\{\\ \\}$'}]}],
  'example': 'Tính giá trị của biểu thức: $180 - 4 \\cdot 5^2$.',
  'example_answer': 'Tính luỹ thừa trước: $5^2 = 25$. Nhân: $4 \\cdot 25 = 100$. Trừ: $180 - 100 = 80$.',
  'real_life': 'Lập biểu thức tính tổng số tiền thanh toán khi mua nhiều loại sản phẩm với số lượng và đơn '
               'giá khác nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đối với biểu thức không có dấu ngoặc, thứ tự thực hiện các phép tính đúng là:',
            'options': ['Nhân chia $\\rightarrow$ Luỹ thừa $\\rightarrow$ Cộng trừ',
                        'Cộng trừ $\\rightarrow$ Nhân chia $\\rightarrow$ Luỹ thừa',
                        'Luỹ thừa $\\rightarrow$ Nhân chia $\\rightarrow$ Cộng trừ',
                        'Thực hiện từ trái sang phải bất kì'],
            'answer': 2,
            'solution': 'Thứ tự đúng là: Luỹ thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $180 - 4 \\cdot 5^2$ là:',
            'options': ['$4400$', '$155$', '$3900$', '$80$'],
            'answer': 3,
            'solution': 'Ta có $5^2 = 25 \\Rightarrow 4 \\cdot 25 = 100 \\Rightarrow 180 - 100 = 80$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 7: Thứ tự thực hiện các phép tính**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Không có ngoặc**?',
            'options': ['$\\text{Luỹ thừa} \\rightarrow \\text{Nhân, chia} \\rightarrow \\text{Cộng, trừ}$',
                        '$(\\ ) \\rightarrow [\\ ] \\rightarrow \\{\\ \\}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 7: Thứ tự thực hiện các phép tính, **Không có '
                        'ngoặc** được xác định bởi: $\\text{Luỹ thừa} \\rightarrow \\text{Nhân, chia} '
                        '\\rightarrow \\text{Cộng, trừ}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Thứ tự thực hiện các phép tính**, nội dung/biểu thức $(\\ ) \\rightarrow '
                 '[\\ ] \\rightarrow \\{\\ \\}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Không có ngoặc', 'Có dấu ngoặc', 'Quan hệ phần tử – tập hợp', 'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 7: Thứ tự thực hiện các phép tính, biểu thức/quy tắc $(\\ ) \\rightarrow '
                        '[\\ ] \\rightarrow \\{\\ \\}$ chính là nội dung của **Có dấu ngoặc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $36 : [18 - 3 \\cdot (2^2 + 1)]$ bằng:',
            'options': ['$4$', '$6$', '$12$', '$9$'],
            'answer': 2,
            'solution': 'Trong ngoặc tròn: $2^2 + 1 = 5$; ngoặc vuông: $18 - 3 \\cdot 5 = 3$; ngoài ngoặc: '
                        '$36 : 3 = 12$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Thứ tự thực hiện các phép tính** (Chương I: Tập hợp các số tự nhiên), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Thực hiện đúng thứ tự phép tính: Luỹ thừa $\\rightarrow$ Nhân và chia '
                        '$\\rightarrow$ Cộng và trừ.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 7: Thứ tự thực hiện các phép tính: Thực hiện đúng thứ '
                        'tự phép tính: Luỹ thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét biểu thức $A = 5 \\cdot 2^3 - 18 : 3^2$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Phép tính cần thực hiện đầu tiên là tính $2^3$ và $3^2$',
                           '$2^3 = 6$ và $3^2 = 6$',
                           '$5 \\cdot 2^3 = 40$ và $18 : 3^2 = 2$',
                           'Giá trị của biểu thức $A$ bằng $38$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì $2^3 = 8$ và $3^2 = 9$. c) Đúng ($5 \\cdot 8 = 40, 18 : 9 = 2$). '
                        'd) Đúng ($40 - 2 = 38$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 7: Thứ tự thực hiện các '
                 'phép tính**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện đúng thứ tự phép tính: '
                           'Luỹ thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ.',
                           'Quy tắc/công thức **Không có ngoặc** trong bài được xác định bởi: $\\text{Luỹ '
                           'thừa} \\rightarrow \\text{Nhân, chia} \\rightarrow \\text{Cộng, trừ}$.',
                           'Trong mọi trường hợp, **Không có ngoặc** luôn được tính bằng công thức $x \\in '
                           'A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 7: Thứ tự thực hiện các phép tính.',
                           'Với bài toán minh họa: “Tính giá trị của biểu thức: $180 - 4 \\cdot 5^2$.”, lời '
                           'giải đúng là: Tính luỹ thừa trước: $5^2 = 25$. Nhân: $4 \\cdot 25 = 100$. Trừ: '
                           '$180 - 100 = 80$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Thứ tự thực hiện các phép tính. b) '
                        '**Đúng** theo công thức trọng tâm **Không có ngoặc** ($\\text{Luỹ thừa} '
                        '\\rightarrow \\text{Nhân, chia} \\rightarrow \\text{Cộng, trừ}$). c) **Sai** vì $x '
                        '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Không có ngoặc**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 7: Thứ tự thực hiện các phép tính** để giải quyết tình huống sau: '
                 'Tính giá trị của biểu thức: $180 - 4 \\cdot 5^2$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Tính luỹ thừa trước: $5^2 = 25$. Nhân: $4 \\cdot 25 = 100$. Trừ: $180 - 100 = 80$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Thứ tự thực hiện các phép tính: Tính luỹ thừa trước: '
                        '$5^2 = 25$. Nhân: $4 \\cdot 25 = 100$. Trừ: $180 - 100 = 80$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tự nhiên $x$ biết $5 \\cdot (x + 3) - 12 = 2^3 \\cdot 6$.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Ta có $2^3 \\cdot 6 = 8 \\cdot 6 = 48 \\Rightarrow 5 \\cdot (x + 3) = 48 + 12 = 60 '
                        '\\Rightarrow x + 3 = 12 \\Rightarrow x = 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch02-tinh-chia-het',
  'context_title': 'Chương II: Tính chia hết trong tập hợp các số tự nhiên',
  'context': 'Chương II · SGK Toán 6: Quan hệ chia hết, dấu hiệu chia hết, số nguyên tố, ƯCLN và BCNN.',
  'title': 'Bài 8: Quan hệ chia hết và tính chất',
  'icon': '➗',
  'description': 'Khái niệm chia hết, ước và bội của một số tự nhiên và tính chất chia hết của một tổng.',
  'requirements': ['Nhận biết được quan hệ chia hết ($a \\vdots b$), tìm được tập hợp các ước $\\text{Ư}(a)$ '
                   'và các bội $\\text{B}(b)$.',
                   'Vận dụng tính chất chia hết của một tổng để xét xem một tổng (hiệu) có chia hết cho một '
                   'số hay không.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Định nghĩa** ($a \\vdots b \\Leftrightarrow '
                   'a = b \\cdot k$ ($k \\in \\mathbb{N}, b \\ne 0$)) vào giải bài tập.'],
  'definition': '- Cho hai số tự nhiên $a$ và $b$ ($b \\ne 0$). Nếu có số tự nhiên $k$ sao cho $a = b \\cdot '
                'k$ thì ta nói $a$ **chia hết** cho $b$ (kí hiệu $a \\vdots b$); nếu không, ta viết $a '
                '\\not\\vdots b$.\n'
                '- Khi $a \\vdots b$, ta nói $a$ là **bội** của $b$ và $b$ là **ước** của $a$.',
  'theory': '### 1. Cách tìm ước và bội\n'
            '- Muốn tìm các ước của $a$ ($a > 1$), ta lần lượt chia $a$ cho các số tự nhiên từ $1$ đến $a$; '
            'các phép chia hết cho ta ước của $a$.\n'
            '- Muốn tìm các bội của $b$ ($b \\ne 0$), ta nhân $b$ lần lượt với $0; 1; 2; 3; \\dots$\n'
            '### 2. Tính chất chia hết của một tổng\n'
            '- Tính chất 1: Nếu $a \\vdots m$ và $b \\vdots m$ thì $(a + b) \\vdots m$ và $(a - b) \\vdots '
            'm$ (với $a \\ge b$).\n'
            '- Tính chất 2: Nếu $a \\vdots m$ và $b \\not\\vdots m$ thì $(a + b) \\not\\vdots m$.',
  'formulas': [{'category': 'I. Quan hệ chia hết và Tính chất',
                'items': [{'name': 'Định nghĩa',
                           'formula': '$a \\vdots b \\Leftrightarrow a = b \\cdot k$ ($k \\in \\mathbb{N}, b '
                                      '\\ne 0$)'},
                          {'name': 'Tính chất 1',
                           'formula': '$a \\vdots m$ và $b \\vdots m \\Rightarrow (a \\pm b) \\vdots m$'},
                          {'name': 'Tính chất 2',
                           'formula': '$a \\vdots m$ và $b \\not\\vdots m \\Rightarrow (a + b) \\not\\vdots '
                                      'm$'}]}],
  'example': 'Tìm tập hợp $\\text{Ư}(12)$ và không thực hiện phép cộng, hãy xét xem tổng $24 + 36$ có chia '
             'hết cho $6$ không.',
  'example_answer': 'Ta có $\\text{Ư}(12) = \\{1; 2; 3; 4; 6; 12\\}$. Vì $24 \\vdots 6$ và $36 \\vdots 6$ '
                    'nên $(24 + 36) \\vdots 6$.',
  'real_life': 'Xét xem có thể chia đều số kẹo trong các túi vào các đĩa mà không cần mở túi hay không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tập hợp tất cả các ước tự nhiên của $8$ là:',
            'options': ['$\\{1; 2; 4\\}$', '$\\{0; 1; 2; 4; 8\\}$', '$\\{2; 4; 8\\}$', '$\\{1; 2; 4; 8\\}$'],
            'answer': 3,
            'solution': 'Các số tự nhiên mà $8$ chia hết là $1; 2; 4; 8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số nào sau đây là bội của $7$?',
            'options': ['$28$', '$17$', '$32$', '$1$'],
            'answer': 0,
            'solution': 'Vì $28 = 7 \\cdot 4$ nên $28 \\vdots 7$, tức $28$ là bội của $7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 8: Quan hệ chia hết và tính chất**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Định nghĩa**?',
            'options': ['$a \\vdots m$ và $b \\vdots m \\Rightarrow (a \\pm b) \\vdots m$',
                        '$a \\vdots b \\Leftrightarrow a = b \\cdot k$ ($k \\in \\mathbb{N}, b \\ne 0$)',
                        '$a \\vdots m$ và $b \\not\\vdots m \\Rightarrow (a + b) \\not\\vdots m$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 8: Quan hệ chia hết và tính chất, **Định '
                        'nghĩa** được xác định bởi: $a \\vdots b \\Leftrightarrow a = b \\cdot k$ ($k \\in '
                        '\\mathbb{N}, b \\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Quan hệ chia hết và tính chất**, nội dung/biểu thức $a \\vdots m$ và $b '
                 '\\vdots m \\Rightarrow (a \\pm b) \\vdots m$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Định nghĩa', 'Tính chất 2', 'Tính chất 1', 'Quan hệ phần tử – tập hợp'],
            'answer': 2,
            'solution': 'Trong Bài 8: Quan hệ chia hết và tính chất, biểu thức/quy tắc $a \\vdots m$ và $b '
                        '\\vdots m \\Rightarrow (a \\pm b) \\vdots m$ chính là nội dung của **Tính chất '
                        '1**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tổng $S = 35 + 49 + x$ (với $x \\in \\mathbb{N}$). Điều kiện để $S \\vdots 7$ là:',
            'options': ['$x$ chia cho $7$ dư $1$', '$x$ là số chẵn', '$x \\not\\vdots 7$', '$x \\vdots 7$'],
            'answer': 3,
            'solution': 'Vì $35 \\vdots 7$ và $49 \\vdots 7$ nên để $(35 + 49 + x) \\vdots 7$ thì $x$ phải '
                        'chia hết cho $7$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Quan hệ chia hết và tính chất** (Chương II: Tính chia hết trong tập hợp '
                 'các số tự nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được quan hệ chia hết ($a \\vdots b$), tìm được tập hợp các ước '
                        '$\\text{Ư}(a)$ và các bội $\\text{B}(b)$.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 8: Quan hệ chia hết và tính chất: Nhận biết được quan '
                        'hệ chia hết ($a \\vdots b$), tìm được tập hợp các ước $\\text{Ư}(a)$ và các bội '
                        '$\\text{B}(b)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét quan hệ chia hết trong $\\mathbb{N}$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Số $1$ là ước của mọi số tự nhiên',
                           'Số $0$ là bội của mọi số tự nhiên khác $0$',
                           'Tổng $40 + 16 + 7$ chia hết cho $8$',
                           'Tập hợp $\\text{Ư}(12)$ có $6$ phần tử'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $0 = b \\cdot 0$. c) Sai vì $40 \\vdots 8, 16 \\vdots 8$ nhưng '
                        '$7 \\not\\vdots 8$. d) Đúng ($\\{1; 2; 3; 4; 6; 12\\}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 8: Quan hệ chia hết và '
                 'tính chất**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được quan hệ chia hết '
                           '($a \\vdots b$), tìm được tập hợp các ước $\\text{Ư}(a)$ và các bội '
                           '$\\text{B}(b)$.',
                           'Quy tắc/công thức **Định nghĩa** trong bài được xác định bởi: $a \\vdots b '
                           '\\Leftrightarrow a = b \\cdot k$ ($k \\in \\mathbb{N}, b \\ne 0$).',
                           'Trong mọi trường hợp, **Định nghĩa** luôn được tính bằng công thức $x \\in A$ '
                           '($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 8: Quan hệ chia hết và tính chất.',
                           'Với bài toán minh họa: “Tìm tập hợp $\\text{Ư}(12)$ và không thực hiện phép '
                           'cộng, hãy xét xem tổng $24 + 36$ có chia hết cho $6$ không.”, lời giải đúng là: '
                           'Ta có $\\text{Ư}(12) = \\{1; 2; 3; 4; 6; 12\\}$. Vì $24 \\vdots 6$ và $36 '
                           '\\vdots 6$ nên $(24 + 36) \\vdots 6$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Quan hệ chia hết và tính chất. b) '
                        '**Đúng** theo công thức trọng tâm **Định nghĩa** ($a \\vdots b \\Leftrightarrow a = '
                        'b \\cdot k$ ($k \\in \\mathbb{N}, b \\ne 0$)). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Định nghĩa**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 8: Quan hệ chia hết và tính chất** để giải quyết tình huống sau: '
                 'Tìm tập hợp $\\text{Ư}(12)$ và không thực hiện phép cộng, hãy xét xem tổng $24 + 36$ có '
                 'chia hết cho $6$ không. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Ta có $\\text{Ư}(12) = \\{1; 2; 3; 4; 6; 12\\}$. Vì $24 \\vdots 6$ và $36 \\vdots '
                        '6$ nên $(24 + 36) \\vdots 6$.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Quan hệ chia hết và tính chất: Ta có $\\text{Ư}(12) = '
                        '\\{1; 2; 3; 4; 6; 12\\}$. Vì $24 \\vdots 6$ và $36 \\vdots 6$ nên $(24 + 36) '
                        '\\vdots 6$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu số tự nhiên là bội của $9$ đồng thời lớn hơn $10$ và nhỏ hơn $50$?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Các bội của $9$ trong khoảng từ $10$ đến $50$ là $18; 27; 36; 45$ nên có $4$ số.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch02-tinh-chia-het',
  'context_title': 'Chương II: Tính chia hết trong tập hợp các số tự nhiên',
  'context': 'Chương II · SGK Toán 6: Quan hệ chia hết, dấu hiệu chia hết, số nguyên tố, ƯCLN và BCNN.',
  'title': 'Bài 9: Dấu hiệu chia hết',
  'icon': '➗',
  'description': 'Dấu hiệu chia hết cho 2, cho 5, cho 9 và cho 3 trong tập hợp các số tự nhiên.',
  'requirements': ['Vận dụng dấu hiệu chia hết cho $2$ và cho $5$ dựa vào chữ số tận cùng.',
                   'Vận dụng dấu hiệu chia hết cho $9$ và cho $3$ dựa vào tổng các chữ số.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Chia hết cho 2 và 5** (Cho $2$: tận cùng '
                   '$\\in \\{0; 2; 4; 6; 8\\}$; Cho $5$: tận cùng $\\in \\{0; 5\\}$) vào giải bài tập.'],
  'definition': '- **Chia hết cho $2$**: các số có chữ số tận cùng là $0; 2; 4; 6; 8$.\n'
                '- **Chia hết cho $5$**: các số có chữ số tận cùng là $0$ hoặc $5$.\n'
                '- **Chia hết cho $9$ (hoặc cho $3$)**: các số có **tổng các chữ số** chia hết cho $9$ (hoặc '
                'cho $3$).',
  'theory': '### 1. Dấu hiệu theo chữ số tận cùng\n'
            '- Số chia hết cho cả $2$ và $5$ thì có chữ số tận cùng là $0$ (tức là chia hết cho $10$).\n'
            '### 2. Dấu hiệu theo tổng các chữ số\n'
            '- Mọi số chia hết cho $9$ thì đều chia hết cho $3$, nhưng một số chia hết cho $3$ chưa chắc đã '
            'chia hết cho $9$ (ví dụ $15 \\vdots 3$ nhưng $15 \\not\\vdots 9$).',
  'formulas': [{'category': 'I. Tóm tắt dấu hiệu chia hết',
                'items': [{'name': 'Chia hết cho 2 và 5',
                           'formula': 'Cho $2$: tận cùng $\\in \\{0; 2; 4; 6; 8\\}$; Cho $5$: tận cùng $\\in '
                                      '\\{0; 5\\}$'},
                          {'name': 'Chia hết cho 3 và 9',
                           'formula': '$\\overline{abc} \\vdots 3 \\Leftrightarrow (a + b + c) \\vdots 3$; '
                                      '$\\overline{abc} \\vdots 9 \\Leftrightarrow (a + b + c) \\vdots '
                                      '9$'}]}],
  'example': 'Tìm chữ số $x$ để số $\\overline{45x0}$ chia hết cho cả $2, 5$ và $9$.',
  'example_answer': 'Số $\\overline{45x0}$ có tận cùng là $0$ nên luôn chia hết cho $2$ và $5$. Để '
                    '$\\overline{45x0} \\vdots 9$ thì $(4 + 5 + x + 0) = 9 + x \\vdots 9$, suy ra $x \\in '
                    '\\{0; 9\\}$.',
  'real_life': 'Kiểm tra nhanh một số tiền hoặc số lượng sản phẩm có chia đều được cho $3, 5$ hay $9$ người '
               'không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số nào dưới đây chia hết cho cả $2$ và $5$?',
            'options': ['$250$', '$125$', '$252$', '$205$'],
            'answer': 0,
            'solution': 'Số chia hết cho cả $2$ và $5$ phải có chữ số tận cùng là $0$, đó là $250$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số nào dưới đây chia hết cho $9$?',
            'options': ['$3125$', '$4518$', '$2024$', '$1001$'],
            'answer': 1,
            'solution': 'Tổng các chữ số của $4518$ là $4 + 5 + 1 + 8 = 18 \\vdots 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 9: Dấu hiệu chia hết**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Chia hết cho 2 và 5**?',
            'options': ['$\\overline{abc} \\vdots 3 \\Leftrightarrow (a + b + c) \\vdots 3$; '
                        '$\\overline{abc} \\vdots 9 \\Leftrightarrow (a + b + c) \\vdots 9$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Cho $2$: tận cùng $\\in \\{0; 2; 4; 6; 8\\}$; Cho $5$: tận cùng $\\in \\{0; 5\\}$',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 9: Dấu hiệu chia hết, **Chia hết cho 2 và 5** '
                        'được xác định bởi: Cho $2$: tận cùng $\\in \\{0; 2; 4; 6; 8\\}$; Cho $5$: tận cùng '
                        '$\\in \\{0; 5\\}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Dấu hiệu chia hết**, nội dung/biểu thức $\\overline{abc} \\vdots 3 '
                 '\\Leftrightarrow (a + b + c) \\vdots 3$; $\\overline{abc} \\vdots 9 \\Leftrightarrow (a + '
                 'b + c) \\vdots 9$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Chia hết cho 2 và 5',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả',
                        'Chia hết cho 3 và 9'],
            'answer': 3,
            'solution': 'Trong Bài 9: Dấu hiệu chia hết, biểu thức/quy tắc $\\overline{abc} \\vdots 3 '
                        '\\Leftrightarrow (a + b + c) \\vdots 3$; $\\overline{abc} \\vdots 9 '
                        '\\Leftrightarrow (a + b + c) \\vdots 9$ chính là nội dung của **Chia hết cho 3 và '
                        '9**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm chữ số $a$ để số $\\overline{2a5}$ chia hết cho $3$ nhưng không chia hết cho $9$:',
            'options': ['$a = 5$', '$a = 2$', '$a = 1$', '$a = 0$'],
            'answer': 0,
            'solution': 'Tổng chữ số là $7 + a$. Với $a = 5$ thì $7 + 5 = 12 \\vdots 3$ và $12 \\not\\vdots '
                        '9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Dấu hiệu chia hết** (Chương II: Tính chia hết trong tập hợp các số tự '
                 'nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Vận dụng dấu hiệu chia hết cho $2$ và cho $5$ dựa vào chữ số tận cùng.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 9: Dấu hiệu chia hết: Vận dụng dấu hiệu chia hết cho '
                        '$2$ và cho $5$ dựa vào chữ số tận cùng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho số tự nhiên $n = 2340$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$n$ chia hết cho cả $2$ và $5$',
                           '$n$ chia hết cho $9$',
                           '$n$ không chia hết cho $3$',
                           'Tổng $n + 45$ chia hết cho $9$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng (tận cùng $0$). b) Đúng ($2 + 3 + 4 + 0 = 9 \\vdots 9$). c) Sai vì $n '
                        '\\vdots 9 \\Rightarrow n \\vdots 3$. d) Đúng vì $n \\vdots 9$ và $45 \\vdots 9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 9: Dấu hiệu chia hết**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Vận dụng dấu hiệu chia hết cho $2$ '
                           'và cho $5$ dựa vào chữ số tận cùng.',
                           'Quy tắc/công thức **Chia hết cho 2 và 5** trong bài được xác định bởi: Cho $2$: '
                           'tận cùng $\\in \\{0; 2; 4; 6; 8\\}$; Cho $5$: tận cùng $\\in \\{0; 5\\}$.',
                           'Trong mọi trường hợp, **Chia hết cho 2 và 5** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 9: Dấu hiệu chia hết.',
                           'Với bài toán minh họa: “Tìm chữ số $x$ để số $\\overline{45x0}$ chia hết cho cả '
                           '$2, 5$ và $9$.”, lời giải đúng là: Số $\\overline{45x0}$ có tận cùng là $0$ nên '
                           'luôn chia hết cho $2$ và $5$. Để $\\overline{45x0} \\vdots 9$ thì $(4 + 5 + x + '
                           '0) = 9 + x \\vdots 9$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Dấu hiệu chia hết. b) **Đúng** theo '
                        'công thức trọng tâm **Chia hết cho 2 và 5** (Cho $2$: tận cùng $\\in \\{0; 2; 4; 6; '
                        '8\\}$; Cho $5$: tận cùng $\\in \\{0; 5\\}$). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Chia hết cho 2 và 5**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 9: Dấu hiệu chia hết** để giải quyết tình huống sau: Tìm chữ số '
                 '$x$ để số $\\overline{45x0}$ chia hết cho cả $2, 5$ và $9$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Số $\\overline{45x0}$ có tận cùng là $0$ nên luôn chia hết cho $2$ và $5$. Để '
                        '$\\overline{45x0} \\vdots 9$ thì $(4 + 5 + x + 0) = 9 + x \\vdots 9$, suy ra $x '
                        '\\in \\{0; 9\\}$...',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Dấu hiệu chia hết: Số $\\overline{45x0}$ có tận cùng '
                        'là $0$ nên luôn chia hết cho $2$ và $5$. Để $\\overline{45x0} \\vdots 9$ thì $(4 + '
                        '5 + x + 0) = 9 + x \\vdots 9$, suy ra $x \\in \\{0; 9\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm chữ số $x$ để số $\\overline{27x}$ chia hết cho cả $2, 5$ và $9$.',
            'answer': ['0'],
            'unit': None,
            'solution': 'Để $\\overline{27x}$ chia hết cho cả $2$ và $5$ thì chữ số tận cùng phải là $x = '
                        '0$. Khi đó $2 + 7 + 0 = 9 \x0b'
                        'dots 9$ (thỏa mãn).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch02-tinh-chia-het',
  'context_title': 'Chương II: Tính chia hết trong tập hợp các số tự nhiên',
  'context': 'Chương II · SGK Toán 6: Quan hệ chia hết, dấu hiệu chia hết, số nguyên tố, ƯCLN và BCNN.',
  'title': 'Bài 10: Số nguyên tố',
  'icon': '➗',
  'description': 'Khái niệm số nguyên tố, hợp số và cách phân tích một số tự nhiên lớn hơn 1 ra thừa số '
                 'nguyên tố.',
  'requirements': ['Nhận biết được số nguyên tố và hợp số; thuộc các số nguyên tố nhỏ hơn $20$.',
                   'Phân tích được một số tự nhiên lớn hơn $1$ ra thừa số nguyên tố bằng sơ đồ cây hoặc sơ '
                   'đồ cột.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Số nguyên tố chẵn duy nhất** (Số $2$) vào '
                   'giải bài tập.'],
  'definition': '- **Số nguyên tố** là số tự nhiên lớn hơn $1$, chỉ có hai ước là $1$ và chính nó.\n'
                '- **Hợp số** là số tự nhiên lớn hơn $1$, có nhiều hơn hai ước. Chú ý: số $0$ và số $1$ '
                '**không là số nguyên tố** và cũng **không là hợp số**.',
  'theory': '### 1. Các số nguyên tố nhỏ cần nhớ\n'
            '- Các số nguyên tố nhỏ hơn $20$: $2; 3; 5; 7; 11; 13; 17; 19$. Số $2$ là số nguyên tố **chẵn '
            'duy nhất**.\n'
            '### 2. Phân tích một số ra thừa số nguyên tố\n'
            '- Mọi hợp số đều phân tích được duy nhất ra tích các thừa số nguyên tố (viết gọn bằng luỹ '
            'thừa). Ví dụ: $36 = 2^2 \\cdot 3^2$; $120 = 2^3 \\cdot 3 \\cdot 5$.',
  'formulas': [{'category': 'I. Số nguyên tố và phân tích thừa số nguyên tố',
                'items': [{'name': 'Số nguyên tố chẵn duy nhất', 'formula': 'Số $2$'},
                          {'name': 'Ví dụ phân tích chuẩn',
                           'formula': '$24 = 2^3 \\cdot 3$; $36 = 2^2 \\cdot 3^2$; $60 = 2^2 \\cdot 3 \\cdot '
                                      '5$'}]}],
  'example': 'Phân tích số $84$ ra thừa số nguyên tố và cho biết các ước nguyên tố của $84$.',
  'example_answer': 'Ta có $84 = 2^2 \\cdot 3 \\cdot 7$. Các ước nguyên tố của $84$ là $2; 3; 7$.',
  'real_life': 'Ứng dụng số nguyên tố trong mật mã học, bảo mật thông tin và tìm ước chung, bội chung.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số nào trong các số sau đây là số nguyên tố?',
            'options': ['$1$', '$17$', '$9$', '$21$'],
            'answer': 1,
            'solution': 'Số $17$ chỉ có hai ước là $1$ và $17$ nên là số nguyên tố.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân tích số $36$ ra thừa số nguyên tố ta được:',
            'options': ['$4 \\cdot 9$', '$6^2$', '$2^2 \\cdot 3^2$', '$2 \\cdot 18$'],
            'answer': 2,
            'solution': 'Các thừa số phải là số nguyên tố: $36 = 2^2 \\cdot 3^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 10: Số nguyên tố**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Số nguyên tố chẵn duy nhất**?',
            'options': ['$24 = 2^3 \\cdot 3$; $36 = 2^2 \\cdot 3^2$; $60 = 2^2 \\cdot 3 \\cdot 5$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        'Số $2$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 10: Số nguyên tố, **Số nguyên tố chẵn duy '
                        'nhất** được xác định bởi: Số $2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Số nguyên tố**, nội dung/biểu thức $24 = 2^3 \\cdot 3$; $36 = 2^2 \\cdot '
                 '3^2$; $60 = 2^2 \\cdot 3 \\cdot 5$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Ví dụ phân tích chuẩn',
                        'Số nguyên tố chẵn duy nhất',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 10: Số nguyên tố, biểu thức/quy tắc $24 = 2^3 \\cdot 3$; $36 = 2^2 \\cdot '
                        '3^2$; $60 = 2^2 \\cdot 3 \\cdot 5$ chính là nội dung của **Ví dụ phân tích '
                        'chuẩn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi phân tích số $120$ ra thừa số nguyên tố được $120 = 2^x \\cdot 3 \\cdot 5$. Giá trị '
                 'của $x$ là:',
            'options': ['$x = 2$', '$x = 3$', '$x = 4$', '$x = 1$'],
            'answer': 1,
            'solution': 'Vì $120 = 8 \\cdot 15 = 2^3 \\cdot 3 \\cdot 5$ nên $x = 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Số nguyên tố** (Chương II: Tính chia hết trong tập hợp các số tự nhiên), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Nhận biết được số nguyên tố và hợp số; thuộc các số nguyên tố nhỏ hơn $20$.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 10: Số nguyên tố: Nhận biết được số nguyên tố và hợp '
                        'số; thuộc các số nguyên tố nhỏ hơn $20$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính chất của số nguyên tố và hợp số. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Số $2$ là số nguyên tố chẵn duy nhất',
                           'Số $1$ là số nguyên tố nhỏ nhất',
                           'Mọi số nguyên tố đều là số lẻ',
                           'Số $91$ là hợp số vì $91 = 7 \\cdot 13$'],
            'answer': [True, False, False, True],
            'solution': 'a) Đúng. b) Sai vì $1$ không là số nguyên tố, số nguyên tố nhỏ nhất là $2$. c) Sai '
                        'vì $2$ là số nguyên tố chẵn. d) Đúng vì $91 = 7 \\cdot 13$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 10: Số nguyên tố**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được số nguyên tố và hợp '
                           'số; thuộc các số nguyên tố nhỏ hơn $20$.',
                           'Quy tắc/công thức **Số nguyên tố chẵn duy nhất** trong bài được xác định bởi: Số '
                           '$2$.',
                           'Trong mọi trường hợp, **Số nguyên tố chẵn duy nhất** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 10: Số nguyên tố.',
                           'Với bài toán minh họa: “Phân tích số $84$ ra thừa số nguyên tố và cho biết các '
                           'ước nguyên tố của $84$.”, lời giải đúng là: Ta có $84 = 2^2 \\cdot 3 \\cdot 7$. '
                           'Các ước nguyên tố của $84$ là $2; 3; 7$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Số nguyên tố. b) **Đúng** theo công '
                        'thức trọng tâm **Số nguyên tố chẵn duy nhất** (Số $2$). c) **Sai** vì $x \\in A$ '
                        '($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung '
                        'khác, không phải quy tắc chung của **Số nguyên tố chẵn duy nhất**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 10: Số nguyên tố** để giải quyết tình huống sau: Phân tích số '
                 '$84$ ra thừa số nguyên tố và cho biết các ước nguyên tố của $84$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Ta có $84 = 2^2 \\cdot 3 \\cdot 7$. Các ước nguyên tố của $84$ là $2; 3; 7$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Số nguyên tố: Ta có $84 = 2^2 \\cdot 3 \\cdot 7$. '
                        'Các ước nguyên tố của $84$ là $2; 3; 7$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu số nguyên tố nhỏ hơn $20$?',
            'answer': ['8'],
            'unit': None,
            'solution': 'Các số nguyên tố nhỏ hơn $20$ là $2; 3; 5; 7; 11; 13; 17; 19$, có tất cả $8$ số.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch02-tinh-chia-het',
  'context_title': 'Chương II: Tính chia hết trong tập hợp các số tự nhiên',
  'context': 'Chương II · SGK Toán 6: Quan hệ chia hết, dấu hiệu chia hết, số nguyên tố, ƯCLN và BCNN.',
  'title': 'Bài 11: Ước chung. Ước chung lớn nhất',
  'icon': '➗',
  'description': 'Khái niệm ước chung, ước chung lớn nhất, hai số nguyên tố cùng nhau và ứng dụng rút gọn '
                 'phân số tối giản.',
  'requirements': ['Tìm được ước chung lớn nhất $\\text{ƯCLN}(a, b)$ bằng cách phân tích các số ra thừa số '
                   'nguyên tố.',
                   'Tìm được tập hợp $\\text{ƯC}(a, b)$ thông qua các ước của $\\text{ƯCLN}(a, b)$ và giải '
                   'bài toán chia đều.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Công thức nhớ nhanh** (ƯCLN = Tích các thừa '
                   'số nguyên tố CHUNG với số mũ NHỎ NHẤT) vào giải bài tập.'],
  'definition': '- **Ước chung** của hai hay nhiều số là ước của tất cả các số đó, kí hiệu $\\text{ƯC}(a, '
                'b)$.\n'
                '- **Ước chung lớn nhất** của hai hay nhiều số là số lớn nhất trong tập hợp các ước chung '
                'của các số đó, kí hiệu $\\text{ƯCLN}(a, b)$.\n'
                '- Hai số có $\\text{ƯCLN}(a, b) = 1$ được gọi là **hai số nguyên tố cùng nhau**.',
  'theory': '### 1. Quy tắc tìm $\\text{ƯCLN}$ bằng phân tích thừa số nguyên tố\n'
            '- Bước 1: Phân tích mỗi số ra thừa số nguyên tố.\n'
            '- Bước 2: Chọn ra các thừa số nguyên tố **chung**.\n'
            '- Bước 3: Lập tích các thừa số đã chọn, mỗi thừa số lấy với **số mũ nhỏ nhất**.\n'
            '### 2. Tìm ước chung từ $\\text{ƯCLN}$\n'
            '- Tất cả các ước chung của $a$ và $b$ đều là ước của $\\text{ƯCLN}(a, b)$.',
  'formulas': [{'category': 'I. Quy tắc ƯCLN',
                'items': [{'name': 'Công thức nhớ nhanh',
                           'formula': 'ƯCLN = Tích các thừa số nguyên tố CHUNG với số mũ NHỎ NHẤT'},
                          {'name': 'Tập ước chung',
                           'formula': '$\\text{ƯC}(a, b) = \\text{Ư}(\\text{ƯCLN}(a, b))$'},
                          {'name': 'Hai số nguyên tố cùng nhau', 'formula': '$\\text{ƯCLN}(a, b) = 1$'}]}],
  'example': 'Tìm $\\text{ƯCLN}(24, 36)$ và tập hợp $\\text{ƯC}(24, 36)$.',
  'example_answer': 'Ta có $24 = 2^3 \\cdot 3$ và $36 = 2^2 \\cdot 3^2$. Suy ra $\\text{ƯCLN}(24, 36) = 2^2 '
                    '\\cdot 3 = 12$ và $\\text{ƯC}(24, 36) = \\text{Ư}(12) = \\{1; 2; 3; 4; 6; 12\\}$.',
  'real_life': 'Chia đều vở và bút thành số phần thưởng nhiều nhất có thể cho học sinh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Ước chung lớn nhất của $24$ và $36$ bằng:',
            'options': ['$6$', '$72$', '$12$', '$4$'],
            'answer': 2,
            'solution': 'Vì $24 = 2^3 \\cdot 3$ và $36 = 2^2 \\cdot 3^2$ nên $\\text{ƯCLN}(24, 36) = 2^2 '
                        '\\cdot 3 = 12$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cặp số nào sau đây là hai số nguyên tố cùng nhau?',
            'options': ['$6$ và $9$', '$12$ và $18$', '$10$ và $25$', '$8$ và $15$'],
            'answer': 3,
            'solution': 'Ta có $\\text{ƯCLN}(8, 15) = 1$ nên $8$ và $15$ là hai số nguyên tố cùng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 11: Ước chung. Ước chung lớn nhất**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Công thức nhớ nhanh**?',
            'options': ['ƯCLN = Tích các thừa số nguyên tố CHUNG với số mũ NHỎ NHẤT',
                        '$\\text{ƯC}(a, b) = \\text{Ư}(\\text{ƯCLN}(a, b))$',
                        '$\\text{ƯCLN}(a, b) = 1$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 11: Ước chung. Ước chung lớn nhất, **Công '
                        'thức nhớ nhanh** được xác định bởi: ƯCLN = Tích các thừa số nguyên tố CHUNG với số '
                        'mũ NHỎ NHẤT.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Ước chung. Ước chung lớn nhất**, nội dung/biểu thức $\\text{ƯC}(a, b) = '
                 '\\text{Ư}(\\text{ƯCLN}(a, b))$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Công thức nhớ nhanh',
                        'Tập ước chung',
                        'Hai số nguyên tố cùng nhau',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 1,
            'solution': 'Trong Bài 11: Ước chung. Ước chung lớn nhất, biểu thức/quy tắc $\\text{ƯC}(a, b) = '
                        '\\text{Ư}(\\text{ƯCLN}(a, b))$ chính là nội dung của **Tập ước chung**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biết $\\text{ƯCLN}(a, b) = 10$. Tập hợp $\\text{ƯC}(a, b)$ có bao nhiêu phần tử?',
            'options': ['$2$ phần tử', '$5$ phần tử', '$4$ phần tử', '$10$ phần tử'],
            'answer': 2,
            'solution': 'Ta có $\\text{ƯC}(a, b) = \\text{Ư}(10) = \\{1; 2; 5; 10\\}$ gồm $4$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Ước chung. Ước chung lớn nhất** (Chương II: Tính chia hết trong tập hợp '
                 'các số tự nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Tìm được ước chung lớn nhất $\\text{ƯCLN}(a, b)$ bằng cách phân tích các số ra thừa '
                        'số nguyên tố.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 11: Ước chung. Ước chung lớn nhất: Tìm được ước chung '
                        'lớn nhất $\\text{ƯCLN}(a, b)$ bằng cách phân tích các số ra thừa số nguyên tố.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai số tự nhiên $18$ và $30$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$\\text{ƯCLN}(18, 30) = 6$',
                           '$18$ và $30$ là hai số nguyên tố cùng nhau',
                           'Tập hợp $\\text{ƯC}(18, 30)$ có đúng $4$ phần tử',
                           'Rút gọn phân số $\\dfrac{18}{30}$ cho $\\text{ƯCLN}(18, 30)$ ta được '
                           '$\\dfrac{3}{5}$'],
            'answer': [True, False, True, True],
            'solution': 'Ta có $18 = 2 \\cdot 3^2, 30 = 2 \\cdot 3 \\cdot 5 \\Rightarrow \\text{ƯCLN} = 6$. '
                        'a) Đúng. b) Sai vì $\\text{ƯCLN} = 6 \\ne 1$. c) Đúng ($\\{1; 2; 3; 6\\}$). d) '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 11: Ước chung. Ước '
                 'chung lớn nhất**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tìm được ước chung lớn nhất '
                           '$\\text{ƯCLN}(a, b)$ bằng cách phân tích các số ra thừa số nguyên tố.',
                           'Quy tắc/công thức **Công thức nhớ nhanh** trong bài được xác định bởi: ƯCLN = '
                           'Tích các thừa số nguyên tố CHUNG với số mũ NHỎ NHẤT.',
                           'Trong mọi trường hợp, **Công thức nhớ nhanh** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 11: Ước chung. Ước chung lớn nhất.',
                           'Với bài toán minh họa: “Tìm $\\text{ƯCLN}(24, 36)$ và tập hợp $\\text{ƯC}(24, '
                           '36)$.”, lời giải đúng là: Ta có $24 = 2^3 \\cdot 3$ và $36 = 2^2 \\cdot 3^2$. '
                           'Suy ra $\\text{ƯCLN}(24, 36) = 2^2 \\cdot 3 = 12$ và $\\text{ƯC}(24, 36) = '
                           '\\text{Ư}(12) = \\{1; 2; 3; 4; 6; 12\\}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Ước chung. Ước chung lớn nhất. b) '
                        '**Đúng** theo công thức trọng tâm **Công thức nhớ nhanh** (ƯCLN = Tích các thừa số '
                        'nguyên tố CHUNG với số mũ NHỎ NHẤT). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y '
                        '\\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc '
                        'chung của **Công thức nhớ nhanh**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 11: Ước chung. Ước chung lớn nhất** để giải quyết tình huống sau: '
                 'Tìm $\\text{ƯCLN}(24, 36)$ và tập hợp $\\text{ƯC}(24, 36)$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $24 = 2^3 \\cdot 3$ và $36 = 2^2 \\cdot 3^2$. Suy ra $\\text{ƯCLN}(24, 36) = '
                        '2^2 \\cdot 3 = 12$ và $\\text{ƯC}(24, 36) = \\text{Ư}(12) = \\{1; 2; 3; 4; 6; '
                        '12\\}$...',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Ước chung. Ước chung lớn nhất: Ta có $24 = 2^3 '
                        '\\cdot 3$ và $36 = 2^2 \\cdot 3^2$. Suy ra $\\text{ƯCLN}(24, 36) = 2^2 \\cdot 3 = '
                        '12$ và $\\text{ƯC}(24, 36) = \\text{Ư}(12) = \\{1; 2; 3; 4; 6; 12\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cô giáo có $48$ quyển vở và $60$ chiếc bút bi, muốn chia đều thành các phần thưởng như '
                 'nhau (mỗi phần đều có cả vở và bút). Hỏi có thể chia được nhiều nhất bao nhiêu phần '
                 'thưởng?',
            'answer': ['12'],
            'unit': None,
            'solution': 'Số phần thưởng nhiều nhất là $\\text{ƯCLN}(48, 60) = 12$ (phần thưởng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch02-tinh-chia-het',
  'context_title': 'Chương II: Tính chia hết trong tập hợp các số tự nhiên',
  'context': 'Chương II · SGK Toán 6: Quan hệ chia hết, dấu hiệu chia hết, số nguyên tố, ƯCLN và BCNN.',
  'title': 'Bài 12: Bội chung. Bội chung nhỏ nhất',
  'icon': '➗',
  'description': 'Khái niệm bội chung, bội chung nhỏ nhất và ứng dụng trong quy đồng mẫu các phân số và bài '
                 'toán thực tiễn.',
  'requirements': ['Tìm được bội chung nhỏ nhất $\\text{BCNN}(a, b)$ bằng cách phân tích ra thừa số nguyên '
                   'tố.',
                   'Tìm được tập hợp $\\text{BC}(a, b)$ từ $\\text{BCNN}(a, b)$ và vận dụng quy đồng mẫu số, '
                   'giải toán thực tế.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Công thức nhớ nhanh** (BCNN = Tích các thừa '
                   'số nguyên tố CHUNG và RIÊNG với số mũ LỚN NHẤT) vào giải bài tập.'],
  'definition': '- **Bội chung** của hai hay nhiều số là bội của tất cả các số đó, kí hiệu $\\text{BC}(a, '
                'b)$.\n'
                '- **Bội chung nhỏ nhất** của hai hay nhiều số là số nhỏ nhất **khác $0$** trong tập hợp các '
                'bội chung của các số đó, kí hiệu $\\text{BCNN}(a, b)$.',
  'theory': '### 1. Quy tắc tìm $\\text{BCNN}$ bằng phân tích thừa số nguyên tố\n'
            '- Bước 1: Phân tích mỗi số ra thừa số nguyên tố.\n'
            '- Bước 2: Chọn ra các thừa số nguyên tố **chung và riêng**.\n'
            '- Bước 3: Lập tích các thừa số đã chọn, mỗi thừa số lấy với **số mũ lớn nhất**.\n'
            '### 2. Tính chất đặc biệt\n'
            '- Mọi bội chung của $a$ và $b$ đều là bội của $\\text{BCNN}(a, b)$.\n'
            '- Nếu $\\text{ƯCLN}(a, b) = 1$ thì $\\text{BCNN}(a, b) = a \\cdot b$.',
  'formulas': [{'category': 'I. Quy tắc BCNN',
                'items': [{'name': 'Công thức nhớ nhanh',
                           'formula': 'BCNN = Tích các thừa số nguyên tố CHUNG và RIÊNG với số mũ LỚN NHẤT'},
                          {'name': 'Tập bội chung',
                           'formula': '$\\text{BC}(a, b) = \\text{B}(\\text{BCNN}(a, b))$'},
                          {'name': 'Hệ thức liên hệ',
                           'formula': '$\\text{ƯCLN}(a, b) \\cdot \\text{BCNN}(a, b) = a \\cdot b$'}]}],
  'example': 'Tìm $\\text{BCNN}(12, 18)$ và thực hiện phép cộng $\\dfrac{5}{12} + \\dfrac{7}{18}$.',
  'example_answer': 'Ta có $12 = 2^2 \\cdot 3$ và $18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN}(12, 18) = 2^2 '
                    '\\cdot 3^2 = 36$. Khi đó $\\dfrac{5}{12} + \\dfrac{7}{18} = \\dfrac{15}{36} + '
                    '\\dfrac{14}{36} = \\dfrac{29}{36}$.',
  'real_life': 'Tính khoảng thời gian ngắn nhất để hai tuyến xe buýt cùng xuất phát trở lại tại bến.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bội chung nhỏ nhất của $12$ và $18$ bằng:',
            'options': ['$6$', '$216$', '$72$', '$36$'],
            'answer': 3,
            'solution': 'Ta có $12 = 2^2 \\cdot 3$ và $18 = 2 \\cdot 3^2$ nên $\\text{BCNN}(12, 18) = 2^2 '
                        '\\cdot 3^2 = 36$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu hai số tự nhiên $a, b$ thỏa mãn $a \\vdots b$ ($b \\ne 0$) thì $\\text{BCNN}(a, b)$ '
                 'bằng:',
            'options': ['$a$', '$b$', '$a \\cdot b$', '$1$'],
            'answer': 0,
            'solution': 'Khi số lớn $a$ chia hết cho số bé $b$ thì $\\text{BCNN}(a, b) = a$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 12: Bội chung. Bội chung nhỏ nhất**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Công thức nhớ nhanh**?',
            'options': ['$\\text{BC}(a, b) = \\text{B}(\\text{BCNN}(a, b))$',
                        'BCNN = Tích các thừa số nguyên tố CHUNG và RIÊNG với số mũ LỚN NHẤT',
                        '$\\text{ƯCLN}(a, b) \\cdot \\text{BCNN}(a, b) = a \\cdot b$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 12: Bội chung. Bội chung nhỏ nhất, **Công '
                        'thức nhớ nhanh** được xác định bởi: BCNN = Tích các thừa số nguyên tố CHUNG và '
                        'RIÊNG với số mũ LỚN NHẤT.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Bội chung. Bội chung nhỏ nhất**, nội dung/biểu thức $\\text{BC}(a, b) = '
                 '\\text{B}(\\text{BCNN}(a, b))$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Công thức nhớ nhanh',
                        'Hệ thức liên hệ',
                        'Tập bội chung',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 2,
            'solution': 'Trong Bài 12: Bội chung. Bội chung nhỏ nhất, biểu thức/quy tắc $\\text{BC}(a, b) = '
                        '\\text{B}(\\text{BCNN}(a, b))$ chính là nội dung của **Tập bội chung**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số tự nhiên $x$ nhỏ nhất khác $0$ biết $x \\vdots 8$ và $x \\vdots 12$:',
            'options': ['$x = 4$', '$x = 48$', '$x = 96$', '$x = 24$'],
            'answer': 3,
            'solution': 'Số nhỏ nhất khác $0$ chia hết cho cả $8$ và $12$ là $\\text{BCNN}(8, 12) = 24$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Bội chung. Bội chung nhỏ nhất** (Chương II: Tính chia hết trong tập hợp '
                 'các số tự nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Tìm được bội chung nhỏ nhất $\\text{BCNN}(a, b)$ bằng cách phân tích ra thừa số '
                        'nguyên tố.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 12: Bội chung. Bội chung nhỏ nhất: Tìm được bội chung '
                        'nhỏ nhất $\\text{BCNN}(a, b)$ bằng cách phân tích ra thừa số nguyên tố.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai số tự nhiên $8$ và $15$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$\\text{ƯCLN}(8, 15) = 1$',
                           '$\\text{BCNN}(8, 15) = 120$',
                           'Số $0$ là bội chung nhỏ nhất của $8$ và $15$',
                           'Mẫu số chung nhỏ nhất của $\\dfrac{3}{8}$ và $\\dfrac{7}{15}$ là $120$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $8 \\cdot 15 = 120$. c) Sai vì $\\text{BCNN}$ là số nhỏ nhất '
                        'khác $0$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 12: Bội chung. Bội '
                 'chung nhỏ nhất**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tìm được bội chung nhỏ nhất '
                           '$\\text{BCNN}(a, b)$ bằng cách phân tích ra thừa số nguyên tố.',
                           'Quy tắc/công thức **Công thức nhớ nhanh** trong bài được xác định bởi: BCNN = '
                           'Tích các thừa số nguyên tố CHUNG và RIÊNG với số mũ LỚN NHẤT.',
                           'Trong mọi trường hợp, **Công thức nhớ nhanh** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 12: Bội chung. Bội chung nhỏ nhất.',
                           'Với bài toán minh họa: “Tìm $\\text{BCNN}(12, 18)$ và thực hiện phép cộng '
                           '$\\dfrac{5}{12} + \\dfrac{7}{18}$.”, lời giải đúng là: Ta có $12 = 2^2 \\cdot 3$ '
                           'và $18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN}(12, 18) = 2^2 \\cdot 3^2 = 36$. '
                           'Khi đó $\\dfrac{5}{12} + \\dfrac{7}{18} = \\dfrac{15}{36} + \\dfrac{14}{36} = '
                           '\\dfrac{29}{36}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Bội chung. Bội chung nhỏ nhất. b) '
                        '**Đúng** theo công thức trọng tâm **Công thức nhớ nhanh** (BCNN = Tích các thừa số '
                        'nguyên tố CHUNG và RIÊNG với số mũ LỚN NHẤT). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Công thức nhớ nhanh**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 12: Bội chung. Bội chung nhỏ nhất** để giải quyết tình huống sau: '
                 'Tìm $\\text{BCNN}(12, 18)$ và thực hiện phép cộng $\\dfrac{5}{12} + \\dfrac{7}{18}$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Ta có $12 = 2^2 \\cdot 3$ và $18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN}(12, 18) = '
                        '2^2 \\cdot 3^2 = 36$. Khi đó $\\dfrac{5}{12} + \\dfrac{7}{18} = \\dfrac{15}{36} + '
                        '\\dfrac{14}{36} = \\dfrac{29}{36}$...',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Bội chung. Bội chung nhỏ nhất: Ta có $12 = 2^2 '
                        '\\cdot 3$ và $18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN}(12, 18) = 2^2 \\cdot 3^2 '
                        '= 36$. Khi đó $\\dfrac{5}{12} + \\dfrac{7}{18} = \\dfrac{15}{36} + \\dfrac{14}{36} '
                        '= \\dfrac{29}{36}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai xe buýt cùng xuất phát từ bến lúc $6$ giờ sáng. Xe thứ nhất cứ $10$ phút chạy một '
                 'chuyến, xe thứ hai cứ $15$ phút chạy một chuyến. Hỏi sau ít nhất bao nhiêu phút thì hai xe '
                 'lại cùng xuất phát tại bến?',
            'answer': ['30'],
            'unit': None,
            'solution': 'Thời gian ít nhất để hai xe cùng xuất phát lại là $\\text{BCNN}(10, 15) = 30$ '
                        '(phút).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch03-so-nguyen',
  'context_title': 'Chương III: Số nguyên',
  'context': 'Chương III · SGK Toán 6: Tập hợp số nguyên, bốn phép tính và quy tắc dấu ngoặc.',
  'title': 'Bài 13: Tập hợp các số nguyên',
  'icon': '🌡️',
  'description': 'Nhận biết số nguyên âm, tập hợp số nguyên Z, trục số, hai số đối nhau và thứ tự trong tập '
                 'hợp số nguyên.',
  'requirements': ['Nhận biết được tập hợp các số nguyên $\\mathbb{Z}$, biểu diễn số nguyên trên trục số và '
                   'tìm số đối của một số nguyên.',
                   'So sánh được hai số nguyên bất kì và sắp xếp các số nguyên theo thứ tự.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tập hợp số nguyên** ($\\mathbb{Z} = '
                   '\\{\\dots; -2; -1; 0; 1; 2; \\dots\\}$) vào giải bài tập.'],
  'definition': '- Tập hợp các **số nguyên** gồm các số nguyên âm, số $0$ và các số nguyên dương: '
                '$\\mathbb{Z} = \\{\\dots; -3; -2; -1; 0; 1; 2; 3; \\dots\\}$. Số $0$ không là số nguyên âm '
                'và cũng không là số nguyên dương.\n'
                '- Hai số nguyên trên trục số nằm ở hai phía của điểm $0$ và cách đều điểm $0$ được gọi là '
                '**hai số đối nhau** (số đối của $a$ là $-a$).\n'
                '- Trên trục số nằm ngang, nếu điểm $a$ nằm bên trái điểm $b$ thì $a < b$.',
  'theory': '### 1. Số đối của một số nguyên\n'
            '- Số đối của $5$ là $-5$; số đối của $-8$ là $8$; số đối của $0$ là $0$.\n'
            '### 2. So sánh hai số nguyên\n'
            '- Mọi số nguyên âm đều nhỏ hơn $0$ và nhỏ hơn mọi số nguyên dương.\n'
            '- Trong hai số nguyên âm, số nào có điểm biểu diễn gần điểm $0$ hơn (có phần số tự nhiên nhỏ '
            'hơn) thì lớn hơn: $-2 > -5$.',
  'formulas': [{'category': 'I. Tập hợp Z và So sánh',
                'items': [{'name': 'Tập hợp số nguyên',
                           'formula': '$\\mathbb{Z} = \\{\\dots; -2; -1; 0; 1; 2; \\dots\\}$'},
                          {'name': 'Quan hệ thứ tự',
                           'formula': '$\\text{Số nguyên âm} < 0 < \\text{Số nguyên dương}$'},
                          {'name': 'So sánh hai số nguyên âm',
                           'formula': 'Nếu $a, b \\in \\mathbb{N}^*$ và $a < b$ thì $-a > -b$'}]}],
  'example': 'Sắp xếp các số nguyên sau theo thứ tự tăng dần: $3; -7; 0; -2; 5$.',
  'example_answer': 'So sánh các số âm và số dương ta có: $-7 < -2 < 0 < 3 < 5$.',
  'real_life': 'Biểu diễn nhiệt độ dưới $0^\\circ\\text{C}$, độ cao dưới mực nước biển, tiền lãi và tiền lỗ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số đối của số nguyên $-8$ là:',
            'options': ['$8$', '$-8$', '$0$', '$\\dfrac{1}{8}$'],
            'answer': 0,
            'solution': 'Số đối của $-8$ là $8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cách sắp xếp nào sau đây theo thứ tự tăng dần là đúng?',
            'options': ['$-5 < -7 < 0$', '$-7 < -5 < 0$', '$0 < -5 < -7$', '$-5 < 0 < -7$'],
            'answer': 1,
            'solution': 'Trên trục số $-7$ nằm bên trái $-5$ và $-5$ nằm bên trái $0$ nên $-7 < -5 < 0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 13: Tập hợp các số nguyên**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Tập hợp số nguyên**?',
            'options': ['$\\text{Số nguyên âm} < 0 < \\text{Số nguyên dương}$',
                        'Nếu $a, b \\in \\mathbb{N}^*$ và $a < b$ thì $-a > -b$',
                        '$\\mathbb{Z} = \\{\\dots; -2; -1; 0; 1; 2; \\dots\\}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 13: Tập hợp các số nguyên, **Tập hợp số '
                        'nguyên** được xác định bởi: $\\mathbb{Z} = \\{\\dots; -2; -1; 0; 1; 2; \\dots\\}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Tập hợp các số nguyên**, nội dung/biểu thức $\\text{Số nguyên âm} < 0 < '
                 '\\text{Số nguyên dương}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tập hợp số nguyên',
                        'So sánh hai số nguyên âm',
                        'Quan hệ phần tử – tập hợp',
                        'Quan hệ thứ tự'],
            'answer': 3,
            'solution': 'Trong Bài 13: Tập hợp các số nguyên, biểu thức/quy tắc $\\text{Số nguyên âm} < 0 < '
                        '\\text{Số nguyên dương}$ chính là nội dung của **Quan hệ thứ tự**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tập hợp $A = \\{x \\in \\mathbb{Z} \\mid -3 < x \\le 2\\}$ có bao nhiêu phần tử?',
            'options': ['$5$ phần tử', '$4$ phần tử', '$6$ phần tử', '$3$ phần tử'],
            'answer': 0,
            'solution': 'Ta có $A = \\{-2; -1; 0; 1; 2\\}$ gồm $5$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Tập hợp các số nguyên** (Chương III: Số nguyên), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Nhận biết được tập hợp các số nguyên $\\mathbb{Z}$, biểu diễn số nguyên trên trục '
                        'số và tìm số đối của một số nguyên.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 13: Tập hợp các số nguyên: Nhận biết được tập hợp các '
                        'số nguyên $\\mathbb{Z}$, biểu diễn số nguyên trên trục số và tìm số đối của một số '
                        'nguyên.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tập hợp các số nguyên $\\mathbb{Z}$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$-5 < -2$',
                           'Số $0$ là số nguyên dương nhỏ nhất',
                           'Mọi số tự nhiên đều là số nguyên',
                           'Số đối của $0$ là $0$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì số $0$ không âm, không dương; số nguyên dương nhỏ nhất là $1$. '
                        'c) Đúng. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 13: Tập hợp các số '
                 'nguyên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được tập hợp các số '
                           'nguyên $\\mathbb{Z}$, biểu diễn số nguyên trên trục số và tìm số đối của một số '
                           'nguyên.',
                           'Quy tắc/công thức **Tập hợp số nguyên** trong bài được xác định bởi: '
                           '$\\mathbb{Z} = \\{\\dots; -2; -1; 0; 1; 2; \\dots\\}$.',
                           'Trong mọi trường hợp, **Tập hợp số nguyên** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 13: Tập hợp các số nguyên.',
                           'Với bài toán minh họa: “Sắp xếp các số nguyên sau theo thứ tự tăng dần: $3; -7; '
                           '0; -2; 5$.”, lời giải đúng là: So sánh các số âm và số dương ta có: $-7 < -2 < 0 '
                           '< 3 < 5$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Tập hợp các số nguyên. b) **Đúng** '
                        'theo công thức trọng tâm **Tập hợp số nguyên** ($\\mathbb{Z} = \\{\\dots; -2; -1; '
                        '0; 1; 2; \\dots\\}$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ '
                        'không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của **Tập '
                        'hợp số nguyên**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 13: Tập hợp các số nguyên** để giải quyết tình huống sau: Sắp xếp '
                 'các số nguyên sau theo thứ tự tăng dần: $3; -7; 0; -2; 5$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'So sánh các số âm và số dương ta có: $-7 < -2 < 0 < 3 < 5$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Tập hợp các số nguyên: So sánh các số âm và số dương '
                        'ta có: $-7 < -2 < 0 < 3 < 5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính tổng tất cả các số nguyên $x$ thỏa mãn $-3 \\le x \\le 4$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Các số nguyên $x$ là $-3; -2; -1; 0; 1; 2; 3; 4$. Các cặp số đối nhau có tổng bằng '
                        '$0$, chỉ còn lại $4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch03-so-nguyen',
  'context_title': 'Chương III: Số nguyên',
  'context': 'Chương III · SGK Toán 6: Tập hợp số nguyên, bốn phép tính và quy tắc dấu ngoặc.',
  'title': 'Bài 14: Phép cộng và phép trừ số nguyên',
  'icon': '🌡️',
  'description': 'Quy tắc cộng hai số nguyên cùng dấu, cộng hai số nguyên khác dấu và quy tắc trừ hai số '
                 'nguyên.',
  'requirements': ['Thực hiện đúng phép cộng hai số nguyên cùng dấu và khác dấu.',
                   'Chuyển phép trừ hai số nguyên thành phép cộng với số đối: $a - b = a + (-b)$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Cộng hai số nguyên âm** ($(-a) + (-b) = -(a '
                   '+ b)$ (với $a, b \\in \\mathbb{N}^*$)) vào giải bài tập.'],
  'definition': '- **Cộng hai số nguyên âm**: ta cộng phần số tự nhiên của chúng với nhau rồi đặt dấu “$-$” '
                'trước kết quả.\n'
                '- **Cộng hai số nguyên khác dấu** (không đối nhau): ta lấy phần số tự nhiên lớn hơn trừ đi '
                'phần số tự nhiên nhỏ hơn rồi đặt trước hiệu tìm được dấu của số có phần số tự nhiên lớn '
                'hơn.\n'
                '- **Trừ hai số nguyên**: muốn trừ số nguyên $a$ cho số nguyên $b$, ta cộng $a$ với số đối '
                'của $b$: $a - b = a + (-b)$.',
  'theory': '### 1. Ví dụ minh họa phép cộng và phép trừ\n'
            '- Cùng dấu âm: $(-12) + (-8) = -(12 + 8) = -20$.\n'
            '- Khác dấu: $(-9) + 4 = -(9 - 4) = -5$; hai số đối nhau có tổng bằng $0$: $a + (-a) = 0$.\n'
            '- Phép trừ: $5 - 12 = 5 + (-12) = -7$; $15 - (-9) = 15 + 9 = 24$.\n'
            '### 2. Tính chất của phép cộng số nguyên\n'
            '- Phép cộng trong $\\mathbb{Z}$ có tính chất giao hoán, kết hợp, cộng với số $0$ và cộng với số '
            'đối.',
  'formulas': [{'category': 'I. Quy tắc cộng và trừ số nguyên',
                'items': [{'name': 'Cộng hai số nguyên âm',
                           'formula': '$(-a) + (-b) = -(a + b)$ (với $a, b \\in \\mathbb{N}^*$)'},
                          {'name': 'Cộng hai số đối nhau', 'formula': '$a + (-a) = 0$'},
                          {'name': 'Phép trừ hai số nguyên',
                           'formula': '$a - b = a + (-b)$; $a - (-b) = a + b$'}]}],
  'example': 'Tính hợp lí: $(-37) + 54 + (-63) + 46$.',
  'example_answer': 'Nhóm $[(-37) + (-63)] + (54 + 46) = (-100) + 100 = 0$.',
  'real_life': 'Tính sự thay đổi nhiệt độ giữa ban ngày và ban đêm ở vùng núi cao hoặc độ sâu của tàu ngầm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $(-12) + (-8)$ là:',
            'options': ['$20$', '$-20$', '$-4$', '$4$'],
            'answer': 1,
            'solution': 'Cộng hai số nguyên âm: $(-12) + (-8) = -(12 + 8) = -20$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $15 - (-9)$ là:',
            'options': ['$6$', '$-24$', '$24$', '$-6$'],
            'answer': 2,
            'solution': 'Ta có $15 - (-9) = 15 + 9 = 24$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 14: Phép cộng và phép trừ số nguyên**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Cộng hai số nguyên âm**?',
            'options': ['$a + (-a) = 0$',
                        '$a - b = a + (-b)$; $a - (-b) = a + b$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$(-a) + (-b) = -(a + b)$ (với $a, b \\in \\mathbb{N}^*$)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 14: Phép cộng và phép trừ số nguyên, **Cộng '
                        'hai số nguyên âm** được xác định bởi: $(-a) + (-b) = -(a + b)$ (với $a, b \\in '
                        '\\mathbb{N}^*$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Phép cộng và phép trừ số nguyên**, nội dung/biểu thức $a + (-a) = 0$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cộng hai số đối nhau',
                        'Cộng hai số nguyên âm',
                        'Phép trừ hai số nguyên',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 0,
            'solution': 'Trong Bài 14: Phép cộng và phép trừ số nguyên, biểu thức/quy tắc $a + (-a) = 0$ '
                        'chính là nội dung của **Cộng hai số đối nhau**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nhiệt độ buổi sáng ở Sa Pa là $-3^\\circ\\text{C}$, đến trưa tăng thêm '
                 '$8^\\circ\\text{C}$, đến tối giảm $6^\\circ\\text{C}$ so với buổi trưa. Nhiệt độ buổi tối '
                 'là:',
            'options': ['$1^\\circ\\text{C}$',
                        '$-1^\\circ\\text{C}$',
                        '$-5^\\circ\\text{C}$',
                        '$11^\\circ\\text{C}$'],
            'answer': 1,
            'solution': 'Nhiệt độ buổi tối là $(-3) + 8 - 6 = 5 - 6 = -1^\\circ\\text{C}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Phép cộng và phép trừ số nguyên** (Chương III: Số nguyên), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Thực hiện đúng phép cộng hai số nguyên cùng dấu và khác dấu.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 14: Phép cộng và phép trừ số nguyên: Thực hiện đúng '
                        'phép cộng hai số nguyên cùng dấu và khác dấu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các phép cộng và trừ số nguyên. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$(-8) + 8 = 0$', '$(-15) + 7 = 8$', '$6 - 14 = -8$', '$(-5) - (-5) = -10$'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng. b) Sai vì $(-15) + 7 = -8$. c) Đúng. d) Sai vì $(-5) - (-5) = (-5) + 5 = '
                        '0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 14: Phép cộng và phép '
                 'trừ số nguyên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện đúng phép cộng hai số '
                           'nguyên cùng dấu và khác dấu.',
                           'Quy tắc/công thức **Cộng hai số nguyên âm** trong bài được xác định bởi: $(-a) + '
                           '(-b) = -(a + b)$ (với $a, b \\in \\mathbb{N}^*$).',
                           'Trong mọi trường hợp, **Cộng hai số nguyên âm** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 14: Phép cộng và phép trừ số '
                           'nguyên.',
                           'Với bài toán minh họa: “Tính hợp lí: $(-37) + 54 + (-63) + 46$.”, lời giải đúng '
                           'là: Nhóm $[(-37) + (-63)] + (54 + 46) = (-100) + 100 = 0$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Phép cộng và phép trừ số nguyên. b) '
                        '**Đúng** theo công thức trọng tâm **Cộng hai số nguyên âm** ($(-a) + (-b) = -(a + '
                        'b)$ (với $a, b \\in \\mathbb{N}^*$)). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y '
                        '\\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc '
                        'chung của **Cộng hai số nguyên âm**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 14: Phép cộng và phép trừ số nguyên** để giải quyết tình huống '
                 'sau: Tính hợp lí: $(-37) + 54 + (-63) + 46$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Nhóm $[(-37) + (-63)] + (54 + 46) = (-100) + 100 = 0$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Phép cộng và phép trừ số nguyên: Nhóm $[(-37) + '
                        '(-63)] + (54 + 46) = (-100) + 100 = 0$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tàu ngầm đang ở độ cao $-120\\text{ m}$ so với mực nước biển. Sau đó tàu nổi lên '
                 '$45\\text{ m}$ rồi lại lặn xuống thêm $30\\text{ m}$. Độ cao mới của tàu ngầm là bao nhiêu '
                 'mét?',
            'answer': ['-105', '−105'],
            'unit': None,
            'solution': 'Độ cao mới của tàu là $(-120) + 45 - 30 = -75 - 30 = -105$ ($\\text{m}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch03-so-nguyen',
  'context_title': 'Chương III: Số nguyên',
  'context': 'Chương III · SGK Toán 6: Tập hợp số nguyên, bốn phép tính và quy tắc dấu ngoặc.',
  'title': 'Bài 15: Quy tắc dấu ngoặc',
  'icon': '🌡️',
  'description': 'Quy tắc bỏ dấu ngoặc và đặt dấu ngoặc để nhóm các số hạng khi tính tổng đại số.',
  'requirements': ['Áp dụng đúng quy tắc bỏ dấu ngoặc có dấu “$+$” hoặc dấu “$-$” đứng trước.',
                   'Biết nhóm các số hạng vào trong ngoặc để tính nhanh, tính hợp lí biểu thức số nguyên.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Trước ngoặc là dấu +** ($a + (b - c + d) = '
                   'a + b - c + d$) vào giải bài tập.'],
  'definition': '- Khi bỏ dấu ngoặc có **dấu “$+$” đứng trước**, ta **giữ nguyên dấu** của các số hạng trong '
                'ngoặc: $+(a - b + c) = a - b + c$.\n'
                '- Khi bỏ dấu ngoặc có **dấu “$-$” đứng trước**, ta phải **đổi dấu tất cả** các số hạng '
                'trong ngoặc: dấu “$+$” đổi thành “$-$” và dấu “$-$” đổi thành “$+$”: $-(a - b + c) = -a + b '
                '- c$.',
  'theory': '### 1. Tổng đại số\n'
            '- Một dãy các phép tính cộng, trừ các số nguyên được gọi là một tổng đại số. Trong tổng đại số, '
            'ta có thể thay đổi vị trí các số hạng kèm theo dấu của chúng.\n'
            '### 2. Đặt dấu ngoặc để tính nhanh\n'
            '- Ví dụ: $25 - (15 - 40) = 25 - 15 + 40 = 10 + 40 = 50$.',
  'formulas': [{'category': 'I. Quy tắc dấu ngoặc',
                'items': [{'name': 'Trước ngoặc là dấu +', 'formula': '$a + (b - c + d) = a + b - c + d$'},
                          {'name': 'Trước ngoặc là dấu -', 'formula': '$a - (b - c + d) = a - b + c - d$'}]}],
  'example': 'Bỏ dấu ngoặc rồi tính: $(125 - 67) - (25 - 67)$.',
  'example_answer': 'Ta có $(125 - 67) - (25 - 67) = 125 - 67 - 25 + 67 = (125 - 25) + (-67 + 67) = 100 + 0 '
                    '= 100$.',
  'real_life': 'Tính nhanh chênh lệch thu – chi qua nhiều khoản mục tài chính.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi bỏ dấu ngoặc trong biểu thức $-(a - b + c)$ ta được:',
            'options': ['$-a - b + c$', '$a - b + c$', '$-a + b - c$', '$-a + b + c$'],
            'answer': 2,
            'solution': 'Trước ngoặc có dấu “$-$” nên đổi dấu tất cả các số hạng trong ngoặc: $-a + b - c$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bỏ dấu ngoặc rồi tính biểu thức $25 - (15 - 40)$ ta được:',
            'options': ['$-30$', '$0$', '$80$', '$50$'],
            'answer': 3,
            'solution': 'Ta có $25 - 15 + 40 = 10 + 40 = 50$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 15: Quy tắc dấu ngoặc**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Trước ngoặc là dấu +**?',
            'options': ['$a + (b - c + d) = a + b - c + d$',
                        '$a - (b - c + d) = a - b + c - d$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 15: Quy tắc dấu ngoặc, **Trước ngoặc là dấu '
                        '+** được xác định bởi: $a + (b - c + d) = a + b - c + d$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Quy tắc dấu ngoặc**, nội dung/biểu thức $a - (b - c + d) = a - b + c - d$ '
                 'là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Trước ngoặc là dấu +',
                        'Trước ngoặc là dấu -',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 15: Quy tắc dấu ngoặc, biểu thức/quy tắc $a - (b - c + d) = a - b + c - '
                        'd$ chính là nội dung của **Trước ngoặc là dấu -**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $-(235 - 48) + (235 - 148)$ là:',
            'options': ['$100$', '$0$', '$-100$', '$-196$'],
            'answer': 2,
            'solution': 'Bỏ ngoặc: $-235 + 48 + 235 - 148 = (-235 + 235) + (48 - 148) = -100$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Quy tắc dấu ngoặc** (Chương III: Số nguyên), khẳng định nào sau đây phản '
                 'ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Áp dụng đúng quy tắc bỏ dấu ngoặc có dấu “$+$” hoặc dấu “$-$” đứng trước.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 15: Quy tắc dấu ngoặc: Áp dụng đúng quy tắc bỏ dấu '
                        'ngoặc có dấu “$+$” hoặc dấu “$-$” đứng trước.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét quy tắc dấu ngoặc với các số nguyên $a, b, c$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$+(a - b - c) = a - b - c$',
                           '$-(a + b - c) = -a - b + c$',
                           '$a - (b + c) = a - b + c$',
                           '$(57 - 89) - (57 - 189) = 100$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì $a - (b + c) = a - b - c$. d) Đúng vì $57 - 89 - 57 + '
                        '189 = 100$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 15: Quy tắc dấu '
                 'ngoặc**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Áp dụng đúng quy tắc bỏ dấu ngoặc '
                           'có dấu “$+$” hoặc dấu “$-$” đứng trước.',
                           'Quy tắc/công thức **Trước ngoặc là dấu +** trong bài được xác định bởi: $a + (b '
                           '- c + d) = a + b - c + d$.',
                           'Trong mọi trường hợp, **Trước ngoặc là dấu +** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 15: Quy tắc dấu ngoặc.',
                           'Với bài toán minh họa: “Bỏ dấu ngoặc rồi tính: $(125 - 67) - (25 - 67)$.”, lời '
                           'giải đúng là: Ta có $(125 - 67) - (25 - 67) = 125 - 67 - 25 + 67 = (125 - 25) + '
                           '(-67 + 67) = 100 + 0 = 100$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Quy tắc dấu ngoặc. b) **Đúng** theo '
                        'công thức trọng tâm **Trước ngoặc là dấu +** ($a + (b - c + d) = a + b - c + d$). '
                        'c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là '
                        'công thức của nội dung khác, không phải quy tắc chung của **Trước ngoặc là dấu +**. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 15: Quy tắc dấu ngoặc** để giải quyết tình huống sau: Bỏ dấu '
                 'ngoặc rồi tính: $(125 - 67) - (25 - 67)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $(125 - 67) - (25 - 67) = 125 - 67 - 25 + 67 = (125 - 25) + (-67 + 67) = 100 '
                        '+ 0 = 100$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Quy tắc dấu ngoặc: Ta có $(125 - 67) - (25 - 67) = '
                        '125 - 67 - 25 + 67 = (125 - 25) + (-67 + 67) = 100 + 0 = 100$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số nguyên $x$ biết $35 - (x - 15) = 60$.',
            'answer': ['-10', '−10'],
            'unit': None,
            'solution': 'Bỏ ngoặc: $35 - x + 15 = 60 \\Rightarrow 50 - x = 60 \\Rightarrow x = 50 - 60 = '
                        '-10$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch03-so-nguyen',
  'context_title': 'Chương III: Số nguyên',
  'context': 'Chương III · SGK Toán 6: Tập hợp số nguyên, bốn phép tính và quy tắc dấu ngoặc.',
  'title': 'Bài 16: Phép nhân số nguyên',
  'icon': '🌡️',
  'description': 'Quy tắc nhân hai số nguyên cùng dấu, khác dấu và các tính chất của phép nhân số nguyên.',
  'requirements': ['Thực hiện đúng phép nhân hai số nguyên cùng dấu (tích dương) và khác dấu (tích âm).',
                   'Vận dụng tính chất giao hoán, kết hợp và phân phối của phép nhân trong $\\mathbb{Z}$ để '
                   'tính hợp lí.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Khác dấu và Cùng dấu âm** ($(-a) \\cdot b = '
                   '-(a \\cdot b)$; $(-a) \\cdot (-b) = a \\cdot b$ ($a, b > 0$)) vào giải bài tập.'],
  'definition': '- **Nhân hai số nguyên khác dấu**: tích của hai số nguyên khác dấu luôn là một **số nguyên '
                'âm**.\n'
                '- **Nhân hai số nguyên cùng dấu**: tích của hai số nguyên cùng dấu luôn là một **số nguyên '
                'dương**: $(-a) \\cdot (-b) = a \\cdot b$ (với $a, b \\in \\mathbb{N}^*$).',
  'theory': '### 1. Quy tắc dấu của tích\n'
            '- Cùng dấu $\\rightarrow$ dương: $(+) \\cdot (+) = (+)$ và $(-) \\cdot (-) = (+)$.\n'
            '- Khác dấu $\\rightarrow$ âm: $(+) \\cdot (-) = (-)$ và $(-) \\cdot (+) = (-)$.\n'
            '### 2. Luỹ thừa của số nguyên âm\n'
            '- $(-a)^n$ là số dương nếu $n$ chẵn, là số âm nếu $n$ lẻ. Ví dụ: $(-2)^3 = -8$; $(-2)^4 = 16$.',
  'formulas': [{'category': 'I. Quy tắc nhân số nguyên',
                'items': [{'name': 'Khác dấu và Cùng dấu âm',
                           'formula': '$(-a) \\cdot b = -(a \\cdot b)$; $(-a) \\cdot (-b) = a \\cdot b$ ($a, '
                                      'b > 0$)'},
                          {'name': 'Tính chất phân phối',
                           'formula': '$a \\cdot (b + c) = a \\cdot b + a \\cdot c$'}]}],
  'example': 'Tính: $(-6) \\cdot 5$; $(-3) \\cdot (-4)$ và tính hợp lí $(-8) \\cdot 72 + (-8) \\cdot 28$.',
  'example_answer': 'Ta có $(-6) \\cdot 5 = -30$; $(-3) \\cdot (-4) = 12$ và $(-8) \\cdot (72 + 28) = (-8) '
                    '\\cdot 100 = -800$.',
  'real_life': 'Tính tổng độ sâu khi thiết bị khoan ngầm đi xuống đều đặn mỗi giờ một khoảng nhất định.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $(-6) \\cdot (-7)$ là:',
            'options': ['$-42$', '$-13$', '$13$', '$42$'],
            'answer': 3,
            'solution': 'Nhân hai số nguyên cùng dấu âm được kết quả dương: $(-6) \\cdot (-7) = 42$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của luỹ thừa $(-3)^3$ bằng:',
            'options': ['$-27$', '$27$', '$-9$', '$9$'],
            'answer': 0,
            'solution': 'Ta có $(-3)^3 = (-3) \\cdot (-3) \\cdot (-3) = -27$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 16: Phép nhân số nguyên**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Khác dấu và Cùng dấu âm**?',
            'options': ['$a \\cdot (b + c) = a \\cdot b + a \\cdot c$',
                        '$(-a) \\cdot b = -(a \\cdot b)$; $(-a) \\cdot (-b) = a \\cdot b$ ($a, b > 0$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 16: Phép nhân số nguyên, **Khác dấu và Cùng '
                        'dấu âm** được xác định bởi: $(-a) \\cdot b = -(a \\cdot b)$; $(-a) \\cdot (-b) = a '
                        '\\cdot b$ ($a, b > 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Phép nhân số nguyên**, nội dung/biểu thức $a \\cdot (b + c) = a \\cdot b + '
                 'a \\cdot c$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khác dấu và Cùng dấu âm',
                        'Quan hệ phần tử – tập hợp',
                        'Tính chất phân phối',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 16: Phép nhân số nguyên, biểu thức/quy tắc $a \\cdot (b + c) = a \\cdot b '
                        '+ a \\cdot c$ chính là nội dung của **Tính chất phân phối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $(-12) \\cdot 63 + (-12) \\cdot 37$ bằng:',
            'options': ['$1200$', '$-120$', '$312$', '$-1200$'],
            'answer': 3,
            'solution': 'Đặt $-12$ làm thừa số chung: $(-12) \\cdot (63 + 37) = (-12) \\cdot 100 = -1200$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Phép nhân số nguyên** (Chương III: Số nguyên), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Thực hiện đúng phép nhân hai số nguyên cùng dấu (tích dương) và khác dấu (tích âm).',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 16: Phép nhân số nguyên: Thực hiện đúng phép nhân hai '
                        'số nguyên cùng dấu (tích dương) và khác dấu (tích âm).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét phép nhân trong tập hợp số nguyên $\\mathbb{Z}$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$(-3) \\cdot (-5) = -15$',
                           '$(-2)^3 = -8$',
                           '$(-2)^4 = 16$',
                           'Tích của một số nguyên bất kì với $0$ luôn bằng $0$'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì $(-3) \\cdot (-5) = 15$. b) Đúng. c) Đúng. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 16: Phép nhân số '
                 'nguyên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện đúng phép nhân hai số '
                           'nguyên cùng dấu (tích dương) và khác dấu (tích âm).',
                           'Quy tắc/công thức **Khác dấu và Cùng dấu âm** trong bài được xác định bởi: $(-a) '
                           '\\cdot b = -(a \\cdot b)$; $(-a) \\cdot (-b) = a \\cdot b$ ($a, b > 0$).',
                           'Trong mọi trường hợp, **Khác dấu và Cùng dấu âm** luôn được tính bằng công thức '
                           '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ '
                           'phần tử – tập hợp) mà không cần điều kiện của Bài 16: Phép nhân số nguyên.',
                           'Với bài toán minh họa: “Tính: $(-6) \\cdot 5$; $(-3) \\cdot (-4)$ và tính hợp lí '
                           '$(-8) \\cdot 72 + (-8) \\cdot 28$.”, lời giải đúng là: Ta có $(-6) \\cdot 5 = '
                           '-30$; $(-3) \\cdot (-4) = 12$ và $(-8) \\cdot (72 + 28) = (-8) \\cdot 100 = '
                           '-800$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Phép nhân số nguyên. b) **Đúng** theo '
                        'công thức trọng tâm **Khác dấu và Cùng dấu âm** ($(-a) \\cdot b = -(a \\cdot b)$; '
                        '$(-a) \\cdot (-b) = a \\cdot b$ ($a, b > 0$)). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Khác dấu và Cùng dấu âm**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 16: Phép nhân số nguyên** để giải quyết tình huống sau: Tính: '
                 '$(-6) \\cdot 5$; $(-3) \\cdot (-4)$ và tính hợp lí $(-8) \\cdot 72 + (-8) \\cdot 28$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Ta có $(-6) \\cdot 5 = -30$; $(-3) \\cdot (-4) = 12$ và $(-8) \\cdot (72 + 28) = '
                        '(-8) \\cdot 100 = -800$.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Phép nhân số nguyên: Ta có $(-6) \\cdot 5 = -30$; '
                        '$(-3) \\cdot (-4) = 12$ và $(-8) \\cdot (72 + 28) = (-8) \\cdot 100 = -800$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một trò chơi trả lời câu hỏi, mỗi câu trả lời đúng được $+10$ điểm, mỗi câu trả lời '
                 'sai bị $-4$ điểm. Bạn An trả lời đúng $7$ câu và sai $5$ câu. Hỏi bạn An được bao nhiêu '
                 'điểm?',
            'answer': ['50'],
            'unit': None,
            'solution': 'Tổng số điểm của bạn An là $7 \\cdot 10 + 5 \\cdot (-4) = 70 - 20 = 50$ (điểm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch03-so-nguyen',
  'context_title': 'Chương III: Số nguyên',
  'context': 'Chương III · SGK Toán 6: Tập hợp số nguyên, bốn phép tính và quy tắc dấu ngoặc.',
  'title': 'Bài 17: Phép chia hết. Ước và bội của một số nguyên',
  'icon': '🌡️',
  'description': 'Phép chia hết hai số nguyên, quy tắc dấu của thương và cách tìm tập hợp các ước, bội của '
                 'một số nguyên.',
  'requirements': ['Thực hiện được phép chia hết hai số nguyên cùng dấu và khác dấu.',
                   'Tìm được tất cả các ước nguyên (cả âm và dương) và các bội nguyên của một số nguyên.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Quy tắc dấu của thương** ($(+) : (+) = '
                   '(+)$; $(-) : (-) = (+)$; $(+) : (-) = (-)$; $(-) : (+) = (-)$) vào giải bài tập.'],
  'definition': '- Cho $a, b \\in \\mathbb{Z}$ với $b \\ne 0$. Nếu có số nguyên $q$ sao cho $a = b \\cdot q$ '
                'thì ta có phép chia hết $a : b = q$, đồng thời $a$ là **bội** của $b$ và $b$ là **ước** của '
                '$a$.\n'
                '- Quy tắc dấu của phép chia giống quy tắc dấu của phép nhân: cùng dấu thì thương dương, '
                'khác dấu thì thương âm.',
  'theory': '### 1. Phép chia hết trong $\\mathbb{Z}$\n'
            '- Ví dụ: $(-20) : 5 = -4$; $(-36) : (-9) = 4$.\n'
            '### 2. Ước và bội trong $\\mathbb{Z}$\n'
            '- Nếu $d$ là một ước của $a$ thì $-d$ cũng là một ước của $a$. Ví dụ, trong $\\mathbb{Z}$ ta có '
            '$\\text{Ư}(6) = \\{-6; -3; -2; -1; 1; 2; 3; 6\\}$.',
  'formulas': [{'category': 'I. Quy tắc dấu của phép chia và Ước trong Z',
                'items': [{'name': 'Quy tắc dấu của thương',
                           'formula': '$(+) : (+) = (+)$; $(-) : (-) = (+)$; $(+) : (-) = (-)$; $(-) : (+) = '
                                      '(-)$'},
                          {'name': 'Số lượng ước trong Z',
                           'formula': 'Số ước nguyên của $a$ gấp đôi số ước tự nhiên của $|a|$'}]}],
  'example': 'Tìm tất cả các ước trong $\\mathbb{Z}$ của $-8$.',
  'example_answer': 'Các ước tự nhiên của $8$ là $1; 2; 4; 8$. Vậy tập hợp các ước nguyên của $-8$ là '
                    '$\\{-8; -4; -2; -1; 1; 2; 4; 8\\}$.',
  'real_life': 'Tính mức thay đổi nhiệt độ trung bình mỗi giờ khi nhiệt độ giảm đều.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $(-36) : 9$ là:',
            'options': ['$-4$', '$4$', '$-27$', '$27$'],
            'answer': 0,
            'solution': 'Chia hai số nguyên khác dấu được thương âm: $(-36) : 9 = -4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập hợp tất cả các ước trong $\\mathbb{Z}$ của $4$ là:',
            'options': ['$\\{1; 2; 4\\}$',
                        '$\\{-4; -2; -1; 1; 2; 4\\}$',
                        '$\\{-4; -2; -1; 0; 1; 2; 4\\}$',
                        '$\\{-1; -2; -4\\}$'],
            'answer': 1,
            'solution': 'Trong $\\mathbb{Z}$, các ước của $4$ gồm cả ước dương và ước âm: $\\{-4; -2; -1; 1; '
                        '2; 4\\}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 17: Phép chia hết. Ước và bội của một số nguyên**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Quy tắc dấu của thương**?',
            'options': ['Số ước nguyên của $a$ gấp đôi số ước tự nhiên của $|a|$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$(+) : (+) = (+)$; $(-) : (-) = (+)$; $(+) : (-) = (-)$; $(-) : (+) = (-)$',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 17: Phép chia hết. Ước và bội của một số '
                        'nguyên, **Quy tắc dấu của thương** được xác định bởi: $(+) : (+) = (+)$; $(-) : (-) '
                        '= (+)$; $(+) : (-) = (-)$; $(-) : (+) = (-)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Phép chia hết. Ước và bội của một số nguyên**, nội dung/biểu thức Số ước '
                 'nguyên của $a$ gấp đôi số ước tự nhiên của $|a|$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Quy tắc dấu của thương',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả',
                        'Số lượng ước trong Z'],
            'answer': 3,
            'solution': 'Trong Bài 17: Phép chia hết. Ước và bội của một số nguyên, biểu thức/quy tắc Số ước '
                        'nguyên của $a$ gấp đôi số ước tự nhiên của $|a|$ chính là nội dung của **Số lượng '
                        'ước trong Z**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số nguyên $x$ biết $(-5) \\cdot x = 45$:',
            'options': ['$x = -9$', '$x = 9$', '$x = 40$', '$x = -50$'],
            'answer': 0,
            'solution': 'Ta có $x = 45 : (-5) = -9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Phép chia hết. Ước và bội của một số nguyên** (Chương III: Số nguyên), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Thực hiện được phép chia hết hai số nguyên cùng dấu và khác dấu.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 17: Phép chia hết. Ước và bội của một số nguyên: Thực '
                        'hiện được phép chia hết hai số nguyên cùng dấu và khác dấu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét phép chia hết và ước, bội trong $\\mathbb{Z}$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$(-48) : (-6) = 8$',
                           'Số $6$ chỉ có $4$ ước trong tập hợp số nguyên $\\mathbb{Z}$',
                           'Mọi ước của $a$ cũng là ước của $-a$',
                           'Số $0$ là ước của mọi số nguyên'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng. b) Sai vì trong $\\mathbb{Z}$ số $6$ có $8$ ước ($\\pm 1; \\pm 2; \\pm 3; '
                        '\\pm 6$). c) Đúng. d) Sai vì không có phép chia cho $0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 17: Phép chia hết. Ước '
                 'và bội của một số nguyên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được phép chia hết hai '
                           'số nguyên cùng dấu và khác dấu.',
                           'Quy tắc/công thức **Quy tắc dấu của thương** trong bài được xác định bởi: $(+) : '
                           '(+) = (+)$; $(-) : (-) = (+)$; $(+) : (-) = (-)$; $(-) : (+) = (-)$.',
                           'Trong mọi trường hợp, **Quy tắc dấu của thương** luôn được tính bằng công thức '
                           '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ '
                           'phần tử – tập hợp) mà không cần điều kiện của Bài 17: Phép chia hết. Ước và bội '
                           'của một số nguyên.',
                           'Với bài toán minh họa: “Tìm tất cả các ước trong $\\mathbb{Z}$ của $-8$.”, lời '
                           'giải đúng là: Các ước tự nhiên của $8$ là $1; 2; 4; 8$. Vậy tập hợp các ước '
                           'nguyên của $-8$ là $\\{-8; -4; -2; -1; 1; 2; 4; 8\\}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Phép chia hết. Ước và bội của một số '
                        'nguyên. b) **Đúng** theo công thức trọng tâm **Quy tắc dấu của thương** ($(+) : (+) '
                        '= (+)$; $(-) : (-) = (+)$; $(+) : (-) = (-)$; $(-) : (+) = (-)$). c) **Sai** vì $x '
                        '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Quy tắc dấu của thương**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 17: Phép chia hết. Ước và bội của một số nguyên** để giải quyết '
                 'tình huống sau: Tìm tất cả các ước trong $\\mathbb{Z}$ của $-8$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các ước tự nhiên của $8$ là $1; 2; 4; 8$. Vậy tập hợp các ước nguyên của $-8$ là '
                        '$\\{-8; -4; -2; -1; 1; 2; 4; 8\\}$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Phép chia hết. Ước và bội của một số nguyên: Các ước '
                        'tự nhiên của $8$ là $1; 2; 4; 8$. Vậy tập hợp các ước nguyên của $-8$ là $\\{-8; '
                        '-4; -2; -1; 1; 2; 4; 8\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu số nguyên $x$ sao cho $(x - 1)$ là ước của $5$?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Các ước nguyên của $5$ là $\\{-5; -1; 1; 5\\}$ gồm $4$ giá trị, ứng với $4$ số '
                        'nguyên $x \\in \\{-4; 0; 2; 6\\}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch04-hinh-phang-trong-thuc-tien',
  'context_title': 'Chương IV: Một số hình phẳng trong thực tiễn',
  'context': 'Chương IV · SGK Toán 6: Nhận dạng, tính chất và công thức tính chu vi, diện tích các hình '
             'phẳng.',
  'title': 'Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều',
  'icon': '⬡',
  'description': 'Nhận dạng và mô tả các yếu tố cơ bản (đỉnh, cạnh, góc, đường chéo) của hình tam giác đều, '
                 'hình vuông và hình lục giác đều.',
  'requirements': ['Mô tả được đặc điểm về cạnh, góc, đường chéo của tam giác đều, hình vuông, lục giác đều.',
                   'Vẽ được tam giác đều bằng thước và compa; vẽ được hình vuông bằng thước và ê-ke.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tam giác đều cạnh a** ($3$ cạnh bằng $a$; '
                   'mỗi góc bằng $60^\\circ$) vào giải bài tập.'],
  'definition': '- **Hình tam giác đều**: có $3$ cạnh bằng nhau và $3$ góc bằng nhau (mỗi góc bằng '
                '$60^\\circ$).\n'
                '- **Hình vuông**: có $4$ cạnh bằng nhau, $4$ góc bằng nhau (đều là góc vuông $90^\\circ$) '
                'và $2$ đường chéo bằng nhau.\n'
                '- **Hình lục giác đều**: có $6$ cạnh bằng nhau, $6$ góc bằng nhau (mỗi góc bằng '
                '$120^\\circ$) và $3$ đường chéo chính bằng nhau.',
  'theory': '### 1. Cấu tạo hình lục giác đều\n'
            '- Khi nối các đỉnh đối diện của hình lục giác đều $ABCDEF$, ba đường chéo chính $AD, BE, CF$ '
            'cắt nhau tại một điểm $O$ và chia lục giác đều thành **$6$ tam giác đều** bằng nhau.\n'
            '- Độ dài đường chéo chính của lục giác đều cạnh $a$ bằng $2a$.',
  'formulas': [{'category': 'I. Đặc điểm góc và cạnh',
                'items': [{'name': 'Tam giác đều cạnh a',
                           'formula': '$3$ cạnh bằng $a$; mỗi góc bằng $60^\\circ$'},
                          {'name': 'Hình vuông cạnh a',
                           'formula': '$4$ cạnh bằng $a$; mỗi góc bằng $90^\\circ$; hai đường chéo bằng '
                                      'nhau'},
                          {'name': 'Lục giác đều cạnh a',
                           'formula': '$6$ cạnh bằng $a$; đường chéo chính dài $2a$'}]}],
  'example': 'Một hình lục giác đều có độ dài một cạnh là $5\\text{ cm}$. Tính chu vi và độ dài đường chéo '
             'chính của lục giác đều đó.',
  'example_answer': 'Chu vi lục giác đều là $6 \\cdot 5 = 30\\text{ cm}$. Độ dài đường chéo chính là $2 '
                    '\\cdot 5 = 10\\text{ cm}$.',
  'real_life': 'Cấu trúc sáp tổ ong có dạng hình lục giác đều, gạch lát nền hình vuông và biển báo tam giác '
               'đều.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Mỗi góc của một hình tam giác đều có số đo bằng:',
            'options': ['$45^\\circ$', '$60^\\circ$', '$90^\\circ$', '$120^\\circ$'],
            'answer': 1,
            'solution': 'Hình tam giác đều có ba góc bằng nhau và mỗi góc bằng $60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình lục giác đều có bao nhiêu cạnh bằng nhau?',
            'options': ['$4$ cạnh', '$5$ cạnh', '$6$ cạnh', '$8$ cạnh'],
            'answer': 2,
            'solution': 'Hình lục giác đều có $6$ cạnh bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tam giác đều cạnh a**?',
            'options': ['$4$ cạnh bằng $a$; mỗi góc bằng $90^\\circ$; hai đường chéo bằng nhau',
                        '$6$ cạnh bằng $a$; đường chéo chính dài $2a$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$3$ cạnh bằng $a$; mỗi góc bằng $60^\\circ$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 18: Hình tam giác đều. Hình vuông. Hình lục '
                        'giác đều, **Tam giác đều cạnh a** được xác định bởi: $3$ cạnh bằng $a$; mỗi góc '
                        'bằng $60^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều**, nội dung/biểu thức $4$ '
                 'cạnh bằng $a$; mỗi góc bằng $90^\\circ$; hai đường chéo bằng nhau là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Hình vuông cạnh a',
                        'Tam giác đều cạnh a',
                        'Lục giác đều cạnh a',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 0,
            'solution': 'Trong Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều, biểu thức/quy tắc '
                        '$4$ cạnh bằng $a$; mỗi góc bằng $90^\\circ$; hai đường chéo bằng nhau chính là nội '
                        'dung của **Hình vuông cạnh a**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình lục giác đều $ABCDEF$ có cạnh $AB = 4\\text{ cm}$. Độ dài đường chéo chính $AD$ '
                 'bằng:',
            'options': ['$4\\text{ cm}$', '$8\\text{ cm}$', '$12\\text{ cm}$', '$6\\text{ cm}$'],
            'answer': 1,
            'solution': 'Đường chéo chính của lục giác đều gấp đôi độ dài cạnh: $AD = 2 \\cdot 4 = 8\\text{ '
                        'cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều** (Chương IV: Một số '
                 'hình phẳng trong thực tiễn), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Mô tả được đặc điểm về cạnh, góc, đường chéo của tam giác đều, hình vuông, lục giác '
                        'đều.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều: '
                        'Mô tả được đặc điểm về cạnh, góc, đường chéo của tam giác đều, hình vuông, lục giác '
                        'đều.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các hình tam giác đều, hình vuông và hình lục giác đều. Mỗi khẳng định sau đúng hay '
                 'sai?',
            'statements': ['Hai đường chéo của hình vuông bằng nhau',
                           'Hình lục giác đều được ghép từ $6$ hình tam giác đều bằng nhau',
                           'Mỗi góc của hình vuông bằng $60^\\circ$',
                           'Ba đường chéo chính của hình lục giác đều bằng nhau'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì mỗi góc của hình vuông bằng $90^\\circ$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 18: Hình tam giác đều. '
                 'Hình vuông. Hình lục giác đều**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được đặc điểm về cạnh, góc, '
                           'đường chéo của tam giác đều, hình vuông, lục giác đều.',
                           'Quy tắc/công thức **Tam giác đều cạnh a** trong bài được xác định bởi: $3$ cạnh '
                           'bằng $a$; mỗi góc bằng $60^\\circ$.',
                           'Trong mọi trường hợp, **Tam giác đều cạnh a** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 18: Hình tam giác đều. Hình vuông. '
                           'Hình lục giác đều.',
                           'Với bài toán minh họa: “Một hình lục giác đều có độ dài một cạnh là $5\\text{ '
                           'cm}$. Tính chu vi và độ dài đường chéo chính của lục giác đều đó.”, lời giải '
                           'đúng là: Chu vi lục giác đều là $6 \\cdot 5 = 30\\text{ cm}$. Độ dài đường chéo '
                           'chính là $2 \\cdot 5 = 10\\text{ cm}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Hình tam giác đều. Hình vuông. Hình '
                        'lục giác đều. b) **Đúng** theo công thức trọng tâm **Tam giác đều cạnh a** ($3$ '
                        'cạnh bằng $a$; mỗi góc bằng $60^\\circ$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); '
                        '$y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy '
                        'tắc chung của **Tam giác đều cạnh a**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều** để giải '
                 'quyết tình huống sau: Một hình lục giác đều có độ dài một cạnh là $5\\text{ cm}$. Tính chu '
                 'vi và độ dài đường chéo chính của lục giác đều đó. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Chu vi lục giác đều là $6 \\cdot 5 = 30\\text{ cm}$. Độ dài đường chéo chính là $2 '
                        '\\cdot 5 = 10\\text{ cm}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều: '
                        'Chu vi lục giác đều là $6 \\cdot 5 = 30\\text{ cm}$. Độ dài đường chéo chính là $2 '
                        '\\cdot 5 = 10\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khung trang trí hình lục giác đều có cạnh $15\\text{ cm}$ được uốn từ một sợi dây '
                 'thép. Cần bao nhiêu xăng-ti-mét dây thép để uốn khung đó (không tính mối nối)?',
            'answer': ['90'],
            'unit': None,
            'solution': 'Chu vi khung hình lục giác đều là $6 \\cdot 15 = 90$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch04-hinh-phang-trong-thuc-tien',
  'context_title': 'Chương IV: Một số hình phẳng trong thực tiễn',
  'context': 'Chương IV · SGK Toán 6: Nhận dạng, tính chất và công thức tính chu vi, diện tích các hình '
             'phẳng.',
  'title': 'Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang cân',
  'icon': '⬡',
  'description': 'Nhận biết và mô tả các tính chất về cạnh, góc, đường chéo của hình chữ nhật, hình thoi, '
                 'hình bình hành, hình thang cân.',
  'requirements': ['Nêu được tính chất về cạnh đối, góc và đường chéo của hình chữ nhật, hình thoi, hình '
                   'bình hành, hình thang cân.',
                   'Vẽ được hình chữ nhật, hình bình hành, hình thoi bằng thước kẻ, ê-ke và compa.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hình chữ nhật và Hình thang cân** (Có hai '
                   'đường chéo bằng nhau) vào giải bài tập.'],
  'definition': '- **Hình chữ nhật**: có $4$ góc vuông, các cạnh đối bằng nhau, **hai đường chéo bằng nhau** '
                'và cắt nhau tại trung điểm của mỗi đường.\n'
                '- **Hình thoi**: có $4$ cạnh bằng nhau, các cạnh đối song song, **hai đường chéo vuông '
                'góc** với nhau.\n'
                '- **Hình bình hành**: các cạnh đối song song và bằng nhau, các góc đối bằng nhau, hai đường '
                'chéo cắt nhau tại trung điểm của mỗi đường.\n'
                '- **Hình thang cân**: có hai đáy song song, hai cạnh bên bằng nhau, hai góc kề một đáy bằng '
                'nhau và **hai đường chéo bằng nhau**.',
  'theory': '### 1. So sánh tính chất đường chéo\n'
            '- Hai đường chéo **bằng nhau**: hình chữ nhật, hình vuông, hình thang cân.\n'
            '- Hai đường chéo **vuông góc**: hình thoi, hình vuông.\n'
            '- Hai đường chéo **cắt nhau tại trung điểm mỗi đường**: hình bình hành, hình chữ nhật, hình '
            'thoi, hình vuông.',
  'formulas': [{'category': 'I. Tính chất đặc trưng của tứ giác',
                'items': [{'name': 'Hình chữ nhật và Hình thang cân',
                           'formula': 'Có hai đường chéo bằng nhau'},
                          {'name': 'Hình thoi và Hình vuông',
                           'formula': 'Có $4$ cạnh bằng nhau và hai đường chéo vuông góc'}]}],
  'example': 'Cho hình bình hành $ABCD$ có $AB = 7\\text{ cm}$, $BC = 5\\text{ cm}$. Tìm độ dài các cạnh '
             '$CD$ và $AD$.',
  'example_answer': 'Trong hình bình hành các cạnh đối bằng nhau nên $CD = AB = 7\\text{ cm}$ và $AD = BC = '
                    '5\\text{ cm}$.',
  'real_life': 'Khung cửa sổ hình chữ nhật, hoa văn hàng rào xếp hình thoi và mặt bàn hình thang cân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các hình sau, hình nào luôn có hai đường chéo vuông góc với nhau?',
            'options': ['Hình chữ nhật', 'Hình bình hành', 'Hình thoi', 'Hình thang cân'],
            'answer': 2,
            'solution': 'Hình thoi có hai đường chéo vuông góc với nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hình thang cân, khẳng định nào sau đây là đúng?',
            'options': ['Bốn cạnh bằng nhau',
                        'Hai đường chéo vuông góc',
                        'Bốn góc bằng nhau',
                        'Hai đường chéo bằng nhau'],
            'answer': 3,
            'solution': 'Hình thang cân có hai cạnh bên bằng nhau và hai đường chéo bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang '
                 'cân**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hình chữ nhật và Hình thang '
                 'cân**?',
            'options': ['Có hai đường chéo bằng nhau',
                        'Có $4$ cạnh bằng nhau và hai đường chéo vuông góc',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. '
                        'Hình thang cân, **Hình chữ nhật và Hình thang cân** được xác định bởi: Có hai đường '
                        'chéo bằng nhau.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang cân**, nội dung/biểu '
                 'thức Có $4$ cạnh bằng nhau và hai đường chéo vuông góc là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Hình chữ nhật và Hình thang cân',
                        'Hình thoi và Hình vuông',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang cân, biểu '
                        'thức/quy tắc Có $4$ cạnh bằng nhau và hai đường chéo vuông góc chính là nội dung '
                        'của **Hình thoi và Hình vuông**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chữ nhật $ABCD$ có đường chéo $AC = 10\\text{ cm}$. Gọi $O$ là giao điểm của hai '
                 'đường chéo. Độ dài đoạn thẳng $OB$ là:',
            'options': ['$10\\text{ cm}$', '$20\\text{ cm}$', '$5\\text{ cm}$', '$2{,}5\\text{ cm}$'],
            'answer': 2,
            'solution': 'Trong hình chữ nhật $BD = AC = 10\\text{ cm}$ và $O$ là trung điểm của $BD$ nên $OB '
                        '= 10 : 2 = 5\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang cân** (Chương IV: '
                 'Một số hình phẳng trong thực tiễn), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Nêu được tính chất về cạnh đối, góc và đường chéo của hình chữ nhật, hình thoi, '
                        'hình bình hành, hình thang cân.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình '
                        'thang cân: Nêu được tính chất về cạnh đối, góc và đường chéo của hình chữ nhật, '
                        'hình thoi, hình bình hành, hình thang cân.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Mỗi khẳng định sau về các tứ giác đặc biệt đúng hay sai?',
            'statements': ['Hình thoi có hai đường chéo vuông góc với nhau',
                           'Hình bình hành luôn có hai đường chéo bằng nhau',
                           'Hình thang cân có hai cạnh bên bằng nhau',
                           'Hình chữ nhật có các cạnh đối song song và bằng nhau'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai (chỉ khi là hình chữ nhật). c) Đúng. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 19: Hình chữ nhật. Hình '
                 'thoi. Hình bình hành. Hình thang cân**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nêu được tính chất về cạnh đối, '
                           'góc và đường chéo của hình chữ nhật, hình thoi, hình bình hành, hình thang cân.',
                           'Quy tắc/công thức **Hình chữ nhật và Hình thang cân** trong bài được xác định '
                           'bởi: Có hai đường chéo bằng nhau.',
                           'Trong mọi trường hợp, **Hình chữ nhật và Hình thang cân** luôn được tính bằng '
                           'công thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc '
                           'Quan hệ phần tử – tập hợp) mà không cần điều kiện của Bài 19: Hình chữ nhật. '
                           'Hình thoi. Hình bình hành. Hình thang cân.',
                           'Với bài toán minh họa: “Cho hình bình hành $ABCD$ có $AB = 7\\text{ cm}$, $BC = '
                           '5\\text{ cm}$. Tìm độ dài các cạnh $CD$ và $AD$.”, lời giải đúng là: Trong hình '
                           'bình hành các cạnh đối bằng nhau nên $CD = AB = 7\\text{ cm}$ và $AD = BC = '
                           '5\\text{ cm}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Hình chữ nhật. Hình thoi. Hình bình '
                        'hành. Hình thang cân. b) **Đúng** theo công thức trọng tâm **Hình chữ nhật và Hình '
                        'thang cân** (Có hai đường chéo bằng nhau). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Hình chữ nhật và Hình thang cân**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang cân** để '
                 'giải quyết tình huống sau: Cho hình bình hành $ABCD$ có $AB = 7\\text{ cm}$, $BC = '
                 '5\\text{ cm}$. Tìm độ dài các cạnh $CD$ và $AD$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Trong hình bình hành các cạnh đối bằng nhau nên $CD = AB = 7\\text{ cm}$ và $AD = '
                        'BC = 5\\text{ cm}$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Hình chữ nhật. Hình thoi. Hình bình hành. Hình thang '
                        'cân: Trong hình bình hành các cạnh đối bằng nhau nên $CD = AB = 7\\text{ cm}$ và '
                        '$AD = BC = 5\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình bình hành có hai cạnh kề nhau dài $12\\text{ cm}$ và $8\\text{ cm}$. Tính tổng độ '
                 'dài bốn cạnh của hình bình hành đó (đơn vị cm).',
            'answer': ['40'],
            'unit': None,
            'solution': 'Các cạnh đối của hình bình hành bằng nhau nên tổng độ dài bốn cạnh là $2 \\cdot (12 '
                        '+ 8) = 40$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch04-hinh-phang-trong-thuc-tien',
  'context_title': 'Chương IV: Một số hình phẳng trong thực tiễn',
  'context': 'Chương IV · SGK Toán 6: Nhận dạng, tính chất và công thức tính chu vi, diện tích các hình '
             'phẳng.',
  'title': 'Bài 20: Chu vi và diện tích của một số tứ giác đã học',
  'icon': '⬡',
  'description': 'Công thức tính chu vi và diện tích của hình vuông, hình chữ nhật, hình bình hành, hình '
                 'thoi và hình thang.',
  'requirements': ['Tính được chu vi và diện tích của hình vuông, hình chữ nhật, hình bình hành, hình thoi, '
                   'hình thang.',
                   'Giải được bài toán thực tế về tính diện tích sân vườn, lối đi và chi phí xây dựng.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hình vuông và Hình thoi cạnh a** ($C = 4a$) '
                   'vào giải bài tập.'],
  'definition': '- **Chu vi** của một tứ giác bằng tổng độ dài bốn cạnh của nó.\n'
                '- **Diện tích hình bình hành**: $S = a \\cdot h$ (đáy nhân chiều cao). **Diện tích hình '
                'thoi**: $S = \\dfrac{m \\cdot n}{2}$ (nửa tích hai đường chéo).\n'
                '- **Diện tích hình thang**: $S = \\dfrac{(a + b) \\cdot h}{2}$.',
  'theory': '### 1. Hệ thống công thức chu vi và diện tích\n'
            '- Hình vuông cạnh $a$: $C = 4a$, $S = a^2$.\n'
            '- Hình chữ nhật cạnh $a, b$: $C = 2(a + b)$, $S = a \\cdot b$.\n'
            '- Hình bình hành cạnh $a, b$, chiều cao $h$ ứng với cạnh $a$: $C = 2(a + b)$, $S = a \\cdot '
            'h$.\n'
            '- Hình thoi cạnh $a$, hai đường chéo $m, n$: $C = 4a$, $S = \\dfrac{m \\cdot n}{2}$.',
  'formulas': [{'category': 'I. Chu vi các tứ giác',
                'items': [{'name': 'Hình vuông và Hình thoi cạnh a', 'formula': '$C = 4a$'},
                          {'name': 'Hình chữ nhật và Hình bình hành cạnh a, b',
                           'formula': '$C = 2(a + b)$'}]},
               {'category': 'II. Diện tích các tứ giác',
                'items': [{'name': 'Hình vuông và Hình chữ nhật',
                           'formula': '$S_{\\text{vuông}} = a^2$; $S_{\\text{CN}} = a \\cdot b$'},
                          {'name': 'Hình bình hành và Hình thoi',
                           'formula': '$S_{\\text{BH}} = a \\cdot h$; $S_{\\text{thoi}} = \\dfrac{m \\cdot '
                                      'n}{2}$'},
                          {'name': 'Hình thang',
                           'formula': '$S_{\\text{thang}} = \\dfrac{(a + b) \\cdot h}{2}$'}]}],
  'example': 'Một mảnh đất hình thang cân có hai đáy $30\\text{ m}$ và $20\\text{ m}$, chiều cao $12\\text{ '
             'm}$. Tính diện tích mảnh đất đó.',
  'example_answer': 'Diện tích mảnh đất là $S = \\dfrac{(30 + 20) \\cdot 12}{2} = 300\\text{ m}^2$.',
  'real_life': 'Tính diện tích đất trồng rau sau khi trừ lối đi và tính số viên gạch cần lát sân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích hình bình hành có độ dài đáy $a$ và chiều cao tương ứng $h$ là:',
            'options': ['$S = \\dfrac{a \\cdot h}{2}$',
                        '$S = 2(a + h)$',
                        '$S = (a + h) : 2$',
                        '$S = a \\cdot h$'],
            'answer': 3,
            'solution': 'Diện tích hình bình hành bằng đáy nhân chiều cao: $S = a \\cdot h$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình thoi có độ dài hai đường chéo là $10\\text{ cm}$ và $6\\text{ cm}$. Diện tích của '
                 'hình thoi đó là:',
            'options': ['$30\\text{ cm}^2$', '$60\\text{ cm}^2$', '$16\\text{ cm}^2$', '$32\\text{ cm}^2$'],
            'answer': 0,
            'solution': 'Ta có $S = \\dfrac{10 \\cdot 6}{2} = 30\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 20: Chu vi và diện tích của một số tứ giác đã học**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hình vuông và Hình thoi cạnh a**?',
            'options': ['$C = 2(a + b)$',
                        '$C = 4a$',
                        '$S_{\\text{vuông}} = a^2$; $S_{\\text{CN}} = a \\cdot b$',
                        '$S_{\\text{BH}} = a \\cdot h$; $S_{\\text{thoi}} = \\dfrac{m \\cdot n}{2}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 20: Chu vi và diện tích của một số tứ giác đã '
                        'học, **Hình vuông và Hình thoi cạnh a** được xác định bởi: $C = 4a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Chu vi và diện tích của một số tứ giác đã học**, nội dung/biểu thức $C = '
                 '2(a + b)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hình vuông và Hình thoi cạnh a',
                        'Hình vuông và Hình chữ nhật',
                        'Hình chữ nhật và Hình bình hành cạnh a, b',
                        'Hình bình hành và Hình thoi'],
            'answer': 2,
            'solution': 'Trong Bài 20: Chu vi và diện tích của một số tứ giác đã học, biểu thức/quy tắc $C = '
                        '2(a + b)$ chính là nội dung của **Hình chữ nhật và Hình bình hành cạnh a, b**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình chữ nhật có chu vi $30\\text{ m}$ và chiều dài $9\\text{ m}$. Diện tích của hình '
                 'chữ nhật đó là:',
            'options': ['$270\\text{ m}^2$', '$81\\text{ m}^2$', '$42\\text{ m}^2$', '$54\\text{ m}^2$'],
            'answer': 3,
            'solution': 'Nửa chu vi là $30 : 2 = 15\\text{ m} \\Rightarrow$ chiều rộng là $15 - 9 = 6\\text{ '
                        'm}$. Diện tích là $9 \\cdot 6 = 54\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Chu vi và diện tích của một số tứ giác đã học** (Chương IV: Một số hình '
                 'phẳng trong thực tiễn), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Tính được chu vi và diện tích của hình vuông, hình chữ nhật, hình bình hành, hình '
                        'thoi, hình thang.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 20: Chu vi và diện tích của một số tứ giác đã học: '
                        'Tính được chu vi và diện tích của hình vuông, hình chữ nhật, hình bình hành, hình '
                        'thoi, hình thang.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét diện tích của các hình tứ giác. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Hình thoi có hai đường chéo $6\\text{ cm}$ và $8\\text{ cm}$ có diện tích '
                           '$24\\text{ cm}^2$',
                           'Hình bình hành đáy $10\\text{ cm}$, chiều cao $4\\text{ cm}$ có diện tích '
                           '$40\\text{ cm}^2$',
                           'Hình thang có hai đáy $5\\text{ cm}$ và $9\\text{ cm}$, chiều cao $4\\text{ cm}$ '
                           'có diện tích $56\\text{ cm}^2$',
                           'Hình vuông có chu vi $20\\text{ cm}$ thì diện tích là $25\\text{ cm}^2$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng ($6 \\cdot 8 : 2 = 24$). b) Đúng ($10 \\cdot 4 = 40$). c) Sai vì $(5 + 9) '
                        '\\cdot 4 : 2 = 28\\text{ cm}^2$. d) Đúng (cạnh $5\\text{ cm} \\Rightarrow S = '
                        '25\\text{ cm}^2$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 20: Chu vi và diện tích '
                 'của một số tứ giác đã học**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được chu vi và diện tích của '
                           'hình vuông, hình chữ nhật, hình bình hành, hình thoi, hình thang.',
                           'Quy tắc/công thức **Hình vuông và Hình thoi cạnh a** trong bài được xác định '
                           'bởi: $C = 4a$.',
                           'Trong mọi trường hợp, **Hình vuông và Hình thoi cạnh a** luôn được tính bằng '
                           'công thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc '
                           'Quan hệ phần tử – tập hợp) mà không cần điều kiện của Bài 20: Chu vi và diện '
                           'tích của một số tứ giác đã học.',
                           'Với bài toán minh họa: “Một mảnh đất hình thang cân có hai đáy $30\\text{ m}$ và '
                           '$20\\text{ m}$, chiều cao $12\\text{ m}$. Tính diện tích mảnh đất đó.”, lời giải '
                           'đúng là: Diện tích mảnh đất là $S = \\dfrac{(30 + 20) \\cdot 12}{2} = 300\\text{ '
                           'm}^2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 20: Chu vi và diện tích của một số tứ giác '
                        'đã học. b) **Đúng** theo công thức trọng tâm **Hình vuông và Hình thoi cạnh a** ($C '
                        '= 4a$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc '
                        '$A$) là công thức của nội dung khác, không phải quy tắc chung của **Hình vuông và '
                        'Hình thoi cạnh a**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 20: Chu vi và diện tích của một số tứ giác đã học** để giải quyết '
                 'tình huống sau: Một mảnh đất hình thang cân có hai đáy $30\\text{ m}$ và $20\\text{ m}$, '
                 'chiều cao $12\\text{ m}$. Tính diện tích mảnh đất đó. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Diện tích mảnh đất là $S = \\dfrac{(30 + 20) \\cdot 12}{2} = 300\\text{ m}^2$.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Chu vi và diện tích của một số tứ giác đã học: Diện '
                        'tích mảnh đất là $S = \\dfrac{(30 + 20) \\cdot 12}{2} = 300\\text{ m}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khu vườn hình chữ nhật dài $25\\text{ m}$, rộng $16\\text{ m}$. Người ta làm một lối '
                 'đi hình bình hành có đáy $2\\text{ m}$ và chiều cao bằng chiều rộng khu vườn ($16\\text{ '
                 'm}$). Tính diện tích phần đất còn lại để trồng rau (đơn vị m²).',
            'answer': ['368'],
            'unit': None,
            'solution': 'Diện tích khu vườn là $25 \\cdot 16 = 400\\text{ m}^2$; diện tích lối đi là $2 '
                        '\\cdot 16 = 32\\text{ m}^2$. Diện tích trồng rau là $400 - 32 = 368\\text{ m}^2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch05-tinh-doi-xung',
  'context_title': 'Chương V: Tính đối xứng của hình phẳng trong tự nhiên',
  'context': 'Chương V · SGK Toán 6: Hình có trục đối xứng, hình có tâm đối xứng và tính đối xứng trong tự '
             'nhiên.',
  'title': 'Bài 21: Hình có trục đối xứng',
  'icon': '🦋',
  'description': 'Nhận biết hình có trục đối xứng, xác định trục đối xứng của các hình phẳng quen thuộc và '
                 'trong tự nhiên.',
  'requirements': ['Nhận biết được hình phẳng có trục đối xứng thông qua thao tác gấp đôi chồng khít.',
                   'Xác định đúng số trục đối xứng của đoạn thẳng, hình tròn, tam giác đều, hình vuông, hình '
                   'chữ nhật, hình thoi, hình thang cân.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hình thang cân / Hình chữ nhật / Hình '
                   'thoi** (Thang cân: $1$ trục; Chữ nhật: $2$ trục; Thoi: $2$ trục) vào giải bài tập.'],
  'definition': '- Một hình được gọi là **hình có trục đối xứng** nếu có một đường thẳng $d$ chia hình thành '
                'hai phần mà khi ta **gấp hình theo đường thẳng $d$** thì hai phần đó **chồng khít** lên '
                'nhau.\n'
                '- Đường thẳng $d$ như vậy được gọi là **trục đối xứng** của hình.',
  'theory': '### 1. Số trục đối xứng của các hình cơ bản\n'
            '- Hình thang cân: $1$ trục đối xứng (đường thẳng đi qua trung điểm hai đáy).\n'
            '- Hình chữ nhật (không vuông) và hình thoi (không vuông): $2$ trục đối xứng.\n'
            '- Hình tam giác đều: $3$ trục đối xứng.\n'
            '- Hình vuông: $4$ trục đối xứng ($2$ đường chéo và $2$ đường thẳng đi qua trung điểm các cặp '
            'cạnh đối).\n'
            '- Hình lục giác đều: $6$ trục đối xứng. Hình tròn: **vô số** trục đối xứng (mọi đường thẳng đi '
            'qua tâm).\n'
            '- Hình bình hành (không phải hình chữ nhật hay hình thoi) **không có** trục đối xứng.',
  'formulas': [{'category': 'I. Bảng số trục đối xứng',
                'items': [{'name': 'Hình thang cân / Hình chữ nhật / Hình thoi',
                           'formula': 'Thang cân: $1$ trục; Chữ nhật: $2$ trục; Thoi: $2$ trục'},
                          {'name': 'Đa giác đều và Hình tròn',
                           'formula': 'Tam giác đều: $3$ trục; Hình vuông: $4$ trục; Lục giác đều: $6$ trục; '
                                      'Hình tròn: vô số trục'}]}],
  'example': 'Trong các chữ cái in hoa $\\text{A}, \\text{H}, \\text{N}, \\text{M}$, những chữ cái nào có '
             'trục đối xứng?',
  'example_answer': 'Các chữ cái có trục đối xứng là $\\text{A}$ ($1$ trục dọc), $\\text{H}$ ($2$ trục dọc '
                    'và ngang), $\\text{M}$ ($1$ trục dọc). Chữ $\\text{N}$ không có trục đối xứng.',
  'real_life': 'Hình ảnh đôi cánh bướm, chiếc lá, khuôn mặt con người và các công trình kiến trúc đối xứng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình vuông có tất cả bao nhiêu trục đối xứng?',
            'options': ['$4$ trục', '$1$ trục', '$2$ trục', 'Vô số trục'],
            'answer': 0,
            'solution': 'Hình vuông có $4$ trục đối xứng ($2$ đường chéo và $2$ đường nối trung điểm các '
                        'cạnh đối).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tròn có bao nhiêu trục đối xứng?',
            'options': ['$1$ trục', 'Vô số trục', '$2$ trục', '$4$ trục'],
            'answer': 1,
            'solution': 'Mọi đường thẳng đi qua tâm của hình tròn đều là trục đối xứng nên có vô số trục.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 21: Hình có trục đối xứng**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Hình thang cân / Hình chữ nhật / Hình thoi**?',
            'options': ['Tam giác đều: $3$ trục; Hình vuông: $4$ trục; Lục giác đều: $6$ trục; Hình tròn: vô '
                        'số trục',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Thang cân: $1$ trục; Chữ nhật: $2$ trục; Thoi: $2$ trục',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 21: Hình có trục đối xứng, **Hình thang cân / '
                        'Hình chữ nhật / Hình thoi** được xác định bởi: Thang cân: $1$ trục; Chữ nhật: $2$ '
                        'trục; Thoi: $2$ trục.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Hình có trục đối xứng**, nội dung/biểu thức Tam giác đều: $3$ trục; Hình '
                 'vuông: $4$ trục; Lục giác đều: $6$ trục; Hình tròn: vô số trục là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Hình thang cân / Hình chữ nhật / Hình thoi',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả',
                        'Đa giác đều và Hình tròn'],
            'answer': 3,
            'solution': 'Trong Bài 21: Hình có trục đối xứng, biểu thức/quy tắc Tam giác đều: $3$ trục; Hình '
                        'vuông: $4$ trục; Lục giác đều: $6$ trục; Hình tròn: vô số trục chính là nội dung '
                        'của **Đa giác đều và Hình tròn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một tờ giấy hình chữ nhật (không phải hình vuông) có bao nhiêu cách gấp đôi để hai nửa '
                 'chồng khít lên nhau?',
            'options': ['$2$ cách', '$1$ cách', '$4$ cách', '$0$ cách'],
            'answer': 0,
            'solution': 'Số cách gấp đôi chồng khít bằng số trục đối xứng của hình chữ nhật là $2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Hình có trục đối xứng** (Chương V: Tính đối xứng của hình phẳng trong tự '
                 'nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Nhận biết được hình phẳng có trục đối xứng thông qua thao tác gấp đôi chồng khít.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 21: Hình có trục đối xứng: Nhận biết được hình phẳng '
                        'có trục đối xứng thông qua thao tác gấp đôi chồng khít.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Mỗi khẳng định sau về trục đối xứng đúng hay sai?',
            'statements': ['Hình tam giác đều có $3$ trục đối xứng',
                           'Hình thang cân có $1$ trục đối xứng',
                           'Hai đường chéo của hình chữ nhật (không vuông) là trục đối xứng của nó',
                           'Hình lục giác đều có $6$ trục đối xứng'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì khi gấp hình chữ nhật theo đường chéo hai nửa không '
                        'chồng khít. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 21: Hình có trục đối '
                 'xứng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hình phẳng có trục '
                           'đối xứng thông qua thao tác gấp đôi chồng khít.',
                           'Quy tắc/công thức **Hình thang cân / Hình chữ nhật / Hình thoi** trong bài được '
                           'xác định bởi: Thang cân: $1$ trục; Chữ nhật: $2$ trục; Thoi: $2$ trục.',
                           'Trong mọi trường hợp, **Hình thang cân / Hình chữ nhật / Hình thoi** luôn được '
                           'tính bằng công thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc '
                           '$A$) (thuộc Quan hệ phần tử – tập hợp) mà không cần điều kiện của Bài 21: Hình '
                           'có trục đối xứng.',
                           'Với bài toán minh họa: “Trong các chữ cái in hoa $\\text{A}, \\text{H}, '
                           '\\text{N}, \\text{M}$, những chữ cái nào có trục đối xứng?”, lời giải đúng là: '
                           'Các chữ cái có trục đối xứng là $\\text{A}$ ($1$ trục dọc), $\\text{H}$ ($2$ '
                           'trục dọc và ngang), $\\text{M}$ ($1$ trục dọc). Chữ $\\text{N}$ khô...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 21: Hình có trục đối xứng. b) **Đúng** '
                        'theo công thức trọng tâm **Hình thang cân / Hình chữ nhật / Hình thoi** (Thang cân: '
                        '$1$ trục; Chữ nhật: $2$ trục; Thoi: $2$ trục). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Hình thang cân / Hình chữ nhật / Hình thoi**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 21: Hình có trục đối xứng** để giải quyết tình huống sau: Trong '
                 'các chữ cái in hoa $\\text{A}, \\text{H}, \\text{N}, \\text{M}$, những chữ cái nào có trục '
                 'đối xứng? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các chữ cái có trục đối xứng là $\\text{A}$ ($1$ trục dọc), $\\text{H}$ ($2$ trục '
                        'dọc và ngang), $\\text{M}$ ($1$ trục dọc). Chữ $\\text{N}$ không có trục đối...',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Hình có trục đối xứng: Các chữ cái có trục đối xứng '
                        'là $\\text{A}$ ($1$ trục dọc), $\\text{H}$ ($2$ trục dọc và ngang), $\\text{M}$ '
                        '($1$ trục dọc). Chữ $\\text{N}$ không có trục đối xứng.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính tổng số trục đối xứng của một hình tam giác đều và một hình vuông.',
            'answer': ['7'],
            'unit': None,
            'solution': 'Hình tam giác đều có $3$ trục đối xứng, hình vuông có $4$ trục đối xứng. Tổng cộng '
                        'là $3 + 4 = 7$ (trục).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch05-tinh-doi-xung',
  'context_title': 'Chương V: Tính đối xứng của hình phẳng trong tự nhiên',
  'context': 'Chương V · SGK Toán 6: Hình có trục đối xứng, hình có tâm đối xứng và tính đối xứng trong tự '
             'nhiên.',
  'title': 'Bài 22: Hình có tâm đối xứng',
  'icon': '🦋',
  'description': 'Nhận biết hình có tâm đối xứng, xác định tâm đối xứng của các hình phẳng quen thuộc và '
                 'trong tự nhiên.',
  'requirements': ['Nhận biết được hình phẳng có tâm đối xứng thông qua phép quay nửa vòng ($180^\\circ$).',
                   'Phân biệt được hình nào có tâm đối xứng, hình nào có trục đối xứng hoặc có cả hai.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Các hình CÓ tâm đối xứng** (Đoạn thẳng, '
                   'Hình bình hành, Chữ nhật, Thoi, Vuông, Lục giác đều, Hình tròn) vào giải bài tập.'],
  'definition': '- Một hình được gọi là **hình có tâm đối xứng** nếu có một điểm $O$ sao cho khi ta **quay '
                'hình một nửa vòng ($180^\\circ$)** quanh điểm $O$ thì hình thu được **chồng khít** với '
                'chính nó ở vị trí ban đầu.\n'
                '- Điểm $O$ như vậy được gọi là **tâm đối xứng** của hình.',
  'theory': '### 1. Tâm đối xứng của các hình cơ bản\n'
            '- Tâm đối xứng của **đoạn thẳng** là trung điểm của nó; của **hình tròn** là tâm hình tròn.\n'
            '- **Hình bình hành, hình chữ nhật, hình thoi, hình vuông**: đều có tâm đối xứng là **giao điểm '
            'của hai đường chéo**.\n'
            '- **Hình lục giác đều**: có tâm đối xứng là giao điểm của ba đường chéo chính.\n'
            '- **Hình tam giác đều** và **hình thang cân**: **không có** tâm đối xứng.',
  'formulas': [{'category': 'I. Phân loại đối xứng tâm',
                'items': [{'name': 'Các hình CÓ tâm đối xứng',
                           'formula': 'Đoạn thẳng, Hình bình hành, Chữ nhật, Thoi, Vuông, Lục giác đều, Hình '
                                      'tròn'},
                          {'name': 'Các hình KHÔNG có tâm đối xứng',
                           'formula': 'Hình tam giác đều, Hình thang cân, Ngũ giác đều'}]}],
  'example': 'Trong các chữ cái in hoa $\\text{H}, \\text{A}, \\text{N}, \\text{O}, \\text{Z}$, chữ cái nào '
             'có tâm đối xứng?',
  'example_answer': 'Các chữ cái khi quay $180^\\circ$ trùng với chính nó là $\\text{H}, \\text{N}, '
                    '\\text{O}, \\text{Z}$ (chữ $\\text{A}$ không có tâm đối xứng).',
  'real_life': 'Cánh quạt trần, bông hoa, hoa văn gạch lát nền và biển báo cấm đỗ xe.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình nào sau đây **không** có tâm đối xứng?',
            'options': ['Hình chữ nhật', 'Hình tam giác đều', 'Hình thoi', 'Hình tròn'],
            'answer': 1,
            'solution': 'Hình tam giác đều có $3$ trục đối xứng nhưng không có tâm đối xứng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tâm đối xứng của một hình bình hành là:',
            'options': ['Một đỉnh bất kì',
                        'Trung điểm của một cạnh',
                        'Giao điểm của hai đường chéo',
                        'Không có tâm đối xứng'],
            'answer': 2,
            'solution': 'Tâm đối xứng của hình bình hành là giao điểm của hai đường chéo.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 22: Hình có tâm đối xứng**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Các hình CÓ tâm đối xứng**?',
            'options': ['Hình tam giác đều, Hình thang cân, Ngũ giác đều',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        'Đoạn thẳng, Hình bình hành, Chữ nhật, Thoi, Vuông, Lục giác đều, Hình tròn'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 22: Hình có tâm đối xứng, **Các hình CÓ tâm '
                        'đối xứng** được xác định bởi: Đoạn thẳng, Hình bình hành, Chữ nhật, Thoi, Vuông, '
                        'Lục giác đều, Hình tròn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Hình có tâm đối xứng**, nội dung/biểu thức Hình tam giác đều, Hình thang '
                 'cân, Ngũ giác đều là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Các hình KHÔNG có tâm đối xứng',
                        'Các hình CÓ tâm đối xứng',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 22: Hình có tâm đối xứng, biểu thức/quy tắc Hình tam giác đều, Hình thang '
                        'cân, Ngũ giác đều chính là nội dung của **Các hình KHÔNG có tâm đối xứng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Chữ cái in hoa nào sau đây có tâm đối xứng nhưng **không** có trục đối xứng?',
            'options': ['Chữ A', 'Chữ N', 'Chữ H', 'Chữ M'],
            'answer': 1,
            'solution': 'Chữ $\\text{N}$ quay $180^\\circ$ trùng với chính nó (có tâm đối xứng) nhưng không '
                        'có trục đối xứng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Hình có tâm đối xứng** (Chương V: Tính đối xứng của hình phẳng trong tự '
                 'nhiên), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Nhận biết được hình phẳng có tâm đối xứng thông qua phép quay nửa vòng '
                        '($180^\\circ$).',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 22: Hình có tâm đối xứng: Nhận biết được hình phẳng có '
                        'tâm đối xứng thông qua phép quay nửa vòng ($180^\\circ$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đối xứng của các chữ cái in hoa $\\text{H}, \\text{A}, \\text{N}$ và các hình tứ '
                 'giác. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Chữ H có cả trục đối xứng và tâm đối xứng',
                           'Chữ A có tâm đối xứng',
                           'Hình bình hành có tâm đối xứng',
                           'Hình thang cân có tâm đối xứng'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng. b) Sai (chữ A chỉ có trục đối xứng). c) Đúng. d) Sai (hình thang cân chỉ '
                        'có trục đối xứng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 22: Hình có tâm đối '
                 'xứng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hình phẳng có tâm '
                           'đối xứng thông qua phép quay nửa vòng ($180^\\circ$).',
                           'Quy tắc/công thức **Các hình CÓ tâm đối xứng** trong bài được xác định bởi: Đoạn '
                           'thẳng, Hình bình hành, Chữ nhật, Thoi, Vuông, Lục giác đều, Hình tròn.',
                           'Trong mọi trường hợp, **Các hình CÓ tâm đối xứng** luôn được tính bằng công thức '
                           '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ '
                           'phần tử – tập hợp) mà không cần điều kiện của Bài 22: Hình có tâm đối xứng.',
                           'Với bài toán minh họa: “Trong các chữ cái in hoa $\\text{H}, \\text{A}, '
                           '\\text{N}, \\text{O}, \\text{Z}$, chữ cái nào có tâm đối xứng?”, lời giải đúng '
                           'là: Các chữ cái khi quay $180^\\circ$ trùng với chính nó là $\\text{H}, '
                           '\\text{N}, \\text{O}, \\text{Z}$ (chữ $\\text{A}$ không có tâm đối xứng).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 22: Hình có tâm đối xứng. b) **Đúng** theo '
                        'công thức trọng tâm **Các hình CÓ tâm đối xứng** (Đoạn thẳng, Hình bình hành, Chữ '
                        'nhật, Thoi, Vuông, Lục giác đều, Hình tròn). c) **Sai** vì $x \\in A$ ($x$ thuộc '
                        '$A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Các hình CÓ tâm đối xứng**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 22: Hình có tâm đối xứng** để giải quyết tình huống sau: Trong '
                 'các chữ cái in hoa $\\text{H}, \\text{A}, \\text{N}, \\text{O}, \\text{Z}$, chữ cái nào có '
                 'tâm đối xứng? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Các chữ cái khi quay $180^\\circ$ trùng với chính nó là $\\text{H}, \\text{N}, '
                        '\\text{O}, \\text{Z}$ (chữ $\\text{A}$ không có tâm đối xứng).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Hình có tâm đối xứng: Các chữ cái khi quay '
                        '$180^\\circ$ trùng với chính nó là $\\text{H}, \\text{N}, \\text{O}, \\text{Z}$ '
                        '(chữ $\\text{A}$ không có tâm đối xứng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong $6$ chữ cái in hoa: $\\text{H}, \\text{A}, \\text{O}, \\text{M}, \\text{Z}, '
                 '\\text{E}$, có bao nhiêu chữ cái có tâm đối xứng?',
            'answer': ['3'],
            'unit': None,
            'solution': 'Các chữ cái có tâm đối xứng là $\\text{H}, \\text{O}, \\text{Z}$ nên có $3$ chữ '
                        'cái.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch06-phan-so',
  'context_title': 'Chương VI: Phân số',
  'context': 'Chương VI · SGK Toán 6: Phân số với tử và mẫu nguyên, bốn phép tính và hai bài toán về phân '
             'số.',
  'title': 'Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau',
  'icon': '🍰',
  'description': 'Phân số với tử và mẫu là số nguyên, quy tắc hai phân số bằng nhau và hai tính chất cơ bản '
                 'của phân số.',
  'requirements': ['Nhận biết được phân số $\\dfrac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\ne 0$ và quy tắc '
                   'bằng nhau $a \\cdot d = b \\cdot c$.',
                   'Vận dụng tính chất cơ bản của phân số để rút gọn phân số và đổi phân số có mẫu âm thành '
                   'mẫu dương.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Quy tắc bằng nhau** ($\\dfrac{a}{b} = '
                   '\\dfrac{c}{d} \\Leftrightarrow a \\cdot d = b \\cdot c$ ($b, d \\ne 0$)) vào giải bài '
                   'tập.'],
  'definition': '- Với $a, b \\in \\mathbb{Z}, b \\ne 0$, ta gọi $\\dfrac{a}{b}$ là một **phân số**, trong '
                'đó $a$ là tử số (tử), $b$ là mẫu số (mẫu).\n'
                '- **Hai phân số bằng nhau**: $\\dfrac{a}{b} = \\dfrac{c}{d}$ nếu $a \\cdot d = b \\cdot '
                'c$.\n'
                '- **Tính chất cơ bản**: $\\dfrac{a}{b} = \\dfrac{a \\cdot m}{b \\cdot m}$ ($m \\in '
                '\\mathbb{Z}, m \\ne 0$) và $\\dfrac{a}{b} = \\dfrac{a : n}{b : n}$ ($n \\in \\text{ƯC}(a, '
                'b)$).',
  'theory': '### 1. Đưa phân số về mẫu dương\n'
            '- Nhân cả tử và mẫu của phân số có mẫu âm với $-1$: $\\dfrac{a}{-b} = \\dfrac{-a}{b}$ (ví dụ '
            '$\\dfrac{3}{-5} = \\dfrac{-3}{5}$ và $\\dfrac{-4}{-7} = \\dfrac{4}{7}$).\n'
            '### 2. Rút gọn về phân số tối giản\n'
            '- Chia cả tử và mẫu cho $\\text{ƯCLN}$ của $|a|$ và $|b|$.',
  'formulas': [{'category': 'I. Phân số bằng nhau và Tính chất cơ bản',
                'items': [{'name': 'Quy tắc bằng nhau',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{c}{d} \\Leftrightarrow a \\cdot d = b \\cdot '
                                      'c$ ($b, d \\ne 0$)'},
                          {'name': 'Quy tắc đổi dấu mẫu',
                           'formula': '$\\dfrac{a}{-b} = \\dfrac{-a}{b}$; $\\dfrac{-a}{-b} = '
                                      '\\dfrac{a}{b}$'}]}],
  'example': 'Tìm số nguyên $x$ biết $\\dfrac{x}{12} = \\dfrac{-3}{4}$.',
  'example_answer': 'Theo quy tắc bằng nhau của hai phân số: $x \\cdot 4 = 12 \\cdot (-3) = -36 \\Rightarrow '
                    'x = (-36) : 4 = -9$.',
  'real_life': 'Biểu thị các phần đại lượng có hướng hoặc tỉ lệ thay đổi âm/dương trong khoa học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số nào dưới đây bằng phân số $\\dfrac{-2}{5}$?',
            'options': ['$\\dfrac{2}{5}$', '$\\dfrac{-5}{2}$', '$\\dfrac{2}{-5}$', '$\\dfrac{5}{-2}$'],
            'answer': 2,
            'solution': 'Nhân cả tử và mẫu của $\\dfrac{-2}{5}$ với $-1$ ta được $\\dfrac{2}{-5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Rút gọn phân số $\\dfrac{-15}{25}$ đến tối giản ta được:',
            'options': ['$\\dfrac{3}{5}$', '$\\dfrac{-5}{3}$', '$\\dfrac{5}{-3}$', '$\\dfrac{-3}{5}$'],
            'answer': 3,
            'solution': 'Chia cả tử và mẫu cho $5$ ta được $\\dfrac{-3}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Quy tắc bằng nhau**?',
            'options': ['$\\dfrac{a}{b} = \\dfrac{c}{d} \\Leftrightarrow a \\cdot d = b \\cdot c$ ($b, d '
                        '\\ne 0$)',
                        '$\\dfrac{a}{-b} = \\dfrac{-a}{b}$; $\\dfrac{-a}{-b} = \\dfrac{a}{b}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 23: Mở rộng khái niệm phân số. Phân số bằng '
                        'nhau, **Quy tắc bằng nhau** được xác định bởi: $\\dfrac{a}{b} = \\dfrac{c}{d} '
                        '\\Leftrightarrow a \\cdot d = b \\cdot c$ ($b, d \\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau**, nội dung/biểu thức '
                 '$\\dfrac{a}{-b} = \\dfrac{-a}{b}$; $\\dfrac{-a}{-b} = \\dfrac{a}{b}$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Quy tắc bằng nhau',
                        'Quy tắc đổi dấu mẫu',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau, biểu thức/quy tắc '
                        '$\\dfrac{a}{-b} = \\dfrac{-a}{b}$; $\\dfrac{-a}{-b} = \\dfrac{a}{b}$ chính là nội '
                        'dung của **Quy tắc đổi dấu mẫu**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số nguyên $x$ biết $\\dfrac{x}{15} = \\dfrac{-4}{5}$:',
            'options': ['$x = 12$', '$x = -20$', '$x = -12$', '$x = -3$'],
            'answer': 2,
            'solution': 'Ta có $x \\cdot 5 = 15 \\cdot (-4) = -60 \\Rightarrow x = -12$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau** (Chương VI: Phân số), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Nhận biết được phân số $\\dfrac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\ne 0$ và quy '
                        'tắc bằng nhau $a \\cdot d = b \\cdot c$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau: Nhận '
                        'biết được phân số $\\dfrac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\ne 0$ và quy tắc '
                        'bằng nhau $a \\cdot d = b \\cdot c$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các phân số với tử và mẫu nguyên. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$\\dfrac{-3}{4} = \\dfrac{6}{-8}$',
                           'Mọi số nguyên $n$ đều viết được dưới dạng phân số $\\dfrac{n}{1}$',
                           'Phân số $\\dfrac{5}{0}$ là một phân số hợp lệ',
                           '$\\dfrac{-12}{-18} = \\dfrac{2}{3}$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $(-3) \\cdot (-8) = 24 = 4 \\cdot 6$. b) Đúng. c) Sai vì mẫu số phải '
                        'khác $0$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 23: Mở rộng khái niệm '
                 'phân số. Phân số bằng nhau**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được phân số '
                           '$\\dfrac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\ne 0$ và quy tắc bằng nhau $a '
                           '\\cdot d = b \\cdot c$.',
                           'Quy tắc/công thức **Quy tắc bằng nhau** trong bài được xác định bởi: '
                           '$\\dfrac{a}{b} = \\dfrac{c}{d} \\Leftrightarrow a \\cdot d = b \\cdot c$ ($b, d '
                           '\\ne 0$).',
                           'Trong mọi trường hợp, **Quy tắc bằng nhau** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 23: Mở rộng khái niệm phân số. Phân '
                           'số bằng nhau.',
                           'Với bài toán minh họa: “Tìm số nguyên $x$ biết $\\dfrac{x}{12} = '
                           '\\dfrac{-3}{4}$.”, lời giải đúng là: Theo quy tắc bằng nhau của hai phân số: $x '
                           '\\cdot 4 = 12 \\cdot (-3) = -36 \\Rightarrow x = (-36) : 4 = -9$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 23: Mở rộng khái niệm phân số. Phân số '
                        'bằng nhau. b) **Đúng** theo công thức trọng tâm **Quy tắc bằng nhau** '
                        '($\\dfrac{a}{b} = \\dfrac{c}{d} \\Leftrightarrow a \\cdot d = b \\cdot c$ ($b, d '
                        '\\ne 0$)). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc '
                        '$A$) là công thức của nội dung khác, không phải quy tắc chung của **Quy tắc bằng '
                        'nhau**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau** để giải quyết '
                 'tình huống sau: Tìm số nguyên $x$ biết $\\dfrac{x}{12} = \\dfrac{-3}{4}$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Theo quy tắc bằng nhau của hai phân số: $x \\cdot 4 = 12 \\cdot (-3) = -36 '
                        '\\Rightarrow x = (-36) : 4 = -9$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Mở rộng khái niệm phân số. Phân số bằng nhau: Theo '
                        'quy tắc bằng nhau của hai phân số: $x \\cdot 4 = 12 \\cdot (-3) = -36 \\Rightarrow '
                        'x = (-36) : 4 = -9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số nguyên $x$ biết $\\dfrac{x - 2}{6} = \\dfrac{-5}{3}$.',
            'answer': ['-8', '−8'],
            'unit': None,
            'solution': 'Ta có $(x - 2) \\cdot 3 = 6 \\cdot (-5) = -30 \\Rightarrow x - 2 = -10 \\Rightarrow '
                        'x = -8$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch06-phan-so',
  'context_title': 'Chương VI: Phân số',
  'context': 'Chương VI · SGK Toán 6: Phân số với tử và mẫu nguyên, bốn phép tính và hai bài toán về phân '
             'số.',
  'title': 'Bài 24: So sánh phân số. Hỗn số dương',
  'icon': '🍰',
  'description': 'Quy tắc so sánh hai phân số (cùng mẫu dương hoặc khác mẫu) và cách đổi giữa hỗn số dương '
                 'với phân số.',
  'requirements': ['So sánh được hai phân số bất kì bằng cách viết chúng dưới dạng hai phân số có cùng một '
                   'mẫu dương.',
                   'Viết được phân số dương lớn hơn $1$ thành hỗn số dương và ngược lại.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Cùng mẫu dương m > 0** (Nếu $a < b$ thì '
                   '$\\dfrac{a}{m} < \\dfrac{b}{m}$) vào giải bài tập.'],
  'definition': '- Trong hai phân số có **cùng một mẫu dương**, phân số nào có tử lớn hơn thì phân số đó lớn '
                'hơn.\n'
                '- Muốn so sánh hai phân số không cùng mẫu, ta **viết chúng dưới dạng hai phân số có cùng '
                'một mẫu dương** rồi so sánh các tử với nhau.\n'
                '- **Hỗn số dương** $a\\dfrac{b}{c}$ ($a, b, c \\in \\mathbb{N}^*, b < c$) có giá trị bằng '
                '$a + \\dfrac{b}{c} = \\dfrac{a \\cdot c + b}{c}$.',
  'theory': '### 1. So sánh phân số âm và dương\n'
            '- Phân số âm $< 0 <$ Phân số dương.\n'
            '- Ví dụ: so sánh $\\dfrac{-2}{3}$ và $\\dfrac{-3}{4}$: quy đồng mẫu dương $12$ được '
            '$\\dfrac{-8}{12}$ và $\\dfrac{-9}{12}$. Vì $-8 > -9$ nên $\\dfrac{-2}{3} > \\dfrac{-3}{4}$.\n'
            '### 2. Hỗn số dương\n'
            '- Ví dụ: $\\dfrac{23}{5} = 4\\dfrac{3}{5}$ và $3\\dfrac{1}{4} = \\dfrac{3 \\cdot 4 + 1}{4} = '
            '\\dfrac{13}{4}$.',
  'formulas': [{'category': 'I. So sánh phân số và Hỗn số dương',
                'items': [{'name': 'Cùng mẫu dương m > 0',
                           'formula': 'Nếu $a < b$ thì $\\dfrac{a}{m} < \\dfrac{b}{m}$'},
                          {'name': 'Đổi hỗn số dương',
                           'formula': '$a\\dfrac{b}{c} = \\dfrac{a \\cdot c + b}{c}$ ($a, b, c \\in '
                                      '\\mathbb{N}^*, b < c$)'}]}],
  'example': 'So sánh hai phân số $\\dfrac{-5}{6}$ và $\\dfrac{7}{-8}$.',
  'example_answer': 'Đưa về mẫu dương $24$: $\\dfrac{-5}{6} = \\dfrac{-20}{24}$ và $\\dfrac{7}{-8} = '
                    '\\dfrac{-7}{8} = \\dfrac{-21}{24}$. Vì $-20 > -21$ nên $\\dfrac{-5}{6} > '
                    '\\dfrac{7}{-8}$.',
  'real_life': 'So sánh các phần thời gian hoàn thành công việc hoặc định lượng nguyên liệu bằng hỗn số.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hỗn số $3\\dfrac{1}{4}$ viết dưới dạng phân số là:',
            'options': ['$\\dfrac{7}{4}$', '$\\dfrac{4}{13}$', '$\\dfrac{31}{4}$', '$\\dfrac{13}{4}$'],
            'answer': 3,
            'solution': 'Ta có $3\\dfrac{1}{4} = \\dfrac{3 \\cdot 4 + 1}{4} = \\dfrac{13}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các phân số $\\dfrac{-5}{7}; \\dfrac{-2}{7}; \\dfrac{1}{7}; \\dfrac{-6}{7}$, phân số '
                 'nhỏ nhất là:',
            'options': ['$\\dfrac{-6}{7}$', '$\\dfrac{-5}{7}$', '$\\dfrac{-2}{7}$', '$\\dfrac{1}{7}$'],
            'answer': 0,
            'solution': 'Cùng mẫu dương $7$, vì $-6 < -5 < -2 < 1$ nên $\\dfrac{-6}{7}$ nhỏ nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 24: So sánh phân số. Hỗn số dương**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Cùng mẫu dương m > 0**?',
            'options': ['$a\\dfrac{b}{c} = \\dfrac{a \\cdot c + b}{c}$ ($a, b, c \\in \\mathbb{N}^*, b < c$)',
                        'Nếu $a < b$ thì $\\dfrac{a}{m} < \\dfrac{b}{m}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 24: So sánh phân số. Hỗn số dương, **Cùng mẫu '
                        'dương m > 0** được xác định bởi: Nếu $a < b$ thì $\\dfrac{a}{m} < \\dfrac{b}{m}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: So sánh phân số. Hỗn số dương**, nội dung/biểu thức $a\\dfrac{b}{c} = '
                 '\\dfrac{a \\cdot c + b}{c}$ ($a, b, c \\in \\mathbb{N}^*, b < c$) là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Cùng mẫu dương m > 0',
                        'Quan hệ phần tử – tập hợp',
                        'Đổi hỗn số dương',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 24: So sánh phân số. Hỗn số dương, biểu thức/quy tắc $a\\dfrac{b}{c} = '
                        '\\dfrac{a \\cdot c + b}{c}$ ($a, b, c \\in \\mathbb{N}^*, b < c$) chính là nội dung '
                        'của **Đổi hỗn số dương**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khẳng định nào sau đây là đúng?',
            'options': ['$\\dfrac{-2}{3} < \\dfrac{-3}{4}$',
                        '$\\dfrac{-2}{3} = \\dfrac{-3}{4}$',
                        '$\\dfrac{-2}{3} > 0$',
                        '$\\dfrac{-2}{3} > \\dfrac{-3}{4}$'],
            'answer': 3,
            'solution': 'Ta có $\\dfrac{-2}{3} = \\dfrac{-8}{12} > \\dfrac{-9}{12} = \\dfrac{-3}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: So sánh phân số. Hỗn số dương** (Chương VI: Phân số), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['So sánh được hai phân số bất kì bằng cách viết chúng dưới dạng hai phân số có cùng '
                        'một mẫu dương.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 24: So sánh phân số. Hỗn số dương: So sánh được hai '
                        'phân số bất kì bằng cách viết chúng dưới dạng hai phân số có cùng một mẫu dương.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Mỗi khẳng định sau về so sánh phân số và hỗn số đúng hay sai?',
            'statements': ['$\\dfrac{-3}{5} < 0 < \\dfrac{1}{4}$',
                           '$\\dfrac{-2}{3} < \\dfrac{-3}{4}$',
                           '$\\dfrac{19}{4} = 4\\dfrac{3}{4}$',
                           '$2\\dfrac{3}{5} = \\dfrac{6}{5}$'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng. b) Sai vì $\\dfrac{-8}{12} > \\dfrac{-9}{12}$. c) Đúng ($19 : 4 = 4$ dư '
                        '$3$). d) Sai vì $2\\dfrac{3}{5} = \\dfrac{13}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 24: So sánh phân số. '
                 'Hỗn số dương**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: So sánh được hai phân số bất kì '
                           'bằng cách viết chúng dưới dạng hai phân số có cùng một mẫu dương.',
                           'Quy tắc/công thức **Cùng mẫu dương m > 0** trong bài được xác định bởi: Nếu $a < '
                           'b$ thì $\\dfrac{a}{m} < \\dfrac{b}{m}$.',
                           'Trong mọi trường hợp, **Cùng mẫu dương m > 0** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 24: So sánh phân số. Hỗn số dương.',
                           'Với bài toán minh họa: “So sánh hai phân số $\\dfrac{-5}{6}$ và '
                           '$\\dfrac{7}{-8}$.”, lời giải đúng là: Đưa về mẫu dương $24$: $\\dfrac{-5}{6} = '
                           '\\dfrac{-20}{24}$ và $\\dfrac{7}{-8} = \\dfrac{-7}{8} = \\dfrac{-21}{24}$. Vì '
                           '$-20 > -21$ nên $\\dfrac{-5}{6} > \\dfrac{7}{-8}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 24: So sánh phân số. Hỗn số dương. b) '
                        '**Đúng** theo công thức trọng tâm **Cùng mẫu dương m > 0** (Nếu $a < b$ thì '
                        '$\\dfrac{a}{m} < \\dfrac{b}{m}$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y '
                        '\\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc '
                        'chung của **Cùng mẫu dương m > 0**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 24: So sánh phân số. Hỗn số dương** để giải quyết tình huống sau: '
                 'So sánh hai phân số $\\dfrac{-5}{6}$ và $\\dfrac{7}{-8}$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Đưa về mẫu dương $24$: $\\dfrac{-5}{6} = \\dfrac{-20}{24}$ và $\\dfrac{7}{-8} = '
                        '\\dfrac{-7}{8} = \\dfrac{-21}{24}$. Vì $-20 > -21$ nên $\\dfrac{-5}{6} > '
                        '\\dfrac{7}{-8}$...',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: So sánh phân số. Hỗn số dương: Đưa về mẫu dương '
                        '$24$: $\\dfrac{-5}{6} = \\dfrac{-20}{24}$ và $\\dfrac{7}{-8} = \\dfrac{-7}{8} = '
                        '\\dfrac{-21}{24}$. Vì $-20 > -21$ nên $\\dfrac{-5}{6} > \\dfrac{7}{-8}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu số nguyên $x$ thỏa mãn $\\dfrac{-7}{3} < x < \\dfrac{5}{2}$?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $-2\\dfrac{1}{3} < x < 2\\dfrac{1}{2}$ nên $x \\in \\{-2; -1; 0; 1; 2\\}$, có '
                        'tất cả $5$ số nguyên.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch06-phan-so',
  'context_title': 'Chương VI: Phân số',
  'context': 'Chương VI · SGK Toán 6: Phân số với tử và mẫu nguyên, bốn phép tính và hai bài toán về phân '
             'số.',
  'title': 'Bài 25: Phép cộng và phép trừ phân số',
  'icon': '🍰',
  'description': 'Quy tắc cộng, trừ hai phân số, số đối của một phân số và các tính chất của phép cộng phân '
                 'số.',
  'requirements': ['Thực hiện được phép cộng và phép trừ các phân số (có tử, mẫu là số nguyên).',
                   'Tìm được số đối của một phân số và vận dụng tính chất giao hoán, kết hợp, quy tắc dấu '
                   'ngoặc để tính hợp lí.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Cộng hai phân số cùng mẫu** ($\\dfrac{a}{m} '
                   '+ \\dfrac{b}{m} = \\dfrac{a + b}{m}$) vào giải bài tập.'],
  'definition': '- **Cộng hai phân số cùng mẫu**: $\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$. Nếu '
                'không cùng mẫu, ta quy đồng về cùng một mẫu dương rồi cộng.\n'
                '- **Số đối** của phân số $\\dfrac{a}{b}$ là $-\\dfrac{a}{b} = \\dfrac{-a}{b} = '
                '\\dfrac{a}{-b}$ (tổng hai phân số đối nhau bằng $0$).\n'
                '- **Phép trừ phân số**: $\\dfrac{a}{b} - \\dfrac{c}{d} = \\dfrac{a}{b} + '
                '\\left(-\\dfrac{c}{d}\\right)$.',
  'theory': '### 1. Ví dụ cộng, trừ phân số\n'
            '- $\\dfrac{-1}{2} + \\dfrac{2}{3} = \\dfrac{-3}{6} + \\dfrac{4}{6} = \\dfrac{1}{6}$; '
            '$\\dfrac{1}{4} - \\dfrac{5}{6} = \\dfrac{3}{12} - \\dfrac{10}{12} = \\dfrac{-7}{12}$.\n'
            '### 2. Tính chất của phép cộng phân số\n'
            '- Giao hoán, kết hợp, cộng với số $0$, cộng với số đối và quy tắc dấu ngoặc hoàn toàn tương tự '
            'như đối với số nguyên.',
  'formulas': [{'category': 'I. Cộng, trừ và Số đối của phân số',
                'items': [{'name': 'Cộng hai phân số cùng mẫu',
                           'formula': '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$'},
                          {'name': 'Số đối',
                           'formula': '$\\dfrac{a}{b} + \\left(-\\dfrac{a}{b}\\right) = 0$; $-\\dfrac{a}{b} '
                                      '= \\dfrac{-a}{b} = \\dfrac{a}{-b}$'},
                          {'name': 'Phép trừ',
                           'formula': '$\\dfrac{a}{b} - \\dfrac{c}{d} = \\dfrac{a}{b} + '
                                      '\\left(-\\dfrac{c}{d}\\right)$'}]}],
  'example': 'Tính hợp lí: $\\dfrac{-3}{7} + \\dfrac{5}{13} + \\dfrac{-4}{7} + \\dfrac{8}{13}$.',
  'example_answer': 'Nhóm các phân số cùng mẫu: $\\left(\\dfrac{-3}{7} + \\dfrac{-4}{7}\\right) + '
                    '\\left(\\dfrac{5}{13} + \\dfrac{8}{13}\\right) = -1 + 1 = 0$.',
  'real_life': 'Tính tổng hoặc phần còn lại của công việc khi nhiều người cùng làm chung một công việc.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số đối của phân số $\\dfrac{-4}{9}$ là:',
            'options': ['$\\dfrac{4}{9}$', '$\\dfrac{-4}{9}$', '$\\dfrac{9}{4}$', '$\\dfrac{-9}{4}$'],
            'answer': 0,
            'solution': 'Số đối của $\\dfrac{-4}{9}$ là $-\\left(\\dfrac{-4}{9}\\right) = \\dfrac{4}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $\\dfrac{-1}{2} + \\dfrac{2}{3}$ là:',
            'options': ['$\\dfrac{1}{5}$', '$\\dfrac{1}{6}$', '$\\dfrac{-1}{6}$', '$\\dfrac{3}{5}$'],
            'answer': 1,
            'solution': 'Quy đồng mẫu $6$: $\\dfrac{-3}{6} + \\dfrac{4}{6} = \\dfrac{1}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 25: Phép cộng và phép trừ phân số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Cộng hai phân số cùng mẫu**?',
            'options': ['$\\dfrac{a}{b} + \\left(-\\dfrac{a}{b}\\right) = 0$; $-\\dfrac{a}{b} = '
                        '\\dfrac{-a}{b} = \\dfrac{a}{-b}$',
                        '$\\dfrac{a}{b} - \\dfrac{c}{d} = \\dfrac{a}{b} + \\left(-\\dfrac{c}{d}\\right)$',
                        '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 25: Phép cộng và phép trừ phân số, **Cộng hai '
                        'phân số cùng mẫu** được xác định bởi: $\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + '
                        'b}{m}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Phép cộng và phép trừ phân số**, nội dung/biểu thức $\\dfrac{a}{b} + '
                 '\\left(-\\dfrac{a}{b}\\right) = 0$; $-\\dfrac{a}{b} = \\dfrac{-a}{b} = \\dfrac{a}{-b}$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cộng hai phân số cùng mẫu', 'Phép trừ', 'Quan hệ phần tử – tập hợp', 'Số đối'],
            'answer': 3,
            'solution': 'Trong Bài 25: Phép cộng và phép trừ phân số, biểu thức/quy tắc $\\dfrac{a}{b} + '
                        '\\left(-\\dfrac{a}{b}\\right) = 0$; $-\\dfrac{a}{b} = \\dfrac{-a}{b} = '
                        '\\dfrac{a}{-b}$ chính là nội dung của **Số đối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $\\dfrac{1}{4} - \\dfrac{5}{6}$ là:',
            'options': ['$\\dfrac{-7}{12}$', '$\\dfrac{7}{12}$', '$\\dfrac{-4}{-2}$', '$\\dfrac{-1}{3}$'],
            'answer': 0,
            'solution': 'Quy đồng mẫu $12$: $\\dfrac{3}{12} - \\dfrac{10}{12} = \\dfrac{-7}{12}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Phép cộng và phép trừ phân số** (Chương VI: Phân số), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Thực hiện được phép cộng và phép trừ các phân số (có tử, mẫu là số nguyên).',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 25: Phép cộng và phép trừ phân số: Thực hiện được phép '
                        'cộng và phép trừ các phân số (có tử, mẫu là số nguyên).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các phép tính cộng và trừ phân số. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$\\dfrac{-2}{9} + \\dfrac{5}{9} = \\dfrac{1}{3}$',
                           'Số đối của $\\dfrac{3}{-7}$ là $\\dfrac{-3}{7}$',
                           '$\\dfrac{1}{4} - \\dfrac{5}{6} = \\dfrac{-7}{12}$',
                           '$\\dfrac{-5}{11} + \\dfrac{3}{8} + \\dfrac{-6}{11} = \\dfrac{-5}{8}$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng ($\\dfrac{3}{9} = \\dfrac{1}{3}$). b) Sai vì $\\dfrac{3}{-7} = '
                        '\\dfrac{-3}{7}$ có số đối là $\\dfrac{3}{7}$. c) Đúng. d) Đúng ($-1 + \\dfrac{3}{8} '
                        '= \\dfrac{-5}{8}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 25: Phép cộng và phép '
                 'trừ phân số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được phép cộng và phép '
                           'trừ các phân số (có tử, mẫu là số nguyên).',
                           'Quy tắc/công thức **Cộng hai phân số cùng mẫu** trong bài được xác định bởi: '
                           '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$.',
                           'Trong mọi trường hợp, **Cộng hai phân số cùng mẫu** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 25: Phép cộng và phép trừ '
                           'phân số.',
                           'Với bài toán minh họa: “Tính hợp lí: $\\dfrac{-3}{7} + \\dfrac{5}{13} + '
                           '\\dfrac{-4}{7} + \\dfrac{8}{13}$.”, lời giải đúng là: Nhóm các phân số cùng mẫu: '
                           '$\\left(\\dfrac{-3}{7} + \\dfrac{-4}{7}\\right) + \\left(\\dfrac{5}{13} + '
                           '\\dfrac{8}{13}\\right) = -1 + 1 = 0$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 25: Phép cộng và phép trừ phân số. b) '
                        '**Đúng** theo công thức trọng tâm **Cộng hai phân số cùng mẫu** ($\\dfrac{a}{m} + '
                        '\\dfrac{b}{m} = \\dfrac{a + b}{m}$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y '
                        '\\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc '
                        'chung của **Cộng hai phân số cùng mẫu**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 25: Phép cộng và phép trừ phân số** để giải quyết tình huống sau: '
                 'Tính hợp lí: $\\dfrac{-3}{7} + \\dfrac{5}{13} + \\dfrac{-4}{7} + \\dfrac{8}{13}$. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Nhóm các phân số cùng mẫu: $\\left(\\dfrac{-3}{7} + \\dfrac{-4}{7}\\right) + '
                        '\\left(\\dfrac{5}{13} + \\dfrac{8}{13}\\right) = -1 + 1 = 0$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25: Phép cộng và phép trừ phân số: Nhóm các phân số cùng '
                        'mẫu: $\\left(\\dfrac{-3}{7} + \\dfrac{-4}{7}\\right) + \\left(\\dfrac{5}{13} + '
                        '\\dfrac{8}{13}\\right) = -1 + 1 = 0$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số nguyên $x$ biết $\\dfrac{x}{12} = \\dfrac{3}{4} - \\dfrac{1}{6}$.',
            'answer': ['7'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{3}{4} - \\dfrac{1}{6} = \\dfrac{9}{12} - \\dfrac{2}{12} = '
                        '\\dfrac{7}{12}$, suy ra $x = 7$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch06-phan-so',
  'context_title': 'Chương VI: Phân số',
  'context': 'Chương VI · SGK Toán 6: Phân số với tử và mẫu nguyên, bốn phép tính và hai bài toán về phân '
             'số.',
  'title': 'Bài 26: Phép nhân và phép chia phân số',
  'icon': '🍰',
  'description': 'Quy tắc nhân hai phân số, phân số nghịch đảo, phép chia phân số và các tính chất của phép '
                 'nhân phân số.',
  'requirements': ['Thực hiện được phép nhân và phép chia phân số; tìm được số nghịch đảo của một phân số '
                   'khác $0$.',
                   'Vận dụng tính chất giao hoán, kết hợp, phân phối của phép nhân phân số để tính hợp lí.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Phép nhân phân số** ($\\dfrac{a}{b} \\cdot '
                   '\\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d}$) vào giải bài tập.'],
  'definition': '- **Phép nhân hai phân số**: $\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b '
                '\\cdot d}$.\n'
                '- Hai số gọi là **nghịch đảo của nhau** nếu tích của chúng bằng $1$. Phân số nghịch đảo của '
                '$\\dfrac{a}{b}$ ($a, b \\ne 0$) là $\\dfrac{b}{a}$.\n'
                '- **Phép chia phân số**: $\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\cdot '
                '\\dfrac{d}{c}$ (với $c \\ne 0$).',
  'theory': '### 1. Rút gọn trước khi nhân\n'
            '- Ví dụ: $\\dfrac{-2}{5} \\cdot \\dfrac{15}{4} = \\dfrac{(-2) \\cdot 15}{5 \\cdot 4} = '
            '\\dfrac{-3}{2}$; $\\dfrac{3}{4} : \\left(\\dfrac{-9}{8}\\right) = \\dfrac{3}{4} \\cdot '
            '\\dfrac{-8}{9} = \\dfrac{-2}{3}$.\n'
            '### 2. Tính chất của phép nhân phân số\n'
            '- Giao hoán: $A \\cdot B = B \\cdot A$; Kết hợp: $(A \\cdot B) \\cdot C = A \\cdot (B \\cdot '
            'C)$; Phân phối: $A \\cdot (B + C) = A \\cdot B + A \\cdot C$.',
  'formulas': [{'category': 'I. Nhân, chia và Số nghịch đảo',
                'items': [{'name': 'Phép nhân phân số',
                           'formula': '$\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot '
                                      'd}$'},
                          {'name': 'Số nghịch đảo',
                           'formula': 'Nghịch đảo của $\\dfrac{a}{b}$ ($a \\ne 0$) là $\\dfrac{b}{a}$ vì '
                                      '$\\dfrac{a}{b} \\cdot \\dfrac{b}{a} = 1$'},
                          {'name': 'Phép chia phân số',
                           'formula': '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\cdot \\dfrac{d}{c}$ '
                                      '($c \\ne 0$)'}]}],
  'example': 'Tính hợp lí: $\\dfrac{-5}{9} \\cdot \\dfrac{4}{11} + \\dfrac{-5}{9} \\cdot \\dfrac{7}{11}$.',
  'example_answer': 'Đặt $\\dfrac{-5}{9}$ làm thừa số chung: $\\dfrac{-5}{9} \\cdot \\left(\\dfrac{4}{11} + '
                    '\\dfrac{7}{11}\\right) = \\dfrac{-5}{9} \\cdot 1 = \\dfrac{-5}{9}$.',
  'real_life': 'Tính vận tốc, quãng đường, diện tích khi các số đo cho dưới dạng phân số.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số nghịch đảo của phân số $\\dfrac{-3}{7}$ là:',
            'options': ['$\\dfrac{3}{7}$', '$\\dfrac{-7}{3}$', '$\\dfrac{7}{3}$', '$\\dfrac{-3}{7}$'],
            'answer': 1,
            'solution': 'Đổi chỗ tử và mẫu, giữ nguyên dấu âm: số nghịch đảo của $\\dfrac{-3}{7}$ là '
                        '$\\dfrac{-7}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $\\dfrac{3}{4} : \\left(\\dfrac{-9}{8}\\right)$ là:',
            'options': ['$\\dfrac{-27}{32}$', '$\\dfrac{2}{3}$', '$\\dfrac{-2}{3}$', '$\\dfrac{-3}{2}$'],
            'answer': 2,
            'solution': 'Ta có $\\dfrac{3}{4} \\cdot \\left(\\dfrac{-8}{9}\\right) = \\dfrac{-24}{36} = '
                        '\\dfrac{-2}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 26: Phép nhân và phép chia phân số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Phép nhân phân số**?',
            'options': ['Nghịch đảo của $\\dfrac{a}{b}$ ($a \\ne 0$) là $\\dfrac{b}{a}$ vì $\\dfrac{a}{b} '
                        '\\cdot \\dfrac{b}{a} = 1$',
                        '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\cdot \\dfrac{d}{c}$ ($c \\ne 0$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 26: Phép nhân và phép chia phân số, **Phép '
                        'nhân phân số** được xác định bởi: $\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a '
                        '\\cdot c}{b \\cdot d}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Phép nhân và phép chia phân số**, nội dung/biểu thức Nghịch đảo của '
                 '$\\dfrac{a}{b}$ ($a \\ne 0$) là $\\dfrac{b}{a}$ vì $\\dfrac{a}{b} \\cdot \\dfrac{b}{a} = '
                 '1$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số nghịch đảo',
                        'Phép nhân phân số',
                        'Phép chia phân số',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 0,
            'solution': 'Trong Bài 26: Phép nhân và phép chia phân số, biểu thức/quy tắc Nghịch đảo của '
                        '$\\dfrac{a}{b}$ ($a \\ne 0$) là $\\dfrac{b}{a}$ vì $\\dfrac{a}{b} \\cdot '
                        '\\dfrac{b}{a} = 1$ chính là nội dung của **Số nghịch đảo**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\dfrac{7}{13} \\cdot \\dfrac{5}{12} + \\dfrac{7}{13} \\cdot '
                 '\\dfrac{7}{12} - \\dfrac{7}{13}$ bằng:',
            'options': ['$\\dfrac{7}{13}$', '$0$', '$1$', '$\\dfrac{-7}{13}$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{7}{13} \\cdot \\left(\\dfrac{5}{12} + \\dfrac{7}{12} - 1\\right) = '
                        '\\dfrac{7}{13} \\cdot 0 = 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Phép nhân và phép chia phân số** (Chương VI: Phân số), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Thực hiện được phép nhân và phép chia phân số; tìm được số nghịch đảo của một phân '
                        'số khác $0$.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 26: Phép nhân và phép chia phân số: Thực hiện được '
                        'phép nhân và phép chia phân số; tìm được số nghịch đảo của một phân số khác $0$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét phép nhân và phép chia phân số. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$\\left(\\dfrac{-2}{5}\\right) \\cdot \\dfrac{15}{4} = \\dfrac{-3}{2}$',
                           'Số $0$ có số nghịch đảo là $0$',
                           'Số nghịch đảo của $-5$ là $\\dfrac{-1}{5}$',
                           '$\\left(\\dfrac{-3}{4}\\right)^2 = \\dfrac{9}{16}$'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì số $0$ không có số nghịch đảo. c) Đúng vì $(-5) \\cdot '
                        '\\dfrac{-1}{5} = 1$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 26: Phép nhân và phép '
                 'chia phân số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được phép nhân và phép '
                           'chia phân số; tìm được số nghịch đảo của một phân số khác $0$.',
                           'Quy tắc/công thức **Phép nhân phân số** trong bài được xác định bởi: '
                           '$\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d}$.',
                           'Trong mọi trường hợp, **Phép nhân phân số** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 26: Phép nhân và phép chia phân số.',
                           'Với bài toán minh họa: “Tính hợp lí: $\\dfrac{-5}{9} \\cdot \\dfrac{4}{11} + '
                           '\\dfrac{-5}{9} \\cdot \\dfrac{7}{11}$.”, lời giải đúng là: Đặt $\\dfrac{-5}{9}$ '
                           'làm thừa số chung: $\\dfrac{-5}{9} \\cdot \\left(\\dfrac{4}{11} + '
                           '\\dfrac{7}{11}\\right) = \\dfrac{-5}{9} \\cdot 1 = \\dfrac{-5}{9}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 26: Phép nhân và phép chia phân số. b) '
                        '**Đúng** theo công thức trọng tâm **Phép nhân phân số** ($\\dfrac{a}{b} \\cdot '
                        '\\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d}$). c) **Sai** vì $x \\in A$ ($x$ '
                        'thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Phép nhân phân số**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 26: Phép nhân và phép chia phân số** để giải quyết tình huống '
                 'sau: Tính hợp lí: $\\dfrac{-5}{9} \\cdot \\dfrac{4}{11} + \\dfrac{-5}{9} \\cdot '
                 '\\dfrac{7}{11}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Đặt $\\dfrac{-5}{9}$ làm thừa số chung: $\\dfrac{-5}{9} \\cdot '
                        '\\left(\\dfrac{4}{11} + \\dfrac{7}{11}\\right) = \\dfrac{-5}{9} \\cdot 1 = '
                        '\\dfrac{-5}{9}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 26: Phép nhân và phép chia phân số: Đặt $\\dfrac{-5}{9}$ '
                        'làm thừa số chung: $\\dfrac{-5}{9} \\cdot \\left(\\dfrac{4}{11} + '
                        '\\dfrac{7}{11}\\right) = \\dfrac{-5}{9} \\cdot 1 = \\dfrac{-5}{9}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chữ nhật có diện tích $\\dfrac{15}{8}\\text{ m}^2$ và chiều rộng '
                 '$\\dfrac{3}{4}\\text{ m}$. Tính chu vi của hình chữ nhật đó dưới dạng phân số tối giản '
                 '(viết dạng a/b).',
            'answer': ['13/2', '6,5', '6.5'],
            'unit': None,
            'solution': 'Chiều dài là $\\dfrac{15}{8} : \\dfrac{3}{4} = \\dfrac{5}{2}\\text{ m}$. Chu vi là '
                        '$2 \\cdot \\left(\\dfrac{5}{2} + \\dfrac{3}{4}\\right) = \\dfrac{13}{2}\\text{ m}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch06-phan-so',
  'context_title': 'Chương VI: Phân số',
  'context': 'Chương VI · SGK Toán 6: Phân số với tử và mẫu nguyên, bốn phép tính và hai bài toán về phân '
             'số.',
  'title': 'Bài 27: Hai bài toán về phân số',
  'icon': '🍰',
  'description': 'Quy tắc tìm giá trị phân số của một số cho trước và tìm một số biết giá trị phân số của số '
                 'đó.',
  'requirements': ['Tính được giá trị phân số $\\dfrac{m}{n}$ của một số $a$ cho trước bằng phép nhân $a '
                   '\\cdot \\dfrac{m}{n}$.',
                   'Tìm được một số khi biết $\\dfrac{m}{n}$ của số đó bằng $b$ bằng phép chia $b : '
                   '\\dfrac{m}{n}$.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Bài toán 1 (Tìm giá trị phân số của a)** '
                   '($b = a \\cdot \\dfrac{m}{n}$) vào giải bài tập.'],
  'definition': '- **Bài toán 1**: Muốn tìm $\\dfrac{m}{n}$ của một số $a$ cho trước, ta tính $a \\cdot '
                '\\dfrac{m}{n}$ ($m \\in \\mathbb{N}, n \\in \\mathbb{N}^*$).\n'
                '- **Bài toán 2**: Muốn tìm một số biết $\\dfrac{m}{n}$ của số đó bằng $b$, ta tính $b : '
                '\\dfrac{m}{n}$ ($m, n \\in \\mathbb{N}^*$).',
  'theory': '### 1. Phân biệt hai bài toán\n'
            '- Khi **đã biết số tổng thể $a$**, cần tìm một phần $\\dfrac{m}{n}$ của nó $\\rightarrow$ dùng '
            '**phép nhân** ($a \\cdot \\dfrac{m}{n}$).\n'
            '- Khi **chưa biết số tổng thể**, chỉ biết một phần $\\dfrac{m}{n}$ của nó ứng với giá trị $b$ '
            '$\\rightarrow$ dùng **phép chia** ($b : \\dfrac{m}{n}$).',
  'formulas': [{'category': 'I. Hai bài toán cơ bản về phân số',
                'items': [{'name': 'Bài toán 1 (Tìm giá trị phân số của a)',
                           'formula': '$b = a \\cdot \\dfrac{m}{n}$'},
                          {'name': 'Bài toán 2 (Tìm số a biết m/n của a bằng b)',
                           'formula': '$a = b : \\dfrac{m}{n} = b \\cdot \\dfrac{n}{m}$'}]}],
  'example': 'Lớp 6A có $40$ học sinh, trong đó $\\dfrac{3}{8}$ số học sinh đạt loại giỏi. Tính số học sinh '
             'giỏi. Nếu lớp 6B có $12$ học sinh giỏi chiếm $\\dfrac{2}{5}$ cả lớp thì lớp 6B có bao nhiêu '
             'học sinh?',
  'example_answer': 'Số học sinh giỏi lớp 6A là $40 \\cdot \\dfrac{3}{8} = 15$ (em). Số học sinh lớp 6B là '
                    '$12 : \\dfrac{2}{5} = 12 \\cdot \\dfrac{5}{2} = 30$ (em).',
  'real_life': 'Tính khối lượng nguyên liệu, quãng đường đã đi hoặc tổng số trang sách khi biết số trang đã '
               'đọc.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị $\\dfrac{3}{5}$ của $45$ bằng:',
            'options': ['$75$', '$15$', '$27$', '$9$'],
            'answer': 2,
            'solution': 'Áp dụng Bài toán 1: $45 \\cdot \\dfrac{3}{5} = 27$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm một số biết $\\dfrac{3}{5}$ của số đó bằng $24$:',
            'options': ['$14{,}4$', '$72$', '$15$', '$40$'],
            'answer': 3,
            'solution': 'Áp dụng Bài toán 2: $24 : \\dfrac{3}{5} = 24 \\cdot \\dfrac{5}{3} = 40$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 27: Hai bài toán về phân số**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Bài toán 1 (Tìm giá trị phân số của a)**?',
            'options': ['$b = a \\cdot \\dfrac{m}{n}$',
                        '$a = b : \\dfrac{m}{n} = b \\cdot \\dfrac{n}{m}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 27: Hai bài toán về phân số, **Bài toán 1 '
                        '(Tìm giá trị phân số của a)** được xác định bởi: $b = a \\cdot \\dfrac{m}{n}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Hai bài toán về phân số**, nội dung/biểu thức $a = b : \\dfrac{m}{n} = b '
                 '\\cdot \\dfrac{n}{m}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Bài toán 1 (Tìm giá trị phân số của a)',
                        'Bài toán 2 (Tìm số a biết m/n của a bằng b)',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 27: Hai bài toán về phân số, biểu thức/quy tắc $a = b : \\dfrac{m}{n} = b '
                        '\\cdot \\dfrac{n}{m}$ chính là nội dung của **Bài toán 2 (Tìm số a biết m/n của a '
                        'bằng b)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một người đi hết quãng đường trong $3$ ngày: ngày đầu đi $\\dfrac{1}{3}$ quãng đường, ngày '
                 'thứ hai đi $\\dfrac{2}{5}$ quãng đường, ngày thứ ba đi nốt $12\\text{ km}$. Quãng đường đó '
                 'dài:',
            'options': ['$36\\text{ km}$', '$60\\text{ km}$', '$45\\text{ km}$', '$30\\text{ km}$'],
            'answer': 2,
            'solution': 'Phân số chỉ $12\\text{ km}$ là $1 - \\dfrac{1}{3} - \\dfrac{2}{5} = '
                        '\\dfrac{4}{15}$. Quãng đường dài $12 : \\dfrac{4}{15} = 45\\text{ km}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Hai bài toán về phân số** (Chương VI: Phân số), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Tính được giá trị phân số $\\dfrac{m}{n}$ của một số $a$ cho trước bằng phép nhân '
                        '$a \\cdot \\dfrac{m}{n}$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 27: Hai bài toán về phân số: Tính được giá trị phân số '
                        '$\\dfrac{m}{n}$ của một số $a$ cho trước bằng phép nhân $a \\cdot \\dfrac{m}{n}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Lớp 6A có $40$ học sinh, trong đó $\\dfrac{3}{8}$ số học sinh xếp loại giỏi, '
                 '$\\dfrac{1}{2}$ số học sinh xếp loại khá, còn lại là đạt. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Lớp 6A có $15$ học sinh giỏi',
                           'Lớp 6A có $20$ học sinh khá',
                           'Lớp 6A có $4$ học sinh xếp loại đạt',
                           'Số học sinh xếp loại đạt chiếm $\\dfrac{1}{8}$ số học sinh cả lớp'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng ($40 \\cdot \\dfrac{3}{8} = 15$). b) Đúng ($40 \\cdot \\dfrac{1}{2} = 20$). '
                        'c) Sai vì $40 - 15 - 20 = 5$ em. d) Đúng ($\\dfrac{5}{40} = \\dfrac{1}{8}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 27: Hai bài toán về '
                 'phân số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được giá trị phân số '
                           '$\\dfrac{m}{n}$ của một số $a$ cho trước bằng phép nhân $a \\cdot '
                           '\\dfrac{m}{n}$.',
                           'Quy tắc/công thức **Bài toán 1 (Tìm giá trị phân số của a)** trong bài được xác '
                           'định bởi: $b = a \\cdot \\dfrac{m}{n}$.',
                           'Trong mọi trường hợp, **Bài toán 1 (Tìm giá trị phân số của a)** luôn được tính '
                           'bằng công thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) '
                           '(thuộc Quan hệ phần tử – tập hợp) mà không cần điều kiện của Bài 27: Hai bài '
                           'toán về phân số.',
                           'Với bài toán minh họa: “Lớp 6A có $40$ học sinh, trong đó $\\dfrac{3}{8}$ số học '
                           'sinh đạt loại giỏi. Tính số học sinh giỏi. Nếu lớp 6B có $12$ học sinh giỏi '
                           'chiếm $\\dfrac{2}{5}$...”, lời giải đúng là: Số học sinh giỏi lớp 6A là $40 '
                           '\\cdot \\dfrac{3}{8} = 15$ (em). Số học sinh lớp 6B là $12 : \\dfrac{2}{5} = 12 '
                           '\\cdot \\dfrac{5}{2} = 30$ (em).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 27: Hai bài toán về phân số. b) **Đúng** '
                        'theo công thức trọng tâm **Bài toán 1 (Tìm giá trị phân số của a)** ($b = a \\cdot '
                        '\\dfrac{m}{n}$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không '
                        'thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của **Bài toán '
                        '1 (Tìm giá trị phân số của a)**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 27: Hai bài toán về phân số** để giải quyết tình huống sau: Lớp '
                 '6A có $40$ học sinh, trong đó $\\dfrac{3}{8}$ số học sinh đạt loại giỏi. Tính số học sinh '
                 'giỏi. Nếu lớp 6B có $12$ học sinh giỏi chiếm $\\dfrac{2}{5}$ cả lớp thì lớp 6B có bao '
                 'nhiêu học sinh? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Số học sinh giỏi lớp 6A là $40 \\cdot \\dfrac{3}{8} = 15$ (em). Số học sinh lớp 6B '
                        'là $12 : \\dfrac{2}{5} = 12 \\cdot \\dfrac{5}{2} = 30$ (em).',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 27: Hai bài toán về phân số: Số học sinh giỏi lớp 6A là '
                        '$40 \\cdot \\dfrac{3}{8} = 15$ (em). Số học sinh lớp 6B là $12 : \\dfrac{2}{5} = 12 '
                        '\\cdot \\dfrac{5}{2} = 30$ (em).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'An đọc một cuốn sách trong hai ngày. Ngày đầu An đọc được $\\dfrac{2}{5}$ số trang sách, '
                 'ngày thứ hai đọc nốt $90$ trang còn lại. Hỏi cuốn sách đó có bao nhiêu trang?',
            'answer': ['150'],
            'unit': None,
            'solution': 'Phân số chỉ $90$ trang là $1 - \\dfrac{2}{5} = \\dfrac{3}{5}$. Tổng số trang sách '
                        'là $90 : \\dfrac{3}{5} = 150$ (trang).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch07-so-thap-phan',
  'context_title': 'Chương VII: Số thập phân',
  'context': 'Chương VII · SGK Toán 6: Số thập phân âm và dương, tính toán, làm tròn và tỉ số phần trăm.',
  'title': 'Bài 28: Số thập phân',
  'icon': '🔟',
  'description': 'Phân số thập phân, số thập phân âm, số đối của số thập phân và quy tắc so sánh hai số thập '
                 'phân.',
  'requirements': ['Nhận biết được số thập phân âm, tìm được số đối của một số thập phân và chuyển đổi giữa '
                   'số thập phân với phân số thập phân.',
                   'So sánh được hai số thập phân bất kì (bao gồm cả số thập phân âm).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Số đối của số thập phân** (Số đối của $a$ '
                   'là $-a$; $a + (-a) = 0$) vào giải bài tập.'],
  'definition': '- Phân số thập phân là phân số mà mẫu là luỹ thừa của $10$ (có tử là số nguyên): '
                '$\\dfrac{-3}{10} = -0{,}3$; $\\dfrac{-125}{100} = -1{,}25$.\n'
                '- Các số thập phân lớn hơn $0$ gọi là **số thập phân dương**; nhỏ hơn $0$ gọi là **số thập '
                'phân âm**.\n'
                '- Hai số thập phân $a$ và $-a$ là **hai số đối nhau**.',
  'theory': '### 1. So sánh hai số thập phân\n'
            '- Số thập phân âm $< 0 <$ Số thập phân dương.\n'
            '- Nếu $a, b$ là hai số thập phân dương và $a > b$ thì $-a < -b$. Ví dụ: vì $1{,}3 > 1{,}25$ nên '
            '$-1{,}3 < -1{,}25$.',
  'formulas': [{'category': 'I. Số thập phân và So sánh',
                'items': [{'name': 'Số đối của số thập phân',
                           'formula': 'Số đối của $a$ là $-a$; $a + (-a) = 0$'},
                          {'name': 'So sánh hai số thập phân âm',
                           'formula': 'Với $a, b > 0$: $a > b \\Leftrightarrow -a < -b$'}]}],
  'example': 'Sắp xếp các số sau theo thứ tự tăng dần: $0{,}5; -1{,}25; -1{,}3; 0; 1{,}05$.',
  'example_answer': 'Vì $1{,}3 > 1{,}25$ nên $-1{,}3 < -1{,}25$. Thứ tự tăng dần là: $-1{,}3; -1{,}25; 0; '
                    '0{,}5; 1{,}05$.',
  'real_life': 'Đọc chỉ số nhiệt độ âm có phần thập phân (như $-2{,}5^\\circ\\text{C}$) hoặc chỉ số độ cận '
               'thị của mắt kính ($-1{,}75$ đi-ốp).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số $\\dfrac{-3}{4}$ viết dưới dạng số thập phân là:',
            'options': ['$-0{,}34$', '$-7{,}5$', '$0{,}75$', '$-0{,}75$'],
            'answer': 3,
            'solution': 'Ta có $\\dfrac{-3}{4} = \\dfrac{-75}{100} = -0{,}75$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số đối của số thập phân $-2{,}7$ là:',
            'options': ['$2{,}7$', '$-2{,}7$', '$0{,}27$', '$-7{,}2$'],
            'answer': 0,
            'solution': 'Số đối của $-2{,}7$ là $2{,}7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 28: Số thập phân**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Số đối của số thập phân**?',
            'options': ['Với $a, b > 0$: $a > b \\Leftrightarrow -a < -b$',
                        'Số đối của $a$ là $-a$; $a + (-a) = 0$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 28: Số thập phân, **Số đối của số thập phân** '
                        'được xác định bởi: Số đối của $a$ là $-a$; $a + (-a) = 0$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 28: Số thập phân**, nội dung/biểu thức Với $a, b > 0$: $a > b \\Leftrightarrow '
                 '-a < -b$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số đối của số thập phân',
                        'Quan hệ phần tử – tập hợp',
                        'So sánh hai số thập phân âm',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 28: Số thập phân, biểu thức/quy tắc Với $a, b > 0$: $a > b '
                        '\\Leftrightarrow -a < -b$ chính là nội dung của **So sánh hai số thập phân âm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Dãy số nào dưới đây được sắp xếp theo thứ tự tăng dần?',
            'options': ['$-1{,}25; -1{,}3; 0{,}5; 1{,}05$',
                        '$-1{,}3; -1{,}25; 1{,}05; 0{,}5$',
                        '$0{,}5; 1{,}05; -1{,}25; -1{,}3$',
                        '$-1{,}3; -1{,}25; 0{,}5; 1{,}05$'],
            'answer': 3,
            'solution': 'Vì $1{,}3 > 1{,}25$ nên $-1{,}3 < -1{,}25 < 0{,}5 < 1{,}05$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 28: Số thập phân** (Chương VII: Số thập phân), khẳng định nào sau đây phản '
                 'ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số thập phân âm, tìm được số đối của một số thập phân và chuyển đổi '
                        'giữa số thập phân với phân số thập phân.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 28: Số thập phân: Nhận biết được số thập phân âm, tìm '
                        'được số đối của một số thập phân và chuyển đổi giữa số thập phân với phân số thập '
                        'phân.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các số thập phân âm và dương. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$-1{,}25 > -1{,}3$',
                           'Số đối của $0{,}45$ là $-0{,}45$',
                           '$\\dfrac{-7}{100} = -0{,}7$',
                           'Mọi số thập phân âm đều nhỏ hơn $0$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng (vì $1{,}25 < 1{,}3$). b) Đúng. c) Sai vì $\\dfrac{-7}{100} = -0{,}07$. d) '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 28: Số thập phân**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được số thập phân âm, '
                           'tìm được số đối của một số thập phân và chuyển đổi giữa số thập phân với phân số '
                           'thập phân.',
                           'Quy tắc/công thức **Số đối của số thập phân** trong bài được xác định bởi: Số '
                           'đối của $a$ là $-a$; $a + (-a) = 0$.',
                           'Trong mọi trường hợp, **Số đối của số thập phân** luôn được tính bằng công thức '
                           '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ '
                           'phần tử – tập hợp) mà không cần điều kiện của Bài 28: Số thập phân.',
                           'Với bài toán minh họa: “Sắp xếp các số sau theo thứ tự tăng dần: $0{,}5; '
                           '-1{,}25; -1{,}3; 0; 1{,}05$.”, lời giải đúng là: Vì $1{,}3 > 1{,}25$ nên $-1{,}3 '
                           '< -1{,}25$. Thứ tự tăng dần là: $-1{,}3; -1{,}25; 0; 0{,}5; 1{,}05$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 28: Số thập phân. b) **Đúng** theo công '
                        'thức trọng tâm **Số đối của số thập phân** (Số đối của $a$ là $-a$; $a + (-a) = '
                        '0$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) '
                        'là công thức của nội dung khác, không phải quy tắc chung của **Số đối của số thập '
                        'phân**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 28: Số thập phân** để giải quyết tình huống sau: Sắp xếp các số '
                 'sau theo thứ tự tăng dần: $0{,}5; -1{,}25; -1{,}3; 0; 1{,}05$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Vì $1{,}3 > 1{,}25$ nên $-1{,}3 < -1{,}25$. Thứ tự tăng dần là: $-1{,}3; -1{,}25; '
                        '0; 0{,}5; 1{,}05$.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 28: Số thập phân: Vì $1{,}3 > 1{,}25$ nên $-1{,}3 < '
                        '-1{,}25$. Thứ tự tăng dần là: $-1{,}3; -1{,}25; 0; 0{,}5; 1{,}05$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu số nguyên $x$ thỏa mãn $-3{,}4 < x < 2{,}1$?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Các số nguyên $x$ thỏa mãn là $-3; -2; -1; 0; 1; 2$, có tất cả $6$ số nguyên.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch07-so-thap-phan',
  'context_title': 'Chương VII: Số thập phân',
  'context': 'Chương VII · SGK Toán 6: Số thập phân âm và dương, tính toán, làm tròn và tỉ số phần trăm.',
  'title': 'Bài 29: Tính toán với số thập phân',
  'icon': '🔟',
  'description': 'Quy tắc cộng, trừ, nhân, chia các số thập phân dương và âm cùng các tính chất của phép '
                 'tính.',
  'requirements': ['Thực hiện thành thạo bốn phép tính cộng, trừ, nhân, chia với số thập phân (cả âm và '
                   'dương).',
                   'Vận dụng tính chất giao hoán, kết hợp, phân phối và quy tắc dấu ngoặc để tính hợp lí.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Cộng và Trừ** ($(-a) + (-b) = -(a + b)$; $x '
                   '- y = x + (-y)$) vào giải bài tập.'],
  'definition': '- Quy tắc dấu khi cộng, trừ, nhân, chia các **số thập phân âm và dương** hoàn toàn giống '
                'quy tắc dấu đối với **số nguyên**.\n'
                '- Cụ thể: nhân hoặc chia hai số thập phân cùng dấu được kết quả dương; khác dấu được kết '
                'quả âm.',
  'theory': '### 1. Ví dụ các phép tính với số thập phân âm\n'
            '- Cộng, trừ: $(-3{,}5) + (-1{,}2) = -4{,}7$; $(-3{,}5) + 1{,}2 = -(3{,}5 - 1{,}2) = -2{,}3$; '
            '$2{,}4 - 5{,}9 = 2{,}4 + (-5{,}9) = -3{,}5$.\n'
            '- Nhân, chia: $(-1{,}5) \\cdot (-0{,}4) = 0{,}6$; $4{,}8 : (-1{,}2) = -(4{,}8 : 1{,}2) = -4$.',
  'formulas': [{'category': 'I. Quy tắc dấu với số thập phân (a, b > 0)',
                'items': [{'name': 'Cộng và Trừ', 'formula': '$(-a) + (-b) = -(a + b)$; $x - y = x + (-y)$'},
                          {'name': 'Nhân và Chia',
                           'formula': '$(-a) \\cdot (-b) = a \\cdot b$; $(-a) \\cdot b = -(a \\cdot b)$; '
                                      '$(-a) : b = -(a : b)$'}]}],
  'example': 'Tính giá trị biểu thức: $(-2{,}5) \\cdot 4 + 1{,}5$ và $4{,}8 : (-1{,}2)$.',
  'example_answer': 'Ta có $(-2{,}5) \\cdot 4 + 1{,}5 = -10 + 1{,}5 = -8{,}5$ và $4{,}8 : (-1{,}2) = -4$.',
  'real_life': 'Tính trung bình nhiệt độ mùa đông tại các vùng ôn đới và tính toán biến động tài khoản.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $(-2{,}5) \\cdot 4 + 1{,}5$ là:',
            'options': ['$-8{,}5$', '$-11{,}5$', '$8{,}5$', '$-4$'],
            'answer': 0,
            'solution': 'Ta có $(-2{,}5) \\cdot 4 = -10$; sau đó $-10 + 1{,}5 = -8{,}5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $4{,}8 : (-1{,}2)$ là:',
            'options': ['$4$', '$-4$', '$-0{,}4$', '$0{,}4$'],
            'answer': 1,
            'solution': 'Chia hai số khác dấu được kết quả âm: $-(4{,}8 : 1{,}2) = -4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 29: Tính toán với số thập phân**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Cộng và Trừ**?',
            'options': ['$(-a) \\cdot (-b) = a \\cdot b$; $(-a) \\cdot b = -(a \\cdot b)$; $(-a) : b = -(a : '
                        'b)$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$(-a) + (-b) = -(a + b)$; $x - y = x + (-y)$',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 29: Tính toán với số thập phân, **Cộng và '
                        'Trừ** được xác định bởi: $(-a) + (-b) = -(a + b)$; $x - y = x + (-y)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Tính toán với số thập phân**, nội dung/biểu thức $(-a) \\cdot (-b) = a '
                 '\\cdot b$; $(-a) \\cdot b = -(a \\cdot b)$; $(-a) : b = -(a : b)$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Cộng và Trừ', 'Quan hệ phần tử – tập hợp', 'Hai cách mô tả', 'Nhân và Chia'],
            'answer': 3,
            'solution': 'Trong Bài 29: Tính toán với số thập phân, biểu thức/quy tắc $(-a) \\cdot (-b) = a '
                        '\\cdot b$; $(-a) \\cdot b = -(a \\cdot b)$; $(-a) : b = -(a : b)$ chính là nội dung '
                        'của **Nhân và Chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tính hợp lí biểu thức $(-3{,}7) \\cdot 6{,}4 + (-3{,}7) \\cdot 3{,}6$ ta được:',
            'options': ['$-37$', '$37$', '$-3{,}7$', '$0$'],
            'answer': 0,
            'solution': 'Đặt $-3{,}7$ làm thừa số chung: $(-3{,}7) \\cdot (6{,}4 + 3{,}6) = (-3{,}7) \\cdot '
                        '10 = -37$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Tính toán với số thập phân** (Chương VII: Số thập phân), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Thực hiện thành thạo bốn phép tính cộng, trừ, nhân, chia với số thập phân (cả âm và '
                        'dương).',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 29: Tính toán với số thập phân: Thực hiện thành thạo '
                        'bốn phép tính cộng, trừ, nhân, chia với số thập phân (cả âm và dương).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các phép tính với số thập phân. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['$(-1{,}5) \\cdot (-0{,}4) = -0{,}6$',
                           '$(-3{,}2) + (-1{,}8) = -5$',
                           '$2{,}5 - (-1{,}5) = 4$',
                           '$(-0{,}5)^2 = 0{,}25$'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì nhân hai số âm phải ra số dương $0{,}6$. b) Đúng. c) Đúng ($2{,}5 + 1{,}5 '
                        '= 4$). d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 29: Tính toán với số '
                 'thập phân**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện thành thạo bốn phép tính '
                           'cộng, trừ, nhân, chia với số thập phân (cả âm và dương).',
                           'Quy tắc/công thức **Cộng và Trừ** trong bài được xác định bởi: $(-a) + (-b) = '
                           '-(a + b)$; $x - y = x + (-y)$.',
                           'Trong mọi trường hợp, **Cộng và Trừ** luôn được tính bằng công thức $x \\in A$ '
                           '($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 29: Tính toán với số thập phân.',
                           'Với bài toán minh họa: “Tính giá trị biểu thức: $(-2{,}5) \\cdot 4 + 1{,}5$ và '
                           '$4{,}8 : (-1{,}2)$.”, lời giải đúng là: Ta có $(-2{,}5) \\cdot 4 + 1{,}5 = -10 + '
                           '1{,}5 = -8{,}5$ và $4{,}8 : (-1{,}2) = -4$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 29: Tính toán với số thập phân. b) '
                        '**Đúng** theo công thức trọng tâm **Cộng và Trừ** ($(-a) + (-b) = -(a + b)$; $x - y '
                        '= x + (-y)$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không '
                        'thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của **Cộng và '
                        'Trừ**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 29: Tính toán với số thập phân** để giải quyết tình huống sau: '
                 'Tính giá trị biểu thức: $(-2{,}5) \\cdot 4 + 1{,}5$ và $4{,}8 : (-1{,}2)$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Ta có $(-2{,}5) \\cdot 4 + 1{,}5 = -10 + 1{,}5 = -8{,}5$ và $4{,}8 : (-1{,}2) = '
                        '-4$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 29: Tính toán với số thập phân: Ta có $(-2{,}5) \\cdot 4 '
                        '+ 1{,}5 = -10 + 1{,}5 = -8{,}5$ và $4{,}8 : (-1{,}2) = -4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số thập phân $x$ biết $2{,}5 \\cdot x + 7{,}5 = -5$.',
            'answer': ['-5', '−5'],
            'unit': None,
            'solution': 'Ta có $2{,}5 \\cdot x = -5 - 7{,}5 = -12{,}5 \\Rightarrow x = (-12{,}5) : 2{,}5 = '
                        '-5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch07-so-thap-phan',
  'context_title': 'Chương VII: Số thập phân',
  'context': 'Chương VII · SGK Toán 6: Số thập phân âm và dương, tính toán, làm tròn và tỉ số phần trăm.',
  'title': 'Bài 30: Làm tròn và ước lượng',
  'icon': '🔟',
  'description': 'Quy tắc làm tròn số tự nhiên, số thập phân đến một hàng cho trước và cách ước lượng kết '
                 'quả phép tính.',
  'requirements': ['Làm tròn được số thập phân và số tự nhiên đến một hàng cho trước (hàng phần mười, phần '
                   'trăm, hàng chục, hàng trăm, ...).',
                   'Biết ước lượng nhanh kết quả các phép tính để phát hiện sai sót.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Chữ số bỏ đi đầu tiên < 5** (Giữ nguyên chữ '
                   'số hàng làm tròn) vào giải bài tập.'],
  'definition': '- Muốn **làm tròn một số** đến một hàng nào đó, ta nhìn vào **chữ số ngay bên phải** hàng '
                'làm tròn:\n'
                '- Nếu chữ số đó **nhỏ hơn $5$** thì giữ nguyên chữ số ở hàng làm tròn; nếu **lớn hơn hoặc '
                'bằng $5$** thì cộng thêm $1$ vào chữ số ở hàng làm tròn, rồi thay các chữ số bỏ đi bằng $0$ '
                '(bỏ hẳn nếu ở phần thập phân).',
  'theory': '### 1. Làm tròn số thập phân và số tự nhiên\n'
            '- Số thập phân: $3{,}14159$ làm tròn đến hàng phần trăm được $3{,}14$; $12{,}467$ làm tròn đến '
            'hàng phần mười được $12{,}5$.\n'
            '- Số tự nhiên: $28\\,472$ làm tròn đến hàng nghìn được $28\\,000$ (thay các chữ số phía sau '
            'bằng chữ số $0$).\n'
            '### 2. Ước lượng kết quả phép tính\n'
            '- Làm tròn các thừa số, số hạng đến chữ số hàng cao nhất rồi nhẩm: $19{,}8 \\cdot 5{,}1 '
            '\\approx 20 \\cdot 5 = 100$.',
  'formulas': [{'category': 'I. Quy tắc làm tròn và ước lượng',
                'items': [{'name': 'Chữ số bỏ đi đầu tiên < 5', 'formula': 'Giữ nguyên chữ số hàng làm tròn'},
                          {'name': 'Chữ số bỏ đi đầu tiên >= 5',
                           'formula': 'Cộng thêm $1$ vào chữ số hàng làm tròn'}]}],
  'example': 'Làm tròn số $7{,}449$ đến hàng phần mười và ước lượng tích $29{,}7 \\cdot 4{,}1$.',
  'example_answer': 'Ở số $7{,}449$, chữ số ngay sau hàng phần mười là $4 < 5$ nên làm tròn đến hàng phần '
                    'mười được $7{,}4$. Ước lượng: $29{,}7 \\cdot 4{,}1 \\approx 30 \\cdot 4 = 120$.',
  'real_life': 'Ước lượng nhanh tổng số tiền cần trả khi đi siêu thị để kiểm tra xem tiền mang theo có đủ '
               'không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $12{,}467$ đến hàng phần mười ta được:',
            'options': ['$12{,}4$', '$12{,}5$', '$12{,}47$', '$13$'],
            'answer': 1,
            'solution': 'Chữ số bỏ đi đầu tiên (hàng phần trăm) là $6 \\ge 5$ nên được $12{,}5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số tự nhiên $45\\,620$ đến hàng nghìn ta được:',
            'options': ['$45\\,000$', '$45\\,600$', '$46\\,000$', '$50\\,000$'],
            'answer': 2,
            'solution': 'Chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được $46\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 30: Làm tròn và ước lượng**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Chữ số bỏ đi đầu tiên < 5**?',
            'options': ['Cộng thêm $1$ vào chữ số hàng làm tròn',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        'Giữ nguyên chữ số hàng làm tròn'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 30: Làm tròn và ước lượng, **Chữ số bỏ đi đầu '
                        'tiên < 5** được xác định bởi: Giữ nguyên chữ số hàng làm tròn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Làm tròn và ước lượng**, nội dung/biểu thức Cộng thêm $1$ vào chữ số hàng '
                 'làm tròn là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Chữ số bỏ đi đầu tiên >= 5',
                        'Chữ số bỏ đi đầu tiên < 5',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 30: Làm tròn và ước lượng, biểu thức/quy tắc Cộng thêm $1$ vào chữ số '
                        'hàng làm tròn chính là nội dung của **Chữ số bỏ đi đầu tiên >= 5**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Ước lượng kết quả của phép nhân $39{,}8 \\cdot 5{,}04$ bằng cách làm tròn hai thừa số đến '
                 'hàng đơn vị ta được:',
            'options': ['$150$', '$200$', '$240$', '$195$'],
            'answer': 1,
            'solution': 'Làm tròn $39{,}8 \\approx 40$ và $5{,}04 \\approx 5$, tích ước lượng là $40 \\cdot '
                        '5 = 200$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Làm tròn và ước lượng** (Chương VII: Số thập phân), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Làm tròn được số thập phân và số tự nhiên đến một hàng cho trước (hàng phần mười, '
                        'phần trăm, hàng chục, hàng trăm, ...).',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 30: Làm tròn và ước lượng: Làm tròn được số thập phân '
                        'và số tự nhiên đến một hàng cho trước (hàng phần mười, phần trăm, hàng chục, hàng '
                        'trăm, ...).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét việc làm tròn các số. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Làm tròn $7{,}449$ đến hàng phần mười được $7{,}5$',
                           'Làm tròn $3{,}14159$ đến hàng phần trăm được $3{,}14$',
                           'Làm tròn $-8{,}62$ đến hàng đơn vị được $-9$',
                           'Làm tròn $1538$ đến hàng chục được $1540$'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì chữ số bỏ đi đầu tiên là $4 < 5$ nên kết quả là $7{,}4$ (không làm tròn '
                        'dây chuyền). b) Đúng. c) Đúng ($6 \\ge 5$). d) Đúng ($8 \\ge 5$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 30: Làm tròn và ước '
                 'lượng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Làm tròn được số thập phân và số '
                           'tự nhiên đến một hàng cho trước (hàng phần mười, phần trăm, hàng chục, hàng '
                           'trăm, ...).',
                           'Quy tắc/công thức **Chữ số bỏ đi đầu tiên < 5** trong bài được xác định bởi: Giữ '
                           'nguyên chữ số hàng làm tròn.',
                           'Trong mọi trường hợp, **Chữ số bỏ đi đầu tiên < 5** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 30: Làm tròn và ước lượng.',
                           'Với bài toán minh họa: “Làm tròn số $7{,}449$ đến hàng phần mười và ước lượng '
                           'tích $29{,}7 \\cdot 4{,}1$.”, lời giải đúng là: Ở số $7{,}449$, chữ số ngay sau '
                           'hàng phần mười là $4 < 5$ nên làm tròn đến hàng phần mười được $7{,}4$. Ước '
                           'lượng: $29{,}7 \\cdot 4{,}1 \\approx 30 \\cdot 4 = 120$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 30: Làm tròn và ước lượng. b) **Đúng** '
                        'theo công thức trọng tâm **Chữ số bỏ đi đầu tiên < 5** (Giữ nguyên chữ số hàng làm '
                        'tròn). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc '
                        '$A$) là công thức của nội dung khác, không phải quy tắc chung của **Chữ số bỏ đi '
                        'đầu tiên < 5**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 30: Làm tròn và ước lượng** để giải quyết tình huống sau: Làm '
                 'tròn số $7{,}449$ đến hàng phần mười và ước lượng tích $29{,}7 \\cdot 4{,}1$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Ở số $7{,}449$, chữ số ngay sau hàng phần mười là $4 < 5$ nên làm tròn đến hàng '
                        'phần mười được $7{,}4$. Ước lượng: $29{,}7 \\cdot 4{,}1 \\approx 30 \\cdot 4 = '
                        '120$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 30: Làm tròn và ước lượng: Ở số $7{,}449$, chữ số ngay '
                        'sau hàng phần mười là $4 < 5$ nên làm tròn đến hàng phần mười được $7{,}4$. Ước '
                        'lượng: $29{,}7 \\cdot 4{,}1 \\approx 30 \\cdot 4 = 120$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mảnh đất hình chữ nhật có chiều dài $15{,}2\\text{ m}$ và chiều rộng $8{,}5\\text{ '
                 'm}$. Tính diện tích mảnh đất rồi làm tròn kết quả đến hàng đơn vị.',
            'answer': ['129'],
            'unit': None,
            'solution': 'Diện tích mảnh đất là $15{,}2 \\cdot 8{,}5 = 129{,}2\\text{ m}^2$. Làm tròn đến '
                        'hàng đơn vị được $129$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch07-so-thap-phan',
  'context_title': 'Chương VII: Số thập phân',
  'context': 'Chương VII · SGK Toán 6: Số thập phân âm và dương, tính toán, làm tròn và tỉ số phần trăm.',
  'title': 'Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm',
  'icon': '🔟',
  'description': 'Tỉ số và tỉ số phần trăm của hai đại lượng, hai bài toán cơ bản về tỉ số phần trăm và ứng '
                 'dụng thực tiễn.',
  'requirements': ['Tính được tỉ số và tỉ số phần trăm của hai số hoặc hai đại lượng (cùng đơn vị đo).',
                   'Giải được hai bài toán cơ bản về tỉ số phần trăm cùng các bài toán lãi suất, giảm giá.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tỉ số phần trăm của a và b** '
                   '($\\dfrac{a}{b} \\cdot 100\\%$) vào giải bài tập.'],
  'definition': '- **Tỉ số** của hai số $a$ và $b$ ($b \\ne 0$) là thương $a : b$ hay $\\dfrac{a}{b}$.\n'
                '- **Tỉ số phần trăm** của hai số $a$ và $b$ là $\\dfrac{a}{b} \\cdot 100\\%$.\n'
                '- **Giá trị $m\\%$ của số $a$** là $a \\cdot \\dfrac{m}{100}$. **Tìm một số biết $m\\%$ của '
                'nó bằng $b$**: ta tính $b : \\dfrac{m}{100} = b \\cdot \\dfrac{100}{m}$.',
  'theory': '### 1. Bài toán giảm giá và tăng giá\n'
            '- Giảm giá $m\\%$: $\\text{Giá mới} = \\text{Giá cũ} \\cdot (100 - m)\\%$.\n'
            '### 2. Bài toán lãi suất ngân hàng\n'
            '- Gửi số tiền gốc $A$ với lãi suất $r\\%$/năm thì sau $1$ năm: $\\text{Tiền lãi} = A \\cdot '
            '\\dfrac{r}{100}$ và $\\text{Tổng gốc + lãi} = A + \\text{Tiền lãi}$.',
  'formulas': [{'category': 'I. Công thức tỉ số phần trăm',
                'items': [{'name': 'Tỉ số phần trăm của a và b', 'formula': '$\\dfrac{a}{b} \\cdot 100\\%$'},
                          {'name': 'Bài toán 1 (Tìm m% của a)', 'formula': '$a \\cdot \\dfrac{m}{100}$'},
                          {'name': 'Bài toán 2 (Biết m% của số đó bằng b)',
                           'formula': '$b : \\dfrac{m}{100} = b \\cdot \\dfrac{100}{m}$'}]}],
  'example': 'Một chiếc áo giá $400\\,000$ đồng được giảm giá $15\\%$. Tính số tiền được giảm và giá bán '
             'mới.',
  'example_answer': 'Số tiền được giảm là $400\\,000 \\cdot \\dfrac{15}{100} = 60\\,000$ (đồng). Giá bán mới '
                    'là $400\\,000 - 60\\,000 = 340\\,000$ (đồng).',
  'real_life': 'Tính tiền lãi gửi tiết kiệm ngân hàng, giá hàng khuyến mãi và phần trăm tăng trưởng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tỉ số phần trăm của $3$ và $4$ là:',
            'options': ['$34\\%$', '$133\\%$', '$75\\%$', '$0{,}75\\%$'],
            'answer': 2,
            'solution': 'Ta có $\\dfrac{3}{4} \\cdot 100\\% = 75\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bác An gửi tiết kiệm $50\\,000\\,000$ đồng với lãi suất $6\\%$/năm. Sau $1$ năm, bác An '
                 'nhận được cả gốc và lãi là:',
            'options': ['$56\\,000\\,000$ đồng',
                        '$3\\,000\\,000$ đồng',
                        '$50\\,300\\,000$ đồng',
                        '$53\\,000\\,000$ đồng'],
            'answer': 3,
            'solution': 'Tiền lãi là $50\\,000\\,000 \\cdot 6\\% = 3\\,000\\,000$ đồng. Tổng gốc và lãi là '
                        '$53\\,000\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Tỉ số phần trăm của a và b**?',
            'options': ['$\\dfrac{a}{b} \\cdot 100\\%$',
                        '$a \\cdot \\dfrac{m}{100}$',
                        '$b : \\dfrac{m}{100} = b \\cdot \\dfrac{100}{m}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 31: Một số bài toán về tỉ số và tỉ số phần '
                        'trăm, **Tỉ số phần trăm của a và b** được xác định bởi: $\\dfrac{a}{b} \\cdot '
                        '100\\%$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm**, nội dung/biểu thức $a '
                 '\\cdot \\dfrac{m}{100}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tỉ số phần trăm của a và b',
                        'Bài toán 1 (Tìm m% của a)',
                        'Bài toán 2 (Biết m% của số đó bằng b)',
                        'Quan hệ phần tử – tập hợp'],
            'answer': 1,
            'solution': 'Trong Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm, biểu thức/quy tắc $a '
                        '\\cdot \\dfrac{m}{100}$ chính là nội dung của **Bài toán 1 (Tìm m% của a)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một cửa hàng giảm giá $20\\%$ cho tất cả mặt hàng. Bạn Bình mua một đôi giày phải trả '
                 '$320\\,000$ đồng. Giá niêm yết ban đầu của đôi giày là:',
            'options': ['$384\\,000$ đồng', '$360\\,000$ đồng', '$400\\,000$ đồng', '$420\\,000$ đồng'],
            'answer': 2,
            'solution': 'Giá sau khi giảm bằng $80\\%$ giá ban đầu, vậy giá ban đầu là $320\\,000 : 80\\% = '
                        '400\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm** (Chương VII: Số thập '
                 'phân), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Tính được tỉ số và tỉ số phần trăm của hai số hoặc hai đại lượng (cùng đơn vị đo).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm: Tính '
                        'được tỉ số và tỉ số phần trăm của hai số hoặc hai đại lượng (cùng đơn vị đo).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một chiếc áo giá $400\\,000$ đồng được giảm giá $15\\%$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Số tiền được giảm là $60\\,000$ đồng',
                           'Giá sau khi giảm là $340\\,000$ đồng',
                           'Giá sau khi giảm bằng $85\\%$ giá ban đầu',
                           'Nếu giảm tiếp $10\\%$ trên giá mới thì tổng cộng đã giảm $25\\%$ giá ban đầu'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $85\\% \\cdot 90\\% = 76{,}5\\%$, tức là giảm '
                        '$23{,}5\\%$ so với giá ban đầu.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 31: Một số bài toán về '
                 'tỉ số và tỉ số phần trăm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được tỉ số và tỉ số phần trăm '
                           'của hai số hoặc hai đại lượng (cùng đơn vị đo).',
                           'Quy tắc/công thức **Tỉ số phần trăm của a và b** trong bài được xác định bởi: '
                           '$\\dfrac{a}{b} \\cdot 100\\%$.',
                           'Trong mọi trường hợp, **Tỉ số phần trăm của a và b** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 31: Một số bài toán về tỉ '
                           'số và tỉ số phần trăm.',
                           'Với bài toán minh họa: “Một chiếc áo giá $400\\,000$ đồng được giảm giá $15\\%$. '
                           'Tính số tiền được giảm và giá bán mới.”, lời giải đúng là: Số tiền được giảm là '
                           '$400\\,000 \\cdot \\dfrac{15}{100} = 60\\,000$ (đồng). Giá bán mới là $400\\,000 '
                           '- 60\\,000 = 340\\,000$ (đồng).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 31: Một số bài toán về tỉ số và tỉ số phần '
                        'trăm. b) **Đúng** theo công thức trọng tâm **Tỉ số phần trăm của a và b** '
                        '($\\dfrac{a}{b} \\cdot 100\\%$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y '
                        '\\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc '
                        'chung của **Tỉ số phần trăm của a và b**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm** để giải quyết '
                 'tình huống sau: Một chiếc áo giá $400\\,000$ đồng được giảm giá $15\\%$. Tính số tiền được '
                 'giảm và giá bán mới. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Số tiền được giảm là $400\\,000 \\cdot \\dfrac{15}{100} = 60\\,000$ (đồng). Giá bán '
                        'mới là $400\\,000 - 60\\,000 = 340\\,000$ (đồng).',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm: Số tiền '
                        'được giảm là $400\\,000 \\cdot \\dfrac{15}{100} = 60\\,000$ (đồng). Giá bán mới là '
                        '$400\\,000 - 60\\,000 = 340\\,000$ (đồng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lớp 6B có $45$ học sinh, trong đó $40\\%$ là học sinh nữ. Hỏi lớp 6B có bao nhiêu học sinh '
                 'nam?',
            'answer': ['27'],
            'unit': None,
            'solution': 'Số học sinh nữ là $45 \\cdot 40 : 100 = 18$ (em). Số học sinh nam là $45 - 18 = 27$ '
                        '(em).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch08-hinh-hoc-co-ban',
  'context_title': 'Chương VIII: Những hình hình học cơ bản',
  'context': 'Chương VIII · SGK Toán 6: Điểm, đường thẳng, tia, đoạn thẳng, trung điểm và góc.',
  'title': 'Bài 32: Điểm và đường thẳng',
  'icon': '📐',
  'description': 'Điểm thuộc hoặc không thuộc đường thẳng, đường thẳng đi qua hai điểm, ba điểm thẳng hàng '
                 'và hai đường thẳng cắt nhau, song song.',
  'requirements': ['Sử dụng đúng kí hiệu $A \\in d$, $B \\notin d$; nhận biết ba điểm thẳng hàng và tiên đề '
                   'đường thẳng đi qua hai điểm phân biệt.',
                   'Phân biệt được hai đường thẳng cắt nhau, hai đường thẳng song song và hai đường thẳng '
                   'trùng nhau.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tiên đề đường thẳng qua 2 điểm** (Qua $2$ '
                   'điểm phân biệt có duy nhất $1$ đường thẳng) vào giải bài tập.'],
  'definition': '- **Điểm** được kí hiệu bằng chữ cái in hoa ($A, B, C, \\dots$), **đường thẳng** kí hiệu '
                'bằng chữ cái thường ($a, b, d, \\dots$) hoặc hai chữ cái in hoa ($AB$).\n'
                '- Có **một và chỉ một** đường thẳng đi qua hai điểm phân biệt $A$ và $B$.\n'
                '- Ba điểm **thẳng hàng** là ba điểm cùng thuộc một đường thẳng.\n'
                '- Hai đường thẳng không có điểm chung nào gọi là **song song**; có đúng một điểm chung gọi '
                'là **cắt nhau** (điểm chung đó là **giao điểm**).',
  'theory': '### 1. Số đường thẳng đi qua các cặp điểm\n'
            '- Cho $n$ điểm phân biệt trong đó không có $3$ điểm nào thẳng hàng. Cứ qua $2$ điểm vẽ một '
            'đường thẳng thì số đường thẳng vẽ được là $\\dfrac{n(n - 1)}{2}$.',
  'formulas': [{'category': 'I. Quan hệ điểm – đường thẳng',
                'items': [{'name': 'Tiên đề đường thẳng qua 2 điểm',
                           'formula': 'Qua $2$ điểm phân biệt có duy nhất $1$ đường thẳng'},
                          {'name': 'Công thức đếm đường thẳng',
                           'formula': 'Qua $n$ điểm (không có $3$ điểm thẳng hàng) có $\\dfrac{n(n - 1)}{2}$ '
                                      'đường thẳng'}]}],
  'example': 'Cho $4$ điểm phân biệt $A, B, C, D$ trong đó không có ba điểm nào thẳng hàng. Vẽ các đường '
             'thẳng đi qua các cặp điểm. Hỏi vẽ được bao nhiêu đường thẳng?',
  'example_answer': 'Áp dụng công thức $\\dfrac{4 \\cdot (4 - 1)}{2} = 6$ đường thẳng (đó là $AB, AC, AD, '
                    'BC, BD, CD$).',
  'real_life': 'Ngắm trồng cây thẳng hàng, hai thanh đường ray tàu hỏa song song và ngã tư giao nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Qua hai điểm phân biệt $A$ và $B$, ta vẽ được bao nhiêu đường thẳng?',
            'options': ['$0$', '$2$', 'Vô số', '$1$'],
            'answer': 3,
            'solution': 'Có một và chỉ một đường thẳng đi qua hai điểm phân biệt $A$ và $B$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đường thẳng song song có bao nhiêu điểm chung?',
            'options': ['$0$ điểm chung', '$1$ điểm chung', '$2$ điểm chung', 'Vô số điểm chung'],
            'answer': 0,
            'solution': 'Hai đường thẳng song song không có điểm chung nào.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 32: Điểm và đường thẳng**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Tiên đề đường thẳng qua 2 điểm**?',
            'options': ['Qua $n$ điểm (không có $3$ điểm thẳng hàng) có $\\dfrac{n(n - 1)}{2}$ đường thẳng',
                        'Qua $2$ điểm phân biệt có duy nhất $1$ đường thẳng',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 32: Điểm và đường thẳng, **Tiên đề đường '
                        'thẳng qua 2 điểm** được xác định bởi: Qua $2$ điểm phân biệt có duy nhất $1$ đường '
                        'thẳng.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Điểm và đường thẳng**, nội dung/biểu thức Qua $n$ điểm (không có $3$ điểm '
                 'thẳng hàng) có $\\dfrac{n(n - 1)}{2}$ đường thẳng là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Tiên đề đường thẳng qua 2 điểm',
                        'Quan hệ phần tử – tập hợp',
                        'Công thức đếm đường thẳng',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 32: Điểm và đường thẳng, biểu thức/quy tắc Qua $n$ điểm (không có $3$ '
                        'điểm thẳng hàng) có $\\dfrac{n(n - 1)}{2}$ đường thẳng chính là nội dung của **Công '
                        'thức đếm đường thẳng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $4$ điểm phân biệt trong đó không có $3$ điểm nào thẳng hàng. Số đường thẳng đi qua '
                 'từng cặp điểm là:',
            'options': ['$4$', '$8$', '$12$', '$6$'],
            'answer': 3,
            'solution': 'Số đường thẳng là $\\dfrac{4 \\cdot 3}{2} = 6$ (đường thẳng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Điểm và đường thẳng** (Chương VIII: Những hình hình học cơ bản), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng đúng kí hiệu $A \\in d$, $B \\notin d$; nhận biết ba điểm thẳng hàng và '
                        'tiên đề đường thẳng đi qua hai điểm phân biệt.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 32: Điểm và đường thẳng: Sử dụng đúng kí hiệu $A \\in '
                        'd$, $B \\notin d$; nhận biết ba điểm thẳng hàng và tiên đề đường thẳng đi qua hai '
                        'điểm phân biệt.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét vị trí tương đối giữa điểm và đường thẳng. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Hai đường thẳng cắt nhau có đúng một điểm chung',
                           'Ba điểm cùng thuộc một đường thẳng gọi là ba điểm thẳng hàng',
                           'Qua một điểm chỉ vẽ được duy nhất một đường thẳng',
                           'Hai đường thẳng phân biệt hoặc cắt nhau hoặc song song'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì qua $1$ điểm vẽ được vô số đường thẳng. d) Đúng (trong '
                        'cùng một mặt phẳng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 32: Điểm và đường '
                 'thẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Sử dụng đúng kí hiệu $A \\in d$, '
                           '$B \\notin d$; nhận biết ba điểm thẳng hàng và tiên đề đường thẳng đi qua hai '
                           'điểm phân biệt.',
                           'Quy tắc/công thức **Tiên đề đường thẳng qua 2 điểm** trong bài được xác định '
                           'bởi: Qua $2$ điểm phân biệt có duy nhất $1$ đường thẳng.',
                           'Trong mọi trường hợp, **Tiên đề đường thẳng qua 2 điểm** luôn được tính bằng '
                           'công thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc '
                           'Quan hệ phần tử – tập hợp) mà không cần điều kiện của Bài 32: Điểm và đường '
                           'thẳng.',
                           'Với bài toán minh họa: “Cho $4$ điểm phân biệt $A, B, C, D$ trong đó không có ba '
                           'điểm nào thẳng hàng. Vẽ các đường thẳng đi qua các cặp điểm. Hỏi vẽ được bao '
                           'nhiêu...”, lời giải đúng là: Áp dụng công thức $\\dfrac{4 \\cdot (4 - 1)}{2} = '
                           '6$ đường thẳng (đó là $AB, AC, AD, BC, BD, CD$).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 32: Điểm và đường thẳng. b) **Đúng** theo '
                        'công thức trọng tâm **Tiên đề đường thẳng qua 2 điểm** (Qua $2$ điểm phân biệt có '
                        'duy nhất $1$ đường thẳng). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ '
                        '($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Tiên đề đường thẳng qua 2 điểm**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 32: Điểm và đường thẳng** để giải quyết tình huống sau: Cho $4$ '
                 'điểm phân biệt $A, B, C, D$ trong đó không có ba điểm nào thẳng hàng. Vẽ các đường thẳng '
                 'đi qua các cặp điểm. Hỏi vẽ được bao nhiêu đường thẳng? Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Áp dụng công thức $\\dfrac{4 \\cdot (4 - 1)}{2} = 6$ đường thẳng (đó là $AB, AC, '
                        'AD, BC, BD, CD$).',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 32: Điểm và đường thẳng: Áp dụng công thức $\\dfrac{4 '
                        '\\cdot (4 - 1)}{2} = 6$ đường thẳng (đó là $AB, AC, AD, BC, BD, CD$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $6$ điểm phân biệt trong đó không có $3$ điểm nào thẳng hàng. Kẻ các đường thẳng đi '
                 'qua các cặp điểm. Hỏi có tất cả bao nhiêu đường thẳng?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Số đường thẳng kẻ được là $\\dfrac{6 \\cdot (6 - 1)}{2} = 15$ (đường thẳng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch08-hinh-hoc-co-ban',
  'context_title': 'Chương VIII: Những hình hình học cơ bản',
  'context': 'Chương VIII · SGK Toán 6: Điểm, đường thẳng, tia, đoạn thẳng, trung điểm và góc.',
  'title': 'Bài 33: Điểm nằm giữa hai điểm. Tia',
  'icon': '📐',
  'description': 'Nhận biết quan hệ điểm nằm giữa hai điểm trong ba điểm thẳng hàng, khái niệm tia và hai '
                 'tia đối nhau.',
  'requirements': ['Nhận biết được trong ba điểm thẳng hàng có một và chỉ một điểm nằm giữa hai điểm còn '
                   'lại.',
                   'Nhận biết được tia gốc $O$, hai tia đối nhau và hai tia trùng nhau.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hai tia đối nhau** (Chung gốc $O$ và tạo '
                   'thành một đường thẳng) vào giải bài tập.'],
  'definition': '- Trong ba điểm thẳng hàng, có **một và chỉ một** điểm nằm giữa hai điểm còn lại.\n'
                '- Hình gồm điểm $O$ và một phần đường thẳng bị chia ra bởi điểm $O$ được gọi là một **tia** '
                'gốc $O$.\n'
                '- Hai tia chung gốc $Ox$ và $Oy$ tạo thành một đường thẳng $xy$ được gọi là **hai tia đối '
                'nhau**.',
  'theory': '### 1. Vị trí của ba điểm thẳng hàng\n'
            '- Nếu điểm $B$ nằm giữa hai điểm $A$ và $C$ thì: $A$ và $B$ nằm cùng phía đối với $C$; $B$ và '
            '$C$ nằm cùng phía đối với $A$; $A$ và $C$ nằm khác phía đối với $B$.\n'
            '### 2. Hai tia đối nhau và hai tia trùng nhau\n'
            '- Mỗi điểm trên đường thẳng là gốc chung của hai tia đối nhau.\n'
            '- Nếu điểm $A$ thuộc tia $Ox$ ($A \\ne O$) thì tia $OA$ và tia $Ox$ là **hai tia trùng nhau**.',
  'formulas': [{'category': 'I. Tia và điểm nằm giữa',
                'items': [{'name': 'Hai tia đối nhau',
                           'formula': 'Chung gốc $O$ và tạo thành một đường thẳng'},
                          {'name': 'Hai tia trùng nhau',
                           'formula': 'Nếu $A \\in Ox$ ($A \\ne O$) thì tia $OA$ trùng với tia $Ox$'}]}],
  'example': 'Trên đường thẳng $xy$ lấy điểm $O$. Điểm $A$ thuộc tia $Ox$, điểm $B$ thuộc tia $Oy$ ($A, B$ '
             'khác $O$). Trong ba điểm $A, O, B$ điểm nào nằm giữa hai điểm còn lại?',
  'example_answer': 'Vì $Ox$ và $Oy$ là hai tia đối nhau gốc $O$ nên điểm $O$ nằm giữa hai điểm $A$ và $B$.',
  'real_life': 'Hình ảnh tia nắng mặt trời hoặc tia sáng phát ra từ đèn pin.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai tia $Ox$ và $Oy$ chung gốc $O$ tạo thành đường thẳng $xy$ được gọi là:',
            'options': ['Hai tia đối nhau', 'Hai tia trùng nhau', 'Hai tia song song', 'Hai đoạn thẳng'],
            'answer': 0,
            'solution': 'Hai tia chung gốc tạo thành một đường thẳng là hai tia đối nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong ba điểm thẳng hàng, có bao nhiêu điểm nằm giữa hai điểm còn lại?',
            'options': ['$0$ điểm', '$1$ điểm', '$2$ điểm', '$3$ điểm'],
            'answer': 1,
            'solution': 'Trong ba điểm thẳng hàng có một và chỉ một điểm nằm giữa hai điểm còn lại.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 33: Điểm nằm giữa hai điểm. Tia**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Hai tia đối nhau**?',
            'options': ['Nếu $A \\in Ox$ ($A \\ne O$) thì tia $OA$ trùng với tia $Ox$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Chung gốc $O$ và tạo thành một đường thẳng',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 33: Điểm nằm giữa hai điểm. Tia, **Hai tia '
                        'đối nhau** được xác định bởi: Chung gốc $O$ và tạo thành một đường thẳng.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 33: Điểm nằm giữa hai điểm. Tia**, nội dung/biểu thức Nếu $A \\in Ox$ ($A \\ne '
                 'O$) thì tia $OA$ trùng với tia $Ox$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hai tia đối nhau',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả',
                        'Hai tia trùng nhau'],
            'answer': 3,
            'solution': 'Trong Bài 33: Điểm nằm giữa hai điểm. Tia, biểu thức/quy tắc Nếu $A \\in Ox$ ($A '
                        '\\ne O$) thì tia $OA$ trùng với tia $Ox$ chính là nội dung của **Hai tia trùng '
                        'nhau**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho điểm $M$ nằm giữa hai điểm $A$ và $B$. Hai tia nào sau đây là hai tia đối nhau?',
            'options': ['Tia $MA$ và tia $MB$',
                        'Tia $AM$ và tia $AB$',
                        'Tia $BA$ và tia $BM$',
                        'Tia $AB$ và tia $BA$'],
            'answer': 0,
            'solution': 'Vì $M$ nằm giữa $A$ và $B$ nên $MA$ và $MB$ chung gốc $M$ và tạo thành đường thẳng '
                        '$AB$, tức là hai tia đối nhau.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 33: Điểm nằm giữa hai điểm. Tia** (Chương VIII: Những hình hình học cơ bản), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Nhận biết được trong ba điểm thẳng hàng có một và chỉ một điểm nằm giữa hai điểm '
                        'còn lại.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 33: Điểm nằm giữa hai điểm. Tia: Nhận biết được trong '
                        'ba điểm thẳng hàng có một và chỉ một điểm nằm giữa hai điểm còn lại.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho ba điểm $A, B, C$ thẳng hàng theo thứ tự đó (điểm $B$ nằm giữa $A$ và $C$). Mỗi khẳng '
                 'định sau đúng hay sai?',
            'statements': ['Tia $BA$ và tia $BC$ là hai tia đối nhau',
                           'Tia $AB$ và tia $AC$ là hai tia trùng nhau',
                           'Tia $CA$ và tia $CB$ là hai tia đối nhau',
                           'Điểm $A$ và điểm $C$ nằm khác phía đối với điểm $B$'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng (chung gốc $B$ ngược hướng). b) Đúng (cùng gốc $A$ cùng hướng). c) Sai vì '
                        'tia $CA$ và $CB$ trùng nhau. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 33: Điểm nằm giữa hai '
                 'điểm. Tia**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được trong ba điểm thẳng '
                           'hàng có một và chỉ một điểm nằm giữa hai điểm còn lại.',
                           'Quy tắc/công thức **Hai tia đối nhau** trong bài được xác định bởi: Chung gốc '
                           '$O$ và tạo thành một đường thẳng.',
                           'Trong mọi trường hợp, **Hai tia đối nhau** luôn được tính bằng công thức $x \\in '
                           'A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 33: Điểm nằm giữa hai điểm. Tia.',
                           'Với bài toán minh họa: “Trên đường thẳng $xy$ lấy điểm $O$. Điểm $A$ thuộc tia '
                           '$Ox$, điểm $B$ thuộc tia $Oy$ ($A, B$ khác $O$). Trong ba điểm $A, O, B$ điểm '
                           'nào nằm...”, lời giải đúng là: Vì $Ox$ và $Oy$ là hai tia đối nhau gốc $O$ nên '
                           'điểm $O$ nằm giữa hai điểm $A$ và $B$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 33: Điểm nằm giữa hai điểm. Tia. b) '
                        '**Đúng** theo công thức trọng tâm **Hai tia đối nhau** (Chung gốc $O$ và tạo thành '
                        'một đường thẳng). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ '
                        'không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của **Hai '
                        'tia đối nhau**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 33: Điểm nằm giữa hai điểm. Tia** để giải quyết tình huống sau: '
                 'Trên đường thẳng $xy$ lấy điểm $O$. Điểm $A$ thuộc tia $Ox$, điểm $B$ thuộc tia $Oy$ ($A, '
                 'B$ khác $O$). Trong ba điểm $A, O, B$ điểm nào nằm giữa hai điểm còn lại? Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Vì $Ox$ và $Oy$ là hai tia đối nhau gốc $O$ nên điểm $O$ nằm giữa hai điểm $A$ và '
                        '$B$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 33: Điểm nằm giữa hai điểm. Tia: Vì $Ox$ và $Oy$ là hai '
                        'tia đối nhau gốc $O$ nên điểm $O$ nằm giữa hai điểm $A$ và $B$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên một đường thẳng lấy $5$ điểm phân biệt. Hỏi có tất cả bao nhiêu tia được tạo thành từ '
                 '$5$ điểm đó làm gốc (hai tia trùng nhau chỉ tính là $1$ tia)?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Mỗi điểm trên đường thẳng là gốc chung của $2$ tia đối nhau. Có $5$ điểm nên có $5 '
                        '\\cdot 2 = 10$ (tia).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch08-hinh-hoc-co-ban',
  'context_title': 'Chương VIII: Những hình hình học cơ bản',
  'context': 'Chương VIII · SGK Toán 6: Điểm, đường thẳng, tia, đoạn thẳng, trung điểm và góc.',
  'title': 'Bài 34: Đoạn thẳng. Độ dài đoạn thẳng',
  'icon': '📐',
  'description': 'Khái niệm đoạn thẳng, độ dài đoạn thẳng và tính chất cộng độ dài đoạn thẳng khi có điểm '
                 'nằm giữa.',
  'requirements': ['Nhận biết được đoạn thẳng $AB$, đo và so sánh độ dài các đoạn thẳng.',
                   'Vận dụng hệ thức $AM + MB = AB$ khi điểm $M$ nằm giữa hai điểm $A$ và $B$ để tính độ dài '
                   'đoạn thẳng.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Điểm M nằm giữa A và B** ($AM + MB = AB '
                   '\\Rightarrow MB = AB - AM$) vào giải bài tập.'],
  'definition': '- **Đoạn thẳng $AB$** (hay đoạn thẳng $BA$) là hình gồm điểm $A$, điểm $B$ và tất cả các '
                'điểm nằm giữa $A$ và $B$. Hai điểm $A, B$ gọi là **hai đầu mút**.\n'
                '- Mỗi đoạn thẳng có một **độ dài** là một số dương.\n'
                '- Nếu điểm $M$ nằm giữa hai điểm $A$ và $B$ thì $AM + MB = AB$.',
  'theory': '### 1. Điểm nằm giữa trên một tia\n'
            '- Trên tia $Ox$, lấy hai điểm $A$ và $B$. Nếu $OA < OB$ thì **điểm $A$ nằm giữa hai điểm $O$ và '
            '$B$**, khi đó $OA + AB = OB \\Rightarrow AB = OB - OA$.\n'
            '### 2. Đếm số đoạn thẳng\n'
            '- Với $n$ điểm phân biệt, cứ $2$ điểm tạo thành $1$ đoạn thẳng nên có $\\dfrac{n(n - 1)}{2}$ '
            'đoạn thẳng.',
  'formulas': [{'category': 'I. Cộng độ dài đoạn thẳng',
                'items': [{'name': 'Điểm M nằm giữa A và B',
                           'formula': '$AM + MB = AB \\Rightarrow MB = AB - AM$'},
                          {'name': 'Hai điểm trên tia Ox',
                           'formula': 'Nếu $OA < OB$ thì $A$ nằm giữa $O, B$ và $AB = OB - OA$'}]}],
  'example': 'Trên tia $Ox$ lấy hai điểm $A, B$ sao cho $OA = 3\\text{ cm}, OB = 7\\text{ cm}$. Tính độ dài '
             'đoạn thẳng $AB$.',
  'example_answer': 'Trên tia $Ox$, vì $OA < OB$ ($3\\text{ cm} < 7\\text{ cm}$) nên điểm $A$ nằm giữa hai '
                    'điểm $O$ và $B$. Suy ra $AB = OB - OA = 7 - 3 = 4\\text{ cm}$.',
  'real_life': 'Đo chiều dài mép bàn, khoảng cách giữa các trạm dừng xe buýt trên cùng một con đường thẳng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho điểm $M$ nằm giữa hai điểm $A$ và $B$. Biết $AM = 3\\text{ cm}, AB = 8\\text{ cm}$. Độ '
                 'dài đoạn thẳng $MB$ là:',
            'options': ['$11\\text{ cm}$', '$5\\text{ cm}$', '$4\\text{ cm}$', '$3\\text{ cm}$'],
            'answer': 1,
            'solution': 'Vì $M$ nằm giữa $A$ và $B$ nên $AM + MB = AB \\Rightarrow MB = 8 - 3 = 5\\text{ '
                        'cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trên tia $Ox$ lấy hai điểm $A$ và $B$ sao cho $OA = 4\\text{ cm}, OB = 9\\text{ cm}$. Điểm '
                 'nào nằm giữa hai điểm còn lại?',
            'options': ['Điểm $O$', 'Điểm $B$', 'Điểm $A$', 'Không có điểm nào'],
            'answer': 2,
            'solution': 'Trên tia $Ox$, vì $OA < OB$ ($4 < 9$) nên điểm $A$ nằm giữa hai điểm $O$ và $B$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 34: Đoạn thẳng. Độ dài đoạn thẳng**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Điểm M nằm giữa A và B**?',
            'options': ['Nếu $OA < OB$ thì $A$ nằm giữa $O, B$ và $AB = OB - OA$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        '$AM + MB = AB \\Rightarrow MB = AB - AM$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 34: Đoạn thẳng. Độ dài đoạn thẳng, **Điểm M '
                        'nằm giữa A và B** được xác định bởi: $AM + MB = AB \\Rightarrow MB = AB - AM$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Đoạn thẳng. Độ dài đoạn thẳng**, nội dung/biểu thức Nếu $OA < OB$ thì $A$ '
                 'nằm giữa $O, B$ và $AB = OB - OA$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hai điểm trên tia Ox',
                        'Điểm M nằm giữa A và B',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 34: Đoạn thẳng. Độ dài đoạn thẳng, biểu thức/quy tắc Nếu $OA < OB$ thì '
                        '$A$ nằm giữa $O, B$ và $AB = OB - OA$ chính là nội dung của **Hai điểm trên tia '
                        'Ox**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho ba điểm $A, B, C$ thẳng hàng, biết $AB = 5\\text{ cm}, BC = 3\\text{ cm}, AC = '
                 '8\\text{ cm}$. Điểm nào nằm giữa hai điểm còn lại?',
            'options': ['Điểm $A$', 'Điểm $B$', 'Điểm $C$', 'Không xác định được'],
            'answer': 1,
            'solution': 'Vì $AB + BC = 5 + 3 = 8\\text{ cm} = AC$ nên điểm $B$ nằm giữa hai điểm $A$ và $C$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Đoạn thẳng. Độ dài đoạn thẳng** (Chương VIII: Những hình hình học cơ '
                 'bản), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Nhận biết được đoạn thẳng $AB$, đo và so sánh độ dài các đoạn thẳng.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 34: Đoạn thẳng. Độ dài đoạn thẳng: Nhận biết được đoạn '
                        'thẳng $AB$, đo và so sánh độ dài các đoạn thẳng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trên tia $Ox$ lấy hai điểm $A, B$ sao cho $OA = 3\\text{ cm}, OB = 7\\text{ cm}$. Mỗi '
                 'khẳng định sau đúng hay sai?',
            'statements': ['Điểm $A$ nằm giữa hai điểm $O$ và $B$',
                           'Độ dài đoạn thẳng $AB$ bằng $4\\text{ cm}$',
                           '$OA > AB$',
                           'Điểm $A$ là trung điểm của đoạn thẳng $OB$'],
            'answer': [True, True, False, False],
            'solution': 'a) Đúng ($OA < OB$). b) Đúng ($AB = 7 - 3 = 4\\text{ cm}$). c) Sai vì $3 < 4$. d) '
                        'Sai vì $OA = 3\\text{ cm} \\ne AB = 4\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 34: Đoạn thẳng. Độ dài '
                 'đoạn thẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được đoạn thẳng $AB$, đo '
                           'và so sánh độ dài các đoạn thẳng.',
                           'Quy tắc/công thức **Điểm M nằm giữa A và B** trong bài được xác định bởi: $AM + '
                           'MB = AB \\Rightarrow MB = AB - AM$.',
                           'Trong mọi trường hợp, **Điểm M nằm giữa A và B** luôn được tính bằng công thức '
                           '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ '
                           'phần tử – tập hợp) mà không cần điều kiện của Bài 34: Đoạn thẳng. Độ dài đoạn '
                           'thẳng.',
                           'Với bài toán minh họa: “Trên tia $Ox$ lấy hai điểm $A, B$ sao cho $OA = 3\\text{ '
                           'cm}, OB = 7\\text{ cm}$. Tính độ dài đoạn thẳng $AB$.”, lời giải đúng là: Trên '
                           'tia $Ox$, vì $OA < OB$ ($3\\text{ cm} < 7\\text{ cm}$) nên điểm $A$ nằm giữa hai '
                           'điểm $O$ và $B$. Suy ra $AB = OB - OA = 7 - 3 = 4\\text{ cm}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 34: Đoạn thẳng. Độ dài đoạn thẳng. b) '
                        '**Đúng** theo công thức trọng tâm **Điểm M nằm giữa A và B** ($AM + MB = AB '
                        '\\Rightarrow MB = AB - AM$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin '
                        'A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung '
                        'của **Điểm M nằm giữa A và B**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 34: Đoạn thẳng. Độ dài đoạn thẳng** để giải quyết tình huống sau: '
                 'Trên tia $Ox$ lấy hai điểm $A, B$ sao cho $OA = 3\\text{ cm}, OB = 7\\text{ cm}$. Tính độ '
                 'dài đoạn thẳng $AB$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Trên tia $Ox$, vì $OA < OB$ ($3\\text{ cm} < 7\\text{ cm}$) nên điểm $A$ nằm giữa '
                        'hai điểm $O$ và $B$. Suy ra $AB = OB - OA = 7 - 3 = 4\\text{ cm}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 34: Đoạn thẳng. Độ dài đoạn thẳng: Trên tia $Ox$, vì $OA '
                        '< OB$ ($3\\text{ cm} < 7\\text{ cm}$) nên điểm $A$ nằm giữa hai điểm $O$ và $B$. '
                        'Suy ra $AB = OB - OA = 7 - 3 = 4\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên đường thẳng lấy $4$ điểm $A, B, C, D$ theo thứ tự đó. Biết $AC = 9\\text{ cm}, BD = '
                 '11\\text{ cm}$ và $BC = 4\\text{ cm}$. Tính độ dài đoạn thẳng $AD$ (đơn vị cm).',
            'answer': ['16'],
            'unit': None,
            'solution': 'Ta có $AB = AC - BC = 9 - 4 = 5\\text{ cm}$. Suy ra $AD = AB + BD = 5 + 11 = '
                        '16\\text{ cm}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch08-hinh-hoc-co-ban',
  'context_title': 'Chương VIII: Những hình hình học cơ bản',
  'context': 'Chương VIII · SGK Toán 6: Điểm, đường thẳng, tia, đoạn thẳng, trung điểm và góc.',
  'title': 'Bài 35: Trung điểm của đoạn thẳng',
  'icon': '📐',
  'description': 'Định nghĩa trung điểm của đoạn thẳng, điều kiện để một điểm là trung điểm và cách tính độ '
                 'dài đoạn thẳng.',
  'requirements': ['Nắm vững hai điều kiện để $M$ là trung điểm của đoạn thẳng $AB$: $M$ nằm giữa $A, B$ và '
                   '$MA = MB$.',
                   'Vận dụng tính chất $MA = MB = \\dfrac{AB}{2}$ để giải các bài toán tính độ dài đoạn '
                   'thẳng.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Công thức độ dài** ($M$ là trung điểm của '
                   '$AB \\Rightarrow MA = MB = \\dfrac{AB}{2}$ hay $AB = 2 \\cdot MA$) vào giải bài tập.'],
  'definition': '- **Trung điểm** $M$ của đoạn thẳng $AB$ là điểm **nằm giữa** hai điểm $A, B$ và **cách '
                'đều** hai điểm đó ($MA = MB$).\n'
                '- Nếu $M$ là trung điểm của đoạn thẳng $AB$ thì $MA = MB = \\dfrac{AB}{2}$.',
  'theory': '### 1. Điều kiện nhận biết trung điểm\n'
            '- Điểm $M$ là trung điểm của $AB \\Leftrightarrow \\begin{cases} M\\text{ nằm giữa }A\\text{ và '
            '}B \\\\ MA = MB \\end{cases} \\Leftrightarrow AM + MB = AB\\text{ và }MA = MB$.\n'
            '- Chú ý: nếu chỉ có $MA = MB$ mà chưa biết $M$ thuộc đoạn thẳng $AB$ thì **chưa kết luận** được '
            '$M$ là trung điểm của $AB$ (vì $A, M, B$ có thể tạo thành tam giác cân).',
  'formulas': [{'category': 'I. Trung điểm của đoạn thẳng',
                'items': [{'name': 'Công thức độ dài',
                           'formula': '$M$ là trung điểm của $AB \\Rightarrow MA = MB = \\dfrac{AB}{2}$ hay '
                                      '$AB = 2 \\cdot MA$'},
                          {'name': 'Khoảng cách giữa hai trung điểm',
                           'formula': 'Nếu $C \\in AB$, $M$ là trung điểm $AC$, $N$ là trung điểm $CB$ thì '
                                      '$MN = \\dfrac{AB}{2}$'}]}],
  'example': 'Cho đoạn thẳng $AB = 12\\text{ cm}$. Gọi $C$ là trung điểm của $AB$, $D$ là trung điểm của '
             '$AC$. Tính độ dài đoạn thẳng $DB$.',
  'example_answer': 'Ta có $AC = CB = 12 : 2 = 6\\text{ cm}$; $DC = AC : 2 = 3\\text{ cm}$. Vì $C$ nằm giữa '
                    '$D$ và $B$ nên $DB = DC + CB = 3 + 6 = 9\\text{ cm}$.',
  'real_life': 'Xác định điểm chính giữa của thanh bập bênh hoặc cưa đôi một thanh gỗ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $M$ là trung điểm của đoạn thẳng $AB$ dài $10\\text{ cm}$. Độ dài đoạn thẳng $MA$ là:',
            'options': ['$10\\text{ cm}$', '$20\\text{ cm}$', '$5\\text{ cm}$', '$2{,}5\\text{ cm}$'],
            'answer': 2,
            'solution': 'Ta có $MA = AB : 2 = 10 : 2 = 5\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho điểm $I$ là trung điểm của đoạn thẳng $CD$. Biết $IC = 4{,}5\\text{ cm}$, độ dài đoạn '
                 'thẳng $CD$ là:',
            'options': ['$4{,}5\\text{ cm}$', '$2{,}25\\text{ cm}$', '$18\\text{ cm}$', '$9\\text{ cm}$'],
            'answer': 3,
            'solution': 'Ta có $CD = 2 \\cdot IC = 2 \\cdot 4{,}5 = 9\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 35: Trung điểm của đoạn thẳng**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Công thức độ dài**?',
            'options': ['$M$ là trung điểm của $AB \\Rightarrow MA = MB = \\dfrac{AB}{2}$ hay $AB = 2 \\cdot '
                        'MA$',
                        'Nếu $C \\in AB$, $M$ là trung điểm $AC$, $N$ là trung điểm $CB$ thì $MN = '
                        '\\dfrac{AB}{2}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 35: Trung điểm của đoạn thẳng, **Công thức độ '
                        'dài** được xác định bởi: $M$ là trung điểm của $AB \\Rightarrow MA = MB = '
                        '\\dfrac{AB}{2}$ hay $AB = 2 \\cdot MA$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 35: Trung điểm của đoạn thẳng**, nội dung/biểu thức Nếu $C \\in AB$, $M$ là '
                 'trung điểm $AC$, $N$ là trung điểm $CB$ thì $MN = \\dfrac{AB}{2}$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Công thức độ dài',
                        'Khoảng cách giữa hai trung điểm',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 35: Trung điểm của đoạn thẳng, biểu thức/quy tắc Nếu $C \\in AB$, $M$ là '
                        'trung điểm $AC$, $N$ là trung điểm $CB$ thì $MN = \\dfrac{AB}{2}$ chính là nội dung '
                        'của **Khoảng cách giữa hai trung điểm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho đoạn thẳng $AB = 12\\text{ cm}$. Gọi $C$ là trung điểm của $AB$, $D$ là trung điểm của '
                 '$AC$. Độ dài đoạn thẳng $DB$ là:',
            'options': ['$6\\text{ cm}$', '$3\\text{ cm}$', '$9\\text{ cm}$', '$4{,}5\\text{ cm}$'],
            'answer': 2,
            'solution': 'Ta có $CB = 6\\text{ cm}$ và $DC = 3\\text{ cm}$, suy ra $DB = DC + CB = 9\\text{ '
                        'cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 35: Trung điểm của đoạn thẳng** (Chương VIII: Những hình hình học cơ bản), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Nắm vững hai điều kiện để $M$ là trung điểm của đoạn thẳng $AB$: $M$ nằm giữa $A, '
                        'B$ và $MA = MB$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 35: Trung điểm của đoạn thẳng: Nắm vững hai điều kiện '
                        'để $M$ là trung điểm của đoạn thẳng $AB$: $M$ nằm giữa $A, B$ và $MA = MB$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét trung điểm của đoạn thẳng. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Nếu $MA = MB$ thì $M$ luôn là trung điểm của đoạn thẳng $AB$',
                           'Nếu $M$ nằm giữa $A, B$ và $MA = MB$ thì $M$ là trung điểm của $AB$',
                           'Mỗi đoạn thẳng chỉ có duy nhất một trung điểm',
                           'Nếu $AM = MB = \\dfrac{AB}{2}$ thì $M$ là trung điểm của $AB$'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì $M$ có thể không nằm trên đoạn thẳng $AB$. b), c), d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 35: Trung điểm của đoạn '
                 'thẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nắm vững hai điều kiện để $M$ là '
                           'trung điểm của đoạn thẳng $AB$: $M$ nằm giữa $A, B$ và $MA = MB$.',
                           'Quy tắc/công thức **Công thức độ dài** trong bài được xác định bởi: $M$ là trung '
                           'điểm của $AB \\Rightarrow MA = MB = \\dfrac{AB}{2}$ hay $AB = 2 \\cdot MA$.',
                           'Trong mọi trường hợp, **Công thức độ dài** luôn được tính bằng công thức $x \\in '
                           'A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 35: Trung điểm của đoạn thẳng.',
                           'Với bài toán minh họa: “Cho đoạn thẳng $AB = 12\\text{ cm}$. Gọi $C$ là trung '
                           'điểm của $AB$, $D$ là trung điểm của $AC$. Tính độ dài đoạn thẳng $DB$.”, lời '
                           'giải đúng là: Ta có $AC = CB = 12 : 2 = 6\\text{ cm}$; $DC = AC : 2 = 3\\text{ '
                           'cm}$. Vì $C$ nằm giữa $D$ và $B$ nên $DB = DC + CB = 3 + 6 = 9\\text{ cm}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 35: Trung điểm của đoạn thẳng. b) **Đúng** '
                        'theo công thức trọng tâm **Công thức độ dài** ($M$ là trung điểm của $AB '
                        '\\Rightarrow MA = MB = \\dfrac{AB}{2}$ hay $AB = 2 \\cdot MA$). c) **Sai** vì $x '
                        '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Công thức độ dài**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 35: Trung điểm của đoạn thẳng** để giải quyết tình huống sau: Cho '
                 'đoạn thẳng $AB = 12\\text{ cm}$. Gọi $C$ là trung điểm của $AB$, $D$ là trung điểm của '
                 '$AC$. Tính độ dài đoạn thẳng $DB$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $AC = CB = 12 : 2 = 6\\text{ cm}$; $DC = AC : 2 = 3\\text{ cm}$. Vì $C$ nằm '
                        'giữa $D$ và $B$ nên $DB = DC + CB = 3 + 6 = 9\\text{ cm}$.',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 35: Trung điểm của đoạn thẳng: Ta có $AC = CB = 12 : 2 = '
                        '6\\text{ cm}$; $DC = AC : 2 = 3\\text{ cm}$. Vì $C$ nằm giữa $D$ và $B$ nên $DB = '
                        'DC + CB = 3 + 6 = 9\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho điểm $C$ nằm giữa hai điểm $A$ và $B$ sao cho $AB = 16\\text{ cm}$. Gọi $M, N$ lần '
                 'lượt là trung điểm của $AC$ và $CB$. Tính độ dài đoạn thẳng $MN$ (đơn vị cm).',
            'answer': ['8'],
            'unit': None,
            'solution': 'Ta có $MN = MC + CN = \\dfrac{AC}{2} + \\dfrac{CB}{2} = \\dfrac{AC + CB}{2} = '
                        '\\dfrac{AB}{2} = 8$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch08-hinh-hoc-co-ban',
  'context_title': 'Chương VIII: Những hình hình học cơ bản',
  'context': 'Chương VIII · SGK Toán 6: Điểm, đường thẳng, tia, đoạn thẳng, trung điểm và góc.',
  'title': 'Bài 36: Góc',
  'icon': '📐',
  'description': 'Khái niệm góc, đỉnh và cạnh của góc, cách kí hiệu góc, góc bẹt và điểm nằm trong góc.',
  'requirements': ['Nhận biết được góc, xác định đúng đỉnh và hai cạnh của góc; đọc và viết đúng kí hiệu góc '
                   '$\\widehat{xOy}$.',
                   'Nhận biết được góc bẹt và điểm nằm trong một góc.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Góc đỉnh O, cạnh Ox và Oy** (Kí hiệu '
                   '$\\widehat{xOy}$ hoặc $\\widehat{AOB}$ (với $A \\in Ox, B \\in Oy$)) vào giải bài tập.'],
  'definition': '- **Góc** là hình gồm **hai tia chung gốc**. Gốc chung của hai tia gọi là **đỉnh** của góc, '
                'hai tia là **hai cạnh** của góc.\n'
                '- Góc tạo bởi hai tia $Ox, Oy$ được kí hiệu là $\\widehat{xOy}$ (hoặc $\\widehat{yOx}$, '
                'hoặc $\\widehat{O}$).\n'
                '- **Góc bẹt** là góc có hai cạnh là hai tia đối nhau.',
  'theory': '### 1. Cách viết tên góc\n'
            '- Chữ cái chỉ **đỉnh của góc luôn viết ở giữa**: ví dụ góc đỉnh $A$ có hai cạnh $AB, AC$ được '
            'viết là $\\widehat{BAC}$ hoặc $\\widehat{CAB}$.\n'
            '### 2. Điểm trong của góc\n'
            '- Cho góc $\\widehat{xOy}$ khác góc bẹt. Nếu tia $Oz$ nằm giữa hai tia $Ox, Oy$ thì mọi điểm '
            '$M$ thuộc tia $Oz$ ($M \\ne O$) là **điểm trong** của góc $\\widehat{xOy}$.\n'
            '- Nếu từ gốc $O$ vẽ $n$ tia phân biệt thì số góc tạo thành là $\\dfrac{n(n - 1)}{2}$.',
  'formulas': [{'category': 'I. Kí hiệu và đếm số góc',
                'items': [{'name': 'Góc đỉnh O, cạnh Ox và Oy',
                           'formula': 'Kí hiệu $\\widehat{xOy}$ hoặc $\\widehat{AOB}$ (với $A \\in Ox, B '
                                      '\\in Oy$)'},
                          {'name': 'Số góc tạo bởi n tia chung gốc',
                           'formula': 'Số góc $= \\dfrac{n(n - 1)}{2}$'}]}],
  'example': 'Cho $4$ tia chung gốc $Oa, Ob, Oc, Od$. Hỏi có tất cả bao nhiêu góc được tạo thành?',
  'example_answer': 'Mỗi cặp tia chung gốc tạo thành một góc nên số góc là $\\dfrac{4 \\cdot (4 - 1)}{2} = '
                    '6$ (góc).',
  'real_life': 'Góc mở của chiếc compa, góc giữa hai kim đồng hồ và góc tạo bởi hai mái nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc $\\widehat{mOn}$ có đỉnh và hai cạnh là:',
            'options': ['Đỉnh $m$, hai cạnh $On$ và $Om$',
                        'Đỉnh $n$, hai cạnh $Om$ và $On$',
                        'Đỉnh $O$, hai cạnh $mn$ và $Om$',
                        'Đỉnh $O$, hai cạnh $Om$ và $On$'],
            'answer': 3,
            'solution': 'Chữ cái ở giữa chỉ đỉnh nên đỉnh là $O$, hai cạnh là hai tia $Om$ và $On$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Góc có hai cạnh là hai tia đối nhau được gọi là:',
            'options': ['Góc bẹt', 'Góc vuông', 'Góc nhọn', 'Góc tù'],
            'answer': 0,
            'solution': 'Theo định nghĩa, góc có hai cạnh là hai tia đối nhau là góc bẹt.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 36: Góc**, công thức hoặc quy tắc nào sau đây biểu diễn '
                 'đúng **Góc đỉnh O, cạnh Ox và Oy**?',
            'options': ['Số góc $= \\dfrac{n(n - 1)}{2}$',
                        'Kí hiệu $\\widehat{xOy}$ hoặc $\\widehat{AOB}$ (với $A \\in Ox, B \\in Oy$)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 36: Góc, **Góc đỉnh O, cạnh Ox và Oy** được '
                        'xác định bởi: Kí hiệu $\\widehat{xOy}$ hoặc $\\widehat{AOB}$ (với $A \\in Ox, B '
                        '\\in Oy$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36: Góc**, nội dung/biểu thức Số góc $= \\dfrac{n(n - 1)}{2}$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Góc đỉnh O, cạnh Ox và Oy',
                        'Quan hệ phần tử – tập hợp',
                        'Số góc tạo bởi n tia chung gốc',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 36: Góc, biểu thức/quy tắc Số góc $= \\dfrac{n(n - 1)}{2}$ chính là nội '
                        'dung của **Số góc tạo bởi n tia chung gốc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Từ gốc $O$ kẻ $5$ tia phân biệt $Oa, Ob, Oc, Od, Oe$. Số góc được tạo thành là:',
            'options': ['$5$ góc', '$15$ góc', '$20$ góc', '$10$ góc'],
            'answer': 3,
            'solution': 'Số góc tạo bởi $5$ tia chung gốc là $\\dfrac{5 \\cdot 4}{2} = 10$ (góc).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 36: Góc** (Chương VIII: Những hình hình học cơ bản), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được góc, xác định đúng đỉnh và hai cạnh của góc; đọc và viết đúng kí '
                        'hiệu góc $\\widehat{xOy}$.',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 36: Góc: Nhận biết được góc, xác định đúng đỉnh và hai '
                        'cạnh của góc; đọc và viết đúng kí hiệu góc $\\widehat{xOy}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho góc $\\widehat{xOy}$ khác góc bẹt, điểm $A \\in Ox$ và $B \\in Oy$ ($A, B$ khác $O$), '
                 'điểm $M$ nằm giữa $A$ và $B$. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Góc $\\widehat{xOy}$ còn được kí hiệu là $\\widehat{AOB}$',
                           'Đỉnh của góc $\\widehat{AOB}$ là điểm $A$',
                           'Điểm $M$ là điểm nằm trong góc $\\widehat{xOy}$',
                           'Hai cạnh của góc $\\widehat{xOy}$ là hai đoạn thẳng $OA$ và $OB$'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng. b) Sai vì đỉnh là điểm $O$. c) Đúng. d) Sai vì hai cạnh của góc là hai tia '
                        '$Ox, Oy$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 36: Góc**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được góc, xác định đúng '
                           'đỉnh và hai cạnh của góc; đọc và viết đúng kí hiệu góc $\\widehat{xOy}$.',
                           'Quy tắc/công thức **Góc đỉnh O, cạnh Ox và Oy** trong bài được xác định bởi: Kí '
                           'hiệu $\\widehat{xOy}$ hoặc $\\widehat{AOB}$ (với $A \\in Ox, B \\in Oy$).',
                           'Trong mọi trường hợp, **Góc đỉnh O, cạnh Ox và Oy** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 36: Góc.',
                           'Với bài toán minh họa: “Cho $4$ tia chung gốc $Oa, Ob, Oc, Od$. Hỏi có tất cả '
                           'bao nhiêu góc được tạo thành?”, lời giải đúng là: Mỗi cặp tia chung gốc tạo '
                           'thành một góc nên số góc là $\\dfrac{4 \\cdot (4 - 1)}{2} = 6$ (góc).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 36: Góc. b) **Đúng** theo công thức trọng '
                        'tâm **Góc đỉnh O, cạnh Ox và Oy** (Kí hiệu $\\widehat{xOy}$ hoặc $\\widehat{AOB}$ '
                        '(với $A \\in Ox, B \\in Oy$)). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin '
                        'A$ ($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung '
                        'của **Góc đỉnh O, cạnh Ox và Oy**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 36: Góc** để giải quyết tình huống sau: Cho $4$ tia chung gốc '
                 '$Oa, Ob, Oc, Od$. Hỏi có tất cả bao nhiêu góc được tạo thành? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Mỗi cặp tia chung gốc tạo thành một góc nên số góc là $\\dfrac{4 \\cdot (4 - 1)}{2} '
                        '= 6$ (góc).',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 36: Góc: Mỗi cặp tia chung gốc tạo thành một góc nên số '
                        'góc là $\\dfrac{4 \\cdot (4 - 1)}{2} = 6$ (góc).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một tam giác $ABC$, nếu nối đỉnh $A$ với $3$ điểm phân biệt nằm trên cạnh $BC$ (khác '
                 '$B$ và $C$) thì có tất cả bao nhiêu góc có đỉnh là $A$ trên hình vẽ?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Từ đỉnh $A$ có tất cả $2 + 3 = 5$ tia ($AB, AC$ và $3$ tia nối tới $3$ điểm trên '
                        '$BC$). Số góc đỉnh $A$ là $\\dfrac{5 \\cdot 4}{2} = 10$ (góc).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch08-hinh-hoc-co-ban',
  'context_title': 'Chương VIII: Những hình hình học cơ bản',
  'context': 'Chương VIII · SGK Toán 6: Điểm, đường thẳng, tia, đoạn thẳng, trung điểm và góc.',
  'title': 'Bài 37: Số đo góc',
  'icon': '📐',
  'description': 'Đơn vị đo góc, cách dùng thước đo góc và phân loại góc vuông, góc nhọn, góc tù, góc bẹt '
                 'theo số đo.',
  'requirements': ['Biết dùng thước đo góc để xác định số đo của một góc và so sánh hai góc dựa vào số đo.',
                   'Phân biệt được góc nhọn ($0^\\circ < \\alpha < 90^\\circ$), góc vuông ($90^\\circ$), góc '
                   'tù ($90^\\circ < \\alpha < 180^\\circ$) và góc bẹt ($180^\\circ$).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Góc nhọn và Góc vuông** (Nhọn: $0^\\circ < '
                   '\\alpha < 90^\\circ$; Vuông: $\\alpha = 90^\\circ$) vào giải bài tập.'],
  'definition': '- Mỗi góc có một **số đo** (đơn vị là **độ**, kí hiệu $^\\circ$). Số đo của một góc không '
                'vượt quá $180^\\circ$.\n'
                '- **Góc vuông**: có số đo bằng $90^\\circ$. **Góc nhọn**: lớn hơn $0^\\circ$ và nhỏ hơn '
                '$90^\\circ$.\n'
                '- **Góc tù**: lớn hơn $90^\\circ$ và nhỏ hơn $180^\\circ$. **Góc bẹt**: có số đo bằng '
                '$180^\\circ$.',
  'theory': '### 1. So sánh các loại góc\n'
            '- Thứ tự độ lớn: $\\text{Góc nhọn} < \\text{Góc vuông } (90^\\circ) < \\text{Góc tù} < '
            '\\text{Góc bẹt } (180^\\circ)$.\n'
            '### 2. Góc giữa hai kim đồng hồ tại giờ đúng\n'
            '- Mặt đồng hồ chia thành $12$ khoảng đều nhau, ứng với $360^\\circ : 12 = 30^\\circ$ cho mỗi '
            'khoảng giữa hai số liên tiếp.',
  'formulas': [{'category': 'I. Phân loại góc theo số đo alpha',
                'items': [{'name': 'Góc nhọn và Góc vuông',
                           'formula': 'Nhọn: $0^\\circ < \\alpha < 90^\\circ$; Vuông: $\\alpha = 90^\\circ$'},
                          {'name': 'Góc tù và Góc bẹt',
                           'formula': 'Tù: $90^\\circ < \\alpha < 180^\\circ$; Bẹt: $\\alpha = 180^\\circ$'},
                          {'name': 'Mặt đồng hồ',
                           'formula': 'Mỗi khoảng giữa $2$ số liên tiếp trên đồng hồ ứng với $30^\\circ$'}]}],
  'example': 'Xác định loại của các góc có số đo $45^\\circ; 90^\\circ; 135^\\circ; 180^\\circ$.',
  'example_answer': 'Góc $45^\\circ$ là góc nhọn; $90^\\circ$ là góc vuông; $135^\\circ$ là góc tù; '
                    '$180^\\circ$ là góc bẹt.',
  'real_life': 'Đo góc nghiêng của thang tựa vào tường, góc sút bóng và góc giữa hai kim đồng hồ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc bẹt có số đo bằng:',
            'options': ['$180^\\circ$', '$90^\\circ$', '$100^\\circ$', '$360^\\circ$'],
            'answer': 0,
            'solution': 'Góc bẹt có số đo bằng $180^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Góc có số đo bằng $125^\\circ$ là góc gì?',
            'options': ['Góc nhọn', 'Góc tù', 'Góc vuông', 'Góc bẹt'],
            'answer': 1,
            'solution': 'Vì $90^\\circ < 125^\\circ < 180^\\circ$ nên đó là góc tù.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 37: Số đo góc**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Góc nhọn và Góc vuông**?',
            'options': ['Tù: $90^\\circ < \\alpha < 180^\\circ$; Bẹt: $\\alpha = 180^\\circ$',
                        'Mỗi khoảng giữa $2$ số liên tiếp trên đồng hồ ứng với $30^\\circ$',
                        'Nhọn: $0^\\circ < \\alpha < 90^\\circ$; Vuông: $\\alpha = 90^\\circ$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 37: Số đo góc, **Góc nhọn và Góc vuông** được '
                        'xác định bởi: Nhọn: $0^\\circ < \\alpha < 90^\\circ$; Vuông: $\\alpha = '
                        '90^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 37: Số đo góc**, nội dung/biểu thức Tù: $90^\\circ < \\alpha < 180^\\circ$; '
                 'Bẹt: $\\alpha = 180^\\circ$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Góc nhọn và Góc vuông',
                        'Mặt đồng hồ',
                        'Quan hệ phần tử – tập hợp',
                        'Góc tù và Góc bẹt'],
            'answer': 3,
            'solution': 'Trong Bài 37: Số đo góc, biểu thức/quy tắc Tù: $90^\\circ < \\alpha < 180^\\circ$; '
                        'Bẹt: $\\alpha = 180^\\circ$ chính là nội dung của **Góc tù và Góc bẹt**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\widehat{A} = 75^\\circ, \\widehat{B} = 90^\\circ, \\widehat{C} = 110^\\circ$. Khẳng '
                 'định nào sau đây là đúng?',
            'options': ['$\\widehat{A} < \\widehat{B} < \\widehat{C}$',
                        '$\\widehat{A}$ là góc tù',
                        '$\\widehat{C}$ là góc nhọn',
                        '$\\widehat{C} < \\widehat{B}$'],
            'answer': 0,
            'solution': 'Vì $75^\\circ < 90^\\circ < 110^\\circ$ nên $\\widehat{A} < \\widehat{B} < '
                        '\\widehat{C}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 37: Số đo góc** (Chương VIII: Những hình hình học cơ bản), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Biết dùng thước đo góc để xác định số đo của một góc và so sánh hai góc dựa vào số '
                        'đo.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 37: Số đo góc: Biết dùng thước đo góc để xác định số '
                        'đo của một góc và so sánh hai góc dựa vào số đo.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét số đo của các góc. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Góc có số đo $95^\\circ$ là góc nhọn',
                           'Mọi góc nhọn đều nhỏ hơn góc tù',
                           'Lúc $3$ giờ đúng, kim giờ và kim phút tạo thành góc vuông $90^\\circ$',
                           'Lúc $6$ giờ đúng, kim giờ và kim phút tạo thành góc bẹt $180^\\circ$'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì $90^\\circ < 95^\\circ < 180^\\circ$ là góc tù. b), c), d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 37: Số đo góc**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Biết dùng thước đo góc để xác định '
                           'số đo của một góc và so sánh hai góc dựa vào số đo.',
                           'Quy tắc/công thức **Góc nhọn và Góc vuông** trong bài được xác định bởi: Nhọn: '
                           '$0^\\circ < \\alpha < 90^\\circ$; Vuông: $\\alpha = 90^\\circ$.',
                           'Trong mọi trường hợp, **Góc nhọn và Góc vuông** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 37: Số đo góc.',
                           'Với bài toán minh họa: “Xác định loại của các góc có số đo $45^\\circ; '
                           '90^\\circ; 135^\\circ; 180^\\circ$.”, lời giải đúng là: Góc $45^\\circ$ là góc '
                           'nhọn; $90^\\circ$ là góc vuông; $135^\\circ$ là góc tù; $180^\\circ$ là góc '
                           'bẹt.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 37: Số đo góc. b) **Đúng** theo công thức '
                        'trọng tâm **Góc nhọn và Góc vuông** (Nhọn: $0^\\circ < \\alpha < 90^\\circ$; Vuông: '
                        '$\\alpha = 90^\\circ$). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ '
                        '($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Góc nhọn và Góc vuông**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 37: Số đo góc** để giải quyết tình huống sau: Xác định loại của '
                 'các góc có số đo $45^\\circ; 90^\\circ; 135^\\circ; 180^\\circ$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Góc $45^\\circ$ là góc nhọn; $90^\\circ$ là góc vuông; $135^\\circ$ là góc tù; '
                        '$180^\\circ$ là góc bẹt.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 37: Số đo góc: Góc $45^\\circ$ là góc nhọn; $90^\\circ$ '
                        'là góc vuông; $135^\\circ$ là góc tù; $180^\\circ$ là góc bẹt.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lúc $5$ giờ đúng, góc tạo bởi kim giờ và kim phút của đồng hồ có số đo bằng bao nhiêu độ?',
            'answer': ['150'],
            'unit': None,
            'solution': 'Lúc $5$ giờ đúng, hai kim cách nhau $5$ khoảng số. Mỗi khoảng ứng với $30^\\circ$ '
                        'nên số đo góc là $5 \\cdot 30^\\circ = 150^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch09-du-lieu-xac-suat-thuc-nghiem',
  'context_title': 'Chương IX: Dữ liệu và xác suất thực nghiệm',
  'context': 'Chương IX · SGK Toán 6: Thu thập dữ liệu, bảng thống kê, biểu đồ tranh, biểu đồ cột và xác '
             'suất thực nghiệm.',
  'title': 'Bài 38: Dữ liệu và thu thập dữ liệu',
  'icon': '📊',
  'description': 'Phân loại dữ liệu là số (số liệu) và dữ liệu không phải là số, các cách thu thập dữ liệu '
                 'và tính hợp lí của dữ liệu.',
  'requirements': ['Phân biệt được dữ liệu là số (số liệu) và dữ liệu không phải là số.',
                   'Nhận biết được các phương pháp thu thập dữ liệu và phát hiện được dữ liệu không hợp lí.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hai loại dữ liệu** (Dữ liệu là số (số liệu) '
                   'và Dữ liệu không phải là số) vào giải bài tập.'],
  'definition': '- Thông tin thu thập được gọi là **dữ liệu**. Dữ liệu được chia thành hai loại: **dữ liệu '
                'là số** (gọi là **số liệu**) và **dữ liệu không phải là số**.\n'
                '- Các cách thu thập dữ liệu: quan sát, làm thí nghiệm, lập phiếu hỏi (phỏng vấn) hoặc thu '
                'thập từ những nguồn có sẵn (sách báo, Internet).\n'
                '- Dữ liệu cần đảm bảo **tính hợp lí** (đúng định dạng, nằm trong phạm vi thực tế cho phép).',
  'theory': '### 1. Ví dụ phân loại dữ liệu\n'
            '- Số liệu: chiều cao ($\\text{cm}$), cân nặng ($\\text{kg}$), điểm kiểm tra Toán, số quyển '
            'sách.\n'
            '- Dữ liệu không phải là số: tên các môn thể thao, màu sắc yêu thích, xếp loại học lực (Tốt, '
            'Khá, Đạt).\n'
            '### 2. Kiểm tra tính hợp lí\n'
            '- Ví dụ: sĩ số lớp là $-35$ hoặc chiều cao học sinh lớp 6 là $15\\text{ m}$ hoặc tỉ lệ phần '
            'trăm vượt quá $100\\%$ là dữ liệu **không hợp lí**.',
  'formulas': [{'category': 'I. Phân loại và kiểm tra dữ liệu',
                'items': [{'name': 'Hai loại dữ liệu',
                           'formula': 'Dữ liệu là số (số liệu) và Dữ liệu không phải là số'},
                          {'name': 'Tiêu chí hợp lí',
                           'formula': 'Đúng kiểu dữ liệu, nằm trong miền giá trị thực tế, tổng phần trăm $= '
                                      '100\\%$'}]}],
  'example': 'Trong danh sách các loài động vật sống dưới nước: Cá heo, Cá chép, Chim đại bàng, Tôm hùm. Dữ '
             'liệu nào không hợp lí?',
  'example_answer': '“Chim đại bàng” là dữ liệu không hợp lí vì đại bàng không phải là động vật sống dưới '
                    'nước.',
  'real_life': 'Thiết kế phiếu khảo sát ý kiến học sinh và kiểm tra lỗi nhập điểm trong sổ điểm điện tử.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dữ liệu nào sau đây **không phải** là số liệu?',
            'options': ['Chiều cao của các bạn trong lớp',
                        'Màu sắc yêu thích của các bạn',
                        'Số anh chị em ruột của mỗi bạn',
                        'Điểm kiểm tra môn Toán'],
            'answer': 1,
            'solution': 'Màu sắc yêu thích (xanh, đỏ, vàng, ...) là dữ liệu không phải là số.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi ghi thân nhiệt (đơn vị $^\\circ\\text{C}$) của $4$ bệnh nhân là: $36{,}5;\\ 37{,}2;\\ '
                 '120;\\ 38{,}0$, số liệu nào không hợp lí?',
            'options': ['$36{,}5$', '$37{,}2$', '$120$', '$38{,}0$'],
            'answer': 2,
            'solution': 'Thân nhiệt con người không thể là $120^\\circ\\text{C}$ nên $120$ là số liệu không '
                        'hợp lí.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 38: Dữ liệu và thu thập dữ liệu**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Hai loại dữ liệu**?',
            'options': ['Đúng kiểu dữ liệu, nằm trong miền giá trị thực tế, tổng phần trăm $= 100\\%$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        'Dữ liệu là số (số liệu) và Dữ liệu không phải là số'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 38: Dữ liệu và thu thập dữ liệu, **Hai loại '
                        'dữ liệu** được xác định bởi: Dữ liệu là số (số liệu) và Dữ liệu không phải là số.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 38: Dữ liệu và thu thập dữ liệu**, nội dung/biểu thức Đúng kiểu dữ liệu, nằm '
                 'trong miền giá trị thực tế, tổng phần trăm $= 100\\%$ là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Tiêu chí hợp lí', 'Hai loại dữ liệu', 'Quan hệ phần tử – tập hợp', 'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 38: Dữ liệu và thu thập dữ liệu, biểu thức/quy tắc Đúng kiểu dữ liệu, nằm '
                        'trong miền giá trị thực tế, tổng phần trăm $= 100\\%$ chính là nội dung của **Tiêu '
                        'chí hợp lí**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để biết môn thể thao được các bạn trong lớp 6A yêu thích nhất, cách thu thập dữ liệu phù '
                 'hợp nhất là:',
            'options': ['Làm thí nghiệm trong phòng hoá học',
                        'Lập phiếu hỏi các bạn trong lớp 6A',
                        'Tra cứu trên mạng Internet',
                        'Quan sát thời tiết'],
            'answer': 1,
            'solution': 'Lập phiếu hỏi (hoặc phỏng vấn) các bạn trong lớp 6A là cách trực tiếp và phù hợp '
                        'nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 38: Dữ liệu và thu thập dữ liệu** (Chương IX: Dữ liệu và xác suất thực '
                 'nghiệm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được dữ liệu là số (số liệu) và dữ liệu không phải là số.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 38: Dữ liệu và thu thập dữ liệu: Phân biệt được dữ '
                        'liệu là số (số liệu) và dữ liệu không phải là số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét việc phân loại và kiểm tra dữ liệu. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Điểm kiểm tra môn Toán của học sinh là số liệu',
                           'Tên các tỉnh thành của Việt Nam là dữ liệu không phải là số',
                           'Điểm kiểm tra trên thang điểm $10$ ghi là $12$ điểm vẫn hợp lí',
                           'Sĩ số một lớp học luôn phải là một số tự nhiên dương'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì thang điểm $10$ không thể có điểm $12$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 38: Dữ liệu và thu thập '
                 'dữ liệu**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phân biệt được dữ liệu là số (số '
                           'liệu) và dữ liệu không phải là số.',
                           'Quy tắc/công thức **Hai loại dữ liệu** trong bài được xác định bởi: Dữ liệu là '
                           'số (số liệu) và Dữ liệu không phải là số.',
                           'Trong mọi trường hợp, **Hai loại dữ liệu** luôn được tính bằng công thức $x \\in '
                           'A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 38: Dữ liệu và thu thập dữ liệu.',
                           'Với bài toán minh họa: “Trong danh sách các loài động vật sống dưới nước: Cá '
                           'heo, Cá chép, Chim đại bàng, Tôm hùm. Dữ liệu nào không hợp lí?”, lời giải đúng '
                           'là: “Chim đại bàng” là dữ liệu không hợp lí vì đại bàng không phải là động vật '
                           'sống dưới nước.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 38: Dữ liệu và thu thập dữ liệu. b) '
                        '**Đúng** theo công thức trọng tâm **Hai loại dữ liệu** (Dữ liệu là số (số liệu) và '
                        'Dữ liệu không phải là số). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ '
                        '($y$ không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Hai loại dữ liệu**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 38: Dữ liệu và thu thập dữ liệu** để giải quyết tình huống sau: '
                 'Trong danh sách các loài động vật sống dưới nước: Cá heo, Cá chép, Chim đại bàng, Tôm hùm. '
                 'Dữ liệu nào không hợp lí? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        '“Chim đại bàng” là dữ liệu không hợp lí vì đại bàng không phải là động vật sống '
                        'dưới nước.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 38: Dữ liệu và thu thập dữ liệu: “Chim đại bàng” là dữ '
                        'liệu không hợp lí vì đại bàng không phải là động vật sống dưới nước.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong dãy số liệu ghi số tuổi của $6$ học sinh lớp 6 là: $11;\\ 12;\\ -12;\\ 11;\\ 12;\\ '
                 '150$, có bao nhiêu giá trị không hợp lí?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Hai giá trị không hợp lí là $-12$ (tuổi không thể âm) và $150$ (vượt quá tuổi học '
                        'sinh lớp 6), vậy có $2$ giá trị.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch09-du-lieu-xac-suat-thuc-nghiem',
  'context_title': 'Chương IX: Dữ liệu và xác suất thực nghiệm',
  'context': 'Chương IX · SGK Toán 6: Thu thập dữ liệu, bảng thống kê, biểu đồ tranh, biểu đồ cột và xác '
             'suất thực nghiệm.',
  'title': 'Bài 39: Bảng thống kê và biểu đồ tranh',
  'icon': '📊',
  'description': 'Cách đọc, lập bảng thống kê từ bảng kiểm đếm và cách đọc, vẽ biểu đồ tranh sử dụng các '
                 'biểu tượng.',
  'requirements': ['Đọc và lập được bảng thống kê từ dữ liệu thu thập được.',
                   'Đọc và tính được số liệu thực tế trên biểu đồ tranh thông qua quy ước giá trị của mỗi '
                   'biểu tượng.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Số lượng của mỗi đối tượng** ($\\text{Số '
                   'lượng} = (\\text{Số biểu tượng}) \\cdot (\\text{Giá trị 1 biểu tượng})$) vào giải bài '
                   'tập.'],
  'definition': '- **Bảng thống kê** là cách trình bày dữ liệu chi tiết theo hàng và cột để thuận tiện cho '
                'việc so sánh và tính toán.\n'
                '- **Biểu đồ tranh** sử dụng các hình ảnh, biểu tượng để biểu diễn số liệu. Mỗi biểu tượng '
                'trọn vẹn ứng với một số lượng $k$ đơn vị quy ước; nửa biểu tượng ứng với $\\dfrac{k}{2}$ '
                'đơn vị.',
  'theory': '### 1. Cách đọc biểu đồ tranh\n'
            '- Bước 1: Đọc kĩ **chú giải** ở cuối biểu đồ để biết $1$ biểu tượng ứng với bao nhiêu đơn vị.\n'
            '- Bước 2: Đếm số biểu tượng của mỗi dòng rồi nhân với giá trị của $1$ biểu tượng.\n'
            '- Ví dụ: nếu $1$ ngôi sao ứng với $10$ học sinh thì $3$ ngôi sao rưỡi ứng với $3 \\cdot 10 + 5 '
            '= 35$ học sinh.',
  'formulas': [{'category': 'I. Tính toán trên biểu đồ tranh',
                'items': [{'name': 'Số lượng của mỗi đối tượng',
                           'formula': '$\\text{Số lượng} = (\\text{Số biểu tượng}) \\cdot (\\text{Giá trị 1 '
                                      'biểu tượng})$'},
                          {'name': 'Số biểu tượng cần vẽ',
                           'formula': '$\\text{Số biểu tượng} = \\text{Số lượng} : (\\text{Giá trị 1 biểu '
                                      'tượng})$'}]}],
  'example': 'Trong biểu đồ tranh về số sách bán được, mỗi hình quyển sách ứng với $20$ quyển. Ngày Chủ nhật '
             'có $4$ hình quyển sách. Hỏi ngày Chủ nhật bán được bao nhiêu quyển sách?',
  'example_answer': 'Số sách bán được trong ngày Chủ nhật là $4 \\cdot 20 = 80$ (quyển sách).',
  'real_life': 'Trình bày trực quan sản lượng nông sản, số lượng học sinh đạt giải hoặc lượng xe bán ra trên '
               'báo chí.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một biểu đồ tranh, mỗi biểu tượng mặt cười ứng với $5$ học sinh. Tổ 1 có $3$ biểu '
                 'tượng mặt cười nghĩa là tổ 1 có:',
            'options': ['$3$ học sinh', '$8$ học sinh', '$15$ học sinh', '$5$ học sinh'],
            'answer': 2,
            'solution': 'Số học sinh của tổ 1 là $3 \\cdot 5 = 15$ (học sinh).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu mỗi biểu tượng quả bóng ứng với $10$ quả bóng thì để biểu diễn $45$ quả bóng ta cần '
                 'vẽ:',
            'options': ['$4$ quả bóng',
                        '$5$ quả bóng',
                        '$45$ quả bóng',
                        '$4$ quả bóng nguyên và nửa quả bóng'],
            'answer': 3,
            'solution': 'Ta có $45 = 4 \\cdot 10 + 5$ nên cần $4$ biểu tượng nguyên và $1$ nửa biểu tượng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 39: Bảng thống kê và biểu đồ tranh**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Số lượng của mỗi đối tượng**?',
            'options': ['$\\text{Số lượng} = (\\text{Số biểu tượng}) \\cdot (\\text{Giá trị 1 biểu tượng})$',
                        '$\\text{Số biểu tượng} = \\text{Số lượng} : (\\text{Giá trị 1 biểu tượng})$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 39: Bảng thống kê và biểu đồ tranh, **Số '
                        'lượng của mỗi đối tượng** được xác định bởi: $\\text{Số lượng} = (\\text{Số biểu '
                        'tượng}) \\cdot (\\text{Giá trị 1 biểu tượng})$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 39: Bảng thống kê và biểu đồ tranh**, nội dung/biểu thức $\\text{Số biểu '
                 'tượng} = \\text{Số lượng} : (\\text{Giá trị 1 biểu tượng})$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Số lượng của mỗi đối tượng',
                        'Số biểu tượng cần vẽ',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 39: Bảng thống kê và biểu đồ tranh, biểu thức/quy tắc $\\text{Số biểu '
                        'tượng} = \\text{Số lượng} : (\\text{Giá trị 1 biểu tượng})$ chính là nội dung của '
                        '**Số biểu tượng cần vẽ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biểu đồ tranh ghi số cây trồng của hai lớp (mỗi hình cái cây $= 8$ cây): lớp 6A có $5$ '
                 'hình, lớp 6B có $3$ hình. Lớp 6A trồng nhiều hơn lớp 6B bao nhiêu cây?',
            'options': ['$2$ cây', '$40$ cây', '$16$ cây', '$24$ cây'],
            'answer': 2,
            'solution': 'Hiệu số hình là $5 - 3 = 2$ (hình), ứng với $2 \\cdot 8 = 16$ (cây).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 39: Bảng thống kê và biểu đồ tranh** (Chương IX: Dữ liệu và xác suất thực '
                 'nghiệm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Đọc và lập được bảng thống kê từ dữ liệu thu thập được.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 39: Bảng thống kê và biểu đồ tranh: Đọc và lập được '
                        'bảng thống kê từ dữ liệu thu thập được.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong biểu đồ tranh thống kê số học sinh giỏi các lớp khối 6, mỗi biểu tượng ngôi sao ứng '
                 'với $4$ học sinh. Biết lớp 6A có $3$ ngôi sao, lớp 6B có $4$ ngôi sao, lớp 6C có $2$ ngôi '
                 'sao. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Lớp 6A có $12$ học sinh giỏi',
                           'Lớp 6B có nhiều học sinh giỏi nhất',
                           'Lớp 6C có $2$ học sinh giỏi',
                           'Cả ba lớp có tất cả $36$ học sinh giỏi'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng ($3 \\cdot 4 = 12$). b) Đúng ($4$ sao $= 16$ em). c) Sai vì $2 \\cdot 4 = '
                        '8$ em. d) Đúng ($(3 + 4 + 2) \\cdot 4 = 36$ em).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 39: Bảng thống kê và '
                 'biểu đồ tranh**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Đọc và lập được bảng thống kê từ '
                           'dữ liệu thu thập được.',
                           'Quy tắc/công thức **Số lượng của mỗi đối tượng** trong bài được xác định bởi: '
                           '$\\text{Số lượng} = (\\text{Số biểu tượng}) \\cdot (\\text{Giá trị 1 biểu '
                           'tượng})$.',
                           'Trong mọi trường hợp, **Số lượng của mỗi đối tượng** luôn được tính bằng công '
                           'thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan '
                           'hệ phần tử – tập hợp) mà không cần điều kiện của Bài 39: Bảng thống kê và biểu '
                           'đồ tranh.',
                           'Với bài toán minh họa: “Trong biểu đồ tranh về số sách bán được, mỗi hình quyển '
                           'sách ứng với $20$ quyển. Ngày Chủ nhật có $4$ hình quyển sách. Hỏi ngày Chủ nhật '
                           'bán...”, lời giải đúng là: Số sách bán được trong ngày Chủ nhật là $4 \\cdot 20 '
                           '= 80$ (quyển sách).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 39: Bảng thống kê và biểu đồ tranh. b) '
                        '**Đúng** theo công thức trọng tâm **Số lượng của mỗi đối tượng** ($\\text{Số lượng} '
                        '= (\\text{Số biểu tượng}) \\cdot (\\text{Giá trị 1 biểu tượng})$). c) **Sai** vì $x '
                        '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Số lượng của mỗi đối tượng**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 39: Bảng thống kê và biểu đồ tranh** để giải quyết tình huống '
                 'sau: Trong biểu đồ tranh về số sách bán được, mỗi hình quyển sách ứng với $20$ quyển. Ngày '
                 'Chủ nhật có $4$ hình quyển sách. Hỏi ngày Chủ nhật bán được bao nhiêu quyển sách? Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Số sách bán được trong ngày Chủ nhật là $4 \\cdot 20 = 80$ (quyển sách).',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 39: Bảng thống kê và biểu đồ tranh: Số sách bán được '
                        'trong ngày Chủ nhật là $4 \\cdot 20 = 80$ (quyển sách).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên biểu đồ tranh thống kê số xe đạp bán được trong $3$ tháng, số biểu tượng xe đạp của '
                 'tháng 1, tháng 2, tháng 3 lần lượt là $4;\\ 6;\\ 5$ biểu tượng. Biết mỗi biểu tượng ứng '
                 'với $12$ chiếc xe đạp. Hỏi cả $3$ tháng cửa hàng bán được bao nhiêu chiếc xe đạp?',
            'answer': ['180'],
            'unit': None,
            'solution': 'Tổng số biểu tượng là $4 + 6 + 5 = 15$. Tổng số xe bán được là $15 \\cdot 12 = 180$ '
                        '(chiếc).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch09-du-lieu-xac-suat-thuc-nghiem',
  'context_title': 'Chương IX: Dữ liệu và xác suất thực nghiệm',
  'context': 'Chương IX · SGK Toán 6: Thu thập dữ liệu, bảng thống kê, biểu đồ tranh, biểu đồ cột và xác '
             'suất thực nghiệm.',
  'title': 'Bài 40: Biểu đồ cột',
  'icon': '📊',
  'description': 'Cách đọc, mô tả dữ liệu và vẽ biểu đồ cột từ bảng thống kê cho trước.',
  'requirements': ['Đọc và phân tích được số liệu từ biểu đồ cột (giá trị lớn nhất, nhỏ nhất, tổng, hiệu, tỉ '
                   'lệ).',
                   'Biết cách vẽ biểu đồ cột gồm trục ngang, trục đứng, các cột hình chữ nhật có cùng chiều '
                   'rộng và tiêu đề.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tổng số liệu** ($N = x_1 + x_2 + \\dots + '
                   'x_k$) vào giải bài tập.'],
  'definition': '- Trong **biểu đồ cột**, trục ngang thường ghi danh sách các đối tượng thống kê, trục đứng '
                'ghi số liệu theo khoảng chia đều.\n'
                '- Mỗi đối tượng được biểu diễn bởi một hình chữ nhật (cột) có cùng chiều rộng và có **chiều '
                'cao tương ứng với số liệu** của đối tượng đó.',
  'theory': '### 1. Phân tích số liệu từ biểu đồ cột\n'
            '- Cột cao nhất ứng với đối tượng có số lượng lớn nhất; cột thấp nhất ứng với đối tượng có số '
            'lượng nhỏ nhất.\n'
            '- Tính tổng số lượng các nhóm và tỉ số của một nhóm so với tổng thể.',
  'formulas': [{'category': 'I. Phân tích biểu đồ cột',
                'items': [{'name': 'Tổng số liệu', 'formula': '$N = x_1 + x_2 + \\dots + x_k$'},
                          {'name': 'Tỉ số của nhóm i so với tổng',
                           'formula': '$\\dfrac{x_i}{N}$ (hoặc $\\dfrac{x_i}{N} \\cdot 100\\%$)'}]}],
  'example': 'Biểu đồ cột cho biết số học sinh lớp 6A thích các môn: Toán $12$, Ngữ văn $8$, Tiếng Anh $10$, '
             'Tin học $15$ (mỗi bạn chọn $1$ môn). Hỏi lớp 6A có bao nhiêu học sinh tham gia khảo sát?',
  'example_answer': 'Tổng số học sinh tham gia khảo sát là $12 + 8 + 10 + 15 = 45$ (học sinh).',
  'real_life': 'Biểu diễn lượng mưa các tháng trong năm, dân số các khu vực hoặc doanh thu theo quý.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong biểu đồ cột đứng, độ cao của mỗi cột biểu diễn:',
            'options': ['Chiều rộng của bảng thống kê',
                        'Số lượng các đối tượng được khảo sát',
                        'Khoảng cách giữa các đối tượng',
                        'Số liệu tương ứng của đối tượng đó'],
            'answer': 3,
            'solution': 'Độ cao của mỗi cột tương ứng với số liệu của đối tượng đó trên trục đứng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu đồ cột ghi số bàn thắng của $4$ đội bóng A, B, C, D lần lượt là $8; 12; 5; 10$. Đội '
                 'ghi được nhiều bàn thắng nhất là:',
            'options': ['Đội B', 'Đội A', 'Đội C', 'Đội D'],
            'answer': 0,
            'solution': 'Đội B có số bàn thắng lớn nhất là $12$ bàn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 40: Biểu đồ cột**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Tổng số liệu**?',
            'options': ['$\\dfrac{x_i}{N}$ (hoặc $\\dfrac{x_i}{N} \\cdot 100\\%$)',
                        '$N = x_1 + x_2 + \\dots + x_k$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 40: Biểu đồ cột, **Tổng số liệu** được xác '
                        'định bởi: $N = x_1 + x_2 + \\dots + x_k$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 40: Biểu đồ cột**, nội dung/biểu thức $\\dfrac{x_i}{N}$ (hoặc $\\dfrac{x_i}{N} '
                 '\\cdot 100\\%$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tổng số liệu',
                        'Quan hệ phần tử – tập hợp',
                        'Tỉ số của nhóm i so với tổng',
                        'Hai cách mô tả'],
            'answer': 2,
            'solution': 'Trong Bài 40: Biểu đồ cột, biểu thức/quy tắc $\\dfrac{x_i}{N}$ (hoặc '
                        '$\\dfrac{x_i}{N} \\cdot 100\\%$) chính là nội dung của **Tỉ số của nhóm i so với '
                        'tổng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Theo số liệu $4$ đội bóng A ($8$ bàn), B ($12$ bàn), C ($5$ bàn), D ($10$ bàn), tổng số '
                 'bàn thắng của cả $4$ đội là:',
            'options': ['$30$ bàn', '$25$ bàn', '$40$ bàn', '$35$ bàn'],
            'answer': 3,
            'solution': 'Tổng số bàn thắng là $8 + 12 + 5 + 10 = 35$ (bàn).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 40: Biểu đồ cột** (Chương IX: Dữ liệu và xác suất thực nghiệm), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc và phân tích được số liệu từ biểu đồ cột (giá trị lớn nhất, nhỏ nhất, tổng, '
                        'hiệu, tỉ lệ).',
                        'Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 40: Biểu đồ cột: Đọc và phân tích được số liệu từ biểu '
                        'đồ cột (giá trị lớn nhất, nhỏ nhất, tổng, hiệu, tỉ lệ).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Biểu đồ cột cho biết số học sinh lớp 6A thích các môn: Toán $12$, Ngữ văn $8$, Tiếng Anh '
                 '$10$, Tin học $15$ (mỗi bạn chọn đúng $1$ môn). Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Môn Tin học được nhiều bạn yêu thích nhất',
                           'Có tất cả $45$ học sinh tham gia khảo sát',
                           'Số bạn thích Toán nhiều hơn số bạn thích Ngữ văn là $2$ bạn',
                           'Số bạn thích Tiếng Anh chiếm $\\dfrac{2}{9}$ tổng số học sinh tham gia'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng ($15$ là lớn nhất). b) Đúng ($12 + 8 + 10 + 15 = 45$). c) Sai vì $12 - 8 = '
                        '4$ bạn. d) Đúng vì $\\dfrac{10}{45} = \\dfrac{2}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 40: Biểu đồ cột**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Đọc và phân tích được số liệu từ '
                           'biểu đồ cột (giá trị lớn nhất, nhỏ nhất, tổng, hiệu, tỉ lệ).',
                           'Quy tắc/công thức **Tổng số liệu** trong bài được xác định bởi: $N = x_1 + x_2 + '
                           '\\dots + x_k$.',
                           'Trong mọi trường hợp, **Tổng số liệu** luôn được tính bằng công thức $x \\in A$ '
                           '($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 40: Biểu đồ cột.',
                           'Với bài toán minh họa: “Biểu đồ cột cho biết số học sinh lớp 6A thích các môn: '
                           'Toán $12$, Ngữ văn $8$, Tiếng Anh $10$, Tin học $15$ (mỗi bạn chọn $1$ môn). Hỏi '
                           'lớp...”, lời giải đúng là: Tổng số học sinh tham gia khảo sát là $12 + 8 + 10 + '
                           '15 = 45$ (học sinh).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 40: Biểu đồ cột. b) **Đúng** theo công '
                        'thức trọng tâm **Tổng số liệu** ($N = x_1 + x_2 + \\dots + x_k$). c) **Sai** vì $x '
                        '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Tổng số liệu**. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 40: Biểu đồ cột** để giải quyết tình huống sau: Biểu đồ cột cho '
                 'biết số học sinh lớp 6A thích các môn: Toán $12$, Ngữ văn $8$, Tiếng Anh $10$, Tin học '
                 '$15$ (mỗi bạn chọn $1$ môn). Hỏi lớp 6A có bao nhiêu học sinh tham gia khảo sát? Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Tổng số học sinh tham gia khảo sát là $12 + 8 + 10 + 15 = 45$ (học sinh).',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 40: Biểu đồ cột: Tổng số học sinh tham gia khảo sát là '
                        '$12 + 8 + 10 + 15 = 45$ (học sinh).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biểu đồ cột ghi số ly trà sữa một quán bán được từ thứ Hai đến thứ Sáu lần lượt là: $40;\\ '
                 '35;\\ 50;\\ 45;\\ 60$. Tính trung bình mỗi ngày trong $5$ ngày đó quán bán được bao nhiêu '
                 'ly trà sữa?',
            'answer': ['46'],
            'unit': None,
            'solution': 'Trung bình mỗi ngày quán bán được $(40 + 35 + 50 + 45 + 60) : 5 = 230 : 5 = 46$ '
                        '(ly).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch09-du-lieu-xac-suat-thuc-nghiem',
  'context_title': 'Chương IX: Dữ liệu và xác suất thực nghiệm',
  'context': 'Chương IX · SGK Toán 6: Thu thập dữ liệu, bảng thống kê, biểu đồ tranh, biểu đồ cột và xác '
             'suất thực nghiệm.',
  'title': 'Bài 41: Biểu đồ cột kép',
  'icon': '📊',
  'description': 'Nhận biết, đọc và phân tích biểu đồ cột kép để so sánh hai bộ dữ liệu cùng loại.',
  'requirements': ['Hiểu được mục đích sử dụng biểu đồ cột kép là để trực quan hóa việc so sánh hai bộ dữ '
                   'liệu cùng loại.',
                   'Đọc, so sánh và tính được tổng, hiệu giữa hai cột ghép liền nhau của mỗi đối tượng.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tổng của đối tượng i** ($T_i = a_i + b_i$ '
                   '($a_i, b_i$: số liệu hai cột thành phần)) vào giải bài tập.'],
  'definition': '- Để **so sánh hai bộ dữ liệu cùng loại** một cách trực quan, người ta ghép hai biểu đồ cột '
                'thành một **biểu đồ cột kép**.\n'
                '- Tại mỗi đối tượng trên trục ngang có **hai cột đặt sát cạnh nhau** với hai màu (hoặc kí '
                'hiệu) khác nhau kèm theo bảng chú giải.',
  'theory': '### 1. Cách đọc và phân tích biểu đồ cột kép\n'
            '- Tổng của hai cột ghép tại một đối tượng cho biết tổng số lượng của cả hai nhóm tại đối tượng '
            'đó.\n'
            '- Độ chênh lệch chiều cao giữa hai cột ghép tại một đối tượng cho biết hiệu giữa hai bộ số liệu '
            'tại đối tượng đó.',
  'formulas': [{'category': 'I. Phân tích tại mỗi đối tượng trên biểu đồ cột kép',
                'items': [{'name': 'Tổng của đối tượng i',
                           'formula': '$T_i = a_i + b_i$ ($a_i, b_i$: số liệu hai cột thành phần)'},
                          {'name': 'Độ chênh lệch tại đối tượng i', 'formula': '$D_i = |a_i - b_i|$'}]}],
  'example': 'Biểu đồ cột kép thống kê số học sinh nam và nữ của lớp 6A là $(18\\text{ nam}, 22\\text{ nữ})$ '
             'và lớp 6B là $(20\\text{ nam}, 19\\text{ nữ})$. Lớp nào có tổng số học sinh đông hơn?',
  'example_answer': 'Sĩ số lớp 6A là $18 + 22 = 40$ (em); sĩ số lớp 6B là $20 + 19 = 39$ (em). Vậy lớp 6A '
                    'đông hơn.',
  'real_life': 'So sánh lượng mưa trung bình hàng tháng giữa hai thành phố Hà Nội và TP. Hồ Chí Minh, hoặc '
               'doanh số hai chi nhánh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Để so sánh trực quan số học sinh nam và số học sinh nữ của từng lớp trong khối 6, loại '
                 'biểu đồ thích hợp nhất là:',
            'options': ['Biểu đồ cột kép', 'Biểu đồ tranh', 'Biểu đồ cột đơn', 'Bảng kiểm đếm'],
            'answer': 0,
            'solution': 'Để so sánh hai bộ dữ liệu cùng loại (nam và nữ của từng lớp), ta dùng biểu đồ cột '
                        'kép.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trên biểu đồ cột kép, để phân biệt hai cột đặt cạnh nhau của mỗi đối tượng, ta cần dựa '
                 'vào:',
            'options': ['Trục đứng',
                        'Bảng chú giải màu sắc (hoặc kí hiệu) của hai cột',
                        'Độ rộng của trục ngang',
                        'Tên biểu đồ'],
            'answer': 1,
            'solution': 'Bảng chú giải cho biết mỗi màu cột tương ứng với bộ dữ liệu nào.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 41: Biểu đồ cột kép**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Tổng của đối tượng i**?',
            'options': ['$D_i = |a_i - b_i|$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        '$T_i = a_i + b_i$ ($a_i, b_i$: số liệu hai cột thành phần)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 41: Biểu đồ cột kép, **Tổng của đối tượng i** '
                        'được xác định bởi: $T_i = a_i + b_i$ ($a_i, b_i$: số liệu hai cột thành phần).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 41: Biểu đồ cột kép**, nội dung/biểu thức $D_i = |a_i - b_i|$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Tổng của đối tượng i',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả',
                        'Độ chênh lệch tại đối tượng i'],
            'answer': 3,
            'solution': 'Trong Bài 41: Biểu đồ cột kép, biểu thức/quy tắc $D_i = |a_i - b_i|$ chính là nội '
                        'dung của **Độ chênh lệch tại đối tượng i**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biểu đồ cột kép cho biết số huy chương của hai trường A và B: năm 2024 là $(12; 15)$, năm '
                 '2025 là $(18; 14)$. Tổng số huy chương của trường A trong cả hai năm là:',
            'options': ['$30$', '$27$', '$32$', '$29$'],
            'answer': 0,
            'solution': 'Số huy chương của trường A trong hai năm là $12 + 18 = 30$ (huy chương).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 41: Biểu đồ cột kép** (Chương IX: Dữ liệu và xác suất thực nghiệm), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Hiểu được mục đích sử dụng biểu đồ cột kép là để trực quan hóa việc so sánh hai bộ '
                        'dữ liệu cùng loại.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 41: Biểu đồ cột kép: Hiểu được mục đích sử dụng biểu '
                        'đồ cột kép là để trực quan hóa việc so sánh hai bộ dữ liệu cùng loại.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Biểu đồ cột kép thống kê số học sinh nam và nữ của ba lớp: 6A ($18$ nam, $22$ nữ), 6B '
                 '($20$ nam, $20$ nữ), 6C ($21$ nam, $17$ nữ). Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Ở lớp 6B, hai cột biểu diễn số nam và số nữ có chiều cao bằng nhau',
                           'Lớp 6A có số nữ nhiều hơn số nam là $4$ bạn',
                           'Lớp 6C có tổng số học sinh nhiều nhất trong ba lớp',
                           'Tổng số học sinh nam của cả ba lớp là $59$ bạn'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng (cùng bằng $20$). b) Đúng ($22 - 18 = 4$). c) Sai vì 6C có $38$ bạn, nhỏ '
                        'hơn 6A ($40$) và 6B ($40$). d) Đúng ($18 + 20 + 21 = 59$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 41: Biểu đồ cột kép**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được mục đích sử dụng biểu đồ '
                           'cột kép là để trực quan hóa việc so sánh hai bộ dữ liệu cùng loại.',
                           'Quy tắc/công thức **Tổng của đối tượng i** trong bài được xác định bởi: $T_i = '
                           'a_i + b_i$ ($a_i, b_i$: số liệu hai cột thành phần).',
                           'Trong mọi trường hợp, **Tổng của đối tượng i** luôn được tính bằng công thức $x '
                           '\\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần '
                           'tử – tập hợp) mà không cần điều kiện của Bài 41: Biểu đồ cột kép.',
                           'Với bài toán minh họa: “Biểu đồ cột kép thống kê số học sinh nam và nữ của lớp '
                           '6A là $(18\\text{ nam}, 22\\text{ nữ})$ và lớp 6B là $(20\\text{ nam}, 19\\text{ '
                           'nữ})$. L...”, lời giải đúng là: Sĩ số lớp 6A là $18 + 22 = 40$ (em); sĩ số lớp '
                           '6B là $20 + 19 = 39$ (em). Vậy lớp 6A đông hơn.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 41: Biểu đồ cột kép. b) **Đúng** theo công '
                        'thức trọng tâm **Tổng của đối tượng i** ($T_i = a_i + b_i$ ($a_i, b_i$: số liệu hai '
                        'cột thành phần)). c) **Sai** vì $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ '
                        'không thuộc $A$) là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Tổng của đối tượng i**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 41: Biểu đồ cột kép** để giải quyết tình huống sau: Biểu đồ cột '
                 'kép thống kê số học sinh nam và nữ của lớp 6A là $(18\\text{ nam}, 22\\text{ nữ})$ và lớp '
                 '6B là $(20\\text{ nam}, 19\\text{ nữ})$. Lớp nào có tổng số học sinh đông hơn? Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Sĩ số lớp 6A là $18 + 22 = 40$ (em); sĩ số lớp 6B là $20 + 19 = 39$ (em). Vậy lớp '
                        '6A đông hơn.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 41: Biểu đồ cột kép: Sĩ số lớp 6A là $18 + 22 = 40$ '
                        '(em); sĩ số lớp 6B là $20 + 19 = 39$ (em). Vậy lớp 6A đông hơn.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biểu đồ cột kép ghi số lượng máy tính để bàn và máy tính xách tay bán được của một cửa '
                 'hàng trong quý I là $(45; 60)$ và quý II là $(50; 75)$. Trong cả hai quý, số máy tính xách '
                 'tay bán được nhiều hơn số máy tính để bàn là bao nhiêu chiếc?',
            'answer': ['40'],
            'unit': None,
            'solution': 'Tổng máy xách tay là $60 + 75 = 135$; tổng máy để bàn là $45 + 50 = 95$. Hiệu số là '
                        '$135 - 95 = 40$ (chiếc).',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch09-du-lieu-xac-suat-thuc-nghiem',
  'context_title': 'Chương IX: Dữ liệu và xác suất thực nghiệm',
  'context': 'Chương IX · SGK Toán 6: Thu thập dữ liệu, bảng thống kê, biểu đồ tranh, biểu đồ cột và xác '
             'suất thực nghiệm.',
  'title': 'Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm',
  'icon': '📊',
  'description': 'Liệt kê tập hợp các kết quả có thể của một trò chơi, thí nghiệm và xác định khi nào một sự '
                 'kiện xảy ra.',
  'requirements': ['Liệt kê được tập hợp tất cả các kết quả có thể trong các trò chơi, thí nghiệm đơn giản '
                   '(tung đồng xu, gieo xúc xắc, rút thẻ).',
                   'Xác định được một sự kiện có xảy ra hay không và liệt kê các kết quả thuận lợi cho sự '
                   'kiện đó.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tung 1 đồng xu** (Tập hợp kết quả '
                   '$\\{\\text{S}, \\text{N}\\}$ ($2$ kết quả)) vào giải bài tập.'],
  'definition': '- Khi thực hiện một trò chơi hay thí nghiệm, các kết quả có thể xảy ra được gọi là **kết '
                'quả có thể**.\n'
                '- Một **sự kiện** trong trò chơi, thí nghiệm có thể xảy ra hoặc không xảy ra tuỳ thuộc vào '
                'kết quả của trò chơi, thí nghiệm đó.',
  'theory': '### 1. Tập hợp các kết quả có thể thường gặp\n'
            '- Tung một đồng xu: tập hợp kết quả có thể là $\\{\\text{S}, \\text{N}\\}$ (Sấp, Ngửa) gồm $2$ '
            'kết quả.\n'
            '- Gieo một con xúc xắc $6$ mặt: tập hợp kết quả có thể là $\\{1; 2; 3; 4; 5; 6\\}$ chấm gồm $6$ '
            'kết quả.\n'
            '### 2. Các kết quả làm cho sự kiện xảy ra (kết quả thuận lợi)\n'
            '- Ví dụ: khi gieo xúc xắc, sự kiện “Số chấm xuất hiện là số nguyên tố” xảy ra khi kết quả là '
            '$2; 3$ hoặc $5$ chấm.',
  'formulas': [{'category': 'I. Không gian kết quả cơ bản',
                'items': [{'name': 'Tung 1 đồng xu',
                           'formula': 'Tập hợp kết quả $\\{\\text{S}, \\text{N}\\}$ ($2$ kết quả)'},
                          {'name': 'Gieo 1 con xúc xắc',
                           'formula': 'Tập hợp kết quả $\\{1; 2; 3; 4; 5; 6\\}$ ($6$ kết quả)'}]}],
  'example': 'Một hộp có $10$ chiếc thẻ ghi các số từ $1$ đến $10$. Rút ngẫu nhiên $1$ thẻ. Liệt kê các kết '
             'quả làm cho sự kiện “Số trên thẻ là bội của $3$” xảy ra.',
  'example_answer': 'Các số từ $1$ đến $10$ là bội của $3$ gồm $3; 6; 9$. Vậy có $3$ kết quả thuận lợi là '
                    'rút được thẻ ghi số $3; 6$ hoặc $9$.',
  'real_life': 'Xác định các kết quả có thể khi bốc thăm chia bảng thi đấu thể thao hoặc quay vòng quay may '
               'mắn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi tung một đồng xu cân đối một lần, tập hợp các kết quả có thể xảy ra là:',
            'options': ['$\\{\\text{S}\\}$',
                        '$\\{\\text{S}; \\text{N}\\}$',
                        '$\\{\\text{N}\\}$',
                        '$\\{1; 2\\}$'],
            'answer': 1,
            'solution': 'Đồng xu có hai mặt Sấp ($\\text{S}$) và Ngửa ($\\text{N}$) nên tập hợp kết quả là '
                        '$\\{\\text{S}; \\text{N}\\}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Gieo một con xúc xắc $6$ mặt. Sự kiện “Số chấm xuất hiện là số chẵn” xảy ra khi số chấm '
                 'xuất hiện thuộc tập hợp nào?',
            'options': ['$\\{1; 3; 5\\}$', '$\\{2; 3; 5\\}$', '$\\{2; 4; 6\\}$', '$\\{4; 5; 6\\}$'],
            'answer': 2,
            'solution': 'Các số chẵn từ $1$ đến $6$ là $2; 4; 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí '
                 'nghiệm**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tung 1 đồng xu**?',
            'options': ['Tập hợp kết quả $\\{1; 2; 3; 4; 5; 6\\}$ ($6$ kết quả)',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$',
                        'Tập hợp kết quả $\\{\\text{S}, \\text{N}\\}$ ($2$ kết quả)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 42: Kết quả có thể và sự kiện trong trò chơi, '
                        'thí nghiệm, **Tung 1 đồng xu** được xác định bởi: Tập hợp kết quả $\\{\\text{S}, '
                        '\\text{N}\\}$ ($2$ kết quả).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm**, nội dung/biểu thức '
                 'Tập hợp kết quả $\\{1; 2; 3; 4; 5; 6\\}$ ($6$ kết quả) là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Gieo 1 con xúc xắc',
                        'Tung 1 đồng xu',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 0,
            'solution': 'Trong Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm, biểu thức/quy '
                        'tắc Tập hợp kết quả $\\{1; 2; 3; 4; 5; 6\\}$ ($6$ kết quả) chính là nội dung của '
                        '**Gieo 1 con xúc xắc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong hộp có $1$ quả bóng xanh, $1$ quả bóng đỏ và $1$ quả bóng vàng. Lấy ngẫu nhiên đồng '
                 'thời $2$ quả bóng từ hộp. Có tất cả bao nhiêu kết quả có thể đối với màu của hai quả bóng '
                 'lấy ra?',
            'options': ['$2$ kết quả', '$3$ kết quả', '$4$ kết quả', '$6$ kết quả'],
            'answer': 1,
            'solution': 'Các cặp màu có thể là: (Xanh, Đỏ), (Xanh, Vàng), (Đỏ, Vàng) nên có $3$ kết quả.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm** (Chương IX: Dữ '
                 'liệu và xác suất thực nghiệm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Liệt kê được tập hợp tất cả các kết quả có thể trong các trò chơi, thí nghiệm đơn '
                        'giản (tung đồng xu, gieo xúc xắc, rút thẻ).',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí '
                        'nghiệm: Liệt kê được tập hợp tất cả các kết quả có thể trong các trò chơi, thí '
                        'nghiệm đơn giản (tung đồng xu, gieo xúc xắc, rút thẻ).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Gieo một con xúc xắc $6$ mặt một lần. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Có tất cả $6$ kết quả có thể về số chấm xuất hiện',
                           'Sự kiện “Số chấm xuất hiện lớn hơn $4$” có $2$ kết quả thuận lợi là $5$ và $6$',
                           'Sự kiện “Số chấm xuất hiện bằng $7$” có thể xảy ra',
                           'Sự kiện “Số chấm xuất hiện là ước của $6$” có $4$ kết quả thuận lợi'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng ($5; 6$). c) Sai vì xúc xắc chỉ có từ $1$ đến $6$ chấm. d) Đúng '
                        '(các ước của $6$ là $1; 2; 3; 6$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 42: Kết quả có thể và '
                 'sự kiện trong trò chơi, thí nghiệm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Liệt kê được tập hợp tất cả các '
                           'kết quả có thể trong các trò chơi, thí nghiệm đơn giản (tung đồng xu, gieo xúc '
                           'xắc, rút thẻ).',
                           'Quy tắc/công thức **Tung 1 đồng xu** trong bài được xác định bởi: Tập hợp kết '
                           'quả $\\{\\text{S}, \\text{N}\\}$ ($2$ kết quả).',
                           'Trong mọi trường hợp, **Tung 1 đồng xu** luôn được tính bằng công thức $x \\in '
                           'A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc Quan hệ phần tử – '
                           'tập hợp) mà không cần điều kiện của Bài 42: Kết quả có thể và sự kiện trong trò '
                           'chơi, thí nghiệm.',
                           'Với bài toán minh họa: “Một hộp có $10$ chiếc thẻ ghi các số từ $1$ đến $10$. '
                           'Rút ngẫu nhiên $1$ thẻ. Liệt kê các kết quả làm cho sự kiện “Số trên thẻ là bội '
                           'của $3$...”, lời giải đúng là: Các số từ $1$ đến $10$ là bội của $3$ gồm $3; 6; '
                           '9$. Vậy có $3$ kết quả thuận lợi là rút được thẻ ghi số $3; 6$ hoặc $9$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 42: Kết quả có thể và sự kiện trong trò '
                        'chơi, thí nghiệm. b) **Đúng** theo công thức trọng tâm **Tung 1 đồng xu** (Tập hợp '
                        'kết quả $\\{\\text{S}, \\text{N}\\}$ ($2$ kết quả)). c) **Sai** vì $x \\in A$ ($x$ '
                        'thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Tung 1 đồng xu**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm** để '
                 'giải quyết tình huống sau: Một hộp có $10$ chiếc thẻ ghi các số từ $1$ đến $10$. Rút ngẫu '
                 'nhiên $1$ thẻ. Liệt kê các kết quả làm cho sự kiện “Số trên thẻ là bội của $3$” xảy ra. '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.',
                        'Các số từ $1$ đến $10$ là bội của $3$ gồm $3; 6; 9$. Vậy có $3$ kết quả thuận lợi '
                        'là rút được thẻ ghi số $3; 6$ hoặc $9$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí '
                        'nghiệm: Các số từ $1$ đến $10$ là bội của $3$ gồm $3; 6; 9$. Vậy có $3$ kết quả '
                        'thuận lợi là rút được thẻ ghi số $3; 6$ hoặc $9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp có $20$ chiếc thẻ cùng loại được đánh số từ $1$ đến $20$. Rút ngẫu nhiên một chiếc '
                 'thẻ trong hộp. Có bao nhiêu kết quả làm cho sự kiện “Số xuất hiện trên thẻ là số nguyên '
                 'tố” xảy ra?',
            'answer': ['8'],
            'unit': None,
            'solution': 'Các số nguyên tố từ $1$ đến $20$ là $2; 3; 5; 7; 11; 13; 17; 19$ nên có $8$ kết '
                        'quả.',
            'alt': None,
            'note': None}]},
 {'topic': 'l6-ch09-du-lieu-xac-suat-thuc-nghiem',
  'context_title': 'Chương IX: Dữ liệu và xác suất thực nghiệm',
  'context': 'Chương IX · SGK Toán 6: Thu thập dữ liệu, bảng thống kê, biểu đồ tranh, biểu đồ cột và xác '
             'suất thực nghiệm.',
  'title': 'Bài 43: Xác suất thực nghiệm',
  'icon': '📊',
  'description': 'Khái niệm và công thức tính xác suất thực nghiệm của một sự kiện khi thực hiện lặp lại '
                 'nhiều lần một phép thử.',
  'requirements': ['Tính được xác suất thực nghiệm $\\dfrac{k}{n}$ của một sự kiện $A$ khi thực hiện thí '
                   'nghiệm $n$ lần.',
                   'Tính được xác suất thực nghiệm của sự kiện đối lập (“không xảy ra $A$”) và đổi sang tỉ '
                   'số phần trăm.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Xác suất thực nghiệm của sự kiện A** ($P(A) '
                   '= \\dfrac{k}{n}$ ($k$: số lần $A$ xảy ra; $n$: tổng số lần thử)) vào giải bài tập.'],
  'definition': '- Giả sử trong $n$ lần thực hiện liên tiếp một trò chơi hay thí nghiệm, sự kiện $A$ xảy ra '
                '$k$ lần. Khi đó tỉ số $\\dfrac{k}{n}$ được gọi là **xác suất thực nghiệm** của sự kiện $A$ '
                'trong $n$ lần thử đã thực hiện.',
  'theory': '### 1. Công thức xác suất thực nghiệm\n'
            '- $\\text{Xác suất thực nghiệm của sự kiện } A = \\dfrac{\\text{Số lần sự kiện } A\\text{ xảy '
            'ra}}{\\text{Tổng số lần thực hiện}} = \\dfrac{k}{n}$ (có thể rút gọn hoặc viết dưới dạng số '
            'thập phân, tỉ số phần trăm).\n'
            '### 2. Sự kiện không xảy ra $A$\n'
            '- Số lần sự kiện $A$ không xảy ra là $n - k$, do đó xác suất thực nghiệm để $A$ không xảy ra là '
            '$\\dfrac{n - k}{n} = 1 - \\dfrac{k}{n}$.',
  'formulas': [{'category': 'I. Xác suất thực nghiệm',
                'items': [{'name': 'Xác suất thực nghiệm của sự kiện A',
                           'formula': '$P(A) = \\dfrac{k}{n}$ ($k$: số lần $A$ xảy ra; $n$: tổng số lần '
                                      'thử)'},
                          {'name': 'Sự kiện không xảy ra A',
                           'formula': '$\\dfrac{n - k}{n} = 1 - \\dfrac{k}{n}$'}]}],
  'example': 'Bình tung một đồng xu $40$ lần và thấy có $18$ lần xuất hiện mặt ngửa. Tính xác suất thực '
             'nghiệm xuất hiện mặt ngửa và mặt sấp.',
  'example_answer': 'Xác suất thực nghiệm xuất hiện mặt ngửa là $\\dfrac{18}{40} = \\dfrac{9}{20} = 45\\%$. '
                    'Mặt sấp xuất hiện $40 - 18 = 22$ lần nên xác suất thực nghiệm là $\\dfrac{22}{40} = '
                    '\\dfrac{11}{20} = 55\\%$.',
  'real_life': 'Đánh giá tỉ lệ nảy mầm của hạt giống, tỉ lệ sản phẩm đạt chuẩn của dây chuyền sản xuất hoặc '
               'hiệu suất ghi bàn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tung một đồng xu $40$ lần, có $18$ lần xuất hiện mặt ngửa. Xác suất thực nghiệm xuất hiện '
                 'mặt ngửa là:',
            'options': ['$\\dfrac{18}{22}$', '$\\dfrac{11}{20}$', '$\\dfrac{9}{20}$', '$18$'],
            'answer': 2,
            'solution': 'Xác suất thực nghiệm là $\\dfrac{18}{40} = \\dfrac{9}{20}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một xạ thủ bắn $60$ viên đạn vào bia, có $51$ viên trúng đích. Xác suất thực nghiệm xạ thủ '
                 'bắn trúng đích viết dưới dạng tỉ số phần trăm là:',
            'options': ['$51\\%$', '$15\\%$', '$9\\%$', '$85\\%$'],
            'answer': 3,
            'solution': 'Ta có $\\dfrac{51}{60} = 0{,}85 = 85\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 43: Xác suất thực nghiệm**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Xác suất thực nghiệm của sự kiện A**?',
            'options': ['$P(A) = \\dfrac{k}{n}$ ($k$: số lần $A$ xảy ra; $n$: tổng số lần thử)',
                        '$\\dfrac{n - k}{n} = 1 - \\dfrac{k}{n}$',
                        '$x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$)',
                        'Liệt kê $A = \\{0; 1; 2; 3\\}$ hoặc đặc trưng $A = \\{x \\in \\mathbb{N} \\mid x < '
                        '4\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 43: Xác suất thực nghiệm, **Xác suất thực '
                        'nghiệm của sự kiện A** được xác định bởi: $P(A) = \\dfrac{k}{n}$ ($k$: số lần $A$ '
                        'xảy ra; $n$: tổng số lần thử).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 43: Xác suất thực nghiệm**, nội dung/biểu thức $\\dfrac{n - k}{n} = 1 - '
                 '\\dfrac{k}{n}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Xác suất thực nghiệm của sự kiện A',
                        'Sự kiện không xảy ra A',
                        'Quan hệ phần tử – tập hợp',
                        'Hai cách mô tả'],
            'answer': 1,
            'solution': 'Trong Bài 43: Xác suất thực nghiệm, biểu thức/quy tắc $\\dfrac{n - k}{n} = 1 - '
                        '\\dfrac{k}{n}$ chính là nội dung của **Sự kiện không xảy ra A**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Gieo một con xúc xắc $50$ lần, thấy mặt có số chấm chẵn xuất hiện $26$ lần. Xác suất thực '
                 'nghiệm xuất hiện mặt có số chấm lẻ là:',
            'options': ['$\\dfrac{26}{50}$', '$\\dfrac{24}{26}$', '$\\dfrac{12}{25}$', '$\\dfrac{13}{25}$'],
            'answer': 2,
            'solution': 'Số lần xuất hiện mặt lẻ là $50 - 26 = 24$ (lần). Xác suất thực nghiệm là '
                        '$\\dfrac{24}{50} = \\dfrac{12}{25}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 43: Xác suất thực nghiệm** (Chương IX: Dữ liệu và xác suất thực nghiệm), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Sử dụng được thuật ngữ tập hợp, phần tử thuộc ($\\in$) hoặc không thuộc ($\\notin$) '
                        'một tập hợp.',
                        'Cho được một tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất đặc trưng '
                        'cho các phần tử.',
                        'Phân biệt được tập hợp $\\mathbb{N}$ và $\\mathbb{N}^*$; xác định được giá trị từng '
                        'chữ số của số tự nhiên trong hệ thập phân.',
                        'Tính được xác suất thực nghiệm $\\dfrac{k}{n}$ của một sự kiện $A$ khi thực hiện '
                        'thí nghiệm $n$ lần.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 43: Xác suất thực nghiệm: Tính được xác suất thực '
                        'nghiệm $\\dfrac{k}{n}$ của một sự kiện $A$ khi thực hiện thí nghiệm $n$ lần.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Gieo một con xúc xắc $50$ lần: mặt $6$ chấm xuất hiện $9$ lần; mặt có số chấm chẵn xuất '
                 'hiện $26$ lần. Mỗi khẳng định sau đúng hay sai?',
            'statements': ['Xác suất thực nghiệm xuất hiện mặt $6$ chấm là $\\dfrac{9}{50}$',
                           'Xác suất thực nghiệm xuất hiện mặt có số chấm lẻ là $\\dfrac{12}{25}$',
                           'Xác suất thực nghiệm xuất hiện mặt có số chấm nhỏ hơn $6$ là $\\dfrac{41}{50}$',
                           'Xác suất thực nghiệm xuất hiện mặt chẵn là $26\\%$'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng ($\\dfrac{50-26}{50} = \\dfrac{12}{25}$). c) Đúng '
                        '($\\dfrac{50-9}{50} = \\dfrac{41}{50}$). d) Sai vì $\\dfrac{26}{50} = 52\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 43: Xác suất thực '
                 'nghiệm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được xác suất thực nghiệm '
                           '$\\dfrac{k}{n}$ của một sự kiện $A$ khi thực hiện thí nghiệm $n$ lần.',
                           'Quy tắc/công thức **Xác suất thực nghiệm của sự kiện A** trong bài được xác định '
                           'bởi: $P(A) = \\dfrac{k}{n}$ ($k$: số lần $A$ xảy ra; $n$: tổng số lần thử).',
                           'Trong mọi trường hợp, **Xác suất thực nghiệm của sự kiện A** luôn được tính bằng '
                           'công thức $x \\in A$ ($x$ thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) (thuộc '
                           'Quan hệ phần tử – tập hợp) mà không cần điều kiện của Bài 43: Xác suất thực '
                           'nghiệm.',
                           'Với bài toán minh họa: “Bình tung một đồng xu $40$ lần và thấy có $18$ lần xuất '
                           'hiện mặt ngửa. Tính xác suất thực nghiệm xuất hiện mặt ngửa và mặt sấp.”, lời '
                           'giải đúng là: Xác suất thực nghiệm xuất hiện mặt ngửa là $\\dfrac{18}{40} = '
                           '\\dfrac{9}{20} = 45\\%$. Mặt sấp xuất hiện $40 - 18 = 22$ lần nên xác suất thực '
                           'n...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 43: Xác suất thực nghiệm. b) **Đúng** theo '
                        'công thức trọng tâm **Xác suất thực nghiệm của sự kiện A** ($P(A) = \\dfrac{k}{n}$ '
                        '($k$: số lần $A$ xảy ra; $n$: tổng số lần thử)). c) **Sai** vì $x \\in A$ ($x$ '
                        'thuộc $A$); $y \\notin A$ ($y$ không thuộc $A$) là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Xác suất thực nghiệm của sự kiện A**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 43: Xác suất thực nghiệm** để giải quyết tình huống sau: Bình '
                 'tung một đồng xu $40$ lần và thấy có $18$ lần xuất hiện mặt ngửa. Tính xác suất thực '
                 'nghiệm xuất hiện mặt ngửa và mặt sấp. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Xác suất thực nghiệm xuất hiện mặt ngửa là $\\dfrac{18}{40} = \\dfrac{9}{20} = '
                        '45\\%$. Mặt sấp xuất hiện $40 - 18 = 22$ lần nên xác suất thực nghiệm là '
                        '$\\dfrac{22}{40} = \\dfrac{11}{20} = 55\\%$...',
                        'Ta có $M = \\{\\text{T}, \\text{O}, \\text{A}, \\text{N}, \\text{H}, \\text{C}\\}$ '
                        '(chữ O xuất hiện $2$ lần nhưng chỉ viết $1$ lần). Tập hợp $M$ có $6$ phần tử.',
                        'Số $27$ viết là $\\text{XXVII}$, số $19$ viết là $\\text{XIX}$. Ta có '
                        '$\\overline{ab} = a \\times 10 + b$.',
                        'Các số tự nhiên từ $4$ đến $8$ là $4; 5; 6; 7; 8$. Vậy $A = \\{4; 5; 6; 7; 8\\}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 43: Xác suất thực nghiệm: Xác suất thực nghiệm xuất hiện '
                        'mặt ngửa là $\\dfrac{18}{40} = \\dfrac{9}{20} = 45\\%$. Mặt sấp xuất hiện $40 - 18 '
                        '= 22$ lần nên xác suất thực nghiệm là $\\dfrac{22}{40} = \\dfrac{11}{20} = 55\\%$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp có bóng đỏ và bóng xanh. Lấy ngẫu nhiên một quả bóng rồi trả lại vào hộp, lặp lại '
                 '$80$ lần thấy có $28$ lần lấy được bóng đỏ. Tính xác suất thực nghiệm của sự kiện “Không '
                 'lấy được bóng đỏ” dưới dạng phân số tối giản (viết dạng a/b).',
            'answer': ['13/20', '0,65', '0.65'],
            'unit': None,
            'solution': 'Số lần không lấy được bóng đỏ là $80 - 28 = 52$ (lần). Xác suất thực nghiệm là '
                        '$\\dfrac{52}{80} = \\dfrac{13}{20}$.',
            'alt': None,
            'note': None}]}]
