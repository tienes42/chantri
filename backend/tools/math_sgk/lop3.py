"""Dữ liệu bài học SGK Toán Lớp 3 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 3 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học (title).
Mỗi bài học gồm đầy đủ Yêu cầu cần đạt (requirements), Định nghĩa, Lý thuyết, Công thức, Ví dụ, Ứng dụng thực tế
và đúng 10 câu hỏi luyện tập theo 3 mức độ: 4 Nhận biết + 4 Thông hiểu + 2 Vận dụng.
"""

GRADE = 3

LESSONS = [{'topic': 'l3-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 3 · Chủ đề 1: Ôn tập các số đến 1 000 và bảng nhân, chia 2, 3, 4, 5.',
  'title': 'Bài 1: Ôn tập các số đến 1 000',
  'icon': '🔢',
  'description': 'Đọc, viết, phân tích cấu tạo thập phân và so sánh các số trong phạm vi 1 000.',
  'requirements': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                   'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                   'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
  'definition': '- Số có ba chữ số gồm hàng trăm, hàng chục và hàng đơn vị: $\\overline{abc} = a \\times 100 '
                '+ b \\times 10 + c$.\n'
                '- Mười trăm bằng một nghìn: $10 \\text{ trăm} = 1\\,000$.\n'
                '- Khi so sánh hai số có ba chữ số, ta so sánh chữ số hàng trăm trước, nếu bằng nhau thì so '
                'sánh tiếp hàng chục rồi đến hàng đơn vị.',
  'theory': '### 1. Cấu tạo số có ba chữ số\n'
            '- Mỗi số có ba chữ số được viết dưới dạng tổng các trăm, chục, đơn vị. Ví dụ: $685 = 600 + 80 + '
            '5$ (gồm $6$ trăm, $8$ chục và $5$ đơn vị).\n'
            '- Nếu hàng chục hoặc hàng đơn vị bằng $0$, khi đọc số ta dùng từ "linh" (ở hàng chục) hoặc '
            'không đọc hàng đơn vị bằng $0$. Ví dụ: $708$ đọc là bảy trăm linh tám.\n'
            '### 2. So sánh các số trong phạm vi $1\\,000$\n'
            '- Số có nhiều chữ số hơn thì lớn hơn: $1\\,000 > 999 > 99$.\n'
            '- Hai số có cùng ba chữ số: so sánh từ trái sang phải (trăm $\\rightarrow$ chục $\\rightarrow$ '
            'đơn vị). Ví dụ: $542 < 561$ vì cùng $5$ trăm và $4 < 6$.',
  'formulas': [{'category': 'I. Cấu tạo thập phân',
                'items': [{'name': 'Phân tích số',
                           'formula': '$\\overline{abc} = a00 + b0 + c$',
                           'note': 'Ví dụ: $437 = 400 + 30 + 7$'},
                          {'name': 'Số tròn trăm, tròn nghìn',
                           'formula': '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'}]},
               {'category': 'II. Quy tắc so sánh',
                'items': [{'name': 'Cùng số chữ số',
                           'formula': 'So sánh hàng trăm $\\rightarrow$ hàng chục $\\rightarrow$ hàng đơn '
                                      'vị'}]}],
  'example': 'Phân tích số $806$ thành tổng các trăm, chục, đơn vị và so sánh $806$ với $798$.',
  'example_answer': 'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị).\n'
                    'Vì chữ số hàng trăm $8 > 7$ nên **$806 > 798$**.',
  'real_life': '- Đọc số thứ tự trang sách, số nhà trên phố, số tiền mệnh giá nhỏ hoặc số ghế trong rạp hát.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số $708$ gồm:',
            'options': ['$7$ trăm, $0$ chục, $8$ đơn vị',
                        '$7$ trăm, $8$ chục',
                        '$70$ chục, $8$ trăm',
                        '$7$ chục, $8$ đơn vị'],
            'answer': 0,
            'solution': 'Ta có $708 = 700 + 0 + 8$ nên gồm **$7$ trăm, $0$ chục, $8$ đơn vị**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số "bốn trăm năm mươi lăm" được viết là:',
            'options': ['$450$', '$455$', '$405$', '$545$'],
            'answer': 1,
            'solution': 'Bốn trăm ($400$), năm mươi ($50$), lăm ($5$) viết là **$455$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 1: Ôn tập các số đến 1 000**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Phân tích số**?',
            'options': ['$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'So sánh hàng trăm $\\rightarrow$ hàng chục $\\rightarrow$ hàng đơn vị',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Đặt thẳng cột · Tính từ phải sang trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm)'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 1: Ôn tập các số đến 1 000, **Phân tích số** '
                        'được xác định bởi: $\\overline{abc} = a00 + b0 + c$. (Ví dụ: $437 = 400 + 30 + 7$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Ôn tập các số đến 1 000**, nội dung/biểu thức $10 \\text{ chục} = 100$ · '
                 '$10 \\text{ trăm} = 1\\,000$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phân tích số', 'Cùng số chữ số', 'Thứ tự tính', 'Số tròn trăm, tròn nghìn'],
            'answer': 3,
            'solution': 'Trong Bài 1: Ôn tập các số đến 1 000, biểu thức/quy tắc $10 \\text{ chục} = 100$ · '
                        '$10 \\text{ trăm} = 1\\,000$ chính là nội dung của **Số tròn trăm, tròn nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các số $689$, $698$, $869$, $690$, số lớn nhất là:',
            'options': ['$869$', '$689$', '$698$', '$690$'],
            'answer': 0,
            'solution': 'So sánh chữ số hàng trăm: $8 > 6$ nên **$869$** là số lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Ôn tập các số đến 1 000** (Chủ đề 1: Ôn tập và bổ sung), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đặt tính và tính đúng phép cộng, phép trừ các số có đến ba chữ số trong phạm vi 1 '
                        '000.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Cộng, trừ nhẩm được các số tròn trăm, tròn chục.',
                        'Giải được bài toán thực tế có một bước cộng hoặc trừ.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 1: Ôn tập các số đến 1 000: Đọc, viết thành thạo các '
                        'số có đến ba chữ số trong phạm vi 1 000.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số liền trước của số $1\\,000$ là số $999$."',
            'answer': True,
            'solution': 'Ta có $1\\,000 - 1 = 999$ nên số liền trước của $1\\,000$ là $999$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 1: Ôn tập các số đến 1 000**, quy tắc **Phân tích số** được xác định bởi '
                 '$\\overline{abc} = a00 + b0 + c$ và áp dụng trực tiếp vào bài toán: “Phân tích số $806$ '
                 'thành tổng các trăm, chục, đơn vị và so sánh $806$ với $798$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Phân tích số** ($\\overline{abc} = a00 + b0 + c$) là '
                        'kiến thức cốt lõi của Bài 1: Ôn tập các số đến 1 000. Ta có $806 = 800 + 6$ (gồm '
                        '$8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 > 7$ nên **$806 > 798$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 1: Ôn tập các số đến 1 000** để giải quyết tình huống sau: Phân '
                 'tích số $806$ thành tổng các trăm, chục, đơn vị và so sánh $806$ với $798$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $3 \\times 9 = 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$). - $4 \\times 7 = 28$ '
                        'và $32 : 4 = 8$ (vì $4 \\times 8 = 32$).'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Ôn tập các số đến 1 000: Ta có $806 = 800 + 6$ (gồm '
                        '$8$ trăm, $0$ chục, $6$ đơn vị).\n'
                        'Vì chữ số hàng trăm $8 > 7$ nên **$806 > 798$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Viết số tự nhiên lớn nhất có ba chữ số khác nhau.',
            'answer': ['987'],
            'unit': None,
            'solution': 'Chọn chữ số hàng trăm lớn nhất là $9$, hàng chục là $8$, hàng đơn vị là $7$. Ta '
                        'được số **$987$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 3 · Chủ đề 1: Ôn tập các số đến 1 000 và bảng nhân, chia 2, 3, 4, 5.',
  'title': 'Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000',
  'icon': '➕',
  'description': 'Thực hiện phép cộng, phép trừ không nhớ và có nhớ trong phạm vi 1 000.',
  'requirements': ['Đặt tính và tính đúng phép cộng, phép trừ các số có đến ba chữ số trong phạm vi 1 000.',
                   'Cộng, trừ nhẩm được các số tròn trăm, tròn chục.',
                   'Giải được bài toán thực tế có một bước cộng hoặc trừ.'],
  'definition': '- Khi đặt tính cộng hoặc trừ các số trong phạm vi $1\\,000$, ta viết các chữ số cùng một '
                'hàng thẳng cột với nhau.\n'
                '- Thực hiện tính lần lượt từ phải sang trái (từ hàng đơn vị $\\rightarrow$ hàng chục '
                '$\\rightarrow$ hàng trăm), có nhớ hoặc mượn $1$ sang hàng kế tiếp khi cần.',
  'theory': '### 1. Phép cộng trong phạm vi $1\\,000$\n'
            '- Ví dụ: $356 + 272$. Cộng hàng đơn vị: $6 + 2 = 8$; cộng hàng chục: $5 + 7 = 12$, viết $2$ nhớ '
            '$1$; cộng hàng trăm: $3 + 2 = 5$, thêm $1$ bằng $6$. Kết quả: $356 + 272 = 628$.\n'
            '### 2. Phép trừ trong phạm vi $1\\,000$\n'
            '- Ví dụ: $642 - 218$. Trừ hàng đơn vị: $12 - 8 = 4$, viết $4$ nhớ $1$; hàng chục: $2$ thêm $1$ '
            'bằng $3$, $4 - 3 = 1$; hàng trăm: $6 - 2 = 4$. Kết quả: $642 - 218 = 424$.',
  'formulas': [{'category': 'I. Quy tắc đặt tính',
                'items': [{'name': 'Thứ tự tính',
                           'formula': 'Đặt thẳng cột · Tính từ phải sang trái (Đơn vị $\\rightarrow$ Chục '
                                      '$\\rightarrow$ Trăm)'}]},
               {'category': 'II. Tính nhẩm số tròn trăm',
                'items': [{'name': 'Cộng, trừ tròn trăm',
                           'formula': '$a00 + b00 = (a+b)00$ · $a00 - b00 = (a-b)00$',
                           'note': 'Ví dụ: $300 + 500 = 800$'}]}],
  'example': 'Đặt tính và tính: $468 + 325$ và $750 - 236$.',
  'example_answer': '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                    '$\\rightarrow$ **$793$**.\n'
                    '- $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + 1) = 1$; $7 - 2 = 5$ '
                    '$\\rightarrow$ **$514$**.',
  'real_life': '- Tính tổng số học sinh khối $3$ của trường hoặc tính số hàng hóa còn lại trong kho sau khi '
               'bán.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $400 + 500$ là:',
            'options': ['$800$', '$900$', '$100$', '$90$'],
            'answer': 1,
            'solution': 'Cộng nhẩm: $4$ trăm $+ 5$ trăm $= 9$ trăm $= 900$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $685 - 243$ là:',
            'options': ['$432$', '$448$', '$442$', '$928$'],
            'answer': 2,
            'solution': 'Trừ từng hàng: $5 - 3 = 2$; $8 - 4 = 4$; $6 - 2 = 4$ $\\rightarrow$ **$442$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự tính**?',
            'options': ['$a00 + b00 = (a+b)00$ · $a00 - b00 = (a-b)00$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Đặt thẳng cột · Tính từ phải sang trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 '
                        '000, **Thứ tự tính** được xác định bởi: Đặt thẳng cột · Tính từ phải sang trái (Đơn '
                        'vị $\\rightarrow$ Chục $\\rightarrow$ Trăm).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000**, nội dung/biểu thức $a00 + '
                 'b00 = (a+b)00$ · $a00 - b00 = (a-b)00$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cộng, trừ tròn trăm', 'Thứ tự tính', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000, biểu thức/quy tắc $a00 '
                        '+ b00 = (a+b)00$ · $a00 - b00 = (a-b)00$ chính là nội dung của **Cộng, trừ tròn '
                        'trăm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng của $367$ và $258$ là:',
            'options': ['$515$', '$625$', '$615$', '$525$'],
            'answer': 1,
            'solution': 'Ta có $367 + 258 = 625$ (nhớ $1$ từ đơn vị sang chục và nhớ $1$ từ chục sang trăm).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000** (Chủ đề 1: Ôn tập và bổ '
                 'sung), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đặt tính và tính đúng phép cộng, phép trừ các số có đến ba chữ số trong phạm vi 1 '
                        '000.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000: Đặt '
                        'tính và tính đúng phép cộng, phép trừ các số có đến ba chữ số trong phạm vi 1 000.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hiệu của $800$ và $345$ bằng $555$."',
            'answer': False,
            'solution': 'Ta có $800 - 345 = 455$, không phải $555$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000**, quy tắc **Thứ tự tính** '
                 'được xác định bởi Đặt thẳng cột · Tính từ phải sang trái (Đơn vị $\\rightarrow$ Chục '
                 '$\\rightarrow$ Trăm) và áp dụng trực tiếp vào bài toán: “Đặt tính và tính: $468 + 325$ và '
                 '$750 - 236$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự tính** (Đặt thẳng cột · Tính từ phải sang '
                        'trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm)) là kiến thức cốt lõi của Bài '
                        '2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000. - $468 + 325$: $8 + 5 = 13$ '
                        '(viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ $\\rightarrow$ **$793$**. - $750 - '
                        '236$: $10 - 6 = 4$ (viết $4$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000** để giải quyết '
                 'tình huống sau: Đặt tính và tính: $468 + 325$ và $750 - 236$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        '- $3 \\times 9 = 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$). - $4 \\times 7 = 28$ '
                        'và $32 : 4 = 8$ (vì $4 \\times 8 = 32$).',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000: - '
                        '$468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**.\n'
                        '- $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + 1) = 1$; $7 - 2 = 5$ '
                        '$\\rightarrow$ **$514$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng có $450\\text{ kg}$ gạo, sau khi bán còn lại $175\\text{ kg}$. Hỏi cửa hàng '
                 'đã bán bao nhiêu ki-lô-gam gạo?',
            'answer': ['275'],
            'unit': 'kg',
            'solution': 'Số gạo đã bán là: $450 - 175 = 275\\text{ (kg)}$.\nĐáp số: **$275\\text{ kg}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 3 · Chủ đề 1: Ôn tập các số đến 1 000 và bảng nhân, chia 2, 3, 4, 5.',
  'title': 'Bài 3: Tìm thành phần trong phép cộng, phép trừ',
  'icon': '🔍',
  'description': 'Quy tắc tìm số hạng chưa biết trong phép cộng, tìm số bị trừ và số trừ trong phép trừ.',
  'requirements': ['Nêu đúng quy tắc và tìm được số hạng chưa biết khi biết tổng và số hạng kia.',
                   'Tìm được số bị trừ hoặc số trừ chưa biết trong phép trừ.',
                   'Vận dụng tìm thành phần chưa biết để giải toán có lời văn.'],
  'definition': '- **Tìm số hạng** ($x + a = b$): Muốn tìm một số hạng, ta lấy tổng trừ đi số hạng kia ($x = '
                'b - a$).\n'
                '- **Tìm số bị trừ** ($x - a = b$): Muốn tìm số bị trừ, ta lấy hiệu cộng với số trừ ($x = b '
                '+ a$).\n'
                '- **Tìm số trừ** ($a - x = b$): Muốn tìm số trừ, ta lấy số bị trừ trừ đi hiệu ($x = a - '
                'b$).',
  'theory': '### 1. Tìm số hạng trong phép cộng\n'
            '- Phép cộng: $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$.\n'
            '- Ví dụ: $? + 35 = 82 \\Rightarrow ? = 82 - 35 = 47$.\n'
            '### 2. Tìm số bị trừ và số trừ trong phép trừ\n'
            '- Phép trừ: $\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$.\n'
            '- Tìm số bị trừ: $? - 26 = 54 \\Rightarrow ? = 54 + 26 = 80$.\n'
            '- Tìm số trừ: $90 - ? = 37 \\Rightarrow ? = 90 - 37 = 53$.',
  'formulas': [{'category': 'I. Phép cộng',
                'items': [{'name': 'Tìm số hạng',
                           'formula': '$\\text{Số hạng} = \\text{Tổng} - \\text{Số hạng kia}$'}]},
               {'category': 'II. Phép trừ',
                'items': [{'name': 'Tìm số bị trừ',
                           'formula': '$\\text{Số bị trừ} = \\text{Hiệu} + \\text{Số trừ}$'},
                          {'name': 'Tìm số trừ',
                           'formula': '$\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu}$'}]}],
  'example': 'Tìm số trừ chưa biết trong phép tính: $85 - ? = 39$.',
  'example_answer': 'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 - '
                    '39 = 46$.\n'
                    'Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
  'real_life': '- Biết tổng số học sinh của lớp và số bạn nam, tìm số bạn nữ; biết số tiền còn lại và số '
               'tiền đã tiêu, tìm số tiền lúc đầu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn tìm số bị trừ, ta lấy:',
            'options': ['Hiệu trừ đi số trừ',
                        'Số trừ trừ đi hiệu',
                        'Hiệu cộng với số trừ',
                        'Tổng trừ đi số hạng'],
            'answer': 2,
            'solution': 'Theo quy tắc: $\\text{Số bị trừ} = \\text{Hiệu} + \\text{Số trừ}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm số hạng $x$ biết $x + 47 = 92$:',
            'options': ['$139$', '$55$', '$35$', '$45$'],
            'answer': 3,
            'solution': 'Số hạng $x = 92 - 47 = 45$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 3: Tìm thành phần trong phép cộng, phép trừ**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Tìm số hạng**?',
            'options': ['$\\text{Số hạng} = \\text{Tổng} - \\text{Số hạng kia}$',
                        '$\\text{Số bị trừ} = \\text{Hiệu} + \\text{Số trừ}$',
                        '$\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu}$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 3: Tìm thành phần trong phép cộng, phép trừ, '
                        '**Tìm số hạng** được xác định bởi: $\\text{Số hạng} = \\text{Tổng} - \\text{Số hạng '
                        'kia}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Tìm thành phần trong phép cộng, phép trừ**, nội dung/biểu thức $\\text{Số '
                 'bị trừ} = \\text{Hiệu} + \\text{Số trừ}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tìm số hạng', 'Tìm số bị trừ', 'Tìm số trừ', 'Phân tích số'],
            'answer': 1,
            'solution': 'Trong Bài 3: Tìm thành phần trong phép cộng, phép trừ, biểu thức/quy tắc $\\text{Số '
                        'bị trừ} = \\text{Hiệu} + \\text{Số trừ}$ chính là nội dung của **Tìm số bị trừ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một phép trừ có hiệu là $125$, số trừ là $238$. Số bị trừ của phép trừ đó là:',
            'options': ['$113$', '$353$', '$363$', '$263$'],
            'answer': 2,
            'solution': 'Số bị trừ $= 125 + 238 = 363$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Tìm thành phần trong phép cộng, phép trừ** (Chủ đề 1: Ôn tập và bổ sung), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Nêu đúng quy tắc và tìm được số hạng chưa biết khi biết tổng và số hạng kia.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 3: Tìm thành phần trong phép cộng, phép trừ: Nêu đúng '
                        'quy tắc và tìm được số hạng chưa biết khi biết tổng và số hạng kia.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong phép tính $70 - ? = 25$, số cần tìm là $95$."',
            'answer': False,
            'solution': 'Số cần tìm là số trừ: $70 - 25 = 45$, không phải $95$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 3: Tìm thành phần trong phép cộng, phép trừ**, quy tắc **Tìm số hạng** được '
                 'xác định bởi $\\text{Số hạng} = \\text{Tổng} - \\text{Số hạng kia}$ và áp dụng trực tiếp '
                 'vào bài toán: “Tìm số trừ chưa biết trong phép tính: $85 - ? = 39$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tìm số hạng** ($\\text{Số hạng} = \\text{Tổng} - '
                        '\\text{Số hạng kia}$) là kiến thức cốt lõi của Bài 3: Tìm thành phần trong phép '
                        'cộng, phép trừ. Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - '
                        '\\text{Hiệu} = 85 - 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 3: Tìm thành phần trong phép cộng, phép trừ** để giải quyết tình '
                 'huống sau: Tìm số trừ chưa biết trong phép tính: $85 - ? = 39$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        '- $3 \\times 9 = 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$). - $4 \\times 7 = 28$ '
                        'và $32 : 4 = 8$ (vì $4 \\times 8 = 32$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Tìm thành phần trong phép cộng, phép trừ: Áp dụng quy '
                        'tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 - 39 = '
                        '46$.\n'
                        'Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bến xe có một số ô tô, sau khi $18$ ô tô rời bến thì còn lại $27$ ô tô. Hỏi lúc đầu '
                 'bến xe có bao nhiêu ô tô?',
            'answer': ['45'],
            'unit': 'ô tô',
            'solution': 'Số ô tô lúc đầu (số bị trừ) là: $27 + 18 = 45\\text{ (ô tô)}$.\n'
                        'Đáp số: **$45\\text{ ô tô}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 3 · Chủ đề 1: Ôn tập các số đến 1 000 và bảng nhân, chia 2, 3, 4, 5.',
  'title': 'Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5',
  'icon': '✖️',
  'description': 'Ôn tập bảng nhân, chia 2, 5 và lập, vận dụng bảng nhân, bảng chia 3, 4.',
  'requirements': ['Thuộc và vận dụng thành thạo bảng nhân 2, 3, 4, 5.',
                   'Thuộc và vận dụng thành thạo bảng chia 2, 3, 4, 5 từ bảng nhân tương ứng.',
                   'Giải được các bài toán thực tế có một phép nhân hoặc một phép chia trong bảng 2, 3, 4, '
                   '5.'],
  'definition': '- **Bảng nhân $3$**: $3 \\times 1 = 3$, $3 \\times 2 = 6$, ..., $3 \\times 10 = 30$ (hai '
                'tích liên tiếp hơn kém nhau $3$ đơn vị).\n'
                '- **Bảng nhân $4$**: $4 \\times 1 = 4$, $4 \\times 2 = 8$, ..., $4 \\times 10 = 40$ (hai '
                'tích liên tiếp hơn kém nhau $4$ đơn vị).\n'
                '- **Bảng chia**: từ phép nhân $a \\times b = c$, ta suy ra phép chia $c : a = b$.',
  'theory': '### 1. Ôn tập bảng nhân, chia $2$ và $5$\n'
            '- Tích trong bảng nhân $2$ là các số chẵn từ $2$ đến $20$; tích trong bảng nhân $5$ có tận cùng '
            'là $0$ hoặc $5$.\n'
            '### 2. Bảng nhân $3$, bảng chia $3$\n'
            '- Ví dụ: $3 \\times 7 = 21 \\Rightarrow 21 : 3 = 7$; $3 \\times 8 = 24 \\Rightarrow 24 : 3 = '
            '8$.\n'
            '### 3. Bảng nhân $4$, bảng chia $4$\n'
            '- Ví dụ: $4 \\times 6 = 24 \\Rightarrow 24 : 4 = 6$; $4 \\times 9 = 36 \\Rightarrow 36 : 4 = '
            '9$.',
  'formulas': [{'category': 'I. Bảng nhân – chia 3',
                'items': [{'name': 'Bảng nhân 3', 'formula': '$3 \\times 1 = 3, \\dots, 3 \\times 10 = 30$'},
                          {'name': 'Bảng chia 3', 'formula': '$3 : 3 = 1, \\dots, 30 : 3 = 10$'}]},
               {'category': 'II. Bảng nhân – chia 4',
                'items': [{'name': 'Bảng nhân 4', 'formula': '$4 \\times 1 = 4, \\dots, 4 \\times 10 = 40$'},
                          {'name': 'Bảng chia 4', 'formula': '$4 : 4 = 1, \\dots, 40 : 4 = 10$'}]}],
  'example': 'Tính nhẩm: $3 \\times 9$, $4 \\times 7$, $24 : 3$, $32 : 4$.',
  'example_answer': '- $3 \\times 9 = 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$).\n'
                    '- $4 \\times 7 = 28$ và $32 : 4 = 8$ (vì $4 \\times 8 = 32$).',
  'real_life': '- Tính tổng số bánh khi mỗi hộp có $4$ cái bánh; chia đều $27$ học sinh thành $3$ hàng bằng '
               'nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $3 \\times 8$ là:',
            'options': ['$21$', '$27$', '$11$', '$24$'],
            'answer': 3,
            'solution': 'Theo bảng nhân $3$: $3 \\times 8 = 24$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $28 : 4$ là:',
            'options': ['$7$', '$6$', '$8$', '$24$'],
            'answer': 0,
            'solution': 'Vì $4 \\times 7 = 28$ nên $28 : 4 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Bảng nhân 3**?',
            'options': ['$3 : 3 = 1, \\dots, 30 : 3 = 10$',
                        '$3 \\times 1 = 3, \\dots, 3 \\times 10 = 30$',
                        '$4 \\times 1 = 4, \\dots, 4 \\times 10 = 40$',
                        '$4 : 4 = 1, \\dots, 40 : 4 = 10$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5, '
                        '**Bảng nhân 3** được xác định bởi: $3 \\times 1 = 3, \\dots, 3 \\times 10 = 30$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5**, nội dung/biểu thức $3 : 3 = 1, '
                 '\\dots, 30 : 3 = 10$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Bảng nhân 3', 'Bảng nhân 4', 'Bảng chia 3', 'Bảng chia 4'],
            'answer': 2,
            'solution': 'Trong Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5, biểu thức/quy tắc $3 : 3 = 1, '
                        '\\dots, 30 : 3 = 10$ chính là nội dung của **Bảng chia 3**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào ô trống trong phép tính $4 \\times 9 = 36 \\Rightarrow 36 : 4 = ?$ '
                 'là:',
            'options': ['$4$', '$6$', '$8$', '$9$'],
            'answer': 3,
            'solution': 'Từ $4 \\times 9 = 36$ suy ra $36 : 4 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5** (Chủ đề 1: Ôn tập và bổ sung), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Thuộc và vận dụng thành thạo bảng nhân 2, 3, 4, 5.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5: Thuộc và vận '
                        'dụng thành thạo bảng nhân 2, 3, 4, 5.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép tính $3 \\times 6$ và phép tính $2 \\times 9$ có cùng kết quả bằng $18$."',
            'answer': True,
            'solution': 'Ta có $3 \\times 6 = 18$ và $2 \\times 9 = 18$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5**, quy tắc **Bảng nhân 3** được xác '
                 'định bởi $3 \\times 1 = 3, \\dots, 3 \\times 10 = 30$ và áp dụng trực tiếp vào bài toán: '
                 '“Tính nhẩm: $3 \\times 9$, $4 \\times 7$, $24 : 3$, $32 : 4$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Bảng nhân 3** ($3 \\times 1 = 3, \\dots, 3 \\times '
                        '10 = 30$) là kiến thức cốt lõi của Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5. - '
                        '$3 \\times 9 = 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$). - $4 \\times 7 = 28$ và '
                        '$32 : 4 = 8$ (vì $4 \\times 8 = 32$).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5** để giải quyết tình '
                 'huống sau: Tính nhẩm: $3 \\times 9$, $4 \\times 7$, $24 : 3$, $32 : 4$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $3 \\times 9 = 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$). - $4 \\times 7 = 28$ '
                        'và $32 : 4 = 8$ (vì $4 \\times 8 = 32$).',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4, 5, 6: Bảng nhân, bảng chia 2, 3, 4, 5: - $3 \\times 9 '
                        '= 27$ và $24 : 3 = 8$ (vì $3 \\times 8 = 24$).\n'
                        '- $4 \\times 7 = 28$ và $32 : 4 = 8$ (vì $4 \\times 8 = 32$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có $27$ học sinh xếp đều thành $3$ hàng. Hỏi mỗi hàng có bao nhiêu học sinh?',
            'answer': ['9'],
            'unit': 'học sinh',
            'solution': 'Số học sinh ở mỗi hàng là: $27 : 3 = 9\\text{ (học sinh)}$.\n'
                        'Đáp số: **$9\\text{ học sinh}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 3 · Chủ đề 1: Ôn tập các số đến 1 000 và bảng nhân, chia 2, 3, 4, 5.',
  'title': 'Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung',
  'icon': '📏',
  'description': 'Ôn tập đường gấp khúc, hình tứ giác, khối trụ, khối cầu và các đơn vị đo độ dài, khối '
                 'lượng, dung tích.',
  'requirements': ['Tính được độ dài đường gấp khúc khi biết độ dài các đoạn thẳng thành phần.',
                   'Nhận dạng được hình tứ giác, khối trụ, khối cầu trong thực tế.',
                   'Chuyển đổi và tính toán được với các đơn vị đo độ dài ($\\text{cm}, \\text{dm}, '
                   '\\text{m}, \\text{km}$), khối lượng ($\\text{kg}$), dung tích ($\\text{l}$).'],
  'definition': '- **Độ dài đường gấp khúc** bằng tổng độ dài các đoạn thẳng tạo nên đường gấp khúc đó (cùng '
                'đơn vị đo).\n'
                '- **Quan hệ đơn vị độ dài**: $1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$; $1\\text{ km} '
                '= 1\\,000\\text{ m}$.',
  'theory': '### 1. Ôn tập hình học\n'
            '- Đường gấp khúc $ABCD$ gồm ba đoạn thẳng $AB$, $BC$, $CD$: độ dài đường gấp khúc là $AB + BC + '
            'CD$.\n'
            '- Hình tứ giác có $4$ đỉnh và $4$ cạnh. Khối cầu (quả bóng), khối trụ (hộp sữa, khúc gỗ tròn).\n'
            '### 2. Ôn tập đo lường\n'
            '- Độ dài: $1\\text{ dm} = 10\\text{ cm}$, $1\\text{ m} = 100\\text{ cm}$, $1\\text{ km} = '
            '1\\,000\\text{ m}$.\n'
            '- Khối lượng và dung tích: thực hiện cộng, trừ các số đo cùng đơn vị $\\text{kg}$ hoặc '
            '$\\text{l}$.',
  'formulas': [{'category': 'I. Đường gấp khúc',
                'items': [{'name': 'Độ dài đường gấp khúc',
                           'formula': '$L = a + b + c + \\dots$ (cùng đơn vị đo)'}]},
               {'category': 'II. Đổi đơn vị độ dài',
                'items': [{'name': 'Quy đổi',
                           'formula': '$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$ · $1\\text{ km} = '
                                      '1\\,000\\text{ m}$'}]}],
  'example': 'Tính độ dài đường gấp khúc $ABC$ biết $AB = 15\\text{ cm}$ và $BC = 2\\text{ dm}$.',
  'example_answer': 'Đổi $2\\text{ dm} = 20\\text{ cm}$.\n'
                    'Độ dài đường gấp khúc $ABC$ là: $15 + 20 = 35\\text{ (cm)}$.',
  'real_life': '- Đo chiều dài quãng đường đi qua nhiều ngã rẽ; ước lượng chiều cao bàn học, chiều dài sân '
               'trường.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ km}$ bằng bao nhiêu mét?',
            'options': ['$1\\,000\\text{ m}$', '$10\\text{ m}$', '$100\\text{ m}$', '$10\\,000\\text{ m}$'],
            'answer': 0,
            'solution': 'Ta có $1\\text{ km} = 1\\,000\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tứ giác có bao nhiêu cạnh?',
            'options': ['$3$ cạnh', '$4$ cạnh', '$5$ cạnh', '$6$ cạnh'],
            'answer': 1,
            'solution': 'Hình tứ giác có **$4$ cạnh** và $4$ đỉnh.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Độ dài đường gấp khúc**?',
            'options': ['$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$ · $1\\text{ km} = 1\\,000\\text{ m}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$L = a + b + c + \\dots$ (cùng đơn vị đo)',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 7, 8: Ôn tập hình học, đo lường và luyện tập '
                        'chung, **Độ dài đường gấp khúc** được xác định bởi: $L = a + b + c + \\dots$ (cùng '
                        'đơn vị đo).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung**, nội dung/biểu thức '
                 '$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$ · $1\\text{ km} = 1\\,000\\text{ m}$ là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Độ dài đường gấp khúc', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Quy đổi'],
            'answer': 3,
            'solution': 'Trong Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung, biểu thức/quy tắc '
                        '$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$ · $1\\text{ km} = 1\\,000\\text{ m}$ '
                        'chính là nội dung của **Quy đổi**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đường gấp khúc $MNP$ có $MN = 12\\text{ cm}$ và $NP = 18\\text{ cm}$. Độ dài đường gấp '
                 'khúc $MNP$ là:',
            'options': ['$30\\text{ cm}$', '$20\\text{ cm}$', '$6\\text{ cm}$', '$30\\text{ dm}$'],
            'answer': 0,
            'solution': 'Độ dài đường gấp khúc $MNP$ là: $12 + 18 = 30\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung** (Chủ đề 1: Ôn tập và bổ '
                 'sung), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Tính được độ dài đường gấp khúc khi biết độ dài các đoạn thẳng thành phần.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung: '
                        'Tính được độ dài đường gấp khúc khi biết độ dài các đoạn thẳng thành phần.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$3\\text{ m } 5\\text{ dm} = 35\\text{ dm}$."',
            'answer': True,
            'solution': 'Vì $3\\text{ m} = 30\\text{ dm}$ nên $30\\text{ dm} + 5\\text{ dm} = 35\\text{ dm}$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung**, quy tắc **Độ dài đường '
                 'gấp khúc** được xác định bởi $L = a + b + c + \\dots$ (cùng đơn vị đo) và áp dụng trực '
                 'tiếp vào bài toán: “Tính độ dài đường gấp khúc $ABC$ biết $AB = 15\\text{ cm}$ và $BC = '
                 '2\\text{ dm}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Độ dài đường gấp khúc** ($L = a + b + c + \\dots$ '
                        '(cùng đơn vị đo)) là kiến thức cốt lõi của Bài 7, 8: Ôn tập hình học, đo lường và '
                        'luyện tập chung. Đổi $2\\text{ dm} = 20\\text{ cm}$. Độ dài đường gấp khúc $ABC$ '
                        'là: $15 + 20 = 35\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung** để giải '
                 'quyết tình huống sau: Tính độ dài đường gấp khúc $ABC$ biết $AB = 15\\text{ cm}$ và $BC = '
                 '2\\text{ dm}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Đổi $2\\text{ dm} = 20\\text{ cm}$. Độ dài đường gấp khúc $ABC$ là: $15 + 20 = '
                        '35\\text{ (cm)}$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 7, 8: Ôn tập hình học, đo lường và luyện tập chung: Đổi '
                        '$2\\text{ dm} = 20\\text{ cm}$.\n'
                        'Độ dài đường gấp khúc $ABC$ là: $15 + 20 = 35\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đường gấp khúc gồm $4$ đoạn thẳng bằng nhau, mỗi đoạn dài $4\\text{ cm}$. Hỏi đường '
                 'gấp khúc đó dài bao nhiêu xăng-ti-mét?',
            'answer': ['16'],
            'unit': 'cm',
            'solution': 'Độ dài đường gấp khúc là: $4 \\times 4 = 16\\text{ (cm)}$.\n'
                        'Đáp số: **$16\\text{ cm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd02-bang-nhan-bang-chia',
  'context_title': 'Chủ đề 2: Bảng nhân, bảng chia',
  'context': 'SGK Toán 3 · Chủ đề 2: Bảng nhân, bảng chia 6, 7, 8, 9; tìm thành phần phép nhân, chia; một '
             'phần mấy.',
  'title': 'Bài 9, 10: Bảng nhân, bảng chia 6 và 7',
  'icon': '✖️',
  'description': 'Lập và vận dụng bảng nhân 6, bảng chia 6, bảng nhân 7, bảng chia 7 trong tính toán.',
  'requirements': ['Thuộc và tính nhẩm nhanh các phép tính trong bảng nhân 6, bảng chia 6.',
                   'Thuộc và tính nhẩm nhanh các phép tính trong bảng nhân 7, bảng chia 7.',
                   'Giải được bài toán thực tế liên quan đến bảng nhân, chia 6 và 7.'],
  'definition': '- **Bảng nhân $6$**: $6 \\times 1 = 6, 6 \\times 2 = 12, \\dots, 6 \\times 10 = 60$; từ đó '
                'suy ra **bảng chia $6$**.\n'
                '- **Bảng nhân $7$**: $7 \\times 1 = 7, 7 \\times 2 = 14, \\dots, 7 \\times 10 = 70$; từ đó '
                'suy ra **bảng chia $7$**.',
  'theory': '### 1. Bảng nhân $6$, bảng chia $6$\n'
            '- Hai tích liên tiếp trong bảng nhân $6$ hơn kém nhau $6$ đơn vị: $6, 12, 18, 24, 30, 36, 42, '
            '48, 54, 60$.\n'
            '- Ví dụ: $6 \\times 7 = 42 \\Rightarrow 42 : 6 = 7$ và $42 : 7 = 6$.\n'
            '### 2. Bảng nhân $7$, bảng chia $7$\n'
            '- Hai tích liên tiếp trong bảng nhân $7$ hơn kém nhau $7$ đơn vị: $7, 14, 21, 28, 35, 42, 49, '
            '56, 63, 70$.\n'
            '- Ví dụ: $7 \\times 8 = 56 \\Rightarrow 56 : 7 = 8$.',
  'formulas': [{'category': 'I. Bảng 6',
                'items': [{'name': 'Nhân – chia 6',
                           'formula': '$6 \\times 7 = 42 \\Leftrightarrow 42 : 6 = 7$ · $6 \\times 8 = 48 '
                                      '\\Leftrightarrow 48 : 6 = 8$'}]},
               {'category': 'II. Bảng 7',
                'items': [{'name': 'Nhân – chia 7',
                           'formula': '$7 \\times 7 = 49 \\Leftrightarrow 49 : 7 = 7$ · $7 \\times 8 = 56 '
                                      '\\Leftrightarrow 56 : 7 = 8$'}]}],
  'example': 'Tính nhẩm: $6 \\times 9$, $54 : 6$, $7 \\times 6$, $63 : 7$.',
  'example_answer': '- $6 \\times 9 = 54 \\Rightarrow 54 : 6 = 9$.\n'
                    '- $7 \\times 6 = 42$ và $63 : 7 = 9$ (vì $7 \\times 9 = 63$).',
  'real_life': '- Một tuần lễ có $7$ ngày: tính số ngày trong $4$ tuần ($7 \\times 4 = 28$ ngày); đóng gói '
               'các lốc sữa $6$ hộp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $6 \\times 7$ là:',
            'options': ['$36$', '$42$', '$48$', '$13$'],
            'answer': 1,
            'solution': 'Theo bảng nhân $6$: $6 \\times 7 = 42$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $56 : 7$ là:',
            'options': ['$6$', '$7$', '$8$', '$9$'],
            'answer': 2,
            'solution': 'Vì $7 \\times 8 = 56$ nên $56 : 7 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 9, 10: Bảng nhân, bảng chia 6 và 7**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Nhân – chia 6**?',
            'options': ['$7 \\times 7 = 49 \\Leftrightarrow 49 : 7 = 7$ · $7 \\times 8 = 56 \\Leftrightarrow '
                        '56 : 7 = 8$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$6 \\times 7 = 42 \\Leftrightarrow 42 : 6 = 7$ · $6 \\times 8 = 48 \\Leftrightarrow '
                        '48 : 6 = 8$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 9, 10: Bảng nhân, bảng chia 6 và 7, **Nhân – '
                        'chia 6** được xác định bởi: $6 \\times 7 = 42 \\Leftrightarrow 42 : 6 = 7$ · $6 '
                        '\\times 8 = 48 \\Leftrightarrow 48 : 6 = 8$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9, 10: Bảng nhân, bảng chia 6 và 7**, nội dung/biểu thức $7 \\times 7 = 49 '
                 '\\Leftrightarrow 49 : 7 = 7$ · $7 \\times 8 = 56 \\Leftrightarrow 56 : 7 = 8$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Nhân – chia 7', 'Nhân – chia 6', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 9, 10: Bảng nhân, bảng chia 6 và 7, biểu thức/quy tắc $7 \\times 7 = 49 '
                        '\\Leftrightarrow 49 : 7 = 7$ · $7 \\times 8 = 56 \\Leftrightarrow 56 : 7 = 8$ chính '
                        'là nội dung của **Nhân – chia 7**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong4 tuần lễ có tất cả bao nhiêu ngày?',
            'options': ['$24$ ngày', '$28$ ngày', '$35$ ngày', '$11$ ngày'],
            'answer': 1,
            'solution': 'Mỗi tuần có $7$ ngày nên $4$ tuần có: $7 \\times 4 = 28\\text{ (ngày)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 9, 10: Bảng nhân, bảng chia 6 và 7** (Chủ đề 2: Bảng nhân, bảng chia), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Thuộc và tính nhẩm nhanh các phép tính trong bảng nhân 6, bảng chia 6.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 9, 10: Bảng nhân, bảng chia 6 và 7: Thuộc và tính nhẩm '
                        'nhanh các phép tính trong bảng nhân 6, bảng chia 6.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $48 : 6$ có kết quả bằng $7$."',
            'answer': False,
            'solution': 'Vì $6 \\times 8 = 48$ nên $48 : 6 = 8$, không phải $7$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 9, 10: Bảng nhân, bảng chia 6 và 7**, quy tắc **Nhân – chia 6** được xác định '
                 'bởi $6 \\times 7 = 42 \\Leftrightarrow 42 : 6 = 7$ · $6 \\times 8 = 48 \\Leftrightarrow 48 '
                 ': 6 = 8$ và áp dụng trực tiếp vào bài toán: “Tính nhẩm: $6 \\times 9$, $54 : 6$, $7 '
                 '\\times 6$, $63 : 7$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhân – chia 6** ($6 \\times 7 = 42 \\Leftrightarrow '
                        '42 : 6 = 7$ · $6 \\times 8 = 48 \\Leftrightarrow 48 : 6 = 8$) là kiến thức cốt lõi '
                        'của Bài 9, 10: Bảng nhân, bảng chia 6 và 7. - $6 \\times 9 = 54 \\Rightarrow 54 : 6 '
                        '= 9$. - $7 \\times 6 = 42$ và $63 : 7 = 9$ (vì $7 \\times 9 = 63$).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 9, 10: Bảng nhân, bảng chia 6 và 7** để giải quyết tình huống '
                 'sau: Tính nhẩm: $6 \\times 9$, $54 : 6$, $7 \\times 6$, $63 : 7$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        '- $6 \\times 9 = 54 \\Rightarrow 54 : 6 = 9$. - $7 \\times 6 = 42$ và $63 : 7 = 9$ '
                        '(vì $7 \\times 9 = 63$).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 9, 10: Bảng nhân, bảng chia 6 và 7: - $6 \\times 9 = 54 '
                        '\\Rightarrow 54 : 6 = 9$.\n'
                        '- $7 \\times 6 = 42$ và $63 : 7 = 9$ (vì $7 \\times 9 = 63$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có $42$ quả cam xếp đều vào $6$ đĩa. Hỏi mỗi đĩa có bao nhiêu quả cam?',
            'answer': ['7'],
            'unit': 'quả',
            'solution': 'Số quả cam ở mỗi đĩa là: $42 : 6 = 7\\text{ (quả)}$.\nĐáp số: **$7\\text{ quả}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd02-bang-nhan-bang-chia',
  'context_title': 'Chủ đề 2: Bảng nhân, bảng chia',
  'context': 'SGK Toán 3 · Chủ đề 2: Bảng nhân, bảng chia 6, 7, 8, 9; tìm thành phần phép nhân, chia; một '
             'phần mấy.',
  'title': 'Bài 11: Bảng nhân 8, bảng chia 8',
  'icon': '🎱',
  'description': 'Lập và vận dụng bảng nhân 8, bảng chia 8 vào thực hành tính và giải toán.',
  'requirements': ['Lập và học thuộc bảng nhân 8, bảng chia 8.',
                   'Tính nhẩm nhanh các phép nhân, phép chia trong bảng 8.',
                   'Giải được bài toán có lời văn liên quan đến bảng nhân 8, bảng chia 8.'],
  'definition': '- **Bảng nhân $8$**: $8 \\times 1 = 8, 8 \\times 2 = 16, \\dots, 8 \\times 10 = 80$ (mỗi '
                'lần thêm $8$ đơn vị).\n'
                '- **Bảng chia $8$**: lập từ bảng nhân $8$, với $8 : 8 = 1, 16 : 8 = 2, \\dots, 80 : 8 = '
                '10$.',
  'theory': '### 1. Bảng nhân $8$\n'
            '- Các tích trong bảng nhân $8$ lần lượt là: $8, 16, 24, 32, 40, 48, 56, 64, 72, 80$.\n'
            '- Lưu ý các phép nhân dễ nhầm: $8 \\times 6 = 48$, $8 \\times 7 = 56$, $8 \\times 8 = 64$, $8 '
            '\\times 9 = 72$.\n'
            '### 2. Bảng chia $8$\n'
            '- Từ $8 \\times 9 = 72$, ta có ngay $72 : 8 = 9$.',
  'formulas': [{'category': 'I. Bảng nhân – chia 8',
                'items': [{'name': 'Các tích trọng tâm',
                           'formula': '$8 \\times 6 = 48$ · $8 \\times 7 = 56$ · $8 \\times 8 = 64$ · $8 '
                                      '\\times 9 = 72$'},
                          {'name': 'Quan hệ nhân – chia',
                           'formula': '$8 \\times n = P \\Leftrightarrow P : 8 = n$'}]}],
  'example': 'Mỗi hộp có $8$ cái bánh. Hỏi $6$ hộp như thế có bao nhiêu cái bánh?',
  'example_answer': 'Số cái bánh trong $6$ hộp là: $8 \\times 6 = 48\\text{ (cái bánh)}$.\n'
                    'Đáp số: **$48\\text{ cái bánh}$**.',
  'real_life': '- Đếm số chân của các con cua hoặc con nhện (mỗi con nhện có $8$ chân); chia bánh trung thu '
               'theo hộp $8$ chiếc.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $8 \\times 8$ là:',
            'options': ['$16$', '$56$', '$64$', '$72$'],
            'answer': 2,
            'solution': 'Theo bảng nhân $8$: $8 \\times 8 = 64$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $72 : 8$ là:',
            'options': ['$7$', '$8$', '$6$', '$9$'],
            'answer': 3,
            'solution': 'Vì $8 \\times 9 = 72$ nên $72 : 8 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 11: Bảng nhân 8, bảng chia 8**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Các tích trọng tâm**?',
            'options': ['$8 \\times 6 = 48$ · $8 \\times 7 = 56$ · $8 \\times 8 = 64$ · $8 \\times 9 = 72$',
                        '$8 \\times n = P \\Leftrightarrow P : 8 = n$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 11: Bảng nhân 8, bảng chia 8, **Các tích '
                        'trọng tâm** được xác định bởi: $8 \\times 6 = 48$ · $8 \\times 7 = 56$ · $8 \\times '
                        '8 = 64$ · $8 \\times 9 = 72$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Bảng nhân 8, bảng chia 8**, nội dung/biểu thức $8 \\times n = P '
                 '\\Leftrightarrow P : 8 = n$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Các tích trọng tâm',
                        'Quan hệ nhân – chia',
                        'Phân tích số',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 11: Bảng nhân 8, bảng chia 8, biểu thức/quy tắc $8 \\times n = P '
                        '\\Leftrightarrow P : 8 = n$ chính là nội dung của **Quan hệ nhân – chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm trong dãy số $8, 16, 24, 32, \\dots, 48$ là:',
            'options': ['$36$', '$42$', '$40$', '$44$'],
            'answer': 2,
            'solution': 'Dãy các tích trong bảng nhân $8$: $32 + 8 = 40$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Bảng nhân 8, bảng chia 8** (Chủ đề 2: Bảng nhân, bảng chia), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Lập và học thuộc bảng nhân 8, bảng chia 8.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 11: Bảng nhân 8, bảng chia 8: Lập và học thuộc bảng '
                        'nhân 8, bảng chia 8.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$8 \\times 7 = 54$."',
            'answer': False,
            'solution': 'Ta có $8 \\times 7 = 56$ (còn $54 = 6 \\times 9$) $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 11: Bảng nhân 8, bảng chia 8**, quy tắc **Các tích trọng tâm** được xác định '
                 'bởi $8 \\times 6 = 48$ · $8 \\times 7 = 56$ · $8 \\times 8 = 64$ · $8 \\times 9 = 72$ và '
                 'áp dụng trực tiếp vào bài toán: “Mỗi hộp có $8$ cái bánh. Hỏi $6$ hộp như thế có bao nhiêu '
                 'cái bánh?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Các tích trọng tâm** ($8 \\times 6 = 48$ · $8 '
                        '\\times 7 = 56$ · $8 \\times 8 = 64$ · $8 \\times 9 = 72$) là kiến thức cốt lõi của '
                        'Bài 11: Bảng nhân 8, bảng chia 8. Số cái bánh trong $6$ hộp là: $8 \\times 6 = '
                        '48\\text{ (cái bánh)}$. Đáp số: **$48\\text{ cái bánh}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 11: Bảng nhân 8, bảng chia 8** để giải quyết tình huống sau: Mỗi '
                 'hộp có $8$ cái bánh. Hỏi $6$ hộp như thế có bao nhiêu cái bánh? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Số cái bánh trong $6$ hộp là: $8 \\times 6 = 48\\text{ (cái bánh)}$. Đáp số: '
                        '**$48\\text{ cái bánh}$**.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Bảng nhân 8, bảng chia 8: Số cái bánh trong $6$ hộp '
                        'là: $8 \\times 6 = 48\\text{ (cái bánh)}$.\n'
                        'Đáp số: **$48\\text{ cái bánh}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cô giáo chia đều $40$ quyển vở cho $8$ bạn học sinh giỏi. Hỏi mỗi bạn nhận được bao nhiêu '
                 'quyển vở?',
            'answer': ['5'],
            'unit': 'quyển',
            'solution': 'Mỗi bạn nhận được số quyển vở là: $40 : 8 = 5\\text{ (quyển)}$.\n'
                        'Đáp số: **$5\\text{ quyển}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd02-bang-nhan-bang-chia',
  'context_title': 'Chủ đề 2: Bảng nhân, bảng chia',
  'context': 'SGK Toán 3 · Chủ đề 2: Bảng nhân, bảng chia 6, 7, 8, 9; tìm thành phần phép nhân, chia; một '
             'phần mấy.',
  'title': 'Bài 12: Bảng nhân 9, bảng chia 9',
  'icon': '9️⃣',
  'description': 'Lập và vận dụng bảng nhân 9, bảng chia 9 cùng mẹo nhẩm nhanh bảng 9.',
  'requirements': ['Thuộc bảng nhân 9 và bảng chia 9.',
                   'Nhận biết đặc điểm tổng hai chữ số của tích trong bảng nhân 9 luôn bằng 9.',
                   'Vận dụng bảng nhân 9, chia 9 để giải bài toán thực tiễn.'],
  'definition': '- **Bảng nhân $9$**: $9 \\times 1 = 9, 9 \\times 2 = 18, \\dots, 9 \\times 10 = 90$.\n'
                '- **Mẹo nhớ nhanh**: $9 \\times n = 10 \\times n - n$ (ví dụ $9 \\times 7 = 70 - 7 = 63$).',
  'theory': '### 1. Bảng nhân $9$\n'
            '- Các tích trong bảng nhân $9$: $9, 18, 27, 36, 45, 54, 63, 72, 81, 90$.\n'
            '- Đặc điểm thú vị: chữ số hàng chục tăng dần từ $0$ đến $9$, chữ số hàng đơn vị giảm dần từ $9$ '
            'về $0$, tổng hai chữ số luôn bằng $9$.\n'
            '### 2. Bảng chia $9$\n'
            '- Lập từ bảng nhân $9$: $9 : 9 = 1, 18 : 9 = 2, \\dots, 81 : 9 = 9, 90 : 9 = 10$.',
  'formulas': [{'category': 'I. Bảng nhân – chia 9',
                'items': [{'name': 'Mẹo tính nhẩm',
                           'formula': '$9 \\times n = 10 \\times n - n$',
                           'note': 'Ví dụ: $9 \\times 8 = 80 - 8 = 72$'},
                          {'name': 'Chia cho 9',
                           'formula': '$9 \\times n = P \\Leftrightarrow P : 9 = n$'}]}],
  'example': 'Tính: $9 \\times 6$, $9 \\times 9$, $54 : 9$, $81 : 9$.',
  'example_answer': '- $9 \\times 6 = 54$ nên $54 : 9 = 6$.\n- $9 \\times 9 = 81$ nên $81 : 9 = 9$.',
  'real_life': '- Chia đều $36$ vận động viên vào $9$ làn bơi; tính số cây trồng trên $9$ hàng đều nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $9 \\times 9$ là:',
            'options': ['$18$', '$72$', '$99$', '$81$'],
            'answer': 3,
            'solution': 'Theo bảng nhân $9$: $9 \\times 9 = 81$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $63 : 9$ là:',
            'options': ['$7$', '$6$', '$8$', '$9$'],
            'answer': 0,
            'solution': 'Vì $9 \\times 7 = 63$ nên $63 : 9 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 12: Bảng nhân 9, bảng chia 9**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Mẹo tính nhẩm**?',
            'options': ['$9 \\times n = P \\Leftrightarrow P : 9 = n$',
                        '$9 \\times n = 10 \\times n - n$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 12: Bảng nhân 9, bảng chia 9, **Mẹo tính '
                        'nhẩm** được xác định bởi: $9 \\times n = 10 \\times n - n$. (Ví dụ: $9 \\times 8 = '
                        '80 - 8 = 72$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Bảng nhân 9, bảng chia 9**, nội dung/biểu thức $9 \\times n = P '
                 '\\Leftrightarrow P : 9 = n$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Mẹo tính nhẩm', 'Phân tích số', 'Chia cho 9', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 12: Bảng nhân 9, bảng chia 9, biểu thức/quy tắc $9 \\times n = P '
                        '\\Leftrightarrow P : 9 = n$ chính là nội dung của **Chia cho 9**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tích của $9$ và số lớn nhất có một chữ số là:',
            'options': ['$90$', '$72$', '$18$', '$81$'],
            'answer': 3,
            'solution': 'Số lớn nhất có một chữ số là $9$. Tích là $9 \\times 9 = 81$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Bảng nhân 9, bảng chia 9** (Chủ đề 2: Bảng nhân, bảng chia), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Thuộc bảng nhân 9 và bảng chia 9.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 12: Bảng nhân 9, bảng chia 9: Thuộc bảng nhân 9 và '
                        'bảng chia 9.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong bảng nhân $9$ (từ $9 \\times 1$ đến $9 \\times 10$), tổng hai chữ số của '
                 'mỗi tích luôn bằng $9$."',
            'answer': True,
            'solution': 'Ví dụ $1+8=9, 2+7=9, \\dots, 8+1=9, 9+0=9$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 12: Bảng nhân 9, bảng chia 9**, quy tắc **Mẹo tính nhẩm** được xác định bởi $9 '
                 '\\times n = 10 \\times n - n$ và áp dụng trực tiếp vào bài toán: “Tính: $9 \\times 6$, $9 '
                 '\\times 9$, $54 : 9$, $81 : 9$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Mẹo tính nhẩm** ($9 \\times n = 10 \\times n - n$) '
                        'là kiến thức cốt lõi của Bài 12: Bảng nhân 9, bảng chia 9. - $9 \\times 6 = 54$ nên '
                        '$54 : 9 = 6$. - $9 \\times 9 = 81$ nên $81 : 9 = 9$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 12: Bảng nhân 9, bảng chia 9** để giải quyết tình huống sau: '
                 'Tính: $9 \\times 6$, $9 \\times 9$, $54 : 9$, $81 : 9$. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $9 \\times 6 = 54$ nên $54 : 9 = 6$. - $9 \\times 9 = 81$ nên $81 : 9 = 9$.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Bảng nhân 9, bảng chia 9: - $9 \\times 6 = 54$ nên '
                        '$54 : 9 = 6$.\n'
                        '- $9 \\times 9 = 81$ nên $81 : 9 = 9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đội tình nguyện có $45$ người được chia đều thành $9$ nhóm. Hỏi mỗi nhóm có bao nhiêu '
                 'người?',
            'answer': ['5'],
            'unit': 'người',
            'solution': 'Số người ở mỗi nhóm là: $45 : 9 = 5\\text{ (người)}$.\n'
                        'Đáp số: **$5\\text{ người}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd02-bang-nhan-bang-chia',
  'context_title': 'Chủ đề 2: Bảng nhân, bảng chia',
  'context': 'SGK Toán 3 · Chủ đề 2: Bảng nhân, bảng chia 6, 7, 8, 9; tìm thành phần phép nhân, chia; một '
             'phần mấy.',
  'title': 'Bài 13: Tìm thành phần trong phép nhân, phép chia',
  'icon': '🧩',
  'description': 'Quy tắc tìm thừa số chưa biết trong phép nhân, tìm số bị chia và số chia trong phép chia.',
  'requirements': ['Tìm được thừa số chưa biết khi biết tích và thừa số kia.',
                   'Tìm được số bị chia hoặc số chia chưa biết trong phép chia hết.',
                   'Giải được bài toán thực tế vận dụng quy tắc tìm thành phần phép nhân, chia.'],
  'definition': '- **Tìm thừa số** ($x \\times a = b$): Muốn tìm một thừa số, ta lấy tích chia cho thừa số '
                'kia ($x = b : a$).\n'
                '- **Tìm số bị chia** ($x : a = b$): Muốn tìm số bị chia, ta lấy thương nhân với số chia ($x '
                '= b \\times a$).\n'
                '- **Tìm số chia** ($a : x = b$): Muốn tìm số chia, ta lấy số bị chia chia cho thương ($x = '
                'a : b$).',
  'theory': '### 1. Tìm thừa số trong phép nhân\n'
            '- Phép nhân: $\\text{Thừa số} \\times \\text{Thừa số} = \\text{Tích}$.\n'
            '- Ví dụ: $? \\times 6 = 54 \\Rightarrow ? = 54 : 6 = 9$.\n'
            '### 2. Tìm số bị chia và số chia trong phép chia\n'
            '- Phép chia hết: $\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$.\n'
            '- Tìm số bị chia: $? : 7 = 5 \\Rightarrow ? = 5 \\times 7 = 35$.\n'
            '- Tìm số chia: $48 : ? = 8 \\Rightarrow ? = 48 : 8 = 6$.',
  'formulas': [{'category': 'I. Phép nhân',
                'items': [{'name': 'Tìm thừa số',
                           'formula': '$\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$'}]},
               {'category': 'II. Phép chia',
                'items': [{'name': 'Tìm số bị chia',
                           'formula': '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia}$'},
                          {'name': 'Tìm số chia',
                           'formula': '$\\text{Số chia} = \\text{Số bị chia} : \\text{Thương}$'}]}],
  'example': 'Tìm thành phần chưa biết: a) $? : 8 = 7$; b) $63 : ? = 9$.',
  'example_answer': 'a) Số bị chia $= \\text{Thương} \\times \\text{Số chia} = 7 \\times 8 = 56$.\n'
                    'b) Số chia $= \\text{Số bị chia} : \\text{Thương} = 63 : 9 = 7$.',
  'real_life': '- Biết tổng số kẹo chia đều cho mỗi bạn được $5$ cái, tìm tổng số kẹo ban đầu hoặc số bạn '
               'được chia.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn tìm một thừa số chưa biết, ta lấy:',
            'options': ['Tích chia cho thừa số kia',
                        'Tích nhân với thừa số kia',
                        'Tích trừ đi thừa số kia',
                        'Thừa số kia chia cho tích'],
            'answer': 0,
            'solution': 'Theo quy tắc: $\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm số chia trong phép tính $63 : ? = 9$:',
            'options': ['$8$', '$7$', '$54$', '$72$'],
            'answer': 1,
            'solution': 'Số chia $= 63 : 9 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 13: Tìm thành phần trong phép nhân, phép chia**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Tìm thừa số**?',
            'options': ['$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia}$',
                        '$\\text{Số chia} = \\text{Số bị chia} : \\text{Thương}$',
                        '$\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 13: Tìm thành phần trong phép nhân, phép '
                        'chia, **Tìm thừa số** được xác định bởi: $\\text{Thừa số} = \\text{Tích} : '
                        '\\text{Thừa số kia}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Tìm thành phần trong phép nhân, phép chia**, nội dung/biểu thức $\\text{Số '
                 'bị chia} = \\text{Thương} \\times \\text{Số chia}$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Tìm thừa số', 'Tìm số chia', 'Phân tích số', 'Tìm số bị chia'],
            'answer': 3,
            'solution': 'Trong Bài 13: Tìm thành phần trong phép nhân, phép chia, biểu thức/quy tắc '
                        '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia}$ chính là nội dung của '
                        '**Tìm số bị chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số bị chia $x$ biết $x : 6 = 8$:',
            'options': ['$48$', '$14$', '$42$', '$56$'],
            'answer': 0,
            'solution': 'Số bị chia $x = 8 \\times 6 = 48$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Tìm thành phần trong phép nhân, phép chia** (Chủ đề 2: Bảng nhân, bảng '
                 'chia), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Tìm được thừa số chưa biết khi biết tích và thừa số kia.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 13: Tìm thành phần trong phép nhân, phép chia: Tìm '
                        'được thừa số chưa biết khi biết tích và thừa số kia.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong phép tính $? \\times 7 = 49$, số cần tìm là $7$."',
            'answer': True,
            'solution': 'Thừa số cần tìm là $49 : 7 = 7$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 13: Tìm thành phần trong phép nhân, phép chia**, quy tắc **Tìm thừa số** được '
                 'xác định bởi $\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$ và áp dụng trực tiếp '
                 'vào bài toán: “Tìm thành phần chưa biết: a) $? : 8 = 7$; b) $63 : ? = 9$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tìm thừa số** ($\\text{Thừa số} = \\text{Tích} : '
                        '\\text{Thừa số kia}$) là kiến thức cốt lõi của Bài 13: Tìm thành phần trong phép '
                        'nhân, phép chia. a) Số bị chia $= \\text{Thương} \\times \\text{Số chia} = 7 '
                        '\\times 8 = 56$. b) Số chia $= \\text{Số bị chia} : \\text{Thương} = 63 : 9 = 7$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 13: Tìm thành phần trong phép nhân, phép chia** để giải quyết '
                 'tình huống sau: Tìm thành phần chưa biết: a) $? : 8 = 7$; b) $63 : ? = 9$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'a) Số bị chia $= \\text{Thương} \\times \\text{Số chia} = 7 \\times 8 = 56$. b) Số '
                        'chia $= \\text{Số bị chia} : \\text{Thương} = 63 : 9 = 7$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Tìm thành phần trong phép nhân, phép chia: a) Số bị '
                        'chia $= \\text{Thương} \\times \\text{Số chia} = 7 \\times 8 = 56$.\n'
                        'b) Số chia $= \\text{Số bị chia} : \\text{Thương} = 63 : 9 = 7$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bà chia đều một số quả táo cho $6$ cháu thì mỗi cháu được $8$ quả. Hỏi lúc đầu bà có bao '
                 'nhiêu quả táo?',
            'answer': ['48'],
            'unit': 'quả',
            'solution': 'Số quả táo lúc đầu (số bị chia) là: $8 \\times 6 = 48\\text{ (quả)}$.\n'
                        'Đáp số: **$48\\text{ quả}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd02-bang-nhan-bang-chia',
  'context_title': 'Chủ đề 2: Bảng nhân, bảng chia',
  'context': 'SGK Toán 3 · Chủ đề 2: Bảng nhân, bảng chia 6, 7, 8, 9; tìm thành phần phép nhân, chia; một '
             'phần mấy.',
  'title': 'Bài 14, 15: Một phần mấy và luyện tập chung',
  'icon': '🍰',
  'description': 'Nhận biết một phần mấy (từ 1/2 đến 1/9) của một hình hoặc một nhóm đồ vật.',
  'requirements': ['Nhận biết được $\\dfrac{1}{2}, \\dfrac{1}{3}, \\dots, \\dfrac{1}{9}$ qua hình ảnh trực '
                   'quan.',
                   'Tìm được một phần mấy của một số bằng phép chia.',
                   'Giải được bài toán thực tế về tìm một phần mấy của một số.'],
  'definition': '- Chia một hình (hoặc một nhóm đồ vật) thành $n$ phần **bằng nhau**, lấy ra $1$ phần thì '
                'được **một phần $n$**, viết là $\\dfrac{1}{n}$.\n'
                '- **Tìm $\\dfrac{1}{n}$ của một số**: Muốn tìm $\\dfrac{1}{n}$ của một số, ta lấy số đó '
                '**chia cho $n$**.',
  'theory': '### 1. Nhận biết một phần mấy\n'
            '- Chia chiếc bánh thành $4$ phần bằng nhau, lấy $1$ phần ta được $\\dfrac{1}{4}$ (một phần tư) '
            'chiếc bánh.\n'
            '- Lưu ý: Các phần được chia bắt buộc phải **bằng nhau**.\n'
            '### 2. Tìm một phần mấy của một số\n'
            '- Ví dụ: $\\dfrac{1}{4}$ của $20$ cái kẹo là $20 : 4 = 5$ (cái kẹo).\n'
            '- Ví dụ: $\\dfrac{1}{6}$ của $42\\text{ l}$ nước là $42 : 6 = 7\\text{ (l)}$.',
  'formulas': [{'category': 'I. Một phần mấy',
                'items': [{'name': 'Ký hiệu',
                           'formula': '$\\dfrac{1}{n}$ đọc là "một phần $n$" ($n = 2, 3, \\dots, 9$)'},
                          {'name': 'Tìm 1/n của số a',
                           'formula': '$\\dfrac{1}{n} \\text{ của } a = a : n$',
                           'note': 'Ví dụ: $\\dfrac{1}{3}$ của $18$ là $18 : 3 = 6$'}]}],
  'example': 'Lớp 3A có $35$ học sinh, trong đó $\\dfrac{1}{7}$ số học sinh đạt giải Cờ vua. Hỏi lớp 3A có '
             'bao nhiêu học sinh đạt giải?',
  'example_answer': 'Số học sinh đạt giải Cờ vua là: $35 : 7 = 5\\text{ (học sinh)}$.\n'
                    'Đáp số: **$5\\text{ học sinh}$**.',
  'real_life': '- Chia đôi ($\\dfrac{1}{2}$) chiếc bánh pizza, chia $\\dfrac{1}{4}$ thời gian buổi tối để '
               'đọc sách.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một phần năm được viết là:',
            'options': ['$\\dfrac{5}{1}$', '$\\dfrac{1}{5}$', '$15$', '$5$'],
            'answer': 1,
            'solution': 'Một phần năm viết là **$\\dfrac{1}{5}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn tìm $\\dfrac{1}{6}$ của $42\\text{ l}$ nước, ta thực hiện phép tính:',
            'options': ['$42 \\times 6$', '$42 - 6$', '$42 : 6$', '$42 + 6$'],
            'answer': 2,
            'solution': 'Ta lấy $42 : 6 = 7\\text{ (l)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 14, 15: Một phần mấy và luyện tập chung**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Ký hiệu**?',
            'options': ['$\\dfrac{1}{n} \\text{ của } a = a : n$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$\\dfrac{1}{n}$ đọc là "một phần $n$" ($n = 2, 3, \\dots, 9$)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 14, 15: Một phần mấy và luyện tập chung, **Ký '
                        'hiệu** được xác định bởi: $\\dfrac{1}{n}$ đọc là "một phần $n$" ($n = 2, 3, \\dots, '
                        '9$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14, 15: Một phần mấy và luyện tập chung**, nội dung/biểu thức $\\dfrac{1}{n} '
                 '\\text{ của } a = a : n$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tìm 1/n của số a', 'Ký hiệu', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 14, 15: Một phần mấy và luyện tập chung, biểu thức/quy tắc $\\dfrac{1}{n} '
                        '\\text{ của } a = a : n$ chính là nội dung của **Tìm 1/n của số a**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': '$\\dfrac{1}{8}$ của $56\\text{ kg}$ gạo là:',
            'options': ['$6\\text{ kg}$', '$7\\text{ kg}$', '$8\\text{ kg}$', '$48\\text{ kg}$'],
            'answer': 1,
            'solution': 'Ta có $56 : 8 = 7\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 14, 15: Một phần mấy và luyện tập chung** (Chủ đề 2: Bảng nhân, bảng chia), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Nhận biết được $\\dfrac{1}{2}, \\dfrac{1}{3}, \\dots, \\dfrac{1}{9}$ qua hình ảnh '
                        'trực quan.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 14, 15: Một phần mấy và luyện tập chung: Nhận biết '
                        'được $\\dfrac{1}{2}, \\dfrac{1}{3}, \\dots, \\dfrac{1}{9}$ qua hình ảnh trực quan.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Chia một hình vuông thành $5$ phần bằng nhau, tô màu $1$ phần thì đã tô màu '
                 '$\\dfrac{1}{5}$ hình vuông đó."',
            'answer': True,
            'solution': 'Chia $5$ phần bằng nhau, lấy $1$ phần chính là $\\dfrac{1}{5}$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 14, 15: Một phần mấy và luyện tập chung**, quy tắc **Ký hiệu** được xác định '
                 'bởi $\\dfrac{1}{n}$ đọc là "một phần $n$" ($n = 2, 3, \\dots, 9$) và áp dụng trực tiếp vào '
                 'bài toán: “Lớp 3A có $35$ học sinh, trong đó $\\dfrac{1}{7}$ số học sinh đạt giải Cờ vua. '
                 'Hỏi lớp 3A có bao nhiêu học sinh đạt giải?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Ký hiệu** ($\\dfrac{1}{n}$ đọc là "một phần $n$" ($n '
                        '= 2, 3, \\dots, 9$)) là kiến thức cốt lõi của Bài 14, 15: Một phần mấy và luyện tập '
                        'chung. Số học sinh đạt giải Cờ vua là: $35 : 7 = 5\\text{ (học sinh)}$. Đáp số: '
                        '**$5\\text{ học sinh}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 14, 15: Một phần mấy và luyện tập chung** để giải quyết tình '
                 'huống sau: Lớp 3A có $35$ học sinh, trong đó $\\dfrac{1}{7}$ số học sinh đạt giải Cờ vua. '
                 'Hỏi lớp 3A có bao nhiêu học sinh đạt giải? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Số học sinh đạt giải Cờ vua là: $35 : 7 = 5\\text{ (học sinh)}$. Đáp số: '
                        '**$5\\text{ học sinh}$**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14, 15: Một phần mấy và luyện tập chung: Số học sinh đạt '
                        'giải Cờ vua là: $35 : 7 = 5\\text{ (học sinh)}$.\n'
                        'Đáp số: **$5\\text{ học sinh}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mẹ hái được $36$ quả xoài, mẹ biếu bà $\\dfrac{1}{4}$ số xoài đó. Hỏi mẹ đã biếu bà bao '
                 'nhiêu quả xoài?',
            'answer': ['9'],
            'unit': 'quả',
            'solution': 'Số quả xoài mẹ biếu bà là: $36 : 4 = 9\\text{ (quả)}$.\n'
                        'Đáp số: **$9\\text{ quả}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd03-hinh-phang-hinh-khoi',
  'context_title': 'Chủ đề 3: Làm quen với hình phẳng, hình khối',
  'context': 'SGK Toán 3 · Chủ đề 3: Làm quen với hình phẳng và hình khối.',
  'title': 'Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng',
  'icon': '📍',
  'description': 'Nhận biết ba điểm thẳng hàng, điểm ở giữa hai điểm và trung điểm của đoạn thẳng.',
  'requirements': ['Xác định được điểm ở giữa hai điểm cho trước trên một đường thẳng.',
                   'Nhận biết và xác định được trung điểm của một đoạn thẳng.',
                   'Tính được độ dài nửa đoạn thẳng khi biết trung điểm.'],
  'definition': '- **Điểm ở giữa**: Với ba điểm $A, O, B$ thẳng hàng theo thứ tự đó, $O$ là điểm ở giữa hai '
                'điểm $A$ và $B$.\n'
                '- **Trung điểm**: Điểm $M$ là trung điểm của đoạn thẳng $AB$ nếu $M$ nằm giữa $A, B$ và $MA '
                '= MB$.',
  'theory': '### 1. Điểm ở giữa hai điểm\n'
            '- Điều kiện cần là ba điểm phải **cùng nằm trên một đường thẳng**.\n'
            '### 2. Trung điểm của đoạn thẳng\n'
            '- Trung điểm chia đoạn thẳng thành hai phần dài bằng nhau: $MA = MB = AB : 2$.\n'
            '- Mọi trung điểm đều là điểm ở giữa, nhưng điểm ở giữa chưa chắc là trung điểm (nếu hai đoạn '
            'không bằng nhau).',
  'formulas': [{'category': 'I. Trung điểm đoạn thẳng',
                'items': [{'name': 'Điều kiện', 'formula': '$M$ ở giữa $A, B$ và $MA = MB$'},
                          {'name': 'Tính độ dài', 'formula': '$MA = MB = AB : 2$ · $AB = 2 \\times MA$'}]}],
  'example': 'Cho đoạn thẳng $AB$ dài $10\\text{ cm}$, $M$ là trung điểm của $AB$. Tính độ dài đoạn thẳng '
             '$AM$.',
  'example_answer': 'Vì $M$ là trung điểm của đoạn thẳng $AB$ nên $AM = MB = 10 : 2 = 5\\text{ (cm)}$.\n'
                    'Đáp số: **$5\\text{ cm}$**.',
  'real_life': '- Gấp đôi sợi dây ruy băng để tìm chính giữa sợi dây; đặt điểm tựa bập bênh ở chính giữa '
               'thanh gỗ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu $M$ là trung điểm của đoạn thẳng $AB$ thì:',
            'options': ['$MA > MB$', '$MA < MB$', '$MA = MB$', '$MA = 2 \\times MB$'],
            'answer': 2,
            'solution': 'Trung điểm chia đoạn thẳng thành hai phần bằng nhau nên **$MA = MB$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đoạn thẳng $CD$ dài $14\\text{ cm}$, $I$ là trung điểm của $CD$. Độ dài đoạn $CI$ là:',
            'options': ['$14\\text{ cm}$', '$28\\text{ cm}$', '$12\\text{ cm}$', '$7\\text{ cm}$'],
            'answer': 3,
            'solution': 'Ta có $CI = 14 : 2 = 7\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Điều kiện**?',
            'options': ['$M$ ở giữa $A, B$ và $MA = MB$',
                        '$MA = MB = AB : 2$ · $AB = 2 \\times MA$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng, '
                        '**Điều kiện** được xác định bởi: $M$ ở giữa $A, B$ và $MA = MB$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng**, nội dung/biểu thức $MA = MB = AB '
                 ': 2$ · $AB = 2 \\times MA$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Điều kiện', 'Tính độ dài', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng, biểu thức/quy tắc $MA = MB = '
                        'AB : 2$ · $AB = 2 \\times MA$ chính là nội dung của **Tính độ dài**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $M$ là trung điểm của đoạn thẳng $PQ$, biết $MP = 6\\text{ cm}$. Độ dài đoạn thẳng '
                 '$PQ$ là:',
            'options': ['$3\\text{ cm}$', '$6\\text{ cm}$', '$12\\text{ cm}$', '$18\\text{ cm}$'],
            'answer': 2,
            'solution': 'Độ dài cả đoạn thẳng $PQ$ gấp đôi $MP$: $6 \\times 2 = 12\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng** (Chủ đề 3: Làm quen với hình '
                 'phẳng, hình khối), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Xác định được điểm ở giữa hai điểm cho trước trên một đường thẳng.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng: Xác định '
                        'được điểm ở giữa hai điểm cho trước trên một đường thẳng.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Nếu điểm $O$ nằm giữa hai điểm $A$ và $B$ thì $O$ chắc chắn là trung điểm của '
                 'đoạn thẳng $AB$."',
            'answer': False,
            'solution': 'Điểm $O$ còn phải thỏa mãn $OA = OB$ mới là trung điểm $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng**, quy tắc **Điều kiện** được xác '
                 'định bởi $M$ ở giữa $A, B$ và $MA = MB$ và áp dụng trực tiếp vào bài toán: “Cho đoạn thẳng '
                 '$AB$ dài $10\\text{ cm}$, $M$ là trung điểm của $AB$. Tính độ dài đoạn thẳng $AM$.”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Điều kiện** ($M$ ở giữa $A, B$ và $MA = MB$) là kiến '
                        'thức cốt lõi của Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng. Vì $M$ là trung '
                        'điểm của đoạn thẳng $AB$ nên $AM = MB = 10 : 2 = 5\\text{ (cm)}$. Đáp số: '
                        '**$5\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng** để giải quyết tình '
                 'huống sau: Cho đoạn thẳng $AB$ dài $10\\text{ cm}$, $M$ là trung điểm của $AB$. Tính độ '
                 'dài đoạn thẳng $AM$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $M$ là trung điểm của đoạn thẳng $AB$ nên $AM = MB = 10 : 2 = 5\\text{ (cm)}$. '
                        'Đáp số: **$5\\text{ cm}$**.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng: Vì $M$ là '
                        'trung điểm của đoạn thẳng $AB$ nên $AM = MB = 10 : 2 = 5\\text{ (cm)}$.\n'
                        'Đáp số: **$5\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thanh gỗ dài $18\\text{ dm}$ được cưa tại chính trung điểm của nó. Hỏi mỗi đoạn gỗ sau '
                 'khi cưa dài bao nhiêu đề-xi-mét?',
            'answer': ['9'],
            'unit': 'dm',
            'solution': 'Độ dài mỗi đoạn gỗ là: $18 : 2 = 9\\text{ (dm)}$.\nĐáp số: **$9\\text{ dm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd03-hinh-phang-hinh-khoi',
  'context_title': 'Chủ đề 3: Làm quen với hình phẳng, hình khối',
  'context': 'SGK Toán 3 · Chủ đề 3: Làm quen với hình phẳng và hình khối.',
  'title': 'Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn',
  'icon': '⭕',
  'description': 'Nhận biết tâm, bán kính, đường kính của hình tròn và mối quan hệ giữa đường kính với bán '
                 'kính.',
  'requirements': ['Nhận biết và gọi đúng tên tâm, bán kính, đường kính của một hình tròn.',
                   'Nắm vững tính chất: đường kính dài gấp hai lần bán kính.',
                   'Sử dụng được compa để vẽ đường tròn có tâm và bán kính cho trước.'],
  'definition': '- **Bán kính**: đoạn thẳng nối tâm $O$ với một điểm trên đường tròn (ví dụ $OA, OB, OM$).\n'
                '- **Đường kính**: đoạn thẳng nối hai điểm trên đường tròn và **đi qua tâm $O$** (ví dụ '
                '$AB$).\n'
                '- Trong một hình tròn, các bán kính đều bằng nhau và **đường kính dài gấp $2$ lần bán '
                'kính**.',
  'theory': '### 1. Các yếu tố của hình tròn\n'
            '- Hình tròn tâm $O$, bán kính $OM$, đường kính $AB$ (với $O$ là trung điểm của đường kính '
            '$AB$).\n'
            '- Lưu ý: Đoạn thẳng nối hai điểm trên đường tròn nhưng **không đi qua tâm** thì không phải là '
            'đường kính.\n'
            '### 2. Quan hệ giữa bán kính ($r$) và đường kính ($d$)\n'
            '- Ta luôn có: $d = 2 \\times r$ và $r = d : 2$.',
  'formulas': [{'category': 'I. Hình tròn tâm O',
                'items': [{'name': 'Đường kính theo bán kính', 'formula': '$d = 2 \\times r$'},
                          {'name': 'Bán kính theo đường kính', 'formula': '$r = d : 2$'}]}],
  'example': 'Một chiếc đĩa tròn có đường kính $20\\text{ cm}$. Tính bán kính của chiếc đĩa đó.',
  'example_answer': 'Bán kính của chiếc đĩa là: $20 : 2 = 10\\text{ (cm)}$.\nĐáp số: **$10\\text{ cm}$**.',
  'real_life': '- Bánh xe đạp có trục ở tâm và các nan hoa là các bán kính bằng nhau; dùng compa vẽ hình '
               'tròn trang trí.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tròn có bán kính $4\\text{ cm}$ thì đường kính của nó dài:',
            'options': ['$2\\text{ cm}$', '$4\\text{ cm}$', '$16\\text{ cm}$', '$8\\text{ cm}$'],
            'answer': 3,
            'solution': 'Đường kính gấp $2$ lần bán kính: $4 \\times 2 = 8\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một hình tròn tâm $O$, tâm $O$ là gì của đường kính $AB$?',
            'options': ['Trung điểm của đoạn thẳng $AB$',
                        'Điểm bất kì',
                        'Đầu mút của $AB$',
                        'Điểm nằm ngoài $AB$'],
            'answer': 0,
            'solution': 'Tâm $O$ nằm giữa $A, B$ và $OA = OB$ nên $O$ là **trung điểm của $AB$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình '
                 'tròn**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Đường kính theo bán kính**?',
            'options': ['$r = d : 2$',
                        '$d = 2 \\times r$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 17: Hình tròn. Tâm, bán kính, đường kính của '
                        'hình tròn, **Đường kính theo bán kính** được xác định bởi: $d = 2 \\times r$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn**, nội dung/biểu thức '
                 '$r = d : 2$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Đường kính theo bán kính',
                        'Phân tích số',
                        'Bán kính theo đường kính',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn, biểu thức/quy tắc '
                        '$r = d : 2$ chính là nội dung của **Bán kính theo đường kính**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình tròn tâm $O$ có đường kính $MN = 18\\text{ cm}$ và điểm $P$ nằm trên đường tròn. '
                 'Độ dài bán kính $OP$ là:',
            'options': ['$18\\text{ cm}$', '$36\\text{ cm}$', '$6\\text{ cm}$', '$9\\text{ cm}$'],
            'answer': 3,
            'solution': 'Mọi bán kính đều bằng nửa đường kính: $OP = 18 : 2 = 9\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn** (Chủ đề 3: Làm quen '
                 'với hình phẳng, hình khối), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Nhận biết và gọi đúng tên tâm, bán kính, đường kính của một hình tròn.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình '
                        'tròn: Nhận biết và gọi đúng tên tâm, bán kính, đường kính của một hình tròn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Mọi đoạn thẳng nối hai điểm trên đường tròn đều là đường kính của hình tròn '
                 'đó."',
            'answer': False,
            'solution': 'Đoạn thẳng đó phải **đi qua tâm** của hình tròn mới là đường kính $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn**, quy tắc **Đường kính '
                 'theo bán kính** được xác định bởi $d = 2 \\times r$ và áp dụng trực tiếp vào bài toán: '
                 '“Một chiếc đĩa tròn có đường kính $20\\text{ cm}$. Tính bán kính của chiếc đĩa đó.”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đường kính theo bán kính** ($d = 2 \\times r$) là '
                        'kiến thức cốt lõi của Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn. '
                        'Bán kính của chiếc đĩa là: $20 : 2 = 10\\text{ (cm)}$. Đáp số: **$10\\text{ '
                        'cm}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn** để giải '
                 'quyết tình huống sau: Một chiếc đĩa tròn có đường kính $20\\text{ cm}$. Tính bán kính của '
                 'chiếc đĩa đó. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Bán kính của chiếc đĩa là: $20 : 2 = 10\\text{ (cm)}$. Đáp số: **$10\\text{ cm}$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn: '
                        'Bán kính của chiếc đĩa là: $20 : 2 = 10\\text{ (cm)}$.\n'
                        'Đáp số: **$10\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mặt bàn hình tròn có bán kính $35\\text{ cm}$. Hỏi đường kính của mặt bàn đó dài bao '
                 'nhiêu xăng-ti-mét?',
            'answer': ['70'],
            'unit': 'cm',
            'solution': 'Đường kính mặt bàn là: $35 \\times 2 = 70\\text{ (cm)}$.\n'
                        'Đáp số: **$70\\text{ cm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd03-hinh-phang-hinh-khoi',
  'context_title': 'Chủ đề 3: Làm quen với hình phẳng, hình khối',
  'context': 'SGK Toán 3 · Chủ đề 3: Làm quen với hình phẳng và hình khối.',
  'title': 'Bài 18: Góc, góc vuông, góc không vuông',
  'icon': '📐',
  'description': 'Nhận biết góc, đỉnh và hai cạnh của góc; dùng ê-ke kiểm tra góc vuông và góc không vuông.',
  'requirements': ['Nhận biết được góc, nêu đúng tên đỉnh và hai cạnh của góc.',
                   'Phân biệt được góc vuông và góc không vuông.',
                   'Biết dùng ê-ke để kiểm tra góc vuông và vẽ góc vuông.'],
  'definition': '- **Góc** gồm một **đỉnh** và **hai cạnh** xuất phát từ đỉnh đó (ví dụ góc đỉnh $O$, cạnh '
                '$OA, OB$).\n'
                '- **Góc vuông**: góc vừa khít với góc vuông của chiếc ê-ke (có số đo bằng $90^\\circ$).\n'
                '- **Góc không vuông**: góc lớn hơn hoặc bé hơn góc vuông của ê-ke.',
  'theory': '### 1. Đỉnh và cạnh của góc\n'
            '- Góc đỉnh $A$, cạnh $AB$ và $AC$: điểm chung $A$ là đỉnh, hai đoạn thẳng $AB, AC$ là hai '
            'cạnh.\n'
            '### 2. Kiểm tra góc vuông bằng ê-ke\n'
            '- Bước 1: Đặt đỉnh góc vuông của ê-ke trùng với đỉnh của góc cần kiểm tra.\n'
            '- Bước 2: Đặt một cạnh góc vuông của ê-ke trùng với một cạnh của góc.\n'
            '- Bước 3: Nếu cạnh còn lại của góc trùng với cạnh góc vuông kia của ê-ke thì góc đó là **góc '
            'vuông**; ngược lại là **góc không vuông**.',
  'formulas': [{'category': 'I. Cấu tạo góc',
                'items': [{'name': 'Góc đỉnh O', 'formula': 'Đỉnh $O$ · Hai cạnh $OA, OB$'}]},
               {'category': 'II. Phân loại bằng ê-ke',
                'items': [{'name': 'Góc vuông', 'formula': 'Hai cạnh trùng khít hai cạnh góc vuông của ê-ke'},
                          {'name': 'Góc không vuông',
                           'formula': 'Cạnh thứ hai không trùng cạnh góc vuông của ê-ke'}]}],
  'example': 'Cho góc đỉnh $M$, hai cạnh $MN$ và $MP$. Hãy chỉ ra đỉnh và các cạnh của góc đó.',
  'example_answer': 'Góc đã cho có **đỉnh là điểm $M$**, hai cạnh là **$MN$ và $MP$**.',
  'real_life': '- Dùng ê-ke kiểm tra góc vuông ở mép bàn học, khung cửa sổ, quyển vở hoặc viên gạch lát nền.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dụng cụ dùng để kiểm tra góc vuông là:',
            'options': ['Ê-ke', 'Compa', 'Cân đồng hồ', 'Nhiệt kế'],
            'answer': 0,
            'solution': 'Ta dùng **ê-ke** để kiểm tra và vẽ góc vuông.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Góc đỉnh $I$, cạnh $IA, IB$ có đỉnh là:',
            'options': ['Điểm $A$', 'Điểm $I$', 'Điểm $B$', 'Đoạn $AB$'],
            'answer': 1,
            'solution': 'Tên đỉnh được gọi ngay sau chữ "góc đỉnh" $\\rightarrow$ **Điểm $I$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 18: Góc, góc vuông, góc không vuông**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Góc đỉnh O**?',
            'options': ['Hai cạnh trùng khít hai cạnh góc vuông của ê-ke',
                        'Cạnh thứ hai không trùng cạnh góc vuông của ê-ke',
                        'Đỉnh $O$ · Hai cạnh $OA, OB$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 18: Góc, góc vuông, góc không vuông, **Góc '
                        'đỉnh O** được xác định bởi: Đỉnh $O$ · Hai cạnh $OA, OB$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Góc, góc vuông, góc không vuông**, nội dung/biểu thức Hai cạnh trùng khít '
                 'hai cạnh góc vuông của ê-ke là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Góc đỉnh O', 'Góc không vuông', 'Phân tích số', 'Góc vuông'],
            'answer': 3,
            'solution': 'Trong Bài 18: Góc, góc vuông, góc không vuông, biểu thức/quy tắc Hai cạnh trùng '
                        'khít hai cạnh góc vuông của ê-ke chính là nội dung của **Góc vuông**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi đồng hồ chỉ đúng $3$ giờ, kim giờ và kim phút tạo thành góc gì?',
            'options': ['Góc vuông', 'Góc không vuông', 'Đường thẳng', 'Hình tròn'],
            'answer': 0,
            'solution': 'Lúc $3$ giờ đúng, kim giờ chỉ số $3$ và kim phút chỉ số $12$ tạo thành **góc '
                        'vuông**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Góc, góc vuông, góc không vuông** (Chủ đề 3: Làm quen với hình phẳng, '
                 'hình khối), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Nhận biết được góc, nêu đúng tên đỉnh và hai cạnh của góc.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 18: Góc, góc vuông, góc không vuông: Nhận biết được '
                        'góc, nêu đúng tên đỉnh và hai cạnh của góc.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Mỗi chiếc ê-ke thông thường có $1$ góc vuông và $2$ góc không vuông."',
            'answer': True,
            'solution': 'Chiếc ê-ke hình tam giác có đúng $1$ góc vuông và $2$ góc nhọn (không vuông) '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 18: Góc, góc vuông, góc không vuông**, quy tắc **Góc đỉnh O** được xác định '
                 'bởi Đỉnh $O$ · Hai cạnh $OA, OB$ và áp dụng trực tiếp vào bài toán: “Cho góc đỉnh $M$, hai '
                 'cạnh $MN$ và $MP$. Hãy chỉ ra đỉnh và các cạnh của góc đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Góc đỉnh O** (Đỉnh $O$ · Hai cạnh $OA, OB$) là kiến '
                        'thức cốt lõi của Bài 18: Góc, góc vuông, góc không vuông. Góc đã cho có **đỉnh là '
                        'điểm $M$**, hai cạnh là **$MN$ và $MP$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 18: Góc, góc vuông, góc không vuông** để giải quyết tình huống '
                 'sau: Cho góc đỉnh $M$, hai cạnh $MN$ và $MP$. Hãy chỉ ra đỉnh và các cạnh của góc đó. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Góc đã cho có **đỉnh là điểm $M$**, hai cạnh là **$MN$ và $MP$**.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 18: Góc, góc vuông, góc không vuông: Góc đã cho có '
                        '**đỉnh là điểm $M$**, hai cạnh là **$MN$ và $MP$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tờ giấy hình chữ nhật có $4$ góc vuông. Nếu em dùng kéo cắt chéo bỏ đi $1$ góc vuông '
                 'bằng một đường thẳng nối hai cạnh kề nhau thì tờ giấy còn lại có mấy góc vuông?',
            'answer': ['3'],
            'unit': 'góc vuông',
            'solution': 'Cắt bỏ $1$ góc vuông trong $4$ góc vuông thì tờ giấy còn lại **$3$** góc vuông.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd03-hinh-phang-hinh-khoi',
  'context_title': 'Chủ đề 3: Làm quen với hình phẳng, hình khối',
  'context': 'SGK Toán 3 · Chủ đề 3: Làm quen với hình phẳng và hình khối.',
  'title': 'Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông',
  'icon': '🟦',
  'description': 'Nhận biết đỉnh, cạnh, góc của tam giác, tứ giác; đặc điểm của hình chữ nhật, hình vuông và '
                 'thực hành vẽ.',
  'requirements': ['Nêu được số đỉnh, số cạnh, số góc của hình tam giác và hình tứ giác.',
                   'Nắm vững đặc điểm về góc và cạnh của hình chữ nhật và hình vuông.',
                   'Vẽ được hình chữ nhật, hình vuông trên lưới ô vuông.'],
  'definition': '- **Hình tam giác** có $3$ đỉnh, $3$ cạnh, $3$ góc. **Hình tứ giác** có $4$ đỉnh, $4$ cạnh, '
                '$4$ góc.\n'
                '- **Hình chữ nhật** có $4$ góc vuông, $2$ cạnh dài có độ dài bằng nhau và $2$ cạnh ngắn có '
                'độ dài bằng nhau.\n'
                '- **Hình vuông** có $4$ góc vuông và $4$ cạnh có độ dài bằng nhau.',
  'theory': '### 1. Hình tam giác và hình tứ giác\n'
            '- Hình tam giác $ABC$ có $3$ đỉnh $A, B, C$; $3$ cạnh $AB, BC, CA$ và $3$ góc.\n'
            '- Hình tứ giác $MNPQ$ có $4$ đỉnh $M, N, P, Q$; $4$ cạnh $MN, NP, PQ, QM$ và $4$ góc.\n'
            '### 2. Hình chữ nhật và hình vuông\n'
            '- Trong hình chữ nhật, độ dài cạnh dài gọi là **chiều dài**, độ dài cạnh ngắn gọi là **chiều '
            'rộng**.\n'
            '- Hình vuông là hình chữ nhật đặc biệt có chiều dài bằng chiều rộng.',
  'formulas': [{'category': 'I. Hình phẳng cơ bản',
                'items': [{'name': 'Tam giác / Tứ giác',
                           'formula': 'Tam giác: $3$ đỉnh, $3$ cạnh, $3$ góc · Tứ giác: $4$ đỉnh, $4$ cạnh, '
                                      '$4$ góc'}]},
               {'category': 'II. Hình chữ nhật & Hình vuông',
                'items': [{'name': 'Hình chữ nhật',
                           'formula': '$4$ góc vuông · $2$ cạnh dài bằng nhau · $2$ cạnh ngắn bằng nhau'},
                          {'name': 'Hình vuông', 'formula': '$4$ góc vuông · $4$ cạnh bằng nhau'}]}],
  'example': 'Hình chữ nhật $ABCD$ có chiều dài $AB = 8\\text{ cm}$, chiều rộng $BC = 5\\text{ cm}$. Tìm độ '
             'dài cạnh $CD$ và $AD$.',
  'example_answer': 'Trong hình chữ nhật $ABCD$, hai cạnh dài bằng nhau nên $CD = AB = 8\\text{ cm}$; hai '
                    'cạnh ngắn bằng nhau nên $AD = BC = 5\\text{ cm}$.',
  'real_life': '- Mặt bảng lớp học, cánh cửa, quyển sách có dạng hình chữ nhật; viên gạch bông lát nền có '
               'dạng hình vuông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình vuông có mấy góc vuông và mấy cạnh bằng nhau?',
            'options': ['$2$ góc vuông, $2$ cạnh bằng nhau',
                        '$4$ góc vuông, $4$ cạnh bằng nhau',
                        '$4$ góc vuông, $2$ cạnh bằng nhau',
                        '$3$ góc vuông, $3$ cạnh bằng nhau'],
            'answer': 1,
            'solution': 'Hình vuông có **$4$ góc vuông và $4$ cạnh bằng nhau**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tam giác có bao nhiêu đỉnh và bao nhiêu cạnh?',
            'options': ['$4$ đỉnh, $4$ cạnh',
                        '$3$ đỉnh, $4$ cạnh',
                        '$3$ đỉnh, $3$ cạnh',
                        '$4$ đỉnh, $3$ cạnh'],
            'answer': 2,
            'solution': 'Hình tam giác có **$3$ đỉnh và $3$ cạnh**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình '
                 'vuông**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tam giác / Tứ giác**?',
            'options': ['$4$ góc vuông · $2$ cạnh dài bằng nhau · $2$ cạnh ngắn bằng nhau',
                        '$4$ góc vuông · $4$ cạnh bằng nhau',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Tam giác: $3$ đỉnh, $3$ cạnh, $3$ góc · Tứ giác: $4$ đỉnh, $4$ cạnh, $4$ góc'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 19, 20: Hình tam giác, tứ giác. Hình chữ '
                        'nhật, hình vuông, **Tam giác / Tứ giác** được xác định bởi: Tam giác: $3$ đỉnh, $3$ '
                        'cạnh, $3$ góc · Tứ giác: $4$ đỉnh, $4$ cạnh, $4$ góc.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông**, nội dung/biểu '
                 'thức $4$ góc vuông · $2$ cạnh dài bằng nhau · $2$ cạnh ngắn bằng nhau là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Hình chữ nhật', 'Tam giác / Tứ giác', 'Hình vuông', 'Phân tích số'],
            'answer': 0,
            'solution': 'Trong Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông, biểu thức/quy '
                        'tắc $4$ góc vuông · $2$ cạnh dài bằng nhau · $2$ cạnh ngắn bằng nhau chính là nội '
                        'dung của **Hình chữ nhật**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chữ nhật $MNPQ$ có $MN = 10\\text{ cm}$ và $NP = 6\\text{ cm}$. Độ dài cạnh $PQ$ '
                 'là:',
            'options': ['$6\\text{ cm}$', '$10\\text{ cm}$', '$16\\text{ cm}$', '$4\\text{ cm}$'],
            'answer': 1,
            'solution': 'Hai cạnh dài đối diện của hình chữ nhật bằng nhau: $PQ = MN = 10\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông** (Chủ đề 3: Làm '
                 'quen với hình phẳng, hình khối), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt '
                 'và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Nêu được số đỉnh, số cạnh, số góc của hình tam giác và hình tứ giác.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình '
                        'vuông: Nêu được số đỉnh, số cạnh, số góc của hình tam giác và hình tứ giác.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tứ giác có $4$ cạnh bằng nhau chắc chắn là hình vuông."',
            'answer': False,
            'solution': 'Hình đó còn phải có $4$ góc vuông mới là hình vuông $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông**, quy tắc **Tam '
                 'giác / Tứ giác** được xác định bởi Tam giác: $3$ đỉnh, $3$ cạnh, $3$ góc · Tứ giác: $4$ '
                 'đỉnh, $4$ cạnh, $4$ góc và áp dụng trực tiếp vào bài toán: “Hình chữ nhật $ABCD$ có chiều '
                 'dài $AB = 8\\text{ cm}$, chiều rộng $BC = 5\\text{ cm}$. Tìm độ dài cạnh $CD$ và $AD$.”. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tam giác / Tứ giác** (Tam giác: $3$ đỉnh, $3$ cạnh, '
                        '$3$ góc · Tứ giác: $4$ đỉnh, $4$ cạnh, $4$ góc) là kiến thức cốt lõi của Bài 19, '
                        '20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông. Trong hình chữ nhật $ABCD$, '
                        'hai cạnh dài bằng nhau nên $CD = AB = 8\\text{ cm}$; hai cạnh ngắn bằng nhau nên '
                        '$AD = BC = 5\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình vuông** để '
                 'giải quyết tình huống sau: Hình chữ nhật $ABCD$ có chiều dài $AB = 8\\text{ cm}$, chiều '
                 'rộng $BC = 5\\text{ cm}$. Tìm độ dài cạnh $CD$ và $AD$. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Trong hình chữ nhật $ABCD$, hai cạnh dài bằng nhau nên $CD = AB = 8\\text{ cm}$; '
                        'hai cạnh ngắn bằng nhau nên $AD = BC = 5\\text{ cm}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 19, 20: Hình tam giác, tứ giác. Hình chữ nhật, hình '
                        'vuông: Trong hình chữ nhật $ABCD$, hai cạnh dài bằng nhau nên $CD = AB = 8\\text{ '
                        'cm}$; hai cạnh ngắn bằng nhau nên $AD = BC = 5\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Để ghép thành một khung tranh hình vuông có cạnh dài $15\\text{ cm}$, bạn Nam cần $4$ '
                 'thanh gỗ dài bằng nhau. Hỏi mỗi thanh gỗ dài bao nhiêu xăng-ti-mét?',
            'answer': ['15'],
            'unit': 'cm',
            'solution': 'Vì $4$ cạnh hình vuông bằng nhau nên mỗi thanh gỗ dài **$15\\text{ cm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd03-hinh-phang-hinh-khoi',
  'context_title': 'Chủ đề 3: Làm quen với hình phẳng, hình khối',
  'context': 'SGK Toán 3 · Chủ đề 3: Làm quen với hình phẳng và hình khối.',
  'title': 'Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập chung',
  'icon': '🧊',
  'description': 'Nhận biết số đỉnh, số cạnh, số mặt của khối lập phương và khối hộp chữ nhật.',
  'requirements': ['Nêu đúng số đỉnh ($8$ đỉnh), số cạnh ($12$ cạnh), số mặt ($6$ mặt) của khối lập phương '
                   'và khối hộp chữ nhật.',
                   'Phân biệt được hình dạng các mặt của khối lập phương (hình vuông) và khối hộp chữ nhật '
                   '(hình chữ nhật).',
                   'Giải được bài toán thực tế gắn với các cạnh, mặt của hình khối.'],
  'definition': '- **Khối lập phương** và **khối hộp chữ nhật** đều có **$8$ đỉnh, $12$ cạnh và $6$ mặt**.\n'
                '- Các mặt của khối lập phương đều là **hình vuông** bằng nhau; các mặt của khối hộp chữ '
                'nhật đều là **hình chữ nhật**.',
  'theory': '### 1. Đặc điểm của khối lập phương\n'
            '- Có $8$ đỉnh, $12$ cạnh dài bằng nhau, $6$ mặt đều là hình vuông.\n'
            '- Ví dụ thực tế: con xúc xắc, khối rubik $3 \\times 3$.\n'
            '### 2. Đặc điểm của khối hộp chữ nhật\n'
            '- Có $8$ đỉnh, $12$ cạnh, $6$ mặt đều là hình chữ nhật (hai mặt đối diện bằng nhau).\n'
            '- Ví dụ thực tế: hộp bánh, bao diêm, viên gạch xây nhà.',
  'formulas': [{'category': 'I. Hình khối',
                'items': [{'name': 'Số yếu tố chung', 'formula': '$8$ đỉnh · $12$ cạnh · $6$ mặt'},
                          {'name': 'Hình dạng mặt',
                           'formula': 'Khối lập phương: $6$ mặt hình vuông · Khối hộp chữ nhật: $6$ mặt hình '
                                      'chữ nhật'}]}],
  'example': 'Bạn Mai muốn dán giấy màu kín tất cả các mặt của $1$ chiếc hộp hình lập phương. Hỏi Mai cần '
             'cắt bao nhiêu mảnh giấy hình vuông?',
  'example_answer': 'Vì khối lập phương có $6$ mặt đều là hình vuông nên Mai cần cắt **$6$ mảnh giấy** hình '
                    'vuông.',
  'real_life': '- Làm khung đèn lồng, gói hộp quà sinh nhật, đếm số mặt của viên xúc xắc từ $1$ đến $6$ '
               'chấm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khối lập phương có bao nhiêu mặt?',
            'options': ['$4$ mặt', '$8$ mặt', '$6$ mặt', '$12$ mặt'],
            'answer': 2,
            'solution': 'Khối lập phương có **$6$ mặt** đều là hình vuông.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khối hộp chữ nhật có bao nhiêu đỉnh và bao nhiêu cạnh?',
            'options': ['$6$ đỉnh, $8$ cạnh',
                        '$12$ đỉnh, $8$ cạnh',
                        '$6$ đỉnh, $12$ cạnh',
                        '$8$ đỉnh, $12$ cạnh'],
            'answer': 3,
            'solution': 'Khối hộp chữ nhật có **$8$ đỉnh và $12$ cạnh**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Số yếu tố chung**?',
            'options': ['$8$ đỉnh · $12$ cạnh · $6$ mặt',
                        'Khối lập phương: $6$ mặt hình vuông · Khối hộp chữ nhật: $6$ mặt hình chữ nhật',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 21, 22: Khối lập phương, khối hộp chữ nhật và '
                        'luyện tập chung, **Số yếu tố chung** được xác định bởi: $8$ đỉnh · $12$ cạnh · $6$ '
                        'mặt.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập chung**, nội dung/biểu '
                 'thức Khối lập phương: $6$ mặt hình vuông · Khối hộp chữ nhật: $6$ mặt hình chữ nhật là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số yếu tố chung', 'Hình dạng mặt', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập chung, biểu '
                        'thức/quy tắc Khối lập phương: $6$ mặt hình vuông · Khối hộp chữ nhật: $6$ mặt hình '
                        'chữ nhật chính là nội dung của **Hình dạng mặt**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Các mặt của khối lập phương là hình gì?',
            'options': ['Hình tam giác', 'Hình tròn', 'Hình vuông', 'Hình ngũ giác'],
            'answer': 2,
            'solution': 'Tất cả $6$ mặt của khối lập phương đều là **hình vuông**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập chung** (Chủ đề 3: '
                 'Làm quen với hình phẳng, hình khối), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Nêu đúng số đỉnh ($8$ đỉnh), số cạnh ($12$ cạnh), số mặt ($6$ mặt) của khối lập '
                        'phương và khối hộp chữ nhật.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện '
                        'tập chung: Nêu đúng số đỉnh ($8$ đỉnh), số cạnh ($12$ cạnh), số mặt ($6$ mặt) của '
                        'khối lập phương và khối hộp chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khối lập phương và khối hộp chữ nhật có số đỉnh bằng nhau và số cạnh bằng '
                 'nhau."',
            'answer': True,
            'solution': 'Cả hai khối đều có $8$ đỉnh và $12$ cạnh $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập chung**, quy tắc **Số '
                 'yếu tố chung** được xác định bởi $8$ đỉnh · $12$ cạnh · $6$ mặt và áp dụng trực tiếp vào '
                 'bài toán: “Bạn Mai muốn dán giấy màu kín tất cả các mặt của $1$ chiếc hộp hình lập phương. '
                 'Hỏi Mai cần cắt bao nhiêu mảnh giấy hình vuông?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Số yếu tố chung** ($8$ đỉnh · $12$ cạnh · $6$ mặt) '
                        'là kiến thức cốt lõi của Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện '
                        'tập chung. Vì khối lập phương có $6$ mặt đều là hình vuông nên Mai cần cắt **$6$ '
                        'mảnh giấy** hình vuông.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập chung** '
                 'để giải quyết tình huống sau: Bạn Mai muốn dán giấy màu kín tất cả các mặt của $1$ chiếc '
                 'hộp hình lập phương. Hỏi Mai cần cắt bao nhiêu mảnh giấy hình vuông? Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Vì khối lập phương có $6$ mặt đều là hình vuông nên Mai cần cắt **$6$ mảnh giấy** '
                        'hình vuông.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 21, 22: Khối lập phương, khối hộp chữ nhật và luyện tập '
                        'chung: Vì khối lập phương có $6$ mặt đều là hình vuông nên Mai cần cắt **$6$ mảnh '
                        'giấy** hình vuông.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bác thợ hàn dùng các thanh sắt dài bằng nhau để hàn thành khung của một chiếc lồng hình '
                 'lập phương (mỗi cạnh là $1$ thanh sắt). Hỏi bác cần bao nhiêu thanh sắt?',
            'answer': ['12'],
            'unit': 'thanh',
            'solution': 'Khối lập phương có $12$ cạnh nên bác thợ cần **$12$ thanh sắt**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd04-nhan-chia-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép nhân, phép chia trong phạm vi 100',
  'context': 'SGK Toán 3 · Chủ đề 4: Phép nhân, phép chia trong phạm vi 100.',
  'title': 'Bài 23: Nhân số có hai chữ số với số có một chữ số',
  'icon': '✖️',
  'description': 'Đặt tính và thực hiện phép nhân số có hai chữ số với số có một chữ số (không nhớ và có '
                 'nhớ).',
  'requirements': ['Đặt tính và tính đúng phép nhân số có hai chữ số với số có một chữ số (không nhớ và có '
                   'nhớ $1$ lượt).',
                   'Thực hiện được tính nhẩm nhân số tròn chục có hai chữ số với số có một chữ số.',
                   'Vận dụng giải bài toán thực tế có một phép nhân.'],
  'definition': '- Khi nhân số có $2$ chữ số ($\\overline{ab}$) với số có $1$ chữ số ($c$), ta đặt thừa số '
                '$c$ thẳng cột với hàng đơn vị $b$.\n'
                '- Nhân lần lượt từ phải sang trái: nhân với chữ số hàng đơn vị trước, rồi nhân với chữ số '
                'hàng chục (cộng thêm số nhớ nếu có).',
  'theory': '### 1. Phép nhân không nhớ\n'
            '- Ví dụ: $23 \\times 3$. Ta tính $3 \\times 3 = 9$ (viết $9$); $3 \\times 2 = 6$ (viết $6$). '
            'Vậy $23 \\times 3 = 69$.\n'
            '### 2. Phép nhân có nhớ\n'
            '- Ví dụ: $26 \\times 3$. Ta tính $3 \\times 6 = 18$, viết $8$ nhớ $1$; $3 \\times 2 = 6$, thêm '
            '$1$ bằng $7$, viết $7$. Vậy $26 \\times 3 = 78$.',
  'formulas': [{'category': 'I. Quy tắc nhân viết',
                'items': [{'name': 'Thứ tự nhân',
                           'formula': 'Nhân hàng đơn vị $\\rightarrow$ Nhân hàng chục (cộng phần nhớ)'},
                          {'name': 'Nhân số tròn chục',
                           'formula': '$a0 \\times b = (a \\times b)0$',
                           'note': 'Ví dụ: $20 \\times 4 = 80$'}]}],
  'example': 'Đặt tính rồi tính: $18 \\times 4$ và $32 \\times 3$.',
  'example_answer': '- $18 \\times 4$: $4 \\times 8 = 32$ (viết $2$ nhớ $3$); $4 \\times 1 = 4$, thêm $3$ '
                    'bằng $7$ $\\rightarrow$ **$72$**.\n'
                    '- $32 \\times 3$: $3 \\times 2 = 6$; $3 \\times 3 = 9$ $\\rightarrow$ **$96$**.',
  'real_life': '- Tính tổng số bút trong $4$ hộp khi mỗi hộp có $12$ chiếc bút chì.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $23 \\times 3$ là:',
            'options': ['$66$', '$26$', '$96$', '$69$'],
            'answer': 3,
            'solution': 'Ta có $3 \\times 3 = 9$ và $3 \\times 2 = 6 \\rightarrow 69$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $30 \\times 3 = ?$',
            'options': ['$90$', '$33$', '$60$', '$9$'],
            'answer': 0,
            'solution': 'Ta có $3$ chục $\\times 3 = 9$ chục $= 90$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 23: Nhân số có hai chữ số với số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự nhân**?',
            'options': ['$a0 \\times b = (a \\times b)0$',
                        'Nhân hàng đơn vị $\\rightarrow$ Nhân hàng chục (cộng phần nhớ)',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 23: Nhân số có hai chữ số với số có một chữ '
                        'số, **Thứ tự nhân** được xác định bởi: Nhân hàng đơn vị $\\rightarrow$ Nhân hàng '
                        'chục (cộng phần nhớ).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Nhân số có hai chữ số với số có một chữ số**, nội dung/biểu thức $a0 '
                 '\\times b = (a \\times b)0$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thứ tự nhân', 'Phân tích số', 'Nhân số tròn chục', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 23: Nhân số có hai chữ số với số có một chữ số, biểu thức/quy tắc $a0 '
                        '\\times b = (a \\times b)0$ chính là nội dung của **Nhân số tròn chục**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $18 \\times 4$ là:',
            'options': ['$42$', '$62$', '$48$', '$72$'],
            'answer': 3,
            'solution': 'Ta có $8 \\times 4 = 32$ (viết $2$ nhớ $3$); $1 \\times 4 + 3 = 7 \\rightarrow 72$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Nhân số có hai chữ số với số có một chữ số** (Chủ đề 4: Phép nhân, phép '
                 'chia trong phạm vi 100), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đặt tính và tính đúng phép nhân số có hai chữ số với số có một chữ số (không nhớ và '
                        'có nhớ $1$ lượt).',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 23: Nhân số có hai chữ số với số có một chữ số: Đặt '
                        'tính và tính đúng phép nhân số có hai chữ số với số có một chữ số (không nhớ và có '
                        'nhớ $1$ lượt).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép nhân $27 \\times 3$ có kết quả bằng $61$."',
            'answer': False,
            'solution': 'Ta có $7 \\times 3 = 21$ (viết $1$ nhớ $2$); $2 \\times 3 + 2 = 8 \\Rightarrow 27 '
                        '\\times 3 = 81$, không phải $61$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 23: Nhân số có hai chữ số với số có một chữ số**, quy tắc **Thứ tự nhân** được '
                 'xác định bởi Nhân hàng đơn vị $\\rightarrow$ Nhân hàng chục (cộng phần nhớ) và áp dụng '
                 'trực tiếp vào bài toán: “Đặt tính rồi tính: $18 \\times 4$ và $32 \\times 3$.”. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự nhân** (Nhân hàng đơn vị $\\rightarrow$ Nhân '
                        'hàng chục (cộng phần nhớ)) là kiến thức cốt lõi của Bài 23: Nhân số có hai chữ số '
                        'với số có một chữ số. - $18 \\times 4$: $4 \\times 8 = 32$ (viết $2$ nhớ $3$); $4 '
                        '\\times 1 = 4$, thêm $3$ bằng $7$ $\\rightarrow$ **$72$**. - $32 \\times 3$: $3 '
                        '\\times 2 = 6$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 23: Nhân số có hai chữ số với số có một chữ số** để giải quyết '
                 'tình huống sau: Đặt tính rồi tính: $18 \\times 4$ và $32 \\times 3$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $18 \\times 4$: $4 \\times 8 = 32$ (viết $2$ nhớ $3$); $4 \\times 1 = 4$, thêm '
                        '$3$ bằng $7$ $\\rightarrow$ **$72$**. - $32 \\times 3$: $3 \\times 2 = 6$; $3 '
                        '\\times 3 = 9$...',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 23: Nhân số có hai chữ số với số có một chữ số: - $18 '
                        '\\times 4$: $4 \\times 8 = 32$ (viết $2$ nhớ $3$); $4 \\times 1 = 4$, thêm $3$ bằng '
                        '$7$ $\\rightarrow$ **$72$**.\n'
                        '- $32 \\times 3$: $3 \\times 2 = 6$; $3 \\times 3 = 9$ $\\rightarrow$ **$96$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi lớp học được trang bị $15$ bộ bàn ghế. Hỏi $5$ lớp học như thế có tất cả bao nhiêu bộ '
                 'bàn ghế?',
            'answer': ['75'],
            'unit': 'bộ',
            'solution': 'Tổng số bộ bàn ghế là: $15 \\times 5 = 75\\text{ (bộ)}$.\n'
                        'Đáp số: **$75\\text{ bộ}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd04-nhan-chia-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép nhân, phép chia trong phạm vi 100',
  'context': 'SGK Toán 3 · Chủ đề 4: Phép nhân, phép chia trong phạm vi 100.',
  'title': 'Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần',
  'icon': '📈',
  'description': 'Quy tắc gấp một số lên một số lần, giảm một số đi một số lần và phân biệt với thêm, bớt.',
  'requirements': ['Biết cách gấp một số lên một số lần bằng phép nhân.',
                   'Biết cách giảm một số đi một số lần bằng phép chia.',
                   'Phân biệt rõ "gấp lên $n$ lần" với "thêm $n$ đơn vị" và "giảm đi $n$ lần" với "bớt $n$ '
                   'đơn vị".'],
  'definition': '- **Gấp một số lên $n$ lần**: Muốn gấp một số $a$ lên $n$ lần, ta lấy số đó **nhân** với số '
                'lần ($a \\times n$).\n'
                '- **Giảm một số đi $n$ lần**: Muốn giảm một số $a$ đi $n$ lần, ta lấy số đó **chia** cho số '
                'lần ($a : n$).',
  'theory': '### 1. Gấp một số lên $n$ lần\n'
            '- Ví dụ: Gấp $7$ lên $5$ lần ta được $7 \\times 5 = 35$.\n'
            '- Phân biệt: "Thêm $5$ đơn vị" là $7 + 5 = 12$; còn "gấp $5$ lần" là $7 \\times 5 = 35$.\n'
            '### 2. Giảm một số đi $n$ lần\n'
            '- Ví dụ: Giảm $48$ đi $6$ lần ta được $48 : 6 = 8$.\n'
            '- Phân biệt: "Bớt $6$ đơn vị" là $48 - 6 = 42$; còn "giảm $6$ lần" là $48 : 6 = 8$.',
  'formulas': [{'category': 'I. Gấp và giảm số lần',
                'items': [{'name': 'Gấp số a lên n lần', 'formula': '$a \\times n$'},
                          {'name': 'Giảm số a đi n lần', 'formula': '$a : n$'},
                          {'name': 'Phân biệt với thêm/bớt',
                           'formula': 'Thêm $n$: $a + n$ · Bớt $n$: $a - n$'}]}],
  'example': 'Đoạn thẳng $AB$ dài $24\\text{ cm}$. Đoạn thẳng $CD$ có độ dài bằng đoạn thẳng $AB$ giảm đi '
             '$3$ lần. Tính độ dài đoạn $CD$.',
  'example_answer': 'Độ dài đoạn thẳng $CD$ là: $24 : 3 = 8\\text{ (cm)}$.\nĐáp số: **$8\\text{ cm}$**.',
  'real_life': '- Công thức nấu ăn khi số người ăn tăng gấp $3$ lần; thời gian đi xe đạp giảm đi $2$ lần so '
               'với đi bộ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Gấp $7$ lên $5$ lần ta được:',
            'options': ['$35$', '$12$', '$2$', '$75$'],
            'answer': 0,
            'solution': 'Lấy $7 \\times 5 = 35$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giảm $48$ đi $6$ lần ta được:',
            'options': ['$42$', '$8$', '$54$', '$288$'],
            'answer': 1,
            'solution': 'Lấy $48 : 6 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số '
                 'lần**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Gấp số a lên n lần**?',
            'options': ['$a : n$',
                        'Thêm $n$: $a + n$ · Bớt $n$: $a - n$',
                        '$a \\times n$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 24, 27: Gấp một số lên một số lần. Giảm một '
                        'số đi một số lần, **Gấp số a lên n lần** được xác định bởi: $a \\times n$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần**, nội dung/biểu '
                 'thức $a : n$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Gấp số a lên n lần', 'Phân biệt với thêm/bớt', 'Phân tích số', 'Giảm số a đi n lần'],
            'answer': 3,
            'solution': 'Trong Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần, biểu '
                        'thức/quy tắc $a : n$ chính là nội dung của **Giảm số a đi n lần**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số $12$ gấp lên $4$ lần rồi bớt đi $8$ đơn vị thì được kết quả là:',
            'options': ['$40$', '$48$', '$8$', '$24$'],
            'answer': 0,
            'solution': 'Gấp $12$ lên $4$ lần được $12 \\times 4 = 48$; bớt đi $8$ được $48 - 8 = 40$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần** (Chủ đề 4: '
                 'Phép nhân, phép chia trong phạm vi 100), khẳng định nào sau đây phản ánh **đúng** yêu cầu '
                 'cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Biết cách gấp một số lên một số lần bằng phép nhân.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một '
                        'số lần: Biết cách gấp một số lên một số lần bằng phép nhân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Gấp $6$ lên $3$ lần thì được $9$."',
            'answer': False,
            'solution': 'Gấp $6$ lên $3$ lần là $6 \\times 3 = 18$ (còn $6 + 3 = 9$ là thêm $3$ đơn vị) '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần**, quy tắc **Gấp '
                 'số a lên n lần** được xác định bởi $a \\times n$ và áp dụng trực tiếp vào bài toán: “Đoạn '
                 'thẳng $AB$ dài $24\\text{ cm}$. Đoạn thẳng $CD$ có độ dài bằng đoạn thẳng $AB$ giảm đi $3$ '
                 'lần. Tính độ dài đoạn $CD$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Gấp số a lên n lần** ($a \\times n$) là kiến thức '
                        'cốt lõi của Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần. Độ '
                        'dài đoạn thẳng $CD$ là: $24 : 3 = 8\\text{ (cm)}$. Đáp số: **$8\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số lần** để '
                 'giải quyết tình huống sau: Đoạn thẳng $AB$ dài $24\\text{ cm}$. Đoạn thẳng $CD$ có độ dài '
                 'bằng đoạn thẳng $AB$ giảm đi $3$ lần. Tính độ dài đoạn $CD$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Độ dài đoạn thẳng $CD$ là: $24 : 3 = 8\\text{ (cm)}$. Đáp số: **$8\\text{ cm}$**.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 24, 27: Gấp một số lên một số lần. Giảm một số đi một số '
                        'lần: Độ dài đoạn thẳng $CD$ là: $24 : 3 = 8\\text{ (cm)}$.\n'
                        'Đáp số: **$8\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Buổi sáng cửa hàng bán được $16\\text{ l}$ mật ong, buổi chiều bán được số lít mật ong '
                 'giảm đi $2$ lần so với buổi sáng. Hỏi buổi chiều cửa hàng bán được bao nhiêu lít mật ong?',
            'answer': ['8'],
            'unit': 'l',
            'solution': 'Số lít mật ong bán buổi chiều là: $16 : 2 = 8\\text{ (l)}$.\n'
                        'Đáp số: **$8\\text{ l}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd04-nhan-chia-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép nhân, phép chia trong phạm vi 100',
  'context': 'SGK Toán 3 · Chủ đề 4: Phép nhân, phép chia trong phạm vi 100.',
  'title': 'Bài 25: Phép chia hết, phép chia có dư',
  'icon': '➗',
  'description': 'Nhận biết phép chia hết, phép chia có dư và điều kiện số dư luôn bé hơn số chia.',
  'requirements': ['Phân biệt được phép chia hết (số dư bằng 0) và phép chia có dư.',
                   'Nắm vững quy tắc: Trong phép chia có dư, số dư luôn bé hơn số chia ($0 < r < b$).',
                   'Giải được bài toán thực tế có sử dụng phép chia có dư (bài toán thêm 1 bàn/chuyến xe).'],
  'definition': '- **Phép chia có dư**: $a = b \\times q + r$, viết là $a : b = q \\text{ (dư } '
                'r\\text{)}$.\n'
                '- **Điều kiện quan trọng**: **Số dư luôn bé hơn số chia** ($r < b$). Nếu $r = 0$ thì đó là '
                '**phép chia hết**.',
  'theory': '### 1. Thực hiện phép chia có dư\n'
            '- Ví dụ: Chia $17$ quả táo vào các đĩa, mỗi đĩa $5$ quả. Ta có $17 : 5 = 3 \\text{ (dư } '
            '2\\text{)}$ vì $5 \\times 3 + 2 = 17$ và $2 < 5$.\n'
            '### 2. Số dư lớn nhất trong phép chia\n'
            '- Vì số dư luôn bé hơn số chia nên khi chia cho $b$, số dư lớn nhất có thể là $b - 1$. Ví dụ: '
            'chia cho $5$ thì số dư chỉ có thể là $1, 2, 3, 4$ (lớn nhất là $4$).',
  'formulas': [{'category': 'I. Phép chia có dư',
                'items': [{'name': 'Công thức liên hệ',
                           'formula': '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + '
                                      '\\text{Số dư}$'},
                          {'name': 'Điều kiện số dư',
                           'formula': '$0 < \\text{Số dư} < \\text{Số chia}$ · $\\text{Số dư lớn nhất} = '
                                      '\\text{Số chia} - 1$'}]}],
  'example': 'Có $34$ học sinh, mỗi bàn ngồi tối đa $4$ bạn. Cần ít nhất bao nhiêu bàn để tất cả học sinh '
             'đều có chỗ ngồi?',
  'example_answer': 'Ta có phép chia: $34 : 4 = 8 \\text{ (dư } 2\\text{)}$.\n'
                    '$8$ bàn ngồi được $32$ bạn, còn dư $2$ bạn cũng cần thêm $1$ bàn nữa.\n'
                    'Vậy số bàn cần ít nhất là: $8 + 1 = 9\\text{ (bàn)}$.',
  'real_life': '- Xếp trứng vào khay $6$ quả; tính số thuyền cần thuê để chở hết đoàn khách qua sông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một phép chia có số chia là $5$, số dư lớn nhất có thể là:',
            'options': ['$5$', '$4$', '$6$', '$1$'],
            'answer': 1,
            'solution': 'Số dư luôn bé hơn số chia nên số dư lớn nhất là $5 - 1 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $29 : 4$ là:',
            'options': ['$7$',
                        '$6 \\text{ (dư } 5\\text{)}$',
                        '$7 \\text{ (dư } 1\\text{)}$',
                        '$8 \\text{ (dư } 3\\text{)}$'],
            'answer': 2,
            'solution': 'Vì $4 \\times 7 = 28$ và $29 - 28 = 1$ nên $29 : 4 = 7 \\text{ (dư } 1\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 25: Phép chia hết, phép chia có dư**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Công thức liên hệ**?',
            'options': ['$0 < \\text{Số dư} < \\text{Số chia}$ · $\\text{Số dư lớn nhất} = \\text{Số chia} - '
                        '1$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 25: Phép chia hết, phép chia có dư, **Công '
                        'thức liên hệ** được xác định bởi: $\\text{Số bị chia} = \\text{Thương} \\times '
                        '\\text{Số chia} + \\text{Số dư}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Phép chia hết, phép chia có dư**, nội dung/biểu thức $0 < \\text{Số dư} < '
                 '\\text{Số chia}$ · $\\text{Số dư lớn nhất} = \\text{Số chia} - 1$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Điều kiện số dư', 'Công thức liên hệ', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 25: Phép chia hết, phép chia có dư, biểu thức/quy tắc $0 < \\text{Số dư} '
                        '< \\text{Số chia}$ · $\\text{Số dư lớn nhất} = \\text{Số chia} - 1$ chính là nội '
                        'dung của **Điều kiện số dư**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một số chia cho $6$ được thương là $4$ và số dư là $3$. Số bị chia đó là:',
            'options': ['$24$', '$27$', '$22$', '$18$'],
            'answer': 1,
            'solution': 'Số bị chia $= 4 \\times 6 + 3 = 27$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Phép chia hết, phép chia có dư** (Chủ đề 4: Phép nhân, phép chia trong '
                 'phạm vi 100), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Phân biệt được phép chia hết (số dư bằng 0) và phép chia có dư.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 25: Phép chia hết, phép chia có dư: Phân biệt được '
                        'phép chia hết (số dư bằng 0) và phép chia có dư.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $38 : 5 = 6 \\text{ (dư } 8\\text{)}$ là đúng."',
            'answer': False,
            'solution': 'Sai vì số dư $8$ lớn hơn số chia $5$; kết quả đúng là $38 : 5 = 7 \\text{ (dư } '
                        '3\\text{)}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 25: Phép chia hết, phép chia có dư**, quy tắc **Công thức liên hệ** được xác '
                 'định bởi $\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$ và '
                 'áp dụng trực tiếp vào bài toán: “Có $34$ học sinh, mỗi bàn ngồi tối đa $4$ bạn. Cần ít '
                 'nhất bao nhiêu bàn để tất cả học sinh đều có chỗ ngồi?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Công thức liên hệ** ($\\text{Số bị chia} = '
                        '\\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$) là kiến thức cốt lõi của '
                        'Bài 25: Phép chia hết, phép chia có dư. Ta có phép chia: $34 : 4 = 8 \\text{ (dư } '
                        '2\\text{)}$. $8$ bàn ngồi được $32$ bạn, còn dư $2$ bạn cũng cần thêm $1$ bàn nữa. '
                        'Vậy số bàn cần í...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 25: Phép chia hết, phép chia có dư** để giải quyết tình huống '
                 'sau: Có $34$ học sinh, mỗi bàn ngồi tối đa $4$ bạn. Cần ít nhất bao nhiêu bàn để tất cả '
                 'học sinh đều có chỗ ngồi? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Ta có phép chia: $34 : 4 = 8 \\text{ (dư } 2\\text{)}$. $8$ bàn ngồi được $32$ bạn, '
                        'còn dư $2$ bạn cũng cần thêm $1$ bàn nữa. Vậy số bàn cần ít nhất là: $8 + 1 = '
                        '9\\text{ (bàn)}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 25: Phép chia hết, phép chia có dư: Ta có phép chia: $34 '
                        ': 4 = 8 \\text{ (dư } 2\\text{)}$.\n'
                        '$8$ bàn ngồi được $32$ bạn, còn dư $2$ bạn cũng cần thêm $1$ bàn nữa.\n'
                        'Vậy số bàn cần ít nhất là: $8 + 1 = 9\\text{ (bàn)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Đoàn khách du lịch có $26$ người muốn thuê thuyền qua sông, mỗi thuyền chở được nhiều nhất '
                 '$6$ người (không kể người lái). Hỏi đoàn cần thuê ít nhất bao nhiêu chiếc thuyền?',
            'answer': ['5'],
            'unit': 'thuyền',
            'solution': 'Ta có $26 : 6 = 4 \\text{ (dư } 2\\text{)}$. Cần thêm $1$ thuyền cho $2$ người còn '
                        'lại: $4 + 1 = 5\\text{ (thuyền)}$.\n'
                        'Đáp số: **$5\\text{ thuyền}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd04-nhan-chia-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép nhân, phép chia trong phạm vi 100',
  'context': 'SGK Toán 3 · Chủ đề 4: Phép nhân, phép chia trong phạm vi 100.',
  'title': 'Bài 26: Chia số có hai chữ số cho số có một chữ số',
  'icon': '📝',
  'description': 'Đặt tính dọc và thực hiện phép chia số có hai chữ số cho số có một chữ số (chia hết và '
                 'chia có dư).',
  'requirements': ['Đặt tính dọc và chia đúng số có hai chữ số cho số có một chữ số từ hàng chục đến hàng '
                   'đơn vị.',
                   'Thực hiện được cả trường hợp chia hết và chia có dư ở từng lượt chia.',
                   'Vận dụng phép chia để giải toán thực tế.'],
  'definition': '- Khi chia số có hai chữ số cho số có một chữ số, ta chia từ trái sang phải: chia chữ số '
                '**hàng chục** trước, rồi hạ chữ số **hàng đơn vị** xuống để chia tiếp.\n'
                '- Ở mỗi lượt chia, ta thực hiện đúng $4$ bước: **Chia $\\rightarrow$ Nhân $\\rightarrow$ '
                'Trừ $\\rightarrow$ Hạ**.',
  'theory': '### 1. Lượt chia thứ nhất không dư\n'
            '- Ví dụ: $84 : 4$. Lượt 1: $8 : 4 = 2$, $2 \\times 4 = 8$, $8 - 8 = 0$. Lượt 2: hạ $4$, $4 : 4 '
            '= 1$, $1 \\times 4 = 4$, $4 - 4 = 0$. Vậy $84 : 4 = 21$.\n'
            '### 2. Lượt chia thứ nhất có dư\n'
            '- Ví dụ: $75 : 3$. Lượt 1: $7 : 3 = 2$, $2 \\times 3 = 6$, $7 - 6 = 1$. Lượt 2: hạ $5$ được '
            '$15$; $15 : 3 = 5$, $5 \\times 3 = 15$, $15 - 15 = 0$. Vậy $75 : 3 = 25$.',
  'formulas': [{'category': 'I. Quy trình 4 bước mỗi lượt chia',
                'items': [{'name': 'Bước 1 – 4',
                           'formula': 'Chia $\\rightarrow$ Nhân $\\rightarrow$ Trừ $\\rightarrow$ Hạ chữ số '
                                      'tiếp theo'},
                          {'name': 'Kiểm tra',
                           'formula': '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số '
                                      'bị chia}$'}]}],
  'example': 'Đặt tính rồi tính: $96 : 3$ và $85 : 5$.',
  'example_answer': '- $96 : 3$: $9 : 3 = 3$; hạ $6$, $6 : 3 = 2$ $\\rightarrow$ **$32$**.\n'
                    '- $85 : 5$: $8 : 5 = 1$ (dư $3$); hạ $5$ được $35$, $35 : 5 = 7$ $\\rightarrow$ '
                    '**$17$**.',
  'real_life': '- Chia đều $90$ quyển sách vào $6$ ngăn tủ; tính số bó hoa khi bó $72$ bông hồng mỗi bó $6$ '
               'bông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $84 : 4$ là:',
            'options': ['$12$', '$24$', '$21$', '$42$'],
            'answer': 2,
            'solution': 'Ta chia từng hàng: $8 : 4 = 2$ và $4 : 4 = 1 \\rightarrow 21$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $75 : 3$ là:',
            'options': ['$15$', '$35$', '$21$', '$25$'],
            'answer': 3,
            'solution': 'Ta có $7 : 3 = 2$ dư $1$, hạ $5$ được $15 : 3 = 5 \\rightarrow 25$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 26: Chia số có hai chữ số cho số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Bước 1 – 4**?',
            'options': ['Chia $\\rightarrow$ Nhân $\\rightarrow$ Trừ $\\rightarrow$ Hạ chữ số tiếp theo',
                        '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 26: Chia số có hai chữ số cho số có một chữ '
                        'số, **Bước 1 – 4** được xác định bởi: Chia $\\rightarrow$ Nhân $\\rightarrow$ Trừ '
                        '$\\rightarrow$ Hạ chữ số tiếp theo.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Chia số có hai chữ số cho số có một chữ số**, nội dung/biểu thức '
                 '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Bước 1 – 4', 'Kiểm tra', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 26: Chia số có hai chữ số cho số có một chữ số, biểu thức/quy tắc '
                        '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$ chính '
                        'là nội dung của **Kiểm tra**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phép chia $67 : 4$ có thương và số dư là:',
            'options': ['Thương $15$, dư $7$',
                        'Thương $17$, dư $1$',
                        'Thương $16$, dư $3$',
                        'Thương $16$, dư $1$'],
            'answer': 2,
            'solution': 'Ta có $6 : 4 = 1$ dư $2$; hạ $7$ được $27 : 4 = 6$ dư $3$ $\\rightarrow$ **Thương '
                        '$16$, dư $3$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Chia số có hai chữ số cho số có một chữ số** (Chủ đề 4: Phép nhân, phép '
                 'chia trong phạm vi 100), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Đặt tính dọc và chia đúng số có hai chữ số cho số có một chữ số từ hàng chục đến '
                        'hàng đơn vị.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 26: Chia số có hai chữ số cho số có một chữ số: Đặt '
                        'tính dọc và chia đúng số có hai chữ số cho số có một chữ số từ hàng chục đến hàng '
                        'đơn vị.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Kết quả của phép chia $96 : 3$ bằng $32$."',
            'answer': True,
            'solution': 'Vì $32 \\times 3 = 96$ nên $96 : 3 = 32$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 26: Chia số có hai chữ số cho số có một chữ số**, quy tắc **Bước 1 – 4** được '
                 'xác định bởi Chia $\\rightarrow$ Nhân $\\rightarrow$ Trừ $\\rightarrow$ Hạ chữ số tiếp '
                 'theo và áp dụng trực tiếp vào bài toán: “Đặt tính rồi tính: $96 : 3$ và $85 : 5$.”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Bước 1 – 4** (Chia $\\rightarrow$ Nhân '
                        '$\\rightarrow$ Trừ $\\rightarrow$ Hạ chữ số tiếp theo) là kiến thức cốt lõi của Bài '
                        '26: Chia số có hai chữ số cho số có một chữ số. - $96 : 3$: $9 : 3 = 3$; hạ $6$, $6 '
                        ': 3 = 2$ $\\rightarrow$ **$32$**. - $85 : 5$: $8 : 5 = 1$ (dư $3$); hạ $5$ được '
                        '$35$, $35 : 5 = 7$ $\\rightarrow$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 26: Chia số có hai chữ số cho số có một chữ số** để giải quyết '
                 'tình huống sau: Đặt tính rồi tính: $96 : 3$ và $85 : 5$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['- $96 : 3$: $9 : 3 = 3$; hạ $6$, $6 : 3 = 2$ $\\rightarrow$ **$32$**. - $85 : 5$: '
                        '$8 : 5 = 1$ (dư $3$); hạ $5$ được $35$, $35 : 5 = 7$ $\\rightarrow$ **$17$*...',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 26: Chia số có hai chữ số cho số có một chữ số: - $96 : '
                        '3$: $9 : 3 = 3$; hạ $6$, $6 : 3 = 2$ $\\rightarrow$ **$32$**.\n'
                        '- $85 : 5$: $8 : 5 = 1$ (dư $3$); hạ $5$ được $35$, $35 : 5 = 7$ $\\rightarrow$ '
                        '**$17$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Người ta xếp đều $96$ bánh xà phòng vào $8$ hộp. Hỏi mỗi hộp có bao nhiêu bánh xà phòng?',
            'answer': ['12'],
            'unit': 'bánh',
            'solution': 'Số bánh xà phòng trong mỗi hộp là: $96 : 8 = 12\\text{ (bánh)}$.\n'
                        'Đáp số: **$12\\text{ bánh}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd04-nhan-chia-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép nhân, phép chia trong phạm vi 100',
  'context': 'SGK Toán 3 · Chủ đề 4: Phép nhân, phép chia trong phạm vi 100.',
  'title': 'Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập chung',
  'icon': '🧠',
  'description': 'Phương pháp phân tích và trình bày bài giải bài toán có lời văn bằng hai bước tính.',
  'requirements': ['Xác định được đại lượng trung gian cần tìm ở bước thứ nhất.',
                   'Trình bày rõ ràng hai lời giải, hai phép tính và đáp số.',
                   'Giải được các bài toán tổng – hiệu – gấp – giảm kết hợp hai bước tính.'],
  'definition': '- **Bài toán giải bằng $2$ bước tính** là bài toán cần thực hiện liên tiếp $2$ phép tính:\n'
                '  - **Bước 1**: Tìm đại lượng chưa biết (thành phần trung gian).\n'
                '  - **Bước 2**: Dùng kết quả vừa tìm được ở Bước 1 để tính đại lượng bài toán hỏi.',
  'theory': '### 1. Dạng toán tìm tổng hoặc hiệu khi một số gấp/giảm $n$ lần\n'
            '- Ví dụ: Tổ 1 trồng $15$ cây, tổ 2 trồng gấp $3$ lần tổ 1. Tìm tổng số cây cả hai tổ.\n'
            '- Bước 1: Số cây tổ 2 trồng là $15 \\times 3 = 45$ (cây).\n'
            '- Bước 2: Cả hai tổ trồng được là $15 + 45 = 60$ (cây).\n'
            '### 2. Lưu ý khi trình bày\n'
            '- Tóm tắt bài toán bằng sơ đồ đoạn thẳng để dễ nhìn mối quan hệ giữa các đại lượng.',
  'formulas': [{'category': 'I. Sơ đồ hai bước tính',
                'items': [{'name': 'Bước 1',
                           'formula': 'Tìm giá trị đại lượng thứ hai (nhân, chia, cộng hoặc trừ)'},
                          {'name': 'Bước 2',
                           'formula': 'Tính tổng $A + B$ hoặc hiệu $A - B$ theo yêu cầu đề bài'}]}],
  'example': 'Thùng thứ nhất có $15\\text{ l}$ dầu, thùng thứ hai có số dầu gấp $3$ lần thùng thứ nhất. Hỏi '
             'cả hai thùng có bao nhiêu lít dầu?',
  'example_answer': '- Bước 1: Số lít dầu ở thùng thứ hai là: $15 \\times 3 = 45\\text{ (l)}$.\n'
                    '- Bước 2: Số lít dầu ở cả hai thùng là: $15 + 45 = 60\\text{ (l)}$.\n'
                    'Đáp số: **$60\\text{ l}$**.',
  'real_life': '- Tính tổng số tiền khi mua hai món hàng mà giá món thứ hai biết theo món thứ nhất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Để giải bài toán: "Ngăn trên có $20$ quyển sách, ngăn dưới có nhiều hơn ngăn trên $5$ '
                 'quyển. Hỏi cả hai ngăn có bao nhiêu quyển sách?", ở bước 1 ta cần tìm:',
            'options': ['Tổng số sách hai ngăn',
                        'Hiệu số sách hai ngăn',
                        'Số sách ngăn trên',
                        'Số sách ở ngăn dưới'],
            'answer': 3,
            'solution': 'Bước 1 ta phải tìm **số sách ở ngăn dưới** ($20 + 5 = 25$ quyển), rồi mới tính '
                        'tổng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Anh có $24$ viên bi, em có số bi bằng số bi của anh giảm đi $3$ lần. Số bi của em là:',
            'options': ['$8$ viên', '$21$ viên', '$27$ viên', '$72$ viên'],
            'answer': 0,
            'solution': 'Số bi của em là: $24 : 3 = 8\\text{ (viên)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Bước 1**?',
            'options': ['Tính tổng $A + B$ hoặc hiệu $A - B$ theo yêu cầu đề bài',
                        'Tìm giá trị đại lượng thứ hai (nhân, chia, cộng hoặc trừ)',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 28, 29: Bài toán giải bằng hai bước tính và '
                        'luyện tập chung, **Bước 1** được xác định bởi: Tìm giá trị đại lượng thứ hai (nhân, '
                        'chia, cộng hoặc trừ).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập chung**, nội dung/biểu '
                 'thức Tính tổng $A + B$ hoặc hiệu $A - B$ theo yêu cầu đề bài là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Bước 1', 'Phân tích số', 'Bước 2', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập chung, biểu '
                        'thức/quy tắc Tính tổng $A + B$ hoặc hiệu $A - B$ theo yêu cầu đề bài chính là nội '
                        'dung của **Bước 2**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bao gạo tẻ nặng $36\\text{ kg}$, bao gạo nếp nhẹ hơn bao gạo tẻ $18\\text{ kg}$. Cả hai '
                 'bao gạo nặng là:',
            'options': ['$18\\text{ kg}$', '$72\\text{ kg}$', '$44\\text{ kg}$', '$54\\text{ kg}$'],
            'answer': 3,
            'solution': 'Bao gạo nếp nặng: $36 - 18 = 18\\text{ (kg)}$. Cả hai bao nặng: $36 + 18 = '
                        '54\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập chung** (Chủ đề 4: '
                 'Phép nhân, phép chia trong phạm vi 100), khẳng định nào sau đây phản ánh **đúng** yêu cầu '
                 'cần đạt và bản chất kiến thức của bài?',
            'options': ['Xác định được đại lượng trung gian cần tìm ở bước thứ nhất.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập '
                        'chung: Xác định được đại lượng trung gian cần tìm ở bước thứ nhất.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Can thứ nhất có $10\\text{ l}$ nước, can thứ hai có gấp đôi can thứ nhất thì '
                 'cả hai can có $20\\text{ l}$ nước."',
            'answer': False,
            'solution': 'Can thứ hai có $10 \\times 2 = 20\\text{ (l)}$, cả hai can có $10 + 20 = 30\\text{ '
                        '(l)}$, không phải $20\\text{ l}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập chung**, quy tắc **Bước '
                 '1** được xác định bởi Tìm giá trị đại lượng thứ hai (nhân, chia, cộng hoặc trừ) và áp dụng '
                 'trực tiếp vào bài toán: “Thùng thứ nhất có $15\\text{ l}$ dầu, thùng thứ hai có số dầu gấp '
                 '$3$ lần thùng thứ nhất. Hỏi cả hai thùng có bao nhiêu lít dầu?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Bước 1** (Tìm giá trị đại lượng thứ hai (nhân, chia, '
                        'cộng hoặc trừ)) là kiến thức cốt lõi của Bài 28, 29: Bài toán giải bằng hai bước '
                        'tính và luyện tập chung. - Bước 1: Số lít dầu ở thùng thứ hai là: $15 \\times 3 = '
                        '45\\text{ (l)}$. - Bước 2: Số lít dầu ở cả hai thùng là: $15 + 45 = 60\\text{ '
                        '(l)}$. Đ...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập chung** để '
                 'giải quyết tình huống sau: Thùng thứ nhất có $15\\text{ l}$ dầu, thùng thứ hai có số dầu '
                 'gấp $3$ lần thùng thứ nhất. Hỏi cả hai thùng có bao nhiêu lít dầu? Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- Bước 1: Số lít dầu ở thùng thứ hai là: $15 \\times 3 = 45\\text{ (l)}$. - Bước 2: '
                        'Số lít dầu ở cả hai thùng là: $15 + 45 = 60\\text{ (l)}$. Đáp số: **$60\\text{ '
                        'l}$...',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 28, 29: Bài toán giải bằng hai bước tính và luyện tập '
                        'chung: - Bước 1: Số lít dầu ở thùng thứ hai là: $15 \\times 3 = 45\\text{ (l)}$.\n'
                        '- Bước 2: Số lít dầu ở cả hai thùng là: $15 + 45 = 60\\text{ (l)}$.\n'
                        'Đáp số: **$60\\text{ l}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lan có $12$ nhãn vở, Hoa có số nhãn vở gấp $4$ lần Lan. Hỏi Hoa có nhiều hơn Lan bao nhiêu '
                 'nhãn vở?',
            'answer': ['36'],
            'unit': 'nhãn vở',
            'solution': 'Hoa có: $12 \\times 4 = 48\\text{ (nhãn vở)}$. Hoa nhiều hơn Lan: $48 - 12 = '
                        '36\\text{ (nhãn vở)}$.\n'
                        'Đáp số: **$36\\text{ nhãn vở}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd05-don-vi-do-do-dai-khoi-luong-dung-tich-nhiet-do',
  'context_title': 'Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ',
  'context': 'SGK Toán 3 · Chủ đề 5: Một số đơn vị đo độ dài (mm), khối lượng (g), dung tích (ml), nhiệt độ '
             '(độ C).',
  'title': 'Bài 30: Mi-li-mét',
  'icon': '📏',
  'description': 'Nhận biết đơn vị đo độ dài mi-li-mét (mm) và mối quan hệ giữa m, dm, cm, mm.',
  'requirements': ['Nhận biết được đơn vị đo độ dài mi-li-mét ($\\text{mm}$) trên thước kẻ.',
                   'Nắm vững mối quan hệ: $1\\text{ cm} = 10\\text{ mm}$, $1\\text{ dm} = 100\\text{ mm}$, '
                   '$1\\text{ m} = 1\\,000\\text{ mm}$.',
                   'Thực hiện được đổi đơn vị và tính toán với số đo độ dài có đơn vị $\\text{mm}$.'],
  'definition': '- **Mi-li-mét** là một đơn vị đo độ dài (dùng để đo những vật rất nhỏ hoặc rất mỏng), viết '
                'tắt là $\\text{mm}$.\n'
                '- Quan hệ quy đổi: $1\\text{ cm} = 10\\text{ mm}$; $1\\text{ dm} = 100\\text{ mm}$; '
                '$1\\text{ m} = 1\\,000\\text{ mm}$.',
  'theory': '### 1. Nhận biết $1\\text{ mm}$ trên thước kẻ\n'
            '- Khoảng cách giữa hai vạch chia nhỏ nhất liên tiếp trên thước kẻ học sinh chính là $1\\text{ '
            'mm}$.\n'
            '- Từ vạch $0$ đến vạch $1\\text{ cm}$ có $10$ khoảng nhỏ nên $1\\text{ cm} = 10\\text{ mm}$.\n'
            '### 2. Chuyển đổi đơn vị đo độ dài\n'
            '- Ví dụ: $4\\text{ cm} = 40\\text{ mm}$; $3\\text{ cm } 5\\text{ mm} = 30\\text{ mm} + 5\\text{ '
            'mm} = 35\\text{ mm}$.',
  'formulas': [{'category': 'I. Quan hệ đơn vị độ dài',
                'items': [{'name': 'Quy đổi sang mm',
                           'formula': '$1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ dm} = 100\\text{ mm}$ · '
                                      '$1\\text{ m} = 1\\,000\\text{ mm}$'}]}],
  'example': 'Đổi các đơn vị sau: $6\\text{ cm} = \\dots\\text{ mm}$; $2\\text{ cm } 8\\text{ mm} = '
             '\\dots\\text{ mm}$.',
  'example_answer': '- $6\\text{ cm} = 60\\text{ mm}$.\n'
                    '- $2\\text{ cm } 8\\text{ mm} = 20\\text{ mm} + 8\\text{ mm} = 28\\text{ mm}$.',
  'real_life': '- Đo bề dày của quyển sách giáo khoa, bề dày đồng xu, lượng mưa tính bằng $\\text{mm}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ cm} = \\dots\\text{ mm}$?',
            'options': ['$10$', '$100$', '$1\\,000$', '$1$'],
            'answer': 0,
            'solution': 'Ta có $1\\text{ cm} = 10\\text{ mm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Mi-li-mét được viết tắt là:',
            'options': ['$\\text{m}$', '$\\text{mm}$', '$\\text{cm}$', '$\\text{ml}$'],
            'answer': 1,
            'solution': 'Mi-li-mét viết tắt là **$\\text{mm}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 30: Mi-li-mét**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Quy đổi sang mm**?',
            'options': ['$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ dm} = 100\\text{ mm}$ · $1\\text{ m} = '
                        '1\\,000\\text{ mm}$',
                        'So sánh hàng trăm $\\rightarrow$ hàng chục $\\rightarrow$ hàng đơn vị'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 30: Mi-li-mét, **Quy đổi sang mm** được xác '
                        'định bởi: $1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ dm} = 100\\text{ mm}$ · '
                        '$1\\text{ m} = 1\\,000\\text{ mm}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Mi-li-mét**, nội dung/biểu thức $1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ '
                 'dm} = 100\\text{ mm}$ · $1\\text{ m} = 1\\,000\\text{ mm}$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Phân tích số', 'Số tròn trăm, tròn nghìn', 'Cùng số chữ số', 'Quy đổi sang mm'],
            'answer': 3,
            'solution': 'Trong Bài 30: Mi-li-mét, biểu thức/quy tắc $1\\text{ cm} = 10\\text{ mm}$ · '
                        '$1\\text{ dm} = 100\\text{ mm}$ · $1\\text{ m} = 1\\,000\\text{ mm}$ chính là nội '
                        'dung của **Quy đổi sang mm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm $5\\text{ cm } 4\\text{ mm} = \\dots\\text{ mm}$ là:',
            'options': ['$54$', '$9$', '$504$', '$45$'],
            'answer': 0,
            'solution': 'Đổi $5\\text{ cm} = 50\\text{ mm}$, cộng thêm $4\\text{ mm}$ được **$54\\text{ '
                        'mm}$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Mi-li-mét** (Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, '
                 'nhiệt độ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Nhận biết được đơn vị đo độ dài mi-li-mét ($\\text{mm}$) trên thước kẻ.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 30: Mi-li-mét: Nhận biết được đơn vị đo độ dài '
                        'mi-li-mét ($\\text{mm}$) trên thước kẻ.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$1\\text{ m} = 1\\,000\\text{ mm}$."',
            'answer': True,
            'solution': 'Vì $1\\text{ m} = 100\\text{ cm} = 100 \\times 10\\text{ mm} = 1\\,000\\text{ mm}$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 30: Mi-li-mét**, quy tắc **Quy đổi sang mm** được xác định bởi $1\\text{ cm} = '
                 '10\\text{ mm}$ · $1\\text{ dm} = 100\\text{ mm}$ · $1\\text{ m} = 1\\,000\\text{ mm}$ và '
                 'áp dụng trực tiếp vào bài toán: “Đổi các đơn vị sau: $6\\text{ cm} = \\dots\\text{ mm}$; '
                 '$2\\text{ cm } 8\\text{ mm} = \\dots\\text{ mm}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy đổi sang mm** ($1\\text{ cm} = 10\\text{ mm}$ · '
                        '$1\\text{ dm} = 100\\text{ mm}$ · $1\\text{ m} = 1\\,000\\text{ mm}$) là kiến thức '
                        'cốt lõi của Bài 30: Mi-li-mét. - $6\\text{ cm} = 60\\text{ mm}$. - $2\\text{ cm } '
                        '8\\text{ mm} = 20\\text{ mm} + 8\\text{ mm} = 28\\text{ mm}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 30: Mi-li-mét** để giải quyết tình huống sau: Đổi các đơn vị sau: '
                 '$6\\text{ cm} = \\dots\\text{ mm}$; $2\\text{ cm } 8\\text{ mm} = \\dots\\text{ mm}$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        '- $6\\text{ cm} = 60\\text{ mm}$. - $2\\text{ cm } 8\\text{ mm} = 20\\text{ mm} + '
                        '8\\text{ mm} = 28\\text{ mm}$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 30: Mi-li-mét: - $6\\text{ cm} = 60\\text{ mm}$.\n'
                        '- $2\\text{ cm } 8\\text{ mm} = 20\\text{ mm} + 8\\text{ mm} = 28\\text{ mm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cuốn từ điển dày $4\\text{ cm}$, một cuốn vở dày $6\\text{ mm}$. Hỏi cả hai cuốn xếp '
                 'chồng lên nhau dày bao nhiêu mi-li-mét?',
            'answer': ['46'],
            'unit': 'mm',
            'solution': 'Đổi $4\\text{ cm} = 40\\text{ mm}$. Tổng bề dày là: $40 + 6 = 46\\text{ (mm)}$.\n'
                        'Đáp số: **$46\\text{ mm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd05-don-vi-do-do-dai-khoi-luong-dung-tich-nhiet-do',
  'context_title': 'Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ',
  'context': 'SGK Toán 3 · Chủ đề 5: Một số đơn vị đo độ dài (mm), khối lượng (g), dung tích (ml), nhiệt độ '
             '(độ C).',
  'title': 'Bài 31: Gam',
  'icon': '⚖️',
  'description': 'Nhận biết đơn vị đo khối lượng gam (g), mối quan hệ giữa kg và g, cách đọc số đo trên cân.',
  'requirements': ['Nhận biết được đơn vị đo khối lượng gam ($\\text{g}$) dùng để cân các vật nhẹ.',
                   'Nắm vững mối quan hệ: $1\\text{ kg} = 1\\,000\\text{ g}$.',
                   'Thực hiện được phép cộng, trừ, nhân, chia với đơn vị $\\text{g}$ và giải toán thực tế.'],
  'definition': '- **Gam** là đơn vị đo khối lượng, viết tắt là $\\text{g}$.\n'
                '- Quan hệ với ki-lô-gam: $1\\text{ kg} = 1\\,000\\text{ g}$ (hay $1\\,000\\text{ g} = '
                '1\\text{ kg}$).',
  'theory': '### 1. Dụng cụ cân và các quả cân\n'
            '- Để cân các vật nhẹ dưới $1\\text{ kg}$, người ta thường dùng cân đĩa với các quả cân '
            '$100\\text{ g}, 200\\text{ g}, 500\\text{ g}$ hoặc cân đồng hồ, cân điện tử chia theo vạch '
            '$\\text{g}$.\n'
            '### 2. Chuyển đổi và tính toán\n'
            '- Khi cộng hoặc trừ khối lượng có đơn vị khác nhau ($\\text{kg}$ và $\\text{g}$), ta phải đổi '
            'về cùng đơn vị $\\text{g}$ trước khi tính.',
  'formulas': [{'category': 'I. Đơn vị khối lượng',
                'items': [{'name': 'Quy đổi',
                           'formula': '$1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\,000\\text{ g} = 1\\text{ '
                                      'kg}$'},
                          {'name': 'Mốc thường gặp', 'formula': 'Nửa ki-lô-gam $= 500\\text{ g}$'}]}],
  'example': 'Quả dưa hấu cân nặng $2\\text{ kg}$, quả bí cân nặng $750\\text{ g}$. Hỏi quả dưa hấu nặng hơn '
             'quả bí bao nhiêu gam?',
  'example_answer': 'Đổi $2\\text{ kg} = 2\\,000\\text{ g}$.\n'
                    'Quả dưa hấu nặng hơn quả bí số gam là: $2\\,000 - 750 = 1\\,250\\text{ (g)}$.',
  'real_life': '- Xem khối lượng tịnh trên gói mì ăn liền ($75\\text{ g}$), gói muối ($500\\text{ g}$), hộp '
               'bơ ($200\\text{ g}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ kg} = \\dots\\text{ g}$?',
            'options': ['$10$', '$1\\,000$', '$100$', '$500$'],
            'answer': 1,
            'solution': 'Ta có $1\\text{ kg} = 1\\,000\\text{ g}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $500\\text{ g} + 300\\text{ g}$ là:',
            'options': ['$8\\text{ kg}$', '$200\\text{ g}$', '$800\\text{ g}$', '$800\\text{ kg}$'],
            'answer': 2,
            'solution': 'Ta có $500 + 300 = 800\\text{ (g)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 31: Gam**, công thức hoặc quy tắc nào sau đây biểu diễn '
                 'đúng **Quy đổi**?',
            'options': ['Nửa ki-lô-gam $= 500\\text{ g}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\,000\\text{ g} = 1\\text{ kg}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 31: Gam, **Quy đổi** được xác định bởi: '
                        '$1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\,000\\text{ g} = 1\\text{ kg}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Gam**, nội dung/biểu thức Nửa ki-lô-gam $= 500\\text{ g}$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Mốc thường gặp', 'Quy đổi', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 31: Gam, biểu thức/quy tắc Nửa ki-lô-gam $= 500\\text{ g}$ chính là nội '
                        'dung của **Mốc thường gặp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mẹ mua $1\\text{ kg}$ đường, mẹ đã dùng hết $400\\text{ g}$ đường để nấu chè. Số đường còn '
                 'lại là:',
            'options': ['$500\\text{ g}$', '$600\\text{ g}$', '$399\\text{ g}$', '$60\\text{ g}$'],
            'answer': 1,
            'solution': 'Đổi $1\\text{ kg} = 1\\,000\\text{ g}$. Còn lại: $1\\,000 - 400 = 600\\text{ (g)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Gam** (Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt '
                 'độ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Nhận biết được đơn vị đo khối lượng gam ($\\text{g}$) dùng để cân các vật nhẹ.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 31: Gam: Nhận biết được đơn vị đo khối lượng gam '
                        '($\\text{g}$) dùng để cân các vật nhẹ.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Một quả trứng gà thông thường cân nặng khoảng $50\\text{ kg}$."',
            'answer': False,
            'solution': 'Quả trứng gà nặng khoảng $50\\text{ g}$, không phải $50\\text{ kg}$ $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 31: Gam**, quy tắc **Quy đổi** được xác định bởi $1\\text{ kg} = '
                 '1\\,000\\text{ g}$ · $1\\,000\\text{ g} = 1\\text{ kg}$ và áp dụng trực tiếp vào bài toán: '
                 '“Quả dưa hấu cân nặng $2\\text{ kg}$, quả bí cân nặng $750\\text{ g}$. Hỏi quả dưa hấu '
                 'nặng hơn quả bí bao nhiêu gam?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy đổi** ($1\\text{ kg} = 1\\,000\\text{ g}$ · '
                        '$1\\,000\\text{ g} = 1\\text{ kg}$) là kiến thức cốt lõi của Bài 31: Gam. Đổi '
                        '$2\\text{ kg} = 2\\,000\\text{ g}$. Quả dưa hấu nặng hơn quả bí số gam là: $2\\,000 '
                        '- 750 = 1\\,250\\text{ (g)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 31: Gam** để giải quyết tình huống sau: Quả dưa hấu cân nặng '
                 '$2\\text{ kg}$, quả bí cân nặng $750\\text{ g}$. Hỏi quả dưa hấu nặng hơn quả bí bao nhiêu '
                 'gam? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Đổi $2\\text{ kg} = 2\\,000\\text{ g}$. Quả dưa hấu nặng hơn quả bí số gam là: '
                        '$2\\,000 - 750 = 1\\,250\\text{ (g)}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 31: Gam: Đổi $2\\text{ kg} = 2\\,000\\text{ g}$.\n'
                        'Quả dưa hấu nặng hơn quả bí số gam là: $2\\,000 - 750 = 1\\,250\\text{ (g)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một gói bánh cân nặng $250\\text{ g}$. Hỏi $4$ gói bánh như thế cân nặng bao nhiêu '
                 'ki-lô-gam?',
            'answer': ['1'],
            'unit': 'kg',
            'solution': 'Bốn gói bánh nặng: $250 \\times 4 = 1\\,000\\text{ (g)} = 1\\text{ (kg)}$.\n'
                        'Đáp số: **$1\\text{ kg}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd05-don-vi-do-do-dai-khoi-luong-dung-tich-nhiet-do',
  'context_title': 'Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ',
  'context': 'SGK Toán 3 · Chủ đề 5: Một số đơn vị đo độ dài (mm), khối lượng (g), dung tích (ml), nhiệt độ '
             '(độ C).',
  'title': 'Bài 32: Mi-li-lít',
  'icon': '🥛',
  'description': 'Nhận biết đơn vị đo dung tích mi-li-lít (ml) và mối quan hệ giữa lít (l) với mi-li-lít '
                 '(ml).',
  'requirements': ['Nhận biết được đơn vị đo dung tích mi-li-lít ($\\text{ml}$) dùng để đo lượng chất lỏng '
                   'nhỏ.',
                   'Nắm vững mối quan hệ: $1\\text{ l} = 1\\,000\\text{ ml}$.',
                   'Đọc được vạch chia trên ca đong và giải bài toán liên quan đến $\\text{l}, \\text{ml}$.'],
  'definition': '- **Mi-li-lít** là đơn vị đo dung tích (nhỏ hơn lít), viết tắt là $\\text{ml}$.\n'
                '- Quan hệ giữa lít và mi-li-lít: $1\\text{ l} = 1\\,000\\text{ ml}$ (hay $1\\,000\\text{ '
                'ml} = 1\\text{ l}$).',
  'theory': '### 1. Ước lượng dung tích với mi-li-lít\n'
            '- Một thìa nhỏ chứa khoảng $5\\text{ ml}$ nước; một hộp sữa tươi nhỏ thường có dung tích '
            '$180\\text{ ml}$; một chai nước suối vừa có dung tích $500\\text{ ml}$.\n'
            '### 2. Tính toán với đơn vị $\\text{ml}$\n'
            '- Khi thực hiện phép tính giữa $\\text{l}$ và $\\text{ml}$, ta đổi $1\\text{ l} = '
            '1\\,000\\text{ ml}$ rồi cộng, trừ như số tự nhiên.',
  'formulas': [{'category': 'I. Đơn vị dung tích',
                'items': [{'name': 'Quy đổi',
                           'formula': '$1\\text{ l} = 1\\,000\\text{ ml}$ · $1\\,000\\text{ ml} = 1\\text{ '
                                      'l}$'}]}],
  'example': 'Mẹ có $1\\text{ l}$ sữa, mẹ rót đều ra $3$ cốc, mỗi cốc $200\\text{ ml}$. Hỏi trong bình còn '
             'lại bao nhiêu mi-li-lít sữa?',
  'example_answer': 'Đổi $1\\text{ l} = 1\\,000\\text{ ml}$.\n'
                    'Số sữa đã rót ra $3$ cốc là: $200 \\times 3 = 600\\text{ (ml)}$.\n'
                    'Số sữa còn lại là: $1\\,000 - 600 = 400\\text{ (ml)}$.',
  'real_life': '- Đong si-rô ho bằng cốc chia vạch $\\text{ml}$; đọc dung tích trên vỏ hộp sữa, chai dầu ăn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ l} = \\dots\\text{ ml}$?',
            'options': ['$100$', '$10$', '$1\\,000$', '$10\\,000$'],
            'answer': 2,
            'solution': 'Ta có $1\\text{ l} = 1\\,000\\text{ ml}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bốn trăm năm mươi mi-li-lít được viết là:',
            'options': ['$45\\text{ ml}$', '$405\\text{ ml}$', '$450\\text{ l}$', '$450\\text{ ml}$'],
            'answer': 3,
            'solution': 'Bốn trăm năm mươi mi-li-lít viết là **$450\\text{ ml}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 32: Mi-li-lít**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Quy đổi**?',
            'options': ['$1\\text{ l} = 1\\,000\\text{ ml}$ · $1\\,000\\text{ ml} = 1\\text{ l}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'So sánh hàng trăm $\\rightarrow$ hàng chục $\\rightarrow$ hàng đơn vị'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 32: Mi-li-lít, **Quy đổi** được xác định bởi: '
                        '$1\\text{ l} = 1\\,000\\text{ ml}$ · $1\\,000\\text{ ml} = 1\\text{ l}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Mi-li-lít**, nội dung/biểu thức $1\\text{ l} = 1\\,000\\text{ ml}$ · '
                 '$1\\,000\\text{ ml} = 1\\text{ l}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phân tích số', 'Quy đổi', 'Số tròn trăm, tròn nghìn', 'Cùng số chữ số'],
            'answer': 1,
            'solution': 'Trong Bài 32: Mi-li-lít, biểu thức/quy tắc $1\\text{ l} = 1\\,000\\text{ ml}$ · '
                        '$1\\,000\\text{ ml} = 1\\text{ l}$ chính là nội dung của **Quy đổi**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một chai nước có $750\\text{ ml}$ nước, bạn Nam uống hết $250\\text{ ml}$. Trong chai còn '
                 'lại:',
            'options': ['$400\\text{ ml}$', '$1\\,000\\text{ ml}$', '$500\\text{ ml}$', '$50\\text{ ml}$'],
            'answer': 2,
            'solution': 'Trong chai còn lại: $750 - 250 = 500\\text{ (ml)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Mi-li-lít** (Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, '
                 'nhiệt độ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Nhận biết được đơn vị đo dung tích mi-li-lít ($\\text{ml}$) dùng để đo lượng chất '
                        'lỏng nhỏ.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 32: Mi-li-lít: Nhận biết được đơn vị đo dung tích '
                        'mi-li-lít ($\\text{ml}$) dùng để đo lượng chất lỏng nhỏ.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hai chai nước mỗi chai $500\\text{ ml}$ có tổng dung tích đúng bằng $1\\text{ '
                 'l}$."',
            'answer': True,
            'solution': 'Vì $500\\text{ ml} + 500\\text{ ml} = 1\\,000\\text{ ml} = 1\\text{ l}$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 32: Mi-li-lít**, quy tắc **Quy đổi** được xác định bởi $1\\text{ l} = '
                 '1\\,000\\text{ ml}$ · $1\\,000\\text{ ml} = 1\\text{ l}$ và áp dụng trực tiếp vào bài '
                 'toán: “Mẹ có $1\\text{ l}$ sữa, mẹ rót đều ra $3$ cốc, mỗi cốc $200\\text{ ml}$. Hỏi trong '
                 'bình còn lại bao nhiêu mi-li-lít sữa?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy đổi** ($1\\text{ l} = 1\\,000\\text{ ml}$ · '
                        '$1\\,000\\text{ ml} = 1\\text{ l}$) là kiến thức cốt lõi của Bài 32: Mi-li-lít. Đổi '
                        '$1\\text{ l} = 1\\,000\\text{ ml}$. Số sữa đã rót ra $3$ cốc là: $200 \\times 3 = '
                        '600\\text{ (ml)}$. Số sữa còn lại là: $1\\,000 - 600 = 400\\text{ (ml)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 32: Mi-li-lít** để giải quyết tình huống sau: Mẹ có $1\\text{ l}$ '
                 'sữa, mẹ rót đều ra $3$ cốc, mỗi cốc $200\\text{ ml}$. Hỏi trong bình còn lại bao nhiêu '
                 'mi-li-lít sữa? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Đổi $1\\text{ l} = 1\\,000\\text{ ml}$. Số sữa đã rót ra $3$ cốc là: $200 \\times 3 '
                        '= 600\\text{ (ml)}$. Số sữa còn lại là: $1\\,000 - 600 = 400\\text{ (ml)}$.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 32: Mi-li-lít: Đổi $1\\text{ l} = 1\\,000\\text{ ml}$.\n'
                        'Số sữa đã rót ra $3$ cốc là: $200 \\times 3 = 600\\text{ (ml)}$.\n'
                        'Số sữa còn lại là: $1\\,000 - 600 = 400\\text{ (ml)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp sữa tươi chứa $180\\text{ ml}$ sữa. Hỏi $5$ hộp sữa như thế chứa tất cả bao nhiêu '
                 'mi-li-lít sữa?',
            'answer': ['900'],
            'unit': 'ml',
            'solution': 'Tổng lượng sữa trong $5$ hộp là: $180 \\times 5 = 900\\text{ (ml)}$.\n'
                        'Đáp số: **$900\\text{ ml}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd05-don-vi-do-do-dai-khoi-luong-dung-tich-nhiet-do',
  'context_title': 'Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ',
  'context': 'SGK Toán 3 · Chủ đề 5: Một số đơn vị đo độ dài (mm), khối lượng (g), dung tích (ml), nhiệt độ '
             '(độ C).',
  'title': 'Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung',
  'icon': '🌡️',
  'description': 'Nhận biết đơn vị đo nhiệt độ (độ C), cách đọc nhiệt kế và thực hành các đơn vị mm, g, ml, '
                 'độ C.',
  'requirements': ['Nhận biết được đơn vị đo nhiệt độ là độ C (ký hiệu $^\\circ\\text{C}$) và dụng cụ đo '
                   'nhiệt độ là nhiệt kế.',
                   'Đọc được số đo nhiệt độ trên nhiệt kế và so sánh nhiệt độ các ngày/vùng miền.',
                   'Nắm được các mốc nhiệt độ quen thuộc (nước đá đang tan $0^\\circ\\text{C}$, cơ thể người '
                   '$37^\\circ\\text{C}$, nước sôi $100^\\circ\\text{C}$).'],
  'definition': '- **Độ C** (ký hiệu $^\\circ\\text{C}$) là đơn vị đo nhiệt độ. Dụng cụ dùng để đo nhiệt độ '
                'gọi là **nhiệt kế**.\n'
                '- Các mốc nhiệt độ cần nhớ: Nước đá đang tan ở $0^\\circ\\text{C}$; thân nhiệt người khỏe '
                'mạnh khoảng $37^\\circ\\text{C}$; nước sôi ở $100^\\circ\\text{C}$.',
  'theory': '### 1. Đọc và viết số đo nhiệt độ\n'
            '- Ví dụ: $25^\\circ\\text{C}$ đọc là "hai mươi lăm độ C".\n'
            '- Khi đọc nhiệt kế, ta nhìn vạch ngang của cột chất lỏng màu đỏ (hoặc số hiện trên nhiệt kế '
            'điện tử).\n'
            '### 2. So sánh nhiệt độ\n'
            '- Nhiệt độ cao hơn thì trời nóng hơn (hoặc nước ấm hơn); nhiệt độ thấp hơn thì trời lạnh hơn.',
  'formulas': [{'category': 'I. Các mốc nhiệt độ chuẩn',
                'items': [{'name': 'Nước đá tan', 'formula': '$0^\\circ\\text{C}$'},
                          {'name': 'Cơ thể người bình thường', 'formula': '$37^\\circ\\text{C}$'},
                          {'name': 'Hơi nước đang sôi', 'formula': '$100^\\circ\\text{C}$'}]}],
  'example': 'Buổi sáng nhiệt độ ở Hà Nội là $21^\\circ\\text{C}$, đến buổi trưa nhiệt độ tăng thêm '
             '$6^\\circ\\text{C}$. Hỏi buổi trưa nhiệt độ là bao nhiêu độ C?',
  'example_answer': 'Nhiệt độ buổi trưa ở Hà Nội là: $21^\\circ\\text{C} + 6^\\circ\\text{C} = '
                    '27^\\circ\\text{C}$.\n'
                    'Đáp số: **$27^\\circ\\text{C}$**.',
  'real_life': '- Xem bản tin dự báo thời tiết hằng ngày để mặc trang phục phù hợp; dùng nhiệt kế kiểm tra '
               'khi bị sốt.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dụng cụ dùng để đo nhiệt độ là:',
            'options': ['Cân đồng hồ', 'Thước thẳng', 'Ca đong', 'Nhiệt kế'],
            'answer': 3,
            'solution': 'Ta dùng **nhiệt kế** để đo nhiệt độ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nhiệt độ cơ thể người khỏe mạnh bình thường vào khoảng:',
            'options': ['$37^\\circ\\text{C}$',
                        '$100^\\circ\\text{C}$',
                        '$0^\\circ\\text{C}$',
                        '$73^\\circ\\text{C}$'],
            'answer': 0,
            'solution': 'Thân nhiệt bình thường của người khoảng **$37^\\circ\\text{C}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Nước đá tan**?',
            'options': ['$37^\\circ\\text{C}$',
                        '$0^\\circ\\text{C}$',
                        '$100^\\circ\\text{C}$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và '
                        'luyện tập chung, **Nước đá tan** được xác định bởi: $0^\\circ\\text{C}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung**, nội dung/biểu '
                 'thức $37^\\circ\\text{C}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Nước đá tan', 'Hơi nước đang sôi', 'Cơ thể người bình thường', 'Phân tích số'],
            'answer': 2,
            'solution': 'Trong Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung, biểu '
                        'thức/quy tắc $37^\\circ\\text{C}$ chính là nội dung của **Cơ thể người bình '
                        'thường**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nhiệt độ tại Sa Pa là $12^\\circ\\text{C}$, tại Cần Thơ là $31^\\circ\\text{C}$. Nhiệt độ '
                 'ở Cần Thơ cao hơn ở Sa Pa bao nhiêu độ C?',
            'options': ['$43^\\circ\\text{C}$',
                        '$21^\\circ\\text{C}$',
                        '$18^\\circ\\text{C}$',
                        '$19^\\circ\\text{C}$'],
            'answer': 3,
            'solution': 'Lấy $31 - 12 = 19\\text{ (}^\\circ\\text{C)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung** (Chủ đề 5: Một '
                 'số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được đơn vị đo nhiệt độ là độ C (ký hiệu $^\\circ\\text{C}$) và dụng cụ '
                        'đo nhiệt độ là nhiệt kế.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập '
                        'chung: Nhận biết được đơn vị đo nhiệt độ là độ C (ký hiệu $^\\circ\\text{C}$) và '
                        'dụng cụ đo nhiệt độ là nhiệt kế.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Nước sôi ở nhiệt độ $100^\\circ\\text{C}$ và nước đá đang tan ở '
                 '$0^\\circ\\text{C}$."',
            'answer': True,
            'solution': 'Đây là hai mốc nhiệt độ cơ bản của thang đo độ C $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung**, quy tắc **Nước '
                 'đá tan** được xác định bởi $0^\\circ\\text{C}$ và áp dụng trực tiếp vào bài toán: “Buổi '
                 'sáng nhiệt độ ở Hà Nội là $21^\\circ\\text{C}$, đến buổi trưa nhiệt độ tăng thêm '
                 '$6^\\circ\\text{C}$. Hỏi buổi trưa nhiệt độ là bao nhiêu đ...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nước đá tan** ($0^\\circ\\text{C}$) là kiến thức cốt '
                        'lõi của Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung. Nhiệt độ '
                        'buổi trưa ở Hà Nội là: $21^\\circ\\text{C} + 6^\\circ\\text{C} = '
                        '27^\\circ\\text{C}$. Đáp số: **$27^\\circ\\text{C}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập chung** để '
                 'giải quyết tình huống sau: Buổi sáng nhiệt độ ở Hà Nội là $21^\\circ\\text{C}$, đến buổi '
                 'trưa nhiệt độ tăng thêm $6^\\circ\\text{C}$. Hỏi buổi trưa nhiệt độ là bao nhiêu độ C? Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Nhiệt độ buổi trưa ở Hà Nội là: $21^\\circ\\text{C} + 6^\\circ\\text{C} = '
                        '27^\\circ\\text{C}$. Đáp số: **$27^\\circ\\text{C}$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 33, 34, 35: Nhiệt độ. Đơn vị đo nhiệt độ và luyện tập '
                        'chung: Nhiệt độ buổi trưa ở Hà Nội là: $21^\\circ\\text{C} + 6^\\circ\\text{C} = '
                        '27^\\circ\\text{C}$.\n'
                        'Đáp số: **$27^\\circ\\text{C}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Buổi trưa nhiệt độ ngoài trời là $34^\\circ\\text{C}$, đến ban đêm nhiệt độ giảm đi '
                 '$8^\\circ\\text{C}$. Hỏi ban đêm nhiệt độ ngoài trời là bao nhiêu độ C?',
            'answer': ['26'],
            'unit': '°C',
            'solution': 'Nhiệt độ ban đêm là: $34 - 8 = 26\\text{ (}^\\circ\\text{C)}$.\n'
                        'Đáp số: **$26^\\circ\\text{C}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd06-nhan-chia-pham-vi-1000',
  'context_title': 'Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000',
  'context': 'SGK Toán 3 · Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000; biểu thức số.',
  'title': 'Bài 36: Nhân số có ba chữ số với số có một chữ số',
  'icon': '🧮',
  'description': 'Đặt tính và thực hiện phép nhân số có ba chữ số với số có một chữ số (không nhớ và có '
                 'nhớ).',
  'requirements': ['Đặt tính và tính đúng phép nhân số có ba chữ số với số có một chữ số.',
                   'Tính nhẩm được phép nhân số tròn trăm với số có một chữ số.',
                   'Giải được bài toán thực tế liên quan đến nhân số có ba chữ số với số có một chữ số.'],
  'definition': '- Khi nhân số có ba chữ số với số có một chữ số, ta đặt tính thẳng cột rồi nhân lần lượt từ '
                'phải sang trái: **hàng đơn vị $\\rightarrow$ hàng chục $\\rightarrow$ hàng trăm**.\n'
                '- Ở lượt nhân nào có kết quả từ $10$ trở lên thì viết chữ số hàng đơn vị và nhớ chữ số hàng '
                'chục sang hàng kế tiếp bên trái.',
  'theory': '### 1. Phép nhân không nhớ\n'
            '- Ví dụ: $213 \\times 3$. Ta tính: $3 \\times 3 = 9$; $3 \\times 1 = 3$; $3 \\times 2 = 6$. Vậy '
            '$213 \\times 3 = 639$.\n'
            '### 2. Phép nhân có nhớ\n'
            '- Ví dụ: $134 \\times 4$. Ta tính: $4 \\times 4 = 16$ (viết $6$ nhớ $1$); $4 \\times 3 = 12$, '
            'thêm $1$ bằng $13$ (viết $3$ nhớ $1$); $4 \\times 1 = 4$, thêm $1$ bằng $5$. Vậy $134 \\times 4 '
            '= 536$.',
  'formulas': [{'category': 'I. Nhân số có ba chữ số',
                'items': [{'name': 'Thứ tự nhân',
                           'formula': 'Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm (cộng phần nhớ vào '
                                      'hàng liền sau)'},
                          {'name': 'Nhân số tròn trăm',
                           'formula': '$a00 \\times b = (a \\times b)00$',
                           'note': 'Ví dụ: $200 \\times 4 = 800$'}]}],
  'example': 'Đặt tính rồi tính: $125 \\times 4$ và $308 \\times 3$.',
  'example_answer': '- $125 \\times 4 = 500$ (vì $5 \\times 4 = 20$ viết $0$ nhớ $2$; $2 \\times 4 + 2 = 10$ '
                    'viết $0$ nhớ $1$; $1 \\times 4 + 1 = 5$).\n'
                    '- $308 \\times 3 = 924$ (vì $8 \\times 3 = 24$ viết $4$ nhớ $2$; $0 \\times 3 + 2 = 2$; '
                    '$3 \\times 3 = 9$).',
  'real_life': '- Tính tổng quãng đường khi chạy $3$ vòng sân vận động, mỗi vòng dài $250\\text{ m}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $213 \\times 3$ là:',
            'options': ['$639$', '$636$', '$216$', '$693$'],
            'answer': 0,
            'solution': 'Nhân từng hàng: $3 \\times 3 = 9$, $1 \\times 3 = 3$, $2 \\times 3 = 6 \\rightarrow '
                        '639$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $300 \\times 3 = ?$',
            'options': ['$600$', '$900$', '$303$', '$90$'],
            'answer': 1,
            'solution': '$3$ trăm $\\times 3 = 9$ trăm $= 900$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 36: Nhân số có ba chữ số với số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự nhân**?',
            'options': ['$a00 \\times b = (a \\times b)00$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm (cộng phần nhớ vào hàng liền sau)',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 36: Nhân số có ba chữ số với số có một chữ '
                        'số, **Thứ tự nhân** được xác định bởi: Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm (cộng phần nhớ vào hàng liền sau).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36: Nhân số có ba chữ số với số có một chữ số**, nội dung/biểu thức $a00 '
                 '\\times b = (a \\times b)00$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thứ tự nhân', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Nhân số tròn trăm'],
            'answer': 3,
            'solution': 'Trong Bài 36: Nhân số có ba chữ số với số có một chữ số, biểu thức/quy tắc $a00 '
                        '\\times b = (a \\times b)00$ chính là nội dung của **Nhân số tròn trăm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $125 \\times 4$ là:',
            'options': ['$500$', '$480$', '$520$', '$800$'],
            'answer': 0,
            'solution': 'Ta có $125 \\times 4 = 500$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 36: Nhân số có ba chữ số với số có một chữ số** (Chủ đề 6: Phép nhân, phép '
                 'chia trong phạm vi 1 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Đặt tính và tính đúng phép nhân số có ba chữ số với số có một chữ số.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 36: Nhân số có ba chữ số với số có một chữ số: Đặt '
                        'tính và tính đúng phép nhân số có ba chữ số với số có một chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tích của $206$ và $4$ bằng $804$."',
            'answer': False,
            'solution': 'Ta có $6 \\times 4 = 24$ (viết $4$ nhớ $2$), $0 \\times 4 + 2 = 2$, $2 \\times 4 = '
                        '8 \\Rightarrow 206 \\times 4 = 824$, không phải $804$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 36: Nhân số có ba chữ số với số có một chữ số**, quy tắc **Thứ tự nhân** được '
                 'xác định bởi Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm (cộng phần nhớ vào hàng liền '
                 'sau) và áp dụng trực tiếp vào bài toán: “Đặt tính rồi tính: $125 \\times 4$ và $308 '
                 '\\times 3$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự nhân** (Đơn vị $\\rightarrow$ Chục '
                        '$\\rightarrow$ Trăm (cộng phần nhớ vào hàng liền sau)) là kiến thức cốt lõi của Bài '
                        '36: Nhân số có ba chữ số với số có một chữ số. - $125 \\times 4 = 500$ (vì $5 '
                        '\\times 4 = 20$ viết $0$ nhớ $2$; $2 \\times 4 + 2 = 10$ viết $0$ nhớ $1$; $1 '
                        '\\times 4 + 1 = 5$). - $308 \\times 3 = 924$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 36: Nhân số có ba chữ số với số có một chữ số** để giải quyết '
                 'tình huống sau: Đặt tính rồi tính: $125 \\times 4$ và $308 \\times 3$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        '- $125 \\times 4 = 500$ (vì $5 \\times 4 = 20$ viết $0$ nhớ $2$; $2 \\times 4 + 2 = '
                        '10$ viết $0$ nhớ $1$; $1 \\times 4 + 1 = 5$). - $308 \\times 3 = 924$ (vì $8 '
                        '\\times 3 = 24$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 36: Nhân số có ba chữ số với số có một chữ số: - $125 '
                        '\\times 4 = 500$ (vì $5 \\times 4 = 20$ viết $0$ nhớ $2$; $2 \\times 4 + 2 = 10$ '
                        'viết $0$ nhớ $1$; $1 \\times 4 + 1 = 5$).\n'
                        '- $308 \\times 3 = 924$ (vì $8 \\times 3 = 24$ viết $4$ nhớ $2$; $0 \\times 3 + 2 = '
                        '2$; $3 \\times 3 = 9$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi chuyến máy bay chở được $215$ hành khách. Hỏi $4$ chuyến máy bay như thế chở được tất '
                 'cả bao nhiêu hành khách?',
            'answer': ['860'],
            'unit': 'hành khách',
            'solution': 'Tổng số hành khách là: $215 \\times 4 = 860\\text{ (hành khách)}$.\n'
                        'Đáp số: **$860\\text{ hành khách}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd06-nhan-chia-pham-vi-1000',
  'context_title': 'Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000',
  'context': 'SGK Toán 3 · Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000; biểu thức số.',
  'title': 'Bài 37: Chia số có ba chữ số cho số có một chữ số',
  'icon': '➗',
  'description': 'Thực hiện phép chia số có ba chữ số cho số có một chữ số (chia hết và chia có dư, thương '
                 'có chữ số 0).',
  'requirements': ['Đặt tính dọc và chia đúng số có ba chữ số cho số có một chữ số từ trái sang phải.',
                   'Xử lý đúng trường hợp chữ số hàng백 bé hơn số chia (lấy hai chữ số đầu để chia) và trường '
                   'hợp thương có chữ số 0.',
                   'Giải được bài toán thực tế có phép chia số có ba chữ số.'],
  'definition': '- Khi chia số có ba chữ số cho số có một chữ số, ta bắt đầu chia từ **hàng trăm** (bên trái '
                'sang phải).\n'
                '- Nếu chữ số hàng trăm bé hơn số chia thì ta lấy cả hàng trăm và hàng chục để chia ở lượt '
                'đầu tiên.\n'
                '- Từ lượt chia thứ hai trở đi, nếu số bị chia ở lượt đó bé hơn số chia thì ta phải **viết '
                '$0$ vào thương** rồi mới hạ tiếp.',
  'theory': '### 1. Thương có ba chữ số\n'
            '- Ví dụ: $648 : 3 = 216$. Trường hợp có chữ số $0$ ở thương: $618 : 3$: $6 : 3 = 2$; hạ $1$, vì '
            '$1 < 3$ nên $1 : 3 = 0$ (viết $0$); hạ $8$ được $18 : 3 = 6 \\Rightarrow 618 : 3 = 206$.\n'
            '### 2. Thương có hai chữ số (chữ số hàng trăm bé hơn số chia)\n'
            '- Ví dụ: $236 : 4$. Lấy $23 : 4 = 5$ (dư $3$); hạ $6$ được $36 : 4 = 9 \\Rightarrow 236 : 4 = '
            '59$.',
  'formulas': [{'category': 'I. Quy tắc chia số có ba chữ số',
                'items': [{'name': 'Thứ tự chia',
                           'formula': 'Từ hàng cao nhất (trái sang phải): Chia $\\rightarrow$ Nhân '
                                      '$\\rightarrow$ Trừ $\\rightarrow$ Hạ'},
                          {'name': 'Lưu ý chữ số 0 ở thương',
                           'formula': 'Hạ xuống mà bé hơn số chia $\\rightarrow$ viết $0$ vào thương'}]}],
  'example': 'Đặt tính rồi tính: $848 : 4$, $425 : 5$ và $612 : 3$.',
  'example_answer': '- $848 : 4 = 212$.\n'
                    '- $425 : 5$: lấy $42 : 5 = 8$ (dư $2$), hạ $5$ được $25 : 5 = 5 \\rightarrow 85$.\n'
                    '- $612 : 3$: $6 : 3 = 2$, hạ $1$ ($1 : 3 = 0$), hạ $2$ được $12 : 3 = 4 \\rightarrow '
                    '204$.',
  'real_life': '- Chia đều $156\\text{ m}$ dây cáp thành $4$ đoạn bằng nhau; đóng gói $540$ quyển sách vào '
               '$6$ thùng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $848 : 4$ là:',
            'options': ['$202$', '$212$', '$221$', '$2\\,012$'],
            'answer': 1,
            'solution': 'Chia lần lượt: $8 : 4 = 2$, $4 : 4 = 1$, $8 : 4 = 2 \\rightarrow 212$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $156 : 4$ là:',
            'options': ['$38$', '$49$', '$39$', '$29$'],
            'answer': 2,
            'solution': 'Lấy $15 : 4 = 3$ (dư $3$), hạ $6$ được $36 : 4 = 9 \\rightarrow 39$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 37: Chia số có ba chữ số cho số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự chia**?',
            'options': ['Hạ xuống mà bé hơn số chia $\\rightarrow$ viết $0$ vào thương',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Từ hàng cao nhất (trái sang phải): Chia $\\rightarrow$ Nhân $\\rightarrow$ Trừ '
                        '$\\rightarrow$ Hạ'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 37: Chia số có ba chữ số cho số có một chữ '
                        'số, **Thứ tự chia** được xác định bởi: Từ hàng cao nhất (trái sang phải): Chia '
                        '$\\rightarrow$ Nhân $\\rightarrow$ Trừ $\\rightarrow$ Hạ.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 37: Chia số có ba chữ số cho số có một chữ số**, nội dung/biểu thức Hạ xuống '
                 'mà bé hơn số chia $\\rightarrow$ viết $0$ vào thương là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Lưu ý chữ số 0 ở thương', 'Thứ tự chia', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 37: Chia số có ba chữ số cho số có một chữ số, biểu thức/quy tắc Hạ xuống '
                        'mà bé hơn số chia $\\rightarrow$ viết $0$ vào thương chính là nội dung của **Lưu ý '
                        'chữ số 0 ở thương**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thương của phép chia $816 : 8$ là:',
            'options': ['$12$', '$102$', '$120$', '$100$'],
            'answer': 1,
            'solution': 'Ta có $8 : 8 = 1$; hạ $1$ bé hơn $8$ nên viết $0$ ở thương; hạ $6$ được $16 : 8 = 2 '
                        '\\rightarrow 102$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 37: Chia số có ba chữ số cho số có một chữ số** (Chủ đề 6: Phép nhân, phép '
                 'chia trong phạm vi 1 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đặt tính dọc và chia đúng số có ba chữ số cho số có một chữ số từ trái sang phải.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 37: Chia số có ba chữ số cho số có một chữ số: Đặt '
                        'tính dọc và chia đúng số có ba chữ số cho số có một chữ số từ trái sang phải.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $427 : 7$ có thương bằng $61$."',
            'answer': True,
            'solution': 'Ta có $42 : 7 = 6$ và $7 : 7 = 1$, thử lại $61 \\times 7 = 427$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 37: Chia số có ba chữ số cho số có một chữ số**, quy tắc **Thứ tự chia** được '
                 'xác định bởi Từ hàng cao nhất (trái sang phải): Chia $\\rightarrow$ Nhân $\\rightarrow$ '
                 'Trừ $\\rightarrow$ Hạ và áp dụng trực tiếp vào bài toán: “Đặt tính rồi tính: $848 : 4$, '
                 '$425 : 5$ và $612 : 3$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự chia** (Từ hàng cao nhất (trái sang phải): '
                        'Chia $\\rightarrow$ Nhân $\\rightarrow$ Trừ $\\rightarrow$ Hạ) là kiến thức cốt lõi '
                        'của Bài 37: Chia số có ba chữ số cho số có một chữ số. - $848 : 4 = 212$. - $425 : '
                        '5$: lấy $42 : 5 = 8$ (dư $2$), hạ $5$ được $25 : 5 = 5 \\rightarrow 85$. - $612 : '
                        '3$: $6 : 3 = 2$, hạ $1$ ($1 : 3 = 0$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 37: Chia số có ba chữ số cho số có một chữ số** để giải quyết '
                 'tình huống sau: Đặt tính rồi tính: $848 : 4$, $425 : 5$ và $612 : 3$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        '- $848 : 4 = 212$. - $425 : 5$: lấy $42 : 5 = 8$ (dư $2$), hạ $5$ được $25 : 5 = 5 '
                        '\\rightarrow 85$. - $612 : 3$: $6 : 3 = 2$, hạ $1$ ($1 : 3 = 0$), hạ $2$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 37: Chia số có ba chữ số cho số có một chữ số: - $848 : '
                        '4 = 212$.\n'
                        '- $425 : 5$: lấy $42 : 5 = 8$ (dư $2$), hạ $5$ được $25 : 5 = 5 \\rightarrow 85$.\n'
                        '- $612 : 3$: $6 : 3 = 2$, hạ $1$ ($1 : 3 = 0$), hạ $2$ được $12 : 3 = 4 '
                        '\\rightarrow 204$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một nhà máy xếp đều $360$ chiếc bánh trung thu vào $9$ thùng. Hỏi mỗi thùng có bao nhiêu '
                 'chiếc bánh?',
            'answer': ['40'],
            'unit': 'chiếc',
            'solution': 'Số bánh trong mỗi thùng là: $360 : 9 = 40\\text{ (chiếc)}$.\n'
                        'Đáp số: **$40\\text{ chiếc}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd06-nhan-chia-pham-vi-1000',
  'context_title': 'Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000',
  'context': 'SGK Toán 3 · Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000; biểu thức số.',
  'title': 'Bài 38: Biểu thức số. Tính giá trị của biểu thức số',
  'icon': '🔢',
  'description': 'Quy tắc thứ tự thực hiện các phép tính trong biểu thức số không có ngoặc và có dấu ngoặc.',
  'requirements': ['Nhận biết được biểu thức số và giá trị của biểu thức số.',
                   'Nắm vững và áp dụng đúng thứ tự thực hiện phép tính (trong ngoặc trước; nhân chia trước, '
                   'cộng trừ sau; cùng cấp từ trái sang phải).',
                   'Vận dụng biểu thức số để giải toán thực tế.'],
  'definition': '- **Biểu thức số** là các số được nối với nhau bởi các dấu phép tính ($+, -, \\times, :$).\n'
                '- **Thứ tự thực hiện phép tính**:\n'
                '  1. Nếu biểu thức **có dấu ngoặc** $()$: thực hiện các phép tính **trong ngoặc trước**.\n'
                '  2. Nếu biểu thức **chỉ có cộng, trừ** hoặc **chỉ có nhân, chia**: thực hiện **từ trái '
                'sang phải**.\n'
                '  3. Nếu biểu thức **có cả cộng, trừ, nhân, chia**: thực hiện **nhân, chia trước; cộng, trừ '
                'sau**.',
  'theory': '### 1. Biểu thức không có dấu ngoặc\n'
            '- Cùng mức độ ưu tiên (chỉ $+, -$ hoặc chỉ $\\times, :$): $48 : 4 \\times 2 = 12 \\times 2 = '
            '24$.\n'
            '- Khác mức độ ưu tiên: $60 + 20 \\times 3 = 60 + 60 = 120$ (thực hiện $20 \\times 3$ trước).\n'
            '### 2. Biểu thức có dấu ngoặc\n'
            '- Ví dụ: $(60 + 20) \\times 3 = 80 \\times 3 = 240$ (thực hiện trong ngoặc $60 + 20$ trước).',
  'formulas': [{'category': 'I. Quy tắc thứ tự thực hiện phép tính',
                'items': [{'name': 'Có ngoặc ()', 'formula': 'Tính trong ngoặc $()$ trước'},
                          {'name': 'Không ngoặc (khác cấp)',
                           'formula': 'Nhân $\\times$, chia $:$ trước $\\rightarrow$ Cộng $+$, trừ $-$ sau'},
                          {'name': 'Không ngoặc (cùng cấp)', 'formula': 'Tính lần lượt từ trái sang phải'}]}],
  'example': 'Tính giá trị của hai biểu thức: a) $120 - 40 : 5$; b) $(120 - 40) : 5$.',
  'example_answer': 'a) $120 - 40 : 5 = 120 - 8 = 112$ (chia trước, trừ sau).\n'
                    'b) $(120 - 40) : 5 = 80 : 5 = 16$ (trong ngoặc trước).',
  'real_life': '- Viết gộp phép tính khi đi mua hàng (ví dụ: tiền đưa trừ đi tích của đơn giá với số lượng).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong biểu thức $45 + 15 : 3$, ta thực hiện phép tính nào trước?',
            'options': ['Phép cộng', 'Tính tùy ý', 'Phép chia', 'Tính từ trái sang phải'],
            'answer': 2,
            'solution': 'Biểu thức không có ngoặc, có phép cộng và phép chia nên ta thực hiện **phép chia** '
                        'trước.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $50 + 10 \\times 4$ là:',
            'options': ['$240$', '$64$', '$200$', '$90$'],
            'answer': 3,
            'solution': 'Thực hiện nhân trước: $10 \\times 4 = 40$; sau đó $50 + 40 = 90$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 38: Biểu thức số. Tính giá trị của biểu thức số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Có ngoặc ()**?',
            'options': ['Tính trong ngoặc $()$ trước',
                        'Nhân $\\times$, chia $:$ trước $\\rightarrow$ Cộng $+$, trừ $-$ sau',
                        'Tính lần lượt từ trái sang phải',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 38: Biểu thức số. Tính giá trị của biểu thức '
                        'số, **Có ngoặc ()** được xác định bởi: Tính trong ngoặc $()$ trước.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 38: Biểu thức số. Tính giá trị của biểu thức số**, nội dung/biểu thức Nhân '
                 '$\\times$, chia $:$ trước $\\rightarrow$ Cộng $+$, trừ $-$ sau là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Có ngoặc ()', 'Không ngoặc (khác cấp)', 'Không ngoặc (cùng cấp)', 'Phân tích số'],
            'answer': 1,
            'solution': 'Trong Bài 38: Biểu thức số. Tính giá trị của biểu thức số, biểu thức/quy tắc Nhân '
                        '$\\times$, chia $:$ trước $\\rightarrow$ Cộng $+$, trừ $-$ sau chính là nội dung '
                        'của **Không ngoặc (khác cấp)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $100 - 4 \\times 9$ là:',
            'options': ['$864$', '$36$', '$64$', '$96$'],
            'answer': 2,
            'solution': 'Ta có $4 \\times 9 = 36$; sau đó $100 - 36 = 64$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 38: Biểu thức số. Tính giá trị của biểu thức số** (Chủ đề 6: Phép nhân, phép '
                 'chia trong phạm vi 1 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Nhận biết được biểu thức số và giá trị của biểu thức số.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 38: Biểu thức số. Tính giá trị của biểu thức số: Nhận '
                        'biết được biểu thức số và giá trị của biểu thức số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $(30 + 6) : 6$ bằng $31$."',
            'answer': False,
            'solution': 'Tính trong ngoặc trước: $(30 + 6) : 6 = 36 : 6 = 6$, không phải $31$ $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 38: Biểu thức số. Tính giá trị của biểu thức số**, quy tắc **Có ngoặc ()** '
                 'được xác định bởi Tính trong ngoặc $()$ trước và áp dụng trực tiếp vào bài toán: “Tính giá '
                 'trị của hai biểu thức: a) $120 - 40 : 5$; b) $(120 - 40) : 5$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Có ngoặc ()** (Tính trong ngoặc $()$ trước) là kiến '
                        'thức cốt lõi của Bài 38: Biểu thức số. Tính giá trị của biểu thức số. a) $120 - 40 '
                        ': 5 = 120 - 8 = 112$ (chia trước, trừ sau). b) $(120 - 40) : 5 = 80 : 5 = 16$ '
                        '(trong ngoặc trước).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 38: Biểu thức số. Tính giá trị của biểu thức số** để giải quyết '
                 'tình huống sau: Tính giá trị của hai biểu thức: a) $120 - 40 : 5$; b) $(120 - 40) : 5$. '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['a) $120 - 40 : 5 = 120 - 8 = 112$ (chia trước, trừ sau). b) $(120 - 40) : 5 = 80 : '
                        '5 = 16$ (trong ngoặc trước).',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 38: Biểu thức số. Tính giá trị của biểu thức số: a) $120 '
                        '- 40 : 5 = 120 - 8 = 112$ (chia trước, trừ sau).\n'
                        'b) $(120 - 40) : 5 = 80 : 5 = 16$ (trong ngoặc trước).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức: $72 : (3 \\times 3) + 12$.',
            'answer': ['20'],
            'unit': None,
            'solution': 'Tính trong ngoặc trước: $3 \\times 3 = 9$; chia tiếp: $72 : 9 = 8$; cộng cuối: $8 + '
                        '12 = 20$.\n'
                        'Đáp số: **$20$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd06-nhan-chia-pham-vi-1000',
  'context_title': 'Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000',
  'context': 'SGK Toán 3 · Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000; biểu thức số.',
  'title': 'Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập chung',
  'icon': '⚖️',
  'description': 'Quy tắc tìm xem số lớn gấp mấy lần số bé và phân biệt với tìm số lớn hơn số bé bao nhiêu '
                 'đơn vị.',
  'requirements': ['Biết cách tìm số lớn gấp mấy lần số bé bằng phép chia.',
                   'Phân biệt được câu hỏi "gấp mấy lần" (phép chia) và "nhiều hơn bao nhiêu" (phép trừ).',
                   'Giải được bài toán có hai bước tính liên quan đến so sánh số lớn gấp mấy lần số bé.'],
  'definition': '- Muốn biết **số lớn $A$ gấp mấy lần số bé $B$**, ta lấy **số lớn chia cho số bé** ($A : '
                'B$, cùng đơn vị đo).\n'
                '- Đơn vị của kết quả là **"lần"**.',
  'theory': '### 1. Quy tắc so sánh gấp mấy lần\n'
            '- Ví dụ: Đoạn thẳng $AB$ dài $18\\text{ cm}$, đoạn thẳng $CD$ dài $6\\text{ cm}$. Độ dài đoạn '
            '$AB$ gấp độ dài đoạn $CD$ số lần là: $18 : 6 = 3$ (lần).\n'
            '### 2. Phân biệt hai câu hỏi so sánh\n'
            '- Hỏi "Số lớn **hơn** số bé bao nhiêu đơn vị?" $\\rightarrow$ Dùng phép trừ: $\\text{Số lớn} - '
            '\\text{Số bé}$.\n'
            '- Hỏi "Số lớn **gấp mấy lần** số bé?" $\\rightarrow$ Dùng phép chia: $\\text{Số lớn} : '
            '\\text{Số bé}$.',
  'formulas': [{'category': 'I. So sánh hai số',
                'items': [{'name': 'Số lớn gấp mấy lần số bé',
                           'formula': '$\\text{Số lần} = \\text{Số lớn} : \\text{Số bé}$'},
                          {'name': 'Số lớn hơn số bé bao nhiêu',
                           'formula': '$\\text{Hiệu} = \\text{Số lớn} - \\text{Số bé}$'}]}],
  'example': 'Năm nay mẹ $35$ tuổi, con $7$ tuổi. Hỏi tuổi mẹ gấp mấy lần tuổi con?',
  'example_answer': 'Tuổi mẹ gấp tuổi con số lần là: $35 : 7 = 5\\text{ (lần)}$.\n'
                    'Đáp số: **$5\\text{ lần}$**.',
  'real_life': '- So sánh chiều cao của tòa nhà với chiều cao cái cây; so sánh giá tiền của chiếc cặp sách '
               'với hộp bút.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn biết số lớn gấp mấy lần số bé, ta lấy:',
            'options': ['Số lớn trừ đi số bé',
                        'Số lớn cộng với số bé',
                        'Số lớn nhân với số bé',
                        'Số lớn chia cho số bé'],
            'answer': 3,
            'solution': 'Theo quy tắc: lấy **số lớn chia cho số bé**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số $42$ gấp số $6$ bao nhiêu lần?',
            'options': ['$7$ lần', '$6$ lần', '$8$ lần', '$36$ lần'],
            'answer': 0,
            'solution': 'Ta có $42 : 6 = 7\\text{ (lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Số lớn gấp mấy lần số bé**?',
            'options': ['$\\text{Hiệu} = \\text{Số lớn} - \\text{Số bé}$',
                        '$\\text{Số lần} = \\text{Số lớn} : \\text{Số bé}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 39, 40: So sánh số lớn gấp mấy lần số bé và '
                        'luyện tập chung, **Số lớn gấp mấy lần số bé** được xác định bởi: $\\text{Số lần} = '
                        '\\text{Số lớn} : \\text{Số bé}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập chung**, nội dung/biểu '
                 'thức $\\text{Hiệu} = \\text{Số lớn} - \\text{Số bé}$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Số lớn gấp mấy lần số bé',
                        'Phân tích số',
                        'Số lớn hơn số bé bao nhiêu',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập chung, biểu '
                        'thức/quy tắc $\\text{Hiệu} = \\text{Số lớn} - \\text{Số bé}$ chính là nội dung của '
                        '**Số lớn hơn số bé bao nhiêu**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một sợi dây đỏ dài $2\\text{ dm}$, sợi dây xanh dài $5\\text{ cm}$. Sợi dây đỏ dài gấp mấy '
                 'lần sợi dây xanh?',
            'options': ['$15$ lần', '$2$ lần', '$10$ lần', '$4$ lần'],
            'answer': 3,
            'solution': 'Đổi $2\\text{ dm} = 20\\text{ cm}$. Sợi dây đỏ gấp sợi dây xanh: $20 : 5 = 4\\text{ '
                        '(lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập chung** (Chủ đề 6: '
                 'Phép nhân, phép chia trong phạm vi 1 000), khẳng định nào sau đây phản ánh **đúng** yêu '
                 'cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Biết cách tìm số lớn gấp mấy lần số bé bằng phép chia.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập '
                        'chung: Biết cách tìm số lớn gấp mấy lần số bé bằng phép chia.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Con lợn nặng $64\\text{ kg}$, con ngỗng nặng $8\\text{ kg}$ thì con lợn nặng '
                 'gấp $8$ lần con ngỗng."',
            'answer': True,
            'solution': 'Ta có $64 : 8 = 8\\text{ (lần)}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập chung**, quy tắc **Số '
                 'lớn gấp mấy lần số bé** được xác định bởi $\\text{Số lần} = \\text{Số lớn} : \\text{Số '
                 'bé}$ và áp dụng trực tiếp vào bài toán: “Năm nay mẹ $35$ tuổi, con $7$ tuổi. Hỏi tuổi mẹ '
                 'gấp mấy lần tuổi con?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Số lớn gấp mấy lần số bé** ($\\text{Số lần} = '
                        '\\text{Số lớn} : \\text{Số bé}$) là kiến thức cốt lõi của Bài 39, 40: So sánh số '
                        'lớn gấp mấy lần số bé và luyện tập chung. Tuổi mẹ gấp tuổi con số lần là: $35 : 7 = '
                        '5\\text{ (lần)}$. Đáp số: **$5\\text{ lần}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập chung** để '
                 'giải quyết tình huống sau: Năm nay mẹ $35$ tuổi, con $7$ tuổi. Hỏi tuổi mẹ gấp mấy lần '
                 'tuổi con? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Tuổi mẹ gấp tuổi con số lần là: $35 : 7 = 5\\text{ (lần)}$. Đáp số: **$5\\text{ '
                        'lần}$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 39, 40: So sánh số lớn gấp mấy lần số bé và luyện tập '
                        'chung: Tuổi mẹ gấp tuổi con số lần là: $35 : 7 = 5\\text{ (lần)}$.\n'
                        'Đáp số: **$5\\text{ lần}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong vườn có $8$ cây cam và $48$ cây chanh. Hỏi số cây chanh gấp mấy lần số cây cam?',
            'answer': ['6'],
            'unit': 'lần',
            'solution': 'Số cây chanh gấp số cây cam số lần là: $48 : 8 = 6\\text{ (lần)}$.\n'
                        'Đáp số: **$6\\text{ lần}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 3 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000',
  'icon': '📝',
  'description': 'Hệ thống hóa kỹ năng nhân, chia số có hai, ba chữ số với số có một chữ số và giải toán.',
  'requirements': ['Thực hiện thành thạo phép nhân, phép chia trong phạm vi $100$ và $1\\,000$.',
                   'Tìm được thành phần chưa biết trong phép nhân, phép chia.',
                   'Giải được bài toán có đến hai bước tính liên quan đến gấp, giảm một số lần.'],
  'definition': '- **Nhân viết**: tính từ hàng đơn vị sang hàng trăm.\n'
                '- **Chia viết**: chia từ hàng cao nhất xuống hàng đơn vị; số dư luôn bé hơn số chia ($r < '
                'b$).',
  'theory': '### 1. Ôn tập tính nhẩm và đặt tính rồi tính\n'
            '- Nhẩm số tròn chục, tròn trăm: $40 \\times 2 = 80$, $600 : 3 = 200$.\n'
            '- Đặt tính: chú ý các lượt nhân có nhớ và các lượt chia có chữ số $0$ ở thương (như $824 : 4 = '
            '206$).\n'
            '### 2. Ôn tập giải toán hai bước tính\n'
            '- Kết hợp các dạng: gấp một số lên $n$ lần, giảm một số đi $n$ lần, tìm một phần mấy của một '
            'số.',
  'formulas': [{'category': 'I. Quan hệ phép tính',
                'items': [{'name': 'Chia có dư',
                           'formula': '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + '
                                      '\\text{Số dư}$ ($0 < r < b$)'},
                          {'name': 'Tìm thành phần',
                           'formula': '$\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$ · $\\text{SBC} '
                                      '= \\text{Thương} \\times \\text{SC}$'}]}],
  'example': 'Một trang trại có $135$ con gà, số vịt bằng số gà giảm đi $3$ lần. Hỏi trang trại có tất cả '
             'bao nhiêu con gà và vịt?',
  'example_answer': 'Số con vịt là: $135 : 3 = 45\\text{ (con)}$.\n'
                    'Tổng số gà và vịt là: $135 + 45 = 180\\text{ (con)}$.\n'
                    'Đáp số: **$180\\text{ con}$**.',
  'real_life': '- Tổng kết số sách quyên góp của các lớp trong học kì $1$; chia quà học tập cuối học kì.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $7 \\times 6$ là:',
            'options': ['$42$', '$48$', '$36$', '$13$'],
            'answer': 0,
            'solution': 'Theo bảng nhân $7$: $7 \\times 6 = 42$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm số bị chia biết thương là $15$ và số chia là $6$:',
            'options': ['$21$', '$90$', '$9$', '$80$'],
            'answer': 1,
            'solution': 'Số bị chia $= 15 \\times 6 = 90$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 '
                 '000**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Chia có dư**?',
            'options': ['$\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$ · $\\text{SBC} = '
                        '\\text{Thương} \\times \\text{SC}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$ ($0 < '
                        'r < b$)',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 41: Ôn tập phép nhân, phép chia trong phạm vi '
                        '100, 1 000, **Chia có dư** được xác định bởi: $\\text{Số bị chia} = \\text{Thương} '
                        '\\times \\text{Số chia} + \\text{Số dư}$ ($0 < r < b$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000**, nội dung/biểu thức '
                 '$\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$ · $\\text{SBC} = \\text{Thương} '
                 '\\times \\text{SC}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Chia có dư', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Tìm thành phần'],
            'answer': 3,
            'solution': 'Trong Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000, biểu thức/quy '
                        'tắc $\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$ · $\\text{SBC} = '
                        '\\text{Thương} \\times \\text{SC}$ chính là nội dung của **Tìm thành phần**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phép chia $518 : 5$ có kết quả là:',
            'options': ['$103$ (dư $3$)', '$13$ (dư $3$)', '$103$ (dư $0$)', '$130$ (dư $3$)'],
            'answer': 0,
            'solution': 'Ta có $5 : 5 = 1$; hạ $1$ ($1 : 5 = 0$); hạ $8$ được $18 : 5 = 3$ dư $3 '
                        '\\rightarrow 103\\text{ (dư } 3\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000** (Chủ đề 7: Ôn tập '
                 'học kì 1), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Thực hiện thành thạo phép nhân, phép chia trong phạm vi $100$ và $1\\,000$.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 '
                        '000: Thực hiện thành thạo phép nhân, phép chia trong phạm vi $100$ và $1\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giảm $56$ đi $8$ lần thì được $48$."',
            'answer': False,
            'solution': 'Giảm $56$ đi $8$ lần là $56 : 8 = 7$ (còn $48$ là $56 - 8$) $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000**, quy tắc **Chia có '
                 'dư** được xác định bởi $\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + '
                 '\\text{Số dư}$ ($0 < r < b$) và áp dụng trực tiếp vào bài toán: “Một trang trại có $135$ '
                 'con gà, số vịt bằng số gà giảm đi $3$ lần. Hỏi trang trại có tất cả bao nhiêu con gà và '
                 'vịt?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Chia có dư** ($\\text{Số bị chia} = \\text{Thương} '
                        '\\times \\text{Số chia} + \\text{Số dư}$ ($0 < r < b$)) là kiến thức cốt lõi của '
                        'Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000. Số con vịt là: $135 : '
                        '3 = 45\\text{ (con)}$. Tổng số gà và vịt là: $135 + 45 = 180\\text{ (con)}$. Đáp '
                        'số: **$180\\text{ con}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000** để '
                 'giải quyết tình huống sau: Một trang trại có $135$ con gà, số vịt bằng số gà giảm đi $3$ '
                 'lần. Hỏi trang trại có tất cả bao nhiêu con gà và vịt? Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Số con vịt là: $135 : 3 = 45\\text{ (con)}$. Tổng số gà và vịt là: $135 + 45 = '
                        '180\\text{ (con)}$. Đáp số: **$180\\text{ con}$**.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 '
                        '000: Số con vịt là: $135 : 3 = 45\\text{ (con)}$.\n'
                        'Tổng số gà và vịt là: $135 + 45 = 180\\text{ (con)}$.\n'
                        'Đáp số: **$180\\text{ con}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi thùng có $115$ gói bánh. Hỏi $6$ thùng như thế có tất cả bao nhiêu gói bánh?',
            'answer': ['690'],
            'unit': 'gói',
            'solution': 'Tổng số gói bánh là: $115 \\times 6 = 690\\text{ (gói)}$.\n'
                        'Đáp số: **$690\\text{ gói}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 3 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 42: Ôn tập biểu thức số',
  'icon': '🧮',
  'description': 'Củng cố cách tính giá trị biểu thức số và lập biểu thức giải bài toán thực tế.',
  'requirements': ['Tính đúng giá trị biểu thức số có đến hai dấu phép tính (có hoặc không có dấu ngoặc).',
                   'So sánh được giá trị của hai biểu thức số.',
                   'Lập và tính được biểu thức số cho bài toán thực tiễn.'],
  'definition': '- Thứ tự thực hiện phép tính trong biểu thức: **Trong ngoặc $()$ trước $\\rightarrow$ Nhân '
                '$\\times$, chia $:$ $\\rightarrow$ Cộng $+$, trừ $-$**.\n'
                '- Nếu chỉ có cộng, trừ hoặc chỉ có nhân, chia thì tính từ **trái sang phải**.',
  'theory': '### 1. So sánh hai biểu thức khi có dấu ngoặc và không có dấu ngoặc\n'
            '- Ví dụ: $7 \\times 8 - 2 = 56 - 2 = 54$, trong khi $7 \\times (8 - 2) = 7 \\times 6 = 42$.\n'
            '- Dấu ngoặc làm thay đổi thứ tự thực hiện phép tính nên làm thay đổi giá trị của biểu thức.\n'
            '### 2. Vận dụng vào giải toán\n'
            '- Có thể gộp hai bước tính thành một biểu thức số duy nhất để tính kết quả.',
  'formulas': [{'category': 'I. Thứ tự ưu tiên',
                'items': [{'name': 'Quy tắc 3 bước',
                           'formula': '$() \\rightarrow \\times, : \\rightarrow +, -$'},
                          {'name': 'Cùng cấp', 'formula': 'Trái $\\rightarrow$ Phải'}]}],
  'example': 'Tính giá trị của biểu thức: a) $240 - 35 \\times 4$; b) $(136 + 64) : 5$.',
  'example_answer': 'a) $240 - 35 \\times 4 = 240 - 140 = 100$.\nb) $(136 + 64) : 5 = 200 : 5 = 40$.',
  'real_life': '- Tính tổng số tiền khi mua nhiều loại đồ dùng học tập cùng lúc.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $7 \\times 8 - 26$ là:',
            'options': ['$42$', '$30$', '$82$', '$20$'],
            'answer': 1,
            'solution': 'Nhân trước: $7 \\times 8 = 56$; trừ sau: $56 - 26 = 30$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $7 \\times (8 - 2)$ là:',
            'options': ['$54$', '$13$', '$42$', '$58$'],
            'answer': 2,
            'solution': 'Tính trong ngoặc trước: $8 - 2 = 6$; nhân sau: $7 \\times 6 = 42$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 42: Ôn tập biểu thức số**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Quy tắc 3 bước**?',
            'options': ['Trái $\\rightarrow$ Phải',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 42: Ôn tập biểu thức số, **Quy tắc 3 bước** '
                        'được xác định bởi: $() \\rightarrow \\times, : \\rightarrow +, -$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 42: Ôn tập biểu thức số**, nội dung/biểu thức Trái $\\rightarrow$ Phải là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cùng cấp', 'Quy tắc 3 bước', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 42: Ôn tập biểu thức số, biểu thức/quy tắc Trái $\\rightarrow$ Phải chính '
                        'là nội dung của **Cùng cấp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $90 : 3 \\times 2$ là:',
            'options': ['$15$', '$60$', '$45$', '$32$'],
            'answer': 1,
            'solution': 'Chỉ có phép chia và nhân nên tính từ trái sang phải: $90 : 3 = 30$; $30 \\times 2 = '
                        '60$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 42: Ôn tập biểu thức số** (Chủ đề 7: Ôn tập học kì 1), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Tính đúng giá trị biểu thức số có đến hai dấu phép tính (có hoặc không có dấu '
                        'ngoặc).',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 42: Ôn tập biểu thức số: Tính đúng giá trị biểu thức '
                        'số có đến hai dấu phép tính (có hoặc không có dấu ngoặc).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hai biểu thức $100 - (40 + 20)$ và $100 - 40 - 20$ có cùng giá trị bằng $40$."',
            'answer': True,
            'solution': 'Cả hai biểu thức đều có giá trị bằng $40$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 42: Ôn tập biểu thức số**, quy tắc **Quy tắc 3 bước** được xác định bởi $() '
                 '\\rightarrow \\times, : \\rightarrow +, -$ và áp dụng trực tiếp vào bài toán: “Tính giá '
                 'trị của biểu thức: a) $240 - 35 \\times 4$; b) $(136 + 64) : 5$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy tắc 3 bước** ($() \\rightarrow \\times, : '
                        '\\rightarrow +, -$) là kiến thức cốt lõi của Bài 42: Ôn tập biểu thức số. a) $240 - '
                        '35 \\times 4 = 240 - 140 = 100$. b) $(136 + 64) : 5 = 200 : 5 = 40$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 42: Ôn tập biểu thức số** để giải quyết tình huống sau: Tính giá '
                 'trị của biểu thức: a) $240 - 35 \\times 4$; b) $(136 + 64) : 5$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'a) $240 - 35 \\times 4 = 240 - 140 = 100$. b) $(136 + 64) : 5 = 200 : 5 = 40$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 42: Ôn tập biểu thức số: a) $240 - 35 \\times 4 = 240 - '
                        '140 = 100$.\n'
                        'b) $(136 + 64) : 5 = 200 : 5 = 40$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi xe tải nhỏ chở $9$ bao xi măng. Có $5$ xe như vậy chở xi măng đến công trường, sau đó '
                 'người ta chở thêm $18$ bao nữa. Hỏi đã chở được tất cả bao nhiêu bao xi măng?',
            'answer': ['63'],
            'unit': 'bao',
            'solution': 'Ta có biểu thức: $9 \\times 5 + 18 = 45 + 18 = 63\\text{ (bao)}$.\n'
                        'Đáp số: **$63\\text{ bao}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 3 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung',
  'icon': '📐',
  'description': 'Hệ thống hóa kiến thức về trung điểm, hình tròn, góc vuông, hình phẳng, hình khối và các '
                 'đơn vị mm, g, ml, độ C.',
  'requirements': ['Xác định đúng trung điểm, tâm, bán kính, đường kính, góc vuông, hình chữ nhật, hình '
                   'vuông, khối lập phương, khối hộp chữ nhật.',
                   'Chuyển đổi và tính toán thành thạo với các đơn vị $\\text{mm}, \\text{g}, \\text{ml}, '
                   '^\\circ\\text{C}$.',
                   'Giải được bài toán tổng hợp cuối học kì 1.'],
  'definition': '- **Hình học**: Trung điểm $M$ chia đôi đoạn thẳng ($MA = MB$); đường kính gấp đôi bán kính '
                '($d = 2 \\times r$); khối lập phương và khối hộp chữ nhật có $8$ đỉnh, $12$ cạnh, $6$ mặt.\n'
                '- **Đo lường**: $1\\text{ cm} = 10\\text{ mm}$; $1\\text{ m} = 1\\,000\\text{ mm}$; '
                '$1\\text{ kg} = 1\\,000\\text{ g}$; $1\\text{ l} = 1\\,000\\text{ ml}$.',
  'theory': '### 1. Tóm tắt hình học học kì 1\n'
            '- Hình chữ nhật có $4$ góc vuông, hai cạnh dài bằng nhau, hai cạnh ngắn bằng nhau.\n'
            '- Hình vuông có $4$ góc vuông và $4$ cạnh bằng nhau.\n'
            '### 2. Tóm tắt đo lường học kì 1\n'
            '- Đổi về cùng đơn vị đo trước khi thực hiện các phép cộng, trừ hoặc so sánh.',
  'formulas': [{'category': 'I. Hình học',
                'items': [{'name': 'Trung điểm & Hình tròn',
                           'formula': '$MA = MB = AB : 2$ · $d = 2 \\times r$'}]},
               {'category': 'II. Đo lường',
                'items': [{'name': 'Quy đổi chuẩn',
                           'formula': '$1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ kg} = 1\\,000\\text{ g}$ · '
                                      '$1\\text{ l} = 1\\,000\\text{ ml}$'}]}],
  'example': 'Hình tròn tâm $O$ có đường kính $16\\text{ cm}$. Tính bán kính của hình tròn đó theo đơn vị '
             'mi-li-mét.',
  'example_answer': 'Bán kính của hình tròn là: $16 : 2 = 8\\text{ (cm)}$.\n'
                    'Đổi sang mi-li-mét: $8\\text{ cm} = 80\\text{ mm}$.',
  'real_life': '- Đo đạc kích thước đồ vật và tính toán khối lượng nguyên liệu làm bánh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tròn có đường kính $12\\text{ cm}$ thì bán kính là:',
            'options': ['$24\\text{ cm}$', '$12\\text{ cm}$', '$6\\text{ cm}$', '$3\\text{ cm}$'],
            'answer': 2,
            'solution': 'Bán kính bằng đường kính chia $2$: $12 : 2 = 6\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $3\\text{ kg} = \\dots\\text{ g}$?',
            'options': ['$30$', '$300$', '$3$', '$3\\,000$'],
            'answer': 3,
            'solution': 'Vì $1\\text{ kg} = 1\\,000\\text{ g}$ nên $3\\text{ kg} = 3\\,000\\text{ g}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Trung điểm & Hình tròn**?',
            'options': ['$MA = MB = AB : 2$ · $d = 2 \\times r$',
                        '$1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\text{ l} '
                        '= 1\\,000\\text{ ml}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 43, 44: Ôn tập hình học, đo lường và ôn tập '
                        'chung, **Trung điểm & Hình tròn** được xác định bởi: $MA = MB = AB : 2$ · $d = 2 '
                        '\\times r$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung**, nội dung/biểu thức '
                 '$1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\text{ l} = '
                 '1\\,000\\text{ ml}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Trung điểm & Hình tròn',
                        'Quy đổi chuẩn',
                        'Phân tích số',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung, biểu thức/quy tắc '
                        '$1\\text{ cm} = 10\\text{ mm}$ · $1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\text{ l} '
                        '= 1\\,000\\text{ ml}$ chính là nội dung của **Quy đổi chuẩn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một chai dầu ăn chứa $1\\text{ l}$, mẹ đã dùng hết $350\\text{ ml}$. Lượng dầu ăn còn lại '
                 'trong chai là:',
            'options': ['$750\\text{ ml}$', '$65\\text{ ml}$', '$650\\text{ ml}$', '$550\\text{ ml}$'],
            'answer': 2,
            'solution': 'Đổi $1\\text{ l} = 1\\,000\\text{ ml}$. Còn lại: $1\\,000 - 350 = 650\\text{ '
                        '(ml)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung** (Chủ đề 7: Ôn tập học kì '
                 '1), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Xác định đúng trung điểm, tâm, bán kính, đường kính, góc vuông, hình chữ nhật, hình '
                        'vuông, khối lập phương, khối hộp chữ nhật.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung: Xác '
                        'định đúng trung điểm, tâm, bán kính, đường kính, góc vuông, hình chữ nhật, hình '
                        'vuông, khối lập phương, khối hộp chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khối hộp chữ nhật có $8$ đỉnh, $12$ cạnh và $6$ mặt."',
            'answer': True,
            'solution': 'Đúng theo đặc điểm của khối hộp chữ nhật $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung**, quy tắc **Trung điểm & '
                 'Hình tròn** được xác định bởi $MA = MB = AB : 2$ · $d = 2 \\times r$ và áp dụng trực tiếp '
                 'vào bài toán: “Hình tròn tâm $O$ có đường kính $16\\text{ cm}$. Tính bán kính của hình '
                 'tròn đó theo đơn vị mi-li-mét.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Trung điểm & Hình tròn** ($MA = MB = AB : 2$ · $d = '
                        '2 \\times r$) là kiến thức cốt lõi của Bài 43, 44: Ôn tập hình học, đo lường và ôn '
                        'tập chung. Bán kính của hình tròn là: $16 : 2 = 8\\text{ (cm)}$. Đổi sang '
                        'mi-li-mét: $8\\text{ cm} = 80\\text{ mm}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung** để giải quyết '
                 'tình huống sau: Hình tròn tâm $O$ có đường kính $16\\text{ cm}$. Tính bán kính của hình '
                 'tròn đó theo đơn vị mi-li-mét. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Bán kính của hình tròn là: $16 : 2 = 8\\text{ (cm)}$. Đổi sang mi-li-mét: $8\\text{ '
                        'cm} = 80\\text{ mm}$.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 43, 44: Ôn tập hình học, đo lường và ôn tập chung: Bán '
                        'kính của hình tròn là: $16 : 2 = 8\\text{ (cm)}$.\n'
                        'Đổi sang mi-li-mét: $8\\text{ cm} = 80\\text{ mm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Con kiến bò từ $A$ đến trung điểm $M$ của đoạn thẳng $AB$ hết $45\\text{ mm}$. Hỏi cả đoạn '
                 'thẳng $AB$ dài bao nhiêu xăng-ti-mét?',
            'answer': ['9'],
            'unit': 'cm',
            'solution': 'Đoạn thẳng $AB$ dài: $45 \\times 2 = 90\\text{ (mm)} = 9\\text{ (cm)}$.\n'
                        'Đáp số: **$9\\text{ cm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd08-cac-so-den-10000',
  'context_title': 'Chủ đề 8: Các số đến 10 000',
  'context': 'SGK Toán 3 · Chủ đề 8: Các số đến 10 000; chữ số La Mã; làm tròn số.',
  'title': 'Bài 45: Các số có bốn chữ số. Số 10 000',
  'icon': '🔢',
  'description': 'Đọc, viết, xác định hàng và phân tích cấu tạo thập phân của các số có bốn chữ số và số 10 '
                 '000.',
  'requirements': ['Đọc, viết được các số có bốn chữ số và số $10\\,000$.',
                   'Nêu được giá trị theo vị trí của từng chữ số (hàng nghìn, hàng trăm, hàng chục, hàng đơn '
                   'vị).',
                   'Viết được số có bốn chữ số thành tổng các nghìn, trăm, chục, đơn vị.'],
  'definition': '- **Số có bốn chữ số** gồm bốn hàng: hàng nghìn, hàng trăm, hàng chục, hàng đơn vị: '
                '$\\overline{abcd} = a\\,000 + b00 + c0 + d$.\n'
                '- Mười nghìn viết là **$10\\,000$** ($10$ nghìn $= 10\\,000$). Số liền trước của $10\\,000$ '
                'là $9\\,999$.',
  'theory': '### 1. Cách đọc và viết số có bốn chữ số\n'
            '- Đọc từ trái sang phải: nghìn $\\rightarrow$ trăm $\\rightarrow$ chục $\\rightarrow$ đơn vị.\n'
            '- Ví dụ: $4\\,058$ đọc là "bốn nghìn không trăm năm mươi tám"; $5\\,007$ đọc là "năm nghìn '
            'không trăm linh bảy".\n'
            '### 2. Cấu tạo thập phân của số\n'
            '- Ví dụ: $3\\,725 = 3\\,000 + 700 + 20 + 5$.',
  'formulas': [{'category': 'I. Cấu tạo số có bốn chữ số',
                'items': [{'name': 'Khai triển tổng',
                           'formula': '$\\overline{abcd} = a \\times 1\\,000 + b \\times 100 + c \\times 10 '
                                      '+ d$'},
                          {'name': 'Số mười nghìn',
                           'formula': '$10 \\text{ nghìn} = 10\\,000$ · $9\\,999 + 1 = 10\\,000$'}]}],
  'example': 'Viết số gồm $6$ nghìn, $2$ trăm, $0$ chục, $4$ đơn vị và viết số đó thành tổng.',
  'example_answer': 'Số đó viết là **$6\\,204$**.\nViết thành tổng: $6\\,204 = 6\\,000 + 200 + 4$.',
  'real_life': '- Đọc năm lịch sử (năm $2026$), số tiền gửi tiết kiệm hoặc số khán giả trong nhà thi đấu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số "năm nghìn không trăm linh bảy" được viết là:',
            'options': ['$5\\,070$', '$507$', '$50\\,007$', '$5\\,007$'],
            'answer': 3,
            'solution': 'Gồm $5$ nghìn, $0$ trăm, $0$ chục, $7$ đơn vị $\\rightarrow 5\\,007$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số liền sau của số $9\\,999$ là:',
            'options': ['$10\\,000$', '$9\\,998$', '$1\\,000$', '$99\\,990$'],
            'answer': 0,
            'solution': 'Ta có $9\\,999 + 1 = 10\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 45: Các số có bốn chữ số. Số 10 000**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Khai triển tổng**?',
            'options': ['$10 \\text{ nghìn} = 10\\,000$ · $9\\,999 + 1 = 10\\,000$',
                        '$\\overline{abcd} = a \\times 1\\,000 + b \\times 100 + c \\times 10 + d$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 45: Các số có bốn chữ số. Số 10 000, **Khai '
                        'triển tổng** được xác định bởi: $\\overline{abcd} = a \\times 1\\,000 + b \\times '
                        '100 + c \\times 10 + d$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 45: Các số có bốn chữ số. Số 10 000**, nội dung/biểu thức $10 \\text{ nghìn} = '
                 '10\\,000$ · $9\\,999 + 1 = 10\\,000$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khai triển tổng', 'Phân tích số', 'Số mười nghìn', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 45: Các số có bốn chữ số. Số 10 000, biểu thức/quy tắc $10 \\text{ nghìn} '
                        '= 10\\,000$ · $9\\,999 + 1 = 10\\,000$ chính là nội dung của **Số mười nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số $3\\,082$ gồm:',
            'options': ['$3$ nghìn, $8$ trăm, $2$ đơn vị',
                        '$30$ trăm, $82$ nghìn',
                        '$3$ trăm, $8$ chục, $2$ đơn vị',
                        '$3$ nghìn, $8$ chục, $2$ đơn vị'],
            'answer': 3,
            'solution': 'Ta có $3\\,082 = 3\\,000 + 80 + 2$ nên gồm **$3$ nghìn, $8$ chục, $2$ đơn vị**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 45: Các số có bốn chữ số. Số 10 000** (Chủ đề 8: Các số đến 10 000), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết được các số có bốn chữ số và số $10\\,000$.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 45: Các số có bốn chữ số. Số 10 000: Đọc, viết được '
                        'các số có bốn chữ số và số $10\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong số $7\\,492$, chữ số $4$ có giá trị là $400$."',
            'answer': True,
            'solution': 'Chữ số $4$ đứng ở hàng trăm nên có giá trị là $400$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 45: Các số có bốn chữ số. Số 10 000**, quy tắc **Khai triển tổng** được xác '
                 'định bởi $\\overline{abcd} = a \\times 1\\,000 + b \\times 100 + c \\times 10 + d$ và áp '
                 'dụng trực tiếp vào bài toán: “Viết số gồm $6$ nghìn, $2$ trăm, $0$ chục, $4$ đơn vị và '
                 'viết số đó thành tổng.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khai triển tổng** ($\\overline{abcd} = a \\times '
                        '1\\,000 + b \\times 100 + c \\times 10 + d$) là kiến thức cốt lõi của Bài 45: Các '
                        'số có bốn chữ số. Số 10 000. Số đó viết là **$6\\,204$**. Viết thành tổng: $6\\,204 '
                        '= 6\\,000 + 200 + 4$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 45: Các số có bốn chữ số. Số 10 000** để giải quyết tình huống '
                 'sau: Viết số gồm $6$ nghìn, $2$ trăm, $0$ chục, $4$ đơn vị và viết số đó thành tổng. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Số đó viết là **$6\\,204$**. Viết thành tổng: $6\\,204 = 6\\,000 + 200 + 4$.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 45: Các số có bốn chữ số. Số 10 000: Số đó viết là '
                        '**$6\\,204$**.\n'
                        'Viết thành tổng: $6\\,204 = 6\\,000 + 200 + 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tự nhiên lớn nhất có bốn chữ số mà tổng các chữ số của nó bằng $4$.',
            'answer': ['4000'],
            'unit': None,
            'solution': 'Để số lớn nhất, chữ số hàng nghìn phải lớn nhất có thể là $4$, các hàng còn lại là '
                        '$0$. Ta được số **$4\\,000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd08-cac-so-den-10000',
  'context_title': 'Chủ đề 8: Các số đến 10 000',
  'context': 'SGK Toán 3 · Chủ đề 8: Các số đến 10 000; chữ số La Mã; làm tròn số.',
  'title': 'Bài 46: So sánh các số trong phạm vi 10 000',
  'icon': '⚖️',
  'description': 'Quy tắc so sánh hai số trong phạm vi 10 000 và sắp xếp nhóm các số theo thứ tự.',
  'requirements': ['So sánh được hai số bất kỳ trong phạm vi $10\\,000$.',
                   'Tìm được số lớn nhất, số bé nhất trong một nhóm không quá $4$ số.',
                   'Sắp xếp được các số theo thứ tự từ bé đến lớn hoặc từ lớn đến bé.'],
  'definition': '- Trong hai số, số nào có **nhiều chữ số hơn** thì lớn hơn (ví dụ $10\\,000 > 9\\,999 > '
                '985$).\n'
                '- Nếu hai số có **cùng số chữ số**, ta so sánh từng cặp chữ số ở cùng một hàng kể từ **trái '
                'sang phải** (nghìn $\\rightarrow$ trăm $\\rightarrow$ chục $\\rightarrow$ đơn vị).',
  'theory': '### 1. So sánh hai số có bốn chữ số\n'
            '- So sánh hàng nghìn trước: $6\\,012 > 5\\,891$ vì $6 > 5$.\n'
            '- Nếu cùng hàng nghìn thì so sánh hàng trăm: $4\\,320 > 4\\,230$ vì $3 > 2$.\n'
            '- Nếu cùng hàng nghìn, hàng trăm thì so sánh hàng chục rồi đến hàng đơn vị: $4\\,320 > 4\\,302$ '
            'vì $2 > 0$.',
  'formulas': [{'category': 'I. Quy tắc so sánh',
                'items': [{'name': 'Khác số chữ số', 'formula': 'Nhiều chữ số hơn $\\rightarrow$ Lớn hơn'},
                          {'name': 'Cùng bốn chữ số',
                           'formula': 'So sánh: Hàng nghìn $\\rightarrow$ Hàng trăm $\\rightarrow$ Hàng chục '
                                      '$\\rightarrow$ Hàng đơn vị'}]}],
  'example': 'Sắp xếp các số $4\\,320$; $4\\,302$; $4\\,230$; $4\\,203$ theo thứ tự từ lớn đến bé.',
  'example_answer': 'Cả bốn số đều có $4$ nghìn. Nhóm có $3$ trăm: $4\\,320 > 4\\,302$. Nhóm có $2$ trăm: '
                    '$4\\,230 > 4\\,203$.\n'
                    'Thứ tự từ lớn đến bé là: **$4\\,320$; $4\\,302$; $4\\,230$; $4\\,203$**.',
  'real_life': '- So sánh chiều cao các đỉnh núi ở Việt Nam (ví dụ đỉnh Fansipan cao $3\\,147\\text{ m}$); '
               'so sánh giá tiền các mặt hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $5\\,891 \\dots 6\\,012$ là:',
            'options': ['$<$', '$>$', '$=$', 'Không so sánh được'],
            'answer': 0,
            'solution': 'So sánh chữ số hàng nghìn: $5 < 6$ nên $5\\,891 < 6\\,012$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số $8\\,542$; $8\\,452$; $8\\,524$; $8\\,254$, số bé nhất là:',
            'options': ['$8\\,542$', '$8\\,254$', '$8\\,452$', '$8\\,524$'],
            'answer': 1,
            'solution': 'Cùng $8$ nghìn, so sánh hàng trăm: $2$ bé nhất nên **$8\\,254$** là số bé nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 46: So sánh các số trong phạm vi 10 000**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Khác số chữ số**?',
            'options': ['So sánh: Hàng nghìn $\\rightarrow$ Hàng trăm $\\rightarrow$ Hàng chục '
                        '$\\rightarrow$ Hàng đơn vị',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Nhiều chữ số hơn $\\rightarrow$ Lớn hơn',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 46: So sánh các số trong phạm vi 10 000, '
                        '**Khác số chữ số** được xác định bởi: Nhiều chữ số hơn $\\rightarrow$ Lớn hơn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 46: So sánh các số trong phạm vi 10 000**, nội dung/biểu thức So sánh: Hàng '
                 'nghìn $\\rightarrow$ Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khác số chữ số', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Cùng bốn chữ số'],
            'answer': 3,
            'solution': 'Trong Bài 46: So sánh các số trong phạm vi 10 000, biểu thức/quy tắc So sánh: Hàng '
                        'nghìn $\\rightarrow$ Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị '
                        'chính là nội dung của **Cùng bốn chữ số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Sắp xếp các số $4\\,320$; $4\\,302$; $4\\,230$; $4\\,203$ theo thứ tự từ lớn đến bé ta '
                 'được:',
            'options': ['$4\\,320; 4\\,302; 4\\,230; 4\\,203$',
                        '$4\\,203; 4\\,230; 4\\,302; 4\\,320$',
                        '$4\\,302; 4\\,320; 4\\,230; 4\\,203$',
                        '$4\\,320; 4\\,230; 4\\,302; 4\\,203$'],
            'answer': 0,
            'solution': 'Ta có $4\\,320 > 4\\,302 > 4\\,230 > 4\\,203$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 46: So sánh các số trong phạm vi 10 000** (Chủ đề 8: Các số đến 10 000), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'So sánh được hai số bất kỳ trong phạm vi $10\\,000$.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 46: So sánh các số trong phạm vi 10 000: So sánh được '
                        'hai số bất kỳ trong phạm vi $10\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$7\\,099 > 7\\,100$."',
            'answer': False,
            'solution': 'Cùng $7$ nghìn, chữ số hàng trăm $0 < 1$ nên $7\\,099 < 7\\,100$ $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 46: So sánh các số trong phạm vi 10 000**, quy tắc **Khác số chữ số** được xác '
                 'định bởi Nhiều chữ số hơn $\\rightarrow$ Lớn hơn và áp dụng trực tiếp vào bài toán: “Sắp '
                 'xếp các số $4\\,320$; $4\\,302$; $4\\,230$; $4\\,203$ theo thứ tự từ lớn đến bé.”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khác số chữ số** (Nhiều chữ số hơn $\\rightarrow$ '
                        'Lớn hơn) là kiến thức cốt lõi của Bài 46: So sánh các số trong phạm vi 10 000. Cả '
                        'bốn số đều có $4$ nghìn. Nhóm có $3$ trăm: $4\\,320 > 4\\,302$. Nhóm có $2$ trăm: '
                        '$4\\,230 > 4\\,203$. Thứ tự từ lớn đến bé là: **$4\\,320$; $4\\,302$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 46: So sánh các số trong phạm vi 10 000** để giải quyết tình '
                 'huống sau: Sắp xếp các số $4\\,320$; $4\\,302$; $4\\,230$; $4\\,203$ theo thứ tự từ lớn '
                 'đến bé. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Cả bốn số đều có $4$ nghìn. Nhóm có $3$ trăm: $4\\,320 > 4\\,302$. Nhóm có $2$ '
                        'trăm: $4\\,230 > 4\\,203$. Thứ tự từ lớn đến bé là: **$4\\,320$; $4\\,302$; '
                        '$4\\,230$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 46: So sánh các số trong phạm vi 10 000: Cả bốn số đều '
                        'có $4$ nghìn. Nhóm có $3$ trăm: $4\\,320 > 4\\,302$. Nhóm có $2$ trăm: $4\\,230 > '
                        '4\\,203$.\n'
                        'Thứ tự từ lớn đến bé là: **$4\\,320$; $4\\,302$; $4\\,230$; $4\\,203$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Chiều cao của ba ngọn núi lần lượt là: núi A cao $2\\,415\\text{ m}$, núi B cao '
                 '$2\\,451\\text{ m}$, núi C cao $2\\,154\\text{ m}$. Ngọn núi cao nhất có độ cao bao nhiêu '
                 'mét?',
            'answer': ['2451'],
            'unit': 'm',
            'solution': 'So sánh: $2\\,451 > 2\\,415 > 2\\,154$ nên ngọn núi cao nhất cao **$2\\,451\\text{ '
                        'm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd08-cac-so-den-10000',
  'context_title': 'Chủ đề 8: Các số đến 10 000',
  'context': 'SGK Toán 3 · Chủ đề 8: Các số đến 10 000; chữ số La Mã; làm tròn số.',
  'title': 'Bài 47: Làm quen với chữ số La Mã',
  'icon': '🏛️',
  'description': 'Nhận biết các chữ số La Mã I, V, X và đọc, viết các số La Mã từ I đến XX (1 đến 20).',
  'requirements': ['Nhận biết giá trị của ba ký hiệu chữ số La Mã cơ bản: $\\text{I} = 1$, $\\text{V} = 5$, '
                   '$\\text{X} = 10$.',
                   'Đọc và viết được các số bằng chữ số La Mã trong phạm vi $20$.',
                   'Đọc được giờ trên mặt đồng hồ dùng chữ số La Mã.'],
  'definition': '- Ba chữ số La Mã cơ bản: $\\text{I}$ có giá trị là $1$; $\\text{V}$ có giá trị là $5$; '
                '$\\text{X}$ có giá trị là $10$.\n'
                '- **Quy tắc ghép**:\n'
                '  - Viết $\\text{I}$ vào **bên trái** $\\text{V}$ hoặc $\\text{X}$ thì giá trị giảm đi $1$ '
                'đơn vị: $\\text{IV} = 4$, $\\text{IX} = 9$.\n'
                '  - Viết thêm vào **bên phải** thì cộng thêm giá trị (mỗi chữ số $\\text{I}, \\text{X}$ '
                'không viết liền nhau quá $3$ lần).',
  'theory': '### 1. Các số La Mã từ $1$ đến $10$\n'
            '- $\\text{I} = 1$, $\\text{II} = 2$, $\\text{III} = 3$, $\\text{IV} = 4$, $\\text{V} = 5$, '
            '$\\text{VI} = 6$, $\\text{VII} = 7$, $\\text{VIII} = 8$, $\\text{IX} = 9$, $\\text{X} = 10$.\n'
            '### 2. Các số La Mã từ $11$ đến $20$\n'
            '- Ghép $\\text{X}$ ($10$) ở bên trái với các số từ $\\text{I}$ đến $\\text{X}$ ở bên phải:\n'
            '- $\\text{XI} = 11$, $\\text{XII} = 12$, ..., $\\text{XIV} = 14$, $\\text{XV} = 15$, '
            '$\\text{XVI} = 16$, ..., $\\text{XIX} = 19$, $\\text{XX} = 20$.',
  'formulas': [{'category': 'I. Ký hiệu La Mã',
                'items': [{'name': 'Cơ bản',
                           'formula': '$\\text{I} = 1$ · $\\text{V} = 5$ · $\\text{X} = 10$'},
                          {'name': 'Cặp trừ cần nhớ',
                           'formula': '$\\text{IV} = 4$ · $\\text{IX} = 9$ · $\\text{XIV} = 14$ · '
                                      '$\\text{XIX} = 19$'}]}],
  'example': 'Đọc các số La Mã sau sang số tự nhiên: $\\text{V}, \\text{IX}, \\text{XIV}, \\text{XVII}, '
             '\\text{XIX}$.',
  'example_answer': 'Ta có: $\\text{IV} = 4$; $\\text{IX} = 9$; $\\text{XIV} = 14$; $\\text{XVII} = 17$; '
                    '$\\text{XIX} = 19$.',
  'real_life': '- Xem mặt đồng hồ cổ điển có chữ số La Mã; đánh số chương sách hoặc các thế kỉ lịch sử (thế '
               'kỉ $\\text{XX}$, $\\text{XXI}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Chữ số La Mã $\\text{X}$ có giá trị là:',
            'options': ['$5$', '$10$', '$1$', '$20$'],
            'answer': 1,
            'solution': 'Chữ số La Mã $\\text{X}$ có giá trị bằng **$10$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số La Mã $\\text{IX}$ biểu diễn số nào?',
            'options': ['$11$', '$4$', '$9$', '$6$'],
            'answer': 2,
            'solution': '$\\text{I}$ đứng trước $\\text{X}$ nên giá trị là $10 - 1 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 47: Làm quen với chữ số La Mã**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Cơ bản**?',
            'options': ['$\\text{IV} = 4$ · $\\text{IX} = 9$ · $\\text{XIV} = 14$ · $\\text{XIX} = 19$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$\\text{I} = 1$ · $\\text{V} = 5$ · $\\text{X} = 10$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 47: Làm quen với chữ số La Mã, **Cơ bản** '
                        'được xác định bởi: $\\text{I} = 1$ · $\\text{V} = 5$ · $\\text{X} = 10$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 47: Làm quen với chữ số La Mã**, nội dung/biểu thức $\\text{IV} = 4$ · '
                 '$\\text{IX} = 9$ · $\\text{XIV} = 14$ · $\\text{XIX} = 19$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Cặp trừ cần nhớ', 'Cơ bản', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 47: Làm quen với chữ số La Mã, biểu thức/quy tắc $\\text{IV} = 4$ · '
                        '$\\text{IX} = 9$ · $\\text{XIV} = 14$ · $\\text{XIX} = 19$ chính là nội dung của '
                        '**Cặp trừ cần nhớ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số $17$ được viết bằng chữ số La Mã là:',
            'options': ['$\\text{XIV}$', '$\\text{XVII}$', '$\\text{XIIV}$', '$\\text{VXII}$'],
            'answer': 1,
            'solution': 'Ta có $17 = 10 + 5 + 2$ nên viết là **$\\text{XVII}$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 47: Làm quen với chữ số La Mã** (Chủ đề 8: Các số đến 10 000), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Nhận biết giá trị của ba ký hiệu chữ số La Mã cơ bản: $\\text{I} = 1$, $\\text{V} = '
                        '5$, $\\text{X} = 10$.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 47: Làm quen với chữ số La Mã: Nhận biết giá trị của '
                        'ba ký hiệu chữ số La Mã cơ bản: $\\text{I} = 1$, $\\text{V} = 5$, $\\text{X} = '
                        '10$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số $14$ được viết bằng chữ số La Mã là $\\text{XIV}$."',
            'answer': True,
            'solution': 'Vì $\\text{X} = 10$ và $\\text{IV} = 4$ nên $\\text{XIV} = 14$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 47: Làm quen với chữ số La Mã**, quy tắc **Cơ bản** được xác định bởi '
                 '$\\text{I} = 1$ · $\\text{V} = 5$ · $\\text{X} = 10$ và áp dụng trực tiếp vào bài toán: '
                 '“Đọc các số La Mã sau sang số tự nhiên: $\\text{V}, \\text{IX}, \\text{XIV}, \\text{XVII}, '
                 '\\text{XIX}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cơ bản** ($\\text{I} = 1$ · $\\text{V} = 5$ · '
                        '$\\text{X} = 10$) là kiến thức cốt lõi của Bài 47: Làm quen với chữ số La Mã. Ta '
                        'có: $\\text{IV} = 4$; $\\text{IX} = 9$; $\\text{XIV} = 14$; $\\text{XVII} = 17$; '
                        '$\\text{XIX} = 19$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 47: Làm quen với chữ số La Mã** để giải quyết tình huống sau: Đọc '
                 'các số La Mã sau sang số tự nhiên: $\\text{V}, \\text{IX}, \\text{XIV}, \\text{XVII}, '
                 '\\text{XIX}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Ta có: $\\text{IV} = 4$; $\\text{IX} = 9$; $\\text{XIV} = 14$; $\\text{XVII} = 17$; '
                        '$\\text{XIX} = 19$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 47: Làm quen với chữ số La Mã: Ta có: $\\text{IV} = 4$; '
                        '$\\text{IX} = 9$; $\\text{XIV} = 14$; $\\text{XVII} = 17$; $\\text{XIX} = 19$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên mặt đồng hồ có ghi chữ số La Mã, kim giờ chỉ đúng vào số $\\text{VIII}$, kim phút chỉ '
                 'đúng vào số $\\text{XII}$. Hỏi lúc đó là mấy giờ?',
            'answer': ['8'],
            'unit': 'giờ',
            'solution': 'Số $\\text{VIII}$ là $8$ và số $\\text{XII}$ là $12$, vậy đồng hồ chỉ **$8$ giờ**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd08-cac-so-den-10000',
  'context_title': 'Chủ đề 8: Các số đến 10 000',
  'context': 'SGK Toán 3 · Chủ đề 8: Các số đến 10 000; chữ số La Mã; làm tròn số.',
  'title': 'Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung',
  'icon': '🔄',
  'description': 'Quy tắc làm tròn số đến hàng chục và làm tròn số đến hàng trăm trong phạm vi 10 000.',
  'requirements': ['Làm tròn được một số đến hàng chục dựa vào chữ số hàng đơn vị.',
                   'Làm tròn được một số đến hàng trăm dựa vào chữ số hàng chục.',
                   'Vận dụng làm tròn số để ước lượng kết quả trong thực tế.'],
  'definition': '- **Làm tròn đến hàng chục**: xét chữ số **hàng đơn vị**. Nếu chữ số hàng đơn vị là $1, 2, '
                '3, 4$ thì làm tròn xuống (giữ nguyên hàng chục, thay đơn vị bằng $0$); nếu là $5, 6, 7, 8, '
                '9$ thì làm tròn lên (tăng hàng chục thêm $1$, thay đơn vị bằng $0$).\n'
                '- **Làm tròn đến hàng trăm**: xét chữ số **hàng chục**. Nếu chữ số hàng chục bé hơn $5$ thì '
                'làm tròn xuống; nếu từ $5$ trở lên thì làm tròn lên.',
  'theory': '### 1. Làm tròn số đến hàng chục\n'
            '- Ví dụ: $1\\,234$ có chữ số hàng đơn vị là $4 < 5 \\rightarrow$ làm tròn xuống thành '
            '$1\\,230$.\n'
            '- Ví dụ: $1\\,347$ có chữ số hàng đơn vị là $7 \\ge 5 \\rightarrow$ làm tròn lên thành '
            '$1\\,350$.\n'
            '### 2. Làm tròn số đến hàng trăm\n'
            '- Ví dụ: $2\\,385$ có chữ số hàng chục là $8 \\ge 5 \\rightarrow$ làm tròn lên thành $2\\,400$.',
  'formulas': [{'category': 'I. Quy tắc làm tròn số',
                'items': [{'name': 'Làm tròn đến hàng chục',
                           'formula': 'Xét hàng đơn vị: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ '
                                      'lên'},
                          {'name': 'Làm tròn đến hàng trăm',
                           'formula': 'Xét hàng chục: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ '
                                      'lên'}]}],
  'example': 'Làm tròn số $4\\,762$ đến hàng chục và đến hàng trăm.',
  'example_answer': '- Làm tròn đến hàng chục: chữ số hàng đơn vị là $2 < 5$ nên được **$4\\,760$**.\n'
                    '- Làm tròn đến hàng trăm: chữ số hàng chục là $6 \\ge 5$ nên được **$4\\,800$**.',
  'real_life': '- Ước lượng nhanh số học sinh toàn trường hoặc số tiền cần mang theo khi đi mua sắm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $64$ đến hàng chục ta được:',
            'options': ['$70$', '$65$', '$60$', '$50$'],
            'answer': 2,
            'solution': 'Chữ số hàng đơn vị là $4 < 5$ nên làm tròn xuống được **$60$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $2\\,385$ đến hàng trăm ta được:',
            'options': ['$2\\,300$', '$2\\,390$', '$2\\,380$', '$2\\,400$'],
            'answer': 3,
            'solution': 'Chữ số hàng chục là $8 \\ge 5$ nên làm tròn lên được **$2\\,400$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện '
                 'tập chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Làm tròn đến hàng chục**?',
            'options': ['Xét hàng đơn vị: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên',
                        'Xét hàng chục: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm '
                        'và luyện tập chung, **Làm tròn đến hàng chục** được xác định bởi: Xét hàng đơn vị: '
                        '$< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung**, nội '
                 'dung/biểu thức Xét hàng chục: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Làm tròn đến hàng chục',
                        'Làm tròn đến hàng trăm',
                        'Phân tích số',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung, biểu '
                        'thức/quy tắc Xét hàng chục: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên '
                        'chính là nội dung của **Làm tròn đến hàng trăm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi làm tròn số $3\\,650$ đến hàng trăm, ta được số nào?',
            'options': ['$3\\,600$', '$3\\,650$', '$3\\,700$', '$4\\,000$'],
            'answer': 2,
            'solution': 'Chữ số hàng chục là $5 \\ge 5$ nên làm tròn lên đến hàng trăm được **$3\\,700$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung** (Chủ đề 8: '
                 'Các số đến 10 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Làm tròn được một số đến hàng chục dựa vào chữ số hàng đơn vị.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện '
                        'tập chung: Làm tròn được một số đến hàng chục dựa vào chữ số hàng đơn vị.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số $5\\,429$ làm tròn đến hàng chục được $5\\,430$, còn làm tròn đến hàng trăm '
                 'được $5\\,400$."',
            'answer': True,
            'solution': 'Đơn vị $9 \\ge 5 \\rightarrow 5\\,430$; chục $2 < 5 \\rightarrow 5\\,400$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung**, quy tắc '
                 '**Làm tròn đến hàng chục** được xác định bởi Xét hàng đơn vị: $< 5 \\rightarrow$ xuống · '
                 '$\\ge 5 \\rightarrow$ lên và áp dụng trực tiếp vào bài toán: “Làm tròn số $4\\,762$ đến '
                 'hàng chục và đến hàng trăm.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Làm tròn đến hàng chục** (Xét hàng đơn vị: $< 5 '
                        '\\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên) là kiến thức cốt lõi của Bài 48, '
                        '49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung. - Làm tròn đến hàng '
                        'chục: chữ số hàng đơn vị là $2 < 5$ nên được **$4\\,760$**. - Làm tròn đến hàng '
                        'trăm: chữ số hàng chục là $6 \\ge 5$ nên đ...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện tập chung** '
                 'để giải quyết tình huống sau: Làm tròn số $4\\,762$ đến hàng chục và đến hàng trăm. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['- Làm tròn đến hàng chục: chữ số hàng đơn vị là $2 < 5$ nên được **$4\\,760$**. - '
                        'Làm tròn đến hàng trăm: chữ số hàng chục là $6 \\ge 5$ nên được **$4\\,800$*...',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 48, 49: Làm tròn số đến hàng chục, hàng trăm và luyện '
                        'tập chung: - Làm tròn đến hàng chục: chữ số hàng đơn vị là $2 < 5$ nên được '
                        '**$4\\,760$**.\n'
                        '- Làm tròn đến hàng trăm: chữ số hàng chục là $6 \\ge 5$ nên được **$4\\,800$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một trường tiểu học có $1\\,347$ học sinh. Nếu làm tròn số học sinh đến hàng chục thì '
                 'trường đó có khoảng bao nhiêu học sinh?',
            'answer': ['1350'],
            'unit': 'học sinh',
            'solution': 'Chữ số hàng đơn vị là $7 \\ge 5$ nên làm tròn lên đến hàng chục được **$1\\,350$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd09-chu-vi-dien-tich',
  'context_title': 'Chủ đề 9: Chu vi, diện tích một số hình phẳng',
  'context': 'SGK Toán 3 · Chủ đề 9: Chu vi và diện tích một số hình phẳng.',
  'title': 'Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông',
  'icon': '📐',
  'description': 'Quy tắc và công thức tính chu vi của hình tam giác, hình tứ giác, hình chữ nhật và hình '
                 'vuông.',
  'requirements': ['Hiểu chu vi của một hình phẳng là tổng độ dài các cạnh của hình đó.',
                   'Thuộc và vận dụng đúng công thức tính chu vi hình chữ nhật $P = (a + b) \\times 2$ và '
                   'chu vi hình vuông $P = a \\times 4$.',
                   'Tìm được độ dài cạnh khi biết chu vi của hình vuông hoặc hình chữ nhật.'],
  'definition': '- **Chu vi** của hình tam giác, hình tứ giác là **tổng độ dài các cạnh** của hình đó (cùng '
                'đơn vị đo).\n'
                '- **Chu vi hình chữ nhật**: Muốn tính chu vi hình chữ nhật, ta lấy chiều dài cộng với chiều '
                'rộng (cùng đơn vị đo) rồi nhân với $2$.\n'
                '- **Chu vi hình vuông**: Muốn tính chu vi hình vuông, ta lấy độ dài một cạnh nhân với $4$.',
  'theory': '### 1. Chu vi hình tam giác, hình tứ giác\n'
            '- Tam giác có ba cạnh $a, b, c$: $P = a + b + c$.\n'
            '- Tứ giác có bốn cạnh $a, b, c, d$: $P = a + b + c + d$.\n'
            '### 2. Chu vi hình chữ nhật và hình vuông\n'
            '- Hình chữ nhật có chiều dài $a$, chiều rộng $b$: $P = (a + b) \\times 2$. Nửa chu vi là $a + b '
            '= P : 2$.\n'
            '- Hình vuông có cạnh $a$: $P = a \\times 4 \\Rightarrow a = P : 4$.',
  'formulas': [{'category': 'I. Công thức chu vi',
                'items': [{'name': 'Hình tam giác, tứ giác', 'formula': '$P = \\text{Tổng độ dài các cạnh}$'},
                          {'name': 'Hình chữ nhật', 'formula': '$P = (a + b) \\times 2$ (cùng đơn vị đo)'},
                          {'name': 'Hình vuông',
                           'formula': '$P = a \\times 4 \\Leftrightarrow a = P : 4$'}]}],
  'example': 'Tính chu vi hình chữ nhật có chiều dài $2\\text{ dm}$ và chiều rộng $8\\text{ cm}$.',
  'example_answer': 'Đổi $2\\text{ dm} = 20\\text{ cm}$.\n'
                    'Chu vi hình chữ nhật là: $(20 + 8) \\times 2 = 56\\text{ (cm)}$.\n'
                    'Đáp số: **$56\\text{ cm}$**.',
  'real_life': '- Tính chiều dài hàng rào bao quanh mảnh vườn; tính độ dài nẹp gỗ làm khung tranh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Chu vi của hình vuông có cạnh $6\\text{ cm}$ là:',
            'options': ['$12\\text{ cm}$', '$36\\text{ cm}$', '$10\\text{ cm}$', '$24\\text{ cm}$'],
            'answer': 3,
            'solution': 'Chu vi hình vuông: $P = 6 \\times 4 = 24\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình tam giác có độ dài ba cạnh lần lượt là $5\\text{ cm}, 7\\text{ cm}, 8\\text{ cm}$. '
                 'Chu vi hình tam giác đó là:',
            'options': ['$20\\text{ cm}$', '$15\\text{ cm}$', '$280\\text{ cm}$', '$13\\text{ cm}$'],
            'answer': 0,
            'solution': 'Chu vi tam giác: $5 + 7 + 8 = 20\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, '
                 'hình vuông**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hình tam giác, tứ '
                 'giác**?',
            'options': ['$P = (a + b) \\times 2$ (cùng đơn vị đo)',
                        '$P = \\text{Tổng độ dài các cạnh}$',
                        '$P = a \\times 4 \\Leftrightarrow a = P : 4$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 50: Chu vi hình tam giác, hình tứ giác, hình '
                        'chữ nhật, hình vuông, **Hình tam giác, tứ giác** được xác định bởi: $P = '
                        '\\text{Tổng độ dài các cạnh}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông**, nội '
                 'dung/biểu thức $P = (a + b) \\times 2$ (cùng đơn vị đo) là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Hình tam giác, tứ giác', 'Hình vuông', 'Hình chữ nhật', 'Phân tích số'],
            'answer': 2,
            'solution': 'Trong Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông, biểu '
                        'thức/quy tắc $P = (a + b) \\times 2$ (cùng đơn vị đo) chính là nội dung của **Hình '
                        'chữ nhật**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình chữ nhật có chiều dài $9\\text{ cm}$ và chiều rộng $5\\text{ cm}$. Chu vi hình '
                 'chữ nhật đó là:',
            'options': ['$14\\text{ cm}$', '$45\\text{ cm}$', '$24\\text{ cm}$', '$28\\text{ cm}$'],
            'answer': 3,
            'solution': 'Chu vi hình chữ nhật: $(9 + 5) \\times 2 = 28\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông** (Chủ đề '
                 '9: Chu vi, diện tích một số hình phẳng), khẳng định nào sau đây phản ánh **đúng** yêu cầu '
                 'cần đạt và bản chất kiến thức của bài?',
            'options': ['Hiểu chu vi của một hình phẳng là tổng độ dài các cạnh của hình đó.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, '
                        'hình vuông: Hiểu chu vi của một hình phẳng là tổng độ dài các cạnh của hình đó.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hình chữ nhật có chiều dài $1\\text{ dm}$, chiều rộng $4\\text{ cm}$ thì có '
                 'chu vi là $10\\text{ cm}$."',
            'answer': False,
            'solution': 'Đổi $1\\text{ dm} = 10\\text{ cm}$, chu vi là $(10 + 4) \\times 2 = 28\\text{ cm}$, '
                        'không phải $10\\text{ cm}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông**, quy tắc '
                 '**Hình tam giác, tứ giác** được xác định bởi $P = \\text{Tổng độ dài các cạnh}$ và áp dụng '
                 'trực tiếp vào bài toán: “Tính chu vi hình chữ nhật có chiều dài $2\\text{ dm}$ và chiều '
                 'rộng $8\\text{ cm}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Hình tam giác, tứ giác** ($P = \\text{Tổng độ dài '
                        'các cạnh}$) là kiến thức cốt lõi của Bài 50: Chu vi hình tam giác, hình tứ giác, '
                        'hình chữ nhật, hình vuông. Đổi $2\\text{ dm} = 20\\text{ cm}$. Chu vi hình chữ nhật '
                        'là: $(20 + 8) \\times 2 = 56\\text{ (cm)}$. Đáp số: **$56\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình '
                 'vuông** để giải quyết tình huống sau: Tính chu vi hình chữ nhật có chiều dài $2\\text{ '
                 'dm}$ và chiều rộng $8\\text{ cm}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Đổi $2\\text{ dm} = 20\\text{ cm}$. Chu vi hình chữ nhật là: $(20 + 8) \\times 2 = '
                        '56\\text{ (cm)}$. Đáp số: **$56\\text{ cm}$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, '
                        'hình vuông: Đổi $2\\text{ dm} = 20\\text{ cm}$.\n'
                        'Chu vi hình chữ nhật là: $(20 + 8) \\times 2 = 56\\text{ (cm)}$.\n'
                        'Đáp số: **$56\\text{ cm}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mảnh vườn hình vuông có chu vi bằng $36\\text{ m}$. Hỏi độ dài mỗi cạnh của mảnh vườn '
                 'là bao nhiêu mét?',
            'answer': ['9'],
            'unit': 'm',
            'solution': 'Độ dài cạnh mảnh vườn hình vuông là: $36 : 4 = 9\\text{ (m)}$.\n'
                        'Đáp số: **$9\\text{ m}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd09-chu-vi-dien-tich',
  'context_title': 'Chủ đề 9: Chu vi, diện tích một số hình phẳng',
  'context': 'SGK Toán 3 · Chủ đề 9: Chu vi và diện tích một số hình phẳng.',
  'title': 'Bài 51: Diện tích của một hình. Xăng-ti-mét vuông',
  'icon': '🟩',
  'description': 'Nhận biết biểu tượng về diện tích của một hình và đơn vị đo diện tích xăng-ti-mét vuông '
                 '(cm²).',
  'requirements': ['Nhận biết và so sánh được diện tích của các hình thông qua đặt chồng hình hoặc tách – '
                   'ghép hình.',
                   'Nhận biết đơn vị đo diện tích xăng-ti-mét vuông ($\\text{cm}^2$) là diện tích hình vuông '
                   'cạnh $1\\text{ cm}$.',
                   'Đọc, viết và thực hiện được các phép tính với số đo diện tích theo đơn vị '
                   '$\\text{cm}^2$.'],
  'definition': '- Phần mặt phẳng nằm bên trong đường bao của một hình là **diện tích** của hình đó.\n'
                '- **Xăng-ti-mét vuông** (viết tắt là $\\text{cm}^2$) là diện tích của hình vuông có cạnh '
                'dài $1\\text{ cm}$.',
  'theory': '### 1. So sánh diện tích hai hình\n'
            '- Nếu hình $A$ nằm hoàn toàn bên trong hình $B$ thì diện tích hình $A$ bé hơn diện tích hình '
            '$B$.\n'
            '- Nếu một hình được tách thành hai hình nhỏ thì diện tích hình lớn bằng tổng diện tích hai hình '
            'nhỏ.\n'
            '### 2. Tính diện tích bằng cách đếm ô vuông $1\\text{ cm}^2$\n'
            '- Một hình được ghép bởi $n$ ô vuông cạnh $1\\text{ cm}$ thì có diện tích là $n\\text{ cm}^2$.',
  'formulas': [{'category': 'I. Đơn vị đo diện tích',
                'items': [{'name': 'Xăng-ti-mét vuông',
                           'formula': '$1\\text{ cm}^2$: diện tích hình vuông cạnh $1\\text{ cm}$'},
                          {'name': 'Cộng, trừ diện tích',
                           'formula': '$a\\text{ cm}^2 + b\\text{ cm}^2 = (a + b)\\text{ cm}^2$'}]}],
  'example': 'Hình $M$ gồm $7$ ô vuông $1\\text{ cm}^2$, hình $N$ gồm $5$ ô vuông $1\\text{ cm}^2$. Tính '
             'tổng diện tích hai hình.',
  'example_answer': 'Diện tích hình $M$ là $7\\text{ cm}^2$, diện tích hình $N$ là $5\\text{ cm}^2$.\n'
                    'Tổng diện tích hai hình là: $7 + 5 = 12\\text{ (cm}^2\\text{)}$.',
  'real_life': '- So sánh diện tích hai phòng học, diện tích mặt bàn; đếm số viên gạch bông lát kín nền nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Xăng-ti-mét vuông là diện tích của hình vuông có cạnh dài:',
            'options': ['$1\\text{ cm}$', '$1\\text{ mm}$', '$1\\text{ dm}$', '$1\\text{ m}$'],
            'answer': 0,
            'solution': '$1\\text{ cm}^2$ là diện tích của hình vuông có cạnh dài **$1\\text{ cm}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': '"Mười tám xăng-ti-mét vuông" được viết là:',
            'options': ['$18\\text{ cm}$', '$18\\text{ cm}^2$', '$81\\text{ cm}^2$', '$180\\text{ cm}^2$'],
            'answer': 1,
            'solution': 'Viết là **$18\\text{ cm}^2$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 51: Diện tích của một hình. Xăng-ti-mét vuông**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Xăng-ti-mét vuông**?',
            'options': ['$a\\text{ cm}^2 + b\\text{ cm}^2 = (a + b)\\text{ cm}^2$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$1\\text{ cm}^2$: diện tích hình vuông cạnh $1\\text{ cm}$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 51: Diện tích của một hình. Xăng-ti-mét '
                        'vuông, **Xăng-ti-mét vuông** được xác định bởi: $1\\text{ cm}^2$: diện tích hình '
                        'vuông cạnh $1\\text{ cm}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 51: Diện tích của một hình. Xăng-ti-mét vuông**, nội dung/biểu thức $a\\text{ '
                 'cm}^2 + b\\text{ cm}^2 = (a + b)\\text{ cm}^2$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Xăng-ti-mét vuông',
                        'Phân tích số',
                        'Số tròn trăm, tròn nghìn',
                        'Cộng, trừ diện tích'],
            'answer': 3,
            'solution': 'Trong Bài 51: Diện tích của một hình. Xăng-ti-mét vuông, biểu thức/quy tắc '
                        '$a\\text{ cm}^2 + b\\text{ cm}^2 = (a + b)\\text{ cm}^2$ chính là nội dung của '
                        '**Cộng, trừ diện tích**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình phẳng được ghép bởi $9$ ô vuông, mỗi ô vuông có diện tích $1\\text{ cm}^2$. Diện '
                 'tích hình đó là:',
            'options': ['$9\\text{ cm}^2$', '$9\\text{ cm}$', '$36\\text{ cm}^2$', '$18\\text{ cm}^2$'],
            'answer': 0,
            'solution': 'Gồm $9$ ô vuông $1\\text{ cm}^2$ nên diện tích là **$9\\text{ cm}^2$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 51: Diện tích của một hình. Xăng-ti-mét vuông** (Chủ đề 9: Chu vi, diện tích '
                 'một số hình phẳng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Nhận biết và so sánh được diện tích của các hình thông qua đặt chồng hình hoặc tách '
                        '– ghép hình.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 51: Diện tích của một hình. Xăng-ti-mét vuông: Nhận '
                        'biết và so sánh được diện tích của các hình thông qua đặt chồng hình hoặc tách – '
                        'ghép hình.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Kết quả của phép tính $25\\text{ cm}^2 + 15\\text{ cm}^2$ là $40\\text{ cm}$."',
            'answer': False,
            'solution': 'Đơn vị của kết quả phải là $\\text{cm}^2$ ($40\\text{ cm}^2$), không phải '
                        '$\\text{cm}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 51: Diện tích của một hình. Xăng-ti-mét vuông**, quy tắc **Xăng-ti-mét vuông** '
                 'được xác định bởi $1\\text{ cm}^2$: diện tích hình vuông cạnh $1\\text{ cm}$ và áp dụng '
                 'trực tiếp vào bài toán: “Hình $M$ gồm $7$ ô vuông $1\\text{ cm}^2$, hình $N$ gồm $5$ ô '
                 'vuông $1\\text{ cm}^2$. Tính tổng diện tích hai hình.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Xăng-ti-mét vuông** ($1\\text{ cm}^2$: diện tích '
                        'hình vuông cạnh $1\\text{ cm}$) là kiến thức cốt lõi của Bài 51: Diện tích của một '
                        'hình. Xăng-ti-mét vuông. Diện tích hình $M$ là $7\\text{ cm}^2$, diện tích hình $N$ '
                        'là $5\\text{ cm}^2$. Tổng diện tích hai hình là: $7 + 5 = 12\\text{ '
                        '(cm}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 51: Diện tích của một hình. Xăng-ti-mét vuông** để giải quyết '
                 'tình huống sau: Hình $M$ gồm $7$ ô vuông $1\\text{ cm}^2$, hình $N$ gồm $5$ ô vuông '
                 '$1\\text{ cm}^2$. Tính tổng diện tích hai hình. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Diện tích hình $M$ là $7\\text{ cm}^2$, diện tích hình $N$ là $5\\text{ cm}^2$. '
                        'Tổng diện tích hai hình là: $7 + 5 = 12\\text{ (cm}^2\\text{)}$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 51: Diện tích của một hình. Xăng-ti-mét vuông: Diện tích '
                        'hình $M$ là $7\\text{ cm}^2$, diện tích hình $N$ là $5\\text{ cm}^2$.\n'
                        'Tổng diện tích hai hình là: $7 + 5 = 12\\text{ (cm}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tờ giấy màu có diện tích $60\\text{ cm}^2$, bạn Lan cắt đi một mảnh có diện tích '
                 '$18\\text{ cm}^2$. Hỏi phần giấy màu còn lại có diện tích bao nhiêu xăng-ti-mét vuông?',
            'answer': ['42'],
            'unit': 'cm²',
            'solution': 'Diện tích phần giấy còn lại là: $60 - 18 = 42\\text{ (cm}^2\\text{)}$.\n'
                        'Đáp số: **$42\\text{ cm}^2$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd09-chu-vi-dien-tich',
  'context_title': 'Chủ đề 9: Chu vi, diện tích một số hình phẳng',
  'context': 'SGK Toán 3 · Chủ đề 9: Chu vi và diện tích một số hình phẳng.',
  'title': 'Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và luyện tập chung',
  'icon': '⬛',
  'description': 'Công thức tính diện tích hình chữ nhật, diện tích hình vuông và vận dụng giải toán thực '
                 'tiễn.',
  'requirements': ['Thuộc và vận dụng đúng công thức tính diện tích hình chữ nhật $S = a \\times b$ (cùng '
                   'đơn vị đo).',
                   'Thuộc và vận dụng đúng công thức tính diện tích hình vuông $S = a \\times a$.',
                   'Giải được các bài toán kết hợp chu vi và diện tích của hình chữ nhật, hình vuông.'],
  'definition': '- **Diện tích hình chữ nhật**: Muốn tính diện tích hình chữ nhật, ta lấy chiều dài nhân với '
                'chiều rộng (cùng đơn vị đo): $S = a \\times b$.\n'
                '- **Diện tích hình vuông**: Muốn tính diện tích hình vuông, ta lấy độ dài một cạnh nhân với '
                'chính nó: $S = a \\times a$.',
  'theory': '### 1. Diện tích hình chữ nhật\n'
            '- Ví dụ: Hình chữ nhật có chiều dài $8\\text{ cm}$, chiều rộng $3\\text{ cm}$ có diện tích là '
            '$8 \\times 3 = 24\\text{ (cm}^2\\text{)}$.\n'
            '- Lưu ý: Nếu chiều dài và chiều rộng chưa cùng đơn vị đo (ví dụ $\\text{dm}$ và $\\text{cm}$), '
            'ta phải đổi về cùng đơn vị $\\text{cm}$ trước khi nhân.\n'
            '### 2. Diện tích hình vuông\n'
            '- Ví dụ: Hình vuông có cạnh $6\\text{ cm}$ có diện tích là $6 \\times 6 = 36\\text{ '
            '(cm}^2\\text{)}$.',
  'formulas': [{'category': 'I. Công thức diện tích',
                'items': [{'name': 'Hình chữ nhật', 'formula': '$S = a \\times b$ ($a, b$ cùng đơn vị đo)'},
                          {'name': 'Hình vuông', 'formula': '$S = a \\times a$'}]},
               {'category': 'II. Phân biệt Chu vi và Diện tích',
                'items': [{'name': 'Hình chữ nhật', 'formula': '$P = (a + b) \\times 2$ · $S = a \\times b$'},
                          {'name': 'Hình vuông', 'formula': '$P = a \\times 4$ · $S = a \\times a$'}]}],
  'example': 'Một tấm bìa hình chữ nhật có chiều rộng $6\\text{ cm}$, chiều dài gấp $2$ lần chiều rộng. Tính '
             'diện tích tấm bìa đó.',
  'example_answer': 'Chiều dài tấm bìa là: $6 \\times 2 = 12\\text{ (cm)}$.\n'
                    'Diện tích tấm bìa là: $12 \\times 6 = 72\\text{ (cm}^2\\text{)}$.\n'
                    'Đáp số: **$72\\text{ cm}^2$**.',
  'real_life': '- Tính diện tích kính làm mặt bàn, diện tích giấy dán tường hoặc diện tích mảnh đất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Diện tích của hình vuông có cạnh $6\\text{ cm}$ là:',
            'options': ['$24\\text{ cm}^2$', '$36\\text{ cm}^2$', '$12\\text{ cm}^2$', '$36\\text{ cm}$'],
            'answer': 1,
            'solution': 'Diện tích hình vuông: $S = 6 \\times 6 = 36\\text{ (cm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình chữ nhật có chiều dài $8\\text{ cm}$, chiều rộng $3\\text{ cm}$ có diện tích là:',
            'options': ['$22\\text{ cm}^2$', '$11\\text{ cm}^2$', '$24\\text{ cm}^2$', '$24\\text{ cm}$'],
            'answer': 2,
            'solution': 'Diện tích hình chữ nhật: $S = 8 \\times 3 = 24\\text{ (cm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và '
                 'luyện tập chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hình chữ nhật**?',
            'options': ['$S = a \\times a$',
                        '$P = (a + b) \\times 2$ · $S = a \\times b$',
                        '$P = a \\times 4$ · $S = a \\times a$',
                        '$S = a \\times b$ ($a, b$ cùng đơn vị đo)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 52, 53: Diện tích hình chữ nhật, diện tích '
                        'hình vuông và luyện tập chung, **Hình chữ nhật** được xác định bởi: $S = a \\times '
                        'b$ ($a, b$ cùng đơn vị đo).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và luyện tập chung**, '
                 'nội dung/biểu thức $S = a \\times a$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hình vuông', 'Hình chữ nhật', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và luyện tập chung, '
                        'biểu thức/quy tắc $S = a \\times a$ chính là nội dung của **Hình vuông**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình vuông có chu vi là $20\\text{ cm}$. Diện tích của hình vuông đó là:',
            'options': ['$20\\text{ cm}^2$', '$25\\text{ cm}^2$', '$80\\text{ cm}^2$', '$100\\text{ cm}^2$'],
            'answer': 1,
            'solution': 'Cạnh hình vuông là: $20 : 4 = 5\\text{ (cm)}$. Diện tích là: $5 \\times 5 = '
                        '25\\text{ (cm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và luyện tập chung** '
                 '(Chủ đề 9: Chu vi, diện tích một số hình phẳng), khẳng định nào sau đây phản ánh **đúng** '
                 'yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Thuộc và vận dụng đúng công thức tính diện tích hình chữ nhật $S = a \\times b$ '
                        '(cùng đơn vị đo).',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông '
                        'và luyện tập chung: Thuộc và vận dụng đúng công thức tính diện tích hình chữ nhật '
                        '$S = a \\times b$ (cùng đơn vị đo).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hình chữ nhật có chiều dài $5\\text{ cm}$, chiều rộng $3\\text{ cm}$ thì có '
                 'diện tích là $16\\text{ cm}^2$."',
            'answer': False,
            'solution': 'Diện tích là $5 \\times 3 = 15\\text{ cm}^2$ (còn $16\\text{ cm}$ là chu vi) '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và luyện tập chung**, '
                 'quy tắc **Hình chữ nhật** được xác định bởi $S = a \\times b$ ($a, b$ cùng đơn vị đo) và '
                 'áp dụng trực tiếp vào bài toán: “Một tấm bìa hình chữ nhật có chiều rộng $6\\text{ cm}$, '
                 'chiều dài gấp $2$ lần chiều rộng. Tính diện tích tấm bìa đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Hình chữ nhật** ($S = a \\times b$ ($a, b$ cùng đơn '
                        'vị đo)) là kiến thức cốt lõi của Bài 52, 53: Diện tích hình chữ nhật, diện tích '
                        'hình vuông và luyện tập chung. Chiều dài tấm bìa là: $6 \\times 2 = 12\\text{ '
                        '(cm)}$. Diện tích tấm bìa là: $12 \\times 6 = 72\\text{ (cm}^2\\text{)}$. Đáp số: '
                        '**$72\\text{ cm}^2$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và luyện '
                 'tập chung** để giải quyết tình huống sau: Một tấm bìa hình chữ nhật có chiều rộng '
                 '$6\\text{ cm}$, chiều dài gấp $2$ lần chiều rộng. Tính diện tích tấm bìa đó. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Chiều dài tấm bìa là: $6 \\times 2 = 12\\text{ (cm)}$. Diện tích tấm bìa là: $12 '
                        '\\times 6 = 72\\text{ (cm}^2\\text{)}$. Đáp số: **$72\\text{ cm}^2$**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 52, 53: Diện tích hình chữ nhật, diện tích hình vuông và '
                        'luyện tập chung: Chiều dài tấm bìa là: $6 \\times 2 = 12\\text{ (cm)}$.\n'
                        'Diện tích tấm bìa là: $12 \\times 6 = 72\\text{ (cm}^2\\text{)}$.\n'
                        'Đáp số: **$72\\text{ cm}^2$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một nhãn vở hình chữ nhật có chiều dài $8\\text{ cm}$, chiều rộng kém chiều dài $3\\text{ '
                 'cm}$. Tính diện tích nhãn vở đó theo xăng-ti-mét vuông.',
            'answer': ['40'],
            'unit': 'cm²',
            'solution': 'Chiều rộng nhãn vở là: $8 - 3 = 5\\text{ (cm)}$. Diện tích là: $8 \\times 5 = '
                        '40\\text{ (cm}^2\\text{)}$.\n'
                        'Đáp số: **$40\\text{ cm}^2$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd10-cong-tru-nhan-chia-pham-vi-10000',
  'context_title': 'Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000',
  'context': 'SGK Toán 3 · Chủ đề 10: Phép cộng, trừ, nhân, chia trong phạm vi 10 000.',
  'title': 'Bài 54: Phép cộng trong phạm vi 10 000',
  'icon': '➕',
  'description': 'Thực hiện phép cộng các số trong phạm vi 10 000 (không nhớ và có nhớ không quá hai lượt).',
  'requirements': ['Đặt tính và tính đúng phép cộng các số có đến bốn chữ số trong phạm vi $10\\,000$.',
                   'Cộng nhẩm được các số tròn nghìn, tròn trăm.',
                   'Giải được bài toán thực tế liên quan đến phép cộng trong phạm vi $10\\,000$.'],
  'definition': '- Khi đặt tính cộng các số trong phạm vi $10\\,000$, ta viết các chữ số cùng hàng thẳng cột '
                'với nhau.\n'
                '- Cộng lần lượt từ phải sang trái: **đơn vị $\\rightarrow$ chục $\\rightarrow$ trăm '
                '$\\rightarrow$ nghìn**, có nhớ sang hàng kế tiếp.',
  'theory': '### 1. Tính nhẩm số tròn nghìn\n'
            '- Ví dụ: $4\\,000 + 3\\,000 = 7\\,000$ ($4$ nghìn $+ 3$ nghìn $= 7$ nghìn).\n'
            '### 2. Đặt tính rồi tính\n'
            '- Ví dụ: $4\\,527 + 3\\,685$. Ta cộng: $7 + 5 = 12$ (viết $2$ nhớ $1$); $2 + 8 + 1 = 11$ (viết '
            '$1$ nhớ $1$); $5 + 6 + 1 = 12$ (viết $2$ nhớ $1$); $4 + 3 + 1 = 8$. Kết quả: $8\\,212$.',
  'formulas': [{'category': 'I. Phép cộng trong phạm vi 10 000',
                'items': [{'name': 'Quy tắc',
                           'formula': 'Đặt thẳng cột · Cộng từ phải sang trái · Nhớ sang hàng liền trước'},
                          {'name': 'Nhẩm số tròn nghìn', 'formula': '$a\\,000 + b\\,000 = (a + b)\\,000$'}]}],
  'example': 'Đặt tính rồi tính: $3\\,526 + 2\\,748$ và $5\\,400 + 2\\,600$.',
  'example_answer': '- $3\\,526 + 2\\,748 = 6\\,274$.\n- $5\\,400 + 2\\,600 = 8\\,000$.',
  'real_life': '- Tính tổng sản lượng thóc thu hoạch được của hai vụ mùa; tính tổng quãng đường hai chặng '
               'đi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $4\\,000 + 3\\,000 = ?$',
            'options': ['$700$', '$70\\,000$', '$7\\,000$', '$1\\,000$'],
            'answer': 2,
            'solution': '$4$ nghìn $+ 3$ nghìn $= 7\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $2\\,315 + 1\\,462$ là:',
            'options': ['$3\\,767$', '$3\\,877$', '$1\\,147$', '$3\\,777$'],
            'answer': 3,
            'solution': 'Cộng từng hàng không nhớ: $5+2=7, 1+6=7, 3+4=7, 2+1=3 \\rightarrow 3\\,777$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 54: Phép cộng trong phạm vi 10 000**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Quy tắc**?',
            'options': ['Đặt thẳng cột · Cộng từ phải sang trái · Nhớ sang hàng liền trước',
                        '$a\\,000 + b\\,000 = (a + b)\\,000$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 54: Phép cộng trong phạm vi 10 000, **Quy '
                        'tắc** được xác định bởi: Đặt thẳng cột · Cộng từ phải sang trái · Nhớ sang hàng '
                        'liền trước.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 54: Phép cộng trong phạm vi 10 000**, nội dung/biểu thức $a\\,000 + b\\,000 = '
                 '(a + b)\\,000$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quy tắc', 'Nhẩm số tròn nghìn', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 54: Phép cộng trong phạm vi 10 000, biểu thức/quy tắc $a\\,000 + b\\,000 '
                        '= (a + b)\\,000$ chính là nội dung của **Nhẩm số tròn nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng của $4\\,527$ và $3\\,685$ là:',
            'options': ['$8\\,112$', '$7\\,212$', '$8\\,212$', '$8\\,202$'],
            'answer': 2,
            'solution': 'Ta có $4\\,527 + 3\\,685 = 8\\,212$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 54: Phép cộng trong phạm vi 10 000** (Chủ đề 10: Cộng, trừ, nhân, chia trong '
                 'phạm vi 10 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Đặt tính và tính đúng phép cộng các số có đến bốn chữ số trong phạm vi $10\\,000$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 54: Phép cộng trong phạm vi 10 000: Đặt tính và tính '
                        'đúng phép cộng các số có đến bốn chữ số trong phạm vi $10\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$5\\,640 + 2\\,360 = 7\\,900$."',
            'answer': False,
            'solution': 'Ta có $40 + 60 = 100$ (nhớ $1$ sang hàng trăm), nên $5\\,640 + 2\\,360 = 8\\,000$, '
                        'không phải $7\\,900$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 54: Phép cộng trong phạm vi 10 000**, quy tắc **Quy tắc** được xác định bởi '
                 'Đặt thẳng cột · Cộng từ phải sang trái · Nhớ sang hàng liền trước và áp dụng trực tiếp vào '
                 'bài toán: “Đặt tính rồi tính: $3\\,526 + 2\\,748$ và $5\\,400 + 2\\,600$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy tắc** (Đặt thẳng cột · Cộng từ phải sang trái · '
                        'Nhớ sang hàng liền trước) là kiến thức cốt lõi của Bài 54: Phép cộng trong phạm vi '
                        '10 000. - $3\\,526 + 2\\,748 = 6\\,274$. - $5\\,400 + 2\\,600 = 8\\,000$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 54: Phép cộng trong phạm vi 10 000** để giải quyết tình huống '
                 'sau: Đặt tính rồi tính: $3\\,526 + 2\\,748$ và $5\\,400 + 2\\,600$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['- $3\\,526 + 2\\,748 = 6\\,274$. - $5\\,400 + 2\\,600 = 8\\,000$.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 54: Phép cộng trong phạm vi 10 000: - $3\\,526 + 2\\,748 '
                        '= 6\\,274$.\n'
                        '- $5\\,400 + 2\\,600 = 8\\,000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Vụ mùa năm nay gia đình bác Tâm thu hoạch được $3\\,250\\text{ kg}$ thóc nếp và '
                 '$4\\,750\\text{ kg}$ thóc tẻ. Hỏi gia đình bác Tâm thu hoạch được tất cả bao nhiêu '
                 'ki-lô-gam thóc?',
            'answer': ['8000', '8 000'],
            'unit': 'kg',
            'solution': 'Tổng số thóc thu hoạch được là: $3\\,250 + 4\\,750 = 8\\,000\\text{ (kg)}$.\n'
                        'Đáp số: **$8\\,000\\text{ kg}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd10-cong-tru-nhan-chia-pham-vi-10000',
  'context_title': 'Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000',
  'context': 'SGK Toán 3 · Chủ đề 10: Phép cộng, trừ, nhân, chia trong phạm vi 10 000.',
  'title': 'Bài 55: Phép trừ trong phạm vi 10 000',
  'icon': '➖',
  'description': 'Thực hiện phép trừ các số trong phạm vi 10 000 và thử lại phép trừ bằng phép cộng.',
  'requirements': ['Đặt tính và tính đúng phép trừ các số trong phạm vi $10\\,000$.',
                   'Trừ nhẩm được các số tròn nghìn, tròn trăm.',
                   'Giải được bài toán thực tế có phép trừ trong phạm vi $10\\,000$.'],
  'definition': '- Khi đặt tính trừ các số trong phạm vi $10\\,000$, ta viết số trừ dưới số bị trừ sao cho '
                'các chữ số cùng hàng thẳng cột.\n'
                '- Trừ lần lượt từ phải sang trái; nếu chữ số ở số bị trừ bé hơn chữ số tương ứng ở số trừ '
                'thì mượn $10$ ở hàng liền trước rồi trả $1$ vào lượt trừ kế tiếp.',
  'theory': '### 1. Tính nhẩm số tròn nghìn\n'
            '- Ví dụ: $9\\,000 - 5\\,000 = 4\\,000$ ($9$ nghìn $- 5$ nghìn $= 4$ nghìn).\n'
            '### 2. Đặt tính rồi tính\n'
            '- Ví dụ: $7\\,452 - 3\\,218 = 4\\,234$.\n'
            '- Ví dụ trừ qua số tròn nghìn: $6\\,000 - 2\\,785 = 3\\,215$ (thử lại: $3\\,215 + 2\\,785 = '
            '6\\,000$).',
  'formulas': [{'category': 'I. Phép trừ trong phạm vi 10 000',
                'items': [{'name': 'Quy tắc',
                           'formula': 'Đặt thẳng cột · Trừ từ phải sang trái · Nhớ $1$ khi mượn'},
                          {'name': 'Thử lại phép trừ',
                           'formula': '$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$'}]}],
  'example': 'Đặt tính rồi tính: $8\\,536 - 4\\,271$ và $10\\,000 - 3\\,500$.',
  'example_answer': '- $8\\,536 - 4\\,271 = 4\\,265$.\n- $10\\,000 - 3\\,500 = 6\\,500$.',
  'real_life': '- Tính số tiền còn lại sau khi thanh toán hóa đơn; tính quãng đường còn lại phải đi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $9\\,000 - 5\\,000 = ?$',
            'options': ['$14\\,000$', '$400$', '$5\\,000$', '$4\\,000$'],
            'answer': 3,
            'solution': '$9$ nghìn $- 5$ nghìn $= 4\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $7\\,452 - 3\\,218$ là:',
            'options': ['$4\\,234$', '$4\\,244$', '$4\\,334$', '$3\\,234$'],
            'answer': 0,
            'solution': 'Trừ từ phải sang trái: $12-8=4$ (nhớ $1$), $5-2=3$, $4-2=2$, $7-3=4 \\rightarrow '
                        '4\\,234$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 55: Phép trừ trong phạm vi 10 000**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Quy tắc**?',
            'options': ['$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                        'Đặt thẳng cột · Trừ từ phải sang trái · Nhớ $1$ khi mượn',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 55: Phép trừ trong phạm vi 10 000, **Quy '
                        'tắc** được xác định bởi: Đặt thẳng cột · Trừ từ phải sang trái · Nhớ $1$ khi mượn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 55: Phép trừ trong phạm vi 10 000**, nội dung/biểu thức $\\text{Hiệu} + '
                 '\\text{Số trừ} = \\text{Số bị trừ}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quy tắc', 'Phân tích số', 'Thử lại phép trừ', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 55: Phép trừ trong phạm vi 10 000, biểu thức/quy tắc $\\text{Hiệu} + '
                        '\\text{Số trừ} = \\text{Số bị trừ}$ chính là nội dung của **Thử lại phép trừ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x + 2\\,450 = 6\\,000$:',
            'options': ['$4\\,550$', '$3\\,650$', '$8\\,450$', '$3\\,550$'],
            'answer': 3,
            'solution': 'Số hạng $x = 6\\,000 - 2\\,450 = 3\\,550$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 55: Phép trừ trong phạm vi 10 000** (Chủ đề 10: Cộng, trừ, nhân, chia trong '
                 'phạm vi 10 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đặt tính và tính đúng phép trừ các số trong phạm vi $10\\,000$.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 55: Phép trừ trong phạm vi 10 000: Đặt tính và tính '
                        'đúng phép trừ các số trong phạm vi $10\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$6\\,000 - 2\\,785 = 3\\,215$."',
            'answer': True,
            'solution': 'Thử lại: $3\\,215 + 2\\,785 = 6\\,000$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 55: Phép trừ trong phạm vi 10 000**, quy tắc **Quy tắc** được xác định bởi Đặt '
                 'thẳng cột · Trừ từ phải sang trái · Nhớ $1$ khi mượn và áp dụng trực tiếp vào bài toán: '
                 '“Đặt tính rồi tính: $8\\,536 - 4\\,271$ và $10\\,000 - 3\\,500$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy tắc** (Đặt thẳng cột · Trừ từ phải sang trái · '
                        'Nhớ $1$ khi mượn) là kiến thức cốt lõi của Bài 55: Phép trừ trong phạm vi 10 000. - '
                        '$8\\,536 - 4\\,271 = 4\\,265$. - $10\\,000 - 3\\,500 = 6\\,500$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 55: Phép trừ trong phạm vi 10 000** để giải quyết tình huống sau: '
                 'Đặt tính rồi tính: $8\\,536 - 4\\,271$ và $10\\,000 - 3\\,500$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $8\\,536 - 4\\,271 = 4\\,265$. - $10\\,000 - 3\\,500 = 6\\,500$.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 55: Phép trừ trong phạm vi 10 000: - $8\\,536 - 4\\,271 '
                        '= 4\\,265$.\n'
                        '- $10\\,000 - 3\\,500 = 6\\,500$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một kho chứa $7\\,500\\text{ l}$ xăng, người ta đã xuất đi $2\\,850\\text{ l}$ xăng. Hỏi '
                 'trong kho còn lại bao nhiêu lít xăng?',
            'answer': ['4650', '4 650'],
            'unit': 'l',
            'solution': 'Số lít xăng còn lại là: $7\\,500 - 2\\,850 = 4\\,650\\text{ (l)}$.\n'
                        'Đáp số: **$4\\,650\\text{ l}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd10-cong-tru-nhan-chia-pham-vi-10000',
  'context_title': 'Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000',
  'context': 'SGK Toán 3 · Chủ đề 10: Phép cộng, trừ, nhân, chia trong phạm vi 10 000.',
  'title': 'Bài 56: Nhân số có bốn chữ số với số có một chữ số',
  'icon': '✖️',
  'description': 'Đặt tính và thực hiện phép nhân số có bốn chữ số với số có một chữ số trong phạm vi 10 '
                 '000.',
  'requirements': ['Đặt tính và tính đúng phép nhân số có bốn chữ số với số có một chữ số.',
                   'Nhân nhẩm được số tròn nghìn với số có một chữ số.',
                   'Giải được bài toán có đến hai bước tính liên quan đến phép nhân.'],
  'definition': '- Khi nhân số có bốn chữ số với số có một chữ số, ta nhân lần lượt từ phải sang trái: **đơn '
                'vị $\\rightarrow$ chục $\\rightarrow$ trăm $\\rightarrow$ nghìn**.\n'
                '- Nhớ phần chục của tích ở mỗi hàng sang hàng kế tiếp ngay bên trái.',
  'theory': '### 1. Tính nhẩm số tròn nghìn\n'
            '- Ví dụ: $2\\,000 \\times 3 = 6\\,000$ ($2$ nghìn $\\times 3 = 6$ nghìn).\n'
            '### 2. Đặt tính rồi tính\n'
            '- Ví dụ: $1\\,218 \\times 4 = 4\\,872$ ($8 \\times 4 = 32$ viết $2$ nhớ $3$; $1 \\times 4 + 3 = '
            '7$; $2 \\times 4 = 8$; $1 \\times 4 = 4$).\n'
            '- Ví dụ: $2\\,615 \\times 3 = 7\\,845$.',
  'formulas': [{'category': 'I. Nhân số có bốn chữ số',
                'items': [{'name': 'Thứ tự nhân',
                           'formula': 'Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm $\\rightarrow$ Nghìn'},
                          {'name': 'Nhẩm số tròn nghìn',
                           'formula': '$a\\,000 \\times b = (a \\times b)\\,000$'}]}],
  'example': 'Một nhà máy ngày đầu sản xuất được $1\\,250$ sản phẩm, ngày thứ hai sản xuất gấp đôi ngày đầu. '
             'Hỏi cả hai ngày nhà máy sản xuất được bao nhiêu sản phẩm?',
  'example_answer': 'Ngày thứ hai sản xuất được: $1\\,250 \\times 2 = 2\\,500\\text{ (sản phẩm)}$.\n'
                    'Cả hai ngày sản xuất được: $1\\,250 + 2\\,500 = 3\\,750\\text{ (sản phẩm)}$.',
  'real_life': '- Tính tiền mua nhiều vé tàu hoặc nhiều quyển vở có giá tiền hàng nghìn đồng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $2\\,143 \\times 2$ là:',
            'options': ['$4\\,286$', '$4\\,386$', '$2\\,145$', '$4\\,246$'],
            'answer': 0,
            'solution': 'Nhân từng hàng: $3\\times2=6, 4\\times2=8, 1\\times2=2, 2\\times2=4 \\rightarrow '
                        '4\\,286$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $3\\,000 \\times 3 = ?$',
            'options': ['$6\\,000$', '$9\\,000$', '$900$', '$3\\,003$'],
            'answer': 1,
            'solution': '$3$ nghìn $\\times 3 = 9\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 56: Nhân số có bốn chữ số với số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự nhân**?',
            'options': ['$a\\,000 \\times b = (a \\times b)\\,000$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm $\\rightarrow$ Nghìn',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 56: Nhân số có bốn chữ số với số có một chữ '
                        'số, **Thứ tự nhân** được xác định bởi: Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm $\\rightarrow$ Nghìn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 56: Nhân số có bốn chữ số với số có một chữ số**, nội dung/biểu thức $a\\,000 '
                 '\\times b = (a \\times b)\\,000$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thứ tự nhân', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Nhẩm số tròn nghìn'],
            'answer': 3,
            'solution': 'Trong Bài 56: Nhân số có bốn chữ số với số có một chữ số, biểu thức/quy tắc '
                        '$a\\,000 \\times b = (a \\times b)\\,000$ chính là nội dung của **Nhẩm số tròn '
                        'nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $2\\,615 \\times 3$ là:',
            'options': ['$7\\,845$', '$7\\,835$', '$6\\,845$', '$7\\,945$'],
            'answer': 0,
            'solution': 'Ta có $2\\,615 \\times 3 = 7\\,845$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 56: Nhân số có bốn chữ số với số có một chữ số** (Chủ đề 10: Cộng, trừ, '
                 'nhân, chia trong phạm vi 10 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt '
                 'và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Đặt tính và tính đúng phép nhân số có bốn chữ số với số có một chữ số.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 56: Nhân số có bốn chữ số với số có một chữ số: Đặt '
                        'tính và tính đúng phép nhân số có bốn chữ số với số có một chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$1\\,625 \\times 4 = 6\\,400$."',
            'answer': False,
            'solution': 'Ta có $1\\,625 \\times 4 = 6\\,500$, không phải $6\\,400$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 56: Nhân số có bốn chữ số với số có một chữ số**, quy tắc **Thứ tự nhân** được '
                 'xác định bởi Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm $\\rightarrow$ Nghìn và áp '
                 'dụng trực tiếp vào bài toán: “Một nhà máy ngày đầu sản xuất được $1\\,250$ sản phẩm, ngày '
                 'thứ hai sản xuất gấp đôi ngày đầu. Hỏi cả hai ngày nhà máy sản xuất được bao nhiê...”. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự nhân** (Đơn vị $\\rightarrow$ Chục '
                        '$\\rightarrow$ Trăm $\\rightarrow$ Nghìn) là kiến thức cốt lõi của Bài 56: Nhân số '
                        'có bốn chữ số với số có một chữ số. Ngày thứ hai sản xuất được: $1\\,250 \\times 2 '
                        '= 2\\,500\\text{ (sản phẩm)}$. Cả hai ngày sản xuất được: $1\\,250 + 2\\,500 = '
                        '3\\,750\\text{ (sản phẩm)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 56: Nhân số có bốn chữ số với số có một chữ số** để giải quyết '
                 'tình huống sau: Một nhà máy ngày đầu sản xuất được $1\\,250$ sản phẩm, ngày thứ hai sản '
                 'xuất gấp đôi ngày đầu. Hỏi cả hai ngày nhà máy sản xuất được bao nhiêu sản phẩm? Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Ngày thứ hai sản xuất được: $1\\,250 \\times 2 = 2\\,500\\text{ (sản phẩm)}$. Cả '
                        'hai ngày sản xuất được: $1\\,250 + 2\\,500 = 3\\,750\\text{ (sản phẩm)}$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 56: Nhân số có bốn chữ số với số có một chữ số: Ngày thứ '
                        'hai sản xuất được: $1\\,250 \\times 2 = 2\\,500\\text{ (sản phẩm)}$.\n'
                        'Cả hai ngày sản xuất được: $1\\,250 + 2\\,500 = 3\\,750\\text{ (sản phẩm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi xe tải chở $1\\,420\\text{ kg}$ gạo. Hỏi $5$ xe tải như thế chở tất cả bao nhiêu '
                 'ki-lô-gam gạo?',
            'answer': ['7100', '7 100'],
            'unit': 'kg',
            'solution': 'Tổng số gạo $5$ xe chở là: $1\\,420 \\times 5 = 7\\,100\\text{ (kg)}$.\n'
                        'Đáp số: **$7\\,100\\text{ kg}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd10-cong-tru-nhan-chia-pham-vi-10000',
  'context_title': 'Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000',
  'context': 'SGK Toán 3 · Chủ đề 10: Phép cộng, trừ, nhân, chia trong phạm vi 10 000.',
  'title': 'Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và luyện tập chung',
  'icon': '➗',
  'description': 'Thực hiện phép chia số có bốn chữ số cho số có một chữ số (chia hết và chia có dư) và giải '
                 'toán.',
  'requirements': ['Đặt tính dọc và chia đúng số có bốn chữ số cho số có một chữ số từ hàng cao nhất.',
                   'Xử lý thành thạo trường hợp có chữ số $0$ ở thương.',
                   'Giải được bài toán tổng hợp có hai bước tính trong phạm vi $10\\,000$.'],
  'definition': '- Khi chia số có bốn chữ số cho số có một chữ số, ta bắt đầu chia từ **hàng cao nhất (hàng '
                'nghìn)** rồi lần lượt đến hàng trăm, hàng chục, hàng đơn vị.\n'
                '- Ở mỗi lượt hạ chữ số xuống, nếu số mới bé hơn số chia thì phải **viết $0$ vào thương** '
                'trước khi hạ chữ số tiếp theo.',
  'theory': '### 1. Chia hết và chia có chữ số $0$ ở thương\n'
            '- Ví dụ: $6\\,369 : 3 = 2\\,123$.\n'
            '- Ví dụ có chữ số $0$ ở thương: $2\\,436 : 4$. Lấy $24 : 4 = 6$; hạ $3$, vì $3 < 4$ nên $3 : 4 '
            '= 0$ (viết $0$); hạ $6$ được $36 : 4 = 9$. Vậy $2\\,436 : 4 = 609$.\n'
            '### 2. Chia có dư\n'
            '- Ví dụ: $4\\,219 : 6 = 703 \\text{ (dư } 1\\text{)}$ vì $703 \\times 6 + 1 = 4\\,219$.',
  'formulas': [{'category': 'I. Quy tắc chia',
                'items': [{'name': 'Thứ tự',
                           'formula': 'Từ hàng nghìn (bên trái) sang hàng đơn vị (bên phải)'},
                          {'name': 'Thử lại',
                           'formula': '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số '
                                      'bị chia}$'}]}],
  'example': 'Có $2\\,835$ quyển sách xếp đều vào $5$ tủ. Hỏi mỗi tủ có bao nhiêu quyển sách?',
  'example_answer': 'Thực hiện phép chia $2\\,835 : 5$:\n'
                    '- $28 : 5 = 5$ (dư $3$); hạ $3$ được $33 : 5 = 6$ (dư $3$); hạ $5$ được $35 : 5 = 7$.\n'
                    'Vậy mỗi tủ có **$567$ quyển sách**.',
  'real_life': '- Chia đều kinh phí, số cây giống hoặc số sách vở cho các trường vùng cao.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi chia số có bốn chữ số cho số có một chữ số, ta bắt đầu chia từ:',
            'options': ['Hàng đơn vị', 'Hàng cao nhất (bên trái)', 'Hàng chục', 'Hàng nào cũng được'],
            'answer': 1,
            'solution': 'Phép chia luôn bắt đầu từ **hàng cao nhất (bên trái)**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $8\\,000 : 4 = ?$',
            'options': ['$200$', '$4\\,000$', '$2\\,000$', '$32\\,000$'],
            'answer': 2,
            'solution': '$8$ nghìn $: 4 = 2$ nghìn $= 2\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và '
                 'luyện tập chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự**?',
            'options': ['$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Từ hàng nghìn (bên trái) sang hàng đơn vị (bên phải)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 57, 58: Chia số có bốn chữ số cho số có một '
                        'chữ số và luyện tập chung, **Thứ tự** được xác định bởi: Từ hàng nghìn (bên trái) '
                        'sang hàng đơn vị (bên phải).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và luyện tập chung**, nội '
                 'dung/biểu thức $\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị '
                 'chia}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thử lại', 'Thứ tự', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và luyện tập chung, '
                        'biểu thức/quy tắc $\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = '
                        '\\text{Số bị chia}$ chính là nội dung của **Thử lại**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $2\\,436 : 4$ là:',
            'options': ['$690$', '$609$', '$69$', '$6\\,009$'],
            'answer': 1,
            'solution': 'Ta có $24 : 4 = 6$; hạ $3$ ($3 : 4 = 0$); hạ $6$ được $36 : 4 = 9 \\rightarrow '
                        '609$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và luyện tập chung** (Chủ '
                 'đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đặt tính dọc và chia đúng số có bốn chữ số cho số có một chữ số từ hàng cao nhất.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và '
                        'luyện tập chung: Đặt tính dọc và chia đúng số có bốn chữ số cho số có một chữ số từ '
                        'hàng cao nhất.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $3\\,640 : 5$ có thương là $728$."',
            'answer': True,
            'solution': 'Vì $728 \\times 5 = 3\\,640$ nên $3\\,640 : 5 = 728$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và luyện tập chung**, quy '
                 'tắc **Thứ tự** được xác định bởi Từ hàng nghìn (bên trái) sang hàng đơn vị (bên phải) và '
                 'áp dụng trực tiếp vào bài toán: “Có $2\\,835$ quyển sách xếp đều vào $5$ tủ. Hỏi mỗi tủ có '
                 'bao nhiêu quyển sách?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự** (Từ hàng nghìn (bên trái) sang hàng đơn vị '
                        '(bên phải)) là kiến thức cốt lõi của Bài 57, 58: Chia số có bốn chữ số cho số có '
                        'một chữ số và luyện tập chung. Thực hiện phép chia $2\\,835 : 5$: - $28 : 5 = 5$ '
                        '(dư $3$); hạ $3$ được $33 : 5 = 6$ (dư $3$); hạ $5$ được $35 : 5 = 7$. Vậy mỗi tủ '
                        'có **$567$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và luyện tập '
                 'chung** để giải quyết tình huống sau: Có $2\\,835$ quyển sách xếp đều vào $5$ tủ. Hỏi mỗi '
                 'tủ có bao nhiêu quyển sách? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Thực hiện phép chia $2\\,835 : 5$: - $28 : 5 = 5$ (dư $3$); hạ $3$ được $33 : 5 = '
                        '6$ (dư $3$); hạ $5$ được $35 : 5 = 7$. Vậy mỗi tủ có **$567$ quyển sách**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 57, 58: Chia số có bốn chữ số cho số có một chữ số và '
                        'luyện tập chung: Thực hiện phép chia $2\\,835 : 5$:\n'
                        '- $28 : 5 = 5$ (dư $3$); hạ $3$ được $33 : 5 = 6$ (dư $3$); hạ $5$ được $35 : 5 = '
                        '7$.\n'
                        'Vậy mỗi tủ có **$567$ quyển sách**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Người ta lắp bánh xe cho các ô tô tải, mỗi ô tô cần $6$ bánh xe. Hỏi có $1\\,236$ bánh xe '
                 'thì lắp được cho bao nhiêu ô tô như thế?',
            'answer': ['206'],
            'unit': 'ô tô',
            'solution': 'Số ô tô lắp được là: $1\\,236 : 6 = 206\\text{ (ô tô)}$.\n'
                        'Đáp số: **$206\\text{ ô tô}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd11-cac-so-den-100000',
  'context_title': 'Chủ đề 11: Các số đến 100 000',
  'context': 'SGK Toán 3 · Chủ đề 11: Các số trong phạm vi 100 000.',
  'title': 'Bài 59: Các số có năm chữ số. Số 100 000',
  'icon': '💯',
  'description': 'Đọc, viết, xác định hàng và phân tích cấu tạo thập phân của các số có năm chữ số và số 100 '
                 '000.',
  'requirements': ['Đọc, viết được các số có năm chữ số và số $100\\,000$ (một trăm nghìn).',
                   'Xác định đúng chữ số thuộc hàng chục nghìn, nghìn, trăm, chục, đơn vị.',
                   'Phân tích được số có năm chữ số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.'],
  'definition': '- **Số có năm chữ số** gồm $5$ hàng từ trái sang phải: **hàng chục nghìn, hàng nghìn, hàng '
                'trăm, hàng chục, hàng đơn vị**.\n'
                '- Mười chục nghìn bằng một trăm nghìn, viết là **$100\\,000$** ($6$ chữ số).',
  'theory': '### 1. Cấu tạo số có năm chữ số\n'
            '- Ví dụ: $45\\,813 = 40\\,000 + 5\\,000 + 800 + 10 + 3$ (gồm $4$ chục nghìn, $5$ nghìn, $8$ '
            'trăm, $1$ chục, $3$ đơn vị).\n'
            '- Ví dụ có chữ số $0$: $60\\,409 = 60\\,000 + 400 + 9$ đọc là "sáu mươi nghìn bốn trăm linh '
            'chín".\n'
            '### 2. Số $100\\,000$\n'
            '- Số liền sau của $99\\,999$ là $100\\,000$ ($99\\,999 + 1 = 100\\,000$).',
  'formulas': [{'category': 'I. Cấu tạo số năm chữ số',
                'items': [{'name': 'Khai triển tổng',
                           'formula': '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'},
                          {'name': 'Số một trăm nghìn',
                           'formula': '$10 \\text{ chục nghìn} = 100\\,000$ · $99\\,999 + 1 = 100\\,000$'}]}],
  'example': 'Viết số "ba mươi hai nghìn không trăm mười lăm" (gồm $5$ chữ số) và chỉ rõ chữ số hàng chục '
             'nghìn, hàng nghìn.',
  'example_answer': 'Số đó viết là **$32\\,015$**, trong đó chữ số hàng chục nghìn là **$3$** và chữ số hàng '
                    'nghìn là **$2$**.',
  'real_life': '- Đọc giá tiền các mặt hàng quen thuộc ($35\\,000$ đồng, $100\\,000$ đồng) hoặc số dân của '
               'một huyện.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số "ba mươi hai nghìn không trăm mười lăm" được viết là:',
            'options': ['$32\\,150$', '$3\\,215$', '$32\\,015$', '$320\\,015$'],
            'answer': 2,
            'solution': 'Ta có $30\\,000 + 2\\,000 + 10 + 5 = 32\\,015$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số $58\\,247$, chữ số $8$ thuộc hàng nào?',
            'options': ['Hàng chục nghìn', 'Hàng trăm', 'Hàng chục', 'Hàng nghìn'],
            'answer': 3,
            'solution': 'Từ trái sang phải: $5$ chục nghìn, **$8$ nghìn**, $2$ trăm, $4$ chục, $7$ đơn vị.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 59: Các số có năm chữ số. Số 100 000**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Khai triển tổng**?',
            'options': ['$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$10 \\text{ chục nghìn} = 100\\,000$ · $99\\,999 + 1 = 100\\,000$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 59: Các số có năm chữ số. Số 100 000, **Khai '
                        'triển tổng** được xác định bởi: $\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 '
                        '+ e$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 59: Các số có năm chữ số. Số 100 000**, nội dung/biểu thức $10 \\text{ chục '
                 'nghìn} = 100\\,000$ · $99\\,999 + 1 = 100\\,000$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Khai triển tổng', 'Số một trăm nghìn', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 59: Các số có năm chữ số. Số 100 000, biểu thức/quy tắc $10 \\text{ chục '
                        'nghìn} = 100\\,000$ · $99\\,999 + 1 = 100\\,000$ chính là nội dung của **Số một '
                        'trăm nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số liền trước của số $100\\,000$ là:',
            'options': ['$100\\,001$', '$99\\,000$', '$99\\,999$', '$10\\,000$'],
            'answer': 2,
            'solution': 'Ta có $100\\,000 - 1 = 99\\,999$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 59: Các số có năm chữ số. Số 100 000** (Chủ đề 11: Các số đến 100 000), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Đọc, viết được các số có năm chữ số và số $100\\,000$ (một trăm nghìn).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 59: Các số có năm chữ số. Số 100 000: Đọc, viết được '
                        'các số có năm chữ số và số $100\\,000$ (một trăm nghìn).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$40\\,000 + 5\\,000 + 30 + 8 = 45\\,038$."',
            'answer': True,
            'solution': 'Gồm $4$ chục nghìn, $5$ nghìn, $0$ trăm, $3$ chục, $8$ đơn vị $\\rightarrow '
                        '45\\,038$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 59: Các số có năm chữ số. Số 100 000**, quy tắc **Khai triển tổng** được xác '
                 'định bởi $\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$ và áp dụng trực tiếp vào '
                 'bài toán: “Viết số "ba mươi hai nghìn không trăm mười lăm" (gồm $5$ chữ số) và chỉ rõ chữ '
                 'số hàng chục nghìn, hàng nghìn.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khai triển tổng** ($\\overline{abcde} = a0\\,000 + '
                        'b\\,000 + c00 + d0 + e$) là kiến thức cốt lõi của Bài 59: Các số có năm chữ số. Số '
                        '100 000. Số đó viết là **$32\\,015$**, trong đó chữ số hàng chục nghìn là **$3$** '
                        'và chữ số hàng nghìn là **$2$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 59: Các số có năm chữ số. Số 100 000** để giải quyết tình huống '
                 'sau: Viết số "ba mươi hai nghìn không trăm mười lăm" (gồm $5$ chữ số) và chỉ rõ chữ số '
                 'hàng chục nghìn, hàng nghìn. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Số đó viết là **$32\\,015$**, trong đó chữ số hàng chục nghìn là **$3$** và chữ số '
                        'hàng nghìn là **$2$**.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 59: Các số có năm chữ số. Số 100 000: Số đó viết là '
                        '**$32\\,015$**, trong đó chữ số hàng chục nghìn là **$3$** và chữ số hàng nghìn là '
                        '**$2$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Viết số tự nhiên lớn nhất có năm chữ số khác nhau (không dùng dấu cách).',
            'answer': ['98765'],
            'unit': None,
            'solution': 'Chọn các chữ số lớn nhất khác nhau từ hàng chục nghìn đến hàng đơn vị: $9, 8, 7, 6, '
                        '5 \\rightarrow$ **$98765$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd11-cac-so-den-100000',
  'context_title': 'Chủ đề 11: Các số đến 100 000',
  'context': 'SGK Toán 3 · Chủ đề 11: Các số trong phạm vi 100 000.',
  'title': 'Bài 60: So sánh các số trong phạm vi 100 000',
  'icon': '⚖️',
  'description': 'So sánh hai số và sắp xếp thứ tự các số trong phạm vi 100 000.',
  'requirements': ['So sánh được hai số trong phạm vi $100\\,000$.',
                   'Xác định được số lớn nhất, số bé nhất trong nhóm $4$ số.',
                   'Sắp xếp được các số trong phạm vi $100\\,000$ theo thứ tự tăng dần hoặc giảm dần.'],
  'definition': '- Số nào có **nhiều chữ số hơn** thì lớn hơn ($100\\,000 > 99\\,999 > 9\\,999$).\n'
                '- Hai số có **cùng năm chữ số**: so sánh từng cặp chữ số ở cùng một hàng từ trái sang phải '
                '(chục nghìn $\\rightarrow$ nghìn $\\rightarrow$ trăm $\\rightarrow$ chục $\\rightarrow$ đơn '
                'vị).',
  'theory': '### 1. Quy tắc so sánh từng hàng\n'
            '- Ví dụ: $48\\,920 < 51\\,003$ vì hàng chục nghìn $4 < 5$.\n'
            '- Ví dụ: $89\\,120 > 89\\,102$ vì cùng $8$ chục nghìn, $9$ nghìn, $1$ trăm nhưng hàng chục $2 > '
            '0$.\n'
            '### 2. Tìm số lớn nhất, số bé nhất\n'
            '- So sánh hàng cao nhất trước để loại trừ nhanh các số không thỏa mãn.',
  'formulas': [{'category': 'I. Quy tắc so sánh',
                'items': [{'name': 'Khác số chữ số', 'formula': 'Số có nhiều chữ số hơn thì lớn hơn'},
                          {'name': 'Cùng năm chữ số',
                           'formula': 'So sánh: Chục nghìn $\\rightarrow$ Nghìn $\\rightarrow$ Trăm '
                                      '$\\rightarrow$ Chục $\\rightarrow$ Đơn vị'}]}],
  'example': 'Trong các số $89\\,012$; $89\\,120$; $81\\,920$; $89\\,102$, hãy tìm số lớn nhất và số bé '
             'nhất.',
  'example_answer': '- Số bé nhất là **$81\\,920$** (vì hàng nghìn $1 < 9$).\n'
                    '- Trong ba số còn lại cùng có $89$ nghìn, so sánh hàng trăm và hàng chục ta được số lớn '
                    'nhất là **$89\\,120$**.',
  'real_life': '- So sánh dân số của các xã/phường hoặc so sánh giá vé các chuyến xe.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $48\\,920 \\dots 51\\,003$ là:',
            'options': ['$>$', '$=$', 'Không xác định', '$<$'],
            'answer': 3,
            'solution': 'Hàng chục nghìn $4 < 5$ nên $48\\,920 < 51\\,003$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số lớn nhất trong các số $89\\,012$; $89\\,120$; $81\\,920$; $89\\,102$ là:',
            'options': ['$89\\,120$', '$89\\,012$', '$81\\,920$', '$89\\,102$'],
            'answer': 0,
            'solution': 'So sánh từ trái sang phải ta được **$89\\,120$** lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 60: So sánh các số trong phạm vi 100 000**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Khác số chữ số**?',
            'options': ['So sánh: Chục nghìn $\\rightarrow$ Nghìn $\\rightarrow$ Trăm $\\rightarrow$ Chục '
                        '$\\rightarrow$ Đơn vị',
                        'Số có nhiều chữ số hơn thì lớn hơn',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 60: So sánh các số trong phạm vi 100 000, '
                        '**Khác số chữ số** được xác định bởi: Số có nhiều chữ số hơn thì lớn hơn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 60: So sánh các số trong phạm vi 100 000**, nội dung/biểu thức So sánh: Chục '
                 'nghìn $\\rightarrow$ Nghìn $\\rightarrow$ Trăm $\\rightarrow$ Chục $\\rightarrow$ Đơn vị '
                 'là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khác số chữ số', 'Phân tích số', 'Cùng năm chữ số', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 60: So sánh các số trong phạm vi 100 000, biểu thức/quy tắc So sánh: Chục '
                        'nghìn $\\rightarrow$ Nghìn $\\rightarrow$ Trăm $\\rightarrow$ Chục $\\rightarrow$ '
                        'Đơn vị chính là nội dung của **Cùng năm chữ số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Dân số xã A là $12\\,876$ người, xã B là $12\\,867$ người, xã C là $13\\,002$ người. Xã '
                 'đông dân nhất là:',
            'options': ['Xã A', 'Xã B', 'Xã A và B bằng nhau', 'Xã C'],
            'answer': 3,
            'solution': 'Ta có $13\\,002 > 12\\,876 > 12\\,867$ nên **xã C** đông dân nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 60: So sánh các số trong phạm vi 100 000** (Chủ đề 11: Các số đến 100 000), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['So sánh được hai số trong phạm vi $100\\,000$.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 60: So sánh các số trong phạm vi 100 000: So sánh được '
                        'hai số trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$99\\,998 > 100\\,000$."',
            'answer': False,
            'solution': 'Số $99\\,998$ có $5$ chữ số còn $100\\,000$ có $6$ chữ số nên $99\\,998 < '
                        '100\\,000$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 60: So sánh các số trong phạm vi 100 000**, quy tắc **Khác số chữ số** được '
                 'xác định bởi Số có nhiều chữ số hơn thì lớn hơn và áp dụng trực tiếp vào bài toán: “Trong '
                 'các số $89\\,012$; $89\\,120$; $81\\,920$; $89\\,102$, hãy tìm số lớn nhất và số bé '
                 'nhất.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khác số chữ số** (Số có nhiều chữ số hơn thì lớn '
                        'hơn) là kiến thức cốt lõi của Bài 60: So sánh các số trong phạm vi 100 000. - Số bé '
                        'nhất là **$81\\,920$** (vì hàng nghìn $1 < 9$). - Trong ba số còn lại cùng có $89$ '
                        'nghìn, so sánh hàng trăm và hàng chục ta được số l...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 60: So sánh các số trong phạm vi 100 000** để giải quyết tình '
                 'huống sau: Trong các số $89\\,012$; $89\\,120$; $81\\,920$; $89\\,102$, hãy tìm số lớn '
                 'nhất và số bé nhất. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- Số bé nhất là **$81\\,920$** (vì hàng nghìn $1 < 9$). - Trong ba số còn lại cùng '
                        'có $89$ nghìn, so sánh hàng trăm và hàng chục ta được số lớn nhất là '
                        '**$89\\,120$...',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 60: So sánh các số trong phạm vi 100 000: - Số bé nhất '
                        'là **$81\\,920$** (vì hàng nghìn $1 < 9$).\n'
                        '- Trong ba số còn lại cùng có $89$ nghìn, so sánh hàng trăm và hàng chục ta được số '
                        'lớn nhất là **$89\\,120$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho bốn chữ số $0, 2, 5, 8, 9$. Hãy lập số tự nhiên nhỏ nhất có năm chữ số khác nhau từ '
                 'năm chữ số đã cho (không dùng dấu cách).',
            'answer': ['20589'],
            'unit': None,
            'solution': 'Chữ số hàng chục nghìn khác $0$ nhỏ nhất là $2$, tiếp theo lần lượt là $0, 5, 8, 9 '
                        '\\rightarrow$ **$20589$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd11-cac-so-den-100000',
  'context_title': 'Chủ đề 11: Các số đến 100 000',
  'context': 'SGK Toán 3 · Chủ đề 11: Các số trong phạm vi 100 000.',
  'title': 'Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập chung',
  'icon': '🔄',
  'description': 'Quy tắc làm tròn số đến hàng nghìn, hàng chục nghìn và vận dụng ước lượng trong phạm vi '
                 '100 000.',
  'requirements': ['Làm tròn được số đến hàng nghìn dựa vào chữ số hàng trăm.',
                   'Làm tròn được số đến hàng chục nghìn dựa vào chữ số hàng nghìn.',
                   'Vận dụng làm tròn số trong các tình huống thực tiễn.'],
  'definition': '- **Làm tròn đến hàng nghìn**: xét chữ số **hàng trăm**. Nếu chữ số hàng trăm $< 5$ thì làm '
                'tròn xuống; nếu $\\ge 5$ thì làm tròn lên.\n'
                '- **Làm tròn đến hàng chục nghìn**: xét chữ số **hàng nghìn**. Nếu chữ số hàng nghìn $< 5$ '
                'thì làm tròn xuống; nếu $\\ge 5$ thì làm tròn lên.',
  'theory': '### 1. Làm tròn số đến hàng nghìn\n'
            '- Ví dụ: $64\\,718$ có chữ số hàng trăm là $7 \\ge 5 \\rightarrow$ làm tròn lên thành '
            '$65\\,000$.\n'
            '- Ví dụ: $36\\,452$ có chữ số hàng trăm là $4 < 5 \\rightarrow$ làm tròn xuống thành '
            '$36\\,000$.\n'
            '### 2. Làm tròn số đến hàng chục nghìn\n'
            '- Ví dụ: $36\\,452$ có chữ số hàng nghìn là $6 \\ge 5 \\rightarrow$ làm tròn lên thành '
            '$40\\,000$.\n'
            '- Ví dụ: $25\\,300$ có chữ số hàng nghìn là $5 \\ge 5 \\rightarrow$ làm tròn lên thành '
            '$30\\,000$.',
  'formulas': [{'category': 'I. Quy tắc làm tròn',
                'items': [{'name': 'Đến hàng nghìn',
                           'formula': 'Nhìn chữ số hàng trăm: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                                      '\\rightarrow$ lên'},
                          {'name': 'Đến hàng chục nghìn',
                           'formula': 'Nhìn chữ số hàng nghìn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                                      '\\rightarrow$ lên'}]}],
  'example': 'Làm tròn số $72\\,680$ đến hàng nghìn và đến hàng chục nghìn.',
  'example_answer': '- Đến hàng nghìn: chữ số hàng trăm là $6 \\ge 5 \\rightarrow$ **$73\\,000$**.\n'
                    '- Đến hàng chục nghìn: chữ số hàng nghìn là $2 < 5 \\rightarrow$ **$70\\,000$**.',
  'real_life': '- Làm tròn giá vé, số lượng khán giả ở sân vận động đến hàng nghìn hoặc hàng chục nghìn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số nào dưới đây là số tròn chục nghìn?',
            'options': ['$70\\,000$', '$45\\,000$', '$70\\,500$', '$7\\,000$'],
            'answer': 0,
            'solution': 'Số **$70\\,000$** có các chữ số hàng nghìn, trăm, chục, đơn vị đều bằng $0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $64\\,718$ đến hàng nghìn ta được:',
            'options': ['$64\\,000$', '$65\\,000$', '$64\\,700$', '$60\\,000$'],
            'answer': 1,
            'solution': 'Chữ số hàng trăm là $7 \\ge 5$ nên làm tròn lên được **$65\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và '
                 'luyện tập chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Đến hàng nghìn**?',
            'options': ['Nhìn chữ số hàng nghìn: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Nhìn chữ số hàng trăm: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục '
                        'nghìn và luyện tập chung, **Đến hàng nghìn** được xác định bởi: Nhìn chữ số hàng '
                        'trăm: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập chung**, nội '
                 'dung/biểu thức Nhìn chữ số hàng nghìn: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ '
                 'lên là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Đến hàng nghìn', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Đến hàng chục nghìn'],
            'answer': 3,
            'solution': 'Trong Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập chung, '
                        'biểu thức/quy tắc Nhìn chữ số hàng nghìn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên chính là nội dung của **Đến hàng chục nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Làm tròn số $47\\,500$ đến hàng chục nghìn ta được:',
            'options': ['$50\\,000$', '$40\\,000$', '$47\\,000$', '$48\\,000$'],
            'answer': 0,
            'solution': 'Chữ số hàng nghìn là $7 \\ge 5$ nên làm tròn lên được **$50\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập chung** '
                 '(Chủ đề 11: Các số đến 100 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt '
                 'và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Làm tròn được số đến hàng nghìn dựa vào chữ số hàng trăm.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và '
                        'luyện tập chung: Làm tròn được số đến hàng nghìn dựa vào chữ số hàng trăm.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Làm tròn số $25\\,300$ đến hàng chục nghìn thì được $20\\,000$."',
            'answer': False,
            'solution': 'Chữ số hàng nghìn là $5 \\ge 5$ nên phải làm tròn lên thành $30\\,000$ '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập chung**, quy '
                 'tắc **Đến hàng nghìn** được xác định bởi Nhìn chữ số hàng trăm: $< 5 \\rightarrow$ xuống · '
                 '$\\ge 5 \\rightarrow$ lên và áp dụng trực tiếp vào bài toán: “Làm tròn số $72\\,680$ đến '
                 'hàng nghìn và đến hàng chục nghìn.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đến hàng nghìn** (Nhìn chữ số hàng trăm: $< 5 '
                        '\\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên) là kiến thức cốt lõi của Bài 61, '
                        '62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập chung. - Đến hàng '
                        'nghìn: chữ số hàng trăm là $6 \\ge 5 \\rightarrow$ **$73\\,000$**. - Đến hàng chục '
                        'nghìn: chữ số hàng nghìn là $2 < 5 \\rightarrow$ *...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và luyện tập '
                 'chung** để giải quyết tình huống sau: Làm tròn số $72\\,680$ đến hàng nghìn và đến hàng '
                 'chục nghìn. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        '- Đến hàng nghìn: chữ số hàng trăm là $6 \\ge 5 \\rightarrow$ **$73\\,000$**. - Đến '
                        'hàng chục nghìn: chữ số hàng nghìn là $2 < 5 \\rightarrow$ **$70\\,000$**.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 61, 62: Làm tròn số đến hàng nghìn, hàng chục nghìn và '
                        'luyện tập chung: - Đến hàng nghìn: chữ số hàng trăm là $6 \\ge 5 \\rightarrow$ '
                        '**$73\\,000$**.\n'
                        '- Đến hàng chục nghìn: chữ số hàng nghìn là $2 < 5 \\rightarrow$ **$70\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một chiếc áo sơ mi có giá $86\\,500$ đồng. Nếu làm tròn giá tiền chiếc áo đến hàng nghìn '
                 'thì cần khoảng bao nhiêu nghìn đồng (chỉ viết số, ví dụ 80000)?',
            'answer': ['87000'],
            'unit': None,
            'solution': 'Chữ số hàng trăm là $5 \\ge 5$ nên làm tròn số $86\\,500$ đến hàng nghìn ta được '
                        '**$87000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd12-cong-tru-pham-vi-100000',
  'context_title': 'Chủ đề 12: Cộng, trừ trong phạm vi 100 000',
  'context': 'SGK Toán 3 · Chủ đề 12: Phép cộng, phép trừ trong phạm vi 100 000.',
  'title': 'Bài 63: Phép cộng trong phạm vi 100 000',
  'icon': '➕',
  'description': 'Đặt tính và thực hiện phép cộng các số trong phạm vi 100 000; tính nhẩm các số tròn chục '
                 'nghìn.',
  'requirements': ['Đặt tính và tính đúng phép cộng các số có đến năm chữ số trong phạm vi $100\\,000$.',
                   'Cộng nhẩm được các số tròn nghìn, tròn chục nghìn.',
                   'Giải được bài toán có lời văn liên quan đến phép cộng trong phạm vi $100\\,000$.'],
  'definition': '- Đặt tính phép cộng $a + b$ sao cho các chữ số cùng hàng thẳng cột với nhau (đơn vị, chục, '
                'trăm, nghìn, chục nghìn).\n'
                '- Thực hiện cộng từ phải sang trái, nhớ $1$ sang hàng liền trước khi tổng một hàng $\\ge '
                '10$.',
  'theory': '### 1. Cộng nhẩm các số tròn chục nghìn\n'
            '- Ví dụ: $60\\,000 + 30\\,000 = 90\\,000$ ($6$ chục nghìn $+ 3$ chục nghìn $= 9$ chục nghìn).\n'
            '### 2. Đặt tính rồi tính\n'
            '- Ví dụ: $35\\,248 + 41\\,637 = 76\\,885$ ($8+7=15$ viết $5$ nhớ $1$; $4+3+1=8$; $2+6=8$; '
            '$5+1=6$; $3+4=7$).',
  'formulas': [{'category': 'I. Phép cộng phạm vi 100 000',
                'items': [{'name': 'Đặt tính', 'formula': 'Thẳng cột theo hàng · Cộng từ phải sang trái'},
                          {'name': 'Nhẩm tròn chục nghìn',
                           'formula': '$a0\\,000 + b0\\,000 = (a + b)0\\,000$'}]}],
  'example': 'Đặt tính rồi tính: $23\\,415 + 51\\,302$ và $47\\,280 + 36\\,450$.',
  'example_answer': '- $23\\,415 + 51\\,302 = 74\\,717$.\n'
                    '- $47\\,280 + 36\\,450 = 83\\,730$ (nhớ $1$ từ hàng chục sang trăm và nhớ $1$ từ hàng '
                    'nghìn sang chục nghìn).',
  'real_life': '- Tính tổng số tiền mua quần áo và sách vở đầu năm học; tổng số cây trồng của hai lâm '
               'trường.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $60\\,000 + 30\\,000 = ?$',
            'options': ['$9\\,000$', '$90\\,000$', '$900\\,000$', '$30\\,000$'],
            'answer': 1,
            'solution': '$6$ chục nghìn $+ 3$ chục nghìn $= 90\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $23\\,415 + 51\\,302$ là:',
            'options': ['$74\\,727$', '$72\\,717$', '$74\\,717$', '$28\\,113$'],
            'answer': 2,
            'solution': 'Cộng từng hàng: $23\\,415 + 51\\,302 = 74\\,717$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 63: Phép cộng trong phạm vi 100 000**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Đặt tính**?',
            'options': ['$a0\\,000 + b0\\,000 = (a + b)0\\,000$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Thẳng cột theo hàng · Cộng từ phải sang trái'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 63: Phép cộng trong phạm vi 100 000, **Đặt '
                        'tính** được xác định bởi: Thẳng cột theo hàng · Cộng từ phải sang trái.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 63: Phép cộng trong phạm vi 100 000**, nội dung/biểu thức $a0\\,000 + b0\\,000 '
                 '= (a + b)0\\,000$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Nhẩm tròn chục nghìn', 'Đặt tính', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 63: Phép cộng trong phạm vi 100 000, biểu thức/quy tắc $a0\\,000 + '
                        'b0\\,000 = (a + b)0\\,000$ chính là nội dung của **Nhẩm tròn chục nghìn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng của $47\\,280$ và $36\\,450$ là:',
            'options': ['$73\\,730$', '$83\\,730$', '$83\\,630$', '$82\\,730$'],
            'answer': 1,
            'solution': 'Chú ý nhớ $1$ ở hàng nghìn ($7 + 6 = 13$) sang hàng chục nghìn: $4 + 3 + 1 = 8 '
                        '\\rightarrow 83\\,730$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 63: Phép cộng trong phạm vi 100 000** (Chủ đề 12: Cộng, trừ trong phạm vi '
                 '100 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đặt tính và tính đúng phép cộng các số có đến năm chữ số trong phạm vi $100\\,000$.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 63: Phép cộng trong phạm vi 100 000: Đặt tính và tính '
                        'đúng phép cộng các số có đến năm chữ số trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tổng của số lớn nhất có bốn chữ số và $1$ là $100\\,000$."',
            'answer': False,
            'solution': 'Số lớn nhất có bốn chữ số là $9\\,999$, cộng $1$ bằng $10\\,000$, không phải '
                        '$100\\,000$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 63: Phép cộng trong phạm vi 100 000**, quy tắc **Đặt tính** được xác định bởi '
                 'Thẳng cột theo hàng · Cộng từ phải sang trái và áp dụng trực tiếp vào bài toán: “Đặt tính '
                 'rồi tính: $23\\,415 + 51\\,302$ và $47\\,280 + 36\\,450$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đặt tính** (Thẳng cột theo hàng · Cộng từ phải sang '
                        'trái) là kiến thức cốt lõi của Bài 63: Phép cộng trong phạm vi 100 000. - $23\\,415 '
                        '+ 51\\,302 = 74\\,717$. - $47\\,280 + 36\\,450 = 83\\,730$ (nhớ $1$ từ hàng chục '
                        'sang trăm và nhớ $1$ từ hàng nghìn sang chục nghìn).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 63: Phép cộng trong phạm vi 100 000** để giải quyết tình huống '
                 'sau: Đặt tính rồi tính: $23\\,415 + 51\\,302$ và $47\\,280 + 36\\,450$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        '- $23\\,415 + 51\\,302 = 74\\,717$. - $47\\,280 + 36\\,450 = 83\\,730$ (nhớ $1$ từ '
                        'hàng chục sang trăm và nhớ $1$ từ hàng nghìn sang chục nghìn).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 63: Phép cộng trong phạm vi 100 000: - $23\\,415 + '
                        '51\\,302 = 74\\,717$.\n'
                        '- $47\\,280 + 36\\,450 = 83\\,730$ (nhớ $1$ từ hàng chục sang trăm và nhớ $1$ từ '
                        'hàng nghìn sang chục nghìn).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mẹ mua một chiếc cặp sách giá $55\\,000$ đồng và một hộp bút màu giá $32\\,000$ đồng. Hỏi '
                 'mẹ phải trả tất cả bao nhiêu đồng (viết liền không dấu cách)?',
            'answer': ['87000'],
            'unit': 'đồng',
            'solution': 'Tổng số tiền mẹ phải trả là: $55\\,000 + 32\\,000 = 87\\,000\\text{ (đồng)}$.\n'
                        'Đáp số: **$87000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd12-cong-tru-pham-vi-100000',
  'context_title': 'Chủ đề 12: Cộng, trừ trong phạm vi 100 000',
  'context': 'SGK Toán 3 · Chủ đề 12: Phép cộng, phép trừ trong phạm vi 100 000.',
  'title': 'Bài 64: Phép trừ trong phạm vi 100 000',
  'icon': '➖',
  'description': 'Đặt tính và thực hiện phép trừ các số trong phạm vi 100 000; trừ nhẩm các số tròn chục '
                 'nghìn.',
  'requirements': ['Đặt tính và tính đúng phép trừ các số có đến năm chữ số trong phạm vi $100\\,000$.',
                   'Trừ nhẩm được các số tròn chục nghìn, tròn nghìn.',
                   'Tìm được thành phần chưa biết và giải bài toán thực tế có phép trừ.'],
  'definition': '- Đặt tính phép trừ $a - b$ sao cho các chữ số cùng hàng thẳng cột.\n'
                '- Thực hiện trừ lần lượt từ phải sang trái (từ hàng đơn vị đến hàng chục nghìn), mượn $10$ '
                'và nhớ $1$ sang hàng liền trước khi cần.',
  'theory': '### 1. Trừ nhẩm số tròn chục nghìn\n'
            '- Ví dụ: $80\\,000 - 50\\,000 = 30\\,000$ ($8$ chục nghìn $- 5$ chục nghìn $= 3$ chục nghìn).\n'
            '### 2. Đặt tính rồi tính\n'
            '- Ví dụ: $85\\,372 - 26\\,145 = 59\\,227$.\n'
            '- Ví dụ: $62\\,548 - 27\\,316 = 35\\,232$.',
  'formulas': [{'category': 'I. Phép trừ phạm vi 100 000',
                'items': [{'name': 'Nhẩm tròn chục nghìn',
                           'formula': '$a0\\,000 - b0\\,000 = (a - b)0\\,000$'},
                          {'name': 'Quan hệ cộng – trừ',
                           'formula': '$a + b = c \\Rightarrow c - a = b \\text{ và } c - b = a$'}]}],
  'example': 'Tìm $x$ biết: $x + 25\\,600 = 70\\,000$.',
  'example_answer': 'Muốn tìm số hạng chưa biết, ta lấy tổng trừ đi số hạng kia:\n'
                    '$x = 70\\,000 - 25\\,600 = 44\\,400$.',
  'real_life': '- Tính số tiền thừa khi đưa tờ $100\\,000$ đồng để mua hàng; tính lượng hàng tồn kho.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $80\\,000 - 50\\,000 = ?$',
            'options': ['$3\\,000$', '$130\\,000$', '$30\\,000$', '$35\\,000$'],
            'answer': 2,
            'solution': '$8$ chục nghìn $- 5$ chục nghìn $= 30\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $62\\,548 - 27\\,316$ là:',
            'options': ['$35\\,332$', '$45\\,232$', '$35\\,222$', '$35\\,232$'],
            'answer': 3,
            'solution': 'Trừ từng hàng: $62\\,548 - 27\\,316 = 35\\,232$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 64: Phép trừ trong phạm vi 100 000**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Nhẩm tròn chục nghìn**?',
            'options': ['$a0\\,000 - b0\\,000 = (a - b)0\\,000$',
                        '$a + b = c \\Rightarrow c - a = b \\text{ và } c - b = a$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 64: Phép trừ trong phạm vi 100 000, **Nhẩm '
                        'tròn chục nghìn** được xác định bởi: $a0\\,000 - b0\\,000 = (a - b)0\\,000$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 64: Phép trừ trong phạm vi 100 000**, nội dung/biểu thức $a + b = c '
                 '\\Rightarrow c - a = b \\text{ và } c - b = a$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Nhẩm tròn chục nghìn',
                        'Quan hệ cộng – trừ',
                        'Phân tích số',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 64: Phép trừ trong phạm vi 100 000, biểu thức/quy tắc $a + b = c '
                        '\\Rightarrow c - a = b \\text{ và } c - b = a$ chính là nội dung của **Quan hệ cộng '
                        '– trừ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x + 25\\,600 = 70\\,000$:',
            'options': ['$95\\,600$', '$45\\,400$', '$44\\,400$', '$54\\,400$'],
            'answer': 2,
            'solution': 'Ta có $x = 70\\,000 - 25\\,600 = 44\\,400$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 64: Phép trừ trong phạm vi 100 000** (Chủ đề 12: Cộng, trừ trong phạm vi 100 '
                 '000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Đặt tính và tính đúng phép trừ các số có đến năm chữ số trong phạm vi $100\\,000$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 64: Phép trừ trong phạm vi 100 000: Đặt tính và tính '
                        'đúng phép trừ các số có đến năm chữ số trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hiệu của $94\\,600$ và $32\\,400$ bằng $62\\,200$."',
            'answer': True,
            'solution': 'Ta có $94\\,600 - 32\\,400 = 62\\,200$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 64: Phép trừ trong phạm vi 100 000**, quy tắc **Nhẩm tròn chục nghìn** được '
                 'xác định bởi $a0\\,000 - b0\\,000 = (a - b)0\\,000$ và áp dụng trực tiếp vào bài toán: '
                 '“Tìm $x$ biết: $x + 25\\,600 = 70\\,000$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhẩm tròn chục nghìn** ($a0\\,000 - b0\\,000 = (a - '
                        'b)0\\,000$) là kiến thức cốt lõi của Bài 64: Phép trừ trong phạm vi 100 000. Muốn '
                        'tìm số hạng chưa biết, ta lấy tổng trừ đi số hạng kia: $x = 70\\,000 - 25\\,600 = '
                        '44\\,400$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 64: Phép trừ trong phạm vi 100 000** để giải quyết tình huống '
                 'sau: Tìm $x$ biết: $x + 25\\,600 = 70\\,000$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Muốn tìm số hạng chưa biết, ta lấy tổng trừ đi số hạng kia: $x = 70\\,000 - '
                        '25\\,600 = 44\\,400$.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 64: Phép trừ trong phạm vi 100 000: Muốn tìm số hạng '
                        'chưa biết, ta lấy tổng trừ đi số hạng kia:\n'
                        '$x = 70\\,000 - 25\\,600 = 44\\,400$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một quãng đường dài $45\\,000\\text{ m}$, người ta đã trải nhựa được $28\\,500\\text{ m}$. '
                 'Hỏi còn lại bao nhiêu mét đường chưa trải nhựa (viết số liền)?',
            'answer': ['16500'],
            'unit': 'm',
            'solution': 'Quãng đường chưa trải nhựa dài: $45\\,000 - 28\\,500 = 16\\,500\\text{ (m)}$.\n'
                        'Đáp số: **$16500$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd12-cong-tru-pham-vi-100000',
  'context_title': 'Chủ đề 12: Cộng, trừ trong phạm vi 100 000',
  'context': 'SGK Toán 3 · Chủ đề 12: Phép cộng, phép trừ trong phạm vi 100 000.',
  'title': 'Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000',
  'icon': '🧠',
  'description': 'Vận dụng tính chất giao hoán, kết hợp của phép cộng để tính thuận tiện và giải toán hai '
                 'bước tính.',
  'requirements': ['Nhận biết và vận dụng được tính chất giao hoán, kết hợp của phép cộng để nhóm các số '
                   'tròn nghìn, tròn chục nghìn.',
                   'Tính đúng giá trị biểu thức có phép cộng và phép trừ trong phạm vi $100\\,000$.',
                   'Giải được bài toán thực tế có hai bước tính cộng, trừ trong phạm vi $100\\,000$.'],
  'definition': '- **Tính chất giao hoán**: khi đổi chỗ các số hạng trong một tổng thì tổng không thay đổi '
                '($a + b = b + a$).\n'
                '- **Tính chất kết hợp**: khi cộng một tổng hai số với số thứ ba, ta có thể cộng số thứ nhất '
                'với tổng của số thứ hai và số thứ ba ($(a + b) + c = a + (b + c)$).',
  'theory': '### 1. Tính bằng cách thuận tiện nhất\n'
            '- Ghép các số hạng có tổng là số tròn nghìn hoặc tròn chục nghìn.\n'
            '- Ví dụ: $4\\,600 + 2\\,700 + 5\\,400 = (4\\,600 + 5\\,400) + 2\\,700 = 10\\,000 + 2\\,700 = '
            '12\\,700$.\n'
            '### 2. Bài toán hai bước tính\n'
            '- Có thể tính tổng số đã bán/đã xuất rồi lấy số ban đầu trừ đi tổng đó.',
  'formulas': [{'category': 'I. Tính chất phép cộng',
                'items': [{'name': 'Giao hoán', 'formula': '$a + b = b + a$'},
                          {'name': 'Kết hợp', 'formula': '$(a + b) + c = a + (b + c)$'}]}],
  'example': 'Mẹ mang $100\\,000$ đồng đi chợ, mua thịt hết $45\\,000$ đồng và mua rau hết $12\\,000$ đồng. '
             'Hỏi mẹ còn lại bao nhiêu tiền?',
  'example_answer': 'Số tiền mẹ đã mua thịt và rau là: $45\\,000 + 12\\,000 = 57\\,000\\text{ (đồng)}$.\n'
                    'Số tiền mẹ còn lại là: $100\\,000 - 57\\,000 = 43\\,000\\text{ (đồng)}$.',
  'real_life': '- Tính nhẩm nhanh tổng hóa đơn siêu thị bằng cách ghép các khoản tiền tròn chục nghìn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính chất $a + b = b + a$ của phép cộng được gọi là:',
            'options': ['Tính chất kết hợp',
                        'Tính chất phân phối',
                        'Quy tắc tìm số hạng',
                        'Tính chất giao hoán'],
            'answer': 3,
            'solution': 'Đổi chỗ các số hạng mà tổng không đổi là **tính chất giao hoán**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhanh biểu thức $2\\,500 + 1\\,300 + 7\\,500$ ta được:',
            'options': ['$11\\,300$', '$10\\,300$', '$9\\,800$', '$12\\,300$'],
            'answer': 0,
            'solution': 'Nhóm $(2\\,500 + 7\\,500) + 1\\,300 = 10\\,000 + 1\\,300 = 11\\,300$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Giao hoán**?',
            'options': ['$(a + b) + c = a + (b + c)$',
                        '$a + b = b + a$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 65: Luyện tập chung cộng, trừ trong phạm vi '
                        '100 000, **Giao hoán** được xác định bởi: $a + b = b + a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000**, nội dung/biểu thức $(a '
                 '+ b) + c = a + (b + c)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Giao hoán', 'Phân tích số', 'Kết hợp', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000, biểu thức/quy tắc '
                        '$(a + b) + c = a + (b + c)$ chính là nội dung của **Kết hợp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mẹ có $100\\,000$ đồng, mua thịt hết $45\\,000$ đồng và mua rau hết $12\\,000$ đồng. Số '
                 'tiền mẹ còn lại là:',
            'options': ['$57\\,000$ đồng', '$33\\,000$ đồng', '$53\\,000$ đồng', '$43\\,000$ đồng'],
            'answer': 3,
            'solution': 'Đã mua: $45\\,000 + 12\\,000 = 57\\,000$ đồng. Còn lại: $100\\,000 - 57\\,000 = '
                        '43\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000** (Chủ đề 12: Cộng, trừ '
                 'trong phạm vi 100 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết và vận dụng được tính chất giao hoán, kết hợp của phép cộng để nhóm các '
                        'số tròn nghìn, tròn chục nghìn.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000: '
                        'Nhận biết và vận dụng được tính chất giao hoán, kết hợp của phép cộng để nhóm các '
                        'số tròn nghìn, tròn chục nghìn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $1\\,800 + 3\\,500 + 200$ bằng $5\\,500$."',
            'answer': True,
            'solution': 'Ta có $(1\\,800 + 200) + 3\\,500 = 2\\,000 + 3\\,500 = 5\\,500$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000**, quy tắc **Giao hoán** '
                 'được xác định bởi $a + b = b + a$ và áp dụng trực tiếp vào bài toán: “Mẹ mang $100\\,000$ '
                 'đồng đi chợ, mua thịt hết $45\\,000$ đồng và mua rau hết $12\\,000$ đồng. Hỏi mẹ còn lại '
                 'bao nhiêu tiền?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Giao hoán** ($a + b = b + a$) là kiến thức cốt lõi '
                        'của Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000. Số tiền mẹ đã mua thịt '
                        'và rau là: $45\\,000 + 12\\,000 = 57\\,000\\text{ (đồng)}$. Số tiền mẹ còn lại là: '
                        '$100\\,000 - 57\\,000 = 43\\,000\\text{ (đồng)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000** để giải '
                 'quyết tình huống sau: Mẹ mang $100\\,000$ đồng đi chợ, mua thịt hết $45\\,000$ đồng và mua '
                 'rau hết $12\\,000$ đồng. Hỏi mẹ còn lại bao nhiêu tiền? Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Số tiền mẹ đã mua thịt và rau là: $45\\,000 + 12\\,000 = 57\\,000\\text{ (đồng)}$. '
                        'Số tiền mẹ còn lại là: $100\\,000 - 57\\,000 = 43\\,000\\text{ (đồng)}$.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 65: Luyện tập chung cộng, trừ trong phạm vi 100 000: Số '
                        'tiền mẹ đã mua thịt và rau là: $45\\,000 + 12\\,000 = 57\\,000\\text{ (đồng)}$.\n'
                        'Số tiền mẹ còn lại là: $100\\,000 - 57\\,000 = 43\\,000\\text{ (đồng)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một kho có $35\\,750\\text{ kg}$ thóc. Lần đầu người ta xuất $12\\,500\\text{ kg}$, lần '
                 'sau xuất $8\\,250\\text{ kg}$. Hỏi trong kho còn lại bao nhiêu ki-lô-gam thóc (viết số '
                 'liền)?',
            'answer': ['15000'],
            'unit': 'kg',
            'solution': 'Đã xuất: $12\\,500 + 8\\,250 = 20\\,750\\text{ (kg)}$. Còn lại: $35\\,750 - '
                        '20\\,750 = 15\\,000\\text{ (kg)}$.\n'
                        'Đáp số: **$15000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd13-dong-ho-thang-nam-tien',
  'context_title': 'Chủ đề 13: Xem đồng hồ. Tháng – năm. Tiền Việt Nam',
  'context': 'SGK Toán 3 · Chủ đề 13: Xem đồng hồ, tháng – năm và tiền Việt Nam.',
  'title': 'Bài 66: Xem đồng hồ. Tháng – năm',
  'icon': '🕰️',
  'description': 'Đọc giờ chính xác đến 5 phút và từng phút trên đồng hồ (cách đọc giờ hơn, giờ kém); các '
                 'tháng trong năm.',
  'requirements': ['Đọc được giờ trên đồng hồ chính xác đến $5$ phút và từng phút (cả cách đọc giờ hơn và '
                   'giờ kém).',
                   'Biết một năm có $12$ tháng và nhớ chính xác số ngày của từng tháng ($30$, $31$, $28$ '
                   'hoặc $29$ ngày).',
                   'Tính được khoảng thời gian diễn ra một hoạt động.'],
  'definition': '- **Đồng hồ**: $1\\text{ giờ} = 60\\text{ phút}$. Kim phút đi từ số này sang số kế tiếp là '
                '$5$ phút, đi từ vạch nhỏ này sang vạch nhỏ kế tiếp là $1$ phút. Khi số phút lớn hơn $30$, '
                'ta có thể đọc theo **giờ kém** (ví dụ $8$ giờ $45$ phút $= 9$ giờ kém $15$ phút).\n'
                '- **Tháng – năm**: Một năm có **$12$ tháng**. Các tháng có **$31$ ngày** là: tháng $1, 3, '
                '5, 7, 8, 10, 12$. Các tháng có **$30$ ngày** là: tháng $4, 6, 9, 11$. Riêng **tháng $2$** '
                'có $28$ hoặc $29$ ngày.',
  'theory': '### 1. Xem đồng hồ đến từng phút\n'
            '- Nếu kim phút chỉ quá số $4$ thêm $2$ vạch nhỏ thì số phút là $5 \\times 4 + 2 = 22$ phút.\n'
            '- Đổi giờ hơn sang giờ kém: Lấy $60$ trừ đi số phút hiện tại, đồng thời tăng giờ thêm $1$.\n'
            '### 2. Mẹo nhớ số ngày trong tháng bằng nắm bàn tay\n'
            '- Đếm lần lượt từ tháng $1$ đến tháng $12$ trên các khớp xương lồi và chỗ lõm của nắm tay: '
            'tháng rơi vào khớp lồi có $31$ ngày, rơi vào chỗ lõm có $30$ ngày (trừ tháng $2$).',
  'formulas': [{'category': 'I. Quan hệ thời gian',
                'items': [{'name': 'Giờ và phút',
                           'formula': '$1\\text{ giờ} = 60\\text{ phút}$ · Giờ kém: $(h + 1)\\text{ giờ kém '
                                      '} (60 - m)\\text{ phút}$'},
                          {'name': 'Số ngày trong tháng',
                           'formula': 'Tháng $31$ ngày: $1, 3, 5, 7, 8, 10, 12$ · Tháng $30$ ngày: $4, 6, 9, '
                                      '11$ · Tháng $2$: $28$ hoặc $29$ ngày'}]}],
  'example': 'Một bộ phim bắt đầu lúc $7$ giờ $15$ phút và kéo dài trong $50$ phút. Hỏi bộ phim kết thúc lúc '
             'mấy giờ?',
  'example_answer': 'Ta có: $7$ giờ $15$ phút $+ 50$ phút $= 7$ giờ $65$ phút.\n'
                    'Vì $60$ phút $= 1$ giờ nên $7$ giờ $65$ phút $= 8$ giờ $5$ phút.',
  'real_life': '- Xem đồng hồ để đi học đúng giờ; nhớ số ngày của tháng để lên lịch học tập.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một năm có bao nhiêu tháng và tháng nào dưới đây có $30$ ngày?',
            'options': ['$12$ tháng; Tháng $4$',
                        '$12$ tháng; Tháng $1$',
                        '$10$ tháng; Tháng $8$',
                        '$12$ tháng; Tháng $12$'],
            'answer': 0,
            'solution': 'Một năm có **$12$ tháng** và các tháng $4, 6, 9, 11$ có $30$ ngày.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi kim phút chỉ đúng vào số $6$ trên mặt đồng hồ thì ứng với bao nhiêu phút?',
            'options': ['$6$ phút', '$30$ phút', '$60$ phút', '$15$ phút'],
            'answer': 1,
            'solution': 'Ta có $5 \\times 6 = 30\\text{ (phút)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 66: Xem đồng hồ. Tháng – năm**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Giờ và phút**?',
            'options': ['Tháng $31$ ngày: $1, 3, 5, 7, 8, 10, 12$ · Tháng $30$ ngày: $4, 6, 9, 11$ · Tháng '
                        '$2$: $28$ hoặc $29$ ngày',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$1\\text{ giờ} = 60\\text{ phút}$ · Giờ kém: $(h + 1)\\text{ giờ kém } (60 - '
                        'm)\\text{ phút}$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 66: Xem đồng hồ. Tháng – năm, **Giờ và phút** '
                        'được xác định bởi: $1\\text{ giờ} = 60\\text{ phút}$ · Giờ kém: $(h + 1)\\text{ giờ '
                        'kém } (60 - m)\\text{ phút}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 66: Xem đồng hồ. Tháng – năm**, nội dung/biểu thức Tháng $31$ ngày: $1, 3, 5, '
                 '7, 8, 10, 12$ · Tháng $30$ ngày: $4, 6, 9, 11$ · Tháng $2$: $28$ hoặc $29$ ngày là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Giờ và phút', 'Phân tích số', 'Số tròn trăm, tròn nghìn', 'Số ngày trong tháng'],
            'answer': 3,
            'solution': 'Trong Bài 66: Xem đồng hồ. Tháng – năm, biểu thức/quy tắc Tháng $31$ ngày: $1, 3, '
                        '5, 7, 8, 10, 12$ · Tháng $30$ ngày: $4, 6, 9, 11$ · Tháng $2$: $28$ hoặc $29$ ngày '
                        'chính là nội dung của **Số ngày trong tháng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': '$8$ giờ $50$ phút còn được đọc là:',
            'options': ['$9$ giờ kém $10$ phút',
                        '$8$ giờ kém $10$ phút',
                        '$9$ giờ $10$ phút',
                        '$10$ giờ kém $50$ phút'],
            'answer': 0,
            'solution': 'Còn $60 - 50 = 10$ phút nữa là đến $9$ giờ $\\rightarrow$ **$9$ giờ kém $10$ '
                        'phút**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 66: Xem đồng hồ. Tháng – năm** (Chủ đề 13: Xem đồng hồ. Tháng – năm. Tiền '
                 'Việt Nam), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Đọc được giờ trên đồng hồ chính xác đến $5$ phút và từng phút (cả cách đọc giờ hơn '
                        'và giờ kém).',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 66: Xem đồng hồ. Tháng – năm: Đọc được giờ trên đồng '
                        'hồ chính xác đến $5$ phút và từng phút (cả cách đọc giờ hơn và giờ kém).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tháng $2$ năm nào cũng có đúng $30$ ngày."',
            'answer': False,
            'solution': 'Tháng $2$ chỉ có $28$ hoặc $29$ ngày $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 66: Xem đồng hồ. Tháng – năm**, quy tắc **Giờ và phút** được xác định bởi '
                 '$1\\text{ giờ} = 60\\text{ phút}$ · Giờ kém: $(h + 1)\\text{ giờ kém } (60 - m)\\text{ '
                 'phút}$ và áp dụng trực tiếp vào bài toán: “Một bộ phim bắt đầu lúc $7$ giờ $15$ phút và '
                 'kéo dài trong $50$ phút. Hỏi bộ phim kết thúc lúc mấy giờ?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Giờ và phút** ($1\\text{ giờ} = 60\\text{ phút}$ · '
                        'Giờ kém: $(h + 1)\\text{ giờ kém } (60 - m)\\text{ phút}$) là kiến thức cốt lõi của '
                        'Bài 66: Xem đồng hồ. Tháng – năm. Ta có: $7$ giờ $15$ phút $+ 50$ phút $= 7$ giờ '
                        '$65$ phút. Vì $60$ phút $= 1$ giờ nên $7$ giờ $65$ phút $= 8$ giờ $5$ phút.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 66: Xem đồng hồ. Tháng – năm** để giải quyết tình huống sau: Một '
                 'bộ phim bắt đầu lúc $7$ giờ $15$ phút và kéo dài trong $50$ phút. Hỏi bộ phim kết thúc lúc '
                 'mấy giờ? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Ta có: $7$ giờ $15$ phút $+ 50$ phút $= 7$ giờ $65$ phút. Vì $60$ phút $= 1$ giờ '
                        'nên $7$ giờ $65$ phút $= 8$ giờ $5$ phút.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 66: Xem đồng hồ. Tháng – năm: Ta có: $7$ giờ $15$ phút '
                        '$+ 50$ phút $= 7$ giờ $65$ phút.\n'
                        'Vì $60$ phút $= 1$ giờ nên $7$ giờ $65$ phút $= 8$ giờ $5$ phút.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bạn Minh bắt đầu làm bài lúc $19$ giờ $20$ phút và làm xong lúc $20$ giờ $5$ phút. Hỏi '
                 'Minh đã làm bài trong bao nhiêu phút?',
            'answer': ['45'],
            'unit': 'phút',
            'solution': 'Từ $19$ giờ $20$ phút đến $20$ giờ là $40$ phút, cộng thêm $5$ phút bằng $45$ '
                        'phút.\n'
                        'Đáp số: **$45\\text{ phút}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd13-dong-ho-thang-nam-tien',
  'context_title': 'Chủ đề 13: Xem đồng hồ. Tháng – năm. Tiền Việt Nam',
  'context': 'SGK Toán 3 · Chủ đề 13: Xem đồng hồ, tháng – năm và tiền Việt Nam.',
  'title': 'Bài 67: Thực hành xem đồng hồ, xem lịch',
  'icon': '📅',
  'description': 'Thực hành đọc giờ trên đồng hồ kim, đồng hồ điện tử và tra cứu ngày, thứ trên tờ lịch '
                 'tháng.',
  'requirements': ['Đọc và liên hệ được giờ giữa đồng hồ kim và đồng hồ điện tử ($24$ giờ).',
                   'Xem được tờ lịch tháng để biết một ngày là thứ mấy, ngày đầu tháng, ngày cuối tháng.',
                   'Tính được thứ và ngày cách nhau $1$ tuần ($7$ ngày) hoặc qua tháng kế tiếp.'],
  'definition': '- **Một tuần lễ** có **$7$ ngày** (từ thứ Hai đến Chủ nhật). Hai ngày cùng thứ ở hai tuần '
                'liên tiếp cách nhau đúng **$7$ ngày**.\n'
                '- Khi tính ngày bước sang tháng mới, cần chú ý tháng hiện tại có $30$ hay $31$ ngày (hoặc '
                '$28, 29$ ngày với tháng $2$).',
  'theory': '### 1. Xem lịch tháng\n'
            '- Nếu ngày $5$ là thứ Tư thì thứ Tư tuần tiếp theo là ngày $5 + 7 = 12$.\n'
            '- Nếu ngày $28$ tháng $3$ là thứ Hai: vì tháng $3$ có $31$ ngày nên thứ Hai tuần kế tiếp là '
            'ngày $28 + 7 - 31 = 4$ (ngày $4$ tháng $4$).\n'
            '### 2. Thực hành xem đồng hồ\n'
            '- Buổi chiều/tối trên đồng hồ $24$ giờ: $13\\text{ giờ} = 1\\text{ giờ chiều}$, $19\\text{ giờ} '
            '= 7\\text{ giờ tối}$.',
  'formulas': [{'category': 'I. Quy tắc tính lịch',
                'items': [{'name': 'Cùng thứ tuần sau',
                           'formula': '$\\text{Ngày mới} = \\text{Ngày cũ} + 7$'},
                          {'name': 'Qua tháng mới',
                           'formula': 'Lấy $(\\text{Ngày cũ} + 7) - \\text{Số ngày của tháng hiện tại}$'}]}],
  'example': 'Ngày $28$ tháng $3$ là thứ Hai. Hỏi ngày $4$ tháng $4$ cùng năm đó là thứ mấy?',
  'example_answer': 'Tháng $3$ có $31$ ngày. Từ ngày $28$ tháng $3$ đến ngày $4$ tháng $4$ có số ngày là: '
                    '$(31 - 28) + 4 = 7\\text{ (ngày)} = 1\\text{ tuần}$.\n'
                    'Vậy ngày $4$ tháng $4$ cũng là **thứ Hai**.',
  'real_life': '- Xem lịch để biết ngày sinh nhật rơi vào thứ mấy; xem giờ tàu chạy trên vé tàu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một tuần lễ có tất cả bao nhiêu ngày?',
            'options': ['$5$ ngày', '$7$ ngày', '$6$ ngày', '$10$ ngày'],
            'answer': 1,
            'solution': 'Một tuần lễ có **$7$ ngày**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tháng $7$ và tháng $8$ mỗi tháng có bao nhiêu ngày?',
            'options': ['Tháng $7$ có $31$ ngày, tháng $8$ có $30$ ngày',
                        'Cả hai tháng đều có $30$ ngày',
                        'Cả hai tháng đều có $31$ ngày',
                        'Tháng $7$ có $30$ ngày, tháng $8$ có $31$ ngày'],
            'answer': 2,
            'solution': 'Hai tháng $7$ và $8$ liên tiếp đều có **$31$ ngày**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 67: Thực hành xem đồng hồ, xem lịch**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Cùng thứ tuần sau**?',
            'options': ['Lấy $(\\text{Ngày cũ} + 7) - \\text{Số ngày của tháng hiện tại}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$\\text{Ngày mới} = \\text{Ngày cũ} + 7$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 67: Thực hành xem đồng hồ, xem lịch, **Cùng '
                        'thứ tuần sau** được xác định bởi: $\\text{Ngày mới} = \\text{Ngày cũ} + 7$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 67: Thực hành xem đồng hồ, xem lịch**, nội dung/biểu thức Lấy $(\\text{Ngày '
                 'cũ} + 7) - \\text{Số ngày của tháng hiện tại}$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Qua tháng mới', 'Cùng thứ tuần sau', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 67: Thực hành xem đồng hồ, xem lịch, biểu thức/quy tắc Lấy $(\\text{Ngày '
                        'cũ} + 7) - \\text{Số ngày của tháng hiện tại}$ chính là nội dung của **Qua tháng '
                        'mới**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nếu ngày $10$ tháng $5$ là Chủ nhật thì Chủ nhật tuần tiếp theo là ngày mấy tháng $5$?',
            'options': ['Ngày $16$', 'Ngày $17$', 'Ngày $18$', 'Ngày $20$'],
            'answer': 1,
            'solution': 'Cộng thêm $7$ ngày: $10 + 7 = 17$ (ngày $17$ tháng $5$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 67: Thực hành xem đồng hồ, xem lịch** (Chủ đề 13: Xem đồng hồ. Tháng – năm. '
                 'Tiền Việt Nam), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đọc và liên hệ được giờ giữa đồng hồ kim và đồng hồ điện tử ($24$ giờ).',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 67: Thực hành xem đồng hồ, xem lịch: Đọc và liên hệ '
                        'được giờ giữa đồng hồ kim và đồng hồ điện tử ($24$ giờ).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Ngày cuối cùng của tháng $4$ hằng năm là ngày $31$ tháng $4$."',
            'answer': False,
            'solution': 'Tháng $4$ chỉ có $30$ ngày nên ngày cuối cùng là ngày $30$ tháng $4$ $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 67: Thực hành xem đồng hồ, xem lịch**, quy tắc **Cùng thứ tuần sau** được xác '
                 'định bởi $\\text{Ngày mới} = \\text{Ngày cũ} + 7$ và áp dụng trực tiếp vào bài toán: “Ngày '
                 '$28$ tháng $3$ là thứ Hai. Hỏi ngày $4$ tháng $4$ cùng năm đó là thứ mấy?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cùng thứ tuần sau** ($\\text{Ngày mới} = \\text{Ngày '
                        'cũ} + 7$) là kiến thức cốt lõi của Bài 67: Thực hành xem đồng hồ, xem lịch. Tháng '
                        '$3$ có $31$ ngày. Từ ngày $28$ tháng $3$ đến ngày $4$ tháng $4$ có số ngày là: $(31 '
                        '- 28) + 4 = 7\\text{ (ngày)} = 1\\text{ tuần}$. Vậy...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 67: Thực hành xem đồng hồ, xem lịch** để giải quyết tình huống '
                 'sau: Ngày $28$ tháng $3$ là thứ Hai. Hỏi ngày $4$ tháng $4$ cùng năm đó là thứ mấy? Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Tháng $3$ có $31$ ngày. Từ ngày $28$ tháng $3$ đến ngày $4$ tháng $4$ có số ngày '
                        'là: $(31 - 28) + 4 = 7\\text{ (ngày)} = 1\\text{ tuần}$. Vậy ngày $4$ tháng...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 67: Thực hành xem đồng hồ, xem lịch: Tháng $3$ có $31$ '
                        'ngày. Từ ngày $28$ tháng $3$ đến ngày $4$ tháng $4$ có số ngày là: $(31 - 28) + 4 = '
                        '7\\text{ (ngày)} = 1\\text{ tuần}$.\n'
                        'Vậy ngày $4$ tháng $4$ cũng là **thứ Hai**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hội chợ sách diễn ra từ ngày $12$ tháng $10$ đến hết ngày $19$ tháng $10$. Hỏi hội chợ '
                 'sách diễn ra trong bao nhiêu ngày?',
            'answer': ['8'],
            'unit': 'ngày',
            'solution': 'Số ngày diễn ra hội chợ (tính cả ngày đầu và ngày cuối) là: $(19 - 12) + 1 = '
                        '8\\text{ (ngày)}$.\n'
                        'Đáp số: **$8\\text{ ngày}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd13-dong-ho-thang-nam-tien',
  'context_title': 'Chủ đề 13: Xem đồng hồ. Tháng – năm. Tiền Việt Nam',
  'context': 'SGK Toán 3 · Chủ đề 13: Xem đồng hồ, tháng – năm và tiền Việt Nam.',
  'title': 'Bài 68, 69: Tiền Việt Nam và luyện tập chung',
  'icon': '💵',
  'description': 'Nhận biết các mệnh giá tiền Việt Nam đến 100 000 đồng (và 200 000, 500 000 đồng); tính '
                 'toán mua bán.',
  'requirements': ['Nhận biết mệnh giá các tờ tiền Việt Nam trong phạm vi $100\\,000$ đồng (và làm quen tờ '
                   '$200\\,000$, $500\\,000$ đồng).',
                   'Biết quy đổi các tờ tiền có giá trị tương đương.',
                   'Tính được tổng tiền mua hàng và số tiền trả lại trong mua bán hằng ngày.'],
  'definition': '- Đơn vị tiền tệ của Việt Nam là **đồng**.\n'
                '- Các mệnh giá tờ tiền phổ biến: $1\\,000$; $2\\,000$; $5\\,000$; $10\\,000$; $20\\,000$; '
                '$50\\,000$; $100\\,000$; $200\\,000$; $500\\,000$ đồng.\n'
                '- **Công thức mua bán**: $\\text{Tiền trả lại} = \\text{Tiền khách đưa} - \\text{Tổng tiền '
                'mua hàng}$.',
  'theory': '### 1. Đổi tiền cùng giá trị\n'
            '- Ví dụ: $1$ tờ $50\\,000$ đồng đổi được $2$ tờ $20\\,000$ đồng và $1$ tờ $10\\,000$ đồng (vì '
            '$20\\,000 \\times 2 + 10\\,000 = 50\\,000$).\n'
            '- Ví dụ: $1$ tờ $100\\,000$ đồng đổi được $2$ tờ $50\\,000$ đồng hoặc $5$ tờ $20\\,000$ đồng.\n'
            '### 2. Tính tiền khi mua hàng\n'
            '- Cộng giá tiền các món hàng đã chọn, sau đó lấy số tiền đưa cho người bán trừ đi tổng tiền '
            'hàng.',
  'formulas': [{'category': 'I. Tính toán với tiền Việt Nam',
                'items': [{'name': 'Tổng tiền hàng', 'formula': '$\\text{Đơn giá} \\times \\text{Số lượng}$'},
                          {'name': 'Tiền thừa trả lại',
                           'formula': '$\\text{Tiền đưa} - \\text{Tiền hàng}$'}]}],
  'example': 'Lan đưa cô bán hàng tờ $50\\,000$ đồng để mua một quyển truyện giá $35\\,000$ đồng. Hỏi cô bán '
             'hàng phải trả lại Lan bao nhiêu tiền?',
  'example_answer': 'Số tiền cô bán hàng trả lại Lan là: $50\\,000 - 35\\,000 = 15\\,000\\text{ (đồng)}$.\n'
                    'Đáp số: **$15\\,000\\text{ đồng}$**.',
  'real_life': '- Đi siêu thị, mua đồ dùng học tập ở hiệu sách và kiểm tra tiền thừa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các tờ tiền sau, tờ tiền có mệnh giá lớn nhất là:',
            'options': ['$50\\,000$ đồng', '$20\\,000$ đồng', '$100\\,000$ đồng', '$10\\,000$ đồng'],
            'answer': 2,
            'solution': 'Tờ **$100\\,000$ đồng** có mệnh giá lớn nhất trong bốn phương án.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Lan đưa tờ $50\\,000$ đồng để mua quyển truyện giá $35\\,000$ đồng. Số tiền Lan được trả '
                 'lại là:',
            'options': ['$25\\,000$ đồng', '$85\\,000$ đồng', '$5\\,000$ đồng', '$15\\,000$ đồng'],
            'answer': 3,
            'solution': 'Ta có $50\\,000 - 35\\,000 = 15\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 68, 69: Tiền Việt Nam và luyện tập chung**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Tổng tiền hàng**?',
            'options': ['$\\text{Đơn giá} \\times \\text{Số lượng}$',
                        '$\\text{Tiền đưa} - \\text{Tiền hàng}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 68, 69: Tiền Việt Nam và luyện tập chung, '
                        '**Tổng tiền hàng** được xác định bởi: $\\text{Đơn giá} \\times \\text{Số lượng}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 68, 69: Tiền Việt Nam và luyện tập chung**, nội dung/biểu thức $\\text{Tiền '
                 'đưa} - \\text{Tiền hàng}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tổng tiền hàng', 'Tiền thừa trả lại', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 68, 69: Tiền Việt Nam và luyện tập chung, biểu thức/quy tắc $\\text{Tiền '
                        'đưa} - \\text{Tiền hàng}$ chính là nội dung của **Tiền thừa trả lại**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một tờ tiền mệnh giá $100\\,000$ đồng có thể đổi được bao nhiêu tờ tiền mệnh giá '
                 '$20\\,000$ đồng?',
            'options': ['$2$ tờ', '$4$ tờ', '$5$ tờ', '$10$ tờ'],
            'answer': 2,
            'solution': 'Vì $20\\,000 \\times 5 = 100\\,000$ nên đổi được **$5$ tờ**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 68, 69: Tiền Việt Nam và luyện tập chung** (Chủ đề 13: Xem đồng hồ. Tháng – '
                 'năm. Tiền Việt Nam), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Nhận biết mệnh giá các tờ tiền Việt Nam trong phạm vi $100\\,000$ đồng (và làm quen '
                        'tờ $200\\,000$, $500\\,000$ đồng).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 68, 69: Tiền Việt Nam và luyện tập chung: Nhận biết '
                        'mệnh giá các tờ tiền Việt Nam trong phạm vi $100\\,000$ đồng (và làm quen tờ '
                        '$200\\,000$, $500\\,000$ đồng).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong ví có $2$ tờ $20\\,000$ đồng và $1$ tờ $10\\,000$ đồng thì tổng số tiền '
                 'là $50\\,000$ đồng."',
            'answer': True,
            'solution': 'Ta có $20\\,000 \\times 2 + 10\\,000 = 50\\,000$ đồng $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 68, 69: Tiền Việt Nam và luyện tập chung**, quy tắc **Tổng tiền hàng** được '
                 'xác định bởi $\\text{Đơn giá} \\times \\text{Số lượng}$ và áp dụng trực tiếp vào bài toán: '
                 '“Lan đưa cô bán hàng tờ $50\\,000$ đồng để mua một quyển truyện giá $35\\,000$ đồng. Hỏi '
                 'cô bán hàng phải trả lại Lan bao nhiêu tiền?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tổng tiền hàng** ($\\text{Đơn giá} \\times \\text{Số '
                        'lượng}$) là kiến thức cốt lõi của Bài 68, 69: Tiền Việt Nam và luyện tập chung. Số '
                        'tiền cô bán hàng trả lại Lan là: $50\\,000 - 35\\,000 = 15\\,000\\text{ (đồng)}$. '
                        'Đáp số: **$15\\,000\\text{ đồng}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 68, 69: Tiền Việt Nam và luyện tập chung** để giải quyết tình '
                 'huống sau: Lan đưa cô bán hàng tờ $50\\,000$ đồng để mua một quyển truyện giá $35\\,000$ '
                 'đồng. Hỏi cô bán hàng phải trả lại Lan bao nhiêu tiền? Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Số tiền cô bán hàng trả lại Lan là: $50\\,000 - 35\\,000 = 15\\,000\\text{ '
                        '(đồng)}$. Đáp số: **$15\\,000\\text{ đồng}$**.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 68, 69: Tiền Việt Nam và luyện tập chung: Số tiền cô bán '
                        'hàng trả lại Lan là: $50\\,000 - 35\\,000 = 15\\,000\\text{ (đồng)}$.\n'
                        'Đáp số: **$15\\,000\\text{ đồng}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Nam mua $3$ chiếc bút bi, mỗi chiếc giá $5\\,000$ đồng và $1$ quyển sổ giá $25\\,000$ '
                 'đồng. Hỏi Nam phải trả cô bán hàng tất cả bao nhiêu đồng (viết số liền)?',
            'answer': ['40000'],
            'unit': 'đồng',
            'solution': 'Tiền mua bút: $5\\,000 \\times 3 = 15\\,000$ (đồng). Tổng số tiền phải trả: '
                        '$15\\,000 + 25\\,000 = 40\\,000$ (đồng).\n'
                        'Đáp số: **$40000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd14-nhan-chia-pham-vi-100000',
  'context_title': 'Chủ đề 14: Nhân, chia trong phạm vi 100 000',
  'context': 'SGK Toán 3 · Chủ đề 14: Phép nhân, phép chia trong phạm vi 100 000.',
  'title': 'Bài 70: Nhân số có năm chữ số với số có một chữ số',
  'icon': '✖️',
  'description': 'Đặt tính và thực hiện phép nhân số có năm chữ số với số có một chữ số; nhân nhẩm số tròn '
                 'chục nghìn.',
  'requirements': ['Đặt tính và tính đúng phép nhân số có năm chữ số với số có một chữ số (có nhớ không quá '
                   'hai lượt).',
                   'Nhân nhẩm được số tròn nghìn, tròn chục nghìn với số có một chữ số.',
                   'Giải được bài toán thực tế có phép nhân trong phạm vi $100\\,000$.'],
  'definition': '- Khi nhân số có năm chữ số với số có một chữ số, ta đặt tính thẳng cột rồi nhân lần lượt '
                'từ phải sang trái: **đơn vị $\\rightarrow$ chục $\\rightarrow$ trăm $\\rightarrow$ nghìn '
                '$\\rightarrow$ chục nghìn**.\n'
                '- Nhớ phần chục của mỗi lượt nhân sang hàng kế tiếp ngay bên trái.',
  'theory': '### 1. Nhân nhẩm số tròn chục nghìn\n'
            '- Ví dụ: $20\\,000 \\times 3 = 60\\,000$ ($2$ chục nghìn $\\times 3 = 6$ chục nghìn).\n'
            '- Ví dụ: $15\\,000 \\times 6 = 90\\,000$.\n'
            '### 2. Đặt tính rồi tính\n'
            '- Ví dụ: $21\\,304 \\times 3 = 63\\,912$.\n'
            '- Ví dụ có nhớ: $14\\,216 \\times 5 = 71\\,080$.',
  'formulas': [{'category': 'I. Nhân trong phạm vi 100 000',
                'items': [{'name': 'Nhẩm tròn chục nghìn',
                           'formula': '$a0\\,000 \\times b = (a \\times b)0\\,000$'},
                          {'name': 'Thứ tự nhân viết',
                           'formula': 'Từ phải sang trái (Đơn vị $\\rightarrow$ Chục nghìn)'}]}],
  'example': 'Đặt tính rồi tính: $12\\,031 \\times 3$ và $18\\,245 \\times 4$.',
  'example_answer': '- $12\\,031 \\times 3 = 36\\,093$.\n'
                    '- $18\\,245 \\times 4 = 72\\,980$ ($5\\times4=20$ viết $0$ nhớ $2$; $4\\times4+2=18$ '
                    'viết $8$ nhớ $1$; $2\\times4+1=9$; $8\\times4=32$ viết $2$ nhớ $3$; $1\\times4+3=7$).',
  'real_life': '- Tính tổng khối lượng hàng hóa của nhiều chuyến xe tải; tính tiền mua nhiều vé tham quan.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $20\\,000 \\times 3 = ?$',
            'options': ['$6\\,000$', '$600\\,000$', '$23\\,000$', '$60\\,000$'],
            'answer': 3,
            'solution': '$2$ chục nghìn $\\times 3 = 60\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $12\\,031 \\times 3$ là:',
            'options': ['$36\\,093$', '$36\\,033$', '$36\\,903$', '$12\\,034$'],
            'answer': 0,
            'solution': 'Nhân từng hàng từ phải sang trái: $12\\,031 \\times 3 = 36\\,093$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 70: Nhân số có năm chữ số với số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Nhẩm tròn chục nghìn**?',
            'options': ['Từ phải sang trái (Đơn vị $\\rightarrow$ Chục nghìn)',
                        '$a0\\,000 \\times b = (a \\times b)0\\,000$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 70: Nhân số có năm chữ số với số có một chữ '
                        'số, **Nhẩm tròn chục nghìn** được xác định bởi: $a0\\,000 \\times b = (a \\times '
                        'b)0\\,000$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 70: Nhân số có năm chữ số với số có một chữ số**, nội dung/biểu thức Từ phải '
                 'sang trái (Đơn vị $\\rightarrow$ Chục nghìn) là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Nhẩm tròn chục nghìn',
                        'Phân tích số',
                        'Thứ tự nhân viết',
                        'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 70: Nhân số có năm chữ số với số có một chữ số, biểu thức/quy tắc Từ phải '
                        'sang trái (Đơn vị $\\rightarrow$ Chục nghìn) chính là nội dung của **Thứ tự nhân '
                        'viết**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $18\\,245 \\times 4$ là:',
            'options': ['$72\\,880$', '$73\\,980$', '$62\\,980$', '$72\\,980$'],
            'answer': 3,
            'solution': 'Ta có $18\\,245 \\times 4 = 72\\,980$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 70: Nhân số có năm chữ số với số có một chữ số** (Chủ đề 14: Nhân, chia '
                 'trong phạm vi 100 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đặt tính và tính đúng phép nhân số có năm chữ số với số có một chữ số (có nhớ không '
                        'quá hai lượt).',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 70: Nhân số có năm chữ số với số có một chữ số: Đặt '
                        'tính và tính đúng phép nhân số có năm chữ số với số có một chữ số (có nhớ không quá '
                        'hai lượt).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$15\\,000 \\times 6 = 90\\,000$."',
            'answer': True,
            'solution': '$15$ nghìn $\\times 6 = 90$ nghìn $= 90\\,000$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 70: Nhân số có năm chữ số với số có một chữ số**, quy tắc **Nhẩm tròn chục '
                 'nghìn** được xác định bởi $a0\\,000 \\times b = (a \\times b)0\\,000$ và áp dụng trực tiếp '
                 'vào bài toán: “Đặt tính rồi tính: $12\\,031 \\times 3$ và $18\\,245 \\times 4$.”. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhẩm tròn chục nghìn** ($a0\\,000 \\times b = (a '
                        '\\times b)0\\,000$) là kiến thức cốt lõi của Bài 70: Nhân số có năm chữ số với số '
                        'có một chữ số. - $12\\,031 \\times 3 = 36\\,093$. - $18\\,245 \\times 4 = 72\\,980$ '
                        '($5\\times4=20$ viết $0$ nhớ $2$; $4\\times4+2=18$ viết $8$ nhớ $1$; '
                        '$2\\times4+1=9$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 70: Nhân số có năm chữ số với số có một chữ số** để giải quyết '
                 'tình huống sau: Đặt tính rồi tính: $12\\,031 \\times 3$ và $18\\,245 \\times 4$. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $12\\,031 \\times 3 = 36\\,093$. - $18\\,245 \\times 4 = 72\\,980$ '
                        '($5\\times4=20$ viết $0$ nhớ $2$; $4\\times4+2=18$ viết $8$ nhớ $1$; '
                        '$2\\times4+1=9$; $8\\times4=32$...',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 70: Nhân số có năm chữ số với số có một chữ số: - '
                        '$12\\,031 \\times 3 = 36\\,093$.\n'
                        '- $18\\,245 \\times 4 = 72\\,980$ ($5\\times4=20$ viết $0$ nhớ $2$; '
                        '$4\\times4+2=18$ viết $8$ nhớ $1$; $2\\times4+1=9$; $8\\times4=32$ viết $2$ nhớ '
                        '$3$; $1\\times4+3=7$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một xe tải chở $4$ chuyến hàng, mỗi chuyến chở $12\\,500\\text{ kg}$ hàng. Hỏi xe tải đó '
                 'đã chở tất cả bao nhiêu ki-lô-gam hàng (viết số liền)?',
            'answer': ['50000'],
            'unit': 'kg',
            'solution': 'Tổng khối lượng hàng xe đã chở là: $12\\,500 \\times 4 = 50\\,000\\text{ (kg)}$.\n'
                        'Đáp số: **$50000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd14-nhan-chia-pham-vi-100000',
  'context_title': 'Chủ đề 14: Nhân, chia trong phạm vi 100 000',
  'context': 'SGK Toán 3 · Chủ đề 14: Phép nhân, phép chia trong phạm vi 100 000.',
  'title': 'Bài 71: Chia số có năm chữ số cho số có một chữ số',
  'icon': '➗',
  'description': 'Thực hiện phép chia số có năm chữ số cho số có một chữ số (chia hết và chia có dư).',
  'requirements': ['Đặt tính dọc và chia đúng số có năm chữ số cho số có một chữ số từ trái sang phải.',
                   'Viết đúng các chữ số $0$ ở thương khi số bị chia ở lượt hạ xuống bé hơn số chia.',
                   'Giải được bài toán thực tế liên quan đến phép chia số có năm chữ số.'],
  'definition': '- Khi chia số có năm chữ số cho số có một chữ số, ta bắt đầu chia từ **hàng chục nghìn** '
                '(hàng cao nhất bên trái).\n'
                '- Mỗi lần hạ một chữ số xuống, nếu số tạo thành bé hơn số chia thì phải **viết $0$ vào '
                'thương** rồi mới hạ chữ số tiếp theo.',
  'theory': '### 1. Phép chia hết\n'
            '- Ví dụ: $36\\,284 : 4 = 9\\,071$ (lấy $36 : 4 = 9$; hạ $2$, vì $2 < 4$ nên viết $0$; hạ $8$ '
            'được $28 : 4 = 7$; hạ $4$ được $4 : 4 = 1$).\n'
            '- Ví dụ có hai chữ số $0$ liên tiếp ở thương: $24\\,036 : 6 = 4\\,006$.\n'
            '### 2. Phép chia có dư\n'
            '- Ví dụ: $25\\,609 : 5 = 5\\,121 \\text{ (dư } 4\\text{)}$.',
  'formulas': [{'category': 'I. Chia số có năm chữ số',
                'items': [{'name': 'Nhẩm tròn chục nghìn', 'formula': '$a0\\,000 : b = (a : b)0\\,000$'},
                          {'name': 'Kiểm tra phép chia',
                           'formula': '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số '
                                      'bị chia}$ ($0 \\le r < b$)'}]}],
  'example': 'Đặt tính rồi tính: $24\\,036 : 6$ và $48\\,567 : 7$.',
  'example_answer': '- $24\\,036 : 6 = 4\\,006$.\n- $48\\,567 : 7 = 6\\,938 \\text{ (dư } 1\\text{)}$.',
  'real_life': '- Chia đều số quyển vở quyên góp cho các trường học; chia đều lượng thóc vào các kho.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $80\\,000 : 4 = ?$',
            'options': ['$20\\,000$', '$2\\,000$', '$200\\,000$', '$32\\,000$'],
            'answer': 0,
            'solution': '$8$ chục nghìn $: 4 = 2$ chục nghìn $= 20\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Thương của phép chia $36\\,284 : 4$ là:',
            'options': ['$971$', '$9\\,071$', '$9\\,701$', '$9\\,017$'],
            'answer': 1,
            'solution': 'Ta có $36 : 4 = 9$; hạ $2 < 4$ viết $0$; $28 : 4 = 7$; $4 : 4 = 1 \\rightarrow '
                        '9\\,071$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 71: Chia số có năm chữ số cho số có một chữ số**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Nhẩm tròn chục nghìn**?',
            'options': ['$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$ ($0 '
                        '\\le r < b$)',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$a0\\,000 : b = (a : b)0\\,000$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 71: Chia số có năm chữ số cho số có một chữ '
                        'số, **Nhẩm tròn chục nghìn** được xác định bởi: $a0\\,000 : b = (a : b)0\\,000$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 71: Chia số có năm chữ số cho số có một chữ số**, nội dung/biểu thức '
                 '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$ ($0 \\le r < '
                 'b$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Nhẩm tròn chục nghìn',
                        'Phân tích số',
                        'Số tròn trăm, tròn nghìn',
                        'Kiểm tra phép chia'],
            'answer': 3,
            'solution': 'Trong Bài 71: Chia số có năm chữ số cho số có một chữ số, biểu thức/quy tắc '
                        '$\\text{Thương} \\times \\text{Số chia} + \\text{Số dư} = \\text{Số bị chia}$ ($0 '
                        '\\le r < b$) chính là nội dung của **Kiểm tra phép chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $24\\,036 : 6$ là:',
            'options': ['$4\\,006$', '$406$', '$4\\,060$', '$460$'],
            'answer': 0,
            'solution': 'Ta có $24 : 6 = 4$; hạ $0 \\rightarrow 0$; hạ $3 < 6 \\rightarrow 0$; hạ $6$ được '
                        '$36 : 6 = 6 \\rightarrow 4\\,006$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 71: Chia số có năm chữ số cho số có một chữ số** (Chủ đề 14: Nhân, chia '
                 'trong phạm vi 100 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Đặt tính dọc và chia đúng số có năm chữ số cho số có một chữ số từ trái sang phải.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 71: Chia số có năm chữ số cho số có một chữ số: Đặt '
                        'tính dọc và chia đúng số có năm chữ số cho số có một chữ số từ trái sang phải.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $32\\,157 : 4$ có số dư là $5$."',
            'answer': False,
            'solution': 'Số dư luôn phải bé hơn số chia $4$ (thực tế $32\\,157 : 4 = 8\\,039$ dư $1$) '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 71: Chia số có năm chữ số cho số có một chữ số**, quy tắc **Nhẩm tròn chục '
                 'nghìn** được xác định bởi $a0\\,000 : b = (a : b)0\\,000$ và áp dụng trực tiếp vào bài '
                 'toán: “Đặt tính rồi tính: $24\\,036 : 6$ và $48\\,567 : 7$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhẩm tròn chục nghìn** ($a0\\,000 : b = (a : '
                        'b)0\\,000$) là kiến thức cốt lõi của Bài 71: Chia số có năm chữ số cho số có một '
                        'chữ số. - $24\\,036 : 6 = 4\\,006$. - $48\\,567 : 7 = 6\\,938 \\text{ (dư } '
                        '1\\text{)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 71: Chia số có năm chữ số cho số có một chữ số** để giải quyết '
                 'tình huống sau: Đặt tính rồi tính: $24\\,036 : 6$ và $48\\,567 : 7$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        '- $24\\,036 : 6 = 4\\,006$. - $48\\,567 : 7 = 6\\,938 \\text{ (dư } 1\\text{)}$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 71: Chia số có năm chữ số cho số có một chữ số: - '
                        '$24\\,036 : 6 = 4\\,006$.\n'
                        '- $48\\,567 : 7 = 6\\,938 \\text{ (dư } 1\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có $45\\,650$ quyển vở chia đều cho $5$ trường. Hỏi mỗi trường nhận được bao nhiêu quyển '
                 'vở (viết số liền)?',
            'answer': ['9130'],
            'unit': 'quyển',
            'solution': 'Mỗi trường nhận được số quyển vở là: $45\\,650 : 5 = 9\\,130\\text{ (quyển)}$.\n'
                        'Đáp số: **$9130$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd14-nhan-chia-pham-vi-100000',
  'context_title': 'Chủ đề 14: Nhân, chia trong phạm vi 100 000',
  'context': 'SGK Toán 3 · Chủ đề 14: Phép nhân, phép chia trong phạm vi 100 000.',
  'title': 'Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000',
  'icon': '🧮',
  'description': 'Vận dụng tính chất giao hoán, kết hợp của phép nhân và giải bài toán hai bước tính trong '
                 'phạm vi 100 000.',
  'requirements': ['Nhận biết và vận dụng được tính chất giao hoán, kết hợp của phép nhân để tính nhẩm '
                   'nhanh.',
                   'Tính đúng giá trị biểu thức có phép nhân, phép chia trong phạm vi $100\\,000$.',
                   'Giải được bài toán có lời văn gồm hai bước tính nhân, chia.'],
  'definition': '- **Tính chất giao hoán của phép nhân**: $a \\times b = b \\times a$.\n'
                '- **Tính chất kết hợp của phép nhân**: $(a \\times b) \\times c = a \\times (b \\times c)$ '
                '(thường nhóm $2 \\times 5 = 10$ hoặc $4 \\times 2 = 8$).',
  'theory': '### 1. Tính bằng cách thuận tiện\n'
            '- Ví dụ: $5 \\times 7 \\times 2 = (5 \\times 2) \\times 7 = 10 \\times 7 = 70$.\n'
            '- Ví dụ: $2\\,000 \\times 9 \\times 5 = (2\\,000 \\times 5) \\times 9 = 10\\,000 \\times 9 = '
            '90\\,000$.\n'
            '### 2. Giải toán hai bước tính\n'
            '- Đọc kỹ đề bài để xác định bước $1$ cần tìm tổng hay tìm giá trị một phần.',
  'formulas': [{'category': 'I. Tính chất phép nhân',
                'items': [{'name': 'Giao hoán', 'formula': '$a \\times b = b \\times a$'},
                          {'name': 'Kết hợp',
                           'formula': '$(a \\times b) \\times c = a \\times (b \\times c)$'}]}],
  'example': 'Tính giá trị của biểu thức: $15\\,000 + 42\\,000 : 6$.',
  'example_answer': 'Thực hiện phép chia trước: $42\\,000 : 6 = 7\\,000$.\n'
                    'Cộng sau: $15\\,000 + 7\\,000 = 22\\,000$.',
  'real_life': '- Tính tiền khi mua nhiều lốc sữa hoặc tính sản lượng chia đều vào các kho.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính chất $(a \\times b) \\times c = a \\times (b \\times c)$ được gọi là:',
            'options': ['Tính chất giao hoán',
                        'Tính chất kết hợp',
                        'Tính chất phân phối',
                        'Chia một số cho một tích'],
            'answer': 1,
            'solution': 'Đó là **tính chất kết hợp** của phép nhân.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $25\\,000 \\times 2 : 5$ là:',
            'options': ['$50\\,000$', '$5\\,000$', '$10\\,000$', '$15\\,000$'],
            'answer': 2,
            'solution': 'Tính từ trái sang phải: $25\\,000 \\times 2 = 50\\,000$; $50\\,000 : 5 = 10\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Giao hoán**?',
            'options': ['$(a \\times b) \\times c = a \\times (b \\times c)$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        '$a \\times b = b \\times a$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 72: Luyện tập chung nhân, chia trong phạm vi '
                        '100 000, **Giao hoán** được xác định bởi: $a \\times b = b \\times a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000**, nội dung/biểu thức $(a '
                 '\\times b) \\times c = a \\times (b \\times c)$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Kết hợp', 'Giao hoán', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000, biểu thức/quy tắc '
                        '$(a \\times b) \\times c = a \\times (b \\times c)$ chính là nội dung của **Kết '
                        'hợp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x : 4 = 12\\,300$:',
            'options': ['$3\\,075$', '$49\\,200$', '$48\\,200$', '$12\\,304$'],
            'answer': 1,
            'solution': 'Số bị chia $x = 12\\,300 \\times 4 = 49\\,200$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000** (Chủ đề 14: Nhân, '
                 'chia trong phạm vi 100 000), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Nhận biết và vận dụng được tính chất giao hoán, kết hợp của phép nhân để tính nhẩm '
                        'nhanh.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000: '
                        'Nhận biết và vận dụng được tính chất giao hoán, kết hợp của phép nhân để tính nhẩm '
                        'nhanh.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của hai biểu thức $(1\\,200 \\times 2) \\times 4$ và $1\\,200 \\times '
                 '(2 \\times 4)$ bằng nhau và bằng $9\\,600$."',
            'answer': True,
            'solution': 'Theo tính chất kết hợp của phép nhân, cả hai đều bằng $1\\,200 \\times 8 = 9\\,600$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000**, quy tắc **Giao hoán** '
                 'được xác định bởi $a \\times b = b \\times a$ và áp dụng trực tiếp vào bài toán: “Tính giá '
                 'trị của biểu thức: $15\\,000 + 42\\,000 : 6$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Giao hoán** ($a \\times b = b \\times a$) là kiến '
                        'thức cốt lõi của Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000. Thực '
                        'hiện phép chia trước: $42\\,000 : 6 = 7\\,000$. Cộng sau: $15\\,000 + 7\\,000 = '
                        '22\\,000$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000** để giải '
                 'quyết tình huống sau: Tính giá trị của biểu thức: $15\\,000 + 42\\,000 : 6$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Thực hiện phép chia trước: $42\\,000 : 6 = 7\\,000$. Cộng sau: $15\\,000 + 7\\,000 '
                        '= 22\\,000$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 72: Luyện tập chung nhân, chia trong phạm vi 100 000: '
                        'Thực hiện phép chia trước: $42\\,000 : 6 = 7\\,000$.\n'
                        'Cộng sau: $15\\,000 + 7\\,000 = 22\\,000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một xưởng may làm được $24\\,600$ chiếc áo trong $3$ tuần. Biết số áo làm được trong mỗi '
                 'tuần là như nhau, hỏi trong $1$ tuần xưởng đó làm được bao nhiêu chiếc áo (viết số liền)?',
            'answer': ['8200'],
            'unit': 'chiếc',
            'solution': 'Số chiếc áo làm được trong $1$ tuần là: $24\\,600 : 3 = 8\\,200\\text{ (chiếc)}$.\n'
                        'Đáp số: **$8200$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd15-thong-ke-xac-suat',
  'context_title': 'Chủ đề 15: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 3 · Chủ đề 15: Làm quen với yếu tố thống kê và xác suất.',
  'title': 'Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu',
  'icon': '📊',
  'description': 'Cách thu thập, phân loại, kiểm đếm số liệu và đọc, phân tích bảng số liệu thống kê.',
  'requirements': ['Biết cách phân loại và kiểm đếm số liệu theo các tiêu chí cho trước.',
                   'Đọc và hiểu được thông tin trình bày trong bảng số liệu (hàng, cột).',
                   'Tìm được giá trị lớn nhất, bé nhất, tổng hoặc hiệu từ bảng số liệu.'],
  'definition': '- **Thu thập, phân loại, ghi chép số liệu** giúp ta nắm được số lượng của từng nhóm đối '
                'tượng (thường dùng vạch kiểm đếm, mỗi cụm $5$ vạch).\n'
                '- **Bảng số liệu** trình bày thông tin theo các hàng và các cột rõ ràng để dễ đọc và so '
                'sánh.',
  'theory': '### 1. Cấu tạo của bảng số liệu\n'
            '- Thường gồm $2$ hàng (hoặc $2$ cột): Hàng 1 ghi tên các đối tượng (ví dụ: Táo, Cam, Xoài); '
            'Hàng 2 ghi số liệu tương ứng (ví dụ: $12, 9, 15$).\n'
            '### 2. Khai thác bảng số liệu\n'
            '- Đối tượng nào có số lớn nhất (nhiều nhất), bé nhất (ít nhất).\n'
            '- Tính tổng số lượng tất cả các đối tượng hoặc tính xem đối tượng A nhiều hơn đối tượng B bao '
            'nhiêu.',
  'formulas': [{'category': 'I. Đọc bảng số liệu',
                'items': [{'name': 'Tổng số liệu',
                           'formula': '$\\text{Tổng} = \\text{Cộng tất cả các số liệu trong bảng}$'},
                          {'name': 'Hơn kém',
                           'formula': '$\\text{Chênh lệch} = \\text{Số liệu lớn} - \\text{Số liệu bé}$'}]}],
  'example': 'Bảng số cây trồng của khối 3: Lớp 3A trồng $25$ cây, lớp 3B trồng $30$ cây, lớp 3C trồng $28$ '
             'cây. Hỏi lớp nào trồng nhiều cây nhất và cả ba lớp trồng được bao nhiêu cây?',
  'example_answer': '- Vì $30 > 28 > 25$ nên **lớp 3B** trồng nhiều cây nhất.\n'
                    '- Cả ba lớp trồng được: $25 + 30 + 28 = 83\\text{ (cây)}$.',
  'real_life': '- Lập bảng thống kê các môn thể thao yêu thích của các bạn trong lớp hoặc số sách mỗi tổ '
               'quyên góp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho bảng số bạn thích các loại quả: Táo ($12$ bạn), Cam ($9$ bạn), Xoài ($15$ bạn). Loại '
                 'quả được nhiều bạn thích nhất là:',
            'options': ['Táo', 'Cam', 'Xoài', 'Ba loại bằng nhau'],
            'answer': 2,
            'solution': 'Vì $15 > 12 > 9$ nên **Xoài** được thích nhiều nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo bảng trên (Táo: $12$, Cam: $9$, Xoài: $15$), số bạn thích quả Cam là:',
            'options': ['$12$ bạn', '$15$ bạn', '$36$ bạn', '$9$ bạn'],
            'answer': 3,
            'solution': 'Đọc cột Cam ta thấy có **$9$ bạn**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số '
                 'liệu**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tổng số liệu**?',
            'options': ['$\\text{Tổng} = \\text{Cộng tất cả các số liệu trong bảng}$',
                        '$\\text{Chênh lệch} = \\text{Số liệu lớn} - \\text{Số liệu bé}$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 73: Thu thập, phân loại, ghi chép số liệu. '
                        'Bảng số liệu, **Tổng số liệu** được xác định bởi: $\\text{Tổng} = \\text{Cộng tất '
                        'cả các số liệu trong bảng}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu**, nội dung/biểu thức '
                 '$\\text{Chênh lệch} = \\text{Số liệu lớn} - \\text{Số liệu bé}$ là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Tổng số liệu', 'Hơn kém', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu, biểu thức/quy '
                        'tắc $\\text{Chênh lệch} = \\text{Số liệu lớn} - \\text{Số liệu bé}$ chính là nội '
                        'dung của **Hơn kém**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Theo bảng trên (Táo: $12$, Cam: $9$, Xoài: $15$), số bạn thích Xoài nhiều hơn số bạn thích '
                 'Cam là:',
            'options': ['$3$ bạn', '$24$ bạn', '$6$ bạn', '$27$ bạn'],
            'answer': 2,
            'solution': 'Ta lấy $15 - 9 = 6\\text{ (bạn)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu** (Chủ đề 15: Làm '
                 'quen với yếu tố thống kê, xác suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Biết cách phân loại và kiểm đếm số liệu theo các tiêu chí cho trước.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số '
                        'liệu: Biết cách phân loại và kiểm đếm số liệu theo các tiêu chí cho trước.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Theo bảng trên (Táo: $12$, Cam: $9$, Xoài: $15$), tổng số lượt bạn được khảo '
                 'sát là $36$."',
            'answer': True,
            'solution': 'Tổng là: $12 + 9 + 15 = 36$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu**, quy tắc **Tổng số '
                 'liệu** được xác định bởi $\\text{Tổng} = \\text{Cộng tất cả các số liệu trong bảng}$ và áp '
                 'dụng trực tiếp vào bài toán: “Bảng số cây trồng của khối 3: Lớp 3A trồng $25$ cây, lớp 3B '
                 'trồng $30$ cây, lớp 3C trồng $28$ cây. Hỏi lớp nào trồng nhiều cây nhất và cả ba...”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tổng số liệu** ($\\text{Tổng} = \\text{Cộng tất cả '
                        'các số liệu trong bảng}$) là kiến thức cốt lõi của Bài 73: Thu thập, phân loại, ghi '
                        'chép số liệu. Bảng số liệu. - Vì $30 > 28 > 25$ nên **lớp 3B** trồng nhiều cây '
                        'nhất. - Cả ba lớp trồng được: $25 + 30 + 28 = 83\\text{ (cây)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu** để giải '
                 'quyết tình huống sau: Bảng số cây trồng của khối 3: Lớp 3A trồng $25$ cây, lớp 3B trồng '
                 '$30$ cây, lớp 3C trồng $28$ cây. Hỏi lớp nào trồng nhiều cây nhất và cả ba lớp trồng được '
                 'bao nhiêu cây? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['- Vì $30 > 28 > 25$ nên **lớp 3B** trồng nhiều cây nhất. - Cả ba lớp trồng được: '
                        '$25 + 30 + 28 = 83\\text{ (cây)}$.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu: '
                        '- Vì $30 > 28 > 25$ nên **lớp 3B** trồng nhiều cây nhất.\n'
                        '- Cả ba lớp trồng được: $25 + 30 + 28 = 83\\text{ (cây)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bảng thống kê số học sinh của trường: Khối 3 có $124$ em, Khối 4 có $118$ em, Khối 5 có '
                 '$130$ em. Hỏi Khối 5 có nhiều hơn Khối 4 bao nhiêu học sinh?',
            'answer': ['12'],
            'unit': 'em',
            'solution': 'Khối 5 nhiều hơn Khối 4 số học sinh là: $130 - 118 = 12\\text{ (em)}$.\n'
                        'Đáp số: **$12\\text{ em}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd15-thong-ke-xac-suat',
  'context_title': 'Chủ đề 15: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 3 · Chủ đề 15: Làm quen với yếu tố thống kê và xác suất.',
  'title': 'Bài 74: Khả năng xảy ra của một sự kiện',
  'icon': '🎲',
  'description': 'Nhận biết và liệt kê các khả năng có thể xảy ra của một sự kiện ngẫu nhiên đơn giản.',
  'requirements': ['Nhận biết và nêu được các khả năng có thể xảy ra khi thực hiện $1$ lần thí nghiệm đơn '
                   'giản (tung đồng xu, gieo xúc xắc, rút thẻ).',
                   'Sử dụng đúng các từ "có thể", "chắc chắn", "không thể" để mô tả sự kiện.',
                   'Đếm được số khả năng thuận lợi cho một sự kiện.'],
  'definition': '- Khi thực hiện một trò chơi hay thí nghiệm ngẫu nhiên, ta có thể liệt kê tất cả các **khả '
                'năng xảy ra**.\n'
                '- Ví dụ: Tung một đồng xu $1$ lần thì có **$2$ khả năng** xảy ra: xuất hiện **mặt sấp** '
                'hoặc xuất hiện **mặt ngửa**.\n'
                '- Gieo một con xúc xắc $1$ lần thì có **$6$ khả năng** xảy ra về số chấm xuất hiện: $1, 2, '
                '3, 4, 5$ hoặc $6$ chấm.',
  'theory': '### 1. Liệt kê các khả năng\n'
            '- Trong hộp có $1$ quả bóng xanh, $1$ quả bóng đỏ và $1$ quả bóng vàng. Lấy ngẫu nhiên $1$ quả '
            'bóng thì có $3$ khả năng xảy ra: lấy được bóng xanh, bóng đỏ hoặc bóng vàng.\n'
            '### 2. Sự kiện chắc chắn, có thể, không thể\n'
            '- Nếu trong hộp chỉ toàn bóng đỏ thì lấy $1$ quả **chắc chắn** là bóng đỏ, **không thể** là '
            'bóng xanh.',
  'formulas': [{'category': 'I. Các mô hình xác suất cơ bản',
                'items': [{'name': 'Tung đồng xu', 'formula': '$2$ khả năng: mặt sấp hoặc mặt ngửa'},
                          {'name': 'Gieo xúc xắc', 'formula': '$6$ khả năng: mặt $1, 2, 3, 4, 5, 6$ chấm'}]}],
  'example': 'Trong hộp có $4$ tấm thẻ ghi các số $1, 2, 3, 4$. Rút ngẫu nhiên $1$ tấm thẻ. Liệt kê các khả '
             'năng xảy ra.',
  'example_answer': 'Có **$4$ khả năng** xảy ra là rút được thẻ ghi số $1$, thẻ ghi số $2$, thẻ ghi số $3$ '
                    'hoặc thẻ ghi số $4$.',
  'real_life': '- Tung đồng xu chọn sân trước trận bóng đá; quay vòng quay may mắn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi tung một đồng xu $1$ lần, có mấy khả năng xảy ra đối với mặt xuất hiện của đồng xu?',
            'options': ['$1$ khả năng', '$3$ khả năng', '$4$ khả năng', '$2$ khả năng'],
            'answer': 3,
            'solution': 'Có **$2$ khả năng**: mặt sấp hoặc mặt ngửa.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi gieo một con xúc xắc $1$ lần, có bao nhiêu khả năng xảy ra về số chấm xuất hiện trên '
                 'mặt trên?',
            'options': ['$6$ khả năng', '$2$ khả năng', '$4$ khả năng', '$12$ khả năng'],
            'answer': 0,
            'solution': 'Xúc xắc có $6$ mặt từ $1$ đến $6$ chấm nên có **$6$ khả năng**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 74: Khả năng xảy ra của một sự kiện**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Tung đồng xu**?',
            'options': ['$6$ khả năng: mặt $1, 2, 3, 4, 5, 6$ chấm',
                        '$2$ khả năng: mặt sấp hoặc mặt ngửa',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 74: Khả năng xảy ra của một sự kiện, **Tung '
                        'đồng xu** được xác định bởi: $2$ khả năng: mặt sấp hoặc mặt ngửa.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 74: Khả năng xảy ra của một sự kiện**, nội dung/biểu thức $6$ khả năng: mặt '
                 '$1, 2, 3, 4, 5, 6$ chấm là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Tung đồng xu', 'Phân tích số', 'Gieo xúc xắc', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 74: Khả năng xảy ra của một sự kiện, biểu thức/quy tắc $6$ khả năng: mặt '
                        '$1, 2, 3, 4, 5, 6$ chấm chính là nội dung của **Gieo xúc xắc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong hộp có $3$ quả bóng xanh và $2$ quả bóng đỏ. Không nhìn vào hộp, lấy ra $1$ quả '
                 'bóng. Các khả năng xảy ra về màu của quả bóng lấy ra là:',
            'options': ['Chỉ có thể là bóng xanh',
                        'Chỉ có thể là bóng đỏ',
                        'Bóng vàng',
                        'Bóng xanh hoặc bóng đỏ'],
            'answer': 3,
            'solution': 'Trong hộp có $2$ màu bóng nên có thể lấy được **bóng xanh hoặc bóng đỏ**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 74: Khả năng xảy ra của một sự kiện** (Chủ đề 15: Làm quen với yếu tố thống '
                 'kê, xác suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Nhận biết và nêu được các khả năng có thể xảy ra khi thực hiện $1$ lần thí nghiệm '
                        'đơn giản (tung đồng xu, gieo xúc xắc, rút thẻ).',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 74: Khả năng xảy ra của một sự kiện: Nhận biết và nêu '
                        'được các khả năng có thể xảy ra khi thực hiện $1$ lần thí nghiệm đơn giản (tung '
                        'đồng xu, gieo xúc xắc, rút thẻ).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khi tung một đồng xu $1$ lần thì chắc chắn đồng xu xuất hiện mặt ngửa."',
            'answer': False,
            'solution': 'Đồng xu có thể xuất hiện mặt sấp hoặc mặt ngửa, không thể biết chắc chắn trước '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 74: Khả năng xảy ra của một sự kiện**, quy tắc **Tung đồng xu** được xác định '
                 'bởi $2$ khả năng: mặt sấp hoặc mặt ngửa và áp dụng trực tiếp vào bài toán: “Trong hộp có '
                 '$4$ tấm thẻ ghi các số $1, 2, 3, 4$. Rút ngẫu nhiên $1$ tấm thẻ. Liệt kê các khả năng xảy '
                 'ra.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tung đồng xu** ($2$ khả năng: mặt sấp hoặc mặt ngửa) '
                        'là kiến thức cốt lõi của Bài 74: Khả năng xảy ra của một sự kiện. Có **$4$ khả '
                        'năng** xảy ra là rút được thẻ ghi số $1$, thẻ ghi số $2$, thẻ ghi số $3$ hoặc thẻ '
                        'ghi số $4$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 74: Khả năng xảy ra của một sự kiện** để giải quyết tình huống '
                 'sau: Trong hộp có $4$ tấm thẻ ghi các số $1, 2, 3, 4$. Rút ngẫu nhiên $1$ tấm thẻ. Liệt kê '
                 'các khả năng xảy ra. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Có **$4$ khả năng** xảy ra là rút được thẻ ghi số $1$, thẻ ghi số $2$, thẻ ghi số '
                        '$3$ hoặc thẻ ghi số $4$.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 74: Khả năng xảy ra của một sự kiện: Có **$4$ khả năng** '
                        'xảy ra là rút được thẻ ghi số $1$, thẻ ghi số $2$, thẻ ghi số $3$ hoặc thẻ ghi số '
                        '$4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong hộp có $5$ tấm thẻ đánh số $1, 2, 3, 4, 5$. Rút ngẫu nhiên $1$ tấm thẻ. Hỏi có bao '
                 'nhiêu khả năng rút được tấm thẻ ghi số lẻ?',
            'answer': ['3'],
            'unit': 'khả năng',
            'solution': 'Các số lẻ trong $\\{1, 2, 3, 4, 5\\}$ là $1, 3, 5$ nên có **$3$ khả năng**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd15-thong-ke-xac-suat',
  'context_title': 'Chủ đề 15: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 3 · Chủ đề 15: Làm quen với yếu tố thống kê và xác suất.',
  'title': 'Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu',
  'icon': '📋',
  'description': 'Thực hành kiểm đếm, hoàn thiện bảng số liệu thống kê và giải quyết các câu hỏi thực tế từ '
                 'bảng.',
  'requirements': ['Chuyển được dữ liệu từ hình vẽ hoặc vạch kiểm đếm sang bảng số liệu.',
                   'So sánh, tính tổng và hiệu từ bảng số liệu có $3$ đến $4$ cột.',
                   'Kết hợp kiến thức bảng số liệu và khả năng xảy ra của sự kiện.'],
  'definition': '- Quy trình thực hành thống kê: **Thu thập dữ liệu $\\rightarrow$ Phân loại theo tiêu chí '
                '$\\rightarrow$ Kiểm đếm và ghi chép $\\rightarrow$ Lập bảng số liệu $\\rightarrow$ Rút ra '
                'nhận xét**.',
  'theory': '### 1. Cách kiểm đếm không bị sót\n'
            '- Dùng kí hiệu vạch kiểm đếm: cứ $4$ vạch dọc thì gạch chéo $1$ vạch thứ $5$ để tạo thành từng '
            'bó $5$, giúp nhân nhẩm theo bảng nhân $5$ rất nhanh.\n'
            '### 2. Trả lời câu hỏi từ bảng số liệu\n'
            '- Đọc kỹ đơn vị của số liệu (quyển, cây, học sinh, ki-lô-gam...) trước khi tính toán.',
  'formulas': [{'category': 'I. Quy trình thống kê',
                'items': [{'name': '5 bước',
                           'formula': 'Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm '
                                      '$\\rightarrow$ Lập bảng $\\rightarrow$ Nhận xét'}]}],
  'example': 'Khi kiểm đếm số quyển truyện của tổ, bạn An ghi được $3$ cụm $5$ vạch và thêm $2$ vạch rời. '
             'Hỏi tổ của An có bao nhiêu quyển truyện?',
  'example_answer': 'Số quyển truyện của tổ là: $5 \\times 3 + 2 = 17\\text{ (quyển)}$.\n'
                    'Đáp số: **$17\\text{ quyển}$**.',
  'real_life': '- Kiểm phiếu bầu lớp trưởng bằng các cụm $5$ vạch trên bảng lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong cách ghi chép bằng vạch kiểm đếm, mỗi bó hoàn chỉnh (gồm $4$ vạch thẳng và $1$ vạch '
                 'gạch chéo) biểu thị số lượng là:',
            'options': ['$5$', '$4$', '$6$', '$10$'],
            'answer': 0,
            'solution': 'Mỗi bó vạch kiểm đếm biểu thị số lượng là **$5$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bảng thống kê số con vật nuôi của bác Tư: Gà ($45$ con), Vịt ($30$ con), Ngỗng ($15$ con). '
                 'Bác Tư nuôi con vật nào ít nhất?',
            'options': ['Gà', 'Ngỗng', 'Vịt', 'Gà và Vịt'],
            'answer': 1,
            'solution': 'Vì $15 < 30 < 45$ nên **Ngỗng** được nuôi ít nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **5 bước**?',
            'options': ['$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm $\\rightarrow$ Lập bảng '
                        '$\\rightarrow$ Nhận xét',
                        'So sánh hàng trăm $\\rightarrow$ hàng chục $\\rightarrow$ hàng đơn vị'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 75: Thực hành thu thập, phân loại, đọc bảng '
                        'số liệu, **5 bước** được xác định bởi: Thu thập $\\rightarrow$ Phân loại '
                        '$\\rightarrow$ Kiểm đếm $\\rightarrow$ Lập bảng $\\rightarrow$ Nhận xét.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu**, nội dung/biểu thức Thu '
                 'thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm $\\rightarrow$ Lập bảng '
                 '$\\rightarrow$ Nhận xét là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phân tích số', 'Số tròn trăm, tròn nghìn', 'Cùng số chữ số', '5 bước'],
            'answer': 3,
            'solution': 'Trong Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu, biểu thức/quy tắc '
                        'Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm $\\rightarrow$ Lập bảng '
                        '$\\rightarrow$ Nhận xét chính là nội dung của **5 bước**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Theo bảng trên (Gà: $45$ con, Vịt: $30$ con, Ngỗng: $15$ con), số con Gà gấp mấy lần số '
                 'con Ngỗng?',
            'options': ['$3$ lần', '$2$ lần', '$30$ lần', '$4$ lần'],
            'answer': 0,
            'solution': 'Ta lấy $45 : 15 = 3\\text{ (lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu** (Chủ đề 15: Làm quen '
                 'với yếu tố thống kê, xác suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt '
                 'và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Chuyển được dữ liệu từ hình vẽ hoặc vạch kiểm đếm sang bảng số liệu.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu: '
                        'Chuyển được dữ liệu từ hình vẽ hoặc vạch kiểm đếm sang bảng số liệu.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Theo bảng trên (Gà: $45$ con, Vịt: $30$ con, Ngỗng: $15$ con), tổng số gia cầm '
                 'bác Tư nuôi là $90$ con."',
            'answer': True,
            'solution': 'Ta có $45 + 30 + 15 = 90$ (con) $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu**, quy tắc **5 bước** được '
                 'xác định bởi Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm $\\rightarrow$ Lập '
                 'bảng $\\rightarrow$ Nhận xét và áp dụng trực tiếp vào bài toán: “Khi kiểm đếm số quyển '
                 'truyện của tổ, bạn An ghi được $3$ cụm $5$ vạch và thêm $2$ vạch rời. Hỏi tổ của An có bao '
                 'nhiêu quyển truyện?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **5 bước** (Thu thập $\\rightarrow$ Phân loại '
                        '$\\rightarrow$ Kiểm đếm $\\rightarrow$ Lập bảng $\\rightarrow$ Nhận xét) là kiến '
                        'thức cốt lõi của Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu. Số quyển '
                        'truyện của tổ là: $5 \\times 3 + 2 = 17\\text{ (quyển)}$. Đáp số: **$17\\text{ '
                        'quyển}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu** để giải '
                 'quyết tình huống sau: Khi kiểm đếm số quyển truyện của tổ, bạn An ghi được $3$ cụm $5$ '
                 'vạch và thêm $2$ vạch rời. Hỏi tổ của An có bao nhiêu quyển truyện? Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Số quyển truyện của tổ là: $5 \\times 3 + 2 = 17\\text{ (quyển)}$. Đáp số: '
                        '**$17\\text{ quyển}$**.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 75: Thực hành thu thập, phân loại, đọc bảng số liệu: Số '
                        'quyển truyện của tổ là: $5 \\times 3 + 2 = 17\\text{ (quyển)}$.\n'
                        'Đáp số: **$17\\text{ quyển}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bảng điểm thi đua của $4$ tổ trong tuần: Tổ 1 được $22$ hoa điểm tốt, Tổ 2 được $25$ hoa, '
                 'Tổ 3 được $18$ hoa, Tổ 4 được $25$ hoa. Hỏi cả lớp đạt được tất cả bao nhiêu hoa điểm tốt?',
            'answer': ['90'],
            'unit': 'hoa',
            'solution': 'Tổng số hoa điểm tốt của cả lớp là: $22 + 25 + 18 + 25 = 90\\text{ (hoa)}$.\n'
                        'Đáp số: **$90\\text{ hoa}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd16-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 16: Ôn tập cuối năm',
  'context': 'SGK Toán 3 · Chủ đề 16: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000',
  'icon': '🔢',
  'description': 'Hệ thống hóa cách đọc, viết, phân tích cấu tạo số, so sánh, làm tròn số đến 100 000 và chữ '
                 'số La Mã.',
  'requirements': ['Đọc, viết, phân tích cấu tạo thập phân và so sánh thành thạo các số trong phạm vi '
                   '$100\\,000$.',
                   'Làm tròn được các số đến hàng chục, hàng trăm, hàng nghìn, hàng chục nghìn.',
                   'Đọc, viết đúng các chữ số La Mã từ $\\text{I}$ đến $\\text{XX}$.'],
  'definition': '- **Cấu tạo số**: $\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$.\n'
                '- **Làm tròn số**: nhìn chữ số ngay bên phải hàng cần làm tròn ($< 5$ làm tròn xuống, $\\ge '
                '5$ làm tròn lên).\n'
                '- **Chữ số La Mã**: $\\text{I} = 1, \\text{V} = 5, \\text{X} = 10$.',
  'theory': '### 1. So sánh và sắp xếp các số đến $100\\,000$\n'
            '- Ví dụ: $35\\,728 < 35\\,782$ vì cùng $35$ nghìn, $7$ trăm nhưng chữ số hàng chục $2 < 8$.\n'
            '### 2. Làm tròn số và chữ số La Mã\n'
            '- Làm tròn $47\\,500$ đến hàng chục nghìn được $50\\,000$.\n'
            '- Chữ số La Mã: $\\text{XVII} = 17$, $\\text{XIX} = 19$.',
  'formulas': [{'category': 'I. Tổng hợp về số đến 100 000',
                'items': [{'name': 'Làm tròn',
                           'formula': 'Chữ số bên phải $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên'},
                          {'name': 'Số La Mã',
                           'formula': '$\\text{IV} = 4, \\text{IX} = 9, \\text{XIV} = 14, \\text{XIX} = '
                                      '19$'}]}],
  'example': 'Cho số $68\\,374$. Hãy làm tròn số đó đến hàng trăm và đến hàng nghìn.',
  'example_answer': '- Làm tròn đến hàng trăm: chữ số hàng chục là $7 \\ge 5 \\rightarrow$ **$68\\,400$**.\n'
                    '- Làm tròn đến hàng nghìn: chữ số hàng trăm là $3 < 5 \\rightarrow$ **$68\\,000$**.',
  'real_life': '- Đọc bảng giá niêm yết hàng hóa và ước lượng chi phí mua sắm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số La Mã $\\text{XVII}$ viết bằng chữ số thường là:',
            'options': ['$12$', '$17$', '$15$', '$22$'],
            'answer': 1,
            'solution': 'Ta có $\\text{X} + \\text{V} + \\text{II} = 10 + 5 + 2 = 17$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $47\\,500$ đến hàng chục nghìn ta được:',
            'options': ['$40\\,000$', '$47\\,000$', '$50\\,000$', '$48\\,000$'],
            'answer': 2,
            'solution': 'Chữ số hàng nghìn là $7 \\ge 5$ nên làm tròn lên được **$50\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Làm tròn**?',
            'options': ['$\\text{IV} = 4, \\text{IX} = 9, \\text{XIV} = 14, \\text{XIX} = 19$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Chữ số bên phải $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 76: Ôn tập các số trong phạm vi 10 000, 100 '
                        '000, **Làm tròn** được xác định bởi: Chữ số bên phải $< 5 \\rightarrow$ xuống · '
                        '$\\ge 5 \\rightarrow$ lên.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000**, nội dung/biểu thức '
                 '$\\text{IV} = 4, \\text{IX} = 9, \\text{XIV} = 14, \\text{XIX} = 19$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Số La Mã', 'Làm tròn', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000, biểu thức/quy tắc '
                        '$\\text{IV} = 4, \\text{IX} = 9, \\text{XIV} = 14, \\text{XIX} = 19$ chính là nội '
                        'dung của **Số La Mã**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số gồm $7$ chục nghìn, $4$ trăm và $5$ đơn vị được viết là:',
            'options': ['$7\\,405$', '$70\\,405$', '$74\\,005$', '$70\\,450$'],
            'answer': 1,
            'solution': 'Ta có $70\\,000 + 400 + 5 = 70\\,405$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000** (Chủ đề 16: Ôn tập cuối '
                 'năm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đọc, viết, phân tích cấu tạo thập phân và so sánh thành thạo các số trong phạm vi '
                        '$100\\,000$.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000: Đọc, '
                        'viết, phân tích cấu tạo thập phân và so sánh thành thạo các số trong phạm vi '
                        '$100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$35\\,728 < 35\\,782$."',
            'answer': True,
            'solution': 'Cùng $35$ nghìn $7$ trăm, chữ số hàng chục $2 < 8$ nên $35\\,728 < 35\\,782$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000**, quy tắc **Làm tròn** được '
                 'xác định bởi Chữ số bên phải $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên và áp '
                 'dụng trực tiếp vào bài toán: “Cho số $68\\,374$. Hãy làm tròn số đó đến hàng trăm và đến '
                 'hàng nghìn.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Làm tròn** (Chữ số bên phải $< 5 \\rightarrow$ xuống '
                        '· $\\ge 5 \\rightarrow$ lên) là kiến thức cốt lõi của Bài 76: Ôn tập các số trong '
                        'phạm vi 10 000, 100 000. - Làm tròn đến hàng trăm: chữ số hàng chục là $7 \\ge 5 '
                        '\\rightarrow$ **$68\\,400$**. - Làm tròn đến hàng nghìn: chữ số hàng trăm là $3 < 5 '
                        '\\rightarrow$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000** để giải quyết '
                 'tình huống sau: Cho số $68\\,374$. Hãy làm tròn số đó đến hàng trăm và đến hàng nghìn. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        '- Làm tròn đến hàng trăm: chữ số hàng chục là $7 \\ge 5 \\rightarrow$ '
                        '**$68\\,400$**. - Làm tròn đến hàng nghìn: chữ số hàng trăm là $3 < 5 \\rightarrow$ '
                        '**$68\\,000$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000: - Làm '
                        'tròn đến hàng trăm: chữ số hàng chục là $7 \\ge 5 \\rightarrow$ **$68\\,400$**.\n'
                        '- Làm tròn đến hàng nghìn: chữ số hàng trăm là $3 < 5 \\rightarrow$ '
                        '**$68\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tròn nghìn liền sau của số $58\\,240$ (viết số liền).',
            'answer': ['59000'],
            'unit': None,
            'solution': 'Số $58\\,240$ nằm giữa hai số tròn nghìn $58\\,000$ và $59\\,000$, nên số tròn '
                        'nghìn liền sau là **$59000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd16-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 16: Ôn tập cuối năm',
  'context': 'SGK Toán 3 · Chủ đề 16: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000',
  'icon': '➕',
  'description': 'Củng cố kỹ năng cộng, trừ các số trong phạm vi 100 000, tìm thành phần chưa biết và giải '
                 'toán.',
  'requirements': ['Tính nhẩm và đặt tính cộng, trừ thành thạo các số trong phạm vi $100\\,000$.',
                   'Tìm được số hạng, số bị trừ, số trừ chưa biết.',
                   'Vận dụng tính chất giao hoán, kết hợp để tính nhanh và giải bài toán thực tế.'],
  'definition': '- **Tìm số hạng**: $\\text{Số hạng} = \\text{Tổng} - \\text{Số hạng kia}$.\n'
                '- **Tìm số bị trừ**: $\\text{Số bị trừ} = \\text{Hiệu} + \\text{Số trừ}$. **Tìm số trừ**: '
                '$\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu}$.',
  'theory': '### 1. Ôn tập tính nhẩm và tính thuận tiện\n'
            '- Ghép các cặp số tròn nghìn: $12\\,500 + 7\\,500 = 20\\,000$.\n'
            '### 2. Ôn tập giải toán cộng, trừ\n'
            '- Chú ý đọc kỹ từ khóa "nhiều hơn", "ít hơn", "còn lại", "tất cả".',
  'formulas': [{'category': 'I. Tìm thành phần chưa biết',
                'items': [{'name': 'Phép cộng', 'formula': '$x + a = b \\Rightarrow x = b - a$'},
                          {'name': 'Phép trừ',
                           'formula': '$x - a = b \\Rightarrow x = b + a$ · $a - x = b \\Rightarrow x = a - '
                                      'b$'}]}],
  'example': 'Tìm $x$ biết: a) $x - 18\\,500 = 31\\,500$; b) $64\\,000 - x = 28\\,000$.',
  'example_answer': 'a) Số bị trừ $x = 31\\,500 + 18\\,500 = 50\\,000$.\n'
                    'b) Số trừ $x = 64\\,000 - 28\\,000 = 36\\,000$.',
  'real_life': '- Lập dự toán thu chi cho chuyến dã ngoại của lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $45\\,000 + 35\\,000$ là:',
            'options': ['$70\\,000$', '$10\\,000$', '$80\\,000$', '$75\\,000$'],
            'answer': 2,
            'solution': 'Ta có $45$ nghìn $+ 35$ nghìn $= 80\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm số bị trừ $x$ biết $x - 14\\,200 = 25\\,800$:',
            'options': ['$11\\,600$', '$39\\,000$', '$30\\,000$', '$40\\,000$'],
            'answer': 3,
            'solution': 'Số bị trừ $x = 25\\,800 + 14\\,200 = 40\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Phép cộng**?',
            'options': ['$x + a = b \\Rightarrow x = b - a$',
                        '$x - a = b \\Rightarrow x = b + a$ · $a - x = b \\Rightarrow x = a - b$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi '
                        '100 000, **Phép cộng** được xác định bởi: $x + a = b \\Rightarrow x = b - a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000**, nội dung/biểu thức $x '
                 '- a = b \\Rightarrow x = b + a$ · $a - x = b \\Rightarrow x = a - b$ là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Phép cộng', 'Phép trừ', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 1,
            'solution': 'Trong Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000, biểu thức/quy tắc '
                        '$x - a = b \\Rightarrow x = b + a$ · $a - x = b \\Rightarrow x = a - b$ chính là '
                        'nội dung của **Phép trừ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $85\\,000 - (25\\,000 + 15\\,000)$ là:',
            'options': ['$55\\,000$', '$75\\,000$', '$45\\,000$', '$35\\,000$'],
            'answer': 2,
            'solution': 'Trong ngoặc trước: $25\\,000 + 15\\,000 = 40\\,000$; sau đó $85\\,000 - 40\\,000 = '
                        '45\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000** (Chủ đề 16: Ôn tập '
                 'cuối năm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.',
                        'Tính nhẩm và đặt tính cộng, trừ thành thạo các số trong phạm vi $100\\,000$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000: '
                        'Tính nhẩm và đặt tính cộng, trừ thành thạo các số trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong phép tính $50\\,000 - x = 18\\,000$, giá trị của $x$ là $68\\,000$."',
            'answer': False,
            'solution': 'Muốn tìm số trừ $x$, ta lấy $50\\,000 - 18\\,000 = 32\\,000$, không phải $68\\,000$ '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000**, quy tắc **Phép cộng** '
                 'được xác định bởi $x + a = b \\Rightarrow x = b - a$ và áp dụng trực tiếp vào bài toán: '
                 '“Tìm $x$ biết: a) $x - 18\\,500 = 31\\,500$; b) $64\\,000 - x = 28\\,000$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Phép cộng** ($x + a = b \\Rightarrow x = b - a$) là '
                        'kiến thức cốt lõi của Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000. a) '
                        'Số bị trừ $x = 31\\,500 + 18\\,500 = 50\\,000$. b) Số trừ $x = 64\\,000 - 28\\,000 '
                        '= 36\\,000$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000** để giải '
                 'quyết tình huống sau: Tìm $x$ biết: a) $x - 18\\,500 = 31\\,500$; b) $64\\,000 - x = '
                 '28\\,000$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['a) Số bị trừ $x = 31\\,500 + 18\\,500 = 50\\,000$. b) Số trừ $x = 64\\,000 - '
                        '28\\,000 = 36\\,000$.',
                        'Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000: a) '
                        'Số bị trừ $x = 31\\,500 + 18\\,500 = 50\\,000$.\n'
                        'b) Số trừ $x = 64\\,000 - 28\\,000 = 36\\,000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Thư viện trường có $24\\,500$ quyển sách, đầu năm học nhà trường nhập thêm $5\\,500$ quyển '
                 'sách mới. Hỏi thư viện có tất cả bao nhiêu quyển sách (viết số liền)?',
            'answer': ['30000'],
            'unit': 'quyển',
            'solution': 'Tổng số sách trong thư viện là: $24\\,500 + 5\\,500 = 30\\,000\\text{ (quyển)}$.\n'
                        'Đáp số: **$30000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd16-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 16: Ôn tập cuối năm',
  'context': 'SGK Toán 3 · Chủ đề 16: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000',
  'icon': '✖️',
  'description': 'Củng cố phép nhân, phép chia số có đến năm chữ số với số có một chữ số và tính giá trị '
                 'biểu thức.',
  'requirements': ['Đặt tính và tính đúng phép nhân, phép chia trong phạm vi $100\\,000$.',
                   'Tính đúng giá trị các biểu thức số kết hợp bốn phép tính.',
                   'Giải được bài toán có đến hai bước tính liên quan đến nhân, chia.'],
  'definition': '- **Tìm thừa số**: $\\text{Thừa số} = \\text{Tích} : \\text{Thừa số kia}$.\n'
                '- **Tìm số bị chia**: $\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia}$.\n'
                '- **Biểu thức số**: thực hiện trong ngoặc $()$ trước, sau đó đến nhân chia $\\times, :$ rồi '
                'đến cộng trừ $+, -$.',
  'theory': '### 1. Ôn tập tính giá trị biểu thức\n'
            '- Ví dụ: $(12\\,500 + 7\\,500) \\times 3 = 20\\,000 \\times 3 = 60\\,000$.\n'
            '- Ví dụ: $36\\,000 : 6 + 4\\,000 = 6\\,000 + 4\\,000 = 10\\,000$.\n'
            '### 2. Giải toán hai bước tính\n'
            '- Ví dụ: Tính tiền mua nhiều món hàng cùng loại rồi tính số tiền được trả lại.',
  'formulas': [{'category': 'I. Biểu thức và tìm x',
                'items': [{'name': 'Thứ tự phép tính',
                           'formula': '$() \\rightarrow \\times, : \\rightarrow +, -$'},
                          {'name': 'Tìm số bị chia',
                           'formula': '$x : a = b \\Rightarrow x = b \\times a$'}]}],
  'example': 'Mua $3$ quyển sách, mỗi quyển giá $24\\,500$ đồng. Đưa người bán tờ $100\\,000$ đồng thì được '
             'trả lại bao nhiêu đồng?',
  'example_answer': 'Tiền mua $3$ quyển sách là: $24\\,500 \\times 3 = 73\\,500\\text{ (đồng)}$.\n'
                    'Số tiền được trả lại là: $100\\,000 - 73\\,500 = 26\\,500\\text{ (đồng)}$.',
  'real_life': '- Tính tiền khi đi mua nhiều quyển sách hoặc nhiều vé xem xiếc cho cả gia đình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $36\\,000 : 6 + 4\\,000$ là:',
            'options': ['$3\\,600$', '$4\\,600$', '$40\\,000$', '$10\\,000$'],
            'answer': 3,
            'solution': 'Chia trước: $36\\,000 : 6 = 6\\,000$; cộng sau: $6\\,000 + 4\\,000 = 10\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $(12\\,500 + 7\\,500) \\times 3$ là:',
            'options': ['$60\\,000$', '$35\\,000$', '$20\\,000$', '$50\\,000$'],
            'answer': 0,
            'solution': 'Trong ngoặc trước: $20\\,000 \\times 3 = 60\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Thứ tự phép tính**?',
            'options': ['$x : a = b \\Rightarrow x = b \\times a$',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 78: Ôn tập phép nhân, phép chia trong phạm vi '
                        '100 000, **Thứ tự phép tính** được xác định bởi: $() \\rightarrow \\times, : '
                        '\\rightarrow +, -$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000**, nội dung/biểu thức $x '
                 ': a = b \\Rightarrow x = b \\times a$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thứ tự phép tính', 'Phân tích số', 'Tìm số bị chia', 'Số tròn trăm, tròn nghìn'],
            'answer': 2,
            'solution': 'Trong Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000, biểu thức/quy tắc '
                        '$x : a = b \\Rightarrow x = b \\times a$ chính là nội dung của **Tìm số bị chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thương của phép chia $45\\,045 : 9$ là:',
            'options': ['$505$', '$5\\,050$', '$5\\,500$', '$5\\,005$'],
            'answer': 3,
            'solution': 'Ta có $45 : 9 = 5$; hạ $0 \\rightarrow 0$; hạ $4 < 9 \\rightarrow 0$; hạ $5$ được '
                        '$45 : 9 = 5 \\rightarrow 5\\,005$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000** (Chủ đề 16: Ôn tập '
                 'cuối năm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đặt tính và tính đúng phép nhân, phép chia trong phạm vi $100\\,000$.',
                        'Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000: '
                        'Đặt tính và tính đúng phép nhân, phép chia trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tìm $x$ biết $x : 4 = 2\\,500$, ta được $x = 625$."',
            'answer': False,
            'solution': 'Số bị chia $x = 2\\,500 \\times 4 = 10\\,000$ (còn $625$ là $2\\,500 : 4$) '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000**, quy tắc **Thứ tự phép '
                 'tính** được xác định bởi $() \\rightarrow \\times, : \\rightarrow +, -$ và áp dụng trực '
                 'tiếp vào bài toán: “Mua $3$ quyển sách, mỗi quyển giá $24\\,500$ đồng. Đưa người bán tờ '
                 '$100\\,000$ đồng thì được trả lại bao nhiêu đồng?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự phép tính** ($() \\rightarrow \\times, : '
                        '\\rightarrow +, -$) là kiến thức cốt lõi của Bài 78: Ôn tập phép nhân, phép chia '
                        'trong phạm vi 100 000. Tiền mua $3$ quyển sách là: $24\\,500 \\times 3 = '
                        '73\\,500\\text{ (đồng)}$. Số tiền được trả lại là: $100\\,000 - 73\\,500 = '
                        '26\\,500\\text{ (đồng)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000** để giải '
                 'quyết tình huống sau: Mua $3$ quyển sách, mỗi quyển giá $24\\,500$ đồng. Đưa người bán tờ '
                 '$100\\,000$ đồng thì được trả lại bao nhiêu đồng? Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        'Tiền mua $3$ quyển sách là: $24\\,500 \\times 3 = 73\\,500\\text{ (đồng)}$. Số tiền '
                        'được trả lại là: $100\\,000 - 73\\,500 = 26\\,500\\text{ (đồng)}$.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000: '
                        'Tiền mua $3$ quyển sách là: $24\\,500 \\times 3 = 73\\,500\\text{ (đồng)}$.\n'
                        'Số tiền được trả lại là: $100\\,000 - 73\\,500 = 26\\,500\\text{ (đồng)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mua $3$ quyển sách, mỗi quyển giá $24\\,500$ đồng. Đưa người bán tờ $100\\,000$ đồng thì '
                 'được trả lại bao nhiêu đồng (viết số liền)?',
            'answer': ['26500'],
            'unit': 'đồng',
            'solution': 'Tiền mua sách: $24\\,500 \\times 3 = 73\\,500$ (đồng). Tiền trả lại: $100\\,000 - '
                        '73\\,500 = 26\\,500$ (đồng).\n'
                        'Đáp số: **$26500$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd16-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 16: Ôn tập cuối năm',
  'context': 'SGK Toán 3 · Chủ đề 16: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 79: Ôn tập hình học và đo lường',
  'icon': '📐',
  'description': 'Hệ thống hóa công thức chu vi, diện tích hình chữ nhật, hình vuông và các đơn vị đo lường '
                 'đã học.',
  'requirements': ['Tính đúng chu vi và diện tích của hình chữ nhật, hình vuông.',
                   'Chuyển đổi thành thạo các đơn vị đo độ dài ($\\text{mm}, \\text{cm}, \\text{dm}, '
                   '\\text{m}, \\text{km}$), khối lượng ($\\text{g}, \\text{kg}$), dung tích ($\\text{ml}, '
                   '\\text{l}$), thời gian.',
                   'Giải được bài toán thực tế về tính chiều dài hàng rào, diện tích mảnh đất.'],
  'definition': '- **Hình chữ nhật** (dài $a$, rộng $b$ cùng đơn vị): Chu vi $P = (a + b) \\times 2$; Diện '
                'tích $S = a \\times b$.\n'
                '- **Hình vuông** (cạnh $a$): Chu vi $P = a \\times 4$; Diện tích $S = a \\times a$.\n'
                '- **Đổi đơn vị**: $1\\text{ m} = 1\\,000\\text{ mm}$; $1\\text{ kg} = 1\\,000\\text{ g}$; '
                '$1\\text{ l} = 1\\,000\\text{ ml}$; $1\\text{ giờ} = 60\\text{ phút}$.',
  'theory': '### 1. Bài toán thực tế về chu vi và diện tích\n'
            '- Khi rào xung quanh mảnh đất có chừa lối cổng: $\\text{Độ dài hàng rào} = \\text{Chu vi mảnh '
            'đất} - \\text{Độ rộng cổng}$.\n'
            '### 2. Ôn tập đo lường\n'
            '- Luôn kiểm tra các số đo đã cùng đơn vị chưa trước khi áp dụng công thức.',
  'formulas': [{'category': 'I. Hình chữ nhật & Hình vuông',
                'items': [{'name': 'Hình chữ nhật', 'formula': '$P = (a + b) \\times 2$ · $S = a \\times b$'},
                          {'name': 'Hình vuông', 'formula': '$P = a \\times 4$ · $S = a \\times a$'}]},
               {'category': 'II. Đơn vị đo',
                'items': [{'name': 'Quan hệ 1 000',
                           'formula': '$1\\text{ km} = 1\\,000\\text{ m}$ · $1\\text{ kg} = 1\\,000\\text{ '
                                      'g}$ · $1\\text{ l} = 1\\,000\\text{ ml}$'}]}],
  'example': 'Một mảnh đất hình chữ nhật dài $25\\text{ m}$, rộng $12\\text{ m}$. Người ta làm hàng rào xung '
             'quanh mảnh đất và chừa $2\\text{ m}$ làm cổng. Tính độ dài hàng rào.',
  'example_answer': 'Chu vi mảnh đất hình chữ nhật là: $(25 + 12) \\times 2 = 74\\text{ (m)}$.\n'
                    'Độ dài hàng rào là: $74 - 2 = 72\\text{ (m)}$.',
  'real_life': '- Tính diện tích nền phòng học và chiều dài tường bao quanh vườn trường.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Diện tích của hình vuông có cạnh $9\\text{ cm}$ là:',
            'options': ['$81\\text{ cm}^2$', '$36\\text{ cm}^2$', '$18\\text{ cm}^2$', '$81\\text{ cm}$'],
            'answer': 0,
            'solution': 'Diện tích hình vuông: $S = 9 \\times 9 = 81\\text{ (cm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $5\\text{ l} = \\dots\\text{ ml}$?',
            'options': ['$50$', '$5\\,000$', '$500$', '$50\\,000$'],
            'answer': 1,
            'solution': 'Vì $1\\text{ l} = 1\\,000\\text{ ml}$ nên $5\\text{ l} = 5\\,000\\text{ ml}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 79: Ôn tập hình học và đo lường**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Hình chữ nhật**?',
            'options': ['$P = a \\times 4$ · $S = a \\times a$',
                        '$1\\text{ km} = 1\\,000\\text{ m}$ · $1\\text{ kg} = 1\\,000\\text{ g}$ · $1\\text{ '
                        'l} = 1\\,000\\text{ ml}$',
                        '$P = (a + b) \\times 2$ · $S = a \\times b$',
                        '$\\overline{abc} = a00 + b0 + c$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 79: Ôn tập hình học và đo lường, **Hình chữ '
                        'nhật** được xác định bởi: $P = (a + b) \\times 2$ · $S = a \\times b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 79: Ôn tập hình học và đo lường**, nội dung/biểu thức $P = a \\times 4$ · $S = '
                 'a \\times a$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hình chữ nhật', 'Quan hệ 1 000', 'Phân tích số', 'Hình vuông'],
            'answer': 3,
            'solution': 'Trong Bài 79: Ôn tập hình học và đo lường, biểu thức/quy tắc $P = a \\times 4$ · $S '
                        '= a \\times a$ chính là nội dung của **Hình vuông**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hình chữ nhật có chiều dài $15\\text{ m}$, chiều rộng $8\\text{ m}$ thì có chu vi là:',
            'options': ['$46\\text{ m}$', '$120\\text{ m}$', '$23\\text{ m}$', '$46\\text{ m}^2$'],
            'answer': 0,
            'solution': 'Chu vi hình chữ nhật: $(15 + 8) \\times 2 = 46\\text{ (m)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 79: Ôn tập hình học và đo lường** (Chủ đề 16: Ôn tập cuối năm), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Tính đúng chu vi và diện tích của hình chữ nhật, hình vuông.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 79: Ôn tập hình học và đo lường: Tính đúng chu vi và '
                        'diện tích của hình chữ nhật, hình vuông.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Một hình vuông có chu vi $32\\text{ cm}$ thì có diện tích là $64\\text{ '
                 'cm}^2$."',
            'answer': True,
            'solution': 'Cạnh hình vuông là $32 : 4 = 8\\text{ (cm)}$, diện tích là $8 \\times 8 = 64\\text{ '
                        '(cm}^2\\text{)}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 79: Ôn tập hình học và đo lường**, quy tắc **Hình chữ nhật** được xác định bởi '
                 '$P = (a + b) \\times 2$ · $S = a \\times b$ và áp dụng trực tiếp vào bài toán: “Một mảnh '
                 'đất hình chữ nhật dài $25\\text{ m}$, rộng $12\\text{ m}$. Người ta làm hàng rào xung '
                 'quanh mảnh đất và chừa $2\\text{ m}$ làm cổng. T...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Hình chữ nhật** ($P = (a + b) \\times 2$ · $S = a '
                        '\\times b$) là kiến thức cốt lõi của Bài 79: Ôn tập hình học và đo lường. Chu vi '
                        'mảnh đất hình chữ nhật là: $(25 + 12) \\times 2 = 74\\text{ (m)}$. Độ dài hàng rào '
                        'là: $74 - 2 = 72\\text{ (m)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 79: Ôn tập hình học và đo lường** để giải quyết tình huống sau: '
                 'Một mảnh đất hình chữ nhật dài $25\\text{ m}$, rộng $12\\text{ m}$. Người ta làm hàng rào '
                 'xung quanh mảnh đất và chừa $2\\text{ m}$ làm cổng. Tính độ dài hàng rào. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Chu vi mảnh đất hình chữ nhật là: $(25 + 12) \\times 2 = 74\\text{ (m)}$. Độ dài '
                        'hàng rào là: $74 - 2 = 72\\text{ (m)}$.',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 79: Ôn tập hình học và đo lường: Chu vi mảnh đất hình '
                        'chữ nhật là: $(25 + 12) \\times 2 = 74\\text{ (m)}$.\n'
                        'Độ dài hàng rào là: $74 - 2 = 72\\text{ (m)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mảnh đất hình chữ nhật dài $25\\text{ m}$, rộng $12\\text{ m}$. Người ta rào xung '
                 'quanh mảnh đất đó và chừa $2\\text{ m}$ làm cổng. Hỏi hàng rào dài bao nhiêu mét?',
            'answer': ['72'],
            'unit': 'm',
            'solution': 'Chu vi mảnh đất: $(25 + 12) \\times 2 = 74\\text{ (m)}$. Hàng rào dài: $74 - 2 = '
                        '72\\text{ (m)}$.\n'
                        'Đáp số: **$72\\text{ m}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l3-cd16-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 16: Ôn tập cuối năm',
  'context': 'SGK Toán 3 · Chủ đề 16: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung',
  'icon': '🏁',
  'description': 'Ôn tập đọc bảng số liệu thống kê, mô tả khả năng xảy ra của sự kiện và giải toán tổng hợp '
                 'cuối lớp 3.',
  'requirements': ['Đọc, phân tích và tính toán thành thạo từ bảng số liệu thống kê.',
                   'Xác định đúng các khả năng xảy ra của một sự kiện ngẫu nhiên.',
                   'Giải được các bài toán tổng hợp toàn chương trình Toán lớp 3.'],
  'definition': '- **Bảng số liệu**: giúp tra cứu nhanh số lượng từng loại, so sánh nhiều nhất/ít nhất và '
                'tính tổng.\n'
                '- **Khả năng xảy ra**: liệt kê đầy đủ các kết quả có thể xuất hiện trong $1$ lần thực hiện '
                'thí nghiệm.',
  'theory': '### 1. Ôn tập thống kê và xác suất\n'
            '- Đọc kỹ hàng và cột của bảng số liệu để lấy đúng số liệu cần tính.\n'
            '- Phân biệt sự kiện "có thể xảy ra", "chắc chắn xảy ra" và "không thể xảy ra".\n'
            '### 2. Tổng kết chương trình Toán lớp 3\n'
            '- Nắm vững các số đến $100\\,000$, bốn phép tính, biểu thức số, chu vi – diện tích hình chữ '
            'nhật, hình vuông và các đơn vị đo.',
  'formulas': [{'category': 'I. Tổng hợp kiến thức',
                'items': [{'name': 'Thống kê',
                           'formula': 'Đọc bảng $\\rightarrow$ So sánh (lớn nhất, bé nhất) $\\rightarrow$ '
                                      'Tính tổng, hiệu'},
                          {'name': 'Giải toán 2 bước',
                           'formula': 'Tìm đại lượng trung gian $\\rightarrow$ Tìm đại lượng đề bài hỏi'}]}],
  'example': 'Bảng số sách quyên góp của 3 lớp: Lớp 3A ($120$ quyển), Lớp 3B ($135$ quyển), Lớp 3C ($145$ '
             'quyển). Tính tổng số sách cả 3 lớp quyên góp được.',
  'example_answer': 'Tổng số sách cả $3$ lớp quyên góp được là: $120 + 135 + 145 = 400\\text{ (quyển)}$.\n'
                    'Đáp số: **$400\\text{ quyển}$**.',
  'real_life': '- Tổng kết thành tích học tập cuối năm học và lập kế hoạch cho kỳ nghỉ hè.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bảng số liệu ghi số cây hoa trong vườn trường: Hoa hồng ($45$ cây), Hoa cúc ($60$ cây), '
                 'Hoa đồng tiền ($35$ cây). Loại hoa có nhiều cây nhất là:',
            'options': ['Hoa hồng', 'Hoa cúc', 'Hoa đồng tiền', 'Hoa hồng và hoa cúc'],
            'answer': 1,
            'solution': 'Vì $60 > 45 > 35$ nên **Hoa cúc** có nhiều cây nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hộp có $1$ quả bóng xanh, $1$ quả bóng vàng và $1$ quả bóng trắng. Lấy ngẫu nhiên '
                 '$1$ quả bóng, có mấy khả năng xảy ra về màu của quả bóng?',
            'options': ['$1$ khả năng', '$2$ khả năng', '$3$ khả năng', '$4$ khả năng'],
            'answer': 2,
            'solution': 'Có **$3$ khả năng**: bóng xanh, bóng vàng hoặc bóng trắng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Thống kê**?',
            'options': ['Tìm đại lượng trung gian $\\rightarrow$ Tìm đại lượng đề bài hỏi',
                        '$\\overline{abc} = a00 + b0 + c$',
                        '$10 \\text{ chục} = 100$ · $10 \\text{ trăm} = 1\\,000$',
                        'Đọc bảng $\\rightarrow$ So sánh (lớn nhất, bé nhất) $\\rightarrow$ Tính tổng, hiệu'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra '
                        'và ôn tập chung, **Thống kê** được xác định bởi: Đọc bảng $\\rightarrow$ So sánh '
                        '(lớn nhất, bé nhất) $\\rightarrow$ Tính tổng, hiệu.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung**, nội dung/biểu '
                 'thức Tìm đại lượng trung gian $\\rightarrow$ Tìm đại lượng đề bài hỏi là quy tắc hoặc công '
                 'thức của mục nào sau đây?',
            'options': ['Giải toán 2 bước', 'Thống kê', 'Phân tích số', 'Số tròn trăm, tròn nghìn'],
            'answer': 0,
            'solution': 'Trong Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung, biểu '
                        'thức/quy tắc Tìm đại lượng trung gian $\\rightarrow$ Tìm đại lượng đề bài hỏi chính '
                        'là nội dung của **Giải toán 2 bước**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Theo bảng cây hoa ở trên (Hoa hồng: $45$, Hoa cúc: $60$, Hoa đồng tiền: $35$), tổng số cây '
                 'hoa trong vườn trường là:',
            'options': ['$130$ cây', '$140$ cây', '$105$ cây', '$150$ cây'],
            'answer': 1,
            'solution': 'Tổng số cây hoa là: $45 + 60 + 35 = 140\\text{ (cây)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung** (Chủ đề 16: '
                 'Ôn tập cuối năm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Đọc, viết thành thạo các số có đến ba chữ số trong phạm vi 1 000.',
                        'Phân tích được số có ba chữ số thành tổng các trăm, chục, đơn vị.',
                        'Đọc, phân tích và tính toán thành thạo từ bảng số liệu thống kê.',
                        'So sánh và sắp xếp được các số trong phạm vi 1 000 theo thứ tự.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập '
                        'chung: Đọc, phân tích và tính toán thành thạo từ bảng số liệu thống kê.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong túi chỉ có các viên bi màu đỏ. Khi lấy ngẫu nhiên $1$ viên bi từ túi thì '
                 'chắc chắn lấy được viên bi màu đỏ."',
            'answer': True,
            'solution': 'Vì trong túi chỉ toàn bi màu đỏ nên chắc chắn lấy được bi đỏ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung**, quy tắc '
                 '**Thống kê** được xác định bởi Đọc bảng $\\rightarrow$ So sánh (lớn nhất, bé nhất) '
                 '$\\rightarrow$ Tính tổng, hiệu và áp dụng trực tiếp vào bài toán: “Bảng số sách quyên góp '
                 'của 3 lớp: Lớp 3A ($120$ quyển), Lớp 3B ($135$ quyển), Lớp 3C ($145$ quyển). Tính tổng số '
                 'sách cả 3 lớp quyên góp đượ...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thống kê** (Đọc bảng $\\rightarrow$ So sánh (lớn '
                        'nhất, bé nhất) $\\rightarrow$ Tính tổng, hiệu) là kiến thức cốt lõi của Bài 80, 81: '
                        'Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung. Tổng số sách cả $3$ lớp quyên '
                        'góp được là: $120 + 135 + 145 = 400\\text{ (quyển)}$. Đáp số: **$400\\text{ '
                        'quyển}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập chung** để '
                 'giải quyết tình huống sau: Bảng số sách quyên góp của 3 lớp: Lớp 3A ($120$ quyển), Lớp 3B '
                 '($135$ quyển), Lớp 3C ($145$ quyển). Tính tổng số sách cả 3 lớp quyên góp được. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $806 = 800 + 6$ (gồm $8$ trăm, $0$ chục, $6$ đơn vị). Vì chữ số hàng trăm $8 '
                        '> 7$ nên **$806 > 798$**.',
                        '- $468 + 325$: $8 + 5 = 13$ (viết $3$ nhớ $1$); $6 + 2 + 1 = 9$; $4 + 3 = 7$ '
                        '$\\rightarrow$ **$793$**. - $750 - 236$: $10 - 6 = 4$ (viết $4$ nhớ $1$); $5 - (3 + '
                        '1) = 1$...',
                        'Áp dụng quy tắc tìm số trừ: $\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu} = 85 '
                        '- 39 = 46$. Thử lại: $85 - 46 = 39$ (đúng). Vậy số cần tìm là **$46$**.',
                        'Tổng số sách cả $3$ lớp quyên góp được là: $120 + 135 + 145 = 400\\text{ (quyển)}$. '
                        'Đáp số: **$400\\text{ quyển}$**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 80, 81: Ôn tập bảng số liệu, khả năng xảy ra và ôn tập '
                        'chung: Tổng số sách cả $3$ lớp quyên góp được là: $120 + 135 + 145 = 400\\text{ '
                        '(quyển)}$.\n'
                        'Đáp số: **$400\\text{ quyển}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng buổi sáng bán được $12\\,400\\text{ kg}$ xi măng, buổi chiều bán được gấp đôi '
                 'buổi sáng. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam xi măng (viết số liền)?',
            'answer': ['37200'],
            'unit': 'kg',
            'solution': 'Buổi chiều bán được: $12\\,400 \\times 2 = 24\\,800\\text{ (kg)}$. Cả hai buổi bán '
                        'được: $12\\,400 + 24\\,800 = 37\\,200\\text{ (kg)}$.\n'
                        'Đáp số: **$37200$**.',
            'alt': None,
            'note': None}]}]
