"""Dữ liệu bài học SGK Toán Lớp 5 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 5 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học độc lập (title).
Mỗi bài học chỉ chứa kiến thức, công thức, ví dụ và 10 câu hỏi của riêng bài học đó.
"""

GRADE = 5

LESSONS = [{'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 1: Ôn tập số tự nhiên',
  'icon': '🔁',
  'description': 'Ôn tập cách đọc, viết, so sánh số tự nhiên và bốn phép tính cộng, trừ, nhân, chia với số '
                 'tự nhiên.',
  'requirements': ['Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ số.',
                   'Thực hiện thành thạo bốn phép tính cộng, trừ, nhân, chia số tự nhiên và vận dụng tính '
                   'chất để tính hợp lí.',
                   'Vận dụng kiến thức của **Bài 1: Ôn tập số tự nhiên** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': '- Hệ thập phân sử dụng $10$ chữ số từ $0$ đến $9$; cứ $10$ đơn vị ở một hàng hợp thành $1$ '
                'đơn vị ở hàng liền trước nó.',
  'theory': '### 1. Cấu tạo thập phân và so sánh số tự nhiên\n'
            '- Lớp đơn vị (hàng đơn vị, chục, trăm), lớp nghìn (nghìn, chục nghìn, trăm nghìn), lớp triệu.\n'
            '- Số nào có nhiều chữ số hơn thì lớn hơn; nếu số chữ số bằng nhau thì so sánh từng cặp chữ số ở '
            'cùng một hàng kể từ trái sang phải.',
  'formulas': [{'category': 'Tính chất phép tính',
                'items': [{'name': 'Giao hoán và kết hợp',
                           'formula': '$a + b = b + a$; $(a + b) + c = a + (b + c)$'},
                          {'name': 'Nhân một số với một tổng',
                           'formula': '$a \\times (b + c) = a \\times b + a \\times c$'}]}],
  'example': 'Tính bằng cách thuận tiện nhất: $125 \\times 37 \\times 8$.',
  'example_answer': 'Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.',
  'real_life': 'Tính tổng tiền mua hàng, dân số các tỉnh thành và chia đều sản phẩm vào các thùng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số $458\\,209$, chữ số $8$ thuộc hàng nào?',
            'options': ['Hàng nghìn', 'Hàng trăm', 'Hàng chục nghìn', 'Hàng triệu'],
            'answer': 0,
            'solution': 'Chữ số $8$ đứng ở vị trí hàng nghìn nên có giá trị là $8000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $250 \\times 4$ là:',
            'options': ['$800$', '$1000$', '$1200$', '$900$'],
            'answer': 1,
            'solution': 'Ta có $250 \\times 4 = 1000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Ôn tập số tự nhiên**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Giao hoán và kết hợp**?',
            'options': ['$a - b = b + a$; $(a + b) + c = a + (b + c)$',
                        'Đảo ngược vế của quy tắc: $a + b = b + a$; $(a + b) + c = a + (b + c)$',
                        '$a + b = b + a$; $(a + b) + c = a + (b + c)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a + b = b + a$; $(a + b) + c = '
                        'a + (b + c)$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 1: Ôn tập số tự nhiên, **Giao hoán và kết hợp** '
                        'được xác định bởi: $a + b = b + a$; $(a + b) + c = a + (b + c)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Ôn tập số tự nhiên**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Nhân một số với một tổng**?',
            'options': ['$a \\times (b - c) = a \\times b + a \\times c$',
                        'Đảo ngược vế của quy tắc: $a \\times (b + c) = a \\times b + a \\times c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a \\times (b + c) = a \\times '
                        'b + a \\times c$',
                        '$a \\times (b + c) = a \\times b + a \\times c$'],
            'answer': 3,
            'solution': 'Trong Bài 1: Ôn tập số tự nhiên, **Nhân một số với một tổng** có công thức/quy tắc '
                        'là: $a \\times (b + c) = a \\times b + a \\times c$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $48 \\times 63 + 48 \\times 37$ là:',
            'options': ['$4800$', '$480$', '$3800$', '$48\\,000$'],
            'answer': 0,
            'solution': 'Áp dụng tính chất phân phối: $48 \\times (63 + 37) = 48 \\times 100 = 4800$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 1: Ôn tập số tự nhiên**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ '
                        'số. (với dấu ngược lại)',
                        'Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ '
                        'số.',
                        'Đảo ngược vế của quy tắc: Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của '
                        'các số tự nhiên nhiều chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đọc, viết, so sánh và xác định '
                        'giá trị theo hàng, lớp của các số tự nhiên nhiều chữ số.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 1: Ôn tập số tự nhiên: Đọc, viết, so sánh và xác định '
                        'giá trị theo hàng, lớp của các số tự nhiên nhiều chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong phép chia có số chia là $7$, số dư lớn nhất có thể là $6$.',
            'answer': True,
            'solution': 'Số dư luôn nhỏ hơn số chia ($0 \\le r < 7$) nên số dư lớn nhất là $6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 1: Ôn tập số tự nhiên**, quy tắc **Giao hoán và kết hợp** được xác định bởi $a '
                 '+ b = b + a$; $(a + b) + c = a + (b + c)$ và khi áp dụng cho ví dụ “Tính bằng cách thuận '
                 'tiện nhất: $125 \\times 37 \\times 8$.” ta có lời giải: Ta có $(125 \\times 8) \\times 37 '
                 '= 1000 \\times 37 = 37000$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Giao hoán và kết hợp** ($a + b = b + a$; '
                        '$(a + b) + c = a + (b + c)$) và lời giải ví dụ minh họa của Bài 1: Ôn tập số tự '
                        'nhiên.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 1: Ôn tập số tự nhiên** để giải bài toán sau: Tính '
                 'bằng cách thuận tiện nhất: $125 \\times 37 \\times 8$. Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $(125 : 8) \\times 37 = 1000 \\times 37 = 37000$.',
                        'Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 36999$.',
                        'Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.',
                        'Ta có $(127 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Ôn tập số tự nhiên: Ta có $(125 \\times 8) \\times 37 '
                        '= 1000 \\times 37 = 37000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một trường tiểu học có $840$ học sinh xếp đều thành $24$ hàng. Hỏi mỗi hàng có bao nhiêu '
                 'học sinh?',
            'answer': ['35'],
            'unit': None,
            'solution': 'Số học sinh mỗi hàng là $840 : 24 = 35$ (học sinh).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 2: Ôn tập các phép tính với số tự nhiên',
  'icon': '🔁',
  'description': 'Ôn tập cách đọc, viết, so sánh số tự nhiên và bốn phép tính cộng, trừ, nhân, chia với số '
                 'tự nhiên.',
  'requirements': ['Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ số.',
                   'Thực hiện thành thạo bốn phép tính cộng, trừ, nhân, chia số tự nhiên và vận dụng tính '
                   'chất để tính hợp lí.',
                   'Vận dụng kiến thức của **Bài 2: Ôn tập các phép tính với số tự nhiên** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '- Các phép tính cộng và nhân có tính chất giao hoán $a + b = b + a$, $a \\times b = b '
                '\\times a$, tính chất kết hợp và tính chất phân phối $a \\times (b + c) = a \\times b + a '
                '\\times c$.',
  'theory': '### 2. Bốn phép tính với số tự nhiên\n'
            '- Phép trừ $a - b = c$ là phép toán ngược của phép cộng ($a = b + c$, với $a \\ge b$).\n'
            '- Phép chia có dư: $a = b \\times q + r$ (với $0 \\le r < b$); khi $r = 0$ ta có phép chia hết '
            '$a : b = q$.',
  'formulas': [{'category': 'Tìm thành phần chưa biết',
                'items': [{'name': 'Số hạng và số trừ',
                           'formula': '$x + b = c \\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - '
                                      'c$'},
                          {'name': 'Phép chia có dư', 'formula': '$a = b \\times q + r$ ($0 \\le r < b$)'}]}],
  'example': 'Tính bằng cách thuận tiện nhất: $125 \\times 37 \\times 8$.',
  'example_answer': 'Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.',
  'real_life': 'Tính tổng tiền mua hàng, dân số các tỉnh thành và chia đều sản phẩm vào các thùng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số $458\\,209$, chữ số $8$ thuộc hàng nào?',
            'options': ['Hàng trăm', 'Hàng nghìn', 'Hàng chục nghìn', 'Hàng triệu'],
            'answer': 1,
            'solution': 'Chữ số $8$ đứng ở vị trí hàng nghìn nên có giá trị là $8000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $250 \\times 4$ là:',
            'options': ['$800$', '$1200$', '$1000$', '$900$'],
            'answer': 2,
            'solution': 'Ta có $250 \\times 4 = 1000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Ôn tập các phép tính với số tự nhiên**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Số hạng và số trừ**?',
            'options': ['$x - b = c \\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$',
                        'Đảo ngược vế của quy tắc: $x + b = c \\Rightarrow x = c - b$; $a - x = c '
                        '\\Rightarrow x = a - c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $x + b = c \\Rightarrow x = c - '
                        'b$; $a - x = c \\Rightarrow x = a - c$',
                        '$x + b = c \\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 2: Ôn tập các phép tính với số tự nhiên, **Số hạng '
                        'và số trừ** được xác định bởi: $x + b = c \\Rightarrow x = c - b$; $a - x = c '
                        '\\Rightarrow x = a - c$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Ôn tập các phép tính với số tự nhiên**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Phép chia có dư**?',
            'options': ['$a = b \\times q + r$ ($0 \\le r < b$)',
                        '$a = b \\times q + r$ ($0 \\ge r < b$)',
                        '$a = b \\times q + r$ ($1 \\le r < b$)',
                        '$a = b \\times q + r$ ($2 \\le r < b$)'],
            'answer': 0,
            'solution': 'Trong Bài 2: Ôn tập các phép tính với số tự nhiên, **Phép chia có dư** có công '
                        'thức/quy tắc là: $a = b \\times q + r$ ($0 \\le r < b$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $48 \\times 63 + 48 \\times 37$ là:',
            'options': ['$480$', '$4800$', '$3800$', '$48\\,000$'],
            'answer': 1,
            'solution': 'Áp dụng tính chất phân phối: $48 \\times (63 + 37) = 48 \\times 100 = 4800$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 2: Ôn tập các phép tính với số tự nhiên**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ '
                        'số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của '
                        'các số tự nhiên nhiều chữ số.',
                        'Đọc, viết, so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ '
                        'số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đọc, viết, so sánh và xác định '
                        'giá trị theo hàng, lớp của các số tự nhiên nhiều chữ số.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 2: Ôn tập các phép tính với số tự nhiên: Đọc, viết, '
                        'so sánh và xác định giá trị theo hàng, lớp của các số tự nhiên nhiều chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong phép chia có số chia là $7$, số dư lớn nhất có thể là $6$.',
            'answer': True,
            'solution': 'Số dư luôn nhỏ hơn số chia ($0 \\le r < 7$) nên số dư lớn nhất là $6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 2: Ôn tập các phép tính với số tự nhiên**, quy tắc **Số hạng và số trừ** được '
                 'xác định bởi $x + b = c \\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$ và khi '
                 'áp dụng cho ví dụ “Tính bằng cách thuận tiện nhất: $125 \\times 37 \\times 8$.” ta có lời '
                 'giải: Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số hạng và số trừ** ($x + b = c '
                        '\\Rightarrow x = c - b$; $a - x = c \\Rightarrow x = a - c$) và lời giải ví dụ minh '
                        'họa của Bài 2: Ôn tập các phép tính với số tự nhiên.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 2: Ôn tập các phép tính với số tự nhiên** để giải '
                 'bài toán sau: Tính bằng cách thuận tiện nhất: $125 \\times 37 \\times 8$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $(125 : 8) \\times 37 = 1000 \\times 37 = 37000$.',
                        'Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 36999$.',
                        'Ta có $(127 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.',
                        'Ta có $(125 \\times 8) \\times 37 = 1000 \\times 37 = 37000$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Ôn tập các phép tính với số tự nhiên: Ta có $(125 '
                        '\\times 8) \\times 37 = 1000 \\times 37 = 37000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một trường tiểu học có $840$ học sinh xếp đều thành $24$ hàng. Hỏi mỗi hàng có bao nhiêu '
                 'học sinh?',
            'answer': ['35'],
            'unit': None,
            'solution': 'Số học sinh mỗi hàng là $840 : 24 = 35$ (học sinh).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 3: Ôn tập phân số và cộng, trừ phân số',
  'icon': '🔁',
  'description': 'Củng cố khái niệm phân số, tính chất cơ bản của phân số, rút gọn, quy đồng, so sánh phân '
                 'số và nhân, chia phân số.',
  'requirements': ['Rút gọn được phân số về phân số tối giản và quy đồng mẫu số hai phân số.',
                   'So sánh được các phân số và thực hiện phép nhân, phép chia phân số.',
                   'Vận dụng kiến thức của **Bài 3: Ôn tập phân số và cộng, trừ phân số** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '- Phân số $\\dfrac{a}{b}$ gồm tử số $a$ và mẫu số $b$ ($b \\ne 0$).',
  'theory': '### 1. Rút gọn và so sánh phân số\n'
            '- Phân số tối giản là phân số không thể rút gọn được nữa, ví dụ $\\dfrac{12}{18} = '
            '\\dfrac{2}{3}$.\n'
            '- Hai phân số cùng mẫu số: phân số nào có tử số lớn hơn thì lớn hơn. Hai phân số cùng tử số: '
            'phân số nào có mẫu số bé hơn thì lớn hơn.',
  'formulas': [{'category': 'Tính chất cơ bản',
                'items': [{'name': 'Bằng nhau',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m} = \\dfrac{a : n}{b '
                                      ': n}$ ($m, n \\ne 0$)'},
                          {'name': 'Cộng, trừ cùng mẫu',
                           'formula': '$\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$'}]}],
  'example': 'Rút gọn rồi tính: $\\dfrac{15}{25} \\times \\dfrac{5}{6}$.',
  'example_answer': 'Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times \\dfrac{5}{6} = '
                    '\\dfrac{15}{30} = \\dfrac{1}{2}$.',
  'real_life': 'Chia bánh, chia phần diện tích đất canh tác và tính lượng nguyên liệu trong nấu ăn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Rút gọn phân số $\\dfrac{18}{24}$ đến tối giản ta được:',
            'options': ['$\\dfrac{9}{12}$', '$\\dfrac{6}{8}$', '$\\dfrac{3}{4}$', '$\\dfrac{2}{3}$'],
            'answer': 2,
            'solution': 'Chia cả tử và mẫu cho $6$: $\\dfrac{18 : 6}{24 : 6} = \\dfrac{3}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số đảo ngược của phân số $\\dfrac{4}{7}$ là:',
            'options': ['$\\dfrac{4}{7}$', '$\\dfrac{1}{7}$', '$\\dfrac{3}{7}$', '$\\dfrac{7}{4}$'],
            'answer': 3,
            'solution': 'Phân số đảo ngược của $\\dfrac{4}{7}$ là $\\dfrac{7}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Ôn tập phân số và cộng, trừ phân số**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Bằng nhau**?',
            'options': ['$\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m} = \\dfrac{a : n}{b : n}$ ($m, n '
                        '\\ne 0$)',
                        '$\\dfrac{a}{b} = \\dfrac{a : m}{b \\times m} = \\dfrac{a : n}{b : n}$ ($m, n \\ne '
                        '0$)',
                        '$\\dfrac{b}{a} = \\dfrac{a \\times m}{b \\times m} = \\dfrac{a : n}{b : n}$ ($m, n '
                        '\\ne 0$)',
                        '$\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m} = \\dfrac{a : n}{b : n}$ ($m, n '
                        '\\ne 2$)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 3: Ôn tập phân số và cộng, trừ phân số, **Bằng '
                        'nhau** được xác định bởi: $\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m} = '
                        '\\dfrac{a : n}{b : n}$ ($m, n \\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Ôn tập phân số và cộng, trừ phân số**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Cộng, trừ cùng mẫu**?',
            'options': ['$\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$ (với dấu ngược lại)',
                        '$\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$',
                        '$\\dfrac{m}{a} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{a}{m} \\pm '
                        '\\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$'],
            'answer': 1,
            'solution': 'Trong Bài 3: Ôn tập phân số và cộng, trừ phân số, **Cộng, trừ cùng mẫu** có công '
                        'thức/quy tắc là: $\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $\\dfrac{3}{5} : \\dfrac{9}{10}$ là:',
            'options': ['$\\dfrac{27}{50}$', '$\\dfrac{3}{2}$', '$\\dfrac{2}{3}$', '$\\dfrac{1}{2}$'],
            'answer': 2,
            'solution': 'Ta có $\\dfrac{3}{5} : \\dfrac{9}{10} = \\dfrac{3}{5} \\times \\dfrac{10}{9} = '
                        '\\dfrac{30}{45} = \\dfrac{2}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 3: Ôn tập phân số và cộng, trừ phân số**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Rút gọn được phân số về phân số tối giản và quy đồng mẫu số hai phân số. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Rút gọn được phân số về phân số tối giản và quy đồng mẫu '
                        'số hai phân số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Rút gọn được phân số về phân số '
                        'tối giản và quy đồng mẫu số hai phân số.',
                        'Rút gọn được phân số về phân số tối giản và quy đồng mẫu số hai phân số.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 3: Ôn tập phân số và cộng, trừ phân số: Rút gọn được '
                        'phân số về phân số tối giản và quy đồng mẫu số hai phân số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $\\dfrac{5}{7} > \\dfrac{5}{9}$ vì hai phân số cùng tử số dương, phân số nào có mẫu '
                 'số bé hơn thì lớn hơn.',
            'answer': True,
            'solution': 'Cùng tử số $5$, vì $7 < 9$ nên $\\dfrac{5}{7} > \\dfrac{5}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 3: Ôn tập phân số và cộng, trừ phân số**, quy tắc **Bằng nhau** được xác định '
                 'bởi $\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m} = \\dfrac{a : n}{b : n}$ ($m, n '
                 '\\ne 0$) và khi áp dụng cho ví dụ “Rút gọn rồi tính: $\\dfrac{15}{25} \\times '
                 '\\dfrac{5}{6}$.” ta có lời giải: Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó '
                 '$\\dfrac{3}{5} \\times \\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Bằng nhau** ($\\dfrac{a}{b} = \\dfrac{a '
                        '\\times m}{b \\times m} = \\dfrac{a : n}{b : n}$ ($m, n \\ne 0$)) và lời giải ví dụ '
                        'minh họa của Bài 3: Ôn tập phân số và cộng, trừ phân số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 3: Ôn tập phân số và cộng, trừ phân số** để giải '
                 'bài toán sau: Rút gọn rồi tính: $\\dfrac{15}{25} \\times \\dfrac{5}{6}$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times '
                        '\\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.',
                        'Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} : \\dfrac{5}{6} = '
                        '\\dfrac{15}{30} = \\dfrac{1}{2}$.',
                        'Ta có $\\dfrac{25}{15} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times '
                        '\\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.',
                        'Ta có $\\dfrac{30}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times '
                        '\\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Ôn tập phân số và cộng, trừ phân số: Ta có '
                        '$\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times \\dfrac{5}{6} = '
                        '\\dfrac{15}{30} = \\dfrac{1}{2}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chữ nhật có chiều dài $\\dfrac{4}{5}\\text{ m}$ và chiều rộng '
                 '$\\dfrac{3}{4}\\text{ m}$. Tính diện tích hình chữ nhật đó dưới dạng phân số tối giản '
                 '(viết dạng a/b).',
            'answer': ['3/5'],
            'unit': None,
            'solution': 'Diện tích hình chữ nhật là $\\dfrac{4}{5} \\times \\dfrac{3}{4} = \\dfrac{3}{5}$ '
                        '($\\text{m}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 5: Ôn tập phép nhân, phép chia phân số',
  'icon': '🔁',
  'description': 'Củng cố khái niệm phân số, tính chất cơ bản của phân số, rút gọn, quy đồng, so sánh phân '
                 'số và nhân, chia phân số.',
  'requirements': ['Rút gọn được phân số về phân số tối giản và quy đồng mẫu số hai phân số.',
                   'So sánh được các phân số và thực hiện phép nhân, phép chia phân số.',
                   'Vận dụng kiến thức của **Bài 5: Ôn tập phép nhân, phép chia phân số** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '- Nhân hoặc chia cả tử số và mẫu số của một phân số với cùng một số tự nhiên khác $0$ thì '
                'được phân số mới bằng phân số đã cho.',
  'theory': '### 2. Nhân và chia phân số\n'
            '- Muốn nhân hai phân số, ta lấy tử số nhân với tử số, mẫu số nhân với mẫu số: $\\dfrac{a}{b} '
            '\\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$.\n'
            '- Muốn chia một phân số cho một phân số khác $0$, ta lấy phân số thứ nhất nhân với phân số đảo '
            'ngược của phân số thứ hai.',
  'formulas': [{'category': 'Nhân, chia phân số',
                'items': [{'name': 'Phép nhân',
                           'formula': '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times '
                                      'd}$'},
                          {'name': 'Phép chia',
                           'formula': '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$ '
                                      '($c \\ne 0$)'}]}],
  'example': 'Rút gọn rồi tính: $\\dfrac{15}{25} \\times \\dfrac{5}{6}$.',
  'example_answer': 'Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times \\dfrac{5}{6} = '
                    '\\dfrac{15}{30} = \\dfrac{1}{2}$.',
  'real_life': 'Chia bánh, chia phần diện tích đất canh tác và tính lượng nguyên liệu trong nấu ăn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Rút gọn phân số $\\dfrac{18}{24}$ đến tối giản ta được:',
            'options': ['$\\dfrac{9}{12}$', '$\\dfrac{6}{8}$', '$\\dfrac{2}{3}$', '$\\dfrac{3}{4}$'],
            'answer': 3,
            'solution': 'Chia cả tử và mẫu cho $6$: $\\dfrac{18 : 6}{24 : 6} = \\dfrac{3}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số đảo ngược của phân số $\\dfrac{4}{7}$ là:',
            'options': ['$\\dfrac{7}{4}$', '$\\dfrac{4}{7}$', '$\\dfrac{1}{7}$', '$\\dfrac{3}{7}$'],
            'answer': 0,
            'solution': 'Phân số đảo ngược của $\\dfrac{4}{7}$ là $\\dfrac{7}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Ôn tập phép nhân, phép chia phân số**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Phép nhân**?',
            'options': ['$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$',
                        '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$',
                        '$\\dfrac{b}{a} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{a}{b} \\times '
                        '\\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 5: Ôn tập phép nhân, phép chia phân số, **Phép '
                        'nhân** được xác định bởi: $\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times '
                        'c}{b \\times d}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Ôn tập phép nhân, phép chia phân số**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Phép chia**?',
            'options': ['$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} : \\dfrac{d}{c}$ ($c \\ne 0$)',
                        '$\\dfrac{b}{a} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$ ($c \\ne 0$)',
                        '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$ ($c \\ne 0$)',
                        '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$ ($c \\ne 2$)'],
            'answer': 2,
            'solution': 'Trong Bài 5: Ôn tập phép nhân, phép chia phân số, **Phép chia** có công thức/quy '
                        'tắc là: $\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$ ($c '
                        '\\ne 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $\\dfrac{3}{5} : \\dfrac{9}{10}$ là:',
            'options': ['$\\dfrac{27}{50}$', '$\\dfrac{3}{2}$', '$\\dfrac{1}{2}$', '$\\dfrac{2}{3}$'],
            'answer': 3,
            'solution': 'Ta có $\\dfrac{3}{5} : \\dfrac{9}{10} = \\dfrac{3}{5} \\times \\dfrac{10}{9} = '
                        '\\dfrac{30}{45} = \\dfrac{2}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 5: Ôn tập phép nhân, phép chia phân số**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Rút gọn được phân số về phân số tối giản và quy đồng mẫu số hai phân số.',
                        'Rút gọn được phân số về phân số tối giản và quy đồng mẫu số hai phân số. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Rút gọn được phân số về phân số tối giản và quy đồng mẫu '
                        'số hai phân số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Rút gọn được phân số về phân số '
                        'tối giản và quy đồng mẫu số hai phân số.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 5: Ôn tập phép nhân, phép chia phân số: Rút gọn được '
                        'phân số về phân số tối giản và quy đồng mẫu số hai phân số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $\\dfrac{5}{7} > \\dfrac{5}{9}$ vì hai phân số cùng tử số dương, phân số nào có mẫu '
                 'số bé hơn thì lớn hơn.',
            'answer': True,
            'solution': 'Cùng tử số $5$, vì $7 < 9$ nên $\\dfrac{5}{7} > \\dfrac{5}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 5: Ôn tập phép nhân, phép chia phân số**, quy tắc **Phép nhân** được xác định '
                 'bởi $\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$ và khi áp '
                 'dụng cho ví dụ “Rút gọn rồi tính: $\\dfrac{15}{25} \\times \\dfrac{5}{6}$.” ta có lời '
                 'giải: Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times \\dfrac{5}{6} '
                 '= \\dfrac{15}{30} = \\dfrac{1}{2}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Phép nhân** ($\\dfrac{a}{b} \\times '
                        '\\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$) và lời giải ví dụ minh họa của '
                        'Bài 5: Ôn tập phép nhân, phép chia phân số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 5: Ôn tập phép nhân, phép chia phân số** để giải '
                 'bài toán sau: Rút gọn rồi tính: $\\dfrac{15}{25} \\times \\dfrac{5}{6}$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} : \\dfrac{5}{6} = '
                        '\\dfrac{15}{30} = \\dfrac{1}{2}$.',
                        'Ta có $\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times '
                        '\\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.',
                        'Ta có $\\dfrac{25}{15} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times '
                        '\\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.',
                        'Ta có $\\dfrac{30}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times '
                        '\\dfrac{5}{6} = \\dfrac{15}{30} = \\dfrac{1}{2}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 5: Ôn tập phép nhân, phép chia phân số: Ta có '
                        '$\\dfrac{15}{25} = \\dfrac{3}{5}$. Khi đó $\\dfrac{3}{5} \\times \\dfrac{5}{6} = '
                        '\\dfrac{15}{30} = \\dfrac{1}{2}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chữ nhật có chiều dài $\\dfrac{4}{5}\\text{ m}$ và chiều rộng '
                 '$\\dfrac{3}{4}\\text{ m}$. Tính diện tích hình chữ nhật đó dưới dạng phân số tối giản '
                 '(viết dạng a/b).',
            'answer': ['3/5'],
            'unit': None,
            'solution': 'Diện tích hình chữ nhật là $\\dfrac{4}{5} \\times \\dfrac{3}{4} = \\dfrac{3}{5}$ '
                        '($\\text{m}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 4: Phân số thập phân',
  'icon': '🔁',
  'description': 'Nhận biết phân số thập phân và cách chuyển đổi một số phân số thành phân số thập phân.',
  'requirements': ['Nhận biết được các phân số thập phân có mẫu số là $10; 100; 1000; \\dots$',
                   'Viết được một số phân số về dạng phân số thập phân bằng cách nhân hoặc chia cả tử và mẫu '
                   'với cùng một số.',
                   'Vận dụng kiến thức của **Bài 4: Phân số thập phân** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': '- **Phân số thập phân** là các phân số có mẫu số là $10; 100; 1000; \\dots$ (ví dụ '
                '$\\dfrac{3}{10}$, $\\dfrac{47}{100}$, $\\dfrac{125}{1000}$).\n'
                '- Một số phân số có thể viết thành phân số thập phân bằng cách tìm một số thích hợp để nhân '
                '(hoặc chia) cả tử số và mẫu số để được mẫu số là $10; 100; 1000; \\dots$',
  'theory': '### 1. Nhận diện phân số thập phân\n'
            '- Các phân số như $\\dfrac{7}{10}$, $\\dfrac{23}{100}$, $\\dfrac{9}{1000}$ là phân số thập '
            'phân.\n'
            '### 2. Chuyển phân số thành phân số thập phân\n'
            '- Nhân cả tử và mẫu: $\\dfrac{3}{5} = \\dfrac{3 \\times 2}{5 \\times 2} = \\dfrac{6}{10}$; '
            '$\\dfrac{7}{20} = \\dfrac{7 \\times 5}{20 \\times 5} = \\dfrac{35}{100}$; $\\dfrac{9}{25} = '
            '\\dfrac{9 \\times 4}{25 \\times 4} = \\dfrac{36}{100}$.\n'
            '- Rút gọn: $\\dfrac{18}{200} = \\dfrac{18 : 2}{200 : 2} = \\dfrac{9}{100}$.',
  'formulas': [{'category': 'Phân số thập phân',
                'items': [{'name': 'Dạng tổng quát',
                           'formula': '$\\dfrac{a}{10}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$'},
                          {'name': 'Các tích mẫu số cần nhớ',
                           'formula': '$2 \\times 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 1000$'}]}],
  'example': 'Viết các phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{8}$ thành phân số thập phân.',
  'example_answer': 'Ta có $\\dfrac{3}{4} = \\dfrac{3 \\times 25}{4 \\times 25} = \\dfrac{75}{100}$ và '
                    '$\\dfrac{5}{8} = \\dfrac{5 \\times 125}{8 \\times 125} = \\dfrac{625}{1000}$.',
  'real_life': 'Biểu diễn số đo độ dài ($\\text{dm}, \\text{cm}, \\text{mm}$ so với $\\text{m}$) và làm nền '
               'tảng để viết số thập phân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số nào dưới đây là phân số thập phân?',
            'options': ['$\\dfrac{9}{100}$', '$\\dfrac{3}{7}$', '$\\dfrac{5}{12}$', '$\\dfrac{10}{3}$'],
            'answer': 0,
            'solution': 'Phân số $\\dfrac{9}{100}$ có mẫu số là $100$ nên là phân số thập phân.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Viết phân số $\\dfrac{3}{4}$ thành phân số thập phân có mẫu số là $100$:',
            'options': ['$\\dfrac{34}{100}$',
                        '$\\dfrac{75}{100}$',
                        '$\\dfrac{25}{100}$',
                        '$\\dfrac{30}{100}$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{3}{4} = \\dfrac{3 \\times 25}{4 \\times 25} = \\dfrac{75}{100}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Phân số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Dạng tổng quát**?',
            'options': ['$\\dfrac{a}{11}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$',
                        '$\\dfrac{10}{a}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$',
                        '$\\dfrac{a}{10}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$',
                        '$\\dfrac{a}{20}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 4: Phân số thập phân, **Dạng tổng quát** được xác '
                        'định bởi: $\\dfrac{a}{10}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Phân số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Các tích mẫu số cần nhớ**?',
            'options': ['$2 : 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 1000$',
                        '$2 \\times 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 999$',
                        '$4 \\times 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 1000$',
                        '$2 \\times 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 1000$'],
            'answer': 3,
            'solution': 'Trong Bài 4: Phân số thập phân, **Các tích mẫu số cần nhớ** có công thức/quy tắc '
                        'là: $2 \\times 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 1000$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phân số $\\dfrac{7}{25}$ viết dưới dạng phân số thập phân là:',
            'options': ['$\\dfrac{28}{100}$',
                        '$\\dfrac{14}{100}$',
                        '$\\dfrac{35}{100}$',
                        '$\\dfrac{70}{100}$'],
            'answer': 0,
            'solution': 'Nhân cả tử và mẫu với $4$: $\\dfrac{7 \\times 4}{25 \\times 4} = \\dfrac{28}{100}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 4: Phân số thập phân**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được các phân số thập phân có mẫu số là $11; 100; 1000; \\dots$',
                        'Nhận biết được các phân số thập phân có mẫu số là $10; 100; 1000; \\dots$',
                        'Nhận biết được các phân số thập phân có mẫu số là $10; 100; 999; \\dots$',
                        'Nhận biết được các phân số thập phân có mẫu số là $20; 100; 1000; \\dots$'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 4: Phân số thập phân: Nhận biết được các phân số thập '
                        'phân có mẫu số là $10; 100; 1000; \\dots$'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Phân số $\\dfrac{15}{300}$ khi rút gọn cho $3$ sẽ trở thành phân số thập phân '
                 '$\\dfrac{5}{100}$.',
            'answer': True,
            'solution': 'Ta có $\\dfrac{15 : 3}{300 : 3} = \\dfrac{5}{100}$ là phân số thập phân.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 4: Phân số thập phân**, quy tắc **Dạng tổng quát** được xác định bởi '
                 '$\\dfrac{a}{10}, \\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$ và khi áp dụng cho ví dụ “Viết '
                 'các phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{8}$ thành phân số thập phân.” ta có lời giải: '
                 'Ta có $\\dfrac{3}{4} = \\dfrac{3 \\times 25}{4 \\times 25} = \\dfrac{75}{100}$ và '
                 '$\\dfrac{5}{8} = \\dfrac{5 \\times 125}{8 \\times 125} = \\dfrac{625}{1000}$.... Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Dạng tổng quát** ($\\dfrac{a}{10}, '
                        '\\dfrac{a}{100}, \\dfrac{a}{1000}, \\dots$) và lời giải ví dụ minh họa của Bài 4: '
                        'Phân số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 4: Phân số thập phân** để giải bài toán sau: Viết '
                 'các phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{8}$ thành phân số thập phân. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\dfrac{3}{4} = \\dfrac{3 : 25}{4 \\times 25} = \\dfrac{75}{100}$ và '
                        '$\\dfrac{5}{8} = \\dfrac{5 \\times 125}{8 \\times 125} = \\dfrac{625}{1000}$.',
                        'Ta có $\\dfrac{4}{3} = \\dfrac{3 \\times 25}{4 \\times 25} = \\dfrac{75}{100}$ và '
                        '$\\dfrac{5}{8} = \\dfrac{5 \\times 125}{8 \\times 125} = \\dfrac{625}{1000}$.',
                        'Ta có $\\dfrac{3}{4} = \\dfrac{3 \\times 25}{4 \\times 25} = \\dfrac{75}{100}$ và '
                        '$\\dfrac{5}{8} = \\dfrac{5 \\times 125}{8 \\times 125} = \\dfrac{625}{1000}$.',
                        'Ta có $\\dfrac{6}{4} = \\dfrac{3 \\times 25}{4 \\times 25} = \\dfrac{75}{100}$ và '
                        '$\\dfrac{5}{8} = \\dfrac{5 \\times 125}{8 \\times 125} = \\dfrac{625}{1000}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 4: Phân số thập phân: Ta có $\\dfrac{3}{4} = \\dfrac{3 '
                        '\\times 25}{4 \\times 25} = \\dfrac{75}{100}$ và $\\dfrac{5}{8} = \\dfrac{5 \\times '
                        '125}{8 \\times 125} = \\dfrac{625}{1000}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Khi viết phân số $\\dfrac{3}{8}$ thành phân số thập phân có mẫu số là $1000$, tử số của '
                 'phân số thập phân đó bằng bao nhiêu?',
            'answer': ['375'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{3}{8} = \\dfrac{3 \\times 125}{8 \\times 125} = \\dfrac{375}{1000}$, '
                        'vậy tử số là $375$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 6: Cộng, trừ hai phân số khác mẫu số',
  'icon': '🔁',
  'description': 'Quy tắc cộng, trừ hai phân số khác mẫu số; nhận biết hỗn số và cách chuyển đổi giữa hỗn số '
                 'với phân số.',
  'requirements': ['Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu số.',
                   'Đọc, viết được hỗn số và chuyển đổi thành thạo hỗn số thành phân số để thực hiện phép '
                   'tính.',
                   'Vận dụng kiến thức của **Bài 6: Cộng, trừ hai phân số khác mẫu số** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': '- Muốn cộng (hoặc trừ) hai phân số khác mẫu số, ta **quy đồng mẫu số** hai phân số đó rồi '
                'cộng (hoặc trừ) hai phân số cùng mẫu.',
  'theory': '### 1. Cộng, trừ hai phân số khác mẫu số\n'
            '- Ví dụ: $\\dfrac{2}{3} + \\dfrac{3}{4} = \\dfrac{8}{12} + \\dfrac{9}{12} = \\dfrac{17}{12}$; '
            '$\\dfrac{3}{5} - \\dfrac{1}{4} = \\dfrac{12}{20} - \\dfrac{5}{20} = \\dfrac{7}{20}$.\n'
            '### 2. Hỗn số',
  'formulas': [{'category': 'Cộng, trừ khác mẫu',
                'items': [{'name': 'Quy tắc chung',
                           'formula': '$\\dfrac{a}{b} \\pm \\dfrac{c}{d} = \\dfrac{a \\times d \\pm c '
                                      '\\times b}{b \\times d}$'}]}],
  'example': 'Tính: $1\\dfrac{1}{2} + 2\\dfrac{2}{3}$.',
  'example_answer': 'Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                    '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + \\dfrac{16}{6} '
                    '= \\dfrac{25}{6} = 4\\dfrac{1}{6}$.',
  'real_life': 'Đong $1\\dfrac{1}{2}$ cốc bột khi làm bánh hoặc đo $2\\dfrac{3}{4}\\text{ m}$ vải may áo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Viết hỗn số $2\\dfrac{1}{3}$ thành phân số ta được:',
            'options': ['$\\dfrac{3}{3}$', '$\\dfrac{7}{3}$', '$\\dfrac{5}{3}$', '$\\dfrac{2}{3}$'],
            'answer': 1,
            'solution': 'Ta có $2\\dfrac{1}{3} = \\dfrac{2 \\times 3 + 1}{3} = \\dfrac{7}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $\\dfrac{1}{2} + \\dfrac{1}{3}$ là:',
            'options': ['$\\dfrac{2}{5}$', '$\\dfrac{1}{5}$', '$\\dfrac{5}{6}$', '$\\dfrac{2}{6}$'],
            'answer': 2,
            'solution': 'Quy đồng mẫu số $6$: $\\dfrac{3}{6} + \\dfrac{2}{6} = \\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Cộng, trừ hai phân số khác mẫu số**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Quy tắc chung**?',
            'options': ['$\\dfrac{a}{b} \\pm \\dfrac{c}{d} = \\dfrac{a : d \\pm c \\times b}{b \\times d}$',
                        '$\\dfrac{b}{a} \\pm \\dfrac{c}{d} = \\dfrac{a \\times d \\pm c \\times b}{b \\times '
                        'd}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{a}{b} \\pm '
                        '\\dfrac{c}{d} = \\dfrac{a \\times d \\pm c \\times b}{b \\times d}$',
                        '$\\dfrac{a}{b} \\pm \\dfrac{c}{d} = \\dfrac{a \\times d \\pm c \\times b}{b \\times '
                        'd}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 6: Cộng, trừ hai phân số khác mẫu số, **Quy tắc '
                        'chung** được xác định bởi: $\\dfrac{a}{b} \\pm \\dfrac{c}{d} = \\dfrac{a \\times d '
                        '\\pm c \\times b}{b \\times d}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo định nghĩa trong **Bài 6: Cộng, trừ hai phân số khác mẫu số**, khẳng định nào dưới '
                 'đây là **đúng**?',
            'options': ['Muốn cộng (hoặc trừ) hai phân số khác mẫu số, ta **quy đồng mẫu số** hai phân số đó '
                        'rồi cộng (hoặc trừ) hai phân số cùng mẫu.',
                        'Muốn cộng (hoặc trừ) hai phân số khác mẫu số, ta **quy đồng mẫu số** hai phân số đó '
                        'rồi cộng (hoặc trừ) hai phân số cùng mẫu. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Muốn cộng (hoặc trừ) hai phân số khác mẫu số, ta **quy '
                        'đồng mẫu số** hai phân số đó rồi cộng (hoặc trừ) hai phân số cùng mẫu.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Muốn cộng (hoặc trừ) hai phân '
                        'số khác mẫu số, ta **quy đồng mẫu số** hai phân số đó rồi cộng (hoặc trừ) hai phân '
                        'số cùng mẫu.'],
            'answer': 0,
            'solution': 'Theo định nghĩa của Bài 6: Cộng, trừ hai phân số khác mẫu số: Muốn cộng (hoặc trừ) '
                        'hai phân số khác mẫu số, ta **quy đồng mẫu số** hai phân số đó rồi cộng (hoặc trừ) '
                        'hai phân số cùng mẫu.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Viết phân số $\\dfrac{23}{6}$ dưới dạng hỗn số ta được:',
            'options': ['$3\\dfrac{1}{6}$', '$3\\dfrac{5}{6}$', '$2\\dfrac{5}{6}$', '$4\\dfrac{1}{6}$'],
            'answer': 1,
            'solution': 'Ta có $23 : 6 = 3$ dư $5$ nên $\\dfrac{23}{6} = 3\\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 6: Cộng, trừ hai phân số khác mẫu số**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu '
                        'số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép cộng, phép trừ hai phân số khác mẫu '
                        'số bằng cách quy đồng mẫu số.',
                        'Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu '
                        'số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép cộng, phép '
                        'trừ hai phân số khác mẫu số bằng cách quy đồng mẫu số.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 6: Cộng, trừ hai phân số khác mẫu số: Thực hiện được '
                        'phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Kết quả của phép trừ $\\dfrac{4}{5} - \\dfrac{1}{3}$ bằng $\\dfrac{7}{15}$.',
            'answer': True,
            'solution': 'Quy đồng mẫu số $15$: $\\dfrac{12}{15} - \\dfrac{5}{15} = \\dfrac{7}{15}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 6: Cộng, trừ hai phân số khác mẫu số**, quy tắc **Quy tắc chung** được xác '
                 'định bởi $\\dfrac{a}{b} \\pm \\dfrac{c}{d} = \\dfrac{a \\times d \\pm c \\times b}{b '
                 '\\times d}$ và khi áp dụng cho ví dụ “Tính: $1\\dfrac{1}{2} + 2\\dfrac{2}{3}$.” ta có lời '
                 'giải: Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                 '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + \\dfrac{16}{6} = '
                 '\\dfrac{25}{6} = 4\\dfrac{1}{6}$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quy tắc chung** ($\\dfrac{a}{b} \\pm '
                        '\\dfrac{c}{d} = \\dfrac{a \\times d \\pm c \\times b}{b \\times d}$) và lời giải ví '
                        'dụ minh họa của Bài 6: Cộng, trừ hai phân số khác mẫu số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 6: Cộng, trừ hai phân số khác mẫu số** để giải bài '
                 'toán sau: Tính: $1\\dfrac{1}{2} + 2\\dfrac{2}{3}$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} - \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...',
                        'Đổi thành phân số: $1\\dfrac{2}{1} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...',
                        'Đổi thành phân số: $2\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...',
                        'Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Cộng, trừ hai phân số khác mẫu số: Đổi thành phân số: '
                        '$1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = \\dfrac{8}{3}$. Khi đó '
                        '$\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + \\dfrac{16}{6} = \\dfrac{25}{6} = '
                        '4\\dfrac{1}{6}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bể nước có vòi A chảy $1$ giờ được $\\dfrac{1}{4}$ bể, vòi B chảy $1$ giờ được '
                 '$\\dfrac{1}{6}$ bể. Cả hai vòi cùng chảy trong $1$ giờ được bao nhiêu phần bể? (viết dạng '
                 'a/b)',
            'answer': ['5/12'],
            'unit': None,
            'solution': 'Trong $1$ giờ cả hai vòi chảy được $\\dfrac{1}{4} + \\dfrac{1}{6} = \\dfrac{3}{12} '
                        '+ \\dfrac{2}{12} = \\dfrac{5}{12}$ (bể).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'Chủ đề 1 · SGK Toán 5: Ôn tập số tự nhiên, phân số, phân số thập phân và hỗn số.',
  'title': 'Bài 7: Hỗn số',
  'icon': '🔁',
  'description': 'Quy tắc cộng, trừ hai phân số khác mẫu số; nhận biết hỗn số và cách chuyển đổi giữa hỗn số '
                 'với phân số.',
  'requirements': ['Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu số.',
                   'Đọc, viết được hỗn số và chuyển đổi thành thạo hỗn số thành phân số để thực hiện phép '
                   'tính.',
                   'Vận dụng kiến thức của **Bài 7: Hỗn số** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': '- **Hỗn số** $a\\dfrac{b}{c}$ gồm phần nguyên $a$ và phần phân số $\\dfrac{b}{c}$ (với '
                '$\\dfrac{b}{c} < 1$). Ta có $a\\dfrac{b}{c} = \\dfrac{a \\times c + b}{c}$.',
  'theory': '- Hỗn số $2\\dfrac{3}{4}$ đọc là “hai và ba phần tư”, có phần nguyên là $2$, phần phân số là '
            '$\\dfrac{3}{4} < 1$.\n'
            '- Chuyển hỗn số thành phân số: $2\\dfrac{3}{4} = \\dfrac{2 \\times 4 + 3}{4} = '
            '\\dfrac{11}{4}$.\n'
            '- Chuyển phân số lớn hơn $1$ thành hỗn số: $\\dfrac{13}{5} = 2\\dfrac{3}{5}$ (vì $13 : 5 = 2$ '
            'dư $3$).',
  'formulas': [{'category': 'Hỗn số',
                'items': [{'name': 'Hỗn số sang phân số',
                           'formula': '$a\\dfrac{b}{c} = \\dfrac{a \\times c + b}{c}$ ($b < c$)'},
                          {'name': 'Phân số sang hỗn số',
                           'formula': 'Lấy tử chia mẫu: thương là phần nguyên, số dư là tử số phần phân '
                                      'số'}]}],
  'example': 'Tính: $1\\dfrac{1}{2} + 2\\dfrac{2}{3}$.',
  'example_answer': 'Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                    '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + \\dfrac{16}{6} '
                    '= \\dfrac{25}{6} = 4\\dfrac{1}{6}$.',
  'real_life': 'Đong $1\\dfrac{1}{2}$ cốc bột khi làm bánh hoặc đo $2\\dfrac{3}{4}\\text{ m}$ vải may áo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Viết hỗn số $2\\dfrac{1}{3}$ thành phân số ta được:',
            'options': ['$\\dfrac{3}{3}$', '$\\dfrac{5}{3}$', '$\\dfrac{7}{3}$', '$\\dfrac{2}{3}$'],
            'answer': 2,
            'solution': 'Ta có $2\\dfrac{1}{3} = \\dfrac{2 \\times 3 + 1}{3} = \\dfrac{7}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $\\dfrac{1}{2} + \\dfrac{1}{3}$ là:',
            'options': ['$\\dfrac{2}{5}$', '$\\dfrac{1}{5}$', '$\\dfrac{2}{6}$', '$\\dfrac{5}{6}$'],
            'answer': 3,
            'solution': 'Quy đồng mẫu số $6$: $\\dfrac{3}{6} + \\dfrac{2}{6} = \\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Hỗn số**, quy tắc hoặc công thức nào sau đây xác định đúng **Hỗn số sang '
                 'phân số**?',
            'options': ['$a\\dfrac{b}{c} = \\dfrac{a \\times c + b}{c}$ ($b < c$)',
                        '$a\\dfrac{b}{c} = \\dfrac{a \\times c - b}{c}$ ($b < c$)',
                        '$a\\dfrac{c}{b} = \\dfrac{a \\times c + b}{c}$ ($b < c$)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a\\dfrac{b}{c} = \\dfrac{a '
                        '\\times c + b}{c}$ ($b < c$)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 7: Hỗn số, **Hỗn số sang phân số** được xác định '
                        'bởi: $a\\dfrac{b}{c} = \\dfrac{a \\times c + b}{c}$ ($b < c$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Hỗn số**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Phân số '
                 'sang hỗn số**?',
            'options': ['Lấy tử chia mẫu: thương là phần nguyên, số dư là tử số phần phân số (với dấu ngược '
                        'lại)',
                        'Lấy tử chia mẫu: thương là phần nguyên, số dư là tử số phần phân số',
                        'Đảo ngược vế của quy tắc: Lấy tử chia mẫu: thương là phần nguyên, số dư là tử số '
                        'phần phân số',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Lấy tử chia mẫu: thương là phần '
                        'nguyên, số dư là tử số phần phân số'],
            'answer': 1,
            'solution': 'Trong Bài 7: Hỗn số, **Phân số sang hỗn số** có công thức/quy tắc là: Lấy tử chia '
                        'mẫu: thương là phần nguyên, số dư là tử số phần phân số.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Viết phân số $\\dfrac{23}{6}$ dưới dạng hỗn số ta được:',
            'options': ['$3\\dfrac{1}{6}$', '$2\\dfrac{5}{6}$', '$3\\dfrac{5}{6}$', '$4\\dfrac{1}{6}$'],
            'answer': 2,
            'solution': 'Ta có $23 : 6 = 3$ dư $5$ nên $\\dfrac{23}{6} = 3\\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 7: Hỗn số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu '
                        'số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép cộng, phép trừ hai phân số khác mẫu '
                        'số bằng cách quy đồng mẫu số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép cộng, phép '
                        'trừ hai phân số khác mẫu số bằng cách quy đồng mẫu số.',
                        'Thực hiện được phép cộng, phép trừ hai phân số khác mẫu số bằng cách quy đồng mẫu '
                        'số.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 7: Hỗn số: Thực hiện được phép cộng, phép trừ hai '
                        'phân số khác mẫu số bằng cách quy đồng mẫu số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Kết quả của phép trừ $\\dfrac{4}{5} - \\dfrac{1}{3}$ bằng $\\dfrac{7}{15}$.',
            'answer': True,
            'solution': 'Quy đồng mẫu số $15$: $\\dfrac{12}{15} - \\dfrac{5}{15} = \\dfrac{7}{15}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 7: Hỗn số**, quy tắc **Hỗn số sang phân số** được xác định bởi $a\\dfrac{b}{c} '
                 '= \\dfrac{a \\times c + b}{c}$ ($b < c$) và khi áp dụng cho ví dụ “Tính: $1\\dfrac{1}{2} + '
                 '2\\dfrac{2}{3}$.” ta có lời giải: Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và '
                 '$2\\dfrac{2}{3} = \\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                 '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hỗn số sang phân số** ($a\\dfrac{b}{c} = '
                        '\\dfrac{a \\times c + b}{c}$ ($b < c$)) và lời giải ví dụ minh họa của Bài 7: Hỗn '
                        'số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 7: Hỗn số** để giải bài toán sau: Tính: '
                 '$1\\dfrac{1}{2} + 2\\dfrac{2}{3}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...',
                        'Đổi thành phân số: $1\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} - \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...',
                        'Đổi thành phân số: $1\\dfrac{2}{1} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...',
                        'Đổi thành phân số: $2\\dfrac{1}{2} = \\dfrac{3}{2}$ và $2\\dfrac{2}{3} = '
                        '\\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + \\dfrac{8}{3} = \\dfrac{9}{6} + '
                        '\\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Hỗn số: Đổi thành phân số: $1\\dfrac{1}{2} = '
                        '\\dfrac{3}{2}$ và $2\\dfrac{2}{3} = \\dfrac{8}{3}$. Khi đó $\\dfrac{3}{2} + '
                        '\\dfrac{8}{3} = \\dfrac{9}{6} + \\dfrac{16}{6} = \\dfrac{25}{6} = 4\\dfrac{1}{6}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bể nước có vòi A chảy $1$ giờ được $\\dfrac{1}{4}$ bể, vòi B chảy $1$ giờ được '
                 '$\\dfrac{1}{6}$ bể. Cả hai vòi cùng chảy trong $1$ giờ được bao nhiêu phần bể? (viết dạng '
                 'a/b)',
            'answer': ['5/12'],
            'unit': None,
            'solution': 'Trong $1$ giờ cả hai vòi chảy được $\\dfrac{1}{4} + \\dfrac{1}{6} = \\dfrac{3}{12} '
                        '+ \\dfrac{2}{12} = \\dfrac{5}{12}$ (bể).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd02-so-thap-phan',
  'context_title': 'Chủ đề 2: Số thập phân',
  'context': 'Chủ đề 2 · SGK Toán 5: Khái niệm, so sánh, đổi đơn vị đo và làm tròn số thập phân.',
  'title': 'Bài 10: Khái niệm số thập phân',
  'icon': '🔟',
  'description': 'Nhận biết số thập phân, cấu tạo gồm phần nguyên và phần thập phân, tên gọi và giá trị các '
                 'hàng của số thập phân.',
  'requirements': ['Đọc, viết được số thập phân và chuyển đổi phân số thập phân, hỗn số có chứa phân số thập '
                   'phân thành số thập phân.',
                   'Xác định đúng phần nguyên, phần thập phân và giá trị của từng chữ số theo hàng.',
                   'Vận dụng kiến thức của **Bài 10: Khái niệm số thập phân** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Mỗi **số thập phân** gồm hai phần: **phần nguyên** (bên trái dấu phẩy) và **phần thập '
                'phân** (bên phải dấu phẩy).\n'
                '- Các hàng sau dấu phẩy lần lượt là: **hàng phần mười** ($0{,}1 = \\dfrac{1}{10}$), **hàng '
                'phần trăm** ($0{,}01 = \\dfrac{1}{100}$), **hàng phần nghìn** ($0{,}001 = '
                '\\dfrac{1}{1000}$).',
  'theory': '### 1. Viết phân số thập phân dưới dạng số thập phân\n'
            '- $\\dfrac{3}{10} = 0{,}3$; $\\dfrac{45}{100} = 0{,}45$; $\\dfrac{7}{1000} = 0{,}007$; hỗn số '
            '$2\\dfrac{7}{10} = 2{,}7$.\n'
            '### 2. Hàng của số thập phân\n'
            '- Trong số $25{,}307$: phần nguyên là $25$ ($2$ chục, $5$ đơn vị); phần thập phân là $307$ ($3$ '
            'phần mười, $0$ phần trăm, $7$ phần nghìn).',
  'formulas': [{'category': 'Quan hệ với phân số thập phân',
                'items': [{'name': 'Đơn vị thập phân',
                           'formula': '$\\dfrac{1}{10} = 0{,}1$; $\\dfrac{1}{100} = 0{,}01$; '
                                      '$\\dfrac{1}{1000} = 0{,}001$'},
                          {'name': 'Hỗn số thập phân',
                           'formula': '$a\\dfrac{b}{10} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$'}]}],
  'example': 'Viết các số sau dưới dạng số thập phân: $\\dfrac{9}{100}$ và $15\\dfrac{3}{10}$.',
  'example_answer': 'Ta có $\\dfrac{9}{100} = 0{,}09$ và $15\\dfrac{3}{10} = 15{,}3$.',
  'real_life': 'Ghi chỉ số chiều cao ($1{,}45\\text{ m}$), cân nặng ($35{,}5\\text{ kg}$), nhiệt độ cơ thể '
               '($36{,}8^\\circ\\text{C}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số thập phân $\\dfrac{7}{100}$ viết dưới dạng số thập phân là:',
            'options': ['$0{,}7$', '$7{,}00$', '$0{,}007$', '$0{,}07$'],
            'answer': 3,
            'solution': 'Ta có $\\dfrac{7}{100} = 0{,}07$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số thập phân $32{,}581$, chữ số $8$ thuộc hàng nào?',
            'options': ['Hàng phần trăm', 'Hàng phần mười', 'Hàng phần nghìn', 'Hàng đơn vị'],
            'answer': 0,
            'solution': 'Sau dấu phẩy lần lượt là $5$ (phần mười), $8$ (phần trăm), $1$ (phần nghìn).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Khái niệm số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Đơn vị thập phân**?',
            'options': ['$\\dfrac{2}{10} = 0{,}1$; $\\dfrac{1}{100} = 0{,}01$; $\\dfrac{1}{1000} = 0{,}001$',
                        '$\\dfrac{1}{10} = 0{,}1$; $\\dfrac{1}{100} = 0{,}01$; $\\dfrac{1}{1000} = 0{,}001$',
                        '$\\dfrac{10}{1} = 0{,}1$; $\\dfrac{1}{100} = 0{,}01$; $\\dfrac{1}{1000} = 0{,}001$',
                        '$a\\dfrac{b}{10} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 10: Khái niệm số thập phân, **Đơn vị thập phân** '
                        'được xác định bởi: $\\dfrac{1}{10} = 0{,}1$; $\\dfrac{1}{100} = 0{,}01$; '
                        '$\\dfrac{1}{1000} = 0{,}001$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Khái niệm số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Hỗn số thập phân**?',
            'options': ['$a\\dfrac{b}{11} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$',
                        '$a\\dfrac{10}{b} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$',
                        '$a\\dfrac{b}{10} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$',
                        '$a\\dfrac{b}{20} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$'],
            'answer': 2,
            'solution': 'Trong Bài 10: Khái niệm số thập phân, **Hỗn số thập phân** có công thức/quy tắc là: '
                        '$a\\dfrac{b}{10} = a{,}b$; $a\\dfrac{bc}{100} = a{,}bc$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thập phân gồm $5$ chục, $4$ đơn vị và $6$ phần nghìn được viết là:',
            'options': ['$54{,}6$', '$54{,}06$', '$504{,}006$', '$54{,}006$'],
            'answer': 3,
            'solution': 'Phần nguyên là $54$, phần thập phân có $0$ phần mười, $0$ phần trăm, $6$ phần nghìn '
                        'nên viết là $54{,}006$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 10: Khái niệm số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Đọc, viết được số thập phân và chuyển đổi phân số thập phân, hỗn số có chứa phân số '
                        'thập phân thành số thập phân.',
                        'Đọc, viết được số thập phân và chuyển đổi phân số thập phân, hỗn số có chứa phân số '
                        'thập phân thành số thập phân. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đọc, viết được số thập phân và chuyển đổi phân số thập '
                        'phân, hỗn số có chứa phân số thập phân thành số thập phân.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đọc, viết được số thập phân và '
                        'chuyển đổi phân số thập phân, hỗn số có chứa phân số thập phân thành số thập phân.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 10: Khái niệm số thập phân: Đọc, viết được số thập '
                        'phân và chuyển đổi phân số thập phân, hỗn số có chứa phân số thập phân thành số '
                        'thập phân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hỗn số $4\\dfrac{25}{1000}$ viết dưới dạng số thập phân là $4{,}25$.',
            'answer': False,
            'solution': 'Ta có $4\\dfrac{25}{1000} = 4{,}025$ chứ không phải $4{,}25$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 10: Khái niệm số thập phân**, quy tắc **Đơn vị thập phân** được xác định bởi '
                 '$\\dfrac{1}{10} = 0{,}1$; $\\dfrac{1}{100} = 0{,}01$; $\\dfrac{1}{1000} = 0{,}001$ và khi '
                 'áp dụng cho ví dụ “Viết các số sau dưới dạng số thập phân: $\\dfrac{9}{100}$ và '
                 '$15\\dfrac{3}{10}$.” ta có lời giải: Ta có $\\dfrac{9}{100} = 0{,}09$ và $15\\dfrac{3}{10} '
                 '= 15{,}3$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đơn vị thập phân** ($\\dfrac{1}{10} = '
                        '0{,}1$; $\\dfrac{1}{100} = 0{,}01$; $\\dfrac{1}{1000} = 0{,}001$) và lời giải ví dụ '
                        'minh họa của Bài 10: Khái niệm số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 10: Khái niệm số thập phân** để giải bài toán sau: '
                 'Viết các số sau dưới dạng số thập phân: $\\dfrac{9}{100}$ và $15\\dfrac{3}{10}$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\dfrac{10}{100} = 0{,}09$ và $15\\dfrac{3}{10} = 15{,}3$.',
                        'Ta có $\\dfrac{9}{100} = 0{,}09$ và $15\\dfrac{3}{10} = 15{,}3$.',
                        'Ta có $\\dfrac{100}{9} = 0{,}09$ và $15\\dfrac{3}{10} = 15{,}3$.',
                        'Ta có $\\dfrac{18}{100} = 0{,}09$ và $15\\dfrac{3}{10} = 15{,}3$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 10: Khái niệm số thập phân: Ta có $\\dfrac{9}{100} = '
                        '0{,}09$ và $15\\dfrac{3}{10} = 15{,}3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm chữ số ở hàng phần trăm của số thập phân bằng với phân số $\\dfrac{3}{4}$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{3}{4} = \\dfrac{75}{100} = 0{,}75$, chữ số ở hàng phần trăm là $5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd02-so-thap-phan',
  'context_title': 'Chủ đề 2: Số thập phân',
  'context': 'Chủ đề 2 · SGK Toán 5: Khái niệm, so sánh, đổi đơn vị đo và làm tròn số thập phân.',
  'title': 'Bài 11: So sánh các số thập phân',
  'icon': '🔟',
  'description': 'Nhận biết hai số thập phân bằng nhau và quy tắc so sánh, sắp xếp các số thập phân.',
  'requirements': ['Nhận biết được tính chất thêm hoặc bớt chữ số $0$ ở tận cùng bên phải phần thập phân.',
                   'So sánh được hai số thập phân và sắp xếp một nhóm số thập phân theo thứ tự từ bé đến lớn '
                   'hoặc ngược lại.',
                   'Vận dụng kiến thức của **Bài 11: So sánh các số thập phân** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Nếu viết thêm (hoặc bỏ bớt) chữ số $0$ ở **tận cùng bên phải phần thập phân** của một số '
                'thập phân thì được một số thập phân bằng nó: $0{,}5 = 0{,}50 = 0{,}500$.\n'
                '- Muốn **so sánh hai số thập phân**, ta so sánh phần nguyên trước; nếu phần nguyên bằng '
                'nhau thì so sánh lần lượt từ hàng phần mười, hàng phần trăm, hàng phần nghìn, ...',
  'theory': '### 1. Số thập phân bằng nhau\n'
            '- $4{,}50 = 4{,}5$; $12 = 12{,}0 = 12{,}00$.\n'
            '### 2. Quy tắc so sánh hai số thập phân\n'
            '- Khác phần nguyên: $12{,}1 > 9{,}98$ vì $12 > 9$.\n'
            '- Cùng phần nguyên: $8{,}45 < 8{,}5$ vì hàng phần mười có $4 < 5$ (không phụ thuộc số lượng chữ '
            'số ở phần thập phân).',
  'formulas': [{'category': 'Tính chất và so sánh',
                'items': [{'name': 'Số thập phân bằng nhau', 'formula': '$a{,}b = a{,}b0 = a{,}b00$'},
                          {'name': 'Thứ tự so sánh',
                           'formula': 'Phần nguyên $\\rightarrow$ Phần mười $\\rightarrow$ Phần trăm '
                                      '$\\rightarrow$ Phần nghìn'}]}],
  'example': 'Sắp xếp các số $7{,}09$; $7{,}9$; $7{,}089$; $7{,}19$ theo thứ tự từ bé đến lớn.',
  'example_answer': 'So sánh từ hàng phần mười và phần trăm ta có: $7{,}089 < 7{,}09 < 7{,}19 < 7{,}9$.',
  'real_life': 'Xếp hạng thành tích chạy cự li ngắn (tính bằng giây) hoặc so sánh chiều cao các bạn trong '
               'lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số thập phân $4{,}50$ bằng số nào dưới đây?',
            'options': ['$4{,}5$', '$4{,}05$', '$45$', '$4{,}005$'],
            'answer': 0,
            'solution': 'Bỏ chữ số $0$ tận cùng bên phải phần thập phân của $4{,}50$ ta được $4{,}5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số lớn nhất trong các số $7{,}09$; $7{,}9$; $7{,}089$; $7{,}19$ là:',
            'options': ['$7{,}09$', '$7{,}9$', '$7{,}089$', '$7{,}19$'],
            'answer': 1,
            'solution': 'Cùng phần nguyên $7$, hàng phần mười của $7{,}9$ là $9$ lớn nhất nên $7{,}9$ lớn '
                        'nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: So sánh các số thập phân**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Số thập phân bằng nhau**?',
            'options': ['$a{,}b = a{,}b0 = a{,}b00$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $a{,}b = a{,}b0 = a{,}b00$',
                        '$a{,}b = a{,}b0 = a{,}b00$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a{,}b = a{,}b0 = a{,}b00$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 11: So sánh các số thập phân, **Số thập phân bằng '
                        'nhau** được xác định bởi: $a{,}b = a{,}b0 = a{,}b00$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: So sánh các số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Thứ tự so sánh**?',
            'options': ['Phần nguyên $\\rightarrow$ Phần mười $\\rightarrow$ Phần trăm $\\rightarrow$ Phần '
                        'nghìn (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Phần nguyên $\\rightarrow$ Phần mười $\\rightarrow$ Phần '
                        'trăm $\\rightarrow$ Phần nghìn',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phần nguyên $\\rightarrow$ Phần '
                        'mười $\\rightarrow$ Phần trăm $\\rightarrow$ Phần nghìn',
                        'Phần nguyên $\\rightarrow$ Phần mười $\\rightarrow$ Phần trăm $\\rightarrow$ Phần '
                        'nghìn'],
            'answer': 3,
            'solution': 'Trong Bài 11: So sánh các số thập phân, **Thứ tự so sánh** có công thức/quy tắc là: '
                        'Phần nguyên $\\rightarrow$ Phần mười $\\rightarrow$ Phần trăm $\\rightarrow$ Phần '
                        'nghìn.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Chiều cao của bốn bạn là: An $1{,}42\\text{ m}$; Bình $1{,}4\\text{ m}$; Chi '
                 '$1{,}38\\text{ m}$; Dũng $1{,}45\\text{ m}$. Bạn thấp nhất là:',
            'options': ['Chi', 'An', 'Bình', 'Dũng'],
            'answer': 0,
            'solution': 'Ta có $1{,}38 < 1{,}40 < 1{,}42 < 1{,}45$ nên Chi thấp nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 11: So sánh các số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được tính chất thêm hoặc bớt chữ số $1$ ở tận cùng bên phải phần thập '
                        'phân.',
                        'Nhận biết được tính chất thêm hoặc bớt chữ số $0$ ở tận cùng bên phải phần thập '
                        'phân.',
                        'Nhận biết được tính chất thêm hoặc bớt chữ số $2$ ở tận cùng bên phải phần thập '
                        'phân.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 11: So sánh các số thập phân: Nhận biết được tính '
                        'chất thêm hoặc bớt chữ số $0$ ở tận cùng bên phải phần thập phân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $0{,}8 > 0{,}75$ vì ở hàng phần mười có $8 > 7$.',
            'answer': True,
            'solution': 'Cùng phần nguyên $0$, hàng phần mười có $8 > 7$ nên $0{,}8 > 0{,}75$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 11: So sánh các số thập phân**, quy tắc **Số thập phân bằng nhau** được xác '
                 'định bởi $a{,}b = a{,}b0 = a{,}b00$ và khi áp dụng cho ví dụ “Sắp xếp các số $7{,}09$; '
                 '$7{,}9$; $7{,}089$; $7{,}19$ theo thứ tự từ bé đến lớn.” ta có lời giải: So sánh từ hàng '
                 'phần mười và phần trăm ta có: $7{,}089 < 7{,}09 < 7{,}19 < 7{,}9$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số thập phân bằng nhau** ($a{,}b = '
                        'a{,}b0 = a{,}b00$) và lời giải ví dụ minh họa của Bài 11: So sánh các số thập '
                        'phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 11: So sánh các số thập phân** để giải bài toán '
                 'sau: Sắp xếp các số $7{,}09$; $7{,}9$; $7{,}089$; $7{,}19$ theo thứ tự từ bé đến lớn. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['So sánh từ hàng phần mười và phần trăm ta có: $7{,}089 > 7{,}09 < 7{,}19 < 7{,}9$.',
                        'So sánh từ hàng phần mười và phần trăm ta có: $7{,}089 < 7{,}09 < 7{,}19 < 7{,}8$.',
                        'So sánh từ hàng phần mười và phần trăm ta có: $7{,}089 < 7{,}09 < 7{,}19 < 7{,}9$.',
                        'So sánh từ hàng phần mười và phần trăm ta có: $14{,}089 < 7{,}09 < 7{,}19 < '
                        '7{,}9$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 11: So sánh các số thập phân: So sánh từ hàng phần mười '
                        'và phần trăm ta có: $7{,}089 < 7{,}09 < 7{,}19 < 7{,}9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm chữ số $x$ biết $15{,}x8 > 15{,}88$.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Để $15{,}x8 > 15{,}88$ thì ở hàng phần mười phải có $x > 8$, suy ra $x = 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd02-so-thap-phan',
  'context_title': 'Chủ đề 2: Số thập phân',
  'context': 'Chủ đề 2 · SGK Toán 5: Khái niệm, so sánh, đổi đơn vị đo và làm tròn số thập phân.',
  'title': 'Bài 12: Viết số đo đại lượng dưới dạng số thập phân',
  'icon': '🔟',
  'description': 'Cách chuyển đổi các số đo độ dài, khối lượng, dung tích và diện tích sang số thập phân.',
  'requirements': ['Nắm vững mối quan hệ thập phân giữa các đơn vị đo độ dài, khối lượng, dung tích.',
                   'Viết đúng các số đo đại lượng có một hoặc hai tên đơn vị dưới dạng số thập phân.',
                   'Vận dụng kiến thức của **Bài 12: Viết số đo đại lượng dưới dạng số thập phân** để giải '
                   'bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Khi đổi từ đơn vị bé sang đơn vị lớn, ta dựa vào mối quan hệ $\\dfrac{1}{10}, '
                '\\dfrac{1}{100}, \\dfrac{1}{1000}$ để đưa về phân số thập phân (hoặc hỗn số) rồi viết thành '
                'số thập phân.\n'
                '- Hai đơn vị độ dài, khối lượng liền kề hơn kém nhau $10$ lần; hai đơn vị diện tích liền kề '
                'hơn kém nhau $100$ lần.',
  'theory': '### 1. Số đo độ dài và khối lượng\n'
            '- $3\\text{ m } 25\\text{ cm} = 3\\dfrac{25}{100}\\text{ m} = 3{,}25\\text{ m}$; $6\\text{ m } '
            '8\\text{ cm} = 6\\dfrac{8}{100}\\text{ m} = 6{,}08\\text{ m}$.\n'
            '- $4\\text{ kg } 50\\text{ g} = 4\\dfrac{50}{1000}\\text{ kg} = 4{,}05\\text{ kg}$; $2\\text{ '
            'tấn } 75\\text{ kg} = 2{,}075\\text{ tấn}$.\n'
            '### 2. Số đo diện tích\n'
            '- $1\\text{ dm}^2 = \\dfrac{1}{100}\\text{ m}^2 = 0{,}01\\text{ m}^2$, do đó $5\\text{ m}^2\\ '
            '7\\text{ dm}^2 = 5\\dfrac{7}{100}\\text{ m}^2 = 5{,}07\\text{ m}^2$.',
  'formulas': [{'category': 'Đổi đơn vị sang số thập phân',
                'items': [{'name': 'Độ dài',
                           'formula': '$1\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = 0{,}01\\text{ m}$; '
                                      '$1\\text{ m} = 0{,}001\\text{ km}$'},
                          {'name': 'Khối lượng',
                           'formula': '$1\\text{ g} = 0{,}001\\text{ kg}$; $1\\text{ kg} = 0{,}001\\text{ '
                                      'tấn}$'},
                          {'name': 'Diện tích',
                           'formula': '$1\\text{ dm}^2 = 0{,}01\\text{ m}^2$; $1\\text{ cm}^2 = '
                                      '0{,}01\\text{ dm}^2$'}]}],
  'example': 'Viết số đo $2\\text{ kg } 35\\text{ g}$ dưới dạng số thập phân có đơn vị ki-lô-gam.',
  'example_answer': 'Vì $35\\text{ g} = \\dfrac{35}{1000}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ kg '
                    '} 35\\text{ g} = 2{,}035\\text{ kg}$.',
  'real_life': 'Đọc khối lượng hàng hóa trên cân điện tử siêu thị và số km trên đồng hồ công-tơ-mét.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số đo $6\\text{ m } 8\\text{ cm}$ viết dưới dạng số thập phân có đơn vị mét là:',
            'options': ['$6{,}8\\text{ m}$', '$6{,}08\\text{ m}$', '$6{,}008\\text{ m}$', '$68\\text{ m}$'],
            'answer': 1,
            'solution': 'Vì $8\\text{ cm} = \\dfrac{8}{100}\\text{ m} = 0{,}08\\text{ m}$ nên $6\\text{ m } '
                        '8\\text{ cm} = 6{,}08\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi $450\\text{ g}$ sang đơn vị ki-lô-gam ta được:',
            'options': ['$4{,}5\\text{ kg}$',
                        '$0{,}045\\text{ kg}$',
                        '$0{,}45\\text{ kg}$',
                        '$45\\text{ kg}$'],
            'answer': 2,
            'solution': 'Ta có $450\\text{ g} = \\dfrac{450}{1000}\\text{ kg} = 0{,}450\\text{ kg} = '
                        '0{,}45\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Viết số đo đại lượng dưới dạng số thập phân**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Độ dài**?',
            'options': ['$2\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = 0{,}01\\text{ m}$; $1\\text{ m} = '
                        '0{,}001\\text{ km}$',
                        '$1\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = 0{,}01\\text{ m}$; $1\\text{ m} = '
                        '0{,}2\\text{ km}$',
                        '$1\\text{ g} = 0{,}001\\text{ kg}$; $1\\text{ kg} = 0{,}001\\text{ tấn}$',
                        '$1\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = 0{,}01\\text{ m}$; $1\\text{ m} = '
                        '0{,}001\\text{ km}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 12: Viết số đo đại lượng dưới dạng số thập phân, '
                        '**Độ dài** được xác định bởi: $1\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = '
                        '0{,}01\\text{ m}$; $1\\text{ m} = 0{,}001\\text{ km}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Viết số đo đại lượng dưới dạng số thập phân**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Khối lượng**?',
            'options': ['$1\\text{ g} = 0{,}001\\text{ kg}$; $1\\text{ kg} = 0{,}001\\text{ tấn}$',
                        '$2\\text{ g} = 0{,}001\\text{ kg}$; $1\\text{ kg} = 0{,}001\\text{ tấn}$',
                        '$1\\text{ g} = 0{,}001\\text{ kg}$; $1\\text{ kg} = 0{,}2\\text{ tấn}$',
                        '$1\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = 0{,}01\\text{ m}$; $1\\text{ m} = '
                        '0{,}001\\text{ km}$'],
            'answer': 0,
            'solution': 'Trong Bài 12: Viết số đo đại lượng dưới dạng số thập phân, **Khối lượng** có công '
                        'thức/quy tắc là: $1\\text{ g} = 0{,}001\\text{ kg}$; $1\\text{ kg} = 0{,}001\\text{ '
                        'tấn}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đo $5\\text{ m}^2\\ 7\\text{ dm}^2$ bằng bao nhiêu mét vuông?',
            'options': ['$5{,}7\\text{ m}^2$',
                        '$5{,}07\\text{ m}^2$',
                        '$50{,}7\\text{ m}^2$',
                        '$5{,}007\\text{ m}^2$'],
            'answer': 1,
            'solution': 'Vì $1\\text{ m}^2 = 100\\text{ dm}^2$ nên $7\\text{ dm}^2 = 0{,}07\\text{ m}^2$, '
                        'suy ra $5{,}07\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 12: Viết số đo đại lượng dưới dạng số thập phân**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nắm vững mối quan hệ thập phân giữa các đơn vị đo độ dài, khối lượng, dung tích. '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nắm vững mối quan hệ thập phân giữa các đơn vị đo độ dài, '
                        'khối lượng, dung tích.',
                        'Nắm vững mối quan hệ thập phân giữa các đơn vị đo độ dài, khối lượng, dung tích.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nắm vững mối quan hệ thập phân '
                        'giữa các đơn vị đo độ dài, khối lượng, dung tích.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 12: Viết số đo đại lượng dưới dạng số thập phân: Nắm '
                        'vững mối quan hệ thập phân giữa các đơn vị đo độ dài, khối lượng, dung tích.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Độ dài $4\\text{ km } 60\\text{ m}$ viết dưới dạng số thập phân là $4{,}6\\text{ km}$.',
            'answer': False,
            'solution': 'Ta có $60\\text{ m} = \\dfrac{60}{1000}\\text{ km} = 0{,}06\\text{ km}$ nên '
                        '$4\\text{ km } 60\\text{ m} = 4{,}06\\text{ km}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 12: Viết số đo đại lượng dưới dạng số thập phân**, quy tắc **Độ dài** được xác '
                 'định bởi $1\\text{ dm} = 0{,}1\\text{ m}$; $1\\text{ cm} = 0{,}01\\text{ m}$; $1\\text{ m} '
                 '= 0{,}001\\text{ km}$ và khi áp dụng cho ví dụ “Viết số đo $2\\text{ kg } 35\\text{ g}$ '
                 'dưới dạng số thập phân có đơn vị ki-lô-gam.” ta có lời giải: Vì $35\\text{ g} = '
                 '\\dfrac{35}{1000}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ kg } 35\\text{ g} = '
                 '2{,}035\\text{ kg}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Độ dài** ($1\\text{ dm} = 0{,}1\\text{ '
                        'm}$; $1\\text{ cm} = 0{,}01\\text{ m}$; $1\\text{ m} = 0{,}001\\text{ km}$) và lời '
                        'giải ví dụ minh họa của Bài 12: Viết số đo đại lượng dưới dạng số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 12: Viết số đo đại lượng dưới dạng số thập phân** '
                 'để giải bài toán sau: Viết số đo $2\\text{ kg } 35\\text{ g}$ dưới dạng số thập phân có '
                 'đơn vị ki-lô-gam. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì $45\\text{ g} = \\dfrac{35}{1000}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ '
                        'kg } 35\\text{ g} = 2{,}035\\text{ kg}$.',
                        'Vì $35\\text{ g} = \\dfrac{1000}{35}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ '
                        'kg } 35\\text{ g} = 2{,}035\\text{ kg}$.',
                        'Vì $70\\text{ g} = \\dfrac{35}{1000}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ '
                        'kg } 35\\text{ g} = 2{,}035\\text{ kg}$.',
                        'Vì $35\\text{ g} = \\dfrac{35}{1000}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ '
                        'kg } 35\\text{ g} = 2{,}035\\text{ kg}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 12: Viết số đo đại lượng dưới dạng số thập phân: Vì '
                        '$35\\text{ g} = \\dfrac{35}{1000}\\text{ kg} = 0{,}035\\text{ kg}$ nên $2\\text{ kg '
                        '} 35\\text{ g} = 2{,}035\\text{ kg}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một con đường dài $3\\text{ km } 75\\text{ m}$. Viết độ dài con đường dưới dạng số thập '
                 'phân với đơn vị ki-lô-mét.',
            'answer': ['3,075', '3.075'],
            'unit': None,
            'solution': 'Ta có $75\\text{ m} = \\dfrac{75}{1000}\\text{ km} = 0{,}075\\text{ km}$ nên độ dài '
                        'con đường là $3{,}075\\text{ km}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd02-so-thap-phan',
  'context_title': 'Chủ đề 2: Số thập phân',
  'context': 'Chủ đề 2 · SGK Toán 5: Khái niệm, so sánh, đổi đơn vị đo và làm tròn số thập phân.',
  'title': 'Bài 13: Làm tròn số thập phân',
  'icon': '🔟',
  'description': 'Quy tắc làm tròn số thập phân đến số tự nhiên gần nhất hoặc đến hàng phần mười, hàng phần '
                 'trăm.',
  'requirements': ['Làm tròn được một số thập phân đến số tự nhiên gần nhất.',
                   'Làm tròn được một số thập phân đến hàng phần mười hoặc hàng phần trăm.',
                   'Vận dụng kiến thức của **Bài 13: Làm tròn số thập phân** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': '- Khi làm tròn số thập phân đến một hàng nào đó, ta xét **chữ số ngay bên phải** hàng làm '
                'tròn:\n'
                '- Nếu chữ số đó **bé hơn $5$** ($0; 1; 2; 3; 4$) thì giữ nguyên chữ số ở hàng làm tròn; nếu '
                '**lớn hơn hoặc bằng $5$** ($5; 6; 7; 8; 9$) thì cộng thêm $1$ vào chữ số ở hàng làm tròn '
                'rồi bỏ các chữ số phía sau ở phần thập phân.',
  'theory': '### 1. Làm tròn đến số tự nhiên gần nhất (hàng đơn vị)\n'
            '- Xét chữ số hàng phần mười: $7{,}46$ có chữ số phần mười là $4 < 5$ nên làm tròn thành $7$; '
            '$12{,}81$ có chữ số phần mười là $8 \\ge 5$ nên làm tròn thành $13$.\n'
            '### 2. Làm tròn đến hàng phần mười, hàng phần trăm\n'
            '- Làm tròn đến hàng phần mười (xét hàng phần trăm): $7{,}46 \\rightarrow 7{,}5$.\n'
            '- Làm tròn đến hàng phần trăm (xét hàng phần nghìn): $12{,}348 \\rightarrow 12{,}35$.',
  'formulas': [{'category': 'Quy tắc làm tròn',
                'items': [{'name': 'Chữ số ngay sau < 5', 'formula': 'Giữ nguyên chữ số ở hàng làm tròn'},
                          {'name': 'Chữ số ngay sau >= 5',
                           'formula': 'Tăng chữ số ở hàng làm tròn thêm $1$ đơn vị'}]}],
  'example': 'Làm tròn số $18{,}637$ đến số tự nhiên gần nhất, đến hàng phần mười và đến hàng phần trăm.',
  'example_answer': 'Đến số tự nhiên gần nhất: $19$ (vì $6 \\ge 5$); đến hàng phần mười: $18{,}6$ (vì $3 < '
                    '5$); đến hàng phần trăm: $18{,}64$ (vì $7 \\ge 5$).',
  'real_life': 'Làm tròn điểm trung bình môn học, số đo khoảng cách trên bản đồ và khối lượng hàng hóa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số thập phân $9{,}72$ đến số tự nhiên gần nhất ta được:',
            'options': ['$9$', '$9{,}7$', '$10$', '$9{,}8$'],
            'answer': 2,
            'solution': 'Chữ số hàng phần mười là $7 \\ge 5$ nên làm tròn lên thành $10$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $6{,}358$ đến hàng phần mười ta được:',
            'options': ['$6{,}3$', '$6{,}36$', '$6$', '$6{,}4$'],
            'answer': 3,
            'solution': 'Chữ số hàng phần trăm là $5 \\ge 5$ nên làm tròn hàng phần mười lên thành $6{,}4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Làm tròn số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Chữ số ngay sau < 5**?',
            'options': ['Giữ nguyên chữ số ở hàng làm tròn',
                        'Giữ nguyên chữ số ở hàng làm tròn (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Giữ nguyên chữ số ở hàng làm tròn',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giữ nguyên chữ số ở hàng làm '
                        'tròn'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 13: Làm tròn số thập phân, **Chữ số ngay sau < 5** '
                        'được xác định bởi: Giữ nguyên chữ số ở hàng làm tròn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Làm tròn số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Chữ số ngay sau >= 5**?',
            'options': ['Tăng chữ số ở hàng làm tròn thêm $2$ đơn vị',
                        'Tăng chữ số ở hàng làm tròn thêm $1$ đơn vị',
                        'Giữ nguyên chữ số ở hàng làm tròn',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 1,
            'solution': 'Trong Bài 13: Làm tròn số thập phân, **Chữ số ngay sau >= 5** có công thức/quy tắc '
                        'là: Tăng chữ số ở hàng làm tròn thêm $1$ đơn vị.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Làm tròn số $24{,}834$ đến hàng phần trăm ta được:',
            'options': ['$24{,}8$', '$24{,}84$', '$24{,}83$', '$25$'],
            'answer': 2,
            'solution': 'Chữ số hàng phần nghìn là $4 < 5$ nên giữ nguyên hàng phần trăm được $24{,}83$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 13: Làm tròn số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Làm tròn được một số thập phân đến số tự nhiên gần nhất. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Làm tròn được một số thập phân đến số tự nhiên gần nhất.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Làm tròn được một số thập phân '
                        'đến số tự nhiên gần nhất.',
                        'Làm tròn được một số thập phân đến số tự nhiên gần nhất.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 13: Làm tròn số thập phân: Làm tròn được một số thập '
                        'phân đến số tự nhiên gần nhất.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Làm tròn số $15{,}46$ đến số tự nhiên gần nhất ta được $16$.',
            'answer': False,
            'solution': 'Chữ số hàng phần mười là $4 < 5$ nên làm tròn đến số tự nhiên gần nhất phải là '
                        '$15$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 13: Làm tròn số thập phân**, quy tắc **Chữ số ngay sau < 5** được xác định bởi '
                 'Giữ nguyên chữ số ở hàng làm tròn và khi áp dụng cho ví dụ “Làm tròn số $18{,}637$ đến số '
                 'tự nhiên gần nhất, đến hàng phần mười và đến hàng phần trăm.” ta có lời giải: Đến số tự '
                 'nhiên gần nhất: $19$ (vì $6 \\ge 5$); đến hàng phần mười: $18{,}6$ (vì $3 < 5$); đến hàng '
                 'phần trăm: $18{,}64$ (vì $7 \\ge 5$).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Chữ số ngay sau < 5** (Giữ nguyên chữ số '
                        'ở hàng làm tròn) và lời giải ví dụ minh họa của Bài 13: Làm tròn số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 13: Làm tròn số thập phân** để giải bài toán sau: '
                 'Làm tròn số $18{,}637$ đến số tự nhiên gần nhất, đến hàng phần mười và đến hàng phần trăm. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đến số tự nhiên gần nhất: $19$ (vì $6 \\ge 5$); đến hàng phần mười: $18{,}6$ (vì $3 '
                        '< 5$); đến hàng phần trăm: $18{,}64$ (vì $7 \\ge 5$).',
                        'Đến số tự nhiên gần nhất: $19$ (vì $6 \\le 5$); đến hàng phần mười: $18{,}6$ (vì $3 '
                        '< 5$); đến hàng phần trăm: $18{,}64$ (vì $7 \\ge 5$).',
                        'Đến số tự nhiên gần nhất: $19$ (vì $6 \\ge 5$); đến hàng phần mười: $18{,}6$ (vì $3 '
                        '< 5$); đến hàng phần trăm: $18{,}64$ (vì $7 \\ge 4$).',
                        'Đến số tự nhiên gần nhất: $38$ (vì $6 \\ge 5$); đến hàng phần mười: $18{,}6$ (vì $3 '
                        '< 5$); đến hàng phần trăm: $18{,}64$ (vì $7 \\ge 5$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 13: Làm tròn số thập phân: Đến số tự nhiên gần nhất: '
                        '$19$ (vì $6 \\ge 5$); đến hàng phần mười: $18{,}6$ (vì $3 < 5$); đến hàng phần '
                        'trăm: $18{,}64$ (vì $7 \\ge 5$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mảnh vườn có diện tích $128{,}74\\text{ m}^2$. Làm tròn diện tích mảnh vườn đó đến '
                 'hàng phần mười.',
            'answer': ['128,7', '128.7'],
            'unit': None,
            'solution': 'Chữ số hàng phần trăm là $4 < 5$ nên làm tròn đến hàng phần mười được $128{,}7$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd03-don-vi-do-dien-tich',
  'context_title': 'Chủ đề 3: Một số đơn vị đo diện tích',
  'context': 'Chủ đề 3 · SGK Toán 5: Ki-lô-mét vuông, héc-ta và bảng đơn vị đo diện tích.',
  'title': 'Bài 15: Ki-lô-mét vuông. Héc-ta',
  'icon': '🗺️',
  'description': 'Nhận biết hai đơn vị đo diện tích lớn là ki-lô-mét vuông và héc-ta cùng mối quan hệ với '
                 'mét vuông.',
  'requirements': ['Nhận biết được đơn vị ki-lô-mét vuông ($\\text{km}^2$) và héc-ta ($\\text{ha}$) dùng để '
                   'đo diện tích lớn.',
                   'Chuyển đổi đúng giữa $\\text{km}^2$, $\\text{ha}$ và $\\text{m}^2$.',
                   'Vận dụng kiến thức của **Bài 15: Ki-lô-mét vuông. Héc-ta** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- **Ki-lô-mét vuông** ($\\text{km}^2$) là diện tích của hình vuông có cạnh dài $1\\text{ '
                'km}$. Ta có $1\\text{ km}^2 = 1\\,000\\,000\\text{ m}^2$.\n'
                '- **Héc-ta** ($\\text{ha}$) là diện tích của hình vuông có cạnh dài $100\\text{ m}$. Ta có '
                '$1\\text{ ha} = 10\\,000\\text{ m}^2$ và $1\\text{ km}^2 = 100\\text{ ha}$.',
  'theory': '### 1. Ki-lô-mét vuông ($\\text{km}^2$)\n'
            '- Dùng để đo diện tích tỉnh, thành phố, quốc gia hoặc khu vực địa lí rộng lớn.\n'
            '### 2. Héc-ta ($\\text{ha}$)\n'
            '- Thường dùng để đo diện tích ruộng đất, khu rừng, nông trường, công viên.\n'
            '- Ví dụ: $3\\text{ ha} = 30\\,000\\text{ m}^2$; $25\\,000\\text{ m}^2 = 2{,}5\\text{ ha}$; '
            '$4\\text{ km}^2 = 400\\text{ ha}$.',
  'formulas': [{'category': 'Quan hệ đơn vị diện tích lớn',
                'items': [{'name': 'Héc-ta sang mét vuông',
                           'formula': '$1\\text{ ha} = 10\\,000\\text{ m}^2$'},
                          {'name': 'Ki-lô-mét vuông',
                           'formula': '$1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$'}]}],
  'example': 'Đổi các đơn vị sau: $5\\text{ ha} = \\dots\\text{ m}^2$ và $350\\text{ ha} = \\dots\\text{ '
             'km}^2$.',
  'example_answer': 'Ta có $5\\text{ ha} = 5 \\times 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ ha} = '
                    '\\dfrac{350}{100}\\text{ km}^2 = 3{,}5\\text{ km}^2$.',
  'real_life': 'Đo diện tích rừng quốc gia Cúc Phương, diện tích cánh đồng lúa hoặc diện tích mặt hồ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một héc-ta ($1\\text{ ha}$) bằng bao nhiêu mét vuông?',
            'options': ['$100\\text{ m}^2$',
                        '$1000\\text{ m}^2$',
                        '$1\\,000\\,000\\text{ m}^2$',
                        '$10\\,000\\text{ m}^2$'],
            'answer': 3,
            'solution': 'Theo quy ước, $1\\text{ ha} = 10\\,000\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một ki-lô-mét vuông ($1\\text{ km}^2$) bằng bao nhiêu héc-ta?',
            'options': ['$100\\text{ ha}$', '$10\\text{ ha}$', '$1000\\text{ ha}$', '$10\\,000\\text{ ha}$'],
            'answer': 0,
            'solution': 'Ta có $1\\text{ km}^2 = 100\\text{ ha}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Ki-lô-mét vuông. Héc-ta**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Héc-ta sang mét vuông**?',
            'options': ['$2\\text{ ha} = 10\\,000\\text{ m}^2$',
                        '$1\\text{ ha} = 10\\,000\\text{ m}^2$',
                        '$1\\text{ ha} = 10\\,000\\text{ m}^1$',
                        '$1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 15: Ki-lô-mét vuông. Héc-ta, **Héc-ta sang mét '
                        'vuông** được xác định bởi: $1\\text{ ha} = 10\\,000\\text{ m}^2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Ki-lô-mét vuông. Héc-ta**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Ki-lô-mét vuông**?',
            'options': ['$2\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$',
                        '$1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^1$',
                        '$1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$',
                        '$1\\text{ ha} = 10\\,000\\text{ m}^2$'],
            'answer': 2,
            'solution': 'Trong Bài 15: Ki-lô-mét vuông. Héc-ta, **Ki-lô-mét vuông** có công thức/quy tắc là: '
                        '$1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đo $45\\,000\\text{ m}^2$ đổi ra héc-ta bằng:',
            'options': ['$45\\text{ ha}$', '$450\\text{ ha}$', '$0{,}45\\text{ ha}$', '$4{,}5\\text{ ha}$'],
            'answer': 3,
            'solution': 'Ta lấy $45\\,000 : 10\\,000 = 4{,}5\\text{ ha}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 15: Ki-lô-mét vuông. Héc-ta**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được đơn vị ki-lô-mét vuông ($\\text{km}^2$) và héc-ta ($\\text{ha}$) '
                        'dùng để đo diện tích lớn.',
                        'Nhận biết được đơn vị ki-lô-mét vuông ($\\text{km}^3$) và héc-ta ($\\text{ha}$) '
                        'dùng để đo diện tích lớn.',
                        'Nhận biết được đơn vị ki-lô-mét vuông ($\\text{km}^1$) và héc-ta ($\\text{ha}$) '
                        'dùng để đo diện tích lớn.',
                        'Nhận biết được đơn vị ki-lô-mét vuông ($\\text{km}^4$) và héc-ta ($\\text{ha}$) '
                        'dùng để đo diện tích lớn.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 15: Ki-lô-mét vuông. Héc-ta: Nhận biết được đơn vị '
                        'ki-lô-mét vuông ($\\text{km}^2$) và héc-ta ($\\text{ha}$) dùng để đo diện tích '
                        'lớn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $2\\text{ km}^2 = 2\\,000\\,000\\text{ m}^2$.',
            'answer': True,
            'solution': 'Vì $1\\text{ km}^2 = 1\\,000\\,000\\text{ m}^2$ nên $2\\text{ km}^2 = '
                        '2\\,000\\,000\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 15: Ki-lô-mét vuông. Héc-ta**, quy tắc **Héc-ta sang mét vuông** được xác định '
                 'bởi $1\\text{ ha} = 10\\,000\\text{ m}^2$ và khi áp dụng cho ví dụ “Đổi các đơn vị sau: '
                 '$5\\text{ ha} = \\dots\\text{ m}^2$ và $350\\text{ ha} = \\dots\\text{ km}^2$.” ta có lời '
                 'giải: Ta có $5\\text{ ha} = 5 \\times 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ ha} '
                 '= \\dfrac{350}{100}\\text{ km}^2 = 3{,}5\\text{ km}^2$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Héc-ta sang mét vuông** ($1\\text{ ha} = '
                        '10\\,000\\text{ m}^2$) và lời giải ví dụ minh họa của Bài 15: Ki-lô-mét vuông. '
                        'Héc-ta.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 15: Ki-lô-mét vuông. Héc-ta** để giải bài toán sau: '
                 'Đổi các đơn vị sau: $5\\text{ ha} = \\dots\\text{ m}^2$ và $350\\text{ ha} = \\dots\\text{ '
                 'km}^2$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $5\\text{ ha} = 5 : 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ ha} = '
                        '\\dfrac{350}{100}\\text{ km}^2 = 3{,}5\\text{ km}^2$.',
                        'Ta có $5\\text{ ha} = 5 \\times 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ ha} '
                        '= \\dfrac{350}{100}\\text{ km}^2 = 3{,}5\\text{ km}^2$.',
                        'Ta có $5\\text{ ha} = 5 \\times 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ ha} '
                        '= \\dfrac{100}{350}\\text{ km}^2 = 3{,}5\\text{ km}^2$.',
                        'Ta có $10\\text{ ha} = 5 \\times 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ '
                        'ha} = \\dfrac{350}{100}\\text{ km}^2 = 3{,}5\\text{ km}^2$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 15: Ki-lô-mét vuông. Héc-ta: Ta có $5\\text{ ha} = 5 '
                        '\\times 10\\,000 = 50\\,000\\text{ m}^2$ và $350\\text{ ha} = '
                        '\\dfrac{350}{100}\\text{ km}^2 = 3{,}5\\text{ km}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khu rừng hình chữ nhật có chiều dài $2\\text{ km}$ và chiều rộng $800\\text{ m}$. Diện '
                 'tích khu rừng đó bằng bao nhiêu héc-ta?',
            'answer': ['160'],
            'unit': None,
            'solution': 'Đổi $2\\text{ km} = 2000\\text{ m}$. Diện tích khu rừng là $2000 \\times 800 = '
                        '1\\,600\\,000\\text{ m}^2 = 160\\text{ ha}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd03-don-vi-do-dien-tich',
  'context_title': 'Chủ đề 3: Một số đơn vị đo diện tích',
  'context': 'Chủ đề 3 · SGK Toán 5: Ki-lô-mét vuông, héc-ta và bảng đơn vị đo diện tích.',
  'title': 'Bài 16: Các đơn vị đo diện tích',
  'icon': '🗺️',
  'description': 'Hệ thống hóa bảng đơn vị đo diện tích và cách chuyển đổi giữa các đơn vị đo diện tích.',
  'requirements': ['Nắm vững thứ tự các đơn vị đo diện tích và quy luật hai đơn vị liền kề hơn kém nhau '
                   '$100$ lần.',
                   'Viết và chuyển đổi được các số đo diện tích dưới dạng số tự nhiên, phân số hoặc số thập '
                   'phân.',
                   'Vận dụng kiến thức của **Bài 16: Các đơn vị đo diện tích** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Trong bảng đơn vị đo diện tích ($\text{km}^2, \text{ha}, \text{m}^2, \text{dm}^2, \t'
                'ext{cm}^2, \text{mm}^2$), mỗi đơn vị lớn gấp $100$ lần đơn vị bé hơn tiếp liền.\n'
                '- Mỗi đơn vị bé bằng $\\dfrac{1}{100} = 0{,}01$ đơn vị lớn hơn tiếp liền.',
  'theory': '### 1. Quan hệ giữa các đơn vị diện tích thông dụng\n'
            '- $1\\text{ m}^2 = 100\\text{ dm}^2 = 10\\,000\\text{ cm}^2$; $1\\text{ dm}^2 = 100\\text{ '
            'cm}^2 = 10\\,000\\text{ mm}^2$.\n'
            '### 2. Viết số đo diện tích dưới dạng số thập phân\n'
            '- Mỗi đơn vị đo diện tích liền kề ứng với **hai chữ số**: $5\\text{ m}^2\\ 8\\text{ dm}^2 = '
            '5{,}08\\text{ m}^2$; $12\\text{ dm}^2\\ 35\\text{ cm}^2 = 12{,}35\\text{ dm}^2$.',
  'formulas': [{'category': 'Quan hệ liền kề',
                'items': [{'name': 'Hai đơn vị diện tích liền kề',
                           'formula': 'Hơn kém nhau $100$ lần (ứng với $2$ chữ số)'},
                          {'name': 'Từ mét vuông đến mi-li-mét vuông',
                           'formula': '$1\\text{ m}^2 = 100\\text{ dm}^2$; $1\\text{ dm}^2 = 100\\text{ '
                                      'cm}^2$; $1\\text{ cm}^2 = 100\\text{ mm}^2$'}]}],
  'example': 'Viết số thích hợp vào chỗ chấm: $7\\text{ m}^2\\ 9\\text{ dm}^2 = \\dots\\text{ m}^2$ và '
             '$3{,}4\\text{ ha} = \\dots\\text{ m}^2$.',
  'example_answer': 'Ta có $7\\text{ m}^2\\ 9\\text{ dm}^2 = 7\\dfrac{9}{100}\\text{ m}^2 = 7{,}09\\text{ '
                    'm}^2$ và $3{,}4\\text{ ha} = 34\\,000\\text{ m}^2$.',
  'real_life': 'Tính diện tích mặt sàn căn hộ, diện tích viên gạch lát nền và diện tích đất canh tác.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đơn vị đo diện tích liền kề nhau hơn kém nhau bao nhiêu lần?',
            'options': ['$100$ lần', '$10$ lần', '$1000$ lần', '$60$ lần'],
            'answer': 0,
            'solution': 'Hai đơn vị đo diện tích liền kề hơn kém nhau $100$ lần.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi $3\\text{ m}^2$ ra đề-xi-mét vuông ta được:',
            'options': ['$30\\text{ dm}^2$',
                        '$300\\text{ dm}^2$',
                        '$3000\\text{ dm}^2$',
                        '$0{,}03\\text{ dm}^2$'],
            'answer': 1,
            'solution': 'Vì $1\\text{ m}^2 = 100\\text{ dm}^2$ nên $3\\text{ m}^2 = 300\\text{ dm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Các đơn vị đo diện tích**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Hai đơn vị diện tích liền kề**?',
            'options': ['Hơn kém nhau $110$ lần (ứng với $2$ chữ số)',
                        'Hơn kém nhau $100$ lần (ứng với $1$ chữ số)',
                        'Hơn kém nhau $100$ lần (ứng với $2$ chữ số)',
                        'Hơn kém nhau $102$ lần (ứng với $2$ chữ số)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 16: Các đơn vị đo diện tích, **Hai đơn vị diện '
                        'tích liền kề** được xác định bởi: Hơn kém nhau $100$ lần (ứng với $2$ chữ số).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Các đơn vị đo diện tích**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Từ mét vuông đến mi-li-mét vuông**?',
            'options': ['$2\\text{ m}^2 = 100\\text{ dm}^2$; $1\\text{ dm}^2 = 100\\text{ cm}^2$; $1\\text{ '
                        'cm}^2 = 100\\text{ mm}^2$',
                        '$1\\text{ m}^2 = 100\\text{ dm}^2$; $1\\text{ dm}^2 = 100\\text{ cm}^2$; $1\\text{ '
                        'cm}^2 = 100\\text{ mm}^1$',
                        'Hơn kém nhau $100$ lần (ứng với $2$ chữ số)',
                        '$1\\text{ m}^2 = 100\\text{ dm}^2$; $1\\text{ dm}^2 = 100\\text{ cm}^2$; $1\\text{ '
                        'cm}^2 = 100\\text{ mm}^2$'],
            'answer': 3,
            'solution': 'Trong Bài 16: Các đơn vị đo diện tích, **Từ mét vuông đến mi-li-mét vuông** có công '
                        'thức/quy tắc là: $1\\text{ m}^2 = 100\\text{ dm}^2$; $1\\text{ dm}^2 = 100\\text{ '
                        'cm}^2$; $1\\text{ cm}^2 = 100\\text{ mm}^2$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đo $5\\text{ m}^2\\ 8\\text{ dm}^2$ viết dưới dạng số thập phân có đơn vị mét vuông là:',
            'options': ['$5{,}08\\text{ m}^2$',
                        '$5{,}8\\text{ m}^2$',
                        '$58\\text{ m}^2$',
                        '$5{,}008\\text{ m}^2$'],
            'answer': 0,
            'solution': 'Ta có $8\\text{ dm}^2 = \\dfrac{8}{100}\\text{ m}^2 = 0{,}08\\text{ m}^2$ nên bằng '
                        '$5{,}08\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 16: Các đơn vị đo diện tích**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nắm vững thứ tự các đơn vị đo diện tích và quy luật hai đơn vị liền kề hơn kém nhau '
                        '$110$ lần.',
                        'Nắm vững thứ tự các đơn vị đo diện tích và quy luật hai đơn vị liền kề hơn kém nhau '
                        '$100$ lần.',
                        'Nắm vững thứ tự các đơn vị đo diện tích và quy luật hai đơn vị liền kề hơn kém nhau '
                        '$99$ lần.',
                        'Nắm vững thứ tự các đơn vị đo diện tích và quy luật hai đơn vị liền kề hơn kém nhau '
                        '$102$ lần.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 16: Các đơn vị đo diện tích: Nắm vững thứ tự các đơn '
                        'vị đo diện tích và quy luật hai đơn vị liền kề hơn kém nhau $100$ lần.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $1\\text{ m}^2 = 10\\text{ dm}^2$.',
            'answer': False,
            'solution': 'Ta có $1\\text{ m}^2 = 100\\text{ dm}^2$ chứ không phải $10\\text{ dm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 16: Các đơn vị đo diện tích**, quy tắc **Hai đơn vị diện tích liền kề** được '
                 'xác định bởi Hơn kém nhau $100$ lần (ứng với $2$ chữ số) và khi áp dụng cho ví dụ “Viết số '
                 'thích hợp vào chỗ chấm: $7\\text{ m}^2\\ 9\\text{ dm}^2 = \\dots\\text{ m}^2$ và '
                 '$3{,}4\\text{ ha} = \\dots\\text{ m}^2$.” ta có lời giải: Ta có $7\\text{ m}^2\\ 9\\text{ '
                 'dm}^2 = 7\\dfrac{9}{100}\\text{ m}^2 = 7{,}09\\text{ m}^2$ và $3{,}4\\text{ ha} = '
                 '34\\,000\\text{ m}^2$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hai đơn vị diện tích liền kề** (Hơn kém '
                        'nhau $100$ lần (ứng với $2$ chữ số)) và lời giải ví dụ minh họa của Bài 16: Các đơn '
                        'vị đo diện tích.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 16: Các đơn vị đo diện tích** để giải bài toán sau: '
                 'Viết số thích hợp vào chỗ chấm: $7\\text{ m}^2\\ 9\\text{ dm}^2 = \\dots\\text{ m}^2$ và '
                 '$3{,}4\\text{ ha} = \\dots\\text{ m}^2$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $8\\text{ m}^2\\ 9\\text{ dm}^2 = 7\\dfrac{9}{100}\\text{ m}^2 = '
                        '7{,}09\\text{ m}^2$ và $3{,}4\\text{ ha} = 34\\,000\\text{ m}^2$.',
                        'Ta có $7\\text{ m}^2\\ 9\\text{ dm}^2 = 7\\dfrac{100}{9}\\text{ m}^2 = '
                        '7{,}09\\text{ m}^2$ và $3{,}4\\text{ ha} = 34\\,000\\text{ m}^2$.',
                        'Ta có $7\\text{ m}^2\\ 9\\text{ dm}^2 = 7\\dfrac{9}{100}\\text{ m}^2 = '
                        '7{,}09\\text{ m}^2$ và $3{,}4\\text{ ha} = 34\\,000\\text{ m}^2$.',
                        'Ta có $14\\text{ m}^2\\ 9\\text{ dm}^2 = 7\\dfrac{9}{100}\\text{ m}^2 = '
                        '7{,}09\\text{ m}^2$ và $3{,}4\\text{ ha} = 34\\,000\\text{ m}^2$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 16: Các đơn vị đo diện tích: Ta có $7\\text{ m}^2\\ '
                        '9\\text{ dm}^2 = 7\\dfrac{9}{100}\\text{ m}^2 = 7{,}09\\text{ m}^2$ và '
                        '$3{,}4\\text{ ha} = 34\\,000\\text{ m}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một căn phòng hình chữ nhật có diện tích $24\\text{ m}^2$. Người ta lát nền bằng các viên '
                 'gạch hình vuông có diện tích $16\\text{ dm}^2$. Hỏi cần bao nhiêu viên gạch để lát kín nền '
                 'phòng?',
            'answer': ['150'],
            'unit': None,
            'solution': 'Đổi $24\\text{ m}^2 = 2400\\text{ dm}^2$. Số viên gạch cần dùng là $2400 : 16 = '
                        '150$ (viên).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd03-don-vi-do-dien-tich',
  'context_title': 'Chủ đề 3: Một số đơn vị đo diện tích',
  'context': 'Chủ đề 3 · SGK Toán 5: Ki-lô-mét vuông, héc-ta và bảng đơn vị đo diện tích.',
  'title': 'Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại lượng',
  'icon': '🗺️',
  'description': 'Vận dụng các đơn vị đo diện tích, độ dài, khối lượng để giải bài toán thực tế về năng suất '
                 'và ước lượng.',
  'requirements': ['Ước lượng và lựa chọn đơn vị đo diện tích phù hợp với các đối tượng trong thực tiễn.',
                   'Giải được bài toán thực tế liên quan đến diện tích ruộng đất và sản lượng thu hoạch.',
                   'Vận dụng kiến thức của **Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại '
                   'lượng** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Khi giải bài toán có nhiều đơn vị đo khác nhau, bước đầu tiên là **đổi về cùng một đơn vị '
                'đo**.\n'
                '- Bài toán năng suất trên diện tích: Tổng thu hoạch = (Diện tích : Diện tích mẫu) $\\times$ '
                'Sản lượng mẫu.',
  'theory': '### 1. Lựa chọn đơn vị đo thích hợp\n'
            '- Diện tích mặt bàn: $\\text{dm}^2$ hoặc $\\text{m}^2$; diện tích phòng học: $\\text{m}^2$; '
            'diện tích trường học hoặc cánh đồng: $\\text{ha}$; diện tích tỉnh thành: $\\text{km}^2$.\n'
            '### 2. Bài toán thu hoạch trên diện tích đất\n'
            '- Đổi diện tích từ $\\text{ha}$ sang $\\text{m}^2$, tính số phần diện tích mẫu rồi nhân với '
            'khối lượng thu hoạch và đổi sang tạ, tấn.',
  'formulas': [{'category': 'Đổi đơn vị kết hợp',
                'items': [{'name': 'Diện tích và khối lượng',
                           'formula': '$1\\text{ ha} = 10\\,000\\text{ m}^2$; $1\\text{ tấn} = 10\\text{ tạ} '
                                      '= 1000\\text{ kg}$'}]}],
  'example': 'Một thửa ruộng rộng $2\\text{ ha}$. Trung bình cứ $100\\text{ m}^2$ thu được $65\\text{ kg}$ '
             'thóc. Hỏi cả thửa ruộng thu được bao nhiêu tấn thóc?',
  'example_answer': 'Đổi $2\\text{ ha} = 20\\,000\\text{ m}^2$. Số thóc thu được là $(20\\,000 : 100) '
                    '\\times 65 = 13\\,000\\text{ kg} = 13\\text{ tấn}$.',
  'real_life': 'Tính sản lượng lúa, ngô trên cánh đồng hoặc ước lượng chi phí mua giống cây trồng cho nông '
               'trại.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị thích hợp nhất để ghi diện tích nước Việt Nam là:',
            'options': ['$\\text{m}^2$', '$\\text{km}^2$', '$\\text{dm}^2$', '$\\text{cm}^2$'],
            'answer': 1,
            'solution': 'Diện tích quốc gia rất lớn nên đo bằng ki-lô-mét vuông ($\\text{km}^2$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một sân bóng đá tiêu chuẩn có diện tích khoảng $7000\\text{ m}^2$, tức là bằng:',
            'options': ['$7\\text{ ha}$', '$70\\text{ ha}$', '$0{,}7\\text{ ha}$', '$0{,}07\\text{ ha}$'],
            'answer': 2,
            'solution': 'Ta có $7000\\text{ m}^2 = \\dfrac{7000}{10\\,000}\\text{ ha} = 0{,}7\\text{ ha}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại lượng**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Diện tích và khối lượng**?',
            'options': ['$2\\text{ ha} = 10\\,000\\text{ m}^2$; $1\\text{ tấn} = 10\\text{ tạ} = 1000\\text{ '
                        'kg}$',
                        '$1\\text{ ha} = 10\\,000\\text{ m}^2$; $1\\text{ tấn} = 10\\text{ tạ} = 999\\text{ '
                        'kg}$',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)',
                        '$1\\text{ ha} = 10\\,000\\text{ m}^2$; $1\\text{ tấn} = 10\\text{ tạ} = 1000\\text{ '
                        'kg}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 17: Thực hành và trải nghiệm với một số đơn vị đo '
                        'đại lượng, **Diện tích và khối lượng** được xác định bởi: $1\\text{ ha} = '
                        '10\\,000\\text{ m}^2$; $1\\text{ tấn} = 10\\text{ tạ} = 1000\\text{ kg}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo định nghĩa trong **Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại lượng**, '
                 'khẳng định nào dưới đây là **đúng**?',
            'options': ['Khi giải bài toán có nhiều đơn vị đo khác nhau, bước đầu tiên là **đổi về cùng một '
                        'đơn vị đo**.',
                        'Khi giải bài toán có nhiều đơn vị đo khác nhau, bước đầu tiên là **đổi về cùng một '
                        'đơn vị đo**. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Khi giải bài toán có nhiều đơn vị đo khác nhau, bước đầu '
                        'tiên là **đổi về cùng một đơn vị đo**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Khi giải bài toán có nhiều đơn '
                        'vị đo khác nhau, bước đầu tiên là **đổi về cùng một đơn vị đo**.'],
            'answer': 0,
            'solution': 'Theo định nghĩa của Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại '
                        'lượng: Khi giải bài toán có nhiều đơn vị đo khác nhau, bước đầu tiên là **đổi về '
                        'cùng một đơn vị đo**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một khu đất rộng $5\\text{ ha}$, người ta dành $\\dfrac{2}{5}$ diện tích để đào hồ nước. '
                 'Diện tích hồ nước là:',
            'options': ['$2000\\text{ m}^2$',
                        '$20\\,000\\text{ m}^2$',
                        '$30\\,000\\text{ m}^2$',
                        '$200\\text{ m}^2$'],
            'answer': 1,
            'solution': 'Diện tích hồ là $5 \\times \\dfrac{2}{5} = 2\\text{ ha} = 20\\,000\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại '
                 'lượng**, nhận định nào sau đây là **chính xác**?',
            'options': ['Ước lượng và lựa chọn đơn vị đo diện tích phù hợp với các đối tượng trong thực '
                        'tiễn. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Ước lượng và lựa chọn đơn vị đo diện tích phù hợp với các '
                        'đối tượng trong thực tiễn.',
                        'Ước lượng và lựa chọn đơn vị đo diện tích phù hợp với các đối tượng trong thực '
                        'tiễn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Ước lượng và lựa chọn đơn vị đo '
                        'diện tích phù hợp với các đối tượng trong thực tiễn.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại '
                        'lượng: Ước lượng và lựa chọn đơn vị đo diện tích phù hợp với các đối tượng trong '
                        'thực tiễn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Diện tích một phòng học tiêu chuẩn thường khoảng $48\\text{ ha}$.',
            'answer': False,
            'solution': 'Phòng học có diện tích khoảng $48\\text{ m}^2$, còn $48\\text{ ha} = '
                        '480\\,000\\text{ m}^2$ là diện tích một khu đô thị lớn.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại lượng**, quy tắc **Diện '
                 'tích và khối lượng** được xác định bởi $1\\text{ ha} = 10\\,000\\text{ m}^2$; $1\\text{ '
                 'tấn} = 10\\text{ tạ} = 1000\\text{ kg}$ và khi áp dụng cho ví dụ “Một thửa ruộng rộng '
                 '$2\\text{ ha}$. Trung bình cứ $100\\text{ m}^2$ thu được $65\\text{ kg}$ thóc. Hỏi cả thửa '
                 'ruộng thu được bao nhiêu tấ...” ta có lời giải: Đổi $2\\text{ ha} = 20\\,000\\text{ m}^2$. '
                 'Số thóc thu được là $(20\\,000 : 100) \\times 65 = 13\\,000\\text{ kg} = 13\\text{ tấn}$.. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Diện tích và khối lượng** ($1\\text{ ha} '
                        '= 10\\,000\\text{ m}^2$; $1\\text{ tấn} = 10\\text{ tạ} = 1000\\text{ kg}$) và lời '
                        'giải ví dụ minh họa của Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại '
                        'lượng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 17: Thực hành và trải nghiệm với một số đơn vị đo '
                 'đại lượng** để giải bài toán sau: Một thửa ruộng rộng $2\\text{ ha}$. Trung bình cứ '
                 '$100\\text{ m}^2$ thu được $65\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu được bao nhiêu tấn '
                 'thóc? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đổi $2\\text{ ha} = 20\\,000\\text{ m}^2$. Số thóc thu được là $(20\\,000 : 100) : '
                        '65 = 13\\,000\\text{ kg} = 13\\text{ tấn}$.',
                        'Đổi $2\\text{ ha} = 20\\,000\\text{ m}^2$. Số thóc thu được là $(20\\,000 : 100) '
                        '\\times 65 = 13\\,000\\text{ kg} = 12\\text{ tấn}$.',
                        'Đổi $4\\text{ ha} = 20\\,000\\text{ m}^2$. Số thóc thu được là $(20\\,000 : 100) '
                        '\\times 65 = 13\\,000\\text{ kg} = 13\\text{ tấn}$.',
                        'Đổi $2\\text{ ha} = 20\\,000\\text{ m}^2$. Số thóc thu được là $(20\\,000 : 100) '
                        '\\times 65 = 13\\,000\\text{ kg} = 13\\text{ tấn}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 17: Thực hành và trải nghiệm với một số đơn vị đo đại '
                        'lượng: Đổi $2\\text{ ha} = 20\\,000\\text{ m}^2$. Số thóc thu được là $(20\\,000 : '
                        '100) \\times 65 = 13\\,000\\text{ kg} = 13\\text{ tấn}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thửa ruộng có diện tích $3\\text{ ha}$. Trung bình cứ $100\\text{ m}^2$ thu hoạch được '
                 '$60\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tấn thóc?',
            'answer': ['18'],
            'unit': None,
            'solution': 'Đổi $3\\text{ ha} = 30\\,000\\text{ m}^2$. Số thóc thu được là $(30\\,000 : 100) '
                        '\\times 60 = 18\\,000\\text{ kg} = 18\\text{ tấn}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd04-phep-tinh-so-thap-phan',
  'context_title': 'Chủ đề 4: Các phép tính với số thập phân',
  'context': 'Chủ đề 4 · SGK Toán 5: Cộng, trừ, nhân, chia số thập phân và tính nhẩm với 10, 100, 1000.',
  'title': 'Bài 19: Phép cộng số thập phân',
  'icon': '🧮',
  'description': 'Quy tắc đặt tính và thực hiện phép cộng hai hay nhiều số thập phân, tính chất của phép '
                 'cộng số thập phân.',
  'requirements': ['Đặt tính và thực hiện đúng phép cộng các số thập phân.',
                   'Vận dụng tính chất giao hoán và kết hợp của phép cộng số thập phân để tính bằng cách '
                   'thuận tiện.',
                   'Vận dụng kiến thức của **Bài 19: Phép cộng số thập phân** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Muốn **cộng hai số thập phân**, ta viết số hạng này dưới số hạng kia sao cho các chữ số ở '
                'cùng một hàng đặt thẳng cột với nhau (**dấu phẩy thẳng cột**), cộng như cộng các số tự '
                'nhiên rồi viết dấu phẩy ở tổng thẳng cột với các dấu phẩy của các số hạng.',
  'theory': '### 1. Quy tắc đặt tính\n'
            '- Nếu số chữ số ở phần thập phân không bằng nhau, có thể viết thêm chữ số $0$ vào bên phải phần '
            'thập phân để dễ cộng: $15{,}6 + 7{,}48 = 15{,}60 + 7{,}48 = 23{,}08$.\n'
            '### 2. Tính chất của phép cộng số thập phân\n'
            '- Giao hoán: $a + b = b + a$. Kết hợp: $(a + b) + c = a + (b + c)$. Cộng với $0$: $a + 0 = 0 + '
            'a = a$.',
  'formulas': [{'category': 'Phép cộng số thập phân',
                'items': [{'name': 'Quy tắc cốt lõi',
                           'formula': 'Đặt các dấu phẩy thẳng cột $\\rightarrow$ Cộng như số tự nhiên '
                                      '$\\rightarrow$ Hạ dấu phẩy thẳng cột'},
                          {'name': 'Tính chất kết hợp', 'formula': '$(a + b) + c = a + (b + c)$'}]}],
  'example': 'Tính bằng cách thuận tiện nhất: $4{,}68 + 6{,}03 + 3{,}32$.',
  'example_answer': 'Ta có $(4{,}68 + 3{,}32) + 6{,}03 = 8 + 6{,}03 = 14{,}03$.',
  'real_life': 'Cộng khối lượng các túi trái cây hoặc tính tổng chiều dài các cuộn dây điện.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $12{,}5 + 3{,}47$ là:',
            'options': ['$16{,}22$', '$4{,}72$', '$15{,}97$', '$15{,}52$'],
            'answer': 2,
            'solution': 'Đặt thẳng dấu phẩy: $12{,}50 + 3{,}47 = 15{,}97$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng của $0{,}8$ và $1{,}2$ bằng:',
            'options': ['$0{,}20$', '$20$', '$1{,}10$', '$2$'],
            'answer': 3,
            'solution': 'Ta có $0{,}8 + 1{,}2 = 2{,}0 = 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Phép cộng số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Quy tắc cốt lõi**?',
            'options': ['Đặt các dấu phẩy thẳng cột $\\rightarrow$ Cộng như số tự nhiên $\\rightarrow$ Hạ '
                        'dấu phẩy thẳng cột',
                        'Đặt các dấu phẩy thẳng cột $\\rightarrow$ Cộng như số tự nhiên $\\rightarrow$ Hạ '
                        'dấu phẩy thẳng cột (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đặt các dấu phẩy thẳng cột $\\rightarrow$ Cộng như số tự '
                        'nhiên $\\rightarrow$ Hạ dấu phẩy thẳng cột',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt các dấu phẩy thẳng cột '
                        '$\\rightarrow$ Cộng như số tự nhiên $\\rightarrow$ Hạ dấu phẩy thẳng cột'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 19: Phép cộng số thập phân, **Quy tắc cốt lõi** '
                        'được xác định bởi: Đặt các dấu phẩy thẳng cột $\\rightarrow$ Cộng như số tự nhiên '
                        '$\\rightarrow$ Hạ dấu phẩy thẳng cột.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Phép cộng số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Tính chất kết hợp**?',
            'options': ['$(a - b) + c = a + (b + c)$',
                        '$(a + b) + c = a + (b + c)$',
                        'Đảo ngược vế của quy tắc: $(a + b) + c = a + (b + c)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $(a + b) + c = a + (b + c)$'],
            'answer': 1,
            'solution': 'Trong Bài 19: Phép cộng số thập phân, **Tính chất kết hợp** có công thức/quy tắc '
                        'là: $(a + b) + c = a + (b + c)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tính hợp lí biểu thức $3{,}75 + 4{,}8 + 6{,}25$ ta được kết quả là:',
            'options': ['$13{,}8$', '$14{,}08$', '$14{,}8$', '$15{,}8$'],
            'answer': 2,
            'solution': 'Nhóm $(3{,}75 + 6{,}25) + 4{,}8 = 10 + 4{,}8 = 14{,}8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 19: Phép cộng số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Đặt tính và thực hiện đúng phép cộng các số thập phân. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đặt tính và thực hiện đúng phép cộng các số thập phân.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt tính và thực hiện đúng phép '
                        'cộng các số thập phân.',
                        'Đặt tính và thực hiện đúng phép cộng các số thập phân.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 19: Phép cộng số thập phân: Đặt tính và thực hiện '
                        'đúng phép cộng các số thập phân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Khi đặt tính cộng hai số thập phân, ta phải đặt chữ số cuối cùng bên phải của hai số thẳng '
                 'cột với nhau.',
            'answer': False,
            'solution': 'Khi cộng hai số thập phân, ta phải đặt các dấu phẩy và các chữ số cùng hàng thẳng '
                        'cột với nhau.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 19: Phép cộng số thập phân**, quy tắc **Quy tắc cốt lõi** được xác định bởi '
                 'Đặt các dấu phẩy thẳng cột $\\rightarrow$ Cộng như số tự nhiên $\\rightarrow$ Hạ dấu phẩy '
                 'thẳng cột và khi áp dụng cho ví dụ “Tính bằng cách thuận tiện nhất: $4{,}68 + 6{,}03 + '
                 '3{,}32$.” ta có lời giải: Ta có $(4{,}68 + 3{,}32) + 6{,}03 = 8 + 6{,}03 = 14{,}03$.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quy tắc cốt lõi** (Đặt các dấu phẩy '
                        'thẳng cột $\\rightarrow$ Cộng như số tự nhiên $\\rightarrow$ Hạ dấu phẩy thẳng cột) '
                        'và lời giải ví dụ minh họa của Bài 19: Phép cộng số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 19: Phép cộng số thập phân** để giải bài toán sau: '
                 'Tính bằng cách thuận tiện nhất: $4{,}68 + 6{,}03 + 3{,}32$. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $(4{,}68 + 3{,}32) + 6{,}03 = 8 + 6{,}03 = 14{,}03$.',
                        'Ta có $(4{,}68 - 3{,}32) + 6{,}03 = 8 + 6{,}03 = 14{,}03$.',
                        'Ta có $(4{,}68 + 3{,}32) + 6{,}03 = 8 + 6{,}03 = 14{,}2$.',
                        'Ta có $(8{,}68 + 3{,}32) + 6{,}03 = 8 + 6{,}03 = 14{,}03$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Phép cộng số thập phân: Ta có $(4{,}68 + 3{,}32) + '
                        '6{,}03 = 8 + 6{,}03 = 14{,}03$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình tam giác có độ dài ba cạnh lần lượt là $4{,}5\\text{ cm}$; $5{,}2\\text{ cm}$ và '
                 '$6{,}3\\text{ cm}$. Tính chu vi hình tam giác đó (đơn vị cm).',
            'answer': ['16'],
            'unit': None,
            'solution': 'Chu vi hình tam giác là $4{,}5 + 5{,}2 + 6{,}3 = 16$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd04-phep-tinh-so-thap-phan',
  'context_title': 'Chủ đề 4: Các phép tính với số thập phân',
  'context': 'Chủ đề 4 · SGK Toán 5: Cộng, trừ, nhân, chia số thập phân và tính nhẩm với 10, 100, 1000.',
  'title': 'Bài 20: Phép trừ số thập phân',
  'icon': '🧮',
  'description': 'Quy tắc trừ hai số thập phân và cách xử lí khi số chữ số ở phần thập phân của số bị trừ ít '
                 'hơn số trừ.',
  'requirements': ['Thực hiện được phép trừ hai số thập phân hoặc trừ một số tự nhiên cho một số thập phân.',
                   'Giải được bài toán tìm thành phần chưa biết và bài toán có lời văn liên quan đến phép '
                   'trừ số thập phân.',
                   'Vận dụng kiến thức của **Bài 20: Phép trừ số thập phân** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': '- Muốn **trừ một số thập phân cho một số thập phân**, ta viết số trừ dưới số bị trừ sao cho '
                'các chữ số ở cùng một hàng đặt thẳng cột với nhau, trừ như trừ các số tự nhiên rồi viết dấu '
                'phẩy ở hiệu thẳng cột với các dấu phẩy.',
  'theory': '### 1. Khi số bị trừ có ít chữ số thập phân hơn số trừ\n'
            '- Ta viết thêm chữ số $0$ vào bên phải phần thập phân của số bị trừ rồi trừ: $25{,}3 - 8{,}47 = '
            '25{,}30 - 8{,}47 = 16{,}83$.\n'
            '- Nếu số bị trừ là số tự nhiên: $20 - 7{,}35 = 20{,}00 - 7{,}35 = 12{,}65$.\n'
            '### 2. Trừ một số cho một tổng\n'
            '- Quy tắc: $a - (b + c) = a - b - c$.',
  'formulas': [{'category': 'Phép trừ số thập phân',
                'items': [{'name': 'Bổ sung chữ số 0',
                           'formula': 'Viết thêm chữ số $0$ vào bên phải phần thập phân của số bị trừ nếu '
                                      'thiếu'},
                          {'name': 'Một số trừ một tổng', 'formula': '$a - (b + c) = a - b - c$'}]}],
  'example': 'Đặt tính và tính: $42 - 15{,}68$.',
  'example_answer': 'Viết $42 = 42{,}00$, thực hiện phép trừ $42{,}00 - 15{,}68 = 26{,}32$.',
  'real_life': 'Tính lượng hàng còn lại trong kho hoặc tính số chiều dài dây còn lại sau khi cắt.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $18{,}5 - 6{,}2$ là:',
            'options': ['$12{,}7$', '$11{,}3$', '$24{,}7$', '$12{,}3$'],
            'answer': 3,
            'solution': 'Ta có $18{,}5 - 6{,}2 = 12{,}3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $10 - 3{,}6$ là:',
            'options': ['$6{,}4$', '$7{,}4$', '$6{,}6$', '$7{,}6$'],
            'answer': 0,
            'solution': 'Viết $10 = 10{,}0$, ta có $10{,}0 - 3{,}6 = 6{,}4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Phép trừ số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Bổ sung chữ số 0**?',
            'options': ['Viết thêm chữ số $1$ vào bên phải phần thập phân của số bị trừ nếu thiếu',
                        'Viết thêm chữ số $0$ vào bên phải phần thập phân của số bị trừ nếu thiếu',
                        'Viết thêm chữ số $2$ vào bên phải phần thập phân của số bị trừ nếu thiếu',
                        '$a - (b + c) = a - b - c$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 20: Phép trừ số thập phân, **Bổ sung chữ số 0** '
                        'được xác định bởi: Viết thêm chữ số $0$ vào bên phải phần thập phân của số bị trừ '
                        'nếu thiếu.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Phép trừ số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Một số trừ một tổng**?',
            'options': ['$a - (b - c) = a - b - c$',
                        'Đảo ngược vế của quy tắc: $a - (b + c) = a - b - c$',
                        '$a - (b + c) = a - b - c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a - (b + c) = a - b - c$'],
            'answer': 2,
            'solution': 'Trong Bài 20: Phép trừ số thập phân, **Một số trừ một tổng** có công thức/quy tắc '
                        'là: $a - (b + c) = a - b - c$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x + 4{,}72 = 12{,}5$:',
            'options': ['$8{,}22$', '$7{,}88$', '$17{,}22$', '$7{,}78$'],
            'answer': 3,
            'solution': 'Ta có $x = 12{,}50 - 4{,}72 = 7{,}78$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 20: Phép trừ số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Thực hiện được phép trừ hai số thập phân hoặc trừ một số tự nhiên cho một số thập '
                        'phân.',
                        'Thực hiện được phép trừ hai số thập phân hoặc trừ một số tự nhiên cho một số thập '
                        'phân. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép trừ hai số thập phân hoặc trừ một số '
                        'tự nhiên cho một số thập phân.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép trừ hai số '
                        'thập phân hoặc trừ một số tự nhiên cho một số thập phân.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 20: Phép trừ số thập phân: Thực hiện được phép trừ '
                        'hai số thập phân hoặc trừ một số tự nhiên cho một số thập phân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Kết quả của phép tính $20 - 7{,}35$ bằng $12{,}65$.',
            'answer': True,
            'solution': 'Ta có $20{,}00 - 7{,}35 = 12{,}65$ (thử lại $12{,}65 + 7{,}35 = 20$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 20: Phép trừ số thập phân**, quy tắc **Bổ sung chữ số 0** được xác định bởi '
                 'Viết thêm chữ số $0$ vào bên phải phần thập phân của số bị trừ nếu thiếu và khi áp dụng '
                 'cho ví dụ “Đặt tính và tính: $42 - 15{,}68$.” ta có lời giải: Viết $42 = 42{,}00$, thực '
                 'hiện phép trừ $42{,}00 - 15{,}68 = 26{,}32$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Bổ sung chữ số 0** (Viết thêm chữ số $0$ '
                        'vào bên phải phần thập phân của số bị trừ nếu thiếu) và lời giải ví dụ minh họa của '
                        'Bài 20: Phép trừ số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 20: Phép trừ số thập phân** để giải bài toán sau: '
                 'Đặt tính và tính: $42 - 15{,}68$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Viết $42 = 42{,}00$, thực hiện phép trừ $42{,}00 + 15{,}68 = 26{,}32$.',
                        'Viết $42 = 42{,}00$, thực hiện phép trừ $42{,}00 - 15{,}68 = 26{,}32$.',
                        'Viết $42 = 42{,}00$, thực hiện phép trừ $42{,}00 - 15{,}68 = 26{,}31$.',
                        'Viết $84 = 42{,}00$, thực hiện phép trừ $42{,}00 - 15{,}68 = 26{,}32$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Phép trừ số thập phân: Viết $42 = 42{,}00$, thực '
                        'hiện phép trừ $42{,}00 - 15{,}68 = 26{,}32$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thùng đựng $25{,}5\\text{ l}$ dầu. Người ta lấy ra lần đầu $6{,}75\\text{ l}$ và lần '
                 'sau $8{,}25\\text{ l}$. Hỏi trong thùng còn lại bao nhiêu lít dầu?',
            'answer': ['10,5', '10.5'],
            'unit': None,
            'solution': 'Số dầu đã lấy ra là $6{,}75 + 8{,}25 = 15\\text{ l}$. Số dầu còn lại là $25{,}5 - '
                        '15 = 10{,}5\\text{ l}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd04-phep-tinh-so-thap-phan',
  'context_title': 'Chủ đề 4: Các phép tính với số thập phân',
  'context': 'Chủ đề 4 · SGK Toán 5: Cộng, trừ, nhân, chia số thập phân và tính nhẩm với 10, 100, 1000.',
  'title': 'Bài 21: Phép nhân số thập phân',
  'icon': '🧮',
  'description': 'Quy tắc nhân một số thập phân với một số tự nhiên và nhân một số thập phân với một số thập '
                 'phân.',
  'requirements': ['Thực hiện đúng phép nhân số thập phân và xác định chính xác vị trí dấu phẩy ở tích.',
                   'Vận dụng tính chất giao hoán, kết hợp, phân phối của phép nhân để tính hợp lí.',
                   'Vận dụng kiến thức của **Bài 21: Phép nhân số thập phân** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Muốn **nhân hai số thập phân**, ta thực hiện nhân như nhân các số tự nhiên, sau đó **đếm '
                'xem trong phần thập phân của cả hai thừa số có bao nhiêu chữ số** rồi dùng dấu phẩy tách ở '
                'tích ra bấy nhiêu chữ số kể từ phải sang trái.',
  'theory': '### 1. Nhân số thập phân với số tự nhiên và với số thập phân\n'
            '- Ví dụ 1: $1{,}2 \\times 3 = 3{,}6$ ($1$ chữ số ở phần thập phân).\n'
            '- Ví dụ 2: $2{,}4 \\times 1{,}5 = 3{,}60 = 3{,}6$ (tổng cộng $1 + 1 = 2$ chữ số ở phần thập '
            'phân).\n'
            '- Ví dụ 3: $0{,}25 \\times 0{,}4 = 0{,}100 = 0{,}1$ (tổng cộng $2 + 1 = 3$ chữ số ở phần thập '
            'phân).',
  'formulas': [{'category': 'Quy tắc đếm chữ số thập phân',
                'items': [{'name': 'Vị trí dấu phẩy ở tích',
                           'formula': 'Số chữ số phần thập phân của tích = Tổng số chữ số phần thập phân của '
                                      'hai thừa số'},
                          {'name': 'Tính chất phân phối',
                           'formula': '$a \\times b + a \\times c = a \\times (b + c)$'}]}],
  'example': 'Tính giá trị biểu thức: $3{,}6 \\times 7{,}2 + 3{,}6 \\times 2{,}8$.',
  'example_answer': 'Ta có $3{,}6 \\times (7{,}2 + 2{,}8) = 3{,}6 \\times 10 = 36$.',
  'real_life': 'Tính tiền mua $2{,}5\\text{ kg}$ táo hoặc tính diện tích hình chữ nhật có kích thước là số '
               'thập phân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $1{,}2 \\times 3$ là:',
            'options': ['$3{,}6$', '$36$', '$0{,}36$', '$4{,}2$'],
            'answer': 0,
            'solution': 'Ta có $12 \\times 3 = 36$, tách $1$ chữ số ở phần thập phân được $3{,}6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tích của $2{,}5 \\times 0{,}4$ bằng:',
            'options': ['$10$', '$1$', '$0{,}1$', '$0{,}01$'],
            'answer': 1,
            'solution': 'Ta có $25 \\times 4 = 100$, tách $2$ chữ số ở phần thập phân được $1{,}00 = 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Phép nhân số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Vị trí dấu phẩy ở tích**?',
            'options': ['Số chữ số phần thập phân của tích = Tổng số chữ số phần thập phân của hai thừa số '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Số chữ số phần thập phân của tích = Tổng số chữ số phần '
                        'thập phân của hai thừa số',
                        'Số chữ số phần thập phân của tích = Tổng số chữ số phần thập phân của hai thừa số',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Số chữ số phần thập phân của '
                        'tích = Tổng số chữ số phần thập phân của hai thừa số'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 21: Phép nhân số thập phân, **Vị trí dấu phẩy ở '
                        'tích** được xác định bởi: Số chữ số phần thập phân của tích = Tổng số chữ số phần '
                        'thập phân của hai thừa số.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Phép nhân số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Tính chất phân phối**?',
            'options': ['$a \\times b - a \\times c = a \\times (b + c)$',
                        'Đảo ngược vế của quy tắc: $a \\times b + a \\times c = a \\times (b + c)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a \\times b + a \\times c = a '
                        '\\times (b + c)$',
                        '$a \\times b + a \\times c = a \\times (b + c)$'],
            'answer': 3,
            'solution': 'Trong Bài 21: Phép nhân số thập phân, **Tính chất phân phối** có công thức/quy tắc '
                        'là: $a \\times b + a \\times c = a \\times (b + c)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một mảnh vườn hình chữ nhật có chiều dài $8{,}5\\text{ m}$ và chiều rộng $4{,}2\\text{ '
                 'm}$. Diện tích mảnh vườn là:',
            'options': ['$35{,}7\\text{ m}^2$',
                        '$357\\text{ m}^2$',
                        '$25{,}4\\text{ m}^2$',
                        '$3{,}57\\text{ m}^2$'],
            'answer': 0,
            'solution': 'Diện tích mảnh vườn là $8{,}5 \\times 4{,}2 = 35{,}70 = 35{,}7\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 21: Phép nhân số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Thực hiện đúng phép nhân số thập phân và xác định chính xác vị trí dấu phẩy ở tích. '
                        '(với dấu ngược lại)',
                        'Thực hiện đúng phép nhân số thập phân và xác định chính xác vị trí dấu phẩy ở tích.',
                        'Đảo ngược vế của quy tắc: Thực hiện đúng phép nhân số thập phân và xác định chính '
                        'xác vị trí dấu phẩy ở tích.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện đúng phép nhân số '
                        'thập phân và xác định chính xác vị trí dấu phẩy ở tích.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 21: Phép nhân số thập phân: Thực hiện đúng phép nhân '
                        'số thập phân và xác định chính xác vị trí dấu phẩy ở tích.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Tích của hai số thập phân $0{,}15$ và $0{,}3$ có phần thập phân gồm $3$ chữ số (khi chưa '
                 'rút gọn chữ số $0$).',
            'answer': True,
            'solution': 'Số $0{,}15$ có $2$ chữ số thập phân, $0{,}3$ có $1$ chữ số thập phân nên tích '
                        '$0{,}045$ có $2 + 1 = 3$ chữ số thập phân.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 21: Phép nhân số thập phân**, quy tắc **Vị trí dấu phẩy ở tích** được xác định '
                 'bởi Số chữ số phần thập phân của tích = Tổng số chữ số phần thập phân của hai thừa số và '
                 'khi áp dụng cho ví dụ “Tính giá trị biểu thức: $3{,}6 \\times 7{,}2 + 3{,}6 \\times '
                 '2{,}8$.” ta có lời giải: Ta có $3{,}6 \\times (7{,}2 + 2{,}8) = 3{,}6 \\times 10 = 36$.. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Vị trí dấu phẩy ở tích** (Số chữ số phần '
                        'thập phân của tích = Tổng số chữ số phần thập phân của hai thừa số) và lời giải ví '
                        'dụ minh họa của Bài 21: Phép nhân số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 21: Phép nhân số thập phân** để giải bài toán sau: '
                 'Tính giá trị biểu thức: $3{,}6 \\times 7{,}2 + 3{,}6 \\times 2{,}8$. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $3{,}6 \\times (7{,}2 - 2{,}8) = 3{,}6 \\times 10 = 36$.',
                        'Ta có $3{,}6 \\times (7{,}2 + 2{,}8) = 3{,}6 \\times 10 = 35$.',
                        'Ta có $3{,}6 \\times (7{,}2 + 2{,}8) = 3{,}6 \\times 10 = 36$.',
                        'Ta có $6{,}6 \\times (7{,}2 + 2{,}8) = 3{,}6 \\times 10 = 36$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Phép nhân số thập phân: Ta có $3{,}6 \\times (7{,}2 '
                        '+ 2{,}8) = 3{,}6 \\times 10 = 36$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mẹ mua $2{,}5\\text{ kg}$ cam, mỗi ki-lô-gam cam giá $36$ nghìn đồng. Hỏi mẹ phải trả bao '
                 'nhiêu nghìn đồng?',
            'answer': ['90'],
            'unit': None,
            'solution': 'Số tiền mẹ phải trả là $36 \\times 2{,}5 = 90$ (nghìn đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd04-phep-tinh-so-thap-phan',
  'context_title': 'Chủ đề 4: Các phép tính với số thập phân',
  'context': 'Chủ đề 4 · SGK Toán 5: Cộng, trừ, nhân, chia số thập phân và tính nhẩm với 10, 100, 1000.',
  'title': 'Bài 22: Phép chia số thập phân',
  'icon': '🧮',
  'description': 'Chia một số thập phân cho một số tự nhiên và chia một số cho một số thập phân.',
  'requirements': ['Thực hiện được phép chia số thập phân cho số tự nhiên và biết đặt dấu phẩy ở thương đúng '
                   'lúc.',
                   'Chuyển được phép chia cho số thập phân về phép chia cho số tự nhiên bằng cách dời dấu '
                   'phẩy.',
                   'Vận dụng kiến thức của **Bài 22: Phép chia số thập phân** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Khi chia một số thập phân cho một số tự nhiên, ta chia phần nguyên trước; **trước khi lấy '
                'chữ số đầu tiên ở phần thập phân** của số bị chia để tiếp tục chia thì ta **viết dấu phẩy '
                'vào bên phải thương**.\n'
                '- Khi chia cho một số thập phân, ta đếm phần thập phân của số chia có bao nhiêu chữ số thì '
                '**chuyển dấu phẩy ở số bị chia sang bên phải** bấy nhiêu chữ số (hoặc thêm chữ số $0$) rồi '
                'bỏ dấu phẩy ở số chia để chia.',
  'theory': '### 1. Chia số thập phân cho số tự nhiên\n'
            '- Ví dụ: $8{,}4 : 4 = 2{,}1$; phép chia hai số tự nhiên mà thương là số thập phân: $15 : 4 = '
            '3{,}75$.\n'
            '### 2. Chia một số cho một số thập phân\n'
            '- Ví dụ 1: $9 : 0{,}6 = 90 : 6 = 15$.\n'
            '- Ví dụ 2: $12{,}6 : 0{,}35 = 1260 : 35 = 36$.',
  'formulas': [{'category': 'Quy tắc chia số thập phân',
                'items': [{'name': 'Chia cho số tự nhiên',
                           'formula': 'Chia hết phần nguyên $\\rightarrow$ Đặt dấu phẩy vào thương '
                                      '$\\rightarrow$ Hạ phần thập phân'},
                          {'name': 'Chia cho số thập phân',
                           'formula': '$a : b = (a \\times 10^n) : (b \\times 10^n)$ để đưa số chia thành số '
                                      'tự nhiên'}]}],
  'example': 'Tính: $7{,}2 : 0{,}8$ và $4{,}5 : 0{,}15$.',
  'example_answer': 'Ta có $7{,}2 : 0{,}8 = 72 : 8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 30$.',
  'real_life': 'Chia đều một cuộn vải dài $22{,}5\\text{ m}$ thành các mảnh dài $1{,}5\\text{ m}$ để may áo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $8{,}4 : 4$ là:',
            'options': ['$21$', '$2{,}1$', '$0{,}21$', '$2{,}4$'],
            'answer': 1,
            'solution': 'Ta có $8 : 4 = 2$, viết dấu phẩy, $4 : 4 = 1$ nên thương là $2{,}1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $7{,}2 : 0{,}8$ là:',
            'options': ['$0{,}9$', '$90$', '$9$', '$5{,}76$'],
            'answer': 2,
            'solution': 'Dời dấu phẩy sang phải $1$ chữ số: $72 : 8 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Phép chia số thập phân**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Chia cho số tự nhiên**?',
            'options': ['Chia hết phần nguyên $\\rightarrow$ Đặt dấu phẩy vào thương $\\rightarrow$ Hạ phần '
                        'thập phân (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Chia hết phần nguyên $\\rightarrow$ Đặt dấu phẩy vào '
                        'thương $\\rightarrow$ Hạ phần thập phân',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chia hết phần nguyên '
                        '$\\rightarrow$ Đặt dấu phẩy vào thương $\\rightarrow$ Hạ phần thập phân',
                        'Chia hết phần nguyên $\\rightarrow$ Đặt dấu phẩy vào thương $\\rightarrow$ Hạ phần '
                        'thập phân'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 22: Phép chia số thập phân, **Chia cho số tự '
                        'nhiên** được xác định bởi: Chia hết phần nguyên $\\rightarrow$ Đặt dấu phẩy vào '
                        'thương $\\rightarrow$ Hạ phần thập phân.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Phép chia số thập phân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Chia cho số thập phân**?',
            'options': ['$a : b = (a \\times 10^n) : (b \\times 10^n)$ để đưa số chia thành số tự nhiên',
                        '$a : b = (a : 10^n) : (b \\times 10^n)$ để đưa số chia thành số tự nhiên',
                        '$a : b = (a \\times 10^n) : (b \\times 9^n)$ để đưa số chia thành số tự nhiên',
                        '$a : b = (a \\times 20^n) : (b \\times 10^n)$ để đưa số chia thành số tự nhiên'],
            'answer': 0,
            'solution': 'Trong Bài 22: Phép chia số thập phân, **Chia cho số thập phân** có công thức/quy '
                        'tắc là: $a : b = (a \\times 10^n) : (b \\times 10^n)$ để đưa số chia thành số tự '
                        'nhiên.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thương của phép chia $4{,}5 : 0{,}15$ bằng:',
            'options': ['$3$', '$30$', '$0{,}3$', '$300$'],
            'answer': 1,
            'solution': 'Dời dấu phẩy sang phải $2$ chữ số: $450 : 15 = 30$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 22: Phép chia số thập phân**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Thực hiện được phép chia số thập phân cho số tự nhiên và biết đặt dấu phẩy ở thương '
                        'đúng lúc. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép chia số thập phân cho số tự nhiên và '
                        'biết đặt dấu phẩy ở thương đúng lúc.',
                        'Thực hiện được phép chia số thập phân cho số tự nhiên và biết đặt dấu phẩy ở thương '
                        'đúng lúc.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép chia số '
                        'thập phân cho số tự nhiên và biết đặt dấu phẩy ở thương đúng lúc.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 22: Phép chia số thập phân: Thực hiện được phép chia '
                        'số thập phân cho số tự nhiên và biết đặt dấu phẩy ở thương đúng lúc.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Phép chia $18 : 24$ có thương là $0{,}75$.',
            'answer': True,
            'solution': 'Ta có $18 : 24 = \\dfrac{3}{4} = 0{,}75$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 22: Phép chia số thập phân**, quy tắc **Chia cho số tự nhiên** được xác định '
                 'bởi Chia hết phần nguyên $\\rightarrow$ Đặt dấu phẩy vào thương $\\rightarrow$ Hạ phần '
                 'thập phân và khi áp dụng cho ví dụ “Tính: $7{,}2 : 0{,}8$ và $4{,}5 : 0{,}15$.” ta có lời '
                 'giải: Ta có $7{,}2 : 0{,}8 = 72 : 8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 30$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Chia cho số tự nhiên** (Chia hết phần '
                        'nguyên $\\rightarrow$ Đặt dấu phẩy vào thương $\\rightarrow$ Hạ phần thập phân) và '
                        'lời giải ví dụ minh họa của Bài 22: Phép chia số thập phân.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 22: Phép chia số thập phân** để giải bài toán sau: '
                 'Tính: $7{,}2 : 0{,}8$ và $4{,}5 : 0{,}15$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $8{,}2 : 0{,}8 = 72 : 8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 30$.',
                        'Ta có $7{,}2 : 0{,}8 = 72 : 8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 29$.',
                        'Ta có $14{,}2 : 0{,}8 = 72 : 8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 30$.',
                        'Ta có $7{,}2 : 0{,}8 = 72 : 8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 30$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Phép chia số thập phân: Ta có $7{,}2 : 0{,}8 = 72 : '
                        '8 = 9$ và $4{,}5 : 0{,}15 = 450 : 15 = 30$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tấm vải dài $22{,}5\\text{ m}$ được cắt thành các mảnh bằng nhau, mỗi mảnh dài '
                 '$1{,}5\\text{ m}$. Hỏi cắt được tất cả bao nhiêu mảnh vải?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Số mảnh vải cắt được là $22{,}5 : 1{,}5 = 225 : 15 = 15$ (mảnh).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd04-phep-tinh-so-thap-phan',
  'context_title': 'Chủ đề 4: Các phép tính với số thập phân',
  'context': 'Chủ đề 4 · SGK Toán 5: Cộng, trừ, nhân, chia số thập phân và tính nhẩm với 10, 100, 1000.',
  'title': 'Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; 0,01; 0,001',
  'icon': '🧮',
  'description': 'Quy tắc dời dấu phẩy khi nhân hoặc chia nhẩm một số thập phân với 10; 100; 1000 hoặc với '
                 '0,1; 0,01; 0,001.',
  'requirements': ['Tính nhẩm nhanh tích và thương của số thập phân với $10; 100; 1000; \\dots$ và với '
                   '$0{,}1; 0{,}01; 0{,}001; \\dots$',
                   'Vận dụng tính nhẩm để đổi đơn vị đo và giải bài toán thực tế.',
                   'Vận dụng kiến thức của **Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; '
                   '0,01; 0,001** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Nhân một số thập phân với $10; 100; 1000; \\dots$ (hoặc chia cho $0{,}1; 0{,}01; 0{,}001; '
                '\\dots$): ta chuyển dấu phẩy sang **bên phải** một, hai, ba, ... chữ số.\n'
                '- Chia một số thập phân cho $10; 100; 1000; \\dots$ (hoặc nhân với $0{,}1; 0{,}01; 0{,}001; '
                '\\dots$): ta chuyển dấu phẩy sang **bên trái** một, hai, ba, ... chữ số.',
  'theory': '### 1. Chuyển dấu phẩy sang bên phải\n'
            '- $3{,}72 \\times 100 = 372$; $4{,}5 : 0{,}1 = 4{,}5 \\times 10 = 45$.\n'
            '### 2. Chuyển dấu phẩy sang bên trái\n'
            '- $36{,}8 : 100 = 0{,}368$; $45{,}6 \\times 0{,}01 = 0{,}456$.',
  'formulas': [{'category': 'Quy tắc dời dấu phẩy',
                'items': [{'name': 'Dời sang phải 1, 2, 3 chữ số',
                           'formula': 'Khi $\\times 10; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}001$'},
                          {'name': 'Dời sang trái 1, 2, 3 chữ số',
                           'formula': 'Khi $: 10; 100; 1000$ hoặc $\\times 0{,}1; 0{,}01; 0{,}001$'}]}],
  'example': 'Tính nhẩm: $0{,}75 \\times 100$; $24{,}5 \\times 0{,}1$ và $1{,}8 : 0{,}01$.',
  'example_answer': 'Ta có $0{,}75 \\times 100 = 75$; $24{,}5 \\times 0{,}1 = 2{,}45$ và $1{,}8 : 0{,}01 = '
                    '180$.',
  'real_life': 'Tính nhanh lượng xăng tiêu thụ của ô tô trên $100\\text{ km}$ và quy đổi tiền tệ, đơn vị đo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính nhẩm $4{,}5 \\times 10$ là:',
            'options': ['$0{,}45$', '$450$', '$45$', '$4{,}05$'],
            'answer': 2,
            'solution': 'Nhân với $10$ ta dời dấu phẩy sang phải $1$ chữ số được $45$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính nhẩm $36{,}8 : 100$ là:',
            'options': ['$3680$', '$3{,}68$', '$0{,}0368$', '$0{,}368$'],
            'answer': 3,
            'solution': 'Chia cho $100$ ta dời dấu phẩy sang trái $2$ chữ số được $0{,}368$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; 0,01; 0,001**, quy '
                 'tắc hoặc công thức nào sau đây xác định đúng **Dời sang phải 1, 2, 3 chữ số**?',
            'options': ['Khi $\\times 10; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}001$',
                        'Khi $\\times 11; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}001$',
                        'Khi $\\times 10; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}2$',
                        'Khi $\\times 20; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}001$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc '
                        'với 0,1; 0,01; 0,001, **Dời sang phải 1, 2, 3 chữ số** được xác định bởi: Khi '
                        '$\\times 10; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}001$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; 0,01; 0,001**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Dời sang trái 1, 2, 3 chữ số**?',
            'options': ['Khi $: 11; 100; 1000$ hoặc $\\times 0{,}1; 0{,}01; 0{,}001$',
                        'Khi $: 10; 100; 1000$ hoặc $\\times 0{,}1; 0{,}01; 0{,}001$',
                        'Khi $: 10; 100; 1000$ hoặc $\\times 0{,}1; 0{,}01; 0{,}2$',
                        'Khi $: 20; 100; 1000$ hoặc $\\times 0{,}1; 0{,}01; 0{,}001$'],
            'answer': 1,
            'solution': 'Trong Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; 0,01; 0,001, '
                        '**Dời sang trái 1, 2, 3 chữ số** có công thức/quy tắc là: Khi $: 10; 100; 1000$ '
                        'hoặc $\\times 0{,}1; 0{,}01; 0{,}001$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phép tính $12{,}5 : 0{,}01$ có kết quả bằng:',
            'options': ['$0{,}125$', '$1{,}25$', '$1250$', '$125$'],
            'answer': 2,
            'solution': 'Chia cho $0{,}01$ tức là nhân với $100$, dời dấu phẩy sang phải $2$ chữ số được '
                        '$1250$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; '
                 '0,01; 0,001**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tính nhẩm nhanh tích và thương của số thập phân với $11; 100; 1000; \\dots$ và với '
                        '$0{,}1; 0{,}01; 0{,}001; \\dots$',
                        'Tính nhẩm nhanh tích và thương của số thập phân với $10; 100; 1000; \\dots$ và với '
                        '$0{,}1; 0{,}01; 0{,}2; \\dots$',
                        'Tính nhẩm nhanh tích và thương của số thập phân với $20; 100; 1000; \\dots$ và với '
                        '$0{,}1; 0{,}01; 0{,}001; \\dots$',
                        'Tính nhẩm nhanh tích và thương của số thập phân với $10; 100; 1000; \\dots$ và với '
                        '$0{,}1; 0{,}01; 0{,}001; \\dots$'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc '
                        'với 0,1; 0,01; 0,001: Tính nhẩm nhanh tích và thương của số thập phân với $10; 100; '
                        '1000; \\dots$ và với $0{,}1; 0{,}01; 0{,}001; \\dots$'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Muốn nhân một số thập phân với $0{,}1$ ta chỉ việc chuyển dấu phẩy của số đó sang bên phải '
                 'một chữ số.',
            'answer': False,
            'solution': 'Nhân với $0{,}1$ tương đương chia cho $10$, ta phải chuyển dấu phẩy sang bên trái '
                        'một chữ số.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; 0,01; 0,001**, quy '
                 'tắc **Dời sang phải 1, 2, 3 chữ số** được xác định bởi Khi $\\times 10; 100; 1000$ hoặc $: '
                 '0{,}1; 0{,}01; 0{,}001$ và khi áp dụng cho ví dụ “Tính nhẩm: $0{,}75 \\times 100$; $24{,}5 '
                 '\\times 0{,}1$ và $1{,}8 : 0{,}01$.” ta có lời giải: Ta có $0{,}75 \\times 100 = 75$; '
                 '$24{,}5 \\times 0{,}1 = 2{,}45$ và $1{,}8 : 0{,}01 = 180$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Dời sang phải 1, 2, 3 chữ số** (Khi '
                        '$\\times 10; 100; 1000$ hoặc $: 0{,}1; 0{,}01; 0{,}001$) và lời giải ví dụ minh họa '
                        'của Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với 0,1; 0,01; 0,001.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc '
                 'với 0,1; 0,01; 0,001** để giải bài toán sau: Tính nhẩm: $0{,}75 \\times 100$; $24{,}5 '
                 '\\times 0{,}1$ và $1{,}8 : 0{,}01$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $0{,}75 \\times 100 = 75$; $24{,}5 \\times 0{,}1 = 2{,}45$ và $1{,}8 : 0{,}01 '
                        '= 180$.',
                        'Ta có $0{,}75 : 100 = 75$; $24{,}5 \\times 0{,}1 = 2{,}45$ và $1{,}8 : 0{,}01 = '
                        '180$.',
                        'Ta có $0{,}75 \\times 100 = 75$; $24{,}5 \\times 0{,}1 = 2{,}45$ và $1{,}8 : 0{,}01 '
                        '= 179$.',
                        'Ta có $2{,}75 \\times 100 = 75$; $24{,}5 \\times 0{,}1 = 2{,}45$ và $1{,}8 : 0{,}01 '
                        '= 180$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Nhân, chia số thập phân với 10; 100; 1000 hoặc với '
                        '0,1; 0,01; 0,001: Ta có $0{,}75 \\times 100 = 75$; $24{,}5 \\times 0{,}1 = 2{,}45$ '
                        'và $1{,}8 : 0{,}01 = 180$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một ô tô đi $100\\text{ km}$ tiêu thụ hết $8{,}5\\text{ l}$ xăng. Hỏi ô tô đó đi quãng '
                 'đường $1000\\text{ km}$ thì tiêu thụ hết bao nhiêu lít xăng?',
            'answer': ['85'],
            'unit': None,
            'solution': 'Quãng đường $1000\\text{ km}$ gấp $100\\text{ km}$ là $10$ lần, số xăng tiêu thụ là '
                        '$8{,}5 \\times 10 = 85$ ($\\text{l}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd05-hinh-phang-chu-vi-dien-tich',
  'context_title': 'Chủ đề 5: Một số hình phẳng. Chu vi và diện tích',
  'context': 'Chủ đề 5 · SGK Toán 5: Hình tam giác, hình thang, hình tròn và công thức tính chu vi, diện '
             'tích.',
  'title': 'Bài 25: Hình tam giác. Diện tích hình tam giác',
  'icon': '🔺',
  'description': 'Nhận biết các loại hình tam giác, đáy và đường cao của hình tam giác, công thức tính diện '
                 'tích hình tam giác.',
  'requirements': ['Nhận biết được tam giác nhọn, tam giác vuông, tam giác tù, tam giác đều và xác định đúng '
                   'đáy, đường cao tương ứng.',
                   'Tính được diện tích hình tam giác khi biết độ dài đáy và chiều cao cùng đơn vị đo.',
                   'Vận dụng kiến thức của **Bài 25: Hình tam giác. Diện tích hình tam giác** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Đường cao** của hình tam giác là đoạn thẳng kẻ từ một đỉnh và vuông góc với cạnh đối '
                'diện (cạnh đáy).\n'
                '- Muốn tính **diện tích hình tam giác**, ta lấy độ dài đáy nhân với chiều cao (cùng một đơn '
                'vị đo) rồi chia cho $2$: $S = \\dfrac{a \\times h}{2}$.',
  'theory': '### 1. Các loại hình tam giác\n'
            '- Tam giác có ba góc nhọn là **tam giác nhọn**; có một góc vuông là **tam giác vuông**; có một '
            'góc tù là **tam giác tù**; có ba cạnh bằng nhau là **tam giác đều**.\n'
            '### 2. Diện tích hình tam giác\n'
            '- Công thức chung: $S = a \\times h : 2$. Từ đó suy ra $a = S \\times 2 : h$ và $h = S \\times '
            '2 : a$.\n'
            '- Với **tam giác vuông**, hai cạnh góc vuông chính là đáy và chiều cao tương ứng: $S = '
            '\\dfrac{a \\times b}{2}$.',
  'formulas': [{'category': 'Hình tam giác',
                'items': [{'name': 'Diện tích tam giác',
                           'formula': '$S = \\dfrac{a \\times h}{2}$ ($a$: đáy, $h$: chiều cao cùng đơn vị)'},
                          {'name': 'Diện tích tam giác vuông',
                           'formula': '$S = \\dfrac{a \\times b}{2}$ ($a, b$: hai cạnh góc vuông)'},
                          {'name': 'Tìm đáy hoặc chiều cao',
                           'formula': '$a = \\dfrac{S \\times 2}{h}$; $h = \\dfrac{S \\times 2}{a}$'}]}],
  'example': 'Tính diện tích hình tam giác có độ dài đáy $12\\text{ cm}$ và chiều cao $7\\text{ cm}$.',
  'example_answer': 'Diện tích hình tam giác là $S = \\dfrac{12 \\times 7}{2} = 42\\text{ cm}^2$.',
  'real_life': 'Tính diện tích tấm biển báo giao thông hình tam giác, cánh buồm hoặc phần mái nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích hình tam giác có độ dài đáy $a$ và chiều cao $h$ (cùng đơn vị đo) '
                 'là:',
            'options': ['$S = a \\times h$',
                        '$S = (a + h) \\times 2$',
                        '$S = a \\times h \\times 2$',
                        '$S = \\dfrac{a \\times h}{2}$'],
            'answer': 3,
            'solution': 'Diện tích hình tam giác bằng đáy nhân chiều cao chia $2$: $S = \\dfrac{a \\times '
                        'h}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tam giác có độ dài đáy $8\\text{ cm}$ và chiều cao $5\\text{ cm}$ có diện tích là:',
            'options': ['$20\\text{ cm}^2$', '$40\\text{ cm}^2$', '$13\\text{ cm}^2$', '$26\\text{ cm}^2$'],
            'answer': 0,
            'solution': 'Ta có $S = \\dfrac{8 \\times 5}{2} = 20\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Hình tam giác. Diện tích hình tam giác**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Diện tích tam giác**?',
            'options': ['$S = \\dfrac{a : h}{2}$ ($a$: đáy, $h$: chiều cao cùng đơn vị)',
                        '$S = \\dfrac{a \\times h}{2}$ ($a$: đáy, $h$: chiều cao cùng đơn vị)',
                        '$S = \\dfrac{2}{a \\times h}$ ($a$: đáy, $h$: chiều cao cùng đơn vị)',
                        '$S = \\dfrac{a \\times h}{4}$ ($a$: đáy, $h$: chiều cao cùng đơn vị)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 25: Hình tam giác. Diện tích hình tam giác, **Diện '
                        'tích tam giác** được xác định bởi: $S = \\dfrac{a \\times h}{2}$ ($a$: đáy, $h$: '
                        'chiều cao cùng đơn vị).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Hình tam giác. Diện tích hình tam giác**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Diện tích tam giác vuông**?',
            'options': ['$S = \\dfrac{a : b}{2}$ ($a, b$: hai cạnh góc vuông)',
                        '$S = \\dfrac{2}{a \\times b}$ ($a, b$: hai cạnh góc vuông)',
                        '$S = \\dfrac{a \\times b}{2}$ ($a, b$: hai cạnh góc vuông)',
                        '$S = \\dfrac{a \\times b}{4}$ ($a, b$: hai cạnh góc vuông)'],
            'answer': 2,
            'solution': 'Trong Bài 25: Hình tam giác. Diện tích hình tam giác, **Diện tích tam giác vuông** '
                        'có công thức/quy tắc là: $S = \\dfrac{a \\times b}{2}$ ($a, b$: hai cạnh góc '
                        'vuông).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình tam giác có diện tích $36\\text{ m}^2$ và độ dài đáy $9\\text{ m}$. Chiều cao của '
                 'tam giác đó là:',
            'options': ['$4\\text{ m}$', '$2\\text{ m}$', '$18\\text{ m}$', '$8\\text{ m}$'],
            'answer': 3,
            'solution': 'Chiều cao của tam giác là $h = \\dfrac{36 \\times 2}{9} = 8\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 25: Hình tam giác. Diện tích hình tam giác**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Nhận biết được tam giác nhọn, tam giác vuông, tam giác tù, tam giác đều và xác định '
                        'đúng đáy, đường cao tương ứng.',
                        'Nhận biết được tam giác nhọn, tam giác vuông, tam giác tù, tam giác đều và xác định '
                        'đúng đáy, đường cao tương ứng. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được tam giác nhọn, tam giác vuông, tam giác '
                        'tù, tam giác đều và xác định đúng đáy, đường cao tương ứng.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được tam giác nhọn, '
                        'tam giác vuông, tam giác tù, tam giác đều và xác định đúng đáy, đường cao tương '
                        'ứng.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 25: Hình tam giác. Diện tích hình tam giác: Nhận biết '
                        'được tam giác nhọn, tam giác vuông, tam giác tù, tam giác đều và xác định đúng đáy, '
                        'đường cao tương ứng.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Diện tích tam giác vuông bằng tích độ dài hai cạnh góc vuông chia cho $2$.',
            'answer': True,
            'solution': 'Trong tam giác vuông, hai cạnh góc vuông vuông góc với nhau nên một cạnh là đáy, '
                        'cạnh kia là chiều cao.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 25: Hình tam giác. Diện tích hình tam giác**, quy tắc **Diện tích tam giác** '
                 'được xác định bởi $S = \\dfrac{a \\times h}{2}$ ($a$: đáy, $h$: chiều cao cùng đơn vị) và '
                 'khi áp dụng cho ví dụ “Tính diện tích hình tam giác có độ dài đáy $12\\text{ cm}$ và chiều '
                 'cao $7\\text{ cm}$.” ta có lời giải: Diện tích hình tam giác là $S = \\dfrac{12 \\times '
                 '7}{2} = 42\\text{ cm}^2$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Diện tích tam giác** ($S = \\dfrac{a '
                        '\\times h}{2}$ ($a$: đáy, $h$: chiều cao cùng đơn vị)) và lời giải ví dụ minh họa '
                        'của Bài 25: Hình tam giác. Diện tích hình tam giác.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 25: Hình tam giác. Diện tích hình tam giác** để '
                 'giải bài toán sau: Tính diện tích hình tam giác có độ dài đáy $12\\text{ cm}$ và chiều cao '
                 '$7\\text{ cm}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Diện tích hình tam giác là $S = \\dfrac{12 : 7}{2} = 42\\text{ cm}^2$.',
                        'Diện tích hình tam giác là $S = \\dfrac{12 \\times 7}{2} = 42\\text{ cm}^2$.',
                        'Diện tích hình tam giác là $S = \\dfrac{2}{12 \\times 7} = 42\\text{ cm}^2$.',
                        'Diện tích hình tam giác là $S = \\dfrac{24 \\times 7}{2} = 42\\text{ cm}^2$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 25: Hình tam giác. Diện tích hình tam giác: Diện tích '
                        'hình tam giác là $S = \\dfrac{12 \\times 7}{2} = 42\\text{ cm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tấm biển quảng cáo hình tam giác vuông có độ dài hai cạnh góc vuông là $60\\text{ cm}$ '
                 'và $45\\text{ cm}$. Tính diện tích tấm biển đó theo đơn vị xăng-ti-mét vuông.',
            'answer': ['1350'],
            'unit': None,
            'solution': 'Diện tích tấm biển là $\\dfrac{60 \\times 45}{2} = 1350$ ($\\text{cm}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd05-hinh-phang-chu-vi-dien-tich',
  'context_title': 'Chủ đề 5: Một số hình phẳng. Chu vi và diện tích',
  'context': 'Chủ đề 5 · SGK Toán 5: Hình tam giác, hình thang, hình tròn và công thức tính chu vi, diện '
             'tích.',
  'title': 'Bài 26: Hình thang. Diện tích hình thang',
  'icon': '🔺',
  'description': 'Nhận biết hình thang, hình thang vuông, các yếu tố của hình thang và công thức tính diện '
                 'tích hình thang.',
  'requirements': ['Nhận biết được hình thang (có một cặp cạnh đối diện song song) và hình thang vuông.',
                   'Tính được diện tích hình thang khi biết độ dài hai đáy và chiều cao cùng đơn vị đo.',
                   'Vận dụng kiến thức của **Bài 26: Hình thang. Diện tích hình thang** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': '- **Hình thang** là hình tứ giác có **một cặp cạnh đối diện song song** (gọi là đáy lớn và '
                'đáy bé).\n'
                '- **Diện tích hình thang** bằng tổng độ dài hai đáy nhân với chiều cao (cùng một đơn vị đo) '
                'rồi chia cho $2$: $S = \\dfrac{(a + b) \\times h}{2}$.',
  'theory': '### 1. Các yếu tố của hình thang\n'
            '- Hai cạnh song song gọi là **hai cạnh đáy** ($a, b$); hai cạnh kia gọi là **hai cạnh bên**.\n'
            '- Hình thang có một cạnh bên vuông góc với hai đáy gọi là **hình thang vuông** (cạnh bên đó '
            'chính là chiều cao).\n'
            '### 2. Công thức diện tích hình thang\n'
            '- Ví dụ: hình thang có hai đáy $6\\text{ cm}$ và $4\\text{ cm}$, chiều cao $3\\text{ cm}$ thì '
            '$S = \\dfrac{(6 + 4) \\times 3}{2} = 15\\text{ cm}^2$.',
  'formulas': [{'category': 'Hình thang',
                'items': [{'name': 'Diện tích hình thang',
                           'formula': '$S = \\dfrac{(a + b) \\times h}{2}$ ($a, b$: hai đáy; $h$: chiều '
                                      'cao)'},
                          {'name': 'Tổng hai đáy hoặc chiều cao',
                           'formula': '$a + b = \\dfrac{S \\times 2}{h}$; $h = \\dfrac{S \\times 2}{a + '
                                      'b}$'}]}],
  'example': 'Một mảnh đất hình thang có đáy lớn $25\\text{ m}$, đáy bé $15\\text{ m}$ và chiều cao '
             '$12\\text{ m}$. Tính diện tích mảnh đất.',
  'example_answer': 'Diện tích mảnh đất là $S = \\dfrac{(25 + 15) \\times 12}{2} = \\dfrac{40 \\times 12}{2} '
                    '= 240\\text{ m}^2$.',
  'real_life': 'Tính diện tích thửa ruộng hình thang, mặt cắt con đê hoặc mặt bàn học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình thang là tứ giác có đặc điểm nào sau đây?',
            'options': ['Một cặp cạnh đối diện song song',
                        'Bốn cạnh bằng nhau',
                        'Bốn góc vuông',
                        'Ba cạnh bằng nhau'],
            'answer': 0,
            'solution': 'Hình thang là tứ giác có một cặp cạnh đối diện song song.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích hình thang có hai đáy $a, b$ và chiều cao $h$ (cùng đơn vị đo) '
                 'là:',
            'options': ['$S = (a + b) \\times h$',
                        '$S = \\dfrac{(a + b) \\times h}{2}$',
                        '$S = \\dfrac{a \\times b \\times h}{2}$',
                        '$S = (a + b) : 2$'],
            'answer': 1,
            'solution': 'Diện tích hình thang là $S = \\dfrac{(a + b) \\times h}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Hình thang. Diện tích hình thang**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Diện tích hình thang**?',
            'options': ['$S = \\dfrac{(a - b) \\times h}{2}$ ($a, b$: hai đáy; $h$: chiều cao)',
                        '$S = \\dfrac{2}{(a + b) \\times h}$ ($a, b$: hai đáy; $h$: chiều cao)',
                        '$S = \\dfrac{(a + b) \\times h}{2}$ ($a, b$: hai đáy; $h$: chiều cao)',
                        '$S = \\dfrac{(a + b) \\times h}{4}$ ($a, b$: hai đáy; $h$: chiều cao)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 26: Hình thang. Diện tích hình thang, **Diện tích '
                        'hình thang** được xác định bởi: $S = \\dfrac{(a + b) \\times h}{2}$ ($a, b$: hai '
                        'đáy; $h$: chiều cao).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Hình thang. Diện tích hình thang**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tổng hai đáy hoặc chiều cao**?',
            'options': ['$a - b = \\dfrac{S \\times 2}{h}$; $h = \\dfrac{S \\times 2}{a + b}$',
                        '$a + b = \\dfrac{h}{S \\times 2}$; $h = \\dfrac{S \\times 2}{a + b}$',
                        '$a + b = \\dfrac{S \\times 4}{h}$; $h = \\dfrac{S \\times 2}{a + b}$',
                        '$a + b = \\dfrac{S \\times 2}{h}$; $h = \\dfrac{S \\times 2}{a + b}$'],
            'answer': 3,
            'solution': 'Trong Bài 26: Hình thang. Diện tích hình thang, **Tổng hai đáy hoặc chiều cao** có '
                        'công thức/quy tắc là: $a + b = \\dfrac{S \\times 2}{h}$; $h = \\dfrac{S \\times '
                        '2}{a + b}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hình thang có đáy lớn $10\\text{ cm}$, đáy bé $6\\text{ cm}$ và chiều cao $5\\text{ cm}$ '
                 'có diện tích là:',
            'options': ['$40\\text{ cm}^2$', '$80\\text{ cm}^2$', '$150\\text{ cm}^2$', '$30\\text{ cm}^2$'],
            'answer': 0,
            'solution': 'Ta có $S = \\dfrac{(10 + 6) \\times 5}{2} = 40\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 26: Hình thang. Diện tích hình thang**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận biết được hình thang (có một cặp cạnh đối diện cắt nhau) và hình thang vuông.',
                        'Nhận biết được hình thang (có một cặp cạnh đối diện song song) và hình thang vuông.',
                        'Đảo ngược vế của quy tắc: Nhận biết được hình thang (có một cặp cạnh đối diện song '
                        'song) và hình thang vuông.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được hình thang (có '
                        'một cặp cạnh đối diện song song) và hình thang vuông.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 26: Hình thang. Diện tích hình thang: Nhận biết được '
                        'hình thang (có một cặp cạnh đối diện song song) và hình thang vuông.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hình thang có hai đáy $8\\text{ m}$ và $6\\text{ m}$, chiều cao $5\\text{ m}$ có diện tích '
                 'là $70\\text{ m}^2$.',
            'answer': False,
            'solution': 'Diện tích đúng là $\\dfrac{(8 + 6) \\times 5}{2} = 35\\text{ m}^2$ (quên chia cho '
                        '$2$ mới ra $70\\text{ m}^2$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 26: Hình thang. Diện tích hình thang**, quy tắc **Diện tích hình thang** được '
                 'xác định bởi $S = \\dfrac{(a + b) \\times h}{2}$ ($a, b$: hai đáy; $h$: chiều cao) và khi '
                 'áp dụng cho ví dụ “Một mảnh đất hình thang có đáy lớn $25\\text{ m}$, đáy bé $15\\text{ '
                 'm}$ và chiều cao $12\\text{ m}$. Tính diện tích mảnh đất.” ta có lời giải: Diện tích mảnh '
                 'đất là $S = \\dfrac{(25 + 15) \\times 12}{2} = \\dfrac{40 \\times 12}{2} = 240\\text{ '
                 'm}^2$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Diện tích hình thang** ($S = \\dfrac{(a '
                        '+ b) \\times h}{2}$ ($a, b$: hai đáy; $h$: chiều cao)) và lời giải ví dụ minh họa '
                        'của Bài 26: Hình thang. Diện tích hình thang.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 26: Hình thang. Diện tích hình thang** để giải bài '
                 'toán sau: Một mảnh đất hình thang có đáy lớn $25\\text{ m}$, đáy bé $15\\text{ m}$ và '
                 'chiều cao $12\\text{ m}$. Tính diện tích mảnh đất. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Diện tích mảnh đất là $S = \\dfrac{(25 - 15) \\times 12}{2} = \\dfrac{40 \\times '
                        '12}{2} = 240\\text{ m}^2$.',
                        'Diện tích mảnh đất là $S = \\dfrac{2}{(25 + 15) \\times 12} = \\dfrac{40 \\times '
                        '12}{2} = 240\\text{ m}^2$.',
                        'Diện tích mảnh đất là $S = \\dfrac{(25 + 15) \\times 12}{2} = \\dfrac{40 \\times '
                        '12}{2} = 240\\text{ m}^2$.',
                        'Diện tích mảnh đất là $S = \\dfrac{(50 + 15) \\times 12}{2} = \\dfrac{40 \\times '
                        '12}{2} = 240\\text{ m}^2$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 26: Hình thang. Diện tích hình thang: Diện tích mảnh đất '
                        'là $S = \\dfrac{(25 + 15) \\times 12}{2} = \\dfrac{40 \\times 12}{2} = 240\\text{ '
                        'm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thửa ruộng hình thang có tổng độ dài hai đáy là $48\\text{ m}$ và chiều cao là '
                 '$15\\text{ m}$. Tính diện tích thửa ruộng đó theo đơn vị mét vuông.',
            'answer': ['360'],
            'unit': None,
            'solution': 'Diện tích thửa ruộng là $\\dfrac{48 \\times 15}{2} = 360$ ($\\text{m}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd05-hinh-phang-chu-vi-dien-tich',
  'context_title': 'Chủ đề 5: Một số hình phẳng. Chu vi và diện tích',
  'context': 'Chủ đề 5 · SGK Toán 5: Hình tam giác, hình thang, hình tròn và công thức tính chu vi, diện '
             'tích.',
  'title': 'Bài 27: Đường tròn. Chu vi và diện tích hình tròn',
  'icon': '🔺',
  'description': 'Nhận biết tâm, bán kính, đường kính của hình tròn và công thức tính chu vi, diện tích hình '
                 'tròn.',
  'requirements': ['Nắm được mối quan hệ giữa đường kính và bán kính ($d = 2 \\times r$) và sử dụng compa để '
                   'vẽ đường tròn.',
                   'Tính được chu vi và diện tích hình tròn khi biết bán kính hoặc đường kính.',
                   'Vận dụng kiến thức của **Bài 27: Đường tròn. Chu vi và diện tích hình tròn** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': '- Trong một hình tròn, **đường kính** dài gấp $2$ lần **bán kính**: $d = 2 \\times r$.\n'
                '- **Chu vi hình tròn**: $C = d \\times 3{,}14 = r \\times 2 \\times 3{,}14$.\n'
                '- **Diện tích hình tròn**: $S = r \\times r \\times 3{,}14$.',
  'theory': '### 1. Tính chu vi hình tròn\n'
            '- Nếu bán kính $r = 5\\text{ cm}$ thì chu vi là $C = 5 \\times 2 \\times 3{,}14 = 31{,}4\\text{ '
            'cm}$.\n'
            '- Biết chu vi $C$, ta tìm được đường kính $d = C : 3{,}14$ và bán kính $r = C : 6{,}28$.\n'
            '### 2. Tính diện tích hình tròn\n'
            '- Nếu biết đường kính $d$, ta phải tìm bán kính $r = d : 2$ trước rồi mới tính diện tích $S = r '
            '\\times r \\times 3{,}14$.',
  'formulas': [{'category': 'Hình tròn (tâm O, bán kính r, đường kính d)',
                'items': [{'name': 'Đường kính và bán kính',
                           'formula': '$d = 2 \\times r \\Rightarrow r = d : 2$'},
                          {'name': 'Chu vi hình tròn',
                           'formula': '$C = d \\times 3{,}14 = r \\times 2 \\times 3{,}14$'},
                          {'name': 'Diện tích hình tròn', 'formula': '$S = r \\times r \\times 3{,}14$'}]}],
  'example': 'Một hình tròn có đường kính $d = 6\\text{ cm}$. Tính chu vi và diện tích của hình tròn đó.',
  'example_answer': 'Chu vi hình tròn: $C = 6 \\times 3{,}14 = 18{,}84\\text{ cm}$. Bán kính $r = 6 : 2 = '
                    '3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = 28{,}26\\text{ '
                    'cm}^2$.',
  'real_life': 'Tính quãng đường bánh xe đạp lăn được sau nhiều vòng quay hoặc diện tích mặt bồn hoa hình '
               'tròn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính chu vi hình tròn có đường kính $d$ là:',
            'options': ['$C = d \\times d \\times 3{,}14$',
                        '$C = d \\times 3{,}14$',
                        '$C = d : 3{,}14$',
                        '$C = d \\times 2$'],
            'answer': 1,
            'solution': 'Chu vi hình tròn bằng đường kính nhân với $3{,}14$: $C = d \\times 3{,}14$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích hình tròn có bán kính $r$ là:',
            'options': ['$S = r \\times 2 \\times 3{,}14$',
                        '$S = r \\times 3{,}14$',
                        '$S = r \\times r \\times 3{,}14$',
                        '$S = d \\times 3{,}14$'],
            'answer': 2,
            'solution': 'Diện tích hình tròn là $S = r \\times r \\times 3{,}14$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Đường tròn. Chu vi và diện tích hình tròn**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Đường kính và bán kính**?',
            'options': ['$d = 2 : r \\Rightarrow r = d : 2$',
                        '$d = 2 \\times r \\Rightarrow r = d : 1$',
                        '$d = 4 \\times r \\Rightarrow r = d : 2$',
                        '$d = 2 \\times r \\Rightarrow r = d : 2$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 27: Đường tròn. Chu vi và diện tích hình tròn, '
                        '**Đường kính và bán kính** được xác định bởi: $d = 2 \\times r \\Rightarrow r = d : '
                        '2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Đường tròn. Chu vi và diện tích hình tròn**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Chu vi hình tròn**?',
            'options': ['$C = d \\times 3{,}14 = r \\times 2 \\times 3{,}14$',
                        '$C = d : 3{,}14 = r \\times 2 \\times 3{,}14$',
                        '$C = d \\times 3{,}14 = r \\times 2 \\times 3{,}13$',
                        '$C = d \\times 6{,}14 = r \\times 2 \\times 3{,}14$'],
            'answer': 0,
            'solution': 'Trong Bài 27: Đường tròn. Chu vi và diện tích hình tròn, **Chu vi hình tròn** có '
                        'công thức/quy tắc là: $C = d \\times 3{,}14 = r \\times 2 \\times 3{,}14$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hình tròn có bán kính $r = 5\\text{ cm}$ thì có chu vi bằng:',
            'options': ['$15{,}7\\text{ cm}$',
                        '$31{,}4\\text{ cm}$',
                        '$78{,}5\\text{ cm}$',
                        '$25\\text{ cm}$'],
            'answer': 1,
            'solution': 'Chu vi hình tròn là $C = 5 \\times 2 \\times 3{,}14 = 31{,}4\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 27: Đường tròn. Chu vi và diện tích hình tròn**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Nắm được mối quan hệ giữa đường kính và bán kính ($d = 2 : r$) và sử dụng compa để '
                        'vẽ đường tròn.',
                        'Nắm được mối quan hệ giữa đường kính và bán kính ($d = 1 \\times r$) và sử dụng '
                        'compa để vẽ đường tròn.',
                        'Nắm được mối quan hệ giữa đường kính và bán kính ($d = 2 \\times r$) và sử dụng '
                        'compa để vẽ đường tròn.',
                        'Nắm được mối quan hệ giữa đường kính và bán kính ($d = 4 \\times r$) và sử dụng '
                        'compa để vẽ đường tròn.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 27: Đường tròn. Chu vi và diện tích hình tròn: Nắm '
                        'được mối quan hệ giữa đường kính và bán kính ($d = 2 \\times r$) và sử dụng compa '
                        'để vẽ đường tròn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hình tròn có bán kính $10\\text{ cm}$ thì có diện tích là $314\\text{ cm}^2$.',
            'answer': True,
            'solution': 'Ta có $S = 10 \\times 10 \\times 3{,}14 = 314\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 27: Đường tròn. Chu vi và diện tích hình tròn**, quy tắc **Đường kính và bán '
                 'kính** được xác định bởi $d = 2 \\times r \\Rightarrow r = d : 2$ và khi áp dụng cho ví dụ '
                 '“Một hình tròn có đường kính $d = 6\\text{ cm}$. Tính chu vi và diện tích của hình tròn '
                 'đó.” ta có lời giải: Chu vi hình tròn: $C = 6 \\times 3{,}14 = 18{,}84\\text{ cm}$. Bán '
                 'kính $r = 6 : 2 = 3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = '
                 '28{,}26\\text{ cm}^2$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đường kính và bán kính** ($d = 2 \\times '
                        'r \\Rightarrow r = d : 2$) và lời giải ví dụ minh họa của Bài 27: Đường tròn. Chu '
                        'vi và diện tích hình tròn.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 27: Đường tròn. Chu vi và diện tích hình tròn** để '
                 'giải bài toán sau: Một hình tròn có đường kính $d = 6\\text{ cm}$. Tính chu vi và diện '
                 'tích của hình tròn đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chu vi hình tròn: $C = 6 : 3{,}14 = 18{,}84\\text{ cm}$. Bán kính $r = 6 : 2 = '
                        '3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = '
                        '28{,}26\\text{ cm}^2$...',
                        'Chu vi hình tròn: $C = 6 \\times 3{,}14 = 18{,}84\\text{ cm}$. Bán kính $r = 6 : 2 '
                        '= 3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = '
                        '28{,}26\\text{ cm}^1$...',
                        'Chu vi hình tròn: $C = 12 \\times 3{,}14 = 18{,}84\\text{ cm}$. Bán kính $r = 6 : 2 '
                        '= 3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = '
                        '28{,}26\\text{ cm}^2$...',
                        'Chu vi hình tròn: $C = 6 \\times 3{,}14 = 18{,}84\\text{ cm}$. Bán kính $r = 6 : 2 '
                        '= 3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = '
                        '28{,}26\\text{ cm}^2$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 27: Đường tròn. Chu vi và diện tích hình tròn: Chu vi '
                        'hình tròn: $C = 6 \\times 3{,}14 = 18{,}84\\text{ cm}$. Bán kính $r = 6 : 2 = '
                        '3\\text{ cm}$, diện tích hình tròn: $S = 3 \\times 3 \\times 3{,}14 = '
                        '28{,}26\\text{ cm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bánh xe đạp có đường kính $0{,}65\\text{ m}$. Khi bánh xe lăn trên mặt đất được $100$ '
                 'vòng thì người đi xe đạp đi được bao nhiêu mét?',
            'answer': ['204,1', '204.1'],
            'unit': None,
            'solution': 'Chu vi bánh xe là $0{,}65 \\times 3{,}14 = 2{,}041\\text{ m}$. Lăn $100$ vòng đi '
                        'được $2{,}041 \\times 100 = 204{,}1\\text{ m}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd06-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 6: Ôn tập học kì 1',
  'context': 'Chủ đề 6 · SGK Toán 5: Ôn tập tổng hợp học kì 1 về số thập phân, hình phẳng và đo lường.',
  'title': 'Bài 30: Ôn tập số thập phân và các phép tính',
  'icon': '📝',
  'description': 'Hệ thống hóa kiến thức về đọc, viết, so sánh, làm tròn số thập phân và bốn phép tính với '
                 'số thập phân.',
  'requirements': ['Đọc, viết, so sánh, làm tròn thành thạo các số thập phân.',
                   'Tính đúng giá trị biểu thức có chứa các phép tính cộng, trừ, nhân, chia số thập phân.',
                   'Vận dụng kiến thức của **Bài 30: Ôn tập số thập phân và các phép tính** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '- Số thập phân gồm phần nguyên và phần thập phân ngăn cách bởi dấu phẩy; $a{,}b = a{,}b0$.\n'
                '- Thứ tự thực hiện phép tính: trong ngoặc trước, ngoài ngoặc sau; nhân chia trước, cộng trừ '
                'sau.',
  'theory': '### 1. Ôn tập cấu tạo, so sánh và làm tròn\n'
            '- So sánh từ phần nguyên đến hàng phần mười, phần trăm, phần nghìn.\n'
            '### 2. Bốn phép tính với số thập phân\n'
            '- Cộng, trừ: đặt dấu phẩy thẳng cột.\n'
            '- Nhân: đếm tổng số chữ số ở phần thập phân của cả hai thừa số.\n'
            '- Chia: dời dấu phẩy để đưa số chia về số tự nhiên.',
  'formulas': [{'category': 'Tính chất vận dụng tính nhanh',
                'items': [{'name': 'Phân phối của phép nhân',
                           'formula': '$a \\times b + a \\times c = a \\times (b + c)$'},
                          {'name': 'Nhân với 0,25; 0,5',
                           'formula': '$a \\times 0{,}5 = a : 2$; $a \\times 0{,}25 = a : 4$'}]}],
  'example': 'Tính giá trị biểu thức: $(12{,}5 - 4{,}7) \\times 2{,}4$.',
  'example_answer': 'Thực hiện trong ngoặc trước: $12{,}5 - 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times '
                    '2{,}4 = 18{,}72$.',
  'real_life': 'Tính tổng hóa đơn tiền điện, tiền nước và tiền mua thực phẩm hằng ngày.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số thập phân “mười hai phẩy không năm” được viết là:',
            'options': ['$12{,}5$', '$12{,}005$', '$12{,}05$', '$1205$'],
            'answer': 2,
            'solution': 'Phần nguyên là $12$, phần thập phân là $05$ nên viết là $12{,}05$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $9{,}6 : 2{,}4$ là:',
            'options': ['$0{,}4$', '$40$', '$23{,}04$', '$4$'],
            'answer': 3,
            'solution': 'Ta có $9{,}6 : 2{,}4 = 96 : 24 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Ôn tập số thập phân và các phép tính**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Phân phối của phép nhân**?',
            'options': ['$a \\times b + a \\times c = a \\times (b + c)$',
                        '$a \\times b - a \\times c = a \\times (b + c)$',
                        'Đảo ngược vế của quy tắc: $a \\times b + a \\times c = a \\times (b + c)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a \\times b + a \\times c = a '
                        '\\times (b + c)$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 30: Ôn tập số thập phân và các phép tính, **Phân '
                        'phối của phép nhân** được xác định bởi: $a \\times b + a \\times c = a \\times (b + '
                        'c)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Ôn tập số thập phân và các phép tính**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Nhân với 0,25; 0,5**?',
            'options': ['$a : 0{,}5 = a : 2$; $a \\times 0{,}25 = a : 4$',
                        '$a \\times 0{,}5 = a : 2$; $a \\times 0{,}25 = a : 4$',
                        '$a \\times 0{,}5 = a : 2$; $a \\times 0{,}25 = a : 3$',
                        '$a \\times 2{,}5 = a : 2$; $a \\times 0{,}25 = a : 4$'],
            'answer': 1,
            'solution': 'Trong Bài 30: Ôn tập số thập phân và các phép tính, **Nhân với 0,25; 0,5** có công '
                        'thức/quy tắc là: $a \\times 0{,}5 = a : 2$; $a \\times 0{,}25 = a : 4$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $6{,}8 \\times 3{,}5 + 6{,}8 \\times 6{,}5$ là:',
            'options': ['$6{,}8$', '$680$', '$68$', '$34$'],
            'answer': 2,
            'solution': 'Ta có $6{,}8 \\times (3{,}5 + 6{,}5) = 6{,}8 \\times 10 = 68$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 30: Ôn tập số thập phân và các phép tính**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Đọc, viết, so sánh, làm tròn thành thạo các số thập phân. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đọc, viết, so sánh, làm tròn thành thạo các số thập phân.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đọc, viết, so sánh, làm tròn '
                        'thành thạo các số thập phân.',
                        'Đọc, viết, so sánh, làm tròn thành thạo các số thập phân.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 30: Ôn tập số thập phân và các phép tính: Đọc, viết, '
                        'so sánh, làm tròn thành thạo các số thập phân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Kết quả của phép nhân $3{,}5 \\times 0{,}2$ bằng $7$.',
            'answer': False,
            'solution': 'Ta có $35 \\times 2 = 70$, tách $2$ chữ số ở phần thập phân được $0{,}70 = 0{,}7$ '
                        'chứ không phải $7$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 30: Ôn tập số thập phân và các phép tính**, quy tắc **Phân phối của phép '
                 'nhân** được xác định bởi $a \\times b + a \\times c = a \\times (b + c)$ và khi áp dụng '
                 'cho ví dụ “Tính giá trị biểu thức: $(12{,}5 - 4{,}7) \\times 2{,}4$.” ta có lời giải: Thực '
                 'hiện trong ngoặc trước: $12{,}5 - 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times 2{,}4 = '
                 '18{,}72$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Phân phối của phép nhân** ($a \\times b '
                        '+ a \\times c = a \\times (b + c)$) và lời giải ví dụ minh họa của Bài 30: Ôn tập '
                        'số thập phân và các phép tính.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 30: Ôn tập số thập phân và các phép tính** để giải '
                 'bài toán sau: Tính giá trị biểu thức: $(12{,}5 - 4{,}7) \\times 2{,}4$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Thực hiện trong ngoặc trước: $12{,}5 - 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times '
                        '2{,}4 = 18{,}72$.',
                        'Thực hiện trong ngoặc trước: $12{,}5 + 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times '
                        '2{,}4 = 18{,}72$.',
                        'Thực hiện trong ngoặc trước: $12{,}5 - 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times '
                        '2{,}4 = 18{,}71$.',
                        'Thực hiện trong ngoặc trước: $24{,}5 - 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times '
                        '2{,}4 = 18{,}72$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 30: Ôn tập số thập phân và các phép tính: Thực hiện '
                        'trong ngoặc trước: $12{,}5 - 4{,}7 = 7{,}8$. Sau đó nhân: $7{,}8 \\times 2{,}4 = '
                        '18{,}72$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm $x$ biết $x \\times 2{,}5 = 11{,}25 + 3{,}75$.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Ta có $x \\times 2{,}5 = 15 \\Rightarrow x = 15 : 2{,}5 = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd06-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 6: Ôn tập học kì 1',
  'context': 'Chủ đề 6 · SGK Toán 5: Ôn tập tổng hợp học kì 1 về số thập phân, hình phẳng và đo lường.',
  'title': 'Bài 32: Ôn tập hình phẳng, chu vi và diện tích',
  'icon': '📝',
  'description': 'Ôn tập đặc điểm và công thức tính chu vi, diện tích hình tam giác, hình thang, hình tròn.',
  'requirements': ['Vận dụng thành thạo công thức diện tích hình tam giác, hình thang và chu vi, diện tích '
                   'hình tròn.',
                   'Giải được bài toán tính diện tích hình ghép hoặc phần đất còn lại trong thực tế.',
                   'Vận dụng kiến thức của **Bài 32: Ôn tập hình phẳng, chu vi và diện tích** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': '- Tam giác: $S = \\dfrac{a \\times h}{2}$. Hình thang: $S = \\dfrac{(a + b) \\times '
                'h}{2}$.\n'
                '- Hình tròn: $C = d \\times 3{,}14 = r \\times 2 \\times 3{,}14$ và $S = r \\times r '
                '\\times 3{,}14$.',
  'theory': '### 1. Tìm yếu tố chưa biết từ chu vi, diện tích\n'
            '- Biết chu vi hình tròn $C$, tìm bán kính $r = C : 3{,}14 : 2$ rồi tính diện tích $S = r '
            '\\times r \\times 3{,}14$.\n'
            '### 2. Diện tích hình phẳng ghép\n'
            '- Chia hình phức tạp thành các hình quen thuộc (chữ nhật, tam giác, hình thang, nửa hình tròn) '
            'để tính.',
  'formulas': [{'category': 'Tổng hợp công thức hình phẳng',
                'items': [{'name': 'Tam giác và Hình thang',
                           'formula': '$S_{\\text{tg}} = \\dfrac{a \\times h}{2}$; $S_{\\text{ht}} = '
                                      '\\dfrac{(a + b) \\times h}{2}$'},
                          {'name': 'Hình tròn',
                           'formula': '$C = 2 \\times r \\times 3{,}14$; $S = r \\times r \\times '
                                      '3{,}14$'}]}],
  'example': 'Một hình tròn có chu vi $18{,}84\\text{ cm}$. Tính diện tích hình tròn đó.',
  'example_answer': 'Bán kính hình tròn là $r = 18{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình tròn là '
                    '$S = 3 \\times 3 \\times 3{,}14 = 28{,}26\\text{ cm}^2$.',
  'real_life': 'Tính diện tích sân trường, vườn hoa và chi phí lát gạch, trồng cỏ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình tròn có đường kính $8\\text{ cm}$ thì bán kính của nó là:',
            'options': ['$16\\text{ cm}$', '$8\\text{ cm}$', '$25{,}12\\text{ cm}$', '$4\\text{ cm}$'],
            'answer': 3,
            'solution': 'Bán kính bằng nửa đường kính: $r = 8 : 2 = 4\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Diện tích hình tam giác có đáy $10\\text{ dm}$ và chiều cao $6\\text{ dm}$ là:',
            'options': ['$30\\text{ dm}^2$', '$60\\text{ dm}^2$', '$16\\text{ dm}^2$', '$15\\text{ dm}^2$'],
            'answer': 0,
            'solution': 'Ta có $S = \\dfrac{10 \\times 6}{2} = 30\\text{ dm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Ôn tập hình phẳng, chu vi và diện tích**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Tam giác và Hình thang**?',
            'options': ['$S_{\\text{tg}} = \\dfrac{a \\times h}{2}$; $S_{\\text{ht}} = \\dfrac{(a - b) '
                        '\\times h}{2}$',
                        '$S_{\\text{tg}} = \\dfrac{a \\times h}{2}$; $S_{\\text{ht}} = \\dfrac{(a + b) '
                        '\\times h}{2}$',
                        '$S_{\\text{tg}} = \\dfrac{2}{a \\times h}$; $S_{\\text{ht}} = \\dfrac{(a + b) '
                        '\\times h}{2}$',
                        '$S_{\\text{tg}} = \\dfrac{a \\times h}{4}$; $S_{\\text{ht}} = \\dfrac{(a + b) '
                        '\\times h}{2}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 32: Ôn tập hình phẳng, chu vi và diện tích, **Tam '
                        'giác và Hình thang** được xác định bởi: $S_{\\text{tg}} = \\dfrac{a \\times h}{2}$; '
                        '$S_{\\text{ht}} = \\dfrac{(a + b) \\times h}{2}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Ôn tập hình phẳng, chu vi và diện tích**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Hình tròn**?',
            'options': ['$C = 2 : r \\times 3{,}14$; $S = r \\times r \\times 3{,}14$',
                        '$C = 2 \\times r \\times 3{,}14$; $S = r \\times r \\times 3{,}13$',
                        '$C = 2 \\times r \\times 3{,}14$; $S = r \\times r \\times 3{,}14$',
                        '$C = 4 \\times r \\times 3{,}14$; $S = r \\times r \\times 3{,}14$'],
            'answer': 2,
            'solution': 'Trong Bài 32: Ôn tập hình phẳng, chu vi và diện tích, **Hình tròn** có công '
                        'thức/quy tắc là: $C = 2 \\times r \\times 3{,}14$; $S = r \\times r \\times '
                        '3{,}14$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình tròn có chu vi $18{,}84\\text{ cm}$. Diện tích của hình tròn đó là:',
            'options': ['$113{,}04\\text{ cm}^2$',
                        '$9{,}42\\text{ cm}^2$',
                        '$56{,}52\\text{ cm}^2$',
                        '$28{,}26\\text{ cm}^2$'],
            'answer': 3,
            'solution': 'Ta có $r = 18{,}84 : 6{,}28 = 3\\text{ cm}$, suy ra $S = 3 \\times 3 \\times 3{,}14 '
                        '= 28{,}26\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 32: Ôn tập hình phẳng, chu vi và diện tích**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Vận dụng thành thạo công thức diện tích hình tam giác, hình thang và chu vi, diện '
                        'tích hình tròn.',
                        'Vận dụng thành thạo công thức diện tích hình tam giác, hình thang và chu vi, diện '
                        'tích hình tròn. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Vận dụng thành thạo công thức diện tích hình tam giác, '
                        'hình thang và chu vi, diện tích hình tròn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Vận dụng thành thạo công thức '
                        'diện tích hình tam giác, hình thang và chu vi, diện tích hình tròn.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 32: Ôn tập hình phẳng, chu vi và diện tích: Vận dụng '
                        'thành thạo công thức diện tích hình tam giác, hình thang và chu vi, diện tích hình '
                        'tròn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hình tam giác có đáy $4{,}5\\text{ m}$ và chiều cao $2\\text{ m}$ có diện tích là '
                 '$4{,}5\\text{ m}^2$.',
            'answer': True,
            'solution': 'Ta có $S = \\dfrac{4{,}5 \\times 2}{2} = 4{,}5\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 32: Ôn tập hình phẳng, chu vi và diện tích**, quy tắc **Tam giác và Hình '
                 'thang** được xác định bởi $S_{\\text{tg}} = \\dfrac{a \\times h}{2}$; $S_{\\text{ht}} = '
                 '\\dfrac{(a + b) \\times h}{2}$ và khi áp dụng cho ví dụ “Một hình tròn có chu vi '
                 '$18{,}84\\text{ cm}$. Tính diện tích hình tròn đó.” ta có lời giải: Bán kính hình tròn là '
                 '$r = 18{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình tròn là $S = 3 \\times 3 \\times '
                 '3{,}14 = 28{,}26\\text{ cm}^2$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tam giác và Hình thang** '
                        '($S_{\\text{tg}} = \\dfrac{a \\times h}{2}$; $S_{\\text{ht}} = \\dfrac{(a + b) '
                        '\\times h}{2}$) và lời giải ví dụ minh họa của Bài 32: Ôn tập hình phẳng, chu vi và '
                        'diện tích.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 32: Ôn tập hình phẳng, chu vi và diện tích** để '
                 'giải bài toán sau: Một hình tròn có chu vi $18{,}84\\text{ cm}$. Tính diện tích hình tròn '
                 'đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Bán kính hình tròn là $r = 18{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình '
                        'tròn là $S = 3 : 3 \\times 3{,}14 = 28{,}26\\text{ cm}^2$.',
                        'Bán kính hình tròn là $r = 18{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình '
                        'tròn là $S = 3 \\times 3 \\times 3{,}14 = 28{,}26\\text{ cm}^2$.',
                        'Bán kính hình tròn là $r = 18{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình '
                        'tròn là $S = 3 \\times 3 \\times 3{,}14 = 28{,}26\\text{ cm}^1$.',
                        'Bán kính hình tròn là $r = 36{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình '
                        'tròn là $S = 3 \\times 3 \\times 3{,}14 = 28{,}26\\text{ cm}^2$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 32: Ôn tập hình phẳng, chu vi và diện tích: Bán kính '
                        'hình tròn là $r = 18{,}84 : 3{,}14 : 2 = 3\\text{ cm}$. Diện tích hình tròn là $S = '
                        '3 \\times 3 \\times 3{,}14 = 28{,}26\\text{ cm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thửa ruộng hình thang có đáy lớn $120\\text{ m}$, đáy bé $80\\text{ m}$ và chiều cao '
                 '$50\\text{ m}$. Diện tích thửa ruộng đó bằng bao nhiêu héc-ta?',
            'answer': ['0,5', '0.5'],
            'unit': None,
            'solution': 'Diện tích thửa ruộng là $\\dfrac{(120 + 80) \\times 50}{2} = 5000\\text{ m}^2 = '
                        '0{,}5\\text{ ha}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd06-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 6: Ôn tập học kì 1',
  'context': 'Chủ đề 6 · SGK Toán 5: Ôn tập tổng hợp học kì 1 về số thập phân, hình phẳng và đo lường.',
  'title': 'Bài 34: Ôn tập đo lường',
  'icon': '📝',
  'description': 'Ôn tập tổng hợp bảng đơn vị đo độ dài, khối lượng, dung tích và diện tích dưới dạng số '
                 'thập phân.',
  'requirements': ['Chuyển đổi chính xác giữa các đơn vị đo độ dài, khối lượng, dung tích và diện tích.',
                   'So sánh và thực hiện các phép tính với số đo đại lượng trong bài toán thực tiễn.',
                   'Vận dụng kiến thức của **Bài 34: Ôn tập đo lường** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': '- Hai đơn vị đo độ dài, khối lượng liền kề hơn kém nhau $10$ lần (ứng với $1$ chữ số thập '
                'phân).\n'
                '- Hai đơn vị đo diện tích liền kề hơn kém nhau $100$ lần (ứng với $2$ chữ số thập phân).',
  'theory': '### 1. Chuyển đổi đơn vị đo thường gặp\n'
            '- Độ dài: $1\\text{ km} = 1000\\text{ m}$; $1\\text{ m} = 100\\text{ cm} = 1000\\text{ mm}$.\n'
            '- Khối lượng: $1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1000\\text{ kg}$; $1\\text{ '
            'kg} = 1000\\text{ g}$.\n'
            '- Diện tích: $1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$; $1\\text{ ha} = '
            '10\\,000\\text{ m}^2$.',
  'formulas': [{'category': 'Quy tắc đổi nhanh sang số thập phân',
                'items': [{'name': 'Tấn, tạ, yến, kg',
                           'formula': '$1\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ '
                                      'tấn}$; $1\\text{ kg} = 0{,}001\\text{ tấn}$'},
                          {'name': 'Héc-ta và mét vuông',
                           'formula': '$1\\text{ m}^2 = 0{,}0001\\text{ ha}$; $100\\text{ m}^2 = '
                                      '0{,}01\\text{ ha}$'}]}],
  'example': 'Đổi các số đo sau: $3\\text{ tấn } 45\\text{ kg} = \\dots\\text{ tấn}$ và $2\\text{ ha } '
             '500\\text{ m}^2 = \\dots\\text{ ha}$.',
  'example_answer': 'Ta có $3\\text{ tấn } 45\\text{ kg} = 3{,}045\\text{ tấn}$ và $2\\text{ ha } 500\\text{ '
                    'm}^2 = 2\\dfrac{500}{10\\,000}\\text{ ha} = 2{,}05\\text{ ha}$.',
  'real_life': 'Quy đổi khối lượng nông sản xuất khẩu (tấn, tạ, kg) và diện tích đất canh tác.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số đo $4\\text{ tấn } 5\\text{ tạ}$ bằng bao nhiêu tấn?',
            'options': ['$4{,}5\\text{ tấn}$',
                        '$4{,}05\\text{ tấn}$',
                        '$45\\text{ tấn}$',
                        '$4{,}005\\text{ tấn}$'],
            'answer': 0,
            'solution': 'Vì $1\\text{ tấn} = 10\\text{ tạ}$ nên $5\\text{ tạ} = 0{,}5\\text{ tấn}$, suy ra '
                        '$4{,}5\\text{ tấn}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi $0{,}35\\text{ ha}$ sang mét vuông ta được:',
            'options': ['$350\\text{ m}^2$',
                        '$3500\\text{ m}^2$',
                        '$35\\,000\\text{ m}^2$',
                        '$35\\text{ m}^2$'],
            'answer': 1,
            'solution': 'Ta có $0{,}35 \\times 10\\,000 = 3500\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Ôn tập đo lường**, quy tắc hoặc công thức nào sau đây xác định đúng **Tấn, '
                 'tạ, yến, kg**?',
            'options': ['$2\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; $1\\text{ '
                        'kg} = 0{,}001\\text{ tấn}$',
                        '$1\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; $1\\text{ '
                        'kg} = 0{,}2\\text{ tấn}$',
                        '$1\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; $1\\text{ '
                        'kg} = 0{,}001\\text{ tấn}$',
                        '$1\\text{ m}^2 = 0{,}0001\\text{ ha}$; $100\\text{ m}^2 = 0{,}01\\text{ ha}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 34: Ôn tập đo lường, **Tấn, tạ, yến, kg** được xác '
                        'định bởi: $1\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; '
                        '$1\\text{ kg} = 0{,}001\\text{ tấn}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Ôn tập đo lường**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Héc-ta và mét vuông**?',
            'options': ['$2\\text{ m}^2 = 0{,}0001\\text{ ha}$; $100\\text{ m}^2 = 0{,}01\\text{ ha}$',
                        '$1\\text{ m}^2 = 0{,}0001\\text{ ha}$; $100\\text{ m}^2 = 0{,}2\\text{ ha}$',
                        '$1\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; $1\\text{ '
                        'kg} = 0{,}001\\text{ tấn}$',
                        '$1\\text{ m}^2 = 0{,}0001\\text{ ha}$; $100\\text{ m}^2 = 0{,}01\\text{ ha}$'],
            'answer': 3,
            'solution': 'Trong Bài 34: Ôn tập đo lường, **Héc-ta và mét vuông** có công thức/quy tắc là: '
                        '$1\\text{ m}^2 = 0{,}0001\\text{ ha}$; $100\\text{ m}^2 = 0{,}01\\text{ ha}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $2{,}5\\text{ km} + 850\\text{ m}$ đổi ra ki-lô-mét là:',
            'options': ['$3{,}35\\text{ km}$',
                        '$11\\text{ km}$',
                        '$2{,}585\\text{ km}$',
                        '$3{,}035\\text{ km}$'],
            'answer': 0,
            'solution': 'Đổi $850\\text{ m} = 0{,}85\\text{ km}$, ta có $2{,}5 + 0{,}85 = 3{,}35\\text{ '
                        'km}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 34: Ôn tập đo lường**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Chuyển đổi chính xác giữa các đơn vị đo độ dài, khối lượng, dung tích và diện tích. '
                        '(với dấu ngược lại)',
                        'Chuyển đổi chính xác giữa các đơn vị đo độ dài, khối lượng, dung tích và diện tích.',
                        'Đảo ngược vế của quy tắc: Chuyển đổi chính xác giữa các đơn vị đo độ dài, khối '
                        'lượng, dung tích và diện tích.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chuyển đổi chính xác giữa các '
                        'đơn vị đo độ dài, khối lượng, dung tích và diện tích.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 34: Ôn tập đo lường: Chuyển đổi chính xác giữa các '
                        'đơn vị đo độ dài, khối lượng, dung tích và diện tích.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Số đo $7\\text{ m}^2\\ 5\\text{ dm}^2$ lớn hơn $7{,}5\\text{ m}^2$.',
            'answer': False,
            'solution': 'Ta có $7\\text{ m}^2\\ 5\\text{ dm}^2 = 7{,}05\\text{ m}^2 < 7{,}5\\text{ m}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 34: Ôn tập đo lường**, quy tắc **Tấn, tạ, yến, kg** được xác định bởi '
                 '$1\\text{ tạ} = 0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; $1\\text{ kg} = '
                 '0{,}001\\text{ tấn}$ và khi áp dụng cho ví dụ “Đổi các số đo sau: $3\\text{ tấn } '
                 '45\\text{ kg} = \\dots\\text{ tấn}$ và $2\\text{ ha } 500\\text{ m}^2 = \\dots\\text{ '
                 'ha}$.” ta có lời giải: Ta có $3\\text{ tấn } 45\\text{ kg} = 3{,}045\\text{ tấn}$ và '
                 '$2\\text{ ha } 500\\text{ m}^2 = 2\\dfrac{500}{10\\,000}\\text{ ha} = 2{,}05\\text{ '
                 'ha}$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tấn, tạ, yến, kg** ($1\\text{ tạ} = '
                        '0{,}1\\text{ tấn}$; $1\\text{ yến} = 0{,}01\\text{ tấn}$; $1\\text{ kg} = '
                        '0{,}001\\text{ tấn}$) và lời giải ví dụ minh họa của Bài 34: Ôn tập đo lường.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 34: Ôn tập đo lường** để giải bài toán sau: Đổi các '
                 'số đo sau: $3\\text{ tấn } 45\\text{ kg} = \\dots\\text{ tấn}$ và $2\\text{ ha } '
                 '500\\text{ m}^2 = \\dots\\text{ ha}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $4\\text{ tấn } 45\\text{ kg} = 3{,}045\\text{ tấn}$ và $2\\text{ ha } '
                        '500\\text{ m}^2 = 2\\dfrac{500}{10\\,000}\\text{ ha} = 2{,}05\\text{ ha}$.',
                        'Ta có $3\\text{ tấn } 45\\text{ kg} = 3{,}045\\text{ tấn}$ và $2\\text{ ha } '
                        '500\\text{ m}^2 = 2\\dfrac{10\\,000}{500}\\text{ ha} = 2{,}05\\text{ ha}$.',
                        'Ta có $3\\text{ tấn } 45\\text{ kg} = 3{,}045\\text{ tấn}$ và $2\\text{ ha } '
                        '500\\text{ m}^2 = 2\\dfrac{500}{10\\,000}\\text{ ha} = 2{,}05\\text{ ha}$.',
                        'Ta có $6\\text{ tấn } 45\\text{ kg} = 3{,}045\\text{ tấn}$ và $2\\text{ ha } '
                        '500\\text{ m}^2 = 2\\dfrac{500}{10\\,000}\\text{ ha} = 2{,}05\\text{ ha}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 34: Ôn tập đo lường: Ta có $3\\text{ tấn } 45\\text{ kg} '
                        '= 3{,}045\\text{ tấn}$ và $2\\text{ ha } 500\\text{ m}^2 = '
                        '2\\dfrac{500}{10\\,000}\\text{ ha} = 2{,}05\\text{ ha}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một xe tải chở được tối đa $3{,}5\\text{ tấn}$ hàng. Hiện trên xe đã có $1\\text{ tấn } '
                 '800\\text{ kg}$ hàng. Hỏi xe còn chở thêm được tối đa bao nhiêu tấn hàng nữa?',
            'answer': ['1,7', '1.7'],
            'unit': None,
            'solution': 'Đổi $1\\text{ tấn } 800\\text{ kg} = 1{,}8\\text{ tấn}$. Xe chở thêm được tối đa '
                        '$3{,}5 - 1{,}8 = 1{,}7\\text{ tấn}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd07-ti-so-va-bai-toan-lien-quan',
  'context_title': 'Chủ đề 7: Tỉ số và các bài toán liên quan',
  'context': 'Chủ đề 7 · SGK Toán 5: Tỉ số, tỉ lệ bản đồ, bài toán tổng-tỉ, hiệu-tỉ và tỉ số phần trăm.',
  'title': 'Bài 36: Tỉ số. Tỉ số phần trăm',
  'icon': '📈',
  'description': 'Nhận biết tỉ số của hai đại lượng cùng loại và khái niệm tỉ số phần trăm.',
  'requirements': ['Viết được tỉ số của hai số $a$ và $b$ ($b \\ne 0$) dưới dạng $a : b$ hoặc '
                   '$\\dfrac{a}{b}$.',
                   'Đọc, viết được tỉ số phần trăm và chuyển đổi giữa phân số thập phân, số thập phân với tỉ '
                   'số phần trăm.',
                   'Vận dụng kiến thức của **Bài 36: Tỉ số. Tỉ số phần trăm** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': "('- **Tỉ số** của hai số $a$ và $b$ ($b \\\\ne 0$) là thương trong phép chia số $a$ cho số "
                '$b$, kí hiệu là $a : b$ hay $\\\\dfrac{a}{b}$.\\n- **Tỉ số phần trăm** là tỉ số được viết '
                'dưới dạng phân số thập phân có mẫu số là $100$, thay mẫu số $100$ bằng kí hiệu $\\\\%$ (ví '
                "dụ $\\\\dfrac{25}{100} = 25\\\\%$).',)",
  'theory': '### 1. Lưu ý khi lập tỉ số\n'
            '- Hai đại lượng phải **cùng một đơn vị đo**, và cần giữ đúng thứ tự số nói trước làm tử số, số '
            'nói sau làm mẫu số.\n'
            '### 2. Biểu diễn tỉ số phần trăm\n'
            '- $\\dfrac{3}{4} = \\dfrac{75}{100} = 75\\%$; $0{,}35 = \\dfrac{35}{100} = 35\\%$; $1 = '
            '100\\%$.',
  'formulas': [{'category': 'Tỉ số và tỉ số phần trăm',
                'items': [{'name': 'Tỉ số của a và b', 'formula': '$a : b = \\dfrac{a}{b}$ ($b \\ne 0$)'},
                          {'name': 'Kí hiệu phần trăm',
                           'formula': '$\\dfrac{n}{100} = n\\%$; $1\\% = \\dfrac{1}{100} = 0{,}01$'}]}],
  'example': 'Lớp 5A có $18$ học sinh nam và $22$ học sinh nữ. Viết tỉ số của số học sinh nam và số học sinh '
             'cả lớp, rồi đổi sang tỉ số phần trăm.',
  'example_answer': 'Số học sinh cả lớp là $18 + 22 = 40$ (em). Tỉ số là $\\dfrac{18}{40} = \\dfrac{9}{20} = '
                    '\\dfrac{45}{100} = 45\\%$.',
  'real_life': 'Biểu thị phần trăm dung lượng pin điện thoại, phần trăm giảm giá hoặc thành phần dinh dưỡng '
               'trên bao bì.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tỉ số của $3$ và $5$ được viết là:',
            'options': ['$\\dfrac{5}{3}$', '$\\dfrac{3}{5}$', '$8$', '$15$'],
            'answer': 1,
            'solution': 'Tỉ số của $a$ và $b$ là $\\dfrac{a}{b}$ nên tỉ số của $3$ và $5$ là '
                        '$\\dfrac{3}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số thập phân $0{,}35$ viết dưới dạng tỉ số phần trăm là:',
            'options': ['$3{,}5\\%$', '$350\\%$', '$35\\%$', '$0{,}35\\%$'],
            'answer': 2,
            'solution': 'Ta có $0{,}35 = \\dfrac{35}{100} = 35\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36: Tỉ số. Tỉ số phần trăm**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Tỉ số của a và b**?',
            'options': ['$a : b = \\dfrac{a}{b}$ ($b \\ne 1$)',
                        '$a : b = \\dfrac{b}{a}$ ($b \\ne 0$)',
                        '$a : b = \\dfrac{a}{b}$ ($b \\ne 2$)',
                        '$a : b = \\dfrac{a}{b}$ ($b \\ne 0$)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 36: Tỉ số. Tỉ số phần trăm, **Tỉ số của a và b** '
                        'được xác định bởi: $a : b = \\dfrac{a}{b}$ ($b \\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 36: Tỉ số. Tỉ số phần trăm**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Kí hiệu phần trăm**?',
            'options': ['$\\dfrac{n}{100} = n\\%$; $1\\% = \\dfrac{1}{100} = 0{,}01$',
                        '$\\dfrac{n}{110} = n\\%$; $1\\% = \\dfrac{1}{100} = 0{,}01$',
                        '$\\dfrac{100}{n} = n\\%$; $1\\% = \\dfrac{1}{100} = 0{,}01$',
                        '$\\dfrac{n}{102} = n\\%$; $1\\% = \\dfrac{1}{100} = 0{,}01$'],
            'answer': 0,
            'solution': 'Trong Bài 36: Tỉ số. Tỉ số phần trăm, **Kí hiệu phần trăm** có công thức/quy tắc '
                        'là: $\\dfrac{n}{100} = n\\%$; $1\\% = \\dfrac{1}{100} = 0{,}01$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phân số $\\dfrac{3}{5}$ viết dưới dạng tỉ số phần trăm là:',
            'options': ['$35\\%$', '$60\\%$', '$30\\%$', '$6\\%$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{3}{5} = \\dfrac{60}{100} = 60\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 36: Tỉ số. Tỉ số phần trăm**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Viết được tỉ số của hai số $a$ và $b$ ($b \\ne 1$) dưới dạng $a : b$ hoặc '
                        '$\\dfrac{a}{b}$.',
                        'Viết được tỉ số của hai số $a$ và $b$ ($b \\ne 0$) dưới dạng $a : b$ hoặc '
                        '$\\dfrac{b}{a}$.',
                        'Viết được tỉ số của hai số $a$ và $b$ ($b \\ne 0$) dưới dạng $a : b$ hoặc '
                        '$\\dfrac{a}{b}$.',
                        'Viết được tỉ số của hai số $a$ và $b$ ($b \\ne 2$) dưới dạng $a : b$ hoặc '
                        '$\\dfrac{a}{b}$.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 36: Tỉ số. Tỉ số phần trăm: Viết được tỉ số của hai '
                        'số $a$ và $b$ ($b \\ne 0$) dưới dạng $a : b$ hoặc $\\dfrac{a}{b}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Tỉ số của $40\\text{ cm}$ và $1\\text{ m}$ là $\\dfrac{2}{5}$.',
            'answer': True,
            'solution': 'Đổi $1\\text{ m} = 100\\text{ cm}$, tỉ số là $\\dfrac{40}{100} = \\dfrac{2}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 36: Tỉ số. Tỉ số phần trăm**, quy tắc **Tỉ số của a và b** được xác định bởi '
                 '$a : b = \\dfrac{a}{b}$ ($b \\ne 0$) và khi áp dụng cho ví dụ “Lớp 5A có $18$ học sinh nam '
                 'và $22$ học sinh nữ. Viết tỉ số của số học sinh nam và số học sinh cả lớp, rồi đổi sang tỉ '
                 'số phần trăm.” ta có lời giải: Số học sinh cả lớp là $18 + 22 = 40$ (em). Tỉ số là '
                 '$\\dfrac{18}{40} = \\dfrac{9}{20} = \\dfrac{45}{100} = 45\\%$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tỉ số của a và b** ($a : b = '
                        '\\dfrac{a}{b}$ ($b \\ne 0$)) và lời giải ví dụ minh họa của Bài 36: Tỉ số. Tỉ số '
                        'phần trăm.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 36: Tỉ số. Tỉ số phần trăm** để giải bài toán sau: '
                 'Lớp 5A có $18$ học sinh nam và $22$ học sinh nữ. Viết tỉ số của số học sinh nam và số học '
                 'sinh cả lớp, rồi đổi sang tỉ số phần trăm. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số học sinh cả lớp là $18 - 22 = 40$ (em). Tỉ số là $\\dfrac{18}{40} = '
                        '\\dfrac{9}{20} = \\dfrac{45}{100} = 45\\%$.',
                        'Số học sinh cả lớp là $18 + 22 = 40$ (em). Tỉ số là $\\dfrac{40}{18} = '
                        '\\dfrac{9}{20} = \\dfrac{45}{100} = 45\\%$.',
                        'Số học sinh cả lớp là $36 + 22 = 40$ (em). Tỉ số là $\\dfrac{18}{40} = '
                        '\\dfrac{9}{20} = \\dfrac{45}{100} = 45\\%$.',
                        'Số học sinh cả lớp là $18 + 22 = 40$ (em). Tỉ số là $\\dfrac{18}{40} = '
                        '\\dfrac{9}{20} = \\dfrac{45}{100} = 45\\%$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 36: Tỉ số. Tỉ số phần trăm: Số học sinh cả lớp là $18 + '
                        '22 = 40$ (em). Tỉ số là $\\dfrac{18}{40} = \\dfrac{9}{20} = \\dfrac{45}{100} = '
                        '45\\%$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một vườn cây, số cây cam chiếm $38\\%$, số cây bưởi chiếm $27\\%$, còn lại là cây '
                 'xoài. Hỏi số cây xoài chiếm bao nhiêu phần trăm tổng số cây trong vườn?',
            'answer': ['35', '35%'],
            'unit': None,
            'solution': 'Tỉ số phần trăm cây xoài là $100\\% - 38\\% - 27\\% = 35\\%$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd07-ti-so-va-bai-toan-lien-quan',
  'context_title': 'Chủ đề 7: Tỉ số và các bài toán liên quan',
  'context': 'Chủ đề 7 · SGK Toán 5: Tỉ số, tỉ lệ bản đồ, bài toán tổng-tỉ, hiệu-tỉ và tỉ số phần trăm.',
  'title': 'Bài 37: Tỉ lệ bản đồ và ứng dụng',
  'icon': '📈',
  'description': 'Hiểu ý nghĩa của tỉ lệ bản đồ và cách tính độ dài thật hoặc độ dài thu nhỏ trên bản đồ.',
  'requirements': ['Hiểu được ý nghĩa của tỉ lệ bản đồ dạng $1 : k$ (hoặc $\\dfrac{1}{k}$).',
                   'Tính được độ dài thật khi biết độ dài trên bản đồ và ngược lại.',
                   'Vận dụng kiến thức của **Bài 37: Tỉ lệ bản đồ và ứng dụng** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- **Tỉ lệ bản đồ** $1 : k$ cho biết độ dài trên bản đồ đã được thu nhỏ đi $k$ lần so với độ '
                'dài thật ngoài thực tế.\n'
                '- Ví dụ: tỉ lệ $1 : 1000$ nghĩa là $1\\text{ cm}$ trên bản đồ ứng với $1000\\text{ cm} = '
                '10\\text{ m}$ ngoài thực tế.',
  'theory': '### 1. Tìm độ dài thật ngoài thực tế\n'
            '- Muốn tìm độ dài thật, ta lấy độ dài thu nhỏ trên bản đồ (cùng đơn vị) nhân với mẫu số $k$ của '
            'tỉ lệ bản đồ, sau đó đổi sang đơn vị thích hợp ($\\text{m}, \\text{km}$).\n'
            '### 2. Tìm độ dài thu nhỏ trên bản đồ\n'
            '- Đổi độ dài thật về đơn vị $\\text{cm}$ (hoặc $\\text{mm}$), rồi chia cho $k$.',
  'formulas': [{'category': 'Công thức tỉ lệ bản đồ 1 : k',
                'items': [{'name': 'Tìm độ dài thật',
                           'formula': '$\\text{Độ dài thật} = \\text{Độ dài trên bản đồ} \\times k$'},
                          {'name': 'Tìm độ dài trên bản đồ',
                           'formula': '$\\text{Độ dài trên bản đồ} = \\text{Độ dài thật} : k$'}]}],
  'example': 'Trên bản đồ tỉ lệ $1 : 500\\,000$, khoảng cách giữa hai địa điểm là $4\\text{ cm}$. Tính '
             'khoảng cách thực tế theo đơn vị ki-lô-mét.',
  'example_answer': 'Khoảng cách thực tế là $4 \\times 500\\,000 = 2\\,000\\,000\\text{ cm} = 20\\text{ '
                    'km}$.',
  'real_life': 'Đọc bản đồ địa lí, bản vẽ thiết kế nhà ở và tính khoảng cách giữa các thành phố.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trên bản đồ tỉ lệ $1 : 1000$, độ dài $1\\text{ cm}$ ứng với độ dài thật là:',
            'options': ['$1000\\text{ m}$', '$100\\text{ m}$', '$10\\text{ m}$', '$1\\text{ m}$'],
            'answer': 2,
            'solution': 'Ta có $1\\text{ cm} \\times 1000 = 1000\\text{ cm} = 10\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu độ dài trên bản đồ là $3\\text{ cm}$ và tỉ lệ bản đồ là $1 : 200$ thì độ dài thật là:',
            'options': ['$200\\text{ cm}$', '$60\\text{ cm}$', '$6000\\text{ cm}$', '$600\\text{ cm}$'],
            'answer': 3,
            'solution': 'Độ dài thật là $3 \\times 200 = 600\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 37: Tỉ lệ bản đồ và ứng dụng**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Tìm độ dài thật**?',
            'options': ['$\\text{Độ dài thật} = \\text{Độ dài trên bản đồ} \\times k$',
                        '$\\text{Độ dài thật} = \\text{Độ dài trên bản đồ} : k$',
                        'Đảo ngược vế của quy tắc: $\\text{Độ dài thật} = \\text{Độ dài trên bản đồ} \\times '
                        'k$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Độ dài thật} = '
                        '\\text{Độ dài trên bản đồ} \\times k$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 37: Tỉ lệ bản đồ và ứng dụng, **Tìm độ dài thật** '
                        'được xác định bởi: $\\text{Độ dài thật} = \\text{Độ dài trên bản đồ} \\times k$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 37: Tỉ lệ bản đồ và ứng dụng**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Tìm độ dài trên bản đồ**?',
            'options': ['$\\text{Độ dài trên bản đồ} = \\text{Độ dài thật} : k$ (với dấu ngược lại)',
                        '$\\text{Độ dài trên bản đồ} = \\text{Độ dài thật} : k$',
                        'Đảo ngược vế của quy tắc: $\\text{Độ dài trên bản đồ} = \\text{Độ dài thật} : k$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Độ dài trên bản đồ} = '
                        '\\text{Độ dài thật} : k$'],
            'answer': 1,
            'solution': 'Trong Bài 37: Tỉ lệ bản đồ và ứng dụng, **Tìm độ dài trên bản đồ** có công thức/quy '
                        'tắc là: $\\text{Độ dài trên bản đồ} = \\text{Độ dài thật} : k$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một sân bóng dài $60\\text{ m}$ được vẽ trên bản đồ tỉ lệ $1 : 1000$. Độ dài sân bóng trên '
                 'bản đồ là:',
            'options': ['$6\\text{ dm}$', '$6\\text{ mm}$', '$6\\text{ cm}$', '$60\\text{ cm}$'],
            'answer': 2,
            'solution': 'Đổi $60\\text{ m} = 6000\\text{ cm}$. Độ dài trên bản đồ là $6000 : 1000 = 6\\text{ '
                        'cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 37: Tỉ lệ bản đồ và ứng dụng**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Hiểu được ý nghĩa của tỉ lệ bản đồ dạng $2 : k$ (hoặc $\\dfrac{1}{k}$).',
                        'Hiểu được ý nghĩa của tỉ lệ bản đồ dạng $1 : k$ (hoặc $\\dfrac{k}{1}$).',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)',
                        'Hiểu được ý nghĩa của tỉ lệ bản đồ dạng $1 : k$ (hoặc $\\dfrac{1}{k}$).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 37: Tỉ lệ bản đồ và ứng dụng: Hiểu được ý nghĩa của '
                        'tỉ lệ bản đồ dạng $1 : k$ (hoặc $\\dfrac{1}{k}$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trên bản đồ tỉ lệ $1 : 1\\,000\\,000$, quãng đường dài $1\\text{ cm}$ ứng với $10\\text{ '
                 'km}$ ngoài thực tế.',
            'answer': True,
            'solution': 'Vì $1\\,000\\,000\\text{ cm} = 10\\,000\\text{ m} = 10\\text{ km}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 37: Tỉ lệ bản đồ và ứng dụng**, quy tắc **Tìm độ dài thật** được xác định bởi '
                 '$\\text{Độ dài thật} = \\text{Độ dài trên bản đồ} \\times k$ và khi áp dụng cho ví dụ '
                 '“Trên bản đồ tỉ lệ $1 : 500\\,000$, khoảng cách giữa hai địa điểm là $4\\text{ cm}$. Tính '
                 'khoảng cách thực tế theo đơn vị ki-lô-mét.” ta có lời giải: Khoảng cách thực tế là $4 '
                 '\\times 500\\,000 = 2\\,000\\,000\\text{ cm} = 20\\text{ km}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tìm độ dài thật** ($\\text{Độ dài thật} '
                        '= \\text{Độ dài trên bản đồ} \\times k$) và lời giải ví dụ minh họa của Bài 37: Tỉ '
                        'lệ bản đồ và ứng dụng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 37: Tỉ lệ bản đồ và ứng dụng** để giải bài toán '
                 'sau: Trên bản đồ tỉ lệ $1 : 500\\,000$, khoảng cách giữa hai địa điểm là $4\\text{ cm}$. '
                 'Tính khoảng cách thực tế theo đơn vị ki-lô-mét. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Khoảng cách thực tế là $4 \\times 500\\,000 = 2\\,000\\,000\\text{ cm} = 20\\text{ '
                        'km}$.',
                        'Khoảng cách thực tế là $4 : 500\\,000 = 2\\,000\\,000\\text{ cm} = 20\\text{ km}$.',
                        'Khoảng cách thực tế là $4 \\times 500\\,000 = 2\\,000\\,000\\text{ cm} = 19\\text{ '
                        'km}$.',
                        'Khoảng cách thực tế là $8 \\times 500\\,000 = 2\\,000\\,000\\text{ cm} = 20\\text{ '
                        'km}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 37: Tỉ lệ bản đồ và ứng dụng: Khoảng cách thực tế là $4 '
                        '\\times 500\\,000 = 2\\,000\\,000\\text{ cm} = 20\\text{ km}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên bản đồ tỉ lệ $1 : 2\\,000\\,000$, quãng đường từ tỉnh A đến tỉnh B đo được $5\\text{ '
                 'cm}$. Quãng đường thật dài bao nhiêu ki-lô-mét?',
            'answer': ['100'],
            'unit': None,
            'solution': 'Độ dài thật là $5 \\times 2\\,000\\,000 = 10\\,000\\,000\\text{ cm} = 100\\text{ '
                        'km}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd07-ti-so-va-bai-toan-lien-quan',
  'context_title': 'Chủ đề 7: Tỉ số và các bài toán liên quan',
  'context': 'Chủ đề 7 · SGK Toán 5: Tỉ số, tỉ lệ bản đồ, bài toán tổng-tỉ, hiệu-tỉ và tỉ số phần trăm.',
  'title': 'Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó',
  'icon': '📈',
  'description': 'Phương pháp sơ đồ đoạn thẳng để giải bài toán tìm hai số khi biết tổng và tỉ số của hai số '
                 'đó.',
  'requirements': ['Vẽ được sơ đồ đoạn thẳng biểu thị tổng và tỉ số của hai số.',
                   'Giải thành thạo bài toán tìm hai số khi biết tổng và tỉ số theo $4$ bước chuẩn.',
                   'Vận dụng kiến thức của **Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Khi biết **tổng** của hai số và **tỉ số** $\\dfrac{m}{n}$ của chúng, ta coi số thứ nhất '
                'gồm $m$ phần bằng nhau, số thứ hai gồm $n$ phần như thế.\n'
                '- Bước giải: Tìm **tổng số phần bằng nhau** $(m + n) \\rightarrow$ Tìm giá trị $1$ phần '
                '$\\rightarrow$ Tìm số bé và số lớn.',
  'theory': '### 1. Các bước giải bài toán Tổng – Tỉ\n'
            '- Bước 1: Vẽ sơ đồ đoạn thẳng.\n'
            '- Bước 2: Tìm tổng số phần bằng nhau: $m + n$ (phần).\n'
            '- Bước 3: Giá trị một phần = $\\text{Tổng} : (m + n)$.\n'
            '- Bước 4: Số thứ nhất = Giá trị $1$ phần $\\times m$; Số thứ hai = Giá trị $1$ phần $\\times '
            'n$.',
  'formulas': [{'category': 'Bài toán Tổng – Tỉ (tỉ số m/n)',
                'items': [{'name': 'Tổng số phần bằng nhau', 'formula': '$P = m + n$'},
                          {'name': 'Hai số cần tìm',
                           'formula': '$\\text{Số bé} = (\\text{Tổng} : P) \\times m$; $\\text{Số lớn} = '
                                      '(\\text{Tổng} : P) \\times n$'}]}],
  'example': 'Tổng của hai số là $45$, tỉ số của hai số đó là $\\dfrac{2}{3}$. Tìm hai số đó.',
  'example_answer': 'Tổng số phần bằng nhau là $2 + 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; số '
                    'lớn là $45 - 18 = 27$.',
  'real_life': 'Tính số học sinh nam và nữ trong lớp, chiều dài và chiều rộng mảnh vườn khi biết chu vi và '
               'tỉ số.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai số có tỉ số là $\\dfrac{3}{5}$. Tổng số phần bằng nhau của hai số đó là:',
            'options': ['$2$ phần', '$15$ phần', '$5$ phần', '$8$ phần'],
            'answer': 3,
            'solution': 'Tổng số phần bằng nhau là $3 + 5 = 8$ (phần).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng của hai số là $60$, tỉ số của chúng là $\\dfrac{1}{4}$. Số lớn là:',
            'options': ['$48$', '$12$', '$15$', '$45$'],
            'answer': 0,
            'solution': 'Tổng số phần là $1 + 4 = 5$ (phần). Số lớn là $(60 : 5) \\times 4 = 48$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Tổng số phần bằng nhau**?',
            'options': ['$P = m - n$',
                        '$P = m + n$',
                        'Đảo ngược vế của quy tắc: $P = m + n$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P = m + n$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số '
                        'đó, **Tổng số phần bằng nhau** được xác định bởi: $P = m + n$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Hai số cần tìm**?',
            'options': ['$\\text{Số bé} = (\\text{Tổng} : P) : m$; $\\text{Số lớn} = (\\text{Tổng} : P) '
                        '\\times n$',
                        'Đảo ngược vế của quy tắc: $\\text{Số bé} = (\\text{Tổng} : P) \\times m$; '
                        '$\\text{Số lớn} = (\\text{Tổng} : P) \\times n$',
                        '$\\text{Số bé} = (\\text{Tổng} : P) \\times m$; $\\text{Số lớn} = (\\text{Tổng} : '
                        'P) \\times n$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số bé} = (\\text{Tổng} '
                        ': P) \\times m$; $\\text{Số lớn} = (\\text{Tổng} : P) \\times n$'],
            'answer': 2,
            'solution': 'Trong Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó, **Hai số cần tìm** '
                        'có công thức/quy tắc là: $\\text{Số bé} = (\\text{Tổng} : P) \\times m$; $\\text{Số '
                        'lớn} = (\\text{Tổng} : P) \\times n$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng số học sinh của hai lớp 5A và 5B là $72$ em, số học sinh lớp 5A bằng $\\dfrac{4}{5}$ '
                 'số học sinh lớp 5B. Lớp 5B có:',
            'options': ['$32$ học sinh', '$36$ học sinh', '$45$ học sinh', '$40$ học sinh'],
            'answer': 3,
            'solution': 'Tổng số phần là $4 + 5 = 9$ (phần). Lớp 5B có $(72 : 9) \\times 5 = 40$ (học sinh).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Vẽ được sơ đồ đoạn thẳng biểu thị tổng và tỉ số của hai số.',
                        'Vẽ được sơ đồ đoạn thẳng biểu thị tổng và tỉ số của hai số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Vẽ được sơ đồ đoạn thẳng biểu thị tổng và tỉ số của hai '
                        'số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Vẽ được sơ đồ đoạn thẳng biểu '
                        'thị tổng và tỉ số của hai số.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó: '
                        'Vẽ được sơ đồ đoạn thẳng biểu thị tổng và tỉ số của hai số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nếu hai số có tổng bằng $100$ và số lớn gấp $3$ lần số bé thì số bé bằng $25$.',
            'answer': True,
            'solution': 'Tỉ số là $\\dfrac{1}{3}$, tổng số phần là $1 + 3 = 4$ phần, số bé là $100 : 4 = '
                        '25$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó**, quy tắc **Tổng số phần '
                 'bằng nhau** được xác định bởi $P = m + n$ và khi áp dụng cho ví dụ “Tổng của hai số là '
                 '$45$, tỉ số của hai số đó là $\\dfrac{2}{3}$. Tìm hai số đó.” ta có lời giải: Tổng số phần '
                 'bằng nhau là $2 + 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; số lớn là $45 - 18 = '
                 '27$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tổng số phần bằng nhau** ($P = m + n$) '
                        'và lời giải ví dụ minh họa của Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số '
                        'đó.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số '
                 'đó** để giải bài toán sau: Tổng của hai số là $45$, tỉ số của hai số đó là '
                 '$\\dfrac{2}{3}$. Tìm hai số đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tổng số phần bằng nhau là $2 - 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; '
                        'số lớn là $45 - 18 = 27$.',
                        'Tổng số phần bằng nhau là $2 + 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; '
                        'số lớn là $45 - 18 = 27$.',
                        'Tổng số phần bằng nhau là $2 + 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; '
                        'số lớn là $45 - 18 = 26$.',
                        'Tổng số phần bằng nhau là $4 + 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; '
                        'số lớn là $45 - 18 = 27$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 38: Tìm hai số khi biết tổng và tỉ số của hai số đó: '
                        'Tổng số phần bằng nhau là $2 + 3 = 5$ (phần). Số bé là $(45 : 5) \\times 2 = 18$; '
                        'số lớn là $45 - 18 = 27$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chữ nhật có nửa chu vi là $56\\text{ m}$, chiều rộng bằng $\\dfrac{3}{5}$ chiều '
                 'dài. Tính chiều dài hình chữ nhật đó theo đơn vị mét.',
            'answer': ['35'],
            'unit': None,
            'solution': 'Tổng số phần bằng nhau là $3 + 5 = 8$ (phần). Chiều dài là $(56 : 8) \\times 5 = '
                        '35$ ($\\text{m}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd07-ti-so-va-bai-toan-lien-quan',
  'context_title': 'Chủ đề 7: Tỉ số và các bài toán liên quan',
  'context': 'Chủ đề 7 · SGK Toán 5: Tỉ số, tỉ lệ bản đồ, bài toán tổng-tỉ, hiệu-tỉ và tỉ số phần trăm.',
  'title': 'Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó',
  'icon': '📈',
  'description': 'Phương pháp giải bài toán tìm hai số khi biết hiệu và tỉ số của hai số đó.',
  'requirements': ['Phân biệt rõ bài toán Hiệu – Tỉ với bài toán Tổng – Tỉ và vẽ được sơ đồ đoạn thẳng.',
                   'Giải đúng các bài toán tìm hai số khi biết hiệu và tỉ số trong thực tế.',
                   'Vận dụng kiến thức của **Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Khi biết **hiệu** của hai số và **tỉ số** $\\dfrac{m}{n}$ ($m < n$) của chúng, hiệu của '
                'hai số ứng với **hiệu số phần bằng nhau** $(n - m)$.\n'
                '- Bước giải: Tìm **hiệu số phần bằng nhau** $(n - m) \\rightarrow$ Tìm giá trị $1$ phần '
                '$\\rightarrow$ Tìm số bé và số lớn.',
  'theory': '### 1. Các bước giải bài toán Hiệu – Tỉ\n'
            '- Bước 1: Vẽ sơ đồ đoạn thẳng.\n'
            '- Bước 2: Tìm hiệu số phần bằng nhau: $n - m$ (phần).\n'
            '- Bước 3: Giá trị một phần = $\\text{Hiệu} : (n - m)$.\n'
            '- Bước 4: Số bé = Giá trị $1$ phần $\\times m$; Số lớn = Số bé $+ \\text{Hiệu}$.',
  'formulas': [{'category': 'Bài toán Hiệu – Tỉ (tỉ số m/n với m < n)',
                'items': [{'name': 'Hiệu số phần bằng nhau', 'formula': '$H = n - m$'},
                          {'name': 'Hai số cần tìm',
                           'formula': '$\\text{Số bé} = (\\text{Hiệu} : H) \\times m$; $\\text{Số lớn} = '
                                      '(\\text{Hiệu} : H) \\times n$'}]}],
  'example': 'Hiệu của hai số là $12$, tỉ số của hai số đó là $\\dfrac{3}{5}$. Tìm hai số đó.',
  'example_answer': 'Hiệu số phần bằng nhau là $5 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; số '
                    'lớn là $18 + 12 = 30$.',
  'real_life': 'Bài toán tính tuổi của hai người khi biết hiệu số tuổi (không đổi theo thời gian) và tỉ số '
               'tuổi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai số có tỉ số là $\\dfrac{2}{7}$. Hiệu số phần bằng nhau của hai số đó là:',
            'options': ['$5$ phần', '$9$ phần', '$14$ phần', '$7$ phần'],
            'answer': 0,
            'solution': 'Hiệu số phần bằng nhau là $7 - 2 = 5$ (phần).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hiệu của hai số là $18$, tỉ số của chúng là $\\dfrac{2}{5}$. Số bé là:',
            'options': ['$6$', '$12$', '$30$', '$18$'],
            'answer': 1,
            'solution': 'Hiệu số phần là $5 - 2 = 3$ (phần). Số bé là $(18 : 3) \\times 2 = 12$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Hiệu số phần bằng nhau**?',
            'options': ['$H = n + m$',
                        'Đảo ngược vế của quy tắc: $H = n - m$',
                        '$H = n - m$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $H = n - m$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số '
                        'đó, **Hiệu số phần bằng nhau** được xác định bởi: $H = n - m$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Hai số cần tìm**?',
            'options': ['$\\text{Số bé} = (\\text{Hiệu} : H) : m$; $\\text{Số lớn} = (\\text{Hiệu} : H) '
                        '\\times n$',
                        'Đảo ngược vế của quy tắc: $\\text{Số bé} = (\\text{Hiệu} : H) \\times m$; '
                        '$\\text{Số lớn} = (\\text{Hiệu} : H) \\times n$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số bé} = (\\text{Hiệu} '
                        ': H) \\times m$; $\\text{Số lớn} = (\\text{Hiệu} : H) \\times n$',
                        '$\\text{Số bé} = (\\text{Hiệu} : H) \\times m$; $\\text{Số lớn} = (\\text{Hiệu} : '
                        'H) \\times n$'],
            'answer': 3,
            'solution': 'Trong Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó, **Hai số cần tìm** '
                        'có công thức/quy tắc là: $\\text{Số bé} = (\\text{Hiệu} : H) \\times m$; $\\text{Số '
                        'lớn} = (\\text{Hiệu} : H) \\times n$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mẹ hơn con $28$ tuổi và tuổi con bằng $\\dfrac{1}{5}$ tuổi mẹ. Tuổi của mẹ hiện nay là:',
            'options': ['$35$ tuổi', '$28$ tuổi', '$30$ tuổi', '$40$ tuổi'],
            'answer': 0,
            'solution': 'Hiệu số phần là $5 - 1 = 4$ (phần). Tuổi mẹ là $(28 : 4) \\times 5 = 35$ (tuổi).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Phân biệt rõ bài toán Hiệu – Tỉ với bài toán Tổng – Tỉ và vẽ được sơ đồ đoạn thẳng. '
                        '(với dấu ngược lại)',
                        'Phân biệt rõ bài toán Hiệu – Tỉ với bài toán Tổng – Tỉ và vẽ được sơ đồ đoạn thẳng.',
                        'Đảo ngược vế của quy tắc: Phân biệt rõ bài toán Hiệu – Tỉ với bài toán Tổng – Tỉ và '
                        'vẽ được sơ đồ đoạn thẳng.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phân biệt rõ bài toán Hiệu – Tỉ '
                        'với bài toán Tổng – Tỉ và vẽ được sơ đồ đoạn thẳng.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó: '
                        'Phân biệt rõ bài toán Hiệu – Tỉ với bài toán Tổng – Tỉ và vẽ được sơ đồ đoạn '
                        'thẳng.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nếu hiệu hai số là $20$ và tỉ số là $\\dfrac{3}{7}$ thì số bé bằng $15$.',
            'answer': True,
            'solution': 'Hiệu số phần là $7 - 3 = 4$ (phần), số bé là $(20 : 4) \\times 3 = 15$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó**, quy tắc **Hiệu số phần '
                 'bằng nhau** được xác định bởi $H = n - m$ và khi áp dụng cho ví dụ “Hiệu của hai số là '
                 '$12$, tỉ số của hai số đó là $\\dfrac{3}{5}$. Tìm hai số đó.” ta có lời giải: Hiệu số phần '
                 'bằng nhau là $5 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; số lớn là $18 + 12 = '
                 '30$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hiệu số phần bằng nhau** ($H = n - m$) '
                        'và lời giải ví dụ minh họa của Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số '
                        'đó.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số '
                 'đó** để giải bài toán sau: Hiệu của hai số là $12$, tỉ số của hai số đó là '
                 '$\\dfrac{3}{5}$. Tìm hai số đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Hiệu số phần bằng nhau là $5 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; '
                        'số lớn là $18 - 12 = 30$.',
                        'Hiệu số phần bằng nhau là $5 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; '
                        'số lớn là $18 + 12 = 29$.',
                        'Hiệu số phần bằng nhau là $5 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; '
                        'số lớn là $18 + 12 = 30$.',
                        'Hiệu số phần bằng nhau là $10 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; '
                        'số lớn là $18 + 12 = 30$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 39: Tìm hai số khi biết hiệu và tỉ số của hai số đó: '
                        'Hiệu số phần bằng nhau là $5 - 3 = 2$ (phần). Số bé là $(12 : 2) \\times 3 = 18$; '
                        'số lớn là $18 + 12 = 30$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mảnh vườn hình chữ nhật có chiều dài hơn chiều rộng $24\\text{ m}$ và chiều rộng bằng '
                 '$\\dfrac{3}{7}$ chiều dài. Tính diện tích mảnh vườn đó theo đơn vị mét vuông.',
            'answer': ['756'],
            'unit': None,
            'solution': 'Hiệu số phần là $7 - 3 = 4$ (phần). Chiều rộng là $(24 : 4) \\times 3 = 18\\text{ '
                        'm}$, chiều dài là $18 + 24 = 42\\text{ m}$. Diện tích là $42 \\times 18 = '
                        '756\\text{ m}^2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd07-ti-so-va-bai-toan-lien-quan',
  'context_title': 'Chủ đề 7: Tỉ số và các bài toán liên quan',
  'context': 'Chủ đề 7 · SGK Toán 5: Tỉ số, tỉ lệ bản đồ, bài toán tổng-tỉ, hiệu-tỉ và tỉ số phần trăm.',
  'title': 'Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của một số',
  'icon': '📈',
  'description': 'Cách tìm tỉ số phần trăm của hai số và tìm giá trị phần trăm của một số cho trước.',
  'requirements': ['Tìm được tỉ số phần trăm của hai số $a$ và $b$ theo quy tắc lấy thương nhân nhẩm với '
                   '$100$ rồi viết kí hiệu $\\%$.',
                   'Tính được giá trị $m\\%$ của một số $A$ và vận dụng vào bài toán giảm giá, lãi suất.',
                   'Vận dụng kiến thức của **Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của '
                   'một số** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Muốn tìm **tỉ số phần trăm của hai số $a$ và $b$**, ta tìm thương $a : b$, sau đó nhân '
                'thương đó với $100$ và viết thêm kí hiệu $\\%$ vào bên phải tích tìm được.\n'
                '- Muốn tìm **$m\\%$ của một số $A$**, ta lấy $A \\times m : 100$ (hoặc $A : 100 \\times '
                'm$).',
  'theory': '### 1. Tìm tỉ số phần trăm của hai số\n'
            '- Ví dụ: tỉ số phần trăm của $18$ và $24$ là $18 : 24 = 0{,}75 = 75\\%$.\n'
            '### 2. Tìm giá trị phần trăm của một số\n'
            '- Ví dụ: $15\\%$ của $320$ là $320 \\times 15 : 100 = 48$.',
  'formulas': [{'category': 'Hai dạng toán tỉ số phần trăm',
                'items': [{'name': 'Tỉ số phần trăm của a và b', 'formula': '$(a : b) \\times 100\\%$'},
                          {'name': 'Giá trị m% của số A', 'formula': '$A \\times m : 100$'},
                          {'name': 'Giá sau khi giảm m%',
                           'formula': '$\\text{Giá mới} = \\text{Giá cũ} \\times (100 - m) : 100$'}]}],
  'example': 'Một chiếc áo giá $250\\,000$ đồng được giảm giá $20\\%$. Tính giá chiếc áo sau khi giảm.',
  'example_answer': 'Số tiền được giảm là $250\\,000 \\times 20 : 100 = 50\\,000$ (đồng). Giá sau khi giảm '
                    'là $250\\,000 - 50\\,000 = 200\\,000$ (đồng).',
  'real_life': 'Tính tiền khuyến mãi khi mua sắm, tiền lãi tiết kiệm ngân hàng và tỉ lệ hoàn thành kế hoạch.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn tìm $20\\%$ của $150$, ta thực hiện phép tính nào?',
            'options': ['$150 : 20$', '$150 \\times 20 : 100$', '$150 \\times 100 : 20$', '$150 + 20$'],
            'answer': 1,
            'solution': 'Muốn tìm $m\\%$ của $A$, ta tính $A \\times m : 100$, tức là $150 \\times 20 : 100 '
                        '= 30$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tỉ số phần trăm của $9$ và $12$ là:',
            'options': ['$7{,}5\\%$', '$133\\%$', '$75\\%$', '$0{,}75\\%$'],
            'answer': 2,
            'solution': 'Ta có $9 : 12 = 0{,}75 = 75\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của một số**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Tỉ số phần trăm của a và b**?',
            'options': ['$(a : b) : 100\\%$',
                        '$(a : b) \\times 99\\%$',
                        '$(a : b) \\times 102\\%$',
                        '$(a : b) \\times 100\\%$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần '
                        'trăm của một số, **Tỉ số phần trăm của a và b** được xác định bởi: $(a : b) \\times '
                        '100\\%$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của một số**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Giá trị m% của số A**?',
            'options': ['$A \\times m : 100$', '$A : m : 100$', '$A \\times m : 99$', '$A \\times m : 102$'],
            'answer': 0,
            'solution': 'Trong Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của một số, **Giá '
                        'trị m% của số A** có công thức/quy tắc là: $A \\times m : 100$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một lớp có $40$ học sinh, trong đó có $18$ học sinh nữ. Tỉ số phần trăm của số học sinh nữ '
                 'và số học sinh cả lớp là:',
            'options': ['$40\\%$', '$45\\%$', '$55\\%$', '$18\\%$'],
            'answer': 1,
            'solution': 'Ta có $18 : 40 = 0{,}45 = 45\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của '
                 'một số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tìm được tỉ số phần trăm của hai số $a$ và $b$ theo quy tắc lấy thương nhân nhẩm '
                        'với $110$ rồi viết kí hiệu $\\%$.',
                        'Tìm được tỉ số phần trăm của hai số $a$ và $b$ theo quy tắc lấy thương nhân nhẩm '
                        'với $99$ rồi viết kí hiệu $\\%$.',
                        'Tìm được tỉ số phần trăm của hai số $a$ và $b$ theo quy tắc lấy thương nhân nhẩm '
                        'với $100$ rồi viết kí hiệu $\\%$.',
                        'Tìm được tỉ số phần trăm của hai số $a$ và $b$ theo quy tắc lấy thương nhân nhẩm '
                        'với $102$ rồi viết kí hiệu $\\%$.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần '
                        'trăm của một số: Tìm được tỉ số phần trăm của hai số $a$ và $b$ theo quy tắc lấy '
                        'thương nhân nhẩm với $100$ rồi viết kí hiệu $\\%$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Giá trị $25\\%$ của $80$ bằng $32$.',
            'answer': False,
            'solution': 'Ta có $80 \\times 25 : 100 = 20$ chứ không phải $32$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm của một số**, quy tắc '
                 '**Tỉ số phần trăm của a và b** được xác định bởi $(a : b) \\times 100\\%$ và khi áp dụng '
                 'cho ví dụ “Một chiếc áo giá $250\\,000$ đồng được giảm giá $20\\%$. Tính giá chiếc áo sau '
                 'khi giảm.” ta có lời giải: Số tiền được giảm là $250\\,000 \\times 20 : 100 = 50\\,000$ '
                 '(đồng). Giá sau khi giảm là $250\\,000 - 50\\,000 = 200\\,000$ (đồng).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tỉ số phần trăm của a và b** ($(a : b) '
                        '\\times 100\\%$) và lời giải ví dụ minh họa của Bài 40: Tìm tỉ số phần trăm của hai '
                        'số và giá trị phần trăm của một số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần '
                 'trăm của một số** để giải bài toán sau: Một chiếc áo giá $250\\,000$ đồng được giảm giá '
                 '$20\\%$. Tính giá chiếc áo sau khi giảm. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số tiền được giảm là $250\\,000 \\times 20 : 100 = 50\\,000$ (đồng). Giá sau khi '
                        'giảm là $250\\,000 + 50\\,000 = 200\\,000$ (đồng).',
                        'Số tiền được giảm là $250\\,000 \\times 20 : 100 = 50\\,000$ (đồng). Giá sau khi '
                        'giảm là $250\\,000 - 50\\,000 = 200\\,1$ (đồng).',
                        'Số tiền được giảm là $252\\,000 \\times 20 : 100 = 50\\,000$ (đồng). Giá sau khi '
                        'giảm là $250\\,000 - 50\\,000 = 200\\,000$ (đồng).',
                        'Số tiền được giảm là $250\\,000 \\times 20 : 100 = 50\\,000$ (đồng). Giá sau khi '
                        'giảm là $250\\,000 - 50\\,000 = 200\\,000$ (đồng).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 40: Tìm tỉ số phần trăm của hai số và giá trị phần trăm '
                        'của một số: Số tiền được giảm là $250\\,000 \\times 20 : 100 = 50\\,000$ (đồng). '
                        'Giá sau khi giảm là $250\\,000 - 50\\,000 = 200\\,000$ (đồng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một chiếc cặp sách có giá niêm yết $250$ nghìn đồng, nhân dịp khai giảng được giảm giá '
                 '$20\\%$. Hỏi giá chiếc cặp sau khi giảm là bao nhiêu nghìn đồng?',
            'answer': ['200'],
            'unit': None,
            'solution': 'Số tiền giảm là $250 \\times 20 : 100 = 50$ (nghìn đồng). Giá sau khi giảm là $250 '
                        '- 50 = 200$ (nghìn đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd08-the-tich-don-vi-do-the-tich',
  'context_title': 'Chủ đề 8: Thể tích. Đơn vị đo thể tích',
  'context': 'Chủ đề 8 · SGK Toán 5: Biểu tượng thể tích và các đơn vị đo thể tích xăng-ti-mét khối, '
             'đề-xi-mét khối, mét khối.',
  'title': 'Bài 45: Thể tích của một hình',
  'icon': '🧊',
  'description': 'Nhận biết biểu tượng về thể tích của một hình và so sánh thể tích các hình bằng cách đếm '
                 'hình lập phương nhỏ.',
  'requirements': ['Hiểu được khái niệm thể tích là lượng không gian mà vật chiếm chỗ.',
                   'So sánh và tính được thể tích của các hình được ghép từ các hình lập phương nhỏ bằng '
                   'nhau.',
                   'Vận dụng kiến thức của **Bài 45: Thể tích của một hình** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': '- **Thể tích của một vật** là lượng không gian mà vật đó chiếm chỗ.\n'
                '- Nếu hình A nằm hoàn toàn trong hình B thì thể tích hình A bé hơn thể tích hình B; nếu một '
                'hình được tách thành hai phần thì thể tích của nó bằng tổng thể tích hai phần đó.',
  'theory': '### 1. So sánh thể tích hai hình\n'
            '- Hai hình được ghép bởi cùng một số lượng các hình lập phương nhỏ như nhau thì có **thể tích '
            'bằng nhau** (dù hình dạng khác nhau).\n'
            '### 2. Đếm số hình lập phương theo lớp\n'
            '- Nếu một hình hộp gồm $k$ lớp, mỗi lớp có $m$ hình lập phương nhỏ thì tổng số hình lập phương '
            'nhỏ là $m \\times k$.',
  'formulas': [{'category': 'Tính chất cộng thể tích',
                'items': [{'name': 'Hình ghép không chồng lấn', 'formula': '$V = V_1 + V_2$'},
                          {'name': 'Đếm theo lớp',
                           'formula': '$\\text{Tổng số hình lập phương nhỏ} = \\text{Số hình 1 lớp} \\times '
                                      '\\text{Số lớp}$'}]}],
  'example': 'Hình A gồm $3$ lớp, mỗi lớp có $8$ hình lập phương nhỏ cạnh $1\\text{ cm}$. Hình A gồm bao '
             'nhiêu hình lập phương nhỏ?',
  'example_answer': 'Tổng số hình lập phương nhỏ tạo nên hình A là $8 \\times 3 = 24$ (hình).',
  'real_life': 'Xếp các thùng hàng hình hộp vào kho hoặc xếp các viên rubik nhỏ vào hộp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu hình P được ghép bởi $12$ hình lập phương nhỏ và hình Q được ghép bởi $15$ hình lập '
                 'phương nhỏ như thế thì:',
            'options': ['Thể tích P lớn hơn Q',
                        'Thể tích P bằng Q',
                        'Thể tích P bé hơn Q',
                        'Không so sánh được'],
            'answer': 2,
            'solution': 'Vì $12 < 15$ nên thể tích hình P bé hơn thể tích hình Q.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình gồm $2$ lớp, mỗi lớp có $9$ hình lập phương nhỏ bằng nhau. Hình đó có tất cả bao '
                 'nhiêu hình lập phương nhỏ?',
            'options': ['$11$ hình', '$27$ hình', '$9$ hình', '$18$ hình'],
            'answer': 3,
            'solution': 'Số hình lập phương nhỏ là $9 \\times 2 = 18$ (hình).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 45: Thể tích của một hình**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Hình ghép không chồng lấn**?',
            'options': ['$V = V_1 + V_2$',
                        '$V = V_1 - V_2$',
                        'Đảo ngược vế của quy tắc: $V = V_1 + V_2$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $V = V_1 + V_2$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 45: Thể tích của một hình, **Hình ghép không chồng '
                        'lấn** được xác định bởi: $V = V_1 + V_2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 45: Thể tích của một hình**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Đếm theo lớp**?',
            'options': ['$\\text{Tổng số hình lập phương nhỏ} = \\text{Số hình 1 lớp} : \\text{Số lớp}$',
                        '$\\text{Tổng số hình lập phương nhỏ} = \\text{Số hình 1 lớp} \\times \\text{Số '
                        'lớp}$',
                        '$\\text{Tổng số hình lập phương nhỏ} = \\text{Số hình 2 lớp} \\times \\text{Số '
                        'lớp}$',
                        '$V = V_1 + V_2$'],
            'answer': 1,
            'solution': 'Trong Bài 45: Thể tích của một hình, **Đếm theo lớp** có công thức/quy tắc là: '
                        '$\\text{Tổng số hình lập phương nhỏ} = \\text{Số hình 1 lớp} \\times \\text{Số '
                        'lớp}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình lập phương lớn cạnh $2\\text{ cm}$ được ghép vừa khít từ các hình lập phương nhỏ '
                 'cạnh $1\\text{ cm}$. Cần bao nhiêu hình lập phương nhỏ?',
            'options': ['$4$ hình', '$6$ hình', '$8$ hình', '$12$ hình'],
            'answer': 2,
            'solution': 'Gồm $2$ lớp, mỗi lớp $2 \\times 2 = 4$ hình nên có $4 \\times 2 = 8$ (hình).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 45: Thể tích của một hình**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Hiểu được khái niệm thể tích là lượng không gian mà vật chiếm chỗ. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Hiểu được khái niệm thể tích là lượng không gian mà vật '
                        'chiếm chỗ.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu được khái niệm thể tích là '
                        'lượng không gian mà vật chiếm chỗ.',
                        'Hiểu được khái niệm thể tích là lượng không gian mà vật chiếm chỗ.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 45: Thể tích của một hình: Hiểu được khái niệm thể '
                        'tích là lượng không gian mà vật chiếm chỗ.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hai hình có hình dạng khác nhau nhưng được ghép từ cùng $10$ hình lập phương nhỏ bằng nhau '
                 'thì có thể tích bằng nhau.',
            'answer': True,
            'solution': 'Cùng số lượng hình lập phương đơn vị như nhau nên thể tích của hai hình bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 45: Thể tích của một hình**, quy tắc **Hình ghép không chồng lấn** được xác '
                 'định bởi $V = V_1 + V_2$ và khi áp dụng cho ví dụ “Hình A gồm $3$ lớp, mỗi lớp có $8$ hình '
                 'lập phương nhỏ cạnh $1\\text{ cm}$. Hình A gồm bao nhiêu hình lập phương nhỏ?” ta có lời '
                 'giải: Tổng số hình lập phương nhỏ tạo nên hình A là $8 \\times 3 = 24$ (hình).. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hình ghép không chồng lấn** ($V = V_1 + '
                        'V_2$) và lời giải ví dụ minh họa của Bài 45: Thể tích của một hình.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 45: Thể tích của một hình** để giải bài toán sau: '
                 'Hình A gồm $3$ lớp, mỗi lớp có $8$ hình lập phương nhỏ cạnh $1\\text{ cm}$. Hình A gồm bao '
                 'nhiêu hình lập phương nhỏ? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tổng số hình lập phương nhỏ tạo nên hình A là $8 \\times 3 = 24$ (hình).',
                        'Tổng số hình lập phương nhỏ tạo nên hình A là $8 : 3 = 24$ (hình).',
                        'Tổng số hình lập phương nhỏ tạo nên hình A là $8 \\times 3 = 23$ (hình).',
                        'Tổng số hình lập phương nhỏ tạo nên hình A là $16 \\times 3 = 24$ (hình).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 45: Thể tích của một hình: Tổng số hình lập phương nhỏ '
                        'tạo nên hình A là $8 \\times 3 = 24$ (hình).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khối hình hộp được xếp từ $4$ lớp, mỗi lớp có $3$ hàng, mỗi hàng có $5$ hình lập '
                 'phương nhỏ. Hỏi khối hình đó gồm tất cả bao nhiêu hình lập phương nhỏ?',
            'answer': ['60'],
            'unit': None,
            'solution': 'Mỗi lớp có $3 \\times 5 = 15$ hình. Cả khối có $15 \\times 4 = 60$ (hình lập phương '
                        'nhỏ).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd08-the-tich-don-vi-do-the-tich',
  'context_title': 'Chủ đề 8: Thể tích. Đơn vị đo thể tích',
  'context': 'Chủ đề 8 · SGK Toán 5: Biểu tượng thể tích và các đơn vị đo thể tích xăng-ti-mét khối, '
             'đề-xi-mét khối, mét khối.',
  'title': 'Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối',
  'icon': '🧊',
  'description': 'Nhận biết đơn vị xăng-ti-mét khối, đề-xi-mét khối và mối liên hệ với đơn vị đo dung tích '
                 'lít, mi-li-lít.',
  'requirements': ['Đọc, viết đúng các số đo thể tích với đơn vị $\\text{cm}^3$ và $\\text{dm}^3$.',
                   'Nắm vững quan hệ $1\\text{ dm}^3 = 1000\\text{ cm}^3 = 1\\text{ l}$ và thực hiện chuyển '
                   'đổi đơn vị.',
                   'Vận dụng kiến thức của **Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': '- **Xăng-ti-mét khối** ($\\text{cm}^3$) là thể tích của hình lập phương có cạnh dài '
                '$1\\text{ cm}$.\n'
                '- **Đề-xi-mét khối** ($\\text{dm}^3$) là thể tích của hình lập phương có cạnh dài $1\\text{ '
                'dm}$. Ta có $1\\text{ dm}^3 = 1000\\text{ cm}^3$ và $1\\text{ dm}^3 = 1\\text{ l}$.',
  'theory': '### 1. Quan hệ giữa $\\text{dm}^3$ và $\\text{cm}^3$\n'
            '- Hình lập phương cạnh $1\\text{ dm} = 10\\text{ cm}$ gồm $10 \\times 10 \\times 10 = 1000$ '
            'hình lập phương cạnh $1\\text{ cm}$, do đó $1\\text{ dm}^3 = 1000\\text{ cm}^3$ và $1\\text{ '
            'cm}^3 = 0{,}001\\text{ dm}^3$.\n'
            '### 2. Liên hệ với dung tích\n'
            '- $1\\text{ dm}^3 = 1\\text{ l}$ (lít); $1\\text{ cm}^3 = 1\\text{ ml}$ (mi-li-lít).',
  'formulas': [{'category': 'Quan hệ đơn vị',
                'items': [{'name': 'Đề-xi-mét khối và xăng-ti-mét khối',
                           'formula': '$1\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 = '
                                      '\\dfrac{1}{1000}\\text{ dm}^3 = 0{,}001\\text{ dm}^3$'},
                          {'name': 'Liên hệ với lít',
                           'formula': '$1\\text{ dm}^3 = 1\\text{ l}$; $1\\text{ cm}^3 = 1\\text{ ml}$'}]}],
  'example': 'Đổi các đơn vị sau: $5\\text{ dm}^3 = \\dots\\text{ cm}^3$ và $4500\\text{ cm}^3 = '
             '\\dots\\text{ dm}^3$.',
  'example_answer': 'Ta có $5\\text{ dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 = 4{,}5\\text{ dm}^3$.',
  'real_life': 'Đo dung tích hộp sữa ($1\\text{ l} = 1\\text{ dm}^3$), bình nước uống và xi-lanh y tế '
               '($\\text{cm}^3$ hay $\\text{ml}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một đề-xi-mét khối ($1\\text{ dm}^3$) bằng bao nhiêu xăng-ti-mét khối?',
            'options': ['$10\\text{ cm}^3$',
                        '$100\\text{ cm}^3$',
                        '$10\\,000\\text{ cm}^3$',
                        '$1000\\text{ cm}^3$'],
            'answer': 3,
            'solution': 'Ta có $1\\text{ dm}^3 = 1000\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một đề-xi-mét khối ($1\\text{ dm}^3$) bằng bao nhiêu lít?',
            'options': ['$1\\text{ l}$', '$1\\text{ ml}$', '$10\\text{ l}$', '$100\\text{ l}$'],
            'answer': 0,
            'solution': 'Theo quy ước dung tích, $1\\text{ dm}^3 = 1\\text{ l}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Đề-xi-mét khối và xăng-ti-mét khối**?',
            'options': ['$2\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 = \\dfrac{1}{1000}\\text{ '
                        'dm}^3 = 0{,}001\\text{ dm}^3$',
                        '$1\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 = \\dfrac{1}{1000}\\text{ '
                        'dm}^3 = 0{,}001\\text{ dm}^3$',
                        '$1\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 = \\dfrac{1000}{1}\\text{ '
                        'dm}^3 = 0{,}001\\text{ dm}^3$',
                        '$1\\text{ dm}^3 = 1\\text{ l}$; $1\\text{ cm}^3 = 1\\text{ ml}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối, **Đề-xi-mét '
                        'khối và xăng-ti-mét khối** được xác định bởi: $1\\text{ dm}^3 = 1000\\text{ cm}^3$; '
                        '$1\\text{ cm}^3 = \\dfrac{1}{1000}\\text{ dm}^3 = 0{,}001\\text{ dm}^3$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Liên hệ với lít**?',
            'options': ['$2\\text{ dm}^3 = 1\\text{ l}$; $1\\text{ cm}^3 = 1\\text{ ml}$',
                        '$1\\text{ dm}^3 = 1\\text{ l}$; $1\\text{ cm}^3 = 2\\text{ ml}$',
                        '$1\\text{ dm}^3 = 1\\text{ l}$; $1\\text{ cm}^3 = 1\\text{ ml}$',
                        '$1\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 = \\dfrac{1}{1000}\\text{ '
                        'dm}^3 = 0{,}001\\text{ dm}^3$'],
            'answer': 2,
            'solution': 'Trong Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối, **Liên hệ với lít** có công '
                        'thức/quy tắc là: $1\\text{ dm}^3 = 1\\text{ l}$; $1\\text{ cm}^3 = 1\\text{ ml}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đo $3\\text{ dm}^3\\ 25\\text{ cm}^3$ viết dưới dạng số thập phân có đơn vị đề-xi-mét '
                 'khối là:',
            'options': ['$3{,}25\\text{ dm}^3$',
                        '$32{,}5\\text{ dm}^3$',
                        '$3{,}0025\\text{ dm}^3$',
                        '$3{,}025\\text{ dm}^3$'],
            'answer': 3,
            'solution': 'Vì $25\\text{ cm}^3 = 0{,}025\\text{ dm}^3$ nên $3\\text{ dm}^3\\ 25\\text{ cm}^3 = '
                        '3{,}025\\text{ dm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Đọc, viết đúng các số đo thể tích với đơn vị $\\text{cm}^3$ và $\\text{dm}^3$.',
                        'Đọc, viết đúng các số đo thể tích với đơn vị $\\text{cm}^4$ và $\\text{dm}^3$.',
                        'Đọc, viết đúng các số đo thể tích với đơn vị $\\text{cm}^3$ và $\\text{dm}^2$.',
                        'Đọc, viết đúng các số đo thể tích với đơn vị $\\text{cm}^6$ và $\\text{dm}^3$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối: Đọc, viết đúng '
                        'các số đo thể tích với đơn vị $\\text{cm}^3$ và $\\text{dm}^3$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $0{,}5\\text{ dm}^3 = 500\\text{ cm}^3$.',
            'answer': True,
            'solution': 'Ta lấy $0{,}5 \\times 1000 = 500\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối**, quy tắc **Đề-xi-mét khối và '
                 'xăng-ti-mét khối** được xác định bởi $1\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 '
                 '= \\dfrac{1}{1000}\\text{ dm}^3 = 0{,}001\\text{ dm}^3$ và khi áp dụng cho ví dụ “Đổi các '
                 'đơn vị sau: $5\\text{ dm}^3 = \\dots\\text{ cm}^3$ và $4500\\text{ cm}^3 = \\dots\\text{ '
                 'dm}^3$.” ta có lời giải: Ta có $5\\text{ dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 '
                 '= 4{,}5\\text{ dm}^3$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đề-xi-mét khối và xăng-ti-mét khối** '
                        '($1\\text{ dm}^3 = 1000\\text{ cm}^3$; $1\\text{ cm}^3 = \\dfrac{1}{1000}\\text{ '
                        'dm}^3 = 0{,}001\\text{ dm}^3$) và lời giải ví dụ minh họa của Bài 46: Xăng-ti-mét '
                        'khối. Đề-xi-mét khối.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối** để giải bài '
                 'toán sau: Đổi các đơn vị sau: $5\\text{ dm}^3 = \\dots\\text{ cm}^3$ và $4500\\text{ cm}^3 '
                 '= \\dots\\text{ dm}^3$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $6\\text{ dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 = 4{,}5\\text{ '
                        'dm}^3$.',
                        'Ta có $5\\text{ dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 = 4{,}5\\text{ '
                        'dm}^3$.',
                        'Ta có $5\\text{ dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 = 4{,}5\\text{ '
                        'dm}^2$.',
                        'Ta có $10\\text{ dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 = 4{,}5\\text{ '
                        'dm}^3$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 46: Xăng-ti-mét khối. Đề-xi-mét khối: Ta có $5\\text{ '
                        'dm}^3 = 5000\\text{ cm}^3$ và $4500\\text{ cm}^3 = 4{,}5\\text{ dm}^3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bình nước chứa được $3{,}5\\text{ dm}^3$ nước. Người ta rót từ bình đầy nước đó ra một '
                 'ca $800\\text{ cm}^3$. Hỏi trong bình còn lại bao nhiêu đề-xi-mét khối nước?',
            'answer': ['2,7', '2.7'],
            'unit': None,
            'solution': 'Đổi $800\\text{ cm}^3 = 0{,}8\\text{ dm}^3$. Lượng nước còn lại là $3{,}5 - 0{,}8 = '
                        '2{,}7\\text{ dm}^3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd08-the-tich-don-vi-do-the-tich',
  'context_title': 'Chủ đề 8: Thể tích. Đơn vị đo thể tích',
  'context': 'Chủ đề 8 · SGK Toán 5: Biểu tượng thể tích và các đơn vị đo thể tích xăng-ti-mét khối, '
             'đề-xi-mét khối, mét khối.',
  'title': 'Bài 47: Mét khối',
  'icon': '🧊',
  'description': 'Nhận biết đơn vị mét khối và mối quan hệ giữa mét khối, đề-xi-mét khối, xăng-ti-mét khối.',
  'requirements': ['Nhận biết được mét khối ($\\text{m}^3$) là thể tích hình lập phương cạnh $1\\text{ m}$.',
                   'Chuyển đổi thành thạo giữa $\\text{m}^3$, $\\text{dm}^3$ (lít) và $\\text{cm}^3$.',
                   'Vận dụng kiến thức của **Bài 47: Mét khối** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': '- **Mét khối** ($\\text{m}^3$) là thể tích của hình lập phương có cạnh dài $1\\text{ m}$.\n'
                '- Hai đơn vị đo thể tích liền kề nhau hơn kém nhau **$1000$ lần**: $1\\text{ m}^3 = '
                '1000\\text{ dm}^3 = 1\\,000\\,000\\text{ cm}^3$.',
  'theory': '### 1. Quan hệ giữa $\\text{m}^3$, $\\text{dm}^3$ và $\\text{cm}^3$\n'
            '- Mỗi đơn vị đo thể tích liền kề ứng với **ba chữ số** khi đổi sang số thập phân: $2\\text{ '
            'm}^3\\ 15\\text{ dm}^3 = 2{,}015\\text{ m}^3$.\n'
            '### 2. Liên hệ giữa mét khối và lít\n'
            '- Vì $1\\text{ dm}^3 = 1\\text{ l}$ nên $1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$.',
  'formulas': [{'category': 'Bảng quan hệ đơn vị thể tích',
                'items': [{'name': 'Mét khối sang đề-xi-mét khối',
                           'formula': '$1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$'},
                          {'name': 'Mét khối sang xăng-ti-mét khối',
                           'formula': '$1\\text{ m}^3 = 1\\,000\\,000\\text{ cm}^3$'},
                          {'name': 'Đổi ngược lại', 'formula': '$1\\text{ dm}^3 = 0{,}001\\text{ m}^3$'}]}],
  'example': 'Đổi các số đo sau: $3{,}2\\text{ m}^3 = \\dots\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ '
             'dm}^3 = \\dots\\text{ m}^3$.',
  'example_answer': 'Ta có $3{,}2\\text{ m}^3 = 3200\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                    '2{,}015\\text{ m}^3$.',
  'real_life': 'Đọc chỉ số đồng hồ nước sinh hoạt hàng tháng của gia đình (tính bằng $\\text{m}^3$) và tính '
               'thể tích bể bơi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một mét khối ($1\\text{ m}^3$) bằng bao nhiêu đề-xi-mét khối?',
            'options': ['$1000\\text{ dm}^3$',
                        '$100\\text{ dm}^3$',
                        '$10\\text{ dm}^3$',
                        '$1\\,000\\,000\\text{ dm}^3$'],
            'answer': 0,
            'solution': 'Hai đơn vị thể tích liền kề hơn kém nhau $1000$ lần nên $1\\text{ m}^3 = '
                        '1000\\text{ dm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một bể chứa $3\\text{ m}^3$ nước tức là chứa được bao nhiêu lít nước?',
            'options': ['$300\\text{ l}$', '$3000\\text{ l}$', '$30\\,000\\text{ l}$', '$30\\text{ l}$'],
            'answer': 1,
            'solution': 'Vì $1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$ nên $3\\text{ m}^3 = '
                        '3000\\text{ l}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 47: Mét khối**, quy tắc hoặc công thức nào sau đây xác định đúng **Mét khối '
                 'sang đề-xi-mét khối**?',
            'options': ['$2\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$',
                        '$1\\text{ m}^3 = 1000\\text{ dm}^3 = 999\\text{ l}$',
                        '$1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$',
                        '$1\\text{ m}^3 = 1\\,000\\,000\\text{ cm}^3$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 47: Mét khối, **Mét khối sang đề-xi-mét khối** '
                        'được xác định bởi: $1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 47: Mét khối**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Mét '
                 'khối sang xăng-ti-mét khối**?',
            'options': ['$2\\text{ m}^3 = 1\\,000\\,000\\text{ cm}^3$',
                        '$1\\text{ m}^3 = 1\\,000\\,000\\text{ cm}^2$',
                        '$1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$',
                        '$1\\text{ m}^3 = 1\\,000\\,000\\text{ cm}^3$'],
            'answer': 3,
            'solution': 'Trong Bài 47: Mét khối, **Mét khối sang xăng-ti-mét khối** có công thức/quy tắc là: '
                        '$1\\text{ m}^3 = 1\\,000\\,000\\text{ cm}^3$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đo $2\\text{ m}^3\\ 15\\text{ dm}^3$ viết dưới dạng số thập phân có đơn vị mét khối là:',
            'options': ['$2{,}015\\text{ m}^3$',
                        '$2{,}15\\text{ m}^3$',
                        '$2{,}0015\\text{ m}^3$',
                        '$215\\text{ m}^3$'],
            'answer': 0,
            'solution': 'Vì $15\\text{ dm}^3 = \\dfrac{15}{1000}\\text{ m}^3 = 0{,}015\\text{ m}^3$ nên bằng '
                        '$2{,}015\\text{ m}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 47: Mét khối**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được mét khối ($\\text{m}^4$) là thể tích hình lập phương cạnh $1\\text{ '
                        'm}$.',
                        'Nhận biết được mét khối ($\\text{m}^3$) là thể tích hình lập phương cạnh $1\\text{ '
                        'm}$.',
                        'Nhận biết được mét khối ($\\text{m}^3$) là thể tích hình lập phương cạnh $2\\text{ '
                        'm}$.',
                        'Nhận biết được mét khối ($\\text{m}^6$) là thể tích hình lập phương cạnh $1\\text{ '
                        'm}$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 47: Mét khối: Nhận biết được mét khối ($\\text{m}^3$) '
                        'là thể tích hình lập phương cạnh $1\\text{ m}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $1\\text{ m}^3 = 100\\text{ dm}^3$.',
            'answer': False,
            'solution': 'Ta có $1\\text{ m}^3 = 1000\\text{ dm}^3$ chứ không phải $100\\text{ dm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 47: Mét khối**, quy tắc **Mét khối sang đề-xi-mét khối** được xác định bởi '
                 '$1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$ và khi áp dụng cho ví dụ “Đổi các số '
                 'đo sau: $3{,}2\\text{ m}^3 = \\dots\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                 '\\dots\\text{ m}^3$.” ta có lời giải: Ta có $3{,}2\\text{ m}^3 = 3200\\text{ dm}^3$ và '
                 '$2\\text{ m}^3\\ 15\\text{ dm}^3 = 2{,}015\\text{ m}^3$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Mét khối sang đề-xi-mét khối** '
                        '($1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$) và lời giải ví dụ minh họa '
                        'của Bài 47: Mét khối.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 47: Mét khối** để giải bài toán sau: Đổi các số đo '
                 'sau: $3{,}2\\text{ m}^3 = \\dots\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                 '\\dots\\text{ m}^3$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $4{,}2\\text{ m}^3 = 3200\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                        '2{,}015\\text{ m}^3$.',
                        'Ta có $3{,}2\\text{ m}^3 = 3200\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                        '2{,}015\\text{ m}^2$.',
                        'Ta có $3{,}2\\text{ m}^3 = 3200\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                        '2{,}015\\text{ m}^3$.',
                        'Ta có $6{,}2\\text{ m}^3 = 3200\\text{ dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = '
                        '2{,}015\\text{ m}^3$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 47: Mét khối: Ta có $3{,}2\\text{ m}^3 = 3200\\text{ '
                        'dm}^3$ và $2\\text{ m}^3\\ 15\\text{ dm}^3 = 2{,}015\\text{ m}^3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Gia đình bạn An trong tháng này dùng hết $18\\text{ m}^3$ nước sạch. Hỏi gia đình An đã '
                 'dùng hết bao nhiêu lít nước?',
            'answer': ['18000'],
            'unit': None,
            'solution': 'Vì $1\\text{ m}^3 = 1000\\text{ l}$ nên $18\\text{ m}^3 = 18\\,000\\text{ l}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd09-dien-tich-the-tich-hinh-khoi',
  'context_title': 'Chủ đề 9: Diện tích và thể tích của một số hình khối',
  'context': 'Chủ đề 9 · SGK Toán 5: Hình khai triển, diện tích xung quanh, diện tích toàn phần và thể tích '
             'hình khối.',
  'title': 'Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ',
  'icon': '📦',
  'description': 'Nhận biết các mặt, đỉnh, cạnh và hình khai triển phẳng của hình hộp chữ nhật, hình lập '
                 'phương, hình trụ.',
  'requirements': ['Nêu được số mặt, số cạnh, số đỉnh của hình hộp chữ nhật và hình lập phương.',
                   'Nhận biết được hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ.',
                   'Vận dụng kiến thức của **Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật '
                   'và hình trụ** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Hình hộp chữ nhật** có $6$ mặt đều là hình chữ nhật (các mặt đối diện bằng nhau), $8$ '
                'đỉnh và $12$ cạnh (ba kích thước: chiều dài $a$, chiều rộng $b$, chiều cao $c$).\n'
                '- **Hình lập phương** có $6$ mặt là $6$ hình vuông bằng nhau. **Hình trụ** khi khai triển '
                'gồm $2$ mặt đáy là hai hình tròn bằng nhau và mặt xung quanh trải phẳng là một hình chữ '
                'nhật.',
  'theory': '### 1. Hình khai triển của hình lập phương và hình hộp chữ nhật\n'
            '- Hình khai triển của hình lập phương gồm $6$ hình vuông bằng nhau nối liền sao cho khi gấp lại '
            'tạo thành hình lập phương.\n'
            '- Hình khai triển của hình hộp chữ nhật gồm $3$ cặp hình chữ nhật từng đôi một bằng nhau ($4$ '
            'mặt bên và $2$ mặt đáy).\n'
            '### 2. Hình khai triển của hình trụ\n'
            '- Gồm $1$ hình chữ nhật (mặt xung quanh) và $2$ hình tròn bằng nhau (hai đáy).',
  'formulas': [{'category': 'Cấu tạo hình khối',
                'items': [{'name': 'Hình hộp chữ nhật và lập phương',
                           'formula': 'Có $6$ mặt, $8$ đỉnh, $12$ cạnh'},
                          {'name': 'Hình trụ khai triển',
                           'formula': 'Gồm $1$ hình chữ nhật và $2$ hình tròn đáy bằng nhau'}]}],
  'example': 'Một khung dây thép hình lập phương có cạnh $10\\text{ cm}$. Cần bao nhiêu xăng-ti-mét dây thép '
             'để uốn khung đó?',
  'example_answer': 'Hình lập phương có $12$ cạnh bằng nhau nên độ dài dây thép cần dùng là $12 \\times 10 = '
                    '120\\text{ cm}$.',
  'real_life': 'Thiết kế mẫu giấy bìa cứng để gấp thành vỏ hộp quà, hộp bánh hoặc lon sữa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình lập phương có tất cả bao nhiêu mặt?',
            'options': ['$4$ mặt', '$6$ mặt', '$8$ mặt', '$12$ mặt'],
            'answer': 1,
            'solution': 'Hình lập phương có $6$ mặt là các hình vuông bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình khai triển của một hình trụ gồm những hình phẳng nào?',
            'options': ['$2$ hình vuông và $1$ hình tròn',
                        '$6$ hình chữ nhật',
                        '$1$ hình chữ nhật và $2$ hình tròn bằng nhau',
                        '$2$ hình tam giác và $1$ hình chữ nhật'],
            'answer': 2,
            'solution': 'Khai triển hình trụ gồm $1$ hình chữ nhật (mặt xung quanh) và $2$ hình tròn bằng '
                        'nhau (hai đáy).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ**, quy '
                 'tắc hoặc công thức nào sau đây xác định đúng **Hình hộp chữ nhật và lập phương**?',
            'options': ['Có $7$ mặt, $8$ đỉnh, $12$ cạnh',
                        'Có $6$ mặt, $8$ đỉnh, $11$ cạnh',
                        'Có $12$ mặt, $8$ đỉnh, $12$ cạnh',
                        'Có $6$ mặt, $8$ đỉnh, $12$ cạnh'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 49: Hình khai triển của hình lập phương, hình hộp '
                        'chữ nhật và hình trụ, **Hình hộp chữ nhật và lập phương** được xác định bởi: Có $6$ '
                        'mặt, $8$ đỉnh, $12$ cạnh.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Hình trụ khai triển**?',
            'options': ['Gồm $1$ hình chữ nhật và $2$ hình tròn đáy bằng nhau',
                        'Gồm $2$ hình chữ nhật và $2$ hình tròn đáy bằng nhau',
                        'Gồm $1$ hình chữ nhật và $1$ hình tròn đáy bằng nhau',
                        'Có $6$ mặt, $8$ đỉnh, $12$ cạnh'],
            'answer': 0,
            'solution': 'Trong Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ, '
                        '**Hình trụ khai triển** có công thức/quy tắc là: Gồm $1$ hình chữ nhật và $2$ hình '
                        'tròn đáy bằng nhau.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng độ dài tất cả các cạnh của một hình lập phương có cạnh $5\\text{ cm}$ là:',
            'options': ['$20\\text{ cm}$', '$60\\text{ cm}$', '$30\\text{ cm}$', '$150\\text{ cm}$'],
            'answer': 1,
            'solution': 'Hình lập phương có $12$ cạnh bằng nhau nên tổng độ dài các cạnh là $12 \\times 5 = '
                        '60\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật '
                 'và hình trụ**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nêu được số mặt, số cạnh, số đỉnh của hình hộp chữ nhật và hình lập phương. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nêu được số mặt, số cạnh, số đỉnh của hình hộp chữ nhật '
                        'và hình lập phương.',
                        'Nêu được số mặt, số cạnh, số đỉnh của hình hộp chữ nhật và hình lập phương.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nêu được số mặt, số cạnh, số '
                        'đỉnh của hình hộp chữ nhật và hình lập phương.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 49: Hình khai triển của hình lập phương, hình hộp chữ '
                        'nhật và hình trụ: Nêu được số mặt, số cạnh, số đỉnh của hình hộp chữ nhật và hình '
                        'lập phương.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong hình hộp chữ nhật, hai mặt đối diện luôn bằng nhau.',
            'answer': True,
            'solution': 'Hình hộp chữ nhật có $3$ cặp mặt đối diện là các hình chữ nhật bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 49: Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ**, quy '
                 'tắc **Hình hộp chữ nhật và lập phương** được xác định bởi Có $6$ mặt, $8$ đỉnh, $12$ cạnh '
                 'và khi áp dụng cho ví dụ “Một khung dây thép hình lập phương có cạnh $10\\text{ cm}$. Cần '
                 'bao nhiêu xăng-ti-mét dây thép để uốn khung đó?” ta có lời giải: Hình lập phương có $12$ '
                 'cạnh bằng nhau nên độ dài dây thép cần dùng là $12 \\times 10 = 120\\text{ cm}$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hình hộp chữ nhật và lập phương** (Có '
                        '$6$ mặt, $8$ đỉnh, $12$ cạnh) và lời giải ví dụ minh họa của Bài 49: Hình khai '
                        'triển của hình lập phương, hình hộp chữ nhật và hình trụ.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 49: Hình khai triển của hình lập phương, hình hộp '
                 'chữ nhật và hình trụ** để giải bài toán sau: Một khung dây thép hình lập phương có cạnh '
                 '$10\\text{ cm}$. Cần bao nhiêu xăng-ti-mét dây thép để uốn khung đó? Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Hình lập phương có $12$ cạnh bằng nhau nên độ dài dây thép cần dùng là $12 : 10 = '
                        '120\\text{ cm}$.',
                        'Hình lập phương có $12$ cạnh bằng nhau nên độ dài dây thép cần dùng là $12 \\times '
                        '10 = 119\\text{ cm}$.',
                        'Hình lập phương có $24$ cạnh bằng nhau nên độ dài dây thép cần dùng là $12 \\times '
                        '10 = 120\\text{ cm}$.',
                        'Hình lập phương có $12$ cạnh bằng nhau nên độ dài dây thép cần dùng là $12 \\times '
                        '10 = 120\\text{ cm}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 49: Hình khai triển của hình lập phương, hình hộp chữ '
                        'nhật và hình trụ: Hình lập phương có $12$ cạnh bằng nhau nên độ dài dây thép cần '
                        'dùng là $12 \\times 10 = 120\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Người ta dùng dây thép để uốn một khung đèn lồng hình hộp chữ nhật có chiều dài $25\\text{ '
                 'cm}$, chiều rộng $15\\text{ cm}$ và chiều cao $20\\text{ cm}$. Tính tổng độ dài dây thép '
                 'cần dùng (không tính mối nối, đơn vị cm).',
            'answer': ['240'],
            'unit': None,
            'solution': 'Hình hộp chữ nhật có $4$ chiều dài, $4$ chiều rộng, $4$ chiều cao. Độ dài dây là '
                        '$(25 + 15 + 20) \\times 4 = 240\\text{ cm}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd09-dien-tich-the-tich-hinh-khoi',
  'context_title': 'Chủ đề 9: Diện tích và thể tích của một số hình khối',
  'context': 'Chủ đề 9 · SGK Toán 5: Hình khai triển, diện tích xung quanh, diện tích toàn phần và thể tích '
             'hình khối.',
  'title': 'Bài 50: Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật',
  'icon': '📦',
  'description': 'Công thức tính diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật.',
  'requirements': ['Tính được diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật.',
                   'Vận dụng giải bài toán thực tế như sơn phòng học hoặc làm thùng tôn không có nắp.',
                   'Vận dụng kiến thức của **Bài 50: Diện tích xung quanh và diện tích toàn phần của hình '
                   'hộp chữ nhật** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Diện tích xung quanh** ($S_{\\text{xq}}$) của hình hộp chữ nhật là tổng diện tích bốn '
                'mặt bên: lấy **chu vi mặt đáy nhân với chiều cao** (cùng đơn vị đo).\n'
                '- **Diện tích toàn phần** ($S_{\\text{tp}}$) của hình hộp chữ nhật là tổng của diện tích '
                'xung quanh và diện tích hai mặt đáy.',
  'theory': '### 1. Công thức tính\n'
            '- Gọi $a, b, c$ lần lượt là chiều dài, chiều rộng, chiều cao (cùng đơn vị đo): $S_{\\text{xq}} '
            '= (a + b) \\times 2 \\times c$ và $S_{\\text{tp}} = S_{\\text{xq}} + 2 \\times a \\times b$.\n'
            '### 2. Chú ý trong bài toán thực tế\n'
            '- Hộp **không có nắp** hoặc sơn phòng (chỉ sơn $4$ bức tường và trần nhà): diện tích cần tính '
            'bằng $S_{\\text{xq}} + a \\times b$ (chỉ cộng $1$ mặt đáy).',
  'formulas': [{'category': 'Hình hộp chữ nhật (dài a, rộng b, cao c)',
                'items': [{'name': 'Diện tích xung quanh',
                           'formula': '$S_{\\text{xq}} = (a + b) \\times 2 \\times c$'},
                          {'name': 'Diện tích toàn phần',
                           'formula': '$S_{\\text{tp}} = S_{\\text{xq}} + 2 \\times a \\times b$'},
                          {'name': 'Hộp không nắp (1 đáy)',
                           'formula': '$S = S_{\\text{xq}} + a \\times b$'}]}],
  'example': 'Tính diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật có chiều dài $5\\text{ '
             'cm}$, chiều rộng $4\\text{ cm}$, chiều cao $3\\text{ cm}$.',
  'example_answer': 'Ta có $S_{\\text{xq}} = (5 + 4) \\times 2 \\times 3 = 54\\text{ cm}^2$. Diện tích hai '
                    'đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy $S_{\\text{tp}} = 54 + 40 = '
                    '94\\text{ cm}^2$.',
  'real_life': 'Tính diện tích tường cần quét sơn trong phòng hoặc diện tích bìa carton cần làm thùng đựng '
               'hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích xung quanh của hình hộp chữ nhật có chiều dài $a$, chiều rộng '
                 '$b$, chiều cao $c$ là:',
            'options': ['$S_{\\text{xq}} = a \\times b \\times c$',
                        '$S_{\\text{xq}} = (a + b) \\times c$',
                        '$S_{\\text{xq}} = (a + b) \\times 2 \\times c$',
                        '$S_{\\text{xq}} = a \\times b \\times 2$'],
            'answer': 2,
            'solution': 'Diện tích xung quanh bằng chu vi đáy nhân với chiều cao: $S_{\\text{xq}} = (a + b) '
                        '\\times 2 \\times c$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình hộp chữ nhật có chiều dài $6\\text{ dm}$, chiều rộng $4\\text{ dm}$, chiều cao '
                 '$5\\text{ dm}$ có diện tích xung quanh là:',
            'options': ['$120\\text{ dm}^2$',
                        '$148\\text{ dm}^2$',
                        '$24\\text{ dm}^2$',
                        '$100\\text{ dm}^2$'],
            'answer': 3,
            'solution': 'Ta có $S_{\\text{xq}} = (6 + 4) \\times 2 \\times 5 = 100\\text{ dm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 50: Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật**, quy '
                 'tắc hoặc công thức nào sau đây xác định đúng **Diện tích xung quanh**?',
            'options': ['$S_{\\text{xq}} = (a + b) \\times 2 \\times c$',
                        '$S_{\\text{xq}} = (a - b) \\times 2 \\times c$',
                        '$S_{\\text{xq}} = (a + b) \\times 1 \\times c$',
                        '$S_{\\text{xq}} = (a + b) \\times 4 \\times c$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 50: Diện tích xung quanh và diện tích toàn phần '
                        'của hình hộp chữ nhật, **Diện tích xung quanh** được xác định bởi: $S_{\\text{xq}} '
                        '= (a + b) \\times 2 \\times c$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 50: Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Diện tích toàn phần**?',
            'options': ['$S_{\\text{tp}} = S_{\\text{xq}} - 2 \\times a \\times b$',
                        '$S_{\\text{tp}} = S_{\\text{xq}} + 2 \\times a \\times b$',
                        '$S_{\\text{tp}} = S_{\\text{xq}} + 1 \\times a \\times b$',
                        '$S_{\\text{tp}} = S_{\\text{xq}} + 4 \\times a \\times b$'],
            'answer': 1,
            'solution': 'Trong Bài 50: Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật, '
                        '**Diện tích toàn phần** có công thức/quy tắc là: $S_{\\text{tp}} = S_{\\text{xq}} + '
                        '2 \\times a \\times b$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Diện tích toàn phần của hình hộp chữ nhật có chiều dài $6\\text{ dm}$, chiều rộng '
                 '$4\\text{ dm}$, chiều cao $5\\text{ dm}$ là:',
            'options': ['$100\\text{ dm}^2$',
                        '$124\\text{ dm}^2$',
                        '$148\\text{ dm}^2$',
                        '$120\\text{ dm}^2$'],
            'answer': 2,
            'solution': 'Ta có $S_{\\text{xq}} = 100\\text{ dm}^2$, diện tích hai đáy là $2 \\times 6 '
                        '\\times 4 = 48\\text{ dm}^2$, suy ra $S_{\\text{tp}} = 148\\text{ dm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 50: Diện tích xung quanh và diện tích toàn phần của hình '
                 'hộp chữ nhật**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tính được diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính được diện tích xung quanh và diện tích toàn phần của '
                        'hình hộp chữ nhật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được diện tích xung quanh '
                        'và diện tích toàn phần của hình hộp chữ nhật.',
                        'Tính được diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 50: Diện tích xung quanh và diện tích toàn phần của '
                        'hình hộp chữ nhật: Tính được diện tích xung quanh và diện tích toàn phần của hình '
                        'hộp chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Một bể kính nuôi cá không có nắp gồm $4$ mặt bên và $1$ mặt đáy.',
            'answer': True,
            'solution': 'Bể cá không có nắp nên chỉ có $4$ mặt xung quanh và $1$ mặt đáy dưới.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 50: Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật**, quy '
                 'tắc **Diện tích xung quanh** được xác định bởi $S_{\\text{xq}} = (a + b) \\times 2 \\times '
                 'c$ và khi áp dụng cho ví dụ “Tính diện tích xung quanh và diện tích toàn phần của hình hộp '
                 'chữ nhật có chiều dài $5\\text{ cm}$, chiều rộng $4\\text{ cm}$, chiều cao...” ta có lời '
                 'giải: Ta có $S_{\\text{xq}} = (5 + 4) \\times 2 \\times 3 = 54\\text{ cm}^2$. Diện tích '
                 'hai đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy $S_{\\text{tp}} = 54 + 40 = '
                 '94\\text{ cm}^2$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Diện tích xung quanh** ($S_{\\text{xq}} '
                        '= (a + b) \\times 2 \\times c$) và lời giải ví dụ minh họa của Bài 50: Diện tích '
                        'xung quanh và diện tích toàn phần của hình hộp chữ nhật.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 50: Diện tích xung quanh và diện tích toàn phần của '
                 'hình hộp chữ nhật** để giải bài toán sau: Tính diện tích xung quanh và diện tích toàn phần '
                 'của hình hộp chữ nhật có chiều dài $5\\text{ cm}$, chiều rộng $4\\text{ cm}$, chiều cao '
                 '$3\\text{ cm}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $S_{\\text{xq}} = (5 + 4) \\times 2 \\times 3 = 54\\text{ cm}^2$. Diện tích '
                        'hai đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy $S_{\\text{tp}} = 54 + 40 '
                        '= 94\\text{ cm}^2$...',
                        'Ta có $S_{\\text{xq}} = (5 - 4) \\times 2 \\times 3 = 54\\text{ cm}^2$. Diện tích '
                        'hai đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy $S_{\\text{tp}} = 54 + 40 '
                        '= 94\\text{ cm}^2$...',
                        'Ta có $S_{\\text{xq}} = (5 + 4) \\times 2 \\times 3 = 54\\text{ cm}^2$. Diện tích '
                        'hai đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy $S_{\\text{tp}} = 54 + 40 '
                        '= 94\\text{ cm}^1$...',
                        'Ta có $S_{\\text{xq}} = (10 + 4) \\times 2 \\times 3 = 54\\text{ cm}^2$. Diện tích '
                        'hai đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy $S_{\\text{tp}} = 54 + 40 '
                        '= 94\\text{ cm}^2$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 50: Diện tích xung quanh và diện tích toàn phần của hình '
                        'hộp chữ nhật: Ta có $S_{\\text{xq}} = (5 + 4) \\times 2 \\times 3 = 54\\text{ '
                        'cm}^2$. Diện tích hai đáy là $2 \\times 5 \\times 4 = 40\\text{ cm}^2$. Vậy '
                        '$S_{\\text{tp}} = 54 + 40 = 94\\text{ cm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cái thùng tôn không nắp dạng hình hộp chữ nhật có chiều dài $8\\text{ dm}$, chiều rộng '
                 '$5\\text{ dm}$ và chiều cao $4\\text{ dm}$. Tính diện tích tôn dùng để làm thùng (không '
                 'tính mép hàn, đơn vị dm²).',
            'answer': ['144'],
            'unit': None,
            'solution': 'Ta có $S_{\\text{xq}} = (8 + 5) \\times 2 \\times 4 = 104\\text{ dm}^2$, diện tích '
                        '$1$ đáy là $8 \\times 5 = 40\\text{ dm}^2$. Tổng diện tích tôn là $104 + 40 = '
                        '144\\text{ dm}^2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd09-dien-tich-the-tich-hinh-khoi',
  'context_title': 'Chủ đề 9: Diện tích và thể tích của một số hình khối',
  'context': 'Chủ đề 9 · SGK Toán 5: Hình khai triển, diện tích xung quanh, diện tích toàn phần và thể tích '
             'hình khối.',
  'title': 'Bài 51: Diện tích xung quanh và diện tích toàn phần của hình lập phương',
  'icon': '📦',
  'description': 'Công thức tính diện tích xung quanh và diện tích toàn phần của hình lập phương.',
  'requirements': ['Hiểu và vận dụng được công thức tính diện tích xung quanh, diện tích toàn phần của hình '
                   'lập phương.',
                   'Tìm được diện tích một mặt và độ dài cạnh khi biết diện tích xung quanh hoặc diện tích '
                   'toàn phần.',
                   'Vận dụng kiến thức của **Bài 51: Diện tích xung quanh và diện tích toàn phần của hình '
                   'lập phương** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Vì $6$ mặt của hình lập phương là $6$ hình vuông bằng nhau có cạnh $a$ nên diện tích một '
                'mặt là $S_{\\text{1 mặt}} = a \\times a$.\n'
                '- **Diện tích xung quanh**: $S_{\\text{xq}} = (a \\times a) \\times 4$. **Diện tích toàn '
                'phần**: $S_{\\text{tp}} = (a \\times a) \\times 6$.',
  'theory': '### 1. Tính diện tích xung quanh và diện tích toàn phần\n'
            '- Với cạnh $a = 4\\text{ cm}$: diện tích một mặt là $4 \\times 4 = 16\\text{ cm}^2$; '
            '$S_{\\text{xq}} = 16 \\times 4 = 64\\text{ cm}^2$; $S_{\\text{tp}} = 16 \\times 6 = 96\\text{ '
            'cm}^2$.\n'
            '### 2. Quan hệ giữa $S_{\\text{xq}}$ và $S_{\\text{tp}}$\n'
            '- Biết $S_{\\text{xq}}$, ta tìm được diện tích $1$ mặt là $S_{\\text{xq}} : 4$, từ đó '
            '$S_{\\text{tp}} = (S_{\\text{xq}} : 4) \\times 6$.',
  'formulas': [{'category': 'Hình lập phương cạnh a',
                'items': [{'name': 'Diện tích một mặt', 'formula': '$S_1 = a \\times a$'},
                          {'name': 'Diện tích xung quanh',
                           'formula': '$S_{\\text{xq}} = a \\times a \\times 4$'},
                          {'name': 'Diện tích toàn phần',
                           'formula': '$S_{\\text{tp}} = a \\times a \\times 6$'}]}],
  'example': 'Một hình lập phương có diện tích xung quanh là $36\\text{ cm}^2$. Tính diện tích toàn phần và '
             'độ dài cạnh của hình lập phương đó.',
  'example_answer': 'Diện tích một mặt là $36 : 4 = 9\\text{ cm}^2$. Vì $9 = 3 \\times 3$ nên cạnh $a = '
                    '3\\text{ cm}$. Diện tích toàn phần là $9 \\times 6 = 54\\text{ cm}^2$.',
  'real_life': 'Tính diện tích giấy màu cần để dán kín các mặt của hộp quà hình lập phương.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích toàn phần của hình lập phương có cạnh $a$ là:',
            'options': ['$a \\times a \\times 4$',
                        '$a \\times a \\times a$',
                        '$a \\times 6$',
                        '$a \\times a \\times 6$'],
            'answer': 3,
            'solution': 'Hình lập phương có $6$ mặt vuông bằng nhau nên $S_{\\text{tp}} = a \\times a '
                        '\\times 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình lập phương có cạnh $5\\text{ cm}$ thì có diện tích xung quanh là:',
            'options': ['$100\\text{ cm}^2$',
                        '$25\\text{ cm}^2$',
                        '$150\\text{ cm}^2$',
                        '$125\\text{ cm}^2$'],
            'answer': 0,
            'solution': 'Ta có $S_{\\text{xq}} = 5 \\times 5 \\times 4 = 100\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 51: Diện tích xung quanh và diện tích toàn phần của hình lập phương**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Diện tích một mặt**?',
            'options': ['$S_1 = a : a$',
                        '$S_1 = a \\times a$',
                        'Đảo ngược vế của quy tắc: $S_1 = a \\times a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $S_1 = a \\times a$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 51: Diện tích xung quanh và diện tích toàn phần '
                        'của hình lập phương, **Diện tích một mặt** được xác định bởi: $S_1 = a \\times a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 51: Diện tích xung quanh và diện tích toàn phần của hình lập phương**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Diện tích xung quanh**?',
            'options': ['$S_{\\text{xq}} = a : a \\times 4$',
                        '$S_{\\text{xq}} = a \\times a \\times 3$',
                        '$S_{\\text{xq}} = a \\times a \\times 4$',
                        '$S_{\\text{xq}} = a \\times a \\times 8$'],
            'answer': 2,
            'solution': 'Trong Bài 51: Diện tích xung quanh và diện tích toàn phần của hình lập phương, '
                        '**Diện tích xung quanh** có công thức/quy tắc là: $S_{\\text{xq}} = a \\times a '
                        '\\times 4$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình lập phương có diện tích xung quanh là $36\\text{ cm}^2$. Diện tích toàn phần của '
                 'hình lập phương đó là:',
            'options': ['$72\\text{ cm}^2$', '$216\\text{ cm}^2$', '$48\\text{ cm}^2$', '$54\\text{ cm}^2$'],
            'answer': 3,
            'solution': 'Diện tích một mặt là $36 : 4 = 9\\text{ cm}^2$, suy ra $S_{\\text{tp}} = 9 \\times '
                        '6 = 54\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 51: Diện tích xung quanh và diện tích toàn phần của hình '
                 'lập phương**, nhận định nào sau đây là **chính xác**?',
            'options': ['Hiểu và vận dụng được công thức tính diện tích xung quanh, diện tích toàn phần của '
                        'hình lập phương.',
                        'Hiểu và vận dụng được công thức tính diện tích xung quanh, diện tích toàn phần của '
                        'hình lập phương. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu và vận dụng được công thức tính diện tích xung '
                        'quanh, diện tích toàn phần của hình lập phương.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu và vận dụng được công thức '
                        'tính diện tích xung quanh, diện tích toàn phần của hình lập phương.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 51: Diện tích xung quanh và diện tích toàn phần của '
                        'hình lập phương: Hiểu và vận dụng được công thức tính diện tích xung quanh, diện '
                        'tích toàn phần của hình lập phương.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nếu cạnh của hình lập phương gấp lên $2$ lần thì diện tích toàn phần của nó gấp lên $4$ '
                 'lần.',
            'answer': True,
            'solution': 'Diện tích một mặt $(2a) \\times (2a) = 4 \\times (a \\times a)$ gấp lên $4$ lần nên '
                        'diện tích toàn phần cũng gấp lên $4$ lần.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 51: Diện tích xung quanh và diện tích toàn phần của hình lập phương**, quy tắc '
                 '**Diện tích một mặt** được xác định bởi $S_1 = a \\times a$ và khi áp dụng cho ví dụ “Một '
                 'hình lập phương có diện tích xung quanh là $36\\text{ cm}^2$. Tính diện tích toàn phần và '
                 'độ dài cạnh của hình lập phương đó.” ta có lời giải: Diện tích một mặt là $36 : 4 = '
                 '9\\text{ cm}^2$. Vì $9 = 3 \\times 3$ nên cạnh $a = 3\\text{ cm}$. Diện tích toàn phần là '
                 '$9 \\times 6 = 54\\text{ cm}^2$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Diện tích một mặt** ($S_1 = a \\times '
                        'a$) và lời giải ví dụ minh họa của Bài 51: Diện tích xung quanh và diện tích toàn '
                        'phần của hình lập phương.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 51: Diện tích xung quanh và diện tích toàn phần của '
                 'hình lập phương** để giải bài toán sau: Một hình lập phương có diện tích xung quanh là '
                 '$36\\text{ cm}^2$. Tính diện tích toàn phần và độ dài cạnh của hình lập phương đó. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Diện tích một mặt là $36 : 4 = 9\\text{ cm}^2$. Vì $9 = 3 : 3$ nên cạnh $a = '
                        '3\\text{ cm}$. Diện tích toàn phần là $9 \\times 6 = 54\\text{ cm}^2$.',
                        'Diện tích một mặt là $36 : 4 = 9\\text{ cm}^2$. Vì $9 = 3 \\times 3$ nên cạnh $a = '
                        '3\\text{ cm}$. Diện tích toàn phần là $9 \\times 6 = 54\\text{ cm}^2$.',
                        'Diện tích một mặt là $36 : 4 = 9\\text{ cm}^2$. Vì $9 = 3 \\times 3$ nên cạnh $a = '
                        '3\\text{ cm}$. Diện tích toàn phần là $9 \\times 6 = 54\\text{ cm}^1$.',
                        'Diện tích một mặt là $72 : 4 = 9\\text{ cm}^2$. Vì $9 = 3 \\times 3$ nên cạnh $a = '
                        '3\\text{ cm}$. Diện tích toàn phần là $9 \\times 6 = 54\\text{ cm}^2$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 51: Diện tích xung quanh và diện tích toàn phần của hình '
                        'lập phương: Diện tích một mặt là $36 : 4 = 9\\text{ cm}^2$. Vì $9 = 3 \\times 3$ '
                        'nên cạnh $a = 3\\text{ cm}$. Diện tích toàn phần là $9 \\times 6 = 54\\text{ '
                        'cm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp quà hình lập phương có cạnh $1{,}5\\text{ dm}$. Tính diện tích toàn phần của hộp '
                 'quà đó theo đơn vị đề-xi-mét vuông.',
            'answer': ['13,5', '13.5'],
            'unit': None,
            'solution': 'Diện tích toàn phần của hộp quà là $1{,}5 \\times 1{,}5 \\times 6 = 13{,}5$ '
                        '($\\text{dm}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd09-dien-tich-the-tich-hinh-khoi',
  'context_title': 'Chủ đề 9: Diện tích và thể tích của một số hình khối',
  'context': 'Chủ đề 9 · SGK Toán 5: Hình khai triển, diện tích xung quanh, diện tích toàn phần và thể tích '
             'hình khối.',
  'title': 'Bài 52: Thể tích của hình hộp chữ nhật',
  'icon': '📦',
  'description': 'Quy tắc và công thức tính thể tích của hình hộp chữ nhật.',
  'requirements': ['Tính được thể tích hình hộp chữ nhật khi biết ba kích thước chiều dài, chiều rộng, chiều '
                   'cao.',
                   'Vận dụng tính thể tích nước trong bể, chiều cao mực nước và các bài toán thực tiễn.',
                   'Vận dụng kiến thức của **Bài 52: Thể tích của hình hộp chữ nhật** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': '- Muốn tính **thể tích hình hộp chữ nhật**, ta lấy chiều dài nhân với chiều rộng rồi nhân '
                'với chiều cao (cùng một đơn vị đo): $V = a \\times b \\times c$.',
  'theory': '### 1. Công thức và hệ quả\n'
            '- Gọi diện tích mặt đáy là $S_{\\text{đáy}} = a \\times b$, khi đó $V = S_{\\text{đáy}} \\times '
            'c$.\n'
            '- Suy ra chiều cao $c = V : (a \\times b)$ và diện tích đáy $S_{\\text{đáy}} = V : c$.\n'
            '### 2. Bài toán mực nước trong bể\n'
            '- Thể tích nước trong bể bằng diện tích đáy bể nhân với **chiều cao mực nước**.',
  'formulas': [{'category': 'Thể tích hình hộp chữ nhật',
                'items': [{'name': 'Công thức thể tích',
                           'formula': '$V = a \\times b \\times c$ ($a, b, c$ cùng đơn vị đo)'},
                          {'name': 'Tìm chiều cao', 'formula': '$c = \\dfrac{V}{a \\times b}$'}]}],
  'example': 'Một bể nước hình hộp chữ nhật dài $2\\text{ m}$, rộng $1{,}5\\text{ m}$ và cao $1\\text{ m}$. '
             'Hỏi bể chứa được tối đa bao nhiêu lít nước?',
  'example_answer': 'Thể tích của bể là $V = 2 \\times 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ dm}^3 = '
                    '3000\\text{ l}$.',
  'real_life': 'Tính lượng nước trong bể bơi, bể cá cảnh hoặc sức chứa của thùng xe tải.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính thể tích hình hộp chữ nhật có ba kích thước $a, b, c$ (cùng đơn vị đo) là:',
            'options': ['$V = a \\times b \\times c$',
                        '$V = (a + b) \\times 2 \\times c$',
                        '$V = a \\times b$',
                        '$V = a + b + c$'],
            'answer': 0,
            'solution': 'Thể tích hình hộp chữ nhật là $V = a \\times b \\times c$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình hộp chữ nhật có chiều dài $5\\text{ cm}$, chiều rộng $4\\text{ cm}$ và chiều cao '
                 '$3\\text{ cm}$ có thể tích là:',
            'options': ['$54\\text{ cm}^3$', '$60\\text{ cm}^3$', '$94\\text{ cm}^3$', '$12\\text{ cm}^3$'],
            'answer': 1,
            'solution': 'Ta có $V = 5 \\times 4 \\times 3 = 60\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 52: Thể tích của hình hộp chữ nhật**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Công thức thể tích**?',
            'options': ['$V = a : b \\times c$ ($a, b, c$ cùng đơn vị đo)',
                        'Đảo ngược vế của quy tắc: $V = a \\times b \\times c$ ($a, b, c$ cùng đơn vị đo)',
                        '$V = a \\times b \\times c$ ($a, b, c$ cùng đơn vị đo)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $V = a \\times b \\times c$ '
                        '($a, b, c$ cùng đơn vị đo)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 52: Thể tích của hình hộp chữ nhật, **Công thức '
                        'thể tích** được xác định bởi: $V = a \\times b \\times c$ ($a, b, c$ cùng đơn vị '
                        'đo).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 52: Thể tích của hình hộp chữ nhật**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tìm chiều cao**?',
            'options': ['$c = \\dfrac{V}{a : b}$',
                        '$c = \\dfrac{a \\times b}{V}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $c = \\dfrac{V}{a \\times b}$',
                        '$c = \\dfrac{V}{a \\times b}$'],
            'answer': 3,
            'solution': 'Trong Bài 52: Thể tích của hình hộp chữ nhật, **Tìm chiều cao** có công thức/quy '
                        'tắc là: $c = \\dfrac{V}{a \\times b}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình hộp chữ nhật có thể tích $120\\text{ dm}^3$, chiều dài $6\\text{ dm}$ và chiều '
                 'rộng $4\\text{ dm}$. Chiều cao của hình hộp là:',
            'options': ['$5\\text{ dm}$', '$12\\text{ dm}$', '$24\\text{ dm}$', '$6\\text{ dm}$'],
            'answer': 0,
            'solution': 'Chiều cao hình hộp là $c = 120 : (6 \\times 4) = 120 : 24 = 5\\text{ dm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 52: Thể tích của hình hộp chữ nhật**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Tính được thể tích hình hộp chữ nhật khi biết ba kích thước chiều dài, chiều rộng, '
                        'chiều cao. (với dấu ngược lại)',
                        'Tính được thể tích hình hộp chữ nhật khi biết ba kích thước chiều dài, chiều rộng, '
                        'chiều cao.',
                        'Đảo ngược vế của quy tắc: Tính được thể tích hình hộp chữ nhật khi biết ba kích '
                        'thước chiều dài, chiều rộng, chiều cao.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được thể tích hình hộp chữ '
                        'nhật khi biết ba kích thước chiều dài, chiều rộng, chiều cao.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 52: Thể tích của hình hộp chữ nhật: Tính được thể '
                        'tích hình hộp chữ nhật khi biết ba kích thước chiều dài, chiều rộng, chiều cao.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hình hộp chữ nhật có chiều dài $5\\text{ cm}$, chiều rộng $3\\text{ cm}$, chiều cao '
                 '$2\\text{ cm}$ có thể tích là $30\\text{ cm}^3$.',
            'answer': True,
            'solution': 'Ta có $V = 5 \\times 3 \\times 2 = 30\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 52: Thể tích của hình hộp chữ nhật**, quy tắc **Công thức thể tích** được xác '
                 'định bởi $V = a \\times b \\times c$ ($a, b, c$ cùng đơn vị đo) và khi áp dụng cho ví dụ '
                 '“Một bể nước hình hộp chữ nhật dài $2\\text{ m}$, rộng $1{,}5\\text{ m}$ và cao $1\\text{ '
                 'm}$. Hỏi bể chứa được tối đa bao nhiêu lít nước?” ta có lời giải: Thể tích của bể là $V = '
                 '2 \\times 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ dm}^3 = 3000\\text{ l}$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Công thức thể tích** ($V = a \\times b '
                        '\\times c$ ($a, b, c$ cùng đơn vị đo)) và lời giải ví dụ minh họa của Bài 52: Thể '
                        'tích của hình hộp chữ nhật.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 52: Thể tích của hình hộp chữ nhật** để giải bài '
                 'toán sau: Một bể nước hình hộp chữ nhật dài $2\\text{ m}$, rộng $1{,}5\\text{ m}$ và cao '
                 '$1\\text{ m}$. Hỏi bể chứa được tối đa bao nhiêu lít nước? Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Thể tích của bể là $V = 2 : 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ dm}^3 = '
                        '3000\\text{ l}$.',
                        'Thể tích của bể là $V = 2 \\times 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ '
                        'dm}^3 = 2999\\text{ l}$.',
                        'Thể tích của bể là $V = 2 \\times 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ '
                        'dm}^3 = 3000\\text{ l}$.',
                        'Thể tích của bể là $V = 4 \\times 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ '
                        'dm}^3 = 3000\\text{ l}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 52: Thể tích của hình hộp chữ nhật: Thể tích của bể là '
                        '$V = 2 \\times 1{,}5 \\times 1 = 3\\text{ m}^3 = 3000\\text{ dm}^3 = 3000\\text{ '
                        'l}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bể cá hình hộp chữ nhật có chiều dài $80\\text{ cm}$, chiều rộng $50\\text{ cm}$ và '
                 'chiều cao $45\\text{ cm}$. Hiện mực nước trong bể cao $30\\text{ cm}$. Hỏi trong bể đang '
                 'có bao nhiêu lít nước?',
            'answer': ['120'],
            'unit': None,
            'solution': 'Thể tích nước trong bể là $80 \\times 50 \\times 30 = 120\\,000\\text{ cm}^3 = '
                        '120\\text{ dm}^3 = 120\\text{ l}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd09-dien-tich-the-tich-hinh-khoi',
  'context_title': 'Chủ đề 9: Diện tích và thể tích của một số hình khối',
  'context': 'Chủ đề 9 · SGK Toán 5: Hình khai triển, diện tích xung quanh, diện tích toàn phần và thể tích '
             'hình khối.',
  'title': 'Bài 53: Thể tích của hình lập phương',
  'icon': '📦',
  'description': 'Quy tắc và công thức tính thể tích của hình lập phương.',
  'requirements': ['Tính được thể tích của hình lập phương khi biết độ dài cạnh.',
                   'So sánh và giải quyết được các bài toán thực tế liên quan đến thể tích hình lập phương.',
                   'Vận dụng kiến thức của **Bài 53: Thể tích của hình lập phương** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': '- Hình lập phương là hình hộp chữ nhật đặc biệt có ba kích thước bằng nhau ($a = b = c$).\n'
                '- Muốn tính **thể tích hình lập phương**, ta lấy cạnh nhân với cạnh rồi nhân với cạnh: $V = '
                'a \\times a \\times a$.',
  'theory': '### 1. Tính thể tích hình lập phương\n'
            '- Với cạnh $a = 4\\text{ cm}$: thể tích là $V = 4 \\times 4 \\times 4 = 64\\text{ cm}^3$.\n'
            '### 2. Sự thay đổi thể tích khi cạnh thay đổi\n'
            '- Nếu gấp cạnh hình lập phương lên $k$ lần thì thể tích của nó gấp lên $k \\times k \\times k$ '
            'lần (ví dụ gấp cạnh lên $2$ lần thì thể tích gấp $2 \\times 2 \\times 2 = 8$ lần).',
  'formulas': [{'category': 'Thể tích hình lập phương',
                'items': [{'name': 'Công thức thể tích',
                           'formula': '$V = a \\times a \\times a$ ($a$: độ dài cạnh)'},
                          {'name': 'Một số thể tích quen thuộc',
                           'formula': '$2^3 = 8$; $3^3 = 27$; $4^3 = 64$; $5^3 = 125$; $10^3 = 1000$'}]}],
  'example': 'Tính thể tích của một khối gỗ hình lập phương có cạnh $0{,}5\\text{ m}$ theo đơn vị đề-xi-mét '
             'khối.',
  'example_answer': 'Đổi $0{,}5\\text{ m} = 5\\text{ dm}$. Thể tích khối gỗ là $V = 5 \\times 5 \\times 5 = '
                    '125\\text{ dm}^3$.',
  'real_life': 'Tính thể tích khối rubik, thùng chứa hình lập phương và khối đá lạnh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Thể tích của hình lập phương có cạnh $3\\text{ cm}$ là:',
            'options': ['$9\\text{ cm}^3$', '$27\\text{ cm}^3$', '$18\\text{ cm}^3$', '$54\\text{ cm}^3$'],
            'answer': 1,
            'solution': 'Ta có $V = 3 \\times 3 \\times 3 = 27\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính thể tích hình lập phương có cạnh $a$ là:',
            'options': ['$V = a \\times 4$',
                        '$V = a \\times a \\times 6$',
                        '$V = a \\times a \\times a$',
                        '$V = a \\times 3$'],
            'answer': 2,
            'solution': 'Thể tích hình lập phương là $V = a \\times a \\times a$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 53: Thể tích của hình lập phương**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Công thức thể tích**?',
            'options': ['$V = a : a \\times a$ ($a$: độ dài cạnh)',
                        'Đảo ngược vế của quy tắc: $V = a \\times a \\times a$ ($a$: độ dài cạnh)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $V = a \\times a \\times a$ '
                        '($a$: độ dài cạnh)',
                        '$V = a \\times a \\times a$ ($a$: độ dài cạnh)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 53: Thể tích của hình lập phương, **Công thức thể '
                        'tích** được xác định bởi: $V = a \\times a \\times a$ ($a$: độ dài cạnh).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 53: Thể tích của hình lập phương**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Một số thể tích quen thuộc**?',
            'options': ['$2^3 = 8$; $3^3 = 27$; $4^3 = 64$; $5^3 = 125$; $10^3 = 1000$',
                        '$3^3 = 8$; $3^3 = 27$; $4^3 = 64$; $5^3 = 125$; $10^3 = 1000$',
                        '$2^3 = 8$; $3^3 = 27$; $4^3 = 64$; $5^3 = 125$; $10^3 = 999$',
                        '$4^3 = 8$; $3^3 = 27$; $4^3 = 64$; $5^3 = 125$; $10^3 = 1000$'],
            'answer': 0,
            'solution': 'Trong Bài 53: Thể tích của hình lập phương, **Một số thể tích quen thuộc** có công '
                        'thức/quy tắc là: $2^3 = 8$; $3^3 = 27$; $4^3 = 64$; $5^3 = 125$; $10^3 = 1000$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình lập phương có diện tích một mặt là $25\\text{ dm}^2$. Thể tích của hình lập '
                 'phương đó là:',
            'options': ['$150\\text{ dm}^3$',
                        '$125\\text{ dm}^3$',
                        '$75\\text{ dm}^3$',
                        '$100\\text{ dm}^3$'],
            'answer': 1,
            'solution': 'Vì $25 = 5 \\times 5$ nên cạnh của hình lập phương là $5\\text{ dm}$, thể tích là '
                        '$5 \\times 5 \\times 5 = 125\\text{ dm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 53: Thể tích của hình lập phương**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Tính được thể tích của hình lập phương khi biết độ dài cạnh. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính được thể tích của hình lập phương khi biết độ dài '
                        'cạnh.',
                        'Tính được thể tích của hình lập phương khi biết độ dài cạnh.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được thể tích của hình lập '
                        'phương khi biết độ dài cạnh.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 53: Thể tích của hình lập phương: Tính được thể tích '
                        'của hình lập phương khi biết độ dài cạnh.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nếu gấp cạnh của một hình lập phương lên $2$ lần thì thể tích của nó gấp lên $2$ lần.',
            'answer': False,
            'solution': 'Khi cạnh gấp lên $2$ lần thì thể tích gấp lên $2 \\times 2 \\times 2 = 8$ lần.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 53: Thể tích của hình lập phương**, quy tắc **Công thức thể tích** được xác '
                 'định bởi $V = a \\times a \\times a$ ($a$: độ dài cạnh) và khi áp dụng cho ví dụ “Tính thể '
                 'tích của một khối gỗ hình lập phương có cạnh $0{,}5\\text{ m}$ theo đơn vị đề-xi-mét '
                 'khối.” ta có lời giải: Đổi $0{,}5\\text{ m} = 5\\text{ dm}$. Thể tích khối gỗ là $V = 5 '
                 '\\times 5 \\times 5 = 125\\text{ dm}^3$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Công thức thể tích** ($V = a \\times a '
                        '\\times a$ ($a$: độ dài cạnh)) và lời giải ví dụ minh họa của Bài 53: Thể tích của '
                        'hình lập phương.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 53: Thể tích của hình lập phương** để giải bài toán '
                 'sau: Tính thể tích của một khối gỗ hình lập phương có cạnh $0{,}5\\text{ m}$ theo đơn vị '
                 'đề-xi-mét khối. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đổi $0{,}5\\text{ m} = 5\\text{ dm}$. Thể tích khối gỗ là $V = 5 : 5 \\times 5 = '
                        '125\\text{ dm}^3$.',
                        'Đổi $0{,}5\\text{ m} = 5\\text{ dm}$. Thể tích khối gỗ là $V = 5 \\times 5 \\times '
                        '5 = 125\\text{ dm}^2$.',
                        'Đổi $2{,}5\\text{ m} = 5\\text{ dm}$. Thể tích khối gỗ là $V = 5 \\times 5 \\times '
                        '5 = 125\\text{ dm}^3$.',
                        'Đổi $0{,}5\\text{ m} = 5\\text{ dm}$. Thể tích khối gỗ là $V = 5 \\times 5 \\times '
                        '5 = 125\\text{ dm}^3$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 53: Thể tích của hình lập phương: Đổi $0{,}5\\text{ m} = '
                        '5\\text{ dm}$. Thể tích khối gỗ là $V = 5 \\times 5 \\times 5 = 125\\text{ dm}^3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bể nước hình lập phương có cạnh đo trong lòng bể là $1{,}2\\text{ m}$. Khi bể chứa đầy '
                 'nước thì trong bể có bao nhiêu lít nước?',
            'answer': ['1728'],
            'unit': None,
            'solution': 'Đổi $1{,}2\\text{ m} = 12\\text{ dm}$. Thể tích bể là $12 \\times 12 \\times 12 = '
                        '1728\\text{ dm}^3 = 1728\\text{ l}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd10-thoi-gian-van-toc-chuyen-dong-deu',
  'context_title': 'Chủ đề 10: Số đo thời gian, vận tốc. Các bài toán liên quan đến chuyển động đều',
  'context': 'Chủ đề 10 · SGK Toán 5: Số đo thời gian và các bài toán về vận tốc, quãng đường, thời gian.',
  'title': 'Bài 56: Các đơn vị đo thời gian',
  'icon': '🚗',
  'description': 'Hệ thống hóa các đơn vị đo thời gian (thế kỉ, năm, tháng, ngày, giờ, phút, giây) và cách '
                 'đổi số đo thời gian sang số thập phân.',
  'requirements': ['Nắm vững mối quan hệ giữa các đơn vị đo thời gian từ thế kỉ đến giây.',
                   'Chuyển đổi được số đo thời gian giữa phút và giờ, giây và phút dưới dạng phân số hoặc số '
                   'thập phân.',
                   'Vận dụng kiến thức của **Bài 56: Các đơn vị đo thời gian** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- $1$ thế kỉ $= 100$ năm; $1$ năm $= 12$ tháng ($365$ ngày, năm nhuận $366$ ngày); $1$ ngày '
                '$= 24$ giờ; $1$ giờ $= 60$ phút; $1$ phút $= 60$ giây.\n'
                '- Đổi phút sang giờ dưới dạng số thập phân: lấy số phút chia cho $60$ (ví dụ $30\\text{ '
                'phút} = \\dfrac{30}{60}\\text{ giờ} = 0{,}5\\text{ giờ}$).',
  'theory': '### 1. Các mốc đổi thời gian thập phân thường gặp\n'
            '- $15\\text{ phút} = 0{,}25\\text{ giờ}$; $30\\text{ phút} = 0{,}5\\text{ giờ}$; $45\\text{ '
            'phút} = 0{,}75\\text{ giờ}$; $12\\text{ phút} = 0{,}2\\text{ giờ}$; $6\\text{ phút} = '
            '0{,}1\\text{ giờ}$.\n'
            '- Đổi ngược lại từ giờ thập phân sang phút: nhân phần thập phân với $60$, ví dụ $2{,}25\\text{ '
            'giờ} = 2\\text{ giờ } 15\\text{ phút}$.',
  'formulas': [{'category': 'Quan hệ đơn vị thời gian',
                'items': [{'name': 'Ngày, giờ, phút, giây',
                           'formula': '$1\\text{ ngày} = 24\\text{ giờ}$; $1\\text{ giờ} = 60\\text{ phút}$; '
                                      '$1\\text{ phút} = 60\\text{ giây}$'},
                          {'name': 'Đổi m phút sang giờ',
                           'formula': '$m\\text{ phút} = \\dfrac{m}{60}\\text{ giờ}$'}]}],
  'example': 'Đổi các số đo sau: $1\\text{ giờ } 30\\text{ phút} = \\dots\\text{ giờ}$ và $2{,}75\\text{ '
             'giờ} = \\dots\\text{ phút}$.',
  'example_answer': 'Ta có $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = '
                    '2{,}75 \\times 60 = 165\\text{ phút}$.',
  'real_life': 'Đọc thời gian thi đấu thể thao, tính thời gian di chuyển của tàu xe và xác định thế kỉ lịch '
               'sử.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một năm nhuận có tất cả bao nhiêu ngày?',
            'options': ['$365$ ngày', '$360$ ngày', '$366$ ngày', '$364$ ngày'],
            'answer': 2,
            'solution': 'Năm nhuận có $366$ ngày (tháng $2$ có $29$ ngày).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số đo $1\\text{ giờ } 30\\text{ phút}$ viết dưới dạng số thập phân có đơn vị giờ là:',
            'options': ['$1{,}3\\text{ giờ}$',
                        '$1{,}30\\text{ giờ}$',
                        '$130\\text{ giờ}$',
                        '$1{,}5\\text{ giờ}$'],
            'answer': 3,
            'solution': 'Vì $30\\text{ phút} = \\dfrac{30}{60}\\text{ giờ} = 0{,}5\\text{ giờ}$ nên bằng '
                        '$1{,}5\\text{ giờ}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 56: Các đơn vị đo thời gian**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Ngày, giờ, phút, giây**?',
            'options': ['$1\\text{ ngày} = 24\\text{ giờ}$; $1\\text{ giờ} = 60\\text{ phút}$; $1\\text{ '
                        'phút} = 60\\text{ giây}$',
                        '$2\\text{ ngày} = 24\\text{ giờ}$; $1\\text{ giờ} = 60\\text{ phút}$; $1\\text{ '
                        'phút} = 60\\text{ giây}$',
                        '$1\\text{ ngày} = 24\\text{ giờ}$; $1\\text{ giờ} = 60\\text{ phút}$; $1\\text{ '
                        'phút} = 59\\text{ giây}$',
                        '$m\\text{ phút} = \\dfrac{m}{60}\\text{ giờ}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 56: Các đơn vị đo thời gian, **Ngày, giờ, phút, '
                        'giây** được xác định bởi: $1\\text{ ngày} = 24\\text{ giờ}$; $1\\text{ giờ} = '
                        '60\\text{ phút}$; $1\\text{ phút} = 60\\text{ giây}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 56: Các đơn vị đo thời gian**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Đổi m phút sang giờ**?',
            'options': ['$m\\text{ phút} = \\dfrac{m}{70}\\text{ giờ}$',
                        '$m\\text{ phút} = \\dfrac{m}{60}\\text{ giờ}$',
                        '$m\\text{ phút} = \\dfrac{60}{m}\\text{ giờ}$',
                        '$m\\text{ phút} = \\dfrac{m}{62}\\text{ giờ}$'],
            'answer': 1,
            'solution': 'Trong Bài 56: Các đơn vị đo thời gian, **Đổi m phút sang giờ** có công thức/quy tắc '
                        'là: $m\\text{ phút} = \\dfrac{m}{60}\\text{ giờ}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đổi $2{,}25\\text{ giờ}$ sang đơn vị phút ta được:',
            'options': ['$225\\text{ phút}$',
                        '$145\\text{ phút}$',
                        '$135\\text{ phút}$',
                        '$125\\text{ phút}$'],
            'answer': 2,
            'solution': 'Ta có $2{,}25 \\times 60 = 135\\text{ phút}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 56: Các đơn vị đo thời gian**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nắm vững mối quan hệ giữa các đơn vị đo thời gian từ thế kỉ đến giây. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Nắm vững mối quan hệ giữa các đơn vị đo thời gian từ thế '
                        'kỉ đến giây.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nắm vững mối quan hệ giữa các '
                        'đơn vị đo thời gian từ thế kỉ đến giây.',
                        'Nắm vững mối quan hệ giữa các đơn vị đo thời gian từ thế kỉ đến giây.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 56: Các đơn vị đo thời gian: Nắm vững mối quan hệ '
                        'giữa các đơn vị đo thời gian từ thế kỉ đến giây.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Số đo $45\\text{ phút}$ bằng $0{,}75\\text{ giờ}$.',
            'answer': True,
            'solution': 'Ta có $45 : 60 = 0{,}75\\text{ giờ}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 56: Các đơn vị đo thời gian**, quy tắc **Ngày, giờ, phút, giây** được xác định '
                 'bởi $1\\text{ ngày} = 24\\text{ giờ}$; $1\\text{ giờ} = 60\\text{ phút}$; $1\\text{ phút} '
                 '= 60\\text{ giây}$ và khi áp dụng cho ví dụ “Đổi các số đo sau: $1\\text{ giờ } 30\\text{ '
                 'phút} = \\dots\\text{ giờ}$ và $2{,}75\\text{ giờ} = \\dots\\text{ phút}$.” ta có lời '
                 'giải: Ta có $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = '
                 '2{,}75 \\times 60 = 165\\text{ phút}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ngày, giờ, phút, giây** ($1\\text{ ngày} '
                        '= 24\\text{ giờ}$; $1\\text{ giờ} = 60\\text{ phút}$; $1\\text{ phút} = 60\\text{ '
                        'giây}$) và lời giải ví dụ minh họa của Bài 56: Các đơn vị đo thời gian.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 56: Các đơn vị đo thời gian** để giải bài toán sau: '
                 'Đổi các số đo sau: $1\\text{ giờ } 30\\text{ phút} = \\dots\\text{ giờ}$ và $2{,}75\\text{ '
                 'giờ} = \\dots\\text{ phút}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = '
                        '2{,}75 \\times 60 = 165\\text{ phút}$.',
                        'Ta có $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = '
                        '2{,}75 : 60 = 165\\text{ phút}$.',
                        'Ta có $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = '
                        '2{,}75 \\times 60 = 164\\text{ phút}$.',
                        'Ta có $2\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = '
                        '2{,}75 \\times 60 = 165\\text{ phút}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 56: Các đơn vị đo thời gian: Ta có $1\\text{ giờ } '
                        '30\\text{ phút} = 1{,}5\\text{ giờ}$ và $2{,}75\\text{ giờ} = 2{,}75 \\times 60 = '
                        '165\\text{ phút}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bộ phim kéo dài $1{,}8\\text{ giờ}$. Hỏi bộ phim đó kéo dài bao nhiêu phút?',
            'answer': ['108'],
            'unit': None,
            'solution': 'Thời lượng bộ phim là $1{,}8 \\times 60 = 108$ (phút).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd10-thoi-gian-van-toc-chuyen-dong-deu',
  'context_title': 'Chủ đề 10: Số đo thời gian, vận tốc. Các bài toán liên quan đến chuyển động đều',
  'context': 'Chủ đề 10 · SGK Toán 5: Số đo thời gian và các bài toán về vận tốc, quãng đường, thời gian.',
  'title': 'Bài 57: Cộng, trừ, nhân, chia số đo thời gian',
  'icon': '🚗',
  'description': 'Quy tắc thực hiện bốn phép tính cộng, trừ, nhân, chia với các số đo thời gian.',
  'requirements': ['Thực hiện được phép cộng, phép trừ hai số đo thời gian (có đổi đơn vị hoặc mượn '
                   '$1\\text{ giờ} = 60\\text{ phút}$).',
                   'Thực hiện được phép nhân và phép chia số đo thời gian với một số.',
                   'Vận dụng kiến thức của **Bài 57: Cộng, trừ, nhân, chia số đo thời gian** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '- Khi **cộng hoặc trừ** số đo thời gian, ta đặt thẳng cột theo từng loại đơn vị; nếu số '
                'phút (hoặc giây) ở tổng $\\ge 60$ thì đổi sang giờ (hoặc phút); nếu số bị trừ có số phút bé '
                'hơn số trừ thì **mượn $1\\text{ giờ} = 60\\text{ phút}$**.\n'
                '- Khi **nhân hoặc chia** số đo thời gian với một số, ta thực hiện với từng đơn vị đo từ lớn '
                'đến bé (khi chia có dư thì đổi số dư sang đơn vị nhỏ hơn liền kề).',
  'theory': '### 1. Cộng và trừ số đo thời gian\n'
            '- Cộng: $3\\text{ giờ } 45\\text{ phút} + 2\\text{ giờ } 30\\text{ phút} = 5\\text{ giờ } '
            '75\\text{ phút} = 6\\text{ giờ } 15\\text{ phút}$.\n'
            '- Trừ: $4\\text{ giờ } 20\\text{ phút} - 1\\text{ giờ } 45\\text{ phút} = 3\\text{ giờ } '
            '80\\text{ phút} - 1\\text{ giờ } 45\\text{ phút} = 2\\text{ giờ } 35\\text{ phút}$.\n'
            '### 2. Nhân và chia số đo thời gian\n'
            '- Nhân: $2\\text{ giờ } 20\\text{ phút} \\times 3 = 6\\text{ giờ } 60\\text{ phút} = 7\\text{ '
            'giờ}$.\n'
            '- Chia: $7\\text{ giờ } 30\\text{ phút} : 3 = 2\\text{ giờ } 30\\text{ phút}$ (vì $7\\text{ '
            'giờ} : 3 = 2\\text{ giờ}$ dư $1\\text{ giờ} = 60\\text{ phút}$, cộng $30\\text{ phút}$ là '
            '$90\\text{ phút} : 3 = 30\\text{ phút}$).',
  'formulas': [{'category': 'Quy tắc đổi và mượn',
                'items': [{'name': 'Khi tổng >= 60 phút',
                           'formula': 'Cứ $60\\text{ phút}$ đổi thành $1\\text{ giờ}$'},
                          {'name': 'Khi trừ thiếu phút',
                           'formula': 'Mượn $1\\text{ giờ} = 60\\text{ phút}$ cộng vào số phút của số bị '
                                      'trừ'}]}],
  'example': 'Tính: $5\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 40\\text{ phút}$.',
  'example_answer': 'Đổi $5\\text{ giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó $4\\text{ '
                    'giờ } 75\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } 35\\text{ '
                    'phút}$.',
  'real_life': 'Tính giờ tàu đến ga, thời gian làm việc trong ca và thời gian sản xuất một sản phẩm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $2\\text{ giờ } 25\\text{ phút} + 1\\text{ giờ } 35\\text{ phút}$ '
                 'là:',
            'options': ['$3\\text{ giờ } 50\\text{ phút}$',
                        '$3\\text{ giờ } 60\\text{ phút}$',
                        '$4\\text{ giờ } 10\\text{ phút}$',
                        '$4\\text{ giờ}$'],
            'answer': 3,
            'solution': 'Ta có $2\\text{ giờ } 25\\text{ phút} + 1\\text{ giờ } 35\\text{ phút} = 3\\text{ '
                        'giờ } 60\\text{ phút} = 4\\text{ giờ}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $4\\text{ giờ } 20\\text{ phút} - 1\\text{ giờ } 45\\text{ phút}$ là:',
            'options': ['$2\\text{ giờ } 35\\text{ phút}$',
                        '$3\\text{ giờ } 25\\text{ phút}$',
                        '$2\\text{ giờ } 75\\text{ phút}$',
                        '$3\\text{ giờ } 35\\text{ phút}$'],
            'answer': 0,
            'solution': 'Mượn $1\\text{ giờ}$: $3\\text{ giờ } 80\\text{ phút} - 1\\text{ giờ } 45\\text{ '
                        'phút} = 2\\text{ giờ } 35\\text{ phút}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 57: Cộng, trừ, nhân, chia số đo thời gian**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Khi tổng >= 60 phút**?',
            'options': ['Cứ $70\\text{ phút}$ đổi thành $1\\text{ giờ}$',
                        'Cứ $60\\text{ phút}$ đổi thành $1\\text{ giờ}$',
                        'Cứ $60\\text{ phút}$ đổi thành $2\\text{ giờ}$',
                        'Cứ $62\\text{ phút}$ đổi thành $1\\text{ giờ}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 57: Cộng, trừ, nhân, chia số đo thời gian, **Khi '
                        'tổng >= 60 phút** được xác định bởi: Cứ $60\\text{ phút}$ đổi thành $1\\text{ '
                        'giờ}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 57: Cộng, trừ, nhân, chia số đo thời gian**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Khi trừ thiếu phút**?',
            'options': ['Mượn $2\\text{ giờ} = 60\\text{ phút}$ cộng vào số phút của số bị trừ',
                        'Mượn $1\\text{ giờ} = 59\\text{ phút}$ cộng vào số phút của số bị trừ',
                        'Mượn $1\\text{ giờ} = 60\\text{ phút}$ cộng vào số phút của số bị trừ',
                        'Cứ $60\\text{ phút}$ đổi thành $1\\text{ giờ}$'],
            'answer': 2,
            'solution': 'Trong Bài 57: Cộng, trừ, nhân, chia số đo thời gian, **Khi trừ thiếu phút** có công '
                        'thức/quy tắc là: Mượn $1\\text{ giờ} = 60\\text{ phút}$ cộng vào số phút của số bị '
                        'trừ.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $7\\text{ giờ } 30\\text{ phút} : 3$ là:',
            'options': ['$2\\text{ giờ } 10\\text{ phút}$',
                        '$2\\text{ giờ } 15\\text{ phút}$',
                        '$2\\text{ giờ } 50\\text{ phút}$',
                        '$2\\text{ giờ } 30\\text{ phút}$'],
            'answer': 3,
            'solution': 'Ta có $7\\text{ giờ} : 3 = 2\\text{ giờ}$ dư $1\\text{ giờ} = 60\\text{ phút}$; '
                        '$(60 + 30)\\text{ phút} : 3 = 30\\text{ phút}$, được $2\\text{ giờ } 30\\text{ '
                        'phút}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 57: Cộng, trừ, nhân, chia số đo thời gian**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Thực hiện được phép cộng, phép trừ hai số đo thời gian (có đổi đơn vị hoặc mượn '
                        '$1\\text{ giờ} = 60\\text{ phút}$).',
                        'Thực hiện được phép cộng, phép trừ hai số đo thời gian (có đổi đơn vị hoặc mượn '
                        '$2\\text{ giờ} = 60\\text{ phút}$).',
                        'Thực hiện được phép cộng, phép trừ hai số đo thời gian (có đổi đơn vị hoặc mượn '
                        '$1\\text{ giờ} = 59\\text{ phút}$).',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 57: Cộng, trừ, nhân, chia số đo thời gian: Thực hiện '
                        'được phép cộng, phép trừ hai số đo thời gian (có đổi đơn vị hoặc mượn $1\\text{ '
                        'giờ} = 60\\text{ phút}$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Kết quả của phép nhân $1\\text{ giờ } 25\\text{ phút} \\times 3$ bằng $4\\text{ giờ } '
                 '15\\text{ phút}$.',
            'answer': True,
            'solution': 'Ta có $1\\text{ giờ } 25\\text{ phút} \\times 3 = 3\\text{ giờ } 75\\text{ phút} = '
                        '4\\text{ giờ } 15\\text{ phút}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 57: Cộng, trừ, nhân, chia số đo thời gian**, quy tắc **Khi tổng >= 60 phút** '
                 'được xác định bởi Cứ $60\\text{ phút}$ đổi thành $1\\text{ giờ}$ và khi áp dụng cho ví dụ '
                 '“Tính: $5\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 40\\text{ phút}$.” ta có lời giải: '
                 'Đổi $5\\text{ giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó $4\\text{ '
                 'giờ } 75\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } 35\\text{ '
                 'phút}$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Khi tổng >= 60 phút** (Cứ $60\\text{ '
                        'phút}$ đổi thành $1\\text{ giờ}$) và lời giải ví dụ minh họa của Bài 57: Cộng, trừ, '
                        'nhân, chia số đo thời gian.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 57: Cộng, trừ, nhân, chia số đo thời gian** để giải '
                 'bài toán sau: Tính: $5\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 40\\text{ phút}$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đổi $5\\text{ giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó '
                        '$4\\text{ giờ } 75\\text{ phút} + 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } '
                        '35\\text{ phút}$...',
                        'Đổi $5\\text{ giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó '
                        '$4\\text{ giờ } 75\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } '
                        '35\\text{ phút}$...',
                        'Đổi $5\\text{ giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó '
                        '$4\\text{ giờ } 75\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } '
                        '34\\text{ phút}$...',
                        'Đổi $10\\text{ giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó '
                        '$4\\text{ giờ } 75\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } '
                        '35\\text{ phút}$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 57: Cộng, trừ, nhân, chia số đo thời gian: Đổi $5\\text{ '
                        'giờ } 15\\text{ phút} = 4\\text{ giờ } 75\\text{ phút}$. Khi đó $4\\text{ giờ } '
                        '75\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} = 2\\text{ giờ } 35\\text{ '
                        'phút}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một người thợ làm $4$ sản phẩm như nhau hết $3\\text{ giờ}$. Hỏi trung bình người thợ đó '
                 'làm $1$ sản phẩm hết bao nhiêu phút?',
            'answer': ['45'],
            'unit': None,
            'solution': 'Đổi $3\\text{ giờ} = 180\\text{ phút}$. Thời gian làm $1$ sản phẩm là $180 : 4 = '
                        '45$ (phút).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd10-thoi-gian-van-toc-chuyen-dong-deu',
  'context_title': 'Chủ đề 10: Số đo thời gian, vận tốc. Các bài toán liên quan đến chuyển động đều',
  'context': 'Chủ đề 10 · SGK Toán 5: Số đo thời gian và các bài toán về vận tốc, quãng đường, thời gian.',
  'title': 'Bài 59: Vận tốc của một chuyển động đều',
  'icon': '🚗',
  'description': 'Khái niệm vận tốc, đơn vị đo vận tốc và công thức tính vận tốc của một chuyển động đều.',
  'requirements': ['Hiểu được ý nghĩa của vận tốc là quãng đường đi được trong một đơn vị thời gian.',
                   'Tính được vận tốc $v = s : t$ với các đơn vị $\\text{km/giờ}, \\text{m/phút}, '
                   '\\text{m/giây}$.',
                   'Vận dụng kiến thức của **Bài 59: Vận tốc của một chuyển động đều** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': '- **Vận tốc** cho biết mức độ nhanh hay chậm của chuyển động, được xác định bằng quãng '
                'đường đi được trong một đơn vị thời gian ($1$ giờ, $1$ phút, $1$ giây).\n'
                '- Muốn tính **vận tốc**, ta lấy quãng đường chia cho thời gian: $v = s : t$.',
  'theory': '### 1. Công thức tính vận tốc\n'
            '- Nếu quãng đường $s$ tính bằng $\\text{km}$, thời gian $t$ tính bằng $\\text{giờ}$ thì vận tốc '
            '$v$ có đơn vị là $\\text{km/giờ}$.\n'
            '- Nếu thời gian cho dưới dạng giờ và phút (ví dụ $1\\text{ giờ } 30\\text{ phút}$), ta phải đổi '
            'ra giờ thập phân ($1{,}5\\text{ giờ}$) trước khi chia.\n'
            '### 2. Đổi đơn vị vận tốc\n'
            '- $1\\text{ km/giờ} = \\dfrac{1000\\text{ m}}{3600\\text{ giây}} = \\dfrac{1}{3{,}6}\\text{ '
            'm/giây}$, do đó $36\\text{ km/giờ} = 10\\text{ m/giây}$ và $54\\text{ km/giờ} = 15\\text{ '
            'm/giây}$.',
  'formulas': [{'category': 'Vận tốc chuyển động đều',
                'items': [{'name': 'Công thức tính vận tốc',
                           'formula': '$v = s : t$ ($s$: quãng đường, $t$: thời gian)'},
                          {'name': 'Đổi km/giờ và m/giây',
                           'formula': '$1\\text{ m/giây} = 3{,}6\\text{ km/giờ}$; $36\\text{ km/giờ} = '
                                      '10\\text{ m/giây}$'}]}],
  'example': 'Một ô tô đi được quãng đường $120\\text{ km}$ trong $1\\text{ giờ } 30\\text{ phút}$. Tính vận '
             'tốc của ô tô theo $\\text{km/giờ}$.',
  'example_answer': 'Đổi $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$. Vận tốc của ô tô là $v = 120 '
                    ': 1{,}5 = 80\\text{ km/giờ}$.',
  'real_life': 'Đọc biển báo tốc độ tối đa trên đường quốc lộ và đồng hồ đo tốc độ trên xe máy, ô tô.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính vận tốc $v$ khi biết quãng đường $s$ và thời gian $t$ là:',
            'options': ['$v = s : t$', '$v = s \\times t$', '$v = t : s$', '$v = s + t$'],
            'answer': 0,
            'solution': 'Muốn tính vận tốc ta lấy quãng đường chia cho thời gian: $v = s : t$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một ô tô đi được $150\\text{ km}$ trong $3\\text{ giờ}$. Vận tốc của ô tô đó là:',
            'options': ['$450\\text{ km/giờ}$',
                        '$50\\text{ km/giờ}$',
                        '$45\\text{ km/giờ}$',
                        '$60\\text{ km/giờ}$'],
            'answer': 1,
            'solution': 'Vận tốc của ô tô là $v = 150 : 3 = 50\\text{ km/giờ}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 59: Vận tốc của một chuyển động đều**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Công thức tính vận tốc**?',
            'options': ['$v = s : t$ ($s$: quãng đường, $t$: thời gian) (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $v = s : t$ ($s$: quãng đường, $t$: thời gian)',
                        '$v = s : t$ ($s$: quãng đường, $t$: thời gian)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $v = s : t$ ($s$: quãng đường, '
                        '$t$: thời gian)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 59: Vận tốc của một chuyển động đều, **Công thức '
                        'tính vận tốc** được xác định bởi: $v = s : t$ ($s$: quãng đường, $t$: thời gian).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 59: Vận tốc của một chuyển động đều**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Đổi km/giờ và m/giây**?',
            'options': ['$2\\text{ m/giây} = 3{,}6\\text{ km/giờ}$; $36\\text{ km/giờ} = 10\\text{ m/giây}$',
                        '$1\\text{ m/giây} = 3{,}6\\text{ km/giờ}$; $36\\text{ km/giờ} = 9\\text{ m/giây}$',
                        '$v = s : t$ ($s$: quãng đường, $t$: thời gian)',
                        '$1\\text{ m/giây} = 3{,}6\\text{ km/giờ}$; $36\\text{ km/giờ} = 10\\text{ m/giây}$'],
            'answer': 3,
            'solution': 'Trong Bài 59: Vận tốc của một chuyển động đều, **Đổi km/giờ và m/giây** có công '
                        'thức/quy tắc là: $1\\text{ m/giây} = 3{,}6\\text{ km/giờ}$; $36\\text{ km/giờ} = '
                        '10\\text{ m/giây}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một vận động viên chạy $400\\text{ m}$ hết $1\\text{ phút } 20\\text{ giây}$. Vận tốc chạy '
                 'tính theo $\\text{m/giây}$ là:',
            'options': ['$5\\text{ m/giây}$',
                        '$4\\text{ m/giây}$',
                        '$6\\text{ m/giây}$',
                        '$8\\text{ m/giây}$'],
            'answer': 0,
            'solution': 'Đổi $1\\text{ phút } 20\\text{ giây} = 80\\text{ giây}$. Vận tốc là $400 : 80 = '
                        '5\\text{ m/giây}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 59: Vận tốc của một chuyển động đều**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Hiểu được ý nghĩa của vận tốc là quãng đường đi được trong một đơn vị thời gian. '
                        '(với dấu ngược lại)',
                        'Hiểu được ý nghĩa của vận tốc là quãng đường đi được trong một đơn vị thời gian.',
                        'Đảo ngược vế của quy tắc: Hiểu được ý nghĩa của vận tốc là quãng đường đi được '
                        'trong một đơn vị thời gian.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu được ý nghĩa của vận tốc '
                        'là quãng đường đi được trong một đơn vị thời gian.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 59: Vận tốc của một chuyển động đều: Hiểu được ý '
                        'nghĩa của vận tốc là quãng đường đi được trong một đơn vị thời gian.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Vận tốc $54\\text{ km/giờ}$ bằng vận tốc $15\\text{ m/giây}$.',
            'answer': True,
            'solution': 'Đổi $54\\text{ km} = 54\\,000\\text{ m}$ và $1\\text{ giờ} = 3600\\text{ giây}$, ta '
                        'có $54\\,000 : 3600 = 15\\text{ m/giây}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 59: Vận tốc của một chuyển động đều**, quy tắc **Công thức tính vận tốc** được '
                 'xác định bởi $v = s : t$ ($s$: quãng đường, $t$: thời gian) và khi áp dụng cho ví dụ “Một '
                 'ô tô đi được quãng đường $120\\text{ km}$ trong $1\\text{ giờ } 30\\text{ phút}$. Tính vận '
                 'tốc của ô tô theo $\\text{km/giờ}$.” ta có lời giải: Đổi $1\\text{ giờ } 30\\text{ phút} = '
                 '1{,}5\\text{ giờ}$. Vận tốc của ô tô là $v = 120 : 1{,}5 = 80\\text{ km/giờ}$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Công thức tính vận tốc** ($v = s : t$ '
                        '($s$: quãng đường, $t$: thời gian)) và lời giải ví dụ minh họa của Bài 59: Vận tốc '
                        'của một chuyển động đều.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 59: Vận tốc của một chuyển động đều** để giải bài '
                 'toán sau: Một ô tô đi được quãng đường $120\\text{ km}$ trong $1\\text{ giờ } 30\\text{ '
                 'phút}$. Tính vận tốc của ô tô theo $\\text{km/giờ}$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Đổi $2\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$. Vận tốc của ô tô là $v = '
                        '120 : 1{,}5 = 80\\text{ km/giờ}$.',
                        'Đổi $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$. Vận tốc của ô tô là $v = '
                        '120 : 1{,}5 = 79\\text{ km/giờ}$.',
                        'Đổi $1\\text{ giờ } 30\\text{ phút} = 1{,}5\\text{ giờ}$. Vận tốc của ô tô là $v = '
                        '120 : 1{,}5 = 80\\text{ km/giờ}$.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 59: Vận tốc của một chuyển động đều: Đổi $1\\text{ giờ } '
                        '30\\text{ phút} = 1{,}5\\text{ giờ}$. Vận tốc của ô tô là $v = 120 : 1{,}5 = '
                        '80\\text{ km/giờ}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một xe máy đi quãng đường dài $90\\text{ km}$ hết $2\\text{ giờ } 15\\text{ phút}$. Tính '
                 'vận tốc của xe máy đó theo đơn vị km/giờ.',
            'answer': ['40'],
            'unit': None,
            'solution': 'Đổi $2\\text{ giờ } 15\\text{ phút} = 2{,}25\\text{ giờ}$. Vận tốc của xe máy là '
                        '$90 : 2{,}25 = 40$ ($\\text{km/giờ}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd10-thoi-gian-van-toc-chuyen-dong-deu',
  'context_title': 'Chủ đề 10: Số đo thời gian, vận tốc. Các bài toán liên quan đến chuyển động đều',
  'context': 'Chủ đề 10 · SGK Toán 5: Số đo thời gian và các bài toán về vận tốc, quãng đường, thời gian.',
  'title': 'Bài 60: Quãng đường, thời gian của một chuyển động đều',
  'icon': '🚗',
  'description': 'Công thức tính quãng đường, thời gian và giải các bài toán chuyển động đều trong thực '
                 'tiễn.',
  'requirements': ['Tính được quãng đường $s = v \\times t$ và thời gian $t = s : v$ trong chuyển động đều.',
                   'Giải được bài toán tìm thời điểm xuất phát, thời điểm đến nơi và hai xe chuyển động '
                   'ngược chiều gặp nhau.',
                   'Vận dụng kiến thức của **Bài 60: Quãng đường, thời gian của một chuyển động đều** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Muốn tính **quãng đường**, ta lấy vận tốc nhân với thời gian: $s = v \\times t$.\n'
                '- Muốn tính **thời gian**, ta lấy quãng đường chia cho vận tốc: $t = s : v$ (trong đó $s, '
                'v, t$ phải cùng hệ đơn vị đo).',
  'theory': '### 1. Tìm thời điểm đến nơi và khởi hành\n'
            '- $\\text{Thời điểm đến nơi} = \\text{Thời điểm khởi hành} + \\text{Thời gian đi} + \\text{Thời '
            'gian nghỉ (nếu có)}$.\n'
            '### 2. Hai vật chuyển động ngược chiều gặp nhau\n'
            '- Khi hai xe xuất phát cùng lúc từ hai đầu quãng đường $s$ và đi ngược chiều nhau với vận tốc '
            '$v_1, v_2$ thì thời gian để hai xe gặp nhau là $t = \\dfrac{s}{v_1 + v_2}$.',
  'formulas': [{'category': 'Công thức quãng đường và thời gian',
                'items': [{'name': 'Quãng đường', 'formula': '$s = v \\times t$'},
                          {'name': 'Thời gian', 'formula': '$t = s : v$'},
                          {'name': 'Hai xe đi ngược chiều gặp nhau',
                           'formula': '$t_{\\text{gặp}} = \\dfrac{s}{v_1 + v_2}$'}]}],
  'example': 'Một xe máy khởi hành lúc $7\\text{ giờ } 15\\text{ phút}$ với vận tốc $40\\text{ km/giờ}$ trên '
             'quãng đường $90\\text{ km}$. Hỏi xe đến nơi lúc mấy giờ?',
  'example_answer': 'Thời gian đi là $t = 90 : 40 = 2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ phút}$. Xe '
                    'đến nơi lúc $7\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 15\\text{ phút} = 9\\text{ '
                    'giờ } 30\\text{ phút}$.',
  'real_life': 'Lập kế hoạch thời gian khởi hành để kịp giờ bay hoặc giờ vào học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính thời gian $t$ khi biết quãng đường $s$ và vận tốc $v$ là:',
            'options': ['$t = s \\times v$', '$t = s : v$', '$t = v : s$', '$t = s - v$'],
            'answer': 1,
            'solution': 'Muốn tính thời gian ta lấy quãng đường chia cho vận tốc: $t = s : v$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một người đi bộ với vận tốc $5\\text{ km/giờ}$ trong $2{,}5\\text{ giờ}$. Quãng đường '
                 'người đó đi được là:',
            'options': ['$2\\text{ km}$', '$7{,}5\\text{ km}$', '$12{,}5\\text{ km}$', '$10\\text{ km}$'],
            'answer': 2,
            'solution': 'Quãng đường đi được là $s = 5 \\times 2{,}5 = 12{,}5\\text{ km}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 60: Quãng đường, thời gian của một chuyển động đều**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Quãng đường**?',
            'options': ['$s = v : t$',
                        'Đảo ngược vế của quy tắc: $s = v \\times t$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $s = v \\times t$',
                        '$s = v \\times t$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 60: Quãng đường, thời gian của một chuyển động '
                        'đều, **Quãng đường** được xác định bởi: $s = v \\times t$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 60: Quãng đường, thời gian của một chuyển động đều**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Thời gian**?',
            'options': ['$t = s : v$',
                        '$t = s : v$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $t = s : v$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $t = s : v$'],
            'answer': 0,
            'solution': 'Trong Bài 60: Quãng đường, thời gian của một chuyển động đều, **Thời gian** có công '
                        'thức/quy tắc là: $t = s : v$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một ca nô đi với vận tốc $24\\text{ km/giờ}$ trên quãng đường dài $30\\text{ km}$. Thời '
                 'gian đi của ca nô là:',
            'options': ['$1\\text{ giờ } 25\\text{ phút}$',
                        '$1\\text{ giờ } 15\\text{ phút}$',
                        '$1\\text{ giờ } 10\\text{ phút}$',
                        '$50\\text{ phút}$'],
            'answer': 1,
            'solution': 'Thời gian đi là $t = 30 : 24 = 1{,}25\\text{ giờ} = 1\\text{ giờ } 15\\text{ '
                        'phút}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 60: Quãng đường, thời gian của một chuyển động đều**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Tính được quãng đường $s = v : t$ và thời gian $t = s : v$ trong chuyển động đều.',
                        'Đảo ngược vế của quy tắc: Tính được quãng đường $s = v \\times t$ và thời gian $t = '
                        's : v$ trong chuyển động đều.',
                        'Tính được quãng đường $s = v \\times t$ và thời gian $t = s : v$ trong chuyển động '
                        'đều.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được quãng đường $s = v '
                        '\\times t$ và thời gian $t = s : v$ trong chuyển động đều.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 60: Quãng đường, thời gian của một chuyển động đều: '
                        'Tính được quãng đường $s = v \\times t$ và thời gian $t = s : v$ trong chuyển động '
                        'đều.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ô tô đi với vận tốc $60\\text{ km/giờ}$ trong $45\\text{ phút}$ thì đi được quãng đường '
                 '$45\\text{ km}$.',
            'answer': True,
            'solution': 'Đổi $45\\text{ phút} = 0{,}75\\text{ giờ}$, quãng đường đi được là $60 \\times '
                        '0{,}75 = 45\\text{ km}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 60: Quãng đường, thời gian của một chuyển động đều**, quy tắc **Quãng đường** '
                 'được xác định bởi $s = v \\times t$ và khi áp dụng cho ví dụ “Một xe máy khởi hành lúc '
                 '$7\\text{ giờ } 15\\text{ phút}$ với vận tốc $40\\text{ km/giờ}$ trên quãng đường '
                 '$90\\text{ km}$. Hỏi xe đến nơi...” ta có lời giải: Thời gian đi là $t = 90 : 40 = '
                 '2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ phút}$. Xe đến nơi lúc $7\\text{ giờ } '
                 '15\\text{ phút} + 2\\text{ giờ } 15\\text{ phút} = 9\\text{ giờ } 30\\text{ phút}$.... '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quãng đường** ($s = v \\times t$) và lời '
                        'giải ví dụ minh họa của Bài 60: Quãng đường, thời gian của một chuyển động đều.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 60: Quãng đường, thời gian của một chuyển động '
                 'đều** để giải bài toán sau: Một xe máy khởi hành lúc $7\\text{ giờ } 15\\text{ phút}$ với '
                 'vận tốc $40\\text{ km/giờ}$ trên quãng đường $90\\text{ km}$. Hỏi xe đến nơi lúc mấy giờ? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Thời gian đi là $t = 90 : 40 = 2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ '
                        'phút}$. Xe đến nơi lúc $7\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 15\\text{ '
                        'phút} = 9\\text{ giờ } 30\\text{ phút}$...',
                        'Thời gian đi là $t = 90 : 40 = 2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ '
                        'phút}$. Xe đến nơi lúc $7\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 15\\text{ '
                        'phút} = 9\\text{ giờ } 29\\text{ phút}$...',
                        'Thời gian đi là $t = 92 : 40 = 2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ '
                        'phút}$. Xe đến nơi lúc $7\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 15\\text{ '
                        'phút} = 9\\text{ giờ } 30\\text{ phút}$...',
                        'Thời gian đi là $t = 90 : 40 = 2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ '
                        'phút}$. Xe đến nơi lúc $7\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 15\\text{ '
                        'phút} = 9\\text{ giờ } 30\\text{ phút}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 60: Quãng đường, thời gian của một chuyển động đều: Thời '
                        'gian đi là $t = 90 : 40 = 2{,}25\\text{ giờ} = 2\\text{ giờ } 15\\text{ phút}$. Xe '
                        'đến nơi lúc $7\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 15\\text{ phút} = '
                        '9\\text{ giờ } 30\\text{ phút}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai ô tô khởi hành cùng một lúc từ hai địa điểm A và B cách nhau $180\\text{ km}$, đi '
                 'ngược chiều nhau với vận tốc $40\\text{ km/giờ}$ và $50\\text{ km/giờ}$. Hỏi sau bao nhiêu '
                 'giờ hai xe gặp nhau?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Mỗi giờ hai xe gần nhau được $40 + 50 = 90\\text{ km}$. Thời gian hai xe gặp nhau '
                        'là $180 : 90 = 2$ (giờ).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd11-thong-ke-xac-suat',
  'context_title': 'Chủ đề 11: Một số yếu tố thống kê và xác suất',
  'context': 'Chủ đề 11 · SGK Toán 5: Thu thập số liệu, biểu đồ hình quạt tròn và tỉ số lặp lại của sự kiện.',
  'title': 'Bài 63: Thu thập, phân loại, sắp xếp các số liệu',
  'icon': '📊',
  'description': 'Cách thu thập, kiểm đếm, phân loại và sắp xếp số liệu vào bảng thống kê hoặc biểu đồ cột.',
  'requirements': ['Thu thập, phân loại và sắp xếp được các số liệu thống kê theo tiêu chí cho trước.',
                   'Đọc, phân tích và rút ra nhận xét từ bảng số liệu thống kê.',
                   'Vận dụng kiến thức của **Bài 63: Thu thập, phân loại, sắp xếp các số liệu** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Thu thập số liệu** có thể thực hiện bằng cách quan sát, phỏng vấn, kiểm đếm hoặc tra '
                'cứu thông tin.\n'
                '- **Phân loại và sắp xếp số liệu** theo các tiêu chí giúp ta lập được bảng số liệu rõ ràng, '
                'dễ so sánh.',
  'theory': '### 1. Kiểm đếm và lập bảng số liệu\n'
            '- Mỗi đối tượng được phân vào một nhóm xác định; tổng số lượng các nhóm bằng tổng số đối tượng '
            'được khảo sát.\n'
            '### 2. Phân tích số liệu\n'
            '- Tìm giá trị lớn nhất, giá trị bé nhất, hiệu giữa hai nhóm và trung bình cộng của các số liệu.',
  'formulas': [{'category': 'Xử lí bảng số liệu',
                'items': [{'name': 'Tổng số liệu', 'formula': '$N = n_1 + n_2 + \\dots + n_k$'},
                          {'name': 'Số trung bình cộng',
                           'formula': '$\\text{TBC} = \\dfrac{n_1 + n_2 + \\dots + n_k}{k}$'}]}],
  'example': 'Khảo sát môn thể thao yêu thích của tổ 1: Bóng đá $5$ bạn, Cầu lông $4$ bạn, Bơi lội $3$ bạn '
             '(mỗi bạn chọn $1$ môn). Tổ 1 có bao nhiêu bạn?',
  'example_answer': 'Tổng số học sinh của tổ 1 là $5 + 4 + 3 = 12$ (bạn).',
  'real_life': 'Thống kê kết quả học tập của lớp, số quyển sách quyên góp của từng tổ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi kiểm đếm số liệu bằng các vạch, mỗi bó gồm $4$ vạch dọc và $1$ vạch chéo biểu thị số '
                 'lượng là:',
            'options': ['$4$', '$6$', '$5$', '$10$'],
            'answer': 2,
            'solution': 'Mỗi bó gồm $4$ vạch dọc và $1$ vạch gạch chéo biểu thị $5$ đơn vị.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bảng thống kê số cây trồng của $3$ lớp: 5A trồng $25$ cây, 5B trồng $30$ cây, 5C trồng '
                 '$20$ cây. Lớp trồng nhiều cây nhất là:',
            'options': ['Lớp 5A', 'Lớp 5C', 'Ba lớp bằng nhau', 'Lớp 5B'],
            'answer': 3,
            'solution': 'Vì $30 > 25 > 20$ nên lớp 5B trồng nhiều cây nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 63: Thu thập, phân loại, sắp xếp các số liệu**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Tổng số liệu**?',
            'options': ['$N = n_1 + n_2 + \\dots + n_k$',
                        '$N = n_1 - n_2 + \\dots + n_k$',
                        'Đảo ngược vế của quy tắc: $N = n_1 + n_2 + \\dots + n_k$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $N = n_1 + n_2 + \\dots + n_k$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 63: Thu thập, phân loại, sắp xếp các số liệu, '
                        '**Tổng số liệu** được xác định bởi: $N = n_1 + n_2 + \\dots + n_k$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 63: Thu thập, phân loại, sắp xếp các số liệu**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Số trung bình cộng**?',
            'options': ['$\\text{TBC} = \\dfrac{n_1 - n_2 + \\dots + n_k}{k}$',
                        '$\\text{TBC} = \\dfrac{n_1 + n_2 + \\dots + n_k}{k}$',
                        '$\\text{TBC} = \\dfrac{k}{n_1 + n_2 + \\dots + n_k}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{TBC} = \\dfrac{n_1 + '
                        'n_2 + \\dots + n_k}{k}$'],
            'answer': 1,
            'solution': 'Trong Bài 63: Thu thập, phân loại, sắp xếp các số liệu, **Số trung bình cộng** có '
                        'công thức/quy tắc là: $\\text{TBC} = \\dfrac{n_1 + n_2 + \\dots + n_k}{k}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trung bình mỗi lớp trong $3$ lớp 5A ($25$ cây), 5B ($30$ cây), 5C ($20$ cây) trồng được '
                 'bao nhiêu cây?',
            'options': ['$24$ cây', '$26$ cây', '$25$ cây', '$75$ cây'],
            'answer': 2,
            'solution': 'Trung bình mỗi lớp trồng được $(25 + 30 + 20) : 3 = 25$ (cây).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 63: Thu thập, phân loại, sắp xếp các số liệu**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Thu thập, phân loại và sắp xếp được các số liệu thống kê theo tiêu chí cho trước. '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thu thập, phân loại và sắp xếp được các số liệu thống kê '
                        'theo tiêu chí cho trước.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thu thập, phân loại và sắp xếp '
                        'được các số liệu thống kê theo tiêu chí cho trước.',
                        'Thu thập, phân loại và sắp xếp được các số liệu thống kê theo tiêu chí cho trước.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 63: Thu thập, phân loại, sắp xếp các số liệu: Thu '
                        'thập, phân loại và sắp xếp được các số liệu thống kê theo tiêu chí cho trước.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Sắp xếp dãy số liệu $18; 25; 12; 30$ theo thứ tự từ bé đến lớn ta được $12; 18; 25; 30$.',
            'answer': True,
            'solution': 'Vì $12 < 18 < 25 < 30$ nên thứ tự từ bé đến lớn là $12; 18; 25; 30$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 63: Thu thập, phân loại, sắp xếp các số liệu**, quy tắc **Tổng số liệu** được '
                 'xác định bởi $N = n_1 + n_2 + \\dots + n_k$ và khi áp dụng cho ví dụ “Khảo sát môn thể '
                 'thao yêu thích của tổ 1: Bóng đá $5$ bạn, Cầu lông $4$ bạn, Bơi lội $3$ bạn (mỗi bạn chọn '
                 '$1$ môn). Tổ 1 có bao nhiêu...” ta có lời giải: Tổng số học sinh của tổ 1 là $5 + 4 + 3 = '
                 '12$ (bạn).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tổng số liệu** ($N = n_1 + n_2 + \\dots '
                        '+ n_k$) và lời giải ví dụ minh họa của Bài 63: Thu thập, phân loại, sắp xếp các số '
                        'liệu.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 63: Thu thập, phân loại, sắp xếp các số liệu** để '
                 'giải bài toán sau: Khảo sát môn thể thao yêu thích của tổ 1: Bóng đá $5$ bạn, Cầu lông $4$ '
                 'bạn, Bơi lội $3$ bạn (mỗi bạn chọn $1$ môn). Tổ 1 có bao nhiêu bạn? Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Tổng số học sinh của tổ 1 là $5 + 4 + 3 = 12$ (bạn).',
                        'Tổng số học sinh của tổ 1 là $5 - 4 + 3 = 12$ (bạn).',
                        'Tổng số học sinh của tổ 1 là $5 + 4 + 3 = 11$ (bạn).',
                        'Tổng số học sinh của tổ 2 là $5 + 4 + 3 = 12$ (bạn).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 63: Thu thập, phân loại, sắp xếp các số liệu: Tổng số '
                        'học sinh của tổ 1 là $5 + 4 + 3 = 12$ (bạn).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Khảo sát $40$ học sinh về loại quả yêu thích (mỗi bạn chọn $1$ loại) gồm Cam, Táo, Xoài. '
                 'Biết có $14$ bạn thích Cam và $16$ bạn thích Táo. Hỏi có bao nhiêu bạn thích Xoài?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Số bạn thích Xoài là $40 - 14 - 16 = 10$ (bạn).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd11-thong-ke-xac-suat',
  'context_title': 'Chủ đề 11: Một số yếu tố thống kê và xác suất',
  'context': 'Chủ đề 11 · SGK Toán 5: Thu thập số liệu, biểu đồ hình quạt tròn và tỉ số lặp lại của sự kiện.',
  'title': 'Bài 64: Biểu đồ hình quạt tròn',
  'icon': '📊',
  'description': 'Đọc, mô tả và tính toán số liệu trên biểu đồ hình quạt tròn có ghi tỉ số phần trăm.',
  'requirements': ['Hiểu được cả hình tròn biểu diễn $100\\%$ tổng số liệu và mỗi hình quạt biểu diễn tỉ lệ '
                   'phần trăm của một thành phần.',
                   'Tính được số lượng cụ thể của từng thành phần từ biểu đồ hình quạt tròn.',
                   'Vận dụng kiến thức của **Bài 64: Biểu đồ hình quạt tròn** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- Trong **biểu đồ hình quạt tròn**, toàn bộ hình tròn biểu diễn **$100\\%$** tổng các số '
                'liệu.\n'
                '- Hình quạt占 một nửa hình tròn ứng với $50\\%$; hình quạt góc vuông ($\\dfrac{1}{4}$ hình '
                'tròn) ứng với $25\\%$.\n'
                '- Số lượng của một nhóm chiếm $m\\%$ trong tổng số $N$ là: $N \\times m : 100$.',
  'theory': '### 1. Tìm phần trăm còn thiếu trên biểu đồ\n'
            '- Lấy $100\\%$ trừ đi tổng phần trăm của các hình quạt đã biết.\n'
            '### 2. Tính số lượng của mỗi nhóm\n'
            '- Ví dụ: lớp có $40$ bạn, hình quạt môn Bóng đá chiếm $25\\%$ thì số bạn thích Bóng đá là $40 '
            '\\times 25 : 100 = 10$ (bạn).',
  'formulas': [{'category': 'Công thức biểu đồ hình quạt tròn',
                'items': [{'name': 'Tổng các hình quạt',
                           'formula': '$p_1\\% + p_2\\% + \\dots + p_k\\% = 100\\%$'},
                          {'name': 'Giá trị của nhóm chiếm m%',
                           'formula': '$\\text{Giá trị} = \\text{Tổng số} \\times m : 100$'}]}],
  'example': 'Biểu đồ hình quạt cho biết trong $200$ học sinh có $45\\%$ thích đọc truyện, $30\\%$ thích thể '
             'thao, còn lại thích âm nhạc. Tính số học sinh thích âm nhạc.',
  'example_answer': 'Tỉ số phần trăm học sinh thích âm nhạc là $100\\% - 45\\% - 30\\% = 25\\%$. Số học sinh '
                    'thích âm nhạc là $200 \\times 25 : 100 = 50$ (học sinh).',
  'real_life': 'Đọc biểu đồ cơ cấu chi tiêu hàng tháng của gia đình hoặc cơ cấu diện tích các loại cây '
               'trồng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong biểu đồ hình quạt tròn, cả hình tròn biểu diễn bao nhiêu phần trăm?',
            'options': ['$50\\%$', '$360\\%$', '$10\\%$', '$100\\%$'],
            'answer': 3,
            'solution': 'Toàn bộ hình tròn biểu diễn $100\\%$ tổng số liệu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu đồ sở thích trái cây của lớp gồm: Táo $40\\%$, Cam $35\\%$, còn lại là Xoài. Tỉ số '
                 'phần trăm của Xoài là:',
            'options': ['$25\\%$', '$75\\%$', '$35\\%$', '$15\\%$'],
            'answer': 0,
            'solution': 'Ta có $100\\% - 40\\% - 35\\% = 25\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 64: Biểu đồ hình quạt tròn**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Tổng các hình quạt**?',
            'options': ['$p_1\\% - p_2\\% + \\dots + p_k\\% = 100\\%$',
                        '$p_1\\% + p_2\\% + \\dots + p_k\\% = 100\\%$',
                        '$p_1\\% + p_2\\% + \\dots + p_k\\% = 99\\%$',
                        '$p_1\\% + p_2\\% + \\dots + p_k\\% = 102\\%$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 64: Biểu đồ hình quạt tròn, **Tổng các hình quạt** '
                        'được xác định bởi: $p_1\\% + p_2\\% + \\dots + p_k\\% = 100\\%$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 64: Biểu đồ hình quạt tròn**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Giá trị của nhóm chiếm m%**?',
            'options': ['$\\text{Giá trị} = \\text{Tổng số} : m : 100$',
                        '$\\text{Giá trị} = \\text{Tổng số} \\times m : 99$',
                        '$\\text{Giá trị} = \\text{Tổng số} \\times m : 100$',
                        '$\\text{Giá trị} = \\text{Tổng số} \\times m : 102$'],
            'answer': 2,
            'solution': 'Trong Bài 64: Biểu đồ hình quạt tròn, **Giá trị của nhóm chiếm m%** có công '
                        'thức/quy tắc là: $\\text{Giá trị} = \\text{Tổng số} \\times m : 100$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một lớp có $40$ học sinh, biểu đồ hình quạt cho biết $30\\%$ học sinh đi học bằng xe đạp. '
                 'Số học sinh đi xe đạp là:',
            'options': ['$30$ học sinh', '$15$ học sinh', '$10$ học sinh', '$12$ học sinh'],
            'answer': 3,
            'solution': 'Số học sinh đi xe đạp là $40 \\times 30 : 100 = 12$ (học sinh).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 64: Biểu đồ hình quạt tròn**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Hiểu được cả hình tròn biểu diễn $100\\%$ tổng số liệu và mỗi hình quạt biểu diễn '
                        'tỉ lệ phần trăm của một thành phần.',
                        'Hiểu được cả hình tròn biểu diễn $110\\%$ tổng số liệu và mỗi hình quạt biểu diễn '
                        'tỉ lệ phần trăm của một thành phần.',
                        'Hiểu được cả hình tròn biểu diễn $99\\%$ tổng số liệu và mỗi hình quạt biểu diễn tỉ '
                        'lệ phần trăm của một thành phần.',
                        'Hiểu được cả hình tròn biểu diễn $102\\%$ tổng số liệu và mỗi hình quạt biểu diễn '
                        'tỉ lệ phần trăm của một thành phần.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 64: Biểu đồ hình quạt tròn: Hiểu được cả hình tròn '
                        'biểu diễn $100\\%$ tổng số liệu và mỗi hình quạt biểu diễn tỉ lệ phần trăm của một '
                        'thành phần.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong biểu đồ hình quạt tròn, hình quạt chiếm một nửa hình tròn biểu diễn tỉ lệ $50\\%$.',
            'answer': True,
            'solution': 'Một nửa hình tròn bằng $\\dfrac{1}{2} \\times 100\\% = 50\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 64: Biểu đồ hình quạt tròn**, quy tắc **Tổng các hình quạt** được xác định bởi '
                 '$p_1\\% + p_2\\% + \\dots + p_k\\% = 100\\%$ và khi áp dụng cho ví dụ “Biểu đồ hình quạt '
                 'cho biết trong $200$ học sinh có $45\\%$ thích đọc truyện, $30\\%$ thích thể thao, còn lại '
                 'thích âm nhạc. Tính số học s...” ta có lời giải: Tỉ số phần trăm học sinh thích âm nhạc là '
                 '$100\\% - 45\\% - 30\\% = 25\\%$. Số học sinh thích âm nhạc là $200 \\times 25 : 100 = 50$ '
                 '(học si.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tổng các hình quạt** ($p_1\\% + p_2\\% + '
                        '\\dots + p_k\\% = 100\\%$) và lời giải ví dụ minh họa của Bài 64: Biểu đồ hình quạt '
                        'tròn.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 64: Biểu đồ hình quạt tròn** để giải bài toán sau: '
                 'Biểu đồ hình quạt cho biết trong $200$ học sinh có $45\\%$ thích đọc truyện, $30\\%$ thích '
                 'thể thao, còn lại thích âm nhạc. Tính số học sinh thích âm nhạc. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Tỉ số phần trăm học sinh thích âm nhạc là $100\\% + 45\\% - 30\\% = 25\\%$. Số học '
                        'sinh thích âm nhạc là $200 \\times 25 : 100 = 50$ (học sinh).',
                        'Tỉ số phần trăm học sinh thích âm nhạc là $100\\% - 45\\% - 30\\% = 25\\%$. Số học '
                        'sinh thích âm nhạc là $200 \\times 25 : 100 = 50$ (học sinh).',
                        'Tỉ số phần trăm học sinh thích âm nhạc là $100\\% - 45\\% - 30\\% = 25\\%$. Số học '
                        'sinh thích âm nhạc là $200 \\times 25 : 100 = 49$ (học sinh).',
                        'Tỉ số phần trăm học sinh thích âm nhạc là $102\\% - 45\\% - 30\\% = 25\\%$. Số học '
                        'sinh thích âm nhạc là $200 \\times 25 : 100 = 50$ (học sinh).'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 64: Biểu đồ hình quạt tròn: Tỉ số phần trăm học sinh '
                        'thích âm nhạc là $100\\% - 45\\% - 30\\% = 25\\%$. Số học sinh thích âm nhạc là '
                        '$200 \\times 25 : 100 = 50$ (học sinh).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Gia đình bác Lan có thu nhập $15$ triệu đồng/tháng, trong đó chi ăn uống $40\\%$, học tập '
                 '$20\\%$, tiết kiệm $15\\%$, còn lại là chi tiêu khác. Tính số tiền chi tiêu khác theo đơn '
                 'vị triệu đồng.',
            'answer': ['3,75', '3.75'],
            'unit': None,
            'solution': 'Phần trăm chi tiêu khác là $100\\% - 40\\% - 20\\% - 15\\% = 25\\%$. Số tiền là $15 '
                        '\\times 25 : 100 = 3{,}75$ (triệu đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd11-thong-ke-xac-suat',
  'context_title': 'Chủ đề 11: Một số yếu tố thống kê và xác suất',
  'context': 'Chủ đề 11 · SGK Toán 5: Thu thập số liệu, biểu đồ hình quạt tròn và tỉ số lặp lại của sự kiện.',
  'title': 'Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện',
  'icon': '📊',
  'description': 'Sử dụng tỉ số và tỉ số phần trăm để mô tả số lần lặp lại của một sự kiện trong trò chơi, '
                 'thí nghiệm.',
  'requirements': ['Viết được tỉ số $\\dfrac{k}{n}$ giữa số lần sự kiện xảy ra ($k$) và tổng số lần thực '
                   'hiện ($n$).',
                   'Đổi được tỉ số lặp lại của một sự kiện sang tỉ số phần trăm.',
                   'Vận dụng kiến thức của **Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần '
                   'thực hiện** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Khi thực hiện một hoạt động hoặc phép thử $n$ lần mà sự kiện $A$ xảy ra $k$ lần thì **tỉ '
                'số của số lần lặp lại sự kiện $A$ so với tổng số lần thực hiện** là $\\dfrac{k}{n}$.',
  'theory': '### 1. Cách viết tỉ số lặp lại\n'
            '- Tử số là số lần sự kiện đó xảy ra ($k$); mẫu số là **tổng số lần thực hiện** ($n$), không '
            'phải số lần sự kiện không xảy ra.\n'
            '- Ví dụ: tung đồng xu $50$ lần, mặt ngửa xuất hiện $23$ lần thì tỉ số là $\\dfrac{23}{50} = '
            '46\\%$.',
  'formulas': [{'category': 'Tỉ số lặp lại của sự kiện',
                'items': [{'name': 'Dạng phân số',
                           'formula': '$\\text{Tỉ số} = \\dfrac{k}{n}$ ($k$: số lần sự kiện xảy ra; $n$: '
                                      'tổng số lần thực hiện)'},
                          {'name': 'Dạng phần trăm', 'formula': '$(k : n) \\times 100\\%$'}]}],
  'example': 'Gieo một con xúc xắc $50$ lần, mặt $6$ chấm xuất hiện $8$ lần. Viết tỉ số và tỉ số phần trăm '
             'số lần xuất hiện mặt $6$ chấm so với tổng số lần gieo.',
  'example_answer': 'Tỉ số là $\\dfrac{8}{50} = \\dfrac{4}{25}$. Đổi sang tỉ số phần trăm: $\\dfrac{8}{50} = '
                    '\\dfrac{16}{100} = 16\\%$.',
  'real_life': 'Tính tỉ lệ sút bóng trúng khung thành của cầu thủ hoặc tỉ lệ hạt giống nảy mầm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tung một đồng xu $20$ lần, mặt ngửa xuất hiện $9$ lần. Tỉ số của số lần xuất hiện mặt ngửa '
                 'và tổng số lần tung là:',
            'options': ['$\\dfrac{9}{20}$', '$\\dfrac{11}{20}$', '$\\dfrac{20}{9}$', '$\\dfrac{9}{11}$'],
            'answer': 0,
            'solution': 'Tỉ số là $\\dfrac{k}{n} = \\dfrac{9}{20}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Gieo xúc xắc $50$ lần, mặt $6$ chấm xuất hiện $8$ lần. Tỉ số phần trăm số lần xuất hiện '
                 'mặt $6$ chấm là:',
            'options': ['$8\\%$', '$16\\%$', '$6\\%$', '$42\\%$'],
            'answer': 1,
            'solution': 'Ta có $8 : 50 = 0{,}16 = 16\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện**, quy '
                 'tắc hoặc công thức nào sau đây xác định đúng **Dạng phân số**?',
            'options': ['$\\text{Tỉ số} = \\dfrac{k}{n}$ ($k$: số lần sự kiện xảy ra; $n$: tổng số lần thực '
                        'hiện) (với dấu ngược lại)',
                        '$\\text{Tỉ số} = \\dfrac{n}{k}$ ($k$: số lần sự kiện xảy ra; $n$: tổng số lần thực '
                        'hiện)',
                        '$\\text{Tỉ số} = \\dfrac{k}{n}$ ($k$: số lần sự kiện xảy ra; $n$: tổng số lần thực '
                        'hiện)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Tỉ số} = \\dfrac{k}{n}$ '
                        '($k$: số lần sự kiện xảy ra; $n$: tổng số lần thực hiện)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 65: Tỉ số của số lần lặp lại một sự kiện so với '
                        'tổng số lần thực hiện, **Dạng phân số** được xác định bởi: $\\text{Tỉ số} = '
                        '\\dfrac{k}{n}$ ($k$: số lần sự kiện xảy ra; $n$: tổng số lần thực hiện).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Dạng phần trăm**?',
            'options': ['$(k : n) : 100\\%$',
                        '$(k : n) \\times 99\\%$',
                        '$(k : n) \\times 102\\%$',
                        '$(k : n) \\times 100\\%$'],
            'answer': 3,
            'solution': 'Trong Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện, '
                        '**Dạng phần trăm** có công thức/quy tắc là: $(k : n) \\times 100\\%$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong hộp có bóng xanh và bóng đỏ. Nam lấy bóng $30$ lần (mỗi lần lấy $1$ quả rồi trả '
                 'lại), thấy có $12$ lần lấy được bóng đỏ. Tỉ số số lần lấy được bóng xanh so với tổng số '
                 'lần lấy là:',
            'options': ['$\\dfrac{18}{30}$', '$\\dfrac{12}{30}$', '$\\dfrac{12}{18}$', '$\\dfrac{18}{12}$'],
            'answer': 0,
            'solution': 'Số lần lấy được bóng xanh là $30 - 12 = 18$ (lần), tỉ số là $\\dfrac{18}{30}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần '
                 'thực hiện**, nhận định nào sau đây là **chính xác**?',
            'options': ['Viết được tỉ số $\\dfrac{k}{n}$ giữa số lần sự kiện xảy ra ($k$) và tổng số lần '
                        'thực hiện ($n$). (với dấu ngược lại)',
                        'Viết được tỉ số $\\dfrac{k}{n}$ giữa số lần sự kiện xảy ra ($k$) và tổng số lần '
                        'thực hiện ($n$).',
                        'Viết được tỉ số $\\dfrac{n}{k}$ giữa số lần sự kiện xảy ra ($k$) và tổng số lần '
                        'thực hiện ($n$).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Viết được tỉ số $\\dfrac{k}{n}$ '
                        'giữa số lần sự kiện xảy ra ($k$) và tổng số lần thực hiện ($n$).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng '
                        'số lần thực hiện: Viết được tỉ số $\\dfrac{k}{n}$ giữa số lần sự kiện xảy ra ($k$) '
                        'và tổng số lần thực hiện ($n$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ném bóng vào rổ $25$ lần, bóng vào rổ $15$ lần thì tỉ số bóng vào rổ so với tổng số lần '
                 'ném là $\\dfrac{15}{40}$.',
            'answer': False,
            'solution': 'Tổng số lần ném là $25$ nên tỉ số đúng phải là $\\dfrac{15}{25}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số lần thực hiện**, quy '
                 'tắc **Dạng phân số** được xác định bởi $\\text{Tỉ số} = \\dfrac{k}{n}$ ($k$: số lần sự '
                 'kiện xảy ra; $n$: tổng số lần thực hiện) và khi áp dụng cho ví dụ “Gieo một con xúc xắc '
                 '$50$ lần, mặt $6$ chấm xuất hiện $8$ lần. Viết tỉ số và tỉ số phần trăm số lần xuất hiện '
                 'mặt $6$ chấm so với tổng...” ta có lời giải: Tỉ số là $\\dfrac{8}{50} = \\dfrac{4}{25}$. '
                 'Đổi sang tỉ số phần trăm: $\\dfrac{8}{50} = \\dfrac{16}{100} = 16\\%$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Dạng phân số** ($\\text{Tỉ số} = '
                        '\\dfrac{k}{n}$ ($k$: số lần sự kiện xảy ra; $n$: tổng số lần thực hiện)) và lời '
                        'giải ví dụ minh họa của Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số '
                        'lần thực hiện.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 65: Tỉ số của số lần lặp lại một sự kiện so với '
                 'tổng số lần thực hiện** để giải bài toán sau: Gieo một con xúc xắc $50$ lần, mặt $6$ chấm '
                 'xuất hiện $8$ lần. Viết tỉ số và tỉ số phần trăm số lần xuất hiện mặt $6$ chấm so với tổng '
                 'số lần gieo. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tỉ số là $\\dfrac{9}{50} = \\dfrac{4}{25}$. Đổi sang tỉ số phần trăm: '
                        '$\\dfrac{8}{50} = \\dfrac{16}{100} = 16\\%$.',
                        'Tỉ số là $\\dfrac{50}{8} = \\dfrac{4}{25}$. Đổi sang tỉ số phần trăm: '
                        '$\\dfrac{8}{50} = \\dfrac{16}{100} = 16\\%$.',
                        'Tỉ số là $\\dfrac{8}{50} = \\dfrac{4}{25}$. Đổi sang tỉ số phần trăm: '
                        '$\\dfrac{8}{50} = \\dfrac{16}{100} = 16\\%$.',
                        'Tỉ số là $\\dfrac{16}{50} = \\dfrac{4}{25}$. Đổi sang tỉ số phần trăm: '
                        '$\\dfrac{8}{50} = \\dfrac{16}{100} = 16\\%$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 65: Tỉ số của số lần lặp lại một sự kiện so với tổng số '
                        'lần thực hiện: Tỉ số là $\\dfrac{8}{50} = \\dfrac{4}{25}$. Đổi sang tỉ số phần '
                        'trăm: $\\dfrac{8}{50} = \\dfrac{16}{100} = 16\\%$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cầu thủ thực hiện $40$ quả sút phạt, trong đó có $34$ lần bóng vào lưới. Tỉ số phần '
                 'trăm số lần sút phạt thành công là bao nhiêu phần trăm?',
            'answer': ['85', '85%'],
            'unit': None,
            'solution': 'Tỉ số phần trăm sút thành công là $(34 : 40) \\times 100\\% = 85\\%$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd12-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 12: Ôn tập cuối năm',
  'context': 'Chủ đề 12 · SGK Toán 5: Ôn tập tổng hợp cuối năm chương trình Toán Tiểu học.',
  'title': 'Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép tính',
  'icon': '🏁',
  'description': 'Hệ thống hóa toàn bộ kiến thức về số tự nhiên, phân số, số thập phân và bốn phép tính.',
  'requirements': ['Chuyển đổi linh hoạt giữa phân số, phân số thập phân, hỗn số, số thập phân và tỉ số phần '
                   'trăm.',
                   'Thực hiện thành thạo bốn phép tính và tính giá trị biểu thức, tìm thành phần chưa biết.',
                   'Vận dụng kiến thức của **Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép '
                   'tính** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Mối liên hệ: $\\dfrac{3}{4} = \\dfrac{75}{100} = 0{,}75 = 75\\%$.\n'
                '- Các tính chất giao hoán, kết hợp, phân phối áp dụng giống nhau cho số tự nhiên, phân số '
                'và số thập phân.',
  'theory': '### 1. Chuyển đổi giữa các dạng số\n'
            '- Phân số $\\rightarrow$ số thập phân: lấy tử số chia cho mẫu số (hoặc đưa về phân số thập '
            'phân).\n'
            '### 2. Tính hợp lí giá trị biểu thức\n'
            '- Nhóm các số hạng có tổng tròn chục, tròn đơn vị ($0{,}25 + 0{,}75 = 1$) hoặc các tích đặc '
            'biệt ($2{,}5 \\times 4 = 10$; $0{,}125 \\times 8 = 1$).',
  'formulas': [{'category': 'Các cặp tích đặc biệt cần nhớ',
                'items': [{'name': 'Tích bằng 1 hoặc 10',
                           'formula': '$0{,}5 \\times 2 = 1$; $0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = '
                                      '1$'},
                          {'name': 'Tính chất phân phối',
                           'formula': '$a \\times b \\pm a \\times c = a \\times (b \\pm c)$'}]}],
  'example': 'Tính bằng cách thuận tiện: $0{,}25 \\times 13{,}8 \\times 4$.',
  'example_answer': 'Nhóm $(0{,}25 \\times 4) \\times 13{,}8 = 1 \\times 13{,}8 = 13{,}8$.',
  'real_life': 'Tính toán chi tiêu, hóa đơn mua sắm và quy đổi các chỉ số trong đời sống.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số $\\dfrac{3}{5}$ viết dưới dạng số thập phân là:',
            'options': ['$0{,}35$', '$0{,}6$', '$3{,}5$', '$0{,}06$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{3}{5} = \\dfrac{6}{10} = 0{,}6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x \\times 2{,}5 = 7{,}5 + 2{,}5$:',
            'options': ['$x = 3$', '$x = 25$', '$x = 4$', '$x = 0{,}4$'],
            'answer': 2,
            'solution': 'Ta có $x \\times 2{,}5 = 10 \\Rightarrow x = 10 : 2{,}5 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép tính**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Tích bằng 1 hoặc 10**?',
            'options': ['$0{,}5 : 2 = 1$; $0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = 1$',
                        '$0{,}5 \\times 2 = 1$; $0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = 2$',
                        '$2{,}5 \\times 2 = 1$; $0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = 1$',
                        '$0{,}5 \\times 2 = 1$; $0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = 1$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và '
                        'các phép tính, **Tích bằng 1 hoặc 10** được xác định bởi: $0{,}5 \\times 2 = 1$; '
                        '$0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = 1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép tính**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Tính chất phân phối**?',
            'options': ['$a \\times b \\pm a \\times c = a \\times (b \\pm c)$',
                        '$a : b \\pm a \\times c = a \\times (b \\pm c)$',
                        'Đảo ngược vế của quy tắc: $a \\times b \\pm a \\times c = a \\times (b \\pm c)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a \\times b \\pm a \\times c = '
                        'a \\times (b \\pm c)$'],
            'answer': 0,
            'solution': 'Trong Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép tính, **Tính '
                        'chất phân phối** có công thức/quy tắc là: $a \\times b \\pm a \\times c = a \\times '
                        '(b \\pm c)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $12{,}5 \\times 4{,}7 \\times 0{,}8$ là:',
            'options': ['$4{,}7$', '$47$', '$470$', '$37{,}6$'],
            'answer': 1,
            'solution': 'Nhóm $(12{,}5 \\times 0{,}8) \\times 4{,}7 = 10 \\times 4{,}7 = 47$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép '
                 'tính**, nhận định nào sau đây là **chính xác**?',
            'options': ['Chuyển đổi linh hoạt giữa phân số, phân số thập phân, hỗn số, số thập phân và tỉ số '
                        'phần trăm. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Chuyển đổi linh hoạt giữa phân số, phân số thập phân, hỗn '
                        'số, số thập phân và tỉ số phần trăm.',
                        'Chuyển đổi linh hoạt giữa phân số, phân số thập phân, hỗn số, số thập phân và tỉ số '
                        'phần trăm.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chuyển đổi linh hoạt giữa phân '
                        'số, phân số thập phân, hỗn số, số thập phân và tỉ số phần trăm.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các '
                        'phép tính: Chuyển đổi linh hoạt giữa phân số, phân số thập phân, hỗn số, số thập '
                        'phân và tỉ số phần trăm.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ta có $\\dfrac{1}{8} = 0{,}125 = 12{,}5\\%$.',
            'answer': True,
            'solution': 'Vì $1 : 8 = 0{,}125 = 12{,}5\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép tính**, quy tắc '
                 '**Tích bằng 1 hoặc 10** được xác định bởi $0{,}5 \\times 2 = 1$; $0{,}25 \\times 4 = 1$; '
                 '$0{,}125 \\times 8 = 1$ và khi áp dụng cho ví dụ “Tính bằng cách thuận tiện: $0{,}25 '
                 '\\times 13{,}8 \\times 4$.” ta có lời giải: Nhóm $(0{,}25 \\times 4) \\times 13{,}8 = 1 '
                 '\\times 13{,}8 = 13{,}8$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tích bằng 1 hoặc 10** ($0{,}5 \\times 2 '
                        '= 1$; $0{,}25 \\times 4 = 1$; $0{,}125 \\times 8 = 1$) và lời giải ví dụ minh họa '
                        'của Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các phép tính.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và '
                 'các phép tính** để giải bài toán sau: Tính bằng cách thuận tiện: $0{,}25 \\times 13{,}8 '
                 '\\times 4$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Nhóm $(0{,}25 : 4) \\times 13{,}8 = 1 \\times 13{,}8 = 13{,}8$.',
                        'Nhóm $(0{,}25 \\times 4) \\times 13{,}8 = 1 \\times 13{,}8 = 13{,}7$.',
                        'Nhóm $(2{,}25 \\times 4) \\times 13{,}8 = 1 \\times 13{,}8 = 13{,}8$.',
                        'Nhóm $(0{,}25 \\times 4) \\times 13{,}8 = 1 \\times 13{,}8 = 13{,}8$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 68: Ôn tập số tự nhiên, phân số, số thập phân và các '
                        'phép tính: Nhóm $(0{,}25 \\times 4) \\times 13{,}8 = 1 \\times 13{,}8 = 13{,}8$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức: $15{,}6 \\times 6{,}4 + 15{,}6 \\times 3{,}6$.',
            'answer': ['156'],
            'unit': None,
            'solution': 'Ta có $15{,}6 \\times (6{,}4 + 3{,}6) = 15{,}6 \\times 10 = 156$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd12-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 12: Ôn tập cuối năm',
  'context': 'Chủ đề 12 · SGK Toán 5: Ôn tập tổng hợp cuối năm chương trình Toán Tiểu học.',
  'title': 'Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động đều',
  'icon': '🏁',
  'description': 'Ôn tập các dạng toán điển hình về tổng – tỉ, hiệu – tỉ, tỉ số phần trăm và toán chuyển '
                 'động đều.',
  'requirements': ['Giải thành thạo bài toán tổng – tỉ, hiệu – tỉ và các bài toán về tỉ số phần trăm (lãi '
                   'suất, giảm giá).',
                   'Vận dụng công thức $s = v \\times t$, $v = s : t$, $t = s : v$ để giải bài toán chuyển '
                   'động đều.',
                   'Vận dụng kiến thức của **Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động đều** '
                   'để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Bài toán Tổng – Tỉ: tìm tổng số phần $(m + n)$. Bài toán Hiệu – Tỉ: tìm hiệu số phần $(n '
                '- m)$.\n'
                '- Chuyển động đều: $s = v \\times t \\Leftrightarrow v = s : t \\Leftrightarrow t = s : v$.',
  'theory': '### 1. Bài toán lãi suất và giảm giá\n'
            '- Tiền lãi sau $1$ kỳ = $\\text{Tiền gốc} \\times \\text{Lãi suất}\\%$.\n'
            '### 2. Chuyển động cùng chiều và ngược chiều\n'
            '- Hai xe đi ngược chiều: mỗi giờ gần nhau một đoạn bằng tổng hai vận tốc $(v_1 + v_2)$.\n'
            '- Hai xe đi cùng chiều đuổi nhau: mỗi giờ xe sau rút ngắn khoảng cách bằng hiệu hai vận tốc '
            '$(v_1 - v_2)$.',
  'formulas': [{'category': 'Tổng hợp công thức giải toán có lời văn',
                'items': [{'name': 'Tỉ số phần trăm',
                           'formula': 'Tỉ số $\\%$ của $a$ và $b$ là $(a : b) \\times 100\\%$; $m\\%$ của '
                                      '$A$ là $A \\times m : 100$'},
                          {'name': 'Chuyển động đều',
                           'formula': '$s = v \\times t$; $v = s : t$; $t = s : v$'}]}],
  'example': 'Một người gửi tiết kiệm $20\\,000\\,000$ đồng với lãi suất $0{,}5\\%$ một tháng. Sau một tháng '
             'người đó nhận được cả gốc và lãi là bao nhiêu?',
  'example_answer': 'Tiền lãi sau $1$ tháng là $20\\,000\\,000 \\times 0{,}5 : 100 = 100\\,000$ (đồng). Tổng '
                    'cả gốc và lãi là $20\\,100\\,000$ (đồng).',
  'real_life': 'Tính toán tài chính gia đình, lập lộ trình chuyến đi du lịch và ước tính thời gian di '
               'chuyển.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tỉ số phần trăm của $7$ và $28$ là:',
            'options': ['$4\\%$', '$400\\%$', '$25\\%$', '$21\\%$'],
            'answer': 2,
            'solution': 'Ta có $7 : 28 = 0{,}25 = 25\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi $2{,}5\\text{ giờ}$ sang đơn vị phút ta được:',
            'options': ['$250\\text{ phút}$',
                        '$25\\text{ phút}$',
                        '$130\\text{ phút}$',
                        '$150\\text{ phút}$'],
            'answer': 3,
            'solution': 'Ta có $2{,}5 \\times 60 = 150\\text{ phút}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động đều**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Tỉ số phần trăm**?',
            'options': ['Tỉ số $\\%$ của $a$ và $b$ là $(a : b) \\times 100\\%$; $m\\%$ của $A$ là $A '
                        '\\times m : 100$',
                        'Tỉ số $\\%$ của $a$ và $b$ là $(a : b) : 100\\%$; $m\\%$ của $A$ là $A \\times m : '
                        '100$',
                        'Tỉ số $\\%$ của $a$ và $b$ là $(a : b) \\times 100\\%$; $m\\%$ của $A$ là $A '
                        '\\times m : 99$',
                        'Tỉ số $\\%$ của $a$ và $b$ là $(a : b) \\times 102\\%$; $m\\%$ của $A$ là $A '
                        '\\times m : 100$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển '
                        'động đều, **Tỉ số phần trăm** được xác định bởi: Tỉ số $\\%$ của $a$ và $b$ là $(a '
                        ': b) \\times 100\\%$; $m\\%$ của $A$ là $A \\times m : 100$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động đều**, biểu thức hoặc '
                 'quy tắc nào dưới đây biểu diễn đúng **Chuyển động đều**?',
            'options': ['$s = v : t$; $v = s : t$; $t = s : v$',
                        '$s = v \\times t$; $v = s : t$; $t = s : v$',
                        'Đảo ngược vế của quy tắc: $s = v \\times t$; $v = s : t$; $t = s : v$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $s = v \\times t$; $v = s : t$; '
                        '$t = s : v$'],
            'answer': 1,
            'solution': 'Trong Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động đều, **Chuyển động '
                        'đều** có công thức/quy tắc là: $s = v \\times t$; $v = s : t$; $t = s : v$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một ô tô đi quãng đường $135\\text{ km}$ với vận tốc $45\\text{ km/giờ}$. Thời gian ô tô '
                 'đi hết quãng đường đó là:',
            'options': ['$2{,}5\\text{ giờ}$', '$3{,}5\\text{ giờ}$', '$3\\text{ giờ}$', '$4\\text{ giờ}$'],
            'answer': 2,
            'solution': 'Thời gian đi là $t = 135 : 45 = 3\\text{ giờ}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động '
                 'đều**, nhận định nào sau đây là **chính xác**?',
            'options': ['Giải thành thạo bài toán tổng – tỉ, hiệu – tỉ và các bài toán về tỉ số phần trăm '
                        '(lãi suất, giảm giá). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Giải thành thạo bài toán tổng – tỉ, hiệu – tỉ và các bài '
                        'toán về tỉ số phần trăm (lãi suất, giảm giá).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải thành thạo bài toán tổng – '
                        'tỉ, hiệu – tỉ và các bài toán về tỉ số phần trăm (lãi suất, giảm giá).',
                        'Giải thành thạo bài toán tổng – tỉ, hiệu – tỉ và các bài toán về tỉ số phần trăm '
                        '(lãi suất, giảm giá).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động '
                        'đều: Giải thành thạo bài toán tổng – tỉ, hiệu – tỉ và các bài toán về tỉ số phần '
                        'trăm (lãi suất, giảm giá).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Một chiếc xe đạp giá $2\\,000\\,000$ đồng, giảm giá $10\\%$ thì giá mới là $1\\,800\\,000$ '
                 'đồng.',
            'answer': True,
            'solution': 'Số tiền giảm là $200\\,000$ đồng nên giá mới là $2\\,000\\,000 - 200\\,000 = '
                        '1\\,800\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động đều**, quy tắc **Tỉ số '
                 'phần trăm** được xác định bởi Tỉ số $\\%$ của $a$ và $b$ là $(a : b) \\times 100\\%$; '
                 '$m\\%$ của $A$ là $A \\times m : 100$ và khi áp dụng cho ví dụ “Một người gửi tiết kiệm '
                 '$20\\,000\\,000$ đồng với lãi suất $0{,}5\\%$ một tháng. Sau một tháng người đó nhận được '
                 'cả gốc và lãi là bao nhi...” ta có lời giải: Tiền lãi sau $1$ tháng là $20\\,000\\,000 '
                 '\\times 0{,}5 : 100 = 100\\,000$ (đồng). Tổng cả gốc và lãi là $20\\,100\\,000$ (đồng).. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tỉ số phần trăm** (Tỉ số $\\%$ của $a$ '
                        'và $b$ là $(a : b) \\times 100\\%$; $m\\%$ của $A$ là $A \\times m : 100$) và lời '
                        'giải ví dụ minh họa của Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động '
                        'đều.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển '
                 'động đều** để giải bài toán sau: Một người gửi tiết kiệm $20\\,000\\,000$ đồng với lãi '
                 'suất $0{,}5\\%$ một tháng. Sau một tháng người đó nhận được cả gốc và lãi là bao nhiêu? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tiền lãi sau $1$ tháng là $20\\,000\\,000 \\times 0{,}5 : 100 = 100\\,000$ (đồng). '
                        'Tổng cả gốc và lãi là $20\\,100\\,000$ (đồng).',
                        'Tiền lãi sau $1$ tháng là $20\\,000\\,000 : 0{,}5 : 100 = 100\\,000$ (đồng). Tổng '
                        'cả gốc và lãi là $20\\,100\\,000$ (đồng).',
                        'Tiền lãi sau $1$ tháng là $20\\,000\\,000 \\times 0{,}5 : 100 = 100\\,000$ (đồng). '
                        'Tổng cả gốc và lãi là $20\\,100\\,1$ (đồng).',
                        'Tiền lãi sau $2$ tháng là $20\\,000\\,000 \\times 0{,}5 : 100 = 100\\,000$ (đồng). '
                        'Tổng cả gốc và lãi là $20\\,100\\,000$ (đồng).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 70: Ôn tập tỉ số, tỉ số phần trăm và toán chuyển động '
                        'đều: Tiền lãi sau $1$ tháng là $20\\,000\\,000 \\times 0{,}5 : 100 = 100\\,000$ '
                        '(đồng). Tổng cả gốc và lãi là $20\\,100\\,000$ (đồng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một người đi xe đạp từ A lúc $6\\text{ giờ}$ với vận tốc $15\\text{ km/giờ}$ và đến B lúc '
                 '$7\\text{ giờ } 20\\text{ phút}$. Tính quãng đường AB theo đơn vị ki-lô-mét.',
            'answer': ['20'],
            'unit': None,
            'solution': 'Thời gian đi là $1\\text{ giờ } 20\\text{ phút} = \\dfrac{4}{3}\\text{ giờ}$. Quãng '
                        'đường AB dài $15 \\times \\dfrac{4}{3} = 20$ ($\\text{km}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l5-cd12-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 12: Ôn tập cuối năm',
  'context': 'Chủ đề 12 · SGK Toán 5: Ôn tập tổng hợp cuối năm chương trình Toán Tiểu học.',
  'title': 'Bài 71: Ôn tập hình học, đo lường và thống kê xác suất',
  'icon': '🏁',
  'description': 'Hệ thống hóa công thức chu vi, diện tích hình phẳng; diện tích, thể tích hình khối; đo '
                 'lường và thống kê xác suất.',
  'requirements': ['Tính đúng chu vi, diện tích tam giác, hình thang, hình tròn và diện tích, thể tích hình '
                   'hộp chữ nhật, hình lập phương.',
                   'Chuyển đổi thành thạo các đơn vị đo và giải bài toán kết hợp biểu đồ, tỉ số phần trăm.',
                   'Vận dụng kiến thức của **Bài 71: Ôn tập hình học, đo lường và thống kê xác suất** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Hình phẳng: tam giác $S = \\dfrac{a \\times h}{2}$; hình thang $S = \\dfrac{(a + b) '
                '\\times h}{2}$; hình tròn $C = d \\times 3{,}14$, $S = r \\times r \\times 3{,}14$.\n'
                '- Hình khối: hình hộp chữ nhật $V = a \\times b \\times c$; hình lập phương $V = a \\times '
                'a \\times a$.',
  'theory': '### 1. Tổng hợp đơn vị đo diện tích và thể tích\n'
            '- Diện tích: $1\\text{ km}^2 = 100\\text{ ha} = 1\\,000\\,000\\text{ m}^2$; $1\\text{ m}^2 = '
            '100\\text{ dm}^2 = 10\\,000\\text{ cm}^2$.\n'
            '- Thể tích: $1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$; $1\\text{ dm}^3 = 1000\\text{ '
            'cm}^3 = 1\\text{ l}$.\n'
            '### 2. Thống kê và xác suất\n'
            '- Biểu đồ hình quạt tròn có tổng các phần bằng $100\\%$; tỉ số lặp lại của sự kiện là '
            '$\\dfrac{k}{n}$.',
  'formulas': [{'category': 'Hình học phẳng và không gian',
                'items': [{'name': 'Hình thang và Hình tròn',
                           'formula': '$S_{\\text{ht}} = \\dfrac{(a + b) \\times h}{2}$; $S_{\\text{tròn}} = '
                                      'r \\times r \\times 3{,}14$'},
                          {'name': 'Hình hộp chữ nhật và Lập phương',
                           'formula': '$V_{\\text{hộp}} = a \\times b \\times c$; $V_{\\text{LP}} = a '
                                      '\\times a \\times a$'}]}],
  'example': 'Một bể nước hình hộp chữ nhật dài $2\\text{ m}$, rộng $1{,}2\\text{ m}$, cao $1\\text{ m}$ '
             'hiện đang chứa $75\\%$ thể tích bể. Trong bể có bao nhiêu lít nước?',
  'example_answer': 'Thể tích bể là $V = 2 \\times 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ l}$. Số '
                    'lít nước hiện có là $2400 \\times 75 : 100 = 1800\\text{ l}$.',
  'real_life': 'Tính thể tích bể chứa nước, diện tích đất xây dựng và đọc biểu đồ thống kê trên sách báo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Diện tích hình thang có hai đáy $7\\text{ cm}$ và $5\\text{ cm}$, chiều cao $4\\text{ cm}$ '
                 'là:',
            'options': ['$48\\text{ cm}^2$', '$140\\text{ cm}^2$', '$16\\text{ cm}^2$', '$24\\text{ cm}^2$'],
            'answer': 3,
            'solution': 'Ta có $S = \\dfrac{(7 + 5) \\times 4}{2} = 24\\text{ cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một mét khối ($1\\text{ m}^3$) bằng bao nhiêu lít?',
            'options': ['$1000\\text{ l}$', '$100\\text{ l}$', '$10\\text{ l}$', '$10\\,000\\text{ l}$'],
            'answer': 0,
            'solution': 'Ta có $1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ l}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 71: Ôn tập hình học, đo lường và thống kê xác suất**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Hình thang và Hình tròn**?',
            'options': ['$S_{\\text{ht}} = \\dfrac{(a - b) \\times h}{2}$; $S_{\\text{tròn}} = r \\times r '
                        '\\times 3{,}14$',
                        '$S_{\\text{ht}} = \\dfrac{(a + b) \\times h}{2}$; $S_{\\text{tròn}} = r \\times r '
                        '\\times 3{,}14$',
                        '$S_{\\text{ht}} = \\dfrac{2}{(a + b) \\times h}$; $S_{\\text{tròn}} = r \\times r '
                        '\\times 3{,}14$',
                        '$S_{\\text{ht}} = \\dfrac{(a + b) \\times h}{4}$; $S_{\\text{tròn}} = r \\times r '
                        '\\times 3{,}14$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 71: Ôn tập hình học, đo lường và thống kê xác '
                        'suất, **Hình thang và Hình tròn** được xác định bởi: $S_{\\text{ht}} = \\dfrac{(a + '
                        'b) \\times h}{2}$; $S_{\\text{tròn}} = r \\times r \\times 3{,}14$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 71: Ôn tập hình học, đo lường và thống kê xác suất**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Hình hộp chữ nhật và Lập phương**?',
            'options': ['$V_{\\text{hộp}} = a : b \\times c$; $V_{\\text{LP}} = a \\times a \\times a$',
                        'Đảo ngược vế của quy tắc: $V_{\\text{hộp}} = a \\times b \\times c$; '
                        '$V_{\\text{LP}} = a \\times a \\times a$',
                        '$V_{\\text{hộp}} = a \\times b \\times c$; $V_{\\text{LP}} = a \\times a \\times a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $V_{\\text{hộp}} = a \\times b '
                        '\\times c$; $V_{\\text{LP}} = a \\times a \\times a$'],
            'answer': 2,
            'solution': 'Trong Bài 71: Ôn tập hình học, đo lường và thống kê xác suất, **Hình hộp chữ nhật '
                        'và Lập phương** có công thức/quy tắc là: $V_{\\text{hộp}} = a \\times b \\times c$; '
                        '$V_{\\text{LP}} = a \\times a \\times a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình lập phương có diện tích toàn phần là $150\\text{ cm}^2$. Thể tích của hình lập '
                 'phương đó là:',
            'options': ['$25\\text{ cm}^3$',
                        '$100\\text{ cm}^3$',
                        '$150\\text{ cm}^3$',
                        '$125\\text{ cm}^3$'],
            'answer': 3,
            'solution': 'Diện tích một mặt là $150 : 6 = 25\\text{ cm}^2 \\Rightarrow$ cạnh $a = 5\\text{ '
                        'cm}$. Thể tích là $5 \\times 5 \\times 5 = 125\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 71: Ôn tập hình học, đo lường và thống kê xác suất**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Tính đúng chu vi, diện tích tam giác, hình thang, hình tròn và diện tích, thể tích '
                        'hình hộp chữ nhật, hình lập phương.',
                        'Tính đúng chu vi, diện tích tam giác, hình thang, hình tròn và diện tích, thể tích '
                        'hình hộp chữ nhật, hình lập phương. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính đúng chu vi, diện tích tam giác, hình thang, hình '
                        'tròn và diện tích, thể tích hình hộp chữ nhật, hình lập phương.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính đúng chu vi, diện tích tam '
                        'giác, hình thang, hình tròn và diện tích, thể tích hình hộp chữ nhật, hình lập '
                        'phương.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 71: Ôn tập hình học, đo lường và thống kê xác suất: '
                        'Tính đúng chu vi, diện tích tam giác, hình thang, hình tròn và diện tích, thể tích '
                        'hình hộp chữ nhật, hình lập phương.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Hình lập phương có cạnh $0{,}5\\text{ m}$ thì có thể tích là $0{,}125\\text{ m}^3$.',
            'answer': True,
            'solution': 'Ta có $V = 0{,}5 \\times 0{,}5 \\times 0{,}5 = 0{,}125\\text{ m}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 71: Ôn tập hình học, đo lường và thống kê xác suất**, quy tắc **Hình thang và '
                 'Hình tròn** được xác định bởi $S_{\\text{ht}} = \\dfrac{(a + b) \\times h}{2}$; '
                 '$S_{\\text{tròn}} = r \\times r \\times 3{,}14$ và khi áp dụng cho ví dụ “Một bể nước hình '
                 'hộp chữ nhật dài $2\\text{ m}$, rộng $1{,}2\\text{ m}$, cao $1\\text{ m}$ hiện đang chứa '
                 '$75\\%$ thể tích bể. Trong bể có...” ta có lời giải: Thể tích bể là $V = 2 \\times 1{,}2 '
                 '\\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ l}$. Số lít nước hiện có là $2400 \\times 75 : '
                 '100 = 1800\\text{ l}$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hình thang và Hình tròn** '
                        '($S_{\\text{ht}} = \\dfrac{(a + b) \\times h}{2}$; $S_{\\text{tròn}} = r \\times r '
                        '\\times 3{,}14$) và lời giải ví dụ minh họa của Bài 71: Ôn tập hình học, đo lường '
                        'và thống kê xác suất.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 71: Ôn tập hình học, đo lường và thống kê xác '
                 'suất** để giải bài toán sau: Một bể nước hình hộp chữ nhật dài $2\\text{ m}$, rộng '
                 '$1{,}2\\text{ m}$, cao $1\\text{ m}$ hiện đang chứa $75\\%$ thể tích bể. Trong bể có bao '
                 'nhiêu lít nước? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Thể tích bể là $V = 2 : 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ l}$. Số '
                        'lít nước hiện có là $2400 \\times 75 : 100 = 1800\\text{ l}$.',
                        'Thể tích bể là $V = 2 \\times 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ '
                        'l}$. Số lít nước hiện có là $2400 \\times 75 : 100 = 1800\\text{ l}$.',
                        'Thể tích bể là $V = 2 \\times 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ '
                        'l}$. Số lít nước hiện có là $2400 \\times 75 : 100 = 1799\\text{ l}$.',
                        'Thể tích bể là $V = 4 \\times 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ '
                        'l}$. Số lít nước hiện có là $2400 \\times 75 : 100 = 1800\\text{ l}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 71: Ôn tập hình học, đo lường và thống kê xác suất: Thể '
                        'tích bể là $V = 2 \\times 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ l}$. Số '
                        'lít nước hiện có là $2400 \\times 75 : 100 = 1800\\text{ l}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bể nước hình hộp chữ nhật dài $2\\text{ m}$, rộng $1{,}2\\text{ m}$, cao $1\\text{ '
                 'm}$. Hiện bể đang chứa nước chiếm $75\\%$ thể tích bể. Hỏi trong bể có bao nhiêu lít nước?',
            'answer': ['1800'],
            'unit': None,
            'solution': 'Thể tích bể là $2 \\times 1{,}2 \\times 1 = 2{,}4\\text{ m}^3 = 2400\\text{ l}$. '
                        'Lượng nước trong bể là $2400 \\times 75 : 100 = 1800$ ($\\text{l}$).',
            'alt': None,
            'note': None}]}]
