"""Dữ liệu bài học SGK Toán Lớp 7 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 7 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học (title).
Mỗi bài học gồm đầy đủ Yêu cầu cần đạt (requirements), Định nghĩa, Lý thuyết, Công thức, Ví dụ, Ứng dụng thực tế
và đúng 10 câu hỏi luyện tập theo 3 mức độ: 4 Nhận biết + 4 Thông hiểu + 2 Vận dụng.
"""

GRADE = 7

LESSONS = [{'topic': 'l7-ch01-so-huu-ti',
  'context_title': 'Chương I: Số hữu tỉ',
  'context': 'Chương I · SGK Toán 7: Tập hợp các số hữu tỉ và các phép tính cộng, trừ, nhân, chia, lũy thừa.',
  'title': 'Bài 1: Tập hợp các số hữu tỉ',
  'icon': '🔢',
  'description': 'Khái niệm số hữu tỉ, biểu diễn số hữu tỉ trên trục số và thứ tự trong tập hợp các số hữu '
                 'tỉ.',
  'requirements': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số hữu tỉ '
                   '$\\mathbb{Q}$.',
                   'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                   'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
  'definition': 'Số hữu tỉ là số viết được dưới dạng phân số $\\dfrac{a}{b}$ với $a, b \\in \\mathbb{Z}, b '
                '\\neq 0$. Tập hợp các số hữu tỉ được kí hiệu là $\\mathbb{Q}$.',
  'theory': '1. Khái niệm số hữu tỉ: Mọi số nguyên, hỗn số, số thập phân hữu hạn đều viết được dưới dạng '
            'phân số $\\dfrac{a}{b}$ ($a, b \\in \\mathbb{Z}, b \\neq 0$) nên đều là số hữu tỉ.\n'
            '2. Số đối: Trên trục số, hai số hữu tỉ (phân biệt) có điểm biểu diễn nằm về hai phía của điểm '
            'gốc $0$ và cách đều điểm gốc $0$ được gọi là hai số đối nhau. Số đối của số hữu tỉ $a$ kí hiệu '
            'là $-a$. Số đối của $0$ là $0$.\n'
            '3. So sánh hai số hữu tỉ: Với hai số hữu tỉ $x, y$ bất kì, ta luôn có hoặc $x = y$, hoặc $x < '
            'y$, hoặc $x > y$. Trên trục số nằm ngang, nếu $x < y$ thì điểm $x$ nằm bên trái điểm $y$. Số '
            'hữu tỉ lớn hơn $0$ gọi là số hữu tỉ dương; nhỏ hơn $0$ gọi là số hữu tỉ âm; số $0$ không là số '
            'hữu tỉ dương cũng không là số hữu tỉ âm.',
  'formulas': [{'category': 'Tập hợp và tính chất số hữu tỉ',
                'items': [{'name': 'Định nghĩa tập $\\mathbb{Q}$',
                           'formula': '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                                      '\\mathbb{Z}, b \\neq 0 \\right\\}$'},
                          {'name': 'Quan hệ tập hợp',
                           'formula': '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'},
                          {'name': 'Tính chất số đối', 'formula': '$-(-a) = a$ với mọi $a \\in \\mathbb{Q}$'},
                          {'name': 'Tính chất bắc cầu', 'formula': 'Nếu $x < y$ và $y < z$ thì $x < z$'}]}],
  'example': 'Viết các số $-2,5$; $1\\dfrac{2}{3}$; $-4$ dưới dạng phân số và sắp xếp chúng theo thứ tự tăng '
             'dần.',
  'example_answer': 'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; $-4 '
                    '= \\dfrac{-4}{1} = \\dfrac{-24}{6}$.\n'
                    'Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ nên thứ tự tăng dần là: $-4; -2,5; 1\\dfrac{2}{3}$.',
  'real_life': 'Biểu diễn mực nước dâng lên hoặc hạ xuống tại các trạm thủy văn (ví dụ: $-1,2\\text{ m}$ '
               'hoặc $+0,75\\text{ m}$) so với mực nước chuẩn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tập hợp các số hữu tỉ được kí hiệu là gì?',
            'options': ['$\\mathbb{Q}$', '$\\mathbb{Z}$', '$\\mathbb{N}$', '$\\mathbb{N}^*$'],
            'answer': 0,
            'solution': 'Tập hợp các số hữu tỉ được kí hiệu là $\\mathbb{Q}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số đối của số hữu tỉ $\\dfrac{-3}{5}$ là số nào?',
            'options': ['$\\dfrac{-5}{3}$', '$\\dfrac{3}{5}$', '$\\dfrac{5}{3}$', '$\\dfrac{-3}{5}$'],
            'answer': 1,
            'solution': 'Số đối của $\\dfrac{-3}{5}$ là $-\\left(\\dfrac{-3}{5}\\right) = \\dfrac{3}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 1: Tập hợp các số hữu tỉ**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Định nghĩa tập $\\mathbb{Q}$**?',
            'options': ['$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$',
                        '$-(-a) = a$ với mọi $a \\in \\mathbb{Q}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        'Nếu $x < y$ và $y < z$ thì $x < z$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 1: Tập hợp các số hữu tỉ, **Định nghĩa tập '
                        '$\\mathbb{Q}$** được xác định bởi: $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Tập hợp các số hữu tỉ**, nội dung/biểu thức $\\mathbb{N} \\subset '
                 '\\mathbb{Z} \\subset \\mathbb{Q}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa tập $\\mathbb{Q}$',
                        'Tính chất số đối',
                        'Tính chất bắc cầu',
                        'Quan hệ tập hợp'],
            'answer': 3,
            'solution': 'Trong Bài 1: Tập hợp các số hữu tỉ, biểu thức/quy tắc $\\mathbb{N} \\subset '
                        '\\mathbb{Z} \\subset \\mathbb{Q}$ chính là nội dung của **Quan hệ tập hợp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các số hữu tỉ $\\dfrac{-2}{3}; -0,5; 0; \\dfrac{3}{4}$, số nhỏ nhất là:',
            'options': ['$\\dfrac{-2}{3}$', '$-0,5$', '$0$', '$\\dfrac{3}{4}$'],
            'answer': 0,
            'solution': 'Ta có $\\dfrac{-2}{3} = \\dfrac{-4}{6}$ và $-0,5 = \\dfrac{-1}{2} = '
                        '\\dfrac{-3}{6}$. Vì $\\dfrac{-4}{6} < \\dfrac{-3}{6} < 0 < \\dfrac{3}{4}$ nên số '
                        'nhỏ nhất là $\\dfrac{-2}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Tập hợp các số hữu tỉ** (Chương I: Số hữu tỉ), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Thực hiện được các phép tính cộng, trừ, nhân, chia trong tập hợp số hữu tỉ '
                        '$\\mathbb{Q}$.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Vận dụng được các tính chất giao hoán, kết hợp, phân phối của phép nhân đối với '
                        'phép cộng để tính nhẩm và tính hợp lí.',
                        'Giải quyết được một số vấn đề thực tiễn gắn với các phép tính về số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 1: Tập hợp các số hữu tỉ: Nhận biết được số hữu tỉ và '
                        'lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số hữu tỉ $\\mathbb{Q}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về số hữu tỉ:',
            'statements': ['Mọi số nguyên đều là số hữu tỉ.',
                           'Số $0$ vừa là số hữu tỉ dương, vừa là số hữu tỉ âm.',
                           'Số hữu tỉ $-1,25$ viết được dưới dạng phân số tối giản là $\\dfrac{-5}{4}$.',
                           'Trên trục số nằm ngang, điểm biểu diễn số $\\dfrac{-1}{3}$ nằm bên phải điểm '
                           'biểu diễn số $\\dfrac{-2}{3}$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $a = \\dfrac{a}{1} \\in \\mathbb{Q}$. b) Sai vì $0$ không là số hữu tỉ '
                        'dương cũng không là số hữu tỉ âm. c) Đúng vì $-1,25 = \\dfrac{-125}{100} = '
                        '\\dfrac{-5}{4}$. d) Đúng vì $\\dfrac{-1}{3} > \\dfrac{-2}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 1: Tập hợp các số hữu '
                 'tỉ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được số hữu tỉ và lấy '
                           'được ví dụ về số hữu tỉ, nhận biết tập hợp các số hữu tỉ $\\mathbb{Q}$.',
                           'Quy tắc/công thức **Định nghĩa tập $\\mathbb{Q}$** trong bài được xác định bởi: '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$.',
                           'Trong mọi trường hợp, **Định nghĩa tập $\\mathbb{Q}$** luôn được tính bằng công '
                           'thức $\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a+b}{m}; \\quad \\dfrac{a}{m} - '
                           '\\dfrac{b}{m} = \\dfrac{a-b}{m} \\quad (m > 0)$ (thuộc Phép cộng, trừ cùng mẫu '
                           'dương) mà không cần điều kiện của Bài 1: Tập hợp các số hữu tỉ.',
                           'Với bài toán minh họa: “Viết các số $-2,5$; $1\\dfrac{2}{3}$; $-4$ dưới dạng '
                           'phân số và sắp xếp chúng theo thứ tự tăng dần.”, lời giải đúng là: Ta có: $-2,5 '
                           '= \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; $-4 = '
                           '\\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Tập hợp các số hữu tỉ. b) **Đúng** theo '
                        'công thức trọng tâm **Định nghĩa tập $\\mathbb{Q}$** ($\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$). c) '
                        '**Sai** vì $\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a+b}{m}; \\quad \\dfrac{a}{m} - '
                        '\\dfrac{b}{m} = \\dfrac{a-b}{m} \\quad (m > 0)$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Định nghĩa tập $\\mathbb{Q}$**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 1: Tập hợp các số hữu tỉ** để giải quyết tình huống sau: Viết các '
                 'số $-2,5$; $1\\dfrac{2}{3}$; $-4$ dưới dạng phân số và sắp xếp chúng theo thứ tự tăng dần. '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Ta có: $\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$. '
                        'Đẳng thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$. Áp '
                        'dụn...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Tập hợp các số hữu tỉ: Ta có: $-2,5 = \\dfrac{-5}{2} '
                        '= \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; $-4 = \\dfrac{-4}{1} = '
                        '\\dfrac{-24}{6}$.\n'
                        'Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ nên thứ tự tăng dần là: $-4; -2,5; '
                        '1\\dfrac{2}{3}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu số nguyên $x$ thỏa mãn $\\dfrac{-7}{2} < x < \\dfrac{5}{2}$?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Ta có $-3,5 < x < 2,5$. Vì $x \\in \\mathbb{Z}$ nên $x \\in \\{-3; -2; -1; 0; 1; '
                        '2\\}$, có tất cả $6$ số nguyên.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch01-so-huu-ti',
  'context_title': 'Chương I: Số hữu tỉ',
  'context': 'Chương I · SGK Toán 7: Tập hợp các số hữu tỉ và các phép tính cộng, trừ, nhân, chia, lũy thừa.',
  'title': 'Bài 2: Cộng, trừ, nhân, chia số hữu tỉ',
  'icon': '➕',
  'description': 'Quy tắc cộng, trừ, nhân, chia hai số hữu tỉ và các tính chất của phép tính trong tập hợp '
                 'số hữu tỉ.',
  'requirements': ['Thực hiện được các phép tính cộng, trừ, nhân, chia trong tập hợp số hữu tỉ '
                   '$\\mathbb{Q}$.',
                   'Vận dụng được các tính chất giao hoán, kết hợp, phân phối của phép nhân đối với phép '
                   'cộng để tính nhẩm và tính hợp lí.',
                   'Giải quyết được một số vấn đề thực tiễn gắn với các phép tính về số hữu tỉ.'],
  'definition': 'Mọi số hữu tỉ đều viết được dưới dạng phân số với mẫu dương, do đó ta có thể cộng, trừ, '
                'nhân, chia hai số hữu tỉ bằng cách viết chúng dưới dạng phân số rồi áp dụng quy tắc cộng, '
                'trừ, nhân, chia phân số.',
  'theory': '1. Cộng và trừ hai số hữu tỉ: Viết hai số hữu tỉ dưới dạng hai phân số có cùng một mẫu dương $x '
            '= \\dfrac{a}{m}, y = \\dfrac{b}{m}$ ($a, b, m \\in \\mathbb{Z}, m > 0$), khi đó $x + y = '
            '\\dfrac{a + b}{m}$ và $x - y = \\dfrac{a - b}{m}$.\n'
            '2. Nhân và chia hai số hữu tỉ: Với $x = \\dfrac{a}{b}, y = \\dfrac{c}{d}$ ($b, d \\neq 0$), ta '
            'có $x \\cdot y = \\dfrac{a \\cdot c}{b \\cdot d}$. Với $y \\neq 0$, ta có $x : y = '
            '\\dfrac{a}{b} \\cdot \\dfrac{d}{c} = \\dfrac{a \\cdot d}{b \\cdot c}$.\n'
            '3. Số nghịch đảo: Hai số gọi là nghịch đảo của nhau nếu tích của chúng bằng $1$. Số nghịch đảo '
            'của $x \\neq 0$ là $\\dfrac{1}{x}$.',
  'formulas': [{'category': 'Các phép tính với số hữu tỉ',
                'items': [{'name': 'Phép cộng, trừ cùng mẫu dương',
                           'formula': '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a+b}{m}; \\quad '
                                      '\\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a-b}{m} \\quad (m > 0)$'},
                          {'name': 'Phép nhân hai số hữu tỉ',
                           'formula': '$\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d} '
                                      '\\quad (b, d \\neq 0)$'},
                          {'name': 'Phép chia hai số hữu tỉ',
                           'formula': '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\cdot \\dfrac{d}{c} = '
                                      '\\dfrac{a \\cdot d}{b \\cdot c} \\quad (b, c, d \\neq 0)$'},
                          {'name': 'Tính chất phân phối',
                           'formula': '$x \\cdot (y + z) = x \\cdot y + x \\cdot z; \\quad x \\cdot (y - z) '
                                      '= x \\cdot y - x \\cdot z$'}]}],
  'example': 'Tính một cách hợp lí: $A = \\dfrac{-3}{7} \\cdot \\dfrac{5}{9} + \\dfrac{-3}{7} \\cdot '
             '\\dfrac{4}{9} + 1\\dfrac{3}{7}$.',
  'example_answer': 'Áp dụng tính chất phân phối của phép nhân đối với phép cộng:\n'
                    '$A = \\dfrac{-3}{7} \\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + '
                    '\\dfrac{10}{7} = \\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$.',
  'real_life': 'Tính tổng khối lượng hàng hóa, chi phí mua sắm hoặc diện tích đất canh tác khi các số đo cho '
               'dưới dạng phân số và số thập phân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $\\dfrac{-2}{5} + \\dfrac{3}{5}$ là:',
            'options': ['$\\dfrac{-1}{5}$', '$\\dfrac{1}{5}$', '$\\dfrac{5}{5}$', '$\\dfrac{-5}{10}$'],
            'answer': 1,
            'solution': '$\\dfrac{-2}{5} + \\dfrac{3}{5} = \\dfrac{-2 + 3}{5} = \\dfrac{1}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $\\dfrac{-3}{4} \\cdot \\dfrac{2}{9}$ là:',
            'options': ['$\\dfrac{1}{6}$', '$\\dfrac{-6}{13}$', '$\\dfrac{-1}{6}$', '$\\dfrac{-27}{8}$'],
            'answer': 2,
            'solution': '$\\dfrac{-3}{4} \\cdot \\dfrac{2}{9} = \\dfrac{-6}{36} = \\dfrac{-1}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 2: Cộng, trừ, nhân, chia số hữu tỉ**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Phép cộng, trừ cùng mẫu dương**?',
            'options': ['$\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d} \\quad (b, d '
                        '\\neq 0)$',
                        '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\cdot \\dfrac{d}{c} = \\dfrac{a '
                        '\\cdot d}{b \\cdot c} \\quad (b, c, d \\neq 0)$',
                        '$x \\cdot (y + z) = x \\cdot y + x \\cdot z; \\quad x \\cdot (y - z) = x \\cdot y - '
                        'x \\cdot z$',
                        '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a+b}{m}; \\quad \\dfrac{a}{m} - '
                        '\\dfrac{b}{m} = \\dfrac{a-b}{m} \\quad (m > 0)$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 2: Cộng, trừ, nhân, chia số hữu tỉ, **Phép '
                        'cộng, trừ cùng mẫu dương** được xác định bởi: $\\dfrac{a}{m} + \\dfrac{b}{m} = '
                        '\\dfrac{a+b}{m}; \\quad \\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a-b}{m} \\quad (m > '
                        '0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Cộng, trừ, nhân, chia số hữu tỉ**, nội dung/biểu thức $\\dfrac{a}{b} \\cdot '
                 '\\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d} \\quad (b, d \\neq 0)$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Phép nhân hai số hữu tỉ',
                        'Phép cộng, trừ cùng mẫu dương',
                        'Phép chia hai số hữu tỉ',
                        'Tính chất phân phối'],
            'answer': 0,
            'solution': 'Trong Bài 2: Cộng, trừ, nhân, chia số hữu tỉ, biểu thức/quy tắc $\\dfrac{a}{b} '
                        '\\cdot \\dfrac{c}{d} = \\dfrac{a \\cdot c}{b \\cdot d} \\quad (b, d \\neq 0)$ chính '
                        'là nội dung của **Phép nhân hai số hữu tỉ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\dfrac{3}{5} - \\dfrac{1}{2} : \\dfrac{5}{4}$ bằng:',
            'options': ['$\\dfrac{2}{5}$', '$\\dfrac{1}{5}$', '$\\dfrac{1}{10}$', '$\\dfrac{-1}{5}$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{3}{5} - \\dfrac{1}{2} \\cdot \\dfrac{4}{5} = \\dfrac{3}{5} - '
                        '\\dfrac{2}{5} = \\dfrac{1}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Cộng, trừ, nhân, chia số hữu tỉ** (Chương I: Số hữu tỉ), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Thực hiện được các phép tính cộng, trừ, nhân, chia trong tập hợp số hữu tỉ '
                        '$\\mathbb{Q}$.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 2: Cộng, trừ, nhân, chia số hữu tỉ: Thực hiện được các '
                        'phép tính cộng, trừ, nhân, chia trong tập hợp số hữu tỉ $\\mathbb{Q}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai số hữu tỉ $x = \\dfrac{-3}{4}$ và $y = \\dfrac{2}{3}$. Xét các khẳng định sau:',
            'statements': ['Tổng của $x$ và $y$ là $x + y = \\dfrac{-1}{12}$.',
                           'Hiệu của $x$ và $y$ là $x - y = \\dfrac{-17}{12}$.',
                           'Tích của $x$ và $y$ là $x \\cdot y = \\dfrac{1}{2}$.',
                           'Thương của $x$ chia cho $y$ là $x : y = \\dfrac{-9}{8}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) $x + y = \\dfrac{-9}{12} + \\dfrac{8}{12} = \\dfrac{-1}{12}$ (Đúng). b) $x - y = '
                        '\\dfrac{-9}{12} - \\dfrac{8}{12} = \\dfrac{-17}{12}$ (Đúng). c) $x \\cdot y = '
                        '\\dfrac{-3}{4} \\cdot \\dfrac{2}{3} = \\dfrac{-1}{2} \\neq \\dfrac{1}{2}$ (Sai). d) '
                        '$x : y = \\dfrac{-3}{4} \\cdot \\dfrac{3}{2} = \\dfrac{-9}{8}$ (Đúng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 2: Cộng, trừ, nhân, '
                 'chia số hữu tỉ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được các phép tính cộng, '
                           'trừ, nhân, chia trong tập hợp số hữu tỉ $\\mathbb{Q}$.',
                           'Quy tắc/công thức **Phép cộng, trừ cùng mẫu dương** trong bài được xác định bởi: '
                           '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a+b}{m}; \\quad \\dfrac{a}{m} - '
                           '\\dfrac{b}{m} = \\dfrac{a-b}{m} \\quad (m > 0)$.',
                           'Trong mọi trường hợp, **Phép cộng, trừ cùng mẫu dương** luôn được tính bằng công '
                           'thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 2: Cộng, trừ, nhân, chia số hữu tỉ.',
                           'Với bài toán minh họa: “Tính một cách hợp lí: $A = \\dfrac{-3}{7} \\cdot '
                           '\\dfrac{5}{9} + \\dfrac{-3}{7} \\cdot \\dfrac{4}{9} + 1\\dfrac{3}{7}$.”, lời '
                           'giải đúng là: Áp dụng tính chất phân phối của phép nhân đối với phép cộng...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Cộng, trừ, nhân, chia số hữu tỉ. b) '
                        '**Đúng** theo công thức trọng tâm **Phép cộng, trừ cùng mẫu dương** ($\\dfrac{a}{m} '
                        '+ \\dfrac{b}{m} = \\dfrac{a+b}{m}; \\quad \\dfrac{a}{m} - \\dfrac{b}{m} = '
                        '\\dfrac{a-b}{m} \\quad (m > 0)$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Phép cộng, trừ cùng mẫu '
                        'dương**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 2: Cộng, trừ, nhân, chia số hữu tỉ** để giải quyết tình huống '
                 'sau: Tính một cách hợp lí: $A = \\dfrac{-3}{7} \\cdot \\dfrac{5}{9} + \\dfrac{-3}{7} '
                 '\\cdot \\dfrac{4}{9} + 1\\dfrac{3}{7}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Ta có: $\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$. '
                        'Đẳng thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$. Áp '
                        'dụn...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Cộng, trừ, nhân, chia số hữu tỉ: Áp dụng tính chất '
                        'phân phối của phép nhân đối với phép cộng:\n'
                        '$A = \\dfrac{-3}{7} \\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + '
                        '\\dfrac{10}{7} = \\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $P = \\dfrac{7}{13} \\cdot \\dfrac{5}{12} + \\dfrac{7}{13} '
                 '\\cdot \\dfrac{7}{12} + \\dfrac{6}{13}$.',
            'answer': ['1'],
            'unit': None,
            'solution': '$P = \\dfrac{7}{13} \\cdot \\left(\\dfrac{5}{12} + \\dfrac{7}{12}\\right) + '
                        '\\dfrac{6}{13} = \\dfrac{7}{13} \\cdot 1 + \\dfrac{6}{13} = \\dfrac{13}{13} = 1$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch01-so-huu-ti',
  'context_title': 'Chương I: Số hữu tỉ',
  'context': 'Chương I · SGK Toán 7: Tập hợp các số hữu tỉ và các phép tính cộng, trừ, nhân, chia, lũy thừa.',
  'title': 'Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ',
  'icon': '⚡',
  'description': 'Định nghĩa lũy thừa với số mũ tự nhiên và các phép tính tích, thương hai lũy thừa cùng cơ '
                 'số, lũy thừa của lũy thừa.',
  'requirements': ['Mô tả được phép tính lũy thừa với số mũ tự nhiên của một số hữu tỉ.',
                   'Thực hiện được các phép tính: nhân, chia hai lũy thừa cùng cơ số, tính lũy thừa của một '
                   'lũy thừa, lũy thừa của một tích và một thương.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Lũy thừa của phân số** '
                   '($\\left(\\dfrac{a}{b}\\right)^n = \\dfrac{a^n}{b^n} \\quad (b \\neq 0, n \\in '
                   '\\mathbb{N})$) vào giải bài tập.'],
  'definition': 'Lũy thừa bậc $n$ của một số hữu tỉ $x$, kí hiệu $x^n$, là tích của $n$ thừa số $x$ ($n$ là '
                'số tự nhiên lớn hơn $1$): $x^n = \\underbrace{x \\cdot x \\cdots x}_{n \\text{ thừa số } '
                'x}$.',
  'theory': '1. Quy ước: $x^1 = x$ và $x^0 = 1$ ($x \\neq 0$). Khi viết số hữu tỉ $x$ dưới dạng phân số '
            '$\\dfrac{a}{b}$ ($a, b \\in \\mathbb{Z}, b \\neq 0$), ta có $\\left(\\dfrac{a}{b}\\right)^n = '
            '\\dfrac{a^n}{b^n}$.\n'
            '2. Nhân và chia hai lũy thừa cùng cơ số: Khi nhân hai lũy thừa cùng cơ số, ta giữ nguyên cơ số '
            'và cộng hai số mũ. Khi chia hai lũy thừa cùng cơ số khác $0$, ta giữ nguyên cơ số và lấy số mũ '
            'của lũy thừa bị chia trừ đi số mũ của lũy thừa chia.\n'
            '3. Lũy thừa của lũy thừa: Khi tính lũy thừa của một lũy thừa, ta giữ nguyên cơ số và nhân hai '
            'số mũ.',
  'formulas': [{'category': 'Các công thức lũy thừa của số hữu tỉ',
                'items': [{'name': 'Lũy thừa của phân số',
                           'formula': '$\\left(\\dfrac{a}{b}\\right)^n = \\dfrac{a^n}{b^n} \\quad (b \\neq '
                                      '0, n \\in \\mathbb{N})$'},
                          {'name': 'Nhân hai lũy thừa cùng cơ số',
                           'formula': '$x^m \\cdot x^n = x^{m+n} \\quad (m, n \\in \\mathbb{N})$'},
                          {'name': 'Chia hai lũy thừa cùng cơ số',
                           'formula': '$x^m : x^n = x^{m-n} \\quad (x \\neq 0, m \\ge n)$'},
                          {'name': 'Lũy thừa của lũy thừa',
                           'formula': '$\\left(x^m\\right)^n = x^{m \\cdot n}$'},
                          {'name': 'Lũy thừa của một tích, thương',
                           'formula': '$(x \\cdot y)^n = x^n \\cdot y^n; \\quad '
                                      '\\left(\\dfrac{x}{y}\\right)^n = \\dfrac{x^n}{y^n} \\quad (y \\neq '
                                      '0)$'}]}],
  'example': 'Rút gọn và tính giá trị của biểu thức $M = \\dfrac{8^{10}}{4^8}$ và $N = (0,125)^3 \\cdot '
             '8^3$.',
  'example_answer': 'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = 2^{14} '
                    '= 16384$.\n'
                    '$N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
  'real_life': 'Tính lãi kép ngân hàng qua nhiều kì hạn hoặc biểu diễn kích thước siêu nhỏ của vi khuẩn, '
               'nguyên tử trong khoa học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của lũy thừa $\\left(\\dfrac{-2}{3}\\right)^3$ là:',
            'options': ['$\\dfrac{8}{27}$', '$\\dfrac{-6}{9}$', '$\\dfrac{-8}{27}$', '$\\dfrac{-8}{9}$'],
            'answer': 2,
            'solution': '$\\left(\\dfrac{-2}{3}\\right)^3 = \\dfrac{(-2)^3}{3^3} = \\dfrac{-8}{27}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Với $x \\neq 0$, kết quả của phép tính $x^7 : x^2$ viết dưới dạng một lũy thừa là:',
            'options': ['$x^9$', '$x^{14}$', '$x^0$', '$x^5$'],
            'answer': 3,
            'solution': 'Áp dụng quy tắc chia hai lũy thừa cùng cơ số: $x^7 : x^2 = x^{7-2} = x^5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Lũy thừa của phân số**?',
            'options': ['$\\left(\\dfrac{a}{b}\\right)^n = \\dfrac{a^n}{b^n} \\quad (b \\neq 0, n \\in '
                        '\\mathbb{N})$',
                        '$x^m \\cdot x^n = x^{m+n} \\quad (m, n \\in \\mathbb{N})$',
                        '$x^m : x^n = x^{m-n} \\quad (x \\neq 0, m \\ge n)$',
                        '$\\left(x^m\\right)^n = x^{m \\cdot n}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu '
                        'tỉ, **Lũy thừa của phân số** được xác định bởi: $\\left(\\dfrac{a}{b}\\right)^n = '
                        '\\dfrac{a^n}{b^n} \\quad (b \\neq 0, n \\in \\mathbb{N})$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ**, nội dung/biểu thức $x^m '
                 '\\cdot x^n = x^{m+n} \\quad (m, n \\in \\mathbb{N})$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Lũy thừa của phân số',
                        'Nhân hai lũy thừa cùng cơ số',
                        'Chia hai lũy thừa cùng cơ số',
                        'Lũy thừa của lũy thừa'],
            'answer': 1,
            'solution': 'Trong Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ, biểu thức/quy tắc $x^m '
                        '\\cdot x^n = x^{m+n} \\quad (m, n \\in \\mathbb{N})$ chính là nội dung của **Nhân '
                        'hai lũy thừa cùng cơ số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $\\left[\\left(\\dfrac{-1}{2}\\right)^2\\right]^3$ bằng:',
            'options': ['$\\dfrac{-1}{64}$', '$\\dfrac{1}{32}$', '$\\dfrac{1}{64}$', '$\\dfrac{-1}{32}$'],
            'answer': 2,
            'solution': 'Ta có $\\left[\\left(\\dfrac{-1}{2}\\right)^2\\right]^3 = '
                        '\\left(\\dfrac{-1}{2}\\right)^6 = \\dfrac{1}{64}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ** (Chương I: Số hữu tỉ), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Mô tả được phép tính lũy thừa với số mũ tự nhiên của một số hữu tỉ.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ: Mô '
                        'tả được phép tính lũy thừa với số mũ tự nhiên của một số hữu tỉ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau với mọi số hữu tỉ $x \\neq 0$:',
            'statements': ['Giá trị của $x^0$ luôn bằng $1$.',
                           '$\\left(\\dfrac{-1}{3}\\right)^4 = \\dfrac{-1}{81}$.',
                           '$\\left(0,25\\right)^5 \\cdot 4^5 = 1$.',
                           'Nếu $x^2 = \\dfrac{4}{9}$ thì $x = \\dfrac{2}{3}$ hoặc $x = \\dfrac{-2}{3}$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng theo quy ước $x^0 = 1$ ($x \\neq 0$). b) Sai vì số mũ chẵn của số âm cho '
                        'kết quả dương: $\\left(\\dfrac{-1}{3}\\right)^4 = \\dfrac{1}{81}$. c) Đúng vì '
                        '$(0,25 \\cdot 4)^5 = 1^5 = 1$. d) Đúng vì $\\left(\\dfrac{2}{3}\\right)^2 = '
                        '\\left(\\dfrac{-2}{3}\\right)^2 = \\dfrac{4}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 3: Lũy thừa với số mũ '
                 'tự nhiên của một số hữu tỉ**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được phép tính lũy thừa với '
                           'số mũ tự nhiên của một số hữu tỉ.',
                           'Quy tắc/công thức **Lũy thừa của phân số** trong bài được xác định bởi: '
                           '$\\left(\\dfrac{a}{b}\\right)^n = \\dfrac{a^n}{b^n} \\quad (b \\neq 0, n \\in '
                           '\\mathbb{N})$.',
                           'Trong mọi trường hợp, **Lũy thừa của phân số** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ.',
                           'Với bài toán minh họa: “Rút gọn và tính giá trị của biểu thức $M = '
                           '\\dfrac{8^{10}}{4^8}$ và $N = (0,125)^3 \\cdot 8^3$.”, lời giải đúng là: Ta có: '
                           '$M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = 2^{14} '
                           '= 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Lũy thừa với số mũ tự nhiên của một số '
                        'hữu tỉ. b) **Đúng** theo công thức trọng tâm **Lũy thừa của phân số** '
                        '($\\left(\\dfrac{a}{b}\\right)^n = \\dfrac{a^n}{b^n} \\quad (b \\neq 0, n \\in '
                        '\\mathbb{N})$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Lũy thừa của phân số**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ** để giải quyết '
                 'tình huống sau: Rút gọn và tính giá trị của biểu thức $M = \\dfrac{8^{10}}{4^8}$ và $N = '
                 '(0,125)^3 \\cdot 8^3$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$. '
                        'Đẳng thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$. Áp '
                        'dụn...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ: Ta có: '
                        '$M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = 2^{14} = '
                        '16384$.\n'
                        '$N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tự nhiên $n$ biết $\\left(\\dfrac{1}{3}\\right)^n = \\dfrac{1}{81}$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{1}{81} = \\left(\\dfrac{1}{3}\\right)^4$, suy ra $n = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch01-so-huu-ti',
  'context_title': 'Chương I: Số hữu tỉ',
  'context': 'Chương I · SGK Toán 7: Tập hợp các số hữu tỉ và các phép tính cộng, trừ, nhân, chia, lũy thừa.',
  'title': 'Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế',
  'icon': '🔄',
  'description': 'Thứ tự thực hiện các phép tính trong biểu thức số hữu tỉ và vận dụng quy tắc chuyển vế để '
                 'tìm thành phần chưa biết.',
  'requirements': ['Mô tả được thứ tự thực hiện các phép tính trong biểu thức chứa số hữu tỉ.',
                   'Mô tả được quy tắc dấu ngoặc và quy tắc chuyển vế trong đẳng thức số hữu tỉ.',
                   'Vận dụng quy tắc chuyển vế và thứ tự phép tính để giải các bài toán tìm $x$ và bài toán '
                   'thực tế.'],
  'definition': 'Khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải đổi dấu số hạng đó: '
                'dấu $+$ đổi thành dấu $-$ và dấu $-$ đổi thành dấu $+$.',
  'theory': '1. Thứ tự thực hiện các phép tính:\n'
            '- Đối với biểu thức không có dấu ngoặc: Nếu chỉ có phép cộng, trừ hoặc chỉ có phép nhân, chia '
            'thì thực hiện từ trái sang phải. Nếu có các phép tính cộng, trừ, nhân, chia, nâng lên lũy thừa '
            'thì thực hiện: Lũy thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ.\n'
            '- Đối với biểu thức có dấu ngoặc: Thực hiện theo thứ tự: Ngoặc tròn $()$ $\\rightarrow$ Ngoặc '
            'vuông $[]$ $\\rightarrow$ Ngoặc nhọn $\\{\\}$.\n'
            '2. Quy tắc chuyển vế: Với mọi $x, y, z \\in \\mathbb{Q}$: Nếu $x + y = z$ thì $x = z - y$; nếu '
            '$x - y = z$ thì $x = z + y$.',
  'formulas': [{'category': 'Quy tắc chuyển vế và dấu ngoặc',
                'items': [{'name': 'Quy tắc chuyển vế (cộng sang trừ)',
                           'formula': '$x + y = z \\Rightarrow x = z - y$'},
                          {'name': 'Quy tắc chuyển vế (trừ sang cộng)',
                           'formula': '$x - y = z \\Rightarrow x = z + y$'},
                          {'name': 'Quy tắc bỏ dấu ngoặc có dấu trừ đằng trước',
                           'formula': '$-(a + b - c) = -a - b + c$'}]}],
  'example': 'Tìm $x$, biết: $x - \\left(\\dfrac{5}{4} - \\dfrac{7}{5}\\right) = \\dfrac{9}{20}$.',
  'example_answer': 'Ta có: $\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$.\n'
                    'Đẳng thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$.\n'
                    'Áp dụng quy tắc chuyển vế: $x = \\dfrac{9}{20} + \\left(\\dfrac{-3}{20}\\right) = '
                    '\\dfrac{6}{20} = \\dfrac{3}{10}$.',
  'real_life': 'Cân bằng phương trình thu chi tài chính cá nhân để tìm khoản tiền còn thiếu hoặc số tiền '
               'tiết kiệm được.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đối với biểu thức không có dấu ngoặc, thứ tự thực hiện các phép tính đúng là:',
            'options': ['Nhân và chia $\\rightarrow$ Lũy thừa $\\rightarrow$ Cộng và trừ',
                        'Cộng và trừ $\\rightarrow$ Nhân và chia $\\rightarrow$ Lũy thừa',
                        'Thực hiện từ trái sang phải không phân biệt phép tính',
                        'Lũy thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ'],
            'answer': 3,
            'solution': 'Thứ tự ưu tiên chuẩn là: Lũy thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng '
                        'và trừ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đẳng thức $x - \\dfrac{2}{5} = \\dfrac{1}{5}$. Áp dụng quy tắc chuyển vế ta được:',
            'options': ['$x = \\dfrac{1}{5} + \\dfrac{2}{5}$',
                        '$x = \\dfrac{1}{5} - \\dfrac{2}{5}$',
                        '$x = \\dfrac{2}{5} - \\dfrac{1}{5}$',
                        '$x = -\\dfrac{1}{5} - \\dfrac{2}{5}$'],
            'answer': 0,
            'solution': 'Chuyển $-\\dfrac{2}{5}$ từ vế trái sang vế phải và đổi dấu thành $+\\dfrac{2}{5}$: '
                        '$x = \\dfrac{1}{5} + \\dfrac{2}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Quy tắc chuyển vế (cộng sang trừ)**?',
            'options': ['$x - y = z \\Rightarrow x = z + y$',
                        '$x + y = z \\Rightarrow x = z - y$',
                        '$-(a + b - c) = -a - b + c$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 4: Thứ tự thực hiện các phép tính. Quy tắc '
                        'chuyển vế, **Quy tắc chuyển vế (cộng sang trừ)** được xác định bởi: $x + y = z '
                        '\\Rightarrow x = z - y$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế**, nội dung/biểu thức $x '
                 '- y = z \\Rightarrow x = z + y$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quy tắc chuyển vế (cộng sang trừ)',
                        'Quy tắc bỏ dấu ngoặc có dấu trừ đằng trước',
                        'Quy tắc chuyển vế (trừ sang cộng)',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế, biểu thức/quy tắc '
                        '$x - y = z \\Rightarrow x = z + y$ chính là nội dung của **Quy tắc chuyển vế (trừ '
                        'sang cộng)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của $x$ thỏa mãn $\\dfrac{3}{4} - 2x = \\dfrac{1}{4}$ là:',
            'options': ['$\\dfrac{1}{2}$', '$\\dfrac{-1}{4}$', '$1$', '$\\dfrac{1}{4}$'],
            'answer': 3,
            'solution': 'Ta có $2x = \\dfrac{3}{4} - \\dfrac{1}{4} = \\dfrac{1}{2}$, suy ra $x = '
                        '\\dfrac{1}{2} : 2 = \\dfrac{1}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế** (Chương I: Số hữu '
                 'tỉ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Mô tả được thứ tự thực hiện các phép tính trong biểu thức chứa số hữu tỉ.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế: '
                        'Mô tả được thứ tự thực hiện các phép tính trong biểu thức chứa số hữu tỉ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $A = 1,5 - \\left[\\left(\\dfrac{-1}{2}\\right)^2 + 0,25\\right] \\cdot 2$. '
                 'Xét các khẳng định sau:',
            'statements': ['Ta thực hiện phép lũy thừa $\\left(\\dfrac{-1}{2}\\right)^2 = \\dfrac{1}{4}$ '
                           'trước tiên.',
                           'Giá trị trong ngoặc vuông là $\\dfrac{1}{4} + 0,25 = 0,5$.',
                           'Ta lấy $1,5 - 0,5$ trước rồi mới nhân với $2$.',
                           'Giá trị cuối cùng của biểu thức $A$ bằng $0,5$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $0,25 + 0,25 = 0,5$. c) Sai vì phải thực hiện phép nhân $0,5 '
                        '\\cdot 2 = 1$ trước phép trừ. d) Đúng vì $A = 1,5 - 1 = 0,5$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 4: Thứ tự thực hiện các '
                 'phép tính. Quy tắc chuyển vế**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được thứ tự thực hiện các '
                           'phép tính trong biểu thức chứa số hữu tỉ.',
                           'Quy tắc/công thức **Quy tắc chuyển vế (cộng sang trừ)** trong bài được xác định '
                           'bởi: $x + y = z \\Rightarrow x = z - y$.',
                           'Trong mọi trường hợp, **Quy tắc chuyển vế (cộng sang trừ)** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế.',
                           'Với bài toán minh họa: “Tìm $x$, biết: $x - \\left(\\dfrac{5}{4} - '
                           '\\dfrac{7}{5}\\right) = \\dfrac{9}{20}$.”, lời giải đúng là: Ta có: '
                           '$\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$. Đẳng '
                           'thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Thứ tự thực hiện các phép tính. Quy tắc '
                        'chuyển vế. b) **Đúng** theo công thức trọng tâm **Quy tắc chuyển vế (cộng sang '
                        'trừ)** ($x + y = z \\Rightarrow x = z - y$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Quy tắc chuyển vế (cộng sang '
                        'trừ)**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế** để giải '
                 'quyết tình huống sau: Tìm $x$, biết: $x - \\left(\\dfrac{5}{4} - \\dfrac{7}{5}\\right) = '
                 '\\dfrac{9}{20}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Ta có: $\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$. '
                        'Đẳng thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$. Áp '
                        'dụn...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế: Ta '
                        'có: $\\dfrac{5}{4} - \\dfrac{7}{5} = \\dfrac{25 - 28}{20} = \\dfrac{-3}{20}$.\n'
                        'Đẳng thức trở thành: $x - \\left(\\dfrac{-3}{20}\\right) = \\dfrac{9}{20}$.\n'
                        'Áp dụng quy tắc chuyển vế: $x = \\dfrac{9}{20} + \\left(\\dfrac{-3}{20}\\right) = '
                        '\\dfrac{6}{20} = \\dfrac{3}{10}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm $x$ (viết dưới dạng số thập phân) biết: $2,5x + 1,5 = 9$.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Ta có $2,5x = 9 - 1,5 = 7,5 \\Rightarrow x = 7,5 : 2,5 = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch02-so-thuc',
  'context_title': 'Chương II: Số thực',
  'context': 'Chương II · SGK Toán 7: Số thập phân vô hạn tuần hoàn, số vô tỉ, căn bậc hai số học và tập hợp '
             'số thực.',
  'title': 'Bài 5: Làm quen với số thập phân vô hạn tuần hoàn',
  'icon': '♾️',
  'description': 'Nhận biết số thập phân hữu hạn, số thập phân vô hạn tuần hoàn và quy tắc làm tròn số thập '
                 'phân theo độ chính xác cho trước.',
  'requirements': ['Nhận biết được số thập phân hữu hạn và số thập phân vô hạn tuần hoàn.',
                   'Nhận biết được chu kì của số thập phân vô hạn tuần hoàn và cách viết gọn.',
                   'Thực hiện được việc làm tròn số thập phân căn cứ vào độ chính xác cho trước.'],
  'definition': 'Số thập phân có phần thập phân lặp lại mãi một nhóm chữ số không bao giờ kết thúc được gọi '
                'là số thập phân vô hạn tuần hoàn; phần lặp lại đó gọi là chu kì và được đặt trong dấu ngoặc '
                'đơn.',
  'theory': '1. Số thập phân hữu hạn và vô hạn tuần hoàn:\n'
            '- Nếu một phân số tối giản với mẫu dương mà mẫu không có ước nguyên tố khác $2$ và $5$ thì phân '
            'số đó viết được dưới dạng số thập phân hữu hạn.\n'
            '- Nếu một phân số tối giản với mẫu dương mà mẫu có ước nguyên tố khác $2$ và $5$ thì phân số đó '
            'viết được dưới dạng số thập phân vô hạn tuần hoàn. Mọi số hữu tỉ đều viết được dưới dạng số '
            'thập phân hữu hạn hoặc vô hạn tuần hoàn.\n'
            '2. Làm tròn số căn cứ vào độ chính xác $d$: Nếu $d = 50$ thì làm tròn đến hàng trăm; nếu $d = '
            '5$ thì làm tròn đến hàng chục; nếu $d = 0,5$ thì làm tròn đến hàng đơn vị; nếu $d = 0,05$ thì '
            'làm tròn đến hàng phần mười; nếu $d = 0,005$ thì làm tròn đến hàng phần trăm.',
  'formulas': [{'category': 'Biểu diễn thập phân và làm tròn số',
                'items': [{'name': 'Cách viết gọn chu kì',
                           'formula': '$0,333\\ldots = 0,(3); \\quad -1,24545\\ldots = -1,2(45)$'},
                          {'name': 'Đổi chu kì đơn giản ra phân số',
                           'formula': '$0,(1) = \\dfrac{1}{9}; \\quad 0,(a) = \\dfrac{a}{9}$ với $a \\in '
                                      '\\{1; 2; \\ldots; 8\\}$'},
                          {'name': 'Độ chính xác $d = 0,05$',
                           'formula': 'Làm tròn số đến hàng phần mười (chữ số thập phân thứ nhất)'},
                          {'name': 'Độ chính xác $d = 0,005$',
                           'formula': 'Làm tròn số đến hàng phần trăm (chữ số thập phân thứ hai)'}]}],
  'example': 'Viết phân số $\\dfrac{5}{12}$ dưới dạng số thập phân vô hạn tuần hoàn và làm tròn kết quả với '
             'độ chính xác $0,005$.',
  'example_answer': 'Chia tử cho mẫu ta được $\\dfrac{5}{12} = 0,41666\\ldots = 0,41(6)$.\n'
                    'Làm tròn $0,41666\\ldots$ với độ chính xác $0,005$ tức là làm tròn đến hàng phần trăm: '
                    'ta được $0,42$.',
  'real_life': 'Làm tròn điểm trung bình môn học (ví dụ: $8,666\\ldots \\approx 8,7$) hoặc làm tròn số liệu '
               'đo đạc trong phòng thí nghiệm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cách viết gọn của số thập phân vô hạn tuần hoàn $2,151515\\ldots$ là:',
            'options': ['$2,(15)$', '$2,1(5)$', '$2,(151)$', '$2,15(15)$'],
            'answer': 0,
            'solution': 'Phần lặp lại mãi là $15$ ngay sau dấu phẩy nên viết gọn là $2,(15)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số nào sau đây viết được dưới dạng số thập phân hữu hạn?',
            'options': ['$\\dfrac{5}{6}$', '$\\dfrac{3}{8}$', '$\\dfrac{7}{15}$', '$\\dfrac{2}{9}$'],
            'answer': 1,
            'solution': 'Phân số tối giản $\\dfrac{3}{8}$ có mẫu $8 = 2^3$ chỉ có ước nguyên tố là $2$ nên '
                        'viết được dưới dạng số thập phân hữu hạn ($0,375$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 5: Làm quen với số thập phân vô hạn tuần hoàn**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Cách viết gọn chu kì**?',
            'options': ['$0,(1) = \\dfrac{1}{9}; \\quad 0,(a) = \\dfrac{a}{9}$ với $a \\in \\{1; 2; \\ldots; '
                        '8\\}$',
                        'Làm tròn số đến hàng phần mười (chữ số thập phân thứ nhất)',
                        '$0,333\\ldots = 0,(3); \\quad -1,24545\\ldots = -1,2(45)$',
                        'Làm tròn số đến hàng phần trăm (chữ số thập phân thứ hai)'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 5: Làm quen với số thập phân vô hạn tuần '
                        'hoàn, **Cách viết gọn chu kì** được xác định bởi: $0,333\\ldots = 0,(3); \\quad '
                        '-1,24545\\ldots = -1,2(45)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Làm quen với số thập phân vô hạn tuần hoàn**, nội dung/biểu thức $0,(1) = '
                 '\\dfrac{1}{9}; \\quad 0,(a) = \\dfrac{a}{9}$ với $a \\in \\{1; 2; \\ldots; 8\\}$ là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cách viết gọn chu kì',
                        'Độ chính xác $d = 0,05$',
                        'Độ chính xác $d = 0,005$',
                        'Đổi chu kì đơn giản ra phân số'],
            'answer': 3,
            'solution': 'Trong Bài 5: Làm quen với số thập phân vô hạn tuần hoàn, biểu thức/quy tắc $0,(1) = '
                        '\\dfrac{1}{9}; \\quad 0,(a) = \\dfrac{a}{9}$ với $a \\in \\{1; 2; \\ldots; 8\\}$ '
                        'chính là nội dung của **Đổi chu kì đơn giản ra phân số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Làm tròn số $3,14159$ với độ chính xác $0,005$ ta được kết quả là:',
            'options': ['$3,14$', '$3,142$', '$3,1$', '$3,15$'],
            'answer': 0,
            'solution': 'Độ chính xác $0,005$ tương ứng với việc làm tròn đến hàng phần trăm: $3,14159 '
                        '\\approx 3,14$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Làm quen với số thập phân vô hạn tuần hoàn** (Chương II: Số thực), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Nhận biết được số thập phân hữu hạn và số thập phân vô hạn tuần hoàn.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 5: Làm quen với số thập phân vô hạn tuần hoàn: Nhận '
                        'biết được số thập phân hữu hạn và số thập phân vô hạn tuần hoàn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau:',
            'statements': ['Phân số $\\dfrac{1}{3}$ viết dưới dạng số thập phân là $0,(3)$.',
                           'Mọi số thập phân vô hạn tuần hoàn đều là số hữu tỉ.',
                           'Làm tròn số $124,56$ với độ chính xác $0,5$ ta được $124,6$.',
                           'Số $0,(7)$ viết dưới dạng phân số tối giản là $\\dfrac{7}{9}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì độ chính xác $0,5$ là làm tròn đến hàng đơn vị, kết quả '
                        'phải là $125$. d) Đúng vì $0,(7) = 7 \\cdot 0,(1) = \\dfrac{7}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 5: Làm quen với số thập '
                 'phân vô hạn tuần hoàn**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được số thập phân hữu '
                           'hạn và số thập phân vô hạn tuần hoàn.',
                           'Quy tắc/công thức **Cách viết gọn chu kì** trong bài được xác định bởi: '
                           '$0,333\\ldots = 0,(3); \\quad -1,24545\\ldots = -1,2(45)$.',
                           'Trong mọi trường hợp, **Cách viết gọn chu kì** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 5: Làm quen với số thập phân vô hạn tuần hoàn.',
                           'Với bài toán minh họa: “Viết phân số $\\dfrac{5}{12}$ dưới dạng số thập phân vô '
                           'hạn tuần hoàn và làm tròn kết quả với độ chính xác $0,005$.”, lời giải đúng là: '
                           'Chia tử cho mẫu ta được $\\dfrac{5}{12} = 0,41666\\ldots = 0,41(6)$. Làm tròn '
                           '$0,41666\\ldots$ với độ chính xác $0,005$ tức là làm tròn đến hàn...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Làm quen với số thập phân vô hạn tuần '
                        'hoàn. b) **Đúng** theo công thức trọng tâm **Cách viết gọn chu kì** ($0,333\\ldots '
                        '= 0,(3); \\quad -1,24545\\ldots = -1,2(45)$). c) **Sai** vì $\\mathbb{Q} = '
                        '\\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 '
                        '\\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của **Cách '
                        'viết gọn chu kì**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 5: Làm quen với số thập phân vô hạn tuần hoàn** để giải quyết '
                 'tình huống sau: Viết phân số $\\dfrac{5}{12}$ dưới dạng số thập phân vô hạn tuần hoàn và '
                 'làm tròn kết quả với độ chính xác $0,005$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Chia tử cho mẫu ta được $\\dfrac{5}{12} = 0,41666\\ldots = 0,41(6)$. Làm tròn '
                        '$0,41666\\ldots$ với độ chính xác $0,005$ tức là làm tròn đến hàng phần trăm: ta...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Làm quen với số thập phân vô hạn tuần hoàn: Chia tử '
                        'cho mẫu ta được $\\dfrac{5}{12} = 0,41666\\ldots = 0,41(6)$.\n'
                        'Làm tròn $0,41666\\ldots$ với độ chính xác $0,005$ tức là làm tròn đến hàng phần '
                        'trăm: ta được $0,42$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Làm tròn số $18,368$ với độ chính xác $0,05$ ta được số nào?',
            'answer': ['18,4', '18.4'],
            'unit': None,
            'solution': 'Độ chính xác $0,05$ là làm tròn đến hàng phần mười. Chữ số hàng phần trăm là $6 '
                        '\\ge 5$ nên $18,368 \\approx 18,4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch02-so-thuc',
  'context_title': 'Chương II: Số thực',
  'context': 'Chương II · SGK Toán 7: Số thập phân vô hạn tuần hoàn, số vô tỉ, căn bậc hai số học và tập hợp '
             'số thực.',
  'title': 'Bài 6: Số vô tỉ. Căn bậc hai số học',
  'icon': '√',
  'description': 'Khái niệm số vô tỉ, số thập phân vô hạn không tuần hoàn và căn bậc hai số học của một số '
                 'không âm.',
  'requirements': ['Nhận biết được số vô tỉ và lấy được ví dụ về số vô tỉ.',
                   'Nhận biết được khái niệm căn bậc hai số học của một số không âm.',
                   'Tính được giá trị (đúng hoặc gần đúng) căn bậc hai số học của một số nguyên dương.'],
  'definition': 'Số vô tỉ là số viết được dưới dạng số thập phân vô hạn không tuần hoàn. Tập hợp các số vô '
                'tỉ được kí hiệu là $\\mathbb{I}$. Căn bậc hai số học của một số $a$ không âm, kí hiệu là '
                '$\\sqrt{a}$, là số không âm $x$ sao cho $x^2 = a$.',
  'theory': '1. Số vô tỉ: Những số không phải là số hữu tỉ được gọi là số vô tỉ. Ví dụ: $\\sqrt{2} = '
            '1,41421356\\ldots$, số $\\pi = 3,14159265\\ldots$ là các số vô tỉ.\n'
            '2. Căn bậc hai số học: Với $a \\ge 0$, ta có $\\sqrt{a} \\ge 0$ và $(\\sqrt{a})^2 = a$. Số âm '
            'không có căn bậc hai số học.\n'
            '3. Tính chất: Với mọi số $a \\ge 0$, ta luôn có $\\sqrt{a^2} = a$.',
  'formulas': [{'category': 'Căn bậc hai số học',
                'items': [{'name': 'Định nghĩa căn bậc hai số học',
                           'formula': '$x = \\sqrt{a} \\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ x^2 = a '
                                      '\\end{cases} \\quad (a \\ge 0)$'},
                          {'name': 'Bình phương của căn bậc hai',
                           'formula': '$(\\sqrt{a})^2 = a \\quad (a \\ge 0)$'},
                          {'name': 'Căn bậc hai của bình phương số không âm',
                           'formula': '$\\sqrt{a^2} = a \\quad (a \\ge 0)$'}]}],
  'example': 'Tính giá trị của biểu thức $A = \\sqrt{81} - 2\\sqrt{25} + \\sqrt{(-4)^2}$.',
  'example_answer': 'Ta có: $\\sqrt{81} = 9$; $\\sqrt{25} = 5$; $\\sqrt{(-4)^2} = \\sqrt{16} = 4$.\n'
                    'Do đó $A = 9 - 2 \\cdot 5 + 4 = 9 - 10 + 4 = 3$.',
  'real_life': 'Tính độ dài cạnh của một mảnh đất hình vuông hoặc viên gạch hình vuông khi biết diện tích '
               'của nó.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Căn bậc hai số học của $49$ là:',
            'options': ['$-7$', '$7$', '$7$ và $-7$', '$2401$'],
            'answer': 1,
            'solution': 'Vì $7 > 0$ và $7^2 = 49$ nên căn bậc hai số học của $49$ là $\\sqrt{49} = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số nào trong các số sau đây là số vô tỉ?',
            'options': ['$\\sqrt{9}$', '$0,(3)$', '$\\sqrt{2}$', '$\\dfrac{-5}{7}$'],
            'answer': 2,
            'solution': '$\\sqrt{2} = 1,4142135\\ldots$ là số thập phân vô hạn không tuần hoàn nên là số vô '
                        'tỉ. Các số còn lại đều là số hữu tỉ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 6: Số vô tỉ. Căn bậc hai số học**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Định nghĩa căn bậc hai số học**?',
            'options': ['$(\\sqrt{a})^2 = a \\quad (a \\ge 0)$',
                        '$\\sqrt{a^2} = a \\quad (a \\ge 0)$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$x = \\sqrt{a} \\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ x^2 = a \\end{cases} '
                        '\\quad (a \\ge 0)$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 6: Số vô tỉ. Căn bậc hai số học, **Định nghĩa '
                        'căn bậc hai số học** được xác định bởi: $x = \\sqrt{a} \\Leftrightarrow '
                        '\\begin{cases} x \\ge 0 \\\\ x^2 = a \\end{cases} \\quad (a \\ge 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Số vô tỉ. Căn bậc hai số học**, nội dung/biểu thức $(\\sqrt{a})^2 = a '
                 '\\quad (a \\ge 0)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Bình phương của căn bậc hai',
                        'Định nghĩa căn bậc hai số học',
                        'Căn bậc hai của bình phương số không âm',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Trong Bài 6: Số vô tỉ. Căn bậc hai số học, biểu thức/quy tắc $(\\sqrt{a})^2 = a '
                        '\\quad (a \\ge 0)$ chính là nội dung của **Bình phương của căn bậc hai**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\sqrt{36} + \\sqrt{0,09}$ bằng:',
            'options': ['$6,03$', '$6,3$', '$0,63$', '$6,9$'],
            'answer': 1,
            'solution': 'Ta có $\\sqrt{36} = 6$ và $\\sqrt{0,09} = 0,3$. Vậy $\\sqrt{36} + \\sqrt{0,09} = 6 '
                        '+ 0,3 = 6,3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Số vô tỉ. Căn bậc hai số học** (Chương II: Số thực), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được số vô tỉ và lấy được ví dụ về số vô tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 6: Số vô tỉ. Căn bậc hai số học: Nhận biết được số vô '
                        'tỉ và lấy được ví dụ về số vô tỉ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau:',
            'statements': ['$\\sqrt{100} = 10$.',
                           '$\\sqrt{(-5)^2} = -5$.',
                           'Số $\\pi = 3,1415926\\ldots$ là một số vô tỉ.',
                           'Nếu $\\sqrt{x} = 4$ (với $x \\ge 0$) thì $x = 16$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì căn bậc hai số học luôn không âm: $\\sqrt{(-5)^2} = \\sqrt{25} = '
                        '5$. c) Đúng. d) Đúng vì $\\sqrt{x} = 4 \\Rightarrow x = 4^2 = 16$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 6: Số vô tỉ. Căn bậc '
                 'hai số học**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được số vô tỉ và lấy '
                           'được ví dụ về số vô tỉ.',
                           'Quy tắc/công thức **Định nghĩa căn bậc hai số học** trong bài được xác định bởi: '
                           '$x = \\sqrt{a} \\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ x^2 = a '
                           '\\end{cases} \\quad (a \\ge 0)$.',
                           'Trong mọi trường hợp, **Định nghĩa căn bậc hai số học** luôn được tính bằng công '
                           'thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 6: Số vô tỉ. Căn bậc hai số học.',
                           'Với bài toán minh họa: “Tính giá trị của biểu thức $A = \\sqrt{81} - 2\\sqrt{25} '
                           '+ \\sqrt{(-4)^2}$.”, lời giải đúng là: Ta có: $\\sqrt{81} = 9$; $\\sqrt{25} = '
                           '5$; $\\sqrt{(-4)^2} = \\sqrt{16} = 4$. Do đó $A = 9 - 2 \\cdot 5 + 4 = 9 - 10 + '
                           '4 = 3$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Số vô tỉ. Căn bậc hai số học. b) '
                        '**Đúng** theo công thức trọng tâm **Định nghĩa căn bậc hai số học** ($x = \\sqrt{a} '
                        '\\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ x^2 = a \\end{cases} \\quad (a \\ge '
                        '0)$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b '
                        '\\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không phải '
                        'quy tắc chung của **Định nghĩa căn bậc hai số học**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 6: Số vô tỉ. Căn bậc hai số học** để giải quyết tình huống sau: '
                 'Tính giá trị của biểu thức $A = \\sqrt{81} - 2\\sqrt{25} + \\sqrt{(-4)^2}$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Ta có: $\\sqrt{81} = 9$; $\\sqrt{25} = 5$; $\\sqrt{(-4)^2} = \\sqrt{16} = 4$. Do đó '
                        '$A = 9 - 2 \\cdot 5 + 4 = 9 - 10 + 4 = 3$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Số vô tỉ. Căn bậc hai số học: Ta có: $\\sqrt{81} = '
                        '9$; $\\sqrt{25} = 5$; $\\sqrt{(-4)^2} = \\sqrt{16} = 4$.\n'
                        'Do đó $A = 9 - 2 \\cdot 5 + 4 = 9 - 10 + 4 = 3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình vuông có diện tích bằng $144\\text{ cm}^2$. Độ dài cạnh của hình vuông đó bằng '
                 'bao nhiêu $\\text{cm}$?',
            'answer': ['12'],
            'unit': None,
            'solution': 'Độ dài cạnh hình vuông là $\\sqrt{144} = 12\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch02-so-thuc',
  'context_title': 'Chương II: Số thực',
  'context': 'Chương II · SGK Toán 7: Số thập phân vô hạn tuần hoàn, số vô tỉ, căn bậc hai số học và tập hợp '
             'số thực.',
  'title': 'Bài 7: Tập hợp các số thực và giá trị tuyệt đối',
  'icon': '📏',
  'description': 'Tập hợp các số thực, biểu diễn số thực trên trục số, thứ tự trong tập số thực và giá trị '
                 'tuyệt đối của một số thực.',
  'requirements': ['Nhận biết được số thực, tập hợp các số thực $\\mathbb{R}$ và trục số thực.',
                   'Nhận biết được số đối và thứ tự trong tập hợp các số thực.',
                   'Nhận biết và tính được giá trị tuyệt đối của một số thực.'],
  'definition': 'Số hữu tỉ và số vô tỉ được gọi chung là số thực. Tập hợp các số thực được kí hiệu là '
                '$\\mathbb{R}$. Khoảng cách từ điểm $a$ trên trục số đến điểm gốc $0$ được gọi là giá trị '
                'tuyệt đối của số thực $a$, kí hiệu là $|a|$.',
  'theory': '1. Tập hợp số thực và trục số thực: Mỗi số thực được biểu diễn bởi một điểm trên trục số; ngược '
            'lại, mỗi điểm trên trục số đều biểu diễn một số thực (các điểm số thực lấp đầy trục số).\n'
            '2. So sánh hai số thực: Với hai số thực không âm $a, b$, ta có: $a > b \\Leftrightarrow '
            '\\sqrt{a} > \\sqrt{b}$.\n'
            '3. Giá trị tuyệt đối của một số thực:\n'
            '- Giá trị tuyệt đối của số $0$ là $0$.\n'
            '- Giá trị tuyệt đối của một số dương là chính nó: $|a| = a$ nếu $a > 0$.\n'
            '- Giá trị tuyệt đối của một số âm là số đối của nó: $|a| = -a$ nếu $a < 0$.',
  'formulas': [{'category': 'Tập hợp số thực và giá trị tuyệt đối',
                'items': [{'name': 'Quan hệ các tập hợp số',
                           'formula': '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset '
                                      '\\mathbb{R}; \\quad \\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$'},
                          {'name': 'Định nghĩa giá trị tuyệt đối',
                           'formula': '$|a| = \\begin{cases} a & \\text{nếu } a \\ge 0 \\\\ -a & \\text{nếu '
                                      '} a < 0 \\end{cases}$'},
                          {'name': 'Tính chất giá trị tuyệt đối',
                           'formula': '$|a| \\ge 0; \\quad |-a| = |a|; \\quad \\sqrt{a^2} = |a|$ với mọi $a '
                                      '\\in \\mathbb{R}$'},
                          {'name': 'So sánh hai căn bậc hai',
                           'formula': 'Với $a, b \\ge 0$: $a < b \\Leftrightarrow \\sqrt{a} < \\sqrt{b}$'}]}],
  'example': 'Tìm tất cả các số thực $x$ thỏa mãn $|x - 1,5| = 2,5$.',
  'example_answer': 'Vì $|x - 1,5| = 2,5$ nên xảy ra hai trường hợp:\n'
                    '- Trường hợp 1: $x - 1,5 = 2,5 \\Rightarrow x = 2,5 + 1,5 = 4$.\n'
                    '- Trường hợp 2: $x - 1,5 = -2,5 \\Rightarrow x = -2,5 + 1,5 = -1$.\n'
                    'Vậy $x \\in \\{-1; 4\\}$.',
  'real_life': 'Tính độ chênh lệch nhiệt độ hoặc sai số tuyệt đối giữa kích thước thực tế của sản phẩm và '
               'kích thước thiết kế chuẩn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của $|-3,5|$ bằng:',
            'options': ['$-3,5$', '$0$', '$3,5$', '$7$'],
            'answer': 2,
            'solution': 'Giá trị tuyệt đối của số âm $-3,5$ là số đối của nó: $|-3,5| = 3,5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khẳng định nào sau đây là SAI?',
            'options': ['$\\sqrt{3} \\in \\mathbb{I}$',
                        '$\\sqrt{3} \\in \\mathbb{R}$',
                        '$-5 \\in \\mathbb{R}$',
                        '$\\sqrt{3} \\in \\mathbb{Q}$'],
            'answer': 3,
            'solution': '$\\sqrt{3}$ là số vô tỉ nên $\\sqrt{3} \\notin \\mathbb{Q}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 7: Tập hợp các số thực và giá trị tuyệt đối**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Quan hệ các tập hợp số**?',
            'options': ['$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}; \\quad '
                        '\\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$',
                        '$|a| = \\begin{cases} a & \\text{nếu } a \\ge 0 \\\\ -a & \\text{nếu } a < 0 '
                        '\\end{cases}$',
                        '$|a| \\ge 0; \\quad |-a| = |a|; \\quad \\sqrt{a^2} = |a|$ với mọi $a \\in '
                        '\\mathbb{R}$',
                        'Với $a, b \\ge 0$: $a < b \\Leftrightarrow \\sqrt{a} < \\sqrt{b}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 7: Tập hợp các số thực và giá trị tuyệt đối, '
                        '**Quan hệ các tập hợp số** được xác định bởi: $\\mathbb{N} \\subset \\mathbb{Z} '
                        '\\subset \\mathbb{Q} \\subset \\mathbb{R}; \\quad \\mathbb{R} = \\mathbb{Q} \\cup '
                        '\\mathbb{I}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Tập hợp các số thực và giá trị tuyệt đối**, nội dung/biểu thức $|a| = '
                 '\\begin{cases} a & \\text{nếu } a \\ge 0 \\\\ -a & \\text{nếu } a < 0 \\end{cases}$ là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quan hệ các tập hợp số',
                        'Định nghĩa giá trị tuyệt đối',
                        'Tính chất giá trị tuyệt đối',
                        'So sánh hai căn bậc hai'],
            'answer': 1,
            'solution': 'Trong Bài 7: Tập hợp các số thực và giá trị tuyệt đối, biểu thức/quy tắc $|a| = '
                        '\\begin{cases} a & \\text{nếu } a \\ge 0 \\\\ -a & \\text{nếu } a < 0 \\end{cases}$ '
                        'chính là nội dung của **Định nghĩa giá trị tuyệt đối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'So sánh hai số thực $4$ và $\\sqrt{15}$ ta được:',
            'options': ['$4 < \\sqrt{15}$', '$4 = \\sqrt{15}$', '$4 > \\sqrt{15}$', 'Không so sánh được'],
            'answer': 2,
            'solution': 'Ta có $4 = \\sqrt{16}$. Vì $16 > 15$ nên $\\sqrt{16} > \\sqrt{15}$, hay $4 > '
                        '\\sqrt{15}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Tập hợp các số thực và giá trị tuyệt đối** (Chương II: Số thực), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Nhận biết được số thực, tập hợp các số thực $\\mathbb{R}$ và trục số thực.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 7: Tập hợp các số thực và giá trị tuyệt đối: Nhận biết '
                        'được số thực, tập hợp các số thực $\\mathbb{R}$ và trục số thực.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau với mọi số thực $x$:',
            'statements': ['Giá trị tuyệt đối của $x$ luôn không âm ($|x| \\ge 0$).',
                           'Hai số thực đối nhau có giá trị tuyệt đối bằng nhau.',
                           'Phương trình $|x| = -2$ có hai nghiệm là $x = 2$ và $x = -2$.',
                           'Số đối của $\\sqrt{5}$ là $-\\sqrt{5}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $|-x| = |x|$. c) Sai vì $|x| \\ge 0$ với mọi $x \\in '
                        '\\mathbb{R}$ nên không có số thực $x$ nào thỏa mãn $|x| = -2$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 7: Tập hợp các số thực '
                 'và giá trị tuyệt đối**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được số thực, tập hợp '
                           'các số thực $\\mathbb{R}$ và trục số thực.',
                           'Quy tắc/công thức **Quan hệ các tập hợp số** trong bài được xác định bởi: '
                           '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}; '
                           '\\quad \\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$.',
                           'Trong mọi trường hợp, **Quan hệ các tập hợp số** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 7: Tập hợp các số thực và giá trị tuyệt đối.',
                           'Với bài toán minh họa: “Tìm tất cả các số thực $x$ thỏa mãn $|x - 1,5| = 2,5$.”, '
                           'lời giải đúng là: Vì $|x - 1,5| = 2,5$ nên xảy ra hai trường hợp: - Trường hợp '
                           '1: $x - 1,5 = 2,5 \\Rightarrow x = 2,5 + 1,5 = 4$. - Trường hợp 2: $x - 1,5 = '
                           '-2,5 \\Rightarrow x = -2,5 + 1,5 = -1$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Tập hợp các số thực và giá trị tuyệt '
                        'đối. b) **Đúng** theo công thức trọng tâm **Quan hệ các tập hợp số** ($\\mathbb{N} '
                        '\\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}; \\quad \\mathbb{R} '
                        '= \\mathbb{Q} \\cup \\mathbb{I}$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Quan hệ các tập hợp số**. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 7: Tập hợp các số thực và giá trị tuyệt đối** để giải quyết tình '
                 'huống sau: Tìm tất cả các số thực $x$ thỏa mãn $|x - 1,5| = 2,5$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Vì $|x - 1,5| = 2,5$ nên xảy ra hai trường hợp: - Trường hợp 1: $x - 1,5 = 2,5 '
                        '\\Rightarrow x = 2,5 + 1,5 = 4$. - Trường hợp 2: $x - 1,5 = -2,5 \\Rightarrow x = '
                        '-2,5 + 1,5 = -1$...',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Tập hợp các số thực và giá trị tuyệt đối: Vì $|x - '
                        '1,5| = 2,5$ nên xảy ra hai trường hợp:\n'
                        '- Trường hợp 1: $x - 1,5 = 2,5 \\Rightarrow x = 2,5 + 1,5 = 4$.\n'
                        '- Trường hợp 2: $x - 1,5 = -2,5 \\Rightarrow x = -2,5 + 1,5 = -1$.\n'
                        'Vậy $x \\in \\{-1; 4\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $P = |-4,2| + |1,8| - |-2|$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $P = 4,2 + 1,8 - 2 = 6 - 2 = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch03-goc-duong-thang-song-song',
  'context_title': 'Chương III: Góc và đường thẳng song song',
  'context': 'Chương III · SGK Toán 7: Các góc ở vị trí đặc biệt, tia phân giác, hai đường thẳng song song '
             'và định lí hình học.',
  'title': 'Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc',
  'icon': '📐',
  'description': 'Hai góc kề bù, hai góc đối đỉnh và tính chất tia phân giác của một góc.',
  'requirements': ['Nhận biết được hai góc kề nhau, hai góc bù nhau, hai góc kề bù và hai góc đối đỉnh.',
                   'Nhận biết và vận dụng được tính chất hai góc đối đỉnh bằng nhau.',
                   'Nhận biết được tia phân giác của một góc và tính chất của tia phân giác.'],
  'definition': 'Hai góc đối đỉnh là hai góc mà mỗi cạnh của góc này là tia đối của một cạnh của góc kia. '
                'Tia phân giác của một góc là tia nằm trong góc và tạo với hai cạnh của góc đó hai góc bằng '
                'nhau.',
  'theory': '1. Hai góc kề bù: Hai góc có một cạnh chung, hai cạnh còn lại là hai tia đối nhau được gọi là '
            'hai góc kề bù. Tổng số đo của hai góc kề bù bằng $180^\\circ$.\n'
            '2. Hai góc đối đỉnh: Hai góc đối đỉnh thì bằng nhau.\n'
            '3. Tia phân giác của một góc: Nếu tia $Oz$ là tia phân giác của góc $\\widehat{xOy}$ thì '
            '$\\widehat{xOz} = \\widehat{zOy} = \\dfrac{1}{2}\\widehat{xOy}$.',
  'formulas': [{'category': 'Các hệ thức về góc đặc biệt',
                'items': [{'name': 'Hai góc kề bù',
                           'formula': '$\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$ (khi $Ox, Oz$ là hai '
                                      'tia đối nhau)'},
                          {'name': 'Hai góc đối đỉnh',
                           'formula': "$\\widehat{xOy}$ và $\\widehat{x'Oy'}$ đối đỉnh $\\Rightarrow "
                                      "\\widehat{xOy} = \\widehat{x'Oy'}$"},
                          {'name': 'Tính chất tia phân giác',
                           'formula': '$Oz$ là tia phân giác của $\\widehat{xOy} \\Rightarrow \\widehat{xOz} '
                                      '= \\widehat{zOy} = \\dfrac{\\widehat{xOy}}{2}$'}]}],
  'example': 'Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$, biết $\\widehat{xOy} = 70^\\circ$. Gọi '
             '$Ot$ là tia phân giác của $\\widehat{yOz}$. Tính số đo $\\widehat{yOt}$.',
  'example_answer': 'Vì $\\widehat{xOy}$ và $\\widehat{yOz}$ là hai góc kề bù nên $\\widehat{xOy} + '
                    '\\widehat{yOz} = 180^\\circ$, suy ra $\\widehat{yOz} = 180^\\circ - 70^\\circ = '
                    '110^\\circ$.\n'
                    'Vì $Ot$ là tia phân giác của $\\widehat{yOz}$ nên $\\widehat{yOt} = '
                    '\\dfrac{\\widehat{yOz}}{2} = \\dfrac{110^\\circ}{2} = 55^\\circ$.',
  'real_life': 'Cơ chế hoạt động của chiếc kéo cắt giấy (góc mở giữa hai lưỡi kéo và góc giữa hai tay cầm là '
               'hai góc đối đỉnh) hoặc gấp đôi tờ giấy theo tia phân giác.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng số đo của hai góc kề bù bằng bao nhiêu độ?',
            'options': ['$90^\\circ$', '$100^\\circ$', '$360^\\circ$', '$180^\\circ$'],
            'answer': 3,
            'solution': 'Tổng số đo của hai góc kề bù luôn bằng $180^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Cho hai đường thẳng $xx'$ và $yy'$ cắt nhau tại $O$, biết $\\widehat{xOy} = 65^\\circ$. Số "
                 "đo góc đối đỉnh $\\widehat{x'Oy'}$ là:",
            'options': ['$65^\\circ$', '$115^\\circ$', '$25^\\circ$', '$130^\\circ$'],
            'answer': 0,
            'solution': "Hai góc đối đỉnh thì bằng nhau nên $\\widehat{x'Oy'} = \\widehat{xOy} = 65^\\circ$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hai góc kề bù**?',
            'options': ["$\\widehat{xOy}$ và $\\widehat{x'Oy'}$ đối đỉnh $\\Rightarrow \\widehat{xOy} = "
                        "\\widehat{x'Oy'}$",
                        '$\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$ (khi $Ox, Oz$ là hai tia đối nhau)',
                        '$Oz$ là tia phân giác của $\\widehat{xOy} \\Rightarrow \\widehat{xOz} = '
                        '\\widehat{zOy} = \\dfrac{\\widehat{xOy}}{2}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của '
                        'một góc, **Hai góc kề bù** được xác định bởi: $\\widehat{xOy} + \\widehat{yOz} = '
                        '180^\\circ$ (khi $Ox, Oz$ là hai tia đối nhau).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc**, nội dung/biểu thức '
                 "$\\widehat{xOy}$ và $\\widehat{x'Oy'}$ đối đỉnh $\\Rightarrow \\widehat{xOy} = "
                 "\\widehat{x'Oy'}$ là quy tắc hoặc công thức của mục nào sau đây?",
            'options': ['Hai góc kề bù',
                        'Tính chất tia phân giác',
                        'Hai góc đối đỉnh',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc, biểu thức/quy tắc '
                        "$\\widehat{xOy}$ và $\\widehat{x'Oy'}$ đối đỉnh $\\Rightarrow \\widehat{xOy} = "
                        "\\widehat{x'Oy'}$ chính là nội dung của **Hai góc đối đỉnh**."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho góc $\\widehat{AOB} = 120^\\circ$. Tia $OC$ là tia phân giác của $\\widehat{AOB}$. Số '
                 'đo của góc $\\widehat{AOC}$ bằng:',
            'options': ['$120^\\circ$', '$30^\\circ$', '$90^\\circ$', '$60^\\circ$'],
            'answer': 3,
            'solution': 'Vì $OC$ là tia phân giác của $\\widehat{AOB}$ nên $\\widehat{AOC} = '
                        '\\dfrac{120^\\circ}{2} = 60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc** (Chương III: Góc và '
                 'đường thẳng song song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được hai góc kề nhau, hai góc bù nhau, hai góc kề bù và hai góc đối đỉnh.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc: '
                        'Nhận biết được hai góc kề nhau, hai góc bù nhau, hai góc kề bù và hai góc đối '
                        'đỉnh.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOx'}$ có $\\widehat{xOy} = 80^\\circ$. "
                 "Gọi $Om, On$ lần lượt là tia phân giác của $\\widehat{xOy}$ và $\\widehat{yOx'}$. Xét các "
                 'khẳng định sau:',
            'statements': ["Số đo góc $\\widehat{yOx'}$ bằng $100^\\circ$.",
                           'Số đo góc $\\widehat{mOy}$ bằng $40^\\circ$.',
                           'Số đo góc $\\widehat{yOn}$ bằng $50^\\circ$.',
                           'Góc tạo bởi hai tia phân giác $\\widehat{mOn}$ bằng $90^\\circ$.'],
            'answer': [True, True, True, True],
            'solution': "a) $\\widehat{yOx'} = 180^\\circ - 80^\\circ = 100^\\circ$ (Đúng). b) "
                        '$\\widehat{mOy} = \\dfrac{80^\\circ}{2} = 40^\\circ$ (Đúng). c) $\\widehat{yOn} = '
                        '\\dfrac{100^\\circ}{2} = 50^\\circ$ (Đúng). d) $\\widehat{mOn} = \\widehat{mOy} + '
                        '\\widehat{yOn} = 40^\\circ + 50^\\circ = 90^\\circ$ (Đúng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 8: Góc ở vị trí đặc '
                 'biệt. Tia phân giác của một góc**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hai góc kề nhau, '
                           'hai góc bù nhau, hai góc kề bù và hai góc đối đỉnh.',
                           'Quy tắc/công thức **Hai góc kề bù** trong bài được xác định bởi: $\\widehat{xOy} '
                           '+ \\widehat{yOz} = 180^\\circ$ (khi $Ox, Oz$ là hai tia đối nhau).',
                           'Trong mọi trường hợp, **Hai góc kề bù** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc.',
                           'Với bài toán minh họa: “Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$, '
                           'biết $\\widehat{xOy} = 70^\\circ$. Gọi $Ot$ là tia phân giác của '
                           '$\\widehat{yOz}$. Tính s...”, lời giải đúng là: Vì $\\widehat{xOy}$ và '
                           '$\\widehat{yOz}$ là hai góc kề bù nên $\\widehat{xOy} + \\widehat{yOz} = '
                           '180^\\circ$, suy ra $\\widehat{yOz} = 180^\\circ - 70^\\circ = 110^\\circ$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Góc ở vị trí đặc biệt. Tia phân giác '
                        'của một góc. b) **Đúng** theo công thức trọng tâm **Hai góc kề bù** '
                        '($\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$ (khi $Ox, Oz$ là hai tia đối '
                        'nhau)). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b '
                        '\\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không phải '
                        'quy tắc chung của **Hai góc kề bù**. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc** để giải '
                 'quyết tình huống sau: Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$, biết '
                 '$\\widehat{xOy} = 70^\\circ$. Gọi $Ot$ là tia phân giác của $\\widehat{yOz}$. Tính số đo '
                 '$\\widehat{yOt}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Vì $\\widehat{xOy}$ và $\\widehat{yOz}$ là hai góc kề bù nên $\\widehat{xOy} + '
                        '\\widehat{yOz} = 180^\\circ$, suy ra $\\widehat{yOz} = 180^\\circ - 70^\\circ = '
                        '110^\\circ$...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc: Vì '
                        '$\\widehat{xOy}$ và $\\widehat{yOz}$ là hai góc kề bù nên $\\widehat{xOy} + '
                        '\\widehat{yOz} = 180^\\circ$, suy ra $\\widehat{yOz} = 180^\\circ - 70^\\circ = '
                        '110^\\circ$.\n'
                        'Vì $Ot$ là tia phân giác của $\\widehat{yOz}$ nên $\\widehat{yOt} = '
                        '\\dfrac{\\widehat{yOz}}{2} = \\dfrac{110^\\circ}{2} = 55^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$, biết $\\widehat{AOB} = '
                 '3\\widehat{BOC}$. Tính số đo góc $\\widehat{BOC}$ (theo đơn vị độ).',
            'answer': ['45'],
            'unit': None,
            'solution': 'Ta có $\\widehat{AOB} + \\widehat{BOC} = 180^\\circ \\Rightarrow 3\\widehat{BOC} + '
                        '\\widehat{BOC} = 180^\\circ \\Rightarrow 4\\widehat{BOC} = 180^\\circ \\Rightarrow '
                        '\\widehat{BOC} = 45^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch03-goc-duong-thang-song-song',
  'context_title': 'Chương III: Góc và đường thẳng song song',
  'context': 'Chương III · SGK Toán 7: Các góc ở vị trí đặc biệt, tia phân giác, hai đường thẳng song song '
             'và định lí hình học.',
  'title': 'Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết',
  'icon': '⏸️',
  'description': 'Các cặp góc so le trong, đồng vị và dấu hiệu nhận biết hai đường thẳng song song.',
  'requirements': ['Nhận biết được các góc tạo bởi một đường thẳng cắt hai đường thẳng: hai góc so le trong, '
                   'hai góc đồng vị.',
                   'Mô tả và vận dụng được dấu hiệu nhận biết hai đường thẳng song song thông qua cặp góc so '
                   'le trong hoặc cặp góc đồng vị.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Theo góc so le trong** (Cặp góc so le trong '
                   '$\\widehat{A_1} = \\widehat{B_1} \\Rightarrow a \\parallel b$) vào giải bài tập.'],
  'definition': 'Nếu đường thẳng $c$ cắt hai đường thẳng phân biệt $a, b$ và trong các góc tạo thành có một '
                'cặp góc so le trong bằng nhau hoặc một cặp góc đồng vị bằng nhau thì $a$ và $b$ song song '
                'với nhau (kí hiệu $a \\parallel b$).',
  'theory': '1. Các góc tạo bởi một đường thẳng cắt hai đường thẳng: Cho đường thẳng $c$ cắt hai đường thẳng '
            '$a$ và $b$ lần lượt tại $A$ và $B$. Tại $A$ và $B$ tạo thành các cặp góc so le trong, các cặp '
            'góc đồng vị và các cặp góc trong cùng phía.\n'
            '2. Dấu hiệu nhận biết hai đường thẳng song song:\n'
            '- Nếu có một cặp góc so le trong bằng nhau thì hai đường thẳng song song.\n'
            '- Nếu có một cặp góc đồng vị bằng nhau thì hai đường thẳng song song.\n'
            '- Hệ quả: Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song '
            'song với nhau.',
  'formulas': [{'category': 'Dấu hiệu nhận biết hai đường thẳng song song',
                'items': [{'name': 'Theo góc so le trong',
                           'formula': 'Cặp góc so le trong $\\widehat{A_1} = \\widehat{B_1} \\Rightarrow a '
                                      '\\parallel b$'},
                          {'name': 'Theo góc đồng vị',
                           'formula': 'Cặp góc đồng vị $\\widehat{A_2} = \\widehat{B_2} \\Rightarrow a '
                                      '\\parallel b$'},
                          {'name': 'Cùng vuông góc đường thứ ba',
                           'formula': '$a \\perp c$ và $b \\perp c$ ($a \\neq b$) $\\Rightarrow a \\parallel '
                                      'b$'}]}],
  'example': 'Đường thẳng $c$ cắt hai đường thẳng $a, b$ tại $A$ và $B$. Biết cặp góc so le trong '
             '$\\widehat{A_1} = 60^\\circ$ và $\\widehat{B_3} = 60^\\circ$. Chứng tỏ $a \\parallel b$.',
  'example_answer': 'Ta có hai góc $\\widehat{A_1}$ và $\\widehat{B_3}$ ở vị trí so le trong và '
                    '$\\widehat{A_1} = \\widehat{B_3} = 60^\\circ$.\n'
                    'Theo dấu hiệu nhận biết hai đường thẳng song song, suy ra $a \\parallel b$.',
  'real_life': 'Người thợ mộc dùng thước góc (ê-ke) kẻ hai vạch cùng tạo với mép gỗ một góc bằng nhau để đảm '
               'bảo hai nhát cưa song song.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu đường thẳng $c$ cắt hai đường thẳng phân biệt $a, b$ và trong các góc tạo thành có một '
                 'cặp góc so le trong bằng nhau thì:',
            'options': ['$a \\parallel b$', '$a \\perp b$', '$a$ cắt $b$', '$a$ trùng $b$'],
            'answer': 0,
            'solution': 'Theo dấu hiệu nhận biết hai đường thẳng song song, nếu có một cặp góc so le trong '
                        'bằng nhau thì $a \\parallel b$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng:',
            'options': ['Vuông góc với nhau', 'Song song với nhau', 'Cắt nhau tại một điểm', 'Trùng nhau'],
            'answer': 1,
            'solution': 'Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì tạo ra hai '
                        'góc đồng vị đều bằng $90^\\circ$ nên chúng song song với nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Theo góc so le trong**?',
            'options': ['Cặp góc đồng vị $\\widehat{A_2} = \\widehat{B_2} \\Rightarrow a \\parallel b$',
                        '$a \\perp c$ và $b \\perp c$ ($a \\neq b$) $\\Rightarrow a \\parallel b$',
                        'Cặp góc so le trong $\\widehat{A_1} = \\widehat{B_1} \\Rightarrow a \\parallel b$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 9: Hai đường thẳng song song và dấu hiệu nhận '
                        'biết, **Theo góc so le trong** được xác định bởi: Cặp góc so le trong '
                        '$\\widehat{A_1} = \\widehat{B_1} \\Rightarrow a \\parallel b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết**, nội dung/biểu thức Cặp '
                 'góc đồng vị $\\widehat{A_2} = \\widehat{B_2} \\Rightarrow a \\parallel b$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Theo góc so le trong',
                        'Cùng vuông góc đường thứ ba',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Theo góc đồng vị'],
            'answer': 3,
            'solution': 'Trong Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết, biểu thức/quy tắc Cặp '
                        'góc đồng vị $\\widehat{A_2} = \\widehat{B_2} \\Rightarrow a \\parallel b$ chính là '
                        'nội dung của **Theo góc đồng vị**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ tạo thành cặp góc trong cùng phía có số đo '
                 'là $75^\\circ$ và $105^\\circ$. Khi đó:',
            'options': ['$a \\parallel b$',
                        '$a \\perp b$',
                        '$a$ cắt $b$ tại góc $75^\\circ$',
                        'Không kết luận được'],
            'answer': 0,
            'solution': 'Vì tổng hai góc trong cùng phía bằng $75^\\circ + 105^\\circ = 180^\\circ$ nên cặp '
                        'góc so le trong tương ứng bằng nhau (đều bằng $75^\\circ$), suy ra $a \\parallel '
                        'b$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết** (Chương III: Góc và '
                 'đường thẳng song song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Nhận biết được các góc tạo bởi một đường thẳng cắt hai đường thẳng: hai góc so le '
                        'trong, hai góc đồng vị.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết: '
                        'Nhận biết được các góc tạo bởi một đường thẳng cắt hai đường thẳng: hai góc so le '
                        'trong, hai góc đồng vị.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đường thẳng $c$ cắt hai đường thẳng phân biệt $a, b$ tại $A$ và $B$. Xét các khẳng '
                 'định sau:',
            'statements': ['Nếu một cặp góc đồng vị bằng nhau thì $a \\parallel b$.',
                           'Nếu một cặp góc đối đỉnh tại $A$ bằng nhau thì suy ra ngay $a \\parallel b$.',
                           'Nếu $a \\perp c$ và $b \\perp c$ thì $a \\parallel b$.',
                           'Nếu hai góc so le trong bằng $50^\\circ$ và $50^\\circ$ thì $a \\parallel b$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì hai góc đối đỉnh tại cùng một đỉnh $A$ luôn bằng nhau với mọi vị '
                        'trí của $a, b$. c) Đúng. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 9: Hai đường thẳng song '
                 'song và dấu hiệu nhận biết**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được các góc tạo bởi một '
                           'đường thẳng cắt hai đường thẳng: hai góc so le trong, hai góc đồng vị.',
                           'Quy tắc/công thức **Theo góc so le trong** trong bài được xác định bởi: Cặp góc '
                           'so le trong $\\widehat{A_1} = \\widehat{B_1} \\Rightarrow a \\parallel b$.',
                           'Trong mọi trường hợp, **Theo góc so le trong** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết.',
                           'Với bài toán minh họa: “Đường thẳng $c$ cắt hai đường thẳng $a, b$ tại $A$ và '
                           '$B$. Biết cặp góc so le trong $\\widehat{A_1} = 60^\\circ$ và $\\widehat{B_3} = '
                           '60^\\circ$...”, lời giải đúng là: Ta có hai góc $\\widehat{A_1}$ và '
                           '$\\widehat{B_3}$ ở vị trí so le trong và $\\widehat{A_1} = \\widehat{B_3} = '
                           '60^\\circ$. Theo dấu hiệu nhận biết...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Hai đường thẳng song song và dấu hiệu '
                        'nhận biết. b) **Đúng** theo công thức trọng tâm **Theo góc so le trong** (Cặp góc '
                        'so le trong $\\widehat{A_1} = \\widehat{B_1} \\Rightarrow a \\parallel b$). c) '
                        '**Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                        '\\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy '
                        'tắc chung của **Theo góc so le trong**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết** để giải '
                 'quyết tình huống sau: Đường thẳng $c$ cắt hai đường thẳng $a, b$ tại $A$ và $B$. Biết cặp '
                 'góc so le trong $\\widehat{A_1} = 60^\\circ$ và $\\widehat{B_3} = 60^\\circ$. Chứng tỏ $a '
                 '\\parallel b$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có hai góc $\\widehat{A_1}$ và $\\widehat{B_3}$ ở vị trí so le trong và '
                        '$\\widehat{A_1} = \\widehat{B_3} = 60^\\circ$. Theo dấu hiệu nhận biết hai đường '
                        'thẳn...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết: Ta '
                        'có hai góc $\\widehat{A_1}$ và $\\widehat{B_3}$ ở vị trí so le trong và '
                        '$\\widehat{A_1} = \\widehat{B_3} = 60^\\circ$.\n'
                        'Theo dấu hiệu nhận biết hai đường thẳng song song, suy ra $a \\parallel b$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Đường thẳng $c$ cắt hai đường thẳng $a, b$ tại $M, N$. Biết góc $\\widehat{M_1} = '
                 '115^\\circ$ và góc đồng vị với $\\widehat{M_1}$ là $\\widehat{N_1} = (2x + 15)^\\circ$. '
                 'Tìm $x$ để $a \\parallel b$.',
            'answer': ['50'],
            'unit': None,
            'solution': 'Để $a \\parallel b$ thì hai góc đồng vị phải bằng nhau: $2x + 15 = 115 \\Rightarrow '
                        '2x = 100 \\Rightarrow x = 50$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch03-goc-duong-thang-song-song',
  'context_title': 'Chương III: Góc và đường thẳng song song',
  'context': 'Chương III · SGK Toán 7: Các góc ở vị trí đặc biệt, tia phân giác, hai đường thẳng song song '
             'và định lí hình học.',
  'title': 'Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song',
  'icon': '🛤️',
  'description': 'Tiên đề Euclid về đường thẳng song song và các tính chất của hai đường thẳng song song.',
  'requirements': ['Nhận biết được tiên đề Euclid về đường thẳng song song.',
                   'Mô tả và vận dụng được các tính chất của hai đường thẳng song song (hai góc so le trong '
                   'bằng nhau, hai góc đồng vị bằng nhau).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tính chất góc so le trong, đồng vị** ($a '
                   '\\parallel b \\Rightarrow$ hai góc so le trong bằng nhau, hai góc đồng vị bằng nhau) vào '
                   'giải bài tập.'],
  'definition': 'Tiên đề Euclid: Qua một điểm ở ngoài một đường thẳng, chỉ có một đường thẳng song song với '
                'đường thẳng đó.',
  'theory': '1. Tiên đề Euclid và hệ quả: Nếu một đường thẳng cắt một trong hai đường thẳng song song thì nó '
            'cũng cắt đường thẳng còn lại.\n'
            '2. Tính chất của hai đường thẳng song song: Nếu một đường thẳng cắt hai đường thẳng song song '
            'thì:\n'
            '- Hai góc so le trong bằng nhau.\n'
            '- Hai góc đồng vị bằng nhau.\n'
            '- Hai góc trong cùng phía bù nhau (tổng bằng $180^\\circ$).\n'
            '3. Quan hệ giữa tính vuông góc và tính song song:\n'
            '- Một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với '
            'đường thẳng kia.\n'
            '- Hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì chúng song song với '
            'nhau.',
  'formulas': [{'category': 'Tính chất hai đường thẳng song song ($a \\parallel b$)',
                'items': [{'name': 'Tính chất góc so le trong, đồng vị',
                           'formula': '$a \\parallel b \\Rightarrow$ hai góc so le trong bằng nhau, hai góc '
                                      'đồng vị bằng nhau'},
                          {'name': 'Tính chất góc trong cùng phía',
                           'formula': '$a \\parallel b \\Rightarrow$ tổng hai góc trong cùng phía bằng '
                                      '$180^\\circ$'},
                          {'name': 'Quan hệ vuông góc - song song',
                           'formula': '$a \\parallel b$ và $c \\perp a \\Rightarrow c \\perp b$'},
                          {'name': 'Ba đường thẳng song song',
                           'formula': '$a \\parallel c$ và $b \\parallel c$ ($a \\neq b$) $\\Rightarrow a '
                                      '\\parallel b$'}]}],
  'example': 'Cho hai đường thẳng song song $a \\parallel b$. Đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại '
             '$B$. Biết $\\widehat{A_1} = 130^\\circ$, tính góc trong cùng phía $\\widehat{B_2}$ với '
             '$\\widehat{A_1}$.',
  'example_answer': 'Vì $a \\parallel b$ nên hai góc trong cùng phía $\\widehat{A_1}$ và $\\widehat{B_2}$ bù '
                    'nhau:\n'
                    '$\\widehat{A_1} + \\widehat{B_2} = 180^\\circ \\Rightarrow \\widehat{B_2} = 180^\\circ '
                    '- 130^\\circ = 50^\\circ$.',
  'real_life': 'Hai thanh ray đường sắt song song cùng vuông góc với các thanh tà vẹt bên dưới.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Theo tiên đề Euclid, qua một điểm nằm ngoài một đường thẳng cho trước, ta vẽ được bao '
                 'nhiêu đường thẳng song song với đường thẳng đó?',
            'options': ['Hai đường thẳng',
                        'Chỉ một đường thẳng',
                        'Vô số đường thẳng',
                        'Không vẽ được đường thẳng nào'],
            'answer': 1,
            'solution': 'Tiên đề Euclid khẳng định: Qua một điểm ở ngoài một đường thẳng, chỉ có một đường '
                        'thẳng song song với đường thẳng đó.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong:',
            'options': ['Phụ nhau', 'Gấp đôi nhau', 'Bằng nhau', 'Có tổng bằng $90^\\circ$'],
            'answer': 2,
            'solution': 'Tính chất hai đường thẳng song song: Hai góc so le trong bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song '
                 'song**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tính chất góc so le trong, '
                 'đồng vị**?',
            'options': ['$a \\parallel b \\Rightarrow$ tổng hai góc trong cùng phía bằng $180^\\circ$',
                        '$a \\parallel b$ và $c \\perp a \\Rightarrow c \\perp b$',
                        '$a \\parallel c$ và $b \\parallel c$ ($a \\neq b$) $\\Rightarrow a \\parallel b$',
                        '$a \\parallel b \\Rightarrow$ hai góc so le trong bằng nhau, hai góc đồng vị bằng '
                        'nhau'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 10: Tiên đề Euclid. Tính chất của hai đường '
                        'thẳng song song, **Tính chất góc so le trong, đồng vị** được xác định bởi: $a '
                        '\\parallel b \\Rightarrow$ hai góc so le trong bằng nhau, hai góc đồng vị bằng '
                        'nhau.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song**, nội dung/biểu '
                 'thức $a \\parallel b \\Rightarrow$ tổng hai góc trong cùng phía bằng $180^\\circ$ là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tính chất góc trong cùng phía',
                        'Tính chất góc so le trong, đồng vị',
                        'Quan hệ vuông góc - song song',
                        'Ba đường thẳng song song'],
            'answer': 0,
            'solution': 'Trong Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song, biểu '
                        'thức/quy tắc $a \\parallel b \\Rightarrow$ tổng hai góc trong cùng phía bằng '
                        '$180^\\circ$ chính là nội dung của **Tính chất góc trong cùng phía**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $a \\parallel b$, đường thẳng $c$ cắt $a, b$ lần lượt tại $A, B$. Biết một góc tại $A$ '
                 'bằng $70^\\circ$, góc đồng vị với nó tại $B$ có số đo là:',
            'options': ['$110^\\circ$', '$70^\\circ$', '$20^\\circ$', '$140^\\circ$'],
            'answer': 1,
            'solution': 'Vì $a \\parallel b$ nên hai góc đồng vị bằng nhau và cùng bằng $70^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song** (Chương III: '
                 'Góc và đường thẳng song song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được tiên đề Euclid về đường thẳng song song.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song '
                        'song: Nhận biết được tiên đề Euclid về đường thẳng song song.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho ba đường thẳng phân biệt $a, b, c$. Xét tính đúng sai của các khẳng định sau:',
            'statements': ['Nếu $a \\parallel b$ và $b \\parallel c$ thì $a \\parallel c$.',
                           'Nếu $a \\parallel b$ và $c \\perp a$ thì $c \\perp b$.',
                           'Nếu $a \\parallel b$ thì hai góc trong cùng phía tạo bởi đường cắt $c$ luôn bằng '
                           'nhau.',
                           'Nếu đường thẳng $c$ cắt đường thẳng $a$ và $a \\parallel b$ thì $c$ cũng cắt '
                           'đường thẳng $b$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng. c) Sai vì hai góc trong cùng phía có tổng bằng $180^\\circ$ (chỉ '
                        'bằng nhau khi cùng bằng $90^\\circ$). d) Đúng theo hệ quả tiên đề Euclid.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 10: Tiên đề Euclid. '
                 'Tính chất của hai đường thẳng song song**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được tiên đề Euclid về '
                           'đường thẳng song song.',
                           'Quy tắc/công thức **Tính chất góc so le trong, đồng vị** trong bài được xác định '
                           'bởi: $a \\parallel b \\Rightarrow$ hai góc so le trong bằng nhau, hai góc đồng '
                           'vị bằng nhau.',
                           'Trong mọi trường hợp, **Tính chất góc so le trong, đồng vị** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song '
                           'song.',
                           'Với bài toán minh họa: “Cho hai đường thẳng song song $a \\parallel b$. Đường '
                           'thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$. Biết $\\widehat{A_1} = '
                           '130^\\circ$, tính gó...”, lời giải đúng là: Vì $a \\parallel b$ nên hai góc '
                           'trong cùng phía $\\widehat{A_1}$ và $\\widehat{B_2}$ bù nhau: $\\widehat{A_1} + '
                           '\\widehat{B_2} = 180^\\circ \\Rightarrow \\widehat{B_2} = 180^\\circ - '
                           '130^\\circ = 50^\\circ$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Tiên đề Euclid. Tính chất của hai '
                        'đường thẳng song song. b) **Đúng** theo công thức trọng tâm **Tính chất góc so le '
                        'trong, đồng vị** ($a \\parallel b \\Rightarrow$ hai góc so le trong bằng nhau, hai '
                        'góc đồng vị bằng nhau). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Tính chất góc so le trong, đồng vị**. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song** để '
                 'giải quyết tình huống sau: Cho hai đường thẳng song song $a \\parallel b$. Đường thẳng $c$ '
                 'cắt $a$ tại $A$ và cắt $b$ tại $B$. Biết $\\widehat{A_1} = 130^\\circ$, tính góc trong '
                 'cùng phía $\\widehat{B_2}$ với $\\widehat{A_1}$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Vì $a \\parallel b$ nên hai góc trong cùng phía $\\widehat{A_1}$ và '
                        '$\\widehat{B_2}$ bù nhau: $\\widehat{A_1} + \\widehat{B_2} = 180^\\circ '
                        '\\Rightarrow \\widehat{B_2} = 180^\\circ - 130^\\circ = 50^\\circ$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song '
                        'song: Vì $a \\parallel b$ nên hai góc trong cùng phía $\\widehat{A_1}$ và '
                        '$\\widehat{B_2}$ bù nhau:\n'
                        '$\\widehat{A_1} + \\widehat{B_2} = 180^\\circ \\Rightarrow \\widehat{B_2} = '
                        '180^\\circ - 130^\\circ = 50^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Cho hai đường thẳng song song $x x' \\parallel y y'$. Một đường thẳng $d$ cắt $x x'$ tại "
                 "$A$ và $y y'$ tại $B$ tạo thành hai góc trong cùng phía $\\widehat{A_1}$ và "
                 '$\\widehat{B_2}$. Biết $\\widehat{A_1} - \\widehat{B_2} = 40^\\circ$, tính số đo góc '
                 '$\\widehat{A_1}$ (đơn vị độ).',
            'answer': ['110'],
            'unit': None,
            'solution': "Vì $xx' \\parallel yy'$ nên $\\widehat{A_1} + \\widehat{B_2} = 180^\\circ$. Kết hợp "
                        '$\\widehat{A_1} - \\widehat{B_2} = 40^\\circ$, ta có $\\widehat{A_1} = '
                        '\\dfrac{180^\\circ + 40^\\circ}{2} = 110^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch03-goc-duong-thang-song-song',
  'context_title': 'Chương III: Góc và đường thẳng song song',
  'context': 'Chương III · SGK Toán 7: Các góc ở vị trí đặc biệt, tia phân giác, hai đường thẳng song song '
             'và định lí hình học.',
  'title': 'Bài 11: Định lí và chứng minh định lí',
  'icon': '📜',
  'description': 'Khái niệm định lí, phần giả thiết, kết luận của định lí và cách chứng minh một định lí.',
  'requirements': ['Nhận biết được thế nào là một định lí.',
                   'Phân biệt được phần giả thiết (GT) và phần kết luận (KL) của một định lí.',
                   'Hiểu thế nào là chứng minh một định lí và bước đầu thực hiện chứng minh định lí hình '
                   'học.'],
  'definition': 'Định lí là một khẳng định được suy ra từ những khẳng định đúng đã biết. Mỗi định lí thường '
                "được phát biểu dưới dạng: 'Nếu ... thì ...', trong đó phần giữa từ 'nếu' và từ 'thì' là giả "
                "thiết (GT), phần sau từ 'thì' là kết luận (KL).",
  'theory': '1. Cấu trúc của định lí:\n'
            '- Giả thiết (viết tắt là GT) là những điều cho biết trước.\n'
            '- Kết luận (viết tắt là KL) là điều cần suy ra.\n'
            '2. Chứng minh định lí: Chứng minh một định lí là dùng lập luận để từ giả thiết và những khẳng '
            'định đúng đã biết suy ra kết luận của định lí.',
  'formulas': [{'category': 'Cấu trúc suy luận của định lí',
                'items': [{'name': 'Dạng phát biểu chuẩn',
                           'formula': 'Nếu $[\\text{Giả thiết (GT)}]$ thì $[\\text{Kết luận (KL)}]$'},
                          {'name': 'Ví dụ định lí hai góc đối đỉnh',
                           'formula': '$\\text{GT: } \\widehat{O_1} \\text{ và } \\widehat{O_3} \\text{ đối '
                                      'đỉnh} \\Rightarrow \\text{KL: } \\widehat{O_1} = \\widehat{O_3}$'}]}],
  'example': "Hãy chỉ rõ giả thiết và kết luận của định lí: 'Nếu một đường thẳng cắt hai đường thẳng song "
             "song thì hai góc đồng vị bằng nhau'.",
  'example_answer': '- Giả thiết (GT): Đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$ ($a '
                    '\\parallel b$).\n'
                    '- Kết luận (KL): Hai góc đồng vị tạo thành bằng nhau.',
  'real_life': 'Rèn luyện tư duy lập luận logic chặt chẽ từ các dữ kiện đã có để đưa ra kết luận chính xác '
               'trong khoa học và pháp luật.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Trong một định lí phát biểu dưới dạng 'Nếu ... thì ...', phần nằm sau từ 'thì' được gọi là "
                 'gì?',
            'options': ['Giả thiết', 'Tiên đề', 'Kết luận', 'Định nghĩa'],
            'answer': 2,
            'solution': "Phần giữa từ 'nếu' và từ 'thì' là giả thiết, phần sau từ 'thì' là kết luận.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Chứng minh một định lí là:',
            'options': ['Dùng thước đo góc và thước thẳng đo trên hình vẽ để kiểm tra',
                        'Lấy một vài ví dụ cụ thể để thử xem định lí có đúng không',
                        'Học thuộc lòng phát biểu của định lí',
                        'Dùng lập luận để từ giả thiết và những khẳng định đúng đã biết suy ra kết luận'],
            'answer': 3,
            'solution': 'Chứng minh định lí phải dùng suy luận logic từ giả thiết và các kiến thức đúng đã '
                        'biết, không thể chỉ đo đạc trực quan.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 11: Định lí và chứng minh định lí**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Dạng phát biểu chuẩn**?',
            'options': ['Nếu $[\\text{Giả thiết (GT)}]$ thì $[\\text{Kết luận (KL)}]$',
                        '$\\text{GT: } \\widehat{O_1} \\text{ và } \\widehat{O_3} \\text{ đối đỉnh} '
                        '\\Rightarrow \\text{KL: } \\widehat{O_1} = \\widehat{O_3}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 11: Định lí và chứng minh định lí, **Dạng '
                        'phát biểu chuẩn** được xác định bởi: Nếu $[\\text{Giả thiết (GT)}]$ thì '
                        '$[\\text{Kết luận (KL)}]$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Định lí và chứng minh định lí**, nội dung/biểu thức $\\text{GT: } '
                 '\\widehat{O_1} \\text{ và } \\widehat{O_3} \\text{ đối đỉnh} \\Rightarrow \\text{KL: } '
                 '\\widehat{O_1} = \\widehat{O_3}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Dạng phát biểu chuẩn',
                        'Ví dụ định lí hai góc đối đỉnh',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp'],
            'answer': 1,
            'solution': 'Trong Bài 11: Định lí và chứng minh định lí, biểu thức/quy tắc $\\text{GT: } '
                        '\\widehat{O_1} \\text{ và } \\widehat{O_3} \\text{ đối đỉnh} \\Rightarrow '
                        '\\text{KL: } \\widehat{O_1} = \\widehat{O_3}$ chính là nội dung của **Ví dụ định lí '
                        'hai góc đối đỉnh**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho định lí: 'Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì "
                 "chúng song song với nhau'. Kết luận của định lí này là:",
            'options': ['Hai đường thẳng đó vuông góc với nhau',
                        'Hai đường thẳng phân biệt cùng vuông góc với đường thẳng thứ ba',
                        'Hai đường thẳng đó song song với nhau',
                        'Ba đường thẳng đôi một cắt nhau'],
            'answer': 2,
            'solution': 'Giả thiết là: $a \\neq b, a \\perp c, b \\perp c$; Kết luận là: $a \\parallel b$ '
                        '(chúng song song với nhau).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Định lí và chứng minh định lí** (Chương III: Góc và đường thẳng song '
                 'song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Nhận biết được thế nào là một định lí.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 11: Định lí và chứng minh định lí: Nhận biết được thế '
                        'nào là một định lí.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Xét định lí: 'Nếu hai góc kề bù và bằng nhau thì mỗi góc là một góc vuông'. Xét các khẳng "
                 'định sau:',
            'statements': ['Giả thiết của định lí là hai góc kề bù và bằng nhau.',
                           'Kết luận của định lí là mỗi góc bằng $90^\\circ$.',
                           'Ta chứng minh định lí này bằng cách sử dụng tính chất tổng hai góc kề bù bằng '
                           '$180^\\circ$.',
                           'Đo bằng thước đo góc trên 1 hình vẽ bất kì là cách chứng minh đầy đủ cho định lí '
                           'trên.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $\\widehat{A} + \\widehat{B} = 180^\\circ$ và $\\widehat{A} = '
                        '\\widehat{B} \\Rightarrow \\widehat{A} = \\widehat{B} = 90^\\circ$. d) Sai vì đo '
                        'đạc không phải là chứng minh toán học.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 11: Định lí và chứng '
                 'minh định lí**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được thế nào là một định '
                           'lí.',
                           'Quy tắc/công thức **Dạng phát biểu chuẩn** trong bài được xác định bởi: Nếu '
                           '$[\\text{Giả thiết (GT)}]$ thì $[\\text{Kết luận (KL)}]$.',
                           'Trong mọi trường hợp, **Dạng phát biểu chuẩn** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 11: Định lí và chứng minh định lí.',
                           "Với bài toán minh họa: “Hãy chỉ rõ giả thiết và kết luận của định lí: 'Nếu một "
                           "đường thẳng cắt hai đường thẳng song song thì hai góc đồng vị bằng nhau'.”, lời "
                           'giải đúng là: - Giả thiết (GT): Đường thẳng $c$ cắt hai đường thẳng song song '
                           '$a$ và $b$ ($a \\parallel b$). - Kết luận (KL): Hai góc đồng vị tạo thành '
                           'bằn...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Định lí và chứng minh định lí. b) '
                        '**Đúng** theo công thức trọng tâm **Dạng phát biểu chuẩn** (Nếu $[\\text{Giả thiết '
                        '(GT)}]$ thì $[\\text{Kết luận (KL)}]$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Dạng phát biểu chuẩn**. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 11: Định lí và chứng minh định lí** để giải quyết tình huống sau: '
                 "Hãy chỉ rõ giả thiết và kết luận của định lí: 'Nếu một đường thẳng cắt hai đường thẳng "
                 "song song thì hai góc đồng vị bằng nhau'. Kết quả và hướng giải nào dưới đây là **đúng**?",
            'options': ['- Giả thiết (GT): Đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$ ($a '
                        '\\parallel b$). - Kết luận (KL): Hai góc đồng vị tạo thành bằng nhau.',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Định lí và chứng minh định lí: - Giả thiết (GT): '
                        'Đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$ ($a \\parallel b$).\n'
                        '- Kết luận (KL): Hai góc đồng vị tạo thành bằng nhau.'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Chứng minh định lí: 'Góc tạo bởi hai tia phân giác của hai góc kề bù là một góc vuông'. "
                 'Hỏi số đo góc tạo bởi hai tia phân giác đó bằng bao nhiêu độ?',
            'answer': ['90'],
            'unit': None,
            'solution': 'Nếu $\\widehat{xOy} + \\widehat{yOz} = 180^\\circ$ thì góc giữa hai tia phân giác '
                        'là $\\dfrac{1}{2}(\\widehat{xOy} + \\widehat{yOz}) = \\dfrac{180^\\circ}{2} = '
                        '90^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch04-tam-giac-bang-nhau',
  'context_title': 'Chương IV: Tam giác bằng nhau',
  'context': 'Chương IV · SGK Toán 7: Tổng các góc trong tam giác, các trường hợp bằng nhau của tam giác và '
             'tam giác cân.',
  'title': 'Bài 12: Tổng các góc trong một tam giác',
  'icon': '🔺',
  'description': 'Định lí tổng ba góc trong một tam giác, tam giác nhọn, tam giác tù, tam giác vuông và tính '
                 'chất góc ngoài của tam giác.',
  'requirements': ['Giải thích được định lí về tổng các góc trong một tam giác bằng $180^\\circ$.',
                   'Nhận biết được tam giác nhọn, tam giác vuông, tam giác tù và tính chất hai góc nhọn phụ '
                   'nhau trong tam giác vuông.',
                   'Nhận biết và vận dụng được tính chất góc ngoài của tam giác.'],
  'definition': 'Tổng ba góc trong một tam giác bằng $180^\\circ$. Góc ngoài của một tam giác là góc kề bù '
                'với một góc trong của tam giác và bằng tổng hai góc trong không kề với nó.',
  'theory': '1. Tổng ba góc của một tam giác: Trong $\\triangle ABC$, ta luôn có $\\widehat{A} + '
            '\\widehat{B} + \\widehat{C} = 180^\\circ$.\n'
            '2. Phân loại tam giác theo góc:\n'
            '- Tam giác có ba góc nhọn gọi là tam giác nhọn.\n'
            '- Tam giác có một góc tù gọi là tam giác tù.\n'
            '- Tam giác có một góc vuông ($90^\\circ$) gọi là tam giác vuông. Trong một tam giác vuông, tổng '
            'hai góc nhọn bằng $90^\\circ$ (hai góc nhọn phụ nhau).\n'
            '3. Góc ngoài của tam giác: Mỗi góc ngoài của một tam giác có số đo bằng tổng số đo hai góc '
            'trong không kề với nó.',
  'formulas': [{'category': 'Các hệ thức góc trong tam giác',
                'items': [{'name': 'Tổng ba góc trong $\\triangle ABC$',
                           'formula': '$\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$'},
                          {'name': 'Hai góc nhọn trong tam giác vuông',
                           'formula': '$\\triangle ABC$ vuông tại $A$ $\\Rightarrow \\widehat{B} + '
                                      '\\widehat{C} = 90^\\circ$'},
                          {'name': 'Góc ngoài tại đỉnh $C$',
                           'formula': '$\\widehat{ACx} = \\widehat{A} + \\widehat{B}$'}]}],
  'example': 'Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 50^\\circ$. Tính số đo góc '
             '$\\widehat{C}$ và góc ngoài tại đỉnh $C$.',
  'example_answer': 'Áp dụng định lí tổng ba góc trong $\\triangle ABC$:\n'
                    '$\\widehat{C} = 180^\\circ - (\\widehat{A} + \\widehat{B}) = 180^\\circ - (60^\\circ + '
                    '50^\\circ) = 70^\\circ$.\n'
                    'Góc ngoài tại đỉnh $C$ bằng $\\widehat{A} + \\widehat{B} = 60^\\circ + 50^\\circ = '
                    '110^\\circ$.',
  'real_life': 'Tính góc nghiêng của mái nhà hình chữ A khi biết hai góc ở chân mái để cắt vì kèo chính xác.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng số đo ba góc trong một tam giác bất kì luôn bằng:',
            'options': ['$90^\\circ$', '$360^\\circ$', '$120^\\circ$', '$180^\\circ$'],
            'answer': 3,
            'solution': 'Định lí tổng ba góc trong một tam giác: $\\widehat{A} + \\widehat{B} + \\widehat{C} '
                        '= 180^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một tam giác vuông, tổng số đo hai góc nhọn bằng:',
            'options': ['$90^\\circ$', '$180^\\circ$', '$45^\\circ$', '$60^\\circ$'],
            'answer': 0,
            'solution': 'Trong một tam giác vuông, hai góc nhọn phụ nhau nên có tổng bằng $90^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 12: Tổng các góc trong một tam giác**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Tổng ba góc trong $\\triangle ABC$**?',
            'options': ['$\\triangle ABC$ vuông tại $A$ $\\Rightarrow \\widehat{B} + \\widehat{C} = '
                        '90^\\circ$',
                        '$\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$',
                        '$\\widehat{ACx} = \\widehat{A} + \\widehat{B}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 12: Tổng các góc trong một tam giác, **Tổng '
                        'ba góc trong $\\triangle ABC$** được xác định bởi: $\\widehat{A} + \\widehat{B} + '
                        '\\widehat{C} = 180^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Tổng các góc trong một tam giác**, nội dung/biểu thức $\\triangle ABC$ '
                 'vuông tại $A$ $\\Rightarrow \\widehat{B} + \\widehat{C} = 90^\\circ$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Tổng ba góc trong $\\triangle ABC$',
                        'Góc ngoài tại đỉnh $C$',
                        'Hai góc nhọn trong tam giác vuông',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 12: Tổng các góc trong một tam giác, biểu thức/quy tắc $\\triangle ABC$ '
                        'vuông tại $A$ $\\Rightarrow \\widehat{B} + \\widehat{C} = 90^\\circ$ chính là nội '
                        'dung của **Hai góc nhọn trong tam giác vuông**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có $\\widehat{A} = 75^\\circ, \\widehat{B} = 45^\\circ$. Số đo góc '
                 '$\\widehat{C}$ là:',
            'options': ['$50^\\circ$', '$70^\\circ$', '$80^\\circ$', '$60^\\circ$'],
            'answer': 3,
            'solution': '$\\widehat{C} = 180^\\circ - (75^\\circ + 45^\\circ) = 60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Tổng các góc trong một tam giác** (Chương IV: Tam giác bằng nhau), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Giải thích được định lí về tổng các góc trong một tam giác bằng $180^\\circ$.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 12: Tổng các góc trong một tam giác: Giải thích được '
                        'định lí về tổng các góc trong một tam giác bằng $180^\\circ$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle MNP$ có $\\widehat{M} = 90^\\circ$ và $\\widehat{N} = 35^\\circ$. Xét các '
                 'khẳng định sau:',
            'statements': ['$\\triangle MNP$ là tam giác vuông tại $M$.',
                           'Số đo góc $\\widehat{P}$ bằng $55^\\circ$.',
                           'Góc ngoài tại đỉnh $P$ có số đo bằng $125^\\circ$.',
                           'Một tam giác có thể có đồng thời hai góc vuông.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $\\widehat{P} = 90^\\circ - 35^\\circ = 55^\\circ$. c) Đúng vì '
                        'góc ngoài tại $P$ bằng $\\widehat{M} + \\widehat{N} = 90^\\circ + 35^\\circ = '
                        '125^\\circ$. d) Sai vì nếu có hai góc vuông thì tổng ba góc lớn hơn $180^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 12: Tổng các góc trong '
                 'một tam giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Giải thích được định lí về tổng '
                           'các góc trong một tam giác bằng $180^\\circ$.',
                           'Quy tắc/công thức **Tổng ba góc trong $\\triangle ABC$** trong bài được xác định '
                           'bởi: $\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$.',
                           'Trong mọi trường hợp, **Tổng ba góc trong $\\triangle ABC$** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 12: Tổng các góc trong một tam giác.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ, '
                           '\\widehat{B} = 50^\\circ$. Tính số đo góc $\\widehat{C}$ và góc ngoài tại đỉnh '
                           '$C$.”, lời giải đúng là: Áp dụng định lí tổng ba góc trong $\\triangle ABC$: '
                           '$\\widehat{C} = 180^\\circ - (\\widehat{A} + \\widehat{B}) = 180^\\circ - '
                           '(60^\\circ + 50^\\circ) = 70^\\circ$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Tổng các góc trong một tam giác. b) '
                        '**Đúng** theo công thức trọng tâm **Tổng ba góc trong $\\triangle ABC$** '
                        '($\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$). c) **Sai** vì '
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Tổng ba góc trong $\\triangle ABC$**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 12: Tổng các góc trong một tam giác** để giải quyết tình huống '
                 'sau: Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 50^\\circ$. Tính số '
                 'đo góc $\\widehat{C}$ và góc ngoài tại đỉnh $C$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng định lí tổng ba góc trong $\\triangle ABC$: $\\widehat{C} = 180^\\circ - '
                        '(\\widehat{A} + \\widehat{B}) = 180^\\circ - (60^\\circ + 50^\\circ) = '
                        '70^\\circ$....',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Tổng các góc trong một tam giác: Áp dụng định lí '
                        'tổng ba góc trong $\\triangle ABC$:\n'
                        '$\\widehat{C} = 180^\\circ - (\\widehat{A} + \\widehat{B}) = 180^\\circ - '
                        '(60^\\circ + 50^\\circ) = 70^\\circ$.\n'
                        'Góc ngoài tại đỉnh $C$ bằng $\\widehat{A} + \\widehat{B} = 60^\\circ + 50^\\circ = '
                        '110^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ có số đo ba góc $\\widehat{A}, \\widehat{B}, \\widehat{C}$ lần lượt '
                 'tỉ lệ với $1; 2; 3$. Tính số đo góc lớn nhất của tam giác (đơn vị độ).',
            'answer': ['90'],
            'unit': None,
            'solution': 'Tổng số phần bằng nhau là $1 + 2 + 3 = 6$. Góc lớn nhất là $\\widehat{C} = '
                        '\\dfrac{180^\\circ}{6} \\cdot 3 = 90^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch04-tam-giac-bang-nhau',
  'context_title': 'Chương IV: Tam giác bằng nhau',
  'context': 'Chương IV · SGK Toán 7: Tổng các góc trong tam giác, các trường hợp bằng nhau của tam giác và '
             'tam giác cân.',
  'title': 'Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất (c.c.c)',
  'icon': '📐',
  'description': 'Định nghĩa hai tam giác bằng nhau, cách viết kí hiệu và trường hợp bằng nhau thứ nhất của '
                 'tam giác cạnh - cạnh - cạnh (c.c.c).',
  'requirements': ['Nhận biết được hai tam giác bằng nhau và chỉ ra các cạnh tương ứng, các góc tương ứng '
                   'bằng nhau.',
                   'Giải thích và vận dụng được trường hợp bằng nhau thứ nhất của hai tam giác: cạnh - cạnh '
                   '- cạnh (c.c.c).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Định nghĩa $\\triangle ABC = \\triangle '
                   "A'B'C'$** ($\\begin{cases} AB = A'B', \\; BC = B'C', \\; CA = C'A' \\\\ \\widehat{A} = "
                   "\\widehat{A'}, \\; \\widehat{B} = \\widehat{B'}, \\; \\widehat{C} = \\widehat{C'} "
                   '\\end{cases}$) vào giải bài tập.'],
  'definition': 'Hai tam giác bằng nhau là hai tam giác có các cạnh tương ứng bằng nhau và các góc tương ứng '
                'bằng nhau. Nếu ba cạnh của tam giác này bằng ba cạnh của tam giác kia thì hai tam giác đó '
                'bằng nhau (trường hợp c.c.c).',
  'theory': "1. Hai tam giác bằng nhau: Khi kí hiệu $\\triangle ABC = \\triangle A'B'C'$, ta quy ước viết "
            "các đỉnh tương ứng theo cùng một thứ tự: $A$ tương ứng với $A'$, $B$ tương ứng với $B'$, $C$ "
            "tương ứng với $C'$.\n"
            "2. Trường hợp bằng nhau thứ nhất (cạnh - cạnh - cạnh): Nếu $AB = A'B'$, $BC = B'C'$, $CA = "
            "C'A'$ thì $\\triangle ABC = \\triangle A'B'C'$ (c.c.c).",
  'formulas': [{'category': 'Hai tam giác bằng nhau và trường hợp c.c.c',
                'items': [{'name': "Định nghĩa $\\triangle ABC = \\triangle A'B'C'$",
                           'formula': "$\\begin{cases} AB = A'B', \\; BC = B'C', \\; CA = C'A' \\\\ "
                                      "\\widehat{A} = \\widehat{A'}, \\; \\widehat{B} = \\widehat{B'}, \\; "
                                      "\\widehat{C} = \\widehat{C'} \\end{cases}$"},
                          {'name': 'Trường hợp cạnh - cạnh - cạnh (c.c.c)',
                           'formula': "$AB = A'B', \\; BC = B'C', \\; CA = C'A' \\Rightarrow \\triangle ABC "
                                      "= \\triangle A'B'C'$"}]}],
  'example': 'Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = 5\\text{ cm}, BC = 7\\text{ cm}, DF = '
             '6\\text{ cm}$. Tính chu vi của $\\triangle ABC$.',
  'example_answer': 'Vì $\\triangle ABC = \\triangle DEF$ nên các cạnh tương ứng bằng nhau: $AC = DF = '
                    '6\\text{ cm}$.\n'
                    'Chu vi của $\\triangle ABC$ là $AB + BC + AC = 5 + 7 + 6 = 18\\text{ (cm)}$.',
  'real_life': 'Trong xây dựng cầu giàn thép, các khung hình tam giác có độ dài ba thanh cố định luôn giữ '
               'nguyên hình dạng và góc (tính cứng vững của khung tam giác theo trường hợp c.c.c).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC = \\triangle MNP$. Cạnh tương ứng với cạnh $BC$ là:',
            'options': ['$NP$', '$MN$', '$MP$', '$AB$'],
            'answer': 0,
            'solution': 'Theo đúng thứ tự đỉnh của $\\triangle ABC = \\triangle MNP$, hai đỉnh cuối $BC$ '
                        'tương ứng với $NP$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu $\\triangle ABC$ và $\\triangle DEF$ có $AB = DE, BC = EF, AC = DF$ thì:',
            'options': ['$\\triangle ABC = \\triangle EDF$',
                        '$\\triangle ABC = \\triangle DEF$',
                        '$\\triangle ABC = \\triangle DFE$',
                        '$\\triangle ABC = \\triangle FED$'],
            'answer': 1,
            'solution': 'Đỉnh $A$ tương ứng với $D$, $B$ tương ứng với $E$, $C$ tương ứng với $F$ nên '
                        '$\\triangle ABC = \\triangle DEF$ (c.c.c).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ '
                 'nhất (c.c.c)**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Định nghĩa $\\triangle '
                 "ABC = \\triangle A'B'C'$**?",
            'options': ["$AB = A'B', \\; BC = B'C', \\; CA = C'A' \\Rightarrow \\triangle ABC = \\triangle "
                        "A'B'C'$",
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        "$\\begin{cases} AB = A'B', \\; BC = B'C', \\; CA = C'A' \\\\ \\widehat{A} = "
                        "\\widehat{A'}, \\; \\widehat{B} = \\widehat{B'}, \\; \\widehat{C} = \\widehat{C'} "
                        '\\end{cases}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 13: Hai tam giác bằng nhau. Trường hợp bằng '
                        "nhau thứ nhất (c.c.c), **Định nghĩa $\\triangle ABC = \\triangle A'B'C'$** được xác "
                        "định bởi: $\\begin{cases} AB = A'B', \\; BC = B'C', \\; CA = C'A' \\\\ \\widehat{A} "
                        "= \\widehat{A'}, \\; \\widehat{B} = \\widehat{B'}, \\; \\widehat{C} = \\widehat{C'} "
                        '\\end{cases}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất (c.c.c)**, nội '
                 "dung/biểu thức $AB = A'B', \\; BC = B'C', \\; CA = C'A' \\Rightarrow \\triangle ABC = "
                 "\\triangle A'B'C'$ là quy tắc hoặc công thức của mục nào sau đây?",
            'options': ["Định nghĩa $\\triangle ABC = \\triangle A'B'C'$",
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp',
                        'Trường hợp cạnh - cạnh - cạnh (c.c.c)'],
            'answer': 3,
            'solution': 'Trong Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất (c.c.c), biểu '
                        "thức/quy tắc $AB = A'B', \\; BC = B'C', \\; CA = C'A' \\Rightarrow \\triangle ABC = "
                        "\\triangle A'B'C'$ chính là nội dung của **Trường hợp cạnh - cạnh - cạnh "
                        '(c.c.c)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC = \\triangle HIK$, biết $\\widehat{A} = 55^\\circ, \\widehat{I} = '
                 '65^\\circ$. Số đo góc $\\widehat{K}$ là:',
            'options': ['$60^\\circ$', '$55^\\circ$', '$65^\\circ$', '$70^\\circ$'],
            'answer': 0,
            'solution': 'Vì $\\triangle ABC = \\triangle HIK$ nên $\\widehat{H} = \\widehat{A} = 55^\\circ$. '
                        'Trong $\\triangle HIK$, $\\widehat{K} = 180^\\circ - (55^\\circ + 65^\\circ) = '
                        '60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất (c.c.c)** (Chương '
                 'IV: Tam giác bằng nhau), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Nhận biết được hai tam giác bằng nhau và chỉ ra các cạnh tương ứng, các góc tương '
                        'ứng bằng nhau.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ '
                        'nhất (c.c.c): Nhận biết được hai tam giác bằng nhau và chỉ ra các cạnh tương ứng, '
                        'các góc tương ứng bằng nhau.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tứ giác $ABCD$ có $AB = AD$ và $CB = CD$. Xét $\\triangle ABC$ và $\\triangle ADC$, '
                 'các khẳng định sau đúng hay sai?',
            'statements': ['Cạnh $AC$ là cạnh chung của hai tam giác $\\triangle ABC$ và $\\triangle ADC$.',
                           '$\\triangle ABC = \\triangle ADC$ theo trường hợp cạnh - cạnh - cạnh (c.c.c).',
                           'Góc $\\widehat{ABC}$ bằng góc $\\widehat{ADC}$.',
                           'Tia $AC$ là tia phân giác của góc $\\widehat{BAD}$.'],
            'answer': [True, True, True, True],
            'solution': 'Cả 4 ý đều đúng vì $AB = AD, BC = DC$ và $AC$ chung nên $\\triangle ABC = '
                        '\\triangle ADC$ (c.c.c), suy ra $\\widehat{ABC} = \\widehat{ADC}$ và '
                        '$\\widehat{BAC} = \\widehat{DAC}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 13: Hai tam giác bằng '
                 'nhau. Trường hợp bằng nhau thứ nhất (c.c.c)**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hai tam giác bằng '
                           'nhau và chỉ ra các cạnh tương ứng, các góc tương ứng bằng nhau.',
                           "Quy tắc/công thức **Định nghĩa $\\triangle ABC = \\triangle A'B'C'$** trong bài "
                           "được xác định bởi: $\\begin{cases} AB = A'B', \\; BC = B'C', \\; CA = C'A' \\\\ "
                           "\\widehat{A} = \\widehat{A'}, \\; \\widehat{B} = \\widehat{B'}, \\; \\widehat{C} "
                           "= \\widehat{C'} \\end{cases}$.",
                           "Trong mọi trường hợp, **Định nghĩa $\\triangle ABC = \\triangle A'B'C'$** luôn "
                           'được tính bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; '
                           'a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập '
                           '$\\mathbb{Q}$) mà không cần điều kiện của Bài 13: Hai tam giác bằng nhau. Trường '
                           'hợp bằng nhau thứ nhất (c.c.c).',
                           'Với bài toán minh họa: “Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = '
                           '5\\text{ cm}, BC = 7\\text{ cm}, DF = 6\\text{ cm}$. Tính chu vi của $\\triangle '
                           'ABC$.”, lời giải đúng là: Vì $\\triangle ABC = \\triangle DEF$ nên các cạnh '
                           'tương ứng bằng nhau: $AC = DF = 6\\text{ cm}$. Chu vi của $\\triangle ABC$ là '
                           '$AB + BC + AC = 5 + 7 + 6 = 18\\text{ (cm)}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Hai tam giác bằng nhau. Trường hợp '
                        'bằng nhau thứ nhất (c.c.c). b) **Đúng** theo công thức trọng tâm **Định nghĩa '
                        "$\\triangle ABC = \\triangle A'B'C'$** ($\\begin{cases} AB = A'B', \\; BC = B'C', "
                        "\\; CA = C'A' \\\\ \\widehat{A} = \\widehat{A'}, \\; \\widehat{B} = \\widehat{B'}, "
                        "\\; \\widehat{C} = \\widehat{C'} \\end{cases}$). c) **Sai** vì $\\mathbb{Q} = "
                        '\\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 '
                        '\\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của **Định '
                        "nghĩa $\\triangle ABC = \\triangle A'B'C'$**. d) **Đúng** theo lời giải ví dụ minh "
                        'họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất '
                 '(c.c.c)** để giải quyết tình huống sau: Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = '
                 '5\\text{ cm}, BC = 7\\text{ cm}, DF = 6\\text{ cm}$. Tính chu vi của $\\triangle ABC$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Vì $\\triangle ABC = \\triangle DEF$ nên các cạnh tương ứng bằng nhau: $AC = DF = '
                        '6\\text{ cm}$. Chu vi của $\\triangle ABC$ là $AB + BC + AC = 5 + 7 + 6 = 18\\text{ '
                        '(cm)}$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ '
                        'nhất (c.c.c): Vì $\\triangle ABC = \\triangle DEF$ nên các cạnh tương ứng bằng '
                        'nhau: $AC = DF = 6\\text{ cm}$.\n'
                        'Chu vi của $\\triangle ABC$ là $AB + BC + AC = 5 + 7 + 6 = 18\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = 6\\text{ cm}, DE + EF = 14\\text{ cm}$ '
                 'và $DF = 9\\text{ cm}$. Tính chu vi của $\\triangle ABC$ (đơn vị $\\text{cm}$).',
            'answer': ['23'],
            'unit': None,
            'solution': 'Vì $\\triangle ABC = \\triangle DEF$ nên $AB + BC = DE + EF = 14\\text{ cm}$ và $AC '
                        '= DF = 9\\text{ cm}$. Chu vi $\\triangle ABC$ là $14 + 9 = 23\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch04-tam-giac-bang-nhau',
  'context_title': 'Chương IV: Tam giác bằng nhau',
  'context': 'Chương IV · SGK Toán 7: Tổng các góc trong tam giác, các trường hợp bằng nhau của tam giác và '
             'tam giác cân.',
  'title': 'Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (c.g.c và g.c.g)',
  'icon': '📐',
  'description': 'Trường hợp bằng nhau thứ hai cạnh - góc - cạnh (c.g.c) và trường hợp bằng nhau thứ ba góc '
                 '- cạnh - góc (g.c.g) của hai tam giác.',
  'requirements': ['Giải thích và vận dụng được trường hợp bằng nhau thứ hai của tam giác: cạnh - góc - cạnh '
                   '(c.g.c).',
                   'Giải thích và vận dụng được trường hợp bằng nhau thứ ba của tam giác: góc - cạnh - góc '
                   '(g.c.g).',
                   'Sử dụng các trường hợp bằng nhau của tam giác để chứng minh hai đoạn thẳng bằng nhau, '
                   'hai góc bằng nhau.'],
  'definition': 'Trường hợp c.g.c: Nếu hai cạnh và góc xen giữa của tam giác này bằng hai cạnh và góc xen '
                'giữa của tam giác kia thì hai tam giác đó bằng nhau. Trường hợp g.c.g: Nếu một cạnh và hai '
                'góc kề của tam giác này bằng một cạnh và hai góc kề của tam giác kia thì hai tam giác đó '
                'bằng nhau.',
  'theory': '1. Trường hợp bằng nhau thứ hai (cạnh - góc - cạnh): Trong $\\triangle ABC$ và $\\triangle '
            "A'B'C'$, nếu $AB = A'B'$, $\\widehat{B} = \\widehat{B'}$ (góc xen giữa hai cạnh) và $BC = B'C'$ "
            "thì $\\triangle ABC = \\triangle A'B'C'$ (c.g.c).\n"
            '2. Trường hợp bằng nhau thứ ba (góc - cạnh - góc): Trong $\\triangle ABC$ và $\\triangle '
            "A'B'C'$, nếu $\\widehat{B} = \\widehat{B'}$, $BC = B'C'$ và $\\widehat{C} = \\widehat{C'}$ (hai "
            "góc cùng kề cạnh đó) thì $\\triangle ABC = \\triangle A'B'C'$ (g.c.g).",
  'formulas': [{'category': 'Trường hợp c.g.c và g.c.g',
                'items': [{'name': 'Trường hợp cạnh - góc - cạnh (c.g.c)',
                           'formula': "$AB = A'B', \\; \\widehat{B} = \\widehat{B'}, \\; BC = B'C' "
                                      "\\Rightarrow \\triangle ABC = \\triangle A'B'C'$"},
                          {'name': 'Trường hợp góc - cạnh - góc (g.c.g)',
                           'formula': "$\\widehat{B} = \\widehat{B'}, \\; BC = B'C', \\; \\widehat{C} = "
                                      "\\widehat{C'} \\Rightarrow \\triangle ABC = \\triangle A'B'C'$"}]}],
  'example': 'Cho đoạn thẳng $AB$ và $CD$ cắt nhau tại trung điểm $O$ của mỗi đoạn. Chứng minh $\\triangle '
             'OAC = \\triangle OBD$ và $AC = BD$.',
  'example_answer': 'Xét $\\triangle OAC$ và $\\triangle OBD$ có:\n'
                    '- $OA = OB$ ($O$ là trung điểm của $AB$);\n'
                    '- $\\widehat{AOC} = \\widehat{BOD}$ (hai góc đối đỉnh);\n'
                    '- $OC = OD$ ($O$ là trung điểm của $CD$).\n'
                    'Do đó $\\triangle OAC = \\triangle OBD$ (c.g.c), suy ra $AC = BD$ (hai cạnh tương ứng).',
  'real_life': 'Đo khoảng cách giữa hai điểm ở hai bờ hồ nước mà không cần đi ngang qua mặt hồ bằng cách '
               'dựng hai tam giác bằng nhau trên bờ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ và $\\triangle DEF$ có $AB = DE$ và $BC = EF$. Cần thêm điều kiện nào '
                 'sau đây để $\\triangle ABC = \\triangle DEF$ theo trường hợp cạnh - góc - cạnh (c.g.c)?',
            'options': ['$\\widehat{A} = \\widehat{D}$',
                        '$\\widehat{B} = \\widehat{E}$',
                        '$\\widehat{C} = \\widehat{F}$',
                        '$\\widehat{B} = \\widehat{D}$'],
            'answer': 1,
            'solution': 'Góc xen giữa hai cạnh $AB, BC$ là $\\widehat{B}$; góc xen giữa hai cạnh $DE, EF$ là '
                        '$\\widehat{E}$. Vậy cần $\\widehat{B} = \\widehat{E}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ và $\\triangle MNP$ có $\\widehat{A} = \\widehat{M}$ và $\\widehat{B} '
                 '= \\widehat{N}$. Để $\\triangle ABC = \\triangle MNP$ theo trường hợp góc - cạnh - góc '
                 '(g.c.g) thì cần thêm điều kiện:',
            'options': ['$BC = NP$', '$AC = MP$', '$AB = MN$', '$AB = MP$'],
            'answer': 2,
            'solution': 'Cạnh kề với hai góc $\\widehat{A}, \\widehat{B}$ là $AB$; cạnh kề với '
                        '$\\widehat{M}, \\widehat{N}$ là $MN$. Vậy cần $AB = MN$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác '
                 '(c.g.c và g.c.g)**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Trường hợp cạnh - '
                 'góc - cạnh (c.g.c)**?',
            'options': ["$\\widehat{B} = \\widehat{B'}, \\; BC = B'C', \\; \\widehat{C} = \\widehat{C'} "
                        "\\Rightarrow \\triangle ABC = \\triangle A'B'C'$",
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$',
                        "$AB = A'B', \\; \\widehat{B} = \\widehat{B'}, \\; BC = B'C' \\Rightarrow \\triangle "
                        "ABC = \\triangle A'B'C'$"],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 14: Trường hợp bằng nhau thứ hai và thứ ba '
                        'của tam giác (c.g.c và g.c.g), **Trường hợp cạnh - góc - cạnh (c.g.c)** được xác '
                        "định bởi: $AB = A'B', \\; \\widehat{B} = \\widehat{B'}, \\; BC = B'C' \\Rightarrow "
                        "\\triangle ABC = \\triangle A'B'C'$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (c.g.c và g.c.g)**, '
                 "nội dung/biểu thức $\\widehat{B} = \\widehat{B'}, \\; BC = B'C', \\; \\widehat{C} = "
                 "\\widehat{C'} \\Rightarrow \\triangle ABC = \\triangle A'B'C'$ là quy tắc hoặc công thức "
                 'của mục nào sau đây?',
            'options': ['Trường hợp góc - cạnh - góc (g.c.g)',
                        'Trường hợp cạnh - góc - cạnh (c.g.c)',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp'],
            'answer': 0,
            'solution': 'Trong Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (c.g.c và g.c.g), '
                        "biểu thức/quy tắc $\\widehat{B} = \\widehat{B'}, \\; BC = B'C', \\; \\widehat{C} = "
                        "\\widehat{C'} \\Rightarrow \\triangle ABC = \\triangle A'B'C'$ chính là nội dung "
                        'của **Trường hợp góc - cạnh - góc (g.c.g)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho góc $\\widehat{xOy}$, trên tia $Ox$ lấy điểm $A$, trên tia $Oy$ lấy điểm $B$ sao cho '
                 '$OA = OB$. Gọi $I$ là một điểm thuộc tia phân giác của góc $\\widehat{xOy}$. Khi đó '
                 '$\\triangle OAI = \\triangle OBI$ theo trường hợp nào?',
            'options': ['c.c.c', 'c.g.c', 'g.c.g', 'Không bằng nhau'],
            'answer': 1,
            'solution': 'Ta có $OA = OB$, $\\widehat{AOI} = \\widehat{BOI}$ ($OI$ là phân giác) và $OI$ là '
                        'cạnh chung nên $\\triangle OAI = \\triangle OBI$ (c.g.c).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (c.g.c và g.c.g)** '
                 '(Chương IV: Tam giác bằng nhau), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt '
                 'và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Giải thích và vận dụng được trường hợp bằng nhau thứ hai của tam giác: cạnh - góc - '
                        'cạnh (c.g.c).',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam '
                        'giác (c.g.c và g.c.g): Giải thích và vận dụng được trường hợp bằng nhau thứ hai của '
                        'tam giác: cạnh - góc - cạnh (c.g.c).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho $\\triangle ABC$ và $\\triangle A'B'C'$. Xét tính đúng sai của các khẳng định sau:",
            'statements': ["Nếu $AB = A'B', AC = A'C'$ và $\\widehat{A} = \\widehat{A'}$ thì $\\triangle ABC "
                           "= \\triangle A'B'C'$ (c.g.c).",
                           "Nếu $AB = A'B', BC = B'C'$ và $\\widehat{A} = \\widehat{A'}$ thì luôn kết luận "
                           "được $\\triangle ABC = \\triangle A'B'C'$ (c.g.c).",
                           "Nếu $\\widehat{B} = \\widehat{B'}, BC = B'C'$ và $\\widehat{C} = \\widehat{C'}$ "
                           "thì $\\triangle ABC = \\triangle A'B'C'$ (g.c.g).",
                           "Nếu $\\widehat{A} = \\widehat{A'}, \\widehat{B} = \\widehat{B'}$ và $BC = B'C'$ "
                           "thì ta tính được $\\widehat{C} = \\widehat{C'}$ rồi suy ra $\\triangle ABC = "
                           "\\triangle A'B'C'$ (g.c.g)."],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $\\widehat{A}$ xen giữa $AB, AC$. b) Sai vì $\\widehat{A}$ không phải là '
                        'góc xen giữa hai cạnh $AB, BC$. c) Đúng. d) Đúng vì tổng 3 góc bằng $180^\\circ$ '
                        "nên $\\widehat{C} = \\widehat{C'}$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 14: Trường hợp bằng '
                 'nhau thứ hai và thứ ba của tam giác (c.g.c và g.c.g)**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Giải thích và vận dụng được trường '
                           'hợp bằng nhau thứ hai của tam giác: cạnh - góc - cạnh (c.g.c).',
                           'Quy tắc/công thức **Trường hợp cạnh - góc - cạnh (c.g.c)** trong bài được xác '
                           "định bởi: $AB = A'B', \\; \\widehat{B} = \\widehat{B'}, \\; BC = B'C' "
                           "\\Rightarrow \\triangle ABC = \\triangle A'B'C'$.",
                           'Trong mọi trường hợp, **Trường hợp cạnh - góc - cạnh (c.g.c)** luôn được tính '
                           'bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác '
                           '(c.g.c và g.c.g).',
                           'Với bài toán minh họa: “Cho đoạn thẳng $AB$ và $CD$ cắt nhau tại trung điểm $O$ '
                           'của mỗi đoạn. Chứng minh $\\triangle OAC = \\triangle OBD$ và $AC = BD$.”, lời '
                           'giải đúng là: Xét $\\triangle OAC$ và $\\triangle OBD$ có: - $OA = OB$ ($O$ là '
                           'trung điểm của $AB$); - $\\widehat{AOC} = \\widehat{BOD}$ (hai góc đối đỉnh)...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Trường hợp bằng nhau thứ hai và thứ ba '
                        'của tam giác (c.g.c và g.c.g). b) **Đúng** theo công thức trọng tâm **Trường hợp '
                        "cạnh - góc - cạnh (c.g.c)** ($AB = A'B', \\; \\widehat{B} = \\widehat{B'}, \\; BC = "
                        "B'C' \\Rightarrow \\triangle ABC = \\triangle A'B'C'$). c) **Sai** vì $\\mathbb{Q} "
                        '= \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 '
                        '\\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của **Trường '
                        'hợp cạnh - góc - cạnh (c.g.c)**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (c.g.c và '
                 'g.c.g)** để giải quyết tình huống sau: Cho đoạn thẳng $AB$ và $CD$ cắt nhau tại trung điểm '
                 '$O$ của mỗi đoạn. Chứng minh $\\triangle OAC = \\triangle OBD$ và $AC = BD$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Xét $\\triangle OAC$ và $\\triangle OBD$ có: - $OA = OB$ ($O$ là trung điểm của '
                        '$AB$); - $\\widehat{AOC} = \\widehat{BOD}$ (hai góc đối đỉnh); - $OC = OD$ ($O$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác '
                        '(c.g.c và g.c.g): Xét $\\triangle OAC$ và $\\triangle OBD$ có:\n'
                        '- $OA = OB$ ($O$ là trung điểm của $AB$);\n'
                        '- $\\widehat{AOC} = \\widehat{BOD}$ (hai góc đối đỉnh);\n'
                        '- $OC = OD$ ($O$ là trung điểm của $CD$).\n'
                        'Do đó $\\triangle OAC = \\triangle OBD$ (c.g.c), suy ra $AC = BD$ (hai cạnh tương '
                        'ứng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai đoạn thẳng $AB$ và $CD$ cắt nhau tại trung điểm $O$ của mỗi đoạn. Biết $AC = 12\\text{ '
                 'm}$, hỏi độ dài đoạn thẳng $BD$ bằng bao nhiêu mét?',
            'answer': ['12'],
            'unit': None,
            'solution': 'Vì $\\triangle OAC = \\triangle OBD$ (c.g.c) nên $BD = AC = 12\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch04-tam-giac-bang-nhau',
  'context_title': 'Chương IV: Tam giác bằng nhau',
  'context': 'Chương IV · SGK Toán 7: Tổng các góc trong tam giác, các trường hợp bằng nhau của tam giác và '
             'tam giác cân.',
  'title': 'Bài 15: Các trường hợp bằng nhau của tam giác vuông',
  'icon': '📐',
  'description': 'Bốn trường hợp bằng nhau của hai tam giác vuông, bao gồm trường hợp cạnh huyền - góc nhọn '
                 'và cạnh huyền - cạnh góc vuông.',
  'requirements': ['Giải thích và vận dụng được các trường hợp bằng nhau của hai tam giác vuông.',
                   'Đặc biệt nắm vững hai trường hợp đặc trưng: cạnh huyền - góc nhọn và cạnh huyền - cạnh '
                   'góc vuông.',
                   "Ghi nhớ và vận dụng đúng quy tắc/công thức **Hai cạnh góc vuông** ($AB = A'B', \\; AC = "
                   "A'C' \\Rightarrow \\triangle ABC = \\triangle A'B'C'$) vào giải bài tập."],
  'definition': 'Trong tam giác vuông, cạnh đối diện với góc vuông gọi là cạnh huyền, hai cạnh kề với góc '
                'vuông gọi là hai cạnh góc vuông. Hai tam giác vuông bằng nhau nếu có: hai cạnh góc vuông '
                'bằng nhau; hoặc một cạnh góc vuông và góc nhọn kề bằng nhau; hoặc cạnh huyền và một góc '
                'nhọn bằng nhau; hoặc cạnh huyền và một cạnh góc vuông bằng nhau.',
  'theory': 'Bốn trường hợp bằng nhau của hai tam giác vuông $\\triangle ABC$ (vuông tại $A$) và $\\triangle '
            "A'B'C'$ (vuông tại $A'$):\n"
            "1. Hai cạnh góc vuông: $AB = A'B'$ và $AC = A'C'$ (suy từ trường hợp c.g.c).\n"
            "2. Cạnh góc vuông - góc nhọn kề: $AB = A'B'$ và $\\widehat{B} = \\widehat{B'}$ (suy từ trường "
            'hợp g.c.g).\n'
            "3. Cạnh huyền - góc nhọn: $BC = B'C'$ và $\\widehat{B} = \\widehat{B'}$ (hoặc $\\widehat{C} = "
            "\\widehat{C'}$).\n"
            "4. Cạnh huyền - cạnh góc vuông: $BC = B'C'$ và $AB = A'B'$ (hoặc $AC = A'C'$).",
  'formulas': [{'category': "Các trường hợp bằng nhau của tam giác vuông ($\\widehat{A} = \\widehat{A'} = "
                            '90^\\circ$)',
                'items': [{'name': 'Hai cạnh góc vuông',
                           'formula': "$AB = A'B', \\; AC = A'C' \\Rightarrow \\triangle ABC = \\triangle "
                                      "A'B'C'$"},
                          {'name': 'Cạnh góc vuông - góc nhọn kề',
                           'formula': "$AB = A'B', \\; \\widehat{B} = \\widehat{B'} \\Rightarrow \\triangle "
                                      "ABC = \\triangle A'B'C'$"},
                          {'name': 'Cạnh huyền - góc nhọn',
                           'formula': "$BC = B'C', \\; \\widehat{B} = \\widehat{B'} \\Rightarrow \\triangle "
                                      "ABC = \\triangle A'B'C'$"},
                          {'name': 'Cạnh huyền - cạnh góc vuông',
                           'formula': "$BC = B'C', \\; AB = A'B' \\Rightarrow \\triangle ABC = \\triangle "
                                      "A'B'C'$"}]}],
  'example': 'Cho $\\triangle ABC$ có $AB = AC$. Kẻ $AH \\perp BC$ tại $H$. Chứng minh $\\triangle AHB = '
             '\\triangle AHC$ và $HB = HC$.',
  'example_answer': 'Xét hai tam giác vuông $\\triangle AHB$ (vuông tại $H$) và $\\triangle AHC$ (vuông tại '
                    '$H$) có:\n'
                    '- Cạnh huyền $AB = AC$ (giả thiết);\n'
                    '- Cạnh góc vuông $AH$ chung.\n'
                    'Do đó $\\triangle AHB = \\triangle AHC$ (cạnh huyền - cạnh góc vuông), suy ra $HB = '
                    'HC$.',
  'real_life': 'Kiểm tra hai thang tựa vào tường có cùng độ dài và cùng độ cao chân thang sẽ đặt ở cùng một '
               'khoảng cách trên mặt đất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai tam giác vuông $\\triangle ABC$ (vuông tại $A$) và $\\triangle DEF$ (vuông tại '
                 '$D$) có cạnh huyền $BC = EF$ và $AB = DE$. Hai tam giác này bằng nhau theo trường hợp nào?',
            'options': ['Cạnh huyền - góc nhọn',
                        'Hai cạnh góc vuông',
                        'Cạnh huyền - cạnh góc vuông',
                        'Cạnh góc vuông - góc nhọn kề'],
            'answer': 2,
            'solution': '$BC, EF$ là cạnh huyền và $AB, DE$ là cạnh góc vuông nên hai tam giác vuông bằng '
                        'nhau theo trường hợp cạnh huyền - cạnh góc vuông.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai tam giác vuông $\\triangle ABC$ (vuông tại $A$) và $\\triangle MNP$ (vuông tại '
                 '$M$) có $BC = NP$ và $\\widehat{B} = \\widehat{N}$. Khi đó $\\triangle ABC = \\triangle '
                 'MNP$ theo trường hợp:',
            'options': ['Cạnh huyền - cạnh góc vuông',
                        'Hai cạnh góc vuông',
                        'Cạnh - cạnh - cạnh',
                        'Cạnh huyền - góc nhọn'],
            'answer': 3,
            'solution': '$BC = NP$ là hai cạnh huyền và $\\widehat{B} = \\widehat{N}$ là hai góc nhọn nên '
                        'bằng nhau theo trường hợp cạnh huyền - góc nhọn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 15: Các trường hợp bằng nhau của tam giác vuông**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Hai cạnh góc vuông**?',
            'options': ["$AB = A'B', \\; AC = A'C' \\Rightarrow \\triangle ABC = \\triangle A'B'C'$",
                        "$AB = A'B', \\; \\widehat{B} = \\widehat{B'} \\Rightarrow \\triangle ABC = "
                        "\\triangle A'B'C'$",
                        "$BC = B'C', \\; \\widehat{B} = \\widehat{B'} \\Rightarrow \\triangle ABC = "
                        "\\triangle A'B'C'$",
                        "$BC = B'C', \\; AB = A'B' \\Rightarrow \\triangle ABC = \\triangle A'B'C'$"],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 15: Các trường hợp bằng nhau của tam giác '
                        "vuông, **Hai cạnh góc vuông** được xác định bởi: $AB = A'B', \\; AC = A'C' "
                        "\\Rightarrow \\triangle ABC = \\triangle A'B'C'$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Các trường hợp bằng nhau của tam giác vuông**, nội dung/biểu thức $AB = '
                 "A'B', \\; \\widehat{B} = \\widehat{B'} \\Rightarrow \\triangle ABC = \\triangle A'B'C'$ là "
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hai cạnh góc vuông',
                        'Cạnh góc vuông - góc nhọn kề',
                        'Cạnh huyền - góc nhọn',
                        'Cạnh huyền - cạnh góc vuông'],
            'answer': 1,
            'solution': 'Trong Bài 15: Các trường hợp bằng nhau của tam giác vuông, biểu thức/quy tắc $AB = '
                        "A'B', \\; \\widehat{B} = \\widehat{B'} \\Rightarrow \\triangle ABC = \\triangle "
                        "A'B'C'$ chính là nội dung của **Cạnh góc vuông - góc nhọn kề**."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tia $Oz$ là tia phân giác của góc $\\widehat{xOy}$. Lấy điểm $M$ trên tia $Oz$, kẻ $MA '
                 '\\perp Ox$ tại $A$ và $MB \\perp Oy$ tại $B$. Khẳng định nào sau đây đúng?',
            'options': ['$\\triangle OAM = \\triangle OBM$ (c.c.c)',
                        '$MA > MB$',
                        '$\\triangle OAM = \\triangle OBM$ (cạnh huyền - góc nhọn)',
                        '$OA \\neq OB$'],
            'answer': 2,
            'solution': 'Hai tam giác vuông $\\triangle OAM$ và $\\triangle OBM$ có cạnh huyền $OM$ chung và '
                        '$\\widehat{AOM} = \\widehat{BOM}$ nên $\\triangle OAM = \\triangle OBM$ (cạnh huyền '
                        '- góc nhọn).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Các trường hợp bằng nhau của tam giác vuông** (Chương IV: Tam giác bằng '
                 'nhau), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Giải thích và vận dụng được các trường hợp bằng nhau của hai tam giác vuông.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 15: Các trường hợp bằng nhau của tam giác vuông: Giải '
                        'thích và vận dụng được các trường hợp bằng nhau của hai tam giác vuông.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có đường cao $AH \\perp BC$ tại $H$. Biết $AB = AC = 10\\text{ cm}$ '
                 'và $BH = 6\\text{ cm}$. Xét các khẳng định sau:',
            'statements': ['Hai tam giác vuông $\\triangle AHB$ và $\\triangle AHC$ có cạnh góc vuông $AH$ '
                           'chung.',
                           '$\\triangle AHB = \\triangle AHC$ theo trường hợp cạnh huyền - cạnh góc vuông.',
                           'Độ dài đoạn thẳng $HC$ bằng $6\\text{ cm}$.',
                           'Tia $AH$ là tia phân giác của góc $\\widehat{BAC}$.'],
            'answer': [True, True, True, True],
            'solution': 'Cả 4 ý đều đúng vì $\\triangle AHB = \\triangle AHC$ (cạnh huyền - cạnh góc vuông) '
                        'nên $HC = BH = 6\\text{ cm}$ và $\\widehat{BAH} = \\widehat{CAH}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 15: Các trường hợp bằng '
                 'nhau của tam giác vuông**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Giải thích và vận dụng được các '
                           'trường hợp bằng nhau của hai tam giác vuông.',
                           'Quy tắc/công thức **Hai cạnh góc vuông** trong bài được xác định bởi: $AB = '
                           "A'B', \\; AC = A'C' \\Rightarrow \\triangle ABC = \\triangle A'B'C'$.",
                           'Trong mọi trường hợp, **Hai cạnh góc vuông** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 15: Các trường hợp bằng nhau của tam giác vuông.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ có $AB = AC$. Kẻ $AH \\perp BC$ tại '
                           '$H$. Chứng minh $\\triangle AHB = \\triangle AHC$ và $HB = HC$.”, lời giải đúng '
                           'là: Xét hai tam giác vuông $\\triangle AHB$ (vuông tại $H$) và $\\triangle AHC$ '
                           '(vuông tại $H$) có: - Cạnh huyền $AB = AC$ (giả thiết); - Cạnh góc...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Các trường hợp bằng nhau của tam giác '
                        "vuông. b) **Đúng** theo công thức trọng tâm **Hai cạnh góc vuông** ($AB = A'B', \\; "
                        "AC = A'C' \\Rightarrow \\triangle ABC = \\triangle A'B'C'$). c) **Sai** vì "
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Hai cạnh góc vuông**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 15: Các trường hợp bằng nhau của tam giác vuông** để giải quyết '
                 'tình huống sau: Cho $\\triangle ABC$ có $AB = AC$. Kẻ $AH \\perp BC$ tại $H$. Chứng minh '
                 '$\\triangle AHB = \\triangle AHC$ và $HB = HC$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Xét hai tam giác vuông $\\triangle AHB$ (vuông tại $H$) và $\\triangle AHC$ (vuông '
                        'tại $H$) có: - Cạnh huyền $AB = AC$ (giả thiết); - Cạnh góc vuông $AH$ chu...',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Các trường hợp bằng nhau của tam giác vuông: Xét hai '
                        'tam giác vuông $\\triangle AHB$ (vuông tại $H$) và $\\triangle AHC$ (vuông tại $H$) '
                        'có:\n'
                        '- Cạnh huyền $AB = AC$ (giả thiết);\n'
                        '- Cạnh góc vuông $AH$ chung.\n'
                        'Do đó $\\triangle AHB = \\triangle AHC$ (cạnh huyền - cạnh góc vuông), suy ra $HB = '
                        'HC$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hai tam giác vuông $\\triangle ABC$ (vuông tại $A$) và $\\triangle DEF$ (vuông tại '
                 '$D$) có $BC = EF = 13\\text{ cm}$, $\\widehat{B} = \\widehat{E}$ và $AB = 5\\text{ cm}$. '
                 'Tính độ dài đoạn thẳng $DE$ (đơn vị $\\text{cm}$).',
            'answer': ['5'],
            'unit': None,
            'solution': 'Vì $\\triangle ABC = \\triangle DEF$ (cạnh huyền - góc nhọn) nên $DE = AB = '
                        '5\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch04-tam-giac-bang-nhau',
  'context_title': 'Chương IV: Tam giác bằng nhau',
  'context': 'Chương IV · SGK Toán 7: Tổng các góc trong tam giác, các trường hợp bằng nhau của tam giác và '
             'tam giác cân.',
  'title': 'Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng',
  'icon': '⛺',
  'description': 'Định nghĩa, tính chất, dấu hiệu nhận biết tam giác cân, tam giác đều và đường trung trực '
                 'của một đoạn thẳng.',
  'requirements': ['Mô tả được tam giác cân, tính chất hai góc ở đáy của tam giác cân và dấu hiệu nhận biết '
                   'tam giác cân, tam giác đều.',
                   'Nhận biết được đường trung trực của một đoạn thẳng và tính chất cơ bản của đường trung '
                   'trực.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tính chất góc ở đáy ($\\triangle ABC$ cân '
                   'tại $A$)** ($\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - \\widehat{A}}{2}$) vào '
                   'giải bài tập.'],
  'definition': 'Tam giác cân là tam giác có hai cạnh bằng nhau. Đường thẳng vuông góc với một đoạn thẳng '
                'tại trung điểm của nó được gọi là đường trung trực của đoạn thẳng đó.',
  'theory': '1. Tam giác cân:\n'
            '- Trong một tam giác cân, hai cạnh bằng nhau gọi là hai cạnh bên, cạnh còn lại gọi là cạnh đáy; '
            'hai góc kề với cạnh đáy gọi là hai góc ở đáy.\n'
            '- Tính chất: Trong một tam giác cân, hai góc ở đáy bằng nhau.\n'
            '- Dấu hiệu nhận biết: Nếu một tam giác có hai góc bằng nhau thì tam giác đó là tam giác cân.\n'
            '- Tam giác đều là tam giác có ba cạnh bằng nhau; trong tam giác đều mỗi góc bằng $60^\\circ$. '
            'Tam giác vuông cân là tam giác vuông có hai cạnh góc vuông bằng nhau (mỗi góc ở đáy bằng '
            '$45^\\circ$).\n'
            '2. Đường trung trực của đoạn thẳng: Điểm nằm trên đường trung trực của một đoạn thẳng thì cách '
            'đều hai mút của đoạn thẳng đó. Ngược lại, điểm cách đều hai mút của một đoạn thẳng thì nằm trên '
            'đường trung trực của đoạn thẳng đó.',
  'formulas': [{'category': 'Hệ thức tam giác cân và đường trung trực',
                'items': [{'name': 'Tính chất góc ở đáy ($\\triangle ABC$ cân tại $A$)',
                           'formula': '$\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - '
                                      '\\widehat{A}}{2}$'},
                          {'name': 'Tính góc ở đỉnh ($\\triangle ABC$ cân tại $A$)',
                           'formula': '$\\widehat{A} = 180^\\circ - 2\\widehat{B}$'},
                          {'name': 'Tam giác đều $\\triangle ABC$',
                           'formula': '$AB = BC = CA \\Leftrightarrow \\widehat{A} = \\widehat{B} = '
                                      '\\widehat{C} = 60^\\circ$'},
                          {'name': 'Tính chất đường trung trực $d$ của $AB$',
                           'formula': '$M \\in d \\Leftrightarrow MA = MB$'}]}],
  'example': 'Cho $\\triangle ABC$ cân tại $A$, biết góc ở đỉnh $\\widehat{A} = 50^\\circ$. Tính số đo hai '
             'góc ở đáy $\\widehat{B}$ và $\\widehat{C}$.',
  'example_answer': 'Vì $\\triangle ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C}$.\n'
                    'Mà $\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ \\Rightarrow \\widehat{B} = '
                    '\\widehat{C} = \\dfrac{180^\\circ - 50^\\circ}{2} = 65^\\circ$.',
  'real_life': 'Xác định vị trí xây trạm phát sóng hoặc giếng nước trên một tuyến đường thẳng sao cho cách '
               'đều hai ngôi làng $A$ và $B$ (giao điểm của đường thẳng với đường trung trực của $AB$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ cân tại $A$. Khẳng định nào sau đây là đúng?',
            'options': ['$\\widehat{A} = \\widehat{B}$',
                        '$\\widehat{A} = \\widehat{C}$',
                        '$AB = BC$',
                        '$\\widehat{B} = \\widehat{C}$'],
            'answer': 3,
            'solution': 'Trong tam giác $\\triangle ABC$ cân tại $A$, hai góc ở đáy là $\\widehat{B}$ và '
                        '$\\widehat{C}$ bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Mỗi góc của một tam giác đều có số đo bằng:',
            'options': ['$60^\\circ$', '$45^\\circ$', '$90^\\circ$', '$180^\\circ$'],
            'answer': 0,
            'solution': 'Trong tam giác đều, ba góc bằng nhau và tổng bằng $180^\\circ$ nên mỗi góc bằng '
                        '$60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tính chất góc ở đáy ($\\triangle ABC$ '
                 'cân tại $A$)**?',
            'options': ['$\\widehat{A} = 180^\\circ - 2\\widehat{B}$',
                        '$\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - \\widehat{A}}{2}$',
                        '$AB = BC = CA \\Leftrightarrow \\widehat{A} = \\widehat{B} = \\widehat{C} = '
                        '60^\\circ$',
                        '$M \\in d \\Leftrightarrow MA = MB$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 16: Tam giác cân. Đường trung trực của đoạn '
                        'thẳng, **Tính chất góc ở đáy ($\\triangle ABC$ cân tại $A$)** được xác định bởi: '
                        '$\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - \\widehat{A}}{2}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng**, nội dung/biểu thức '
                 '$\\widehat{A} = 180^\\circ - 2\\widehat{B}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tính chất góc ở đáy ($\\triangle ABC$ cân tại $A$)',
                        'Tam giác đều $\\triangle ABC$',
                        'Tính góc ở đỉnh ($\\triangle ABC$ cân tại $A$)',
                        'Tính chất đường trung trực $d$ của $AB$'],
            'answer': 2,
            'solution': 'Trong Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng, biểu thức/quy tắc '
                        '$\\widehat{A} = 180^\\circ - 2\\widehat{B}$ chính là nội dung của **Tính góc ở đỉnh '
                        '($\\triangle ABC$ cân tại $A$)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{B} = 70^\\circ$. Số đo góc ở đỉnh '
                 '$\\widehat{A}$ là:',
            'options': ['$70^\\circ$', '$55^\\circ$', '$110^\\circ$', '$40^\\circ$'],
            'answer': 3,
            'solution': 'Vì $\\triangle ABC$ cân tại $A$ nên $\\widehat{C} = \\widehat{B} = 70^\\circ '
                        '\\Rightarrow \\widehat{A} = 180^\\circ - 2 \\cdot 70^\\circ = 40^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng** (Chương IV: Tam giác '
                 'bằng nhau), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Mô tả được tam giác cân, tính chất hai góc ở đáy của tam giác cân và dấu hiệu nhận '
                        'biết tam giác cân, tam giác đều.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng: Mô '
                        'tả được tam giác cân, tính chất hai góc ở đáy của tam giác cân và dấu hiệu nhận '
                        'biết tam giác cân, tam giác đều.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đoạn thẳng $AB = 8\\text{ cm}$ có trung điểm $I$ và đường trung trực $d$. Lấy điểm $M$ '
                 'thuộc $d$ (khác $I$). Xét các khẳng định sau:',
            'statements': ['Độ dài đoạn thẳng $IA = IB = 4\\text{ cm}$ và $d \\perp AB$ tại $I$.',
                           'Điểm $M$ cách đều hai đầu mút $A$ và $B$ ($MA = MB$).',
                           '$\\triangle MAB$ là tam giác cân tại $M$.',
                           'Mọi điểm $N$ thỏa mãn $NA = NB$ đều nằm ngoài đường thẳng $d$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng theo định nghĩa và tính chất đường trung trực. d) Sai vì mọi điểm '
                        'cách đều $A$ và $B$ đều nằm trên đường trung trực $d$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 16: Tam giác cân. Đường '
                 'trung trực của đoạn thẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được tam giác cân, tính chất '
                           'hai góc ở đáy của tam giác cân và dấu hiệu nhận biết tam giác cân, tam giác đều.',
                           'Quy tắc/công thức **Tính chất góc ở đáy ($\\triangle ABC$ cân tại $A$)** trong '
                           'bài được xác định bởi: $\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - '
                           '\\widehat{A}}{2}$.',
                           'Trong mọi trường hợp, **Tính chất góc ở đáy ($\\triangle ABC$ cân tại $A$)** '
                           'luôn được tính bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                           '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa '
                           'tập $\\mathbb{Q}$) mà không cần điều kiện của Bài 16: Tam giác cân. Đường trung '
                           'trực của đoạn thẳng.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ cân tại $A$, biết góc ở đỉnh '
                           '$\\widehat{A} = 50^\\circ$. Tính số đo hai góc ở đáy $\\widehat{B}$ và '
                           '$\\widehat{C}$.”, lời giải đúng là: Vì $\\triangle ABC$ cân tại $A$ nên '
                           '$\\widehat{B} = \\widehat{C}$. Mà...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Tam giác cân. Đường trung trực của '
                        'đoạn thẳng. b) **Đúng** theo công thức trọng tâm **Tính chất góc ở đáy ($\\triangle '
                        'ABC$ cân tại $A$)** ($\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - '
                        '\\widehat{A}}{2}$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Tính chất góc ở đáy ($\\triangle ABC$ cân '
                        'tại $A$)**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng** để giải quyết '
                 'tình huống sau: Cho $\\triangle ABC$ cân tại $A$, biết góc ở đỉnh $\\widehat{A} = '
                 '50^\\circ$. Tính số đo hai góc ở đáy $\\widehat{B}$ và $\\widehat{C}$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Vì $\\triangle ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C}$. Mà $\\widehat{A} '
                        '+ \\widehat{B} + \\widehat{C} = 180^\\circ \\Rightarrow \\widehat{B} = \\widehat{C} '
                        '= \\dfrac{180^\\circ - 50^\\circ}{2} = 65^\\circ$...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng: Vì '
                        '$\\triangle ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C}$.\n'
                        'Mà $\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ \\Rightarrow '
                        '\\widehat{B} = \\widehat{C} = \\dfrac{180^\\circ - 50^\\circ}{2} = 65^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ cân tại $A$ có góc ở đỉnh $\\widehat{A} = 80^\\circ$. Tính số đo góc '
                 'ở đáy $\\widehat{B}$ (đơn vị độ).',
            'answer': ['50'],
            'unit': None,
            'solution': 'Ta có $\\widehat{B} = \\dfrac{180^\\circ - 80^\\circ}{2} = 50^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch05-thu-thap-bieu-dien-du-lieu',
  'context_title': 'Chương V: Thu thập và biểu diễn dữ liệu',
  'context': 'Chương V · SGK Toán 7: Thu thập, phân loại dữ liệu và đọc, phân tích biểu đồ hình quạt tròn, '
             'biểu đồ đoạn thẳng.',
  'title': 'Bài 17: Thu thập và phân loại dữ liệu',
  'icon': '📋',
  'description': 'Các phương pháp thu thập dữ liệu, phân loại dữ liệu định tính và dữ liệu định lượng, tính '
                 'đại diện của dữ liệu.',
  'requirements': ['Thực hiện và lí giải được việc thu thập, phân loại dữ liệu theo các tiêu chí cho trước.',
                   'Phân biệt được dữ liệu là số (số liệu / định lượng) và dữ liệu không là số (định tính).',
                   'Nhận biết được tính hợp lí và tính đại diện của dữ liệu thu thập được.'],
  'definition': 'Dữ liệu được chia thành hai loại chính: Dữ liệu là số (dữ liệu định lượng, còn gọi là số '
                'liệu) và dữ liệu không là số (dữ liệu định tính, chia thành loại có thể sắp thứ tự và loại '
                'không thể sắp thứ tự).',
  'theory': '1. Thu thập dữ liệu: Có thể thu thập trực tiếp qua quan sát, làm thí nghiệm, lập phiếu hỏi, '
            'phỏng vấn hoặc gián tiếp từ các nguồn có sẵn (sách báo, niên giám thống kê, Internet).\n'
            '2. Phân loại dữ liệu:\n'
            '- Dữ liệu là số (số liệu): Chiều cao, cân nặng, điểm số, nhiệt độ.\n'
            '- Dữ liệu không là số: Tên môn thể thao yêu thích (không thể sắp thứ tự); mức độ đánh giá Tốt / '
            'Khá / Đạt / Chưa đạt (có thể sắp thứ tự).\n'
            '3. Tính đại diện của dữ liệu: Để đưa ra kết luận hợp lí, dữ liệu thu thập được phải đảm bảo '
            'tính đại diện cho toàn bộ đối tượng đang được quan tâm.',
  'formulas': [{'category': 'Phân loại và kiểm tra dữ liệu',
                'items': [{'name': 'Sơ đồ phân loại dữ liệu',
                           'formula': '$\\text{Dữ liệu} \\begin{cases} \\text{Số liệu (là số)} \\\\ '
                                      '\\text{Không là số} \\; (\\text{Có thể sắp thứ tự} \\; / \\; '
                                      '\\text{Không thể sắp thứ tự}) \\end{cases}$'},
                          {'name': 'Tỉ lệ phần trăm của một nhóm',
                           'formula': '$p\\% = \\dfrac{\\text{Số lượng phần tử của nhóm}}{\\text{Tổng số '
                                      'phần tử khảo sát}} \\cdot 100\\%$'}]}],
  'example': 'Khảo sát môn thể thao yêu thích của $40$ học sinh lớp 7A thu được: Bóng đá ($18$ em), Cầu lông '
             '($12$ em), Bơi lội ($10$ em). Dữ liệu tên môn thể thao thuộc loại nào và tỉ lệ học sinh thích '
             'Bóng đá là bao nhiêu?',
  'example_answer': '- Tên các môn thể thao (Bóng đá, Cầu lông, Bơi lội) là dữ liệu không là số và không thể '
                    'sắp thứ tự.\n'
                    '- Tỉ lệ học sinh thích Bóng đá là $\\dfrac{18}{40} \\cdot 100\\% = 45\\%$.',
  'real_life': 'Thực hiện khảo sát nhu cầu đọc sách của học sinh toàn trường để thư viện bổ sung đầu sách '
               'phù hợp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dữ liệu nào sau đây là số liệu (dữ liệu định lượng)?',
            'options': ['Chiều cao (tính bằng $\\text{cm}$) của các học sinh trong tổ',
                        'Tên các tỉnh thành của Việt Nam',
                        'Màu sắc yêu thích của các bạn trong lớp',
                        'Xếp loại hạnh kiểm: Tốt, Khá, Đạt'],
            'answer': 0,
            'solution': 'Chiều cao biểu diễn bằng các con số đo lường nên là dữ liệu số (số liệu).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Dữ liệu về mức độ hài lòng của khách hàng gồm: 'Rất hài lòng; Hài lòng; Bình thường; Không "
                 "hài lòng' thuộc loại dữ liệu nào?",
            'options': ['Dữ liệu là số (số liệu)',
                        'Dữ liệu không là số, có thể sắp thứ tự',
                        'Dữ liệu không là số, không thể sắp thứ tự',
                        'Dữ liệu không hợp lí'],
            'answer': 1,
            'solution': 'Các mức độ hài lòng là chữ nhưng sắp xếp được theo bậc từ cao xuống thấp nên là dữ '
                        'liệu không là số, có thể sắp thứ tự.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 17: Thu thập và phân loại dữ liệu**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Sơ đồ phân loại dữ liệu**?',
            'options': ['$p\\% = \\dfrac{\\text{Số lượng phần tử của nhóm}}{\\text{Tổng số phần tử khảo '
                        'sát}} \\cdot 100\\%$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\text{Dữ liệu} \\begin{cases} \\text{Số liệu (là số)} \\\\ \\text{Không là số} '
                        '\\; (\\text{Có thể sắp thứ tự} \\; / \\; \\text{Không thể sắp thứ tự}) '
                        '\\end{cases}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 17: Thu thập và phân loại dữ liệu, **Sơ đồ '
                        'phân loại dữ liệu** được xác định bởi: $\\text{Dữ liệu} \\begin{cases} \\text{Số '
                        'liệu (là số)} \\\\ \\text{Không là số} \\; (\\text{Có thể sắp thứ tự} \\; / \\; '
                        '\\text{Không thể sắp thứ tự}) \\end{cases}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Thu thập và phân loại dữ liệu**, nội dung/biểu thức $p\\% = '
                 '\\dfrac{\\text{Số lượng phần tử của nhóm}}{\\text{Tổng số phần tử khảo sát}} \\cdot '
                 '100\\%$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Sơ đồ phân loại dữ liệu',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp',
                        'Tỉ lệ phần trăm của một nhóm'],
            'answer': 3,
            'solution': 'Trong Bài 17: Thu thập và phân loại dữ liệu, biểu thức/quy tắc $p\\% = '
                        '\\dfrac{\\text{Số lượng phần tử của nhóm}}{\\text{Tổng số phần tử khảo sát}} \\cdot '
                        '100\\%$ chính là nội dung của **Tỉ lệ phần trăm của một nhóm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để khảo sát thời gian tự học ở nhà của học sinh toàn trường THCS, cách chọn mẫu nào sau '
                 'đây đảm bảo tính đại diện tốt nhất?',
            'options': ['Chọn ngẫu nhiên mỗi lớp ở cả 4 khối 6, 7, 8, 9 một số học sinh',
                        'Chỉ hỏi các bạn trong đội tuyển học sinh giỏi Toán khối 9',
                        'Chỉ hỏi các bạn nam trong câu lạc bộ bóng đá',
                        'Chỉ hỏi 5 bạn ngồi bàn đầu của lớp 7A'],
            'answer': 0,
            'solution': 'Chọn ngẫu nhiên học sinh ở tất cả các khối lớp giúp mẫu khảo sát có tính đại diện '
                        'cho toàn trường.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Thu thập và phân loại dữ liệu** (Chương V: Thu thập và biểu diễn dữ '
                 'liệu), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Thực hiện và lí giải được việc thu thập, phân loại dữ liệu theo các tiêu chí cho '
                        'trước.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 17: Thu thập và phân loại dữ liệu: Thực hiện và lí '
                        'giải được việc thu thập, phân loại dữ liệu theo các tiêu chí cho trước.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về thu thập và phân loại dữ liệu:',
            'statements': ['Số lượng sách mượn thư viện mỗi tuần ($15; 20; 18; 25$) là dữ liệu số (số liệu).',
                           'Danh sách các loại trái cây (Cam, Xoài, Ổi, Nhãn) là dữ liệu không là số, không '
                           'thể sắp thứ tự.',
                           'Trong bảng thống kê tỉ lệ phần trăm các nhóm của cùng một tổng thể, tổng các tỉ '
                           'lệ có thể vượt quá $100\\%$ rất nhiều.',
                           'Khi thống kê sĩ số các lớp 7 (khoảng 35 đến 45 học sinh), một lớp ghi sĩ số là '
                           '$-40$ học sinh là dữ liệu không hợp lí.'],
            'answer': [True, True, False, True],
            'solution': 'a), b) Đúng. c) Sai vì tổng tỉ lệ phần trăm các phần của một tổng thể phải bằng '
                        '$100\\%$. d) Đúng vì sĩ số học sinh phải là số nguyên dương.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 17: Thu thập và phân '
                 'loại dữ liệu**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện và lí giải được việc thu '
                           'thập, phân loại dữ liệu theo các tiêu chí cho trước.',
                           'Quy tắc/công thức **Sơ đồ phân loại dữ liệu** trong bài được xác định bởi: '
                           '$\\text{Dữ liệu} \\begin{cases} \\text{Số liệu (là số)} \\\\ \\text{Không là số} '
                           '\\; (\\text{Có thể sắp thứ tự} \\; / \\; \\text{Không thể sắp thứ tự}) '
                           '\\end{cases}$.',
                           'Trong mọi trường hợp, **Sơ đồ phân loại dữ liệu** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 17: Thu thập và phân loại dữ liệu.',
                           'Với bài toán minh họa: “Khảo sát môn thể thao yêu thích của $40$ học sinh lớp 7A '
                           'thu được: Bóng đá ($18$ em), Cầu lông ($12$ em), Bơi lội ($10$ em). Dữ liệu tên '
                           'môn...”, lời giải đúng là: - Tên các môn thể thao (Bóng đá, Cầu lông, Bơi lội) '
                           'là dữ liệu không là số và không thể sắp thứ tự. - Tỉ lệ học sinh thích Bóng đá '
                           'là $\\dfrac{18}{40} \\cdot 100\\% = 45\\%$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Thu thập và phân loại dữ liệu. b) '
                        '**Đúng** theo công thức trọng tâm **Sơ đồ phân loại dữ liệu** ($\\text{Dữ liệu} '
                        '\\begin{cases} \\text{Số liệu (là số)} \\\\ \\text{Không là số} \\; (\\text{Có thể '
                        'sắp thứ tự} \\; / \\; \\text{Không thể sắp thứ tự}) \\end{cases}$). c) **Sai** vì '
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Sơ đồ phân loại dữ liệu**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 17: Thu thập và phân loại dữ liệu** để giải quyết tình huống sau: '
                 'Khảo sát môn thể thao yêu thích của $40$ học sinh lớp 7A thu được: Bóng đá ($18$ em), Cầu '
                 'lông ($12$ em), Bơi lội ($10$ em). Dữ liệu tên môn thể thao thuộc loại nào và tỉ lệ học '
                 'sinh thích Bóng đá là bao nhiêu? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        '- Tên các môn thể thao (Bóng đá, Cầu lông, Bơi lội) là dữ liệu không là số và không '
                        'thể sắp thứ tự. - Tỉ lệ học sinh thích Bóng đá là $\\dfrac{18}{40} \\cdot 100\\% = '
                        '45\\%$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Thu thập và phân loại dữ liệu: - Tên các môn thể '
                        'thao (Bóng đá, Cầu lông, Bơi lội) là dữ liệu không là số và không thể sắp thứ tự.\n'
                        '- Tỉ lệ học sinh thích Bóng đá là $\\dfrac{18}{40} \\cdot 100\\% = 45\\%$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong đợt khảo sát $50$ học sinh lớp 7 về phương tiện đến trường, có $20$ bạn đi xe đạp, '
                 '$15$ bạn được bố mẹ chở bằng xe máy, còn lại là đi bộ. Hỏi có bao nhiêu phần trăm học sinh '
                 'đi bộ?',
            'answer': ['30'],
            'unit': None,
            'solution': 'Số học sinh đi bộ là $50 - 20 - 15 = 15$ (bạn). Tỉ lệ phần trăm học sinh đi bộ là '
                        '$\\dfrac{15}{50} \\cdot 100\\% = 30\\%$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch05-thu-thap-bieu-dien-du-lieu',
  'context_title': 'Chương V: Thu thập và biểu diễn dữ liệu',
  'context': 'Chương V · SGK Toán 7: Thu thập, phân loại dữ liệu và đọc, phân tích biểu đồ hình quạt tròn, '
             'biểu đồ đoạn thẳng.',
  'title': 'Bài 18: Biểu đồ hình quạt tròn',
  'icon': '🥧',
  'description': 'Đọc, mô tả và phân tích dữ liệu được biểu diễn trên biểu đồ hình quạt tròn.',
  'requirements': ['Đọc và mô tả thành thạo dữ liệu từ biểu đồ hình quạt tròn.',
                   'Biểu diễn được dữ liệu vào biểu đồ hình quạt tròn có sẵn theo tỉ lệ phần trăm.',
                   'Nhận biết và giải quyết được các bài toán phân tích số liệu dựa trên biểu đồ hình quạt '
                   'tròn.'],
  'definition': 'Biểu đồ hình quạt tròn dùng để so sánh các phần trong toàn bộ dữ liệu. Trong biểu đồ hình '
                'quạt tròn, cả hình tròn biểu diễn toàn bộ dữ liệu ứng với $100\\%$, còn mỗi hình quạt biểu '
                'diễn tỉ lệ của một phần so với toàn bộ dữ liệu.',
  'theory': '1. Cấu tạo biểu đồ hình quạt tròn: Gồm tiêu đề biểu đồ, hình tròn được chia thành các hình quạt '
            'kèm theo tỉ lệ phần trăm và phần chú giải.\n'
            '2. Liên hệ giữa tỉ lệ phần trăm và số liệu thực tế:\n'
            '- Tổng các tỉ lệ phần trăm trên biểu đồ hình quạt tròn luôn bằng $100\\%$.\n'
            '- Giá trị của thành phần ứng với $p\\%$ trong tổng số $N$ phần tử là $n = N \\cdot '
            '\\dfrac{p}{100}$.\n'
            '- Góc ở tâm của hình quạt biểu diễn $p\\%$ là $\\alpha = 360^\\circ \\cdot \\dfrac{p}{100}$.',
  'formulas': [{'category': 'Công thức tính trên biểu đồ hình quạt tròn',
                'items': [{'name': 'Tổng tỉ lệ phần trăm',
                           'formula': '$p_1\\% + p_2\\% + \\cdots + p_k\\% = 100\\%$'},
                          {'name': 'Số lượng của thành phần $p\\%$',
                           'formula': '$n = N \\cdot \\dfrac{p}{100}$ (với $N$ là tổng số lượng)'},
                          {'name': 'Số đo góc ở tâm của hình quạt',
                           'formula': '$\\alpha = 360^\\circ \\cdot \\dfrac{p}{100}$'}]}],
  'example': 'Biểu đồ hình quạt tròn thống kê xếp loại học tập của $200$ học sinh khối 7 gồm: Tốt ($25\\%$), '
             'Khá ($50\\%$), Đạt ($20\\%$) và Chưa đạt ($5\\%$). Tính số học sinh xếp loại Tốt và loại Khá.',
  'example_answer': '- Số học sinh xếp loại Tốt là: $200 \\cdot \\dfrac{25}{100} = 50$ (học sinh).\n'
                    '- Số học sinh xếp loại Khá là: $200 \\cdot \\dfrac{50}{100} = 100$ (học sinh).',
  'real_life': 'Phân tích cơ cấu chi tiêu hàng tháng của gia đình (tiền ăn, tiền điện nước, tiết kiệm, giáo '
               'dục) trên ứng dụng quản lí tài chính.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong biểu đồ hình quạt tròn, toàn bộ hình tròn biểu diễn tổng tỉ lệ phần trăm là:',
            'options': ['$50\\%$', '$100\\%$', '$360\\%$', '$180\\%$'],
            'answer': 1,
            'solution': 'Toàn bộ hình tròn biểu diễn $100\\%$ tổng dữ liệu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình quạt biểu diễn tỉ lệ $25\\%$ chiếm một phần mấy của hình tròn?',
            'options': ['$\\dfrac{1}{2}$ hình tròn',
                        '$\\dfrac{1}{5}$ hình tròn',
                        '$\\dfrac{1}{4}$ hình tròn',
                        '$\\dfrac{1}{3}$ hình tròn'],
            'answer': 2,
            'solution': 'Ta có $25\\% = \\dfrac{25}{100} = \\dfrac{1}{4}$ hình tròn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 18: Biểu đồ hình quạt tròn**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Tổng tỉ lệ phần trăm**?',
            'options': ['$n = N \\cdot \\dfrac{p}{100}$ (với $N$ là tổng số lượng)',
                        '$\\alpha = 360^\\circ \\cdot \\dfrac{p}{100}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$p_1\\% + p_2\\% + \\cdots + p_k\\% = 100\\%$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 18: Biểu đồ hình quạt tròn, **Tổng tỉ lệ phần '
                        'trăm** được xác định bởi: $p_1\\% + p_2\\% + \\cdots + p_k\\% = 100\\%$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Biểu đồ hình quạt tròn**, nội dung/biểu thức $n = N \\cdot '
                 '\\dfrac{p}{100}$ (với $N$ là tổng số lượng) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số lượng của thành phần $p\\%$',
                        'Tổng tỉ lệ phần trăm',
                        'Số đo góc ở tâm của hình quạt',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Trong Bài 18: Biểu đồ hình quạt tròn, biểu thức/quy tắc $n = N \\cdot '
                        '\\dfrac{p}{100}$ (với $N$ là tổng số lượng) chính là nội dung của **Số lượng của '
                        'thành phần $p\\%$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một lớp có $40$ học sinh, trên biểu đồ hình quạt tròn tỉ lệ học sinh tham gia câu lạc bộ '
                 'Mỹ thuật là $15\\%$. Số học sinh tham gia câu lạc bộ Mỹ thuật là:',
            'options': ['$15$ học sinh', '$6$ học sinh', '$8$ học sinh', '$10$ học sinh'],
            'answer': 1,
            'solution': 'Số học sinh tham gia là $40 \\cdot 15\\% = 40 \\cdot \\dfrac{15}{100} = 6$ (học '
                        'sinh).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Biểu đồ hình quạt tròn** (Chương V: Thu thập và biểu diễn dữ liệu), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Đọc và mô tả thành thạo dữ liệu từ biểu đồ hình quạt tròn.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 18: Biểu đồ hình quạt tròn: Đọc và mô tả thành thạo dữ '
                        'liệu từ biểu đồ hình quạt tròn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Biểu đồ hình quạt tròn biểu diễn cơ cấu doanh thu $500$ triệu đồng của một cửa hàng gồm 3 '
                 'mặt hàng: Quần áo ($50\\%$), Giày dép ($30\\%$) và Phụ kiện (còn lại). Xét các khẳng định '
                 'sau:',
            'statements': ['Tỉ lệ doanh thu của mặt hàng Phụ kiện là $20\\%$.',
                           'Hình quạt biểu diễn doanh thu Quần áo là một nửa hình tròn.',
                           'Doanh thu từ Giày dép là $150$ triệu đồng.',
                           'Doanh thu từ Quần áo nhiều hơn Phụ kiện là $100$ triệu đồng.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $100\\% - 50\\% - 30\\% = 20\\%$. b) Đúng vì $50\\% = \\dfrac{1}{2}$ '
                        'hình tròn. c) Đúng vì $500 \\cdot 30\\% = 150$ triệu đồng. d) Sai vì Quần áo hơn '
                        'Phụ kiện là $500 \\cdot (50\\% - 20\\%) = 150$ triệu đồng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 18: Biểu đồ hình quạt '
                 'tròn**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Đọc và mô tả thành thạo dữ liệu từ '
                           'biểu đồ hình quạt tròn.',
                           'Quy tắc/công thức **Tổng tỉ lệ phần trăm** trong bài được xác định bởi: $p_1\\% '
                           '+ p_2\\% + \\cdots + p_k\\% = 100\\%$.',
                           'Trong mọi trường hợp, **Tổng tỉ lệ phần trăm** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 18: Biểu đồ hình quạt tròn.',
                           'Với bài toán minh họa: “Biểu đồ hình quạt tròn thống kê xếp loại học tập của '
                           '$200$ học sinh khối 7 gồm: Tốt ($25\\%$), Khá ($50\\%$), Đạt ($20\\%$) và Chưa '
                           'đạt ($5\\%$)...”, lời giải đúng là: - Số học sinh xếp loại Tốt là: $200 \\cdot '
                           '\\dfrac{25}{100} = 50$ (học sinh). - Số học sinh xếp loại Khá là: $200 \\cdot '
                           '\\dfrac{50}{100} = 100$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Biểu đồ hình quạt tròn. b) **Đúng** '
                        'theo công thức trọng tâm **Tổng tỉ lệ phần trăm** ($p_1\\% + p_2\\% + \\cdots + '
                        'p_k\\% = 100\\%$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Tổng tỉ lệ phần trăm**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 18: Biểu đồ hình quạt tròn** để giải quyết tình huống sau: Biểu '
                 'đồ hình quạt tròn thống kê xếp loại học tập của $200$ học sinh khối 7 gồm: Tốt ($25\\%$), '
                 'Khá ($50\\%$), Đạt ($20\\%$) và Chưa đạt ($5\\%$). Tính số học sinh xếp loại Tốt và loại '
                 'Khá. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        '- Số học sinh xếp loại Tốt là: $200 \\cdot \\dfrac{25}{100} = 50$ (học sinh). - Số '
                        'học sinh xếp loại Khá là: $200 \\cdot \\dfrac{50}{100} = 100$ (học sinh).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Biểu đồ hình quạt tròn: - Số học sinh xếp loại Tốt '
                        'là: $200 \\cdot \\dfrac{25}{100} = 50$ (học sinh).\n'
                        '- Số học sinh xếp loại Khá là: $200 \\cdot \\dfrac{50}{100} = 100$ (học sinh).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một biểu đồ hình quạt tròn biểu diễn kết quả khảo sát $300$ học sinh, hình quạt biểu '
                 'diễn nhóm học sinh thích đọc sách truyện chiếm $40\\%$. Hỏi có bao nhiêu học sinh thích '
                 'đọc sách truyện?',
            'answer': ['120'],
            'unit': None,
            'solution': 'Số học sinh thích đọc sách truyện là $300 \\cdot \\dfrac{40}{100} = 120$ (học '
                        'sinh).',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch05-thu-thap-bieu-dien-du-lieu',
  'context_title': 'Chương V: Thu thập và biểu diễn dữ liệu',
  'context': 'Chương V · SGK Toán 7: Thu thập, phân loại dữ liệu và đọc, phân tích biểu đồ hình quạt tròn, '
             'biểu đồ đoạn thẳng.',
  'title': 'Bài 19: Biểu đồ đoạn thẳng',
  'icon': '📈',
  'description': 'Nhận biết, đọc, vẽ và phân tích xu thế thay đổi của dữ liệu qua thời gian bằng biểu đồ '
                 'đoạn thẳng.',
  'requirements': ['Đọc và mô tả được dữ liệu từ biểu đồ đoạn thẳng.',
                   'Vẽ được biểu đồ đoạn thẳng biểu diễn dữ liệu theo thời gian.',
                   'Phân tích được xu thế tăng, giảm của số liệu dựa vào biểu đồ đoạn thẳng.'],
  'definition': 'Biểu đồ đoạn thẳng thường được dùng để biểu diễn sự thay đổi của một đại lượng theo thời '
                'gian. Nó gồm trục ngang biểu diễn thời gian, trục đứng biểu diễn đại lượng đang quan tâm, '
                'và các đoạn thẳng nối các điểm dữ liệu liên tiếp.',
  'theory': '1. Các thành phần của biểu đồ đoạn thẳng: Tiêu đề biểu đồ, trục ngang (thời gian), trục đứng '
            '(giá trị số liệu), các điểm biểu diễn số liệu và các đoạn thẳng nối các điểm liên tiếp.\n'
            '2. Đọc và phân tích biểu đồ đoạn thẳng: Nhìn vào độ dốc lên hay dốc xuống của các đoạn thẳng '
            'nối các điểm liên tiếp, ta biết đại lượng tăng hay giảm trong từng khoảng thời gian.',
  'formulas': [{'category': 'Phân tích số liệu trên biểu đồ đoạn thẳng',
                'items': [{'name': 'Độ tăng (hoặc giảm) giữa hai mốc thời gian',
                           'formula': '$\\Delta y = y_2 - y_1$'},
                          {'name': 'Tỉ lệ phần trăm tăng trưởng',
                           'formula': '$r\\% = \\dfrac{y_2 - y_1}{y_1} \\cdot 100\\%$'}]}],
  'example': 'Số lượng máy tính bán được của một cửa hàng từ tháng 1 đến tháng 4 lần lượt là: $40; 50; 45; '
             '65$ (chiếc). Hỏi tháng nào bán được nhiều nhất và từ tháng 3 sang tháng 4 số lượng tăng bao '
             'nhiêu chiếc?',
  'example_answer': '- Tháng 4 bán được nhiều nhất với $65$ chiếc.\n'
                    '- Từ tháng 3 sang tháng 4, số lượng máy tính bán được tăng thêm: $65 - 45 = 20$ '
                    '(chiếc).',
  'real_life': 'Theo dõi biểu đồ biến động nhiệt độ trong ngày, lượng mưa hàng tháng hoặc doanh số bán hàng '
               'qua các năm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong biểu đồ đoạn thẳng biểu diễn sự thay đổi của một đại lượng theo thời gian, trục '
                 'ngang thường biểu diễn đại lượng nào?',
            'options': ['Số lượng phần tử', 'Tỉ lệ phần trăm', 'Thời gian', 'Tên biểu đồ'],
            'answer': 2,
            'solution': 'Trong biểu đồ đoạn thẳng, trục ngang biểu diễn thời gian (giờ, ngày, tháng, năm) và '
                        'trục đứng biểu diễn đại lượng được thống kê.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu đồ nào thích hợp nhất để biểu diễn sự thay đổi nhiệt độ tại Hà Nội qua các khung giờ '
                 'trong một ngày?',
            'options': ['Biểu đồ hình quạt tròn', 'Biểu đồ tranh', 'Sơ đồ đoạn thẳng', 'Biểu đồ đoạn thẳng'],
            'answer': 3,
            'solution': 'Để biểu diễn xu thế thay đổi của một đại lượng theo thời gian, ta dùng biểu đồ đoạn '
                        'thẳng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 19: Biểu đồ đoạn thẳng**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Độ tăng (hoặc giảm) giữa hai mốc thời gian**?',
            'options': ['$\\Delta y = y_2 - y_1$',
                        '$r\\% = \\dfrac{y_2 - y_1}{y_1} \\cdot 100\\%$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 19: Biểu đồ đoạn thẳng, **Độ tăng (hoặc giảm) '
                        'giữa hai mốc thời gian** được xác định bởi: $\\Delta y = y_2 - y_1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Biểu đồ đoạn thẳng**, nội dung/biểu thức $r\\% = \\dfrac{y_2 - y_1}{y_1} '
                 '\\cdot 100\\%$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Độ tăng (hoặc giảm) giữa hai mốc thời gian',
                        'Tỉ lệ phần trăm tăng trưởng',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp'],
            'answer': 1,
            'solution': 'Trong Bài 19: Biểu đồ đoạn thẳng, biểu thức/quy tắc $r\\% = \\dfrac{y_2 - y_1}{y_1} '
                        '\\cdot 100\\%$ chính là nội dung của **Tỉ lệ phần trăm tăng trưởng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nhiệt độ đo được lúc $6$ giờ là $22^\\circ\\text{C}$, lúc $9$ giờ là $26^\\circ\\text{C}$, '
                 'lúc $12$ giờ là $31^\\circ\\text{C}$. Từ $6$ giờ đến $12$ giờ, nhiệt độ đã tăng thêm:',
            'options': ['$5^\\circ\\text{C}$',
                        '$4^\\circ\\text{C}$',
                        '$9^\\circ\\text{C}$',
                        '$26^\\circ\\text{C}$'],
            'answer': 2,
            'solution': 'Từ $6$ giờ đến $12$ giờ, nhiệt độ tăng thêm $31^\\circ\\text{C} - '
                        '22^\\circ\\text{C} = 9^\\circ\\text{C}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Biểu đồ đoạn thẳng** (Chương V: Thu thập và biểu diễn dữ liệu), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Đọc và mô tả được dữ liệu từ biểu đồ đoạn thẳng.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 19: Biểu đồ đoạn thẳng: Đọc và mô tả được dữ liệu từ '
                        'biểu đồ đoạn thẳng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Biểu đồ đoạn thẳng ghi lại số cây trồng được của khối 7 từ năm $2021$ đến năm $2024$ lần '
                 'lượt là: $120; 150; 140; 180$ (cây). Xét các khẳng định sau:',
            'statements': ['Năm $2024$ khối 7 trồng được nhiều cây nhất với $180$ cây.',
                           'Từ năm $2021$ đến năm $2022$, số cây trồng được tăng $25\\%$.',
                           'Giai đoạn từ năm $2022$ đến năm $2023$, đoạn thẳng trên biểu đồ đi lên.',
                           'Tổng số cây trồng được trong cả 4 năm là $590$ cây.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $\\dfrac{150 - 120}{120} \\cdot 100\\% = 25\\%$. c) Sai vì từ '
                        '$150$ giảm xuống $140$ nên đoạn thẳng đi xuống. d) Đúng vì $120 + 150 + 140 + 180 = '
                        '590$ (cây).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 19: Biểu đồ đoạn '
                 'thẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Đọc và mô tả được dữ liệu từ biểu '
                           'đồ đoạn thẳng.',
                           'Quy tắc/công thức **Độ tăng (hoặc giảm) giữa hai mốc thời gian** trong bài được '
                           'xác định bởi: $\\Delta y = y_2 - y_1$.',
                           'Trong mọi trường hợp, **Độ tăng (hoặc giảm) giữa hai mốc thời gian** luôn được '
                           'tính bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b '
                           '\\in \\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà '
                           'không cần điều kiện của Bài 19: Biểu đồ đoạn thẳng.',
                           'Với bài toán minh họa: “Số lượng máy tính bán được của một cửa hàng từ tháng 1 '
                           'đến tháng 4 lần lượt là: $40; 50; 45; 65$ (chiếc). Hỏi tháng nào bán được nhiều '
                           'nhất...”, lời giải đúng là: - Tháng 4 bán được nhiều nhất với $65$ chiếc. - Từ '
                           'tháng 3 sang tháng 4, số lượng máy tính bán được tăng thêm: $65 - 45 = 20$ '
                           '(chiếc).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Biểu đồ đoạn thẳng. b) **Đúng** theo '
                        'công thức trọng tâm **Độ tăng (hoặc giảm) giữa hai mốc thời gian** ($\\Delta y = '
                        'y_2 - y_1$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; '
                        'a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Độ tăng (hoặc giảm) giữa hai mốc thời gian**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 19: Biểu đồ đoạn thẳng** để giải quyết tình huống sau: Số lượng '
                 'máy tính bán được của một cửa hàng từ tháng 1 đến tháng 4 lần lượt là: $40; 50; 45; 65$ '
                 '(chiếc). Hỏi tháng nào bán được nhiều nhất và từ tháng 3 sang tháng 4 số lượng tăng bao '
                 'nhiêu chiếc? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['- Tháng 4 bán được nhiều nhất với $65$ chiếc. - Từ tháng 3 sang tháng 4, số lượng '
                        'máy tính bán được tăng thêm: $65 - 45 = 20$ (chiếc).',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Biểu đồ đoạn thẳng: - Tháng 4 bán được nhiều nhất '
                        'với $65$ chiếc.\n'
                        '- Từ tháng 3 sang tháng 4, số lượng máy tính bán được tăng thêm: $65 - 45 = 20$ '
                        '(chiếc).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Doanh thu của một tiệm bánh trong 4 quý của năm lần lượt là $80; 100; 95; 125$ (triệu '
                 'đồng). Tính doanh thu trung bình mỗi quý trong năm của tiệm bánh đó (đơn vị: triệu đồng).',
            'answer': ['100'],
            'unit': None,
            'solution': 'Doanh thu trung bình mỗi quý là $\\dfrac{80 + 100 + 95 + 125}{4} = \\dfrac{400}{4} '
                        '= 100$ (triệu đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch06-ti-le-thuc',
  'context_title': 'Chương VI: Tỉ lệ thức và đại lượng tỉ lệ',
  'context': 'Chương VI · SGK Toán 7: Tỉ lệ thức, tính chất dãy tỉ số bằng nhau, đại lượng tỉ lệ thuận và '
             'đại lượng tỉ lệ nghịch.',
  'title': 'Bài 20: Tỉ lệ thức',
  'icon': '⚖️',
  'description': 'Định nghĩa tỉ lệ thức và các tính chất cơ bản của tỉ lệ thức.',
  'requirements': ['Nhận biết được tỉ lệ thức và các số hạng của tỉ lệ thức.',
                   'Nhận biết và vận dụng được tính chất cơ bản của tỉ lệ thức để tìm số hạng chưa biết và '
                   'lập các tỉ lệ thức mới.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Định nghĩa tỉ lệ thức** ($\\dfrac{a}{b} = '
                   '\\dfrac{c}{d} \\quad (b, d \\neq 0)$) vào giải bài tập.'],
  'definition': 'Tỉ lệ thức là đẳng thức của hai tỉ số $\\dfrac{a}{b} = \\dfrac{c}{d}$ (hoặc viết $a : b = c '
                ': d$), trong đó $a, d$ gọi là các ngoại tỉ và $b, c$ gọi là các trung tỉ.',
  'theory': '1. Tính chất 1 (Tính chất cơ bản của tỉ lệ thức): Nếu $\\dfrac{a}{b} = \\dfrac{c}{d}$ thì $a '
            '\\cdot d = b \\cdot c$.\n'
            '2. Tính chất 2 (Suy ra các tỉ lệ thức từ tích): Nếu $a \\cdot d = b \\cdot c$ và $a, b, c, d '
            '\\neq 0$ thì ta có các tỉ lệ thức:\n'
            '$\\dfrac{a}{b} = \\dfrac{c}{d}; \\quad \\dfrac{a}{c} = \\dfrac{b}{d}; \\quad \\dfrac{d}{b} = '
            '\\dfrac{c}{a}; \\quad \\dfrac{d}{c} = \\dfrac{b}{a}$.',
  'formulas': [{'category': 'Định nghĩa và tính chất tỉ lệ thức',
                'items': [{'name': 'Định nghĩa tỉ lệ thức',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{c}{d} \\quad (b, d \\neq 0)$'},
                          {'name': 'Tính chất cơ bản (nhân chéo)',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{c}{d} \\Rightarrow a \\cdot d = b \\cdot c$'},
                          {'name': 'Tìm một số hạng trong tỉ lệ thức',
                           'formula': '$x = \\dfrac{b \\cdot c}{d}$ khi $\\dfrac{x}{b} = \\dfrac{c}{d}$'}]}],
  'example': 'Tìm $x$ trong tỉ lệ thức $\\dfrac{x}{6} = \\dfrac{-5}{3}$.',
  'example_answer': 'Áp dụng tính chất cơ bản của tỉ lệ thức, ta có:\n'
                    '$3 \\cdot x = 6 \\cdot (-5) \\Rightarrow 3x = -30 \\Rightarrow x = \\dfrac{-30}{3} = '
                    '-10$.',
  'real_life': 'Tính chiều dài thực tế của một con đường từ bản đồ dựa vào tỉ lệ bản đồ hoặc pha chế nguyên '
               'liệu nấu ăn theo công thức chuẩn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu $\\dfrac{a}{b} = \\dfrac{c}{d}$ (với $b, d \\neq 0$) thì đẳng thức nào sau đây đúng?',
            'options': ['$a \\cdot b = c \\cdot d$',
                        '$a \\cdot c = b \\cdot d$',
                        '$a + d = b + c$',
                        '$a \\cdot d = b \\cdot c$'],
            'answer': 3,
            'solution': 'Theo tính chất cơ bản của tỉ lệ thức: $\\dfrac{a}{b} = \\dfrac{c}{d} \\Rightarrow a '
                        '\\cdot d = b \\cdot c$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cặp tỉ số nào sau đây lập thành một tỉ lệ thức?',
            'options': ['$\\dfrac{2}{5}$ và $\\dfrac{6}{15}$',
                        '$\\dfrac{3}{4}$ và $\\dfrac{6}{9}$',
                        '$\\dfrac{1}{2}$ và $\\dfrac{2}{3}$',
                        '$\\dfrac{4}{5}$ và $\\dfrac{5}{4}$'],
            'answer': 0,
            'solution': 'Vì $2 \\cdot 15 = 5 \\cdot 6 = 30$ nên $\\dfrac{2}{5} = \\dfrac{6}{15}$ lập thành '
                        'một tỉ lệ thức.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 20: Tỉ lệ thức**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Định nghĩa tỉ lệ thức**?',
            'options': ['$\\dfrac{a}{b} = \\dfrac{c}{d} \\Rightarrow a \\cdot d = b \\cdot c$',
                        '$\\dfrac{a}{b} = \\dfrac{c}{d} \\quad (b, d \\neq 0)$',
                        '$x = \\dfrac{b \\cdot c}{d}$ khi $\\dfrac{x}{b} = \\dfrac{c}{d}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 20: Tỉ lệ thức, **Định nghĩa tỉ lệ thức** '
                        'được xác định bởi: $\\dfrac{a}{b} = \\dfrac{c}{d} \\quad (b, d \\neq 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Tỉ lệ thức**, nội dung/biểu thức $\\dfrac{a}{b} = \\dfrac{c}{d} '
                 '\\Rightarrow a \\cdot d = b \\cdot c$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa tỉ lệ thức',
                        'Tìm một số hạng trong tỉ lệ thức',
                        'Tính chất cơ bản (nhân chéo)',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 20: Tỉ lệ thức, biểu thức/quy tắc $\\dfrac{a}{b} = \\dfrac{c}{d} '
                        '\\Rightarrow a \\cdot d = b \\cdot c$ chính là nội dung của **Tính chất cơ bản '
                        '(nhân chéo)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của $x$ thỏa mãn tỉ lệ thức $\\dfrac{x}{12} = \\dfrac{3}{4}$ là:',
            'options': ['$16$', '$4$', '$8$', '$9$'],
            'answer': 3,
            'solution': 'Ta có $x = \\dfrac{12 \\cdot 3}{4} = 9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Tỉ lệ thức** (Chương VI: Tỉ lệ thức và đại lượng tỉ lệ), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được tỉ lệ thức và các số hạng của tỉ lệ thức.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 20: Tỉ lệ thức: Nhận biết được tỉ lệ thức và các số '
                        'hạng của tỉ lệ thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đẳng thức $2 \\cdot 9 = 3 \\cdot 6$. Xét tính đúng sai của các khẳng định sau:',
            'statements': ['Từ đẳng thức trên ta suy ra được tỉ lệ thức $\\dfrac{2}{3} = \\dfrac{6}{9}$.',
                           'Từ đẳng thức trên ta suy ra được tỉ lệ thức $\\dfrac{2}{6} = \\dfrac{3}{9}$.',
                           'Từ đẳng thức trên ta suy ra được tỉ lệ thức $\\dfrac{2}{9} = \\dfrac{3}{6}$.',
                           'Từ bốn số $2; 3; 6; 9$ ta lập được tất cả $4$ tỉ lệ thức đúng.'],
            'answer': [True, True, False, True],
            'solution': 'a), b), d) Đúng. c) Sai vì $\\dfrac{2}{9} \\neq \\dfrac{3}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 20: Tỉ lệ thức**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được tỉ lệ thức và các '
                           'số hạng của tỉ lệ thức.',
                           'Quy tắc/công thức **Định nghĩa tỉ lệ thức** trong bài được xác định bởi: '
                           '$\\dfrac{a}{b} = \\dfrac{c}{d} \\quad (b, d \\neq 0)$.',
                           'Trong mọi trường hợp, **Định nghĩa tỉ lệ thức** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 20: Tỉ lệ thức.',
                           'Với bài toán minh họa: “Tìm $x$ trong tỉ lệ thức $\\dfrac{x}{6} = '
                           '\\dfrac{-5}{3}$.”, lời giải đúng là: Áp dụng tính chất cơ bản của tỉ lệ thức, ta '
                           'có: $3 \\cdot x = 6 \\cdot (-5) \\Rightarrow 3x = -30 \\Rightarrow x = '
                           '\\dfrac{-30}{3} = -10$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 20: Tỉ lệ thức. b) **Đúng** theo công thức '
                        'trọng tâm **Định nghĩa tỉ lệ thức** ($\\dfrac{a}{b} = \\dfrac{c}{d} \\quad (b, d '
                        '\\neq 0)$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, '
                        'b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Định nghĩa tỉ lệ thức**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 20: Tỉ lệ thức** để giải quyết tình huống sau: Tìm $x$ trong tỉ '
                 'lệ thức $\\dfrac{x}{6} = \\dfrac{-5}{3}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất cơ bản của tỉ lệ thức, ta có: $3 \\cdot x = 6 \\cdot (-5) '
                        '\\Rightarrow 3x = -30 \\Rightarrow x = \\dfrac{-30}{3} = -10$.',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Tỉ lệ thức: Áp dụng tính chất cơ bản của tỉ lệ thức, '
                        'ta có:\n'
                        '$3 \\cdot x = 6 \\cdot (-5) \\Rightarrow 3x = -30 \\Rightarrow x = \\dfrac{-30}{3} '
                        '= -10$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số dương $x$ biết $\\dfrac{x}{4} = \\dfrac{9}{x}$.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Ta có $x^2 = 4 \\cdot 9 = 36$. Vì $x > 0$ nên $x = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch06-ti-le-thuc',
  'context_title': 'Chương VI: Tỉ lệ thức và đại lượng tỉ lệ',
  'context': 'Chương VI · SGK Toán 7: Tỉ lệ thức, tính chất dãy tỉ số bằng nhau, đại lượng tỉ lệ thuận và '
             'đại lượng tỉ lệ nghịch.',
  'title': 'Bài 21: Tính chất của dãy tỉ số bằng nhau',
  'icon': '🔗',
  'description': 'Tính chất của dãy hai hay nhiều tỉ số bằng nhau và ứng dụng giải bài toán chia theo tỉ lệ.',
  'requirements': ['Nhận biết và mô tả được tính chất của dãy tỉ số bằng nhau.',
                   'Vận dụng được tính chất của dãy tỉ số bằng nhau để tìm các số chưa biết và giải quyết '
                   'các bài toán thực tiễn.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Dãy hai tỉ số bằng nhau** ($\\dfrac{a}{b} = '
                   '\\dfrac{c}{d} = \\dfrac{a + c}{b + d} = \\dfrac{a - c}{b - d}$) vào giải bài tập.'],
  'definition': 'Từ dãy tỉ số bằng nhau $\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{e}{f}$, ta suy ra '
                '$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{e}{f} = \\dfrac{a + c + e}{b + d + f} = \\dfrac{a '
                '- c + e}{b - d + f}$ (giả thiết các tỉ số đều có nghĩa).',
  'theory': '1. Tính chất của dãy hai tỉ số bằng nhau: Từ $\\dfrac{a}{b} = \\dfrac{c}{d}$ suy ra '
            '$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{a + c}{b + d} = \\dfrac{a - c}{b - d}$ (với $b + d '
            '\\neq 0, b - d \\neq 0$).\n'
            '2. Chú ý về cách viết tỉ lệ: Khi nói các số $a, b, c$ tỉ lệ với các số $x, y, z$, ta viết '
            '$\\dfrac{a}{x} = \\dfrac{b}{y} = \\dfrac{c}{z}$ hoặc $a : b : c = x : y : z$.',
  'formulas': [{'category': 'Tính chất dãy tỉ số bằng nhau',
                'items': [{'name': 'Dãy hai tỉ số bằng nhau',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{a + c}{b + d} = \\dfrac{a - '
                                      'c}{b - d}$'},
                          {'name': 'Dãy ba tỉ số bằng nhau',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{e}{f} = \\dfrac{a + c + e}{b '
                                      '+ d + f} = \\dfrac{a - c + e}{b - d + f}$'},
                          {'name': 'Kí hiệu ba số tỉ lệ',
                           'formula': '$a : b : c = m : n : p \\Leftrightarrow \\dfrac{a}{m} = \\dfrac{b}{n} '
                                      '= \\dfrac{c}{p}$'}]}],
  'example': 'Tìm hai số $x, y$ biết $\\dfrac{x}{3} = \\dfrac{y}{5}$ và $x + y = 24$.',
  'example_answer': 'Áp dụng tính chất của dãy tỉ số bằng nhau, ta có:\n'
                    '$\\dfrac{x}{3} = \\dfrac{y}{5} = \\dfrac{x + y}{3 + 5} = \\dfrac{24}{8} = 3$.\n'
                    'Suy ra $x = 3 \\cdot 3 = 9$ và $y = 5 \\cdot 3 = 15$.',
  'real_life': 'Chia tiền thưởng hoặc phân bổ số cây trồng cho các lớp tỉ lệ với số học sinh của mỗi lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với giả thiết các tỉ số đều có nghĩa, từ $\\dfrac{x}{a} = \\dfrac{y}{b}$ ta suy ra:',
            'options': ['$\\dfrac{x}{a} = \\dfrac{y}{b} = \\dfrac{x + y}{a + b}$',
                        '$\\dfrac{x}{a} = \\dfrac{y}{b} = \\dfrac{x + y}{a - b}$',
                        '$\\dfrac{x}{a} = \\dfrac{y}{b} = \\dfrac{x \\cdot y}{a \\cdot b}$',
                        '$\\dfrac{x}{a} = \\dfrac{y}{b} = \\dfrac{x - y}{a + b}$'],
            'answer': 0,
            'solution': 'Theo tính chất dãy tỉ số bằng nhau: $\\dfrac{x}{a} = \\dfrac{y}{b} = \\dfrac{x + '
                        'y}{a + b}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi nói ba số $x, y, z$ tỉ lệ với ba số $2; 3; 5$, cách viết nào sau đây là đúng?',
            'options': ['$2x = 3y = 5z$',
                        '$\\dfrac{x}{2} = \\dfrac{y}{3} = \\dfrac{z}{5}$',
                        '$\\dfrac{x}{5} = \\dfrac{y}{3} = \\dfrac{z}{2}$',
                        '$x + 2 = y + 3 = z + 5$'],
            'answer': 1,
            'solution': 'Ba số $x, y, z$ tỉ lệ với $2; 3; 5$ có nghĩa là $\\dfrac{x}{2} = \\dfrac{y}{3} = '
                        '\\dfrac{z}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 21: Tính chất của dãy tỉ số bằng nhau**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Dãy hai tỉ số bằng nhau**?',
            'options': ['$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{e}{f} = \\dfrac{a + c + e}{b + d + f} = '
                        '\\dfrac{a - c + e}{b - d + f}$',
                        '$a : b : c = m : n : p \\Leftrightarrow \\dfrac{a}{m} = \\dfrac{b}{n} = '
                        '\\dfrac{c}{p}$',
                        '$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{a + c}{b + d} = \\dfrac{a - c}{b - d}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 21: Tính chất của dãy tỉ số bằng nhau, **Dãy '
                        'hai tỉ số bằng nhau** được xác định bởi: $\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{a '
                        '+ c}{b + d} = \\dfrac{a - c}{b - d}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Tính chất của dãy tỉ số bằng nhau**, nội dung/biểu thức $\\dfrac{a}{b} = '
                 '\\dfrac{c}{d} = \\dfrac{e}{f} = \\dfrac{a + c + e}{b + d + f} = \\dfrac{a - c + e}{b - d + '
                 'f}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Dãy hai tỉ số bằng nhau',
                        'Kí hiệu ba số tỉ lệ',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Dãy ba tỉ số bằng nhau'],
            'answer': 3,
            'solution': 'Trong Bài 21: Tính chất của dãy tỉ số bằng nhau, biểu thức/quy tắc $\\dfrac{a}{b} = '
                        '\\dfrac{c}{d} = \\dfrac{e}{f} = \\dfrac{a + c + e}{b + d + f} = \\dfrac{a - c + '
                        'e}{b - d + f}$ chính là nội dung của **Dãy ba tỉ số bằng nhau**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\dfrac{x}{4} = \\dfrac{y}{7}$ và $y - x = 12$. Giá trị của $x$ và $y$ lần lượt là:',
            'options': ['$x = 16; y = 28$', '$x = 12; y = 24$', '$x = 4; y = 7$', '$x = 28; y = 16$'],
            'answer': 0,
            'solution': 'Ta có $\\dfrac{x}{4} = \\dfrac{y}{7} = \\dfrac{y - x}{7 - 4} = \\dfrac{12}{3} = 4 '
                        '\\Rightarrow x = 16, y = 28$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Tính chất của dãy tỉ số bằng nhau** (Chương VI: Tỉ lệ thức và đại lượng '
                 'tỉ lệ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Nhận biết và mô tả được tính chất của dãy tỉ số bằng nhau.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 21: Tính chất của dãy tỉ số bằng nhau: Nhận biết và mô '
                        'tả được tính chất của dãy tỉ số bằng nhau.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Ba lớp 7A, 7B, 7C trồng được tổng cộng $120$ cây xanh. Biết số cây trồng được của ba lớp '
                 '$x, y, z$ lần lượt tỉ lệ với $3; 4; 5$. Xét các khẳng định sau:',
            'statements': ['Ta lập được dãy tỉ số bằng nhau $\\dfrac{x}{3} = \\dfrac{y}{4} = \\dfrac{z}{5}$.',
                           'Giá trị chung của dãy tỉ số bằng $\\dfrac{120}{3 + 4 + 5} = 10$.',
                           'Lớp 7A trồng được $30$ cây và lớp 7B trồng được $40$ cây.',
                           'Lớp 7C trồng được nhiều hơn lớp 7A là $10$ cây.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $x = 30, y = 40, z = 50$. d) Sai vì lớp 7C trồng được $50$ cây, '
                        'nhiều hơn lớp 7A là $50 - 30 = 20$ cây.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 21: Tính chất của dãy '
                 'tỉ số bằng nhau**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết và mô tả được tính chất '
                           'của dãy tỉ số bằng nhau.',
                           'Quy tắc/công thức **Dãy hai tỉ số bằng nhau** trong bài được xác định bởi: '
                           '$\\dfrac{a}{b} = \\dfrac{c}{d} = \\dfrac{a + c}{b + d} = \\dfrac{a - c}{b - d}$.',
                           'Trong mọi trường hợp, **Dãy hai tỉ số bằng nhau** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 21: Tính chất của dãy tỉ số bằng nhau.',
                           'Với bài toán minh họa: “Tìm hai số $x, y$ biết $\\dfrac{x}{3} = \\dfrac{y}{5}$ '
                           'và $x + y = 24$.”, lời giải đúng là: Áp dụng tính chất của dãy tỉ số bằng nhau, '
                           'ta có: $\\dfrac{x}{3} = \\dfrac{y}{5} = \\dfrac{x + y}{3 + 5} = \\dfrac{24}{8} = '
                           '3$. Suy ra $x = 3 \\cdot 3 = 9$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 21: Tính chất của dãy tỉ số bằng nhau. b) '
                        '**Đúng** theo công thức trọng tâm **Dãy hai tỉ số bằng nhau** ($\\dfrac{a}{b} = '
                        '\\dfrac{c}{d} = \\dfrac{a + c}{b + d} = \\dfrac{a - c}{b - d}$). c) **Sai** vì '
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Dãy hai tỉ số bằng nhau**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 21: Tính chất của dãy tỉ số bằng nhau** để giải quyết tình huống '
                 'sau: Tìm hai số $x, y$ biết $\\dfrac{x}{3} = \\dfrac{y}{5}$ và $x + y = 24$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Áp dụng tính chất của dãy tỉ số bằng nhau, ta có: $\\dfrac{x}{3} = \\dfrac{y}{5} = '
                        '\\dfrac{x + y}{3 + 5} = \\dfrac{24}{8} = 3$. Suy ra $x = 3 \\cdot 3 = 9$ và $y = 5 '
                        '\\cdot 3 = 15$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Tính chất của dãy tỉ số bằng nhau: Áp dụng tính chất '
                        'của dãy tỉ số bằng nhau, ta có:\n'
                        '$\\dfrac{x}{3} = \\dfrac{y}{5} = \\dfrac{x + y}{3 + 5} = \\dfrac{24}{8} = 3$.\n'
                        'Suy ra $x = 3 \\cdot 3 = 9$ và $y = 5 \\cdot 3 = 15$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chữ nhật có tỉ số giữa chiều rộng và chiều dài là $\\dfrac{2}{3}$ và chu vi bằng '
                 '$50\\text{ m}$. Tính diện tích của hình chữ nhật đó (đơn vị $\\text{m}^2$).',
            'answer': ['150'],
            'unit': None,
            'solution': 'Nửa chu vi là $50 : 2 = 25\\text{ (m)}$. Gọi chiều rộng và chiều dài là $a, b$, ta '
                        'có $\\dfrac{a}{2} = \\dfrac{b}{3} = \\dfrac{a+b}{5} = \\dfrac{25}{5} = 5 '
                        '\\Rightarrow a = 10\\text{ m}, b = 15\\text{ m}$. Diện tích là $10 \\cdot 15 = '
                        '150\\text{ (m}^2\\text{)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch06-ti-le-thuc',
  'context_title': 'Chương VI: Tỉ lệ thức và đại lượng tỉ lệ',
  'context': 'Chương VI · SGK Toán 7: Tỉ lệ thức, tính chất dãy tỉ số bằng nhau, đại lượng tỉ lệ thuận và '
             'đại lượng tỉ lệ nghịch.',
  'title': 'Bài 22: Đại lượng tỉ lệ thuận',
  'icon': '⬆️',
  'description': 'Khái niệm, tính chất của hai đại lượng tỉ lệ thuận và giải các bài toán thực tế về đại '
                 'lượng tỉ lệ thuận.',
  'requirements': ['Nhận biết được hai đại lượng tỉ lệ thuận và hệ số tỉ lệ.',
                   'Mô tả được các tính chất của hai đại lượng tỉ lệ thuận.',
                   'Giải được một số bài toán thực tiễn về đại lượng tỉ lệ thuận.'],
  'definition': 'Nếu đại lượng $y$ liên hệ với đại lượng $x$ theo công thức $y = ax$ (với $a$ là một hằng số '
                'khác $0$) thì ta nói $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $a$.',
  'theory': '1. Hệ số tỉ lệ ngược lại: Nếu $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $a$ ($a \\neq 0$) thì '
            '$x$ cũng tỉ lệ thuận với $y$ theo hệ số tỉ lệ $\\dfrac{1}{a}$.\n'
            '2. Tính chất của hai đại lượng tỉ lệ thuận: Nếu hai đại lượng $y$ và $x$ tỉ lệ thuận với nhau '
            'thì:\n'
            '- Tỉ số hai giá trị tương ứng của chúng luôn không đổi và bằng hệ số tỉ lệ: $\\dfrac{y_1}{x_1} '
            '= \\dfrac{y_2}{x_2} = \\dfrac{y_3}{x_3} = \\cdots = a$.\n'
            '- Tỉ số hai giá trị bất kì của đại lượng này bằng tỉ số hai giá trị tương ứng của đại lượng '
            'kia: $\\dfrac{x_1}{x_2} = \\dfrac{y_1}{y_2}$.',
  'formulas': [{'category': 'Công thức và tính chất đại lượng tỉ lệ thuận',
                'items': [{'name': 'Công thức tỉ lệ thuận',
                           'formula': '$y = ax \\quad (a \\neq 0) \\Rightarrow x = \\dfrac{1}{a}y$'},
                          {'name': 'Tỉ số các giá trị tương ứng',
                           'formula': '$\\dfrac{y_1}{x_1} = \\dfrac{y_2}{x_2} = \\dfrac{y_3}{x_3} = a$'},
                          {'name': 'Quan hệ hai cặp giá trị',
                           'formula': '$\\dfrac{x_1}{x_2} = \\dfrac{y_1}{y_2}$'}]}],
  'example': 'Cho biết $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $a$. Khi $x = 4$ thì $y = 12$. Tìm hệ số tỉ '
             'lệ $a$ và tính giá trị của $y$ khi $x = -5$.',
  'example_answer': 'Vì $y = ax$ nên thay $x = 4, y = 12$ ta được $a = \\dfrac{y}{x} = \\dfrac{12}{4} = 3$.\n'
                    'Vậy $y = 3x$. Khi $x = -5$ thì $y = 3 \\cdot (-5) = -15$.',
  'real_life': 'Quãng đường đi được $s = v \\cdot t$ của một vật chuyển động đều tỉ lệ thuận với thời gian '
               '$t$; số tiền mua hàng tỉ lệ thuận với số lượng sản phẩm cùng loại.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu đại lượng $y$ tỉ lệ thuận với đại lượng $x$ theo hệ số tỉ lệ $a = -3$ thì công thức '
                 'biểu diễn $y$ theo $x$ là:',
            'options': ['$y = \\dfrac{-3}{x}$', '$y = -3x$', '$y = x - 3$', '$y = \\dfrac{-1}{3}x$'],
            'answer': 1,
            'solution': 'Theo định nghĩa, $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $a = -3$ thì $y = -3x$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $k = 5$ thì $x$ tỉ lệ thuận với $y$ theo hệ '
                 'số tỉ lệ nào?',
            'options': ['$5$', '$-5$', '$\\dfrac{1}{5}$', '$\\dfrac{-1}{5}$'],
            'answer': 2,
            'solution': 'Từ $y = 5x$ suy ra $x = \\dfrac{1}{5}y$, nên $x$ tỉ lệ thuận với $y$ theo hệ số tỉ '
                        'lệ $\\dfrac{1}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 22: Đại lượng tỉ lệ thuận**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Công thức tỉ lệ thuận**?',
            'options': ['$\\dfrac{y_1}{x_1} = \\dfrac{y_2}{x_2} = \\dfrac{y_3}{x_3} = a$',
                        '$\\dfrac{x_1}{x_2} = \\dfrac{y_1}{y_2}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$y = ax \\quad (a \\neq 0) \\Rightarrow x = \\dfrac{1}{a}y$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 22: Đại lượng tỉ lệ thuận, **Công thức tỉ lệ '
                        'thuận** được xác định bởi: $y = ax \\quad (a \\neq 0) \\Rightarrow x = '
                        '\\dfrac{1}{a}y$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Đại lượng tỉ lệ thuận**, nội dung/biểu thức $\\dfrac{y_1}{x_1} = '
                 '\\dfrac{y_2}{x_2} = \\dfrac{y_3}{x_3} = a$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tỉ số các giá trị tương ứng',
                        'Công thức tỉ lệ thuận',
                        'Quan hệ hai cặp giá trị',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Trong Bài 22: Đại lượng tỉ lệ thuận, biểu thức/quy tắc $\\dfrac{y_1}{x_1} = '
                        '\\dfrac{y_2}{x_2} = \\dfrac{y_3}{x_3} = a$ chính là nội dung của **Tỉ số các giá '
                        'trị tương ứng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai đại lượng $x$ và $y$ tỉ lệ thuận với nhau và khi $x = 6$ thì $y = 18$. Khi $x = '
                 '10$ thì giá trị của $y$ là:',
            'options': ['$22$', '$30$', '$10,8$', '$60$'],
            'answer': 1,
            'solution': 'Hệ số tỉ lệ $a = \\dfrac{18}{6} = 3$. Khi $x = 10$ thì $y = 3 \\cdot 10 = 30$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Đại lượng tỉ lệ thuận** (Chương VI: Tỉ lệ thức và đại lượng tỉ lệ), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được hai đại lượng tỉ lệ thuận và hệ số tỉ lệ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 22: Đại lượng tỉ lệ thuận: Nhận biết được hai đại '
                        'lượng tỉ lệ thuận và hệ số tỉ lệ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cứ xay $100\\text{ kg}$ thóc thì thu được $65\\text{ kg}$ gạo. Gọi $x\\text{ (kg)}$ là '
                 'khối lượng thóc và $y\\text{ (kg)}$ là khối lượng gạo thu được. Xét các khẳng định sau:',
            'statements': ['Hai đại lượng $x$ và $y$ là hai đại lượng tỉ lệ thuận.',
                           'Hệ số tỉ lệ của $y$ đối với $x$ là $0,65$.',
                           'Nếu xay $200\\text{ kg}$ thóc thì thu được $130\\text{ kg}$ gạo.',
                           'Muốn thu được $650\\text{ kg}$ gạo thì cần xay $800\\text{ kg}$ thóc.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $y = 0,65x$. d) Sai vì để có $650\\text{ kg}$ gạo cần xay $650 : '
                        '0,65 = 1000\\text{ kg}$ thóc.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 22: Đại lượng tỉ lệ '
                 'thuận**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hai đại lượng tỉ lệ '
                           'thuận và hệ số tỉ lệ.',
                           'Quy tắc/công thức **Công thức tỉ lệ thuận** trong bài được xác định bởi: $y = ax '
                           '\\quad (a \\neq 0) \\Rightarrow x = \\dfrac{1}{a}y$.',
                           'Trong mọi trường hợp, **Công thức tỉ lệ thuận** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 22: Đại lượng tỉ lệ thuận.',
                           'Với bài toán minh họa: “Cho biết $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $a$. '
                           'Khi $x = 4$ thì $y = 12$. Tìm hệ số tỉ lệ $a$ và tính giá trị của $y$ khi $x = '
                           '-5$.”, lời giải đúng là: Vì $y = ax$ nên thay $x = 4, y = 12$ ta được $a = '
                           '\\dfrac{y}{x} = \\dfrac{12}{4} = 3$. Vậy $y = 3x$. Khi $x = -5$ thì $y = 3 '
                           '\\cdot (-5) = -15$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 22: Đại lượng tỉ lệ thuận. b) **Đúng** '
                        'theo công thức trọng tâm **Công thức tỉ lệ thuận** ($y = ax \\quad (a \\neq 0) '
                        '\\Rightarrow x = \\dfrac{1}{a}y$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Công thức tỉ lệ thuận**. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 22: Đại lượng tỉ lệ thuận** để giải quyết tình huống sau: Cho '
                 'biết $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $a$. Khi $x = 4$ thì $y = 12$. Tìm hệ số tỉ '
                 'lệ $a$ và tính giá trị của $y$ khi $x = -5$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Vì $y = ax$ nên thay $x = 4, y = 12$ ta được $a = \\dfrac{y}{x} = \\dfrac{12}{4} = '
                        '3$. Vậy $y = 3x$. Khi $x = -5$ thì $y = 3 \\cdot (-5) = -15$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Đại lượng tỉ lệ thuận: Vì $y = ax$ nên thay $x = 4, '
                        'y = 12$ ta được $a = \\dfrac{y}{x} = \\dfrac{12}{4} = 3$.\n'
                        'Vậy $y = 3x$. Khi $x = -5$ thì $y = 3 \\cdot (-5) = -15$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mua $5$ quyển vở cùng loại hết $45$ nghìn đồng. Hỏi mua $8$ quyển vở như thế hết bao nhiêu '
                 'nghìn đồng?',
            'answer': ['72'],
            'unit': None,
            'solution': 'Giá một quyển vở là $45 : 5 = 9$ (nghìn đồng). Mua $8$ quyển vở hết $9 \\cdot 8 = '
                        '72$ (nghìn đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch06-ti-le-thuc',
  'context_title': 'Chương VI: Tỉ lệ thức và đại lượng tỉ lệ',
  'context': 'Chương VI · SGK Toán 7: Tỉ lệ thức, tính chất dãy tỉ số bằng nhau, đại lượng tỉ lệ thuận và '
             'đại lượng tỉ lệ nghịch.',
  'title': 'Bài 23: Đại lượng tỉ lệ nghịch',
  'icon': '🔄',
  'description': 'Khái niệm, tính chất của hai đại lượng tỉ lệ nghịch và giải các bài toán thực tế về đại '
                 'lượng tỉ lệ nghịch.',
  'requirements': ['Nhận biết được hai đại lượng tỉ lệ nghịch và hệ số tỉ lệ.',
                   'Mô tả được các tính chất của hai đại lượng tỉ lệ nghịch.',
                   'Giải được một số bài toán thực tiễn về đại lượng tỉ lệ nghịch (như bài toán năng suất, '
                   'vận tốc - thời gian).'],
  'definition': 'Nếu đại lượng $y$ liên hệ với đại lượng $x$ theo công thức $y = \\dfrac{a}{x}$ hay $x '
                '\\cdot y = a$ (với $a$ là một hằng số khác $0$) thì ta nói $y$ tỉ lệ nghịch với $x$ theo hệ '
                'số tỉ lệ $a$.',
  'theory': '1. Quan hệ đối xứng: Nếu $y$ tỉ lệ nghịch với $x$ theo hệ số tỉ lệ $a$ thì $x$ cũng tỉ lệ '
            'nghịch với $y$ theo chính hệ số tỉ lệ $a$.\n'
            '2. Tính chất của hai đại lượng tỉ lệ nghịch: Nếu hai đại lượng $y$ và $x$ tỉ lệ nghịch với nhau '
            'thì:\n'
            '- Tích hai giá trị tương ứng của chúng luôn không đổi (bằng hệ số tỉ lệ): $x_1 y_1 = x_2 y_2 = '
            'x_3 y_3 = \\cdots = a$.\n'
            '- Tỉ số hai giá trị bất kì của đại lượng này bằng nghịch đảo của tỉ số hai giá trị tương ứng '
            'của đại lượng kia: $\\dfrac{x_1}{x_2} = \\dfrac{y_2}{y_1}$.',
  'formulas': [{'category': 'Công thức và tính chất đại lượng tỉ lệ nghịch',
                'items': [{'name': 'Công thức tỉ lệ nghịch',
                           'formula': '$y = \\dfrac{a}{x} \\Leftrightarrow x \\cdot y = a \\quad (a \\neq '
                                      '0)$'},
                          {'name': 'Tích các giá trị tương ứng không đổi',
                           'formula': '$x_1 y_1 = x_2 y_2 = x_3 y_3 = a$'},
                          {'name': 'Tỉ số nghịch đảo hai cặp giá trị',
                           'formula': '$\\dfrac{x_1}{x_2} = \\dfrac{y_2}{y_1}$'}]}],
  'example': 'Cho biết $12$ công nhân có cùng năng suất hoàn thành một công việc trong $10$ ngày. Hỏi nếu có '
             '$15$ công nhân như thế thì hoàn thành công việc đó trong bao nhiêu ngày?',
  'example_answer': 'Với cùng một khối lượng công việc và cùng năng suất, số công nhân $x$ và số ngày hoàn '
                    'thành $y$ là hai đại lượng tỉ lệ nghịch.\n'
                    'Ta có $x_1 y_1 = x_2 y_2 \\Rightarrow 12 \\cdot 10 = 15 \\cdot y_2 \\Rightarrow y_2 = '
                    '\\dfrac{120}{15} = 8$ (ngày).',
  'real_life': 'Trên cùng một quãng đường cố định, vận tốc di chuyển và thời gian đi hết quãng đường là hai '
               'đại lượng tỉ lệ nghịch.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu hai đại lượng $x$ và $y$ liên hệ với nhau bởi công thức $x \\cdot y = 20$ thì:',
            'options': ['$y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $20$',
                        '$y$ tỉ lệ nghịch với $x$ theo hệ số tỉ lệ $\\dfrac{1}{20}$',
                        '$y$ tỉ lệ nghịch với $x$ theo hệ số tỉ lệ $20$',
                        '$x$ và $y$ không tỉ lệ với nhau'],
            'answer': 2,
            'solution': 'Theo định nghĩa, $x \\cdot y = a$ ($a = 20 \\neq 0$) thì $y$ tỉ lệ nghịch với $x$ '
                        'theo hệ số tỉ lệ $20$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai đại lượng $x$ và $y$ tỉ lệ nghịch với nhau. Khẳng định nào sau đây là đúng?',
            'options': ['$\\dfrac{x_1}{y_1} = \\dfrac{x_2}{y_2}$',
                        '$\\dfrac{x_1}{x_2} = \\dfrac{y_1}{y_2}$',
                        '$x_1 + y_1 = x_2 + y_2$',
                        '$x_1 y_1 = x_2 y_2$'],
            'answer': 3,
            'solution': 'Tính chất của hai đại lượng tỉ lệ nghịch là tích hai giá trị tương ứng luôn không '
                        'đổi: $x_1 y_1 = x_2 y_2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 23: Đại lượng tỉ lệ nghịch**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Công thức tỉ lệ nghịch**?',
            'options': ['$y = \\dfrac{a}{x} \\Leftrightarrow x \\cdot y = a \\quad (a \\neq 0)$',
                        '$x_1 y_1 = x_2 y_2 = x_3 y_3 = a$',
                        '$\\dfrac{x_1}{x_2} = \\dfrac{y_2}{y_1}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 23: Đại lượng tỉ lệ nghịch, **Công thức tỉ lệ '
                        'nghịch** được xác định bởi: $y = \\dfrac{a}{x} \\Leftrightarrow x \\cdot y = a '
                        '\\quad (a \\neq 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Đại lượng tỉ lệ nghịch**, nội dung/biểu thức $x_1 y_1 = x_2 y_2 = x_3 y_3 '
                 '= a$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Công thức tỉ lệ nghịch',
                        'Tích các giá trị tương ứng không đổi',
                        'Tỉ số nghịch đảo hai cặp giá trị',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 1,
            'solution': 'Trong Bài 23: Đại lượng tỉ lệ nghịch, biểu thức/quy tắc $x_1 y_1 = x_2 y_2 = x_3 '
                        'y_3 = a$ chính là nội dung của **Tích các giá trị tương ứng không đổi**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $x$ và $y$ là hai đại lượng tỉ lệ nghịch. Biết khi $x = 4$ thì $y = -9$. Hỏi khi $x = '
                 '-6$ thì $y$ bằng bao nhiêu?',
            'options': ['$-6$', '$13,5$', '$6$', '$-13,5$'],
            'answer': 2,
            'solution': 'Hệ số tỉ lệ là $a = 4 \\cdot (-9) = -36$. Khi $x = -6$ thì $y = \\dfrac{-36}{-6} = '
                        '6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Đại lượng tỉ lệ nghịch** (Chương VI: Tỉ lệ thức và đại lượng tỉ lệ), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Nhận biết được hai đại lượng tỉ lệ nghịch và hệ số tỉ lệ.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 23: Đại lượng tỉ lệ nghịch: Nhận biết được hai đại '
                        'lượng tỉ lệ nghịch và hệ số tỉ lệ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một ô tô đi từ thành phố $A$ đến thành phố $B$ cách nhau $180\\text{ km}$ với vận tốc '
                 'không đổi $v\\text{ (km/h)}$ hết thời gian $t\\text{ (giờ)}$. Xét các khẳng định sau:',
            'statements': ['Vận tốc $v$ và thời gian $t$ là hai đại lượng tỉ lệ nghịch với hệ số tỉ lệ '
                           '$180$.',
                           'Công thức tính thời gian $t$ theo vận tốc $v$ là $t = \\dfrac{180}{v}$.',
                           'Nếu ô tô đi với vận tốc $v = 60\\text{ km/h}$ thì thời gian đi là $t = 3$ giờ.',
                           'Nếu vận tốc tăng gấp đôi thì thời gian đi từ $A$ đến $B$ cũng tăng gấp đôi.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $v \\cdot t = 180$. d) Sai vì vận tốc và thời gian tỉ lệ nghịch '
                        'nên vận tốc tăng gấp đôi thì thời gian giảm đi một nửa.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 23: Đại lượng tỉ lệ '
                 'nghịch**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được hai đại lượng tỉ lệ '
                           'nghịch và hệ số tỉ lệ.',
                           'Quy tắc/công thức **Công thức tỉ lệ nghịch** trong bài được xác định bởi: $y = '
                           '\\dfrac{a}{x} \\Leftrightarrow x \\cdot y = a \\quad (a \\neq 0)$.',
                           'Trong mọi trường hợp, **Công thức tỉ lệ nghịch** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 23: Đại lượng tỉ lệ nghịch.',
                           'Với bài toán minh họa: “Cho biết $12$ công nhân có cùng năng suất hoàn thành một '
                           'công việc trong $10$ ngày. Hỏi nếu có $15$ công nhân như thế thì hoàn thành công '
                           'vi...”, lời giải đúng là: Với cùng một khối lượng công việc và cùng năng suất, '
                           'số công nhân $x$ và số ngày hoàn thành $y$ là hai đại lượng tỉ lệ nghịch. Ta '
                           'có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 23: Đại lượng tỉ lệ nghịch. b) **Đúng** '
                        'theo công thức trọng tâm **Công thức tỉ lệ nghịch** ($y = \\dfrac{a}{x} '
                        '\\Leftrightarrow x \\cdot y = a \\quad (a \\neq 0)$). c) **Sai** vì $\\mathbb{Q} = '
                        '\\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 '
                        '\\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của **Công '
                        'thức tỉ lệ nghịch**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 23: Đại lượng tỉ lệ nghịch** để giải quyết tình huống sau: Cho '
                 'biết $12$ công nhân có cùng năng suất hoàn thành một công việc trong $10$ ngày. Hỏi nếu có '
                 '$15$ công nhân như thế thì hoàn thành công việc đó trong bao nhiêu ngày? Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Với cùng một khối lượng công việc và cùng năng suất, số công nhân $x$ và số ngày '
                        'hoàn thành $y$ là hai đại lượng tỉ lệ nghịch. Ta có...',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Đại lượng tỉ lệ nghịch: Với cùng một khối lượng công '
                        'việc và cùng năng suất, số công nhân $x$ và số ngày hoàn thành $y$ là hai đại lượng '
                        'tỉ lệ nghịch.\n'
                        'Ta có $x_1 y_1 = x_2 y_2 \\Rightarrow 12 \\cdot 10 = 15 \\cdot y_2 \\Rightarrow y_2 '
                        '= \\dfrac{120}{15} = 8$ (ngày).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đội gồm $8$ máy cày có cùng năng suất cày xong một cánh đồng hết $15$ giờ. Hỏi $12$ '
                 'máy cày như thế cày xong cánh đồng đó hết bao nhiêu giờ?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Số máy cày và thời gian hoàn thành là hai đại lượng tỉ lệ nghịch nên thời gian cần '
                        'tìm là $\\dfrac{8 \\cdot 15}{12} = 10$ (giờ).',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch07-bieu-thuc-dai-so',
  'context_title': 'Chương VII: Biểu thức đại số và đa thức một biến',
  'context': 'Chương VII · SGK Toán 7: Biểu thức đại số, đa thức một biến, nghiệm của đa thức và các phép '
             'tính cộng, trừ, nhân, chia đa thức một biến.',
  'title': 'Bài 24: Biểu thức đại số',
  'icon': '🔤',
  'description': 'Khái niệm biểu thức số, biểu thức đại số, biến số và cách tính giá trị của một biểu thức '
                 'đại số.',
  'requirements': ['Nhận biết được biểu thức số và biểu thức đại số.',
                   'Tính được giá trị của một biểu thức đại số tại những giá trị cho trước của biến.',
                   'Viết được biểu thức đại số biểu thị các đại lượng quen thuộc trong toán học và thực '
                   'tiễn.'],
  'definition': 'Biểu thức bao gồm các số và các chữ (đại diện cho số) được nối với nhau bởi các kí hiệu '
                'phép tính cộng, trừ, nhân, chia, nâng lên lũy thừa được gọi là biểu thức đại số. Các chữ '
                'trong biểu thức đại số được gọi là biến số (hay gọi tắt là biến).',
  'theory': '1. Quy ước viết biểu thức đại số: Trong biểu thức đại số, ta thường không viết dấu nhân giữa '
            'chữ với số hoặc giữa chữ với chữ (ví dụ: $3 \\cdot x \\cdot y$ viết là $3xy$); hệ số $1$ hoặc '
            '$-1$ viết gọn là $x$ hoặc $-x$.\n'
            '2. Giá trị của biểu thức đại số: Để tính giá trị của một biểu thức đại số tại những giá trị cho '
            'trước của các biến, ta thay các giá trị cho trước đó vào biểu thức rồi thực hiện các phép tính.',
  'formulas': [{'category': 'Các biểu thức đại số thường gặp',
                'items': [{'name': 'Chu vi và diện tích hình chữ nhật cạnh $x, y$',
                           'formula': '$P = 2(x + y); \\quad S = xy$'},
                          {'name': 'Quãng đường đi với vận tốc $v$ trong thời gian $t$',
                           'formula': '$s = vt$'},
                          {'name': 'Giá trị biểu thức $A(x)$ tại $x = a$',
                           'formula': 'Thay $x = a$ vào biểu thức và thực hiện phép tính'}]}],
  'example': 'Tính giá trị của biểu thức đại số $A = 3x^2 - 5x + 2$ tại $x = -2$.',
  'example_answer': 'Thay $x = -2$ vào biểu thức $A$, ta được:\n'
                    '$A = 3 \\cdot (-2)^2 - 5 \\cdot (-2) + 2 = 3 \\cdot 4 + 10 + 2 = 12 + 10 + 2 = 24$.',
  'real_life': 'Công thức tính tiền cước taxi theo số kilômét di chuyển $x$: $T = 15000 + 12000(x - 1)$ '
               '(đồng) với $x \\ge 1$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Biểu thức đại số biểu thị 'Tổng của hai lần $x$ và bình phương của $y$' là:",
            'options': ['$2(x + y)^2$', '$2x^2 + y$', '$(2x + y)^2$', '$2x + y^2$'],
            'answer': 3,
            'solution': 'Hai lần $x$ là $2x$, bình phương của $y$ là $y^2$, nên tổng của chúng là $2x + '
                        'y^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu thức biểu thị diện tích của hình chữ nhật có chiều rộng $a\\text{ (cm)}$ và chiều dài '
                 'hơn chiều rộng $3\\text{ (cm)}$ là:',
            'options': ['$a(a + 3)$', '$2(a + a + 3)$', '$a(a - 3)$', '$3a$'],
            'answer': 0,
            'solution': 'Chiều dài là $a + 3$, do đó diện tích hình chữ nhật là $a(a + 3)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 24: Biểu thức đại số**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Chu vi và diện tích hình chữ nhật cạnh $x, y$**?',
            'options': ['$s = vt$',
                        '$P = 2(x + y); \\quad S = xy$',
                        'Thay $x = a$ vào biểu thức và thực hiện phép tính',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 24: Biểu thức đại số, **Chu vi và diện tích '
                        'hình chữ nhật cạnh $x, y$** được xác định bởi: $P = 2(x + y); \\quad S = xy$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: Biểu thức đại số**, nội dung/biểu thức $s = vt$ là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Chu vi và diện tích hình chữ nhật cạnh $x, y$',
                        'Giá trị biểu thức $A(x)$ tại $x = a$',
                        'Quãng đường đi với vận tốc $v$ trong thời gian $t$',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 24: Biểu thức đại số, biểu thức/quy tắc $s = vt$ chính là nội dung của '
                        '**Quãng đường đi với vận tốc $v$ trong thời gian $t$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $P = 2x^2 - 3y$ tại $x = -3$ và $y = 2$ là:',
            'options': ['$-24$', '$24$', '$-12$', '$12$'],
            'answer': 3,
            'solution': 'Thay $x = -3, y = 2$ vào $P$ ta được: $P = 2 \\cdot (-3)^2 - 3 \\cdot 2 = 2 \\cdot '
                        '9 - 6 = 12$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: Biểu thức đại số** (Chương VII: Biểu thức đại số và đa thức một biến), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được biểu thức số và biểu thức đại số.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 24: Biểu thức đại số: Nhận biết được biểu thức số và '
                        'biểu thức đại số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một người mua $x$ quyển vở giá $10$ nghìn đồng một quyển và $y$ chiếc bút giá $5$ nghìn '
                 'đồng một chiếc. Xét các khẳng định sau:',
            'statements': ['Biểu thức biểu thị tổng số tiền phải trả (nghìn đồng) là $10x + 5y$.',
                           'Trong biểu thức $10x + 5y$, các chữ $x$ và $y$ được gọi là các biến số.',
                           'Nếu mua $4$ quyển vở và $2$ chiếc bút thì tổng số tiền là $50$ nghìn đồng.',
                           'Nếu $x = 3$ và $y = 4$ thì giá trị của biểu thức $10x + 5y$ bằng $60$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b) Đúng. c) Đúng vì $10 \\cdot 4 + 5 \\cdot 2 = 50$. d) Sai vì khi $x = 3, y = '
                        '4$ thì $10 \\cdot 3 + 5 \\cdot 4 = 50 \\neq 60$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 24: Biểu thức đại số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được biểu thức số và '
                           'biểu thức đại số.',
                           'Quy tắc/công thức **Chu vi và diện tích hình chữ nhật cạnh $x, y$** trong bài '
                           'được xác định bởi: $P = 2(x + y); \\quad S = xy$.',
                           'Trong mọi trường hợp, **Chu vi và diện tích hình chữ nhật cạnh $x, y$** luôn '
                           'được tính bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; '
                           'a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập '
                           '$\\mathbb{Q}$) mà không cần điều kiện của Bài 24: Biểu thức đại số.',
                           'Với bài toán minh họa: “Tính giá trị của biểu thức đại số $A = 3x^2 - 5x + 2$ '
                           'tại $x = -2$.”, lời giải đúng là: Thay $x = -2$ vào biểu thức $A$, ta được: $A = '
                           '3 \\cdot (-2)^2 - 5 \\cdot (-2) + 2 = 3 \\cdot 4 + 10 + 2 = 12 + 10 + 2 = 24$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 24: Biểu thức đại số. b) **Đúng** theo '
                        'công thức trọng tâm **Chu vi và diện tích hình chữ nhật cạnh $x, y$** ($P = 2(x + '
                        'y); \\quad S = xy$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Chu vi và diện tích hình chữ nhật cạnh '
                        '$x, y$**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 24: Biểu thức đại số** để giải quyết tình huống sau: Tính giá trị '
                 'của biểu thức đại số $A = 3x^2 - 5x + 2$ tại $x = -2$. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Thay $x = -2$ vào biểu thức $A$, ta được: $A = 3 \\cdot (-2)^2 - 5 \\cdot (-2) + 2 '
                        '= 3 \\cdot 4 + 10 + 2 = 12 + 10 + 2 = 24$.',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: Biểu thức đại số: Thay $x = -2$ vào biểu thức $A$, '
                        'ta được:\n'
                        '$A = 3 \\cdot (-2)^2 - 5 \\cdot (-2) + 2 = 3 \\cdot 4 + 10 + 2 = 12 + 10 + 2 = '
                        '24$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $M = x^3 - 2x^2 + 5$ tại $x = 3$.',
            'answer': ['14'],
            'unit': None,
            'solution': 'Thay $x = 3$ vào $M$: $M = 3^3 - 2 \\cdot 3^2 + 5 = 27 - 18 + 5 = 14$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch07-bieu-thuc-dai-so',
  'context_title': 'Chương VII: Biểu thức đại số và đa thức một biến',
  'context': 'Chương VII · SGK Toán 7: Biểu thức đại số, đa thức một biến, nghiệm của đa thức và các phép '
             'tính cộng, trừ, nhân, chia đa thức một biến.',
  'title': 'Bài 25: Đa thức một biến',
  'icon': '🔣',
  'description': 'Đơn thức một biến, đa thức một biến, thu gọn và sắp xếp đa thức, bậc, hệ số và nghiệm của '
                 'đa thức một biến.',
  'requirements': ['Nhận biết được đơn thức một biến, đa thức một biến và dạng thu gọn của đa thức một biến.',
                   'Xác định được bậc, hệ số cao nhất, hệ số tự do của một đa thức một biến.',
                   'Nhận biết và kiểm tra được một số có phải là nghiệm của đa thức một biến hay không.'],
  'definition': 'Đa thức một biến (gọi tắt là đa thức) là tổng của những đơn thức của cùng một biến; mỗi đơn '
                'thức trong tổng gọi là một hạng tử của đa thức đó. Nếu tại $x = a$, đa thức $P(x)$ có giá '
                'trị bằng $0$, tức là $P(a) = 0$, thì $a$ gọi là một nghiệm của đa thức $P(x)$.',
  'theory': '1. Đơn thức một biến: Là biểu thức đại số có dạng tích của một số thực với một lũy thừa của '
            'biến (ví dụ: $-4x^3$ có hệ số là $-4$ và bậc là $3$).\n'
            '2. Thu gọn và sắp xếp đa thức một biến: Đa thức thu gọn là đa thức không còn hai hạng tử nào '
            'cùng bậc. Ta thường sắp xếp các hạng tử của đa thức theo lũy thừa giảm dần (hoặc tăng dần) của '
            'biến.\n'
            '3. Bậc và các hệ số của đa thức khác đa thức không (đã thu gọn):\n'
            '- Bậc của đa thức là số mũ lớn nhất của biến trong đa thức đó.\n'
            '- Hệ số của lũy thừa cao nhất gọi là hệ số cao nhất; hạng tử bậc $0$ (không chứa biến) gọi là '
            'hệ số tự do.',
  'formulas': [{'category': 'Bậc, hệ số và nghiệm của đa thức một biến',
                'items': [{'name': 'Cộng trừ hai đơn thức cùng bậc', 'formula': '$ax^k + bx^k = (a + b)x^k$'},
                          {'name': 'Đa thức bậc $n$ ($a_n \\neq 0$)',
                           'formula': '$P(x) = a_n x^n + a_{n-1} x^{n-1} + \\cdots + a_1 x + a_0$'},
                          {'name': 'Điều kiện $x = a$ là nghiệm của $P(x)$', 'formula': '$P(a) = 0$'}]}],
  'example': 'Cho đa thức $P(x) = 3x^3 - 2x + 5x^2 - 3x^3 + 6$. Hãy thu gọn, sắp xếp theo lũy thừa giảm dần '
             'của biến, tìm bậc và tính $P(-1)$.',
  'example_answer': 'Thu gọn và sắp xếp: $P(x) = (3x^3 - 3x^3) + 5x^2 - 2x + 6 = 5x^2 - 2x + 6$.\n'
                    'Đa thức $P(x)$ có bậc là $2$, hệ số cao nhất là $5$, hệ số tự do là $6$.\n'
                    'Ta có $P(-1) = 5 \\cdot (-1)^2 - 2 \\cdot (-1) + 6 = 5 + 2 + 6 = 13$.',
  'real_life': 'Biểu diễn độ cao của một quả bóng được ném lên theo thời gian $t$ (giây) bằng đa thức bậc '
               'hai $h(t) = -5t^2 + 20t + 1,5$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bậc của đa thức $P(x) = -4x^5 + 3x^3 - 2x + 7$ là:',
            'options': ['$5$', '$-4$', '$7$', '$3$'],
            'answer': 0,
            'solution': 'Số mũ cao nhất của biến $x$ trong đa thức đã thu gọn là $5$, nên bậc của đa thức là '
                        '$5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hệ số cao nhất và hệ số tự do của đa thức $Q(x) = 6x^3 - 4x^2 + x - 9$ lần lượt là:',
            'options': ['$3$ và $-9$', '$6$ và $-9$', '$6$ và $9$', '$-4$ và $1$'],
            'answer': 1,
            'solution': 'Hạng tử bậc cao nhất là $6x^3$ có hệ số cao nhất là $6$; hạng tử không chứa biến là '
                        '$-9$ (hệ số tự do).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 25: Đa thức một biến**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Cộng trừ hai đơn thức cùng bậc**?',
            'options': ['$P(x) = a_n x^n + a_{n-1} x^{n-1} + \\cdots + a_1 x + a_0$',
                        '$P(a) = 0$',
                        '$ax^k + bx^k = (a + b)x^k$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 25: Đa thức một biến, **Cộng trừ hai đơn thức '
                        'cùng bậc** được xác định bởi: $ax^k + bx^k = (a + b)x^k$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Đa thức một biến**, nội dung/biểu thức $P(x) = a_n x^n + a_{n-1} x^{n-1} + '
                 '\\cdots + a_1 x + a_0$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cộng trừ hai đơn thức cùng bậc',
                        'Điều kiện $x = a$ là nghiệm của $P(x)$',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Đa thức bậc $n$ ($a_n \\neq 0$)'],
            'answer': 3,
            'solution': 'Trong Bài 25: Đa thức một biến, biểu thức/quy tắc $P(x) = a_n x^n + a_{n-1} x^{n-1} '
                        '+ \\cdots + a_1 x + a_0$ chính là nội dung của **Đa thức bậc $n$ ($a_n \\neq '
                        '0$)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số nào sau đây là nghiệm của đa thức $A(x) = 2x - 6$?',
            'options': ['$3$', '$-3$', '$6$', '$2$'],
            'answer': 0,
            'solution': 'Ta có $A(3) = 2 \\cdot 3 - 6 = 0$, nên $x = 3$ là nghiệm của $A(x)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Đa thức một biến** (Chương VII: Biểu thức đại số và đa thức một biến), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Nhận biết được đơn thức một biến, đa thức một biến và dạng thu gọn của đa thức một '
                        'biến.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 25: Đa thức một biến: Nhận biết được đơn thức một '
                        'biến, đa thức một biến và dạng thu gọn của đa thức một biến.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đa thức $P(x) = 2x^4 + 3x^2 - 2x^4 - 3x - 9$. Xét các khẳng định sau:',
            'statements': ['Dạng thu gọn của đa thức là $P(x) = 3x^2 - 3x - 9$.',
                           'Bậc của đa thức $P(x)$ là $4$.',
                           'Hệ số cao nhất của $P(x)$ là $3$ và hệ số tự do là $-9$.',
                           'Tại $x = -1$, giá trị của $P(-1)$ bằng $-3$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $2x^4 - 2x^4 = 0$. b) Sai vì sau khi thu gọn, số mũ cao nhất là $2$ nên '
                        'bậc là $2$. c) Đúng. d) Đúng vì $P(-1) = 3(-1)^2 - 3(-1) - 9 = 3 + 3 - 9 = -3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 25: Đa thức một biến**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được đơn thức một biến, '
                           'đa thức một biến và dạng thu gọn của đa thức một biến.',
                           'Quy tắc/công thức **Cộng trừ hai đơn thức cùng bậc** trong bài được xác định '
                           'bởi: $ax^k + bx^k = (a + b)x^k$.',
                           'Trong mọi trường hợp, **Cộng trừ hai đơn thức cùng bậc** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 25: Đa thức một biến.',
                           'Với bài toán minh họa: “Cho đa thức $P(x) = 3x^3 - 2x + 5x^2 - 3x^3 + 6$. Hãy '
                           'thu gọn, sắp xếp theo lũy thừa giảm dần của biến, tìm bậc và tính $P(-1)$.”, lời '
                           'giải đúng là: Thu gọn và sắp xếp: $P(x) = (3x^3 - 3x^3) + 5x^2 - 2x + 6 = 5x^2 - '
                           '2x + 6$. Đa thức $P(x)$ có bậc là $2$, hệ số cao nhất là $5$, hệ số tự do...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 25: Đa thức một biến. b) **Đúng** theo '
                        'công thức trọng tâm **Cộng trừ hai đơn thức cùng bậc** ($ax^k + bx^k = (a + '
                        'b)x^k$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b '
                        '\\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không phải '
                        'quy tắc chung của **Cộng trừ hai đơn thức cùng bậc**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 25: Đa thức một biến** để giải quyết tình huống sau: Cho đa thức '
                 '$P(x) = 3x^3 - 2x + 5x^2 - 3x^3 + 6$. Hãy thu gọn, sắp xếp theo lũy thừa giảm dần của '
                 'biến, tìm bậc và tính $P(-1)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Thu gọn và sắp xếp: $P(x) = (3x^3 - 3x^3) + 5x^2 - 2x + 6 = 5x^2 - 2x + 6$. Đa thức '
                        '$P(x)$ có bậc là $2$, hệ số cao nhất là $5$, hệ số tự do là $6$. Ta có...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25: Đa thức một biến: Thu gọn và sắp xếp: $P(x) = (3x^3 '
                        '- 3x^3) + 5x^2 - 2x + 6 = 5x^2 - 2x + 6$.\n'
                        'Đa thức $P(x)$ có bậc là $2$, hệ số cao nhất là $5$, hệ số tự do là $6$.\n'
                        'Ta có $P(-1) = 5 \\cdot (-1)^2 - 2 \\cdot (-1) + 6 = 5 + 2 + 6 = 13$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm nghiệm của đa thức $B(x) = 3x - 15$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Cho $B(x) = 0 \\Rightarrow 3x - 15 = 0 \\Rightarrow 3x = 15 \\Rightarrow x = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch07-bieu-thuc-dai-so',
  'context_title': 'Chương VII: Biểu thức đại số và đa thức một biến',
  'context': 'Chương VII · SGK Toán 7: Biểu thức đại số, đa thức một biến, nghiệm của đa thức và các phép '
             'tính cộng, trừ, nhân, chia đa thức một biến.',
  'title': 'Bài 26: Phép cộng và phép trừ đa thức một biến',
  'icon': '➕',
  'description': 'Quy tắc cộng, trừ hai đa thức một biến theo hàng ngang hoặc theo cột dọc.',
  'requirements': ['Thực hiện được phép cộng và phép trừ hai đa thức một biến.',
                   'Vận dụng được các tính chất giao hoán, kết hợp của phép cộng đa thức trong tính toán.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Cộng hai hạng tử cùng bậc** ($ax^k + bx^k = '
                   '(a + b)x^k$) vào giải bài tập.'],
  'definition': 'Để cộng hoặc trừ hai đa thức một biến, ta có thể đặt tính theo hàng ngang (bỏ dấu ngoặc rồi '
                'nhóm các hạng tử cùng bậc) hoặc đặt tính theo cột dọc (sắp xếp các hạng tử cùng bậc thẳng '
                'cột với nhau rồi cộng hoặc trừ các hệ số).',
  'theory': '1. Cộng, trừ theo hàng ngang: Viết tổng $P(x) + Q(x)$ hoặc hiệu $P(x) - Q(x)$, áp dụng quy tắc '
            'bỏ dấu ngoặc (lưu ý đổi dấu tất cả các hạng tử trong ngoặc khi trước ngoặc có dấu $-$) rồi thu '
            'gọn các đơn thức cùng bậc.\n'
            '2. Cộng, trừ theo cột dọc: Thu gọn và sắp xếp hai đa thức theo lũy thừa giảm dần của biến, đặt '
            'các hạng tử cùng bậc ở cùng một cột rồi cộng (hoặc trừ) theo từng cột.',
  'formulas': [{'category': 'Quy tắc cộng, trừ hai đa thức',
                'items': [{'name': 'Cộng hai hạng tử cùng bậc', 'formula': '$ax^k + bx^k = (a + b)x^k$'},
                          {'name': 'Trừ hai hạng tử cùng bậc', 'formula': '$ax^k - bx^k = (a - b)x^k$'},
                          {'name': 'Quy tắc đổi dấu khi trừ đa thức',
                           'formula': '$P(x) - (ax^2 - bx + c) = P(x) - ax^2 + bx - c$'}]}],
  'example': 'Cho $P(x) = 3x^2 - 4x + 1$ và $Q(x) = x^2 + 4x - 5$. Tính $P(x) + Q(x)$ và $P(x) - Q(x)$.',
  'example_answer': '- $P(x) + Q(x) = (3x^2 + x^2) + (-4x + 4x) + (1 - 5) = 4x^2 - 4$.\n'
                    '- $P(x) - Q(x) = (3x^2 - x^2) + (-4x - 4x) + (1 - (-5)) = 2x^2 - 8x + 6$.',
  'real_life': 'Tính lợi nhuận của doanh nghiệp bằng cách lấy đa thức doanh thu $R(x)$ trừ đi đa thức chi '
               'phí $C(x)$: $L(x) = R(x) - C(x)$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai đa thức $A(x) = 2x^2 + 3x$ và $B(x) = x^2 - x$. Tổng $A(x) + B(x)$ bằng:',
            'options': ['$x^2 + 4x$', '$3x^2 + 2x$', '$3x^2 + 4x$', '$3x^4 + 2x^2$'],
            'answer': 1,
            'solution': '$A(x) + B(x) = (2x^2 + x^2) + (3x - x) = 3x^2 + 2x$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $M(x) = 5x - 3$ và $N(x) = 2x - 7$. Hiệu $M(x) - N(x)$ bằng:',
            'options': ['$3x - 10$', '$7x - 10$', '$3x + 4$', '$3x - 4$'],
            'answer': 2,
            'solution': '$M(x) - N(x) = (5x - 3) - (2x - 7) = 5x - 3 - 2x + 7 = 3x + 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 26: Phép cộng và phép trừ đa thức một biến**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Cộng hai hạng tử cùng bậc**?',
            'options': ['$ax^k - bx^k = (a - b)x^k$',
                        '$P(x) - (ax^2 - bx + c) = P(x) - ax^2 + bx - c$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$ax^k + bx^k = (a + b)x^k$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 26: Phép cộng và phép trừ đa thức một biến, '
                        '**Cộng hai hạng tử cùng bậc** được xác định bởi: $ax^k + bx^k = (a + b)x^k$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Phép cộng và phép trừ đa thức một biến**, nội dung/biểu thức $ax^k - bx^k '
                 '= (a - b)x^k$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Trừ hai hạng tử cùng bậc',
                        'Cộng hai hạng tử cùng bậc',
                        'Quy tắc đổi dấu khi trừ đa thức',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Trong Bài 26: Phép cộng và phép trừ đa thức một biến, biểu thức/quy tắc $ax^k - '
                        'bx^k = (a - b)x^k$ chính là nội dung của **Trừ hai hạng tử cùng bậc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đa thức $P(x)$ thỏa mãn $P(x) + (x^2 - 2x + 5) = 3x^2 + x - 1$ là:',
            'options': ['$4x^2 - x + 4$', '$2x^2 + 3x - 6$', '$2x^2 - x + 4$', '$2x^2 + 3x + 6$'],
            'answer': 1,
            'solution': '$P(x) = (3x^2 + x - 1) - (x^2 - 2x + 5) = 2x^2 + 3x - 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Phép cộng và phép trừ đa thức một biến** (Chương VII: Biểu thức đại số '
                 'và đa thức một biến), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Thực hiện được phép cộng và phép trừ hai đa thức một biến.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 26: Phép cộng và phép trừ đa thức một biến: Thực hiện '
                        'được phép cộng và phép trừ hai đa thức một biến.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai đa thức $P(x) = 2x^3 - 3x^2 + 5$ và $Q(x) = -2x^3 + 3x^2 + 2x - 1$. Xét các khẳng '
                 'định sau:',
            'statements': ['Tổng hai đa thức là $P(x) + Q(x) = 2x + 4$.',
                           'Bậc của đa thức tổng $P(x) + Q(x)$ là bậc $3$.',
                           'Hiệu hai đa thức là $P(x) - Q(x) = 4x^3 - 6x^2 - 2x + 6$.',
                           'Nghiệm của đa thức $P(x) + Q(x)$ là $x = -2$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì $P(x) + Q(x) = 2x + 4$ có bậc là $1$. c) Đúng. d) Đúng vì $2(-2) '
                        '+ 4 = 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 26: Phép cộng và phép '
                 'trừ đa thức một biến**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được phép cộng và phép '
                           'trừ hai đa thức một biến.',
                           'Quy tắc/công thức **Cộng hai hạng tử cùng bậc** trong bài được xác định bởi: '
                           '$ax^k + bx^k = (a + b)x^k$.',
                           'Trong mọi trường hợp, **Cộng hai hạng tử cùng bậc** luôn được tính bằng công '
                           'thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 26: Phép cộng và phép trừ đa thức một biến.',
                           'Với bài toán minh họa: “Cho $P(x) = 3x^2 - 4x + 1$ và $Q(x) = x^2 + 4x - 5$. '
                           'Tính $P(x) + Q(x)$ và $P(x) - Q(x)$.”, lời giải đúng là: - $P(x) + Q(x) = (3x^2 '
                           '+ x^2) + (-4x + 4x) + (1 - 5) = 4x^2 - 4$. - $P(x) - Q(x) = (3x^2 - x^2) + (-4x '
                           '- 4x) + (1 - (-5)) = 2x^2 - 8x + 6$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 26: Phép cộng và phép trừ đa thức một '
                        'biến. b) **Đúng** theo công thức trọng tâm **Cộng hai hạng tử cùng bậc** ($ax^k + '
                        'bx^k = (a + b)x^k$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} '
                        '\\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội '
                        'dung khác, không phải quy tắc chung của **Cộng hai hạng tử cùng bậc**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 26: Phép cộng và phép trừ đa thức một biến** để giải quyết tình '
                 'huống sau: Cho $P(x) = 3x^2 - 4x + 1$ và $Q(x) = x^2 + 4x - 5$. Tính $P(x) + Q(x)$ và '
                 '$P(x) - Q(x)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        '- $P(x) + Q(x) = (3x^2 + x^2) + (-4x + 4x) + (1 - 5) = 4x^2 - 4$. - $P(x) - Q(x) = '
                        '(3x^2 - x^2) + (-4x - 4x) + (1 - (-5)) = 2x^2 - 8x + 6$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 26: Phép cộng và phép trừ đa thức một biến: - $P(x) + '
                        'Q(x) = (3x^2 + x^2) + (-4x + 4x) + (1 - 5) = 4x^2 - 4$.\n'
                        '- $P(x) - Q(x) = (3x^2 - x^2) + (-4x - 4x) + (1 - (-5)) = 2x^2 - 8x + 6$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $A(x) = 4x^2 - 3x + 7$ và $B(x) = 3x^2 - 3x + 2$. Tính giá trị của đa thức $H(x) = '
                 'A(x) - B(x)$ tại $x = 2$.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Ta có $H(x) = A(x) - B(x) = x^2 + 5$. Tại $x = 2$, $H(2) = 2^2 + 5 = 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch07-bieu-thuc-dai-so',
  'context_title': 'Chương VII: Biểu thức đại số và đa thức một biến',
  'context': 'Chương VII · SGK Toán 7: Biểu thức đại số, đa thức một biến, nghiệm của đa thức và các phép '
             'tính cộng, trừ, nhân, chia đa thức một biến.',
  'title': 'Bài 27: Phép nhân đa thức một biến',
  'icon': '✖️',
  'description': 'Quy tắc nhân hai đơn thức, nhân đơn thức với đa thức và nhân hai đa thức một biến.',
  'requirements': ['Thực hiện được phép nhân đơn thức với đơn thức và nhân đơn thức với đa thức một biến.',
                   'Thực hiện được phép nhân hai đa thức một biến và thu gọn kết quả.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Nhân hai đơn thức** ($(ax^m) \\cdot (bx^n) '
                   '= (ab)x^{m+n}$) vào giải bài tập.'],
  'definition': 'Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức với từng hạng tử của đa thức rồi '
                'cộng các tích với nhau. Muốn nhân một đa thức với một đa thức, ta nhân mỗi hạng tử của đa '
                'thức này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.',
  'theory': '1. Nhân hai đơn thức một biến: Nhân hai hệ số với nhau và nhân hai lũy thừa của biến với nhau: '
            '$(ax^m) \\cdot (bx^n) = (a \\cdot b)x^{m+n}$.\n'
            '2. Nhân đơn thức với đa thức: $A \\cdot (B + C) = A \\cdot B + A \\cdot C$.\n'
            '3. Nhân đa thức với đa thức: $(A + B) \\cdot (C + D) = A \\cdot C + A \\cdot D + B \\cdot C + B '
            '\\cdot D$.',
  'formulas': [{'category': 'Các quy tắc nhân đa thức một biến',
                'items': [{'name': 'Nhân hai đơn thức', 'formula': '$(ax^m) \\cdot (bx^n) = (ab)x^{m+n}$'},
                          {'name': 'Nhân đơn thức với đa thức', 'formula': '$A(B + C - D) = AB + AC - AD$'},
                          {'name': 'Nhân hai đa thức', 'formula': '$(A + B)(C + D) = AC + AD + BC + BD$'}]}],
  'example': 'Thực hiện phép nhân: $(2x - 3)(x^2 - 2x + 1)$.',
  'example_answer': 'Ta có: $(2x - 3)(x^2 - 2x + 1) = 2x(x^2 - 2x + 1) - 3(x^2 - 2x + 1)$\n'
                    '$= 2x^3 - 4x^2 + 2x - 3x^2 + 6x - 3 = 2x^3 - 7x^2 + 8x - 3$.',
  'real_life': 'Biểu diễn diện tích lối đi hoặc diện tích mảnh vườn hình chữ nhật sau khi mở rộng chiều dài '
               'thêm $a\\text{ (m)}$ và chiều rộng thêm $b\\text{ (m)}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân hai đơn thức $(-3x^2) \\cdot (4x^3)$ là:',
            'options': ['$-12x^6$', '$12x^5$', '$-12x^5$', '$x^5$'],
            'answer': 2,
            'solution': '$(-3x^2) \\cdot (4x^3) = (-3 \\cdot 4) \\cdot (x^2 \\cdot x^3) = -12x^5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $2x(x^2 - 3x + 4)$ là:',
            'options': ['$2x^3 - 3x + 4$', '$2x^3 - 6x + 8$', '$2x^2 - 6x + 8$', '$2x^3 - 6x^2 + 8x$'],
            'answer': 3,
            'solution': '$2x(x^2 - 3x + 4) = 2x \\cdot x^2 - 2x \\cdot 3x + 2x \\cdot 4 = 2x^3 - 6x^2 + 8x$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 27: Phép nhân đa thức một biến**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Nhân hai đơn thức**?',
            'options': ['$(ax^m) \\cdot (bx^n) = (ab)x^{m+n}$',
                        '$A(B + C - D) = AB + AC - AD$',
                        '$(A + B)(C + D) = AC + AD + BC + BD$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 27: Phép nhân đa thức một biến, **Nhân hai '
                        'đơn thức** được xác định bởi: $(ax^m) \\cdot (bx^n) = (ab)x^{m+n}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Phép nhân đa thức một biến**, nội dung/biểu thức $A(B + C - D) = AB + AC - '
                 'AD$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Nhân hai đơn thức',
                        'Nhân đơn thức với đa thức',
                        'Nhân hai đa thức',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 1,
            'solution': 'Trong Bài 27: Phép nhân đa thức một biến, biểu thức/quy tắc $A(B + C - D) = AB + AC '
                        '- AD$ chính là nội dung của **Nhân đơn thức với đa thức**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khai triển và thu gọn tích $(x + 2)(x - 5)$ ta được đa thức nào?',
            'options': ['$x^2 + 3x - 10$', '$x^2 - 7x - 10$', '$x^2 - 3x - 10$', '$x^2 - 10$'],
            'answer': 2,
            'solution': '$(x + 2)(x - 5) = x^2 - 5x + 2x - 10 = x^2 - 3x - 10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Phép nhân đa thức một biến** (Chương VII: Biểu thức đại số và đa thức '
                 'một biến), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Thực hiện được phép nhân đơn thức với đơn thức và nhân đơn thức với đa thức một '
                        'biến.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 27: Phép nhân đa thức một biến: Thực hiện được phép '
                        'nhân đơn thức với đơn thức và nhân đơn thức với đa thức một biến.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đa thức $P(x) = (x - 1)(x^2 + x + 1)$. Xét các khẳng định sau:',
            'statements': ['Khi nhân phân phối và thu gọn, ta được $P(x) = x^3 - 1$.',
                           'Đa thức $P(x)$ có bậc là $3$.',
                           'Hệ số của hạng tử bậc hai ($x^2$) trong $P(x)$ sau khi thu gọn bằng $0$.',
                           'Giá trị của $P(2)$ bằng $9$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $(x - 1)(x^2 + x + 1) = x^3 + x^2 + x - x^2 - x - 1 = x^3 - 1$. '
                        'd) Sai vì $P(2) = 2^3 - 1 = 7 \\neq 9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 27: Phép nhân đa thức '
                 'một biến**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được phép nhân đơn thức '
                           'với đơn thức và nhân đơn thức với đa thức một biến.',
                           'Quy tắc/công thức **Nhân hai đơn thức** trong bài được xác định bởi: $(ax^m) '
                           '\\cdot (bx^n) = (ab)x^{m+n}$.',
                           'Trong mọi trường hợp, **Nhân hai đơn thức** luôn được tính bằng công thức '
                           '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                           '\\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không cần điều kiện '
                           'của Bài 27: Phép nhân đa thức một biến.',
                           'Với bài toán minh họa: “Thực hiện phép nhân: $(2x - 3)(x^2 - 2x + 1)$.”, lời '
                           'giải đúng là: Ta có: $(2x - 3)(x^2 - 2x + 1) = 2x(x^2 - 2x + 1) - 3(x^2 - 2x + '
                           '1)$ $= 2x^3 - 4x^2 + 2x - 3x^2 + 6x - 3 = 2x^3 - 7x^2 + 8x - 3$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 27: Phép nhân đa thức một biến. b) '
                        '**Đúng** theo công thức trọng tâm **Nhân hai đơn thức** ($(ax^m) \\cdot (bx^n) = '
                        '(ab)x^{m+n}$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; '
                        'a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Nhân hai đơn thức**. d) **Đúng** theo lời giải ví dụ minh '
                        'họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 27: Phép nhân đa thức một biến** để giải quyết tình huống sau: '
                 'Thực hiện phép nhân: $(2x - 3)(x^2 - 2x + 1)$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có: $(2x - 3)(x^2 - 2x + 1) = 2x(x^2 - 2x + 1) - 3(x^2 - 2x + 1)$ $= 2x^3 - 4x^2 '
                        '+ 2x - 3x^2 + 6x - 3 = 2x^3 - 7x^2 + 8x - 3$.',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 27: Phép nhân đa thức một biến: Ta có: $(2x - 3)(x^2 - '
                        '2x + 1) = 2x(x^2 - 2x + 1) - 3(x^2 - 2x + 1)$\n'
                        '$= 2x^3 - 4x^2 + 2x - 3x^2 + 6x - 3 = 2x^3 - 7x^2 + 8x - 3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn biểu thức $A = (x + 3)(x - 1) - x^2$ rồi tính giá trị của $A$ tại $x = 5$.',
            'answer': ['7'],
            'unit': None,
            'solution': 'Ta có $A = x^2 + 2x - 3 - x^2 = 2x - 3$. Tại $x = 5$, $A = 2 \\cdot 5 - 3 = 7$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch07-bieu-thuc-dai-so',
  'context_title': 'Chương VII: Biểu thức đại số và đa thức một biến',
  'context': 'Chương VII · SGK Toán 7: Biểu thức đại số, đa thức một biến, nghiệm của đa thức và các phép '
             'tính cộng, trừ, nhân, chia đa thức một biến.',
  'title': 'Bài 28: Phép chia đa thức một biến',
  'icon': '➗',
  'description': 'Chia đơn thức cho đơn thức, chia đa thức cho đơn thức và chia đa thức một biến đã sắp xếp '
                 '(chia hết và chia có dư).',
  'requirements': ['Thực hiện được phép chia đơn thức cho đơn thức và chia đa thức cho đơn thức.',
                   'Thực hiện được phép chia đa thức một biến cho đa thức một biến (trường hợp chia hết và '
                   'chia có dư).',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Chia đơn thức cho đơn thức** ($(ax^m) : '
                   '(bx^n) = \\dfrac{a}{b}x^{m-n} \\quad (b \\neq 0, m \\ge n)$) vào giải bài tập.'],
  'definition': 'Cho hai đa thức $A$ và $B$ ($B \\neq 0$). Khi đó luôn tồn tại duy nhất cặp đa thức $Q$ '
                '(thương) và $R$ (dư) sao cho $A = B \\cdot Q + R$, trong đó $R = 0$ (phép chia hết) hoặc '
                'bậc của $R$ nhỏ hơn bậc của $B$ (phép chia có dư).',
  'theory': '1. Chia đơn thức cho đơn thức: Với $b \\neq 0$ và $m \\ge n$, ta có $(ax^m) : (bx^n) = '
            '\\dfrac{a}{b} x^{m-n}$.\n'
            '2. Chia đa thức cho đơn thức: Nếu mỗi hạng tử của đa thức $A$ đều chia hết cho đơn thức $B$ thì '
            'ta chia từng hạng tử của $A$ cho $B$ rồi cộng các kết quả lại.\n'
            '3. Chia hai đa thức một biến đã sắp xếp: Đặt tính chia tương tự phép chia các số tự nhiên theo '
            'thứ tự lũy thừa giảm dần của biến cho đến khi đa thức dư bằng $0$ hoặc có bậc nhỏ hơn bậc của '
            'đa thức chia.',
  'formulas': [{'category': 'Các quy tắc chia đa thức một biến',
                'items': [{'name': 'Chia đơn thức cho đơn thức',
                           'formula': '$(ax^m) : (bx^n) = \\dfrac{a}{b}x^{m-n} \\quad (b \\neq 0, m \\ge '
                                      'n)$'},
                          {'name': 'Chia đa thức cho đơn thức',
                           'formula': '$(A + B - C) : D = (A : D) + (B : D) - (C : D)$'},
                          {'name': 'Hệ thức phép chia có dư',
                           'formula': '$A = B \\cdot Q + R \\quad (\\text{với } R = 0 \\text{ hoặc } '
                                      '\\deg(R) < \\deg(B))$'}]}],
  'example': 'Thực hiện phép chia đa thức $(2x^2 - 5x + 3)$ cho $(x - 1)$.',
  'example_answer': 'Đặt tính chia hoặc tách hạng tử: $2x^2 - 5x + 3 = 2x(x - 1) - 3(x - 1) = (2x - 3)(x - '
                    '1)$.\n'
                    'Vậy $(2x^2 - 5x + 3) : (x - 1) = 2x - 3$ (phép chia hết, dư $R = 0$).',
  'real_life': 'Tìm chiều dài của một mảnh đất hình chữ nhật dưới dạng đa thức khi biết đa thức diện tích và '
               'đa thức biểu thị chiều rộng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia đơn thức $(12x^5) : (3x^2)$ là:',
            'options': ['$9x^3$', '$4x^7$', '$4x^2$', '$4x^3$'],
            'answer': 3,
            'solution': '$(12x^5) : (3x^2) = (12 : 3) \\cdot x^{5-2} = 4x^3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $(6x^3 - 9x^2 + 3x) : (3x)$ là:',
            'options': ['$2x^2 - 3x + 1$', '$2x^2 - 3x$', '$2x^3 - 3x^2 + 1$', '$3x^2 - 6x + 1$'],
            'answer': 0,
            'solution': 'Chia từng hạng tử cho $3x$: $(6x^3 : 3x) - (9x^2 : 3x) + (3x : 3x) = 2x^2 - 3x + '
                        '1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 28: Phép chia đa thức một biến**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Chia đơn thức cho đơn thức**?',
            'options': ['$(A + B - C) : D = (A : D) + (B : D) - (C : D)$',
                        '$(ax^m) : (bx^n) = \\dfrac{a}{b}x^{m-n} \\quad (b \\neq 0, m \\ge n)$',
                        '$A = B \\cdot Q + R \\quad (\\text{với } R = 0 \\text{ hoặc } \\deg(R) < \\deg(B))$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 28: Phép chia đa thức một biến, **Chia đơn '
                        'thức cho đơn thức** được xác định bởi: $(ax^m) : (bx^n) = \\dfrac{a}{b}x^{m-n} '
                        '\\quad (b \\neq 0, m \\ge n)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 28: Phép chia đa thức một biến**, nội dung/biểu thức $(A + B - C) : D = (A : '
                 'D) + (B : D) - (C : D)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Chia đơn thức cho đơn thức',
                        'Hệ thức phép chia có dư',
                        'Chia đa thức cho đơn thức',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 28: Phép chia đa thức một biến, biểu thức/quy tắc $(A + B - C) : D = (A : '
                        'D) + (B : D) - (C : D)$ chính là nội dung của **Chia đa thức cho đơn thức**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thương của phép chia $(x^2 - 4x + 3) : (x - 1)$ là:',
            'options': ['$x + 3$', '$x - 4$', '$x + 1$', '$x - 3$'],
            'answer': 3,
            'solution': 'Vì $(x - 1)(x - 3) = x^2 - 4x + 3$ nên $(x^2 - 4x + 3) : (x - 1) = x - 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 28: Phép chia đa thức một biến** (Chương VII: Biểu thức đại số và đa thức '
                 'một biến), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Thực hiện được phép chia đơn thức cho đơn thức và chia đa thức cho đơn thức.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 28: Phép chia đa thức một biến: Thực hiện được phép '
                        'chia đơn thức cho đơn thức và chia đa thức cho đơn thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Thực hiện phép chia đa thức $A(x) = x^2 + 3x + 5$ cho đa thức $B(x) = x + 1$. Xét các '
                 'khẳng định sau:',
            'statements': ['Ta có đẳng thức $x^2 + 3x + 5 = (x + 1)(x + 2) + 3$.',
                           'Đa thức thương của phép chia là $Q(x) = x + 2$.',
                           'Số dư của phép chia là $R = 3$.',
                           'Đây là một phép chia hết.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $(x+1)(x+2) + 3 = x^2 + 3x + 2 + 3 = x^2 + 3x + 5$. d) Sai vì dư '
                        '$R = 3 \\neq 0$ nên đây là phép chia có dư.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 28: Phép chia đa thức '
                 'một biến**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thực hiện được phép chia đơn thức '
                           'cho đơn thức và chia đa thức cho đơn thức.',
                           'Quy tắc/công thức **Chia đơn thức cho đơn thức** trong bài được xác định bởi: '
                           '$(ax^m) : (bx^n) = \\dfrac{a}{b}x^{m-n} \\quad (b \\neq 0, m \\ge n)$.',
                           'Trong mọi trường hợp, **Chia đơn thức cho đơn thức** luôn được tính bằng công '
                           'thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 28: Phép chia đa thức một biến.',
                           'Với bài toán minh họa: “Thực hiện phép chia đa thức $(2x^2 - 5x + 3)$ cho $(x - '
                           '1)$.”, lời giải đúng là: Đặt tính chia hoặc tách hạng tử: $2x^2 - 5x + 3 = 2x(x '
                           '- 1) - 3(x - 1) = (2x - 3)(x - 1)$. Vậy $(2x^2 - 5x + 3) : (x - 1) = 2x - 3$ '
                           '(phép ch...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 28: Phép chia đa thức một biến. b) '
                        '**Đúng** theo công thức trọng tâm **Chia đơn thức cho đơn thức** ($(ax^m) : (bx^n) '
                        '= \\dfrac{a}{b}x^{m-n} \\quad (b \\neq 0, m \\ge n)$). c) **Sai** vì $\\mathbb{Q} = '
                        '\\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 '
                        '\\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của **Chia đơn '
                        'thức cho đơn thức**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 28: Phép chia đa thức một biến** để giải quyết tình huống sau: '
                 'Thực hiện phép chia đa thức $(2x^2 - 5x + 3)$ cho $(x - 1)$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Đặt tính chia hoặc tách hạng tử: $2x^2 - 5x + 3 = 2x(x - 1) - 3(x - 1) = (2x - 3)(x '
                        '- 1)$. Vậy $(2x^2 - 5x + 3) : (x - 1) = 2x - 3$ (phép chia hết, dư $R = 0$...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 28: Phép chia đa thức một biến: Đặt tính chia hoặc tách '
                        'hạng tử: $2x^2 - 5x + 3 = 2x(x - 1) - 3(x - 1) = (2x - 3)(x - 1)$.\n'
                        'Vậy $(2x^2 - 5x + 3) : (x - 1) = 2x - 3$ (phép chia hết, dư $R = 0$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số dư của phép chia đa thức $P(x) = x^3 - 2x^2 + x + 4$ cho $x - 2$.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Ta có $x^3 - 2x^2 + x + 4 = x^2(x - 2) + (x - 2) + 6 = (x^2 + 1)(x - 2) + 6$. Vậy '
                        'số dư là $6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch08-xac-suat',
  'context_title': 'Chương VIII: Làm quen với biến cố và xác suất của biến cố',
  'context': 'Chương VIII · SGK Toán 7: Làm quen với biến cố ngẫu nhiên, biến cố chắc chắn, biến cố không '
             'thể và xác suất của biến cố.',
  'title': 'Bài 29: Làm quen với biến cố',
  'icon': '🎲',
  'description': 'Nhận biết biến cố ngẫu nhiên, biến cố chắc chắn và biến cố không thể trong một số trò '
                 'chơi, thí nghiệm đơn giản.',
  'requirements': ['Làm quen với các khái niệm mở đầu về biến cố trong các trò chơi, thí nghiệm đơn giản.',
                   'Phân biệt được biến cố chắc chắn, biến cố không thể và biến cố ngẫu nhiên.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tập kết quả khi gieo 1 con xúc xắc** '
                   '($\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ (gồm $6$ kết quả có thể)) vào giải bài tập.'],
  'definition': 'Các hiện tượng, sự kiện trong tự nhiên hay trong một phép thử nghiệm được gọi chung là biến '
                'cố. Biến cố luôn xảy ra gọi là biến cố chắc chắn; biến cố không bao giờ xảy ra gọi là biến '
                'cố không thể; biến cố không biết trước có xảy ra hay không gọi là biến cố ngẫu nhiên.',
  'theory': 'Phân loại ba loại biến cố cơ bản:\n'
            '1. Biến cố chắc chắn: Là biến cố biết trước luôn luôn xảy ra (ví dụ: Gieo một con xúc xắc $6$ '
            "mặt, biến cố 'Số chấm xuất hiện nhỏ hơn $7$').\n"
            '2. Biến cố không thể: Là biến cố biết trước không bao giờ xảy ra (ví dụ: Gieo một con xúc xắc '
            "$6$ mặt, biến cố 'Số chấm xuất hiện bằng $8$').\n"
            '3. Biến cố ngẫu nhiên: Là biến cố không thể biết trước được có xảy ra hay không (ví dụ: Gieo '
            "một con xúc xắc $6$ mặt, biến cố 'Xuất hiện mặt $6$ chấm').",
  'formulas': [{'category': 'Phân loại biến cố và tập kết quả',
                'items': [{'name': 'Tập kết quả khi gieo 1 con xúc xắc',
                           'formula': '$\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ (gồm $6$ kết quả có thể)'},
                          {'name': 'Ba loại biến cố',
                           'formula': 'Biến cố chắc chắn $\\mid$ Biến cố không thể $\\mid$ Biến cố ngẫu '
                                      'nhiên'}]}],
  'example': "Gieo một con xúc xắc cân đối $6$ mặt. Xét biến cố $A$: 'Số chấm xuất hiện là số tự nhiên từ "
             "$1$ đến $6$' và biến cố $B$: 'Số chấm xuất hiện là số chẵn'. Phân loại biến cố $A$ và $B$.",
  'example_answer': '- Biến cố $A$ là biến cố chắc chắn vì mặt nào của xúc xắc cũng có số chấm từ $1$ đến '
                    '$6$.\n'
                    '- Biến cố $B$ là biến cố ngẫu nhiên vì có thể xảy ra (khi ra mặt $2, 4, 6$) hoặc không '
                    'xảy ra (khi ra mặt $1, 3, 5$).',
  'real_life': 'Dự báo các sự kiện thời tiết (khả năng có mưa rào chiều mai là một biến cố ngẫu nhiên; mặt '
               'trời mọc ở hướng Đông là biến cố chắc chắn).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Gieo một con xúc xắc $6$ mặt cân đối. Biến cố 'Số chấm xuất hiện bằng $7$' là:",
            'options': ['Biến cố không thể',
                        'Biến cố chắc chắn',
                        'Biến cố ngẫu nhiên',
                        'Biến cố đồng khả năng'],
            'answer': 0,
            'solution': 'Con xúc xắc chỉ có các mặt từ $1$ đến $6$ chấm nên không bao giờ xuất hiện mặt $7$ '
                        'chấm (biến cố không thể).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một hộp kín chỉ có $5$ quả bóng màu đỏ. Lấy ngẫu nhiên $1$ quả bóng từ hộp. Biến cố '
                 "'Lấy được quả bóng màu đỏ' là:",
            'options': ['Biến cố không thể', 'Biến cố chắc chắn', 'Biến cố ngẫu nhiên', 'Biến cố hiếm gặp'],
            'answer': 1,
            'solution': 'Vì trong hộp chỉ toàn bóng màu đỏ nên lấy ra 1 quả chắc chắn là màu đỏ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 29: Làm quen với biến cố**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Tập kết quả khi gieo 1 con xúc xắc**?',
            'options': ['Biến cố chắc chắn $\\mid$ Biến cố không thể $\\mid$ Biến cố ngẫu nhiên',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ (gồm $6$ kết quả có thể)',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 29: Làm quen với biến cố, **Tập kết quả khi '
                        'gieo 1 con xúc xắc** được xác định bởi: $\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ (gồm $6$ '
                        'kết quả có thể).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Làm quen với biến cố**, nội dung/biểu thức Biến cố chắc chắn $\\mid$ Biến '
                 'cố không thể $\\mid$ Biến cố ngẫu nhiên là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tập kết quả khi gieo 1 con xúc xắc',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp',
                        'Ba loại biến cố'],
            'answer': 3,
            'solution': 'Trong Bài 29: Làm quen với biến cố, biểu thức/quy tắc Biến cố chắc chắn $\\mid$ '
                        'Biến cố không thể $\\mid$ Biến cố ngẫu nhiên chính là nội dung của **Ba loại biến '
                        'cố**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Rút ngẫu nhiên một thẻ từ hộp đựng $10$ thẻ đánh số từ $1$ đến $10$. Biến cố nào sau đây '
                 'là biến cố ngẫu nhiên?',
            'options': ['Số trên thẻ rút được là số nguyên tố',
                        'Số trên thẻ rút được là số tự nhiên lớn hơn $0$',
                        'Số trên thẻ rút được là số $15$',
                        'Số trên thẻ rút được là số âm'],
            'answer': 0,
            'solution': "Trong các số từ $1$ đến $10$ có các số nguyên tố ($2; 3; 5; 7$) và hợp số, nên 'Rút "
                        "được số nguyên tố' là biến cố ngẫu nhiên.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Làm quen với biến cố** (Chương VIII: Làm quen với biến cố và xác suất '
                 'của biến cố), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Làm quen với các khái niệm mở đầu về biến cố trong các trò chơi, thí nghiệm đơn '
                        'giản.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 29: Làm quen với biến cố: Làm quen với các khái niệm '
                        'mở đầu về biến cố trong các trò chơi, thí nghiệm đơn giản.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một hộp có $4$ chiếc thẻ được ghi các số $2; 4; 6; 8$. Rút ngẫu nhiên một chiếc thẻ từ '
                 'hộp. Xét các khẳng định sau:',
            'statements': ["Biến cố $A$: 'Rút được thẻ ghi số chẵn' là biến cố chắc chắn.",
                           "Biến cố $B$: 'Rút được thẻ ghi số lẻ' là biến cố không thể.",
                           "Biến cố $C$: 'Rút được thẻ ghi số chia hết cho $3$' là biến cố ngẫu nhiên.",
                           "Biến cố $D$: 'Rút được thẻ ghi số nhỏ hơn $10$' là biến cố ngẫu nhiên."],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng (số $6$ chia hết cho $3$). d) Sai vì cả 4 số $2; 4; 6; 8$ đều nhỏ '
                        'hơn $10$ nên $D$ là biến cố chắc chắn.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 29: Làm quen với biến '
                 'cố**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Làm quen với các khái niệm mở đầu '
                           'về biến cố trong các trò chơi, thí nghiệm đơn giản.',
                           'Quy tắc/công thức **Tập kết quả khi gieo 1 con xúc xắc** trong bài được xác định '
                           'bởi: $\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ (gồm $6$ kết quả có thể).',
                           'Trong mọi trường hợp, **Tập kết quả khi gieo 1 con xúc xắc** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 29: Làm quen với biến cố.',
                           'Với bài toán minh họa: “Gieo một con xúc xắc cân đối $6$ mặt. Xét biến cố $A$: '
                           "'Số chấm xuất hiện là số tự nhiên từ $1$ đến $6$' và biến cố $B$: 'Số chấm xuất "
                           'hiện...”, lời giải đúng là: - Biến cố $A$ là biến cố chắc chắn vì mặt nào của '
                           'xúc xắc cũng có số chấm từ $1$ đến $6$. - Biến cố $B$ là biến cố ngẫu nhiên vì '
                           'có thể xảy...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 29: Làm quen với biến cố. b) **Đúng** theo '
                        'công thức trọng tâm **Tập kết quả khi gieo 1 con xúc xắc** ($\\Omega = \\{1; 2; 3; '
                        '4; 5; 6\\}$ (gồm $6$ kết quả có thể)). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Tập kết quả khi gieo 1 con '
                        'xúc xắc**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 29: Làm quen với biến cố** để giải quyết tình huống sau: Gieo một '
                 "con xúc xắc cân đối $6$ mặt. Xét biến cố $A$: 'Số chấm xuất hiện là số tự nhiên từ $1$ đến "
                 "$6$' và biến cố $B$: 'Số chấm xuất hiện là số chẵn'. Phân loại biến cố $A$ và $B$. Kết quả "
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        '- Biến cố $A$ là biến cố chắc chắn vì mặt nào của xúc xắc cũng có số chấm từ $1$ '
                        'đến $6$. - Biến cố $B$ là biến cố ngẫu nhiên vì có thể xảy ra (khi ra mặt...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 29: Làm quen với biến cố: - Biến cố $A$ là biến cố chắc '
                        'chắn vì mặt nào của xúc xắc cũng có số chấm từ $1$ đến $6$.\n'
                        '- Biến cố $B$ là biến cố ngẫu nhiên vì có thể xảy ra (khi ra mặt $2, 4, 6$) hoặc '
                        'không xảy ra (khi ra mặt $1, 3, 5$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Gieo một con xúc xắc $6$ mặt cân đối. Có bao nhiêu kết quả làm cho biến cố 'Số chấm xuất "
                 "hiện là ước của $6$' xảy ra?",
            'answer': ['4'],
            'unit': None,
            'solution': 'Các ước của $6$ từ $1$ đến $6$ là $\\{1; 2; 3; 6\\}$, vậy có $4$ kết quả.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch08-xac-suat',
  'context_title': 'Chương VIII: Làm quen với biến cố và xác suất của biến cố',
  'context': 'Chương VIII · SGK Toán 7: Làm quen với biến cố ngẫu nhiên, biến cố chắc chắn, biến cố không '
             'thể và xác suất của biến cố.',
  'title': 'Bài 30: Làm quen với xác suất của biến cố',
  'icon': '🎯',
  'description': 'Xác suất của biến cố chắc chắn, biến cố không thể và xác suất của các biến cố đồng khả '
                 'năng.',
  'requirements': ['Nhận biết được xác suất của một biến cố là một số từ $0$ đến $1$ đo lường khả năng xảy '
                   'ra của biến cố đó.',
                   'Tính được xác suất của biến cố chắc chắn, biến cố không thể và các biến cố đồng khả năng '
                   'trong trò chơi đơn giản.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Xác suất của biến cố không thể** ($P(A) = '
                   '0$) vào giải bài tập.'],
  'definition': 'Khả năng xảy ra của một biến cố được đo lường bởi một số nhận giá trị từ $0$ đến $1$, gọi '
                'là xác suất của biến cố đó. Biến cố không thể có xác suất bằng $0$; biến cố chắc chắn có '
                'xác suất bằng $1$.',
  'theory': '1. Xác suất của biến cố chắc chắn và biến cố không thể:\n'
            '- Xác suất của biến cố không thể bằng $0$.\n'
            '- Xác suất của biến cố chắc chắn bằng $1$.\n'
            '- Xác suất của biến cố càng gần $1$ thì biến cố đó càng có nhiều khả năng xảy ra.\n'
            '2. Biến cố đồng khả năng: Trong một trò chơi hay thí nghiệm, nếu có $n$ biến cố đồng khả năng '
            'và luôn xảy ra duy nhất một biến cố trong $n$ biến cố đó thì xác suất của mỗi biến cố đều bằng '
            '$\\dfrac{1}{n}$.',
  'formulas': [{'category': 'Công thức xác suất cơ bản',
                'items': [{'name': 'Xác suất của biến cố không thể', 'formula': '$P(A) = 0$'},
                          {'name': 'Xác suất của biến cố chắc chắn', 'formula': '$P(A) = 1$ (hay $100\\%$)'},
                          {'name': 'Xác suất của mỗi biến cố trong $n$ biến cố đồng khả năng',
                           'formula': '$P = \\dfrac{1}{n}$'}]}],
  'example': "Gieo một con xúc xắc $6$ mặt cân đối và đồng chất. Tính xác suất của biến cố $E$: 'Xuất hiện "
             "mặt $5$ chấm'.",
  'example_answer': 'Vì con xúc xắc cân đối và đồng chất nên $6$ biến cố xuất hiện mặt $1; 2; 3; 4; 5; 6$ '
                    'chấm là đồng khả năng.\n'
                    'Vậy xác suất của biến cố $E$ là $P(E) = \\dfrac{1}{6}$.',
  'real_life': 'Đánh giá cơ hội trúng thưởng khi bốc thăm ngẫu nhiên hoặc tung đồng xu để chọn sân trước '
               'trận đấu bóng đá ($50\\%$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Xác suất của một biến cố chắc chắn luôn bằng:',
            'options': ['$0$', '$1$', '$\\dfrac{1}{2}$', '$\\dfrac{1}{6}$'],
            'answer': 1,
            'solution': 'Biến cố chắc chắn luôn xảy ra nên có xác suất bằng $1$ (hay $100\\%$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Tung một đồng xu cân đối và đồng chất một lần. Xác suất của biến cố 'Đồng xu xuất hiện mặt "
                 "sấp' là:",
            'options': ['$1$', '$0$', '$\\dfrac{1}{2}$', '$\\dfrac{1}{4}$'],
            'answer': 2,
            'solution': 'Đồng xu cân đối có $2$ mặt sấp và ngửa đồng khả năng nên xác suất xuất hiện mặt sấp '
                        'là $\\dfrac{1}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 30: Làm quen với xác suất của biến cố**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Xác suất của biến cố không thể**?',
            'options': ['$P(A) = 1$ (hay $100\\%$)',
                        '$P = \\dfrac{1}{n}$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$P(A) = 0$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 30: Làm quen với xác suất của biến cố, **Xác '
                        'suất của biến cố không thể** được xác định bởi: $P(A) = 0$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Làm quen với xác suất của biến cố**, nội dung/biểu thức $P(A) = 1$ (hay '
                 '$100\\%$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Xác suất của biến cố chắc chắn',
                        'Xác suất của biến cố không thể',
                        'Xác suất của mỗi biến cố trong $n$ biến cố đồng khả năng',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 0,
            'solution': 'Trong Bài 30: Làm quen với xác suất của biến cố, biểu thức/quy tắc $P(A) = 1$ (hay '
                        '$100\\%$) chính là nội dung của **Xác suất của biến cố chắc chắn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hộp có $8$ quả bóng có cùng kích thước và khối lượng được đánh số từ $1$ đến $8$. Lấy '
                 "ngẫu nhiên $1$ quả bóng từ hộp. Xác suất của biến cố 'Lấy được quả bóng ghi số $5$' là:",
            'options': ['$\\dfrac{5}{8}$', '$\\dfrac{1}{8}$', '$\\dfrac{1}{5}$', '$1$'],
            'answer': 1,
            'solution': 'Có $8$ kết quả đồng khả năng từ $1$ đến $8$, nên xác suất lấy được quả bóng số $5$ '
                        'là $\\dfrac{1}{8}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Làm quen với xác suất của biến cố** (Chương VIII: Làm quen với biến cố '
                 'và xác suất của biến cố), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được xác suất của một biến cố là một số từ $0$ đến $1$ đo lường khả năng '
                        'xảy ra của biến cố đó.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 30: Làm quen với xác suất của biến cố: Nhận biết được '
                        'xác suất của một biến cố là một số từ $0$ đến $1$ đo lường khả năng xảy ra của biến '
                        'cố đó.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một vòng quay may mắn được chia thành $10$ hình quạt bằng nhau ghi các số từ $1$ đến $10$. '
                 'Quay vòng quay một lần. Xét các khẳng định sau:',
            'statements': ['Xác suất để kim chỉ vào ô số $10$ là $\\dfrac{1}{10} = 0,1$.',
                           "Xác suất của biến cố 'Kim chỉ vào ô ghi số $0$' bằng $0$.",
                           "Xác suất của biến cố 'Kim chỉ vào ô ghi số nhỏ hơn $11$' bằng $1$.",
                           'Khả năng kim chỉ vào ô số $9$ cao hơn khả năng kim chỉ vào ô số $1$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì 10 hình quạt bằng nhau nên khả năng kim chỉ vào ô số $9$ '
                        'và ô số $1$ là như nhau (đều bằng $\\dfrac{1}{10}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 30: Làm quen với xác '
                 'suất của biến cố**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được xác suất của một '
                           'biến cố là một số từ $0$ đến $1$ đo lường khả năng xảy ra của biến cố đó.',
                           'Quy tắc/công thức **Xác suất của biến cố không thể** trong bài được xác định '
                           'bởi: $P(A) = 0$.',
                           'Trong mọi trường hợp, **Xác suất của biến cố không thể** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 30: Làm quen với xác suất của biến cố.',
                           'Với bài toán minh họa: “Gieo một con xúc xắc $6$ mặt cân đối và đồng chất. Tính '
                           "xác suất của biến cố $E$: 'Xuất hiện mặt $5$ chấm'.”, lời giải đúng là: Vì con "
                           'xúc xắc cân đối và đồng chất nên $6$ biến cố xuất hiện mặt $1; 2; 3; 4; 5; 6$ '
                           'chấm là đồng khả năng. Vậy xác suất của biến cố $E$ là...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 30: Làm quen với xác suất của biến cố. b) '
                        '**Đúng** theo công thức trọng tâm **Xác suất của biến cố không thể** ($P(A) = 0$). '
                        'c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                        '\\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy '
                        'tắc chung của **Xác suất của biến cố không thể**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 30: Làm quen với xác suất của biến cố** để giải quyết tình huống '
                 'sau: Gieo một con xúc xắc $6$ mặt cân đối và đồng chất. Tính xác suất của biến cố $E$: '
                 "'Xuất hiện mặt $5$ chấm'. Kết quả và hướng giải nào dưới đây là **đúng**?",
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Vì con xúc xắc cân đối và đồng chất nên $6$ biến cố xuất hiện mặt $1; 2; 3; 4; 5; '
                        '6$ chấm là đồng khả năng. Vậy xác suất của biến cố $E$ là $P(E) = '
                        '\\dfrac{1}{6}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 30: Làm quen với xác suất của biến cố: Vì con xúc xắc '
                        'cân đối và đồng chất nên $6$ biến cố xuất hiện mặt $1; 2; 3; 4; 5; 6$ chấm là đồng '
                        'khả năng.\n'
                        'Vậy xác suất của biến cố $E$ là $P(E) = \\dfrac{1}{6}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong hộp có $20$ chiếc thẻ cùng loại được đánh số từ $1$ đến $20$. Rút ngẫu nhiên một '
                 "chiếc thẻ. Tính xác suất (viết dưới dạng số thập phân) của biến cố 'Rút được thẻ ghi số "
                 "$12$'.",
            'answer': ['0,05', '0.05'],
            'unit': None,
            'solution': 'Có $20$ kết quả đồng khả năng nên xác suất rút được thẻ số $12$ là $\\dfrac{1}{20} '
                        '= 0,05$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch09-quan-he-trong-tam-giac',
  'context_title': 'Chương IX: Quan hệ giữa các yếu tố trong một tam giác',
  'context': 'Chương IX · SGK Toán 7: Quan hệ giữa góc và cạnh đối diện, đường vuông góc và đường xiên, bất '
             'đẳng thức tam giác và các đường đồng quy trong tam giác.',
  'title': 'Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác',
  'icon': '📐',
  'description': 'Mối quan hệ giữa góc lớn hơn và cạnh đối diện lớn hơn trong cùng một tam giác.',
  'requirements': ['Nhận biết được góc đối diện với cạnh và cạnh đối diện với góc trong một tam giác.',
                   'Giải thích và vận dụng được định lí về quan hệ giữa góc và cạnh đối diện trong một tam '
                   'giác để so sánh các cạnh hoặc các góc.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **So sánh hai cạnh và hai góc** ($AC > AB '
                   '\\Leftrightarrow \\widehat{B} > \\widehat{C}$) vào giải bài tập.'],
  'definition': 'Trong một tam giác, góc đối diện với cạnh lớn hơn là góc lớn hơn; ngược lại, cạnh đối diện '
                'với góc lớn hơn là cạnh lớn hơn.',
  'theory': '1. Quan hệ giữa góc và cạnh đối diện trong $\\triangle ABC$:\n'
            '- Định lí 1: Nếu $AC > AB$ thì $\\widehat{B} > \\widehat{C}$.\n'
            '- Định lí 2: Nếu $\\widehat{B} > \\widehat{C}$ thì $AC > AB$.\n'
            '2. Hệ quả quan trọng:\n'
            '- Trong tam giác vuông, góc vuông là góc lớn nhất nên cạnh đối diện với góc vuông (cạnh huyền) '
            'là cạnh lớn nhất.\n'
            '- Trong tam giác tù, góc tù là góc lớn nhất nên cạnh đối diện với góc tù là cạnh lớn nhất.',
  'formulas': [{'category': 'Quan hệ góc và cạnh đối diện trong $\\triangle ABC$',
                'items': [{'name': 'So sánh hai cạnh và hai góc',
                           'formula': '$AC > AB \\Leftrightarrow \\widehat{B} > \\widehat{C}$'},
                          {'name': 'Thứ tự ba cạnh và ba góc',
                           'formula': '$BC > AC > AB \\Leftrightarrow \\widehat{A} > \\widehat{B} > '
                                      '\\widehat{C}$'},
                          {'name': 'Tam giác vuông tại $A$',
                           'formula': '$BC > AB$ và $BC > AC$ ($BC$ là cạnh huyền)'}]}],
  'example': 'Cho $\\triangle ABC$ có $AB = 4\\text{ cm}, BC = 7\\text{ cm}, AC = 5\\text{ cm}$. Hãy sắp xếp '
             'các góc $\\widehat{A}, \\widehat{B}, \\widehat{C}$ của tam giác theo thứ tự từ nhỏ đến lớn.',
  'example_answer': 'Trong $\\triangle ABC$, ta có $AB < AC < BC$ ($4 < 5 < 7$).\n'
                    'Các góc đối diện với $AB, AC, BC$ lần lượt là $\\widehat{C}, \\widehat{B}, '
                    '\\widehat{A}$.\n'
                    'Theo định lí quan hệ giữa góc và cạnh đối diện, ta có: $\\widehat{C} < \\widehat{B} < '
                    '\\widehat{A}$.',
  'real_life': 'Khi thiết kế cầu trượt hoặc mái dốc, đối diện với góc mở lớn hơn sẽ cần thanh giằng dài hơn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong $\\triangle ABC$, nếu $AB < AC$ thì khẳng định nào sau đây là đúng?',
            'options': ['$\\widehat{B} < \\widehat{C}$',
                        '$\\widehat{A} < \\widehat{B}$',
                        '$\\widehat{C} < \\widehat{B}$',
                        '$\\widehat{C} = \\widehat{B}$'],
            'answer': 2,
            'solution': 'Góc đối diện với cạnh $AB$ là $\\widehat{C}$, góc đối diện với cạnh $AC$ là '
                        '$\\widehat{B}$. Vì $AB < AC$ nên $\\widehat{C} < \\widehat{B}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một tam giác vuông, cạnh lớn nhất luôn là:',
            'options': ['Cạnh góc vuông ngắn hơn',
                        'Cạnh góc vuông dài hơn',
                        'Ba cạnh bằng nhau',
                        'Cạnh huyền'],
            'answer': 3,
            'solution': 'Trong tam giác vuông, góc vuông là góc lớn nhất nên cạnh huyền (đối diện góc vuông) '
                        'là cạnh lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam '
                 'giác**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **So sánh hai cạnh và hai góc**?',
            'options': ['$AC > AB \\Leftrightarrow \\widehat{B} > \\widehat{C}$',
                        '$BC > AC > AB \\Leftrightarrow \\widehat{A} > \\widehat{B} > \\widehat{C}$',
                        '$BC > AB$ và $BC > AC$ ($BC$ là cạnh huyền)',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 31: Quan hệ giữa góc và cạnh đối diện trong '
                        'một tam giác, **So sánh hai cạnh và hai góc** được xác định bởi: $AC > AB '
                        '\\Leftrightarrow \\widehat{B} > \\widehat{C}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác**, nội dung/biểu thức '
                 '$BC > AC > AB \\Leftrightarrow \\widehat{A} > \\widehat{B} > \\widehat{C}$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['So sánh hai cạnh và hai góc',
                        'Thứ tự ba cạnh và ba góc',
                        'Tam giác vuông tại $A$',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 1,
            'solution': 'Trong Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác, biểu thức/quy '
                        'tắc $BC > AC > AB \\Leftrightarrow \\widehat{A} > \\widehat{B} > \\widehat{C}$ '
                        'chính là nội dung của **Thứ tự ba cạnh và ba góc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle MNP$ có $\\widehat{M} = 50^\\circ, \\widehat{N} = 70^\\circ$. Cạnh lớn '
                 'nhất của $\\triangle MNP$ là:',
            'options': ['$MN$', '$NP$', '$MP$', 'Không xác định được'],
            'answer': 2,
            'solution': 'Ta có $\\widehat{P} = 180^\\circ - (50^\\circ + 70^\\circ) = 60^\\circ$. Vì '
                        '$\\widehat{N} = 70^\\circ$ là góc lớn nhất nên cạnh đối diện $MP$ là cạnh lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác** (Chương IX: Quan '
                 'hệ giữa các yếu tố trong một tam giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu '
                 'cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Nhận biết được góc đối diện với cạnh và cạnh đối diện với góc trong một tam giác.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam '
                        'giác: Nhận biết được góc đối diện với cạnh và cạnh đối diện với góc trong một tam '
                        'giác.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có $AB = 5\\text{ cm}, AC = 8\\text{ cm}, BC = 10\\text{ cm}$. Xét '
                 'các khẳng định sau:',
            'statements': ['Góc đối diện với cạnh $BC$ là góc $\\widehat{A}$.',
                           'Trong $\\triangle ABC$, góc $\\widehat{A}$ là góc lớn nhất.',
                           'Góc $\\widehat{B}$ nhỏ hơn góc $\\widehat{C}$.',
                           'Thứ tự các góc tăng dần là $\\widehat{C} < \\widehat{B} < \\widehat{A}$.'],
            'answer': [True, True, False, True],
            'solution': 'a), b), d) Đúng vì $AB < AC < BC \\Rightarrow \\widehat{C} < \\widehat{B} < '
                        '\\widehat{A}$. c) Sai vì $\\widehat{B} > \\widehat{C}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 31: Quan hệ giữa góc và '
                 'cạnh đối diện trong một tam giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được góc đối diện với '
                           'cạnh và cạnh đối diện với góc trong một tam giác.',
                           'Quy tắc/công thức **So sánh hai cạnh và hai góc** trong bài được xác định bởi: '
                           '$AC > AB \\Leftrightarrow \\widehat{B} > \\widehat{C}$.',
                           'Trong mọi trường hợp, **So sánh hai cạnh và hai góc** luôn được tính bằng công '
                           'thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ có $AB = 4\\text{ cm}, BC = '
                           '7\\text{ cm}, AC = 5\\text{ cm}$. Hãy sắp xếp các góc $\\widehat{A}, '
                           '\\widehat{B}, \\widehat{C}$ c...”, lời giải đúng là: Trong $\\triangle ABC$, ta '
                           'có $AB < AC < BC$ ($4 < 5 < 7$). Các góc đối diện với $AB, AC, BC$ lần lượt là '
                           '$\\widehat{C}, \\widehat{B}, \\widehat{A}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 31: Quan hệ giữa góc và cạnh đối diện '
                        'trong một tam giác. b) **Đúng** theo công thức trọng tâm **So sánh hai cạnh và hai '
                        'góc** ($AC > AB \\Leftrightarrow \\widehat{B} > \\widehat{C}$). c) **Sai** vì '
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của '
                        '**So sánh hai cạnh và hai góc**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác** để '
                 'giải quyết tình huống sau: Cho $\\triangle ABC$ có $AB = 4\\text{ cm}, BC = 7\\text{ cm}, '
                 'AC = 5\\text{ cm}$. Hãy sắp xếp các góc $\\widehat{A}, \\widehat{B}, \\widehat{C}$ của tam '
                 'giác theo thứ tự từ nhỏ đến lớn. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong $\\triangle ABC$, ta có $AB < AC < BC$ ($4 < 5 < 7$). Các góc đối diện với '
                        '$AB, AC, BC$ lần lượt là $\\widehat{C}, \\widehat{B}, \\widehat{A}$. Theo định...',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam '
                        'giác: Trong $\\triangle ABC$, ta có $AB < AC < BC$ ($4 < 5 < 7$).\n'
                        'Các góc đối diện với $AB, AC, BC$ lần lượt là $\\widehat{C}, \\widehat{B}, '
                        '\\widehat{A}$.\n'
                        'Theo định lí quan hệ giữa góc và cạnh đối diện, ta có: $\\widehat{C} < \\widehat{B} '
                        '< \\widehat{A}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$ có cạnh góc vuông $AB = 6\\text{ cm}, AC = 8\\text{ '
                 'cm}$ và cạnh huyền $BC = 10\\text{ cm}$. Độ dài cạnh đối diện với góc lớn nhất của '
                 '$\\triangle ABC$ bằng bao nhiêu $\\text{cm}$?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Góc lớn nhất là góc vuông $\\widehat{A} = 90^\\circ$, cạnh đối diện với '
                        '$\\widehat{A}$ là cạnh huyền $BC = 10\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch09-quan-he-trong-tam-giac',
  'context_title': 'Chương IX: Quan hệ giữa các yếu tố trong một tam giác',
  'context': 'Chương IX · SGK Toán 7: Quan hệ giữa góc và cạnh đối diện, đường vuông góc và đường xiên, bất '
             'đẳng thức tam giác và các đường đồng quy trong tam giác.',
  'title': 'Bài 32: Quan hệ giữa đường vuông góc và đường xiên',
  'icon': '📏',
  'description': 'Khái niệm đường vuông góc, đường xiên kẻ từ một điểm đến một đường thẳng và tính chất '
                 'đường vuông góc là ngắn nhất.',
  'requirements': ['Nhận biết được đường vuông góc và đường xiên kẻ từ một điểm nằm ngoài đường thẳng đến '
                   'đường thẳng đó.',
                   'Giải thích và vận dụng được định lí: Trong các đường xiên và đường vuông góc kẻ từ một '
                   'điểm ở ngoài một đường thẳng đến đường thẳng đó, đường vuông góc là đường ngắn nhất.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **So sánh đường vuông góc và đường xiên** '
                   '($AH \\perp d$ tại $H$, $M \\in d$ ($M \\neq H$) $\\Rightarrow AH < AM$) vào giải bài '
                   'tập.'],
  'definition': 'Từ một điểm $A$ không nằm trên đường thẳng $d$, kẻ đường thẳng vuông góc với $d$ tại $H$: '
                'đoạn thẳng $AH$ gọi là đoạn vuông góc (hay đường vuông góc), $H$ là chân đường vuông góc, '
                'độ dài $AH$ là khoảng cách từ $A$ đến $d$. Với điểm $M \\in d$ ($M \\neq H$), đoạn $AM$ gọi '
                'là đường xiên.',
  'theory': 'Định lí: Trong các đường xiên và đường vuông góc kẻ từ một điểm nằm ngoài một đường thẳng đến '
            'đường thẳng đó, đường vuông góc là đường ngắn nhất.\n'
            'Chứng minh: Trong tam giác vuông $\\triangle AHM$ (vuông tại $H$), $AM$ là cạnh huyền còn $AH$ '
            'là cạnh góc vuông nên $AH < AM$.',
  'formulas': [{'category': 'Quan hệ đường vuông góc và đường xiên',
                'items': [{'name': 'So sánh đường vuông góc và đường xiên',
                           'formula': '$AH \\perp d$ tại $H$, $M \\in d$ ($M \\neq H$) $\\Rightarrow AH < '
                                      'AM$'},
                          {'name': 'Khoảng cách từ điểm $A$ đến đường thẳng $d$',
                           'formula': '$d(A, d) = AH$ (với $AH \\perp d$ tại $H$)'}]}],
  'example': 'Từ điểm $A$ trên bờ hồ cách mép đường thẳng $d$ một khoảng $AH = 15\\text{ m}$ ($AH \\perp '
             'd$), người ta bắc một cây cầu đi bộ từ $A$ đến một điểm $M$ trên đường $d$. Hỏi chiều dài cây '
             'cầu ngắn nhất là bao nhiêu mét?',
  'example_answer': 'Trong các đoạn thẳng nối từ $A$ đến đường thẳng $d$, đoạn vuông góc $AH$ là ngắn nhất.\n'
                    'Vậy cây cầu ngắn nhất khi bắc tại chân đường vuông góc $H$ và có chiều dài bằng '
                    '$15\\text{ m}$.',
  'real_life': 'Khi bơi từ một vị trí trong hồ bơi vào thành bể thẳng, bơi vuông góc với thành bể là quãng '
               'đường ngắn nhất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các đường xiên và đường vuông góc kẻ từ một điểm ở ngoài một đường thẳng đến đường '
                 'thẳng đó thì:',
            'options': ['Đường vuông góc là đường dài nhất',
                        'Đường vuông góc bằng mọi đường xiên',
                        'Đường xiên luôn ngắn hơn đường vuông góc',
                        'Đường vuông góc là đường ngắn nhất'],
            'answer': 3,
            'solution': 'Theo định lí, đường vuông góc luôn ngắn hơn mọi đường xiên kẻ từ cùng điểm đó đến '
                        'đường thẳng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho điểm $A$ nằm ngoài đường thẳng $d$, kẻ $AH \\perp d$ tại $H$ và lấy điểm $B \\in d$ '
                 '($B \\neq H$). Kết luận nào sau đây đúng?',
            'options': ['$AH < AB$', '$AH > AB$', '$AH = AB$', '$AB < BH$'],
            'answer': 0,
            'solution': '$AH$ là đường vuông góc còn $AB$ là đường xiên nên $AH < AB$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 32: Quan hệ giữa đường vuông góc và đường xiên**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **So sánh đường vuông góc và đường xiên**?',
            'options': ['$d(A, d) = AH$ (với $AH \\perp d$ tại $H$)',
                        '$AH \\perp d$ tại $H$, $M \\in d$ ($M \\neq H$) $\\Rightarrow AH < AM$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 32: Quan hệ giữa đường vuông góc và đường '
                        'xiên, **So sánh đường vuông góc và đường xiên** được xác định bởi: $AH \\perp d$ '
                        'tại $H$, $M \\in d$ ($M \\neq H$) $\\Rightarrow AH < AM$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Quan hệ giữa đường vuông góc và đường xiên**, nội dung/biểu thức $d(A, d) '
                 '= AH$ (với $AH \\perp d$ tại $H$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['So sánh đường vuông góc và đường xiên',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Khoảng cách từ điểm $A$ đến đường thẳng $d$',
                        'Quan hệ tập hợp'],
            'answer': 2,
            'solution': 'Trong Bài 32: Quan hệ giữa đường vuông góc và đường xiên, biểu thức/quy tắc $d(A, '
                        'd) = AH$ (với $AH \\perp d$ tại $H$) chính là nội dung của **Khoảng cách từ điểm '
                        '$A$ đến đường thẳng $d$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$, điểm $M$ nằm trên cạnh $AC$ ($M$ khác $A$ và $C$). So '
                 'sánh độ dài $BM$ và $BC$:',
            'options': ['$BC < BM < AB$', '$BM > BC$', '$BM = AB$', '$AB < BM < BC$'],
            'answer': 3,
            'solution': 'Kẻ từ $B$ đến đường thẳng $AC$: $BA$ là đường vuông góc nên $AB < BM$. Trong '
                        '$\\triangle BMC$, góc $\\widehat{BMC}$ là góc ngoài của $\\triangle ABM$ vuông tại '
                        '$A$ nên $\\widehat{BMC} > 90^\\circ$, suy ra $BM < BC$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Quan hệ giữa đường vuông góc và đường xiên** (Chương IX: Quan hệ giữa '
                 'các yếu tố trong một tam giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt '
                 'và bản chất kiến thức của bài?',
            'options': ['Nhận biết được đường vuông góc và đường xiên kẻ từ một điểm nằm ngoài đường thẳng '
                        'đến đường thẳng đó.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 32: Quan hệ giữa đường vuông góc và đường xiên: Nhận '
                        'biết được đường vuông góc và đường xiên kẻ từ một điểm nằm ngoài đường thẳng đến '
                        'đường thẳng đó.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Từ điểm $P$ nằm ngoài đường thẳng $d$, kẻ $PH \\perp d$ tại $H$ biết $PH = 8\\text{ cm}$. '
                 'Lấy điểm $Q$ bất kì trên đường thẳng $d$ ($Q \\neq H$). Xét các khẳng định sau:',
            'statements': ['Đoạn thẳng $PH$ là đường vuông góc, đoạn thẳng $PQ$ là đường xiên.',
                           'Khoảng cách từ điểm $P$ đến đường thẳng $d$ bằng $8\\text{ cm}$.',
                           'Độ dài đoạn thẳng $PQ$ luôn lớn hơn $8\\text{ cm}$.',
                           'Có thể tìm được một điểm $Q$ trên $d$ sao cho $PQ = 6\\text{ cm}$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì mọi điểm $Q \\in d$ đều có $PQ \\ge PH = 8\\text{ cm}$, '
                        'không thể bằng $6\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 32: Quan hệ giữa đường '
                 'vuông góc và đường xiên**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được đường vuông góc và '
                           'đường xiên kẻ từ một điểm nằm ngoài đường thẳng đến đường thẳng đó.',
                           'Quy tắc/công thức **So sánh đường vuông góc và đường xiên** trong bài được xác '
                           'định bởi: $AH \\perp d$ tại $H$, $M \\in d$ ($M \\neq H$) $\\Rightarrow AH < '
                           'AM$.',
                           'Trong mọi trường hợp, **So sánh đường vuông góc và đường xiên** luôn được tính '
                           'bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 32: Quan hệ giữa đường vuông góc và đường xiên.',
                           'Với bài toán minh họa: “Từ điểm $A$ trên bờ hồ cách mép đường thẳng $d$ một '
                           'khoảng $AH = 15\\text{ m}$ ($AH \\perp d$), người ta bắc một cây cầu đi bộ từ '
                           '$A$ đến một...”, lời giải đúng là: Trong các đoạn thẳng nối từ $A$ đến đường '
                           'thẳng $d$, đoạn vuông góc $AH$ là ngắn nhất. Vậy cây cầu ngắn nhất khi bắc tại '
                           'chân đường vuông gó...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 32: Quan hệ giữa đường vuông góc và đường '
                        'xiên. b) **Đúng** theo công thức trọng tâm **So sánh đường vuông góc và đường '
                        'xiên** ($AH \\perp d$ tại $H$, $M \\in d$ ($M \\neq H$) $\\Rightarrow AH < AM$). c) '
                        '**Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                        '\\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy '
                        'tắc chung của **So sánh đường vuông góc và đường xiên**. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 32: Quan hệ giữa đường vuông góc và đường xiên** để giải quyết '
                 'tình huống sau: Từ điểm $A$ trên bờ hồ cách mép đường thẳng $d$ một khoảng $AH = 15\\text{ '
                 'm}$ ($AH \\perp d$), người ta bắc một cây cầu đi bộ từ $A$ đến một điểm $M$ trên đường '
                 '$d$. Hỏi chiều dài cây cầu ngắn nhất là bao nhiêu mét? Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Trong các đoạn thẳng nối từ $A$ đến đường thẳng $d$, đoạn vuông góc $AH$ là ngắn '
                        'nhất. Vậy cây cầu ngắn nhất khi bắc tại chân đường vuông góc $H$ và có chi...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 32: Quan hệ giữa đường vuông góc và đường xiên: Trong '
                        'các đoạn thẳng nối từ $A$ đến đường thẳng $d$, đoạn vuông góc $AH$ là ngắn nhất.\n'
                        'Vậy cây cầu ngắn nhất khi bắc tại chân đường vuông góc $H$ và có chiều dài bằng '
                        '$15\\text{ m}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Ngôi nhà tại điểm $A$ cách đường quốc lộ thẳng $d$ một khoảng vuông góc $AH = 25\\text{ '
                 'm}$. Người ta muốn làm một lối đi thẳng từ $A$ ra đường quốc lộ $d$. Hỏi chiều dài tối '
                 'thiểu của lối đi đó là bao nhiêu mét?',
            'answer': ['25'],
            'unit': None,
            'solution': 'Chiều dài tối thiểu chính là độ dài đường vuông góc $AH = 25\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch09-quan-he-trong-tam-giac',
  'context_title': 'Chương IX: Quan hệ giữa các yếu tố trong một tam giác',
  'context': 'Chương IX · SGK Toán 7: Quan hệ giữa góc và cạnh đối diện, đường vuông góc và đường xiên, bất '
             'đẳng thức tam giác và các đường đồng quy trong tam giác.',
  'title': 'Bài 33: Quan hệ giữa ba cạnh của một tam giác',
  'icon': '🔺',
  'description': 'Bất đẳng thức tam giác và điều kiện để ba đoạn thẳng lập thành ba cạnh của một tam giác.',
  'requirements': ['Giải thích được định lí về bất đẳng thức tam giác (tổng độ dài hai cạnh bất kì lớn hơn '
                   'độ dài cạnh còn lại).',
                   'Vận dụng được bất đẳng thức tam giác để kiểm tra ba độ dài có tạo thành một tam giác hay '
                   'không và tìm khoảng giá trị của cạnh thứ ba.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Tổng hai cạnh lớn hơn cạnh thứ ba** ($AB + '
                   'AC > BC; \\quad AB + BC > AC; \\quad AC + BC > AB$) vào giải bài tập.'],
  'definition': 'Trong một tam giác, độ dài của một cạnh bất kì luôn nhỏ hơn tổng độ dài hai cạnh còn lại và '
                'lớn hơn hiệu độ dài hai cạnh đó.',
  'theory': '1. Bất đẳng thức tam giác: Trong $\\triangle ABC$, với ba cạnh $a, b, c$, ta luôn có:\n'
            '$|b - c| < a < b + c$.\n'
            '2. Kiểm tra bộ ba độ dài có là ba cạnh của một tam giác: Để kiểm tra nhanh ba độ dài dương $a, '
            'b, c$ có tạo thành một tam giác hay không, ta chỉ cần so sánh độ dài lớn nhất với tổng của hai '
            'độ dài còn lại. Nếu độ dài lớn nhất nhỏ hơn tổng hai độ dài kia thì ba đoạn thẳng đó lập thành '
            'một tam giác.',
  'formulas': [{'category': 'Bất đẳng thức tam giác',
                'items': [{'name': 'Tổng hai cạnh lớn hơn cạnh thứ ba',
                           'formula': '$AB + AC > BC; \\quad AB + BC > AC; \\quad AC + BC > AB$'},
                          {'name': 'Hệ quả kẹp độ dài một cạnh', 'formula': '$|AB - AC| < BC < AB + AC$'}]}],
  'example': 'Cho $\\triangle ABC$ có $AB = 3\\text{ cm}, AC = 7\\text{ cm}$. Tìm độ dài cạnh $BC$ biết độ '
             'dài $BC$ (tính theo $\\text{cm}$) là một số nguyên và $\\triangle ABC$ là tam giác cân.',
  'example_answer': 'Theo bất đẳng thức tam giác: $7 - 3 < BC < 7 + 3 \\Leftrightarrow 4 < BC < 10$.\n'
                    'Vì $\\triangle ABC$ cân nên $BC = AB = 3\\text{ cm}$ hoặc $BC = AC = 7\\text{ cm}$.\n'
                    'So với điều kiện $4 < BC < 10$, chỉ có $BC = 7\\text{ cm}$ thỏa mãn.',
  'real_life': 'Xác định khoảng cách phủ sóng tối đa và tối thiểu giữa hai trạm thu phát sóng qua một trạm '
               'trung chuyển thứ ba.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bộ ba độ dài nào sau đây có thể là độ dài ba cạnh của một tam giác?',
            'options': ['$3\\text{ cm}; 4\\text{ cm}; 5\\text{ cm}$',
                        '$2\\text{ cm}; 3\\text{ cm}; 5\\text{ cm}$',
                        '$1\\text{ cm}; 2\\text{ cm}; 4\\text{ cm}$',
                        '$3\\text{ cm}; 3\\text{ cm}; 7\\text{ cm}$'],
            'answer': 0,
            'solution': 'Vì $3 + 4 = 7 > 5$ nên bộ ba $3\\text{ cm}; 4\\text{ cm}; 5\\text{ cm}$ thỏa mãn '
                        'bất đẳng thức tam giác.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong $\\triangle ABC$ bất kì, khẳng định nào sau đây luôn đúng?',
            'options': ['$AB + BC = AC$', '$AB + BC > AC$', '$AB + BC < AC$', '$AB - BC > AC$'],
            'answer': 1,
            'solution': 'Theo bất đẳng thức tam giác, tổng độ dài hai cạnh bất kì luôn lớn hơn độ dài cạnh '
                        'còn lại: $AB + BC > AC$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 33: Quan hệ giữa ba cạnh của một tam giác**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Tổng hai cạnh lớn hơn cạnh thứ ba**?',
            'options': ['$|AB - AC| < BC < AB + AC$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$AB + AC > BC; \\quad AB + BC > AC; \\quad AC + BC > AB$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 33: Quan hệ giữa ba cạnh của một tam giác, '
                        '**Tổng hai cạnh lớn hơn cạnh thứ ba** được xác định bởi: $AB + AC > BC; \\quad AB + '
                        'BC > AC; \\quad AC + BC > AB$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 33: Quan hệ giữa ba cạnh của một tam giác**, nội dung/biểu thức $|AB - AC| < '
                 'BC < AB + AC$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tổng hai cạnh lớn hơn cạnh thứ ba',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp',
                        'Hệ quả kẹp độ dài một cạnh'],
            'answer': 3,
            'solution': 'Trong Bài 33: Quan hệ giữa ba cạnh của một tam giác, biểu thức/quy tắc $|AB - AC| < '
                        'BC < AB + AC$ chính là nội dung của **Hệ quả kẹp độ dài một cạnh**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một tam giác cân có hai cạnh bằng $3\\text{ cm}$ và $7\\text{ cm}$. Độ dài cạnh còn lại '
                 'của tam giác cân đó là:',
            'options': ['$7\\text{ cm}$', '$3\\text{ cm}$', '$4\\text{ cm}$', '$10\\text{ cm}$'],
            'answer': 0,
            'solution': 'Nếu cạnh còn lại là $3\\text{ cm}$ thì $3 + 3 = 6 < 7$ (không thỏa mãn bất đẳng '
                        'thức tam giác). Vậy cạnh còn lại phải là $7\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 33: Quan hệ giữa ba cạnh của một tam giác** (Chương IX: Quan hệ giữa các yếu '
                 'tố trong một tam giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Giải thích được định lí về bất đẳng thức tam giác (tổng độ dài hai cạnh bất kì lớn '
                        'hơn độ dài cạnh còn lại).',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 33: Quan hệ giữa ba cạnh của một tam giác: Giải thích '
                        'được định lí về bất đẳng thức tam giác (tổng độ dài hai cạnh bất kì lớn hơn độ dài '
                        'cạnh còn lại).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có $AB = 2\\text{ cm}$ và $BC = 6\\text{ cm}$. Xét các khẳng định '
                 'sau:',
            'statements': ['Độ dài cạnh $AC$ luôn thỏa mãn $4\\text{ cm} < AC < 8\\text{ cm}$.',
                           'Cạnh $AC$ có thể nhận độ dài bằng $4\\text{ cm}$.',
                           'Nếu độ dài $AC$ là một số nguyên (theo $\\text{cm}$) thì $AC \\in \\{5; 6; '
                           '7\\}$.',
                           'Chu vi của $\\triangle ABC$ luôn lớn hơn $12\\text{ cm}$.'],
            'answer': [True, False, True, True],
            'solution': 'a), c) Đúng vì $6 - 2 < AC < 6 + 2 \\Leftrightarrow 4 < AC < 8$. b) Sai vì $AC > '
                        '4$. d) Đúng vì chu vi là $AB + BC + AC = 8 + AC > 8 + 4 = 12\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 33: Quan hệ giữa ba '
                 'cạnh của một tam giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Giải thích được định lí về bất '
                           'đẳng thức tam giác (tổng độ dài hai cạnh bất kì lớn hơn độ dài cạnh còn lại).',
                           'Quy tắc/công thức **Tổng hai cạnh lớn hơn cạnh thứ ba** trong bài được xác định '
                           'bởi: $AB + AC > BC; \\quad AB + BC > AC; \\quad AC + BC > AB$.',
                           'Trong mọi trường hợp, **Tổng hai cạnh lớn hơn cạnh thứ ba** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 33: Quan hệ giữa ba cạnh của một tam giác.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ có $AB = 3\\text{ cm}, AC = '
                           '7\\text{ cm}$. Tìm độ dài cạnh $BC$ biết độ dài $BC$ (tính theo $\\text{cm}$) là '
                           'một số nguyên...”, lời giải đúng là: Theo bất đẳng thức tam giác: $7 - 3 < BC < '
                           '7 + 3 \\Leftrightarrow 4 < BC < 10$. Vì $\\triangle ABC$ cân nên $BC = AB = '
                           '3\\text{ cm}$ hoặc $BC = AC = 7\\text{ cm}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 33: Quan hệ giữa ba cạnh của một tam giác. '
                        'b) **Đúng** theo công thức trọng tâm **Tổng hai cạnh lớn hơn cạnh thứ ba** ($AB + '
                        'AC > BC; \\quad AB + BC > AC; \\quad AC + BC > AB$). c) **Sai** vì $\\mathbb{Q} = '
                        '\\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 '
                        '\\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của **Tổng hai '
                        'cạnh lớn hơn cạnh thứ ba**. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 33: Quan hệ giữa ba cạnh của một tam giác** để giải quyết tình '
                 'huống sau: Cho $\\triangle ABC$ có $AB = 3\\text{ cm}, AC = 7\\text{ cm}$. Tìm độ dài cạnh '
                 '$BC$ biết độ dài $BC$ (tính theo $\\text{cm}$) là một số nguyên và $\\triangle ABC$ là tam '
                 'giác cân. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Theo bất đẳng thức tam giác: $7 - 3 < BC < 7 + 3 \\Leftrightarrow 4 < BC < 10$. Vì '
                        '$\\triangle ABC$ cân nên $BC = AB = 3\\text{ cm}$ hoặc $BC = AC = 7\\text{ cm}$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 33: Quan hệ giữa ba cạnh của một tam giác: Theo bất đẳng '
                        'thức tam giác: $7 - 3 < BC < 7 + 3 \\Leftrightarrow 4 < BC < 10$.\n'
                        'Vì $\\triangle ABC$ cân nên $BC = AB = 3\\text{ cm}$ hoặc $BC = AC = 7\\text{ '
                        'cm}$.\n'
                        'So với điều kiện $4 < BC < 10$, chỉ có $BC = 7\\text{ cm}$ thỏa mãn.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tam giác cân có độ dài hai cạnh là $4\\text{ cm}$ và $9\\text{ cm}$. Tính chu vi của '
                 'tam giác cân đó (đơn vị $\\text{cm}$).',
            'answer': ['22'],
            'unit': None,
            'solution': 'Vì $4 + 4 = 8 < 9$ nên cạnh bên của tam giác cân phải là $9\\text{ cm}$ và cạnh đáy '
                        'là $4\\text{ cm}$. Chu vi là $9 + 9 + 4 = 22\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch09-quan-he-trong-tam-giac',
  'context_title': 'Chương IX: Quan hệ giữa các yếu tố trong một tam giác',
  'context': 'Chương IX · SGK Toán 7: Quan hệ giữa góc và cạnh đối diện, đường vuông góc và đường xiên, bất '
             'đẳng thức tam giác và các đường đồng quy trong tam giác.',
  'title': 'Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác trong một tam giác',
  'icon': '🎯',
  'description': 'Tính chất ba đường trung tuyến (trọng tâm của tam giác) và ba đường phân giác trong một '
                 'tam giác.',
  'requirements': ['Nhận biết được đường trung tuyến, trọng tâm và tính chất trọng tâm của tam giác.',
                   'Nhận biết được sự đồng quy của ba đường phân giác trong một tam giác và tính chất điểm '
                   'đồng quy cách đều ba cạnh.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hệ thức trọng tâm $G$ trên trung tuyến '
                   '$AM$** ($AG = \\dfrac{2}{3}AM; \\quad GM = \\dfrac{1}{3}AM; \\quad AG = 2GM$) vào giải '
                   'bài tập.'],
  'definition': 'Đường trung tuyến của tam giác là đoạn thẳng nối một đỉnh với trung điểm của cạnh đối diện. '
                'Ba đường trung tuyến của một tam giác cùng đi qua một điểm gọi là trọng tâm. Ba đường phân '
                'giác của một tam giác cùng đi qua một điểm và điểm đó cách đều ba cạnh của tam giác.',
  'theory': '1. Sự đồng quy của ba đường trung tuyến:\n'
            '- Ba đường trung tuyến của $\\triangle ABC$ cùng đi qua một điểm $G$ (gọi là trọng tâm của tam '
            'giác).\n'
            '- Tính chất trọng tâm: Trọng tâm $G$ cách mỗi đỉnh một khoảng bằng $\\dfrac{2}{3}$ độ dài đường '
            'trung tuyến đi qua đỉnh ấy. Với trung tuyến $AM$, ta có $\\dfrac{AG}{AM} = \\dfrac{2}{3}$; $GM '
            '= \\dfrac{1}{3}AM$; $AG = 2GM$.\n'
            '2. Sự đồng quy của ba đường phân giác:\n'
            '- Ba đường phân giác của một tam giác đồng quy tại một điểm $I$.\n'
            '- Điểm $I$ cách đều ba cạnh của tam giác đó.',
  'formulas': [{'category': 'Tính chất trọng tâm và giao điểm ba đường phân giác',
                'items': [{'name': 'Hệ thức trọng tâm $G$ trên trung tuyến $AM$',
                           'formula': '$AG = \\dfrac{2}{3}AM; \\quad GM = \\dfrac{1}{3}AM; \\quad AG = 2GM$'},
                          {'name': 'Giao điểm $I$ của ba đường phân giác',
                           'formula': 'Khoảng cách từ $I$ đến ba cạnh $AB, BC, CA$ bằng nhau ($IH = IK = '
                                      'IL$)'}]}],
  'example': 'Cho $\\triangle ABC$ có đường trung tuyến $AM = 12\\text{ cm}$ và trọng tâm $G$. Tính độ dài '
             'các đoạn thẳng $AG$ và $GM$.',
  'example_answer': 'Vì $G$ là trọng tâm của $\\triangle ABC$ nên:\n'
                    '- $AG = \\dfrac{2}{3}AM = \\dfrac{2}{3} \\cdot 12 = 8\\text{ (cm)}$;\n'
                    '- $GM = \\dfrac{1}{3}AM = \\dfrac{1}{3} \\cdot 12 = 4\\text{ (cm)}$.',
  'real_life': 'Xác định tâm thăng bằng (trọng tâm) của một tấm bìa hoặc mặt bàn hình tam giác bằng cách tìm '
               'giao điểm của các đường trung tuyến.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giao điểm của ba đường trung tuyến trong một tam giác được gọi là:',
            'options': ['Trực tâm của tam giác',
                        'Trọng tâm của tam giác',
                        'Tâm đường tròn ngoại tiếp',
                        'Chân đường cao'],
            'answer': 1,
            'solution': 'Giao điểm của ba đường trung tuyến trong một tam giác được gọi là trọng tâm của tam '
                        'giác đó.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giao điểm của ba đường phân giác trong một tam giác có tính chất nào sau đây?',
            'options': ['Cách đều ba đỉnh của tam giác',
                        'Luôn nằm ngoài tam giác',
                        'Cách đều ba cạnh của tam giác',
                        'Chia mỗi đường phân giác theo tỉ số $\\dfrac{2}{3}$'],
            'answer': 2,
            'solution': 'Giao điểm của ba đường phân giác trong tam giác cách đều ba cạnh của tam giác đó.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân '
                 'giác trong một tam giác**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hệ thức '
                 'trọng tâm $G$ trên trung tuyến $AM$**?',
            'options': ['Khoảng cách từ $I$ đến ba cạnh $AB, BC, CA$ bằng nhau ($IH = IK = IL$)',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$',
                        '$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q}$',
                        '$AG = \\dfrac{2}{3}AM; \\quad GM = \\dfrac{1}{3}AM; \\quad AG = 2GM$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 34: Sự đồng quy của ba đường trung tuyến, ba '
                        'đường phân giác trong một tam giác, **Hệ thức trọng tâm $G$ trên trung tuyến $AM$** '
                        'được xác định bởi: $AG = \\dfrac{2}{3}AM; \\quad GM = \\dfrac{1}{3}AM; \\quad AG = '
                        '2GM$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác trong một tam '
                 'giác**, nội dung/biểu thức Khoảng cách từ $I$ đến ba cạnh $AB, BC, CA$ bằng nhau ($IH = IK '
                 '= IL$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Giao điểm $I$ của ba đường phân giác',
                        'Hệ thức trọng tâm $G$ trên trung tuyến $AM$',
                        'Định nghĩa tập $\\mathbb{Q}$',
                        'Quan hệ tập hợp'],
            'answer': 0,
            'solution': 'Trong Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác trong một '
                        'tam giác, biểu thức/quy tắc Khoảng cách từ $I$ đến ba cạnh $AB, BC, CA$ bằng nhau '
                        '($IH = IK = IL$) chính là nội dung của **Giao điểm $I$ của ba đường phân giác**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có trung tuyến $AM = 9\\text{ cm}$ và trọng tâm $G$. Độ dài đoạn '
                 'thẳng $AG$ bằng:',
            'options': ['$3\\text{ cm}$', '$6\\text{ cm}$', '$4,5\\text{ cm}$', '$12\\text{ cm}$'],
            'answer': 1,
            'solution': 'Theo tính chất trọng tâm: $AG = \\dfrac{2}{3}AM = \\dfrac{2}{3} \\cdot 9 = 6\\text{ '
                        '(cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác trong một tam '
                 'giác** (Chương IX: Quan hệ giữa các yếu tố trong một tam giác), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được đường trung tuyến, trọng tâm và tính chất trọng tâm của tam giác.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường '
                        'phân giác trong một tam giác: Nhận biết được đường trung tuyến, trọng tâm và tính '
                        'chất trọng tâm của tam giác.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có hai đường trung tuyến $BM$ và $CN$ cắt nhau tại $G$. Xét các khẳng '
                 'định sau:',
            'statements': ['Điểm $G$ là trọng tâm của $\\triangle ABC$.',
                           'Đường thẳng $AG$ đi qua trung điểm của cạnh $BC$.',
                           'Ta có tỉ số $\\dfrac{BG}{BM} = \\dfrac{2}{3}$ và $BG = 2GM$.',
                           'Điểm $G$ luôn cách đều ba cạnh của $\\triangle ABC$ với mọi tam giác bất kì.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng theo tính chất ba đường trung tuyến. d) Sai vì điểm cách đều ba '
                        'cạnh là giao điểm của ba đường phân giác (chỉ trùng với $G$ khi tam giác đều).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 34: Sự đồng quy của ba '
                 'đường trung tuyến, ba đường phân giác trong một tam giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được đường trung tuyến, '
                           'trọng tâm và tính chất trọng tâm của tam giác.',
                           'Quy tắc/công thức **Hệ thức trọng tâm $G$ trên trung tuyến $AM$** trong bài được '
                           'xác định bởi: $AG = \\dfrac{2}{3}AM; \\quad GM = \\dfrac{1}{3}AM; \\quad AG = '
                           '2GM$.',
                           'Trong mọi trường hợp, **Hệ thức trọng tâm $G$ trên trung tuyến $AM$** luôn được '
                           'tính bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b '
                           '\\in \\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà '
                           'không cần điều kiện của Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường '
                           'phân giác trong một tam giác.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ có đường trung tuyến $AM = '
                           '12\\text{ cm}$ và trọng tâm $G$. Tính độ dài các đoạn thẳng $AG$ và $GM$.”, lời '
                           'giải đúng là: Vì $G$ là trọng tâm của $\\triangle ABC$ nên: - $AG = '
                           '\\dfrac{2}{3}AM = \\dfrac{2}{3} \\cdot 12 = 8\\text{ (cm)}$; - $GM = '
                           '\\dfrac{1}{3}AM = \\dfrac{1}{3} \\cdot 12 = 4\\text{ (cm)}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 34: Sự đồng quy của ba đường trung tuyến, '
                        'ba đường phân giác trong một tam giác. b) **Đúng** theo công thức trọng tâm **Hệ '
                        'thức trọng tâm $G$ trên trung tuyến $AM$** ($AG = \\dfrac{2}{3}AM; \\quad GM = '
                        '\\dfrac{1}{3}AM; \\quad AG = 2GM$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ '
                        '\\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công '
                        'thức của nội dung khác, không phải quy tắc chung của **Hệ thức trọng tâm $G$ trên '
                        'trung tuyến $AM$**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác '
                 'trong một tam giác** để giải quyết tình huống sau: Cho $\\triangle ABC$ có đường trung '
                 'tuyến $AM = 12\\text{ cm}$ và trọng tâm $G$. Tính độ dài các đoạn thẳng $AG$ và $GM$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.',
                        'Vì $G$ là trọng tâm của $\\triangle ABC$ nên: - $AG = \\dfrac{2}{3}AM = '
                        '\\dfrac{2}{3} \\cdot 12 = 8\\text{ (cm)}$; - $GM = \\dfrac{1}{3}AM = \\dfrac{1}{3} '
                        '\\cdot 12 = 4\\text{ (cm)}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân '
                        'giác trong một tam giác: Vì $G$ là trọng tâm của $\\triangle ABC$ nên:\n'
                        '- $AG = \\dfrac{2}{3}AM = \\dfrac{2}{3} \\cdot 12 = 8\\text{ (cm)}$;\n'
                        '- $GM = \\dfrac{1}{3}AM = \\dfrac{1}{3} \\cdot 12 = 4\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ có trọng tâm $G$ và đường trung tuyến $AD$. Biết $GD = 5\\text{ cm}$, '
                 'tính độ dài cả đường trung tuyến $AD$ (đơn vị $\\text{cm}$).',
            'answer': ['15'],
            'unit': None,
            'solution': 'Vì $GD = \\dfrac{1}{3}AD$ nên $AD = 3 \\cdot GD = 3 \\cdot 5 = 15\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch09-quan-he-trong-tam-giac',
  'context_title': 'Chương IX: Quan hệ giữa các yếu tố trong một tam giác',
  'context': 'Chương IX · SGK Toán 7: Quan hệ giữa góc và cạnh đối diện, đường vuông góc và đường xiên, bất '
             'đẳng thức tam giác và các đường đồng quy trong tam giác.',
  'title': 'Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác',
  'icon': '⭐',
  'description': 'Sự đồng quy của ba đường trung trực (điểm cách đều ba đỉnh) và sự đồng quy của ba đường '
                 'cao (trực tâm) trong một tam giác.',
  'requirements': ['Nhận biết được đường trung trực của tam giác và tính chất ba đường trung trực đồng quy '
                   'tại một điểm cách đều ba đỉnh.',
                   'Nhận biết được đường cao của tam giác và sự đồng quy của ba đường cao tại trực tâm của '
                   'tam giác.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Giao điểm 3 đường trung trực $O$** ($OA = '
                   'OB = OC$ (cách đều ba đỉnh $A, B, C$)) vào giải bài tập.'],
  'definition': 'Ba đường trung trực của một tam giác cùng đi qua một điểm và điểm này cách đều ba đỉnh của '
                'tam giác. Đường thẳng kẻ từ một đỉnh và vuông góc với cạnh đối diện gọi là đường cao của '
                'tam giác; ba đường cao của tam giác cùng đi qua một điểm gọi là trực tâm.',
  'theory': '1. Sự đồng quy của ba đường trung trực:\n'
            '- Trong một tam giác, đường trung trực của mỗi cạnh gọi là đường trung trực của tam giác đó.\n'
            '- Ba đường trung trực của $\\triangle ABC$ cùng đi qua một điểm $O$ và $OA = OB = OC$ ($O$ là '
            'tâm đường tròn đi qua ba đỉnh $A, B, C$).\n'
            '2. Sự đồng quy của ba đường cao:\n'
            '- Ba đường cao của một tam giác cùng đi qua một điểm $H$, gọi là trực tâm của tam giác.\n'
            '- Chú ý trong tam giác cân và tam giác đều: Trong tam giác cân, đường trung tuyến xuất phát từ '
            'đỉnh đồng thời là đường phân giác, đường trung trực và đường cao. Trong tam giác đều, trọng '
            'tâm, trực tâm, giao điểm ba đường phân giác và giao điểm ba đường trung trực trùng nhau.',
  'formulas': [{'category': 'Tổng kết 4 đường đồng quy trong $\\triangle ABC$',
                'items': [{'name': 'Giao điểm 3 đường trung trực $O$',
                           'formula': '$OA = OB = OC$ (cách đều ba đỉnh $A, B, C$)'},
                          {'name': 'Giao điểm 3 đường cao $H$ (trực tâm)',
                           'formula': '$AH \\perp BC, \\; BH \\perp AC, \\; CH \\perp AB$'},
                          {'name': 'Tính chất tam giác cân tại $A$',
                           'formula': 'Đường trung tuyến, phân giác, đường cao kẻ từ $A$ và trung trực của '
                                      '$BC$ trùng nhau'}]}],
  'example': 'Cho $\\triangle ABC$ có hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Chứng minh $AH \\perp '
             'BC$.',
  'example_answer': 'Trong $\\triangle ABC$, hai đường cao $BD$ và $CE$ cắt nhau tại $H$ nên $H$ là trực tâm '
                    'của $\\triangle ABC$.\n'
                    'Vì ba đường cao của tam giác đồng quy tại trực tâm $H$ nên đường thẳng $AH$ là đường '
                    'cao thứ ba, suy ra $AH \\perp BC$.',
  'real_life': 'Tìm vị trí lắp cột đèn chiếu sáng hoặc trạm phát Wi-Fi sao cho cách đều cả ba tòa nhà $A, B, '
               'C$ (chính là giao điểm ba đường trung trực của $\\triangle ABC$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giao điểm của ba đường cao trong một tam giác được gọi là:',
            'options': ['Trọng tâm của tam giác',
                        'Tâm đường tròn nội tiếp',
                        'Trực tâm của tam giác',
                        'Tâm đường tròn ngoại tiếp'],
            'answer': 2,
            'solution': 'Ba đường cao của tam giác cùng đi qua một điểm gọi là trực tâm của tam giác.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Điểm cách đều ba đỉnh của một tam giác là giao điểm của:',
            'options': ['Ba đường phân giác của tam giác',
                        'Ba đường trung tuyến của tam giác',
                        'Ba đường cao của tam giác',
                        'Ba đường trung trực của tam giác'],
            'answer': 3,
            'solution': 'Giao điểm $O$ của ba đường trung trực thỏa mãn $OA = OB = OC$ nên cách đều ba đỉnh.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao '
                 'trong một tam giác**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Giao điểm 3 '
                 'đường trung trực $O$**?',
            'options': ['$OA = OB = OC$ (cách đều ba đỉnh $A, B, C$)',
                        '$AH \\perp BC, \\; BH \\perp AC, \\; CH \\perp AB$',
                        'Đường trung tuyến, phân giác, đường cao kẻ từ $A$ và trung trực của $BC$ trùng nhau',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 35: Sự đồng quy của ba đường trung trực, ba '
                        'đường cao trong một tam giác, **Giao điểm 3 đường trung trực $O$** được xác định '
                        'bởi: $OA = OB = OC$ (cách đều ba đỉnh $A, B, C$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác**, '
                 'nội dung/biểu thức $AH \\perp BC, \\; BH \\perp AC, \\; CH \\perp AB$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Giao điểm 3 đường trung trực $O$',
                        'Giao điểm 3 đường cao $H$ (trực tâm)',
                        'Tính chất tam giác cân tại $A$',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 1,
            'solution': 'Trong Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác, '
                        'biểu thức/quy tắc $AH \\perp BC, \\; BH \\perp AC, \\; CH \\perp AB$ chính là nội '
                        'dung của **Giao điểm 3 đường cao $H$ (trực tâm)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong một tam giác vuông, trực tâm của tam giác nằm ở vị trí nào?',
            'options': ['Nằm ở trung điểm cạnh huyền',
                        'Nằm bên trong tam giác',
                        'Trùng với đỉnh góc vuông',
                        'Nằm bên ngoài tam giác'],
            'answer': 2,
            'solution': 'Trong tam giác vuông, hai cạnh góc vuông chính là hai đường cao cắt nhau tại đỉnh '
                        'góc vuông nên trực tâm trùng với đỉnh góc vuông.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác** '
                 '(Chương IX: Quan hệ giữa các yếu tố trong một tam giác), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.',
                        'Nhận biết được đường trung trực của tam giác và tính chất ba đường trung trực đồng '
                        'quy tại một điểm cách đều ba đỉnh.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao '
                        'trong một tam giác: Nhận biết được đường trung trực của tam giác và tính chất ba '
                        'đường trung trực đồng quy tại một điểm cách đều ba đỉnh.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ cân tại $A$ có $AM$ là đường trung tuyến ứng với cạnh đáy $BC$. Xét '
                 'các khẳng định sau:',
            'statements': ['$AM$ đồng thời là đường phân giác xuất phát từ đỉnh $A$.',
                           '$AM$ đồng thời là đường cao và đường trung trực ứng với cạnh $BC$.',
                           'Trọng tâm, trực tâm, giao điểm ba đường phân giác và giao điểm ba đường trung '
                           'trực của $\\triangle ABC$ cùng nằm trên đường thẳng $AM$.',
                           'Nếu $O$ là giao điểm ba đường trung trực của $\\triangle ABC$ và $OA = 6\\text{ '
                           'cm}$ thì $OB + OC = 10\\text{ cm}$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng theo tính chất tam giác cân. d) Sai vì $OA = OB = OC = 6\\text{ '
                        'cm}$ nên $OB + OC = 12\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 35: Sự đồng quy của ba '
                 'đường trung trực, ba đường cao trong một tam giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được đường trung trực '
                           'của tam giác và tính chất ba đường trung trực đồng quy tại một điểm cách đều ba '
                           'đỉnh.',
                           'Quy tắc/công thức **Giao điểm 3 đường trung trực $O$** trong bài được xác định '
                           'bởi: $OA = OB = OC$ (cách đều ba đỉnh $A, B, C$).',
                           'Trong mọi trường hợp, **Giao điểm 3 đường trung trực $O$** luôn được tính bằng '
                           'công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao '
                           'trong một tam giác.',
                           'Với bài toán minh họa: “Cho $\\triangle ABC$ có hai đường cao $BD$ và $CE$ cắt '
                           'nhau tại $H$. Chứng minh $AH \\perp BC$.”, lời giải đúng là: Trong $\\triangle '
                           'ABC$, hai đường cao $BD$ và $CE$ cắt nhau tại $H$ nên $H$ là trực tâm của '
                           '$\\triangle ABC$. Vì ba đường cao của tam giác đồn...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 35: Sự đồng quy của ba đường trung trực, '
                        'ba đường cao trong một tam giác. b) **Đúng** theo công thức trọng tâm **Giao điểm 3 '
                        'đường trung trực $O$** ($OA = OB = OC$ (cách đều ba đỉnh $A, B, C$)). c) **Sai** vì '
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$ là công thức của nội dung khác, không phải quy tắc chung của '
                        '**Giao điểm 3 đường trung trực $O$**. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một '
                 'tam giác** để giải quyết tình huống sau: Cho $\\triangle ABC$ có hai đường cao $BD$ và '
                 '$CE$ cắt nhau tại $H$. Chứng minh $AH \\perp BC$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Trong $\\triangle ABC$, hai đường cao $BD$ và $CE$ cắt nhau tại $H$ nên $H$ là trực '
                        'tâm của $\\triangle ABC$. Vì ba đường cao của tam giác đồng quy tại trực...',
                        'Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao '
                        'trong một tam giác: Trong $\\triangle ABC$, hai đường cao $BD$ và $CE$ cắt nhau tại '
                        '$H$ nên $H$ là trực tâm của $\\triangle ABC$.\n'
                        'Vì ba đường cao của tam giác đồng quy tại trực tâm $H$ nên đường thẳng $AH$ là '
                        'đường cao thứ ba, suy ra $AH \\perp BC$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Gọi $O$ là giao điểm của ba đường trung trực trong $\\triangle ABC$. Biết $OA = 7\\text{ '
                 'cm}$, tính tổng độ dài $OB + OC$ (đơn vị $\\text{cm}$).',
            'answer': ['14'],
            'unit': None,
            'solution': 'Vì $O$ cách đều ba đỉnh của $\\triangle ABC$ nên $OB = OC = OA = 7\\text{ cm}$, suy '
                        'ra $OB + OC = 7 + 7 = 14\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l7-ch10-hinh-khoi',
  'context_title': 'Chương X: Một số hình khối trong thực tiễn',
  'context': 'Chương X · SGK Toán 7: Hình hộp chữ nhật, hình lập phương, hình lăng trụ đứng tam giác và hình '
             'lăng trụ đứng tứ giác.',
  'title': 'Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng tam giác, tứ giác',
  'icon': '📦',
  'description': 'Các yếu tố cơ bản, công thức tính diện tích xung quanh và thể tích của hình hộp chữ nhật, '
                 'hình lập phương và hình lăng trụ đứng.',
  'requirements': ['Mô tả được các yếu tố (đỉnh, cạnh, mặt đáy, mặt bên, chiều cao) của hình hộp chữ nhật, '
                   'hình lập phương, hình lăng trụ đứng tam giác và tứ giác.',
                   'Tính được diện tích xung quanh và thể tích của hình hộp chữ nhật, hình lập phương và '
                   'hình lăng trụ đứng trong thực tiễn.',
                   'Ghi nhớ và vận dụng đúng quy tắc/công thức **Hình hộp chữ nhật kích thước $a, b, c$** '
                   '($S_{xq} = 2(a + b)c; \\quad V = a \\cdot b \\cdot c$) vào giải bài tập.'],
  'definition': 'Hình hộp chữ nhật có $6$ mặt là các hình chữ nhật, $8$ đỉnh, $12$ cạnh. Hình lập phương là '
                'hình hộp chữ nhật có $6$ mặt đều là hình vuông bằng nhau. Hình lăng trụ đứng tam giác (tứ '
                'giác) có hai mặt đáy song song là tam giác (tứ giác) và các mặt bên là các hình chữ nhật.',
  'theory': '1. Hình hộp chữ nhật (ba kích thước $a, b, c$) và hình lập phương (cạnh $d$):\n'
            '- Diện tích xung quanh hình hộp chữ nhật: $S_{xq} = 2(a + b)c$; Thể tích: $V = abc$.\n'
            '- Diện tích xung quanh hình lập phương: $S_{xq} = 4d^2$; Thể tích: $V = d^3$.\n'
            '2. Hình lăng trụ đứng tam giác và hình lăng trụ đứng tứ giác:\n'
            '- Diện tích xung quanh bằng chu vi đáy nhân với chiều cao: $S_{xq} = C_{\\text{đáy}} \\cdot '
            'h$.\n'
            '- Thể tích bằng diện tích đáy nhân với chiều cao: $V = S_{\\text{đáy}} \\cdot h$.',
  'formulas': [{'category': 'Diện tích xung quanh và thể tích các hình khối',
                'items': [{'name': 'Hình hộp chữ nhật kích thước $a, b, c$',
                           'formula': '$S_{xq} = 2(a + b)c; \\quad V = a \\cdot b \\cdot c$'},
                          {'name': 'Hình lập phương cạnh $d$',
                           'formula': '$S_{xq} = 4d^2; \\quad S_{tp} = 6d^2; \\quad V = d^3$'},
                          {'name': 'Hình lăng trụ đứng tam giác, tứ giác',
                           'formula': '$S_{xq} = C_{\\text{đáy}} \\cdot h; \\quad V = S_{\\text{đáy}} \\cdot '
                                      'h$'}]}],
  'example': 'Một chiếc lều cắm trại có dạng hình lăng trụ đứng tam giác với chiều cao lều (chiều dài lăng '
             'trụ) $h = 3\\text{ m}$, đáy là tam giác có cạnh đáy $2\\text{ m}$ và chiều cao tương ứng của '
             'tam giác đáy là $1,5\\text{ m}$. Tính thể tích không gian bên trong lều.',
  'example_answer': 'Diện tích mặt đáy hình tam giác là: $S_{\\text{đáy}} = \\dfrac{1}{2} \\cdot 2 \\cdot '
                    '1,5 = 1,5\\text{ (m}^2\\text{)}$.\n'
                    'Thể tích không gian bên trong lều là: $V = S_{\\text{đáy}} \\cdot h = 1,5 \\cdot 3 = '
                    '4,5\\text{ (m}^3\\text{)}$.',
  'real_life': 'Tính thể tích nước chứa trong bể cá cảnh hình hộp chữ nhật, lượng bìa carton làm thùng đóng '
               'gói hoặc thể tích lều trại chữ A.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình hộp chữ nhật có bao nhiêu đỉnh và bao nhiêu cạnh?',
            'options': ['$6$ đỉnh và $12$ cạnh',
                        '$8$ đỉnh và $8$ cạnh',
                        '$6$ đỉnh và $8$ cạnh',
                        '$8$ đỉnh và $12$ cạnh'],
            'answer': 3,
            'solution': 'Hình hộp chữ nhật và hình lập phương đều có $6$ mặt, $8$ đỉnh và $12$ cạnh.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính thể tích $V$ của hình lăng trụ đứng có diện tích đáy $S_{\\text{đáy}}$ và '
                 'chiều cao $h$ là:',
            'options': ['$V = S_{\\text{đáy}} \\cdot h$',
                        '$V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h$',
                        '$V = 2 S_{\\text{đáy}} \\cdot h$',
                        '$V = C_{\\text{đáy}} \\cdot h$'],
            'answer': 0,
            'solution': 'Thể tích của hình lăng trụ đứng bằng diện tích đáy nhân với chiều cao: $V = '
                        'S_{\\text{đáy}} \\cdot h$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ '
                 'đứng tam giác, tứ giác**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hình hộp chữ '
                 'nhật kích thước $a, b, c$**?',
            'options': ['$S_{xq} = 4d^2; \\quad S_{tp} = 6d^2; \\quad V = d^3$',
                        '$S_{xq} = 2(a + b)c; \\quad V = a \\cdot b \\cdot c$',
                        '$S_{xq} = C_{\\text{đáy}} \\cdot h; \\quad V = S_{\\text{đáy}} \\cdot h$',
                        '$\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in \\mathbb{Z}, b '
                        '\\neq 0 \\right\\}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 36: Hình hộp chữ nhật, hình lập phương và '
                        'hình lăng trụ đứng tam giác, tứ giác, **Hình hộp chữ nhật kích thước $a, b, c$** '
                        'được xác định bởi: $S_{xq} = 2(a + b)c; \\quad V = a \\cdot b \\cdot c$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng tam giác, tứ '
                 'giác**, nội dung/biểu thức $S_{xq} = 4d^2; \\quad S_{tp} = 6d^2; \\quad V = d^3$ là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hình hộp chữ nhật kích thước $a, b, c$',
                        'Hình lăng trụ đứng tam giác, tứ giác',
                        'Hình lập phương cạnh $d$',
                        'Định nghĩa tập $\\mathbb{Q}$'],
            'answer': 2,
            'solution': 'Trong Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng tam giác, tứ '
                        'giác, biểu thức/quy tắc $S_{xq} = 4d^2; \\quad S_{tp} = 6d^2; \\quad V = d^3$ chính '
                        'là nội dung của **Hình lập phương cạnh $d$**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình lập phương có độ dài cạnh bằng $4\\text{ cm}$. Diện tích xung quanh và thể tích '
                 'của hình lập phương đó lần lượt là:',
            'options': ['$96\\text{ cm}^2$ và $64\\text{ cm}^3$',
                        '$16\\text{ cm}^2$ và $64\\text{ cm}^3$',
                        '$64\\text{ cm}^2$ và $16\\text{ cm}^3$',
                        '$64\\text{ cm}^2$ và $64\\text{ cm}^3$'],
            'answer': 3,
            'solution': 'Ta có $S_{xq} = 4 \\cdot 4^2 = 64\\text{ cm}^2$ và $V = 4^3 = 64\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng tam giác, tứ '
                 'giác** (Chương X: Một số hình khối trong thực tiễn), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Mô tả được các yếu tố (đỉnh, cạnh, mặt đáy, mặt bên, chiều cao) của hình hộp chữ '
                        'nhật, hình lập phương, hình lăng trụ đứng tam giác và tứ giác.',
                        'Nhận biết được số hữu tỉ và lấy được ví dụ về số hữu tỉ, nhận biết tập hợp các số '
                        'hữu tỉ $\\mathbb{Q}$.',
                        'Biểu diễn được số hữu tỉ trên trục số và nhận biết được số đối của một số hữu tỉ.',
                        'Nhận biết được thứ tự trong tập hợp các số hữu tỉ và so sánh được hai số hữu tỉ.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng '
                        'trụ đứng tam giác, tứ giác: Mô tả được các yếu tố (đỉnh, cạnh, mặt đáy, mặt bên, '
                        'chiều cao) của hình hộp chữ nhật, hình lập phương, hình lăng trụ đứng tam giác và '
                        'tứ giác.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho một bể cá dạng hình hộp chữ nhật không nắp có chiều dài $a = 80\\text{ cm}$, chiều '
                 'rộng $b = 40\\text{ cm}$ và chiều cao $c = 50\\text{ cm}$. Xét các khẳng định sau:',
            'statements': ['Diện tích mặt đáy của bể cá là $3200\\text{ cm}^2$.',
                           'Diện tích xung quanh của bể cá là $S_{xq} = 2(80 + 40) \\cdot 50 = 12000\\text{ '
                           'cm}^2$.',
                           'Thể tích của bể cá là $V = 160000\\text{ cm}^3$ (tức là $160$ lít).',
                           'Các mặt bên của hình lăng trụ đứng tam giác là các hình tam giác.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng ($1\\text{ lít} = 1000\\text{ cm}^3$). d) Sai vì các mặt bên của '
                        'hình lăng trụ đứng luôn là các hình chữ nhật.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 36: Hình hộp chữ nhật, '
                 'hình lập phương và hình lăng trụ đứng tam giác, tứ giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả được các yếu tố (đỉnh, cạnh, '
                           'mặt đáy, mặt bên, chiều cao) của hình hộp chữ nhật, hình lập phương, hình lăng '
                           'trụ đứng tam giác và tứ giác.',
                           'Quy tắc/công thức **Hình hộp chữ nhật kích thước $a, b, c$** trong bài được xác '
                           'định bởi: $S_{xq} = 2(a + b)c; \\quad V = a \\cdot b \\cdot c$.',
                           'Trong mọi trường hợp, **Hình hộp chữ nhật kích thước $a, b, c$** luôn được tính '
                           'bằng công thức $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, b \\in '
                           '\\mathbb{Z}, b \\neq 0 \\right\\}$ (thuộc Định nghĩa tập $\\mathbb{Q}$) mà không '
                           'cần điều kiện của Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ '
                           'đứng tam giác, tứ giác.',
                           'Với bài toán minh họa: “Một chiếc lều cắm trại có dạng hình lăng trụ đứng tam '
                           'giác với chiều cao lều (chiều dài lăng trụ) $h = 3\\text{ m}$, đáy là tam giác '
                           'có cạnh...”, lời giải đúng là: Diện tích mặt đáy hình tam giác là: '
                           '$S_{\\text{đáy}} = \\dfrac{1}{2} \\cdot 2 \\cdot 1,5 = 1,5\\text{ '
                           '(m}^2\\text{)}$. Thể tích không gian bên tro...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 36: Hình hộp chữ nhật, hình lập phương và '
                        'hình lăng trụ đứng tam giác, tứ giác. b) **Đúng** theo công thức trọng tâm **Hình '
                        'hộp chữ nhật kích thước $a, b, c$** ($S_{xq} = 2(a + b)c; \\quad V = a \\cdot b '
                        '\\cdot c$). c) **Sai** vì $\\mathbb{Q} = \\left\\{ \\dfrac{a}{b} \\;\\middle|\\; a, '
                        'b \\in \\mathbb{Z}, b \\neq 0 \\right\\}$ là công thức của nội dung khác, không '
                        'phải quy tắc chung của **Hình hộp chữ nhật kích thước $a, b, c$**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ đứng tam '
                 'giác, tứ giác** để giải quyết tình huống sau: Một chiếc lều cắm trại có dạng hình lăng trụ '
                 'đứng tam giác với chiều cao lều (chiều dài lăng trụ) $h = 3\\text{ m}$, đáy là tam giác có '
                 'cạnh đáy $2\\text{ m}$ và chiều cao tương ứng của tam giác đáy là $1,5\\text{ m}$. Tính '
                 'thể tích không gian bên trong lều. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có: $-2,5 = \\dfrac{-5}{2} = \\dfrac{-15}{6}$; $1\\dfrac{2}{3} = \\dfrac{5}{3}$; '
                        '$-4 = \\dfrac{-4}{1} = \\dfrac{-24}{6}$. Vì $-4 < -2,5 < 0 < 1\\dfrac{2}{3}$ n...',
                        'Diện tích mặt đáy hình tam giác là: $S_{\\text{đáy}} = \\dfrac{1}{2} \\cdot 2 '
                        '\\cdot 1,5 = 1,5\\text{ (m}^2\\text{)}$. Thể tích không gian bên trong lều là...',
                        'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = \\dfrac{-3}{7} '
                        '\\cdot \\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) + \\dfrac{10}{7} = '
                        '\\dfrac{-3}{7} \\cdot 1 + \\dfrac{10}{7} = \\dfrac{7}{7} = 1$...',
                        'Ta có: $M = \\dfrac{(2^3)^{10}}{(2^2)^8} = \\dfrac{2^{30}}{2^{16}} = 2^{30-16} = '
                        '2^{14} = 16384$. $N = (0,125 \\cdot 8)^3 = 1^3 = 1$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 36: Hình hộp chữ nhật, hình lập phương và hình lăng trụ '
                        'đứng tam giác, tứ giác: Diện tích mặt đáy hình tam giác là: $S_{\\text{đáy}} = '
                        '\\dfrac{1}{2} \\cdot 2 \\cdot 1,5 = 1,5\\text{ (m}^2\\text{)}$.\n'
                        'Thể tích không gian bên trong lều là: $V = S_{\\text{đáy}} \\cdot h = 1,5 \\cdot 3 '
                        '= 4,5\\text{ (m}^3\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình lăng trụ đứng tam giác có đáy là tam giác vuông với hai cạnh góc vuông dài '
                 '$3\\text{ cm}$ và $4\\text{ cm}$, chiều cao của hình lăng trụ là $10\\text{ cm}$. Tính thể '
                 'tích của hình lăng trụ đứng đó (đơn vị $\\text{cm}^3$).',
            'answer': ['60'],
            'unit': None,
            'solution': 'Diện tích đáy là $S_{\\text{đáy}} = \\dfrac{1}{2} \\cdot 3 \\cdot 4 = 6\\text{ '
                        '(cm}^2\\text{)}$. Thể tích là $V = S_{\\text{đáy}} \\cdot h = 6 \\cdot 10 = '
                        '60\\text{ (cm}^3\\text{)}$.',
            'alt': None,
            'note': None}]}]
